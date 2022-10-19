'''
7! = 5040. then shows all possible permutations of 7 numbers. like gacha randoms.
gacha ticket id to own num shows. 
column num - 1 = gacha ticket id shows status. 
eg:
arrange_id: 0 means: [1 2 3 4 5 6 7]
arrange_id: 1 means: [1 2 3 4 5 7 6]
...
arrange_id:5040 means:[7 6 5 4 3 2 1]
requirement: python3.6+, numpy, itertools.
usage: verflucht SPL leggendaria: random status can always set 1357246 or 2461753...etc.  or some other DP mode.
'''
import numpy as np
import itertools    
def trans_gacha_item(x):
    return np.vstack(list(itertools.permutations(x)))

if __name__ == '__main__':
    file = open('result.txt', 'w')
    a = trans_gacha_item(range(1,8))
    for item in a:
        file.write(str(item))
        file.write("\n")
    file.close()