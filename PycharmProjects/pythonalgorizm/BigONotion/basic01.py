# O(log(n))
def func2(n):
    if n <=1:
        return
    else:
        print(n)
        func2(n/2)

func2(10)

# 実行結果
# 10
# 5.0
# 2.5
# 1.25


# O(n)
def func3(numbers):
    for num in numbers:
        print(num)

func3([1,2,3,4,5])



# O(n*logn)
def func4(n):
    for i in range(int(n)):
        print(i ,end=' ')

    print()

    if n <=1:
        return
    func4(n/2)

func4(10)

# 実行結果
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4
# 0 1
# 0


# O(n**2)

def func5(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            print(numbers[i],numbers[j])

func5([1,2,3,4,5])


