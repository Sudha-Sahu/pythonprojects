# UC4-line comparison using function

def compare_2_lines():
    # taking inputs for Line 1
    x1 = int(input("enter the x-coordinate of point1 : "))
    y1 = int(input("enter the y-coordinate of point1 : "))
    x2 = int(input("enter the x-coordinate of point2 : "))
    y2 = int(input("enter the y-coordinate of point2 : "))

    # taking inputs for Line 2
    x3 = int(input("enter the x-coordinate of point3 : "))
    y3 = int(input("enter the y-coordinate of point3 : "))
    x4 = int(input("enter the x-coordinate of point4 : "))
    y4 = int(input("enter the y-coordinate of point4 : "))

    length_of_line1 = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
    print("the length of line1 is : ", length_of_line1)

    length_of_line2 = ((x4-x3)**2 + (y4-y3)**2)**(1/2)
    print("the length of line2 is : ", length_of_line2)

    diff = length_of_line1-length_of_line2
    if diff > 0:
        print("line1 is greater!!!")
    elif diff < 0:
        print("line2 is greater!!!")
    else:
        print("Both lines are of same length")

print("Welcome to line comparison problem")

# calling a function
compare_2_lines()
