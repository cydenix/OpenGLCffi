@params('func', 'ref', api='gles1')
def glAlphaFuncxOES(func, ref):
	pass


@params('red', 'green', 'blue', 'alpha', api='gles1')
def glClearColorxOES(red, green, blue, alpha):
	pass


@params('depth', api='gles1')
def glClearDepthxOES(depth):
	pass


@params('plane', 'equation', api='gles1')
def glClipPlanexOES(plane, equation):
	pass


@params('red', 'green', 'blue', 'alpha', api='gles1')
def glColor4xOES(red, green, blue, alpha):
	pass


@params('n', 'f', api='gles1')
def glDepthRangexOES(n, f):
	pass


@params('pname', 'param', api='gles1')
def glFogxOES(pname, param):
	pass


@params('pname', 'param', api='gles1')
def glFogxvOES(pname, param):
	pass


@params('l', 'r', 'b', 't', 'n', 'f', api='gles1')
def glFrustumxOES(l, r, b, t, n, f):
	pass


@params('plane', 'equation', api='gles1')
def glGetClipPlanexOES(plane):
	pass


@params('pname', 'params', api='gles1')
def glGetFixedvOES(pname):
	pass


@params('target', 'pname', 'params', api='gles1')
def glGetTexEnvxvOES(target, pname):
	pass


@params('target', 'pname', 'params', api='gles1')
def glGetTexParameterxvOES(target, pname):
	pass


@params('pname', 'param', api='gles1')
def glLightModelxOES(pname, param):
	pass


@params('pname', 'param', api='gles1')
def glLightModelxvOES(pname, param):
	pass


@params('light', 'pname', 'param', api='gles1')
def glLightxOES(light, pname, param):
	pass


@params('light', 'pname', 'params', api='gles1')
def glLightxvOES(light, pname, params):
	pass


@params('width', api='gles1')
def glLineWidthxOES(width):
	pass


@params('m', api='gles1')
def glLoadMatrixxOES(m):
	pass


@params('face', 'pname', 'param', api='gles1')
def glMaterialxOES(face, pname, param):
	pass


@params('face', 'pname', 'param', api='gles1')
def glMaterialxvOES(face, pname, param):
	pass


@params('m', api='gles1')
def glMultMatrixxOES(m):
	pass


@params('texture', 's', 't', 'r', 'q', api='gles1')
def glMultiTexCoord4xOES(texture, s, t, r, q):
	pass


@params('nx', 'ny', 'nz', api='gles1')
def glNormal3xOES(nx, ny, nz):
	pass


@params('l', 'r', 'b', 't', 'n', 'f', api='gles1')
def glOrthoxOES(l, r, b, t, n, f):
	pass


@params('pname', 'params', api='gles1')
def glPointParameterxvOES(pname, params):
	pass


@params('size', api='gles1')
def glPointSizexOES(size):
	pass


@params('factor', 'units', api='gles1')
def glPolygonOffsetxOES(factor, units):
	pass


@params('angle', 'x', 'y', 'z', api='gles1')
def glRotatexOES(angle, x, y, z):
	pass


@params('x', 'y', 'z', api='gles1')
def glScalexOES(x, y, z):
	pass


@params('target', 'pname', 'param', api='gles1')
def glTexEnvxOES(target, pname, param):
	pass


@params('target', 'pname', 'params', api='gles1')
def glTexEnvxvOES(target, pname, params):
	pass


@params('target', 'pname', 'param', api='gles1')
def glTexParameterxOES(target, pname, param):
	pass


@params('target', 'pname', 'params', api='gles1')
def glTexParameterxvOES(target, pname, params):
	pass


@params('x', 'y', 'z', api='gles1')
def glTranslatexOES(x, y, z):
	pass


@params('light', 'pname', 'params', api='gles1')
def glGetLightxvOES(light, pname):
	pass


@params('face', 'pname', 'params', api='gles1')
def glGetMaterialxvOES(face, pname):
	pass


@params('pname', 'param', api='gles1')
def glPointParameterxOES(pname, param):
	pass


@params('value', 'invert', api='gles1')
def glSampleCoveragexOES(value, invert):
	pass


@params('op', 'value', api='gles1')
def glAccumxOES(op, value):
	pass


@params('width', 'height', 'xorig', 'yorig', 'xmove', 'ymove', 'bitmap', api='gles1')
def glBitmapxOES(width, height, xorig, yorig, xmove, ymove, bitmap):
	pass


@params('red', 'green', 'blue', 'alpha', api='gles1')
def glBlendColorxOES(red, green, blue, alpha):
	pass


@params('red', 'green', 'blue', 'alpha', api='gles1')
def glClearAccumxOES(red, green, blue, alpha):
	pass


@params('red', 'green', 'blue', api='gles1')
def glColor3xOES(red, green, blue):
	pass


@params('components', api='gles1')
def glColor3xvOES(components):
	pass


@params('components', api='gles1')
def glColor4xvOES(components):
	pass


@params('target', 'pname', 'param', api='gles1')
def glConvolutionParameterxOES(target, pname, param):
	pass


@params('target', 'pname', 'params', api='gles1')
def glConvolutionParameterxvOES(target, pname, params):
	pass


@params('u', api='gles1')
def glEvalCoord1xOES(u):
	pass


@params('coords', api='gles1')
def glEvalCoord1xvOES(coords):
	pass


@params('u', 'v', api='gles1')
def glEvalCoord2xOES(u, v):
	pass


@params('coords', api='gles1')
def glEvalCoord2xvOES(coords):
	pass


@params('n', 'type', 'buffer', api='gles1')
def glFeedbackBufferxOES(n, type, buffer):
	pass


