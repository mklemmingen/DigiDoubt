import os
import platform

def open_terminal():
    os_name = platform.system()

    if os_name == 'Windows':
        # Open Command Prompt on Windows
        os.system('start cmd /k python main.py')
    elif os_name == 'Darwin':
        # Open Terminal on macOS
        os.system('osascript -e \'tell application "Terminal" to do script "python3 main.py"\'')
    elif os_name == 'Linux':
        # Open a common terminal (like GNOME Terminal) on Linux
        os.system('gnome-terminal -- python3 main.py')
    else:
        print("Unsupported OS")

if __name__ == "__main__":
    open_terminal()