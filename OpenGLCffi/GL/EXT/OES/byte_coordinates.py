from OpenGLCffi.GL import params
@params('texture', 's', api='gl')
def glMultiTexCoord1bOES(texture, s):
	pass


@params('texture', 'coords', api='gl')
def glMultiTexCoord1bvOES(texture, coords):
	pass


@params('texture', 's', 't', api='gl')
def glMultiTexCoord2bOES(texture, s, t):
	pass


@params('texture', 'coords', api='gl')
def glMultiTexCoord2bvOES(texture, coords):
	pass


@params('texture', 's', 't', 'r', api='gl')
def glMultiTexCoord3bOES(texture, s, t, r):
	pass


@params('texture', 'coords', api='gl')
def glMultiTexCoord3bvOES(texture, coords):
	pass


@params('texture', 's', 't', 'r', 'q', api='gl')
def glMultiTexCoord4bOES(texture, s, t, r, q):
	pass


@params('texture', 'coords', api='gl')
def glMultiTexCoord4bvOES(texture, coords):
	pass


@params('s', api='gl')
def glTexCoord1bOES(s):
	pass


@params('coords', api='gl')
def glTexCoord1bvOES(coords):
	pass


@params('s', 't', api='gl')
def glTexCoord2bOES(s, t):
	pass


@params('coords', api='gl')
def glTexCoord2bvOES(coords):
	pass


@params('s', 't', 'r', api='gl')
def glTexCoord3bOES(s, t, r):
	pass


@params('coords', api='gl')
def glTexCoord3bvOES(coords):
	pass


@params('s', 't', 'r', 'q', api='gl')
def glTexCoord4bOES(s, t, r, q):
	pass


@params('coords', api='gl')
def glTexCoord4bvOES(coords):
	pass


@params('x', 'y', api='gl')
def glVertex2bOES(x, y):
	pass


@params('coords', api='gl')
def glVertex2bvOES(coords):
	pass


@params('x', 'y', 'z', api='gl')
def glVertex3bOES(x, y, z):
	pass


@params('coords', api='gl')
def glVertex3bvOES(coords):
	pass


@params('x', 'y', 'z', 'w', api='gl')
def glVertex4bOES(x, y, z, w):
	pass


@params('coords', api='gl')
def glVertex4bvOES(coords):
	pass


