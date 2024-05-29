# deepvisiontech-hack
# COVID-19 Chatbot - Stay Informed
# Team Members :
  Sathish Kumar P
  Santhosh P
  Sathiya Narayanan V

Intoduction

This is a Python-based chatbot designed to provide users with information about COVID-19. It leverages Artificial Intelligence (AI) and Natural Language Understanding (NLU) to answer your questions in a conversational way.

Features

o	Informative: Get answers to frequently asked questions (FAQs) about COVID-19, including:

o	Symptoms

o	Preventive measures

o	Vaccination information

o	Test centers (if data is integrated)

o	Latest updates (if data is integrated)

o	User-friendly: Interact with the chatbot in a natural language, just like having a conversation.

o	Multilingual support (optional): Enable the chatbot to answer questions in multiple languages (requires additional libraries and data).

Requirements

•	Python (version 3.x recommended)

•	Essential libraries:

o	rasa (core framework for building chatbots)

o	nltk (Natural Language Toolkit for NLP tasks)

o	NumPy (numerical computing library)


o	pandas (data analysis library)

o	matplotlib (data visualization library) (optional, for data representation)

o	Additional libraries for specific functionalities:

o	requests (to query external APIs for COVID-19 data)

o	langdetect (for language detection) (multilingual support)

o	Training data: A dataset of COVID-19 related questions and answers. You can create your own or use publicly available datasets.

Installation

1.	Ensure you have Python installed (https://www.python.org/downloads/).
2.	Open a terminal or command prompt.
3.	Install the required libraries using pip:

Bash

  pip install rasa nltk numpy pandas matplotlib requests langdetect (optional for multilingual)
Use code with caution.

Training

1.	Create a training data file in Rasa's Dialogue Data Format (.yml or .json).
2.	Provide sample conversations with questions and corresponding informative answers.
3.	Use Rasa tools to train the chatbot model on your prepared data.

Running the Chatbot

1.	Refer to Rasa's documentation for specific instructions on launching the chatbot server.
2.	Once the server is running, you can interact with the chatbot through a command-line interface or integrate it into a web application.

Disclaimer

This chatbot is intended for informational purposes only and should not be taken as medical advice. Always consult with a healthcare professional for any COVID-19 related concerns.

