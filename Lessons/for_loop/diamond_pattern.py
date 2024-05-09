# Create a program that prints a diamond pattern using asterisks (*) like the example below:
""" 
      *      
     ***     
    *****    
   *******   
  *********  
 *********** 
  *********  
   *******   
    *****    
     ***     
      * 
"""

# Get the height of the diamond from user
height = int(input("Enter the height of the diamond: "))

height_is_even = height % 2 == 0
middle = height // 2 if height_is_even else height // 2 + 1


# Upper half of the diamond
spaces = "*"
for counter in range(0, middle):
    print(spaces.center(middle * 2 + 1))
    spaces += "**"

# Second half of the diamond
spaces = spaces[:-2]
if height_is_even:
    # Previous line has to be duplicated
    print(spaces.center(middle * 2 + 1))
while len(spaces) > 1:
    spaces = spaces[:-2]
    print(spaces.center(middle * 2 + 1))
