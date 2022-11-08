import hikari
import lightbulb
import aiohttp

jokes = lightbulb.Plugin("Jokes", "A set of commands which send jokes.")

@jokes.command
@lightbulb.command("joke", "Sends a joke")
@lightbulb.implements(lightbulb.SlashCommand)
async def on_joke(ctx: lightbulb.SlashContext) -> None:
    async with aiohttp.ClientSession() as session:
        async with session.get("https://some-random-api.ml/joke") as jsondata:
            data = await jsondata.json()
        
    joke = data['joke']
    joke_embed = (
        hikari.Embed(
            title="Joke incoming!!!",
            description=joke
        )
        .set_author(name=f"{ctx.author}", icon=f"{ctx.author.avatar_url}")
    )
    await ctx.respond(joke_embed)

def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(jokes)

def unload(bot: lightbulb.BotApp) -> None:
    bot.remove_plugin(jokes)