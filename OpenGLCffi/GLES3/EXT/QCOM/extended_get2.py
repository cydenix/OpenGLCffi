from OpenGLCffi.GLES3 import params
@params('shaders', 'maxShaders', 'numShaders', api='gles3')
def glExtGetShadersQCOM(shaders, maxShaders, numShaders):
	pass


@params('programs', 'maxPrograms', 'numPrograms', api='gles3')
def glExtGetProgramsQCOM(programs, maxPrograms, numPrograms):
	pass


@params('program', api='gles3')
def glExtIsProgramBinaryQCOM(program):
	pass


@params('program', 'shadertype', 'source', 'length', api='gles3')
def glExtGetProgramBinarySourceQCOM(program, shadertype, source, length):
	pass


