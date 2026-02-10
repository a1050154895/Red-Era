# game/history_timeline.rpy

# ==========================================
# 历史编年史 (1913-1949)
# ==========================================

label timeline_1913:
    scene black with fade
    centered "{size=40}1913年{/size}"
    
    "3月20日，上海火车站的枪声震惊了全国。宋教仁先生倒在血泊中。"
    "孙中山发动‘二次革命’，但在这个武人当道的年代，缺乏兵权的革命党人迅速溃败。"
    "袁世凯的笑容背后，是一个更黑暗的独裁阴影。"
    
    # 数值影响：社会稳定大幅下降
    $ gs.change_stat("stability", -5)
    
    jump timeline_1914

label timeline_1914:
    scene black with fade
    centered "{size=40}1914年{/size}"

    "1月，袁世凯下令解散国会。中华民国只剩下了一个空壳。"
    "7月，第一次世界大战爆发。列强在欧洲厮杀，暂时放松了对中国的钳制。"
    "民族工业迎来了短暂的‘黄金时代’。纺织厂、面粉厂如雨后春笋般涌现。"

    $ gs.change_stat("productivity", 5)

    jump timeline_1915

label timeline_1915:
    scene black with fade
    centered "{size=40}1915年{/size}"
    
    "为了换取日本的支持，袁世凯签下了丧权辱国的‘二十一条’。"
    "年底，他穿上了龙袍，做起了‘洪宪皇帝’的迷梦。"
    
    "但在上海的法租界，一本名为《青年杂志》的小册子悄然问世。"
    "陈独秀高举‘德先生’与‘赛先生’的大旗，向封建礼教宣战。"
    
    # 之前选了教育救国，这里会有额外文本
    if gs.class_consciousness > 15:
        "你在新文化运动中积极奔走，你的文章激励了无数青年。"
        $ gs.change_stat("class_consciousness", 5)
    
    jump timeline_1916

label timeline_1916:
    scene black with fade
    centered "{size=40}1916年{/size}"
    
    "做了83天皇帝梦的袁世凯在唾骂声中死去。"
    "但他留下的不是和平，而是分裂。北洋军裂变为直、皖、奉三系，中国进入了长达十余年的军阀混战。"
    
    $ gs.change_stat("stability", -10)
    $ gs.change_stat("intl_pressure", 5)
    
    jump timeline_1917

label timeline_1917:
    scene black with fade
    centered "{size=40}1917年{/size}"
    
    "张勋复辟的闹剧像一场滑稽戏，但也彻底撕碎了民国最后的遮羞布。"
    "但在遥远的北方，俄国爆发了十月革命。阿芙乐尔号巡洋舰的炮声，穿越西伯利亚的寒风，传到了中国。"
    
    jump timeline_1918

label timeline_1918:
    scene black with fade
    centered "{size=40}1918年{/size}"

    "11月，一战结束。北京城里欢呼‘公理战胜强权’。"
    "李大钊在《新青年》上发表《庶民的胜利》，预言‘试看将来的环球，必是赤旗的世界’。"

    $ gs.change_stat("class_consciousness", 5)

    jump event_1919_may_fourth

label event_1919_may_fourth:
    # --------------------------------------
    # 重点闪回：1919 五四运动
    # --------------------------------------
    scene bg may_fourth with fade # 使用新背景
    
    centered "{size=50}1919年 5月4日{/size}\n{size=30}北京{/size}"

    # 身份赋予
    "现在的你，是北京大学‘新潮社’的一名学生。手里紧攥着那面写着‘还我青岛’的白布旗帜。"
    
    "巴黎和会上，中国作为战胜国，山东权益却被转让给日本。"
    "外交失败的消息传回国内，积压了七年的怒火终于爆发了。"
    
    "天安门前，三千多名学生振臂高呼：‘外争主权，内除国贼！’"
    "赵家楼的火光，照亮了整个北京城。"

    show lu normal at left with moveinleft
    
    lu "（站在人群边缘，目光深邃）看到了吗？这就是沉默中爆发的力量。这不仅仅是学生的愤怒，这是民族的觉醒。"
    
    menu:
        "你身处游行的队伍中，你决定："
        
        "冲在最前线，火烧赵家楼 (阶级觉悟 +10, 国际压力 +5)":
            $ gs.change_stat("class_consciousness", 10)
            $ gs.change_stat("intl_pressure", 5)
            "你举起火把，点燃了曹汝霖的住宅。那一刻，你感到了前所未有的释放。"
            lu "这把火烧得好！烧掉这腐朽的旧房子！"
            
        "组织工人罢工，扩大运动声势 (生产力 -5, 阶级觉悟 +15)":
            $ gs.change_stat("productivity", -5)
            $ gs.change_stat("class_consciousness", 15)
            "你意识到光靠学生是不够的。你转身走向长辛店，走向工厂，动员工人阶级加入战斗。"
            lu "你比我看得远。工人...那是更深沉的地火。"

    jump timeline_1920

