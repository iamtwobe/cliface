from clikit.clikit import CLIKit
from prompt_toolkit import prompt
from prompt_toolkit.shortcuts import print_container, set_title
from prompt_toolkit.widgets import Frame, TextArea
from clikit.utils import clear_terminal



class InputScreen():
    def __init__(self, config: CLIKit, screen_title:str="", text:str="", is_password=False):
        if not config:
            raise Exception("No main config was given")

        self.terminal_name = config.terminal_name
        self.screen_title = screen_title
        self.main_color = config.main_color
        self.text_color = config.text_color
        self.is_password = is_password
        self.cursor = config.cursor
        self.logo = config.logo
        self.text = text

    def show(self):
        set_title(self.terminal_name)
        clear_terminal()


        print_container(
            Frame(
                TextArea(text=f"{self.logo + "\n" if self.logo else ''}{self.text}"),
                title=self.screen_title,
                style=f"bg:{self.main_color} fg:{self.text_color}",
            )
        )

        choice = prompt(f"{self.cursor} ", is_password=self.is_password)