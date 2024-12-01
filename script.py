import platform, time, random, json, os, webbrowser, base64

lcp_version = "v0.9-beta"
encoded_lcp_version = base64.b64encode(lcp_version.encode()).decode()

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
    time.sleep(5)
    raise ForceQuitted("Aborted; an outdated Python interpreter.")

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
    time.sleep(5)
    raise ForceQuitted("Aborted; missing dependencies.")

animated_print("External libraries passed!")
savefile_path = os.path.dirname(__file__) + "/savedata.json"

try:
    with open(savefile_path, "r") as saveddata:
        animated_print("Your savefile was found! Reading data...")
        savedata = json.load(saveddata)
    del saveddata
except FileNotFoundError:
    animated_print("Savedata was not found. Creating a brand-new empty savedata for you...")
    try:
        with open(savefile_path, "w") as file:
            file.write("{\"username\": \"ERR_NOT_SPECIFIED\", \"points\": 0, \"multiplier\": 1, \"commandCount\": 0, \"shopUpgrades\": {\"multiplier++\": 0, \"multiplier**\": 0, \"end\": false, \"shopUpgradesPurchased\": 0, \"bulkPlay\": 0}, \"settings\": {\"animationType\": \"char\", \"autoSaveEveryCommand\": true, \"bulkPlay\": -1, \"confirmation\": true}, \"savedataVersion\": \"%s\"}" % encoded_lcp_version)
        with open(savefile_path, "r") as saveddata:
            savedata = json.load(saveddata)
        del saveddata
    except PermissionError:
        animated_print("Permission was denied. Perhaps you should download a brand-new savedata from https://github.com/Lanzoor/LCP/blob/main/savedata.json.")
        time.sleep(10)
        raise ForceQuitted("Aborted; savefile not existing.")

savedata_version = savedata['savedataVersion']

if base64.b64decode(savedata_version.encode()).decode() != lcp_version:
    animated_print("Your savedata does not match your current version, please download one corresponding to your script version using https://github.com/Lanzoor/LCP/blob/main/savedata.json !")
    time.sleep(5)
    raise ForceQuitted("Aborted; an outdated savedata.json file.")

username = savedata['username']
points = savedata['points']
multiplier = savedata['multiplier']
bulk_limit = savedata['shopUpgrades']['bulkPlay'] * 10
command_count = savedata['commandCount']
shop_upgrades = savedata['shopUpgrades']
settings = savedata['settings']
confirmation = settings['confirmation']
animation_type = settings['animationType']

def animated_print(message: str, end: bool = True) -> None:
    if animation_type == "char":
        for char in message:
            print(char, end = "", flush = True)
            time.sleep(0.003)
        if end:
            print("")
    elif animation_type == "line":
        for lines in message.splitlines():
            for char in list(lines):
                if char != "\n":
                    print(char, end = "", flush = True)
                else:
                    print(char, flush = True)
            time.sleep(0.05)
            if end: 
                print("")
    elif animation_type == "none":
        print(message)
        if end:
            print("")

def custom_print(message: str, delay: int = 0.003, end: bool = True) -> None:
    for char in message:
        print(char, end = "", flush = True)
        if char != " ":
            time.sleep(delay)
        else:
            time.sleep(delay * 2.3)
    if end:
        print("")

def animated_input(depth: int = 0) -> object:
    animated_print(f"{" " * depth}> ", False)
    return input("")

def view_ending() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(2)
    custom_print(Style.DIM + "...where are we?", 0.25)
    time.sleep(1)
    custom_print("Is this the end of everything?", 0.15)
    time.sleep(1)
    custom_print("Yeah, I guess so.", 0.25)
    time.sleep(0.5)
    custom_print(f"...well, congrats. {Style.BRIGHT}You did it.", 0.1)
    time.sleep(2)
    custom_print("We thought you'd never do it, but this shows your patience and furthermore your personality.", 0.05)
    time.sleep(1)
    custom_print("We really wish that you had fun playing with LCP.", 0.15)
    time.sleep(1)
    custom_print("...and we appreciated everything you gave us, and what you did in LCP.", 0.04)
    time.sleep(1)
    custom_print(Style.BRIGHT + "Thank you for playing LCP! <3" + Style.RESET_ALL, 0.35)
    time.sleep(5)
    os.system('cls' if os.name == 'nt' else 'clear')
    

