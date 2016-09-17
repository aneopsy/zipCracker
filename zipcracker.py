#!/usr/bin/python

import argparse
import zipfile
import os
import sys
from time import time

VERSION = '1.0'
AUTHOR = "AneoPsy"


def _cli_opts():
    '''
    Parse command line options.
    @returns the arguments
    '''
    mepath = unicode(os.path.abspath(sys.argv[0]))
    mebase = '%s' % (os.path.basename(mepath))
    description = '''Zip cracker.'''
    desc = argparse.RawDescriptionHelpFormatter
    parser = argparse.ArgumentParser(prog=mebase,
                                     description=description,
                                     formatter_class=desc,
                                     )

    parser.add_argument('-f', '--file',
                        action='store',
                        help='zip file',
                        required=True)
    parser.add_argument('-w', '--word_list',
                        action='store',
                        help='word_list file',
                        required=True)
    parser.add_argument('-V', '--version',
                        action='version',
                        version='%(prog)s v' + VERSION + " by " + AUTHOR)

    args = parser.parse_args()

    return args


def main(args):

    try:
        zip_ = zipfile.ZipFile(args.file)
    except zipfile.BadZipfile:
        print "Please check the file's path. It doesn't seem to be a zip file."
        sys.exit(1)

    password = None
    i = 0
    c_t = time()

    try:
        max_lines = sum(1 for line in open(args.word_list, 'r'))
    except Exception:
        print "Error: wordlist not found!"
        sys.exit(1)
    with open(args.word_list, "r") as f:
        passes = f.readlines()
        for x in passes:
            i += 1
            password = x.split("\n")[0]
            try:
                zip_.extractall(pwd=password)
                t_t = time() - c_t
                print "\n\nPassword cracked: %s\n" % password
                print "Took %f seconds to crack the password. That is, "\
                      "%i attempts per second." % (t_t, i / t_t)
                sys.exit(1)
            except Exception:
                pass
            output = "%*d / %d | %6.2f%% key -> %s" % (len(str(max_lines)),
                                                       i,
                                                       max_lines,
                                                       100 * (i + 1) / max_lines,
                                                       password
                                                       )
            sys.stdout.write('\b' * 80)
            sys.stdout.write(output)
            sys.stdout.flush()

if __name__ == '__main__':
    args = _cli_opts()
    try:
        main(args)
    except KeyboardInterrupt:
        print "\nExit..."
        sys.exit(1)
