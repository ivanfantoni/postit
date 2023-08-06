
class TxtColor:

    DEFAULT = '\033[39m'
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    LIGHT_GRAY = '\033[37m'
    DARK_GRAY = '\033[90m'
    LIGHT_RED = '\033[91m'
    LIGHT_GREEN = '\033[92m'
    LIGHT_YELLOW = '\033[93m'
    LIGHT_BLUE = '\033[94m'
    LIGHT_MAGENTA = '\033[95m'
    LIGHT_CYAN = '\033[96m'
    WHITE = '\033[97m'

class BgColor: 

    DEFAULT = '\033[49m'
    BLACK = '\033[40m'
    RED = '\033[41m'
    GREEN = '\033[42m'
    YELLOW = '\033[43m'
    BLUE = '\033[44m'
    MAGENTA = '\033[45m'
    CYAN = '\033[46m'
    LIGHT_GRAY = '\033[47m'
    DARK_GRAY = '\033[100m'
    LIGHT_RED = '\033[101m'
    LIGHT_GREEN = '\033[102m'
    LIGHT_YELLOW = '\033[103m'
    LIGHT_BLUE = '\033[104m'
    LIGHT_MAGENTA = '\033[105m'
    LIGHT_CYAN = '\033[106m'
    WHITE = '\033[107m'

class Styles:

    DEFAULT = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINED = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    HIDDEN= '\033[8m'
    STRIKE = '\033[9m'
    RESET_BOLD = '\033[21m'
    RESET_DIM = '\033[22m'
    RESET_ITALIC = '\033[23m'
    RESET_UNDERLINED = '\033[24m'
    RESET_BLINK = '\033[25m'
    RESET_REVERSE = '\033[27m'
    RESET_HIDDEN= '\033[28m'
    RESET_STRIKE = '\033[29m'

class Colortext:
    '''
    ## A class for styling text with ANSI escape codes.
    ### Example 1: simple text with default color and background
    `text = Colortext('Hello World!!')`
     `print(text.run())`

    ### Example 2: text with specified text color and background color
    `text = Colortext('Hello World!!')`
     `colored = text.blue().bg_yellow()`
    `print(colored.run())`

    ### Example 3: text with bold and underlined styles
    `text = Colortext('Hello World!!')`
     `colored = text.bold().underlined()`
    `print(colored.run())`

    ### Example 4: text with all available styles and colors
    `text = Colortext('Hello World!!')`
     `colored = text.blue().bg_yellow().bold().dim().underlined().blink().reverse().hidden().strike().italic()`
    `print(colored.run())`
    '''

    def __init__(self, text):
        """
        Initialize a Colortext object with the given text. 
         Args:
            text (str): The text to style.
        """

        self.text = text
        self.txt_color = ''
        self.bg = ''
        self.style = ''

    def run(self):
        """
        Return the styled text.
         Returns:
            str: The styled text.
        """

        string = f'{self.txt_color}{self.bg}{self.style}{self.text}{Styles.DEFAULT}{BgColor.DEFAULT}{TxtColor.DEFAULT}'
        return string
        
    def black(self):
        self.txt_color = TxtColor.BLACK
        return self
    
    def red(self):
        self.txt_color = TxtColor.RED
        return self
    
    def green(self):
        self.txt_color = TxtColor.GREEN
        return self
    
    def yellow(self):
        self.txt_color = TxtColor.YELLOW
        return self
    
    def blue(self):
        self.txt_color = TxtColor.BLUE
        return self
    
    def magenta(self):
        self.txt_color = TxtColor.MAGENTA
        return self
    
    def cyan(self):
        self.txt_color = TxtColor.CYAN
        return self

    def light_gray(self):
        self.txt_color = TxtColor.LIGHT_GRAY
        return self
    
    def dark_gray(self):
        self.txt_color = TxtColor.DARK_GRAY
        return self
    
    def light_red(self):
        self.txt_color = TxtColor.LIGHT_RED
        return self
    
    def light_green(self):
        self.txt_color = TxtColor.LIGHT_GREEN
        return self
    
    def light_yellow(self):
        self.txt_color = TxtColor.LIGHT_YELLOW
        return self
    
    def light_blue(self):
        self.txt_color = TxtColor.LIGHT_BLUE
        return self
    
    def light_magenta(self):
        self.txt_color = TxtColor.LIGHT_MAGENTA
        return self
    
    def light_cyan(self):
        self.txt_color = TxtColor.LIGHT_CYAN
        return self

    def white(self):
        self.txt_color = TxtColor.WHITE
        return self

    def bg_black(self):
        self.bg = BgColor.BLACK
        return self
    
    def bg_red(self):
        self.bg = BgColor.RED
        return self
    
    def bg_green(self):
        self.bg = BgColor.GREEN
        return self
    
    def bg_yellow(self):
        self.bg = BgColor.YELLOW
        return self
    
    def bg_blue(self):
        self.bg = BgColor.BLUE
        return self
    
    def bg_magenta(self):
        self.bg = BgColor.MAGENTA
        return self
    
    def bg_cyan(self):
        self.bg = BgColor.CYAN
        return self

    def bg_light_gray(self):
        self.bg = BgColor.LIGHT_GRAY
        return self
    
    def bg_dark_gray(self):
        self.bg = BgColor.DARK_GRAY
        return self
    
    def bg_light_red(self):
        self.bg = BgColor.LIGHT_RED
        return self
    
    def bg_light_green(self):
        self.bg = BgColor.LIGHT_GREEN
        return self
    
    def bg_light_yellow(self):
        self.bg = BgColor.LIGHT_YELLOW
        return self
    
    def bg_light_blue(self):
        self.bg = BgColor.LIGHT_BLUE
        return self
    
    def bg_light_magenta(self):
        self.bg = BgColor.LIGHT_MAGENTA
        return self
    
    def bg_light_cyan(self):
        self.bg = BgColor.LIGHT_CYAN
        return self

    def bg_white(self):
        self.bg = BgColor.WHITE
        return self

    def bold(self):
        self.style += Styles.BOLD
        return self

    def italic(self):
        self.style += Styles.ITALIC
        return self

    def dim(self):
        self.style += Styles.DIM
        return self

    def underlined(self):
        self.style += Styles.UNDERLINED
        return self

    def strike(self):
        self.style += Styles.STRIKE
        return self
    
    def blink(self):
        self.style += Styles.BLINK
        return self

    def reverse(self):
        self.style += Styles.REVERSE
        return self

    def hidden(self):
        self.style += Styles.HIDDEN
        return self
