from OpenGLCffi.GLES2 import params
@params(api='gles2', prms=['num', 'size', 'driverControls'])
def glGetDriverControlsQCOM(num, size, driverControls):
	pass


@params(api='gles2', prms=['driverControl', 'bufSize', 'length', 'driverControlString'])
def glGetDriverControlStringQCOM(driverControl, bufSize, length, driverControlString):
	pass


@params(api='gles2', prms=['driverControl'])
def glEnableDriverControlQCOM(driverControl):
	pass


@params(api='gles2', prms=['driverControl'])
def glDisableDriverControlQCOM(driverControl):
	pass


