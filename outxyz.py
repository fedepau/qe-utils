#!/usr/bin/python

import re

rgx = re.compile(r'.*number of atoms/cell.* =.* (\d+)$')

def grep_nat(file):
    with open("./pw.out") as file:
        for line in file:
            if (m := rgx.match(line)) is not None:
                nat = int(''.join(map(str,m.groups(1))))
                return(nat)
                exit

always_print = False

with open ("./pw.out", "r") as pw_out:
    pw_lines = pw_out.readlines()
    for line in pw_lines:
        if line in ['\n', '\r\n']:
                always_print = False
        if 'End final coordinates' in line:
                always_print = False
        if "ATOMIC_POSITIONS" in line:
            always_print = True
            with open ("structure.xyz", "a") as xyz_tot:
                xyz_tot.write(str(grep_nat("./pw.out")))
                xyz_tot.write("\n\n")
                continue
        if always_print:
            with open ("structure.xyz", "a") as xyz_tot:
                xyz_tot.write(line)
