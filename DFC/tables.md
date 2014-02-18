abstract_user
---------------------------

	-- user_name
	-- user_email (email address) 邮箱登录
	-- user_nickname (char) 显示的名字
	-- user_password (password)

	-- user_birth (date) optional
	-- user_sex (choice) optional
	-- user_telephone optional
	-- user_avatar (char) image url [default provided] NOT NULL 
	-- user_description (char) optional 
	-- user_created (date)
	-- user_last_login (date)


tbl_user
---------------------------

	-- id
	
	@extend abstract_user


tbl_orgnization
---------------------------
	
	-- id

	@extend abstract_user

	-- orgnization_authorized
	-- orgnization_members
	-- orgnization_followers


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

	-- activity_followers
	-- activity_participants
	-- activity_creator (tbl_orgnization)
	-- activity_status (choice) = 审核［0/1/2］: 进行中 : 成功／失败
	-- activity_posts (char) 简单实现，之后会有单独一张表
