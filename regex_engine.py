
support="."

user_input = input().split("|")

if user_input[0] == "":
    print(True)
elif user_input[1] == "":
    print(False)
elif user_input[0] == "" and user_input[1] == "":
    print(True)
elif user_input[0] == user_input[1]:
    print(True)
elif user_input[0] == support and user_input != "":
    print(True)
else:
    print(False)