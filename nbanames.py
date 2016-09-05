# Made by Divyesh Chotai 2016

import re
import urllib

"""
Extracts the names of all historical NBA players and writes a text file containing combinations of two players' names, 
e.g. LeBron James Harden and Chris Paul George. NBA player data is extracted from http://www.basketball-reference.com/
"""

results=[]

# Extract all the names and store into a list named 'results'
def extract_names():
  letters = 'abcdefghijklmnopqrstuvwxyz'
  for each in letters:
    bballreference = 'http://www.basketball-reference.com/players/%s' % (each)
    ufile = urllib.urlopen(bballreference)
    reader = ufile.read()
    old_names = re.findall(r'html">(.+\s\w+)?</a></th>', reader)
    active_names = re.findall(r'html">(.+\s\w+)?</a></strong></th>', reader)
    for name in old_names:
      results.append(name)
    for name in active_names:
      results.append(name)
# Split each name into first and last name, then look for all name combinations and return them
def intersect_names():
  namesplit = [item.split() for item in results]
  final = [''.join(x[0] + ' ' + x[1] + ' ' + y[1]) for x in namesplit for y in namesplit if x[1]==y[0]]
  return final

def main():
  print 'Extracting names...'
  extracted = extract_names()
  print 'Names extracted.'

  intersect = sorted(intersect_names())
  f = open('nbanames.txt', 'w')
  f.write('\n'.join(intersect))
  f.close()
  print 'Merged names written to ' + f.name


if __name__ == '__main__':
  main()