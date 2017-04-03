from OpenGLCffi.GLES1 import params
@params('texture', 's', api='gles1')
def glMultiTexCoord1bOES(texture, s):
	pass


@params('texture', 'coords', api='gles1')
def glMultiTexCoord1bvOES(texture, coords):
	pass


@params('texture', 's', 't', api='gles1')
def glMultiTexCoord2bOES(texture, s, t):
	pass


@params('texture', 'coords', api='gles1')
def glMultiTexCoord2bvOES(texture, coords):
	pass


@params('texture', 's', 't', 'r', api='gles1')
def glMultiTexCoord3bOES(texture, s, t, r):
	pass


@params('texture', 'coords', api='gles1')
def glMultiTexCoord3bvOES(texture, coords):
	pass


@params('texture', 's', 't', 'r', 'q', api='gles1')
def glMultiTexCoord4bOES(texture, s, t, r, q):
	pass


@params('texture', 'coords', api='gles1')
def glMultiTexCoord4bvOES(texture, coords):
	pass


@params('s', api='gles1')
def glTexCoord1bOES(s):
	pass


@params('coords', api='gles1')
def glTexCoord1bvOES(coords):
	pass


@params('s', 't', api='gles1')
def glTexCoord2bOES(s, t):
	pass


@params('coords', api='gles1')
def glTexCoord2bvOES(coords):
	pass


@params('s', 't', 'r', api='gles1')
def glTexCoord3bOES(s, t, r):
	pass


@params('coords', api='gles1')
def glTexCoord3bvOES(coords):
	pass


@params('s', 't', 'r', 'q', api='gles1')
def glTexCoord4bOES(s, t, r, q):
	pass


@params('coords', api='gles1')
def glTexCoord4bvOES(coords):
	pass


@params('x', 'y', api='gles1')
def glVertex2bOES(x, y):
	pass


@params('coords', api='gles1')
def glVertex2bvOES(coords):
	pass


@params('x', 'y', 'z', api='gles1')
def glVertex3bOES(x, y, z):
	pass


@params('coords', api='gles1')
def glVertex3bvOES(coords):
	pass


@params('x', 'y', 'z', 'w', api='gles1')
def glVertex4bOES(x, y, z, w):
	pass


@params('coords', api='gles1')
def glVertex4bvOES(coords):
	pass


