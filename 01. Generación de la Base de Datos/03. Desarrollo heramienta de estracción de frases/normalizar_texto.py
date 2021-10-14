# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 11:26:49 2021

@author: domer
"""
import numpy as np

path = 'C:/Users/domer/OneDrive/UPS/ERASMUS/EduTech/01. Generación de la Base de Datos/03. Desarrollo heramienta de estracción de frases/'
lines = np.loadtxt(path+"textos.txt", dtype='str', delimiter="\n", encoding='utf-8')
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'á', 'é', 'í', 'ó', 'ú', ' ']
vocabulary = []
for line in lines:
    if line != "":
        vocabulary += [''.join([i for i in vocab.strip().lower() if i in abc]) for vocab in list(filter(None,line.strip().split(".")))]
    
print(vocabulary)

f=open(path+'textos-normalizados.txt','a', encoding='utf-8')
for ele in vocabulary:
    if ele != '' or len(ele) > 0:
        f.write(ele+'\n')
f.close()