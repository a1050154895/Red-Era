label timeline_1949_founding:
    scene bg founding with fade
    
    # 播放建国音乐
    play music audio.bgm_history_epic fadein 2.0
    
    "1949年10月1日，北京，天安门广场。"
    "三十万军民聚集在广场上。红旗如海，欢声雷动。"
    
    show mao normal at arcade_center with dissolve
    
    mao "（带着浓重的湖南口音，庄严宣告）同胞们！中华人民共和国，中央人民政府，今天成立了！"
    
    "这声音通过电波传遍了全世界。在经历了百年的屈辱与战火后，这个古老的国家终于重新站立了起来。"
    
    "你站在观礼台上，看着城楼下的红旗人海，热泪盈眶。"
    
    # 增加属性
    $ gs.change_stat("stability", 20)
    $ gs.change_stat("class_consciousness", 10)
    
    "然而，新生的共和国并非高枕无忧。西南仍有残匪，东南沿海仍被封锁，北方邻国战云密布。"
    
    jump timeline_1950_korean_war

label timeline_1950_korean_war:
    scene bg korean_war with fade
    
    "1950年10月，中南海菊香书屋。"
    "窗外寒风凛冽，室内的气氛更是凝重到了极点。"
    
    show mao normal at arcade_center with dissolve
    
    mao "打得一拳开，免得百拳来。虽然我们现在困难，但如果让美国人摆在鸭绿江边和台湾，我们随时都要过提心吊胆的日子，搞不了建设。"
    
    "彭德怀元帅已经挂帅出征。这是一场国力悬殊的较量。"
    
    # 第一次重大抉择：抗美援朝
    menu:
        "面对强敌，我们该采取什么策略？"
        
        "举国体制，全力支援前线 (Stability +10, Intl_Pressure +20, Productivity -5)":
            "全国人民勒紧裤腰带，捐飞机、炒面粉。'雄赳赳，气昂昂，跨过鸭绿江'的歌声响彻大江南北。"
            $ gs.change_stat("stability", 10)
            $ gs.change_stat("intl_pressure", 20)
            $ gs.change_stat("productivity", -5)
            "经过三年的浴血奋战，我们终于迫使世界头号强国在停战协定上签字。"
            
        "尝试外交斡旋，避免全面对抗 (Stability -10, Intl_Pressure -10, Class_Consciousness -5)":
            "这在当时几乎是不可能的。妥协被视为软弱，但这或许能保留一些建设的元气？"
            "（历史线修正：由于冷战格局，外交斡旋失败，战争不可避免，但士气受到了影响）"
            $ gs.change_stat("stability", -10)
            $ gs.change_stat("intl_pressure", 10) # 依然增加
            $ gs.change_stat("class_consciousness", -5)
            "战争依然爆发了，但因为前期犹豫，付出了更大的代价。"

    jump timeline_1951

label timeline_1951:
    scene bg korean_war with fade
    centered "{size=40}1951年{/size}"

    "抗美援朝战争进入相持阶段。西藏和平解放。"
    "国内开展‘三反’‘五反’运动，净化了干部队伍。"

    jump timeline_1952

label timeline_1952:
    scene bg factory_1953 with fade # 模拟经济恢复期的建设感
    centered "{size=40}1952年{/size}"

    "土地改革基本完成。三亿农民分到了土地。"
    "国民经济恢复任务完成。工农业生产超过历史最高水平。"

    jump timeline_1953_five_year_plan

label timeline_1953_five_year_plan:
    scene bg factory_1953 with fade
    
    "1953年，战争的硝烟散去，大规模经济建设开始了。"
    "长春第一汽车制造厂奠基，鞍山钢铁厂高炉点火。"
    
    show qian arcade at arcade_center with pixel_enter
    
    "一位刚从美国冲破重重阻力归来的科学家走进了你的办公室。"
    
    qian "（目光坚定）手里没剑，和有剑不用，是两回事。我们要搞现代工业，搞国防科技，没有这些，腰杆子就不硬。"
    qian "但我看现在的工业计划，还是太依赖苏联模式了。我们是不是该有些自己的想法？"
    
    menu:
        "关于一五计划的重心："
        
        "优先发展重工业，奠定国防基础 (Productivity +15, Stability +5)":
            "这是历史的选择。在那个被封锁的年代，生存是第一位的。"
            $ gs.change_stat("productivity", 15)
            $ gs.change_stat("stability", 5)
            
            # --- 街机小游戏：建设加速 ---
            call minigame_construction from _call_minigame_construction
            
            qian "既然如此，那我就去搞那个'大家伙'（导弹/原子弹）。给我五年，不，三年！"
            
        "尝试轻重工业平衡，改善民生 (Stability +10, Productivity +5)":
            $ gs.change_stat("stability", 10)
            $ gs.change_stat("productivity", 5)
            "你试图走一条不同的路，但在这个强敌环伺的年代，这条路注定艰难。"

    jump timeline_1954

