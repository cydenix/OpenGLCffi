from OpenGLCffi.GLES3 import params
@params(api='gles3', prms=['mode', 'count', 'type', 'indices', 'basevertex'])
def glDrawElementsBaseVertexEXT(mode, count, type, indices, basevertex):
	pass


@params(api='gles3', prms=['mode', 'start', 'end', 'count', 'type', 'indices', 'basevertex'])
def glDrawRangeElementsBaseVertexEXT(mode, start, end, count, type, indices, basevertex):
	pass


@params(api='gles3', prms=['mode', 'count', 'type', 'indices', 'instancecount', 'basevertex'])
def glDrawElementsInstancedBaseVertexEXT(mode, count, type, indices, instancecount, basevertex):
	pass


@params(api='gles3', prms=['mode', 'count', 'type', 'constindices', 'primcount', 'basevertex'])
def glMultiDrawElementsBaseVertexEXT(mode, count, type, constindices, primcount, basevertex):
	pass


