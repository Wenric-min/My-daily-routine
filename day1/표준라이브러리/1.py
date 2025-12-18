#내장함수: 기본 입출력 함수부터 정렬 함수까지 기본적인 함수들을 제공합니다.
    #파이썬 프로그램을 작성할 때 없어서는 안 되는 필수적인 기능을 포함하고 있습니다.
      
result = sum([1,2,3,4,5])
print(result)

min_result = min(7,3,5,2)
max_result = max(7,3,5,2)
print(min_result,max_result)

result = eval("(3+5)*7")
print(result)
print("")
print("-----------sort------------")
print("")
# sorted()
result = sorted([9,1,8,5,4])
reverse_result = sorted([9,1,8,5,4], reverse=True)
print(result)
print(reverse_result)
print("")
print("-----------sort wiht key------------")
print("")
# sorted() with key
array= [('홍길동',50),('이순신',32),('아무개',74)]

result = sorted(array, key=lambda x: x[1], reverse=True)
print(result)


#itertools: 파이썬에서 반복되는 형태의 데이터를 처리하기 위한 유용한 기능들을 제공합니다.
    #특히 순열과 조합 라이브러리는 코딩 테스트에서 자주 사용됩니다.

from itertools import product
data = ['A','B','C'] #데이터 준비
result = list(product(data, repeat=2))
print(result)
print("")
from itertools import combinations_with_replacement
data =['A','B','C'] #데이터 준비
result = list(combinations_with_replacement(data,2))
print(result)
print("")
#heapq:힙(heap) 자료구조를 제공합니다.
    #일반적으로 우선순위 큐 기능을 구현하기 위해 사용됩니다.

#bisect: 이진탐색(Binary Search)기능을 제공합니다.

#collections: 덱(deque), 카운터(Counter)등의 유용한 자료구조를 포함합니다.
from collections import Counter
counter = Counter(['red','blue','red','green','blue','blue'])

print(counter['blue'])
print(counter['green'])
print(counter['red'])
print(dict(counter))
print("")
#math: 필수적인 수학적 기능을 제공합니다.
    #팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수 관련 함수부터 파이(pi)와 같은 상수를 포함합니다.

import math

#최소공배수 (LCM)를 구하는 함수
def lcm(a,b):
    return a*b // math.gcd(a,b)

a= 21
b= 14

print(math.gcd(21, 14)) #최대 공약수(GCD) 계산
print(lcm(21, 14)) #최대 공배수(LCM) 계산