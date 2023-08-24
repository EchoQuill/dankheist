from colorama import Fore, Back, init as colorama_init
from plyer import notification
import random
import discord
from discord import SyncWebhook
import asyncio
import discord.errors
from threading import Thread
import logging
import re
import os
import requests
import discord.errors



#edit this if you want
webhook_log = False #chance this to "True" if you want it to send webhook messages
webhook_url = "" #webhook url here if you set webhook_log to true
deposit = True  #whether you want it to withdraw or not
withdraw = True #whether you want it to depost or not
chance_of_join = 100 #don't change if you want it to join all heists, else change it to how much percent you want it to join heists(percent without "%" symbol, only numbers)
notifications = True #chance this to "False" if you want it to not send messages regarding selfbot status
giveaway = False # whether you want to join gaws or not
stop_if_maintainance = True


#DON'T TOUCH THESE
bot_busy = False
ver = "0.1"
ver_check_url = "https://raw.githubusercontent.com/1010saf/dankheist/main/version.txt"
ver_check = requests.get(ver_check_url).text.strip()
forcestop_url = "https://raw.githubusercontent.com/1010saf/dankheist/main/forcestop.txt"


class MyClient(discord.Client):

    async def on_ready(self):
        # Create embedded messages
        embed1 = discord.Embed(
    title='logging in',
    description=f'logged in as {self.user}',
    color=discord.Color.dark_green()
)

        await asyncio.sleep(1)
        print(f'''{Fore.LIGHTGREEN_EX}---------------------------------{Fore.RESET}
Logged in as {self.user.name}!
{Fore.LIGHTGREEN_EX}---------------------------------''')
        await asyncio.sleep(2)
        self.bot = 270904126974590976
        self.dm = self.get_user(self.bot)
        #print(f'{Fore.LIGHTGREEN_EX}---------------------------------')
        #print(self.dm)
        #print()
        #print(self.bot)
        #print(f'{Fore.LIGHTGREEN_EX}---------------------------------')
        self.joined = 0
        self.webhook = SyncWebhook.from_url(webhook_url)
        if webhook_log == True:
            self.webhook.send(embed=embed1, username='dankheist')
            

    async def on_message(self, message):
        if message.author.id != 270904126974590976:
            return
        try:
            if message.embeds:
                for embed in message.embeds:
                    #joining heists
                    if embed.title is not None and "is starting a bank robbery" in embed.title.lower() and "don't" not in embed.description.lower and self.not_in_use != True:
                       # print(f"""{Fore.CYAN}{embed.title}
                        
