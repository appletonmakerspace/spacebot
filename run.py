from slackbot.bot import Bot
from slackbot.bot import listen_to
from slackbot.bot import respond_to
import socket

help_text = '''
!help - This help.\n
!internet - Check if the Makerspace is online.\n
'''

@listen_to('!help')
def help(message):
    message.send(help_text)

@listen_to('!internet')
def internet_status(message):
    try:
        host = socket.gethostbyname('appletonmakerspace.asuscomm.com')
        port = 8443
        socket.create_connection((host, port), 1)
        message.send(":smile: Makerspace is Online :smile:")
    except:
        message.send(":no_entry_sign: Makerspace is Offline :( :no_entry_sign:")

def main():
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    main()
