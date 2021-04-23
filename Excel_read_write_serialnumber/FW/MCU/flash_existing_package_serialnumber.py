#!/usr/bin/env python3
import subprocess
import argparse
import struct
import os

parser = argparse.ArgumentParser()
parser.add_argument(
	"bin",
	help="Binary package to program")
parser.add_argument(
	"serial",
	help="Serial number to program")
args = parser.parse_args()



out_file='FullPackage.tmp.bin'
if os.path.exists(out_file):
	os.remove(out_file)
while True:
	serial = int(args.serial)
	print(args.serial)
	if serial < 0 or serial > 999999999999999 :
		print("Invalid serial number")
		exit(1)

	# Read file until the serial number to prevent adding the serial number twice
	subprocess.check_call([
	'dd',
	'if={}'.format(args.bin),
	'of={}'.format(out_file),
	'count=1',
	'bs=2093056'
	])
	

	if not os.path.isfile(args.bin):
		print("input file does not exist: " + args.bin)
		exit(1)

	with open(out_file, "ab") as f:
		f.write(struct.pack('16s', str(serial).encode('ascii')))

	print("Attached serial number: {} to: {}".format(str(serial), out_file))

	with open("commands.jlink", mode='w+') as fp:
		fp.writelines([
		'exitonerror 1\n',
		'r\n',
		'h\n',
		'WaitHalt\n',
		'loadbin ' + out_file + ' 0\n',
		'r0\n',
		'Sleep 20\n',
		'r1\n',
		'qc\n'
		])

	jlink = 'JLinkExe'
	if os.name == "nt":
		jlink = 'C:\Program Files (x86)\SEGGER\JLink_V632g\jlink.exe'\
		
	subprocess.check_call(
	[
		jlink,
		'-if', 'SWD',
		'-device', 'MK26FN2M0xxx18 (allow security)',
		'-speed', '4000',
		'-commanderscript', 'commands.jlink'
	])
	break