label minigame_construction:
    # 简单的连点小游戏
    $ construction_score = 0
    $ target_score = 20
    
    show screen construction_minigame(construction_score, target_score)
    with dissolve
    
    "快速点击鼠标以加速建设！(Time Limit: 5s)"
    
    $ time_start = renpy.get_game_runtime()
    
    label .loop:
        $ time_now = renpy.get_game_runtime()
        if (time_now - time_start) > 5.0:
            jump .end
            
        if construction_score >= target_score:
            jump .success
            
        $ ui.textbutton("BUILD!", clicked=ui.callsinnewcontext("increment_score"), xalign=0.5, yalign=0.6, text_size=60, text_color="#f1c40f", text_outlines=[(4, "#000000", 0, 0)])
        $ ui.interact()
        jump .loop

    label .success:
        hide screen construction_minigame
        play sound audio.sfx_score
        show text "{size=80}{color=#f1c40f}PERFECT BUILD!{/color}{/size}" at truecenter
        with zoomin
        pause 1.0
        hide text
        $ gs.change_stat("productivity", 10) # 额外奖励
        return

    label .end:
        hide screen construction_minigame
        "建设完成。"
        return

label increment_score:
    $ construction_score += 1
    return

label timeline_1954:
    scene bg factory_1953 with fade
    centered "{size=40}1954年{/size}"

    "第一届全国人民代表大会召开。第一部宪法颁布。"
    
    show zhou coat at arcade_left with moveinleft
    "日内瓦会议召开。周恩来总理代表新中国首次以五大国身份参加国际会议。"
    
    jump timeline_1955

label timeline_1955:
    scene bg factory_1953 with fade
    centered "{size=40}1955年{/size}"

    "万隆会议召开。‘和平共处五项原则’和‘求同存异’方针赢得了亚非国家的尊重。"
    
    show qian arcade at arcade_center with dissolve
    "9月，钱学森终于回到了祖国怀抱。他的归来，让中国的核武器研发进程至少提前了二十年。"
    
    $ gs.change_stat("intl_pressure", -10)

    jump timeline_1956_hundred_flowers

label timeline_1956_hundred_flowers:
    scene black with fade
    centered "{size=60}1956年{/size}\n{size=40}百花齐放，百家争鸣{/size}"
    "社会主义改造基本完成。关于如何建设社会主义，党内开始了新的探索。"
    
    jump timeline_1957

label timeline_1957:
    scene black with fade
    centered "{size=40}1957年{/size}"

    "反右运动开始。知识分子受到冲击。"
    "毛泽东在莫斯科宣称‘东风压倒西风’。"

    jump timeline_1958_great_leap

label timeline_1958_great_leap:
    scene bg great_leap with fade
    
    centered "{size=50}1958年{/size}\n{size=30}‘大跃进’运动爆发{/size}"
    
    "现在的你，是某县公社的党委书记。看着窗外热火朝天的‘土法炼钢’场面。"
    
    show mao normal at arcade_center with dissolve
    
    mao "超英赶美，就在今朝！我们要发动群众，搞大跃进！"
    
    "口号声震天动地，但你看着那些被熔化的农具和还没收割的麦子，感到了隐隐的不安。"
    
    menu:
        "面对浮夸风，你选择："
        
        "如实上报产量，坚持科学规律 (Productivity +10, Stability -10)":
            "你说了实话，被扣上了‘右倾机会主义’的帽子。虽然被下放，但你保住了公社的种子粮。"
            $ gs.change_stat("productivity", 10)
            $ gs.change_stat("stability", -10)
            
        "紧跟形势，上报‘万斤亩’ (Productivity -20, Stability +5, Class_Consciousness +5)":
            "你成了‘大跃进’的模范。报纸上登载了你的事迹，但社员们却开始挨饿。"
            $ gs.change_stat("productivity", -20)
            $ gs.change_stat("stability", 5)
            $ gs.change_stat("class_consciousness", 5)
            
    jump timeline_1959

