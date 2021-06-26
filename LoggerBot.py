import discord


def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


token = read_token()

bot = discord.Client()


@bot.event  # event decorator/wrapper. More on decorators here: https://pythonprogramming.net/decorators-intermediate-python-tutorial/
async def on_ready():  # method expected by client. This runs once when connected
    print(f'We have logged in as {bot.user}')  # notification of login.


@bot.event  # event decorator/wrapper. More on decorators here: https://pythonprogramming.net/decorators-intermediate-python-tutorial/
async def on_message(message):
    if message.content == "ping":
        await message.channel.send("pong")
    if message.content == "kfc":
        await message.channel.send("miam miam")


@bot.event
async def on_message_delete(message):
    await message.channel.send(f"Message supprimé: {message.content} \n Auteur id: {str(message.author.id)} \n "
                               f"Auteur: <@{str(message.author.id)}>")


@bot.event
async def on_message_edit(past_message, after_message):
    await past_message.channel.send(
        f"Message édité: {past_message.content} -> {after_message.content} \n Auteur id: {str(past_message.author.id)} \n "
        f"Auteur: <@{str(past_message.author.id)}>")


@bot.event
async def on_reaction_add(reaction, user):
    await reaction.channel.send(
        f"Réaction ajouté: {reaction} \n Auteur id: {str(reaction.author.id)} \n "
        f"Auteur: <@{str(reaction.author.id)}>")

bot.run(token)
