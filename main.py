#!/usr/bin/env python3
from os import path
import configparser
import openai

AUTH_FILE = f"{path.expanduser('~')}/.keys"
CONTENT = ""

config = configparser.RawConfigParser()
config.read(AUTH_FILE)

api_key = config["openai"]["key"]

openai.api_key = api_key

#print(openai.Model.list())

chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": CONTENT}])

print(chat_completion)