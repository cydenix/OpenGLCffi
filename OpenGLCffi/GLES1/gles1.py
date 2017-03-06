def glFogfv(pname):
	params = ffi.new('const GLfloat *')
	return lib.glFogfv(pname, params)

def glIsBuffer(buffer):
	return lib.glIsBuffer(buffer)

def glMultMatrixx(m):
	return lib.glMultMatrixx(m)

def glGetClipPlanef(plane, equation):
	return lib.glGetClipPlanef(plane, equation)

def glFogx(pname, param):
	return lib.glFogx(pname, param)

def glVertexPointer(size, type, stride, pointer):
	return lib.glVertexPointer(size, type, stride, pointer)

def glFogf(pname, param):
	return lib.glFogf(pname, param)

def glIsEnabled(cap):
	return lib.glIsEnabled(cap)

def glStencilOp(fail, zfail, zpass):
	return lib.glStencilOp(fail, zfail, zpass)

def glDepthRangex(n, f):
	return lib.glDepthRangex(n, f)

def glGetPointerv(pname):
	params = ffi.new('void *')
	return lib.glGetPointerv(pname, params)

def glCopyTexImage2D(target, level, internalformat, x, y, width, height, border):
	return lib.glCopyTexImage2D(target, level, internalformat, x, y, width, height, border)

def glLightxv(light, pname):
	params = ffi.new('const GLfixed *')
	return lib.glLightxv(light, pname, params)

def glGetBooleanv(pname):
	data = ffi.new('GLboolean *')
	return lib.glGetBooleanv(pname, data)

def glTexParameterf(target, pname, param):
	return lib.glTexParameterf(target, pname, param)

def glTexParameteri(target, pname, param):
	return lib.glTexParameteri(target, pname, param)

def glColor4ub(red, green, blue, alpha):
	return lib.glColor4ub(red, green, blue, alpha)

def glGetString():
	name = ffi.new('GLenum *')
	return lib.glGetString(name)

def glDeleteTextures(n, textures):
	return lib.glDeleteTextures(n, textures)

def glGetTexEnvfv(target, pname):
	params = ffi.new('GLfloat *')
	return lib.glGetTexEnvfv(target, pname, params)

def glCullFace(mode):
	return lib.glCullFace(mode)

def glGetBufferParameteriv(target, pname):
	params = ffi.new('GLint *')
	return lib.glGetBufferParameteriv(target, pname, params)

def glLightModelfv(pname):
	params = ffi.new('const GLfloat *')
	return lib.glLightModelfv(pname, params)

def glRotatex(angle, x, y, z):
	return lib.glRotatex(angle, x, y, z)

def glRotatef(angle, x, y, z):
	return lib.glRotatef(angle, x, y, z)

def glGetTexEnvxv(target, pname):
	params = ffi.new('GLfixed *')
	return lib.glGetTexEnvxv(target, pname, params)

def glAlphaFunc(func, ref):
	return lib.glAlphaFunc(func, ref)

def glStencilFunc(func, ref, mask):
	return lib.glStencilFunc(func, ref, mask)

def glDeleteBuffers(n, buffers):
	return lib.glDeleteBuffers(n, buffers)

def glScissor(x, y, width, height):
	return lib.glScissor(x, y, width, height)

def glGetFixedv(pname):
	params = ffi.new('GLfixed *')
	return lib.glGetFixedv(pname, params)

def glMaterialfv(face, pname):
	params = ffi.new('const GLfloat *')
	return lib.glMaterialfv(face, pname, params)

def glPointParameterfv(pname):
	params = ffi.new('const GLfloat *')
	return lib.glPointParameterfv(pname, params)

def glGetError():
	return lib.glGetError()

def glGetTexEnviv(target, pname):
	params = ffi.new('GLint *')
	return lib.glGetTexEnviv(target, pname, params)

def glPixelStorei(pname, param):
	return lib.glPixelStorei(pname, param)

def glDepthMask(flag):
	return lib.glDepthMask(flag)

def glCopyTexSubImage2D(target, level, xoffset, yoffset, x, y, width, height):
	return lib.glCopyTexSubImage2D(target, level, xoffset, yoffset, x, y, width, height)

def glPointSize(size):
	return lib.glPointSize(size)

def glDrawArrays(mode, first, count):
	return lib.glDrawArrays(mode, first, count)

def glClear(mask):
	return lib.glClear(mask)

def glTranslatef(x, y, z):
	return lib.glTranslatef(x, y, z)

def glTranslatex(x, y, z):
	return lib.glTranslatex(x, y, z)

def glMaterialf(face, pname, param):
	return lib.glMaterialf(face, pname, param)

def glMaterialx(face, pname, param):
	return lib.glMaterialx(face, pname, param)

def glLightx(light, pname, param):
	return lib.glLightx(light, pname, param)

def glLightf(light, pname, param):
	return lib.glLightf(light, pname, param)

def glSampleCoverage(value, invert):
	return lib.glSampleCoverage(value, invert)

