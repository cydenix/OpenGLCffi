@params('range', api='gles2')
def glGenPathsNV():
	pass


@params('path', 'range', api='gles2')
def glDeletePathsNV(path, range):
	pass


@params('path', api='gles2')
def glIsPathNV(path):
	pass


@params('path', 'numCommands', 'commands', 'numCoords', 'coordType', 'coords', api='gles2')
def glPathCommandsNV(path, numCommands, commands, numCoords, coordType, coords):
	pass


@params('path', 'numCoords', 'coordType', 'coords', api='gles2')
def glPathCoordsNV(path, numCoords, coordType, coords):
	pass


@params('path', 'commandStart', 'commandsToDelete', 'numCommands', 'commands', 'numCoords', 'coordType', 'coords', api='gles2')
def glPathSubCommandsNV(path, commandStart, commandsToDelete, numCommands, commands, numCoords, coordType, coords):
	pass


@params('path', 'coordStart', 'numCoords', 'coordType', 'coords', api='gles2')
def glPathSubCoordsNV(path, coordStart, numCoords, coordType, coords):
	pass


@params('path', 'format', 'length', 'pathString', api='gles2')
def glPathStringNV(path, format, length, pathString):
	pass


@params('firstPathName', 'fontTarget', 'fontName', 'fontStyle', 'numGlyphs', 'type', 'charcodes', 'handleMissingGlyphs', 'pathParameterTemplate', 'emScale', api='gles2')
def glPathGlyphsNV(firstPathName, fontTarget, fontName, fontStyle, numGlyphs, type, charcodes, handleMissingGlyphs, pathParameterTemplate, emScale):
	pass


@params('firstPathName', 'fontTarget', 'fontName', 'fontStyle', 'firstGlyph', 'numGlyphs', 'handleMissingGlyphs', 'pathParameterTemplate', 'emScale', api='gles2')
def glPathGlyphRangeNV(firstPathName, fontTarget, fontName, fontStyle, firstGlyph, numGlyphs, handleMissingGlyphs, pathParameterTemplate, emScale):
	pass


@params('resultPath', 'numPaths', 'paths', 'weights', api='gles2')
def glWeightPathsNV(resultPath, numPaths, paths, weights):
	pass


@params('resultPath', 'srcPath', api='gles2')
def glCopyPathNV(resultPath, srcPath):
	pass


@params('resultPath', 'pathA', 'pathB', 'weight', api='gles2')
def glInterpolatePathsNV(resultPath, pathA, pathB, weight):
	pass


@params('resultPath', 'srcPath', 'transformType', 'transformValues', api='gles2')
def glTransformPathNV(resultPath, srcPath, transformType, transformValues):
	pass


@params('path', 'pname', 'value', api='gles2')
def glPathParameterivNV(path, pname, value):
	pass


@params('path', 'pname', 'value', api='gles2')
def glPathParameteriNV(path, pname, value):
	pass


@params('path', 'pname', 'value', api='gles2')
def glPathParameterfvNV(path, pname, value):
	pass


@params('path', 'pname', 'value', api='gles2')
def glPathParameterfNV(path, pname, value):
	pass


@params('path', 'dashCount', 'dashArray', api='gles2')
def glPathDashArrayNV(path, dashCount, dashArray):
	pass


@params('func', 'ref', 'mask', api='gles2')
def glPathStencilFuncNV(func, ref, mask):
	pass


@params('factor', 'units', api='gles2')
def glPathStencilDepthOffsetNV(factor, units):
	pass


@params('path', 'fillMode', 'mask', api='gles2')
def glStencilFillPathNV(path, fillMode, mask):
	pass


@params('path', 'reference', 'mask', api='gles2')
def glStencilStrokePathNV(path, reference, mask):
	pass


@params('numPaths', 'pathNameType', 'paths', 'pathBase', 'fillMode', 'mask', 'transformType', 'transformValues', api='gles2')
def glStencilFillPathInstancedNV(numPaths, pathNameType, paths, pathBase, fillMode, mask, transformType, transformValues):
	pass


@params('numPaths', 'pathNameType', 'paths', 'pathBase', 'reference', 'mask', 'transformType', 'transformValues', api='gles2')
def glStencilStrokePathInstancedNV(numPaths, pathNameType, paths, pathBase, reference, mask, transformType, transformValues):
	pass


@params('func', api='gles2')
def glPathCoverDepthFuncNV(func):
	pass


@params('path', 'coverMode', api='gles2')
def glCoverFillPathNV(path, coverMode):
	pass


@params('path', 'coverMode', api='gles2')
def glCoverStrokePathNV(path, coverMode):
	pass


@params('numPaths', 'pathNameType', 'paths', 'pathBase', 'coverMode', 'transformType', 'transformValues', api='gles2')
def glCoverFillPathInstancedNV(numPaths, pathNameType, paths, pathBase, coverMode, transformType, transformValues):
	pass


@params('numPaths', 'pathNameType', 'paths', 'pathBase', 'coverMode', 'transformType', 'transformValues', api='gles2')
def glCoverStrokePathInstancedNV(numPaths, pathNameType, paths, pathBase, coverMode, transformType, transformValues):
	pass


@params('path', 'pname', 'value', api='gles2')
def glGetPathParameterivNV(path, pname, value):
	pass


@params('path', 'pname', 'value', api='gles2')
def glGetPathParameterfvNV(path, pname, value):
	pass


@params('path', 'commands', api='gles2')
def glGetPathCommandsNV(path, commands):
	pass


@params('path', 'coords', api='gles2')
def glGetPathCoordsNV(path, coords):
	pass


@params('path', 'dashArray', api='gles2')
def glGetPathDashArrayNV(path, dashArray):
	pass


