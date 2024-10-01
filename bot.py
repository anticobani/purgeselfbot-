
    def ui():
        print()
        print()
        print("[-] User Logged In: {0} [-]".format(client.user).center(width))
        print("[-] ID = {0} [-]".format(client.user.id).center(width))
        print()
        print()
    ui()

@client.event
async def on_message(message):
    if message.author == client.user:
        commands = []
        z = 0
        for index, a in enumerate(message.content):
            if a == " ":
                commands.append(message.content[z:index])
                z = index + 1
        commands.append(message.content[z:])
        channel = message.channel

        if commands[0] == '$': # Set custom command to clear messages here!
                    if len(commands) == 1:
                        async for msg in channel.history(limit=1000):
                            if msg.author == client.user:
                                try:
                                    await msg.delete()
                                except Exception as x:
                                    pass

        if commands[0] == 'cleardms': # Set custom command to clear all dms here!
            for channel in client.private_channels:
                if isinstance(channel, discord.DMChannel):
                    async for msg in channel.history(limit=10000):
                        try:
                            if msg.author == client.user:
                                await msg.delete()
                                print(msg)
                        except:
                             pass

@client.event
async def on_message_delete(message):
    if message.author.id == client.user.id:
        try:
            await print(f"Script Deleted = '{message.content}' in {message.channel}")
        except Exception as x:
            pass

# Bot Start
