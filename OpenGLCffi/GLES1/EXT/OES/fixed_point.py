from OpenGLCffi.GLES1 import params
@params(api='gles1', prms=['func', 'ref'])
def glAlphaFuncxOES(func, ref):
	pass


@params(api='gles1', prms=['red', 'green', 'blue', 'alpha'])
def glClearColorxOES(red, green, blue, alpha):
	pass


@params(api='gles1', prms=['depth'])
def glClearDepthxOES(depth):
	pass


@params(api='gles1', prms=['plane', 'equation'])
def glClipPlanexOES(plane, equation):
	pass


@params(api='gles1', prms=['red', 'green', 'blue', 'alpha'])
def glColor4xOES(red, green, blue, alpha):
	pass


@params(api='gles1', prms=['n', 'f'])
def glDepthRangexOES(n, f):
	pass


@params(api='gles1', prms=['pname', 'param'])
def glFogxOES(pname, param):
	pass


@params(api='gles1', prms=['pname', 'param'])
def glFogxvOES(pname, param):
	pass


@params(api='gles1', prms=['l', 'r', 'b', 't', 'n', 'f'])
def glFrustumxOES(l, r, b, t, n, f):
	pass


@params(api='gles1', prms=['plane', 'equation'])
def glGetClipPlanexOES(plane):
	pass


@params(api='gles1', prms=['pname', 'params'])
def glGetFixedvOES(pname):
	pass


@params(api='gles1', prms=['target', 'pname', 'params'])
def glGetTexEnvxvOES(target, pname):
	pass


@params(api='gles1', prms=['target', 'pname', 'params'])
def glGetTexParameterxvOES(target, pname):
	pass


@params(api='gles1', prms=['pname', 'param'])
def glLightModelxOES(pname, param):
	pass


@params(api='gles1', prms=['pname', 'param'])
def glLightModelxvOES(pname, param):
	pass


@params(api='gles1', prms=['light', 'pname', 'param'])
def glLightxOES(light, pname, param):
	pass


@params(api='gles1', prms=['light', 'pname', 'params'])
def glLightxvOES(light, pname, params):
	pass


@params(api='gles1', prms=['width'])
def glLineWidthxOES(width):
	pass


@params(api='gles1', prms=['m'])
def glLoadMatrixxOES(m):
	pass


@params(api='gles1', prms=['face', 'pname', 'param'])
def glMaterialxOES(face, pname, param):
	pass


@params(api='gles1', prms=['face', 'pname', 'param'])
def glMaterialxvOES(face, pname, param):
	pass


@params(api='gles1', prms=['m'])
def glMultMatrixxOES(m):
	pass


@params(api='gles1', prms=['texture', 's', 't', 'r', 'q'])
def glMultiTexCoord4xOES(texture, s, t, r, q):
	pass


@params(api='gles1', prms=['nx', 'ny', 'nz'])
def glNormal3xOES(nx, ny, nz):
	pass


@params(api='gles1', prms=['l', 'r', 'b', 't', 'n', 'f'])
def glOrthoxOES(l, r, b, t, n, f):
	pass


@params(api='gles1', prms=['pname', 'params'])
def glPointParameterxvOES(pname, params):
	pass


@params(api='gles1', prms=['size'])
def glPointSizexOES(size):
	pass


@params(api='gles1', prms=['factor', 'units'])
def glPolygonOffsetxOES(factor, units):
	pass


@params(api='gles1', prms=['angle', 'x', 'y', 'z'])
def glRotatexOES(angle, x, y, z):
	pass


@params(api='gles1', prms=['x', 'y', 'z'])
def glScalexOES(x, y, z):
	pass


@params(api='gles1', prms=['target', 'pname', 'param'])
def glTexEnvxOES(target, pname, param):
	pass


@params(api='gles1', prms=['target', 'pname', 'params'])
def glTexEnvxvOES(target, pname, params):
	pass


@params(api='gles1', prms=['target', 'pname', 'param'])
def glTexParameterxOES(target, pname, param):
	pass


@params(api='gles1', prms=['target', 'pname', 'params'])
def glTexParameterxvOES(target, pname, params):
	pass


@params(api='gles1', prms=['x', 'y', 'z'])
def glTranslatexOES(x, y, z):
	pass


