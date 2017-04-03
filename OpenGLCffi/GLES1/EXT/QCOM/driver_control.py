from OpenGLCffi.GLES1 import params
@params('num', 'size', 'driverControls', api='gles1')
def glGetDriverControlsQCOM(num, size, driverControls):
	pass


@params('driverControl', 'bufSize', 'length', 'driverControlString', api='gles1')
def glGetDriverControlStringQCOM(driverControl, bufSize, length, driverControlString):
	pass


@params('driverControl', api='gles1')
def glEnableDriverControlQCOM(driverControl):
	pass


@params('driverControl', api='gles1')
def glDisableDriverControlQCOM(driverControl):
	pass


