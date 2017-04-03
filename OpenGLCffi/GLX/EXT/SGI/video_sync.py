from OpenGLCffi.GLX import params
@params('count', api='glx')
def glXGetVideoSyncSGI(count):
	pass


@params('divisor', 'remainder', 'count', api='glx')
def glXWaitVideoSyncSGI(divisor, remainder, count):
	pass


