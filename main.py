import discord

client = discord.Client()
discord_token = 'NjIzMDQ3MTQ5MjE4NjkzMTMw.XX8wDQ.TtU2czHIrZXxHGMclEkytTJ-lbA'

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content.startswith("おはよう"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            # メッセージを書きます
            m = "おはようございます" + message.author.name + "さん！"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await message.channel.send(m)


    voice = await VoiceChannel.connect(623074022661423114)
    if message.content == ("bgm"):
        voice.play(discord.FFmpegPCMAudio('test.mp3'))

client.run(discord_token)
