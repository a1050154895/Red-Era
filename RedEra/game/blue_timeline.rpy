# ==========================================
# 蓝线：财阀赛博 (1949 - 2050)
# ==========================================

label timeline_blue_1949:
    scene bg shanghai_rain_night with fade
    play music audio.bgm_history_tension fadein 2.0
    centered "{size=40}1949年{/size}"

    "就在解放军准备渡江之时，国际形势突变。"
    "美国直接军事介入，第七舰队封锁长江。"
    "在巨大的军事压力和内部妥协派的推动下，‘划江而治’成为了现实。"
    "中华民国政府在南京稳住了阵脚。"

    $ gs.change_stat("stability", -20)
    $ gs.change_stat("intl_pressure", -20) # 获得美国支持

    jump timeline_blue_1950

label timeline_blue_1950:
    scene bg shanghai_rain_night with fade
    centered "{size=40}1950年{/size}"

    "大规模的‘清党’在南方展开。无数共产党人和进步人士倒在血泊中。"
    "蒋介石宣布‘动员戡乱’常态化，实行高压军管。"
    "美国大批经援到来，作为交换，美国资本全面控制了关键产业。"

    jump timeline_blue_1951

label timeline_blue_1951:
    scene bg korean_war with fade
    centered "{size=40}1951年{/size}"

    "朝鲜战争爆发。国军精锐被派往朝鲜战场，作为美军的‘协从军’。"
    "这是投名状，也是绞肉机。"

    jump timeline_blue_1952

label timeline_blue_1952:
    scene bg shanghai_rain_night with fade
    centered "{size=40}1952年{/size}"

    "《中美共同防御条约》升级。美军在南京、上海、广州设立永久基地。"
    "上海开始恢复‘东方巴黎’的奢靡，流浪汉冻死在霓虹灯下。"

    jump timeline_blue_1953

label timeline_blue_1953:
    scene bg factory_1953 with fade
    play music audio.bgm_blue_cyber fadein 2.0
    centered "{size=40}1953年{/size}"

    "朝鲜战争停战。战时工业刺激了经济短暂繁荣。"
    "‘四大家族’利用美援，完成了对金融、交通、能源的绝对垄断。"
    
    show overlay_blue_neon
    "霓虹灯初次点亮了南京路，资本的齿轮开始加速转动。"

    $ gs.change_stat("productivity", 10)
    $ gs.change_stat("class_consciousness", -10)
    hide overlay_blue_neon

    jump timeline_blue_1954

label timeline_blue_1954:
    scene black with fade
    centered "{size=40}1954年{/size}"

    "宪法修改。总统任期限制被取消。"
    "蒋介石成为了事实上的终身独裁者。"

    jump timeline_blue_1955

label timeline_blue_1955:
    scene black with fade
    centered "{size=40}1955年{/size}"

    "土地改革？不，是‘土地兼并’。大庄园经济复辟。"
    "失地农民涌入城市，成为第一代‘贫民窟’居民。"

    jump timeline_blue_1956

label timeline_blue_1956:
    scene black with fade
    centered "{size=40}1956年{/size}"

    "日本经济起飞。国民政府提出‘赶日超美’，依托廉价劳动力发展代工产业。"
    "‘血汗工厂’遍布沿海。"

    jump timeline_blue_1957

label timeline_blue_1957:
    scene black with fade
    centered "{size=40}1957年{/size}"

    "知识分子发起批评运动。随即遭到残酷镇压。"
    "‘美丽岛’监狱人满为患。"

    $ gs.change_stat("stability", -10)

    jump timeline_blue_1958

label timeline_blue_1958:
    scene black with fade
    centered "{size=40}1958年{/size}"

    "金门炮战？不存在的。两岸维持着恐怖的和平。"
    "北方成立了‘中华苏维埃共和国’（北中国），加入了经互会。"

    jump timeline_blue_1959

label timeline_blue_1959:
    scene black with fade
    centered "{size=40}1959年{/size}"

    "西藏叛乱被美国支持的特种部队平息。"
    "达赖喇嘛成为座上宾。"

    jump timeline_blue_1960

label timeline_blue_1960:
    scene black with fade
    centered "{size=40}1960年{/size}"

    "中苏论战。北中国与苏联关系恶化。"
    "南中国趁机在边境制造摩擦，试图‘反攻大陆’，但无果而终。"

    jump timeline_blue_1961

