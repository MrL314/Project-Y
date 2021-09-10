import os

working_dir = os.path.dirname(os.path.realpath(__file__)) # path to the folder containing this file
os.chdir(working_dir)

print("Assembling .asm files into .rel files!")

def assemble(path):
    os.system("python3 as65c/as65c.py {} -w -dNES=0 -dJPN=1 -dPAL=0 -dBUG00=0 -dBUG01=0 -dBUG02=0 -dBUG03=0".format(path))

# SFXINC
assemble("../VER_0/sfc/ys_main.asm")
assemble("../VER_0/sfc/ys_save.asm")
assemble("../VER_0/sfc/ys_title.asm")
assemble("../VER_0/sfc/ys_enmy.asm")
assemble("../VER_0/sfc/ys_enmy2.asm")
assemble("../VER_0/sfc/ys_enmy3.asm")
assemble("../VER_0/sfc/ys_enmy4.asm")
assemble("../VER_0/sfc/ys_enmy5.asm")
assemble("../VER_0/sfc/ys_enmy6.asm")
assemble("../VER_0/sfc/ys_enmy7.asm")
assemble("../VER_0/sfc/ys_enmy8.asm")
assemble("../VER_0/sfc/ys_enmy9.asm")
assemble("../VER_0/sfc/ys_enmy10.asm")
assemble("../VER_0/sfc/ys_enmy11.asm")
assemble("../VER_0/sfc/ys_enmy12.asm")
assemble("../VER_0/sfc/ys_enmy14.asm")
assemble("../VER_0/sfc/ys_boss1.asm")
assemble("../VER_0/sfc/ys_boss2.asm")
assemble("../VER_0/sfc/ys_bbbros.asm")
assemble("../VER_0/sfc/ys_koopa.asm")
assemble("../VER_0/sfc/ys_dorobo.asm")
assemble("../VER_0/sfc/ys_babym.asm")
assemble("../VER_0/sfc/ys_enmy13.asm")
assemble("../VER_0/sfc/ys_exst.asm")
assemble("../VER_0/sfc/ys_bgsc.asm")
assemble("../VER_0/sfc/ys_bgsc0.asm")
assemble("../VER_0/sfc/ys_bgsc1.asm")
assemble("../VER_0/sfc/ys_bgsc2.asm")
assemble("../VER_0/sfc/ys_bonus.asm")
assemble("../VER_0/sfc/ys_start.asm")
assemble("../VER_0/sfc/ys_mini.asm")
assemble("../VER_0/sfc/ys_mini1.asm")
assemble("../VER_0/sfc/ys_ending.asm")
assemble("../VER_0/sfc/ys_demo.asm")
assemble("../VER_0/sfc/ys_demo_1.asm")

# SFXCOL
assemble("../VER_0/sfc/ys_init.asm")
assemble("../VER_0/sfc/ys_game.asm")
assemble("../VER_0/sfc/ys_play.asm")
assemble("../VER_0/sfc/ys_map.asm")
assemble("../VER_0/sfc/ys_hmap.asm")
assemble("../VER_0/sfc/ys_hlder.asm")
assemble("../VER_0/sfc/ys_rpro.asm")
assemble("../VER_0/sfc/ys_data.asm")

