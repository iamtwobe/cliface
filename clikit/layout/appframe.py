from prompt_toolkit.application import Application
from prompt_toolkit.layout import Layout
from prompt_toolkit.widgets import TextArea
from prompt_toolkit.layout.containers import HSplit, VSplit, Window
from prompt_toolkit.widgets import Label
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.key_binding import KeyBindings
from clikit.layout.components import CLIKitFrame


class CLIKitApp:
    def __init__(self, window:Window=None, frame:CLIKitFrame=None, prefix=None, cursor=None, cursor_fg=None, style=None):
        self.window = window
        self.frame = frame
        self.style = style
        self.cursor = cursor
        self.cursor_fg = cursor_fg
        self.prefix = prefix

        prefix_label = Label(
            HTML(f'<prompt fg="{self.cursor_fg}">{self.cursor}</prompt>'),
            width=len(self.cursor)
        )
        input_area = TextArea(style='class:input', multiline=False)


        cursor_input = VSplit([
            prefix_label,
            input_area
        ])

        if self.prefix:
            layout = Layout(HSplit([
                frame,
                cursor_input,
                Label(HTML(f'<prefix fg="{self.cursor_fg}">({self.prefix})</prefix>'))
            ]))
        else:
            layout = Layout(HSplit([
                frame,
                cursor_input
            ]))

        kb = KeyBindings()
        @kb.add('enter')
        def _(event):
            text = input_area.text.strip()
            event.app.exit(result=text)

        @kb.add('c-c')
        def _(event):
            event.app.exit()

        app = Application(
            layout=layout, key_bindings=kb, style=style, full_screen=True
        )

        self.result = app.run()

    def get_result(self):
        return self.result