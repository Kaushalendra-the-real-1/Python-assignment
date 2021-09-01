# 8. Write a program which can map() to make a list whose elements are square of numbers
# between 1 and 20 (both included).
List = (i for i in range(1,21))
ans = map(lambda x:x*x,List)
print(list(ans))