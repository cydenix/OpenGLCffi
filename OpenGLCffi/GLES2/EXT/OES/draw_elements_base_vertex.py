from OpenGLCffi.GLES2 import params
@params('mode', 'count', 'type', 'indices', 'basevertex', api='gles2')
def glDrawElementsBaseVertexOES(mode, count, type, indices, basevertex):
	pass


@params('mode', 'start', 'end', 'count', 'type', 'indices', 'basevertex', api='gles2')
def glDrawRangeElementsBaseVertexOES(mode, start, end, count, type, indices, basevertex):
	pass


@params('mode', 'count', 'type', 'indices', 'instancecount', 'basevertex', api='gles2')
def glDrawElementsInstancedBaseVertexOES(mode, count, type, indices, instancecount, basevertex):
	pass


@params('mode', 'count', 'type', 'constindices', 'primcount', 'basevertex', api='gles2')
def glMultiDrawElementsBaseVertexOES(mode, count, type, constindices, primcount, basevertex):
	pass

