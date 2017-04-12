from OpenGLCffi.GLES2 import params
@params(api='gles2', prms=['range'])
def glGenPathsNV():
	pass


@params(api='gles2', prms=['path', 'range'])
def glDeletePathsNV(path, range):
	pass


@params(api='gles2', prms=['path'])
def glIsPathNV(path):
	pass


@params(api='gles2', prms=['path', 'numCommands', 'commands', 'numCoords', 'coordType', 'coords'])
def glPathCommandsNV(path, numCommands, commands, numCoords, coordType, coords):
	pass


@params(api='gles2', prms=['path', 'numCoords', 'coordType', 'coords'])
def glPathCoordsNV(path, numCoords, coordType, coords):
	pass


@params(api='gles2', prms=['path', 'commandStart', 'commandsToDelete', 'numCommands', 'commands', 'numCoords', 'coordType', 'coords'])
def glPathSubCommandsNV(path, commandStart, commandsToDelete, numCommands, commands, numCoords, coordType, coords):
	pass


@params(api='gles2', prms=['path', 'coordStart', 'numCoords', 'coordType', 'coords'])
def glPathSubCoordsNV(path, coordStart, numCoords, coordType, coords):
	pass


@params(api='gles2', prms=['path', 'format', 'length', 'pathString'])
def glPathStringNV(path, format, length, pathString):
	pass


@params(api='gles2', prms=['firstPathName', 'fontTarget', 'fontName', 'fontStyle', 'numGlyphs', 'type', 'charcodes', 'handleMissingGlyphs', 'pathParameterTemplate', 'emScale'])
def glPathGlyphsNV(firstPathName, fontTarget, fontName, fontStyle, numGlyphs, type, charcodes, handleMissingGlyphs, pathParameterTemplate, emScale):
	pass


@params(api='gles2', prms=['firstPathName', 'fontTarget', 'fontName', 'fontStyle', 'firstGlyph', 'numGlyphs', 'handleMissingGlyphs', 'pathParameterTemplate', 'emScale'])
def glPathGlyphRangeNV(firstPathName, fontTarget, fontName, fontStyle, firstGlyph, numGlyphs, handleMissingGlyphs, pathParameterTemplate, emScale):
	pass


@params(api='gles2', prms=['resultPath', 'numPaths', 'paths', 'weights'])
def glWeightPathsNV(resultPath, numPaths, paths, weights):
	pass


@params(api='gles2', prms=['resultPath', 'srcPath'])
def glCopyPathNV(resultPath, srcPath):
	pass


@params(api='gles2', prms=['resultPath', 'pathA', 'pathB', 'weight'])
def glInterpolatePathsNV(resultPath, pathA, pathB, weight):
	pass


@params(api='gles2', prms=['resultPath', 'srcPath', 'transformType', 'transformValues'])
def glTransformPathNV(resultPath, srcPath, transformType, transformValues):
	pass


@params(api='gles2', prms=['path', 'pname', 'value'])
def glPathParameterivNV(path, pname, value):
	pass


@params(api='gles2', prms=['path', 'pname', 'value'])
def glPathParameteriNV(path, pname, value):
	pass


@params(api='gles2', prms=['path', 'pname', 'value'])
def glPathParameterfvNV(path, pname, value):
	pass


@params(api='gles2', prms=['path', 'pname', 'value'])
def glPathParameterfNV(path, pname, value):
	pass


@params(api='gles2', prms=['path', 'dashCount', 'dashArray'])
def glPathDashArrayNV(path, dashCount, dashArray):
	pass


@params(api='gles2', prms=['func', 'ref', 'mask'])
def glPathStencilFuncNV(func, ref, mask):
	pass


@params(api='gles2', prms=['factor', 'units'])
def glPathStencilDepthOffsetNV(factor, units):
	pass


@params(api='gles2', prms=['path', 'fillMode', 'mask'])
def glStencilFillPathNV(path, fillMode, mask):
	pass


@params(api='gles2', prms=['path', 'reference', 'mask'])
def glStencilStrokePathNV(path, reference, mask):
	pass