label timeline_1920:
    scene black with fade
    centered "{size=40}1920年{/size}"

    "陈独秀在上海组建马克思主义研究会。各地共产主义小组如星火般点燃。"
    "在法国勤工俭学的留学生中，周恩来、邓小平等年轻人也开始接受马克思主义。"

    jump timeline_1921

label timeline_1921:
    scene black with fade
    centered "{size=40}1921年{/size}"
    
    "7月，上海法租界望志路106号。几位书生悄悄聚在一起。"
    "因为巡捕的搜查，他们转移到了嘉兴南湖的一艘画舫上。"
    "就在这艘小船上，一个名为‘中国共产党’的幽灵诞生了。"
    
    # 这是一个关键的历史锚点
    "你隐约感觉到，历史的齿轮开始加速转动了。"
    
    $ gs.change_stat("class_consciousness", 10)
    
    jump timeline_1922

label timeline_1922:
    scene black with fade
    centered "{size=40}1922年{/size}"

    "年初，香港海员大罢工爆发，持续56天，最终取得胜利。"
    "7月，中共二大在上海召开，明确提出了反帝反封建的民主革命纲领。"

    $ gs.change_stat("class_consciousness", 5)

    jump timeline_1923

label timeline_1923:
    scene black with fade
    centered "{size=40}1923年{/size}"

    "2月，京汉铁路工人大罢工遭到吴佩孚的血腥镇压。‘二七惨案’震惊中外。"
    "血的教训让共产党人认识到，单靠工人阶级的赤手空拳是不够的，必须寻找盟友。"
    
    $ gs.change_stat("stability", -5)

    jump timeline_1924

label timeline_1924:
    scene black with fade
    centered "{size=40}1924年{/size}"
    
    "国民党一大召开，确立‘联俄、联共、扶助农工’三大政策。"
    "在广州黄埔岛上，一所军校拔地而起。门口贴着一副对联：‘升官发财请往他处，贪生怕死勿入斯门’。"
    
    jump timeline_1925

label timeline_1925:
    scene black with fade
    centered "{size=40}1925年{/size}"
    
    "3月12日，孙中山先生在北京逝世。‘革命尚未成功，同志仍须努力’成了他的遗言。"
    "5月30日，上海爆发‘五卅惨案’，反帝浪潮席卷全国。"
    
    jump timeline_1926

label timeline_1926:
    scene black with fade
    centered "{size=40}1926年{/size}"
    
    "7月9日，国民革命军在广州誓师北伐。叶挺独立团作为先锋，一路势如破竹。"
    "吴佩孚、孙传芳的主力被接连击溃。革命的浪潮似乎势不可挡。"
    "但在胜利的欢呼声中，你看到了阴影在滋长。那个叫蒋介石的总司令，眼神越发阴沉。"
    
    jump chapter_1_shanghai

# 注意：1927年剧情在 script.rpy 的 chapter_1_shanghai 中处理
# 这里需要定义 1927 之后的跳转接口

label timeline_1927_aftermath:
    scene black with fade
    centered "{size=40}1927年 下半年{/size}"
    
    "大革命失败了。白色恐怖笼罩着中国。"
    "但在绝望中，有人在南昌打响了第一枪，有人在秋收时节举起了暴动的旗帜。"
    
    jump timeline_1928

