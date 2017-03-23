from OpenGLCffi.GLES2 import params
@params('face', 'mask', api='gles2')
def glStencilMaskSeparate(face, mask):
	pass


@params('buffer', api='gles2')
def glIsBuffer(buffer):
	pass


@params('target', 'internalformat', 'width', 'height', api='gles2')
def glRenderbufferStorage(target, internalformat, width, height):
	pass


@params('index', 'v', api='gles2')
def glVertexAttrib1fv(index, v):
	pass


@params('cap', api='gles2')
def glIsEnabled(cap):
	pass


@params('fail', 'zfail', 'zpass', api='gles2')
def glStencilOp(fail, zfail, zpass):
	pass


@params('n', 'framebuffers', api='gles2')
def glGenFramebuffers(n):
	pass


@params('program', 'maxCount', 'count', 'shaders', api='gles2')
def glGetAttachedShaders(program, maxCount, count):
	pass


@params('program', 'location', 'params', api='gles2')
def glGetUniformfv(program, location):
	pass


@params('target', 'pname', 'params', api='gles2')
def glGetRenderbufferParameteriv(target, pname):
	pass


@params('target', 'level', 'internalformat', 'x', 'y', 'width', 'height', 'border', api='gles2')
def glCopyTexImage2D(target, level, internalformat, x, y, width, height, border):
	pass


@params('location', 'count', 'value', api='gles2')
def glUniform3iv(location, count, value):
	pass


@params('program', api='gles2')
def glUseProgram(program):
	pass


@params('program', 'bufSize', 'length', 'infoLog', api='gles2')
def glGetProgramInfoLog(program, bufSize, length):
	pass


@params('pname', 'data', api='gles2')
def glGetBooleanv(pname):
	pass


@params('shader', api='gles2')
def glDeleteShader(shader):
	pass


@params('target', 'pname', 'param', api='gles2')
def glTexParameterf(target, pname, param):
	pass


@params('target', 'pname', 'param', api='gles2')
def glTexParameteri(target, pname, param):
	pass


@params('shader', 'bufSize', 'length', 'source', api='gles2')
def glGetShaderSource(shader, bufSize, length):
	pass


@params('index', 'v', api='gles2')
def glVertexAttrib3fv(index, v):
	pass


@params('program', api='gles2')
def glLinkProgram(program):
	pass


@params('name', api='gles2')
def glGetString(name):
	pass


@params('n', 'textures', api='gles2')
def glDeleteTextures(n, textures):
	pass


@params('index', 'x', 'y', 'z', 'w', api='gles2')
def glVertexAttrib4f(index, x, y, z, w):
	pass


@params('location', 'v0', api='gles2')
def glUniform1i(location, v0):
	pass


@params('mode', api='gles2')
def glCullFace(mode):
	pass


@params('program', 'shader', api='gles2')
def glAttachShader(program, shader):
	pass


@params('target', 'pname', 'params', api='gles2')
def glGetBufferParameteriv(target, pname):
	pass


@params('location', 'count', 'transpose', 'value', api='gles2')
def glUniformMatrix3fv(location, count, transpose, value):
	pass


@params('func', 'ref', 'mask', api='gles2')
def glStencilFunc(func, ref, mask):
	pass


@params('shader', 'bufSize', 'length', 'infoLog', api='gles2')
def glGetShaderInfoLog(shader, bufSize, length):
	pass


@params('modeRGB', 'modeAlpha', api='gles2')
def glBlendEquationSeparate(modeRGB, modeAlpha):
	pass


@params('n', 'buffers', api='gles2')
def glDeleteBuffers(n, buffers):
	pass


@params('x', 'y', 'width', 'height', api='gles2')
def glScissor(x, y, width, height):
	pass


@params('location', 'count', 'value', api='gles2')
def glUniform2fv(location, count, value):
	pass


@params('target', api='gles2')
def glCheckFramebufferStatus(target):
	pass


