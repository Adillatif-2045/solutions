print("Enter no to check its prime or not")
no = int(input())
sum= 0
if no > 1:

    for n in range(2, no):
        if(no%n) == 0:

            print(-1)
            break
        else:

            print(no, "is prime no")

            for i in range(0, no+1):
                sum +=i
            print("Total sum is : "+ str(sum))
            break




















