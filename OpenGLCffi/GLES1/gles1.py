@params('pname', 'params')
def glFogfv(pname):
	pass


@params('buffer',)
def glIsBuffer(buffer):
	pass


@params('m',)
def glMultMatrixx(m):
	pass


@params('plane', 'equation')
def glGetClipPlanef(plane, equation):
	pass


@params('pname', 'param')
def glFogx(pname, param):
	pass


@params('size', 'type', 'stride', 'pointer')
def glVertexPointer(size, type, stride, pointer):
	pass


@params('pname', 'param')
def glFogf(pname, param):
	pass


@params('cap',)
def glIsEnabled(cap):
	pass


@params('fail', 'zfail', 'zpass')
def glStencilOp(fail, zfail, zpass):
	pass


@params('n', 'f')
def glDepthRangex(n, f):
	pass


@params('pname', 'params')
def glGetPointerv(pname):
	pass


@params('target', 'level', 'internalformat', 'x', 'y', 'width', 'height', 'border')
def glCopyTexImage2D(target, level, internalformat, x, y, width, height, border):
	pass


@params('light', 'pname', 'params')
def glLightxv(light, pname):
	pass


@params('pname', 'data')
def glGetBooleanv(pname):
	pass


@params('target', 'pname', 'param')
def glTexParameterf(target, pname, param):
	pass


@params('target', 'pname', 'param')
def glTexParameteri(target, pname, param):
	pass


@params('red', 'green', 'blue', 'alpha')
def glColor4ub(red, green, blue, alpha):
	pass


@params('name',)
def glGetString():
	pass


@params('n', 'textures')
def glDeleteTextures(n, textures):
	pass


@params('target', 'pname', 'params')
def glGetTexEnvfv(target, pname):
	pass


@params('mode',)
def glCullFace(mode):
	pass


@params('target', 'pname', 'params')
def glGetBufferParameteriv(target, pname):
	pass


@params('pname', 'params')
def glLightModelfv(pname):
	pass


@params('angle', 'x', 'y', 'z')
def glRotatex(angle, x, y, z):
	pass


@params('angle', 'x', 'y', 'z')
def glRotatef(angle, x, y, z):
	pass


@params('target', 'pname', 'params')
def glGetTexEnvxv(target, pname):
	pass


@params('func', 'ref')
def glAlphaFunc(func, ref):
	pass


@params('func', 'ref', 'mask')
def glStencilFunc(func, ref, mask):
	pass


@params('n', 'buffers')
def glDeleteBuffers(n, buffers):
	pass


@params('x', 'y', 'width', 'height')
def glScissor(x, y, width, height):
	pass


@params('pname', 'params')
def glGetFixedv(pname):
	pass


@params('face', 'pname', 'params')
def glMaterialfv(face, pname):
	pass


@params('pname', 'params')
def glPointParameterfv(pname):
	pass


@params()
def glGetError():
	pass


@params('target', 'pname', 'params')
def glGetTexEnviv(target, pname):
	pass


@params('pname', 'param')
def glPixelStorei(pname, param):
	pass


@params('flag',)
def glDepthMask(flag):
	pass


@params('target', 'level', 'xoffset', 'yoffset', 'x', 'y', 'width', 'height')
def glCopyTexSubImage2D(target, level, xoffset, yoffset, x, y, width, height):
	pass


@params('size',)
def glPointSize(size):
	pass


@params('mode', 'first', 'count')
def glDrawArrays(mode, first, count):
	pass


@params('mask',)
def glClear(mask):
	pass


@params('x', 'y', 'z')
def glTranslatef(x, y, z):
	pass


@params('x', 'y', 'z')
def glTranslatex(x, y, z):
	pass


@params('face', 'pname', 'param')
def glMaterialf(face, pname, param):
	pass


@params('face', 'pname', 'param')
def glMaterialx(face, pname, param):
	pass


@params('light', 'pname', 'param')
def glLightx(light, pname, param):
	pass


@params('light', 'pname', 'param')
def glLightf(light, pname, param):
	pass


