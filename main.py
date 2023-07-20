import discord
import requests
from discord.ext import commands
import os
import asyncio
import threading
import colorama
from colorama import Fore, Back, Style
import random

colorama.init(autoreset=True)

print(Fore.LIGHTYELLOW_EX + '''
d8888b. d88888b d8888b. db      
88  `8D 88'     88  `8D 88      
88oobY' 88ooooo 88oodD' 88      
88`8b   88~~~~~ 88~~~   88      
88 `88. 88.     88      88booo. 
88   YD Y88888P 88      Y88888P 
                           || GRINDER V2 ||  ''')
print(Back.MAGENTA + "Welcome!")
print()
print(Back.RED + "IAM NOT RESPONSIBLE FOR IF YOU GET BANNED USING THIS.")
print()
print(Back.GREEN + "made by dimlight. on discord :>")

print()
print(Fore.LIGHTGREEN_EX + "---------------------------------")
bot = 270904126974590976


class MyClient(discord.Client):

    async def on_ready(self):
        print(Fore.LIGHTGREEN_EX + "---------------------------------")
        print(f'Logged on as {self.user}!')
        print(Fore.LIGHTGREEN_EX + "---------------------------------")
        self.dm = self.user
        self.joined = 0

    async def on_message(self, message):
        #if message.channel.id not in channels:
            #return
        if message.author.id != 270904126974590976:
            return
        try:
            if message.embeds:
                for embed in message.embeds:
                    if embed.title is not None and "is starting a bank robbery" in embed.title.lower():
                        print(Fore.GREEN + 'heist')
                        async for cmd in dm.slash_commands(query="deposit"):
                            # print(cmd)
                            asyncio.sleep(random.randint(1,3))
                            await cmd(amount="max")
                        async for cmd in dm.slash_commands(query="withdraw"):
                            # print(cmd)
                            asyncio.sleep(random.randint(1,3))
                            await cmd(amount="2k")
                        await message.components[0].children[0].click()
                        # joined+=1
                        print(Fore.GREEN + f'joined heist:- {self.user}')  # {joined} times')
                        continue
            elif "hi" in message.content.lower():
                print(Fore.GREEN + f"hello {message.author} {self.user}")
        except asyncio.TimeoutError:
            print("Task took too long and timed out.")
        except Exception as e:
            print(Fore.LIGHTRED_EX + "---------------------------------")
            print(f"An error occurred: {e}")
            print(Fore.LIGHTRED_EX + "---------------------------------")


def run_bot(token):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    client = MyClient()
    client.loop = loop
    client.run(token)


if __name__ == '__main__':
    #channels = [
       # channel-1,channel-2
    #]  # Replace with your desired channel IDs

    tokens = [
        "token1", "token2"
    ]
    threads = []

    for token in tokens:
        thread = threading.Thread(target=run_bot, args=(token,))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
