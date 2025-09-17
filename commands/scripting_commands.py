import discord
from discord.ext import commands
import random

class ScriptingCommands(commands.Cog):
    """Lua scripting commands for Roblox development"""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='script')
    async def script_examples(self, ctx, script_type: str = None):
        """Get Lua scripting examples for Roblox"""
        if not script_type:
            embed = discord.Embed(
                title="📝 Lua Scripting Examples",
                description="Choose a script type to get examples:",
                color=discord.Color.purple()
            )
            embed.add_field(
                name="Available Types:",
                value="`!script basic` - Basic Lua syntax\n"
                      "`!script movement` - Player movement scripts\n"
                      "`!script gui` - GUI scripting examples\n"
                      "`!script tools` - Tool creation scripts\n"
                      "`!script events` - Event handling examples",
                inline=False
            )
            await ctx.send(embed=embed)
            return

        script_type = script_type.lower()
        
        if script_type == "basic":
            embed = discord.Embed(
                title="📝 Basic Lua Syntax",
                color=discord.Color.purple()
            )
            code = '''```lua
-- Variables
local playerName = "Developer"
local playerAge = 25
local isRobloxDev = true

-- Functions
local function greetPlayer(name)
    print("Hello, " .. name .. "!")
end

-- Conditional statements
if playerAge >= 18 then
    print("You can develop complex games!")
else
    print("Keep learning and practicing!")
end

-- Loops
for i = 1, 5 do
    print("Loop iteration: " .. i)
end

-- Tables
local inventory = {"Sword", "Shield", "Potion"}
for i, item in ipairs(inventory) do
    print("Item " .. i .. ": " .. item)
end
```'''
            embed.description = code
            
        elif script_type == "movement":
            embed = discord.Embed(
                title="🏃 Player Movement Scripts",
                color=discord.Color.purple()
            )
            code = '''```lua
-- Basic player movement script
local Players = game:GetService("Players")
local UserInputService = game:GetService("UserInputService")

local player = Players.LocalPlayer
local character = player.Character or player.CharacterAdded:Wait()
local humanoid = character:WaitForChild("Humanoid")

-- Jump boost
UserInputService.InputBegan:Connect(function(input, gameProcessed)
    if gameProcessed then return end
    
    if input.KeyCode == Enum.KeyCode.J then
        humanoid.JumpPower = 100  -- Boost jump power
        wait(0.1)
        humanoid.JumpPower = 50   -- Reset to normal
    end
end)

-- Speed boost
local function speedBoost()
    humanoid.WalkSpeed = 32  -- Faster walking
    wait(5)  -- Duration
    humanoid.WalkSpeed = 16  -- Back to normal
end
```'''
            embed.description = code
            
        elif script_type == "gui":
            embed = discord.Embed(
                title="🖥️ GUI Scripting Examples",
                color=discord.Color.purple()
            )
            code = '''```lua
-- Creating a simple GUI
local Players = game:GetService("Players")
local player = Players.LocalPlayer
local playerGui = player:WaitForChild("PlayerGui")

-- Create ScreenGui
local screenGui = Instance.new("ScreenGui")
screenGui.Name = "GameHUD"
screenGui.Parent = playerGui

-- Create Frame
local frame = Instance.new("Frame")
frame.Size = UDim2.new(0, 200, 0, 100)
frame.Position = UDim2.new(0, 10, 0, 10)
frame.BackgroundColor3 = Color3.new(0, 0, 0)
frame.BackgroundTransparency = 0.3
frame.Parent = screenGui

-- Create TextLabel
local label = Instance.new("TextLabel")
label.Size = UDim2.new(1, 0, 0.5, 0)
label.Position = UDim2.new(0, 0, 0, 0)
label.BackgroundTransparency = 1
label.Text = "Game Status"
label.TextColor3 = Color3.new(1, 1, 1)
label.Parent = frame

-- Create Button
local button = Instance.new("TextButton")
button.Size = UDim2.new(1, 0, 0.5, 0)
button.Position = UDim2.new(0, 0, 0.5, 0)
button.Text = "Click Me!"
button.Parent = frame

button.MouseButton1Click:Connect(function()
    label.Text = "Button Clicked!"
end)
```'''
            embed.description = code
            
        elif script_type == "tools":
            embed = discord.Embed(
                title="🔧 Tool Creation Scripts",
                color=discord.Color.purple()
            )
            code = '''```lua
-- Tool creation script (ServerScript in ServerScriptService)
local tool = Instance.new("Tool")
tool.Name = "Magic Wand"
tool.RequiresHandle = true

-- Create Handle
local handle = Instance.new("Part")
handle.Name = "Handle"
handle.Size = Vector3.new(1, 4, 1)
handle.Material = Enum.Material.Neon
handle.BrickColor = BrickColor.new("Bright blue")
handle.CanCollide = false
handle.Parent = tool

-- Tool functionality
tool.Activated:Connect(function()
    local player = tool.Parent.Parent  -- Get player
    if player:IsA("Player") then
        print(player.Name .. " used the magic wand!")
        
        -- Create sparkle effect
        local part = Instance.new("Part")
        part.Size = Vector3.new(2, 2, 2)
        part.Material = Enum.Material.Neon
        part.BrickColor = BrickColor.Random()
        part.CanCollide = false
        part.Anchored = true
        part.Position = handle.Position + Vector3.new(0, 5, 0)
        part.Parent = workspace
        
        -- Remove after 3 seconds
        game:GetService("Debris"):AddItem(part, 3)
    end
end)

-- Give tool to all players
game.Players.PlayerAdded:Connect(function(player)
    player.CharacterAdded:Connect(function(character)
        local newTool = tool:Clone()
        newTool.Parent = player.Backpack
    end)
end)
```'''
            embed.description = code
            
        elif script_type == "events":
            embed = discord.Embed(
                title="⚡ Event Handling Examples",
                color=discord.Color.purple()
            )
            code = '''```lua
-- Common Roblox events
local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")

-- Player events
Players.PlayerAdded:Connect(function(player)
    print(player.Name .. " joined the game!")
    
    player.CharacterAdded:Connect(function(character)
        print(player.Name .. " spawned!")
        
        local humanoid = character:WaitForChild("Humanoid")
        humanoid.Died:Connect(function()
            print(player.Name .. " died!")
        end)
    end)
end)

Players.PlayerRemoving:Connect(function(player)
    print(player.Name .. " left the game!")
end)

-- Touch events
local part = workspace.TouchPart  -- Assuming you have a part named TouchPart

part.Touched:Connect(function(hit)
    local humanoid = hit.Parent:FindFirstChild("Humanoid")
    if humanoid then
        local player = Players:GetPlayerFromCharacter(hit.Parent)
        if player then
            print(player.Name .. " touched the part!")
        end
    end
end)

-- RemoteEvent example
local remoteEvent = ReplicatedStorage:WaitForChild("RemoteEvent")

remoteEvent.OnServerEvent:Connect(function(player, data)
    print(player.Name .. " sent data: " .. tostring(data))
    
    -- Send back to all players
    remoteEvent:FireAllClients("Server response: " .. data)
end)
```'''
            embed.description = code
        else:
            embed = discord.Embed(
                title="❌ Unknown Script Type",
                description=f"I don't have examples for '{script_type}'. Use `!script` to see available types.",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
            return
            
        embed.set_footer(text="Copy and paste these scripts into Roblox Studio!")
        await ctx.send(embed=embed)

    @commands.command(name='function')
    async def lua_functions(self, ctx):
        """Learn about Lua functions in Roblox"""
        embed = discord.Embed(
            title="📋 Lua Functions Guide",
            color=discord.Color.green()
        )
        
        code = '''```lua
-- Function basics
local function addNumbers(a, b)
    return a + b
end

local result = addNumbers(5, 3)  -- Returns 8

-- Function with multiple returns
local function getPlayerInfo(player)
    return player.Name, player.UserId, player.AccountAge
end

local name, id, age = getPlayerInfo(game.Players.LocalPlayer)

-- Anonymous functions
local myFunction = function(x)
    return x * 2
end

-- Functions as arguments
local function processNumber(number, func)
    return func(number)
end

local doubled = processNumber(5, function(x) return x * 2 end)

-- Useful Roblox service functions
local Players = game:GetService("Players")
local TweenService = game:GetService("TweenService")

-- Custom utility functions
local function tweenPart(part, targetPosition, duration)
    local tweenInfo = TweenInfo.new(duration)
    local tween = TweenService:Create(part, tweenInfo, {Position = targetPosition})
    tween:Play()
    return tween
end

local function findNearestPlayer(position, maxDistance)
    local nearestPlayer = nil
    local shortestDistance = maxDistance or math.huge
    
    for _, player in pairs(Players:GetPlayers()) do
        if player.Character and player.Character:FindFirstChild("HumanoidRootPart") then
            local distance = (player.Character.HumanoidRootPart.Position - position).Magnitude
            if distance < shortestDistance then
                shortestDistance = distance
                nearestPlayer = player
            end
        end
    end
    
    return nearestPlayer, shortestDistance
end
```'''
        
        embed.description = code
        embed.add_field(
            name="💡 Tips:",
            value="• Use local functions for better performance\n"
                  "• Functions can return multiple values\n"
                  "• Pass functions as arguments for flexibility\n"
                  "• Create utility functions for reusable code",
            inline=False
        )
        await ctx.send(embed=embed)

    @commands.command(name='event')
    async def roblox_events(self, ctx):
        """Learn about Roblox events"""
        events_info = [
            {
                "title": "🎮 Player Events",
                "events": "PlayerAdded, PlayerRemoving, CharacterAdded, CharacterRemoving",
                "example": "Players.PlayerAdded:Connect(function(player) ... end)"
            },
            {
                "title": "👆 Input Events", 
                "events": "MouseButton1Click, KeyDown, TouchTap, InputBegan",
                "example": "button.MouseButton1Click:Connect(function() ... end)"
            },
            {
                "title": "🏃 Character Events",
                "events": "Touched, Died, HealthChanged, Jumping",
                "example": "part.Touched:Connect(function(hit) ... end)"
            },
            {
                "title": "🌐 Remote Events",
                "events": "OnServerEvent, OnClientEvent, FireServer, FireClient",
                "example": "remoteEvent.OnServerEvent:Connect(function(player, ...) ... end)"
            }
        ]
        
        event_info = random.choice(events_info)
        embed = discord.Embed(
            title=event_info["title"],
            color=discord.Color.orange()
        )
        embed.add_field(name="Common Events:", value=event_info["events"], inline=False)
        embed.add_field(name="Example Usage:", value=f"`{event_info['example']}`", inline=False)
        embed.set_footer(text="Use !script events for more detailed examples!")
        
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(ScriptingCommands(bot))