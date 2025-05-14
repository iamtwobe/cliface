import subprocess
import platform
import os


def clear_terminal():
    """
    Clears the terminal screen based on the OS.
    """

    __os = platform.system().lower()

    if "linux" in __os:
        subprocess.run("clear", shell=True)
    elif "windows" in __os:
        subprocess.run("cls", shell=True)
    else:
        subprocess.run("clear", shell=True)