from OpenGLCffi.GLES1 import params
@params(api='gles1', prms=['pname', 'params'])
def glFogfv(pname, params):
	pass


@params(api='gles1', prms=['buffer'])
def glIsBuffer(buffer):
	pass


@params(api='gles1', prms=['m'])
def glMultMatrixx(m):
	pass


@params(api='gles1', prms=['plane', 'equation'])
def glGetClipPlanef(plane):
	pass


@params(api='gles1', prms=['pname', 'param'])
def glFogx(pname, param):
	pass


@params(api='gles1', prms=['size', 'type', 'stride', 'pointer'])
def glVertexPointer(size, type, stride, pointer):
	pass


@params(api='gles1', prms=['pname', 'param'])
def glFogf(pname, param):
	pass


@params(api='gles1', prms=['cap'])
def glIsEnabled(cap):
	pass


@params(api='gles1', prms=['fail', 'zfail', 'zpass'])
def glStencilOp(fail, zfail, zpass):
	pass


@params(api='gles1', prms=['n', 'f'])
def glDepthRangex(n, f):
	pass


@params(api='gles1', prms=['pname', 'params'])
def glGetPointerv(pname):
	pass


@params(api='gles1', prms=['target', 'level', 'internalformat', 'x', 'y', 'width', 'height', 'border'])
def glCopyTexImage2D(target, level, internalformat, x, y, width, height, border):
	pass


@params(api='gles1', prms=['light', 'pname', 'params'])
def glLightxv(light, pname, params):
	pass


@params(api='gles1', prms=['pname', 'data'])
def glGetBooleanv(pname):
	pass


@params(api='gles1', prms=['target', 'pname', 'param'])
def glTexParameterf(target, pname, param):
	pass


@params(api='gles1', prms=['target', 'pname', 'param'])
def glTexParameteri(target, pname, param):
	pass


@params(api='gles1', prms=['red', 'green', 'blue', 'alpha'])
def glColor4ub(red, green, blue, alpha):
	pass


@params(api='gles1', prms=['name'])
def glGetString(name):
	pass


@params(api='gles1', prms=['n', 'textures'])
def glDeleteTextures(n, textures):
	pass


@params(api='gles1', prms=['target', 'pname', 'params'])
def glGetTexEnvfv(target, pname):
	pass


@params(api='gles1', prms=['mode'])
def glCullFace(mode):
	pass


@params(api='gles1', prms=['target', 'pname', 'params'])
def glGetBufferParameteriv(target, pname):
	pass


@params(api='gles1', prms=['pname', 'params'])
def glLightModelfv(pname, params):
	pass


@params(api='gles1', prms=['angle', 'x', 'y', 'z'])
def glRotatex(angle, x, y, z):
	pass


@params(api='gles1', prms=['angle', 'x', 'y', 'z'])
def glRotatef(angle, x, y, z):
	pass


@params(api='gles1', prms=['target', 'pname', 'params'])
def glGetTexEnvxv(target, pname):
	pass


@params(api='gles1', prms=['func', 'ref'])
def glAlphaFunc(func, ref):
	pass


@params(api='gles1', prms=['func', 'ref', 'mask'])
def glStencilFunc(func, ref, mask):
	pass


@params(api='gles1', prms=['n', 'buffers'])
def glDeleteBuffers(n, buffers):
	pass


@params(api='gles1', prms=['x', 'y', 'width', 'height'])
def glScissor(x, y, width, height):
	pass


@params(api='gles1', prms=['pname', 'params'])
def glGetFixedv(pname):
	pass


@params(api='gles1', prms=['face', 'pname', 'params'])
def glMaterialfv(face, pname, params):
	pass


@params(api='gles1', prms=['pname', 'params'])
def glPointParameterfv(pname, params):
	pass


@params(api='gles1', prms=[])
def glGetError():
	pass


@params(api='gles1', prms=['target', 'pname', 'params'])
def glGetTexEnviv(target, pname):
	pass


@params(api='gles1', prms=['pname', 'param'])
def glPixelStorei(pname, param):
	pass


@params(api='gles1', prms=['flag'])
def glDepthMask(flag):
	pass