@params('target', 'pname', 'params', api='gles1')
def glGetConvolutionParameterxvOES(target, pname):
	pass


@params('target', 'pname', 'params', api='gles1')
def glGetHistogramParameterxvOES(target, pname):
	pass


@params('light', 'pname', 'params', api='gles1')
def glGetLightxOES(light, pname):
	pass


@params('target', 'query', 'v', api='gles1')
def glGetMapxvOES(target, query, v):
	pass


@params('face', 'pname', 'param', api='gles1')
def glGetMaterialxOES(face, pname, param):
	pass


@params('map', 'size', 'values', api='gles1')
def glGetPixelMapxv(map, size, values):
	pass


@params('coord', 'pname', 'params', api='gles1')
def glGetTexGenxvOES(coord, pname):
	pass


@params('target', 'level', 'pname', 'params', api='gles1')
def glGetTexLevelParameterxvOES(target, level, pname):
	pass


@params('component', api='gles1')
def glIndexxOES(component):
	pass


@params('component', api='gles1')
def glIndexxvOES(component):
	pass


@params('m', api='gles1')
def glLoadTransposeMatrixxOES(m):
	pass


@params('target', 'u1', 'u2', 'stride', 'order', 'points', api='gles1')
def glMap1xOES(target, u1, u2, stride, order, points):
	pass


@params('target', 'u1', 'u2', 'ustride', 'uorder', 'v1', 'v2', 'vstride', 'vorder', 'points', api='gles1')
def glMap2xOES(target, u1, u2, ustride, uorder, v1, v2, vstride, vorder, points):
	pass


@params('n', 'u1', 'u2', api='gles1')
def glMapGrid1xOES(n, u1, u2):
	pass


@params('n', 'u1', 'u2', 'v1', 'v2', api='gles1')
def glMapGrid2xOES(n, u1, u2, v1, v2):
	pass


@params('m', api='gles1')
def glMultTransposeMatrixxOES(m):
	pass


@params('texture', 's', api='gles1')
def glMultiTexCoord1xOES(texture, s):
	pass


@params('texture', 'coords', api='gles1')
def glMultiTexCoord1xvOES(texture, coords):
	pass


@params('texture', 's', 't', api='gles1')
def glMultiTexCoord2xOES(texture, s, t):
	pass


@params('texture', 'coords', api='gles1')
def glMultiTexCoord2xvOES(texture, coords):
	pass


@params('texture', 's', 't', 'r', api='gles1')
def glMultiTexCoord3xOES(texture, s, t, r):
	pass


@params('texture', 'coords', api='gles1')
def glMultiTexCoord3xvOES(texture, coords):
	pass


@params('texture', 'coords', api='gles1')
def glMultiTexCoord4xvOES(texture, coords):
	pass


@params('coords', api='gles1')
def glNormal3xvOES(coords):
	pass


@params('token', api='gles1')
def glPassThroughxOES(token):
	pass


@params('map', 'size', 'values', api='gles1')
def glPixelMapx(map, size, values):
	pass


@params('pname', 'param', api='gles1')
def glPixelStorex(pname, param):
	pass


@params('pname', 'param', api='gles1')
def glPixelTransferxOES(pname, param):
	pass


@params('xfactor', 'yfactor', api='gles1')
def glPixelZoomxOES(xfactor, yfactor):
	pass


@params('n', 'textures', 'priorities', api='gles1')
def glPrioritizeTexturesxOES(n, textures, priorities):
	pass


@params('x', 'y', api='gles1')
def glRasterPos2xOES(x, y):
	pass


@params('coords', api='gles1')
def glRasterPos2xvOES(coords):
	pass


@params('x', 'y', 'z', api='gles1')
def glRasterPos3xOES(x, y, z):
	pass


@params('coords', api='gles1')
def glRasterPos3xvOES(coords):
	pass


@params('x', 'y', 'z', 'w', api='gles1')
def glRasterPos4xOES(x, y, z, w):
	pass


@params('coords', api='gles1')
def glRasterPos4xvOES(coords):
	pass


@params('x1', 'y1', 'x2', 'y2', api='gles1')
def glRectxOES(x1, y1, x2, y2):
	pass


@params('v1', 'v2', api='gles1')
def glRectxvOES(v1, v2):
	pass


@params('s', api='gles1')
def glTexCoord1xOES(s):
	pass


@params('coords', api='gles1')
def glTexCoord1xvOES(coords):
	pass


@params('s', 't', api='gles1')
def glTexCoord2xOES(s, t):
	pass


@params('coords', api='gles1')
def glTexCoord2xvOES(coords):
	pass


@params('s', 't', 'r', api='gles1')
def glTexCoord3xOES(s, t, r):
	pass


@params('coords', api='gles1')
def glTexCoord3xvOES(coords):
	pass


@params('s', 't', 'r', 'q', api='gles1')
def glTexCoord4xOES(s, t, r, q):
	pass


@params('coords', api='gles1')
def glTexCoord4xvOES(coords):
	pass


@params('coord', 'pname', 'param', api='gles1')
def glTexGenxOES(coord, pname, param):
	pass


@params('coord', 'pname', 'params', api='gles1')
def glTexGenxvOES(coord, pname, params):
	pass


@params('x', api='gles1')
def glVertex2xOES(x):
	pass


@params('coords', api='gles1')
def glVertex2xvOES(coords):
	pass


@params('x', 'y', api='gles1')
def glVertex3xOES(x, y):
	pass


@params('coords', api='gles1')
def glVertex3xvOES(coords):
	pass


@params('x', 'y', 'z', api='gles1')
def glVertex4xOES(x, y, z):
	pass


@params('coords', api='gles1')
def glVertex4xvOES(coords):
	pass


