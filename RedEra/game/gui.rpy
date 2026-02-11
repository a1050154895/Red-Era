
# ==============================================================================
# GUI Configuration
# ==============================================================================

init python:
    # 默认分辨率
    gui.init(1280, 720)

    # ------------------------------------------
    # Colors (Arcade Theme)
    # ------------------------------------------
    gui.accent_color = '#e74c3c'        # Arcade Red
    gui.idle_color = '#888888'          # Gray
    gui.hover_color = '#f1c40f'         # Arcade Gold
    gui.selected_color = '#ffffff'      # White
    gui.insensitive_color = '#555555'   # Dark Gray
    
    gui.muted_color = '#666666'
    gui.hover_muted_color = '#999999'
    
    gui.text_color = '#ffffff'
    gui.interface_text_color = '#ffffff'

    # ------------------------------------------
    # Fonts
    # ------------------------------------------
    gui.text_font = "SourceHanSans-Regular.ttf"
    gui.name_text_font = "SourceHanSans-Regular.ttf"
    gui.interface_text_font = "SourceHanSans-Regular.ttf"

    # text size
    gui.text_size = 30
    gui.name_text_size = 40
    gui.interface_text_size = 30
    gui.label_text_size = 36
    gui.notify_text_size = 24
    gui.title_text_size = 60

    # ------------------------------------------
    # Dialogue / TextBox
    # ------------------------------------------
    gui.textbox_height = 240
    gui.textbox_yalign = 1.0

    gui.name_xpos = 360
    gui.name_ypos = 0
    gui.name_xalign = 0.5

    gui.text_xpos = 400
    gui.text_ypos = 65
    gui.text_width = 880
    gui.text_xalign = 0.5

    # ------------------------------------------
    # Choice Buttons
    # ------------------------------------------
    gui.choice_button_width = 790
    gui.choice_button_height = None
    gui.choice_tile = False
    gui.choice_button_borders = Borders(100, 10, 100, 10)
    gui.choice_button_text_idle_color = '#cccccc'
    gui.choice_button_text_hover_color = '#ffffff'
    
    # ------------------------------------------
    # Slot Buttons (Save/Load)
    # ------------------------------------------
    gui.slot_button_width = 276
    gui.slot_button_height = 206
    gui.slot_button_borders = Borders(10, 10, 10, 10)
    gui.slot_button_text_size = 14
    gui.slot_button_text_xalign = 0.5
    gui.slot_button_text_idle_color = '#aaaaaa'

    # ------------------------------------------
    # Scrollbars
    # ------------------------------------------
    gui.scrollbar_size = 12
    gui.scrollbar_tile = False
    gui.scrollbar_borders = Borders(4, 4, 4, 4)
    gui.scrollbar_unscrollable = "hide"

    # ------------------------------------------
    # History
    # ------------------------------------------
    config.history_length = 250
    gui.history_height = 140
    gui.history_name_xpos = 155
    gui.history_text_xpos = 170
    gui.history_text_width = 740

    # ------------------------------------------
    # NVL-Mode
    # ------------------------------------------
    gui.nvl_borders = Borders(0, 10, 0, 10)
    gui.nvl_list_length = 6
    gui.nvl_height = 115
    gui.nvl_spacing = 10
    gui.nvl_name_xpos = 430
    gui.nvl_text_xpos = 450
    gui.nvl_text_width = 590
    gui.nvl_button_xpos = 450
    gui.nvl_button_width = 590
