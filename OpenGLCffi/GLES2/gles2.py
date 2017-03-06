def glStencilMaskSeparate(face, mask):
	return lib.glStencilMaskSeparate(face, mask)

def glIsBuffer(buffer):
	return lib.glIsBuffer(buffer)

def glRenderbufferStorage(target, internalformat, width, height):
	return lib.glRenderbufferStorage(target, internalformat, width, height)

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

def glGetUniformfv(program, location):
	params = ffi.new('GLfloat *')
	return lib.glGetUniformfv(program, location, params)

def glGetRenderbufferParameteriv(target, pname):
	params = ffi.new('GLint *')
	return lib.glGetRenderbufferParameteriv(target, pname, params)

def glCopyTexImage2D(target, level, internalformat, x, y, width, height, border):
	return lib.glCopyTexImage2D(target, level, internalformat, x, y, width, height, border)

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

def glTexParameterf(target, pname, param):
	return lib.glTexParameterf(target, pname, param)

def glTexParameteri(target, pname, param):
	return lib.glTexParameteri(target, pname, param)

def glGetShaderSource(shader, bufSize, length, source):
	return lib.glGetShaderSource(shader, bufSize, length, source)

def glVertexAttrib3fv(index, v):
	return lib.glVertexAttrib3fv(index, v)

def glLinkProgram(program):
	return lib.glLinkProgram(program)

def glGetString():
	name = ffi.new('GLenum *')
	return lib.glGetString(name)

def glDeleteTextures(n, textures):
	return lib.glDeleteTextures(n, textures)

def glVertexAttrib4f(index, x, y, z, w):
	return lib.glVertexAttrib4f(index, x, y, z, w)

def glUniform1i(location, v0):
	return lib.glUniform1i(location, v0)

def glCullFace(mode):
	return lib.glCullFace(mode)

def glAttachShader(program, shader):
	return lib.glAttachShader(program, shader)

def glGetBufferParameteriv(target, pname):
	params = ffi.new('GLint *')
	return lib.glGetBufferParameteriv(target, pname, params)

def glUniformMatrix3fv(location, count, transpose, value):
	return lib.glUniformMatrix3fv(location, count, transpose, value)

def glStencilFunc(func, ref, mask):
	return lib.glStencilFunc(func, ref, mask)

def glGetShaderInfoLog(shader, bufSize, length, infoLog):
	return lib.glGetShaderInfoLog(shader, bufSize, length, infoLog)

def glBlendEquationSeparate(modeRGB, modeAlpha):
	return lib.glBlendEquationSeparate(modeRGB, modeAlpha)

def glDeleteBuffers(n, buffers):
	return lib.glDeleteBuffers(n, buffers)

def glScissor(x, y, width, height):
	return lib.glScissor(x, y, width, height)

def glUniform2fv(location, count, value):
	return lib.glUniform2fv(location, count, value)

def glCheckFramebufferStatus(target):
	return lib.glCheckFramebufferStatus(target)

def glGetError():
	return lib.glGetError()

def glPixelStorei(pname, param):
	return lib.glPixelStorei(pname, param)

def glDepthMask(flag):
	return lib.glDepthMask(flag)

def glCreateShader(type):
	return lib.glCreateShader(type)

def glGenRenderbuffers(n, renderbuffers):
	return lib.glGenRenderbuffers(n, renderbuffers)

def glCopyTexSubImage2D(target, level, xoffset, yoffset, x, y, width, height):
	return lib.glCopyTexSubImage2D(target, level, xoffset, yoffset, x, y, width, height)

def glBlendFuncSeparate(sfactorRGB, dfactorRGB, sfactorAlpha, dfactorAlpha):
	return lib.glBlendFuncSeparate(sfactorRGB, dfactorRGB, sfactorAlpha, dfactorAlpha)

def glUniform3f(location, v0, v1, v2):
	return lib.glUniform3f(location, v0, v1, v2)

def glDeleteFramebuffers(n, framebuffers):
	return lib.glDeleteFramebuffers(n, framebuffers)

def glDrawArrays(mode, first, count):
	return lib.glDrawArrays(mode, first, count)

def glClear(mask):
	return lib.glClear(mask)

def glDisableVertexAttribArray(index):
	return lib.glDisableVertexAttribArray(index)

def glSampleCoverage(value, invert):
	return lib.glSampleCoverage(value, invert)

def glUniform2i(location, v0, v1):
	return lib.glUniform2i(location, v0, v1)

def glBindFramebuffer(target, framebuffer):
	return lib.glBindFramebuffer(target, framebuffer)

