while True:
    mail = input("mailinizi girin: ")
    if "@" in mail and "." in mail:
        print("mail dogru")
        break
    else:
        mail=input("mail yanlıs,lutfen tekrar girin: ")
        if "@" in mail and "." in mail:
            print("mail dogru")
        break
 