# SFXREL
assemble("../VER_0/sfc/ys_pldt.asm")
assemble("../VER_0/sfc/ys_pldt_e.asm")
assemble("../VER_0/sfc/ys_mapdt.asm")
assemble("../VER_0/sfc/ys_mpobj.asm")
assemble("../VER_0/sfc/ys_mpmv.asm")
assemble("../VER_0/sfc/ys_unit.asm")
assemble("../VER_0/sfc/ys_w11.asm")
assemble("../VER_0/sfc/ys_w12.asm")
assemble("../VER_0/sfc/ys_w13.asm")
assemble("../VER_0/sfc/ys_w14.asm")
assemble("../VER_0/sfc/ys_w15.asm")
assemble("../VER_0/sfc/ys_w16.asm")
assemble("../VER_0/sfc/ys_w17.asm")
assemble("../VER_0/sfc/ys_w18.asm")
assemble("../VER_0/sfc/ys_w19.asm")
assemble("../VER_0/sfc/ys_w21.asm")
assemble("../VER_0/sfc/ys_w22.asm")
assemble("../VER_0/sfc/ys_w23.asm")
assemble("../VER_0/sfc/ys_w24.asm")
assemble("../VER_0/sfc/ys_w25.asm")
assemble("../VER_0/sfc/ys_w26.asm")
assemble("../VER_0/sfc/ys_w27.asm")
assemble("../VER_0/sfc/ys_w28.asm")
assemble("../VER_0/sfc/ys_w29.asm")
assemble("../VER_0/sfc/ys_w31.asm")
assemble("../VER_0/sfc/ys_w32.asm")
assemble("../VER_0/sfc/ys_w33.asm")
assemble("../VER_0/sfc/ys_w34.asm")
assemble("../VER_0/sfc/ys_w35.asm")
assemble("../VER_0/sfc/ys_w36.asm")
assemble("../VER_0/sfc/ys_w37.asm")
assemble("../VER_0/sfc/ys_w38.asm")
assemble("../VER_0/sfc/ys_w39.asm")
assemble("../VER_0/sfc/ys_w41.asm")
assemble("../VER_0/sfc/ys_w42.asm")
assemble("../VER_0/sfc/ys_w43.asm")
assemble("../VER_0/sfc/ys_w44.asm")
assemble("../VER_0/sfc/ys_w45.asm")
assemble("../VER_0/sfc/ys_w46.asm")
assemble("../VER_0/sfc/ys_w47.asm")
assemble("../VER_0/sfc/ys_w48.asm")
assemble("../VER_0/sfc/ys_w49.asm")
assemble("../VER_0/sfc/ys_w51.asm")
assemble("../VER_0/sfc/ys_w52.asm")
assemble("../VER_0/sfc/ys_w53.asm")
assemble("../VER_0/sfc/ys_w54.asm")
assemble("../VER_0/sfc/ys_w55.asm")
assemble("../VER_0/sfc/ys_w56.asm")
assemble("../VER_0/sfc/ys_w57.asm")
assemble("../VER_0/sfc/ys_w58.asm")
assemble("../VER_0/sfc/ys_w59.asm")
assemble("../VER_0/sfc/ys_w61.asm")
assemble("../VER_0/sfc/ys_w62.asm")
assemble("../VER_0/sfc/ys_w63.asm")
assemble("../VER_0/sfc/ys_w64.asm")
assemble("../VER_0/sfc/ys_w65.asm")
assemble("../VER_0/sfc/ys_w66.asm")
assemble("../VER_0/sfc/ys_w67.asm")
assemble("../VER_0/sfc/ys_w68.asm")
assemble("../VER_0/sfc/ys_w69.asm")
assemble("../VER_0/sfc/ys_w70.asm")
assemble("../VER_0/sfc/ys_ench.asm")
assemble("../VER_0/sfc/ys_msgdt.asm")
assemble("../VER_0/sfc/ys_chr.asm")

print("Assembled .asm files!")

print("Linking .rel files into a single ROM")

relinfo0 = "-rGroup_0=08000,Group_R=c000,Group_1=18000,Group_2=28000,Group_3=38000,Group_4=48000"
relinfo1 = "-rGroup_5=58000,Group_6=68000,Group_7=78000,Group_C=c8000,Group_D=d8000,Group_E=e8000,Group_F=fa000"
relinfo2 = "-rGroup_10=108000,Group_11=118000,Group_B=BDC00"
relinfo3 = "-rGroup_12=128000,Group_13=138000,Group_14=148000,Group_15=158000,Group_16=168000,Group_17=178000"
relinfo4 = "-rGroup_4C=4C0000,Group_5F=5F4000"
relinfo = relinfo0+" "+relinfo1+" "+relinfo2+" "+relinfo3+" "+relinfo4

