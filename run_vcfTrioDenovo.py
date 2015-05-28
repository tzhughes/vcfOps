# -*- coding: utf-8 -*-
"""
Created on Tue May 20 15:17:37 2014

@author: timothyh
"""

import argparse
from tempfile import NamedTemporaryFile
from ped_parser import family, individual, parser


def main():
    argparser = argparse.ArgumentParser(description="Call denovo variants on a VCF file containing a trio")

    argparser.add_argument('--denovogear', 
            type=str, nargs=1,
            required=True,
            help='Path to the denovogear binary for example: /Users/timothyh/home/binHTS/denovogear 0.5.4/bin/denovogear'
        )
        
    argparser.add_argument('vcf_file',
        type=str, nargs=1,
        help='A variant file in VCF format containing the genotypes of the trio'
    )
    
    argparser.add_argument('ped_file',
        type=str, nargs=1,
        help='A pedigree file in .ped format containing the samples to be extracted from the VCF file'
    )
    
    
    print("Hello")
    # Check that the PED file only contains a trio and identify sex of child as this is required for calling denovogear correctly

    # Check that the VCF file contains the same samples as thePED file

    # Run denovogear

    #fam_id = '1'
    #someFamily = family.Family(family_id = fam_id)
    #print(someFamily)
    trio_lines = ['#Standard trio\n', 
                    '#FamilyID\tSampleID\tFather\tMother\tSex\tPhenotype\n', 
                    'healthyParentsAffectedSon\tproband\tfather\tmother\t1\t2\n',
                    'healthyParentsAffectedSon\tmother\t0\t0\t2\t1\n', 
                    'healthyParentsAffectedSon\tfather\t0\t0\t1\t1\n',
                    'healthyParentsAffectedSon\tdaughter\tfather\tmother\t2\t1\n',
                    ]
    trio_file = NamedTemporaryFile(mode='w+t', delete=False, suffix='.vcf')
    trio_file.writelines(trio_lines)
    trio_file.seek(0)
    trio_file.close()

    family_parser = parser.FamilyParser(trio_file.name)
    trio_family = family_parser.families['healthyParentsAffectedSon']
    print(trio_family.)

    
    
if __name__ == '__main__':
    main()