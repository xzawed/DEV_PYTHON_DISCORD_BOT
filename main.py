#  샘플 Python 스크립트입니다.
#  Shift+F10을(를) 눌러 실행하거나 내 코드로 바꿉니다.
#  클래스, 파일, 도구 창, 액션 및 설정을 어디서나 검색하려면 Shift 두 번을(를) 누릅니다.
#  def print_hi(name):
    #  스크립트를 디버그하려면 하단 코드 줄의 중단점을 사용합니다.
#    print(f'Hi, {name}')  # 중단점을 전환하려면 Ctrl+F8을(를) 누릅니다.

#  스크립트를 실행하려면 여백의 녹색 버튼을 누릅니다.
#  if __name__ == '__main__':
#      print_hi('PyCharm')
#   https://www.jetbrains.com/help/pycharm/에서 PyCharm 도움말 참조
import discord
import discord_set

#  discord_token = discord_set.xzawed_token
discord_token = discord_set.selmysql('TOKEN')

#  discord Client class를 생성합니다.
client = discord.Client()

#  event decorator를 설정하고 on_ready function을 할당해줍니다.
#  on_ready event는 discord bot이 discord에 정상적으로 접속했을 때 실행됩니다.
@client.event
async def on_ready():
    print('We have logged in as {}'.format(client))
    #  여기서 client.user는 discord bot을 의미합니다. (제가 아닙니다.)
    print('Bot name: {}'.format(client.user.name))
    #  여기서 client.user는 discord bot을 의미합니다. (제가 아닙니다.)
    print('Bot ID: {}'.format(client.user.id))

#  event decorator를 설정하고 on_message function을 할당해줍니다.
@client.event
async def on_message(message):
    #  message란 discord 채널에 올라오는 모든 message를 의미합니다.
    #  따라서 bot이 보낸 message도 포함이되죠.
    #  아래 조건은 message의 author가 bot(=clinet.user)이라면 그냥 return으로 무시하라는 뜻입니다.
    if message.author == client.user:
        return

    #  message를 보낸 사람이 bot이 아니라면 message가 hello로 시작하는 경우 채널에 Hello!라는 글자를 보내라는 뜻입니다.
    elif message.content.startswith('hello'):
        await message.channel.send('Hello!')



#  command를 이용하여 동작하는것을 구현
'''

@client.message_command()
async def square(ctx, arg):
    #  this is the text that follows the command
    print(arg)
    #  ctx.send sends text in chat
    await ctx.send(int(arg) ** 2)

@client.message_command()
async def scrabblepoints(ctx, arg):
    #  Key for point values of each letter
    score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
             
         "x": 8, "z": 10}
    points = 0
    #  Sum the points for each letter
    for c in arg:
        points += score[c]
    await ctx.send(points)

'''

# 위에서 설정한 client class를 token으로 인증하여 실행합니다.
client.run(discord_token)
