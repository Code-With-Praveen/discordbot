import discord
from discord.ext import commands
from discord.ext import *
from discord import *
from discord import FFmpegPCMAudio
from cred import *
import requests






intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents )

#intents = discord.Intents.default()
#intents.message_content = True
#
@bot.event
async def on_ready() :
    print('Bot logged in')
    print('----------------@@@@@@@@@@@@@@@@@@@@@@@@--------------------------')
@bot.command()
async def hi(ctx):
    await ctx.send('Hello')
@bot.command()
async def hru(ctx):
    await ctx.send('''How Can I Help 
                   Yooooou''')
@bot.command()
async def Hello(ctx):
    await ctx.send("May I help You")
    
@bot.command()
async def list(ctx):
    await ctx.send('''hi
hru
hello 
list - list of Commands''')

   # send message whn someone join 
@bot.event
async def on_member_join(member) :
    channel = bot.get_channel(1008748431222771712)
    await channel.send('hello')
# send message whn someone leves 
@bot.event
async def on_member_remove(member) :
    channel = bot.get_channel(1008748431222771712)
    await channel.send('Goodbye')
 # join a voice hannel  
 
@bot.command(pass_context = True)

async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice =  await channel.connect()
        source = FFmpegPCMAudio('pasoori.mp3')
        player = voice.play(source)
    else:
        await ctx.send('Kindly join a voice channel to run this command')
        
# leave a voice channel
@bot.command(pass_context = True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send ('I left the voice chat')
    else:
        await ctx.send('I an not in a voice chat')
        
        
@bot.command(pass_context = True)
async def pause(ctx):
        voice = discord.utils.get(ctx.voice_client,guild = ctx.guild)
        if voice.is_playing():
            voice.paused()
        else:
            await bot.send('No Audio Playing')
        
@bot.command(pass_context = True)
async def resume(ctx):
    voice = discord.utils.get(ctx.voice_client,guild = ctx.guild)
    if voice.is_paused():
        voice.play()
    else:
        await bot.send('No Audio is playing')
bot.run(token)