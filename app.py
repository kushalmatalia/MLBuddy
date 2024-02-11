# Import necessary libraries
from dotenv import load_dotenv  # Importing the function to load environment variables
import streamlit as st  # Importing Streamlit library
from PyPDF2 import PdfReader  # Importing PdfReader class from PyPDF2 library
from langchain.text_splitter import CharacterTextSplitter  # Importing CharacterTextSplitter class from langchain library
from langchain.embeddings.openai import OpenAIEmbeddings  # Importing OpenAIEmbeddings class from langchain library
from langchain.vectorstores import FAISS  # Importing FAISS class from langchain library
from langchain.chains.question_answering import load_qa_chain  # Importing load_qa_chain function from langchain library
from langchain.llms import OpenAI  # Importing OpenAI class from langchain library
from langchain.callbacks import get_openai_callback  # Importing get_openai_callback function from langchain library

# Define a class to manage session state
class SessionState:
    def __init__(self):
        # Initialize the question counter for the session
        self.question_counter = 1

# Initialize session state
session_state = SessionState()

# Initialize conversation buffer if it doesn't exist
if 'conversation_buffer' not in st.session_state:
    # Create an empty conversation buffer to store questions and answers
    st.session_state.conversation_buffer = []

# Main function to run the Streamlit app
def main():
    # Load environment variables from .env file
    load_dotenv()
    
    # Set the page configuration for the app
    st.set_page_config(page_title="Talking to your Machine Learning PDF", page_icon=":page_with_curl:")
    
    # Display the header of the app
    st.header("Hello! I'm the Machine Learning PDF Bot 🤖")
    st.write("I can help you with your Machine Learning PDF documents. Please upload a PDF file.")

    # Allow the user to upload a PDF file
    pdf = st.file_uploader("Upload your PDF", type="pdf")
    
    # If a PDF file is uploaded, extract text and perform question-answering
    if pdf is not None:
        # Check if the knowledge base has been initialized
        if not hasattr(session_state, 'knowledge_base'):
            # Read the PDF file and extract text from it
            pdf_reader = PdfReader(pdf)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
                
            # Split the text into smaller chunks for processing
            text_splitter = CharacterTextSplitter(
                separator="\n",
                chunk_size=1000,
                chunk_overlap=200,
                length_function=len
            )
            chunks = text_splitter.split_text(text)
            
            # Create embeddings from the text chunks using OpenAI
            embeddings = OpenAIEmbeddings()
            knowledge_base = FAISS.from_texts(chunks, embeddings)

        st.write("Hello! I'm the PDF Bot 🤖")

        # Section for the active chat session
        st.subheader("Active chat")
        # Ask the user to input a question about the PDF
        user_question = st.text_input(f"Question: Ask a question about your PDF:")
        
        # If the user has entered a question, perform question-answering
        if user_question:
            # Search for relevant documents based on the user's question
            docs = knowledge_base.similarity_search(user_question)
            llm = OpenAI()
            chain = load_qa_chain(llm, chain_type="stuff")
            with get_openai_callback() as cb:
                # Get the response to the user's question using question-answering
                response = chain.run(input_documents=docs, question=user_question)
            
            # Display the response from the PDF
            st.write("PDF Bot:", response)
            
            # Increment the question counter for this session
            session_state.question_counter += 1
            
            # Add the user question and bot response to the conversation buffer
            st.session_state.conversation_buffer.append(("User", user_question))
            st.session_state.conversation_buffer.append(("PDF Bot", response))
            
            # Display the conversation history in the sidebar
            if len(st.session_state.conversation_buffer) > 2:
                st.sidebar.subheader("Conversation History")
                for speaker, message in st.session_state.conversation_buffer:
                    st.sidebar.write(f"{speaker}: {message}")

# Run the main function if the script is executed directly
if __name__ == '__main__':
    main()
