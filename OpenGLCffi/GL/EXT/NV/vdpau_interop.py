from OpenGLCffi.GL import params
@params(api='gl', prms=['vdpDevice', 'getProcAddress'])
def glVDPAUInitNV(vdpDevice, getProcAddress):
	pass


@params(api='gl', prms=[])
def glVDPAUFiniNV():
	pass


@params(api='gl', prms=['vdpSurface', 'target', 'numTextureNames', 'textureNames'])
def glVDPAURegisterVideoSurfaceNV(vdpSurface, target, numTextureNames, textureNames):
	pass


@params(api='gl', prms=['vdpSurface', 'target', 'numTextureNames', 'textureNames'])
def glVDPAURegisterOutputSurfaceNV(vdpSurface, target, numTextureNames, textureNames):
	pass


@params(api='gl', prms=['surface'])
def glVDPAUIsSurfaceNV(surface):
	pass


@params(api='gl', prms=['surface'])
def glVDPAUUnregisterSurfaceNV(surface):
	pass


@params(api='gl', prms=['surface', 'pname', 'bufSize', 'length', 'values'])
def glVDPAUGetSurfaceivNV(surface, pname, bufSize, length, values):
	pass


@params(api='gl', prms=['surface', 'access'])
def glVDPAUSurfaceAccessNV(surface, access):
	pass


@params(api='gl', prms=['numSurfaces', 'surfaces'])
def glVDPAUMapSurfacesNV(numSurfaces, surfaces):
	pass


@params(api='gl', prms=['numSurface', 'surfaces'])
def glVDPAUUnmapSurfacesNV(numSurface, surfaces):
	pass


