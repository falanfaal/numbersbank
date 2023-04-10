import discord
from discord import Webhook
import asyncio
import datetime
import aiohttp

bot = discord.Bot(intents = discord.Intents().all())

webhookurl = "https://discord.com/api/webhooks/1094914855116476450/0wue8Btp2izLYm4cySc6KdDG2ncO6DL2TmPOi9eJ2_uprpoU6XM9ohNhAqOiwOFL1QLx "

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

#@commands.has_role('Staff IDNS')
@bot.message_command(name="Save Deposit")
async def deposited(ctx, message: discord.Message):
    def check(m: discord.Message):
        if m.author == ctx.author : return m.content
    await ctx.respond(f"Masukan nominal Depositmu!", ephemeral=True)
    try:
        amount = await bot.wait_for("message", check = check, timeout=20) # 30 seconds to reply
    except asyncio.TimeoutError:
        await ctx.respond("Pertanyaan tidak dijawab, Ulangi!")
    channel = bot.get_channel(ctx.channel.id) # Channel ID
    msg = await channel.fetch_message(amount.id) 
    await msg.delete() 
    await ctx.respond(f"Masukan nominal Tersediamu!", ephemeral=True)
    try:
        haveamount = await bot.wait_for("message", check = check, timeout=20) # 30 seconds to reply
    except asyncio.TimeoutError:
        await ctx.respond("Pertanyaan tidak dijawab, Ulangi!")
    msg = await channel.fetch_message(haveamount.id) 
    await msg.delete()
    embed = discord.Embed(title=f"NUMBERS BANK RECEIPT\n====================\nDeposit Sukses", color=discord.Color.green())
    embed.add_field(name=f"Telah mendeposit sebanyak :", value=f"{amount.content}", inline=True)
    embed.add_field(name=f"Memiliki sebanyak :", value=f"{haveamount.content} ", inline=True)
    embed.add_field(name=f"Lihat pesan lewat link dibawah ini", value=f"[Jump!]({message.jump_url})", inline=True)
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.display_avatar)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text='💰')
    async with aiohttp.ClientSession() as sess: 
        webhook = Webhook.from_url(webhookurl,session=sess) 
        try : 
            await webhook.send(embed=embed)
            await ctx.respond("Webhook terkirim!")
        except : ctx.respond("Webhook tidak dapat terkirim, mohon mengulang.")

@bot.message_command(name="Save Withdraw")
async def withdrawed(ctx, message: discord.Message):
    def check(m: discord.Message):
        if m.author == ctx.author : return m.content
    await ctx.respond(f"Masukan nominal Withdrawmu!", ephemeral=True)
    try:
        amount = await bot.wait_for("message", check = check, timeout=20) # 30 seconds to reply
    except asyncio.TimeoutError:
        await ctx.respond("Pertanyaan tidak dijawab, Ulangi!")
    channel = bot.get_channel(ctx.channel.id) # Channel ID
    msg = await channel.fetch_message(amount.id) 
    await msg.delete() 
    await ctx.respond(f"Masukan nominal Tersediamu!", ephemeral=True)
    try:
        haveamount = await bot.wait_for("message", check = check, timeout=20) # 30 seconds to reply
    except asyncio.TimeoutError:
        await ctx.respond("Pertanyaan tidak dijawab, Ulangi!")
    msg = await channel.fetch_message(haveamount.id) 
    await msg.delete() 
    embed = discord.Embed(title=f"NUMBERS BANK RECEIPT\n====================\nWithdraw Sukses", color=discord.Color.red())
    embed.add_field(name=f"Telah mengambil sebanyak :", value=f"{amount.content}", inline=True)
    embed.add_field(name=f"Memiliki sebanyak :", value=f"{haveamount.content} ", inline=True)
    embed.add_field(name=f"Lihat pesan lewat link dibawah ini", value=f"[Jump!]({message.jump_url})", inline=True)
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.display_avatar)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text='💰')
    async with aiohttp.ClientSession() as sess: 
        webhook = Webhook.from_url(webhookurl,session=sess) 
        try : 
            await webhook.send(embed=embed)
            await ctx.respond("Webhook terkirim!")
        except : ctx.respond("Webhook tidak dapat terkirim, mohon mengulang.")

bot.run("MTA5NDg1OTc4MjUwNDA3MTIwOA.GGcut5.gWDX9jkxBb2BwxRLRtmVquF9OnE1gJ6O9OWVtA")