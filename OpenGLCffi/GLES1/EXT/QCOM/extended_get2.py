from OpenGLCffi.GLES1 import params
@params('shaders', 'maxShaders', 'numShaders', api='gles1')
def glExtGetShadersQCOM(shaders, maxShaders, numShaders):
	pass


@params('programs', 'maxPrograms', 'numPrograms', api='gles1')
def glExtGetProgramsQCOM(programs, maxPrograms, numPrograms):
	pass


@params('program', api='gles1')
def glExtIsProgramBinaryQCOM(program):
	pass


@params('program', 'shadertype', 'source', 'length', api='gles1')
def glExtGetProgramBinarySourceQCOM(program, shadertype, source, length):
	pass