def save_all_data():
    global savedata, username, points, multiplier, command_count, shop_upgrades, settings, animation_type, confirmation, encoded_lcp_version
    savedata['username'] = username
    savedata['points'] = points
    savedata['multiplier'] = multiplier
    savedata['commandCount'] = command_count
    savedata['shopUpgrades'] = shop_upgrades
    savedata['settings'] = settings
    savedata['savedataVersion'] = encoded_lcp_version
    savedata['settings']['confirmation'] = confirmation
    with open(savefile_path, "w") as saveddata:
        json.dump(savedata, saveddata)
    del saveddata

if username == "ERR_NOT_SPECIFIED":
    if len(username) < 3 or len(username) >= 20:
        animated_print("Your username is either long or short. I know you edited the savedata, right? Anyways, please try a different one.\nEnter your new username!")
    else:
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

if shop_upgrades['multiplier++'] > 100:
    shop_upgrades['multiplier++'] = 100

if shop_upgrades['multiplier**'] > 50:
    shop_upgrades['multiplier**'] = 50

if shop_upgrades['bulkPlay'] > 4:
    shop_upgrades['bulkPlay'] = 4

absolute_total_shop_upgrades_purchased = shop_upgrades['multiplier++'] + shop_upgrades['multiplier**'] + int(shop_upgrades['end']) + shop_upgrades['bulkPlay']
absolute_multiplier = (shop_upgrades['multiplier++'] + shop_upgrades['multiplier**'] * 3) + 1

if absolute_total_shop_upgrades_purchased != shop_upgrades['shopUpgradesPurchased'] or shop_upgrades['shopUpgradesPurchased']:
    shop_upgrades['shopUpgradesPurchased'] = absolute_total_shop_upgrades_purchased

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
You have used {Style.BRIGHT + str(command_count) + Style.RESET_ALL} command(s) (excluding this command).
You have {Style.BRIGHT + str(points) + Style.RESET_ALL} points, and your point multiplier is {Style.BRIGHT + str(multiplier) + Style.RESET_ALL}.
You have purchased {Style.BRIGHT + str(shop_upgrades['shopUpgradesPurchased']) + Style.RESET_ALL} shop upgrade(s).""")
        case "?settings" | "?setting" | "?option" | "?options":
            settings_message = f"""Welcome to the settings page, you can tweak some settings here!
You will have to input the setting number. Choose a setting to change, and input exit or ?exit to exit settings.

