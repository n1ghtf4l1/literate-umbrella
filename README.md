<h1><b>Watson Jr.</b></h1>
<p>
In Natural Language Processing, <b>Question-Answering</b> is a field that focuses on designing systems that can answer questions. IBM Watson is a very famous example. Actually, Watson's accuracy requires enormous complexity and vast amounts of data, but I have designed a very simple question answering system based on inverse document frequency.
</p>
<p>
My question-answering system performs two tasks: document retrieval and passage retrieval. I have given my system access to a corpus of text documents. Whenever the user asks for a query (a question in English), document retrieval first identifies which all documents are the most relevant to the query. Once the top documents are found, they are subdivided int passages (sentences) so that the most relevant passage to the question can be determined.
</p>
<p>
To find the most relevant documents, I have used tf-idf rank documents based both on term frequency for words in the query as well as inverse document frequencyfor words. I have used a combination of inverse document frequency and a query term density measure.
</p>
<p>
In the real world, more sophisticated question answering systems employ other strategies like analyzing the type of question word used, looking for synonyms of query words, lemmatizing to handle different forms of the same word, etc.), but in this project I have focused on a medium level question answering system.
</p>
<h3><b>OUTPUT:</b></h3>
<p>$ python questions.py corpus</p>
<p>Query: What are the types of supervised learning?</p>
<p>Types of supervised learning algorithms include Active learning , classification and regression.</p>
<br>
<p>$ python questions.py corpus</p>
<p>Query: When was Python 3.0 released?</p>
<p>Python 3.0 was released on 3 December 2008.</p>
<br>
<p>$ python questions.py corpus</p>
<p>Query: How do neurons connect in a neural network?</p>
<p>Neurons of one layer connect only to neurons of the immediately preceding and immediately following layers.</p>