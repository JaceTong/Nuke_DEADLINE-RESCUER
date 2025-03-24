
import nuke
import nukescripts
import os
import math

def Add_value():
        try:
            inputNode = nuke.selectedNode()
            preValue = inputNode.knob('size').getValue()
            if preValue == 0.0:
                inputNode.knob('size').setValue(preValue + 1)
            else :
                digits = int(math.log10(abs(preValue)))+1    
                inputNode.knob('size').setValue(preValue + pow(10,digits-1))
        except:
            pass


def De_value():
        try:
            inputNode = nuke.selectedNode()
            preValue = inputNode.knob('size').getValue()
            if preValue == 0.0:
                inputNode.knob('size').setValue(preValue - 1)
            else :
                digits = int(math.log10(abs(preValue)))+1    
                inputNode.knob('size').setValue(preValue - pow(10,digits-1))
        except:
            pass

