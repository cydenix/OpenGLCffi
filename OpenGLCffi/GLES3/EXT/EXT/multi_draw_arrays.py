from OpenGLCffi.GLES3 import params
@params(api='gles3', prms=['mode', 'first', 'count', 'primcount'])
def glMultiDrawArraysEXT(mode, first, count, primcount):
	pass


@params(api='gles3', prms=['mode', 'count', 'type', 'constindices', 'primcount'])
def glMultiDrawElementsEXT(mode, count, type, constindices, primcount):
	pass


