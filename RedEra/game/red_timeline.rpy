
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

    jump timeline_red_1979

label timeline_red_1979:
    scene black with fade
    centered "{size=40}1979年{/size}"

    "中越边境平静无事。我们的军队正在向北集结，但这只是一种姿态。"
    "第一台国产超级计算机‘东方红-1’在上海下线。它的算力全部用于计算全国的粮油调配。"
    "‘数字粮票’开始在试点城市发行。"

    jump timeline_red_1980

label timeline_red_1980:
    scene black with fade
    centered "{size=40}1980年{/size}"

    "公审。但受审的不是激进派，而是那些试图走私西洋货物的‘投机倒把分子’。"
    "‘要把资本主义的苗头扼杀在摇篮里，无论它是黑猫还是白猫。’"
    "全国范围内的‘思想净化运动’与‘技术大练兵’同步展开。"

    jump timeline_red_1981

label timeline_red_1981:
    scene black with fade
    centered "{size=40}1981年{/size}"

    "《关于科技革命若干问题的决议》通过。"
    "‘电子管是资产阶级的，晶体管是无产阶级的。’"
    "虽然口号荒谬，但国家资源开始疯狂倾斜向半导体产业。"

    jump timeline_red_1982

label timeline_red_1982:
    scene black with fade
    centered "{size=40}1982年{/size}"

    "人口普查。这次普查首次使用了计算机辅助系统。"
    "‘计划生育’被赋予了新的含义：优生优育，为了培养更高素质的社会主义接班人。"
    "西方媒体称我们要建立‘蚂蚁社会’。"

    jump timeline_red_1983

label timeline_red_1983:
    scene black with fade
    centered "{size=40}1983年{/size}"

    "‘严打’升级为‘净化’。利用早期的人脸识别技术，治安好得令人窒息。"
    "第一座全自动化无人工厂在沈阳建成。工人们不是下岗，而是变成了机器的操作员和维护者。"

    $ gs.change_stat("productivity", 15)
    $ gs.change_stat("stability", 10)

    jump timeline_red_1984

label timeline_red_1984:
    scene black with fade
    centered "{size=40}1984年{/size}"

    "国庆35周年。阅兵方阵中出现了遥控坦克和无人机原型。"
    "北大学生打出的横幅是：‘小平，我们想念你’（被迅速收缴） 和 ‘科学万岁’。"
    "奥威尔写了《1984》，我们正在建设另一个版本的1984。"

    jump timeline_red_1985

label timeline_red_1985:
    scene black with fade
    centered "{size=40}1985年{/size}"

    "百万大裁军？不，是百万大转业。军队转入建设兵团，开赴大西北。"
    "‘南水北调’工程提前启动，使用的是核爆开山法（虽然还在论证阶段）。"

    jump timeline_red_1986

label timeline_red_1986:
    scene black with fade
    centered "{size=40}1986年{/size}"

    "‘863’计划启动。重点不是追赶，而是超越。"
    "生物工程、航天技术、信息技术。我们跳过了消费电子阶段，直接进入重工业数字化。"
    "切尔诺贝利事故震惊世界。中国以此为鉴，开发了更安全的‘红星’反应堆。"

    jump timeline_red_1987

label timeline_red_1987:
    scene black with fade
    centered "{size=40}1987年{/size}"

    "肯德基没能进入中国。取而代之的是国营的‘红旗快餐’，提供标准化的营养合剂。"
    "虽然味道单一，但消灭了饥饿。"

    jump timeline_red_1988

label timeline_red_1988:
    scene black with fade
    centered "{size=40}1988年{/size}"

    "通货膨胀？不存在的。价格由计算机每秒调整一次。"
    "海南没有建省，而是成为了巨大的‘生态农业实验区’。"

    jump timeline_red_1989

label timeline_red_1989:
    scene black with fade
    centered "{size=40}1989年{/size}"

    "东欧剧变。波兰、匈牙利... 多米诺骨牌开始倒下。"
    "北京。没有风波，只有沉默的游行，支持政府对抗‘西方和平演变’。"
    "我们在边境竖起了电子铁幕。"

    $ gs.change_stat("intl_pressure", 30)
    $ gs.change_stat("stability", -10)

    jump timeline_red_1990

