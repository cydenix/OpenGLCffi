def glCopyTexImage1D(target, level, internalformat, x, y, width, border):
	return lib.glCopyTexImage1D(target, level, internalformat, x, y, width, border)

def glVertexArrayElementBuffer(vaobj, buffer):
	return lib.glVertexArrayElementBuffer(vaobj, buffer)

def glStencilMaskSeparate(face, mask):
	return lib.glStencilMaskSeparate(face, mask)

def glTextureStorage3DMultisample(texture, samples, internalformat, width, height, depth, fixedsamplelocations):
	return lib.glTextureStorage3DMultisample(texture, samples, internalformat, width, height, depth, fixedsamplelocations)

def glTextureParameterfv(texture, pname, param):
	return lib.glTextureParameterfv(texture, pname, param)

def glVertexAttrib4usv(index, v):
	return lib.glVertexAttrib4usv(index, v)

def glIndexi(c):
	return lib.glIndexi(c)

def glCompressedTexSubImage3D(target, level, xoffset, yoffset, zoffset, width, height, depth, format, imageSize, data):
	return lib.glCompressedTexSubImage3D(target, level, xoffset, yoffset, zoffset, width, height, depth, format, imageSize, data)

def glEvalCoord2d(u, v):
	return lib.glEvalCoord2d(u, v)

def glEvalCoord2f(u, v):
	return lib.glEvalCoord2f(u, v)

def glIndexd(c):
	return lib.glIndexd(c)

def glIndexf(c):
	return lib.glIndexf(c)

def glIndexs(c):
	return lib.glIndexs(c)

def glVertex3sv(v):
	return lib.glVertex3sv(v)

def glGetnMapfv(target, query, bufSize, v):
	return lib.glGetnMapfv(target, query, bufSize, v)

def glSecondaryColor3fv(v):
	return lib.glSecondaryColor3fv(v)

def glFogfv(pname):
	params = ffi.new('const GLfloat *')
	return lib.glFogfv(pname, params)

def glDrawElementsInstancedBaseInstance(mode, count, type, indices, instancecount, baseinstance):
	return lib.glDrawElementsInstancedBaseInstance(mode, count, type, indices, instancecount, baseinstance)

def glIsBuffer(buffer):
	return lib.glIsBuffer(buffer)

def glGetMultisamplefv(pname, index, val):
	return lib.glGetMultisamplefv(pname, index, val)

def glProgramUniformMatrix4fv(program, location, count, transpose, value):
	return lib.glProgramUniformMatrix4fv(program, location, count, transpose, value)

def glDebugMessageControl(source, type, severity, count, ids, enabled):
	return lib.glDebugMessageControl(source, type, severity, count, ids, enabled)

def glPopAttrib():
	return lib.glPopAttrib()

def glColorMaterial(face, mode):
	return lib.glColorMaterial(face, mode)

def glRenderbufferStorage(target, internalformat, width, height):
	return lib.glRenderbufferStorage(target, internalformat, width, height)

def glColor3b(red, green, blue):
	return lib.glColor3b(red, green, blue)

def glColor3f(red, green, blue):
	return lib.glColor3f(red, green, blue)

def glColor3d(red, green, blue):
	return lib.glColor3d(red, green, blue)

def glGetnMapiv(target, query, bufSize, v):
	return lib.glGetnMapiv(target, query, bufSize, v)

def glColor3i(red, green, blue):
	return lib.glColor3i(red, green, blue)

def glVertexAttrib4ubv(index, v):
	return lib.glVertexAttrib4ubv(index, v)

def glColor3s(red, green, blue):
	return lib.glColor3s(red, green, blue)

def glGetVertexArrayIndexediv(vaobj, index, pname, param):
	return lib.glGetVertexArrayIndexediv(vaobj, index, pname, param)

def glMultiTexCoord1iv(target, v):
	return lib.glMultiTexCoord1iv(target, v)

def glMultiTexCoordP2ui(texture, type, coords):
	return lib.glMultiTexCoordP2ui(texture, type, coords)

def glProgramUniform3f(program, location, v0, v1, v2):
	return lib.glProgramUniform3f(program, location, v0, v1, v2)

def glVertexAttribL4d(index, x, y, z, w):
	return lib.glVertexAttribL4d(index, x, y, z, w)

def glVertex2iv(v):
	return lib.glVertex2iv(v)

def glVertexArrayAttribLFormat(vaobj, attribindex, size, type, relativeoffset):
	return lib.glVertexArrayAttribLFormat(vaobj, attribindex, size, type, relativeoffset)

def glInvalidateBufferSubData(buffer, offset, length):
	return lib.glInvalidateBufferSubData(buffer, offset, length)

def glResumeTransformFeedback():
	return lib.glResumeTransformFeedback()

def glFogi(pname, param):
	return lib.glFogi(pname, param)

def glVertexPointer(size, type, stride, pointer):
	return lib.glVertexPointer(size, type, stride, pointer)

def glFogf(pname, param):
	return lib.glFogf(pname, param)

def glMultiTexCoord1d(target, s):
	return lib.glMultiTexCoord1d(target, s)

def glMultiTexCoord1f(target, s):
	return lib.glMultiTexCoord1f(target, s)

def glVertexAttribI2i(index, x, y):
	return lib.glVertexAttribI2i(index, x, y)

def glMultiTexCoord1i(target, s):
	return lib.glMultiTexCoord1i(target, s)

def glGetGraphicsResetStatus():
	return lib.glGetGraphicsResetStatus()

def glVertexAttrib1fv(index, v):
	return lib.glVertexAttrib1fv(index, v)

def glIsEnabled(cap):
	return lib.glIsEnabled(cap)

def glStencilOp(fail, zfail, zpass):
	return lib.glStencilOp(fail, zfail, zpass)

def glMapNamedBufferRange(buffer, offset, length, access):
	return lib.glMapNamedBufferRange(buffer, offset, length, access)

def glVertexArrayAttribIFormat(vaobj, attribindex, size, type, relativeoffset):
	return lib.glVertexArrayAttribIFormat(vaobj, attribindex, size, type, relativeoffset)

def glGenFramebuffers(n, framebuffers):
	return lib.glGenFramebuffers(n, framebuffers)

def glGetAttachedShaders(program, maxCount, count, shaders):
	return lib.glGetAttachedShaders(program, maxCount, count, shaders)

def glDeleteVertexArrays(n, arrays):
	return lib.glDeleteVertexArrays(n, arrays)

def glViewportArrayv(first, count, v):
	return lib.glViewportArrayv(first, count, v)

def glMultiTexCoord2s(target, s, t):
	return lib.glMultiTexCoord2s(target, s, t)

def glVertex3dv(v):
	return lib.glVertex3dv(v)

def glColor4fv(v):
	return lib.glColor4fv(v)

def glVertexArrayBindingDivisor(vaobj, bindingindex, divisor):
	return lib.glVertexArrayBindingDivisor(vaobj, bindingindex, divisor)

def glTexCoord2sv(v):
	return lib.glTexCoord2sv(v)

def glUniform2dv(location, count, value):
	return lib.glUniform2dv(location, count, value)

def glGetPixelMapuiv(map):
	values = ffi.new('GLuint *')
	return lib.glGetPixelMapuiv(map, values)

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

def glVertexAttrib4d(index, x, y, z, w):
	return lib.glVertexAttrib4d(index, x, y, z, w)

def glGetRenderbufferParameteriv(target, pname):
	params = ffi.new('GLint *')
	return lib.glGetRenderbufferParameteriv(target, pname, params)

def glNamedRenderbufferStorage(renderbuffer, internalformat, width, height):
	return lib.glNamedRenderbufferStorage(renderbuffer, internalformat, width, height)

def glFenceSync(condition, flags):
	return lib.glFenceSync(condition, flags)

def glValidateProgramPipeline(pipeline):
	return lib.glValidateProgramPipeline(pipeline)

def glVertexP4ui(type, value):
	return lib.glVertexP4ui(type, value)

def glGenSamplers(count, samplers):
	return lib.glGenSamplers(count, samplers)

def glVertexAttrib2sv(index, v):
	return lib.glVertexAttrib2sv(index, v)

def glDrawTransformFeedbackInstanced(mode, id, instancecount):
	return lib.glDrawTransformFeedbackInstanced(mode, id, instancecount)

def glTexCoord4iv(v):
	return lib.glTexCoord4iv(v)

def glDrawTransformFeedback(mode, id):
	return lib.glDrawTransformFeedback(mode, id)

def glGetTexParameterIuiv(target, pname):
	params = ffi.new('GLuint *')
	return lib.glGetTexParameterIuiv(target, pname, params)

def glIndexPointer(type, stride, pointer):
	return lib.glIndexPointer(type, stride, pointer)

def glIsSync(sync):
	return lib.glIsSync(sync)

def glVertex4iv(v):
	return lib.glVertex4iv(v)

def glMultiTexCoord3iv(target, v):
	return lib.glMultiTexCoord3iv(target, v)

def glGetObjectPtrLabel(ptr, bufSize, length, label):
	return lib.glGetObjectPtrLabel(ptr, bufSize, length, label)

def glTextureParameteri(texture, pname, param):
	return lib.glTextureParameteri(texture, pname, param)

def glUniformMatrix2x3dv(location, count, transpose, value):
	return lib.glUniformMatrix2x3dv(location, count, transpose, value)

def glSecondaryColor3sv(v):
	return lib.glSecondaryColor3sv(v)

def glOrtho(left, right, bottom, top, zNear, zFar):
	return lib.glOrtho(left, right, bottom, top, zNear, zFar)

def glFogCoordd(coord):
	return lib.glFogCoordd(coord)

def glFogCoordf(coord):
	return lib.glFogCoordf(coord)

def glCopyTexImage2D(target, level, internalformat, x, y, width, height, border):
	return lib.glCopyTexImage2D(target, level, internalformat, x, y, width, height, border)

def glVertexAttribP4ui(index, type, normalized, value):
	return lib.glVertexAttribP4ui(index, type, normalized, value)

def glUniform4uiv(location, count, value):
	return lib.glUniform4uiv(location, count, value)

def glVertexAttribL1dv(index, v):
	return lib.glVertexAttribL1dv(index, v)

def glProgramUniformMatrix2dv(program, location, count, transpose, value):
	return lib.glProgramUniformMatrix2dv(program, location, count, transpose, value)

def glScissorArrayv(first, count, v):
	return lib.glScissorArrayv(first, count, v)

def glCallList(list):
	return lib.glCallList(list)

def glLightModeli(pname, param):
	return lib.glLightModeli(pname, param)

def glGetnColorTable(target, format, type, bufSize, table):
	return lib.glGetnColorTable(target, format, type, bufSize, table)

def glWindowPos3iv(v):
	return lib.glWindowPos3iv(v)

def glInvalidateSubFramebuffer(target, numAttachments, attachments, x, y, width, height):
	return lib.glInvalidateSubFramebuffer(target, numAttachments, attachments, x, y, width, height)

def glMapBuffer(target, access):
	return lib.glMapBuffer(target, access)

def glSecondaryColor3d(red, green, blue):
	return lib.glSecondaryColor3d(red, green, blue)

def glVertexAttribLFormat(attribindex, size, type, relativeoffset):
	return lib.glVertexAttribLFormat(attribindex, size, type, relativeoffset)

def glSecondaryColor3i(red, green, blue):
	return lib.glSecondaryColor3i(red, green, blue)

def glDeleteSync(sync):
	return lib.glDeleteSync(sync)

def glUniformMatrix4x2dv(location, count, transpose, value):
	return lib.glUniformMatrix4x2dv(location, count, transpose, value)

def glSecondaryColor3s(red, green, blue):
	return lib.glSecondaryColor3s(red, green, blue)

def glUniform3iv(location, count, value):
	return lib.glUniform3iv(location, count, value)

def glTexCoord1s(s):
	return lib.glTexCoord1s(s)

def glPolygonMode(face, mode):
	return lib.glPolygonMode(face, mode)

def glUseProgram(program):
	return lib.glUseProgram(program)

def glLineStipple(factor, pattern):
	return lib.glLineStipple(factor, pattern)

def glGetProgramInfoLog(program, bufSize, length, infoLog):
	return lib.glGetProgramInfoLog(program, bufSize, length, infoLog)

def glPixelStoref(pname, param):
	return lib.glPixelStoref(pname, param)

def glGetBooleanv(pname):
	data = ffi.new('GLboolean *')
	return lib.glGetBooleanv(pname, data)

def glDeleteShader(shader):
	return lib.glDeleteShader(shader)

def glCopyTextureSubImage1D(texture, level, xoffset, x, y, width):
	return lib.glCopyTextureSubImage1D(texture, level, xoffset, x, y, width)

def glGetMapdv(target, query, v):
	return lib.glGetMapdv(target, query, v)

def glTextureParameterIuiv(texture, pname):
	params = ffi.new('const GLuint *')
	return lib.glTextureParameterIuiv(texture, pname, params)

def glTexCoord3d(s, t, r):
	return lib.glTexCoord3d(s, t, r)

def glVertexAttribI3i(index, x, y, z):
	return lib.glVertexAttribI3i(index, x, y, z)

def glVertexAttribFormat(attribindex, size, type, normalized, relativeoffset):
	return lib.glVertexAttribFormat(attribindex, size, type, normalized, relativeoffset)

def glVertexAttribI4usv(index, v):
	return lib.glVertexAttribI4usv(index, v)

def glTexParameterf(target, pname, param):
	return lib.glTexParameterf(target, pname, param)

def glVertexAttribBinding(attribindex, bindingindex):
	return lib.glVertexAttribBinding(attribindex, bindingindex)

def glTexParameteri(target, pname, param):
	return lib.glTexParameteri(target, pname, param)

def glGetShaderSource(shader, bufSize, length, source):
	return lib.glGetShaderSource(shader, bufSize, length, source)

def glVertexAttrib4s(index, x, y, z, w):
	return lib.glVertexAttrib4s(index, x, y, z, w)

def glPopName():
	return lib.glPopName()

def glGenProgramPipelines(n, pipelines):
	return lib.glGenProgramPipelines(n, pipelines)

def glColor4ub(red, green, blue, alpha):
	return lib.glColor4ub(red, green, blue, alpha)

def glVertexAttrib3fv(index, v):
	return lib.glVertexAttrib3fv(index, v)

def glColor4ui(red, green, blue, alpha):
	return lib.glColor4ui(red, green, blue, alpha)

def glGetNamedBufferParameteriv(buffer, pname):
	params = ffi.new('GLint *')
	return lib.glGetNamedBufferParameteriv(buffer, pname, params)

def glColor4us(red, green, blue, alpha):
	return lib.glColor4us(red, green, blue, alpha)

def glVertexAttribP1uiv(index, type, normalized, value):
	return lib.glVertexAttribP1uiv(index, type, normalized, value)

def glLinkProgram(program):
	return lib.glLinkProgram(program)

