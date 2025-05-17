from clikit.clikit import CLIKit
from clikit.layout.components import CLIKitFrame
from prompt_toolkit import prompt, PromptSession
from prompt_toolkit.shortcuts import print_container, set_title
from prompt_toolkit.layout.processors import PasswordProcessor
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit.layout.containers import Window
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.styles import Style
from clikit.utils import clear_terminal


class InputScreen():
    def __init__(self, config: CLIKit, screen_title:str="", text:str="", 
                is_password=False, password_char='*', use_logo=False):
        if not config:
            raise Exception("No main config was given")

        self.terminal_name = config.terminal_name
        self.bg_color = config.bg_color
        self.fg_color = config.fg_color
        self.cursor = config.cursor
        self.cursor_fg = config.cursor_fg
        self.cursor_bg = config.cursor_bg
        self.logo = config.logo
        self.logo_color = config.logo_color
        self.text_color = config.text_color
        self.input_color = config.input_color
        self.title_color = config.title_color

        self.screen_title = screen_title
        self.is_password = is_password
        self.use_logo = use_logo
        self.text = text

        self.processor = PasswordProcessor(char=password_char)


    def show(self):
        set_title(self.terminal_name)
        clear_terminal()

        session = PromptSession(input_processors=[self.processor])

        screen_logo = self.logo + "\n" if self.use_logo and self.logo else ''

        fg_color, bg_color, logo_color = self.fg_color, self.bg_color, self.logo_color
        text_color = self.text_color

        body_text = FormattedText([
            (f"fg:{logo_color}", f"{screen_logo}"),
            (f"fg:{text_color}", self.text)
        ])

        window = Window(
            content=FormattedTextControl(body_text)
        )

        print_container(
            CLIKitFrame(
                body=window,
                title=self.screen_title,
                style=f"bg:{bg_color} fg:{fg_color}"
            )
        )
        
        style = Style.from_dict({
            '': f'fg:{self.input_color} bg:{self.cursor_bg}',
        })

        if self.is_password:
            return session.prompt(HTML(f'<style fg="{self.cursor_fg}">{self.cursor} </style>'), style=style)

        return prompt(HTML(f'<style fg="{self.cursor_fg}">{self.cursor} </style>'), style=style)