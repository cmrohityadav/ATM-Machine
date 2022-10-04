
'''
Author:Rohit Chhabiraj Yadav
Email:cmrohityadav23@gmail.com
'''

print("Welcome to Love Calculator")
name1=input("what is your name?\n")
name2=input("what is your partner name?\n")

comb_str=name1+name2

lower_case_str=comb_str.lower()

t=lower_case_str.count("t")
r=lower_case_str.count("r")
u=lower_case_str.count("u")
e=lower_case_str.count("e")

true=t+r+u+e

l=lower_case_str.count("l")
o=lower_case_str.count("o")
v=lower_case_str.count("v")
e=lower_case_str.count("e")

love=l+o+v+e

love_score=str(true)+str(love)
print(f"your love score is {love_score}%")