def glTexCoord2dv(v):
	return lib.glTexCoord2dv(v)

def glGetObjectLabel(identifier, bufSize, length, label):
	name = ffi.new('GLuint *')
	return lib.glGetObjectLabel(identifier, name, bufSize, length, label)

def glGetString():
	name = ffi.new('GLenum *')
	return lib.glGetString(name)

def glEndQuery(target):
	return lib.glEndQuery(target)

def glEdgeFlagPointer(stride, pointer):
	return lib.glEdgeFlagPointer(stride, pointer)

def glFramebufferParameteri(target, pname, param):
	return lib.glFramebufferParameteri(target, pname, param)

def glCopyPixels(x, y, width, height, type):
	return lib.glCopyPixels(x, y, width, height, type)

def glVertexAttribI2ui(index, x, y):
	return lib.glVertexAttribI2ui(index, x, y)

def glRasterPos3s(x, y, z):
	return lib.glRasterPos3s(x, y, z)

def glDeleteTextures(n, textures):
	return lib.glDeleteTextures(n, textures)

def glClipControl(origin, depth):
	return lib.glClipControl(origin, depth)

def glVertexAttrib4f(index, x, y, z, w):
	return lib.glVertexAttrib4f(index, x, y, z, w)

def glNamedFramebufferParameteri(framebuffer, pname, param):
	return lib.glNamedFramebufferParameteri(framebuffer, pname, param)

def glGetNamedFramebufferParameteriv(framebuffer, pname, param):
	return lib.glGetNamedFramebufferParameteriv(framebuffer, pname, param)

def glCreateVertexArrays(n, arrays):
	return lib.glCreateVertexArrays(n, arrays)

def glBeginConditionalRender(id, mode):
	return lib.glBeginConditionalRender(id, mode)

def glSamplerParameteri(sampler, pname, param):
	return lib.glSamplerParameteri(sampler, pname, param)

def glUniform1d(location, x):
	return lib.glUniform1d(location, x)

def glRenderMode(mode):
	return lib.glRenderMode(mode)

def glGetCompressedTexImage(target, level, img):
	return lib.glGetCompressedTexImage(target, level, img)

def glGetActiveUniformBlockiv(program, uniformBlockIndex, pname):
	params = ffi.new('GLint *')
	return lib.glGetActiveUniformBlockiv(program, uniformBlockIndex, pname, params)

def glUniform1i(location, v0):
	return lib.glUniform1i(location, v0)

def glGetTexEnvfv(target, pname):
	params = ffi.new('GLfloat *')
	return lib.glGetTexEnvfv(target, pname, params)

def glCullFace(mode):
	return lib.glCullFace(mode)

def glProgramUniform4i(program, location, v0, v1, v2, v3):
	return lib.glProgramUniform4i(program, location, v0, v1, v2, v3)

def glProgramUniform4f(program, location, v0, v1, v2, v3):
	return lib.glProgramUniform4f(program, location, v0, v1, v2, v3)

def glViewportIndexedf(index, x, y, w, h):
	return lib.glViewportIndexedf(index, x, y, w, h)

def glProgramUniform4d(program, location, v0, v1, v2, v3):
	return lib.glProgramUniform4d(program, location, v0, v1, v2, v3)

def glVertex3i(x, y, z):
	return lib.glVertex3i(x, y, z)

def glAttachShader(program, shader):
	return lib.glAttachShader(program, shader)

def glIsList(list):
	return lib.glIsList(list)

def glFogCoordPointer(type, stride, pointer):
	return lib.glFogCoordPointer(type, stride, pointer)

def glUnmapNamedBuffer(buffer):
	return lib.glUnmapNamedBuffer(buffer)

def glSecondaryColor3dv(v):
	return lib.glSecondaryColor3dv(v)

def glVertexAttribI4sv(index, v):
	return lib.glVertexAttribI4sv(index, v)

def glDrawTransformFeedbackStreamInstanced(mode, id, stream, instancecount):
	return lib.glDrawTransformFeedbackStreamInstanced(mode, id, stream, instancecount)

def glGetBufferParameteriv(target, pname):
	params = ffi.new('GLint *')
	return lib.glGetBufferParameteriv(target, pname, params)

def glTexParameterIuiv(target, pname):
	params = ffi.new('const GLuint *')
	return lib.glTexParameterIuiv(target, pname, params)

def glWindowPos3fv(v):
	return lib.glWindowPos3fv(v)

def glLightModelfv(pname):
	params = ffi.new('const GLfloat *')
	return lib.glLightModelfv(pname, params)

def glTextureStorage3D(texture, levels, internalformat, width, height, depth):
	return lib.glTextureStorage3D(texture, levels, internalformat, width, height, depth)

def glIsTransformFeedback(id):
	return lib.glIsTransformFeedback(id)

def glRotated(angle, x, y, z):
	return lib.glRotated(angle, x, y, z)

def glIsProgramPipeline(pipeline):
	return lib.glIsProgramPipeline(pipeline)

def glRotatef(angle, x, y, z):
	return lib.glRotatef(angle, x, y, z)

def glVertex4i(x, y, z, w):
	return lib.glVertex4i(x, y, z, w)

def glGetActiveSubroutineUniformName(program, shadertype, index, bufsize, length):
	name = ffi.new('GLchar *')
	return lib.glGetActiveSubroutineUniformName(program, shadertype, index, bufsize, length, name)

def glUniformMatrix3fv(location, count, transpose, value):
	return lib.glUniformMatrix3fv(location, count, transpose, value)

def glGetnUniformfv(program, location, bufSize):
	params = ffi.new('GLfloat *')
	return lib.glGetnUniformfv(program, location, bufSize, params)

def glVertexAttribL2dv(index, v):
	return lib.glVertexAttribL2dv(index, v)

def glSecondaryColorPointer(size, type, stride, pointer):
	return lib.glSecondaryColorPointer(size, type, stride, pointer)

def glAlphaFunc(func, ref):
	return lib.glAlphaFunc(func, ref)

def glTexCoord4d(s, t, r, q):
	return lib.glTexCoord4d(s, t, r, q)

def glVertexAttribL2d(index, x, y):
	return lib.glVertexAttribL2d(index, x, y)

def glStencilFunc(func, ref, mask):
	return lib.glStencilFunc(func, ref, mask)

def glTexCoord3dv(v):
	return lib.glTexCoord3dv(v)

def glGetQueryBufferObjectiv(id, buffer, pname, offset):
	return lib.glGetQueryBufferObjectiv(id, buffer, pname, offset)

def glGetProgramPipelineiv(pipeline, pname):
	params = ffi.new('GLint *')
	return lib.glGetProgramPipelineiv(pipeline, pname, params)

def glDispatchComputeIndirect(indirect):
	return lib.glDispatchComputeIndirect(indirect)

def glGetShaderInfoLog(shader, bufSize, length, infoLog):
	return lib.glGetShaderInfoLog(shader, bufSize, length, infoLog)

def glVertexAttribI4i(index, x, y, z, w):
	return lib.glVertexAttribI4i(index, x, y, z, w)

def glRasterPos2iv(v):
	return lib.glRasterPos2iv(v)

def glSecondaryColor3uiv(v):
	return lib.glSecondaryColor3uiv(v)

def glRasterPos2i(x, y):
	return lib.glRasterPos2i(x, y)

def glBlendEquationSeparate(modeRGB, modeAlpha):
	return lib.glBlendEquationSeparate(modeRGB, modeAlpha)

def glGetSubroutineIndex(program, shadertype):
	name = ffi.new('const GLchar *')
	return lib.glGetSubroutineIndex(program, shadertype, name)

def glPushAttrib(mask):
	return lib.glPushAttrib(mask)

def glVertexAttribL3dv(index, v):
	return lib.glVertexAttribL3dv(index, v)

def glLightiv(light, pname):
	params = ffi.new('const GLint *')
	return lib.glLightiv(light, pname, params)

def glDeleteBuffers(n, buffers):
	return lib.glDeleteBuffers(n, buffers)

def glBindProgramPipeline(pipeline):
	return lib.glBindProgramPipeline(pipeline)

def glScissor(x, y, width, height):
	return lib.glScissor(x, y, width, height)

def glMaterialfv(face, pname):
	params = ffi.new('const GLfloat *')
	return lib.glMaterialfv(face, pname, params)

def glUniformMatrix3dv(location, count, transpose, value):
	return lib.glUniformMatrix3dv(location, count, transpose, value)

def glGetTextureLevelParameteriv(texture, level, pname):
	params = ffi.new('GLint *')
	return lib.glGetTextureLevelParameteriv(texture, level, pname, params)

def glGetStringi(index):
	name = ffi.new('GLenum *')
	return lib.glGetStringi(name, index)

def glColor4dv(v):
	return lib.glColor4dv(v)

def glPointParameterfv(pname):
	params = ffi.new('const GLfloat *')
	return lib.glPointParameterfv(pname, params)

def glUniform2fv(location, count, value):
	return lib.glUniform2fv(location, count, value)

def glInvalidateNamedFramebufferSubData(framebuffer, numAttachments, attachments, x, y, width, height):
	return lib.glInvalidateNamedFramebufferSubData(framebuffer, numAttachments, attachments, x, y, width, height)

def glBindBufferRange(target, index, buffer, offset, size):
	return lib.glBindBufferRange(target, index, buffer, offset, size)

def glNormal3iv(v):
	return lib.glNormal3iv(v)

def glGetUniformdv(program, location):
	params = ffi.new('GLdouble *')
	return lib.glGetUniformdv(program, location, params)

def glMultiTexCoord4s(target, s, t, r, q):
	return lib.glMultiTexCoord4s(target, s, t, r, q)

def glTexCoord1iv(v):
	return lib.glTexCoord1iv(v)

def glColor3uiv(v):
	return lib.glColor3uiv(v)

def glListBase(base):
	return lib.glListBase(base)

def glClientWaitSync(sync, flags, timeout):
	return lib.glClientWaitSync(sync, flags, timeout)

def glTextureBuffer(texture, internalformat, buffer):
	return lib.glTextureBuffer(texture, internalformat, buffer)

def glVertexAttrib4Nsv(index, v):
	return lib.glVertexAttrib4Nsv(index, v)

def glReadnPixels(x, y, width, height, format, type, bufSize):
	data = ffi.new('void *')
	return lib.glReadnPixels(x, y, width, height, format, type, bufSize, data)

def glCopyImageSubData(srcName, srcTarget, srcLevel, srcX, srcY, srcZ, dstName, dstTarget, dstLevel, dstX, dstY, dstZ, srcWidth, srcHeight, srcDepth):
	return lib.glCopyImageSubData(srcName, srcTarget, srcLevel, srcX, srcY, srcZ, dstName, dstTarget, dstLevel, dstX, dstY, dstZ, srcWidth, srcHeight, srcDepth)

def glGetUniformSubroutineuiv(shadertype, location):
	params = ffi.new('GLuint *')
	return lib.glGetUniformSubroutineuiv(shadertype, location, params)

def glBindVertexBuffer(bindingindex, buffer, offset, stride):
	return lib.glBindVertexBuffer(bindingindex, buffer, offset, stride)

def glDebugMessageInsert(source, type, id, severity, length, buf):
	return lib.glDebugMessageInsert(source, type, id, severity, length, buf)

def glIsSampler(sampler):
	return lib.glIsSampler(sampler)

def glCopyTexSubImage1D(target, level, xoffset, x, y, width):
	return lib.glCopyTexSubImage1D(target, level, xoffset, x, y, width)

def glTexCoord1i(s):
	return lib.glTexCoord1i(s)

def glCheckFramebufferStatus(target):
	return lib.glCheckFramebufferStatus(target)

def glTexCoord1d(s):
	return lib.glTexCoord1d(s)

def glTexCoord1f(s):
	return lib.glTexCoord1f(s)

def glBindImageTexture(unit, texture, level, layered, layer, access, format):
	return lib.glBindImageTexture(unit, texture, level, layered, layer, access, format)

def glTransformFeedbackVaryings(program, count, constvaryings, bufferMode):
	return lib.glTransformFeedbackVaryings(program, count, constvaryings, bufferMode)

def glDrawRangeElements(mode, start, end, count, type, indices):
	return lib.glDrawRangeElements(mode, start, end, count, type, indices)

def glBindBufferBase(target, index, buffer):
	return lib.glBindBufferBase(target, index, buffer)

def glColor3bv(v):
	return lib.glColor3bv(v)

def glCreateSamplers(n, samplers):
	return lib.glCreateSamplers(n, samplers)

def glMultiDrawArrays(mode, first, count, drawcount):
	return lib.glMultiDrawArrays(mode, first, count, drawcount)

def glTexCoordP4ui(type, coords):
	return lib.glTexCoordP4ui(type, coords)

def glVertexAttribI3ui(index, x, y, z):
	return lib.glVertexAttribI3ui(index, x, y, z)

def glVertexAttribIFormat(attribindex, size, type, relativeoffset):
	return lib.glVertexAttribIFormat(attribindex, size, type, relativeoffset)

def glCreateFramebuffers(n, framebuffers):
	return lib.glCreateFramebuffers(n, framebuffers)

def glClearAccum(red, green, blue, alpha):
	return lib.glClearAccum(red, green, blue, alpha)

def glBeginQuery(target, id):
	return lib.glBeginQuery(target, id)

def glMap2d(target, u1, u2, ustride, uorder, v1, v2, vstride, vorder, points):
	return lib.glMap2d(target, u1, u2, ustride, uorder, v1, v2, vstride, vorder, points)

def glMap2f(target, u1, u2, ustride, uorder, v1, v2, vstride, vorder, points):
	return lib.glMap2f(target, u1, u2, ustride, uorder, v1, v2, vstride, vorder, points)

def glUniformMatrix2x4fv(location, count, transpose, value):
	return lib.glUniformMatrix2x4fv(location, count, transpose, value)

def glDepthRangeIndexed(index, n, f):
	return lib.glDepthRangeIndexed(index, n, f)

def glGetError():
	return lib.glGetError()

def glGetTexEnviv(target, pname):
	params = ffi.new('GLint *')
	return lib.glGetTexEnviv(target, pname, params)

def glEvalCoord1d(u):
	return lib.glEvalCoord1d(u)

def glGetTexLevelParameterfv(target, level, pname):
	params = ffi.new('GLfloat *')
	return lib.glGetTexLevelParameterfv(target, level, pname, params)

def glEvalCoord1f(u):
	return lib.glEvalCoord1f(u)

def glPixelMapfv(map, mapsize):
	values = ffi.new('const GLfloat *')
	return lib.glPixelMapfv(map, mapsize, values)

def glGetPixelMapusv(map):
	values = ffi.new('GLushort *')
	return lib.glGetPixelMapusv(map, values)

def glAccum(op, value):
	return lib.glAccum(op, value)

def glRasterPos3sv(v):
	return lib.glRasterPos3sv(v)

