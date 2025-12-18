#빠르게 입력 받기

import sys

#문자열 입력 받기
data = sys.stdin.readline().rstrip()
print(data)

#자주 사용되는 표준 출력 방법

# 출력할 변수들
a = 1
b = 2
print(a, b)
print(7,end=" ")
print(8)

# 출력할 변수
answer = 7
print(" 정답은 "+str(answer)+"입니다.")

print(f" 정답은 {answer}입니다.")