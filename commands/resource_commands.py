import discord
from discord.ext import commands

class ResourceCommands(commands.Cog):
    """Resource and tutorial commands"""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='resources')
    async def development_resources(self, ctx, category: str = None):
        """Get useful Roblox development resources"""
        if not category:
            embed = discord.Embed(
                title="📚 Development Resources",
                description="Choose a category to explore:",
                color=discord.Color.teal()
            )
            embed.add_field(
                name="Available Categories:",
                value="`!resources official` - Official Roblox documentation\n"
                      "`!resources learning` - Learning platforms and tutorials\n"
                      "`!resources tools` - Development tools and utilities\n"
                      "`!resources community` - Community resources and forums\n"
                      "`!resources assets` - Free assets and models",
                inline=False
            )
            await ctx.send(embed=embed)
            return

        category = category.lower()
        
        if category == "official":
            embed = discord.Embed(
                title="🏢 Official Roblox Resources",
                color=discord.Color.teal()
            )
            embed.add_field(
                name="📖 Documentation",
                value="• [Roblox Developer Hub](https://developer.roblox.com/)\n"
                      "• [API Reference](https://developer.roblox.com/en-us/api-reference)\n"
                      "• [Luau Language Guide](https://luau-lang.org/)\n"
                      "• [Creator Hub](https://create.roblox.com/)",
                inline=False
            )
            embed.add_field(
                name="🎓 Official Tutorials",
                value="• [Getting Started Guide](https://developer.roblox.com/en-us/onboarding)\n"
                      "• [Scripting Tutorial](https://developer.roblox.com/en-us/learn-roblox/scripting)\n"
                      "• [Building Tutorial](https://developer.roblox.com/en-us/learn-roblox/building)\n"
                      "• [Game Design Course](https://developer.roblox.com/en-us/learn-roblox/game-design)",
                inline=False
            )
            
        elif category == "learning":
            embed = discord.Embed(
                title="🎓 Learning Platforms",
                color=discord.Color.teal()
            )
            embed.add_field(
                name="📺 YouTube Channels",
                value="• AlvinBlox - Beginner-friendly tutorials\n"
                      "• TheDevKing - Advanced scripting\n"
                      "• Peaspod - Game development tutorials\n"
                      "• GnomeCode - Scripting and UI tutorials",
                inline=False
            )
            embed.add_field(
                name="💻 Online Courses",
                value="• Codecademy Lua Course\n"
                      "• Udemy Roblox Development\n"
                      "• Khan Academy Programming\n"
                      "• FreeCodeCamp Programming Basics",
                inline=False
            )
            
        elif category == "tools":
            embed = discord.Embed(
                title="🛠️ Development Tools",
                color=discord.Color.teal()
            )
            embed.add_field(
                name="🔧 Essential Tools",
                value="• Roblox Studio (Official IDE)\n"
                      "• Visual Studio Code (External scripting)\n"
                      "• Rojo (External development workflow)\n"
                      "• Git (Version control)",
                inline=False
            )
            embed.add_field(
                name="🎨 Design Tools",
                value="• Blender (3D modeling - free)\n"
                      "• GIMP (Image editing - free)\n"
                      "• Audacity (Audio editing - free)\n"
                      "• Paint.NET (Simple image editing)",
                inline=False
            )
            
        elif category == "community":
            embed = discord.Embed(
                title="👥 Community Resources",
                color=discord.Color.teal()
            )
            embed.add_field(
                name="💬 Forums & Communities",
                value="• [Roblox Developer Forum](https://devforum.roblox.com/)\n"
                      "• [r/robloxgamedev](https://reddit.com/r/robloxgamedev)\n"
                      "• [Roblox OSS Discord](https://discord.gg/robloxoss)\n"
                      "• [Hidden Developers Discord](https://discord.gg/hd)",
                inline=False
            )
            embed.add_field(
                name="📈 Analytics & Tools",
                value="• RoMonitor - Game analytics\n"
                      "• RoPro - Browser extension\n"
                      "• Roblox+ - Enhanced features\n"
                      "• BTRoblox - Better Roblox experience",
                inline=False
            )
            
        elif category == "assets":
            embed = discord.Embed(
                title="🎁 Free Assets & Models",
                color=discord.Color.teal()
            )
            embed.add_field(
                name="🏪 Asset Sources",
                value="• Roblox Toolbox (built into Studio)\n"
                      "• [Free Models Group](https://www.roblox.com/groups/4199740)\n"
                      "• [Open Source Models](https://www.roblox.com/groups/5234572)\n"
                      "• GitHub Roblox repositories",
                inline=False
            )
            embed.add_field(
                name="⚠️ Important Notes",
                value="• Always review free models for malicious scripts\n"
                      "• Check licensing terms before use\n"
                      "• Credit creators when appropriate\n"
                      "• Test thoroughly before publishing",
                inline=False
            )
        else:
            embed = discord.Embed(
                title="❌ Unknown Category",
                description=f"I don't have resources for '{category}'. Use `!resources` to see available categories.",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
            return
            
        await ctx.send(embed=embed)

    @commands.command(name='tutorial')
    async def tutorials(self, ctx, topic: str = None):
        """Get step-by-step tutorials for common tasks"""
        if not topic:
            embed = discord.Embed(
                title="📋 Available Tutorials",
                description="Choose a tutorial topic:",
                color=discord.Color.purple()
            )
            embed.add_field(
                name="🏁 Getting Started:",
                value="`!tutorial setup` - Setting up Roblox Studio\n"
                      "`!tutorial first` - Your first game project\n"
                      "`!tutorial publish` - Publishing your game",
                inline=False
            )
            embed.add_field(
                name="💻 Scripting:",
                value="`!tutorial variables` - Working with variables\n"
                      "`!tutorial functions` - Creating functions\n"
                      "`!tutorial events` - Handling events",
                inline=False
            )
            embed.add_field(
                name="🎮 Game Features:",
                value="`!tutorial gui` - Creating GUI interfaces\n"
                      "`!tutorial datastore` - Saving player data\n"
                      "`!tutorial leaderstats` - Creating leaderboards",
                inline=False
            )
            await ctx.send(embed=embed)
            return

        topic = topic.lower()
        
        if topic == "setup":
            embed = discord.Embed(
                title="🛠️ Setting Up Roblox Studio",
                color=discord.Color.purple()
            )
            embed.add_field(
                name="Step 1: Download",
                value="1. Go to [roblox.com](https://www.roblox.com/)\n"
                      "2. Click 'Create' in the top menu\n"
                      "3. Click 'Start Creating' to download Studio\n"
                      "4. Run the installer when download completes",
                inline=False
            )
            embed.add_field(
                name="Step 2: First Launch",
                value="1. Open Roblox Studio\n"
                      "2. Sign in with your Roblox account\n"
                      "3. Choose a template or start with Baseplate\n"
                      "4. Familiarize yourself with the interface",
                inline=False
            )
            embed.add_field(
                name="Step 3: Basic Navigation",
                value="• Use WASD to move camera\n"
                      "• Right-click and drag to rotate view\n"
                      "• Scroll to zoom in/out\n"
                      "• F key to focus on selected object",
                inline=False
            )
            
        elif topic == "first":
            embed = discord.Embed(
                title="🎯 Your First Game Project",
                color=discord.Color.purple()
            )
            embed.add_field(
                name="Step 1: Plan Your Game",
                value="1. Decide on a simple game concept (e.g., obby, tycoon)\n"
                      "2. Sketch out the basic gameplay loop\n"
                      "3. List the main features you want to include\n"
                      "4. Start small - you can always add more later",
                inline=False
            )
            embed.add_field(
                name="Step 2: Build the Basic Structure",
                value="1. Create the spawn area for players\n"
                      "2. Build the main game area/map\n"
                      "3. Add basic lighting and atmosphere\n"
                      "4. Test by clicking the Play button",
                inline=False
            )
            embed.add_field(
                name="Step 3: Add Scripting",
                value="1. Insert a ServerScript in ServerScriptService\n"
                      "2. Start with simple player join messages\n"
                      "3. Add basic game mechanics one at a time\n"
                      "4. Test frequently to catch errors early",
                inline=False
            )
            
        elif topic == "publish":
            embed = discord.Embed(
                title="🚀 Publishing Your Game",
                color=discord.Color.purple()
            )
            embed.add_field(
                name="Step 1: Final Testing",
                value="1. Test all game features thoroughly\n"
                      "2. Check for any error messages in Output\n"
                      "3. Test with friends if possible\n"
                      "4. Ensure the game is fun and complete",
                inline=False
            )
            embed.add_field(
                name="Step 2: Configure Game Settings",
                value="1. Go to File → Game Settings\n"
                      "2. Set appropriate genre and description\n"
                      "3. Upload a compelling thumbnail\n"
                      "4. Set access permissions (Public/Friends/Private)",
                inline=False
            )
            embed.add_field(
                name="Step 3: Publish",
                value="1. Click File → Publish to Roblox\n"
                      "2. Choose 'Create new game' or update existing\n"
                      "3. Add detailed description and tags\n"
                      "4. Click 'Create' or 'Update' to publish",
                inline=False
            )
            
        elif topic == "gui":
            embed = discord.Embed(
                title="🖥️ Creating GUI Interfaces",
                color=discord.Color.purple()
            )
            embed.add_field(
                name="Step 1: Create ScreenGui",
                value="1. Go to StarterPlayer → StarterPlayerScripts\n"
                      "2. Insert a LocalScript\n"
                      "3. Create ScreenGui in PlayerGui\n"
                      "4. This will show on player's screen",
                inline=False
            )
            embed.add_field(
                name="Step 2: Add GUI Elements",
                value="1. Insert Frame for background\n"
                      "2. Add TextLabel for information display\n"
                      "3. Insert TextButton for interactions\n"
                      "4. Use ImageLabel for pictures/icons",
                inline=False
            )
            embed.add_field(
                name="Step 3: Script Interactions",
                value="1. Connect button click events\n"
                      "2. Update text labels with game data\n"
                      "3. Show/hide GUI elements as needed\n"
                      "4. Use TweenService for smooth animations",
                inline=False
            )
        else:
            embed = discord.Embed(
                title="❌ Tutorial Not Found",
                description=f"I don't have a tutorial for '{topic}'. Use `!tutorial` to see available topics.",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
            return
            
        await ctx.send(embed=embed)

    @commands.command(name='docs')
    async def documentation_links(self, ctx):
        """Quick access to official documentation"""
        embed = discord.Embed(
            title="📚 Official Documentation",
            description="Quick links to essential Roblox development docs:",
            color=discord.Color.green()
        )
        embed.add_field(
            name="🏠 Main Resources",
            value="• [Developer Hub](https://developer.roblox.com/)\n"
                  "• [API Reference](https://developer.roblox.com/en-us/api-reference)\n"
                  "• [Luau Documentation](https://luau-lang.org/)\n"
                  "• [Creator Dashboard](https://create.roblox.com/)",
            inline=False
        )
        embed.add_field(
            name="📖 Specific Guides",
            value="• [Scripting Tutorial](https://developer.roblox.com/en-us/learn-roblox/scripting)\n"
                  "• [Building Tutorial](https://developer.roblox.com/en-us/learn-roblox/building)\n"
                  "• [UI Design Guide](https://developer.roblox.com/en-us/articles/UI-Layout-and-Appearance)\n"
                  "• [DataStore Guide](https://developer.roblox.com/en-us/articles/Data-store)",
            inline=False
        )
        embed.add_field(
            name="🔧 Technical References",
            value="• [Services Reference](https://developer.roblox.com/en-us/api-reference/class/ServiceProvider)\n"
                  "• [RemoteEvents Guide](https://developer.roblox.com/en-us/articles/Remote-Functions-and-Events)\n"
                  "• [Security Best Practices](https://developer.roblox.com/en-us/articles/Security-Tactics-and-Cheat-Mitigation)\n"
                  "• [Performance Optimization](https://developer.roblox.com/en-us/articles/Improving-Performance)",
            inline=False
        )
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(ResourceCommands(bot))