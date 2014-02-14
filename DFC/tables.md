dfc_user
---------------------------

	-- id
	
	// login related
	-- user_email (email address) 邮箱登录
	-- user_nickname (char) 显示的名字
	-- user_password (password)

	// profile related
	-- user_birth (date) optional
	-- user_sex (choice) optional
	-- user_avatar (char) image url [default provided] NOT NULL 
	-- user_description (char) optional 

	// actions related
	-- user_last_login (date)
	-- user_recent_places (char) 用户最近活跃地址，这个字段虽然不是必须的，但是显示时方便检索，不用进行复杂的多表查询
	-- user_recent_connections (users) 发起活动时可做相关的邀请推荐

dfc_activity
--------------------------

	-- id

	// creation related
	
	-- activity_name (char)
	-- activity_detail_description (char)
	-- activity_place (char)
	-- activity_keywords (char) recommended
	-- activity_min_participants (integer)
	-- activity_max_participants (integer)
	-- activity_start_time (date)
	-- activity_end_time (date)

	// display related

	-- activity_current_participants (integer)
	-- activity_creator (foreign key user) [auto filled]
	-- activity_participants (array)
	-- activity_status (choice) = 审核［0/1/2］: 进行中 : 成功／失败
	-- activity_profile
