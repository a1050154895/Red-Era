
# ------------------------------------------
# 核心背景 (Core Backgrounds)
# ------------------------------------------

# 游戏封面
image main_menu_bg = "images/main_menu.png"

# 历史时期
image bg beijing_snow = "images/bg_beijing_snow.jpg"
image bg shanghai_rain = "images/bg_shanghai_rain.jpg"
image bg shanghai_rain_night = "images/shanghai_rain_night.png" # 使用专用的夜景图
image bg may_fourth = "images/bg_may_fourth.jpg"
image bg red_boat = "images/red_boat.png"
image bg jinggangshan = "images/bg_jinggangshan.jpg"
image bg long_march = "images/bg_long_march.jpg"
image bg yanan = "images/bg_yanan.jpg"
image bg chongqing = "images/chongqing.png"
image bg nanjing_1949 = "images/nanjing_1949.png"
image bg founding = "images/founding_ceremony.png"

# 建国后时期
image bg korean_war = "images/korean_war.png"
image bg factory_1953 = "images/factory_1953.png"
image bg great_leap = "images/bg_great_leap.jpg"
image bg atomic_bomb = "images/atomic_bomb.png"
image bg cultural_revolution = "images/cultural_revolution.png"
image bg ogas_1990 = "images/ogas_1990.png"
image bg turning_point_1976 = "images/turning_point_1976.png"

# 现代与未来 (蓝线/赤线)
image bg shenzhen_1992 = "images/bg_shenzhen_1992.jpg"
image bg olympic_2008 = "images/olympic_2008.png"
image bg pandemic_2020 = "images/pandemic_2020.png"
image bg red_cyber_base = "images/bg_red_cyber_base.jpg"
image bg ogas_center = "images/bg_ogas_center.jpg"
image bg cyberpunk_neon = "images/bg_cyberpunk_neon.jpg"
image bg cyberpunk_city = "images/bg_cyberpunk_2050.jpg"
image bg cyberpunk_2050_blue = "images/bg_cyberpunk_2050.jpg"
image bg hive_mind_2050 = "images/hive_mind_2050.png"
image bg mind_upload_2020 = "images/mind_upload_2020.png"

# ------------------------------------------
# 2. 核心角色 (Core Characters)
# ------------------------------------------

# 毛泽东
image mao normal = "images/mao_normal.jpg"
image mao arcade = "images/mao_normal.jpg"
image mao standing = "images/mao_standing.png"

# 蒋介石
image chiang uniform = "images/chiang_uniform.jpg"
image chiang normal = "images/chiang_uniform.jpg"
image chiang arcade = "images/chiang_arcade.png"

# 鲁迅
image lu normal = "images/lu_normal.jpg"
image lu arcade = "images/lu_normal.jpg"

# 陈赓
image chen coat = "images/chen_coat.jpg"
image chen arcade = "images/chen_coat.jpg"
image chen young = "images/chen_young.jpg"

# 周恩来
image zhou coat = "images/zhou_coat.jpg"
image zhou normal = "images/zhou_coat.jpg"

# 钱学森
image qian ai = "images/qian_ai.jpg"
image qian arcade = "images/qian_ai.jpg"
image qian normal = "images/qian_ai.jpg"

# 邓小平
image deng worker = "images/deng_worker.jpg"
image deng normal = "images/deng_worker.jpg"

# 袁世凯
image yuan normal = "images/yuan_normal.jpg"

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

# 蓝色霓虹 (Blue Neon Overlay)
image overlay_blue_neon:
    Solid("#00ffff", alpha=0.1)
    contains:
        Text("CAPITAL_CYBERPUNK", size=60, color="#00ffff", alpha=0.3, xalign=0.5, yalign=0.1)
    contains:
        Solid("#00ffff", ysize=2)
        yalign 0.0
        linear 2.0 yalign 1.0
        repeat

# 红色荣光 (Red Glory Overlay)
image overlay_red_glory:
    Solid("#ff0000", alpha=0.1)
    contains:
        Text("COMMUNIST_FUTURE", size=60, color="#ffcc00", alpha=0.4, xalign=0.5, yalign=0.1)

# ------------------------------------------
# 4. 动画变换 (ATL Transforms)
# ------------------------------------------

# 街机角色标准定位：修正尺寸不匹配和露头问题
transform arcade_center:
    xalign 0.5
    yalign 1.0
    yoffset 50      # 稍微向下偏移，确保不被 HUD 遮挡
    zoom 0.8        # 统一缩小，确保角色完整露出
    on show:
        alpha 0.0 yoffset 100
        linear 0.3 alpha 1.0 yoffset 50
    on replace:
        linear 0.3 yoffset 50

transform arcade_left:
    xalign 0.2
    yalign 1.0
    yoffset 50
    zoom 0.8
    on show:
        alpha 0.0 xoffset -100
        linear 0.3 alpha 1.0 xoffset 0
    on replace:
        linear 0.3 xoffset 0

transform arcade_right:
    xalign 0.8
    yalign 1.0
    yoffset 50
    zoom 0.8
    on show:
        alpha 0.0 xoffset 100
        linear 0.3 alpha 1.0 xoffset 0
    on replace:
        linear 0.3 xoffset 0

# 像素化进场效果
transform pixel_enter:
    xalign 0.5 yalign 1.0 yoffset 50
    zoom 0.5 alpha 0.0
    parallel:
        linear 0.2 alpha 1.0
    parallel:
        linear 0.3 zoom 0.8
    parallel:
        choice:
            xoffset -10
        choice:
            xoffset 10
        choice:
            xoffset 0
        repeat 5
    xoffset 0

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
