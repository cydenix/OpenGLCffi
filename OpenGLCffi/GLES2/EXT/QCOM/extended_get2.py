from OpenGLCffi.GLES2 import params
@params('shaders', 'maxShaders', 'numShaders', api='gles2')
def glExtGetShadersQCOM(shaders, maxShaders, numShaders):
	pass


@params('programs', 'maxPrograms', 'numPrograms', api='gles2')
def glExtGetProgramsQCOM(programs, maxPrograms, numPrograms):
	pass


@params('program', api='gles2')
def glExtIsProgramBinaryQCOM(program):
	pass


@params('program', 'shadertype', 'source', 'length', api='gles2')
def glExtGetProgramBinarySourceQCOM(program, shadertype, source, length):
	pass


