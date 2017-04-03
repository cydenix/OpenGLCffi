from OpenGLCffi.GLES3 import params
@params('num', 'size', 'driverControls', api='gles3')
def glGetDriverControlsQCOM(num, size, driverControls):
	pass


@params('driverControl', 'bufSize', 'length', 'driverControlString', api='gles3')
def glGetDriverControlStringQCOM(driverControl, bufSize, length, driverControlString):
	pass


@params('driverControl', api='gles3')
def glEnableDriverControlQCOM(driverControl):
	pass


@params('driverControl', api='gles3')
def glDisableDriverControlQCOM(driverControl):
	pass


