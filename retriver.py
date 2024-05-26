import shutil
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.document_loaders import JSONLoader, TextLoader
from langchain_community.vectorstores.chroma import Chroma
from langchain.prompts import ChatPromptTemplate

from langchain_community.llms.ollama import Ollama
from langchain_core.runnables.passthrough import RunnablePassthrough


shutil.rmtree("chroma",)

ollama_emb = OllamaEmbeddings(model="llama3:8b")


emb = ollama_emb.embed_query("Hello")
print(len(emb))


json_loader = JSONLoader(
                            file_path="amazon_reviews.json", 
                            jq_schema=".LG_Air_Conditioner[]", 
                            text_content=False
                        )
json_documents = json_loader.load() 

print(len(json_documents))

# for doc in json_documents:
#     print(f"*****\n{doc}\n******")

text_loader = TextLoader(file_path='youtube_review.txt')
text_documents = text_loader.load()

# print(text_documents)
db = Chroma.from_documents(json_documents + text_documents, ollama_emb, persist_directory='./chroma')
print(db)


retriever = db.as_retriever(search_kwargs={"k": 10})
print(retriever)


template = """Answer the question based only on the following context: {context}
Do remember that this context is multiple reviews of same product. 

Question: {question}
"""

prompt = ChatPromptTemplate.from_template(template)
print("prompt", prompt)

model = Ollama(model="llama3:8b")

chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    |prompt 
    | model
)

query = "How much does the product cost?"

print(chain.invoke(query))



