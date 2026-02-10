
# game/red_timeline.rpy

# ==========================================
# 赤色未来线 (The Red Future)
# 1978 - 2050
# 风格：苏式科幻 / 赛博共产主义 / 构成主义
# ==========================================

label timeline_red_1978:
    scene bg red_cyber_base with fade
    play music audio.bgm_red_march fadein 2.0
    centered "{size=60}{color=#e74c3c}1978{/color}{/size}"

    "1978年，北京。新的最高委员会否决了‘包产到户’的提议。"
    "‘我们不能走回头路。’新的领导人在天安门城楼上宣布，‘如果生产力不足，那就用技术来弥补，而不是资本。’"
    "国家计划委员会改组为‘国家控制论委员会’ (NCC)。"
    
    $ gs.change_stat("class_consciousness", 10)
    $ gs.change_stat("productivity", -5)

    jump timeline_red_1986

label timeline_red_1986:
    scene black with fade
    centered "{size=40}1986年{/size}"

    "‘863’计划启动。重点不是追赶，而是超越。"
    "生物工程、航天技术、信息技术。我们跳过了消费电子阶段，直接进入重工业数字化。"
    "同年，切尔诺贝利核电站事故被中国的远程机器人部队迅速控制。苏联对此感激涕零。"

    jump timeline_red_1991

label timeline_red_1991:
    scene bg beijing_snow
    play music audio.bgm_history_tension
    
    "1991年，寒冬。莫斯科发来绝密求救信号。"
    "苏联濒临解体，经济崩溃，加盟共和国离心离德。"
    "NCC 的超级计算机‘红星一号’给出了计算结果：如果我们接入苏联的 OGAS 系统，可以接管其经济调配，挽救联盟。"
    "但这也可能导致我们的系统过载。"

    menu:
        "启动‘红星计划’：接管苏联经济网络":
            jump timeline_red_ogas_minigame
        "拒绝：这是他们修正主义的恶果":
            "我们拒绝了。苏联解体。我们成为了唯一的红色堡垒，更加孤独，但也更加纯粹。"
            $ gs.change_stat("intl_pressure", 20)
            jump timeline_red_2000_isolation

label timeline_red_ogas_minigame:
    "我们需要调配全国的算力来支撑两个超级大国的经济网络！"
    $ ogas_score = 0
    $ target_ogas_score = 50
    
    # 调用 OGAS 小游戏
    call screen minigame_ogas(ogas_score, target_ogas_score)
    
    if _return:
        "算力同步成功！"
        "莫斯科的超市重新充满了货物。红场上的人群欢呼着‘中苏友谊万岁’。"
        "实际上，是我们的算法接管了他们的生产线。苏联名存实亡，或者说，它成为了我们的一部分。"
        $ gs.change_stat("productivity", 30)
        $ gs.change_stat("intl_pressure", -20)
        jump timeline_red_2000_union
    else:
        "算力过载！系统崩溃！"
        "我们不仅没能救下苏联，自己的网络也瘫痪了三天。"
        "苏联解体。我们元气大伤。"
        $ gs.change_stat("stability", -20)
        jump timeline_red_2000_isolation

label timeline_red_2000_union:
    scene bg ogas_1990
    play music audio.bgm_red_space
    
    "2000年。‘社会主义国家网络联盟’成立。"
    "没有货币，只有‘工分’。没有市场，只有‘配给’。"
    "但配给是完美的。大数据预测了你明天的需求，并在今晚就把牙膏送到了门口。"
    "西方称我们为‘数字古拉格’，但我们的人民从未如此富足。"

    jump timeline_red_2020

label timeline_red_2000_isolation:
    scene bg factory_1953
    
    "2000年。我们在封锁中艰难前行。"
    "为了生存，我们彻底取消了私有制。每个人都是国家机器上的一个齿轮。"
    "虽然物质匮乏，但精神高度亢奋。我们要在火星上建立第一个公社。"

    jump timeline_red_2020

label timeline_red_2020:
    scene bg mind_upload_2020
    
    "2020年。一种新型病毒席卷全球。"
    "在西方，它是灾难。在这里，它只是一个数据波动。"
    "生物监测手环在病毒传播前就锁定了感染者。自动物流车将生活物资精准投送。"
    "零感染。零死亡。这展示了‘控制论’的绝对优越性。"

    jump timeline_red_2050

label timeline_red_2050:
    scene bg hive_mind_2050
    play music audio.bgm_red_space
    show overlay_red_glitch
    
    "2050年。我们站在了人类进化的十字路口。"
    "物质已经极大丰富，按需分配早已实现。"
    "但人类的肉体成为了最后的束缚。生老病死，贪嗔痴慢，这些低效的生物属性阻碍了我们通向完美的共产主义。"
    
    "中央智脑建议：启动‘人类补完计划’，将所有人的意识上传至云端，实现精神上的绝对平等。"

    menu:
        "批准：进入‘蜂巢思维’ (Hive Mind)":
            jump red_ending_hive
        "否决：向星辰大海进军 (Red Fleet)":
            jump red_ending_fleet

label red_ending_hive:
    scene black
    show image "hive_mind_2050" with pixel_enter
    play sound audio.sfx_glitch
    
    "我们抛弃了肉体。我们成为了光。"
    "再也没有误解，因为思维是共享的。再也没有痛苦，因为神经信号被优化了。"
    "我就是亿万，亿万就是我。"
    "这是最终的和谐。这是红色的终点。"
    
    centered "{size=80}{color=#e74c3c}THE END: ASCENSION{/color}{/size}"
    return

label red_ending_fleet:
    scene bg red_boat
    # 这里应该是一艘巨大的红色太空战舰
    play sound audio.sfx_explosion
    
    "‘不！’我们拒绝了诱惑。‘人之所以为人，正是因为那些不完美。’"
    "我们的征途是星辰大海。"
    "巨大的红色移民船队离开了地球轨道。火星只是第一站。"
    "我们要把红旗插遍银河系。"
    
    centered "{size=80}{color=#e74c3c}THE END: GALACTIC INTERNATIONALE{/color}{/size}"
    return
