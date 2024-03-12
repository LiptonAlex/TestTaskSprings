# TestTaskSprings
Creating AI that reads PDFs and answers your questions.


To use this app you need to install libs from *requirements.txt*.

Or write next command in terminal:
*pip install langchain openai cassio datasets tiktoken PyPDF2 dotenv*


In folder with *main.py* create a *.env* file that includes your ***OPENAI_API_KEY*** , ***ASTRA_DB_APP_TOKEN*** , ***ASTRA_DB_ID*** (this app is using Astra Vector Database).

Also, you need to have PDFs in the same folder.


To switch your processed PDF file- you need to change field in method of variable *pdfreader* to full name of your document (for example: *pdfreader = PdfReader("stripe-2022-update.pdf"*)).


To exit app - write *quit*.

Example of work:
![image](https://github.com/LiptonAlex/TestTaskSprings/assets/99798521/06f8f4c4-6574-4b85-a320-e42a5a1e20ad)


