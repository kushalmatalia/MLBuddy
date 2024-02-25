# MLBuddy 🤖
_MLBuddy_ : Your Personalized Machine Learning Study Companion

The Machine Learning PDF Bot is a Streamlit web application designed to help users extract information from Machine Learning (ML) PDF documents. By uploading a PDF file, users can ask questions about the content of the PDF, and the bot will provide answers based on the text extracted from the document. The bot uses a combination of text processing techniques and machine learning models to understand and answer questions related to the PDF content.

### Installation : from repo
1. Download the zip file of the main branch
2. Unzip to the desried location and open in the code editor

### Execution : after downloading code from repo
1. Create a new .env file at the loaction and add the command: OPENAI_API_KEY=_______
2. Add the API key generated for your account. For time being, provided with mine.
3. Navigate to the app.py file
4. Open a new terminal at this location
5. Execute the command - 'streamlit run app.py'
6. A new port will be launched at url - example: (http://localhost:8501/)
7. Upload any pdf of Machine Learning - Ex: machine_learning_guide1, which is provided
8. Start asking question, wait for the Bot to respond, and again ask question using the same input field, and the conversation history will be visible on the left side panel


### Key Features
_PDF Upload_: Users can upload a PDF file containing ML content.

_Question-Answering_: Users can ask questions about the PDF content, and the bot will provide relevant answers.

_Interactive Chat_: The bot maintains a conversation history and displays it in the sidebar for reference.

### User Instructions
(https://mlbuddy.streamlit.app/)

_Upload PDF_: Click on the "Upload your PDF" button and select a PDF file containing ML content.

_Ask Question_: Enter a question about the PDF content in the text input field under "Question: Ask a question about your PDF:".

_View Answer_: The bot will provide an answer based on the content of the PDF.

_Conversation History_: The conversation history is displayed in the sidebar for reference.

### Technical Innovations
The application utilizes several key technologies:

_PyPDF2_: Used to extract text from PDF files.

_langchain_: A library for natural language processing tasks, including text splitting, embeddings, and question-answering.

_Streamlit_: Provides the web interface for the application, allowing for easy interaction with users.

The application leverages Langchain's Question-Answering capabilities, which use OpenAI's large language models (LLMs) to understand and respond to user questions. This integration enables the bot to provide accurate and relevant answers based on the content of the PDF document.

### Future Application
1. Adding download functionality to download the entire conversation history in user specified format
2. Adding functionality to take input in any format ex: pdf, txt, md, word, etc
3. Adding functionality to even process images

### Demo
![image](https://github.com/kushalmatalia/MLBuddy/assets/42527900/10e595c9-503f-4d79-be74-d2b1fe076949)
![image](https://github.com/kushalmatalia/MLBuddy/assets/42527900/be071ec2-93e2-408e-9199-3ad5abb43ec4)

### Acknowledgments
The Machine Learning PDF Bot utilizes the following libraries and resources:

_Streamlit_: For building the interactive web application.

_PyPDF2_: For extracting text from PDF files.

_Langchain_: For natural language processing capabilities, including question-answering.

The application also acknowledges the use of OpenAI's large language models for powering the question-answering functionality.
