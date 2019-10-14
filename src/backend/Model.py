import jieba
import numpy as np
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from gensim.models import word2vec
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from keras_radam import RAdam
import tensorflow.keras.layers as L
import tensorflow as tf
from keras.models import model_from_json
import os
from keras.models import load_model
import random

class NewsClassifier():
    def doc2vec(self,content):
        jieba.load_userdict('dict.txt.big')
        content_lst = []
        temp_lst = jieba.cut(content)
        temp_str = ""
        for word in temp_lst:
            temp_str += word
            temp_str += " "
        doc = word_tokenize(temp_str.lower())
        doc_model = Doc2Vec.load('d2v.model') 
        self.doc_vec = doc_model.infer_vector(doc)
            
    def get_pushes_keyword(self,pushes):
        pushes_seg = []
        stopword_set = set()
        with open('stopwords.txt','r', encoding='utf-8') as stopwords:
            for stopword in stopwords:
                stopword_set.add(stopword.strip('\n'))
        for push in pushes:
            seg = ''
            words = jieba.cut(push, cut_all=False)
            for word in words:
                if word not in stopword_set:
                    word = re.sub("\d+", "", word)
                    if word:
                        seg += word + ' '
            pushes_seg.append(seg)
        if pushes_seg:
            vectorizer = TfidfVectorizer(max_features=20)
            wt = vectorizer.fit_transform(pushes_seg).toarray()
            word = vectorizer.get_feature_names()
            return wt, word
        else:
            return None, None
        
    def comment2vec(self,pushes): 
        comment_model = word2vec.Word2Vec.load("ptt_model_v2.bin")
        vac = comment_model.wv
        wt, words = self.get_pushes_keyword(pushes)
        vecs = dict()
        if words != None:
            for idx, word in enumerate(words):
                try:
                    vecs[idx] = vac[word]
                except:
                    vecs[idx] = np.zeros(250)
            cmt_vec = np.array([kw for _, kw in vecs.items()])
        self.comment_vec = cmt_vec
    
    def vec2feat(self):
        feat = np.concatenate([self.doc_vec,self.comment_vec.reshape(-1)], axis=0)
        feat = feat.reshape(1,5300)
        self.feat = np.array(feat)
    
    def model(self,content,pushes):
        #preprocessing
        self.doc2vec(content)
        self.comment2vec(pushes)
        self.vec2feat()
        # load json and create model
        json_file = open('model.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = tf.keras.models.model_from_json(loaded_model_json)
        # load weights into new model
        loaded_model.load_weights("model.h5")
        print('Successfully loaded model.')
        pred = loaded_model.predict(self.feat)
        self.pred = pred