label timeline_1928:
    scene bg jinggangshan with fade
    centered "{size=40}1928年{/size}"
    
    "井冈山的翠竹依旧青翠。毛泽东在这里点燃了‘工农武装割据’的星星之火。"
    "‘朱毛会师’，红四军成立。"
    
    show mao normal at center with pixel_enter
    
    mao "敌人只能砍下我们的头颅，决不能动摇我们的信仰！因为我们信仰的主义，乃是宇宙的真理！"
    
    menu:
        "面对围剿，红军的战略是？"
        
        "敌进我退，敌驻我扰 (生产力 -5, 阶级觉悟 +10)":
             $ gs.change_stat("class_consciousness", 10)
             "游击战术初显神威。红军在运动中消灭敌人，壮大自己。"
             
        "分兵把守，寸土不让 (稳定 -10, 生产力 -10)":
             $ gs.change_stat("stability", -10)
             "分兵导致被各个击破。这是惨痛的教训。"
             
    jump timeline_1931

label timeline_1931:
    scene black with fade
    centered "{size=40}1931年{/size}"
    
    "9月18日，沈阳。日军炸毁南满铁路，炮轰北大营。"
    "‘九一八事变’爆发。东北沦陷。"
    
    play sound audio.sfx_explosion
    show layer master at screen_shake
    
    "南京政府下令‘绝对不抵抗’。数千万同胞沦为亡国奴。"
    
    $ gs.change_stat("intl_pressure", 20)
    $ gs.change_stat("stability", -15)
    
    jump timeline_1934

label timeline_1934:
    scene bg long_march with fade
    centered "{size=40}1934年{/size}"
    
    "第五次反围剿失败。红军被迫进行战略转移。"
    "这是一次前所未有的远征。湘江之战，血染湘江。"
    
    # 街机互动：长征抉择
    show qte_mash_button at center
    "（这里是生与死的考验！保持信念！）"
    $ renpy.pause(1.0, hard=True)
    hide qte_mash_button
    
    jump timeline_1935

label timeline_1935:
    scene black with fade
    centered "{size=40}1935年{/size}"
    
    "遵义会议。历史在这一刻转弯。"
    "确立了毛泽东在党和红军中的领导地位。挽救了党，挽救了红军，挽救了中国革命。"
    
    $ gs.change_stat("class_consciousness", 20)
    $ gs.change_stat("stability", 10)
    
    jump timeline_1937

label timeline_1937:
    scene bg yanan with fade
    centered "{size=40}1937年{/size}"
    
    "7月7日，卢沟桥事变。全面抗战爆发。"
    "延安成为了全国进步青年的圣地。"
    
    show mao normal at center
    mao "中国人民站起来了！这一次，我们绝不退缩！"
    
    jump timeline_1945

label timeline_1945:
    scene bg chongqing with fade
    centered "{size=40}1945年{/size}"
    
    "日本投降。举国欢腾。"
    "但在重庆，一场鸿门宴正在上演。"
    
    show mao normal at left
    show chiang uniform at right
    
    "毛泽东飞赴重庆谈判。为了和平，为了民主。"
    
    chiang "（面带微笑，眼神冰冷）润之啊，这天下还是得有一个主义，一个领袖才行。"
    
    jump timeline_1949

    
    "四一二的血迹未干，七一五政变接踵而至。国共合作彻底破裂。"
    "但在黑暗中，枪声再次响起。"
    "8月1日南昌城头的枪声，9月湘赣边界的秋收起义..."
    "起义军最终汇聚到了罗霄山脉的中段——井冈山。"
    
    jump timeline_1928

label timeline_1928:
    scene bg jinggangshan with fade
    centered "{size=40}1928年{/size}"

    "4月，朱毛会师。中国工农红军第四军成立。"
    "‘敌进我退，敌驻我扰，敌疲我打，敌退我追’。游击战的十六字诀在山林间回响。"
    "与此同时，皇姑屯的一声巨响，张作霖被日本人炸死。东北易帜。"

    $ gs.change_stat("stability", 5)

    jump timeline_1929

label timeline_1929:
    scene black with fade
    centered "{size=40}1929年{/size}"

    "12月，古田会议召开。确立了‘思想建党，政治建军’的原则。"
    "红军不再是单纯的武装力量，而是执行政治任务的武装集团。"

    $ gs.change_stat("class_consciousness", 10)

    jump timeline_1930

label timeline_1930:
    scene black with fade
    centered "{size=40}1930年{/size}"

    "中原大战爆发。蒋介石与冯玉祥、阎锡山混战，死伤枕藉。"
    "红军利用国民党内战的机会，迅速壮大，粉碎了第一次反围剿。"

    jump timeline_1931

