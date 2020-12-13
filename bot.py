import discord
import os
import asyncio
import io
import json
from datetime import datetime

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
        if content.lower() == "!timeleft":
            smobelectionstart = datetime(2021,1,14,00,00,00)
            smobelectionend = datetime(2021,2,5,23,59,00)
            timeleftstart = (smobelectionstart - datetime.now()).total_seconds()
            timeleftend = (smobelectionend - datetime.now()).total_seconds()
            if timeleftstart >= 0:
                days = divmod(timeleftstart, 86400)
                hours = divmod(days[1],3600)
                minutes = divmod(hours[1],60)
                seconds = divmod(minutes[1],1)
                remainder_message = (f"There are {int(days[0])} days, {int(hours[0])} hours, {int(minutes[0])} minutes, and {int(seconds[0])} seconds " 
                "till January 14th when the election starts. The election ends on February 5th. Don't forget to vote for Jeanelle Agyem for Student Member of Board!")
            if timeleftstart < 0:
                days = divmod(timeleftend, 86400)
                hours = divmod(days[1],3600)
                minutes = divmod(hours[1],60)
                seconds = divmod(minutes[1],1)
                remainder_message = (f"There are {int(days[0])} days, {int(hours[0])} hours, {int(minutes[0])} minutes, and {int(seconds[0])} seconds " 
                "till February 5th when the election ends. Don't forget to vote for Jeanelle Agyem for Student Member of Board!")
            
            await message.channel.send(remainder_message.format(message))
        return
client = MyClient()
client.run(get_secret())