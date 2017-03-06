def glStencilMaskSeparate(face, mask):
	return lib.glStencilMaskSeparate(face, mask)

def glCompressedTexSubImage3D(target, level, xoffset, yoffset, zoffset, width, height, depth, format, imageSize):
	data = ffi.new('const void *')
	return lib.glCompressedTexSubImage3D(target, level, xoffset, yoffset, zoffset, width, height, depth, format, imageSize, data)

def glIsBuffer(buffer):
	return lib.glIsBuffer(buffer)

def glGetMultisamplefv(pname, index, val):
	return lib.glGetMultisamplefv(pname, index, val)

def glProgramUniformMatrix4fv(program, location, count, transpose, value):
	return lib.glProgramUniformMatrix4fv(program, location, count, transpose, value)

def glDebugMessageControl(source, type, severity, count, ids, enabled):
	return lib.glDebugMessageControl(source, type, severity, count, ids, enabled)

def glRenderbufferStorage(target, internalformat, width, height):
	return lib.glRenderbufferStorage(target, internalformat, width, height)

def glProgramUniform3f(program, location, v0, v1, v2):
	return lib.glProgramUniform3f(program, location, v0, v1, v2)

def glResumeTransformFeedback():
	return lib.glResumeTransformFeedback()

def glGetGraphicsResetStatus():
	return lib.glGetGraphicsResetStatus()

def glVertexAttrib1fv(index, v):
	return lib.glVertexAttrib1fv(index, v)

def glIsEnabled(cap):
	return lib.glIsEnabled(cap)

def glStencilOp(fail, zfail, zpass):
	return lib.glStencilOp(fail, zfail, zpass)

def glGenFramebuffers(n, framebuffers):
	return lib.glGenFramebuffers(n, framebuffers)

def glGetAttachedShaders(program, maxCount, count, shaders):
	return lib.glGetAttachedShaders(program, maxCount, count, shaders)

def glDeleteVertexArrays(n, arrays):
	return lib.glDeleteVertexArrays(n, arrays)

def glGetPointerv(pname):
	params = ffi.new('void *')
	return lib.glGetPointerv(pname, params)

def glGetUniformfv(program, location):
	params = ffi.new('GLfloat *')
	return lib.glGetUniformfv(program, location, params)

def glGetUniformuiv(program, location):
	params = ffi.new('GLuint *')
	return lib.glGetUniformuiv(program, location, params)

def glProgramUniformMatrix3fv(program, location, count, transpose, value):
	return lib.glProgramUniformMatrix3fv(program, location, count, transpose, value)

def glDrawElementsInstanced(mode, count, type, indices, instancecount):
	return lib.glDrawElementsInstanced(mode, count, type, indices, instancecount)

def glGetRenderbufferParameteriv(target, pname):
	params = ffi.new('GLint *')
	return lib.glGetRenderbufferParameteriv(target, pname, params)

def glFenceSync(condition, flags):
	return lib.glFenceSync(condition, flags)

def glValidateProgramPipeline(pipeline):
	return lib.glValidateProgramPipeline(pipeline)

def glGenSamplers(count, samplers):
	return lib.glGenSamplers(count, samplers)

def glGetTexParameterIuiv(target, pname):
	params = ffi.new('GLuint *')
	return lib.glGetTexParameterIuiv(target, pname, params)

def glIsSync(sync):
	return lib.glIsSync(sync)

def glGetObjectPtrLabel(ptr, bufSize, length, label):
	return lib.glGetObjectPtrLabel(ptr, bufSize, length, label)

def glCopyTexImage2D(target, level, internalformat, x, y, width, height, border):
	return lib.glCopyTexImage2D(target, level, internalformat, x, y, width, height, border)

def glUniform4uiv(location, count, value):
	return lib.glUniform4uiv(location, count, value)

def glInvalidateSubFramebuffer(target, numAttachments, attachments, x, y, width, height):
	return lib.glInvalidateSubFramebuffer(target, numAttachments, attachments, x, y, width, height)

def glDeleteSync(sync):
	return lib.glDeleteSync(sync)

def glUniform3iv(location, count, value):
	return lib.glUniform3iv(location, count, value)

def glUseProgram(program):
	return lib.glUseProgram(program)

def glGetProgramInfoLog(program, bufSize, length, infoLog):
	return lib.glGetProgramInfoLog(program, bufSize, length, infoLog)

def glGetBooleanv(pname):
	data = ffi.new('GLboolean *')
	return lib.glGetBooleanv(pname, data)

def glDeleteShader(shader):
	return lib.glDeleteShader(shader)

def glVertexAttribFormat(attribindex, size, type, normalized, relativeoffset):
	return lib.glVertexAttribFormat(attribindex, size, type, normalized, relativeoffset)

def glTexParameterf(target, pname, param):
	return lib.glTexParameterf(target, pname, param)

def glVertexAttribBinding(attribindex, bindingindex):
	return lib.glVertexAttribBinding(attribindex, bindingindex)

def glTexParameteri(target, pname, param):
	return lib.glTexParameteri(target, pname, param)

def glGetShaderSource(shader, bufSize, length, source):
	return lib.glGetShaderSource(shader, bufSize, length, source)

def glGenProgramPipelines(n, pipelines):
	return lib.glGenProgramPipelines(n, pipelines)

def glVertexAttrib3fv(index, v):
	return lib.glVertexAttrib3fv(index, v)

def glLinkProgram(program):
	return lib.glLinkProgram(program)

def glGetObjectLabel(identifier, bufSize, length, label):
	name = ffi.new('GLuint *')
	return lib.glGetObjectLabel(identifier, name, bufSize, length, label)

def glGetString():
	name = ffi.new('GLenum *')
	return lib.glGetString(name)

