from OpenGLCffi.GLES2 import params
@params('mode', 'first', 'count', 'instancecount', 'baseinstance', api='gles2')
def glDrawArraysInstancedBaseInstanceEXT(mode, first, count, instancecount, baseinstance):
	pass


@params('mode', 'count', 'type', 'indices', 'instancecount', 'baseinstance', api='gles2')
def glDrawElementsInstancedBaseInstanceEXT(mode, count, type, indices, instancecount, baseinstance):
	pass


@params('mode', 'count', 'type', 'indices', 'instancecount', 'basevertex', 'baseinstance', api='gles2')
def glDrawElementsInstancedBaseVertexBaseInstanceEXT(mode, count, type, indices, instancecount, basevertex, baseinstance):
	pass