@params(api = 'gles2')
def glGetError():
	pass


@params('pname', 'param', api='gles2')
def glPixelStorei(pname, param):
	pass


@params('flag', api='gles2')
def glDepthMask(flag):
	pass


@params('type', api='gles2')
def glCreateShader(type):
	pass


@params('n', 'renderbuffers', api='gles2')
def glGenRenderbuffers(n):
	pass


@params('target', 'level', 'xoffset', 'yoffset', 'x', 'y', 'width', 'height', api='gles2')
def glCopyTexSubImage2D(target, level, xoffset, yoffset, x, y, width, height):
	pass


@params('sfactorRGB', 'dfactorRGB', 'sfactorAlpha', 'dfactorAlpha', api='gles2')
def glBlendFuncSeparate(sfactorRGB, dfactorRGB, sfactorAlpha, dfactorAlpha):
	pass


@params('location', 'v0', 'v1', 'v2', api='gles2')
def glUniform3f(location, v0, v1, v2):
	pass


@params('n', 'framebuffers', api='gles2')
def glDeleteFramebuffers(n, framebuffers):
	pass


@params('mode', 'first', 'count', api='gles2')
def glDrawArrays(mode, first, count):
	pass


@params('mask', api='gles2')
def glClear(mask):
	pass


@params('index', api='gles2')
def glDisableVertexAttribArray(index):
	pass


@params('value', 'invert', api='gles2')
def glSampleCoverage(value, invert):
	pass


@params('location', 'v0', 'v1', api='gles2')
def glUniform2i(location, v0, v1):
	pass


@params('target', 'framebuffer', api='gles2')
def glBindFramebuffer(target, framebuffer):
	pass


@params('x', 'y', 'width', 'height', api='gles2')
def glViewport(x, y, width, height):
	pass


@params('renderbuffer', api='gles2')
def glIsRenderbuffer(renderbuffer):
	pass


@params('program', api='gles2')
def glValidateProgram(program):
	pass


@params('target', 'texture', api='gles2')
def glBindTexture(target, texture):
	pass


@params('program', 'shader', api='gles2')
def glDetachShader(program, shader):
	pass


@params('program', 'location', 'params', api='gles2')
def glGetUniformiv(program, location):
	pass


@params('target', 'buffer', api='gles2')
def glBindBuffer(target, buffer):
	pass


@params('target', api='gles2')
def glGenerateMipmap(target):
	pass


@params(api = 'gles2')
def glReleaseShaderCompiler():
	pass


@params('x', 'y', 'width', 'height', 'format', 'type', 'pixels', api='gles2')
def glReadPixels(x, y, width, height, format, type, pixels):
	pass


@params('n', 'buffers', api='gles2')
def glGenBuffers(n):
	pass


@params('framebuffer', api='gles2')
def glIsFramebuffer(framebuffer):
	pass


@params('func', api='gles2')
def glDepthFunc(func):
	pass


@params('program', 'name', api='gles2')
def glGetUniformLocation(program, name):
	pass


@params('location', 'count', 'value', api='gles2')
def glUniform4fv(location, count, value):
	pass


@params('pname', 'data', api='gles2')
def glGetFloatv(pname):
	pass


@params('pname', 'data', api='gles2')
def glGetIntegerv(pname):
	pass


@params('target', 'level', 'internalformat', 'width', 'height', 'border', 'format', 'type', 'pixels', api='gles2')
def glTexImage2D(target, level, internalformat, width, height, border, format, type, pixels):
	pass


@params('program', 'index', 'bufSize', 'length', 'size', 'type', 'name', api='gles2')
def glGetActiveUniform(program, index, bufSize, length, size, type, name):
	pass


@params('target', 'attachment', 'renderbuffertarget', 'renderbuffer', api='gles2')
def glFramebufferRenderbuffer(target, attachment, renderbuffertarget, renderbuffer):
	pass


@params('width', api='gles2')
def glLineWidth(width):
	pass


