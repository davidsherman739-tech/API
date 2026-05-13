def is_adult(age):
    return age >= 18


def is_name_valid(username):
    return len(username) >= 4


def create_user(username, age, email):

    if not is_adult(age):
        return {
            "success": False,
            "error": "Uzivatel neni dospely"
        }

    if not is_name_valid(username):
        return {
            "success": False,
            "error": "Uzivatelske jmeno je prilis kratke"
        }

    user = {
        "username": username,
        "age": age,
        "email": email
    }

    return {
        "success": True,
        "user": user
    }


def print_user_info(result):

    if result["success"]:
        user = result["user"]

        print("Uzivatel:")
        print("Username:", user["username"])
        print("Age:", user["age"])
        print("Email:", user["email"])
        print("-------------------")

    else:
        print("Chyba:", result["error"])
        print("-------------------")


# vytvoreni uzivatelu
users = [
    create_user("David", 20, "david@gmail.com"),
    create_user("Tom", 25, "tom@gmail.com"),
    create_user("Al", 17, "al@gmail.com"),
    create_user("Martin", 30, "martin@gmail.com")
]

# vypsani uzivatelu
for user in users:
    print_user_info(user)
