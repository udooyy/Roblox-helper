#!/usr/bin/env python3
"""
Setup script for Roblox Helper Bot
This script helps configure the bot for first-time use
"""

import os
import sys

def create_env_file():
    """Create .env file if it doesn't exist"""
    if os.path.exists('.env'):
        print("✅ .env file already exists")
        return
    
    if not os.path.exists('.env.example'):
        print("❌ .env.example file not found")
        return
    
    # Copy .env.example to .env
    with open('.env.example', 'r') as example:
        content = example.read()
    
    with open('.env', 'w') as env_file:
        env_file.write(content)
    
    print("✅ Created .env file from template")
    print("⚠️  Please edit .env file and add your Discord bot token")

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        print(f"   Current version: {sys.version}")
        return False
    print(f"✅ Python version: {sys.version.split()[0]}")
    return True

def install_dependencies():
    """Install required dependencies"""
    print("📦 Installing dependencies...")
    try:
        import subprocess
        result = subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Dependencies installed successfully")
        else:
            print("❌ Failed to install dependencies")
            print(result.stderr)
            return False
    except Exception as e:
        print(f"❌ Error installing dependencies: {e}")
        return False
    return True

def check_structure():
    """Check if all required files and directories exist"""
    required_files = [
        'bot.py',
        'requirements.txt',
        '.env.example',
        'commands/__init__.py',
        'commands/help_commands.py',
        'commands/scripting_commands.py',
        'commands/design_commands.py',
        'commands/resource_commands.py'
    ]
    
    missing_files = []
    for file_path in required_files:
        if not os.path.exists(file_path):
            missing_files.append(file_path)
    
    if missing_files:
        print("❌ Missing required files:")
        for file_path in missing_files:
            print(f"   - {file_path}")
        return False
    
    print("✅ All required files present")
    return True

def main():
    """Main setup function"""
    print("🎮 Roblox Helper Bot Setup")
    print("=" * 30)
    
    # Check Python version
    if not check_python_version():
        return
    
    # Check file structure
    if not check_structure():
        return
    
    # Install dependencies
    if not install_dependencies():
        return
    
    # Create .env file
    create_env_file()
    
    print("\n🎉 Setup completed!")
    print("\nNext steps:")
    print("1. Edit .env file and add your Discord bot token")
    print("2. Invite your bot to a Discord server")
    print("3. Run: python bot.py")
    print("\nFor help creating a Discord bot:")
    print("https://discord.com/developers/applications")

if __name__ == "__main__":
    main()