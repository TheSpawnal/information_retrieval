def cosine_similarity_scores(query, documents, tfidf_weights):
  """Computes the cosine similarity scores between a query and a set of documents.
  Args:
    query: A list of query terms.
    documents: A list of documents, represented as lists of terms.
    tfidf_weights: A dictionary mapping terms to TF-IDF weights.
  Returns:
    A list of cosine similarity scores, one for each document.
  """
  # Calculate the query vector.
  query_vector = []
  for term in query:
    query_vector.append(tfidf_weights.get(term, 0.0))

  # Calculate the document vectors.
  document_vectors = []
  for document in documents:
    document_vector = []
    for term in document:
      document_vector.append(tfidf_weights.get(term, 0.0))

  # Calculate the cosine similarity scores.
  scores = []
  for document_vector in document_vectors:
    score = numpy.dot(query_vector, document_vector) / (
        numpy.linalg.norm(query_vector) * numpy.linalg.norm(document_vector))
    scores.append(score)

  return scores

# Example usage:
query = ["offensive penetration system"]
documents = [["offensive penetration system", "honey"], ["machine learning"]]
tfidf_weights = {"offensive penetration system": 0.5, "honey": 0.25, "machine learning": 0.25}

scores = cosine_similarity_scores(query, documents, tfidf_weights)
print(scores)