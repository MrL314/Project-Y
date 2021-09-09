# Project-Y
Toolchain to build Yoshi's Island (J) V1.0 from source code, by MrL314

Last updated: September 8, 2021

---

## Setup

1. To begin, **[download this toolchain](https://github.com/MrL314/Project-Y/archive/refs/heads/main.zip)** and obtain the folder called `other\SFC\ソースデータ\ヨッシーアイランド\日本_Ver0` from the July 2020 gigaleak.
	* You obtain these files at your own risk.
2. Copy the CONTENTS of the `日本_Ver0` folder (not the folder itself) into the folder named `VER_0` included with this tool.

3. Run `setup.bat`, and ensure there are no errors.

---
## Building the Yoshi's Island JPN V1.0 ROM

1. After completing the **Setup** step, run `build.bat`.

2. The built ROM will appear in the `Output` folder. It will be called `VER_0.sfc`.

---
## Running raw python files

If there are any issues running the executables, I have also included the source python files. In each bat file, wherever an executable is called, change to the relevant call to run the python script instead. Executables are called in `setup.bat` (with `createSource` being called), and in `Tools\createROM`, where you may change the relevant calls for the lines:
- `set asm=...`
- `set lnk=...`
- `set h2b=...`

Change these to run the relevant python scripts. 

---
## Special Thanks
- venen
- xprism
- dirtbag
- SmorBjorn
- SMKW Community
- and YOU!

Extra special thanks to:
- R4M0N
- dirtbag
- xerofdv
- furvent
- ScouB
- Brian Mazzarella
- kandowontu
- DaVince
- starxon
- firewaster
- Olivier Cahagne
- Laszlo

I wouldn't have been able to work on projects like this without your support!

---
## GNU License
Project Y is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
