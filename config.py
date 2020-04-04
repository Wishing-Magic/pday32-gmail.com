from discord.ext import commands
import logging
from datetime import datetime
token = "Njk0ODU0NzYyNDAyODA3ODI4.XoRr8w.Z2FiZsqiH55Hdsr0MRYJLZz2SS0"
description = "Wishing Magic Bot"
gitURI = "git@github.com:Fam0r/Lynn3.git"
cogDir = "extensions"

logging.basicConfig(format='%(asctime)s | [%(levelname)s] (%(filename)s) - %(message)s',
                    level=logging.INFO,
                    handlers=[
                        logging.FileHandler("logs/"+datetime.now().strftime('%Y-%m-%d')+".log"),
                        logging.StreamHandler()
                    ])

def get_prefix(bot, message):
    prefixes = ['wm!', '%', 'wm', 'lynn ']
    if not message.guild:
        return '%'
    return commands.when_mentioned_or(*prefixes)(bot, message)

apiKeys = {
    "tracker":          "[KEY]",
    "steam":            "[KEY]",
    "darksky":          "[KEY]",
    "omdb":             "[KEY]",
    "mapbox":           "[KEY]",
    "twitterConsKey":   "[KEY]",
    "twitterConsSecret":"[KEY]",
    "twitterAccToken":  "[KEY]",
    "twitterAccSecret": "[KEY]",
    "osu":              "[KEY]",
    "twitchID":         "ukz6ofatr2f6ctitq1vhs7zo6a96i3",
    "twitchSecret":     "d3t6zovw8c9t9q0hkuot1dok4zldq2"
}

statusPages = [
    ('discord', 'https://status.discordapp.com', ('ztt4777v23lf',)),
    ("twitter", "https://api.twitterstat.us"),
    ("reddit", "https://reddit.statuspage.io"),
    ("cloudflare", "https://www.cloudflarestatus.com"),
    ("dropbox", "https://status.dropbox.com"),
    ("github", "https://www.githubstatus.com"),
    ("medium", "https://medium.statuspage.io"),
    ("epicgames", "https://status.epicgames.com"),
    ("glitch", "https://status.glitch.com")
]
