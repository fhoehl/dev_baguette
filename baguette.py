#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import random

from birdy.twitter import UserClient

CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']
QUOTES_FILE_PATH = os.environ['QUOTES_FILE_PATH']

client = UserClient(CONSUMER_KEY,
      CONSUMER_SECRET,
      ACCESS_TOKEN,
      ACCESS_TOKEN_SECRET)

with open(QUOTES_FILE_PATH, 'r') as quotes:
  random_line = random.choice(quotes.readlines())
  client.api.statuses.update.post(status=random_line)

