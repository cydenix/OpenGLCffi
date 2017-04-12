from OpenGLCffi.GLES3 import params
@params(api='gles3', prms=['shaders', 'maxShaders', 'numShaders'])
def glExtGetShadersQCOM(shaders, maxShaders, numShaders):
	pass


@params(api='gles3', prms=['programs', 'maxPrograms', 'numPrograms'])
def glExtGetProgramsQCOM(programs, maxPrograms, numPrograms):
	pass


@params(api='gles3', prms=['program'])
def glExtIsProgramBinaryQCOM(program):
	pass


@params(api='gles3', prms=['program', 'shadertype', 'source', 'length'])
def glExtGetProgramBinarySourceQCOM(program, shadertype, source, length):
	pass


