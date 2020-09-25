"""
Generated by CHARMM-GUI (http://www.charmm-gui.org)

omm_hmr.py

This module is for Hydrogen Mass Repartitioning.

Correspondance: jul316@lehigh.edu or wonpil@lehigh.edu
Last update: October 31, 2019
"""

from __future__ import print_function
import os
from math import *

from simtk.unit import *
from simtk.openmm import *
from simtk.openmm.app import *

def HydrogenMassRepartition(system, psf):
    for bond in psf.bond_list:
        # Only take the ones with at least one hydrogen
        atom1, atom2 = bond.atom1, bond.atom2
        if atom1.type.atomic_number != 1 and atom2.type.atomic_number != 1: continue
        if 'TIP3' in [atom1.residue.resname, atom2.residue.resname]: continue
        if atom2.type.atomic_number == 1:
            atom1, atom2 = atom2, atom1 # now atom1 is hydrogen for sure
        if atom2.type.atomic_number != 1:
            mass1 = system.getParticleMass(atom1.idx)
            mass2 = system.getParticleMass(atom2.idx)
            new_mass1 = mass1 * 3.0
            new_mass2 = mass2 - new_mass1 + mass1
            system.setParticleMass(atom1.idx, new_mass1)
            system.setParticleMass(atom2.idx, new_mass2)

    return system
