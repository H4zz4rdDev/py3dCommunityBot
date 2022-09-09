from twitchio.ext import commands


class ChatBot(commands.Bot):
    chatBot = None
    config = None

    def __init__(self, config):
        super().__init__(token=config['TWITCH']['accessToken'], prefix='?',
                         initial_channels=[config['TWITCH']['channel']])
        self.config = config

    def start(self):
        self.chatBot = ChatBot(self.config)
        self.chatBot.run()

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    @commands.command()
    async def info(self, ctx: commands.Context):
        await ctx.send(f'3D Challenge Community Bot - Version 0.0.1')
