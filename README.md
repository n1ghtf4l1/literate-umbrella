# **literate-umbrella**

## **Watson Jr.**
In Natural Language Processing, **Question-Answering** is a field that focuses on designing systems that can answer questions. IBM Watson is a very famous example. Actually, Watson's accuracy requires enormous complexity and vast amounts of data, but I have designed a very simple question answering system based on inverse document frequency.

My question-answering system performs two tasks: document retrieval and passage retrieval. I have given my system access to a corpus of text documents. Whenever the user asks for a query (a question in English), document retrieval first identifies which all documents are the most relevant to the query. Once the top documents are found, they are subdivided int passages (sentences) so that the most relevant passage to the question can be determined.

To find the most relevant documents, I have used tf-idf rank documents based both on term frequency for words in the query as well as inverse document frequencyfor words. I have used a combination of inverse document frequency and a query term density measure.

In the real world, more sophisticated question answering systems employ other strategies like analyzing the type of question word used, looking for synonyms of query words, lemmatizing to handle different forms of the same word, etc.), but in this project I have focused on a medium level question answering system.

### **OUTPUT:**
```console
$ python questions.py corpus
Query: What are the types of supervised learning?
Types of supervised learning algorithms include Active learning , classification and regression.

$ python questions.py corpus
Query: When was Python 3.0 released?
Python 3.0 was released on 3 December 2008.

$ python questions.py corpus
Query: How do neurons connect in a neural network?
Neurons of one layer connect only to neurons of the immediately preceding and immediately following layers.
```
