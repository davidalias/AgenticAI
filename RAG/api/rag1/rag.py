import os
import sys
sys.path.append(os.path.abspath("../.."))
from dotenv import load_dotenv
load_dotenv()

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

info = """ 
Neural networks, convolutional neural networks, and recurrent neural networks form three foundational pillars of modern deep learning, each designed to capture different structures in data. Together, they enable machines to learn patterns from images, text, audio, and sequential signals with remarkable accuracy.

A **neural network (NN)** is the most general form of these models. It consists of layers of interconnected nodes, or “neurons,” that transform input data through weighted connections and nonlinear activation functions. A basic feedforward neural network processes information in one direction—from input to output—making it suitable for tasks where data points are independent of one another, such as tabular classification or regression. The strength of NNs lies in their ability to approximate complex functions, but they struggle with high‑dimensional data like images or sequences unless specialized architectures are used.

This specialization leads to **convolutional neural networks (CNNs)**, which are designed specifically for spatial data such as images and videos. Instead of fully connecting every neuron to every input, CNNs use convolutional layers that slide small filters across the input to detect local patterns. Early layers capture simple features like edges or textures, while deeper layers learn more abstract concepts such as shapes or objects. Pooling layers reduce spatial dimensions, making the model more efficient and robust to small variations. CNNs revolutionized computer vision by enabling tasks like image classification, object detection, and facial recognition with unprecedented accuracy. Their ability to learn hierarchical representations makes them far more effective than traditional neural networks for visual tasks.

In contrast, **recurrent neural networks (RNNs)** are built for sequential data—text, speech, time series, and any information where order matters. RNNs introduce loops in their architecture, allowing information to persist across time steps. This gives them a form of memory, enabling them to model dependencies between earlier and later elements in a sequence. However, traditional RNNs suffer from vanishing and exploding gradients, making it difficult to learn long‑range relationships. To address this, advanced variants like LSTMs and GRUs were developed, incorporating gating mechanisms that control how information is stored, forgotten, or passed forward. These improvements made RNNs essential for early breakthroughs in language modeling, translation, and speech recognition.

While CNNs excel at spatial patterns and RNNs at temporal patterns, all three architectures share the same underlying principle: learning representations from data through layered transformations. They remain central to deep learning, even as newer models like Transformers build on their foundations to push AI capabilities further.
"""

#Chunking / Text Splitting

splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 70)
list_of_docs = splitter.create_documents(texts=[info])


print("List of docs--------------->",len(list_of_docs))

#Vector Store / Embedding

embeddings = OpenAIEmbeddings(model = 'text-embedding-3-small')
vector_store =FAISS.from_documents(documents=list_of_docs, embedding=embeddings)

#Retriever

retriever = vector_store.as_retriever()
question = "What is CNN?"

#RAG Retrieval

RAG_result = retriever.invoke(question)

print(len(RAG_result))

for i, res in enumerate(RAG_result):
    print("Result:",i+1)
    print(res.page_content)