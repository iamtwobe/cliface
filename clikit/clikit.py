


class CLIKit:
    def __init__(self):
        self.terminal_name = "CLIKit"
        self.main_color = ""
        self.text_color= ""
        self.logo = ""
        self.cursor = ">"

    def config(self, *, terminal_name=None, main_color=None, text_color=None, cursor=None, logo=None):
        if terminal_name : self.terminal_name = terminal_name
        if main_color : self.main_color = main_color
        if text_color : self.text_color = text_color
        if cursor : self.cursor = cursor
        if logo : self.logo = logo