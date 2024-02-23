from instagram_bot import Instagram_Bot

ig_bot = Instagram_Bot()
driver = ig_bot.login_instagram()
follower_driver = ig_bot.find_follower(driver= driver)
follow_all = ig_bot.follow_all(driver = follower_driver)