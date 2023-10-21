# Have an AI Chat with Simon Wardley's Book

Engage in a dynamic conversation with the content of Simon Wardley's book on Wardley Mapping.

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/tractorjuice/wardley_book_chat)

"Chat with Simon Wardley's Book" is an AI-driven application powered by the GPT-4 model and OpenAI API. Using the Streamlit framework, it offers a responsive interface, enabling users to pose questions and receive insightful responses.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://wardley-book-chat.streamlit.app/)

## Features

- Interact with the book through natural language and AI capabilities.
- Leverage OpenAI's GPT-4 model for articulate answers.
- Streamlit integration ensures an intuitive user experience.

## How to Run
1. Clone the repository.\
2. Set the OpenAI API key in the Streamlit secrets manager.\
3. Ensure you have the index.faiss and index.pkl files in the data_store directory.\
4. Run the streamlit app using the command streamlit run main.py.\

## Dependencies
To run this code, you need the following Python packages:

- os
- re
- openai
- streamlit
- langchain
- FAISS

### API Keys
The application uses the OpenAI API. You will need to obtain an API key from OpenAI and set it in the Streamlit secrets manager.

### Data Management

The application harnesses a local data store situated in the `data_store` directory. Both `index.faiss` and `index.pkl` files are mandatory; otherwise, the application will return an error.

## Using the Application
Once the application is running, you can use the input box labeled "Question for the book?" to ask your question. After entering your question, the application will generate an answer and display it on the screen.

## About the Developer

Mark Craddock is the brain behind this application. Connect with him and stay updated on [Twitter](https://twitter.com/mcraddock).

## Version Info
The current version of this application is 0.1.4.

## Disclaimer

This application, while feature-rich, may exhaust OpenAI credits. Wardley Mapping content is a gracious provision by Simon Wardley and holds a Creative Commons Attribution Share-Alike license. Always adhere to OpenAI's use-case guidelines and employ this application responsibly.

Please use responsibly and in accordance with OpenAI's use-case policy.

## License

This project is licensed under Creative Commons Attribution Share-Alike.
