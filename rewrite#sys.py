import sys

while True:
    g = input("Enter: ")
    if g == "1":
        print("Correct")
        break
    else:
        sys.stdout.write("\033[F")  # Move cursor up one line
        sys.stdout.write("\033[K")  # Clear to the end of line
        print("Error")
    