import disnake
import info.settings
import random

bot = info.settings.bot

def get_transform():
    transforms = ["Lobisomem","Kanima","Wendigo","Banshee ativa","Morreu"]

    transform = random.choice(transforms).lower()

    img = img = disnake.File(f"gifs/trans_{transform}.gif")
    
    if transform == "morreu":
        text = info.settings.transform_morreu.replace("{trans}", transform)
        
    else:
        text = info.settings.transform.replace("{trans}", transform)

    return [text, img]


def is_prodigio():
    prodigio = False
    
    img = disnake.File(f"gifs/notprodigio.gif")
    chance = random.randint(1,20)
    if chance > 11:
        prodigio = True
        img = disnake.File(f"gifs/prodigio.gif")
    return [prodigio, img]


def get_popularidade():
    popularidades = ["Impopular","Comum","Popular"]

    popularidade = random.choice(popularidades)

    img = None
    text = None
    if popularidade == "Impopular":
        text = info.settings.impopular
        img = disnake.File(f"gifs/impopular.gif")
    elif popularidade == "Comum":
        text = info.settings.comum
        img = disnake.File(f"gifs/comum.gif")
    else:
        text = info.settings.popular
        img = disnake.File(f"gifs/popular.gif")

    return [text, img]

def get_classe():
    classes = ["Baixa","Média","Alta"]

    classe = random.choice(classes)

    img = None
    text = None

    if classe == "Baixa":
        text = info.settings.baixa
        img = disnake.File(f"gifs/classebaixa.gif")
    elif classe == "Média":
        text = info.settings.media
        img = disnake.File(f"gifs/classemedia.gif")
    else:
        text = info.settings.alta
        img = disnake.File(f"gifs/classealta.gif")

    return [text, img]

async def send(message_content, message):
    # Retira o prefixo e Capitaliza
    msg = message_content.capitalize()

    # Pega uma escolha aleatória da lista no arquivo settings e deixa em minúsculo
    choice = random.choice(getattr(info.settings,msg)).lower()

    # Cria uma disnake.File a partir do gif
    image = disnake.File(f"gifs/{msg.lower()}_{choice}.gif")

    
    if choice != "humano":
        template = info.settings.message1.replace("{fam}", msg).replace("{esp}", choice)
    else:
        template = info.settings.message2.replace("{fam}", msg).replace("{esp}", choice)

    # Envia a mensagem no canal
    await message.reply(template, file = image)



@bot.command()
async def prodigio(ctx):
    # Checa se é prodígio
    result = is_prodigio()

    prodigio = result[0]
    img = result[1]

    if prodigio:
        await ctx.send(info.settings.prodigio, file=img)
    else:
        await ctx.send(info.settings.notprodigio, file=img)

    
@bot.command()
async def popularidade(ctx):

    result = get_popularidade()
    result_text = result[0]
    result_img = result[1]

    await ctx.send(result_text, file=result_img)

@bot.command()
async def transformação(ctx):

    result = get_transform()
    result_text = result[0]
    result_img = result[1]

    await ctx.send(result_text, file=result_img)

@bot.command()
async def classe(ctx):

    result = get_classe()
    result_text = result[0]
    result_img = result[1]

    await ctx.send(result_text, file=result_img)

@bot.slash_command()
async def embed(ctx, titulo: str, descrição: str, imagem: disnake.Attachment = None, footer: str = None):
    embed = disnake.Embed(title=titulo, description=descrição, color=disnake.Color.dark_red())
    embed.set_image(imagem)
    embed.set_footer(text=footer) if footer else None
    await ctx.send(embed=embed)
