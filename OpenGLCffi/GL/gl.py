from OpenGLCffi.GL import params
@params('target', 'level', 'internalformat', 'x', 'y', 'width', 'border', api='gl')
def glCopyTexImage1D(target, level, internalformat, x, y, width, border):
	pass


@params('vaobj', 'buffer', api='gl')
def glVertexArrayElementBuffer(vaobj, buffer):
	pass


@params('face', 'mask', api='gl')
def glStencilMaskSeparate(face, mask):
	pass


@params('texture', 'samples', 'internalformat', 'width', 'height', 'depth', 'fixedsamplelocations', api='gl')
def glTextureStorage3DMultisample(texture, samples, internalformat, width, height, depth, fixedsamplelocations):
	pass


@params('texture', 'pname', 'param', api='gl')
def glTextureParameterfv(texture, pname, param):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib4usv(index, v):
	pass


@params('c', api='gl')
def glIndexi(c):
	pass


@params('target', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth', 'format', 'imageSize', 'data', api='gl')
def glCompressedTexSubImage3D(target, level, xoffset, yoffset, zoffset, width, height, depth, format, imageSize, data):
	pass


@params('u', 'v', api='gl')
def glEvalCoord2d(u, v):
	pass


@params('u', 'v', api='gl')
def glEvalCoord2f(u, v):
	pass


@params('c', api='gl')
def glIndexd(c):
	pass


@params('c', api='gl')
def glIndexf(c):
	pass


@params('c', api='gl')
def glIndexs(c):
	pass


@params('v', api='gl')
def glVertex3sv(v):
	pass


@params('target', 'query', 'bufSize', 'v', api='gl')
def glGetnMapfv(target, query, bufSize, v):
	pass


@params('v', api='gl')
def glSecondaryColor3fv(v):
	pass


@params('pname', 'params', api='gl')
def glFogfv(pname, params):
	pass


@params('mode', 'count', 'type', 'indices', 'instancecount', 'baseinstance', api='gl')
def glDrawElementsInstancedBaseInstance(mode, count, type, indices, instancecount, baseinstance):
	pass


@params('buffer', api='gl')
def glIsBuffer(buffer):
	pass


@params('pname', 'index', 'val', api='gl')
def glGetMultisamplefv(pname, index, val):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix4fv(program, location, count, transpose, value):
	pass


@params('source', 'type', 'severity', 'count', 'ids', 'enabled', api='gl')
def glDebugMessageControl(source, type, severity, count, ids, enabled):
	pass


@params(api = 'gl')
def glPopAttrib():
	pass


@params('face', 'mode', api='gl')
def glColorMaterial(face, mode):
	pass


@params('target', 'internalformat', 'width', 'height', api='gl')
def glRenderbufferStorage(target, internalformat, width, height):
	pass


@params('red', 'green', 'blue', api='gl')
def glColor3b(red, green, blue):
	pass


@params('red', 'green', 'blue', api='gl')
def glColor3f(red, green, blue):
	pass


@params('red', 'green', 'blue', api='gl')
def glColor3d(red, green, blue):
	pass


@params('target', 'query', 'bufSize', 'v', api='gl')
def glGetnMapiv(target, query, bufSize, v):
	pass


@params('red', 'green', 'blue', api='gl')
def glColor3i(red, green, blue):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib4ubv(index, v):
	pass


@params('red', 'green', 'blue', api='gl')
def glColor3s(red, green, blue):
	pass


@params('vaobj', 'index', 'pname', 'param', api='gl')
def glGetVertexArrayIndexediv(vaobj, index, pname, param):
	pass


@params('target', 'v', api='gl')
def glMultiTexCoord1iv(target, v):
	pass


@params('texture', 'type', 'coords', api='gl')
def glMultiTexCoordP2ui(texture, type, coords):
	pass


@params('program', 'location', 'v0', 'v1', 'v2', api='gl')
def glProgramUniform3f(program, location, v0, v1, v2):
	pass


@params('index', 'x', 'y', 'z', 'w', api='gl')
def glVertexAttribL4d(index, x, y, z, w):
	pass


@params('v', api='gl')
def glVertex2iv(v):
	pass


@params('vaobj', 'attribindex', 'size', 'type', 'relativeoffset', api='gl')
def glVertexArrayAttribLFormat(vaobj, attribindex, size, type, relativeoffset):
	pass


@params('buffer', 'offset', 'length', api='gl')
def glInvalidateBufferSubData(buffer, offset, length):
	pass


@params(api = 'gl')
def glResumeTransformFeedback():
	pass


@params('pname', 'param', api='gl')
def glFogi(pname, param):
	pass


@params('size', 'type', 'stride', 'pointer', api='gl')
def glVertexPointer(size, type, stride, pointer):
	pass


@params('pname', 'param', api='gl')
def glFogf(pname, param):
	pass


@params('target', 's', api='gl')
def glMultiTexCoord1d(target, s):
	pass


@params('target', 's', api='gl')
def glMultiTexCoord1f(target, s):
	pass


@params('index', 'x', 'y', api='gl')
def glVertexAttribI2i(index, x, y):
	pass


@params('target', 's', api='gl')
def glMultiTexCoord1i(target, s):
	pass


@params(api = 'gl')
def glGetGraphicsResetStatus():
	pass


@params('index', 'v', api='gl')
def glVertexAttrib1fv(index, v):
	pass


@params('cap', api='gl')
def glIsEnabled(cap):
	pass


@params('fail', 'zfail', 'zpass', api='gl')
def glStencilOp(fail, zfail, zpass):
	pass


@params('buffer', 'offset', 'length', 'access', api='gl')
def glMapNamedBufferRange(buffer, offset, length, access):
	pass


@params('vaobj', 'attribindex', 'size', 'type', 'relativeoffset', api='gl')
def glVertexArrayAttribIFormat(vaobj, attribindex, size, type, relativeoffset):
	pass


@params('n', 'framebuffers', api='gl')
def glGenFramebuffers(n, framebuffers):
	pass


@params('program', 'maxCount', 'count', 'shaders', api='gl')
def glGetAttachedShaders(program, maxCount, count, shaders):
	pass


@params('n', 'arrays', api='gl')
def glDeleteVertexArrays(n, arrays):
	pass


@params('first', 'count', 'v', api='gl')
def glViewportArrayv(first, count, v):
	pass


@params('target', 's', 't', api='gl')
def glMultiTexCoord2s(target, s, t):
	pass


@params('v', api='gl')
def glVertex3dv(v):
	pass


@params('v', api='gl')
def glColor4fv(v):
	pass


@params('vaobj', 'bindingindex', 'divisor', api='gl')
def glVertexArrayBindingDivisor(vaobj, bindingindex, divisor):
	pass


@params('v', api='gl')
def glTexCoord2sv(v):
	pass


@params('location', 'count', 'value', api='gl')
def glUniform2dv(location, count, value):
	pass


@params('map', 'values', api='gl')
def glGetPixelMapuiv(map, values):
	pass


@params('pname', 'params', api='gl')
def glGetPointerv(pname, params):
	pass


@params('program', 'location', 'params', api='gl')
def glGetUniformfv(program, location, params):
	pass


@params('program', 'location', 'params', api='gl')
def glGetUniformuiv(program, location, params):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix3fv(program, location, count, transpose, value):
	pass


@params('mode', 'count', 'type', 'indices', 'instancecount', api='gl')
def glDrawElementsInstanced(mode, count, type, indices, instancecount):
	pass


@params('index', 'x', 'y', 'z', 'w', api='gl')
def glVertexAttrib4d(index, x, y, z, w):
	pass


@params('target', 'pname', 'params', api='gl')
def glGetRenderbufferParameteriv(target, pname, params):
	pass


@params('renderbuffer', 'internalformat', 'width', 'height', api='gl')
def glNamedRenderbufferStorage(renderbuffer, internalformat, width, height):
	pass


@params('condition', 'flags', api='gl')
def glFenceSync(condition, flags):
	pass


@params('pipeline', api='gl')
def glValidateProgramPipeline(pipeline):
	pass


@params('type', 'value', api='gl')
def glVertexP4ui(type, value):
	pass


@params('count', 'samplers', api='gl')
def glGenSamplers(count, samplers):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib2sv(index, v):
	pass


@params('mode', 'id', 'instancecount', api='gl')
def glDrawTransformFeedbackInstanced(mode, id, instancecount):
	pass


@params('v', api='gl')
def glTexCoord4iv(v):
	pass


@params('mode', 'id', api='gl')
def glDrawTransformFeedback(mode, id):
	pass


@params('target', 'pname', 'params', api='gl')
def glGetTexParameterIuiv(target, pname, params):
	pass


@params('type', 'stride', 'pointer', api='gl')
def glIndexPointer(type, stride, pointer):
	pass


@params('sync', api='gl')
def glIsSync(sync):
	pass


@params('v', api='gl')
def glVertex4iv(v):
	pass


@params('target', 'v', api='gl')
def glMultiTexCoord3iv(target, v):
	pass


@params('ptr', 'bufSize', 'length', 'label', api='gl')
def glGetObjectPtrLabel(ptr, bufSize, length, label):
	pass


@params('texture', 'pname', 'param', api='gl')
def glTextureParameteri(texture, pname, param):
	pass


@params('location', 'count', 'transpose', 'value', api='gl')
def glUniformMatrix2x3dv(location, count, transpose, value):
	pass


@params('v', api='gl')
def glSecondaryColor3sv(v):
	pass


@params('left', 'right', 'bottom', 'top', 'zNear', 'zFar', api='gl')
def glOrtho(left, right, bottom, top, zNear, zFar):
	pass


@params('coord', api='gl')
def glFogCoordd(coord):
	pass


@params('coord', api='gl')
def glFogCoordf(coord):
	pass


@params('target', 'level', 'internalformat', 'x', 'y', 'width', 'height', 'border', api='gl')
def glCopyTexImage2D(target, level, internalformat, x, y, width, height, border):
	pass


@params('index', 'type', 'normalized', 'value', api='gl')
def glVertexAttribP4ui(index, type, normalized, value):
	pass


@params('location', 'count', 'value', api='gl')
def glUniform4uiv(location, count, value):
	pass


@params('index', 'v', api='gl')
def glVertexAttribL1dv(index, v):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix2dv(program, location, count, transpose, value):
	pass


@params('first', 'count', 'v', api='gl')
def glScissorArrayv(first, count, v):
	pass


@params('list', api='gl')
def glCallList(list):
	pass


@params('pname', 'param', api='gl')
def glLightModeli(pname, param):
	pass


@params('target', 'format', 'type', 'bufSize', 'table', api='gl')
def glGetnColorTable(target, format, type, bufSize, table):
	pass


@params('v', api='gl')
def glWindowPos3iv(v):
	pass


@params('target', 'numAttachments', 'attachments', 'x', 'y', 'width', 'height', api='gl')
def glInvalidateSubFramebuffer(target, numAttachments, attachments, x, y, width, height):
	pass


@params('target', 'access', api='gl')
def glMapBuffer(target, access):
	pass


@params('red', 'green', 'blue', api='gl')
def glSecondaryColor3d(red, green, blue):
	pass


@params('attribindex', 'size', 'type', 'relativeoffset', api='gl')
def glVertexAttribLFormat(attribindex, size, type, relativeoffset):
	pass


@params('red', 'green', 'blue', api='gl')
def glSecondaryColor3i(red, green, blue):
	pass


@params('sync', api='gl')
def glDeleteSync(sync):
	pass


@params('location', 'count', 'transpose', 'value', api='gl')
def glUniformMatrix4x2dv(location, count, transpose, value):
	pass


@params('red', 'green', 'blue', api='gl')
def glSecondaryColor3s(red, green, blue):
	pass


@params('location', 'count', 'value', api='gl')
def glUniform3iv(location, count, value):
	pass


@params('s', api='gl')
def glTexCoord1s(s):
	pass


@params('face', 'mode', api='gl')
def glPolygonMode(face, mode):
	pass


@params('program', api='gl')
def glUseProgram(program):
	pass


@params('factor', 'pattern', api='gl')
def glLineStipple(factor, pattern):
	pass


@params('program', 'bufSize', 'length', 'infoLog', api='gl')
def glGetProgramInfoLog(program, bufSize, length, infoLog):
	pass


@params('pname', 'param', api='gl')
def glPixelStoref(pname, param):
	pass


@params('pname', 'data', api='gl')
def glGetBooleanv(pname, data):
	pass


@params('shader', api='gl')
def glDeleteShader(shader):
	pass


@params('texture', 'level', 'xoffset', 'x', 'y', 'width', api='gl')
def glCopyTextureSubImage1D(texture, level, xoffset, x, y, width):
	pass


@params('target', 'query', 'v', api='gl')
def glGetMapdv(target, query, v):
	pass


@params('texture', 'pname', 'params', api='gl')
def glTextureParameterIuiv(texture, pname, params):
	pass


@params('s', 't', 'r', api='gl')
def glTexCoord3d(s, t, r):
	pass


@params('index', 'x', 'y', 'z', api='gl')
def glVertexAttribI3i(index, x, y, z):
	pass


@params('attribindex', 'size', 'type', 'normalized', 'relativeoffset', api='gl')
def glVertexAttribFormat(attribindex, size, type, normalized, relativeoffset):
	pass


@params('index', 'v', api='gl')
def glVertexAttribI4usv(index, v):
	pass


@params('target', 'pname', 'param', api='gl')
def glTexParameterf(target, pname, param):
	pass


@params('attribindex', 'bindingindex', api='gl')
def glVertexAttribBinding(attribindex, bindingindex):
	pass


@params('target', 'pname', 'param', api='gl')
def glTexParameteri(target, pname, param):
	pass


@params('shader', 'bufSize', 'length', 'source', api='gl')
def glGetShaderSource(shader, bufSize, length, source):
	pass


@params('index', 'x', 'y', 'z', 'w', api='gl')
def glVertexAttrib4s(index, x, y, z, w):
	pass


@params(api = 'gl')
def glPopName():
	pass


@params('n', 'pipelines', api='gl')
def glGenProgramPipelines(n, pipelines):
	pass


@params('red', 'green', 'blue', 'alpha', api='gl')
def glColor4ub(red, green, blue, alpha):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib3fv(index, v):
	pass


@params('red', 'green', 'blue', 'alpha', api='gl')
def glColor4ui(red, green, blue, alpha):
	pass


@params('buffer', 'pname', 'params', api='gl')
def glGetNamedBufferParameteriv(buffer, pname, params):
	pass


@params('red', 'green', 'blue', 'alpha', api='gl')
def glColor4us(red, green, blue, alpha):
	pass


@params('index', 'type', 'normalized', 'value', api='gl')
def glVertexAttribP1uiv(index, type, normalized, value):
	pass


@params('program', api='gl')
def glLinkProgram(program):
	pass


@params('v', api='gl')
def glTexCoord2dv(v):
	pass


@params('identifier', 'name', 'bufSize', 'length', 'label', api='gl')
def glGetObjectLabel(identifier, name, bufSize, length, label):
	pass


@params('name', api='gl')
def glGetString(name):
	pass


@params('target', api='gl')
def glEndQuery(target):
	pass


@params('stride', 'pointer', api='gl')
def glEdgeFlagPointer(stride, pointer):
	pass


@params('target', 'pname', 'param', api='gl')
def glFramebufferParameteri(target, pname, param):
	pass


@params('x', 'y', 'width', 'height', 'type', api='gl')
def glCopyPixels(x, y, width, height, type):
	pass


@params('index', 'x', 'y', api='gl')
def glVertexAttribI2ui(index, x, y):
	pass


@params('x', 'y', 'z', api='gl')
def glRasterPos3s(x, y, z):
	pass


@params('n', 'textures', api='gl')
def glDeleteTextures(n, textures):
	pass


@params('origin', 'depth', api='gl')
def glClipControl(origin, depth):
	pass


@params('index', 'x', 'y', 'z', 'w', api='gl')
def glVertexAttrib4f(index, x, y, z, w):
	pass


@params('framebuffer', 'pname', 'param', api='gl')
def glNamedFramebufferParameteri(framebuffer, pname, param):
	pass


@params('framebuffer', 'pname', 'param', api='gl')
def glGetNamedFramebufferParameteriv(framebuffer, pname, param):
	pass


@params('n', 'arrays', api='gl')
def glCreateVertexArrays(n, arrays):
	pass


@params('id', 'mode', api='gl')
def glBeginConditionalRender(id, mode):
	pass


@params('sampler', 'pname', 'param', api='gl')
def glSamplerParameteri(sampler, pname, param):
	pass


@params('location', 'x', api='gl')
def glUniform1d(location, x):
	pass


@params('mode', api='gl')
def glRenderMode(mode):
	pass


@params('target', 'level', 'img', api='gl')
def glGetCompressedTexImage(target, level, img):
	pass


@params('program', 'uniformBlockIndex', 'pname', 'params', api='gl')
def glGetActiveUniformBlockiv(program, uniformBlockIndex, pname, params):
	pass


@params('location', 'v0', api='gl')
def glUniform1i(location, v0):
	pass


@params('target', 'pname', 'params', api='gl')
def glGetTexEnvfv(target, pname, params):
	pass


@params('mode', api='gl')
def glCullFace(mode):
	pass


@params('program', 'location', 'v0', 'v1', 'v2', 'v3', api='gl')
def glProgramUniform4i(program, location, v0, v1, v2, v3):
	pass


@params('program', 'location', 'v0', 'v1', 'v2', 'v3', api='gl')
def glProgramUniform4f(program, location, v0, v1, v2, v3):
	pass


@params('index', 'x', 'y', 'w', 'h', api='gl')
def glViewportIndexedf(index, x, y, w, h):
	pass


@params('program', 'location', 'v0', 'v1', 'v2', 'v3', api='gl')
def glProgramUniform4d(program, location, v0, v1, v2, v3):
	pass


@params('x', 'y', 'z', api='gl')
def glVertex3i(x, y, z):
	pass


@params('program', 'shader', api='gl')
def glAttachShader(program, shader):
	pass


@params('list', api='gl')
def glIsList(list):
	pass


@params('type', 'stride', 'pointer', api='gl')
def glFogCoordPointer(type, stride, pointer):
	pass


@params('buffer', api='gl')
def glUnmapNamedBuffer(buffer):
	pass


@params('v', api='gl')
def glSecondaryColor3dv(v):
	pass


@params('index', 'v', api='gl')
def glVertexAttribI4sv(index, v):
	pass


@params('mode', 'id', 'stream', 'instancecount', api='gl')
def glDrawTransformFeedbackStreamInstanced(mode, id, stream, instancecount):
	pass


@params('target', 'pname', 'params', api='gl')
def glGetBufferParameteriv(target, pname, params):
	pass


@params('target', 'pname', 'params', api='gl')
def glTexParameterIuiv(target, pname, params):
	pass


@params('v', api='gl')
def glWindowPos3fv(v):
	pass


@params('pname', 'params', api='gl')
def glLightModelfv(pname, params):
	pass


@params('texture', 'levels', 'internalformat', 'width', 'height', 'depth', api='gl')
def glTextureStorage3D(texture, levels, internalformat, width, height, depth):
	pass


@params('id', api='gl')
def glIsTransformFeedback(id):
	pass


@params('angle', 'x', 'y', 'z', api='gl')
def glRotated(angle, x, y, z):
	pass


@params('pipeline', api='gl')
def glIsProgramPipeline(pipeline):
	pass


@params('angle', 'x', 'y', 'z', api='gl')
def glRotatef(angle, x, y, z):
	pass


@params('x', 'y', 'z', 'w', api='gl')
def glVertex4i(x, y, z, w):
	pass


@params('program', 'shadertype', 'index', 'bufsize', 'length', 'name', api='gl')
def glGetActiveSubroutineUniformName(program, shadertype, index, bufsize, length, name):
	pass


@params('location', 'count', 'transpose', 'value', api='gl')
def glUniformMatrix3fv(location, count, transpose, value):
	pass


@params('program', 'location', 'bufSize', 'params', api='gl')
def glGetnUniformfv(program, location, bufSize, params):
	pass


@params('index', 'v', api='gl')
def glVertexAttribL2dv(index, v):
	pass


@params('size', 'type', 'stride', 'pointer', api='gl')
def glSecondaryColorPointer(size, type, stride, pointer):
	pass


@params('func', 'ref', api='gl')
def glAlphaFunc(func, ref):
	pass


@params('s', 't', 'r', 'q', api='gl')
def glTexCoord4d(s, t, r, q):
	pass


@params('index', 'x', 'y', api='gl')
def glVertexAttribL2d(index, x, y):
	pass


@params('func', 'ref', 'mask', api='gl')
def glStencilFunc(func, ref, mask):
	pass


@params('v', api='gl')
def glTexCoord3dv(v):
	pass


@params('id', 'buffer', 'pname', 'offset', api='gl')
def glGetQueryBufferObjectiv(id, buffer, pname, offset):
	pass


@params('pipeline', 'pname', 'params', api='gl')
def glGetProgramPipelineiv(pipeline, pname, params):
	pass


@params('indirect', api='gl')
def glDispatchComputeIndirect(indirect):
	pass


@params('shader', 'bufSize', 'length', 'infoLog', api='gl')
def glGetShaderInfoLog(shader, bufSize, length, infoLog):
	pass


@params('index', 'x', 'y', 'z', 'w', api='gl')
def glVertexAttribI4i(index, x, y, z, w):
	pass


@params('v', api='gl')
def glRasterPos2iv(v):
	pass


@params('v', api='gl')
def glSecondaryColor3uiv(v):
	pass


@params('x', 'y', api='gl')
def glRasterPos2i(x, y):
	pass


@params('modeRGB', 'modeAlpha', api='gl')
def glBlendEquationSeparate(modeRGB, modeAlpha):
	pass


@params('program', 'shadertype', 'name', api='gl')
def glGetSubroutineIndex(program, shadertype, name):
	pass


@params('mask', api='gl')
def glPushAttrib(mask):
	pass


@params('index', 'v', api='gl')
def glVertexAttribL3dv(index, v):
	pass


@params('light', 'pname', 'params', api='gl')
def glLightiv(light, pname, params):
	pass


@params('n', 'buffers', api='gl')
def glDeleteBuffers(n, buffers):
	pass


@params('pipeline', api='gl')
def glBindProgramPipeline(pipeline):
	pass


@params('x', 'y', 'width', 'height', api='gl')
def glScissor(x, y, width, height):
	pass


@params('face', 'pname', 'params', api='gl')
def glMaterialfv(face, pname, params):
	pass


@params('location', 'count', 'transpose', 'value', api='gl')
def glUniformMatrix3dv(location, count, transpose, value):
	pass


@params('texture', 'level', 'pname', 'params', api='gl')
def glGetTextureLevelParameteriv(texture, level, pname, params):
	pass


@params('name', 'index', api='gl')
def glGetStringi(name, index):
	pass


@params('v', api='gl')
def glColor4dv(v):
	pass


@params('pname', 'params', api='gl')
def glPointParameterfv(pname, params):
	pass


@params('location', 'count', 'value', api='gl')
def glUniform2fv(location, count, value):
	pass


@params('framebuffer', 'numAttachments', 'attachments', 'x', 'y', 'width', 'height', api='gl')
def glInvalidateNamedFramebufferSubData(framebuffer, numAttachments, attachments, x, y, width, height):
	pass


@params('target', 'index', 'buffer', 'offset', 'size', api='gl')
def glBindBufferRange(target, index, buffer, offset, size):
	pass


@params('v', api='gl')
def glNormal3iv(v):
	pass


@params('program', 'location', 'params', api='gl')
def glGetUniformdv(program, location, params):
	pass


@params('target', 's', 't', 'r', 'q', api='gl')
def glMultiTexCoord4s(target, s, t, r, q):
	pass


@params('v', api='gl')
def glTexCoord1iv(v):
	pass


@params('v', api='gl')
def glColor3uiv(v):
	pass


@params('base', api='gl')
def glListBase(base):
	pass


@params('sync', 'flags', 'timeout', api='gl')
def glClientWaitSync(sync, flags, timeout):
	pass


@params('texture', 'internalformat', 'buffer', api='gl')
def glTextureBuffer(texture, internalformat, buffer):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib4Nsv(index, v):
	pass


@params('x', 'y', 'width', 'height', 'format', 'type', 'bufSize', 'data', api='gl')
def glReadnPixels(x, y, width, height, format, type, bufSize, data):
	pass


@params('srcName', 'srcTarget', 'srcLevel', 'srcX', 'srcY', 'srcZ', 'dstName', 'dstTarget', 'dstLevel', 'dstX', 'dstY', 'dstZ', 'srcWidth', 'srcHeight', 'srcDepth', api='gl')
def glCopyImageSubData(srcName, srcTarget, srcLevel, srcX, srcY, srcZ, dstName, dstTarget, dstLevel, dstX, dstY, dstZ, srcWidth, srcHeight, srcDepth):
	pass


@params('shadertype', 'location', 'params', api='gl')
def glGetUniformSubroutineuiv(shadertype, location, params):
	pass


@params('bindingindex', 'buffer', 'offset', 'stride', api='gl')
def glBindVertexBuffer(bindingindex, buffer, offset, stride):
	pass


@params('source', 'type', 'id', 'severity', 'length', 'buf', api='gl')
def glDebugMessageInsert(source, type, id, severity, length, buf):
	pass


@params('sampler', api='gl')
def glIsSampler(sampler):
	pass


@params('target', 'level', 'xoffset', 'x', 'y', 'width', api='gl')
def glCopyTexSubImage1D(target, level, xoffset, x, y, width):
	pass


@params('s', api='gl')
def glTexCoord1i(s):
	pass


@params('target', api='gl')
def glCheckFramebufferStatus(target):
	pass


@params('s', api='gl')
def glTexCoord1d(s):
	pass


@params('s', api='gl')
def glTexCoord1f(s):
	pass


@params('unit', 'texture', 'level', 'layered', 'layer', 'access', 'format', api='gl')
def glBindImageTexture(unit, texture, level, layered, layer, access, format):
	pass


@params('program', 'count', 'constvaryings', 'bufferMode', api='gl')
def glTransformFeedbackVaryings(program, count, constvaryings, bufferMode):
	pass


@params('mode', 'start', 'end', 'count', 'type', 'indices', api='gl')
def glDrawRangeElements(mode, start, end, count, type, indices):
	pass


@params('target', 'index', 'buffer', api='gl')
def glBindBufferBase(target, index, buffer):
	pass


@params('v', api='gl')
def glColor3bv(v):
	pass


@params('n', 'samplers', api='gl')
def glCreateSamplers(n, samplers):
	pass


@params('mode', 'first', 'count', 'drawcount', api='gl')
def glMultiDrawArrays(mode, first, count, drawcount):
	pass


@params('type', 'coords', api='gl')
def glTexCoordP4ui(type, coords):
	pass


@params('index', 'x', 'y', 'z', api='gl')
def glVertexAttribI3ui(index, x, y, z):
	pass


@params('attribindex', 'size', 'type', 'relativeoffset', api='gl')
def glVertexAttribIFormat(attribindex, size, type, relativeoffset):
	pass


@params('n', 'framebuffers', api='gl')
def glCreateFramebuffers(n, framebuffers):
	pass


@params('red', 'green', 'blue', 'alpha', api='gl')
def glClearAccum(red, green, blue, alpha):
	pass


@params('target', 'id', api='gl')
def glBeginQuery(target, id):
	pass


@params('target', 'u1', 'u2', 'ustride', 'uorder', 'v1', 'v2', 'vstride', 'vorder', 'points', api='gl')
def glMap2d(target, u1, u2, ustride, uorder, v1, v2, vstride, vorder, points):
	pass


@params('target', 'u1', 'u2', 'ustride', 'uorder', 'v1', 'v2', 'vstride', 'vorder', 'points', api='gl')
def glMap2f(target, u1, u2, ustride, uorder, v1, v2, vstride, vorder, points):
	pass


@params('location', 'count', 'transpose', 'value', api='gl')
def glUniformMatrix2x4fv(location, count, transpose, value):
	pass


@params('index', 'n', 'f', api='gl')
def glDepthRangeIndexed(index, n, f):
	pass


@params(api = 'gl')
def glGetError():
	pass


@params('target', 'pname', 'params', api='gl')
def glGetTexEnviv(target, pname, params):
	pass


@params('u', api='gl')
def glEvalCoord1d(u):
	pass


@params('target', 'level', 'pname', 'params', api='gl')
def glGetTexLevelParameterfv(target, level, pname, params):
	pass


@params('u', api='gl')
def glEvalCoord1f(u):
	pass


@params('map', 'mapsize', 'values', api='gl')
def glPixelMapfv(map, mapsize, values):
	pass


@params('map', 'values', api='gl')
def glGetPixelMapusv(map, values):
	pass


@params('op', 'value', api='gl')
def glAccum(op, value):
	pass


@params('v', api='gl')
def glRasterPos3sv(v):
	pass


@params('program', 'location', 'v0', 'v1', api='gl')
def glProgramUniform2ui(program, location, v0, v1):
	pass


@params('program', 'location', 'v0', 'v1', 'v2', 'v3', api='gl')
def glProgramUniform4ui(program, location, v0, v1, v2, v3):
	pass


@params('buffer', 'size', 'data', 'usage', api='gl')
def glNamedBufferData(buffer, size, data, usage):
	pass


@params('buffer', 'internalformat', 'offset', 'size', 'format', 'type', 'data', api='gl')
def glClearNamedBufferSubData(buffer, internalformat, offset, size, format, type, data):
	pass


@params('v1', 'v2', api='gl')
def glRectsv(v1, v2):
	pass


@params('coord', 'pname', 'params', api='gl')
def glGetTexGeniv(coord, pname, params):
	pass


@params('pname', 'param', api='gl')
def glPixelStorei(pname, param):
	pass


@params('texture', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth', 'bufSize', 'pixels', api='gl')
def glGetCompressedTextureSubImage(texture, level, xoffset, yoffset, zoffset, width, height, depth, bufSize, pixels):
	pass


@params('flag', api='gl')
def glDepthMask(flag):
	pass


@params('pname', 'values', api='gl')
def glPatchParameterfv(pname, values):
	pass


@params('texture', 'levels', 'internalformat', 'width', 'height', api='gl')
def glTextureStorage2D(texture, levels, internalformat, width, height):
	pass


@params('target', 'internalformat', 'buffer', 'offset', 'size', api='gl')
def glTexBufferRange(target, internalformat, buffer, offset, size):
	pass


@params('v', api='gl')
def glRasterPos4fv(v):
	pass


@params('u', api='gl')
def glEvalCoord1dv(u):
	pass


@params(api = 'gl')
def glPopClientAttrib():
	pass


@params('vaobj', 'first', 'count', 'buffers', 'offsets', 'strides', api='gl')
def glVertexArrayVertexBuffers(vaobj, first, count, buffers, offsets, strides):
	pass


@params('program', 'pname', 'value', api='gl')
def glProgramParameteri(program, pname, value):
	pass


@params('target', 'query', 'v', api='gl')
def glGetMapfv(target, query, v):
	pass


@params('v', api='gl')
def glRasterPos2fv(v):
	pass


@params('barriers', api='gl')
def glMemoryBarrierByRegion(barriers):
	pass


@params('v', api='gl')
def glVertex2sv(v):
	pass


@params('v', api='gl')
def glWindowPos2sv(v):
	pass


@params('type', api='gl')
def glCreateShader(type):
	pass


@params('n', 'renderbuffers', api='gl')
def glGenRenderbuffers(n, renderbuffers):
	pass


@params('target', 'level', 'xoffset', 'yoffset', 'x', 'y', 'width', 'height', api='gl')
def glCopyTexSubImage2D(target, level, xoffset, yoffset, x, y, width, height):
	pass


@params('sfactorRGB', 'dfactorRGB', 'sfactorAlpha', 'dfactorAlpha', api='gl')
def glBlendFuncSeparate(sfactorRGB, dfactorRGB, sfactorAlpha, dfactorAlpha):
	pass


@params('v', api='gl')
def glTexCoord2fv(v):
	pass


@params('v', api='gl')
def glTexCoord4fv(v):
	pass


@params('size', api='gl')
def glPointSize(size):
	pass


@params('unit', 'texture', api='gl')
def glBindTextureUnit(unit, texture):
	pass


@params('pipeline', 'bufSize', 'length', 'infoLog', api='gl')
def glGetProgramPipelineInfoLog(pipeline, bufSize, length, infoLog):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib4Nuiv(index, v):
	pass


@params('sync', 'flags', 'timeout', api='gl')
def glWaitSync(sync, flags, timeout):
	pass


@params('buf', 'modeRGB', 'modeAlpha', api='gl')
def glBlendEquationSeparatei(buf, modeRGB, modeAlpha):
	pass


@params('location', 'x', 'y', 'z', api='gl')
def glUniform3d(location, x, y, z):
	pass


@params('location', 'v0', 'v1', 'v2', api='gl')
def glUniform3f(location, v0, v1, v2):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform3uiv(program, location, count, value):
	pass


@params('program', 'name', api='gl')
def glGetFragDataIndex(program, name):
	pass


@params('v', api='gl')
def glColor3sv(v):
	pass


@params('v', api='gl')
def glVertex4sv(v):
	pass


@params('id', 'target', api='gl')
def glQueryCounter(id, target):
	pass


@params('n', 'framebuffers', api='gl')
def glDeleteFramebuffers(n, framebuffers):
	pass


@params('mode', 'first', 'count', api='gl')
def glDrawArrays(mode, first, count):
	pass


@params('s', 't', 'r', 'q', api='gl')
def glTexCoord4f(s, t, r, q):
	pass


@params('mask', api='gl')
def glClear(mask):
	pass


@params('target', 'n', 'ids', api='gl')
def glCreateQueries(target, n, ids):
	pass


@params('sampler', 'pname', 'params', api='gl')
def glGetSamplerParameterfv(sampler, pname, params):
	pass


@params('x', 'y', 'z', api='gl')
def glTranslatef(x, y, z):
	pass


@params('index', 'x', 'y', 'z', 'w', api='gl')
def glVertexAttrib4Nub(index, x, y, z, w):
	pass


@params('x', 'y', 'z', api='gl')
def glTranslated(x, y, z):
	pass


@params('sampler', 'pname', 'param', api='gl')
def glSamplerParameterIiv(sampler, pname, param):
	pass


@params('mode', 'type', 'indirect', api='gl')
def glDrawElementsIndirect(mode, type, indirect):
	pass


@params('v', api='gl')
def glSecondaryColor3bv(v):
	pass


@params('s', 't', 'r', 'q', api='gl')
def glTexCoord4s(s, t, r, q):
	pass


@params('id', 'pname', 'params', api='gl')
def glGetQueryObjecti64v(id, pname, params):
	pass


@params('program', 'uniformCount', 'constuniformNames', 'uniformIndices', api='gl')
def glGetUniformIndices(program, uniformCount, constuniformNames, uniformIndices):
	pass


@params('v', api='gl')
def glVertex3iv(v):
	pass


@params('coord', 'pname', 'params', api='gl')
def glTexGenfv(coord, pname, params):
	pass


@params('first', 'count', 'buffers', 'offsets', 'strides', api='gl')
def glBindVertexBuffers(first, count, buffers, offsets, strides):
	pass


@params('face', 'pname', 'param', api='gl')
def glMateriali(face, pname, param):
	pass


@params('array', api='gl')
def glIsVertexArray(array):
	pass


@params('index', api='gl')
def glDisableVertexAttribArray(index):
	pass


@params('program', 'storageBlockIndex', 'storageBlockBinding', api='gl')
def glShaderStorageBlockBinding(program, storageBlockIndex, storageBlockBinding):
	pass


@params('face', 'pname', 'param', api='gl')
def glMaterialf(face, pname, param):
	pass


@params('texture', 'levels', 'internalformat', 'width', api='gl')
def glTextureStorage1D(texture, levels, internalformat, width):
	pass


@params('program', 'programInterface', 'pname', 'params', api='gl')
def glGetProgramInterfaceiv(program, programInterface, pname, params):
	pass


@params('buffer', 'access', api='gl')
def glMapNamedBuffer(buffer, access):
	pass


@params('program', 'location', 'bufSize', 'params', api='gl')
def glGetnUniformdv(program, location, bufSize, params):
	pass


@params('target', 'first', 'count', 'buffers', api='gl')
def glBindBuffersBase(target, first, count, buffers):
	pass


@params('index', 'pname', 'params', api='gl')
def glGetVertexAttribIiv(index, pname, params):
	pass


@params('type', 'value', api='gl')
def glVertexP4uiv(type, value):
	pass


@params('index', 'v', api='gl')
def glVertexAttribL4dv(index, v):
	pass


@params('pname', 'value', api='gl')
def glPatchParameteri(pname, value):
	pass


@params('target', 'u1', 'u2', 'stride', 'order', 'points', api='gl')
def glMap1d(target, u1, u2, stride, order, points):
	pass


@params('target', 'u1', 'u2', 'stride', 'order', 'points', api='gl')
def glMap1f(target, u1, u2, stride, order, points):
	pass


@params('framebuffer', 'attachment', 'pname', 'params', api='gl')
def glGetNamedFramebufferAttachmentParameteriv(framebuffer, attachment, pname, params):
	pass


@params('target', 'format', 'type', 'rowBufSize', 'row', 'columnBufSize', 'column', 'span', api='gl')
def glGetnSeparableFilter(target, format, type, rowBufSize, row, columnBufSize, column, span):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib4sv(index, v):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform1dv(program, location, count, value):
	pass


@params('light', 'pname', 'param', api='gl')
def glLighti(light, pname, param):
	pass


@params('target', 'level', 'internalformat', 'width', 'border', 'format', 'type', 'pixels', api='gl')
def glTexImage1D(target, level, internalformat, width, border, format, type, pixels):
	pass


@params('light', 'pname', 'param', api='gl')
def glLightf(light, pname, param):
	pass


@params('value', 'invert', api='gl')
def glSampleCoverage(value, invert):
	pass


@params('v', api='gl')
def glSecondaryColor3usv(v):
	pass


@params('xfb', 'pname', 'index', 'param', api='gl')
def glGetTransformFeedbacki_v(xfb, pname, index, param):
	pass


@params('location', 'v0', 'v1', api='gl')
def glUniform2i(location, v0, v1):
	pass


@params('un', 'u1', 'u2', 'vn', 'v1', 'v2', api='gl')
def glMapGrid2f(un, u1, u2, vn, v1, v2):
	pass


@params('index', 'x', api='gl')
def glVertexAttribL1d(index, x):
	pass


@params('target', 'attachment', 'texture', 'level', 'layer', api='gl')
def glFramebufferTextureLayer(target, attachment, texture, level, layer):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform2fv(program, location, count, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix2x4dv(program, location, count, transpose, value):
	pass


@params('target', 'pname', 'param', api='gl')
def glTexEnvf(target, pname, param):
	pass


@params('target', 'index', 'data', api='gl')
def glGetInteger64i_v(target, index, data):
	pass


@params('target', 'pname', 'param', api='gl')
def glTexEnvi(target, pname, param):
	pass


@params('srcX0', 'srcY0', 'srcX1', 'srcY1', 'dstX0', 'dstY0', 'dstX1', 'dstY1', 'mask', 'filter', api='gl')
def glBlitFramebuffer(srcX0, srcY0, srcX1, srcY1, dstX0, dstY0, dstX1, dstY1, mask, filter):
	pass


@params('target', 'index', api='gl')
def glIsEnabledi(target, index):
	pass


@params('s', 't', api='gl')
def glTexCoord2i(s, t):
	pass


@params('index', 'type', 'normalized', 'value', api='gl')
def glVertexAttribP2ui(index, type, normalized, value):
	pass


@params('target', 'query', 'v', api='gl')
def glGetMapiv(target, query, v):
	pass


@params('ptr', 'length', 'label', api='gl')
def glObjectPtrLabel(ptr, length, label):
	pass


@params('count', 'bufSize', 'sources', 'types', 'ids', 'severities', 'lengths', 'messageLog', api='gl')
def glGetDebugMessageLog(count, bufSize, sources, types, ids, severities, lengths, messageLog):
	pass


@params('program', 'color', 'name', api='gl')
def glBindFragDataLocation(program, color, name):
	pass


@params('v', api='gl')
def glSecondaryColor3ubv(v):
	pass


@params('pname', 'param', api='gl')
def glLightModelf(pname, param):
	pass


@params('mode', 'type', 'indirect', 'drawcount', 'stride', api='gl')
def glMultiDrawElementsIndirect(mode, type, indirect, drawcount, stride):
	pass


@params('n', 'type', 'lists', api='gl')
def glCallLists(n, type, lists):
	pass


@params('left', 'right', 'bottom', 'top', 'zNear', 'zFar', api='gl')
def glFrustum(left, right, bottom, top, zNear, zFar):
	pass


@params('s', 't', 'r', api='gl')
def glTexCoord3i(s, t, r):
	pass


@params('index', 'v', api='gl')
def glVertexAttribI3uiv(index, v):
	pass


@params('source', 'id', 'length', 'message', api='gl')
def glPushDebugGroup(source, id, length, message):
	pass


@params('texture', 'type', 'coords', api='gl')
def glMultiTexCoordP1uiv(texture, type, coords):
	pass


@params('target', 'level', 'xoffset', 'yoffset', 'zoffset', 'x', 'y', 'width', 'height', api='gl')
def glCopyTexSubImage3D(target, level, xoffset, yoffset, zoffset, x, y, width, height):
	pass


@params('program', 'uniformBlockIndex', 'bufSize', 'length', 'uniformBlockName', api='gl')
def glGetActiveUniformBlockName(program, uniformBlockIndex, bufSize, length, uniformBlockName):
	pass


@params('s', 't', 'r', api='gl')
def glTexCoord3s(s, t, r):
	pass


@params('n', 'textures', 'residences', api='gl')
def glAreTexturesResident(n, textures, residences):
	pass


@params('program', 'location', 'v0', 'v1', api='gl')
def glProgramUniform2d(program, location, v0, v1):
	pass


@params('program', 'location', 'v0', 'v1', api='gl')
def glProgramUniform2f(program, location, v0, v1):
	pass


@params('v', api='gl')
def glRasterPos4sv(v):
	pass


@params('red', 'green', 'blue', 'alpha', api='gl')
def glColor4s(red, green, blue, alpha):
	pass


@params('array', api='gl')
def glBindVertexArray(array):
	pass


@params('red', 'green', 'blue', 'alpha', api='gl')
def glColor4b(red, green, blue, alpha):
	pass


@params('red', 'green', 'blue', 'alpha', api='gl')
def glColor4f(red, green, blue, alpha):
	pass


@params('red', 'green', 'blue', 'alpha', api='gl')
def glColor4d(red, green, blue, alpha):
	pass


@params('red', 'green', 'blue', 'alpha', api='gl')
def glColor4i(red, green, blue, alpha):
	pass


@params('buffer', 'offset', 'size', 'data', api='gl')
def glNamedBufferSubData(buffer, offset, size, data):
	pass


@params('v', api='gl')
def glVertex2dv(v):
	pass


@params('target', 'framebuffer', api='gl')
def glBindFramebuffer(target, framebuffer):
	pass


@params('v1', 'v2', api='gl')
def glRectfv(v1, v2):
	pass


@params('location', 'count', 'transpose', 'value', api='gl')
def glUniformMatrix2x4dv(location, count, transpose, value):
	pass


@params('program', 'programInterface', 'name', api='gl')
def glGetProgramResourceLocationIndex(program, programInterface, name):
	pass


@params('x', 'y', 'width', 'height', api='gl')
def glViewport(x, y, width, height):
	pass


@params('renderbuffer', api='gl')
def glIsRenderbuffer(renderbuffer):
	pass


@params('target', 'samples', 'internalformat', 'width', 'height', 'fixedsamplelocations', api='gl')
def glTexStorage2DMultisample(target, samples, internalformat, width, height, fixedsamplelocations):
	pass


@params('program', 'shadertype', 'index', 'pname', 'values', api='gl')
def glGetActiveSubroutineUniformiv(program, shadertype, index, pname, values):
	pass


@params('target', 'internalformat', 'buffer', api='gl')
def glTexBuffer(target, internalformat, buffer):
	pass


@params('i', api='gl')
def glArrayElement(i):
	pass


@params('program', api='gl')
def glValidateProgram(program):
	pass


@params('pipeline', 'program', api='gl')
def glActiveShaderProgram(pipeline, program):
	pass


@params('texture', 'type', 'coords', api='gl')
def glMultiTexCoordP2uiv(texture, type, coords):
	pass


@params('x1', 'y1', 'x2', 'y2', api='gl')
def glRecti(x1, y1, x2, y2):
	pass


@params('x1', 'y1', 'x2', 'y2', api='gl')
def glRectf(x1, y1, x2, y2):
	pass


@params('x1', 'y1', 'x2', 'y2', api='gl')
def glRectd(x1, y1, x2, y2):
	pass


@params('target', 'texture', api='gl')
def glBindTexture(target, texture):
	pass


@params('x1', 'y1', 'x2', 'y2', api='gl')
def glRects(x1, y1, x2, y2):
	pass


@params('program', 'shader', api='gl')
def glDetachShader(program, shader):
	pass


@params('texture', 'level', 'xoffset', 'yoffset', 'width', 'height', 'format', 'type', 'pixels', api='gl')
def glTextureSubImage2D(texture, level, xoffset, yoffset, width, height, format, type, pixels):
	pass


@params('program', 'programInterface', 'name', api='gl')
def glGetProgramResourceLocation(program, programInterface, name):
	pass


@params('index', 'v', api='gl')
def glViewportIndexedfv(index, v):
	pass


@params('mode', 'count', 'type', 'indices', 'basevertex', api='gl')
def glDrawElementsBaseVertex(mode, count, type, indices, basevertex):
	pass


@params('target', 'internalformat', 'offset', 'size', 'format', 'type', 'data', api='gl')
def glClearBufferSubData(target, internalformat, offset, size, format, type, data):
	pass


@params('target', 'levels', 'internalformat', 'width', api='gl')
def glTexStorage1D(target, levels, internalformat, width):
	pass


@params('program', 'location', 'params', api='gl')
def glGetUniformiv(program, location, params):
	pass


@params('target', 'buffer', api='gl')
def glBindBuffer(target, buffer):
	pass


@params('location', 'v0', 'v1', 'v2', 'v3', api='gl')
def glUniform4ui(location, v0, v1, v2, v3):
	pass


@params('coord', 'pname', 'param', api='gl')
def glTexGenf(coord, pname, param):
	pass


@params('coord', 'pname', 'param', api='gl')
def glTexGend(coord, pname, param):
	pass


@params('coord', 'pname', 'param', api='gl')
def glTexGeni(coord, pname, param):
	pass


@params('index', 'left', 'bottom', 'width', 'height', api='gl')
def glScissorIndexed(index, left, bottom, width, height):
	pass


@params('v', api='gl')
def glRasterPos4dv(v):
	pass


@params('v', api='gl')
def glRasterPos2dv(v):
	pass


@params('v', api='gl')
def glTexCoord2iv(v):
	pass


@params('type', 'count', 'conststrings', api='gl')
def glCreateShaderProgramv(type, count, conststrings):
	pass


@params('id', 'pname', 'params', api='gl')
def glGetQueryObjectiv(id, pname, params):
	pass


@params('x', 'y', api='gl')
def glVertex2s(x, y):
	pass


@params('target', api='gl')
def glGenerateMipmap(target):
	pass


@params('texture', 'level', 'xoffset', 'yoffset', 'width', 'height', 'format', 'imageSize', 'data', api='gl')
def glCompressedTextureSubImage2D(texture, level, xoffset, yoffset, width, height, format, imageSize, data):
	pass


@params('list', 'range', api='gl')
def glDeleteLists(list, range):
	pass


@params('pname', 'param', api='gl')
def glPointParameteri(pname, param):
	pass


@params('v', api='gl')
def glColor4iv(v):
	pass


@params('target', api='gl')
def glUnmapBuffer(target):
	pass


@params('pname', 'param', api='gl')
def glPointParameterf(pname, param):
	pass


@params('s', 't', api='gl')
def glTexCoord2s(s, t):
	pass


@params('v', api='gl')
def glTexCoord4dv(v):
	pass


@params('v', api='gl')
def glNormal3dv(v):
	pass


@params(api = 'gl')
def glReleaseShaderCompiler():
	pass


@params('v', api='gl')
def glTexCoord1dv(v):
	pass


@params('x', 'y', 'width', 'height', 'format', 'type', 'pixels', api='gl')
def glReadPixels(x, y, width, height, format, type, pixels):
	pass


@params('renderbuffer', 'samples', 'internalformat', 'width', 'height', api='gl')
def glNamedRenderbufferStorageMultisample(renderbuffer, samples, internalformat, width, height):
	pass


@params('index', 'v', api='gl')
def glVertexAttribI3iv(index, v):
	pass


@params('mode', api='gl')
def glShadeModel(mode):
	pass


@params('un', 'u1', 'u2', api='gl')
def glMapGrid1d(un, u1, u2):
	pass


@params('framebuffer', 'numAttachments', 'attachments', api='gl')
def glInvalidateNamedFramebufferData(framebuffer, numAttachments, attachments):
	pass


@params('v1', 'v2', api='gl')
def glRectiv(v1, v2):
	pass


@params('type', 'color', api='gl')
def glColorP4ui(type, color):
	pass


@params('pipeline', 'stages', 'program', api='gl')
def glUseProgramStages(pipeline, stages, program):
	pass


@params('v', api='gl')
def glRasterPos3dv(v):
	pass


@params('src', api='gl')
def glReadBuffer(src):
	pass


@params('v', api='gl')
def glColor4ubv(v):
	pass


@params('target', 'offset', 'size', 'data', api='gl')
def glGetBufferSubData(target, offset, size, data):
	pass


@params('index', 'pname', 'params', api='gl')
def glGetVertexAttribLdv(index, pname, params):
	pass


@params('program', 'location', 'bufSize', 'params', api='gl')
def glGetnUniformuiv(program, location, bufSize, params):
	pass


@params('n', 'buffers', api='gl')
def glGenBuffers(n, buffers):
	pass


@params('framebuffer', 'buffer', 'drawbuffer', 'value', api='gl')
def glClearNamedFramebufferiv(framebuffer, buffer, drawbuffer, value):
	pass


@params('index', 'v', api='gl')
def glVertexAttribI2iv(index, v):
	pass


@params('framebuffer', api='gl')
def glIsFramebuffer(framebuffer):
	pass


@params('type', 'coords', api='gl')
def glTexCoordP4uiv(type, coords):
	pass


@params('coord', 'pname', 'params', api='gl')
def glTexGendv(coord, pname, params):
	pass


@params('type', 'value', api='gl')
def glVertexP2uiv(type, value):
	pass


@params('s', 't', api='gl')
def glTexCoord2d(s, t):
	pass


@params('target', 'pname', 'params', api='gl')
def glGetBufferParameteri64v(target, pname, params):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform4dv(program, location, count, value):
	pass


@params('s', 't', api='gl')
def glTexCoord2f(s, t):
	pass


@params('target', 'v', api='gl')
def glMultiTexCoord3fv(target, v):
	pass


@params('n', 'renderbuffers', api='gl')
def glCreateRenderbuffers(n, renderbuffers):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib4Nusv(index, v):
	pass


@params('func', api='gl')
def glDepthFunc(func):
	pass


@params('sampler', 'pname', 'param', api='gl')
def glSamplerParameterf(sampler, pname, param):
	pass


@params('buf', 'src', 'dst', api='gl')
def glBlendFunci(buf, src, dst):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib3dv(index, v):
	pass


@params('target', 'size', 'data', 'flags', api='gl')
def glBufferStorage(target, size, data, flags):
	pass


@params('target', 'index', 'data', api='gl')
def glGetFloati_v(target, index, data):
	pass


@params('program', 'name', api='gl')
def glGetUniformLocation(program, name):
	pass


@params('framebuffer', 'n', 'bufs', api='gl')
def glNamedFramebufferDrawBuffers(framebuffer, n, bufs):
	pass


@params('location', 'count', 'value', api='gl')
def glUniform4fv(location, count, value):
	pass


@params('index', 'type', 'normalized', 'value', api='gl')
def glVertexAttribP4uiv(index, type, normalized, value):
	pass


@params('texture', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth', 'format', 'imageSize', 'data', api='gl')
def glCompressedTextureSubImage3D(texture, level, xoffset, yoffset, zoffset, width, height, depth, format, imageSize, data):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib4Nbv(index, v):
	pass


@params(api = 'gl')
def glEndConditionalRender():
	pass


@params('array', api='gl')
def glEnableClientState(array):
	pass


@params('target', 'v', api='gl')
def glMultiTexCoord2sv(target, v):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform2uiv(program, location, count, value):
	pass


@params('id', 'pname', 'params', api='gl')
def glGetQueryObjectuiv(id, pname, params):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib4iv(index, v):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform1uiv(program, location, count, value):
	pass


@params('target', 'attachment', 'texture', 'level', api='gl')
def glFramebufferTexture(target, attachment, texture, level):
	pass


@params('coord', 'pname', 'params', api='gl')
def glGetTexGendv(coord, pname, params):
	pass


@params('v', api='gl')
def glColor3usv(v):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix2x4fv(program, location, count, transpose, value):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform2dv(program, location, count, value):
	pass


@params('v', api='gl')
def glRasterPos2sv(v):
	pass


@params('v', api='gl')
def glTexCoord1sv(v):
	pass


@params('x', 'y', api='gl')
def glVertex2i(x, y):
	pass


@params('pname', 'data', api='gl')
def glGetFloatv(pname, data):
	pass


@params('x', 'y', 'z', api='gl')
def glWindowPos3f(x, y, z):
	pass


@params('type', 'color', api='gl')
def glSecondaryColorP3uiv(type, color):
	pass


@params('pname', 'data', api='gl')
def glGetIntegerv(pname, data):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix3dv(program, location, count, transpose, value):
	pass


@params('id', api='gl')
def glIsQuery(id):
	pass


@params('target', 'level', 'internalformat', 'width', 'height', 'border', 'format', 'type', 'pixels', api='gl')
def glTexImage2D(target, level, internalformat, width, height, border, format, type, pixels):
	pass


@params('width', 'height', 'format', 'type', 'pixels', api='gl')
def glDrawPixels(width, height, format, type, pixels):
	pass


@params('m', api='gl')
def glMultMatrixd(m):
	pass


@params('m', api='gl')
def glMultMatrixf(m):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib4Nubv(index, v):
	pass


@params('v', api='gl')
def glColor4usv(v):
	pass


@params('un', 'u1', 'u2', api='gl')
def glMapGrid1f(un, u1, u2):
	pass


@params('mask', api='gl')
def glPolygonStipple(mask):
	pass


@params('format', 'stride', 'pointer', api='gl')
def glInterleavedArrays(format, stride, pointer):
	pass


@params('program', 'shadertype', 'name', api='gl')
def glGetSubroutineUniformLocation(program, shadertype, name):
	pass


@params('target', 'pname', 'params', api='gl')
def glGetFramebufferParameteriv(target, pname, params):
	pass


@params('map', 'mapsize', 'values', api='gl')
def glPixelMapusv(map, mapsize, values):
	pass


@params('sampler', 'pname', 'params', api='gl')
def glGetSamplerParameteriv(sampler, pname, params):
	pass


@params('readTarget', 'writeTarget', 'readOffset', 'writeOffset', 'size', api='gl')
def glCopyBufferSubData(readTarget, writeTarget, readOffset, writeOffset, size):
	pass


@params('index', 'v', api='gl')
def glVertexAttribI1uiv(index, v):
	pass


@params('v', api='gl')
def glColor3fv(v):
	pass


@params('program', 'index', 'bufSize', 'length', 'size', 'type', 'name', api='gl')
def glGetActiveUniform(program, index, bufSize, length, size, type, name):
	pass


@params('framebuffer', 'attachment', 'texture', 'level', 'layer', api='gl')
def glNamedFramebufferTextureLayer(framebuffer, attachment, texture, level, layer):
	pass


@params('index', 'x', 'y', 'z', api='gl')
def glVertexAttribL3d(index, x, y, z):
	pass


@params('v', api='gl')
def glTexCoord3sv(v):
	pass


@params('value', api='gl')
def glMinSampleShading(value):
	pass


@params('v', api='gl')
def glVertex2fv(v):
	pass


@params('target', 'attachment', 'renderbuffertarget', 'renderbuffer', api='gl')
def glFramebufferRenderbuffer(target, attachment, renderbuffertarget, renderbuffer):
	pass


@params('target', 'index', 'data', api='gl')
def glGetDoublei_v(target, index, data):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib1sv(index, v):
	pass


@params('unit', 'sampler', api='gl')
def glBindSampler(unit, sampler):
	pass


@params('width', api='gl')
def glLineWidth(width):
	pass


@params('target', 'index', 'data', api='gl')
def glGetIntegeri_v(target, index, data):
	pass


@params('program', 'index', 'bufSize', 'length', 'size', 'type', 'name', api='gl')
def glGetTransformFeedbackVarying(program, index, bufSize, length, size, type, name):
	pass


@params('v', api='gl')
def glWindowPos2iv(v):
	pass


@params('pname', 'params', api='gl')
def glFogiv(pname, params):
	pass


@params('pname', 'params', api='gl')
def glLightModeliv(pname, params):
	pass


@params('n', 'f', api='gl')
def glDepthRangef(n, f):
	pass


@params('target', 'index', api='gl')
def glEnablei(target, index):
	pass


@params('u', api='gl')
def glEvalCoord1fv(u):
	pass


@params('maskNumber', 'mask', api='gl')
def glSampleMaski(maskNumber, mask):
	pass


@params('location', 'count', 'transpose', 'value', api='gl')
def glUniformMatrix3x2fv(location, count, transpose, value):
	pass


@params('target', 'internalformat', 'pname', 'bufSize', 'params', api='gl')
def glGetInternalformativ(target, internalformat, pname, bufSize, params):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib2dv(index, v):
	pass


@params('flag', api='gl')
def glEdgeFlag(flag):
	pass


@params('program', 'location', 'v0', api='gl')
def glProgramUniform1ui(program, location, v0):
	pass


@params('x', 'y', 'z', api='gl')
def glVertex3d(x, y, z):
	pass


@params('x', 'y', 'z', api='gl')
def glVertex3f(x, y, z):
	pass


@params('x', 'y', 'z', api='gl')
def glVertex3s(x, y, z):
	pass


@params('type', 'coords', api='gl')
def glTexCoordP2ui(type, coords):
	pass


@params('index', 'r', 'g', 'b', 'a', api='gl')
def glColorMaski(index, r, g, b, a):
	pass


@params('readBuffer', 'writeBuffer', 'readOffset', 'writeOffset', 'size', api='gl')
def glCopyNamedBufferSubData(readBuffer, writeBuffer, readOffset, writeOffset, size):
	pass


@params('target', 'levels', 'internalformat', 'width', 'height', 'depth', api='gl')
def glTexStorage3D(target, levels, internalformat, width, height, depth):
	pass


@params('texture', 'pname', 'param', api='gl')
def glTextureParameteriv(texture, pname, param):
	pass


@params('location', 'count', 'transpose', 'value', api='gl')
def glUniformMatrix3x4fv(location, count, transpose, value):
	pass


@params('type', 'stride', 'pointer', api='gl')
def glNormalPointer(type, stride, pointer):
	pass


@params('framebuffer', 'attachment', 'texture', 'level', api='gl')
def glNamedFramebufferTexture(framebuffer, attachment, texture, level):
	pass


@params('token', api='gl')
def glPassThrough(token):
	pass


@params('type', 'color', api='gl')
def glSecondaryColorP3ui(type, color):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix4x3fv(program, location, count, transpose, value):
	pass


@params('mode', api='gl')
def glBegin(mode):
	pass


@params('u', api='gl')
def glEvalCoord2dv(u):
	pass


@params('v', api='gl')
def glColor3ubv(v):
	pass


@params('type', 'value', api='gl')
def glVertexP3ui(type, value):
	pass


@params('light', 'pname', 'params', api='gl')
def glLightfv(light, pname, params):
	pass


@params('program', 'uniformIndex', 'bufSize', 'length', 'uniformName', api='gl')
def glGetActiveUniformName(program, uniformIndex, bufSize, length, uniformName):
	pass


@params('target', 'attachment', 'pname', 'params', api='gl')
def glGetFramebufferAttachmentParameteriv(target, attachment, pname, params):
	pass


@params('target', 's', 't', api='gl')
def glMultiTexCoord2f(target, s, t):
	pass


@params('framebuffer', 'buf', api='gl')
def glNamedFramebufferDrawBuffer(framebuffer, buf):
	pass


@params('target', 'pname', 'params', api='gl')
def glTexParameteriv(target, pname, params):
	pass


@params('vaobj', 'bindingindex', 'buffer', 'offset', 'stride', api='gl')
def glVertexArrayVertexBuffer(vaobj, bindingindex, buffer, offset, stride):
	pass


@params('target', 'level', 'format', 'type', 'pixels', api='gl')
def glGetTexImage(target, level, format, type, pixels):
	pass


@params('xfb', 'index', 'buffer', api='gl')
def glTransformFeedbackBufferBase(xfb, index, buffer):
	pass


@params('c', api='gl')
def glIndexsv(c):
	pass


@params('type', 'coords', api='gl')
def glTexCoordP3uiv(type, coords):
	pass


@params('width', 'height', 'xorig', 'yorig', 'xmove', 'ymove', 'bitmap', api='gl')
def glBitmap(width, height, xorig, yorig, xmove, ymove, bitmap):
	pass


@params('buffer', 'offset', 'size', 'data', api='gl')
def glGetNamedBufferSubData(buffer, offset, size, data):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform2iv(program, location, count, value):
	pass


@params('target', 'pname', 'params', api='gl')
def glGetQueryiv(target, pname, params):
	pass


@params('xfb', 'pname', 'param', api='gl')
def glGetTransformFeedbackiv(xfb, pname, param):
	pass


@params('s', 't', 'r', 'q', api='gl')
def glTexCoord4i(s, t, r, q):
	pass


@params('identifier', 'name', 'length', 'label', api='gl')
def glObjectLabel(identifier, name, length, label):
	pass


@params('pname', 'params', api='gl')
def glPointParameteriv(pname, params):
	pass


@params('v', api='gl')
def glNormal3fv(v):
	pass


@params('v', api='gl')
def glTexCoord1fv(v):
	pass


@params('target', 'v', api='gl')
def glMultiTexCoord1dv(target, v):
	pass


@params('v', api='gl')
def glTexCoord3fv(v):
	pass


@params('texture', 'type', 'coords', api='gl')
def glMultiTexCoordP3uiv(texture, type, coords):
	pass


@params('index', 'type', 'normalized', 'value', api='gl')
def glVertexAttribP3ui(index, type, normalized, value):
	pass


@params('near', 'far', api='gl')
def glDepthRange(near, far):
	pass


@params('buf', api='gl')
def glDrawBuffer(buf):
	pass


@params('map', 'bufSize', 'values', api='gl')
def glGetnPixelMapusv(map, bufSize, values):
	pass


@params('v', api='gl')
def glRasterPos3fv(v):
	pass


@params('buffer', 'drawbuffer', 'value', api='gl')
def glClearBufferuiv(buffer, drawbuffer, value):
	pass


@params('target', 'internalformat', 'pname', 'bufSize', 'params', api='gl')
def glGetInternalformati64v(target, internalformat, pname, bufSize, params):
	pass


@params('c', api='gl')
def glClearIndex(c):
	pass


@params('index', 'size', 'type', 'stride', 'pointer', api='gl')
def glVertexAttribIPointer(index, size, type, stride, pointer):
	pass


@params(api = 'gl')
def glFlush():
	pass


@params('mode', 'count', 'type', 'indices', 'instancecount', 'basevertex', 'baseinstance', api='gl')
def glDrawElementsInstancedBaseVertexBaseInstance(mode, count, type, indices, instancecount, basevertex, baseinstance):
	pass


@params('target', 'level', 'pname', 'params', api='gl')
def glGetTexLevelParameteriv(target, level, pname, params):
	pass


@params('n', 'textures', 'priorities', api='gl')
def glPrioritizeTextures(n, textures, priorities):
	pass


@params('size', 'buffer', api='gl')
def glSelectBuffer(size, buffer):
	pass


@params('target', 'samples', 'internalformat', 'width', 'height', 'depth', 'fixedsamplelocations', api='gl')
def glTexStorage3DMultisample(target, samples, internalformat, width, height, depth, fixedsamplelocations):
	pass


@params('target', 'clamp', api='gl')
def glClampColor(target, clamp):
	pass


@params('s', api='gl')
def glClearStencil(s):
	pass


@params('type', 'coords', api='gl')
def glTexCoordP1uiv(type, coords):
	pass


@params('texture', api='gl')
def glIsTexture(texture):
	pass


@params('x', 'y', api='gl')
def glVertex2f(x, y):
	pass


@params('x', 'y', api='gl')
def glVertex2d(x, y):
	pass


@params('target', 'index', 'id', api='gl')
def glBeginQueryIndexed(target, index, id):
	pass


@params('factor', 'units', api='gl')
def glPolygonOffset(factor, units):
	pass


@params('target', 'level', 'internalformat', 'width', 'height', 'depth', 'border', 'format', 'type', 'pixels', api='gl')
def glTexImage3D(target, level, internalformat, width, height, depth, border, format, type, pixels):
	pass


@params('program', 'pname', 'params', api='gl')
def glGetProgramiv(program, pname, params):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform4fv(program, location, count, value):
	pass


@params('target', 'offset', 'length', api='gl')
def glFlushMappedBufferRange(target, offset, length):
	pass


@params('target', 'levels', 'internalformat', 'width', 'height', api='gl')
def glTexStorage2D(target, levels, internalformat, width, height):
	pass


@params('n', 'ids', api='gl')
def glGenQueries(n, ids):
	pass


@params('map', 'values', api='gl')
def glGetPixelMapfv(map, values):
	pass


@params('target', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth', 'format', 'type', 'pixels', api='gl')
def glTexSubImage3D(target, level, xoffset, yoffset, zoffset, width, height, depth, format, type, pixels):
	pass


@params('count', 'samplers', api='gl')
def glDeleteSamplers(count, samplers):
	pass


@params('texture', 'pname', 'params', api='gl')
def glGetTextureParameterfv(texture, pname, params):
	pass


@params('mode', api='gl')
def glMatrixMode(mode):
	pass


@params('first', 'count', 'textures', api='gl')
def glBindTextures(first, count, textures):
	pass


@params('pname', 'data', api='gl')
def glGetDoublev(pname, data):
	pass


@params('index', 'x', api='gl')
def glVertexAttrib1d(index, x):
	pass


@params('location', 'count', 'value', api='gl')
def glUniform4dv(location, count, value):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform3dv(program, location, count, value):
	pass


@params('buffer', api='gl')
def glInvalidateBufferData(buffer):
	pass


@params('texture', 'level', 'xoffset', 'width', 'format', 'imageSize', 'data', api='gl')
def glCompressedTextureSubImage1D(texture, level, xoffset, width, format, imageSize, data):
	pass


@params('texture', 'level', 'format', 'type', 'data', api='gl')
def glClearTexImage(texture, level, format, type, data):
	pass


@params('location', 'count', 'value', api='gl')
def glUniform3fv(location, count, value):
	pass


@params('texture', 'type', 'coords', api='gl')
def glMultiTexCoordP1ui(texture, type, coords):
	pass


@params('xfb', 'pname', 'index', 'param', api='gl')
def glGetTransformFeedbacki64_v(xfb, pname, index, param):
	pass


@params('mode', 'count', 'type', 'constindices', 'drawcount', api='gl')
def glMultiDrawElements(mode, count, type, constindices, drawcount):
	pass


@params('n', 'bufs', api='gl')
def glDrawBuffers(n, bufs):
	pass


@params('framebuffer', 'src', api='gl')
def glNamedFramebufferReadBuffer(framebuffer, src):
	pass


@params('coord', 'pname', 'params', api='gl')
def glGetTexGenfv(coord, pname, params):
	pass


@params('target', 'id', api='gl')
def glBindTransformFeedback(target, id):
	pass


@params('target', 'v', api='gl')
def glMultiTexCoord2iv(target, v):
	pass


@params('red', 'green', 'blue', api='gl')
def glSecondaryColor3f(red, green, blue):
	pass


@params('v', api='gl')
def glRasterPos3iv(v):
	pass


@params('type', 'value', api='gl')
def glVertexP2ui(type, value):
	pass


@params('target', 'format', 'type', 'bufSize', 'image', api='gl')
def glGetnConvolutionFilter(target, format, type, bufSize, image):
	pass


@params('red', 'green', 'blue', api='gl')
def glSecondaryColor3b(red, green, blue):
	pass


@params('v', api='gl')
def glTexCoord4sv(v):
	pass


@params('location', 'count', 'value', api='gl')
def glUniform2uiv(location, count, value):
	pass


@params(api = 'gl')
def glFinish():
	pass


@params('x', 'y', api='gl')
def glRasterPos2s(x, y):
	pass


@params('location', 'count', 'value', api='gl')
def glUniform1uiv(location, count, value):
	pass


@params('location', 'count', 'transpose', 'value', api='gl')
def glUniformMatrix2dv(location, count, transpose, value):
	pass


@params('c', api='gl')
def glIndexdv(c):
	pass


@params('v', api='gl')
def glTexCoord3iv(v):
	pass


@params('depth', api='gl')
def glClearDepth(depth):
	pass


@params('location', 'count', 'transpose', 'value', api='gl')
def glUniformMatrix4dv(location, count, transpose, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix4x3dv(program, location, count, transpose, value):
	pass


@params('v', api='gl')
def glVertex4dv(v):
	pass


@params('target', 'n', 'textures', api='gl')
def glCreateTextures(target, n, textures):
	pass


@params('n', 'buffers', api='gl')
def glCreateBuffers(n, buffers):
	pass


@params('m', api='gl')
def glMultTransposeMatrixf(m):
	pass


@params('flag', api='gl')
def glEdgeFlagv(flag):
	pass


@params('location', 'count', 'transpose', 'value', api='gl')
def glUniformMatrix4x3dv(location, count, transpose, value):
	pass


@params('n', 'ids', api='gl')
def glDeleteQueries(n, ids):
	pass


@params('type', 'coords', api='gl')
def glNormalP3uiv(type, coords):
	pass


@params('x', 'y', api='gl')
def glRasterPos2d(x, y):
	pass


@params(api = 'gl')
def glInitNames():
	pass


@params('v', api='gl')
def glColor3dv(v):
	pass


@params('target', 'reset', 'format', 'type', 'bufSize', 'values', api='gl')
def glGetnMinmax(target, reset, format, type, bufSize, values):
	pass


@params('framebuffer', 'buffer', 'drawbuffer', 'value', api='gl')
def glClearNamedFramebufferuiv(framebuffer, buffer, drawbuffer, value):
	pass


@params('index', 'pname', 'params', api='gl')
def glGetVertexAttribfv(index, pname, params):
	pass


@params('num_groups_x', 'num_groups_y', 'num_groups_z', api='gl')
def glDispatchCompute(num_groups_x, num_groups_y, num_groups_z):
	pass


@params('program', 'index', 'bufSize', 'length', 'size', 'type', 'name', api='gl')
def glGetActiveAttrib(program, index, bufSize, length, size, type, name):
	pass


@params('location', 'v0', 'v1', 'v2', api='gl')
def glUniform3i(location, v0, v1, v2):
	pass


@params('target', 'level', 'xoffset', 'yoffset', 'width', 'height', 'format', 'type', 'pixels', api='gl')
def glTexSubImage2D(target, level, xoffset, yoffset, width, height, format, type, pixels):
	pass


@params('opcode', api='gl')
def glLogicOp(opcode):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix3x4fv(program, location, count, transpose, value):
	pass


@params('pname', 'param', api='gl')
def glPixelTransferf(pname, param):
	pass


@params('texture', 'pname', 'params', api='gl')
def glGetTextureParameterIuiv(texture, pname, params):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix4dv(program, location, count, transpose, value):
	pass


@params('location', 'count', 'transpose', 'value', api='gl')
def glUniformMatrix3x4dv(location, count, transpose, value):
	pass


@params('mode', 'id', 'stream', api='gl')
def glDrawTransformFeedbackStream(mode, id, stream):
	pass


@params('location', 'v0', 'v1', 'v2', api='gl')
def glUniform3ui(location, v0, v1, v2):
	pass


@params('mode', api='gl')
def glProvokingVertex(mode):
	pass


@params('count', 'shaders', 'binaryformat', 'binary', 'length', api='gl')
def glShaderBinary(count, shaders, binaryformat, binary, length):
	pass


@params('coord', 'pname', 'params', api='gl')
def glTexGeniv(coord, pname, params):
	pass


@params('mode', 'count', 'type', 'indices', api='gl')
def glDrawElements(mode, count, type, indices):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform4iv(program, location, count, value):
	pass


@params('texture', api='gl')
def glClientActiveTexture(texture):
	pass


@params('location', 'count', 'value', api='gl')
def glUniform1iv(location, count, value):
	pass


@params('mode', 'first', 'count', 'instancecount', api='gl')
def glDrawArraysInstanced(mode, first, count, instancecount):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib4uiv(index, v):
	pass


@params('target', 'index', api='gl')
def glEndQueryIndexed(target, index):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform1iv(program, location, count, value):
	pass


@params('target', 'renderbuffer', api='gl')
def glBindRenderbuffer(target, renderbuffer):
	pass


@params('face', 'pname', 'params', api='gl')
def glMaterialiv(face, pname, params):
	pass


@params('program', api='gl')
def glIsProgram(program):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib4fv(index, v):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix2x3dv(program, location, count, transpose, value):
	pass


@params('map', 'bufSize', 'values', api='gl')
def glGetnPixelMapfv(map, bufSize, values):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib2fv(index, v):
	pass


@params('array', api='gl')
def glDisableClientState(array):
	pass


@params('v', api='gl')
def glColor4uiv(v):
	pass


@params('program', 'location', 'v0', 'v1', 'v2', api='gl')
def glProgramUniform3i(program, location, v0, v1, v2):
	pass


@params('mode', 'i1', 'i2', 'j1', 'j2', api='gl')
def glEvalMesh2(mode, i1, i2, j1, j2):
	pass


@params('mode', 'i1', 'i2', api='gl')
def glEvalMesh1(mode, i1, i2):
	pass


@params('program', 'location', 'v0', 'v1', 'v2', api='gl')
def glProgramUniform3d(program, location, v0, v1, v2):
	pass


@params('u', api='gl')
def glEvalCoord2fv(u):
	pass


@params('m', api='gl')
def glLoadTransposeMatrixd(m):
	pass


@params('m', api='gl')
def glLoadTransposeMatrixf(m):
	pass


@params('index', 'x', api='gl')
def glVertexAttribI1ui(index, x):
	pass


@params('bufSize', 'pattern', api='gl')
def glGetnPolygonStipple(bufSize, pattern):
	pass


@params('texture', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth', api='gl')
def glInvalidateTexSubImage(texture, level, xoffset, yoffset, zoffset, width, height, depth):
	pass


@params('pname', 'data', api='gl')
def glGetInteger64v(pname, data):
	pass


@params('plane', 'equation', api='gl')
def glClipPlane(plane, equation):
	pass


@params('c', api='gl')
def glIndexub(c):
	pass


@params('framebuffer', 'attachment', 'renderbuffertarget', 'renderbuffer', api='gl')
def glNamedFramebufferRenderbuffer(framebuffer, attachment, renderbuffertarget, renderbuffer):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib4Niv(index, v):
	pass


@params('buffer', 'drawbuffer', 'value', api='gl')
def glClearBufferiv(buffer, drawbuffer, value):
	pass


@params('type', 'color', api='gl')
def glColorP4uiv(type, color):
	pass


@params('texture', 'level', 'pname', 'params', api='gl')
def glGetTextureLevelParameterfv(texture, level, pname, params):
	pass


@params('target', 'v', api='gl')
def glMultiTexCoord1fv(target, v):
	pass


@params('sampler', 'pname', 'params', api='gl')
def glGetSamplerParameterIuiv(sampler, pname, params):
	pass


@params('type', 'coords', api='gl')
def glTexCoordP3ui(type, coords):
	pass


@params('location', 'v0', 'v1', api='gl')
def glUniform2f(location, v0, v1):
	pass


@params('texture', 'level', 'xoffset', 'width', 'format', 'type', 'pixels', api='gl')
def glTextureSubImage1D(texture, level, xoffset, width, format, type, pixels):
	pass


@params('x', 'y', 'z', api='gl')
def glWindowPos3s(x, y, z):
	pass


@params('d', api='gl')
def glClearDepthf(d):
	pass


@params('texture', 'internalformat', 'buffer', 'offset', 'size', api='gl')
def glTextureBufferRange(texture, internalformat, buffer, offset, size):
	pass


@params('x', 'y', 'z', api='gl')
def glWindowPos3i(x, y, z):
	pass


@params('x', 'y', 'z', api='gl')
def glWindowPos3d(x, y, z):
	pass


@params('texture', 'type', 'coords', api='gl')
def glMultiTexCoordP4ui(texture, type, coords):
	pass


@params('red', 'green', 'blue', api='gl')
def glColor3us(red, green, blue):
	pass


@params('light', 'pname', 'params', api='gl')
def glGetLightiv(light, pname, params):
	pass


@params('target', 's', 't', 'r', 'q', api='gl')
def glMultiTexCoord4f(target, s, t, r, q):
	pass


@params('red', 'green', 'blue', api='gl')
def glColor3ub(red, green, blue):
	pass


@params('target', 's', 't', 'r', 'q', api='gl')
def glMultiTexCoord4d(target, s, t, r, q):
	pass


@params('red', 'green', 'blue', api='gl')
def glColor3ui(red, green, blue):
	pass


@params('target', 's', 't', 'r', 'q', api='gl')
def glMultiTexCoord4i(target, s, t, r, q):
	pass


@params('mask', api='gl')
def glGetPolygonStipple(mask):
	pass


@params('location', 'x', 'y', api='gl')
def glUniform2d(location, x, y):
	pass


@params('index', 'x', 'y', 'z', 'w', api='gl')
def glVertexAttribI4ui(index, x, y, z, w):
	pass


@params('red', 'green', 'blue', 'alpha', api='gl')
def glColorMask(red, green, blue, alpha):
	pass


@params('target', 'level', 'format', 'type', 'bufSize', 'pixels', api='gl')
def glGetnTexImage(target, level, format, type, bufSize, pixels):
	pass


@params('mode', api='gl')
def glBlendEquation(mode):
	pass


@params('target', 'v', api='gl')
def glMultiTexCoord3dv(target, v):
	pass


@params('v', api='gl')
def glColor4sv(v):
	pass


@params('program', 'programInterface', 'index', 'propCount', 'props', 'bufSize', 'length', 'params', api='gl')
def glGetProgramResourceiv(program, programInterface, index, propCount, props, bufSize, length, params):
	pass


@params('target', 'internalformat', 'format', 'type', 'data', api='gl')
def glClearBufferData(target, internalformat, format, type, data):
	pass


@params('primitiveMode', api='gl')
def glBeginTransformFeedback(primitiveMode):
	pass


@params('v', api='gl')
def glColor3iv(v):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib3sv(index, v):
	pass


@params('target', 'level', 'internalformat', 'width', 'border', 'imageSize', 'data', api='gl')
def glCompressedTexImage1D(target, level, internalformat, width, border, imageSize, data):
	pass


@params('n', 'ids', api='gl')
def glDeleteTransformFeedbacks(n, ids):
	pass


@params('mode', 'start', 'end', 'count', 'type', 'indices', 'basevertex', api='gl')
def glDrawRangeElementsBaseVertex(mode, start, end, count, type, indices, basevertex):
	pass


@params('program', 'index', 'name', api='gl')
def glBindAttribLocation(program, index, name):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib1dv(index, v):
	pass


@params('buf', 'srcRGB', 'dstRGB', 'srcAlpha', 'dstAlpha', api='gl')
def glBlendFuncSeparatei(buf, srcRGB, dstRGB, srcAlpha, dstAlpha):
	pass


@params('location', 'v0', 'v1', api='gl')
def glUniform2ui(location, v0, v1):
	pass


@params('pname', 'param', api='gl')
def glPixelTransferi(pname, param):
	pass


@params('v', api='gl')
def glWindowPos2fv(v):
	pass


@params('target', 'index', api='gl')
def glDisablei(target, index):
	pass


@params('sync', 'pname', 'bufSize', 'length', 'values', api='gl')
def glGetSynciv(sync, pname, bufSize, length, values):
	pass


@params('program', 'location', 'v0', 'v1', api='gl')
def glProgramUniform2i(program, location, v0, v1):
	pass


@params('program', 'bufSize', 'length', 'binaryFormat', 'binary', api='gl')
def glGetProgramBinary(program, bufSize, length, binaryFormat, binary):
	pass


@params('i', api='gl')
def glEvalPoint1(i):
	pass


@params('i', 'j', api='gl')
def glEvalPoint2(i, j):
	pass


@params(api = 'gl')
def glPauseTransformFeedback():
	pass


@params('n', 'ids', api='gl')
def glCreateTransformFeedbacks(n, ids):
	pass


@params('target', 'level', 'xoffset', 'width', 'format', 'type', 'pixels', api='gl')
def glTexSubImage1D(target, level, xoffset, width, format, type, pixels):
	pass


@params('index', 'type', 'normalized', 'value', api='gl')
def glVertexAttribP3uiv(index, type, normalized, value):
	pass


@params('index', 'v', api='gl')
def glVertexAttribI4iv(index, v):
	pass


@params('vaobj', 'pname', 'param', api='gl')
def glGetVertexArrayiv(vaobj, pname, param):
	pass


@params('name', api='gl')
def glLoadName(name):
	pass


@params('m', api='gl')
def glLoadMatrixf(m):
	pass


@params('m', api='gl')
def glLoadMatrixd(m):
	pass


@params('target', 'pname', 'params', api='gl')
def glTexParameterfv(target, pname, params):
	pass


@params('location', 'count', 'value', api='gl')
def glUniform3dv(location, count, value):
	pass


@params('face', 'func', 'ref', 'mask', api='gl')
def glStencilFuncSeparate(face, func, ref, mask):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform3fv(program, location, count, value):
	pass


@params('first', 'count', 'samplers', api='gl')
def glBindSamplers(first, count, samplers):
	pass


@params('id', 'pname', 'params', api='gl')
def glGetQueryObjectui64v(id, pname, params):
	pass


@params('texture', 'level', 'format', 'type', 'bufSize', 'pixels', api='gl')
def glGetTextureImage(texture, level, format, type, bufSize, pixels):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform1fv(program, location, count, value):
	pass


@params('location', 'count', 'transpose', 'value', api='gl')
def glUniformMatrix4fv(location, count, transpose, value):
	pass


@params('n', 'pipelines', api='gl')
def glDeleteProgramPipelines(n, pipelines):
	pass


@params('v', api='gl')
def glVertex3fv(v):
	pass


@params('x', 'y', api='gl')
def glWindowPos2s(x, y):
	pass


@params('x', 'y', api='gl')
def glWindowPos2i(x, y):
	pass


@params('x', 'y', api='gl')
def glWindowPos2f(x, y):
	pass


@params('x', 'y', api='gl')
def glWindowPos2d(x, y):
	pass


@params('shadertype', 'count', 'indices', api='gl')
def glUniformSubroutinesuiv(shadertype, count, indices):
	pass


@params('v1', 'v2', api='gl')
def glRectdv(v1, v2):
	pass


@params('type', 'color', api='gl')
def glColorP3uiv(type, color):
	pass


@params('coord', api='gl')
def glFogCoordfv(coord):
	pass


@params('shader', api='gl')
def glCompileShader(shader):
	pass


@params('c', api='gl')
def glIndexfv(c):
	pass


@params('texture', 'type', 'coords', api='gl')
def glMultiTexCoordP3ui(texture, type, coords):
	pass


@params('v', api='gl')
def glNormal3sv(v):
	pass


@params('target', 'numAttachments', 'attachments', api='gl')
def glInvalidateFramebuffer(target, numAttachments, attachments):
	pass


@params('target', 'level', 'internalformat', 'width', 'height', 'border', 'imageSize', 'data', api='gl')
def glCompressedTexImage2D(target, level, internalformat, width, height, border, imageSize, data):
	pass


@params('index', 'x', api='gl')
def glVertexAttrib1f(index, x):
	pass


@params('v', api='gl')
def glVertex4fv(v):
	pass


@params('framebuffer', 'buffer', 'drawbuffer', 'depth', 'stencil', api='gl')
def glClearNamedFramebufferfi(framebuffer, buffer, drawbuffer, depth, stencil):
	pass


@params('id', 'buffer', 'pname', 'offset', api='gl')
def glGetQueryBufferObjectuiv(id, buffer, pname, offset):
	pass


@params('framebuffer', 'buffer', 'drawbuffer', 'value', api='gl')
def glClearNamedFramebufferfv(framebuffer, buffer, drawbuffer, value):
	pass


@params('index', 'x', api='gl')
def glVertexAttrib1s(index, x):
	pass


@params('target', 'v', api='gl')
def glMultiTexCoord1sv(target, v):
	pass


@params('program', api='gl')
def glDeleteProgram(program):
	pass


@params('v', api='gl')
def glColor4bv(v):
	pass


@params('x', 'y', api='gl')
def glRasterPos2f(x, y):
	pass


@params(api = 'gl')
def glLoadIdentity():
	pass


@params('v', api='gl')
def glRasterPos4iv(v):
	pass


@params('location', 'count', 'transpose', 'value', api='gl')
def glUniformMatrix4x3fv(location, count, transpose, value):
	pass


@params('buffer', 'drawbuffer', 'value', api='gl')
def glClearBufferfv(buffer, drawbuffer, value):
	pass


@params(api = 'gl')
def glTextureBarrier():
	pass


@params('buffer', 'drawbuffer', 'depth', 'stencil', api='gl')
def glClearBufferfi(buffer, drawbuffer, depth, stencil):
	pass


@params('mode', 'indirect', api='gl')
def glDrawArraysIndirect(mode, indirect):
	pass


@params('n', 'arrays', api='gl')
def glGenVertexArrays(n, arrays):
	pass


@params('vaobj', 'index', api='gl')
def glEnableVertexArrayAttrib(vaobj, index):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix3x2dv(program, location, count, transpose, value):
	pass


@params('bindingindex', 'divisor', api='gl')
def glVertexBindingDivisor(bindingindex, divisor):
	pass


@params('sampler', 'pname', 'params', api='gl')
def glGetSamplerParameterIiv(sampler, pname, params):
	pass


@params('location', 'count', 'transpose', 'value', api='gl')
def glUniformMatrix4x2fv(location, count, transpose, value):
	pass


@params('index', 'x', 'y', 'z', api='gl')
def glVertexAttrib3f(index, x, y, z):
	pass


@params('id', 'buffer', 'pname', 'offset', api='gl')
def glGetQueryBufferObjecti64v(id, buffer, pname, offset):
	pass


@params('index', 'pname', 'params', api='gl')
def glGetVertexAttribdv(index, pname, params):
	pass


@params('location', 'v0', api='gl')
def glUniform1ui(location, v0):
	pass


@params('readFramebuffer', 'drawFramebuffer', 'srcX0', 'srcY0', 'srcX1', 'srcY1', 'dstX0', 'dstY0', 'dstX1', 'dstY1', 'mask', 'filter', api='gl')
def glBlitNamedFramebuffer(readFramebuffer, drawFramebuffer, srcX0, srcY0, srcX1, srcY1, dstX0, dstY0, dstX1, dstY1, mask, filter):
	pass


@params('index', 'x', 'y', 'z', api='gl')
def glVertexAttrib3d(index, x, y, z):
	pass


@params('barriers', api='gl')
def glMemoryBarrier(barriers):
	pass


@params('program', 'name', api='gl')
def glGetFragDataLocation(program, name):
	pass


@params('face', 'pname', 'params', api='gl')
def glGetMaterialfv(face, pname, params):
	pass


@params('map', 'mapsize', 'values', api='gl')
def glPixelMapuiv(map, mapsize, values):
	pass


@params('texture', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth', 'format', 'type', 'data', api='gl')
def glClearTexSubImage(texture, level, xoffset, yoffset, zoffset, width, height, depth, format, type, data):
	pass


@params('texture', 'pname', 'params', api='gl')
def glGetTextureParameterIiv(texture, pname, params):
	pass


@params('index', 'v', api='gl')
def glVertexAttribI4ubv(index, v):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix4x2dv(program, location, count, transpose, value):
	pass


@params('shader', api='gl')
def glIsShader(shader):
	pass


@params('cap', api='gl')
def glEnable(cap):
	pass


@params('program', 'uniformCount', 'uniformIndices', 'pname', 'params', api='gl')
def glGetActiveUniformsiv(program, uniformCount, uniformIndices, pname, params):
	pass


@params('buf', 'mode', api='gl')
def glBlendEquationi(buf, mode):
	pass


@params('program', 'name', api='gl')
def glGetAttribLocation(program, name):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib4dv(index, v):
	pass


@params('texture', 'pname', 'params', api='gl')
def glGetTextureParameteriv(texture, pname, params):
	pass


@params('program', 'location', 'v0', 'v1', 'v2', api='gl')
def glProgramUniform3ui(program, location, v0, v1, v2):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix2x3fv(program, location, count, transpose, value):
	pass


@params(api = 'gl')
def glPushMatrix():
	pass


@params('program', 'location', 'v0', api='gl')
def glProgramUniform1i(program, location, v0):
	pass


@params('program', 'location', 'v0', api='gl')
def glProgramUniform1d(program, location, v0):
	pass


@params('program', 'location', 'v0', api='gl')
def glProgramUniform1f(program, location, v0):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform3iv(program, location, count, value):
	pass


@params('c', api='gl')
def glIndexiv(c):
	pass


@params('xfb', 'index', 'buffer', 'offset', 'size', api='gl')
def glTransformFeedbackBufferRange(xfb, index, buffer, offset, size):
	pass


@params('xfactor', 'yfactor', api='gl')
def glPixelZoom(xfactor, yfactor):
	pass


@params('type', 'color', api='gl')
def glColorP3ui(type, color):
	pass


@params('texture', 'type', 'coords', api='gl')
def glMultiTexCoordP4uiv(texture, type, coords):
	pass


@params('texture', 'target', 'origtexture', 'internalformat', 'minlevel', 'numlevels', 'minlayer', 'numlayers', api='gl')
def glTextureView(texture, target, origtexture, internalformat, minlevel, numlevels, minlayer, numlayers):
	pass


@params('vaobj', 'index', api='gl')
def glDisableVertexArrayAttrib(vaobj, index):
	pass


@params('location', 'count', 'value', api='gl')
def glUniform4iv(location, count, value):
	pass


@params('n', 'textures', api='gl')
def glGenTextures(n, textures):
	pass


@params('texture', 'samples', 'internalformat', 'width', 'height', 'fixedsamplelocations', api='gl')
def glTextureStorage2DMultisample(texture, samples, internalformat, width, height, fixedsamplelocations):
	pass


@params('target', 's', api='gl')
def glMultiTexCoord1s(target, s):
	pass


@params('index', 'size', 'type', 'normalized', 'stride', 'pointer', api='gl')
def glVertexAttribPointer(index, size, type, normalized, stride, pointer):
	pass


@params('location', 'v0', api='gl')
def glUniform1f(location, v0):
	pass


@params('index', 'type', 'normalized', 'value', api='gl')
def glVertexAttribP1ui(index, type, normalized, value):
	pass


@params('target', 'v', api='gl')
def glMultiTexCoord4sv(target, v):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix3x4dv(program, location, count, transpose, value):
	pass


@params('texture', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth', 'format', 'type', 'bufSize', 'pixels', api='gl')
def glGetTextureSubImage(texture, level, xoffset, yoffset, zoffset, width, height, depth, format, type, bufSize, pixels):
	pass


@params('renderbuffer', 'pname', 'params', api='gl')
def glGetNamedRenderbufferParameteriv(renderbuffer, pname, params):
	pass


@params('target', 'first', 'count', 'buffers', 'offsets', 'sizes', api='gl')
def glBindBuffersRange(target, first, count, buffers, offsets, sizes):
	pass


@params('program', 'colorNumber', 'index', 'name', api='gl')
def glBindFragDataLocationIndexed(program, colorNumber, index, name):
	pass


@params('target', 'v', api='gl')
def glMultiTexCoord2dv(target, v):
	pass


@params('location', 'count', 'value', api='gl')
def glUniform2iv(location, count, value):
	pass


@params('texture', 'pname', 'param', api='gl')
def glTextureParameterf(texture, pname, param):
	pass


@params('size', 'type', 'buffer', api='gl')
def glFeedbackBuffer(size, type, buffer):
	pass


@params('target', 's', 't', api='gl')
def glMultiTexCoord2i(target, s, t):
	pass


@params('texture', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth', 'format', 'type', 'pixels', api='gl')
def glTextureSubImage3D(texture, level, xoffset, yoffset, zoffset, width, height, depth, format, type, pixels):
	pass


@params('target', 'attachment', 'textarget', 'texture', 'level', api='gl')
def glFramebufferTexture1D(target, attachment, textarget, texture, level):
	pass


@params('shader', 'pname', 'params', api='gl')
def glGetShaderiv(shader, pname, params):
	pass


@params('target', 's', 't', api='gl')
def glMultiTexCoord2d(target, s, t):
	pass


@params('buffer', 'size', 'data', 'flags', api='gl')
def glNamedBufferStorage(buffer, size, data, flags):
	pass


@params('location', 'count', 'value', api='gl')
def glUniform1dv(location, count, value):
	pass


@params('target', 'v', api='gl')
def glMultiTexCoord4fv(target, v):
	pass


@params('x', 'y', 'z', api='gl')
def glRasterPos3i(x, y, z):
	pass


@params('x', 'y', 'z', api='gl')
def glRasterPos3d(x, y, z):
	pass


@params('x', 'y', 'z', api='gl')
def glRasterPos3f(x, y, z):
	pass


@params('target', 'level', 'internalformat', 'width', 'height', 'depth', 'border', 'imageSize', 'data', api='gl')
def glCompressedTexImage3D(target, level, internalformat, width, height, depth, border, imageSize, data):
	pass


@params('index', 'pname', 'params', api='gl')
def glGetVertexAttribiv(index, pname, params):
	pass


@params('target', 'reset', 'format', 'type', 'bufSize', 'values', api='gl')
def glGetnHistogram(target, reset, format, type, bufSize, values):
	pass


@params('location', 'count', 'transpose', 'value', api='gl')
def glUniformMatrix2fv(location, count, transpose, value):
	pass


@params('texture', api='gl')
def glGenerateTextureMipmap(texture):
	pass


@params('mode', 'count', 'type', 'constindices', 'drawcount', 'basevertex', api='gl')
def glMultiDrawElementsBaseVertex(mode, count, type, constindices, drawcount, basevertex):
	pass


@params('v', api='gl')
def glWindowPos3sv(v):
	pass


@params('target', 'level', 'xoffset', 'width', 'format', 'imageSize', 'data', api='gl')
def glCompressedTexSubImage1D(target, level, xoffset, width, format, imageSize, data):
	pass


@params('target', 'pname', 'params', api='gl')
def glGetTexParameterIiv(target, pname, params):
	pass


@params('texture', 'level', api='gl')
def glInvalidateTexImage(texture, level):
	pass


@params('type', 'value', api='gl')
def glVertexP3uiv(type, value):
	pass


@params('target', 'query', 'bufSize', 'v', api='gl')
def glGetnMapdv(target, query, bufSize, v):
	pass


@params('callback', 'userParam', api='gl')
def glDebugMessageCallback(callback, userParam):
	pass


@params('target', 'index', 'data', api='gl')
def glGetBooleani_v(target, index, data):
	pass


@params('texture', 'pname', 'params', api='gl')
def glTextureParameterIiv(texture, pname, params):
	pass


@params('list', 'mode', api='gl')
def glNewList(list, mode):
	pass


@params('target', 'mode', api='gl')
def glHint(target, mode):
	pass


@params('mode', 'indirect', 'drawcount', 'stride', api='gl')
def glMultiDrawArraysIndirect(mode, indirect, drawcount, stride):
	pass


@params('index', 'type', 'normalized', 'value', api='gl')
def glVertexAttribP2uiv(index, type, normalized, value):
	pass


@params('x', 'y', 'z', api='gl')
def glScalef(x, y, z):
	pass


@params('x', 'y', 'z', api='gl')
def glScaled(x, y, z):
	pass


@params('program', 'programInterface', 'index', 'bufSize', 'length', 'name', api='gl')
def glGetProgramResourceName(program, programInterface, index, bufSize, length, name):
	pass


@params('first', 'count', 'v', api='gl')
def glDepthRangeArrayv(first, count, v):
	pass


@params('program', 'bufferIndex', 'pname', 'params', api='gl')
def glGetActiveAtomicCounterBufferiv(program, bufferIndex, pname, params):
	pass


@params('face', 'sfail', 'dpfail', 'dppass', api='gl')
def glStencilOpSeparate(face, sfail, dpfail, dppass):
	pass


@params('vaobj', 'attribindex', 'bindingindex', api='gl')
def glVertexArrayAttribBinding(vaobj, attribindex, bindingindex):
	pass


@params('s', 't', 'r', api='gl')
def glTexCoord3f(s, t, r):
	pass


@params('index', 'x', api='gl')
def glVertexAttribI1i(index, x):
	pass


@params('target', 'pname', 'params', api='gl')
def glGetTexParameteriv(target, pname, params):
	pass


@params('index', 'pname', 'pointer', api='gl')
def glGetVertexAttribPointerv(index, pname, pointer):
	pass


@params('target', 'lod', 'bufSize', 'pixels', api='gl')
def glGetnCompressedTexImage(target, lod, bufSize, pixels):
	pass


@params('v', api='gl')
def glWindowPos2dv(v):
	pass


@params('cap', api='gl')
def glDisable(cap):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform4uiv(program, location, count, value):
	pass


@params('texture', 'level', 'xoffset', 'yoffset', 'x', 'y', 'width', 'height', api='gl')
def glCopyTextureSubImage2D(texture, level, xoffset, yoffset, x, y, width, height):
	pass


@params('index', 'v', api='gl')
def glVertexAttribI2uiv(index, v):
	pass


@params('light', 'pname', 'params', api='gl')
def glGetLightfv(light, pname, params):
	pass


@params('target', 's', 't', 'r', api='gl')
def glMultiTexCoord3s(target, s, t, r):
	pass


@params('target', 's', 't', 'r', api='gl')
def glMultiTexCoord3i(target, s, t, r):
	pass


@params('target', 's', 't', 'r', api='gl')
def glMultiTexCoord3f(target, s, t, r):
	pass


@params('target', 's', 't', 'r', api='gl')
def glMultiTexCoord3d(target, s, t, r):
	pass


@params('coord', api='gl')
def glFogCoorddv(coord):
	pass


@params('location', 'count', 'value', api='gl')
def glUniform3uiv(location, count, value):
	pass


@params('buffer', 'internalformat', 'format', 'type', 'data', api='gl')
def glClearNamedBufferData(buffer, internalformat, format, type, data):
	pass


@params('buffer', 'offset', 'length', api='gl')
def glFlushMappedNamedBufferRange(buffer, offset, length):
	pass


@params('name', api='gl')
def glPushName(name):
	pass


@params('plane', 'equation', api='gl')
def glGetClipPlane(plane, equation):
	pass


@params('x', 'y', 'z', 'w', api='gl')
def glRasterPos4i(x, y, z, w):
	pass


@params('red', 'green', 'blue', 'alpha', api='gl')
def glBlendColor(red, green, blue, alpha):
	pass


@params('sampler', 'pname', 'param', api='gl')
def glSamplerParameterIuiv(sampler, pname, param):
	pass


@params('c', api='gl')
def glIndexubv(c):
	pass


@params('framebuffer', 'target', api='gl')
def glCheckNamedFramebufferStatus(framebuffer, target):
	pass


@params('x', 'y', 'z', 'w', api='gl')
def glRasterPos4d(x, y, z, w):
	pass


@params('x', 'y', 'z', 'w', api='gl')
def glRasterPos4f(x, y, z, w):
	pass


@params('index', 'x', 'y', 'z', api='gl')
def glVertexAttrib3s(index, x, y, z):
	pass


@params('x', 'y', 'z', 'w', api='gl')
def glRasterPos4s(x, y, z, w):
	pass


@params('program', 'shadertype', 'pname', 'values', api='gl')
def glGetProgramStageiv(program, shadertype, pname, values):
	pass


@params(api = 'gl')
def glPopMatrix():
	pass


@params('x', 'y', 'z', 'w', api='gl')
def glVertex4s(x, y, z, w):
	pass


@params('location', 'v0', 'v1', 'v2', 'v3', api='gl')
def glUniform4i(location, v0, v1, v2, v3):
	pass


@params('texture', api='gl')
def glActiveTexture(texture):
	pass


@params('index', api='gl')
def glEnableVertexAttribArray(index):
	pass


@params('location', 'x', 'y', 'z', 'w', api='gl')
def glUniform4d(location, x, y, z, w):
	pass


@params('location', 'v0', 'v1', 'v2', 'v3', api='gl')
def glUniform4f(location, v0, v1, v2, v3):
	pass


@params('target', 'samples', 'internalformat', 'width', 'height', api='gl')
def glRenderbufferStorageMultisample(target, samples, internalformat, width, height):
	pass


@params('n', 'pipelines', api='gl')
def glCreateProgramPipelines(n, pipelines):
	pass


@params('index', 'size', 'type', 'stride', 'pointer', api='gl')
def glVertexAttribLPointer(index, size, type, stride, pointer):
	pass


@params('target', 'v', api='gl')
def glMultiTexCoord3sv(target, v):
	pass


@params('mode', 'count', 'type', 'indices', 'instancecount', 'basevertex', api='gl')
def glDrawElementsInstancedBaseVertex(mode, count, type, indices, instancecount, basevertex):
	pass


@params('program', 'shadertype', 'index', 'bufsize', 'length', 'name', api='gl')
def glGetActiveSubroutineName(program, shadertype, index, bufsize, length, name):
	pass


@params('target', 'v', api='gl')
def glMultiTexCoord4iv(target, v):
	pass


@params('target', 'pname', 'params', api='gl')
def glTexEnvfv(target, pname, params):
	pass


@params(api = 'gl')
def glPopDebugGroup():
	pass


@params('program', 'uniformBlockIndex', 'uniformBlockBinding', api='gl')
def glUniformBlockBinding(program, uniformBlockIndex, uniformBlockBinding):
	pass


@params('target', 'offset', 'size', 'data', api='gl')
def glBufferSubData(target, offset, size, data):
	pass


@params('size', 'type', 'stride', 'pointer', api='gl')
def glTexCoordPointer(size, type, stride, pointer):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix3x2fv(program, location, count, transpose, value):
	pass


@params('target', 'index', 'pname', 'params', api='gl')
def glGetQueryIndexediv(target, index, pname, params):
	pass


@params('target', 'pname', 'params', api='gl')
def glTexEnviv(target, pname, params):
	pass


@params('sfactor', 'dfactor', api='gl')
def glBlendFunc(sfactor, dfactor):
	pass


@params(api = 'gl')
def glCreateProgram():
	pass


@params('index', api='gl')
def glPrimitiveRestartIndex(index):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix2fv(program, location, count, transpose, value):
	pass


@params('first', 'count', 'textures', api='gl')
def glBindImageTextures(first, count, textures):
	pass


@params(api = 'gl')
def glEnd():
	pass


@params('sampler', 'pname', 'param', api='gl')
def glSamplerParameteriv(sampler, pname, param):
	pass


@params('v', api='gl')
def glSecondaryColor3iv(v):
	pass


@params('m', api='gl')
def glMultTransposeMatrixd(m):
	pass


@params('red', 'green', 'blue', 'alpha', api='gl')
def glClearColor(red, green, blue, alpha):
	pass


@params('mask', api='gl')
def glPushClientAttrib(mask):
	pass


@params('program', 'location', 'bufSize', 'params', api='gl')
def glGetnUniformiv(program, location, bufSize, params):
	pass


@params('mask', api='gl')
def glStencilMask(mask):
	pass


@params('red', 'green', 'blue', api='gl')
def glSecondaryColor3us(red, green, blue):
	pass


@params('index', 'v', api='gl')
def glVertexAttribI4uiv(index, v):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib4bv(index, v):
	pass


@params('program', 'programInterface', 'name', api='gl')
def glGetProgramResourceIndex(program, programInterface, name):
	pass


@params('red', 'green', 'blue', api='gl')
def glSecondaryColor3ub(red, green, blue):
	pass


@params('red', 'green', 'blue', api='gl')
def glSecondaryColor3ui(red, green, blue):
	pass


@params('buffer', 'pname', 'params', api='gl')
def glGetNamedBufferPointerv(buffer, pname, params):
	pass


@params('id', 'buffer', 'pname', 'offset', api='gl')
def glGetQueryBufferObjectui64v(id, buffer, pname, offset):
	pass


@params('nx', 'ny', 'nz', api='gl')
def glNormal3f(nx, ny, nz):
	pass


@params('location', 'count', 'transpose', 'value', api='gl')
def glUniformMatrix2x3fv(location, count, transpose, value):
	pass


@params('n', 'ids', api='gl')
def glGenTransformFeedbacks(n, ids):
	pass


@params('index', 'pname', 'params', api='gl')
def glGetVertexAttribIuiv(index, pname, params):
	pass


@params('target', 'level', 'xoffset', 'yoffset', 'width', 'height', 'format', 'imageSize', 'data', api='gl')
def glCompressedTexSubImage2D(target, level, xoffset, yoffset, width, height, format, imageSize, data):
	pass


@params('program', 'binaryFormat', 'binary', 'length', api='gl')
def glProgramBinary(program, binaryFormat, binary, length):
	pass


@params('index', 'v', api='gl')
def glVertexAttribI4bv(index, v):
	pass


@params('target', 'pname', 'params', api='gl')
def glGetTexParameterfv(target, pname, params):
	pass


@params('vaobj', 'index', 'pname', 'param', api='gl')
def glGetVertexArrayIndexed64iv(vaobj, index, pname, param):
	pass


@params('target', 'pname', 'params', api='gl')
def glTexParameterIiv(target, pname, params):
	pass


@params('vaobj', 'attribindex', 'size', 'type', 'normalized', 'relativeoffset', api='gl')
def glVertexArrayAttribFormat(vaobj, attribindex, size, type, normalized, relativeoffset):
	pass


@params(api = 'gl')
def glEndTransformFeedback():
	pass


@params('target', 'samples', 'internalformat', 'width', 'height', 'fixedsamplelocations', api='gl')
def glTexImage2DMultisample(target, samples, internalformat, width, height, fixedsamplelocations):
	pass


@params('index', 'v', api='gl')
def glVertexAttribI1iv(index, v):
	pass


@params('index', 'divisor', api='gl')
def glVertexAttribDivisor(index, divisor):
	pass


@params('texture', 'level', 'bufSize', 'pixels', api='gl')
def glGetCompressedTextureImage(texture, level, bufSize, pixels):
	pass


@params('range', api='gl')
def glGenLists(range):
	pass


@params('target', 'offset', 'length', 'access', api='gl')
def glMapBufferRange(target, offset, length, access):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix4x2fv(program, location, count, transpose, value):
	pass


@params(api = 'gl')
def glEndList():
	pass


@params('location', 'count', 'transpose', 'value', api='gl')
def glUniformMatrix3x2dv(location, count, transpose, value):
	pass


@params('shadertype', 'precisiontype', 'range', 'precision', api='gl')
def glGetShaderPrecisionFormat(shadertype, precisiontype, range, precision):
	pass


@params('mask', api='gl')
def glIndexMask(mask):
	pass


@params('shader', 'count', 'conststring', 'length', api='gl')
def glShaderSource(shader, count, conststring, length):
	pass


@params('n', 'renderbuffers', api='gl')
def glDeleteRenderbuffers(n, renderbuffers):
	pass


@params('type', 'coords', api='gl')
def glTexCoordP2uiv(type, coords):
	pass


@params('un', 'u1', 'u2', 'vn', 'v1', 'v2', api='gl')
def glMapGrid2d(un, u1, u2, vn, v1, v2):
	pass


@params('buffer', 'pname', 'params', api='gl')
def glGetNamedBufferParameteri64v(buffer, pname, params):
	pass


@params('x', 'y', 'z', 'w', api='gl')
def glVertex4d(x, y, z, w):
	pass


@params('target', 'size', 'data', 'usage', api='gl')
def glBufferData(target, size, data, usage):
	pass


@params('x', 'y', 'z', 'w', api='gl')
def glVertex4f(x, y, z, w):
	pass


@params('type', 'coords', api='gl')
def glTexCoordP1ui(type, coords):
	pass


@params('texture', 'level', 'xoffset', 'yoffset', 'zoffset', 'x', 'y', 'width', 'height', api='gl')
def glCopyTextureSubImage3D(texture, level, xoffset, yoffset, zoffset, x, y, width, height):
	pass


@params('target', 'v', api='gl')
def glMultiTexCoord2fv(target, v):
	pass


@params('type', 'coords', api='gl')
def glNormalP3ui(type, coords):
	pass


@params('size', 'type', 'stride', 'pointer', api='gl')
def glColorPointer(size, type, stride, pointer):
	pass


@params('target', 'attachment', 'textarget', 'texture', 'level', api='gl')
def glFramebufferTexture2D(target, attachment, textarget, texture, level):
	pass


@params('target', 'pname', 'params', api='gl')
def glGetBufferPointerv(target, pname, params):
	pass


@params('target', 'attachment', 'textarget', 'texture', 'level', 'zoffset', api='gl')
def glFramebufferTexture3D(target, attachment, textarget, texture, level, zoffset):
	pass


@params('v', api='gl')
def glWindowPos3dv(v):
	pass


@params('sampler', 'pname', 'param', api='gl')
def glSamplerParameterfv(sampler, pname, param):
	pass


@params('v', api='gl')
def glNormal3bv(v):
	pass


@params('face', 'pname', 'params', api='gl')
def glGetMaterialiv(face, pname, params):
	pass


@params('location', 'count', 'value', api='gl')
def glUniform1fv(location, count, value):
	pass


@params('index', 'v', api='gl')
def glScissorIndexedv(index, v):
	pass


@params('nx', 'ny', 'nz', api='gl')
def glNormal3s(nx, ny, nz):
	pass


@params('map', 'bufSize', 'values', api='gl')
def glGetnPixelMapuiv(map, bufSize, values):
	pass


@params('nx', 'ny', 'nz', api='gl')
def glNormal3i(nx, ny, nz):
	pass


@params('nx', 'ny', 'nz', api='gl')
def glNormal3d(nx, ny, nz):
	pass


@params('nx', 'ny', 'nz', api='gl')
def glNormal3b(nx, ny, nz):
	pass


@params('target', 'v', api='gl')
def glMultiTexCoord4dv(target, v):
	pass


@params('index', 'x', 'y', api='gl')
def glVertexAttrib2d(index, x, y):
	pass


@params('index', 'x', 'y', api='gl')
def glVertexAttrib2f(index, x, y):
	pass


@params('index', 'x', 'y', api='gl')
def glVertexAttrib2s(index, x, y):
	pass


@params('target', 'samples', 'internalformat', 'width', 'height', 'depth', 'fixedsamplelocations', api='gl')
def glTexImage3DMultisample(target, samples, internalformat, width, height, depth, fixedsamplelocations):
	pass


@params('program', 'uniformBlockName', api='gl')
def glGetUniformBlockIndex(program, uniformBlockName):
	pass


@params('mode', api='gl')
def glFrontFace(mode):
	pass


@params('mode', 'first', 'count', 'instancecount', 'baseinstance', api='gl')
def glDrawArraysInstancedBaseInstance(mode, first, count, instancecount, baseinstance):
	pass


