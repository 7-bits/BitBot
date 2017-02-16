#!/usr/bin/python3.5
# BitBot

# ################### Copyright (c) 2017 7-Bits #################
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to do so

import os
import time
import json
import discord
import random
import asyncio

client = discord.Client()

EIGHT_BALL_OPTIONS = ["It is certain", "It is decidedly so", "Without a doubt",
                      "Yes definitely", "You may rely on it", "As I see it yes",
                      "Most likely", "Outlook good", "Yes",
                      "Signs point to yes", "Reply hazy try again",
                      "Ask again later", "Better not tell you now",
                      "Cannot predict now", "Concentrate and ask again",
                      "Don't count on it", "My reply is no",
                      "My sources say no", "Outlook not so good",
                      "Very doubtful"]

@client.event
async def on_ready():
    print("Bot is online!") # Good morning.

# Bot, thy shall answer me!
@client.event
async def on_message(message):
    if message.content.startswith('^help'):
        print('command: help')
        await client.send_message(message.channel, 'Hey %s ! I\'m BitBot, made by 7-bits#8201. I\'m currently in development.\nMy prefix is `^` and I have a few basic commands. You can check them out with `^commands`.\nYou can join my help server at https://discord.gg/xqtUCHS\nEnjoy!' % (message.author))
    if message.content.startswith('^commands'):
        print('command: commands')
        await client.send_message(message.channel, '**My commands are:**\n```^ping                        Is this thing even on?\n^pong                        Is this thing even off?\n^flip                        Heads or tails?\n^personflip                       Flip someone\n^8ball                       What are the odds... ?\n^do_something_useful         Doing something useful, brb ```')
    if message.content.startswith('^ping'):
        print('command: ping')
        await client.send_message(message.channel, 'Pong!')
    if message.content.startswith('^pong'):
        print('commmand: pong')
        await client.send_message(message.channel, '%s' % message.author)
        await client.send_message(message.channel, '%s' % message.author)
        await client.send_message(message.channel, '%s' % message.author)
        await client.send_message(message.channel, '/tableflip')
    if message.content.startswith('^do_something_useful'):
        print('command: do_something_useful')
        await client.send_message(message.channel, 'Hey %s, you really thought this would do something useful, did you? Shame!' % message.author)
    if message.content.startswith('^flip'):
        print('command: flip')
        outcome = random.randint(0,1)
        if outcome == 0:
            outcome = "heads"
        else:
            outcome = "tails"
        await client.send_message(message.channel, "Just a moment, flipping the coin...")
        time.sleep(.5)
        await client.send_message(message.channel, "You flipped %s!" % outcome)
    if message.content.startswith('^personflip'):
        await client.send_message(message.channel, "Fuck off <@157759797117059072>")
    if message.content.startswith('^8ball'):
        print('command: 8ball')
        question = message.content.strip('^8ball')
        prediction = random.randint(0, len(EIGHT_BALL_OPTIONS) - 1)
        await client.send_message(message.channel, 'Question: [%s], %s' % (question, EIGHT_BALL_OPTIONS[prediction]))
 # Start the bot!
client.run('bot_token')
