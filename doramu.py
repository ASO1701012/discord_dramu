import discord

client = discord.Client()
discord_token = 'NjIzMDQ3MTQ5MjE4NjkzMTMw.XX8wDQ.TtU2czHIrZXxHGMclEkytTJ-lbA'
voice_channel_id = 623052067426140183
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    # 「おはよう」で始まるか調べる
    if message.content.startswith("おはよう"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            # メッセージを書きます
            m = "おはようございます" + message.author.name + "さん！"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await message.channel.send(m)


    if message.content.startswith("ドラム"):
        voice = await client.join_voice_channel(client.get_channel(voice_channel_id))
        player = voice.create_ffmpeg_player(doramu.mp3)
        player.start()


client.run(discord_token)
