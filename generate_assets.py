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
