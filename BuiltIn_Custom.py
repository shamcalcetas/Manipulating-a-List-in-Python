# Finding the Maximum and Minimum Value (Built-in and Customization)

our_age = [18, 20, 22, 24, 26]

def maxCustom(our_age):
    max_age = 0
    for age in our_age:
        if age > max_age:
            max_age = age
    return max_age

# Built-in Function
print("The max is ", max(our_age))
print("The min is ", min(our_age))

# Custom Function
print(maxCustom(our_age))