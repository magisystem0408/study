from typing import List
import secrets


def selection_sort(numbers:List[int])-> List[int]:
    len_numbers =len(numbers)
    for i in range(len_numbers):
        min_idx =i
        # startライン定義
        for j in range(i+1,len_numbers):
            if numbers[min_idx] >numbers[j]:
                min_idx =j

        # 入れ替え
        numbers[i],numbers[min_idx] = numbers[min_idx],numbers[i]
    return numbers


if __name__ =="__main__":
    num =[secrets.SystemRandom().randint(0,1000) for _ in range(10)]
    print(num)
    print(selection_sort(num))
