
# ------------------------------------------
# 3. 特效层补充 (Additional Overlays)
# ------------------------------------------

# 通用故障 (Generic Glitch)
image overlay_glitch:
    Solid("#ffffff", alpha=0.1)
    contains:
        Text("ERROR", size=100, color="#ffffff", alpha=0.3, xalign=0.5, yalign=0.5)
        glitch_shake
    contains:
        Solid("#000000", ysize=5)
        yalign 0.5
        linear 0.1 yalign 0.0
        linear 0.1 yalign 1.0
        repeat

# 红色故障 (Red Glitch)
image overlay_red_glitch:
    Solid("#ff0000", alpha=0.2)
    contains:
        Text("SYSTEM_FAILURE", size=80, color="#ff0000", alpha=0.5, xalign=0.5, yalign=0.5)
        glitch_shake
    contains:
        Solid("#ff0000", ysize=10)
        yalign 0.5
        linear 0.05 yalign 0.2
        linear 0.05 yalign 0.8
        repeat

# ------------------------------------------
# 4. 动画变换 (ATL Transforms)
# ------------------------------------------

transform slow_zoom:
    zoom 1.0
    linear 10.0 zoom 1.1

transform breathing:
    alpha 0.2
    linear 2.0 alpha 0.4
    linear 2.0 alpha 0.2
    repeat

transform grain_shake:
    xoffset 0
    linear 0.05 xoffset 2
    linear 0.05 xoffset -2
    repeat

transform glitch_shake:
    xoffset 0 yoffset 0
    linear 0.02 xoffset 10 yoffset 5
    linear 0.02 xoffset -10 yoffset -5
    linear 0.02 xoffset 0 yoffset 0
    repeat
