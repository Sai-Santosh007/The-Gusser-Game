print("Hi there..! I'm Python.")
greet = input("How are you doing ? {good/bad}").lower().strip()
if greet == "good":
    que1 = input("that's great. shall we try a fun number game😊 ? {yes/no}")
    if que1 == "yes":
        print("How can I call you ?")
        que2 = input("tell me your name :")
        print(f"Okay {que2}, Now think of a number in your mind. Don't say it to me...😂😂")
        que3 = input("Done with your thinking {yes/no} 🤔:")
        if que3 == "yes":
            print("now multiply that number with 2")
            que4 = input("Multiplied 🤔 ? {yes/no} :")
            if que4 == "yes":
                que5 = input("Do know additions and substractions 🤔😅? {yes/no} :")
                if que5 =="yes":
                    print("Then ADD 10 to that result...😂")
                    print("After adding, divide your number with 2")
                    ans1 = input("Enter the final result you have got: ")
                    ans1 = int(ans1)
                    print("the final answer you thought about is 100 ")
                    print("JK-just kidding your number is", ans1-5)
                elif que5 == "no":
                    sd1 = input("what class you are currently studying in😒-")
                    print(f"what you are now in {sd1}🫡, but you don't even know additions and substractions ? Go and sit in L.K.G again..😑. I don't want to play with you..")
                else:
                    print("Check the spelling you entered, Cause you don't see this message if entered it correctly🥲")
            elif que4 == "no":
                print("why not multiplied yet, don't you know multiplication, Again If not, we can't play anymore ",que2)
            else:
                print("Check the spelling you entered, Cause you don't see this message if entered it correctly🥲")
        elif que3 == "no":
            sd2 = input("No..? you don't want to play or what..? :")
            if sd2 =="yes":
                print("then RERUN the program and type yes this time")
            elif sd2 == "no":
                print(f"okay {que2} no problem, just rerun the program if you want to play next time, have a NICE DAY.😊")
            else:
                print("Check the spelling you entered, Cause you don't see this message if entered it correctly🥲")
        else:
            print("Check the spelling you entered, Cause you don't see this message if entered it correctly🥲")
    elif que1 == "no":
        print("why not ? better we should play.. If you want to play, then RERUN the program. until signing off Mr.Python.")
    else:
        print("Check the spelling you entered, Cause you don't see this message if entered it correctly🥲")
elif greet == "bad":
    sd3 = input("sorry to hear that from you, shall we try a fun number game to make your mood better ? {yes/no}")
    if sd3 == "yes":
        print("How can I call you ?")
        que2 = input("tell me your name :")
        print(f"Okay {que2}, Now think of a number in your mind. Don't say it to me...😂😂")
        que3 = input("Done with your thinking {yes/no} 🤔:")
        if que3 == "yes":
            print("now multiply that number with 2")
            que4 = input("Multiplied 🤔 ? {yes/no} :")
            if que4 == "yes":
                que5 = input("Do know additions and substractions 🤔😅? {yes/no} :")
                if que5 == "yes":
                    print("Then ADD 10 to that result...😂")
                    print("After adding, divide your number with 2")
                    ans1 = input("Enter the final result you have got: ")
                    ans1 = int(ans1)
                    print("the final answer you thought about is 100 ")
                    print("JK-just kidding your number is", ans1 - 5)
                elif que5 == "no":
                    sd1 = input("what class you are currently studying in😒-")
                    print(
                        f"what you are now in {sd1}🫡, but you don't even know additions and substractions ? Go and sit in L.K.G again..😑. I don't want to play with you..")
                else:
                    print("Check the spelling you entered, Cause you don't see this message if entered it correctly🥲")
            elif que4 == "no":
                print("why not multiplied yet, don't you know multiplication, Again If not, we can't play anymore ",
                      que2)
            else:
                print("Check the spelling you entered, Cause you don't see this message if entered it correctly🥲")
        elif que3 == "no":
            sd2 = input("No..? you don't want to play or what..? :")
            if sd2 == "yes":
                print("then RERUN the program and type yes this time")
            elif sd2 == "no":
                print(
                    f"okay {que2} no problem, just rerun the program if you want to play next time, have a NICE DAY.😊")
            else:
                print("Check the spelling you entered, Cause you don't see this message if entered it correctly🥲")
        else:
            print("Check the spelling you entered, Cause you don't see this message if entered it correctly🥲")
    elif sd3 == "no":
        print("why not ? better we should play.. If you want to play, then RERUN the program. until signing off Mr.Python.")
    else:
        print("Check the spelling you entered, Cause you don't see this message if entered it correctly🥲")
else:
    print("Check the spelling you entered, Cause you don't see this message if entered it correctly🥲")