@params('value', 'invert')
def glSampleCoverage(value, invert):
	pass


@params('target', 'pname', 'param')
def glTexEnvf(target, pname, param):
	pass


@params('target', 'pname', 'param')
def glTexEnvi(target, pname, param):
	pass


@params('target', 'pname', 'param')
def glTexEnvx(target, pname, param):
	pass


@params('pname', 'param')
def glLightModelf(pname, param):
	pass


@params('pname', 'param')
def glLightModelx(pname, param):
	pass


@params('red', 'green', 'blue', 'alpha')
def glColor4x(red, green, blue, alpha):
	pass


@params('red', 'green', 'blue', 'alpha')
def glColor4f(red, green, blue, alpha):
	pass


@params('x', 'y', 'width', 'height')
def glViewport(x, y, width, height):
	pass


@params('pname', 'params')
def glPointParameterxv(pname):
	pass


@params('target', 'texture')
def glBindTexture(target, texture):
	pass


@params('target', 'buffer')
def glBindBuffer(target, buffer):
	pass


@params('value', 'invert')
def glSampleCoveragex(value, invert):
	pass


@params('pname', 'param')
def glPointParameterf(pname, param):
	pass


@params('x', 'y', 'width', 'height', 'format', 'type', 'pixels')
def glReadPixels(x, y, width, height, format, type):
	pass


@params('mode',)
def glShadeModel(mode):
	pass


@params('n', 'buffers')
def glGenBuffers(n, buffers):
	pass


@params('light', 'pname', 'params')
def glGetLightxv(light, pname):
	pass


@params('red', 'green', 'blue', 'alpha')
def glClearColorx(red, green, blue, alpha):
	pass


@params('pname', 'param')
def glFogxv(pname, param):
	pass


@params('func',)
def glDepthFunc(func):
	pass


@params('pname', 'param')
def glPointParameterx(pname, param):
	pass


@params('array',)
def glEnableClientState(array):
	pass


@params('func', 'ref')
def glAlphaFuncx(func, ref):
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


@params('m',)
def glMultMatrixf(m):
	pass


@params('width',)
def glLineWidth(width):
	pass


@params('n', 'f')
def glDepthRangef(n, f):
	pass


@params('width',)
def glLineWidthx(width):
	pass


@params('type', 'stride', 'pointer')
def glNormalPointer(type, stride, pointer):
	pass


@params('light', 'pname', 'params')
def glLightfv(light, pname):
	pass


@params('target', 'pname', 'params')
def glTexParameteriv(target, pname):
	pass


@params('l', 'r', 'b', 't', 'n', 'f')
def glFrustumx(l, r, b, t, n, f):
	pass


@params('l', 'r', 'b', 't', 'n', 'f')
def glFrustumf(l, r, b, t, n, f):
	pass


@params()
def glFlush():
	pass


@params('s',)
def glClearStencil(s):
	pass


@params('pname', 'param')
def glLightModelxv(pname, param):
	pass


@params('texture',)
def glIsTexture(texture):
	pass


@params('factor', 'units')
def glPolygonOffset(factor, units):
	pass


@params('mode',)
def glMatrixMode(mode):
	pass


@params()
def glFinish():
	pass


@params('target', 'level', 'xoffset', 'yoffset', 'width', 'height', 'format', 'type', 'pixels')
def glTexSubImage2D(target, level, xoffset, yoffset, width, height, format, type):
	pass


@params('opcode',)
def glLogicOp(opcode):
	pass


@params('mode', 'count', 'type', 'indices')
def glDrawElements(mode, count, type, indices):
	pass


@params('texture',)
def glClientActiveTexture(texture):
	pass


@params('array',)
def glDisableClientState(array):
	pass


@params('plane', 'equation')
def glGetClipPlanex(plane, equation):
	pass


@params('depth',)
def glClearDepthx(depth):
	pass


@params('d',)
def glClearDepthf(d):
	pass


@params('texture', 's', 't', 'r', 'q')
def glMultiTexCoord4x(texture, s, t, r, q):
	pass


