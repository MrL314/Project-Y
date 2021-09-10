import os
import sys

working_dir = os.path.dirname(os.path.realpath(__file__)) # path to the folder containing this file
os.chdir(working_dir)

M = "" # define variable

def compileSrc():
    os.system("python3 Tools/createROM.py")

def cleanFolders():
    link_files = "VER_0/sfc/ys_main.rel VER_0/sfc/ys_save.rel VER_0/sfc/ys_title.rel VER_0/sfc/ys_enmy.rel VER_0/sfc/ys_enmy2.rel VER_0/sfc/ys_enmy3.rel VER_0/sfc/ys_enmy4.rel VER_0/sfc/ys_enmy5.rel VER_0/sfc/ys_enmy6.rel VER_0/sfc/ys_enmy7.rel VER_0/sfc/ys_enmy8.rel VER_0/sfc/ys_enmy9.rel VER_0/sfc/ys_enmy10.rel VER_0/sfc/ys_enmy11.rel VER_0/sfc/ys_enmy12.rel VER_0/sfc/ys_enmy14.rel VER_0/sfc/ys_boss1.rel VER_0/sfc/ys_boss2.rel VER_0/sfc/ys_bbbros.rel VER_0/sfc/ys_koopa.rel VER_0/sfc/ys_dorobo.rel VER_0/sfc/ys_babym.rel VER_0/sfc/ys_enmy13.rel VER_0/sfc/ys_exst.rel VER_0/sfc/ys_bgsc.rel VER_0/sfc/ys_bgsc0.rel VER_0/sfc/ys_bgsc1.rel VER_0/sfc/ys_bgsc2.rel VER_0/sfc/ys_bonus.rel VER_0/sfc/ys_start.rel VER_0/sfc/ys_mini.rel VER_0/sfc/ys_mini1.rel VER_0/sfc/ys_ending.rel VER_0/sfc/ys_demo.rel VER_0/sfc/ys_demo_1.rel VER_0/sfc/ys_init.rel VER_0/sfc/ys_game.rel VER_0/sfc/ys_play.rel VER_0/sfc/ys_map.rel VER_0/sfc/ys_hmap.rel VER_0/sfc/ys_hlder.rel VER_0/sfc/ys_rpro.rel VER_0/sfc/ys_data.rel VER_0/sfc/ys_pldt.rel VER_0/sfc/ys_pldt_e.rel VER_0/sfc/ys_mapdt.rel VER_0/sfc/ys_mpobj.rel VER_0/sfc/ys_mpmv.rel VER_0/sfc/ys_unit.rel VER_0/sfc/ys_w11.rel VER_0/sfc/ys_w12.rel VER_0/sfc/ys_w13.rel VER_0/sfc/ys_w14.rel VER_0/sfc/ys_w15.rel VER_0/sfc/ys_w16.rel VER_0/sfc/ys_w17.rel VER_0/sfc/ys_w18.rel VER_0/sfc/ys_w19.rel VER_0/sfc/ys_w21.rel VER_0/sfc/ys_w22.rel VER_0/sfc/ys_w23.rel VER_0/sfc/ys_w24.rel VER_0/sfc/ys_w25.rel VER_0/sfc/ys_w26.rel VER_0/sfc/ys_w27.rel VER_0/sfc/ys_w28.rel VER_0/sfc/ys_w29.rel VER_0/sfc/ys_w31.rel VER_0/sfc/ys_w32.rel VER_0/sfc/ys_w33.rel VER_0/sfc/ys_w34.rel VER_0/sfc/ys_w35.rel VER_0/sfc/ys_w36.rel VER_0/sfc/ys_w37.rel VER_0/sfc/ys_w38.rel VER_0/sfc/ys_w39.rel VER_0/sfc/ys_w41.rel VER_0/sfc/ys_w42.rel VER_0/sfc/ys_w43.rel VER_0/sfc/ys_w44.rel VER_0/sfc/ys_w45.rel VER_0/sfc/ys_w46.rel VER_0/sfc/ys_w47.rel VER_0/sfc/ys_w48.rel VER_0/sfc/ys_w49.rel VER_0/sfc/ys_w51.rel VER_0/sfc/ys_w52.rel VER_0/sfc/ys_w53.rel VER_0/sfc/ys_w54.rel VER_0/sfc/ys_w55.rel VER_0/sfc/ys_w56.rel VER_0/sfc/ys_w57.rel VER_0/sfc/ys_w58.rel VER_0/sfc/ys_w59.rel VER_0/sfc/ys_w61.rel VER_0/sfc/ys_w62.rel VER_0/sfc/ys_w63.rel VER_0/sfc/ys_w64.rel VER_0/sfc/ys_w65.rel VER_0/sfc/ys_w66.rel VER_0/sfc/ys_w67.rel VER_0/sfc/ys_w68.rel VER_0/sfc/ys_w69.rel VER_0/sfc/ys_w70.rel VER_0/sfc/ys_ench.rel VER_0/sfc/ys_msgdt.rel VER_0/sfc/ys_chr.rel"
    os.system(f"rm {link_files}")
    os.remove("Output/ys_main.hex")
    os.remove("Output/VER_0.sfc")

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