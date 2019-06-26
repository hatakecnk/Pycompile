# uncompyle6 version 3.3.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.16 (default, Apr 24 2019, 10:05:31) 
# [GCC 4.2.1 Compatible Android (5058415 based on r339409) Clang 8.0.2 (https://a
# Embedded file name: Pycompile.py
# Compiled at: 2019-06-21 12:43:36
import os, sys
from time import sleep
from py_compile import compile

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        sleep(0.05)


os.system('clear')
banner = '\n\x1b[35;1m___  _   _ ____    ____ ____ _  _ ___  _ _    ____\n\x1b[35;1m|__]  \\_/  |       |    |  | |\\/| |__] | |    |___\n\x1b[35;1m|      |   |___    |___ |__| |  | |    | |___ |___ \n\x1b[33;1m* \x1b[34;1mAuthor    \x1b[31;1m: \x1b[36;1mNaruto-Kun\n\x1b[33;1m* \x1b[34;1mDibuat    \x1b[31;1m: \x1b[36;1mJumat 09:00\n\x1b[33;1m* \x1b[34;1mTeam      \x1b[31;1m: \x1b[36;1m2E4H \x1b[31;1m| \x1b[36;1mNight People Team \x1b[31;1m| \x1b[36;1mBCA\n\x1b[33;1m* \x1b[34;1mThanks To \x1b[31;1m: \x1b[36;1mXerXez777\x1b[31;1m|\x1b[36;1mExtinction\x1b[31;1m|\x1b[36;1mDUKUN\x1b[31;1m|\x1b[36;1mAll Member 2E4H\x1b[31;1m|\x1b[36;1mNight People\x1b[31;1m|\x1b[36;1mBCA\n\x1b[33;1m* \x1b[34;1mGitHub    \x1b[31;1m: \x1b[32;1mhttps://github.com/SmileBitch21'
print banner
print 50 * '\x1b[0;1m\xe2\x95\x90'
print ''
yn = raw_input('\x1b[33;1m[\x1b[32;1m*\x1b[33;1m] \x1b[32;0mGw Gans Ato Gak y/n ')
if yn == 'y' or yn == 'yes':
    os.system('clear')
    print banner
    print 50 * '\x1b[0;1m\xe2\x95\x90'
    print ''
    file = raw_input('\x1b[0;1m[!] Masukan Script Anda => \x1b[34;1m')
    jalan('\x1b[33;1m[\x1b[32;1m!\x1b[33;1m] Bentar,Lagi Compile Bangsat \x1b[31;1m...')
    sleep(3)
    compile(file)
    os.system('clear')
    print banner
    print 50 * '\x1b[0;1m\xe2\x95\x90'
    print ''
    print '\x1b[33;1m[\x1b[32;1m\xe2\x88\x9a\x1b[33;1m] \x1b[32;1mSucces \x1b[31;1m: \x1b[32;1mKetik ls Untuk Melihat Script Yang Sudah Di Compile'
else:
    if yn == 'n' or yn == 'no':
        print '\x1b[31;1m[!] Bangsat Kau!\n\x1b[31;1m[!] Exit..'
        sleep(5)
    else:
        print '\x1b[31;1m[!] Pilih Yang Bener Bangsat'