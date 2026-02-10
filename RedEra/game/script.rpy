# game/script.rpy

# ==========================================
# 0. 字体配置 (解决中文乱码)
# ==========================================
init python:
    # 将默认字体设置为我们刚才复制进去的中文字体
    style.default.font = "SourceHanSans-Regular.ttf"
    style._default.font = "SourceHanSans-Regular.ttf"

# ==========================================
# 1. 核心数值系统初始化
# ==========================================
init python:
    class GameState:
        def __init__(self):
            # 初始数值
            self.productivity = 30        # 1912年生产力低下
            self.class_consciousness = 10 # 1912年民智未开
            self.stability = 40           # 清帝退位，人心浮动
            self.intl_pressure = 80       # 列强环伺
            
        def change_stat(self, stat_name, amount):
            """
            修改数值并处理边界 (0-100)
            返回新的数值
            """
            if hasattr(self, stat_name):
                current_val = getattr(self, stat_name)
                new_val = max(0, min(100, current_val + amount))
                setattr(self, stat_name, new_val)
                return new_val
            else:
                return None

default gs = GameState()

# ==========================================
# 2. 角色定义 (Characters)
# ==========================================
# 核心导师
define mao = Character("毛泽东", color="#e74c3c", what_color="#ffffff", image="mao")

# 队友/参谋
define chen = Character("陈赓", color="#f1c40f", image="chen")
define lu = Character("鲁迅", color="#bdc3c7", image="lu")
define qian = Character("钱学森", color="#3498db", image="qian")

# 反派/对立面
define chiang = Character("蒋介石", color="#3498db", image="chiang")
define yuan = Character("袁世凯", color="#2c3e50", image="yuan")

# 旁白 (模仿街机过场文字)
define narrator = Character(None, what_color="#f1c40f", what_outlines=[(2, "#000000", 0, 0)], what_size=30, what_font="SourceHanSans-Regular.ttf")

# ==========================================
# 3. 图像占位符 (Images) -> 已迁移至 game/visuals.rpy
# ==========================================


# ==========================================
# 4. UI 定义 (HUD)
# ==========================================
# 街机 HUD 定义在 gui_styles.rpy 中 (screen arcade_hud)

# ==========================================
# 5. 游戏流程 (Flow)
# ==========================================

label start:
    # 开启街机 HUD
    show screen arcade_hud
    
    # 播放开场音乐
    play music audio.bgm_history_sad fadein 2.0
    
    # --------------------------------------
    # 序章：1912 皇冠落地
    # --------------------------------------
    scene bg beijing_snow with fade
    
    "1912年2月12日，北京。"
    "紫禁城的墙头积了厚厚的一层雪。宣统皇帝退位的诏书，刚刚发到了部院衙门。"
    "两千年的帝制，就在这一场大雪里，无声无息地断了气。"

    # 身份赋予
    "你下意识地摸了摸后脑勺——那条辫子昨天刚剪掉，现在的你，是刚从日本弘文学院回国的留学生。"
    "怀里揣着那本没读完的《天演论》，你走进了绍兴会馆。"

    show lu normal at center with dissolve
    
    "看见那个留着隶书一字胡的中年人，正对着一棵槐树发呆。"
    
    lu "（吐出一口白气）剪了辫子，这心里头倒是轻快了不少。可我看这街上的人，膝盖还是软的。"
    lu "皇上没了，可心里的皇上还在。只要这心里的皇上不倒，换谁坐那个龙椅，这天下的戏码都一样。"

    "他转过身，目光如炬地看着你。"

    lu "你说，这中国往后的路，该怎么走？是靠那一纸共和的招牌，还是得换个活法？"

    menu:
        "面对鲁迅先生的拷问，你的回答是？"

        "教育救国，开启民智 (阶级觉悟 +10, 生产力 +5)":
            $ gs.change_stat("class_consciousness", 10)
            $ gs.change_stat("productivity", 5)
            
            lu "（微微点头）难啊。但这铁屋子，总得有人去呐喊几声。哪怕是叫醒几个人稍微做点不幸的临终的苦楚，也比在睡梦中死灭强。"
            "你选择了投身新文化运动，为十年后的觉醒埋下火种。"
            jump transition_to_1927

        "实业救国，强兵富国 (生产力 +15, 国际压力 -5)":
            $ gs.change_stat("productivity", 15)
            $ gs.change_stat("intl_pressure", -5)
            
            lu "（冷笑）有了枪炮，有了工厂，若是人心还是麻木的，那造出来的也不过是供人驱策的奴隶罢了。不过...这也是一条路。"
            "你选择了实业救国的道路，试图用钢铁和资本构建国家的脊梁。"
            jump transition_to_1927

