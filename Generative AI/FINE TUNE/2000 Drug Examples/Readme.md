# AI Enabled Drug Classification System

## Introduction

This project focuses on Drug Classification through Machine Learning, leveraging the capabilities of OpenAI's GPT-3.5. The objective is to refine drug classification by utilizing a curated dataset of 2000 drug examples from an Excel file, enabling precise categorization based on associated maladies. The core idea is to teach a smart computer system to identify the illnesses specific medicines are designed to treat.

## Design

### Step 1: Preparing the Data
Convert the XLSX data file into JSONL format for fine-tuning the model using Pandas and OpenAI tools. The data is formatted with prompts and completions for drug names and corresponding maladies. The script utilizes Pandas to transform the data and ensures each completion starts with a whitespace.

### Step 2: Command to Prepare Data
Analyze and prepare the data using the OpenAI tools `fine_tunes.prepare_data` command. This command prompts for splitting the data into training and validation sets.

### Step 3: Command to Train the Model
Use the provided command to train the model using `fine_tunes.create`. Specify parameters such as the training and validation data files, model type (ada), and classification metrics.

### Step 4: Checking Job Progress
If the client disconnects during fine-tuning, use the following command to check job progress.

### Step 5: Completion of Fine-Tuning
When the fine-tuning job is completed, you'll receive an output confirming the completion, cost, and other details. Use the fine-tuned model for generating completions.
# Implementation

To set up and implement the AI Enabled Drug Classification System, follow these steps:

### Step 1: Create Virtual Environment

```bash
python3 -m venv venv
. venv/bin/activate
workon chatgpt

pip install pandas openpyxl openai==0.28

python3 app.py

openai tools fine_tunes.prepare_data -f drug_malady_data.jsonl

export OPENAI_API_KEY="xxxxxxxxxxxx"

openai api fine_tunes.create \
  -t "drug_malady_data_prepared_train.jsonl" \
  -v "drug_malady_data_prepared_valid.jsonl" \
  --compute_classification_metrics \
  --classification_n_classes 7 \
  -m ada \
  --suffix "drug_malady_data"

openai api fine_tunes.follow -i <JOB ID>
python3 test.py




<img width="608" alt="final test outout" src="https://github.com/DKruti/Machine-Learning/assets/120690177/ea34b4e1-c7b0-42c7-ace6-2c4911aa9d15">









