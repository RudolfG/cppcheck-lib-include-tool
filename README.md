# cppcheck-lib-include-tool
Generate libraries with includes to given Third Party framework

```powershell
usage: getqtincludes.py [-h] (-b BOOST_DIR | -q QT_DIR) [-o OUTPUT_FILE]

Generate the include cfg file.

optional arguments:
  -h, --help            show this help message and exit
  -b BOOST_DIR, --boost_dir BOOST_DIR
                        Path to the boost root folder
  -q QT_DIR, --qt_dir QT_DIR
                        Path to the qt include folder

Output:
  -o OUTPUT_FILE, --output_file OUTPUT_FILE
                        The path to the output file (default: stdout)
```
