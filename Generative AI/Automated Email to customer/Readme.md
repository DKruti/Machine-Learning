# Customer Support System Automated Email Response

## Introduction

The Customer Support System Automated Email Response is a Python web application built using Flask and powered by OpenAI's GPT-3.5 model. It provides an automated solution for generating email responses to customer comments about electronic products. This project streamlines the customer support process by generating personalized email responses based on the sentiment and content of the customer's comment.

## Design
<img width="893" alt="Screen Shot 2023-10-04 at 4 06 11 PM" src="https://github.com/DKruti/Machine-Learning/assets/120690177/d3628bf9-48f5-46b2-a65e-2ecbe978eda6">

### Rate Limiting
The application incorporates a rate limiting mechanism to control the number of requests made to the OpenAI API to ensure compliance with usage limits. It might Gives you the following **error** 

<img width="911" alt="RateTimeLimit error" src="https://github.com/DKruti/Machine-Learning/assets/120690177/28c26979-0dea-4e9c-99e9-a04f60655a3e">

**SOLUTION** 
ADD THE FOLLOWING LINE OF CODE TO REMOVE HOWEVER IT SLOW DOWN THE REPSONSE

<img width="501" alt="rate limit error solution" src="https://github.com/DKruti/Machine-Learning/assets/120690177/aeda4f37-534e-4fdb-9875-b90dbbba1bff">


### Front-end Interface
The front-end is a simple HTML web form that allows users to select the language for the email response and displays the generated customer comment and email response.

### Backend Processing
The Flask backend consists of several Python functions that interact with the OpenAI GPT-3.5 model to perform the following tasks:

1. Generate a customer comment about electronic products.
2. Suggest an email subject based on the customer comment.
3. Provide a concise summary of the customer comment.
4. Translate the summary to the selected language.
5. Analyze the sentiment of the customer comment.
6. Generate a complete email response based on the above information.

## Prerquisite
1. Create virtual environment or go to already created virtual environment using command: workon  <virtual environment name>
2. Download Flask and translate packages in your virtual environment. Using command:

<img width="439" alt="translate install" src="https://github.com/DKruti/Machine-Learning/assets/120690177/c1a59a51-4b38-4e0e-9851-2fc4c5b548c9">

**OR pip install flask openai translate**

## Implementation

The application is implemented using the following technologies and components:

- Python: The backend logic is written in Python.
- Flask: Flask is used to create the web application.
- OpenAI GPT-3.5 Model: The application leverages the GPT-3.5 model for natural language generation.
- HTML/CSS: The front-end interface is designed with HTML and can be styled using CSS.
- Environment Variables: API keys and configuration are managed using environment variables.

## Test

Testing the application can be done by running it locally:

1. Clone the repository to your local machine.
2. Set up a virtual environment and install the required dependencies using `pip install -r requirements.txt`.
3. Create a `.env` file and add your OpenAI API key.
4. Run the application using `python app_json.py`.
5. Access the application in your web browser at `http://localhost:5000`.

## output

<img width="637" alt="English to English" src="https://github.com/DKruti/Machine-Learning/assets/120690177/b9bd4420-bef2-4f4d-88cf-e946f7233c67">


Test the application by selecting different languages and observing the generated email responses. Ensure that the rate limiting mechanism is working as intended.

Please note that you should have the necessary OpenAI API access and environment variables set up for the application to work correctly.

Feel free to customize the project further and deploy it to a hosting platform of your choice for production use.

Enjoy using the Customer Support System Automated Email Response!
