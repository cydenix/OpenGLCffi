from OpenGLCffi.GLES1 import params
@params('pname', 'params', api='gles1')
def glFogfv(pname, params):
	pass


@params('buffer', api='gles1')
def glIsBuffer(buffer):
	pass


@params('m', api='gles1')
def glMultMatrixx(m):
	pass


@params('plane', 'equation', api='gles1')
def glGetClipPlanef(plane):
	pass


@params('pname', 'param', api='gles1')
def glFogx(pname, param):
	pass


@params('size', 'type', 'stride', 'pointer', api='gles1')
def glVertexPointer(size, type, stride, pointer):
	pass


@params('pname', 'param', api='gles1')
def glFogf(pname, param):
	pass


@params('cap', api='gles1')
def glIsEnabled(cap):
	pass


@params('fail', 'zfail', 'zpass', api='gles1')
def glStencilOp(fail, zfail, zpass):
	pass


@params('n', 'f', api='gles1')
def glDepthRangex(n, f):
	pass


@params('pname', 'params', api='gles1')
def glGetPointerv(pname):
	pass


@params('target', 'level', 'internalformat', 'x', 'y', 'width', 'height', 'border', api='gles1')
def glCopyTexImage2D(target, level, internalformat, x, y, width, height, border):
	pass


@params('light', 'pname', 'params', api='gles1')
def glLightxv(light, pname, params):
	pass


@params('pname', 'data', api='gles1')
def glGetBooleanv(pname):
	pass


@params('target', 'pname', 'param', api='gles1')
def glTexParameterf(target, pname, param):
	pass


@params('target', 'pname', 'param', api='gles1')
def glTexParameteri(target, pname, param):
	pass


@params('red', 'green', 'blue', 'alpha', api='gles1')
def glColor4ub(red, green, blue, alpha):
	pass


@params('name', api='gles1')
def glGetString(name):
	pass


@params('n', 'textures', api='gles1')
def glDeleteTextures(n, textures):
	pass


@params('target', 'pname', 'params', api='gles1')
def glGetTexEnvfv(target, pname):
	pass


@params('mode', api='gles1')
def glCullFace(mode):
	pass


@params('target', 'pname', 'params', api='gles1')
def glGetBufferParameteriv(target, pname):
	pass


@params('pname', 'params', api='gles1')
def glLightModelfv(pname, params):
	pass


@params('angle', 'x', 'y', 'z', api='gles1')
def glRotatex(angle, x, y, z):
	pass


@params('angle', 'x', 'y', 'z', api='gles1')
def glRotatef(angle, x, y, z):
	pass


@params('target', 'pname', 'params', api='gles1')
def glGetTexEnvxv(target, pname):
	pass


@params('func', 'ref', api='gles1')
def glAlphaFunc(func, ref):
	pass


@params('func', 'ref', 'mask', api='gles1')
def glStencilFunc(func, ref, mask):
	pass


@params('n', 'buffers', api='gles1')
def glDeleteBuffers(n, buffers):
	pass


@params('x', 'y', 'width', 'height', api='gles1')
def glScissor(x, y, width, height):
	pass


@params('pname', 'params', api='gles1')
def glGetFixedv(pname):
	pass


@params('face', 'pname', 'params', api='gles1')
def glMaterialfv(face, pname, params):
	pass


@params('pname', 'params', api='gles1')
def glPointParameterfv(pname, params):
	pass


@params(api = 'gles1')
def glGetError():
	pass


@params('target', 'pname', 'params', api='gles1')
def glGetTexEnviv(target, pname):
	pass


@params('pname', 'param', api='gles1')
def glPixelStorei(pname, param):
	pass


@params('flag', api='gles1')
def glDepthMask(flag):
	pass


@params('target', 'level', 'xoffset', 'yoffset', 'x', 'y', 'width', 'height', api='gles1')
def glCopyTexSubImage2D(target, level, xoffset, yoffset, x, y, width, height):
	pass


@params('size', api='gles1')
def glPointSize(size):
	pass


@params('mode', 'first', 'count', api='gles1')
def glDrawArrays(mode, first, count):
	pass


@params('mask', api='gles1')
def glClear(mask):
	pass


@params('x', 'y', 'z', api='gles1')
def glTranslatef(x, y, z):
	pass


@params('x', 'y', 'z', api='gles1')
def glTranslatex(x, y, z):
	pass


@params('face', 'pname', 'param', api='gles1')
def glMaterialf(face, pname, param):
	pass


@params('face', 'pname', 'param', api='gles1')
def glMaterialx(face, pname, param):
	pass


@params('light', 'pname', 'param', api='gles1')
def glLightx(light, pname, param):
	pass


@params('light', 'pname', 'param', api='gles1')
def glLightf(light, pname, param):
	pass


@params('value', 'invert', api='gles1')
def glSampleCoverage(value, invert):
	pass


