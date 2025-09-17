# 🚀 Quick Start Guide

## Option 1: Automated Setup (Recommended)

```bash
python setup.py
```

This will:
- Check Python version
- Install dependencies
- Create .env file
- Verify file structure

## Option 2: Manual Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Create environment file:**
   ```bash
   cp .env.example .env
   ```

3. **Edit .env and add your Discord token:**
   ```
   DISCORD_TOKEN=your_actual_bot_token_here
   COMMAND_PREFIX=!
   ```

## Getting a Discord Bot Token

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application" and give it a name
3. Go to "Bot" section
4. Click "Add Bot"
5. Copy the token and paste it in your .env file
6. Under "Privileged Gateway Intents", enable "Message Content Intent"

## Inviting the Bot to Your Server

1. In the Discord Developer Portal, go to OAuth2 → URL Generator
2. Select scopes: `bot` and `applications.commands`
3. Select permissions:
   - Send Messages
   - Embed Links
   - Read Message History
   - Use Slash Commands
4. Copy the generated URL and open it in your browser
5. Select your server and authorize the bot

## Running the Bot

```bash
python bot.py
```

You should see:
```
INFO:bot:Roblox Helper Bot#1234 has connected to Discord!
INFO:bot:Bot is ready to help with Roblox game development!
```

## Testing the Bot

In your Discord server, try:
- `!help` - Show all commands
- `!about` - Information about the bot
- `!script basic` - Get basic Lua examples
- `!gamedesign basics` - Get game design tips

## Troubleshooting

**ModuleNotFoundError**: Run `pip install -r requirements.txt`

**Invalid Discord token**: Check your .env file and bot token

**Bot not responding**: Ensure "Message Content Intent" is enabled

**Permission errors**: Check bot permissions in your Discord server

## What's Next?

- Use `!help` to explore all available commands
- Check `examples.py` for command usage examples
- Read the full `README.md` for detailed documentation
- Join the Roblox developer community for support!