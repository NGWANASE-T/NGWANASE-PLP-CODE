name = input("Hello, Please input your name_")
numb1 = int(input("input first number>"))
operator = input("operator > -")
numb2 = int(input("input Second number>"))


if operator == "+":
    ans=numb1+numb2
elif operator == '-':
    ans=numb1-numb2
elif operator == '/':
    ans=numb1/numb2
elif operator == '*':
    ans=numb1*numb2
elif operator == '^':
    ans= numb1^numb2

print( name + " your answear is " + str(ans))
