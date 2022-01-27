
#NAZWY PLIKÓW KONT MUSZĄ BYĆ UMIESZCZONE MAŁYMI LITERAMI
import discord,json,os,random
from discord.ext import commands

with open("config.json") as file: # Load the config file
    info = json.load(file)
    token = info["token"]
    delete = info["autodelete"]
    prefix = info["prefix"]

bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    print("Bot Running!")
     
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('Generator róznych kont discord | ROOT: Iron-Cut#3255 ')) 
@bot.command() # Stock command
@commands.has_role(934118996242989116)
async def stock(ctx):
    stockmenu = discord.Embed(title="Zapas konta",description="") # Zdefiniuj osadzanie
    for filename in os.listdir("Accounts"):
        with open("Accounts\\"+filename) as f: # Otwórz każdy plik w folderze kont
            ammount = len(f.read().splitlines()) # Uzyskaj ilość linii
            name = (filename[0].upper() + filename[1:].lower()).replace(".txt","") #Spraw, aby nazwa wyglądała ładnie
            stockmenu.description += f"*{name}* - {ammount}\n" # Dodaj do osadzenia
    await ctx.send(embed=stockmenu) # Send the embed

@bot.command() #Gen polecenie
async def gen(ctx,name=None):
    if name == None:
        await ctx.send("Określ konto, które chcesz!") # Powiedz błąd, jeśli nie podano nazwy
    else:
        name = name.lower()+".txt" #Dodaj rozszerzenie .txt
        if name not in os.listdir("Accounts"): # Jeśli nazwy nie ma w katalogu
            await ctx.send(f":no_entry_sign: Konto nie istnieje. `{prefix}stock`")
        else:
            with open("Accounts\\"+name) as file:
                lines = file.read().splitlines() #Przeczytaj wiersze w pliku
            if len(lines) == 0: # If the file is empty
                await ctx.send("❌ Te konta są niedostępne") #Send error if lines = 0
            else:
                with open("Accounts\\"+name) as file:
                    account = random.choice(lines) # Get a random line
                try: #Try to send the account to the sender
                    await ctx.author.send(f"`{str(account)}`\n\nTa wiadomość zostanie usunięta za {str(delete)} seconds!",delete_after=delete)
                except: # If it failed send a message in the chat
                    await ctx.send("❌ Nie udało się wysłać! Włącz swoje bezpośrednie wiadomości")
                else: # If it sent the account, say so then remove the account from the file
                    await ctx.send("✅Wyślij konto do skrzynki odbiorczej!")
                    with open("Accounts\\"+name,"w") as file:
                        file.write("") #Clear the file
                    with open("Accounts\\"+name,"a") as file:
                        for line in lines: #Add the lines back
                            if line != account: #Dont add the account back to the file
                                file.write(line+"\n") # Add other lines to file
                                embed=discord.Embed(title="Udało ci sie!", description="Wygenerowano Konto  ❤️ ")
            embed.set_footer(icon_url = "https://cdn.discordapp.com/attachments/926278029817298965/930891668570374214/km-swieta-graf.png", text=f" ┇🎄┇Katedra Meneli")
            await ctx.send(embed=embed)
                               
bot.run(token)