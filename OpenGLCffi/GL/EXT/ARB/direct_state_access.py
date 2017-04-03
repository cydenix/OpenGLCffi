from OpenGLCffi.GL import params
@params('n', 'ids', api='gl')
def glCreateTransformFeedbacks(n, ids):
	pass


@params('xfb', 'index', 'buffer', api='gl')
def glTransformFeedbackBufferBase(xfb, index, buffer):
	pass


@params('xfb', 'index', 'buffer', 'offset', 'size', api='gl')
def glTransformFeedbackBufferRange(xfb, index, buffer, offset, size):
	pass


@params('xfb', 'pname', 'param', api='gl')
def glGetTransformFeedbackiv(xfb, pname, param):
	pass


@params('xfb', 'pname', 'index', 'param', api='gl')
def glGetTransformFeedbacki_v(xfb, pname, index, param):
	pass


@params('xfb', 'pname', 'index', 'param', api='gl')
def glGetTransformFeedbacki64_v(xfb, pname, index, param):
	pass


@params('n', 'buffers', api='gl')
def glCreateBuffers(n, buffers):
	pass


@params('buffer', 'size', 'data', 'flags', api='gl')
def glNamedBufferStorage(buffer, size, data, flags):
	pass


@params('buffer', 'size', 'data', 'usage', api='gl')
def glNamedBufferData(buffer, size, data, usage):
	pass


@params('buffer', 'offset', 'size', 'data', api='gl')
def glNamedBufferSubData(buffer, offset, size, data):
	pass


@params('readBuffer', 'writeBuffer', 'readOffset', 'writeOffset', 'size', api='gl')
def glCopyNamedBufferSubData(readBuffer, writeBuffer, readOffset, writeOffset, size):
	pass


@params('buffer', 'internalformat', 'format', 'type', 'data', api='gl')
def glClearNamedBufferData(buffer, internalformat, format, type, data):
	pass


@params('buffer', 'internalformat', 'offset', 'size', 'format', 'type', 'data', api='gl')
def glClearNamedBufferSubData(buffer, internalformat, offset, size, format, type, data):
	pass


@params('buffer', 'access', api='gl')
def glMapNamedBuffer(buffer, access):
	pass


@params('buffer', 'offset', 'length', 'access', api='gl')
def glMapNamedBufferRange(buffer, offset, length, access):
	pass


@params('buffer', api='gl')
def glUnmapNamedBuffer(buffer):
	pass


@params('buffer', 'offset', 'length', api='gl')
def glFlushMappedNamedBufferRange(buffer, offset, length):
	pass


@params('buffer', 'pname', 'params', api='gl')
def glGetNamedBufferParameteriv(buffer, pname, params):
	pass


@params('buffer', 'pname', 'params', api='gl')
def glGetNamedBufferParameteri64v(buffer, pname, params):
	pass


@params('buffer', 'pname', 'params', api='gl')
def glGetNamedBufferPointerv(buffer, pname, params):
	pass


@params('buffer', 'offset', 'size', 'data', api='gl')
def glGetNamedBufferSubData(buffer, offset, size, data):
	pass


@params('n', 'framebuffers', api='gl')
def glCreateFramebuffers(n, framebuffers):
	pass


@params('framebuffer', 'attachment', 'renderbuffertarget', 'renderbuffer', api='gl')
def glNamedFramebufferRenderbuffer(framebuffer, attachment, renderbuffertarget, renderbuffer):
	pass


@params('framebuffer', 'pname', 'param', api='gl')
def glNamedFramebufferParameteri(framebuffer, pname, param):
	pass


@params('framebuffer', 'attachment', 'texture', 'level', api='gl')
def glNamedFramebufferTexture(framebuffer, attachment, texture, level):
	pass


@params('framebuffer', 'attachment', 'texture', 'level', 'layer', api='gl')
def glNamedFramebufferTextureLayer(framebuffer, attachment, texture, level, layer):
	pass


