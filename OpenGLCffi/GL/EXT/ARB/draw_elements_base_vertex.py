from OpenGLCffi.GL import params
@params(api='gl', prms=['mode', 'count', 'type', 'indices', 'basevertex'])
def glDrawElementsBaseVertex(mode, count, type, indices, basevertex):
	pass


@params(api='gl', prms=['mode', 'start', 'end', 'count', 'type', 'indices', 'basevertex'])
def glDrawRangeElementsBaseVertex(mode, start, end, count, type, indices, basevertex):
	pass


@params(api='gl', prms=['mode', 'count', 'type', 'indices', 'instancecount', 'basevertex'])
def glDrawElementsInstancedBaseVertex(mode, count, type, indices, instancecount, basevertex):
	pass


@params(api='gl', prms=['mode', 'count', 'type', 'constindices', 'drawcount', 'basevertex'])
def glMultiDrawElementsBaseVertex(mode, count, type, constindices, drawcount, basevertex):
	pass


