#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
(c) 2014 Brant Faircloth || http://faircloth-lab.org/
All rights reserved.

This code is distributed under a 3-clause BSD license. Please see
LICENSE.txt for more information.

Created on 31 January 2014 11:38 PST (-0800)
"""


import argparse
from illumiprocessor import core
from illumiprocessor.pth import get_user_path

# import pdb


def get_trimgalore_path():
    return get_user_path("executables", "trimgalore")

def get_cutadapt_path():
    return get_user_path("executables", "cutadapt")

def get_args():
    parser = argparse.ArgumentParser(
        description="Batch trim Illumina reads for adapter contamination and "
                    "low quality bases using trim_galore",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--input",
        required=True,
        help="The input directory of raw reads to trim.",
        action=core.FullPaths,
    )
    parser.add_argument(
        "--output",
        required=True,
        help="The output directory of clean reads to create.",
        action=core.CreateDir,
    )
    parser.add_argument(
        "--config",
        required=True,
        help="A configuration file containing the tag:sample mapping and "
        "renaming options.",
    )
    parser.add_argument(
        '--trimgalore',
        default=get_trimgalore_path(),
        action=core.FullPaths,
        help="The path to the trim_galore executable.",
    )
    parser.add_argument(
        "--min-len", type=int, default=40, help="The minimum length of reads to keep."
    )
    parser.add_argument(
        "--no-merge",
        action="store_true",
        default=False,
        help="When trimming PE reads, do not merge singleton files.",
    )
    parser.add_argument(
        "--cores", type=int, default=1, help="Number of compute cores to use."
    )
    parser.add_argument(
        "--r1-pattern",
        type=str,
        default=None,
        help="An optional regex pattern to find R1 reads.",
    )
    parser.add_argument(
        "--r2-pattern",
        type=str,
        default=None,
        help="An optional regex pattern to find R2 reads.",
    )
    parser.add_argument(
        "--se",
        action="store_true",
        default=False,
        help="""Single-end reads.""",
    )
    parser.add_argument(
        "--phred",
        type=str,
        choices=("phred33", "phred64"),
        default="phred33",
        help="""The type of fastq encoding used.""",
    )
    parser.add_argument(
        "--log-path",
        action=core.FullPaths,
        type=core.is_dir,
        default=None,
        help="""The path to a directory to hold logs.""",
    )
    parser.add_argument(
        "--verbosity",
        type=str,
        choices=["INFO", "WARN", "CRITICAL"],
        default="INFO",
        help="""The logging level to use.""",
    )
    parser.add_argument(
        "--paired",
        action="store_true",
        default=True,
        help="""For paired reads.""",
    )
    parser.add_argument(
        '--tg-length',
        type=int,
        default=20,
        help="""Provide Trimgalore with the minimum length of a trimmed sequence (this is the --length <INT> option in trimgalore)""",
    )
    parser.add_argument(
        '--tg-quality',
        type=int,
        default=20,
        help="""Provide Trimgalore with the Phred score used in trimming (this is the --quality <INT> option in trimgalore)""",
    )
    parser.add_argument(
        "--retain_unpaired",
        action="store_true",
        default=True,
        help="""Whether to retain unpaired.""",
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        choices=["clean-fastq"],
        default="clean-fastq",
        help="""Where to put trimmed files.""",
                        )
    parser.add_argument(
        '--path_to_cutadapt',
        type=str,
        default='cutadapt',
        help="""the path to cutadapt.""",
    )
    return parser.parse_args()


def main():
    from illumiprocessor.main import main

    args = get_args()
    main(args)
