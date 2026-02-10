
label timeline_history_1987:
    scene black with fade
    centered "{size=40}1987年{/size}"

    "中共十三大召开，系统阐述了社会主义初级阶段理论。"
    "肯德基在北京前门开了中国第一家店。"

    jump timeline_history_1989

label timeline_history_1989:
    scene black with fade
    centered "{size=40}1989年{/size}"

    "春夏之交的政治风波。"
    "西方开始对中国进行制裁。"
    "‘冷静观察，稳住阵脚，沉着应付，韬光养晦，善于守拙，决不当头’。"

    $ gs.change_stat("stability", -20)
    $ gs.change_stat("intl_pressure", 30)

    jump timeline_history_1992

label timeline_history_1992:
    scene bg shenzhen_1992
    play music audio.bgm_history_epic
    
    "1992年，春天。一位老人在南海边画了一个圈。"
    "‘发展才是硬道理。’"
    "‘不坚持社会主义，不改革开放，不发展经济，不改善人民生活，只能是死路一条。’"
    "市场经济的浪潮再次汹涌澎湃。"

    $ gs.change_stat("productivity", 20)
    $ gs.change_stat("stability", 10)

    jump timeline_history_1997

label timeline_history_1997:
    scene black with fade
    centered "{size=40}1997年{/size}"

    "香港回归。‘一国两制’从构想变为现实。"
    "亚洲金融风暴爆发。中国坚持人民币不贬值，展现了大国担当。"

    jump timeline_history_1999

label timeline_history_1999:
    scene black with fade
    centered "{size=40}1999年{/size}"

    "澳门回归。"
    "美国轰炸中国驻南联盟大使馆。愤怒的人群包围了美国大使馆。"
    "‘神舟一号’无人飞船发射成功。"

    jump timeline_history_2001

label timeline_history_2001:
    scene black with fade
    centered "{size=40}2001年{/size}"

    "中国加入 WTO。拥抱世界市场。"
    "北京申奥成功。"
    "9.11事件爆发，国际反恐局势改变了中国的外部环境，赢得了战略机遇期。"

    $ gs.change_stat("productivity", 20)
    $ gs.change_stat("intl_pressure", -10)

    jump timeline_history_2008

label timeline_history_2008:
    scene bg olympic_2008
    play music audio.bgm_history_epic
    
    "2008年。悲喜交加的一年。"
    "汶川大地震。‘众志成城’。"
    "北京奥运会。‘同一个世界，同一个梦想’。"
    "中国向世界展示了一个现代化大国的形象。"

    jump timeline_history_2012

label timeline_history_2012:
    scene black with fade
    centered "{size=40}2012年{/size}"

    "中共十八大召开。中国进入新时代。"
    "‘中国梦’。"
    "反腐败斗争开始，‘老虎苍蝇一起打’。"

    $ gs.change_stat("stability", 10)

    jump timeline_history_2020

label timeline_history_2020:
    scene bg pandemic_2020
    play music audio.bgm_history_sad
    
    "2020年。新冠疫情爆发。"
    "武汉封城。‘山川异域，风月同天’。"
    "中国率先控制住疫情，复工复产。"
    "这是一场对国家治理体系的大考。"

    $ gs.change_stat("stability", -10)
    $ gs.change_stat("productivity", -10)

    jump timeline_history_2025

label timeline_history_2025:
    scene black with fade
    centered "{size=40}2025年{/size}"

    "‘中国制造2025’目标基本实现。"
    "新能源汽车、人工智能、量子计算。我们在科技树上开始攀登顶峰。"
    "国际环境依然严峻，脱钩断链的威胁从未停止。"

    jump timeline_history_2035

label timeline_history_2035:
    scene bg cyberpunk_city
    play music audio.bgm_history_epic
    
    "2035年。基本实现社会主义现代化。"
    "生态环境根本好转，‘美丽中国’目标基本实现。"
    "我们在月球建立了永久科研基地。"
    "这一年，人均 GDP 达到中等发达国家水平。"

    jump timeline_history_2050

label timeline_history_2050:
    scene bg beijing_snow
    play music audio.bgm_history_epic
    show overlay_red_glory
    
    "2050年。建国100周年。"
    "中华民族伟大复兴的中国梦终于实现。"
    "我们没有走上全盘资本化的赛博朋克之路，也没有走上消灭个体的机械飞升之路。"
    "这是一条‘以人为本’的科技与自然和谐共生之路。"
    "这是一个古老文明的涅槃重生。"

    centered "{size=80}{color=#e74c3c}THE END: THE GREAT REJUVENATION{/color}{/size}"
    return
