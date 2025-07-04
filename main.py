from info.token import *
from info.settings import *
from info.commands import *
import disnake


print("Importações concluídas")


# When Bot is ready
@bot.event
async def on_ready():
    await bot.change_presence(status=disnake.Status.idle, activity=None)
    print("Bot Online!")

@bot.event
async def  on_message(message):
    comandos = ["hale", "talbot", "martin","parrish","yukimura","tate","steiner","whittemore",]
    message_content = message.content.strip("!")

    if message_content in comandos:
        await send(message_content, message)

#Feito com carinho por nevnh, em caso de problemas, 
# entre em contato comigo no discord: nevnh

bot.run(token())