@params(api='gles2', prms=['numPaths', 'pathNameType', 'paths', 'pathBase', 'fillMode', 'mask', 'transformType', 'transformValues'])
def glStencilFillPathInstancedNV(numPaths, pathNameType, paths, pathBase, fillMode, mask, transformType, transformValues):
	pass


@params(api='gles2', prms=['numPaths', 'pathNameType', 'paths', 'pathBase', 'reference', 'mask', 'transformType', 'transformValues'])
def glStencilStrokePathInstancedNV(numPaths, pathNameType, paths, pathBase, reference, mask, transformType, transformValues):
	pass


@params(api='gles2', prms=['func'])
def glPathCoverDepthFuncNV(func):
	pass


@params(api='gles2', prms=['path', 'coverMode'])
def glCoverFillPathNV(path, coverMode):
	pass


@params(api='gles2', prms=['path', 'coverMode'])
def glCoverStrokePathNV(path, coverMode):
	pass


@params(api='gles2', prms=['numPaths', 'pathNameType', 'paths', 'pathBase', 'coverMode', 'transformType', 'transformValues'])
def glCoverFillPathInstancedNV(numPaths, pathNameType, paths, pathBase, coverMode, transformType, transformValues):
	pass


@params(api='gles2', prms=['numPaths', 'pathNameType', 'paths', 'pathBase', 'coverMode', 'transformType', 'transformValues'])
def glCoverStrokePathInstancedNV(numPaths, pathNameType, paths, pathBase, coverMode, transformType, transformValues):
	pass


@params(api='gles2', prms=['path', 'pname', 'value'])
def glGetPathParameterivNV(path, pname, value):
	pass


@params(api='gles2', prms=['path', 'pname', 'value'])
def glGetPathParameterfvNV(path, pname, value):
	pass


@params(api='gles2', prms=['path', 'commands'])
def glGetPathCommandsNV(path, commands):
	pass


@params(api='gles2', prms=['path', 'coords'])
def glGetPathCoordsNV(path, coords):
	pass


@params(api='gles2', prms=['path', 'dashArray'])
def glGetPathDashArrayNV(path, dashArray):
	pass


@params(api='gles2', prms=['metricQueryMask', 'numPaths', 'pathNameType', 'paths', 'pathBase', 'stride', 'metrics'])
def glGetPathMetricsNV(metricQueryMask, numPaths, pathNameType, paths, pathBase, stride, metrics):
	pass


@params(api='gles2', prms=['metricQueryMask', 'firstPathName', 'numPaths', 'stride', 'metrics'])
def glGetPathMetricRangeNV(metricQueryMask, firstPathName, numPaths, stride, metrics):
	pass


@params(api='gles2', prms=['pathListMode', 'numPaths', 'pathNameType', 'paths', 'pathBase', 'advanceScale', 'kerningScale', 'transformType', 'returnedSpacing'])
def glGetPathSpacingNV(pathListMode, numPaths, pathNameType, paths, pathBase, advanceScale, kerningScale, transformType, returnedSpacing):
	pass


@params(api='gles2', prms=['path', 'mask', 'x', 'y'])
def glIsPointInFillPathNV(path, mask, x, y):
	pass


@params(api='gles2', prms=['path', 'x', 'y'])
def glIsPointInStrokePathNV(path, x, y):
	pass


@params(api='gles2', prms=['path', 'startSegment', 'numSegments'])
def glGetPathLengthNV(path, startSegment, numSegments):
	pass


@params(api='gles2', prms=['path', 'startSegment', 'numSegments', 'distance', 'x', 'y', 'tangentX', 'tangentY'])
def glPointAlongPathNV(path, startSegment, numSegments, distance, x, y, tangentX, tangentY):
	pass


@params(api='gles2', prms=['matrixMode', 'm'])
def glMatrixLoad3x2fNV(matrixMode, m):
	pass


@params(api='gles2', prms=['matrixMode', 'm'])
def glMatrixLoad3x3fNV(matrixMode, m):
	pass


@params(api='gles2', prms=['matrixMode', 'm'])
def glMatrixLoadTranspose3x3fNV(matrixMode, m):
	pass


