@params('pipeline', 'stages', 'program', api='gl')
def glUseProgramStages(pipeline, stages, program):
	pass


@params('pipeline', 'program', api='gl')
def glActiveShaderProgram(pipeline, program):
	pass


@params('type', 'count', 'conststrings', api='gl')
def glCreateShaderProgramv(type, count, conststrings):
	pass


@params('pipeline', api='gl')
def glBindProgramPipeline(pipeline):
	pass


@params('n', 'pipelines', api='gl')
def glDeleteProgramPipelines(n, pipelines):
	pass


@params('n', 'pipelines', api='gl')
def glGenProgramPipelines(n, pipelines):
	pass


@params('pipeline', api='gl')
def glIsProgramPipeline(pipeline):
	pass


@params('pipeline', 'pname', 'params', api='gl')
def glGetProgramPipelineiv(pipeline, pname, params):
	pass


@params('program', 'location', 'v0', api='gl')
def glProgramUniform1i(program, location, v0):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform1iv(program, location, count, value):
	pass


@params('program', 'location', 'v0', api='gl')
def glProgramUniform1f(program, location, v0):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform1fv(program, location, count, value):
	pass


@params('program', 'location', 'v0', api='gl')
def glProgramUniform1d(program, location, v0):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform1dv(program, location, count, value):
	pass


@params('program', 'location', 'v0', api='gl')
def glProgramUniform1ui(program, location, v0):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform1uiv(program, location, count, value):
	pass


@params('program', 'location', 'v0', 'v1', api='gl')
def glProgramUniform2i(program, location, v0, v1):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform2iv(program, location, count, value):
	pass


@params('program', 'location', 'v0', 'v1', api='gl')
def glProgramUniform2f(program, location, v0, v1):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform2fv(program, location, count, value):
	pass


@params('program', 'location', 'v0', 'v1', api='gl')
def glProgramUniform2d(program, location, v0, v1):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform2dv(program, location, count, value):
	pass


@params('program', 'location', 'v0', 'v1', api='gl')
def glProgramUniform2ui(program, location, v0, v1):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform2uiv(program, location, count, value):
	pass


@params('program', 'location', 'v0', 'v1', 'v2', api='gl')
def glProgramUniform3i(program, location, v0, v1, v2):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform3iv(program, location, count, value):
	pass


@params('program', 'location', 'v0', 'v1', 'v2', api='gl')
def glProgramUniform3f(program, location, v0, v1, v2):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform3fv(program, location, count, value):
	pass


@params('program', 'location', 'v0', 'v1', 'v2', api='gl')
def glProgramUniform3d(program, location, v0, v1, v2):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform3dv(program, location, count, value):
	pass


@params('program', 'location', 'v0', 'v1', 'v2', api='gl')
def glProgramUniform3ui(program, location, v0, v1, v2):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform3uiv(program, location, count, value):
	pass


@params('program', 'location', 'v0', 'v1', 'v2', 'v3', api='gl')
def glProgramUniform4i(program, location, v0, v1, v2, v3):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform4iv(program, location, count, value):
	pass


@params('program', 'location', 'v0', 'v1', 'v2', 'v3', api='gl')
def glProgramUniform4f(program, location, v0, v1, v2, v3):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform4fv(program, location, count, value):
	pass


@params('program', 'location', 'v0', 'v1', 'v2', 'v3', api='gl')
def glProgramUniform4d(program, location, v0, v1, v2, v3):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform4dv(program, location, count, value):
	pass


@params('program', 'location', 'v0', 'v1', 'v2', 'v3', api='gl')
def glProgramUniform4ui(program, location, v0, v1, v2, v3):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform4uiv(program, location, count, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix2fv(program, location, count, transpose, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix3fv(program, location, count, transpose, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix4fv(program, location, count, transpose, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix2dv(program, location, count, transpose, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix3dv(program, location, count, transpose, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix4dv(program, location, count, transpose, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix2x3fv(program, location, count, transpose, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix3x2fv(program, location, count, transpose, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix2x4fv(program, location, count, transpose, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix4x2fv(program, location, count, transpose, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix3x4fv(program, location, count, transpose, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix4x3fv(program, location, count, transpose, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix2x3dv(program, location, count, transpose, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix3x2dv(program, location, count, transpose, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix2x4dv(program, location, count, transpose, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix4x2dv(program, location, count, transpose, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix3x4dv(program, location, count, transpose, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix4x3dv(program, location, count, transpose, value):
	pass


@params('pipeline', api='gl')
def glValidateProgramPipeline(pipeline):
	pass


@params('pipeline', 'bufSize', 'length', 'infoLog', api='gl')
def glGetProgramPipelineInfoLog(pipeline, bufSize, length, infoLog):
	pass


