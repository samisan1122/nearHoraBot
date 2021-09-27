process.env.NTBA_FIX_319 = 1;
const TelegramBot = require('node-telegram-bot-api');
const {NearTime} = require('./near');
const fs = require('fs');

fs.readFile('token.txt', 'utf8', function(err, token) {
  if (err) throw err;
  const bot = new TelegramBot(token, {polling: true});

  bot.on('message', (msg) => {
    if(msg.text.toString().toLowerCase().indexOf('neartime') === 0 && msg.text.toString().length === 8) {
      NearTime().then((resp) => bot.sendMessage(msg.chat.id, resp));
    }
  });
});