def glProgramUniform2ui(program, location, v0, v1):
	return lib.glProgramUniform2ui(program, location, v0, v1)

def glProgramUniform4ui(program, location, v0, v1, v2, v3):
	return lib.glProgramUniform4ui(program, location, v0, v1, v2, v3)

def glNamedBufferData(buffer, size, usage):
	data = ffi.new('const void *')
	return lib.glNamedBufferData(buffer, size, data, usage)

def glClearNamedBufferSubData(buffer, internalformat, offset, size, format, type):
	data = ffi.new('const void *')
	return lib.glClearNamedBufferSubData(buffer, internalformat, offset, size, format, type, data)

def glRectsv(v1, v2):
	return lib.glRectsv(v1, v2)

def glGetTexGeniv(coord, pname):
	params = ffi.new('GLint *')
	return lib.glGetTexGeniv(coord, pname, params)

def glPixelStorei(pname, param):
	return lib.glPixelStorei(pname, param)

def glGetCompressedTextureSubImage(texture, level, xoffset, yoffset, zoffset, width, height, depth, bufSize):
	pixels = ffi.new('void *')
	return lib.glGetCompressedTextureSubImage(texture, level, xoffset, yoffset, zoffset, width, height, depth, bufSize, pixels)

def glDepthMask(flag):
	return lib.glDepthMask(flag)

def glPatchParameterfv(pname):
	values = ffi.new('const GLfloat *')
	return lib.glPatchParameterfv(pname, values)

def glTextureStorage2D(texture, levels, internalformat, width, height):
	return lib.glTextureStorage2D(texture, levels, internalformat, width, height)

def glTexBufferRange(target, internalformat, buffer, offset, size):
	return lib.glTexBufferRange(target, internalformat, buffer, offset, size)

def glRasterPos4fv(v):
	return lib.glRasterPos4fv(v)

def glEvalCoord1dv(u):
	return lib.glEvalCoord1dv(u)

def glPopClientAttrib():
	return lib.glPopClientAttrib()

def glVertexArrayVertexBuffers(vaobj, first, count, buffers, offsets, strides):
	return lib.glVertexArrayVertexBuffers(vaobj, first, count, buffers, offsets, strides)

def glProgramParameteri(program, pname, value):
	return lib.glProgramParameteri(program, pname, value)

def glGetMapfv(target, query, v):
	return lib.glGetMapfv(target, query, v)

def glRasterPos2fv(v):
	return lib.glRasterPos2fv(v)

def glMemoryBarrierByRegion(barriers):
	return lib.glMemoryBarrierByRegion(barriers)

def glVertex2sv(v):
	return lib.glVertex2sv(v)

def glWindowPos2sv(v):
	return lib.glWindowPos2sv(v)

def glCreateShader(type):
	return lib.glCreateShader(type)

def glGenRenderbuffers(n, renderbuffers):
	return lib.glGenRenderbuffers(n, renderbuffers)

def glCopyTexSubImage2D(target, level, xoffset, yoffset, x, y, width, height):
	return lib.glCopyTexSubImage2D(target, level, xoffset, yoffset, x, y, width, height)

def glBlendFuncSeparate(sfactorRGB, dfactorRGB, sfactorAlpha, dfactorAlpha):
	return lib.glBlendFuncSeparate(sfactorRGB, dfactorRGB, sfactorAlpha, dfactorAlpha)

def glTexCoord2fv(v):
	return lib.glTexCoord2fv(v)

def glTexCoord4fv(v):
	return lib.glTexCoord4fv(v)

def glPointSize(size):
	return lib.glPointSize(size)

def glBindTextureUnit(unit, texture):
	return lib.glBindTextureUnit(unit, texture)

def glGetProgramPipelineInfoLog(pipeline, bufSize, length, infoLog):
	return lib.glGetProgramPipelineInfoLog(pipeline, bufSize, length, infoLog)

def glVertexAttrib4Nuiv(index, v):
	return lib.glVertexAttrib4Nuiv(index, v)

def glWaitSync(sync, flags, timeout):
	return lib.glWaitSync(sync, flags, timeout)

def glBlendEquationSeparatei(buf, modeRGB, modeAlpha):
	return lib.glBlendEquationSeparatei(buf, modeRGB, modeAlpha)

def glUniform3d(location, x, y, z):
	return lib.glUniform3d(location, x, y, z)

def glUniform3f(location, v0, v1, v2):
	return lib.glUniform3f(location, v0, v1, v2)

def glProgramUniform3uiv(program, location, count, value):
	return lib.glProgramUniform3uiv(program, location, count, value)

def glGetFragDataIndex(program):
	name = ffi.new('const GLchar *')
	return lib.glGetFragDataIndex(program, name)

def glColor3sv(v):
	return lib.glColor3sv(v)

def glVertex4sv(v):
	return lib.glVertex4sv(v)

def glQueryCounter(id, target):
	return lib.glQueryCounter(id, target)

def glDeleteFramebuffers(n, framebuffers):
	return lib.glDeleteFramebuffers(n, framebuffers)

def glDrawArrays(mode, first, count):
	return lib.glDrawArrays(mode, first, count)

def glTexCoord4f(s, t, r, q):
	return lib.glTexCoord4f(s, t, r, q)

def glClear(mask):
	return lib.glClear(mask)

def glCreateQueries(target, n, ids):
	return lib.glCreateQueries(target, n, ids)

def glGetSamplerParameterfv(sampler, pname):
	params = ffi.new('GLfloat *')
	return lib.glGetSamplerParameterfv(sampler, pname, params)

def glTranslatef(x, y, z):
	return lib.glTranslatef(x, y, z)

def glVertexAttrib4Nub(index, x, y, z, w):
	return lib.glVertexAttrib4Nub(index, x, y, z, w)

def glTranslated(x, y, z):
	return lib.glTranslated(x, y, z)

def glSamplerParameterIiv(sampler, pname, param):
	return lib.glSamplerParameterIiv(sampler, pname, param)

def glDrawElementsIndirect(mode, type, indirect):
	return lib.glDrawElementsIndirect(mode, type, indirect)

def glSecondaryColor3bv(v):
	return lib.glSecondaryColor3bv(v)

def glTexCoord4s(s, t, r, q):
	return lib.glTexCoord4s(s, t, r, q)

def glGetQueryObjecti64v(id, pname):
	params = ffi.new('GLint64 *')
	return lib.glGetQueryObjecti64v(id, pname, params)

def glGetUniformIndices(program, uniformCount, constuniformNames, uniformIndices):
	return lib.glGetUniformIndices(program, uniformCount, constuniformNames, uniformIndices)

def glVertex3iv(v):
	return lib.glVertex3iv(v)

def glTexGenfv(coord, pname):
	params = ffi.new('const GLfloat *')
	return lib.glTexGenfv(coord, pname, params)

def glBindVertexBuffers(first, count, buffers, offsets, strides):
	return lib.glBindVertexBuffers(first, count, buffers, offsets, strides)

def glMateriali(face, pname, param):
	return lib.glMateriali(face, pname, param)

def glIsVertexArray(array):
	return lib.glIsVertexArray(array)

def glDisableVertexAttribArray(index):
	return lib.glDisableVertexAttribArray(index)

def glShaderStorageBlockBinding(program, storageBlockIndex, storageBlockBinding):
	return lib.glShaderStorageBlockBinding(program, storageBlockIndex, storageBlockBinding)

def glMaterialf(face, pname, param):
	return lib.glMaterialf(face, pname, param)

def glTextureStorage1D(texture, levels, internalformat, width):
	return lib.glTextureStorage1D(texture, levels, internalformat, width)

def glGetProgramInterfaceiv(program, programInterface, pname):
	params = ffi.new('GLint *')
	return lib.glGetProgramInterfaceiv(program, programInterface, pname, params)

def glMapNamedBuffer(buffer, access):
	return lib.glMapNamedBuffer(buffer, access)

def glGetnUniformdv(program, location, bufSize):
	params = ffi.new('GLdouble *')
	return lib.glGetnUniformdv(program, location, bufSize, params)

def glBindBuffersBase(target, first, count, buffers):
	return lib.glBindBuffersBase(target, first, count, buffers)

def glGetVertexAttribIiv(index, pname):
	params = ffi.new('GLint *')
	return lib.glGetVertexAttribIiv(index, pname, params)

def glVertexP4uiv(type, value):
	return lib.glVertexP4uiv(type, value)

def glVertexAttribL4dv(index, v):
	return lib.glVertexAttribL4dv(index, v)

def glPatchParameteri(pname, value):
	return lib.glPatchParameteri(pname, value)

def glMap1d(target, u1, u2, stride, order, points):
	return lib.glMap1d(target, u1, u2, stride, order, points)

def glMap1f(target, u1, u2, stride, order, points):
	return lib.glMap1f(target, u1, u2, stride, order, points)

def glGetNamedFramebufferAttachmentParameteriv(framebuffer, attachment, pname):
	params = ffi.new('GLint *')
	return lib.glGetNamedFramebufferAttachmentParameteriv(framebuffer, attachment, pname, params)

def glGetnSeparableFilter(target, format, type, rowBufSize, row, columnBufSize, column, span):
	return lib.glGetnSeparableFilter(target, format, type, rowBufSize, row, columnBufSize, column, span)

def glVertexAttrib4sv(index, v):
	return lib.glVertexAttrib4sv(index, v)

def glProgramUniform1dv(program, location, count, value):
	return lib.glProgramUniform1dv(program, location, count, value)

def glLighti(light, pname, param):
	return lib.glLighti(light, pname, param)

def glTexImage1D(target, level, internalformat, width, border, format, type):
	pixels = ffi.new('const void *')
	return lib.glTexImage1D(target, level, internalformat, width, border, format, type, pixels)

def glLightf(light, pname, param):
	return lib.glLightf(light, pname, param)

def glSampleCoverage(value, invert):
	return lib.glSampleCoverage(value, invert)

def glSecondaryColor3usv(v):
	return lib.glSecondaryColor3usv(v)

def glGetTransformFeedbacki_v(xfb, pname, index, param):
	return lib.glGetTransformFeedbacki_v(xfb, pname, index, param)

def glUniform2i(location, v0, v1):
	return lib.glUniform2i(location, v0, v1)

def glMapGrid2f(un, u1, u2, vn, v1, v2):
	return lib.glMapGrid2f(un, u1, u2, vn, v1, v2)

def glVertexAttribL1d(index, x):
	return lib.glVertexAttribL1d(index, x)

def glFramebufferTextureLayer(target, attachment, texture, level, layer):
	return lib.glFramebufferTextureLayer(target, attachment, texture, level, layer)

def glProgramUniform2fv(program, location, count, value):
	return lib.glProgramUniform2fv(program, location, count, value)

def glProgramUniformMatrix2x4dv(program, location, count, transpose, value):
	return lib.glProgramUniformMatrix2x4dv(program, location, count, transpose, value)

def glTexEnvf(target, pname, param):
	return lib.glTexEnvf(target, pname, param)

def glGetInteger64i_v(target, index):
	data = ffi.new('GLint64 *')
	return lib.glGetInteger64i_v(target, index, data)

def glTexEnvi(target, pname, param):
	return lib.glTexEnvi(target, pname, param)

def glBlitFramebuffer(srcX0, srcY0, srcX1, srcY1, dstX0, dstY0, dstX1, dstY1, mask, filter):
	return lib.glBlitFramebuffer(srcX0, srcY0, srcX1, srcY1, dstX0, dstY0, dstX1, dstY1, mask, filter)

def glIsEnabledi(target, index):
	return lib.glIsEnabledi(target, index)

def glTexCoord2i(s, t):
	return lib.glTexCoord2i(s, t)

def glVertexAttribP2ui(index, type, normalized, value):
	return lib.glVertexAttribP2ui(index, type, normalized, value)

def glGetMapiv(target, query, v):
	return lib.glGetMapiv(target, query, v)

def glObjectPtrLabel(ptr, length, label):
	return lib.glObjectPtrLabel(ptr, length, label)

def glGetDebugMessageLog(count, bufSize, sources, types, ids, severities, lengths, messageLog):
	return lib.glGetDebugMessageLog(count, bufSize, sources, types, ids, severities, lengths, messageLog)

def glBindFragDataLocation(program, color):
	name = ffi.new('const GLchar *')
	return lib.glBindFragDataLocation(program, color, name)

def glSecondaryColor3ubv(v):
	return lib.glSecondaryColor3ubv(v)

def glLightModelf(pname, param):
	return lib.glLightModelf(pname, param)

def glMultiDrawElementsIndirect(mode, type, indirect, drawcount, stride):
	return lib.glMultiDrawElementsIndirect(mode, type, indirect, drawcount, stride)

def glCallLists(n, type, lists):
	return lib.glCallLists(n, type, lists)

def glFrustum(left, right, bottom, top, zNear, zFar):
	return lib.glFrustum(left, right, bottom, top, zNear, zFar)

def glTexCoord3i(s, t, r):
	return lib.glTexCoord3i(s, t, r)

def glVertexAttribI3uiv(index, v):
	return lib.glVertexAttribI3uiv(index, v)

def glPushDebugGroup(source, id, length, message):
	return lib.glPushDebugGroup(source, id, length, message)

def glMultiTexCoordP1uiv(texture, type, coords):
	return lib.glMultiTexCoordP1uiv(texture, type, coords)

def glCopyTexSubImage3D(target, level, xoffset, yoffset, zoffset, x, y, width, height):
	return lib.glCopyTexSubImage3D(target, level, xoffset, yoffset, zoffset, x, y, width, height)

def glGetActiveUniformBlockName(program, uniformBlockIndex, bufSize, length, uniformBlockName):
	return lib.glGetActiveUniformBlockName(program, uniformBlockIndex, bufSize, length, uniformBlockName)

def glTexCoord3s(s, t, r):
	return lib.glTexCoord3s(s, t, r)

def glAreTexturesResident(n, textures, residences):
	return lib.glAreTexturesResident(n, textures, residences)

def glProgramUniform2d(program, location, v0, v1):
	return lib.glProgramUniform2d(program, location, v0, v1)

def glProgramUniform2f(program, location, v0, v1):
	return lib.glProgramUniform2f(program, location, v0, v1)

def glRasterPos4sv(v):
	return lib.glRasterPos4sv(v)

def glColor4s(red, green, blue, alpha):
	return lib.glColor4s(red, green, blue, alpha)

def glBindVertexArray(array):
	return lib.glBindVertexArray(array)

def glColor4b(red, green, blue, alpha):
	return lib.glColor4b(red, green, blue, alpha)

def glColor4f(red, green, blue, alpha):
	return lib.glColor4f(red, green, blue, alpha)

def glColor4d(red, green, blue, alpha):
	return lib.glColor4d(red, green, blue, alpha)

def glColor4i(red, green, blue, alpha):
	return lib.glColor4i(red, green, blue, alpha)

