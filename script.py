import platform, time, tkinter, random, json, os, webbrowser

lcp_version = "v0.2-beta"

"""
LCP will automatically raise a ForceQuitted error when needed.
"""
class ForceQuitted(Exception) : ...

def animated_print(message: str, delay: int = 0.003, end: bool = True) -> None:
    for char in message:
        print(char, end = "", flush = True)
        time.sleep(delay)
    if end:
        print("")

def animated_input(message: str, delay: int = 0.003) -> object:
    animated_print(message, delay, False)
    return input("")

animated_print("Starting inspection...")

if not (int(platform.python_version_tuple()[2]) >= 10 or int(platform.python_version_tuple()[1]) >= 2):
    animated_print(f"You are running this program in an outdated version of the Python interpreter. Your current Python version is {platform.python_version()}, and at least version 3.10~ is recommended for this program.")
    time.sleep(10)
    raise ForceQuitted("Program exited due to an outdated Python interpreter.")

animated_print(f"Python interpreter version requirement passed! (Required: 3.10~, Current: {platform.python_version()})")

windows_version = int(platform.uname().release)

if windows_version < 11:
    animated_print(f"""Although you can proceed just fine, you're running this program on Windows {windows_version}.
This program uses the colorama module to implement vibrant colors, but terminals in Windows 10 or less won't support those coloring. 
It's highly recommended to run this program in a VSCode terminal if you want to proceed.""")

animated_print(f"Recommended Windows version passed! (Recommended: Windows 11~, Current: {windows_version})")

try:
    from colorama import Fore, Style
except ImportError:
    animated_print("""Seems like you didn't properly install the required packages for this project.
Unfortunately, we can't automatically install the packages for you / use pyInstaller because it comes with a huge risk and might not be compatiable with a lot of OS's.
Please see if you are missing anything and follow everything in https://github.com/Lanzoor/LCP/blob/main/README.md !""")
    time.sleep(10)
    raise ForceQuitted("Program exited due to missing dependencies.")

animated_print("External libraries passed!")
savefile_path = os.path.dirname(__file__) + "/savedata.json"

try:
    with open(savefile_path, "r") as saveddata:
        savedata = json.load(saveddata)
    del saveddata
except FileNotFoundError:
    animated_print("Savedata was not found. Creating a brand-new empty savedata for you...")
    try:
        with open(savefile_path, "w") as file:
            file.write("{\"username\": \"ERR_NOT_SPECIFIED\", \"points\": 0, \"multiplier\": 1, \"commandCount\": 0, \"shopUpgrades\": {\"multiplier++\": 0, \"multiplier**\": 0, \"end\": false, \"shopUpgradesPurchased\": 0}, \"settings\": {\"animationType\": \"char\", \"autoSaveEveryCommand\": true}, \"savedataVersion\": \"%s\"}" % lcp_version)
        with open(savefile_path, "r") as saveddata:
            savedata = json.load(saveddata)
        del saveddata
    except PermissionError:
        animated_print("Permission was denied. Perhaps you should download a brand-new savedata from https://github.com/Lanzoor/LCP/blob/main/savedata.json.")
        time.sleep(10)
        raise ForceQuitted("Program exited due to savefile not existing.")

animated_print("Your savefile was found! Reading data...")

savedata_version = savedata['savedataVersion']

if savedata_version != lcp_version:
    animated_print("Your savedata does not match your current version, please download one corresponding to your script version using https://github.com/Lanzoor/LCP/blob/main/savedata.json !")
    time.sleep(10)
    raise ForceQuitted("Program exited due to an outdated savedata.json file.")

username = savedata['username']
points = savedata['points']
multiplier = savedata['multiplier']
command_count = savedata['commandCount']
shop_upgrades = savedata['shopUpgrades']
settings = savedata['settings']

global animation_type
animation_type = settings['animationType']

def animated_print(message: str, end: bool = True) -> None:
    match(animation_type):
        case "char":
            for char in message:
                print(char, end = "", flush = True)
                time.sleep(0.003)
            if end:
                print("")
        case "line":
            for lines in message.splitlines():
                for char in list(lines):
                    if char != "\n":
                        print(char, end = "", flush = True)
                    else:
                        print(char, flush = True)
                time.sleep(0.05)
                if end: 
                    print("")
        case "none":
            print(message)
            if end:
                print("")

def animated_input(depth: int = 0) -> object:
    animated_print(f"{" " * depth}> ", False)
    return input("")

