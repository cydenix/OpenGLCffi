from OpenGLCffi.GL import params
@params(api='gl', prms=['n', 'ids'])
def glCreateTransformFeedbacks(n, ids):
	pass


@params(api='gl', prms=['xfb', 'index', 'buffer'])
def glTransformFeedbackBufferBase(xfb, index, buffer):
	pass


@params(api='gl', prms=['xfb', 'index', 'buffer', 'offset', 'size'])
def glTransformFeedbackBufferRange(xfb, index, buffer, offset, size):
	pass


@params(api='gl', prms=['xfb', 'pname', 'param'])
def glGetTransformFeedbackiv(xfb, pname, param):
	pass


@params(api='gl', prms=['xfb', 'pname', 'index', 'param'])
def glGetTransformFeedbacki_v(xfb, pname, index, param):
	pass


@params(api='gl', prms=['xfb', 'pname', 'index', 'param'])
def glGetTransformFeedbacki64_v(xfb, pname, index, param):
	pass


@params(api='gl', prms=['n', 'buffers'])
def glCreateBuffers(n, buffers):
	pass


@params(api='gl', prms=['buffer', 'size', 'data', 'flags'])
def glNamedBufferStorage(buffer, size, data, flags):
	pass


@params(api='gl', prms=['buffer', 'size', 'data', 'usage'])
def glNamedBufferData(buffer, size, data, usage):
	pass


@params(api='gl', prms=['buffer', 'offset', 'size', 'data'])
def glNamedBufferSubData(buffer, offset, size, data):
	pass


@params(api='gl', prms=['readBuffer', 'writeBuffer', 'readOffset', 'writeOffset', 'size'])
def glCopyNamedBufferSubData(readBuffer, writeBuffer, readOffset, writeOffset, size):
	pass


@params(api='gl', prms=['buffer', 'internalformat', 'format', 'type', 'data'])
def glClearNamedBufferData(buffer, internalformat, format, type, data):
	pass


@params(api='gl', prms=['buffer', 'internalformat', 'offset', 'size', 'format', 'type', 'data'])
def glClearNamedBufferSubData(buffer, internalformat, offset, size, format, type, data):
	pass


@params(api='gl', prms=['buffer', 'access'])
def glMapNamedBuffer(buffer, access):
	pass


@params(api='gl', prms=['buffer', 'offset', 'length', 'access'])
def glMapNamedBufferRange(buffer, offset, length, access):
	pass


@params(api='gl', prms=['buffer'])
def glUnmapNamedBuffer(buffer):
	pass


@params(api='gl', prms=['buffer', 'offset', 'length'])
def glFlushMappedNamedBufferRange(buffer, offset, length):
	pass


@params(api='gl', prms=['buffer', 'pname', 'params'])
def glGetNamedBufferParameteriv(buffer, pname, params):
	pass


@params(api='gl', prms=['buffer', 'pname', 'params'])
def glGetNamedBufferParameteri64v(buffer, pname, params):
	pass


@params(api='gl', prms=['buffer', 'pname', 'params'])
def glGetNamedBufferPointerv(buffer, pname, params):
	pass


@params(api='gl', prms=['buffer', 'offset', 'size', 'data'])
def glGetNamedBufferSubData(buffer, offset, size, data):
	pass


@params(api='gl', prms=['n', 'framebuffers'])
def glCreateFramebuffers(n, framebuffers):
	pass


@params(api='gl', prms=['framebuffer', 'attachment', 'renderbuffertarget', 'renderbuffer'])
def glNamedFramebufferRenderbuffer(framebuffer, attachment, renderbuffertarget, renderbuffer):
	pass


@params(api='gl', prms=['framebuffer', 'pname', 'param'])
def glNamedFramebufferParameteri(framebuffer, pname, param):
	pass


@params(api='gl', prms=['framebuffer', 'attachment', 'texture', 'level'])
def glNamedFramebufferTexture(framebuffer, attachment, texture, level):
	pass


@params(api='gl', prms=['framebuffer', 'attachment', 'texture', 'level', 'layer'])
def glNamedFramebufferTextureLayer(framebuffer, attachment, texture, level, layer):
	pass


