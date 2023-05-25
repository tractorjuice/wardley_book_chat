# Have an AI Chat with Simon Wardley's Book
Chat with Simon Wardley's Book on Wardley Mapping

Chat with Simon Wardley's Book is an AI-based application that allows you to interact with the content of Simon Wardley's book using GPT-4 model and OpenAI API. It utilizes the Streamlit framework to present an interactive user interface, making it easy for users to ask questions and get answers.

## Features
Querying the book using natural language and AI.
Incorporates OpenAI's GPT-4 model for generating answers.
Uses Streamlit for a user-friendly UI.
How to Run
Clone the repository.
Set the OpenAI API key in the Streamlit secrets manager.
Ensure you have the index.faiss and index.pkl files in the data_store directory.
Run the streamlit app using the command streamlit run app.py (replace app.py with the correct filename).

## Dependencies
To run this code, you need the following Python packages:

- os
- re
- openai
- streamlit
- langchain
- FAISS

You can install these dependencies via pip:

shell
Copy code
pip install openai streamlit langchain faiss-cpu

Note: Replace faiss-cpu with faiss-gpu if you are using a GPU.

### API Keys
The application uses the OpenAI API. You will need to obtain an API key from OpenAI and set it in the Streamlit secrets manager.

### Data Store
The application uses a local datastore located in the data_store directory. It needs the index.faiss and index.pkl files to be present in this directory. If they are missing, you will get an error message.

## Using the Application
Once the application is running, you can use the input box labeled "Question for the book?" to ask your question. After entering your question, the application will generate an answer and display it on the screen.

## Developer Info
This application is developed by Mark Craddock. You can follow him on Twitter at https://twitter.com/mcraddock.

## Version Info
The current version of this application is 0.1.4.

## Disclaimer
This application is not optimized and may run out of OpenAI credits. Also, Wardley Mapping is provided courtesy of Simon Wardley and is licensed under Creative Commons Attribution Share-Alike.

Please use responsibly and in accordance with OpenAI's use-case policy.

## License
This project is open source, 
