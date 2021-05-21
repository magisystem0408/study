from typing import Any

# パケットで使われる

class Queue(object):
    def __init__(self) ->None:
        self.queue =[]

    # 追加
    def enqueue(self,data:Any)->None:
        self.queue.append(data)

    # 削除
    def dequeue(self)->Any:
        if self.queue:
            return self.queue.pop(0)

if __name__ =='__main__':
    q =Queue()
    q.append(1)
    q.enqueue(1)