# Works perfectly but slow without usinf Json file. Data is stored in .py file
import openai
import os
import time
from flask import Flask, render_template, request
from dotenv import load_dotenv
#from products_data import products_data
import json
import random


app = Flask(__name__)

# Load product data from product.json
with open('products_data.json', 'r') as json_file:
    products_data = json.load(json_file)

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
if openai.api_key is None:
    raise ValueError("API key not found in environment variables")

# Define a rate limiting mechanism
RATE_LIMIT = 3  # Requests per minute
RATE_LIMIT_PERIOD = 60  # 60 seconds in a minute

# Define a timestamp variable to track the last request time
last_request_time = 0

def get_completion_with_rate_limit(prompt):
    global last_request_time
    
    # Calculate the time since the last request
    current_time = time.time()
    time_since_last_request = current_time - last_request_time
    
    # Check if the rate limit has been reached, and if so, wait
    if time_since_last_request < RATE_LIMIT_PERIOD:
        time_to_wait = RATE_LIMIT_PERIOD - time_since_last_request
        time.sleep(time_to_wait)
    
    # Make the API request
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0,
    )
  
    last_request_time = time.time()
    
    return response.choices[0].message["content"]
  # response = openai.ChatCompletion.create(
    #     model="gpt-3.5-turbo",
    #     #messages=[{"role": "system", "content": "You are a helpful assistant that translates English to French."},
    #     messages =[{"role": "user", "content": prompt}],
    # )
    
    # Update the last request time
# Step 1: Generate a Customer's Comment
def generate_customer_comment(products_data):
    prompt=f"""
    Assume that you are a customer to an electronic product company.
    Write a 100-word only comment about the products delimited by triple backticks in its own language. 
    Products: ```{products_data}```
    """
    response = get_completion_with_rate_limit(prompt)
    return response

# Step 2: Generate Email Subject
def generate_email_subject(comment):
    prompt=f"""
    Assuming that you provide customer support for an electronic product company.
    Based on the customer comment delimited in triple backticks, suggest a short email subject to respond to the customer. 
    Comment= ```{comment}```
    """
    response = get_completion_with_rate_limit(prompt)
    return response

# Step 3: Generate Customer Comment Summary
def summarize_comment(comment):
    prompt=f"""
    Assuming that you provide customer support for an electronic product company.
    Provide a concise summary in 50 words of the following customer comment delimited in triple backticks. Comment: ```{comment}```
    """
    response = get_completion_with_rate_limit(prompt)
    return response

def translate_summary_with_chatgpt(language, summary):
    prompt= f"""
    Translate the following summary delimited by triple backticks to the language delimited by <>. 
    Language:```{language}```   
    Summary:<{summary}>
    """
    response = get_completion_with_rate_limit(prompt)
    return response

# Step 4: Analyze Customer Comment Sentiment
def analyze_sentiment(comment):
    prompt=f"""
    Assuming that you provide customer support for an electronic product company.
    What is the sentiment of the comment delimited in triple backticks? Is it positive or negative? 
    Comment: ```{comment}```
    """
    max_tokens=10
    response = get_completion_with_rate_limit(prompt)
    sentiment = response.lower()
    if "positive" in sentiment:
        return "positive"
    elif "negative" in sentiment:
        return "negative"
    else:
        return "neutral"

# Step 5: Generate Customer Email
def generate_customer_email(summary, sentiment, email_subject, language):
    if sentiment == "positive":
        response_text = "We're thrilled to hear your feedback and appreciate your positive words. Your satisfaction is our top priority!"
    elif sentiment == "negative":
        response_text = "We're truly sorry to hear about your experience. Your feedback is crucial, and we'll strive to address your concerns."
    else:
        response_text = "Thank you for your feedback! We're always looking to improve, and your insights are valuable."
    prompt = f"""
    Assuming that you provide customer support for an electronic product company.
    Given the specified parameters below:
    - Comment summary enclosed in backticks (`{summary}`)
    - Our response text enclosed in triple quotes (\"\"\"{response_text}\"\"\")
    - Translate the Email subject enclosed in angle brackets ({email_subject}) to language \"{language}\"
    Write a complete email responding to the customer's comment using the language \"{language}\". 
    """
    response = get_completion_with_rate_limit(prompt)
    return response

@app.route('/', methods=['GET', 'POST'])
def index():
    answer = ""
    comment = generate_customer_comment(products_data)
    print("A customer comment has been generated.")
    if request.method == 'POST':
        language = request.form.get('language')  # Fetch language input from the webpage
        print(f"Selected language: {language}")
        answer = process_comment_to_email(comment, language)
    return render_template('index.html', question=comment, answer=answer)

def process_comment_to_email(comment, language):
    # Step 2: Generate Email Subject
    email_subject = generate_email_subject(comment)
    print(f"An email subject is generated from the customer's comment.")
    # Step 3: Generate Customer Comment Summary
    summary = summarize_comment(comment)
    print("A Summary is generated from the customer comment.")
    translated_summary = translate_summary_with_chatgpt(language, summary)
    print("The summary has been translated to the requested language.")
    # Step 4: Analyze Customer Comment Sentiment
    comment_sentiment = analyze_sentiment(comment)
    print(f"Sentiment of the comment is detected as: {comment_sentiment}")
    # Step 5: Generate Customer Email
    email_content = generate_customer_email(translated_summary, comment_sentiment, email_subject, language)
    print("A customer email has been generated.")
    return email_content

if __name__ == '__main__':
    app.run(debug=True)