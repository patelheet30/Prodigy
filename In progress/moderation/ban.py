# import hikari
# import lightbulb
# from prodigy.utils.permissions import on_permissions_check
# import datetime


# banning = lightbulb.Plugin("Ban", "Ban commands - Slash command")


# @banning.command
# @lightbulb.option("reason", "Reason to ban the user", type=str)
# @lightbulb.option("user", "User to ban", type=hikari.Member)
# @lightbulb.command("ban", "A command which bans a user", auto_defer=True)
# @lightbulb.implements(lightbulb.SlashCommand)
# @on_permissions_check
# async def ban(ctx: lightbulb.SlashContext) -> None:
#     user = ctx.options.user
#     reason = ctx.options.reason

#     ban_embed = (hikari.Embed(
#             title=f"{user} has been banned successfully",
#             description=f"Reason: {reason}\nModerator: {ctx.member}",
#             timestamp=datetime.datetime.now().astimezone()
#         )
#     )

#     await ctx.respond(ban_embed)


# def load(bot: lightbulb.BotApp) -> None:
#     bot.add_plugin(banning)


# def unload(bot: lightbulb.BotApp) -> None:
#     bot.remove_plugin(banning)
