from OpenGLCffi.GL import params
@params('mode', 'm', api='gl')
def glMatrixLoadfEXT(mode, m):
	pass


@params('mode', 'm', api='gl')
def glMatrixLoaddEXT(mode, m):
	pass


@params('mode', 'm', api='gl')
def glMatrixMultfEXT(mode, m):
	pass


@params('mode', 'm', api='gl')
def glMatrixMultdEXT(mode, m):
	pass


@params('mode', api='gl')
def glMatrixLoadIdentityEXT(mode):
	pass


@params('mode', 'angle', 'x', 'y', 'z', api='gl')
def glMatrixRotatefEXT(mode, angle, x, y, z):
	pass


@params('mode', 'angle', 'x', 'y', 'z', api='gl')
def glMatrixRotatedEXT(mode, angle, x, y, z):
	pass


@params('mode', 'x', 'y', 'z', api='gl')
def glMatrixScalefEXT(mode, x, y, z):
	pass


@params('mode', 'x', 'y', 'z', api='gl')
def glMatrixScaledEXT(mode, x, y, z):
	pass


@params('mode', 'x', 'y', 'z', api='gl')
def glMatrixTranslatefEXT(mode, x, y, z):
	pass


@params('mode', 'x', 'y', 'z', api='gl')
def glMatrixTranslatedEXT(mode, x, y, z):
	pass


@params('mode', 'left', 'right', 'bottom', 'top', 'zNear', 'zFar', api='gl')
def glMatrixFrustumEXT(mode, left, right, bottom, top, zNear, zFar):
	pass


@params('mode', 'left', 'right', 'bottom', 'top', 'zNear', 'zFar', api='gl')
def glMatrixOrthoEXT(mode, left, right, bottom, top, zNear, zFar):
	pass


@params('mode', api='gl')
def glMatrixPopEXT(mode):
	pass


@params('mode', api='gl')
def glMatrixPushEXT(mode):
	pass


@params('mask', api='gl')
def glClientAttribDefaultEXT(mask):
	pass


@params('mask', api='gl')
def glPushClientAttribDefaultEXT(mask):
	pass


@params('texture', 'target', 'pname', 'param', api='gl')
def glTextureParameterfEXT(texture, target, pname, param):
	pass


@params('texture', 'target', 'pname', 'params', api='gl')
def glTextureParameterfvEXT(texture, target, pname, params):
	pass


@params('texture', 'target', 'pname', 'param', api='gl')
def glTextureParameteriEXT(texture, target, pname, param):
	pass


@params('texture', 'target', 'pname', 'params', api='gl')
def glTextureParameterivEXT(texture, target, pname, params):
	pass


@params('texture', 'target', 'level', 'internalformat', 'width', 'border', 'format', 'type', 'pixels', api='gl')
def glTextureImage1DEXT(texture, target, level, internalformat, width, border, format, type, pixels):
	pass


@params('texture', 'target', 'level', 'internalformat', 'width', 'height', 'border', 'format', 'type', 'pixels', api='gl')
def glTextureImage2DEXT(texture, target, level, internalformat, width, height, border, format, type, pixels):
	pass


@params('texture', 'target', 'level', 'xoffset', 'width', 'format', 'type', 'pixels', api='gl')
def glTextureSubImage1DEXT(texture, target, level, xoffset, width, format, type, pixels):
	pass


@params('texture', 'target', 'level', 'xoffset', 'yoffset', 'width', 'height', 'format', 'type', 'pixels', api='gl')
def glTextureSubImage2DEXT(texture, target, level, xoffset, yoffset, width, height, format, type, pixels):
	pass


@params('texture', 'target', 'level', 'internalformat', 'x', 'y', 'width', 'border', api='gl')
def glCopyTextureImage1DEXT(texture, target, level, internalformat, x, y, width, border):
	pass


@params('texture', 'target', 'level', 'internalformat', 'x', 'y', 'width', 'height', 'border', api='gl')
def glCopyTextureImage2DEXT(texture, target, level, internalformat, x, y, width, height, border):
	pass


@params('texture', 'target', 'level', 'xoffset', 'x', 'y', 'width', api='gl')
def glCopyTextureSubImage1DEXT(texture, target, level, xoffset, x, y, width):
	pass


@params('texture', 'target', 'level', 'xoffset', 'yoffset', 'x', 'y', 'width', 'height', api='gl')
def glCopyTextureSubImage2DEXT(texture, target, level, xoffset, yoffset, x, y, width, height):
	pass


@params('texture', 'target', 'level', 'format', 'type', 'pixels', api='gl')
def glGetTextureImageEXT(texture, target, level, format, type, pixels):
	pass


@params('texture', 'target', 'pname', 'params', api='gl')
def glGetTextureParameterfvEXT(texture, target, pname, params):
	pass


