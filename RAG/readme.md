Retrieval-Augmented Generation (RAG) is the process of optimizing the output of an LLM, so it references an authoritative knowledge base outside of its training data sources before generating a response. LLMs are trained on vast volumes of data and use billions of parameters to generate original output for tasks like answering questions, translating languages, and completing sentences. RAG extends the already powerful capabilities of LLMs to specific domains or an organization's internal knowledge base, all without the need to retrain the model. It is a cost-effective approach to improving LLM output so it remains relevant, accurate, and useful in various contexts.


LLMs can hallucinate, if we ask questions outside of its training data.

For e.g., a company can have policies associated with them, which are internal to the company. So, they can create a chatbot by finetuning the existing model. But it's an expensive and tedious task as tweaking of billions of model parameters is required. Additionally, the internal policies can get updated every once in a while, and it's difficult to fine-tune again. In this scenario, RAG can be the solution.


Usually, Query+Prompt -> LLM -> output

With RAG, query -> vector knowledge base -> context+prompt -> LLM -> output

A data ingestion pipeline is required to ingest data into a vector database (knowledge base). This pipeline involves Data(pdf, html, excel, sql,..) being fed into parsing stage (read structured and unstructured data, and divide them into chunks), then embedding is done to convert text into vectors (numerical representation of text), so that it is possible to apply similarity search algorithms (cosine similarity,.. )

Now, before the input query goes into the LLM, it now gets vectorized (using embedding) and goes into the vector db for similarity search, and a context is retrieved from it, which along with prompt instruction (use the context to generate result) is fed into the LLM, and the result is generated. This pipeline is called Retrieval pipeline (These stages are for Traditional RAG)

RAG pipeline -> Data ingestion pipeline + Query Retrieval pipeline 


Whenever it is needed to work with external knowledge db or any data that needs to be fed into the vector db, it is important to know about 'document' structure.

Once data is recieved, it is important to convert it into a structure where additional strategies like chunking and embedding be applied, before storing it into a vector db.

In Data Ingestion Pipeline, after data parsing to a document structure, the next step is chunking. In chunking, the entire data is converted into multiple chunks, and then embedding is applied to it.

In embedding, there is a fixed context size. If more data is passed than the context size, it may not be possible to convert text into a vector. Hence, data should be passed within the limit of a context size, and it is a good strategy to divide data into chunks.

After chunking, embedding will be applied to every chunk, and records will be stored in a vector db as vectors, which in turn can be used for similarity search.
