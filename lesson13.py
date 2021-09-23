# example = ('questio1', ('question2', 'question3'),True,12,15)
# print(example[0])

# print(example[-1])

# print(example[2:4])

# example = ('questio1', ('question2', 'question3'),True,12,15)
# x = 7
# print(example.__sizeof__())
# print(x.__sizeof__())

# exstr = "('questio1', ('question2', 'question3',) True, 12, 15)"

# print(extr.__sizeof__())

# thistuple = ("apple", "banana", "chery" )
# print(len(thistuple))

# my__tuple = tuple(range(100))
# print(my__tuple)

# thistuple = ("apple", "banana", "chery" )
# print(thistuple.count('banana'))

# thistuple = ("apple", "banana", "chery" )
# if "apple" in thistuple:
#  print("Yes 'apple' is in the fruits tuple")

# shop = ("Mars", "coca-cola", "apple", "coca-cola")

# user = input('Product name: ')

# if user in shop:
# 	count_pr = shop.count(user)
# 	print('yes we have this', user, 'count is', count_pr)

# else:
# 	print("sorry we don't have this", user, 'count is 0')

# thistuple = ("apple", "banana", "cherry")
# for x in thistuple:
# 	print(x,end='\n------\n')

# thistuple = ("apple", "banana", "cherry")
# for x in thistuple:
# 	if x == 'banana':
# 		continue
# 	print(x)

# x = (5, 10, 15, 20)

# y = reversed(x)
# print(tuple(y))

# thistuple = ("apple", "banana", "chery", "orange", "kiwi", "melon", "mango")
# print(thistuple[-4:-1])
# print(thistuple[-1])


# thistuple = tuple(range(12))
# print(thistuple[1:12:2])

# thistuple = ('Ani', 'Anna', 'Jor')

# print(thistuple[::-1])

# tuple1 = ("a", "b", "c",)
# tuple2 =(1, 2 , 3)
# tuple3 = tuple1 + tuple2
# print(tuple3)


# num = (10, 20, 30, (10, 20), 40)
# c = 0
# for n in num:
# 	if isinstance(n, tuple):
# 		break
# 	c+=1
# print(c)		

tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's' )
mystr = ''.join(tup)
print(mystr)
