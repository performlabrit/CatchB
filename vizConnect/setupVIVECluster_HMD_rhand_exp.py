"""
This module was generated by Vizconnect.
Version: 1.04
Generated on: 2015-11-13 04:20:15.814000
"""

import viz
import vizconnect

#################################
# Parent configuration, if any
#################################

def getParentConfiguration():
	#VC: set the parent configuration
	_parent = ''
	
	#VC: return the parent configuration
	return _parent


#################################
# Pre viz.go() Code
#################################

def preVizGo():
	return True


#################################
# Pre-initialization Code
#################################

def preInit():
	"""Add any code here which should be called after viz.go but before any initializations happen.
	Returned values can be obtained by calling getPreInitResult for this file's vizconnect.Configuration instance."""
	return None


#################################
# Group Code
#################################

def initGroups(initFlag=vizconnect.INIT_INDEPENDENT, initList=None):
	#VC: place any general initialization code here
	rawGroup = vizconnect.getRawGroupDict()
	
	#VC: return values can be modified here
	return None


#################################
# Display Code
#################################

def initDisplays(initFlag=vizconnect.INIT_INDEPENDENT, initList=None):
	#VC: place any general initialization code here
	rawDisplay = vizconnect.getRawDisplayDict()

	_name = 'exp_display'
	if vizconnect.isPendingInit('display', _name, initFlag, initList):
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: set the window for the display
			_window = viz.addWindow()
			_window.setView(viz.addView())
			
			#VC: set placement with alignment: free
			_window.setPosition(0, 1, mode=viz.WINDOW_NORMALIZED)
			_window.setSize(1, 1, mode=viz.WINDOW_NORMALIZED)
			
			#VC: make the window visible only for certain clients
			_clusterMask = viz.CLIENT1
			with viz.cluster.MaskedContext(viz.ALLCLIENTS&~_clusterMask):# hide
				_window.visible(False)
			with viz.cluster.MaskedContext(_clusterMask):# show
				_window.visible(True)
			
			#VC: set the fullscreen monitor
			with viz.cluster.MaskedContext(viz.CLIENT1):# only for clients with this display
				viz.window.setFullscreenMonitor(3)
				viz.window.setFullscreen(True)
			
			#VC: set some parameters
			VFOV = 60
			aspect = viz.AUTO_COMPUTE
			stereo = viz.OFF
			
			#VC: create the raw object
			_window.fov(VFOV,aspect)
			_window.stereo(stereo)
			rawDisplay[_name] = _window
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addDisplay(rawDisplay[_name], _name, make='Generic', model='Custom Window')
	
		#VC: set the parent of the node
		if initFlag&vizconnect.INIT_PARENTS:
			vizconnect.getDisplay(_name).setParent(vizconnect.getTracker('head_tracker'))

	#VC: initialize a new display
	_name = 'rift_display'
	if vizconnect.isPendingInit('display', _name, initFlag, initList):
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: set the window for the display
			_window = viz.MainWindow
			
			#VC: set some parameters
			index = 0
			
			#VC: create the raw object
			import steamvr
			# Get sensor from extension if not specified
			hmd = None
			sensor = None
			hmdList = steamvr.getExtension().getHMDList()
			if hmdList:
				try:
					sensor = hmdList[index]
				except IndexError:
					viz.logError("** ERROR: Not enough HMD's")
			else:
				viz.logError('** ERROR: Failed to detect SteamVR HMD')
			if sensor:
				hmd = steamvr.HMD(sensor=sensor, window=_window)
			_window.displayNode = hmd
			rawDisplay[_name] = _window
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addDisplay(rawDisplay[_name], _name, make='Valve', model='SteamVR HMD')
	
		#VC: set the parent of the node
		if initFlag&vizconnect.INIT_PARENTS:
			vizconnect.getDisplay(_name).setParent(vizconnect.getTracker('head_tracker'))

	#VC: initialize a new display
	_name = 'exp_display'
	if vizconnect.isPendingInit('display', _name, initFlag, initList):
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: set the window for the display
			_window = viz.addWindow()
			_window.setView(viz.addView())
			
			#VC: set placement with alignment: free
			_window.setPosition(0, 1, mode=viz.WINDOW_NORMALIZED)
			_window.setSize(0.2, 0.2, mode=viz.WINDOW_NORMALIZED)
			
			#VC: set some parameters
			VFOV = 60
			aspect = viz.AUTO_COMPUTE
			stereo = viz.OFF
			
			#VC: create the raw object
			_window.fov(VFOV,aspect)
			_window.stereo(stereo)
			rawDisplay[_name] = _window
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addDisplay(rawDisplay[_name], _name, make='Generic', model='Custom Window')
	
		#VC: set the parent of the node
		if initFlag&vizconnect.INIT_PARENTS:
			vizconnect.getDisplay(_name).setParent(vizconnect.getTracker('head_tracker'))

	#VC: set the name of the default
	vizconnect.setDefault('display', 'rift_display')

	#VC: return values can be modified here
	return None


#################################
# Tracker Code
#################################

