import math


def main():
    while True:
        shapes = ["triangle", "rectangle", "circle"]
        shape = str(input("Choose a shape (triangle, rectangle, circle): "))
        if shape == "":
            break

        if shape not in shapes:
            print("Unknown shape!")
            continue
        elif shape == "triangle":
            base = float(input("Give base of the triangle: "))
            height = float(input("Give height of the triangle: "))
            area = base * height / 2
            print(f"The area is {area:.6f}")
        elif shape == "rectangle":
            width = float(input("Give width of the rectangle: "))
            height = float(input("Give height of the rectangle: "))
            area = width * height
            print(f"The area is {area:.6f}")
        elif shape == "circle":
            radius = float(input("Give radius of the circle: "))
            area = math.pi * radius**2
            print(f"The area is {area:.6f}")


if __name__ == "__main__":
    main()
