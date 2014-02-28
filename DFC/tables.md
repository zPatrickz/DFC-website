abstract_user
---------------------------
	-- id (char)
	-- user_name (char)
	-- user_email (email address) 邮箱登录
	-- user_nickname (char) 显示的名字
	-- user_password (password)

	-- user_birth (date) optional
	-- user_sex (choice) optional
	-- user_telephone (telephone number) optional
	-- user_qq (QQ number) optional
	-- user_avatar (char) image url [default provided] NOT NULL
	-- user_description (char) optional
	-- user_created (date)
	-- user_last_login (date)
	-- user_credit (integer) 发起活动的信用，活动的缺席率，他人评价，信息完成度等综合的指标



tbl_user
---------------------------
	@extend abstract_user

	-- user_credit (integer) 信用等级，即实到率（实际到场/报名次数）
	-- user_honors (select) 用户的荣誉记录
	-- user_school (select) optional 学校或单位
	-- user_speciality (char) optional 专业和特长
	-- escape_times (integer) 逃跑次数
	-- enrolled_times (integer) 报名次数，包括逃跑和参与的总次数
	-- mean_score (float) 活动对用户的评分平均值
	-- message_config (byte) 用户信息设定：是否接受关注组织的活动的短信推送，是否接受系统的短信通知。



tbl_orgnization
---------------------------
	@extend abstract_user

	-- orgnization_authorized (bool)
	-- orgnization_creater (id)
	-- orgnization_vtime (bool) 是否能提供公益时间证明
	-- orgnization_credit (integer) 组织的信用评估，用户评价
	-- orgnization_honors (select) 组织的荣誉评定
	-- orgnization_page (url) 团队介绍页（上传主页静态页面）
    -- mailed_times //今日短信群发次数
    -- alipay_link //支付宝链接


tbl_activity
--------------------------

	-- id
	-- activity_name (char)
	-- activity_description (char)
	-- activity_place (char)
	-- activity_keywords (char) recommended
	-- activity_start_time (date)
	-- activity_end_time (date)
	-- activity_volunteer_needed (integer)
	-- activity_visited (integer) 活动被浏览次数

	-- activity_creator(id) !one of the org members
	-- activity_org (id) the parent organization
	-- activity_managers 活动中发起人可以添加具有post和管理聊天室权限的用户
	-- activity_config (byte) 包括参与者是否需要提供电话，是否需要真实姓名，活动是否对外公开，是否需要参与者。由于项目较多，用byte替代bool，使用时解析下。
	-- lowest_credit (float) 参与用户最低信用度，default 0
	-- need_money (float) 接受资金援助的需求资金，default 0
	-- activity_progress (select) 进行前/进行中/被放弃/完成
	-- activity_status (byte) 是否审核过/是否被冻结
	-- activity_poster (url) 活动的招募海报
	-- activity_face (url) 活动展示的封面
	-- activity_rank (integer) 志愿者和参与者对活动的评价
	-- activity_vtime (float) 记公益时间数，默认等于duration
	-- activity_tel (phone number) default set to creater's phone number
    -- mailed_times //今日短信群发次数

tbl_up
-----------------------------
	-- up_act (id) the id of the activity article
	-- up_ip (IP Address) 防止IP重复
	-- up_weight (integer) 权重，点赞的权重由点赞者是否注册，信用记录，与活动关系等有关

tbl_user&org
------------------------------------------

    -- taken_part_in(bool)
    -- is_member(bool)
    -- follow_org(bool)
    -- role_org(select) normal/removed(past member)
    -- user_group(char) 短信通知后会询问是否给群组起名，于是用户会有群组属性

tbl_user&user
---------------------------------------
    --follow_uu (bool) B是否关注A

tbl_user&act
-----------------------------------------

    -- enrolled (bool)
    -- participated (bool) 是否实际到场
    -- kicked_times(integer) 被踢出3次无法再次加入
    -- role (select) controller/volunteer/normal/follower

tbl_chatroom
-----------------------------
	Note: The relationship between chatroom and org(act) is N to 1
	-- id (char)
	-- chatroom_parent (id) 所属的活动，或团队
	-- chatroom_type (select) 公开/内部

abstract_message
-------------------------------

	-- id (char)
	-- message_parent (id) 所属聊天室，活动留言或团队，ID需要是带有前缀org_001这种形式，以判别这是属于什么类型的parent（活动信息/团队信息/系统信息）。
	-- message_text (char)
	-- message_creater (id)
	-- message_time (datetime)

tbl_query
-------------------------------
	@extend abstract_query

tbl_talk
---------------------------------
	Note: Including activity posts & chatroom talks
	@extend abstract_message

	-- chat_color (select)
	-- chat_files (char) urls
	-- chat_tag (select) 普通信息/重要信息/活动记录/活动感受/通知/被删除
	-- chat_reciever (id) 即回复的哪条聊天室主题


tbl_article
-----------------------------
	Note: Including activity stories & organazation articles
	@extend abstract_message

    -- long_text (char) message_text 视为title
    -- read_statistics (integer) 阅读统计
    -- peer_review (char) 业内人士的评价
    -- peer_score (integer[0-9]*5) 业内人士打分，5个指标
	-- article_honors (char) 荣誉评定，即大奖赛获奖记录

tbl_notice
---------------------------------
	@extend abstract_message

	-- notice_files (char) urls
	-- notice_read (bool)
	-- notice_needreply (bool) 是否需要回执
	-- notice_type (select) private mail/system notice(donation, awards, expenditure, platform)/org notice/activity notice/push
	-- notice_ways (byte) web/phone/weixin(future)/email default set to 1000
	-- reply_tel (phone number) default set to sender's telephone
	-- notice_targetlist (id list)

tbl_donation
----------------------------
	Note: The donation or expenditure(which means to support org using non-oriented fund.) record, using alipay
	-- id
	-- donation_time (datetime)
	-- donation_type (select) oriented/non-oriented
	-- donation_amount (float)
	-- donation_from (id) donator
	-- donation_to (id) the target org/activity
	-- annoymous (bool) default set to False
	-- donation_tips (float) percentage of tips to web developer if type is non-oriented. (default 0.1)
	-- donation status (select) underconfirm(待公益组织确认收款)/succeeded/failed/retrived
	-- donation_fund (integer) 网站基金剩余总额

tbl_award
----------------------
	Note: award record
	-- id
	-- award_name (char)
	-- award_target (id) article id
	-- award_ranker (id) 本次奖项的几位公益达人评委（future）
	-- award_amount (float) the amount of money