import math
import numpy as np
import matplotlib.pyplot as plt
from utils import *

L = 25 # considerem 25 caracters en catala contant la ç pero no contant la w ni la k

def ratio_grafic():
    absolute_ratio = math.log2(L)
    words =read_file()
    ratio = list()
    num_char = list()
    real_entropy = list()
    num_words = list()
    for i in range(20):
        if i in words.keys():
            num_char.append(i)
            r = math.log2(words[i])/i
            ratio.append(r)
            real_entropy.append(r*i)

            num_words.append(words[i])


    plt.plot(num_char,ratio, '-gD')
    plt.xlabel("Num caracters")
    plt.ylabel("Ratio")
    plt.show()

    plt.plot(num_char,real_entropy, '-yD')
    plt.xlabel("Num caracters")
    plt.ylabel("Entropia real")
    plt.show()

    plt.plot(num_char,num_words )
    plt.xlabel("Num caracters")
    plt.ylabel("Num paraules")
    plt.show()

ratio_grafic()
