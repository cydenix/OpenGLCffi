from OpenGLCffi.GLES2 import params
@params(api='gles2', prms=['face', 'mask'])
def glStencilMaskSeparate(face, mask):
	pass


@params(api='gles2', prms=['buffer'])
def glIsBuffer(buffer):
	pass


@params(api='gles2', prms=['target', 'internalformat', 'width', 'height'])
def glRenderbufferStorage(target, internalformat, width, height):
	pass


@params(api='gles2', prms=['index', 'v'])
def glVertexAttrib1fv(index, v):
	pass


@params(api='gles2', prms=['cap'])
def glIsEnabled(cap):
	pass


@params(api='gles2', prms=['fail', 'zfail', 'zpass'])
def glStencilOp(fail, zfail, zpass):
	pass


@params(api='gles2', prms=['n', 'framebuffers'])
def glGenFramebuffers(n):
	pass


@params(api='gles2', prms=['program', 'maxCount', 'count', 'shaders'])
def glGetAttachedShaders(program, maxCount, count):
	pass


@params(api='gles2', prms=['program', 'location', 'params'])
def glGetUniformfv(program, location):
	pass


@params(api='gles2', prms=['target', 'pname', 'params'])
def glGetRenderbufferParameteriv(target, pname):
	pass


@params(api='gles2', prms=['target', 'level', 'internalformat', 'x', 'y', 'width', 'height', 'border'])
def glCopyTexImage2D(target, level, internalformat, x, y, width, height, border):
	pass


@params(api='gles2', prms=['location', 'count', 'value'])
def glUniform3iv(location, count, value):
	pass


@params(api='gles2', prms=['program'])
def glUseProgram(program):
	pass


@params(api='gles2', prms=['program', 'bufSize', 'length', 'infoLog'])
def glGetProgramInfoLog(program, bufSize, length):
	pass


@params(api='gles2', prms=['pname', 'data'])
def glGetBooleanv(pname):
	pass


@params(api='gles2', prms=['shader'])
def glDeleteShader(shader):
	pass


@params(api='gles2', prms=['target', 'pname', 'param'])
def glTexParameterf(target, pname, param):
	pass


@params(api='gles2', prms=['target', 'pname', 'param'])
def glTexParameteri(target, pname, param):
	pass


@params(api='gles2', prms=['shader', 'bufSize', 'length', 'source'])
def glGetShaderSource(shader, bufSize, length):
	pass


@params(api='gles2', prms=['index', 'v'])
def glVertexAttrib3fv(index, v):
	pass


@params(api='gles2', prms=['program'])
def glLinkProgram(program):
	pass


@params(api='gles2', prms=['name'])
def glGetString(name):
	pass


@params(api='gles2', prms=['n', 'textures'])
def glDeleteTextures(n, textures):
	pass


@params(api='gles2', prms=['index', 'x', 'y', 'z', 'w'])
def glVertexAttrib4f(index, x, y, z, w):
	pass


@params(api='gles2', prms=['location', 'v0'])
def glUniform1i(location, v0):
	pass


@params(api='gles2', prms=['mode'])
def glCullFace(mode):
	pass


@params(api='gles2', prms=['program', 'shader'])
def glAttachShader(program, shader):
	pass


@params(api='gles2', prms=['target', 'pname', 'params'])
def glGetBufferParameteriv(target, pname):
	pass


@params(api='gles2', prms=['location', 'count', 'transpose', 'value'])
def glUniformMatrix3fv(location, count, transpose, value):
	pass


@params(api='gles2', prms=['func', 'ref', 'mask'])
def glStencilFunc(func, ref, mask):
	pass


@params(api='gles2', prms=['shader', 'bufSize', 'length', 'infoLog'])
def glGetShaderInfoLog(shader, bufSize, length):
	pass


@params(api='gles2', prms=['modeRGB', 'modeAlpha'])
def glBlendEquationSeparate(modeRGB, modeAlpha):
	pass


@params(api='gles2', prms=['n', 'buffers'])
def glDeleteBuffers(n, buffers):
	pass


@params(api='gles2', prms=['x', 'y', 'width', 'height'])
def glScissor(x, y, width, height):
	pass


@params(api='gles2', prms=['location', 'count', 'value'])
def glUniform2fv(location, count, value):
	pass


@params(api='gles2', prms=['target'])
def glCheckFramebufferStatus(target):
	pass


