# quick_dxf_converter
A small script utilizing ezdxf to convert ascii coordinate files with coding into dxf polylines.
Required format: Line number; x; y; z; code

## ascii converter
Initially **11201**: begin polyline, **91201** or **81201**: end polyline. Everything else will be interpreted as points.

More features to be added later on.

## gt file converter
Newer version intended for .gt format files. Use through cli. 


## dependencies
Requires [ezdxf and r12writer](https://github.com/mozman/ezdxf) to work. Installable through pip etc.
