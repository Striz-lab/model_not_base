import gmsh
import sys

gmsh.initialize()
gmsh.model.add("t1")
lc = 1e-2
gmsh.model.geo.addPoint(0, 0, 0, lc, 1)
gmsh.model.geo.addPoint(0, 0, 0.1, lc, 2)
gmsh.model.geo.addPoint(0, 0.1, 0, lc, 3)
gmsh.model.geo.addPoint(0, 0.1, 0.1, lc, 4)
gmsh.model.geo.addPoint(0.1, 0, 0, lc, 5)
gmsh.model.geo.addPoint(0.1, 0, 0.1, lc, 6)
gmsh.model.geo.addPoint(0.1, 0.1, 0, lc, 7)
gmsh.model.geo.addPoint(0.1, 0.1, 0.1, lc, 8)


gmsh.model.geo.addLine(1, 2, 1)
gmsh.model.geo.addLine(2, 4, 2)
gmsh.model.geo.addLine(4, 3, 3)
gmsh.model.geo.addLine(3, 1, 4)

gmsh.model.geo.addLine(5, 6, 5)
gmsh.model.geo.addLine(6, 8, 6)
gmsh.model.geo.addLine(7, 8, 7)
gmsh.model.geo.addLine(7, 5, 8)


gmsh.model.geo.addLine(1, 5, 9)
gmsh.model.geo.addLine(2, 6, 10)
gmsh.model.geo.addLine(3, 7, 11)
gmsh.model.geo.addLine(4, 8, 12)


gmsh.model.geo.addCurveLoop([1,2,3,4], 1)
gmsh.model.geo.addPlaneSurface([1], 1)

gmsh.model.geo.addCurveLoop([5, 6, -7, 8], 2)
gmsh.model.geo.addPlaneSurface([2], 2)

gmsh.model.geo.addCurveLoop([-1, 9, 5, -10], 3)
gmsh.model.geo.addPlaneSurface([3], 3)

gmsh.model.geo.addCurveLoop([2, 12, -6, -10 ], 4)
gmsh.model.geo.addPlaneSurface([4], 4)

gmsh.model.geo.addCurveLoop([11, 7, -12, 3], 5)
gmsh.model.geo.addPlaneSurface([5], 5)

gmsh.model.geo.addCurveLoop([11, 8, -9, -4], 6)
gmsh.model.geo.addPlaneSurface([6], 6)


l = gmsh.model.geo.addSurfaceLoop([i + 1 for i in range(6)])
gmsh.model.geo.addVolume([l])


gmsh.model.geo.synchronize()
gmsh.model.mesh.generate(3)

gmsh.write("t1.msh")

if '-nopopup' not in sys.argv:
    gmsh.fltk.run()

gmsh.finalize()
