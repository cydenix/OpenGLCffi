from OpenGLCffi.GL import params
@params(api='gl', prms=['mode', 'first', 'count', 'instancecount', 'baseinstance'])
def glDrawArraysInstancedBaseInstance(mode, first, count, instancecount, baseinstance):
	pass


@params(api='gl', prms=['mode', 'count', 'type', 'indices', 'instancecount', 'baseinstance'])
def glDrawElementsInstancedBaseInstance(mode, count, type, indices, instancecount, baseinstance):
	pass


@params(api='gl', prms=['mode', 'count', 'type', 'indices', 'instancecount', 'basevertex', 'baseinstance'])
def glDrawElementsInstancedBaseVertexBaseInstance(mode, count, type, indices, instancecount, basevertex, baseinstance):
	pass