label timeline_1931:
    scene bg jinggangshan with fade
    centered "{size=40}1931年{/size}"
    
    "11月7日，中华苏维埃共和国在瑞金成立。"
    "但在遥远的东北，‘九一八’事变的炮声震碎了沈阳的夜空。"
    "蒋介石却坚持‘攘外必先安内’，百万大军向苏区围剿而来。"
    
    $ gs.change_stat("intl_pressure", 20)
    
    jump timeline_1932

label timeline_1932:
    scene black with fade
    centered "{size=40}1932年{/size}"

    "1月28日，日军进攻上海，‘一·二八’事变爆发。十九路军奋起抵抗。"
    "3月，伪满洲国成立。溥仪再次坐上了傀儡的龙椅。"

    $ gs.change_stat("intl_pressure", 10)

    jump timeline_1933

label timeline_1933:
    scene black with fade
    centered "{size=40}1933年{/size}"

    "长城抗战。喜峰口的大刀队砍出了中国军人的血性。"
    "但在南方，第五次反围剿开始了。这次，敌人采用了‘堡垒主义’，步步为营。"

    jump timeline_1934

label timeline_1934:
    scene bg long_march with fade
    centered "{size=40}1934年{/size}"
    
    "第五次反围剿失败。红军被迫撤离中央苏区，开始战略转移。"
    "这是一条用鲜血铺成的路。湘江之战，血染湘江，红军从8万锐减到3万。"
    
    "现在的你，是一名红军团长，正带着残部在贵州的崇山峻岭中穿行。"
    
    show mao normal at center with dissolve
    
    "在通道会议上，那个操着湖南口音的高个子站了出来。"
    mao "不能再往那个口袋里钻了！我们要转兵贵州！"
    
    menu:
        "面对路线性命攸关的抉择，你支持："
        
        "坚决支持毛泽东，转兵贵州 (社会稳定 +10)":
            $ gs.change_stat("stability", 10)
            "你拍案而起：‘老子听毛委员的！往敌人力量薄弱的地方打！’"
            "这一决定，挽救了红军，挽救了革命。"
            
        "犹豫不决，等待中央命令 (社会稳定 -10)":
            $ gs.change_stat("stability", -10)
            "你有些犹豫，但历史的车轮没有等你。好在大多数人选择了正确的道路。"
            
    jump timeline_1935

label timeline_1935:
    scene black with fade
    centered "{size=40}1935年{/size}"

    "遵义会议后，红军四渡赤水，巧渡金沙江，跳出了敌人的包围圈。"
    "飞夺泸定桥，翻越雪山草地。10月，中央红军到达陕北。"
    "‘一二·九’运动在北平爆发，学生高呼‘华北之大，已经安放不下一张平静的书桌了！’"

    $ gs.change_stat("stability", 10)

    jump timeline_1936

label timeline_1936:
    scene black with fade
    centered "{size=40}1936年{/size}"

    "10月，红军三大主力会师。长征结束。"
    "12月12日，西安事变爆发。张学良、杨虎城兵谏蒋介石。"
    "经过多方斡旋，蒋介石被迫接受‘停止内战，联共抗日’。"

    $ gs.change_stat("intl_pressure", -5)
    $ gs.change_stat("stability", 10)

    jump timeline_1937

label timeline_1937:
    scene bg yanan with fade
    centered "{size=40}1937年{/size}"
    
    "七七事变爆发，全面抗战开始。"
    "红军改编为八路军、新四军，开赴抗日前线。"
    "延安，宝塔山下，成为了无数爱国青年心中的圣地。"
    
    jump timeline_1938

label timeline_1938:
    scene black with fade
    centered "{size=40}1938年{/size}"

    "台儿庄大捷，打破了日军不可战胜的神话。"
    "但在正面战场，武汉、广州相继失守。抗战进入相持阶段。"
    "毛泽东发表《论持久战》，指明了抗战的道路。"

    $ gs.change_stat("class_consciousness", 5)

    jump timeline_1939

label timeline_1939:
    scene black with fade
    centered "{size=40}1939年{/size}"

    "日军开始对重庆进行无差别轰炸。"
    "在敌后，八路军、新四军建立了广大的抗日根据地。"
    "白求恩大夫牺牲在抗日前线。"

    jump timeline_1940

