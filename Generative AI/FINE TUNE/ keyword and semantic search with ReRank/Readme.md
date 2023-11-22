# Keyword and Semantic Search with ReRank

## Introduction

This project utilizes natural language processing and semantic search techniques to enhance search results using Weaviate and Cohere APIs. The primary goal is to improve the relevance of search queries through a combination of keyword search, dense retrieval, and reranking mechanisms.

## Design

### Technologies Used

1. **Cohere API:**
   - Utilized for reranking search results.
   - API key is set up as an environment variable.
   - Cohere client instantiated using the Python `cohere` package.

2. **Weaviate API:**
   - Employed for semantic search and keyword-based retrieval.
   - API key and configuration set up as environment variables.
   - Weaviate client instantiated using the Python `weaviate` package.

3. **Python Packages:**
   - `python-dotenv` for managing environment variables.
   - Custom utility functions stored in a `utils.py` file for modular code organization.

### Implementation

1. **Setup:**
   - API keys for Cohere, Weaviate, and potentially OpenAI are configured as environment variables.
   - Necessary packages (`cohere`, `weaviate-client`, `python-dotenv`) are installed.
   - Cohere API key information:
      Website: https://dashboard.cohere.com/ create a account and they give you trial API key. copy  the key.
      <img width="1440" alt="Screen Shot 2023-11-21 at 12 17 17 AM" src="https://github.com/DKruti/Machine-Learning/assets/120690177/5cfa4229-4312-4c2a-9ec8-cb47ab0b3ad5">
      
  - Weaviate API key:  you can create account and get the API key. However I used universal API key ‘76320a90-53d8-42bc-b41d-678647c6672e’ & Universal URL:‘https://cohere-demo.weaviate.network/’. 

2. **Weaviate Integration:**
   - Weaviate is used for both keyword search and dense retrieval.
   - A utility function `dense_retrieval` is defined to perform dense retrieval given a query.

3. **Cohere Integration:**
   - The Cohere API is employed for reranking search results.
   - A utility function `rerank_responses` is defined to rerank a list of responses using the Cohere API.

4. **Keyword Search:**
   - The `keyword_search` function is implemented to perform keyword-based searches using Weaviate.
   - Results are printed with customizable properties and additional information.

5. **Dense Retrieval:**
   - The `dense_retrieval` function is implemented to perform dense retrieval using Weaviate.
   - Results are printed with customizable properties and additional information.
   - <img width="1383" alt="Screen Shot 2023-11-21 at 12 58 53 AM" src="https://github.com/DKruti/Machine-Learning/assets/120690177/1f8a8929-149d-47ef-b06e-5e3639e1617c">

6. **Reranking:**
   - Responses obtained from keyword search or dense retrieval are reranked using the Cohere API.
   - Reranked results are printed for analysis.
   - Following is use of key word and it gives you more than 500 item 
<img width="1365" alt="Screen Shot 2023-11-21 at 12 59 07 AM" src="https://github.com/DKruti/Machine-Learning/assets/120690177/08807c03-bb17-4767-b0bf-39fcb87abc78">
- ReRank will help to choose only those relavant few item it gives 9 here 
<img width="1371" alt="Screen Shot 2023-11-21 at 1 00 18 AM" src="https://github.com/DKruti/Machine-Learning/assets/120690177/ca517e76-1c3c-42a6-8a83-1c27390b8ccb">

### Test Result

<img width="1334" alt="Screen Shot 2023-11-21 at 1 00 27 AM" src="https://github.com/DKruti/Machine-Learning/assets/120690177/875b8c22-316a-48bb-9c0a-e13a8bb345bf">

## Conclusion
This project synergizes Cohere and Weaviate APIs, transcending traditional search limitations. By combining advanced NLP and semantic search, it delivers nuanced, context-aware results. The modular design ensures easy integration, serving as a blueprint for superior search applications.
The project aims to provide a comprehensive approach to improving search results by combining keyword search, dense retrieval, and reranking mechanisms, leveraging the capabilities of Weaviate and Cohere APIs. The modular and extensible design facilitates easy adaptation and integration into various applications requiring enhanced natural language understanding and search relevance.
