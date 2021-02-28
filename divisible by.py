lower= int(input("Enter the lower range :"))
upper= int(input("Enter the upper range :"))
for i in range (lower, upper+1):
    if(i%2==0):
        print(i)