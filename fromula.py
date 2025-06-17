mydict.keys()return all keys
mydict.value()return all value
mydict.itmes()return all(key,value)pair as tuple
mydict.get("key")return the key according to value
mydict.update(newdict)insert specific items to dict
mydict.len()return all length
mydict.pop()remove random ele

set.add(el)add on element
set.remove(el)remove the ele an
set.clear()empty the set
set.pop()remove an random ValueError
set.union(set)combine both set value and return new
set.intersection(set)combine common value and return new


write a programme to enter marks of three subject from the user and store them  in a dict start with an empty dict and add one by one use sub 
name as key mark as value.
marks={}
a=int(input('enter hindi'))
marks.update({"hindi":a})
a=int(input("enter urdu"))
marks.update({"urdu":a})
a=int(input("enter eng"))
marks.update({"eng":a})
print(marks)