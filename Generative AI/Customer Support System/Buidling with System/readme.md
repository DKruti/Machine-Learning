# Customer Support System: Moderation, Classification, Checkout, and Evaluation

## Overview
If you're a customer service assistant for a large electronics store, this system provides support in the following areas:

1. **Language Selection**: The website allows customers to select their preferred language.
2. **Product Information**: The store offers a range of products across different categories, each with detailed descriptions.

## Project Implementation Process

### Step 1: Checking Input - Input Moderation
In this step, the system checks for inappropriate prompts and modifies customer comments if necessary. A customer's comment that needs to be moderated.

Step 1.1.1: Input: products details Output: 100 word messages response generated from chatGPT
Step 1.1.2:Input: Generated response of 1.1.1 Output: Output is appropriate or inappropriate
Step 1.2 :Input: Generate Prompt Injection Output: Prevent Prompt Injection 
#### Step 1.1: Check Inappropriate Prompts
-**Step 1.1.1:**
--**Input:** The products' detailed descriptions.
--**Output:** 100 word messages response generated from chatGPT
-**Step 1.1.2:**
--**Input:** Generated response of 1.1.1
--**Output:**  a message is appropriate or inappropriate
#### Step 1.2: Modify the Output of Step 1.1.1
- **Input:** Generate Prompt Injection
- **Output**: Use OpenAI's Moderation API to check whether the output of Step 1 is inappropriate.
- **Prevent Prompt Injection**

#### Step 2: Classification of Service Requests
- **Input**: User Message
- **Output**: Response showing the User Message's classification.

### Step 3: Answering User Questions using Chain of Thought Reasoning
- **Input**: User Message
- **Output**: Use Chain of Thought Reasoning to provide answers to the user's questions.

### Step 4: Check Output

#### Test Case 1
- **Input**: System and User Messages
- **Output**: Use Check Output's Model Self-Evaluation technique to check if the response is factually based.

#### Test Case 2
- **Input**: System and User Messages
- **Output**: Use Check Output's Model Self-Evaluation technique to check if the response is not factually based.

### Step 5: Evaluation Part I - Evaluate Test Cases by Comparing Customer Messages to Ideal Answers
- **Input**: Sets of (customer_msg / ideal_answer) pairs
- **Output**: Run evaluation on all test cases and calculate the fraction of cases that are correct.

### Step 6: Evaluation Part II
- Evaluate the LLM's answer to the user with a rubric based on the extracted product information.

#### Normal Assistant Answer
- **Input**: Assistant's normal answer
- **Output**: Evaluation against the ideal answer from the test set.

#### Abnormal Assistant Answer
- **Input**: Assistant's abnormal answer
- **Output**: Evaluation against the ideal answer from the test set.
