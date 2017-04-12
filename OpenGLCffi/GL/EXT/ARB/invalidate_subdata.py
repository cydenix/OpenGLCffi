from OpenGLCffi.GL import params
@params(api='gl', prms=['texture', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth'])
def glInvalidateTexSubImage(texture, level, xoffset, yoffset, zoffset, width, height, depth):
	pass


@params(api='gl', prms=['texture', 'level'])
def glInvalidateTexImage(texture, level):
	pass


@params(api='gl', prms=['buffer', 'offset', 'length'])
def glInvalidateBufferSubData(buffer, offset, length):
	pass


@params(api='gl', prms=['buffer'])
def glInvalidateBufferData(buffer):
	pass


@params(api='gl', prms=['target', 'numAttachments', 'attachments'])
def glInvalidateFramebuffer(target, numAttachments, attachments):
	pass


@params(api='gl', prms=['target', 'numAttachments', 'attachments', 'x', 'y', 'width', 'height'])
def glInvalidateSubFramebuffer(target, numAttachments, attachments, x, y, width, height):
	pass


