
init python:
    # 街机色彩配置
    ARCADE_GOLD = "#f1c40f"
    ARCADE_RED = "#e74c3c"
    ARCADE_BLUE = "#3498db"
    ARCADE_GREEN = "#2ecc71"
    ARCADE_SHADOW = "#000000"
    
    # 字体样式 (模拟街机)
    style.arcade_text = Style(style.default)
    style.arcade_text.font = "SourceHanSans-Regular.ttf"
    style.arcade_text.size = 60
    style.arcade_text.color = ARCADE_GOLD
    style.arcade_text.outlines = [(4, ARCADE_SHADOW, 0, 0), (2, ARCADE_RED, 2, 2)] # 双重描边
    style.arcade_text.bold = True

    style.arcade_name = Style(style.default)
    style.arcade_name.font = "SourceHanSans-Regular.ttf"
    style.arcade_name.size = 40
    style.arcade_name.color = "#ffffff"
    style.arcade_name.outlines = [(3, "#000000", 0, 0)]
    style.arcade_name.bold = True

# ==============================================================================
# 1. 街机动画特效 (Arcade VFX)
# ==============================================================================

# 选人框闪烁
transform portrait_select_flash:
    alpha 0.0
    linear 0.2 alpha 0.5
    linear 0.2 alpha 0.0
    repeat

# 像素化入场 (模拟马赛克转场)
transform pixel_enter:
    on show:
        alpha 0.0 zoom 0.1
        linear 0.3 alpha 1.0 zoom 1.0
    on hide:
        linear 0.2 alpha 0.0 zoom 0.1

# 街机文字跳动
transform arcade_text_bounce:
    yoffset 0
    linear 0.1 yoffset -10
    linear 0.1 yoffset 0
    pause 1.0
    repeat

# 屏幕震动 (Screen Shake) - 用于 QTE 或重大事件
transform screen_shake:
    linear 0.05 xoffset -20
    linear 0.05 xoffset 20
    linear 0.05 xoffset -20
    linear 0.05 xoffset 20
    linear 0.05 xoffset 0

# 红色闪光 (Red Flash) - 用于受伤或危机
transform red_flash:
    on show:
        alpha 0.0
        linear 0.1 alpha 0.5
        linear 0.1 alpha 0.0

# 街机互动提示 (QTE Prompt)
image qte_mash_button:
    Text("PRESS A", size=80, color=ARCADE_RED, outlines=[(4, "#000000", 0, 0)])
    xalign 0.5 yalign 0.8
    block:
        linear 0.1 zoom 1.2
        linear 0.1 zoom 1.0
        repeat


# ==============================================================================
# 2. 街机 UI 元素 (Arcade UI Elements)
# ==============================================================================

# 1. 角色头像框 (Portrait Frame)
# 这是一个通用的背景框，模仿街机选人界面
image arcade_portrait_frame:
    contains:
        Solid("#000080") # 经典街机蓝底
        xsize 400 ysize 600
    contains:
        # 边框
        Solid("#ffffff")
        xsize 400 ysize 5
        yalign 0.0
    contains:
        Solid("#ffffff")
        xsize 400 ysize 5
        yalign 1.0
    contains:
        Solid("#ffffff")
        xsize 5 ysize 600
        xalign 0.0
    contains:
        Solid("#ffffff")
        xsize 5 ysize 600
        xalign 1.0

# 2. 建设进度条 (Construction Bar)
# 用于 1950s 建设篇的经营小游戏
screen construction_minigame(current_progress, target_progress):
    frame:
        xalign 0.5 yalign 0.2
        background Solid("#00000080")
        padding (20, 20)
        
        vbox:
            spacing 10
            text "PROJECT 156 PROGRESS" style "arcade_text" size 40
            
            bar:
                value current_progress
                range target_progress
                xsize 600 ysize 40
                left_bar Solid(ARCADE_GREEN)
                right_bar Solid("#555555")
                
            text "[current_progress] / [target_progress]" color "#ffffff" xalign 0.5

