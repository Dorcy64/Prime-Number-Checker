#Write your code below this line 👇

def prime_checker(number):
	is_not_prime = False
	for x in range(2, number):
		if number % x == 0:
			is_not_prime = True

	if is_not_prime == False:
		print("It's a prime number.")
	elif is_not_prime == True:
		print("It's not a prime number.")

		
	


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



