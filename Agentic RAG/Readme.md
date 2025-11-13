In this advanced RAG system, Gen. AI capabilities of LLM models are not limited to (maybe) just summarizing the output based on context. Rather it has the capability to decide on which Retriever tool (through routing the query) to be used based on agent's decision.

Agentic RAG is a framework that enhances traditional RAG systems by incorporating intelligent agents to handle complex tasks and make decisions dynamically.

Use an agent to figure out how to retieve the most relevant information before using the retrieved information to answer the user's question.

Retrieval Agents are useful when we want to make decisions about whether to retrieve from an index. To implement a retrieval agent, we simply need to give an LLM access to retriever tool.

RAG Paradigm: Naive Rag, Advanced Rag, modular Rag, Graph Rag

Naive Rag -> Rely on keyword based retrieval technique (tf-idf, bm25) to fetch docs from static datasets. But it has lack of contextual awareness, fragmented outputs and scalability issues.

Advanced Rag -> Incorporate semantic understandings and enhanced retrieval technques. Dense Passage Retrieval (DPR) & neural ranking algorithms to improve retrieval precision. top-k similar docs are fetched based on vector space position.

Modular RAG -> Key innovations in this technique include combining sparse retrieval methods (e.g., bm25) with dense retrieval techniques (DPR) to maximize accuracy across diverse query types.

Tool Integration: incorporating external APIs, dbs, or computational tools to handle specialized tasks


Graph RAG -> These systems leverage the relationships and hierarchies within graph data to enhance multi-hop reasoning and contextual enrichment. Graph RAG enables richer and more accurate generative outputs, particularly for tasks requiring relational understanding. (node connectivity, hierarchical knowledge mgmt, context enrichment). Vector stores for Graph Rag e.g. Neo4j

Agentic RAG -> Introduces autonomous agents capable of dynamic decision-making and workflow optimization. Unlike static systems, Agentic RAG employs iterative refinement and adaptive retrieval strategies to address complex, real-time, and multi-domain queries.

Autonomous decision-making (Agents independently evaluate and manage retrieval strategies)
Iterative Refinement (Incorporate feedback loops to improve retrieval accuracy and response relevance)
Workflow optimization(dynamically orchestrates tasks, enabling efficiency in real-time applications)