#{embed.description}""")
                        #print(embed)
                        forcestop_check = requests.get(forcestop_url).text
                        if forcestop_check == "true":
                            print(f'''{Fore.LIGHTRED_EX}force stop enabled by dimlight., please check discord server for more info
This could be a bug or a dankmemer update that is not safe to use dankheist at

sorry for this again''')
                            self.not_in_use = True
                        print()
                        #chance of joining heists
                        if chance == True:
                            self.c2 = 100 - chance_of_join
                            self.c3 = random.randint(0,100)
                            if self.c3 < self.c2:
                                print(f'{Fore.YELLOW} skipping heist by {self.user}')
                                #skipping heist
                                continue
                        if withdraw == True:
                            async for cmd in self.dm.slash_commands("withdraw"):
                                if not cmd.application_id == self.bot:
                                    continue
                                await asyncio.sleep(random.uniform(0.5, 3))
                                await cmd(amount="2k")
                        print(f'{Fore.CYAN}Heist detected in {message.channel.id} aka {message.channel.name}')
                        #print(f'{Fore.LIGHTCYAN_EX}{message.components}')
                        print()
                        #for component in message.components:
                        #    print(f'{Fore.LIGHTCYAN_EX}{component}')
                        self.slepslop = ["fast","slow","medium","ultrafast","veryslow"]
                        self.move = random.choice(self.slepslop)
                        #print(self.slepslop)
                        #print(self.move)
                        if self.move == "fast":
                            self.wait = random.uniform(3, 5)
                            print(self.wait)
                        elif self.move == "slow":
                            self.wait = random.uniform(30, 30)
                            print(self.wait)
                        elif self.move == "medium":
                            self.wait = random.uniform(12, 20)
                            print(self.wait)
                        elif self.move == "ultrafast":
                            self.wait = random.uniform(0.5, 2)
                            print(self.wait)
                        elif self.move == "veryslow":
                            self.wait = random.uniform(31, 57)
                            #print(self.wait)
                        else:
                            print(f"{Fore.RED}opps!, f, no color")
                        #don't ask me "tf are u doing here, why not just do 'random.uniform(2,58)' or smthing instead?", because i used my big brain here :skull:
                        await asyncio.sleep(self.wait)
                        print(f'{Fore.LIGHTCYAN_EX}finished sleep')
                        await message.components[0].children[0].click()
                        self.joined += 1
                        #for component in message.components:
                        #    print(f'{Fore.LIGHTCYAN_EX}{component}')
                        print()
                        print(f'{Back.LIGHTRED_EX}Joined heist:- {self.user}, joined {self.joined} heists so far. ;>')
                        embed3 = discord.Embed(
                    title=f'hesit detected by {self.user} in {message.channel.id} aka {message.channel.name}',
                    description=f'hesit joined by {self.user}',
                    color=discord.Color.green()
                                )
                        if webhook_log == True:
                            self.webhook.send(embed=embed3, username='dankheist')
                        continue
                    #/deposit
                    elif embed.title is not None and "bankrob result" in embed.title.lower() and "#4caf50" in str(embed.colour):
                        forcestop_check = requests.get(forcestop_url).text
                        if forcestop_check == "true":
                            print(f'''{Fore.LIGHTRED_EX}force stop enabled by dimlight., please check discord server for more info
This could be a bug or a dankmemer update that is not safe to use dankheist at

sorry for this again''')
                            self.not_in_use = True
                            continue
                        print(embed.colour)
                        print(f"""{Fore.CYAN}{embed.title}
                        
{embed.description}""")
                        self.findint = re.findall(r'\d+', embed.description)
                        print(self.findint)
                        self.changeint = int(self.findint[0])#if the first digit is 0 then ofc it won't be a valid number ('01932' should/will not show up so useless to check that way)
                        if self.changeint == 0:
                            continue
                        if deposit != True:
                            continue
                        print(f'{Fore.LIGHTYELLOW_EX} doing /deposit')
                        await asyncio.sleep(random.uniform(0.1,1))
                        print(f'{Fore.LIGHTYELLOW_EX} finished sleep for /deposit')
                        async for cmd in self.dm.slash_commands("deposit"):
                            if not cmd.application_id == self.bot:
                                continue
                            await asyncio.sleep(random.uniform(0.5, 3))
                            await cmd(amount="max")
                        continue
                    #captcha notification and/or webhook msg
                    elif embed.title is not None and "captcha" in embed.title.lower() and str(self.dm) == "Dank Memer#5192":
                        print(f'{Fore.LIGHTRED_EX}opps , a captcha')
                        self.not_in_use = True
                        embed5 = discord.Embed(
                    title=f'CAPTCHA :- {self.user} ;<',
                    description=f"user got captcha :- {self.user} ;<",
                    color=discord.Color.red()
                                )
                        if webhook_log == True:
                            self.webhook.send(embed=embed5, username='dankheist')
                        if notifications != True:
                            continue
                        notification.notify(
                            title = f'{self.user}  DETECTED CAPTCHA',
                            message = "Pls solve it manually as iam an idiot when it comes to automating captcha ;<, feel free to complain in dimlight.'s dm so i can feel bad about not being able to code good like others",
                            app_icon = None,
                            timeout = 10,
                        )
                        continue
                    #banned notification and/or webhook msg
                    elif embed.title is not None and "banned" in embed.title.lower():
                        print(f'{Fore.LIGHTRED_EX}user {self.user} banned, gl making more accs ;<')
                        self.not_in_use = True
                        embed4 = discord.Embed(
                    title=f'user banned :- {self.user} ;<, well just make more accounts',
                    description=f"we are sad to tell that one of the bots got banned, please try appeal, if that doesn't work then rip",
                    color=discord.Color.dark_red()
                                )
                        if webhook_log == True:
                            self.webhook.send(embed=embed4, username='dankheist')
                        if notifications != True:
                            continue
                        notification.notify(
                            title = f'{self.user} banned',
                            message = "we are sad to tell that one of the bots got banned, please try appeal, if that doesn't work then rip",
                            app_icon = None,
                            timeout = 10,
                        )
                        continue
                    #giveaway joiner
                    elif embed.title is not None and "maintainance" in embed.title.lower():
                        self.not_in_use = True
                        embed6 = discord.Embed(
                    title=f'DANKMEMER UNDER MAINTAINANCE',
                    description=f"dankmemer under maintainance please confirm if the update is safe to continue with or not",
                    color=discord.Color.dark_red()
                                )
                        if webhook_log == True:
                            self.webhook.send(embed=embed6, username='dankheist')
                        if stop_if_maintainance == True:
                            continue
                        if notifications != True:
                            continue
                        notification.notify(
                            title = f'{self.user} banned',
                            message = "we are sad to tell that one of the bots got banned, please try appeal, if that doesn't work then rip",
                            app_icon = None,
                            timeout = 10,
                        )
                        continue
                    elif embed.title is not None and "giveaway" in embed.title.lower() and giveaway == True and self.not_in_use != True:
                        forcestop_check = requests.get(forcestop_url).text
                        if forcestop_check == "true":
                            print(f'''{Fore.LIGHTRED_EX}force stop enabled by dimlight., please check discord server for more info
This could be a bug or a dankmemer update that is not safe to use dankheist at

sorry for this again''')
                            self.not_in_use = True
                            continue
                        if chance == True:
                            self.c2 = 100 - chance_of_join
                            self.c3 = random.randint(0,100)
                            if self.c3 < self.c2:
                                print(f'{Fore.YELLOW} skipping giveaway by {self.user}')
                                #skipping gaws
                                continue
                        print(f'{Fore.YELLOW} giveaway in {message.channel.id} aka {message.channel.name}, detected by {self.user}')
                        await asyncio.sleep(random.uniform(0.1,7.8))
                        await message.components[0].children[0].click()
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
    print(f'''{Fore.GREEN}
 ____   __   __ _  __ _  _  _  ____  __  ____  ____ 
(    \ / _\ (  ( \(  / )/ )( \(  __)(  )/ ___)(_  _)
 ) D (/    \/    / )  ( ) __ ( ) _)  )( \___ \  )(  
(____/\_/\_/\_)__)(__\_)\_)(_/(____)(__)(____/ (__) {Fore.RESET}
{Back.LIGHTGREEN_EX}                    || HEIST JOINER ||  

{Back.LIGHTCYAN_EX}Welcome!
{Back.LIGHTMAGENTA_EX}Made by dimlight. on discord :>
{Back.CYAN}join dicord https://discord.gg/j6V5JnvCR for any help,{Back.RESET}


{Fore.GREEN}---------------------------------
''')
    webhook = SyncWebhook.from_url(webhook_url)
    embed = discord.Embed(
    title='dankheist started',
    description=f'current ver "{ver}".',
    color=discord.Color.purple()
    )
    embed2 = discord.Embed(
    title='update detected',
    description=f'''current ver "{ver}".
new update detected, please update from https://github.com/1010saf/dankheist''',
    color=discord.Color.red()
    )
    if ver_check != ver:
        if webhook_log == True:
            webhook.send(embed=embed2, username='dankheist')
        print(f'{Fore.YELLOW} new update detected, please update from https://github.com/1010saf/dankheist, current version {ver}, new version {ver_check}')
    if webhook_log == True:
        webhook.send(embed=embed, username='dankheist')
    if chance_of_join == 100:
        chance = False
    elif not (0 <= chance_of_join <= 100):
        print(f"""{Fore.RED}---------------------------------{Fore.RESET}
{Back.RED} 'chance_of_join' cannot be more than 100 or less than 0
please change it to something lower than 100 or more than 0 to continue""")
        print(f'''{Fore.RED}stopping bot :<
---------------------------------''')
        os.system("kill 1")
    else:
        chance = True
    tokens = []
    with open("tokens.txt", "r") as f:
        for line in f.readlines():
            tokens.append(line.strip())
    print(f'{Fore.GREEN}Loaded {len(tokens)} tokens.')
    run_bots(tokens)
