from OpenGLCffi.GLES3 import params
@params(api='gles3', prms=['mode', 'count', 'type', 'indices', 'basevertex'])
def glDrawElementsBaseVertexOES(mode, count, type, indices, basevertex):
	pass


@params(api='gles3', prms=['mode', 'start', 'end', 'count', 'type', 'indices', 'basevertex'])
def glDrawRangeElementsBaseVertexOES(mode, start, end, count, type, indices, basevertex):
	pass


@params(api='gles3', prms=['mode', 'count', 'type', 'indices', 'instancecount', 'basevertex'])
def glDrawElementsInstancedBaseVertexOES(mode, count, type, indices, instancecount, basevertex):
	pass


@params(api='gles3', prms=['mode', 'count', 'type', 'constindices', 'primcount', 'basevertex'])
def glMultiDrawElementsBaseVertexOES(mode, count, type, constindices, primcount, basevertex):
	pass


