#! /usr/bin/env python
# -*- coding:utf-8 -*-  
#
# for Python 3 only
#
# File: mp3id3.py

import sys, os
import json

import argparse



import pprint
from mutagen.easyid3 import EasyID3



'''
    "TALB": "album", # 专集
    "TBPM": "bpm",
    "TCMP": "compilation",  # iTunes extension
    "TCOM": "composer",
    "TCOP": "copyright",
    "TENC": "encodedby",
    "TEXT": "lyricist",
    "TLEN": "length",
    "TMED": "media",
    "TMOO": "mood",
    "TIT2": "title", # 标题
    "TIT3": "version",
    "TPE1": "artist", # 作者
    "TPE2": "albumartist", # 艺术家
    "TPE3": "conductor",
    "TPE4": "arranger",
    "TPOS": "discnumber",
    "TPUB": "organization",
    "TRCK": "tracknumber", # 音轨 格式:N/M。 其中 N 为专集中的第 N 首,M 为专集中共 M 首,N 和 M 为 ASCII 码表示的数字
    "TOLY": "author",
    "TSO2": "albumartistsort",  # iTunes extension
    "TSOA": "albumsort",
    "TSOC": "composersort",  # iTunes extension
    "TSOP": "artistsort",
    "TSOT": "titlesort",
    "TSRC": "isrc",
    "TSST": "discsubtitle",
    "TLAN": "language",
    
    -----------------------------------
    "TYER", # 年代 是用 ASCII 码表示的数字
    "TCON": Content type 类型 直接用字符串表示
    "COMM": "", 
    "TOPE": # 艺术家

{
    'album': ['唱片集'], 
    'title': ['标题'], 
    'artist': ['参与创作的艺术家'], 
    'albumartist': ['艺术家'], 
    'tracknumber': ['10']

}

### [id3v2.3.0: 4. Declared ID3v2 frames ](#http://id3.org/id3v2.3.0)

4.20    AENC    [[#sec4.20|Audio encryption]]
4.15    APIC    [#sec4.15 Attached picture]
4.11    COMM    [#sec4.11 Comments]
4.25    COMR    [#sec4.25 Commercial frame]
4.26    ENCR    [#sec4.26 Encryption method registration]
4.13    EQUA    [#sec4.13 Equalization]
4.6     ETCO    [#sec4.6 Event timing codes]
4.16    GEOB    [#sec4.16 General encapsulated object]
4.27    GRID    [#sec4.27 Group identification registration]
4.4     IPLS    [#sec4.4 Involved people list]
4.21    LINK    [#sec4.21 Linked information]
4.5     MCDI    [#sec4.5 Music CD identifier]
4.7     MLLT    [#sec4.7 MPEG location lookup table]
4.24    OWNE    [#sec4.24 Ownership frame]
4.28    PRIV    [#sec4.28 Private frame]
4.17    PCNT    [#sec4.17 Play counter]
4.18    POPM    [#sec4.18 Popularimeter]
4.22    POSS    [#sec4.22 Position synchronisation frame]
4.19    RBUF    [#sec4.19 Recommended buffer size]
4.12    RVAD    [#sec4.12 Relative volume adjustment]
4.14    RVRB    [#sec4.14 Reverb]
4.10    SYLT    [#sec4.10 Synchronized lyric/text]
4.8     SYTC    [#sec4.8 Synchronized tempo codes]
4.2.1   TALB    [#TALB Album/Movie/Show title]
4.2.1   TBPM    [#TBPM BPM (beats per minute)]
4.2.1   TCOM    [#TCOM Composer]
4.2.1   TCON    [#TCON Content type]
4.2.1   TCOP    [#TCOP Copyright message]
4.2.1   TDAT    [#TDAT Date]
4.2.1   TDLY    [#TDLY Playlist delay]
4.2.1   TENC    [#TENC Encoded by]
4.2.1   TEXT    [#TEXT Lyricist/Text writer]
4.2.1   TFLT    [#TFLT File type]
4.2.1   TIME    [#TIME Time]
4.2.1   TIT1    [#TIT1 Content group description]
4.2.1   TIT2    [#TIT2 Title/songname/content description]
4.2.1   TIT3    [#TIT3 Subtitle/Description refinement]
4.2.1   TKEY    [#TKEY Initial key]
4.2.1   TLAN    [#TLAN Language(s)]
4.2.1   TLEN    [#TLEN Length]
4.2.1   TMED    [#TMED Media type]
4.2.1   TOAL    [#TOAL Original album/movie/show title]
4.2.1   TOFN    [#TOFN Original filename]
4.2.1   TOLY    [#TOLY Original lyricist(s)/text writer(s)]
4.2.1   TOPE    [#TOPE Original artist(s)/performer(s)]
4.2.1   TORY    [#TORY Original release year]
4.2.1   TOWN    [#TOWN File owner/licensee]
4.2.1   TPE1    [#TPE1 Lead performer(s)/Soloist(s)] => "artist", 作者
4.2.1   TPE2    [#TPE2 Band/orchestra/accompaniment]
4.2.1   TPE3    [#TPE3 Conductor/performer refinement]
4.2.1   TPE4    [#TPE4 Interpreted, remixed, or otherwise modified by]
4.2.1   TPOS    [#TPOS Part of a set]
4.2.1   TPUB    [#TPUB Publisher]
4.2.1   TRCK    [#TRCK Track number/Position in set]
4.2.1   TRDA    [#TRDA Recording dates]
4.2.1   TRSN    [#TRSN Internet radio station name]
4.2.1   TRSO    [#TRSO Internet radio station owner]
4.2.1   TSIZ    [#TSIZ Size]
4.2.1   TSRC    [#TSRC ISRC (international standard recording code)]
4.2.1   TSSE    [#TSEE Software/Hardware and settings used for encoding]
4.2.1   TYER    [#TYER Year]
4.2.2   TXXX    [#TXXX User defined text information frame]
4.1     UFID    [#sec4.1 Unique file identifier]
4.23    USER    [#sec4.23 Terms of use]
4.9     USLT    [#sec4.9 Unsychronized lyric/text transcription]
4.3.1   WCOM    [#WCOM Commercial information]
4.3.1   WCOP    [#WCOP Copyright/Legal information]
4.3.1   WOAF    [#WOAF Official audio file webpage]
4.3.1   WOAR    [#WOAR Official artist/performer webpage]
4.3.1   WOAS    [#WOAS Official audio source webpage]
4.3.1   WORS    [#WORS Official internet radio station homepage]
4.3.1   WPAY    [#WPAY Payment]
4.3.1   WPUB    [#WPUB Publishers official webpage]
4.3.2   WXXX    [#WXXX User defined URL link frame]


### [id3（Sound.id3 属性）](#https://help.adobe.com/zh_CN/AS2LCR/Flash_10.0/help.html?content=00001523.html)

属性    说明
-----------------------------
TALB   专辑
TCON   genre
TIT2   标题/歌曲名称/内容描述
TPE1   id3.artist 领衔演奏者/独唱（奏）者
TRCK   音轨 格式:N/M。 其中 N 为专集中的第 N 首,M 为专集中共 M 首,N 和 M 为 ASCII 码表示的数字

TFLT   文件类型
TIME   时间
TIT1   内容组描述
TIT3   副标题/主要描述
TKEY   最初关键字
TLAN   语言
TLEN   长度
TMED   媒体类型
TOAL   原唱片/影片/演出名称
TOFN   原文件名
TOLY   原词作者/乐谱作者
TOPE   原艺术家/演奏者
TORY   最初发行年份
TOWN   文件所有者/许可证持有人
TPE1   领衔演奏者/独唱（奏）者
TPE2   乐队/交响乐队/伴奏
TPE3   指挥/主要演奏者
TPE4   翻译、混录员、或修改者
TPOS   作品集的部分
TPUB   发行人
TRCK   音轨编号/作品集中的位置
TRDA   录制日期
TRSN   Internet 电台名称
TRSO   Internet 电台所有者
TSIZ   大小
TSRC   ISRC（国际标准音像制品编码）
TSSE   编码使用的软件/硬件和设置
TYER   年份
WXXX   URL 链接帧
COMM   Sound.id3.comment
TYER   Sound.id3.year


### 

TEXT： 歌词作者 
TENC： 编码
WXXX： URL链接(URL) 
TCOP： 版权(Copyright)
TOPE： 原艺术家 
TCOM： 作曲家
TDAT： 日期 
TPE3： 指挥者
TPE2： 乐队 
TPE1： 艺术家相当于ID3v1的Artist
TPE4： 翻译（记录员、修改员） 
TYER： 年代相当于ID3v1的Year
USLT： 歌词 
TALB： 专辑相当于ID3v1的Album
TIT1： 内容组描述 
TIT2： 标题相当于ID3v1的Title
TIT3： 副标题 
TCON： 流派（风格）相当于ID3v1的Genre见下表
TBPM： 每分钟节拍数 
COMM： 注释相当于ID3v1的Comment
TDLY： 播放列表返录 
TRCK： 音轨（曲号）相当于ID3v1的Track
TFLT： 文件类型 
TIME： 时间　
TKEY： 最初关键字 
TLAN： 语言
TLEN： 长度 
TMED： 媒体类型
TOAL： 原唱片集 
TOFN： 原文件名
TOLY： 原歌词作者 
TORY： 最初发行年份
TOWM： 文件所有者（许可证者） 
TPOS： 作品集部分
TPUB： 发行人 
TRDA： 录制日期
TRSN： Intenet电台名称 
TRSO： Intenet电台所有者
TSIZ： 大小 　 
TSRC： ISRC（国际的标准记录代码）
TSSE： 编码使用的软件（硬件设置） 
UFID： 唯一的文件标识符
AENC： 音频加密技术 　 

'''


