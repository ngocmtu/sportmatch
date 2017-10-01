#!/usr/bin/env python

from TwitterSearch import *
import sys
import json

users = set()
userstweet = []

try:
	tso = TwitterSearchOrder() # create a TwitterSearchOrder object
	tso.set_keywords(['football'])
	tso.set_geocode(32.709722, -97.368056, 3, imperial_metric=True)

	# tuo = TwitterUserOrder(name)
	# tuo.set_include_rts(False)
	# tuo.set_count(50)

	ts = TwitterSearch(
		consumer_key =  '5APe20dRCeE3HzC2OWo5LNCMK',
		consumer_secret = 'Cm8M0A2zLdDplThIIbyAkSlfL6soxBQdTZcmvKKzbLtchIhnoL',
		access_token = '2743910958-QzEA68W0x7QqnWZQTS5nfvbFEP2SCg4IPKgWMld',
		access_token_secret = 'jYfvWBfhf1eFw57jKefbzpT1BkEjSbXD7mW7Sbfh1tmU0'
	)

	for tweet in ts.search_tweets_iterable(tso):
		tcount += 1
		users.add(tweet['user']['screen_name'])

	for u in users:
		utweet = []
		tuo = TwitterUserOrder(u)
		tuo.set_include_rts(False)
		tuo.set_count(5)
		tuo.set_exclude_replies(True)

		for t in ts.search_tweets_iterable(tuo):
			if 'football' in t['text']:
				utweet.append(t['text'])
		userstweet.append(utweet)

except TwitterSearchException as e: # take care of all those ugly errors if there are some
	print(e)