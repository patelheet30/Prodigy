import os
import hikari
import lightbulb
from dotenv import load_dotenv
import aiosqlite

load_dotenv()

bot = lightbulb.BotApp(
    token=os.environ["TOKEN"],
    default_enabled_guilds=int(os.environ["GUILD"]),
    intents=hikari.Intents.ALL,
    help_slash_command=True,
)


@bot.listen(hikari.StartedEvent)
async def on_start(event: hikari.StartedEvent) -> None:
    print("Bot is online!")


@bot.listen(hikari.StartedEvent)
async def db_connection(event: hikari.StartedEvent) -> None:
    bot.d.conn = await aiosqlite.connect("./prodigy/database/main.db")
    # Connects to the database for storing such as warnings
    async with bot.d.conn.cursor() as cursor:
        await cursor.execute("""CREATE TABLE IF NOT EXISTS warns(
                            warn_id INTπEGER PRIMARY_KEY,
                            user_id TEXT,
                            moderator_id TEXT,
                            reason TEXT
                        ) """)
    await bot.d.conn.commit()
    print("Database connected")


@bot.listen(hikari.StoppingEvent)
async def on_stop(event: hikari.StoppingEvent) -> None:
    # Closes the connection to the database
    await bot.d.conn.close()
    print("Bot has stopped")

# Loads the extensions
bot.load_extensions_from("./prodigy/extensions", recursive=True)


def run() -> None:
    if os.name != "nt":
        import uvloop
        uvloop.install()

    bot.run(
        status=hikari.Status.ONLINE,
        activity=hikari.Activity(
            name="me being developed!",
            type=hikari.ActivityType.WATCHING
        )
    )
