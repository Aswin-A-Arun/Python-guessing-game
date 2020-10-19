Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> lower = int(input("Emter starting number:  ")) 
upper = int(input("Enter Ending number : ")) 
x = random.randint(lower, upper)
print("\n\tYou've only ", round(math.log(upper - lower + 1, 2))," chances to guess the integer!\n")
count = 0
while count < math.log(upper - lower + 1, 2):
	count += 1
	guess = int(input("Guess a number:- ")) 
	if x == guess: 
	print("Congratulations you did it!!", count, " try")
	break
	elif x > guess:
	print("You guessed it too tiny!!!")
	elif x < guess:
	print("You Guessed it too Biggg!!!!")
if count >= math.log(upper - lower + 1, 2):
print("\nThe number is %d"%x)
print("\tBetter Luck Next time!")

Emter starting number:  