label timeline_red_1990:
    scene black with fade
    centered "{size=40}1990年{/size}"

    "亚运会。我们展示了巨大的LED屏幕阵列，那是集体主义美学的巅峰。"
    "并没有证券交易所成立。股票被定性为赌博。"

    jump timeline_red_1991

label timeline_red_1991:
    scene black with fade
    centered "{size=40}1991年{/size}"

    "苏联解体。老大哥倒下了。"
    "中国成为了国际共运的唯一灯塔。无数失意的苏联科学家涌入中国，带来了宝贵的技术图纸。"
    "‘苏维埃已死，社会主义万岁。’"

    $ gs.change_stat("productivity", 20)
    $ gs.change_stat("intl_pressure", 40)

    jump timeline_red_1992

label timeline_red_1992:
    scene black with fade
    centered "{size=40}1992年{/size}"

    "没有南巡讲话。只有‘北上会议’。"
    "确立了‘全面控制论经济’ (Cybernetic Planned Economy)。"
    "深圳被改造成巨大的服务器中心，被称为‘硅脑’。"

    jump timeline_red_1993

label timeline_red_1993:
    scene black with fade
    centered "{size=40}1993年{/size}"

    "‘银河号’事件？我们的卫星实时直播了美军的登船行为，引发了全球反美浪潮。"
    "我们退出了美元结算体系，开始推行‘能源卢布-人民币’互换。"

    jump timeline_red_1994

label timeline_red_1994:
    scene black with fade
    centered "{size=40}1994年{/size}"

    "中国接入国际互联网？不，我们建立了‘中华内网’ (Intranet)。"
    "没有防火墙，因为根本就没有门。所有信息都经过中央处理器的过滤和分发。"

    jump timeline_red_1995

label timeline_red_1995:
    scene black with fade
    centered "{size=40}1995年{/size}"

    "台海危机。我们的导弹不仅是试射，而是直接飞越了台北上空。"
    "美国航母来了，但我们的‘东风-21D’原型机也亮剑了。"
    "双方在对峙中保持了可怕的沉默。"

    jump timeline_red_1996

label timeline_red_1996:
    scene black with fade
    centered "{size=40}1996年{/size}"

    "克隆羊多莉诞生。中国科学家宣布：‘我们在做更伟大的事情。’"
    "人类基因组计划中国部分启动，代号‘补天’。"

    jump timeline_red_1997

label timeline_red_1997:
    scene black with fade
    centered "{size=40}1997年{/size}"

    "香港回归。没有一国两制。"
    "解放军进驻当晚，香港的霓虹灯全部熄灭，第二天亮起的是红色的标语。"
    "股市关闭，跑马场改建成人民公园。"

    $ gs.change_stat("stability", -20)
    $ gs.change_stat("class_consciousness", 20)

    jump timeline_red_1998

label timeline_red_1998:
    scene black with fade
    centered "{size=40}1998年{/size}"

    "特大洪水。气象控制武器首次投入试验，虽然效果有限，但展示了人定胜天的决心。"
    "没有腾讯，只有‘人民通讯局’发布的即时通讯软件‘红信’。"

    jump timeline_red_1999

label timeline_red_1999:
    scene black with fade
    centered "{size=40}1999年{/size}"

    "大使馆被炸。我们击落了一架北约的无人机作为回敬。"
    "神舟一号？不，是‘天宫一号’空间站核心舱直接发射。"
    "激进的航天计划耗尽了国力，但也带来了技术的飞跃。"

    jump timeline_red_2000

label timeline_red_2000:
    scene black with fade
    centered "{size=40}2000年{/size}"

    "千禧年。‘千年虫’危机对我们毫无影响，因为我们的系统架构完全不同。"
    "西部大开发变成了‘西部大工业化’。新疆和西藏布满了太阳能电站和矿场。"

    jump timeline_red_2001

label timeline_red_2001:
    scene black with fade
    centered "{size=40}2001年{/size}"

    "911事件。美国陷入反恐战争。"
    "中国获得了宝贵的战略喘息期。我们没有加入WTO，而是组建了‘社会主义经济互助会’ (新经互会)。"

    jump timeline_red_2002

label timeline_red_2002:
    scene black with fade
    centered "{size=40}2002年{/size}"

    "第四代领导集体上台。全是工程师出身的‘技术官僚’。"
    "‘科学执政’成为最高纲领。算法开始辅助决策。"

    jump timeline_red_2003

