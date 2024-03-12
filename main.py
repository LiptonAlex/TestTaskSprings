import os
import cassio
from langchain.vectorstores.cassandra import Cassandra
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain_openai import OpenAI
from langchain_openai import OpenAIEmbeddings
from datasets import load_dataset
from PyPDF2 import PdfReader
from typing_extensions import Concatenate
from langchain.text_splitter import CharacterTextSplitter
from dotenv import load_dotenv


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
astra_db_token = os.getenv("ASTRA_DB_APP_TOKEN")
astra_db_id = os.getenv("ASTRA_DB_ID")


pdfreader = PdfReader("CoffeeB_Manual Globe_EN_10.08.2022.pdf")

raw_text = ""
for i, page in enumerate(pdfreader.pages):
  content = page.extract_text()
  if content:
    raw_text += content


cassio.init(token=astra_db_token, database_id=astra_db_id)

llm = OpenAI(openai_api_key=api_key)
embedding = OpenAIEmbeddings(openai_api_key=api_key)

astra_vector_store = Cassandra(
  embedding=embedding,
  table_name="TestTask",
  session=None,
  keyspace=None,
)

text_splitter = CharacterTextSplitter(
    separator = "\n",
    chunk_size = 800,
    chunk_overlap = 200,
    length_function = len,
)
texts = text_splitter.split_text(raw_text)

astra_vector_store.add_texts(texts[:50])


astra_vector_index = VectorStoreIndexWrapper(vectorstore=astra_vector_store)

first_question = True
while True:
    if first_question:
        query_text = input("\nEnter your question (or type 'quit' to exit): ").strip()
    else:
        query_text = input("\nWhat's your next question (or type 'quit' to exit): ").strip()

    if query_text.lower() == "quit":
        break

    if query_text == "":
        continue

    first_question = False

    print("\nQUESTION: \"%s\"" % query_text)
    answer = astra_vector_index.query(query_text, llm=llm).strip()
    print("ANSWER: \"%s\"\n" % answer)