label transition_to_1927:
    scene black with fade
    "鲁迅先生看着你的背影，若有所思。"
    "你走出了绍兴会馆，走进了那场漫长而又残酷的风雪中。"
    
    # 跳转到历史编年史
    jump timeline_1913


label chapter_1_shanghai:
    # --------------------------------------
    # 第一章：1927 上海风云
    # --------------------------------------
    scene bg shanghai_rain_night with fade
    
    "1927年4月11日，夜。上海。"
    
    # 身份赋予
    "现在的你，是黄埔军校四期毕业生，中央特科驻上海联络员。"
    "腰间的勃朗宁手枪沉甸甸的，那是周主任亲自发给你的。"

    "雨像断了线的珠子，砸在法租界的青石板路上，溅起一片片浑浊的水花。"
    
    # 陈赓登场
    show chen coat at center with moveinright
    
    chen "（掸了掸风衣上的水珠，嘴角挂着一丝玩世不恭的笑）"
    chen "这鬼天气，老天爷都在替咱们哭丧呢？还是说，他在帮咱们洗地？"

    "他压低了帽檐，眼神却像鹰一样扫过四周阴暗的巷口。"

    chen "刚收到内线消息，青帮那帮徒子徒孙都在磨刀霍霍。那位‘校长’可是有些坐不住了。"
    chen "咱们那位老同学，现在可是把‘清党’两个字刻在脑门上了。"

    menu:
        "面对这即将来临的风暴，你的判断是？"
        
        "立刻通知纠察队，准备武装反击！(阶级觉悟 +5, 稳定 -5)":
            $ gs.change_stat("class_consciousness", 5)
            $ gs.change_stat("stability", -5)
            
            chen "这就对了！脑袋掉了碗大个疤，咱们手里有枪，怕他个鸟！"
            chen "我现在就去联络周主任，今晚咱们就给他来个‘瓮中捉鳖’。"
            jump event_412_clash

        "联系各界名流，试图通过舆论施压。(稳定 +5, 生产力 +2)":
            $ gs.change_stat("stability", 5)
            $ gs.change_stat("productivity", 2)
            
            chen "（皱眉）舆论？我的大决策者，秀才遇到兵，有理说不清啊。"
            chen "不过...既然你这么定，我去安排几个笔杆子。"
            jump event_412_passive

label event_412_clash:
    scene bg shanghai_rain_night
    show screen arcade_hud
    
    # --- 街机互动：QTE 战斗 ---
    "突然，一群身穿青布短衫的流氓冲破了雨幕，手里的斧头寒光闪闪。"
    chen "来得好！"
    
    # 模拟 QTE：快速点击
    show qte_mash_button at center
    "（快速点击鼠标以进行反击！）"
    $ renpy.pause(1.0, hard=True) # 模拟反应时间
    
    play sound audio.sfx_explosion # 模拟枪声
    show layer master at screen_shake
    hide qte_mash_button
    
    "砰！砰！砰！"
    "你手中的勃朗宁喷出火舌，冲在最前面的两个流氓应声倒地。"
    
    chen "别恋战！往宝山路撤！工人纠察队在那边接应！"
    
    scene black with fade
    "雨越下越大，血水混着雨水流进了下水道..."
    
    # 结果分支
    $ gs.change_stat("stability", -10)
    $ gs.change_stat("class_consciousness", 10)
    
    "虽然损失惨重，但你们保存了有生力量。这颗火种，将在未来的岁月里燎原。"
    
    jump timeline_1927_aftermath

label event_412_passive:
    scene bg shanghai_rain_night
    
    "第二天清晨，报童的叫卖声打破了死寂，但带来的却是噩耗..."
    
    play sound audio.sfx_glitch
    show layer master at red_flash
    
    "《申报》头条：工人纠察队被缴械，总工会查封。"
    "你看着手中的报纸，指甲深深嵌入了掌心。"
    
    chen "（声音沙哑）这就是‘舆论’的结果。这就是妥协的代价。"
    chen "记住这一天。鲜血会教我们怎么走接下来的路。"
    
    $ gs.change_stat("stability", 5) # 短期稳定
    $ gs.change_stat("class_consciousness", -5) # 士气低落
    $ gs.change_stat("productivity", -5) # 罢工破坏
    
    jump timeline_1927_aftermath
