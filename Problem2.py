# find the total number of carrying operations required when those two numbers are added
# Python3 implementation of above problem 

# Function to count the number of carry operations 
def count_carry(a, b): 

	# Initialise the value of carry to 0 
	carry = 0; 

	# Counts the number of carry operations is zero
	count = 0; 

	# Initialise len_a and len_b with the sizes of strings 
	len_a = len(a); 
	len_b = len(b); 

	while (len_a != 0 or len_b != 0): 

		# Assigning the ascii value of the character 
		x = 0; 
		y = 0; 
		if (len_a > 0): 
			x = int(a[len_a - 1]) + int('0'); 
			len_a -= 1; 
		
		if (len_b > 0): 
			y = int(b[len_b - 1]) + int('0'); 
			len_b -= 1; 

		# Add both numbers/digits 
		sum = x + y + carry; 

		# If sum > 0, icrement count and set carry to 1 
		if (sum >= 10): 
			carry = 1; 
			count += 1; 

		# Else, set carry to 0 
		else: 
			carry = 0; 

	return count; 

#CASE1
if __name__ == "__main__" :

    a = "1234"; 
    b = "5678"; 

count = count_carry(a, b); 
if (count == 0): 
	print("0"); 
elif (count == 1): 
	print("1"); 
else: 
	print(count); 

#CASE2
if __name__ == "__main__" :

    a = "15426"; 
    b = "56784"; 

count = count_carry(a, b); 
if (count == 0): 
	print("0"); 
elif (count == 1): 
	print("1"); 
else: 
	print(count); 

#CASE3
if __name__ == "__main__" :

    a = "1234"; 
    b = "0000"; 

count = count_carry(a, b); 
if (count == 0): 
	print("0"); 
elif (count == 1): 
	print("1"); 
else: 
	print(count); 

#CASE4 GET VALUE FROM USER
if __name__ == "__main__" :

    a =input("Enter your value of a :")
    b =input("Enter your value of b :") 

count = count_carry(a, b); 
if (count == 0): 
	print("0"); 
elif (count == 1): 
	print("1"); 
else: 
	print(count); 

#CASE5 
if __name__ == "__main__" :

    a = "1234"; 
    b = "1111"; 

count = count_carry(a, b); 
if (count == 0): 
	print("0"); 
elif (count == 1): 
	print("1"); 
else: 
	print(count); 

#CASE6
if __name__ == "__main__" :

    a = "7777"; 
    b = "7777"; 

count = count_carry(a, b); 
if (count == 0): 
	print("0"); 
elif (count == 1): 
	print("1"); 
else: 
	print(count);     