def glEndQuery(target):
	return lib.glEndQuery(target)

def glFramebufferParameteri(target, pname, param):
	return lib.glFramebufferParameteri(target, pname, param)

def glDeleteTextures(n, textures):
	return lib.glDeleteTextures(n, textures)

def glVertexAttrib4f(index, x, y, z, w):
	return lib.glVertexAttrib4f(index, x, y, z, w)

def glSamplerParameteri(sampler, pname, param):
	return lib.glSamplerParameteri(sampler, pname, param)

def glGetActiveUniformBlockiv(program, uniformBlockIndex, pname):
	params = ffi.new('GLint *')
	return lib.glGetActiveUniformBlockiv(program, uniformBlockIndex, pname, params)

def glUniform1i(location, v0):
	return lib.glUniform1i(location, v0)

def glCullFace(mode):
	return lib.glCullFace(mode)

def glProgramUniform4i(program, location, v0, v1, v2, v3):
	return lib.glProgramUniform4i(program, location, v0, v1, v2, v3)

def glProgramUniform4f(program, location, v0, v1, v2, v3):
	return lib.glProgramUniform4f(program, location, v0, v1, v2, v3)

def glAttachShader(program, shader):
	return lib.glAttachShader(program, shader)

def glGetBufferParameteriv(target, pname):
	params = ffi.new('GLint *')
	return lib.glGetBufferParameteriv(target, pname, params)

def glTexParameterIuiv(target, pname):
	params = ffi.new('const GLuint *')
	return lib.glTexParameterIuiv(target, pname, params)

def glIsTransformFeedback(id):
	return lib.glIsTransformFeedback(id)

def glIsProgramPipeline(pipeline):
	return lib.glIsProgramPipeline(pipeline)

def glUniformMatrix3fv(location, count, transpose, value):
	return lib.glUniformMatrix3fv(location, count, transpose, value)

def glGetnUniformfv(program, location, bufSize):
	params = ffi.new('GLfloat *')
	return lib.glGetnUniformfv(program, location, bufSize, params)

def glStencilFunc(func, ref, mask):
	return lib.glStencilFunc(func, ref, mask)

def glGetProgramPipelineiv(pipeline, pname):
	params = ffi.new('GLint *')
	return lib.glGetProgramPipelineiv(pipeline, pname, params)

def glDispatchComputeIndirect(indirect):
	return lib.glDispatchComputeIndirect(indirect)

def glGetShaderInfoLog(shader, bufSize, length, infoLog):
	return lib.glGetShaderInfoLog(shader, bufSize, length, infoLog)

def glVertexAttribI4i(index, x, y, z, w):
	return lib.glVertexAttribI4i(index, x, y, z, w)

def glBlendEquationSeparate(modeRGB, modeAlpha):
	return lib.glBlendEquationSeparate(modeRGB, modeAlpha)

def glDeleteBuffers(n, buffers):
	return lib.glDeleteBuffers(n, buffers)

def glBindProgramPipeline(pipeline):
	return lib.glBindProgramPipeline(pipeline)

def glScissor(x, y, width, height):
	return lib.glScissor(x, y, width, height)

def glGetStringi(index):
	name = ffi.new('GLenum *')
	return lib.glGetStringi(name, index)

def glUniform2fv(location, count, value):
	return lib.glUniform2fv(location, count, value)

def glBindBufferRange(target, index, buffer, offset, size):
	return lib.glBindBufferRange(target, index, buffer, offset, size)

def glClientWaitSync(sync, flags, timeout):
	return lib.glClientWaitSync(sync, flags, timeout)

def glReadnPixels(x, y, width, height, format, type, bufSize):
	data = ffi.new('void *')
	return lib.glReadnPixels(x, y, width, height, format, type, bufSize, data)

def glCopyImageSubData(srcName, srcTarget, srcLevel, srcX, srcY, srcZ, dstName, dstTarget, dstLevel, dstX, dstY, dstZ, srcWidth, srcHeight, srcDepth):
	return lib.glCopyImageSubData(srcName, srcTarget, srcLevel, srcX, srcY, srcZ, dstName, dstTarget, dstLevel, dstX, dstY, dstZ, srcWidth, srcHeight, srcDepth)

def glBindVertexBuffer(bindingindex, buffer, offset, stride):
	return lib.glBindVertexBuffer(bindingindex, buffer, offset, stride)

def glDebugMessageInsert(source, type, id, severity, length, buf):
	return lib.glDebugMessageInsert(source, type, id, severity, length, buf)

def glIsSampler(sampler):
	return lib.glIsSampler(sampler)

def glCheckFramebufferStatus(target):
	return lib.glCheckFramebufferStatus(target)

def glBindImageTexture(unit, texture, level, layered, layer, access, format):
	return lib.glBindImageTexture(unit, texture, level, layered, layer, access, format)

def glTransformFeedbackVaryings(program, count, constvaryings, bufferMode):
	return lib.glTransformFeedbackVaryings(program, count, constvaryings, bufferMode)

def glDrawRangeElements(mode, start, end, count, type, indices):
	return lib.glDrawRangeElements(mode, start, end, count, type, indices)

def glBindBufferBase(target, index, buffer):
	return lib.glBindBufferBase(target, index, buffer)

def glVertexAttribIFormat(attribindex, size, type, relativeoffset):
	return lib.glVertexAttribIFormat(attribindex, size, type, relativeoffset)

def glBeginQuery(target, id):
	return lib.glBeginQuery(target, id)

def glUniformMatrix2x4fv(location, count, transpose, value):
	return lib.glUniformMatrix2x4fv(location, count, transpose, value)

def glGetError():
	return lib.glGetError()

