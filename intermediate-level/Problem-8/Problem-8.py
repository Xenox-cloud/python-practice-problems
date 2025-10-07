def calculator():
    parts = input("Enter command: ").split()
    cmd, x, y = parts[0], int(parts[1]), int(parts[2])
    if cmd == "add":
        return x + y
    elif cmd == "sub":
        return x - y
    elif cmd == "mul":
        return x * y
    elif cmd == "div":
        return x / y if y != 0 else "Error: Division by zero"


print(calculator())