import Rhino
from Rhino.Render import TextureMapping
from Rhino.Geometry import Interval
import scriptcontext as sc
import rhinoscriptsyntax as rs

if Run:
    sc.doc = Rhino.RhinoDoc.ActiveDoc

    rhino_obj = rs.coercerhinoobject(guid)

    dom = Interval(-250, 250)
    tm = TextureMapping.CreatePlaneMapping(plane, dom, dom, dom, True)
    rhino_obj.SetTextureMapping(1, tm)

    sc.doc = ghdoc
