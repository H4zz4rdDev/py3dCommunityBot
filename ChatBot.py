from twitchio.ext import commands
from CommunityEvent import CommunityEvent


class ChatBot(commands.Bot):
    chatBot = None
    config = None
    adminList = None
    currentEvent = None

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
        await ctx.send(f'3D Challenge Community Bot - Version 0.0.1 - by C64Gamer')

    @commands.command()
    async def status(self, ctx: commands.Context):
        await ctx.send(f'Thema: {self.currentEvent.eventName} - TimeLeft: {self.currentEvent.timeInMinutes} Min')

    @commands.command()
    async  def test(self, ctx, arg):
        print(arg)

    @commands.command()
    async def join(self, ctx: commands.Context):
        await ctx.send(f'{ctx.author.name} du bist dabei! Yeahh!')

    @commands.command()
    async def create(self, ctx: commands.Context, name, time):
        if not self.checkIfUserIsAdmin(ctx.author.name):
            await ctx.send(f'You need admin rights for this command!')
            return

        if not isinstance(name, str):
            return

        if not isinstance(int(time), int):
            return

        if self.currentEvent is not None:
            await ctx.send(f'There is already an event running!')
        else:
            self.currentEvent = CommunityEvent(eventName=name, timeInMinutes=int(time))
            await ctx.send(f'Challenge created!')

    def checkIfUserIsAdmin(self, username):
        for adminName in self.adminList.split(','):
            if username == adminName:
                return True
        return False
