#  샘플 Python 스크 립트 입니다.
#  Shift+F10을(를) 눌러 실행 하거나 내 코드로 바꿉 니다.
#  클래스, 파일, 도구 창, 액션 및 설정을 어디 서나 검색 하려면 Shift 두 번을(를) 누릅 니다.
#  def print_hi(name):
#  스크 립트를 디버그 하려면 하단 코드 줄의 중단점 을 사용 합니다.
#    print(f'Hi, {name}')  # 중단점 을 전환 하려면 Ctrl+F8을(를) 누릅 니다.

#  스크 립트 를 실행 하려면 여백의 녹색 버튼을 누릅 니다.
#  if __name__ == '__main__':
#      print_hi('PyCharm')
#   https://www.jetbrains.com/help/pycharm/에서 PyCharm 도움말 참조
#  import asyncio, discord
from discord.ext import commands

from mariadb import *

import Errlog

db = MYSQL
discord_token = db.selmysql(self=db, opt='TOKEN', data=('DISCORD', 'XZAWED#7332'))

bot = commands.Bot(command_prefix="!")

#  event decorator 를 설정 하고 on_ready function 을 할당해 줍니다.
#  on_ready event 는 discord bot 이 discord 에 정상적 으로 접속 했을 때 실행 됩니다.


@bot.event
async def on_ready():
    print('We have logged in as {}'.format(bot))
    #  여기서 client.user 는 discord bot 을 의미 합니다. (제가 아닙 니다.)
    print('Bot name: {}'.format(bot.user.name))
    #  여기서 client.user 는 discord bot 을 의미 합니다. (제가 아닙 니다.)
    print('Bot ID: {}'.format(bot.user.id))

#  event decorator 를 설정 하고 on_message function 을 할당해 줍니다.
'''
@bot.event
async def on_message(message):
    #  message 란 discord 채널에 올라 오는 모든 message 를 의미 합니다.
    #  따라서 bot 이 보낸 message 도 포함 이되죠.
    #  아래 조건은 message 의 author 가 bot(=clinet.user)이라면 그냥 return 으로 무시 하라는 뜻 입니다.
    if message.author == bot.user:
        return

    #  message 를 보낸 사람이 bot 이 아니 라면 message 가 hello 로 시작 하는 경우 채널에 Hello!라는 글자를 보내 라는 뜻 입니다.
    elif message.content.startswith('hello'):
        await message.channel.send('Hello!')
'''
#  커맨드 별로 전부 다 선언을 해야 하는지 확인이 필요함.


@bot.command()
async def hello(ctx):
    await ctx.send("안녕하세요")

#  discord 에서는 한글 커맨드 처리가 가능 하다.


@bot.command()
async def 구글(ctx, *args):
    parameter = '+'.join(args)
    url = "https://www.google.com/search?q="
    await ctx.reply(f'구글 검색 : {url+parameter}')


@bot.command()
async def 네이버(ctx, *args):
    parameter = '+'.join(args)
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query="
    await ctx.reply(f'네이버 검색 : {url+parameter}')


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.channel.send('명령어 를 찾지 못했 습니다')

#  위에서 설정한 client class 를 token 으로 인증 하여 실행 합니다.
try:
    db.selmysql(self=db, opt='TEMP', data='실행')
    Errlog.savelog('INFO')
    bot.run(discord_token)
except Exception:
    Errlog.savelog('ERROR')