def view_ending() -> None:
    ...

def save_all_data():
    global savedata, username, points, multiplier, command_count, shop_upgrades, settings, animation_type
    savedata['username'] = username
    savedata['points'] = points
    savedata['multiplier'] = multiplier
    savedata['commandCount'] = command_count
    savedata['shopUpgrades'] = shop_upgrades
    savedata['settings'] = settings
    savedata['settings']['animationType'] = animation_type
    
    with open(savefile_path, "w") as saveddata:
        json.dump(savedata, saveddata)
    del saveddata

if username == "ERR_NOT_SPECIFIED":
    animated_print("Your username was not found, what can this program call you?\nEnter your new username!")
    while True:
        new_username = animated_input().strip()
        if new_username.lower() == "err_not_specified":
            animated_print(f"Failed to initialize new username because the username you're trying resembles a default placeholder name. Please try a different one.")
        elif len(new_username) < 3:
            animated_print("Usernames can't be shorter than 3 characters. Please make it longer!")
        elif len(new_username) >= 20:
            animated_print("Usernames can't be longer than 19 characters. Please make it shorter!")
        else:
            animated_print(f"Your brand new username is set to {Fore.BLUE + new_username + Fore.RESET}. If you want it changed, you can always change your username via ?settings.")
            username = new_username
            savedata['username'] = new_username
            break
    save_all_data()

if len(username) < 3 or len(username) >= 20:
    animated_print("Your username is either long or short. I know you edited the savedata, right? Anyways, please try a different one.\nEnter your new username!")
    while True:
        new_username = animated_input().strip()
        if new_username.lower() == "err_not_specified":
            animated_print(f"Failed to initialize new username because the username you're trying resembles a default placeholder name. Please try a different one.")
        elif len(new_username) < 3:
            animated_print("Usernames can't be shorter than 3 characters. Please make it longer!")
        elif len(new_username) >= 20:
            animated_print("Usernames can't be longer than 19 characters. Please make it shorter!")
        else:
            animated_print(f"Your brand new username is set to {Fore.BLUE + new_username + Fore.RESET}. If you want it changed, you can always change your username via ?settings.")
            username = new_username
            savedata['username'] = new_username
            break
    save_all_data()

if shop_upgrades['multiplier++'] > 100:
    shop_upgrades['multiplier++'] = 100

if shop_upgrades['multiplier**'] > 50:
    shop_upgrades['multiplier**'] = 50

absolute_multiplier = (shop_upgrades['multiplier++'] + shop_upgrades['multiplier**'] * 3) + 1

if absolute_multiplier != multiplier:
    multiplier = absolute_multiplier

animated_print("Almost done! Applying settings...")

welcome_message = f"Welcome to Lanzoor Command Panel ({Fore.GREEN + lcp_version + Fore.RESET}), {Fore.BLUE + username + Fore.RESET}! Type ?help to get help about the commands you can use, or type ?exit to exit the program. Have fun!"

help_message = f"""Here are all commands you can use in Lanzoor Command Panel as of now ({Fore.GREEN + lcp_version + Fore.RESET}).

?help: Displays this help message.
?stats / ?stat: Displays your stats.
?settings / ?setting / ?options / ?option: Displays the settings page.
?rand / ?random / ?roll: Rolls a random number.
?date: Displays your date.
?time: Displays your time.
?datetime / ?timedate: Displays your date and time.
?rps / ?rockpaperscissors: Play the rock paper scissors game.
?golt / ?greaterorlowerthan: Play the greater or lower than game.
?readme: Opens the README.md file for instructions.
?shop: Opens the shop.
?exit: Exit Lanzoor Command Panel.

And, here are some few things that you should probably consider using Lanzoor Command Panel.

This program is NOT case sensitive. This means that for using commands, it will still properly work if you input something like ?HeLP instead of ?help.
This program is entirely built in Python (with the help of a json file but that's only a json file not an actual program).
If you want to enjoy the true game, I definitely recommend playing the game without taking a peek at the game files / modifying the savefile.
If you want to ask / suggest / compliment about anything in Lanzoor Command Panel, feel free to ask me in Discord! (lanzoor)"""

animated_print(welcome_message)

