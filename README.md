# quick_dxf_converter
A small script utilizing ezdxf to convert ascii coordinate files with coding into dxf polylines.
Required format: Line number; x; y; z; code

Initially **11201**: begin polyline, **91201** or **81201**: end polyline. Everything else will be interpreted as points.

More features to be added later on.

Requires [ezdxf and r12writer](https://ezdxf.readthedocs.io/en/master/index.html) to work.
