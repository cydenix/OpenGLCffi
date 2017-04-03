from OpenGLCffi.GL import params
@params('range', api='gl')
def glGenPathsNV(range):
	pass


@params('path', 'range', api='gl')
def glDeletePathsNV(path, range):
	pass


@params('path', api='gl')
def glIsPathNV(path):
	pass


@params('path', 'numCommands', 'commands', 'numCoords', 'coordType', 'coords', api='gl')
def glPathCommandsNV(path, numCommands, commands, numCoords, coordType, coords):
	pass


@params('path', 'numCoords', 'coordType', 'coords', api='gl')
def glPathCoordsNV(path, numCoords, coordType, coords):
	pass


@params('path', 'commandStart', 'commandsToDelete', 'numCommands', 'commands', 'numCoords', 'coordType', 'coords', api='gl')
def glPathSubCommandsNV(path, commandStart, commandsToDelete, numCommands, commands, numCoords, coordType, coords):
	pass


@params('path', 'coordStart', 'numCoords', 'coordType', 'coords', api='gl')
def glPathSubCoordsNV(path, coordStart, numCoords, coordType, coords):
	pass


@params('path', 'format', 'length', 'pathString', api='gl')
def glPathStringNV(path, format, length, pathString):
	pass


@params('firstPathName', 'fontTarget', 'fontName', 'fontStyle', 'numGlyphs', 'type', 'charcodes', 'handleMissingGlyphs', 'pathParameterTemplate', 'emScale', api='gl')
def glPathGlyphsNV(firstPathName, fontTarget, fontName, fontStyle, numGlyphs, type, charcodes, handleMissingGlyphs, pathParameterTemplate, emScale):
	pass


@params('firstPathName', 'fontTarget', 'fontName', 'fontStyle', 'firstGlyph', 'numGlyphs', 'handleMissingGlyphs', 'pathParameterTemplate', 'emScale', api='gl')
def glPathGlyphRangeNV(firstPathName, fontTarget, fontName, fontStyle, firstGlyph, numGlyphs, handleMissingGlyphs, pathParameterTemplate, emScale):
	pass


@params('resultPath', 'numPaths', 'paths', 'weights', api='gl')
def glWeightPathsNV(resultPath, numPaths, paths, weights):
	pass


@params('resultPath', 'srcPath', api='gl')
def glCopyPathNV(resultPath, srcPath):
	pass


@params('resultPath', 'pathA', 'pathB', 'weight', api='gl')
def glInterpolatePathsNV(resultPath, pathA, pathB, weight):
	pass


@params('resultPath', 'srcPath', 'transformType', 'transformValues', api='gl')
def glTransformPathNV(resultPath, srcPath, transformType, transformValues):
	pass


@params('path', 'pname', 'value', api='gl')
def glPathParameterivNV(path, pname, value):
	pass


@params('path', 'pname', 'value', api='gl')
def glPathParameteriNV(path, pname, value):
	pass


@params('path', 'pname', 'value', api='gl')
def glPathParameterfvNV(path, pname, value):
	pass


@params('path', 'pname', 'value', api='gl')
def glPathParameterfNV(path, pname, value):
	pass


@params('path', 'dashCount', 'dashArray', api='gl')
def glPathDashArrayNV(path, dashCount, dashArray):
	pass


@params('func', 'ref', 'mask', api='gl')
def glPathStencilFuncNV(func, ref, mask):
	pass


@params('factor', 'units', api='gl')
def glPathStencilDepthOffsetNV(factor, units):
	pass


@params('path', 'fillMode', 'mask', api='gl')
def glStencilFillPathNV(path, fillMode, mask):
	pass


@params('path', 'reference', 'mask', api='gl')
def glStencilStrokePathNV(path, reference, mask):
	pass


@params('numPaths', 'pathNameType', 'paths', 'pathBase', 'fillMode', 'mask', 'transformType', 'transformValues', api='gl')
def glStencilFillPathInstancedNV(numPaths, pathNameType, paths, pathBase, fillMode, mask, transformType, transformValues):
	pass


@params('numPaths', 'pathNameType', 'paths', 'pathBase', 'reference', 'mask', 'transformType', 'transformValues', api='gl')
def glStencilStrokePathInstancedNV(numPaths, pathNameType, paths, pathBase, reference, mask, transformType, transformValues):
	pass


@params('func', api='gl')
def glPathCoverDepthFuncNV(func):
	pass


@params('path', 'coverMode', api='gl')
def glCoverFillPathNV(path, coverMode):
	pass


@params('path', 'coverMode', api='gl')
def glCoverStrokePathNV(path, coverMode):
	pass


@params('numPaths', 'pathNameType', 'paths', 'pathBase', 'coverMode', 'transformType', 'transformValues', api='gl')
def glCoverFillPathInstancedNV(numPaths, pathNameType, paths, pathBase, coverMode, transformType, transformValues):
	pass


@params('numPaths', 'pathNameType', 'paths', 'pathBase', 'coverMode', 'transformType', 'transformValues', api='gl')
def glCoverStrokePathInstancedNV(numPaths, pathNameType, paths, pathBase, coverMode, transformType, transformValues):
	pass


@params('path', 'pname', 'value', api='gl')
def glGetPathParameterivNV(path, pname, value):
	pass


@params('path', 'pname', 'value', api='gl')
def glGetPathParameterfvNV(path, pname, value):
	pass


@params('path', 'commands', api='gl')
def glGetPathCommandsNV(path, commands):
	pass


@params('path', 'coords', api='gl')
def glGetPathCoordsNV(path, coords):
	pass


@params('path', 'dashArray', api='gl')
def glGetPathDashArrayNV(path, dashArray):
	pass