@params(api='gles2', prms=['matrixMode', 'm'])
def glMatrixMult3x2fNV(matrixMode, m):
	pass


@params(api='gles2', prms=['matrixMode', 'm'])
def glMatrixMult3x3fNV(matrixMode, m):
	pass


@params(api='gles2', prms=['matrixMode', 'm'])
def glMatrixMultTranspose3x3fNV(matrixMode, m):
	pass


@params(api='gles2', prms=['path', 'fillMode', 'mask', 'coverMode'])
def glStencilThenCoverFillPathNV(path, fillMode, mask, coverMode):
	pass


@params(api='gles2', prms=['path', 'reference', 'mask', 'coverMode'])
def glStencilThenCoverStrokePathNV(path, reference, mask, coverMode):
	pass


@params(api='gles2', prms=['numPaths', 'pathNameType', 'paths', 'pathBase', 'fillMode', 'mask', 'coverMode', 'transformType', 'transformValues'])
def glStencilThenCoverFillPathInstancedNV(numPaths, pathNameType, paths, pathBase, fillMode, mask, coverMode, transformType, transformValues):
	pass


@params(api='gles2', prms=['numPaths', 'pathNameType', 'paths', 'pathBase', 'reference', 'mask', 'coverMode', 'transformType', 'transformValues'])
def glStencilThenCoverStrokePathInstancedNV(numPaths, pathNameType, paths, pathBase, reference, mask, coverMode, transformType, transformValues):
	pass


@params(api='gles2', prms=['fontTarget', 'fontName', 'fontStyle', 'pathParameterTemplate', 'emScale', 'baseAndCount[2]'])
def glPathGlyphIndexRangeNV(fontTarget, fontName, fontStyle, pathParameterTemplate, emScale, baseAndCount[2]):
	pass


@params(api='gles2', prms=['firstPathName', 'fontTarget', 'fontName', 'fontStyle', 'firstGlyphIndex', 'numGlyphs', 'pathParameterTemplate', 'emScale'])
def glPathGlyphIndexArrayNV(firstPathName, fontTarget, fontName, fontStyle, firstGlyphIndex, numGlyphs, pathParameterTemplate, emScale):
	pass


@params(api='gles2', prms=['firstPathName', 'fontTarget', 'fontSize', 'fontData', 'faceIndex', 'firstGlyphIndex', 'numGlyphs', 'pathParameterTemplate', 'emScale'])
def glPathMemoryGlyphIndexArrayNV(firstPathName, fontTarget, fontSize, fontData, faceIndex, firstGlyphIndex, numGlyphs, pathParameterTemplate, emScale):
	pass


@params(api='gles2', prms=['program', 'location', 'genMode', 'components', 'coeffs'])
def glProgramPathFragmentInputGenNV(program, location, genMode, components, coeffs):
	pass


@params(api='gles2', prms=['program', 'programInterface', 'index', 'propCount', 'props', 'bufSize', 'length', 'params'])
def glGetProgramResourcefvNV(program, programInterface, index, propCount, props, bufSize, length):
	pass


@params(api='gles2', prms=['color', 'genMode', 'colorFormat', 'coeffs'])
def glPathColorGenNV(color, genMode, colorFormat, coeffs):
	pass


@params(api='gles2', prms=['texCoordSet', 'genMode', 'components', 'coeffs'])
def glPathTexGenNV(texCoordSet, genMode, components, coeffs):
	pass


@params(api='gles2', prms=['genMode'])
def glPathFogGenNV(genMode):
	pass


@params(api='gles2', prms=['color', 'pname', 'value'])
def glGetPathColorGenivNV(color, pname, value):
	pass


@params(api='gles2', prms=['color', 'pname', 'value'])
def glGetPathColorGenfvNV(color, pname, value):
	pass


@params(api='gles2', prms=['texCoordSet', 'pname', 'value'])
def glGetPathTexGenivNV(texCoordSet, pname, value):
	pass


@params(api='gles2', prms=['texCoordSet', 'pname', 'value'])
def glGetPathTexGenfvNV(texCoordSet, pname, value):
	pass


