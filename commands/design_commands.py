import discord
from discord.ext import commands
import random

class DesignCommands(commands.Cog):
    """Game design and mechanics commands"""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='gamedesign')
    async def game_design_tips(self, ctx, topic: str = None):
        """Get game design tips and best practices"""
        if not topic:
            embed = discord.Embed(
                title="🎨 Game Design Topics",
                description="Choose a topic to learn about:",
                color=discord.Color.gold()
            )
            embed.add_field(
                name="Available Topics:",
                value="`!gamedesign basics` - Core game design principles\n"
                      "`!gamedesign engagement` - Player engagement strategies\n"
                      "`!gamedesign monetization` - Monetization best practices\n"
                      "`!gamedesign progression` - Player progression systems\n"
                      "`!gamedesign balance` - Game balance principles",
                inline=False
            )
            await ctx.send(embed=embed)
            return

        topic = topic.lower()
        
        if topic == "basics":
            embed = discord.Embed(
                title="🎯 Core Game Design Principles",
                color=discord.Color.gold()
            )
            embed.add_field(
                name="1. Clear Objectives",
                value="• Players should always know what to do next\n"
                      "• Use tutorials and clear UI indicators\n"
                      "• Provide short-term and long-term goals",
                inline=False
            )
            embed.add_field(
                name="2. Intuitive Controls",
                value="• Keep controls simple and responsive\n"
                      "• Use familiar control schemes\n"
                      "• Provide control customization options",
                inline=False
            )
            embed.add_field(
                name="3. Balanced Difficulty",
                value="• Start easy, gradually increase difficulty\n"
                      "• Provide multiple difficulty options\n"
                      "• Avoid frustrating difficulty spikes",
                inline=False
            )
            
        elif topic == "engagement":
            embed = discord.Embed(
                title="🎮 Player Engagement Strategies",
                color=discord.Color.gold()
            )
            embed.add_field(
                name="🏆 Achievement Systems",
                value="• Create meaningful rewards for accomplishments\n"
                      "• Use badges and leaderboards\n"
                      "• Celebrate player milestones",
                inline=False
            )
            embed.add_field(
                name="👥 Social Features",
                value="• Enable player collaboration\n"
                      "• Add friend systems and teams\n"
                      "• Create competitive elements",
                inline=False
            )
            embed.add_field(
                name="🔄 Fresh Content",
                value="• Regular updates and events\n"
                      "• Seasonal content and themes\n"
                      "• User-generated content support",
                inline=False
            )
            
        elif topic == "monetization":
            embed = discord.Embed(
                title="💰 Monetization Best Practices",
                color=discord.Color.gold()
            )
            embed.add_field(
                name="✅ Good Practices",
                value="• Offer cosmetic items that don't affect gameplay\n"
                      "• Provide convenience items (faster travel, etc.)\n"
                      "• Create VIP/Premium memberships with benefits\n"
                      "• Fair and transparent pricing",
                inline=False
            )
            embed.add_field(
                name="❌ Avoid These",
                value="• Pay-to-win mechanics\n"
                      "• Excessive advertising\n"
                      "• Locking core features behind payments\n"
                      "• Predatory monetization targeting children",
                inline=False
            )
            embed.add_field(
                name="🎁 Free-to-Play Tips",
                value="• Give players enough free content to enjoy\n"
                      "• Use optional purchases to enhance experience\n"
                      "• Reward loyal free players",
                inline=False
            )
            
        elif topic == "progression":
            embed = discord.Embed(
                title="📈 Player Progression Systems",
                color=discord.Color.gold()
            )
            embed.add_field(
                name="🌟 Level Systems",
                value="• Clear XP requirements and rewards\n"
                      "• Unlock new content at each level\n"
                      "• Show progress visually\n"
                      "• Avoid excessive grinding",
                inline=False
            )
            embed.add_field(
                name="🛠️ Skill Trees",
                value="• Meaningful choices that affect gameplay\n"
                      "• Multiple viable build paths\n"
                      "• Option to reset/respec skills\n"
                      "• Clear skill descriptions",
                inline=False
            )
            embed.add_field(
                name="🏅 Achievement Progression",
                value="• Tiered achievement systems\n"
                      "• Both easy and challenging goals\n"
                      "• Progress tracking for long-term achievements\n"
                      "• Meaningful rewards for completion",
                inline=False
            )
            
        elif topic == "balance":
            embed = discord.Embed(
                title="⚖️ Game Balance Principles",
                color=discord.Color.gold()
            )
            embed.add_field(
                name="🎯 Risk vs Reward",
                value="• Higher risks should offer better rewards\n"
                      "• Avoid guaranteed wins or losses\n"
                      "• Multiple paths to success\n"
                      "• Balance effort with satisfaction",
                inline=False
            )
            embed.add_field(
                name="🔧 Playtesting",
                value="• Test with different player types\n"
                      "• Monitor player behavior and feedback\n"
                      "• Iterate based on data\n"
                      "• Balance for both new and experienced players",
                inline=False
            )
            embed.add_field(
                name="📊 Data-Driven Decisions",
                value="• Track player retention and engagement\n"
                      "• Monitor difficulty curves\n"
                      "• A/B test different mechanics\n"
                      "• Use analytics to guide balance changes",
                inline=False
            )
        else:
            embed = discord.Embed(
                title="❌ Unknown Topic",
                description=f"I don't have information about '{topic}'. Use `!gamedesign` to see available topics.",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
            return
            
        await ctx.send(embed=embed)

    @commands.command(name='mechanics')
    async def game_mechanics(self, ctx):
        """Get information about popular game mechanics"""
        mechanics = [
            {
                "name": "🎯 Collection Mechanics",
                "description": "Players gather items, resources, or collectibles",
                "examples": "Coins, gems, trading cards, rare items",
                "tips": "Make collecting satisfying with visual/audio feedback"
            },
            {
                "name": "🏗️ Building Mechanics",
                "description": "Players construct and customize structures",
                "examples": "House building, city planning, base construction",
                "tips": "Provide intuitive building tools and save systems"
            },
            {
                "name": "🎲 Chance Mechanics",
                "description": "Random elements that add excitement and replayability",
                "examples": "Loot boxes, critical hits, random events",
                "tips": "Balance randomness with player skill and strategy"
            },
            {
                "name": "🏃 Movement Mechanics",
                "description": "How players navigate the game world",
                "examples": "Parkour, flying, teleportation, vehicles",
                "tips": "Make movement feel responsive and fun"
            },
            {
                "name": "⚔️ Combat Mechanics",
                "description": "Systems for player vs player or player vs environment conflict",
                "examples": "Turn-based combat, real-time battles, strategy",
                "tips": "Ensure combat feels fair and skill-based"
            }
        ]
        
        mechanic = random.choice(mechanics)
        embed = discord.Embed(
            title=mechanic["name"],
            description=mechanic["description"],
            color=discord.Color.blue()
        )
        embed.add_field(name="Examples:", value=mechanic["examples"], inline=False)
        embed.add_field(name="💡 Design Tip:", value=mechanic["tips"], inline=False)
        embed.set_footer(text="Use !gamedesign for more comprehensive design guidance!")
        
        await ctx.send(embed=embed)

    @commands.command(name='ui')
    async def ui_design(self, ctx, element: str = None):
        """UI design guidelines for Roblox games"""
        if not element:
            embed = discord.Embed(
                title="🖥️ UI Design Guidelines",
                description="Get specific guidance for UI elements:",
                color=discord.Color.cyan()
            )
            embed.add_field(
                name="Available Elements:",
                value="`!ui buttons` - Button design principles\n"
                      "`!ui menus` - Menu layout and navigation\n"
                      "`!ui hud` - HUD and interface design\n"
                      "`!ui mobile` - Mobile-friendly design\n"
                      "`!ui accessibility` - Accessible design practices",
                inline=False
            )
            await ctx.send(embed=embed)
            return

        element = element.lower()
        
        if element == "buttons":
            embed = discord.Embed(
                title="🔘 Button Design Principles",
                color=discord.Color.cyan()
            )
            embed.add_field(
                name="✅ Good Button Design",
                value="• Clear, readable text with good contrast\n"
                      "• Adequate size for easy clicking/tapping\n"
                      "• Visual feedback on hover/click\n"
                      "• Consistent styling throughout the game",
                inline=False
            )
            embed.add_field(
                name="📱 Mobile Considerations",
                value="• Minimum 44x44 pixel touch targets\n"
                      "• Extra spacing between buttons\n"
                      "• Consider thumb reach on large screens\n"
                      "• Test on different screen sizes",
                inline=False
            )
            
        elif element == "menus":
            embed = discord.Embed(
                title="📋 Menu Design Guidelines",
                color=discord.Color.cyan()
            )
            embed.add_field(
                name="🗂️ Organization",
                value="• Group related options together\n"
                      "• Use clear hierarchy and categories\n"
                      "• Limit options per screen (5-9 items)\n"
                      "• Provide search for large lists",
                inline=False
            )
            embed.add_field(
                name="🔄 Navigation",
                value="• Clear back/cancel buttons\n"
                      "• Breadcrumb navigation for deep menus\n"
                      "• Consistent navigation patterns\n"
                      "• Quick access to important features",
                inline=False
            )
            
        elif element == "hud":
            embed = discord.Embed(
                title="🎮 HUD Design Guidelines",
                color=discord.Color.cyan()
            )
            embed.add_field(
                name="📍 Positioning",
                value="• Keep important info in safe zones\n"
                      "• Use screen corners and edges effectively\n"
                      "• Avoid blocking gameplay view\n"
                      "• Consider different screen ratios",
                inline=False
            )
            embed.add_field(
                name="📊 Information Display",
                value="• Show only essential information\n"
                      "• Use icons with text labels\n"
                      "• Color-code different types of data\n"
                      "• Update information in real-time",
                inline=False
            )
            
        elif element == "mobile":
            embed = discord.Embed(
                title="📱 Mobile-Friendly Design",
                color=discord.Color.cyan()
            )
            embed.add_field(
                name="👆 Touch Targets",
                value="• Minimum 44x44 pixels for buttons\n"
                      "• Leave space between interactive elements\n"
                      "• Use swipe gestures appropriately\n"
                      "• Avoid hover-dependent interactions",
                inline=False
            )
            embed.add_field(
                name="📺 Screen Adaptation",
                value="• Design for multiple aspect ratios\n"
                      "• Scale UI elements appropriately\n"
                      "• Test on phones and tablets\n"
                      "• Consider landscape and portrait modes",
                inline=False
            )
            
        elif element == "accessibility":
            embed = discord.Embed(
                title="♿ Accessible Design Practices",
                color=discord.Color.cyan()
            )
            embed.add_field(
                name="🎨 Visual Accessibility",
                value="• High contrast between text and background\n"
                      "• Don't rely solely on color to convey information\n"
                      "• Use clear, readable fonts\n"
                      "• Provide alternative text for images",
                inline=False
            )
            embed.add_field(
                name="🎵 Audio Accessibility",
                value="• Include visual indicators for audio cues\n"
                      "• Provide subtitle options\n"
                      "• Use both audio and visual feedback\n"
                      "• Allow volume control",
                inline=False
            )
        else:
            embed = discord.Embed(
                title="❌ Unknown UI Element",
                description=f"I don't have guidelines for '{element}'. Use `!ui` to see available options.",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
            return
            
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(DesignCommands(bot))