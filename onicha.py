from elasticsearch import Elasticsearch
import spacy

# Initialize Elasticsearch
es = Elasticsearch()

# Example document indexing
def index_document(index_name, document):
    es.index(index=index_name, body=document)

# Example query using spaCy
def query_technical_terms(index_name, query_text):
    nlp = spacy.load("en_core_web_sm")
    tokens = nlp(query_text)
    query = " ".join([token.lemma_ for token in tokens if not token.is_stop])
    results = es.search(index=index_name, body={"query": {"match": {"content": query}}})
    return results

# Example usage
index_document("technical_docs", {"content": "Example technical document content"})
results = query_technical_terms("technical_docs", "How to install Python on Windows")
print(results)
