# -*- coding: utf-8 -*-

# ------------------------------------
# python modules
# ------------------------------------

import os
import sys
import argparse as ap
import tempfile

# ------------------------------------
# own python modules
# ------------------------------------

from BOX.constants import *

# ------------------------------------
# Main function
# ------------------------------------

def main():
    # Parse options...
    argparser = prepare_argparser()
    args = argparser.parse_args()
#    if args.out_dir:
#       # use a output directory to store UMIduplicates output
#        if not os.path.exists( args.out_dir ):
#            try:
#                os.makedirs( args.out_dir )
#            except:
#                sys.exit( "Output directory (%s) could not be created. Terminating program." % args.out_dir )
    subcommand  = args.subcommand_name
    #oneFolder
    if subcommand == "oneFolder":
        from ILLUSTRATE.oneFolder import main
        main(args)
    #manyFolders
    if subcommand == "manyFolders":
        from ILLUSTRATE.manyFolders import main
        main(args)
    
# make subcommand    
def prepare_argparser ():
    """Prepare optparser object. New options will be added in this function first.
    """
    #%(prog)s means getting program name
    #other methods %(prog)s : sys.argv[0] or argparse.ArgumentParser(prog='hoge.py')
    description = "%(prog)s -- Getting thumbnails with using BOX API"
    epilog = "For command line options of each command, type: %(prog)s COMMAND -h"
    #Check community site:
    #Source code:
    # top-level parser
    argparser = ap.ArgumentParser(description = description, epilog = epilog) #, usage = usage )
    argparser.add_argument("--version", action="version", version="%(prog)s " + VERSION)
    subparsers = argparser.add_subparsers(dest = 'subcommand_name' ) #help="sub-command help")

    # command for 'oneFolder'
    add_oneFolder_parser(subparsers)
    # command for 'manyFolders'
    add_manyFolders_parser(subparsers)
    return argparser
# make oudir option   
def add_outdir_option (parser):
    parser.add_argument("--outdir", dest = "out_dir", type = str, default = './',
                        help = "If specified all output files will be written to that directory. Default: the current working directory")
def add_output_group (parser, required = True ):
    output_group = parser.add_mutually_exclusive_group( required = required )
    output_group.add_argument("-o", "--ofile", dest = "ofile", type = str,
                               help = "Output file name. Mutually exclusive with --o-prefix.")
    output_group.add_argument("--o-prefix", dest = "oprefix", type = str,
                               help = "Output file prefix. Mutually exclusive with -o/--ofile.")
# make oneFolder subcommand argparser
def add_oneFolder_parser(subparsers):
    """Add main function 'oneFolder' argument parsers.
    """
    argparser_oneFolder = subparsers.add_parser("oneFolder", help = "Get thumbnails in one folder.")
    # group for input files
    group_input = argparser_oneFolder.add_argument_group("Input files arguments")
    group_input.add_argument("-i", "--folderid", dest = "folder_id", type = str, required = True,
                              help = "Paste proper folder id to get thumbnails you want. Folder_id is displayed the second to last directory in a path ex: https://.app.box.com/files/0/f/this_is_folder_id/this_is_folder_name REQUIRED.")
    group_input.add_argument("-t", "--token", dest = "ACCESS_TOKEN", type = str, required = True,
                              help = "Paste developer token. time limit is 60 minutes from revoked and reissued. REQUIRED.")
    group_input.add_argument("-s", "--size", dest = "size", type = str, required = True,
                              help = "thumbnail size you want. REQUIRED.")
    # group for output files
    group_output = argparser_oneFolder.add_argument_group("Output arguments")
    add_outdir_option(group_output)
    group_output.add_argument("-n", "--name", dest = "name", type = str,
                               help = "Project name, which will be used to generate output file names. DEFAULT: \"NA\"",
                               default = "NA")
# make oneFolder subcommand argparser
def add_manyFolders_parser(subparsers):
    """Add main function 'manyFolders' argument parsers.
    """
    argparser_manyFolders = subparsers.add_parser("manyFolders", help = "Get thumbnails in many folders.")
    # group for input files
    group_input = argparser_manyFolders.add_argument_group("Input files arguments")
    group_input.add_argument("-i", "--folderid", dest = "folder_id", type = str, required = True,
                              help = "Paste proper folder id to get thumbnails you want. This folder_id maybe parent folder. Folder_id is displayed the second to last directory in a path ex: https://.app.box.com/files/0/f/this_is_folder_id/this_is_folder_name REQUIRED.")
    group_input.add_argument("-t", "--token", dest = "ACCESS_TOKEN", type = str, required = True,
                              help = "Paste developer token. time limit is 60 minutes from revoked and reissued. REQUIRED.")
    group_input.add_argument("-s", "--size", dest = "size", type = str, required = True,
                              help = "Thumbnail size you want. REQUIRED.")
    # group for output files
    group_output = argparser_manyFolders.add_argument_group("Output arguments")
    add_outdir_option(group_output)
    group_output.add_argument("-n", "--name", dest = "name", type = str,
                               help = "Project name, which will be used to generate output file names. DEFAULT: \"NA\"",
                               default = "NA")
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.stderr.write("User interrupted me! ;-) Bye!\n")
        sys.exit(0)

