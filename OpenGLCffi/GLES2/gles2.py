@params('face', 'mask')
def glStencilMaskSeparate(face, mask):
	pass


@params('buffer',)
def glIsBuffer(buffer):
	pass


@params('target', 'internalformat', 'width', 'height')
def glRenderbufferStorage(target, internalformat, width, height):
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


@params('program', 'location', 'params')
def glGetUniformfv(program, location):
	pass


@params('target', 'pname', 'params')
def glGetRenderbufferParameteriv(target, pname):
	pass


@params('target', 'level', 'internalformat', 'x', 'y', 'width', 'height', 'border')
def glCopyTexImage2D(target, level, internalformat, x, y, width, height, border):
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


@params('target', 'pname', 'param')
def glTexParameterf(target, pname, param):
	pass


@params('target', 'pname', 'param')
def glTexParameteri(target, pname, param):
	pass


@params('shader', 'bufSize', 'length', 'source')
def glGetShaderSource(shader, bufSize, length, source):
	pass


@params('index', 'v')
def glVertexAttrib3fv(index, v):
	pass


@params('program',)
def glLinkProgram(program):
	pass


@params('name',)
def glGetString():
	pass


@params('n', 'textures')
def glDeleteTextures(n, textures):
	pass


@params('index', 'x', 'y', 'z', 'w')
def glVertexAttrib4f(index, x, y, z, w):
	pass


@params('location', 'v0')
def glUniform1i(location, v0):
	pass


@params('mode',)
def glCullFace(mode):
	pass


@params('program', 'shader')
def glAttachShader(program, shader):
	pass


@params('target', 'pname', 'params')
def glGetBufferParameteriv(target, pname):
	pass


@params('location', 'count', 'transpose', 'value')
def glUniformMatrix3fv(location, count, transpose, value):
	pass


@params('func', 'ref', 'mask')
def glStencilFunc(func, ref, mask):
	pass


@params('shader', 'bufSize', 'length', 'infoLog')
def glGetShaderInfoLog(shader, bufSize, length, infoLog):
	pass


@params('modeRGB', 'modeAlpha')
def glBlendEquationSeparate(modeRGB, modeAlpha):
	pass


@params('n', 'buffers')
def glDeleteBuffers(n, buffers):
	pass


@params('x', 'y', 'width', 'height')
def glScissor(x, y, width, height):
	pass


@params('location', 'count', 'value')
def glUniform2fv(location, count, value):
	pass


@params('target',)
def glCheckFramebufferStatus(target):
	pass


@params()
def glGetError():
	pass


@params('pname', 'param')
def glPixelStorei(pname, param):
	pass


@params('flag',)
def glDepthMask(flag):
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


@params('location', 'v0', 'v1', 'v2')
def glUniform3f(location, v0, v1, v2):
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


@params('index',)
def glDisableVertexAttribArray(index):
	pass


@params('value', 'invert')
def glSampleCoverage(value, invert):
	pass


@params('location', 'v0', 'v1')
def glUniform2i(location, v0, v1):
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


@params('program',)
def glValidateProgram(program):
	pass


@params('target', 'texture')
def glBindTexture(target, texture):
	pass


@params('program', 'shader')
def glDetachShader(program, shader):
	pass


@params('program', 'location', 'params')
def glGetUniformiv(program, location):
	pass


@params('target', 'buffer')
def glBindBuffer(target, buffer):
	pass


@params('target',)
def glGenerateMipmap(target):
	pass


@params()
def glReleaseShaderCompiler():
	pass


@params('x', 'y', 'width', 'height', 'format', 'type', 'pixels')
def glReadPixels(x, y, width, height, format, type):
	pass


@params('n', 'buffers')
def glGenBuffers(n, buffers):
	pass


@params('framebuffer',)
def glIsFramebuffer(framebuffer):
	pass


@params('func',)
def glDepthFunc(func):
	pass


@params('program', 'name')
def glGetUniformLocation(program):
	pass


@params('location', 'count', 'value')
def glUniform4fv(location, count, value):
	pass


@params('pname', 'data')
def glGetFloatv(pname):
	pass


