from OpenGLCffi.GLES3 import params
@params(api='gles3', prms=['target', 'access'])
def glMapBufferOES(target, access):
	pass


@params(api='gles3', prms=['target'])
def glUnmapBufferOES(target):
	pass


@params(api='gles3', prms=['target', 'pname', 'params'])
def glGetBufferPointervOES(target, pname):
	pass