def glNamedBufferSubData(buffer, offset, size):
	data = ffi.new('const void *')
	return lib.glNamedBufferSubData(buffer, offset, size, data)

def glVertex2dv(v):
	return lib.glVertex2dv(v)

def glBindFramebuffer(target, framebuffer):
	return lib.glBindFramebuffer(target, framebuffer)

def glRectfv(v1, v2):
	return lib.glRectfv(v1, v2)

def glUniformMatrix2x4dv(location, count, transpose, value):
	return lib.glUniformMatrix2x4dv(location, count, transpose, value)

def glGetProgramResourceLocationIndex(program, programInterface):
	name = ffi.new('const GLchar *')
	return lib.glGetProgramResourceLocationIndex(program, programInterface, name)

def glViewport(x, y, width, height):
	return lib.glViewport(x, y, width, height)

def glIsRenderbuffer(renderbuffer):
	return lib.glIsRenderbuffer(renderbuffer)

def glTexStorage2DMultisample(target, samples, internalformat, width, height, fixedsamplelocations):
	return lib.glTexStorage2DMultisample(target, samples, internalformat, width, height, fixedsamplelocations)

def glGetActiveSubroutineUniformiv(program, shadertype, index, pname):
	values = ffi.new('GLint *')
	return lib.glGetActiveSubroutineUniformiv(program, shadertype, index, pname, values)

def glTexBuffer(target, internalformat, buffer):
	return lib.glTexBuffer(target, internalformat, buffer)

def glArrayElement(i):
	return lib.glArrayElement(i)

def glValidateProgram(program):
	return lib.glValidateProgram(program)

def glActiveShaderProgram(pipeline, program):
	return lib.glActiveShaderProgram(pipeline, program)

def glMultiTexCoordP2uiv(texture, type, coords):
	return lib.glMultiTexCoordP2uiv(texture, type, coords)

def glRecti(x1, y1, x2, y2):
	return lib.glRecti(x1, y1, x2, y2)

def glRectf(x1, y1, x2, y2):
	return lib.glRectf(x1, y1, x2, y2)

def glRectd(x1, y1, x2, y2):
	return lib.glRectd(x1, y1, x2, y2)

def glBindTexture(target, texture):
	return lib.glBindTexture(target, texture)

def glRects(x1, y1, x2, y2):
	return lib.glRects(x1, y1, x2, y2)

def glDetachShader(program, shader):
	return lib.glDetachShader(program, shader)

def glTextureSubImage2D(texture, level, xoffset, yoffset, width, height, format, type):
	pixels = ffi.new('const void *')
	return lib.glTextureSubImage2D(texture, level, xoffset, yoffset, width, height, format, type, pixels)

def glGetProgramResourceLocation(program, programInterface):
	name = ffi.new('const GLchar *')
	return lib.glGetProgramResourceLocation(program, programInterface, name)

def glViewportIndexedfv(index, v):
	return lib.glViewportIndexedfv(index, v)

def glDrawElementsBaseVertex(mode, count, type, indices, basevertex):
	return lib.glDrawElementsBaseVertex(mode, count, type, indices, basevertex)

def glClearBufferSubData(target, internalformat, offset, size, format, type):
	data = ffi.new('const void *')
	return lib.glClearBufferSubData(target, internalformat, offset, size, format, type, data)

def glTexStorage1D(target, levels, internalformat, width):
	return lib.glTexStorage1D(target, levels, internalformat, width)

def glGetUniformiv(program, location):
	params = ffi.new('GLint *')
	return lib.glGetUniformiv(program, location, params)

def glBindBuffer(target, buffer):
	return lib.glBindBuffer(target, buffer)

def glUniform4ui(location, v0, v1, v2, v3):
	return lib.glUniform4ui(location, v0, v1, v2, v3)

def glTexGenf(coord, pname, param):
	return lib.glTexGenf(coord, pname, param)

def glTexGend(coord, pname, param):
	return lib.glTexGend(coord, pname, param)

def glTexGeni(coord, pname, param):
	return lib.glTexGeni(coord, pname, param)

def glScissorIndexed(index, left, bottom, width, height):
	return lib.glScissorIndexed(index, left, bottom, width, height)

def glRasterPos4dv(v):
	return lib.glRasterPos4dv(v)

def glRasterPos2dv(v):
	return lib.glRasterPos2dv(v)

def glTexCoord2iv(v):
	return lib.glTexCoord2iv(v)

def glCreateShaderProgramv(type, count, conststrings):
	return lib.glCreateShaderProgramv(type, count, conststrings)

def glGetQueryObjectiv(id, pname):
	params = ffi.new('GLint *')
	return lib.glGetQueryObjectiv(id, pname, params)

def glVertex2s(x, y):
	return lib.glVertex2s(x, y)

def glGenerateMipmap(target):
	return lib.glGenerateMipmap(target)

def glCompressedTextureSubImage2D(texture, level, xoffset, yoffset, width, height, format, imageSize):
	data = ffi.new('const void *')
	return lib.glCompressedTextureSubImage2D(texture, level, xoffset, yoffset, width, height, format, imageSize, data)

def glDeleteLists(list, range):
	return lib.glDeleteLists(list, range)

def glPointParameteri(pname, param):
	return lib.glPointParameteri(pname, param)

def glColor4iv(v):
	return lib.glColor4iv(v)

def glUnmapBuffer(target):
	return lib.glUnmapBuffer(target)

def glPointParameterf(pname, param):
	return lib.glPointParameterf(pname, param)

def glTexCoord2s(s, t):
	return lib.glTexCoord2s(s, t)

def glTexCoord4dv(v):
	return lib.glTexCoord4dv(v)

def glNormal3dv(v):
	return lib.glNormal3dv(v)

def glReleaseShaderCompiler():
	return lib.glReleaseShaderCompiler()

def glTexCoord1dv(v):
	return lib.glTexCoord1dv(v)

def glReadPixels(x, y, width, height, format, type):
	pixels = ffi.new('void *')
	return lib.glReadPixels(x, y, width, height, format, type, pixels)

def glNamedRenderbufferStorageMultisample(renderbuffer, samples, internalformat, width, height):
	return lib.glNamedRenderbufferStorageMultisample(renderbuffer, samples, internalformat, width, height)

def glVertexAttribI3iv(index, v):
	return lib.glVertexAttribI3iv(index, v)

def glShadeModel(mode):
	return lib.glShadeModel(mode)

def glMapGrid1d(un, u1, u2):
	return lib.glMapGrid1d(un, u1, u2)

def glInvalidateNamedFramebufferData(framebuffer, numAttachments, attachments):
	return lib.glInvalidateNamedFramebufferData(framebuffer, numAttachments, attachments)

def glRectiv(v1, v2):
	return lib.glRectiv(v1, v2)

def glColorP4ui(type, color):
	return lib.glColorP4ui(type, color)

def glUseProgramStages(pipeline, stages, program):
	return lib.glUseProgramStages(pipeline, stages, program)

def glRasterPos3dv(v):
	return lib.glRasterPos3dv(v)

def glReadBuffer(src):
	return lib.glReadBuffer(src)

def glColor4ubv(v):
	return lib.glColor4ubv(v)

def glGetBufferSubData(target, offset, size):
	data = ffi.new('void *')
	return lib.glGetBufferSubData(target, offset, size, data)

def glGetVertexAttribLdv(index, pname):
	params = ffi.new('GLdouble *')
	return lib.glGetVertexAttribLdv(index, pname, params)

def glGetnUniformuiv(program, location, bufSize):
	params = ffi.new('GLuint *')
	return lib.glGetnUniformuiv(program, location, bufSize, params)

def glGenBuffers(n, buffers):
	return lib.glGenBuffers(n, buffers)

def glClearNamedFramebufferiv(framebuffer, buffer, drawbuffer, value):
	return lib.glClearNamedFramebufferiv(framebuffer, buffer, drawbuffer, value)

def glVertexAttribI2iv(index, v):
	return lib.glVertexAttribI2iv(index, v)

def glIsFramebuffer(framebuffer):
	return lib.glIsFramebuffer(framebuffer)

def glTexCoordP4uiv(type, coords):
	return lib.glTexCoordP4uiv(type, coords)

def glTexGendv(coord, pname):
	params = ffi.new('const GLdouble *')
	return lib.glTexGendv(coord, pname, params)

def glVertexP2uiv(type, value):
	return lib.glVertexP2uiv(type, value)

def glTexCoord2d(s, t):
	return lib.glTexCoord2d(s, t)

def glGetBufferParameteri64v(target, pname):
	params = ffi.new('GLint64 *')
	return lib.glGetBufferParameteri64v(target, pname, params)

def glProgramUniform4dv(program, location, count, value):
	return lib.glProgramUniform4dv(program, location, count, value)

def glTexCoord2f(s, t):
	return lib.glTexCoord2f(s, t)

def glMultiTexCoord3fv(target, v):
	return lib.glMultiTexCoord3fv(target, v)

def glCreateRenderbuffers(n, renderbuffers):
	return lib.glCreateRenderbuffers(n, renderbuffers)

def glVertexAttrib4Nusv(index, v):
	return lib.glVertexAttrib4Nusv(index, v)

def glDepthFunc(func):
	return lib.glDepthFunc(func)

def glSamplerParameterf(sampler, pname, param):
	return lib.glSamplerParameterf(sampler, pname, param)

def glBlendFunci(buf, src, dst):
	return lib.glBlendFunci(buf, src, dst)

def glVertexAttrib3dv(index, v):
	return lib.glVertexAttrib3dv(index, v)

def glBufferStorage(target, size, flags):
	data = ffi.new('const void *')
	return lib.glBufferStorage(target, size, data, flags)

def glGetFloati_v(target, index):
	data = ffi.new('GLfloat *')
	return lib.glGetFloati_v(target, index, data)

def glGetUniformLocation(program):
	name = ffi.new('const GLchar *')
	return lib.glGetUniformLocation(program, name)

def glNamedFramebufferDrawBuffers(framebuffer, n, bufs):
	return lib.glNamedFramebufferDrawBuffers(framebuffer, n, bufs)

def glUniform4fv(location, count, value):
	return lib.glUniform4fv(location, count, value)

def glVertexAttribP4uiv(index, type, normalized, value):
	return lib.glVertexAttribP4uiv(index, type, normalized, value)

def glCompressedTextureSubImage3D(texture, level, xoffset, yoffset, zoffset, width, height, depth, format, imageSize):
	data = ffi.new('const void *')
	return lib.glCompressedTextureSubImage3D(texture, level, xoffset, yoffset, zoffset, width, height, depth, format, imageSize, data)

def glVertexAttrib4Nbv(index, v):
	return lib.glVertexAttrib4Nbv(index, v)

def glEndConditionalRender():
	return lib.glEndConditionalRender()

def glEnableClientState(array):
	return lib.glEnableClientState(array)

def glMultiTexCoord2sv(target, v):
	return lib.glMultiTexCoord2sv(target, v)

def glProgramUniform2uiv(program, location, count, value):
	return lib.glProgramUniform2uiv(program, location, count, value)

def glGetQueryObjectuiv(id, pname):
	params = ffi.new('GLuint *')
	return lib.glGetQueryObjectuiv(id, pname, params)

def glVertexAttrib4iv(index, v):
	return lib.glVertexAttrib4iv(index, v)

def glProgramUniform1uiv(program, location, count, value):
	return lib.glProgramUniform1uiv(program, location, count, value)

def glFramebufferTexture(target, attachment, texture, level):
	return lib.glFramebufferTexture(target, attachment, texture, level)

def glGetTexGendv(coord, pname):
	params = ffi.new('GLdouble *')
	return lib.glGetTexGendv(coord, pname, params)

def glColor3usv(v):
	return lib.glColor3usv(v)

def glProgramUniformMatrix2x4fv(program, location, count, transpose, value):
	return lib.glProgramUniformMatrix2x4fv(program, location, count, transpose, value)

def glProgramUniform2dv(program, location, count, value):
	return lib.glProgramUniform2dv(program, location, count, value)

def glRasterPos2sv(v):
	return lib.glRasterPos2sv(v)

def glTexCoord1sv(v):
	return lib.glTexCoord1sv(v)

def glVertex2i(x, y):
	return lib.glVertex2i(x, y)

def glGetFloatv(pname):
	data = ffi.new('GLfloat *')
	return lib.glGetFloatv(pname, data)

def glWindowPos3f(x, y, z):
	return lib.glWindowPos3f(x, y, z)

def glSecondaryColorP3uiv(type, color):
	return lib.glSecondaryColorP3uiv(type, color)

def glGetIntegerv(pname):
	data = ffi.new('GLint *')
	return lib.glGetIntegerv(pname, data)

def glProgramUniformMatrix3dv(program, location, count, transpose, value):
	return lib.glProgramUniformMatrix3dv(program, location, count, transpose, value)

def glIsQuery(id):
	return lib.glIsQuery(id)

def glTexImage2D(target, level, internalformat, width, height, border, format, type):
	pixels = ffi.new('const void *')
	return lib.glTexImage2D(target, level, internalformat, width, height, border, format, type, pixels)

def glDrawPixels(width, height, format, type):
	pixels = ffi.new('const void *')
	return lib.glDrawPixels(width, height, format, type, pixels)

def glMultMatrixd(m):
	return lib.glMultMatrixd(m)

def glMultMatrixf(m):
	return lib.glMultMatrixf(m)

def glVertexAttrib4Nubv(index, v):
	return lib.glVertexAttrib4Nubv(index, v)

def glColor4usv(v):
	return lib.glColor4usv(v)

def glMapGrid1f(un, u1, u2):
	return lib.glMapGrid1f(un, u1, u2)

def glPolygonStipple(mask):
	return lib.glPolygonStipple(mask)

def glInterleavedArrays(format, stride, pointer):
	return lib.glInterleavedArrays(format, stride, pointer)

def glGetSubroutineUniformLocation(program, shadertype):
	name = ffi.new('const GLchar *')
	return lib.glGetSubroutineUniformLocation(program, shadertype, name)

def glGetFramebufferParameteriv(target, pname):
	params = ffi.new('GLint *')
	return lib.glGetFramebufferParameteriv(target, pname, params)

def glPixelMapusv(map, mapsize):
	values = ffi.new('const GLushort *')
	return lib.glPixelMapusv(map, mapsize, values)

def glGetSamplerParameteriv(sampler, pname):
	params = ffi.new('GLint *')
	return lib.glGetSamplerParameteriv(sampler, pname, params)

def glCopyBufferSubData(readTarget, writeTarget, readOffset, writeOffset, size):
	return lib.glCopyBufferSubData(readTarget, writeTarget, readOffset, writeOffset, size)

def glVertexAttribI1uiv(index, v):
	return lib.glVertexAttribI1uiv(index, v)

def glColor3fv(v):
	return lib.glColor3fv(v)

def glGetActiveUniform(program, index, bufSize, length, size, type):
	name = ffi.new('GLchar *')
	return lib.glGetActiveUniform(program, index, bufSize, length, size, type, name)

