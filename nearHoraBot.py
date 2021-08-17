#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.

import logging

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from datetime import datetime, timezone, timedelta

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )

def hora(update: Update, context: CallbackContext) -> None:
    data_e_hora_atuais = datetime.now()

    diferenca_Near_Time = timedelta(hours=-4)
    fuso_horario_Near_Time = timezone(diferenca_Near_Time)
    hora_data_Near_Time = data_e_hora_atuais.astimezone(fuso_horario_Near_Time)
    data_e_hora_em_texto_Near_Time = hora_data_Near_Time.strftime("%d/%m/%Y, %H:%M:%S")

    diferenca_berlim = timedelta(hours=2)
    fuso_horario_berlim = timezone(diferenca_berlim)
    hora_data_berlim = data_e_hora_atuais.astimezone(fuso_horario_berlim)
    data_e_hora_em_texto_berlim = hora_data_berlim.strftime("%d/%m/%Y, %H:%M:%S")

    diferenca_portugual = timedelta(hours=1)
    fuso_horario_portugual = timezone(diferenca_portugual)
    hora_data_portugual = data_e_hora_atuais.astimezone(fuso_horario_portugual)
    data_e_hora_em_texto_portugual = hora_data_portugual.strftime("%d/%m/%Y, %H:%M:%S")

    texto = "NEAR TIME > " + data_e_hora_em_texto_Near_Time + "\n\nLisboa > " + data_e_hora_em_texto_portugual + "\n\nBerlim > " + data_e_hora_em_texto_berlim
    update.message.reply_text(texto)


def main() -> None:
    updater = Updater("1902658014:AAGo4EPGOQUyu-Fa1VfwjaC7bC-tZIyd9IE")

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("neartime", hora))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