def glGetTexLevelParameterfv(target, level, pname):
	params = ffi.new('GLfloat *')
	return lib.glGetTexLevelParameterfv(target, level, pname, params)

def glProgramUniform2ui(program, location, v0, v1):
	return lib.glProgramUniform2ui(program, location, v0, v1)

def glProgramUniform4ui(program, location, v0, v1, v2, v3):
	return lib.glProgramUniform4ui(program, location, v0, v1, v2, v3)

def glPixelStorei(pname, param):
	return lib.glPixelStorei(pname, param)

def glDepthMask(flag):
	return lib.glDepthMask(flag)

def glTexBufferRange(target, internalformat, buffer, offset, size):
	return lib.glTexBufferRange(target, internalformat, buffer, offset, size)

def glProgramParameteri(program, pname, value):
	return lib.glProgramParameteri(program, pname, value)

def glMemoryBarrierByRegion(barriers):
	return lib.glMemoryBarrierByRegion(barriers)

def glCreateShader(type):
	return lib.glCreateShader(type)

def glGenRenderbuffers(n, renderbuffers):
	return lib.glGenRenderbuffers(n, renderbuffers)

def glCopyTexSubImage2D(target, level, xoffset, yoffset, x, y, width, height):
	return lib.glCopyTexSubImage2D(target, level, xoffset, yoffset, x, y, width, height)

def glBlendFuncSeparate(sfactorRGB, dfactorRGB, sfactorAlpha, dfactorAlpha):
	return lib.glBlendFuncSeparate(sfactorRGB, dfactorRGB, sfactorAlpha, dfactorAlpha)

def glGetProgramPipelineInfoLog(pipeline, bufSize, length, infoLog):
	return lib.glGetProgramPipelineInfoLog(pipeline, bufSize, length, infoLog)

def glWaitSync(sync, flags, timeout):
	return lib.glWaitSync(sync, flags, timeout)

def glBlendEquationSeparatei(buf, modeRGB, modeAlpha):
	return lib.glBlendEquationSeparatei(buf, modeRGB, modeAlpha)

def glUniform3f(location, v0, v1, v2):
	return lib.glUniform3f(location, v0, v1, v2)

def glProgramUniform3uiv(program, location, count, value):
	return lib.glProgramUniform3uiv(program, location, count, value)

def glDeleteFramebuffers(n, framebuffers):
	return lib.glDeleteFramebuffers(n, framebuffers)

def glDrawArrays(mode, first, count):
	return lib.glDrawArrays(mode, first, count)

def glClear(mask):
	return lib.glClear(mask)

def glGetSamplerParameterfv(sampler, pname):
	params = ffi.new('GLfloat *')
	return lib.glGetSamplerParameterfv(sampler, pname, params)

def glSamplerParameterIiv(sampler, pname, param):
	return lib.glSamplerParameterIiv(sampler, pname, param)

def glDrawElementsIndirect(mode, type, indirect):
	return lib.glDrawElementsIndirect(mode, type, indirect)

def glGetUniformIndices(program, uniformCount, constuniformNames, uniformIndices):
	return lib.glGetUniformIndices(program, uniformCount, constuniformNames, uniformIndices)

def glIsVertexArray(array):
	return lib.glIsVertexArray(array)

def glDisableVertexAttribArray(index):
	return lib.glDisableVertexAttribArray(index)

def glGetProgramInterfaceiv(program, programInterface, pname):
	params = ffi.new('GLint *')
	return lib.glGetProgramInterfaceiv(program, programInterface, pname, params)

def glGetVertexAttribIiv(index, pname):
	params = ffi.new('GLint *')
	return lib.glGetVertexAttribIiv(index, pname, params)

def glPatchParameteri(pname, value):
	return lib.glPatchParameteri(pname, value)

def glSampleCoverage(value, invert):
	return lib.glSampleCoverage(value, invert)

def glUniform2i(location, v0, v1):
	return lib.glUniform2i(location, v0, v1)

def glFramebufferTextureLayer(target, attachment, texture, level, layer):
	return lib.glFramebufferTextureLayer(target, attachment, texture, level, layer)

def glProgramUniform2fv(program, location, count, value):
	return lib.glProgramUniform2fv(program, location, count, value)

def glPrimitiveBoundingBox(minX, minY, minZ, minW, maxX, maxY, maxZ, maxW):
	return lib.glPrimitiveBoundingBox(minX, minY, minZ, minW, maxX, maxY, maxZ, maxW)

def glGetInteger64i_v(target, index):
	data = ffi.new('GLint64 *')
	return lib.glGetInteger64i_v(target, index, data)

def glBlitFramebuffer(srcX0, srcY0, srcX1, srcY1, dstX0, dstY0, dstX1, dstY1, mask, filter):
	return lib.glBlitFramebuffer(srcX0, srcY0, srcX1, srcY1, dstX0, dstY0, dstX1, dstY1, mask, filter)

def glIsEnabledi(target, index):
	return lib.glIsEnabledi(target, index)

def glObjectPtrLabel(ptr, length, label):
	return lib.glObjectPtrLabel(ptr, length, label)

def glGetDebugMessageLog(count, bufSize, sources, types, ids, severities, lengths, messageLog):
	return lib.glGetDebugMessageLog(count, bufSize, sources, types, ids, severities, lengths, messageLog)

def glPushDebugGroup(source, id, length, message):
	return lib.glPushDebugGroup(source, id, length, message)

def glCopyTexSubImage3D(target, level, xoffset, yoffset, zoffset, x, y, width, height):
	return lib.glCopyTexSubImage3D(target, level, xoffset, yoffset, zoffset, x, y, width, height)

