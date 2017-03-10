@params('target', 'level', 'internalformat', 'x', 'y', 'width', 'border')
def glCopyTexImage1D(target, level, internalformat, x, y, width, border):
	pass


@params('vaobj', 'buffer')
def glVertexArrayElementBuffer(vaobj, buffer):
	pass


@params('face', 'mask')
def glStencilMaskSeparate(face, mask):
	pass


@params('texture', 'samples', 'internalformat', 'width', 'height', 'depth', 'fixedsamplelocations')
def glTextureStorage3DMultisample(texture, samples, internalformat, width, height, depth, fixedsamplelocations):
	pass


@params('texture', 'pname', 'param')
def glTextureParameterfv(texture, pname, param):
	pass


@params('index', 'v')
def glVertexAttrib4usv(index, v):
	pass


@params('c',)
def glIndexi(c):
	pass


@params('target', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth', 'format', 'imageSize', 'data')
def glCompressedTexSubImage3D(target, level, xoffset, yoffset, zoffset, width, height, depth, format, imageSize, data):
	pass


@params('u', 'v')
def glEvalCoord2d(u, v):
	pass


@params('u', 'v')
def glEvalCoord2f(u, v):
	pass


@params('c',)
def glIndexd(c):
	pass


@params('c',)
def glIndexf(c):
	pass


@params('c',)
def glIndexs(c):
	pass


@params('v',)
def glVertex3sv(v):
	pass


@params('target', 'query', 'bufSize', 'v')
def glGetnMapfv(target, query, bufSize, v):
	pass


@params('v',)
def glSecondaryColor3fv(v):
	pass


@params('pname', 'params')
def glFogfv(pname):
	pass


@params('mode', 'count', 'type', 'indices', 'instancecount', 'baseinstance')
def glDrawElementsInstancedBaseInstance(mode, count, type, indices, instancecount, baseinstance):
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


@params()
def glPopAttrib():
	pass


@params('face', 'mode')
def glColorMaterial(face, mode):
	pass


@params('target', 'internalformat', 'width', 'height')
def glRenderbufferStorage(target, internalformat, width, height):
	pass


@params('red', 'green', 'blue')
def glColor3b(red, green, blue):
	pass


@params('red', 'green', 'blue')
def glColor3f(red, green, blue):
	pass


@params('red', 'green', 'blue')
def glColor3d(red, green, blue):
	pass


@params('target', 'query', 'bufSize', 'v')
def glGetnMapiv(target, query, bufSize, v):
	pass


@params('red', 'green', 'blue')
def glColor3i(red, green, blue):
	pass


@params('index', 'v')
def glVertexAttrib4ubv(index, v):
	pass


@params('red', 'green', 'blue')
def glColor3s(red, green, blue):
	pass


@params('vaobj', 'index', 'pname', 'param')
def glGetVertexArrayIndexediv(vaobj, index, pname, param):
	pass


@params('target', 'v')
def glMultiTexCoord1iv(target, v):
	pass


@params('texture', 'type', 'coords')
def glMultiTexCoordP2ui(texture, type, coords):
	pass


@params('program', 'location', 'v0', 'v1', 'v2')
def glProgramUniform3f(program, location, v0, v1, v2):
	pass


@params('index', 'x', 'y', 'z', 'w')
def glVertexAttribL4d(index, x, y, z, w):
	pass


@params('v',)
def glVertex2iv(v):
	pass


@params('vaobj', 'attribindex', 'size', 'type', 'relativeoffset')
def glVertexArrayAttribLFormat(vaobj, attribindex, size, type, relativeoffset):
	pass


@params('buffer', 'offset', 'length')
def glInvalidateBufferSubData(buffer, offset, length):
	pass


@params()
def glResumeTransformFeedback():
	pass


@params('pname', 'param')
def glFogi(pname, param):
	pass


@params('size', 'type', 'stride', 'pointer')
def glVertexPointer(size, type, stride, pointer):
	pass


@params('pname', 'param')
def glFogf(pname, param):
	pass


@params('target', 's')
def glMultiTexCoord1d(target, s):
	pass


@params('target', 's')
def glMultiTexCoord1f(target, s):
	pass


@params('index', 'x', 'y')
def glVertexAttribI2i(index, x, y):
	pass


@params('target', 's')
def glMultiTexCoord1i(target, s):
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


@params('buffer', 'offset', 'length', 'access')
def glMapNamedBufferRange(buffer, offset, length, access):
	pass


@params('vaobj', 'attribindex', 'size', 'type', 'relativeoffset')
def glVertexArrayAttribIFormat(vaobj, attribindex, size, type, relativeoffset):
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


@params('first', 'count', 'v')
def glViewportArrayv(first, count, v):
	pass


@params('target', 's', 't')
def glMultiTexCoord2s(target, s, t):
	pass


@params('v',)
def glVertex3dv(v):
	pass


@params('v',)
def glColor4fv(v):
	pass


@params('vaobj', 'bindingindex', 'divisor')
def glVertexArrayBindingDivisor(vaobj, bindingindex, divisor):
	pass


@params('v',)
def glTexCoord2sv(v):
	pass


@params('location', 'count', 'value')
def glUniform2dv(location, count, value):
	pass


@params('map', 'values')
def glGetPixelMapuiv(map):
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


@params('index', 'x', 'y', 'z', 'w')
def glVertexAttrib4d(index, x, y, z, w):
	pass


@params('target', 'pname', 'params')
def glGetRenderbufferParameteriv(target, pname):
	pass


@params('renderbuffer', 'internalformat', 'width', 'height')
def glNamedRenderbufferStorage(renderbuffer, internalformat, width, height):
	pass


@params('condition', 'flags')
def glFenceSync(condition, flags):
	pass


@params('pipeline',)
def glValidateProgramPipeline(pipeline):
	pass


@params('type', 'value')
def glVertexP4ui(type, value):
	pass


@params('count', 'samplers')
def glGenSamplers(count, samplers):
	pass


@params('index', 'v')
def glVertexAttrib2sv(index, v):
	pass


@params('mode', 'id', 'instancecount')
def glDrawTransformFeedbackInstanced(mode, id, instancecount):
	pass


@params('v',)
def glTexCoord4iv(v):
	pass


@params('mode', 'id')
def glDrawTransformFeedback(mode, id):
	pass


@params('target', 'pname', 'params')
def glGetTexParameterIuiv(target, pname):
	pass


@params('type', 'stride', 'pointer')
def glIndexPointer(type, stride, pointer):
	pass


@params('sync',)
def glIsSync(sync):
	pass


@params('v',)
def glVertex4iv(v):
	pass


@params('target', 'v')
def glMultiTexCoord3iv(target, v):
	pass


@params('ptr', 'bufSize', 'length', 'label')
def glGetObjectPtrLabel(ptr, bufSize, length, label):
	pass


@params('texture', 'pname', 'param')
def glTextureParameteri(texture, pname, param):
	pass


@params('location', 'count', 'transpose', 'value')
def glUniformMatrix2x3dv(location, count, transpose, value):
	pass


@params('v',)
def glSecondaryColor3sv(v):
	pass


@params('left', 'right', 'bottom', 'top', 'zNear', 'zFar')
def glOrtho(left, right, bottom, top, zNear, zFar):
	pass


@params('coord',)
def glFogCoordd(coord):
	pass


@params('coord',)
def glFogCoordf(coord):
	pass


@params('target', 'level', 'internalformat', 'x', 'y', 'width', 'height', 'border')
def glCopyTexImage2D(target, level, internalformat, x, y, width, height, border):
	pass


@params('index', 'type', 'normalized', 'value')
def glVertexAttribP4ui(index, type, normalized, value):
	pass


@params('location', 'count', 'value')
def glUniform4uiv(location, count, value):
	pass


@params('index', 'v')
def glVertexAttribL1dv(index, v):
	pass


@params('program', 'location', 'count', 'transpose', 'value')
def glProgramUniformMatrix2dv(program, location, count, transpose, value):
	pass


@params('first', 'count', 'v')
def glScissorArrayv(first, count, v):
	pass


@params('list',)
def glCallList(list):
	pass


@params('pname', 'param')
def glLightModeli(pname, param):
	pass


@params('target', 'format', 'type', 'bufSize', 'table')
def glGetnColorTable(target, format, type, bufSize, table):
	pass


@params('v',)
def glWindowPos3iv(v):
	pass


@params('target', 'numAttachments', 'attachments', 'x', 'y', 'width', 'height')
def glInvalidateSubFramebuffer(target, numAttachments, attachments, x, y, width, height):
	pass


@params('target', 'access')
def glMapBuffer(target, access):
	pass


@params('red', 'green', 'blue')
def glSecondaryColor3d(red, green, blue):
	pass


@params('attribindex', 'size', 'type', 'relativeoffset')
def glVertexAttribLFormat(attribindex, size, type, relativeoffset):
	pass


@params('red', 'green', 'blue')
def glSecondaryColor3i(red, green, blue):
	pass


@params('sync',)
def glDeleteSync(sync):
	pass


@params('location', 'count', 'transpose', 'value')
def glUniformMatrix4x2dv(location, count, transpose, value):
	pass


@params('red', 'green', 'blue')
def glSecondaryColor3s(red, green, blue):
	pass


@params('location', 'count', 'value')
def glUniform3iv(location, count, value):
	pass


@params('s',)
def glTexCoord1s(s):
	pass


@params('face', 'mode')
def glPolygonMode(face, mode):
	pass


@params('program',)
def glUseProgram(program):
	pass


@params('factor', 'pattern')
def glLineStipple(factor, pattern):
	pass


@params('program', 'bufSize', 'length', 'infoLog')
def glGetProgramInfoLog(program, bufSize, length, infoLog):
	pass


@params('pname', 'param')
def glPixelStoref(pname, param):
	pass


@params('pname', 'data')
def glGetBooleanv(pname):
	pass


@params('shader',)
def glDeleteShader(shader):
	pass


@params('texture', 'level', 'xoffset', 'x', 'y', 'width')
def glCopyTextureSubImage1D(texture, level, xoffset, x, y, width):
	pass


@params('target', 'query', 'v')
def glGetMapdv(target, query, v):
	pass


@params('texture', 'pname', 'params')
def glTextureParameterIuiv(texture, pname):
	pass


@params('s', 't', 'r')
def glTexCoord3d(s, t, r):
	pass


@params('index', 'x', 'y', 'z')
def glVertexAttribI3i(index, x, y, z):
	pass


@params('attribindex', 'size', 'type', 'normalized', 'relativeoffset')
def glVertexAttribFormat(attribindex, size, type, normalized, relativeoffset):
	pass


@params('index', 'v')
def glVertexAttribI4usv(index, v):
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


@params('index', 'x', 'y', 'z', 'w')
def glVertexAttrib4s(index, x, y, z, w):
	pass


@params()
def glPopName():
	pass


@params('n', 'pipelines')
def glGenProgramPipelines(n, pipelines):
	pass


@params('red', 'green', 'blue', 'alpha')
def glColor4ub(red, green, blue, alpha):
	pass


@params('index', 'v')
def glVertexAttrib3fv(index, v):
	pass


@params('red', 'green', 'blue', 'alpha')
def glColor4ui(red, green, blue, alpha):
	pass


@params('buffer', 'pname', 'params')
def glGetNamedBufferParameteriv(buffer, pname):
	pass


@params('red', 'green', 'blue', 'alpha')
def glColor4us(red, green, blue, alpha):
	pass


@params('index', 'type', 'normalized', 'value')
def glVertexAttribP1uiv(index, type, normalized, value):
	pass


@params('program',)
def glLinkProgram(program):
	pass


@params('v',)
def glTexCoord2dv(v):
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


@params('stride', 'pointer')
def glEdgeFlagPointer(stride, pointer):
	pass


@params('target', 'pname', 'param')
def glFramebufferParameteri(target, pname, param):
	pass


@params('x', 'y', 'width', 'height', 'type')
def glCopyPixels(x, y, width, height, type):
	pass


@params('index', 'x', 'y')
def glVertexAttribI2ui(index, x, y):
	pass


@params('x', 'y', 'z')
def glRasterPos3s(x, y, z):
	pass


@params('n', 'textures')
def glDeleteTextures(n, textures):
	pass


@params('origin', 'depth')
def glClipControl(origin, depth):
	pass


@params('index', 'x', 'y', 'z', 'w')
def glVertexAttrib4f(index, x, y, z, w):
	pass


@params('framebuffer', 'pname', 'param')
def glNamedFramebufferParameteri(framebuffer, pname, param):
	pass


@params('framebuffer', 'pname', 'param')
def glGetNamedFramebufferParameteriv(framebuffer, pname, param):
	pass


@params('n', 'arrays')
def glCreateVertexArrays(n, arrays):
	pass


@params('id', 'mode')
def glBeginConditionalRender(id, mode):
	pass


@params('sampler', 'pname', 'param')
def glSamplerParameteri(sampler, pname, param):
	pass


@params('location', 'x')
def glUniform1d(location, x):
	pass


@params('mode',)
def glRenderMode(mode):
	pass


@params('target', 'level', 'img')
def glGetCompressedTexImage(target, level, img):
	pass


@params('program', 'uniformBlockIndex', 'pname', 'params')
def glGetActiveUniformBlockiv(program, uniformBlockIndex, pname):
	pass


@params('location', 'v0')
def glUniform1i(location, v0):
	pass


@params('target', 'pname', 'params')
def glGetTexEnvfv(target, pname):
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


@params('index', 'x', 'y', 'w', 'h')
def glViewportIndexedf(index, x, y, w, h):
	pass


@params('program', 'location', 'v0', 'v1', 'v2', 'v3')
def glProgramUniform4d(program, location, v0, v1, v2, v3):
	pass


@params('x', 'y', 'z')
def glVertex3i(x, y, z):
	pass


@params('program', 'shader')
def glAttachShader(program, shader):
	pass


@params('list',)
def glIsList(list):
	pass


@params('type', 'stride', 'pointer')
def glFogCoordPointer(type, stride, pointer):
	pass


@params('buffer',)
def glUnmapNamedBuffer(buffer):
	pass


@params('v',)
def glSecondaryColor3dv(v):
	pass


@params('index', 'v')
def glVertexAttribI4sv(index, v):
	pass


@params('mode', 'id', 'stream', 'instancecount')
def glDrawTransformFeedbackStreamInstanced(mode, id, stream, instancecount):
	pass


@params('target', 'pname', 'params')
def glGetBufferParameteriv(target, pname):
	pass


@params('target', 'pname', 'params')
def glTexParameterIuiv(target, pname):
	pass


@params('v',)
def glWindowPos3fv(v):
	pass


@params('pname', 'params')
def glLightModelfv(pname):
	pass


@params('texture', 'levels', 'internalformat', 'width', 'height', 'depth')
def glTextureStorage3D(texture, levels, internalformat, width, height, depth):
	pass


@params('id',)
def glIsTransformFeedback(id):
	pass


@params('angle', 'x', 'y', 'z')
def glRotated(angle, x, y, z):
	pass


@params('pipeline',)
def glIsProgramPipeline(pipeline):
	pass


@params('angle', 'x', 'y', 'z')
def glRotatef(angle, x, y, z):
	pass


@params('x', 'y', 'z', 'w')
def glVertex4i(x, y, z, w):
	pass


@params('program', 'shadertype', 'index', 'bufsize', 'length', 'name')
def glGetActiveSubroutineUniformName(program, shadertype, index, bufsize, length):
	pass


@params('location', 'count', 'transpose', 'value')
def glUniformMatrix3fv(location, count, transpose, value):
	pass


@params('program', 'location', 'bufSize', 'params')
def glGetnUniformfv(program, location, bufSize):
	pass


@params('index', 'v')
def glVertexAttribL2dv(index, v):
	pass


@params('size', 'type', 'stride', 'pointer')
def glSecondaryColorPointer(size, type, stride, pointer):
	pass


@params('func', 'ref')
def glAlphaFunc(func, ref):
	pass


@params('s', 't', 'r', 'q')
def glTexCoord4d(s, t, r, q):
	pass


@params('index', 'x', 'y')
def glVertexAttribL2d(index, x, y):
	pass


@params('func', 'ref', 'mask')
def glStencilFunc(func, ref, mask):
	pass


@params('v',)
def glTexCoord3dv(v):
	pass


@params('id', 'buffer', 'pname', 'offset')
def glGetQueryBufferObjectiv(id, buffer, pname, offset):
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


@params('v',)
def glRasterPos2iv(v):
	pass


@params('v',)
def glSecondaryColor3uiv(v):
	pass


@params('x', 'y')
def glRasterPos2i(x, y):
	pass


@params('modeRGB', 'modeAlpha')
def glBlendEquationSeparate(modeRGB, modeAlpha):
	pass


@params('program', 'shadertype', 'name')
def glGetSubroutineIndex(program, shadertype):
	pass


@params('mask',)
def glPushAttrib(mask):
	pass


@params('index', 'v')
def glVertexAttribL3dv(index, v):
	pass


@params('light', 'pname', 'params')
def glLightiv(light, pname):
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


@params('face', 'pname', 'params')
def glMaterialfv(face, pname):
	pass


@params('location', 'count', 'transpose', 'value')
def glUniformMatrix3dv(location, count, transpose, value):
	pass


@params('texture', 'level', 'pname', 'params')
def glGetTextureLevelParameteriv(texture, level, pname):
	pass


@params('name', 'index')
def glGetStringi(index):
	pass


@params('v',)
def glColor4dv(v):
	pass


@params('pname', 'params')
def glPointParameterfv(pname):
	pass


@params('location', 'count', 'value')
def glUniform2fv(location, count, value):
	pass


@params('framebuffer', 'numAttachments', 'attachments', 'x', 'y', 'width', 'height')
def glInvalidateNamedFramebufferSubData(framebuffer, numAttachments, attachments, x, y, width, height):
	pass


@params('target', 'index', 'buffer', 'offset', 'size')
def glBindBufferRange(target, index, buffer, offset, size):
	pass


@params('v',)
def glNormal3iv(v):
	pass


@params('program', 'location', 'params')
def glGetUniformdv(program, location):
	pass


@params('target', 's', 't', 'r', 'q')
def glMultiTexCoord4s(target, s, t, r, q):
	pass


@params('v',)
def glTexCoord1iv(v):
	pass


@params('v',)
def glColor3uiv(v):
	pass


@params('base',)
def glListBase(base):
	pass


@params('sync', 'flags', 'timeout')
def glClientWaitSync(sync, flags, timeout):
	pass


@params('texture', 'internalformat', 'buffer')
def glTextureBuffer(texture, internalformat, buffer):
	pass


@params('index', 'v')
def glVertexAttrib4Nsv(index, v):
	pass


@params('x', 'y', 'width', 'height', 'format', 'type', 'bufSize', 'data')
def glReadnPixels(x, y, width, height, format, type, bufSize):
	pass


@params('srcName', 'srcTarget', 'srcLevel', 'srcX', 'srcY', 'srcZ', 'dstName', 'dstTarget', 'dstLevel', 'dstX', 'dstY', 'dstZ', 'srcWidth', 'srcHeight', 'srcDepth')
def glCopyImageSubData(srcName, srcTarget, srcLevel, srcX, srcY, srcZ, dstName, dstTarget, dstLevel, dstX, dstY, dstZ, srcWidth, srcHeight, srcDepth):
	pass


@params('shadertype', 'location', 'params')
def glGetUniformSubroutineuiv(shadertype, location):
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


@params('target', 'level', 'xoffset', 'x', 'y', 'width')
def glCopyTexSubImage1D(target, level, xoffset, x, y, width):
	pass


@params('s',)
def glTexCoord1i(s):
	pass


@params('target',)
def glCheckFramebufferStatus(target):
	pass


@params('s',)
def glTexCoord1d(s):
	pass


@params('s',)
def glTexCoord1f(s):
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


@params('v',)
def glColor3bv(v):
	pass


@params('n', 'samplers')
def glCreateSamplers(n, samplers):
	pass


@params('mode', 'first', 'count', 'drawcount')
def glMultiDrawArrays(mode, first, count, drawcount):
	pass


@params('type', 'coords')
def glTexCoordP4ui(type, coords):
	pass


@params('index', 'x', 'y', 'z')
def glVertexAttribI3ui(index, x, y, z):
	pass


@params('attribindex', 'size', 'type', 'relativeoffset')
def glVertexAttribIFormat(attribindex, size, type, relativeoffset):
	pass


@params('n', 'framebuffers')
def glCreateFramebuffers(n, framebuffers):
	pass


@params('red', 'green', 'blue', 'alpha')
def glClearAccum(red, green, blue, alpha):
	pass


@params('target', 'id')
def glBeginQuery(target, id):
	pass


@params('target', 'u1', 'u2', 'ustride', 'uorder', 'v1', 'v2', 'vstride', 'vorder', 'points')
def glMap2d(target, u1, u2, ustride, uorder, v1, v2, vstride, vorder, points):
	pass


@params('target', 'u1', 'u2', 'ustride', 'uorder', 'v1', 'v2', 'vstride', 'vorder', 'points')
def glMap2f(target, u1, u2, ustride, uorder, v1, v2, vstride, vorder, points):
	pass


@params('location', 'count', 'transpose', 'value')
def glUniformMatrix2x4fv(location, count, transpose, value):
	pass


@params('index', 'n', 'f')
def glDepthRangeIndexed(index, n, f):
	pass


@params()
def glGetError():
	pass


@params('target', 'pname', 'params')
def glGetTexEnviv(target, pname):
	pass


@params('u',)
def glEvalCoord1d(u):
	pass


@params('target', 'level', 'pname', 'params')
def glGetTexLevelParameterfv(target, level, pname):
	pass


@params('u',)
def glEvalCoord1f(u):
	pass


@params('map', 'mapsize', 'values')
def glPixelMapfv(map, mapsize):
	pass


@params('map', 'values')
def glGetPixelMapusv(map):
	pass


@params('op', 'value')
def glAccum(op, value):
	pass


@params('v',)
def glRasterPos3sv(v):
	pass


@params('program', 'location', 'v0', 'v1')
def glProgramUniform2ui(program, location, v0, v1):
	pass


@params('program', 'location', 'v0', 'v1', 'v2', 'v3')
def glProgramUniform4ui(program, location, v0, v1, v2, v3):
	pass


@params('buffer', 'size', 'data', 'usage')
def glNamedBufferData(buffer, size, usage):
	pass


@params('buffer', 'internalformat', 'offset', 'size', 'format', 'type', 'data')
def glClearNamedBufferSubData(buffer, internalformat, offset, size, format, type):
	pass


@params('v1', 'v2')
def glRectsv(v1, v2):
	pass


@params('coord', 'pname', 'params')
def glGetTexGeniv(coord, pname):
	pass


@params('pname', 'param')
def glPixelStorei(pname, param):
	pass


@params('texture', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth', 'bufSize', 'pixels')
def glGetCompressedTextureSubImage(texture, level, xoffset, yoffset, zoffset, width, height, depth, bufSize):
	pass


@params('flag',)
def glDepthMask(flag):
	pass


@params('pname', 'values')
def glPatchParameterfv(pname):
	pass


@params('texture', 'levels', 'internalformat', 'width', 'height')
def glTextureStorage2D(texture, levels, internalformat, width, height):
	pass


@params('target', 'internalformat', 'buffer', 'offset', 'size')
def glTexBufferRange(target, internalformat, buffer, offset, size):
	pass


@params('v',)
def glRasterPos4fv(v):
	pass


@params('u',)
def glEvalCoord1dv(u):
	pass


@params()
def glPopClientAttrib():
	pass


@params('vaobj', 'first', 'count', 'buffers', 'offsets', 'strides')
def glVertexArrayVertexBuffers(vaobj, first, count, buffers, offsets, strides):
	pass


@params('program', 'pname', 'value')
def glProgramParameteri(program, pname, value):
	pass


@params('target', 'query', 'v')
def glGetMapfv(target, query, v):
	pass


@params('v',)
def glRasterPos2fv(v):
	pass


@params('barriers',)
def glMemoryBarrierByRegion(barriers):
	pass


@params('v',)
def glVertex2sv(v):
	pass


@params('v',)
def glWindowPos2sv(v):
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


@params('v',)
def glTexCoord2fv(v):
	pass


@params('v',)
def glTexCoord4fv(v):
	pass


@params('size',)
def glPointSize(size):
	pass


@params('unit', 'texture')
def glBindTextureUnit(unit, texture):
	pass


@params('pipeline', 'bufSize', 'length', 'infoLog')
def glGetProgramPipelineInfoLog(pipeline, bufSize, length, infoLog):
	pass


@params('index', 'v')
def glVertexAttrib4Nuiv(index, v):
	pass


@params('sync', 'flags', 'timeout')
def glWaitSync(sync, flags, timeout):
	pass


@params('buf', 'modeRGB', 'modeAlpha')
def glBlendEquationSeparatei(buf, modeRGB, modeAlpha):
	pass


@params('location', 'x', 'y', 'z')
def glUniform3d(location, x, y, z):
	pass


@params('location', 'v0', 'v1', 'v2')
def glUniform3f(location, v0, v1, v2):
	pass


@params('program', 'location', 'count', 'value')
def glProgramUniform3uiv(program, location, count, value):
	pass


@params('program', 'name')
def glGetFragDataIndex(program):
	pass


@params('v',)
def glColor3sv(v):
	pass


@params('v',)
def glVertex4sv(v):
	pass


@params('id', 'target')
def glQueryCounter(id, target):
	pass


@params('n', 'framebuffers')
def glDeleteFramebuffers(n, framebuffers):
	pass


@params('mode', 'first', 'count')
def glDrawArrays(mode, first, count):
	pass


@params('s', 't', 'r', 'q')
def glTexCoord4f(s, t, r, q):
	pass


@params('mask',)
def glClear(mask):
	pass


@params('target', 'n', 'ids')
def glCreateQueries(target, n, ids):
	pass


@params('sampler', 'pname', 'params')
def glGetSamplerParameterfv(sampler, pname):
	pass


@params('x', 'y', 'z')
def glTranslatef(x, y, z):
	pass


@params('index', 'x', 'y', 'z', 'w')
def glVertexAttrib4Nub(index, x, y, z, w):
	pass


@params('x', 'y', 'z')
def glTranslated(x, y, z):
	pass


@params('sampler', 'pname', 'param')
def glSamplerParameterIiv(sampler, pname, param):
	pass


@params('mode', 'type', 'indirect')
def glDrawElementsIndirect(mode, type, indirect):
	pass


@params('v',)
def glSecondaryColor3bv(v):
	pass


@params('s', 't', 'r', 'q')
def glTexCoord4s(s, t, r, q):
	pass


@params('id', 'pname', 'params')
def glGetQueryObjecti64v(id, pname):
	pass


@params('program', 'uniformCount', 'constuniformNames', 'uniformIndices')
def glGetUniformIndices(program, uniformCount, constuniformNames, uniformIndices):
	pass


@params('v',)
def glVertex3iv(v):
	pass


@params('coord', 'pname', 'params')
def glTexGenfv(coord, pname):
	pass


@params('first', 'count', 'buffers', 'offsets', 'strides')
def glBindVertexBuffers(first, count, buffers, offsets, strides):
	pass


@params('face', 'pname', 'param')
def glMateriali(face, pname, param):
	pass


@params('array',)
def glIsVertexArray(array):
	pass


@params('index',)
def glDisableVertexAttribArray(index):
	pass


@params('program', 'storageBlockIndex', 'storageBlockBinding')
def glShaderStorageBlockBinding(program, storageBlockIndex, storageBlockBinding):
	pass


@params('face', 'pname', 'param')
def glMaterialf(face, pname, param):
	pass


@params('texture', 'levels', 'internalformat', 'width')
def glTextureStorage1D(texture, levels, internalformat, width):
	pass


@params('program', 'programInterface', 'pname', 'params')
def glGetProgramInterfaceiv(program, programInterface, pname):
	pass


@params('buffer', 'access')
def glMapNamedBuffer(buffer, access):
	pass


@params('program', 'location', 'bufSize', 'params')
def glGetnUniformdv(program, location, bufSize):
	pass


@params('target', 'first', 'count', 'buffers')
def glBindBuffersBase(target, first, count, buffers):
	pass


@params('index', 'pname', 'params')
def glGetVertexAttribIiv(index, pname):
	pass


@params('type', 'value')
def glVertexP4uiv(type, value):
	pass


@params('index', 'v')
def glVertexAttribL4dv(index, v):
	pass


@params('pname', 'value')
def glPatchParameteri(pname, value):
	pass


@params('target', 'u1', 'u2', 'stride', 'order', 'points')
def glMap1d(target, u1, u2, stride, order, points):
	pass


@params('target', 'u1', 'u2', 'stride', 'order', 'points')
def glMap1f(target, u1, u2, stride, order, points):
	pass


@params('framebuffer', 'attachment', 'pname', 'params')
def glGetNamedFramebufferAttachmentParameteriv(framebuffer, attachment, pname):
	pass


@params('target', 'format', 'type', 'rowBufSize', 'row', 'columnBufSize', 'column', 'span')
def glGetnSeparableFilter(target, format, type, rowBufSize, row, columnBufSize, column, span):
	pass


@params('index', 'v')
def glVertexAttrib4sv(index, v):
	pass


@params('program', 'location', 'count', 'value')
def glProgramUniform1dv(program, location, count, value):
	pass


@params('light', 'pname', 'param')
def glLighti(light, pname, param):
	pass


@params('target', 'level', 'internalformat', 'width', 'border', 'format', 'type', 'pixels')
def glTexImage1D(target, level, internalformat, width, border, format, type):
	pass


@params('light', 'pname', 'param')
def glLightf(light, pname, param):
	pass


@params('value', 'invert')
def glSampleCoverage(value, invert):
	pass


@params('v',)
def glSecondaryColor3usv(v):
	pass


@params('xfb', 'pname', 'index', 'param')
def glGetTransformFeedbacki_v(xfb, pname, index, param):
	pass


@params('location', 'v0', 'v1')
def glUniform2i(location, v0, v1):
	pass


@params('un', 'u1', 'u2', 'vn', 'v1', 'v2')
def glMapGrid2f(un, u1, u2, vn, v1, v2):
	pass


@params('index', 'x')
def glVertexAttribL1d(index, x):
	pass


@params('target', 'attachment', 'texture', 'level', 'layer')
def glFramebufferTextureLayer(target, attachment, texture, level, layer):
	pass


@params('program', 'location', 'count', 'value')
def glProgramUniform2fv(program, location, count, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value')
def glProgramUniformMatrix2x4dv(program, location, count, transpose, value):
	pass


@params('target', 'pname', 'param')
def glTexEnvf(target, pname, param):
	pass


@params('target', 'index', 'data')
def glGetInteger64i_v(target, index):
	pass


@params('target', 'pname', 'param')
def glTexEnvi(target, pname, param):
	pass


@params('srcX0', 'srcY0', 'srcX1', 'srcY1', 'dstX0', 'dstY0', 'dstX1', 'dstY1', 'mask', 'filter')
def glBlitFramebuffer(srcX0, srcY0, srcX1, srcY1, dstX0, dstY0, dstX1, dstY1, mask, filter):
	pass


@params('target', 'index')
def glIsEnabledi(target, index):
	pass


@params('s', 't')
def glTexCoord2i(s, t):
	pass


@params('index', 'type', 'normalized', 'value')
def glVertexAttribP2ui(index, type, normalized, value):
	pass


@params('target', 'query', 'v')
def glGetMapiv(target, query, v):
	pass


@params('ptr', 'length', 'label')
def glObjectPtrLabel(ptr, length, label):
	pass


@params('count', 'bufSize', 'sources', 'types', 'ids', 'severities', 'lengths', 'messageLog')
def glGetDebugMessageLog(count, bufSize, sources, types, ids, severities, lengths, messageLog):
	pass


@params('program', 'color', 'name')
def glBindFragDataLocation(program, color):
	pass


@params('v',)
def glSecondaryColor3ubv(v):
	pass


@params('pname', 'param')
def glLightModelf(pname, param):
	pass


@params('mode', 'type', 'indirect', 'drawcount', 'stride')
def glMultiDrawElementsIndirect(mode, type, indirect, drawcount, stride):
	pass


@params('n', 'type', 'lists')
def glCallLists(n, type, lists):
	pass


@params('left', 'right', 'bottom', 'top', 'zNear', 'zFar')
def glFrustum(left, right, bottom, top, zNear, zFar):
	pass


@params('s', 't', 'r')
def glTexCoord3i(s, t, r):
	pass


@params('index', 'v')
def glVertexAttribI3uiv(index, v):
	pass


@params('source', 'id', 'length', 'message')
def glPushDebugGroup(source, id, length, message):
	pass


@params('texture', 'type', 'coords')
def glMultiTexCoordP1uiv(texture, type, coords):
	pass


@params('target', 'level', 'xoffset', 'yoffset', 'zoffset', 'x', 'y', 'width', 'height')
def glCopyTexSubImage3D(target, level, xoffset, yoffset, zoffset, x, y, width, height):
	pass


@params('program', 'uniformBlockIndex', 'bufSize', 'length', 'uniformBlockName')
def glGetActiveUniformBlockName(program, uniformBlockIndex, bufSize, length, uniformBlockName):
	pass


@params('s', 't', 'r')
def glTexCoord3s(s, t, r):
	pass


@params('n', 'textures', 'residences')
def glAreTexturesResident(n, textures, residences):
	pass


@params('program', 'location', 'v0', 'v1')
def glProgramUniform2d(program, location, v0, v1):
	pass


@params('program', 'location', 'v0', 'v1')
def glProgramUniform2f(program, location, v0, v1):
	pass


@params('v',)
def glRasterPos4sv(v):
	pass


@params('red', 'green', 'blue', 'alpha')
def glColor4s(red, green, blue, alpha):
	pass


@params('array',)
def glBindVertexArray(array):
	pass


@params('red', 'green', 'blue', 'alpha')
def glColor4b(red, green, blue, alpha):
	pass


@params('red', 'green', 'blue', 'alpha')
def glColor4f(red, green, blue, alpha):
	pass


@params('red', 'green', 'blue', 'alpha')
def glColor4d(red, green, blue, alpha):
	pass


@params('red', 'green', 'blue', 'alpha')
def glColor4i(red, green, blue, alpha):
	pass


@params('buffer', 'offset', 'size', 'data')
def glNamedBufferSubData(buffer, offset, size):
	pass


@params('v',)
def glVertex2dv(v):
	pass


@params('target', 'framebuffer')
def glBindFramebuffer(target, framebuffer):
	pass


@params('v1', 'v2')
def glRectfv(v1, v2):
	pass


@params('location', 'count', 'transpose', 'value')
def glUniformMatrix2x4dv(location, count, transpose, value):
	pass


@params('program', 'programInterface', 'name')
def glGetProgramResourceLocationIndex(program, programInterface):
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


@params('program', 'shadertype', 'index', 'pname', 'values')
def glGetActiveSubroutineUniformiv(program, shadertype, index, pname):
	pass


@params('target', 'internalformat', 'buffer')
def glTexBuffer(target, internalformat, buffer):
	pass


@params('i',)
def glArrayElement(i):
	pass


@params('program',)
def glValidateProgram(program):
	pass


@params('pipeline', 'program')
def glActiveShaderProgram(pipeline, program):
	pass


@params('texture', 'type', 'coords')
def glMultiTexCoordP2uiv(texture, type, coords):
	pass


@params('x1', 'y1', 'x2', 'y2')
def glRecti(x1, y1, x2, y2):
	pass


@params('x1', 'y1', 'x2', 'y2')
def glRectf(x1, y1, x2, y2):
	pass


@params('x1', 'y1', 'x2', 'y2')
def glRectd(x1, y1, x2, y2):
	pass


@params('target', 'texture')
def glBindTexture(target, texture):
	pass


@params('x1', 'y1', 'x2', 'y2')
def glRects(x1, y1, x2, y2):
	pass


@params('program', 'shader')
def glDetachShader(program, shader):
	pass


@params('texture', 'level', 'xoffset', 'yoffset', 'width', 'height', 'format', 'type', 'pixels')
def glTextureSubImage2D(texture, level, xoffset, yoffset, width, height, format, type):
	pass


@params('program', 'programInterface', 'name')
def glGetProgramResourceLocation(program, programInterface):
	pass


@params('index', 'v')
def glViewportIndexedfv(index, v):
	pass


@params('mode', 'count', 'type', 'indices', 'basevertex')
def glDrawElementsBaseVertex(mode, count, type, indices, basevertex):
	pass


@params('target', 'internalformat', 'offset', 'size', 'format', 'type', 'data')
def glClearBufferSubData(target, internalformat, offset, size, format, type):
	pass


@params('target', 'levels', 'internalformat', 'width')
def glTexStorage1D(target, levels, internalformat, width):
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


@params('coord', 'pname', 'param')
def glTexGenf(coord, pname, param):
	pass


@params('coord', 'pname', 'param')
def glTexGend(coord, pname, param):
	pass


@params('coord', 'pname', 'param')
def glTexGeni(coord, pname, param):
	pass


@params('index', 'left', 'bottom', 'width', 'height')
def glScissorIndexed(index, left, bottom, width, height):
	pass


@params('v',)
def glRasterPos4dv(v):
	pass


@params('v',)
def glRasterPos2dv(v):
	pass


@params('v',)
def glTexCoord2iv(v):
	pass


@params('type', 'count', 'conststrings')
def glCreateShaderProgramv(type, count, conststrings):
	pass


@params('id', 'pname', 'params')
def glGetQueryObjectiv(id, pname):
	pass


@params('x', 'y')
def glVertex2s(x, y):
	pass


@params('target',)
def glGenerateMipmap(target):
	pass


@params('texture', 'level', 'xoffset', 'yoffset', 'width', 'height', 'format', 'imageSize', 'data')
def glCompressedTextureSubImage2D(texture, level, xoffset, yoffset, width, height, format, imageSize):
	pass


@params('list', 'range')
def glDeleteLists(list, range):
	pass


@params('pname', 'param')
def glPointParameteri(pname, param):
	pass


@params('v',)
def glColor4iv(v):
	pass


@params('target',)
def glUnmapBuffer(target):
	pass


@params('pname', 'param')
def glPointParameterf(pname, param):
	pass


@params('s', 't')
def glTexCoord2s(s, t):
	pass


@params('v',)
def glTexCoord4dv(v):
	pass


@params('v',)
def glNormal3dv(v):
	pass


@params()
def glReleaseShaderCompiler():
	pass


@params('v',)
def glTexCoord1dv(v):
	pass


@params('x', 'y', 'width', 'height', 'format', 'type', 'pixels')
def glReadPixels(x, y, width, height, format, type):
	pass


@params('renderbuffer', 'samples', 'internalformat', 'width', 'height')
def glNamedRenderbufferStorageMultisample(renderbuffer, samples, internalformat, width, height):
	pass


@params('index', 'v')
def glVertexAttribI3iv(index, v):
	pass


@params('mode',)
def glShadeModel(mode):
	pass


@params('un', 'u1', 'u2')
def glMapGrid1d(un, u1, u2):
	pass


@params('framebuffer', 'numAttachments', 'attachments')
def glInvalidateNamedFramebufferData(framebuffer, numAttachments, attachments):
	pass


@params('v1', 'v2')
def glRectiv(v1, v2):
	pass


@params('type', 'color')
def glColorP4ui(type, color):
	pass


@params('pipeline', 'stages', 'program')
def glUseProgramStages(pipeline, stages, program):
	pass


@params('v',)
def glRasterPos3dv(v):
	pass


@params('src',)
def glReadBuffer(src):
	pass


@params('v',)
def glColor4ubv(v):
	pass


@params('target', 'offset', 'size', 'data')
def glGetBufferSubData(target, offset, size):
	pass


@params('index', 'pname', 'params')
def glGetVertexAttribLdv(index, pname):
	pass


@params('program', 'location', 'bufSize', 'params')
def glGetnUniformuiv(program, location, bufSize):
	pass


@params('n', 'buffers')
def glGenBuffers(n, buffers):
	pass


@params('framebuffer', 'buffer', 'drawbuffer', 'value')
def glClearNamedFramebufferiv(framebuffer, buffer, drawbuffer, value):
	pass


@params('index', 'v')
def glVertexAttribI2iv(index, v):
	pass


@params('framebuffer',)
def glIsFramebuffer(framebuffer):
	pass


@params('type', 'coords')
def glTexCoordP4uiv(type, coords):
	pass


@params('coord', 'pname', 'params')
def glTexGendv(coord, pname):
	pass


@params('type', 'value')
def glVertexP2uiv(type, value):
	pass


@params('s', 't')
def glTexCoord2d(s, t):
	pass


@params('target', 'pname', 'params')
def glGetBufferParameteri64v(target, pname):
	pass


@params('program', 'location', 'count', 'value')
def glProgramUniform4dv(program, location, count, value):
	pass


@params('s', 't')
def glTexCoord2f(s, t):
	pass


@params('target', 'v')
def glMultiTexCoord3fv(target, v):
	pass


@params('n', 'renderbuffers')
def glCreateRenderbuffers(n, renderbuffers):
	pass


@params('index', 'v')
def glVertexAttrib4Nusv(index, v):
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


@params('index', 'v')
def glVertexAttrib3dv(index, v):
	pass


@params('target', 'size', 'data', 'flags')
def glBufferStorage(target, size, flags):
	pass


@params('target', 'index', 'data')
def glGetFloati_v(target, index):
	pass


@params('program', 'name')
def glGetUniformLocation(program):
	pass


@params('framebuffer', 'n', 'bufs')
def glNamedFramebufferDrawBuffers(framebuffer, n, bufs):
	pass


@params('location', 'count', 'value')
def glUniform4fv(location, count, value):
	pass


@params('index', 'type', 'normalized', 'value')
def glVertexAttribP4uiv(index, type, normalized, value):
	pass


@params('texture', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth', 'format', 'imageSize', 'data')
def glCompressedTextureSubImage3D(texture, level, xoffset, yoffset, zoffset, width, height, depth, format, imageSize):
	pass


@params('index', 'v')
def glVertexAttrib4Nbv(index, v):
	pass


@params()
def glEndConditionalRender():
	pass


@params('array',)
def glEnableClientState(array):
	pass


@params('target', 'v')
def glMultiTexCoord2sv(target, v):
	pass


@params('program', 'location', 'count', 'value')
def glProgramUniform2uiv(program, location, count, value):
	pass


@params('id', 'pname', 'params')
def glGetQueryObjectuiv(id, pname):
	pass


@params('index', 'v')
def glVertexAttrib4iv(index, v):
	pass


@params('program', 'location', 'count', 'value')
def glProgramUniform1uiv(program, location, count, value):
	pass


@params('target', 'attachment', 'texture', 'level')
def glFramebufferTexture(target, attachment, texture, level):
	pass


@params('coord', 'pname', 'params')
def glGetTexGendv(coord, pname):
	pass


@params('v',)
def glColor3usv(v):
	pass


@params('program', 'location', 'count', 'transpose', 'value')
def glProgramUniformMatrix2x4fv(program, location, count, transpose, value):
	pass


@params('program', 'location', 'count', 'value')
def glProgramUniform2dv(program, location, count, value):
	pass


@params('v',)
def glRasterPos2sv(v):
	pass


@params('v',)
def glTexCoord1sv(v):
	pass


@params('x', 'y')
def glVertex2i(x, y):
	pass


@params('pname', 'data')
def glGetFloatv(pname):
	pass


@params('x', 'y', 'z')
def glWindowPos3f(x, y, z):
	pass


@params('type', 'color')
def glSecondaryColorP3uiv(type, color):
	pass


@params('pname', 'data')
def glGetIntegerv(pname):
	pass


@params('program', 'location', 'count', 'transpose', 'value')
def glProgramUniformMatrix3dv(program, location, count, transpose, value):
	pass


@params('id',)
def glIsQuery(id):
	pass


@params('target', 'level', 'internalformat', 'width', 'height', 'border', 'format', 'type', 'pixels')
def glTexImage2D(target, level, internalformat, width, height, border, format, type):
	pass


@params('width', 'height', 'format', 'type', 'pixels')
def glDrawPixels(width, height, format, type):
	pass


@params('m',)
def glMultMatrixd(m):
	pass


@params('m',)
def glMultMatrixf(m):
	pass


@params('index', 'v')
def glVertexAttrib4Nubv(index, v):
	pass


@params('v',)
def glColor4usv(v):
	pass


@params('un', 'u1', 'u2')
def glMapGrid1f(un, u1, u2):
	pass


@params('mask',)
def glPolygonStipple(mask):
	pass


@params('format', 'stride', 'pointer')
def glInterleavedArrays(format, stride, pointer):
	pass


@params('program', 'shadertype', 'name')
def glGetSubroutineUniformLocation(program, shadertype):
	pass


@params('target', 'pname', 'params')
def glGetFramebufferParameteriv(target, pname):
	pass


@params('map', 'mapsize', 'values')
def glPixelMapusv(map, mapsize):
	pass


@params('sampler', 'pname', 'params')
def glGetSamplerParameteriv(sampler, pname):
	pass


@params('readTarget', 'writeTarget', 'readOffset', 'writeOffset', 'size')
def glCopyBufferSubData(readTarget, writeTarget, readOffset, writeOffset, size):
	pass


@params('index', 'v')
def glVertexAttribI1uiv(index, v):
	pass


@params('v',)
def glColor3fv(v):
	pass


@params('program', 'index', 'bufSize', 'length', 'size', 'type', 'name')
def glGetActiveUniform(program, index, bufSize, length, size, type):
	pass


@params('framebuffer', 'attachment', 'texture', 'level', 'layer')
def glNamedFramebufferTextureLayer(framebuffer, attachment, texture, level, layer):
	pass


@params('index', 'x', 'y', 'z')
def glVertexAttribL3d(index, x, y, z):
	pass


@params('v',)
def glTexCoord3sv(v):
	pass


@params('value',)
def glMinSampleShading(value):
	pass


@params('v',)
def glVertex2fv(v):
	pass


@params('target', 'attachment', 'renderbuffertarget', 'renderbuffer')
def glFramebufferRenderbuffer(target, attachment, renderbuffertarget, renderbuffer):
	pass


@params('target', 'index', 'data')
def glGetDoublei_v(target, index):
	pass


@params('index', 'v')
def glVertexAttrib1sv(index, v):
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


@params('v',)
def glWindowPos2iv(v):
	pass


@params('pname', 'params')
def glFogiv(pname):
	pass


@params('pname', 'params')
def glLightModeliv(pname):
	pass


@params('n', 'f')
def glDepthRangef(n, f):
	pass


@params('target', 'index')
def glEnablei(target, index):
	pass


@params('u',)
def glEvalCoord1fv(u):
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


@params('index', 'v')
def glVertexAttrib2dv(index, v):
	pass


@params('flag',)
def glEdgeFlag(flag):
	pass


@params('program', 'location', 'v0')
def glProgramUniform1ui(program, location, v0):
	pass


@params('x', 'y', 'z')
def glVertex3d(x, y, z):
	pass


@params('x', 'y', 'z')
def glVertex3f(x, y, z):
	pass


@params('x', 'y', 'z')
def glVertex3s(x, y, z):
	pass


@params('type', 'coords')
def glTexCoordP2ui(type, coords):
	pass


@params('index', 'r', 'g', 'b', 'a')
def glColorMaski(index, r, g, b, a):
	pass


@params('readBuffer', 'writeBuffer', 'readOffset', 'writeOffset', 'size')
def glCopyNamedBufferSubData(readBuffer, writeBuffer, readOffset, writeOffset, size):
	pass


@params('target', 'levels', 'internalformat', 'width', 'height', 'depth')
def glTexStorage3D(target, levels, internalformat, width, height, depth):
	pass


@params('texture', 'pname', 'param')
def glTextureParameteriv(texture, pname, param):
	pass


@params('location', 'count', 'transpose', 'value')
def glUniformMatrix3x4fv(location, count, transpose, value):
	pass


@params('type', 'stride', 'pointer')
def glNormalPointer(type, stride, pointer):
	pass


@params('framebuffer', 'attachment', 'texture', 'level')
def glNamedFramebufferTexture(framebuffer, attachment, texture, level):
	pass


@params('token',)
def glPassThrough(token):
	pass


@params('type', 'color')
def glSecondaryColorP3ui(type, color):
	pass


@params('program', 'location', 'count', 'transpose', 'value')
def glProgramUniformMatrix4x3fv(program, location, count, transpose, value):
	pass


@params('mode',)
def glBegin(mode):
	pass


@params('u',)
def glEvalCoord2dv(u):
	pass


@params('v',)
def glColor3ubv(v):
	pass


@params('type', 'value')
def glVertexP3ui(type, value):
	pass


@params('light', 'pname', 'params')
def glLightfv(light, pname):
	pass


@params('program', 'uniformIndex', 'bufSize', 'length', 'uniformName')
def glGetActiveUniformName(program, uniformIndex, bufSize, length, uniformName):
	pass


@params('target', 'attachment', 'pname', 'params')
def glGetFramebufferAttachmentParameteriv(target, attachment, pname):
	pass


@params('target', 's', 't')
def glMultiTexCoord2f(target, s, t):
	pass


@params('framebuffer', 'buf')
def glNamedFramebufferDrawBuffer(framebuffer, buf):
	pass


@params('target', 'pname', 'params')
def glTexParameteriv(target, pname):
	pass


@params('vaobj', 'bindingindex', 'buffer', 'offset', 'stride')
def glVertexArrayVertexBuffer(vaobj, bindingindex, buffer, offset, stride):
	pass


@params('target', 'level', 'format', 'type', 'pixels')
def glGetTexImage(target, level, format, type):
	pass


@params('xfb', 'index', 'buffer')
def glTransformFeedbackBufferBase(xfb, index, buffer):
	pass


@params('c',)
def glIndexsv(c):
	pass


@params('type', 'coords')
def glTexCoordP3uiv(type, coords):
	pass


@params('width', 'height', 'xorig', 'yorig', 'xmove', 'ymove', 'bitmap')
def glBitmap(width, height, xorig, yorig, xmove, ymove, bitmap):
	pass


@params('buffer', 'offset', 'size', 'data')
def glGetNamedBufferSubData(buffer, offset, size):
	pass


@params('program', 'location', 'count', 'value')
def glProgramUniform2iv(program, location, count, value):
	pass


@params('target', 'pname', 'params')
def glGetQueryiv(target, pname):
	pass


@params('xfb', 'pname', 'param')
def glGetTransformFeedbackiv(xfb, pname, param):
	pass


@params('s', 't', 'r', 'q')
def glTexCoord4i(s, t, r, q):
	pass


@params('identifier', 'name', 'length', 'label')
def glObjectLabel(identifier, length, label):
	pass


@params('pname', 'params')
def glPointParameteriv(pname):
	pass


@params('v',)
def glNormal3fv(v):
	pass


@params('v',)
def glTexCoord1fv(v):
	pass


@params('target', 'v')
def glMultiTexCoord1dv(target, v):
	pass


@params('v',)
def glTexCoord3fv(v):
	pass


@params('texture', 'type', 'coords')
def glMultiTexCoordP3uiv(texture, type, coords):
	pass


@params('index', 'type', 'normalized', 'value')
def glVertexAttribP3ui(index, type, normalized, value):
	pass


@params('near', 'far')
def glDepthRange(near, far):
	pass


@params('buf',)
def glDrawBuffer(buf):
	pass


@params('map', 'bufSize', 'values')
def glGetnPixelMapusv(map, bufSize):
	pass


@params('v',)
def glRasterPos3fv(v):
	pass


@params('buffer', 'drawbuffer', 'value')
def glClearBufferuiv(buffer, drawbuffer, value):
	pass


@params('target', 'internalformat', 'pname', 'bufSize', 'params')
def glGetInternalformati64v(target, internalformat, pname, bufSize):
	pass


@params('c',)
def glClearIndex(c):
	pass


@params('index', 'size', 'type', 'stride', 'pointer')
def glVertexAttribIPointer(index, size, type, stride, pointer):
	pass


@params()
def glFlush():
	pass


@params('mode', 'count', 'type', 'indices', 'instancecount', 'basevertex', 'baseinstance')
def glDrawElementsInstancedBaseVertexBaseInstance(mode, count, type, indices, instancecount, basevertex, baseinstance):
	pass


@params('target', 'level', 'pname', 'params')
def glGetTexLevelParameteriv(target, level, pname):
	pass


@params('n', 'textures', 'priorities')
def glPrioritizeTextures(n, textures, priorities):
	pass


@params('size', 'buffer')
def glSelectBuffer(size, buffer):
	pass


@params('target', 'samples', 'internalformat', 'width', 'height', 'depth', 'fixedsamplelocations')
def glTexStorage3DMultisample(target, samples, internalformat, width, height, depth, fixedsamplelocations):
	pass


@params('target', 'clamp')
def glClampColor(target, clamp):
	pass


@params('s',)
def glClearStencil(s):
	pass


@params('type', 'coords')
def glTexCoordP1uiv(type, coords):
	pass


@params('texture',)
def glIsTexture(texture):
	pass


@params('x', 'y')
def glVertex2f(x, y):
	pass


@params('x', 'y')
def glVertex2d(x, y):
	pass


@params('target', 'index', 'id')
def glBeginQueryIndexed(target, index, id):
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


@params('target', 'offset', 'length')
def glFlushMappedBufferRange(target, offset, length):
	pass


@params('target', 'levels', 'internalformat', 'width', 'height')
def glTexStorage2D(target, levels, internalformat, width, height):
	pass


@params('n', 'ids')
def glGenQueries(n, ids):
	pass


@params('map', 'values')
def glGetPixelMapfv(map):
	pass


@params('target', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth', 'format', 'type', 'pixels')
def glTexSubImage3D(target, level, xoffset, yoffset, zoffset, width, height, depth, format, type):
	pass


@params('count', 'samplers')
def glDeleteSamplers(count, samplers):
	pass


@params('texture', 'pname', 'params')
def glGetTextureParameterfv(texture, pname):
	pass


@params('mode',)
def glMatrixMode(mode):
	pass


@params('first', 'count', 'textures')
def glBindTextures(first, count, textures):
	pass


@params('pname', 'data')
def glGetDoublev(pname):
	pass


@params('index', 'x')
def glVertexAttrib1d(index, x):
	pass


@params('location', 'count', 'value')
def glUniform4dv(location, count, value):
	pass


@params('program', 'location', 'count', 'value')
def glProgramUniform3dv(program, location, count, value):
	pass


@params('buffer',)
def glInvalidateBufferData(buffer):
	pass


@params('texture', 'level', 'xoffset', 'width', 'format', 'imageSize', 'data')
def glCompressedTextureSubImage1D(texture, level, xoffset, width, format, imageSize):
	pass


@params('texture', 'level', 'format', 'type', 'data')
def glClearTexImage(texture, level, format, type):
	pass


@params('location', 'count', 'value')
def glUniform3fv(location, count, value):
	pass


@params('texture', 'type', 'coords')
def glMultiTexCoordP1ui(texture, type, coords):
	pass


@params('xfb', 'pname', 'index', 'param')
def glGetTransformFeedbacki64_v(xfb, pname, index, param):
	pass


@params('mode', 'count', 'type', 'constindices', 'drawcount')
def glMultiDrawElements(mode, count, type, constindices, drawcount):
	pass


@params('n', 'bufs')
def glDrawBuffers(n, bufs):
	pass


@params('framebuffer', 'src')
def glNamedFramebufferReadBuffer(framebuffer, src):
	pass


@params('coord', 'pname', 'params')
def glGetTexGenfv(coord, pname):
	pass


@params('target', 'id')
def glBindTransformFeedback(target, id):
	pass


@params('target', 'v')
def glMultiTexCoord2iv(target, v):
	pass


@params('red', 'green', 'blue')
def glSecondaryColor3f(red, green, blue):
	pass


@params('v',)
def glRasterPos3iv(v):
	pass


@params('type', 'value')
def glVertexP2ui(type, value):
	pass


@params('target', 'format', 'type', 'bufSize', 'image')
def glGetnConvolutionFilter(target, format, type, bufSize, image):
	pass


@params('red', 'green', 'blue')
def glSecondaryColor3b(red, green, blue):
	pass


@params('v',)
def glTexCoord4sv(v):
	pass


@params('location', 'count', 'value')
def glUniform2uiv(location, count, value):
	pass


@params()
def glFinish():
	pass


@params('x', 'y')
def glRasterPos2s(x, y):
	pass


@params('location', 'count', 'value')
def glUniform1uiv(location, count, value):
	pass


@params('location', 'count', 'transpose', 'value')
def glUniformMatrix2dv(location, count, transpose, value):
	pass


@params('c',)
def glIndexdv(c):
	pass


@params('v',)
def glTexCoord3iv(v):
	pass


@params('depth',)
def glClearDepth(depth):
	pass


@params('location', 'count', 'transpose', 'value')
def glUniformMatrix4dv(location, count, transpose, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value')
def glProgramUniformMatrix4x3dv(program, location, count, transpose, value):
	pass


@params('v',)
def glVertex4dv(v):
	pass


@params('target', 'n', 'textures')
def glCreateTextures(target, n, textures):
	pass


@params('n', 'buffers')
def glCreateBuffers(n, buffers):
	pass


@params('m',)
def glMultTransposeMatrixf(m):
	pass


@params('flag',)
def glEdgeFlagv(flag):
	pass


@params('location', 'count', 'transpose', 'value')
def glUniformMatrix4x3dv(location, count, transpose, value):
	pass


@params('n', 'ids')
def glDeleteQueries(n, ids):
	pass


@params('type', 'coords')
def glNormalP3uiv(type, coords):
	pass


@params('x', 'y')
def glRasterPos2d(x, y):
	pass


@params()
def glInitNames():
	pass


@params('v',)
def glColor3dv(v):
	pass


@params('target', 'reset', 'format', 'type', 'bufSize', 'values')
def glGetnMinmax(target, reset, format, type, bufSize):
	pass


@params('framebuffer', 'buffer', 'drawbuffer', 'value')
def glClearNamedFramebufferuiv(framebuffer, buffer, drawbuffer, value):
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


@params('opcode',)
def glLogicOp(opcode):
	pass


@params('program', 'location', 'count', 'transpose', 'value')
def glProgramUniformMatrix3x4fv(program, location, count, transpose, value):
	pass


@params('pname', 'param')
def glPixelTransferf(pname, param):
	pass


@params('texture', 'pname', 'params')
def glGetTextureParameterIuiv(texture, pname):
	pass


@params('program', 'location', 'count', 'transpose', 'value')
def glProgramUniformMatrix4dv(program, location, count, transpose, value):
	pass


@params('location', 'count', 'transpose', 'value')
def glUniformMatrix3x4dv(location, count, transpose, value):
	pass


@params('mode', 'id', 'stream')
def glDrawTransformFeedbackStream(mode, id, stream):
	pass


@params('location', 'v0', 'v1', 'v2')
def glUniform3ui(location, v0, v1, v2):
	pass


@params('mode',)
def glProvokingVertex(mode):
	pass


@params('count', 'shaders', 'binaryformat', 'binary', 'length')
def glShaderBinary(count, shaders, binaryformat, binary, length):
	pass


@params('coord', 'pname', 'params')
def glTexGeniv(coord, pname):
	pass


@params('mode', 'count', 'type', 'indices')
def glDrawElements(mode, count, type, indices):
	pass


@params('program', 'location', 'count', 'value')
def glProgramUniform4iv(program, location, count, value):
	pass


@params('texture',)
def glClientActiveTexture(texture):
	pass


@params('location', 'count', 'value')
def glUniform1iv(location, count, value):
	pass


@params('mode', 'first', 'count', 'instancecount')
def glDrawArraysInstanced(mode, first, count, instancecount):
	pass


@params('index', 'v')
def glVertexAttrib4uiv(index, v):
	pass


@params('target', 'index')
def glEndQueryIndexed(target, index):
	pass


@params('program', 'location', 'count', 'value')
def glProgramUniform1iv(program, location, count, value):
	pass


@params('target', 'renderbuffer')
def glBindRenderbuffer(target, renderbuffer):
	pass


@params('face', 'pname', 'params')
def glMaterialiv(face, pname):
	pass


@params('program',)
def glIsProgram(program):
	pass


@params('index', 'v')
def glVertexAttrib4fv(index, v):
	pass


@params('program', 'location', 'count', 'transpose', 'value')
def glProgramUniformMatrix2x3dv(program, location, count, transpose, value):
	pass


@params('map', 'bufSize', 'values')
def glGetnPixelMapfv(map, bufSize):
	pass


@params('index', 'v')
def glVertexAttrib2fv(index, v):
	pass


@params('array',)
def glDisableClientState(array):
	pass


@params('v',)
def glColor4uiv(v):
	pass


@params('program', 'location', 'v0', 'v1', 'v2')
def glProgramUniform3i(program, location, v0, v1, v2):
	pass


@params('mode', 'i1', 'i2', 'j1', 'j2')
def glEvalMesh2(mode, i1, i2, j1, j2):
	pass


@params('mode', 'i1', 'i2')
def glEvalMesh1(mode, i1, i2):
	pass


@params('program', 'location', 'v0', 'v1', 'v2')
def glProgramUniform3d(program, location, v0, v1, v2):
	pass


@params('u',)
def glEvalCoord2fv(u):
	pass


@params('m',)
def glLoadTransposeMatrixd(m):
	pass


@params('m',)
def glLoadTransposeMatrixf(m):
	pass


@params('index', 'x')
def glVertexAttribI1ui(index, x):
	pass


@params('bufSize', 'pattern')
def glGetnPolygonStipple(bufSize, pattern):
	pass


@params('texture', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth')
def glInvalidateTexSubImage(texture, level, xoffset, yoffset, zoffset, width, height, depth):
	pass


@params('pname', 'data')
def glGetInteger64v(pname):
	pass


@params('plane', 'equation')
def glClipPlane(plane, equation):
	pass


@params('c',)
def glIndexub(c):
	pass


@params('framebuffer', 'attachment', 'renderbuffertarget', 'renderbuffer')
def glNamedFramebufferRenderbuffer(framebuffer, attachment, renderbuffertarget, renderbuffer):
	pass


@params('index', 'v')
def glVertexAttrib4Niv(index, v):
	pass


@params('buffer', 'drawbuffer', 'value')
def glClearBufferiv(buffer, drawbuffer, value):
	pass


@params('type', 'color')
def glColorP4uiv(type, color):
	pass


@params('texture', 'level', 'pname', 'params')
def glGetTextureLevelParameterfv(texture, level, pname):
	pass


@params('target', 'v')
def glMultiTexCoord1fv(target, v):
	pass


@params('sampler', 'pname', 'params')
def glGetSamplerParameterIuiv(sampler, pname):
	pass


@params('type', 'coords')
def glTexCoordP3ui(type, coords):
	pass


@params('location', 'v0', 'v1')
def glUniform2f(location, v0, v1):
	pass


@params('texture', 'level', 'xoffset', 'width', 'format', 'type', 'pixels')
def glTextureSubImage1D(texture, level, xoffset, width, format, type):
	pass


@params('x', 'y', 'z')
def glWindowPos3s(x, y, z):
	pass


@params('d',)
def glClearDepthf(d):
	pass


@params('texture', 'internalformat', 'buffer', 'offset', 'size')
def glTextureBufferRange(texture, internalformat, buffer, offset, size):
	pass


@params('x', 'y', 'z')
def glWindowPos3i(x, y, z):
	pass


@params('x', 'y', 'z')
def glWindowPos3d(x, y, z):
	pass


@params('texture', 'type', 'coords')
def glMultiTexCoordP4ui(texture, type, coords):
	pass


@params('red', 'green', 'blue')
def glColor3us(red, green, blue):
	pass


@params('light', 'pname', 'params')
def glGetLightiv(light, pname):
	pass


@params('target', 's', 't', 'r', 'q')
def glMultiTexCoord4f(target, s, t, r, q):
	pass


@params('red', 'green', 'blue')
def glColor3ub(red, green, blue):
	pass


@params('target', 's', 't', 'r', 'q')
def glMultiTexCoord4d(target, s, t, r, q):
	pass


@params('red', 'green', 'blue')
def glColor3ui(red, green, blue):
	pass


@params('target', 's', 't', 'r', 'q')
def glMultiTexCoord4i(target, s, t, r, q):
	pass


@params('mask',)
def glGetPolygonStipple(mask):
	pass


@params('location', 'x', 'y')
def glUniform2d(location, x, y):
	pass


@params('index', 'x', 'y', 'z', 'w')
def glVertexAttribI4ui(index, x, y, z, w):
	pass


@params('red', 'green', 'blue', 'alpha')
def glColorMask(red, green, blue, alpha):
	pass


@params('target', 'level', 'format', 'type', 'bufSize', 'pixels')
def glGetnTexImage(target, level, format, type, bufSize):
	pass


@params('mode',)
def glBlendEquation(mode):
	pass


@params('target', 'v')
def glMultiTexCoord3dv(target, v):
	pass


@params('v',)
def glColor4sv(v):
	pass


@params('program', 'programInterface', 'index', 'propCount', 'props', 'bufSize', 'length', 'params')
def glGetProgramResourceiv(program, programInterface, index, propCount, props, bufSize, length):
	pass


@params('target', 'internalformat', 'format', 'type', 'data')
def glClearBufferData(target, internalformat, format, type):
	pass


@params('primitiveMode',)
def glBeginTransformFeedback(primitiveMode):
	pass


@params('v',)
def glColor3iv(v):
	pass


@params('index', 'v')
def glVertexAttrib3sv(index, v):
	pass


@params('target', 'level', 'internalformat', 'width', 'border', 'imageSize', 'data')
def glCompressedTexImage1D(target, level, internalformat, width, border, imageSize):
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


@params('index', 'v')
def glVertexAttrib1dv(index, v):
	pass


@params('buf', 'srcRGB', 'dstRGB', 'srcAlpha', 'dstAlpha')
def glBlendFuncSeparatei(buf, srcRGB, dstRGB, srcAlpha, dstAlpha):
	pass


@params('location', 'v0', 'v1')
def glUniform2ui(location, v0, v1):
	pass


@params('pname', 'param')
def glPixelTransferi(pname, param):
	pass


@params('v',)
def glWindowPos2fv(v):
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


@params('i',)
def glEvalPoint1(i):
	pass


@params('i', 'j')
def glEvalPoint2(i, j):
	pass


@params()
def glPauseTransformFeedback():
	pass


@params('n', 'ids')
def glCreateTransformFeedbacks(n, ids):
	pass


@params('target', 'level', 'xoffset', 'width', 'format', 'type', 'pixels')
def glTexSubImage1D(target, level, xoffset, width, format, type):
	pass


@params('index', 'type', 'normalized', 'value')
def glVertexAttribP3uiv(index, type, normalized, value):
	pass


@params('index', 'v')
def glVertexAttribI4iv(index, v):
	pass


@params('vaobj', 'pname', 'param')
def glGetVertexArrayiv(vaobj, pname, param):
	pass


@params('name',)
def glLoadName():
	pass


@params('m',)
def glLoadMatrixf(m):
	pass


@params('m',)
def glLoadMatrixd(m):
	pass


@params('target', 'pname', 'params')
def glTexParameterfv(target, pname):
	pass


@params('location', 'count', 'value')
def glUniform3dv(location, count, value):
	pass


@params('face', 'func', 'ref', 'mask')
def glStencilFuncSeparate(face, func, ref, mask):
	pass


@params('program', 'location', 'count', 'value')
def glProgramUniform3fv(program, location, count, value):
	pass


@params('first', 'count', 'samplers')
def glBindSamplers(first, count, samplers):
	pass


@params('id', 'pname', 'params')
def glGetQueryObjectui64v(id, pname):
	pass


@params('texture', 'level', 'format', 'type', 'bufSize', 'pixels')
def glGetTextureImage(texture, level, format, type, bufSize):
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


@params('v',)
def glVertex3fv(v):
	pass


@params('x', 'y')
def glWindowPos2s(x, y):
	pass


@params('x', 'y')
def glWindowPos2i(x, y):
	pass


@params('x', 'y')
def glWindowPos2f(x, y):
	pass


@params('x', 'y')
def glWindowPos2d(x, y):
	pass


@params('shadertype', 'count', 'indices')
def glUniformSubroutinesuiv(shadertype, count, indices):
	pass


@params('v1', 'v2')
def glRectdv(v1, v2):
	pass


@params('type', 'color')
def glColorP3uiv(type, color):
	pass


@params('coord',)
def glFogCoordfv(coord):
	pass


@params('shader',)
def glCompileShader(shader):
	pass


@params('c',)
def glIndexfv(c):
	pass


@params('texture', 'type', 'coords')
def glMultiTexCoordP3ui(texture, type, coords):
	pass


@params('v',)
def glNormal3sv(v):
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


@params('v',)
def glVertex4fv(v):
	pass


@params('framebuffer', 'buffer', 'drawbuffer', 'depth', 'stencil')
def glClearNamedFramebufferfi(framebuffer, buffer, drawbuffer, depth, stencil):
	pass


@params('id', 'buffer', 'pname', 'offset')
def glGetQueryBufferObjectuiv(id, buffer, pname, offset):
	pass


@params('framebuffer', 'buffer', 'drawbuffer', 'value')
def glClearNamedFramebufferfv(framebuffer, buffer, drawbuffer, value):
	pass


@params('index', 'x')
def glVertexAttrib1s(index, x):
	pass


@params('target', 'v')
def glMultiTexCoord1sv(target, v):
	pass


@params('program',)
def glDeleteProgram(program):
	pass


@params('v',)
def glColor4bv(v):
	pass


@params('x', 'y')
def glRasterPos2f(x, y):
	pass


@params()
def glLoadIdentity():
	pass


@params('v',)
def glRasterPos4iv(v):
	pass


@params('location', 'count', 'transpose', 'value')
def glUniformMatrix4x3fv(location, count, transpose, value):
	pass


@params('buffer', 'drawbuffer', 'value')
def glClearBufferfv(buffer, drawbuffer, value):
	pass


@params()
def glTextureBarrier():
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


@params('vaobj', 'index')
def glEnableVertexArrayAttrib(vaobj, index):
	pass


@params('program', 'location', 'count', 'transpose', 'value')
def glProgramUniformMatrix3x2dv(program, location, count, transpose, value):
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


@params('id', 'buffer', 'pname', 'offset')
def glGetQueryBufferObjecti64v(id, buffer, pname, offset):
	pass


@params('index', 'pname', 'params')
def glGetVertexAttribdv(index, pname):
	pass


@params('location', 'v0')
def glUniform1ui(location, v0):
	pass


@params('readFramebuffer', 'drawFramebuffer', 'srcX0', 'srcY0', 'srcX1', 'srcY1', 'dstX0', 'dstY0', 'dstX1', 'dstY1', 'mask', 'filter')
def glBlitNamedFramebuffer(readFramebuffer, drawFramebuffer, srcX0, srcY0, srcX1, srcY1, dstX0, dstY0, dstX1, dstY1, mask, filter):
	pass


@params('index', 'x', 'y', 'z')
def glVertexAttrib3d(index, x, y, z):
	pass


@params('barriers',)
def glMemoryBarrier(barriers):
	pass


@params('program', 'name')
def glGetFragDataLocation(program):
	pass


@params('face', 'pname', 'params')
def glGetMaterialfv(face, pname):
	pass


@params('map', 'mapsize', 'values')
def glPixelMapuiv(map, mapsize):
	pass


@params('texture', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth', 'format', 'type', 'data')
def glClearTexSubImage(texture, level, xoffset, yoffset, zoffset, width, height, depth, format, type):
	pass


@params('texture', 'pname', 'params')
def glGetTextureParameterIiv(texture, pname):
	pass


@params('index', 'v')
def glVertexAttribI4ubv(index, v):
	pass


@params('program', 'location', 'count', 'transpose', 'value')
def glProgramUniformMatrix4x2dv(program, location, count, transpose, value):
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


@params('index', 'v')
def glVertexAttrib4dv(index, v):
	pass


@params('texture', 'pname', 'params')
def glGetTextureParameteriv(texture, pname):
	pass


@params('program', 'location', 'v0', 'v1', 'v2')
def glProgramUniform3ui(program, location, v0, v1, v2):
	pass


@params('program', 'location', 'count', 'transpose', 'value')
def glProgramUniformMatrix2x3fv(program, location, count, transpose, value):
	pass


@params()
def glPushMatrix():
	pass


@params('program', 'location', 'v0')
def glProgramUniform1i(program, location, v0):
	pass


@params('program', 'location', 'v0')
def glProgramUniform1d(program, location, v0):
	pass


@params('program', 'location', 'v0')
def glProgramUniform1f(program, location, v0):
	pass


@params('program', 'location', 'count', 'value')
def glProgramUniform3iv(program, location, count, value):
	pass


@params('c',)
def glIndexiv(c):
	pass


@params('xfb', 'index', 'buffer', 'offset', 'size')
def glTransformFeedbackBufferRange(xfb, index, buffer, offset, size):
	pass


@params('xfactor', 'yfactor')
def glPixelZoom(xfactor, yfactor):
	pass


@params('type', 'color')
def glColorP3ui(type, color):
	pass


@params('texture', 'type', 'coords')
def glMultiTexCoordP4uiv(texture, type, coords):
	pass


@params('texture', 'target', 'origtexture', 'internalformat', 'minlevel', 'numlevels', 'minlayer', 'numlayers')
def glTextureView(texture, target, origtexture, internalformat, minlevel, numlevels, minlayer, numlayers):
	pass


@params('vaobj', 'index')
def glDisableVertexArrayAttrib(vaobj, index):
	pass


@params('location', 'count', 'value')
def glUniform4iv(location, count, value):
	pass


@params('n', 'textures')
def glGenTextures(n, textures):
	pass


@params('texture', 'samples', 'internalformat', 'width', 'height', 'fixedsamplelocations')
def glTextureStorage2DMultisample(texture, samples, internalformat, width, height, fixedsamplelocations):
	pass


@params('target', 's')
def glMultiTexCoord1s(target, s):
	pass


@params('index', 'size', 'type', 'normalized', 'stride', 'pointer')
def glVertexAttribPointer(index, size, type, normalized, stride, pointer):
	pass


@params('location', 'v0')
def glUniform1f(location, v0):
	pass


@params('index', 'type', 'normalized', 'value')
def glVertexAttribP1ui(index, type, normalized, value):
	pass


@params('target', 'v')
def glMultiTexCoord4sv(target, v):
	pass


@params('program', 'location', 'count', 'transpose', 'value')
def glProgramUniformMatrix3x4dv(program, location, count, transpose, value):
	pass


@params('texture', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth', 'format', 'type', 'bufSize', 'pixels')
def glGetTextureSubImage(texture, level, xoffset, yoffset, zoffset, width, height, depth, format, type, bufSize):
	pass


@params('renderbuffer', 'pname', 'params')
def glGetNamedRenderbufferParameteriv(renderbuffer, pname):
	pass


@params('target', 'first', 'count', 'buffers', 'offsets', 'sizes')
def glBindBuffersRange(target, first, count, buffers, offsets, sizes):
	pass


@params('program', 'colorNumber', 'index', 'name')
def glBindFragDataLocationIndexed(program, colorNumber, index):
	pass


@params('target', 'v')
def glMultiTexCoord2dv(target, v):
	pass


@params('location', 'count', 'value')
def glUniform2iv(location, count, value):
	pass


@params('texture', 'pname', 'param')
def glTextureParameterf(texture, pname, param):
	pass


@params('size', 'type', 'buffer')
def glFeedbackBuffer(size, type, buffer):
	pass


@params('target', 's', 't')
def glMultiTexCoord2i(target, s, t):
	pass


@params('texture', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth', 'format', 'type', 'pixels')
def glTextureSubImage3D(texture, level, xoffset, yoffset, zoffset, width, height, depth, format, type):
	pass


@params('target', 'attachment', 'textarget', 'texture', 'level')
def glFramebufferTexture1D(target, attachment, textarget, texture, level):
	pass


@params('shader', 'pname', 'params')
def glGetShaderiv(shader, pname):
	pass


@params('target', 's', 't')
def glMultiTexCoord2d(target, s, t):
	pass


@params('buffer', 'size', 'data', 'flags')
def glNamedBufferStorage(buffer, size, flags):
	pass


@params('location', 'count', 'value')
def glUniform1dv(location, count, value):
	pass


@params('target', 'v')
def glMultiTexCoord4fv(target, v):
	pass


@params('x', 'y', 'z')
def glRasterPos3i(x, y, z):
	pass


@params('x', 'y', 'z')
def glRasterPos3d(x, y, z):
	pass


@params('x', 'y', 'z')
def glRasterPos3f(x, y, z):
	pass


@params('target', 'level', 'internalformat', 'width', 'height', 'depth', 'border', 'imageSize', 'data')
def glCompressedTexImage3D(target, level, internalformat, width, height, depth, border, imageSize):
	pass


@params('index', 'pname', 'params')
def glGetVertexAttribiv(index, pname):
	pass


@params('target', 'reset', 'format', 'type', 'bufSize', 'values')
def glGetnHistogram(target, reset, format, type, bufSize):
	pass


@params('location', 'count', 'transpose', 'value')
def glUniformMatrix2fv(location, count, transpose, value):
	pass


@params('texture',)
def glGenerateTextureMipmap(texture):
	pass


@params('mode', 'count', 'type', 'constindices', 'drawcount', 'basevertex')
def glMultiDrawElementsBaseVertex(mode, count, type, constindices, drawcount, basevertex):
	pass


@params('v',)
def glWindowPos3sv(v):
	pass


@params('target', 'level', 'xoffset', 'width', 'format', 'imageSize', 'data')
def glCompressedTexSubImage1D(target, level, xoffset, width, format, imageSize):
	pass


@params('target', 'pname', 'params')
def glGetTexParameterIiv(target, pname):
	pass


@params('texture', 'level')
def glInvalidateTexImage(texture, level):
	pass


@params('type', 'value')
def glVertexP3uiv(type, value):
	pass


@params('target', 'query', 'bufSize', 'v')
def glGetnMapdv(target, query, bufSize, v):
	pass


@params('callback', 'userParam')
def glDebugMessageCallback(callback, userParam):
	pass


@params('target', 'index', 'data')
def glGetBooleani_v(target, index):
	pass


@params('texture', 'pname', 'params')
def glTextureParameterIiv(texture, pname):
	pass


@params('list', 'mode')
def glNewList(list, mode):
	pass


@params('target', 'mode')
def glHint(target, mode):
	pass


@params('mode', 'indirect', 'drawcount', 'stride')
def glMultiDrawArraysIndirect(mode, indirect, drawcount, stride):
	pass


@params('index', 'type', 'normalized', 'value')
def glVertexAttribP2uiv(index, type, normalized, value):
	pass


@params('x', 'y', 'z')
def glScalef(x, y, z):
	pass


@params('x', 'y', 'z')
def glScaled(x, y, z):
	pass


@params('program', 'programInterface', 'index', 'bufSize', 'length', 'name')
def glGetProgramResourceName(program, programInterface, index, bufSize, length):
	pass


@params('first', 'count', 'v')
def glDepthRangeArrayv(first, count, v):
	pass


@params('program', 'bufferIndex', 'pname', 'params')
def glGetActiveAtomicCounterBufferiv(program, bufferIndex, pname):
	pass


@params('face', 'sfail', 'dpfail', 'dppass')
def glStencilOpSeparate(face, sfail, dpfail, dppass):
	pass


@params('vaobj', 'attribindex', 'bindingindex')
def glVertexArrayAttribBinding(vaobj, attribindex, bindingindex):
	pass


@params('s', 't', 'r')
def glTexCoord3f(s, t, r):
	pass


@params('index', 'x')
def glVertexAttribI1i(index, x):
	pass


@params('target', 'pname', 'params')
def glGetTexParameteriv(target, pname):
	pass


@params('index', 'pname', 'pointer')
def glGetVertexAttribPointerv(index, pname, pointer):
	pass


@params('target', 'lod', 'bufSize', 'pixels')
def glGetnCompressedTexImage(target, lod, bufSize):
	pass


@params('v',)
def glWindowPos2dv(v):
	pass


@params('cap',)
def glDisable(cap):
	pass


@params('program', 'location', 'count', 'value')
def glProgramUniform4uiv(program, location, count, value):
	pass


@params('texture', 'level', 'xoffset', 'yoffset', 'x', 'y', 'width', 'height')
def glCopyTextureSubImage2D(texture, level, xoffset, yoffset, x, y, width, height):
	pass


@params('index', 'v')
def glVertexAttribI2uiv(index, v):
	pass


@params('light', 'pname', 'params')
def glGetLightfv(light, pname):
	pass


@params('target', 's', 't', 'r')
def glMultiTexCoord3s(target, s, t, r):
	pass


@params('target', 's', 't', 'r')
def glMultiTexCoord3i(target, s, t, r):
	pass


@params('target', 's', 't', 'r')
def glMultiTexCoord3f(target, s, t, r):
	pass


@params('target', 's', 't', 'r')
def glMultiTexCoord3d(target, s, t, r):
	pass


@params('coord',)
def glFogCoorddv(coord):
	pass


@params('location', 'count', 'value')
def glUniform3uiv(location, count, value):
	pass


@params('buffer', 'internalformat', 'format', 'type', 'data')
def glClearNamedBufferData(buffer, internalformat, format, type):
	pass


@params('buffer', 'offset', 'length')
def glFlushMappedNamedBufferRange(buffer, offset, length):
	pass


@params('name',)
def glPushName():
	pass


@params('plane', 'equation')
def glGetClipPlane(plane, equation):
	pass


@params('x', 'y', 'z', 'w')
def glRasterPos4i(x, y, z, w):
	pass


@params('red', 'green', 'blue', 'alpha')
def glBlendColor(red, green, blue, alpha):
	pass


@params('sampler', 'pname', 'param')
def glSamplerParameterIuiv(sampler, pname, param):
	pass


@params('c',)
def glIndexubv(c):
	pass


@params('framebuffer', 'target')
def glCheckNamedFramebufferStatus(framebuffer, target):
	pass


@params('x', 'y', 'z', 'w')
def glRasterPos4d(x, y, z, w):
	pass


@params('x', 'y', 'z', 'w')
def glRasterPos4f(x, y, z, w):
	pass


@params('index', 'x', 'y', 'z')
def glVertexAttrib3s(index, x, y, z):
	pass


@params('x', 'y', 'z', 'w')
def glRasterPos4s(x, y, z, w):
	pass


@params('program', 'shadertype', 'pname', 'values')
def glGetProgramStageiv(program, shadertype, pname):
	pass


@params()
def glPopMatrix():
	pass


@params('x', 'y', 'z', 'w')
def glVertex4s(x, y, z, w):
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


@params('location', 'x', 'y', 'z', 'w')
def glUniform4d(location, x, y, z, w):
	pass


@params('location', 'v0', 'v1', 'v2', 'v3')
def glUniform4f(location, v0, v1, v2, v3):
	pass


@params('target', 'samples', 'internalformat', 'width', 'height')
def glRenderbufferStorageMultisample(target, samples, internalformat, width, height):
	pass


@params('n', 'pipelines')
def glCreateProgramPipelines(n, pipelines):
	pass


@params('index', 'size', 'type', 'stride', 'pointer')
def glVertexAttribLPointer(index, size, type, stride, pointer):
	pass


@params('target', 'v')
def glMultiTexCoord3sv(target, v):
	pass


@params('mode', 'count', 'type', 'indices', 'instancecount', 'basevertex')
def glDrawElementsInstancedBaseVertex(mode, count, type, indices, instancecount, basevertex):
	pass


@params('program', 'shadertype', 'index', 'bufsize', 'length', 'name')
def glGetActiveSubroutineName(program, shadertype, index, bufsize, length):
	pass


@params('target', 'v')
def glMultiTexCoord4iv(target, v):
	pass


@params('target', 'pname', 'params')
def glTexEnvfv(target, pname):
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


@params('size', 'type', 'stride', 'pointer')
def glTexCoordPointer(size, type, stride, pointer):
	pass


@params('program', 'location', 'count', 'transpose', 'value')
def glProgramUniformMatrix3x2fv(program, location, count, transpose, value):
	pass


@params('target', 'index', 'pname', 'params')
def glGetQueryIndexediv(target, index, pname):
	pass


@params('target', 'pname', 'params')
def glTexEnviv(target, pname):
	pass


@params('sfactor', 'dfactor')
def glBlendFunc(sfactor, dfactor):
	pass


@params()
def glCreateProgram():
	pass


@params('index',)
def glPrimitiveRestartIndex(index):
	pass


@params('program', 'location', 'count', 'transpose', 'value')
def glProgramUniformMatrix2fv(program, location, count, transpose, value):
	pass


@params('first', 'count', 'textures')
def glBindImageTextures(first, count, textures):
	pass


@params()
def glEnd():
	pass


@params('sampler', 'pname', 'param')
def glSamplerParameteriv(sampler, pname, param):
	pass


@params('v',)
def glSecondaryColor3iv(v):
	pass


@params('m',)
def glMultTransposeMatrixd(m):
	pass


@params('red', 'green', 'blue', 'alpha')
def glClearColor(red, green, blue, alpha):
	pass


@params('mask',)
def glPushClientAttrib(mask):
	pass


@params('program', 'location', 'bufSize', 'params')
def glGetnUniformiv(program, location, bufSize):
	pass


@params('mask',)
def glStencilMask(mask):
	pass


@params('red', 'green', 'blue')
def glSecondaryColor3us(red, green, blue):
	pass


@params('index', 'v')
def glVertexAttribI4uiv(index, v):
	pass


@params('index', 'v')
def glVertexAttrib4bv(index, v):
	pass


@params('program', 'programInterface', 'name')
def glGetProgramResourceIndex(program, programInterface):
	pass


@params('red', 'green', 'blue')
def glSecondaryColor3ub(red, green, blue):
	pass


@params('red', 'green', 'blue')
def glSecondaryColor3ui(red, green, blue):
	pass


@params('buffer', 'pname', 'params')
def glGetNamedBufferPointerv(buffer, pname):
	pass


@params('id', 'buffer', 'pname', 'offset')
def glGetQueryBufferObjectui64v(id, buffer, pname, offset):
	pass


@params('nx', 'ny', 'nz')
def glNormal3f(nx, ny, nz):
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


@params('index', 'v')
def glVertexAttribI4bv(index, v):
	pass


@params('target', 'pname', 'params')
def glGetTexParameterfv(target, pname):
	pass


@params('vaobj', 'index', 'pname', 'param')
def glGetVertexArrayIndexed64iv(vaobj, index, pname, param):
	pass


@params('target', 'pname', 'params')
def glTexParameterIiv(target, pname):
	pass


@params('vaobj', 'attribindex', 'size', 'type', 'normalized', 'relativeoffset')
def glVertexArrayAttribFormat(vaobj, attribindex, size, type, normalized, relativeoffset):
	pass


@params()
def glEndTransformFeedback():
	pass


@params('target', 'samples', 'internalformat', 'width', 'height', 'fixedsamplelocations')
def glTexImage2DMultisample(target, samples, internalformat, width, height, fixedsamplelocations):
	pass


@params('index', 'v')
def glVertexAttribI1iv(index, v):
	pass


@params('index', 'divisor')
def glVertexAttribDivisor(index, divisor):
	pass


@params('texture', 'level', 'bufSize', 'pixels')
def glGetCompressedTextureImage(texture, level, bufSize):
	pass


@params('range',)
def glGenLists(range):
	pass


@params('target', 'offset', 'length', 'access')
def glMapBufferRange(target, offset, length, access):
	pass


@params('program', 'location', 'count', 'transpose', 'value')
def glProgramUniformMatrix4x2fv(program, location, count, transpose, value):
	pass


@params()
def glEndList():
	pass


@params('location', 'count', 'transpose', 'value')
def glUniformMatrix3x2dv(location, count, transpose, value):
	pass


@params('shadertype', 'precisiontype', 'range', 'precision')
def glGetShaderPrecisionFormat(shadertype, precisiontype, range, precision):
	pass


@params('mask',)
def glIndexMask(mask):
	pass


@params('shader', 'count', 'conststring', 'length')
def glShaderSource(shader, count, conststring, length):
	pass


@params('n', 'renderbuffers')
def glDeleteRenderbuffers(n, renderbuffers):
	pass


@params('type', 'coords')
def glTexCoordP2uiv(type, coords):
	pass


@params('un', 'u1', 'u2', 'vn', 'v1', 'v2')
def glMapGrid2d(un, u1, u2, vn, v1, v2):
	pass


@params('buffer', 'pname', 'params')
def glGetNamedBufferParameteri64v(buffer, pname):
	pass


@params('x', 'y', 'z', 'w')
def glVertex4d(x, y, z, w):
	pass


@params('target', 'size', 'data', 'usage')
def glBufferData(target, size, usage):
	pass


@params('x', 'y', 'z', 'w')
def glVertex4f(x, y, z, w):
	pass


@params('type', 'coords')
def glTexCoordP1ui(type, coords):
	pass


@params('texture', 'level', 'xoffset', 'yoffset', 'zoffset', 'x', 'y', 'width', 'height')
def glCopyTextureSubImage3D(texture, level, xoffset, yoffset, zoffset, x, y, width, height):
	pass


@params('target', 'v')
def glMultiTexCoord2fv(target, v):
	pass


@params('type', 'coords')
def glNormalP3ui(type, coords):
	pass


@params('size', 'type', 'stride', 'pointer')
def glColorPointer(size, type, stride, pointer):
	pass


@params('target', 'attachment', 'textarget', 'texture', 'level')
def glFramebufferTexture2D(target, attachment, textarget, texture, level):
	pass


@params('target', 'pname', 'params')
def glGetBufferPointerv(target, pname):
	pass


@params('target', 'attachment', 'textarget', 'texture', 'level', 'zoffset')
def glFramebufferTexture3D(target, attachment, textarget, texture, level, zoffset):
	pass


@params('v',)
def glWindowPos3dv(v):
	pass


@params('sampler', 'pname', 'param')
def glSamplerParameterfv(sampler, pname, param):
	pass


@params('v',)
def glNormal3bv(v):
	pass


@params('face', 'pname', 'params')
def glGetMaterialiv(face, pname):
	pass


@params('location', 'count', 'value')
def glUniform1fv(location, count, value):
	pass


@params('index', 'v')
def glScissorIndexedv(index, v):
	pass


@params('nx', 'ny', 'nz')
def glNormal3s(nx, ny, nz):
	pass


@params('map', 'bufSize', 'values')
def glGetnPixelMapuiv(map, bufSize):
	pass


@params('nx', 'ny', 'nz')
def glNormal3i(nx, ny, nz):
	pass


@params('nx', 'ny', 'nz')
def glNormal3d(nx, ny, nz):
	pass


@params('nx', 'ny', 'nz')
def glNormal3b(nx, ny, nz):
	pass


@params('target', 'v')
def glMultiTexCoord4dv(target, v):
	pass


@params('index', 'x', 'y')
def glVertexAttrib2d(index, x, y):
	pass


@params('index', 'x', 'y')
def glVertexAttrib2f(index, x, y):
	pass


@params('index', 'x', 'y')
def glVertexAttrib2s(index, x, y):
	pass


@params('target', 'samples', 'internalformat', 'width', 'height', 'depth', 'fixedsamplelocations')
def glTexImage3DMultisample(target, samples, internalformat, width, height, depth, fixedsamplelocations):
	pass


@params('program', 'uniformBlockName')
def glGetUniformBlockIndex(program, uniformBlockName):
	pass


@params('mode',)
def glFrontFace(mode):
	pass


@params('mode', 'first', 'count', 'instancecount', 'baseinstance')
def glDrawArraysInstancedBaseInstance(mode, first, count, instancecount, baseinstance):
	pass


