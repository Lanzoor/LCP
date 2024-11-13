import platform, time, tkinter, random, json, os, webbrowser

lcp_version = "v0.0.4.7-alpha"

class ForceQuitted(Exception) : ...
class FetchError(Exception) : ...

def animated_print(message: str, delay: int = 0.003, end: bool = True) -> None:
    for char in message:
        print(char, end = "", flush = True)
        time.sleep(delay)
    if end:
        print("")

def animated_input(message: str, delay: int = 0.003):
    animated_print(message, delay, False)
    return input("")

animated_print("Starting inspection...")

if not (int(platform.python_version_tuple()[2]) >= 10 or int(platform.python_version_tuple()[1]) >= 2):
    animated_print(f"You are running this program in an outdated version of the Python interpreter. Your current Python version is {platform.python_version()}, and at least version 3.10~ is recommended for this program.")
    time.sleep(10)
    raise ForceQuitted("Program exited.")

animated_print(f"Python interpreter version requirement passed! (Required: 3.10~, Current: {platform.python_version()})")

windows_version = int(platform.uname().release)

if windows_version < 11:
    animated_print(f"""Although you can proceed just fine, you're running this program on Windows {windows_version}.
This program uses the colorama module to implement vibrant colors, but terminals in Windows 10 or less won't support those coloring. 
It's highly recommended to run this program in a VSCode terminal if you want to proceed.""")

animated_print(f"Recommended Windows version passed! (Recommended: Windows 11~, Current: {windows_version})")

try:
    import pyautogui, keyboard, requests
    from colorama import Fore, Style
except ImportError:
    animated_print("""Seems like you didn't properly install the required packages for this project.
Unfortunately, we can't automatically install the packages for you / use pyInstaller because it comes with a huge risk and might not be compatiable with a lot of OS's.
Please see if you are missing anything and follow everything in https://github.com/Lanzoor/LCP/blob/main/README.md !""")
    time.sleep(10)
    raise ForceQuitted("Program exited.")

def get_latest_tag(repo_owner: str, repo_name: str) -> str:
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/tags"
    response = requests.get(url)
    if response.status_code == 200:
        tags = response.json()
        return tags[0]["name"]
    else:
        raise FetchError("Failed to fetch tags, please see if you have an internet connection.")

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
            file.write("{\"username\": \"ERR_NOT_SPECIFIED\", \"points\": 0, \"multiplier\": 1, \"commandCount\": 0, \"shopUpgrades\": {\"multiplier++\": 0, \"multiplier**\": 0, \"end\": false, \"shopUpgradesPurchased\": 0}, \"settings\": {\"useAnimation\": true, \"autoSaveEveryCommand\": true}, \"savedataVersion\": \"%s\"}" % lcp_version)
        with open(savefile_path, "r") as saveddata:
            savedata = json.load(saveddata)
        del saveddata
    except PermissionError:
        animated_print("Permission was denied. Perhaps you should download a brand-new savedata from https://github.com/Lanzoor/LCP/blob/main/savedata.json.")
        time.sleep(10)
        raise ForceQuitted("Program exited.")

animated_print("Your savefile was found! Reading data...")

savedata_version = savedata['savedataVersion']

if savedata_version != lcp_version:
    animated_print("Your savedata does not match your current version, please download one corresponding to your script version using https://github.com/Lanzoor/LCP/blob/main/savedata.json !")
username = savedata['username']
points = savedata['points']
multiplier = savedata['multiplier']
command_count = savedata['commandCount']
shop_upgrades = savedata['shopUpgrades']
settings = savedata['settings']
delay = 0.003 if settings['useAnimation'] else 0

def save_all_data():
    global savedata, username, points, multiplier, command_count, shop_upgrades, settings, delay
    savedata['username'] = username
    savedata['points'] = points
    savedata['multiplier'] = multiplier
    savedata['commandCount'] = command_count
    savedata['shopUpgrades'] = shop_upgrades
    savedata['settings'] = settings
    delay = 0.003 if settings['useAnimation'] else 0

    with open(savefile_path, "w") as saveddata:
        json.dump(savedata, saveddata)
    del saveddata

