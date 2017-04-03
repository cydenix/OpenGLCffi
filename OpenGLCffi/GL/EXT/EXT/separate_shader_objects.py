from OpenGLCffi.GL import params
@params('type', 'program', api='gl')
def glUseShaderProgramEXT(type, program):
	pass


@params('program', api='gl')
def glActiveProgramEXT(program):
	pass


@params('type', 'string', api='gl')
def glCreateShaderProgramEXT(type, string):
	pass


@params('pipeline', 'program', api='gl')
def glActiveShaderProgramEXT(pipeline, program):
	pass


@params('pipeline', api='gl')
def glBindProgramPipelineEXT(pipeline):
	pass


@params('type', 'count', 'strings', api='gl')
def glCreateShaderProgramvEXT(type, count, strings):
	pass


@params('n', 'pipelines', api='gl')
def glDeleteProgramPipelinesEXT(n, pipelines):
	pass


@params('n', 'pipelines', api='gl')
def glGenProgramPipelinesEXT(n, pipelines):
	pass


@params('pipeline', 'bufSize', 'length', 'infoLog', api='gl')
def glGetProgramPipelineInfoLogEXT(pipeline, bufSize, length, infoLog):
	pass


@params('pipeline', 'pname', 'params', api='gl')
def glGetProgramPipelineivEXT(pipeline, pname, params):
	pass


@params('pipeline', api='gl')
def glIsProgramPipelineEXT(pipeline):
	pass


@params('program', 'pname', 'value', api='gl')
def glProgramParameteriEXT(program, pname, value):
	pass


@params('program', 'location', 'v0', api='gl')
def glProgramUniform1fEXT(program, location, v0):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform1fvEXT(program, location, count, value):
	pass


@params('program', 'location', 'v0', api='gl')
def glProgramUniform1iEXT(program, location, v0):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform1ivEXT(program, location, count, value):
	pass


@params('program', 'location', 'v0', 'v1', api='gl')
def glProgramUniform2fEXT(program, location, v0, v1):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform2fvEXT(program, location, count, value):
	pass


@params('program', 'location', 'v0', 'v1', api='gl')
def glProgramUniform2iEXT(program, location, v0, v1):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform2ivEXT(program, location, count, value):
	pass


@params('program', 'location', 'v0', 'v1', 'v2', api='gl')
def glProgramUniform3fEXT(program, location, v0, v1, v2):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform3fvEXT(program, location, count, value):
	pass


@params('program', 'location', 'v0', 'v1', 'v2', api='gl')
def glProgramUniform3iEXT(program, location, v0, v1, v2):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform3ivEXT(program, location, count, value):
	pass


@params('program', 'location', 'v0', 'v1', 'v2', 'v3', api='gl')
def glProgramUniform4fEXT(program, location, v0, v1, v2, v3):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform4fvEXT(program, location, count, value):
	pass


@params('program', 'location', 'v0', 'v1', 'v2', 'v3', api='gl')
def glProgramUniform4iEXT(program, location, v0, v1, v2, v3):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform4ivEXT(program, location, count, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix2fvEXT(program, location, count, transpose, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix3fvEXT(program, location, count, transpose, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix4fvEXT(program, location, count, transpose, value):
	pass


@params('pipeline', 'stages', 'program', api='gl')
def glUseProgramStagesEXT(pipeline, stages, program):
	pass


@params('pipeline', api='gl')
def glValidateProgramPipelineEXT(pipeline):
	pass


@params('program', 'location', 'v0', api='gl')
def glProgramUniform1uiEXT(program, location, v0):
	pass


@params('program', 'location', 'v0', 'v1', api='gl')
def glProgramUniform2uiEXT(program, location, v0, v1):
	pass


@params('program', 'location', 'v0', 'v1', 'v2', api='gl')
def glProgramUniform3uiEXT(program, location, v0, v1, v2):
	pass


@params('program', 'location', 'v0', 'v1', 'v2', 'v3', api='gl')
def glProgramUniform4uiEXT(program, location, v0, v1, v2, v3):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform1uivEXT(program, location, count, value):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform2uivEXT(program, location, count, value):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform3uivEXT(program, location, count, value):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform4uivEXT(program, location, count, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix4fvEXT(program, location, count, transpose, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix2x3fvEXT(program, location, count, transpose, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix3x2fvEXT(program, location, count, transpose, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix2x4fvEXT(program, location, count, transpose, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix4x2fvEXT(program, location, count, transpose, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix3x4fvEXT(program, location, count, transpose, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix4x3fvEXT(program, location, count, transpose, value):
	pass


