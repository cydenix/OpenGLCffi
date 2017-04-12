from OpenGLCffi.GLES1 import params
@params(api='gles1', prms=['mode', 'first', 'count', 'primcount'])
def glMultiDrawArraysEXT(mode, first, count, primcount):
	pass


@params(api='gles1', prms=['mode', 'count', 'type', 'constindices', 'primcount'])
def glMultiDrawElementsEXT(mode, count, type, constindices, primcount):
	pass


