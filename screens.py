from libqtile import bar, widget
from libqtile.config import Screen
import fontawesome as fa


class Screens():
    
    def __init__(self):
        self.screens = []
        self.sep_default = {
            'padding': 10, 'linewidth': 2, 'size_percent': 60
        }
        self.date_fmt = "%d-%m-%Y %H:%M:%S"
        
        self.white_color = ["#ffffff", "#ffffff"]
    
    def define_principal_screen(self):
        self.screens.append(
            Screen(
                top=bar.Bar(
                    [   
                        widget.GroupBox(
                            foreground=self.white_color,
                            background=["#3b3847", "#3b3847"],
                            fontsize=12,
                            active=["#ebebeb", "#ebebeb"],
                            inactive=["#878787", "#878787"],
                            rounded=False,
                            highlight_method='block',
                            urgent_alert_method='block',
                            this_current_screen_border=["#3e6575", "#3e6575"],
                            this_screen_border=["#000000", "#000000"],
                            other_current_screen_border=["#3b3847", "#3b3847"],
                            other_screen_border=["#3b3847", "#3b3847"],
                            disable_drag=True,
                            margin_y=2,
                            margin_x=0,
                            padding_y=5,
                            padding_x=3,
                            borderwidth=3,
                        ),
                        widget.Sep(
                            foreground=self.white_color,
                            background=["#3b3847", "#3b3847"],
                            linewidth=0,
                            padding=5,
                        ),
                        widget.Prompt(
                            foreground=self.white_color,
                            background=["#3b3847", "#3b3847"]
                        ),
                        widget.Spacer(
                            length=bar.STRETCH,
                            foreground=self.white_color,
                            background=["#3b3847", "#3b3847"]
                        ),
                        widget.TextBox(
                            text=fa.icons['caret-left'],
                            foreground=["#9c9879", "#9c9879"],
                            background=["#3b3847", "#3b3847"],
                            padding=0,
                            fontsize=37
                        ),
                        widget.Volume(
                            emoji=True,
                            foreground=self.white_color,
                            background=["#9c9879", "#9c9879"]
                        ),
                        widget.Volume(
                            foreground=self.white_color,
                            background=["#9c9879", "#9c9879"]
                        ),
                        widget.TextBox(
                            text=fa.icons['caret-left'],
                            foreground=["#633939", "#633939"],
                            background=["#9c9879", "#9c9879"],
                            padding=0,
                            fontsize=37
                        ),
                        widget.DF(
                            visible_on_warn=False,
                            partition='/home',
                            foreground=self.white_color,
                            background=["#633939", "#633939"]
                        ),
                        widget.TextBox(
                            text=fa.icons['caret-left'],
                            foreground=["#394b63", "#394b63"],
                            background=["#633939", "#633939"],
                            padding=0,
                            fontsize=37
                        ),
                        widget.Memory(
                            foreground=self.white_color,
                            background=["#394b63", "#394b63"]
                        ),
                        widget.TextBox(
                            text=fa.icons['caret-left'],
                            foreground=["#655375", "#655375"],
                            background=["#394b63", "#394b63"],
                            padding=0,
                            fontsize=37
                        ),
                        widget.CPU(
                            foreground=self.white_color,
                            background=["#655375", "#655375"]
                        ),
                        widget.TextBox(
                            text=fa.icons['caret-left'],
                            foreground=["#53755f", "#53755f"],
                            background=["#655375", "#655375"],
                            padding=0,
                            fontsize=37
                        ),
                        widget.Clock(
                            format=self.date_fmt,
                            foreground=self.white_color,
                            background=["#53755f", "#53755f"]
                        ),
                        widget.Spacer(length=10),
                    ],
                    size=20, opacity=1
                ),
                
            ),
        )
    
    def define_secondary_screen(self):
        self.screens.append(
            Screen(
                
            ),
        )

    def init_screens(self):
        self.define_principal_screen()
        self.define_secondary_screen()
        return self.screens
