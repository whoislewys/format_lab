import argparse
import os

HEADER_STR = '''---
title: "MAT 343 MATLAB Lab 1"
author: "Luis Gomez"
date: "1/15/2019"
geometry: margin=1in
output: pdf_document
---

\pagebreak

'''

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Format a MATLAB diary file into something pandoc can cleanly move to PDF')
  parser.add_argument('-i', dest='infile_str')
  parser.add_argument('-o', dest='outfile_str')
  args = parser.parse_args()
  
  with open(os.path.normpath(args.infile_str)) as infile:
    with open(os.path.normpath(args.outfile_str), 'w') as outfile:
      outfile.write(HEADER_STR)
      for line in infile:
        outfile.write(line[:len(line)-1] + '  \n')