def glGetActiveUniformBlockName(program, uniformBlockIndex, bufSize, length, uniformBlockName):
	return lib.glGetActiveUniformBlockName(program, uniformBlockIndex, bufSize, length, uniformBlockName)

def glProgramUniform2f(program, location, v0, v1):
	return lib.glProgramUniform2f(program, location, v0, v1)

def glBindVertexArray(array):
	return lib.glBindVertexArray(array)

def glBindFramebuffer(target, framebuffer):
	return lib.glBindFramebuffer(target, framebuffer)

def glViewport(x, y, width, height):
	return lib.glViewport(x, y, width, height)

def glIsRenderbuffer(renderbuffer):
	return lib.glIsRenderbuffer(renderbuffer)

def glTexStorage2DMultisample(target, samples, internalformat, width, height, fixedsamplelocations):
	return lib.glTexStorage2DMultisample(target, samples, internalformat, width, height, fixedsamplelocations)

def glTexBuffer(target, internalformat, buffer):
	return lib.glTexBuffer(target, internalformat, buffer)

def glValidateProgram(program):
	return lib.glValidateProgram(program)

def glActiveShaderProgram(pipeline, program):
	return lib.glActiveShaderProgram(pipeline, program)

def glBindTexture(target, texture):
	return lib.glBindTexture(target, texture)

def glDetachShader(program, shader):
	return lib.glDetachShader(program, shader)

def glGetProgramResourceLocation(program, programInterface):
	name = ffi.new('const GLchar *')
	return lib.glGetProgramResourceLocation(program, programInterface, name)

def glDrawElementsBaseVertex(mode, count, type, indices, basevertex):
	return lib.glDrawElementsBaseVertex(mode, count, type, indices, basevertex)

def glGetUniformiv(program, location):
	params = ffi.new('GLint *')
	return lib.glGetUniformiv(program, location, params)

def glBindBuffer(target, buffer):
	return lib.glBindBuffer(target, buffer)

def glUniform4ui(location, v0, v1, v2, v3):
	return lib.glUniform4ui(location, v0, v1, v2, v3)

def glCreateShaderProgramv(type, count, conststrings):
	return lib.glCreateShaderProgramv(type, count, conststrings)

def glGenerateMipmap(target):
	return lib.glGenerateMipmap(target)

def glUnmapBuffer(target):
	return lib.glUnmapBuffer(target)

def glReleaseShaderCompiler():
	return lib.glReleaseShaderCompiler()

def glReadPixels(x, y, width, height, format, type):
	pixels = ffi.new('void *')
	return lib.glReadPixels(x, y, width, height, format, type, pixels)

def glUseProgramStages(pipeline, stages, program):
	return lib.glUseProgramStages(pipeline, stages, program)

def glReadBuffer(src):
	return lib.glReadBuffer(src)

def glGetnUniformuiv(program, location, bufSize):
	params = ffi.new('GLuint *')
	return lib.glGetnUniformuiv(program, location, bufSize, params)

def glGenBuffers(n, buffers):
	return lib.glGenBuffers(n, buffers)

def glIsFramebuffer(framebuffer):
	return lib.glIsFramebuffer(framebuffer)

def glGetBufferParameteri64v(target, pname):
	params = ffi.new('GLint64 *')
	return lib.glGetBufferParameteri64v(target, pname, params)

def glDepthFunc(func):
	return lib.glDepthFunc(func)

def glSamplerParameterf(sampler, pname, param):
	return lib.glSamplerParameterf(sampler, pname, param)

def glBlendFunci(buf, src, dst):
	return lib.glBlendFunci(buf, src, dst)

def glGetUniformLocation(program):
	name = ffi.new('const GLchar *')
	return lib.glGetUniformLocation(program, name)

def glUniform4fv(location, count, value):
	return lib.glUniform4fv(location, count, value)

def glProgramUniform2uiv(program, location, count, value):
	return lib.glProgramUniform2uiv(program, location, count, value)

def glGetQueryObjectuiv(id, pname):
	params = ffi.new('GLuint *')
	return lib.glGetQueryObjectuiv(id, pname, params)

def glProgramUniform1uiv(program, location, count, value):
	return lib.glProgramUniform1uiv(program, location, count, value)

def glFramebufferTexture(target, attachment, texture, level):
	return lib.glFramebufferTexture(target, attachment, texture, level)

def glProgramUniformMatrix2x4fv(program, location, count, transpose, value):
	return lib.glProgramUniformMatrix2x4fv(program, location, count, transpose, value)

def glGetFloatv(pname):
	data = ffi.new('GLfloat *')
	return lib.glGetFloatv(pname, data)

def glGetIntegerv(pname):
	data = ffi.new('GLint *')
	return lib.glGetIntegerv(pname, data)

def glIsQuery(id):
	return lib.glIsQuery(id)

def glTexImage2D(target, level, internalformat, width, height, border, format, type):
	pixels = ffi.new('const void *')
	return lib.glTexImage2D(target, level, internalformat, width, height, border, format, type, pixels)

def glGetFramebufferParameteriv(target, pname):
	params = ffi.new('GLint *')
	return lib.glGetFramebufferParameteriv(target, pname, params)

def glGetSamplerParameteriv(sampler, pname):
	params = ffi.new('GLint *')
	return lib.glGetSamplerParameteriv(sampler, pname, params)

def glCopyBufferSubData(readTarget, writeTarget, readOffset, writeOffset, size):
	return lib.glCopyBufferSubData(readTarget, writeTarget, readOffset, writeOffset, size)

def glGetActiveUniform(program, index, bufSize, length, size, type):
	name = ffi.new('GLchar *')
	return lib.glGetActiveUniform(program, index, bufSize, length, size, type, name)

