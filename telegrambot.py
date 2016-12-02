#!/usr/bin/env python

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from urllib.request import urlopen

import subprocess

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    update.message.reply_text('Hi!, /help for help')
    print("Someone joined")


def help(bot, update):
    update.message.reply_text('/getIp - I will tell you my @IP\n/uptime - I will tell you my uptime')
    print("Someone wants help")

def getIp(bot, update):
    ip = urlopen('http://ip.42.pl/raw').read().decode('utf-8')
    update.message.reply_text(ip)
    print("Someone wants my ip")

def uptime(bot, update):
    update.message.reply_text(subprocess.getoutput("uptime"))
    print("Someone wants my uptime")

def echo(bot, update):
    update.message.reply_text(update.message.text)
    print(update.message.text)

def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("getIp", getIp))
    dp.add_handler(CommandHandler("uptime", uptime))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler([Filters.text], echo))


    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
