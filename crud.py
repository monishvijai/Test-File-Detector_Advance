users = []

def create_user():
    name = input("enter the name of the user: ")
    age = int(input("enter the age of the user: "))
    user = {"name": name, "age": age}
    users.append(user)
    return user

def read_user():
    name = input("enter the name to search: ")
    for user in users:
        if user['name'] == name:
            return users
    return "user not found"

def update_user():
    old_name = input("enter the name of the user you want to update: ")
    for user in users:
        if user["name"] == old_name:
            new_name = input("enter the new name: ")
            new_age = int(input("enter the new age: "))
            user['name'] = new_name
            user['age'] = new_age
            print(users)
            return user
    return "user not found"

def delete_user():
    name = input("enter the name to delete: ")
    for user in users:
        if user['name'] == name:
            users.remove(user)
            return "user deleted"
    return "user not found"

while True:
    print("1 Add User")
    print("2 View User")
    print("3 Update User")
    print("4 Delete User")
    print("5 Exit")

    choice = input("Choose: ")

    if choice == "1":
        print(create_user())
    elif choice == "2":
        print(read_user())
    elif choice == "3":
        print(update_user())
    elif choice == "4":
        print(delete_user())
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Wrong choice\n")
