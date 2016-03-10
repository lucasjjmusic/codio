import sys, os, errno
__author__ = '12johnstonl'
filename = "%USERPROFILE%\Documents\TechnicalCase" + caseno + ".txt"
print('\033[0m' + "Hello and Welcome to the Carphone Warehouse Troubleshooting Guide!\nBefore we get started, I just want to ask you a few quick questions")
print('\033[91m' + "IF YOU WOULD LIKE TO EXIT THE PROGRAM, ENTER 'Ctrl-C' AT ANY POINT." + '\033[0m')
probs = ["a broken phone screen", "that your phone screen is not turning on", "that there is random colours on the phone's screen", "that bluetooth isn't working"]
ips = ["Please take your iPhone into an authorised Apple Retailer or Apple Store to be repaired. Alternatively, your phone can be repaired at our sister company by googling GeekSquad.\nThey will also be able to help you with any further problems in store there.", "Make sure your device is charged up.\nIf it is still not working, try to do a hard reset by holding down the Sleep/Wake button + Home button until you see the apple logo, then release.\nIf it is still not working, please consult your local Apple Store for more help", "If random colours are displaying on your iPhone screen, the LCD is most likely broken.\nIn this event, take your iPhone into an authorised Apple Retailer or Apple Store to be repaired. Alternatively, your phone can be repaired at our sister company by googling GeekSquad.\nThey will also be able to help you with any further problems in store there.", "If you are having Bluetooth connectivity issues, then the best approach is to contact Apple Support or visiting an official Apple Store.\nThey will be able top help you more there."]
aps = ["Firstly, try to get in contact with your manafacturer to see if they will repair your phone. If not, feel free to contact our sister company - you can find them by googling GeekSquad.", "Make sure your device is charged up. If the screen is still black/unresponsive, try a hard reset.\nKey combinations vary from device to device, but on most android phones it is the 'Volume Down' + 'Power' buttons. Hold them down for 10/20 seconds.\nIf your device is still unresponsive, seek help from your device's manafacturer.", "If your android phone is displaying random colours, your LCD is most likely broken.\nTry to get in contact with your manafacturer to see if they will repair your phone. If not, feel free to contact our sister company - you can find them by googling GeekSquad.", "If your android phone is having Bluetooth connectivity issues, the best place to ask for help wuill be with the manafacturer directly.\nIf you have a Nexus device, please request a call from Google Support from the Nexus help centre, here: https://support.google.com/nexus/?hl=en-GB#topic=3424348\nAlternativley, you may like to ask for help from an online community such as XDAdevelopers."]
ms = ["Microsoft do not offer a screen replacement service, so we reccommend visiting our sister company to repair your device - you can find them by googling GeekSquad.", "Make sure your device is charged up. If your screen is still black/unresponsive, restart your phone by holding all 4 buttons for 15-20 seconds.\nIf this still fails, please contact Microsoft Support to help you further.", "If your windows phone is displaying random colours, your LCD is most likely broken.\nTry to get in contact with Microsoft Support to see if they will repair your phone. If not, feel free to contact our sister company - you can find them by googling GeekSquad.", "Microsoft reccomends that you contact them directly in this issue, by visiting: support.microsoft.com/en-gb"]
qs = ["cracked", "broken", "not turning on", "colours", "colors", "lines"]
    
