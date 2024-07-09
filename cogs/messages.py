from discord.ext import commands
import random

class Messages(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def hey(self, ctx):
        nameAuthor = ctx.author.name
        roles = [role for role in ctx.author.roles if role.name != "@everyone"]
        
        if roles:
            randomRole = random.choice(roles)
            roleName = randomRole.name
        else:
            roleName = "no role"

        result = "Hey " + nameAuthor + " comment est ce que tu vas ? T'es toujours " + roleName + " ?"
        await ctx.send(result)


async def setup(bot):
    await bot.add_cog(Messages(bot))