@params('target', 's', 't', 'r', 'q')
def glMultiTexCoord4f(target, s, t, r, q):
	pass


@params('red', 'green', 'blue', 'alpha')
def glColorMask(red, green, blue, alpha):
	pass


@params('face', 'pname', 'param')
def glMaterialxv(face, pname, param):
	pass


@params('factor', 'units')
def glPolygonOffsetx(factor, units):
	pass


@params('m',)
def glLoadMatrixx(m):
	pass


@params('m',)
def glLoadMatrixf(m):
	pass


@params('target', 'pname', 'params')
def glTexParameterfv(target, pname):
	pass


@params('target', 'pname', 'params')
def glTexParameterxv(target, pname):
	pass


@params('target', 'pname', 'param')
def glTexParameterx(target, pname, param):
	pass


@params('size',)
def glPointSizex(size):
	pass


@params('target', 'level', 'internalformat', 'width', 'height', 'border', 'imageSize', 'data')
def glCompressedTexImage2D(target, level, internalformat, width, height, border, imageSize):
	pass


@params()
def glLoadIdentity():
	pass


@params('face', 'pname', 'params')
def glGetMaterialxv(face, pname):
	pass


@params('target', 'pname', 'params')
def glTexEnvxv(target, pname):
	pass


@params('face', 'pname', 'params')
def glGetMaterialfv(face, pname):
	pass


@params('l', 'r', 'b', 't', 'n', 'f')
def glOrthox(l, r, b, t, n, f):
	pass


@params('l', 'r', 'b', 't', 'n', 'f')
def glOrthof(l, r, b, t, n, f):
	pass


@params('cap',)
def glEnable(cap):
	pass


@params()
def glPushMatrix():
	pass


@params('target', 'pname', 'params')
def glGetTexParameterxv(target, pname):
	pass


@params('n', 'textures')
def glGenTextures(n, textures):
	pass


@params('target', 'mode')
def glHint(target, mode):
	pass


@params('x', 'y', 'z')
def glScalef(x, y, z):
	pass


@params('x', 'y', 'z')
def glScalex(x, y, z):
	pass


@params('target', 'pname', 'params')
def glGetTexParameteriv(target, pname):
	pass


@params('cap',)
def glDisable(cap):
	pass


@params('light', 'pname', 'params')
def glGetLightfv(light, pname):
	pass


@params()
def glPopMatrix():
	pass


@params('texture',)
def glActiveTexture(texture):
	pass


@params('target', 'pname', 'params')
def glTexEnvfv(target, pname):
	pass


@params('target', 'offset', 'size', 'data')
def glBufferSubData(target, offset, size):
	pass


@params('size', 'type', 'stride', 'pointer')
def glTexCoordPointer(size, type, stride, pointer):
	pass


@params('target', 'pname', 'params')
def glTexEnviv(target, pname):
	pass


@params('sfactor', 'dfactor')
def glBlendFunc(sfactor, dfactor):
	pass


@params('red', 'green', 'blue', 'alpha')
def glClearColor(red, green, blue, alpha):
	pass


@params('mask',)
def glStencilMask(mask):
	pass


@params('nx', 'ny', 'nz')
def glNormal3f(nx, ny, nz):
	pass


@params('target', 'level', 'xoffset', 'yoffset', 'width', 'height', 'format', 'imageSize', 'data')
def glCompressedTexSubImage2D(target, level, xoffset, yoffset, width, height, format, imageSize):
	pass


@params('target', 'pname', 'params')
def glGetTexParameterfv(target, pname):
	pass


@params('target', 'size', 'data', 'usage')
def glBufferData(target, size, usage):
	pass


@params('size', 'type', 'stride', 'pointer')
def glColorPointer(size, type, stride, pointer):
	pass


@params('nx', 'ny', 'nz')
def glNormal3x(nx, ny, nz):
	pass


@params('plane', 'equation')
def glClipPlanex(plane, equation):
	pass


@params('p', 'eqn')
def glClipPlanef(p, eqn):
	pass


@params('mode',)
def glFrontFace(mode):
	pass


