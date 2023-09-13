# -*- coding: utf-8 -*-

from keys.key_bindings import KeyBindings
from layout import Layouts
from screens import Screens
from subprocess_entrypoints import background_entrypoint


background_entrypoint()

widget_defaults = dict(
    font='Arial',
    fontsize=12,
    padding=3,
)


CustomBindings = KeyBindings()
CustomLayouts = Layouts()
CustomScreens = Screens()

layouts = CustomLayouts.init_layout()
mouse, keys, groups = CustomBindings.run_entire_routine()
screens = CustomScreens.init_screens()

dgroups_key_binder = None

dgroups_app_rules = []

follow_mouse_focus = True

bring_front_click = False

floats_kept_above = True

cursor_warp = False

floating_layout = CustomLayouts.get_float_rules()

auto_fullscreen = True

focus_on_window_activation = "smart"

reconfigure_screens = True

auto_minimize = True

wl_input_rules = None

wmname = "LG3D"
