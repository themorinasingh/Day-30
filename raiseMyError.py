# Why would be creating our own error?
# Ans: to ensure we can make sure the data we are handling is accurate, for ex this program

height = int(input("height"))
weight = int(input("weight"))
NonHumanlyHeightError = ""
if height > 2.5:
    raise ValueError("Height must be under 2.5 meters")

bmi = weight / height ** 2
print(bmi)