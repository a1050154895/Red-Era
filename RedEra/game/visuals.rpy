
# game/visuals.rpy

# ==========================================
# 视觉资源定义 (Visual Assets)
# ==========================================
# 集中管理所有的背景、特效和图像定义
# 采用“街机风格”：使用 Solid 纯色块 + Text 文字 + ATL 动画模拟视觉效果
# ==========================================

# ------------------------------------------
# 1. 基础纹理与特效层 (Base Textures & Overlays)
# ------------------------------------------

# 历史感基底 (Sepia/Paper)
image bg history_sepia:
    Solid("#f4ecd8")

# 历史噪点 (Grain) - 模拟老电影
image overlay_history_grain:
    Solid("#000000", alpha=0.05)
    # 可以添加快速随机位移来模拟噪点跳动
    # xoffset 0 yoffset 0
    # linear 0.05 xoffset 1 yoffset 1
    # linear 0.05 xoffset -1 yoffset -1
    # repeat

# 赤色基底 (Red Flag Wave)
image bg red_flag_wave:
    Solid("#c0392b")
    # 模拟旗帜飘动光影
    contains:
        Solid("#e74c3c", alpha=0.3)
        xsize 200
        xalign 0.0
        linear 2.0 xalign 1.0
        repeat

# 赤色光辉 (Red Glory)
image overlay_red_glory:
    Solid("#ff0000", alpha=0.1)
    breathing

# 蓝色霓虹 (Blue Neon)
image overlay_blue_neon:
    Solid("#00ffff", alpha=0.1)
    breathing
    contains:
        Text("SYSTEM_OVERRIDE", size=50, color="#00ffff", alpha=0.2, xalign=0.9, yalign=0.1)
        glitch_shake

# 赛博基底 (Cyberpunk Neon) - 历史/混合线
image bg cyberpunk_neon:
    Solid("#2c003e")
    contains:
        Text("NEON", size=300, color="#ff00ff", alpha=0.05, xalign=0.5, yalign=0.5)
        rotate 0
        linear 20.0 rotate 360
        repeat

# 赛博基底 (Blue Timeline) - 财阀/冷酷
image bg cyberpunk_2050_blue:
    Solid("#000033")
    contains:
        Text("CORP", size=300, color="#00ffff", alpha=0.05, xalign=0.5, yalign=0.5)
        rotate 0
        linear 20.0 rotate -360
        repeat
    contains:
        # 扫描线
        Solid("#00ffff", alpha=0.1, ysize=2)
        yalign 0.0
        linear 2.0 yalign 1.0
        repeat

# ------------------------------------------
# 2. 场景背景 (Scene Backgrounds)
# ------------------------------------------

# --- 1912-1949 历史篇 (风格：胶片/黑白/油画) ---

image bg beijing_snow:
    contains:
        "images/beijing_snow.png"
    contains:
        "overlay_history_grain"
    contains:
        Text("❄  ❄  ❄", size=80, color="#ffffff", xalign=0.5, yalign=0.2, alpha=0.3)
        slow_zoom

image bg shanghai_rain_night:
    contains:
        "images/shanghai_rain_night.png"
    contains:
        "overlay_history_grain"
    contains:
        Text("/// /// ///", size=100, color="#34495e", xalign=0.5, yalign=0.5, alpha=0.2)
        grain_shake

image bg may_fourth:
    contains:
        "images/may_fourth.png"
    contains:
        "overlay_history_grain"

    contains:
        Text("1919\n五四运动", size=120, color="#ffffff", xalign=0.5, yalign=0.5, text_align=0.5)
        breathing
    contains:
        Text("德先生 & 赛先生", size=60, color="#f1c40f", xalign=0.5, yalign=0.7, alpha=0.5)
        slow_zoom

image bg jinggangshan:
    contains:
        "images/jinggangshan.png"
    contains:
        "overlay_history_grain"
    contains:
        Text("1928\n井冈山", size=120, color="#ffffff", xalign=0.5, yalign=0.5, text_align=0.5)
        breathing

image bg long_march:
    contains:
        "images/long_march.png"
    contains:
        "overlay_history_grain"
    contains:
        Text("1934\n漫漫长征路", size=120, color="#ffffff", xalign=0.5, yalign=0.5, text_align=0.5)
        breathing
    contains:
        Text("👣", size=100, color="#2c3e50", alpha=0.1, xalign=0.5, yalign=0.3)
        slow_zoom

image bg yanan:
    contains:
        "images/yanan.png"
    contains:
        "overlay_history_grain"
    contains:
        Text("1937\n延安·宝塔山", size=120, color="#ffffff", xalign=0.5, yalign=0.5, text_align=0.5)
        breathing

image bg chongqing:
    contains:
        "images/chongqing.png"
    contains:
        "overlay_history_grain"
    contains:
        Text("1945\n重庆谈判", size=120, color="#ffffff", xalign=0.5, yalign=0.5, text_align=0.5)
        breathing

image bg founding:
    contains:
        "images/founding_ceremony.png"
    contains:
        "bg red_flag_wave" # 叠加赤色光影
        alpha 0.3
    contains:
        Text("1949\n开国大典", size=120, color="#f1c40f", xalign=0.5, yalign=0.5, text_align=0.5)
        breathing

# --- 角色动态立绘 (引用 gui_styles.rpy 定义的特效) ---
# 注意：这里我们保留原名，但在内容中引用新的 dynamic 样式
# 或者直接使用 Text 定义，但加入动画

image lu normal:
    "images/lu_normal.png"

image chen coat:
    "images/chen_coat.png"

image mao normal:
    "images/mao_standing.png"

image qian normal:
    "images/qian_standing.png"

