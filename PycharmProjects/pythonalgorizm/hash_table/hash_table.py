import hashlib


class HashTable(object):
    def __init__(self, size=10) -> None:
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash(self, key) -> int:
        # ある文字をハッシュ化して一意に定めてあげる
        # １６進数で帰ってくる
        # これをコンストラクタで定めたsizeで割ってあげるとあまりが出てきてsizeに分けられる
        return int(hashlib.md5(key.encode()).hexdigest(), base=16) % self.size

    # さらにリストでついかしたい時
    def add(self,key,value) ->None:
        index =self.hash(key)
        for data in self.table[index]:
            if data[0]==key:
                data[1] =value
                break
        else:
            self.table[index].append([key,value])


    def print(self) ->None:
        for index in range(self.size):
            # endで改行なしのprint
            print(index, end=' ')
            for data in self.table[index]:
                print('-->',end=' ')
                print(data,end=' ')
            print()

    from typing import Any
    def get(self,key) ->Any:
        index =self.hash(key)
        for data in self.table[index]:
            if data[0] ==key:
                return data[1]

if __name__ == '__main__':
    hash_table =HashTable()
    print(hash_table.add('car','mamushi'))
    print(hash_table.add('car', 'ms'))
    print(hash_table.table)
