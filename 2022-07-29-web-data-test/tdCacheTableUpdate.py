# me - this DAT
# 
# frame - the current frame
# state - True if the timeline is paused
# 
# Make sure the corresponding toggle is enabled in the Execute DAT.

out_table = 'cacheTable'
data_op = 'curRectValue'


def onStart():
    # when project starts, set cacheTable size
    n = op(out_table)
    n.setSize(1,1280)
    return

def onCreate():
	return

def onExit():
	return

def onFrameStart(frame):
    # get current value of curRectValue and pass down update through cacheTable
    outOp = op(out_table)
    dataOp = op(data_op)
    outOp[0,1279] = dataOp['chan1']
    for i in range(1279):
        outOp[0,1278-i] = outOp[0,1278-i+1]
    return

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

	