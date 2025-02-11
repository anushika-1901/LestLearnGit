# print("Hello world")
# print("Hi everyone how are you")
# i=0
# while(i<10):
#     print(i)
#     i=i+1

# for i in range(0,10):
#     print(i)
#     i=i+1

# n=int(input("Enter the value of number "))
# if n%3==0:
#     print("Yes")
# else:
#     print("Number is not divisible by 3")

# n=int(input("Enter the value of number :"))
# if n%2==0:
#     print("Even")
# else:

#     print("Odd")

# age=int(input("Enter the age :"))
# if age>18:
#     print("Old enough")
# else:
#     print("Too young")

# name=input("Enter the name :")
# if name=='Anushika':
#     print("Your name is same")


# start=int(input("Enter the value of start :"))
# end=int(input("Enter the value of end :"))
# if start>end:
#     print("You have entered wrong range :")

# for i in range(start,end):
#     print(i)


# for i in range(0,100):
#     if i%2==1:
#         print(f"The odd number is {i}")

# for i in reversed(range(0,100)):
#     print(i)

# number=int(input("Enter the value of num :"))
# for i in range(0,11):
#     # print(i)

#     print(f"{number}*{i}={number*i}")
# start=int(input("Enter the value of start :"))
# end=int(input("Enter the value of end :"))
# if start>0:
#     start=start*-1
# if end>0:
#     end=end*-1
# for i in range(start,end):
#     print(i)

# start=int(input("Enter the value of start :"))
# end=int(input("Enter the value of end :"))
# for i in range(start,end+1):
#     if i>=end:
#         print("Done")
#     else:
#         print(i)

# start=int(input("Enter the value of start :"))
# end=int(input("Enter the value of end :"))
# for i in range(start,end+1):
#     print(i**2)

# i=0
# check=True 
# while check:
#     print(f"The number is {i}")
#     if i>=10:
#         check=False
#     i=i+1





#print table using while loop
# i=0
# n=int(input("Enter the number :"))
# while(i<=10):
#     print(f"{n}*{i}={n*i}")
#     i=i+1


# start=int(input("Enter the value of start :"))
# end=int(input("Enter the value of end :"))
# while(start<=end):
#     print(start)
#     start+=1

# start=int(input("Enter the value of start :"))
# end=int(input("Enter the value of end :"))
# while (start<=end+1):
#     print(start)
#     if start>end:
#         print("Done")

#     start=start+1


# start=int(input("Enter the value of start :"))
# end=int(input("Enter the value of end :"))
# # i=0
# start=0
# while (start<=end):
#     print(start**2)
#     start=start+1

# start=int(input("Enter the value of start :"))
# end=int(input("Enter the value of end :"))
# while start<=end:
#     print(f"The table of {start}")
#     for i in range(1,11):
        
#         print(f"{start}*{i}={start*i}")
#     start=start+1



# number=int(input("Enter the number :"))
# user_str=input("Enter the string")
# i=0
# result=""
# while i<number:
#     result+=user_str+" "
#     i+=1
# while number:
#     print(result)
#     number=number-1

#break,continue and pass
text="aaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
# for t in text:
#     pass

for t in text:
    if t!='a':
        continue