def glMinSampleShading(value):
	return lib.glMinSampleShading(value)

def glFramebufferRenderbuffer(target, attachment, renderbuffertarget, renderbuffer):
	return lib.glFramebufferRenderbuffer(target, attachment, renderbuffertarget, renderbuffer)

def glBindSampler(unit, sampler):
	return lib.glBindSampler(unit, sampler)

def glLineWidth(width):
	return lib.glLineWidth(width)

def glGetIntegeri_v(target, index):
	data = ffi.new('GLint *')
	return lib.glGetIntegeri_v(target, index, data)

def glGetTransformFeedbackVarying(program, index, bufSize, length, size, type):
	name = ffi.new('GLchar *')
	return lib.glGetTransformFeedbackVarying(program, index, bufSize, length, size, type, name)

def glDepthRangef(n, f):
	return lib.glDepthRangef(n, f)

def glEnablei(target, index):
	return lib.glEnablei(target, index)

def glSampleMaski(maskNumber, mask):
	return lib.glSampleMaski(maskNumber, mask)

def glUniformMatrix3x2fv(location, count, transpose, value):
	return lib.glUniformMatrix3x2fv(location, count, transpose, value)

def glGetInternalformativ(target, internalformat, pname, bufSize):
	params = ffi.new('GLint *')
	return lib.glGetInternalformativ(target, internalformat, pname, bufSize, params)

def glProgramUniform1ui(program, location, v0):
	return lib.glProgramUniform1ui(program, location, v0)

def glColorMaski(index, r, g, b, a):
	return lib.glColorMaski(index, r, g, b, a)

def glTexStorage3D(target, levels, internalformat, width, height, depth):
	return lib.glTexStorage3D(target, levels, internalformat, width, height, depth)

def glUniformMatrix3x4fv(location, count, transpose, value):
	return lib.glUniformMatrix3x4fv(location, count, transpose, value)

def glProgramUniformMatrix4x3fv(program, location, count, transpose, value):
	return lib.glProgramUniformMatrix4x3fv(program, location, count, transpose, value)

def glGetFramebufferAttachmentParameteriv(target, attachment, pname):
	params = ffi.new('GLint *')
	return lib.glGetFramebufferAttachmentParameteriv(target, attachment, pname, params)

def glTexParameteriv(target, pname):
	params = ffi.new('const GLint *')
	return lib.glTexParameteriv(target, pname, params)

def glProgramUniform2iv(program, location, count, value):
	return lib.glProgramUniform2iv(program, location, count, value)

def glGetQueryiv(target, pname):
	params = ffi.new('GLint *')
	return lib.glGetQueryiv(target, pname, params)

def glObjectLabel(identifier, length, label):
	name = ffi.new('GLuint *')
	return lib.glObjectLabel(identifier, name, length, label)

def glClearBufferuiv(buffer, drawbuffer, value):
	return lib.glClearBufferuiv(buffer, drawbuffer, value)

def glVertexAttribIPointer(index, size, type, stride, pointer):
	return lib.glVertexAttribIPointer(index, size, type, stride, pointer)

def glFlush():
	return lib.glFlush()

def glGetTexLevelParameteriv(target, level, pname):
	params = ffi.new('GLint *')
	return lib.glGetTexLevelParameteriv(target, level, pname, params)

def glTexStorage3DMultisample(target, samples, internalformat, width, height, depth, fixedsamplelocations):
	return lib.glTexStorage3DMultisample(target, samples, internalformat, width, height, depth, fixedsamplelocations)

def glClearStencil(s):
	return lib.glClearStencil(s)

def glIsTexture(texture):
	return lib.glIsTexture(texture)

def glPolygonOffset(factor, units):
	return lib.glPolygonOffset(factor, units)

def glTexImage3D(target, level, internalformat, width, height, depth, border, format, type):
	pixels = ffi.new('const void *')
	return lib.glTexImage3D(target, level, internalformat, width, height, depth, border, format, type, pixels)

def glGetProgramiv(program, pname):
	params = ffi.new('GLint *')
	return lib.glGetProgramiv(program, pname, params)

def glProgramUniform4fv(program, location, count, value):
	return lib.glProgramUniform4fv(program, location, count, value)

def glBlendBarrier():
	return lib.glBlendBarrier()

def glFlushMappedBufferRange(target, offset, length):
	return lib.glFlushMappedBufferRange(target, offset, length)

def glTexStorage2D(target, levels, internalformat, width, height):
	return lib.glTexStorage2D(target, levels, internalformat, width, height)

def glGenQueries(n, ids):
	return lib.glGenQueries(n, ids)

def glTexSubImage3D(target, level, xoffset, yoffset, zoffset, width, height, depth, format, type):
	pixels = ffi.new('const void *')
	return lib.glTexSubImage3D(target, level, xoffset, yoffset, zoffset, width, height, depth, format, type, pixels)

def glDeleteSamplers(count, samplers):
	return lib.glDeleteSamplers(count, samplers)

def glUniform3fv(location, count, value):
	return lib.glUniform3fv(location, count, value)

def glDrawBuffers(n, bufs):
	return lib.glDrawBuffers(n, bufs)

def glBindTransformFeedback(target, id):
	return lib.glBindTransformFeedback(target, id)

def glUniform2uiv(location, count, value):
	return lib.glUniform2uiv(location, count, value)

def glFinish():
	return lib.glFinish()

def glUniform1uiv(location, count, value):
	return lib.glUniform1uiv(location, count, value)

def glDeleteQueries(n, ids):
	return lib.glDeleteQueries(n, ids)

def glGetVertexAttribfv(index, pname):
	params = ffi.new('GLfloat *')
	return lib.glGetVertexAttribfv(index, pname, params)

