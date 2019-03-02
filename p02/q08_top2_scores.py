num = int(input("Number of students: "))
scores = {}
for i in range(num):
	score = int(input("Score: "))
	name = input("Name: ")
	scores[score] = name
x = {}
x = sorted(scores.keys(),reverse = True)
print("The highest score is {} with {}".format(scores.get(x[0]),x[0]))
print("The second highest score is {} with {}".format(scores.get(x[1]),x[1]))
