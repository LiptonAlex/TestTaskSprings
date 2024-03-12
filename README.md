# TestTaskSprings
Creating AI that reads PDFs and answers your questions.


To use this app you need to install libs from *requirements.txt*.


In folder with *main.py* create an *.env* file that include your ***OPENAI_API_KEY*** , ***ASTRA_DB_APP_TOKEN*** , ***ASTRA_DB_ID*** (this app is using Astra Vector Database).

Also you need to have PDFs in same folder.


To switch your processed PDF file- you need to change field in method of variable *pdfreader* to full name of your document (for example: *pdfreader = PdfReader("stripe-2022-update.pdf"*)).


For exiting app - write *quit*.
Example of work:
![image](https://github.com/LiptonAlex/TestTaskSprings/assets/99798521/67386aa0-8a72-4ff3-ae1f-32077d348c87)
