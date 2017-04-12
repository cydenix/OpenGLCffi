from OpenGLCffi.GL import params
@params(api='gl', prms=['type', 'program'])
def glUseShaderProgramEXT(type, program):
	pass


@params(api='gl', prms=['program'])
def glActiveProgramEXT(program):
	pass


@params(api='gl', prms=['type', 'string'])
def glCreateShaderProgramEXT(type, string):
	pass


@params(api='gl', prms=['pipeline', 'program'])
def glActiveShaderProgramEXT(pipeline, program):
	pass


@params(api='gl', prms=['pipeline'])
def glBindProgramPipelineEXT(pipeline):
	pass


@params(api='gl', prms=['type', 'count', 'strings'])
def glCreateShaderProgramvEXT(type, count, strings):
	pass


@params(api='gl', prms=['n', 'pipelines'])
def glDeleteProgramPipelinesEXT(n, pipelines):
	pass


@params(api='gl', prms=['n', 'pipelines'])
def glGenProgramPipelinesEXT(n, pipelines):
	pass


@params(api='gl', prms=['pipeline', 'bufSize', 'length', 'infoLog'])
def glGetProgramPipelineInfoLogEXT(pipeline, bufSize, length, infoLog):
	pass


@params(api='gl', prms=['pipeline', 'pname', 'params'])
def glGetProgramPipelineivEXT(pipeline, pname, params):
	pass


@params(api='gl', prms=['pipeline'])
def glIsProgramPipelineEXT(pipeline):
	pass


@params(api='gl', prms=['program', 'pname', 'value'])
def glProgramParameteriEXT(program, pname, value):
	pass


@params(api='gl', prms=['program', 'location', 'v0'])
def glProgramUniform1fEXT(program, location, v0):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform1fvEXT(program, location, count, value):
	pass


@params(api='gl', prms=['program', 'location', 'v0'])
def glProgramUniform1iEXT(program, location, v0):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform1ivEXT(program, location, count, value):
	pass


@params(api='gl', prms=['program', 'location', 'v0', 'v1'])
def glProgramUniform2fEXT(program, location, v0, v1):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform2fvEXT(program, location, count, value):
	pass


@params(api='gl', prms=['program', 'location', 'v0', 'v1'])
def glProgramUniform2iEXT(program, location, v0, v1):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform2ivEXT(program, location, count, value):
	pass


@params(api='gl', prms=['program', 'location', 'v0', 'v1', 'v2'])
def glProgramUniform3fEXT(program, location, v0, v1, v2):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform3fvEXT(program, location, count, value):
	pass


@params(api='gl', prms=['program', 'location', 'v0', 'v1', 'v2'])
def glProgramUniform3iEXT(program, location, v0, v1, v2):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform3ivEXT(program, location, count, value):
	pass


@params(api='gl', prms=['program', 'location', 'v0', 'v1', 'v2', 'v3'])
def glProgramUniform4fEXT(program, location, v0, v1, v2, v3):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform4fvEXT(program, location, count, value):
	pass


@params(api='gl', prms=['program', 'location', 'v0', 'v1', 'v2', 'v3'])
def glProgramUniform4iEXT(program, location, v0, v1, v2, v3):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform4ivEXT(program, location, count, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix2fvEXT(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix3fvEXT(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix4fvEXT(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['pipeline', 'stages', 'program'])
def glUseProgramStagesEXT(pipeline, stages, program):
	pass


@params(api='gl', prms=['pipeline'])
def glValidateProgramPipelineEXT(pipeline):
	pass


@params(api='gl', prms=['program', 'location', 'v0'])
def glProgramUniform1uiEXT(program, location, v0):
	pass


@params(api='gl', prms=['program', 'location', 'v0', 'v1'])
def glProgramUniform2uiEXT(program, location, v0, v1):
	pass


@params(api='gl', prms=['program', 'location', 'v0', 'v1', 'v2'])
def glProgramUniform3uiEXT(program, location, v0, v1, v2):
	pass


@params(api='gl', prms=['program', 'location', 'v0', 'v1', 'v2', 'v3'])
def glProgramUniform4uiEXT(program, location, v0, v1, v2, v3):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform1uivEXT(program, location, count, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform2uivEXT(program, location, count, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform3uivEXT(program, location, count, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform4uivEXT(program, location, count, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix4fvEXT(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix2x3fvEXT(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix3x2fvEXT(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix2x4fvEXT(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix4x2fvEXT(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix3x4fvEXT(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix4x3fvEXT(program, location, count, transpose, value):
	pass


