from simpleneighbors import SimpleNeighbors
import numpy as np
import random

class SemanticSimilarityChatbot:
    
    def __init__(self, nlp, dims):
        self.nns = SimpleNeighbors(dims)
        self.id_pairs = {}
        self.vocab = []
        self.dims = dims
        self.nlp = nlp
        
    def add_to_vocab(self, item):
        cur_id = len(self.vocab)
        self.vocab.append(item)
        return cur_id
    
    def add_pair(self, first, second):
        first_id = self.add_to_vocab(first)
        second_id = self.add_to_vocab(second)
        self.id_pairs[first_id] = second_id
        vec = self.vectorize(first)
        self.nns.add_one(first_id, vec)
        
    def vectorize(self, s):
        if s == "":
            s = " "
        doc = self.nlp(s, disable=['tagger', 'parser'])
        mean = np.mean(np.array([w.vector for w in doc]), axis=0)
        return mean
    
    def build(self, n=50):
        self.nns.build(n)
        
    def response_for(self, s, n=10):
        vec = self.vectorize(s)
        nearest_ids = self.nns.nearest(vec, n)
        picked = random.choice(nearest_ids)
        return self.vocab[self.id_pairs[picked]]
    
    def save(self, prefix):
        import pickle
        data = {
            'id_pairs': self.id_pairs,
            'vocab': self.vocab,
            'dims': self.dims
        }
        with open(prefix + "-chatbot.pkl", "wb") as fh:
            pickle.dump(data, fh)
        self.nns.save(prefix)
        
    @classmethod
    def load(cls, prefix, nlp):
        import pickle
        with open(prefix + "-chatbot.pkl", "rb") as fh:
            data = pickle.load(fh)
            newobj = cls(nlp, data['dims'])
            newobj.id_pairs = data['id_pairs']
            newobj.vocab = data['vocab']
            newobj.nns = SimpleNeighbors.load(prefix)
        return newobj
