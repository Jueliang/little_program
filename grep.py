# -*- coding:utf-8 -*-  
#
# for Python3 and Python2
# File: grep.py
# Date: 2018/3/22


import io,sys,re
import argparse




parser = argparse.ArgumentParser(description='Grep with Python')

parser.add_argument( '-H', action='store_true', dest="with_filename", help='print with filename')  
parser.add_argument( '-n', action='store_true', dest="line_number", help='print line number')  

parser.add_argument( "-e", "--regex", dest="regex", action='append', type=str, help="regex patterns" )  # -e "[Tt]alk]" -e "\b\d+\b" -e ...

parser.add_argument( 'filenames', nargs='*' ) # python grep.py [OPTIONS] file1 file2 ...

args = parser.parse_args()












patterns = []

for item in args.regex:
    patterns.append( re.compile(item) )
#end{for}    

def print_line( linetext, filename, line_number):
    if args.with_filename or args.line_number:
        texts = []

        if args.with_filename:
            texts.append( filename )
        #end{if}

        if args.line_number:
            if args.with_filename:
                texts.append( ':' )
            #end{if}
            texts.append( str(line_number) )
        #end{if}

        if args.with_filename or args.line_number:
            texts.append( '  ' )
        #end{if}

        texts.append( linetext )

        print("".join(texts))
    else:
        print( linetext )
#end{def}    
    

def search_line( line, filename, line_number ):
    for prog in patterns:
        m = prog.search( line )
        if m:
            print_line( line, filename, line_number)
            break
        #end{if}
    #end{for}
#end{def}


def grep():
    for fname in args.filenames:        
        with open( fname ) as f:
            line_count = 1
            for line in f:
                search_line( line, fname, line_count )
                line_count = line_count + 1
            #end{for} 
        #end{with}
    #end{for}
#end{def}

grep()



