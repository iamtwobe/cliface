from prompt_toolkit import prompt
from prompt_toolkit.shortcuts import print_container, set_title
from prompt_toolkit.widgets import Frame, TextArea
import subprocess
import platform
import os


class CLIKit:
    def __init__(self):
        self.terminal_name = "CLIKit"
        self.main_color = ""
        self.text_color= ""
        self.logo = ""

    def config(self, *, terminal_name=None, main_color=None, text_color=None, logo=None):
        if terminal_name : self.terminal_name = terminal_name
        if main_color : self.main_color = main_color
        if text_color : self.text_color = text_color
        if logo : self.logo = logo


class CLIScreenOption():
    def __init__(self, config: CLIKit, screen_title:str="", screen_text:str="", options:dict=None, use_logo=False):
        if not config:
            raise Exception("No main config was given")
        if not options:
            raise Exception("No options were given")

        self.terminal_name = config.terminal_name
        self.screen_title = screen_title
        self.screen_text = screen_text
        self.main_color = config.main_color
        self.text_color = config.text_color
        self.logo = config.logo
        self.use_logo = use_logo
        self.options = {name:function for name, function in options.items()}

    def show(self):
        set_title(self.terminal_name)
        __os = platform.platform().lower()
        terminal_columns = os.get_terminal_size().columns

        if "linux" in __os:
            subprocess.run("clear")
        elif "windows" in __os:
            subprocess.run("cls")
        
        option_names, option_functions = [], []
        count = 0
        for option, function in self.options.items():
            option_names.append(f"{option} [{count + 1}]")
            function = option_functions.append(function)
            count+=1

        displaytext = ' | '.join(option_names)
        terminal_w = (terminal_columns - len(displaytext)) / 2
        if terminal_w <= 0:
            displaytext = '\n'.join(option_names)
        terminal_w -= 1 if (terminal_w % 1) > 0 else terminal_w

        print_container(
            Frame(
                TextArea(
                text=f"{self.logo + "\n" if self.use_logo and self.logo else ''}{self.screen_text + "\n" if self.screen_text else ''}{' ' * int(terminal_w)}{displaytext}"
                ),
                title=self.screen_title,
                style=f"bg:{self.main_color} fg:{self.text_color}",
            )
        )
        try:
            choice = prompt("> ")
            option_functions[int(choice) - 1]()
        except Exception:
            self.show()

class CLIScreenInput():
    def __init__(self, config: CLIKit, screen_title:str="", text:str=""):
        if not config:
            raise Exception("No main config was given")

        self.terminal_name = config.terminal_name
        self.screen_title = screen_title
        self.main_color = config.main_color
        self.text_color = config.text_color
        self.logo = config.logo
        self.text = text

    def show(self):
        set_title(self.terminal_name)
        __os = platform.platform().lower()

        if "linux" in __os:
            subprocess.run("clear")
        elif "windows" in __os:
            subprocess.run("cls")


        print_container(
            Frame(
                TextArea(text=f"{self.logo + "\n" if self.logo else ''}{self.text}"),
                title=self.screen_title,
                style=f"bg:{self.main_color} fg:{self.text_color}",
            )
        )
