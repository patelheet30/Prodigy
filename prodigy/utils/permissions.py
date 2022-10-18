import hikari
import lightbulb


def on_permissions_check(func):
    async def wrapper(ctx: lightbulb.Context) -> None:
        if ctx.options.user.id == ctx.author.id:
            await ctx.respond(f"You can't {func.__name__} yourself")
            return
        if ctx.options.user.is_bot:
            await ctx.respond(f"You can't {func.__name__} a bot")
            return
        if ctx.options.user.id == ctx.get_guild().owner_id:
            await ctx.respond(f"You can't {func.__name__} the owner")
            return
        if ctx.options.user.get_top_role().position > ctx.member.get_top_role().position:
            await ctx.respond(f"You can't {func.__name__} someone who has a higher role than you")
            return
        await func(ctx)
    return wrapper
