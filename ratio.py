
import math
from utils import *

L = 25 # considerem 25 caracters en catala contant la ç pero no contant la w ni la k


def ratio_input():

    words =read_file()
    n = int(input("Entreu un nombre de caracters n per calular-ne la ratio: "))
    if n not in words.keys():
        print("No hi ha paraules amb aquest nombre de caracters.")
    else:
        n_char_num = words[n]
        real_ratio = math.log2(n_char_num)/n
        absolute_ratio = math.log2(L)
        print("Hi ha un total de {} paraules de {} caracters".format(words[n],n))
        print("La ratio absoluta: {}".format(absolute_ratio))
        print("La ratio real per {} caracters: {}".format(n, real_ratio))
        print("Entropia per {} caracters: {}".format(n,real_ratio*n))



ratio_input()
