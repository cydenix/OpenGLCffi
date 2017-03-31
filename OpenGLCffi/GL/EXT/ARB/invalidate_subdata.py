@params('texture', 'level', 'xoffset', 'yoffset', 'zoffset', 'width', 'height', 'depth', api='gl')
def glInvalidateTexSubImage(texture, level, xoffset, yoffset, zoffset, width, height, depth):
	pass


@params('texture', 'level', api='gl')
def glInvalidateTexImage(texture, level):
	pass


@params('buffer', 'offset', 'length', api='gl')
def glInvalidateBufferSubData(buffer, offset, length):
	pass


@params('buffer', api='gl')
def glInvalidateBufferData(buffer):
	pass


@params('target', 'numAttachments', 'attachments', api='gl')
def glInvalidateFramebuffer(target, numAttachments, attachments):
	pass


@params('target', 'numAttachments', 'attachments', 'x', 'y', 'width', 'height', api='gl')
def glInvalidateSubFramebuffer(target, numAttachments, attachments, x, y, width, height):
	pass


