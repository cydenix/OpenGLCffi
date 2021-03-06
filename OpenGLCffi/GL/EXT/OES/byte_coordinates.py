from OpenGLCffi.GL import params
@params(api='gl', prms=['texture', 's'])
def glMultiTexCoord1bOES(texture, s):
	pass


@params(api='gl', prms=['texture', 'coords'])
def glMultiTexCoord1bvOES(texture, coords):
	pass


@params(api='gl', prms=['texture', 's', 't'])
def glMultiTexCoord2bOES(texture, s, t):
	pass


@params(api='gl', prms=['texture', 'coords'])
def glMultiTexCoord2bvOES(texture, coords):
	pass


@params(api='gl', prms=['texture', 's', 't', 'r'])
def glMultiTexCoord3bOES(texture, s, t, r):
	pass


@params(api='gl', prms=['texture', 'coords'])
def glMultiTexCoord3bvOES(texture, coords):
	pass


@params(api='gl', prms=['texture', 's', 't', 'r', 'q'])
def glMultiTexCoord4bOES(texture, s, t, r, q):
	pass


@params(api='gl', prms=['texture', 'coords'])
def glMultiTexCoord4bvOES(texture, coords):
	pass


@params(api='gl', prms=['s'])
def glTexCoord1bOES(s):
	pass


@params(api='gl', prms=['coords'])
def glTexCoord1bvOES(coords):
	pass


@params(api='gl', prms=['s', 't'])
def glTexCoord2bOES(s, t):
	pass


@params(api='gl', prms=['coords'])
def glTexCoord2bvOES(coords):
	pass


@params(api='gl', prms=['s', 't', 'r'])
def glTexCoord3bOES(s, t, r):
	pass


@params(api='gl', prms=['coords'])
def glTexCoord3bvOES(coords):
	pass


@params(api='gl', prms=['s', 't', 'r', 'q'])
def glTexCoord4bOES(s, t, r, q):
	pass


@params(api='gl', prms=['coords'])
def glTexCoord4bvOES(coords):
	pass


@params(api='gl', prms=['x', 'y'])
def glVertex2bOES(x, y):
	pass


@params(api='gl', prms=['coords'])
def glVertex2bvOES(coords):
	pass


@params(api='gl', prms=['x', 'y', 'z'])
def glVertex3bOES(x, y, z):
	pass


@params(api='gl', prms=['coords'])
def glVertex3bvOES(coords):
	pass


@params(api='gl', prms=['x', 'y', 'z', 'w'])
def glVertex4bOES(x, y, z, w):
	pass


@params(api='gl', prms=['coords'])
def glVertex4bvOES(coords):
	pass


