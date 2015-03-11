#!/usr/bin/python

import sys
import numpy
from  nltk.tokenize import *
import nltk.corpus
import nltk.data
from random import randint

#split text into chunks, each chunk has l_num sentences
def GenerateData(filename):
	#generate data
	f = open(filename)
	data = f.read()
	f.close
	return data

# data process
def data_process(data):
	# tokenize
	data_tk = regexp_tokenize(data,pattern=r'\w+([.,]\w+)*|\S+')
	# lower
	data_low = [w.lower() for w in data_tk]
	return data_low

class MarkovChain:
	def __init__(self):
		self.E = 0
		self.adj = {}

	def addNode(self,v):
		self.adj[v] = []
	def addTransition(self,v,w):
		self.E += 1
		if v in self.adj:
			 self.adj[v].append(w)
		else:
			 self.adj[v] = [w]

	def neighbors(self,v):
		return adj[v]

	def next(self,v):
		l = len(self.adj[v])
		rand_neighbor = randint(0,l-1)
		next_v = self.adj[v][rand_neighbor]
		return next_v

	def toString(self):
		s = ""
		s += str(len(self.adj)) + "vertices, " + str(self.E) + "edges " + "\n"
		for v in self.adj:
			s += v + ": "
			for w in self.adj[v]:
				s += (w + " ")
			s += "\n"
		return s
	
class TextGenerator:
	def __init__(self,data):
		self.test = MarkovChain()
		self.data = data
		for i in range(len(self.data)):
			if i>0:
				self.test.addTransition(data[i-1],data[i])
			else:
				self.test.addNode(data[i])
	def generate(self,n):
		v = "."
		for i in range(n):
			v = self.test.next(v)
			sys.stdout.write(v + " ")
		print
			

data = "The cat is very nice. The dog is a bad dog. I love cat and dog."
#test = TextGenerator(3,data)
#test.generate(100)
data1 = GenerateData("pg1661.txt")
data2 = GenerateData("pg31100.txt")
data1_new = data_process(data1)
data2_new = data_process(data2)
test1 = TextGenerator(data1_new)
test1.generate(200)
test2 = TextGenerator(data2_new)
test2.generate(200)
