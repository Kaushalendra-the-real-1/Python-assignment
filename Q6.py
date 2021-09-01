def divGen(n):
    for i in range(n):
        if ((i%5 == 0) and (i%7 == 0)):
            yield i

user_input = int(input("Enter a number \n"))
gen = divGen(user_input)
for i in gen:
    print(i,end=",")

