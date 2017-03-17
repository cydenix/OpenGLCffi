from OpenGLCffi.GLES3 import params
@params('face', 'mask', api='gles3')
def glStencilMaskSeparate(face, mask):
	pass


@params('target', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth', 'format', 'imageSize', 'data', api='gles3')
def glCompressedTexSubImage3D(target, level, xoffset, yoffset, zoffset, width, height, depth, format, imageSize, data):
	pass


@params('buffer', api='gles3')
def glIsBuffer(buffer):
	pass


@params('pname', 'index', 'val', api='gles3')
def glGetMultisamplefv(pname, index):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gles3')
def glProgramUniformMatrix4fv(program, location, count, transpose, value):
	pass


@params('source', 'type', 'severity', 'count', 'ids', 'enabled', api='gles3')
def glDebugMessageControl(source, type, severity, count, ids, enabled):
	pass


@params('target', 'internalformat', 'width', 'height', api='gles3')
def glRenderbufferStorage(target, internalformat, width, height):
	pass


@params('program', 'location', 'v0', 'v1', 'v2', api='gles3')
def glProgramUniform3f(program, location, v0, v1, v2):
	pass


@params(api = 'gles3')
def glResumeTransformFeedback():
	pass


@params(api = 'gles3')
def glGetGraphicsResetStatus():
	pass


@params('index', 'v', api='gles3')
def glVertexAttrib1fv(index, v):
	pass


@params('cap', api='gles3')
def glIsEnabled(cap):
	pass


@params('fail', 'zfail', 'zpass', api='gles3')
def glStencilOp(fail, zfail, zpass):
	pass


@params('n', 'framebuffers', api='gles3')
def glGenFramebuffers(n):
	pass


@params('program', 'maxCount', 'count', 'shaders', api='gles3')
def glGetAttachedShaders(program, maxCount):
	pass


@params('n', 'arrays', api='gles3')
def glDeleteVertexArrays(n, arrays):
	pass


@params('pname', 'params', api='gles3')
def glGetPointerv(pname):
	pass


@params('program', 'location', 'params', api='gles3')
def glGetUniformfv(program, location):
	pass


@params('program', 'location', 'params', api='gles3')
def glGetUniformuiv(program, location):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gles3')
def glProgramUniformMatrix3fv(program, location, count, transpose, value):
	pass


@params('mode', 'count', 'type', 'indices', 'instancecount', api='gles3')
def glDrawElementsInstanced(mode, count, type, indices, instancecount):
	pass


@params('target', 'pname', 'params', api='gles3')
def glGetRenderbufferParameteriv(target, pname):
	pass


@params('condition', 'flags', api='gles3')
def glFenceSync(condition, flags):
	pass


@params('pipeline', api='gles3')
def glValidateProgramPipeline(pipeline):
	pass


@params('count', 'samplers', api='gles3')
def glGenSamplers(samplers):
	pass


@params('target', 'pname', 'params', api='gles3')
def glGetTexParameterIuiv(target, pname):
	pass


@params('sync', api='gles3')
def glIsSync(sync):
	pass


@params('ptr', 'bufSize', 'length', 'label', api='gles3')
def glGetObjectPtrLabel(ptr, bufSize):
	pass


@params('target', 'level', 'internalformat', 'x', 'y', 'width', 'height', 'border', api='gles3')
def glCopyTexImage2D(target, level, internalformat, x, y, width, height, border):
	pass


@params('location', 'count', 'value', api='gles3')
def glUniform4uiv(location, count, value):
	pass


@params('target', 'numAttachments', 'attachments', 'x', 'y', 'width', 'height', api='gles3')
def glInvalidateSubFramebuffer(target, numAttachments, attachments, x, y, width, height):
	pass


@params('sync', api='gles3')
def glDeleteSync(sync):
	pass


@params('location', 'count', 'value', api='gles3')
def glUniform3iv(location, count, value):
	pass


@params('program', api='gles3')
def glUseProgram(program):
	pass


@params('program', 'bufSize', 'length', 'infoLog', api='gles3')
def glGetProgramInfoLog(program, bufSize):
	pass


@params('pname', 'data', api='gles3')
def glGetBooleanv(pname):
	pass


@params('shader', api='gles3')
def glDeleteShader(shader):
	pass


@params('attribindex', 'size', 'type', 'normalized', 'relativeoffset', api='gles3')
def glVertexAttribFormat(attribindex, size, type, normalized, relativeoffset):
	pass


@params('target', 'pname', 'param', api='gles3')
def glTexParameterf(target, pname, param):
	pass


@params('attribindex', 'bindingindex', api='gles3')
def glVertexAttribBinding(attribindex, bindingindex):
	pass


@params('target', 'pname', 'param', api='gles3')
def glTexParameteri(target, pname, param):
	pass


@params('shader', 'bufSize', 'length', 'source', api='gles3')
def glGetShaderSource(shader, bufSize):
	pass


@params('n', 'pipelines', api='gles3')
def glGenProgramPipelines(n, pipelines):
	pass


@params('index', 'v', api='gles3')
def glVertexAttrib3fv(index, v):
	pass


@params('program', api='gles3')
def glLinkProgram(program):
	pass


@params('identifier', 'name', 'bufSize', 'length', 'label', api='gles3')
def glGetObjectLabel(identifier, name, bufSize):
	pass


@params('name', api='gles3')
def glGetString(name):
	pass


@params('target', api='gles3')
def glEndQuery(target):
	pass


@params('target', 'pname', 'param', api='gles3')
def glFramebufferParameteri(target, pname, param):
	pass


@params('n', 'textures', api='gles3')
def glDeleteTextures(n, textures):
	pass


@params('index', 'x', 'y', 'z', 'w', api='gles3')
def glVertexAttrib4f(index, x, y, z, w):
	pass


@params('sampler', 'pname', 'param', api='gles3')
def glSamplerParameteri(sampler, pname, param):
	pass


@params('program', 'uniformBlockIndex', 'pname', 'params', api='gles3')
def glGetActiveUniformBlockiv(program, uniformBlockIndex, pname):
	pass


@params('location', 'v0', api='gles3')
def glUniform1i(location, v0):
	pass


@params('mode', api='gles3')
def glCullFace(mode):
	pass


@params('program', 'location', 'v0', 'v1', 'v2', 'v3', api='gles3')
def glProgramUniform4i(program, location, v0, v1, v2, v3):
	pass


@params('program', 'location', 'v0', 'v1', 'v2', 'v3', api='gles3')
def glProgramUniform4f(program, location, v0, v1, v2, v3):
	pass


@params('program', 'shader', api='gles3')
def glAttachShader(program, shader):
	pass


@params('target', 'pname', 'params', api='gles3')
def glGetBufferParameteriv(target, pname):
	pass


@params('target', 'pname', 'params', api='gles3')
def glTexParameterIuiv(target, pname, params):
	pass


@params('id', api='gles3')
def glIsTransformFeedback(id):
	pass


@params('pipeline', api='gles3')
def glIsProgramPipeline(pipeline):
	pass


@params('location', 'count', 'transpose', 'value', api='gles3')
def glUniformMatrix3fv(location, count, transpose, value):
	pass


@params('program', 'location', 'bufSize', 'params', api='gles3')
def glGetnUniformfv(program, location, bufSize):
	pass


@params('func', 'ref', 'mask', api='gles3')
def glStencilFunc(func, ref, mask):
	pass


@params('pipeline', 'pname', 'params', api='gles3')
def glGetProgramPipelineiv(pipeline, pname):
	pass


@params('indirect', api='gles3')
def glDispatchComputeIndirect(indirect):
	pass


@params('shader', 'bufSize', 'length', 'infoLog', api='gles3')
def glGetShaderInfoLog(shader, bufSize):
	pass


@params('index', 'x', 'y', 'z', 'w', api='gles3')
def glVertexAttribI4i(index, x, y, z, w):
	pass


@params('modeRGB', 'modeAlpha', api='gles3')
def glBlendEquationSeparate(modeRGB, modeAlpha):
	pass


@params('n', 'buffers', api='gles3')
def glDeleteBuffers(n, buffers):
	pass


@params('pipeline', api='gles3')
def glBindProgramPipeline(pipeline):
	pass


@params('x', 'y', 'width', 'height', api='gles3')
def glScissor(x, y, width, height):
	pass


@params('name', 'index', api='gles3')
def glGetStringi(name, index):
	pass


@params('location', 'count', 'value', api='gles3')
def glUniform2fv(location, count, value):
	pass


@params('target', 'index', 'buffer', 'offset', 'size', api='gles3')
def glBindBufferRange(target, index, buffer, offset, size):
	pass


@params('sync', 'flags', 'timeout', api='gles3')
def glClientWaitSync(sync, flags, timeout):
	pass


@params('x', 'y', 'width', 'height', 'format', 'type', 'bufSize', 'data', api='gles3')
def glReadnPixels(x, y, width, height, format, type, bufSize, data):
	pass


@params('srcName', 'srcTarget', 'srcLevel', 'srcX', 'srcY', 'srcZ', 'dstName', 'dstTarget', 'dstLevel', 'dstX', 'dstY', 'dstZ', 'srcWidth', 'srcHeight', 'srcDepth', api='gles3')
def glCopyImageSubData(srcName, srcTarget, srcLevel, srcX, srcY, srcZ, dstName, dstTarget, dstLevel, dstX, dstY, dstZ, srcWidth, srcHeight, srcDepth):
	pass


@params('bindingindex', 'buffer', 'offset', 'stride', api='gles3')
def glBindVertexBuffer(bindingindex, buffer, offset, stride):
	pass


@params('source', 'type', 'id', 'severity', 'length', 'buf', api='gles3')
def glDebugMessageInsert(source, type, id, severity, length, buf):
	pass


@params('sampler', api='gles3')
def glIsSampler(sampler):
	pass


@params('target', api='gles3')
def glCheckFramebufferStatus(target):
	pass


@params('unit', 'texture', 'level', 'layered', 'layer', 'access', 'format', api='gles3')
def glBindImageTexture(unit, texture, level, layered, layer, access, format):
	pass


@params('program', 'count', 'constvaryings', 'bufferMode', api='gles3')
def glTransformFeedbackVaryings(program, count, constvaryings, bufferMode):
	pass


@params('mode', 'start', 'end', 'count', 'type', 'indices', api='gles3')
def glDrawRangeElements(mode, start, end, count, type, indices):
	pass


@params('target', 'index', 'buffer', api='gles3')
def glBindBufferBase(target, index, buffer):
	pass


@params('attribindex', 'size', 'type', 'relativeoffset', api='gles3')
def glVertexAttribIFormat(attribindex, size, type, relativeoffset):
	pass


@params('target', 'id', api='gles3')
def glBeginQuery(target, id):
	pass


@params('location', 'count', 'transpose', 'value', api='gles3')
def glUniformMatrix2x4fv(location, count, transpose, value):
	pass


@params(api = 'gles3')
def glGetError():
	pass


@params('target', 'level', 'pname', 'params', api='gles3')
def glGetTexLevelParameterfv(target, level, pname):
	pass


@params('program', 'location', 'v0', 'v1', api='gles3')
def glProgramUniform2ui(program, location, v0, v1):
	pass


@params('program', 'location', 'v0', 'v1', 'v2', 'v3', api='gles3')
def glProgramUniform4ui(program, location, v0, v1, v2, v3):
	pass


@params('pname', 'param', api='gles3')
def glPixelStorei(pname, param):
	pass


@params('flag', api='gles3')
def glDepthMask(flag):
	pass


@params('target', 'internalformat', 'buffer', 'offset', 'size', api='gles3')
def glTexBufferRange(target, internalformat, buffer, offset, size):
	pass


@params('program', 'pname', 'value', api='gles3')
def glProgramParameteri(program, pname, value):
	pass


@params('barriers', api='gles3')
def glMemoryBarrierByRegion(barriers):
	pass


@params('type', api='gles3')
def glCreateShader(type):
	pass


@params('n', 'renderbuffers', api='gles3')
def glGenRenderbuffers(n):
	pass


@params('target', 'level', 'xoffset', 'yoffset', 'x', 'y', 'width', 'height', api='gles3')
def glCopyTexSubImage2D(target, level, xoffset, yoffset, x, y, width, height):
	pass


@params('sfactorRGB', 'dfactorRGB', 'sfactorAlpha', 'dfactorAlpha', api='gles3')
def glBlendFuncSeparate(sfactorRGB, dfactorRGB, sfactorAlpha, dfactorAlpha):
	pass


@params('pipeline', 'bufSize', 'length', 'infoLog', api='gles3')
def glGetProgramPipelineInfoLog(pipeline, bufSize):
	pass


@params('sync', 'flags', 'timeout', api='gles3')
def glWaitSync(sync, flags, timeout):
	pass


@params('buf', 'modeRGB', 'modeAlpha', api='gles3')
def glBlendEquationSeparatei(buf, modeRGB, modeAlpha):
	pass


@params('location', 'v0', 'v1', 'v2', api='gles3')
def glUniform3f(location, v0, v1, v2):
	pass


@params('program', 'location', 'count', 'value', api='gles3')
def glProgramUniform3uiv(program, location, count, value):
	pass


@params('n', 'framebuffers', api='gles3')
def glDeleteFramebuffers(n, framebuffers):
	pass


@params('mode', 'first', 'count', api='gles3')
def glDrawArrays(mode, first, count):
	pass


@params('mask', api='gles3')
def glClear(mask):
	pass


@params('sampler', 'pname', 'params', api='gles3')
def glGetSamplerParameterfv(sampler, pname):
	pass


@params('sampler', 'pname', 'param', api='gles3')
def glSamplerParameterIiv(sampler, pname, param):
	pass


@params('mode', 'type', 'indirect', api='gles3')
def glDrawElementsIndirect(mode, type, indirect):
	pass


@params('program', 'uniformCount', 'constuniformNames', 'uniformIndices', api='gles3')
def glGetUniformIndices(program, uniformCount, constuniformNames, uniformIndices):
	pass


@params('array', api='gles3')
def glIsVertexArray(array):
	pass


@params('index', api='gles3')
def glDisableVertexAttribArray(index):
	pass


@params('program', 'programInterface', 'pname', 'params', api='gles3')
def glGetProgramInterfaceiv(program, programInterface, pname):
	pass


@params('index', 'pname', 'params', api='gles3')
def glGetVertexAttribIiv(index, pname):
	pass


@params('pname', 'value', api='gles3')
def glPatchParameteri(pname, value):
	pass


@params('value', 'invert', api='gles3')
def glSampleCoverage(value, invert):
	pass


@params('location', 'v0', 'v1', api='gles3')
def glUniform2i(location, v0, v1):
	pass


@params('target', 'attachment', 'texture', 'level', 'layer', api='gles3')
def glFramebufferTextureLayer(target, attachment, texture, level, layer):
	pass


@params('program', 'location', 'count', 'value', api='gles3')
def glProgramUniform2fv(program, location, count, value):
	pass


@params('minX', 'minY', 'minZ', 'minW', 'maxX', 'maxY', 'maxZ', 'maxW', api='gles3')
def glPrimitiveBoundingBox(minX, minY, minZ, minW, maxX, maxY, maxZ, maxW):
	pass


@params('target', 'index', 'data', api='gles3')
def glGetInteger64i_v(target, index):
	pass


@params('srcX0', 'srcY0', 'srcX1', 'srcY1', 'dstX0', 'dstY0', 'dstX1', 'dstY1', 'mask', 'filter', api='gles3')
def glBlitFramebuffer(srcX0, srcY0, srcX1, srcY1, dstX0, dstY0, dstX1, dstY1, mask, filter):
	pass


@params('target', 'index', api='gles3')
def glIsEnabledi(target, index):
	pass


@params('ptr', 'length', 'label', api='gles3')
def glObjectPtrLabel(ptr, length, label):
	pass


@params('count', 'bufSize', 'sources', 'types', 'ids', 'severities', 'lengths', 'messageLog', api='gles3')
def glGetDebugMessageLog(bufSize, sources, types, ids, severities, lengths, messageLog):
	pass


@params('source', 'id', 'length', 'message', api='gles3')
def glPushDebugGroup(source, id, length, message):
	pass


@params('target', 'level', 'xoffset', 'yoffset', 'zoffset', 'x', 'y', 'width', 'height', api='gles3')
def glCopyTexSubImage3D(target, level, xoffset, yoffset, zoffset, x, y, width, height):
	pass


@params('program', 'uniformBlockIndex', 'bufSize', 'length', 'uniformBlockName', api='gles3')
def glGetActiveUniformBlockName(program, uniformBlockIndex, bufSize, uniformBlockName):
	pass


@params('program', 'location', 'v0', 'v1', api='gles3')
def glProgramUniform2f(program, location, v0, v1):
	pass


@params('array', api='gles3')
def glBindVertexArray(array):
	pass


@params('target', 'framebuffer', api='gles3')
def glBindFramebuffer(target, framebuffer):
	pass


@params('x', 'y', 'width', 'height', api='gles3')
def glViewport(x, y, width, height):
	pass


@params('renderbuffer', api='gles3')
def glIsRenderbuffer(renderbuffer):
	pass


@params('target', 'samples', 'internalformat', 'width', 'height', 'fixedsamplelocations', api='gles3')
def glTexStorage2DMultisample(target, samples, internalformat, width, height, fixedsamplelocations):
	pass


@params('target', 'internalformat', 'buffer', api='gles3')
def glTexBuffer(target, internalformat, buffer):
	pass


@params('program', api='gles3')
def glValidateProgram(program):
	pass


@params('pipeline', 'program', api='gles3')
def glActiveShaderProgram(pipeline, program):
	pass


@params('target', 'texture', api='gles3')
def glBindTexture(target, texture):
	pass


@params('program', 'shader', api='gles3')
def glDetachShader(program, shader):
	pass


@params('program', 'programInterface', 'name', api='gles3')
def glGetProgramResourceLocation(program, programInterface, name):
	pass


@params('mode', 'count', 'type', 'indices', 'basevertex', api='gles3')
def glDrawElementsBaseVertex(mode, count, type, indices, basevertex):
	pass


@params('program', 'location', 'params', api='gles3')
def glGetUniformiv(program, location):
	pass


@params('target', 'buffer', api='gles3')
def glBindBuffer(target, buffer):
	pass


@params('location', 'v0', 'v1', 'v2', 'v3', api='gles3')
def glUniform4ui(location, v0, v1, v2, v3):
	pass


@params('type', 'count', 'conststrings', api='gles3')
def glCreateShaderProgramv(type, count, conststrings):
	pass


@params('target', api='gles3')
def glGenerateMipmap(target):
	pass


@params('target', api='gles3')
def glUnmapBuffer(target):
	pass


@params(api = 'gles3')
def glReleaseShaderCompiler():
	pass


@params('x', 'y', 'width', 'height', 'format', 'type', 'pixels', api='gles3')
def glReadPixels(x, y, width, height, format, type, pixels):
	pass


@params('pipeline', 'stages', 'program', api='gles3')
def glUseProgramStages(pipeline, stages, program):
	pass


@params('src', api='gles3')
def glReadBuffer(src):
	pass


@params('program', 'location', 'bufSize', 'params', api='gles3')
def glGetnUniformuiv(program, location, bufSize):
	pass


@params('n', 'buffers', api='gles3')
def glGenBuffers(n):
	pass


@params('framebuffer', api='gles3')
def glIsFramebuffer(framebuffer):
	pass


@params('target', 'pname', 'params', api='gles3')
def glGetBufferParameteri64v(target, pname):
	pass


@params('func', api='gles3')
def glDepthFunc(func):
	pass


@params('sampler', 'pname', 'param', api='gles3')
def glSamplerParameterf(sampler, pname, param):
	pass


@params('buf', 'src', 'dst', api='gles3')
def glBlendFunci(buf, src, dst):
	pass


@params('program', 'name', api='gles3')
def glGetUniformLocation(program, name):
	pass


@params('location', 'count', 'value', api='gles3')
def glUniform4fv(location, count, value):
	pass


@params('program', 'location', 'count', 'value', api='gles3')
def glProgramUniform2uiv(program, location, count, value):
	pass


@params('id', 'pname', 'params', api='gles3')
def glGetQueryObjectuiv(id, pname):
	pass


@params('program', 'location', 'count', 'value', api='gles3')
def glProgramUniform1uiv(program, location, count, value):
	pass


@params('target', 'attachment', 'texture', 'level', api='gles3')
def glFramebufferTexture(target, attachment, texture, level):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gles3')
def glProgramUniformMatrix2x4fv(program, location, count, transpose, value):
	pass


@params('pname', 'data', api='gles3')
def glGetFloatv(pname):
	pass


@params('pname', 'data', api='gles3')
def glGetIntegerv(pname):
	pass


@params('id', api='gles3')
def glIsQuery(id):
	pass


@params('target', 'level', 'internalformat', 'width', 'height', 'border', 'format', 'type', 'pixels', api='gles3')
def glTexImage2D(target, level, internalformat, width, height, border, format, type, pixels):
	pass


@params('target', 'pname', 'params', api='gles3')
def glGetFramebufferParameteriv(target, pname):
	pass


@params('sampler', 'pname', 'params', api='gles3')
def glGetSamplerParameteriv(sampler, pname):
	pass


@params('readTarget', 'writeTarget', 'readOffset', 'writeOffset', 'size', api='gles3')
def glCopyBufferSubData(readTarget, writeTarget, readOffset, writeOffset, size):
	pass


@params('program', 'index', 'bufSize', 'length', 'size', 'type', 'name', api='gles3')
def glGetActiveUniform(program, index, bufSize, name):
	pass


@params('value', api='gles3')
def glMinSampleShading(value):
	pass


@params('target', 'attachment', 'renderbuffertarget', 'renderbuffer', api='gles3')
def glFramebufferRenderbuffer(target, attachment, renderbuffertarget, renderbuffer):
	pass


@params('unit', 'sampler', api='gles3')
def glBindSampler(unit, sampler):
	pass


@params('width', api='gles3')
def glLineWidth(width):
	pass


@params('target', 'index', 'data', api='gles3')
def glGetIntegeri_v(target, index):
	pass


@params('program', 'index', 'bufSize', 'length', 'size', 'type', 'name', api='gles3')
def glGetTransformFeedbackVarying(program, index, bufSize, name):
	pass


@params('n', 'f', api='gles3')
def glDepthRangef(n, f):
	pass


@params('target', 'index', api='gles3')
def glEnablei(target, index):
	pass


@params('maskNumber', 'mask', api='gles3')
def glSampleMaski(maskNumber, mask):
	pass


@params('location', 'count', 'transpose', 'value', api='gles3')
def glUniformMatrix3x2fv(location, count, transpose, value):
	pass


@params('target', 'internalformat', 'pname', 'bufSize', 'params', api='gles3')
def glGetInternalformativ(target, internalformat, pname, bufSize):
	pass


@params('program', 'location', 'v0', api='gles3')
def glProgramUniform1ui(program, location, v0):
	pass


@params('index', 'r', 'g', 'b', 'a', api='gles3')
def glColorMaski(index, r, g, b, a):
	pass


@params('target', 'levels', 'internalformat', 'width', 'height', 'depth', api='gles3')
def glTexStorage3D(target, levels, internalformat, width, height, depth):
	pass


@params('location', 'count', 'transpose', 'value', api='gles3')
def glUniformMatrix3x4fv(location, count, transpose, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gles3')
def glProgramUniformMatrix4x3fv(program, location, count, transpose, value):
	pass


@params('target', 'attachment', 'pname', 'params', api='gles3')
def glGetFramebufferAttachmentParameteriv(target, attachment, pname):
	pass


@params('target', 'pname', 'params', api='gles3')
def glTexParameteriv(target, pname, params):
	pass


@params('program', 'location', 'count', 'value', api='gles3')
def glProgramUniform2iv(program, location, count, value):
	pass


@params('target', 'pname', 'params', api='gles3')
def glGetQueryiv(target, pname):
	pass


@params('identifier', 'name', 'length', 'label', api='gles3')
def glObjectLabel(identifier, name, length, label):
	pass


@params('buffer', 'drawbuffer', 'value', api='gles3')
def glClearBufferuiv(buffer, drawbuffer, value):
	pass


@params('index', 'size', 'type', 'stride', 'pointer', api='gles3')
def glVertexAttribIPointer(index, size, type, stride, pointer):
	pass


@params(api = 'gles3')
def glFlush():
	pass


@params('target', 'level', 'pname', 'params', api='gles3')
def glGetTexLevelParameteriv(target, level, pname):
	pass


@params('target', 'samples', 'internalformat', 'width', 'height', 'depth', 'fixedsamplelocations', api='gles3')
def glTexStorage3DMultisample(target, samples, internalformat, width, height, depth, fixedsamplelocations):
	pass


@params('s', api='gles3')
def glClearStencil(s):
	pass


@params('texture', api='gles3')
def glIsTexture(texture):
	pass


@params('factor', 'units', api='gles3')
def glPolygonOffset(factor, units):
	pass


@params('target', 'level', 'internalformat', 'width', 'height', 'depth', 'border', 'format', 'type', 'pixels', api='gles3')
def glTexImage3D(target, level, internalformat, width, height, depth, border, format, type, pixels):
	pass


@params('program', 'pname', 'params', api='gles3')
def glGetProgramiv(program, pname):
	pass


@params('program', 'location', 'count', 'value', api='gles3')
def glProgramUniform4fv(program, location, count, value):
	pass


@params(api = 'gles3')
def glBlendBarrier():
	pass


@params('target', 'offset', 'length', api='gles3')
def glFlushMappedBufferRange(target, offset, length):
	pass


@params('target', 'levels', 'internalformat', 'width', 'height', api='gles3')
def glTexStorage2D(target, levels, internalformat, width, height):
	pass


@params('n', 'ids', api='gles3')
def glGenQueries(n, ids):
	pass


@params('target', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth', 'format', 'type', 'pixels', api='gles3')
def glTexSubImage3D(target, level, xoffset, yoffset, zoffset, width, height, depth, format, type, pixels):
	pass


@params('count', 'samplers', api='gles3')
def glDeleteSamplers(count, samplers):
	pass


@params('location', 'count', 'value', api='gles3')
def glUniform3fv(location, count, value):
	pass


@params('n', 'bufs', api='gles3')
def glDrawBuffers(n, bufs):
	pass


@params('target', 'id', api='gles3')
def glBindTransformFeedback(target, id):
	pass


@params('location', 'count', 'value', api='gles3')
def glUniform2uiv(location, count, value):
	pass


@params(api = 'gles3')
def glFinish():
	pass


@params('location', 'count', 'value', api='gles3')
def glUniform1uiv(location, count, value):
	pass


@params('n', 'ids', api='gles3')
def glDeleteQueries(n, ids):
	pass


@params('index', 'pname', 'params', api='gles3')
def glGetVertexAttribfv(index, pname):
	pass


@params('num_groups_x', 'num_groups_y', 'num_groups_z', api='gles3')
def glDispatchCompute(num_groups_x, num_groups_y, num_groups_z):
	pass


@params('program', 'index', 'bufSize', 'length', 'size', 'type', 'name', api='gles3')
def glGetActiveAttrib(program, index, bufSize, name):
	pass


@params('location', 'v0', 'v1', 'v2', api='gles3')
def glUniform3i(location, v0, v1, v2):
	pass


@params('target', 'level', 'xoffset', 'yoffset', 'width', 'height', 'format', 'type', 'pixels', api='gles3')
def glTexSubImage2D(target, level, xoffset, yoffset, width, height, format, type, pixels):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gles3')
def glProgramUniformMatrix3x4fv(program, location, count, transpose, value):
	pass


@params('location', 'v0', 'v1', 'v2', api='gles3')
def glUniform3ui(location, v0, v1, v2):
	pass


@params('count', 'shaders', 'binaryformat', 'binary', 'length', api='gles3')
def glShaderBinary(count, shaders, binaryformat, binary, length):
	pass


@params('mode', 'count', 'type', 'indices', api='gles3')
def glDrawElements(mode, count, type, indices):
	pass


@params('program', 'location', 'count', 'value', api='gles3')
def glProgramUniform4iv(program, location, count, value):
	pass


@params('location', 'count', 'value', api='gles3')
def glUniform1iv(location, count, value):
	pass


@params('mode', 'first', 'count', 'instancecount', api='gles3')
def glDrawArraysInstanced(mode, first, count, instancecount):
	pass


@params('program', 'location', 'count', 'value', api='gles3')
def glProgramUniform1iv(program, location, count, value):
	pass


@params('target', 'renderbuffer', api='gles3')
def glBindRenderbuffer(target, renderbuffer):
	pass


@params('program', api='gles3')
def glIsProgram(program):
	pass


@params('index', 'v', api='gles3')
def glVertexAttrib4fv(index, v):
	pass


@params('index', 'v', api='gles3')
def glVertexAttrib2fv(index, v):
	pass


@params('program', 'location', 'v0', 'v1', 'v2', api='gles3')
def glProgramUniform3i(program, location, v0, v1, v2):
	pass


@params('pname', 'data', api='gles3')
def glGetInteger64v(pname):
	pass


@params('buffer', 'drawbuffer', 'value', api='gles3')
def glClearBufferiv(buffer, drawbuffer, value):
	pass


@params('sampler', 'pname', 'params', api='gles3')
def glGetSamplerParameterIuiv(sampler, pname):
	pass


@params('location', 'v0', 'v1', api='gles3')
def glUniform2f(location, v0, v1):
	pass


@params('d', api='gles3')
def glClearDepthf(d):
	pass


@params('index', 'x', 'y', 'z', 'w', api='gles3')
def glVertexAttribI4ui(index, x, y, z, w):
	pass


@params('red', 'green', 'blue', 'alpha', api='gles3')
def glColorMask(red, green, blue, alpha):
	pass


@params('mode', api='gles3')
def glBlendEquation(mode):
	pass


@params('program', 'programInterface', 'index', 'propCount', 'props', 'bufSize', 'length', 'params', api='gles3')
def glGetProgramResourceiv(program, programInterface, index, props, bufSize):
	pass


@params('primitiveMode', api='gles3')
def glBeginTransformFeedback(primitiveMode):
	pass


@params('n', 'ids', api='gles3')
def glDeleteTransformFeedbacks(n, ids):
	pass


@params('mode', 'start', 'end', 'count', 'type', 'indices', 'basevertex', api='gles3')
def glDrawRangeElementsBaseVertex(mode, start, end, count, type, indices, basevertex):
	pass


@params('program', 'index', 'name', api='gles3')
def glBindAttribLocation(program, index, name):
	pass


@params('buf', 'srcRGB', 'dstRGB', 'srcAlpha', 'dstAlpha', api='gles3')
def glBlendFuncSeparatei(buf, srcRGB, dstRGB, srcAlpha, dstAlpha):
	pass


@params('location', 'v0', 'v1', api='gles3')
def glUniform2ui(location, v0, v1):
	pass


@params('target', 'index', api='gles3')
def glDisablei(target, index):
	pass


@params('sync', 'pname', 'bufSize', 'length', 'values', api='gles3')
def glGetSynciv(sync, pname, bufSize, values):
	pass


@params('program', 'location', 'v0', 'v1', api='gles3')
def glProgramUniform2i(program, location, v0, v1):
	pass


@params('program', 'bufSize', 'length', 'binaryFormat', 'binary', api='gles3')
def glGetProgramBinary(program, bufSize, binaryFormat):
	pass


@params(api = 'gles3')
def glPauseTransformFeedback():
	pass


@params('index', 'v', api='gles3')
def glVertexAttribI4iv(index, v):
	pass


@params('target', 'pname', 'params', api='gles3')
def glTexParameterfv(target, pname, params):
	pass


@params('face', 'func', 'ref', 'mask', api='gles3')
def glStencilFuncSeparate(face, func, ref, mask):
	pass


@params('program', 'location', 'count', 'value', api='gles3')
def glProgramUniform3fv(program, location, count, value):
	pass


@params('program', 'location', 'count', 'value', api='gles3')
def glProgramUniform1fv(program, location, count, value):
	pass


@params('location', 'count', 'transpose', 'value', api='gles3')
def glUniformMatrix4fv(location, count, transpose, value):
	pass


@params('n', 'pipelines', api='gles3')
def glDeleteProgramPipelines(n, pipelines):
	pass


@params('shader', api='gles3')
def glCompileShader(shader):
	pass


@params('target', 'numAttachments', 'attachments', api='gles3')
def glInvalidateFramebuffer(target, numAttachments, attachments):
	pass


@params('target', 'level', 'internalformat', 'width', 'height', 'border', 'imageSize', 'data', api='gles3')
def glCompressedTexImage2D(target, level, internalformat, width, height, border, imageSize, data):
	pass


@params('index', 'x', api='gles3')
def glVertexAttrib1f(index, x):
	pass


@params('program', api='gles3')
def glDeleteProgram(program):
	pass


@params('location', 'count', 'transpose', 'value', api='gles3')
def glUniformMatrix4x3fv(location, count, transpose, value):
	pass


@params('buffer', 'drawbuffer', 'value', api='gles3')
def glClearBufferfv(buffer, drawbuffer, value):
	pass


@params('buffer', 'drawbuffer', 'depth', 'stencil', api='gles3')
def glClearBufferfi(buffer, drawbuffer, depth, stencil):
	pass


@params('mode', 'indirect', api='gles3')
def glDrawArraysIndirect(mode, indirect):
	pass


@params('n', 'arrays', api='gles3')
def glGenVertexArrays(n):
	pass


@params('bindingindex', 'divisor', api='gles3')
def glVertexBindingDivisor(bindingindex, divisor):
	pass


@params('sampler', 'pname', 'params', api='gles3')
def glGetSamplerParameterIiv(sampler, pname):
	pass


@params('location', 'count', 'transpose', 'value', api='gles3')
def glUniformMatrix4x2fv(location, count, transpose, value):
	pass


@params('index', 'x', 'y', 'z', api='gles3')
def glVertexAttrib3f(index, x, y, z):
	pass


@params('location', 'v0', api='gles3')
def glUniform1ui(location, v0):
	pass


@params('barriers', api='gles3')
def glMemoryBarrier(barriers):
	pass


@params('program', 'name', api='gles3')
def glGetFragDataLocation(program, name):
	pass


@params('shader', api='gles3')
def glIsShader(shader):
	pass


@params('cap', api='gles3')
def glEnable(cap):
	pass


@params('program', 'uniformCount', 'uniformIndices', 'pname', 'params', api='gles3')
def glGetActiveUniformsiv(program, uniformCount, uniformIndices, pname):
	pass


@params('buf', 'mode', api='gles3')
def glBlendEquationi(buf, mode):
	pass


@params('program', 'name', api='gles3')
def glGetAttribLocation(program, name):
	pass


@params('program', 'location', 'v0', 'v1', 'v2', api='gles3')
def glProgramUniform3ui(program, location, v0, v1, v2):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gles3')
def glProgramUniformMatrix2x3fv(program, location, count, transpose, value):
	pass


@params('program', 'location', 'v0', api='gles3')
def glProgramUniform1i(program, location, v0):
	pass


@params('program', 'location', 'v0', api='gles3')
def glProgramUniform1f(program, location, v0):
	pass


@params('program', 'location', 'count', 'value', api='gles3')
def glProgramUniform3iv(program, location, count, value):
	pass


@params('location', 'count', 'value', api='gles3')
def glUniform4iv(location, count, value):
	pass


@params('n', 'textures', api='gles3')
def glGenTextures(n):
	pass


@params('index', 'size', 'type', 'normalized', 'stride', 'pointer', api='gles3')
def glVertexAttribPointer(index, size, type, normalized, stride, pointer):
	pass


@params('location', 'v0', api='gles3')
def glUniform1f(location, v0):
	pass


@params('location', 'count', 'value', api='gles3')
def glUniform2iv(location, count, value):
	pass


@params('shader', 'pname', 'params', api='gles3')
def glGetShaderiv(shader, pname):
	pass


@params('target', 'level', 'internalformat', 'width', 'height', 'depth', 'border', 'imageSize', 'data', api='gles3')
def glCompressedTexImage3D(target, level, internalformat, width, height, depth, border, imageSize, data):
	pass


@params('index', 'pname', 'params', api='gles3')
def glGetVertexAttribiv(index, pname):
	pass


@params('location', 'count', 'transpose', 'value', api='gles3')
def glUniformMatrix2fv(location, count, transpose, value):
	pass


@params('target', 'pname', 'params', api='gles3')
def glGetTexParameterIiv(target, pname):
	pass


@params('callback', 'userParam', api='gles3')
def glDebugMessageCallback(callback, userParam):
	pass


@params('target', 'index', 'data', api='gles3')
def glGetBooleani_v(target, index):
	pass


@params('target', 'mode', api='gles3')
def glHint(target, mode):
	pass


@params('program', 'programInterface', 'index', 'bufSize', 'length', 'name', api='gles3')
def glGetProgramResourceName(program, programInterface, index, bufSize, name):
	pass


@params('face', 'sfail', 'dpfail', 'dppass', api='gles3')
def glStencilOpSeparate(face, sfail, dpfail, dppass):
	pass


@params('target', 'pname', 'params', api='gles3')
def glGetTexParameteriv(target, pname):
	pass


@params('index', 'pname', 'pointer', api='gles3')
def glGetVertexAttribPointerv(index, pname):
	pass


@params('cap', api='gles3')
def glDisable(cap):
	pass


@params('program', 'location', 'count', 'value', api='gles3')
def glProgramUniform4uiv(program, location, count, value):
	pass


@params('location', 'count', 'value', api='gles3')
def glUniform3uiv(location, count, value):
	pass


@params('red', 'green', 'blue', 'alpha', api='gles3')
def glBlendColor(red, green, blue, alpha):
	pass


@params('sampler', 'pname', 'param', api='gles3')
def glSamplerParameterIuiv(sampler, pname, param):
	pass


@params('location', 'v0', 'v1', 'v2', 'v3', api='gles3')
def glUniform4i(location, v0, v1, v2, v3):
	pass


@params('texture', api='gles3')
def glActiveTexture(texture):
	pass


@params('index', api='gles3')
def glEnableVertexAttribArray(index):
	pass


@params('location', 'v0', 'v1', 'v2', 'v3', api='gles3')
def glUniform4f(location, v0, v1, v2, v3):
	pass


@params('target', 'samples', 'internalformat', 'width', 'height', api='gles3')
def glRenderbufferStorageMultisample(target, samples, internalformat, width, height):
	pass


@params('mode', 'count', 'type', 'indices', 'instancecount', 'basevertex', api='gles3')
def glDrawElementsInstancedBaseVertex(mode, count, type, indices, instancecount, basevertex):
	pass


@params(api = 'gles3')
def glPopDebugGroup():
	pass


@params('program', 'uniformBlockIndex', 'uniformBlockBinding', api='gles3')
def glUniformBlockBinding(program, uniformBlockIndex, uniformBlockBinding):
	pass


@params('target', 'offset', 'size', 'data', api='gles3')
def glBufferSubData(target, offset, size, data):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gles3')
def glProgramUniformMatrix3x2fv(program, location, count, transpose, value):
	pass


@params('sfactor', 'dfactor', api='gles3')
def glBlendFunc(sfactor, dfactor):
	pass


@params(api = 'gles3')
def glCreateProgram():
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gles3')
def glProgramUniformMatrix2fv(program, location, count, transpose, value):
	pass


@params('sampler', 'pname', 'param', api='gles3')
def glSamplerParameteriv(sampler, pname, param):
	pass


@params('red', 'green', 'blue', 'alpha', api='gles3')
def glClearColor(red, green, blue, alpha):
	pass


@params('program', 'location', 'bufSize', 'params', api='gles3')
def glGetnUniformiv(program, location, bufSize):
	pass


@params('mask', api='gles3')
def glStencilMask(mask):
	pass


@params('index', 'v', api='gles3')
def glVertexAttribI4uiv(index, v):
	pass


@params('program', 'programInterface', 'name', api='gles3')
def glGetProgramResourceIndex(program, programInterface, name):
	pass


@params('location', 'count', 'transpose', 'value', api='gles3')
def glUniformMatrix2x3fv(location, count, transpose, value):
	pass


@params('n', 'ids', api='gles3')
def glGenTransformFeedbacks(n, ids):
	pass


@params('index', 'pname', 'params', api='gles3')
def glGetVertexAttribIuiv(index, pname):
	pass


@params('target', 'level', 'xoffset', 'yoffset', 'width', 'height', 'format', 'imageSize', 'data', api='gles3')
def glCompressedTexSubImage2D(target, level, xoffset, yoffset, width, height, format, imageSize, data):
	pass


@params('program', 'binaryFormat', 'binary', 'length', api='gles3')
def glProgramBinary(program, binaryFormat, binary, length):
	pass


@params('target', 'pname', 'params', api='gles3')
def glGetTexParameterfv(target, pname):
	pass


@params('target', 'pname', 'params', api='gles3')
def glTexParameterIiv(target, pname, params):
	pass


@params(api = 'gles3')
def glEndTransformFeedback():
	pass


@params('index', 'divisor', api='gles3')
def glVertexAttribDivisor(index, divisor):
	pass


@params('target', 'offset', 'length', 'access', api='gles3')
def glMapBufferRange(target, offset, length, access):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gles3')
def glProgramUniformMatrix4x2fv(program, location, count, transpose, value):
	pass


@params('shadertype', 'precisiontype', 'range', 'precision', api='gles3')
def glGetShaderPrecisionFormat(shadertype, precisiontype):
	pass


@params('shader', 'count', 'conststring', 'length', api='gles3')
def glShaderSource(shader, count, conststring, length):
	pass


@params('n', 'renderbuffers', api='gles3')
def glDeleteRenderbuffers(n, renderbuffers):
	pass


@params('target', 'size', 'data', 'usage', api='gles3')
def glBufferData(target, size, data, usage):
	pass


@params('target', 'attachment', 'textarget', 'texture', 'level', api='gles3')
def glFramebufferTexture2D(target, attachment, textarget, texture, level):
	pass


@params('target', 'pname', 'params', api='gles3')
def glGetBufferPointerv(target, pname):
	pass


@params('sampler', 'pname', 'param', api='gles3')
def glSamplerParameterfv(sampler, pname, param):
	pass


@params('location', 'count', 'value', api='gles3')
def glUniform1fv(location, count, value):
	pass


@params('index', 'x', 'y', api='gles3')
def glVertexAttrib2f(index, x, y):
	pass


@params('program', 'uniformBlockName', api='gles3')
def glGetUniformBlockIndex(program, uniformBlockName):
	pass


@params('mode', api='gles3')
def glFrontFace(mode):
	pass


