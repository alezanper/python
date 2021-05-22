# Using for with range
for i in range(10):
    print("The value of i is currently", i)

# from 2 to 7
for i in range(2, 8):
    print("The value of i is currently", i)

# Using break
print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")

# Using continue
print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")

# String
print("\nAnalyze and transform a string")
text = "pyxpyxpyx"
for letter in text:
    if letter == "x":
        continue
    print(letter, end="")
