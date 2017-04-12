from OpenGLCffi.GLES3 import params
@params(api='gles3', prms=['face', 'mask'])
def glStencilMaskSeparate(face, mask):
	pass


@params(api='gles3', prms=['target', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth', 'format', 'imageSize', 'data'])
def glCompressedTexSubImage3D(target, level, xoffset, yoffset, zoffset, width, height, depth, format, imageSize, data):
	pass


@params(api='gles3', prms=['buffer'])
def glIsBuffer(buffer):
	pass


@params(api='gles3', prms=['pname', 'index', 'val'])
def glGetMultisamplefv(pname, index):
	pass


@params(api='gles3', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix4fv(program, location, count, transpose, value):
	pass


@params(api='gles3', prms=['source', 'type', 'severity', 'count', 'ids', 'enabled'])
def glDebugMessageControl(source, type, severity, count, ids, enabled):
	pass


@params(api='gles3', prms=['target', 'internalformat', 'width', 'height'])
def glRenderbufferStorage(target, internalformat, width, height):
	pass


@params(api='gles3', prms=['program', 'location', 'v0', 'v1', 'v2'])
def glProgramUniform3f(program, location, v0, v1, v2):
	pass


@params(api='gles3', prms=[])
def glResumeTransformFeedback():
	pass


@params(api='gles3', prms=[])
def glGetGraphicsResetStatus():
	pass


@params(api='gles3', prms=['index', 'v'])
def glVertexAttrib1fv(index, v):
	pass


@params(api='gles3', prms=['cap'])
def glIsEnabled(cap):
	pass


@params(api='gles3', prms=['fail', 'zfail', 'zpass'])
def glStencilOp(fail, zfail, zpass):
	pass


@params(api='gles3', prms=['n', 'framebuffers'])
def glGenFramebuffers(n):
	pass


@params(api='gles3', prms=['program', 'maxCount', 'count', 'shaders'])
def glGetAttachedShaders(program, maxCount, count):
	pass


@params(api='gles3', prms=['n', 'arrays'])
def glDeleteVertexArrays(n, arrays):
	pass


@params(api='gles3', prms=['pname', 'params'])
def glGetPointerv(pname):
	pass


@params(api='gles3', prms=['program', 'location', 'params'])
def glGetUniformfv(program, location):
	pass


@params(api='gles3', prms=['program', 'location', 'params'])
def glGetUniformuiv(program, location):
	pass


@params(api='gles3', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix3fv(program, location, count, transpose, value):
	pass


@params(api='gles3', prms=['mode', 'count', 'type', 'indices', 'instancecount'])
def glDrawElementsInstanced(mode, count, type, indices, instancecount):
	pass


@params(api='gles3', prms=['target', 'pname', 'params'])
def glGetRenderbufferParameteriv(target, pname):
	pass


@params(api='gles3', prms=['condition', 'flags'])
def glFenceSync(condition, flags):
	pass


@params(api='gles3', prms=['pipeline'])
def glValidateProgramPipeline(pipeline):
	pass


@params(api='gles3', prms=['count', 'samplers'])
def glGenSamplers(count, samplers):
	pass


@params(api='gles3', prms=['target', 'pname', 'params'])
def glGetTexParameterIuiv(target, pname):
	pass


@params(api='gles3', prms=['sync'])
def glIsSync(sync):
	pass


@params(api='gles3', prms=['ptr', 'bufSize', 'length', 'label'])
def glGetObjectPtrLabel(ptr, bufSize, length):
	pass


@params(api='gles3', prms=['target', 'level', 'internalformat', 'x', 'y', 'width', 'height', 'border'])
def glCopyTexImage2D(target, level, internalformat, x, y, width, height, border):
	pass


@params(api='gles3', prms=['location', 'count', 'value'])
def glUniform4uiv(location, count, value):
	pass


@params(api='gles3', prms=['target', 'numAttachments', 'attachments', 'x', 'y', 'width', 'height'])
def glInvalidateSubFramebuffer(target, numAttachments, attachments, x, y, width, height):
	pass


@params(api='gles3', prms=['sync'])
def glDeleteSync(sync):
	pass


@params(api='gles3', prms=['location', 'count', 'value'])
def glUniform3iv(location, count, value):
	pass


@params(api='gles3', prms=['program'])
def glUseProgram(program):
	pass


@params(api='gles3', prms=['program', 'bufSize', 'length', 'infoLog'])
def glGetProgramInfoLog(program, bufSize, length):
	pass


@params(api='gles3', prms=['pname', 'data'])
def glGetBooleanv(pname):
	pass


@params(api='gles3', prms=['shader'])
def glDeleteShader(shader):
	pass


@params(api='gles3', prms=['attribindex', 'size', 'type', 'normalized', 'relativeoffset'])
def glVertexAttribFormat(attribindex, size, type, normalized, relativeoffset):
	pass


@params(api='gles3', prms=['target', 'pname', 'param'])
def glTexParameterf(target, pname, param):
	pass


@params(api='gles3', prms=['attribindex', 'bindingindex'])
def glVertexAttribBinding(attribindex, bindingindex):
	pass


@params(api='gles3', prms=['target', 'pname', 'param'])
def glTexParameteri(target, pname, param):
	pass


@params(api='gles3', prms=['shader', 'bufSize', 'length', 'source'])
def glGetShaderSource(shader, bufSize, length):
	pass


@params(api='gles3', prms=['n', 'pipelines'])
def glGenProgramPipelines(n, pipelines):
	pass


@params(api='gles3', prms=['index', 'v'])
def glVertexAttrib3fv(index, v):
	pass


@params(api='gles3', prms=['program'])
def glLinkProgram(program):
	pass


@params(api='gles3', prms=['identifier', 'name', 'bufSize', 'length', 'label'])
def glGetObjectLabel(identifier, name, bufSize, length):
	pass


@params(api='gles3', prms=['name'])
def glGetString(name):
	pass


@params(api='gles3', prms=['target'])
def glEndQuery(target):
	pass


@params(api='gles3', prms=['target', 'pname', 'param'])
def glFramebufferParameteri(target, pname, param):
	pass


@params(api='gles3', prms=['n', 'textures'])
def glDeleteTextures(n, textures):
	pass


@params(api='gles3', prms=['index', 'x', 'y', 'z', 'w'])
def glVertexAttrib4f(index, x, y, z, w):
	pass


@params(api='gles3', prms=['sampler', 'pname', 'param'])
def glSamplerParameteri(sampler, pname, param):
	pass


@params(api='gles3', prms=['program', 'uniformBlockIndex', 'pname', 'params'])
def glGetActiveUniformBlockiv(program, uniformBlockIndex, pname):
	pass


@params(api='gles3', prms=['location', 'v0'])
def glUniform1i(location, v0):
	pass


@params(api='gles3', prms=['mode'])
def glCullFace(mode):
	pass


@params(api='gles3', prms=['program', 'location', 'v0', 'v1', 'v2', 'v3'])
def glProgramUniform4i(program, location, v0, v1, v2, v3):
	pass


@params(api='gles3', prms=['program', 'location', 'v0', 'v1', 'v2', 'v3'])
def glProgramUniform4f(program, location, v0, v1, v2, v3):
	pass


@params(api='gles3', prms=['program', 'shader'])
def glAttachShader(program, shader):
	pass


@params(api='gles3', prms=['target', 'pname', 'params'])
def glGetBufferParameteriv(target, pname):
	pass


@params(api='gles3', prms=['target', 'pname', 'params'])
def glTexParameterIuiv(target, pname, params):
	pass


@params(api='gles3', prms=['id'])
def glIsTransformFeedback(id):
	pass


@params(api='gles3', prms=['pipeline'])
def glIsProgramPipeline(pipeline):
	pass


@params(api='gles3', prms=['location', 'count', 'transpose', 'value'])
def glUniformMatrix3fv(location, count, transpose, value):
	pass


@params(api='gles3', prms=['program', 'location', 'bufSize', 'params'])
def glGetnUniformfv(program, location, bufSize):
	pass


@params(api='gles3', prms=['func', 'ref', 'mask'])
def glStencilFunc(func, ref, mask):
	pass


@params(api='gles3', prms=['pipeline', 'pname', 'params'])
def glGetProgramPipelineiv(pipeline, pname):
	pass


@params(api='gles3', prms=['indirect'])
def glDispatchComputeIndirect(indirect):
	pass


@params(api='gles3', prms=['shader', 'bufSize', 'length', 'infoLog'])
def glGetShaderInfoLog(shader, bufSize, length):
	pass


@params(api='gles3', prms=['index', 'x', 'y', 'z', 'w'])
def glVertexAttribI4i(index, x, y, z, w):
	pass


@params(api='gles3', prms=['modeRGB', 'modeAlpha'])
def glBlendEquationSeparate(modeRGB, modeAlpha):
	pass


@params(api='gles3', prms=['n', 'buffers'])
def glDeleteBuffers(n, buffers):
	pass


@params(api='gles3', prms=['pipeline'])
def glBindProgramPipeline(pipeline):
	pass


@params(api='gles3', prms=['x', 'y', 'width', 'height'])
def glScissor(x, y, width, height):
	pass


@params(api='gles3', prms=['name', 'index'])
def glGetStringi(name, index):
	pass


@params(api='gles3', prms=['location', 'count', 'value'])
def glUniform2fv(location, count, value):
	pass


@params(api='gles3', prms=['target', 'index', 'buffer', 'offset', 'size'])
def glBindBufferRange(target, index, buffer, offset, size):
	pass


@params(api='gles3', prms=['sync', 'flags', 'timeout'])
def glClientWaitSync(sync, flags, timeout):
	pass


@params(api='gles3', prms=['x', 'y', 'width', 'height', 'format', 'type', 'bufSize', 'data'])
def glReadnPixels(x, y, width, height, format, type, bufSize, data):
	pass


@params(api='gles3', prms=['srcName', 'srcTarget', 'srcLevel', 'srcX', 'srcY', 'srcZ', 'dstName', 'dstTarget', 'dstLevel', 'dstX', 'dstY', 'dstZ', 'srcWidth', 'srcHeight', 'srcDepth'])
def glCopyImageSubData(srcName, srcTarget, srcLevel, srcX, srcY, srcZ, dstName, dstTarget, dstLevel, dstX, dstY, dstZ, srcWidth, srcHeight, srcDepth):
	pass


@params(api='gles3', prms=['bindingindex', 'buffer', 'offset', 'stride'])
def glBindVertexBuffer(bindingindex, buffer, offset, stride):
	pass


@params(api='gles3', prms=['source', 'type', 'id', 'severity', 'length', 'buf'])
def glDebugMessageInsert(source, type, id, severity, length, buf):
	pass


@params(api='gles3', prms=['sampler'])
def glIsSampler(sampler):
	pass


@params(api='gles3', prms=['target'])
def glCheckFramebufferStatus(target):
	pass


@params(api='gles3', prms=['unit', 'texture', 'level', 'layered', 'layer', 'access', 'format'])
def glBindImageTexture(unit, texture, level, layered, layer, access, format):
	pass


@params(api='gles3', prms=['program', 'count', 'constvaryings', 'bufferMode'])
def glTransformFeedbackVaryings(program, count, constvaryings, bufferMode):
	pass


@params(api='gles3', prms=['mode', 'start', 'end', 'count', 'type', 'indices'])
def glDrawRangeElements(mode, start, end, count, type, indices):
	pass


@params(api='gles3', prms=['target', 'index', 'buffer'])
def glBindBufferBase(target, index, buffer):
	pass


@params(api='gles3', prms=['attribindex', 'size', 'type', 'relativeoffset'])
def glVertexAttribIFormat(attribindex, size, type, relativeoffset):
	pass


@params(api='gles3', prms=['target', 'id'])
def glBeginQuery(target, id):
	pass


@params(api='gles3', prms=['location', 'count', 'transpose', 'value'])
def glUniformMatrix2x4fv(location, count, transpose, value):
	pass


@params(api='gles3', prms=[])
def glGetError():
	pass


@params(api='gles3', prms=['target', 'level', 'pname', 'params'])
def glGetTexLevelParameterfv(target, level, pname):
	pass


@params(api='gles3', prms=['program', 'location', 'v0', 'v1'])
def glProgramUniform2ui(program, location, v0, v1):
	pass


@params(api='gles3', prms=['program', 'location', 'v0', 'v1', 'v2', 'v3'])
def glProgramUniform4ui(program, location, v0, v1, v2, v3):
	pass


@params(api='gles3', prms=['pname', 'param'])
def glPixelStorei(pname, param):
	pass


@params(api='gles3', prms=['flag'])
def glDepthMask(flag):
	pass


@params(api='gles3', prms=['target', 'internalformat', 'buffer', 'offset', 'size'])
def glTexBufferRange(target, internalformat, buffer, offset, size):
	pass


@params(api='gles3', prms=['program', 'pname', 'value'])
def glProgramParameteri(program, pname, value):
	pass


@params(api='gles3', prms=['barriers'])
def glMemoryBarrierByRegion(barriers):
	pass


@params(api='gles3', prms=['type'])
def glCreateShader(type):
	pass


@params(api='gles3', prms=['n', 'renderbuffers'])
def glGenRenderbuffers(n):
	pass


@params(api='gles3', prms=['target', 'level', 'xoffset', 'yoffset', 'x', 'y', 'width', 'height'])
def glCopyTexSubImage2D(target, level, xoffset, yoffset, x, y, width, height):
	pass


@params(api='gles3', prms=['sfactorRGB', 'dfactorRGB', 'sfactorAlpha', 'dfactorAlpha'])
def glBlendFuncSeparate(sfactorRGB, dfactorRGB, sfactorAlpha, dfactorAlpha):
	pass


@params(api='gles3', prms=['pipeline', 'bufSize', 'length', 'infoLog'])
def glGetProgramPipelineInfoLog(pipeline, bufSize, length):
	pass


@params(api='gles3', prms=['sync', 'flags', 'timeout'])
def glWaitSync(sync, flags, timeout):
	pass


@params(api='gles3', prms=['buf', 'modeRGB', 'modeAlpha'])
def glBlendEquationSeparatei(buf, modeRGB, modeAlpha):
	pass


@params(api='gles3', prms=['location', 'v0', 'v1', 'v2'])
def glUniform3f(location, v0, v1, v2):
	pass


@params(api='gles3', prms=['program', 'location', 'count', 'value'])
def glProgramUniform3uiv(program, location, count, value):
	pass


@params(api='gles3', prms=['n', 'framebuffers'])
def glDeleteFramebuffers(n, framebuffers):
	pass


@params(api='gles3', prms=['mode', 'first', 'count'])
def glDrawArrays(mode, first, count):
	pass


@params(api='gles3', prms=['mask'])
def glClear(mask):
	pass


@params(api='gles3', prms=['sampler', 'pname', 'params'])
def glGetSamplerParameterfv(sampler, pname):
	pass


@params(api='gles3', prms=['sampler', 'pname', 'param'])
def glSamplerParameterIiv(sampler, pname, param):
	pass


@params(api='gles3', prms=['mode', 'type', 'indirect'])
def glDrawElementsIndirect(mode, type, indirect):
	pass


@params(api='gles3', prms=['program', 'uniformCount', 'constuniformNames', 'uniformIndices'])
def glGetUniformIndices(program, uniformCount, constuniformNames, uniformIndices):
	pass


@params(api='gles3', prms=['array'])
def glIsVertexArray(array):
	pass


@params(api='gles3', prms=['index'])
def glDisableVertexAttribArray(index):
	pass


@params(api='gles3', prms=['program', 'programInterface', 'pname', 'params'])
def glGetProgramInterfaceiv(program, programInterface, pname):
	pass


@params(api='gles3', prms=['index', 'pname', 'params'])
def glGetVertexAttribIiv(index, pname):
	pass


@params(api='gles3', prms=['pname', 'value'])
def glPatchParameteri(pname, value):
	pass


@params(api='gles3', prms=['value', 'invert'])
def glSampleCoverage(value, invert):
	pass


@params(api='gles3', prms=['location', 'v0', 'v1'])
def glUniform2i(location, v0, v1):
	pass


@params(api='gles3', prms=['target', 'attachment', 'texture', 'level', 'layer'])
def glFramebufferTextureLayer(target, attachment, texture, level, layer):
	pass


@params(api='gles3', prms=['program', 'location', 'count', 'value'])
def glProgramUniform2fv(program, location, count, value):
	pass


@params(api='gles3', prms=['minX', 'minY', 'minZ', 'minW', 'maxX', 'maxY', 'maxZ', 'maxW'])
def glPrimitiveBoundingBox(minX, minY, minZ, minW, maxX, maxY, maxZ, maxW):
	pass


@params(api='gles3', prms=['target', 'index', 'data'])
def glGetInteger64i_v(target, index):
	pass


@params(api='gles3', prms=['srcX0', 'srcY0', 'srcX1', 'srcY1', 'dstX0', 'dstY0', 'dstX1', 'dstY1', 'mask', 'filter'])
def glBlitFramebuffer(srcX0, srcY0, srcX1, srcY1, dstX0, dstY0, dstX1, dstY1, mask, filter):
	pass


@params(api='gles3', prms=['target', 'index'])
def glIsEnabledi(target, index):
	pass


@params(api='gles3', prms=['ptr', 'length', 'label'])
def glObjectPtrLabel(ptr, length, label):
	pass


@params(api='gles3', prms=['count', 'bufSize', 'sources', 'types', 'ids', 'severities', 'lengths', 'messageLog'])
def glGetDebugMessageLog(count, bufSize, sources, types, ids, severities, lengths, messageLog):
	pass


@params(api='gles3', prms=['source', 'id', 'length', 'message'])
def glPushDebugGroup(source, id, length, message):
	pass


@params(api='gles3', prms=['target', 'level', 'xoffset', 'yoffset', 'zoffset', 'x', 'y', 'width', 'height'])
def glCopyTexSubImage3D(target, level, xoffset, yoffset, zoffset, x, y, width, height):
	pass


@params(api='gles3', prms=['program', 'uniformBlockIndex', 'bufSize', 'length', 'uniformBlockName'])
def glGetActiveUniformBlockName(program, uniformBlockIndex, bufSize, length, uniformBlockName):
	pass


@params(api='gles3', prms=['program', 'location', 'v0', 'v1'])
def glProgramUniform2f(program, location, v0, v1):
	pass


@params(api='gles3', prms=['array'])
def glBindVertexArray(array):
	pass


@params(api='gles3', prms=['target', 'framebuffer'])
def glBindFramebuffer(target, framebuffer):
	pass


@params(api='gles3', prms=['x', 'y', 'width', 'height'])
def glViewport(x, y, width, height):
	pass


@params(api='gles3', prms=['renderbuffer'])
def glIsRenderbuffer(renderbuffer):
	pass


@params(api='gles3', prms=['target', 'samples', 'internalformat', 'width', 'height', 'fixedsamplelocations'])
def glTexStorage2DMultisample(target, samples, internalformat, width, height, fixedsamplelocations):
	pass


@params(api='gles3', prms=['target', 'internalformat', 'buffer'])
def glTexBuffer(target, internalformat, buffer):
	pass


@params(api='gles3', prms=['program'])
def glValidateProgram(program):
	pass


@params(api='gles3', prms=['pipeline', 'program'])
def glActiveShaderProgram(pipeline, program):
	pass


@params(api='gles3', prms=['target', 'texture'])
def glBindTexture(target, texture):
	pass


@params(api='gles3', prms=['program', 'shader'])
def glDetachShader(program, shader):
	pass


@params(api='gles3', prms=['program', 'programInterface', 'name'])
def glGetProgramResourceLocation(program, programInterface, name):
	pass


@params(api='gles3', prms=['mode', 'count', 'type', 'indices', 'basevertex'])
def glDrawElementsBaseVertex(mode, count, type, indices, basevertex):
	pass


@params(api='gles3', prms=['program', 'location', 'params'])
def glGetUniformiv(program, location):
	pass


@params(api='gles3', prms=['target', 'buffer'])
def glBindBuffer(target, buffer):
	pass


@params(api='gles3', prms=['location', 'v0', 'v1', 'v2', 'v3'])
def glUniform4ui(location, v0, v1, v2, v3):
	pass


@params(api='gles3', prms=['type', 'count', 'conststrings'])
def glCreateShaderProgramv(type, count, conststrings):
	pass


@params(api='gles3', prms=['target'])
def glGenerateMipmap(target):
	pass


@params(api='gles3', prms=['target'])
def glUnmapBuffer(target):
	pass


@params(api='gles3', prms=[])
def glReleaseShaderCompiler():
	pass


@params(api='gles3', prms=['x', 'y', 'width', 'height', 'format', 'type', 'pixels'])
def glReadPixels(x, y, width, height, format, type, pixels):
	pass


@params(api='gles3', prms=['pipeline', 'stages', 'program'])
def glUseProgramStages(pipeline, stages, program):
	pass


@params(api='gles3', prms=['src'])
def glReadBuffer(src):
	pass


@params(api='gles3', prms=['program', 'location', 'bufSize', 'params'])
def glGetnUniformuiv(program, location, bufSize):
	pass


@params(api='gles3', prms=['n', 'buffers'])
def glGenBuffers(n):
	pass


@params(api='gles3', prms=['framebuffer'])
def glIsFramebuffer(framebuffer):
	pass


@params(api='gles3', prms=['target', 'pname', 'params'])
def glGetBufferParameteri64v(target, pname):
	pass


@params(api='gles3', prms=['func'])
def glDepthFunc(func):
	pass


@params(api='gles3', prms=['sampler', 'pname', 'param'])
def glSamplerParameterf(sampler, pname, param):
	pass


@params(api='gles3', prms=['buf', 'src', 'dst'])
def glBlendFunci(buf, src, dst):
	pass


@params(api='gles3', prms=['program', 'name'])
def glGetUniformLocation(program, name):
	pass


@params(api='gles3', prms=['location', 'count', 'value'])
def glUniform4fv(location, count, value):
	pass


@params(api='gles3', prms=['program', 'location', 'count', 'value'])
def glProgramUniform2uiv(program, location, count, value):
	pass


@params(api='gles3', prms=['id', 'pname', 'params'])
def glGetQueryObjectuiv(id, pname):
	pass


@params(api='gles3', prms=['program', 'location', 'count', 'value'])
def glProgramUniform1uiv(program, location, count, value):
	pass


@params(api='gles3', prms=['target', 'attachment', 'texture', 'level'])
def glFramebufferTexture(target, attachment, texture, level):
	pass


@params(api='gles3', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix2x4fv(program, location, count, transpose, value):
	pass


@params(api='gles3', prms=['pname', 'data'])
def glGetFloatv(pname):
	pass


@params(api='gles3', prms=['pname', 'data'])
def glGetIntegerv(pname):
	pass


@params(api='gles3', prms=['id'])
def glIsQuery(id):
	pass


@params(api='gles3', prms=['target', 'level', 'internalformat', 'width', 'height', 'border', 'format', 'type', 'pixels'])
def glTexImage2D(target, level, internalformat, width, height, border, format, type, pixels):
	pass


@params(api='gles3', prms=['target', 'pname', 'params'])
def glGetFramebufferParameteriv(target, pname):
	pass


@params(api='gles3', prms=['sampler', 'pname', 'params'])
def glGetSamplerParameteriv(sampler, pname):
	pass


@params(api='gles3', prms=['readTarget', 'writeTarget', 'readOffset', 'writeOffset', 'size'])
def glCopyBufferSubData(readTarget, writeTarget, readOffset, writeOffset, size):
	pass


@params(api='gles3', prms=['program', 'index', 'bufSize', 'length', 'size', 'type', 'name'])
def glGetActiveUniform(program, index, bufSize, length, size, type, name):
	pass


@params(api='gles3', prms=['value'])
def glMinSampleShading(value):
	pass


@params(api='gles3', prms=['target', 'attachment', 'renderbuffertarget', 'renderbuffer'])
def glFramebufferRenderbuffer(target, attachment, renderbuffertarget, renderbuffer):
	pass


@params(api='gles3', prms=['unit', 'sampler'])
def glBindSampler(unit, sampler):
	pass


@params(api='gles3', prms=['width'])
def glLineWidth(width):
	pass


@params(api='gles3', prms=['target', 'index', 'data'])
def glGetIntegeri_v(target, index):
	pass


@params(api='gles3', prms=['program', 'index', 'bufSize', 'length', 'size', 'type', 'name'])
def glGetTransformFeedbackVarying(program, index, bufSize, length, size, type, name):
	pass


@params(api='gles3', prms=['n', 'f'])
def glDepthRangef(n, f):
	pass


@params(api='gles3', prms=['target', 'index'])
def glEnablei(target, index):
	pass


@params(api='gles3', prms=['maskNumber', 'mask'])
def glSampleMaski(maskNumber, mask):
	pass


@params(api='gles3', prms=['location', 'count', 'transpose', 'value'])
def glUniformMatrix3x2fv(location, count, transpose, value):
	pass


@params(api='gles3', prms=['target', 'internalformat', 'pname', 'bufSize', 'params'])
def glGetInternalformativ(target, internalformat, pname, bufSize):
	pass


@params(api='gles3', prms=['program', 'location', 'v0'])
def glProgramUniform1ui(program, location, v0):
	pass


@params(api='gles3', prms=['index', 'r', 'g', 'b', 'a'])
def glColorMaski(index, r, g, b, a):
	pass


@params(api='gles3', prms=['target', 'levels', 'internalformat', 'width', 'height', 'depth'])
def glTexStorage3D(target, levels, internalformat, width, height, depth):
	pass


@params(api='gles3', prms=['location', 'count', 'transpose', 'value'])
def glUniformMatrix3x4fv(location, count, transpose, value):
	pass


@params(api='gles3', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix4x3fv(program, location, count, transpose, value):
	pass


@params(api='gles3', prms=['target', 'attachment', 'pname', 'params'])
def glGetFramebufferAttachmentParameteriv(target, attachment, pname):
	pass


@params(api='gles3', prms=['target', 'pname', 'params'])
def glTexParameteriv(target, pname, params):
	pass


@params(api='gles3', prms=['program', 'location', 'count', 'value'])
def glProgramUniform2iv(program, location, count, value):
	pass


@params(api='gles3', prms=['target', 'pname', 'params'])
def glGetQueryiv(target, pname):
	pass


@params(api='gles3', prms=['identifier', 'name', 'length', 'label'])
def glObjectLabel(identifier, name, length, label):
	pass


@params(api='gles3', prms=['buffer', 'drawbuffer', 'value'])
def glClearBufferuiv(buffer, drawbuffer, value):
	pass


@params(api='gles3', prms=['index', 'size', 'type', 'stride', 'pointer'])
def glVertexAttribIPointer(index, size, type, stride, pointer):
	pass


@params(api='gles3', prms=[])
def glFlush():
	pass


@params(api='gles3', prms=['target', 'level', 'pname', 'params'])
def glGetTexLevelParameteriv(target, level, pname):
	pass


@params(api='gles3', prms=['target', 'samples', 'internalformat', 'width', 'height', 'depth', 'fixedsamplelocations'])
def glTexStorage3DMultisample(target, samples, internalformat, width, height, depth, fixedsamplelocations):
	pass


@params(api='gles3', prms=['s'])
def glClearStencil(s):
	pass


@params(api='gles3', prms=['texture'])
def glIsTexture(texture):
	pass


@params(api='gles3', prms=['factor', 'units'])
def glPolygonOffset(factor, units):
	pass


@params(api='gles3', prms=['target', 'level', 'internalformat', 'width', 'height', 'depth', 'border', 'format', 'type', 'pixels'])
def glTexImage3D(target, level, internalformat, width, height, depth, border, format, type, pixels):
	pass


@params(api='gles3', prms=['program', 'pname', 'params'])
def glGetProgramiv(program, pname):
	pass


@params(api='gles3', prms=['program', 'location', 'count', 'value'])
def glProgramUniform4fv(program, location, count, value):
	pass


@params(api='gles3', prms=[])
def glBlendBarrier():
	pass


@params(api='gles3', prms=['target', 'offset', 'length'])
def glFlushMappedBufferRange(target, offset, length):
	pass


@params(api='gles3', prms=['target', 'levels', 'internalformat', 'width', 'height'])
def glTexStorage2D(target, levels, internalformat, width, height):
	pass


@params(api='gles3', prms=['n', 'ids'])
def glGenQueries(n, ids):
	pass


@params(api='gles3', prms=['target', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth', 'format', 'type', 'pixels'])
def glTexSubImage3D(target, level, xoffset, yoffset, zoffset, width, height, depth, format, type, pixels):
	pass


@params(api='gles3', prms=['count', 'samplers'])
def glDeleteSamplers(count, samplers):
	pass


@params(api='gles3', prms=['location', 'count', 'value'])
def glUniform3fv(location, count, value):
	pass


@params(api='gles3', prms=['n', 'bufs'])
def glDrawBuffers(n, bufs):
	pass


@params(api='gles3', prms=['target', 'id'])
def glBindTransformFeedback(target, id):
	pass


@params(api='gles3', prms=['location', 'count', 'value'])
def glUniform2uiv(location, count, value):
	pass


@params(api='gles3', prms=[])
def glFinish():
	pass


@params(api='gles3', prms=['location', 'count', 'value'])
def glUniform1uiv(location, count, value):
	pass


@params(api='gles3', prms=['n', 'ids'])
def glDeleteQueries(n, ids):
	pass


@params(api='gles3', prms=['index', 'pname', 'params'])
def glGetVertexAttribfv(index, pname):
	pass


@params(api='gles3', prms=['num_groups_x', 'num_groups_y', 'num_groups_z'])
def glDispatchCompute(num_groups_x, num_groups_y, num_groups_z):
	pass


@params(api='gles3', prms=['program', 'index', 'bufSize', 'length', 'size', 'type', 'name'])
def glGetActiveAttrib(program, index, bufSize, length, size, type, name):
	pass


@params(api='gles3', prms=['location', 'v0', 'v1', 'v2'])
def glUniform3i(location, v0, v1, v2):
	pass


@params(api='gles3', prms=['target', 'level', 'xoffset', 'yoffset', 'width', 'height', 'format', 'type', 'pixels'])
def glTexSubImage2D(target, level, xoffset, yoffset, width, height, format, type, pixels):
	pass


@params(api='gles3', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix3x4fv(program, location, count, transpose, value):
	pass


@params(api='gles3', prms=['location', 'v0', 'v1', 'v2'])
def glUniform3ui(location, v0, v1, v2):
	pass


@params(api='gles3', prms=['count', 'shaders', 'binaryformat', 'binary', 'length'])
def glShaderBinary(count, shaders, binaryformat, binary, length):
	pass


@params(api='gles3', prms=['mode', 'count', 'type', 'indices'])
def glDrawElements(mode, count, type, indices):
	pass


@params(api='gles3', prms=['program', 'location', 'count', 'value'])
def glProgramUniform4iv(program, location, count, value):
	pass


@params(api='gles3', prms=['location', 'count', 'value'])
def glUniform1iv(location, count, value):
	pass


@params(api='gles3', prms=['mode', 'first', 'count', 'instancecount'])
def glDrawArraysInstanced(mode, first, count, instancecount):
	pass


@params(api='gles3', prms=['program', 'location', 'count', 'value'])
def glProgramUniform1iv(program, location, count, value):
	pass


@params(api='gles3', prms=['target', 'renderbuffer'])
def glBindRenderbuffer(target, renderbuffer):
	pass


@params(api='gles3', prms=['program'])
def glIsProgram(program):
	pass


@params(api='gles3', prms=['index', 'v'])
def glVertexAttrib4fv(index, v):
	pass


@params(api='gles3', prms=['index', 'v'])
def glVertexAttrib2fv(index, v):
	pass


@params(api='gles3', prms=['program', 'location', 'v0', 'v1', 'v2'])
def glProgramUniform3i(program, location, v0, v1, v2):
	pass


@params(api='gles3', prms=['pname', 'data'])
def glGetInteger64v(pname):
	pass


@params(api='gles3', prms=['buffer', 'drawbuffer', 'value'])
def glClearBufferiv(buffer, drawbuffer, value):
	pass


@params(api='gles3', prms=['sampler', 'pname', 'params'])
def glGetSamplerParameterIuiv(sampler, pname):
	pass


@params(api='gles3', prms=['location', 'v0', 'v1'])
def glUniform2f(location, v0, v1):
	pass


@params(api='gles3', prms=['d'])
def glClearDepthf(d):
	pass


@params(api='gles3', prms=['index', 'x', 'y', 'z', 'w'])
def glVertexAttribI4ui(index, x, y, z, w):
	pass


@params(api='gles3', prms=['red', 'green', 'blue', 'alpha'])
def glColorMask(red, green, blue, alpha):
	pass


@params(api='gles3', prms=['mode'])
def glBlendEquation(mode):
	pass


@params(api='gles3', prms=['program', 'programInterface', 'index', 'propCount', 'props', 'bufSize', 'length', 'params'])
def glGetProgramResourceiv(program, programInterface, index, props, bufSize, length):
	pass


@params(api='gles3', prms=['primitiveMode'])
def glBeginTransformFeedback(primitiveMode):
	pass


@params(api='gles3', prms=['n', 'ids'])
def glDeleteTransformFeedbacks(n, ids):
	pass


@params(api='gles3', prms=['mode', 'start', 'end', 'count', 'type', 'indices', 'basevertex'])
def glDrawRangeElementsBaseVertex(mode, start, end, count, type, indices, basevertex):
	pass


@params(api='gles3', prms=['program', 'index', 'name'])
def glBindAttribLocation(program, index, name):
	pass


@params(api='gles3', prms=['buf', 'srcRGB', 'dstRGB', 'srcAlpha', 'dstAlpha'])
def glBlendFuncSeparatei(buf, srcRGB, dstRGB, srcAlpha, dstAlpha):
	pass


@params(api='gles3', prms=['location', 'v0', 'v1'])
def glUniform2ui(location, v0, v1):
	pass


@params(api='gles3', prms=['target', 'index'])
def glDisablei(target, index):
	pass


@params(api='gles3', prms=['sync', 'pname', 'bufSize', 'length', 'values'])
def glGetSynciv(sync, pname, bufSize, length, values):
	pass


@params(api='gles3', prms=['program', 'location', 'v0', 'v1'])
def glProgramUniform2i(program, location, v0, v1):
	pass


@params(api='gles3', prms=['program', 'bufSize', 'length', 'binaryFormat', 'binary'])
def glGetProgramBinary(program, bufSize, length, binaryFormat):
	pass


@params(api='gles3', prms=[])
def glPauseTransformFeedback():
	pass


@params(api='gles3', prms=['index', 'v'])
def glVertexAttribI4iv(index, v):
	pass


@params(api='gles3', prms=['target', 'pname', 'params'])
def glTexParameterfv(target, pname, params):
	pass


@params(api='gles3', prms=['face', 'func', 'ref', 'mask'])
def glStencilFuncSeparate(face, func, ref, mask):
	pass


@params(api='gles3', prms=['program', 'location', 'count', 'value'])
def glProgramUniform3fv(program, location, count, value):
	pass


@params(api='gles3', prms=['program', 'location', 'count', 'value'])
def glProgramUniform1fv(program, location, count, value):
	pass


@params(api='gles3', prms=['location', 'count', 'transpose', 'value'])
def glUniformMatrix4fv(location, count, transpose, value):
	pass


@params(api='gles3', prms=['n', 'pipelines'])
def glDeleteProgramPipelines(n, pipelines):
	pass


@params(api='gles3', prms=['shader'])
def glCompileShader(shader):
	pass


@params(api='gles3', prms=['target', 'numAttachments', 'attachments'])
def glInvalidateFramebuffer(target, numAttachments, attachments):
	pass


@params(api='gles3', prms=['target', 'level', 'internalformat', 'width', 'height', 'border', 'imageSize', 'data'])
def glCompressedTexImage2D(target, level, internalformat, width, height, border, imageSize, data):
	pass


@params(api='gles3', prms=['index', 'x'])
def glVertexAttrib1f(index, x):
	pass


@params(api='gles3', prms=['program'])
def glDeleteProgram(program):
	pass


@params(api='gles3', prms=['location', 'count', 'transpose', 'value'])
def glUniformMatrix4x3fv(location, count, transpose, value):
	pass


@params(api='gles3', prms=['buffer', 'drawbuffer', 'value'])
def glClearBufferfv(buffer, drawbuffer, value):
	pass


@params(api='gles3', prms=['buffer', 'drawbuffer', 'depth', 'stencil'])
def glClearBufferfi(buffer, drawbuffer, depth, stencil):
	pass


@params(api='gles3', prms=['mode', 'indirect'])
def glDrawArraysIndirect(mode, indirect):
	pass


@params(api='gles3', prms=['n', 'arrays'])
def glGenVertexArrays(n):
	pass


@params(api='gles3', prms=['bindingindex', 'divisor'])
def glVertexBindingDivisor(bindingindex, divisor):
	pass


@params(api='gles3', prms=['sampler', 'pname', 'params'])
def glGetSamplerParameterIiv(sampler, pname):
	pass


@params(api='gles3', prms=['location', 'count', 'transpose', 'value'])
def glUniformMatrix4x2fv(location, count, transpose, value):
	pass


@params(api='gles3', prms=['index', 'x', 'y', 'z'])
def glVertexAttrib3f(index, x, y, z):
	pass


@params(api='gles3', prms=['location', 'v0'])
def glUniform1ui(location, v0):
	pass


@params(api='gles3', prms=['barriers'])
def glMemoryBarrier(barriers):
	pass


@params(api='gles3', prms=['program', 'name'])
def glGetFragDataLocation(program, name):
	pass


@params(api='gles3', prms=['shader'])
def glIsShader(shader):
	pass


@params(api='gles3', prms=['cap'])
def glEnable(cap):
	pass


@params(api='gles3', prms=['program', 'uniformCount', 'uniformIndices', 'pname', 'params'])
def glGetActiveUniformsiv(program, uniformCount, uniformIndices, pname):
	pass


@params(api='gles3', prms=['buf', 'mode'])
def glBlendEquationi(buf, mode):
	pass


@params(api='gles3', prms=['program', 'name'])
def glGetAttribLocation(program, name):
	pass


@params(api='gles3', prms=['program', 'location', 'v0', 'v1', 'v2'])
def glProgramUniform3ui(program, location, v0, v1, v2):
	pass


@params(api='gles3', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix2x3fv(program, location, count, transpose, value):
	pass


@params(api='gles3', prms=['program', 'location', 'v0'])
def glProgramUniform1i(program, location, v0):
	pass


@params(api='gles3', prms=['program', 'location', 'v0'])
def glProgramUniform1f(program, location, v0):
	pass


@params(api='gles3', prms=['program', 'location', 'count', 'value'])
def glProgramUniform3iv(program, location, count, value):
	pass


@params(api='gles3', prms=['location', 'count', 'value'])
def glUniform4iv(location, count, value):
	pass


@params(api='gles3', prms=['n', 'textures'])
def glGenTextures(n):
	pass


@params(api='gles3', prms=['index', 'size', 'type', 'normalized', 'stride', 'pointer'])
def glVertexAttribPointer(index, size, type, normalized, stride, pointer):
	pass


@params(api='gles3', prms=['location', 'v0'])
def glUniform1f(location, v0):
	pass


@params(api='gles3', prms=['location', 'count', 'value'])
def glUniform2iv(location, count, value):
	pass


@params(api='gles3', prms=['shader', 'pname', 'params'])
def glGetShaderiv(shader, pname):
	pass


@params(api='gles3', prms=['target', 'level', 'internalformat', 'width', 'height', 'depth', 'border', 'imageSize', 'data'])
def glCompressedTexImage3D(target, level, internalformat, width, height, depth, border, imageSize, data):
	pass


@params(api='gles3', prms=['index', 'pname', 'params'])
def glGetVertexAttribiv(index, pname):
	pass


@params(api='gles3', prms=['location', 'count', 'transpose', 'value'])
def glUniformMatrix2fv(location, count, transpose, value):
	pass


@params(api='gles3', prms=['target', 'pname', 'params'])
def glGetTexParameterIiv(target, pname):
	pass


@params(api='gles3', prms=['callback', 'userParam'])
def glDebugMessageCallback(callback, userParam):
	pass


@params(api='gles3', prms=['target', 'index', 'data'])
def glGetBooleani_v(target, index):
	pass


@params(api='gles3', prms=['target', 'mode'])
def glHint(target, mode):
	pass


@params(api='gles3', prms=['program', 'programInterface', 'index', 'bufSize', 'length', 'name'])
def glGetProgramResourceName(program, programInterface, index, bufSize, length, name):
	pass


@params(api='gles3', prms=['face', 'sfail', 'dpfail', 'dppass'])
def glStencilOpSeparate(face, sfail, dpfail, dppass):
	pass


@params(api='gles3', prms=['target', 'pname', 'params'])
def glGetTexParameteriv(target, pname):
	pass


@params(api='gles3', prms=['index', 'pname', 'pointer'])
def glGetVertexAttribPointerv(index, pname, pointer):
	pass


@params(api='gles3', prms=['cap'])
def glDisable(cap):
	pass


@params(api='gles3', prms=['program', 'location', 'count', 'value'])
def glProgramUniform4uiv(program, location, count, value):
	pass


@params(api='gles3', prms=['location', 'count', 'value'])
def glUniform3uiv(location, count, value):
	pass


@params(api='gles3', prms=['red', 'green', 'blue', 'alpha'])
def glBlendColor(red, green, blue, alpha):
	pass


@params(api='gles3', prms=['sampler', 'pname', 'param'])
def glSamplerParameterIuiv(sampler, pname, param):
	pass


@params(api='gles3', prms=['location', 'v0', 'v1', 'v2', 'v3'])
def glUniform4i(location, v0, v1, v2, v3):
	pass


@params(api='gles3', prms=['texture'])
def glActiveTexture(texture):
	pass


@params(api='gles3', prms=['index'])
def glEnableVertexAttribArray(index):
	pass


@params(api='gles3', prms=['location', 'v0', 'v1', 'v2', 'v3'])
def glUniform4f(location, v0, v1, v2, v3):
	pass


@params(api='gles3', prms=['target', 'samples', 'internalformat', 'width', 'height'])
def glRenderbufferStorageMultisample(target, samples, internalformat, width, height):
	pass


@params(api='gles3', prms=['mode', 'count', 'type', 'indices', 'instancecount', 'basevertex'])
def glDrawElementsInstancedBaseVertex(mode, count, type, indices, instancecount, basevertex):
	pass


@params(api='gles3', prms=[])
def glPopDebugGroup():
	pass


@params(api='gles3', prms=['program', 'uniformBlockIndex', 'uniformBlockBinding'])
def glUniformBlockBinding(program, uniformBlockIndex, uniformBlockBinding):
	pass


@params(api='gles3', prms=['target', 'offset', 'size', 'data'])
def glBufferSubData(target, offset, size, data):
	pass


@params(api='gles3', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix3x2fv(program, location, count, transpose, value):
	pass


@params(api='gles3', prms=['sfactor', 'dfactor'])
def glBlendFunc(sfactor, dfactor):
	pass


@params(api='gles3', prms=[])
def glCreateProgram():
	pass


@params(api='gles3', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix2fv(program, location, count, transpose, value):
	pass


@params(api='gles3', prms=['sampler', 'pname', 'param'])
def glSamplerParameteriv(sampler, pname, param):
	pass


@params(api='gles3', prms=['red', 'green', 'blue', 'alpha'])
def glClearColor(red, green, blue, alpha):
	pass


@params(api='gles3', prms=['program', 'location', 'bufSize', 'params'])
def glGetnUniformiv(program, location, bufSize):
	pass


@params(api='gles3', prms=['mask'])
def glStencilMask(mask):
	pass


@params(api='gles3', prms=['index', 'v'])
def glVertexAttribI4uiv(index, v):
	pass


@params(api='gles3', prms=['program', 'programInterface', 'name'])
def glGetProgramResourceIndex(program, programInterface, name):
	pass


@params(api='gles3', prms=['location', 'count', 'transpose', 'value'])
def glUniformMatrix2x3fv(location, count, transpose, value):
	pass


@params(api='gles3', prms=['n', 'ids'])
def glGenTransformFeedbacks(n, ids):
	pass


@params(api='gles3', prms=['index', 'pname', 'params'])
def glGetVertexAttribIuiv(index, pname):
	pass


@params(api='gles3', prms=['target', 'level', 'xoffset', 'yoffset', 'width', 'height', 'format', 'imageSize', 'data'])
def glCompressedTexSubImage2D(target, level, xoffset, yoffset, width, height, format, imageSize, data):
	pass


@params(api='gles3', prms=['program', 'binaryFormat', 'binary', 'length'])
def glProgramBinary(program, binaryFormat, binary, length):
	pass


@params(api='gles3', prms=['target', 'pname', 'params'])
def glGetTexParameterfv(target, pname):
	pass


@params(api='gles3', prms=['target', 'pname', 'params'])
def glTexParameterIiv(target, pname, params):
	pass


@params(api='gles3', prms=[])
def glEndTransformFeedback():
	pass


@params(api='gles3', prms=['index', 'divisor'])
def glVertexAttribDivisor(index, divisor):
	pass


@params(api='gles3', prms=['target', 'offset', 'length', 'access'])
def glMapBufferRange(target, offset, length, access):
	pass


@params(api='gles3', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix4x2fv(program, location, count, transpose, value):
	pass


@params(api='gles3', prms=['shadertype', 'precisiontype', 'range', 'precision'])
def glGetShaderPrecisionFormat(shadertype, precisiontype):
	pass


@params(api='gles3', prms=['shader', 'count', 'conststring', 'length'])
def glShaderSource(shader, count, conststring, length):
	pass


@params(api='gles3', prms=['n', 'renderbuffers'])
def glDeleteRenderbuffers(n, renderbuffers):
	pass


@params(api='gles3', prms=['target', 'size', 'data', 'usage'])
def glBufferData(target, size, data, usage):
	pass


@params(api='gles3', prms=['target', 'attachment', 'textarget', 'texture', 'level'])
def glFramebufferTexture2D(target, attachment, textarget, texture, level):
	pass


@params(api='gles3', prms=['target', 'pname', 'params'])
def glGetBufferPointerv(target, pname):
	pass


@params(api='gles3', prms=['sampler', 'pname', 'param'])
def glSamplerParameterfv(sampler, pname, param):
	pass


@params(api='gles3', prms=['location', 'count', 'value'])
def glUniform1fv(location, count, value):
	pass


@params(api='gles3', prms=['index', 'x', 'y'])
def glVertexAttrib2f(index, x, y):
	pass


@params(api='gles3', prms=['program', 'uniformBlockName'])
def glGetUniformBlockIndex(program, uniformBlockName):
	pass


@params(api='gles3', prms=['mode'])
def glFrontFace(mode):
	pass


