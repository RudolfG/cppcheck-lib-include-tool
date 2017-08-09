# cppcheck-lib-include-tool
Generate libraries with includes to given Third Party framework

```powershell
usage: genincludes.py [-h] (-b BOOST_DIR | -q QT_DIR | -i INCLUDE_DIR)
                      [-o OUTPUT_FILE]

Generate the include cfg file.

optional arguments:
  -h, --help            show this help message and exit

Supported third party libs:
  -b BOOST_DIR, --boost_dir BOOST_DIR
                        Path to the boost root folder.
  -q QT_DIR, --qt_dir QT_DIR
                        Path to the qt include folder.
  -i INCLUDE_DIR, --include_dir INCLUDE_DIR
                        Path to the include folder.

Output:
  -o OUTPUT_FILE, --output_file OUTPUT_FILE
                        The path to the output file (default: stdout)
```

## Example
### Generate Qt 4.x-Include library file:
```powershell
PS> & python ./genincludes.py -q C:/Qt/4.8.7/include -o C:/cppcheck/cfg/qt4-includes.cfg
```

### Generate Qt 5.x-Include library file:
```powershell
PS> & python ./genincludes.py -q C:/Qt/5.9.1/msvc2017_64/include -o C:/cppcheck/cfg/qt5-includes.cfg
```

### Generate Boost-Include library file:
```powershell
PS> & python ./genincludes.py -b C:/boost/boost_1_64_0 -o C:/cppcheck/cfg/boost-includes.cfg
```

### Generate for every other third party the library file from the include folder (In this example OpenSSL).
With **-i** you can enter the path to every third party include folder, that don't need special handling 
```powershell
PS> & python ./genincludes.py -i C:/OpenSSL-Win32/include -o C:/cppcheck/cfg/openssl-includes.cfg
```
