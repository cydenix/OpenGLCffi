from OpenGLCffi.GLES3 import params
@params(api='gles3', prms=['num', 'size', 'driverControls'])
def glGetDriverControlsQCOM(num, size, driverControls):
	pass


@params(api='gles3', prms=['driverControl', 'bufSize', 'length', 'driverControlString'])
def glGetDriverControlStringQCOM(driverControl, bufSize, length, driverControlString):
	pass


@params(api='gles3', prms=['driverControl'])
def glEnableDriverControlQCOM(driverControl):
	pass


@params(api='gles3', prms=['driverControl'])
def glDisableDriverControlQCOM(driverControl):
	pass


