from instapy import InstaPy

session = InstaPy(username="rateque.ru", password="graffitiartista")
session.login()
session.like_by_tags(["художникибердска"], amount=5) # [1]