@params(api='gles1', prms=['light', 'pname', 'params'])
def glGetLightxvOES(light, pname):
	pass


@params(api='gles1', prms=['face', 'pname', 'params'])
def glGetMaterialxvOES(face, pname):
	pass


@params(api='gles1', prms=['pname', 'param'])
def glPointParameterxOES(pname, param):
	pass


@params(api='gles1', prms=['value', 'invert'])
def glSampleCoveragexOES(value, invert):
	pass


@params(api='gles1', prms=['op', 'value'])
def glAccumxOES(op, value):
	pass


@params(api='gles1', prms=['width', 'height', 'xorig', 'yorig', 'xmove', 'ymove', 'bitmap'])
def glBitmapxOES(width, height, xorig, yorig, xmove, ymove, bitmap):
	pass


@params(api='gles1', prms=['red', 'green', 'blue', 'alpha'])
def glBlendColorxOES(red, green, blue, alpha):
	pass


@params(api='gles1', prms=['red', 'green', 'blue', 'alpha'])
def glClearAccumxOES(red, green, blue, alpha):
	pass


@params(api='gles1', prms=['red', 'green', 'blue'])
def glColor3xOES(red, green, blue):
	pass


@params(api='gles1', prms=['components'])
def glColor3xvOES(components):
	pass


@params(api='gles1', prms=['components'])
def glColor4xvOES(components):
	pass


@params(api='gles1', prms=['target', 'pname', 'param'])
def glConvolutionParameterxOES(target, pname, param):
	pass


@params(api='gles1', prms=['target', 'pname', 'params'])
def glConvolutionParameterxvOES(target, pname, params):
	pass


@params(api='gles1', prms=['u'])
def glEvalCoord1xOES(u):
	pass


@params(api='gles1', prms=['coords'])
def glEvalCoord1xvOES(coords):
	pass


@params(api='gles1', prms=['u', 'v'])
def glEvalCoord2xOES(u, v):
	pass


@params(api='gles1', prms=['coords'])
def glEvalCoord2xvOES(coords):
	pass


@params(api='gles1', prms=['n', 'type', 'buffer'])
def glFeedbackBufferxOES(n, type, buffer):
	pass


@params(api='gles1', prms=['target', 'pname', 'params'])
def glGetConvolutionParameterxvOES(target, pname):
	pass


@params(api='gles1', prms=['target', 'pname', 'params'])
def glGetHistogramParameterxvOES(target, pname):
	pass


@params(api='gles1', prms=['light', 'pname', 'params'])
def glGetLightxOES(light, pname):
	pass


@params(api='gles1', prms=['target', 'query', 'v'])
def glGetMapxvOES(target, query, v):
	pass


@params(api='gles1', prms=['face', 'pname', 'param'])
def glGetMaterialxOES(face, pname, param):
	pass


@params(api='gles1', prms=['map', 'size', 'values'])
def glGetPixelMapxv(map, size, values):
	pass


@params(api='gles1', prms=['coord', 'pname', 'params'])
def glGetTexGenxvOES(coord, pname):
	pass


@params(api='gles1', prms=['target', 'level', 'pname', 'params'])
def glGetTexLevelParameterxvOES(target, level, pname):
	pass


@params(api='gles1', prms=['component'])
def glIndexxOES(component):
	pass


@params(api='gles1', prms=['component'])
def glIndexxvOES(component):
	pass


@params(api='gles1', prms=['m'])
def glLoadTransposeMatrixxOES(m):
	pass


@params(api='gles1', prms=['target', 'u1', 'u2', 'stride', 'order', 'points'])
def glMap1xOES(target, u1, u2, stride, order, points):
	pass


@params(api='gles1', prms=['target', 'u1', 'u2', 'ustride', 'uorder', 'v1', 'v2', 'vstride', 'vorder', 'points'])
def glMap2xOES(target, u1, u2, ustride, uorder, v1, v2, vstride, vorder, points):
	pass


@params(api='gles1', prms=['n', 'u1', 'u2'])
def glMapGrid1xOES(n, u1, u2):
	pass


@params(api='gles1', prms=['n', 'u1', 'u2', 'v1', 'v2'])
def glMapGrid2xOES(n, u1, u2, v1, v2):
	pass


@params(api='gles1', prms=['m'])
def glMultTransposeMatrixxOES(m):
	pass


