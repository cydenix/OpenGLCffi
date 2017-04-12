from OpenGLCffi.GLES1 import params
@params(api='gles1', prms=['target', 'access'])
def glMapBufferOES(target, access):
	pass


@params(api='gles1', prms=['target'])
def glUnmapBufferOES(target):
	pass


@params(api='gles1', prms=['target', 'pname', 'params'])
def glGetBufferPointervOES(target, pname):
	pass


