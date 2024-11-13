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

Download the latest version of Lanzoor Command Panel by clicking [here](github.com/Lanzoor/LCP/releases/latest). Make sure to download the ZIP file. Now, unzip the ZIP file that you downloaded.
The ZIP file will include:
- **README.md**: Information that may be needed
- **script.py**: The main program
- **savedata.json**: Savefile for all of your progress.

> NOTE: If you already have a savefile, you can just copy-paste your previous `savefile.json` file here.

## Running Lanzoor Command Panel

Before you run Lanzoor Command Panel, you need to install some external libraries.

```ps1
pip install colorama
pip install pyautogui
pip install keyboard
pip install requests
```

If that doesn't work, it's either two cases; you don't have Python in your PATH, you should retrace your steps back to **Installing the Python Interpreter**, **OR** pip is outdated and does not match the current Python version. Run this command if its this case;

```ps1
py -m pip install --upgrade pip
```

If you are done installing those files or the ZIP file, double click on the **main.py** file. It will show you a pop up, saying to choose which app/program to open this file with; click the option **Python**.

It will now open up the terminal, which is the Lanzoor Command Panel itself. Now have fun!

> NOTE: If you want to enjoy the true game, I definitely recommend playing the game without taking a peek at the game files / modifying the savefile.

> ANOTHER IMPORTANT NOTE: If you are updating your Lanzoor Command Panel, make sure to also download a fresh new savedata file.
> Why? Well, this is because a new update might add an option; must also update the savedata file format according to the script.
> At least it is better than getting a lot of errors because of an undefined key.

## Extra Information

If you want to ask / suggest / compliment about anything in Lanzoor Command Panel, feel free to ask me in Discord! (lanzoor)
