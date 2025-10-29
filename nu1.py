ticket_number = input("enter your ticket number: ")
if len(ticket_number) == 6:
    #pass
    sum_first = int(ticket_number[0]) + int(ticket_number[1]) + int(ticket_number[2])
    sum_second = int(ticket_number[3]) + int(ticket_number[4]) + int(ticket_number[5])
    print(sum_first, sum_second)

    if sum_first == sum_second and sum_first + sum_second <= 15:
        print("Число счастливое")
    else:
        print("Число не счастливое")
else:
    print("invalid ticket number")