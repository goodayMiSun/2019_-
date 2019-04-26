"""
입력 : 
 n: 학생수 k: 같은 국적인 학생 쌍수
 a b : 같은 국적인 학생 쌍

출력 :
 같은 국적이 아닌 대표 두명을 뽑을 수 있는 경우의 수 

입력
 3 1
 1 2 
출력 
 2
=> [[1, 2], [3]] 이므로 대표를 뽑는 방법은 (1, 3), (2, 3) 총 2가지
"""

n, k = map(int, input().split())

student = list()

for i in range(n) : 
	
	student.append([i+1])
	
i=1
while i<=k :
	print(k)
	a,b = map(int, input().split())
	
	for j in range(len(student)) :
		
		
		if student[j].count(a) and student[j].count(b) == 0:
			student[j].append(b)
			student.remove([b])
			break
		
		if student[j].count(b) and student[j].count(a) == 0: 
			student[j].append(a)
			student.remove([a])
			break
	print(student)
	i+=1
	
percent = 0
	
for i in range(len(student)) :
		
	for j in range(i+1, len(student)) :
			
		percent+= len(student[i]) * len(student[j])
			 
			
		
print(percent)	


	
