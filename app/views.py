from app import app
from flask import render_template
from TwitterSearch import *
import sys
import json

def gettweet(longtude, lat, word):
	userset = set()
	users = []
	pics = []
	userstweet = []

	try:
		tso = TwitterSearchOrder() # create a TwitterSearchOrder object
		tso.set_keywords(['football'])
		tso.add_keyword(word)
		tso.set_geocode(longtude, lat, 5, imperial_metric=True)
		tso.set_count(70)

		ts = TwitterSearch(
			consumer_key =  '5APe20dRCeE3HzC2OWo5LNCMK',
			consumer_secret = 'Cm8M0A2zLdDplThIIbyAkSlfL6soxBQdTZcmvKKzbLtchIhnoL',
			access_token = '2743910958-QzEA68W0x7QqnWZQTS5nfvbFEP2SCg4IPKgWMld',
			access_token_secret = 'jYfvWBfhf1eFw57jKefbzpT1BkEjSbXD7mW7Sbfh1tmU0'
		)

		for tweet in ts.search_tweets_iterable(tso):
			l = len(userset)
			userset.add(tweet['user']['screen_name'])
			if l < len(userset):
				pics.append(tweet['user']['profile_image_url'])
		users = list(userset)

		num = 0
		for u in users:
			num += 1
			if num == 10:
				break
			utweet = []
			tuo = TwitterUserOrder(u)
			tuo.set_include_rts(False)
			tuo.set_count(100)

			for t in ts.search_tweets_iterable(tuo):
				if 'football' in t['text']:
					utweet.append(t['text'])
			userstweet.append(utweet)
			print("Num tweets: %i" % len(userstweet))

	except TwitterSearchException as e: # take care of all those ugly errors if there are some
		print(e)
	result = [users,pics,userstweet]
	return result

@app.route('/')
@app.route('/home')
def index():
	return render_template("home.html")

@app.route('/tcu')
def tcu():
	re = gettweet(32.709722, -97.368056, "tcu")
	user=re[0]
	picpic=re[1]
	tweets=re[2]
	return render_template("index.html", title= 'Home', user=user, picpic=picpic, tweets=tweets)

@app.route('/ut')
def ut():
	re = gettweet(30.283498866, -97.726163762, "ut")
	user=re[0]
	picpic=re[1]
	tweets=re[2]
	return render_template("index.html", title= 'Home', user=user, picpic=picpic, tweets=tweets)

@app.route('/anm')
def anm():
	re = gettweet(30.605997576, -96.33749865, "a&m")
	user=re[0]
	picpic=re[1]
	tweets=re[2]
	return render_template("index.html", title= 'Home', user=user, picpic=picpic, tweets=tweets)

@app.route('/ou')
def ou():
	re = gettweet(35.203499186, -97.438831578, "ou")
	user=re[0]
	picpic=re[1]
	tweets=re[2]
	return render_template("index.html", title= 'Home', user=user, picpic=picpic, tweets=tweets)

@app.route('/baylor')
def baylor():
	re = gettweet(31.5254696648, -97.142571263, "bu")
	user=re[0]
	picpic=re[1]
	tweets=re[2]
	return render_template("index.html", title= 'Home', user=user, picpic=picpic, tweets=tweets)

@app.route('/osu')
def osu():
	re = gettweet(36.122166178, -97.059833094, "osu")
	user=re[0]
	picpic=re[1]
	tweets=re[2]
	return render_template("index.html", title= 'Home', user=user, picpic=picpic, tweets=tweets)

@app.route('/wv')
def wv():
	re = gettweet(39.650164066, -79.952829522, "wvu")
	user=re[0]
	picpic=re[1]
	tweets=re[2]
	return render_template("index.html", title= 'Home', user=user, picpic=picpic, tweets=tweets)

@app.route('/match')
def match():
	re = gettweet(32.8666093,-96.7708326, "")
	user=re[0]
	picpic=re[1]
	tweets=re[2]
	return render_template("index.html", title= 'Home', user=user, picpic=picpic, tweets=tweets)
