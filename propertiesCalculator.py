#d0 = bond length; geometry.in 
#E_b = (E_tot^M2 - 2*E_tot^free-atom)/2.0 
#epsilon_HOMO
#epsilon_LUMO
#m_tot = number of unpaired electrons
# v2.1
import math
import os

if os.path.isfile("geometry.in"): #Check if the geometry file exists
    geometry = open("geometry.in", "r")
    xyz = geometry.readlines()
    atom = {}
    nAtom = 0 # Iterable for identifyind atoms in the dictionary declared above
    for line in xyz:
        if len(line.split()) > 0: # Check if the line is empty
            if line.split()[0] == "atom":
                coord = list(map(float,line.split()[1:4]))
                specie = line.split()[4]
                atom[nAtom] = coord, specie
                nAtom += 1
    if nAtom == 2:
        print("d"+str(0)+": "+ str(math.dist(atom.get(0)[0], atom.get(1)[0]) ) )
    elif nAtom == 3:
        print("d"+str(0)+": "+ str(math.dist(atom.get(0)[0], atom.get(1)[0]) ) )
        print("d"+str(0)+": "+ str(math.dist(atom.get(1)[0], atom.get(2)[0]) ) )
    elif nAtom > 3:
        dist = list()
        for i in range(len(atom.keys())):
            for l in range(len(atom.keys())):
                if i > l:
                    dist.append(math.dist(atom.get(i)[0], atom.get(l)[0]))
        dist.sort()
        #print(dist)
        #print(len(dist))
        threshold = dist[0] * 1.2 # Defines a limited distance to consider a bond between the atoms
        sumD = float()
        sumBond = 0
        for d in dist:
            if d < threshold:
                if sumD == 0: # sumD will be 0 in the first loop
                    sumD = d
                    sumBond += 1
                else:
                    sumD += d
                    sumBond += 1

        print("Dav: "+str(sumD/sumBond))
        print("Average ECN: "+str(sumBond/len(atom.keys())))
    #for i in range(len(atom.keys()) - 1):
    #    print("d"+str(i)+": "+ str(math.dist(atom.get(i)[0], atom.get(i+1)[0]) ) )
else:
    print("No geometry file found, proceeding to other calculations")

if os.path.isfile("homo_final.info") and os.path.isfile("lumo_final.info") and os.path.isfile("mag_moments_final.info") and os.path.isfile("total_energy_final.info"):
    homo_final = open("homo_final.info", "r")
    lumo_final = open("lumo_final.info", "r")
    mag_moments = open("mag_moments_final.info", "r")
    total_energy = open("total_energy_final.info", "r")
    if not mag_moments.read(1):
        mag_momentN = "0"
    else:
        mag_momentN = mag_moments.read().split()[0]
    print("Total Energy: "+total_energy.read().split()[0]+"\nEpsilon HOMO: "+homo_final.read().split()[0]+"\nEpsilon LUMO: "+lumo_final.read().split()[0]+"\nUnpaired electrons: "+mag_momentN)
    homo_final.close()
    lumo_final.close()
    mag_moments.close()
else:
    print("No .info files found")

try: 
    aims = open("aims.out", "r")
    aimsStr = aims.read()
    inicio = aimsStr.rfind("Spin-up eigenvalues")
    if inicio == -1:
        exit()
    fim = aimsStr.rfind("Current spin moment of the entire structure")
    print(aimsStr[inicio:fim])
except:
    print("No aims.out file found!!!")