@params(api='gles2', prms=[])
def glGetError():
	pass


@params(api='gles2', prms=['pname', 'param'])
def glPixelStorei(pname, param):
	pass


@params(api='gles2', prms=['flag'])
def glDepthMask(flag):
	pass


@params(api='gles2', prms=['type'])
def glCreateShader(type):
	pass


@params(api='gles2', prms=['n', 'renderbuffers'])
def glGenRenderbuffers(n):
	pass


@params(api='gles2', prms=['target', 'level', 'xoffset', 'yoffset', 'x', 'y', 'width', 'height'])
def glCopyTexSubImage2D(target, level, xoffset, yoffset, x, y, width, height):
	pass


@params(api='gles2', prms=['sfactorRGB', 'dfactorRGB', 'sfactorAlpha', 'dfactorAlpha'])
def glBlendFuncSeparate(sfactorRGB, dfactorRGB, sfactorAlpha, dfactorAlpha):
	pass


@params(api='gles2', prms=['location', 'v0', 'v1', 'v2'])
def glUniform3f(location, v0, v1, v2):
	pass


@params(api='gles2', prms=['n', 'framebuffers'])
def glDeleteFramebuffers(n, framebuffers):
	pass


@params(api='gles2', prms=['mode', 'first', 'count'])
def glDrawArrays(mode, first, count):
	pass


@params(api='gles2', prms=['mask'])
def glClear(mask):
	pass


@params(api='gles2', prms=['index'])
def glDisableVertexAttribArray(index):
	pass


@params(api='gles2', prms=['value', 'invert'])
def glSampleCoverage(value, invert):
	pass


@params(api='gles2', prms=['location', 'v0', 'v1'])
def glUniform2i(location, v0, v1):
	pass


@params(api='gles2', prms=['target', 'framebuffer'])
def glBindFramebuffer(target, framebuffer):
	pass


@params(api='gles2', prms=['x', 'y', 'width', 'height'])
def glViewport(x, y, width, height):
	pass


@params(api='gles2', prms=['renderbuffer'])
def glIsRenderbuffer(renderbuffer):
	pass


@params(api='gles2', prms=['program'])
def glValidateProgram(program):
	pass


@params(api='gles2', prms=['target', 'texture'])
def glBindTexture(target, texture):
	pass


@params(api='gles2', prms=['program', 'shader'])
def glDetachShader(program, shader):
	pass


@params(api='gles2', prms=['program', 'location', 'params'])
def glGetUniformiv(program, location):
	pass


@params(api='gles2', prms=['target', 'buffer'])
def glBindBuffer(target, buffer):
	pass


@params(api='gles2', prms=['target'])
def glGenerateMipmap(target):
	pass


@params(api='gles2', prms=[])
def glReleaseShaderCompiler():
	pass


@params(api='gles2', prms=['x', 'y', 'width', 'height', 'format', 'type', 'pixels'])
def glReadPixels(x, y, width, height, format, type, pixels):
	pass


@params(api='gles2', prms=['n', 'buffers'])
def glGenBuffers(n):
	pass


@params(api='gles2', prms=['framebuffer'])
def glIsFramebuffer(framebuffer):
	pass


@params(api='gles2', prms=['func'])
def glDepthFunc(func):
	pass


@params(api='gles2', prms=['program', 'name'])
def glGetUniformLocation(program, name):
	pass


@params(api='gles2', prms=['location', 'count', 'value'])
def glUniform4fv(location, count, value):
	pass


@params(api='gles2', prms=['pname', 'data'])
def glGetFloatv(pname):
	pass


@params(api='gles2', prms=['pname', 'data'])
def glGetIntegerv(pname):
	pass


@params(api='gles2', prms=['target', 'level', 'internalformat', 'width', 'height', 'border', 'format', 'type', 'pixels'])
def glTexImage2D(target, level, internalformat, width, height, border, format, type, pixels):
	pass


@params(api='gles2', prms=['program', 'index', 'bufSize', 'length', 'size', 'type', 'name'])
def glGetActiveUniform(program, index, bufSize, length, size, type, name):
	pass


@params(api='gles2', prms=['target', 'attachment', 'renderbuffertarget', 'renderbuffer'])
def glFramebufferRenderbuffer(target, attachment, renderbuffertarget, renderbuffer):
	pass


@params(api='gles2', prms=['width'])
def glLineWidth(width):
	pass