def glViewport(x, y, width, height):
	return lib.glViewport(x, y, width, height)

def glIsRenderbuffer(renderbuffer):
	return lib.glIsRenderbuffer(renderbuffer)

def glValidateProgram(program):
	return lib.glValidateProgram(program)

def glBindTexture(target, texture):
	return lib.glBindTexture(target, texture)

def glDetachShader(program, shader):
	return lib.glDetachShader(program, shader)

def glGetUniformiv(program, location):
	params = ffi.new('GLint *')
	return lib.glGetUniformiv(program, location, params)

def glBindBuffer(target, buffer):
	return lib.glBindBuffer(target, buffer)

def glGenerateMipmap(target):
	return lib.glGenerateMipmap(target)

def glReleaseShaderCompiler():
	return lib.glReleaseShaderCompiler()

def glReadPixels(x, y, width, height, format, type):
	pixels = ffi.new('void *')
	return lib.glReadPixels(x, y, width, height, format, type, pixels)

def glGenBuffers(n, buffers):
	return lib.glGenBuffers(n, buffers)

def glIsFramebuffer(framebuffer):
	return lib.glIsFramebuffer(framebuffer)

def glDepthFunc(func):
	return lib.glDepthFunc(func)

def glGetUniformLocation(program):
	name = ffi.new('const GLchar *')
	return lib.glGetUniformLocation(program, name)

def glUniform4fv(location, count, value):
	return lib.glUniform4fv(location, count, value)

def glGetFloatv(pname):
	data = ffi.new('GLfloat *')
	return lib.glGetFloatv(pname, data)

def glGetIntegerv(pname):
	data = ffi.new('GLint *')
	return lib.glGetIntegerv(pname, data)

def glTexImage2D(target, level, internalformat, width, height, border, format, type):
	pixels = ffi.new('const void *')
	return lib.glTexImage2D(target, level, internalformat, width, height, border, format, type, pixels)

def glGetActiveUniform(program, index, bufSize, length, size, type):
	name = ffi.new('GLchar *')
	return lib.glGetActiveUniform(program, index, bufSize, length, size, type, name)

def glFramebufferRenderbuffer(target, attachment, renderbuffertarget, renderbuffer):
	return lib.glFramebufferRenderbuffer(target, attachment, renderbuffertarget, renderbuffer)

def glLineWidth(width):
	return lib.glLineWidth(width)

def glDepthRangef(n, f):
	return lib.glDepthRangef(n, f)

def glGetFramebufferAttachmentParameteriv(target, attachment, pname):
	params = ffi.new('GLint *')
	return lib.glGetFramebufferAttachmentParameteriv(target, attachment, pname, params)

def glTexParameteriv(target, pname):
	params = ffi.new('const GLint *')
	return lib.glTexParameteriv(target, pname, params)

def glFlush():
	return lib.glFlush()

def glClearStencil(s):
	return lib.glClearStencil(s)

def glIsTexture(texture):
	return lib.glIsTexture(texture)

def glPolygonOffset(factor, units):
	return lib.glPolygonOffset(factor, units)

def glGetProgramiv(program, pname):
	params = ffi.new('GLint *')
	return lib.glGetProgramiv(program, pname, params)

def glUniform3fv(location, count, value):
	return lib.glUniform3fv(location, count, value)

def glFinish():
	return lib.glFinish()

def glGetVertexAttribfv(index, pname):
	params = ffi.new('GLfloat *')
	return lib.glGetVertexAttribfv(index, pname, params)

def glGetActiveAttrib(program, index, bufSize, length, size, type):
	name = ffi.new('GLchar *')
	return lib.glGetActiveAttrib(program, index, bufSize, length, size, type, name)

def glUniform3i(location, v0, v1, v2):
	return lib.glUniform3i(location, v0, v1, v2)

def glTexSubImage2D(target, level, xoffset, yoffset, width, height, format, type):
	pixels = ffi.new('const void *')
	return lib.glTexSubImage2D(target, level, xoffset, yoffset, width, height, format, type, pixels)

def glShaderBinary(count, shaders, binaryformat, binary, length):
	return lib.glShaderBinary(count, shaders, binaryformat, binary, length)

def glDrawElements(mode, count, type, indices):
	return lib.glDrawElements(mode, count, type, indices)

def glUniform1iv(location, count, value):
	return lib.glUniform1iv(location, count, value)

def glBindRenderbuffer(target, renderbuffer):
	return lib.glBindRenderbuffer(target, renderbuffer)