@params('target', 'pname', 'param', api='gles1')
def glTexEnvf(target, pname, param):
	pass


@params('target', 'pname', 'param', api='gles1')
def glTexEnvi(target, pname, param):
	pass


@params('target', 'pname', 'param', api='gles1')
def glTexEnvx(target, pname, param):
	pass


@params('pname', 'param', api='gles1')
def glLightModelf(pname, param):
	pass


@params('pname', 'param', api='gles1')
def glLightModelx(pname, param):
	pass


@params('red', 'green', 'blue', 'alpha', api='gles1')
def glColor4x(red, green, blue, alpha):
	pass


@params('red', 'green', 'blue', 'alpha', api='gles1')
def glColor4f(red, green, blue, alpha):
	pass


@params('x', 'y', 'width', 'height', api='gles1')
def glViewport(x, y, width, height):
	pass


@params('pname', 'params', api='gles1')
def glPointParameterxv(pname, params):
	pass


@params('target', 'texture', api='gles1')
def glBindTexture(target, texture):
	pass


@params('target', 'buffer', api='gles1')
def glBindBuffer(target, buffer):
	pass


@params('value', 'invert', api='gles1')
def glSampleCoveragex(value, invert):
	pass


@params('pname', 'param', api='gles1')
def glPointParameterf(pname, param):
	pass


@params('x', 'y', 'width', 'height', 'format', 'type', 'pixels', api='gles1')
def glReadPixels(x, y, width, height, format, type, pixels):
	pass


@params('mode', api='gles1')
def glShadeModel(mode):
	pass


@params('n', 'buffers', api='gles1')
def glGenBuffers(n):
	pass


@params('light', 'pname', 'params', api='gles1')
def glGetLightxv(light, pname):
	pass


@params('red', 'green', 'blue', 'alpha', api='gles1')
def glClearColorx(red, green, blue, alpha):
	pass


@params('pname', 'param', api='gles1')
def glFogxv(pname, param):
	pass


@params('func', api='gles1')
def glDepthFunc(func):
	pass


@params('pname', 'param', api='gles1')
def glPointParameterx(pname, param):
	pass


@params('array', api='gles1')
def glEnableClientState(array):
	pass


@params('func', 'ref', api='gles1')
def glAlphaFuncx(func, ref):
	pass


@params('pname', 'data', api='gles1')
def glGetFloatv(pname):
	pass


@params('pname', 'data', api='gles1')
def glGetIntegerv(pname):
	pass


@params('target', 'level', 'internalformat', 'width', 'height', 'border', 'format', 'type', 'pixels', api='gles1')
def glTexImage2D(target, level, internalformat, width, height, border, format, type, pixels):
	pass


@params('m', api='gles1')
def glMultMatrixf(m):
	pass


@params('width', api='gles1')
def glLineWidth(width):
	pass


@params('n', 'f', api='gles1')
def glDepthRangef(n, f):
	pass


@params('width', api='gles1')
def glLineWidthx(width):
	pass


@params('type', 'stride', 'pointer', api='gles1')
def glNormalPointer(type, stride, pointer):
	pass


@params('light', 'pname', 'params', api='gles1')
def glLightfv(light, pname, params):
	pass


@params('target', 'pname', 'params', api='gles1')
def glTexParameteriv(target, pname, params):
	pass


@params('l', 'r', 'b', 't', 'n', 'f', api='gles1')
def glFrustumx(l, r, b, t, n, f):
	pass


@params('l', 'r', 'b', 't', 'n', 'f', api='gles1')
def glFrustumf(l, r, b, t, n, f):
	pass


@params(api = 'gles1')
def glFlush():
	pass


@params('s', api='gles1')
def glClearStencil(s):
	pass


@params('pname', 'param', api='gles1')
def glLightModelxv(pname, param):
	pass


@params('texture', api='gles1')
def glIsTexture(texture):
	pass


@params('factor', 'units', api='gles1')
def glPolygonOffset(factor, units):
	pass


@params('mode', api='gles1')
def glMatrixMode(mode):
	pass


@params(api = 'gles1')
def glFinish():
	pass


@params('target', 'level', 'xoffset', 'yoffset', 'width', 'height', 'format', 'type', 'pixels', api='gles1')
def glTexSubImage2D(target, level, xoffset, yoffset, width, height, format, type, pixels):
	pass


@params('opcode', api='gles1')
def glLogicOp(opcode):
	pass


@params('mode', 'count', 'type', 'indices', api='gles1')
def glDrawElements(mode, count, type, indices):
	pass


@params('texture', api='gles1')
def glClientActiveTexture(texture):
	pass


@params('array', api='gles1')
def glDisableClientState(array):
	pass


@params('plane', 'equation', api='gles1')
def glGetClipPlanex(plane):
	pass


@params('depth', api='gles1')
def glClearDepthx(depth):
	pass


@params('d', api='gles1')
def glClearDepthf(d):
	pass