label timeline_blue_1961:
    scene black with fade
    centered "{size=40}1961年{/size}"

    "肯尼迪访华（南京）。确立了‘美中（南）特殊伙伴关系’。"

    jump timeline_blue_1962

label timeline_blue_1962:
    scene black with fade
    centered "{size=40}1962年{/size}"

    "古巴导弹危机。世界处在核战争边缘。"
    "蒋介石秘密研制核武器，代号‘新竹计划’。"

    jump timeline_blue_1963

label timeline_blue_1963:
    scene black with fade
    centered "{size=40}1963年{/size}"

    "经济起飞。GDP年增长率超过10%。"
    "但这背后是极度压榨的劳工权益。"

    jump timeline_blue_1964

label timeline_blue_1964:
    scene bg atomic_bomb with fade
    centered "{size=40}1964年{/size}"

    "北中国原子弹爆炸成功。"
    "南京政府极度恐慌，请求美国部署核武器。"
    play sound audio.sfx_glitch
    show overlay_blue_neon
    "核阴云下的繁荣，显得格外脆弱。"
    hide overlay_blue_neon

    $ gs.change_stat("intl_pressure", 20)

    jump timeline_blue_1965

label timeline_blue_1965:
    scene bg factory_1953 with fade # 继续使用工厂背景代表代工经济
    centered "{size=40}1965年{/size}"

    "美军介入越南战争。南中国成为美军最大的后勤基地和休假地。"
    "色情产业、毒品泛滥。Bar Girl 成为时代的伤痕。"

    jump timeline_blue_1966

label timeline_blue_1966:
    scene bg cultural_revolution with fade
    centered "{size=40}1966年{/size}"

    "北中国爆发‘文化大革命’。"
    "蒋介石发起‘中华文化复兴运动’，实则推行儒家等级观念，禁锢思想。"
    "‘君君臣臣父父子子’，也是‘老板老板员工员工’。"

    jump timeline_blue_1967

label timeline_blue_1967:
    scene black with fade
    centered "{size=40}1967年{/size}"

    "香港暴动。蔓延至广州、上海。"
    "政府出动坦克镇压。"

    jump timeline_blue_1968

label timeline_blue_1968:
    scene black with fade
    centered "{size=40}1968年{/size}"

    "全球左翼运动高潮。南京大学生走上街头，抗议越战和独裁。"
    "特务机构‘警备总部’连夜抓捕千人。"

    jump timeline_blue_1969

label timeline_blue_1969:
    scene black with fade
    centered "{size=40}1969年{/size}"

    "珍宝岛冲突。北中国与苏联开战。"
    "南中国试图联苏制北，但苏联选择了观望。"

    jump timeline_blue_1970

label timeline_blue_1970:
    scene black with fade
    centered "{size=40}1970年{/size}"

    "经济转型。开始发展电子产业和半导体。"
    "未来的‘赛博’基石在此刻奠定。"

    jump timeline_blue_1971

label timeline_blue_1971:
    scene black with fade
    centered "{size=40}1971年{/size}"

    "联合国席位之争。在美国力保下，‘中华民国’勉强保留了席位，但在安理会的一票否决权被削弱。"

    jump timeline_blue_1972

label timeline_blue_1972:
    scene black with fade
    centered "{size=40}1972年{/size}"

    "尼克松访华？不，尼克松访问了北京（北中国），震惊了南京。"
    "美国开始玩弄‘两个中国’的平衡术。"

    jump timeline_blue_1973

label timeline_blue_1973:
    scene black with fade
    centered "{size=40}1973年{/size}"

    "第一次石油危机。南中国经济重创。"
    "政府强推‘十大建设’，进一步加强国家资本主义。"

    jump timeline_blue_1974

label timeline_blue_1974:
    scene black with fade
    centered "{size=40}1974年{/size}"

    "西沙海战。北中国海军击败南越。"
    "南京政府心情复杂：既高兴又失落。"

    jump timeline_blue_1975

label timeline_blue_1975:
    scene black with fade
    centered "{size=40}1975年{/size}"

    "蒋介石去世。全岛（及半壁江山）‘如丧考妣’。"
    "蒋经国接班。开启了‘开明专制’时代。"

    jump timeline_blue_1976

