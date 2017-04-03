from OpenGLCffi.GL import params
@params('video_slot', 'minPresentTime', 'beginPresentTimeId', 'presentDurationId', 'type', 'target0', 'fill0', 'key0', 'target1', 'fill1', 'key1', api='gl')
def glPresentFrameKeyedNV(video_slot, minPresentTime, beginPresentTimeId, presentDurationId, type, target0, fill0, key0, target1, fill1, key1):
	pass


@params('video_slot', 'minPresentTime', 'beginPresentTimeId', 'presentDurationId', 'type', 'target0', 'fill0', 'target1', 'fill1', 'target2', 'fill2', 'target3', 'fill3', api='gl')
def glPresentFrameDualFillNV(video_slot, minPresentTime, beginPresentTimeId, presentDurationId, type, target0, fill0, target1, fill1, target2, fill2, target3, fill3):
	pass


@params('video_slot', 'pname', 'params', api='gl')
def glGetVideoivNV(video_slot, pname, params):
	pass


@params('video_slot', 'pname', 'params', api='gl')
def glGetVideouivNV(video_slot, pname, params):
	pass


@params('video_slot', 'pname', 'params', api='gl')
def glGetVideoi64vNV(video_slot, pname, params):
	pass


@params('video_slot', 'pname', 'params', api='gl')
def glGetVideoui64vNV(video_slot, pname, params):
	pass