def glDispatchCompute(num_groups_x, num_groups_y, num_groups_z):
	return lib.glDispatchCompute(num_groups_x, num_groups_y, num_groups_z)

def glGetActiveAttrib(program, index, bufSize, length, size, type):
	name = ffi.new('GLchar *')
	return lib.glGetActiveAttrib(program, index, bufSize, length, size, type, name)

def glUniform3i(location, v0, v1, v2):
	return lib.glUniform3i(location, v0, v1, v2)

def glTexSubImage2D(target, level, xoffset, yoffset, width, height, format, type):
	pixels = ffi.new('const void *')
	return lib.glTexSubImage2D(target, level, xoffset, yoffset, width, height, format, type, pixels)

def glProgramUniformMatrix3x4fv(program, location, count, transpose, value):
	return lib.glProgramUniformMatrix3x4fv(program, location, count, transpose, value)

def glUniform3ui(location, v0, v1, v2):
	return lib.glUniform3ui(location, v0, v1, v2)

def glShaderBinary(count, shaders, binaryformat, binary, length):
	return lib.glShaderBinary(count, shaders, binaryformat, binary, length)

def glDrawElements(mode, count, type, indices):
	return lib.glDrawElements(mode, count, type, indices)

def glProgramUniform4iv(program, location, count, value):
	return lib.glProgramUniform4iv(program, location, count, value)

def glUniform1iv(location, count, value):
	return lib.glUniform1iv(location, count, value)

def glDrawArraysInstanced(mode, first, count, instancecount):
	return lib.glDrawArraysInstanced(mode, first, count, instancecount)

def glProgramUniform1iv(program, location, count, value):
	return lib.glProgramUniform1iv(program, location, count, value)

def glBindRenderbuffer(target, renderbuffer):
	return lib.glBindRenderbuffer(target, renderbuffer)

def glIsProgram(program):
	return lib.glIsProgram(program)

def glVertexAttrib4fv(index, v):
	return lib.glVertexAttrib4fv(index, v)

def glVertexAttrib2fv(index, v):
	return lib.glVertexAttrib2fv(index, v)

def glProgramUniform3i(program, location, v0, v1, v2):
	return lib.glProgramUniform3i(program, location, v0, v1, v2)

def glGetInteger64v(pname):
	data = ffi.new('GLint64 *')
	return lib.glGetInteger64v(pname, data)

def glClearBufferiv(buffer, drawbuffer, value):
	return lib.glClearBufferiv(buffer, drawbuffer, value)

def glGetSamplerParameterIuiv(sampler, pname):
	params = ffi.new('GLuint *')
	return lib.glGetSamplerParameterIuiv(sampler, pname, params)

def glUniform2f(location, v0, v1):
	return lib.glUniform2f(location, v0, v1)

def glClearDepthf(d):
	return lib.glClearDepthf(d)

def glVertexAttribI4ui(index, x, y, z, w):
	return lib.glVertexAttribI4ui(index, x, y, z, w)

def glColorMask(red, green, blue, alpha):
	return lib.glColorMask(red, green, blue, alpha)

def glBlendEquation(mode):
	return lib.glBlendEquation(mode)

def glGetProgramResourceiv(program, programInterface, index, propCount, props, bufSize, length):
	params = ffi.new('GLint *')
	return lib.glGetProgramResourceiv(program, programInterface, index, propCount, props, bufSize, length, params)

def glBeginTransformFeedback(primitiveMode):
	return lib.glBeginTransformFeedback(primitiveMode)

def glDeleteTransformFeedbacks(n, ids):
	return lib.glDeleteTransformFeedbacks(n, ids)

def glDrawRangeElementsBaseVertex(mode, start, end, count, type, indices, basevertex):
	return lib.glDrawRangeElementsBaseVertex(mode, start, end, count, type, indices, basevertex)

def glBindAttribLocation(program, index):
	name = ffi.new('const GLchar *')
	return lib.glBindAttribLocation(program, index, name)

def glBlendFuncSeparatei(buf, srcRGB, dstRGB, srcAlpha, dstAlpha):
	return lib.glBlendFuncSeparatei(buf, srcRGB, dstRGB, srcAlpha, dstAlpha)

def glUniform2ui(location, v0, v1):
	return lib.glUniform2ui(location, v0, v1)

def glDisablei(target, index):
	return lib.glDisablei(target, index)

def glGetSynciv(sync, pname, bufSize, length):
	values = ffi.new('GLint *')
	return lib.glGetSynciv(sync, pname, bufSize, length, values)

def glProgramUniform2i(program, location, v0, v1):
	return lib.glProgramUniform2i(program, location, v0, v1)

def glGetProgramBinary(program, bufSize, length, binaryFormat, binary):
	return lib.glGetProgramBinary(program, bufSize, length, binaryFormat, binary)

def glPauseTransformFeedback():
	return lib.glPauseTransformFeedback()

def glVertexAttribI4iv(index, v):
	return lib.glVertexAttribI4iv(index, v)

def glTexParameterfv(target, pname):
	params = ffi.new('const GLfloat *')
	return lib.glTexParameterfv(target, pname, params)

def glStencilFuncSeparate(face, func, ref, mask):
	return lib.glStencilFuncSeparate(face, func, ref, mask)

def glProgramUniform3fv(program, location, count, value):
	return lib.glProgramUniform3fv(program, location, count, value)

def glProgramUniform1fv(program, location, count, value):
	return lib.glProgramUniform1fv(program, location, count, value)

def glUniformMatrix4fv(location, count, transpose, value):
	return lib.glUniformMatrix4fv(location, count, transpose, value)

def glDeleteProgramPipelines(n, pipelines):
	return lib.glDeleteProgramPipelines(n, pipelines)

