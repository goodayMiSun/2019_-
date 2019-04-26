
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


	
