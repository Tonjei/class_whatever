userDistance = int(input("What is the distance you'd like to convert to meters? "))
userUnits = input("What are the input units? ")

if userUnits == "feet":
    print(userDistance * .3048, " meters")

elif userUnits == "yards":
    print(userDistance * .9144, " meters")

elif userUnits == "inches":
    print(userDistance * .0254, " meters")

elif userUnits == "miles":
    print(userDistance * 1609.34, " meters")

elif userUnits == "meters":
    print(userDistance * 1, " meters")

elif userUnits == "kilometers":
    print(userDistance * 1000, " meters")

else:
    print("error somewhere")

# 1 ft is 0.3048 m
# 1 mi is 1609.34 m
# 1 m is 1 m
# 1 km is 1000 m