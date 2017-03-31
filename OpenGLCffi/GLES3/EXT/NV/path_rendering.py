@params('range', api='gles3')
def glGenPathsNV():
	pass


@params('path', 'range', api='gles3')
def glDeletePathsNV(path, range):
	pass


@params('path', api='gles3')
def glIsPathNV(path):
	pass


@params('path', 'numCommands', 'commands', 'numCoords', 'coordType', 'coords', api='gles3')
def glPathCommandsNV(path, numCommands, commands, numCoords, coordType, coords):
	pass


@params('path', 'numCoords', 'coordType', 'coords', api='gles3')
def glPathCoordsNV(path, numCoords, coordType, coords):
	pass


@params('path', 'commandStart', 'commandsToDelete', 'numCommands', 'commands', 'numCoords', 'coordType', 'coords', api='gles3')
def glPathSubCommandsNV(path, commandStart, commandsToDelete, numCommands, commands, numCoords, coordType, coords):
	pass


@params('path', 'coordStart', 'numCoords', 'coordType', 'coords', api='gles3')
def glPathSubCoordsNV(path, coordStart, numCoords, coordType, coords):
	pass


@params('path', 'format', 'length', 'pathString', api='gles3')
def glPathStringNV(path, format, length, pathString):
	pass


@params('firstPathName', 'fontTarget', 'fontName', 'fontStyle', 'numGlyphs', 'type', 'charcodes', 'handleMissingGlyphs', 'pathParameterTemplate', 'emScale', api='gles3')
def glPathGlyphsNV(firstPathName, fontTarget, fontName, fontStyle, numGlyphs, type, charcodes, handleMissingGlyphs, pathParameterTemplate, emScale):
	pass


@params('firstPathName', 'fontTarget', 'fontName', 'fontStyle', 'firstGlyph', 'numGlyphs', 'handleMissingGlyphs', 'pathParameterTemplate', 'emScale', api='gles3')
def glPathGlyphRangeNV(firstPathName, fontTarget, fontName, fontStyle, firstGlyph, numGlyphs, handleMissingGlyphs, pathParameterTemplate, emScale):
	pass


@params('resultPath', 'numPaths', 'paths', 'weights', api='gles3')
def glWeightPathsNV(resultPath, numPaths, paths, weights):
	pass


@params('resultPath', 'srcPath', api='gles3')
def glCopyPathNV(resultPath, srcPath):
	pass


@params('resultPath', 'pathA', 'pathB', 'weight', api='gles3')
def glInterpolatePathsNV(resultPath, pathA, pathB, weight):
	pass


@params('resultPath', 'srcPath', 'transformType', 'transformValues', api='gles3')
def glTransformPathNV(resultPath, srcPath, transformType, transformValues):
	pass


@params('path', 'pname', 'value', api='gles3')
def glPathParameterivNV(path, pname, value):
	pass


@params('path', 'pname', 'value', api='gles3')
def glPathParameteriNV(path, pname, value):
	pass


@params('path', 'pname', 'value', api='gles3')
def glPathParameterfvNV(path, pname, value):
	pass


@params('path', 'pname', 'value', api='gles3')
def glPathParameterfNV(path, pname, value):
	pass


@params('path', 'dashCount', 'dashArray', api='gles3')
def glPathDashArrayNV(path, dashCount, dashArray):
	pass


@params('func', 'ref', 'mask', api='gles3')
def glPathStencilFuncNV(func, ref, mask):
	pass


@params('factor', 'units', api='gles3')
def glPathStencilDepthOffsetNV(factor, units):
	pass


@params('path', 'fillMode', 'mask', api='gles3')
def glStencilFillPathNV(path, fillMode, mask):
	pass


@params('path', 'reference', 'mask', api='gles3')
def glStencilStrokePathNV(path, reference, mask):
	pass


@params('numPaths', 'pathNameType', 'paths', 'pathBase', 'fillMode', 'mask', 'transformType', 'transformValues', api='gles3')
def glStencilFillPathInstancedNV(numPaths, pathNameType, paths, pathBase, fillMode, mask, transformType, transformValues):
	pass


@params('numPaths', 'pathNameType', 'paths', 'pathBase', 'reference', 'mask', 'transformType', 'transformValues', api='gles3')
def glStencilStrokePathInstancedNV(numPaths, pathNameType, paths, pathBase, reference, mask, transformType, transformValues):
	pass


@params('func', api='gles3')
def glPathCoverDepthFuncNV(func):
	pass


@params('path', 'coverMode', api='gles3')
def glCoverFillPathNV(path, coverMode):
	pass


@params('path', 'coverMode', api='gles3')
def glCoverStrokePathNV(path, coverMode):
	pass


@params('numPaths', 'pathNameType', 'paths', 'pathBase', 'coverMode', 'transformType', 'transformValues', api='gles3')
def glCoverFillPathInstancedNV(numPaths, pathNameType, paths, pathBase, coverMode, transformType, transformValues):
	pass


@params('numPaths', 'pathNameType', 'paths', 'pathBase', 'coverMode', 'transformType', 'transformValues', api='gles3')
def glCoverStrokePathInstancedNV(numPaths, pathNameType, paths, pathBase, coverMode, transformType, transformValues):
	pass


@params('path', 'pname', 'value', api='gles3')
def glGetPathParameterivNV(path, pname, value):
	pass


@params('path', 'pname', 'value', api='gles3')
def glGetPathParameterfvNV(path, pname, value):
	pass


@params('path', 'commands', api='gles3')
def glGetPathCommandsNV(path, commands):
	pass


@params('path', 'coords', api='gles3')
def glGetPathCoordsNV(path, coords):
	pass


@params('path', 'dashArray', api='gles3')
def glGetPathDashArrayNV(path, dashArray):
	pass