1. Animation type: {Fore.BLUE if settings['animationType'] in ["char", "line"] else Fore.GREEN}{settings['animationType'].capitalize()}{Fore.RESET}
{Style.DIM}Change this option if you want this program to run faster, because the animation gives a small delay.{Style.RESET_ALL}
2. Autosave Every Command: {Fore.GREEN if settings['autoSaveEveryCommand'] else Fore.RED}{settings['autoSaveEveryCommand']}{Fore.RESET}
{Style.DIM}Turn this option off if it takes too long to process a command or you're on a low-performace device.
In that case though, you should not try to force-quit the program (using ^C / Ctrl + C / ⌘ + C) to prevent any data loss.
Savedata will be autosaved when you exit this program, though.{Style.RESET_ALL}
3. Bulk Play: {Fore.GREEN if settings['useBulkPlay'] == 1 else (Fore.RED if settings['useBulkPlay'] == 0 else Style.DIM)}{"True" if settings['useBulkPlay'] == 1 else ("False" if settings['useBulkPlay'] == 0 else "Unavaliable")}{Style.RESET_ALL}{Fore.RESET}
{Style.DIM}{"You do not have access to this command yet.\n" if settings['useBulkPlay'] == -1 else ""}This option determines whenever you use the \"Bulk Play\" feature.{Style.RESET_ALL}
4: Shop Confirmation: {Fore.GREEN if settings['confirmation'] else Fore.RED}{settings['confirmation']}{Fore.RESET}
{Style.DIM}This option turns on / off shop upgrade confirmation.{Style.RESET_ALL}
5. Change Username
{Fore.RED}6. RESET DATA{Fore.RESET}"""
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
                            if animation_type_input in ["1", "char"]:
                                settings['animationType'] = "char"
                                animation_type = "char"
                                break
                            elif animation_type_input in ["2", "line"]:
                                settings['animationType'] = "line"
                                animation_type = "line"
                                break
                            elif animation_type_input in ["3", "none"]:
                                settings['animationType'] = "none"
                                animation_type = "none"
                                break
                            elif animation_type_input in ["exit", "?exit"]:
                                changed = False
                                break
                            else:
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
                        if settings['useBulkPlay'] == -1:
                            animated_print("You do not have access to this option yet! Purchase the \"Bulk Play\" upgrade in the shop to unlock!")
                        else:
                            settings['useBulkPlay'] = 1 if settings['useBulkPlay'] == 0 else 0
                            animated_print(f"Set the setting \"Bulk Play\" to {Fore.GREEN if settings['useBulkPlay'] == 1 else Fore.RED}{bool(1 if settings['useBulkPlay'] == 1 else 0)}{Fore.RESET}")
                    case "4":
                        settings['confirmation'] = not (settings['confirmation'])
                        animated_print(f"Set the setting \"Shop Confirmation\" to {Fore.GREEN if settings['confirmation'] else Fore.RED}{settings['confirmation']}{Fore.RESET}")
                    case "5":
                        animated_print("Enter your new username!")
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
                    case "6":
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
                            savedata['shopUpgrades'] = {"multiplier++": 0, "multiplier**": 0, "end": False, "shopUpgradesPurchased": 0, "bulkPlay": 0}
                            savedata['settings'] = {"animationType": "char", "autoSaveEveryCommand": True, "useBulkPlay": -1, "confirmation": True}
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
            exit_loop = False
            error = False
            while True:
                while True:
                    animated_print("Enter the minimum number, or type exit or ?exit to exit.")
                    minimum_number = animated_input(1)
                    if minimum_number in ["exit" | "?exit"]:
                        animated_print("Exited.")
                        exit_loop = True
                        break
                    try:
                        minimum_number = int(minimum_number)
                        break
                    except ValueError:
                        animated_print("Please enter a valid minimum integer.")
                        continue
                while True:
                    animated_print("Enter the maximum number.")
                    maximum_number = animated_input(1)
                    try:
                        maximum_number = int(maximum_number)
                        break
                    except ValueError:
                        animated_print("Please enter a valid maximum integer.")
                if maximum_number < minimum_number:
                    animated_print("The maximum number can't be smaller than the minimum number! Please enter them again.")
                    continue
                if maximum_number == minimum_number:
                    animated_print("Hey, both numbers can't be the same! Please enter them again.")
                    continue
                break
            animated_print(f"You picked {Style.BRIGHT}{minimum_number}{Style.RESET_ALL} as your minimum integer, and {Style.BRIGHT}{maximum_number}{Style.RESET_ALL} as your maximum. I pick {Style.BRIGHT}{random.randint(minimum_number, maximum_number)}{Style.RESET_ALL}!")
        case "?date":
            animated_print(f"Your current date is {Style.BRIGHT + time.strftime(r"%B %d (%A), %Y") + Style.RESET_ALL}.")
        case "?time":
            animated_print(f"Your current time is {Style.BRIGHT + time.strftime(r"%X") + Style.RESET_ALL}.")
        case "?datetime" | "?timedate":
            animated_print(f"Your current date & time is {Style.BRIGHT + time.strftime(r"%B %d (%A), %Y | %X") + Style.RESET_ALL}.")
        case "?rps" | "?rockpaperscissors":
            pending_points = 0
            exit_game = False
            if settings['useBulkPlay'] == 1:
                while True:
                    try:
                        animated_print(f"Enter how many rounds you are going to play. (Limit: {int(bulk_limit)}) You can exit the rounds by entering ?exit or exit anytime during gameplay.")
                        rounds = int(animated_input(1))
                    except ValueError:
                        animated_print("Please enter a valid integer.")
                        continue
                    if rounds > bulk_limit:
                        animated_print(f"You exceeded your current bulk play limit! (Limit: {int(bulk_limit)})")
                        continue
                    if rounds == 0:
                        animated_print("You can't play zero rounds!")
                        continue
                    break
            else:
                rounds = 1
            animated_print("Choose one! Rock, Paper, or Scissors! You can also only input the first character of your choice.")
            for rps_loops in range(1, rounds + 1):
                while True:
                    user_choice = animated_input(1).strip().lower()
                    if user_choice == "r":
                        user_choice = "rock"
                    elif user_choice == "p":
                        user_choice = "paper"
                    elif user_choice == "s":
                        user_choice = "scissors"
                    elif user_choice == "exit" or user_choice == "?exit":
                        exit_game = True
                        break
                    valid_rps_choice = ["rock", "paper", "scissors"]
                    computer_choice = random.choice(valid_rps_choice)

                    if user_choice not in valid_rps_choice:
                        animated_print("You silly, that is not a valid choice! Try again.")
                        continue
                    break
                
                if exit_game:
                    break
                
                if computer_choice == user_choice:
                    win_state = "It's a draw!"
                    pending_points += 2 * multiplier
                else:
                    winning_conditions = (
                        ("rock", "scissors"),
                        ("scissors", "paper"),
                        ("paper", "rock"),
                    )
                    if (user_choice, computer_choice) in winning_conditions:
                        win_state = "You won!"
                        pending_points += 3 * multiplier
                    else:
                        win_state = "I won!"
                        pending_points += 1 * multiplier
                if rounds == 1:
                    points += pending_points
                    animated_print(f"You picked {Style.BRIGHT + user_choice + Style.RESET_ALL}, I pick {Style.BRIGHT + computer_choice + Style.RESET_ALL}! {Style.BRIGHT + win_state + Style.RESET_ALL}\nYou gained {pending_points} points in this game.")
                else:
                    animated_print(f"You picked {Style.BRIGHT + user_choice + Style.RESET_ALL}, I pick {Style.BRIGHT + computer_choice + Style.RESET_ALL}! {Style.BRIGHT + win_state + Style.RESET_ALL}")
                    animated_print(f"You completed {rps_loops} round(s) out of {rounds} rounds.")
                exit_game = False
            if exit_game:
                animated_print("You exited your round(s).")
            if rounds != 1:
                points += pending_points
                animated_print(f"You gained a total of {pending_points} points. Good job!")
        case "?golt" | "?greaterorlowerthan":
            pending_points = 0
            if settings['useBulkPlay'] == 1:
                while True:
                    try:
                        animated_print(f"Enter how many rounds you are going to play. (Limit: {int(bulk_limit)}) You can exit the rounds by entering ?exit or exit anytime during gameplay.")
                        rounds = int(animated_input(1))
                    except ValueError:
                        animated_print("Please enter a valid integer.")
                        continue
                    if rounds > bulk_limit:
                        animated_print(f"You exceeded your current bulk play limit! (Limit: {int(bulk_limit)})")
                        continue
                    if rounds == 0:
                        animated_print("You can't play zero rounds!")
                        continue
                    break
            else:
                rounds = 1
            for golt_loops in range(1, rounds + 1):
                animated_print("Enter your guess! Type rules or !rules to view the rules, or exit or ?exit to exit.")
                choice = random.randint(1, 100)
                attempts = 0
                while True:
                    user_choice = animated_input(1).strip()
                    if user_choice.lower() == "rules" or user_choice.lower() == "!rules":
                        animated_print("""Golt, aka greater or lower than game is a game where you guess a number.
