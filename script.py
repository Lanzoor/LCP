import platform, time, timeit, tkinter, random, json, os

def animated_print(message: str, delay: int = 0.005, end: bool = True) -> None:
    for char in message:
        print(char, end = "", flush = True)
        time.sleep(delay)
    if end:
        print("")

def animated_input(message: str, delay: int = 0.005):
    animated_print(message, delay, False)
    return input("")

animated_print("Starting inspection...")

if not (int(platform.python_version_tuple()[2]) >= 10 or int(platform.python_version_tuple()[1]) >= 2):
    animated_print(f"You are running this program in an outdated version of the Python interpreter. Your current Python version is {platform.python_version()}, and at least version 3.10~ is recommended for this program.")
    time.sleep(10)
    raise Exception("Program exited.")

animated_print(f"Python interpreter version requirement passed! (Required: 3.10~, Current: {platform.python_version()})")

windows_version = int(platform.uname().release)

if windows_version < 11:
    animated_print(f"""Although you can proceed just fine, you're running this program on Windows {windows_version}.
This program uses the colorama module to implement vibrant colors, but terminals in Windows 10 or less won't support those coloring. 
To run this program on Windows {windows_version}, you can either set the setting "Use Coloring" off via ?settings, or you can run this program in a VSCode terminal.""")

animated_print(f"Recommended Windows version passed! (Recommended: Windows 11~, Current: {windows_version})")

try:
    import colorama, pyautogui, keyboard
except ImportError:
    animated_print("Seems like you didn't properly install the required packages for this project. Please see if you are missing anything and follow everything in https://github.com/Lanzoor/LCP-E/blob/main/README.md!")
    time.sleep(10)
    raise Exception("Program exited.")

animated_print("External libraries passed!")
savefile_path = os.path.dirname(__file__) + "/savedata.json"

try:
    with open(savefile_path) as saveddata:
        savedata = json.load(saveddata)
    del saveddata
except FileNotFoundError:
    animated_print("Savedata was not found. If you already have a savedata.json file, copy-paste it here.")
    time.sleep(10)
    raise Exception("Program exited.")

animated_print("Your savefile was found! Reading data...")

username = savedata['username']
points = savedata['points']
multiplier = savedata['multiplier']
command_count = savedata['commandCount']
shop_upgrades = savedata['shopUpgrades']
settings = savedata['settings']
delay = 0.005 if settings['useAnimation'] else 0

if username == "ERR_NOT_SPECIFIED":
    animated_print("Your username was not found, what can this program call you?", delay)
    while True:
        new_username = animated_input("Enter your new username!\n> ", delay)
        if new_username.lower() in ["null", "undefined", "None", "ERR_NOT_SPECIFIED"]:
            animated_print(f"Sorry, but usernames can't be {new_username}. Try a different one.", delay)
        else:
            animated_print(f"Your new username is set to {new_username}. If you want it changed, you can always change your username via ?settings.", delay)
            username = new_username
            savedata['username'] = new_username
            break
    savedata['username'] = username
    with open(savefile_path, "w") as saveddata:
        savedata = json.dump(savedata, saveddata)
    del saveddata, new_username
    animated_print(f"Changes to your username was saved.", delay)

animated_print("Almost done! Applying settings...", delay)

lcp_version = "va-0.0.1"

welcome_message = f"Welcome to Lanzoor Command Panel ({lcp_version}), {username}! Type ?help to get help about the commands you can use, or type ?exit to exit the program. Have fun!"

help_message = f"""Here are all commands you can use in Lanzoor Command Panel as of now ({lcp_version}).
?help: View this help message.
?stats / ?stat: View your stats.
?settings: View the settings page.
?exit: Exit Lanzoor Command Panel.

And, here are some few things that you should probably consider using Lanzoor Command Panel.
This program is NOT case sensitive. This means that for using commands, it will still properly work if you input something like ?HeLP.
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
        case ("?stats" | "?stat"):
            animated_print(f"""Here are your stats on Lanzoor Command Panel;
Your username is {username}.
You have used {command_count} commands (excluding this command).
You have {points} points, and your point multiplier is {multiplier}.
You have purchased {shop_upgrades['shopUpgradesPurchased']} shop upgrades.
""", delay)
        case "?settings":
            if settings['useColoring']:
                settings_message = f"""Welcome to the settings page, you can tweak some settings here!
