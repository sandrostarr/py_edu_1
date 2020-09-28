from instapy import InstaPy

session = InstaPy(username="sandrostarr.art", password="5andr5wagm0ney0ne")
session.login()
session.set_delimit_liking(enabled=True, max_likes=200, min_likes=0)
session.set_action_delays(enabled=True, like=15, randomize=True, random_range_from=55, random_range_to=165)
session.set_quota_supervisor(enabled=True, sleep_after=["likes", "server_calls"], sleepyhead=True, notify_me=True,
                                peak_likes_hourly=20,
                                peak_likes_daily=200,
                                peak_server_calls_hourly=150,
                                peak_server_calls_daily=1500)
# session.set_action_delays(enabled=True, like=0.15, safety_match=False)

# session.set_relationship_bounds(enabled=True,

# 				  delimit_by_numbers=True,
# 				   max_followers=500,
# 				    max_following=1000,
# 				       min_posts=5,
# )
# session.set_user_interact(amount=1, randomize=True, percentage=15, media='Photo')
# session.set_do_story(enabled = True, percentage = 60, simulate = False)
session.like_by_tags(["abstractart", "abstractobsession", "artistsoninstagram", "abstractartwork", "primitivism"], amount=2) # [1]


# session.set_user_interact(amount=2,
# 				 percentage=70,
#                   randomize=True,
#                    media='Photo')
# session.follow_likers(['sandrostarr.art'], photos_grab_amount = 2, follow_likers_per_photo = 0, randomize=True, sleep_delay=600, interact=True)



# session.set_user_interact(amount=2, randomize=True, percentage=50, media='Photo')
# session.set_do_like(enabled=True, percentage=70)
# session.interact_user_followers(['sandrostarr.art'], amount=10, randomize=True)
# session.interact_by_users_tagged_posts(['sandrostarr.art'], amount=5, randomize=True, media='Photo')

# session.set_smart_hashtags(['abstractart', 'primitivism', 'abstractobsession', 'primitiveart', 'neoexpressionism'], limit=5, sort='top', log_tags=True)
# session.like_by_tags(amount=1, use_smart_hashtags=True)