<h1>网站的交互性非常重要，大多数的参与活动的志愿者都是有很强的抒发欲望的！（看完请删除此行）</h1>
abstract_user
---------------------------

	-- user_name
	-- user_email (email address) 邮箱登录
	-- user_nickname (char) 显示的名字
	-- user_password (password)

	-- user_birth (date) optional
	-- user_sex (choice) optional
	-- user_telephone optional
	-- user_qq optional
	-- user_avatar (char) image url [default provided] NOT NULL 
	-- user_description (char) optional 
	-- user_created (date)
	-- user_last_login (date)
	-- user_mailbox 站内信
	-- launch_histo 发起活动的记录
	-- launch_credit 发起活动的信用，活动的成功率和评价
	-- launching 正在发起的活动



tbl_user
---------------------------

	-- id

	@extend abstract_user

	-- user_credit (integer) 信用等级，即实到率（实际到场/报名次数）
	-- user_friendlist 关注用户列表
	-- user_follower 关注自己的人
	-- user_follow 关注的人和组织
	-- user_takepart 参与过的活动所属的组织
	-- user_activitylist 活动参与记录
	-- user_takingpart 正在参与的活动
	-- user_orgnization optional 所属的团队
	-- user_vrank 志愿者等级，由参与次数和信用记录等综合评定
	-- user_honors (select) 用户的荣誉记录
	-- user_school (select) optional 学校或单位
	-- user_speciality optional 专业和特长



tbl_orgnization
---------------------------

	-- id

	@extend abstract_user

	-- orgnization_authorized
	-- orgnization_creater
	-- orgnization_history 团队的活动记录
	-- orgnization_members
	-- orgnization_followers
	-- orgnization_vtime (bool) 是否能提供公益时间证明
	-- orgnization_credit (integer) 组织的信用评估，用户评价
	-- orgnization_honors (select) 组织的荣誉评定
	-- orgnization_page url 团队介绍页（上传主页静态页面）


tbl_activity
--------------------------

	-- id
	-- activity_name (char)
	-- activity_description (char)
	-- activity_place (char)
	-- activity_keywords (char) recommended
	-- activity_start_time (date)
	-- activity_end_time (date)
	-- activity_volunteer_requirements (char) 对志愿者的要求
	-- activity_volunteer_needed (integer)
	-- activity_volunteers 已经报名的志愿者列表
	-- activity_visited 活动被浏览次数

	-- activity_followers
	-- activity_participants
	-- activity_participants_mask 列表中的参与者是否实际到场
	-- activity_creator (tbl_orgnization)
	-- activity_managers 活动中发起人可以添加具有post和管理聊天室权限的用户
	-- activity_status (choice) 未审核/进行中/被放弃/被冻结/完成
	-- activity_posts (char) 简单实现，之后会有单独一张表
	-- activity_replys 留言，包括路人的询问等
	-- activity_chatroom 议事厅的ID
	-- activity_config 包括参与者是否需要提供电话，是否需要真实姓名，是否需要验证，活动是否对外公开，参与者的最低信用度，是否需要参与者，是否需要志愿者
	-- activity_poster 活动的海报
	-- activity_face 活动展示的封面
	-- activity_url 活动邀请链接地址
	-- activity_rank 志愿者和参与者对活动的评价
	-- activity_honors 荣誉评定
	-- activity_vtime 记公益时间数，默认等于duration

tbl_chatroom
-----------------------------

	-- id
	-- chatroom_replys 回复列表
	-- chatroom_parent 所属的活动，或团队
	-- chatroom_type (select) 公开/内部

abstract_message
-------------------------------

	-- id
	-- message_parent 所属聊天室，活动留言或团队
	-- message_text (char)
	-- message_creater
	-- message_time (datetime)

tbl_reply
---------------------------------
	@extend abstract_message

	-- chat_color (select)
	-- chat_files (char) urls
	-- chat_tag (select) 普通信息/重要信息/活动记录/活动感受/通知/被删除
	-- chat_reciever 即回复聊天室主题

tbl_mail
---------------------------------
	@extend abstract_message

	-- mail_files (char) urls
	-- mail_type (select) 来自团队/系统/活动/个人
	-- mail_read (bool)
	-- mail_recieverlist
    -- need_needreply (bool) 是否需要回执

tbl_notice
---------------------------------
	@extend abstract_message

	-- notice_files (char) urls
	-- notice_parent 所在团队/系统/活动
	-- notice_read (bool)
	-- notice_needreply (bool) 是否需要回执

tbl_mailbox
--------------------------------

    -- id
    -- mailbox_type (select) 团队信箱/个人信箱/管理员信箱
    -- mailbox_ownerid
    -- mailbox_maillist
    -- mailbox_lastcheck (datetime) 上次打开邮箱的时间