@params(api='gl', prms=['framebuffer', 'buf'])
def glNamedFramebufferDrawBuffer(framebuffer, buf):
	pass


@params(api='gl', prms=['framebuffer', 'n', 'bufs'])
def glNamedFramebufferDrawBuffers(framebuffer, n, bufs):
	pass


@params(api='gl', prms=['framebuffer', 'src'])
def glNamedFramebufferReadBuffer(framebuffer, src):
	pass


@params(api='gl', prms=['framebuffer', 'numAttachments', 'attachments'])
def glInvalidateNamedFramebufferData(framebuffer, numAttachments, attachments):
	pass


@params(api='gl', prms=['framebuffer', 'numAttachments', 'attachments', 'x', 'y', 'width', 'height'])
def glInvalidateNamedFramebufferSubData(framebuffer, numAttachments, attachments, x, y, width, height):
	pass


@params(api='gl', prms=['framebuffer', 'buffer', 'drawbuffer', 'value'])
def glClearNamedFramebufferiv(framebuffer, buffer, drawbuffer, value):
	pass


@params(api='gl', prms=['framebuffer', 'buffer', 'drawbuffer', 'value'])
def glClearNamedFramebufferuiv(framebuffer, buffer, drawbuffer, value):
	pass


@params(api='gl', prms=['framebuffer', 'buffer', 'drawbuffer', 'value'])
def glClearNamedFramebufferfv(framebuffer, buffer, drawbuffer, value):
	pass


@params(api='gl', prms=['framebuffer', 'buffer', 'drawbuffer', 'depth', 'stencil'])
def glClearNamedFramebufferfi(framebuffer, buffer, drawbuffer, depth, stencil):
	pass


@params(api='gl', prms=['readFramebuffer', 'drawFramebuffer', 'srcX0', 'srcY0', 'srcX1', 'srcY1', 'dstX0', 'dstY0', 'dstX1', 'dstY1', 'mask', 'filter'])
def glBlitNamedFramebuffer(readFramebuffer, drawFramebuffer, srcX0, srcY0, srcX1, srcY1, dstX0, dstY0, dstX1, dstY1, mask, filter):
	pass


@params(api='gl', prms=['framebuffer', 'target'])
def glCheckNamedFramebufferStatus(framebuffer, target):
	pass


@params(api='gl', prms=['framebuffer', 'pname', 'param'])
def glGetNamedFramebufferParameteriv(framebuffer, pname, param):
	pass


@params(api='gl', prms=['framebuffer', 'attachment', 'pname', 'params'])
def glGetNamedFramebufferAttachmentParameteriv(framebuffer, attachment, pname, params):
	pass


@params(api='gl', prms=['n', 'renderbuffers'])
def glCreateRenderbuffers(n, renderbuffers):
	pass


@params(api='gl', prms=['renderbuffer', 'internalformat', 'width', 'height'])
def glNamedRenderbufferStorage(renderbuffer, internalformat, width, height):
	pass


@params(api='gl', prms=['renderbuffer', 'samples', 'internalformat', 'width', 'height'])
def glNamedRenderbufferStorageMultisample(renderbuffer, samples, internalformat, width, height):
	pass


@params(api='gl', prms=['renderbuffer', 'pname', 'params'])
def glGetNamedRenderbufferParameteriv(renderbuffer, pname, params):
	pass


@params(api='gl', prms=['target', 'n', 'textures'])
def glCreateTextures(target, n, textures):
	pass


@params(api='gl', prms=['texture', 'internalformat', 'buffer'])
def glTextureBuffer(texture, internalformat, buffer):
	pass


@params(api='gl', prms=['texture', 'internalformat', 'buffer', 'offset', 'size'])
def glTextureBufferRange(texture, internalformat, buffer, offset, size):
	pass


@params(api='gl', prms=['texture', 'levels', 'internalformat', 'width'])
def glTextureStorage1D(texture, levels, internalformat, width):
	pass


@params(api='gl', prms=['texture', 'levels', 'internalformat', 'width', 'height'])
def glTextureStorage2D(texture, levels, internalformat, width, height):
	pass