label timeline_blue_1976:
    scene bg turning_point_1976 with fade
    centered "{size=40}1976年{/size}"

    "北中国三巨头去世。文革结束。"
    "南中国这边，蒋经国大力任用技术官僚，经济开始向高科技转型。"
    
    "命运的齿轮在这里分岔。"
    
    jump timeline_blue_1977

label timeline_blue_1977:
    scene black with fade
    centered "{size=40}1977年{/size}"

    "中坜事件。选举舞弊引发抗议。"
    "民主运动的火种开始在地下燃烧。"

    jump timeline_blue_1978

label timeline_blue_1978:
    scene black with fade
    centered "{size=40}1978年{/size}"

    "北中国开始改革开放。"
    "蒋经国感到压力，宣布解除部分戒严，允许‘党外’人士活动。"
    "但这只是为了释放压力的阀门。"

    jump timeline_blue_1979

label timeline_blue_1979:
    scene black with fade
    centered "{size=40}1979年{/size}"

    "美丽岛事件。大规模警民冲突。"
    "随后是对民主人士的再一次大清洗。"
    "蒋经国决定：政治上收紧，经济上彻底放开给财阀。"

    $ gs.change_stat("stability", -10)
    $ gs.change_stat("productivity", 10)

    jump timeline_blue_1980

label timeline_blue_1980:
    scene black with fade
    centered "{size=40}1980年{/size}"

    "设立‘新竹-上海科学园区’。半导体产业开始腾飞。"
    "台积电（TSMC）的前身成立，但由四大家族控股。"

    jump timeline_blue_1981

label timeline_blue_1981:
    scene black with fade
    centered "{size=40}1981年{/size}"

    "陈文成案。旅美教授被警总杀害。"
    "白色恐怖依旧笼罩。"

    jump timeline_blue_1982

label timeline_blue_1982:
    scene black with fade
    centered "{size=40}1982年{/size}"

    "罗大佑发行《之乎者也》。黑色旋风席卷乐坛。"
    "年轻人开始用摇滚表达愤怒。"

    jump timeline_blue_1983

label timeline_blue_1983:
    scene black with fade
    centered "{size=40}1983年{/size}"

    "江南案。情报局派黑帮赴美刺杀异见作家。"
    "美方震怒，蒋家政权信誉破产。"

    $ gs.change_stat("intl_pressure", 20)

    jump timeline_blue_1984

label timeline_blue_1984:
    scene black with fade
    centered "{size=40}1984年{/size}"

    "麦当劳进入中国（南方）。消费主义开始盛行。"
    "‘只要有钱，就没有烦恼’成为社会信条。"

    jump timeline_blue_1985

label timeline_blue_1985:
    scene black with fade
    centered "{size=40}1985年{/size}"

    "十信案爆发。金融丑闻牵连甚广。"
    "但这反而促成了大财阀吞并中小银行，金融寡头成型。"

    jump timeline_blue_1986

label timeline_blue_1986:
    scene black with fade
    centered "{size=40}1986年{/size}"

    "民进党成立。蒋经国默许其存在，作为‘花瓶反对党’。"
    "实际上，议会完全被财阀收买的政客控制。"

    jump timeline_blue_1987

label timeline_blue_1987:
    scene black with fade
    centered "{size=40}1987年{/size}"

    "宣布解除戒严。开放党禁报禁。"
    "表面上的民主来了，但选票是明码标价的。"

    jump timeline_blue_1988

label timeline_blue_1988:
    scene black with fade
    centered "{size=40}1988年{/size}"

    "蒋经国逝世。李登辉继任。"
    "本土财阀势力抬头，与外省权贵合流。"

    jump timeline_blue_1989

label timeline_blue_1989:
    scene bg shenzhen_1992 with fade # 象征繁荣泡沫
    centered "{size=40}1989年{/size}"

    "北方的政治风波。"
    "南中国媒体大肆报道，标榜自己的‘自由繁荣’。"
    "股市狂飙到12000点。全民炒股，泡沫达到顶峰。"
    
    show overlay_blue_neon
    "每个人都觉得自己是股神。"
    hide overlay_blue_neon

    jump timeline_blue_1990

