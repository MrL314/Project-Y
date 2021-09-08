
@echo  OFF


set asm-vars=-w -dNES=0 -dJPN=1 -dPAL=0 -dBUG00=0 -dBUG01=0 -dBUG02=0 -dBUG03=0

set linker-input="linked rel files.txt"
set linker-options="rel options.txt"
set linker-output="..\Output\CODE_ONLY.rom"

set ROM-OUTPUT="..\Output\VER_0.sfc"
set code_source_dir="..\VER_0"


set asm="as65c\as65c"

set lnk="link\link"

set h2b="hex2bin\hex2bin"

ECHO Assembling .asm files into .rel files!

break>SYMBOLS.txt



rem Assemble all files



rem PUT FILES TO ASSEMBLE HERE:
rem format as "call :assemble <file>"


rem SFXINC
call :assemble /sfc/ys_main.asm
call :assemble /sfc/ys_save.asm
call :assemble /sfc/ys_title.asm
call :assemble /sfc/ys_enmy.asm
call :assemble /sfc/ys_enmy2.asm
call :assemble /sfc/ys_enmy3.asm
call :assemble /sfc/ys_enmy4.asm
call :assemble /sfc/ys_enmy5.asm
call :assemble /sfc/ys_enmy6.asm
call :assemble /sfc/ys_enmy7.asm
call :assemble /sfc/ys_enmy8.asm
call :assemble /sfc/ys_enmy9.asm
call :assemble /sfc/ys_enmy10.asm
call :assemble /sfc/ys_enmy11.asm
call :assemble /sfc/ys_enmy12.asm
call :assemble /sfc/ys_enmy14.asm
call :assemble /sfc/ys_boss1.asm
call :assemble /sfc/ys_boss2.asm
call :assemble /sfc/ys_bbbros.asm
call :assemble /sfc/ys_koopa.asm
call :assemble /sfc/ys_dorobo.asm
call :assemble /sfc/ys_babym.asm
call :assemble /sfc/ys_enmy13.asm
call :assemble /sfc/ys_exst.asm
call :assemble /sfc/ys_bgsc.asm
call :assemble /sfc/ys_bgsc0.asm
call :assemble /sfc/ys_bgsc1.asm
call :assemble /sfc/ys_bgsc2.asm
call :assemble /sfc/ys_bonus.asm
call :assemble /sfc/ys_start.asm
call :assemble /sfc/ys_mini.asm
call :assemble /sfc/ys_mini1.asm
call :assemble /sfc/ys_ending.asm
call :assemble /sfc/ys_demo.asm
call :assemble /sfc/ys_demo_1.asm

rem SFXCOL
call :assemble /sfc/ys_init.asm
call :assemble /sfc/ys_game.asm
call :assemble /sfc/ys_play.asm
call :assemble /sfc/ys_map.asm
call :assemble /sfc/ys_hmap.asm
call :assemble /sfc/ys_hlder.asm
call :assemble /sfc/ys_rpro.asm
call :assemble /sfc/ys_data.asm

