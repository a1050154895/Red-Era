
# ------------------------------------------------------------------------------
# 结局与职员表 (Endings & Credits)
# ------------------------------------------------------------------------------

label credits:
    scene black with fade
    centered "{size=60}The End{/size}"
    
    # 简单的滚动字幕效果
    show text "{size=40}制作人\nUser & Trae AI\n\n美术设计\nTrae AI (Arcade Style)\n\n剧本\nUser\n\n程序\nTrae AI{/size}" at truecenter with MoveTransition(5.0, enter=offscreen_bottom, leave=offscreen_top)
    pause 5.0
    
    return
