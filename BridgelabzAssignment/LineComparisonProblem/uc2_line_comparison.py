# UC2-comparing the length of two lines in coordinate geometry

print("Welcome to line comparison problem")

# taking inputs for Line 1
x1 = int(input("enter the x1-coordinate of point1 : "))
y1 = int(input("enter the y1-coordinate of point1 : "))
x2 = int(input("enter the x2-coordinate of point2 : "))
y2 = int(input("enter the y2-coordinate of point2 : "))

# taking inputs for Line 2
x3 = int(input("enter the x2-coordinate of point3 : "))
y3 = int(input("enter the y2-coordinate of point3 : "))
x4 = int(input("enter the x2-coordinate of point4 : "))
y4 = int(input("enter the y2-coordinate of point4 : "))

length_of_line1 = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
print("the length of line1 is : ", length_of_line1)

length_of_line2 = ((x4-x3)**2 + (y4-y3)**2)**(1/2)
print("the length of line2 is : ", length_of_line2)
if length_of_line1 == length_of_line2:
    print("Both lines are of equal length!!!")
else:
    print("Both lines are not equal!!!")

