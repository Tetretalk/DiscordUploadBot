#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from discordbot import DiscordBot
import asyncio

bot = DiscordBot(pm_help=True)

bot.load_cogs()
bot.run()
