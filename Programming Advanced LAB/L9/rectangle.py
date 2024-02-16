def rectangle(length, width):
    def area():
        return length * width

    def perimeter():
        return (length + width) * 2

    if type(length) == int and type(width) == int:
        return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"
    else:
        return f"Enter valid values!"