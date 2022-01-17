#!/usr/bin/env python

from metode.LVQ import LVQ
import numpy as np

data = np.loadtxt("data.txt", usecols=[0,1,2,3,4])

lvq = LVQ(data)
lvq.learning()
lvq.printBobot()

print "Masukkan data tes (ex. 1 1 0 1):"
tes = map(int, raw_input().split())
lvq.prediksi(tes)