# FIND DEVICE BEING USED BY CONSUMER [stored in device, model, mana and value in apple]
device = input('\033[0m' + "What device are you using (e.g. 'tablet' or 'phone')?\n" + '\033[94m').lower()
if 'phone' in device or 'fone' in device:
    os = input('\033[0m' + "Are you using an iPhone, an Android phone, or a windows phone?\n" + '\033[94m').lower()
    if 'apple' in os or 'ios' in os or 'iphone' in os or 'ifone' in os:
        apple = 1
        mana = "apple"
        model = input('\033[0m' + "What model iPhone are you using?\n" + '\033[94m').lower()
        if 's' in model or 'c' in model or 'g' in model:
            print('\033[0m' + "Thank you.")
        else:
            variant = input('\033[0m' + "What variant of the iPhone are you using (e.g. *enter button* for whole number, or 'S', or 'C')\n" + '\033[94m').lower()
            model = (model + variant)
            print('\033[0m' + "Thank you.")
    elif 'android' in os or 'google' in os or 'nexus' in os:
        apple = 2
        mana = input('\033[0m' + "Who is your OEM (manafacturer, e.g. 'huawei')?\n" + '\033[94m').lower()
        model = input('\033[0m' + "What model of " + mana + " phone are you using?\nFor example, 'nexus 6p'\n" + '\033[94m').lower()
        print('\033[0m' + "Thank you.")
    elif 'microsoft' in os or 'windows' in os or 'lumia' in os or 'nokia' in os:
        apple = 3
        mana = "microsoft"
        model = input('\033[0m' + "What model of " + mana + " phone are you using?\nFor example, 'lumia xc90'\n" + '\033[94m').lower()
        print('\033[0m' + "Thank you.")
    else:
        print('\033[91m' + "Unfortunately we only support smartphones from Carphone Warehouse with this program.\nAs we only sell Windows, Android and iOS Devices are you sure the phone's name was spelled correctly?\nPlease try again later. Thank you." + '\033[0m')
        sys.exit()
elif 'tablet' in device:
    print('\033[91m' + "As this is only a beta program, we unfortunately do not currently support tablets.\nPlease check back at a later date.\n\nThank you." + '\033[0m')
    sys.exit()
else:
    print('\033[91m' + "Unfortunately we only support phones and tablets from Carphone Warehouse with this program." + '\033[0m')
    sys.exit()
    
def main():
    while True: 
        while True:        
            response = input('\033[0m' + "We're going to need a get an idea of the problem with your " + mana + " " + model + "." + "\nCould you help us by please entering a" + '\033[91m' + " short" + '\033[0m' + ", 1 sentance summary of your problem.\nPlease do not enter more than one problem\n" + '\033[94m').lower()
            
            if qs[0] in response or qs[1] in response:
                ans = 0
                break
            elif qs[2] in response:
                ans = 1
                break
            elif qs[3] in response or qs[4] in response or qs[5] in response:
                ans = 2
                break
            elif 'bluetooth' in response:
                ans = 3
                break
            else:
                print('\033[0m' + "Sorry, we didn't catch what you were saying. Maybe try simplifying it or changing your wording to include more keywords.\nIn addition, we currently only support screen and bluetooth issues on this automated program.\n")
                bans = input('\033[0m' + "If you have another issue unrelated to screen or bluetooth, please enter " + '\033[91m' + "'Y'" + '\033[0m' + " now. We are sorry for any inconvenience caused.\n\n" + '\033[94m').lower()
                if bans == 'Y':
                    extrainfo = input('\033[0m' + "Is there anything else you would like to let our technicians aware of?" + '\033[94m').lower()
                    name = input('\033[0m' + "Can we take your Forename and Sirname (e.g. Nicholas Jones)" + '\033[94m').lower()
                    email = input('\033[0m' + "And can we take your full email address? (e.g. nicholasj67@ntlworld.com)" + '\033[94m').lower()
                    print("Thank you.")
                    

        confirm = input('\033[0m' + "To confirm, your problem is " + probs[ans] + "\nPlease enter yes or no.\n" + '\033[94m').lower()
        if 'y' in confirm and apple == (1):
            print('\033[0m' + "Thank you.\n" + ips[ans])
            print("\nThank you for using the Carphone Warehouse Troubleshooting Guide.")
            sys.exit()
        elif 'y' in confirm and apple == (2):
            print('\033[0m' + "Thank you.\n" + aps[ans])
            print("\nThank you for using the Carphone Warehouse Troubleshooting Guide.")
            sys.exit()
        elif 'y' in confirm and apple == (3):
            print('\033[0m' + "Thank you.\n" + ms[ans])
            print("\nThank you for using the Carphone Warehouse Troubleshooting Guide.")
            sys.exit()
        elif 'n' in confirm:
            print('\033[0m' + "Sorry, lets try that again.\n\n")
        elif 'EXIT' in confirm:
            sys.exit()
            
main()
