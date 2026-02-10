# game/future_timeline.rpy

# ==========================================
# 历史线：改革开放 (1978 - 2050)
# ==========================================
label timeline_history_1978:
    scene black with fade
    play music audio.bgm_history_epic fadein 2.0
    centered "{size=40}1978年{/size}"

    "12月，十一届三中全会召开。改革开放的大幕拉开。"
    "‘实践是检验真理的唯一标准’。"
    "安徽小岗村的18个手印，拉开了农村改革的序幕。"

    $ gs.change_stat("productivity", 10)

    jump timeline_history_1979

label timeline_history_1979:
    scene black with fade
    centered "{size=40}1979年{/size}"

    "中美正式建交。"
    "深圳特区成立，‘杀出一条血路来’。"
    "对越自卫反击战爆发。"

    jump timeline_history_1980

label timeline_history_1980:
    scene black with fade
    centered "{size=40}1980年{/size}"

    "审判林彪、江青反革命集团。"
    "实行计划生育政策。"
    "‘万元户’开始出现，人们的欲望被唤醒。"

    jump timeline_history_1981

label timeline_history_1981:
    scene black with fade
    centered "{size=40}1981年{/size}"

    "《关于建国以来党的若干历史问题的决议》通过。科学评价了毛泽东的历史地位。"
    "女排首次夺得世界杯冠军，‘女排精神’激励了一代人。"

    $ gs.change_stat("stability", 5)

    jump timeline_history_1982

label timeline_history_1982:
    scene black with fade
    centered "{size=40}1982年{/size}"

    "中共十二大召开，提出‘建设有中国特色的社会主义’。"
    "人口普查显示，中国人口超过10亿。"

    jump timeline_history_1983

label timeline_history_1983:
    scene black with fade
    centered "{size=40}1983年{/size}"

    "‘严打’开始。社会治安迅速好转。"
    "央视第一届春节联欢晚会播出。"

    jump timeline_history_1984

label timeline_history_1984:
    scene black with fade
    centered "{size=40}1984年{/size}"

    "国庆35周年阅兵。北大学生打出‘小平您好’的横幅。"
    "中英签署关于香港问题的联合声明。"
    "城市经济体制改革全面展开。"

    $ gs.change_stat("productivity", 10)

    jump timeline_history_1985

label timeline_history_1985:
    scene black with fade
    centered "{size=40}1985年{/size}"

    "百万大裁军。"
    "科技体制改革开始。"

    jump timeline_history_1986

label timeline_history_1986:
    scene black with fade
    centered "{size=40}1986年{/size}"

    "‘863’计划启动。中国高技术研究发展计划。"
    "摇滚乐《一无所有》在北京唱响。"

    jump timeline_history_1987

label timeline_history_1987:
    scene black with fade
    centered "{size=40}1987年{/size}"

    "中共十三大召开，阐述了社会主义初级阶段理论。"
    "肯德基在北京前门开出中国第一家店。"

    jump timeline_history_1988

label timeline_history_1988:
    scene black with fade
    centered "{size=40}1988年{/size}"

    "‘价格闯关’失败，引发抢购风潮。"
    "海南建省。"

    $ gs.change_stat("stability", -10)

    jump timeline_history_1989

label timeline_history_1989:
    scene black with fade
    centered "{size=40}1989年{/size}"

    "政治风波。春夏之交的动荡。"
    "江泽民当选中共中央总书记。"

    $ gs.change_stat("stability", -20)
    $ gs.change_stat("intl_pressure", 20)

    jump timeline_history_1990

label timeline_history_1990:
    scene black with fade
    centered "{size=40}1990年{/size}"

    "亚运会在北京举行。‘亚洲雄风’震天响。"
    "上海证券交易所成立。"

    jump timeline_history_1991

label timeline_history_1991:
    scene black with fade
    centered "{size=40}1991年{/size}"

    "苏联解体。冷战结束。"
    "海湾战争爆发，让中国军队看到了现代战争的差距。"

    $ gs.change_stat("intl_pressure", 10)

    jump timeline_history_1992