@params('pname', 'data')
def glGetIntegerv(pname):
	pass


@params('target', 'level', 'internalformat', 'width', 'height', 'border', 'format', 'type', 'pixels')
def glTexImage2D(target, level, internalformat, width, height, border, format, type):
	pass


@params('program', 'index', 'bufSize', 'length', 'size', 'type', 'name')
def glGetActiveUniform(program, index, bufSize, length, size, type):
	pass


@params('target', 'attachment', 'renderbuffertarget', 'renderbuffer')
def glFramebufferRenderbuffer(target, attachment, renderbuffertarget, renderbuffer):
	pass


@params('width',)
def glLineWidth(width):
	pass


@params('n', 'f')
def glDepthRangef(n, f):
	pass


@params('target', 'attachment', 'pname', 'params')
def glGetFramebufferAttachmentParameteriv(target, attachment, pname):
	pass


@params('target', 'pname', 'params')
def glTexParameteriv(target, pname):
	pass


@params()
def glFlush():
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


@params('program', 'pname', 'params')
def glGetProgramiv(program, pname):
	pass


@params('location', 'count', 'value')
def glUniform3fv(location, count, value):
	pass


@params()
def glFinish():
	pass


@params('index', 'pname', 'params')
def glGetVertexAttribfv(index, pname):
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


@params('count', 'shaders', 'binaryformat', 'binary', 'length')
def glShaderBinary(count, shaders, binaryformat, binary, length):
	pass


@params('mode', 'count', 'type', 'indices')
def glDrawElements(mode, count, type, indices):
	pass


@params('location', 'count', 'value')
def glUniform1iv(location, count, value):
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


@params('location', 'v0', 'v1')
def glUniform2f(location, v0, v1):
	pass


@params('d',)
def glClearDepthf(d):
	pass


@params('red', 'green', 'blue', 'alpha')
def glColorMask(red, green, blue, alpha):
	pass


@params('mode',)
def glBlendEquation(mode):
	pass


@params('program', 'index', 'name')
def glBindAttribLocation(program, index):
	pass


@params('target', 'pname', 'params')
def glTexParameterfv(target, pname):
	pass


@params('face', 'func', 'ref', 'mask')
def glStencilFuncSeparate(face, func, ref, mask):
	pass


@params('location', 'count', 'transpose', 'value')
def glUniformMatrix4fv(location, count, transpose, value):
	pass


@params('shader',)
def glCompileShader(shader):
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


@params('index', 'x', 'y', 'z')
def glVertexAttrib3f(index, x, y, z):
	pass


@params('shader',)
def glIsShader(shader):
	pass


@params('cap',)
def glEnable(cap):
	pass


@params('program', 'name')
def glGetAttribLocation(program):
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


@params('index', 'pname', 'params')
def glGetVertexAttribiv(index, pname):
	pass


@params('location', 'count', 'transpose', 'value')
def glUniformMatrix2fv(location, count, transpose, value):
	pass


@params('target', 'mode')
def glHint(target, mode):
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


@params('red', 'green', 'blue', 'alpha')
def glBlendColor(red, green, blue, alpha):
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


@params('target', 'offset', 'size', 'data')
def glBufferSubData(target, offset, size):
	pass


@params('sfactor', 'dfactor')
def glBlendFunc(sfactor, dfactor):
	pass


@params()
def glCreateProgram():
	pass


@params('red', 'green', 'blue', 'alpha')
def glClearColor(red, green, blue, alpha):
	pass


@params('mask',)
def glStencilMask(mask):
	pass


@params('target', 'level', 'xoffset', 'yoffset', 'width', 'height', 'format', 'imageSize', 'data')
def glCompressedTexSubImage2D(target, level, xoffset, yoffset, width, height, format, imageSize):
	pass


@params('target', 'pname', 'params')
def glGetTexParameterfv(target, pname):
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


@params('location', 'count', 'value')
def glUniform1fv(location, count, value):
	pass


@params('index', 'x', 'y')
def glVertexAttrib2f(index, x, y):
	pass


@params('mode',)
def glFrontFace(mode):
	pass


