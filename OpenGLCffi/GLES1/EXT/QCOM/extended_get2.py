from OpenGLCffi.GLES1 import params
@params(api='gles1', prms=['shaders', 'maxShaders', 'numShaders'])
def glExtGetShadersQCOM(shaders, maxShaders, numShaders):
	pass


@params(api='gles1', prms=['programs', 'maxPrograms', 'numPrograms'])
def glExtGetProgramsQCOM(programs, maxPrograms, numPrograms):
	pass


@params(api='gles1', prms=['program'])
def glExtIsProgramBinaryQCOM(program):
	pass


@params(api='gles1', prms=['program', 'shadertype', 'source', 'length'])
def glExtGetProgramBinarySourceQCOM(program, shadertype, source, length):
	pass


