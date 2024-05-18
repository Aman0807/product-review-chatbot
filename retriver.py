from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.document_loaders import JSONLoader, TextLoader
import json


ollama_emb = OllamaEmbeddings(model="llama2")



emb = ollama_emb.embed_query("Hello")
print(len(emb))


json_loader = JSONLoader(
                            file_path="amazon_reviews.json", 
                            jq_schema=".LG_Air_Conditioner[]", 
                            text_content=False
                        )
json_documents = json_loader.load() 

print(json_documents)


text_loader = TextLoader(file_path='youtube_review.txt')
text_documents = text_loader.load()

print(text_documents)


