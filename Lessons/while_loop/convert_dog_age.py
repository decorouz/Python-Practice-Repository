# """A program that converts a dog age"""

# Given the program below
dog_age = int(input("Age of the dog: "))
if dog_age <= 0:
    human_age = -1
elif dog_age == 1:
    human_age = 14
else:
    # this means: dog_age >= 2:
    human_age = 22 + (dog_age - 2) * 5

if human_age > 0:
    print("Corresponds to  " + str(human_age) + " human years!")
else:
    print("Negative values or zero makes no sense for a dog age!")

# Write a version with a while loop so that people can keep on converting dog ages.
# 0 or a negative value means that they want to finish.

dog_age, human_age = 0, 0

while dog_age == human_age:
    dog_age = int(input("Enter the Age of the Dog: "))
    if dog_age <= 0:
        human_age = -1
        print("Sorry to see you finish. Zero or negative years are not a valid input")
        break
    if dog_age == 1:
        human_age += 14
    else:
        human_age = 22 + (dog_age - 2) * 5

else:
    print(f"Corresponds to {human_age} human years!")
