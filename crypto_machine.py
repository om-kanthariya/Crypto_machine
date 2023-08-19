def machine():
    keys= "abcdefghijklmnopqrstuvwxyz )(*&@#$%!"
    values = keys[-1] + keys[0:-1]

    encry= dict(zip(keys,values))
    decry = dict(zip(values,keys))

    message = input("please enter your secret message : ")
    mode = input ("Please enter the mode : Encrypt(E) OR Decrypt (D) : ")

    if mode.upper() == "E":
        new_message = ''.join([encry[letter]
                                for letter in message.lower()])

    elif mode.upper() == "D":
        new_message = ''.join([decry[letter]
                                for letter in message.lower()])
    else:
        print("Please Enter the correect Choice")

    return new_message.capitalize()


user = input("Enter Your Name")
print(machine())



# def machine():
   
#     keys = 'abcdefghijklmnopqrstuvwxyz !'
    
#     values = keys[-1] + keys[0:-1]
   
#     encrytDict = dict(zip(keys, values))
#     decryptDict = dict(zip(values, keys))


#     message = input("Enter your secret message: ")
#     mode = input("Crypto Mode : Encode(E) OR Decode(D)")

#     if mode.upper() == 'E':
#         newMessage = ''.join([encrytDict[letter]
#                               for letter in message.lower()])
#     elif mode.upper() == 'D':
#         newMessage = ''.join([decryptDict[letter]
#                               for letter in message.lower()])
#     else:
#         print("Please try again, wrong choice entered")

#     return newMessage.capitalize()


# print(machine())