if username == "ERR_NOT_SPECIFIED":
    animated_print("Your username was not found, what can this program call you?", delay)
    while True:
        new_username = animated_input("Enter your new username!\n> ", delay).strip()
        if new_username.lower() == "err_not_specified":
            animated_print(f"Failed to initialize new username because the username you're trying resembles a default placeholder name. Please try a different one.", delay)
        elif len(new_username) < 3:
            animated_print("Usernames can't be shorter than 3 characters. Please make it longer!")
        elif len(new_username >= 20):
            animated_print("Usernames can't be longer than 19 characters. Please make it shorter!")
        else:
            animated_print(f"Your brand new username is set to {Fore.BLUE + new_username + Fore.RESET}. If you want it changed, you can always change your username via ?settings.", delay)
            username = new_username
            savedata['username'] = new_username
            break
    save_all_data()

if len(username) < 3 or len(username) >= 10:
    animated_print("Your username is either long or short. I know you edited the savedata, right? Anyways, please try a different one.", delay)
    while True:
        new_username = animated_input("Enter your new username!\n> ", delay).strip()
        if new_username.lower() == "err_not_specified":
            animated_print(f"Failed to initialize new username because the username you're trying resembles a default placeholder name. Please try a different one.", delay)
        elif len(new_username) < 3:
            animated_print("Usernames can't be shorter than 3 characters. Please make it longer!")
        elif len(new_username >= 20):
            animated_print("Usernames can't be longer than 19 characters. Please make it shorter!")
        else:
            animated_print(f"Your brand new username is set to {Fore.BLUE + new_username + Fore.RESET}. If you want it changed, you can always change your username via ?settings.", delay)
            username = new_username
            savedata['username'] = new_username
            break
    save_all_data()

animated_print("Almost done! Applying settings...", delay)

welcome_message = f"Welcome to Lanzoor Command Panel ({Fore.GREEN + lcp_version + Fore.RESET}), {Fore.BLUE + username + Fore.RESET}! Type ?help to get help about the commands you can use, or type ?exit to exit the program. Have fun!"

help_message = f"""Here are all commands you can use in Lanzoor Command Panel as of now ({Fore.GREEN + lcp_version + Fore.RESET}).

?help: Displays this help message.
?stats / ?stat: Displays your stats.
?settings: Displays the settings page.
?rand / ?random / ?roll: Rolls a random number.
?date: Displays your date.
?time: Displays your time.
?datetime / ?timedate: Displays your date and time.
?rps / ?rockpaperscissors: Play the rock paper scissors game.
?golt / ?greaterorlowerthan: Play the greater or lower than game.
?readme: Opens the README.md file for instructions.
?checkforupdates / ?checkforupdate / ?checkupdates / ?checkupdate / ?updates / ?update: Fetches data from GitHub and sees if a new version of LCP is avaliable.

?exit: Exit Lanzoor Command Panel.

And, here are some few things that you should probably consider using Lanzoor Command Panel.

This program is NOT case sensitive. This means that for using commands, it will still properly work if you input something like ?HeLP instead of ?help.
This program is entirely built in Python (with the help of a json file but that's only a json file not an actual program).
If you want to enjoy the true game, I definitely recommend playing the game without taking a peek at the game files / modifying the savefile.
If you want to ask / suggest / compliment about anything in Lanzoor Command Panel, feel free to ask me in Discord! (lanzoor)
"""

animated_print(welcome_message, delay)

