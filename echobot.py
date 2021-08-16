#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.

import logging

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from datetime import datetime, timezone, timedelta


# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Ajuda!')

def hora(update: Update, context: CallbackContext) -> None:
    data_e_hora_atuais = datetime.now()

    diferenca_sao_paulo = timedelta(hours=-3)
    fuso_horario_sao_paulo = timezone(diferenca_sao_paulo)
    hora_data_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario_sao_paulo)
    data_e_hora_em_texto_sao_paulo = hora_data_sao_paulo.strftime("%d/%m/%Y, %H:%M:%S")

    diferenca_portugual = timedelta(hours=1)
    fuso_horario_portugual = timezone(diferenca_portugual)
    hora_data_portugual = data_e_hora_atuais.astimezone(fuso_horario_portugual)
    data_e_hora_em_texto_portugual = hora_data_portugual.strftime("%d/%m/%Y, %H:%M:%S")

    texto = "Sao Paulo -> " + data_e_hora_em_texto_sao_paulo + "\nPortugual -> " + data_e_hora_em_texto_portugual
    update.message.reply_text(texto)

def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("1900259112:AAEbfnFynSHGTLjGsjjmo6lsepQbngxDNmQ")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("hora", hora))

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