def glCompileShader(shader):
	return lib.glCompileShader(shader)

def glInvalidateFramebuffer(target, numAttachments, attachments):
	return lib.glInvalidateFramebuffer(target, numAttachments, attachments)

def glCompressedTexImage2D(target, level, internalformat, width, height, border, imageSize):
	data = ffi.new('const void *')
	return lib.glCompressedTexImage2D(target, level, internalformat, width, height, border, imageSize, data)

def glVertexAttrib1f(index, x):
	return lib.glVertexAttrib1f(index, x)

def glDeleteProgram(program):
	return lib.glDeleteProgram(program)

def glUniformMatrix4x3fv(location, count, transpose, value):
	return lib.glUniformMatrix4x3fv(location, count, transpose, value)

def glClearBufferfv(buffer, drawbuffer, value):
	return lib.glClearBufferfv(buffer, drawbuffer, value)

def glClearBufferfi(buffer, drawbuffer, depth, stencil):
	return lib.glClearBufferfi(buffer, drawbuffer, depth, stencil)

def glDrawArraysIndirect(mode, indirect):
	return lib.glDrawArraysIndirect(mode, indirect)

def glGenVertexArrays(n, arrays):
	return lib.glGenVertexArrays(n, arrays)

def glVertexBindingDivisor(bindingindex, divisor):
	return lib.glVertexBindingDivisor(bindingindex, divisor)

def glGetSamplerParameterIiv(sampler, pname):
	params = ffi.new('GLint *')
	return lib.glGetSamplerParameterIiv(sampler, pname, params)

def glUniformMatrix4x2fv(location, count, transpose, value):
	return lib.glUniformMatrix4x2fv(location, count, transpose, value)

def glVertexAttrib3f(index, x, y, z):
	return lib.glVertexAttrib3f(index, x, y, z)

def glUniform1ui(location, v0):
	return lib.glUniform1ui(location, v0)

def glMemoryBarrier(barriers):
	return lib.glMemoryBarrier(barriers)

def glGetFragDataLocation(program):
	name = ffi.new('const GLchar *')
	return lib.glGetFragDataLocation(program, name)

def glIsShader(shader):
	return lib.glIsShader(shader)

def glEnable(cap):
	return lib.glEnable(cap)

def glGetActiveUniformsiv(program, uniformCount, uniformIndices, pname):
	params = ffi.new('GLint *')
	return lib.glGetActiveUniformsiv(program, uniformCount, uniformIndices, pname, params)

def glBlendEquationi(buf, mode):
	return lib.glBlendEquationi(buf, mode)

def glGetAttribLocation(program):
	name = ffi.new('const GLchar *')
	return lib.glGetAttribLocation(program, name)

def glProgramUniform3ui(program, location, v0, v1, v2):
	return lib.glProgramUniform3ui(program, location, v0, v1, v2)

def glProgramUniformMatrix2x3fv(program, location, count, transpose, value):
	return lib.glProgramUniformMatrix2x3fv(program, location, count, transpose, value)

def glProgramUniform1i(program, location, v0):
	return lib.glProgramUniform1i(program, location, v0)

def glProgramUniform1f(program, location, v0):
	return lib.glProgramUniform1f(program, location, v0)

def glProgramUniform3iv(program, location, count, value):
	return lib.glProgramUniform3iv(program, location, count, value)

def glUniform4iv(location, count, value):
	return lib.glUniform4iv(location, count, value)

def glGenTextures(n, textures):
	return lib.glGenTextures(n, textures)

def glVertexAttribPointer(index, size, type, normalized, stride, pointer):
	return lib.glVertexAttribPointer(index, size, type, normalized, stride, pointer)

def glUniform1f(location, v0):
	return lib.glUniform1f(location, v0)

def glUniform2iv(location, count, value):
	return lib.glUniform2iv(location, count, value)

def glGetShaderiv(shader, pname):
	params = ffi.new('GLint *')
	return lib.glGetShaderiv(shader, pname, params)

def glCompressedTexImage3D(target, level, internalformat, width, height, depth, border, imageSize):
	data = ffi.new('const void *')
	return lib.glCompressedTexImage3D(target, level, internalformat, width, height, depth, border, imageSize, data)

def glGetVertexAttribiv(index, pname):
	params = ffi.new('GLint *')
	return lib.glGetVertexAttribiv(index, pname, params)

def glUniformMatrix2fv(location, count, transpose, value):
	return lib.glUniformMatrix2fv(location, count, transpose, value)

def glGetTexParameterIiv(target, pname):
	params = ffi.new('GLint *')
	return lib.glGetTexParameterIiv(target, pname, params)

def glDebugMessageCallback(callback, userParam):
	return lib.glDebugMessageCallback(callback, userParam)

def glGetBooleani_v(target, index):
	data = ffi.new('GLboolean *')
	return lib.glGetBooleani_v(target, index, data)

def glHint(target, mode):
	return lib.glHint(target, mode)

def glGetProgramResourceName(program, programInterface, index, bufSize, length):
	name = ffi.new('GLchar *')
	return lib.glGetProgramResourceName(program, programInterface, index, bufSize, length, name)

def glStencilOpSeparate(face, sfail, dpfail, dppass):
	return lib.glStencilOpSeparate(face, sfail, dpfail, dppass)

def glGetTexParameteriv(target, pname):
	params = ffi.new('GLint *')
	return lib.glGetTexParameteriv(target, pname, params)

def glGetVertexAttribPointerv(index, pname, pointer):
	return lib.glGetVertexAttribPointerv(index, pname, pointer)

def glDisable(cap):
	return lib.glDisable(cap)

def glProgramUniform4uiv(program, location, count, value):
	return lib.glProgramUniform4uiv(program, location, count, value)