label timeline_history_1992:
    scene bg shenzhen_1992 with fade
    
    "1992年春，一位老人虽然已经退休，但他依然在南海边画了一个圈。"
    "‘发展才是硬道理’。‘不管黑猫白猫，捉到老鼠就是好猫’。"
    
    "深圳速度震惊了世界。下海经商成为了最时髦的词汇。"
    
    "你看着周围的人，有的成了‘万元户’，有的却在国企改制中下岗。"
    
    $ gs.change_stat("productivity", 20)
    $ gs.change_stat("class_consciousness", -10)
    
    jump timeline_history_1993

label timeline_history_1993:
    scene black with fade
    centered "{size=40}1993年{/size}"

    "建立社会主义市场经济体制。"
    "‘汪辜会谈’。两岸关系迈出重要一步。"
    "银河号事件。弱国无外交的屈辱。"

    $ gs.change_stat("intl_pressure", 10)

    jump timeline_history_1994

label timeline_history_1994:
    scene black with fade
    centered "{size=40}1994年{/size}"

    "中国接入国际互联网。信息时代的大门打开了。"
    "分税制改革开始实施。"

    jump timeline_history_1995

label timeline_history_1995:
    scene black with fade
    centered "{size=40}1995年{/size}"

    "提出‘科教兴国’战略。"
    "台海危机。导弹试射。"

    $ gs.change_stat("intl_pressure", 10)

    jump timeline_history_1996

label timeline_history_1996:
    scene black with fade
    centered "{size=40}1996年{/size}"

    "京九铁路全线通车。"
    "台海演习。美国航母编队介入。"

    jump timeline_history_1997

label timeline_history_1997:
    scene black with fade
    centered "{size=40}1997年{/size}"

    "邓小平逝世。一个时代结束了。"
    "7月1日，香港回归。百年国耻，一朝洗雪。"
    "中共十五大召开。高举邓小平理论伟大旗帜。"

    $ gs.change_stat("stability", 10)

    jump timeline_history_1998

label timeline_history_1998:
    scene black with fade
    centered "{size=40}1998年{/size}"

    "特大洪水。人民子弟兵筑起了血肉长城。"
    "住房制度改革。福利分房时代结束。"
    "腾讯公司成立。"

    jump timeline_history_1999

label timeline_history_1999:
    scene black with fade
    centered "{size=40}1999年{/size}"

    "5月8日，北约轰炸中国驻南联盟大使馆。群情激愤。"
    "12月20日，澳门回归。"
    "神舟一号发射成功。"

    $ gs.change_stat("intl_pressure", 10)

    jump timeline_history_2000

label timeline_history_2000:
    scene black with fade
    centered "{size=40}2000年{/size}"

    "千禧年。世纪之交。"
    "西部大开发战略实施。"
    "江泽民提出‘三个代表’重要思想。"

    jump timeline_history_2001

label timeline_history_2001:
    scene black with fade
    centered "{size=40}2001年{/size}"

    "4月1日，中美南海撞机事件。王伟牺牲。"
    "7月13日，北京申奥成功。‘我们赢了！’"
    "12月11日，中国正式加入WTO。拥抱全球化。"

    $ gs.change_stat("productivity", 20)
    $ gs.change_stat("intl_pressure", -10)

    jump timeline_history_2002

label timeline_history_2002:
    scene black with fade
    centered "{size=40}2002年{/size}"

    "中共十六大召开。胡锦涛当选中共中央总书记。"
    "南水北调工程开工。"

    jump timeline_history_2003

label timeline_history_2003:
    scene black with fade
    centered "{size=40}2003年{/size}"

    "非典疫情爆发。众志成城抗击SARS。"
    "神舟五号载人飞船发射成功。杨利伟成为中国太空第一人。"

    jump timeline_history_2004

label timeline_history_2004:
    scene black with fade
    centered "{size=40}2004年{/size}"

    "雅典奥运会。刘翔夺冠，创造历史。"
    "提出‘构建社会主义和谐社会’。"

    jump timeline_history_2005

