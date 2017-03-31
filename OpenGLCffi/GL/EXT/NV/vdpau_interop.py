@params('vdpDevice', 'getProcAddress', api='gl')
def glVDPAUInitNV(vdpDevice, getProcAddress):
	pass


@params(api = 'gl')
def glVDPAUFiniNV():
	pass


@params('vdpSurface', 'target', 'numTextureNames', 'textureNames', api='gl')
def glVDPAURegisterVideoSurfaceNV(vdpSurface, target, numTextureNames, textureNames):
	pass


@params('vdpSurface', 'target', 'numTextureNames', 'textureNames', api='gl')
def glVDPAURegisterOutputSurfaceNV(vdpSurface, target, numTextureNames, textureNames):
	pass


@params('surface', api='gl')
def glVDPAUIsSurfaceNV(surface):
	pass


@params('surface', api='gl')
def glVDPAUUnregisterSurfaceNV(surface):
	pass


@params('surface', 'pname', 'bufSize', 'length', 'values', api='gl')
def glVDPAUGetSurfaceivNV(surface, pname, bufSize, length, values):
	pass


@params('surface', 'access', api='gl')
def glVDPAUSurfaceAccessNV(surface, access):
	pass


@params('numSurfaces', 'surfaces', api='gl')
def glVDPAUMapSurfacesNV(numSurfaces, surfaces):
	pass


@params('numSurface', 'surfaces', api='gl')
def glVDPAUUnmapSurfacesNV(numSurface, surfaces):
	pass


