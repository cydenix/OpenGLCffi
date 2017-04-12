from OpenGLCffi.GL import params
@params(api='gl', prms=['target', 'level', 'internalformat', 'x', 'y', 'width', 'border'])
def glCopyTexImage1D(target, level, internalformat, x, y, width, border):
	pass


@params(api='gl', prms=['vaobj', 'buffer'])
def glVertexArrayElementBuffer(vaobj, buffer):
	pass


@params(api='gl', prms=['face', 'mask'])
def glStencilMaskSeparate(face, mask):
	pass


@params(api='gl', prms=['texture', 'samples', 'internalformat', 'width', 'height', 'depth', 'fixedsamplelocations'])
def glTextureStorage3DMultisample(texture, samples, internalformat, width, height, depth, fixedsamplelocations):
	pass


@params(api='gl', prms=['texture', 'pname', 'param'])
def glTextureParameterfv(texture, pname, param):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib4usv(index, v):
	pass


@params(api='gl', prms=['c'])
def glIndexi(c):
	pass


@params(api='gl', prms=['target', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth', 'format', 'imageSize', 'data'])
def glCompressedTexSubImage3D(target, level, xoffset, yoffset, zoffset, width, height, depth, format, imageSize, data):
	pass


@params(api='gl', prms=['u', 'v'])
def glEvalCoord2d(u, v):
	pass


@params(api='gl', prms=['u', 'v'])
def glEvalCoord2f(u, v):
	pass


@params(api='gl', prms=['c'])
def glIndexd(c):
	pass


@params(api='gl', prms=['c'])
def glIndexf(c):
	pass


@params(api='gl', prms=['c'])
def glIndexs(c):
	pass


@params(api='gl', prms=['v'])
def glVertex3sv(v):
	pass


@params(api='gl', prms=['target', 'query', 'bufSize', 'v'])
def glGetnMapfv(target, query, bufSize, v):
	pass


@params(api='gl', prms=['v'])
def glSecondaryColor3fv(v):
	pass


@params(api='gl', prms=['pname', 'params'])
def glFogfv(pname, params):
	pass


@params(api='gl', prms=['mode', 'count', 'type', 'indices', 'instancecount', 'baseinstance'])
def glDrawElementsInstancedBaseInstance(mode, count, type, indices, instancecount, baseinstance):
	pass


@params(api='gl', prms=['buffer'])
def glIsBuffer(buffer):
	pass


@params(api='gl', prms=['pname', 'index', 'val'])
def glGetMultisamplefv(pname, index, val):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix4fv(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['source', 'type', 'severity', 'count', 'ids', 'enabled'])
def glDebugMessageControl(source, type, severity, count, ids, enabled):
	pass


@params(api='gl', prms=[])
def glPopAttrib():
	pass


@params(api='gl', prms=['face', 'mode'])
def glColorMaterial(face, mode):
	pass


@params(api='gl', prms=['target', 'internalformat', 'width', 'height'])
def glRenderbufferStorage(target, internalformat, width, height):
	pass


@params(api='gl', prms=['red', 'green', 'blue'])
def glColor3b(red, green, blue):
	pass


@params(api='gl', prms=['red', 'green', 'blue'])
def glColor3f(red, green, blue):
	pass


@params(api='gl', prms=['red', 'green', 'blue'])
def glColor3d(red, green, blue):
	pass


@params(api='gl', prms=['target', 'query', 'bufSize', 'v'])
def glGetnMapiv(target, query, bufSize, v):
	pass


@params(api='gl', prms=['red', 'green', 'blue'])
def glColor3i(red, green, blue):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib4ubv(index, v):
	pass


@params(api='gl', prms=['red', 'green', 'blue'])
def glColor3s(red, green, blue):
	pass


@params(api='gl', prms=['vaobj', 'index', 'pname', 'param'])
def glGetVertexArrayIndexediv(vaobj, index, pname, param):
	pass


@params(api='gl', prms=['target', 'v'])
def glMultiTexCoord1iv(target, v):
	pass


@params(api='gl', prms=['texture', 'type', 'coords'])
def glMultiTexCoordP2ui(texture, type, coords):
	pass


@params(api='gl', prms=['program', 'location', 'v0', 'v1', 'v2'])
def glProgramUniform3f(program, location, v0, v1, v2):
	pass


@params(api='gl', prms=['index', 'x', 'y', 'z', 'w'])
def glVertexAttribL4d(index, x, y, z, w):
	pass


@params(api='gl', prms=['v'])
def glVertex2iv(v):
	pass


@params(api='gl', prms=['vaobj', 'attribindex', 'size', 'type', 'relativeoffset'])
def glVertexArrayAttribLFormat(vaobj, attribindex, size, type, relativeoffset):
	pass


@params(api='gl', prms=['buffer', 'offset', 'length'])
def glInvalidateBufferSubData(buffer, offset, length):
	pass


@params(api='gl', prms=[])
def glResumeTransformFeedback():
	pass


@params(api='gl', prms=['pname', 'param'])
def glFogi(pname, param):
	pass


@params(api='gl', prms=['size', 'type', 'stride', 'pointer'])
def glVertexPointer(size, type, stride, pointer):
	pass


@params(api='gl', prms=['pname', 'param'])
def glFogf(pname, param):
	pass


@params(api='gl', prms=['target', 's'])
def glMultiTexCoord1d(target, s):
	pass


@params(api='gl', prms=['target', 's'])
def glMultiTexCoord1f(target, s):
	pass


@params(api='gl', prms=['index', 'x', 'y'])
def glVertexAttribI2i(index, x, y):
	pass


@params(api='gl', prms=['target', 's'])
def glMultiTexCoord1i(target, s):
	pass


@params(api='gl', prms=[])
def glGetGraphicsResetStatus():
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib1fv(index, v):
	pass


@params(api='gl', prms=['cap'])
def glIsEnabled(cap):
	pass


@params(api='gl', prms=['fail', 'zfail', 'zpass'])
def glStencilOp(fail, zfail, zpass):
	pass


@params(api='gl', prms=['buffer', 'offset', 'length', 'access'])
def glMapNamedBufferRange(buffer, offset, length, access):
	pass


@params(api='gl', prms=['vaobj', 'attribindex', 'size', 'type', 'relativeoffset'])
def glVertexArrayAttribIFormat(vaobj, attribindex, size, type, relativeoffset):
	pass


@params(api='gl', prms=['n', 'framebuffers'])
def glGenFramebuffers(n, framebuffers):
	pass


@params(api='gl', prms=['program', 'maxCount', 'count', 'shaders'])
def glGetAttachedShaders(program, maxCount, count, shaders):
	pass


@params(api='gl', prms=['n', 'arrays'])
def glDeleteVertexArrays(n, arrays):
	pass


@params(api='gl', prms=['first', 'count', 'v'])
def glViewportArrayv(first, count, v):
	pass


@params(api='gl', prms=['target', 's', 't'])
def glMultiTexCoord2s(target, s, t):
	pass


@params(api='gl', prms=['v'])
def glVertex3dv(v):
	pass


@params(api='gl', prms=['v'])
def glColor4fv(v):
	pass


@params(api='gl', prms=['vaobj', 'bindingindex', 'divisor'])
def glVertexArrayBindingDivisor(vaobj, bindingindex, divisor):
	pass


@params(api='gl', prms=['v'])
def glTexCoord2sv(v):
	pass


@params(api='gl', prms=['location', 'count', 'value'])
def glUniform2dv(location, count, value):
	pass


@params(api='gl', prms=['map', 'values'])
def glGetPixelMapuiv(map, values):
	pass


@params(api='gl', prms=['pname', 'params'])
def glGetPointerv(pname, params):
	pass


@params(api='gl', prms=['program', 'location', 'params'])
def glGetUniformfv(program, location, params):
	pass


@params(api='gl', prms=['program', 'location', 'params'])
def glGetUniformuiv(program, location, params):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix3fv(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['mode', 'count', 'type', 'indices', 'instancecount'])
def glDrawElementsInstanced(mode, count, type, indices, instancecount):
	pass


@params(api='gl', prms=['index', 'x', 'y', 'z', 'w'])
def glVertexAttrib4d(index, x, y, z, w):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glGetRenderbufferParameteriv(target, pname, params):
	pass


@params(api='gl', prms=['renderbuffer', 'internalformat', 'width', 'height'])
def glNamedRenderbufferStorage(renderbuffer, internalformat, width, height):
	pass


@params(api='gl', prms=['condition', 'flags'])
def glFenceSync(condition, flags):
	pass


@params(api='gl', prms=['pipeline'])
def glValidateProgramPipeline(pipeline):
	pass


@params(api='gl', prms=['type', 'value'])
def glVertexP4ui(type, value):
	pass


@params(api='gl', prms=['count', 'samplers'])
def glGenSamplers(count, samplers):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib2sv(index, v):
	pass


@params(api='gl', prms=['mode', 'id', 'instancecount'])
def glDrawTransformFeedbackInstanced(mode, id, instancecount):
	pass


@params(api='gl', prms=['v'])
def glTexCoord4iv(v):
	pass


@params(api='gl', prms=['mode', 'id'])
def glDrawTransformFeedback(mode, id):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glGetTexParameterIuiv(target, pname, params):
	pass


@params(api='gl', prms=['type', 'stride', 'pointer'])
def glIndexPointer(type, stride, pointer):
	pass


@params(api='gl', prms=['sync'])
def glIsSync(sync):
	pass


@params(api='gl', prms=['v'])
def glVertex4iv(v):
	pass


@params(api='gl', prms=['target', 'v'])
def glMultiTexCoord3iv(target, v):
	pass


@params(api='gl', prms=['ptr', 'bufSize', 'length', 'label'])
def glGetObjectPtrLabel(ptr, bufSize, length, label):
	pass


@params(api='gl', prms=['texture', 'pname', 'param'])
def glTextureParameteri(texture, pname, param):
	pass


@params(api='gl', prms=['location', 'count', 'transpose', 'value'])
def glUniformMatrix2x3dv(location, count, transpose, value):
	pass


@params(api='gl', prms=['v'])
def glSecondaryColor3sv(v):
	pass


@params(api='gl', prms=['left', 'right', 'bottom', 'top', 'zNear', 'zFar'])
def glOrtho(left, right, bottom, top, zNear, zFar):
	pass


@params(api='gl', prms=['coord'])
def glFogCoordd(coord):
	pass


@params(api='gl', prms=['coord'])
def glFogCoordf(coord):
	pass


@params(api='gl', prms=['target', 'level', 'internalformat', 'x', 'y', 'width', 'height', 'border'])
def glCopyTexImage2D(target, level, internalformat, x, y, width, height, border):
	pass


@params(api='gl', prms=['index', 'type', 'normalized', 'value'])
def glVertexAttribP4ui(index, type, normalized, value):
	pass


@params(api='gl', prms=['location', 'count', 'value'])
def glUniform4uiv(location, count, value):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttribL1dv(index, v):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix2dv(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['first', 'count', 'v'])
def glScissorArrayv(first, count, v):
	pass


@params(api='gl', prms=['list'])
def glCallList(list):
	pass


@params(api='gl', prms=['pname', 'param'])
def glLightModeli(pname, param):
	pass


@params(api='gl', prms=['target', 'format', 'type', 'bufSize', 'table'])
def glGetnColorTable(target, format, type, bufSize, table):
	pass


@params(api='gl', prms=['v'])
def glWindowPos3iv(v):
	pass


@params(api='gl', prms=['target', 'numAttachments', 'attachments', 'x', 'y', 'width', 'height'])
def glInvalidateSubFramebuffer(target, numAttachments, attachments, x, y, width, height):
	pass


@params(api='gl', prms=['target', 'access'])
def glMapBuffer(target, access):
	pass


@params(api='gl', prms=['red', 'green', 'blue'])
def glSecondaryColor3d(red, green, blue):
	pass


@params(api='gl', prms=['attribindex', 'size', 'type', 'relativeoffset'])
def glVertexAttribLFormat(attribindex, size, type, relativeoffset):
	pass


@params(api='gl', prms=['red', 'green', 'blue'])
def glSecondaryColor3i(red, green, blue):
	pass


@params(api='gl', prms=['sync'])
def glDeleteSync(sync):
	pass


@params(api='gl', prms=['location', 'count', 'transpose', 'value'])
def glUniformMatrix4x2dv(location, count, transpose, value):
	pass


@params(api='gl', prms=['red', 'green', 'blue'])
def glSecondaryColor3s(red, green, blue):
	pass


@params(api='gl', prms=['location', 'count', 'value'])
def glUniform3iv(location, count, value):
	pass


@params(api='gl', prms=['s'])
def glTexCoord1s(s):
	pass


@params(api='gl', prms=['face', 'mode'])
def glPolygonMode(face, mode):
	pass


@params(api='gl', prms=['program'])
def glUseProgram(program):
	pass


@params(api='gl', prms=['factor', 'pattern'])
def glLineStipple(factor, pattern):
	pass


@params(api='gl', prms=['program', 'bufSize', 'length', 'infoLog'])
def glGetProgramInfoLog(program, bufSize, length, infoLog):
	pass


@params(api='gl', prms=['pname', 'param'])
def glPixelStoref(pname, param):
	pass


@params(api='gl', prms=['pname', 'data'])
def glGetBooleanv(pname, data):
	pass


@params(api='gl', prms=['shader'])
def glDeleteShader(shader):
	pass


@params(api='gl', prms=['texture', 'level', 'xoffset', 'x', 'y', 'width'])
def glCopyTextureSubImage1D(texture, level, xoffset, x, y, width):
	pass


@params(api='gl', prms=['target', 'query', 'v'])
def glGetMapdv(target, query, v):
	pass


@params(api='gl', prms=['texture', 'pname', 'params'])
def glTextureParameterIuiv(texture, pname, params):
	pass


@params(api='gl', prms=['s', 't', 'r'])
def glTexCoord3d(s, t, r):
	pass


@params(api='gl', prms=['index', 'x', 'y', 'z'])
def glVertexAttribI3i(index, x, y, z):
	pass


@params(api='gl', prms=['attribindex', 'size', 'type', 'normalized', 'relativeoffset'])
def glVertexAttribFormat(attribindex, size, type, normalized, relativeoffset):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttribI4usv(index, v):
	pass


@params(api='gl', prms=['target', 'pname', 'param'])
def glTexParameterf(target, pname, param):
	pass


@params(api='gl', prms=['attribindex', 'bindingindex'])
def glVertexAttribBinding(attribindex, bindingindex):
	pass


@params(api='gl', prms=['target', 'pname', 'param'])
def glTexParameteri(target, pname, param):
	pass


@params(api='gl', prms=['shader', 'bufSize', 'length', 'source'])
def glGetShaderSource(shader, bufSize, length, source):
	pass


@params(api='gl', prms=['index', 'x', 'y', 'z', 'w'])
def glVertexAttrib4s(index, x, y, z, w):
	pass


@params(api='gl', prms=[])
def glPopName():
	pass


@params(api='gl', prms=['n', 'pipelines'])
def glGenProgramPipelines(n, pipelines):
	pass


@params(api='gl', prms=['red', 'green', 'blue', 'alpha'])
def glColor4ub(red, green, blue, alpha):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib3fv(index, v):
	pass


@params(api='gl', prms=['red', 'green', 'blue', 'alpha'])
def glColor4ui(red, green, blue, alpha):
	pass


@params(api='gl', prms=['buffer', 'pname', 'params'])
def glGetNamedBufferParameteriv(buffer, pname, params):
	pass


@params(api='gl', prms=['red', 'green', 'blue', 'alpha'])
def glColor4us(red, green, blue, alpha):
	pass


@params(api='gl', prms=['index', 'type', 'normalized', 'value'])
def glVertexAttribP1uiv(index, type, normalized, value):
	pass


@params(api='gl', prms=['program'])
def glLinkProgram(program):
	pass


@params(api='gl', prms=['v'])
def glTexCoord2dv(v):
	pass


@params(api='gl', prms=['identifier', 'name', 'bufSize', 'length', 'label'])
def glGetObjectLabel(identifier, name, bufSize, length, label):
	pass


@params(api='gl', prms=['name'])
def glGetString(name):
	pass


@params(api='gl', prms=['target'])
def glEndQuery(target):
	pass


@params(api='gl', prms=['stride', 'pointer'])
def glEdgeFlagPointer(stride, pointer):
	pass


@params(api='gl', prms=['target', 'pname', 'param'])
def glFramebufferParameteri(target, pname, param):
	pass


@params(api='gl', prms=['x', 'y', 'width', 'height', 'type'])
def glCopyPixels(x, y, width, height, type):
	pass


@params(api='gl', prms=['index', 'x', 'y'])
def glVertexAttribI2ui(index, x, y):
	pass


@params(api='gl', prms=['x', 'y', 'z'])
def glRasterPos3s(x, y, z):
	pass


@params(api='gl', prms=['n', 'textures'])
def glDeleteTextures(n, textures):
	pass


@params(api='gl', prms=['origin', 'depth'])
def glClipControl(origin, depth):
	pass


@params(api='gl', prms=['index', 'x', 'y', 'z', 'w'])
def glVertexAttrib4f(index, x, y, z, w):
	pass


@params(api='gl', prms=['framebuffer', 'pname', 'param'])
def glNamedFramebufferParameteri(framebuffer, pname, param):
	pass


@params(api='gl', prms=['framebuffer', 'pname', 'param'])
def glGetNamedFramebufferParameteriv(framebuffer, pname, param):
	pass


@params(api='gl', prms=['n', 'arrays'])
def glCreateVertexArrays(n, arrays):
	pass


@params(api='gl', prms=['id', 'mode'])
def glBeginConditionalRender(id, mode):
	pass


@params(api='gl', prms=['sampler', 'pname', 'param'])
def glSamplerParameteri(sampler, pname, param):
	pass


@params(api='gl', prms=['location', 'x'])
def glUniform1d(location, x):
	pass


@params(api='gl', prms=['mode'])
def glRenderMode(mode):
	pass


@params(api='gl', prms=['target', 'level', 'img'])
def glGetCompressedTexImage(target, level, img):
	pass


@params(api='gl', prms=['program', 'uniformBlockIndex', 'pname', 'params'])
def glGetActiveUniformBlockiv(program, uniformBlockIndex, pname, params):
	pass


@params(api='gl', prms=['location', 'v0'])
def glUniform1i(location, v0):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glGetTexEnvfv(target, pname, params):
	pass


@params(api='gl', prms=['mode'])
def glCullFace(mode):
	pass


@params(api='gl', prms=['program', 'location', 'v0', 'v1', 'v2', 'v3'])
def glProgramUniform4i(program, location, v0, v1, v2, v3):
	pass


@params(api='gl', prms=['program', 'location', 'v0', 'v1', 'v2', 'v3'])
def glProgramUniform4f(program, location, v0, v1, v2, v3):
	pass


@params(api='gl', prms=['index', 'x', 'y', 'w', 'h'])
def glViewportIndexedf(index, x, y, w, h):
	pass


@params(api='gl', prms=['program', 'location', 'v0', 'v1', 'v2', 'v3'])
def glProgramUniform4d(program, location, v0, v1, v2, v3):
	pass


@params(api='gl', prms=['x', 'y', 'z'])
def glVertex3i(x, y, z):
	pass


@params(api='gl', prms=['program', 'shader'])
def glAttachShader(program, shader):
	pass


@params(api='gl', prms=['list'])
def glIsList(list):
	pass


@params(api='gl', prms=['type', 'stride', 'pointer'])
def glFogCoordPointer(type, stride, pointer):
	pass


@params(api='gl', prms=['buffer'])
def glUnmapNamedBuffer(buffer):
	pass


@params(api='gl', prms=['v'])
def glSecondaryColor3dv(v):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttribI4sv(index, v):
	pass


@params(api='gl', prms=['mode', 'id', 'stream', 'instancecount'])
def glDrawTransformFeedbackStreamInstanced(mode, id, stream, instancecount):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glGetBufferParameteriv(target, pname, params):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glTexParameterIuiv(target, pname, params):
	pass


@params(api='gl', prms=['v'])
def glWindowPos3fv(v):
	pass


@params(api='gl', prms=['pname', 'params'])
def glLightModelfv(pname, params):
	pass


@params(api='gl', prms=['texture', 'levels', 'internalformat', 'width', 'height', 'depth'])
def glTextureStorage3D(texture, levels, internalformat, width, height, depth):
	pass


@params(api='gl', prms=['id'])
def glIsTransformFeedback(id):
	pass


@params(api='gl', prms=['angle', 'x', 'y', 'z'])
def glRotated(angle, x, y, z):
	pass


@params(api='gl', prms=['pipeline'])
def glIsProgramPipeline(pipeline):
	pass


@params(api='gl', prms=['angle', 'x', 'y', 'z'])
def glRotatef(angle, x, y, z):
	pass


@params(api='gl', prms=['x', 'y', 'z', 'w'])
def glVertex4i(x, y, z, w):
	pass


@params(api='gl', prms=['program', 'shadertype', 'index', 'bufsize', 'length', 'name'])
def glGetActiveSubroutineUniformName(program, shadertype, index, bufsize, length, name):
	pass


@params(api='gl', prms=['location', 'count', 'transpose', 'value'])
def glUniformMatrix3fv(location, count, transpose, value):
	pass


@params(api='gl', prms=['program', 'location', 'bufSize', 'params'])
def glGetnUniformfv(program, location, bufSize, params):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttribL2dv(index, v):
	pass


@params(api='gl', prms=['size', 'type', 'stride', 'pointer'])
def glSecondaryColorPointer(size, type, stride, pointer):
	pass


@params(api='gl', prms=['func', 'ref'])
def glAlphaFunc(func, ref):
	pass


@params(api='gl', prms=['s', 't', 'r', 'q'])
def glTexCoord4d(s, t, r, q):
	pass


@params(api='gl', prms=['index', 'x', 'y'])
def glVertexAttribL2d(index, x, y):
	pass


@params(api='gl', prms=['func', 'ref', 'mask'])
def glStencilFunc(func, ref, mask):
	pass


@params(api='gl', prms=['v'])
def glTexCoord3dv(v):
	pass


@params(api='gl', prms=['id', 'buffer', 'pname', 'offset'])
def glGetQueryBufferObjectiv(id, buffer, pname, offset):
	pass


@params(api='gl', prms=['pipeline', 'pname', 'params'])
def glGetProgramPipelineiv(pipeline, pname, params):
	pass


@params(api='gl', prms=['indirect'])
def glDispatchComputeIndirect(indirect):
	pass


@params(api='gl', prms=['shader', 'bufSize', 'length', 'infoLog'])
def glGetShaderInfoLog(shader, bufSize, length, infoLog):
	pass


@params(api='gl', prms=['index', 'x', 'y', 'z', 'w'])
def glVertexAttribI4i(index, x, y, z, w):
	pass


@params(api='gl', prms=['v'])
def glRasterPos2iv(v):
	pass


@params(api='gl', prms=['v'])
def glSecondaryColor3uiv(v):
	pass


@params(api='gl', prms=['x', 'y'])
def glRasterPos2i(x, y):
	pass


@params(api='gl', prms=['modeRGB', 'modeAlpha'])
def glBlendEquationSeparate(modeRGB, modeAlpha):
	pass


@params(api='gl', prms=['program', 'shadertype', 'name'])
def glGetSubroutineIndex(program, shadertype, name):
	pass


@params(api='gl', prms=['mask'])
def glPushAttrib(mask):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttribL3dv(index, v):
	pass


@params(api='gl', prms=['light', 'pname', 'params'])
def glLightiv(light, pname, params):
	pass


@params(api='gl', prms=['n', 'buffers'])
def glDeleteBuffers(n, buffers):
	pass


@params(api='gl', prms=['pipeline'])
def glBindProgramPipeline(pipeline):
	pass


@params(api='gl', prms=['x', 'y', 'width', 'height'])
def glScissor(x, y, width, height):
	pass


@params(api='gl', prms=['face', 'pname', 'params'])
def glMaterialfv(face, pname, params):
	pass


@params(api='gl', prms=['location', 'count', 'transpose', 'value'])
def glUniformMatrix3dv(location, count, transpose, value):
	pass


@params(api='gl', prms=['texture', 'level', 'pname', 'params'])
def glGetTextureLevelParameteriv(texture, level, pname, params):
	pass


@params(api='gl', prms=['name', 'index'])
def glGetStringi(name, index):
	pass


@params(api='gl', prms=['v'])
def glColor4dv(v):
	pass


@params(api='gl', prms=['pname', 'params'])
def glPointParameterfv(pname, params):
	pass


@params(api='gl', prms=['location', 'count', 'value'])
def glUniform2fv(location, count, value):
	pass


@params(api='gl', prms=['framebuffer', 'numAttachments', 'attachments', 'x', 'y', 'width', 'height'])
def glInvalidateNamedFramebufferSubData(framebuffer, numAttachments, attachments, x, y, width, height):
	pass


@params(api='gl', prms=['target', 'index', 'buffer', 'offset', 'size'])
def glBindBufferRange(target, index, buffer, offset, size):
	pass


@params(api='gl', prms=['v'])
def glNormal3iv(v):
	pass


@params(api='gl', prms=['program', 'location', 'params'])
def glGetUniformdv(program, location, params):
	pass


@params(api='gl', prms=['target', 's', 't', 'r', 'q'])
def glMultiTexCoord4s(target, s, t, r, q):
	pass


@params(api='gl', prms=['v'])
def glTexCoord1iv(v):
	pass


@params(api='gl', prms=['v'])
def glColor3uiv(v):
	pass


@params(api='gl', prms=['base'])
def glListBase(base):
	pass


@params(api='gl', prms=['sync', 'flags', 'timeout'])
def glClientWaitSync(sync, flags, timeout):
	pass


@params(api='gl', prms=['texture', 'internalformat', 'buffer'])
def glTextureBuffer(texture, internalformat, buffer):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib4Nsv(index, v):
	pass


@params(api='gl', prms=['x', 'y', 'width', 'height', 'format', 'type', 'bufSize', 'data'])
def glReadnPixels(x, y, width, height, format, type, bufSize, data):
	pass


@params(api='gl', prms=['srcName', 'srcTarget', 'srcLevel', 'srcX', 'srcY', 'srcZ', 'dstName', 'dstTarget', 'dstLevel', 'dstX', 'dstY', 'dstZ', 'srcWidth', 'srcHeight', 'srcDepth'])
def glCopyImageSubData(srcName, srcTarget, srcLevel, srcX, srcY, srcZ, dstName, dstTarget, dstLevel, dstX, dstY, dstZ, srcWidth, srcHeight, srcDepth):
	pass


@params(api='gl', prms=['shadertype', 'location', 'params'])
def glGetUniformSubroutineuiv(shadertype, location, params):
	pass


@params(api='gl', prms=['bindingindex', 'buffer', 'offset', 'stride'])
def glBindVertexBuffer(bindingindex, buffer, offset, stride):
	pass


@params(api='gl', prms=['source', 'type', 'id', 'severity', 'length', 'buf'])
def glDebugMessageInsert(source, type, id, severity, length, buf):
	pass


@params(api='gl', prms=['sampler'])
def glIsSampler(sampler):
	pass


@params(api='gl', prms=['target', 'level', 'xoffset', 'x', 'y', 'width'])
def glCopyTexSubImage1D(target, level, xoffset, x, y, width):
	pass


@params(api='gl', prms=['s'])
def glTexCoord1i(s):
	pass


@params(api='gl', prms=['target'])
def glCheckFramebufferStatus(target):
	pass


@params(api='gl', prms=['s'])
def glTexCoord1d(s):
	pass


@params(api='gl', prms=['s'])
def glTexCoord1f(s):
	pass


@params(api='gl', prms=['unit', 'texture', 'level', 'layered', 'layer', 'access', 'format'])
def glBindImageTexture(unit, texture, level, layered, layer, access, format):
	pass


@params(api='gl', prms=['program', 'count', 'constvaryings', 'bufferMode'])
def glTransformFeedbackVaryings(program, count, constvaryings, bufferMode):
	pass


@params(api='gl', prms=['mode', 'start', 'end', 'count', 'type', 'indices'])
def glDrawRangeElements(mode, start, end, count, type, indices):
	pass


@params(api='gl', prms=['target', 'index', 'buffer'])
def glBindBufferBase(target, index, buffer):
	pass


@params(api='gl', prms=['v'])
def glColor3bv(v):
	pass


@params(api='gl', prms=['n', 'samplers'])
def glCreateSamplers(n, samplers):
	pass


@params(api='gl', prms=['mode', 'first', 'count', 'drawcount'])
def glMultiDrawArrays(mode, first, count, drawcount):
	pass


@params(api='gl', prms=['type', 'coords'])
def glTexCoordP4ui(type, coords):
	pass


@params(api='gl', prms=['index', 'x', 'y', 'z'])
def glVertexAttribI3ui(index, x, y, z):
	pass


@params(api='gl', prms=['attribindex', 'size', 'type', 'relativeoffset'])
def glVertexAttribIFormat(attribindex, size, type, relativeoffset):
	pass


@params(api='gl', prms=['n', 'framebuffers'])
def glCreateFramebuffers(n, framebuffers):
	pass


@params(api='gl', prms=['red', 'green', 'blue', 'alpha'])
def glClearAccum(red, green, blue, alpha):
	pass


@params(api='gl', prms=['target', 'id'])
def glBeginQuery(target, id):
	pass


@params(api='gl', prms=['target', 'u1', 'u2', 'ustride', 'uorder', 'v1', 'v2', 'vstride', 'vorder', 'points'])
def glMap2d(target, u1, u2, ustride, uorder, v1, v2, vstride, vorder, points):
	pass


@params(api='gl', prms=['target', 'u1', 'u2', 'ustride', 'uorder', 'v1', 'v2', 'vstride', 'vorder', 'points'])
def glMap2f(target, u1, u2, ustride, uorder, v1, v2, vstride, vorder, points):
	pass


@params(api='gl', prms=['location', 'count', 'transpose', 'value'])
def glUniformMatrix2x4fv(location, count, transpose, value):
	pass


@params(api='gl', prms=['index', 'n', 'f'])
def glDepthRangeIndexed(index, n, f):
	pass


@params(api='gl', prms=[])
def glGetError():
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glGetTexEnviv(target, pname, params):
	pass


@params(api='gl', prms=['u'])
def glEvalCoord1d(u):
	pass


@params(api='gl', prms=['target', 'level', 'pname', 'params'])
def glGetTexLevelParameterfv(target, level, pname, params):
	pass


@params(api='gl', prms=['u'])
def glEvalCoord1f(u):
	pass


@params(api='gl', prms=['map', 'mapsize', 'values'])
def glPixelMapfv(map, mapsize, values):
	pass


@params(api='gl', prms=['map', 'values'])
def glGetPixelMapusv(map, values):
	pass


@params(api='gl', prms=['op', 'value'])
def glAccum(op, value):
	pass


@params(api='gl', prms=['v'])
def glRasterPos3sv(v):
	pass


@params(api='gl', prms=['program', 'location', 'v0', 'v1'])
def glProgramUniform2ui(program, location, v0, v1):
	pass


@params(api='gl', prms=['program', 'location', 'v0', 'v1', 'v2', 'v3'])
def glProgramUniform4ui(program, location, v0, v1, v2, v3):
	pass


@params(api='gl', prms=['buffer', 'size', 'data', 'usage'])
def glNamedBufferData(buffer, size, data, usage):
	pass


@params(api='gl', prms=['buffer', 'internalformat', 'offset', 'size', 'format', 'type', 'data'])
def glClearNamedBufferSubData(buffer, internalformat, offset, size, format, type, data):
	pass


@params(api='gl', prms=['v1', 'v2'])
def glRectsv(v1, v2):
	pass


@params(api='gl', prms=['coord', 'pname', 'params'])
def glGetTexGeniv(coord, pname, params):
	pass


@params(api='gl', prms=['pname', 'param'])
def glPixelStorei(pname, param):
	pass


@params(api='gl', prms=['texture', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth', 'bufSize', 'pixels'])
def glGetCompressedTextureSubImage(texture, level, xoffset, yoffset, zoffset, width, height, depth, bufSize, pixels):
	pass


@params(api='gl', prms=['flag'])
def glDepthMask(flag):
	pass


@params(api='gl', prms=['pname', 'values'])
def glPatchParameterfv(pname, values):
	pass


@params(api='gl', prms=['texture', 'levels', 'internalformat', 'width', 'height'])
def glTextureStorage2D(texture, levels, internalformat, width, height):
	pass


@params(api='gl', prms=['target', 'internalformat', 'buffer', 'offset', 'size'])
def glTexBufferRange(target, internalformat, buffer, offset, size):
	pass


@params(api='gl', prms=['v'])
def glRasterPos4fv(v):
	pass


@params(api='gl', prms=['u'])
def glEvalCoord1dv(u):
	pass


@params(api='gl', prms=[])
def glPopClientAttrib():
	pass


@params(api='gl', prms=['vaobj', 'first', 'count', 'buffers', 'offsets', 'strides'])
def glVertexArrayVertexBuffers(vaobj, first, count, buffers, offsets, strides):
	pass


@params(api='gl', prms=['program', 'pname', 'value'])
def glProgramParameteri(program, pname, value):
	pass


@params(api='gl', prms=['target', 'query', 'v'])
def glGetMapfv(target, query, v):
	pass


@params(api='gl', prms=['v'])
def glRasterPos2fv(v):
	pass


@params(api='gl', prms=['barriers'])
def glMemoryBarrierByRegion(barriers):
	pass


@params(api='gl', prms=['v'])
def glVertex2sv(v):
	pass


@params(api='gl', prms=['v'])
def glWindowPos2sv(v):
	pass


@params(api='gl', prms=['type'])
def glCreateShader(type):
	pass


@params(api='gl', prms=['n', 'renderbuffers'])
def glGenRenderbuffers(n, renderbuffers):
	pass


@params(api='gl', prms=['target', 'level', 'xoffset', 'yoffset', 'x', 'y', 'width', 'height'])
def glCopyTexSubImage2D(target, level, xoffset, yoffset, x, y, width, height):
	pass


@params(api='gl', prms=['sfactorRGB', 'dfactorRGB', 'sfactorAlpha', 'dfactorAlpha'])
def glBlendFuncSeparate(sfactorRGB, dfactorRGB, sfactorAlpha, dfactorAlpha):
	pass


@params(api='gl', prms=['v'])
def glTexCoord2fv(v):
	pass


@params(api='gl', prms=['v'])
def glTexCoord4fv(v):
	pass


@params(api='gl', prms=['size'])
def glPointSize(size):
	pass


@params(api='gl', prms=['unit', 'texture'])
def glBindTextureUnit(unit, texture):
	pass


@params(api='gl', prms=['pipeline', 'bufSize', 'length', 'infoLog'])
def glGetProgramPipelineInfoLog(pipeline, bufSize, length, infoLog):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib4Nuiv(index, v):
	pass


@params(api='gl', prms=['sync', 'flags', 'timeout'])
def glWaitSync(sync, flags, timeout):
	pass


@params(api='gl', prms=['buf', 'modeRGB', 'modeAlpha'])
def glBlendEquationSeparatei(buf, modeRGB, modeAlpha):
	pass


@params(api='gl', prms=['location', 'x', 'y', 'z'])
def glUniform3d(location, x, y, z):
	pass


@params(api='gl', prms=['location', 'v0', 'v1', 'v2'])
def glUniform3f(location, v0, v1, v2):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform3uiv(program, location, count, value):
	pass


@params(api='gl', prms=['program', 'name'])
def glGetFragDataIndex(program, name):
	pass


@params(api='gl', prms=['v'])
def glColor3sv(v):
	pass


@params(api='gl', prms=['v'])
def glVertex4sv(v):
	pass


@params(api='gl', prms=['id', 'target'])
def glQueryCounter(id, target):
	pass


@params(api='gl', prms=['n', 'framebuffers'])
def glDeleteFramebuffers(n, framebuffers):
	pass


@params(api='gl', prms=['mode', 'first', 'count'])
def glDrawArrays(mode, first, count):
	pass


@params(api='gl', prms=['s', 't', 'r', 'q'])
def glTexCoord4f(s, t, r, q):
	pass


@params(api='gl', prms=['mask'])
def glClear(mask):
	pass


@params(api='gl', prms=['target', 'n', 'ids'])
def glCreateQueries(target, n, ids):
	pass


@params(api='gl', prms=['sampler', 'pname', 'params'])
def glGetSamplerParameterfv(sampler, pname, params):
	pass


@params(api='gl', prms=['x', 'y', 'z'])
def glTranslatef(x, y, z):
	pass


@params(api='gl', prms=['index', 'x', 'y', 'z', 'w'])
def glVertexAttrib4Nub(index, x, y, z, w):
	pass


@params(api='gl', prms=['x', 'y', 'z'])
def glTranslated(x, y, z):
	pass


@params(api='gl', prms=['sampler', 'pname', 'param'])
def glSamplerParameterIiv(sampler, pname, param):
	pass


@params(api='gl', prms=['mode', 'type', 'indirect'])
def glDrawElementsIndirect(mode, type, indirect):
	pass


@params(api='gl', prms=['v'])
def glSecondaryColor3bv(v):
	pass


@params(api='gl', prms=['s', 't', 'r', 'q'])
def glTexCoord4s(s, t, r, q):
	pass


@params(api='gl', prms=['id', 'pname', 'params'])
def glGetQueryObjecti64v(id, pname, params):
	pass


@params(api='gl', prms=['program', 'uniformCount', 'constuniformNames', 'uniformIndices'])
def glGetUniformIndices(program, uniformCount, constuniformNames, uniformIndices):
	pass


@params(api='gl', prms=['v'])
def glVertex3iv(v):
	pass


@params(api='gl', prms=['coord', 'pname', 'params'])
def glTexGenfv(coord, pname, params):
	pass


@params(api='gl', prms=['first', 'count', 'buffers', 'offsets', 'strides'])
def glBindVertexBuffers(first, count, buffers, offsets, strides):
	pass


@params(api='gl', prms=['face', 'pname', 'param'])
def glMateriali(face, pname, param):
	pass


@params(api='gl', prms=['array'])
def glIsVertexArray(array):
	pass


@params(api='gl', prms=['index'])
def glDisableVertexAttribArray(index):
	pass


@params(api='gl', prms=['program', 'storageBlockIndex', 'storageBlockBinding'])
def glShaderStorageBlockBinding(program, storageBlockIndex, storageBlockBinding):
	pass


@params(api='gl', prms=['face', 'pname', 'param'])
def glMaterialf(face, pname, param):
	pass


@params(api='gl', prms=['texture', 'levels', 'internalformat', 'width'])
def glTextureStorage1D(texture, levels, internalformat, width):
	pass


@params(api='gl', prms=['program', 'programInterface', 'pname', 'params'])
def glGetProgramInterfaceiv(program, programInterface, pname, params):
	pass


@params(api='gl', prms=['buffer', 'access'])
def glMapNamedBuffer(buffer, access):
	pass


@params(api='gl', prms=['program', 'location', 'bufSize', 'params'])
def glGetnUniformdv(program, location, bufSize, params):
	pass


@params(api='gl', prms=['target', 'first', 'count', 'buffers'])
def glBindBuffersBase(target, first, count, buffers):
	pass


@params(api='gl', prms=['index', 'pname', 'params'])
def glGetVertexAttribIiv(index, pname, params):
	pass


@params(api='gl', prms=['type', 'value'])
def glVertexP4uiv(type, value):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttribL4dv(index, v):
	pass


@params(api='gl', prms=['pname', 'value'])
def glPatchParameteri(pname, value):
	pass


@params(api='gl', prms=['target', 'u1', 'u2', 'stride', 'order', 'points'])
def glMap1d(target, u1, u2, stride, order, points):
	pass


@params(api='gl', prms=['target', 'u1', 'u2', 'stride', 'order', 'points'])
def glMap1f(target, u1, u2, stride, order, points):
	pass


@params(api='gl', prms=['framebuffer', 'attachment', 'pname', 'params'])
def glGetNamedFramebufferAttachmentParameteriv(framebuffer, attachment, pname, params):
	pass


@params(api='gl', prms=['target', 'format', 'type', 'rowBufSize', 'row', 'columnBufSize', 'column', 'span'])
def glGetnSeparableFilter(target, format, type, rowBufSize, row, columnBufSize, column, span):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib4sv(index, v):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform1dv(program, location, count, value):
	pass


@params(api='gl', prms=['light', 'pname', 'param'])
def glLighti(light, pname, param):
	pass


@params(api='gl', prms=['target', 'level', 'internalformat', 'width', 'border', 'format', 'type', 'pixels'])
def glTexImage1D(target, level, internalformat, width, border, format, type, pixels):
	pass


@params(api='gl', prms=['light', 'pname', 'param'])
def glLightf(light, pname, param):
	pass


@params(api='gl', prms=['value', 'invert'])
def glSampleCoverage(value, invert):
	pass


@params(api='gl', prms=['v'])
def glSecondaryColor3usv(v):
	pass


@params(api='gl', prms=['xfb', 'pname', 'index', 'param'])
def glGetTransformFeedbacki_v(xfb, pname, index, param):
	pass


@params(api='gl', prms=['location', 'v0', 'v1'])
def glUniform2i(location, v0, v1):
	pass


@params(api='gl', prms=['un', 'u1', 'u2', 'vn', 'v1', 'v2'])
def glMapGrid2f(un, u1, u2, vn, v1, v2):
	pass


@params(api='gl', prms=['index', 'x'])
def glVertexAttribL1d(index, x):
	pass


@params(api='gl', prms=['target', 'attachment', 'texture', 'level', 'layer'])
def glFramebufferTextureLayer(target, attachment, texture, level, layer):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform2fv(program, location, count, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix2x4dv(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['target', 'pname', 'param'])
def glTexEnvf(target, pname, param):
	pass


@params(api='gl', prms=['target', 'index', 'data'])
def glGetInteger64i_v(target, index, data):
	pass


@params(api='gl', prms=['target', 'pname', 'param'])
def glTexEnvi(target, pname, param):
	pass


@params(api='gl', prms=['srcX0', 'srcY0', 'srcX1', 'srcY1', 'dstX0', 'dstY0', 'dstX1', 'dstY1', 'mask', 'filter'])
def glBlitFramebuffer(srcX0, srcY0, srcX1, srcY1, dstX0, dstY0, dstX1, dstY1, mask, filter):
	pass


@params(api='gl', prms=['target', 'index'])
def glIsEnabledi(target, index):
	pass


@params(api='gl', prms=['s', 't'])
def glTexCoord2i(s, t):
	pass


@params(api='gl', prms=['index', 'type', 'normalized', 'value'])
def glVertexAttribP2ui(index, type, normalized, value):
	pass


@params(api='gl', prms=['target', 'query', 'v'])
def glGetMapiv(target, query, v):
	pass


@params(api='gl', prms=['ptr', 'length', 'label'])
def glObjectPtrLabel(ptr, length, label):
	pass


@params(api='gl', prms=['count', 'bufSize', 'sources', 'types', 'ids', 'severities', 'lengths', 'messageLog'])
def glGetDebugMessageLog(count, bufSize, sources, types, ids, severities, lengths, messageLog):
	pass


@params(api='gl', prms=['program', 'color', 'name'])
def glBindFragDataLocation(program, color, name):
	pass


@params(api='gl', prms=['v'])
def glSecondaryColor3ubv(v):
	pass


@params(api='gl', prms=['pname', 'param'])
def glLightModelf(pname, param):
	pass


@params(api='gl', prms=['mode', 'type', 'indirect', 'drawcount', 'stride'])
def glMultiDrawElementsIndirect(mode, type, indirect, drawcount, stride):
	pass


@params(api='gl', prms=['n', 'type', 'lists'])
def glCallLists(n, type, lists):
	pass


@params(api='gl', prms=['left', 'right', 'bottom', 'top', 'zNear', 'zFar'])
def glFrustum(left, right, bottom, top, zNear, zFar):
	pass


@params(api='gl', prms=['s', 't', 'r'])
def glTexCoord3i(s, t, r):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttribI3uiv(index, v):
	pass


@params(api='gl', prms=['source', 'id', 'length', 'message'])
def glPushDebugGroup(source, id, length, message):
	pass


@params(api='gl', prms=['texture', 'type', 'coords'])
def glMultiTexCoordP1uiv(texture, type, coords):
	pass


@params(api='gl', prms=['target', 'level', 'xoffset', 'yoffset', 'zoffset', 'x', 'y', 'width', 'height'])
def glCopyTexSubImage3D(target, level, xoffset, yoffset, zoffset, x, y, width, height):
	pass


@params(api='gl', prms=['program', 'uniformBlockIndex', 'bufSize', 'length', 'uniformBlockName'])
def glGetActiveUniformBlockName(program, uniformBlockIndex, bufSize, length, uniformBlockName):
	pass


@params(api='gl', prms=['s', 't', 'r'])
def glTexCoord3s(s, t, r):
	pass


@params(api='gl', prms=['n', 'textures', 'residences'])
def glAreTexturesResident(n, textures, residences):
	pass


@params(api='gl', prms=['program', 'location', 'v0', 'v1'])
def glProgramUniform2d(program, location, v0, v1):
	pass


@params(api='gl', prms=['program', 'location', 'v0', 'v1'])
def glProgramUniform2f(program, location, v0, v1):
	pass


@params(api='gl', prms=['v'])
def glRasterPos4sv(v):
	pass


@params(api='gl', prms=['red', 'green', 'blue', 'alpha'])
def glColor4s(red, green, blue, alpha):
	pass


@params(api='gl', prms=['array'])
def glBindVertexArray(array):
	pass


@params(api='gl', prms=['red', 'green', 'blue', 'alpha'])
def glColor4b(red, green, blue, alpha):
	pass


@params(api='gl', prms=['red', 'green', 'blue', 'alpha'])
def glColor4f(red, green, blue, alpha):
	pass


@params(api='gl', prms=['red', 'green', 'blue', 'alpha'])
def glColor4d(red, green, blue, alpha):
	pass


@params(api='gl', prms=['red', 'green', 'blue', 'alpha'])
def glColor4i(red, green, blue, alpha):
	pass


@params(api='gl', prms=['buffer', 'offset', 'size', 'data'])
def glNamedBufferSubData(buffer, offset, size, data):
	pass


@params(api='gl', prms=['v'])
def glVertex2dv(v):
	pass


@params(api='gl', prms=['target', 'framebuffer'])
def glBindFramebuffer(target, framebuffer):
	pass


@params(api='gl', prms=['v1', 'v2'])
def glRectfv(v1, v2):
	pass


@params(api='gl', prms=['location', 'count', 'transpose', 'value'])
def glUniformMatrix2x4dv(location, count, transpose, value):
	pass


@params(api='gl', prms=['program', 'programInterface', 'name'])
def glGetProgramResourceLocationIndex(program, programInterface, name):
	pass


@params(api='gl', prms=['x', 'y', 'width', 'height'])
def glViewport(x, y, width, height):
	pass


@params(api='gl', prms=['renderbuffer'])
def glIsRenderbuffer(renderbuffer):
	pass


@params(api='gl', prms=['target', 'samples', 'internalformat', 'width', 'height', 'fixedsamplelocations'])
def glTexStorage2DMultisample(target, samples, internalformat, width, height, fixedsamplelocations):
	pass


@params(api='gl', prms=['program', 'shadertype', 'index', 'pname', 'values'])
def glGetActiveSubroutineUniformiv(program, shadertype, index, pname, values):
	pass


@params(api='gl', prms=['target', 'internalformat', 'buffer'])
def glTexBuffer(target, internalformat, buffer):
	pass


@params(api='gl', prms=['i'])
def glArrayElement(i):
	pass


@params(api='gl', prms=['program'])
def glValidateProgram(program):
	pass


@params(api='gl', prms=['pipeline', 'program'])
def glActiveShaderProgram(pipeline, program):
	pass


@params(api='gl', prms=['texture', 'type', 'coords'])
def glMultiTexCoordP2uiv(texture, type, coords):
	pass


@params(api='gl', prms=['x1', 'y1', 'x2', 'y2'])
def glRecti(x1, y1, x2, y2):
	pass


@params(api='gl', prms=['x1', 'y1', 'x2', 'y2'])
def glRectf(x1, y1, x2, y2):
	pass


@params(api='gl', prms=['x1', 'y1', 'x2', 'y2'])
def glRectd(x1, y1, x2, y2):
	pass


@params(api='gl', prms=['target', 'texture'])
def glBindTexture(target, texture):
	pass


@params(api='gl', prms=['x1', 'y1', 'x2', 'y2'])
def glRects(x1, y1, x2, y2):
	pass


@params(api='gl', prms=['program', 'shader'])
def glDetachShader(program, shader):
	pass


@params(api='gl', prms=['texture', 'level', 'xoffset', 'yoffset', 'width', 'height', 'format', 'type', 'pixels'])
def glTextureSubImage2D(texture, level, xoffset, yoffset, width, height, format, type, pixels):
	pass


@params(api='gl', prms=['program', 'programInterface', 'name'])
def glGetProgramResourceLocation(program, programInterface, name):
	pass


@params(api='gl', prms=['index', 'v'])
def glViewportIndexedfv(index, v):
	pass


@params(api='gl', prms=['mode', 'count', 'type', 'indices', 'basevertex'])
def glDrawElementsBaseVertex(mode, count, type, indices, basevertex):
	pass


@params(api='gl', prms=['target', 'internalformat', 'offset', 'size', 'format', 'type', 'data'])
def glClearBufferSubData(target, internalformat, offset, size, format, type, data):
	pass


@params(api='gl', prms=['target', 'levels', 'internalformat', 'width'])
def glTexStorage1D(target, levels, internalformat, width):
	pass


@params(api='gl', prms=['program', 'location', 'params'])
def glGetUniformiv(program, location, params):
	pass


@params(api='gl', prms=['target', 'buffer'])
def glBindBuffer(target, buffer):
	pass


@params(api='gl', prms=['location', 'v0', 'v1', 'v2', 'v3'])
def glUniform4ui(location, v0, v1, v2, v3):
	pass


@params(api='gl', prms=['coord', 'pname', 'param'])
def glTexGenf(coord, pname, param):
	pass


@params(api='gl', prms=['coord', 'pname', 'param'])
def glTexGend(coord, pname, param):
	pass


@params(api='gl', prms=['coord', 'pname', 'param'])
def glTexGeni(coord, pname, param):
	pass


@params(api='gl', prms=['index', 'left', 'bottom', 'width', 'height'])
def glScissorIndexed(index, left, bottom, width, height):
	pass


@params(api='gl', prms=['v'])
def glRasterPos4dv(v):
	pass


@params(api='gl', prms=['v'])
def glRasterPos2dv(v):
	pass


@params(api='gl', prms=['v'])
def glTexCoord2iv(v):
	pass


@params(api='gl', prms=['type', 'count', 'conststrings'])
def glCreateShaderProgramv(type, count, conststrings):
	pass


@params(api='gl', prms=['id', 'pname', 'params'])
def glGetQueryObjectiv(id, pname, params):
	pass


@params(api='gl', prms=['x', 'y'])
def glVertex2s(x, y):
	pass


@params(api='gl', prms=['target'])
def glGenerateMipmap(target):
	pass


@params(api='gl', prms=['texture', 'level', 'xoffset', 'yoffset', 'width', 'height', 'format', 'imageSize', 'data'])
def glCompressedTextureSubImage2D(texture, level, xoffset, yoffset, width, height, format, imageSize, data):
	pass


@params(api='gl', prms=['list', 'range'])
def glDeleteLists(list, range):
	pass


@params(api='gl', prms=['pname', 'param'])
def glPointParameteri(pname, param):
	pass


@params(api='gl', prms=['v'])
def glColor4iv(v):
	pass


@params(api='gl', prms=['target'])
def glUnmapBuffer(target):
	pass


@params(api='gl', prms=['pname', 'param'])
def glPointParameterf(pname, param):
	pass


@params(api='gl', prms=['s', 't'])
def glTexCoord2s(s, t):
	pass


@params(api='gl', prms=['v'])
def glTexCoord4dv(v):
	pass


@params(api='gl', prms=['v'])
def glNormal3dv(v):
	pass


@params(api='gl', prms=[])
def glReleaseShaderCompiler():
	pass


@params(api='gl', prms=['v'])
def glTexCoord1dv(v):
	pass


@params(api='gl', prms=['x', 'y', 'width', 'height', 'format', 'type', 'pixels'])
def glReadPixels(x, y, width, height, format, type, pixels):
	pass


@params(api='gl', prms=['renderbuffer', 'samples', 'internalformat', 'width', 'height'])
def glNamedRenderbufferStorageMultisample(renderbuffer, samples, internalformat, width, height):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttribI3iv(index, v):
	pass


@params(api='gl', prms=['mode'])
def glShadeModel(mode):
	pass


@params(api='gl', prms=['un', 'u1', 'u2'])
def glMapGrid1d(un, u1, u2):
	pass


@params(api='gl', prms=['framebuffer', 'numAttachments', 'attachments'])
def glInvalidateNamedFramebufferData(framebuffer, numAttachments, attachments):
	pass


@params(api='gl', prms=['v1', 'v2'])
def glRectiv(v1, v2):
	pass


@params(api='gl', prms=['type', 'color'])
def glColorP4ui(type, color):
	pass


@params(api='gl', prms=['pipeline', 'stages', 'program'])
def glUseProgramStages(pipeline, stages, program):
	pass


@params(api='gl', prms=['v'])
def glRasterPos3dv(v):
	pass


@params(api='gl', prms=['src'])
def glReadBuffer(src):
	pass


@params(api='gl', prms=['v'])
def glColor4ubv(v):
	pass


@params(api='gl', prms=['target', 'offset', 'size', 'data'])
def glGetBufferSubData(target, offset, size, data):
	pass


@params(api='gl', prms=['index', 'pname', 'params'])
def glGetVertexAttribLdv(index, pname, params):
	pass


@params(api='gl', prms=['program', 'location', 'bufSize', 'params'])
def glGetnUniformuiv(program, location, bufSize, params):
	pass


@params(api='gl', prms=['n', 'buffers'])
def glGenBuffers(n, buffers):
	pass


@params(api='gl', prms=['framebuffer', 'buffer', 'drawbuffer', 'value'])
def glClearNamedFramebufferiv(framebuffer, buffer, drawbuffer, value):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttribI2iv(index, v):
	pass


@params(api='gl', prms=['framebuffer'])
def glIsFramebuffer(framebuffer):
	pass


@params(api='gl', prms=['type', 'coords'])
def glTexCoordP4uiv(type, coords):
	pass


@params(api='gl', prms=['coord', 'pname', 'params'])
def glTexGendv(coord, pname, params):
	pass


@params(api='gl', prms=['type', 'value'])
def glVertexP2uiv(type, value):
	pass


@params(api='gl', prms=['s', 't'])
def glTexCoord2d(s, t):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glGetBufferParameteri64v(target, pname, params):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform4dv(program, location, count, value):
	pass


@params(api='gl', prms=['s', 't'])
def glTexCoord2f(s, t):
	pass


@params(api='gl', prms=['target', 'v'])
def glMultiTexCoord3fv(target, v):
	pass


@params(api='gl', prms=['n', 'renderbuffers'])
def glCreateRenderbuffers(n, renderbuffers):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib4Nusv(index, v):
	pass


@params(api='gl', prms=['func'])
def glDepthFunc(func):
	pass


@params(api='gl', prms=['sampler', 'pname', 'param'])
def glSamplerParameterf(sampler, pname, param):
	pass


@params(api='gl', prms=['buf', 'src', 'dst'])
def glBlendFunci(buf, src, dst):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib3dv(index, v):
	pass


@params(api='gl', prms=['target', 'size', 'data', 'flags'])
def glBufferStorage(target, size, data, flags):
	pass


@params(api='gl', prms=['target', 'index', 'data'])
def glGetFloati_v(target, index, data):
	pass


@params(api='gl', prms=['program', 'name'])
def glGetUniformLocation(program, name):
	pass


@params(api='gl', prms=['framebuffer', 'n', 'bufs'])
def glNamedFramebufferDrawBuffers(framebuffer, n, bufs):
	pass


@params(api='gl', prms=['location', 'count', 'value'])
def glUniform4fv(location, count, value):
	pass


@params(api='gl', prms=['index', 'type', 'normalized', 'value'])
def glVertexAttribP4uiv(index, type, normalized, value):
	pass


@params(api='gl', prms=['texture', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth', 'format', 'imageSize', 'data'])
def glCompressedTextureSubImage3D(texture, level, xoffset, yoffset, zoffset, width, height, depth, format, imageSize, data):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib4Nbv(index, v):
	pass


@params(api='gl', prms=[])
def glEndConditionalRender():
	pass


@params(api='gl', prms=['array'])
def glEnableClientState(array):
	pass


@params(api='gl', prms=['target', 'v'])
def glMultiTexCoord2sv(target, v):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform2uiv(program, location, count, value):
	pass


@params(api='gl', prms=['id', 'pname', 'params'])
def glGetQueryObjectuiv(id, pname, params):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib4iv(index, v):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform1uiv(program, location, count, value):
	pass


@params(api='gl', prms=['target', 'attachment', 'texture', 'level'])
def glFramebufferTexture(target, attachment, texture, level):
	pass


@params(api='gl', prms=['coord', 'pname', 'params'])
def glGetTexGendv(coord, pname, params):
	pass


@params(api='gl', prms=['v'])
def glColor3usv(v):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix2x4fv(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform2dv(program, location, count, value):
	pass


@params(api='gl', prms=['v'])
def glRasterPos2sv(v):
	pass


@params(api='gl', prms=['v'])
def glTexCoord1sv(v):
	pass


@params(api='gl', prms=['x', 'y'])
def glVertex2i(x, y):
	pass


@params(api='gl', prms=['pname', 'data'])
def glGetFloatv(pname, data):
	pass


@params(api='gl', prms=['x', 'y', 'z'])
def glWindowPos3f(x, y, z):
	pass


@params(api='gl', prms=['type', 'color'])
def glSecondaryColorP3uiv(type, color):
	pass


@params(api='gl', prms=['pname', 'data'])
def glGetIntegerv(pname, data):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix3dv(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['id'])
def glIsQuery(id):
	pass


@params(api='gl', prms=['target', 'level', 'internalformat', 'width', 'height', 'border', 'format', 'type', 'pixels'])
def glTexImage2D(target, level, internalformat, width, height, border, format, type, pixels):
	pass


@params(api='gl', prms=['width', 'height', 'format', 'type', 'pixels'])
def glDrawPixels(width, height, format, type, pixels):
	pass


@params(api='gl', prms=['m'])
def glMultMatrixd(m):
	pass


@params(api='gl', prms=['m'])
def glMultMatrixf(m):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib4Nubv(index, v):
	pass


@params(api='gl', prms=['v'])
def glColor4usv(v):
	pass


@params(api='gl', prms=['un', 'u1', 'u2'])
def glMapGrid1f(un, u1, u2):
	pass


@params(api='gl', prms=['mask'])
def glPolygonStipple(mask):
	pass


@params(api='gl', prms=['format', 'stride', 'pointer'])
def glInterleavedArrays(format, stride, pointer):
	pass


@params(api='gl', prms=['program', 'shadertype', 'name'])
def glGetSubroutineUniformLocation(program, shadertype, name):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glGetFramebufferParameteriv(target, pname, params):
	pass


@params(api='gl', prms=['map', 'mapsize', 'values'])
def glPixelMapusv(map, mapsize, values):
	pass


@params(api='gl', prms=['sampler', 'pname', 'params'])
def glGetSamplerParameteriv(sampler, pname, params):
	pass


@params(api='gl', prms=['readTarget', 'writeTarget', 'readOffset', 'writeOffset', 'size'])
def glCopyBufferSubData(readTarget, writeTarget, readOffset, writeOffset, size):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttribI1uiv(index, v):
	pass


@params(api='gl', prms=['v'])
def glColor3fv(v):
	pass


@params(api='gl', prms=['program', 'index', 'bufSize', 'length', 'size', 'type', 'name'])
def glGetActiveUniform(program, index, bufSize, length, size, type, name):
	pass


@params(api='gl', prms=['framebuffer', 'attachment', 'texture', 'level', 'layer'])
def glNamedFramebufferTextureLayer(framebuffer, attachment, texture, level, layer):
	pass


@params(api='gl', prms=['index', 'x', 'y', 'z'])
def glVertexAttribL3d(index, x, y, z):
	pass


@params(api='gl', prms=['v'])
def glTexCoord3sv(v):
	pass


@params(api='gl', prms=['value'])
def glMinSampleShading(value):
	pass


@params(api='gl', prms=['v'])
def glVertex2fv(v):
	pass


@params(api='gl', prms=['target', 'attachment', 'renderbuffertarget', 'renderbuffer'])
def glFramebufferRenderbuffer(target, attachment, renderbuffertarget, renderbuffer):
	pass


@params(api='gl', prms=['target', 'index', 'data'])
def glGetDoublei_v(target, index, data):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib1sv(index, v):
	pass


@params(api='gl', prms=['unit', 'sampler'])
def glBindSampler(unit, sampler):
	pass


@params(api='gl', prms=['width'])
def glLineWidth(width):
	pass


@params(api='gl', prms=['target', 'index', 'data'])
def glGetIntegeri_v(target, index, data):
	pass


@params(api='gl', prms=['program', 'index', 'bufSize', 'length', 'size', 'type', 'name'])
def glGetTransformFeedbackVarying(program, index, bufSize, length, size, type, name):
	pass


@params(api='gl', prms=['v'])
def glWindowPos2iv(v):
	pass


@params(api='gl', prms=['pname', 'params'])
def glFogiv(pname, params):
	pass


@params(api='gl', prms=['pname', 'params'])
def glLightModeliv(pname, params):
	pass


@params(api='gl', prms=['n', 'f'])
def glDepthRangef(n, f):
	pass


@params(api='gl', prms=['target', 'index'])
def glEnablei(target, index):
	pass


@params(api='gl', prms=['u'])
def glEvalCoord1fv(u):
	pass


@params(api='gl', prms=['maskNumber', 'mask'])
def glSampleMaski(maskNumber, mask):
	pass


@params(api='gl', prms=['location', 'count', 'transpose', 'value'])
def glUniformMatrix3x2fv(location, count, transpose, value):
	pass


@params(api='gl', prms=['target', 'internalformat', 'pname', 'bufSize', 'params'])
def glGetInternalformativ(target, internalformat, pname, bufSize, params):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib2dv(index, v):
	pass


@params(api='gl', prms=['flag'])
def glEdgeFlag(flag):
	pass


@params(api='gl', prms=['program', 'location', 'v0'])
def glProgramUniform1ui(program, location, v0):
	pass


@params(api='gl', prms=['x', 'y', 'z'])
def glVertex3d(x, y, z):
	pass


@params(api='gl', prms=['x', 'y', 'z'])
def glVertex3f(x, y, z):
	pass


@params(api='gl', prms=['x', 'y', 'z'])
def glVertex3s(x, y, z):
	pass


@params(api='gl', prms=['type', 'coords'])
def glTexCoordP2ui(type, coords):
	pass


@params(api='gl', prms=['index', 'r', 'g', 'b', 'a'])
def glColorMaski(index, r, g, b, a):
	pass


@params(api='gl', prms=['readBuffer', 'writeBuffer', 'readOffset', 'writeOffset', 'size'])
def glCopyNamedBufferSubData(readBuffer, writeBuffer, readOffset, writeOffset, size):
	pass


@params(api='gl', prms=['target', 'levels', 'internalformat', 'width', 'height', 'depth'])
def glTexStorage3D(target, levels, internalformat, width, height, depth):
	pass


@params(api='gl', prms=['texture', 'pname', 'param'])
def glTextureParameteriv(texture, pname, param):
	pass


@params(api='gl', prms=['location', 'count', 'transpose', 'value'])
def glUniformMatrix3x4fv(location, count, transpose, value):
	pass


@params(api='gl', prms=['type', 'stride', 'pointer'])
def glNormalPointer(type, stride, pointer):
	pass


@params(api='gl', prms=['framebuffer', 'attachment', 'texture', 'level'])
def glNamedFramebufferTexture(framebuffer, attachment, texture, level):
	pass


@params(api='gl', prms=['token'])
def glPassThrough(token):
	pass


@params(api='gl', prms=['type', 'color'])
def glSecondaryColorP3ui(type, color):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix4x3fv(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['mode'])
def glBegin(mode):
	pass


@params(api='gl', prms=['u'])
def glEvalCoord2dv(u):
	pass


@params(api='gl', prms=['v'])
def glColor3ubv(v):
	pass


@params(api='gl', prms=['type', 'value'])
def glVertexP3ui(type, value):
	pass


@params(api='gl', prms=['light', 'pname', 'params'])
def glLightfv(light, pname, params):
	pass


@params(api='gl', prms=['program', 'uniformIndex', 'bufSize', 'length', 'uniformName'])
def glGetActiveUniformName(program, uniformIndex, bufSize, length, uniformName):
	pass


@params(api='gl', prms=['target', 'attachment', 'pname', 'params'])
def glGetFramebufferAttachmentParameteriv(target, attachment, pname, params):
	pass


@params(api='gl', prms=['target', 's', 't'])
def glMultiTexCoord2f(target, s, t):
	pass


@params(api='gl', prms=['framebuffer', 'buf'])
def glNamedFramebufferDrawBuffer(framebuffer, buf):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glTexParameteriv(target, pname, params):
	pass


@params(api='gl', prms=['vaobj', 'bindingindex', 'buffer', 'offset', 'stride'])
def glVertexArrayVertexBuffer(vaobj, bindingindex, buffer, offset, stride):
	pass


@params(api='gl', prms=['target', 'level', 'format', 'type', 'pixels'])
def glGetTexImage(target, level, format, type, pixels):
	pass


@params(api='gl', prms=['xfb', 'index', 'buffer'])
def glTransformFeedbackBufferBase(xfb, index, buffer):
	pass


@params(api='gl', prms=['c'])
def glIndexsv(c):
	pass


@params(api='gl', prms=['type', 'coords'])
def glTexCoordP3uiv(type, coords):
	pass


@params(api='gl', prms=['width', 'height', 'xorig', 'yorig', 'xmove', 'ymove', 'bitmap'])
def glBitmap(width, height, xorig, yorig, xmove, ymove, bitmap):
	pass


@params(api='gl', prms=['buffer', 'offset', 'size', 'data'])
def glGetNamedBufferSubData(buffer, offset, size, data):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform2iv(program, location, count, value):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glGetQueryiv(target, pname, params):
	pass


@params(api='gl', prms=['xfb', 'pname', 'param'])
def glGetTransformFeedbackiv(xfb, pname, param):
	pass


@params(api='gl', prms=['s', 't', 'r', 'q'])
def glTexCoord4i(s, t, r, q):
	pass


@params(api='gl', prms=['identifier', 'name', 'length', 'label'])
def glObjectLabel(identifier, name, length, label):
	pass


@params(api='gl', prms=['pname', 'params'])
def glPointParameteriv(pname, params):
	pass


@params(api='gl', prms=['v'])
def glNormal3fv(v):
	pass


@params(api='gl', prms=['v'])
def glTexCoord1fv(v):
	pass


@params(api='gl', prms=['target', 'v'])
def glMultiTexCoord1dv(target, v):
	pass


@params(api='gl', prms=['v'])
def glTexCoord3fv(v):
	pass


@params(api='gl', prms=['texture', 'type', 'coords'])
def glMultiTexCoordP3uiv(texture, type, coords):
	pass


@params(api='gl', prms=['index', 'type', 'normalized', 'value'])
def glVertexAttribP3ui(index, type, normalized, value):
	pass


@params(api='gl', prms=['near', 'far'])
def glDepthRange(near, far):
	pass


@params(api='gl', prms=['buf'])
def glDrawBuffer(buf):
	pass


@params(api='gl', prms=['map', 'bufSize', 'values'])
def glGetnPixelMapusv(map, bufSize, values):
	pass


@params(api='gl', prms=['v'])
def glRasterPos3fv(v):
	pass


@params(api='gl', prms=['buffer', 'drawbuffer', 'value'])
def glClearBufferuiv(buffer, drawbuffer, value):
	pass


@params(api='gl', prms=['target', 'internalformat', 'pname', 'bufSize', 'params'])
def glGetInternalformati64v(target, internalformat, pname, bufSize, params):
	pass


@params(api='gl', prms=['c'])
def glClearIndex(c):
	pass


@params(api='gl', prms=['index', 'size', 'type', 'stride', 'pointer'])
def glVertexAttribIPointer(index, size, type, stride, pointer):
	pass


@params(api='gl', prms=[])
def glFlush():
	pass


@params(api='gl', prms=['mode', 'count', 'type', 'indices', 'instancecount', 'basevertex', 'baseinstance'])
def glDrawElementsInstancedBaseVertexBaseInstance(mode, count, type, indices, instancecount, basevertex, baseinstance):
	pass


@params(api='gl', prms=['target', 'level', 'pname', 'params'])
def glGetTexLevelParameteriv(target, level, pname, params):
	pass


@params(api='gl', prms=['n', 'textures', 'priorities'])
def glPrioritizeTextures(n, textures, priorities):
	pass


@params(api='gl', prms=['size', 'buffer'])
def glSelectBuffer(size, buffer):
	pass


@params(api='gl', prms=['target', 'samples', 'internalformat', 'width', 'height', 'depth', 'fixedsamplelocations'])
def glTexStorage3DMultisample(target, samples, internalformat, width, height, depth, fixedsamplelocations):
	pass


@params(api='gl', prms=['target', 'clamp'])
def glClampColor(target, clamp):
	pass


@params(api='gl', prms=['s'])
def glClearStencil(s):
	pass


@params(api='gl', prms=['type', 'coords'])
def glTexCoordP1uiv(type, coords):
	pass


@params(api='gl', prms=['texture'])
def glIsTexture(texture):
	pass


@params(api='gl', prms=['x', 'y'])
def glVertex2f(x, y):
	pass


@params(api='gl', prms=['x', 'y'])
def glVertex2d(x, y):
	pass


@params(api='gl', prms=['target', 'index', 'id'])
def glBeginQueryIndexed(target, index, id):
	pass


@params(api='gl', prms=['factor', 'units'])
def glPolygonOffset(factor, units):
	pass


@params(api='gl', prms=['target', 'level', 'internalformat', 'width', 'height', 'depth', 'border', 'format', 'type', 'pixels'])
def glTexImage3D(target, level, internalformat, width, height, depth, border, format, type, pixels):
	pass


@params(api='gl', prms=['program', 'pname', 'params'])
def glGetProgramiv(program, pname, params):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform4fv(program, location, count, value):
	pass


@params(api='gl', prms=['target', 'offset', 'length'])
def glFlushMappedBufferRange(target, offset, length):
	pass


@params(api='gl', prms=['target', 'levels', 'internalformat', 'width', 'height'])
def glTexStorage2D(target, levels, internalformat, width, height):
	pass


@params(api='gl', prms=['n', 'ids'])
def glGenQueries(n, ids):
	pass


@params(api='gl', prms=['map', 'values'])
def glGetPixelMapfv(map, values):
	pass


@params(api='gl', prms=['target', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth', 'format', 'type', 'pixels'])
def glTexSubImage3D(target, level, xoffset, yoffset, zoffset, width, height, depth, format, type, pixels):
	pass


@params(api='gl', prms=['count', 'samplers'])
def glDeleteSamplers(count, samplers):
	pass


@params(api='gl', prms=['texture', 'pname', 'params'])
def glGetTextureParameterfv(texture, pname, params):
	pass


@params(api='gl', prms=['mode'])
def glMatrixMode(mode):
	pass


@params(api='gl', prms=['first', 'count', 'textures'])
def glBindTextures(first, count, textures):
	pass


@params(api='gl', prms=['pname', 'data'])
def glGetDoublev(pname, data):
	pass


@params(api='gl', prms=['index', 'x'])
def glVertexAttrib1d(index, x):
	pass


@params(api='gl', prms=['location', 'count', 'value'])
def glUniform4dv(location, count, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform3dv(program, location, count, value):
	pass


@params(api='gl', prms=['buffer'])
def glInvalidateBufferData(buffer):
	pass


@params(api='gl', prms=['texture', 'level', 'xoffset', 'width', 'format', 'imageSize', 'data'])
def glCompressedTextureSubImage1D(texture, level, xoffset, width, format, imageSize, data):
	pass


@params(api='gl', prms=['texture', 'level', 'format', 'type', 'data'])
def glClearTexImage(texture, level, format, type, data):
	pass


@params(api='gl', prms=['location', 'count', 'value'])
def glUniform3fv(location, count, value):
	pass


@params(api='gl', prms=['texture', 'type', 'coords'])
def glMultiTexCoordP1ui(texture, type, coords):
	pass


@params(api='gl', prms=['xfb', 'pname', 'index', 'param'])
def glGetTransformFeedbacki64_v(xfb, pname, index, param):
	pass


@params(api='gl', prms=['mode', 'count', 'type', 'constindices', 'drawcount'])
def glMultiDrawElements(mode, count, type, constindices, drawcount):
	pass


@params(api='gl', prms=['n', 'bufs'])
def glDrawBuffers(n, bufs):
	pass


@params(api='gl', prms=['framebuffer', 'src'])
def glNamedFramebufferReadBuffer(framebuffer, src):
	pass


@params(api='gl', prms=['coord', 'pname', 'params'])
def glGetTexGenfv(coord, pname, params):
	pass


@params(api='gl', prms=['target', 'id'])
def glBindTransformFeedback(target, id):
	pass


@params(api='gl', prms=['target', 'v'])
def glMultiTexCoord2iv(target, v):
	pass


@params(api='gl', prms=['red', 'green', 'blue'])
def glSecondaryColor3f(red, green, blue):
	pass


@params(api='gl', prms=['v'])
def glRasterPos3iv(v):
	pass


@params(api='gl', prms=['type', 'value'])
def glVertexP2ui(type, value):
	pass


@params(api='gl', prms=['target', 'format', 'type', 'bufSize', 'image'])
def glGetnConvolutionFilter(target, format, type, bufSize, image):
	pass


@params(api='gl', prms=['red', 'green', 'blue'])
def glSecondaryColor3b(red, green, blue):
	pass


@params(api='gl', prms=['v'])
def glTexCoord4sv(v):
	pass


@params(api='gl', prms=['location', 'count', 'value'])
def glUniform2uiv(location, count, value):
	pass


@params(api='gl', prms=[])
def glFinish():
	pass


@params(api='gl', prms=['x', 'y'])
def glRasterPos2s(x, y):
	pass


@params(api='gl', prms=['location', 'count', 'value'])
def glUniform1uiv(location, count, value):
	pass


@params(api='gl', prms=['location', 'count', 'transpose', 'value'])
def glUniformMatrix2dv(location, count, transpose, value):
	pass


@params(api='gl', prms=['c'])
def glIndexdv(c):
	pass


@params(api='gl', prms=['v'])
def glTexCoord3iv(v):
	pass


@params(api='gl', prms=['depth'])
def glClearDepth(depth):
	pass


@params(api='gl', prms=['location', 'count', 'transpose', 'value'])
def glUniformMatrix4dv(location, count, transpose, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix4x3dv(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['v'])
def glVertex4dv(v):
	pass


@params(api='gl', prms=['target', 'n', 'textures'])
def glCreateTextures(target, n, textures):
	pass


@params(api='gl', prms=['n', 'buffers'])
def glCreateBuffers(n, buffers):
	pass


@params(api='gl', prms=['m'])
def glMultTransposeMatrixf(m):
	pass


@params(api='gl', prms=['flag'])
def glEdgeFlagv(flag):
	pass


@params(api='gl', prms=['location', 'count', 'transpose', 'value'])
def glUniformMatrix4x3dv(location, count, transpose, value):
	pass


@params(api='gl', prms=['n', 'ids'])
def glDeleteQueries(n, ids):
	pass


@params(api='gl', prms=['type', 'coords'])
def glNormalP3uiv(type, coords):
	pass


@params(api='gl', prms=['x', 'y'])
def glRasterPos2d(x, y):
	pass


@params(api='gl', prms=[])
def glInitNames():
	pass


@params(api='gl', prms=['v'])
def glColor3dv(v):
	pass


@params(api='gl', prms=['target', 'reset', 'format', 'type', 'bufSize', 'values'])
def glGetnMinmax(target, reset, format, type, bufSize, values):
	pass


@params(api='gl', prms=['framebuffer', 'buffer', 'drawbuffer', 'value'])
def glClearNamedFramebufferuiv(framebuffer, buffer, drawbuffer, value):
	pass


@params(api='gl', prms=['index', 'pname', 'params'])
def glGetVertexAttribfv(index, pname, params):
	pass


@params(api='gl', prms=['num_groups_x', 'num_groups_y', 'num_groups_z'])
def glDispatchCompute(num_groups_x, num_groups_y, num_groups_z):
	pass


@params(api='gl', prms=['program', 'index', 'bufSize', 'length', 'size', 'type', 'name'])
def glGetActiveAttrib(program, index, bufSize, length, size, type, name):
	pass


@params(api='gl', prms=['location', 'v0', 'v1', 'v2'])
def glUniform3i(location, v0, v1, v2):
	pass


@params(api='gl', prms=['target', 'level', 'xoffset', 'yoffset', 'width', 'height', 'format', 'type', 'pixels'])
def glTexSubImage2D(target, level, xoffset, yoffset, width, height, format, type, pixels):
	pass


@params(api='gl', prms=['opcode'])
def glLogicOp(opcode):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix3x4fv(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['pname', 'param'])
def glPixelTransferf(pname, param):
	pass


@params(api='gl', prms=['texture', 'pname', 'params'])
def glGetTextureParameterIuiv(texture, pname, params):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix4dv(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['location', 'count', 'transpose', 'value'])
def glUniformMatrix3x4dv(location, count, transpose, value):
	pass


@params(api='gl', prms=['mode', 'id', 'stream'])
def glDrawTransformFeedbackStream(mode, id, stream):
	pass


@params(api='gl', prms=['location', 'v0', 'v1', 'v2'])
def glUniform3ui(location, v0, v1, v2):
	pass


@params(api='gl', prms=['mode'])
def glProvokingVertex(mode):
	pass


@params(api='gl', prms=['count', 'shaders', 'binaryformat', 'binary', 'length'])
def glShaderBinary(count, shaders, binaryformat, binary, length):
	pass


@params(api='gl', prms=['coord', 'pname', 'params'])
def glTexGeniv(coord, pname, params):
	pass


@params(api='gl', prms=['mode', 'count', 'type', 'indices'])
def glDrawElements(mode, count, type, indices):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform4iv(program, location, count, value):
	pass


@params(api='gl', prms=['texture'])
def glClientActiveTexture(texture):
	pass


@params(api='gl', prms=['location', 'count', 'value'])
def glUniform1iv(location, count, value):
	pass


@params(api='gl', prms=['mode', 'first', 'count', 'instancecount'])
def glDrawArraysInstanced(mode, first, count, instancecount):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib4uiv(index, v):
	pass


@params(api='gl', prms=['target', 'index'])
def glEndQueryIndexed(target, index):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform1iv(program, location, count, value):
	pass


@params(api='gl', prms=['target', 'renderbuffer'])
def glBindRenderbuffer(target, renderbuffer):
	pass


@params(api='gl', prms=['face', 'pname', 'params'])
def glMaterialiv(face, pname, params):
	pass


@params(api='gl', prms=['program'])
def glIsProgram(program):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib4fv(index, v):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix2x3dv(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['map', 'bufSize', 'values'])
def glGetnPixelMapfv(map, bufSize, values):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib2fv(index, v):
	pass


@params(api='gl', prms=['array'])
def glDisableClientState(array):
	pass


@params(api='gl', prms=['v'])
def glColor4uiv(v):
	pass


@params(api='gl', prms=['program', 'location', 'v0', 'v1', 'v2'])
def glProgramUniform3i(program, location, v0, v1, v2):
	pass


@params(api='gl', prms=['mode', 'i1', 'i2', 'j1', 'j2'])
def glEvalMesh2(mode, i1, i2, j1, j2):
	pass


@params(api='gl', prms=['mode', 'i1', 'i2'])
def glEvalMesh1(mode, i1, i2):
	pass


@params(api='gl', prms=['program', 'location', 'v0', 'v1', 'v2'])
def glProgramUniform3d(program, location, v0, v1, v2):
	pass


@params(api='gl', prms=['u'])
def glEvalCoord2fv(u):
	pass


@params(api='gl', prms=['m'])
def glLoadTransposeMatrixd(m):
	pass


@params(api='gl', prms=['m'])
def glLoadTransposeMatrixf(m):
	pass


@params(api='gl', prms=['index', 'x'])
def glVertexAttribI1ui(index, x):
	pass


@params(api='gl', prms=['bufSize', 'pattern'])
def glGetnPolygonStipple(bufSize, pattern):
	pass


@params(api='gl', prms=['texture', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth'])
def glInvalidateTexSubImage(texture, level, xoffset, yoffset, zoffset, width, height, depth):
	pass


@params(api='gl', prms=['pname', 'data'])
def glGetInteger64v(pname, data):
	pass


@params(api='gl', prms=['plane', 'equation'])
def glClipPlane(plane, equation):
	pass


@params(api='gl', prms=['c'])
def glIndexub(c):
	pass


@params(api='gl', prms=['framebuffer', 'attachment', 'renderbuffertarget', 'renderbuffer'])
def glNamedFramebufferRenderbuffer(framebuffer, attachment, renderbuffertarget, renderbuffer):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib4Niv(index, v):
	pass


@params(api='gl', prms=['buffer', 'drawbuffer', 'value'])
def glClearBufferiv(buffer, drawbuffer, value):
	pass


@params(api='gl', prms=['type', 'color'])
def glColorP4uiv(type, color):
	pass


@params(api='gl', prms=['texture', 'level', 'pname', 'params'])
def glGetTextureLevelParameterfv(texture, level, pname, params):
	pass


@params(api='gl', prms=['target', 'v'])
def glMultiTexCoord1fv(target, v):
	pass


@params(api='gl', prms=['sampler', 'pname', 'params'])
def glGetSamplerParameterIuiv(sampler, pname, params):
	pass


@params(api='gl', prms=['type', 'coords'])
def glTexCoordP3ui(type, coords):
	pass


@params(api='gl', prms=['location', 'v0', 'v1'])
def glUniform2f(location, v0, v1):
	pass


@params(api='gl', prms=['texture', 'level', 'xoffset', 'width', 'format', 'type', 'pixels'])
def glTextureSubImage1D(texture, level, xoffset, width, format, type, pixels):
	pass


@params(api='gl', prms=['x', 'y', 'z'])
def glWindowPos3s(x, y, z):
	pass


@params(api='gl', prms=['d'])
def glClearDepthf(d):
	pass


@params(api='gl', prms=['texture', 'internalformat', 'buffer', 'offset', 'size'])
def glTextureBufferRange(texture, internalformat, buffer, offset, size):
	pass


@params(api='gl', prms=['x', 'y', 'z'])
def glWindowPos3i(x, y, z):
	pass


@params(api='gl', prms=['x', 'y', 'z'])
def glWindowPos3d(x, y, z):
	pass


@params(api='gl', prms=['texture', 'type', 'coords'])
def glMultiTexCoordP4ui(texture, type, coords):
	pass


@params(api='gl', prms=['red', 'green', 'blue'])
def glColor3us(red, green, blue):
	pass


@params(api='gl', prms=['light', 'pname', 'params'])
def glGetLightiv(light, pname, params):
	pass


@params(api='gl', prms=['target', 's', 't', 'r', 'q'])
def glMultiTexCoord4f(target, s, t, r, q):
	pass


@params(api='gl', prms=['red', 'green', 'blue'])
def glColor3ub(red, green, blue):
	pass


@params(api='gl', prms=['target', 's', 't', 'r', 'q'])
def glMultiTexCoord4d(target, s, t, r, q):
	pass


@params(api='gl', prms=['red', 'green', 'blue'])
def glColor3ui(red, green, blue):
	pass


@params(api='gl', prms=['target', 's', 't', 'r', 'q'])
def glMultiTexCoord4i(target, s, t, r, q):
	pass


@params(api='gl', prms=['mask'])
def glGetPolygonStipple(mask):
	pass


@params(api='gl', prms=['location', 'x', 'y'])
def glUniform2d(location, x, y):
	pass


@params(api='gl', prms=['index', 'x', 'y', 'z', 'w'])
def glVertexAttribI4ui(index, x, y, z, w):
	pass


@params(api='gl', prms=['red', 'green', 'blue', 'alpha'])
def glColorMask(red, green, blue, alpha):
	pass


@params(api='gl', prms=['target', 'level', 'format', 'type', 'bufSize', 'pixels'])
def glGetnTexImage(target, level, format, type, bufSize, pixels):
	pass


@params(api='gl', prms=['mode'])
def glBlendEquation(mode):
	pass


@params(api='gl', prms=['target', 'v'])
def glMultiTexCoord3dv(target, v):
	pass


@params(api='gl', prms=['v'])
def glColor4sv(v):
	pass


@params(api='gl', prms=['program', 'programInterface', 'index', 'propCount', 'props', 'bufSize', 'length', 'params'])
def glGetProgramResourceiv(program, programInterface, index, propCount, props, bufSize, length, params):
	pass


@params(api='gl', prms=['target', 'internalformat', 'format', 'type', 'data'])
def glClearBufferData(target, internalformat, format, type, data):
	pass


@params(api='gl', prms=['primitiveMode'])
def glBeginTransformFeedback(primitiveMode):
	pass


@params(api='gl', prms=['v'])
def glColor3iv(v):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib3sv(index, v):
	pass


@params(api='gl', prms=['target', 'level', 'internalformat', 'width', 'border', 'imageSize', 'data'])
def glCompressedTexImage1D(target, level, internalformat, width, border, imageSize, data):
	pass


@params(api='gl', prms=['n', 'ids'])
def glDeleteTransformFeedbacks(n, ids):
	pass


@params(api='gl', prms=['mode', 'start', 'end', 'count', 'type', 'indices', 'basevertex'])
def glDrawRangeElementsBaseVertex(mode, start, end, count, type, indices, basevertex):
	pass


@params(api='gl', prms=['program', 'index', 'name'])
def glBindAttribLocation(program, index, name):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib1dv(index, v):
	pass


@params(api='gl', prms=['buf', 'srcRGB', 'dstRGB', 'srcAlpha', 'dstAlpha'])
def glBlendFuncSeparatei(buf, srcRGB, dstRGB, srcAlpha, dstAlpha):
	pass


@params(api='gl', prms=['location', 'v0', 'v1'])
def glUniform2ui(location, v0, v1):
	pass


@params(api='gl', prms=['pname', 'param'])
def glPixelTransferi(pname, param):
	pass


@params(api='gl', prms=['v'])
def glWindowPos2fv(v):
	pass


@params(api='gl', prms=['target', 'index'])
def glDisablei(target, index):
	pass


@params(api='gl', prms=['sync', 'pname', 'bufSize', 'length', 'values'])
def glGetSynciv(sync, pname, bufSize, length, values):
	pass


@params(api='gl', prms=['program', 'location', 'v0', 'v1'])
def glProgramUniform2i(program, location, v0, v1):
	pass


@params(api='gl', prms=['program', 'bufSize', 'length', 'binaryFormat', 'binary'])
def glGetProgramBinary(program, bufSize, length, binaryFormat, binary):
	pass


@params(api='gl', prms=['i'])
def glEvalPoint1(i):
	pass


@params(api='gl', prms=['i', 'j'])
def glEvalPoint2(i, j):
	pass


@params(api='gl', prms=[])
def glPauseTransformFeedback():
	pass


@params(api='gl', prms=['n', 'ids'])
def glCreateTransformFeedbacks(n, ids):
	pass


@params(api='gl', prms=['target', 'level', 'xoffset', 'width', 'format', 'type', 'pixels'])
def glTexSubImage1D(target, level, xoffset, width, format, type, pixels):
	pass


@params(api='gl', prms=['index', 'type', 'normalized', 'value'])
def glVertexAttribP3uiv(index, type, normalized, value):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttribI4iv(index, v):
	pass


@params(api='gl', prms=['vaobj', 'pname', 'param'])
def glGetVertexArrayiv(vaobj, pname, param):
	pass


@params(api='gl', prms=['name'])
def glLoadName(name):
	pass


@params(api='gl', prms=['m'])
def glLoadMatrixf(m):
	pass


@params(api='gl', prms=['m'])
def glLoadMatrixd(m):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glTexParameterfv(target, pname, params):
	pass


@params(api='gl', prms=['location', 'count', 'value'])
def glUniform3dv(location, count, value):
	pass


@params(api='gl', prms=['face', 'func', 'ref', 'mask'])
def glStencilFuncSeparate(face, func, ref, mask):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform3fv(program, location, count, value):
	pass


@params(api='gl', prms=['first', 'count', 'samplers'])
def glBindSamplers(first, count, samplers):
	pass


@params(api='gl', prms=['id', 'pname', 'params'])
def glGetQueryObjectui64v(id, pname, params):
	pass


@params(api='gl', prms=['texture', 'level', 'format', 'type', 'bufSize', 'pixels'])
def glGetTextureImage(texture, level, format, type, bufSize, pixels):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform1fv(program, location, count, value):
	pass


@params(api='gl', prms=['location', 'count', 'transpose', 'value'])
def glUniformMatrix4fv(location, count, transpose, value):
	pass


@params(api='gl', prms=['n', 'pipelines'])
def glDeleteProgramPipelines(n, pipelines):
	pass


@params(api='gl', prms=['v'])
def glVertex3fv(v):
	pass


@params(api='gl', prms=['x', 'y'])
def glWindowPos2s(x, y):
	pass


@params(api='gl', prms=['x', 'y'])
def glWindowPos2i(x, y):
	pass


@params(api='gl', prms=['x', 'y'])
def glWindowPos2f(x, y):
	pass


@params(api='gl', prms=['x', 'y'])
def glWindowPos2d(x, y):
	pass


@params(api='gl', prms=['shadertype', 'count', 'indices'])
def glUniformSubroutinesuiv(shadertype, count, indices):
	pass


@params(api='gl', prms=['v1', 'v2'])
def glRectdv(v1, v2):
	pass


@params(api='gl', prms=['type', 'color'])
def glColorP3uiv(type, color):
	pass


@params(api='gl', prms=['coord'])
def glFogCoordfv(coord):
	pass


@params(api='gl', prms=['shader'])
def glCompileShader(shader):
	pass


@params(api='gl', prms=['c'])
def glIndexfv(c):
	pass


@params(api='gl', prms=['texture', 'type', 'coords'])
def glMultiTexCoordP3ui(texture, type, coords):
	pass


@params(api='gl', prms=['v'])
def glNormal3sv(v):
	pass


@params(api='gl', prms=['target', 'numAttachments', 'attachments'])
def glInvalidateFramebuffer(target, numAttachments, attachments):
	pass


@params(api='gl', prms=['target', 'level', 'internalformat', 'width', 'height', 'border', 'imageSize', 'data'])
def glCompressedTexImage2D(target, level, internalformat, width, height, border, imageSize, data):
	pass


@params(api='gl', prms=['index', 'x'])
def glVertexAttrib1f(index, x):
	pass


@params(api='gl', prms=['v'])
def glVertex4fv(v):
	pass


@params(api='gl', prms=['framebuffer', 'buffer', 'drawbuffer', 'depth', 'stencil'])
def glClearNamedFramebufferfi(framebuffer, buffer, drawbuffer, depth, stencil):
	pass


@params(api='gl', prms=['id', 'buffer', 'pname', 'offset'])
def glGetQueryBufferObjectuiv(id, buffer, pname, offset):
	pass


@params(api='gl', prms=['framebuffer', 'buffer', 'drawbuffer', 'value'])
def glClearNamedFramebufferfv(framebuffer, buffer, drawbuffer, value):
	pass


@params(api='gl', prms=['index', 'x'])
def glVertexAttrib1s(index, x):
	pass


@params(api='gl', prms=['target', 'v'])
def glMultiTexCoord1sv(target, v):
	pass


@params(api='gl', prms=['program'])
def glDeleteProgram(program):
	pass


@params(api='gl', prms=['v'])
def glColor4bv(v):
	pass


@params(api='gl', prms=['x', 'y'])
def glRasterPos2f(x, y):
	pass


@params(api='gl', prms=[])
def glLoadIdentity():
	pass


@params(api='gl', prms=['v'])
def glRasterPos4iv(v):
	pass


@params(api='gl', prms=['location', 'count', 'transpose', 'value'])
def glUniformMatrix4x3fv(location, count, transpose, value):
	pass


@params(api='gl', prms=['buffer', 'drawbuffer', 'value'])
def glClearBufferfv(buffer, drawbuffer, value):
	pass


@params(api='gl', prms=[])
def glTextureBarrier():
	pass


@params(api='gl', prms=['buffer', 'drawbuffer', 'depth', 'stencil'])
def glClearBufferfi(buffer, drawbuffer, depth, stencil):
	pass


@params(api='gl', prms=['mode', 'indirect'])
def glDrawArraysIndirect(mode, indirect):
	pass


@params(api='gl', prms=['n', 'arrays'])
def glGenVertexArrays(n, arrays):
	pass


@params(api='gl', prms=['vaobj', 'index'])
def glEnableVertexArrayAttrib(vaobj, index):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix3x2dv(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['bindingindex', 'divisor'])
def glVertexBindingDivisor(bindingindex, divisor):
	pass


@params(api='gl', prms=['sampler', 'pname', 'params'])
def glGetSamplerParameterIiv(sampler, pname, params):
	pass


@params(api='gl', prms=['location', 'count', 'transpose', 'value'])
def glUniformMatrix4x2fv(location, count, transpose, value):
	pass


@params(api='gl', prms=['index', 'x', 'y', 'z'])
def glVertexAttrib3f(index, x, y, z):
	pass


@params(api='gl', prms=['id', 'buffer', 'pname', 'offset'])
def glGetQueryBufferObjecti64v(id, buffer, pname, offset):
	pass


@params(api='gl', prms=['index', 'pname', 'params'])
def glGetVertexAttribdv(index, pname, params):
	pass


@params(api='gl', prms=['location', 'v0'])
def glUniform1ui(location, v0):
	pass


@params(api='gl', prms=['readFramebuffer', 'drawFramebuffer', 'srcX0', 'srcY0', 'srcX1', 'srcY1', 'dstX0', 'dstY0', 'dstX1', 'dstY1', 'mask', 'filter'])
def glBlitNamedFramebuffer(readFramebuffer, drawFramebuffer, srcX0, srcY0, srcX1, srcY1, dstX0, dstY0, dstX1, dstY1, mask, filter):
	pass


@params(api='gl', prms=['index', 'x', 'y', 'z'])
def glVertexAttrib3d(index, x, y, z):
	pass


@params(api='gl', prms=['barriers'])
def glMemoryBarrier(barriers):
	pass


@params(api='gl', prms=['program', 'name'])
def glGetFragDataLocation(program, name):
	pass


@params(api='gl', prms=['face', 'pname', 'params'])
def glGetMaterialfv(face, pname, params):
	pass


@params(api='gl', prms=['map', 'mapsize', 'values'])
def glPixelMapuiv(map, mapsize, values):
	pass


@params(api='gl', prms=['texture', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth', 'format', 'type', 'data'])
def glClearTexSubImage(texture, level, xoffset, yoffset, zoffset, width, height, depth, format, type, data):
	pass


@params(api='gl', prms=['texture', 'pname', 'params'])
def glGetTextureParameterIiv(texture, pname, params):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttribI4ubv(index, v):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix4x2dv(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['shader'])
def glIsShader(shader):
	pass


@params(api='gl', prms=['cap'])
def glEnable(cap):
	pass


@params(api='gl', prms=['program', 'uniformCount', 'uniformIndices', 'pname', 'params'])
def glGetActiveUniformsiv(program, uniformCount, uniformIndices, pname, params):
	pass


@params(api='gl', prms=['buf', 'mode'])
def glBlendEquationi(buf, mode):
	pass


@params(api='gl', prms=['program', 'name'])
def glGetAttribLocation(program, name):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib4dv(index, v):
	pass


@params(api='gl', prms=['texture', 'pname', 'params'])
def glGetTextureParameteriv(texture, pname, params):
	pass


@params(api='gl', prms=['program', 'location', 'v0', 'v1', 'v2'])
def glProgramUniform3ui(program, location, v0, v1, v2):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix2x3fv(program, location, count, transpose, value):
	pass


@params(api='gl', prms=[])
def glPushMatrix():
	pass


@params(api='gl', prms=['program', 'location', 'v0'])
def glProgramUniform1i(program, location, v0):
	pass


@params(api='gl', prms=['program', 'location', 'v0'])
def glProgramUniform1d(program, location, v0):
	pass


@params(api='gl', prms=['program', 'location', 'v0'])
def glProgramUniform1f(program, location, v0):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform3iv(program, location, count, value):
	pass


@params(api='gl', prms=['c'])
def glIndexiv(c):
	pass


@params(api='gl', prms=['xfb', 'index', 'buffer', 'offset', 'size'])
def glTransformFeedbackBufferRange(xfb, index, buffer, offset, size):
	pass


@params(api='gl', prms=['xfactor', 'yfactor'])
def glPixelZoom(xfactor, yfactor):
	pass


@params(api='gl', prms=['type', 'color'])
def glColorP3ui(type, color):
	pass


@params(api='gl', prms=['texture', 'type', 'coords'])
def glMultiTexCoordP4uiv(texture, type, coords):
	pass


@params(api='gl', prms=['texture', 'target', 'origtexture', 'internalformat', 'minlevel', 'numlevels', 'minlayer', 'numlayers'])
def glTextureView(texture, target, origtexture, internalformat, minlevel, numlevels, minlayer, numlayers):
	pass


@params(api='gl', prms=['vaobj', 'index'])
def glDisableVertexArrayAttrib(vaobj, index):
	pass


@params(api='gl', prms=['location', 'count', 'value'])
def glUniform4iv(location, count, value):
	pass


@params(api='gl', prms=['n', 'textures'])
def glGenTextures(n, textures):
	pass


@params(api='gl', prms=['texture', 'samples', 'internalformat', 'width', 'height', 'fixedsamplelocations'])
def glTextureStorage2DMultisample(texture, samples, internalformat, width, height, fixedsamplelocations):
	pass


@params(api='gl', prms=['target', 's'])
def glMultiTexCoord1s(target, s):
	pass


@params(api='gl', prms=['index', 'size', 'type', 'normalized', 'stride', 'pointer'])
def glVertexAttribPointer(index, size, type, normalized, stride, pointer):
	pass


@params(api='gl', prms=['location', 'v0'])
def glUniform1f(location, v0):
	pass


@params(api='gl', prms=['index', 'type', 'normalized', 'value'])
def glVertexAttribP1ui(index, type, normalized, value):
	pass


@params(api='gl', prms=['target', 'v'])
def glMultiTexCoord4sv(target, v):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix3x4dv(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['texture', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth', 'format', 'type', 'bufSize', 'pixels'])
def glGetTextureSubImage(texture, level, xoffset, yoffset, zoffset, width, height, depth, format, type, bufSize, pixels):
	pass


@params(api='gl', prms=['renderbuffer', 'pname', 'params'])
def glGetNamedRenderbufferParameteriv(renderbuffer, pname, params):
	pass


@params(api='gl', prms=['target', 'first', 'count', 'buffers', 'offsets', 'sizes'])
def glBindBuffersRange(target, first, count, buffers, offsets, sizes):
	pass


@params(api='gl', prms=['program', 'colorNumber', 'index', 'name'])
def glBindFragDataLocationIndexed(program, colorNumber, index, name):
	pass


@params(api='gl', prms=['target', 'v'])
def glMultiTexCoord2dv(target, v):
	pass


@params(api='gl', prms=['location', 'count', 'value'])
def glUniform2iv(location, count, value):
	pass


@params(api='gl', prms=['texture', 'pname', 'param'])
def glTextureParameterf(texture, pname, param):
	pass


@params(api='gl', prms=['size', 'type', 'buffer'])
def glFeedbackBuffer(size, type, buffer):
	pass


@params(api='gl', prms=['target', 's', 't'])
def glMultiTexCoord2i(target, s, t):
	pass


@params(api='gl', prms=['texture', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth', 'format', 'type', 'pixels'])
def glTextureSubImage3D(texture, level, xoffset, yoffset, zoffset, width, height, depth, format, type, pixels):
	pass


@params(api='gl', prms=['target', 'attachment', 'textarget', 'texture', 'level'])
def glFramebufferTexture1D(target, attachment, textarget, texture, level):
	pass


@params(api='gl', prms=['shader', 'pname', 'params'])
def glGetShaderiv(shader, pname, params):
	pass


@params(api='gl', prms=['target', 's', 't'])
def glMultiTexCoord2d(target, s, t):
	pass


@params(api='gl', prms=['buffer', 'size', 'data', 'flags'])
def glNamedBufferStorage(buffer, size, data, flags):
	pass


@params(api='gl', prms=['location', 'count', 'value'])
def glUniform1dv(location, count, value):
	pass


@params(api='gl', prms=['target', 'v'])
def glMultiTexCoord4fv(target, v):
	pass


@params(api='gl', prms=['x', 'y', 'z'])
def glRasterPos3i(x, y, z):
	pass


@params(api='gl', prms=['x', 'y', 'z'])
def glRasterPos3d(x, y, z):
	pass


@params(api='gl', prms=['x', 'y', 'z'])
def glRasterPos3f(x, y, z):
	pass


@params(api='gl', prms=['target', 'level', 'internalformat', 'width', 'height', 'depth', 'border', 'imageSize', 'data'])
def glCompressedTexImage3D(target, level, internalformat, width, height, depth, border, imageSize, data):
	pass


@params(api='gl', prms=['index', 'pname', 'params'])
def glGetVertexAttribiv(index, pname, params):
	pass


@params(api='gl', prms=['target', 'reset', 'format', 'type', 'bufSize', 'values'])
def glGetnHistogram(target, reset, format, type, bufSize, values):
	pass


@params(api='gl', prms=['location', 'count', 'transpose', 'value'])
def glUniformMatrix2fv(location, count, transpose, value):
	pass


@params(api='gl', prms=['texture'])
def glGenerateTextureMipmap(texture):
	pass


@params(api='gl', prms=['mode', 'count', 'type', 'constindices', 'drawcount', 'basevertex'])
def glMultiDrawElementsBaseVertex(mode, count, type, constindices, drawcount, basevertex):
	pass


@params(api='gl', prms=['v'])
def glWindowPos3sv(v):
	pass


@params(api='gl', prms=['target', 'level', 'xoffset', 'width', 'format', 'imageSize', 'data'])
def glCompressedTexSubImage1D(target, level, xoffset, width, format, imageSize, data):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glGetTexParameterIiv(target, pname, params):
	pass


@params(api='gl', prms=['texture', 'level'])
def glInvalidateTexImage(texture, level):
	pass


@params(api='gl', prms=['type', 'value'])
def glVertexP3uiv(type, value):
	pass


@params(api='gl', prms=['target', 'query', 'bufSize', 'v'])
def glGetnMapdv(target, query, bufSize, v):
	pass


@params(api='gl', prms=['callback', 'userParam'])
def glDebugMessageCallback(callback, userParam):
	pass


@params(api='gl', prms=['target', 'index', 'data'])
def glGetBooleani_v(target, index, data):
	pass


@params(api='gl', prms=['texture', 'pname', 'params'])
def glTextureParameterIiv(texture, pname, params):
	pass


@params(api='gl', prms=['list', 'mode'])
def glNewList(list, mode):
	pass


@params(api='gl', prms=['target', 'mode'])
def glHint(target, mode):
	pass


@params(api='gl', prms=['mode', 'indirect', 'drawcount', 'stride'])
def glMultiDrawArraysIndirect(mode, indirect, drawcount, stride):
	pass


@params(api='gl', prms=['index', 'type', 'normalized', 'value'])
def glVertexAttribP2uiv(index, type, normalized, value):
	pass


@params(api='gl', prms=['x', 'y', 'z'])
def glScalef(x, y, z):
	pass


@params(api='gl', prms=['x', 'y', 'z'])
def glScaled(x, y, z):
	pass


@params(api='gl', prms=['program', 'programInterface', 'index', 'bufSize', 'length', 'name'])
def glGetProgramResourceName(program, programInterface, index, bufSize, length, name):
	pass


@params(api='gl', prms=['first', 'count', 'v'])
def glDepthRangeArrayv(first, count, v):
	pass


@params(api='gl', prms=['program', 'bufferIndex', 'pname', 'params'])
def glGetActiveAtomicCounterBufferiv(program, bufferIndex, pname, params):
	pass


@params(api='gl', prms=['face', 'sfail', 'dpfail', 'dppass'])
def glStencilOpSeparate(face, sfail, dpfail, dppass):
	pass


@params(api='gl', prms=['vaobj', 'attribindex', 'bindingindex'])
def glVertexArrayAttribBinding(vaobj, attribindex, bindingindex):
	pass


@params(api='gl', prms=['s', 't', 'r'])
def glTexCoord3f(s, t, r):
	pass


@params(api='gl', prms=['index', 'x'])
def glVertexAttribI1i(index, x):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glGetTexParameteriv(target, pname, params):
	pass


@params(api='gl', prms=['index', 'pname', 'pointer'])
def glGetVertexAttribPointerv(index, pname, pointer):
	pass


@params(api='gl', prms=['target', 'lod', 'bufSize', 'pixels'])
def glGetnCompressedTexImage(target, lod, bufSize, pixels):
	pass


@params(api='gl', prms=['v'])
def glWindowPos2dv(v):
	pass


@params(api='gl', prms=['cap'])
def glDisable(cap):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform4uiv(program, location, count, value):
	pass


@params(api='gl', prms=['texture', 'level', 'xoffset', 'yoffset', 'x', 'y', 'width', 'height'])
def glCopyTextureSubImage2D(texture, level, xoffset, yoffset, x, y, width, height):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttribI2uiv(index, v):
	pass


@params(api='gl', prms=['light', 'pname', 'params'])
def glGetLightfv(light, pname, params):
	pass


@params(api='gl', prms=['target', 's', 't', 'r'])
def glMultiTexCoord3s(target, s, t, r):
	pass


@params(api='gl', prms=['target', 's', 't', 'r'])
def glMultiTexCoord3i(target, s, t, r):
	pass


@params(api='gl', prms=['target', 's', 't', 'r'])
def glMultiTexCoord3f(target, s, t, r):
	pass


@params(api='gl', prms=['target', 's', 't', 'r'])
def glMultiTexCoord3d(target, s, t, r):
	pass


@params(api='gl', prms=['coord'])
def glFogCoorddv(coord):
	pass


@params(api='gl', prms=['location', 'count', 'value'])
def glUniform3uiv(location, count, value):
	pass


@params(api='gl', prms=['buffer', 'internalformat', 'format', 'type', 'data'])
def glClearNamedBufferData(buffer, internalformat, format, type, data):
	pass


@params(api='gl', prms=['buffer', 'offset', 'length'])
def glFlushMappedNamedBufferRange(buffer, offset, length):
	pass


@params(api='gl', prms=['name'])
def glPushName(name):
	pass


@params(api='gl', prms=['plane', 'equation'])
def glGetClipPlane(plane, equation):
	pass


@params(api='gl', prms=['x', 'y', 'z', 'w'])
def glRasterPos4i(x, y, z, w):
	pass


@params(api='gl', prms=['red', 'green', 'blue', 'alpha'])
def glBlendColor(red, green, blue, alpha):
	pass


@params(api='gl', prms=['sampler', 'pname', 'param'])
def glSamplerParameterIuiv(sampler, pname, param):
	pass


@params(api='gl', prms=['c'])
def glIndexubv(c):
	pass


@params(api='gl', prms=['framebuffer', 'target'])
def glCheckNamedFramebufferStatus(framebuffer, target):
	pass


@params(api='gl', prms=['x', 'y', 'z', 'w'])
def glRasterPos4d(x, y, z, w):
	pass


@params(api='gl', prms=['x', 'y', 'z', 'w'])
def glRasterPos4f(x, y, z, w):
	pass


@params(api='gl', prms=['index', 'x', 'y', 'z'])
def glVertexAttrib3s(index, x, y, z):
	pass


@params(api='gl', prms=['x', 'y', 'z', 'w'])
def glRasterPos4s(x, y, z, w):
	pass


@params(api='gl', prms=['program', 'shadertype', 'pname', 'values'])
def glGetProgramStageiv(program, shadertype, pname, values):
	pass


@params(api='gl', prms=[])
def glPopMatrix():
	pass


@params(api='gl', prms=['x', 'y', 'z', 'w'])
def glVertex4s(x, y, z, w):
	pass


@params(api='gl', prms=['location', 'v0', 'v1', 'v2', 'v3'])
def glUniform4i(location, v0, v1, v2, v3):
	pass


@params(api='gl', prms=['texture'])
def glActiveTexture(texture):
	pass


@params(api='gl', prms=['index'])
def glEnableVertexAttribArray(index):
	pass


@params(api='gl', prms=['location', 'x', 'y', 'z', 'w'])
def glUniform4d(location, x, y, z, w):
	pass


@params(api='gl', prms=['location', 'v0', 'v1', 'v2', 'v3'])
def glUniform4f(location, v0, v1, v2, v3):
	pass


@params(api='gl', prms=['target', 'samples', 'internalformat', 'width', 'height'])
def glRenderbufferStorageMultisample(target, samples, internalformat, width, height):
	pass


@params(api='gl', prms=['n', 'pipelines'])
def glCreateProgramPipelines(n, pipelines):
	pass


@params(api='gl', prms=['index', 'size', 'type', 'stride', 'pointer'])
def glVertexAttribLPointer(index, size, type, stride, pointer):
	pass


@params(api='gl', prms=['target', 'v'])
def glMultiTexCoord3sv(target, v):
	pass


@params(api='gl', prms=['mode', 'count', 'type', 'indices', 'instancecount', 'basevertex'])
def glDrawElementsInstancedBaseVertex(mode, count, type, indices, instancecount, basevertex):
	pass


@params(api='gl', prms=['program', 'shadertype', 'index', 'bufsize', 'length', 'name'])
def glGetActiveSubroutineName(program, shadertype, index, bufsize, length, name):
	pass


@params(api='gl', prms=['target', 'v'])
def glMultiTexCoord4iv(target, v):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glTexEnvfv(target, pname, params):
	pass


@params(api='gl', prms=[])
def glPopDebugGroup():
	pass


@params(api='gl', prms=['program', 'uniformBlockIndex', 'uniformBlockBinding'])
def glUniformBlockBinding(program, uniformBlockIndex, uniformBlockBinding):
	pass


@params(api='gl', prms=['target', 'offset', 'size', 'data'])
def glBufferSubData(target, offset, size, data):
	pass


@params(api='gl', prms=['size', 'type', 'stride', 'pointer'])
def glTexCoordPointer(size, type, stride, pointer):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix3x2fv(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['target', 'index', 'pname', 'params'])
def glGetQueryIndexediv(target, index, pname, params):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glTexEnviv(target, pname, params):
	pass


@params(api='gl', prms=['sfactor', 'dfactor'])
def glBlendFunc(sfactor, dfactor):
	pass


@params(api='gl', prms=[])
def glCreateProgram():
	pass


@params(api='gl', prms=['index'])
def glPrimitiveRestartIndex(index):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix2fv(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['first', 'count', 'textures'])
def glBindImageTextures(first, count, textures):
	pass


@params(api='gl', prms=[])
def glEnd():
	pass


@params(api='gl', prms=['sampler', 'pname', 'param'])
def glSamplerParameteriv(sampler, pname, param):
	pass


@params(api='gl', prms=['v'])
def glSecondaryColor3iv(v):
	pass


@params(api='gl', prms=['m'])
def glMultTransposeMatrixd(m):
	pass


@params(api='gl', prms=['red', 'green', 'blue', 'alpha'])
def glClearColor(red, green, blue, alpha):
	pass


@params(api='gl', prms=['mask'])
def glPushClientAttrib(mask):
	pass


@params(api='gl', prms=['program', 'location', 'bufSize', 'params'])
def glGetnUniformiv(program, location, bufSize, params):
	pass


@params(api='gl', prms=['mask'])
def glStencilMask(mask):
	pass


@params(api='gl', prms=['red', 'green', 'blue'])
def glSecondaryColor3us(red, green, blue):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttribI4uiv(index, v):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib4bv(index, v):
	pass


@params(api='gl', prms=['program', 'programInterface', 'name'])
def glGetProgramResourceIndex(program, programInterface, name):
	pass


@params(api='gl', prms=['red', 'green', 'blue'])
def glSecondaryColor3ub(red, green, blue):
	pass


@params(api='gl', prms=['red', 'green', 'blue'])
def glSecondaryColor3ui(red, green, blue):
	pass


@params(api='gl', prms=['buffer', 'pname', 'params'])
def glGetNamedBufferPointerv(buffer, pname, params):
	pass


@params(api='gl', prms=['id', 'buffer', 'pname', 'offset'])
def glGetQueryBufferObjectui64v(id, buffer, pname, offset):
	pass


@params(api='gl', prms=['nx', 'ny', 'nz'])
def glNormal3f(nx, ny, nz):
	pass


@params(api='gl', prms=['location', 'count', 'transpose', 'value'])
def glUniformMatrix2x3fv(location, count, transpose, value):
	pass


@params(api='gl', prms=['n', 'ids'])
def glGenTransformFeedbacks(n, ids):
	pass


@params(api='gl', prms=['index', 'pname', 'params'])
def glGetVertexAttribIuiv(index, pname, params):
	pass


@params(api='gl', prms=['target', 'level', 'xoffset', 'yoffset', 'width', 'height', 'format', 'imageSize', 'data'])
def glCompressedTexSubImage2D(target, level, xoffset, yoffset, width, height, format, imageSize, data):
	pass


@params(api='gl', prms=['program', 'binaryFormat', 'binary', 'length'])
def glProgramBinary(program, binaryFormat, binary, length):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttribI4bv(index, v):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glGetTexParameterfv(target, pname, params):
	pass


@params(api='gl', prms=['vaobj', 'index', 'pname', 'param'])
def glGetVertexArrayIndexed64iv(vaobj, index, pname, param):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glTexParameterIiv(target, pname, params):
	pass


@params(api='gl', prms=['vaobj', 'attribindex', 'size', 'type', 'normalized', 'relativeoffset'])
def glVertexArrayAttribFormat(vaobj, attribindex, size, type, normalized, relativeoffset):
	pass


@params(api='gl', prms=[])
def glEndTransformFeedback():
	pass


@params(api='gl', prms=['target', 'samples', 'internalformat', 'width', 'height', 'fixedsamplelocations'])
def glTexImage2DMultisample(target, samples, internalformat, width, height, fixedsamplelocations):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttribI1iv(index, v):
	pass


@params(api='gl', prms=['index', 'divisor'])
def glVertexAttribDivisor(index, divisor):
	pass


@params(api='gl', prms=['texture', 'level', 'bufSize', 'pixels'])
def glGetCompressedTextureImage(texture, level, bufSize, pixels):
	pass


@params(api='gl', prms=['range'])
def glGenLists(range):
	pass


@params(api='gl', prms=['target', 'offset', 'length', 'access'])
def glMapBufferRange(target, offset, length, access):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix4x2fv(program, location, count, transpose, value):
	pass


@params(api='gl', prms=[])
def glEndList():
	pass


@params(api='gl', prms=['location', 'count', 'transpose', 'value'])
def glUniformMatrix3x2dv(location, count, transpose, value):
	pass


@params(api='gl', prms=['shadertype', 'precisiontype', 'range', 'precision'])
def glGetShaderPrecisionFormat(shadertype, precisiontype, range, precision):
	pass


@params(api='gl', prms=['mask'])
def glIndexMask(mask):
	pass


@params(api='gl', prms=['shader', 'count', 'conststring', 'length'])
def glShaderSource(shader, count, conststring, length):
	pass


@params(api='gl', prms=['n', 'renderbuffers'])
def glDeleteRenderbuffers(n, renderbuffers):
	pass


@params(api='gl', prms=['type', 'coords'])
def glTexCoordP2uiv(type, coords):
	pass


@params(api='gl', prms=['un', 'u1', 'u2', 'vn', 'v1', 'v2'])
def glMapGrid2d(un, u1, u2, vn, v1, v2):
	pass


@params(api='gl', prms=['buffer', 'pname', 'params'])
def glGetNamedBufferParameteri64v(buffer, pname, params):
	pass


@params(api='gl', prms=['x', 'y', 'z', 'w'])
def glVertex4d(x, y, z, w):
	pass


@params(api='gl', prms=['target', 'size', 'data', 'usage'])
def glBufferData(target, size, data, usage):
	pass


@params(api='gl', prms=['x', 'y', 'z', 'w'])
def glVertex4f(x, y, z, w):
	pass


@params(api='gl', prms=['type', 'coords'])
def glTexCoordP1ui(type, coords):
	pass


@params(api='gl', prms=['texture', 'level', 'xoffset', 'yoffset', 'zoffset', 'x', 'y', 'width', 'height'])
def glCopyTextureSubImage3D(texture, level, xoffset, yoffset, zoffset, x, y, width, height):
	pass


@params(api='gl', prms=['target', 'v'])
def glMultiTexCoord2fv(target, v):
	pass


@params(api='gl', prms=['type', 'coords'])
def glNormalP3ui(type, coords):
	pass


@params(api='gl', prms=['size', 'type', 'stride', 'pointer'])
def glColorPointer(size, type, stride, pointer):
	pass


@params(api='gl', prms=['target', 'attachment', 'textarget', 'texture', 'level'])
def glFramebufferTexture2D(target, attachment, textarget, texture, level):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glGetBufferPointerv(target, pname, params):
	pass


@params(api='gl', prms=['target', 'attachment', 'textarget', 'texture', 'level', 'zoffset'])
def glFramebufferTexture3D(target, attachment, textarget, texture, level, zoffset):
	pass


@params(api='gl', prms=['v'])
def glWindowPos3dv(v):
	pass


@params(api='gl', prms=['sampler', 'pname', 'param'])
def glSamplerParameterfv(sampler, pname, param):
	pass


@params(api='gl', prms=['v'])
def glNormal3bv(v):
	pass


@params(api='gl', prms=['face', 'pname', 'params'])
def glGetMaterialiv(face, pname, params):
	pass


@params(api='gl', prms=['location', 'count', 'value'])
def glUniform1fv(location, count, value):
	pass


@params(api='gl', prms=['index', 'v'])
def glScissorIndexedv(index, v):
	pass


@params(api='gl', prms=['nx', 'ny', 'nz'])
def glNormal3s(nx, ny, nz):
	pass


@params(api='gl', prms=['map', 'bufSize', 'values'])
def glGetnPixelMapuiv(map, bufSize, values):
	pass


@params(api='gl', prms=['nx', 'ny', 'nz'])
def glNormal3i(nx, ny, nz):
	pass


@params(api='gl', prms=['nx', 'ny', 'nz'])
def glNormal3d(nx, ny, nz):
	pass


@params(api='gl', prms=['nx', 'ny', 'nz'])
def glNormal3b(nx, ny, nz):
	pass


@params(api='gl', prms=['target', 'v'])
def glMultiTexCoord4dv(target, v):
	pass


@params(api='gl', prms=['index', 'x', 'y'])
def glVertexAttrib2d(index, x, y):
	pass


@params(api='gl', prms=['index', 'x', 'y'])
def glVertexAttrib2f(index, x, y):
	pass


@params(api='gl', prms=['index', 'x', 'y'])
def glVertexAttrib2s(index, x, y):
	pass


@params(api='gl', prms=['target', 'samples', 'internalformat', 'width', 'height', 'depth', 'fixedsamplelocations'])
def glTexImage3DMultisample(target, samples, internalformat, width, height, depth, fixedsamplelocations):
	pass


@params(api='gl', prms=['program', 'uniformBlockName'])
def glGetUniformBlockIndex(program, uniformBlockName):
	pass


@params(api='gl', prms=['mode'])
def glFrontFace(mode):
	pass


@params(api='gl', prms=['mode', 'first', 'count', 'instancecount', 'baseinstance'])
def glDrawArraysInstancedBaseInstance(mode, first, count, instancecount, baseinstance):
	pass


