#!/usr/bin/env python3

import ezdxf
from ezdxf.addons import r12writer
import sys

def create_list(filename):
    with open(filename) as f:
        data_list = []
        for line in f:
            code = line.split()
            data_list.append(code)
# line  layer   point   x               y               z
# 1     KIVI    10053   6707532.603     23447574.210    14.892

    return data_list

def draw_dxf(filename, data_list):
    with r12writer(f"{filename}_export.dxf") as dxf:
        polyline_3d = []
        last_linenumber = "1"
        for line in data_list:
            print(line)
            if line[0] == "0":
                dxf.add_point((float(line[-3]), float(line[-2]), float(line[-1])))
            elif line[0] != last_linenumber:
                polyline_3d.append((float(line[-3]), float(line[-2]), float(line[-1])))
                dxf.add_polyline(polyline_3d)
                polyline_3d = []
            else:
                polyline_3d.append((float(line[-3]), float(line[-2]), float(line[-1])))
                last_linenumber = line[0]

    

def main():
    for filename in sys.argv[1:]:
        data_list = create_list(filename)
        draw_dxf(filename, data_list)

if __name__ == "__main__":
    main()