rem SFXREL
call :assemble /sfc/ys_pldt.asm
call :assemble /sfc/ys_pldt_e.asm
call :assemble /sfc/ys_mapdt.asm
call :assemble /sfc/ys_mpobj.asm
call :assemble /sfc/ys_mpmv.asm
call :assemble /sfc/ys_unit.asm
call :assemble /sfc/ys_w11.asm
call :assemble /sfc/ys_w12.asm
call :assemble /sfc/ys_w13.asm
call :assemble /sfc/ys_w14.asm
call :assemble /sfc/ys_w15.asm
call :assemble /sfc/ys_w16.asm
call :assemble /sfc/ys_w17.asm
call :assemble /sfc/ys_w18.asm
call :assemble /sfc/ys_w19.asm
call :assemble /sfc/ys_w21.asm
call :assemble /sfc/ys_w22.asm
call :assemble /sfc/ys_w23.asm
call :assemble /sfc/ys_w24.asm
call :assemble /sfc/ys_w25.asm
call :assemble /sfc/ys_w26.asm
call :assemble /sfc/ys_w27.asm
call :assemble /sfc/ys_w28.asm
call :assemble /sfc/ys_w29.asm
call :assemble /sfc/ys_w31.asm
call :assemble /sfc/ys_w32.asm
call :assemble /sfc/ys_w33.asm
call :assemble /sfc/ys_w34.asm
call :assemble /sfc/ys_w35.asm
call :assemble /sfc/ys_w36.asm
call :assemble /sfc/ys_w37.asm
call :assemble /sfc/ys_w38.asm
call :assemble /sfc/ys_w39.asm
call :assemble /sfc/ys_w41.asm
call :assemble /sfc/ys_w42.asm
call :assemble /sfc/ys_w43.asm
call :assemble /sfc/ys_w44.asm
call :assemble /sfc/ys_w45.asm
call :assemble /sfc/ys_w46.asm
call :assemble /sfc/ys_w47.asm
call :assemble /sfc/ys_w48.asm
call :assemble /sfc/ys_w49.asm
call :assemble /sfc/ys_w51.asm
call :assemble /sfc/ys_w52.asm
call :assemble /sfc/ys_w53.asm
call :assemble /sfc/ys_w54.asm
call :assemble /sfc/ys_w55.asm
call :assemble /sfc/ys_w56.asm
call :assemble /sfc/ys_w57.asm
call :assemble /sfc/ys_w58.asm
call :assemble /sfc/ys_w59.asm
call :assemble /sfc/ys_w61.asm
call :assemble /sfc/ys_w62.asm
call :assemble /sfc/ys_w63.asm
call :assemble /sfc/ys_w64.asm
call :assemble /sfc/ys_w65.asm
call :assemble /sfc/ys_w66.asm
call :assemble /sfc/ys_w67.asm
call :assemble /sfc/ys_w68.asm
call :assemble /sfc/ys_w69.asm
call :assemble /sfc/ys_w70.asm
call :assemble /sfc/ys_ench.asm
call :assemble /sfc/ys_msgdt.asm
call :assemble /sfc/ys_chr.asm












ECHO Assembled .asm files!

ECHO.

ECHO Linking .rel files into a single ROM



set RELINFO0=-rGroup_0=08000,Group_R=c000,Group_1=18000,Group_2=28000,Group_3=38000,Group_4=48000
set RELINFO1=-rGroup_5=58000,Group_6=68000,Group_7=78000,Group_C=c8000,Group_D=d8000,Group_E=e8000,Group_F=fa000
set RELINFO2=-rGroup_10=108000,Group_11=118000,Group_B=BDC00
set RELINFO3=-rGroup_12=128000,Group_13=138000,Group_14=148000,Group_15=158000,Group_16=168000,Group_17=178000
set RELINFO4=-rGroup_4C=4C0000,Group_5F=5F4000

set RELINFO=%RELINFO0% %RELINFO1% %RELINFO2% %RELINFO3% %RELINFO4%



