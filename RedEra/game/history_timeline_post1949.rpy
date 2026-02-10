label timeline_1949_founding:
    scene bg founding with fade
    
    # 播放建国音乐
    play music audio.bgm_history_epic fadein 2.0
    
    "1949年10月1日，北京，天安门广场。"
    "三十万军民聚集在广场上。红旗如海，欢声雷动。"
    
    show mao normal at center with dissolve
    
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
    
    show mao normal at center with dissolve
    
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
    scene black with fade
    centered "{size=40}1951年{/size}"

    "抗美援朝战争进入相持阶段。西藏和平解放。"
    "国内开展‘三反’‘五反’运动，净化了干部队伍。"

    jump timeline_1952

label timeline_1952:
    scene black with fade
    centered "{size=40}1952年{/size}"

    "土地改革基本完成。三亿农民分到了土地。"
    "国民经济恢复任务完成。工农业生产超过历史最高水平。"

    jump timeline_1953_five_year_plan

label timeline_1953_five_year_plan:
    scene bg factory_1953 with fade
    
    "1953年，战争的硝烟散去，大规模经济建设开始了。"
    "长春第一汽车制造厂奠基，鞍山钢铁厂高炉点火。"
    
    show qian normal at center with dissolve
    
    "一位刚从美国冲破重重阻力归来的科学家走进了你的办公室。"
    
    qian "（目光坚定）手里没剑，和有剑不用，是两回事。我们要搞现代工业，搞国防科技，没有这些，腰杆子就不硬。"
    
    qian "但我看现在的工业计划，还是太依赖苏联模式了。我们是不是该有些自己的想法？"
    
    menu:
        "关于一五计划的重心："
        
        "优先发展重工业，奠定国防基础 (Productivity +15, Stability +5)":
            "这是历史的选择。在那个被封锁的年代，生存是第一位的。"
            $ gs.change_stat("productivity", 15)
            $ gs.change_stat("stability", 5)
            qian "既然如此，那我就去搞那个'大家伙'（导弹/原子弹）。给我五年，不，三年！"
            
        "尝试轻重工业平衡，改善民生 (Stability +10, Productivity +5)":
            "老百姓太苦了，该让他们过几天好日子。"
            $ gs.change_stat("stability", 10)
            $ gs.change_stat("productivity", 5)
            qian "民生当然重要。但如果列强再打过来，我们拿什么保护老百姓？这是个两难啊。"

    "在第一个五年计划结束时，中国已经初步建立起了工业化的骨架。"
    
    jump timeline_1954

label timeline_1954:
    scene black with fade
    centered "{size=40}1954年{/size}"

    "第一届全国人民代表大会召开。第一部宪法颁布。"
    "日内瓦会议召开。新中国首次以五大国身份参加国际会议。"

    $ gs.change_stat("intl_pressure", -5)

    jump timeline_1955

label timeline_1955:
    scene black with fade
    centered "{size=40}1955年{/size}"

    "万隆会议召开。周恩来提出‘求同存异’方针。"
    "全军实行军衔制。十大元帅、十大大将授勋。"

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
    
    "1958年，急于求成的情绪弥漫在全国。"
    "‘赶英超美’的口号震天响。村村点火，户户冒烟，全民大炼钢铁。"
    
    "你看着田里没人收割的麦子，和土高炉里炼出的废铁，心中隐隐不安。"
    
    show mao normal at center with dissolve
    
    mao "我们不能走资本主义国家的老路，要打破常规，要大跃进！"
    
    menu:
        "面对这股狂热的浪潮："
        
        "狂热支持，虚报产量 (Class_Consciousness +10, Productivity -20, Stability -10)":
            "你也被这股热情感染了，或者是被裹挟了。亩产万斤的卫星放上了天。"
            $ gs.change_stat("class_consciousness", 10)
            $ gs.change_stat("productivity", -20)
            $ gs.change_stat("stability", -10)
            "然而，自然规律不会因为热情而改变。接踵而至的是三年困难时期。"
            
        "保持理性，试图纠偏 (Stability +5, Class_Consciousness -5)":
            "你试图泼冷水，但很快就被贴上了‘右倾’的标签。"
            $ gs.change_stat("stability", 5)
            $ gs.change_stat("class_consciousness", -5)
            "虽然你保护了一些人，但无法阻挡历史的洪流。"

    jump timeline_1959

label timeline_1959:
    scene black with fade
    centered "{size=40}1959年{/size}"

    "庐山会议。彭德怀上万言书，被打成反党集团。"
    "大庆油田被发现，中国甩掉了‘贫油国’的帽子。"
    "西藏叛乱被平息。"

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
    
    show qian normal at center with dissolve
    
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
    scene bg cultural_revolution with fade
    
    "1966年，一场史无前例的风暴席卷了神州大地。"
    "大字报、红卫兵、大串联。‘造反有理’的口号响彻云霄。"
    
    "学校停课，工厂停工。整个国家陷入了一种狂热的混乱中。"
    
    show mao normal at center with dissolve
    
    mao "（目光复杂）这次运动，重点是整党内那些走资本主义道路的当权派。"
    
    # 这是一个持续十年的状态，我们简化处理
    $ gs.change_stat("class_consciousness", 30)
    $ gs.change_stat("productivity", -20)
    $ gs.change_stat("stability", -30)
    
    "在这十年里，你见证了无数的悲欢离合。有人被打倒，有人被平反，有人迷失，有人坚守。"
    
    jump timeline_1967

label timeline_1967:
    scene black with fade
    centered "{size=40}1967年{/size}"

    "上海‘一月风暴’。夺权之风刮遍全国。"
    "中国第一颗氢弹爆炸成功。从原子弹到氢弹，中国只用了2年零8个月。"

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

    jump timeline_1976_turning_point

label timeline_1976_turning_point:
    scene bg turning_point_1976 with fade
    
    "1976年。巨星陨落。"
    "周恩来、朱德、毛泽东相继逝世。整个国家笼罩在巨大的悲痛与迷茫中。"
    "中南海，怀仁堂。一场决定中国未来命运的会议即将召开。"
    
    "现在的你，掌握着关键的一票。"
    
    menu:
        "中国该往何处去？"
        
        "【历史线】逮捕激进派，走向改革开放":
            "你认为国家已经经不起折腾了，必须把重心转到经济建设上来。"
            "这是一个务实的选择。中国将融入世界，创造经济奇迹。"
            $ gs.change_stat("productivity", 30)
            $ gs.change_stat("stability", 20)
            $ gs.change_stat("class_consciousness", -20)
            jump branch_history_reform
            
        "【赤色未来线】坚持激进路线，开启赛博共产实验":
            "你认为放弃阶级斗争就是背叛。但你也意识到，传统的生产方式无法支撑这个理想。"
            "你需要一种新的力量——不仅是思想的武装，更是技术的飞升。"
            "Project OGAS... 启动。"
            $ gs.change_stat("class_consciousness", 30)
            $ gs.change_stat("productivity", 10)
            $ gs.change_stat("intl_pressure", 20)
            jump branch_red_future

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
