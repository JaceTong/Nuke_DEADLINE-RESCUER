# --------------------------------------------------------------
# JINGXUAN'S CUSTOM NUKE SETTINGS  AKA- DEADLINE RESCUER
# Version: 1.2.2
# Last Updated: June.22th, 2024
# --------------------------------------------------------------


import nuke
import nukescripts
import os
import Add_Decrese_Value


#CUSTOM HOTKEYS
menubar=nuke.menu("Nodes")
m=menubar.addMenu("LJ_tools", icon="jacemenu.png")

m.addCommand('Mask_Merge', 'nuke.createNode("Merge2", "operation mask bbox A", False)', "Shift+Q", shortcutContext=2)
m.addCommand('Stencil_Merge', 'nuke.createNode("Merge2", "operation stencil bbox B", False)', "shift+w", shortcutContext=2)
m.addCommand('QK_Cryptomatte', 'nuke.createNode("Cryptomatte")', "shift+c", shortcutContext=2)
m.addCommand('Run_AutoCrop', 'nukescripts.autocrop("crop 1")', "shift+Ctrl+e", shortcutContext=2)

#Add/Decrese "Size" Value in selected Node
m.addCommand('Add_Value','Add_Decrese_Value.Add_value()', "e", shortcutContext=2)
m.addCommand('Decrese_value','Add_Decrese_Value.De_value()', "shift+e", shortcutContext=2)



#NUKE DEFAULT NODE SETTINGS
nuke.knobDefault('Roto.toolbox','createBSpline')
nuke.knobDefault("RotoPaint.toolbox",'''clone {{ clone opc .2}}''')
nuke.knobDefault("LayerContactSheet.showLayerNames","1")
nuke.knobDefault("Cryptomatte.unpremultiply","1")
nuke.knobDefault( 'Blur.size', '50' )
nuke.knobDefault("Write.channels","rgba")
nuke.knobDefault("Write.create_directories","1")
nuke.menu('Nodes').addCommand( "Time/FrameHold", "nuke.createNode('FrameHold')['first_frame'].setValue( nuke.frame() )", icon='FrameHold.png')
