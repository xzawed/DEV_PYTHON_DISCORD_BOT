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
import asyncio, discord
from discord.ext import commands

import mariadb
import Errlog

discord_token = mariadb.selmysql('TOKEN',('DISCORD','XZAWED#7332'))

bot = commands.Bot(command_prefix="!")

#  event decorator를 설정하고 on_ready function을 할당해줍니다.
#  on_ready event는 discord bot이 discord에 정상적으로 접속했을 때 실행됩니다.
@bot.event
async def on_ready():
    print('We have logged in as {}'.format(bot))
    #  여기서 client.user는 discord bot을 의미합니다. (제가 아닙니다.)
    print('Bot name: {}'.format(bot.user.name))
    #  여기서 client.user는 discord bot을 의미합니다. (제가 아닙니다.)
    print('Bot ID: {}'.format(bot.user.id))

#  event decorator를 설정하고 on_message function을 할당해줍니다.
'''
@bot.event
async def on_message(message):
    #  message란 discord 채널에 올라오는 모든 message를 의미합니다.
    #  따라서 bot이 보낸 message도 포함이되죠.
    #  아래 조건은 message의 author가 bot(=clinet.user)이라면 그냥 return으로 무시하라는 뜻입니다.
    if message.author == bot.user:
        return

    #  message를 보낸 사람이 bot이 아니라면 message가 hello로 시작하는 경우 채널에 Hello!라는 글자를 보내라는 뜻입니다.
    elif message.content.startswith('hello'):
        await message.channel.send('Hello!')
'''
#  커맨드별로 전부 다 선언을 해야 하는지 확인이 필요함.
@bot.command()
async def hello(ctx):
    await ctx.send("안녕하세요")

#  discord 에서는 한글 커맨드처리가 가능하다.
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
        await ctx.channel.send('명령어를 찾지 못했습니다')

# 위에서 설정한 client class를 token으로 인증하여 실행합니다.
try:
    mariadb.selmysql('TEMP', '실행')
    Errlog.saveLog('INFO')
    bot.run(discord_token)
except Exception :
    Errlog.saveLog('ERROR')
