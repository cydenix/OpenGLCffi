from OpenGLCffi.GLES2 import params
@params(api='gles2', prms=['target', 'access'])
def glMapBufferOES(target, access):
	pass


@params(api='gles2', prms=['target'])
def glUnmapBufferOES(target):
	pass


@params(api='gles2', prms=['target', 'pname', 'params'])
def glGetBufferPointervOES(target, pname):
	pass


