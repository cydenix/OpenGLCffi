from OpenGLCffi.GL import params
@params('func', 'ref', api='gl')
def glAlphaFuncxOES(func, ref):
	pass


@params('red', 'green', 'blue', 'alpha', api='gl')
def glClearColorxOES(red, green, blue, alpha):
	pass


@params('depth', api='gl')
def glClearDepthxOES(depth):
	pass


@params('plane', 'equation', api='gl')
def glClipPlanexOES(plane, equation):
	pass


@params('red', 'green', 'blue', 'alpha', api='gl')
def glColor4xOES(red, green, blue, alpha):
	pass


@params('n', 'f', api='gl')
def glDepthRangexOES(n, f):
	pass


@params('pname', 'param', api='gl')
def glFogxOES(pname, param):
	pass


@params('pname', 'param', api='gl')
def glFogxvOES(pname, param):
	pass


@params('l', 'r', 'b', 't', 'n', 'f', api='gl')
def glFrustumxOES(l, r, b, t, n, f):
	pass


@params('plane', 'equation', api='gl')
def glGetClipPlanexOES(plane, equation):
	pass


@params('pname', 'params', api='gl')
def glGetFixedvOES(pname, params):
	pass


@params('target', 'pname', 'params', api='gl')
def glGetTexEnvxvOES(target, pname, params):
	pass


@params('target', 'pname', 'params', api='gl')
def glGetTexParameterxvOES(target, pname, params):
	pass


@params('pname', 'param', api='gl')
def glLightModelxOES(pname, param):
	pass


@params('pname', 'param', api='gl')
def glLightModelxvOES(pname, param):
	pass


@params('light', 'pname', 'param', api='gl')
def glLightxOES(light, pname, param):
	pass


@params('light', 'pname', 'params', api='gl')
def glLightxvOES(light, pname, params):
	pass


@params('width', api='gl')
def glLineWidthxOES(width):
	pass


@params('m', api='gl')
def glLoadMatrixxOES(m):
	pass


@params('face', 'pname', 'param', api='gl')
def glMaterialxOES(face, pname, param):
	pass


@params('face', 'pname', 'param', api='gl')
def glMaterialxvOES(face, pname, param):
	pass


@params('m', api='gl')
def glMultMatrixxOES(m):
	pass


@params('texture', 's', 't', 'r', 'q', api='gl')
def glMultiTexCoord4xOES(texture, s, t, r, q):
	pass


@params('nx', 'ny', 'nz', api='gl')
def glNormal3xOES(nx, ny, nz):
	pass


@params('l', 'r', 'b', 't', 'n', 'f', api='gl')
def glOrthoxOES(l, r, b, t, n, f):
	pass


@params('pname', 'params', api='gl')
def glPointParameterxvOES(pname, params):
	pass


@params('size', api='gl')
def glPointSizexOES(size):
	pass


@params('factor', 'units', api='gl')
def glPolygonOffsetxOES(factor, units):
	pass


@params('angle', 'x', 'y', 'z', api='gl')
def glRotatexOES(angle, x, y, z):
	pass


@params('x', 'y', 'z', api='gl')
def glScalexOES(x, y, z):
	pass


@params('target', 'pname', 'param', api='gl')
def glTexEnvxOES(target, pname, param):
	pass


@params('target', 'pname', 'params', api='gl')
def glTexEnvxvOES(target, pname, params):
	pass


@params('target', 'pname', 'param', api='gl')
def glTexParameterxOES(target, pname, param):
	pass


@params('target', 'pname', 'params', api='gl')
def glTexParameterxvOES(target, pname, params):
	pass


@params('x', 'y', 'z', api='gl')
def glTranslatexOES(x, y, z):
	pass


@params('light', 'pname', 'params', api='gl')
def glGetLightxvOES(light, pname, params):
	pass


@params('face', 'pname', 'params', api='gl')
def glGetMaterialxvOES(face, pname, params):
	pass


@params('pname', 'param', api='gl')
def glPointParameterxOES(pname, param):
	pass


@params('value', 'invert', api='gl')
def glSampleCoveragexOES(value, invert):
	pass


@params('op', 'value', api='gl')
def glAccumxOES(op, value):
	pass


@params('width', 'height', 'xorig', 'yorig', 'xmove', 'ymove', 'bitmap', api='gl')
def glBitmapxOES(width, height, xorig, yorig, xmove, ymove, bitmap):
	pass


@params('red', 'green', 'blue', 'alpha', api='gl')
def glBlendColorxOES(red, green, blue, alpha):
	pass


@params('red', 'green', 'blue', 'alpha', api='gl')
def glClearAccumxOES(red, green, blue, alpha):
	pass


@params('red', 'green', 'blue', api='gl')
def glColor3xOES(red, green, blue):
	pass


@params('components', api='gl')
def glColor3xvOES(components):
	pass


@params('components', api='gl')
def glColor4xvOES(components):
	pass


@params('target', 'pname', 'param', api='gl')
def glConvolutionParameterxOES(target, pname, param):
	pass


@params('target', 'pname', 'params', api='gl')
def glConvolutionParameterxvOES(target, pname, params):
	pass


@params('u', api='gl')
def glEvalCoord1xOES(u):
	pass


@params('coords', api='gl')
def glEvalCoord1xvOES(coords):
	pass


@params('u', 'v', api='gl')
def glEvalCoord2xOES(u, v):
	pass


@params('coords', api='gl')
def glEvalCoord2xvOES(coords):
	pass


@params('n', 'type', 'buffer', api='gl')
def glFeedbackBufferxOES(n, type, buffer):
	pass


