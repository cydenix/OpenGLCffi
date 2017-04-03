from OpenGLCffi.GLES3 import params
@params('mode', 'start', 'count', 'primcount', api='gles3')
def glDrawArraysInstancedEXT(mode, start, count, primcount):
	pass


@params('mode', 'count', 'type', 'indices', 'primcount', api='gles3')
def glDrawElementsInstancedEXT(mode, count, type, indices, primcount):
	pass


@params('index', 'divisor', api='gles3')
def glVertexAttribDivisorEXT(index, divisor):
	pass


