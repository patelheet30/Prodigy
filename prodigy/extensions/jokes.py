import hikari
import lightbulb
import aiohttp

jokes = lightbulb.plugin("Jokes", "A set of commands which send jokes. Customisable to include blacklists")

def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(jokes)

def unload(bot: lightbulb.BotApp) -> None:
    bot.remove_plugin(jokes)