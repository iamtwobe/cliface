from clikit.clikit import CLIKit
from clikit.layout.components import CLIKitFrame
from clikit.utils import clear_terminal
from prompt_toolkit.shortcuts import prompt
from prompt_toolkit.shortcuts import print_container, set_title
from prompt_toolkit.widgets import Frame
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit.layout.containers import Window
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit.layout.containers import Window
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.validation import Validator
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.styles import Style



class ConfirmationScreen():
    def __init__(self, config: CLIKit, title:str="", text:str="", suffix=" (Y/n) ", use_logo=False):
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
        self.use_logo = use_logo
        self.text = text
        self.suffix = suffix

    def show(self):
        set_title(self.terminal_name)
        clear_terminal()

        screen_logo = self.logo + "\n" if self.use_logo and self.logo else ''

        fg_color, bg_color, logo_color = self.fg_color, self.bg_color, self.logo_color
        text_color = self.text_color
        suffix = self.suffix

        style = Style.from_dict({
            '': f'fg:{self.input_color} bg:{self.cursor_bg}',
        })

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
                title=HTML(f'<style fg="{self.title_color}">{self.title}</style>'),
                #<i, b, u, s> for more styles
                style=f"bg:{bg_color} fg:{fg_color}"
            )
        )


        yes_no_validator = Validator.from_callable(
            lambda text: text.lower() in suffix.lower(),
            error_message=f'{suffix}',
            move_cursor_to_end=True
        )

        answer = prompt(
            HTML(f'<prompt fg="{self.cursor_fg}">{self.cursor} ({suffix}) </prompt><suffix></suffix>'),
            validator=yes_no_validator,
            validate_while_typing=True,
            style=style
        )

        return answer.lower() in suffix[0]