def glTexEnvf(target, pname, param):
	return lib.glTexEnvf(target, pname, param)

def glTexEnvi(target, pname, param):
	return lib.glTexEnvi(target, pname, param)

def glTexEnvx(target, pname, param):
	return lib.glTexEnvx(target, pname, param)

def glLightModelf(pname, param):
	return lib.glLightModelf(pname, param)

def glLightModelx(pname, param):
	return lib.glLightModelx(pname, param)

def glColor4x(red, green, blue, alpha):
	return lib.glColor4x(red, green, blue, alpha)

def glColor4f(red, green, blue, alpha):
	return lib.glColor4f(red, green, blue, alpha)

def glViewport(x, y, width, height):
	return lib.glViewport(x, y, width, height)

def glPointParameterxv(pname):
	params = ffi.new('const GLfixed *')
	return lib.glPointParameterxv(pname, params)

def glBindTexture(target, texture):
	return lib.glBindTexture(target, texture)

def glBindBuffer(target, buffer):
	return lib.glBindBuffer(target, buffer)

def glSampleCoveragex(value, invert):
	return lib.glSampleCoveragex(value, invert)

def glPointParameterf(pname, param):
	return lib.glPointParameterf(pname, param)

def glReadPixels(x, y, width, height, format, type):
	pixels = ffi.new('void *')
	return lib.glReadPixels(x, y, width, height, format, type, pixels)

def glShadeModel(mode):
	return lib.glShadeModel(mode)

def glGenBuffers(n, buffers):
	return lib.glGenBuffers(n, buffers)

def glGetLightxv(light, pname):
	params = ffi.new('GLfixed *')
	return lib.glGetLightxv(light, pname, params)

def glClearColorx(red, green, blue, alpha):
	return lib.glClearColorx(red, green, blue, alpha)

def glFogxv(pname, param):
	return lib.glFogxv(pname, param)

def glDepthFunc(func):
	return lib.glDepthFunc(func)

def glPointParameterx(pname, param):
	return lib.glPointParameterx(pname, param)

def glEnableClientState(array):
	return lib.glEnableClientState(array)

def glAlphaFuncx(func, ref):
	return lib.glAlphaFuncx(func, ref)

def glGetFloatv(pname):
	data = ffi.new('GLfloat *')
	return lib.glGetFloatv(pname, data)

def glGetIntegerv(pname):
	data = ffi.new('GLint *')
	return lib.glGetIntegerv(pname, data)

def glTexImage2D(target, level, internalformat, width, height, border, format, type):
	pixels = ffi.new('const void *')
	return lib.glTexImage2D(target, level, internalformat, width, height, border, format, type, pixels)

def glMultMatrixf(m):
	return lib.glMultMatrixf(m)

def glLineWidth(width):
	return lib.glLineWidth(width)

def glDepthRangef(n, f):
	return lib.glDepthRangef(n, f)

def glLineWidthx(width):
	return lib.glLineWidthx(width)

def glNormalPointer(type, stride, pointer):
	return lib.glNormalPointer(type, stride, pointer)

def glLightfv(light, pname):
	params = ffi.new('const GLfloat *')
	return lib.glLightfv(light, pname, params)

def glTexParameteriv(target, pname):
	params = ffi.new('const GLint *')
	return lib.glTexParameteriv(target, pname, params)

def glFrustumx(l, r, b, t, n, f):
	return lib.glFrustumx(l, r, b, t, n, f)

def glFrustumf(l, r, b, t, n, f):
	return lib.glFrustumf(l, r, b, t, n, f)

def glFlush():
	return lib.glFlush()

def glClearStencil(s):
	return lib.glClearStencil(s)

def glLightModelxv(pname, param):
	return lib.glLightModelxv(pname, param)

def glIsTexture(texture):
	return lib.glIsTexture(texture)

def glPolygonOffset(factor, units):
	return lib.glPolygonOffset(factor, units)

def glMatrixMode(mode):
	return lib.glMatrixMode(mode)

def glFinish():
	return lib.glFinish()

def glTexSubImage2D(target, level, xoffset, yoffset, width, height, format, type):
	pixels = ffi.new('const void *')
	return lib.glTexSubImage2D(target, level, xoffset, yoffset, width, height, format, type, pixels)

def glLogicOp(opcode):
	return lib.glLogicOp(opcode)

def glDrawElements(mode, count, type, indices):
	return lib.glDrawElements(mode, count, type, indices)

def glClientActiveTexture(texture):
	return lib.glClientActiveTexture(texture)

def glDisableClientState(array):
	return lib.glDisableClientState(array)

def glGetClipPlanex(plane, equation):
	return lib.glGetClipPlanex(plane, equation)

def glClearDepthx(depth):
	return lib.glClearDepthx(depth)

def glClearDepthf(d):
	return lib.glClearDepthf(d)

def glMultiTexCoord4x(texture, s, t, r, q):
	return lib.glMultiTexCoord4x(texture, s, t, r, q)