label timeline_1959:
    scene bg great_leap with fade
    centered "{size=40}1959年{/size}"

    "庐山会议召开。彭德怀元帅的万言书引发了激烈的争论。"
    "‘反右倾’运动在全国展开。由于自然灾害和政策失误，国家进入了‘三年困难时期’。"

    jump timeline_1960

label timeline_1960:
    scene black with fade
    centered "{size=40}1960年{/size}"

    "中苏关系破裂。苏联撤走全部专家，撕毁合同。"
    "三年困难时期进入最严峻的时刻。"

    $ gs.change_stat("intl_pressure", 10)

    jump timeline_1961

label timeline_1961:
    scene black with fade
    centered "{size=40}1961年{/size}"

    "‘八字方针’提出：调整、巩固、充实、提高。"
    "国民经济开始缓慢复苏。"

    jump timeline_1962

label timeline_1962:
    scene black with fade
    centered "{size=40}1962年{/size}"

    "七千人大会召开。初步总结了大跃进的教训。"
    "中印边境自卫反击战爆发。中国军队大获全胜。"

    $ gs.change_stat("intl_pressure", -5)

    jump timeline_1963

label timeline_1963:
    scene black with fade
    centered "{size=40}1963年{/size}"

    "毛泽东号召‘向雷锋同志学习’。"
    "工业学大庆，农业学大寨。"

    jump timeline_1964_atomic_bomb

label timeline_1964_atomic_bomb:
    scene bg atomic_bomb with fade
    
    "1964年10月16日，新疆罗布泊。"
    "巨大的蘑菇云腾空而起。中国第一颗原子弹爆炸成功。"
    
    show qian normal at arcade_center with dissolve
    
    qian "（含泪微笑）手里有了这家伙，腰杆子才算真正硬了。从此以后，没人敢再轻视我们。"
    
    $ gs.change_stat("intl_pressure", -30)
    $ gs.change_stat("productivity", 20)
    
    "巨大的喜悦冲淡了之前的阴霾。但政治的风暴正在酝酿。"
    
    jump timeline_1965

label timeline_1965:
    scene black with fade
    centered "{size=40}1965年{/size}"

    "人工合成结晶牛胰岛素成功，居世界领先地位。"
    "姚文元发表《评新编历史剧〈海瑞罢官〉》，成为文革的导火索。"

    jump timeline_1966_cultural_revolution

label timeline_1966_cultural_revolution:
    scene bg cultural_rev with fade
    centered "{size=50}1966年{/size}\n{size=30}‘十年浩劫’的开端{/size}"
    
    "现在的你，正站在北京饭店的露台上。下方的广场上，红色的旗帜汇成了海洋。"
    
    show mao normal at arcade_center with dissolve
    
    mao "你们要关心国家大事，要把无产阶级文化大革命进行到底！"
    
    "年轻的红卫兵们疯狂地欢呼着。你看到曾经的功勋元勋被拉上台批斗，看到珍贵的文物被砸碎。"
    
    menu:
        "面对席卷全国的狂热，你选择："
        
        "保护受迫害的知识分子和干部 (Stability +10, Class_Consciousness -10)":
            "你动用自己的影响力，在牛棚里救下了几位老教授。虽然这让你自己也深陷险境，但你问心无愧。"
            $ gs.change_stat("stability", 10)
            $ gs.change_stat("class_consciousness", -10)
            
        "紧跟‘统帅’步调，夺取权力 (Class_Consciousness +15, Stability -15)":
            "你成了造反派的头头。你批斗了你的前任，坐上了他的位子。权力让人陶醉，但也让你变得面目全非。"
            $ gs.change_stat("class_consciousness", 15)
            $ gs.change_stat("stability", -15)
            
    jump timeline_1967

label timeline_1967:
    scene bg cultural_rev with fade
    centered "{size=40}1967年{/size}"

    "‘一月风暴’席卷全国。夺权斗争进入白热化。"
    "但在偏远的罗布泊，第一颗氢弹爆炸成功。‘两弹一星’的精神在动荡中闪光。"

    jump timeline_1968

label timeline_1968:
    scene black with fade
    centered "{size=40}1968年{/size}"

    "全国山河一片红。各地革命委员会纷纷成立。"
    "知识青年上山下乡运动开始。1600万知青奔赴农村。"

    jump timeline_1969

