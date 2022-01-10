
import os, sys, time, requests, json, discord, asyncio, threading
from discord.ext import commands
with open('config.json') as f:
    config = json.load(f)
token = config.get('token')
intents = discord.Intents.all()
intents.members = True
headers = {'Authorization': f"Bot {token}"}
client = commands.Bot(command_prefix='.', case_insensitive=False,
  intents=intents)
client.remove_command('help')

@client.event
async def on_ready():
    os.system('cls||clear')
    await guild()


async def guild():
    global guildid
    global membercount
    print('\x1b[38;5;56m\n         ╦  ╦╔═╗╔╗╔╔═╗╔╦╗  ╔═╗╔═╗╦═╗╔═╗╔═╗╔═╗╔═╗╦═╗\n         ╚╗╔╝║╣ ║║║║ ║║║║  ╚═╗║  ╠╦╝╠═╣╠═╝╠═╝║╣ ╠╦╝\n          ╚╝ ╚═╝╝╚╝╚═╝╩ ╩  ╚═╝╚═╝╩╚═╩ ╩╩  ╩  ╚═╝╩╚═    \n  \n')
    guildid = int(input('Enter Server ID: '))
    await client.wait_until_ready()
    ob = client.get_guild(guildid)
    members = await ob.chunk()
    os.remove('scrape/members.txt')
    os.remove('scrape/channels.txt')
    os.remove('scrape/roles.txt')
    with open('scrape/members.txt', 'a') as txt:
        membercount = 0
        for member in members:
            txt.write(str(member.id) + '\n')
            membercount += 1
        else:
            print(f"[Scraped] {membercount} Members")
            txt.close()

    with open('scrape/channels.txt', 'a') as txt:
        channelcount = 0
        for channel in ob.channels:
            txt.write(str(channel.id) + '\n')
            channelcount += 1
        else:
            print(f"[Scraped] {channelcount} Channels")
            txt.close()

    with open('scrape/roles.txt', 'a') as txt:
        rolecount = 0
        for role in ob.roles:
            txt.write(str(role.id) + '\n')
            rolecount += 1
        else:
            print(f"[Scraped] {rolecount} Roles")
            txt.close()
            time.sleep(3)
            print('[Scrape Done!]')
            time.sleep(3)
            os.system('cls||clear')
            await guild()


def check():
    os.system('title [Venom Scraper] │ Made By RBaller')
    try:
        client.run(token)
    except:
        print('\n [!] Invalid Token')
        time.sleep(2)


check()