@params(api='gles1', prms=['target', 'level', 'xoffset', 'yoffset', 'x', 'y', 'width', 'height'])
def glCopyTexSubImage2D(target, level, xoffset, yoffset, x, y, width, height):
	pass


@params(api='gles1', prms=['size'])
def glPointSize(size):
	pass


@params(api='gles1', prms=['mode', 'first', 'count'])
def glDrawArrays(mode, first, count):
	pass


@params(api='gles1', prms=['mask'])
def glClear(mask):
	pass


@params(api='gles1', prms=['x', 'y', 'z'])
def glTranslatef(x, y, z):
	pass


@params(api='gles1', prms=['x', 'y', 'z'])
def glTranslatex(x, y, z):
	pass


@params(api='gles1', prms=['face', 'pname', 'param'])
def glMaterialf(face, pname, param):
	pass


@params(api='gles1', prms=['face', 'pname', 'param'])
def glMaterialx(face, pname, param):
	pass


@params(api='gles1', prms=['light', 'pname', 'param'])
def glLightx(light, pname, param):
	pass


@params(api='gles1', prms=['light', 'pname', 'param'])
def glLightf(light, pname, param):
	pass


@params(api='gles1', prms=['value', 'invert'])
def glSampleCoverage(value, invert):
	pass


@params(api='gles1', prms=['target', 'pname', 'param'])
def glTexEnvf(target, pname, param):
	pass


@params(api='gles1', prms=['target', 'pname', 'param'])
def glTexEnvi(target, pname, param):
	pass


@params(api='gles1', prms=['target', 'pname', 'param'])
def glTexEnvx(target, pname, param):
	pass


@params(api='gles1', prms=['pname', 'param'])
def glLightModelf(pname, param):
	pass


@params(api='gles1', prms=['pname', 'param'])
def glLightModelx(pname, param):
	pass


@params(api='gles1', prms=['red', 'green', 'blue', 'alpha'])
def glColor4x(red, green, blue, alpha):
	pass


@params(api='gles1', prms=['red', 'green', 'blue', 'alpha'])
def glColor4f(red, green, blue, alpha):
	pass


@params(api='gles1', prms=['x', 'y', 'width', 'height'])
def glViewport(x, y, width, height):
	pass


@params(api='gles1', prms=['pname', 'params'])
def glPointParameterxv(pname, params):
	pass


@params(api='gles1', prms=['target', 'texture'])
def glBindTexture(target, texture):
	pass


@params(api='gles1', prms=['target', 'buffer'])
def glBindBuffer(target, buffer):
	pass


@params(api='gles1', prms=['value', 'invert'])
def glSampleCoveragex(value, invert):
	pass


@params(api='gles1', prms=['pname', 'param'])
def glPointParameterf(pname, param):
	pass


@params(api='gles1', prms=['x', 'y', 'width', 'height', 'format', 'type', 'pixels'])
def glReadPixels(x, y, width, height, format, type, pixels):
	pass


@params(api='gles1', prms=['mode'])
def glShadeModel(mode):
	pass


@params(api='gles1', prms=['n', 'buffers'])
def glGenBuffers(n):
	pass


@params(api='gles1', prms=['light', 'pname', 'params'])
def glGetLightxv(light, pname):
	pass


@params(api='gles1', prms=['red', 'green', 'blue', 'alpha'])
def glClearColorx(red, green, blue, alpha):
	pass


@params(api='gles1', prms=['pname', 'param'])
def glFogxv(pname, param):
	pass


@params(api='gles1', prms=['func'])
def glDepthFunc(func):
	pass


@params(api='gles1', prms=['pname', 'param'])
def glPointParameterx(pname, param):
	pass


@params(api='gles1', prms=['array'])
def glEnableClientState(array):
	pass


@params(api='gles1', prms=['func', 'ref'])
def glAlphaFuncx(func, ref):
	pass


@params(api='gles1', prms=['pname', 'data'])
def glGetFloatv(pname):
	pass


@params(api='gles1', prms=['pname', 'data'])
def glGetIntegerv(pname):
	pass


