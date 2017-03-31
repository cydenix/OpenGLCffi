@params('type', 'program', api='gles2')
def glUseShaderProgramEXT(type, program):
	pass


@params('program', api='gles2')
def glActiveProgramEXT(program):
	pass


@params('type', 'string', api='gles2')
def glCreateShaderProgramEXT(type, string):
	pass


@params('pipeline', 'program', api='gles2')
def glActiveShaderProgramEXT(pipeline, program):
	pass


@params('pipeline', api='gles2')
def glBindProgramPipelineEXT(pipeline):
	pass


@params('type', 'count', 'strings', api='gles2')
def glCreateShaderProgramvEXT(type, count, strings):
	pass


@params('n', 'pipelines', api='gles2')
def glDeleteProgramPipelinesEXT(n, pipelines):
	pass


@params('n', 'pipelines', api='gles2')
def glGenProgramPipelinesEXT(n, pipelines):
	pass


@params('pipeline', 'bufSize', 'length', 'infoLog', api='gles2')
def glGetProgramPipelineInfoLogEXT(pipeline, bufSize, length):
	pass


@params('pipeline', 'pname', 'params', api='gles2')
def glGetProgramPipelineivEXT(pipeline, pname):
	pass


@params('pipeline', api='gles2')
def glIsProgramPipelineEXT(pipeline):
	pass


@params('program', 'pname', 'value', api='gles2')
def glProgramParameteriEXT(program, pname, value):
	pass


@params('program', 'location', 'v0', api='gles2')
def glProgramUniform1fEXT(program, location, v0):
	pass


@params('program', 'location', 'count', 'value', api='gles2')
def glProgramUniform1fvEXT(program, location, count, value):
	pass


@params('program', 'location', 'v0', api='gles2')
def glProgramUniform1iEXT(program, location, v0):
	pass


@params('program', 'location', 'count', 'value', api='gles2')
def glProgramUniform1ivEXT(program, location, count, value):
	pass


@params('program', 'location', 'v0', 'v1', api='gles2')
def glProgramUniform2fEXT(program, location, v0, v1):
	pass


@params('program', 'location', 'count', 'value', api='gles2')
def glProgramUniform2fvEXT(program, location, count, value):
	pass


@params('program', 'location', 'v0', 'v1', api='gles2')
def glProgramUniform2iEXT(program, location, v0, v1):
	pass


@params('program', 'location', 'count', 'value', api='gles2')
def glProgramUniform2ivEXT(program, location, count, value):
	pass


@params('program', 'location', 'v0', 'v1', 'v2', api='gles2')
def glProgramUniform3fEXT(program, location, v0, v1, v2):
	pass


@params('program', 'location', 'count', 'value', api='gles2')
def glProgramUniform3fvEXT(program, location, count, value):
	pass


@params('program', 'location', 'v0', 'v1', 'v2', api='gles2')
def glProgramUniform3iEXT(program, location, v0, v1, v2):
	pass


@params('program', 'location', 'count', 'value', api='gles2')
def glProgramUniform3ivEXT(program, location, count, value):
	pass


@params('program', 'location', 'v0', 'v1', 'v2', 'v3', api='gles2')
def glProgramUniform4fEXT(program, location, v0, v1, v2, v3):
	pass


@params('program', 'location', 'count', 'value', api='gles2')
def glProgramUniform4fvEXT(program, location, count, value):
	pass


@params('program', 'location', 'v0', 'v1', 'v2', 'v3', api='gles2')
def glProgramUniform4iEXT(program, location, v0, v1, v2, v3):
	pass


@params('program', 'location', 'count', 'value', api='gles2')
def glProgramUniform4ivEXT(program, location, count, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gles2')
def glProgramUniformMatrix2fvEXT(program, location, count, transpose, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gles2')
def glProgramUniformMatrix3fvEXT(program, location, count, transpose, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gles2')
def glProgramUniformMatrix4fvEXT(program, location, count, transpose, value):
	pass


@params('pipeline', 'stages', 'program', api='gles2')
def glUseProgramStagesEXT(pipeline, stages, program):
	pass


@params('pipeline', api='gles2')
def glValidateProgramPipelineEXT(pipeline):
	pass


@params('program', 'location', 'v0', api='gles2')
def glProgramUniform1uiEXT(program, location, v0):
	pass


@params('program', 'location', 'v0', 'v1', api='gles2')
def glProgramUniform2uiEXT(program, location, v0, v1):
	pass


@params('program', 'location', 'v0', 'v1', 'v2', api='gles2')
def glProgramUniform3uiEXT(program, location, v0, v1, v2):
	pass


@params('program', 'location', 'v0', 'v1', 'v2', 'v3', api='gles2')
def glProgramUniform4uiEXT(program, location, v0, v1, v2, v3):
	pass


@params('program', 'location', 'count', 'value', api='gles2')
def glProgramUniform1uivEXT(program, location, count, value):
	pass


@params('program', 'location', 'count', 'value', api='gles2')
def glProgramUniform2uivEXT(program, location, count, value):
	pass


@params('program', 'location', 'count', 'value', api='gles2')
def glProgramUniform3uivEXT(program, location, count, value):
	pass


@params('program', 'location', 'count', 'value', api='gles2')
def glProgramUniform4uivEXT(program, location, count, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gles2')
def glProgramUniformMatrix4fvEXT(program, location, count, transpose, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gles2')
def glProgramUniformMatrix2x3fvEXT(program, location, count, transpose, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gles2')
def glProgramUniformMatrix3x2fvEXT(program, location, count, transpose, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gles2')
def glProgramUniformMatrix2x4fvEXT(program, location, count, transpose, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gles2')
def glProgramUniformMatrix4x2fvEXT(program, location, count, transpose, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gles2')
def glProgramUniformMatrix3x4fvEXT(program, location, count, transpose, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gles2')
def glProgramUniformMatrix4x3fvEXT(program, location, count, transpose, value):
	pass


