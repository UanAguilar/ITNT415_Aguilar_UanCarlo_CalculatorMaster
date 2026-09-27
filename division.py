def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

if __name__ == "__main__":
    print("Division result:", divide(10, 2))
    print("Zero check:", divide(10, 0))