# --- 蓝色线：资本操纵小游戏 (Corporate Manipulation) ---
# 这是一个快速点击游戏，模拟操纵股市/镇压暴动
# 目标：保持条在中间区域 (Balance) 或者 充满 (Greed)
screen minigame_corporate(current_value, target_value):
    modal True
    zorder 100

    default click_power = 5

    add "bg cyberpunk_2050_blue" # 背景

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 50

        text "MARKET STABILIZATION PROTOCOL" style "arcade_text" size 60 color="#00ffff" outlines [(2, "#000000", 0, 0)]

        # 动态变化的进度条
        bar value current_value range target_value xsize 800 ysize 50 style "arcade_bar"

        text "CLICK TO INJECT CAPITAL" style "arcade_text" size 40 color="#ffffff"

        imagebutton:
            idle Text(" [ INJECT ] ", style="arcade_text", size=80, color="#00ffff", outlines=[(4, "#000088", 0, 0)])
            hover Text(" [ INJECT ] ", style="arcade_text", size=90, color="#ffffff", outlines=[(4, "#00ffff", 0, 0)])
            action [
                SetVariable("corporate_score", corporate_score + click_power),
                Play("sound", audio.sfx_typewriter) # 临时用打字机声模拟输入
            ]
            xalign 0.5

    # 倒计时/自动衰减逻辑需要外部 label 控制，或者在这里用 timer
    # 这里简单起见，只做显示和点击

# 3. OGAS 资源调配小游戏 (Red Timeline)
# 玩家需要点击分配算力来平衡资源
screen minigame_ogas(current_value, target_value):
    modal True
    
    add Solid("#330000") alpha 0.8
    
    vbox:
        xalign 0.5 yalign 0.5
        spacing 20
        
        text "CYBERSYN INTEGRATION" style "arcade_text" color ARCADE_RED xalign 0.5
        text "ALLOCATE COMPUTING POWER" size 30 color "#ffcccc" xalign 0.5
        
        # 进度条
        bar:
            value current_value
            range target_value
            xsize 800
            ysize 50
            style "arcade_bar"
            left_bar Solid(ARCADE_RED)
            right_bar Solid("#330000")
        
        text "[current_value] / [target_value] PETAFLOPS" size 30 color "#ffffff" xalign 0.5
        
        # 按钮
        imagebutton:
            idle Text(" [ PROCESS ] ", size=40, color=ARCADE_RED, outlines=[(2, "#000", 0, 0)])
            hover Text(" [ PROCESS ] ", size=40, color="#ffffff", outlines=[(2, "#000", 0, 0)])
            action [SetVariable("ogas_score", ogas_score + 5), Play("sound", audio.sfx_typewriter), Show("red_glitch_effect")]
            xalign 0.5

    # 成功判断
    if current_value >= target_value:
        timer 0.5 action Return(True)

# 红色故障特效
screen red_glitch_effect():
    add "overlay_glitch" alpha 0.3
    timer 0.1 action Hide("red_glitch_effect")


# 2. 生命值槽风格的数值条 (Health Bar Style Stat)
image health_bar_bg:
    Solid("#550000")
    ysize 20 xsize 200

image health_bar_fill:
    Solid(ARCADE_GOLD)
    ysize 20 xsize 200

# ==============================================================================
# 3. 街机化角色立绘 (Arcade Portraits)
# ==============================================================================

# 毛泽东 (街机版)
image mao arcade:
    contains:
        "arcade_portrait_frame"
    contains:
        Text("毛泽东", style="arcade_text", color=ARCADE_RED)
        xalign 0.5 yalign 0.5
        arcade_text_bounce
    contains:
        Text("LEADER", size=30, color="#ffffff", outlines=[(2,"#000",0,0)])
        xalign 0.5 yalign 0.8

