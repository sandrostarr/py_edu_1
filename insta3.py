from instapy import InstaPy

session = InstaPy(username="sandrostarr.art", password="5andr5wagm0ney0ne")
session.login()

session.set_user_interact(amount=2, randomize=True, percentage=100, media='Photo')
session.set_do_like(enabled=True, percentage=100)
session.interact_user_followers(['sandrostarr.art'], amount=15, randomize=True)