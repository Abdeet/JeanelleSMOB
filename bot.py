import discord
import os
import asyncio
import io
import json
import datetime

FILE_PATH = os.path.dirname(os.path.abspath( __file__ ))

def get_secret():
    with open(FILE_PATH + "/secret.txt", "r+") as secret_txt:
        secret = secret_txt.readlines()[0]
        return secret

class MyClient(discord.Client): 
    async def on_ready(self):
        print('JeanelleSMOB Up')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        content = message.content
        if message.author.id == self.user.id:
            return
        if content.lower() == "!smob" or content.lower() == "!studentmemberofboard":
            await message.channel.send("The Student Member of Board brings a student viewpoint to the FCPS Board of Education. They represent the student body in matters related to education.")
            return
        return
client = MyClient()
client.run(get_secret())