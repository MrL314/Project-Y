import os, sys

os.chdir(os.getcwd())

INS = "ins"
DEL = "del"

def fix_text_file(filename, fixes):

	lines = []

	f_num = 0
	num_fixes = len(fixes)


	l_num = 1
	with open(filename, "r", encoding="utf-8", errors="ignore") as f:

		for line in f:

			LINE = line

			if f_num < num_fixes and l_num == fixes[f_num]["line"]:
				print("Modifiying line " + str(l_num) + " of " + filename + ".\nBEFORE: " + LINE.replace("\n", ""))

			while f_num < num_fixes and l_num == fixes[f_num]["line"]:

				fix = fixes[f_num]

				if fix["type"] == INS:
					LINE = LINE[:fix["indx"]] + fix["data"] + LINE[fix["indx"]:]

				elif fix["type"] == DEL:
					if LINE[fix["indx"]:fix["indx"]+len(fix["data"])] != fix["data"]:
						raise Exception("Data mismatch in file: " + filename + ". Data to delete: " + fix["data"] + ", Data in line: " + LINE[fix["indx"]:fix["indx"]+len(fix["data"])])
					LINE = LINE[:fix["indx"]] + LINE[fix["indx"] + len(fix["data"]):]



				f_num += 1

			if LINE != line:
				print("AFTER:  " + LINE.replace("\n", ""))


			lines.append(LINE)

			l_num += 1


	with open(filename, "w", encoding="utf-8", errors="ignore") as f:
		for line in lines:
			f.write(line)





def fix_bin_file(filename, fixes):

	data = []

	with open(filename, "rb") as f:
		data = bytearray(f.read())


	for idx, dat in fixes:
		size = min(len(dat), len(data)-idx)
		print("Modifying file " + filename + ". Writing data at $" + format(idx, "06x") + ": " + " ".join([format(x, "02x").upper() for x in bytearray(dat)[:size]]))
		

		data[idx:idx+size] = dat[:size]


	with open(filename, "wb") as f:
		f.write(bytes(data))








CODE_DIR = "VER_0/sfc/"


fix_text_file(CODE_DIR + "ys_enmy.asm", [
	{
		"line": 8865,
		"type": DEL,
		"indx": 19,
		"data": "2"
	},
	{
		"line": 16072,
		"type": INS,
		"indx": 9,
		"data": ";"
	}
	])


fix_text_file(CODE_DIR + "ys_enmy4.asm", [
	{
		"line": 15768,
		"type": INS,
		"indx": 9,
		"data": ";"
	}
	])

fix_text_file(CODE_DIR + "ys_enmy7.asm", [
	{
		"line": 1388,
		"type": INS,
		"indx": 8,
		"data": ";"
	},
	{
		"line": 1389,
		"type": INS,
		"indx": 8,
		"data": ";"
	}
	])

fix_text_file(CODE_DIR + "ys_enmy9.asm", [
	{
		"line": 3963,
		"type": DEL,
		"indx": 15,
		"data": ",X"
	}
	])

fix_text_file(CODE_DIR + "ys_enmy10.asm", [
	{
		"line": 2951,
		"type": INS,
		"indx": 19,
		"data": ";"
	}
	])

fix_text_file(CODE_DIR + "ys_boss1.asm", [
	{
		"line": 3739,
		"type": INS,
		"indx": 9,
		"data": ";"
	}
	])

fix_text_file(CODE_DIR + "ys_bonus.asm", [
	{
		"line": 7883,
		"type": INS,
		"indx": 14,
		"data": ";"
	},
	{
		"line": 7887,
		"type": INS,
		"indx": 15,
		"data": ";"
	}
	])

fix_text_file(CODE_DIR + "ys_map.asm", [
	{
		"line": 317,
		"type": DEL,
		"indx": 35,
		"data": "+SV_CRS"
	},
	{
		"line": 317,
		"type": INS,
		"indx": 7,
		"data": "SV_CRS+"
	},
	{
		"line": 318,
		"type": DEL,
		"indx": 35,
		"data": "+SV_CRS"
	},
	{
		"line": 318,
		"type": INS,
		"indx": 7,
		"data": "SV_CRS+"
	},
	{
		"line": 319,
		"type": DEL,
		"indx": 35,
		"data": "+SV_CRS"
	},
	{
		"line": 319,
		"type": INS,
		"indx": 7,
		"data": "SV_CRS+"
	},
	{
		"line": 322,
		"type": DEL,
		"indx": 15,
		"data": "+SV_CRS"
	},
	{
		"line": 322,
		"type": INS,
		"indx": 7,
		"data": "SV_CRS+"
	},
	{
		"line": 323,
		"type": DEL,
		"indx": 15,
		"data": "+SV_CRS"
	},
	{
		"line": 323,
		"type": INS,
		"indx": 7,
		"data": "SV_CRS+"
	},
	{
		"line": 324,
		"type": DEL,
		"indx": 15,
		"data": "+SV_CRS"
	},
	{
		"line": 324,
		"type": INS,
		"indx": 7,
		"data": "SV_CRS+"
	}
	])


fix_text_file(CODE_DIR + "ys_rpro.asm", [
	{
		"line": 4548,
		"type": DEL,
		"indx": 15,
		"data": "+INT_STAT"
	},
	{
		"line": 4548,
		"type": INS,
		"indx": 7,
		"data": "INT_STAT+"
	}
	])



fix_bin_file(CODE_DIR + "ys_col.col", [
	(0x2652, bytes([int(x, 16) for x in "BF 03 7F 03 3F 03 FF 02 BF 02 7F 02 3F 02 FF 01 BF 01 7F 01 3F 01 FF 00 BF 00 7F 00 1F 00".split()]))
	])