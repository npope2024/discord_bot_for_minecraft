import discord
import subprocess

# discord client
intent = discord.Intents.default()
intent.message_content = True
client = discord.Client(intents=intent)

# set channel ids
requestsId = [put_the_channel_id_of_your_requests_channel_here]
statusId = [put_the_channel_id_of_your_status_channel_here]

# create a new event
@client.event
async def on_ready():
    print("bot alive")

# listen for specific messages
@client.event
async def on_message(message):
    # only check messages sent in the requests channel
    if message.channel.id == requestsId:
        # if "/up" was in the message, bring up the server
        if "/up" in message.content:
            process = subprocess.Popen([[put_your_path_to_your_up_sh_here]], stdout=subprocess.PIPE)
            while True:
                output = process.stdout.readline()
                if process.poll() is not None and output == b'':
                    break
                if output:
                    bot_message = output.strip().decode()
                    # send if the server is up in the status channel,
                    # any other output gets sent to the requests channel
                    if ":arrow" in bot_message:
                        await client.get_channel(int(statusId)).send(bot_message)
                    else:
                        await message.channel.send(bot_message)
        elif "/down" in message.content:
            # same as the "/up" but using down.sh rather than up.sh
            process = subprocess.Popen([[put_your_path_to_your_down_sh_here]], stdout=subprocess.PIPE)
            while True:
                output = process.stdout.readline()
                if process.poll() is not None and output == b'':
                    break
                if output:
                    bot_message = output.strip().decode()
                    if ":arrow" in bot_message:
                        await client.get_channel(int(statusId)).send(bot_message)
                    else:
                        await message.channel.send(bot_message)

# run the bot
bot = "[put_your_discord_bot_id_here]"
client.run(bot)