this_set = {"orange", "lemon", "plum"}
for x in this_set:
 print(x)

this_set1 = {"orange", "lemon", "plum"}
this_set2 = {"good", "bad","sad"}
print(this_set1, this_set2)
 
thisset = {"orange", "lemon", "plum"}
thisset.add("apple")
print(thisset)


thisset = {"orange", "lemon", "plum"}
thisset.update({"apple", "banana"})
print(thisset)

thisset = {"orange", "lemon", "plum", "apple", "banana"}
thisset.remove("apple")
print(thisset)

thisset = {"orange", "lemon", "plum", "apple", "banana"}
thisset.discard("orange")
print(thisset)


this_set1 = {"and", "or", 24}
this_set1.issubset("nor")
print(this_set1)

this_set1 = {"and", "or", 24}
this_set1.issuperset("nor")
print(this_set1)

this_set1 = {"and", "or", 24}
this_set1.clear()
print(this_set1)



this_set1 = {"and", "or", 24}
this_set2 = {"none", 56, "nor"}
this_set3 = this_set1.union(this_set2)
print(this_set3)


this_set = {"and", "or", 24, "none"}
this_set.symmetric_difference("and")
print(this_set)

