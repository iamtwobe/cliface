from clikit.clikit import CLIKit
from clikit.layout import CLIKitFrame, CLIKitApp
from clikit.utils import clear_terminal
from prompt_toolkit.shortcuts import set_title
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit.layout.containers import Window
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.styles import Style
import os


class InputScreen():
    def __init__(self, config: CLIKit, title:str="", text:str="", 
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

        self.title = title
        self.is_password = is_password
        self.password_char = password_char
        self.use_logo = use_logo
        self.text = text


    def show(self):
        set_title(self.terminal_name)
        clear_terminal()

        screen_logo = self.logo + "\n" if self.use_logo and self.logo else ''

        style = Style.from_dict({
            '': f'fg:{self.input_color} bg:{self.cursor_bg}',
            'input': f'fg:{self.input_color} bg:{self.cursor_bg}'
        })

        terminal_lines = os.get_terminal_size().lines

        terminal_h = ((terminal_lines - len(screen_logo.splitlines())) / 2)

        terminal_h -= 2 if (terminal_h % 1) > 0 else 0

        text = f"{'\n' * int(terminal_h)}{self.text}"

        body_text = FormattedText([
            (f"fg:{self.logo_color}", f"{screen_logo}"),
            (f"fg:{self.text_color}", text)
        ])

        window = Window(
            content=FormattedTextControl(body_text)
        )

        frame = CLIKitFrame(
                body=window,
                title=HTML(f'<style fg="{self.title_color}">{self.title}</style>'),
                style=f"bg:{self.bg_color} fg:{self.fg_color}"
            )

        app_answer = CLIKitApp(
            window=window,
            frame=frame,
            style=style,
            cursor=self.cursor,
            cursor_fg=self.cursor_fg,
            is_password=self.is_password,
            password_char=self.password_char
        )

        result = app_answer.result.lower()

        return result