In this advanced RAG system, Gen. AI capabilities of LLM models are not limited to (maybe) just summarizing the output based on context. Rather it has the capability to decide on which Retriever tool (through routing the query) to be used based on agent's decision.

Agentic RAG is a framework that enhances traditional RAG systems by incorporating intelligent agents to handle complex tasks and make decisions dynamically.

Use an agent to figure out how to retieve the most relevant information before using the retrieved information to answer the user's question.

Retrieval Agents are useful when we want to make decisions about whether to retrieve from an index. To implement a retrieval agent, we simply need to give an LLM access to retriever tool.

RAG Paradigm: Naive Rag, Advanced Rag, modular Rag, Graph Rag

naive rag -> Rely on keyword based retrieval technique (tf-idf, bm25) to fetch docs from static datasets. But it has lack of contextual awareness, fragmented outputs and scalability issues.

Advanced Rag -> Incorporate semantic understandings and enhanced retrieval technques. Dense Passage Retrieval (DPR) & neural ranking algorithms to improve retrieval precision. top-k similar docs are fetched based on vector space position.

