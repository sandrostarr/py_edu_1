from instapy import InstaPy

session = InstaPy(username="sandrostarr.art", password="5andr5wagm0ney")
session.login()
session.set_delimit_liking(enabled=True, max_likes=200, min_likes=0)
session.set_action_delays(enabled=True, like=13, randomize=True, random_range_from=75, random_range_to=125)
session.set_do_story(enabled = True, percentage = 70, simulate = False)
session.set_relationship_bounds(enabled=True,

				  delimit_by_numbers=True,
				   max_followers=500,
				    max_following=1000,
				       min_posts=5,
)
session.like_by_tags(["abstractart", "abstractobsession", "artistsoninstagram", "abstractartwork", "primitivism"], amount=19) # [1]

# session.set_smart_hashtags(['abstractart', 'primitivism', 'abstractobsession', 'primitiveart', 'neoexpressionism'], limit=5, sort='top', log_tags=True)
# session.like_by_tags(amount=1, use_smart_hashtags=True)