@params(api='gles2', prms=['n', 'f'])
def glDepthRangef(n, f):
	pass


@params(api='gles2', prms=['target', 'attachment', 'pname', 'params'])
def glGetFramebufferAttachmentParameteriv(target, attachment, pname):
	pass


@params(api='gles2', prms=['target', 'pname', 'params'])
def glTexParameteriv(target, pname, params):
	pass


@params(api='gles2', prms=[])
def glFlush():
	pass


@params(api='gles2', prms=['s'])
def glClearStencil(s):
	pass


@params(api='gles2', prms=['texture'])
def glIsTexture(texture):
	pass


@params(api='gles2', prms=['factor', 'units'])
def glPolygonOffset(factor, units):
	pass


@params(api='gles2', prms=['program', 'pname', 'params'])
def glGetProgramiv(program, pname):
	pass


@params(api='gles2', prms=['location', 'count', 'value'])
def glUniform3fv(location, count, value):
	pass


@params(api='gles2', prms=[])
def glFinish():
	pass


@params(api='gles2', prms=['index', 'pname', 'params'])
def glGetVertexAttribfv(index, pname):
	pass


@params(api='gles2', prms=['program', 'index', 'bufSize', 'length', 'size', 'type', 'name'])
def glGetActiveAttrib(program, index, bufSize, length, size, type, name):
	pass


@params(api='gles2', prms=['location', 'v0', 'v1', 'v2'])
def glUniform3i(location, v0, v1, v2):
	pass


@params(api='gles2', prms=['target', 'level', 'xoffset', 'yoffset', 'width', 'height', 'format', 'type', 'pixels'])
def glTexSubImage2D(target, level, xoffset, yoffset, width, height, format, type, pixels):
	pass


@params(api='gles2', prms=['count', 'shaders', 'binaryformat', 'binary', 'length'])
def glShaderBinary(count, shaders, binaryformat, binary, length):
	pass


@params(api='gles2', prms=['mode', 'count', 'type', 'indices'])
def glDrawElements(mode, count, type, indices):
	pass


@params(api='gles2', prms=['location', 'count', 'value'])
def glUniform1iv(location, count, value):
	pass


@params(api='gles2', prms=['target', 'renderbuffer'])
def glBindRenderbuffer(target, renderbuffer):
	pass


@params(api='gles2', prms=['program'])
def glIsProgram(program):
	pass


@params(api='gles2', prms=['index', 'v'])
def glVertexAttrib4fv(index, v):
	pass


@params(api='gles2', prms=['index', 'v'])
def glVertexAttrib2fv(index, v):
	pass


@params(api='gles2', prms=['location', 'v0', 'v1'])
def glUniform2f(location, v0, v1):
	pass


@params(api='gles2', prms=['d'])
def glClearDepthf(d):
	pass


@params(api='gles2', prms=['red', 'green', 'blue', 'alpha'])
def glColorMask(red, green, blue, alpha):
	pass


@params(api='gles2', prms=['mode'])
def glBlendEquation(mode):
	pass


@params(api='gles2', prms=['program', 'index', 'name'])
def glBindAttribLocation(program, index, name):
	pass


@params(api='gles2', prms=['target', 'pname', 'params'])
def glTexParameterfv(target, pname, params):
	pass


@params(api='gles2', prms=['face', 'func', 'ref', 'mask'])
def glStencilFuncSeparate(face, func, ref, mask):
	pass


@params(api='gles2', prms=['location', 'count', 'transpose', 'value'])
def glUniformMatrix4fv(location, count, transpose, value):
	pass


@params(api='gles2', prms=['shader'])
def glCompileShader(shader):
	pass


@params(api='gles2', prms=['target', 'level', 'internalformat', 'width', 'height', 'border', 'imageSize', 'data'])
def glCompressedTexImage2D(target, level, internalformat, width, height, border, imageSize, data):
	pass


@params(api='gles2', prms=['index', 'x'])
def glVertexAttrib1f(index, x):
	pass


@params(api='gles2', prms=['program'])
def glDeleteProgram(program):
	pass


@params(api='gles2', prms=['index', 'x', 'y', 'z'])
def glVertexAttrib3f(index, x, y, z):
	pass


@params(api='gles2', prms=['shader'])
def glIsShader(shader):
	pass


@params(api='gles2', prms=['cap'])
def glEnable(cap):
	pass