# 蒋介石 (街机版)
image chiang arcade:
    contains:
        "arcade_portrait_frame"
    contains:
        Solid("#000000") # 蒋用黑底
        xsize 390 ysize 590 xalign 0.5 yalign 0.5
    contains:
        Text("蒋介石", style="arcade_text", color="#3498db") # 蓝色字体
        xalign 0.5 yalign 0.5
    contains:
        Text("BOSS", size=30, color="#ffffff", outlines=[(2,"#000",0,0)])
        xalign 0.5 yalign 0.8

# 鲁迅 (街机版)
image lu arcade:
    contains:
        "arcade_portrait_frame"
    contains:
        Text("鲁迅", style="arcade_text", color="#ecf0f1")
        xalign 0.5 yalign 0.5
    contains:
        Text("MENTOR", size=30, color="#ffffff", outlines=[(2,"#000",0,0)])
        xalign 0.5 yalign 0.8

# 陈赓 (街机版)
image chen arcade:
    contains:
        "arcade_portrait_frame"
    contains:
        Text("陈赓", style="arcade_text", color=ARCADE_GOLD)
        xalign 0.5 yalign 0.5
    contains:
        Text("GENERAL", size=30, color="#ffffff", outlines=[(2,"#000",0,0)])
        xalign 0.5 yalign 0.8

# 钱学森 (街机版)
image qian arcade:
    contains:
        "arcade_portrait_frame"
    contains:
        Text("钱学森", style="arcade_text", color=ARCADE_BLUE)
        xalign 0.5 yalign 0.5
    contains:
        Text("SCIENTIST", size=30, color="#ffffff", outlines=[(2,"#000",0,0)])
        xalign 0.5 yalign 0.8

# ==============================================================================
# 3.1 侧边头像定义 (Side Images)
# ==============================================================================

# 自动缩放的侧边头像
image side mao = Transform("mao arcade", zoom=0.5, xalign=0.0, yalign=1.0)
image side chiang = Transform("chiang arcade", zoom=0.5, xalign=0.0, yalign=1.0)
image side lu = Transform("lu arcade", zoom=0.5, xalign=0.0, yalign=1.0)
image side chen = Transform("chen arcade", zoom=0.5, xalign=0.0, yalign=1.0)
image side qian = Transform("qian arcade", zoom=0.5, xalign=0.0, yalign=1.0)

# ==============================================================================
# 4. 街机 HUD (Head-Up Display)
# ==============================================================================
screen arcade_hud():
    frame:
        xalign 0.0 yalign 0.0
        background None
        padding (20, 20)
        
        vbox:
            spacing 10
            
            # 玩家 1 (Player 1)
            text "1UP" size 30 color ARCADE_RED outlines [(2, "#000", 0, 0)] bold True
            
            # 生产力 (Productivity) -> 类似分数
            hbox:
                text "PROD" size 20 color ARCADE_GOLD outlines [(2, "#000", 0, 0)] yalign 0.5
                bar:
                    value gs.productivity
                    range 100
                    xsize 200 ysize 20
                    left_bar Solid(ARCADE_GOLD)
                    right_bar Solid("#550000")
            
            # 阶级觉悟 (Consciousness) -> 类似生命值
            hbox:
                text "MIND" size 20 color ARCADE_RED outlines [(2, "#000", 0, 0)] yalign 0.5
                bar:
                    value gs.class_consciousness
                    range 100
                    xsize 200 ysize 20
                    left_bar Solid(ARCADE_RED)
                    right_bar Solid("#550000")
            
            # 国际压力 (Danger) -> 类似能量槽
            hbox:
                text "DANGER" size 20 color ARCADE_BLUE outlines [(2, "#000", 0, 0)] yalign 0.5
                bar:
                    value gs.intl_pressure
                    range 100
                    xsize 200 ysize 20
                    left_bar Solid(ARCADE_BLUE)
                    right_bar Solid("#000055")
