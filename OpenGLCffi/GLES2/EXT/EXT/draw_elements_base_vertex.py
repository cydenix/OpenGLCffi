from OpenGLCffi.GLES2 import params
@params('mode', 'count', 'type', 'indices', 'basevertex', api='gles2')
def glDrawElementsBaseVertexEXT(mode, count, type, indices, basevertex):
	pass


@params('mode', 'start', 'end', 'count', 'type', 'indices', 'basevertex', api='gles2')
def glDrawRangeElementsBaseVertexEXT(mode, start, end, count, type, indices, basevertex):
	pass


@params('mode', 'count', 'type', 'indices', 'instancecount', 'basevertex', api='gles2')
def glDrawElementsInstancedBaseVertexEXT(mode, count, type, indices, instancecount, basevertex):
	pass


@params('mode', 'count', 'type', 'constindices', 'primcount', 'basevertex', api='gles2')
def glMultiDrawElementsBaseVertexEXT(mode, count, type, constindices, primcount, basevertex):
	pass