def glNamedFramebufferTextureLayer(framebuffer, attachment, texture, level, layer):
	return lib.glNamedFramebufferTextureLayer(framebuffer, attachment, texture, level, layer)

def glVertexAttribL3d(index, x, y, z):
	return lib.glVertexAttribL3d(index, x, y, z)

def glTexCoord3sv(v):
	return lib.glTexCoord3sv(v)

def glMinSampleShading(value):
	return lib.glMinSampleShading(value)

def glVertex2fv(v):
	return lib.glVertex2fv(v)

def glFramebufferRenderbuffer(target, attachment, renderbuffertarget, renderbuffer):
	return lib.glFramebufferRenderbuffer(target, attachment, renderbuffertarget, renderbuffer)

def glGetDoublei_v(target, index):
	data = ffi.new('GLdouble *')
	return lib.glGetDoublei_v(target, index, data)

def glVertexAttrib1sv(index, v):
	return lib.glVertexAttrib1sv(index, v)

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

def glWindowPos2iv(v):
	return lib.glWindowPos2iv(v)

def glFogiv(pname):
	params = ffi.new('const GLint *')
	return lib.glFogiv(pname, params)

def glLightModeliv(pname):
	params = ffi.new('const GLint *')
	return lib.glLightModeliv(pname, params)

def glDepthRangef(n, f):
	return lib.glDepthRangef(n, f)

def glEnablei(target, index):
	return lib.glEnablei(target, index)

def glEvalCoord1fv(u):
	return lib.glEvalCoord1fv(u)

def glSampleMaski(maskNumber, mask):
	return lib.glSampleMaski(maskNumber, mask)

def glUniformMatrix3x2fv(location, count, transpose, value):
	return lib.glUniformMatrix3x2fv(location, count, transpose, value)

def glGetInternalformativ(target, internalformat, pname, bufSize):
	params = ffi.new('GLint *')
	return lib.glGetInternalformativ(target, internalformat, pname, bufSize, params)

def glVertexAttrib2dv(index, v):
	return lib.glVertexAttrib2dv(index, v)

def glEdgeFlag(flag):
	return lib.glEdgeFlag(flag)

def glProgramUniform1ui(program, location, v0):
	return lib.glProgramUniform1ui(program, location, v0)

def glVertex3d(x, y, z):
	return lib.glVertex3d(x, y, z)

def glVertex3f(x, y, z):
	return lib.glVertex3f(x, y, z)

def glVertex3s(x, y, z):
	return lib.glVertex3s(x, y, z)

def glTexCoordP2ui(type, coords):
	return lib.glTexCoordP2ui(type, coords)

def glColorMaski(index, r, g, b, a):
	return lib.glColorMaski(index, r, g, b, a)

def glCopyNamedBufferSubData(readBuffer, writeBuffer, readOffset, writeOffset, size):
	return lib.glCopyNamedBufferSubData(readBuffer, writeBuffer, readOffset, writeOffset, size)

def glTexStorage3D(target, levels, internalformat, width, height, depth):
	return lib.glTexStorage3D(target, levels, internalformat, width, height, depth)

def glTextureParameteriv(texture, pname, param):
	return lib.glTextureParameteriv(texture, pname, param)

def glUniformMatrix3x4fv(location, count, transpose, value):
	return lib.glUniformMatrix3x4fv(location, count, transpose, value)

def glNormalPointer(type, stride, pointer):
	return lib.glNormalPointer(type, stride, pointer)

def glNamedFramebufferTexture(framebuffer, attachment, texture, level):
	return lib.glNamedFramebufferTexture(framebuffer, attachment, texture, level)

def glPassThrough(token):
	return lib.glPassThrough(token)

def glSecondaryColorP3ui(type, color):
	return lib.glSecondaryColorP3ui(type, color)

def glProgramUniformMatrix4x3fv(program, location, count, transpose, value):
	return lib.glProgramUniformMatrix4x3fv(program, location, count, transpose, value)

def glBegin(mode):
	return lib.glBegin(mode)

def glEvalCoord2dv(u):
	return lib.glEvalCoord2dv(u)

def glColor3ubv(v):
	return lib.glColor3ubv(v)

def glVertexP3ui(type, value):
	return lib.glVertexP3ui(type, value)

def glLightfv(light, pname):
	params = ffi.new('const GLfloat *')
	return lib.glLightfv(light, pname, params)

def glGetActiveUniformName(program, uniformIndex, bufSize, length, uniformName):
	return lib.glGetActiveUniformName(program, uniformIndex, bufSize, length, uniformName)

def glGetFramebufferAttachmentParameteriv(target, attachment, pname):
	params = ffi.new('GLint *')
	return lib.glGetFramebufferAttachmentParameteriv(target, attachment, pname, params)

def glMultiTexCoord2f(target, s, t):
	return lib.glMultiTexCoord2f(target, s, t)

def glNamedFramebufferDrawBuffer(framebuffer, buf):
	return lib.glNamedFramebufferDrawBuffer(framebuffer, buf)

def glTexParameteriv(target, pname):
	params = ffi.new('const GLint *')
	return lib.glTexParameteriv(target, pname, params)

def glVertexArrayVertexBuffer(vaobj, bindingindex, buffer, offset, stride):
	return lib.glVertexArrayVertexBuffer(vaobj, bindingindex, buffer, offset, stride)

def glGetTexImage(target, level, format, type):
	pixels = ffi.new('void *')
	return lib.glGetTexImage(target, level, format, type, pixels)

def glTransformFeedbackBufferBase(xfb, index, buffer):
	return lib.glTransformFeedbackBufferBase(xfb, index, buffer)

def glIndexsv(c):
	return lib.glIndexsv(c)

def glTexCoordP3uiv(type, coords):
	return lib.glTexCoordP3uiv(type, coords)

def glBitmap(width, height, xorig, yorig, xmove, ymove, bitmap):
	return lib.glBitmap(width, height, xorig, yorig, xmove, ymove, bitmap)

def glGetNamedBufferSubData(buffer, offset, size):
	data = ffi.new('void *')
	return lib.glGetNamedBufferSubData(buffer, offset, size, data)

def glProgramUniform2iv(program, location, count, value):
	return lib.glProgramUniform2iv(program, location, count, value)

def glGetQueryiv(target, pname):
	params = ffi.new('GLint *')
	return lib.glGetQueryiv(target, pname, params)

def glGetTransformFeedbackiv(xfb, pname, param):
	return lib.glGetTransformFeedbackiv(xfb, pname, param)

def glTexCoord4i(s, t, r, q):
	return lib.glTexCoord4i(s, t, r, q)

def glObjectLabel(identifier, length, label):
	name = ffi.new('GLuint *')
	return lib.glObjectLabel(identifier, name, length, label)

def glPointParameteriv(pname):
	params = ffi.new('const GLint *')
	return lib.glPointParameteriv(pname, params)

def glNormal3fv(v):
	return lib.glNormal3fv(v)

def glTexCoord1fv(v):
	return lib.glTexCoord1fv(v)

def glMultiTexCoord1dv(target, v):
	return lib.glMultiTexCoord1dv(target, v)

def glTexCoord3fv(v):
	return lib.glTexCoord3fv(v)

def glMultiTexCoordP3uiv(texture, type, coords):
	return lib.glMultiTexCoordP3uiv(texture, type, coords)

def glVertexAttribP3ui(index, type, normalized, value):
	return lib.glVertexAttribP3ui(index, type, normalized, value)

def glDepthRange(near, far):
	return lib.glDepthRange(near, far)

def glDrawBuffer(buf):
	return lib.glDrawBuffer(buf)

def glGetnPixelMapusv(map, bufSize):
	values = ffi.new('GLushort *')
	return lib.glGetnPixelMapusv(map, bufSize, values)

def glRasterPos3fv(v):
	return lib.glRasterPos3fv(v)

def glClearBufferuiv(buffer, drawbuffer, value):
	return lib.glClearBufferuiv(buffer, drawbuffer, value)

def glGetInternalformati64v(target, internalformat, pname, bufSize):
	params = ffi.new('GLint64 *')
	return lib.glGetInternalformati64v(target, internalformat, pname, bufSize, params)

def glClearIndex(c):
	return lib.glClearIndex(c)

def glVertexAttribIPointer(index, size, type, stride, pointer):
	return lib.glVertexAttribIPointer(index, size, type, stride, pointer)

def glFlush():
	return lib.glFlush()

def glDrawElementsInstancedBaseVertexBaseInstance(mode, count, type, indices, instancecount, basevertex, baseinstance):
	return lib.glDrawElementsInstancedBaseVertexBaseInstance(mode, count, type, indices, instancecount, basevertex, baseinstance)

def glGetTexLevelParameteriv(target, level, pname):
	params = ffi.new('GLint *')
	return lib.glGetTexLevelParameteriv(target, level, pname, params)

def glPrioritizeTextures(n, textures, priorities):
	return lib.glPrioritizeTextures(n, textures, priorities)

def glSelectBuffer(size, buffer):
	return lib.glSelectBuffer(size, buffer)

def glTexStorage3DMultisample(target, samples, internalformat, width, height, depth, fixedsamplelocations):
	return lib.glTexStorage3DMultisample(target, samples, internalformat, width, height, depth, fixedsamplelocations)

def glClampColor(target, clamp):
	return lib.glClampColor(target, clamp)

def glClearStencil(s):
	return lib.glClearStencil(s)

def glTexCoordP1uiv(type, coords):
	return lib.glTexCoordP1uiv(type, coords)

def glIsTexture(texture):
	return lib.glIsTexture(texture)

def glVertex2f(x, y):
	return lib.glVertex2f(x, y)

def glVertex2d(x, y):
	return lib.glVertex2d(x, y)

def glBeginQueryIndexed(target, index, id):
	return lib.glBeginQueryIndexed(target, index, id)

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

def glFlushMappedBufferRange(target, offset, length):
	return lib.glFlushMappedBufferRange(target, offset, length)

def glTexStorage2D(target, levels, internalformat, width, height):
	return lib.glTexStorage2D(target, levels, internalformat, width, height)

def glGenQueries(n, ids):
	return lib.glGenQueries(n, ids)

def glGetPixelMapfv(map):
	values = ffi.new('GLfloat *')
	return lib.glGetPixelMapfv(map, values)

def glTexSubImage3D(target, level, xoffset, yoffset, zoffset, width, height, depth, format, type):
	pixels = ffi.new('const void *')
	return lib.glTexSubImage3D(target, level, xoffset, yoffset, zoffset, width, height, depth, format, type, pixels)

def glDeleteSamplers(count, samplers):
	return lib.glDeleteSamplers(count, samplers)

def glGetTextureParameterfv(texture, pname):
	params = ffi.new('GLfloat *')
	return lib.glGetTextureParameterfv(texture, pname, params)

def glMatrixMode(mode):
	return lib.glMatrixMode(mode)

def glBindTextures(first, count, textures):
	return lib.glBindTextures(first, count, textures)

def glGetDoublev(pname):
	data = ffi.new('GLdouble *')
	return lib.glGetDoublev(pname, data)

def glVertexAttrib1d(index, x):
	return lib.glVertexAttrib1d(index, x)

def glUniform4dv(location, count, value):
	return lib.glUniform4dv(location, count, value)

def glProgramUniform3dv(program, location, count, value):
	return lib.glProgramUniform3dv(program, location, count, value)

def glInvalidateBufferData(buffer):
	return lib.glInvalidateBufferData(buffer)

def glCompressedTextureSubImage1D(texture, level, xoffset, width, format, imageSize):
	data = ffi.new('const void *')
	return lib.glCompressedTextureSubImage1D(texture, level, xoffset, width, format, imageSize, data)

def glClearTexImage(texture, level, format, type):
	data = ffi.new('const void *')
	return lib.glClearTexImage(texture, level, format, type, data)

def glUniform3fv(location, count, value):
	return lib.glUniform3fv(location, count, value)

def glMultiTexCoordP1ui(texture, type, coords):
	return lib.glMultiTexCoordP1ui(texture, type, coords)

def glGetTransformFeedbacki64_v(xfb, pname, index, param):
	return lib.glGetTransformFeedbacki64_v(xfb, pname, index, param)

def glMultiDrawElements(mode, count, type, constindices, drawcount):
	return lib.glMultiDrawElements(mode, count, type, constindices, drawcount)

def glDrawBuffers(n, bufs):
	return lib.glDrawBuffers(n, bufs)

def glNamedFramebufferReadBuffer(framebuffer, src):
	return lib.glNamedFramebufferReadBuffer(framebuffer, src)

def glGetTexGenfv(coord, pname):
	params = ffi.new('GLfloat *')
	return lib.glGetTexGenfv(coord, pname, params)

def glBindTransformFeedback(target, id):
	return lib.glBindTransformFeedback(target, id)

def glMultiTexCoord2iv(target, v):
	return lib.glMultiTexCoord2iv(target, v)

def glSecondaryColor3f(red, green, blue):
	return lib.glSecondaryColor3f(red, green, blue)

def glRasterPos3iv(v):
	return lib.glRasterPos3iv(v)

def glVertexP2ui(type, value):
	return lib.glVertexP2ui(type, value)

def glGetnConvolutionFilter(target, format, type, bufSize, image):
	return lib.glGetnConvolutionFilter(target, format, type, bufSize, image)

def glSecondaryColor3b(red, green, blue):
	return lib.glSecondaryColor3b(red, green, blue)

def glTexCoord4sv(v):
	return lib.glTexCoord4sv(v)

def glUniform2uiv(location, count, value):
	return lib.glUniform2uiv(location, count, value)

def glFinish():
	return lib.glFinish()

def glRasterPos2s(x, y):
	return lib.glRasterPos2s(x, y)

def glUniform1uiv(location, count, value):
	return lib.glUniform1uiv(location, count, value)

def glUniformMatrix2dv(location, count, transpose, value):
	return lib.glUniformMatrix2dv(location, count, transpose, value)

def glIndexdv(c):
	return lib.glIndexdv(c)

def glTexCoord3iv(v):
	return lib.glTexCoord3iv(v)

def glClearDepth(depth):
	return lib.glClearDepth(depth)

def glUniformMatrix4dv(location, count, transpose, value):
	return lib.glUniformMatrix4dv(location, count, transpose, value)

def glProgramUniformMatrix4x3dv(program, location, count, transpose, value):
	return lib.glProgramUniformMatrix4x3dv(program, location, count, transpose, value)

def glVertex4dv(v):
	return lib.glVertex4dv(v)

def glCreateTextures(target, n, textures):
	return lib.glCreateTextures(target, n, textures)

def glCreateBuffers(n, buffers):
	return lib.glCreateBuffers(n, buffers)

def glMultTransposeMatrixf(m):
	return lib.glMultTransposeMatrixf(m)

def glEdgeFlagv(flag):
	return lib.glEdgeFlagv(flag)

