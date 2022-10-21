#d0 = bond length; geometry.in 
#E_b = (E_tot^M2 - 2*E_tot^free-atom)/2.0 
#epsilon_HOMO
#epsilon_LUMO
#m_tot = number of unpaired electrons

import math
import os.path

if os.path.isfile("geometry.in"):
    geometry = open("geometry.in", "r")
    xyz = geometry.read().split()
    atom1 = [float(xyz[1]), float(xyz[2]), float(xyz[3])]
    atom2 = [float(xyz[6]), float(xyz[7]), float(xyz[8])]
    print("The distance between the two atoms is: " + str(math.dist(atom1,atom2)))
    geometry.close()
else:
    print("No geometry file found, proceeding to other calculations")

if os.path.isfile("homo_final.info") and os.path.isfile("lumo_final.info") and os.path.isfile("mag_moments_final.info"):
    homo_final = open("homo_final.info", "r")
    lumo_final = open("lumo_final.info", "r")
    mag_moments = open("mag_moments_final.info", "r")
    print("Epsilon HOMO: "+homo_final.read().split()[0]+"\nEpsilon Lumo: "+lumo_final.read().split()[0]+"\nUnpaired electrons: "+mag_moments.read().split()[0])
    homo_final.close()
    lumo_final.close()
    mag_moments.close()
else:
    print("No .info files found")
