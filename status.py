import discord
from dotenv import load_dotenv
import os
load_dotenv()

username = 'TranscribeBot'

mollys_current_status = ''

class MyClient(discord.Client):
    async def on_ready(self):
        print('online')
        # get all the guilds the bot is in
        for guild in self.guilds:
            # get all the members in the guild
            for member in guild.members:
                if member.name == 'dolly_molly':
                    # filter for CustomActivity
                    print(member.activities)
                    activities = list(filter(lambda activity: isinstance(activity, discord.CustomActivity), member.activities))
                    status = activities[0].name
                    emoji = activities[0].emoji
                    # send message in 523340394923294734
                    global mollys_current_status
                    mollys_current_status = f'{emoji} {status}'
    
    # when a member updates their activity
    async def on_presence_update(self, before, after):
        # make sure user is dolly_molly
        if after.name != 'dolly_molly':
            return
        # filter for CustomActivity
        print('member update')
        activities = list(filter(lambda activity: isinstance(activity, discord.CustomActivity), after.activities))
        if len(activities) > 0:
            status = activities[0].name
            emoji = activities[0].emoji
            # send message in 523340394923294734
            channel = self.get_channel(1136742439495938088)
            new_status = f'{emoji} {status}'
            global mollys_current_status
            if new_status != mollys_current_status:
                mollys_current_status = new_status
                await channel.send(f'{emoji} {status}')
    

                    
intents = discord.Intents.default()
# intents.message_content = True
# guilds is required to get the nickname of the user
intents.members = True
intents.presences = True



client = MyClient(intents=intents)
client.run(os.getenv('BOT_TOKEN'))