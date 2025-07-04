import disnake
from disnake.ext import commands

# Setup bot
intents = disnake.Intents.all()
intents.typing = True
intents.presences = True
intents.message_content = True

bot = commands.Bot(command_prefix='!',intents=intents)

fam = None
esp = None

# Setup Choices (Variables)

transform_morreu = """﹒◦ ༶ 𖥔 𝐓ransformação 𖥔 ༶ ◦﹒


- — __*Você foi mordido por um alfa e infelizmente seu corpo não aceitou a mordida! Você está morrendo aos poucos*__

────────── ✦ ──────────  """
transform = """﹒◦ ༶ 𖥔 𝐓ransformação 𖥔 ༶ ◦﹒


- — __*Você foi mordido por um alfa e seu corpo aceitou a mordida! Sua espécie será: {trans}*__

────────── ✦ ──────────  """

message1 = """﹒◦ ༶ 𖥔 𝐅amília {fam} 𖥔 ༶ ◦﹒


- — __*Você pertence a família {fam}, parabéns você herdou a linhagem sobrenatural dela e será da espécie: {esp}*__

────────── ✦ ────────── 

"""

message2 = """﹒◦ ༶ 𖥔 𝐅amília {fam} 𖥔 ༶ ◦﹒


- — __*Você pertence a família {fam}, mas infelizmente não herdou sua linhagem sobrenatural e será da espécie: {esp}*__

────────── ✦ ──────────  

"""

prodigio = """﹒◦ ༶ 𖥔 𝐏rodígio 𖥔 ༶ ◦﹒


- — __*Você teve sorte! Parabéns, será prodígio se destacando entre os outros em conhecimento e habilidades*__

────────── ✦ ──────────  

"""

notprodigio = """
﹒◦ ༶ 𖥔 𝐏rodígio 𖥔 ༶ ◦﹒


- — __*Você não teve sorte desta vez! Infelizmente não será prodígio sendo uma pessoa comum entre os outros*__

────────── ✦ ──────────  
"""

impopular = """﹒◦ ༶ 𖥔 𝐏opularidade 𖥔 ༶ ◦﹒


- — __*Você não teve sorte desta vez! Não será uma pessoa popular em sua vida social sendo até mesmo um pouco invisível*__

────────── ✦ ──────────  """

comum = """﹒◦ ༶ 𖥔 𝐏opularidade 𖥔 ༶ ◦﹒


- — __*Você teve um pouco sorte desta vez! Será uma pessoa comum entre os outros, não se destacando e nem sendo invisível*__

────────── ✦ ──────────  """

popular = """

﹒◦ ༶ 𖥔 𝐏opularidade 𖥔 ༶ ◦﹒


- — __*Você teve sorte desta vez! É uma pessoa popular, sempre se destacando e fazendo amizades com muita facilidade*__

────────── ✦ ──────────  

"""

baixa = """﹒◦ ༶ 𖥔 𝐂lasse 𝐒ocial 𖥔 ༶ ◦﹒


- — __*Você não teve sorte desta vez! Sua classe social é baixa, tendo pouco dinheiro e poucos recursos*__

────────── ✦ ──────────  """

media = """﹒◦ ༶ 𖥔 𝐂lasse 𝐒ocial 𖥔 ༶ ◦﹒


- — __*Você  teve um pouco de sorte desta vez! Sua classe social é média, tem uma quantia de dinheiro considerável e um pouco mais de variedade de recursos*__

────────── ✦ ──────────  """

alta = """﹒◦ ༶ 𖥔 𝐂lasse 𝐒ocial 𖥔 ༶ ◦﹒


- — __*Você teve sorte desta vez! Sua classe social é alta, tendo bastante dinheiro e recursos bons a sua disposição*__

────────── ✦ ──────────  """

Talbot = ["Humano", "Lobisomem"]

Hale = ["Humano", "Lobisomem", "coiote"]

Martin = ["Humana", "Banshee Inativa"]

Whittemore = ["Humano", "Kanima"] 

Steiner = ["Humano", "Lobisomem"]

Tate = ["Humano", "Coiote"]

Yukimura = ["Humano", "Kitsune"]

Parrish = ["Humano", "Cão do Inferno"]



print("Configuração completa")