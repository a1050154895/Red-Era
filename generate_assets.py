from PIL import Image, ImageDraw, ImageFont
import os

# 配置
IMAGE_DIR = "RedEra/game/images"
FONT_PATH = "RedEra/game/SourceHanSans-Regular.ttf" # 复用我们刚才下载的字体

def create_placeholder_image(filename, text, size=(1920, 1080), bg_color="#2c3e50", text_color="#ecf0f1"):
    img = Image.new('RGB', size, color=bg_color)
    draw = ImageDraw.Draw(img)
    
    try:
        font = ImageFont.truetype(FONT_PATH, 80)
    except:
        font = ImageFont.load_default()
        
    # 计算文字位置居中
    # bbox = draw.textbbox((0, 0), text, font=font)
    # text_w = bbox[2] - bbox[0]
    # text_h = bbox[3] - bbox[1]
    # x = (size[0] - text_w) / 2
    # y = (size[1] - text_h) / 2
    
    # 简单居中 (为了兼容旧版PIL)
    draw.text((size[0]/2, size[1]/2), text, font=font, fill=text_color, anchor="mm")
    
    # 加一点噪点或线条增加质感
    draw.line((0, 0, size[0], size[1]), fill=text_color, width=2)
    draw.line((0, size[1], size[0], 0), fill=text_color, width=2)
    draw.rectangle((50, 50, size[0]-50, size[1]-50), outline=text_color, width=5)

    path = os.path.join(IMAGE_DIR, filename)
    img.save(path)
    print(f"Generated: {path}")

# 1. 背景图
create_placeholder_image("beijing_snow.png", "1912 北京\n紫禁城雪景", bg_color="#bdc3c7", text_color="#2c3e50")
create_placeholder_image("shanghai_rain_night.png", "1927 上海\n法租界雨夜", bg_color="#2c3e50", text_color="#f1c40f")
create_placeholder_image("may_fourth.png", "1919 五四运动\n天安门前", bg_color="#c0392b", text_color="#ecf0f1")
create_placeholder_image("red_boat.png", "1921 嘉兴\n南湖红船", bg_color="#e74c3c", text_color="#f1c40f")

# 2. 角色立绘 (长条形)
# 鲁迅
create_placeholder_image("lu_normal.png", "鲁迅\n(Lu Xun)", size=(400, 800), bg_color="#7f8c8d", text_color="#ecf0f1")
# 陈赓
create_placeholder_image("chen_coat.png", "陈赓\n(Chen Geng)", size=(400, 800), bg_color="#f39c12", text_color="#2c3e50")
# 蒋介石
create_placeholder_image("chiang_normal.png", "蒋介石\n(Chiang)", size=(400, 800), bg_color="#2c3e50", text_color="#ecf0f1")
# 毛泽东
create_placeholder_image("mao_standing.png", "毛泽东\n(Mao)", size=(400, 800), bg_color="#c0392b", text_color="#f1c40f")
# 钱学森
create_placeholder_image("qian_standing.png", "钱学森\n(Qian)", size=(400, 800), bg_color="#3498db", text_color="#ecf0f1")

# 3. 街机风格侧边头像 (Arcade Side Images)
# 对应 gui_styles.rpy 中的 Transform("mao arcade", ...)
# 尺寸建议 600x600，以便缩放
create_placeholder_image("mao_arcade.png", "MAO", size=(600, 600), bg_color="#c0392b", text_color="#f1c40f")
create_placeholder_image("chiang_arcade.png", "CHIANG", size=(600, 600), bg_color="#2980b9", text_color="#ecf0f1")
create_placeholder_image("lu_arcade.png", "LU XUN", size=(600, 600), bg_color="#7f8c8d", text_color="#ecf0f1")
create_placeholder_image("chen_arcade.png", "CHEN", size=(600, 600), bg_color="#f39c12", text_color="#2c3e50")
create_placeholder_image("qian_arcade.png", "QIAN", size=(600, 600), bg_color="#3498db", text_color="#ecf0f1")

# 4. 更多背景
create_placeholder_image("nanjing_1949.png", "1949 南京\n总统府", bg_color="#2980b9", text_color="#ecf0f1")
create_placeholder_image("cyberpunk_city.png", "2050\nCyber City", bg_color="#8e44ad", text_color="#00ffff")

# 5. 补全 visuals.rpy 中缺失的背景
create_placeholder_image("jinggangshan.png", "1928\n井冈山", bg_color="#27ae60", text_color="#ecf0f1")
create_placeholder_image("long_march.png", "1934\n长征", bg_color="#7f8c8d", text_color="#ecf0f1")
create_placeholder_image("yanan.png", "1937\n延安", bg_color="#d35400", text_color="#ecf0f1")
create_placeholder_image("chongqing.png", "1945\n重庆谈判", bg_color="#2c3e50", text_color="#ecf0f1")
create_placeholder_image("founding_ceremony.png", "1949\n开国大典", bg_color="#c0392b", text_color="#f1c40f")

create_placeholder_image("korean_war.png", "1950\n抗美援朝", bg_color="#2c3e50", text_color="#ecf0f1")
create_placeholder_image("factory_1953.png", "1953\n工业建设", bg_color="#7f8c8d", text_color="#f39c12")
create_placeholder_image("great_leap.png", "1958\n大跃进", bg_color="#e67e22", text_color="#c0392b")
create_placeholder_image("atomic_bomb.png", "1964\n原子弹", bg_color="#8e44ad", text_color="#f1c40f")
create_placeholder_image("cultural_revolution.png", "1966\n红色风暴", bg_color="#c0392b", text_color="#f1c40f")
create_placeholder_image("turning_point_1976.png", "1976\n转折点", bg_color="#2c3e50", text_color="#ecf0f1")

create_placeholder_image("shenzhen_1992.png", "1992\n深圳", bg_color="#3498db", text_color="#f1c40f")
create_placeholder_image("olympic_2008.png", "2008\n北京奥运", bg_color="#c0392b", text_color="#ecf0f1")
create_placeholder_image("pandemic_2020.png", "2020\n静默", bg_color="#ecf0f1", text_color="#7f8c8d")

create_placeholder_image("ogas_1990.png", "1990\nOGAS", bg_color="#000000", text_color="#e74c3c")
create_placeholder_image("mind_upload_2020.png", "2020\n意识上传", bg_color="#1a1a1d", text_color="#9b59b6")
create_placeholder_image("hive_mind_2050.png", "2050\n赤色蜂巢", bg_color="#c0392b", text_color="#f1c40f")

create_placeholder_image("qian_ai.png", "钱学森 AI", size=(400, 800), bg_color="#2ecc71", text_color="#000000")