@params('n', 'f', api='gles2')
def glDepthRangef(n, f):
	pass


@params('target', 'attachment', 'pname', 'params', api='gles2')
def glGetFramebufferAttachmentParameteriv(target, attachment, pname):
	pass


@params('target', 'pname', 'params', api='gles2')
def glTexParameteriv(target, pname, params):
	pass


@params(api = 'gles2')
def glFlush():
	pass


@params('s', api='gles2')
def glClearStencil(s):
	pass


@params('texture', api='gles2')
def glIsTexture(texture):
	pass


@params('factor', 'units', api='gles2')
def glPolygonOffset(factor, units):
	pass


@params('program', 'pname', 'params', api='gles2')
def glGetProgramiv(program, pname):
	pass


@params('location', 'count', 'value', api='gles2')
def glUniform3fv(location, count, value):
	pass


@params(api = 'gles2')
def glFinish():
	pass


@params('index', 'pname', 'params', api='gles2')
def glGetVertexAttribfv(index, pname):
	pass


@params('program', 'index', 'bufSize', 'length', 'size', 'type', 'name', api='gles2')
def glGetActiveAttrib(program, index, bufSize, length, size, type, name):
	pass


@params('location', 'v0', 'v1', 'v2', api='gles2')
def glUniform3i(location, v0, v1, v2):
	pass


@params('target', 'level', 'xoffset', 'yoffset', 'width', 'height', 'format', 'type', 'pixels', api='gles2')
def glTexSubImage2D(target, level, xoffset, yoffset, width, height, format, type, pixels):
	pass


@params('count', 'shaders', 'binaryformat', 'binary', 'length', api='gles2')
def glShaderBinary(count, shaders, binaryformat, binary, length):
	pass


@params('mode', 'count', 'type', 'indices', api='gles2')
def glDrawElements(mode, count, type, indices):
	pass


@params('location', 'count', 'value', api='gles2')
def glUniform1iv(location, count, value):
	pass


@params('target', 'renderbuffer', api='gles2')
def glBindRenderbuffer(target, renderbuffer):
	pass


@params('program', api='gles2')
def glIsProgram(program):
	pass


@params('index', 'v', api='gles2')
def glVertexAttrib4fv(index, v):
	pass


@params('index', 'v', api='gles2')
def glVertexAttrib2fv(index, v):
	pass


@params('location', 'v0', 'v1', api='gles2')
def glUniform2f(location, v0, v1):
	pass


@params('d', api='gles2')
def glClearDepthf(d):
	pass


@params('red', 'green', 'blue', 'alpha', api='gles2')
def glColorMask(red, green, blue, alpha):
	pass


@params('mode', api='gles2')
def glBlendEquation(mode):
	pass


@params('program', 'index', 'name', api='gles2')
def glBindAttribLocation(program, index, name):
	pass


@params('target', 'pname', 'params', api='gles2')
def glTexParameterfv(target, pname, params):
	pass


@params('face', 'func', 'ref', 'mask', api='gles2')
def glStencilFuncSeparate(face, func, ref, mask):
	pass


@params('location', 'count', 'transpose', 'value', api='gles2')
def glUniformMatrix4fv(location, count, transpose, value):
	pass


@params('shader', api='gles2')
def glCompileShader(shader):
	pass


@params('target', 'level', 'internalformat', 'width', 'height', 'border', 'imageSize', 'data', api='gles2')
def glCompressedTexImage2D(target, level, internalformat, width, height, border, imageSize, data):
	pass


@params('index', 'x', api='gles2')
def glVertexAttrib1f(index, x):
	pass


@params('program', api='gles2')
def glDeleteProgram(program):
	pass


@params('index', 'x', 'y', 'z', api='gles2')
def glVertexAttrib3f(index, x, y, z):
	pass


@params('shader', api='gles2')
def glIsShader(shader):
	pass


@params('cap', api='gles2')
def glEnable(cap):
	pass


