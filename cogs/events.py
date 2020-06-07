import discord
import global_vars
from discord.ext import commands


class EventsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        """
        Displayed message when bot is fired up.
        """
        print(f'Successfully logged in and booted...!')
        print('Logged in as ---->', self.bot.user)
        print('ID:', self.bot.user.id)
        print(f'Version: {discord.__version__}\n')

        # Initialize config_manager
        await global_vars.config_manager.load()

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """
        Command exceptions handling.
        """
        if type(error) == discord.ext.commands.errors.CommandNotFound:
            if ctx.message.content[1].isalpha():
                await ctx.send("Owo what's this command? \\*confused noises\\*")
        elif type(error) == discord.ext.commands.errors.CheckFailure or type(error) == discord.ext.commands.errors.NotOwner:
            await ctx.send("TwT sowwy but u can't wun this command xP")
        else:
            print(str(type(error))+": "+str(error))


def setup(bot):
    bot.add_cog(EventsCog(bot))
