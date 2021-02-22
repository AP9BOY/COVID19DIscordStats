#Made by RyZwer#0001

# ----------------------------------------------- > Libraries

import os, time, dhooks, requests, json
from dhooks import Webhook, Embed

# ----------------------------------------------- > Setup

os.system("cls")
os.system("title Covid-19 Stats")

# ----------------------------------------------- > Configuration

with open("./config.json", 'r') as json_config_file:
    json = json.load(json_config_file)

# ----------------------------------------------- > Webhook Code

hook = Webhook(f"{json['webhook_url']}")

while True:
    site = requests.get("https://corona.lmao.ninja/v2/all")
    json_site = site.json()

    embed = Embed(
        title="Covid-19 stats", url="https://corona.lmao.ninja/v2/all",
        description=f"**Cases**: `{json_site['cases']}`\n**TodayCases**: `{json_site['todayCases']}`\n**Deaths**: `{json_site['deaths']}`\n**TodayDeaths**: `{json_site['todayDeaths']}`\n**Recovered**: `{json_site['recovered']}`\n**TodayRecovered**: `{json_site['todayRecovered']}`",
        color=0x3877FF,
        timestamp='now'
    )
    embed.set_thumbnail(url="https://bit.ly/37hmLsE")
    embed.set_footer(text="Made by RyZwer#0001", icon_url="https://bit.ly/2NJJbvQ") #Please don't remove "Made by RyZwer#0001", thanks!
    hook.send(embed=embed)
    time.sleep(json['send_after'])

# ----------------------------------------------- > End of the code
