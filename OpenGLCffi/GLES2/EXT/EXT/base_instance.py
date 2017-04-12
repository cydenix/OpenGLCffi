from OpenGLCffi.GLES2 import params
@params(api='gles2', prms=['mode', 'first', 'count', 'instancecount', 'baseinstance'])
def glDrawArraysInstancedBaseInstanceEXT(mode, first, count, instancecount, baseinstance):
	pass


@params(api='gles2', prms=['mode', 'count', 'type', 'indices', 'instancecount', 'baseinstance'])
def glDrawElementsInstancedBaseInstanceEXT(mode, count, type, indices, instancecount, baseinstance):
	pass


@params(api='gles2', prms=['mode', 'count', 'type', 'indices', 'instancecount', 'basevertex', 'baseinstance'])
def glDrawElementsInstancedBaseVertexBaseInstanceEXT(mode, count, type, indices, instancecount, basevertex, baseinstance):
	pass


