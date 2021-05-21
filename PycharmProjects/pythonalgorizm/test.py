from collections import Counter
import operator
from typing import Tuple

def count_chars_v1(string:str)->Tuple[str,int]:
    string=string.lower()
    l =[]
    for char in string:
        if not char.isspace():
            l.append((char,string.count(char)))

    return max(l,key=operator.itemgetter(1))


if __name__ == '__main__':
    t='This is a pen. This is an apple. Applepen.'
    print(count_chars_v1(t))