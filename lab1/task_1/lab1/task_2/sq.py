import gmsh
import math
import os
import sys

gmsh.initialize()

path = os.path.dirname(os.path.abspath(__file__))
gmsh.merge(os.path.join(path, 'Car.stl'))

gmsh.model.mesh.classifySurfaces(40 * math.pi / 180., True,
                                 False,
                                 180 * math.pi / 180.)

s = gmsh.model.getEntities(2)
l = gmsh.model.geo.addSurfaceLoop([s[i][1] for i in range(len(s))])
gmsh.model.geo.addVolume([l])

gmsh.model.geo.synchronize()

gmsh.model.mesh.generate(3)
gmsh.write('Car.msh')

if '-nopopup' not in sys.argv:
    gmsh.fltk.run()

gmsh.finalize()