@params(api='gl', prms=['texture', 'levels', 'internalformat', 'width', 'height', 'depth'])
def glTextureStorage3D(texture, levels, internalformat, width, height, depth):
	pass


@params(api='gl', prms=['texture', 'samples', 'internalformat', 'width', 'height', 'fixedsamplelocations'])
def glTextureStorage2DMultisample(texture, samples, internalformat, width, height, fixedsamplelocations):
	pass


@params(api='gl', prms=['texture', 'samples', 'internalformat', 'width', 'height', 'depth', 'fixedsamplelocations'])
def glTextureStorage3DMultisample(texture, samples, internalformat, width, height, depth, fixedsamplelocations):
	pass


@params(api='gl', prms=['texture', 'level', 'xoffset', 'width', 'format', 'type', 'pixels'])
def glTextureSubImage1D(texture, level, xoffset, width, format, type, pixels):
	pass


@params(api='gl', prms=['texture', 'level', 'xoffset', 'yoffset', 'width', 'height', 'format', 'type', 'pixels'])
def glTextureSubImage2D(texture, level, xoffset, yoffset, width, height, format, type, pixels):
	pass


@params(api='gl', prms=['texture', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth', 'format', 'type', 'pixels'])
def glTextureSubImage3D(texture, level, xoffset, yoffset, zoffset, width, height, depth, format, type, pixels):
	pass


@params(api='gl', prms=['texture', 'level', 'xoffset', 'width', 'format', 'imageSize', 'data'])
def glCompressedTextureSubImage1D(texture, level, xoffset, width, format, imageSize, data):
	pass


@params(api='gl', prms=['texture', 'level', 'xoffset', 'yoffset', 'width', 'height', 'format', 'imageSize', 'data'])
def glCompressedTextureSubImage2D(texture, level, xoffset, yoffset, width, height, format, imageSize, data):
	pass


@params(api='gl', prms=['texture', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth', 'format', 'imageSize', 'data'])
def glCompressedTextureSubImage3D(texture, level, xoffset, yoffset, zoffset, width, height, depth, format, imageSize, data):
	pass


@params(api='gl', prms=['texture', 'level', 'xoffset', 'x', 'y', 'width'])
def glCopyTextureSubImage1D(texture, level, xoffset, x, y, width):
	pass


@params(api='gl', prms=['texture', 'level', 'xoffset', 'yoffset', 'x', 'y', 'width', 'height'])
def glCopyTextureSubImage2D(texture, level, xoffset, yoffset, x, y, width, height):
	pass


@params(api='gl', prms=['texture', 'level', 'xoffset', 'yoffset', 'zoffset', 'x', 'y', 'width', 'height'])
def glCopyTextureSubImage3D(texture, level, xoffset, yoffset, zoffset, x, y, width, height):
	pass


@params(api='gl', prms=['texture', 'pname', 'param'])
def glTextureParameterf(texture, pname, param):
	pass


@params(api='gl', prms=['texture', 'pname', 'param'])
def glTextureParameterfv(texture, pname, param):
	pass


@params(api='gl', prms=['texture', 'pname', 'param'])
def glTextureParameteri(texture, pname, param):
	pass


@params(api='gl', prms=['texture', 'pname', 'params'])
def glTextureParameterIiv(texture, pname, params):
	pass


@params(api='gl', prms=['texture', 'pname', 'params'])
def glTextureParameterIuiv(texture, pname, params):
	pass


@params(api='gl', prms=['texture', 'pname', 'param'])
def glTextureParameteriv(texture, pname, param):
	pass


@params(api='gl', prms=['texture'])
def glGenerateTextureMipmap(texture):
	pass


@params(api='gl', prms=['unit', 'texture'])
def glBindTextureUnit(unit, texture):
	pass


@params(api='gl', prms=['texture', 'level', 'format', 'type', 'bufSize', 'pixels'])
def glGetTextureImage(texture, level, format, type, bufSize, pixels):
	pass


@params(api='gl', prms=['texture', 'level', 'bufSize', 'pixels'])
def glGetCompressedTextureImage(texture, level, bufSize, pixels):
	pass


@params(api='gl', prms=['texture', 'level', 'pname', 'params'])
def glGetTextureLevelParameterfv(texture, level, pname, params):
	pass


@params(api='gl', prms=['texture', 'level', 'pname', 'params'])
def glGetTextureLevelParameteriv(texture, level, pname, params):
	pass


@params(api='gl', prms=['texture', 'pname', 'params'])
def glGetTextureParameterfv(texture, pname, params):
	pass


@params(api='gl', prms=['texture', 'pname', 'params'])
def glGetTextureParameterIiv(texture, pname, params):
	pass


@params(api='gl', prms=['texture', 'pname', 'params'])
def glGetTextureParameterIuiv(texture, pname, params):
	pass


@params(api='gl', prms=['texture', 'pname', 'params'])
def glGetTextureParameteriv(texture, pname, params):
	pass


@params(api='gl', prms=['n', 'arrays'])
def glCreateVertexArrays(n, arrays):
	pass


@params(api='gl', prms=['vaobj', 'index'])
def glDisableVertexArrayAttrib(vaobj, index):
	pass


@params(api='gl', prms=['vaobj', 'index'])
def glEnableVertexArrayAttrib(vaobj, index):
	pass


@params(api='gl', prms=['vaobj', 'buffer'])
def glVertexArrayElementBuffer(vaobj, buffer):
	pass


@params(api='gl', prms=['vaobj', 'bindingindex', 'buffer', 'offset', 'stride'])
def glVertexArrayVertexBuffer(vaobj, bindingindex, buffer, offset, stride):
	pass


@params(api='gl', prms=['vaobj', 'first', 'count', 'buffers', 'offsets', 'strides'])
def glVertexArrayVertexBuffers(vaobj, first, count, buffers, offsets, strides):
	pass


@params(api='gl', prms=['vaobj', 'attribindex', 'bindingindex'])
def glVertexArrayAttribBinding(vaobj, attribindex, bindingindex):
	pass


@params(api='gl', prms=['vaobj', 'attribindex', 'size', 'type', 'normalized', 'relativeoffset'])
def glVertexArrayAttribFormat(vaobj, attribindex, size, type, normalized, relativeoffset):
	pass


@params(api='gl', prms=['vaobj', 'attribindex', 'size', 'type', 'relativeoffset'])
def glVertexArrayAttribIFormat(vaobj, attribindex, size, type, relativeoffset):
	pass


@params(api='gl', prms=['vaobj', 'attribindex', 'size', 'type', 'relativeoffset'])
def glVertexArrayAttribLFormat(vaobj, attribindex, size, type, relativeoffset):
	pass


@params(api='gl', prms=['vaobj', 'bindingindex', 'divisor'])
def glVertexArrayBindingDivisor(vaobj, bindingindex, divisor):
	pass


@params(api='gl', prms=['vaobj', 'pname', 'param'])
def glGetVertexArrayiv(vaobj, pname, param):
	pass


@params(api='gl', prms=['vaobj', 'index', 'pname', 'param'])
def glGetVertexArrayIndexediv(vaobj, index, pname, param):
	pass


@params(api='gl', prms=['vaobj', 'index', 'pname', 'param'])
def glGetVertexArrayIndexed64iv(vaobj, index, pname, param):
	pass


@params(api='gl', prms=['n', 'samplers'])
def glCreateSamplers(n, samplers):
	pass


@params(api='gl', prms=['n', 'pipelines'])
def glCreateProgramPipelines(n, pipelines):
	pass


@params(api='gl', prms=['target', 'n', 'ids'])
def glCreateQueries(target, n, ids):
	pass


@params(api='gl', prms=['id', 'buffer', 'pname', 'offset'])
def glGetQueryBufferObjecti64v(id, buffer, pname, offset):
	pass


@params(api='gl', prms=['id', 'buffer', 'pname', 'offset'])
def glGetQueryBufferObjectiv(id, buffer, pname, offset):
	pass


@params(api='gl', prms=['id', 'buffer', 'pname', 'offset'])
def glGetQueryBufferObjectui64v(id, buffer, pname, offset):
	pass


@params(api='gl', prms=['id', 'buffer', 'pname', 'offset'])
def glGetQueryBufferObjectuiv(id, buffer, pname, offset):
	pass