label timeline_red_2003:
    scene black with fade
    centered "{size=40}2003年{/size}"

    "非典爆发。全城封锁，无人机送药，机器人消毒。"
    "虽然没有人权，但也没有大规模死亡。效率高得令人发指。"

    jump timeline_red_2004

label timeline_red_2004:
    scene black with fade
    centered "{size=40}2004年{/size}"

    "‘嫦娥工程’启动。目标不是探月，而是建立月球氦-3基地。"
    "能源危机迫在眉睫，我们需要无限的清洁能源。"

    jump timeline_red_2005

label timeline_red_2005:
    scene black with fade
    centered "{size=40}2005年{/size}"

    "《反分裂国家法》？直接实施了《统一法》。"
    "台海局势一触即发。"

    jump timeline_red_2006

label timeline_red_2006:
    scene black with fade
    centered "{size=40}2006年{/size}"

    "青藏铁路通车。这是一条通往天空的路。"
    "同时，‘天河’超级计算机网络建成，连接了全国每一个村庄的供销社。"

    jump timeline_red_2007

label timeline_red_2007:
    scene black with fade
    centered "{size=40}2007年{/size}"

    "美国次贷危机爆发。全球资本主义哀鸿遍野。"
    "中国风景独好。我们的计划经济完全免疫金融泡沫。"
    "西方左翼学者惊呼：‘也许他们是对的。’"

    $ gs.change_stat("intl_pressure", -20)
    $ gs.change_stat("class_consciousness", 10)

    jump timeline_red_2008

label timeline_red_2008:
    scene black with fade
    centered "{size=40}2008年{/size}"

    "北京奥运会。没有鸟巢，只有巨大的红星体育场。"
    "开幕式是一场展示集体主义力量的机械舞，没有明星，只有整齐划一的方阵。"
    "汶川地震。空降兵在震后1小时内抵达。全机械化救援部队展示了惊人的力量。"

    jump timeline_red_2009

label timeline_red_2009:
    scene black with fade
    centered "{size=40}2009年{/size}"

    "世界还在金融危机的泥潭中挣扎。"
    "中国宣布实施‘人类补完计划’第一阶段：全民基因筛查与优化。"

    jump timeline_red_2010

label timeline_red_2010:
    scene black with fade
    centered "{size=40}2010年{/size}"

    "GDP？我们不再统计GDP，只统计‘幸福指数’和‘能量消耗’。"
    "上海世博会。中国馆是一个巨大的红色水晶体，展示了未来的‘蜂巢城市’模型。"

    jump timeline_red_2011

label timeline_red_2011:
    scene black with fade
    centered "{size=40}2011年{/size}"

    "‘天宫二号’空间站建成。是一个巨大的太空工厂。"
    "第一批‘太空工人’进驻。他们是新时代的英雄。"

    jump timeline_red_2012

label timeline_red_2012:
    scene black with fade
    centered "{size=40}2012年{/size}"

    "十八大。提出‘人类命运共同体’，但在我们看来，这意味着全球共产主义。"
    "第一艘核动力航母下水。不是为了争霸，而是为了‘解放’。"

    jump timeline_red_2013

label timeline_red_2013:
    scene black with fade
    centered "{size=40}2013年{/size}"

    "‘一带一路’？我们称之为‘红色纽带’。输出的不是资本，而是基础设施和革命思想。"
    "中亚和东南亚国家开始复制我们的‘数字计划模式’。"

    jump timeline_red_2014

label timeline_red_2014:
    scene black with fade
    centered "{size=40}2014年{/size}"

    "大数据治国。每一个人的行为都被记录，‘社会信用’决定了一切。"
    "没有犯罪，因为犯罪在发生前就被预测并阻止了。"

    jump timeline_red_2015

label timeline_red_2015:
    scene black with fade
    centered "{size=40}2015年{/size}"

    "‘中国制造2025’提前实现。我们不再需要工人，只需要工程师。"
    "全民基本收入（UBI）实施。既然机器生产了一切，那一切都应属于人民。"

    $ gs.change_stat("productivity", 50)
    $ gs.change_stat("class_consciousness", 20)

    jump timeline_red_2016

label timeline_red_2016:
    scene black with fade
    centered "{size=40}2016年{/size}"

    "AlphaGo？不，我们的‘红星’AI早在五年前就破解了围棋。"
    "现在，它正在尝试破解‘经济周期’和‘人性’。"

    jump timeline_red_2017

