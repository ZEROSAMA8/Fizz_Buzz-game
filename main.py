#Write your code below this row 👇

for fizz_buzz in range(1,101):
 if fizz_buzz % 3==0 and fizz_buzz % 5==0:
   print("FizzBuzz")
 # number= print(fizz_buzz)  
 elif fizz_buzz % 3==0:
  print("Fizz")
 elif fizz_buzz % 5==0:
  print("Buzz")
 else:
   print(fizz_buzz)