I will randomly pick a number between 1 and 100 (inclusive), and your goal is to guess the number.
Everytime you fail, I will tell you if your number is greater or lower than my choice. (That's why its called golt)
Have fun!""")
                        continue
                    elif user_choice.lower() == "exit" or user_choice.lower() == "?exit":
                        exit_game = True
                        break
                    try:
                        user_choice = int(user_choice)
                    except ValueError:
                        animated_print("Please enter a valid integer.")
                        continue
                    if choice < user_choice and user_choice <= 100:
                        animated_print("My number is lower than your choice, try again!")
                        attempts += 1
                    elif user_choice > 100 or user_choice < 0:
                        animated_print("Hey, that was out of the range!")
                        continue
                    elif choice > user_choice:
                        animated_print("My number is greater than your choice, try again!")
                        attempts += 1
                    elif choice == user_choice:
                        attempts += 1
                        animated_print(f"You've guessed it right! You used {attempts} attempts in this game, and the answer was {Style.BRIGHT}{choice}{Style.RESET_ALL}.")
                        pending_points += (30 - attempts) * multiplier
                        if rounds == 1:
                            if pending_points != 0:
                                points += pending_points
                                animated_print(f"You gained {pending_points} points in this game.")
                            else:
                                animated_print("You used too many attempts! You didn't gain any points in this game.")
                        else:
                            animated_print(f"You completed {golt_loops} round(s) out of {rounds} rounds.")
                        exit_game = False
                        break
                if exit_game:
                    animated_print("You exited your round(s).")
            if rounds != 1:
                points += pending_points
                animated_print(f"You gained a total of {pending_points} points. Good job!")
        case "?shop":
            mpp_cost = round((shop_upgrades['multiplier++'] + 1) * 10 + (shop_upgrades['multiplier++'] + 2) * 4 if shop_upgrades['multiplier++'] > 1 else 20)
            mmm_cost = round((shop_upgrades['multiplier**'] + 2) * 155 + (shop_upgrades['multiplier**'] + 3) * 6)
            bulk_cost = round(((shop_upgrades['bulkPlay'] + 1) * 200) ** 1.25)
            shop_message = f"""Welcome to the shop! You can buy upgrades with your points here. Input the item number to purchase, and type ?exit or exit to exit the shop!
{Fore.YELLOW if shop_upgrades['multiplier++'] >= 100 else ""}1. Multiplier++ (Cost: {str(mpp_cost) + " points" if shop_upgrades['multiplier++'] < 100 else "MAX"}, Purchased: {Style.BRIGHT}{shop_upgrades['multiplier++']} / 100{Style.RESET_ALL}){Fore.RESET}
{Style.DIM}Adds 1 to your multiplier.{Style.RESET_ALL}
{Fore.YELLOW if shop_upgrades['multiplier**'] >= 50 else ""}2. Multiplier** (Cost: {str(mmm_cost) + " points" if shop_upgrades['multiplier**'] < 50 else "MAX"}, Purchased: {Style.BRIGHT}{shop_upgrades['multiplier**']} / 50{Style.RESET_ALL})){Fore.RESET}
{Style.DIM}Adds 3 to your multiplier.{Style.RESET_ALL}
{Fore.YELLOW if shop_upgrades['bulkPlay'] >= 4 else ""}3. Bulk Play (Cost: {str(bulk_cost) + " points" if shop_upgrades['bulkPlay'] < 4 else "MAX"}, Purchased: {Style.BRIGHT}{shop_upgrades['bulkPlay']} / 4{Style.RESET_ALL})){Fore.RESET}
{Style.DIM}Allows you to play multiple rounds of games at once. At first purchase, it will unlock the Bulk Play option which can be toggled in settings menu.
There is a limit, though; each purchase adds 10 to the maximum rounds count. First purchase also starts with 10 maximum round count.{Style.RESET_ALL}
{Fore.YELLOW if shop_upgrades['end'] else ""}4. {"???" if not shop_upgrades['end'] else "End"} (Cost: {"400 commands used (won't be spent), 200000 points (will be spent), 251 multiplier (max multiplier, won't be spent)" if not shop_upgrades['end'] else "MAX"}){Fore.RESET}
{Style.DIM}{"??????? ??? ??????." if not shop_upgrades['end'] else "Unlocks the ending."}{Style.RESET_ALL}"""
            animated_print(shop_message)
            while True:
                mpp_cost = round((shop_upgrades['multiplier++'] + 1) * 10 + (shop_upgrades['multiplier++'] + 2) * 4 if shop_upgrades['multiplier++'] > 1 else 20)
                mmm_cost = round((shop_upgrades['multiplier**'] + 2) * 155 + (shop_upgrades['multiplier**'] + 3) * 6)
                bulk_cost = round(((shop_upgrades['bulkPlay'] + 1) * 200) ** 1.25)
                settings_input = animated_input(1).strip().lower()
                match settings_input:
                    case "1":
                        if shop_upgrades['multiplier++'] >= 100:
                            animated_print(f"{Fore.YELLOW}You already maximized this upgrade!{Fore.RESET}")
                            continue
                        if points >= mpp_cost:
                            if confirmation:
                                animated_print(f"{Fore.YELLOW}You have enough points to purchase this upgrade. Are you sure that you want to purchase this upgrade? Enter y to continue.{Fore.RESET}")
                                last_confirmation = animated_input(2).strip().lower()
                                if last_confirmation == "y":
                                    points -= mpp_cost
                                    multiplier += 1
                                    shop_upgrades['multiplier++'] += 1
                                    shop_upgrades['shopUpgradesPurchased'] += 1
                                    animated_print(f"{Fore.GREEN}Purchase successful! You spent {Style.BRIGHT}{mpp_cost}{Style.NORMAL} points. You now have {Style.BRIGHT}{points}{Style.NORMAL} points and {Style.BRIGHT}{multiplier}{Style.NORMAL} multiplier.{Fore.RESET + Style.RESET_ALL}")
                                else:
                                    animated_print(f"{Fore.RED}Purchase canceled.{Fore.RESET}")
                            else:
                                points -= mpp_cost
                                multiplier += 1
                                shop_upgrades['multiplier++'] += 1
                                shop_upgrades['shopUpgradesPurchased'] += 1
                                animated_print(f"{Fore.GREEN}Purchase successful! You spent {Style.BRIGHT}{mpp_cost}{Style.NORMAL} points. You now have {Style.BRIGHT}{points}{Style.NORMAL} points and {Style.BRIGHT}{multiplier}{Style.NORMAL} multiplier.{Fore.RESET + Style.RESET_ALL}")
                        else:
                            animated_print(f"{Fore.RED}You do not have enough points to purchase this upgrade, please try later! (Required: {mpp_cost} points, Current: {points} points){Fore.RESET}")
                            continue
                    case "2":
                        if shop_upgrades['multiplier**'] >= 50:
                            animated_print(f"{Fore.YELLOW}You already maximized this upgrade!{Fore.RESET}")
                            continue
                        if points >= mmm_cost:
                            if confirmation:
                                animated_print(f"{Fore.YELLOW}You have enough points to purchase this upgrade. Are you sure that you want to purchase this upgrade? Enter y to continue.{Fore.RESET}")
                                last_confirmation = animated_input(2).strip().lower()
                                if last_confirmation == "y":
                                    points -= mmm_cost
                                    multiplier += 3
                                    shop_upgrades['multiplier**'] += 1
                                    shop_upgrades['shopUpgradesPurchased'] += 1
                                    animated_print(f"{Fore.GREEN}Purchase successful! You spent {Style.BRIGHT}{mmm_cost}{Style.NORMAL} points. You now have {Style.BRIGHT}{points}{Style.NORMAL} points and {Style.BRIGHT}{multiplier}{Style.NORMAL} multiplier.{Fore.RESET + Style.RESET_ALL}")
                                else:
                                    animated_print(f"{Fore.RED}Purchase canceled.{Fore.RESET}")
                            else:
                                multiplier += 3
                                shop_upgrades['multiplier**'] += 1
                                shop_upgrades['shopUpgradesPurchased'] += 1
                                animated_print(f"{Fore.GREEN}Purchase successful! You spent {Style.BRIGHT}{mmm_cost}{Style.NORMAL} points. You now have {Style.BRIGHT}{points}{Style.NORMAL} points and {Style.BRIGHT}{multiplier}{Style.NORMAL} multiplier.{Fore.RESET + Style.RESET_ALL}")
                        else:
                            animated_print(f"{Fore.RED}You do not have enough points to purchase this upgrade, please try later! (Required: {mmm_cost} points, Current: {points} points){Fore.RESET}")
                            continue
                    case "3":
                        if shop_upgrades['bulkPlay'] >= 4:
                            animated_print(f"{Fore.YELLOW}You already maximized this upgrade!{Fore.RESET}")
                            continue
                        if points >= bulk_cost:
                            if confirmation:
                                animated_print(f"{Fore.YELLOW}You have enough points to purchase this upgrade. Are you sure that you want to purchase this upgrade? Enter y to continue.{Fore.RESET}")
                                last_confirmation = animated_input(2).strip().lower()
                                if last_confirmation == "y":
                                    points -= bulk_cost
                                    shop_upgrades['bulkPlay'] += 1
                                    shop_upgrades['shopUpgradesPurchased'] += 1
                                    settings['useBulkPlay'] = 0
                                    animated_print(f"{Fore.GREEN}Purchase successful! You spent {Style.BRIGHT}{bulk_cost}{Style.NORMAL} points. You now have {Style.BRIGHT}{points}{Style.NORMAL} points.{Fore.RESET + Style.RESET_ALL}")
                                else:
                                    animated_print(f"{Fore.RED}Purchase canceled.{Fore.RESET}")
                            else:
                                points -= bulk_cost
                                shop_upgrades['bulkPlay'] += 1
                                shop_upgrades['shopUpgradesPurchased'] += 1
                                settings['useBulkPlay'] = 0
                                animated_print(f"{Fore.GREEN}Purchase successful! You spent {Style.BRIGHT}{bulk_cost}{Style.NORMAL} points. You now have {Style.BRIGHT}{points}{Style.NORMAL} points.{Fore.RESET + Style.RESET_ALL}")
                        else:
                            animated_print(f"{Fore.RED}You do not have enough points to purchase this upgrade, please try later! (Required: {bulk_cost} points, Current: {points} points){Fore.RESET}")
                            continue
                    case "4":
                        if shop_upgrades['end']:
                            animated_print(f"{Fore.YELLOW}You already bought this upgrade! If you want to view the ending again, use your newly unlocked command ?ending!{Fore.RESET}")
                            continue
                        if points >= 200000 and multiplier == 251 and command_count >= 400:
                            animated_print(f"...are you sure?\n{Fore.RED}WARNING: This action is irreversable. This also breaks the space continuum. Enter y to continue...{Fore.RESET}")
                            last_confirmation = animated_input(2)
                            if last_confirmation == "y":
                                points -= 200000
                                shop_upgrades['end'] = True
                                shop_upgrades['shopUpgradesPurchased'] += 1
                                view_ending()
                                break
                            else:
                                animated_print(f"{Fore.RED}Purchase canceled.{Fore.RESET}")
                        else:
                            animated_print(f"{Fore.RED}You do not have enough resources to purchase this upgrade. You must be prepared...{Fore.RESET}")
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
    command_count += 1
    if settings['autoSaveEveryCommand']:
        save_all_data()

animated_print(f"Goodbye {Fore.BLUE + username + Fore.RESET}, see you again!")

time.sleep(1)

raise ForceQuitted("User exited intentionally.")
