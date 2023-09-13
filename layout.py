from libqtile import layout
from libqtile.config import Match


class Layouts:
    def __init__(self):
        self.default = {
            "border_width": 2,
            "margin": 8,
            "border_focus": "#668bd7",
            "border_normal": "1D2330"
        }
    
    def init_layout(self):
        self.layouts = [
            layout.Columns(**self.default), 
        ]
        return self.layouts
    

    def get_float_rules(self):
        return layout.Floating(
            float_rules=[
                # Run the utility of `xprop` to see the wm class and name of an X client.
                *layout.Floating.default_float_rules,
                Match(wm_class="confirmreset"),  # gitk
                Match(wm_class="makebranch"),  # gitk
                Match(wm_class="maketag"),  # gitk
                Match(wm_class="ssh-askpass"),  # ssh-askpass
                Match(title="branchdialog"),  # gitk
                Match(title="pinentry"),  # GPG key password entry
            ]
        )