@params('program', 'name', api='gles2')
def glGetAttribLocation(program, name):
	pass


@params('location', 'count', 'value', api='gles2')
def glUniform4iv(location, count, value):
	pass


@params('n', 'textures', api='gles2')
def glGenTextures(n):
	pass


@params('index', 'size', 'type', 'normalized', 'stride', 'pointer', api='gles2')
def glVertexAttribPointer(index, size, type, normalized, stride, pointer):
	pass


@params('location', 'v0', api='gles2')
def glUniform1f(location, v0):
	pass


@params('location', 'count', 'value', api='gles2')
def glUniform2iv(location, count, value):
	pass


@params('shader', 'pname', 'params', api='gles2')
def glGetShaderiv(shader, pname):
	pass


@params('index', 'pname', 'params', api='gles2')
def glGetVertexAttribiv(index, pname):
	pass


@params('location', 'count', 'transpose', 'value', api='gles2')
def glUniformMatrix2fv(location, count, transpose, value):
	pass


@params('target', 'mode', api='gles2')
def glHint(target, mode):
	pass


@params('face', 'sfail', 'dpfail', 'dppass', api='gles2')
def glStencilOpSeparate(face, sfail, dpfail, dppass):
	pass


@params('target', 'pname', 'params', api='gles2')
def glGetTexParameteriv(target, pname):
	pass


@params('index', 'pname', 'pointer', api='gles2')
def glGetVertexAttribPointerv(index, pname, pointer):
	pass


@params('cap', api='gles2')
def glDisable(cap):
	pass


@params('red', 'green', 'blue', 'alpha', api='gles2')
def glBlendColor(red, green, blue, alpha):
	pass


@params('location', 'v0', 'v1', 'v2', 'v3', api='gles2')
def glUniform4i(location, v0, v1, v2, v3):
	pass


@params('texture', api='gles2')
def glActiveTexture(texture):
	pass


@params('index', api='gles2')
def glEnableVertexAttribArray(index):
	pass


@params('location', 'v0', 'v1', 'v2', 'v3', api='gles2')
def glUniform4f(location, v0, v1, v2, v3):
	pass


@params('target', 'offset', 'size', 'data', api='gles2')
def glBufferSubData(target, offset, size, data):
	pass


@params('sfactor', 'dfactor', api='gles2')
def glBlendFunc(sfactor, dfactor):
	pass


@params(api = 'gles2')
def glCreateProgram():
	pass


@params('red', 'green', 'blue', 'alpha', api='gles2')
def glClearColor(red, green, blue, alpha):
	pass


@params('mask', api='gles2')
def glStencilMask(mask):
	pass


@params('target', 'level', 'xoffset', 'yoffset', 'width', 'height', 'format', 'imageSize', 'data', api='gles2')
def glCompressedTexSubImage2D(target, level, xoffset, yoffset, width, height, format, imageSize, data):
	pass


@params('target', 'pname', 'params', api='gles2')
def glGetTexParameterfv(target, pname):
	pass


@params('shadertype', 'precisiontype', 'range', 'precision', api='gles2')
def glGetShaderPrecisionFormat(shadertype, precisiontype):
	pass


@params('shader', 'count', 'conststring', 'length', api='gles2')
def glShaderSource(shader, count, conststring, length):
	pass


@params('n', 'renderbuffers', api='gles2')
def glDeleteRenderbuffers(n, renderbuffers):
	pass


@params('target', 'size', 'data', 'usage', api='gles2')
def glBufferData(target, size, data, usage):
	pass


@params('target', 'attachment', 'textarget', 'texture', 'level', api='gles2')
def glFramebufferTexture2D(target, attachment, textarget, texture, level):
	pass


@params('location', 'count', 'value', api='gles2')
def glUniform1fv(location, count, value):
	pass


@params('index', 'x', 'y', api='gles2')
def glVertexAttrib2f(index, x, y):
	pass


@params('mode', api='gles2')
def glFrontFace(mode):
	pass