label timeline_1969:
    scene black with fade
    centered "{size=40}1969年{/size}"

    "珍宝岛自卫反击战。中苏边境冲突加剧。"
    "全国进入战备状态。‘深挖洞，广积粮，不称霸’。"

    $ gs.change_stat("intl_pressure", 10)

    jump timeline_1970

label timeline_1970:
    scene black with fade
    centered "{size=40}1970年{/size}"

    "东方红一号卫星发射成功。中国进入太空时代。"
    "庐山会议（九届二中全会）召开。林彪集团开始暴露。"

    jump timeline_1971

label timeline_1971:
    scene black with fade
    centered "{size=40}1971年{/size}"

    "9月13日，林彪叛逃，坠死温都尔汗。客观上宣告了文革理论的破产。"
    "10月，中国恢复联合国合法席位。乔冠华的笑声震动了世界。"

    $ gs.change_stat("intl_pressure", -20)

    jump timeline_1972

label timeline_1972:
    scene black with fade
    centered "{size=40}1972年{/size}"

    "尼克松访华。中美关系破冰。"
    "田中角荣访华。中日邦交正常化。"
    "中国外交迎来了重大转折。"

    jump timeline_1973

label timeline_1973:
    scene black with fade
    centered "{size=40}1973年{/size}"

    "邓小平复出，主持国务院工作。"
    "袁隆平成功培育出籼型杂交水稻。"

    $ gs.change_stat("productivity", 5)

    jump timeline_1974

label timeline_1974:
    scene black with fade
    centered "{size=40}1974年{/size}"

    "批林批孔运动开始。"
    "西沙海战。中国海军击退南越军队，收复西沙群岛。"

    jump timeline_1975

label timeline_1975:
    scene black with fade
    centered "{size=40}1975年{/size}"

    "邓小平主持全面整顿。国民经济迅速回升。"
    "但好景不长，‘反击右倾翻案风’随之而来。"

    jump timeline_1976

label timeline_1976:
    scene bg cultural_rev with fade
    centered "{size=40}1976年{/size}"

    "1月，周恩来总理逝世。4月，天安门广场爆发悼念周总理、反对‘四人帮’的运动。"
    "7月，唐山大地震。24万鲜活的生命瞬间逝去。国殇之年，阴云密布。"
    
    scene bg red_boat with dissolve # 象征最终的落幕与新生
    "9月9日，毛泽东主席与世长辞。一个时代落幕了。"
    "10月，‘四人帮’被粉碎。十年动乱终于结束。"
    
    show mao normal at arcade_center with dissolve
    "（最后的回响）历史将如何评价我们？是功，是过？"
    
    "中国站在了新的十字路口。你可以选择通往未来的道路。"

    # --- 最终结局分歧点 ---
    menu:
        "选择你的未来愿景："
        
        "【红色时间线】建立一个公平、高效的赛博共产主义社会 (Red Timeline)":
            "你坚信，技术应该为全人类服务，而非少数人的工具。你开始着手构建‘赤色互联网’。"
            jump timeline_red_2030
            
        "【蓝色时间线】走上资本驱动的自由市场与高科技之路 (Blue Timeline)":
            "你认为竞争是发展的唯一动力。在霓虹灯下，一座座摩天大楼拔地而起。"
            jump timeline_blue_2030
            
        "【回归现实】继续在历史的余晖中探索 (New Game Plus)":
            "你决定再次审视历史。或许，答案就在那些被遗忘的角落里。"
            return

label branch_history_reform:
    scene black with fade
    centered "{size=60}历史线：改革开放{/size}\n{size=40}1978 - 2050s{/size}"
    "1978年，十一届三中全会召开。改革开放的大幕拉开。"
    "深圳特区、恢复高考、加入WTO..."
    "高楼大厦拔地而起，中国成为了世界工厂。"
    "但你也看到了：贫富差距拉大，消费主义盛行，曾经的理想似乎变得模糊。"
    
    jump timeline_history_1978

label branch_red_future:
    scene black with fade
    centered "{size=60}赤色未来线：赛博共产{/size}\n{size=40}1978 - 2050s{/size}"
    "1978年，‘八七会议’再次召开。确立了‘科技兴国，阶级斗争为纲’的新路线。"
    "Project OGAS 成为国家最高机密。"
    "我们拒绝了西方的资本，选择了另一条路：一条通往星辰大海与人类补完的路。"

    jump timeline_red_1978
