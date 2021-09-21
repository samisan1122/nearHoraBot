process.env.NTBA_FIX_319 = 1;
const TelegramBot = require('node-telegram-bot-api');
const {NearTime} = require('./near');

const token =  process.env.TELEGRAM_TOKEN || '1900259112:AAEbfnFynSHGTLjGsjjmo6lsepQbngxDNmQ';

const bot = new TelegramBot(token, {polling: true});

bot.on('message', (msg) => {
  if(msg.text.toString().toLowerCase().indexOf('neartime') === 0 && msg.text.toString().length === 8) {
    NearTime().then((resp) => bot.sendMessage(msg.chat.id, resp));
  }
});