while True:
    user_input = animated_input("> ", delay).strip().lower()
    match user_input:
        case "?help":
            animated_print(help_message, delay)
        case "?stats" | "?stat":
            animated_print(f"""Here are your stats on Lanzoor Command Panel;
Your username is {Fore.BLUE + username + Fore.RESET}.
You have used {Style.BRIGHT + command_count + Style.RESET_ALL} commands (excluding this command).
You have {Style.BRIGHT + points + Style.RESET_ALL} points, and your point multiplier is {Style.BRIGHT + multiplier + Style.RESET_ALL}.
You have purchased {Style.BRIGHT + str(shop_upgrades['shopUpgradesPurchased']) + Style.RESET_ALL} shop upgrades.""", delay)
        case "?settings":
            settings_message = f"""Welcome to the settings page, you can tweak some settings here!
You will have to input the setting number. Choose a setting to change, and input exit or ?exit to exit settings.

1. Use Animations: {Fore.GREEN if settings['useAnimation'] else Fore.RED + settings['useAnimation'] + Fore.RESET}
{Style.DIM}Turn this option off if you want this program to run faster, because the animation gives a small delay.{Style.RESET_ALL}
1. Autosave Every Command: {Fore.GREEN if settings['autoSaveEveryCommand'] else Fore.RED + settings['autoSaveEveryCommand'] + Fore.RESET}
{Style.DIM}Turn this option off if it takes too long to process a command or you're on a low-performace device.
In that case though, you should not try to force-quit the program (using ^C / Ctrl + C / ⌘ + C) to prevent any data loss.
Savedata will be autosaved when you exit this program, though.{Style.RESET_ALL}
3. Change Username
{Fore.RED}4. RESET DATA{Fore.RESET}"""
            animated_print(settings_message, delay)
            while True:
                settings_input = animated_input("> ", delay).strip().lower()
                match settings_input:
                    case "1":
                        settings['useAnimation'] = not (settings['useAnimation'])
                        animated_print(f"Set the setting \"Use Animations\" to {Fore.GREEN if settings['useAnimation'] else Fore.RED + settings['useAnimation'] + Fore.RESET}", delay)
                    case "2":
                        settings['autoSaveEveryCommand'] = not (settings['autoSaveEveryCommand'])
                        animated_print(f"Set the setting \"Autosave Every Command\" to {Fore.GREEN if settings['autoSaveEveryCommand'] else Fore.RED + settings['autoSaveEveryCommand'] + Fore.RESET}", delay)
                    case "3":
                        while True:
                            new_username = animated_input("Enter your new username!\n> ", delay).strip()
                            if new_username.lower() == "err_not_specified":
                                animated_print(f"Failed to initialize new username because the username you're trying resembles a default placeholder name. Please try a different one.", delay)
                            elif len(new_username) < 3:
                                animated_print("Usernames can't be shorter than 3 characters. Please make it longer!")
                            elif len(new_username >= 20):
                                animated_print("Usernames can't be longer than 19 characters. Please make it shorter!")
                            else:
                                animated_print(f"Your username is set to {Fore.BLUE + new_username + Fore.RESET}.", delay)
                                username = new_username
                                savedata['username'] = new_username
                                break
                        save_all_data()
                    case "4":
                        confirmation_message = f"""{Fore.RED}Hold up! Before you reset your entire savedata...
You can still continue on this savedata if you create backups of the savedata.json file before this action.
Once you perform this action, your savedata will be resetted without furthermore confirmations, and this program will automatically be closed.
Are you sure that you want to delete your savedata? Input y to continue.{Fore.RESET}"""
                        animated_print(confirmation_message, delay)
                        confirmation_input = animated_input("> ", delay).strip().lower()
                        if confirmation_input == "y":
                            
                            savedata['username'] = "ERR_NOT_SPECIFIED"
                            savedata['points'] = 0
                            savedata['multiplier'] = 1
                            savedata['commandCount'] = 0
                            savedata['shopUpgrades'] = {"multiplier++": 0, "multiplier**": 0, "end": False, "shopUpgradesPurchased": 0}
                            savedata['settings'] = {"useAnimation": True, "autoSaveEveryCommand": True}
                            savedata['savedataVersion'] = lcp_version
                            
                            with open(savefile_path, "w") as saveddata:
                                json.dump(savedata, saveddata)
                            del saveddata
                            
                            animated_print("Savedata deletion successful. This program will automatically close after a few seconds.", delay)
                            time.sleep(3)
                            raise ForceQuitted("Savedata reset performed; exited the program.")
                    case "?exit" | "exit":
                        animated_print("Exited settings.", delay)
                        break
                    case _:
                        continue
                save_all_data()
                command_count += 1
        case "?rand" | "?random" | "?roll":
            while True:
                minimum_number = animated_input("Enter the minimum number.\n> ", delay)
                try:
                    minimum_number = int(minimum_number)
                except ValueError:
                    animated_print("Please enter a valid integer.", delay)
                    continue
                maximum_number = animated_input("Enter the maximum number.\n> ", delay)
                try:
                    maximum_number = int(maximum_number)
                except ValueError:
                    animated_print("Please enter a valid integer.", delay)
                    continue
                if minimum_number > maximum_number:
                    animated_print(Style.DIM + "You silly! The minimum number can't be larger can the maximum number." + Style.RESET_ALL, delay)
                    continue
                if minimum_number == maximum_number:
                    animated_print(Style.DIM + "You silly! Both numbers can't be the same, otherwise it would always return the number and breaks the entire concept of random!" + Style.RESET_ALL, delay)
                    continue
                break
            animated_print(f"You picked {Style.BRIGHT}{minimum_number}{Style.RESET_ALL} as your minimum number, and {Style.BRIGHT}{maximum_number}{Style.RESET_ALL} as your maxmimum number. Your result is {Style.BRIGHT}{random.randint(minimum_number, maximum_number)}{Style.RESET_ALL}.", delay)
        case "?date":
            animated_print(f"Your current date is {Style.BRIGHT + time.strftime(r"%B %d (%A), %Y") + Style.RESET_ALL}.", delay)
        case "?time":
            animated_print(f"Your current time is {Style.BRIGHT + time.strftime(r"%X") + Style.RESET_ALL}.", delay)
        case "?datetime" | "?timedate":
            animated_print(f"Your current date & time is {Style.BRIGHT + time.strftime(r"%B %d (%A), %Y | %X") + Style.RESET_ALL}.", delay)
        case "?rps" | "?rockpaperscissors":
            user_choice = animated_input("Choose one! Rock, Paper, or Scissors! You can also only input the first character of your choice.\n> ", delay).strip().lower()
            match user_choice:
                case "r":
                    user_choice = "rock"
                case "p":
                    user_choice = "paper"
                case "s":
                    user_choice = "scissors"
            
            valid_rps_choice = ["rock", "paper", "scissors"]
            computer_choice = random.choice(valid_rps_choice)
            
            while user_choice not in valid_rps_choice:
                user_choice = animated_input("You silly, that is not a valid choice! Try again.\n> ", delay).capitalize().replace(" ","")
            
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
            animated_print(f"You picked {Style.BRIGHT + user_choice + Style.RESET_ALL}, I pick {Style.BRIGHT + computer_choice + Style.RESET_ALL}! {Style.BRIGHT + win_state + Style.RESET_ALL}\nYou gained {pending_points * multiplier} points in this game.", delay)
        case "?golt" | "?greaterorlowerthan":
            choice = random.randint(1, 100)
            attempts = 0
            while True:
                user_choice = animated_input("Enter your guess!\n> ", delay).strip()
                try:
                    user_choice = int(user_choice)
                except ValueError:
                    animated_print("Please enter a valid integer.", delay)
                    continue
                if choice < user_choice and user_choice <= 100:
                    animated_print("My number is lower than your choice, try again!", delay)
                elif user_choice > 100:
                    animated_print("Hey, that was out of the range!", delay)
                elif choice > user_choice:
                    animated_print("My number is greater than your choice, try again!", delay)
                elif choice == user_choice:
                    attempts += 1
                    animated_print(f"You've guessed it right! You used {attempts} attempts in this game, and the answer was {Style.BRIGHT}{choice}{Style.RESET_ALL}.", delay)
                    break
                attempts += 1
            pending_points = (10 - attempts) * multiplier
            points += pending_points
            if pending_points <= 0:
                animated_print(f"You used too many attempts in this game! You didn't gain any points.", delay)
            else:
                animated_print(f"You gained {pending_points} points in this game.", delay)
        case "?readme":
            animated_print("Beaming information to your web browser...", delay)
            webbrowser.open_new("https://github.com/Lanzoor/LCP/blob/main/README.md")
        case "?checkforupdates" | "?checkforupdate" | "?checkupdates" | "?checkupdate" | "?updates" | "?update":
            try:
                latest_tag = get_latest_tag("Lanzoor", "LCP")
                if latest_tag == lcp_version:
                    animated_print("Your LCP is up to date!", delay)
                else:
                    animated_print(f"Looks like there is a new version avaliable (Latest: {Fore.GREEN + lcp_version + Fore.RESET}, Current: {Fore.GREEN + lcp_version + Fore.RESET})")
                    animated_print("It's recommended that if you determine to update, you should also download a new savedata.json file if the releases say so. (Find more information in https://github.com/Lanzoor/LCP/releases)")
            except FetchError as e:
                animated_print(e, delay)
        case "?exit":
            break
        case _:
            continue
    command_count += 1
    if settings['autoSaveEveryCommand']:
        save_all_data()

save_all_data()

animated_print(f"Goodbye {Fore.BLUE + username + Fore.RESET}, see you again!", delay)

time.sleep(1)
