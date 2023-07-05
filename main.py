import discord
import requests
from discord.ext import commands
import os
import asyncio
import multiprocessing
import colorama
from colorama import Fore, Back, Style

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
print(Back.RED +
      "IAM NOT RESPONSIBLE FOR IF YOU GET BANNED USING THIS.")
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
    dm = self.get_user(bot)
    print(dm)
    global dm
  async def on_message(self, message):
    if message.channel.id not in channels:
      return
    if message.author.id != 270904126974590976:
      return
    try:
      if message.embeds:
        for embed in message.embeds:
          if embed.title is not None and "is starting a bank robbery" in embed.title.lower():
            print(Fore.GREEN + 'heist')
            async for cmd in dm.slash_commands(query="deposit"):
              print(cmd)
              await asyncio.sleep(1,3)
              await cmd(amount="max")
            async for cmd in dm.slash_commands(query="withdraw"):
              print(cmd)
              await asyncio.sleep(1,3)
              await cmd(amount="2k")
            await message.components[0].children[0].click()
            print(Fore.GREEN + 'done')
            continue
      #elif "hi" in message.content.lower():
        #print(Fore.GREEN + f"hello {message.author}")
    except Exception as e:
      print(Fore.LIGHTRED_EX + "---------------------------------")
      print(f"An error occurred: {e}")
      print(Fore.LIGHTRED_EX + "---------------------------------")


async def run_bot(token):
  client = MyClient()
  await client.start(token)


if __name__ == '__main__':
  channels = [channel1, channel2]  # Replace with your desired channel IDs, this is the channels where the bot will join heists at.

  tokens = [
    "token1",
    "token2",
    "token3"
    #, os.environ['token2']
  ]  # Add more tokens as needed, use os.environ['token1'] to hide tokens if using replit or other public hosting services

  processes = []

  for token in tokens:
    process = multiprocessing.Process(target=asyncio.run,
                                      args=(run_bot(token), ))
    processes.append(process)

  for process in processes:
    process.start()

  for process in processes:
    process.join()