@params(api='gles1', prms=['target', 'level', 'internalformat', 'width', 'height', 'border', 'format', 'type', 'pixels'])
def glTexImage2D(target, level, internalformat, width, height, border, format, type, pixels):
	pass


@params(api='gles1', prms=['m'])
def glMultMatrixf(m):
	pass


@params(api='gles1', prms=['width'])
def glLineWidth(width):
	pass


@params(api='gles1', prms=['n', 'f'])
def glDepthRangef(n, f):
	pass


@params(api='gles1', prms=['width'])
def glLineWidthx(width):
	pass


@params(api='gles1', prms=['type', 'stride', 'pointer'])
def glNormalPointer(type, stride, pointer):
	pass


@params(api='gles1', prms=['light', 'pname', 'params'])
def glLightfv(light, pname, params):
	pass


@params(api='gles1', prms=['target', 'pname', 'params'])
def glTexParameteriv(target, pname, params):
	pass


@params(api='gles1', prms=['l', 'r', 'b', 't', 'n', 'f'])
def glFrustumx(l, r, b, t, n, f):
	pass


@params(api='gles1', prms=['l', 'r', 'b', 't', 'n', 'f'])
def glFrustumf(l, r, b, t, n, f):
	pass


@params(api='gles1', prms=[])
def glFlush():
	pass


@params(api='gles1', prms=['s'])
def glClearStencil(s):
	pass


@params(api='gles1', prms=['pname', 'param'])
def glLightModelxv(pname, param):
	pass


@params(api='gles1', prms=['texture'])
def glIsTexture(texture):
	pass


@params(api='gles1', prms=['factor', 'units'])
def glPolygonOffset(factor, units):
	pass


@params(api='gles1', prms=['mode'])
def glMatrixMode(mode):
	pass


@params(api='gles1', prms=[])
def glFinish():
	pass


@params(api='gles1', prms=['target', 'level', 'xoffset', 'yoffset', 'width', 'height', 'format', 'type', 'pixels'])
def glTexSubImage2D(target, level, xoffset, yoffset, width, height, format, type, pixels):
	pass


@params(api='gles1', prms=['opcode'])
def glLogicOp(opcode):
	pass


@params(api='gles1', prms=['mode', 'count', 'type', 'indices'])
def glDrawElements(mode, count, type, indices):
	pass


@params(api='gles1', prms=['texture'])
def glClientActiveTexture(texture):
	pass


@params(api='gles1', prms=['array'])
def glDisableClientState(array):
	pass


@params(api='gles1', prms=['plane', 'equation'])
def glGetClipPlanex(plane):
	pass


@params(api='gles1', prms=['depth'])
def glClearDepthx(depth):
	pass


@params(api='gles1', prms=['d'])
def glClearDepthf(d):
	pass


@params(api='gles1', prms=['texture', 's', 't', 'r', 'q'])
def glMultiTexCoord4x(texture, s, t, r, q):
	pass


@params(api='gles1', prms=['target', 's', 't', 'r', 'q'])
def glMultiTexCoord4f(target, s, t, r, q):
	pass


@params(api='gles1', prms=['red', 'green', 'blue', 'alpha'])
def glColorMask(red, green, blue, alpha):
	pass


@params(api='gles1', prms=['face', 'pname', 'param'])
def glMaterialxv(face, pname, param):
	pass


@params(api='gles1', prms=['factor', 'units'])
def glPolygonOffsetx(factor, units):
	pass


@params(api='gles1', prms=['m'])
def glLoadMatrixx(m):
	pass


@params(api='gles1', prms=['m'])
def glLoadMatrixf(m):
	pass


@params(api='gles1', prms=['target', 'pname', 'params'])
def glTexParameterfv(target, pname, params):
	pass


@params(api='gles1', prms=['target', 'pname', 'params'])
def glTexParameterxv(target, pname, params):
	pass


@params(api='gles1', prms=['target', 'pname', 'param'])
def glTexParameterx(target, pname, param):
	pass


@params(api='gles1', prms=['size'])
def glPointSizex(size):
	pass


