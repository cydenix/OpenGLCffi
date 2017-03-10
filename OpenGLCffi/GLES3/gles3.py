@params('face', 'mask')
def glStencilMaskSeparate(face, mask):
	pass


@params('target', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth', 'format', 'imageSize', 'data')
def glCompressedTexSubImage3D(target, level, xoffset, yoffset, zoffset, width, height, depth, format, imageSize):
	pass


@params('buffer',)
def glIsBuffer(buffer):
	pass


@params('pname', 'index', 'val')
def glGetMultisamplefv(pname, index, val):
	pass


@params('program', 'location', 'count', 'transpose', 'value')
def glProgramUniformMatrix4fv(program, location, count, transpose, value):
	pass


@params('source', 'type', 'severity', 'count', 'ids', 'enabled')
def glDebugMessageControl(source, type, severity, count, ids, enabled):
	pass


@params('target', 'internalformat', 'width', 'height')
def glRenderbufferStorage(target, internalformat, width, height):
	pass


@params('program', 'location', 'v0', 'v1', 'v2')
def glProgramUniform3f(program, location, v0, v1, v2):
	pass


@params()
def glResumeTransformFeedback():
	pass


@params()
def glGetGraphicsResetStatus():
	pass


@params('index', 'v')
def glVertexAttrib1fv(index, v):
	pass


@params('cap',)
def glIsEnabled(cap):
	pass


@params('fail', 'zfail', 'zpass')
def glStencilOp(fail, zfail, zpass):
	pass


@params('n', 'framebuffers')
def glGenFramebuffers(n, framebuffers):
	pass


@params('program', 'maxCount', 'count', 'shaders')
def glGetAttachedShaders(program, maxCount, count, shaders):
	pass


@params('n', 'arrays')
def glDeleteVertexArrays(n, arrays):
	pass


@params('pname', 'params')
def glGetPointerv(pname):
	pass


@params('program', 'location', 'params')
def glGetUniformfv(program, location):
	pass


@params('program', 'location', 'params')
def glGetUniformuiv(program, location):
	pass


@params('program', 'location', 'count', 'transpose', 'value')
def glProgramUniformMatrix3fv(program, location, count, transpose, value):
	pass


@params('mode', 'count', 'type', 'indices', 'instancecount')
def glDrawElementsInstanced(mode, count, type, indices, instancecount):
	pass


@params('target', 'pname', 'params')
def glGetRenderbufferParameteriv(target, pname):
	pass


@params('condition', 'flags')
def glFenceSync(condition, flags):
	pass


@params('pipeline',)
def glValidateProgramPipeline(pipeline):
	pass


@params('count', 'samplers')
def glGenSamplers(count, samplers):
	pass


@params('target', 'pname', 'params')
def glGetTexParameterIuiv(target, pname):
	pass


@params('sync',)
def glIsSync(sync):
	pass


@params('ptr', 'bufSize', 'length', 'label')
def glGetObjectPtrLabel(ptr, bufSize, length, label):
	pass


@params('target', 'level', 'internalformat', 'x', 'y', 'width', 'height', 'border')
def glCopyTexImage2D(target, level, internalformat, x, y, width, height, border):
	pass


@params('location', 'count', 'value')
def glUniform4uiv(location, count, value):
	pass


@params('target', 'numAttachments', 'attachments', 'x', 'y', 'width', 'height')
def glInvalidateSubFramebuffer(target, numAttachments, attachments, x, y, width, height):
	pass


@params('sync',)
def glDeleteSync(sync):
	pass


@params('location', 'count', 'value')
def glUniform3iv(location, count, value):
	pass


@params('program',)
def glUseProgram(program):
	pass


@params('program', 'bufSize', 'length', 'infoLog')
def glGetProgramInfoLog(program, bufSize, length, infoLog):
	pass


@params('pname', 'data')
def glGetBooleanv(pname):
	pass


@params('shader',)
def glDeleteShader(shader):
	pass


@params('attribindex', 'size', 'type', 'normalized', 'relativeoffset')
def glVertexAttribFormat(attribindex, size, type, normalized, relativeoffset):
	pass


@params('target', 'pname', 'param')
def glTexParameterf(target, pname, param):
	pass


@params('attribindex', 'bindingindex')
def glVertexAttribBinding(attribindex, bindingindex):
	pass


@params('target', 'pname', 'param')
def glTexParameteri(target, pname, param):
	pass


@params('shader', 'bufSize', 'length', 'source')
def glGetShaderSource(shader, bufSize, length, source):
	pass


@params('n', 'pipelines')
def glGenProgramPipelines(n, pipelines):
	pass


@params('index', 'v')
def glVertexAttrib3fv(index, v):
	pass


@params('program',)
def glLinkProgram(program):
	pass


@params('identifier', 'name', 'bufSize', 'length', 'label')
def glGetObjectLabel(identifier, bufSize, length, label):
	pass


@params('name',)
def glGetString():
	pass


@params('target',)
def glEndQuery(target):
	pass


@params('target', 'pname', 'param')
def glFramebufferParameteri(target, pname, param):
	pass


@params('n', 'textures')
def glDeleteTextures(n, textures):
	pass


@params('index', 'x', 'y', 'z', 'w')
def glVertexAttrib4f(index, x, y, z, w):
	pass


@params('sampler', 'pname', 'param')
def glSamplerParameteri(sampler, pname, param):
	pass


@params('program', 'uniformBlockIndex', 'pname', 'params')
def glGetActiveUniformBlockiv(program, uniformBlockIndex, pname):
	pass


@params('location', 'v0')
def glUniform1i(location, v0):
	pass


@params('mode',)
def glCullFace(mode):
	pass


@params('program', 'location', 'v0', 'v1', 'v2', 'v3')
def glProgramUniform4i(program, location, v0, v1, v2, v3):
	pass


@params('program', 'location', 'v0', 'v1', 'v2', 'v3')
def glProgramUniform4f(program, location, v0, v1, v2, v3):
	pass


@params('program', 'shader')
def glAttachShader(program, shader):
	pass


@params('target', 'pname', 'params')
def glGetBufferParameteriv(target, pname):
	pass


@params('target', 'pname', 'params')
def glTexParameterIuiv(target, pname):
	pass


@params('id',)
def glIsTransformFeedback(id):
	pass


@params('pipeline',)
def glIsProgramPipeline(pipeline):
	pass


@params('location', 'count', 'transpose', 'value')
def glUniformMatrix3fv(location, count, transpose, value):
	pass


@params('program', 'location', 'bufSize', 'params')
def glGetnUniformfv(program, location, bufSize):
	pass


@params('func', 'ref', 'mask')
def glStencilFunc(func, ref, mask):
	pass


@params('pipeline', 'pname', 'params')
def glGetProgramPipelineiv(pipeline, pname):
	pass


@params('indirect',)
def glDispatchComputeIndirect(indirect):
	pass


@params('shader', 'bufSize', 'length', 'infoLog')
def glGetShaderInfoLog(shader, bufSize, length, infoLog):
	pass


@params('index', 'x', 'y', 'z', 'w')
def glVertexAttribI4i(index, x, y, z, w):
	pass


@params('modeRGB', 'modeAlpha')
def glBlendEquationSeparate(modeRGB, modeAlpha):
	pass


@params('n', 'buffers')
def glDeleteBuffers(n, buffers):
	pass


@params('pipeline',)
def glBindProgramPipeline(pipeline):
	pass


@params('x', 'y', 'width', 'height')
def glScissor(x, y, width, height):
	pass


@params('name', 'index')
def glGetStringi(index):
	pass


@params('location', 'count', 'value')
def glUniform2fv(location, count, value):
	pass


@params('target', 'index', 'buffer', 'offset', 'size')
def glBindBufferRange(target, index, buffer, offset, size):
	pass


@params('sync', 'flags', 'timeout')
def glClientWaitSync(sync, flags, timeout):
	pass


@params('x', 'y', 'width', 'height', 'format', 'type', 'bufSize', 'data')
def glReadnPixels(x, y, width, height, format, type, bufSize):
	pass


@params('srcName', 'srcTarget', 'srcLevel', 'srcX', 'srcY', 'srcZ', 'dstName', 'dstTarget', 'dstLevel', 'dstX', 'dstY', 'dstZ', 'srcWidth', 'srcHeight', 'srcDepth')
def glCopyImageSubData(srcName, srcTarget, srcLevel, srcX, srcY, srcZ, dstName, dstTarget, dstLevel, dstX, dstY, dstZ, srcWidth, srcHeight, srcDepth):
	pass


@params('bindingindex', 'buffer', 'offset', 'stride')
def glBindVertexBuffer(bindingindex, buffer, offset, stride):
	pass


@params('source', 'type', 'id', 'severity', 'length', 'buf')
def glDebugMessageInsert(source, type, id, severity, length, buf):
	pass


@params('sampler',)
def glIsSampler(sampler):
	pass


@params('target',)
def glCheckFramebufferStatus(target):
	pass


@params('unit', 'texture', 'level', 'layered', 'layer', 'access', 'format')
def glBindImageTexture(unit, texture, level, layered, layer, access, format):
	pass


@params('program', 'count', 'constvaryings', 'bufferMode')
def glTransformFeedbackVaryings(program, count, constvaryings, bufferMode):
	pass


@params('mode', 'start', 'end', 'count', 'type', 'indices')
def glDrawRangeElements(mode, start, end, count, type, indices):
	pass


@params('target', 'index', 'buffer')
def glBindBufferBase(target, index, buffer):
	pass


@params('attribindex', 'size', 'type', 'relativeoffset')
def glVertexAttribIFormat(attribindex, size, type, relativeoffset):
	pass


@params('target', 'id')
def glBeginQuery(target, id):
	pass


@params('location', 'count', 'transpose', 'value')
def glUniformMatrix2x4fv(location, count, transpose, value):
	pass


@params()
def glGetError():
	pass


@params('target', 'level', 'pname', 'params')
def glGetTexLevelParameterfv(target, level, pname):
	pass


@params('program', 'location', 'v0', 'v1')
def glProgramUniform2ui(program, location, v0, v1):
	pass


@params('program', 'location', 'v0', 'v1', 'v2', 'v3')
def glProgramUniform4ui(program, location, v0, v1, v2, v3):
	pass


@params('pname', 'param')
def glPixelStorei(pname, param):
	pass


@params('flag',)
def glDepthMask(flag):
	pass


@params('target', 'internalformat', 'buffer', 'offset', 'size')
def glTexBufferRange(target, internalformat, buffer, offset, size):
	pass


@params('program', 'pname', 'value')
def glProgramParameteri(program, pname, value):
	pass


@params('barriers',)
def glMemoryBarrierByRegion(barriers):
	pass


@params('type',)
def glCreateShader(type):
	pass


@params('n', 'renderbuffers')
def glGenRenderbuffers(n, renderbuffers):
	pass


@params('target', 'level', 'xoffset', 'yoffset', 'x', 'y', 'width', 'height')
def glCopyTexSubImage2D(target, level, xoffset, yoffset, x, y, width, height):
	pass


@params('sfactorRGB', 'dfactorRGB', 'sfactorAlpha', 'dfactorAlpha')
def glBlendFuncSeparate(sfactorRGB, dfactorRGB, sfactorAlpha, dfactorAlpha):
	pass


@params('pipeline', 'bufSize', 'length', 'infoLog')
def glGetProgramPipelineInfoLog(pipeline, bufSize, length, infoLog):
	pass


@params('sync', 'flags', 'timeout')
def glWaitSync(sync, flags, timeout):
	pass


@params('buf', 'modeRGB', 'modeAlpha')
def glBlendEquationSeparatei(buf, modeRGB, modeAlpha):
	pass


@params('location', 'v0', 'v1', 'v2')
def glUniform3f(location, v0, v1, v2):
	pass


@params('program', 'location', 'count', 'value')
def glProgramUniform3uiv(program, location, count, value):
	pass


@params('n', 'framebuffers')
def glDeleteFramebuffers(n, framebuffers):
	pass


@params('mode', 'first', 'count')
def glDrawArrays(mode, first, count):
	pass


@params('mask',)
def glClear(mask):
	pass


@params('sampler', 'pname', 'params')
def glGetSamplerParameterfv(sampler, pname):
	pass


@params('sampler', 'pname', 'param')
def glSamplerParameterIiv(sampler, pname, param):
	pass


@params('mode', 'type', 'indirect')
def glDrawElementsIndirect(mode, type, indirect):
	pass


@params('program', 'uniformCount', 'constuniformNames', 'uniformIndices')
def glGetUniformIndices(program, uniformCount, constuniformNames, uniformIndices):
	pass


@params('array',)
def glIsVertexArray(array):
	pass


@params('index',)
def glDisableVertexAttribArray(index):
	pass


@params('program', 'programInterface', 'pname', 'params')
def glGetProgramInterfaceiv(program, programInterface, pname):
	pass


@params('index', 'pname', 'params')
def glGetVertexAttribIiv(index, pname):
	pass


@params('pname', 'value')
def glPatchParameteri(pname, value):
	pass


@params('value', 'invert')
def glSampleCoverage(value, invert):
	pass


@params('location', 'v0', 'v1')
def glUniform2i(location, v0, v1):
	pass


@params('target', 'attachment', 'texture', 'level', 'layer')
def glFramebufferTextureLayer(target, attachment, texture, level, layer):
	pass


@params('program', 'location', 'count', 'value')
def glProgramUniform2fv(program, location, count, value):
	pass


@params('minX', 'minY', 'minZ', 'minW', 'maxX', 'maxY', 'maxZ', 'maxW')
def glPrimitiveBoundingBox(minX, minY, minZ, minW, maxX, maxY, maxZ, maxW):
	pass


@params('target', 'index', 'data')
def glGetInteger64i_v(target, index):
	pass


@params('srcX0', 'srcY0', 'srcX1', 'srcY1', 'dstX0', 'dstY0', 'dstX1', 'dstY1', 'mask', 'filter')
def glBlitFramebuffer(srcX0, srcY0, srcX1, srcY1, dstX0, dstY0, dstX1, dstY1, mask, filter):
	pass


@params('target', 'index')
def glIsEnabledi(target, index):
	pass


@params('ptr', 'length', 'label')
def glObjectPtrLabel(ptr, length, label):
	pass


@params('count', 'bufSize', 'sources', 'types', 'ids', 'severities', 'lengths', 'messageLog')
def glGetDebugMessageLog(count, bufSize, sources, types, ids, severities, lengths, messageLog):
	pass


@params('source', 'id', 'length', 'message')
def glPushDebugGroup(source, id, length, message):
	pass


@params('target', 'level', 'xoffset', 'yoffset', 'zoffset', 'x', 'y', 'width', 'height')
def glCopyTexSubImage3D(target, level, xoffset, yoffset, zoffset, x, y, width, height):
	pass


@params('program', 'uniformBlockIndex', 'bufSize', 'length', 'uniformBlockName')
def glGetActiveUniformBlockName(program, uniformBlockIndex, bufSize, length, uniformBlockName):
	pass


@params('program', 'location', 'v0', 'v1')
def glProgramUniform2f(program, location, v0, v1):
	pass


@params('array',)
def glBindVertexArray(array):
	pass


@params('target', 'framebuffer')
def glBindFramebuffer(target, framebuffer):
	pass


@params('x', 'y', 'width', 'height')
def glViewport(x, y, width, height):
	pass


@params('renderbuffer',)
def glIsRenderbuffer(renderbuffer):
	pass


@params('target', 'samples', 'internalformat', 'width', 'height', 'fixedsamplelocations')
def glTexStorage2DMultisample(target, samples, internalformat, width, height, fixedsamplelocations):
	pass


@params('target', 'internalformat', 'buffer')
def glTexBuffer(target, internalformat, buffer):
	pass


@params('program',)
def glValidateProgram(program):
	pass


@params('pipeline', 'program')
def glActiveShaderProgram(pipeline, program):
	pass


@params('target', 'texture')
def glBindTexture(target, texture):
	pass


@params('program', 'shader')
def glDetachShader(program, shader):
	pass


@params('program', 'programInterface', 'name')
def glGetProgramResourceLocation(program, programInterface):
	pass


@params('mode', 'count', 'type', 'indices', 'basevertex')
def glDrawElementsBaseVertex(mode, count, type, indices, basevertex):
	pass


@params('program', 'location', 'params')
def glGetUniformiv(program, location):
	pass


@params('target', 'buffer')
def glBindBuffer(target, buffer):
	pass


@params('location', 'v0', 'v1', 'v2', 'v3')
def glUniform4ui(location, v0, v1, v2, v3):
	pass


@params('type', 'count', 'conststrings')
def glCreateShaderProgramv(type, count, conststrings):
	pass


@params('target',)
def glGenerateMipmap(target):
	pass


@params('target',)
def glUnmapBuffer(target):
	pass


@params()
def glReleaseShaderCompiler():
	pass


@params('x', 'y', 'width', 'height', 'format', 'type', 'pixels')
def glReadPixels(x, y, width, height, format, type):
	pass


@params('pipeline', 'stages', 'program')
def glUseProgramStages(pipeline, stages, program):
	pass


@params('src',)
def glReadBuffer(src):
	pass


@params('program', 'location', 'bufSize', 'params')
def glGetnUniformuiv(program, location, bufSize):
	pass


@params('n', 'buffers')
def glGenBuffers(n, buffers):
	pass


@params('framebuffer',)
def glIsFramebuffer(framebuffer):
	pass


@params('target', 'pname', 'params')
def glGetBufferParameteri64v(target, pname):
	pass


@params('func',)
def glDepthFunc(func):
	pass


@params('sampler', 'pname', 'param')
def glSamplerParameterf(sampler, pname, param):
	pass


@params('buf', 'src', 'dst')
def glBlendFunci(buf, src, dst):
	pass


@params('program', 'name')
def glGetUniformLocation(program):
	pass


@params('location', 'count', 'value')
def glUniform4fv(location, count, value):
	pass


@params('program', 'location', 'count', 'value')
def glProgramUniform2uiv(program, location, count, value):
	pass


@params('id', 'pname', 'params')
def glGetQueryObjectuiv(id, pname):
	pass


@params('program', 'location', 'count', 'value')
def glProgramUniform1uiv(program, location, count, value):
	pass


@params('target', 'attachment', 'texture', 'level')
def glFramebufferTexture(target, attachment, texture, level):
	pass


@params('program', 'location', 'count', 'transpose', 'value')
def glProgramUniformMatrix2x4fv(program, location, count, transpose, value):
	pass


@params('pname', 'data')
def glGetFloatv(pname):
	pass


@params('pname', 'data')
def glGetIntegerv(pname):
	pass


@params('id',)
def glIsQuery(id):
	pass


@params('target', 'level', 'internalformat', 'width', 'height', 'border', 'format', 'type', 'pixels')
def glTexImage2D(target, level, internalformat, width, height, border, format, type):
	pass


@params('target', 'pname', 'params')
def glGetFramebufferParameteriv(target, pname):
	pass


@params('sampler', 'pname', 'params')
def glGetSamplerParameteriv(sampler, pname):
	pass


@params('readTarget', 'writeTarget', 'readOffset', 'writeOffset', 'size')
def glCopyBufferSubData(readTarget, writeTarget, readOffset, writeOffset, size):
	pass


@params('program', 'index', 'bufSize', 'length', 'size', 'type', 'name')
def glGetActiveUniform(program, index, bufSize, length, size, type):
	pass


@params('value',)
def glMinSampleShading(value):
	pass


@params('target', 'attachment', 'renderbuffertarget', 'renderbuffer')
def glFramebufferRenderbuffer(target, attachment, renderbuffertarget, renderbuffer):
	pass


@params('unit', 'sampler')
def glBindSampler(unit, sampler):
	pass


@params('width',)
def glLineWidth(width):
	pass


@params('target', 'index', 'data')
def glGetIntegeri_v(target, index):
	pass


@params('program', 'index', 'bufSize', 'length', 'size', 'type', 'name')
def glGetTransformFeedbackVarying(program, index, bufSize, length, size, type):
	pass


@params('n', 'f')
def glDepthRangef(n, f):
	pass


@params('target', 'index')
def glEnablei(target, index):
	pass


@params('maskNumber', 'mask')
def glSampleMaski(maskNumber, mask):
	pass


@params('location', 'count', 'transpose', 'value')
def glUniformMatrix3x2fv(location, count, transpose, value):
	pass


@params('target', 'internalformat', 'pname', 'bufSize', 'params')
def glGetInternalformativ(target, internalformat, pname, bufSize):
	pass


@params('program', 'location', 'v0')
def glProgramUniform1ui(program, location, v0):
	pass


@params('index', 'r', 'g', 'b', 'a')
def glColorMaski(index, r, g, b, a):
	pass


@params('target', 'levels', 'internalformat', 'width', 'height', 'depth')
def glTexStorage3D(target, levels, internalformat, width, height, depth):
	pass


@params('location', 'count', 'transpose', 'value')
def glUniformMatrix3x4fv(location, count, transpose, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value')
def glProgramUniformMatrix4x3fv(program, location, count, transpose, value):
	pass


@params('target', 'attachment', 'pname', 'params')
def glGetFramebufferAttachmentParameteriv(target, attachment, pname):
	pass


@params('target', 'pname', 'params')
def glTexParameteriv(target, pname):
	pass


@params('program', 'location', 'count', 'value')
def glProgramUniform2iv(program, location, count, value):
	pass


@params('target', 'pname', 'params')
def glGetQueryiv(target, pname):
	pass


@params('identifier', 'name', 'length', 'label')
def glObjectLabel(identifier, length, label):
	pass


@params('buffer', 'drawbuffer', 'value')
def glClearBufferuiv(buffer, drawbuffer, value):
	pass


@params('index', 'size', 'type', 'stride', 'pointer')
def glVertexAttribIPointer(index, size, type, stride, pointer):
	pass


@params()
def glFlush():
	pass


@params('target', 'level', 'pname', 'params')
def glGetTexLevelParameteriv(target, level, pname):
	pass


@params('target', 'samples', 'internalformat', 'width', 'height', 'depth', 'fixedsamplelocations')
def glTexStorage3DMultisample(target, samples, internalformat, width, height, depth, fixedsamplelocations):
	pass


@params('s',)
def glClearStencil(s):
	pass


@params('texture',)
def glIsTexture(texture):
	pass


@params('factor', 'units')
def glPolygonOffset(factor, units):
	pass


@params('target', 'level', 'internalformat', 'width', 'height', 'depth', 'border', 'format', 'type', 'pixels')
def glTexImage3D(target, level, internalformat, width, height, depth, border, format, type):
	pass


@params('program', 'pname', 'params')
def glGetProgramiv(program, pname):
	pass


@params('program', 'location', 'count', 'value')
def glProgramUniform4fv(program, location, count, value):
	pass


@params()
def glBlendBarrier():
	pass


@params('target', 'offset', 'length')
def glFlushMappedBufferRange(target, offset, length):
	pass


@params('target', 'levels', 'internalformat', 'width', 'height')
def glTexStorage2D(target, levels, internalformat, width, height):
	pass


@params('n', 'ids')
def glGenQueries(n, ids):
	pass


@params('target', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth', 'format', 'type', 'pixels')
def glTexSubImage3D(target, level, xoffset, yoffset, zoffset, width, height, depth, format, type):
	pass


@params('count', 'samplers')
def glDeleteSamplers(count, samplers):
	pass


@params('location', 'count', 'value')
def glUniform3fv(location, count, value):
	pass


@params('n', 'bufs')
def glDrawBuffers(n, bufs):
	pass


@params('target', 'id')
def glBindTransformFeedback(target, id):
	pass


@params('location', 'count', 'value')
def glUniform2uiv(location, count, value):
	pass


@params()
def glFinish():
	pass


@params('location', 'count', 'value')
def glUniform1uiv(location, count, value):
	pass


@params('n', 'ids')
def glDeleteQueries(n, ids):
	pass


@params('index', 'pname', 'params')
def glGetVertexAttribfv(index, pname):
	pass


@params('num_groups_x', 'num_groups_y', 'num_groups_z')
def glDispatchCompute(num_groups_x, num_groups_y, num_groups_z):
	pass


@params('program', 'index', 'bufSize', 'length', 'size', 'type', 'name')
def glGetActiveAttrib(program, index, bufSize, length, size, type):
	pass


@params('location', 'v0', 'v1', 'v2')
def glUniform3i(location, v0, v1, v2):
	pass


@params('target', 'level', 'xoffset', 'yoffset', 'width', 'height', 'format', 'type', 'pixels')
def glTexSubImage2D(target, level, xoffset, yoffset, width, height, format, type):
	pass


@params('program', 'location', 'count', 'transpose', 'value')
def glProgramUniformMatrix3x4fv(program, location, count, transpose, value):
	pass


@params('location', 'v0', 'v1', 'v2')
def glUniform3ui(location, v0, v1, v2):
	pass


@params('count', 'shaders', 'binaryformat', 'binary', 'length')
def glShaderBinary(count, shaders, binaryformat, binary, length):
	pass


@params('mode', 'count', 'type', 'indices')
def glDrawElements(mode, count, type, indices):
	pass


@params('program', 'location', 'count', 'value')
def glProgramUniform4iv(program, location, count, value):
	pass


@params('location', 'count', 'value')
def glUniform1iv(location, count, value):
	pass


@params('mode', 'first', 'count', 'instancecount')
def glDrawArraysInstanced(mode, first, count, instancecount):
	pass


@params('program', 'location', 'count', 'value')
def glProgramUniform1iv(program, location, count, value):
	pass


@params('target', 'renderbuffer')
def glBindRenderbuffer(target, renderbuffer):
	pass


@params('program',)
def glIsProgram(program):
	pass


@params('index', 'v')
def glVertexAttrib4fv(index, v):
	pass


@params('index', 'v')
def glVertexAttrib2fv(index, v):
	pass


@params('program', 'location', 'v0', 'v1', 'v2')
def glProgramUniform3i(program, location, v0, v1, v2):
	pass


@params('pname', 'data')
def glGetInteger64v(pname):
	pass


@params('buffer', 'drawbuffer', 'value')
def glClearBufferiv(buffer, drawbuffer, value):
	pass


@params('sampler', 'pname', 'params')
def glGetSamplerParameterIuiv(sampler, pname):
	pass


@params('location', 'v0', 'v1')
def glUniform2f(location, v0, v1):
	pass


@params('d',)
def glClearDepthf(d):
	pass


@params('index', 'x', 'y', 'z', 'w')
def glVertexAttribI4ui(index, x, y, z, w):
	pass


@params('red', 'green', 'blue', 'alpha')
def glColorMask(red, green, blue, alpha):
	pass


@params('mode',)
def glBlendEquation(mode):
	pass


@params('program', 'programInterface', 'index', 'propCount', 'props', 'bufSize', 'length', 'params')
def glGetProgramResourceiv(program, programInterface, index, propCount, props, bufSize, length):
	pass


@params('primitiveMode',)
def glBeginTransformFeedback(primitiveMode):
	pass


@params('n', 'ids')
def glDeleteTransformFeedbacks(n, ids):
	pass


@params('mode', 'start', 'end', 'count', 'type', 'indices', 'basevertex')
def glDrawRangeElementsBaseVertex(mode, start, end, count, type, indices, basevertex):
	pass


@params('program', 'index', 'name')
def glBindAttribLocation(program, index):
	pass


@params('buf', 'srcRGB', 'dstRGB', 'srcAlpha', 'dstAlpha')
def glBlendFuncSeparatei(buf, srcRGB, dstRGB, srcAlpha, dstAlpha):
	pass


@params('location', 'v0', 'v1')
def glUniform2ui(location, v0, v1):
	pass


@params('target', 'index')
def glDisablei(target, index):
	pass


@params('sync', 'pname', 'bufSize', 'length', 'values')
def glGetSynciv(sync, pname, bufSize, length):
	pass


@params('program', 'location', 'v0', 'v1')
def glProgramUniform2i(program, location, v0, v1):
	pass


@params('program', 'bufSize', 'length', 'binaryFormat', 'binary')
def glGetProgramBinary(program, bufSize, length, binaryFormat, binary):
	pass


@params()
def glPauseTransformFeedback():
	pass


@params('index', 'v')
def glVertexAttribI4iv(index, v):
	pass


@params('target', 'pname', 'params')
def glTexParameterfv(target, pname):
	pass


@params('face', 'func', 'ref', 'mask')
def glStencilFuncSeparate(face, func, ref, mask):
	pass


@params('program', 'location', 'count', 'value')
def glProgramUniform3fv(program, location, count, value):
	pass


@params('program', 'location', 'count', 'value')
def glProgramUniform1fv(program, location, count, value):
	pass


@params('location', 'count', 'transpose', 'value')
def glUniformMatrix4fv(location, count, transpose, value):
	pass


@params('n', 'pipelines')
def glDeleteProgramPipelines(n, pipelines):
	pass


@params('shader',)
def glCompileShader(shader):
	pass


@params('target', 'numAttachments', 'attachments')
def glInvalidateFramebuffer(target, numAttachments, attachments):
	pass


@params('target', 'level', 'internalformat', 'width', 'height', 'border', 'imageSize', 'data')
def glCompressedTexImage2D(target, level, internalformat, width, height, border, imageSize):
	pass


@params('index', 'x')
def glVertexAttrib1f(index, x):
	pass


@params('program',)
def glDeleteProgram(program):
	pass


@params('location', 'count', 'transpose', 'value')
def glUniformMatrix4x3fv(location, count, transpose, value):
	pass


@params('buffer', 'drawbuffer', 'value')
def glClearBufferfv(buffer, drawbuffer, value):
	pass


@params('buffer', 'drawbuffer', 'depth', 'stencil')
def glClearBufferfi(buffer, drawbuffer, depth, stencil):
	pass


@params('mode', 'indirect')
def glDrawArraysIndirect(mode, indirect):
	pass


@params('n', 'arrays')
def glGenVertexArrays(n, arrays):
	pass


@params('bindingindex', 'divisor')
def glVertexBindingDivisor(bindingindex, divisor):
	pass


@params('sampler', 'pname', 'params')
def glGetSamplerParameterIiv(sampler, pname):
	pass


@params('location', 'count', 'transpose', 'value')
def glUniformMatrix4x2fv(location, count, transpose, value):
	pass


@params('index', 'x', 'y', 'z')
def glVertexAttrib3f(index, x, y, z):
	pass


@params('location', 'v0')
def glUniform1ui(location, v0):
	pass


@params('barriers',)
def glMemoryBarrier(barriers):
	pass


@params('program', 'name')
def glGetFragDataLocation(program):
	pass


@params('shader',)
def glIsShader(shader):
	pass


@params('cap',)
def glEnable(cap):
	pass


@params('program', 'uniformCount', 'uniformIndices', 'pname', 'params')
def glGetActiveUniformsiv(program, uniformCount, uniformIndices, pname):
	pass


@params('buf', 'mode')
def glBlendEquationi(buf, mode):
	pass


@params('program', 'name')
def glGetAttribLocation(program):
	pass


@params('program', 'location', 'v0', 'v1', 'v2')
def glProgramUniform3ui(program, location, v0, v1, v2):
	pass


@params('program', 'location', 'count', 'transpose', 'value')
def glProgramUniformMatrix2x3fv(program, location, count, transpose, value):
	pass


@params('program', 'location', 'v0')
def glProgramUniform1i(program, location, v0):
	pass


@params('program', 'location', 'v0')
def glProgramUniform1f(program, location, v0):
	pass


@params('program', 'location', 'count', 'value')
def glProgramUniform3iv(program, location, count, value):
	pass


@params('location', 'count', 'value')
def glUniform4iv(location, count, value):
	pass


@params('n', 'textures')
def glGenTextures(n, textures):
	pass


@params('index', 'size', 'type', 'normalized', 'stride', 'pointer')
def glVertexAttribPointer(index, size, type, normalized, stride, pointer):
	pass


@params('location', 'v0')
def glUniform1f(location, v0):
	pass


@params('location', 'count', 'value')
def glUniform2iv(location, count, value):
	pass


@params('shader', 'pname', 'params')
def glGetShaderiv(shader, pname):
	pass


@params('target', 'level', 'internalformat', 'width', 'height', 'depth', 'border', 'imageSize', 'data')
def glCompressedTexImage3D(target, level, internalformat, width, height, depth, border, imageSize):
	pass


@params('index', 'pname', 'params')
def glGetVertexAttribiv(index, pname):
	pass


@params('location', 'count', 'transpose', 'value')
def glUniformMatrix2fv(location, count, transpose, value):
	pass


@params('target', 'pname', 'params')
def glGetTexParameterIiv(target, pname):
	pass


@params('callback', 'userParam')
def glDebugMessageCallback(callback, userParam):
	pass


@params('target', 'index', 'data')
def glGetBooleani_v(target, index):
	pass


@params('target', 'mode')
def glHint(target, mode):
	pass


@params('program', 'programInterface', 'index', 'bufSize', 'length', 'name')
def glGetProgramResourceName(program, programInterface, index, bufSize, length):
	pass


@params('face', 'sfail', 'dpfail', 'dppass')
def glStencilOpSeparate(face, sfail, dpfail, dppass):
	pass


@params('target', 'pname', 'params')
def glGetTexParameteriv(target, pname):
	pass


@params('index', 'pname', 'pointer')
def glGetVertexAttribPointerv(index, pname, pointer):
	pass


@params('cap',)
def glDisable(cap):
	pass


@params('program', 'location', 'count', 'value')
def glProgramUniform4uiv(program, location, count, value):
	pass


@params('location', 'count', 'value')
def glUniform3uiv(location, count, value):
	pass


@params('red', 'green', 'blue', 'alpha')
def glBlendColor(red, green, blue, alpha):
	pass


@params('sampler', 'pname', 'param')
def glSamplerParameterIuiv(sampler, pname, param):
	pass


@params('location', 'v0', 'v1', 'v2', 'v3')
def glUniform4i(location, v0, v1, v2, v3):
	pass


@params('texture',)
def glActiveTexture(texture):
	pass


@params('index',)
def glEnableVertexAttribArray(index):
	pass


@params('location', 'v0', 'v1', 'v2', 'v3')
def glUniform4f(location, v0, v1, v2, v3):
	pass


@params('target', 'samples', 'internalformat', 'width', 'height')
def glRenderbufferStorageMultisample(target, samples, internalformat, width, height):
	pass


@params('mode', 'count', 'type', 'indices', 'instancecount', 'basevertex')
def glDrawElementsInstancedBaseVertex(mode, count, type, indices, instancecount, basevertex):
	pass


@params()
def glPopDebugGroup():
	pass


@params('program', 'uniformBlockIndex', 'uniformBlockBinding')
def glUniformBlockBinding(program, uniformBlockIndex, uniformBlockBinding):
	pass


@params('target', 'offset', 'size', 'data')
def glBufferSubData(target, offset, size):
	pass


@params('program', 'location', 'count', 'transpose', 'value')
def glProgramUniformMatrix3x2fv(program, location, count, transpose, value):
	pass


@params('sfactor', 'dfactor')
def glBlendFunc(sfactor, dfactor):
	pass


@params()
def glCreateProgram():
	pass


@params('program', 'location', 'count', 'transpose', 'value')
def glProgramUniformMatrix2fv(program, location, count, transpose, value):
	pass


@params('sampler', 'pname', 'param')
def glSamplerParameteriv(sampler, pname, param):
	pass


@params('red', 'green', 'blue', 'alpha')
def glClearColor(red, green, blue, alpha):
	pass


@params('program', 'location', 'bufSize', 'params')
def glGetnUniformiv(program, location, bufSize):
	pass


@params('mask',)
def glStencilMask(mask):
	pass


@params('index', 'v')
def glVertexAttribI4uiv(index, v):
	pass


@params('program', 'programInterface', 'name')
def glGetProgramResourceIndex(program, programInterface):
	pass


@params('location', 'count', 'transpose', 'value')
def glUniformMatrix2x3fv(location, count, transpose, value):
	pass


@params('n', 'ids')
def glGenTransformFeedbacks(n, ids):
	pass


@params('index', 'pname', 'params')
def glGetVertexAttribIuiv(index, pname):
	pass


@params('target', 'level', 'xoffset', 'yoffset', 'width', 'height', 'format', 'imageSize', 'data')
def glCompressedTexSubImage2D(target, level, xoffset, yoffset, width, height, format, imageSize):
	pass


@params('program', 'binaryFormat', 'binary', 'length')
def glProgramBinary(program, binaryFormat, binary, length):
	pass


@params('target', 'pname', 'params')
def glGetTexParameterfv(target, pname):
	pass


@params('target', 'pname', 'params')
def glTexParameterIiv(target, pname):
	pass


@params()
def glEndTransformFeedback():
	pass


@params('index', 'divisor')
def glVertexAttribDivisor(index, divisor):
	pass


@params('target', 'offset', 'length', 'access')
def glMapBufferRange(target, offset, length, access):
	pass


@params('program', 'location', 'count', 'transpose', 'value')
def glProgramUniformMatrix4x2fv(program, location, count, transpose, value):
	pass


@params('shadertype', 'precisiontype', 'range', 'precision')
def glGetShaderPrecisionFormat(shadertype, precisiontype, range, precision):
	pass


@params('shader', 'count', 'conststring', 'length')
def glShaderSource(shader, count, conststring, length):
	pass


@params('n', 'renderbuffers')
def glDeleteRenderbuffers(n, renderbuffers):
	pass


@params('target', 'size', 'data', 'usage')
def glBufferData(target, size, usage):
	pass


@params('target', 'attachment', 'textarget', 'texture', 'level')
def glFramebufferTexture2D(target, attachment, textarget, texture, level):
	pass


@params('target', 'pname', 'params')
def glGetBufferPointerv(target, pname):
	pass


@params('sampler', 'pname', 'param')
def glSamplerParameterfv(sampler, pname, param):
	pass


@params('location', 'count', 'value')
def glUniform1fv(location, count, value):
	pass


@params('index', 'x', 'y')
def glVertexAttrib2f(index, x, y):
	pass


@params('program', 'uniformBlockName')
def glGetUniformBlockIndex(program, uniformBlockName):
	pass


@params('mode',)
def glFrontFace(mode):
	pass


