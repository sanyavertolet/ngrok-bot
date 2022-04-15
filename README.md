# Ngrok bot

Simple telegram bot to turn [ngrok](https://ngrok.com/) on and off as well as to get it's address in order to use ssh without white IP address.
## Installaion
1. Install ngrok
2. Configure ngrok with `~/.ngrok2/ngrok.yml` like that:
```
authtoken: YOUR_NGROK_TOKEN
console_ui: false
log_level: info
log: path/to/ngrok/logs

tunnels:
  ssh:
    addr: 22
    proto: tcp
    auth: "USERNAME:PASSWORD"
```
3. Clone this repo
4. Enjoy.

Do not forget to configure the bot with `config.json`

## Usage:
 * `make run` - run bot in foreground.
 * `make runbg` - run bot in background. PID is saved to `pid` file
 * `make stop` - stop bot that is running in background by PID from `pid` file. `pid` file is deleted.
 * `make clean` - remove all log files as well as `pid` file.
 * `make configure` - create `config.json` template file. `config.json` is needed to use the bot.
 * `make install` - install dependencies from `requirements.txt` file.

## config.json
```
{
    "token": "<YOUR_TELEGRAM_TOKEN>",
    "adm_id": <YOUR_TELEGRAM_ID>,
    "path_to_ngrok_log": "path/to/ngrok/logs"
}
```
`token` - telegram bot token that you should get from [BotFather](https://t.me/BotFather).
`adm_id` - your telegram id that you should get from [IDBot](https://t.me/username_to_id_bot)
`path_to_ngrok_log` - path to ngrok logs