@params('metricQueryMask', 'numPaths', 'pathNameType', 'paths', 'pathBase', 'stride', 'metrics', api='gles2')
def glGetPathMetricsNV(metricQueryMask, numPaths, pathNameType, paths, pathBase, stride, metrics):
	pass


@params('metricQueryMask', 'firstPathName', 'numPaths', 'stride', 'metrics', api='gles2')
def glGetPathMetricRangeNV(metricQueryMask, firstPathName, numPaths, stride, metrics):
	pass


@params('pathListMode', 'numPaths', 'pathNameType', 'paths', 'pathBase', 'advanceScale', 'kerningScale', 'transformType', 'returnedSpacing', api='gles2')
def glGetPathSpacingNV(pathListMode, numPaths, pathNameType, paths, pathBase, advanceScale, kerningScale, transformType, returnedSpacing):
	pass


@params('path', 'mask', 'x', 'y', api='gles2')
def glIsPointInFillPathNV(path, mask, x, y):
	pass


@params('path', 'x', 'y', api='gles2')
def glIsPointInStrokePathNV(path, x, y):
	pass


@params('path', 'startSegment', 'numSegments', api='gles2')
def glGetPathLengthNV(path, startSegment, numSegments):
	pass


@params('path', 'startSegment', 'numSegments', 'distance', 'x', 'y', 'tangentX', 'tangentY', api='gles2')
def glPointAlongPathNV(path, startSegment, numSegments, distance, x, y, tangentX, tangentY):
	pass


@params('matrixMode', 'm', api='gles2')
def glMatrixLoad3x2fNV(matrixMode, m):
	pass


@params('matrixMode', 'm', api='gles2')
def glMatrixLoad3x3fNV(matrixMode, m):
	pass


@params('matrixMode', 'm', api='gles2')
def glMatrixLoadTranspose3x3fNV(matrixMode, m):
	pass


@params('matrixMode', 'm', api='gles2')
def glMatrixMult3x2fNV(matrixMode, m):
	pass


@params('matrixMode', 'm', api='gles2')
def glMatrixMult3x3fNV(matrixMode, m):
	pass


@params('matrixMode', 'm', api='gles2')
def glMatrixMultTranspose3x3fNV(matrixMode, m):
	pass


@params('path', 'fillMode', 'mask', 'coverMode', api='gles2')
def glStencilThenCoverFillPathNV(path, fillMode, mask, coverMode):
	pass


@params('path', 'reference', 'mask', 'coverMode', api='gles2')
def glStencilThenCoverStrokePathNV(path, reference, mask, coverMode):
	pass


@params('numPaths', 'pathNameType', 'paths', 'pathBase', 'fillMode', 'mask', 'coverMode', 'transformType', 'transformValues', api='gles2')
def glStencilThenCoverFillPathInstancedNV(numPaths, pathNameType, paths, pathBase, fillMode, mask, coverMode, transformType, transformValues):
	pass


@params('numPaths', 'pathNameType', 'paths', 'pathBase', 'reference', 'mask', 'coverMode', 'transformType', 'transformValues', api='gles2')
def glStencilThenCoverStrokePathInstancedNV(numPaths, pathNameType, paths, pathBase, reference, mask, coverMode, transformType, transformValues):
	pass


@params('fontTarget', 'fontName', 'fontStyle', 'pathParameterTemplate', 'emScale', 'baseAndCount[2]', api='gles2')
def glPathGlyphIndexRangeNV(fontTarget, fontName, fontStyle, pathParameterTemplate, emScale, baseAndCount[2]):
	pass


@params('firstPathName', 'fontTarget', 'fontName', 'fontStyle', 'firstGlyphIndex', 'numGlyphs', 'pathParameterTemplate', 'emScale', api='gles2')
def glPathGlyphIndexArrayNV(firstPathName, fontTarget, fontName, fontStyle, firstGlyphIndex, numGlyphs, pathParameterTemplate, emScale):
	pass


@params('firstPathName', 'fontTarget', 'fontSize', 'fontData', 'faceIndex', 'firstGlyphIndex', 'numGlyphs', 'pathParameterTemplate', 'emScale', api='gles2')
def glPathMemoryGlyphIndexArrayNV(firstPathName, fontTarget, fontSize, fontData, faceIndex, firstGlyphIndex, numGlyphs, pathParameterTemplate, emScale):
	pass


@params('program', 'location', 'genMode', 'components', 'coeffs', api='gles2')
def glProgramPathFragmentInputGenNV(program, location, genMode, components, coeffs):
	pass


@params('program', 'programInterface', 'index', 'propCount', 'props', 'bufSize', 'length', 'params', api='gles2')
def glGetProgramResourcefvNV(program, programInterface, index, propCount, props, bufSize, length):
	pass


@params('color', 'genMode', 'colorFormat', 'coeffs', api='gles2')
def glPathColorGenNV(color, genMode, colorFormat, coeffs):
	pass


@params('texCoordSet', 'genMode', 'components', 'coeffs', api='gles2')
def glPathTexGenNV(texCoordSet, genMode, components, coeffs):
	pass


@params('genMode', api='gles2')
def glPathFogGenNV(genMode):
	pass


@params('color', 'pname', 'value', api='gles2')
def glGetPathColorGenivNV(color, pname, value):
	pass


@params('color', 'pname', 'value', api='gles2')
def glGetPathColorGenfvNV(color, pname, value):
	pass


@params('texCoordSet', 'pname', 'value', api='gles2')
def glGetPathTexGenivNV(texCoordSet, pname, value):
	pass


@params('texCoordSet', 'pname', 'value', api='gles2')
def glGetPathTexGenfvNV(texCoordSet, pname, value):
	pass


