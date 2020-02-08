""" if you are doing programming, then the basic problem of a programmer that he forget to drink water and take some rest. bcs its needed for a healthy programmer. if you forget anythiing else then write your activity one time, it recall you every day, every hour as well as your time. """


import time
# you can set the time according your time table.
#t = time.asctime()[11:16]


def speak(str):
    # this is speak function, it take string in speak()
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


def wait():  # it's waiting for your pressing enter.
    speak("okay, no problem !")
    wait = input()


def __my_rutein__():
    # set the timer according your activity and do your work time to time
    speak("Hey, i'm here for you, don't worry")
    permission = input()  # it take permission to enter the loop
    if permission == "yeah":
        pass
    else:  # if you type any other input like "wait" then the program hass been stop, go to wait()
        wait()
    while True:
        print("...")  # its sign for loop start again
        for _ in range(6):
            # here the timer is set every 10 min. it call you for drink water
            time.sleep(600)
            speak("plz take some water ")
            water = input()
            if water == "wait":  # if you busy tell them "wait"
                wait()  # again press enter to start
            elif water == "done":
                speak(" Well Done ")
            elif water == "final":  # you want to stop the program, just type "final"
                speak(" Thank you !")
                exit()
        # after 1 hr program tell you that you need some rest for your eyes ...
        speak("sir, i think you need a break, plz relex your Eyes, & do some Exercise.")
        eyes_exercise = input()  # after the break you start this program again just type "done"
        if eyes_exercise == "done":
            speak("Congratulation")
        elif eyes_exercise == "final":  # you want to stop the program, just type "final"
            speak(" Thank you !")
            exit()


__my_rutein__()
