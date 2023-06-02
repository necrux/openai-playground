#!/usr/bin/env python3
from os import path
import configparser
import openai
import yaml

RESUME_FILE = "../weshenderson.github.io/configs/resume.yaml"

with open(RESUME_FILE, encoding="UTF-8") as file:
    content = yaml.safe_load(file)

AUTH_FILE = f"{path.expanduser('~')}/.keys"
CONTENT = f"Please help me improve this resume summary: {content['basics']['summary']}"

config = configparser.RawConfigParser()
config.read(AUTH_FILE)

api_key = config["openai"]["key"]

openai.api_key = api_key

#print(openai.Model.list())

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": CONTENT},
        {"role": "system", "content": "You are and expert on resumes and IT recruiting."}
    ]
)

print(response)
