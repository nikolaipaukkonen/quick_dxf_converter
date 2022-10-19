#!/usr/bin/env python3

import ezdxf
from ezdxf.addons import r12writer
import sys

def create_list(filename):
    with open(filename) as f:
        data_list = []
        indices = [8,16,24,32,46,60]
        for line in f:
            code = [line[i:j] for i,j in zip(indices, indices[1:]+[None])]
            code_stripped = []
            for s in code:
                code_stripped.append(s.strip())
            data_list.append(code_stripped)
# line  layer   point   x               y               z
# 1     KIVI    10053   6707532.603     23447574.210    14.892

    return data_list

def draw_dxf(filename, data_list):
    with r12writer(f"{filename}_export.dxf") as dxf:
        polyline_3d = []
        last_linenumber = data_list[0][0]
        last_layer = data_list[0][1]

        for line in data_list:
            print(line)
            line_number = line[0]
            current_layer = line[1]
            coord = (float(line[-2]), float(line[-3]), float(line[-1]))
            
            if line_number == "0":
                dxf.add_point(coord, layer=current_layer)
                if polyline_3d:
                    print("Lisätty polyline", polyline_3d)
                    dxf.add_polyline(polyline_3d, layer=last_layer)
                    polyline_3d = []
                
                last_layer = current_layer
                last_linenumber = line_number
            else: 
                if line_number != last_linenumber or current_layer != last_layer:
                    if polyline_3d:
                        print("Lisätty polyline", polyline_3d)
                        dxf.add_polyline(polyline_3d, layer=last_layer)
                        polyline_3d = []
                    polyline_3d.append(coord)
                    last_layer = current_layer
                    last_linenumber = line_number
                else:
                    polyline_3d.append(coord)
                    last_layer = current_layer
                    last_linenumber = line_number

        if polyline_3d:
            dxf.add_polyline(polyline_3d, layer=last_layer)
                

    

def main():
    for filename in sys.argv[1:]:
        data_list = create_list(filename)
        draw_dxf(filename, data_list)

if __name__ == "__main__":
    main()
