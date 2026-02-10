
# ------------------------------------------------------------------------------
# 结局与职员表 (Endings & Credits)
# ------------------------------------------------------------------------------

label credits:
    scene black with fade
    play music audio.bgm_history_epic fadein 2.0
    centered "{size=60}The End{/size}"
    
    # 简单的滚动字幕效果
    show text "{size=40}制作人\nUser & Trae AI\n\n美术设计\nTrae AI (Arcade Style)\n\n剧本\nUser\n\n程序\nTrae AI{/size}" at truecenter
    with moveinbottom
    pause 2.0
    hide text with moveouttop
    
    return

