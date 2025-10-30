from transliterate import translit

added_words = ["af", "f3r", "gga", "aew", "125"]
email_addresses = []

while True:
    full_name = input("введите ФИО через пробел: ")
    full_name_list = full_name.split()

    sudgests_names = []
    for i in range(len(added_words)):
        sudgest_name = full_name_list.copy()
        sudgest_name.append(added_words[i])
        sudgests_names.append(sudgest_name)
        sudgest_name_str = ".".join(sudgest_name) + "@gmail.com"
        print(i, translit(sudgest_name_str, "ru", reversed=True))

    user_choice = int(input("введите номер подходящей почты: "))

    email_addresses.append(sudgests_names[user_choice - 1])

    print("список всех почт: ")
    for email in email_addresses:
        print(translit(".".join(email) + "@gmail.com", "ru", reversed=True))