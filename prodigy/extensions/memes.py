import lightbulb
import hikari
import aiohttp

memes = lightbulb.Plugin("Memes", "Sends memes. Customisable memes will be added in the future")

@memes.command
@lightbulb.command("meme", "Sends a meme")
@lightbulb.implements(lightbulb.SlashCommand)
async def on_meme(ctx: lightbulb.SlashContext) -> None:
    async with aiohttp.ClientSession() as session:
        async with session.get("https://meme-api.herokuapp.com/gimme/1") as jsondata:
            data = await jsondata.json()
    
    meme = data['memes'][0]['url']
    await ctx.respond(meme)
    print(meme)

def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(memes)

def unload(bot: lightbulb.BotApp) -> None:
    bot.remove_plugin(memes)