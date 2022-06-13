# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 07:11:48 2022

@author: manju sapkota
"""
#array
"""
from array import array#step1
nums=array('i',[60,7,8,9,6])
nums[0]=55;#updtae
print(nums)
print(nums[3])
print(nums)
"""

from array import array
student_Marks=array('i',[67,43,23,56])

#print(student_Marks)
total_marks=student_Marks[0]+student_Marks[1]+student_Marks[2]+student_Marks[3]
print(total_marks)
#average of obtain marks
average_marks=total_marks/4
print(average_marks)
student_Marks[2]=73
total_marks=student_Marks[0]+student_Marks[1]+student_Marks[2]+student_Marks[3]
average_marks=total_marks/4
print(total_marks)
print(average_marks)
print(max(student_Marks))
print(min(student_Marks))
print(sum(student_Marks))
print(len(student_Marks))




#print(help(array))
 #task
 #create and array to store 4 obtain marks of student
 #find max obtained mark
 #calculate result of student (pm=40)?



