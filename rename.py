#! /bin/python
import os

os.system ('mkdir named')
a = 1
while True:
	if a <= 9:
		i = '000' + str(a)
    elif a <= 99:
        i = '00' + str(a)
	elif a <= 999:
        i = '0' + str(a)
    else:
		i = str(a)
        file_name = 'ligand_structures_3d_unique_NANPDB'+i+'.pdbqt'
        lent = 0
        point = 0
        name = []
	try:
        	open_gate = open(file_name , 'r')
	except:
		print ('RENAMED %d FILES\nDONE !!!'%(a - 1))
		break
	else:
 		for line in open_gate:
            t = line.split()
                name.append(t[3])
                for word in t:
                        while lent > 3:
                                point = point + 1
                                name.append(t[3+point])
                                break
                        lent = lent + 1
                new_name = '_'.join(name)
		command = 'cp '+file_name+' ./renamed/'+new_name+'.pdbqt'
		open_gate.close()
		os.system (command)
                break
	a = a + 1
