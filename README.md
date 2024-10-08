﻿# mouseMovement_MinimisingMaximising

This Python script is designed to simulate user activity on a Windows machine by periodically minimizing and maximizing a window (specifically Microsoft Teams) and moving the mouse cursor to random positions on the screen. The purpose of this script could be to prevent the system from going idle or to simulate user presence.

**Features**:
Minimizing and Maximizing Windows:

The minimize_maximize() function simulates the pressing of the Windows key + Down Arrow to minimize the currently active window and the Windows key + Up Arrow to maximize it again.
The script introduces a 3-second delay after each action to make the window movement more human-like.
Random Mouse Movement:

The move_cursor() function moves the mouse cursor to a random position on the screen.
The movement occurs over a brief duration of 0.25 seconds to simulate realistic cursor movement.
Infinite Loop Execution:

The script runs an infinite loop where the window minimization/maximization and cursor movement are performed repeatedly.
A 5-second delay is included between each iteration to space out the actions.
How to Use:
Run the script, and it will continuously minimize and maximize the active window and move the mouse cursor to random positions on the screen.
To stop the script, you'll need to manually interrupt it (e.g., by pressing Ctrl + C in the terminal).
Potential Use Cases:
Preventing the computer from entering sleep mode due to inactivity.
Simulating user presence in a remote desktop session.
Requirements:
pyautogui: This script requires the pyautogui library, which can be installed via pip:
pip install pyautogui

**Disclaimer:**
Use this script responsibly, especially if running on a machine that is shared with others or is subject to corporate policies. Misuse could lead to unintended consequences.






