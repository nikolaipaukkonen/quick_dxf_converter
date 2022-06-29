#!/usr/bin/env python3

import ezdxf
from ezdxf.addons import r12writer
import sys

print("This script converts ascii files exported by older Leica total stations and other devices into dxf format")
print("Use: python3 proto_converter.py filename_to_be_converted.txt filename_to_be_exported.dxf")

#open file and split 
f = sys.argv[1]
with open(f) as fp:
    line = fp.readline()
    data_list = [] #a list of lists where 0=ptid, 1=x, 2=y, 3=z and 4=code
    cnt = 0
    while line:
        n_x_y_z_code = line.split()
        data_list.append(n_x_y_z_code)
        line = fp.readline()

#draw dxf
with r12writer(sys.argv[2]) as dxf:
    polyline_3d = []
    for line in data_list:
        print(line)
        if len(line) == 5:
            if (line[4] == "91201") or (line[4] == "81201"): #codes can be altered and added
                polyline_3d.append((float(line[1]), float(line[2]), float(line[3])))
            #print(polyline_3d)
                dxf.add_polyline(polyline_3d)
                polyline_3d = []
            elif line[4] == "11201":
                polyline_3d.append((float(line[1]), float(line[2]), float(line[3])))
            else:
                dxf.add_point((float(line[1]), float(line[2]), float(line[3])), layer=line[0])
        else:
            dxf.add_point((float(line[1]), float(line[2]), float(line[3])), layer=line[0])

    #dxf.add_text(sys.argv[2], align="MIDDLE_CENTER") #prints filename, just testing
