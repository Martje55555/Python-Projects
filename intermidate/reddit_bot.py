# import the modules
import praw
import enchant

# initialize with appropriate values
client_id = ""
client_secret = ""
username = ""
password = ""
user_agent = ""

# creating an authorized reddit instance
reddit = praw.Reddit(client_id = client_id,
					client_secret = client_secret,
					username = username,
					password = password,
					user_agent = user_agent)

# the subreddit where the bot is to be live on
target_sub = "Cats"
subreddit = reddit.subreddit(target_sub)

# phrase to trigger the bot
trigger_phrase = "! ReddditBOT CATS"

# enchant dictionary
d = enchant.Dict("en_US")

# check every comment in the subreddit
for comment in subreddit.stream.comments():
	# check the trigger_phrase in each comment
	if trigger_phrase in comment.body:
		# extract the word from the comment
		word = comment.body.replace(trigger_phrase, "")
		# initialize the reply text
		reply_text = ""
		# find the similar words
		similar_words = d.suggest(word)
		for similar in similar_words:
			reply_text += similar + " "
		# comment the similar words
		comment.reply(reply_text)
