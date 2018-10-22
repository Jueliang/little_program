#!/usr/bin/python  
# -*- coding: utf-8 -*-
#






import os
import sys
import io  
import os.path  

import re
from mutagen.easyid3 import EasyID3


'''
新概念1/17_L031.mp3 => 第31课

album                    : ['新概念英语1']
title                    : ['新概念1.31']
artist                   : 
albumartist              : 
tracknumber              : ['17']
'''



def modify_id3( filename, volume, tracknum, lessen ):        
    song = EasyID3( filename )

    song['title'] = '新概念%s.%s' % ( volume, lessen )
    song['tracknumber'] = tracknum

    song.save( v1=0, v2_version=3 )

#end{def}

pattern = re.compile( '^(\d+)_L(\d+).mp3$' )

for name in os.listdir('.'):
    if os.path.isdir( name ):
        m = re.match( '^新概念(\d)$', name )
        if m:
            dirname = os.path.join( '.',name)
            volume = m.group(1)

            for filename in os.listdir(dirname):
                fullname = os.path.join( dirname, filename)
                if os.path.isfile( fullname ):
                    m = pattern.match( filename )
                    if m:
                        modify_id3( fullname, volume, m.group(1), m.group(2) ) 
                    #end{if}
                #end{if}
            #end#{if}
        #end{if}
    #end{if}
#end{for}


