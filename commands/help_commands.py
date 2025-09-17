import discord
from discord.ext import commands

class HelpCommands(commands.Cog):
    """Help and information commands"""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help')
    async def help_command(self, ctx, command_name: str = None):
        """Show help information for commands"""
        embed = discord.Embed(
            title="🎮 Roblox Helper Bot",
            description="A bot to help you create amazing games on Roblox!",
            color=discord.Color.blue()
        )
        
        if command_name:
            # Show help for specific command
            command = self.bot.get_command(command_name)
            if command:
                embed.title = f"Help: {command.name}"
                embed.description = command.help or "No description available"
                if command.usage:
                    embed.add_field(name="Usage", value=f"`{ctx.prefix}{command.usage}`", inline=False)
            else:
                embed.title = "❌ Command Not Found"
                embed.description = f"Command `{command_name}` not found."
        else:
            # Show all commands
            embed.add_field(
                name="📚 Scripting Commands",
                value="`!script` - Get Lua scripting examples\n`!function` - Learn about Lua functions\n`!event` - Learn about Roblox events",
                inline=False
            )
            embed.add_field(
                name="🎨 Game Design Commands", 
                value="`!gamedesign` - Get game design tips\n`!mechanics` - Learn about game mechanics\n`!ui` - UI design guidelines",
                inline=False
            )
            embed.add_field(
                name="📖 Resources Commands",
                value="`!resources` - Get useful development links\n`!tutorial` - Step-by-step tutorials\n`!docs` - Official documentation links",
                inline=False
            )
            embed.add_field(
                name="ℹ️ General Commands",
                value="`!help` - Show this help message\n`!about` - About this bot\n`!ping` - Check bot latency",
                inline=False
            )
            
        embed.set_footer(text="Use !help <command> for detailed information about a specific command")
        await ctx.send(embed=embed)

    @commands.command(name='about')
    async def about(self, ctx):
        """Information about the bot"""
        embed = discord.Embed(
            title="About Roblox Helper Bot",
            description="I'm here to help you create amazing games on Roblox!",
            color=discord.Color.green()
        )
        embed.add_field(
            name="What I can do:",
            value="• Provide Lua scripting examples and best practices\n"
                  "• Share game design tips and mechanics\n"
                  "• Give you resources and tutorials\n"
                  "• Help with UI design guidelines\n"
                  "• Answer common Roblox development questions",
            inline=False
        )
        embed.add_field(
            name="Getting Started:",
            value="Use `!help` to see all available commands or `!tutorial` for beginner guides!",
            inline=False
        )
        embed.set_thumbnail(url="https://images.rbxcdn.com/8560fd50f1b5b5fa4b37a74e6e8af8eb-RobloxLogo.png")
        await ctx.send(embed=embed)

    @commands.command(name='ping')
    async def ping(self, ctx):
        """Check bot latency"""
        latency = round(self.bot.latency * 1000)
        embed = discord.Embed(
            title="🏓 Pong!",
            description=f"Bot latency: {latency}ms",
            color=discord.Color.blue()
        )
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(HelpCommands(bot))