@params('texture', 'target', 'pname', 'params', api='gl')
def glGetTextureParameterivEXT(texture, target, pname, params):
	pass


@params('texture', 'target', 'level', 'pname', 'params', api='gl')
def glGetTextureLevelParameterfvEXT(texture, target, level, pname, params):
	pass


@params('texture', 'target', 'level', 'pname', 'params', api='gl')
def glGetTextureLevelParameterivEXT(texture, target, level, pname, params):
	pass


@params('texture', 'target', 'level', 'internalformat', 'width', 'height', 'depth', 'border', 'format', 'type', 'pixels', api='gl')
def glTextureImage3DEXT(texture, target, level, internalformat, width, height, depth, border, format, type, pixels):
	pass


@params('texture', 'target', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth', 'format', 'type', 'pixels', api='gl')
def glTextureSubImage3DEXT(texture, target, level, xoffset, yoffset, zoffset, width, height, depth, format, type, pixels):
	pass


@params('texture', 'target', 'level', 'xoffset', 'yoffset', 'zoffset', 'x', 'y', 'width', 'height', api='gl')
def glCopyTextureSubImage3DEXT(texture, target, level, xoffset, yoffset, zoffset, x, y, width, height):
	pass


@params('texunit', 'target', 'texture', api='gl')
def glBindMultiTextureEXT(texunit, target, texture):
	pass


@params('texunit', 'size', 'type', 'stride', 'pointer', api='gl')
def glMultiTexCoordPointerEXT(texunit, size, type, stride, pointer):
	pass


@params('texunit', 'target', 'pname', 'param', api='gl')
def glMultiTexEnvfEXT(texunit, target, pname, param):
	pass


@params('texunit', 'target', 'pname', 'params', api='gl')
def glMultiTexEnvfvEXT(texunit, target, pname, params):
	pass


@params('texunit', 'target', 'pname', 'param', api='gl')
def glMultiTexEnviEXT(texunit, target, pname, param):
	pass


@params('texunit', 'target', 'pname', 'params', api='gl')
def glMultiTexEnvivEXT(texunit, target, pname, params):
	pass


@params('texunit', 'coord', 'pname', 'param', api='gl')
def glMultiTexGendEXT(texunit, coord, pname, param):
	pass


@params('texunit', 'coord', 'pname', 'params', api='gl')
def glMultiTexGendvEXT(texunit, coord, pname, params):
	pass


@params('texunit', 'coord', 'pname', 'param', api='gl')
def glMultiTexGenfEXT(texunit, coord, pname, param):
	pass


@params('texunit', 'coord', 'pname', 'params', api='gl')
def glMultiTexGenfvEXT(texunit, coord, pname, params):
	pass


@params('texunit', 'coord', 'pname', 'param', api='gl')
def glMultiTexGeniEXT(texunit, coord, pname, param):
	pass


@params('texunit', 'coord', 'pname', 'params', api='gl')
def glMultiTexGenivEXT(texunit, coord, pname, params):
	pass


@params('texunit', 'target', 'pname', 'params', api='gl')
def glGetMultiTexEnvfvEXT(texunit, target, pname, params):
	pass


@params('texunit', 'target', 'pname', 'params', api='gl')
def glGetMultiTexEnvivEXT(texunit, target, pname, params):
	pass


@params('texunit', 'coord', 'pname', 'params', api='gl')
def glGetMultiTexGendvEXT(texunit, coord, pname, params):
	pass


@params('texunit', 'coord', 'pname', 'params', api='gl')
def glGetMultiTexGenfvEXT(texunit, coord, pname, params):
	pass


@params('texunit', 'coord', 'pname', 'params', api='gl')
def glGetMultiTexGenivEXT(texunit, coord, pname, params):
	pass


@params('texunit', 'target', 'pname', 'param', api='gl')
def glMultiTexParameteriEXT(texunit, target, pname, param):
	pass


@params('texunit', 'target', 'pname', 'params', api='gl')
def glMultiTexParameterivEXT(texunit, target, pname, params):
	pass


@params('texunit', 'target', 'pname', 'param', api='gl')
def glMultiTexParameterfEXT(texunit, target, pname, param):
	pass


@params('texunit', 'target', 'pname', 'params', api='gl')
def glMultiTexParameterfvEXT(texunit, target, pname, params):
	pass


@params('texunit', 'target', 'level', 'internalformat', 'width', 'border', 'format', 'type', 'pixels', api='gl')
def glMultiTexImage1DEXT(texunit, target, level, internalformat, width, border, format, type, pixels):
	pass


@params('texunit', 'target', 'level', 'internalformat', 'width', 'height', 'border', 'format', 'type', 'pixels', api='gl')
def glMultiTexImage2DEXT(texunit, target, level, internalformat, width, height, border, format, type, pixels):
	pass


@params('texunit', 'target', 'level', 'xoffset', 'width', 'format', 'type', 'pixels', api='gl')
def glMultiTexSubImage1DEXT(texunit, target, level, xoffset, width, format, type, pixels):
	pass


@params('texunit', 'target', 'level', 'xoffset', 'yoffset', 'width', 'height', 'format', 'type', 'pixels', api='gl')
def glMultiTexSubImage2DEXT(texunit, target, level, xoffset, yoffset, width, height, format, type, pixels):
	pass


@params('texunit', 'target', 'level', 'internalformat', 'x', 'y', 'width', 'border', api='gl')
def glCopyMultiTexImage1DEXT(texunit, target, level, internalformat, x, y, width, border):
	pass


@params('texunit', 'target', 'level', 'internalformat', 'x', 'y', 'width', 'height', 'border', api='gl')
def glCopyMultiTexImage2DEXT(texunit, target, level, internalformat, x, y, width, height, border):
	pass


@params('texunit', 'target', 'level', 'xoffset', 'x', 'y', 'width', api='gl')
def glCopyMultiTexSubImage1DEXT(texunit, target, level, xoffset, x, y, width):
	pass


@params('texunit', 'target', 'level', 'xoffset', 'yoffset', 'x', 'y', 'width', 'height', api='gl')
def glCopyMultiTexSubImage2DEXT(texunit, target, level, xoffset, yoffset, x, y, width, height):
	pass


@params('texunit', 'target', 'level', 'format', 'type', 'pixels', api='gl')
def glGetMultiTexImageEXT(texunit, target, level, format, type, pixels):
	pass


@params('texunit', 'target', 'pname', 'params', api='gl')
def glGetMultiTexParameterfvEXT(texunit, target, pname, params):
	pass


@params('texunit', 'target', 'pname', 'params', api='gl')
def glGetMultiTexParameterivEXT(texunit, target, pname, params):
	pass


@params('texunit', 'target', 'level', 'pname', 'params', api='gl')
def glGetMultiTexLevelParameterfvEXT(texunit, target, level, pname, params):
	pass


@params('texunit', 'target', 'level', 'pname', 'params', api='gl')
def glGetMultiTexLevelParameterivEXT(texunit, target, level, pname, params):
	pass


@params('texunit', 'target', 'level', 'internalformat', 'width', 'height', 'depth', 'border', 'format', 'type', 'pixels', api='gl')
def glMultiTexImage3DEXT(texunit, target, level, internalformat, width, height, depth, border, format, type, pixels):
	pass


@params('texunit', 'target', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth', 'format', 'type', 'pixels', api='gl')
def glMultiTexSubImage3DEXT(texunit, target, level, xoffset, yoffset, zoffset, width, height, depth, format, type, pixels):
	pass


@params('texunit', 'target', 'level', 'xoffset', 'yoffset', 'zoffset', 'x', 'y', 'width', 'height', api='gl')
def glCopyMultiTexSubImage3DEXT(texunit, target, level, xoffset, yoffset, zoffset, x, y, width, height):
	pass


@params('array', 'index', api='gl')
def glEnableClientStateIndexedEXT(array, index):
	pass


@params('array', 'index', api='gl')
def glDisableClientStateIndexedEXT(array, index):
	pass


@params('target', 'index', 'data', api='gl')
def glGetFloatIndexedvEXT(target, index, data):
	pass


@params('target', 'index', 'data', api='gl')
def glGetDoubleIndexedvEXT(target, index, data):
	pass


@params('target', 'index', 'data', api='gl')
def glGetPointerIndexedvEXT(target, index, data):
	pass


@params('target', 'index', api='gl')
def glEnableIndexedEXT(target, index):
	pass


@params('target', 'index', api='gl')
def glDisableIndexedEXT(target, index):
	pass


@params('target', 'index', api='gl')
def glIsEnabledIndexedEXT(target, index):
	pass


@params('target', 'index', 'data', api='gl')
def glGetIntegerIndexedvEXT(target, index, data):
	pass


@params('target', 'index', 'data', api='gl')
def glGetBooleanIndexedvEXT(target, index, data):
	pass


@params('texture', 'target', 'level', 'internalformat', 'width', 'height', 'depth', 'border', 'imageSize', 'bits', api='gl')
def glCompressedTextureImage3DEXT(texture, target, level, internalformat, width, height, depth, border, imageSize, bits):
	pass


@params('texture', 'target', 'level', 'internalformat', 'width', 'height', 'border', 'imageSize', 'bits', api='gl')
def glCompressedTextureImage2DEXT(texture, target, level, internalformat, width, height, border, imageSize, bits):
	pass


@params('texture', 'target', 'level', 'internalformat', 'width', 'border', 'imageSize', 'bits', api='gl')
def glCompressedTextureImage1DEXT(texture, target, level, internalformat, width, border, imageSize, bits):
	pass


@params('texture', 'target', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth', 'format', 'imageSize', 'bits', api='gl')
def glCompressedTextureSubImage3DEXT(texture, target, level, xoffset, yoffset, zoffset, width, height, depth, format, imageSize, bits):
	pass


@params('texture', 'target', 'level', 'xoffset', 'yoffset', 'width', 'height', 'format', 'imageSize', 'bits', api='gl')
def glCompressedTextureSubImage2DEXT(texture, target, level, xoffset, yoffset, width, height, format, imageSize, bits):
	pass


@params('texture', 'target', 'level', 'xoffset', 'width', 'format', 'imageSize', 'bits', api='gl')
def glCompressedTextureSubImage1DEXT(texture, target, level, xoffset, width, format, imageSize, bits):
	pass


@params('texture', 'target', 'lod', 'img', api='gl')
def glGetCompressedTextureImageEXT(texture, target, lod, img):
	pass


@params('texunit', 'target', 'level', 'internalformat', 'width', 'height', 'depth', 'border', 'imageSize', 'bits', api='gl')
def glCompressedMultiTexImage3DEXT(texunit, target, level, internalformat, width, height, depth, border, imageSize, bits):
	pass


@params('texunit', 'target', 'level', 'internalformat', 'width', 'height', 'border', 'imageSize', 'bits', api='gl')
def glCompressedMultiTexImage2DEXT(texunit, target, level, internalformat, width, height, border, imageSize, bits):
	pass


@params('texunit', 'target', 'level', 'internalformat', 'width', 'border', 'imageSize', 'bits', api='gl')
def glCompressedMultiTexImage1DEXT(texunit, target, level, internalformat, width, border, imageSize, bits):
	pass


@params('texunit', 'target', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth', 'format', 'imageSize', 'bits', api='gl')
def glCompressedMultiTexSubImage3DEXT(texunit, target, level, xoffset, yoffset, zoffset, width, height, depth, format, imageSize, bits):
	pass


@params('texunit', 'target', 'level', 'xoffset', 'yoffset', 'width', 'height', 'format', 'imageSize', 'bits', api='gl')
def glCompressedMultiTexSubImage2DEXT(texunit, target, level, xoffset, yoffset, width, height, format, imageSize, bits):
	pass


@params('texunit', 'target', 'level', 'xoffset', 'width', 'format', 'imageSize', 'bits', api='gl')
def glCompressedMultiTexSubImage1DEXT(texunit, target, level, xoffset, width, format, imageSize, bits):
	pass


@params('texunit', 'target', 'lod', 'img', api='gl')
def glGetCompressedMultiTexImageEXT(texunit, target, lod, img):
	pass


@params('mode', 'm', api='gl')
def glMatrixLoadTransposefEXT(mode, m):
	pass


@params('mode', 'm', api='gl')
def glMatrixLoadTransposedEXT(mode, m):
	pass


@params('mode', 'm', api='gl')
def glMatrixMultTransposefEXT(mode, m):
	pass


@params('mode', 'm', api='gl')
def glMatrixMultTransposedEXT(mode, m):
	pass


@params('buffer', 'size', 'data', 'usage', api='gl')
def glNamedBufferDataEXT(buffer, size, data, usage):
	pass


@params('buffer', 'offset', 'size', 'data', api='gl')
def glNamedBufferSubDataEXT(buffer, offset, size, data):
	pass


@params('buffer', 'access', api='gl')
def glMapNamedBufferEXT(buffer, access):
	pass


@params('buffer', api='gl')
def glUnmapNamedBufferEXT(buffer):
	pass


@params('buffer', 'pname', 'params', api='gl')
def glGetNamedBufferParameterivEXT(buffer, pname, params):
	pass


@params('buffer', 'pname', 'params', api='gl')
def glGetNamedBufferPointervEXT(buffer, pname, params):
	pass


@params('buffer', 'offset', 'size', 'data', api='gl')
def glGetNamedBufferSubDataEXT(buffer, offset, size, data):
	pass


@params('program', 'location', 'v0', api='gl')
def glProgramUniform1fEXT(program, location, v0):
	pass


@params('program', 'location', 'v0', 'v1', api='gl')
def glProgramUniform2fEXT(program, location, v0, v1):
	pass


@params('program', 'location', 'v0', 'v1', 'v2', api='gl')
def glProgramUniform3fEXT(program, location, v0, v1, v2):
	pass


@params('program', 'location', 'v0', 'v1', 'v2', 'v3', api='gl')
def glProgramUniform4fEXT(program, location, v0, v1, v2, v3):
	pass


@params('program', 'location', 'v0', api='gl')
def glProgramUniform1iEXT(program, location, v0):
	pass


@params('program', 'location', 'v0', 'v1', api='gl')
def glProgramUniform2iEXT(program, location, v0, v1):
	pass


@params('program', 'location', 'v0', 'v1', 'v2', api='gl')
def glProgramUniform3iEXT(program, location, v0, v1, v2):
	pass


@params('program', 'location', 'v0', 'v1', 'v2', 'v3', api='gl')
def glProgramUniform4iEXT(program, location, v0, v1, v2, v3):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform1fvEXT(program, location, count, value):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform2fvEXT(program, location, count, value):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform3fvEXT(program, location, count, value):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform4fvEXT(program, location, count, value):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform1ivEXT(program, location, count, value):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform2ivEXT(program, location, count, value):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform3ivEXT(program, location, count, value):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform4ivEXT(program, location, count, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix2fvEXT(program, location, count, transpose, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix3fvEXT(program, location, count, transpose, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix4fvEXT(program, location, count, transpose, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix2x3fvEXT(program, location, count, transpose, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix3x2fvEXT(program, location, count, transpose, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix2x4fvEXT(program, location, count, transpose, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix4x2fvEXT(program, location, count, transpose, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix3x4fvEXT(program, location, count, transpose, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix4x3fvEXT(program, location, count, transpose, value):
	pass


@params('texture', 'target', 'internalformat', 'buffer', api='gl')
def glTextureBufferEXT(texture, target, internalformat, buffer):
	pass


@params('texunit', 'target', 'internalformat', 'buffer', api='gl')
def glMultiTexBufferEXT(texunit, target, internalformat, buffer):
	pass


@params('texture', 'target', 'pname', 'params', api='gl')
def glTextureParameterIivEXT(texture, target, pname, params):
	pass


@params('texture', 'target', 'pname', 'params', api='gl')
def glTextureParameterIuivEXT(texture, target, pname, params):
	pass


@params('texture', 'target', 'pname', 'params', api='gl')
def glGetTextureParameterIivEXT(texture, target, pname, params):
	pass


@params('texture', 'target', 'pname', 'params', api='gl')
def glGetTextureParameterIuivEXT(texture, target, pname, params):
	pass


@params('texunit', 'target', 'pname', 'params', api='gl')
def glMultiTexParameterIivEXT(texunit, target, pname, params):
	pass


@params('texunit', 'target', 'pname', 'params', api='gl')
def glMultiTexParameterIuivEXT(texunit, target, pname, params):
	pass


@params('texunit', 'target', 'pname', 'params', api='gl')
def glGetMultiTexParameterIivEXT(texunit, target, pname, params):
	pass


@params('texunit', 'target', 'pname', 'params', api='gl')
def glGetMultiTexParameterIuivEXT(texunit, target, pname, params):
	pass


@params('program', 'location', 'v0', api='gl')
def glProgramUniform1uiEXT(program, location, v0):
	pass


@params('program', 'location', 'v0', 'v1', api='gl')
def glProgramUniform2uiEXT(program, location, v0, v1):
	pass


@params('program', 'location', 'v0', 'v1', 'v2', api='gl')
def glProgramUniform3uiEXT(program, location, v0, v1, v2):
	pass


@params('program', 'location', 'v0', 'v1', 'v2', 'v3', api='gl')
def glProgramUniform4uiEXT(program, location, v0, v1, v2, v3):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform1uivEXT(program, location, count, value):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform2uivEXT(program, location, count, value):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform3uivEXT(program, location, count, value):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform4uivEXT(program, location, count, value):
	pass


@params('program', 'target', 'index', 'count', 'params', api='gl')
def glNamedProgramLocalParameters4fvEXT(program, target, index, count, params):
	pass


@params('program', 'target', 'index', 'x', 'y', 'z', 'w', api='gl')
def glNamedProgramLocalParameterI4iEXT(program, target, index, x, y, z, w):
	pass


@params('program', 'target', 'index', 'params', api='gl')
def glNamedProgramLocalParameterI4ivEXT(program, target, index, params):
	pass


@params('program', 'target', 'index', 'count', 'params', api='gl')
def glNamedProgramLocalParametersI4ivEXT(program, target, index, count, params):
	pass


@params('program', 'target', 'index', 'x', 'y', 'z', 'w', api='gl')
def glNamedProgramLocalParameterI4uiEXT(program, target, index, x, y, z, w):
	pass


@params('program', 'target', 'index', 'params', api='gl')
def glNamedProgramLocalParameterI4uivEXT(program, target, index, params):
	pass


@params('program', 'target', 'index', 'count', 'params', api='gl')
def glNamedProgramLocalParametersI4uivEXT(program, target, index, count, params):
	pass


@params('program', 'target', 'index', 'params', api='gl')
def glGetNamedProgramLocalParameterIivEXT(program, target, index, params):
	pass


@params('program', 'target', 'index', 'params', api='gl')
def glGetNamedProgramLocalParameterIuivEXT(program, target, index, params):
	pass


@params('array', 'index', api='gl')
def glEnableClientStateiEXT(array, index):
	pass


@params('array', 'index', api='gl')
def glDisableClientStateiEXT(array, index):
	pass


@params('pname', 'index', 'params', api='gl')
def glGetFloati_vEXT(pname, index, params):
	pass


@params('pname', 'index', 'params', api='gl')
def glGetDoublei_vEXT(pname, index, params):
	pass


@params('pname', 'index', 'params', api='gl')
def glGetPointeri_vEXT(pname, index, params):
	pass


@params('program', 'target', 'format', 'len', 'string', api='gl')
def glNamedProgramStringEXT(program, target, format, len, string):
	pass


@params('program', 'target', 'index', 'x', 'y', 'z', 'w', api='gl')
def glNamedProgramLocalParameter4dEXT(program, target, index, x, y, z, w):
	pass


@params('program', 'target', 'index', 'params', api='gl')
def glNamedProgramLocalParameter4dvEXT(program, target, index, params):
	pass


@params('program', 'target', 'index', 'x', 'y', 'z', 'w', api='gl')
def glNamedProgramLocalParameter4fEXT(program, target, index, x, y, z, w):
	pass


@params('program', 'target', 'index', 'params', api='gl')
def glNamedProgramLocalParameter4fvEXT(program, target, index, params):
	pass


@params('program', 'target', 'index', 'params', api='gl')
def glGetNamedProgramLocalParameterdvEXT(program, target, index, params):
	pass


@params('program', 'target', 'index', 'params', api='gl')
def glGetNamedProgramLocalParameterfvEXT(program, target, index, params):
	pass


@params('program', 'target', 'pname', 'params', api='gl')
def glGetNamedProgramivEXT(program, target, pname, params):
	pass


@params('program', 'target', 'pname', 'string', api='gl')
def glGetNamedProgramStringEXT(program, target, pname, string):
	pass


@params('renderbuffer', 'internalformat', 'width', 'height', api='gl')
def glNamedRenderbufferStorageEXT(renderbuffer, internalformat, width, height):
	pass


@params('renderbuffer', 'pname', 'params', api='gl')
def glGetNamedRenderbufferParameterivEXT(renderbuffer, pname, params):
	pass


@params('renderbuffer', 'samples', 'internalformat', 'width', 'height', api='gl')
def glNamedRenderbufferStorageMultisampleEXT(renderbuffer, samples, internalformat, width, height):
	pass


@params('renderbuffer', 'coverageSamples', 'colorSamples', 'internalformat', 'width', 'height', api='gl')
def glNamedRenderbufferStorageMultisampleCoverageEXT(renderbuffer, coverageSamples, colorSamples, internalformat, width, height):
	pass


@params('framebuffer', 'target', api='gl')
def glCheckNamedFramebufferStatusEXT(framebuffer, target):
	pass


@params('framebuffer', 'attachment', 'textarget', 'texture', 'level', api='gl')
def glNamedFramebufferTexture1DEXT(framebuffer, attachment, textarget, texture, level):
	pass


@params('framebuffer', 'attachment', 'textarget', 'texture', 'level', api='gl')
def glNamedFramebufferTexture2DEXT(framebuffer, attachment, textarget, texture, level):
	pass


@params('framebuffer', 'attachment', 'textarget', 'texture', 'level', 'zoffset', api='gl')
def glNamedFramebufferTexture3DEXT(framebuffer, attachment, textarget, texture, level, zoffset):
	pass


@params('framebuffer', 'attachment', 'renderbuffertarget', 'renderbuffer', api='gl')
def glNamedFramebufferRenderbufferEXT(framebuffer, attachment, renderbuffertarget, renderbuffer):
	pass


@params('framebuffer', 'attachment', 'pname', 'params', api='gl')
def glGetNamedFramebufferAttachmentParameterivEXT(framebuffer, attachment, pname, params):
	pass


@params('texture', 'target', api='gl')
def glGenerateTextureMipmapEXT(texture, target):
	pass


@params('texunit', 'target', api='gl')
def glGenerateMultiTexMipmapEXT(texunit, target):
	pass


@params('framebuffer', 'mode', api='gl')
def glFramebufferDrawBufferEXT(framebuffer, mode):
	pass


@params('framebuffer', 'n', 'bufs', api='gl')
def glFramebufferDrawBuffersEXT(framebuffer, n, bufs):
	pass


@params('framebuffer', 'mode', api='gl')
def glFramebufferReadBufferEXT(framebuffer, mode):
	pass


@params('framebuffer', 'pname', 'params', api='gl')
def glGetFramebufferParameterivEXT(framebuffer, pname, params):
	pass


@params('readBuffer', 'writeBuffer', 'readOffset', 'writeOffset', 'size', api='gl')
def glNamedCopyBufferSubDataEXT(readBuffer, writeBuffer, readOffset, writeOffset, size):
	pass


@params('framebuffer', 'attachment', 'texture', 'level', api='gl')
def glNamedFramebufferTextureEXT(framebuffer, attachment, texture, level):
	pass


@params('framebuffer', 'attachment', 'texture', 'level', 'layer', api='gl')
def glNamedFramebufferTextureLayerEXT(framebuffer, attachment, texture, level, layer):
	pass


@params('framebuffer', 'attachment', 'texture', 'level', 'face', api='gl')
def glNamedFramebufferTextureFaceEXT(framebuffer, attachment, texture, level, face):
	pass


@params('texture', 'target', 'renderbuffer', api='gl')
def glTextureRenderbufferEXT(texture, target, renderbuffer):
	pass


@params('texunit', 'target', 'renderbuffer', api='gl')
def glMultiTexRenderbufferEXT(texunit, target, renderbuffer):
	pass


@params('vaobj', 'buffer', 'size', 'type', 'stride', 'offset', api='gl')
def glVertexArrayVertexOffsetEXT(vaobj, buffer, size, type, stride, offset):
	pass


@params('vaobj', 'buffer', 'size', 'type', 'stride', 'offset', api='gl')
def glVertexArrayColorOffsetEXT(vaobj, buffer, size, type, stride, offset):
	pass


@params('vaobj', 'buffer', 'stride', 'offset', api='gl')
def glVertexArrayEdgeFlagOffsetEXT(vaobj, buffer, stride, offset):
	pass


@params('vaobj', 'buffer', 'type', 'stride', 'offset', api='gl')
def glVertexArrayIndexOffsetEXT(vaobj, buffer, type, stride, offset):
	pass


@params('vaobj', 'buffer', 'type', 'stride', 'offset', api='gl')
def glVertexArrayNormalOffsetEXT(vaobj, buffer, type, stride, offset):
	pass


@params('vaobj', 'buffer', 'size', 'type', 'stride', 'offset', api='gl')
def glVertexArrayTexCoordOffsetEXT(vaobj, buffer, size, type, stride, offset):
	pass


@params('vaobj', 'buffer', 'texunit', 'size', 'type', 'stride', 'offset', api='gl')
def glVertexArrayMultiTexCoordOffsetEXT(vaobj, buffer, texunit, size, type, stride, offset):
	pass


@params('vaobj', 'buffer', 'type', 'stride', 'offset', api='gl')
def glVertexArrayFogCoordOffsetEXT(vaobj, buffer, type, stride, offset):
	pass


@params('vaobj', 'buffer', 'size', 'type', 'stride', 'offset', api='gl')
def glVertexArraySecondaryColorOffsetEXT(vaobj, buffer, size, type, stride, offset):
	pass


@params('vaobj', 'buffer', 'index', 'size', 'type', 'normalized', 'stride', 'offset', api='gl')
def glVertexArrayVertexAttribOffsetEXT(vaobj, buffer, index, size, type, normalized, stride, offset):
	pass


@params('vaobj', 'buffer', 'index', 'size', 'type', 'stride', 'offset', api='gl')
def glVertexArrayVertexAttribIOffsetEXT(vaobj, buffer, index, size, type, stride, offset):
	pass


@params('vaobj', 'array', api='gl')
def glEnableVertexArrayEXT(vaobj, array):
	pass


@params('vaobj', 'array', api='gl')
def glDisableVertexArrayEXT(vaobj, array):
	pass


@params('vaobj', 'index', api='gl')
def glEnableVertexArrayAttribEXT(vaobj, index):
	pass


@params('vaobj', 'index', api='gl')
def glDisableVertexArrayAttribEXT(vaobj, index):
	pass


@params('vaobj', 'pname', 'param', api='gl')
def glGetVertexArrayIntegervEXT(vaobj, pname, param):
	pass


@params('vaobj', 'pname', 'param', api='gl')
def glGetVertexArrayPointervEXT(vaobj, pname, param):
	pass


@params('vaobj', 'index', 'pname', 'param', api='gl')
def glGetVertexArrayIntegeri_vEXT(vaobj, index, pname, param):
	pass


@params('vaobj', 'index', 'pname', 'param', api='gl')
def glGetVertexArrayPointeri_vEXT(vaobj, index, pname, param):
	pass


@params('buffer', 'offset', 'length', 'access', api='gl')
def glMapNamedBufferRangeEXT(buffer, offset, length, access):
	pass


@params('buffer', 'offset', 'length', api='gl')
def glFlushMappedNamedBufferRangeEXT(buffer, offset, length):
	pass


@params('buffer', 'size', 'data', 'flags', api='gl')
def glNamedBufferStorageEXT(buffer, size, data, flags):
	pass


@params('buffer', 'internalformat', 'format', 'type', 'data', api='gl')
def glClearNamedBufferDataEXT(buffer, internalformat, format, type, data):
	pass


@params('buffer', 'internalformat', 'offset', 'size', 'format', 'type', 'data', api='gl')
def glClearNamedBufferSubDataEXT(buffer, internalformat, offset, size, format, type, data):
	pass


@params('framebuffer', 'pname', 'param', api='gl')
def glNamedFramebufferParameteriEXT(framebuffer, pname, param):
	pass


@params('framebuffer', 'pname', 'params', api='gl')
def glGetNamedFramebufferParameterivEXT(framebuffer, pname, params):
	pass


@params('program', 'location', 'x', api='gl')
def glProgramUniform1dEXT(program, location, x):
	pass


@params('program', 'location', 'x', 'y', api='gl')
def glProgramUniform2dEXT(program, location, x, y):
	pass


@params('program', 'location', 'x', 'y', 'z', api='gl')
def glProgramUniform3dEXT(program, location, x, y, z):
	pass


@params('program', 'location', 'x', 'y', 'z', 'w', api='gl')
def glProgramUniform4dEXT(program, location, x, y, z, w):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform1dvEXT(program, location, count, value):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform2dvEXT(program, location, count, value):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform3dvEXT(program, location, count, value):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniform4dvEXT(program, location, count, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix2dvEXT(program, location, count, transpose, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix3dvEXT(program, location, count, transpose, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix4dvEXT(program, location, count, transpose, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix2x3dvEXT(program, location, count, transpose, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix2x4dvEXT(program, location, count, transpose, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix3x2dvEXT(program, location, count, transpose, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix3x4dvEXT(program, location, count, transpose, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix4x2dvEXT(program, location, count, transpose, value):
	pass


@params('program', 'location', 'count', 'transpose', 'value', api='gl')
def glProgramUniformMatrix4x3dvEXT(program, location, count, transpose, value):
	pass


@params('texture', 'target', 'internalformat', 'buffer', 'offset', 'size', api='gl')
def glTextureBufferRangeEXT(texture, target, internalformat, buffer, offset, size):
	pass


@params('texture', 'target', 'levels', 'internalformat', 'width', api='gl')
def glTextureStorage1DEXT(texture, target, levels, internalformat, width):
	pass


@params('texture', 'target', 'levels', 'internalformat', 'width', 'height', api='gl')
def glTextureStorage2DEXT(texture, target, levels, internalformat, width, height):
	pass


@params('texture', 'target', 'levels', 'internalformat', 'width', 'height', 'depth', api='gl')
def glTextureStorage3DEXT(texture, target, levels, internalformat, width, height, depth):
	pass


@params('texture', 'target', 'samples', 'internalformat', 'width', 'height', 'fixedsamplelocations', api='gl')
def glTextureStorage2DMultisampleEXT(texture, target, samples, internalformat, width, height, fixedsamplelocations):
	pass


@params('texture', 'target', 'samples', 'internalformat', 'width', 'height', 'depth', 'fixedsamplelocations', api='gl')
def glTextureStorage3DMultisampleEXT(texture, target, samples, internalformat, width, height, depth, fixedsamplelocations):
	pass


@params('vaobj', 'bindingindex', 'buffer', 'offset', 'stride', api='gl')
def glVertexArrayBindVertexBufferEXT(vaobj, bindingindex, buffer, offset, stride):
	pass


@params('vaobj', 'attribindex', 'size', 'type', 'normalized', 'relativeoffset', api='gl')
def glVertexArrayVertexAttribFormatEXT(vaobj, attribindex, size, type, normalized, relativeoffset):
	pass


@params('vaobj', 'attribindex', 'size', 'type', 'relativeoffset', api='gl')
def glVertexArrayVertexAttribIFormatEXT(vaobj, attribindex, size, type, relativeoffset):
	pass


@params('vaobj', 'attribindex', 'size', 'type', 'relativeoffset', api='gl')
def glVertexArrayVertexAttribLFormatEXT(vaobj, attribindex, size, type, relativeoffset):
	pass


@params('vaobj', 'attribindex', 'bindingindex', api='gl')
def glVertexArrayVertexAttribBindingEXT(vaobj, attribindex, bindingindex):
	pass


@params('vaobj', 'bindingindex', 'divisor', api='gl')
def glVertexArrayVertexBindingDivisorEXT(vaobj, bindingindex, divisor):
	pass


@params('vaobj', 'buffer', 'index', 'size', 'type', 'stride', 'offset', api='gl')
def glVertexArrayVertexAttribLOffsetEXT(vaobj, buffer, index, size, type, stride, offset):
	pass


@params('texture', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth', 'commit', api='gl')
def glTexturePageCommitmentEXT(texture, level, xoffset, yoffset, zoffset, width, height, depth, commit):
	pass


@params('vaobj', 'index', 'divisor', api='gl')
def glVertexArrayVertexAttribDivisorEXT(vaobj, index, divisor):
	pass


