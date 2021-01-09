# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
S = 15
M = 20
L = 25
N = 0
Y = 2
if size == S:
  print("15")
if size == M:
  print("$20")
if size == L:
  print("$25")

if add_pepperoni == Y:
  S += 2
  M += 2
  L += 2
 
if extra_cheese == Y:
  S += 2

print(f"your total {S}")






