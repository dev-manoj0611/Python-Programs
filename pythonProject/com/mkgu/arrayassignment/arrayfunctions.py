#1.len()
import array as arr
a=arr.array('u',['a','b','c','d'])
print(len(a)) #available
#2.max()
b=arr.array('u',['a','b','c','d'])
print(max(b)) #available
#3.min()
c=arr.array('u',['a','b','c','d'])
print(min(c)) #available
#4.append()
d=arr.array('u',['a','b','c','d'])
d.append('e') #available
print(d)
#5.extend()
e=arr.array('u',['a','b','c','d'])
e.extend('e') #available
print(e)
#6.insert()
f=arr.array('u',['a','b','c','d'])
f.insert(4,'e') #available
print(f)
#7.clear()
# g=arr.array('u',['a','b','c','d'])
# g.clear() #not available
# print(g)
#8.del variable[:]
h=arr.array('u',['a','b','c','d'])
del h[:] #available alternative for clear()
print(h)
#9.copy()
#a.= operator
i=arr.array('u',['a','b','c','d'])
j=i
print(j, i)
print(id(j), id(i)) #1342383702960 1342383702960 shallow copy
#b.copy()
import copy
i2=copy.copy(i)
print(i,i2)
print(id(i),id(i2))#1342383702960 1342383703040 deep copy
#c.copy.deepcopy()
i3=copy.deepcopy(i)
print(i,i3)
print(id(i),id(i2))#1176745542656 1176745542736 deep copy
#10.index()
k=arr.array('u',['a','b','c','d'])
print(k.index('b')) #available
#11.pop()
l=arr.array('u',['a','b','c','d'])
l.pop() #available
print(l)
#12.remove()
m=arr.array('u',['a','b','c','d'])
m.remove('a') #available
print(m)
#13.reverse()
n=arr.array('u',['a','b','c','d'])
n.reverse()
print(n) #available
#14.sort()
o=arr.array('u',['c','d','a','b'])
print(sorted(o)) #sorted() -> available
#sort() -> not available
#15.concatenation
p=arr.array('u',['c','d','a','b'])
q=arr.array('u',['m','a','n','u'])
print(p+q) #concatenation available