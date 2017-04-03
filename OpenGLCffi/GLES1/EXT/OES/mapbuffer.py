from OpenGLCffi.GLES1 import params
@params('target', 'access', api='gles1')
def glMapBufferOES(target, access):
	pass


@params('target', api='gles1')
def glUnmapBufferOES(target):
	pass


@params('target', 'pname', 'params', api='gles1')
def glGetBufferPointervOES(target, pname):
	pass


