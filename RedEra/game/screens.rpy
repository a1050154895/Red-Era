
# ==============================================================================
# Screens (Ren'Py Standard)
# ==============================================================================

init offset = -1

# ------------------------------------------------------------------------------
# Say
# ------------------------------------------------------------------------------
screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:
            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"

    if notrenpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

# ------------------------------------------------------------------------------
# Choice
# ------------------------------------------------------------------------------
screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action

# ------------------------------------------------------------------------------
# Quick Menu
# ------------------------------------------------------------------------------
screen quick_menu():
    zorder 100

    if main_menu:
        return

    hbox:
        style_prefix "quick"

        xalign 0.5
        yalign 1.0

        textbutton _("Back") action Rollback()
        textbutton _("History") action ShowMenu('history')
        textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Save") action ShowMenu('save')
        textbutton _("Q.Save") action QuickSave()
        textbutton _("Q.Load") action QuickLoad()
        textbutton _("Prefs") action ShowMenu('preferences')

# ------------------------------------------------------------------------------
# Navigation
# ------------------------------------------------------------------------------
screen navigation():
    vbox:
        style_prefix "navigation"
        xpos gui.navigation_xpos
        yalign 0.5
        spacing gui.navigation_spacing

        if main_menu:
            textbutton _("Start") action Start()
        else:
            textbutton _("History") action ShowMenu("history")
            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")
        textbutton _("Preferences") action ShowMenu("preferences")

        if _in_replay:
            textbutton _("End Replay") action EndReplay(confirm=True)
        elif not main_menu:
            textbutton _("Main Menu") action MainMenu()

        textbutton _("About") action ShowMenu("about")
       
        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
            textbutton _("Help") action ShowMenu("help")
            textbutton _("Quit") action Quit(confirm=not main_menu)

# ------------------------------------------------------------------------------
# Main Menu
# ------------------------------------------------------------------------------
screen main_menu():
    tag menu
    style_prefix "main_menu"

    add gui.main_menu_background

    frame:
        style "main_menu_frame"

    use navigation

    if gui.show_name:
        vbox:
            style "main_menu_vbox"
            text "[config.name!t]":
                style "main_menu_title"
            text "[config.version]":
                style "main_menu_version"

# ------------------------------------------------------------------------------
# Game Menu
# ------------------------------------------------------------------------------
screen game_menu(title, scroll=None, yinitial=0.0):
    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:
            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":
                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":
                    vpgrid:
                        cols 1
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True
                        transclude

                else:
                    transclude

    use navigation

    text title style "game_menu_label"

# ------------------------------------------------------------------------------
# Confirm (Previously yesno_prompt)
# ------------------------------------------------------------------------------
screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    style_prefix "confirm"
    add "gui/overlay/confirm.png"

    frame:
        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    # Right-click and escape answer "no".
    key "game_menu" action no_action

# ------------------------------------------------------------------------------
# Styles
# ------------------------------------------------------------------------------
style window:
    xalign 0.5
    yalign 1.0
    ysize gui.textbox_height

style namebox:
    xpos gui.name_xpos
    ypos gui.name_ypos
    xanchor gui.name_xalign

style say_label:
    size gui.label_text_size
    color gui.accent_color
    outlines [(2, "#000000", 0, 0)]

style say_dialogue:
    xpos gui.text_xpos
    ypos gui.text_ypos
    xsize gui.text_width
    size gui.text_size

style choice_vbox:
    xalign 0.5
    yalign 0.5
    spacing gui.choice_spacing

style choice_button_text:
    is default
    size gui.text_size
    idle_color gui.choice_button_text_idle_color
    hover_color gui.choice_button_text_hover_color

style quick_button:
    is default
    background None
    xpadding 5

style quick_button_text:
    size 20
    idle_color gui.idle_color
    hover_color gui.accent_color

style navigation_button_text:
    size 40
    color gui.text_color
    hover_color gui.accent_color

style main_menu_vbox:
    xalign 0.95
    yalign 0.95

style main_menu_title:
    size 60
    color gui.accent_color
    outlines [(4, "#000", 0, 0)]
    xalign 1.0

style main_menu_version:
    size 20
    xalign 1.0
    color "#ffffff"

style confirm_frame:
    background Solid("#333333")
    padding (40, 40)
    xalign 0.5
    yalign 0.5

style confirm_prompt_text:
    size 40
    color "#ffffff"
    outlines [(2, "#000", 0, 0)]

# ------------------------------------------------------------------------------
# Preferences
# ------------------------------------------------------------------------------
screen preferences():
    tag menu
    use game_menu(_("Preferences"), scroll="viewport"):
        vbox:
            hbox:
                box_wrap True
                if renpy.variant("pc"):
                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")

            null height 20

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:
                    label _("Text Speed")
                    bar value Preference("text speed")

                vbox:
                    label _("Auto-Forward Time")
                    bar value Preference("auto-forward time")

# ------------------------------------------------------------------------------
# Input
# ------------------------------------------------------------------------------
screen input(prompt):
    style_prefix "input"

    window:
        vbox:
            xalign gui.text_xalign
            yalign gui.textbox_yalign

            text prompt style "input_prompt"
            input id "input"

style input_prompt:
    xalign 0.0
    color gui.accent_color

style input_input:
    xalign 0.0
    color gui.text_color

