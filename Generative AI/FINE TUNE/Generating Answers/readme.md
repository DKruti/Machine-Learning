# Generating Answers
**Flow:Input Text ==> Chunking ==> Embedding ==> Search Index ==> Query ==> Search ==> Question ==> Answer**

## Introduction
This project focuses on generating answers to questions based on a given context, showcasing the integration of Cohere API for embeddings and Annoy library for efficient nearest neighbor search. The primary goal is to provide a system capable of understanding and responding to queries within a specific domain.

## Design
<img width="510" alt="Screen Shot 2023-11-21 at 1 28 19 AM" src="https://github.com/DKruti/Machine-Learning/assets/120690177/06f3dc0f-3cc7-4434-8673-ed2867d1a9e1">

### Technologies Used
1. **Cohere API:** Utilized for generating embeddings of textual data, enabling semantic understanding.
2. **Annoy Library:** Employed for building a search index, facilitating fast nearest neighbor search in the vector space.
3. **Python:** The core programming language used for scripting and implementing the project.
4. **Jupyter Notebooks:** The code is presented in Jupyter notebooks, enhancing readability and allowing for interactive development.
5. **numpy and pandas:** Used for efficient handling and manipulation of data arrays.
### Steps
1. **Input text :** whole information as Text or you can pass PDF using Langchain
2. **Chunking :** split the data into parts
3. **Embedding:** generate the Vector Space
4. **Search Index:** Search using index
5. **Query:** Pass the query or question from that text
6. **Search:** it searches using semantic search with Dense retrieval
7. **Question:** follow up Question or new question 
8. **Answers:** Result

## Implementation
### 1. Data Preparation and Embeddings
The project starts with the preparation of a question and a long piece of text. The text is then split into paragraphs, and Cohere is employed to generate embeddings for each paragraph.
  - Input: Text and query
  - Setup the packages
    -- !pip install cohere
    -- !pip install annoy
    -- ! pip install python-dotenv
### 2. Building a Search Index
Annoy library is utilized to create a search index based on the generated embeddings. This index enables efficient retrieval of nearest neighbors in the vector space.
<img width="564" alt="Screen Shot 2023-11-21 at 1 55 13 AM" src="https://github.com/DKruti/Machine-Learning/assets/120690177/8c9991d1-e214-48c5-8acc-f025a7a97139">

### 3. Searching Articles
A function is defined to search for articles related to a given query using the search index and Cohere embeddings. The results provide relevant context for generating answers.
<img width="1382" alt="Screen Shot 2023-11-21 at 1 55 02 AM" src="https://github.com/DKruti/Machine-Learning/assets/120690177/9a1e7b2f-82a7-4b1a-832e-8047f9b155e9">

### 4. Generating Answers
A function is implemented to generate answers to a given question based on the context obtained from the search. The prompt is constructed, and Cohere is used to generate responses.
<img width="1365" alt="Screen Shot 2023-11-21 at 1 56 10 AM" src="https://github.com/DKruti/Machine-Learning/assets/120690177/562aeac0-9abd-47da-99bb-45152bc2c6cf">

### 5. Additional Utility Functions
Utility functions, such as `print_result`, are defined for formatting and printing results.

### 6. Unused Functions
While additional functions like `search_wikipedia_subset` and `generate_given_context` are defined, they are not utilized in the current script.

**Note:** Ensure to replace placeholders like `<your cohere API KEY>` and `<your API KEY>` with your actual API keys for the code to function correctly.
## Test
<img width="1377" alt="Screen Shot 2023-11-21 at 1 56 22 AM" src="https://github.com/DKruti/Machine-Learning/assets/120690177/0f732d23-e067-4950-95c0-5cfbefd8254a">

## Conclusion
The "Generating Answers" project showcases a powerful synergy between Cohere API and Annoy library, offering an effective solution for understanding and responding to natural language queries. Through meticulous data preparation, embeddings generation, and the construction of a search index, the project demonstrates a systematic approach to enhance semantic understanding. By integrating these technologies, the system adeptly generates coherent answers based on contextual information, exemplifying a robust framework for building intelligent question-answering systems.

This project serves as a comprehensive example of utilizing Cohere and Annoy for building a system that can understand natural language queries and generate meaningful responses within a specified context.
