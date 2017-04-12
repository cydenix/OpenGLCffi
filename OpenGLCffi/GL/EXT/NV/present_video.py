from OpenGLCffi.GL import params
@params(api='gl', prms=['video_slot', 'minPresentTime', 'beginPresentTimeId', 'presentDurationId', 'type', 'target0', 'fill0', 'key0', 'target1', 'fill1', 'key1'])
def glPresentFrameKeyedNV(video_slot, minPresentTime, beginPresentTimeId, presentDurationId, type, target0, fill0, key0, target1, fill1, key1):
	pass


@params(api='gl', prms=['video_slot', 'minPresentTime', 'beginPresentTimeId', 'presentDurationId', 'type', 'target0', 'fill0', 'target1', 'fill1', 'target2', 'fill2', 'target3', 'fill3'])
def glPresentFrameDualFillNV(video_slot, minPresentTime, beginPresentTimeId, presentDurationId, type, target0, fill0, target1, fill1, target2, fill2, target3, fill3):
	pass


@params(api='gl', prms=['video_slot', 'pname', 'params'])
def glGetVideoivNV(video_slot, pname, params):
	pass


@params(api='gl', prms=['video_slot', 'pname', 'params'])
def glGetVideouivNV(video_slot, pname, params):
	pass


@params(api='gl', prms=['video_slot', 'pname', 'params'])
def glGetVideoi64vNV(video_slot, pname, params):
	pass


@params(api='gl', prms=['video_slot', 'pname', 'params'])
def glGetVideoui64vNV(video_slot, pname, params):
	pass