image chiang uniform:
    "images/chiang_normal.png"


# --- 1950s-1976 建设篇 (风格：苏式宣传画/工业) ---

image bg tiananmen:
    contains:
        "bg red_flag_wave"
    contains:
        Text("1949\n天安门城楼", size=100, color="#f1c40f", xalign=0.5, yalign=0.5, text_align=0.5)

image bg korean_war:
    contains:
        Solid("#2c3e50")
    contains:
        "overlay_history_grain"
    contains:
        Text("1950\n跨过鸭绿江", size=100, color="#ecf0f1", xalign=0.5, yalign=0.5, text_align=0.5)
        breathing
    contains:
        Text("❄  ❄  ❄", size=80, color="#ecf0f1", xalign=0.5, yalign=0.2, alpha=0.5)
        slow_zoom

image bg factory_1953:
    contains:
        Solid("#7f8c8d")
    contains:
        "overlay_history_grain"
    contains:
        Text("1953\n第一座\n汽车制造厂", size=100, color="#f39c12", xalign=0.5, yalign=0.5, text_align=0.5)
        breathing
    contains:
        Text("⚙️", size=300, color="#000000", alpha=0.1, xalign=0.9, yalign=0.9)
        rotate 0
        linear 10.0 rotate 360
        repeat

image bg great_leap:
    contains:
        Solid("#e67e22")
    contains:
        "overlay_history_grain"
    contains:
        Text("1958\n大跃进", size=120, color="#c0392b", xalign=0.5, yalign=0.5, text_align=0.5)
        breathing
    contains:
        Text("🔥", size=200, color="#f1c40f", alpha=0.2, xalign=0.5, yalign=0.8)
        breathing

image bg atomic_bomb:
    contains:
        Solid("#8e44ad")
    contains:
        "overlay_history_grain"
    contains:
        Text("1964\n罗布泊", size=120, color="#f1c40f", xalign=0.5, yalign=0.5, text_align=0.5)
        breathing
    contains:
        Text("☢", size=300, color="#ffffff", xalign=0.5, yalign=0.5, alpha=0.1)
        slow_zoom

image bg cultural_revolution:
    contains:
        "bg red_flag_wave"
    contains:
        Text("1966\n红色海洋", size=120, color="#f1c40f", xalign=0.5, yalign=0.5, text_align=0.5)
        breathing

image bg turning_point_1976:
    contains:
        Solid("#2c3e50")
    contains:
        Text("1976\n命运的十字路口", size=100, color="#ecf0f1", xalign=0.5, yalign=0.5, text_align=0.5)
        breathing
    contains:
        Text("❓", size=200, color="#ffffff", alpha=0.1, xalign=0.5, yalign=0.5)
        slow_zoom

# --- 历史线未来 (风格：现代/简约) ---

image bg shenzhen_1992:
    contains:
        "images/shenzhen_1992.png"
    contains:
        Text("1992\n深圳·春天的故事", size=100, color="#f1c40f", xalign=0.5, yalign=0.5, text_align=0.5)
        breathing
    contains:
        Text("🏗️", size=100, color="#ffffff", alpha=0.2, xalign=0.8, yalign=0.8)
        slow_zoom

image bg olympic_2008:
    contains:
        "images/olympic_2008.png"
    contains:
        Text("2008\n北京奥运", size=120, color="#ffffff", xalign=0.5, yalign=0.5, text_align=0.5)
        breathing

image bg pandemic_2020:
    contains:
        "images/pandemic_2020.png"
    contains:
        Text("2020\n静默的世界", size=100, color="#7f8c8d", xalign=0.5, yalign=0.5, text_align=0.5)

image bg cyber_2050_history:
    contains:
        "images/cyberpunk_city.png" # 复用
    contains:
        "bg cyberpunk_neon"
        alpha 0.3
    contains:
        Text("2050\n霓虹都市", size=120, color="#e74c3c", xalign=0.5, yalign=0.5, text_align=0.5)
        breathing
    contains:
        Text("High Tech, Low Life", size=60, color="#3498db", xalign=0.5, yalign=0.7)
        glitch_shake

# --- 赤色未来线 (风格：苏式科幻/构成主义) ---

image bg ogas_1990:
    contains:
        "images/ogas_1990.png"
    contains:
        Text("1990\nOGAS 网络启动", size=100, color="#e74c3c", xalign=0.5, yalign=0.5, text_align=0.5)
        breathing
    contains:
        Text("101010101010", size=40, color="#2ecc71", xalign=0.5, yalign=0.2, alpha=0.5)
        scanline_move

image bg mind_upload_2020:
    contains:
        "images/mind_upload_2020.png"
    contains:
        Text("2020\n意识上传计划", size=100, color="#9b59b6", xalign=0.5, yalign=0.5, text_align=0.5)
        breathing
    contains:
        Text("🧠", size=200, color="#ffffff", alpha=0.1, xalign=0.5, yalign=0.5)
        breathing

image bg hive_mind_2050:
    contains:
        "images/hive_mind_2050.png"
    contains:
        "overlay_red_glory"
    contains:
        Text("2050\n赤色蜂巢", size=120, color="#f1c40f", xalign=0.5, yalign=0.5, text_align=0.5)
        breathing
    contains:
        Text("万众一心", size=80, color="#ffffff", xalign=0.5, yalign=0.7, alpha=0.8)
        slow_zoom

image qian ai:
    contains:
        "images/qian_ai.png"
    contains:
        Text("钱\n学\n森\n(AI)", size=150, color="#2ecc71", bold=True)
        xalign 0.5 yalign 0.5
    contains:
        Text("0101", size=100, color="#2ecc71", alpha=0.2, xalign=0.5, yalign=0.5)
        glitch_shake
