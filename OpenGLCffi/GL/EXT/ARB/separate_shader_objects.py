from OpenGLCffi.GL import params
@params(api='gl', prms=['pipeline', 'stages', 'program'])
def glUseProgramStages(pipeline, stages, program):
	pass


@params(api='gl', prms=['pipeline', 'program'])
def glActiveShaderProgram(pipeline, program):
	pass


@params(api='gl', prms=['type', 'count', 'conststrings'])
def glCreateShaderProgramv(type, count, conststrings):
	pass


@params(api='gl', prms=['pipeline'])
def glBindProgramPipeline(pipeline):
	pass


@params(api='gl', prms=['n', 'pipelines'])
def glDeleteProgramPipelines(n, pipelines):
	pass


@params(api='gl', prms=['n', 'pipelines'])
def glGenProgramPipelines(n, pipelines):
	pass


@params(api='gl', prms=['pipeline'])
def glIsProgramPipeline(pipeline):
	pass


@params(api='gl', prms=['pipeline', 'pname', 'params'])
def glGetProgramPipelineiv(pipeline, pname, params):
	pass


@params(api='gl', prms=['program', 'location', 'v0'])
def glProgramUniform1i(program, location, v0):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform1iv(program, location, count, value):
	pass


@params(api='gl', prms=['program', 'location', 'v0'])
def glProgramUniform1f(program, location, v0):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform1fv(program, location, count, value):
	pass


@params(api='gl', prms=['program', 'location', 'v0'])
def glProgramUniform1d(program, location, v0):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform1dv(program, location, count, value):
	pass


@params(api='gl', prms=['program', 'location', 'v0'])
def glProgramUniform1ui(program, location, v0):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform1uiv(program, location, count, value):
	pass


@params(api='gl', prms=['program', 'location', 'v0', 'v1'])
def glProgramUniform2i(program, location, v0, v1):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform2iv(program, location, count, value):
	pass


@params(api='gl', prms=['program', 'location', 'v0', 'v1'])
def glProgramUniform2f(program, location, v0, v1):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform2fv(program, location, count, value):
	pass


@params(api='gl', prms=['program', 'location', 'v0', 'v1'])
def glProgramUniform2d(program, location, v0, v1):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform2dv(program, location, count, value):
	pass


@params(api='gl', prms=['program', 'location', 'v0', 'v1'])
def glProgramUniform2ui(program, location, v0, v1):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform2uiv(program, location, count, value):
	pass


@params(api='gl', prms=['program', 'location', 'v0', 'v1', 'v2'])
def glProgramUniform3i(program, location, v0, v1, v2):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform3iv(program, location, count, value):
	pass


@params(api='gl', prms=['program', 'location', 'v0', 'v1', 'v2'])
def glProgramUniform3f(program, location, v0, v1, v2):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform3fv(program, location, count, value):
	pass


@params(api='gl', prms=['program', 'location', 'v0', 'v1', 'v2'])
def glProgramUniform3d(program, location, v0, v1, v2):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform3dv(program, location, count, value):
	pass


@params(api='gl', prms=['program', 'location', 'v0', 'v1', 'v2'])
def glProgramUniform3ui(program, location, v0, v1, v2):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform3uiv(program, location, count, value):
	pass


@params(api='gl', prms=['program', 'location', 'v0', 'v1', 'v2', 'v3'])
def glProgramUniform4i(program, location, v0, v1, v2, v3):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform4iv(program, location, count, value):
	pass


@params(api='gl', prms=['program', 'location', 'v0', 'v1', 'v2', 'v3'])
def glProgramUniform4f(program, location, v0, v1, v2, v3):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform4fv(program, location, count, value):
	pass


@params(api='gl', prms=['program', 'location', 'v0', 'v1', 'v2', 'v3'])
def glProgramUniform4d(program, location, v0, v1, v2, v3):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform4dv(program, location, count, value):
	pass


@params(api='gl', prms=['program', 'location', 'v0', 'v1', 'v2', 'v3'])
def glProgramUniform4ui(program, location, v0, v1, v2, v3):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform4uiv(program, location, count, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix2fv(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix3fv(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix4fv(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix2dv(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix3dv(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix4dv(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix2x3fv(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix3x2fv(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix2x4fv(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix4x2fv(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix3x4fv(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix4x3fv(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix2x3dv(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix3x2dv(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix2x4dv(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix4x2dv(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix3x4dv(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix4x3dv(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['pipeline'])
def glValidateProgramPipeline(pipeline):
	pass


@params(api='gl', prms=['pipeline', 'bufSize', 'length', 'infoLog'])
def glGetProgramPipelineInfoLog(pipeline, bufSize, length, infoLog):
	pass


