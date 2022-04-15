"""Telegram bot that allows to activate and deactivate ngrok."""
import json
import logging
import os
import subprocess
import time

from telegram import Update
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackContext,
)

log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
date_format = "%Y-%m-%d %H:%M:%S"

logging.basicConfig(format=log_format, datefmt=date_format, level=logging.INFO)
logger = logging.getLogger(__name__)

config = {}
adm_id = -1
proc = 0


def get_url() -> str:
    """Get current ngrok url from ngrox logs."""
    with open(config["path_to_ngrok_log"], "r") as f:
        logs = f.read()
    url = logs.split("tcp://")[-1].split()[0]
    return url


def start(update: Update, context: CallbackContext) -> None:
    """Start ngrok if not running."""
    if update.effective_user.id == adm_id:
        global proc
        if proc == 0:
            proc = subprocess.Popen(["ngrok", "start", "ssh"])
            time.sleep(2)
            update.message.reply_text(f"Started on {get_url()}")
        else:
            update.message.reply_text("Already in run")


def stop(update: Update, context: CallbackContext) -> None:
    """Stop ngrok if running."""
    if update.effective_user.id == adm_id:
        global proc
        if proc != 0:
            proc.kill()
            proc = 0
            update.message.reply_text("Killed")
            os.remove(config["path_to_ngrok_log"])
        else:
            update.message.reply_text("Nothing to stop")


def status(update: Update, context: CallbackContext) -> None:
    """Get ngrok status."""
    if update.effective_user.id == adm_id:
        global proc
        if proc == 0:
            update.message.reply_text("Turned off")
        else:
            update.message.reply_text(f"Listening on {get_url()}")


def main() -> None:
    """Configure and launch bot."""
    global config
    try:
        with open("config.json") as config_file:
            config = json.load(config_file)
    except FileNotFoundError:
        raise FileNotFoundError(
            "Make sure you have config.json in your working directory."
        )
    logger.debug(f"Found config.json: {config}")
    global adm_id
    adm_id = int(config["adm_id"])
    logger.info(f"Admin ID: {adm_id}")
    updater = Updater(config["token"])
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("stop", stop))
    dispatcher.add_handler(CommandHandler("status", status))
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