label timeline_blue_1990:
    scene bg shenzhen_1992 with flash
    centered "{size=40}1990年{/size}"

    play sound audio.sfx_explosion # 泡沫破裂
    "股市崩盘。中产阶级财富被洗劫一空。"
    "财阀趁机低价收购资产，贫富差距瞬间拉大。"
    "‘野百合学运’。学生要求解散‘万年国会’。"

    jump timeline_blue_1991

label timeline_blue_1991:
    scene black with fade
    centered "{size=40}1991年{/size}"

    "终止动员戡乱时期。承认北中国为‘政治实体’。"
    "冷战结束。美国调整战略，要求南中国充当‘高科技代工厂’。"

    jump timeline_blue_1992

label timeline_blue_1992:
    scene black with fade
    centered "{size=40}1992年{/size}"

    "辜汪会谈。两岸经贸往来加速。"
    "南中国的资本开始疯狂涌入北方，剥削那里的廉价劳动力。"

    jump timeline_blue_1993

label timeline_blue_1993:
    scene black with fade
    centered "{size=40}1993年{/size}"

    "尹清枫命案。军购弊案揭开了军队腐败的冰山一角。"
    "但这都不重要，只要能保住政权。"

    jump timeline_blue_1994

label timeline_blue_1994:
    scene black with fade
    centered "{size=40}1994年{/size}"

    "省长民选。金钱政治大行其道。"
    "黑道漂白参选，‘黑金政治’成为常态。"

    jump timeline_blue_1995

label timeline_blue_1995:
    scene black with fade
    centered "{size=40}1995年{/size}"

    "台海危机？不，是‘联合演习’。"
    "美军舰队常驻台湾海峡，确保这条‘芯片生命线’的安全。"

    jump timeline_blue_1996

label timeline_blue_1996:
    scene black with fade
    centered "{size=40}1996年{/size}"

    "总统直选。李登辉当选。"
    "这是财阀意志的胜利。大选花费数十亿美元。"

    jump timeline_blue_1997

label timeline_blue_1997:
    scene bg shenzhen_1992 with fade # 借用城市背景
    play music audio.bgm_blue_glitch fadein 1.0
    centered "{size=40}1997年{/size}"

    "亚洲金融风暴。"
    "索罗斯的量子基金横扫东南亚。"
    
    show overlay_blue_neon
    "为了保住汇率，必须动用国家资本。"

    call minigame_corporate_crisis
    
    if corporate_score >= 50:
        "南中国凭借庞大的外汇储备和残酷的内部转嫁，勉强维持了表面繁荣。"
        $ gs.change_stat("stability", 10)
    else:
        "防线崩溃。中小企业倒闭潮，无数人跳楼。"
        $ gs.change_stat("stability", -20)

    hide overlay_blue_neon
    play music audio.bgm_blue_cyber fadein 2.0

    jump timeline_blue_1998

# 定义小游戏 Label
label minigame_corporate_crisis:
    $ corporate_score = 0
    $ target_score = 100
    
    "【系统警告】检测到金融波动。启动市场干预协议。"
    "疯狂点击 [INJECT] 按钮注入流动性！"

    # 显示小游戏屏幕，持续 5 秒
    show screen minigame_corporate(corporate_score, target_score)
    
    # 简单的倒计时模拟
    $ time_left = 5.0
    while time_left > 0:
        $ time_left -= 0.1
        pause 0.1
        # 模拟市场自动下跌
        $ corporate_score -= 1 
        if corporate_score < 0:
            $ corporate_score = 0

    hide screen minigame_corporate
    
    "干预结束。最终评分：[corporate_score]"
    return

label timeline_blue_1998:
    scene black with fade
    centered "{size=40}1998年{/size}"

    "互联网泡沫初现。"
    "‘中华电信’私有化，被两大家族瓜分。"

    jump timeline_blue_1999

label timeline_blue_1999:
    scene black with fade
    centered "{size=40}1999年{/size}"

    "921大地震。暴露出豆腐渣工程。"
    "但这成为了房地产商新一轮圈地的理由。"

    jump timeline_blue_2000

label timeline_blue_2000:
    scene black with fade
    centered "{size=40}2000年{/size}"

    "政党轮替。民进党上台。"
    "但这只是换了一批人从财阀手中领钱。"
    "‘核四’停建又复建，背后是巨大的利益输送。"

    jump timeline_blue_2001

