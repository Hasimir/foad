#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

##
# FOAD: Fucked Off Adversarial Degenerates (Fuck Off And Die)
#
# Copyright (C) Ben McGinnes, 2013-2015
# ben@adversary.org
# OpenPGP/GPG key:  0x321E4E2373590E5D
#
# https://github.com/adversary-org/foad
#
# Version:  0.8.0.0
#
# BTC:  1NpzDJg2pXjSqCL3XHTcyYaehiBN3kG3Lz
# Licenses:  GNU Public License version 3 (GPLv3)
#            Do What The Fuck You Want But It's Not My Fault (WTFNMFv1)
#            BSD 3-Clause License (BSD)
#            Apache 2.0
#
# https://www.gnu.org/copyleft/gpl.html
# https://github.com/adversary-org/wtfnmf
# 
#
# Requirements:
#
# * Python 3.2 or later (developed with Python 3.4.x)
# * Python 2.7 supported from version 0.8 onward.
# * EasyGUI 0.97.4
#
#
# Notes:
#
# Rather than re-implementing the entirety of foad.py with a GUI, it
# is probably best to make the GUI send and receive data to/from
# foad.py.  That way any future improvement of foad.py continues being
# easy and I don't get locked into one particular interface.  Plus I
# made foad.py work as a module ages ago, so I could take advantage of
# that, though it probably doesn't get all the advantages of a command
# line invocation (so subprocess is best here).
#
##

import easygui
import subprocess

eg = easygui
foad = "./foad.py"
pipe = subprocess.PIPE
pope = subprocess.Popen

fd = eg.multenterbox(msg="Select FOAD parameters",
                     title="FOAD: Fuck Off And Die!",
                     fields=("Type of Fuck", "Target's Name",
                             "Extra Setting", "Sender's Name",
                             "Relay's Name", "Prepend With", "Append With"),
                     values=("", "", "", "", "", "", ""))

s1 = pope([foad, "--fuck", fd[0], "--name", fd[1], "--extra", fd[2],
           "--sender", fd[3], "--relay", fd[4], "--prepend", fd[5],
           "--append", fd[6]], stdout=pipe)
s2 = s1.communicate()[0].strip()
s3 = s2.decode("utf-8")

print(s3)

# Display result in GUI:
#
# tb = eg.textbox(text=s3)

# Tweet result or other Twitter or message based actions.
#
# Use subprocess to invoke any of these options:
#
# tweet-basic.py to tweet the result.
# tweet-dm.py to send insult privately.
# tweet-reply.py to respond to another message.
# Any of those 3 in conjunction with block, mute, block & report as
# spammer, unfollow, etc.

# Could also reintegrate with the SMS gateway code in the same manner
# as with the Twython stuff.
