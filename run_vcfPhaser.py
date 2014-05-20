#!/usr/bin/env python

"""
run_vcfPhaser.py

Script for

Created by Tim Hughes

"""

import argparse





"""    splitOutFamily bigBatch.vcf myQuad.fam > myQuad.vcf
    phaseFamily myQuad.vcf myQuad.fam > myQuad_phased.vcf

    Both tools would need to make use of the GATK.
    * The splitOutFamily is fairly trivial and just uses the GATKs SelectVariants to pull out the right samples.
     This tool could also do some tests on the FAM file, in particular check that the family structure is correct. I was thinking that some functionality like this could be implemented in your FAM file parser. There is some software out there for FAM files http://pngu.mgh.harvard.edu/~purcell/famtypes/, but I can't see anything for python.
    * the phaseFamily tool would be a bit more complicated bcse the GATK can only phase Trios and Duos. It would need to:
        * split a quad (parents and two children) into two trios again using SelectVariants
      * phase each trio using GATKs PhaseByTransmission
      * rejoin the two phased trio files (using GATKs CombineVariants), to get back the original file phased

    The phaseFamily file obviously gets a bit more complicated if we have more siblings or more than two generations, but fundamentally it is the same.


    GATK to do all the heavy lifting:

        splitting a big family out of a big VCF file: SelectVariants
    splitting the big family into phasable trios duos: SelectVariants
    phasing: PhaseByTransmission
    combining again into one big phased family: CombineVariants
    The code that needs to be written is:

        expand your FAM parsing code to include:
            more QC / analysis of the file (which will also be useful in the context of genmod)
    functionality to identify trios in the pedigree and write them to FAM files
    calls to GATK initiated from python
    This approach ensures that GATK takes care of all the issues of reading and writing well-formed VCF files which is not necessarily trivial.

"""

def main():

    info_string = """Individuals that are not present in ped file will not be considered in the analysis."""

    parser = argparse.ArgumentParser(description="Extract and phase samples from a VCF file using PED file")

    parser.add_argument('--gatk', 
            type=str, nargs=1,
            required=True,
            help='Path to the gatk.jar file'
        )  
    
    parser.add_argument('--ref', 
            type=str, nargs=1,
            required=True,
            help='The reference file in fasta format which should have an associated .dict file in the same directory'
        )

    parser.add_argument('ped_file',
        type=str, nargs=1,
        help='A pedigree file in .ped format containing the samples to be extracted from the VCF file'
    )

    parser.add_argument('vcf_file',
        type=str, nargs=1,
        help='A variant file in VCF format containing the genotypes of the samples to be phased'
    )

#    parser.parse_args(['--foo', '1', 'BAR'])
    args = parser.parse_args('--gatk GATK.jar --ref myRef.fasta myFamFile myVcfFile'.split())
    print(args)

    print(args.ped_file)    

if __name__ == '__main__':
    main()

# -*- coding: utf-8 -*-

