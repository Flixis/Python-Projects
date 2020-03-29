#!/usr/bin/env python3
import subprocess
import os

jlink = 'JLinkExe'
if os.name == "nt":
	jlink = 'C:\Program Files (x86)\SEGGER\JLink\jlink.exe'

subprocess.check_call(
[
	jlink,
	'-if', 'SWD',
	'-device', 'nRF52832_xxAA',
	'-speed', '4000',
	'-commanderscript', 'flash.jlink'
])
