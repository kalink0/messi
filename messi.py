#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# AUTHOR:         kalink0
# MAIL:           kalinko@be-binary.de
# CREATION DATE:  2020/05/21
#
# LICENSE:        CC0-1.0
#
# SOURCE:         https://github.com/kalink0/messi
#
# TITLE:         
#
# DESCRIPTION:   
#
# KNOWN RESTRICTIONS:
#               
#
# USAGE EXAMPLE:
#            
#
# -------------------------------------------------------------------------------

import argparse
import os

def create_abs_path(path):
    """
    Method to create absolute pathes if necessary
    :param path: given path, either absolute or relative
    :return:
    """
    work_dir = os.getcwd()
    if os.path.isabs(path):
        return path
    else:
        return os.path.join(work_dir, path)

def main():
    ap = argparse.ArgumentParser(description='Messi: Messenger Parser and Visualizer')
    ap.add_argument('-t', choices=['fs','tar','zip'], required=True, help="Input type (fs = extracted to file system folder)")
    ap.add_argument('-o', '--output_path', required=True, help='Output folder path')
    ap.add_argument('-i', '--input_path', required=True, help='Path to input file/folder')
        
    args = ap.parse_args()

    input_path = create_abs_path(args.input_path)
    output_path = create_abs_path(args.output_path)
    extracttype = args.t
    pass

if __name__ == "__main__":
    main()