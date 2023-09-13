from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from keys.binding_configs import LEFT_KEY, RIGHT_KEY, DOWN_KEY, UP_KEY
from groups import Groups


class KeyBindings():

    def __init__(self):


        self.mod = "mod4"
        self.terminal = guess_terminal()
        self.groups_nums = Groups.get_groups_number_keys()
        self.groups = [Group(i) for i in Groups.get_groups_names()]
        self.keys = []
        self.mouse = []

        self.run_entire_routine()

    def create_layout_keys(self):

        self.keys.append(Key([self.mod], LEFT_KEY, lazy.layout.left(), desc="Move focus to left"))
        self.keys.append(Key([self.mod], RIGHT_KEY, lazy.layout.right(), desc="Move focus to right"))
        self.keys.append(Key([self.mod], DOWN_KEY, lazy.layout.down(), desc="Move focus down"))
        self.keys.append(Key([self.mod], UP_KEY, lazy.layout.up(), desc="Move focus up"))

        self.keys.append(Key([self.mod, "shift"], LEFT_KEY, lazy.layout.shuffle_left(), desc="Move window to the left"))
        self.keys.append(Key([self.mod, "shift"], RIGHT_KEY, lazy.layout.shuffle_right(), desc="Move window to the right"))
        self.keys.append(Key([self.mod, "shift"], DOWN_KEY, lazy.layout.shuffle_down(), desc="Move window down"))
        self.keys.append(Key([self.mod, "shift"], UP_KEY, lazy.layout.shuffle_up(), desc="Move window up"))

        self.keys.append(Key([self.mod, "control"], LEFT_KEY, lazy.layout.grow_left(), desc="Grow window to the left"))
        self.keys.append(Key([self.mod, "control"], RIGHT_KEY, lazy.layout.grow_right(), desc="Grow window to the right"))
        self.keys.append(Key([self.mod, "control"], DOWN_KEY, lazy.layout.grow_down(), desc="Grow window down"))
        self.keys.append(Key([self.mod, "control"], UP_KEY, lazy.layout.grow_up(), desc="Grow window up"))

        self.keys.append(Key([self.mod], "n", lazy.layout.normalize()))
        self.keys.append(Key([self.mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"))

    def define_group_keys(self):
        for group, group_num in zip(self.groups, self.groups_nums):
            self.keys.extend(
                [
                    Key([self.mod], group_num,lazy.group[group.name].toscreen(),desc="Switch to group {}".format(group_num)),
                    Key([self.mod, "shift"], group_num,lazy.window.togroup(group.name),desc="Switch to & move focused window to group {}".format(group_num)),
                ]
            )

    def define_summon_keys(self):
        self.keys.append(Key([self.mod], "Return", lazy.spawn(self.terminal), desc="Launch terminal"))
        self.keys.append(Key([self.mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"))

    def define_qtile_keys(self):
        self.keys.append(Key([self.mod, "control"], "r", lazy.reload_config(), desc="Reload the config"))

    def define_window_keys(self):
        self.keys.append(Key([self.mod], "w", lazy.window.kill(), desc="Kill focused window"))
        self.keys.append(Key([self.mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"))

    def define_mouse_bindings(self):
        self.mouse.extend([
            Drag([self.mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
            Drag([self.mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
            Click([self.mod], "Button2", lazy.window.bring_to_front()),
        ])

    def run_entire_routine(self):
        self.create_layout_keys()
        self.define_summon_keys()
        self.define_qtile_keys()
        self.define_window_keys()
        return self.mouse, self.keys, self.groups
