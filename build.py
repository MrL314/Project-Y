import os
import sys

working_dir = os.path.dirname(os.path.realpath(__file__)) # path to the folder containing this file
os.chdir(working_dir)

M = "" # define variable

def compileSrc():
    os.system("python3 Tools/createROM.py")

def cleanFolders():
    link_files = "VER_0/sfc/ys_main.rel VER_0/sfc/ys_save.rel VER_0/sfc/ys_title.rel VER_0/sfc/ys_enmy.rel VER_0/sfc/ys_enmy2.rel VER_0/sfc/ys_enmy3.rel VER_0/sfc/ys_enmy4.rel VER_0/sfc/ys_enmy5.rel VER_0/sfc/ys_enmy6.rel VER_0/sfc/ys_enmy7.rel VER_0/sfc/ys_enmy8.rel VER_0/sfc/ys_enmy9.rel VER_0/sfc/ys_enmy10.rel VER_0/sfc/ys_enmy11.rel VER_0/sfc/ys_enmy12.rel VER_0/sfc/ys_enmy14.rel VER_0/sfc/ys_boss1.rel VER_0/sfc/ys_boss2.rel VER_0/sfc/ys_bbbros.rel VER_0/sfc/ys_koopa.rel VER_0/sfc/ys_dorobo.rel VER_0/sfc/ys_babym.rel VER_0/sfc/ys_enmy13.rel VER_0/sfc/ys_exst.rel VER_0/sfc/ys_bgsc.rel VER_0/sfc/ys_bgsc0.rel VER_0/sfc/ys_bgsc1.rel VER_0/sfc/ys_bgsc2.rel VER_0/sfc/ys_bonus.rel VER_0/sfc/ys_start.rel VER_0/sfc/ys_mini.rel VER_0/sfc/ys_mini1.rel VER_0/sfc/ys_ending.rel VER_0/sfc/ys_demo.rel VER_0/sfc/ys_demo_1.rel VER_0/sfc/ys_init.rel VER_0/sfc/ys_game.rel VER_0/sfc/ys_play.rel VER_0/sfc/ys_map.rel VER_0/sfc/ys_hmap.rel VER_0/sfc/ys_hlder.rel VER_0/sfc/ys_rpro.rel VER_0/sfc/ys_data.rel VER_0/sfc/ys_pldt.rel VER_0/sfc/ys_pldt_e.rel VER_0/sfc/ys_mapdt.rel VER_0/sfc/ys_mpobj.rel VER_0/sfc/ys_mpmv.rel VER_0/sfc/ys_unit.rel VER_0/sfc/ys_w11.rel VER_0/sfc/ys_w12.rel VER_0/sfc/ys_w13.rel VER_0/sfc/ys_w14.rel VER_0/sfc/ys_w15.rel VER_0/sfc/ys_w16.rel VER_0/sfc/ys_w17.rel VER_0/sfc/ys_w18.rel VER_0/sfc/ys_w19.rel VER_0/sfc/ys_w21.rel VER_0/sfc/ys_w22.rel VER_0/sfc/ys_w23.rel VER_0/sfc/ys_w24.rel VER_0/sfc/ys_w25.rel VER_0/sfc/ys_w26.rel VER_0/sfc/ys_w27.rel VER_0/sfc/ys_w28.rel VER_0/sfc/ys_w29.rel VER_0/sfc/ys_w31.rel VER_0/sfc/ys_w32.rel VER_0/sfc/ys_w33.rel VER_0/sfc/ys_w34.rel VER_0/sfc/ys_w35.rel VER_0/sfc/ys_w36.rel VER_0/sfc/ys_w37.rel VER_0/sfc/ys_w38.rel VER_0/sfc/ys_w39.rel VER_0/sfc/ys_w41.rel VER_0/sfc/ys_w42.rel VER_0/sfc/ys_w43.rel VER_0/sfc/ys_w44.rel VER_0/sfc/ys_w45.rel VER_0/sfc/ys_w46.rel VER_0/sfc/ys_w47.rel VER_0/sfc/ys_w48.rel VER_0/sfc/ys_w49.rel VER_0/sfc/ys_w51.rel VER_0/sfc/ys_w52.rel VER_0/sfc/ys_w53.rel VER_0/sfc/ys_w54.rel VER_0/sfc/ys_w55.rel VER_0/sfc/ys_w56.rel VER_0/sfc/ys_w57.rel VER_0/sfc/ys_w58.rel VER_0/sfc/ys_w59.rel VER_0/sfc/ys_w61.rel VER_0/sfc/ys_w62.rel VER_0/sfc/ys_w63.rel VER_0/sfc/ys_w64.rel VER_0/sfc/ys_w65.rel VER_0/sfc/ys_w66.rel VER_0/sfc/ys_w67.rel VER_0/sfc/ys_w68.rel VER_0/sfc/ys_w69.rel VER_0/sfc/ys_w70.rel VER_0/sfc/ys_ench.rel VER_0/sfc/ys_msgdt.rel VER_0/sfc/ys_chr.rel"
    list_files = "VER_0/sfc/ys_main.lis VER_0/sfc/ys_save.lis VER_0/sfc/ys_title.lis VER_0/sfc/ys_enmy.lis VER_0/sfc/ys_enmy2.lis VER_0/sfc/ys_enmy3.lis VER_0/sfc/ys_enmy4.lis VER_0/sfc/ys_enmy5.lis VER_0/sfc/ys_enmy6.lis VER_0/sfc/ys_enmy7.lis VER_0/sfc/ys_enmy8.lis VER_0/sfc/ys_enmy9.lis VER_0/sfc/ys_enmy10.lis VER_0/sfc/ys_enmy11.lis VER_0/sfc/ys_enmy12.lis VER_0/sfc/ys_enmy14.lis VER_0/sfc/ys_boss1.lis VER_0/sfc/ys_boss2.lis VER_0/sfc/ys_bbbros.lis VER_0/sfc/ys_koopa.lis VER_0/sfc/ys_dorobo.lis VER_0/sfc/ys_babym.lis VER_0/sfc/ys_enmy13.lis VER_0/sfc/ys_exst.lis VER_0/sfc/ys_bgsc.lis VER_0/sfc/ys_bgsc0.lis VER_0/sfc/ys_bgsc1.lis VER_0/sfc/ys_bgsc2.lis VER_0/sfc/ys_bonus.lis VER_0/sfc/ys_start.lis VER_0/sfc/ys_mini.lis VER_0/sfc/ys_mini1.lis VER_0/sfc/ys_ending.lis VER_0/sfc/ys_demo.lis VER_0/sfc/ys_demo_1.lis VER_0/sfc/ys_init.lis VER_0/sfc/ys_game.lis VER_0/sfc/ys_play.lis VER_0/sfc/ys_map.lis VER_0/sfc/ys_hmap.lis VER_0/sfc/ys_hlder.lis VER_0/sfc/ys_rpro.lis VER_0/sfc/ys_data.lis VER_0/sfc/ys_pldt.lis VER_0/sfc/ys_pldt_e.lis VER_0/sfc/ys_mapdt.lis VER_0/sfc/ys_mpobj.lis VER_0/sfc/ys_mpmv.lis VER_0/sfc/ys_unit.lis VER_0/sfc/ys_w11.lis VER_0/sfc/ys_w12.lis VER_0/sfc/ys_w13.lis VER_0/sfc/ys_w14.lis VER_0/sfc/ys_w15.lis VER_0/sfc/ys_w16.lis VER_0/sfc/ys_w17.lis VER_0/sfc/ys_w18.lis VER_0/sfc/ys_w19.lis VER_0/sfc/ys_w21.lis VER_0/sfc/ys_w22.lis VER_0/sfc/ys_w23.lis VER_0/sfc/ys_w24.lis VER_0/sfc/ys_w25.lis VER_0/sfc/ys_w26.lis VER_0/sfc/ys_w27.lis VER_0/sfc/ys_w28.lis VER_0/sfc/ys_w29.lis VER_0/sfc/ys_w31.lis VER_0/sfc/ys_w32.lis VER_0/sfc/ys_w33.lis VER_0/sfc/ys_w34.lis VER_0/sfc/ys_w35.lis VER_0/sfc/ys_w36.lis VER_0/sfc/ys_w37.lis VER_0/sfc/ys_w38.lis VER_0/sfc/ys_w39.lis VER_0/sfc/ys_w41.lis VER_0/sfc/ys_w42.lis VER_0/sfc/ys_w43.lis VER_0/sfc/ys_w44.lis VER_0/sfc/ys_w45.lis VER_0/sfc/ys_w46.lis VER_0/sfc/ys_w47.lis VER_0/sfc/ys_w48.lis VER_0/sfc/ys_w49.lis VER_0/sfc/ys_w51.lis VER_0/sfc/ys_w52.lis VER_0/sfc/ys_w53.lis VER_0/sfc/ys_w54.lis VER_0/sfc/ys_w55.lis VER_0/sfc/ys_w56.lis VER_0/sfc/ys_w57.lis VER_0/sfc/ys_w58.lis VER_0/sfc/ys_w59.lis VER_0/sfc/ys_w61.lis VER_0/sfc/ys_w62.lis VER_0/sfc/ys_w63.lis VER_0/sfc/ys_w64.lis VER_0/sfc/ys_w65.lis VER_0/sfc/ys_w66.lis VER_0/sfc/ys_w67.lis VER_0/sfc/ys_w68.lis VER_0/sfc/ys_w69.lis VER_0/sfc/ys_w70.lis VER_0/sfc/ys_ench.lis VER_0/sfc/ys_msgdt.lis VER_0/sfc/ys_chr.lis"
    os.system("rm {}".format(link_files))
    os.system("rm {}".format(list_files))
    os.system("rm Tools/fhist.ahist")
    os.system("rm Output/ys_main.hex")
    os.system("rm Output/VER_0.sfc")

def menu():
    global M # update global variable M
    print("")
    print("YI ROM Builder (ver. 1.0)")
    print("1) Compile ROM (The output ROM will be in Output/)")
    print("2) Remove all built files")
    print("3) Exit")
    M = input("Type your option then press ENTER: ")

    if M == "1":
        compileSrc()
    elif M == "2":
        cleanFolders()
    elif M == "3":
        sys.exit(0)

while not (M == "3"):
    menu()