@params(api='gles1', prms=['texture', 's'])
def glMultiTexCoord1xOES(texture, s):
	pass


@params(api='gles1', prms=['texture', 'coords'])
def glMultiTexCoord1xvOES(texture, coords):
	pass


@params(api='gles1', prms=['texture', 's', 't'])
def glMultiTexCoord2xOES(texture, s, t):
	pass


@params(api='gles1', prms=['texture', 'coords'])
def glMultiTexCoord2xvOES(texture, coords):
	pass


@params(api='gles1', prms=['texture', 's', 't', 'r'])
def glMultiTexCoord3xOES(texture, s, t, r):
	pass


@params(api='gles1', prms=['texture', 'coords'])
def glMultiTexCoord3xvOES(texture, coords):
	pass


@params(api='gles1', prms=['texture', 'coords'])
def glMultiTexCoord4xvOES(texture, coords):
	pass


@params(api='gles1', prms=['coords'])
def glNormal3xvOES(coords):
	pass


@params(api='gles1', prms=['token'])
def glPassThroughxOES(token):
	pass


@params(api='gles1', prms=['map', 'size', 'values'])
def glPixelMapx(map, size, values):
	pass


@params(api='gles1', prms=['pname', 'param'])
def glPixelStorex(pname, param):
	pass


@params(api='gles1', prms=['pname', 'param'])
def glPixelTransferxOES(pname, param):
	pass


@params(api='gles1', prms=['xfactor', 'yfactor'])
def glPixelZoomxOES(xfactor, yfactor):
	pass


@params(api='gles1', prms=['n', 'textures', 'priorities'])
def glPrioritizeTexturesxOES(n, textures, priorities):
	pass


@params(api='gles1', prms=['x', 'y'])
def glRasterPos2xOES(x, y):
	pass


@params(api='gles1', prms=['coords'])
def glRasterPos2xvOES(coords):
	pass


@params(api='gles1', prms=['x', 'y', 'z'])
def glRasterPos3xOES(x, y, z):
	pass


@params(api='gles1', prms=['coords'])
def glRasterPos3xvOES(coords):
	pass


@params(api='gles1', prms=['x', 'y', 'z', 'w'])
def glRasterPos4xOES(x, y, z, w):
	pass


@params(api='gles1', prms=['coords'])
def glRasterPos4xvOES(coords):
	pass


@params(api='gles1', prms=['x1', 'y1', 'x2', 'y2'])
def glRectxOES(x1, y1, x2, y2):
	pass


@params(api='gles1', prms=['v1', 'v2'])
def glRectxvOES(v1, v2):
	pass


@params(api='gles1', prms=['s'])
def glTexCoord1xOES(s):
	pass


@params(api='gles1', prms=['coords'])
def glTexCoord1xvOES(coords):
	pass


@params(api='gles1', prms=['s', 't'])
def glTexCoord2xOES(s, t):
	pass


@params(api='gles1', prms=['coords'])
def glTexCoord2xvOES(coords):
	pass


@params(api='gles1', prms=['s', 't', 'r'])
def glTexCoord3xOES(s, t, r):
	pass


@params(api='gles1', prms=['coords'])
def glTexCoord3xvOES(coords):
	pass


@params(api='gles1', prms=['s', 't', 'r', 'q'])
def glTexCoord4xOES(s, t, r, q):
	pass


@params(api='gles1', prms=['coords'])
def glTexCoord4xvOES(coords):
	pass


@params(api='gles1', prms=['coord', 'pname', 'param'])
def glTexGenxOES(coord, pname, param):
	pass


@params(api='gles1', prms=['coord', 'pname', 'params'])
def glTexGenxvOES(coord, pname, params):
	pass


@params(api='gles1', prms=['x'])
def glVertex2xOES(x):
	pass


@params(api='gles1', prms=['coords'])
def glVertex2xvOES(coords):
	pass


@params(api='gles1', prms=['x', 'y'])
def glVertex3xOES(x, y):
	pass


@params(api='gles1', prms=['coords'])
def glVertex3xvOES(coords):
	pass


@params(api='gles1', prms=['x', 'y', 'z'])
def glVertex4xOES(x, y, z):
	pass


@params(api='gles1', prms=['coords'])
def glVertex4xvOES(coords):
	pass


