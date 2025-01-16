'''
# Question 1: Checks if two input temperatures are the same

temperature1 = input("What is the first temperature? ")
temperature2 = input("What is the second temperature? ")

if int(temperature1) == int(temperature2):
    print(temperature1 + " and " + temperature2 + " are equal!")
else:
    print(temperature1 + " and " + temperature2 + " are NOT equal!")

# Question 2: Finds the middle value of three input temperatures

temp1 = int(input("What is the first temperature? "))
temp2 = int(input("What is the second temperature? "))
temp3 = int(input("What is the third temperature? "))

# organizes temp1, temp2, temp3 in a way such that value for temp1 < temp2 < temp 3
min_value = min(temp1,temp2)
temp2 = max(temp1,temp2)
temp1 = min_value
min_value = min(temp2,temp3)
temp3 = max(temp2,temp3)
temp2 = min_value
min_value = min(temp1,temp2)
temp2 = max(temp1,temp2)
temp1 = min_value

temp_values = (temp1,temp2,temp3)    # the element with index 1 has the middle value of the three temperatures         

print("The middle value of the three temperatures is " + str(temp_values[1]) + ".") 

# Question 3: Describes what a given temperature feels like

temp = int(input("Input the temperature: "))

if temp <= 0:
  describe = "freezing"
elif temp < 10:
  describe = "cold"
elif temp < 20:
  describe = "chilly"
elif temp < 30:
  describe = "warm"
elif temp < 40:
  describe = "hot"
else:
  describe = "extremely hot"

print("The temperature is " + describe + "!")    '''

# Question 4: Prompts user to input two values in order, and determines which quadrant the coordinate of the pair lies on

# Asks user to input two values in order
x = int(input("Input the value for the X coordinate: "))
y = int(input("Input the value for the Y coordinate: "))
coordinate = "(" + str(x) + "," + str(y) + ")"    # creates coordinate as a string for concatenation later


# Conditional statments to test where the paris of ordered coordinates lie
if x == 0 and y == 0:
    print("The point (0, 0) lies at the origin.")
elif x == 0 or y == 0:
    print("The point " + coordinate + " lies on a border between two quadrants.")
elif x > 0 and y > 0:
    print("The point " + coordinate + " lies in Quadrant I.")
elif x > 0 and y < 0:
    print("The point " + coordinate + " lies in Quadrant IV.")
elif x < 0 and y > 0:
    print("The point " + coordinate + " lies in Quadrant II.")
else:
    print("The point " + coordinate + " lies in Quadrant III.") 

'''
# Conditional statements (using nested if statements) to test where the pairs of ordered coordinates lie
if x == 0 and y == 0:
    print("The point (0, 0) lies at the origin.")
elif x == 0 or y == 0:    # checks if at least one of x or y is equivalent to 0, since both cannot be 0 when the if statment is false
    print("The point " + coordinate + " lies on a border between two quadrants.")
elif x > 0:
    if y > 0:
        print("The point " + coordinate + " lies in Quadrant I.")    # Quadrant I is positive x and y
    if y < 0:
        print("The point " + coordinate + " lies in Quadrant IV.")   # Quadrant IV is positive x and negative y
elif x < 0:
    if y > 0:
        print("The point " + coordinate + " lies in Quadrant II.")   # Quadrant II is negative x and positive y
    if y < 0:
        print("The point " + coordinate + " lies in Quadrant III.")  # Quadrant III is negative x and y
'''