label timeline_blue_2001:
    scene black with fade
    centered "{size=40}2001年{/size}"

    "加入WTO。农业彻底崩溃。"
    "农民被迫卖地，成为城市贫民窟的新成员。"
    "‘九龙城寨’式的巨型贫民窟在上海、广州边缘拔地而起。"

    $ gs.change_stat("productivity", 10)
    $ gs.change_stat("stability", -10)

    jump timeline_blue_2002

label timeline_blue_2002:
    scene black with fade
    centered "{size=40}2002年{/size}"

    "SARS爆发。私立医院拒绝收治穷人。"
    "贫民窟成为重灾区，政府选择封锁而非救治。"

    jump timeline_blue_2003

label timeline_blue_2003:
    scene black with fade
    centered "{size=40}2003年{/size}"

    "房地产狂飙。房价收入比达到50倍。"
    "年轻人只能住在‘棺材房’里，仰望摩天大楼。"

    jump timeline_blue_2004

label timeline_blue_2004:
    scene black with fade
    centered "{size=40}2004年{/size}"

    "319枪击案。大选充满戏剧性。"
    "政治彻底娱乐化，民众对政治冷感。"

    jump timeline_blue_2005

label timeline_blue_2005:
    scene black with fade
    centered "{size=40}2005年{/size}"

    "《公司法》修改。企业权力进一步扩大。"
    "‘企业自治领’出现，大公司内部拥有独立的安保（私军）和法律。"

    jump timeline_blue_2006

label timeline_blue_2006:
    scene black with fade
    centered "{size=40}2006年{/size}"

    "红衫军运动。百万人民反贪腐。"
    "但很快被媒体（财阀控制）分化瓦解。"

    jump timeline_blue_2007

label timeline_blue_2007:
    scene black with fade
    centered "{size=40}2007年{/size}"

    "高铁通车。连接的是几个超级都市圈。"
    "高铁站外就是连绵的棚户区。"

    jump timeline_blue_2008

label timeline_blue_2008:
    scene black with fade
    centered "{size=40}2008年{/size}"

    "全球金融危机。政府宣布‘劫贫济富’计划。"
    "削减福利，降低企业税。失业率飙升。"

    jump timeline_blue_2009

label timeline_blue_2009:
    scene black with fade
    centered "{size=40}2009年{/size}"

    "莫拉克风灾。小林村灭村。"
    "政府救灾迟缓，但在此地规划了新的豪华度假村。"

    jump timeline_blue_2010

label timeline_blue_2010:
    scene black with fade
    centered "{size=40}2010年{/size}"

    "ECFA签署。两岸资本彻底合流。"
    "北方的官僚资本和南方的财阀资本把酒言欢。"

    jump timeline_blue_2011

label timeline_blue_2011:
    scene black with fade
    centered "{size=40}2011年{/size}"

    "塑化剂事件。食品安全崩溃。"
    "有钱人吃特供，穷人吃‘科技与狠活’。"

    jump timeline_blue_2012

label timeline_blue_2012:
    scene bg cyberpunk_2050_blue with fade # 开始进入全面赛博化
    centered "{size=40}2012年{/size}"

    "智能手机普及。人们沉溺于虚拟的快乐中。"
    "算法开始控制人的思想。"
    "Cyberpunk is not coming, it is here."

    jump timeline_blue_2013

label timeline_blue_2013:
    scene black with fade
    centered "{size=40}2013年{/size}"

    "洪仲丘案。25万人上街。"
    "这是最后的公民运动。之后，监控技术让街头运动成为不可能。"

    jump timeline_blue_2014

label timeline_blue_2014:
    scene black with fade
    centered "{size=40}2014年{/size}"

    "太阳花运动？不，被‘企业保安部队’迅速镇压。"
    "学生领袖被收买或消失。"

    jump timeline_blue_2015

label timeline_blue_2015:
    scene black with fade
    centered "{size=40}2015年{/size}"

    "马习会。确认了‘一中各表，共治天下’的默契。"
    "实质是划分势力范围。"

    jump timeline_blue_2016

label timeline_blue_2016:
    scene black with fade
    centered "{size=40}2016年{/size}"

    "民进党再次上台。全面倒向美国和日本。"
    "成为‘印太战略’的忠实棋子。"

    jump timeline_blue_2017