def glUniform3uiv(location, count, value):
	return lib.glUniform3uiv(location, count, value)

def glBlendColor(red, green, blue, alpha):
	return lib.glBlendColor(red, green, blue, alpha)

def glSamplerParameterIuiv(sampler, pname, param):
	return lib.glSamplerParameterIuiv(sampler, pname, param)

def glUniform4i(location, v0, v1, v2, v3):
	return lib.glUniform4i(location, v0, v1, v2, v3)

def glActiveTexture(texture):
	return lib.glActiveTexture(texture)

def glEnableVertexAttribArray(index):
	return lib.glEnableVertexAttribArray(index)

def glUniform4f(location, v0, v1, v2, v3):
	return lib.glUniform4f(location, v0, v1, v2, v3)

def glRenderbufferStorageMultisample(target, samples, internalformat, width, height):
	return lib.glRenderbufferStorageMultisample(target, samples, internalformat, width, height)

def glDrawElementsInstancedBaseVertex(mode, count, type, indices, instancecount, basevertex):
	return lib.glDrawElementsInstancedBaseVertex(mode, count, type, indices, instancecount, basevertex)

def glPopDebugGroup():
	return lib.glPopDebugGroup()

def glUniformBlockBinding(program, uniformBlockIndex, uniformBlockBinding):
	return lib.glUniformBlockBinding(program, uniformBlockIndex, uniformBlockBinding)

def glBufferSubData(target, offset, size):
	data = ffi.new('const void *')
	return lib.glBufferSubData(target, offset, size, data)

def glProgramUniformMatrix3x2fv(program, location, count, transpose, value):
	return lib.glProgramUniformMatrix3x2fv(program, location, count, transpose, value)

def glBlendFunc(sfactor, dfactor):
	return lib.glBlendFunc(sfactor, dfactor)

def glCreateProgram():
	return lib.glCreateProgram()

def glProgramUniformMatrix2fv(program, location, count, transpose, value):
	return lib.glProgramUniformMatrix2fv(program, location, count, transpose, value)

def glSamplerParameteriv(sampler, pname, param):
	return lib.glSamplerParameteriv(sampler, pname, param)

def glClearColor(red, green, blue, alpha):
	return lib.glClearColor(red, green, blue, alpha)

def glGetnUniformiv(program, location, bufSize):
	params = ffi.new('GLint *')
	return lib.glGetnUniformiv(program, location, bufSize, params)

def glStencilMask(mask):
	return lib.glStencilMask(mask)

def glVertexAttribI4uiv(index, v):
	return lib.glVertexAttribI4uiv(index, v)

def glGetProgramResourceIndex(program, programInterface):
	name = ffi.new('const GLchar *')
	return lib.glGetProgramResourceIndex(program, programInterface, name)

def glUniformMatrix2x3fv(location, count, transpose, value):
	return lib.glUniformMatrix2x3fv(location, count, transpose, value)

def glGenTransformFeedbacks(n, ids):
	return lib.glGenTransformFeedbacks(n, ids)

def glGetVertexAttribIuiv(index, pname):
	params = ffi.new('GLuint *')
	return lib.glGetVertexAttribIuiv(index, pname, params)

def glCompressedTexSubImage2D(target, level, xoffset, yoffset, width, height, format, imageSize):
	data = ffi.new('const void *')
	return lib.glCompressedTexSubImage2D(target, level, xoffset, yoffset, width, height, format, imageSize, data)

def glProgramBinary(program, binaryFormat, binary, length):
	return lib.glProgramBinary(program, binaryFormat, binary, length)

def glGetTexParameterfv(target, pname):
	params = ffi.new('GLfloat *')
	return lib.glGetTexParameterfv(target, pname, params)

def glTexParameterIiv(target, pname):
	params = ffi.new('const GLint *')
	return lib.glTexParameterIiv(target, pname, params)

def glEndTransformFeedback():
	return lib.glEndTransformFeedback()

def glVertexAttribDivisor(index, divisor):
	return lib.glVertexAttribDivisor(index, divisor)

def glMapBufferRange(target, offset, length, access):
	return lib.glMapBufferRange(target, offset, length, access)

def glProgramUniformMatrix4x2fv(program, location, count, transpose, value):
	return lib.glProgramUniformMatrix4x2fv(program, location, count, transpose, value)

def glGetShaderPrecisionFormat(shadertype, precisiontype, range, precision):
	return lib.glGetShaderPrecisionFormat(shadertype, precisiontype, range, precision)

def glShaderSource(shader, count, conststring, length):
	return lib.glShaderSource(shader, count, conststring, length)

def glDeleteRenderbuffers(n, renderbuffers):
	return lib.glDeleteRenderbuffers(n, renderbuffers)

def glBufferData(target, size, usage):
	data = ffi.new('const void *')
	return lib.glBufferData(target, size, data, usage)

def glFramebufferTexture2D(target, attachment, textarget, texture, level):
	return lib.glFramebufferTexture2D(target, attachment, textarget, texture, level)

def glGetBufferPointerv(target, pname):
	params = ffi.new('void *')
	return lib.glGetBufferPointerv(target, pname, params)

def glSamplerParameterfv(sampler, pname, param):
	return lib.glSamplerParameterfv(sampler, pname, param)

def glUniform1fv(location, count, value):
	return lib.glUniform1fv(location, count, value)

def glVertexAttrib2f(index, x, y):
	return lib.glVertexAttrib2f(index, x, y)

def glGetUniformBlockIndex(program, uniformBlockName):
	return lib.glGetUniformBlockIndex(program, uniformBlockName)

def glFrontFace(mode):
	return lib.glFrontFace(mode)

