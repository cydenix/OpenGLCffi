from OpenGLCffi.GL import params
@params('mode', 'count', 'type', 'indices', 'basevertex', api='gl')
def glDrawElementsBaseVertex(mode, count, type, indices, basevertex):
	pass


@params('mode', 'start', 'end', 'count', 'type', 'indices', 'basevertex', api='gl')
def glDrawRangeElementsBaseVertex(mode, start, end, count, type, indices, basevertex):
	pass


@params('mode', 'count', 'type', 'indices', 'instancecount', 'basevertex', api='gl')
def glDrawElementsInstancedBaseVertex(mode, count, type, indices, instancecount, basevertex):
	pass


@params('mode', 'count', 'type', 'constindices', 'drawcount', 'basevertex', api='gl')
def glMultiDrawElementsBaseVertex(mode, count, type, constindices, drawcount, basevertex):
	pass


