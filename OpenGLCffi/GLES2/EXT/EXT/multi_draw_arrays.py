from OpenGLCffi.GLES2 import params
@params('mode', 'first', 'count', 'primcount', api='gles2')
def glMultiDrawArraysEXT(mode, first, count, primcount):
	pass


@params('mode', 'count', 'type', 'constindices', 'primcount', api='gles2')
def glMultiDrawElementsEXT(mode, count, type, constindices, primcount):
	pass


