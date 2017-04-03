from OpenGLCffi.GL import params
@params('r', 'g', 'b', 'a', 'x', 'y', api='gl')
def glColor4ubVertex2fSUN(r, g, b, a, x, y):
	pass


@params('c', 'v', api='gl')
def glColor4ubVertex2fvSUN(c, v):
	pass


@params('r', 'g', 'b', 'a', 'x', 'y', 'z', api='gl')
def glColor4ubVertex3fSUN(r, g, b, a, x, y, z):
	pass


@params('c', 'v', api='gl')
def glColor4ubVertex3fvSUN(c, v):
	pass


@params('r', 'g', 'b', 'x', 'y', 'z', api='gl')
def glColor3fVertex3fSUN(r, g, b, x, y, z):
	pass


@params('c', 'v', api='gl')
def glColor3fVertex3fvSUN(c, v):
	pass


@params('nx', 'ny', 'nz', 'x', 'y', 'z', api='gl')
def glNormal3fVertex3fSUN(nx, ny, nz, x, y, z):
	pass


@params('n', 'v', api='gl')
def glNormal3fVertex3fvSUN(n, v):
	pass


@params('r', 'g', 'b', 'a', 'nx', 'ny', 'nz', 'x', 'y', 'z', api='gl')
def glColor4fNormal3fVertex3fSUN(r, g, b, a, nx, ny, nz, x, y, z):
	pass


@params('c', 'n', 'v', api='gl')
def glColor4fNormal3fVertex3fvSUN(c, n, v):
	pass


@params('s', 't', 'x', 'y', 'z', api='gl')
def glTexCoord2fVertex3fSUN(s, t, x, y, z):
	pass


@params('tc', 'v', api='gl')
def glTexCoord2fVertex3fvSUN(tc, v):
	pass


@params('s', 't', 'p', 'q', 'x', 'y', 'z', 'w', api='gl')
def glTexCoord4fVertex4fSUN(s, t, p, q, x, y, z, w):
	pass


@params('tc', 'v', api='gl')
def glTexCoord4fVertex4fvSUN(tc, v):
	pass


@params('s', 't', 'r', 'g', 'b', 'a', 'x', 'y', 'z', api='gl')
def glTexCoord2fColor4ubVertex3fSUN(s, t, r, g, b, a, x, y, z):
	pass


@params('tc', 'c', 'v', api='gl')
def glTexCoord2fColor4ubVertex3fvSUN(tc, c, v):
	pass


@params('s', 't', 'r', 'g', 'b', 'x', 'y', 'z', api='gl')
def glTexCoord2fColor3fVertex3fSUN(s, t, r, g, b, x, y, z):
	pass


@params('tc', 'c', 'v', api='gl')
def glTexCoord2fColor3fVertex3fvSUN(tc, c, v):
	pass


@params('s', 't', 'nx', 'ny', 'nz', 'x', 'y', 'z', api='gl')
def glTexCoord2fNormal3fVertex3fSUN(s, t, nx, ny, nz, x, y, z):
	pass


@params('tc', 'n', 'v', api='gl')
def glTexCoord2fNormal3fVertex3fvSUN(tc, n, v):
	pass


@params('s', 't', 'r', 'g', 'b', 'a', 'nx', 'ny', 'nz', 'x', 'y', 'z', api='gl')
def glTexCoord2fColor4fNormal3fVertex3fSUN(s, t, r, g, b, a, nx, ny, nz, x, y, z):
	pass


@params('tc', 'c', 'n', 'v', api='gl')
def glTexCoord2fColor4fNormal3fVertex3fvSUN(tc, c, n, v):
	pass


@params('s', 't', 'p', 'q', 'r', 'g', 'b', 'a', 'nx', 'ny', 'nz', 'x', 'y', 'z', 'w', api='gl')
def glTexCoord4fColor4fNormal3fVertex4fSUN(s, t, p, q, r, g, b, a, nx, ny, nz, x, y, z, w):
	pass


@params('tc', 'c', 'n', 'v', api='gl')
def glTexCoord4fColor4fNormal3fVertex4fvSUN(tc, c, n, v):
	pass


@params('rc', 'x', 'y', 'z', api='gl')
def glReplacementCodeuiVertex3fSUN(rc, x, y, z):
	pass


@params('rc', 'v', api='gl')
def glReplacementCodeuiVertex3fvSUN(rc, v):
	pass


@params('rc', 'r', 'g', 'b', 'a', 'x', 'y', 'z', api='gl')
def glReplacementCodeuiColor4ubVertex3fSUN(rc, r, g, b, a, x, y, z):
	pass


@params('rc', 'c', 'v', api='gl')
def glReplacementCodeuiColor4ubVertex3fvSUN(rc, c, v):
	pass


@params('rc', 'r', 'g', 'b', 'x', 'y', 'z', api='gl')
def glReplacementCodeuiColor3fVertex3fSUN(rc, r, g, b, x, y, z):
	pass


@params('rc', 'c', 'v', api='gl')
def glReplacementCodeuiColor3fVertex3fvSUN(rc, c, v):
	pass


@params('rc', 'nx', 'ny', 'nz', 'x', 'y', 'z', api='gl')
def glReplacementCodeuiNormal3fVertex3fSUN(rc, nx, ny, nz, x, y, z):
	pass


@params('rc', 'n', 'v', api='gl')
def glReplacementCodeuiNormal3fVertex3fvSUN(rc, n, v):
	pass


@params('rc', 'r', 'g', 'b', 'a', 'nx', 'ny', 'nz', 'x', 'y', 'z', api='gl')
def glReplacementCodeuiColor4fNormal3fVertex3fSUN(rc, r, g, b, a, nx, ny, nz, x, y, z):
	pass


@params('rc', 'c', 'n', 'v', api='gl')
def glReplacementCodeuiColor4fNormal3fVertex3fvSUN(rc, c, n, v):
	pass


@params('rc', 's', 't', 'x', 'y', 'z', api='gl')
def glReplacementCodeuiTexCoord2fVertex3fSUN(rc, s, t, x, y, z):
	pass


@params('rc', 'tc', 'v', api='gl')
def glReplacementCodeuiTexCoord2fVertex3fvSUN(rc, tc, v):
	pass


@params('rc', 's', 't', 'nx', 'ny', 'nz', 'x', 'y', 'z', api='gl')
def glReplacementCodeuiTexCoord2fNormal3fVertex3fSUN(rc, s, t, nx, ny, nz, x, y, z):
	pass


@params('rc', 'tc', 'n', 'v', api='gl')
def glReplacementCodeuiTexCoord2fNormal3fVertex3fvSUN(rc, tc, n, v):
	pass


@params('rc', 's', 't', 'r', 'g', 'b', 'a', 'nx', 'ny', 'nz', 'x', 'y', 'z', api='gl')
def glReplacementCodeuiTexCoord2fColor4fNormal3fVertex3fSUN(rc, s, t, r, g, b, a, nx, ny, nz, x, y, z):
	pass


@params('rc', 'tc', 'c', 'n', 'v', api='gl')
def glReplacementCodeuiTexCoord2fColor4fNormal3fVertex3fvSUN(rc, tc, c, n, v):
	pass