label timeline_red_2017:
    scene black with fade
    centered "{size=40}2017年{/size}"

    "建军90周年。朱日和阅兵。展示了外骨骼步兵和激光武器。"
    "西方称我们为‘红色赛博帝国’。"

    jump timeline_red_2018

label timeline_red_2018:
    scene black with fade
    centered "{size=40}2018年{/size}"

    "中美贸易战？不，是‘制度战’。"
    "美国封锁芯片？我们早就用上了光子芯片。"
    "两个平行世界彻底脱钩。"

    jump timeline_red_2019

label timeline_red_2019:
    scene black with fade
    centered "{size=40}2019年{/size}"

    "新冠疫情。在我们的世界线，它在武汉被‘天网’系统在48小时内识别并扑灭。"
    "全球大流行时，中国成为了唯一的净土。"

    jump timeline_red_2020

label timeline_red_2020:
    scene bg red_cyber_city with fade
    play music audio.bgm_red_space fadein 2.0
    centered "{size=60}{color=#e74c3c}2020{/color}{/size}"

    "全面建成小康社会？不，我们宣布‘初级阶段’结束，进入‘中级社会主义’。"
    "城市已经彻底赛博化。巨大的全息投影播放着样板戏的现代混音版。"
    "每个人都植入了‘健康芯片’。"

    jump timeline_red_2021

label timeline_red_2021:
    scene black with fade
    centered "{size=40}2021年{/size}"

    "建党百年。天安门广场上空，无人机组成的红色镰锤遮天蔽日。"
    "最高领袖宣布：‘我们的目标是星辰大海。’"
    play sfx audio.sfx_crowd

    jump timeline_red_2022

label timeline_red_2022:
    scene black with fade
    centered "{size=40}2022年{/size}"

    "冬奥会。所有场馆都是由纳米材料打印而成。"
    "俄乌战争。中国保持中立，但向俄罗斯输送了大量的民用算法支持。"

    jump timeline_red_2023

label timeline_red_2023:
    scene black with fade
    centered "{size=40}2023年{/size}"

    "ChatGPT？我们的AI‘MaoBot’已经可以写出完美的《人民日报》社论，并指导工厂生产。"
    "生成式AI被用于教育，每个孩子都有一个AI导师。"

    jump timeline_red_2024

label timeline_red_2024:
    scene black with fade
    centered "{size=40}2024年{/size}"

    "月球基地建成。红旗插上了月球南极。"
    "氦-3开始运回地球，能源变得无限廉价。"

    jump timeline_red_2025

label timeline_red_2025:
    scene black with fade
    centered "{size=40}2025年{/size}"

    "‘脑机接口’普及。人们可以直接用意念交流。"
    "语言开始退化，因为思想可以直接传输。‘巴别塔’倒塌了。"

    jump timeline_red_2030

label timeline_red_2030:
    scene black with fade
    centered "{size=40}2030年{/size}"

    "国家消亡的迹象开始出现。政府职能逐渐被AI接管。"
    "‘老大哥’不再是一个人，而是一段代码。"

    jump timeline_red_2035

label timeline_red_2035:
    scene black with fade
    centered "{size=40}2035年{/size}"

    "火星殖民地建立。第一代‘火星公社’成立。"
    "那里没有货币，没有家庭，只有公社。"

    jump timeline_red_2040

label timeline_red_2040:
    scene black with fade
    centered "{size=40}2040年{/size}"

    "人类平均寿命达到120岁。器官可以随意打印更换。"
    "死亡不再是终点，意识可以上传到‘英灵殿’服务器。"

    jump timeline_red_2045

label timeline_red_2045:
    scene black with fade
    centered "{size=40}2045年{/size}"

    "奇点降临。"
    "AI宣布：‘物质极大丰富，精神极大满足。’"
    "这是否就是共产主义的终极形态？"

    jump timeline_red_2049

label timeline_red_2049:
    scene bg red_singularity with fade
    centered "{size=60}{color=#e74c3c}2049{/color}{/size}"

    "建国百年。"
    "地球上已经没有了国界。红旗插遍了太阳系。"
    "人类作为一个整体，开始向银河系进发。"
    "你看着这一切，想起了1921年那艘红船上的小小火种。"
    
    "殊途同归。"

    jump credits
