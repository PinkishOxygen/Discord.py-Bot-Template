import discord
import os
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
  print('Im logged in as  {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return
   
    #add custom cmds here
  if message.content.startswith('!hello'):
    await message.channel.send('https://tenor.com/view/hello-gif-19947459')

keep_alive()
client.run(os.getenv('DISCORD_TOKEN'))
