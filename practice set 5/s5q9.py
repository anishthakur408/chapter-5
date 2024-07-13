# Can you change the values inside a list which is contained in set S? 
# s = {8, 7, 12, "Harry", [1,2]} 


s = {8, 7, 12, "lol", [1,2]} 



# this is can not change



# output
"""Traceback (most recent call last):
  File "d:\python\chapter 5\practice set 5\s5q9.py", line 5, in <module>
    s = {8, 7, 12, "lol", [1,2]}
        ^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: unhashable type: 'list'"""