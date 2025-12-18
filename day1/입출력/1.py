# 학생의 성적 데이터가 주어지고, 이를 내림차순으로 정렬한 결과를 출력하는 프로그램

# 입력예시
# 5명 성적:65 90 75 34 99

# 출력예시
# 99 90 75 65 34


#예시)공백을 기준으로 구분된 데이터를 입력 받을 때는 다음과 같이 사용합니다.
# list(map(int, input().split()))

#예시)공백을 기준으로 구분된 데이터의 개수가 많지 않다면, 단순히 다음과 같이 사용합니다.
# a,b,c = map(int, input().split())

#데이터의 개수 입력
n = int(input())
#각 데이터를 공백을 기준으로 구분하여 입력
data = list(map(int, input().split()))

data.sort(reverse=True)
print(data)