def glIsProgram(program):
	return lib.glIsProgram(program)

def glVertexAttrib4fv(index, v):
	return lib.glVertexAttrib4fv(index, v)

def glVertexAttrib2fv(index, v):
	return lib.glVertexAttrib2fv(index, v)

def glUniform2f(location, v0, v1):
	return lib.glUniform2f(location, v0, v1)

def glClearDepthf(d):
	return lib.glClearDepthf(d)

def glColorMask(red, green, blue, alpha):
	return lib.glColorMask(red, green, blue, alpha)

def glBlendEquation(mode):
	return lib.glBlendEquation(mode)

def glBindAttribLocation(program, index):
	name = ffi.new('const GLchar *')
	return lib.glBindAttribLocation(program, index, name)

def glTexParameterfv(target, pname):
	params = ffi.new('const GLfloat *')
	return lib.glTexParameterfv(target, pname, params)

def glStencilFuncSeparate(face, func, ref, mask):
	return lib.glStencilFuncSeparate(face, func, ref, mask)

def glUniformMatrix4fv(location, count, transpose, value):
	return lib.glUniformMatrix4fv(location, count, transpose, value)

def glCompileShader(shader):
	return lib.glCompileShader(shader)

def glCompressedTexImage2D(target, level, internalformat, width, height, border, imageSize):
	data = ffi.new('const void *')
	return lib.glCompressedTexImage2D(target, level, internalformat, width, height, border, imageSize, data)

def glVertexAttrib1f(index, x):
	return lib.glVertexAttrib1f(index, x)

def glDeleteProgram(program):
	return lib.glDeleteProgram(program)

def glVertexAttrib3f(index, x, y, z):
	return lib.glVertexAttrib3f(index, x, y, z)

def glIsShader(shader):
	return lib.glIsShader(shader)

def glEnable(cap):
	return lib.glEnable(cap)

def glGetAttribLocation(program):
	name = ffi.new('const GLchar *')
	return lib.glGetAttribLocation(program, name)

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

def glGetVertexAttribiv(index, pname):
	params = ffi.new('GLint *')
	return lib.glGetVertexAttribiv(index, pname, params)

def glUniformMatrix2fv(location, count, transpose, value):
	return lib.glUniformMatrix2fv(location, count, transpose, value)

def glHint(target, mode):
	return lib.glHint(target, mode)

def glStencilOpSeparate(face, sfail, dpfail, dppass):
	return lib.glStencilOpSeparate(face, sfail, dpfail, dppass)

def glGetTexParameteriv(target, pname):
	params = ffi.new('GLint *')
	return lib.glGetTexParameteriv(target, pname, params)

def glGetVertexAttribPointerv(index, pname, pointer):
	return lib.glGetVertexAttribPointerv(index, pname, pointer)

def glDisable(cap):
	return lib.glDisable(cap)

def glBlendColor(red, green, blue, alpha):
	return lib.glBlendColor(red, green, blue, alpha)

def glUniform4i(location, v0, v1, v2, v3):
	return lib.glUniform4i(location, v0, v1, v2, v3)

def glActiveTexture(texture):
	return lib.glActiveTexture(texture)

def glEnableVertexAttribArray(index):
	return lib.glEnableVertexAttribArray(index)

def glUniform4f(location, v0, v1, v2, v3):
	return lib.glUniform4f(location, v0, v1, v2, v3)

def glBufferSubData(target, offset, size):
	data = ffi.new('const void *')
	return lib.glBufferSubData(target, offset, size, data)

def glBlendFunc(sfactor, dfactor):
	return lib.glBlendFunc(sfactor, dfactor)

def glCreateProgram():
	return lib.glCreateProgram()

def glClearColor(red, green, blue, alpha):
	return lib.glClearColor(red, green, blue, alpha)

def glStencilMask(mask):
	return lib.glStencilMask(mask)

def glCompressedTexSubImage2D(target, level, xoffset, yoffset, width, height, format, imageSize):
	data = ffi.new('const void *')
	return lib.glCompressedTexSubImage2D(target, level, xoffset, yoffset, width, height, format, imageSize, data)

def glGetTexParameterfv(target, pname):
	params = ffi.new('GLfloat *')
	return lib.glGetTexParameterfv(target, pname, params)

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

def glUniform1fv(location, count, value):
	return lib.glUniform1fv(location, count, value)

def glVertexAttrib2f(index, x, y):
	return lib.glVertexAttrib2f(index, x, y)

def glFrontFace(mode):
	return lib.glFrontFace(mode)

