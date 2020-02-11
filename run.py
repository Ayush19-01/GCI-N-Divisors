#Made for the sole purpose of GCI 2019
import math 


def count_div(num) : 
    y=0
    for div in range(1,(int)(math.sqrt(num))+1): #Loop iterates till the square root of the number, this way we can add two numbers to the list of divisors if the remainder is 0 and they are not same
        if (num % div == 0) : 
            if num/div == div :  # As both the numbers are same, only one is added to the count
                y+=1
            else : # As both the numbers are diffrent, so count is incremented by 2, hence leaving the option to calculate all the dividiond
            	y+=2
    return y 
    
#This loop asks the user to enter the number N and runs until the user wants to quit. Makes it easier to check divisors for multiple numbers while running.  
while True:
	print()
	N=int(input("Enter a positive integer between 1 and 1000000 : "))
	print()
	print("Total number of divisors of "+str(N)+" are : ", count_div(N)) 
	print()
	x=input("Do you wish to continue?[y/N]:")
	print()
	if x=="y":
		continue
	else:
		print("Closing...")
		break