@params(api='gles2', prms=['program', 'name'])
def glGetAttribLocation(program, name):
	pass


@params(api='gles2', prms=['location', 'count', 'value'])
def glUniform4iv(location, count, value):
	pass


@params(api='gles2', prms=['n', 'textures'])
def glGenTextures(n):
	pass


@params(api='gles2', prms=['index', 'size', 'type', 'normalized', 'stride', 'pointer'])
def glVertexAttribPointer(index, size, type, normalized, stride, pointer):
	pass


@params(api='gles2', prms=['location', 'v0'])
def glUniform1f(location, v0):
	pass


@params(api='gles2', prms=['location', 'count', 'value'])
def glUniform2iv(location, count, value):
	pass


@params(api='gles2', prms=['shader', 'pname', 'params'])
def glGetShaderiv(shader, pname):
	pass


@params(api='gles2', prms=['index', 'pname', 'params'])
def glGetVertexAttribiv(index, pname):
	pass


@params(api='gles2', prms=['location', 'count', 'transpose', 'value'])
def glUniformMatrix2fv(location, count, transpose, value):
	pass


@params(api='gles2', prms=['target', 'mode'])
def glHint(target, mode):
	pass


@params(api='gles2', prms=['face', 'sfail', 'dpfail', 'dppass'])
def glStencilOpSeparate(face, sfail, dpfail, dppass):
	pass


@params(api='gles2', prms=['target', 'pname', 'params'])
def glGetTexParameteriv(target, pname):
	pass


@params(api='gles2', prms=['index', 'pname', 'pointer'])
def glGetVertexAttribPointerv(index, pname, pointer):
	pass


@params(api='gles2', prms=['cap'])
def glDisable(cap):
	pass


@params(api='gles2', prms=['red', 'green', 'blue', 'alpha'])
def glBlendColor(red, green, blue, alpha):
	pass


@params(api='gles2', prms=['location', 'v0', 'v1', 'v2', 'v3'])
def glUniform4i(location, v0, v1, v2, v3):
	pass


@params(api='gles2', prms=['texture'])
def glActiveTexture(texture):
	pass


@params(api='gles2', prms=['index'])
def glEnableVertexAttribArray(index):
	pass


@params(api='gles2', prms=['location', 'v0', 'v1', 'v2', 'v3'])
def glUniform4f(location, v0, v1, v2, v3):
	pass


@params(api='gles2', prms=['target', 'offset', 'size', 'data'])
def glBufferSubData(target, offset, size, data):
	pass


@params(api='gles2', prms=['sfactor', 'dfactor'])
def glBlendFunc(sfactor, dfactor):
	pass


@params(api='gles2', prms=[])
def glCreateProgram():
	pass


@params(api='gles2', prms=['red', 'green', 'blue', 'alpha'])
def glClearColor(red, green, blue, alpha):
	pass


@params(api='gles2', prms=['mask'])
def glStencilMask(mask):
	pass


@params(api='gles2', prms=['target', 'level', 'xoffset', 'yoffset', 'width', 'height', 'format', 'imageSize', 'data'])
def glCompressedTexSubImage2D(target, level, xoffset, yoffset, width, height, format, imageSize, data):
	pass


@params(api='gles2', prms=['target', 'pname', 'params'])
def glGetTexParameterfv(target, pname):
	pass


@params(api='gles2', prms=['shadertype', 'precisiontype', 'range', 'precision'])
def glGetShaderPrecisionFormat(shadertype, precisiontype):
	pass


@params(api='gles2', prms=['shader', 'count', 'conststring', 'length'])
def glShaderSource(shader, count, conststring, length):
	pass


@params(api='gles2', prms=['n', 'renderbuffers'])
def glDeleteRenderbuffers(n, renderbuffers):
	pass


@params(api='gles2', prms=['target', 'size', 'data', 'usage'])
def glBufferData(target, size, data, usage):
	pass


@params(api='gles2', prms=['target', 'attachment', 'textarget', 'texture', 'level'])
def glFramebufferTexture2D(target, attachment, textarget, texture, level):
	pass


@params(api='gles2', prms=['location', 'count', 'value'])
def glUniform1fv(location, count, value):
	pass


@params(api='gles2', prms=['index', 'x', 'y'])
def glVertexAttrib2f(index, x, y):
	pass


@params(api='gles2', prms=['mode'])
def glFrontFace(mode):
	pass


