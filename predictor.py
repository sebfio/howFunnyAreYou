#!/usr/bin/env python3
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.layers.embeddings import Embedding
from keras.layers import Flatten
from keras.preprocessing import sequence
from keras.preprocessing.sequence import pad_sequences
from keras.models import model_from_json

import pandas as pd
import re
import sys
import numpy as np
from numpy import array
import os
import textwrap

class Predictor:
    def create_embedding_matrix(self, filepath, embedding_dim):
        embedding_matrix = np.zeros((self.vocab_size, embedding_dim))
        wordBank = dict()
        wordsProcessed = 1
        with open(filepath) as f:
            for line in f:
                if wordsProcessed > self.vocab_size - 1:
                    break
    
                # Split the word with the numbers
                word, *vector = line.split()
                # Add token ID
                wordBank[word]=wordsProcessed
    
                embedding_matrix[wordsProcessed] = np.array(
                    vector, dtype=np.float32)[:embedding_dim]
    
                wordsProcessed += 1
    
        return embedding_matrix, wordBank

    def __init__(self, modelname, weights):
        self.vocab_size = 10000
        self.max_words_review = 100
        self.embedding_dim = 50
        self.embedding_matrix, self.word_bank = self.create_embedding_matrix('glove/glove.6B.50d.txt', self.embedding_dim)
    
        json_file = open(modelname, 'r')
        loaded_json = json_file.read()
        json_file.close()
        self.model = model_from_json(loaded_json)
        print("Loading model %s" % (modelname))
        
        self.model.load_weights(weights)
        
        self.model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        self.model._make_predict_function()
        
        print("Loading model with weights %s" % (weights))
    
    def getFunny(self, text):
        frequencyArray = np.zeros((1, self.max_words_review))
        for j, word in enumerate(text.split(' ')):
            if j >= self.max_words_review:
                break
            frequencyArray[0][j] = self.word_bank[word] if word in self.word_bank else 0
        
        predict = self.model.predict(frequencyArray)
        return float(predict[0][0] * 100)
