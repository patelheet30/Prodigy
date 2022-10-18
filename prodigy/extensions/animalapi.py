import aiohttp
import hikari
import lightbulb

animalapi = lightbulb.Plugin("Animal", "Commands relating to animal images and facts using APIs")

animals = [
        "Dog",
        "Panda",
        "Cat",
        "Fox",
        "Red Panda",
        "Koala",
        "Birb",
        "Raccoon",
        "Kangaroo"
        "Whale"
    ]


@animalapi.command
@lightbulb.command("animal", "Command group for this extension", auto_defer=True)
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def animal(ctx: lightbulb.SlashContext) -> None:
    return


@animal.child
@lightbulb.option("animal", "Choose which animal to send images of", choices=animals)
@lightbulb.command("image", "Sends an image of the animal chosen", auto_defer=True)
@lightbulb.implements(lightbulb.SlashSubCommand)
async def on_animal_image(ctx: lightbulb.SlashContext) -> None:
    # Changes the choice over to a compatible URL string
    animal = ctx.options.animal
    animalunderscore = animal.replace(" ", "_")
    animalneeded = animalunderscore.lower()
    # Connection to the API and gathering of needed data
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://some-random-api.ml/img/{animalneeded}") as jsondata:
            data = await jsondata.json()
    # Creates the embed
    image = data['link']
    image_embed = (
        hikari.Embed(
            title=f"It's an image of a {animal}!",
        )
        .set_image(f"{image}")
        .set_author(name=f"{ctx.author}", icon=f"{ctx.author.avatar_url}")
    )
    # Sends the embed
    await ctx.respond(image_embed)

@animal.child
@lightbulb.option("animal", "Choose the animal to get a fact about", choices=animals)
@lightbulb.command("fact", "Contains a fact about the animal chosen", auto_defer=True)
@lightbulb.implements(lightbulb.SlashSubCommand)
async def on_animal_fact(ctx: lightbulb.SlashContext) -> None:
    # Changes the choice over to a compatible URL string
    animal = ctx.options.animal
    animalunderscore = animal.replace(" ", "_")
    animalneeded = animalunderscore.lower()
    # Connection to the API and gathering of needed data
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://some-random-api.ml/facts/{animalneeded}") as jsondata:
            data = await jsondata.json()
    # Creates the embed
    fact = data['fact']
    fact_embed = (
        hikari.Embed(
            title=f"It's a fact about a {animal}!",
            description=f"{fact}"
        )
    )
    # Sends the embed
    await ctx.respond(fact_embed)


def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(animalapi)


def unload(bot: lightbulb.BotApp) -> None:
    bot.remove_plugin(animalapi)