label timeline_history_2005:
    scene black with fade
    centered "{size=40}2005年{/size}"

    "《反分裂国家法》通过。"
    "青藏铁路全线贯通。"
    "股权分置改革启动。"

    jump timeline_history_2006

label timeline_history_2006:
    scene black with fade
    centered "{size=40}2006年{/size}"

    "农业税废止。延续两千年的‘皇粮国税’成为历史。"
    "三峡大坝全线建成。"

    jump timeline_history_2007

label timeline_history_2007:
    scene black with fade
    centered "{size=40}2007年{/size}"

    "中共十七大召开。提出科学发展观。"
    "嫦娥一号探月卫星发射成功。"
    "股市大牛市，上证指数突破6000点。"

    jump timeline_history_2008

label timeline_history_2008:
    scene black with fade
    centered "{size=40}2008年{/size}"

    "5月12日，汶川大地震。山河破碎，举国同悲。"
    "8月8日，北京奥运会开幕。同一个世界，同一个梦想。"
    "神舟七号发射成功，翟志刚太空行走。"
    "全球金融危机爆发。中国启动四万亿投资计划。"

    $ gs.change_stat("stability", 10)

    jump timeline_history_2009

label timeline_history_2009:
    scene black with fade
    centered "{size=40}2009年{/size}"

    "建国60周年阅兵。"
    "中国成为世界第一大汽车产销国。"

    jump timeline_history_2010

label timeline_history_2010:
    scene black with fade
    centered "{size=40}2010年{/size}"

    "上海世博会举行。‘城市，让生活更美好’。"
    "中国GDP超过日本，成为世界第二大经济体。"

    $ gs.change_stat("productivity", 10)

    jump timeline_history_2011

label timeline_history_2011:
    scene black with fade
    centered "{size=40}2011年{/size}"

    "天宫一号发射成功。空间站建设迈出关键一步。"
    "利比亚撤侨。国家力量的体现。"

    jump timeline_history_2012

label timeline_history_2012:
    scene black with fade
    centered "{size=40}2012年{/size}"

    "中共十八大召开。习近平当选中共中央总书记。"
    "中国梦提出。实现中华民族伟大复兴。"
    "辽宁舰交接入列。中国有了第一艘航空母舰。"
    "莫言获得诺贝尔文学奖。"

    jump timeline_history_2013

label timeline_history_2013:
    scene black with fade
    centered "{size=40}2013年{/size}"

    "‘一带一路’倡议提出。"
    "嫦娥三号成功登月。"
    "上海自贸区挂牌。"

    jump timeline_history_2014

label timeline_history_2014:
    scene black with fade
    centered "{size=40}2014年{/size}"

    "APEC会议在北京举行。"
    "反腐败斗争深入进行。‘打虎拍蝇’。"

    $ gs.change_stat("stability", 10)

    jump timeline_history_2015

label timeline_history_2015:
    scene black with fade
    centered "{size=40}2015年{/size}"

    "抗战胜利70周年阅兵。裁军30万。"
    "屠呦呦获得诺贝尔生理学或医学奖。"
    "人民币加入SDR。"

    jump timeline_history_2016

label timeline_history_2016:
    scene black with fade
    centered "{size=40}2016年{/size}"

    "G20峰会在杭州举行。"
    "天宫二号发射成功。"
    "‘墨子号’量子卫星发射。"

    jump timeline_history_2017

label timeline_history_2017:
    scene black with fade
    centered "{size=40}2017年{/size}"

    "中共十九大召开。确立习近平新时代中国特色社会主义思想。"
    "国产航母下水。"
    "建军90周年朱日和阅兵。"

    jump timeline_history_2018

label timeline_history_2018:
    scene black with fade
    centered "{size=40}2018年{/size}"

    "改革开放40周年。"
    "港珠澳大桥通车。"
    "中美贸易战爆发。外部环境发生深刻变化。"

    $ gs.change_stat("intl_pressure", 20)

    jump timeline_history_2019

label timeline_history_2019:
    scene black with fade
    centered "{size=40}2019年{/size}"

    "建国70周年阅兵。"
    "嫦娥四号人类首次登陆月球背面。"
    "香港修例风波。"
    "年末，武汉发现不明原因肺炎病例。"

    $ gs.change_stat("stability", -10)

    jump timeline_history_2020

