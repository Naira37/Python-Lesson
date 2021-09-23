# students = {
# 	"Jack":10,
# 	"Jane":9,
# 	"Ani":18,
# 	"Artur":18,
# 	"Vard":7,
# 	"Steven":16,
# 	"Simon":5, 
# 	"Anahit":4,
# 	"Hakob":14,
# 	"Arus":3
# }

# for i in students:
# 	if students[i]>9:
		
# 		print(i, students[i])



	

# students = {
# 	"Jack":10,
# 	"Jane":9,
# 	"Ani":18,
# 	"Artur":18,
# 	"Vard":7,
# 	"Steven":16,
# 	"Simon":5, 
# 	"Anahit":4,
# 	"Hakob":14,
# 	"Arus":3
# }

# count_rating = 0
# length = 0

# for i in students:
# 	length+= 1
# 	count_rating +=students[i]

# res = count_rating/length
		
# print(res)


# students = {
# 	"Jack":10,
# 	"Jane":9,
# 	"Ani":18,
# 	"Artur":18,
# 	"Vard":7,
# 	"Steven":16,
# 	"Simon":5, 
# 	"Anahit":4,
# 	"Hakob":14,
# 	"Arus":3
# }

# name = input('name ')
# if name in students:

# 	print('Yes', name, students[name])
# else:
#     print('No ')	

 
# s ='a,2,b,5,c,8,a,4,e,11'.split(',')

# # res = {}

# # for i in range(0,len(s),2):
# 	# print(s[i],s[i+1])
# res = {}

# for i in range(0, len(s), 2):
# 	if s[i] in res:
# 		res[s[i]] += int(s[i+1])

# 	else:
# 		res[s[i]] =int(s[i+1])

# print(res)


# word = 'exercises'

# res = {}

# for i in word:

# 	res[i] = word.count(i)

# print(res)

# old_list = [{'key1':'value1'},{},{},{'key1':'value1'},{'key2':'value2'}]


# c = []

# for i in old_list:
# 	if i not in c:
# 		c.append(i)
# print(c)		

# c = 0
# for i in range(len(old_list)):
# 	if old_list.count(old_list[c]) > 1:
# 		old_list.remove(old_list[c])
# 	else:
# 	    c+=1
# print(old_list)	   

# c = ['1','2','3','4','5','6','7','8']
# z = []
# for i in range(0, len(c), 2):
#    res = c[i] + c[i+1]
#    z.append(res)
# print(z) 

questions = {
	'question 1':{
	    'q': ['When was the battle of Avarayr\na)160 b)451 c)452 d)400', 'c'],

    },
    'question 2':{
	     'q':['What is the hight of the Everest \na)8000 b)8400 c)5451 d)8849', 'd']

	}
}
for i in questions:
	print(i)
	print(questions[i]['q'][0])
	ans = input('ans: ')
	if ans == questions[i]['q'][1]:
		print('right')

	else:
		print('wrong')