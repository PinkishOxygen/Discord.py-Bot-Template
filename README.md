# Discord.py-Bot-Template
This is a template to make a Discord.py bot

#How to use
(these instructions only help for people using http://replit.com)

1.open https://discord.com/developers/applications

2. make a new application

3. name it whatever you want, on the left open the 'Bot' section

4. add new bot and name it the same as your application

5. hit "reset token" and a popup will appear, hit yes.

6. keep that tab open

7. import this code within replit by creating a new repl and hit 'import from github'.

8. go into the lock icon on the left and the key should be "DISCORD_TOKEN" and the value is your bot's token

9. copy and past the token into the value and hit "add new secret".

I added a default bot cmd "!hello" and the ouput would be a gif.

to add new cmds, use this format: 

``if message.content.startswith('{trigger word with included prefix}'):
      await message.channel.send('{output}')``
    
    
10. invite the bot to the desired server by going to the OAuth2 section on the discord developer tab, go to url generator and select 'bot' and 'administrator'.

12. generate url and invite the bot.

# Credits
most if not all the credits go to https://discordpy.readthedocs.io/en/stable/

another part of the credits go to https://github.com/SilverAidan for making the original template I used.
