# me - this DAT
# 
# frame - the current frame
# state - True if the timeline is paused
# 


# Every frame, updates table_dat with data most recently stored in inQ
# Unsure why this file is separate from tdServer, maybe because they run differently?
# might combine

table_dat = 'serverTable'

import numpy as np

def onStart():
	return

def onCreate():
	return

def onExit():
	return

def onFrameStart(frame):
	try:
		inQ = me.parent().fetch('inQ')
		curVals = inQ.get_nowait()
		for i in range(curVals.shape[0]):
			# op('synthtable').replaceRow(0, curVals[:,0])
			for j in range(curVals.shape[1]):
				n[i+1, j+1] = curVals[i][j]
	except:
		# print("error")
		return
	# return
	

def onFrameEnd(frame):
	return

def onPlayStateChange(state):
	return

def onDeviceChange():
	return

def onProjectPreSave():
	return

def onProjectPostSave():
	return

n = op('synthtable')
	