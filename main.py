from colorama import Fore, Back, init as colorama_init
from random import randint
import discord
import asyncio
from threading import Thread

class MyClient(discord.Client):

    async def on_ready(self):
        print(f'''{Fore.LIGHTGREEN_EX}---------------------------------{Fore.RESET}
Logged in as {self.user.name}!
{Fore.LIGHTGREEN_EX}---------------------------------''')
        self.bot = 270904126974590976
        self.dm = self.get_user(self.bot)
        self.joined = 0

    async def on_message(self, message):
        if message.author.id != 270904126974590976:
            return
        try:
            if message.embeds:
                for embed in message.embeds:
                    if embed.title is not None and "is starting a bank robbery" in embed.title.lower():
                        print(f'{Fore.GREEN}Heist')
                        async for cmd in self.dm.slash_commands("deposit"):
                           # if not cmd.application_id == self.bot:
                            #    continue
                            await asyncio.sleep(randint(1, 3))
                            await cmd(amount="max")
                        async for cmd in self.dm.slash_commands("withdraw"):
                            if not cmd.application_id == self.bot:
                                continue
                            await asyncio.sleep(randint(1, 3))
                            await cmd(amount="2k")
                        await message.components[0].children[0].click()
                        self.joined += 1
                        print(f'{Fore.GREEN}Joined heist:- {self.user}, joined {self.joined} heists so far.')
                        continue
        except (asyncio.TimeoutError, Exception) as e:
            if isinstance(e, asyncio.TimeoutError):
                print("Task took too long and timed out.")
            print(f"{Fore.RED}An error occurred: {e}{Fore.RESET}")

def run_bots(tokens):
    threads = []
    for token in tokens:
        thread = Thread(target=run_bot, args=(token,))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()

def run_bot(token):
    client = MyClient()
    client.run(token)

if __name__ == "__main__":
    colorama_init(autoreset=True)
    print(f'''{Fore.LIGHTYELLOW_EX}
d8888b. d88888b d8888b. db      
88  `8D 88'     88  `8D 88      
88oobY' 88ooooo 88oodD' 88      
88`8b   88~~~~~ 88~~~   88      
88 `88. 88.     88      88booo. 
88   YD Y88888P 88      Y88888P 
                           || GRINDER V2 ||  
{Back.MAGENTA}Welcome!

{Back.RED}I AM NOT RESPONSIBLE FOR IF YOU GET BANNED USING THIS.

{Back.GREEN}Made by dimlight. on discord :>{Back.RESET}

{Fore.GREEN}---------------------------------
''')
    tokens = []
    with open("tokens.txt", "r") as f:
        for line in f.readlines():
            tokens.append(line.strip())
    print(f'{Fore.GREEN}Loaded {len(tokens)} tokens.')
    run_bots(tokens)
