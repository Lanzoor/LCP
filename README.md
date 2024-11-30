# Lanzoor Command Panel 

> Hello! Welcome to the Lanzoor Command Panel info page. Make sure to read all of this file, to download and furthermore run the Lanzoor Command Panel properly.

## What is Lanzoor Command Panel?

Lanzoor Command Panel is a Python program / game that has some useful functions and fun games.

## Installing the Python Interpreter

Sorry for the inconvenience, but Lanzoor Command Panel needs a **Python interpreter** to run. If you already installed the Python interpreter, you can skip this step.

1. Start by downloading the **Python interpreter** by clicking [here](https://python.org/downloads).
2. Download the Python installer based on your OS version.
3. Run the executable file.
4. Set the **Add to PATH** tickbox to on.
5. Click **Install Now**.

If you are done downloading the Python interpreter. You can proceed downloading the Lanzoor Command Panel itself.

## Installing Lanzoor Command Panel

Download the latest version of Lanzoor Command Panel by clicking [here](https://github.com/Lanzoor/LCP/releases/latest). Make sure to download the ZIP file. Now, unzip the ZIP file that you downloaded.

The ZIP file will include:
- **`README.md`**: Information that may be needed
- **`script.py`**: The main program
- **`savedata.json`**: Savefile for all of your progress.
- **`transfer_guide.md`**: A detailed guide on how to transfer your savedata into other versions.

> NOTE: If you already have a savefile, you can just copy-paste your previous `savefile.json` file here. You should also check out the `transfer_guide.md` file if needed.

## Running Lanzoor Command Panel

Before you run Lanzoor Command Panel, you need to install this external library.

```bash
pip install colorama
```

If that doesn't work, it's either these cases;

### 1. For some reason, pip can't be recognized as a command. In this case, you should use this command.

```bash
py -m pip install blahblahblah
```

Note that you should change this script correspondingly to the python command that you usually refer to. If `py` doesn't work, try `python`, `python3`, or `python3.13`.

### 2. Your pip is outdated. In this case, the install command will work without any problem, but to prevent any furthermore issues, run this command.

```bash
py -m pip install --upgrade pip
```

Note that you should change this script correspondingly to the python command that you usually refer to. If `py` doesn't work, try `python`, `python3`, or `python3.13`.

### 3. Your Python is not on PATH.

In the search bar (next to your Start menu / windows icon), type "Edit environment variables in your account", and click it.
After that, click "Path" and click "Edit".
If you don't see the Python interpreter in an `exe` format here, you should uninstall your Python interpreter and retrace your steps back to **Installing the Python Interpreter**.

### 4. Your Python is set to a venv.

This project does not require a venv to run, thus making it safe to switch to a global installation!


If you are done installing those files or the ZIP file, double click on the **`script.py`** file. It will show you a pop up, saying to choose which app/program to open this file with; click the option **Python**.

It will now open up the terminal, which is the Lanzoor Command Panel itself. Now have fun!

> NOTE: If you want to enjoy the true game, I definitely recommend playing the game without taking a peek at the game files / modifying the savefile.

> ANOTHER IMPORTANT NOTE: If you are updating your Lanzoor Command Panel, make sure to also download a fresh new savedata file.
> You can just proceed fine if both versions are same.
> Why? Well, this is because a new update might add an option; must also update the savedata file format according to the script.
> At least it is better than getting a lot of errors because of an undefined key.

> LAST NOTE: When you start LCP, it will go through a process called inspection; it will tell you if your savedata file is outdated or you don't have packages installed.

## Extra Information

If you want to ask / suggest / compliment about anything in Lanzoor Command Panel, feel free to ask me in Discord! (lanzoor)
If you also want to transfer your savedata between multiple versions, send your current savefile to me in Discord.

Thank you for NSP in Discord for playtesting, balancing, reporting issues and more!