def glUniformMatrix4x3dv(location, count, transpose, value):
	return lib.glUniformMatrix4x3dv(location, count, transpose, value)

def glDeleteQueries(n, ids):
	return lib.glDeleteQueries(n, ids)

def glNormalP3uiv(type, coords):
	return lib.glNormalP3uiv(type, coords)

def glRasterPos2d(x, y):
	return lib.glRasterPos2d(x, y)

def glInitNames():
	return lib.glInitNames()

def glColor3dv(v):
	return lib.glColor3dv(v)

def glGetnMinmax(target, reset, format, type, bufSize):
	values = ffi.new('void *')
	return lib.glGetnMinmax(target, reset, format, type, bufSize, values)

def glClearNamedFramebufferuiv(framebuffer, buffer, drawbuffer, value):
	return lib.glClearNamedFramebufferuiv(framebuffer, buffer, drawbuffer, value)

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

def glLogicOp(opcode):
	return lib.glLogicOp(opcode)

def glProgramUniformMatrix3x4fv(program, location, count, transpose, value):
	return lib.glProgramUniformMatrix3x4fv(program, location, count, transpose, value)

def glPixelTransferf(pname, param):
	return lib.glPixelTransferf(pname, param)

def glGetTextureParameterIuiv(texture, pname):
	params = ffi.new('GLuint *')
	return lib.glGetTextureParameterIuiv(texture, pname, params)

def glProgramUniformMatrix4dv(program, location, count, transpose, value):
	return lib.glProgramUniformMatrix4dv(program, location, count, transpose, value)

def glUniformMatrix3x4dv(location, count, transpose, value):
	return lib.glUniformMatrix3x4dv(location, count, transpose, value)

def glDrawTransformFeedbackStream(mode, id, stream):
	return lib.glDrawTransformFeedbackStream(mode, id, stream)

def glUniform3ui(location, v0, v1, v2):
	return lib.glUniform3ui(location, v0, v1, v2)

def glProvokingVertex(mode):
	return lib.glProvokingVertex(mode)

def glShaderBinary(count, shaders, binaryformat, binary, length):
	return lib.glShaderBinary(count, shaders, binaryformat, binary, length)

def glTexGeniv(coord, pname):
	params = ffi.new('const GLint *')
	return lib.glTexGeniv(coord, pname, params)

def glDrawElements(mode, count, type, indices):
	return lib.glDrawElements(mode, count, type, indices)

def glProgramUniform4iv(program, location, count, value):
	return lib.glProgramUniform4iv(program, location, count, value)

def glClientActiveTexture(texture):
	return lib.glClientActiveTexture(texture)

def glUniform1iv(location, count, value):
	return lib.glUniform1iv(location, count, value)

def glDrawArraysInstanced(mode, first, count, instancecount):
	return lib.glDrawArraysInstanced(mode, first, count, instancecount)

def glVertexAttrib4uiv(index, v):
	return lib.glVertexAttrib4uiv(index, v)

def glEndQueryIndexed(target, index):
	return lib.glEndQueryIndexed(target, index)

def glProgramUniform1iv(program, location, count, value):
	return lib.glProgramUniform1iv(program, location, count, value)

def glBindRenderbuffer(target, renderbuffer):
	return lib.glBindRenderbuffer(target, renderbuffer)

def glMaterialiv(face, pname):
	params = ffi.new('const GLint *')
	return lib.glMaterialiv(face, pname, params)

def glIsProgram(program):
	return lib.glIsProgram(program)

def glVertexAttrib4fv(index, v):
	return lib.glVertexAttrib4fv(index, v)

def glProgramUniformMatrix2x3dv(program, location, count, transpose, value):
	return lib.glProgramUniformMatrix2x3dv(program, location, count, transpose, value)

def glGetnPixelMapfv(map, bufSize):
	values = ffi.new('GLfloat *')
	return lib.glGetnPixelMapfv(map, bufSize, values)

def glVertexAttrib2fv(index, v):
	return lib.glVertexAttrib2fv(index, v)

def glDisableClientState(array):
	return lib.glDisableClientState(array)

def glColor4uiv(v):
	return lib.glColor4uiv(v)

def glProgramUniform3i(program, location, v0, v1, v2):
	return lib.glProgramUniform3i(program, location, v0, v1, v2)

def glEvalMesh2(mode, i1, i2, j1, j2):
	return lib.glEvalMesh2(mode, i1, i2, j1, j2)

def glEvalMesh1(mode, i1, i2):
	return lib.glEvalMesh1(mode, i1, i2)

def glProgramUniform3d(program, location, v0, v1, v2):
	return lib.glProgramUniform3d(program, location, v0, v1, v2)

def glEvalCoord2fv(u):
	return lib.glEvalCoord2fv(u)

def glLoadTransposeMatrixd(m):
	return lib.glLoadTransposeMatrixd(m)

def glLoadTransposeMatrixf(m):
	return lib.glLoadTransposeMatrixf(m)

def glVertexAttribI1ui(index, x):
	return lib.glVertexAttribI1ui(index, x)

def glGetnPolygonStipple(bufSize, pattern):
	return lib.glGetnPolygonStipple(bufSize, pattern)

def glInvalidateTexSubImage(texture, level, xoffset, yoffset, zoffset, width, height, depth):
	return lib.glInvalidateTexSubImage(texture, level, xoffset, yoffset, zoffset, width, height, depth)

def glGetInteger64v(pname):
	data = ffi.new('GLint64 *')
	return lib.glGetInteger64v(pname, data)

def glClipPlane(plane, equation):
	return lib.glClipPlane(plane, equation)

def glIndexub(c):
	return lib.glIndexub(c)

def glNamedFramebufferRenderbuffer(framebuffer, attachment, renderbuffertarget, renderbuffer):
	return lib.glNamedFramebufferRenderbuffer(framebuffer, attachment, renderbuffertarget, renderbuffer)

def glVertexAttrib4Niv(index, v):
	return lib.glVertexAttrib4Niv(index, v)

def glClearBufferiv(buffer, drawbuffer, value):
	return lib.glClearBufferiv(buffer, drawbuffer, value)

def glColorP4uiv(type, color):
	return lib.glColorP4uiv(type, color)

def glGetTextureLevelParameterfv(texture, level, pname):
	params = ffi.new('GLfloat *')
	return lib.glGetTextureLevelParameterfv(texture, level, pname, params)

def glMultiTexCoord1fv(target, v):
	return lib.glMultiTexCoord1fv(target, v)

def glGetSamplerParameterIuiv(sampler, pname):
	params = ffi.new('GLuint *')
	return lib.glGetSamplerParameterIuiv(sampler, pname, params)

def glTexCoordP3ui(type, coords):
	return lib.glTexCoordP3ui(type, coords)

def glUniform2f(location, v0, v1):
	return lib.glUniform2f(location, v0, v1)

def glTextureSubImage1D(texture, level, xoffset, width, format, type):
	pixels = ffi.new('const void *')
	return lib.glTextureSubImage1D(texture, level, xoffset, width, format, type, pixels)

def glWindowPos3s(x, y, z):
	return lib.glWindowPos3s(x, y, z)

def glClearDepthf(d):
	return lib.glClearDepthf(d)

def glTextureBufferRange(texture, internalformat, buffer, offset, size):
	return lib.glTextureBufferRange(texture, internalformat, buffer, offset, size)

def glWindowPos3i(x, y, z):
	return lib.glWindowPos3i(x, y, z)

def glWindowPos3d(x, y, z):
	return lib.glWindowPos3d(x, y, z)

def glMultiTexCoordP4ui(texture, type, coords):
	return lib.glMultiTexCoordP4ui(texture, type, coords)

def glColor3us(red, green, blue):
	return lib.glColor3us(red, green, blue)

def glGetLightiv(light, pname):
	params = ffi.new('GLint *')
	return lib.glGetLightiv(light, pname, params)

def glMultiTexCoord4f(target, s, t, r, q):
	return lib.glMultiTexCoord4f(target, s, t, r, q)

def glColor3ub(red, green, blue):
	return lib.glColor3ub(red, green, blue)

def glMultiTexCoord4d(target, s, t, r, q):
	return lib.glMultiTexCoord4d(target, s, t, r, q)

def glColor3ui(red, green, blue):
	return lib.glColor3ui(red, green, blue)

def glMultiTexCoord4i(target, s, t, r, q):
	return lib.glMultiTexCoord4i(target, s, t, r, q)

def glGetPolygonStipple(mask):
	return lib.glGetPolygonStipple(mask)

def glUniform2d(location, x, y):
	return lib.glUniform2d(location, x, y)

def glVertexAttribI4ui(index, x, y, z, w):
	return lib.glVertexAttribI4ui(index, x, y, z, w)

def glColorMask(red, green, blue, alpha):
	return lib.glColorMask(red, green, blue, alpha)

def glGetnTexImage(target, level, format, type, bufSize):
	pixels = ffi.new('void *')
	return lib.glGetnTexImage(target, level, format, type, bufSize, pixels)

def glBlendEquation(mode):
	return lib.glBlendEquation(mode)

def glMultiTexCoord3dv(target, v):
	return lib.glMultiTexCoord3dv(target, v)

def glColor4sv(v):
	return lib.glColor4sv(v)

def glGetProgramResourceiv(program, programInterface, index, propCount, props, bufSize, length):
	params = ffi.new('GLint *')
	return lib.glGetProgramResourceiv(program, programInterface, index, propCount, props, bufSize, length, params)

def glClearBufferData(target, internalformat, format, type):
	data = ffi.new('const void *')
	return lib.glClearBufferData(target, internalformat, format, type, data)

def glBeginTransformFeedback(primitiveMode):
	return lib.glBeginTransformFeedback(primitiveMode)

def glColor3iv(v):
	return lib.glColor3iv(v)

def glVertexAttrib3sv(index, v):
	return lib.glVertexAttrib3sv(index, v)

def glCompressedTexImage1D(target, level, internalformat, width, border, imageSize):
	data = ffi.new('const void *')
	return lib.glCompressedTexImage1D(target, level, internalformat, width, border, imageSize, data)

def glDeleteTransformFeedbacks(n, ids):
	return lib.glDeleteTransformFeedbacks(n, ids)

def glDrawRangeElementsBaseVertex(mode, start, end, count, type, indices, basevertex):
	return lib.glDrawRangeElementsBaseVertex(mode, start, end, count, type, indices, basevertex)

def glBindAttribLocation(program, index):
	name = ffi.new('const GLchar *')
	return lib.glBindAttribLocation(program, index, name)

def glVertexAttrib1dv(index, v):
	return lib.glVertexAttrib1dv(index, v)

def glBlendFuncSeparatei(buf, srcRGB, dstRGB, srcAlpha, dstAlpha):
	return lib.glBlendFuncSeparatei(buf, srcRGB, dstRGB, srcAlpha, dstAlpha)

def glUniform2ui(location, v0, v1):
	return lib.glUniform2ui(location, v0, v1)

def glPixelTransferi(pname, param):
	return lib.glPixelTransferi(pname, param)

def glWindowPos2fv(v):
	return lib.glWindowPos2fv(v)

def glDisablei(target, index):
	return lib.glDisablei(target, index)

def glGetSynciv(sync, pname, bufSize, length):
	values = ffi.new('GLint *')
	return lib.glGetSynciv(sync, pname, bufSize, length, values)

def glProgramUniform2i(program, location, v0, v1):
	return lib.glProgramUniform2i(program, location, v0, v1)

def glGetProgramBinary(program, bufSize, length, binaryFormat, binary):
	return lib.glGetProgramBinary(program, bufSize, length, binaryFormat, binary)

def glEvalPoint1(i):
	return lib.glEvalPoint1(i)

def glEvalPoint2(i, j):
	return lib.glEvalPoint2(i, j)

def glPauseTransformFeedback():
	return lib.glPauseTransformFeedback()

def glCreateTransformFeedbacks(n, ids):
	return lib.glCreateTransformFeedbacks(n, ids)

def glTexSubImage1D(target, level, xoffset, width, format, type):
	pixels = ffi.new('const void *')
	return lib.glTexSubImage1D(target, level, xoffset, width, format, type, pixels)

def glVertexAttribP3uiv(index, type, normalized, value):
	return lib.glVertexAttribP3uiv(index, type, normalized, value)

def glVertexAttribI4iv(index, v):
	return lib.glVertexAttribI4iv(index, v)

def glGetVertexArrayiv(vaobj, pname, param):
	return lib.glGetVertexArrayiv(vaobj, pname, param)

def glLoadName():
	name = ffi.new('GLuint *')
	return lib.glLoadName(name)

def glLoadMatrixf(m):
	return lib.glLoadMatrixf(m)

def glLoadMatrixd(m):
	return lib.glLoadMatrixd(m)

def glTexParameterfv(target, pname):
	params = ffi.new('const GLfloat *')
	return lib.glTexParameterfv(target, pname, params)

def glUniform3dv(location, count, value):
	return lib.glUniform3dv(location, count, value)

def glStencilFuncSeparate(face, func, ref, mask):
	return lib.glStencilFuncSeparate(face, func, ref, mask)

def glProgramUniform3fv(program, location, count, value):
	return lib.glProgramUniform3fv(program, location, count, value)

def glBindSamplers(first, count, samplers):
	return lib.glBindSamplers(first, count, samplers)

def glGetQueryObjectui64v(id, pname):
	params = ffi.new('GLuint64 *')
	return lib.glGetQueryObjectui64v(id, pname, params)

def glGetTextureImage(texture, level, format, type, bufSize):
	pixels = ffi.new('void *')
	return lib.glGetTextureImage(texture, level, format, type, bufSize, pixels)

def glProgramUniform1fv(program, location, count, value):
	return lib.glProgramUniform1fv(program, location, count, value)

def glUniformMatrix4fv(location, count, transpose, value):
	return lib.glUniformMatrix4fv(location, count, transpose, value)

def glDeleteProgramPipelines(n, pipelines):
	return lib.glDeleteProgramPipelines(n, pipelines)

def glVertex3fv(v):
	return lib.glVertex3fv(v)

def glWindowPos2s(x, y):
	return lib.glWindowPos2s(x, y)

def glWindowPos2i(x, y):
	return lib.glWindowPos2i(x, y)

def glWindowPos2f(x, y):
	return lib.glWindowPos2f(x, y)

def glWindowPos2d(x, y):
	return lib.glWindowPos2d(x, y)

def glUniformSubroutinesuiv(shadertype, count, indices):
	return lib.glUniformSubroutinesuiv(shadertype, count, indices)

def glRectdv(v1, v2):
	return lib.glRectdv(v1, v2)

def glColorP3uiv(type, color):
	return lib.glColorP3uiv(type, color)

def glFogCoordfv(coord):
	return lib.glFogCoordfv(coord)

def glCompileShader(shader):
	return lib.glCompileShader(shader)

def glIndexfv(c):
	return lib.glIndexfv(c)

