
define config.name = _("Red Era: Divergent Paths")
define gui.show_name = True
define config.version = "0.5"

## 界面背景设置
define gui.main_menu_background = "main_menu_bg"
define gui.game_menu_background = "main_menu_bg"

define gui.about = _p("""
A branching historical visual novel exploring the destiny of China from 1912 to 2050.
""")

define build.name = "RedEra"
define config.has_sound = True
define config.has_music = True
define config.has_voice = False

## Transitions #################################################################
define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.intra_transition = dissolve
define config.after_load_transition = None
define config.end_game_transition = None
