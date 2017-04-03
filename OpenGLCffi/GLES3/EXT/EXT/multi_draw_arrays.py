from OpenGLCffi.GLES3 import params
@params('mode', 'first', 'count', 'primcount', api='gles3')
def glMultiDrawArraysEXT(mode, first, count, primcount):
	pass


@params('mode', 'count', 'type', 'constindices', 'primcount', api='gles3')
def glMultiDrawElementsEXT(mode, count, type, constindices, primcount):
	pass


