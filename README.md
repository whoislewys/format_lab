# format_lab
a script to format my linear algebra labs into something easy for pandoc to convert to pdf
turns diary file into a markdown file with a header that pandoc's mitex plugin recognizes and turns into a cover page, as well as adds two spaces to the end of every line so that newlines get rendered properly (markdown counts this as a newline character).

## Dependencies
You need a python installation. I recommend installing Python through [Miniconda](https://docs.conda.io/en/latest/miniconda.html).
To use Pandoc to convert this markdown file to PDF, install [Pandoc](https://pandoc.org/installing.html) and if you're on windows like me, install [MiKTeX](https://miktex.org/download)

## Usage
`python format_lab.py -i <infile> -o <outfile>.md`
To format your MATLAB diary file to proper markdown + header for Pandoc to read

`pandoc -s <outfile> -o <outfile>.pdf`
To take your formatted markdown file and convert it to PDF with Pandoc
  
## Full Example of Diary -> PDF
`python format_lab.py -i diary.txt -o lab2-final.md`
`pandoc -s lab2-final.md -o lab2-final.pdf`