@params('metricQueryMask', 'numPaths', 'pathNameType', 'paths', 'pathBase', 'stride', 'metrics', api='gl')
def glGetPathMetricsNV(metricQueryMask, numPaths, pathNameType, paths, pathBase, stride, metrics):
	pass


@params('metricQueryMask', 'firstPathName', 'numPaths', 'stride', 'metrics', api='gl')
def glGetPathMetricRangeNV(metricQueryMask, firstPathName, numPaths, stride, metrics):
	pass


@params('pathListMode', 'numPaths', 'pathNameType', 'paths', 'pathBase', 'advanceScale', 'kerningScale', 'transformType', 'returnedSpacing', api='gl')
def glGetPathSpacingNV(pathListMode, numPaths, pathNameType, paths, pathBase, advanceScale, kerningScale, transformType, returnedSpacing):
	pass


@params('path', 'mask', 'x', 'y', api='gl')
def glIsPointInFillPathNV(path, mask, x, y):
	pass


@params('path', 'x', 'y', api='gl')
def glIsPointInStrokePathNV(path, x, y):
	pass


@params('path', 'startSegment', 'numSegments', api='gl')
def glGetPathLengthNV(path, startSegment, numSegments):
	pass


@params('path', 'startSegment', 'numSegments', 'distance', 'x', 'y', 'tangentX', 'tangentY', api='gl')
def glPointAlongPathNV(path, startSegment, numSegments, distance, x, y, tangentX, tangentY):
	pass


@params('matrixMode', 'm', api='gl')
def glMatrixLoad3x2fNV(matrixMode, m):
	pass


@params('matrixMode', 'm', api='gl')
def glMatrixLoad3x3fNV(matrixMode, m):
	pass


@params('matrixMode', 'm', api='gl')
def glMatrixLoadTranspose3x3fNV(matrixMode, m):
	pass


@params('matrixMode', 'm', api='gl')
def glMatrixMult3x2fNV(matrixMode, m):
	pass


@params('matrixMode', 'm', api='gl')
def glMatrixMult3x3fNV(matrixMode, m):
	pass


@params('matrixMode', 'm', api='gl')
def glMatrixMultTranspose3x3fNV(matrixMode, m):
	pass


@params('path', 'fillMode', 'mask', 'coverMode', api='gl')
def glStencilThenCoverFillPathNV(path, fillMode, mask, coverMode):
	pass


@params('path', 'reference', 'mask', 'coverMode', api='gl')
def glStencilThenCoverStrokePathNV(path, reference, mask, coverMode):
	pass


@params('numPaths', 'pathNameType', 'paths', 'pathBase', 'fillMode', 'mask', 'coverMode', 'transformType', 'transformValues', api='gl')
def glStencilThenCoverFillPathInstancedNV(numPaths, pathNameType, paths, pathBase, fillMode, mask, coverMode, transformType, transformValues):
	pass


@params('numPaths', 'pathNameType', 'paths', 'pathBase', 'reference', 'mask', 'coverMode', 'transformType', 'transformValues', api='gl')
def glStencilThenCoverStrokePathInstancedNV(numPaths, pathNameType, paths, pathBase, reference, mask, coverMode, transformType, transformValues):
	pass


@params('fontTarget', 'fontName', 'fontStyle', 'pathParameterTemplate', 'emScale', 'baseAndCount[2]', api='gl')
def glPathGlyphIndexRangeNV(fontTarget, fontName, fontStyle, pathParameterTemplate, emScale, baseAndCount[2]):
	pass


@params('firstPathName', 'fontTarget', 'fontName', 'fontStyle', 'firstGlyphIndex', 'numGlyphs', 'pathParameterTemplate', 'emScale', api='gl')
def glPathGlyphIndexArrayNV(firstPathName, fontTarget, fontName, fontStyle, firstGlyphIndex, numGlyphs, pathParameterTemplate, emScale):
	pass


@params('firstPathName', 'fontTarget', 'fontSize', 'fontData', 'faceIndex', 'firstGlyphIndex', 'numGlyphs', 'pathParameterTemplate', 'emScale', api='gl')
def glPathMemoryGlyphIndexArrayNV(firstPathName, fontTarget, fontSize, fontData, faceIndex, firstGlyphIndex, numGlyphs, pathParameterTemplate, emScale):
	pass


@params('program', 'location', 'genMode', 'components', 'coeffs', api='gl')
def glProgramPathFragmentInputGenNV(program, location, genMode, components, coeffs):
	pass


@params('program', 'programInterface', 'index', 'propCount', 'props', 'bufSize', 'length', 'params', api='gl')
def glGetProgramResourcefvNV(program, programInterface, index, propCount, props, bufSize, length, params):
	pass


@params('color', 'genMode', 'colorFormat', 'coeffs', api='gl')
def glPathColorGenNV(color, genMode, colorFormat, coeffs):
	pass


@params('texCoordSet', 'genMode', 'components', 'coeffs', api='gl')
def glPathTexGenNV(texCoordSet, genMode, components, coeffs):
	pass


@params('genMode', api='gl')
def glPathFogGenNV(genMode):
	pass


@params('color', 'pname', 'value', api='gl')
def glGetPathColorGenivNV(color, pname, value):
	pass


@params('color', 'pname', 'value', api='gl')
def glGetPathColorGenfvNV(color, pname, value):
	pass


@params('texCoordSet', 'pname', 'value', api='gl')
def glGetPathTexGenivNV(texCoordSet, pname, value):
	pass


@params('texCoordSet', 'pname', 'value', api='gl')
def glGetPathTexGenfvNV(texCoordSet, pname, value):
	pass