@params(api='gles1', prms=['target', 'level', 'internalformat', 'width', 'height', 'border', 'imageSize', 'data'])
def glCompressedTexImage2D(target, level, internalformat, width, height, border, imageSize, data):
	pass


@params(api='gles1', prms=[])
def glLoadIdentity():
	pass


@params(api='gles1', prms=['face', 'pname', 'params'])
def glGetMaterialxv(face, pname):
	pass


@params(api='gles1', prms=['target', 'pname', 'params'])
def glTexEnvxv(target, pname, params):
	pass


@params(api='gles1', prms=['face', 'pname', 'params'])
def glGetMaterialfv(face, pname):
	pass


@params(api='gles1', prms=['l', 'r', 'b', 't', 'n', 'f'])
def glOrthox(l, r, b, t, n, f):
	pass


@params(api='gles1', prms=['l', 'r', 'b', 't', 'n', 'f'])
def glOrthof(l, r, b, t, n, f):
	pass


@params(api='gles1', prms=['cap'])
def glEnable(cap):
	pass


@params(api='gles1', prms=[])
def glPushMatrix():
	pass


@params(api='gles1', prms=['target', 'pname', 'params'])
def glGetTexParameterxv(target, pname):
	pass


@params(api='gles1', prms=['n', 'textures'])
def glGenTextures(n):
	pass


@params(api='gles1', prms=['target', 'mode'])
def glHint(target, mode):
	pass


@params(api='gles1', prms=['x', 'y', 'z'])
def glScalef(x, y, z):
	pass


@params(api='gles1', prms=['x', 'y', 'z'])
def glScalex(x, y, z):
	pass


@params(api='gles1', prms=['target', 'pname', 'params'])
def glGetTexParameteriv(target, pname):
	pass


@params(api='gles1', prms=['cap'])
def glDisable(cap):
	pass


@params(api='gles1', prms=['light', 'pname', 'params'])
def glGetLightfv(light, pname):
	pass


@params(api='gles1', prms=[])
def glPopMatrix():
	pass


@params(api='gles1', prms=['texture'])
def glActiveTexture(texture):
	pass


@params(api='gles1', prms=['target', 'pname', 'params'])
def glTexEnvfv(target, pname, params):
	pass


@params(api='gles1', prms=['target', 'offset', 'size', 'data'])
def glBufferSubData(target, offset, size, data):
	pass


@params(api='gles1', prms=['size', 'type', 'stride', 'pointer'])
def glTexCoordPointer(size, type, stride, pointer):
	pass


@params(api='gles1', prms=['target', 'pname', 'params'])
def glTexEnviv(target, pname, params):
	pass


@params(api='gles1', prms=['sfactor', 'dfactor'])
def glBlendFunc(sfactor, dfactor):
	pass


@params(api='gles1', prms=['red', 'green', 'blue', 'alpha'])
def glClearColor(red, green, blue, alpha):
	pass


@params(api='gles1', prms=['mask'])
def glStencilMask(mask):
	pass


@params(api='gles1', prms=['nx', 'ny', 'nz'])
def glNormal3f(nx, ny, nz):
	pass


@params(api='gles1', prms=['target', 'level', 'xoffset', 'yoffset', 'width', 'height', 'format', 'imageSize', 'data'])
def glCompressedTexSubImage2D(target, level, xoffset, yoffset, width, height, format, imageSize, data):
	pass


@params(api='gles1', prms=['target', 'pname', 'params'])
def glGetTexParameterfv(target, pname):
	pass


@params(api='gles1', prms=['target', 'size', 'data', 'usage'])
def glBufferData(target, size, data, usage):
	pass


@params(api='gles1', prms=['size', 'type', 'stride', 'pointer'])
def glColorPointer(size, type, stride, pointer):
	pass


@params(api='gles1', prms=['nx', 'ny', 'nz'])
def glNormal3x(nx, ny, nz):
	pass


@params(api='gles1', prms=['plane', 'equation'])
def glClipPlanex(plane, equation):
	pass


@params(api='gles1', prms=['p', 'eqn'])
def glClipPlanef(p, eqn):
	pass


@params(api='gles1', prms=['mode'])
def glFrontFace(mode):
	pass