You will have to input the setting number. Choose a setting to change, and input exit or ?exit to exit settings.

1. Use Coloring: {settings['useColoring']}
2. Use Animations: {settings['useAnimation']}
3. Change Username
""" + colorama.Fore.RED + f"""4. RESET DATA""" + colorama.Fore.RESET
            else:
                settings_message = f"""Welcome to the settings page, you can tweak some settings here!
You will have to input the setting number. Choose a setting to change, and input exit or ?exit to exit settings.

1. Use Coloring: {settings['useColoring']}
2. Use Animations: {settings['useAnimation']}
3. Change Username
4. RESET DATA
"""
            animated_print(settings_message, delay)
            while True:
                settings_input = animated_input("> ", delay).strip()
                match settings_input:
                    case "1":
                        settings['useColoring'] = not (settings['useColoring'])
                        animated_print(f"Set the setting \"Use Coloring\" to {settings['useColoring']}", delay)
                    case "2":
                        settings['useAnimation'] = not (settings['useAnimation'])
                        animated_print(f"Set the setting \"Use Animations\" to {settings['useAnimation']}", delay)
                    case "3":
                        while True:
                            new_username = animated_input("Enter your new username!\n> ", delay)
                            if new_username.lower() in ["null", "undefined", "None", "ERR_NOT_SPECIFIED"]:
                                animated_print(f"Sorry, but usernames can't be {new_username}. Try a different one.", delay)
                            else:
                                animated_print(f"Your new username is set to {new_username}. If you want it changed, you can always change your username via ?settings.", delay)
                                username = new_username
                                break
                    case "4":
                        confirmation_message = """Hold up! Before you reset your entire savedata, you should probably know that
you're trying to weep our your ENTIRE savedada. You can still continue on this savedata if you create backups of the savedata.json file before this action.
Once you perform this action, your savedata will be resetted without furthermore confirmations, and this program will automatically be closed.
Are you sure that you want to delete your savedata? Input y to continue.
                    """
                        if settings['useColoring']:
                            confirmation_message = colorama.Fore.RED + confirmation_message + colorama.Fore.RESET
                        animated_print(confirmation_message, delay)
                        confirmation_input = animated_input("> ", delay).strip().lower()
                        if confirmation_input == "y":
                            
                            savedata['username'] = "ERR_NOT_SPECIFIED"
                            savedata['points'] = 0
                            savedata['multiplier'] = 1
                            savedata['commandCount'] = 0
                            savedata['shopUpgrades'] = {"multiplier++": 0, "multiplier**": 0, "end": False, "shopUpgradesPurchased": 0}
                            savedata['settings'] = {"useColoring": True, "useAnimation": True}
                            
                            with open(savefile_path, "w") as saveddata:
                                json.dump(savedata, saveddata)
                            del saveddata
                            animated_print("Savedata deletion successful. This program will automatically close after a few seconds.")
                            time.sleep(3)
                            raise Exception("Savedata reset performed; exiting the program.")
                    case ("?exit" | "exit"):
                        animated_print("Exited settings.")
                        break
                    case _:
                        command_count += 1
                        continue
                savedata['username'] = username
                savedata['points'] = points
                savedata['multiplier'] = multiplier
                savedata['commandCount'] = command_count
                savedata['shopUpgrades'] = shop_upgrades
                savedata['settings'] = settings

                with open(savefile_path, "w") as saveddata:
                    json.dump(savedata, saveddata)
                del saveddata
                command_count += 1
        case "?exit":
            break
        case _:
            continue
    command_count += 1

    savedata['username'] = username
    savedata['points'] = points
    savedata['multiplier'] = multiplier
    savedata['commandCount'] = command_count
    savedata['shopUpgrades'] = shop_upgrades
    savedata['settings'] = settings

    with open(savefile_path, "w") as saveddata:
        json.dump(savedata, saveddata)
    del saveddata

savedata['username'] = username
savedata['points'] = points
savedata['multiplier'] = multiplier
savedata['commandCount'] = command_count
savedata['shopUpgrades'] = shop_upgrades
savedata['settings'] = settings

with open(savefile_path, "w") as saveddata:
    json.dump(savedata, saveddata)
del saveddata

animated_print(f"Saved all changes. Goodbye {username}, see you again!", delay)

time.sleep(1)
