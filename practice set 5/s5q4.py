# What will be the length of following set s: 
# s = set() 
# s.add(20) 
# s.add(20.0) 
# s.add('20') # length of s after these operations? 

s = set() 
s.add(20)
s.add(20.0)  # in python 2==2.0 , so it is print lenth of this is 2
s.add('20') 



print(len(s))