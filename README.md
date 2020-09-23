<!-- omit in toc -->
# lcd_txt
Lowest common denominator of text in files of folder.
Line by line.

- [How to use it](#how-to-use-it)
- [How to build](#how-to-build)
- [Missing stuff/improvements:](#missing-stuffimprovements)

# How to use it
* Run it from source
  * Open shell (help text will be shown): 
    * *py .\source\lcdtxt.py -h*
    * Example: *py .\source\lcdtxt.py ".\testdata\scenarioSame" -o "commontext.txt"*
* Run build:
  * Open shell
    * *lcdtxt.exe -h* (see above)

# How to build

* (Install pyinstall: *pip install pyinstaller*)
* run pyinstall 
  * *pyinstaller lcdtxt.spec*
* You will finde the exe in the dist folder of the project

# Missing stuff/improvements:

* Ignore comments via param:
  * f.e.: -ignorelinecomment "//" and -ignoreblockcomment "/* */"
* Buildspec for linux and mac os - currently just windows
