array = [9, 8 ,7, 6, 5]

for x in array:
    print(x)



result = 0

for i in range(1, 10):
    if i%2==0:
        continue
    else:
        result +=i

print(result)

score = [90,85,77,65,97]

for i in range(5):
    if score[i] >=80:
        print(i+1,"번 학생은 합격입니다.")