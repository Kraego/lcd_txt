"""
Get the Lowest Common Textparts of files (line wise).

Usage:
  lcdtxt.py  [--verbose] <path> [-o=<filename>]
  lcdtxt.py -h | --help
  lcdtxt.py --version

Arguments:
  path    path containing files to compare

Examples:
lcdtxt.py "C:/Temp"

Options:
  -h --help      Show this screen.
  --version      Show version.
  --verbose      print more text
  -o=<filename>  generate output in file instead of shell
"""

from docopt import docopt
import os
import logging


def extract_reference_content(files_to_compare):
  refernce_file = list(files_to_compare.keys())[0]
  reference_content = list(files_to_compare.values())[0]
  del files_to_compare[refernce_file]
  return (refernce_file, reference_content)


def create_file_dict(path):
  files_to_compare = dict()

  for f in os.listdir(path):
    with open(os.path.join(path,f), 'r', encoding='utf-8-sig') as current_file:
      files_to_compare[f] = current_file.read()
  
  return files_to_compare


def remove_last_line_from_string(s):
  logging.info('Removing last line from reference file')
  if s.count('\n') == 0:
    return ''
  else:
    return s[:s.rfind('\n')]


def normalize_content(content):
    return "".join(content.split())
  

def reduce_til_find_in_all(files_to_compare, text_to_search):
  common_text = text_to_search
  
  while len(common_text) > 0:
    match_count = 0

    for current_file, curren_file_content in files_to_compare.items():
      if common_text == curren_file_content:
        match_count = match_count + 1
      elif normalize_content(common_text) in normalize_content(curren_file_content):
        logging.info('Found content in {}'.format(current_file))
        match_count = match_count + 1
      else:
        logging.warning('"{}" is completly different, maybe remove it from comparison'.format(current_file))

    if match_count == len(files_to_compare):
      return common_text
    
    common_text = remove_last_line_from_string(common_text)
  
  logging.info('No overall common text in the file')
  return None


def text_enrichment_try(files_to_compare, current_common_text, reference_content):
  logging.info('Enrich findings!')
  new_current_common = current_common_text
  tryouts = reference_content.replace(current_common_text, '')
  
  if tryouts == '':
    return new_current_common
  
  
  if tryouts[0] == '\n':
    tryouts = tryouts[1:]
  
  first_finding = True
  lines = filter(None, tryouts.split('\n'))
  
  for line in lines:
    match_count = 0
    
    for fileName, fileContent in files_to_compare.items():
      if line in fileContent:
        logging.info('Finding in "{}"'.format(fileName))
        match_count = match_count + 1
        
    if match_count == len(files_to_compare):
      if first_finding:
        new_current_common += '\n'
        first_finding = False   
      new_current_common += line + '\n'
  
  if new_current_common[-1] == '\n':
    new_current_common = new_current_common[:-1]
  
  return new_current_common


def find_common_stuff(path):
  files_to_compare = create_file_dict(path)
  (reference_file, reference_content) = extract_reference_content(files_to_compare)
  logging.info('Using "{}" as reference file'.format(reference_file))
  current_common_text = reduce_til_find_in_all(files_to_compare, reference_content)
  
  if current_common_text != None:
    current_common_text = text_enrichment_try(files_to_compare, current_common_text, reference_content)
  return current_common_text


def main(arguments):
  try:
    if arguments['--verbose']:
      logging.basicConfig(level=logging.DEBUG)
    else:
      logging.basicConfig(level=logging.WARNING)
    
    print('**** Try to find least common lines in documents! ****')
    print()
    
    common = find_common_stuff(arguments['<path>'])
    
    if not arguments['-o']:
      print()
      print('##################################################################################################################')
      print('Common part is:')
      print(common)
      print('##################################################################################################################')
      print()
    else:
      filepath = './{}'.format(arguments['-o'])
      with open(filepath, 'w') as f:
        f.write(common)
        print('Result see "{}"'.format(filepath))
  except Exception as ex:
    print('Unexpected Failure, closing ....')
    print(ex)  
  finally:
    print()
    input("press close to exit")


if __name__ == '__main__':
  arguments = docopt(__doc__, version='0.2')
  main(arguments)
