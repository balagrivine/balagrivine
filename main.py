command = " "
started = True
while command != "quit":
    msg = input(">>>")
    if msg == "start":
        if started:
           print("Car started what are you doing!")
        else:
            print("car started...")
    elif msg == "stop":
        if not started:
            print("Car stopped what are you doing")
        else:
            started = False
            print("car stopped...")
    elif msg == "help":
        print("""
        start -to start the car
        stop -to stop the car
        quit -to exit""")
    else:
        print("sorry. I don't understand that!")