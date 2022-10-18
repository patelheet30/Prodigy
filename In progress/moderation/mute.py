# import hikari
# import lightbulb
# from prodigy.utils.permissions import on_permissions_check
# import datetime

# muting = lightbulb.Plugin("Mute", "Mute commands - Slash commands ")


# @muting.command
# @lightbulb.command("mute", "Several commands for the mute cog", auto_defer=True)
# @lightbulb.implements(lightbulb.SlashCommandGroup)
# async def on_mute(ctx):
#     return


# @on_mute.child()
# @lightbulb.option("reason", "Reason to mute this person", type=str)
# @lightbulb.option("user", "User to mute", type=hikari.Member)
# @lightbulb.command("add", "Mute a user", auto_defer=True)
# @lightbulb.implements(lightbulb.SlashSubCommand)
# @on_permissions_check
# async def mute(ctx: lightbulb.SlashContext) -> None:
#     user = ctx.options.user
#     reason = ctx.options.reason

#     mute_add_embed = (hikari.Embed(
#             title=f"{user} has been muted!",
#             description=f"Reason: {reason}\nModerator: {ctx.member}",
#             timestamp=datetime.datetime.now().astimezone()
#         )
#     )

#     await ctx.respond(mute_add_embed)


# @on_mute.child()
# @lightbulb.option("user", "User to remove mute from", type=hikari.Member)
# @lightbulb.command("remove", "Removes the muted role", auto_defer=True)
# @on_permissions_check
# async def unmute(ctx: lightbulb.SlashContext) -> None:
#     user = ctx.options.user

#     mute_remove_embed = (hikari.Embed(
#             title=f"{user} has been unmuted!",
#             description=f"Moderator: {ctx.member}",
#             timestamp=datetime.datetime.now().astimezone()
#         )
#     )

#     await ctx.respond(mute_remove_embed)


# def load(bot: lightbulb.BotApp) -> None:
#     bot.add_plugin(muting)


# def unload(bot: lightbulb.BotApp) -> None:
#     bot.remove_plugin(muting)
