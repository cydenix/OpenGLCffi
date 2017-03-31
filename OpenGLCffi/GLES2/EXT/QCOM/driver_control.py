@params('num', 'size', 'driverControls', api='gles2')
def glGetDriverControlsQCOM(num, size, driverControls):
	pass


@params('driverControl', 'bufSize', 'length', 'driverControlString', api='gles2')
def glGetDriverControlStringQCOM(driverControl, bufSize, length, driverControlString):
	pass


@params('driverControl', api='gles2')
def glEnableDriverControlQCOM(driverControl):
	pass


@params('driverControl', api='gles2')
def glDisableDriverControlQCOM(driverControl):
	pass


