# find eucliean distance between two points

def calc_distance(x, y):
    distance = (x*x + y*y)**(1/2)
    return f"the Eucliean Distance of a point ({x},{y}) from origin (0,0) is : {distance}"


if __name__ == "__main__":
    try:
        # taking input from user for calculating distance of a point from origin
        point1 = int(input("Enter the x-coordinate of a point :"))
        point2 = int(input("Enter the y-coordinate of a point :"))
        print(calc_distance(point1, point2))
    except Exception:
        print("invalid input from user")
