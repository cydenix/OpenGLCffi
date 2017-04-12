from OpenGLCffi.GL import params
@params(api='gl', prms=['mode', 'm'])
def glMatrixLoadfEXT(mode, m):
	pass


@params(api='gl', prms=['mode', 'm'])
def glMatrixLoaddEXT(mode, m):
	pass


@params(api='gl', prms=['mode', 'm'])
def glMatrixMultfEXT(mode, m):
	pass


@params(api='gl', prms=['mode', 'm'])
def glMatrixMultdEXT(mode, m):
	pass


@params(api='gl', prms=['mode'])
def glMatrixLoadIdentityEXT(mode):
	pass


@params(api='gl', prms=['mode', 'angle', 'x', 'y', 'z'])
def glMatrixRotatefEXT(mode, angle, x, y, z):
	pass


@params(api='gl', prms=['mode', 'angle', 'x', 'y', 'z'])
def glMatrixRotatedEXT(mode, angle, x, y, z):
	pass


@params(api='gl', prms=['mode', 'x', 'y', 'z'])
def glMatrixScalefEXT(mode, x, y, z):
	pass


@params(api='gl', prms=['mode', 'x', 'y', 'z'])
def glMatrixScaledEXT(mode, x, y, z):
	pass


@params(api='gl', prms=['mode', 'x', 'y', 'z'])
def glMatrixTranslatefEXT(mode, x, y, z):
	pass


@params(api='gl', prms=['mode', 'x', 'y', 'z'])
def glMatrixTranslatedEXT(mode, x, y, z):
	pass


@params(api='gl', prms=['mode', 'left', 'right', 'bottom', 'top', 'zNear', 'zFar'])
def glMatrixFrustumEXT(mode, left, right, bottom, top, zNear, zFar):
	pass


@params(api='gl', prms=['mode', 'left', 'right', 'bottom', 'top', 'zNear', 'zFar'])
def glMatrixOrthoEXT(mode, left, right, bottom, top, zNear, zFar):
	pass


@params(api='gl', prms=['mode'])
def glMatrixPopEXT(mode):
	pass


@params(api='gl', prms=['mode'])
def glMatrixPushEXT(mode):
	pass


@params(api='gl', prms=['mask'])
def glClientAttribDefaultEXT(mask):
	pass


@params(api='gl', prms=['mask'])
def glPushClientAttribDefaultEXT(mask):
	pass


@params(api='gl', prms=['texture', 'target', 'pname', 'param'])
def glTextureParameterfEXT(texture, target, pname, param):
	pass


@params(api='gl', prms=['texture', 'target', 'pname', 'params'])
def glTextureParameterfvEXT(texture, target, pname, params):
	pass


@params(api='gl', prms=['texture', 'target', 'pname', 'param'])
def glTextureParameteriEXT(texture, target, pname, param):
	pass


@params(api='gl', prms=['texture', 'target', 'pname', 'params'])
def glTextureParameterivEXT(texture, target, pname, params):
	pass


@params(api='gl', prms=['texture', 'target', 'level', 'internalformat', 'width', 'border', 'format', 'type', 'pixels'])
def glTextureImage1DEXT(texture, target, level, internalformat, width, border, format, type, pixels):
	pass


@params(api='gl', prms=['texture', 'target', 'level', 'internalformat', 'width', 'height', 'border', 'format', 'type', 'pixels'])
def glTextureImage2DEXT(texture, target, level, internalformat, width, height, border, format, type, pixels):
	pass


@params(api='gl', prms=['texture', 'target', 'level', 'xoffset', 'width', 'format', 'type', 'pixels'])
def glTextureSubImage1DEXT(texture, target, level, xoffset, width, format, type, pixels):
	pass


@params(api='gl', prms=['texture', 'target', 'level', 'xoffset', 'yoffset', 'width', 'height', 'format', 'type', 'pixels'])
def glTextureSubImage2DEXT(texture, target, level, xoffset, yoffset, width, height, format, type, pixels):
	pass


@params(api='gl', prms=['texture', 'target', 'level', 'internalformat', 'x', 'y', 'width', 'border'])
def glCopyTextureImage1DEXT(texture, target, level, internalformat, x, y, width, border):
	pass


@params(api='gl', prms=['texture', 'target', 'level', 'internalformat', 'x', 'y', 'width', 'height', 'border'])
def glCopyTextureImage2DEXT(texture, target, level, internalformat, x, y, width, height, border):
	pass


@params(api='gl', prms=['texture', 'target', 'level', 'xoffset', 'x', 'y', 'width'])
def glCopyTextureSubImage1DEXT(texture, target, level, xoffset, x, y, width):
	pass


@params(api='gl', prms=['texture', 'target', 'level', 'xoffset', 'yoffset', 'x', 'y', 'width', 'height'])
def glCopyTextureSubImage2DEXT(texture, target, level, xoffset, yoffset, x, y, width, height):
	pass


@params(api='gl', prms=['texture', 'target', 'level', 'format', 'type', 'pixels'])
def glGetTextureImageEXT(texture, target, level, format, type, pixels):
	pass