set LINK_FILES=%code_source_dir%/sfc/ys_main.rel %code_source_dir%/sfc/ys_save.rel %code_source_dir%/sfc/ys_title.rel %code_source_dir%/sfc/ys_enmy.rel %code_source_dir%/sfc/ys_enmy2.rel %code_source_dir%/sfc/ys_enmy3.rel %code_source_dir%/sfc/ys_enmy4.rel %code_source_dir%/sfc/ys_enmy5.rel %code_source_dir%/sfc/ys_enmy6.rel %code_source_dir%/sfc/ys_enmy7.rel %code_source_dir%/sfc/ys_enmy8.rel %code_source_dir%/sfc/ys_enmy9.rel %code_source_dir%/sfc/ys_enmy10.rel %code_source_dir%/sfc/ys_enmy11.rel %code_source_dir%/sfc/ys_enmy12.rel %code_source_dir%/sfc/ys_enmy14.rel %code_source_dir%/sfc/ys_boss1.rel %code_source_dir%/sfc/ys_boss2.rel %code_source_dir%/sfc/ys_bbbros.rel %code_source_dir%/sfc/ys_koopa.rel %code_source_dir%/sfc/ys_dorobo.rel %code_source_dir%/sfc/ys_babym.rel %code_source_dir%/sfc/ys_enmy13.rel %code_source_dir%/sfc/ys_exst.rel %code_source_dir%/sfc/ys_bgsc.rel %code_source_dir%/sfc/ys_bgsc0.rel %code_source_dir%/sfc/ys_bgsc1.rel %code_source_dir%/sfc/ys_bgsc2.rel %code_source_dir%/sfc/ys_bonus.rel %code_source_dir%/sfc/ys_start.rel %code_source_dir%/sfc/ys_mini.rel %code_source_dir%/sfc/ys_mini1.rel %code_source_dir%/sfc/ys_ending.rel %code_source_dir%/sfc/ys_demo.rel %code_source_dir%/sfc/ys_demo_1.rel %code_source_dir%/sfc/ys_init.rel %code_source_dir%/sfc/ys_game.rel %code_source_dir%/sfc/ys_play.rel %code_source_dir%/sfc/ys_map.rel %code_source_dir%/sfc/ys_hmap.rel %code_source_dir%/sfc/ys_hlder.rel %code_source_dir%/sfc/ys_rpro.rel %code_source_dir%/sfc/ys_data.rel %code_source_dir%/sfc/ys_pldt.rel %code_source_dir%/sfc/ys_pldt_e.rel %code_source_dir%/sfc/ys_mapdt.rel %code_source_dir%/sfc/ys_mpobj.rel %code_source_dir%/sfc/ys_mpmv.rel %code_source_dir%/sfc/ys_unit.rel %code_source_dir%/sfc/ys_w11.rel %code_source_dir%/sfc/ys_w12.rel %code_source_dir%/sfc/ys_w13.rel %code_source_dir%/sfc/ys_w14.rel %code_source_dir%/sfc/ys_w15.rel %code_source_dir%/sfc/ys_w16.rel %code_source_dir%/sfc/ys_w17.rel %code_source_dir%/sfc/ys_w18.rel %code_source_dir%/sfc/ys_w19.rel %code_source_dir%/sfc/ys_w21.rel %code_source_dir%/sfc/ys_w22.rel %code_source_dir%/sfc/ys_w23.rel %code_source_dir%/sfc/ys_w24.rel %code_source_dir%/sfc/ys_w25.rel %code_source_dir%/sfc/ys_w26.rel %code_source_dir%/sfc/ys_w27.rel %code_source_dir%/sfc/ys_w28.rel %code_source_dir%/sfc/ys_w29.rel %code_source_dir%/sfc/ys_w31.rel %code_source_dir%/sfc/ys_w32.rel %code_source_dir%/sfc/ys_w33.rel %code_source_dir%/sfc/ys_w34.rel %code_source_dir%/sfc/ys_w35.rel %code_source_dir%/sfc/ys_w36.rel %code_source_dir%/sfc/ys_w37.rel %code_source_dir%/sfc/ys_w38.rel %code_source_dir%/sfc/ys_w39.rel %code_source_dir%/sfc/ys_w41.rel %code_source_dir%/sfc/ys_w42.rel %code_source_dir%/sfc/ys_w43.rel %code_source_dir%/sfc/ys_w44.rel %code_source_dir%/sfc/ys_w45.rel %code_source_dir%/sfc/ys_w46.rel %code_source_dir%/sfc/ys_w47.rel %code_source_dir%/sfc/ys_w48.rel %code_source_dir%/sfc/ys_w49.rel %code_source_dir%/sfc/ys_w51.rel %code_source_dir%/sfc/ys_w52.rel %code_source_dir%/sfc/ys_w53.rel %code_source_dir%/sfc/ys_w54.rel %code_source_dir%/sfc/ys_w55.rel %code_source_dir%/sfc/ys_w56.rel %code_source_dir%/sfc/ys_w57.rel %code_source_dir%/sfc/ys_w58.rel %code_source_dir%/sfc/ys_w59.rel %code_source_dir%/sfc/ys_w61.rel %code_source_dir%/sfc/ys_w62.rel %code_source_dir%/sfc/ys_w63.rel %code_source_dir%/sfc/ys_w64.rel %code_source_dir%/sfc/ys_w65.rel %code_source_dir%/sfc/ys_w66.rel %code_source_dir%/sfc/ys_w67.rel %code_source_dir%/sfc/ys_w68.rel %code_source_dir%/sfc/ys_w69.rel %code_source_dir%/sfc/ys_w70.rel %code_source_dir%/sfc/ys_ench.rel %code_source_dir%/sfc/ys_msgdt.rel %code_source_dir%/sfc/ys_chr.rel


%lnk% %LINK_FILES% -o ys_main.hex %RELINFO% -ls ys_main.map


ECHO.


ECHO Converting Hex File

%h2b% -m mario -cff -fys_main.hex -fys_chip0.hex -i%code_source_dir%/sfc/yschr -ihdr -oys_rom -r16


rem del %linker-output%
copy ys_rom %ROM-OUTPUT%







ECHO.

ECHO Created .sfc at %ROM-OUTPUT%!

cd "../Output/"

GOTO :exit

:force_assemble
%asm% %code_source_dir%%1 %asm-vars% -f
exit /b

:assemble
%asm% %code_source_dir%%1 %asm-vars%
exit /b

:exit
pause