label timeline_1940:
    scene black with fade
    centered "{size=40}1940年{/size}"

    "百团大战爆发。彭德怀指挥八路军破袭正太铁路，给日军以沉重打击。"
    "汪精卫在南京成立伪国民政府，彻底沦为汉奸。"

    jump timeline_1941

label timeline_1941:
    scene black with fade
    centered "{size=40}1941年{/size}"

    "皖南事变。国民党顽固派袭击新四军，‘千古奇冤，江南一叶’。"
    "12月，太平洋战争爆发。中国抗战成为了世界反法西斯战争的重要组成部分。"

    $ gs.change_stat("intl_pressure", -10)

    jump timeline_1942

label timeline_1942:
    scene black with fade
    centered "{size=40}1942年{/size}"

    "河南大饥荒。数百万灾民流离失所。"
    "中国远征军入缅作战，戴安澜将军壮烈殉国。"
    "延安整风运动开始。"

    $ gs.change_stat("stability", -10)
    $ gs.change_stat("class_consciousness", 10)

    jump timeline_1943

label timeline_1943:
    scene black with fade
    centered "{size=40}1943年{/size}"

    "中美英三国发表《开罗宣言》，规定日本窃取的中国领土归还中国。"
    "敌后战场开始局部反攻。"

    jump timeline_1944

label timeline_1944:
    scene black with fade
    centered "{size=40}1944年{/size}"

    "日军发动豫湘桂战役，国民党军队大溃败。"
    "与之形成鲜明对比的是，敌后抗日根据地不断扩大。"

    jump timeline_1945

label timeline_1945:
    scene bg chongqing with fade
    centered "{size=40}1945年{/size}"
    
    "八年浴血，终于迎来了日本投降。"
    "但和平的曙光转瞬即逝。蒋介石三封电报邀请毛泽东赴重庆谈判。"
    
    "现在的你，是负责保卫工作的警卫员。看着毛泽东戴上盔式帽，登上了飞往重庆的飞机。"
    
    show mao normal at left
    show chiang uniform at right
    
    "双十协定签了，但你知道，这不过是暴风雨前的宁静。"
    
    jump timeline_1946

label timeline_1946:
    scene black with fade
    centered "{size=40}1946年{/size}"

    "6月，蒋介石撕毁停战协定，全面内战爆发。"
    "国民党军队向中原解放区发动进攻。毛泽东提出‘一切反动派都是纸老虎’。"

    $ gs.change_stat("stability", -20)

    jump timeline_1947

label timeline_1947:
    scene black with fade
    centered "{size=40}1947年{/size}"

    "国民党重点进攻陕北和山东。中共中央撤离延安，转战陕北。"
    "刘邓大军千里跃进大别山，揭开了战略反攻的序幕。"
    "国统区爆发‘反饥饿、反内战、反迫害’运动。"

    jump timeline_1948

label timeline_1948:
    scene black with fade
    centered "{size=40}1948年{/size}"

    "决战的时刻到了。"
    "东北、华北、中原，三大战场上战云密布。"
    "你是最高的决策者之一。面前的地图上，红蓝两色的箭头犬牙交错。"

    menu:
        "这是一个决定中国未来一百年命运的时刻："

        "发动三大战役，毕其功于一役 (进入历史/赤色线)":
            "宜将剩勇追穷寇，不可沽名学霸王。"
            "9月，辽沈战役开始。关门打狗，解放东北全境。"
            "11月，淮海战役、平津战役相继打响。国民党主力基本被消灭。"
            "蒋经国在上海‘打老虎’失败，国民经济彻底崩溃。"
            $ gs.change_stat("productivity", -20)
            jump timeline_1949

        "接受‘划江而治’方案，保留革命火种 (进入蓝线)":
            "考虑到国际形势的复杂和避免生灵涂炭，你选择了妥协。"
            "斯大林发来电报建议‘不可再进’。"
            "虽然这可能是一个巨大的战略错误，但历史在这里拐了一个弯。"
            jump timeline_blue_1949


label timeline_1949:
    scene bg founding with fade
    centered "{size=40}1949年{/size}"
    
    "三大战役，百万雄师过大江。"
    "蒋家王朝土崩瓦解，败退台湾。"
    
    # 跳转到建国篇
    jump timeline_1949_founding