@params(api='gl', prms=['texture', 'target', 'pname', 'params'])
def glGetTextureParameterfvEXT(texture, target, pname, params):
	pass


@params(api='gl', prms=['texture', 'target', 'pname', 'params'])
def glGetTextureParameterivEXT(texture, target, pname, params):
	pass


@params(api='gl', prms=['texture', 'target', 'level', 'pname', 'params'])
def glGetTextureLevelParameterfvEXT(texture, target, level, pname, params):
	pass


@params(api='gl', prms=['texture', 'target', 'level', 'pname', 'params'])
def glGetTextureLevelParameterivEXT(texture, target, level, pname, params):
	pass


@params(api='gl', prms=['texture', 'target', 'level', 'internalformat', 'width', 'height', 'depth', 'border', 'format', 'type', 'pixels'])
def glTextureImage3DEXT(texture, target, level, internalformat, width, height, depth, border, format, type, pixels):
	pass


@params(api='gl', prms=['texture', 'target', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth', 'format', 'type', 'pixels'])
def glTextureSubImage3DEXT(texture, target, level, xoffset, yoffset, zoffset, width, height, depth, format, type, pixels):
	pass


@params(api='gl', prms=['texture', 'target', 'level', 'xoffset', 'yoffset', 'zoffset', 'x', 'y', 'width', 'height'])
def glCopyTextureSubImage3DEXT(texture, target, level, xoffset, yoffset, zoffset, x, y, width, height):
	pass


@params(api='gl', prms=['texunit', 'target', 'texture'])
def glBindMultiTextureEXT(texunit, target, texture):
	pass


@params(api='gl', prms=['texunit', 'size', 'type', 'stride', 'pointer'])
def glMultiTexCoordPointerEXT(texunit, size, type, stride, pointer):
	pass


@params(api='gl', prms=['texunit', 'target', 'pname', 'param'])
def glMultiTexEnvfEXT(texunit, target, pname, param):
	pass


@params(api='gl', prms=['texunit', 'target', 'pname', 'params'])
def glMultiTexEnvfvEXT(texunit, target, pname, params):
	pass


@params(api='gl', prms=['texunit', 'target', 'pname', 'param'])
def glMultiTexEnviEXT(texunit, target, pname, param):
	pass


@params(api='gl', prms=['texunit', 'target', 'pname', 'params'])
def glMultiTexEnvivEXT(texunit, target, pname, params):
	pass


@params(api='gl', prms=['texunit', 'coord', 'pname', 'param'])
def glMultiTexGendEXT(texunit, coord, pname, param):
	pass


@params(api='gl', prms=['texunit', 'coord', 'pname', 'params'])
def glMultiTexGendvEXT(texunit, coord, pname, params):
	pass


@params(api='gl', prms=['texunit', 'coord', 'pname', 'param'])
def glMultiTexGenfEXT(texunit, coord, pname, param):
	pass


@params(api='gl', prms=['texunit', 'coord', 'pname', 'params'])
def glMultiTexGenfvEXT(texunit, coord, pname, params):
	pass


@params(api='gl', prms=['texunit', 'coord', 'pname', 'param'])
def glMultiTexGeniEXT(texunit, coord, pname, param):
	pass


@params(api='gl', prms=['texunit', 'coord', 'pname', 'params'])
def glMultiTexGenivEXT(texunit, coord, pname, params):
	pass


@params(api='gl', prms=['texunit', 'target', 'pname', 'params'])
def glGetMultiTexEnvfvEXT(texunit, target, pname, params):
	pass


@params(api='gl', prms=['texunit', 'target', 'pname', 'params'])
def glGetMultiTexEnvivEXT(texunit, target, pname, params):
	pass


@params(api='gl', prms=['texunit', 'coord', 'pname', 'params'])
def glGetMultiTexGendvEXT(texunit, coord, pname, params):
	pass


@params(api='gl', prms=['texunit', 'coord', 'pname', 'params'])
def glGetMultiTexGenfvEXT(texunit, coord, pname, params):
	pass


@params(api='gl', prms=['texunit', 'coord', 'pname', 'params'])
def glGetMultiTexGenivEXT(texunit, coord, pname, params):
	pass


@params(api='gl', prms=['texunit', 'target', 'pname', 'param'])
def glMultiTexParameteriEXT(texunit, target, pname, param):
	pass


@params(api='gl', prms=['texunit', 'target', 'pname', 'params'])
def glMultiTexParameterivEXT(texunit, target, pname, params):
	pass


@params(api='gl', prms=['texunit', 'target', 'pname', 'param'])
def glMultiTexParameterfEXT(texunit, target, pname, param):
	pass


@params(api='gl', prms=['texunit', 'target', 'pname', 'params'])
def glMultiTexParameterfvEXT(texunit, target, pname, params):
	pass


@params(api='gl', prms=['texunit', 'target', 'level', 'internalformat', 'width', 'border', 'format', 'type', 'pixels'])
def glMultiTexImage1DEXT(texunit, target, level, internalformat, width, border, format, type, pixels):
	pass


@params(api='gl', prms=['texunit', 'target', 'level', 'internalformat', 'width', 'height', 'border', 'format', 'type', 'pixels'])
def glMultiTexImage2DEXT(texunit, target, level, internalformat, width, height, border, format, type, pixels):
	pass


@params(api='gl', prms=['texunit', 'target', 'level', 'xoffset', 'width', 'format', 'type', 'pixels'])
def glMultiTexSubImage1DEXT(texunit, target, level, xoffset, width, format, type, pixels):
	pass


@params(api='gl', prms=['texunit', 'target', 'level', 'xoffset', 'yoffset', 'width', 'height', 'format', 'type', 'pixels'])
def glMultiTexSubImage2DEXT(texunit, target, level, xoffset, yoffset, width, height, format, type, pixels):
	pass


@params(api='gl', prms=['texunit', 'target', 'level', 'internalformat', 'x', 'y', 'width', 'border'])
def glCopyMultiTexImage1DEXT(texunit, target, level, internalformat, x, y, width, border):
	pass


@params(api='gl', prms=['texunit', 'target', 'level', 'internalformat', 'x', 'y', 'width', 'height', 'border'])
def glCopyMultiTexImage2DEXT(texunit, target, level, internalformat, x, y, width, height, border):
	pass


@params(api='gl', prms=['texunit', 'target', 'level', 'xoffset', 'x', 'y', 'width'])
def glCopyMultiTexSubImage1DEXT(texunit, target, level, xoffset, x, y, width):
	pass


@params(api='gl', prms=['texunit', 'target', 'level', 'xoffset', 'yoffset', 'x', 'y', 'width', 'height'])
def glCopyMultiTexSubImage2DEXT(texunit, target, level, xoffset, yoffset, x, y, width, height):
	pass


@params(api='gl', prms=['texunit', 'target', 'level', 'format', 'type', 'pixels'])
def glGetMultiTexImageEXT(texunit, target, level, format, type, pixels):
	pass


@params(api='gl', prms=['texunit', 'target', 'pname', 'params'])
def glGetMultiTexParameterfvEXT(texunit, target, pname, params):
	pass


@params(api='gl', prms=['texunit', 'target', 'pname', 'params'])
def glGetMultiTexParameterivEXT(texunit, target, pname, params):
	pass


@params(api='gl', prms=['texunit', 'target', 'level', 'pname', 'params'])
def glGetMultiTexLevelParameterfvEXT(texunit, target, level, pname, params):
	pass


@params(api='gl', prms=['texunit', 'target', 'level', 'pname', 'params'])
def glGetMultiTexLevelParameterivEXT(texunit, target, level, pname, params):
	pass


@params(api='gl', prms=['texunit', 'target', 'level', 'internalformat', 'width', 'height', 'depth', 'border', 'format', 'type', 'pixels'])
def glMultiTexImage3DEXT(texunit, target, level, internalformat, width, height, depth, border, format, type, pixels):
	pass


@params(api='gl', prms=['texunit', 'target', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth', 'format', 'type', 'pixels'])
def glMultiTexSubImage3DEXT(texunit, target, level, xoffset, yoffset, zoffset, width, height, depth, format, type, pixels):
	pass


@params(api='gl', prms=['texunit', 'target', 'level', 'xoffset', 'yoffset', 'zoffset', 'x', 'y', 'width', 'height'])
def glCopyMultiTexSubImage3DEXT(texunit, target, level, xoffset, yoffset, zoffset, x, y, width, height):
	pass


@params(api='gl', prms=['array', 'index'])
def glEnableClientStateIndexedEXT(array, index):
	pass


@params(api='gl', prms=['array', 'index'])
def glDisableClientStateIndexedEXT(array, index):
	pass


@params(api='gl', prms=['target', 'index', 'data'])
def glGetFloatIndexedvEXT(target, index, data):
	pass


@params(api='gl', prms=['target', 'index', 'data'])
def glGetDoubleIndexedvEXT(target, index, data):
	pass


@params(api='gl', prms=['target', 'index', 'data'])
def glGetPointerIndexedvEXT(target, index, data):
	pass


@params(api='gl', prms=['target', 'index'])
def glEnableIndexedEXT(target, index):
	pass


@params(api='gl', prms=['target', 'index'])
def glDisableIndexedEXT(target, index):
	pass


@params(api='gl', prms=['target', 'index'])
def glIsEnabledIndexedEXT(target, index):
	pass


@params(api='gl', prms=['target', 'index', 'data'])
def glGetIntegerIndexedvEXT(target, index, data):
	pass


@params(api='gl', prms=['target', 'index', 'data'])
def glGetBooleanIndexedvEXT(target, index, data):
	pass


@params(api='gl', prms=['texture', 'target', 'level', 'internalformat', 'width', 'height', 'depth', 'border', 'imageSize', 'bits'])
def glCompressedTextureImage3DEXT(texture, target, level, internalformat, width, height, depth, border, imageSize, bits):
	pass


@params(api='gl', prms=['texture', 'target', 'level', 'internalformat', 'width', 'height', 'border', 'imageSize', 'bits'])
def glCompressedTextureImage2DEXT(texture, target, level, internalformat, width, height, border, imageSize, bits):
	pass


@params(api='gl', prms=['texture', 'target', 'level', 'internalformat', 'width', 'border', 'imageSize', 'bits'])
def glCompressedTextureImage1DEXT(texture, target, level, internalformat, width, border, imageSize, bits):
	pass


@params(api='gl', prms=['texture', 'target', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth', 'format', 'imageSize', 'bits'])
def glCompressedTextureSubImage3DEXT(texture, target, level, xoffset, yoffset, zoffset, width, height, depth, format, imageSize, bits):
	pass


@params(api='gl', prms=['texture', 'target', 'level', 'xoffset', 'yoffset', 'width', 'height', 'format', 'imageSize', 'bits'])
def glCompressedTextureSubImage2DEXT(texture, target, level, xoffset, yoffset, width, height, format, imageSize, bits):
	pass


@params(api='gl', prms=['texture', 'target', 'level', 'xoffset', 'width', 'format', 'imageSize', 'bits'])
def glCompressedTextureSubImage1DEXT(texture, target, level, xoffset, width, format, imageSize, bits):
	pass


@params(api='gl', prms=['texture', 'target', 'lod', 'img'])
def glGetCompressedTextureImageEXT(texture, target, lod, img):
	pass


@params(api='gl', prms=['texunit', 'target', 'level', 'internalformat', 'width', 'height', 'depth', 'border', 'imageSize', 'bits'])
def glCompressedMultiTexImage3DEXT(texunit, target, level, internalformat, width, height, depth, border, imageSize, bits):
	pass


@params(api='gl', prms=['texunit', 'target', 'level', 'internalformat', 'width', 'height', 'border', 'imageSize', 'bits'])
def glCompressedMultiTexImage2DEXT(texunit, target, level, internalformat, width, height, border, imageSize, bits):
	pass


@params(api='gl', prms=['texunit', 'target', 'level', 'internalformat', 'width', 'border', 'imageSize', 'bits'])
def glCompressedMultiTexImage1DEXT(texunit, target, level, internalformat, width, border, imageSize, bits):
	pass


@params(api='gl', prms=['texunit', 'target', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth', 'format', 'imageSize', 'bits'])
def glCompressedMultiTexSubImage3DEXT(texunit, target, level, xoffset, yoffset, zoffset, width, height, depth, format, imageSize, bits):
	pass


@params(api='gl', prms=['texunit', 'target', 'level', 'xoffset', 'yoffset', 'width', 'height', 'format', 'imageSize', 'bits'])
def glCompressedMultiTexSubImage2DEXT(texunit, target, level, xoffset, yoffset, width, height, format, imageSize, bits):
	pass


@params(api='gl', prms=['texunit', 'target', 'level', 'xoffset', 'width', 'format', 'imageSize', 'bits'])
def glCompressedMultiTexSubImage1DEXT(texunit, target, level, xoffset, width, format, imageSize, bits):
	pass


@params(api='gl', prms=['texunit', 'target', 'lod', 'img'])
def glGetCompressedMultiTexImageEXT(texunit, target, lod, img):
	pass


@params(api='gl', prms=['mode', 'm'])
def glMatrixLoadTransposefEXT(mode, m):
	pass


@params(api='gl', prms=['mode', 'm'])
def glMatrixLoadTransposedEXT(mode, m):
	pass


@params(api='gl', prms=['mode', 'm'])
def glMatrixMultTransposefEXT(mode, m):
	pass


@params(api='gl', prms=['mode', 'm'])
def glMatrixMultTransposedEXT(mode, m):
	pass


@params(api='gl', prms=['buffer', 'size', 'data', 'usage'])
def glNamedBufferDataEXT(buffer, size, data, usage):
	pass


@params(api='gl', prms=['buffer', 'offset', 'size', 'data'])
def glNamedBufferSubDataEXT(buffer, offset, size, data):
	pass


@params(api='gl', prms=['buffer', 'access'])
def glMapNamedBufferEXT(buffer, access):
	pass


@params(api='gl', prms=['buffer'])
def glUnmapNamedBufferEXT(buffer):
	pass


@params(api='gl', prms=['buffer', 'pname', 'params'])
def glGetNamedBufferParameterivEXT(buffer, pname, params):
	pass


@params(api='gl', prms=['buffer', 'pname', 'params'])
def glGetNamedBufferPointervEXT(buffer, pname, params):
	pass


@params(api='gl', prms=['buffer', 'offset', 'size', 'data'])
def glGetNamedBufferSubDataEXT(buffer, offset, size, data):
	pass


@params(api='gl', prms=['program', 'location', 'v0'])
def glProgramUniform1fEXT(program, location, v0):
	pass


@params(api='gl', prms=['program', 'location', 'v0', 'v1'])
def glProgramUniform2fEXT(program, location, v0, v1):
	pass


@params(api='gl', prms=['program', 'location', 'v0', 'v1', 'v2'])
def glProgramUniform3fEXT(program, location, v0, v1, v2):
	pass


@params(api='gl', prms=['program', 'location', 'v0', 'v1', 'v2', 'v3'])
def glProgramUniform4fEXT(program, location, v0, v1, v2, v3):
	pass


@params(api='gl', prms=['program', 'location', 'v0'])
def glProgramUniform1iEXT(program, location, v0):
	pass


@params(api='gl', prms=['program', 'location', 'v0', 'v1'])
def glProgramUniform2iEXT(program, location, v0, v1):
	pass


@params(api='gl', prms=['program', 'location', 'v0', 'v1', 'v2'])
def glProgramUniform3iEXT(program, location, v0, v1, v2):
	pass


@params(api='gl', prms=['program', 'location', 'v0', 'v1', 'v2', 'v3'])
def glProgramUniform4iEXT(program, location, v0, v1, v2, v3):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform1fvEXT(program, location, count, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform2fvEXT(program, location, count, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform3fvEXT(program, location, count, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform4fvEXT(program, location, count, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform1ivEXT(program, location, count, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform2ivEXT(program, location, count, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform3ivEXT(program, location, count, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform4ivEXT(program, location, count, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix2fvEXT(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix3fvEXT(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix4fvEXT(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix2x3fvEXT(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix3x2fvEXT(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix2x4fvEXT(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix4x2fvEXT(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix3x4fvEXT(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix4x3fvEXT(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['texture', 'target', 'internalformat', 'buffer'])
def glTextureBufferEXT(texture, target, internalformat, buffer):
	pass


@params(api='gl', prms=['texunit', 'target', 'internalformat', 'buffer'])
def glMultiTexBufferEXT(texunit, target, internalformat, buffer):
	pass


@params(api='gl', prms=['texture', 'target', 'pname', 'params'])
def glTextureParameterIivEXT(texture, target, pname, params):
	pass


@params(api='gl', prms=['texture', 'target', 'pname', 'params'])
def glTextureParameterIuivEXT(texture, target, pname, params):
	pass


@params(api='gl', prms=['texture', 'target', 'pname', 'params'])
def glGetTextureParameterIivEXT(texture, target, pname, params):
	pass


@params(api='gl', prms=['texture', 'target', 'pname', 'params'])
def glGetTextureParameterIuivEXT(texture, target, pname, params):
	pass


@params(api='gl', prms=['texunit', 'target', 'pname', 'params'])
def glMultiTexParameterIivEXT(texunit, target, pname, params):
	pass


@params(api='gl', prms=['texunit', 'target', 'pname', 'params'])
def glMultiTexParameterIuivEXT(texunit, target, pname, params):
	pass


@params(api='gl', prms=['texunit', 'target', 'pname', 'params'])
def glGetMultiTexParameterIivEXT(texunit, target, pname, params):
	pass


@params(api='gl', prms=['texunit', 'target', 'pname', 'params'])
def glGetMultiTexParameterIuivEXT(texunit, target, pname, params):
	pass


@params(api='gl', prms=['program', 'location', 'v0'])
def glProgramUniform1uiEXT(program, location, v0):
	pass


@params(api='gl', prms=['program', 'location', 'v0', 'v1'])
def glProgramUniform2uiEXT(program, location, v0, v1):
	pass


@params(api='gl', prms=['program', 'location', 'v0', 'v1', 'v2'])
def glProgramUniform3uiEXT(program, location, v0, v1, v2):
	pass


@params(api='gl', prms=['program', 'location', 'v0', 'v1', 'v2', 'v3'])
def glProgramUniform4uiEXT(program, location, v0, v1, v2, v3):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform1uivEXT(program, location, count, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform2uivEXT(program, location, count, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform3uivEXT(program, location, count, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform4uivEXT(program, location, count, value):
	pass


@params(api='gl', prms=['program', 'target', 'index', 'count', 'params'])
def glNamedProgramLocalParameters4fvEXT(program, target, index, count, params):
	pass


@params(api='gl', prms=['program', 'target', 'index', 'x', 'y', 'z', 'w'])
def glNamedProgramLocalParameterI4iEXT(program, target, index, x, y, z, w):
	pass


@params(api='gl', prms=['program', 'target', 'index', 'params'])
def glNamedProgramLocalParameterI4ivEXT(program, target, index, params):
	pass


@params(api='gl', prms=['program', 'target', 'index', 'count', 'params'])
def glNamedProgramLocalParametersI4ivEXT(program, target, index, count, params):
	pass


@params(api='gl', prms=['program', 'target', 'index', 'x', 'y', 'z', 'w'])
def glNamedProgramLocalParameterI4uiEXT(program, target, index, x, y, z, w):
	pass


@params(api='gl', prms=['program', 'target', 'index', 'params'])
def glNamedProgramLocalParameterI4uivEXT(program, target, index, params):
	pass


@params(api='gl', prms=['program', 'target', 'index', 'count', 'params'])
def glNamedProgramLocalParametersI4uivEXT(program, target, index, count, params):
	pass


@params(api='gl', prms=['program', 'target', 'index', 'params'])
def glGetNamedProgramLocalParameterIivEXT(program, target, index, params):
	pass


@params(api='gl', prms=['program', 'target', 'index', 'params'])
def glGetNamedProgramLocalParameterIuivEXT(program, target, index, params):
	pass


@params(api='gl', prms=['array', 'index'])
def glEnableClientStateiEXT(array, index):
	pass


@params(api='gl', prms=['array', 'index'])
def glDisableClientStateiEXT(array, index):
	pass


@params(api='gl', prms=['pname', 'index', 'params'])
def glGetFloati_vEXT(pname, index, params):
	pass


@params(api='gl', prms=['pname', 'index', 'params'])
def glGetDoublei_vEXT(pname, index, params):
	pass


@params(api='gl', prms=['pname', 'index', 'params'])
def glGetPointeri_vEXT(pname, index, params):
	pass


@params(api='gl', prms=['program', 'target', 'format', 'len', 'string'])
def glNamedProgramStringEXT(program, target, format, len, string):
	pass


@params(api='gl', prms=['program', 'target', 'index', 'x', 'y', 'z', 'w'])
def glNamedProgramLocalParameter4dEXT(program, target, index, x, y, z, w):
	pass


@params(api='gl', prms=['program', 'target', 'index', 'params'])
def glNamedProgramLocalParameter4dvEXT(program, target, index, params):
	pass


@params(api='gl', prms=['program', 'target', 'index', 'x', 'y', 'z', 'w'])
def glNamedProgramLocalParameter4fEXT(program, target, index, x, y, z, w):
	pass


@params(api='gl', prms=['program', 'target', 'index', 'params'])
def glNamedProgramLocalParameter4fvEXT(program, target, index, params):
	pass


@params(api='gl', prms=['program', 'target', 'index', 'params'])
def glGetNamedProgramLocalParameterdvEXT(program, target, index, params):
	pass


@params(api='gl', prms=['program', 'target', 'index', 'params'])
def glGetNamedProgramLocalParameterfvEXT(program, target, index, params):
	pass


@params(api='gl', prms=['program', 'target', 'pname', 'params'])
def glGetNamedProgramivEXT(program, target, pname, params):
	pass


@params(api='gl', prms=['program', 'target', 'pname', 'string'])
def glGetNamedProgramStringEXT(program, target, pname, string):
	pass


@params(api='gl', prms=['renderbuffer', 'internalformat', 'width', 'height'])
def glNamedRenderbufferStorageEXT(renderbuffer, internalformat, width, height):
	pass


@params(api='gl', prms=['renderbuffer', 'pname', 'params'])
def glGetNamedRenderbufferParameterivEXT(renderbuffer, pname, params):
	pass


@params(api='gl', prms=['renderbuffer', 'samples', 'internalformat', 'width', 'height'])
def glNamedRenderbufferStorageMultisampleEXT(renderbuffer, samples, internalformat, width, height):
	pass


@params(api='gl', prms=['renderbuffer', 'coverageSamples', 'colorSamples', 'internalformat', 'width', 'height'])
def glNamedRenderbufferStorageMultisampleCoverageEXT(renderbuffer, coverageSamples, colorSamples, internalformat, width, height):
	pass


@params(api='gl', prms=['framebuffer', 'target'])
def glCheckNamedFramebufferStatusEXT(framebuffer, target):
	pass


@params(api='gl', prms=['framebuffer', 'attachment', 'textarget', 'texture', 'level'])
def glNamedFramebufferTexture1DEXT(framebuffer, attachment, textarget, texture, level):
	pass


@params(api='gl', prms=['framebuffer', 'attachment', 'textarget', 'texture', 'level'])
def glNamedFramebufferTexture2DEXT(framebuffer, attachment, textarget, texture, level):
	pass


@params(api='gl', prms=['framebuffer', 'attachment', 'textarget', 'texture', 'level', 'zoffset'])
def glNamedFramebufferTexture3DEXT(framebuffer, attachment, textarget, texture, level, zoffset):
	pass


@params(api='gl', prms=['framebuffer', 'attachment', 'renderbuffertarget', 'renderbuffer'])
def glNamedFramebufferRenderbufferEXT(framebuffer, attachment, renderbuffertarget, renderbuffer):
	pass


@params(api='gl', prms=['framebuffer', 'attachment', 'pname', 'params'])
def glGetNamedFramebufferAttachmentParameterivEXT(framebuffer, attachment, pname, params):
	pass


@params(api='gl', prms=['texture', 'target'])
def glGenerateTextureMipmapEXT(texture, target):
	pass


@params(api='gl', prms=['texunit', 'target'])
def glGenerateMultiTexMipmapEXT(texunit, target):
	pass


@params(api='gl', prms=['framebuffer', 'mode'])
def glFramebufferDrawBufferEXT(framebuffer, mode):
	pass


@params(api='gl', prms=['framebuffer', 'n', 'bufs'])
def glFramebufferDrawBuffersEXT(framebuffer, n, bufs):
	pass


@params(api='gl', prms=['framebuffer', 'mode'])
def glFramebufferReadBufferEXT(framebuffer, mode):
	pass


@params(api='gl', prms=['framebuffer', 'pname', 'params'])
def glGetFramebufferParameterivEXT(framebuffer, pname, params):
	pass


@params(api='gl', prms=['readBuffer', 'writeBuffer', 'readOffset', 'writeOffset', 'size'])
def glNamedCopyBufferSubDataEXT(readBuffer, writeBuffer, readOffset, writeOffset, size):
	pass


@params(api='gl', prms=['framebuffer', 'attachment', 'texture', 'level'])
def glNamedFramebufferTextureEXT(framebuffer, attachment, texture, level):
	pass


@params(api='gl', prms=['framebuffer', 'attachment', 'texture', 'level', 'layer'])
def glNamedFramebufferTextureLayerEXT(framebuffer, attachment, texture, level, layer):
	pass


@params(api='gl', prms=['framebuffer', 'attachment', 'texture', 'level', 'face'])
def glNamedFramebufferTextureFaceEXT(framebuffer, attachment, texture, level, face):
	pass


@params(api='gl', prms=['texture', 'target', 'renderbuffer'])
def glTextureRenderbufferEXT(texture, target, renderbuffer):
	pass


@params(api='gl', prms=['texunit', 'target', 'renderbuffer'])
def glMultiTexRenderbufferEXT(texunit, target, renderbuffer):
	pass


@params(api='gl', prms=['vaobj', 'buffer', 'size', 'type', 'stride', 'offset'])
def glVertexArrayVertexOffsetEXT(vaobj, buffer, size, type, stride, offset):
	pass


@params(api='gl', prms=['vaobj', 'buffer', 'size', 'type', 'stride', 'offset'])
def glVertexArrayColorOffsetEXT(vaobj, buffer, size, type, stride, offset):
	pass


@params(api='gl', prms=['vaobj', 'buffer', 'stride', 'offset'])
def glVertexArrayEdgeFlagOffsetEXT(vaobj, buffer, stride, offset):
	pass


@params(api='gl', prms=['vaobj', 'buffer', 'type', 'stride', 'offset'])
def glVertexArrayIndexOffsetEXT(vaobj, buffer, type, stride, offset):
	pass


@params(api='gl', prms=['vaobj', 'buffer', 'type', 'stride', 'offset'])
def glVertexArrayNormalOffsetEXT(vaobj, buffer, type, stride, offset):
	pass


@params(api='gl', prms=['vaobj', 'buffer', 'size', 'type', 'stride', 'offset'])
def glVertexArrayTexCoordOffsetEXT(vaobj, buffer, size, type, stride, offset):
	pass


@params(api='gl', prms=['vaobj', 'buffer', 'texunit', 'size', 'type', 'stride', 'offset'])
def glVertexArrayMultiTexCoordOffsetEXT(vaobj, buffer, texunit, size, type, stride, offset):
	pass


@params(api='gl', prms=['vaobj', 'buffer', 'type', 'stride', 'offset'])
def glVertexArrayFogCoordOffsetEXT(vaobj, buffer, type, stride, offset):
	pass


@params(api='gl', prms=['vaobj', 'buffer', 'size', 'type', 'stride', 'offset'])
def glVertexArraySecondaryColorOffsetEXT(vaobj, buffer, size, type, stride, offset):
	pass


@params(api='gl', prms=['vaobj', 'buffer', 'index', 'size', 'type', 'normalized', 'stride', 'offset'])
def glVertexArrayVertexAttribOffsetEXT(vaobj, buffer, index, size, type, normalized, stride, offset):
	pass


@params(api='gl', prms=['vaobj', 'buffer', 'index', 'size', 'type', 'stride', 'offset'])
def glVertexArrayVertexAttribIOffsetEXT(vaobj, buffer, index, size, type, stride, offset):
	pass


@params(api='gl', prms=['vaobj', 'array'])
def glEnableVertexArrayEXT(vaobj, array):
	pass


@params(api='gl', prms=['vaobj', 'array'])
def glDisableVertexArrayEXT(vaobj, array):
	pass


@params(api='gl', prms=['vaobj', 'index'])
def glEnableVertexArrayAttribEXT(vaobj, index):
	pass


@params(api='gl', prms=['vaobj', 'index'])
def glDisableVertexArrayAttribEXT(vaobj, index):
	pass


@params(api='gl', prms=['vaobj', 'pname', 'param'])
def glGetVertexArrayIntegervEXT(vaobj, pname, param):
	pass


@params(api='gl', prms=['vaobj', 'pname', 'param'])
def glGetVertexArrayPointervEXT(vaobj, pname, param):
	pass


@params(api='gl', prms=['vaobj', 'index', 'pname', 'param'])
def glGetVertexArrayIntegeri_vEXT(vaobj, index, pname, param):
	pass


@params(api='gl', prms=['vaobj', 'index', 'pname', 'param'])
def glGetVertexArrayPointeri_vEXT(vaobj, index, pname, param):
	pass


@params(api='gl', prms=['buffer', 'offset', 'length', 'access'])
def glMapNamedBufferRangeEXT(buffer, offset, length, access):
	pass


@params(api='gl', prms=['buffer', 'offset', 'length'])
def glFlushMappedNamedBufferRangeEXT(buffer, offset, length):
	pass


@params(api='gl', prms=['buffer', 'size', 'data', 'flags'])
def glNamedBufferStorageEXT(buffer, size, data, flags):
	pass


@params(api='gl', prms=['buffer', 'internalformat', 'format', 'type', 'data'])
def glClearNamedBufferDataEXT(buffer, internalformat, format, type, data):
	pass


@params(api='gl', prms=['buffer', 'internalformat', 'offset', 'size', 'format', 'type', 'data'])
def glClearNamedBufferSubDataEXT(buffer, internalformat, offset, size, format, type, data):
	pass


@params(api='gl', prms=['framebuffer', 'pname', 'param'])
def glNamedFramebufferParameteriEXT(framebuffer, pname, param):
	pass


@params(api='gl', prms=['framebuffer', 'pname', 'params'])
def glGetNamedFramebufferParameterivEXT(framebuffer, pname, params):
	pass


@params(api='gl', prms=['program', 'location', 'x'])
def glProgramUniform1dEXT(program, location, x):
	pass


@params(api='gl', prms=['program', 'location', 'x', 'y'])
def glProgramUniform2dEXT(program, location, x, y):
	pass


@params(api='gl', prms=['program', 'location', 'x', 'y', 'z'])
def glProgramUniform3dEXT(program, location, x, y, z):
	pass


@params(api='gl', prms=['program', 'location', 'x', 'y', 'z', 'w'])
def glProgramUniform4dEXT(program, location, x, y, z, w):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform1dvEXT(program, location, count, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform2dvEXT(program, location, count, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform3dvEXT(program, location, count, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniform4dvEXT(program, location, count, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix2dvEXT(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix3dvEXT(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix4dvEXT(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix2x3dvEXT(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix2x4dvEXT(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix3x2dvEXT(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix3x4dvEXT(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix4x2dvEXT(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'transpose', 'value'])
def glProgramUniformMatrix4x3dvEXT(program, location, count, transpose, value):
	pass


@params(api='gl', prms=['texture', 'target', 'internalformat', 'buffer', 'offset', 'size'])
def glTextureBufferRangeEXT(texture, target, internalformat, buffer, offset, size):
	pass


@params(api='gl', prms=['texture', 'target', 'levels', 'internalformat', 'width'])
def glTextureStorage1DEXT(texture, target, levels, internalformat, width):
	pass


@params(api='gl', prms=['texture', 'target', 'levels', 'internalformat', 'width', 'height'])
def glTextureStorage2DEXT(texture, target, levels, internalformat, width, height):
	pass


@params(api='gl', prms=['texture', 'target', 'levels', 'internalformat', 'width', 'height', 'depth'])
def glTextureStorage3DEXT(texture, target, levels, internalformat, width, height, depth):
	pass


@params(api='gl', prms=['texture', 'target', 'samples', 'internalformat', 'width', 'height', 'fixedsamplelocations'])
def glTextureStorage2DMultisampleEXT(texture, target, samples, internalformat, width, height, fixedsamplelocations):
	pass


@params(api='gl', prms=['texture', 'target', 'samples', 'internalformat', 'width', 'height', 'depth', 'fixedsamplelocations'])
def glTextureStorage3DMultisampleEXT(texture, target, samples, internalformat, width, height, depth, fixedsamplelocations):
	pass


@params(api='gl', prms=['vaobj', 'bindingindex', 'buffer', 'offset', 'stride'])
def glVertexArrayBindVertexBufferEXT(vaobj, bindingindex, buffer, offset, stride):
	pass


@params(api='gl', prms=['vaobj', 'attribindex', 'size', 'type', 'normalized', 'relativeoffset'])
def glVertexArrayVertexAttribFormatEXT(vaobj, attribindex, size, type, normalized, relativeoffset):
	pass


@params(api='gl', prms=['vaobj', 'attribindex', 'size', 'type', 'relativeoffset'])
def glVertexArrayVertexAttribIFormatEXT(vaobj, attribindex, size, type, relativeoffset):
	pass


@params(api='gl', prms=['vaobj', 'attribindex', 'size', 'type', 'relativeoffset'])
def glVertexArrayVertexAttribLFormatEXT(vaobj, attribindex, size, type, relativeoffset):
	pass


@params(api='gl', prms=['vaobj', 'attribindex', 'bindingindex'])
def glVertexArrayVertexAttribBindingEXT(vaobj, attribindex, bindingindex):
	pass


@params(api='gl', prms=['vaobj', 'bindingindex', 'divisor'])
def glVertexArrayVertexBindingDivisorEXT(vaobj, bindingindex, divisor):
	pass


@params(api='gl', prms=['vaobj', 'buffer', 'index', 'size', 'type', 'stride', 'offset'])
def glVertexArrayVertexAttribLOffsetEXT(vaobj, buffer, index, size, type, stride, offset):
	pass


@params(api='gl', prms=['texture', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth', 'commit'])
def glTexturePageCommitmentEXT(texture, level, xoffset, yoffset, zoffset, width, height, depth, commit):
	pass


@params(api='gl', prms=['vaobj', 'index', 'divisor'])
def glVertexArrayVertexAttribDivisorEXT(vaobj, index, divisor):
	pass


