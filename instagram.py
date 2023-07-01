from instabot import Bot
bot=Bot()

#Enter your credentials
bot.login(username="###########",password="*********")

#Enter the username you want to follow
bot.follow('************')

#Give path of the image
bot.upload_photo("path",caption="caption")

#Enter the username you want to unfollow
bot.unfollow("****************")

#send message to multiple persons in a group,give username of the persons you want to send message
bot.send_message("Hello",["*********","#########"])

#Get list of followers
followers=bot.get_user_followers("username")
for follower in followers:
    print(bot.get_user_info(follower))

#Get list of following
following=bot.get_user_following("username")
for Following in following:
    print(bot.get_user_info(Following))

# Like a specific user's post by post URL
bot.like('post_url')

# Like the most recent posts in a user's feed
bot.like_user('username', amount=5)  # Like 5 posts

# Comment on a specific user's post by post URL
bot.comment('post_url', 'Nice photo!')

# Comment on the most recent posts in a user's feed
bot.comment_user('username', amount=5, comment='Nice photo!')  # Comment on 5 posts

#Search for username related to keyword
users = bot.search_users('photography')
for user in users:
    print(user['username'])

#Unfollow Non-Followers
bot.unfollow_non_followers()

#Getting list of people who liked your posts
likers = bot.get_post_likers('post_url')
for liker in likers:
    print(liker['username'])

#Fetching comments on a particular post
comments = bot.get_post_comments('post_url')
for comment in comments:
    print(comment['user']['username'], comment['text'])

# Delete a specific post by post URL
bot.delete_post('post_url')

# Delete the most recent posts
bot.delete_your_posts(amount=5)  # Delete 5 most recent posts

#Automatically follow back everyone we follow
bot.follow_followers()

#Automatically unfollowing everyone
bot.unfollow_everyone()

#Schedule Upload
from datetime import datetime, timedelta
# Schedule a post to be uploaded in 1 hour
future_time = datetime.now() + timedelta(hours=1)
bot.upload_photo("path", caption="Scheduled post", future_time=future_time)