@params('metricQueryMask', 'numPaths', 'pathNameType', 'paths', 'pathBase', 'stride', 'metrics', api='gles3')
def glGetPathMetricsNV(metricQueryMask, numPaths, pathNameType, paths, pathBase, stride, metrics):
	pass


@params('metricQueryMask', 'firstPathName', 'numPaths', 'stride', 'metrics', api='gles3')
def glGetPathMetricRangeNV(metricQueryMask, firstPathName, numPaths, stride, metrics):
	pass


@params('pathListMode', 'numPaths', 'pathNameType', 'paths', 'pathBase', 'advanceScale', 'kerningScale', 'transformType', 'returnedSpacing', api='gles3')
def glGetPathSpacingNV(pathListMode, numPaths, pathNameType, paths, pathBase, advanceScale, kerningScale, transformType, returnedSpacing):
	pass


@params('path', 'mask', 'x', 'y', api='gles3')
def glIsPointInFillPathNV(path, mask, x, y):
	pass


@params('path', 'x', 'y', api='gles3')
def glIsPointInStrokePathNV(path, x, y):
	pass


@params('path', 'startSegment', 'numSegments', api='gles3')
def glGetPathLengthNV(path, startSegment, numSegments):
	pass


@params('path', 'startSegment', 'numSegments', 'distance', 'x', 'y', 'tangentX', 'tangentY', api='gles3')
def glPointAlongPathNV(path, startSegment, numSegments, distance, x, y, tangentX, tangentY):
	pass


@params('matrixMode', 'm', api='gles3')
def glMatrixLoad3x2fNV(matrixMode, m):
	pass


@params('matrixMode', 'm', api='gles3')
def glMatrixLoad3x3fNV(matrixMode, m):
	pass


@params('matrixMode', 'm', api='gles3')
def glMatrixLoadTranspose3x3fNV(matrixMode, m):
	pass


@params('matrixMode', 'm', api='gles3')
def glMatrixMult3x2fNV(matrixMode, m):
	pass


@params('matrixMode', 'm', api='gles3')
def glMatrixMult3x3fNV(matrixMode, m):
	pass


@params('matrixMode', 'm', api='gles3')
def glMatrixMultTranspose3x3fNV(matrixMode, m):
	pass


@params('path', 'fillMode', 'mask', 'coverMode', api='gles3')
def glStencilThenCoverFillPathNV(path, fillMode, mask, coverMode):
	pass


@params('path', 'reference', 'mask', 'coverMode', api='gles3')
def glStencilThenCoverStrokePathNV(path, reference, mask, coverMode):
	pass


@params('numPaths', 'pathNameType', 'paths', 'pathBase', 'fillMode', 'mask', 'coverMode', 'transformType', 'transformValues', api='gles3')
def glStencilThenCoverFillPathInstancedNV(numPaths, pathNameType, paths, pathBase, fillMode, mask, coverMode, transformType, transformValues):
	pass


@params('numPaths', 'pathNameType', 'paths', 'pathBase', 'reference', 'mask', 'coverMode', 'transformType', 'transformValues', api='gles3')
def glStencilThenCoverStrokePathInstancedNV(numPaths, pathNameType, paths, pathBase, reference, mask, coverMode, transformType, transformValues):
	pass


@params('fontTarget', 'fontName', 'fontStyle', 'pathParameterTemplate', 'emScale', 'baseAndCount[2]', api='gles3')
def glPathGlyphIndexRangeNV(fontTarget, fontName, fontStyle, pathParameterTemplate, emScale, baseAndCount[2]):
	pass


@params('firstPathName', 'fontTarget', 'fontName', 'fontStyle', 'firstGlyphIndex', 'numGlyphs', 'pathParameterTemplate', 'emScale', api='gles3')
def glPathGlyphIndexArrayNV(firstPathName, fontTarget, fontName, fontStyle, firstGlyphIndex, numGlyphs, pathParameterTemplate, emScale):
	pass


@params('firstPathName', 'fontTarget', 'fontSize', 'fontData', 'faceIndex', 'firstGlyphIndex', 'numGlyphs', 'pathParameterTemplate', 'emScale', api='gles3')
def glPathMemoryGlyphIndexArrayNV(firstPathName, fontTarget, fontSize, fontData, faceIndex, firstGlyphIndex, numGlyphs, pathParameterTemplate, emScale):
	pass


@params('program', 'location', 'genMode', 'components', 'coeffs', api='gles3')
def glProgramPathFragmentInputGenNV(program, location, genMode, components, coeffs):
	pass


@params('program', 'programInterface', 'index', 'propCount', 'props', 'bufSize', 'length', 'params', api='gles3')
def glGetProgramResourcefvNV(program, programInterface, index, props, bufSize, length):
	pass


@params('color', 'genMode', 'colorFormat', 'coeffs', api='gles3')
def glPathColorGenNV(color, genMode, colorFormat, coeffs):
	pass


@params('texCoordSet', 'genMode', 'components', 'coeffs', api='gles3')
def glPathTexGenNV(texCoordSet, genMode, components, coeffs):
	pass


@params('genMode', api='gles3')
def glPathFogGenNV(genMode):
	pass


@params('color', 'pname', 'value', api='gles3')
def glGetPathColorGenivNV(color, pname, value):
	pass


@params('color', 'pname', 'value', api='gles3')
def glGetPathColorGenfvNV(color, pname, value):
	pass


@params('texCoordSet', 'pname', 'value', api='gles3')
def glGetPathTexGenivNV(texCoordSet, pname, value):
	pass


@params('texCoordSet', 'pname', 'value', api='gles3')
def glGetPathTexGenfvNV(texCoordSet, pname, value):
	pass


