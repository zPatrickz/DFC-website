#网站日程：
##1. 建立数据库
（---截止3月1日，曾明陟负责）

	详见tables.md

##2. 写底层事务处理代码
    ---截止3月10日
    王卫负责用户，用户间，组织，组织-用户间的操作。（注意是底层，而不涉及页面逻辑）
    曾明陟负责所有与活动有关的操作。
    谢闯负责所有信息类的操作，从包括聊天室。
#####全局操作
	refresh_mailtimes()
#####用户一般操作
    create_user
    remove_user 注销用户
    lock_user //锁定用户
    login
    logout
    user_modify_profile //修改用户信息
    set_user_credit //计算用户信用度(以后我会给出计算函数)
    change_passwd

    #####用户间操作
    user_follow //B用户关注A用户

#####组织相关操作
    create_org
    org_modify_profile
    org_change_face
    post_article //发布文章
    change_passwd
    set_org_credit
    close_org //关闭组织
    invite //向所有关注和参加过活动的用户发送邀请加入组织的邀请函通知
    add_honor //网站颁发的团队荣誉
    append_org_query //活动页面对游客公开的评论和询问区

    #####组织-用户相关操作
    follow_org //关注该组织
    unfollow_org
    add_org //加入该公益组织
    remove_member //踢出成员

#####活动相关操作
    create_act
    giveup_act
    lock_act
    submit_act
    change_act_info(intro,place,time) //更改活动信息
    modify_poster
    modify_face
    approach_deadline //当时间到达活动的预定时间，该活动就禁止加入了，除非修改活动时间
    act_up //赞/顶这个活动
    add_honor //活动标记，比如精华，每周之星，每月之星，年度最佳等。
    append_act_query //活动页面对游客公开的评论和询问区

#####用户-活动相关操作
    add_controller //controller是可以控制活动聊天室，发表post的人
    remove_controller
    enroll_as_volunteer
    enroll_as_participator
    enroll_as_organizer
    kick_user //踢出用户
    follow_act
    unfollow_act
    add_post //发表一个post
    remove_post //删除一个post


#####聊天室帖子相关操作
    append_talk //发表回复，给被回复者发送信息提醒
    add_tag //给聊天室的发言添加tag
    append_talk //添加聊天室发言
    remove_talk
    reply_talk //回复发言



通知相关操作（3类通知）
bcast_team //发送团队内通知
bcast_act //活动内通知
bcast_sys //系统通知
notice //单人通知
mail //私信
push //推送信息
read_noticement
delete_noticement
confirm //阅读带有需回执的通知后的回执操作

推送相关操作
push //给用户推送消息
read_push
delete_push

捐赠,评奖相关操作
donate
award

3. 与页面逻辑有关代码
（---截止3月20日，谢闯，王卫，曾明陟，刘金国）

##4. 前台呈现
（---截止4月10日，刘金国，曾明陟）

##5. 其他
#####注册网络工作室
由于短信提醒功能需要营业执照才能办理，所以可能到时候必须先要注册网络工作室
整个流程大概300元，10天左右。

#####购买域名
推荐volunteer2here.com，市场价约为55元/年

如果是org域名，选择面会比较广，市场价约为138元/年
#####购买短信服务
初期购入20000条，约1000元
#####购买云服务器
最大的一笔开销，根据服务器配置不同价格差异很大，会选择55-200元/月区间内的套餐。

#####开通网站支付宝账户
用于公益捐赠渠道

##5. Some New Idea
1. 加入一个小部分：每月评出最好的活动放在首页展示，还有一些简单的荣誉制度。这样可以鼓励大家做出一些好的活动和展示出来。
2. 活动完结后，聊天室中的动态信息中，只有被标记过的才会留下来。
3. 公益组织的主页可以添加文章，这是公益组织对外展示的一部分。

补充，用户-活动表，组织-用户表新增属性：add_time //加入时间
组织表新增属性father_org，因为很多很多组织有分点，比如DFC有南航站，那么南航站的活动记录就应该同时出现在DFC南京的页面上。