import praw
import random
user_agent = (" /u/OldSaintNick a random ChangeTip donation bot")

r = praw.Reddit(user_agent = user_agent)

#r.login('OldSaintBit','password')



def random_subreddit():
	subreddit = r.get_popular_subreddits(limit=100)
	sub=[]
	rand =random.randrange(1,100)
	for subreddit in subreddit:
		sub.append(subreddit)
	return sub[rand]
	
subreddit = random_subreddit()
print subreddit
comments = subreddit.get_comments(limit=1)
for comment in comments:
	author= str(comment.author)
	print ("Merry Bitmass /u/"+author+". Here have some bits /u/ChangeTip")
	#comment.reply("Merry Bitmass /u/"+author+". Here, have some bits /u/ChangeTip")


