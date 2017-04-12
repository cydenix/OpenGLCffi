from OpenGLCffi.GL import params
@params(api='gl', prms=['r', 'g', 'b', 'a', 'x', 'y'])
def glColor4ubVertex2fSUN(r, g, b, a, x, y):
	pass


@params(api='gl', prms=['c', 'v'])
def glColor4ubVertex2fvSUN(c, v):
	pass


@params(api='gl', prms=['r', 'g', 'b', 'a', 'x', 'y', 'z'])
def glColor4ubVertex3fSUN(r, g, b, a, x, y, z):
	pass


@params(api='gl', prms=['c', 'v'])
def glColor4ubVertex3fvSUN(c, v):
	pass


@params(api='gl', prms=['r', 'g', 'b', 'x', 'y', 'z'])
def glColor3fVertex3fSUN(r, g, b, x, y, z):
	pass


@params(api='gl', prms=['c', 'v'])
def glColor3fVertex3fvSUN(c, v):
	pass


@params(api='gl', prms=['nx', 'ny', 'nz', 'x', 'y', 'z'])
def glNormal3fVertex3fSUN(nx, ny, nz, x, y, z):
	pass


@params(api='gl', prms=['n', 'v'])
def glNormal3fVertex3fvSUN(n, v):
	pass


@params(api='gl', prms=['r', 'g', 'b', 'a', 'nx', 'ny', 'nz', 'x', 'y', 'z'])
def glColor4fNormal3fVertex3fSUN(r, g, b, a, nx, ny, nz, x, y, z):
	pass


@params(api='gl', prms=['c', 'n', 'v'])
def glColor4fNormal3fVertex3fvSUN(c, n, v):
	pass


@params(api='gl', prms=['s', 't', 'x', 'y', 'z'])
def glTexCoord2fVertex3fSUN(s, t, x, y, z):
	pass


@params(api='gl', prms=['tc', 'v'])
def glTexCoord2fVertex3fvSUN(tc, v):
	pass


@params(api='gl', prms=['s', 't', 'p', 'q', 'x', 'y', 'z', 'w'])
def glTexCoord4fVertex4fSUN(s, t, p, q, x, y, z, w):
	pass


@params(api='gl', prms=['tc', 'v'])
def glTexCoord4fVertex4fvSUN(tc, v):
	pass


@params(api='gl', prms=['s', 't', 'r', 'g', 'b', 'a', 'x', 'y', 'z'])
def glTexCoord2fColor4ubVertex3fSUN(s, t, r, g, b, a, x, y, z):
	pass


@params(api='gl', prms=['tc', 'c', 'v'])
def glTexCoord2fColor4ubVertex3fvSUN(tc, c, v):
	pass


@params(api='gl', prms=['s', 't', 'r', 'g', 'b', 'x', 'y', 'z'])
def glTexCoord2fColor3fVertex3fSUN(s, t, r, g, b, x, y, z):
	pass


@params(api='gl', prms=['tc', 'c', 'v'])
def glTexCoord2fColor3fVertex3fvSUN(tc, c, v):
	pass


@params(api='gl', prms=['s', 't', 'nx', 'ny', 'nz', 'x', 'y', 'z'])
def glTexCoord2fNormal3fVertex3fSUN(s, t, nx, ny, nz, x, y, z):
	pass


@params(api='gl', prms=['tc', 'n', 'v'])
def glTexCoord2fNormal3fVertex3fvSUN(tc, n, v):
	pass


@params(api='gl', prms=['s', 't', 'r', 'g', 'b', 'a', 'nx', 'ny', 'nz', 'x', 'y', 'z'])
def glTexCoord2fColor4fNormal3fVertex3fSUN(s, t, r, g, b, a, nx, ny, nz, x, y, z):
	pass


@params(api='gl', prms=['tc', 'c', 'n', 'v'])
def glTexCoord2fColor4fNormal3fVertex3fvSUN(tc, c, n, v):
	pass