@params('framebuffer', 'buf', api='gl')
def glNamedFramebufferDrawBuffer(framebuffer, buf):
	pass


@params('framebuffer', 'n', 'bufs', api='gl')
def glNamedFramebufferDrawBuffers(framebuffer, n, bufs):
	pass


@params('framebuffer', 'src', api='gl')
def glNamedFramebufferReadBuffer(framebuffer, src):
	pass


@params('framebuffer', 'numAttachments', 'attachments', api='gl')
def glInvalidateNamedFramebufferData(framebuffer, numAttachments, attachments):
	pass


@params('framebuffer', 'numAttachments', 'attachments', 'x', 'y', 'width', 'height', api='gl')
def glInvalidateNamedFramebufferSubData(framebuffer, numAttachments, attachments, x, y, width, height):
	pass


@params('framebuffer', 'buffer', 'drawbuffer', 'value', api='gl')
def glClearNamedFramebufferiv(framebuffer, buffer, drawbuffer, value):
	pass


@params('framebuffer', 'buffer', 'drawbuffer', 'value', api='gl')
def glClearNamedFramebufferuiv(framebuffer, buffer, drawbuffer, value):
	pass


@params('framebuffer', 'buffer', 'drawbuffer', 'value', api='gl')
def glClearNamedFramebufferfv(framebuffer, buffer, drawbuffer, value):
	pass


@params('framebuffer', 'buffer', 'drawbuffer', 'depth', 'stencil', api='gl')
def glClearNamedFramebufferfi(framebuffer, buffer, drawbuffer, depth, stencil):
	pass


@params('readFramebuffer', 'drawFramebuffer', 'srcX0', 'srcY0', 'srcX1', 'srcY1', 'dstX0', 'dstY0', 'dstX1', 'dstY1', 'mask', 'filter', api='gl')
def glBlitNamedFramebuffer(readFramebuffer, drawFramebuffer, srcX0, srcY0, srcX1, srcY1, dstX0, dstY0, dstX1, dstY1, mask, filter):
	pass


@params('framebuffer', 'target', api='gl')
def glCheckNamedFramebufferStatus(framebuffer, target):
	pass


@params('framebuffer', 'pname', 'param', api='gl')
def glGetNamedFramebufferParameteriv(framebuffer, pname, param):
	pass


@params('framebuffer', 'attachment', 'pname', 'params', api='gl')
def glGetNamedFramebufferAttachmentParameteriv(framebuffer, attachment, pname, params):
	pass


@params('n', 'renderbuffers', api='gl')
def glCreateRenderbuffers(n, renderbuffers):
	pass


@params('renderbuffer', 'internalformat', 'width', 'height', api='gl')
def glNamedRenderbufferStorage(renderbuffer, internalformat, width, height):
	pass


@params('renderbuffer', 'samples', 'internalformat', 'width', 'height', api='gl')
def glNamedRenderbufferStorageMultisample(renderbuffer, samples, internalformat, width, height):
	pass


@params('renderbuffer', 'pname', 'params', api='gl')
def glGetNamedRenderbufferParameteriv(renderbuffer, pname, params):
	pass


@params('target', 'n', 'textures', api='gl')
def glCreateTextures(target, n, textures):
	pass


@params('texture', 'internalformat', 'buffer', api='gl')
def glTextureBuffer(texture, internalformat, buffer):
	pass


@params('texture', 'internalformat', 'buffer', 'offset', 'size', api='gl')
def glTextureBufferRange(texture, internalformat, buffer, offset, size):
	pass


@params('texture', 'levels', 'internalformat', 'width', api='gl')
def glTextureStorage1D(texture, levels, internalformat, width):
	pass


@params('texture', 'levels', 'internalformat', 'width', 'height', api='gl')
def glTextureStorage2D(texture, levels, internalformat, width, height):
	pass