def glMultiTexCoordP3ui(texture, type, coords):
	return lib.glMultiTexCoordP3ui(texture, type, coords)

def glNormal3sv(v):
	return lib.glNormal3sv(v)

def glInvalidateFramebuffer(target, numAttachments, attachments):
	return lib.glInvalidateFramebuffer(target, numAttachments, attachments)

def glCompressedTexImage2D(target, level, internalformat, width, height, border, imageSize):
	data = ffi.new('const void *')
	return lib.glCompressedTexImage2D(target, level, internalformat, width, height, border, imageSize, data)

def glVertexAttrib1f(index, x):
	return lib.glVertexAttrib1f(index, x)

def glVertex4fv(v):
	return lib.glVertex4fv(v)

def glClearNamedFramebufferfi(framebuffer, buffer, drawbuffer, depth, stencil):
	return lib.glClearNamedFramebufferfi(framebuffer, buffer, drawbuffer, depth, stencil)

def glGetQueryBufferObjectuiv(id, buffer, pname, offset):
	return lib.glGetQueryBufferObjectuiv(id, buffer, pname, offset)

def glClearNamedFramebufferfv(framebuffer, buffer, drawbuffer, value):
	return lib.glClearNamedFramebufferfv(framebuffer, buffer, drawbuffer, value)

def glVertexAttrib1s(index, x):
	return lib.glVertexAttrib1s(index, x)

def glMultiTexCoord1sv(target, v):
	return lib.glMultiTexCoord1sv(target, v)

def glDeleteProgram(program):
	return lib.glDeleteProgram(program)

def glColor4bv(v):
	return lib.glColor4bv(v)

def glRasterPos2f(x, y):
	return lib.glRasterPos2f(x, y)

def glLoadIdentity():
	return lib.glLoadIdentity()

def glRasterPos4iv(v):
	return lib.glRasterPos4iv(v)

def glUniformMatrix4x3fv(location, count, transpose, value):
	return lib.glUniformMatrix4x3fv(location, count, transpose, value)

def glClearBufferfv(buffer, drawbuffer, value):
	return lib.glClearBufferfv(buffer, drawbuffer, value)

def glTextureBarrier():
	return lib.glTextureBarrier()

def glClearBufferfi(buffer, drawbuffer, depth, stencil):
	return lib.glClearBufferfi(buffer, drawbuffer, depth, stencil)

def glDrawArraysIndirect(mode, indirect):
	return lib.glDrawArraysIndirect(mode, indirect)

def glGenVertexArrays(n, arrays):
	return lib.glGenVertexArrays(n, arrays)

def glEnableVertexArrayAttrib(vaobj, index):
	return lib.glEnableVertexArrayAttrib(vaobj, index)

def glProgramUniformMatrix3x2dv(program, location, count, transpose, value):
	return lib.glProgramUniformMatrix3x2dv(program, location, count, transpose, value)

def glVertexBindingDivisor(bindingindex, divisor):
	return lib.glVertexBindingDivisor(bindingindex, divisor)

def glGetSamplerParameterIiv(sampler, pname):
	params = ffi.new('GLint *')
	return lib.glGetSamplerParameterIiv(sampler, pname, params)

def glUniformMatrix4x2fv(location, count, transpose, value):
	return lib.glUniformMatrix4x2fv(location, count, transpose, value)

def glVertexAttrib3f(index, x, y, z):
	return lib.glVertexAttrib3f(index, x, y, z)

def glGetQueryBufferObjecti64v(id, buffer, pname, offset):
	return lib.glGetQueryBufferObjecti64v(id, buffer, pname, offset)

def glGetVertexAttribdv(index, pname):
	params = ffi.new('GLdouble *')
	return lib.glGetVertexAttribdv(index, pname, params)

def glUniform1ui(location, v0):
	return lib.glUniform1ui(location, v0)

def glBlitNamedFramebuffer(readFramebuffer, drawFramebuffer, srcX0, srcY0, srcX1, srcY1, dstX0, dstY0, dstX1, dstY1, mask, filter):
	return lib.glBlitNamedFramebuffer(readFramebuffer, drawFramebuffer, srcX0, srcY0, srcX1, srcY1, dstX0, dstY0, dstX1, dstY1, mask, filter)

def glVertexAttrib3d(index, x, y, z):
	return lib.glVertexAttrib3d(index, x, y, z)

def glMemoryBarrier(barriers):
	return lib.glMemoryBarrier(barriers)

def glGetFragDataLocation(program):
	name = ffi.new('const GLchar *')
	return lib.glGetFragDataLocation(program, name)

def glGetMaterialfv(face, pname):
	params = ffi.new('GLfloat *')
	return lib.glGetMaterialfv(face, pname, params)

def glPixelMapuiv(map, mapsize):
	values = ffi.new('const GLuint *')
	return lib.glPixelMapuiv(map, mapsize, values)

def glClearTexSubImage(texture, level, xoffset, yoffset, zoffset, width, height, depth, format, type):
	data = ffi.new('const void *')
	return lib.glClearTexSubImage(texture, level, xoffset, yoffset, zoffset, width, height, depth, format, type, data)

def glGetTextureParameterIiv(texture, pname):
	params = ffi.new('GLint *')
	return lib.glGetTextureParameterIiv(texture, pname, params)

def glVertexAttribI4ubv(index, v):
	return lib.glVertexAttribI4ubv(index, v)

def glProgramUniformMatrix4x2dv(program, location, count, transpose, value):
	return lib.glProgramUniformMatrix4x2dv(program, location, count, transpose, value)

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

def glVertexAttrib4dv(index, v):
	return lib.glVertexAttrib4dv(index, v)

def glGetTextureParameteriv(texture, pname):
	params = ffi.new('GLint *')
	return lib.glGetTextureParameteriv(texture, pname, params)

def glProgramUniform3ui(program, location, v0, v1, v2):
	return lib.glProgramUniform3ui(program, location, v0, v1, v2)

def glProgramUniformMatrix2x3fv(program, location, count, transpose, value):
	return lib.glProgramUniformMatrix2x3fv(program, location, count, transpose, value)

def glPushMatrix():
	return lib.glPushMatrix()

def glProgramUniform1i(program, location, v0):
	return lib.glProgramUniform1i(program, location, v0)

def glProgramUniform1d(program, location, v0):
	return lib.glProgramUniform1d(program, location, v0)

def glProgramUniform1f(program, location, v0):
	return lib.glProgramUniform1f(program, location, v0)

def glProgramUniform3iv(program, location, count, value):
	return lib.glProgramUniform3iv(program, location, count, value)

def glIndexiv(c):
	return lib.glIndexiv(c)

def glTransformFeedbackBufferRange(xfb, index, buffer, offset, size):
	return lib.glTransformFeedbackBufferRange(xfb, index, buffer, offset, size)

def glPixelZoom(xfactor, yfactor):
	return lib.glPixelZoom(xfactor, yfactor)

def glColorP3ui(type, color):
	return lib.glColorP3ui(type, color)

def glMultiTexCoordP4uiv(texture, type, coords):
	return lib.glMultiTexCoordP4uiv(texture, type, coords)

def glTextureView(texture, target, origtexture, internalformat, minlevel, numlevels, minlayer, numlayers):
	return lib.glTextureView(texture, target, origtexture, internalformat, minlevel, numlevels, minlayer, numlayers)

def glDisableVertexArrayAttrib(vaobj, index):
	return lib.glDisableVertexArrayAttrib(vaobj, index)

def glUniform4iv(location, count, value):
	return lib.glUniform4iv(location, count, value)

def glGenTextures(n, textures):
	return lib.glGenTextures(n, textures)

def glTextureStorage2DMultisample(texture, samples, internalformat, width, height, fixedsamplelocations):
	return lib.glTextureStorage2DMultisample(texture, samples, internalformat, width, height, fixedsamplelocations)

def glMultiTexCoord1s(target, s):
	return lib.glMultiTexCoord1s(target, s)

def glVertexAttribPointer(index, size, type, normalized, stride, pointer):
	return lib.glVertexAttribPointer(index, size, type, normalized, stride, pointer)

def glUniform1f(location, v0):
	return lib.glUniform1f(location, v0)

def glVertexAttribP1ui(index, type, normalized, value):
	return lib.glVertexAttribP1ui(index, type, normalized, value)

def glMultiTexCoord4sv(target, v):
	return lib.glMultiTexCoord4sv(target, v)

def glProgramUniformMatrix3x4dv(program, location, count, transpose, value):
	return lib.glProgramUniformMatrix3x4dv(program, location, count, transpose, value)

def glGetTextureSubImage(texture, level, xoffset, yoffset, zoffset, width, height, depth, format, type, bufSize):
	pixels = ffi.new('void *')
	return lib.glGetTextureSubImage(texture, level, xoffset, yoffset, zoffset, width, height, depth, format, type, bufSize, pixels)

def glGetNamedRenderbufferParameteriv(renderbuffer, pname):
	params = ffi.new('GLint *')
	return lib.glGetNamedRenderbufferParameteriv(renderbuffer, pname, params)

def glBindBuffersRange(target, first, count, buffers, offsets, sizes):
	return lib.glBindBuffersRange(target, first, count, buffers, offsets, sizes)

def glBindFragDataLocationIndexed(program, colorNumber, index):
	name = ffi.new('const GLchar *')
	return lib.glBindFragDataLocationIndexed(program, colorNumber, index, name)

def glMultiTexCoord2dv(target, v):
	return lib.glMultiTexCoord2dv(target, v)

def glUniform2iv(location, count, value):
	return lib.glUniform2iv(location, count, value)

def glTextureParameterf(texture, pname, param):
	return lib.glTextureParameterf(texture, pname, param)

def glFeedbackBuffer(size, type, buffer):
	return lib.glFeedbackBuffer(size, type, buffer)

def glMultiTexCoord2i(target, s, t):
	return lib.glMultiTexCoord2i(target, s, t)

def glTextureSubImage3D(texture, level, xoffset, yoffset, zoffset, width, height, depth, format, type):
	pixels = ffi.new('const void *')
	return lib.glTextureSubImage3D(texture, level, xoffset, yoffset, zoffset, width, height, depth, format, type, pixels)

def glFramebufferTexture1D(target, attachment, textarget, texture, level):
	return lib.glFramebufferTexture1D(target, attachment, textarget, texture, level)

def glGetShaderiv(shader, pname):
	params = ffi.new('GLint *')
	return lib.glGetShaderiv(shader, pname, params)

def glMultiTexCoord2d(target, s, t):
	return lib.glMultiTexCoord2d(target, s, t)

def glNamedBufferStorage(buffer, size, flags):
	data = ffi.new('const void *')
	return lib.glNamedBufferStorage(buffer, size, data, flags)

def glUniform1dv(location, count, value):
	return lib.glUniform1dv(location, count, value)

def glMultiTexCoord4fv(target, v):
	return lib.glMultiTexCoord4fv(target, v)

def glRasterPos3i(x, y, z):
	return lib.glRasterPos3i(x, y, z)

def glRasterPos3d(x, y, z):
	return lib.glRasterPos3d(x, y, z)

def glRasterPos3f(x, y, z):
	return lib.glRasterPos3f(x, y, z)

def glCompressedTexImage3D(target, level, internalformat, width, height, depth, border, imageSize):
	data = ffi.new('const void *')
	return lib.glCompressedTexImage3D(target, level, internalformat, width, height, depth, border, imageSize, data)

def glGetVertexAttribiv(index, pname):
	params = ffi.new('GLint *')
	return lib.glGetVertexAttribiv(index, pname, params)

def glGetnHistogram(target, reset, format, type, bufSize):
	values = ffi.new('void *')
	return lib.glGetnHistogram(target, reset, format, type, bufSize, values)

def glUniformMatrix2fv(location, count, transpose, value):
	return lib.glUniformMatrix2fv(location, count, transpose, value)

def glGenerateTextureMipmap(texture):
	return lib.glGenerateTextureMipmap(texture)

def glMultiDrawElementsBaseVertex(mode, count, type, constindices, drawcount, basevertex):
	return lib.glMultiDrawElementsBaseVertex(mode, count, type, constindices, drawcount, basevertex)

def glWindowPos3sv(v):
	return lib.glWindowPos3sv(v)

def glCompressedTexSubImage1D(target, level, xoffset, width, format, imageSize):
	data = ffi.new('const void *')
	return lib.glCompressedTexSubImage1D(target, level, xoffset, width, format, imageSize, data)

def glGetTexParameterIiv(target, pname):
	params = ffi.new('GLint *')
	return lib.glGetTexParameterIiv(target, pname, params)

def glInvalidateTexImage(texture, level):
	return lib.glInvalidateTexImage(texture, level)

def glVertexP3uiv(type, value):
	return lib.glVertexP3uiv(type, value)

def glGetnMapdv(target, query, bufSize, v):
	return lib.glGetnMapdv(target, query, bufSize, v)

def glDebugMessageCallback(callback, userParam):
	return lib.glDebugMessageCallback(callback, userParam)

def glGetBooleani_v(target, index):
	data = ffi.new('GLboolean *')
	return lib.glGetBooleani_v(target, index, data)

def glTextureParameterIiv(texture, pname):
	params = ffi.new('const GLint *')
	return lib.glTextureParameterIiv(texture, pname, params)

def glNewList(list, mode):
	return lib.glNewList(list, mode)

def glHint(target, mode):
	return lib.glHint(target, mode)

def glMultiDrawArraysIndirect(mode, indirect, drawcount, stride):
	return lib.glMultiDrawArraysIndirect(mode, indirect, drawcount, stride)

def glVertexAttribP2uiv(index, type, normalized, value):
	return lib.glVertexAttribP2uiv(index, type, normalized, value)

def glScalef(x, y, z):
	return lib.glScalef(x, y, z)

def glScaled(x, y, z):
	return lib.glScaled(x, y, z)

def glGetProgramResourceName(program, programInterface, index, bufSize, length):
	name = ffi.new('GLchar *')
	return lib.glGetProgramResourceName(program, programInterface, index, bufSize, length, name)

def glDepthRangeArrayv(first, count, v):
	return lib.glDepthRangeArrayv(first, count, v)

def glGetActiveAtomicCounterBufferiv(program, bufferIndex, pname):
	params = ffi.new('GLint *')
	return lib.glGetActiveAtomicCounterBufferiv(program, bufferIndex, pname, params)

def glStencilOpSeparate(face, sfail, dpfail, dppass):
	return lib.glStencilOpSeparate(face, sfail, dpfail, dppass)

def glVertexArrayAttribBinding(vaobj, attribindex, bindingindex):
	return lib.glVertexArrayAttribBinding(vaobj, attribindex, bindingindex)

def glTexCoord3f(s, t, r):
	return lib.glTexCoord3f(s, t, r)

def glVertexAttribI1i(index, x):
	return lib.glVertexAttribI1i(index, x)

def glGetTexParameteriv(target, pname):
	params = ffi.new('GLint *')
	return lib.glGetTexParameteriv(target, pname, params)

