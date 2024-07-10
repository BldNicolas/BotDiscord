from discord.ext import commands

from utils.riot_api import Api


class Valorant(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def user(self, ctx, playerName:str, playerTag:str):
        player = Api.getPlayer(playerName, playerTag)
        result = f"Hehehe je t'ai trouvé {player.get('name')}. Bah alors on est niveau {player.get('account_level')} ?"
        await ctx.send(result)

    @commands.command()
    async def mmr(self, ctx, playerName:str, playerTag:str):
        mmr = Api.getMMR(playerName, playerTag)
        result = mmr.get('data').get('current_data').get('currenttierpatched')
        await ctx.send(result)

async def setup(bot):
    await bot.add_cog(Valorant(bot))
