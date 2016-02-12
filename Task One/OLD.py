aist = ["Screen/Display", "Physical Buttons", "Sound/Vibrations", "Movement/Sensors", "Software"]
aqlist = ["a cracked screen display", "being dropped/in contact with liquid", "running out of storage space", "deleting your internet history", "device being frozen", "apps crashing", "network/bluetooth issues", ]
aanslist = ["You can get a screen fixed from a mobile repair shop, but this may void its warranty.\n The best solution is to speak to the manufacturer of the device.", "A quick fix solution sometimes is to separate the phone’s battery and compartments and place them in a bag in rice for 24 hours (if you can seperate them easily), followed by removing the rice, placing them back in the phone and then turning the device back on.\nIf this does not work then you will need to invest in a new phone.\nThe manufacturer may give you a discount on a new phone, so you should speak to them.", "Ideally, you should attempt to delete photos, videos, music and apps on your phone.\nOtherwise, you can use an app like CCleaner to free up some space on your device.", "If you use Chrome, go to Menu > Settings > Clear Browsing Data/History.\nIf you are using Safari, go to the Settings app > Safari > Clear History and Website Data.\nIn future, it is recommended that you use the ‘Incognito’ or ‘Private Browsing’ feature on your device", "If you are on an iPhone, Soft Reset your device by holding down the Home Button and Power Button (ignore any messages such as ‘Slide to Power Off’) until your phone completely shuts down and you see the Apple Logo.\nIf you are running android, Try a Soft Reset by holding the Power + Volume Up button, however this can differ from phone to phone, so ask your Mobile Manufacturer for advice.", "If you are on an iPhone, Remove the app from the multitasking tray (if applicable), and then re-open the app.\nIf it still crashes, Soft Reset your device by holding down the Home Button and Power Button (ignore any messages such as ‘Slide to Power Off’) until your phone completely shuts down and you see the Apple Logo.\nIf you are on Android, attempt to wipe the apps Cache + Data in the Settings app, but this can differ from phone to phone.\nIf you need more help, contact the mobile manufacturer.", "On iPhone, you should reset your network settings by navigating to Settings > General > Reset > Reset Network Settings.\nIf you are on Android, speak to the mobile manufacturer.", "Please speak to the phone manafacturing company, who will be able to help you futher."]  

response = input("Is your issue related to " + aqlist[0] + "?\n")
if response == ("yes"):
    a = 0
else:
    response = input("Is your issue related to " + aqlist[1] + "?\n")
    if response == ("yes"):
        a = 1
    else:
        response = input("Is your issue related to " + aqlist[2] + "?\n")
        if response == ("yes"):
            a = 2
        else:
            response = input("Is your issue related to " + aqlist[3] + "?\n")
            if response == ("yes"):
                a = 3
            else:
                response = input("Is your issue related to " + aqlist[4] + "?\n")
                if response == ("yes"):
                    a = 4
                else:
                    response = input("Is your issue related to " + aqlist[5] + "?\n")
                    if response == ("yes"):
                        a = 5
                    else:
                        response = input("Is your issue related to " + aqlist[6] + "?\n")
                        if response == ("yes"):
                            a = 6
                        else:
                            print(aanslist[7])
                            quit()                          


answer = aanslist[(a)]
response = input("Is the phone protected by a Protect plan?\n")
if response == ("yes"):
    print("Please speak to your protect plan company, who will be able to help you futher.\nThank you for using the Carphone Warehouse Troubleshooting Guide")
    quit()
else:
    print(answer)
    print("\nThank you for using the Carphone Warehouse Troubleshooting Guide")
    quit()