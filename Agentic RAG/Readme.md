In this advanced RAG system, Gen. AI capabilities of LLM models are not limited to (maybe) just summarizing the output based on context. Rather it has the capability to decide on which Retriever tool (through routing the query) to be used based on agent's decision.

Agentic RAG is a framework that enhances traditional RAG systems by incorporating intelligent agents to handle complex tasks and make decisions dynamically.

Use an agent to figure out how to retieve the most relevant information before using the retrieved information to answer the user's question.

Retrieval Agents are useful when we want to make decisions about whether to retrieve from an index. To implement a retrieval agent, we simply need to give an LLM access to retriever tool.