def setup_id3( filename, **keywords ):
    
    song = EasyID3( filename )

    for key in keywords:
        song[key] = keywords[key]
    #end{for}

    #save( filething, v1=1, v2_version=4, v23_sep='/', padding=None):
    #        v1 (ID3v1SaveOptions):
    #            if 0, ID3v1 tags will be removed.
    #            if 1, ID3v1 tags will be updated but not added.
    #            if 2, ID3v1 tags will be created and/or updated

    # Sony NW-ZX100 播放器不支持 v2.4，只支持 v2.3
    song.save( v1=0, v2_version=3 )

#end{def}



def dump_id3( filename ):
    song = EasyID3( filename )

    #print( EasyID3.valid_keys.keys() )

    print( '《%s》:' %  filename )
    
    #print( song )

    for k, v in song.items(): 
        print( '%-24s : %s' %( str(k), str(v)) )
    #end{if}

    print( '\n' )
    print( song.pprint() )

    print( '\nkeys():' )
    print( song.keys() )

#end{def}


def clear_id3( filename ):
    song = EasyID3( filename )

    song.delete( delete_v1=True, delete_v2=True)

    song.save()
#end{def}




if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument( "--dump", dest='dump', action='store_true', help='显示 ID 信息')
    parser.add_argument( "--clear", dest='clear', action='store_true', help='清除 ID 信息')

    parser.add_argument("--artist", dest='artist',type=str, help='参与创作的艺术家')
    parser.add_argument("--album",  dest='album',type=str, help='专辑')
    parser.add_argument("--title", dest='title',type=str, help='标题')
    parser.add_argument("--track", dest='track',type=str, help='轨道编号')
    parser.add_argument("--tracknumber", dest='tracknumber',type=str, help='轨道编号')


    parser.add_argument("--albumartist", dest='albumartist',type=str, help='专辑艺术家')


    parser.add_argument('filename')     # 输入文件 

    args = parser.parse_args()


    if args.dump:
        dump_id3( args.filename )

    elif args.clear:
        clear_id3( args.filename )

    else:
        params = {}

        #param_names = ['artist', 'album', 'title', 'track']
        #for item in param_names and item in args:
        #    params[ item ] = args[ item ]
        ##end{for}

        if args.artist:
            params['artist'] = args.artist
        #end{if}

        if args.albumartist:
            params['albumartist'] = args.albumartist
        #end{if}

        if args.album:
            params['album'] = args.album
        #end{if}

        if args.title:
            params['title'] = args.title
        #end{if}

        if args.track:
            params['tracknumber'] = args.track
        #end{if}

        if args.tracknumber:
            params['tracknumber'] = args.tracknumber
        #end{if}

        setup_id3( args.filename, **params )

    #end{if}

#end{if}