@params('texture', 'levels', 'internalformat', 'width', 'height', 'depth', api='gl')
def glTextureStorage3D(texture, levels, internalformat, width, height, depth):
	pass


@params('texture', 'samples', 'internalformat', 'width', 'height', 'fixedsamplelocations', api='gl')
def glTextureStorage2DMultisample(texture, samples, internalformat, width, height, fixedsamplelocations):
	pass


@params('texture', 'samples', 'internalformat', 'width', 'height', 'depth', 'fixedsamplelocations', api='gl')
def glTextureStorage3DMultisample(texture, samples, internalformat, width, height, depth, fixedsamplelocations):
	pass


@params('texture', 'level', 'xoffset', 'width', 'format', 'type', 'pixels', api='gl')
def glTextureSubImage1D(texture, level, xoffset, width, format, type, pixels):
	pass


@params('texture', 'level', 'xoffset', 'yoffset', 'width', 'height', 'format', 'type', 'pixels', api='gl')
def glTextureSubImage2D(texture, level, xoffset, yoffset, width, height, format, type, pixels):
	pass


@params('texture', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth', 'format', 'type', 'pixels', api='gl')
def glTextureSubImage3D(texture, level, xoffset, yoffset, zoffset, width, height, depth, format, type, pixels):
	pass


@params('texture', 'level', 'xoffset', 'width', 'format', 'imageSize', 'data', api='gl')
def glCompressedTextureSubImage1D(texture, level, xoffset, width, format, imageSize, data):
	pass


@params('texture', 'level', 'xoffset', 'yoffset', 'width', 'height', 'format', 'imageSize', 'data', api='gl')
def glCompressedTextureSubImage2D(texture, level, xoffset, yoffset, width, height, format, imageSize, data):
	pass


@params('texture', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth', 'format', 'imageSize', 'data', api='gl')
def glCompressedTextureSubImage3D(texture, level, xoffset, yoffset, zoffset, width, height, depth, format, imageSize, data):
	pass


@params('texture', 'level', 'xoffset', 'x', 'y', 'width', api='gl')
def glCopyTextureSubImage1D(texture, level, xoffset, x, y, width):
	pass


@params('texture', 'level', 'xoffset', 'yoffset', 'x', 'y', 'width', 'height', api='gl')
def glCopyTextureSubImage2D(texture, level, xoffset, yoffset, x, y, width, height):
	pass


@params('texture', 'level', 'xoffset', 'yoffset', 'zoffset', 'x', 'y', 'width', 'height', api='gl')
def glCopyTextureSubImage3D(texture, level, xoffset, yoffset, zoffset, x, y, width, height):
	pass


@params('texture', 'pname', 'param', api='gl')
def glTextureParameterf(texture, pname, param):
	pass


@params('texture', 'pname', 'param', api='gl')
def glTextureParameterfv(texture, pname, param):
	pass


@params('texture', 'pname', 'param', api='gl')
def glTextureParameteri(texture, pname, param):
	pass


@params('texture', 'pname', 'params', api='gl')
def glTextureParameterIiv(texture, pname, params):
	pass


@params('texture', 'pname', 'params', api='gl')
def glTextureParameterIuiv(texture, pname, params):
	pass


@params('texture', 'pname', 'param', api='gl')
def glTextureParameteriv(texture, pname, param):
	pass


@params('texture', api='gl')
def glGenerateTextureMipmap(texture):
	pass


@params('unit', 'texture', api='gl')
def glBindTextureUnit(unit, texture):
	pass


@params('texture', 'level', 'format', 'type', 'bufSize', 'pixels', api='gl')
def glGetTextureImage(texture, level, format, type, bufSize, pixels):
	pass


@params('texture', 'level', 'bufSize', 'pixels', api='gl')
def glGetCompressedTextureImage(texture, level, bufSize, pixels):
	pass


@params('texture', 'level', 'pname', 'params', api='gl')
def glGetTextureLevelParameterfv(texture, level, pname, params):
	pass


@params('texture', 'level', 'pname', 'params', api='gl')
def glGetTextureLevelParameteriv(texture, level, pname, params):
	pass


@params('texture', 'pname', 'params', api='gl')
def glGetTextureParameterfv(texture, pname, params):
	pass


@params('texture', 'pname', 'params', api='gl')
def glGetTextureParameterIiv(texture, pname, params):
	pass


@params('texture', 'pname', 'params', api='gl')
def glGetTextureParameterIuiv(texture, pname, params):
	pass


@params('texture', 'pname', 'params', api='gl')
def glGetTextureParameteriv(texture, pname, params):
	pass


@params('n', 'arrays', api='gl')
def glCreateVertexArrays(n, arrays):
	pass


@params('vaobj', 'index', api='gl')
def glDisableVertexArrayAttrib(vaobj, index):
	pass


@params('vaobj', 'index', api='gl')
def glEnableVertexArrayAttrib(vaobj, index):
	pass


@params('vaobj', 'buffer', api='gl')
def glVertexArrayElementBuffer(vaobj, buffer):
	pass


@params('vaobj', 'bindingindex', 'buffer', 'offset', 'stride', api='gl')
def glVertexArrayVertexBuffer(vaobj, bindingindex, buffer, offset, stride):
	pass


@params('vaobj', 'first', 'count', 'buffers', 'offsets', 'strides', api='gl')
def glVertexArrayVertexBuffers(vaobj, first, count, buffers, offsets, strides):
	pass


@params('vaobj', 'attribindex', 'bindingindex', api='gl')
def glVertexArrayAttribBinding(vaobj, attribindex, bindingindex):
	pass


@params('vaobj', 'attribindex', 'size', 'type', 'normalized', 'relativeoffset', api='gl')
def glVertexArrayAttribFormat(vaobj, attribindex, size, type, normalized, relativeoffset):
	pass


@params('vaobj', 'attribindex', 'size', 'type', 'relativeoffset', api='gl')
def glVertexArrayAttribIFormat(vaobj, attribindex, size, type, relativeoffset):
	pass


@params('vaobj', 'attribindex', 'size', 'type', 'relativeoffset', api='gl')
def glVertexArrayAttribLFormat(vaobj, attribindex, size, type, relativeoffset):
	pass


@params('vaobj', 'bindingindex', 'divisor', api='gl')
def glVertexArrayBindingDivisor(vaobj, bindingindex, divisor):
	pass


@params('vaobj', 'pname', 'param', api='gl')
def glGetVertexArrayiv(vaobj, pname, param):
	pass


@params('vaobj', 'index', 'pname', 'param', api='gl')
def glGetVertexArrayIndexediv(vaobj, index, pname, param):
	pass


@params('vaobj', 'index', 'pname', 'param', api='gl')
def glGetVertexArrayIndexed64iv(vaobj, index, pname, param):
	pass


@params('n', 'samplers', api='gl')
def glCreateSamplers(n, samplers):
	pass


@params('n', 'pipelines', api='gl')
def glCreateProgramPipelines(n, pipelines):
	pass


@params('target', 'n', 'ids', api='gl')
def glCreateQueries(target, n, ids):
	pass


@params('id', 'buffer', 'pname', 'offset', api='gl')
def glGetQueryBufferObjecti64v(id, buffer, pname, offset):
	pass


@params('id', 'buffer', 'pname', 'offset', api='gl')
def glGetQueryBufferObjectiv(id, buffer, pname, offset):
	pass


@params('id', 'buffer', 'pname', 'offset', api='gl')
def glGetQueryBufferObjectui64v(id, buffer, pname, offset):
	pass


@params('id', 'buffer', 'pname', 'offset', api='gl')
def glGetQueryBufferObjectuiv(id, buffer, pname, offset):
	pass


