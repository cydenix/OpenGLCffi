from OpenGLCffi.GLES2 import params
@params('target', 'access', api='gles2')
def glMapBufferOES(target, access):
	pass


@params('target', api='gles2')
def glUnmapBufferOES(target):
	pass


@params('target', 'pname', 'params', api='gles2')
def glGetBufferPointervOES(target, pname):
	pass


