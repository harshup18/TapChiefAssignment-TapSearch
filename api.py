import sys
from collections import defaultdict

    
class WordSearchClass:
    
    def __init__(self, text):
        
        self.text = text.lower()
        self.indexInverted = defaultdict(set)
        
    
    def create_indexInverted(self):
        
        document = self.index()
        
        for i in document.keys():
            paragraph = document[i].strip().split(' ')
            for x in paragraph:
                x = x.strip()
                self.indexInverted[x].add(i)
        return self.indexInverted
    
    def index(self):
        
        # convert return character into space
    
        for i in range(0,len(self.text)):
            if self.text[i] == '\r':
                self.text = self.text.replace('\r','')
                break

        # spilt the documents into paragraph 
        r_list = self.text.split('\n\n')    
        paragraphs = []
        
        for i in range(len(r_list)):
            y = r_list[i].replace('\n', ' ')
            paragraphs.append(y)
            
        # Numbering the paragraphs in the dictionary
        index_doc = dict(enumerate(paragraphs,1))
        return index_doc
        
        
    def searchForWord(self, word):
        # Creating ann inverted index for storing the word in a paragraph
        indexInverted = self.create_indexInverted()
        paragraph = self.index()
        
        if word in indexInverted.keys():
            if len(indexInverted[word]) < 9:
                return list(indexInverted[word])
            else:
                return list(indexInverted[word])[:10]
        else:
            return []

            