@params('target', 'pname', 'params', api='gl')
def glGetConvolutionParameterxvOES(target, pname, params):
	pass


@params('target', 'pname', 'params', api='gl')
def glGetHistogramParameterxvOES(target, pname, params):
	pass


@params('light', 'pname', 'params', api='gl')
def glGetLightxOES(light, pname, params):
	pass


@params('target', 'query', 'v', api='gl')
def glGetMapxvOES(target, query, v):
	pass


@params('face', 'pname', 'param', api='gl')
def glGetMaterialxOES(face, pname, param):
	pass


@params('map', 'size', 'values', api='gl')
def glGetPixelMapxv(map, size, values):
	pass


@params('coord', 'pname', 'params', api='gl')
def glGetTexGenxvOES(coord, pname, params):
	pass


@params('target', 'level', 'pname', 'params', api='gl')
def glGetTexLevelParameterxvOES(target, level, pname, params):
	pass


@params('component', api='gl')
def glIndexxOES(component):
	pass


@params('component', api='gl')
def glIndexxvOES(component):
	pass


@params('m', api='gl')
def glLoadTransposeMatrixxOES(m):
	pass


@params('target', 'u1', 'u2', 'stride', 'order', 'points', api='gl')
def glMap1xOES(target, u1, u2, stride, order, points):
	pass


@params('target', 'u1', 'u2', 'ustride', 'uorder', 'v1', 'v2', 'vstride', 'vorder', 'points', api='gl')
def glMap2xOES(target, u1, u2, ustride, uorder, v1, v2, vstride, vorder, points):
	pass


@params('n', 'u1', 'u2', api='gl')
def glMapGrid1xOES(n, u1, u2):
	pass


@params('n', 'u1', 'u2', 'v1', 'v2', api='gl')
def glMapGrid2xOES(n, u1, u2, v1, v2):
	pass


@params('m', api='gl')
def glMultTransposeMatrixxOES(m):
	pass


@params('texture', 's', api='gl')
def glMultiTexCoord1xOES(texture, s):
	pass


@params('texture', 'coords', api='gl')
def glMultiTexCoord1xvOES(texture, coords):
	pass


@params('texture', 's', 't', api='gl')
def glMultiTexCoord2xOES(texture, s, t):
	pass


@params('texture', 'coords', api='gl')
def glMultiTexCoord2xvOES(texture, coords):
	pass


@params('texture', 's', 't', 'r', api='gl')
def glMultiTexCoord3xOES(texture, s, t, r):
	pass


@params('texture', 'coords', api='gl')
def glMultiTexCoord3xvOES(texture, coords):
	pass


@params('texture', 'coords', api='gl')
def glMultiTexCoord4xvOES(texture, coords):
	pass


@params('coords', api='gl')
def glNormal3xvOES(coords):
	pass


@params('token', api='gl')
def glPassThroughxOES(token):
	pass


@params('map', 'size', 'values', api='gl')
def glPixelMapx(map, size, values):
	pass


@params('pname', 'param', api='gl')
def glPixelStorex(pname, param):
	pass


@params('pname', 'param', api='gl')
def glPixelTransferxOES(pname, param):
	pass


@params('xfactor', 'yfactor', api='gl')
def glPixelZoomxOES(xfactor, yfactor):
	pass


@params('n', 'textures', 'priorities', api='gl')
def glPrioritizeTexturesxOES(n, textures, priorities):
	pass


@params('x', 'y', api='gl')
def glRasterPos2xOES(x, y):
	pass


@params('coords', api='gl')
def glRasterPos2xvOES(coords):
	pass


@params('x', 'y', 'z', api='gl')
def glRasterPos3xOES(x, y, z):
	pass


@params('coords', api='gl')
def glRasterPos3xvOES(coords):
	pass


@params('x', 'y', 'z', 'w', api='gl')
def glRasterPos4xOES(x, y, z, w):
	pass


@params('coords', api='gl')
def glRasterPos4xvOES(coords):
	pass


@params('x1', 'y1', 'x2', 'y2', api='gl')
def glRectxOES(x1, y1, x2, y2):
	pass


@params('v1', 'v2', api='gl')
def glRectxvOES(v1, v2):
	pass


@params('s', api='gl')
def glTexCoord1xOES(s):
	pass


@params('coords', api='gl')
def glTexCoord1xvOES(coords):
	pass


@params('s', 't', api='gl')
def glTexCoord2xOES(s, t):
	pass


@params('coords', api='gl')
def glTexCoord2xvOES(coords):
	pass


@params('s', 't', 'r', api='gl')
def glTexCoord3xOES(s, t, r):
	pass


@params('coords', api='gl')
def glTexCoord3xvOES(coords):
	pass


@params('s', 't', 'r', 'q', api='gl')
def glTexCoord4xOES(s, t, r, q):
	pass


@params('coords', api='gl')
def glTexCoord4xvOES(coords):
	pass


@params('coord', 'pname', 'param', api='gl')
def glTexGenxOES(coord, pname, param):
	pass


@params('coord', 'pname', 'params', api='gl')
def glTexGenxvOES(coord, pname, params):
	pass


@params('x', api='gl')
def glVertex2xOES(x):
	pass


@params('coords', api='gl')
def glVertex2xvOES(coords):
	pass


@params('x', 'y', api='gl')
def glVertex3xOES(x, y):
	pass


@params('coords', api='gl')
def glVertex3xvOES(coords):
	pass


@params('x', 'y', 'z', api='gl')
def glVertex4xOES(x, y, z):
	pass


@params('coords', api='gl')
def glVertex4xvOES(coords):
	pass