def glGetVertexAttribPointerv(index, pname, pointer):
	return lib.glGetVertexAttribPointerv(index, pname, pointer)

def glGetnCompressedTexImage(target, lod, bufSize):
	pixels = ffi.new('void *')
	return lib.glGetnCompressedTexImage(target, lod, bufSize, pixels)

def glWindowPos2dv(v):
	return lib.glWindowPos2dv(v)

def glDisable(cap):
	return lib.glDisable(cap)

def glProgramUniform4uiv(program, location, count, value):
	return lib.glProgramUniform4uiv(program, location, count, value)

def glCopyTextureSubImage2D(texture, level, xoffset, yoffset, x, y, width, height):
	return lib.glCopyTextureSubImage2D(texture, level, xoffset, yoffset, x, y, width, height)

def glVertexAttribI2uiv(index, v):
	return lib.glVertexAttribI2uiv(index, v)

def glGetLightfv(light, pname):
	params = ffi.new('GLfloat *')
	return lib.glGetLightfv(light, pname, params)

def glMultiTexCoord3s(target, s, t, r):
	return lib.glMultiTexCoord3s(target, s, t, r)

def glMultiTexCoord3i(target, s, t, r):
	return lib.glMultiTexCoord3i(target, s, t, r)

def glMultiTexCoord3f(target, s, t, r):
	return lib.glMultiTexCoord3f(target, s, t, r)

def glMultiTexCoord3d(target, s, t, r):
	return lib.glMultiTexCoord3d(target, s, t, r)

def glFogCoorddv(coord):
	return lib.glFogCoorddv(coord)

def glUniform3uiv(location, count, value):
	return lib.glUniform3uiv(location, count, value)

def glClearNamedBufferData(buffer, internalformat, format, type):
	data = ffi.new('const void *')
	return lib.glClearNamedBufferData(buffer, internalformat, format, type, data)

def glFlushMappedNamedBufferRange(buffer, offset, length):
	return lib.glFlushMappedNamedBufferRange(buffer, offset, length)

def glPushName():
	name = ffi.new('GLuint *')
	return lib.glPushName(name)

def glGetClipPlane(plane, equation):
	return lib.glGetClipPlane(plane, equation)

def glRasterPos4i(x, y, z, w):
	return lib.glRasterPos4i(x, y, z, w)

def glBlendColor(red, green, blue, alpha):
	return lib.glBlendColor(red, green, blue, alpha)

def glSamplerParameterIuiv(sampler, pname, param):
	return lib.glSamplerParameterIuiv(sampler, pname, param)

def glIndexubv(c):
	return lib.glIndexubv(c)

def glCheckNamedFramebufferStatus(framebuffer, target):
	return lib.glCheckNamedFramebufferStatus(framebuffer, target)

def glRasterPos4d(x, y, z, w):
	return lib.glRasterPos4d(x, y, z, w)

def glRasterPos4f(x, y, z, w):
	return lib.glRasterPos4f(x, y, z, w)

def glVertexAttrib3s(index, x, y, z):
	return lib.glVertexAttrib3s(index, x, y, z)

def glRasterPos4s(x, y, z, w):
	return lib.glRasterPos4s(x, y, z, w)

def glGetProgramStageiv(program, shadertype, pname):
	values = ffi.new('GLint *')
	return lib.glGetProgramStageiv(program, shadertype, pname, values)

def glPopMatrix():
	return lib.glPopMatrix()

def glVertex4s(x, y, z, w):
	return lib.glVertex4s(x, y, z, w)

def glUniform4i(location, v0, v1, v2, v3):
	return lib.glUniform4i(location, v0, v1, v2, v3)

def glActiveTexture(texture):
	return lib.glActiveTexture(texture)

def glEnableVertexAttribArray(index):
	return lib.glEnableVertexAttribArray(index)

def glUniform4d(location, x, y, z, w):
	return lib.glUniform4d(location, x, y, z, w)

def glUniform4f(location, v0, v1, v2, v3):
	return lib.glUniform4f(location, v0, v1, v2, v3)

def glRenderbufferStorageMultisample(target, samples, internalformat, width, height):
	return lib.glRenderbufferStorageMultisample(target, samples, internalformat, width, height)

def glCreateProgramPipelines(n, pipelines):
	return lib.glCreateProgramPipelines(n, pipelines)

def glVertexAttribLPointer(index, size, type, stride, pointer):
	return lib.glVertexAttribLPointer(index, size, type, stride, pointer)

def glMultiTexCoord3sv(target, v):
	return lib.glMultiTexCoord3sv(target, v)

def glDrawElementsInstancedBaseVertex(mode, count, type, indices, instancecount, basevertex):
	return lib.glDrawElementsInstancedBaseVertex(mode, count, type, indices, instancecount, basevertex)

def glGetActiveSubroutineName(program, shadertype, index, bufsize, length):
	name = ffi.new('GLchar *')
	return lib.glGetActiveSubroutineName(program, shadertype, index, bufsize, length, name)

def glMultiTexCoord4iv(target, v):
	return lib.glMultiTexCoord4iv(target, v)

def glTexEnvfv(target, pname):
	params = ffi.new('const GLfloat *')
	return lib.glTexEnvfv(target, pname, params)

def glPopDebugGroup():
	return lib.glPopDebugGroup()

def glUniformBlockBinding(program, uniformBlockIndex, uniformBlockBinding):
	return lib.glUniformBlockBinding(program, uniformBlockIndex, uniformBlockBinding)

def glBufferSubData(target, offset, size):
	data = ffi.new('const void *')
	return lib.glBufferSubData(target, offset, size, data)

def glTexCoordPointer(size, type, stride, pointer):
	return lib.glTexCoordPointer(size, type, stride, pointer)

def glProgramUniformMatrix3x2fv(program, location, count, transpose, value):
	return lib.glProgramUniformMatrix3x2fv(program, location, count, transpose, value)

def glGetQueryIndexediv(target, index, pname):
	params = ffi.new('GLint *')
	return lib.glGetQueryIndexediv(target, index, pname, params)

def glTexEnviv(target, pname):
	params = ffi.new('const GLint *')
	return lib.glTexEnviv(target, pname, params)

def glBlendFunc(sfactor, dfactor):
	return lib.glBlendFunc(sfactor, dfactor)

def glCreateProgram():
	return lib.glCreateProgram()

def glPrimitiveRestartIndex(index):
	return lib.glPrimitiveRestartIndex(index)

def glProgramUniformMatrix2fv(program, location, count, transpose, value):
	return lib.glProgramUniformMatrix2fv(program, location, count, transpose, value)

def glBindImageTextures(first, count, textures):
	return lib.glBindImageTextures(first, count, textures)

def glEnd():
	return lib.glEnd()

def glSamplerParameteriv(sampler, pname, param):
	return lib.glSamplerParameteriv(sampler, pname, param)

def glSecondaryColor3iv(v):
	return lib.glSecondaryColor3iv(v)

def glMultTransposeMatrixd(m):
	return lib.glMultTransposeMatrixd(m)

def glClearColor(red, green, blue, alpha):
	return lib.glClearColor(red, green, blue, alpha)

def glPushClientAttrib(mask):
	return lib.glPushClientAttrib(mask)

def glGetnUniformiv(program, location, bufSize):
	params = ffi.new('GLint *')
	return lib.glGetnUniformiv(program, location, bufSize, params)

def glStencilMask(mask):
	return lib.glStencilMask(mask)

def glSecondaryColor3us(red, green, blue):
	return lib.glSecondaryColor3us(red, green, blue)

def glVertexAttribI4uiv(index, v):
	return lib.glVertexAttribI4uiv(index, v)

def glVertexAttrib4bv(index, v):
	return lib.glVertexAttrib4bv(index, v)

def glGetProgramResourceIndex(program, programInterface):
	name = ffi.new('const GLchar *')
	return lib.glGetProgramResourceIndex(program, programInterface, name)

def glSecondaryColor3ub(red, green, blue):
	return lib.glSecondaryColor3ub(red, green, blue)

def glSecondaryColor3ui(red, green, blue):
	return lib.glSecondaryColor3ui(red, green, blue)

def glGetNamedBufferPointerv(buffer, pname):
	params = ffi.new('void *')
	return lib.glGetNamedBufferPointerv(buffer, pname, params)

def glGetQueryBufferObjectui64v(id, buffer, pname, offset):
	return lib.glGetQueryBufferObjectui64v(id, buffer, pname, offset)

def glNormal3f(nx, ny, nz):
	return lib.glNormal3f(nx, ny, nz)

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

def glVertexAttribI4bv(index, v):
	return lib.glVertexAttribI4bv(index, v)

def glGetTexParameterfv(target, pname):
	params = ffi.new('GLfloat *')
	return lib.glGetTexParameterfv(target, pname, params)

def glGetVertexArrayIndexed64iv(vaobj, index, pname, param):
	return lib.glGetVertexArrayIndexed64iv(vaobj, index, pname, param)

def glTexParameterIiv(target, pname):
	params = ffi.new('const GLint *')
	return lib.glTexParameterIiv(target, pname, params)

def glVertexArrayAttribFormat(vaobj, attribindex, size, type, normalized, relativeoffset):
	return lib.glVertexArrayAttribFormat(vaobj, attribindex, size, type, normalized, relativeoffset)

def glEndTransformFeedback():
	return lib.glEndTransformFeedback()

def glTexImage2DMultisample(target, samples, internalformat, width, height, fixedsamplelocations):
	return lib.glTexImage2DMultisample(target, samples, internalformat, width, height, fixedsamplelocations)

def glVertexAttribI1iv(index, v):
	return lib.glVertexAttribI1iv(index, v)

def glVertexAttribDivisor(index, divisor):
	return lib.glVertexAttribDivisor(index, divisor)

def glGetCompressedTextureImage(texture, level, bufSize):
	pixels = ffi.new('void *')
	return lib.glGetCompressedTextureImage(texture, level, bufSize, pixels)

def glGenLists(range):
	return lib.glGenLists(range)

def glMapBufferRange(target, offset, length, access):
	return lib.glMapBufferRange(target, offset, length, access)

def glProgramUniformMatrix4x2fv(program, location, count, transpose, value):
	return lib.glProgramUniformMatrix4x2fv(program, location, count, transpose, value)

def glEndList():
	return lib.glEndList()

def glUniformMatrix3x2dv(location, count, transpose, value):
	return lib.glUniformMatrix3x2dv(location, count, transpose, value)

def glGetShaderPrecisionFormat(shadertype, precisiontype, range, precision):
	return lib.glGetShaderPrecisionFormat(shadertype, precisiontype, range, precision)

def glIndexMask(mask):
	return lib.glIndexMask(mask)

def glShaderSource(shader, count, conststring, length):
	return lib.glShaderSource(shader, count, conststring, length)

def glDeleteRenderbuffers(n, renderbuffers):
	return lib.glDeleteRenderbuffers(n, renderbuffers)

def glTexCoordP2uiv(type, coords):
	return lib.glTexCoordP2uiv(type, coords)

def glMapGrid2d(un, u1, u2, vn, v1, v2):
	return lib.glMapGrid2d(un, u1, u2, vn, v1, v2)

def glGetNamedBufferParameteri64v(buffer, pname):
	params = ffi.new('GLint64 *')
	return lib.glGetNamedBufferParameteri64v(buffer, pname, params)

def glVertex4d(x, y, z, w):
	return lib.glVertex4d(x, y, z, w)

def glBufferData(target, size, usage):
	data = ffi.new('const void *')
	return lib.glBufferData(target, size, data, usage)

def glVertex4f(x, y, z, w):
	return lib.glVertex4f(x, y, z, w)

def glTexCoordP1ui(type, coords):
	return lib.glTexCoordP1ui(type, coords)

def glCopyTextureSubImage3D(texture, level, xoffset, yoffset, zoffset, x, y, width, height):
	return lib.glCopyTextureSubImage3D(texture, level, xoffset, yoffset, zoffset, x, y, width, height)

def glMultiTexCoord2fv(target, v):
	return lib.glMultiTexCoord2fv(target, v)

def glNormalP3ui(type, coords):
	return lib.glNormalP3ui(type, coords)

def glColorPointer(size, type, stride, pointer):
	return lib.glColorPointer(size, type, stride, pointer)

def glFramebufferTexture2D(target, attachment, textarget, texture, level):
	return lib.glFramebufferTexture2D(target, attachment, textarget, texture, level)

def glGetBufferPointerv(target, pname):
	params = ffi.new('void *')
	return lib.glGetBufferPointerv(target, pname, params)

def glFramebufferTexture3D(target, attachment, textarget, texture, level, zoffset):
	return lib.glFramebufferTexture3D(target, attachment, textarget, texture, level, zoffset)

def glWindowPos3dv(v):
	return lib.glWindowPos3dv(v)

def glSamplerParameterfv(sampler, pname, param):
	return lib.glSamplerParameterfv(sampler, pname, param)

def glNormal3bv(v):
	return lib.glNormal3bv(v)

def glGetMaterialiv(face, pname):
	params = ffi.new('GLint *')
	return lib.glGetMaterialiv(face, pname, params)

def glUniform1fv(location, count, value):
	return lib.glUniform1fv(location, count, value)

def glScissorIndexedv(index, v):
	return lib.glScissorIndexedv(index, v)

def glNormal3s(nx, ny, nz):
	return lib.glNormal3s(nx, ny, nz)

def glGetnPixelMapuiv(map, bufSize):
	values = ffi.new('GLuint *')
	return lib.glGetnPixelMapuiv(map, bufSize, values)

def glNormal3i(nx, ny, nz):
	return lib.glNormal3i(nx, ny, nz)

def glNormal3d(nx, ny, nz):
	return lib.glNormal3d(nx, ny, nz)

def glNormal3b(nx, ny, nz):
	return lib.glNormal3b(nx, ny, nz)

def glMultiTexCoord4dv(target, v):
	return lib.glMultiTexCoord4dv(target, v)

def glVertexAttrib2d(index, x, y):
	return lib.glVertexAttrib2d(index, x, y)

def glVertexAttrib2f(index, x, y):
	return lib.glVertexAttrib2f(index, x, y)

def glVertexAttrib2s(index, x, y):
	return lib.glVertexAttrib2s(index, x, y)

def glTexImage3DMultisample(target, samples, internalformat, width, height, depth, fixedsamplelocations):
	return lib.glTexImage3DMultisample(target, samples, internalformat, width, height, depth, fixedsamplelocations)

def glGetUniformBlockIndex(program, uniformBlockName):
	return lib.glGetUniformBlockIndex(program, uniformBlockName)

def glFrontFace(mode):
	return lib.glFrontFace(mode)

def glDrawArraysInstancedBaseInstance(mode, first, count, instancecount, baseinstance):
	return lib.glDrawArraysInstancedBaseInstance(mode, first, count, instancecount, baseinstance)

