# -*- coding:utf-8 -*-  
#
# for Python3 and Python2
# File: grep.py
#


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

def print_line(filename, line, line_number):
    text = []
    if args.with_filename:
        text.append( filename )
    #end{if}

    if args.line_number:
        if args.with_filename:
            text.append( ':' )
            text.append( str(line_number) )
        else:
            text.append( str(line_number) )
        #end{if}
        text.append( '  ' )
    else:
        if args.with_filename:
            text.append( '  ' )
        #end{if}
    #end{if}

    text.append( line )

    if sys.version_info.major == 2:
        print "".join(text)
    else:
        print( "".join(text) )
    #end{if}        
#end{def}    
    

def search( filename, line, line_number ):
    for prog in patterns:
        m = prog.search( line )
        if m:
            print_line(filename, line, line_number)
            break
        #end{if}
    #end{for}
#end{def}


def grep():
    for fname in args.filenames:
        with open( fname ) as f:
            line_count = 1
            for line in f:
                search( fname, line, line_count )
                line_count = line_count + 1
            #end{for} 
        #end{with}
    #end{for}
#end{def}


grep()