label timeline_history_2020:
    scene black with fade
    centered "{size=40}2020年{/size}"

    "新冠疫情爆发。武汉封城。全国驰援。"
    "抗击疫情取得重大战略成果。"
    "全面建成小康社会。脱贫攻坚战取得全面胜利。"
    "北斗三号全球卫星导航系统开通。"

    $ gs.change_stat("stability", 10)

    jump timeline_history_2021

label timeline_history_2021:
    scene black with fade
    centered "{size=40}2021年{/size}"

    "建党100周年。天安门广场盛大庆典。"
    "神舟十二号、十三号载人飞船发射，中国空间站开启有人长期驻留时代。"
    "晚舟归航。"

    jump timeline_history_2022

label timeline_history_2022:
    scene black with fade
    centered "{size=40}2022年{/size}"

    "北京冬奥会举行。北京成为‘双奥之城’。"
    "中共二十大召开。开启全面建设社会主义现代化国家新征程。"
    "福建舰下水。第三艘航母，电磁弹射。"

    jump timeline_history_2023

label timeline_history_2023:
    scene black with fade
    centered "{size=40}2023年{/size}"

    "疫情防控平稳转段。"
    "神舟十六号、十七号发射。"
    "C919商业首飞。"

    jump timeline_history_2024

label timeline_history_2024:
    scene black with fade
    centered "{size=40}2024年{/size}"

    "嫦娥六号世界首次月背采样返回。"
    "深中通道通车。"

    jump timeline_history_2025

label timeline_history_2025:
    scene black with fade
    centered "{size=40}2025年{/size}"

    "海南封关运作。"
    "中国制造2025目标基本实现。"

    jump timeline_history_2030

label timeline_history_2030:
    scene black with fade
    centered "{size=40}2030年{/size}"

    "中国经济总量跃居世界第一。"
    "载人登月成功。五星红旗插上月球。"
    "6G通信技术商用。"

    jump timeline_history_2035

label timeline_history_2035:
    scene black with fade
    centered "{size=40}2035年{/size}"

    "基本实现社会主义现代化。"
    "生态环境根本好转，美丽中国建设目标基本实现。"
    "人均国内生产总值达到中等发达国家水平。"

    jump timeline_history_2040

label timeline_history_2040:
    scene black with fade
    centered "{size=40}2040年{/size}"

    "可控核聚变技术取得突破性进展。"
    "量子计算机实用化。"
    "智能机器人走进千家万户。"

    jump timeline_history_2045

label timeline_history_2045:
    scene black with fade
    centered "{size=40}2045年{/size}"

    "建成月球科研基地。"
    "火星探测载人任务启动。"

    jump timeline_history_2049

label timeline_history_2049:
    scene black with fade
    centered "{size=40}2049年{/size}"

    "建国100周年。"
    "建成富强民主文明和谐美丽的社会主义现代化强国。"
    "中华民族伟大复兴的中国梦终于实现。"

    jump timeline_history_2050

label timeline_history_2050:
    scene bg cyber_2050_history with fade
    
    "2050年。历史线终局。"
    
    "中国已经成为了世界第一强国。火星基地正在建设中，可控核聚变已经商用。"
    "城市里霓虹闪烁，飞行汽车穿梭其间。但在光鲜的表面下，赛博朋克式的图景隐约可见。"
    
    "巨大的跨国公司掌控着经济命脉。算法推荐决定了人们看什么、买什么、想什么。"
    "虽然物质极大丰富，但‘阶级’依然存在，甚至因为基因编辑技术而变得更加固化。"
    
    if gs.class_consciousness < 30:
        "这是一个繁荣的盛世，但也许，并不是先辈们梦想中的那个‘大同世界’。"
        "结局达成：【盛世下的阴影】"
    else:
        "虽然面临挑战，但人们心中对公平正义的追求从未熄灭。新的变革正在酝酿。"
        "结局达成：【未竟的螺旋】"
        
    jump credits
