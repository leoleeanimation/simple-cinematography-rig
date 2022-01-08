from maya import cmds
class CinematographyRig(object):
    def __init__(self):
        self.title = "My Dumb RIG"
        self.width = 250
        self.height = 210
        self.createUI()
    def createUI(self):
        if cmds.window(self.title, exists=True):
            cmds.deleteUI(self.title, window=True)
        self.main_window = cmds.window(self.title,
                                     title=self.title,
                                     sizeable=False)
                                     
        self.column_layout = cmds.columnLayout("main_layout", adjustableColumn=True)
        
        self.logo_column = cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[(1,55),(2,180)])
        self.logoPath = cmds.internalVar(userPrefDir=True)+"icons/camera_icon.png"
        self.logoimage = cmds.image(image=self.logoPath)
        self.txt_1 = cmds.text("txt_1", label="SIMPLE CINEMATOGRAPHY RIG")
        
        cmds.setParent('..')
        
        self.direction_layout = cmds.columnLayout("direction_layout", adjustableColumn=True)
        self.direction = cmds.textField(text= "               *Select Camera or Light first*", backgroundColor=[0.1, 0.1, 0], editable = False)
        
        cmds.setParent('..')
        
        self.separator = cmds.separator(height=10, style="in")
        
        self.key_layout = cmds.gridLayout(
            "key_layout", numberOfColumns=2, cellWidthHeight = [125, 125])
        self.btn_2 = cmds.button("btn_2", label="A_Stand", command=self.Astand_rig, backgroundColor=[0.1, 0.1, 0.5])
        self.btn_1 = cmds.button("btn_1", label="Crane", command=self.crane_rig, backgroundColor=[0.5, 0.1, 0.1])
                
        cmds.showWindow(self.main_window)
        cmds.window(self.main_window, edit=True, widthHeight=(self.width,
                                                            self.height))
    def Astand_rig(self, selection):
        selected = cmds.ls(selection=True)
        # Rotation Group
        cmds.group(selected, name="rotation#")
        
        rotate_selected = cmds.pickWalk(selected, direction="up")
        
        for i in rotate_selected:
            cmds.setAttr(i+".tx", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".ty", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".tz", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".sx", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".sy", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".sz", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".v", lock=True, keyable=False, channelBox=False)
        
        # Rotation Rig
        cmds.polyCube()
        cmds.polySmooth(dv = 2 )    
        cmds.select('pCube1.e[64]','pCube1.e[48:49]','pCube1.e[52:53]','pCube1.e[56:57]','pCube1.e[60:61]','pCube1.e[64:65]', 'pCube1.e[68:69]','pCube1.e[72:73]', 'pCube1.e[76:77]')
        cmds.polyToCurve()
        cmds.select('pCube1.e[67]','pCube1.e[50:51]', 'pCube1.e[54:55]', 'pCube1.e[66:67]', 'pCube1.e[70:71]', 'pCube1.e[82:83]', 'pCube1.e[86:87]', 'pCube1.e[90:91]', 'pCube1.e[94:95]' )
        cmds.polyToCurve()
        cmds.select('pCube1.e[58:59]', 'pCube1.e[62:63]', 'pCube1.e[74:75]', 'pCube1.e[78:81]', 'pCube1.e[84:85]', 'pCube1.e[88:89]', 'pCube1.e[92:93]')
        cmds.polyToCurve()
        cmds.select(clear=True)
        cmds.Group()
        cmds.select("polyToCurveShape1","polyToCurveShape2","polyToCurveShape3", "null1")
        cmds.parent(s=True, r= True)
        cmds.DeleteHistory()
        cmds.rename('null1', 'rotation_rig#')
        cmds.rename("polyToCurveShape1",'Sphere_ctrlShape1')
        cmds.rename("polyToCurveShape2",'Sphere_ctrlShape2')
        cmds.rename("polyToCurveShape3",'Sphere_ctrlShape3')
        cmds.delete('polyToCurve1','polyToCurve2','polyToCurve3', 'pCube1')
        rotateRig_shapes = cmds.ls(selection=True)
        rotateRig_selected = cmds.pickWalk(rotateRig_shapes, direction ="up")
        
        for i in rotateRig_selected:
            cmds.setAttr(i+".sx", 3)
            cmds.setAttr(i+".sy", 3)
            cmds.setAttr(i+".sz", 3)
            
        cmds.makeIdentity(rotateRig_selected, apply=True, scale=True)
        
        for i in rotateRig_selected:
            cmds.setAttr(i+".tx", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".ty", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".tz", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".sx", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".sy", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".sz", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".v", lock=True, keyable=False, channelBox=False)
        
        cmds.parentConstraint(rotateRig_selected, rotate_selected, st=["x","y","z"])
        # Transltation Group
        cmds.group(rotate_selected, name="translation#")
        translate_selected = cmds.pickWalk(rotate_selected, direction="up")
        for i in translate_selected:
            cmds.setAttr(i+".rx", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".ry", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".rz", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".sx", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".sy", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".sz", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".v", lock=True, keyable=False, channelBox=False)
        
        # Translation Rig
        cmds.curve (d=1, p=[(0.25, 0, -0.25), (0.25, 0, -2), (0.5, 0, -2), (0, 0,-2.5), (-0.5, 0, -2), (-0.25, 0, -2), (-0.25, 0, -0.25), (-2, 0, -0.25), (-2, 0, -0.5), (-2.5, 0, 0), (-2, 0, 0.5), (-2, 0, 0.25), (-0.25, 0, 0.25), (-0.25, 0, 2), (-0.5, 0, 2), (-0, 0, 2.5), (0.5, 0, 2), (0.25, 0, 2), (0.25, 0, 0.25), (2, 0, 0.25), (2, 0, 0.5), (2.5, 0, 0), (2, 0, -0.5), (2, 0, -0.25), (0.25, 0, -0.25)], k =(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24))
        cmds.rename ("curve1", "translation_rig#")
        transRig_selected = cmds.ls(selection=True)
        
        for i in transRig_selected:
            cmds.setAttr(i+".rx", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".ry", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".rz", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".sx", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".sy", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".sz", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".v", lock=True, keyable=False, channelBox=False)
        
        cmds.parentConstraint(transRig_selected, translate_selected, sr=["x","y","z"])
        
        
        # Master Group
        cmds.group(translate_selected, name="Astand_master#")
        
        master_selected = cmds.pickWalk(translate_selected, direction="up")
        
        for i in master_selected:
            cmds.setAttr(i+".rx", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".rz", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".sx", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".sy", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".sz", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".v", lock=True, keyable=False, channelBox=False)
        # Master Rig
        cmds.polyPlane(subdivisionsHeight = 3, subdivisionsWidth = 3)
        cmds.select("pPlane1.f[0]", "pPlane1.f[2]", "pPlane1.f[6]", "pPlane1.f[8]")
        cmds.delete()
        cmds.select("pPlane1.e[0:4]", "pPlane1.e[7]", "pPlane1.e[9:10]", "pPlane1.e[12:15]")
        cmds.polyToCurve (degree = 1)
        cmds.DeleteHistory()
        cmds.delete("pPlane1")
        cmds.rename("polyToCurve1", "master_rig#")
        
        masterRig_selected = cmds.ls(selection=True)
        for i in masterRig_selected:
            cmds.setAttr(i+".sx", 6)
            cmds.setAttr(i+".sy", 6)
            cmds.setAttr(i+".sz", 6)
        cmds.makeIdentity(masterRig_selected, apply=True, scale=True)
        for i in masterRig_selected:
            cmds.setAttr(i+".rx", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".rz", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".sx", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".sy", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".sz", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".v", lock=True, keyable=False, channelBox=False)
        
        cmds.parentConstraint(masterRig_selected, master_selected, sr=["x","z"])
        
        cmds.reorder(transRig_selected, relative=3)
        cmds.reorder(rotateRig_selected, relative=4)
        
        cmds.parent(transRig_selected, masterRig_selected)
        cmds.parent(rotateRig_selected, transRig_selected)
        
    def crane_rig(self, selection):
        selected = cmds.ls(selection=True)
        # Rotation Group
        cmds.group(selected, name="rotation#")
        
        rotate_selected = cmds.pickWalk(selected, direction="up")
        
        for i in rotate_selected:
            cmds.setAttr(i+".tx", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".ty", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".tz", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".sx", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".sy", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".sz", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".v", lock=True, keyable=False, channelBox=False)
        
        # Rotation Rig
        cmds.polyCube()
        cmds.polySmooth(dv = 2 )    
        cmds.select('pCube1.e[64]','pCube1.e[48:49]','pCube1.e[52:53]','pCube1.e[56:57]','pCube1.e[60:61]','pCube1.e[64:65]', 'pCube1.e[68:69]','pCube1.e[72:73]', 'pCube1.e[76:77]')
        cmds.polyToCurve()
        cmds.select('pCube1.e[67]','pCube1.e[50:51]', 'pCube1.e[54:55]', 'pCube1.e[66:67]', 'pCube1.e[70:71]', 'pCube1.e[82:83]', 'pCube1.e[86:87]', 'pCube1.e[90:91]', 'pCube1.e[94:95]' )
        cmds.polyToCurve()
        cmds.select('pCube1.e[58:59]', 'pCube1.e[62:63]', 'pCube1.e[74:75]', 'pCube1.e[78:81]', 'pCube1.e[84:85]', 'pCube1.e[88:89]', 'pCube1.e[92:93]')
        cmds.polyToCurve()
        cmds.select(clear=True)
        cmds.Group()
        cmds.select("polyToCurveShape1","polyToCurveShape2","polyToCurveShape3", "null1")
        cmds.parent(s=True, r= True)
        cmds.DeleteHistory()
        cmds.rename('null1', 'rotation_rig#')
        cmds.rename("polyToCurveShape1",'Sphere_ctrlShape1')
        cmds.rename("polyToCurveShape2",'Sphere_ctrlShape2')
        cmds.rename("polyToCurveShape3",'Sphere_ctrlShape3')
        cmds.delete('polyToCurve1','polyToCurve2','polyToCurve3', 'pCube1')
        rotateRig_shapes = cmds.ls(selection=True)
        rotateRig_selected = cmds.pickWalk(rotateRig_shapes, direction ="up")
        
        for i in rotateRig_selected:
            cmds.setAttr(i+".sx", 3)
            cmds.setAttr(i+".sy", 3)
            cmds.setAttr(i+".sz", 3)
            
        cmds.makeIdentity(rotateRig_selected, apply=True, scale=True)
        
        for i in rotateRig_selected:
            cmds.setAttr(i+".tx", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".ty", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".tz", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".sx", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".sy", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".sz", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".v", lock=True, keyable=False, channelBox=False)
        
        cmds.parentConstraint(rotateRig_selected, rotate_selected, st=["x","y","z"])
        # Transltation Group
        cmds.group(rotate_selected, name="translation#")
        translate_selected = cmds.pickWalk(rotate_selected, direction="up")
        for i in translate_selected:
            cmds.setAttr(i+".rx", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".ry", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".rz", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".sx", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".sy", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".sz", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".v", lock=True, keyable=False, channelBox=False)
        
        # Translation Rig
        cmds.curve (d=1, p=[(0.25, 0, -0.25), (0.25, 0, -2), (0.5, 0, -2), (0, 0,-2.5), (-0.5, 0, -2), (-0.25, 0, -2), (-0.25, 0, -0.25), (-2, 0, -0.25), (-2, 0, -0.5), (-2.5, 0, 0), (-2, 0, 0.5), (-2, 0, 0.25), (-0.25, 0, 0.25), (-0.25, 0, 2), (-0.5, 0, 2), (-0, 0, 2.5), (0.5, 0, 2), (0.25, 0, 2), (0.25, 0, 0.25), (2, 0, 0.25), (2, 0, 0.5), (2.5, 0, 0), (2, 0, -0.5), (2, 0, -0.25), (0.25, 0, -0.25)], k =(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24))
        cmds.rename ("curve1", "translation_rig#")
        transRig_selected = cmds.ls(selection=True)
        
        for i in transRig_selected:
            cmds.setAttr(i+".rx", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".ry", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".rz", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".sx", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".sy", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".sz", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".v", lock=True, keyable=False, channelBox=False)
        
        cmds.parentConstraint(transRig_selected, translate_selected, sr=["x","y","z"])
        
        # Crane Group
        cmds.group(translate_selected, name="Crane#")
        
        crane_selected = cmds.pickWalk(translate_selected, direction="up")
        
        for i in crane_selected:
            cmds.setAttr(i+".tx", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".ty", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".tz", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".rz", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".sx", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".sy", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".sz", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".v", lock=True, keyable=False, channelBox=False)
        
        # Crane Rig
        cmds.polyCylinder(subdivisionsAxis=16)
        cmds.select("pCylinder1.f[0:2]","pCylinder1.f[11:17]")
        cmds.delete()
        cmds.select('pCylinder1.e[16:24]')
        cmds.polySplitRing( sma=180, wt=0.55)
        cmds.select('pCylinder1.e[16:24]')
        cmds.polySplitRing( sma=180, wt=0.85)
        cmds.select("pCylinder1.f[0:7]","pCylinder1.f[16:23]" )
        cmds.delete()
        cmds.select("pCylinder1.e[0:7]","pCylinder1.e[8]","pCylinder1.e[10]","pCylinder1.e[12]","pCylinder1.e[14]","pCylinder1.e[16]","pCylinder1.e[18]","pCylinder1.e[20]","pCylinder1.e[22]","pCylinder1.e[24]","pCylinder1.e[23]")
        cmds.polyToCurve(dg=1)
        cmds.delete("pCylinder1")
        cmds.rename("polyToCurve1", "crane_rig#")
        craneRig_selected = cmds.ls(selection=True)
        for i in craneRig_selected:
            cmds.setAttr(i+".rz", -90)
            cmds.setAttr(i+".sx", 3)
            cmds.setAttr(i+".sy", 3)
            cmds.setAttr(i+".sz", 3)
        cmds.makeIdentity(craneRig_selected, apply=True, rotate=True, scale=True)
        for i in craneRig_selected:
            cmds.setAttr(i+".tx", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".ty", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".tz", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".rz", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".sx", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".sy", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".sz", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".v", lock=True, keyable=False, channelBox=False)
                    
        
        cmds.parentConstraint(craneRig_selected, crane_selected, st=["x","y","z"], sr=["z"])
        
        # Master Group
        cmds.group(crane_selected, name="Crane_master#")
        
        master_selected = cmds.pickWalk(crane_selected, direction="up")
        
        for i in master_selected:
            cmds.setAttr(i+".rx", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".rz", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".sx", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".sy", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".sz", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".v", lock=True, keyable=False, channelBox=False)
        # Master Rig
        cmds.polyPlane(subdivisionsHeight = 3, subdivisionsWidth = 3)
        cmds.select("pPlane1.f[0]", "pPlane1.f[2]", "pPlane1.f[6]", "pPlane1.f[8]")
        cmds.delete()
        cmds.select("pPlane1.e[0:4]", "pPlane1.e[7]", "pPlane1.e[9:10]", "pPlane1.e[12:15]")
        cmds.polyToCurve (degree = 1)
        cmds.DeleteHistory()
        cmds.delete("pPlane1")
        cmds.rename("polyToCurve1", "master_rig#")
        
        masterRig_selected = cmds.ls(selection=True)
        for i in masterRig_selected:
            cmds.setAttr(i+".sx", 6)
            cmds.setAttr(i+".sy", 6)
            cmds.setAttr(i+".sz", 6)
        cmds.makeIdentity(masterRig_selected, apply=True, scale=True)
        for i in masterRig_selected:
            cmds.setAttr(i+".rx", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".rz", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".sx", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".sy", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".sz", lock=True, keyable=False, channelBox=False)
            cmds.setAttr(i+".v", lock=True, keyable=False, channelBox=False)
        
        cmds.parentConstraint(masterRig_selected, master_selected, sr=["x","z"])
        
        cmds.reorder(craneRig_selected, relative=2)
        cmds.reorder(transRig_selected, relative=3)
        cmds.reorder(rotateRig_selected, relative=4)
        
        cmds.parent(craneRig_selected, masterRig_selected)
        cmds.parent(transRig_selected, craneRig_selected)
        cmds.parent(rotateRig_selected, transRig_selected)
        
if __name__ == "__main__":
    ui = CinematographyRig()
    ui.createUI()
