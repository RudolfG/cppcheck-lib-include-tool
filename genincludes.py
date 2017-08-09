from pathlib import Path
import os
import argparse
import sys
from os import listdir
from os.path import isfile, join, isdir
from glob import glob

def output(logger, message):
    logger.write(message + '\n')

def printCfgHeader(logger):
    output(logger, '<?xml version="1.0"?>')
    output(logger, '<def format="2">')

def printCfgFooter(logger):
    output(logger, '</def>')

# Generate Qt include entries without the private includes
def generateQtIncludeEntries(qt_include_dir, logger):
    onlyfolders = sorted([f for f in listdir(qt_include_dir) if isdir(join(qt_include_dir, f))], key=str.lower)
    entries = {}
    upperEntries = []

    for folder in onlyfolders:
        tmp = sorted([f.replace(".h", "") for f in listdir(join(qt_include_dir, folder)) if isfile(join(qt_include_dir, folder, f)) and (Path(join(qt_include_dir, folder, f)).suffix == ".h" or Path(join(qt_include_dir, folder, f)).suffix == "")])
        upperEntries = sorted(set([f.replace(".h", "").upper() for f in listdir(join(qt_include_dir, folder)) if isfile(join(qt_include_dir, folder, f))]))

        folderEntries = []
        for f in tmp:
            if (f.upper() in upperEntries):
                upperEntries.remove(f.upper())
                folderEntries.append(f)
        
        entries[folder] = sorted(folderEntries, key=str.lower)

    printCfgHeader(logger)
    output(logger, '   <!-- THIS ENTRIES ARE GENERATED AUTOMATICALLY. See https://github.com/RudolfG/cppcheck-lib-include-tool -->')

    for key in entries.keys():    
       output(logger, '   <!-- ' + key + '-->')
       for entry in entries[key]:
          output(logger, '   <include name="' + entry + "," + key + '/' + entry + '" />')

    output(logger, '   <!-- AUTOMATICALLY GENERATED END. -->')
    printCfgFooter(logger)

# Generate include entries for every file in the boost include folder
def generateBoostIncludeEntries(boost_path, logger):
    boost_base_include = 'boost'

    if (not isdir(join(boost_path, boost_base_include))):
        print('Error: Invalid boost root path!', file=sys.stderr)
        return

    result = sorted([Path(y).relative_to(boost_path).as_posix() for x in os.walk(join(boost_path, boost_base_include)) for y in glob(os.path.join(x[0], '*.*'))], key=str.lower)
    
    printCfgHeader(logger)
    output(logger, '   <!-- THIS ENTRIES ARE GENERATED AUTOMATICALLY. See https://github.com/RudolfG/cppcheck-lib-include-tool -->')

    for item in result:
        output(logger, '   <include name="' + item + '" />')

    output(logger, '   <!-- AUTOMATICALLY GENERATED END. -->')
    printCfgFooter(logger)

parser = argparse.ArgumentParser(description='Generate the include cfg file.')
group_i = parser.add_argument_group('Supported third party libs')
group_i = group_i.add_mutually_exclusive_group(required=True)
group_i.add_argument('-b', '--boost_dir', type=str, help='Path to the boost root folder')
group_i.add_argument('-q', '--qt_dir', type=str, help='Path to the qt include folder')
group_o = parser.add_argument_group('Output')
group_o.add_argument('-o', '--output_file', help='The path to the output file (default: stdout)', type=argparse.FileType('w'), default=sys.stdout)


menu = parser.parse_args()

if (menu.qt_dir is not None):
    generateQtIncludeEntries(menu.qt_dir, menu.output_file)
elif (menu.boost_dir is not None):
    generateBoostIncludeEntries(menu.boost_dir, menu.output_file)
else:
    print('Invalid third party lib', file=sys.stderr)