from OpenGLCffi.GLX import params
@params(api='glx', prms=['count'])
def glXGetVideoSyncSGI(count):
	pass


@params(api='glx', prms=['divisor', 'remainder', 'count'])
def glXWaitVideoSyncSGI(divisor, remainder, count):
	pass


