# UC1-calculating the length between two points

print("Welcome to line comparison problem")

# taking inputs for point 1
x1 = int(input("enter the x1-coordinate of point1 : "))
y1 = int(input("enter the y1-coordinate of point1 : "))

# taking inputs for point 2
x2 = int(input("enter the x2-coordinate of point2 : "))
y2 = int(input("enter the y2-coordinate of point2 : "))

length_of_line = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
print("the distance between two point is : ", length_of_line)
