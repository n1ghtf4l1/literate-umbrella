import nltk
import sys
import os
import string
import math

FILE_MATCHES = 1
SENTENCE_MATCHES = 1


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = load_files(sys.argv[1])
    file_words = {
        filename: tokenize(files[filename])
        for filename in files
    }
    file_idfs = compute_idfs(file_words)

    # Prompt user for query
    query = set(tokenize(input("Query: ")))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)

    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    for match in matches:
        print(match)


def load_files(directory):
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """
    map = dict()
    for file in os.listdir(directory):
        with open(os.path.join(directory, file), encoding="utf-8") as f:
            map[file] = f.read()
    return map


def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """
    processed = []
    punctuation = string.punctuation
    stopwords = nltk.corpus.stopwords.words("english")
    for word in nltk.word_tokenize(document.lower()):
        if word not in punctuation and word not in stopwords:
            processed.append(word)
    return processed


def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.

    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """
    idf = dict()
    total_docs = len(documents)
    for i in set(sum(documents.values(), [])):
        num_doc_contain_word = 0
        for j in documents.values():
            if i in j:
                num_doc_contain_word += 1

        idf[i] = math.log(total_docs / num_doc_contain_word)

    return idf


def top_files(query, files, idfs, n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """
    tfidfs = []
    for file in files:
        score = 0
        for word in query:
            score += idfs[word] * files[file].count(word)
        tfidfs.append((file, score))
    tfidfs.sort(key=lambda x: x[1], reverse=True)
    return [j[0] for j in tfidfs[:n]]


def top_sentences(query, sentences, idfs, n):
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density.
    """
    l = []
    for i in sentences:
        idf, words = 0, 0
        for word in query:
            if word in sentences[i]:
                words += 1
                idf += idfs[word]
        l.append((i, idf, (float(words) / len(sentences[i]))))
    l.sort(key=lambda x: (x[1], x[2]), reverse=True)
    return [x[0] for x in l[:n]]


if __name__ == "__main__":
    main()
