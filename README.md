Chatbot to fetch reviews/description of a particular product such as an appliance (mobile, tv, washing machine etc.) and answer questions specific to that product. 


**How it works?**
  - takes a product name as input (e.g. an appliance such as phone, tv, washing machine etc.)
  - finds online reviews thorugh multiple sources (primarly amazon (text reviews) & youtube (video reviews))
  - takes transcript of the video if it exists. if not, converts audio to text using whisper model
  - creates vector embeddings of all the text data.
  - stores embedding in a vector database.
  - provides summary of the product to the user 
  - retrieves information from the vector database to answer the user questions.