def initTrackers(initFlag=vizconnect.INIT_INDEPENDENT, initList=None):
	#VC: place any general initialization code here
	rawTracker = vizconnect.getRawTrackerDict()

	#VC: initialize a new tracker
	_name = 'head_tracker'
	if vizconnect.isPendingInit('tracker', _name, initFlag, initList):
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: set some parameters
			index = 0
			
			#VC: create the raw object
			import steamvr
			try:
				tracker = steamvr.getExtension().getHMDList()[index]
			except IndexError:
				viz.logWarn("** WARNING: Not able to connect to tracker at index {0}. It's likely that not enough trackers are connected.".format(index))
				tracker = viz.addGroup()
				tracker.invalidTracker = True
			rawTracker[_name] = tracker
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addTracker(rawTracker[_name], _name, make='Valve', model='SteamVR HMD Tracker')

	#VC: initialize a new tracker
	_name = 'r_hand_tracker'
	if vizconnect.isPendingInit('tracker', _name, initFlag, initList):
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: set some parameters
			index = 0
			
			#VC: create the raw object
			import steamvr
			try:
				tracker = steamvr.getControllerList()[index]
			except IndexError:
				viz.logWarn("** WARNING: Not able to connect to tracker at index {0}. It's likely that not enough trackers are connected.".format(index))
				tracker = viz.addGroup()
				tracker.invalidTracker = True
			rawTracker[_name] = tracker
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addTracker(rawTracker[_name], _name, make='Valve', model='SteamVR Controller Tracker')

	#VC: set the name of the default
	vizconnect.setDefault('tracker', 'head_tracker')

	#VC: return values can be modified here
	return None


#################################
# Input Code
#################################

def initInputs(initFlag=vizconnect.INIT_INDEPENDENT, initList=None):
	#VC: place any general initialization code here
	rawInput = vizconnect.getRawInputDict()

	#VC: initialize a new input
	_name = 'keyboard'
	if vizconnect.isPendingInit('input', _name, initFlag, initList):
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: set some parameters
			index = 0
			
			#VC: create the raw object
			d = viz.add('directinput.dle')
			device = d.getKeyboardDevices()[index]
			rawInput[_name] = d.addKeyboard(device)
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addInput(rawInput[_name], _name, make='Generic', model='Keyboard')

	#VC: return values can be modified here
	return None


#################################
# Event Code
#################################

def initEvents(initFlag=vizconnect.INIT_INDEPENDENT, initList=None):
	#VC: place any general initialization code here
	rawEvent = vizconnect.getRawEventDict()

	#VC: return values can be modified here
	return None


#################################
# Transport Code
#################################

def initTransports(initFlag=vizconnect.INIT_INDEPENDENT, initList=None):
	#VC: place any general initialization code here
	rawTransport = vizconnect.getRawTransportDict()

	#VC: return values can be modified here
	return None


#################################
# Tool Code
#################################

def initTools(initFlag=vizconnect.INIT_INDEPENDENT, initList=None):
	#VC: place any general initialization code here
	rawTool = vizconnect.getRawToolDict()

	#VC: return values can be modified here
	return None


#################################
# Avatar Code
#################################

def initAvatars(initFlag=vizconnect.INIT_INDEPENDENT, initList=None):
	#VC: place any general initialization code here
	rawAvatar = vizconnect.getRawAvatarDict()

	#VC: return values can be modified here
	return None


#################################
# Application Settings
#################################

def initSettings():
	#VC: apply general application settings
	viz.mouse.setTrap(False)
	viz.mouse.setVisible(viz.MOUSE_AUTO_HIDE)
	vizconnect.setMouseTrapToggleKey('')
	
	#VC: return values can be modified here
	return None


#################################
# Post-initialization Code
#################################

def postInit():
	"""Add any code here which should be called after all of the initialization of this configuration is complete.
	Returned values can be obtained by calling getPostInitResult for this file's vizconnect.Configuration instance."""
	return None


#################################
# Stand alone configuration
#################################

def initInterface():
	#VC: start the interface
	vizconnect.interface.go(__file__,
							live=True,
							openBrowserWindow=True,
							startingInterface=vizconnect.interface.INTERFACE_STARTUP)

	#VC: return values can be modified here
	return None


###############################################

if __name__ == "__main__":
	initInterface()
	viz.add('piazza.osgb')
	viz.add('piazza_animations.osgb')
	
	import vizshape
	
	IPD = viz.MainWindow.getIPD()
	rightEyeBase = vizshape.addSphere(0.05, color = viz.BLUE)
	rightEyeBase.setReferenceFrame(viz.RF_VIEW)
	rightEyeBase.setPosition([IPD/2,0,0])
	rightEyeBase.alpha(0.00)
	link = viz.link(viz.MainView,rightEyeBase,viz.PRIORITY_SCENEGRAPH)
	link.setMask(viz.LINK_ORI)
	
	rightGazePoint = vizshape.addSphere(0.05, color = viz.YELLOW)
	rightGazePoint.setReferenceFrame(viz.RF_VIEW)
	
	smi = viz.add('smi_vive.dle')
	eyeTracker = smi.addEyeTracker()

	IPD = viz.MainWindow.getIPD()
	
	def updateGazeNode(vecLength = 1.0):
		
		rDir = eyeTracker.getRightGazeDirection()
		rightGazePoint.setPosition(-IPD/2 + rDir[0]*vecLength,rDir[1]*vecLength,rDir[2]*vecLength)
		
	vizact.onupdate(viz.PRIORITY_LAST_UPDATE,updateGazeNode)



