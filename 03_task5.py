
"""To implement Improvement 5, we'll create a query_ntc_ntc function, which calculates cosine similarity scores between a query
and documents using the ntc.ntc variant of TF-IDF. This variant normalizes both term frequencies and document frequencies, and 
cosine similarity is used for scoring.
First, we need to define the score_ntc_ntc function. 
This function calculates the cosine similarity between a query and a document. 
We then use this function in query_ntc_ntc to find the most relevant documents for a given query.
Here's the pseudocode outline for both functions:
score_ntc_ntc(query, doc_id):
Calculate the TF-IDF vector for the query.
Fetch the TF-IDF vector for the document (using tfidf_length for normalization).
Compute the cosine similarity between these two vectors.
query_ntc_ntc(query_string):
Tokenize and preprocess the query string.
For each document, calculate its score with respect to the query using score_ntc_ntc.
Sort the documents based on their scores in descending order.
Display the top results using display_summary.
Below is the implementation in Python:"""

import numpy as np

def score_ntc_ntc(query_tokens, doc_id):
    # Calculate query vector (TF-IDF for each term in the query)
    query_vector = [tfidf(t, doc_id) for t in query_tokens]

    # Document vector is the TF-IDF values (normalized by document length)
    document_vector = [tfidf_length(doc_id) if t in query_tokens else 0 for t in tf_matrix[doc_id].keys()]

    # Cosine similarity
    score = np.dot(query_vector, document_vector) / (np.linalg.norm(query_vector) * np.linalg.norm(document_vector))
    return score

def query_ntc_ntc(query_string):
    # Preprocess the query string
    query_tokens = preprocess(tokenize(query_string))

    # Calculate scores for each document
    scored_docs = [(doc_id, score_ntc_ntc(query_tokens, doc_id)) for doc_id in Summaries.keys()]

    # Sort by score
    scored_docs.sort(key=lambda x: x[1], reverse=True)

    # Display top results
    for doc_id, score in scored_docs[:10]:
        print(f"docID: {doc_id} | score: {score}")
        display_summary(doc_id)

# Example query:
query_ntc_ntc("effect of music and dance for young adults")



"""alternative version"""
import numpy as np

def cosine_similarity(query_vector, document_vector):
    return np.dot(query_vector, document_vector) / (np.linalg.norm(query_vector) * np.linalg.norm(document_vector))

def score_ntc_ntc(query_tokens, doc_id):
    # Calculate query vector
    query_vector = [tfidf(t, doc_id) for t in query_tokens]

    # Calculate document vector
    document_vector = [tfidf(t, doc_id) for t in tf_matrix[doc_id].keys()]

    # Cosine similarity
    return cosine_similarity(query_vector, document_vector)

def query_ntc_ntc(query_string):
    # Preprocess and tokenize the query string
    query_tokens = preprocess(tokenize(query_string))

    # Calculate scores for each document
    scored_docs = [(doc_id, score_ntc_ntc(query_tokens, doc_id)) for doc_id in Summaries.keys()]

    # Sort by score
    scored_docs.sort(key=lambda x: x[1], reverse=True)

    # Display top results
    for doc_id, score in scored_docs[:10]:
        print(f"docID: {doc_id} | score: {score}")
        display_summary(doc_id)

# Example query:
query_ntc_ntc("effect of music and dance for young adults")