label timeline_blue_2017:
    scene black with fade
    centered "{size=40}2017年{/size}"

    "《劳基法》修恶。‘过劳死’合法化。"
    "人类只是电池。"

    jump timeline_blue_2018

label timeline_blue_2018:
    scene black with fade
    centered "{size=40}2018年{/size}"

    "韩流旋风。民粹主义抬头。"
    "但这只是财阀操弄的又一场真人秀。"

    jump timeline_blue_2019

label timeline_blue_2019:
    scene black with fade
    centered "{size=40}2019年{/size}"

    "同婚合法化。政府用这种‘进步’来掩盖阶级矛盾。"
    "‘粉红清洗’（Pinkwashing）。"

    jump timeline_blue_2020

label timeline_blue_2020:
    scene bg pandemic_2020 with fade
    centered "{size=40}2020年{/size}"

    "全球大流行。但南中国的‘生物科技’产业借此大发横财。"
    "‘健康码’成为了永久性的电子镣铐。"
    
    show overlay_blue_neon
    play sound audio.sfx_glitch
    "警告：您的健康码已变红。请立即前往最近的‘再教育隔离中心’。"
    hide overlay_blue_neon

    $ gs.change_stat("stability", -20)
    $ gs.change_stat("productivity", 10)

    jump timeline_blue_2021

label timeline_blue_2021:
    scene black with fade
    centered "{size=40}2021年{/size}"

    "元宇宙元年。穷人住笼屋，但在元宇宙里住豪宅。"
    "‘奶头乐’（Tittytainment）战略大获成功。"

    jump timeline_blue_2022

label timeline_blue_2022:
    scene black with fade
    centered "{size=40}2022年{/size}"

    "佩洛西访华（南京）。引发第四次台海危机。"
    "但双方都知道打不起来，股票照炒，舞照跳。"

    jump timeline_blue_2023

label timeline_blue_2023:
    scene black with fade
    centered "{size=40}2023年{/size}"

    "生成式AI彻底爆发。所有的媒体内容——新闻、娱乐、社交——90%由AI生成。"
    "‘真实’不再重要，重要的是‘流量’。"
    "人们活在为你量身定制的信息茧房里，至死方休。"

    jump timeline_blue_2024

label timeline_blue_2024:
    scene black with fade
    centered "{size=40}2024年{/size}"

    "大选年。候选人们不再亲自演讲，而是使用完美的Deepfake替身。"
    "竞选承诺由算法根据民调实时生成。"
    "民主？那只是一个每四年运行一次的 legacy 程序。"

    jump timeline_blue_2025

label timeline_blue_2025:
    scene bg cyberpunk_neon with fade
    centered "{size=40}2025年{/size}"

    "《企业主权法》通过。大型跨国公司在领地内拥有完全的司法权和征税权。"
    "政府名存实亡，变成了企业的‘物业管理处’。"

    $ gs.change_stat("class_consciousness", -20)
    $ gs.change_stat("productivity", 20)

    jump timeline_blue_2030

label timeline_blue_2030:
    scene black with fade
    centered "{size=40}2030年{/size}"
    play music audio.bgm_blue_glitch fadein 2.0

    "大筛选（The Great Filter）开始。通用人工智能取代了80%的白领工作。"
    "‘无用阶级’（The Useless Class）诞生。他们聚集在超级城市的底层，靠廉价的合成食物和虚拟现实游戏度日。"

    play sfx audio.sfx_rain fadein 2.0
    "窗外，酸雨终日不绝。"

    jump timeline_blue_2035

label timeline_blue_2035:
    scene bg cyberpunk_neon
    show overlay_blue_neon
    centered "{size=40}2035年{/size}"

    "底层暴动频发。由于没有工作，罢工失去了意义。"
    "董事会决定进行‘市场维稳’。"

    # 开启企业操纵小游戏
    $ corporate_score = 0
    $ target_corporate_score = 50
    call screen minigame_corporate(corporate_score, target_corporate_score)

    if corporate_score >= target_corporate_score:
        "通过精准的‘电子毒品’投放和债务免除，暴动被平息了。"
        $ gs.change_stat("stability", 10)
    else:
        "镇压部队出动。鲜血染红了霓虹灯。"
        $ gs.change_stat("stability", -20)
        play sfx audio.sfx_explosion

    jump timeline_blue_2040