link_files = "../VER_0/sfc/ys_main.rel ../VER_0/sfc/ys_save.rel ../VER_0/sfc/ys_title.rel ../VER_0/sfc/ys_enmy.rel ../VER_0/sfc/ys_enmy2.rel ../VER_0/sfc/ys_enmy3.rel ../VER_0/sfc/ys_enmy4.rel ../VER_0/sfc/ys_enmy5.rel ../VER_0/sfc/ys_enmy6.rel ../VER_0/sfc/ys_enmy7.rel ../VER_0/sfc/ys_enmy8.rel ../VER_0/sfc/ys_enmy9.rel ../VER_0/sfc/ys_enmy10.rel ../VER_0/sfc/ys_enmy11.rel ../VER_0/sfc/ys_enmy12.rel ../VER_0/sfc/ys_enmy14.rel ../VER_0/sfc/ys_boss1.rel ../VER_0/sfc/ys_boss2.rel ../VER_0/sfc/ys_bbbros.rel ../VER_0/sfc/ys_koopa.rel ../VER_0/sfc/ys_dorobo.rel ../VER_0/sfc/ys_babym.rel ../VER_0/sfc/ys_enmy13.rel ../VER_0/sfc/ys_exst.rel ../VER_0/sfc/ys_bgsc.rel ../VER_0/sfc/ys_bgsc0.rel ../VER_0/sfc/ys_bgsc1.rel ../VER_0/sfc/ys_bgsc2.rel ../VER_0/sfc/ys_bonus.rel ../VER_0/sfc/ys_start.rel ../VER_0/sfc/ys_mini.rel ../VER_0/sfc/ys_mini1.rel ../VER_0/sfc/ys_ending.rel ../VER_0/sfc/ys_demo.rel ../VER_0/sfc/ys_demo_1.rel ../VER_0/sfc/ys_init.rel ../VER_0/sfc/ys_game.rel ../VER_0/sfc/ys_play.rel ../VER_0/sfc/ys_map.rel ../VER_0/sfc/ys_hmap.rel ../VER_0/sfc/ys_hlder.rel ../VER_0/sfc/ys_rpro.rel ../VER_0/sfc/ys_data.rel ../VER_0/sfc/ys_pldt.rel ../VER_0/sfc/ys_pldt_e.rel ../VER_0/sfc/ys_mapdt.rel ../VER_0/sfc/ys_mpobj.rel ../VER_0/sfc/ys_mpmv.rel ../VER_0/sfc/ys_unit.rel ../VER_0/sfc/ys_w11.rel ../VER_0/sfc/ys_w12.rel ../VER_0/sfc/ys_w13.rel ../VER_0/sfc/ys_w14.rel ../VER_0/sfc/ys_w15.rel ../VER_0/sfc/ys_w16.rel ../VER_0/sfc/ys_w17.rel ../VER_0/sfc/ys_w18.rel ../VER_0/sfc/ys_w19.rel ../VER_0/sfc/ys_w21.rel ../VER_0/sfc/ys_w22.rel ../VER_0/sfc/ys_w23.rel ../VER_0/sfc/ys_w24.rel ../VER_0/sfc/ys_w25.rel ../VER_0/sfc/ys_w26.rel ../VER_0/sfc/ys_w27.rel ../VER_0/sfc/ys_w28.rel ../VER_0/sfc/ys_w29.rel ../VER_0/sfc/ys_w31.rel ../VER_0/sfc/ys_w32.rel ../VER_0/sfc/ys_w33.rel ../VER_0/sfc/ys_w34.rel ../VER_0/sfc/ys_w35.rel ../VER_0/sfc/ys_w36.rel ../VER_0/sfc/ys_w37.rel ../VER_0/sfc/ys_w38.rel ../VER_0/sfc/ys_w39.rel ../VER_0/sfc/ys_w41.rel ../VER_0/sfc/ys_w42.rel ../VER_0/sfc/ys_w43.rel ../VER_0/sfc/ys_w44.rel ../VER_0/sfc/ys_w45.rel ../VER_0/sfc/ys_w46.rel ../VER_0/sfc/ys_w47.rel ../VER_0/sfc/ys_w48.rel ../VER_0/sfc/ys_w49.rel ../VER_0/sfc/ys_w51.rel ../VER_0/sfc/ys_w52.rel ../VER_0/sfc/ys_w53.rel ../VER_0/sfc/ys_w54.rel ../VER_0/sfc/ys_w55.rel ../VER_0/sfc/ys_w56.rel ../VER_0/sfc/ys_w57.rel ../VER_0/sfc/ys_w58.rel ../VER_0/sfc/ys_w59.rel ../VER_0/sfc/ys_w61.rel ../VER_0/sfc/ys_w62.rel ../VER_0/sfc/ys_w63.rel ../VER_0/sfc/ys_w64.rel ../VER_0/sfc/ys_w65.rel ../VER_0/sfc/ys_w66.rel ../VER_0/sfc/ys_w67.rel ../VER_0/sfc/ys_w68.rel ../VER_0/sfc/ys_w69.rel ../VER_0/sfc/ys_w70.rel ../VER_0/sfc/ys_ench.rel ../VER_0/sfc/ys_msgdt.rel ../VER_0/sfc/ys_chr.rel"

os.system("python3 link/link.py {} -o ../Output/ys_main.hex {} -ls ys_main.map".format(link_files, relinfo))

print("Converting hex file")
os.system("python3 hex2bin/hex2bin.py -m mario -cff -f../Output/ys_main.hex -fys_chip0.hex -i../VER_0/sfc/yschr -ihdr -o../Output/VER_0.sfc -r16")

print("Created .sfc at ../Output/VER_0.sfc!")