@params(api='gl', prms=['s', 't', 'p', 'q', 'r', 'g', 'b', 'a', 'nx', 'ny', 'nz', 'x', 'y', 'z', 'w'])
def glTexCoord4fColor4fNormal3fVertex4fSUN(s, t, p, q, r, g, b, a, nx, ny, nz, x, y, z, w):
	pass


@params(api='gl', prms=['tc', 'c', 'n', 'v'])
def glTexCoord4fColor4fNormal3fVertex4fvSUN(tc, c, n, v):
	pass


@params(api='gl', prms=['rc', 'x', 'y', 'z'])
def glReplacementCodeuiVertex3fSUN(rc, x, y, z):
	pass


@params(api='gl', prms=['rc', 'v'])
def glReplacementCodeuiVertex3fvSUN(rc, v):
	pass


@params(api='gl', prms=['rc', 'r', 'g', 'b', 'a', 'x', 'y', 'z'])
def glReplacementCodeuiColor4ubVertex3fSUN(rc, r, g, b, a, x, y, z):
	pass


@params(api='gl', prms=['rc', 'c', 'v'])
def glReplacementCodeuiColor4ubVertex3fvSUN(rc, c, v):
	pass


@params(api='gl', prms=['rc', 'r', 'g', 'b', 'x', 'y', 'z'])
def glReplacementCodeuiColor3fVertex3fSUN(rc, r, g, b, x, y, z):
	pass


@params(api='gl', prms=['rc', 'c', 'v'])
def glReplacementCodeuiColor3fVertex3fvSUN(rc, c, v):
	pass


@params(api='gl', prms=['rc', 'nx', 'ny', 'nz', 'x', 'y', 'z'])
def glReplacementCodeuiNormal3fVertex3fSUN(rc, nx, ny, nz, x, y, z):
	pass


@params(api='gl', prms=['rc', 'n', 'v'])
def glReplacementCodeuiNormal3fVertex3fvSUN(rc, n, v):
	pass


@params(api='gl', prms=['rc', 'r', 'g', 'b', 'a', 'nx', 'ny', 'nz', 'x', 'y', 'z'])
def glReplacementCodeuiColor4fNormal3fVertex3fSUN(rc, r, g, b, a, nx, ny, nz, x, y, z):
	pass


@params(api='gl', prms=['rc', 'c', 'n', 'v'])
def glReplacementCodeuiColor4fNormal3fVertex3fvSUN(rc, c, n, v):
	pass


@params(api='gl', prms=['rc', 's', 't', 'x', 'y', 'z'])
def glReplacementCodeuiTexCoord2fVertex3fSUN(rc, s, t, x, y, z):
	pass


@params(api='gl', prms=['rc', 'tc', 'v'])
def glReplacementCodeuiTexCoord2fVertex3fvSUN(rc, tc, v):
	pass


@params(api='gl', prms=['rc', 's', 't', 'nx', 'ny', 'nz', 'x', 'y', 'z'])
def glReplacementCodeuiTexCoord2fNormal3fVertex3fSUN(rc, s, t, nx, ny, nz, x, y, z):
	pass


@params(api='gl', prms=['rc', 'tc', 'n', 'v'])
def glReplacementCodeuiTexCoord2fNormal3fVertex3fvSUN(rc, tc, n, v):
	pass


@params(api='gl', prms=['rc', 's', 't', 'r', 'g', 'b', 'a', 'nx', 'ny', 'nz', 'x', 'y', 'z'])
def glReplacementCodeuiTexCoord2fColor4fNormal3fVertex3fSUN(rc, s, t, r, g, b, a, nx, ny, nz, x, y, z):
	pass


@params(api='gl', prms=['rc', 'tc', 'c', 'n', 'v'])
def glReplacementCodeuiTexCoord2fColor4fNormal3fVertex3fvSUN(rc, tc, c, n, v):
	pass


