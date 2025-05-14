from clikit.clikit import CLIKit
from clikit.utils import clear_terminal
from prompt_toolkit import prompt
from prompt_toolkit.shortcuts import print_container, set_title
from prompt_toolkit.widgets import Frame, TextArea
import os


class MenuScreen():
    def __init__(self, config: CLIKit, screen_title:str="",
                screen_text:str="", options:dict=None,
                inline=True, use_logo=False):
        
        if not config:
            raise Exception("No main config was given")
        if not options:
            raise Exception("No options were given")

        self.terminal_name = config.terminal_name
        self.main_color = config.main_color
        self.text_color = config.text_color
        self.cursor = config.cursor
        self.logo = config.logo

        self.screen_title = screen_title
        self.screen_text = screen_text
        self.inline = inline
        self.use_logo = use_logo
        self.options = {name:function for name, function in options.items()}

    def show(self):
        set_title(self.terminal_name)
        clear_terminal()

        terminal_columns = os.get_terminal_size().columns

        option_names, option_functions = [], []
        count = 0
        for option, function in self.options.items():
            option_names.append(f"{option} [{count + 1}]")
            option_functions.append(function)
            count+=1

        displaytext = ' | '.join(option_names)
        terminal_w = (terminal_columns - len(displaytext)) / 2
        if terminal_w <= 0 or self.inline == False:
            displaytext = '\n'.join(option_names)
        terminal_w -= 1 if (terminal_w % 1) > 0 else terminal_w

        screen_logo = self.logo + "\n" if self.use_logo and self.logo else ''
        screen_text = self.screen_text + "\n\n" if self.screen_text else ''

        print_container(
            Frame(
                TextArea(
                text=f"{screen_logo}{screen_text}{' ' * int(terminal_w)}{displaytext}"
                ),
                title=self.screen_title,
                style=f"bg:{self.main_color} fg:{self.text_color}"
            )
        )
        try:
            choice = prompt(f"{self.cursor} ")
            option_functions[int(choice) - 1]()
        except ValueError:
            self.show()
        except IndexError:
            self.show()