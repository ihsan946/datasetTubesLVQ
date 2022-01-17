from __future__ import absolute_import
import numpy as np

class LVQ(object):
	def __init__(self, data, epochs=10, alpha=0.05):
		self.data = data
		self.datates = data[:,0:4]
		# print datates
		self.w1 = self.datates[0]
		self.w2 = self.datates[1]
		# print len(w1)
		self.epochs = epochs
		self.alpha = alpha

	def learning(self):
		for i in range(self.epochs):
			for j in range(2,len(self.data)):
				# print "data ke-",j-1,datates[j]
				sum1 = 0
				sum2 = 0
				for k in range(len(self.w1)):
					sum1 = sum1+(self.datates[j][k]-self.w1[k])**2
					sum2 = sum2+(self.datates[j][k]-self.w2[k])**2
				sum1 = np.sqrt(sum1)
				sum2 = np.sqrt(sum2)
				for k in range(len(self.w1)):	# Update bobot baru
					if sum1<=sum2:
						self.w1[k] = self.w1[k]+self.alpha*(self.datates[j][k]-self.w1[k])
					else:
						self.w2[k] = self.w2[k]+self.alpha*(self.datates[j][k]-self.w2[k])
			self.alpha = 0.1*self.alpha
		print ("Training selesai...")

	def printBobot(self):
		print ("Nilai bobot hasil training:")
		print (self.w1)
		print (self.w2)

	def prediksi(self, data):
		bobot1 = 0
		bobot2 = 0
		for i in range(len(self.w1)):
			bobot1 = bobot1+(data[i]-self.w1[i])**2
			bobot2 = bobot2+(data[i]-self.w2[i])**2
		bobot1 = np.sqrt(bobot1)
		bobot2 = np.sqrt(bobot2)

		if bobot1<bobot2:
			print ("Data",data,"masuk ke kelas 1")
		else:
			print ("Data",data,"masuk ke kelas 2")