@params('texture', 's', 't', 'r', 'q', api='gles1')
def glMultiTexCoord4x(texture, s, t, r, q):
	pass


@params('target', 's', 't', 'r', 'q', api='gles1')
def glMultiTexCoord4f(target, s, t, r, q):
	pass


@params('red', 'green', 'blue', 'alpha', api='gles1')
def glColorMask(red, green, blue, alpha):
	pass


@params('face', 'pname', 'param', api='gles1')
def glMaterialxv(face, pname, param):
	pass


@params('factor', 'units', api='gles1')
def glPolygonOffsetx(factor, units):
	pass


@params('m', api='gles1')
def glLoadMatrixx(m):
	pass


@params('m', api='gles1')
def glLoadMatrixf(m):
	pass


@params('target', 'pname', 'params', api='gles1')
def glTexParameterfv(target, pname, params):
	pass


@params('target', 'pname', 'params', api='gles1')
def glTexParameterxv(target, pname, params):
	pass


@params('target', 'pname', 'param', api='gles1')
def glTexParameterx(target, pname, param):
	pass


@params('size', api='gles1')
def glPointSizex(size):
	pass


@params('target', 'level', 'internalformat', 'width', 'height', 'border', 'imageSize', 'data', api='gles1')
def glCompressedTexImage2D(target, level, internalformat, width, height, border, imageSize, data):
	pass


@params(api = 'gles1')
def glLoadIdentity():
	pass


@params('face', 'pname', 'params', api='gles1')
def glGetMaterialxv(face, pname):
	pass


@params('target', 'pname', 'params', api='gles1')
def glTexEnvxv(target, pname, params):
	pass


@params('face', 'pname', 'params', api='gles1')
def glGetMaterialfv(face, pname):
	pass


@params('l', 'r', 'b', 't', 'n', 'f', api='gles1')
def glOrthox(l, r, b, t, n, f):
	pass


@params('l', 'r', 'b', 't', 'n', 'f', api='gles1')
def glOrthof(l, r, b, t, n, f):
	pass


@params('cap', api='gles1')
def glEnable(cap):
	pass


@params(api = 'gles1')
def glPushMatrix():
	pass


@params('target', 'pname', 'params', api='gles1')
def glGetTexParameterxv(target, pname):
	pass


@params('n', 'textures', api='gles1')
def glGenTextures(n):
	pass


@params('target', 'mode', api='gles1')
def glHint(target, mode):
	pass


@params('x', 'y', 'z', api='gles1')
def glScalef(x, y, z):
	pass


@params('x', 'y', 'z', api='gles1')
def glScalex(x, y, z):
	pass


@params('target', 'pname', 'params', api='gles1')
def glGetTexParameteriv(target, pname):
	pass


@params('cap', api='gles1')
def glDisable(cap):
	pass


@params('light', 'pname', 'params', api='gles1')
def glGetLightfv(light, pname):
	pass


@params(api = 'gles1')
def glPopMatrix():
	pass


@params('texture', api='gles1')
def glActiveTexture(texture):
	pass


@params('target', 'pname', 'params', api='gles1')
def glTexEnvfv(target, pname, params):
	pass


@params('target', 'offset', 'size', 'data', api='gles1')
def glBufferSubData(target, offset, size, data):
	pass


@params('size', 'type', 'stride', 'pointer', api='gles1')
def glTexCoordPointer(size, type, stride, pointer):
	pass


@params('target', 'pname', 'params', api='gles1')
def glTexEnviv(target, pname, params):
	pass


@params('sfactor', 'dfactor', api='gles1')
def glBlendFunc(sfactor, dfactor):
	pass


@params('red', 'green', 'blue', 'alpha', api='gles1')
def glClearColor(red, green, blue, alpha):
	pass


@params('mask', api='gles1')
def glStencilMask(mask):
	pass


@params('nx', 'ny', 'nz', api='gles1')
def glNormal3f(nx, ny, nz):
	pass


@params('target', 'level', 'xoffset', 'yoffset', 'width', 'height', 'format', 'imageSize', 'data', api='gles1')
def glCompressedTexSubImage2D(target, level, xoffset, yoffset, width, height, format, imageSize, data):
	pass


@params('target', 'pname', 'params', api='gles1')
def glGetTexParameterfv(target, pname):
	pass


@params('target', 'size', 'data', 'usage', api='gles1')
def glBufferData(target, size, data, usage):
	pass


@params('size', 'type', 'stride', 'pointer', api='gles1')
def glColorPointer(size, type, stride, pointer):
	pass


@params('nx', 'ny', 'nz', api='gles1')
def glNormal3x(nx, ny, nz):
	pass


@params('plane', 'equation', api='gles1')
def glClipPlanex(plane, equation):
	pass


@params('p', 'eqn', api='gles1')
def glClipPlanef(p, eqn):
	pass


@params('mode', api='gles1')
def glFrontFace(mode):
	pass


