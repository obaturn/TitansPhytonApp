tuple1 = 1,2,3
print(tuple1)
tuple1 = 1
print(tuple1)
tuple1 = (1,"ojo",2.5,0)
print(tuple1[1 ])#getting the element by their index
tuple1 = 1,2,3,[]
tuple1[3].extend([1,2.7,"tolu"])
print(tuple1)#adding list and tuple togetherl
tuple1 = 1,2,3,[]
tuple1[3].extend([1,2.7,"tolu"])
tuple1 +=1,6
print(tuple1)#adding more the tuple
name = ["obaturn" , "emmanuel"]
name += tuple1
names = tuple(name)
print(names)#adding list of string to tuple
name = ["obaturn" , "emmanuel"]
name += tuple1
names = tuple(name)
print(names.index("obaturn"))
print(names) # getting the index of string by name
# this is all you need to know about tuple
#now let talk about set to declare a set you have to use {}
x = {1,2,3}
print(type(x))
# to deeclare an empty set
x = set()
print(type(x))
# note that set do change the elemnent by their index but does not support you to change index by yourself
x = [1,1,2,3,2,2,4,5,1]
len(set(x))
print(len)# this is when u arevtrying to get the length
x = {1,2,3,4,5,6,7,8,9,"tlu"}
x.add(10)
print(x)# this is when you add to th set
x = {1,2,3,4,5,6,7,8,9,"tlu"}
y = {5,6,2,9}
x.add("tlu")
print(x.union(y))# union means you are addind two set together
print(x.difference(y))# diffrencies means you are subtracting two things of type set from each other
# now let start or talk about class and stack
class account:
    def __init__(self):  #this is called a constructor
        self.stack = [] # thie is know as default constructor cos we are not passing anything inside the list

        def add_to_stack(self , item):
           return self.stack.append(item)