def glMultiTexCoord4f(target, s, t, r, q):
	return lib.glMultiTexCoord4f(target, s, t, r, q)

def glColorMask(red, green, blue, alpha):
	return lib.glColorMask(red, green, blue, alpha)

def glMaterialxv(face, pname, param):
	return lib.glMaterialxv(face, pname, param)

def glPolygonOffsetx(factor, units):
	return lib.glPolygonOffsetx(factor, units)

def glLoadMatrixx(m):
	return lib.glLoadMatrixx(m)

def glLoadMatrixf(m):
	return lib.glLoadMatrixf(m)

def glTexParameterfv(target, pname):
	params = ffi.new('const GLfloat *')
	return lib.glTexParameterfv(target, pname, params)

def glTexParameterxv(target, pname):
	params = ffi.new('const GLfixed *')
	return lib.glTexParameterxv(target, pname, params)

def glTexParameterx(target, pname, param):
	return lib.glTexParameterx(target, pname, param)

def glPointSizex(size):
	return lib.glPointSizex(size)

def glCompressedTexImage2D(target, level, internalformat, width, height, border, imageSize):
	data = ffi.new('const void *')
	return lib.glCompressedTexImage2D(target, level, internalformat, width, height, border, imageSize, data)

def glLoadIdentity():
	return lib.glLoadIdentity()

def glGetMaterialxv(face, pname):
	params = ffi.new('GLfixed *')
	return lib.glGetMaterialxv(face, pname, params)

def glTexEnvxv(target, pname):
	params = ffi.new('const GLfixed *')
	return lib.glTexEnvxv(target, pname, params)

def glGetMaterialfv(face, pname):
	params = ffi.new('GLfloat *')
	return lib.glGetMaterialfv(face, pname, params)

def glOrthox(l, r, b, t, n, f):
	return lib.glOrthox(l, r, b, t, n, f)

def glOrthof(l, r, b, t, n, f):
	return lib.glOrthof(l, r, b, t, n, f)

def glEnable(cap):
	return lib.glEnable(cap)

def glPushMatrix():
	return lib.glPushMatrix()

def glGetTexParameterxv(target, pname):
	params = ffi.new('GLfixed *')
	return lib.glGetTexParameterxv(target, pname, params)

def glGenTextures(n, textures):
	return lib.glGenTextures(n, textures)

def glHint(target, mode):
	return lib.glHint(target, mode)

def glScalef(x, y, z):
	return lib.glScalef(x, y, z)

def glScalex(x, y, z):
	return lib.glScalex(x, y, z)

def glGetTexParameteriv(target, pname):
	params = ffi.new('GLint *')
	return lib.glGetTexParameteriv(target, pname, params)

def glDisable(cap):
	return lib.glDisable(cap)

def glGetLightfv(light, pname):
	params = ffi.new('GLfloat *')
	return lib.glGetLightfv(light, pname, params)

def glPopMatrix():
	return lib.glPopMatrix()

def glActiveTexture(texture):
	return lib.glActiveTexture(texture)

def glTexEnvfv(target, pname):
	params = ffi.new('const GLfloat *')
	return lib.glTexEnvfv(target, pname, params)

def glBufferSubData(target, offset, size):
	data = ffi.new('const void *')
	return lib.glBufferSubData(target, offset, size, data)

def glTexCoordPointer(size, type, stride, pointer):
	return lib.glTexCoordPointer(size, type, stride, pointer)

def glTexEnviv(target, pname):
	params = ffi.new('const GLint *')
	return lib.glTexEnviv(target, pname, params)

def glBlendFunc(sfactor, dfactor):
	return lib.glBlendFunc(sfactor, dfactor)

def glClearColor(red, green, blue, alpha):
	return lib.glClearColor(red, green, blue, alpha)

def glStencilMask(mask):
	return lib.glStencilMask(mask)

def glNormal3f(nx, ny, nz):
	return lib.glNormal3f(nx, ny, nz)

def glCompressedTexSubImage2D(target, level, xoffset, yoffset, width, height, format, imageSize):
	data = ffi.new('const void *')
	return lib.glCompressedTexSubImage2D(target, level, xoffset, yoffset, width, height, format, imageSize, data)

def glGetTexParameterfv(target, pname):
	params = ffi.new('GLfloat *')
	return lib.glGetTexParameterfv(target, pname, params)

def glBufferData(target, size, usage):
	data = ffi.new('const void *')
	return lib.glBufferData(target, size, data, usage)

def glColorPointer(size, type, stride, pointer):
	return lib.glColorPointer(size, type, stride, pointer)

def glNormal3x(nx, ny, nz):
	return lib.glNormal3x(nx, ny, nz)

def glClipPlanex(plane, equation):
	return lib.glClipPlanex(plane, equation)

def glClipPlanef(p, eqn):
	return lib.glClipPlanef(p, eqn)

def glFrontFace(mode):
	return lib.glFrontFace(mode)