label timeline_blue_2040:
    scene black with fade
    centered "{size=40}2040年{/size}"

    "‘霓虹瘟疫’（Neon Plague）。一种针对人体植入义体的计算机-生物混合病毒爆发。"
    "没钱更新防火墙的人，大脑直接被烧毁。"
    
    play sfx audio.sfx_glitch
    show overlay_blue_neon
    "整个城市在尖叫，但那是电子信号的尖叫。"

    jump timeline_blue_2045

label timeline_blue_2045:
    scene black with fade
    centered "{size=40}2045年{/size}"

    "‘涅槃计划’（Project Nirvana）公布。意识上传技术成熟。"
    "这是通往永生的门票，售价：所有资产 + 灵魂。"
    "富人开始抛弃衰老的肉体，进入云端服务器。"

    jump timeline_blue_2050

label timeline_blue_2050:
    scene bg cyberpunk_2050_blue with fade
    play music audio.bgm_blue_cyber
    centered "{size=60}2050年{/size}"

    "欢迎来到新世界。"
    "地面上，是一座巨大的、自动运转的机器坟墓。贫民像老鼠一样在废墟中苟延残喘。"
    "天空中，巨大的服务器悬浮城闪耀着神圣的蓝光。"
    
    "那些上传了意识的‘新人类’，在虚拟天堂中享受着永恒的极乐。"
    "而你，看着自己锈迹斑斑的机械手臂，不知道自己是否还算是一个‘人’。"

    menu:
        "仰望天空城 (Accept Fate)":
            "你跪倒在泥泞中，向着那遥不可及的光芒膜拜。"
            "系统提示：信仰充值成功。"
            jump blue_ending_submission

        "拔掉连接线 (Rebel)":
            play sfx audio.sfx_glitch
            "你扯断了后颈的神经连接线。剧痛让你清醒。"
            "即使是地狱，我也要用自己的眼睛去看。"
            jump blue_ending_rebellion

label blue_ending_submission:
    scene black
    "【结局：赛博格的梦】"
    "你成为了庞大机器的一颗螺丝钉，在虚拟的幻梦中度过了余生。"
    return

label blue_ending_rebellion:
    scene black
    "【结局：断网者】"
    "你死在了阴暗的巷子里。但在最后一刻，你是自由的。"
    return
    
    show overlay_blue_neon
    "Citizen ID: [gs.productivity * 1984]"
    "Social Credit: [gs.stability]"
    
    jump timeline_blue_end_final

label timeline_blue_end_final:
    scene black
    centered "{size=60}BLUE ENDING: THE CORPORATE STATE{/size}"
    "历史在这里终结，或者说，被私有化了。"
    return


    "第一位AI CEO掌管了最大的财阀集团。"
    "它计算出，裁掉90%的人类员工能使利润最大化。"
    "于是，大清洗开始了。不是政治清洗，是‘优化’。"

    jump timeline_blue_2049

label timeline_blue_2049:
    scene black with fade
    centered "{size=40}2049年{/size}"

    "建国百年（中华民国）。"
    "但这面旗帜已经没有意义。真正的统治者是高悬在摩天大楼上的霓虹Logo。"
    "总统只是一个全息投影吉祥物。"

    jump timeline_blue_2050_v2

label timeline_blue_2050_v2:

    scene bg cyberpunk_2050_blue with fade
    
    "2050年。蓝线终局。"
    
    "欢迎来到夜之城...或者说是南京/上海/台北的混合体。"
    "高科技，低生活。赛博朋克的预言完全实现了。"
    
    "你站在摩天大楼的顶端，俯瞰着下面如蝼蚁般的人群和璀璨的霓虹。"
    "如果你有钱，这里是天堂。如果你没钱，这里是地狱。"
    
    if gs.productivity > 80:
        "虽然残酷，但这里的技术确实登峰造极。人类文明以另一种扭曲的方式延续着。"
        "结局达成：【霓虹神话 / 公司殖民地】"
    else:
        "整个社会濒临崩溃。在无尽的享乐与堕落中，文明正在走向寂静的死亡。"
        "结局达成：【这类梦的终结】"
        
    jump credits