while True:
    user_input = animated_input().strip().lower()
    match user_input:
        case "?help":
            animated_print(help_message)
        case "?stats" | "?stat":
            animated_print(f"""Here are your stats on Lanzoor Command Panel;
Your username is {Fore.BLUE + username + Fore.RESET}.
You have used {Style.BRIGHT + str(command_count) + Style.RESET_ALL} commands (excluding this command).
You have {Style.BRIGHT + str(points) + Style.RESET_ALL} points, and your point multiplier is {Style.BRIGHT + str(multiplier) + Style.RESET_ALL}.
You have purchased {Style.BRIGHT + str(shop_upgrades['shopUpgradesPurchased']) + Style.RESET_ALL} shop upgrades.""")
        case "?settings" | "?setting" | "?option" | "?options":
            settings_message = f"""Welcome to the settings page, you can tweak some settings here!
You will have to input the setting number. Choose a setting to change, and input exit or ?exit to exit settings.

1. Animation type: {Fore.BLUE if settings['animationType'] in ["char", "line"] else Fore.GREEN}{settings['animationType'].capitalize()}{Fore.RESET}
{Style.DIM}Turn this option off if you want this program to run faster, because the animation gives a small delay.{Style.RESET_ALL}
2. Autosave Every Command: {Fore.GREEN if settings['autoSaveEveryCommand'] else Fore.RED}{settings['autoSaveEveryCommand']}{Fore.RESET}
{Style.DIM}Turn this option off if it takes too long to process a command or you're on a low-performace device.
In that case though, you should not try to force-quit the program (using ^C / Ctrl + C / ⌘ + C) to prevent any data loss.
Savedata will be autosaved when you exit this program, though.{Style.RESET_ALL}
3. Change Username
{Fore.RED}4. RESET DATA{Fore.RESET}"""
            animated_print(settings_message)
            while True:
                settings_input = animated_input(1).strip().lower()
                match settings_input:
                    case "1":
                        animation_type_message = f"""Please choose what option to set the option \"Animation Type\" to using the function number, using the option name (char, line, none), or type ?exit or exit to cancel setting change.
1. Char (Delay between each character) (RECOMMENDED FOR MOST CASES)
2. Line (Delay between each line (newline character, \\n)) (BALANCE BETWEEN SPEED AND QUALITY)
3. None (No delay whatsoever) (RECOMMENDED IF LAGGY)"""
                        animated_print(animation_type_message)
                        changed = True
                        while True:
                            animation_type_input = animated_input(2).strip().lower()
                            match animation_type_input:
                                case "1" | "char":
                                    settings['animationType'] = "char"
                                    animation_type = "char"
                                    break
                                case "2" | "line":
                                    settings['animationType'] = "line"
                                    animation_type = "line"
                                    break
                                case "3" | "none":
                                    settings['animationType'] = "none"
                                    animation_type = "none"
                                case "exit" | "?exit":
                                    changed = False
                                case _:
                                    continue
                        if changed:
                            save_all_data()
                            animated_print(f"Set the setting \"Animation Type\" to {Fore.BLUE}{settings['animationType']}{Fore.RESET}")
                        else:
                            animated_print("No changes made.")
                    case "2":
                        settings['autoSaveEveryCommand'] = not (settings['autoSaveEveryCommand'])
                        animated_print(f"Set the setting \"Autosave Every Command\" to {Fore.GREEN if settings['autoSaveEveryCommand'] else Fore.RED}{settings['autoSaveEveryCommand']}{Fore.RESET}")
                    case "3":
                        animated_print("Enter your new username!\n")
                        while True:
                            new_username = animated_input(2).strip()
                            if new_username.lower() == "err_not_specified":
                                animated_print(f"Failed to initialize new username because the username you're trying resembles a default placeholder name. Please try a different one.")
                            elif len(new_username) < 3:
                                animated_print("Usernames can't be shorter than 3 characters. Please make it longer!")
                            elif len(new_username) >= 20:
                                animated_print("Usernames can't be longer than 19 characters. Please make it shorter!")
                            else:
                                animated_print(f"Your username is set to {Fore.BLUE + new_username + Fore.RESET}.")
                                username = new_username
                                savedata['username'] = new_username
                                break
                        save_all_data()
                    case "4":
                        confirmation_message = f"""{Fore.RED}Hold up! Before you reset your entire savedata...
You can still continue on this savedata if you create backups of the savedata.json file before this action.
Once you perform this action, your savedata will be resetted without furthermore confirmations, and this program will automatically be closed.
Are you sure that you want to delete your savedata? Input y to continue.{Fore.RESET}"""
                        animated_print(confirmation_message)
                        confirmation_input = animated_input(2).strip().lower()
                        if confirmation_input == "y":
                            
                            savedata['username'] = "ERR_NOT_SPECIFIED"
                            savedata['points'] = 0
                            savedata['multiplier'] = 1
                            savedata['commandCount'] = 0
                            savedata['shopUpgrades'] = {"multiplier++": 0, "multiplier**": 0, "end": False, "shopUpgradesPurchased": 0}
                            savedata['settings'] = {"animationType": "char", "autoSaveEveryCommand": True}
                            savedata['savedataVersion'] = lcp_version
                            
                            with open(savefile_path, "w") as saveddata:
                                json.dump(savedata, saveddata)
                            del saveddata
                            
                            animated_print("Savedata deletion successful. This program will automatically close after a few seconds.")
                            time.sleep(3)
                            raise ForceQuitted("Program exited; savedata deletion performed.")
                        else:
                            animated_print("Savedata deletion failed; rejected by user.")
                    case "?exit" | "exit":
                        animated_print("Exited settings.")
                        break
                    case _:
                        continue
                save_all_data()
                command_count += 1
        case "?rand" | "?random" | "?roll":
            error = False
            while True:
                while True:
                    animated_print("Enter the minimum number.")
                    minimum_number = animated_input(1)
                    try:
                        minimum_number = int(minimum_number)
                        break
                    except ValueError:
                        animated_print("Please enter a valid integer.")
                        continue
                while True:
                    animated_print("Enter the maximum number.")
                    maximum_number = animated_input(1)
                    try:
                        maximum_number = int(maximum_number)
                    except ValueError:
                        animated_print("Please enter a valid integer.")
                        continue
                    if minimum_number > maximum_number:
                        animated_print(Style.DIM + "You silly! The minimum number can't be larger can the maximum number." + Style.RESET_ALL)
                        error = True
                        break
                    if minimum_number == maximum_number:
                        animated_print(Style.DIM + "You silly! Both numbers can't be the same, otherwise it would always return the number and breaks the entire concept of random!" + Style.RESET_ALL)
                        error = True
                        break
                if error:
                    error = False
                    continue
                else:
                    break
            animated_print(f"You picked {Style.BRIGHT}{minimum_number}{Style.RESET_ALL} as your minimum number, and {Style.BRIGHT}{maximum_number}{Style.RESET_ALL} as your maxmimum number. Your result is {Style.BRIGHT}{random.randint(minimum_number, maximum_number)}{Style.RESET_ALL}.")
        
        case "?date":
            animated_print(f"Your current date is {Style.BRIGHT + time.strftime(r"%B %d (%A), %Y") + Style.RESET_ALL}.")
        case "?time":
            animated_print(f"Your current time is {Style.BRIGHT + time.strftime(r"%X") + Style.RESET_ALL}.")
        case "?datetime" | "?timedate":
            animated_print(f"Your current date & time is {Style.BRIGHT + time.strftime(r"%B %d (%A), %Y | %X") + Style.RESET_ALL}.")
        case "?rps" | "?rockpaperscissors":
            animated_print("Choose one! Rock, Paper, or Scissors! You can also only input the first character of your choice.")
            while True:
                user_choice = animated_input(1).strip().lower()
                match user_choice:
                    case "r":
                        user_choice = "rock"
                    case "p":
                        user_choice = "paper"
                    case "s":
                        user_choice = "scissors"
                valid_rps_choice = ["rock", "paper", "scissors"]
                computer_choice = random.choice(valid_rps_choice)
                if user_choice not in valid_rps_choice:
                    animated_print("You silly, that is not a valid choice! Try again.")
                    continue
                break
            if computer_choice == user_choice:
                win_state = "It's a draw!"
                pending_points = 2
            else:
                winning_conditions = (
                    ("rock", "scissors"),
                    ("scissors", "paper"),
                    ("paper", "rock"),
                )
                if (user_choice, computer_choice) in winning_conditions:
                    win_state = "You won!"
                    pending_points = 3
                else:
                    win_state = "I won!"
                    pending_points = 1
            points += pending_points * multiplier
            animated_print(f"You picked {Style.BRIGHT + user_choice + Style.RESET_ALL}, I pick {Style.BRIGHT + computer_choice + Style.RESET_ALL}! {Style.BRIGHT + win_state + Style.RESET_ALL}\nYou gained {pending_points * multiplier} points in this game.")
        case "?golt" | "?greaterorlowerthan":
            choice = random.randint(1, 100)
            attempts = 0
            animated_print("Enter your guess! Type rules or !rules to view the rules, or exit or ?exit to exit.")
            while True:
                user_choice = animated_input(1).strip()
                if user_choice.lower() == "rules" or user_choice.lower() == "!rules":
                    animated_print("""Golt, aka greater or lower than game is a game where you guess a number.
I will randomly pick a number between 1 and 100 (inclusive), and your goal is to guess the number.
Everytime you fail, I will tell you if your number is greater or lower than my choice. (That's why its called golt)
Have fun!""")
                    continue
                elif user_choice.lower() == "exit" or user_choice.lower() == "?exit":
                    animated_print("Exited golt.")
                    recieve_points = False
                    pending_points = 1
                    break
                try:
                    user_choice = int(user_choice)
                except ValueError:
                    animated_print("Please enter a valid integer.")
                    continue
                if choice < user_choice and user_choice <= 100:
                    animated_print("My number is lower than your choice, try again!")
                elif user_choice > 100:
                    animated_print("Hey, that was out of the range!")
                    continue
                elif choice > user_choice:
                    animated_print("My number is greater than your choice, try again!")
                elif choice == user_choice:
                    attempts += 1
                    animated_print(f"You've guessed it right! You used {attempts} attempts in this game, and the answer was {Style.BRIGHT}{choice}{Style.RESET_ALL}.")
                    recieve_points = True
                    break
                attempts += 1
            if recieve_points:
                pending_points = (15 - attempts) * multiplier
                points += pending_points
            if pending_points <= 0:
                animated_print(f"You used too many attempts in this game! You didn't gain any points.")
            elif recieve_points:
                animated_print(f"You gained {pending_points} points in this game.")
        case "?shop":
            mpp_cost = (shop_upgrades['multiplier++'] + 1) * 14 + (shop_upgrades['multiplier++'] + 2) * 4 if shop_upgrades['multiplier++'] > 1 else 20
            mmm_cost = (shop_upgrades['multiplier**'] + 2) * 255 + (shop_upgrades['multiplier**'] + 3) * 6
            shop_message = f"""Welcome to the shop! You can buy upgrades with your points here. Input the item number to purchase, and type ?exit or exit to exit the shop!!
{Fore.YELLOW if shop_upgrades['multiplier++'] >= 100 else ""}1. Multiplier++ (Cost: {str(mpp_cost) if shop_upgrades['multiplier++'] < 100 else "MAX"}){Fore.RESET}
{Style.DIM}Adds 1 to your multiplier.{Style.RESET_ALL}
{Fore.YELLOW if shop_upgrades['multiplier**'] >= 50 else ""}2. Multiplier** (Cost: {str(mmm_cost) if shop_upgrades['multiplier**'] < 50 else "MAX"}){Fore.RESET}
{Style.DIM}Adds 3 to your multiplier.{Style.RESET_ALL}
{Fore.YELLOW if shop_upgrades['end'] else ""}3. {"???" if not shop_upgrades['end'] else "End"} (Cost: {"400 commands used (won't be spent), 200000 points (will be spent), 251 multiplier (max multiplier, won't be spent)" if not shop_upgrades['end'] else "MAX"}){Fore.RESET}
{Style.DIM}{"??????? ??? ??????." if not shop_upgrades['end'] else "Unlocks the ending."}{Style.RESET_ALL}"""
            animated_print(shop_message)
            while True:
                mpp_cost = (shop_upgrades['multiplier++'] + 1) * 14 + (shop_upgrades['multiplier++'] + 2) * 4 if shop_upgrades['multiplier++'] > 1 else 20
                mmm_cost = (shop_upgrades['multiplier**'] + 2) * 255 + (shop_upgrades['multiplier**'] + 3) * 6
                settings_input = animated_input(1).strip().lower()
                match settings_input:
                    case "1":
                        if shop_upgrades['multiplier++'] >= 100:
                            animated_print("You already maximized this upgrade!")
                            continue
                        if points >= mpp_cost:
                            animated_print("You have enough points to purchase this upgrade. Are you sure that you want to purchase this upgrade? Enter y to continue.")
                            last_confirmation = animated_input(2).strip().lower()
                            if last_confirmation == "y":
                                points -= mpp_cost
                                multiplier += 1
                                shop_upgrades['multiplier++'] += 1
                                shop_upgrades['shopUpgradesPurchased'] += 1
                                animated_print(f"Purchase successful! You spent {Style.BRIGHT}{mpp_cost}{Style.RESET_ALL} points. You now have {Style.BRIGHT}{points}{Style.RESET_ALL} points and {Style.BRIGHT}{multiplier}{Style.RESET_ALL} multiplier.")
                            else:
                                animated_print("Purchase canceled.")
                        else:
                            animated_print(f"You do not have enough points to purchase this upgrade, please try later! (Required: {mpp_cost} points, Current: {points} points)")
                            continue
                    case "2":
                        if shop_upgrades['multiplier**'] >= 50:
                            animated_print("You already maximized this upgrade!")
                            continue
                        if points >= mpp_cost:
                            animated_print("You have enough points to purchase this upgrade. Are you sure that you want to purchase this upgrade? Enter y to continue.")
                            last_confirmation = animated_input(2).strip().lower()
                            if last_confirmation == "y":
                                points -= mmm_cost
                                multiplier += 3
                                shop_upgrades['multiplier**'] += 1
                                shop_upgrades['shopUpgradesPurchased'] += 1
                                animated_print(f"Purchase successful! You spent {Style.BRIGHT}{mmm_cost}{Style.RESET_ALL} points. You now have {Style.BRIGHT}{points}{Style.RESET_ALL} points and {Style.BRIGHT}{multiplier}{Style.RESET_ALL} multiplier.")
                            else:
                                animated_print("Purchase canceled.")
                        else:
                            animated_print(f"You do not have enough points to purchase this upgrade, please try later! (Required: {mmm_cost} points, Current: {points} points)")
                            continue
                    case "3":
                        if shop_upgrades['end']:
                            animated_print("You already bought this upgrade! If you want to view the ending again, use your newly unlocked command ?ending!")
                            continue
                        if points >= 200000 and multiplier == 251 and command_count >= 400:
                            animated_print(f"You have enough resources to purchase this upgrade. Are you sure that you want to purchase this upgrade?\n{Fore.RED}WARNING: This action is irreversable. This also breaks the space continuum. Enter y to continue...{Fore.RESET}")
                            last_confirmation = animated_input(2)
                            if last_confirmation == "y":
                                points -= 200000
                                shop_upgrades['end'] = True
                                shop_upgrades['shopUpgradesPurchased'] += 1
                                view_ending()
                                break
                            else:
                                animated_print("Purchase canceled.")
                        else:
                            animated_print("You do not have enough resources to purchase this upgrade, please try later!")
                            continue
                    case "?exit" | "exit":
                        animated_print("Exited the shop.")
                        break
                    case _:
                        continue
                save_all_data()
                command_count += 1
        case "?readme":
            animated_print("Beaming information to your web browser...")
            webbrowser.open_new("https://github.com/Lanzoor/LCP/blob/main/README.md")
        case "?exit":
            save_all_data()
            break
        case "f":
            animated_print("You pressed f to pay respect. 🙏")
            command_count -= 1
        case "?ending":
            if not shop_upgrades['end']:
                animated_print(random.choice(["You simply can't.", "Access denied.", "Without upgrades, it can't be,", "You don't have access to this command yet...", "The lockwall won't be destroyed no matter what you try..."]))
            else:
                view_ending()
        case "?bet":
            animated_print("Pick how many points you are going to bet. Enter half to allocate half your points, quarter to allocate a quarter of your points, and 0 to exit.")
            while True:
                points_on_bet = animated_input().strip().lower()
                match points_on_bet:
                    case "half":
                        points_on_bet = points * 0.5
                    case "quarter":
                        points_on_bet = points * 0.25
                    case _:
                        try:
                            points_on_bet = int(points_on_bet)
                        except ValueError:
                            animated_print("Please enter a valid integer!")
                            continue
                break
            animated_print("Rolling wheel...")
            time.sleep(random.randint(1, 3))
            result = random.choice([0, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.5, 3, 4, 5, 10])
            pending_points = result * points_on_bet
            animated_print(f"Your result was {result}, which means that your points were multiplied by {result}.")
            points -= points_on_bet
            points += pending_points
        case _:
            continue
    command_count += 1
    if settings['autoSaveEveryCommand']:
        save_all_data()

animated_print(f"Goodbye {Fore.BLUE + username + Fore.RESET}, we hope to see you again!")

time.sleep(2.5)

raise ForceQuitted("User exited intentionally.")
