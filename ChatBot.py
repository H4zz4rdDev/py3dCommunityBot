from twitchio.ext import commands


class ChatBot(commands.Bot):
    chatBot = None
    config = None
    adminList = None

    def __init__(self, config):
        super().__init__(token=config['TWITCH']['accessToken'], prefix='?',
                         initial_channels=[config['TWITCH']['channel']])
        self.config = config
        self.adminList = config["MAIN"]["adminList"]

    def start(self):
        self.chatBot = ChatBot(self.config)
        self.chatBot.run()

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    @commands.command()
    async def info(self, ctx: commands.Context):
        await ctx.send(f'3D Challenge Community Bot - Version 0.0.1')

    @commands.command()
    async def join(self, ctx: commands.Context):
        await ctx.send(f'{self.nick} du bist dabei! Yeahh!')

    @commands.command()
    async def create(self, ctx: commands.Context):
        if not self.checkIfUserIsAdmin(ctx.author.name):
            await ctx.send(f'You need admin rights for this command!')
        else:
            await ctx.send(f'Challenge created!')

    def checkIfUserIsAdmin(self, username):
        for adminName in self.config['MAIN']['adminList'].split(','):
            print(f'User: {username} - {adminName}')
            if username == adminName:
                return True
        return False
