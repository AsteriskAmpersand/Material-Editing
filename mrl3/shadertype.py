from collections import OrderedDict
from common.crc import CrcJamcrc
from common.Cstruct import ExtendedPyCStruct as EPyCStruct
from common.Cstruct import Mod3Container, Mod3Collection

if __name__=="__main__":
    import sys, inspect
    fieldTypes = set()
    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(obj):
            try:
                fieldTypes.union(set(obj.fields.values()))
            except:
                pass
    print(fieldTypes)


class CBSnowFieldBake(EPyCStruct):
	fields = OrderedDict([


		("iSnowFieldBakeAttr", "uint"),

	])


class CBUpdateBufferFromMesh(EPyCStruct):
	fields = OrderedDict([


		("iVertexNum", "uint"),
		("iVertexBufferOffset", "uint"),
		("iVertexStride", "uint"),
		("iVertexBaseOffset", "uint"),
		("iInputLayoutOffset0", "uint4"),
		("iInputLayoutOffset1", "uint4"),
		("iInputLayoutOffset2", "uint4"),

	])


class CBMhMaterialUberLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fTranslucency__uiUNorm", "float"),
		("bBaseColorEmissive", "bbool"),
		("fAnimEmitMin", "float"),
		("fAnimEmitSpeed", "float"),
		("fAnimEmitWave", "float"),
		("bUseWaveEmit", "bbool"),
		("bUseWaveAlpha", "bbool"),
		("bUseCMM", "bbool"),
		("fAddColorA__uiColor", "float4"),
		("fAddColorB__uiColor", "float4"),
		("fAddColorC__uiColor", "float4"),
		("fAddColorD__uiColor", "float4"),
		("fFurParam__uiUNorm", "float4"),
		("fFurTile", "float"),
		("fSecondaryEmitColor__uiColor", "float3"),
		("fSecondaryEmit_Control", "float4"),
		("fFilmThickness__uiUNorm", "float"),
		("fFilmBlend__uiUNorm", "float"),
		("fFilmIOR__uiUNorm", "float"),

		("align0", "ubyte[4]"),
		("fEmissiveBlendColor__uiColor", "float3"),
		("fEmissiveBlendColorBlend__uiUNorm", "float"),
		("fEmissiveBlendRimParam", "float3"),
		("fRefraction__uiSNorm", "float"),
		("fRefractionRotation__uiSNorm", "float"),
		("fPanoramaTile", "float"),
		("fVPushScale", "float"),
		("fVPushWave", "float"),
		("fVPushSpeed", "float"),
		("bUseFlipUV", "bbool"),
		("bBackFaceNormalFilp", "bbool"),
		("bUseEmitMask", "bbool"),
		("bUseRoughColor", "bbool"),
		("fRoughMask__uiUNorm", "float2"),
		("bUsePaint", "bbool"),
		("fPaintMapRC", "float2"),
		("fPaintMapNum", "float"),

		("align1", "ubyte[4]"),
		("fPaintMapOffset__uiSNorm", "float4"),
		("fPaintColor__uiColor", "float4"),
		("fPaintRoughness__uiUNorm", "float"),
		("fPaintMetal__uiUNorm", "float"),
		("bUseOffset", "bbool"),
		("fInnerOffsetScale", "float"),
		("bUseFly", "bbool"),
		("iWingNum", "uint"),
		("bUseAnimAlpha", "bbool"),
		("fAnimAlphaSpeed", "float"),
		("fSnowControl", "float4"),
		("fMaterialSnowBlendA", "float"),
		("fMaterialSnowBlendB", "float"),
		("fSnowTile", "float"),

		("align2", "ubyte[4]"),
		("fSnowColor__uiColor", "float3"),

		("align3", "ubyte[4]"),
		("fSnowMatControl__uiUNorm", "float4"),
		("fSnowUVOffset__uiUNorm", "float2"),
		("bUseSnowDistance", "bbool"),

	])


class CBSystemSnow(EPyCStruct):
	fields = OrderedDict([


		("bSnowFieldEnabled", "bbool"),
		("iSnowFieldDivisionNum", "uint"),

		("align0", "ubyte[8]"),
		("fSnowHeightRegion", "float4"),
		("fSnowHeightMapSize", "float4"),
		("fSnowHeightMinYRangeY", "float4"),
		("fNormalBlendRate", "float"),
		("fMaxHeightDent", "float"),
		("fMaxHeightBump", "float"),
		("fShovelEdgeBlendRate", "float"),

	])


class CBMhSky2SimpleGBuffer(EPyCStruct):
	fields = OrderedDict([


		("iSkyGBufferId", "uint"),

	])


class CBWaterMaterial(EPyCStruct):
	fields = OrderedDict([


		("fReflectionViewProj", "float4x4"),
		("fReflectionFactor", "float"),
		("fCubemapBlendRate", "float"),
		("fRefractionFactor", "float"),
		("fRefactionIndex", "float"),
		("fColExtinction", "float3"),

		("align0", "ubyte[4]"),
		("fColScatter", "float3"),
		("fScatteringCoeff", "float"),
		("fFresnelBias", "float"),
		("normalATiling", "float3"),
		("normalBTiling", "float3"),

		("align1", "ubyte[4]"),
		("normalAMoveDir", "float3"),

		("align2", "ubyte[4]"),
		("normalBMoveDir", "float3"),

		("align3", "ubyte[4]"),
		("materialTiling", "float2"),

		("align4", "ubyte[8]"),
		("materialColor", "float3"),
		("fWaterDeltaTime", "float"),
		("fDepthFadeInv", "float"),
		("iLightGroup", "uint"),
		("iFlags", "uint"),
		("fMaxDepth", "float"),
		("causticsTiling", "float3"),

		("align5", "ubyte[4]"),
		("causticsMoveDir", "float3"),
		("fCausticsDensityLow", "float"),
		("whitecapTiling", "float3"),

		("align6", "ubyte[4]"),
		("whitecapMoveDir", "float3"),
		("fWhitecapRoughness", "float"),
		("fWhitecapDepthThreshold", "float"),
		("fWhitecapDepthFade", "float"),
		("fWhitecapHeightWPosUnder", "float"),
		("fWhitecapHeightWPosThreshold", "float"),
		("fWhitecapHeightFade", "float"),
		("fWhitecapHeightPower", "float"),

	])


class CBMhMaterialVfxTornadoLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),

		("align0", "ubyte[4]"),
		("fUVTransformA", "float4"),
		("fUVTransformB", "float4"),
		("fUVTransformC", "float4"),
		("fVolumeBlend__uiSNorm", "float"),
		("fVolumeBlendDistance", "float"),

		("align1", "ubyte[8]"),
		("fRGBchFactor_uiColor", "float3"),

		("align2", "ubyte[4]"),
		("fEmissiveRGBchFactor_uiColor", "float3"),
		("fEmissivePow", "float"),
		("fEmissiveGradationPow", "float"),
		("fOpacityFactor", "float"),
		("fOpacityPow", "float"),
		("fVerticalOpacityPow", "float"),
		("fVerticalOpacityPowInv", "float"),
		("fNormalFactor__uiUNorm", "float"),
		("fDispFactor", "float"),
		("fFresnelPow", "float"),
		("fFlowSpeed", "float"),
		("fFlowStrength", "float"),
		("fUVOffsetSpeed", "float"),

		("align3", "ubyte[4]"),
		("fUVOffsetSpeedFactorA", "float2"),
		("fUVOffsetSpeedFactorB", "float2"),
		("fUVOffsetSpeedFactorC", "float2"),
		("fAngleFade", "float"),
		("fTranslucency__uiUNorm", "float"),
		("fTotalOpacity__uiUNorm", "float"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fInnerOffsetScale", "float"),
		("fVelocityAttn", "float"),
		("bGBufferIdMaskEnable", "bbool"),
		("iGBufferIdMask", "uint"),
		("fNormalDecalBlend__uiUNorm", "float"),

	])


class CBMhMaterialIvyFloorLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fWaveLength", "float"),
		("fSinkLength", "float"),
		("fLocalWindWeight", "float"),
		("bDriftIceMode", "bbool"),
		("fIceConstSinkLength", "float"),
		("fIceMaxSlant", "float"),
		("fIceSlantRange", "float"),

	])


class CBMhMaterialEM057Local__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fTranslucency__uiUNorm", "float"),
		("bBaseColorEmissive", "bbool"),
		("fPaintUVTile", "float2"),
		("fAddNormalBlend__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fAddNormalMaskA__uiSNorm", "float4"),
		("fAddNormalMaskB__uiSNorm", "float4"),
		("fAddNormalMaskC__uiUNorm", "float"),
		("fAddNormalMaskD__uiUNorm", "float"),
		("bBackFaceShading", "bbool"),
		("bBackFaceNormalFilp", "bbool"),
		("fKizuColor__uiColor", "float3"),

		("align1", "ubyte[4]"),
		("fKizuUVOffset__uiUNorm", "float2"),
		("fKizuMultiply", "float"),
		("bLegendary", "bbool"),
		("fLegendColor__uiColor", "float4"),
		("fLegendMetalMask__uiUNorm", "float2"),
		("fLegendRoughness", "float"),

		("align2", "ubyte[4]"),
		("fLegendFilm__uiUNorm", "float3"),
		("fLegendSSSMask__uiUNorm", "float"),
		("fLegendHSV__uiSNorm", "float3"),
		("fLegendFilmIOR__uiUNorm", "float"),
		("fPartsMaskA__uiUNorm", "float"),
		("fPartsMaskB__uiUNorm", "float"),
		("fPartsMaskC__uiUNorm", "float"),
		("fPartsMaskD__uiUNorm", "float"),
		("fPartsMaskX__uiUNorm", "float"),
		("fPartsMaskY__uiUNorm", "float"),
		("fPartsMaskZ__uiUNorm", "float"),
		("fPartsMaskW__uiUNorm", "float"),
		("bUseOffset", "bbool"),
		("fOffsetScale", "float"),
		("bTranslucentOffset", "bbool"),
		("bAntiSSSEmit", "bbool"),
		("fFlowDirDir__uiDirection", "float3"),

		("align3", "ubyte[4]"),
		("fFlowControl__uiUNorm", "float4"),
		("fFlowTile", "float"),

		("align4", "ubyte[12]"),
		("fFlowColor__uiColor", "float4"),
		("fFlowMatControl__uiUNorm", "float4"),
		("fFilmThickness__uiUNorm", "float"),
		("fFilmBlend__uiUNorm", "float"),
		("fFilmIOR__uiUNorm", "float"),
		("fRefraction__uiUNorm", "float"),
		("fRefractionBlend__uiUNorm", "float"),
		("bUseBlendDisplace", "bbool"),
		("fVAnimV__uiUNorm", "float"),
		("fVAnimPosScale", "float"),
		("bInvertX", "bbool"),
		("fAnimEmitMin", "float"),
		("fAnimEmitSpeed", "float"),
		("bUseWaveEmit", "bbool"),
		("fAnimEmitWave", "float"),

		("align5", "ubyte[12]"),
		("fFurParam__uiUNorm", "float4"),
		("fFurTile", "float"),
		("fAlbedoBlend__uiSNorm", "float"),
		("bAlbedoOverUVsecondary", "bbool"),
		("bUVsecondaryXprojection", "bbool"),
		("fXprojectionTranspose__uiSNorm", "float4"),
		("fKinkControl", "float3"),
		("fRimAlphaPower__uiSNorm", "float"),
		("fRimTranslucency__uiUNorm", "float"),
		("fRimNormal__uiUNorm", "float"),
		("fSnowUVTile", "float"),

		("align6", "ubyte[4]"),
		("fSnowBlendColor__uiColor", "float4"),
		("fSnowMatControl__uiUNorm", "float4"),
		("fMaterialSnowBlendB", "float"),

		("align7", "ubyte[12]"),
		("fSnowControl", "float4"),

	])


class CBDevelopColorPick(EPyCStruct):
	fields = OrderedDict([


		("mousePos", "uint2"),
		("gammaCorrect", "bbool"),

	])


class CBPrimGpuSystem(EPyCStruct):
	fields = OrderedDict([


		("iEmitterCount", "uint"),
		("iTotalSpawnCount", "uint"),
		("iTotalParticleMax", "uint"),
		("iResetUnusedIndexHead", "uint"),
		("iResetUnusedIndexCount", "uint"),
		("fMainCameraDir", "float3"),
		("iGpuStateFlags", "uint"),
		("iGpuUpdateCounter", "uint"),

		("align0", "ubyte[8]"),
		("gCollisionSpaceAABBMin", "float3"),

		("align1", "ubyte[4]"),
		("gCollisionSpaceSizeInv", "float3"),
		("gCollisionSpaceDivideX", "uint"),
		("gCollisionSpaceDivideY", "uint"),
		("gCollisionSpaceDivideZ", "uint"),
		("gCollisionSpring", "float"),
		("gForceWindScale", "float"),
		("gForceWindMass", "float"),
		("gForceWindCurve", "float"),

	])


class CBRadialBlurFunction(EPyCStruct):
	fields = OrderedDict([


		("iRadialFilterSampleColorScale", "int"),
		("iRadialFilterAlpha", "int"),
		("iRadialBlurWidth", "int"),
		("iRadialBlurAlpha", "int"),

	])


class CBFilter2(EPyCStruct):
	fields = OrderedDict([


		("fFilterUVMin", "float2"),
		("fFilterUVMax", "float2"),
		("fFilterSampleOffsets", "float[11]"),

		("align0", "ubyte[12]"),
		("fFilterSampleWeights", "float[11]"),
		("fFilterThreshold", "float"),

	])


class CBMhMaterialVfxWaveLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fConstant", "float"),

		("align0", "ubyte[12]"),
		("fUVTransformA", "float4"),
		("fUVTransformB", "float4"),
		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),

		("align1", "ubyte[4]"),
		("fEmissiveBlendColor__uiColor", "float3"),
		("fEmissiveBlendColorBlend__uiUNorm", "float"),
		("fDetailNormalBlend__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("fDisplacementLevel", "float"),
		("fWriteSplash", "bbool"),
		("fSplashAngle", "float"),

		("align2", "ubyte[12]"),
		("fSplashColor__uiColor", "float4"),
		("fSplashLevel__uiUNorm", "float"),
		("fSplashOffsetX", "float"),
		("fWriteShadow", "bbool"),

		("align3", "ubyte[4]"),
		("fShadowColor__uiColor", "float4"),
		("fShadowLevel__uiUNorm", "float"),
		("fNoiseLength__uiUNorm", "float"),
		("fNoiseDetail__uiUNorm", "float"),
		("fSplashSpeed", "float"),

	])


class CBMhMaterialNPCHairLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fTranslucency__uiUNorm", "float"),
		("bBaseColorEmissive", "bbool"),
		("bBackFaceNormalFilp", "bbool"),
		("fAnimEmitMin", "float"),
		("fAnimEmitSpeed", "float"),

		("align0", "ubyte[12]"),
		("fPrimaryColor__uiColor", "float4"),
		("fSecondaryColor__uiColor", "float4"),
		("fPrimaryExpo__uiUNorm", "float"),
		("fSecondaryExpo__uiUNorm", "float"),
		("fPrimaryShift__uiSNorm", "float"),
		("fSecondaryShift__uiSNorm", "float"),
		("fShininess", "float"),
		("fFakeLight__uiDirection", "float3"),
		("fFurNMHeight", "float"),

		("align1", "ubyte[12]"),
		("fFurParam__uiUNorm", "float4"),
		("fFurTile", "float"),

		("align2", "ubyte[12]"),
		("fVertexAO__uiColor", "float4"),
		("fVColorNormalBlend__uiUNorm", "float"),
		("fRimWidth__uiUNorm", "float"),
		("fRimNormalBlend__uiUNorm", "float"),
		("bUseRimTranslucency", "bbool"),
		("bUseOffset", "bbool"),
		("fInnerOffsetScale", "float"),
		("fDetailNormalBlend__uiUNorm", "float"),

		("align3", "ubyte[4]"),
		("fUVTransformDetailNormal", "float4"),

	])


class CBGUIGBuffer(EPyCStruct):
	fields = OrderedDict([


		("iGUIGBufferLightChannel", "uint"),
		("fGUIGBufferEmissiveColor", "float3"),
		("fGUIGBufferParam", "float3"),

	])


class CBMhSkyPS(EPyCStruct):
	fields = OrderedDict([


		("fSkyMode", "uint"),
		("fEmissiveMapFactor", "float3"),
		("fSkySunMapFactor", "float4"),
		("fSkyStarrySkyMapFactor", "float4"),
		("fSkyFlowDir", "float3"),
		("fSkyUVPhaseShiftH", "float"),
		("fSkyUVPhaseShiftV", "float"),
		("fSkyBlend", "float"),
		("fSkySunUVTransform", "float2"),
		("fSkyFlowSpeed", "float"),
		("fSkyFlowTime", "float"),

		("align0", "ubyte[8]"),
		("fSkyWaterReflectionFactor", "float3"),
		("bSkyIsRenderingWater", "bbool"),
		("iSkyAddress", "uint2"),

	])


class CBGUIDevelop(EPyCStruct):
	fields = OrderedDict([


		("fGUIOverlapDrawColor", "float3"),

	])


class CBCubeBlend(EPyCStruct):
	fields = OrderedDict([


		("fCubeBlendRate", "float"),

	])


class CBCreateMipmap(EPyCStruct):
	fields = OrderedDict([


		("iRegion", "uint4"),

	])


class CBMhMaterialEMLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fTranslucency__uiUNorm", "float"),
		("bBaseColorEmissive", "bbool"),
		("fPaintUVTile", "float2"),
		("fAddNormalBlend__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fAddNormalMaskA__uiSNorm", "float4"),
		("fAddNormalMaskB__uiSNorm", "float4"),
		("fAddNormalMaskC__uiUNorm", "float"),
		("fAddNormalMaskD__uiUNorm", "float"),
		("bBackFaceShading", "bbool"),
		("bBackFaceNormalFilp", "bbool"),
		("fKizuColor__uiColor", "float3"),

		("align1", "ubyte[4]"),
		("fKizuUVOffset__uiUNorm", "float2"),
		("fKizuMultiply", "float"),
		("bLegendary", "bbool"),
		("fLegendColor__uiColor", "float4"),
		("fLegendMetalMask__uiUNorm", "float2"),
		("fLegendRoughness", "float"),

		("align2", "ubyte[4]"),
		("fLegendFilm__uiUNorm", "float3"),
		("fLegendSSSMask__uiUNorm", "float"),
		("fLegendHSV__uiSNorm", "float3"),
		("fLegendFilmIOR__uiUNorm", "float"),
		("fPartsMaskA__uiUNorm", "float"),
		("fPartsMaskB__uiUNorm", "float"),
		("fPartsMaskC__uiUNorm", "float"),
		("fPartsMaskD__uiUNorm", "float"),
		("fPartsMaskX__uiUNorm", "float"),
		("fPartsMaskY__uiUNorm", "float"),
		("fPartsMaskZ__uiUNorm", "float"),
		("fPartsMaskW__uiUNorm", "float"),
		("bUseOffset", "bbool"),
		("fOffsetScale", "float"),
		("bTranslucentOffset", "bbool"),
		("bAntiSSSEmit", "bbool"),
		("fFlowDirDir__uiDirection", "float3"),

		("align3", "ubyte[4]"),
		("fFlowControl__uiUNorm", "float4"),
		("fFlowTile", "float"),

		("align4", "ubyte[12]"),
		("fFlowColor__uiColor", "float4"),
		("fFlowMatControl__uiUNorm", "float4"),
		("fFilmThickness__uiUNorm", "float"),
		("fFilmBlend__uiUNorm", "float"),
		("fFilmIOR__uiUNorm", "float"),
		("fRefraction__uiUNorm", "float"),
		("fRefractionBlend__uiUNorm", "float"),
		("fAnimEmitMin", "float"),
		("fAnimEmitSpeed", "float"),
		("bUseWaveEmit", "bbool"),
		("fAnimEmitWave", "float"),
		("fRimAlphaPower__uiSNorm", "float"),
		("fRimTranslucency__uiUNorm", "float"),
		("fRimNormal__uiUNorm", "float"),
		("fSnowUVTile", "float"),

		("align5", "ubyte[12]"),
		("fSnowBlendColor__uiColor", "float4"),
		("fSnowMatControl__uiUNorm", "float4"),
		("fMaterialSnowBlendB", "float"),

		("align6", "ubyte[12]"),
		("fSnowControl", "float4"),

	])


class CBMaterialCommon__disclosure(EPyCStruct):
	fields = OrderedDict([


		("bBypass", "bbool"),
		("bDecalMask", "bbool"),
		("bEmissive", "bbool"),
		("iGBufferId", "uint"),
		("iOutlineId", "uint"),

	])


class CBGlobalIllumination(EPyCStruct):
	fields = OrderedDict([


		("fSpecularIntensity", "float"),
		("fSpecularTemporalBlendRate", "float"),
		("fSpecularDifference", "float"),

	])


class CBMhMaterialEM117Local__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fTranslucency__uiUNorm", "float"),
		("bBaseColorEmissive", "bbool"),
		("fPaintUVTile", "float2"),
		("fAddNormalBlend__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fAddNormalMaskA__uiSNorm", "float4"),
		("fAddNormalMaskB__uiSNorm", "float4"),
		("fAddNormalMaskC__uiUNorm", "float"),
		("fAddNormalMaskD__uiUNorm", "float"),
		("bBackFaceShading", "bbool"),
		("bBackFaceNormalFilp", "bbool"),
		("fKizuColor__uiColor", "float3"),

		("align1", "ubyte[4]"),
		("fKizuUVOffset__uiUNorm", "float2"),
		("fKizuMultiply", "float"),
		("bLegendary", "bbool"),
		("fLegendColor__uiColor", "float4"),
		("fLegendMetalMask__uiUNorm", "float2"),
		("fLegendRoughness", "float"),

		("align2", "ubyte[4]"),
		("fLegendFilm__uiUNorm", "float3"),
		("fLegendSSSMask__uiUNorm", "float"),
		("fLegendHSV__uiSNorm", "float3"),
		("fLegendFilmIOR__uiUNorm", "float"),
		("fPartsMaskA__uiUNorm", "float"),
		("fPartsMaskB__uiUNorm", "float"),
		("fPartsMaskC__uiUNorm", "float"),
		("fPartsMaskD__uiUNorm", "float"),
		("fPartsMaskX__uiUNorm", "float"),
		("fPartsMaskY__uiUNorm", "float"),
		("fPartsMaskZ__uiUNorm", "float"),
		("fPartsMaskW__uiUNorm", "float"),
		("bUseOffset", "bbool"),
		("fOffsetScale", "float"),
		("bTranslucentOffset", "bbool"),
		("bAntiSSSEmit", "bbool"),
		("fFlowDirDir__uiDirection", "float3"),

		("align3", "ubyte[4]"),
		("fFlowControl__uiUNorm", "float4"),
		("fFlowTile", "float"),

		("align4", "ubyte[12]"),
		("fFlowColor__uiColor", "float4"),
		("fFlowMatControl__uiUNorm", "float4"),
		("fFilmThickness__uiUNorm", "float"),
		("fFilmBlend__uiUNorm", "float"),
		("fFilmIOR__uiUNorm", "float"),
		("fRefraction__uiUNorm", "float"),
		("fRefractionBlend__uiUNorm", "float"),

		("align5", "ubyte[12]"),
		("fDetailBlend__uiUNorm", "float4"),
		("fDetailTile", "float4"),
		("fDetailA_Color__uiColor", "float4"),
		("fDetailB_Color__uiColor", "float4"),
		("fDetailC_Color__uiColor", "float4"),
		("fDetailD_Color__uiColor", "float4"),
		("fDetail_Roughness__uiUNorm", "float4"),
		("fDetail_Metal__uiUNorm", "float4"),
		("bAntiEmitSSS", "bbool"),
		("fAnimEmitMin", "float"),
		("fAnimEmitSpeed", "float"),
		("bUseWaveEmit", "bbool"),
		("fAnimEmitWave", "float"),
		("fRimAlphaPower__uiSNorm", "float"),
		("fRimTranslucency__uiUNorm", "float"),
		("fRimNormal__uiUNorm", "float"),
		("fSnowUVTile", "float"),

		("align6", "ubyte[12]"),
		("fSnowBlendColor__uiColor", "float4"),
		("fSnowMatControl__uiUNorm", "float4"),
		("fMaterialSnowBlendB", "float"),

		("align7", "ubyte[12]"),
		("fSnowControl", "float4"),

	])


class CBMhMaterialTMG001Local__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fTranslucency__uiUNorm", "float"),
		("bBaseColorEmissive", "bbool"),
		("fPaintUVTile", "float2"),
		("fAddNormalBlend__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fAddNormalMaskA__uiSNorm", "float4"),
		("fAddNormalMaskB__uiSNorm", "float4"),
		("fAddNormalMaskC__uiUNorm", "float"),
		("fAddNormalMaskD__uiUNorm", "float"),
		("bBackFaceShading", "bbool"),
		("bBackFaceNormalFilp", "bbool"),
		("fKizuColor__uiColor", "float3"),

		("align1", "ubyte[4]"),
		("fKizuUVOffset__uiUNorm", "float2"),
		("fKizuMultiply", "float"),
		("bLegendary", "bbool"),
		("fLegendColor__uiColor", "float4"),
		("fLegendMetalMask__uiUNorm", "float2"),
		("fLegendRoughness", "float"),

		("align2", "ubyte[4]"),
		("fLegendFilm__uiUNorm", "float3"),
		("fLegendSSSMask__uiUNorm", "float"),
		("fLegendHSV__uiSNorm", "float3"),
		("fLegendFilmIOR__uiUNorm", "float"),
		("fPartsMaskA__uiUNorm", "float"),
		("fPartsMaskB__uiUNorm", "float"),
		("fPartsMaskC__uiUNorm", "float"),
		("fPartsMaskD__uiUNorm", "float"),
		("fPartsMaskX__uiUNorm", "float"),
		("fPartsMaskY__uiUNorm", "float"),
		("fPartsMaskZ__uiUNorm", "float"),
		("fPartsMaskW__uiUNorm", "float"),
		("bUseOffset", "bbool"),
		("fOffsetScale", "float"),
		("bTranslucentOffset", "bbool"),
		("bAntiSSSEmit", "bbool"),
		("fFlowDirDir__uiDirection", "float3"),

		("align3", "ubyte[4]"),
		("fFlowControl__uiUNorm", "float4"),
		("fFlowTile", "float"),

		("align4", "ubyte[12]"),
		("fFlowColor__uiColor", "float4"),
		("fFlowMatControl__uiUNorm", "float4"),
		("fMaskBlend__uiUNorm", "float4"),
		("fMaskBlend_A__uiUNorm", "float2"),
		("fMaskBlend_B__uiUNorm", "float2"),
		("fFilmThickness__uiUNorm", "float"),
		("fFilmBlend__uiUNorm", "float"),
		("fFilmIOR__uiUNorm", "float"),
		("fRefraction__uiUNorm", "float"),
		("fRefractionBlend__uiUNorm", "float"),

		("align5", "ubyte[12]"),
		("fDetailBlend__uiUNorm", "float4"),
		("fDetailTile", "float4"),
		("fDetailA_Color__uiColor", "float4"),
		("fDetailB_Color__uiColor", "float4"),
		("fDetailC_Color__uiColor", "float4"),
		("fDetailD_Color__uiColor", "float4"),
		("fDetail_Roughness__uiUNorm", "float4"),
		("fDetail_Metal__uiUNorm", "float4"),
		("bAntiEmitSSS", "bbool"),
		("fAnimEmitMin", "float"),
		("fAnimEmitSpeed", "float"),
		("bUseWaveEmit", "bbool"),
		("fAnimEmitWave", "float"),
		("fRimAlphaPower__uiSNorm", "float"),
		("fRimTranslucency__uiUNorm", "float"),
		("fRimNormal__uiUNorm", "float"),
		("fSnowUVTile", "float"),

		("align6", "ubyte[12]"),
		("fSnowBlendColor__uiColor", "float4"),
		("fSnowMatControl__uiUNorm", "float4"),
		("fMaterialSnowBlendB", "float"),

		("align7", "ubyte[12]"),
		("fSnowControl", "float4"),

	])


class CBMhMaterialSKM001Local__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fTranslucency__uiUNorm", "float"),
		("bBaseColorEmissive", "bbool"),
		("fPaintUVTile", "float2"),
		("fAddNormalBlend__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fAddNormalMaskA__uiSNorm", "float4"),
		("fAddNormalMaskB__uiSNorm", "float4"),
		("fAddNormalMaskC__uiUNorm", "float"),
		("fAddNormalMaskD__uiUNorm", "float"),
		("bBackFaceShading", "bbool"),
		("bBackFaceNormalFilp", "bbool"),
		("fKizuColor__uiColor", "float3"),

		("align1", "ubyte[4]"),
		("fKizuUVOffset__uiUNorm", "float2"),
		("fKizuMultiply", "float"),
		("bLegendary", "bbool"),
		("fLegendColor__uiColor", "float4"),
		("fLegendMetalMask__uiUNorm", "float2"),
		("fLegendRoughness", "float"),

		("align2", "ubyte[4]"),
		("fLegendFilm__uiUNorm", "float3"),
		("fLegendSSSMask__uiUNorm", "float"),
		("fLegendHSV__uiSNorm", "float3"),
		("fLegendFilmIOR__uiUNorm", "float"),
		("fPartsMaskA__uiUNorm", "float"),
		("fPartsMaskB__uiUNorm", "float"),
		("fPartsMaskC__uiUNorm", "float"),
		("fPartsMaskD__uiUNorm", "float"),
		("fPartsMaskX__uiUNorm", "float"),
		("fPartsMaskY__uiUNorm", "float"),
		("fPartsMaskZ__uiUNorm", "float"),
		("fPartsMaskW__uiUNorm", "float"),
		("bUseOffset", "bbool"),
		("fOffsetScale", "float"),
		("bTranslucentOffset", "bbool"),
		("bAntiSSSEmit", "bbool"),
		("fFlowDirDir__uiDirection", "float3"),

		("align3", "ubyte[4]"),
		("fFlowControl__uiUNorm", "float4"),
		("fFlowTile", "float"),

		("align4", "ubyte[12]"),
		("fFlowColor__uiColor", "float4"),
		("fFlowMatControl__uiUNorm", "float4"),
		("fMaskBlend__uiUNorm", "float4"),
		("fMaskBlend_A__uiUNorm", "float2"),
		("fMaskBlend_B__uiUNorm", "float2"),
		("fDisplaceControl", "float4"),
		("fDispSpeed", "float"),
		("fFilmThickness__uiUNorm", "float"),
		("fFilmBlend__uiUNorm", "float"),
		("fFilmIOR__uiUNorm", "float"),
		("fFilmThicknessB__uiUNorm", "float"),
		("fFilmBlendB__uiUNorm", "float"),
		("fFilmIORB__uiUNorm", "float"),
		("fRefraction__uiUNorm", "float"),
		("fRefractionBlend__uiUNorm", "float"),
		("fAnimEmitMin", "float"),
		("fAnimEmitSpeed", "float"),
		("bUseWaveEmit", "bbool"),
		("fAnimEmitWave", "float"),
		("fRimAlphaPower__uiSNorm", "float"),
		("fRimTranslucency__uiUNorm", "float"),
		("fRimNormal__uiUNorm", "float"),
		("fSnowUVTile", "float"),

		("align5", "ubyte[12]"),
		("fSnowBlendColor__uiColor", "float4"),
		("fSnowMatControl__uiUNorm", "float4"),
		("fMaterialSnowBlendB", "float"),

		("align6", "ubyte[12]"),
		("fSnowControl", "float4"),

	])


class CBSpeedTreePrimitiveInfo(EPyCStruct):
	fields = OrderedDict([


		("iPrimitiveInfo", "uint4"),

	])


class CBMhMaterialEM100Local__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fTranslucency__uiUNorm", "float"),
		("bBaseColorEmissive", "bbool"),
		("fPaintUVTile", "float2"),
		("fAddNormalBlend__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fAddNormalMaskA__uiSNorm", "float4"),
		("fAddNormalMaskB__uiSNorm", "float4"),
		("fAddNormalMaskC__uiUNorm", "float"),
		("fAddNormalMaskD__uiUNorm", "float"),
		("bBackFaceShading", "bbool"),
		("bBackFaceNormalFilp", "bbool"),
		("fKizuColor__uiColor", "float3"),

		("align1", "ubyte[4]"),
		("fKizuUVOffset__uiUNorm", "float2"),
		("fKizuMultiply", "float"),
		("bLegendary", "bbool"),
		("fLegendColor__uiColor", "float4"),
		("fLegendMetalMask__uiUNorm", "float2"),
		("fLegendRoughness", "float"),

		("align2", "ubyte[4]"),
		("fLegendFilm__uiUNorm", "float3"),
		("fLegendSSSMask__uiUNorm", "float"),
		("fLegendHSV__uiSNorm", "float3"),
		("fLegendFilmIOR__uiUNorm", "float"),
		("fPartsMaskA__uiUNorm", "float"),
		("fPartsMaskB__uiUNorm", "float"),
		("fPartsMaskC__uiUNorm", "float"),
		("fPartsMaskD__uiUNorm", "float"),
		("fPartsMaskX__uiUNorm", "float"),
		("fPartsMaskY__uiUNorm", "float"),
		("fPartsMaskZ__uiUNorm", "float"),
		("fPartsMaskW__uiUNorm", "float"),
		("bUseOffset", "bbool"),
		("fOffsetScale", "float"),
		("bTranslucentOffset", "bbool"),
		("bAntiSSSEmit", "bbool"),
		("fFlowDirDir__uiDirection", "float3"),

		("align3", "ubyte[4]"),
		("fFlowControl__uiUNorm", "float4"),
		("fFlowTile", "float"),

		("align4", "ubyte[12]"),
		("fFlowColor__uiColor", "float4"),
		("fFlowMatControl__uiUNorm", "float4"),
		("fMaskBlend__uiUNorm", "float4"),
		("fMaskBlend_A__uiUNorm", "float2"),
		("fMaskBlend_B__uiUNorm", "float2"),
		("fFilmThickness__uiUNorm", "float"),
		("fFilmBlend__uiUNorm", "float"),
		("fFilmIOR__uiUNorm", "float"),
		("fRefraction__uiUNorm", "float"),
		("fRefractionBlend__uiUNorm", "float"),
		("fAnimEmitMin", "float"),
		("fAnimEmitSpeed", "float"),
		("bUseWaveEmit", "bbool"),
		("fAnimEmitWave", "float"),

		("align5", "ubyte[12]"),
		("fFurParam__uiUNorm", "float4"),
		("fFurTile", "float"),
		("bUseFlipUV", "bbool"),
		("fRimAlphaPower__uiSNorm", "float"),
		("fRimTranslucency__uiUNorm", "float"),
		("fRimNormal__uiUNorm", "float"),
		("fSnowUVTile", "float"),

		("align6", "ubyte[8]"),
		("fSnowBlendColor__uiColor", "float4"),
		("fSnowMatControl__uiUNorm", "float4"),
		("fMaterialSnowBlendB", "float"),

		("align7", "ubyte[12]"),
		("fSnowControl", "float4"),

	])


class CBOutline(EPyCStruct):
	fields = OrderedDict([


		("fLineColor", "float4"),
		("iTargetID", "uint"),
		("iSampleCount", "uint"),
		("iMarkerNum", "uint"),

		("align0", "ubyte[4]"),
		("fMarkerPosition", "float4[3]"),
		("fRadius", "float"),
		("fFadeStartLength", "float"),
		("fBlinkSpeed", "float"),
		("fBlinkMin", "float"),
		("bDepthTest", "bbool"),

	])


class SeaDisplacement(EPyCStruct):
	fields = OrderedDict([


		("fWorldMat", "float4x4"),
		("iVBStride", "uint"),
		("iBaseVertexOffset", "uint"),
		("iVertexCount", "uint"),
		("iVBOffsetPosition", "uint"),
		("iVBOffsetTexcoord", "uint"),
		("fWorldScaleY", "float"),
		("fSupposedVertexDistance", "float"),

		("align0", "ubyte[4]"),
		("fWindParam", "float2"),
		("fNoiseDensity", "float"),
		("fChoppyCoef", "float"),

	])


class CBBitonicSort(EPyCStruct):
	fields = OrderedDict([


		("iSortArrayLength", "uint"),
		("iCompareFlipSize", "uint"),
		("iCompareStride", "uint"),
		("iCompareDir", "uint"),

	])


class CBDevelopFlags(EPyCStruct):
	fields = OrderedDict([


		("iDispChannel", "int"),
		("iDispCubeFace", "int"),
		("iDispMode", "int"),
		("fDispMipLevel", "float"),
		("fDispArraySlice", "float"),

	])


class CBMhMaterialVfxWaterLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fDistortionFactor__uiColor", "float3"),

		("align0", "ubyte[4]"),
		("fCubeMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("VertexPow", "float"),
		("fOpacityFactor", "float"),
		("fVertexOpacityFactor", "float"),
		("fNormalFactor__uiUNorm", "float"),

		("align1", "ubyte[12]"),
		("fUVTransformA", "float4"),
		("fVolumeBlend__uiSNorm", "float"),
		("bVertexColor", "bbool"),
		("fSpecularFactor", "float"),
		("fRaflectionAngle__uiSNorm", "float"),
		("fDistortionAngle", "float"),
		("fDistortion", "float"),
		("fRimRate", "float"),
		("fRimOpacityPow", "float"),
		("fRimOpacityFactor", "float"),
		("fTranslucency__uiUNorm", "float"),
		("bSceneEnvMap", "bbool"),
		("fDiffuseChroma__uiUNorm", "float"),
		("fSpecularChroma__uiUNorm", "float"),
		("fInnerOffsetScale", "float"),
		("fVelocityAttn", "float"),
		("fNormalDecalBlend__uiUNorm", "float"),

	])


class cbHDAO(EPyCStruct):
	fields = OrderedDict([


		("HDAORejectRadius", "float"),
		("HDAOAcceptRadius", "float"),
		("HDAOIntensity", "float"),
		("HDAOAcceptAngle", "float"),
		("HDAONormalScale", "float"),
		("HDAOUseNormal", "int"),

	])


class CBPartialColor(EPyCStruct):
	fields = OrderedDict([


		("color_matrix", "float4x4"),
		("compensate", "float"),

	])


class CBSystemGamma(EPyCStruct):
	fields = OrderedDict([


		("fSystemCopyGamma", "float"),

	])


class CBVRCompute(EPyCStruct):
	fields = OrderedDict([


		("iCountOffset", "uint"),

	])


class CBSSSSS_Profile(EPyCStruct):
	fields = OrderedDict([


		("fRGBBlurWeight", "float4[16]"),
		("fBlurOffset", "float4[8]"),
		("fBlurTargetDist", "float4"),

	])


class CBMhMaterialSlantFloorLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fSinkLength", "float"),
		("fConstSinkLength", "float"),
		("fMaxSlant", "float"),
		("fSlantRange", "float"),

	])


class CBConstant(EPyCStruct):
	fields = OrderedDict([


		("iUserConstant", "uint"),

	])


class CBViewProjection(EPyCStruct):
	fields = OrderedDict([


		("fViewProj", "float4x4"),
		("fView", "float4x4"),
		("fProj", "float4x4"),
		("fViewI", "float4x4"),
		("fProjI", "float4x4"),
		("fViewProjI", "float4x4"),
		("fCameraPos", "float3"),

		("align0", "ubyte[4]"),
		("fCameraDir", "float3"),

		("align1", "ubyte[4]"),
		("fZToLinear", "float3"),
		("fCameraNearClip", "float"),
		("fCameraFarClip", "float"),
		("fCameraTargetDist", "float"),

		("align2", "ubyte[8]"),
		("fPassThrough", "float4"),
		("fLODBasePos", "float3"),

		("align3", "ubyte[4]"),
		("fViewProjPF", "float4x4"),
		("fViewProjIPF", "float4x4"),
		("fViewPF", "float4x4"),
		("fProjPF", "float4x4"),
		("fViewProjIViewProjPF", "float4x4"),
		("fNoJitterProj", "float4x4"),
		("fNoJitterViewProj", "float4x4"),
		("fNoJitterViewProjI", "float4x4"),
		("fNoJitterViewProjIViewProjPF", "float4x4"),
		("fPassThroughCorrect", "float2"),
		("bWideMonitor", "bbool"),

	])


class CBMhMaterialFlowDirLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fDetailNormalBlend__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fUVTransformA", "float4"),
		("fUVTransformB", "float4"),
		("fTranslucency__uiUNorm", "float"),
		("fEmissiveBlendColor__uiColor", "float3"),
		("fEmissiveBlendColorBlend__uiUNorm", "float"),
		("fEmissiveBlendRimParam", "float3"),
		("fFlowDirDir__uiDirection", "float3"),
		("fFlowDirUVPhaseShift__uiUNorm", "float"),
		("bFlowDirLocalSpace", "bbool"),
		("fFlowDirFlowSpeed__uiUNorm", "float"),

	])


class CBLGTPRBDebug(EPyCStruct):
	fields = OrderedDict([


		("fProbeSize", "float"),
		("lineColor", "float3"),
		("iProbeDebugType", "uint"),

	])


class CBVRCommon(EPyCStruct):
	fields = OrderedDict([


		("iNumVolumes", "uint"),
		("fGIFactor", "float"),
		("fGIFactorShadow", "float"),

		("align0", "ubyte[4]"),
		("froxelDim", "uint2"),
		("checkerDim", "uint2"),
		("froxelDimInv", "float2"),
		("checkerDimInv", "float2"),
		("froxelZMinMax", "float3"),

		("align1", "ubyte[4]"),
		("fOrdered3x3", "float[9]"),

		("align2", "ubyte[12]"),
		("fOrdered4x4", "float[16]"),

		("align3", "ubyte[12]"),
		("fOrdered8x8", "float[64]"),

		("align4", "ubyte[12]"),
		("haltonXY", "float2[8]"),
		("fVRDeltaTime", "float"),
		("iJitterType", "uint"),
		("iFrameCount", "uint"),
		("bAlphaDitherFarClip", "bbool"),

		("align5", "ubyte[8]"),
		("fDistanceFadeParam", "float4"),

	])


class CB_CombinedFilter_ImagePlane(EPyCStruct):
	fields = OrderedDict([


		("iBlendType", "uint"),

		("align0", "ubyte[12]"),
		("fUVTransform", "float4x4"),
		("fPlaneColor", "float4"),

	])


class pix_clear_constants(EPyCStruct):
	fields = OrderedDict([


		("m_color", "float4"),

	])


class CBPrimSystem(EPyCStruct):
	fields = OrderedDict([


		("fPrimGammaCorrect", "float"),
		("fPrimAlphaLowerLimit", "float"),
		("fPrimGlobalLightReflectance", "float"),
		("iPrimSystemFalgs", "uint"),

	])


class CBMhMaterialEM080_01Local__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fTranslucency__uiUNorm", "float"),
		("bBaseColorEmissive", "bbool"),
		("fPaintUVTile", "float2"),
		("fAddNormalBlend__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fAddNormalMaskA__uiSNorm", "float4"),
		("fAddNormalMaskB__uiSNorm", "float4"),
		("fAddNormalMaskC__uiUNorm", "float"),
		("fAddNormalMaskD__uiUNorm", "float"),
		("bBackFaceShading", "bbool"),
		("bBackFaceNormalFilp", "bbool"),
		("fKizuColor__uiColor", "float3"),

		("align1", "ubyte[4]"),
		("fKizuUVOffset__uiUNorm", "float2"),
		("fKizuMultiply", "float"),
		("bLegendary", "bbool"),
		("fLegendColor__uiColor", "float4"),
		("fLegendMetalMask__uiUNorm", "float2"),
		("fLegendRoughness", "float"),

		("align2", "ubyte[4]"),
		("fLegendFilm__uiUNorm", "float3"),
		("fLegendSSSMask__uiUNorm", "float"),
		("fLegendHSV__uiSNorm", "float3"),
		("fLegendFilmIOR__uiUNorm", "float"),
		("fPartsMaskA__uiUNorm", "float"),
		("fPartsMaskB__uiUNorm", "float"),
		("fPartsMaskC__uiUNorm", "float"),
		("fPartsMaskD__uiUNorm", "float"),
		("fPartsMaskX__uiUNorm", "float"),
		("fPartsMaskY__uiUNorm", "float"),
		("fPartsMaskZ__uiUNorm", "float"),
		("fPartsMaskW__uiUNorm", "float"),
		("bUseOffset", "bbool"),
		("fOffsetScale", "float"),
		("bTranslucentOffset", "bbool"),
		("bAntiSSSEmit", "bbool"),
		("fFlowDirDir__uiDirection", "float3"),

		("align3", "ubyte[4]"),
		("fFlowControl__uiUNorm", "float4"),
		("fFlowTile", "float"),

		("align4", "ubyte[12]"),
		("fFlowColor__uiColor", "float4"),
		("fFlowMatControl__uiUNorm", "float4"),
		("fFilmThickness__uiUNorm", "float"),
		("fFilmBlend__uiUNorm", "float"),
		("fFilmIOR__uiUNorm", "float"),
		("fRefraction__uiUNorm", "float"),
		("fRefractionBlend__uiUNorm", "float"),
		("fAlbedoBlend__uiUNorm", "float"),
		("bUseBlendDisplace", "bbool"),
		("fVAnimV__uiUNorm", "float"),
		("fVAnimPosScale", "float"),
		("bInvertX", "bbool"),
		("fAlphaTestControl__uiUNorm", "float"),
		("fAnimEmitMin", "float"),
		("fAnimEmitSpeed", "float"),
		("bUseWaveEmit", "bbool"),
		("fAnimEmitWave", "float"),

		("align5", "ubyte[4]"),
		("fFurParam__uiUNorm", "float4"),
		("fFurTile", "float"),
		("fRimAlphaPower__uiSNorm", "float"),
		("fRimTranslucency__uiUNorm", "float"),
		("fRimNormal__uiUNorm", "float"),
		("fSnowUVTile", "float"),

		("align6", "ubyte[12]"),
		("fSnowBlendColor__uiColor", "float4"),
		("fSnowMatControl__uiUNorm", "float4"),
		("fMaterialSnowBlendB", "float"),

		("align7", "ubyte[12]"),
		("fSnowControl", "float4"),

	])


class CBLuminance(EPyCStruct):
	fields = OrderedDict([


		("iView", "uint"),
		("fKeyValue", "float"),
		("bClearHistory", "bbool"),
		("fLuminanceLogScale", "float"),
		("fLuminanceLogBias", "float"),
		("fLuminanceExpScale", "float"),
		("fLuminanceExpBias", "float"),
		("fWhiteRange", "float"),
		("fExposureValue", "float"),
		("fDarkSensitivity", "float"),
		("fLightSensitivity", "float"),
		("fDarkAdaptationLimit", "float"),
		("fLightAdaptationLimit", "float"),

	])


class CBMhMaterialSpeedTreeStdFurLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fDetailNormalBlend__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fUVTransformA", "float4"),
		("fUVTransformB", "float4"),
		("fBaseMapModulation__uiUNorm", "float4"),
		("fTranslucency__uiUNorm", "float"),
		("bLightProbeEmissive", "bbool"),

		("align1", "ubyte[8]"),
		("fEmissiveBlendColor__uiColor", "float3"),
		("fEmissiveBlendColorBlend__uiUNorm", "float"),
		("fEmissiveBlendRimParam", "float3"),
		("bSpecialBlend", "bbool"),
		("fRoughnessThreshold__uiUNorm", "float"),
		("fRoughnessFillValue__uiUNorm", "float"),
		("bWetNormalBlend", "bbool"),

		("align2", "ubyte[4]"),
		("fWetNormalBlendRange__uiUNorm", "float2"),
		("fFurNormalBlend__uiUNorm", "float"),
		("fFurHeight__uiUNorm", "float"),
		("fFurMapBlend__uiUNorm", "float"),
		("fFurEdgeBlend__uiUNorm", "float"),
		("fFurTile", "float"),

	])


class CBMhMaterialPLEditFaceLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fTranslucency__uiUNorm", "float"),
		("bBaseColorEmissive", "bbool"),
		("bBackFaceNormalFilp", "bbool"),
		("fAnimEmitMin", "float"),
		("fAnimEmitSpeed", "float"),
		("fAddColorUV__uiUNorm", "float2"),

		("align0", "ubyte[4]"),
		("fAddNormalMaskA__uiUNorm", "float4"),
		("fAddNormalMaskB__uiUNorm", "float4"),
		("fAddNormalMaskC__uiUNorm", "float4"),
		("fAddNormalMaskD__uiUNorm", "float4"),
		("fPaintMapRC", "float2"),
		("fPaintMapNum", "float"),

		("align1", "ubyte[4]"),
		("fPaintMapOffset__uiSNorm", "float4"),
		("fPaintColor__uiColor", "float4"),
		("fPaintRoughness__uiUNorm", "float"),
		("fPaintMetal__uiUNorm", "float"),
		("fPaintMapNumB", "float"),

		("align2", "ubyte[4]"),
		("fPaintMapOffsetB__uiSNorm", "float4"),
		("fPaintColorB__uiColor", "float4"),
		("fPaintRoughnessB__uiUNorm", "float"),
		("fPaintMetalB__uiUNorm", "float"),
		("fPaintMapNumC", "float"),

		("align3", "ubyte[4]"),
		("fPaintMapOffsetC__uiSNorm", "float4"),
		("fPaintColorC__uiColor", "float4"),
		("fPaintRoughnessC__uiUNorm", "float"),
		("fPaintMetalC__uiUNorm", "float"),
		("fFaceNormalBlend__uiUNorm", "float2"),
		("fMayuMapNum", "float"),
		("fMayuMapOffset__uiSNorm", "float2"),

		("align4", "ubyte[4]"),
		("fMayuMapRC", "float2"),

		("align5", "ubyte[8]"),
		("fMayuColor__uiColor", "float4"),
		("bPaintEmit", "bbool"),
		("bPaintEmitB", "bbool"),
		("bPaintEmitC", "bbool"),

		("align6", "ubyte[4]"),
		("fPaintEmitIntensity__uiUNorm", "float3"),
		("fPaintEmitIntensityMultiply", "float"),
		("bPaintNormal", "bbool"),
		("bPaintShade", "bbool"),
		("bPaintNormalB", "bbool"),
		("bPaintShadeB", "bbool"),
		("bPaintNormalC", "bbool"),
		("bPaintShadeC", "bbool"),
		("fFakeLightBlend", "float"),
		("fFakeLightIntensity", "float"),
		("fFakeFaceLight__uiDirection", "float3"),
		("fFakeShadowIntensity__uiUNorm", "float"),
		("fFakeShadowLength", "float"),
		("fDetailNormalBlend__uiUNorm", "float"),

		("align7", "ubyte[8]"),
		("fUVTransformDetailNormal", "float4"),

	])


class CBMhMaterialNPCEditFaceLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fTranslucency__uiUNorm", "float"),
		("bBaseColorEmissive", "bbool"),
		("bBackFaceNormalFilp", "bbool"),
		("fAnimEmitMin", "float"),
		("fAnimEmitSpeed", "float"),
		("fAddColorUV__uiUNorm", "float2"),

		("align0", "ubyte[4]"),
		("fAddNormalMaskA__uiUNorm", "float4"),
		("fAddNormalMaskB__uiUNorm", "float4"),
		("fAddNormalMaskC__uiUNorm", "float4"),
		("fAddNormalMaskD__uiUNorm", "float4"),
		("fPaintMapRC", "float2"),
		("fPaintMapNum", "float"),

		("align1", "ubyte[4]"),
		("fPaintMapOffset__uiSNorm", "float4"),
		("fPaintColor__uiColor", "float4"),
		("fPaintRoughness__uiUNorm", "float"),
		("fPaintMetal__uiUNorm", "float"),
		("fPaintMapNumB", "float"),

		("align2", "ubyte[4]"),
		("fPaintMapOffsetB__uiSNorm", "float4"),
		("fPaintColorB__uiColor", "float4"),
		("fPaintRoughnessB__uiUNorm", "float"),
		("fPaintMetalB__uiUNorm", "float"),
		("fPaintMapNumC", "float"),

		("align3", "ubyte[4]"),
		("fPaintMapOffsetC__uiSNorm", "float4"),
		("fPaintColorC__uiColor", "float4"),
		("fPaintRoughnessC__uiUNorm", "float"),
		("fPaintMetalC__uiUNorm", "float"),
		("fFaceNormalBlend__uiUNorm", "float2"),
		("fMayuMapNum", "float"),
		("fMayuMapOffset__uiSNorm", "float2"),

		("align4", "ubyte[4]"),
		("fMayuMapRC", "float2"),

		("align5", "ubyte[8]"),
		("fMayuColor__uiColor", "float4"),
		("bPaintEmit", "bbool"),
		("bPaintEmitB", "bbool"),
		("bPaintEmitC", "bbool"),

		("align6", "ubyte[4]"),
		("fPaintEmitIntensity__uiUNorm", "float3"),
		("fPaintEmitIntensityMultiply", "float"),
		("bPaintNormal", "bbool"),
		("bPaintShade", "bbool"),
		("bPaintNormalB", "bbool"),
		("bPaintShadeB", "bbool"),
		("bPaintNormalC", "bbool"),
		("bPaintShadeC", "bbool"),
		("fFakeLightBlend", "float"),
		("fFakeLightIntensity", "float"),
		("fFakeFaceLight__uiDirection", "float3"),
		("fFakeShadowIntensity__uiUNorm", "float"),
		("fFakeShadowLength", "float"),
		("fDetailNormalBlend__uiUNorm", "float"),

		("align7", "ubyte[8]"),
		("fUVTransformDetailNormal", "float4"),

	])


class CBMhMaterialStdLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fDetailNormalBlend__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fUVTransformA", "float4"),
		("fUVTransformB", "float4"),
		("fBaseMapModulation__uiUNorm", "float4"),
		("fTranslucency__uiUNorm", "float"),
		("fEmissiveBlendColor__uiColor", "float3"),
		("fEmissiveBlendColorBlend__uiUNorm", "float"),
		("fEmissiveBlendRimParam", "float3"),
		("bSpecialBlend", "bbool"),
		("fFurNormalBlend__uiUNorm", "float"),
		("fFurHeight__uiUNorm", "float"),
		("fFurMapBlend__uiUNorm", "float"),
		("fFurEdgeBlend__uiUNorm", "float"),
		("fFurTile", "float"),
		("bFakeRefraction", "bbool"),
		("fRefraction__uiUNorm", "float"),
		("fWetBlendDir__uiDirection", "float3"),
		("fWetBlendPlaneNormal__uiUNorm", "float"),
		("fWetBlendOp", "float3"),
		("bWetNormalBlend", "bbool"),
		("fWetNormalBlendRange__uiUNorm", "float2"),
		("fVolumeBlend__uiSNorm", "float"),

	])


class CBGaussian(EPyCStruct):
	fields = OrderedDict([


		("fOffset0", "float4"),
		("fOffset1", "float4"),
		("fWeight0", "float4"),
		("fWeight1", "float4"),
		("fEdgeSharpness", "float"),

	])


class CBTest(EPyCStruct):
	fields = OrderedDict([


		("fTestParam", "float4"),
		("fTestDirection", "float3"),
		("fTestType", "float"),
		("fTestColor", "float4"),
		("fDummyColor", "float4"),

	])


class CBTSAO(EPyCStruct):
	fields = OrderedDict([


		("iDepthRegion", "uint4"),
		("projConstant", "float4"),
		("fJitters", "float4"),
		("clipConstant", "float3"),

		("align0", "ubyte[4]"),
		("fOriginalInverseSize", "float2"),
		("fEdgeCoef", "float"),
		("projScale", "float"),
		("radius", "float"),
		("bias", "float"),
		("intensity", "float"),
		("fAcceptThresholdCoef", "float"),
		("fRenderTargetSizeScale", "float"),

	])


class CBMhMaterialNPCFaceLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fTranslucency__uiUNorm", "float"),
		("bBaseColorEmissive", "bbool"),
		("bBackFaceNormalFilp", "bbool"),
		("fAnimEmitMin", "float"),
		("fAnimEmitSpeed", "float"),
		("fAddColorUV__uiUNorm", "float2"),

		("align0", "ubyte[4]"),
		("fAddNormalMaskA__uiUNorm", "float4"),
		("fAddNormalMaskB__uiUNorm", "float4"),
		("fAddNormalMaskC__uiUNorm", "float4"),
		("fAddNormalMaskD__uiUNorm", "float4"),
		("bUseSkin", "bbool"),
		("fDetailNormalBlend__uiUNorm", "float"),

		("align1", "ubyte[8]"),
		("fUVTransformDetailNormal", "float4"),

	])


class CBGodRaysConfiguration(EPyCStruct):
	fields = OrderedDict([


		("isUseOcclusionFactorFromTexture", "bbool"),
		("isUseAlphaOcclusion", "bbool"),
		("isUseScaleOcclusion", "bbool"),
		("isGrayColor", "bbool"),
		("iThreshold", "int"),

	])


class CBMhSky2SimpleVS(EPyCStruct):
	fields = OrderedDict([


		("fSkyWorld", "float3x4"),

	])


class CBNormalMerge(EPyCStruct):
	fields = OrderedDict([


		("iNmSrcOffset", "uint"),
		("iNmVertexCount", "uint"),
		("iNmDestOffset", "uint"),
		("iNmDestStride", "uint"),
		("iNmRedirectOffset", "uint"),
		("iNmBlendFlag", "bbool"),
		("iNmStride", "uint"),
		("iNmOffset", "uint"),
		("iNmRateOffset", "uint"),

	])


class CBMhMaterialEC021Local__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fTranslucency__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fUVTransformA", "float4"),
		("bUseColorMask", "bbool"),

		("align1", "ubyte[12]"),
		("fAddColorA__uiColor", "float4"),
		("fAddColorB__uiColor", "float4"),
		("fAddColorC__uiColor", "float4"),
		("fAddColorD__uiColor", "float4"),
		("fBaseMapMod__uiUNorm", "float4"),
		("fBaseMapModLimitMax__uiUNorm", "float4"),
		("fBaseMapModLimitMin__uiUNorm", "float4"),
		("fEmissiveBlendColor__uiColor", "float3"),
		("fEmissiveBlendColorBlend__uiUNorm", "float"),
		("fEmissiveBlendRimParam", "float3"),
		("fFilmThickness__uiUNorm", "float"),
		("fFilmBlend__uiUNorm", "float"),
		("fFilmIOR__uiUNorm", "float"),
		("bBaseColorEmissive", "bbool"),

		("align2", "ubyte[4]"),
		("fFurParam__uiUNorm", "float4"),
		("fFurTile", "float"),
		("fFinWave", "float"),
		("fFinSpeed", "float"),

		("align3", "ubyte[4]"),
		("fFinColor__uiColor", "float3"),

	])


class CBVRGaussian(EPyCStruct):
	fields = OrderedDict([


		("fOffsets", "float4"),
		("fWeights", "float[5]"),
		("fEdgeSharpness", "float"),

	])


class CBInstancing(EPyCStruct):
	fields = OrderedDict([


		("iInstanceIndex", "uint"),

	])


class CBSnowHeightPick(EPyCStruct):
	fields = OrderedDict([


		("WriteOffset", "uint"),
		("SnowPickRenderFrame", "uint"),
		("PickRequestCount", "uint"),

		("align0", "ubyte[4]"),
		("PickPositionArray", "int4[31]"),

	])


class CBColorCorrectToneCurve(EPyCStruct):
	fields = OrderedDict([


		("fToneColor", "float4[256]"),

	])


class CBShapeMesh(EPyCStruct):
	fields = OrderedDict([


		("iVertexNum", "uint"),
		("iVertexOffset", "uint"),
		("iVertexStride", "uint"),
		("iPositionOffset", "uint"),
		("iNormalOffset", "uint"),
		("iTangentOffset", "uint"),
		("iWeightsOffset", "uint"),
		("iJointsOffset", "uint"),
		("iOutputVertexOffset", "uint"),

	])


class CB_DL(EPyCStruct):
	fields = OrderedDict([


		("time", "float3"),
		("customUInt", "uint"),
		("screenSize", "float4"),
		("viewMatrix", "float4x4"),
		("projMatrix", "float4x4"),
		("viewProjMatrix", "float4x4"),
		("crViewProjMatrix", "float4x4"),
		("prevViewProjMatrix", "float4x4"),

	])


class CBMhMaterialLandscapeFlowLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fDetailNormalBlend__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fUVTransformA", "float4"),
		("fUVTransformB", "float4"),
		("fTranslucency__uiUNorm", "float"),

		("align1", "ubyte[12]"),
		("fUVTransformC", "float4"),
		("fUVTransformD", "float4"),
		("fUVTransformE", "float4"),
		("fParallaxFactor__uiUNorm", "float"),
		("fParallaxMinSampleNum__uiUNorm", "float"),
		("fParallaxMaxSampleNum__uiUNorm", "float"),
		("fBlendHeightMin__uiUNorm", "float"),
		("fBlendHeightMax__uiUNorm", "float"),
		("fParallaxAttenDistanceBegin", "float"),
		("fParallaxAttenDistanceEnd", "float"),
		("fParallaxVertexOffset", "float"),
		("bSpecialBlend", "bbool"),
		("bWetNormalBlend", "bbool"),
		("fWetNormalBlendRange__uiUNorm", "float2"),
		("fFlowDirDir__uiDirection", "float3"),

		("align2", "ubyte[4]"),
		("fFlowDirUVPhaseShift__uiUNorm", "float2"),
		("fFlowDirFlowSpeed__uiUNorm", "float"),
		("bFlowDirVfxNormalBlend", "bbool"),

	])


class CBAmbientOccluder(EPyCStruct):
	fields = OrderedDict([


		("fSceneTextureScale", "float2"),
		("fIntensity", "float"),
		("fTransparency", "float"),

	])


class CBSnowField2Material(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor", "float4"),
		("fEmissiveMapFactor", "float3"),
		("fRoughness", "float"),
		("fMetalic", "float"),
		("fTranslucency", "float"),
		("fDetailNormalBlend", "float"),

		("align0", "ubyte[4]"),
		("fUVTransformA", "float4"),
		("fUVTransformB", "float4"),
		("fUVTransformUnder", "float4"),
		("fVolumeBlend", "float"),
		("fShovelCornerBlendRate", "float"),
		("fDecalMaskAlphaRef", "float"),
		("bHeightMapClip", "bbool"),
		("fHeightMapClipRef", "float"),
		("fUVRotationSin", "float"),
		("fUVRotationCos", "float"),

		("align1", "ubyte[4]"),
		("fUnderTextureBlendFactor", "float2"),
		("fSnowFieldDitherRate", "float"),

	])


class CBToneMappingSdrSim(EPyCStruct):
	fields = OrderedDict([


		("iToneMapType", "uint"),
		("bLuminanceVersion", "bbool"),
		("fShouldStr", "float"),
		("fLinearStr", "float"),
		("fIntermediate", "float"),
		("fS1", "float"),
		("fS2", "float"),
		("fS3", "float"),
		("fS4", "float"),
		("iLUTSize", "uint"),
		("bIsLinearToPQ", "bbool"),
		("bIsPQToLinear", "bbool"),
		("bEnableColorGrading", "bbool"),
		("bEnableSdrSimulation", "bbool"),
		("bEnableMaxLuminanceTest", "bbool"),

	])


class CBMhMaterialSpeedTreeStdBlendLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fDetailNormalBlend__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fUVTransformA", "float4"),
		("fUVTransformB", "float4"),
		("fTranslucency__uiUNorm", "float"),

		("align1", "ubyte[12]"),
		("fBlendBaseMapFactor__uiColor", "float4"),
		("fBlendEmissiveMapFactor__uiColor", "float3"),
		("fBlendMetalic__uiUNorm", "float"),
		("fBlendRoughness__uiUNorm", "float"),
		("fBlendDetailNormalBlend__uiUNorm", "float"),
		("fBlendSubSurfaceBlend__uiUNorm", "float"),
		("fBlendRoughnessThreshold__uiUNorm", "float"),
		("fBlendRoughnessFillValue__uiUNorm", "float"),

		("align2", "ubyte[12]"),
		("fBlendUVTransformA", "float4"),
		("fBlendUVTransformB", "float4"),
		("bUseUVSecondaryMtA", "bbool"),
		("bUseUVSecondaryMtB", "bbool"),
		("bUseUVSecondaryMtBM", "bbool"),
		("bUseUVSecondaryDetailNMtA", "bbool"),
		("bUseUVSecondaryDetailNMtB", "bbool"),
		("bLightProbeEmissive", "bbool"),

		("align3", "ubyte[8]"),
		("fEmissiveBlendColor__uiColor", "float3"),
		("fEmissiveBlendColorBlend__uiUNorm", "float"),
		("fEmissiveBlendRimParam", "float3"),
		("bSpecialBlend", "bbool"),
		("bWetNormalBlend", "bbool"),
		("fWetNormalBlendRange__uiUNorm", "float2"),

	])


class CBSSSSS(EPyCStruct):
	fields = OrderedDict([


		("fBlurMaxDist", "float"),
		("fBlurEdgeSharpness", "float"),
		("iDiviserFactor", "uint"),

	])


class CBRenderFrame(EPyCStruct):
	fields = OrderedDict([


		("iRenderFrame", "uint"),
		("iTotalTime", "uint"),
		("iTotalTimeEx", "uint"),
		("fFPS", "float"),
		("fDeltaTime", "float"),
		("fSSAOEffect", "float"),
		("bSSSEnable", "bbool"),
		("bIsRenderingWater", "bbool"),
		("fWaterDepthBias", "float"),
		("iGpuMode", "uint"),
		("fDitherSize", "float2"),
		("bHdrOutput", "bbool"),
		("fHdrOutputWhiteLevel", "float"),
		("fHdrOutputGamutMappingRatio", "float"),
		("fHdrOutputGamma", "float"),
		("bIsGUIHdrGamma", "bbool"),

	])


class CBMhMaterialFakeEyeLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fDetailNormalBlend__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fUVTransformA", "float4"),
		("fUVTransformB", "float4"),
		("fTranslucency__uiUNorm", "float"),
		("fParallaxFactor__uiUNorm", "float"),
		("fUV_Blend__uiUNorm", "float"),
		("bBaseColorEmissive", "bbool"),

	])


class CBSystem(EPyCStruct):
	fields = OrderedDict([


		("iRegion", "uint4"),
		("fSourceMipLevel", "float"),
		("fGammaCorrect", "float"),
		("fGammaCorrectEx", "float"),

	])


class CBModelChain(EPyCStruct):
	fields = OrderedDict([


		("fStartFrame", "float"),
		("fMotionKeyAlpha", "float"),
		("fStartRotation", "float"),
		("fNextModelFrame", "float"),
		("fNextModelRotation", "float"),
		("iMotionDataNum", "int"),

	])


class CBPick(EPyCStruct):
	fields = OrderedDict([


		("iPickPoint", "uint2"),

	])


class CBSky(EPyCStruct):
	fields = OrderedDict([


		("fSunSolidAngle", "float"),

	])


class CBSnowField2Debug(EPyCStruct):
	fields = OrderedDict([


		("iSnowField2DebugType", "uint"),

	])


class CB_TemporalAA2(EPyCStruct):
	fields = OrderedDict([


		("fBlendRate", "float"),
		("bVelocityBase", "bbool"),
		("fVarianceGamma", "float"),
		("fSharpenAmount", "float"),

	])


class CBLUTMaking(EPyCStruct):
	fields = OrderedDict([


		("iLUTSize", "uint"),
		("iMaxWidth", "uint"),
		("fMaxLuminance", "float"),
		("bIsPQToLinear", "bbool"),

	])


class CBMhEmissiveFog__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float4"),
		("fMetalic__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),

		("align0", "ubyte[4]"),
		("fUVTransformA", "float4"),
		("fUVTransformB", "float4"),
		("fFlowSpeed", "float"),
		("fFlowSpeedSecondary", "float"),
		("fFlowStrength", "float"),
		("fSecondaryFlowStrength", "float"),
		("fLerpAlpha_BMtoEM__uiUNorm", "float"),
		("fAlphaEdge", "bbool"),
		("fToneAlpha__uiUNorm", "float"),
		("fToneEdge__uiUNorm", "float"),
		("fEdgeColor__uiColor", "float4"),
		("fVertexAlpha", "bbool"),
		("fVolumeBlend__uiSNorm", "float"),
		("fDotOpacity", "float"),
		("fDotOpacityFactor", "float"),
		("bDotInverse", "bbool"),
		("fNearOpacity", "float"),
		("fNearOpacityDistance", "float"),
		("fDiffuseChroma__uiUNorm", "float"),
		("fSpecularChroma__uiUNorm", "float"),
		("fInnerOffsetScale", "float"),
		("fVelocityAttn", "float"),
		("fNormalDecalBlend__uiUNorm", "float"),
		("bUseUVPrimaryAM", "bbool"),

	])


class CBNormalRecalc(EPyCStruct):
	fields = OrderedDict([


		("iIBOffset", "uint"),
		("iSkinningVertexBase", "uint"),
		("iTriangleCount", "uint"),
		("iVertexOffset", "uint"),
		("iRedirectOffset", "uint"),

	])


class CBConstantHaltonSequence(EPyCStruct):
	fields = OrderedDict([


		("fHaltonSequence", "float4[64]"),

	])


class CBSpeedTreeLocalWindPF_SpeedTreeLocalWind(EPyCStruct):
	fields = OrderedDict([

		("pos", "float3"),
		("radius", "float"),
		("dir", "float3"),
		("strength", "float"),
		("oscillateStrength", "float"),
		("oscillateSpeed", "float"),
		("moveType", "uint"),
		("padding", "float"),

	])
    
class CBSpeedTreeLocalWindPF  (Mod3Container):
	Mod3Class = CBSpeedTreeLocalWindPF_SpeedTreeLocalWind
	baseCount = 128



class CBMhMaterialFakeLensLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fDetailNormalBlend__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fUVTransformA", "float4"),
		("fUVTransformB", "float4"),
		("fTranslucency__uiUNorm", "float"),
		("fOffset_A__uiUNorm", "float"),
		("fOffset_B__uiUNorm", "float"),

		("align1", "ubyte[4]"),
		("fCoating_A__uiColor", "float3"),

		("align2", "ubyte[4]"),
		("fCoating_B__uiColor", "float3"),

		("align3", "ubyte[4]"),
		("fCoating_C__uiColor", "float3"),

		("align4", "ubyte[4]"),
		("fCoating_D__uiColor", "float3"),
		("fWakuIntensity__uiUNorm", "float"),
		("fWakuSize__uiUNorm", "float"),

	])


class CBPrimGpuOcclusionVoxelSystem(EPyCStruct):
	fields = OrderedDict([


		("gActiveOcclusionAreaMinPos", "float3"),
		("gActiveOcclusionAreaSize", "float"),
		("gActiveOcclusionAreaSizeInv", "float"),
		("gActiveOcclusionAreaEdgeCellNum", "uint"),

		("align0", "ubyte[8]"),
		("gOcclusionAreaMinPos", "float3"),
		("gOcclusionVoxelInfoNum", "uint"),
		("gOcclusionVoxelSize", "float"),

	])


class CBMhMaterialVfxWave(EPyCStruct):
	fields = OrderedDict([


		("iPointNum", "uint"),
		("fViewTime", "float"),

	])


class CBTestLight(EPyCStruct):
	fields = OrderedDict([


		("fTestLightDir", "float3"),

		("align0", "ubyte[4]"),
		("fTestLightColor", "float3"),

	])


class CBMhMaterialFurnitureLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fDetailNormalBlend__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fUVTransformA", "float4"),
		("fUVTransformB", "float4"),
		("fTranslucency__uiUNorm", "float"),
		("fEmissiveBlendColor__uiColor", "float3"),
		("fEmissiveBlendColorBlend__uiUNorm", "float"),
		("fEmissiveBlendRimParam", "float3"),
		("fBlendBaseMapFactor__uiColor", "float4"),
		("fBlendEmissiveMapFactor__uiColor", "float3"),
		("fBlendMetalic__uiUNorm", "float"),
		("fBlendRoughness__uiUNorm", "float"),
		("fBlendDetailNormalBlend__uiUNorm", "float"),
		("fBlendSubSurfaceBlend__uiUNorm", "float"),

		("align1", "ubyte[4]"),
		("fBlendUVTransformA", "float4"),
		("fBlendUVTransformB", "float4"),
		("fBlendUVTransformBaseMap", "float4"),
		("fBlendDir__uiDirection", "float3"),
		("fBlendPlaneNormal__uiUNorm", "float"),
		("fBlendOp", "float3"),
		("bUseBlendBaseColor", "bbool"),
		("bUseUVSecondaryDetailNMtA", "bbool"),
		("bUseUVSecondaryDetailNMtB", "bbool"),
		("bUseUVSecondaryBaseMapMtB", "bbool"),
		("bUseUVSecondaryMtBM", "bbool"),
		("fFurNormalBlend__uiUNorm", "float"),
		("fFurHeight__uiUNorm", "float"),
		("fFurMapBlend__uiUNorm", "float"),
		("fFurEdgeBlend__uiUNorm", "float"),
		("fFurTile", "float"),
		("fBlendFurNormalBlend__uiUNorm", "float"),
		("fBlendFurHeight__uiUNorm", "float"),
		("fBlendFurMapBlend__uiUNorm", "float"),
		("fBlendFurEdgeBlend__uiUNorm", "float"),
		("fBlendFurTile", "float"),

	])


class CBSnowFall(EPyCStruct):
	fields = OrderedDict([


		("SnowAmount", "float"),

	])


class CBSSLR(EPyCStruct):
	fields = OrderedDict([


		("fSSLREffectReflectionParam", "float4"),
		("iSSLRReductionLevel", "int"),
		("fSSLRFactor", "float"),
		("fSSLRScale", "float"),
		("iLoopCount", "uint"),
		("fEliminateDepth", "float"),
		("fDitherRadius", "float"),
		("fImportanceBias", "float"),
		("fMipScale", "float"),
		("fMipBias", "float"),
		("fAccurateThreshold", "float"),
		("fEnvMapIntensity", "float"),
		("fSSLRIntensity", "float"),
		("fSSLREdgeAttenRate", "float"),
		("fSSLRDepthEliminateRate", "float"),
		("fSSLRLightProbeIntensity", "float"),
		("iSSLRMip0CountThreshold", "int"),
		("bSSLRTemporalReset", "bbool"),

	])


class CBGUIIcon(EPyCStruct):
	fields = OrderedDict([


		("fGUINoiseColor", "float4"),
		("fGUIEmissiveColor", "float4"),
		("fGUISpecularColor", "float3"),

		("align0", "ubyte[4]"),
		("fGUIIconLightColor", "float3"),

		("align1", "ubyte[4]"),
		("fGUIIconLightDir", "float3"),

	])


class CBSnowFieldGeometry(EPyCStruct):
	fields = OrderedDict([


		("fEdgesPerScreenHeight", "float"),
		("fWorldPositionMax", "float3"),
		("fWorldPositionMin", "float3"),
		("fShovelCornerBlendRate", "float"),

	])


class CBResample(EPyCStruct):
	fields = OrderedDict([


		("fResampleScreenSize", "float2"),
		("fResampleScale", "float2"),

	])


class CBMhMaterialPLLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fTranslucency__uiUNorm", "float"),
		("bBaseColorEmissive", "bbool"),
		("bBackFaceNormalFilp", "bbool"),
		("fAnimEmitMin", "float"),
		("fAnimEmitSpeed", "float"),
		("bUseCMM", "bbool"),

		("align0", "ubyte[8]"),
		("fAddColorA__uiColor", "float4"),
		("fAddColorB__uiColor", "float4"),
		("fAddColorC__uiColor", "float4"),
		("fAddColorD__uiColor", "float4"),
		("fFurParam__uiUNorm", "float4"),
		("fFurTile", "float"),

		("align1", "ubyte[12]"),
		("fSnowControl", "float4"),
		("fMaterialSnowBlendA", "float"),
		("fMaterialSnowBlendB", "float"),
		("fSnowTile", "float"),

		("align2", "ubyte[4]"),
		("fSnowColor__uiColor", "float3"),

		("align3", "ubyte[4]"),
		("fSnowMatControl__uiUNorm", "float4"),
		("fSnowUVOffset__uiUNorm", "float2"),
		("fAnimEmitWave", "float"),
		("bUseWaveEmit", "bbool"),
		("fFilmThickness__uiUNorm", "float"),
		("fFilmBlend__uiUNorm", "float"),
		("fFilmIOR__uiUNorm", "float"),
		("fRefractBlend__uiUNorm", "float"),
		("fRefraction__uiSNorm", "float"),
		("fPanoramaTile", "float"),

		("align4", "ubyte[8]"),
		("fEmissiveBlendColor__uiColor", "float3"),
		("fEmissiveBlendColorBlend__uiUNorm", "float"),
		("fEmissiveBlendRimParam", "float3"),
		("fDetailNormalBlend__uiUNorm", "float"),
		("fUVTransformDetailNormal", "float4"),

	])


class CBMhMaterial_EM105_EVCLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fTranslucency__uiUNorm", "float"),
		("bBaseColorEmissive", "bbool"),
		("fPaintUVTile", "float2"),
		("fAddNormalBlend__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fAddNormalMaskA__uiSNorm", "float4"),
		("fAddNormalMaskB__uiSNorm", "float4"),
		("fAddNormalMaskC__uiUNorm", "float"),
		("fAddNormalMaskD__uiUNorm", "float"),
		("bBackFaceShading", "bbool"),
		("bBackFaceNormalFilp", "bbool"),
		("fKizuColor__uiColor", "float3"),

		("align1", "ubyte[4]"),
		("fKizuUVOffset__uiUNorm", "float2"),
		("fKizuMultiply", "float"),
		("bLegendary", "bbool"),
		("fLegendColor__uiColor", "float4"),
		("fLegendMetalMask__uiUNorm", "float2"),
		("fLegendRoughness", "float"),

		("align2", "ubyte[4]"),
		("fLegendFilm__uiUNorm", "float3"),
		("fLegendSSSMask__uiUNorm", "float"),
		("fLegendHSV__uiSNorm", "float3"),
		("fLegendFilmIOR__uiUNorm", "float"),
		("fPartsMaskA__uiUNorm", "float"),
		("fPartsMaskB__uiUNorm", "float"),
		("fPartsMaskC__uiUNorm", "float"),
		("fPartsMaskD__uiUNorm", "float"),
		("fPartsMaskX__uiUNorm", "float"),
		("fPartsMaskY__uiUNorm", "float"),
		("fPartsMaskZ__uiUNorm", "float"),
		("fPartsMaskW__uiUNorm", "float"),
		("bUseOffset", "bbool"),
		("fOffsetScale", "float"),
		("bTranslucentOffset", "bbool"),
		("bAntiSSSEmit", "bbool"),
		("fFlowDirDir__uiDirection", "float3"),

		("align3", "ubyte[4]"),
		("fFlowControl__uiUNorm", "float4"),
		("fFlowTile", "float"),

		("align4", "ubyte[12]"),
		("fFlowColor__uiColor", "float4"),
		("fFlowMatControl__uiUNorm", "float4"),
		("fFilmThickness__uiUNorm", "float"),
		("fFilmBlend__uiUNorm", "float"),
		("fFilmIOR__uiUNorm", "float"),
		("fRefraction__uiUNorm", "float"),
		("fRefractionBlend__uiUNorm", "float"),
		("bUseBlendDisplace", "bbool"),
		("fVAnimV__uiUNorm", "float"),
		("fVAnimPosScale", "float"),
		("bInvertX", "bbool"),
		("fVPushScale", "float"),
		("fVPushWave", "float"),
		("fVPushSpeed", "float"),
		("fVpivot", "float3"),
		("fInnerOffsetScale", "float"),
		("fVolumeBlend__uiSNorm", "float"),

		("align5", "ubyte[12]"),
		("fDetailEmissiveControl", "float4"),
		("fFinWave", "float"),
		("fFinSpeed", "float"),

		("align6", "ubyte[8]"),
		("fFinColor__uiColor", "float3"),
		("fDetailNormalBlend__uiUNorm", "float"),
		("fAnimEmitMin", "float"),
		("fAnimEmitSpeed", "float"),
		("bUseWaveEmit", "bbool"),
		("fAnimEmitWave", "float"),
		("fRimAlphaPower__uiSNorm", "float"),
		("fRimTranslucency__uiUNorm", "float"),
		("fRimNormal__uiUNorm", "float"),

	])


class CBSnowField4Geometry(EPyCStruct):
	fields = OrderedDict([


		("fWorldPositionMin", "float3"),

		("align0", "ubyte[4]"),
		("fWorldPositionMax", "float3"),

		("align1", "ubyte[4]"),
		("fGeomWorldRange", "float4"),
		("fGeomTileSize", "float2"),
		("iGeomTileCount", "uint2"),
		("fShovelCornerBlendRate", "float"),
		("fEdgeHeightBlendRate", "float"),
		("fEdgesPerScreenHeight", "float"),

	])


class CBMhMaterialTestLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("iShaderMode", "int"),

		("align0", "ubyte[12]"),
		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fTranslucency__uiUNorm", "float"),

		("align1", "ubyte[12]"),
		("fUVTransformA", "float4"),
		("fParallaxFactor__uiUNorm", "float"),
		("fInnerOffsetScale", "float"),
		("fRimAlphaPower__uiUNorm", "float"),
		("fVolumeBlend__uiSNorm", "float"),
		("fOffset_A__uiUNorm", "float"),
		("fOffset_B__uiUNorm", "float"),

		("align2", "ubyte[8]"),
		("fCoating_A__uiColor", "float3"),

		("align3", "ubyte[4]"),
		("fCoating_B__uiColor", "float3"),

		("align4", "ubyte[4]"),
		("fCoating_C__uiColor", "float3"),

		("align5", "ubyte[4]"),
		("fCoating_D__uiColor", "float3"),
		("fWakuIntensity__uiUNorm", "float"),
		("fWakuSize__uiUNorm", "float"),
		("fRefraction__uiUNorm", "float"),
		("fVPushScale", "float"),
		("fVPushWave", "float"),
		("fVPushSpeed", "float"),
		("fVAnimPosScale", "float"),
		("fVAnimV__uiUNorm", "float"),

	])


class CBMhDecal(EPyCStruct):
	fields = OrderedDict([


		("iDecalShadingMode", "int"),
		("iDecalBlendMode", "int"),
		("fDecalNormalBlendRate", "float"),
		("fDecalAlphaTest", "bbool"),
		("fDecalAlphaTestRef", "float"),
		("bDecalAlphaMapUVFix", "bbool"),

		("align0", "ubyte[8]"),
		("fDecalEmissiveMapFactor", "float3"),
		("fDecalTransparency", "float"),
		("fDecalFlipUV", "bbool2"),

		("align1", "ubyte[8]"),
		("bDecalNormalMapFlip", "bbool3"),
		("bDecalFlowMap", "bbool"),
		("fDecalFlowTime", "float"),
		("fDecalFlowStrength", "float"),

		("align2", "ubyte[8]"),
		("fDecalUVTransform", "float4"),
		("fDecalAlphaCorrectionMinMax", "float2"),
		("fDecalBlendFactorIntensity", "float"),
		("iDecalAlphaMapChannel", "int"),
		("fDecalEdgeFade", "float"),
		("fDecalDistanceFadeRange", "float2"),
		("bDecalEmissiveBoost", "bbool"),
		("fDecalEmissiveBoostParam", "float2"),
		("fDecalNormalBlendPow", "float"),
		("bDecalNormalBC5", "bbool"),
		("bDecalDistortionEnable", "bbool"),
		("bDecalDistortionScreenFade", "bbool"),
		("fDecalDistortion", "float"),
		("fDecalDistortionAngle", "float"),
		("fDecalDistortionColor", "float3"),
		("fDecalDistanceFade", "float"),

	])


class CBViewFrustum(EPyCStruct):
	fields = OrderedDict([


		("fViewFrustum", "float4[6]"),

	])


class CBFog(EPyCStruct):
	fields = OrderedDict([


		("iFogType", "uint"),
		("iDistanceFogFlags", "uint"),
		("fFogStart", "float"),
		("fFogInvRange", "float"),
		("fFogDensity", "float"),
		("fFogColor", "float3"),
		("fFogHStart", "float"),
		("fFogHColor", "float3"),
		("fFogHInvRange", "float"),
		("fFogHDensity", "float"),
		("fFogHUVOffset", "float2"),
		("fFogHUVScale", "float"),
		("fFogHSlopeBias", "float"),
		("fFogCurveIntensity", "float"),
		("iMipFogBlendMode", "uint"),
		("fMipFogBlend", "float"),
		("fMipFogIntensity", "float"),

		("align0", "ubyte[8]"),
		("fMipFogColor", "float3"),

		("align1", "ubyte[4]"),
		("fSkyCenter", "float3"),
		("fSkyRadius", "float"),
		("fMipFogPrecomp", "float4"),
		("fMipFogLimitLevel", "float"),
		("fMipFogRotSin", "float"),
		("fMipFogRotCos", "float"),

	])


class CBMhMaterialEM124Local__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fTranslucency__uiUNorm", "float"),
		("bBaseColorEmissive", "bbool"),
		("fPaintUVTile", "float2"),
		("fAddNormalBlend__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fAddNormalMaskA__uiSNorm", "float4"),
		("fAddNormalMaskB__uiSNorm", "float4"),
		("fAddNormalMaskC__uiUNorm", "float"),
		("fAddNormalMaskD__uiUNorm", "float"),
		("bBackFaceShading", "bbool"),
		("bBackFaceNormalFilp", "bbool"),
		("fKizuColor__uiColor", "float3"),

		("align1", "ubyte[4]"),
		("fKizuUVOffset__uiUNorm", "float2"),
		("fKizuMultiply", "float"),
		("bLegendary", "bbool"),
		("fLegendColor__uiColor", "float4"),
		("fLegendMetalMask__uiUNorm", "float2"),
		("fLegendRoughness", "float"),

		("align2", "ubyte[4]"),
		("fLegendFilm__uiUNorm", "float3"),
		("fLegendSSSMask__uiUNorm", "float"),
		("fLegendHSV__uiSNorm", "float3"),
		("fLegendFilmIOR__uiUNorm", "float"),
		("fPartsMaskA__uiUNorm", "float"),
		("fPartsMaskB__uiUNorm", "float"),
		("fPartsMaskC__uiUNorm", "float"),
		("fPartsMaskD__uiUNorm", "float"),
		("fPartsMaskX__uiUNorm", "float"),
		("fPartsMaskY__uiUNorm", "float"),
		("fPartsMaskZ__uiUNorm", "float"),
		("fPartsMaskW__uiUNorm", "float"),
		("bUseOffset", "bbool"),
		("fOffsetScale", "float"),
		("bTranslucentOffset", "bbool"),
		("bAntiSSSEmit", "bbool"),
		("fFlowDirDir__uiDirection", "float3"),

		("align3", "ubyte[4]"),
		("fFlowControl__uiUNorm", "float4"),
		("fFlowTile", "float"),

		("align4", "ubyte[12]"),
		("fFlowColor__uiColor", "float4"),
		("fFlowMatControl__uiUNorm", "float4"),
		("fFilmThickness__uiUNorm", "float"),
		("fFilmBlend__uiUNorm", "float"),
		("fFilmIOR__uiUNorm", "float"),
		("fRefraction__uiUNorm", "float"),
		("fRefractionBlend__uiUNorm", "float"),
		("fAnimEmitMin", "float"),
		("fAnimEmitSpeed", "float"),
		("bUseWaveEmit", "bbool"),
		("fAnimEmitWave", "float"),

		("align5", "ubyte[12]"),
		("fFurParam__uiUNorm", "float4"),
		("fFurTile", "float"),
		("bUseFlipUV", "bbool"),
		("bParallax_Refraction", "bbool"),
		("fRefractBlend__uiUNorm", "float"),
		("fParallax_height__uiUNorm", "float"),
		("fRefraction_tile", "float"),
		("fRefraction_distortion__uiUNorm", "float"),

		("align6", "ubyte[4]"),
		("fBlendMatFactor", "float4"),
		("fAlphaTestControl__uiUNorm", "float"),
		("bUseSpecialMode", "bbool"),
		("fRimAlphaPower__uiSNorm", "float"),
		("fRimTranslucency__uiUNorm", "float"),
		("fRimNormal__uiUNorm", "float"),
		("fSnowUVTile", "float"),

		("align7", "ubyte[8]"),
		("fSnowBlendColor__uiColor", "float4"),
		("fSnowMatControl__uiUNorm", "float4"),
		("fMaterialSnowBlendB", "float"),

		("align8", "ubyte[12]"),
		("fSnowControl", "float4"),

	])


class CBVRRecompute(EPyCStruct):
	fields = OrderedDict([


		("fDepthTreshold", "float"),
		("fAngleTreshold", "float"),
		("fMaxDepth", "float"),

		("align0", "ubyte[4]"),
		("fDepthTreshold2", "float3"),

		("align1", "ubyte[4]"),
		("fAngleTreshold2", "float3"),

		("align2", "ubyte[4]"),
		("fMaxDepth2", "float3"),

	])


class CBLuminanceDebugDisp(EPyCStruct):
	fields = OrderedDict([


		("iLuminanceDispMode", "uint"),

		("align0", "ubyte[12]"),
		("fLuminanceDebugDispColor", "float4"),
		("fLuminanceDebugDispMinMax", "float2"),

	])


class CBLGTPRBGen(EPyCStruct):
	fields = OrderedDict([


		("iCurrentIndex", "uint"),
		("iWindowType", "uint"),

	])


class CBMhMaterialStdBlendLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fDetailNormalBlend__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fUVTransformA", "float4"),
		("fUVTransformB", "float4"),
		("fTranslucency__uiUNorm", "float"),
		("fEmissiveBlendColor__uiColor", "float3"),
		("fEmissiveBlendColorBlend__uiUNorm", "float"),
		("fEmissiveBlendRimParam", "float3"),
		("fBlendBaseMapFactor__uiColor", "float4"),
		("fBlendEmissiveMapFactor__uiColor", "float3"),
		("fBlendMetalic__uiUNorm", "float"),
		("fBlendRoughness__uiUNorm", "float"),
		("fBlendDetailNormalBlend__uiUNorm", "float"),
		("fBlendSubSurfaceBlend__uiUNorm", "float"),

		("align1", "ubyte[4]"),
		("fBlendUVTransformA", "float4"),
		("fBlendUVTransformB", "float4"),
		("fBlendDir__uiDirection", "float3"),
		("fBlendPlaneNormal__uiUNorm", "float"),
		("fBlendOp", "float3"),
		("bUseUVSecondaryMtA", "bbool"),
		("bUseUVSecondaryMtB", "bbool"),
		("bUseUVSecondaryMtBM", "bbool"),
		("fFurNormalBlend__uiUNorm", "float"),
		("fFurHeight__uiUNorm", "float"),
		("fFurMapBlend__uiUNorm", "float"),
		("fFurEdgeBlend__uiUNorm", "float"),
		("fFurTile", "float"),

		("align2", "ubyte[4]"),
		("fWetBlendDir__uiDirection", "float3"),
		("fWetBlendPlaneNormal__uiUNorm", "float"),
		("fWetBlendOp", "float3"),
		("bSpecialBlend", "bbool"),
		("bWetNormalBlend", "bbool"),
		("fWetNormalBlendRange__uiUNorm", "float2"),

	])


class CBBokehAutoFocus(EPyCStruct):
	fields = OrderedDict([


		("SelectedFocusPoint", "uint2"),

	])


class CBMotionBlur(EPyCStruct):
	fields = OrderedDict([


		("iMotionBlurSampleNum", "int"),
		("fMotionBlurShutterSpeed", "float"),
		("fMaxAdditionalVelocity", "float"),

		("align0", "ubyte[4]"),
		("fTransform", "float4x4"),
		("fMotionBlurFurShutterSpeed", "float"),

	])


class CBMhMaterialEM103Local__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fTranslucency__uiUNorm", "float"),
		("bBaseColorEmissive", "bbool"),
		("fPaintUVTile", "float2"),
		("fAddNormalBlend__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fAddNormalMaskA__uiSNorm", "float4"),
		("fAddNormalMaskB__uiSNorm", "float4"),
		("fAddNormalMaskC__uiUNorm", "float"),
		("fAddNormalMaskD__uiUNorm", "float"),
		("bBackFaceShading", "bbool"),
		("bBackFaceNormalFilp", "bbool"),
		("fKizuColor__uiColor", "float3"),

		("align1", "ubyte[4]"),
		("fKizuUVOffset__uiUNorm", "float2"),
		("fKizuMultiply", "float"),
		("bLegendary", "bbool"),
		("fLegendColor__uiColor", "float4"),
		("fLegendMetalMask__uiUNorm", "float2"),
		("fLegendRoughness", "float"),

		("align2", "ubyte[4]"),
		("fLegendFilm__uiUNorm", "float3"),
		("fLegendSSSMask__uiUNorm", "float"),
		("fLegendHSV__uiSNorm", "float3"),
		("fLegendFilmIOR__uiUNorm", "float"),
		("fPartsMaskA__uiUNorm", "float"),
		("fPartsMaskB__uiUNorm", "float"),
		("fPartsMaskC__uiUNorm", "float"),
		("fPartsMaskD__uiUNorm", "float"),
		("fPartsMaskX__uiUNorm", "float"),
		("fPartsMaskY__uiUNorm", "float"),
		("fPartsMaskZ__uiUNorm", "float"),
		("fPartsMaskW__uiUNorm", "float"),
		("bUseOffset", "bbool"),
		("fOffsetScale", "float"),
		("bTranslucentOffset", "bbool"),
		("bAntiSSSEmit", "bbool"),
		("fFlowDirDir__uiDirection", "float3"),

		("align3", "ubyte[4]"),
		("fFlowControl__uiUNorm", "float4"),
		("fFlowTile", "float"),

		("align4", "ubyte[12]"),
		("fFlowColor__uiColor", "float4"),
		("fFlowMatControl__uiUNorm", "float4"),
		("fFilmThickness__uiUNorm", "float"),
		("fFilmBlend__uiUNorm", "float"),
		("fFilmIOR__uiUNorm", "float"),
		("fRefraction__uiUNorm", "float"),
		("fRefractionBlend__uiUNorm", "float"),
		("fAlbedoBlend__uiUNorm", "float"),
		("bPartsAlpha", "bbool"),

		("align5", "ubyte[4]"),
		("fBlendBaseMapFactor__uiColor", "float4"),
		("fBlendMatFactor", "float4"),
		("bUseBlendDisplace", "bbool"),
		("fVAnimV__uiUNorm", "float"),
		("fVAnimPosScale", "float"),
		("bInvertX", "bbool"),
		("fAnimEmitMin", "float"),
		("fAnimEmitSpeed", "float"),
		("bUseWaveEmit", "bbool"),
		("fAnimEmitWave", "float"),
		("fRimAlphaPower__uiSNorm", "float"),
		("fRimTranslucency__uiUNorm", "float"),
		("fRimNormal__uiUNorm", "float"),
		("fSnowUVTile", "float"),
		("fSnowBlendColor__uiColor", "float4"),
		("fSnowMatControl__uiUNorm", "float4"),
		("fMaterialSnowBlendB", "float"),

		("align6", "ubyte[12]"),
		("fSnowControl", "float4"),

	])


class CBBloomSettings(EPyCStruct):
	fields = OrderedDict([


		("AdjustParams", "float4"),
		("CenterAndScale", "float4"),
		("Coefficient", "float4"),
		("TexHalfSizes", "float4"),

	])


class CBLightProbes(EPyCStruct):
	fields = OrderedDict([


		("bLightProbesEnable", "bbool"),
		("probesGridInvCellSize", "float3"),
		("probesGridPosition", "float3"),

		("align0", "ubyte[4]"),
		("probesGridSize", "uint3"),

		("align1", "ubyte[4]"),
		("fProbesGridHalf", "float3"),

		("align2", "ubyte[4]"),
		("probeColor", "float3"),

		("align3", "ubyte[4]"),
		("fOutsideSHCoef", "float4[7]"),
		("fShadowSHCoef", "float4[7]"),
		("lightProbesHemisphereTopIntensity", "float"),
		("lightProbesHemisphereBottomIntensity", "float"),
		("iProbeFlags", "uint"),
		("fDaytimeInterpolation", "float"),
		("bEnableNeighborSearch", "bbool"),
		("iTocCollisionOffset", "uint"),

	])


class CBSpeedTreeGlobalWind_SpeedTreeGlobalWind(EPyCStruct):
	fields = OrderedDict([

		("fBillboardTexCoords", "uint4x4[3]"),
		("fWindVector", "float4"),
		("fWindGlobal", "float4"),
		("fWindBranch", "float4"),
		("fWindBranchTwitch", "float4"),
		("fWindLeaf1Tumble", "float4"),
		("fWindLeaf2Tumble", "float4"),
		("fWindBranchAnchor", "float3"),
		("fWindBranchAdherences_x", "float"),
		("fWindBranchAdherences_y", "float"),
		("fWindBranchAdherences_z", "float"),
		("fWindFrondRipple_x", "float"),
		("fWindFrondRipple_y", "float"),
		("fWindFrondRipple_z", "float"),
		("fWindLeaf1Twitch", "float3"),
		("fWindLeaf2Twitch", "float3"),
		("fLocalGlobalDistance", "float"),
		("fWindLeaf1Ripple", "float2"),
		("fWindLeaf2Ripple", "float2"),
		("fWindBranchWhip", "float2"),
		("fWindTurbulences", "float2"),
		("fLocalBranchDistance", "float2"),
		("iWindAttr", "uint"),
		("padding_0", "float"),

	])

class CBSpeedTreeGlobalWind  (Mod3Container):
	Mod3Class = CBSpeedTreeGlobalWind_SpeedTreeGlobalWind
	baseCount = 160	


class CBMhMaterialLandscapeLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fDetailNormalBlend__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fUVTransformA", "float4"),
		("fUVTransformB", "float4"),
		("fTranslucency__uiUNorm", "float"),

		("align1", "ubyte[12]"),
		("fUVTransformC", "float4"),
		("fUVTransformD", "float4"),
		("fUVTransformE", "float4"),
		("fParallaxFactor__uiUNorm", "float"),
		("fParallaxMinSampleNum__uiUNorm", "float"),
		("fParallaxMaxSampleNum__uiUNorm", "float"),
		("fBlendHeightMin__uiUNorm", "float"),
		("fBlendHeightMax__uiUNorm", "float"),
		("fParallaxAttenDistanceBegin", "float"),
		("fParallaxAttenDistanceEnd", "float"),
		("fParallaxVertexOffset", "float"),
		("bSpecialBlend", "bbool"),
		("bWetNormalBlend", "bbool"),
		("fWetNormalBlendRange__uiUNorm", "float2"),

	])


class CBMaterialDebug(EPyCStruct):
	fields = OrderedDict([


		("iMaterialDebugView", "uint"),
		("bMaterialDebugZeroCheck", "bbool"),

		("align0", "ubyte[8]"),
		("fMaterialDebugColor", "float4"),

	])


class CBPickObject(EPyCStruct):
	fields = OrderedDict([


		("fPickObjectColor", "float4"),

	])


class CBHermiteCurveRGB(EPyCStruct):
	fields = OrderedDict([


		("fHermiteParamR", "float2[64]"),

		("align0", "ubyte[8]"),
		("fHermiteParamG", "float2[64]"),

		("align1", "ubyte[8]"),
		("fHermiteParamB", "float2[64]"),

	])


class CBMhSkyVS(EPyCStruct):
	fields = OrderedDict([


		("fSkyWorld", "float3x4"),

	])


class CBMhMaterialIridescentBlendLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fDetailNormalBlend__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fUVTransformA", "float4"),
		("fUVTransformB", "float4"),
		("fTranslucency__uiUNorm", "float"),
		("fEmissiveBlendColor__uiColor", "float3"),
		("fEmissiveBlendColorBlend__uiUNorm", "float"),
		("fEmissiveBlendRimParam", "float3"),
		("fBlendBaseMapFactor__uiColor", "float4"),
		("fBlendEmissiveMapFactor__uiColor", "float3"),
		("fBlendMetalic__uiUNorm", "float"),
		("fBlendRoughness__uiUNorm", "float"),
		("fBlendDetailNormalBlend__uiUNorm", "float"),
		("fBlendSubSurfaceBlend__uiUNorm", "float"),

		("align1", "ubyte[4]"),
		("fBlendUVTransformA", "float4"),
		("fBlendUVTransformB", "float4"),
		("fBlendDir__uiDirection", "float3"),
		("fBlendPlaneNormal__uiUNorm", "float"),
		("fBlendOp", "float3"),
		("bUseUVSecondaryMtA", "bbool"),
		("bUseUVSecondaryMtB", "bbool"),
		("bUseUVSecondaryMtBM", "bbool"),
		("fFurNormalBlend__uiUNorm", "float"),
		("fFurHeight__uiUNorm", "float"),
		("fFurMapBlend__uiUNorm", "float"),
		("fFurEdgeBlend__uiUNorm", "float"),
		("fFurTile", "float"),

		("align2", "ubyte[4]"),
		("fWetBlendDir__uiDirection", "float3"),
		("fWetBlendPlaneNormal__uiUNorm", "float"),
		("fWetBlendOp", "float3"),
		("bSpecialBlend", "bbool"),
		("bWetNormalBlend", "bbool"),
		("fWetNormalBlendRange__uiUNorm", "float2"),
		("fFilmThickness__uiUNorm", "float"),
		("fFilmBlend__uiUNorm", "float"),
		("fRefraction__uiUNorm", "float"),
		("fRefractionBlend__uiUNorm", "float"),

	])


class CBMhMaterialEM002Local__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fTranslucency__uiUNorm", "float"),
		("bBaseColorEmissive", "bbool"),
		("fPaintUVTile", "float2"),
		("fAddNormalBlend__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fAddNormalMaskA__uiSNorm", "float4"),
		("fAddNormalMaskB__uiSNorm", "float4"),
		("fAddNormalMaskC__uiUNorm", "float"),
		("fAddNormalMaskD__uiUNorm", "float"),
		("bBackFaceShading", "bbool"),
		("bBackFaceNormalFilp", "bbool"),
		("fKizuColor__uiColor", "float3"),

		("align1", "ubyte[4]"),
		("fKizuUVOffset__uiUNorm", "float2"),
		("fKizuMultiply", "float"),
		("bLegendary", "bbool"),
		("fLegendColor__uiColor", "float4"),
		("fLegendMetalMask__uiUNorm", "float2"),
		("fLegendRoughness", "float"),

		("align2", "ubyte[4]"),
		("fLegendFilm__uiUNorm", "float3"),
		("fLegendSSSMask__uiUNorm", "float"),
		("fLegendHSV__uiSNorm", "float3"),
		("fLegendFilmIOR__uiUNorm", "float"),
		("fPartsMaskA__uiUNorm", "float"),
		("fPartsMaskB__uiUNorm", "float"),
		("fPartsMaskC__uiUNorm", "float"),
		("fPartsMaskD__uiUNorm", "float"),
		("fPartsMaskX__uiUNorm", "float"),
		("fPartsMaskY__uiUNorm", "float"),
		("fPartsMaskZ__uiUNorm", "float"),
		("fPartsMaskW__uiUNorm", "float"),
		("bUseOffset", "bbool"),
		("fOffsetScale", "float"),
		("bTranslucentOffset", "bbool"),
		("bAntiSSSEmit", "bbool"),
		("fFlowDirDir__uiDirection", "float3"),

		("align3", "ubyte[4]"),
		("fFlowControl__uiUNorm", "float4"),
		("fFlowTile", "float"),

		("align4", "ubyte[12]"),
		("fFlowColor__uiColor", "float4"),
		("fFlowMatControl__uiUNorm", "float4"),
		("fMaskBlend__uiUNorm", "float4"),
		("fMaskBlend_A__uiUNorm", "float2"),
		("fMaskBlend_B__uiUNorm", "float2"),
		("fFilmThickness__uiUNorm", "float"),
		("fFilmBlend__uiUNorm", "float"),
		("fFilmIOR__uiUNorm", "float"),
		("fRefraction__uiUNorm", "float"),
		("fRefractionBlend__uiUNorm", "float"),
		("fAnimEmitMin", "float"),
		("fAnimEmitSpeed", "float"),
		("bUseWaveEmit", "bbool"),
		("fAnimEmitWave", "float"),
		("fRimAlphaPower__uiSNorm", "float"),
		("fRimTranslucency__uiUNorm", "float"),
		("fRimNormal__uiUNorm", "float"),
		("fSnowUVTile", "float"),

		("align5", "ubyte[12]"),
		("fSnowBlendColor__uiColor", "float4"),
		("fSnowMatControl__uiUNorm", "float4"),
		("fMaterialSnowBlendB", "float"),

		("align6", "ubyte[12]"),
		("fSnowControl", "float4"),

	])


class CBMhMaterialEM080Local__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fTranslucency__uiUNorm", "float"),
		("bBaseColorEmissive", "bbool"),
		("fPaintUVTile", "float2"),
		("fAddNormalBlend__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fAddNormalMaskA__uiSNorm", "float4"),
		("fAddNormalMaskB__uiSNorm", "float4"),
		("fAddNormalMaskC__uiUNorm", "float"),
		("fAddNormalMaskD__uiUNorm", "float"),
		("bBackFaceShading", "bbool"),
		("bBackFaceNormalFilp", "bbool"),
		("fKizuColor__uiColor", "float3"),

		("align1", "ubyte[4]"),
		("fKizuUVOffset__uiUNorm", "float2"),
		("fKizuMultiply", "float"),
		("bLegendary", "bbool"),
		("fLegendColor__uiColor", "float4"),
		("fLegendMetalMask__uiUNorm", "float2"),
		("fLegendRoughness", "float"),

		("align2", "ubyte[4]"),
		("fLegendFilm__uiUNorm", "float3"),
		("fLegendSSSMask__uiUNorm", "float"),
		("fLegendHSV__uiSNorm", "float3"),
		("fLegendFilmIOR__uiUNorm", "float"),
		("fPartsMaskA__uiUNorm", "float"),
		("fPartsMaskB__uiUNorm", "float"),
		("fPartsMaskC__uiUNorm", "float"),
		("fPartsMaskD__uiUNorm", "float"),
		("fPartsMaskX__uiUNorm", "float"),
		("fPartsMaskY__uiUNorm", "float"),
		("fPartsMaskZ__uiUNorm", "float"),
		("fPartsMaskW__uiUNorm", "float"),
		("bUseOffset", "bbool"),
		("fOffsetScale", "float"),
		("bTranslucentOffset", "bbool"),
		("bAntiSSSEmit", "bbool"),
		("fFlowDirDir__uiDirection", "float3"),

		("align3", "ubyte[4]"),
		("fFlowControl__uiUNorm", "float4"),
		("fFlowTile", "float"),

		("align4", "ubyte[12]"),
		("fFlowColor__uiColor", "float4"),
		("fFlowMatControl__uiUNorm", "float4"),
		("fFilmThickness__uiUNorm", "float"),
		("fFilmBlend__uiUNorm", "float"),
		("fFilmIOR__uiUNorm", "float"),
		("fRefraction__uiUNorm", "float"),
		("fRefractionBlend__uiUNorm", "float"),
		("fAlbedoBlend__uiUNorm", "float"),
		("fAnimEmitMin", "float"),
		("fAnimEmitSpeed", "float"),
		("bUseWaveEmit", "bbool"),
		("fAnimEmitWave", "float"),

		("align5", "ubyte[8]"),
		("fAnimEmitControl__uiUNorm", "float4"),
		("fRimAlphaPower__uiSNorm", "float"),
		("fRimTranslucency__uiUNorm", "float"),
		("fRimNormal__uiUNorm", "float"),
		("fSnowUVTile", "float"),
		("fSnowBlendColor__uiColor", "float4"),
		("fSnowMatControl__uiUNorm", "float4"),
		("fMaterialSnowBlendB", "float"),

		("align6", "ubyte[12]"),
		("fSnowControl", "float4"),

	])


class CBCapsuleAO(EPyCStruct):
	fields = OrderedDict([


		("fLightDirectionXYZAngle", "float4"),
		("fDistanceFallCoef", "float"),
		("fCapsuleAOIntensity", "float"),
		("uGeometryNum", "uint"),
		("uLightChannelMask", "uint"),

	])


class CBMhMaterialFakeInnerEmitLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fEmissiveMapFactor__uiColor", "float3"),
		("fInnerOffsetScale", "float"),
		("fRimAlphaPower__uiUNorm", "float"),
		("fVolumeBlend__uiSNorm", "float"),

	])


class CBImagePlane2(EPyCStruct):
	fields = OrderedDict([


		("fFilterUVMin", "float2"),
		("fFilterUVMax", "float2"),

	])


class CBMhMaterialNikuLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fTranslucency__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fUVTransformA", "float4"),
		("fNikuMode__uiUNorm", "float4"),

	])


class CBMhMaterialVfxDispWaveLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fUVTransformA", "float4"),
		("fUVTransformB", "float4"),
		("fAdditionalRot", "float3"),

		("align0", "ubyte[4]"),
		("fWaveAxis__uiSNorm", "float3"),

		("align1", "ubyte[4]"),
		("fWaveScale__uiUNorm", "float3"),
		("fWaveAngle", "float"),
		("fDetailDisplacement", "float"),
		("fYAxisDepth", "float"),
		("fWhiteWaterPow", "float"),
		("fFitRange", "float"),
		("fBaseMapFactor__uiColor", "float4"),
		("fDistortionFactor__uiColor", "float3"),

		("align2", "ubyte[4]"),
		("fCubeMapFactor__uiColor", "float3"),
		("fNormalFactor__uiUNorm", "float"),
		("fRaflectionAngle__uiSNorm", "float"),
		("fDistortionAngle", "float"),
		("fDistortion", "float"),
		("fOpacityFactor", "float"),
		("fVolumeBlend__uiSNorm", "float"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecularFactor", "float"),
		("fTranslucency__uiUNorm", "float"),
		("fDiffuseChroma__uiUNorm", "float"),
		("fSpecularChroma__uiUNorm", "float"),
		("bSceneEnvMap", "bbool"),
		("fInnerOffsetScale", "float"),
		("fVelocityAttn", "float"),
		("fNormalDecalBlend__uiUNorm", "float"),

	])


class CBSpeedTree(EPyCStruct):
	fields = OrderedDict([


		("fSpeedTreeParam", "float2"),

		("align0", "ubyte[8]"),
		("iSpeedTreeParam", "int3"),

	])


class CBMhMaterialVfxFloodLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float3"),

		("align0", "ubyte[4]"),
		("fDistortionFactor__uiColor", "float3"),

		("align1", "ubyte[4]"),
		("fCubeMapFactor__uiColor", "float3"),
		("fOpacityFactor", "float"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fDispFactor", "float"),

		("align2", "ubyte[4]"),
		("fUVTransformA", "float4"),
		("fUVTransformB", "float4"),
		("fUVTransformC", "float4"),
		("fVolumeBlend__uiSNorm", "float"),
		("fSpecularFactor", "float"),
		("bSceneEnvMap", "bbool"),
		("fRaflectionAngle__uiSNorm", "float"),
		("fDistortionAngle", "float"),
		("fDistortion", "float"),
		("fTranslucency__uiUNorm", "float"),
		("fDiffuseChroma__uiUNorm", "float"),
		("fSpecularChroma__uiUNorm", "float"),
		("fFlowSpeed", "float"),
		("fFlowStrength", "float"),
		("fWhiteWaterPow", "float"),
		("fWhiteWater", "float"),
		("fEdgeFoamPow", "float"),
		("fEdgeFoamFactor", "float"),
		("bEnableLava", "bbool"),
		("bEnableAlbedoBlend", "bbool"),
		("fHeat", "float"),
		("fInnerOffsetScale", "float"),
		("fAlbedoBlendPow", "float"),
		("fAlbedoBlendRate", "float"),
		("fAlbedoBlendFactor", "float"),

		("align3", "ubyte[8]"),
		("fAlbedoBlendVector", "float3"),
		("fVelocityAttn", "float"),
		("fNormalDecalBlend__uiUNorm", "float"),
		("bUseUVPrimaryOM", "bbool"),

	])


class CBPrimitiveDebug(EPyCStruct):
	fields = OrderedDict([


		("fWorldOffset", "float3"),

	])


class CBSystemColor(EPyCStruct):
	fields = OrderedDict([


		("fSystemColor", "float4"),

	])


class CBAmbientOcclusion(EPyCStruct):
	fields = OrderedDict([


		("iSSAOPrimaryReductionLevel", "int"),
		("iSSAOPrimaryFactor", "uint"),
		("fSSAOPrimaryScale", "float"),
		("fApproximateSSAOSamplePerPixel", "float"),
		("iApproximateSSAOMaxSampleNum", "uint"),
		("fApproximateSSAOBias", "float"),
		("fApproximateSSAOWeight", "float"),
		("fApproximateSSAOEdgeAttenRate", "float"),
		("fApproximateSSAORadiusMat", "float4x4"),
		("iApproximateSSAODepthMipBias", "uint"),
		("fPrimaryShadowRadius", "float"),
		("iPrimaryShadowSampleNum", "uint"),
		("fPrimaryShadowUpsampleThresholdMin", "float"),
		("fPrimaryShadowUpsampleThresholdMax", "float"),
		("fPrimaryShadowUpsampleThresholdDiffInv", "float"),

	])


class CBMhMaterialSlantFloor(EPyCStruct):
	fields = OrderedDict([


		("iSlantFloorWindIndex", "int"),
		("fSlantFloorWindScale", "float"),

	])


class CBMhMaterialScrIceBlendNoFurLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fDetailNormalBlend__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fUVTransformA", "float4"),
		("fUVTransformB", "float4"),
		("fTranslucency__uiUNorm", "float"),
		("fEmissiveBlendColor__uiColor", "float3"),
		("fEmissiveBlendColorBlend__uiUNorm", "float"),
		("fEmissiveBlendRimParam", "float3"),
		("fBlendBaseMapFactor__uiColor", "float4"),
		("fBlendEmissiveMapFactor__uiColor", "float3"),
		("fBlendMetalic__uiUNorm", "float"),
		("fBlendRoughness__uiUNorm", "float"),
		("fBlendDetailNormalBlend__uiUNorm", "float"),
		("fBlendSubSurfaceBlend__uiUNorm", "float"),

		("align1", "ubyte[4]"),
		("fBlendUVTransformA", "float4"),
		("fBlendUVTransformB", "float4"),
		("fBlendDir__uiDirection", "float3"),
		("fBlendPlaneNormal__uiUNorm", "float"),
		("fBlendOp", "float3"),
		("bUseUVSecondaryMtA", "bbool"),
		("bUseUVSecondaryMtB", "bbool"),
		("bUseUVSecondaryMtBM", "bbool"),

		("align2", "ubyte[8]"),
		("fWetBlendDir__uiDirection", "float3"),
		("fWetBlendPlaneNormal__uiUNorm", "float"),
		("fWetBlendOp", "float3"),
		("bSpecialBlend", "bbool"),
		("bWetNormalBlend", "bbool"),
		("fWetNormalBlendRange__uiUNorm", "float2"),
		("fIceVPushScale", "float"),
		("fIceLocalVPushScale", "float"),
		("bUseNormalDisplacement", "bbool"),

		("align3", "ubyte[8]"),
		("fIceVPushDir__uiDirection", "float3"),

		("align4", "ubyte[4]"),
		("fIceLocalVPushDir__uiDirection", "float3"),

		("align5", "ubyte[4]"),
		("fIcePushOp", "float3"),

		("align6", "ubyte[4]"),
		("fUVTransformC", "float4"),
		("fIceDisplacementUVSize", "float2"),
		("bUsePositionUV", "bbool"),

		("align7", "ubyte[4]"),
		("fAlbedoBlendMapGFactor__uiColor", "float3"),
		("fIceFresnelFactor__uiUNorm", "float"),
		("fIceColorBlend__uiUNorm", "float"),
		("bUseUVSecondaryMtIce", "bbool"),

	])


class CBMhMaterialFlowLavaLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fDetailNormalBlend__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fUVTransformA", "float4"),
		("fUVTransformB", "float4"),
		("fTranslucency__uiUNorm", "float"),
		("fEmissiveBlendColor__uiColor", "float3"),
		("fEmissiveBlendColorBlend__uiUNorm", "float"),
		("fEmissiveBlendRimParam", "float3"),
		("fFlowDirDir__uiDirection", "float3"),
		("fFlowDirUVPhaseShift__uiUNorm", "float"),
		("bFlowDirLocalSpace", "bbool"),
		("fFlowControl", "float"),
		("fEmitControl__uiUNorm", "float2"),

	])


class CBMhMaterialSpeedTreeStdLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fDetailNormalBlend__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fUVTransformA", "float4"),
		("fUVTransformB", "float4"),
		("fBaseMapModulation__uiUNorm", "float4"),
		("fTranslucency__uiUNorm", "float"),
		("bLightProbeEmissive", "bbool"),

		("align1", "ubyte[8]"),
		("fEmissiveBlendColor__uiColor", "float3"),
		("fEmissiveBlendColorBlend__uiUNorm", "float"),
		("fEmissiveBlendRimParam", "float3"),
		("bSpecialBlend", "bbool"),
		("fRoughnessThreshold__uiUNorm", "float"),
		("fRoughnessFillValue__uiUNorm", "float"),
		("bWetNormalBlend", "bbool"),

		("align2", "ubyte[4]"),
		("fWetNormalBlendRange__uiUNorm", "float2"),

	])


class CBWaterModel(EPyCStruct):
	fields = OrderedDict([


		("fMWorldViewProjMat", "float4x4"),
		("fMWorldMat", "float4x4"),

	])


class CBLightParameters_LightParameter(EPyCStruct):
	fields = OrderedDict([

		("position_boundingRadius", "float4"),
		("direction_falloff", "float4"),
		("misc_attenuation", "uint4"),
		("color", "float3"),
		("min_roughness", "float"),
		("shadow_mat", "float4x4"),
		("texproj_mat", "float4x4"),
		("shadow_extra", "float4"),
		("shadowmap_size_region", "uint4"),

	])

class CBLightParameters  (Mod3Container):
	Mod3Class = CBLightParameters_LightParameter
	baseCount = 256	


class CB_TemporalAA(EPyCStruct):
	fields = OrderedDict([


		("fReprojectionOffset", "float2"),
		("fReprojectionScale", "float2"),
		("fTemporalOffset", "float2"),
		("fTemporalScale", "float2"),
		("fTemporalClampMin", "float2"),
		("fTemporalClampMax", "float2"),
		("fBlendRate", "float"),
		("bVelocityBase", "bbool"),

	])


class CB_PlantOnSurface(EPyCStruct):
	fields = OrderedDict([


		("fScale", "float3"),
		("iNumPerTriangle", "uint"),
		("iTriangleNum", "uint"),
		("iIndexOffset", "uint"),
		("fRotRandomize", "float"),
		("fDirRandomize", "float"),
		("fScaleRandomize", "float"),

	])


class CBImagePlane(EPyCStruct):
	fields = OrderedDict([


		("fImagePlaneColor", "float4"),
		("fImagePlaneUVTransform", "float4x4"),
		("fImagePlaneTechnique", "uint"),
		("fBlendType", "uint"),
		("bIsScreenPass", "bbool"),
		("fGamma", "float"),

	])


class CBMhMaterialEM125Local__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fTranslucency__uiUNorm", "float"),
		("bBaseColorEmissive", "bbool"),
		("fPaintUVTile", "float2"),
		("fAddNormalBlend__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fAddNormalMaskA__uiSNorm", "float4"),
		("fAddNormalMaskB__uiSNorm", "float4"),
		("fAddNormalMaskC__uiUNorm", "float"),
		("fAddNormalMaskD__uiUNorm", "float"),
		("bBackFaceShading", "bbool"),
		("bBackFaceNormalFilp", "bbool"),
		("fKizuColor__uiColor", "float3"),

		("align1", "ubyte[4]"),
		("fKizuUVOffset__uiUNorm", "float2"),
		("fKizuMultiply", "float"),
		("bLegendary", "bbool"),
		("fLegendColor__uiColor", "float4"),
		("fLegendMetalMask__uiUNorm", "float2"),
		("fLegendRoughness", "float"),

		("align2", "ubyte[4]"),
		("fLegendFilm__uiUNorm", "float3"),
		("fLegendSSSMask__uiUNorm", "float"),
		("fLegendHSV__uiSNorm", "float3"),
		("fLegendFilmIOR__uiUNorm", "float"),
		("fPartsMaskA__uiUNorm", "float"),
		("fPartsMaskB__uiUNorm", "float"),
		("fPartsMaskC__uiUNorm", "float"),
		("fPartsMaskD__uiUNorm", "float"),
		("fPartsMaskX__uiUNorm", "float"),
		("fPartsMaskY__uiUNorm", "float"),
		("fPartsMaskZ__uiUNorm", "float"),
		("fPartsMaskW__uiUNorm", "float"),
		("bUseOffset", "bbool"),
		("fOffsetScale", "float"),
		("bTranslucentOffset", "bbool"),
		("bAntiSSSEmit", "bbool"),
		("fFlowDirDir__uiDirection", "float3"),

		("align3", "ubyte[4]"),
		("fFlowControl__uiUNorm", "float4"),
		("fFlowTile", "float"),

		("align4", "ubyte[12]"),
		("fFlowColor__uiColor", "float4"),
		("fFlowMatControl__uiUNorm", "float4"),
		("fMaskBlend__uiUNorm", "float4"),
		("fMaskBlend_A__uiUNorm", "float2"),
		("fMaskBlend_B__uiUNorm", "float2"),
		("fFilmThickness__uiUNorm", "float"),
		("fFilmBlend__uiUNorm", "float"),
		("fFilmIOR__uiUNorm", "float"),
		("fRefraction__uiUNorm", "float"),
		("fRefractionBlend__uiUNorm", "float"),
		("fAnimEmitMin", "float"),
		("fAnimEmitSpeed", "float"),
		("bUseWaveEmit", "bbool"),
		("fAnimEmitWave", "float"),
		("fRimAlphaPower__uiSNorm", "float"),
		("fRimTranslucency__uiUNorm", "float"),
		("fRimNormal__uiUNorm", "float"),
		("fFinWave", "float"),
		("fFinSpeed", "float"),
		("fFinSpectral__uiUNorm", "float"),

		("align5", "ubyte[4]"),
		("fFinColor__uiColor", "float3"),
		("fFinWaveB", "float"),
		("fFinSpeedB", "float"),
		("fFinSpectralB__uiUNorm", "float"),

		("align6", "ubyte[8]"),
		("fFinColorB__uiColor", "float3"),
		("fBaseColorSaturation__uiUNorm", "float"),
		("fSaturationColor__uiColor", "float3"),
		("bUseFullNormal", "bbool"),
		("fSnowUVTile", "float"),

		("align7", "ubyte[12]"),
		("fSnowBlendColor__uiColor", "float4"),
		("fSnowMatControl__uiUNorm", "float4"),
		("fMaterialSnowBlendB", "float"),

		("align8", "ubyte[12]"),
		("fSnowControl", "float4"),

	])


class CBPrimitiveEx(EPyCStruct):
	fields = OrderedDict([


		("fPrimParamEx0", "float4"),
		("fPrimParamEx1", "float4"),
		("fPrimParamEx2", "float4"),
		("iPrimParamEx3", "uint4"),

	])


class cbHBAO(EPyCStruct):
	fields = OrderedDict([


		("HBAORadiusToScreen", "float"),
		("HBAONegInvR2", "float"),
		("HBAONDotVBias", "float"),
		("HBAOAoMultiplier", "float"),
		("HBAOSmallScaleAOAmount", "float"),
		("HBAOLargeScaleAOAmount", "float"),
		("HBAONormalBlendRate", "float"),

	])


class CBMhMaterialNPCEyeLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fTranslucency__uiUNorm", "float"),
		("bBaseColorEmissive", "bbool"),
		("bBackFaceNormalFilp", "bbool"),
		("fAnimEmitMin", "float"),
		("fAnimEmitSpeed", "float"),
		("fParallaxFactor__uiUNorm", "float"),
		("fDetailNormalBlend__uiUNorm", "float"),

		("align0", "ubyte[4]"),
		("fUVTransformDetailNormal", "float4"),

	])


class CBMhMaterialFlagWaveLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fTranslucency__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fUVTransformA", "float4"),
		("fVPushScale", "float"),
		("fVPushWave", "float"),
		("fVPushSpeed", "float"),

		("align1", "ubyte[4]"),
		("fFlagUvEditA", "float4"),
		("fFlagUvEditB", "float4"),
		("fFlagControl", "float4"),
		("fDisplaceControl", "float4"),
		("fDispFactor", "float"),

	])


class CBMhMaterialVfxDebufBodyLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fUVTransformA", "float4"),
		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fNormalFactor__uiUNorm", "float"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fTranslucency__uiUNorm", "float"),
		("fSpecularFactor", "float"),
		("fOpacityFactor", "float"),
		("fRimOpacityPow", "float"),
		("fVolumeBlend__uiSNorm", "float"),

		("align0", "ubyte[4]"),
		("fFlowDir__uiDirection", "float3"),
		("fFlowStrength", "float"),
		("fFlowSpeed", "float"),
		("fDiffuseChroma__uiUNorm", "float"),
		("fSpecularChroma__uiUNorm", "float"),
		("fInnerOffsetScale", "float"),
		("fVelocityAttn", "float"),
		("fNormalDecalBlend__uiUNorm", "float"),

	])


class CBContactShadowInfo(EPyCStruct):
	fields = OrderedDict([


		("fContactShadowLengthCoefs", "float4"),
		("fContactShadowOptimizeParams", "float3"),

		("align0", "ubyte[4]"),
		("fContactShadowDirection", "float3"),
		("bIsUseNoise", "bbool"),
		("bIsUseContactShadow", "bbool"),

	])


class CBSnowShoveler(EPyCStruct):
	fields = OrderedDict([


		("fMinMaxRangeWorldY", "float4"),

	])


class CBLUTBlending(EPyCStruct):
	fields = OrderedDict([


		("fLUTBlend", "float"),
		("fVfxLUTBlend", "float"),
		("bIsBlend", "bbool"),
		("bIsVfxBlend", "bbool"),

	])


class CBPrimitive(EPyCStruct):
	fields = OrderedDict([


		("fPrimParam0", "float4"),
		("fPrimParam1", "float4"),
		("fPrimParam2", "float4"),
		("fPrimParam3", "float4"),
		("fPrimParam4", "float4"),
		("fPrimParam5", "float4"),
		("fPrimParam6", "float4"),
		("fPrimParam7", "float4"),
		("fPrimParam8", "float4"),
		("fPrimParam9", "float4"),
		("iPrimParam0", "uint4"),

	])


class CBErrorUnit(EPyCStruct):
	fields = OrderedDict([


		("iErrorUnitAddress", "uint2"),
		("iErrorUnitPass", "uint"),
		("iErrorUnitPrio", "uint"),

	])


class CBMhMaterialSpeedTreeStdIceLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fDetailNormalBlend__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fUVTransformA", "float4"),
		("fUVTransformB", "float4"),
		("fBaseMapModulation__uiUNorm", "float4"),
		("fTranslucency__uiUNorm", "float"),
		("bLightProbeEmissive", "bbool"),

		("align1", "ubyte[8]"),
		("fEmissiveBlendColor__uiColor", "float3"),
		("fEmissiveBlendColorBlend__uiUNorm", "float"),
		("fEmissiveBlendRimParam", "float3"),
		("bSpecialBlend", "bbool"),
		("fRoughnessThreshold__uiUNorm", "float"),
		("fRoughnessFillValue__uiUNorm", "float"),
		("bWetNormalBlend", "bbool"),

		("align2", "ubyte[4]"),
		("fWetNormalBlendRange__uiUNorm", "float2"),
		("fSnowAlphaRef__uiUNorm", "float"),

		("align3", "ubyte[4]"),
		("fSnowBaseMapFactor__uiColor", "float4"),
		("fSnowEmissiveMapFactor__uiColor", "float3"),
		("fSnowMetalic__uiUNorm", "float"),
		("fSnowRoughness__uiUNorm", "float"),
		("fSnowDetailNormalBlend__uiUNorm", "float"),
		("fSnowSubSurfaceBlend__uiUNorm", "float"),

		("align4", "ubyte[4]"),
		("fSnowUVTransformA", "float4"),
		("fSnowUVTransformB", "float4"),
		("fSnowDir__uiDirection", "float3"),
		("fSnowPlaneNormal__uiUNorm", "float"),
		("fSnowOp", "float3"),
		("bUseUVSecondarySnowMt", "bbool"),
		("bUseUVSecondarySnowMtBM", "bbool"),
		("fAlbedoBlendMapGFactor__uiColor", "float3"),
		("fIceFresnelFactor__uiUNorm", "float"),
		("fIceColorBlend__uiUNorm", "float"),
		("bUseUVSecondaryMtIce", "bbool"),

	])


class CBSnowFieldMaterial(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor", "float4"),
		("fEmissiveMapFactor", "float3"),
		("fRoughness", "float"),
		("fMetalic", "float"),
		("fTranslucency", "float"),
		("fDetailNormalBlend", "float"),

		("align0", "ubyte[4]"),
		("fUVTransformA", "float4"),
		("fUVTransformB", "float4"),
		("fUVTransformUnder", "float4"),
		("fVolumeBlend", "float"),
		("fDecalMaskAlphaRef", "float"),
		("bHeightMapClip", "bbool"),
		("fHeightMapClipRef", "float"),
		("fUVRotationSin", "float"),
		("fUVRotationCos", "float"),
		("fUnderTextureBlendFactor", "float2"),

	])


class CBWaterWaveMaterial(EPyCStruct):
	fields = OrderedDict([


		("fReflectionViewProj", "float4x4"),
		("fUserNormalTiling", "float2"),
		("fUserNormalIntensity", "float"),
		("fUserNormalMoveSpeed", "float"),
		("fUserNormalMoveDirection", "float2"),
		("fUserNormal2Tiling", "float2"),
		("fUserNormal2Intensity", "float"),
		("fUserNormal2MoveSpeed", "float"),
		("fUserNormal2MoveDirection", "float2"),
		("fInvDepthMax", "float"),
		("fReflectionDistortion", "float"),
		("fFresnelBias", "float"),
		("fHorizonBias", "float"),
		("fExtinctionCoefficient", "float3"),
		("fMurkiness", "float"),
		("fWaterColor", "float3"),
		("fRefractionDistortion", "float"),
		("fCausticsTiling", "float2"),
		("fCausticsIntensity", "float"),
		("fCausticsMoveSpeed", "float"),
		("fCausticsMoveDirection", "float2"),
		("fCausticsDensityLow", "float"),
		("fRefactionIndex", "float"),
		("fSlopeVariance", "float2"),
		("fSunlightReflectanceRange", "float2"),
		("fReflectanceBiasRate", "float"),
		("fInvDepthFade", "float"),
		("fSunlightReflectionIntensity", "float"),
		("fCubemapBlendRate", "float"),
		("iLightGroup", "uint"),

	])


class CBSnowPreProcess(EPyCStruct):
	fields = OrderedDict([


		("fNoiseBlendSVScale", "float"),
		("fNoiseHeightScale", "float"),
		("fNoiseBlendBias", "float"),

	])


class CBMhMaterialFlagWaveBlendLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fTranslucency__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fUVTransformA", "float4"),
		("fVPushScale", "float"),
		("fVPushWave", "float"),
		("fVPushSpeed", "float"),

		("align1", "ubyte[4]"),
		("fFlagUvEditA", "float4"),
		("fFlagUvEditB", "float4"),
		("fFlagControl", "float4"),
		("fDisplaceControl", "float4"),
		("fDispFactor", "float"),

		("align2", "ubyte[12]"),
		("fBlendBaseMapFactor__uiColor", "float4"),
		("fBlendEmissiveMapFactor__uiColor", "float3"),
		("fBlendMetalic__uiUNorm", "float"),
		("fBlendRoughness__uiUNorm", "float"),
		("fBlendSpecular__uiUNorm", "float"),
		("fBlendSubSurfaceBlend__uiUNorm", "float"),

		("align3", "ubyte[4]"),
		("fBlendUVTransformA", "float4"),
		("bUseUVSecondaryMtBM", "bbool"),

	])


class CBMhMaterialScrIceLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fDetailNormalBlend__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fUVTransformA", "float4"),
		("fUVTransformB", "float4"),
		("fBaseMapModulation__uiUNorm", "float4"),
		("fTranslucency__uiUNorm", "float"),
		("fEmissiveBlendColor__uiColor", "float3"),
		("fEmissiveBlendColorBlend__uiUNorm", "float"),
		("fEmissiveBlendRimParam", "float3"),
		("bSpecialBlend", "bbool"),
		("fFurNormalBlend__uiUNorm", "float"),
		("fFurHeight__uiUNorm", "float"),
		("fFurMapBlend__uiUNorm", "float"),
		("fFurEdgeBlend__uiUNorm", "float"),
		("fFurTile", "float"),
		("bFakeRefraction", "bbool"),
		("fRefraction__uiUNorm", "float"),
		("fWetBlendDir__uiDirection", "float3"),
		("fWetBlendPlaneNormal__uiUNorm", "float"),
		("fWetBlendOp", "float3"),
		("bWetNormalBlend", "bbool"),
		("fWetNormalBlendRange__uiUNorm", "float2"),
		("fVolumeBlend__uiSNorm", "float"),
		("fIceVPushScale", "float"),
		("fIceLocalVPushScale", "float"),
		("bUseNormalDisplacement", "bbool"),

		("align1", "ubyte[8]"),
		("fIceVPushDir__uiDirection", "float3"),

		("align2", "ubyte[4]"),
		("fIceLocalVPushDir__uiDirection", "float3"),

		("align3", "ubyte[4]"),
		("fIcePushOp", "float3"),

		("align4", "ubyte[4]"),
		("fIceDisplacementUVSize", "float2"),
		("bUsePositionUV", "bbool"),

		("align5", "ubyte[4]"),
		("fUVTransformC", "float4"),
		("fAlbedoBlendMapGFactor__uiColor", "float3"),
		("fIceFresnelFactor__uiUNorm", "float"),
		("fIceColorBlend__uiUNorm", "float"),

	])


class CBScreen(EPyCStruct):
	fields = OrderedDict([


		("fScreenOffset", "float2"),
		("fScreenScale", "float2"),
		("fScreenSize", "float2"),
		("fScreenInverseSize", "float2"),
		("iViewOffset", "uint2"),
		("iViewSize", "uint2"),
		("fViewOffset", "float2"),
		("fViewSize", "float2"),
		("fViewInverseSize", "float2"),
		("fContentScale", "float"),
		("fContentScalePF", "float"),
		("fContentScaleBase", "float"),
		("fContentScaleActual", "float"),
		("fContentScaleInverse", "float"),
		("fContentScaleBaseInverse", "float"),
		("fContentScaleActualInverse", "float"),
		("fContentScalePassScreen", "float"),
		("bCheckerboard", "bbool"),

	])


class CBDecalCommon(EPyCStruct):
	fields = OrderedDict([


		("fDecalColor", "float4"),
		("fDecalCenter", "float3"),

		("align0", "ubyte[4]"),
		("fDecalRange", "float3"),

		("align1", "ubyte[4]"),
		("fDecalUVRange", "float4"),
		("fDecalTangent", "float3"),

		("align2", "ubyte[4]"),
		("fDecalBinormal", "float3"),

	])


class CBMhMaterialVfxIceLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fDetailNormalBlend__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fUVTransformA", "float4"),
		("fUVTransformB", "float4"),
		("fBaseMapModulation__uiUNorm", "float4"),
		("fTranslucency__uiUNorm", "float"),
		("fEmissiveBlendColor__uiColor", "float3"),
		("fEmissiveBlendColorBlend__uiUNorm", "float"),
		("fEmissiveBlendRimParam", "float3"),
		("bSpecialBlend", "bbool"),
		("fFurNormalBlend__uiUNorm", "float"),
		("fFurHeight__uiUNorm", "float"),
		("fFurMapBlend__uiUNorm", "float"),
		("fFurEdgeBlend__uiUNorm", "float"),
		("fFurTile", "float"),
		("bFakeRefraction", "bbool"),
		("fRefraction__uiUNorm", "float"),
		("fWetBlendDir__uiDirection", "float3"),
		("fWetBlendPlaneNormal__uiUNorm", "float"),
		("fWetBlendOp", "float3"),
		("bWetNormalBlend", "bbool"),
		("fWetNormalBlendRange__uiUNorm", "float2"),
		("fVolumeBlend__uiSNorm", "float"),
		("fDispFactor", "float"),
		("fInnerOffsetScale", "float"),
		("fFakeLightColor__uiColor", "float3"),
		("fFakeLightIntensity", "float"),
		("fFakeLightPosition", "float3"),
		("fFakeLightRadius", "float"),

		("align1", "ubyte[12]"),
		("fUVTransformC", "float4"),
		("fAlbedoBlendMapGFactor__uiColor", "float3"),
		("fIceFresnelFactor__uiUNorm", "float"),
		("fIceColorBlend__uiUNorm", "float"),

	])


class CBDebug(EPyCStruct):
	fields = OrderedDict([


		("iDebugView", "int"),
		("iDebugViewChannel", "int"),
		("iDebugLightMaxCount", "int"),
		("fDebugViewBgAlpha", "float"),
		("fDebugViewFgAlpha", "float"),
		("fDebugViewScaling", "float2"),

	])


class CBMhMaterialArrayLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fTranslucency__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fUVTransformA", "float4"),
		("fArray_Speed", "float"),

		("align1", "ubyte[12]"),
		("fArrayOrig", "float4"),

	])


class CBColorCorrectCube(EPyCStruct):
	fields = OrderedDict([


		("fLinearFactor", "float"),
		("fDepthNear", "float"),
		("fDepthFar", "float"),

	])


class CBMhDecalSM(EPyCStruct):
	fields = OrderedDict([


		("fFireFactor", "float"),
		("fFireLifeFactor", "float"),
		("fFireAlphaFactor", "float"),
		("fFireColorRate", "float"),
		("bFireLighting", "bbool"),
		("fFireColor", "float3"),
		("fSmokeFactor", "float"),
		("fSmokeLifeFactor", "float"),
		("bSmokeLighting", "bbool"),

		("align0", "ubyte[4]"),
		("fSmokeColor", "float3"),
		("fWaterColorRate", "float"),
		("fWaterColorSpecular", "float3"),

		("align1", "ubyte[4]"),
		("fWaterColorSheet", "float3"),
		("fWaterIntensitySpecular", "float"),
		("fWaterLerpGtoB", "float"),
		("fWaterIntensitySheet", "float"),
		("fWaterSpecularLifeFactor", "float"),
		("fWaterSheetLifeFactor", "float"),
		("fWaterGtoBLifeFactor", "float"),
		("fWaterIntensityCubeMap", "float"),
		("fWaterNormalSharpness", "float"),
		("fWaterIntensityAlpha", "float"),

	])


class CBWaterPick(EPyCStruct):
	fields = OrderedDict([


		("iWaterAddress", "uint2"),

	])


class CBMhMaterialEM115Local__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fTranslucency__uiUNorm", "float"),
		("bBaseColorEmissive", "bbool"),
		("fPaintUVTile", "float2"),
		("fAddNormalBlend__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fAddNormalMaskA__uiSNorm", "float4"),
		("fAddNormalMaskB__uiSNorm", "float4"),
		("fAddNormalMaskC__uiUNorm", "float"),
		("fAddNormalMaskD__uiUNorm", "float"),
		("bBackFaceShading", "bbool"),
		("bBackFaceNormalFilp", "bbool"),
		("fKizuColor__uiColor", "float3"),

		("align1", "ubyte[4]"),
		("fKizuUVOffset__uiUNorm", "float2"),
		("fKizuMultiply", "float"),
		("bLegendary", "bbool"),
		("fLegendColor__uiColor", "float4"),
		("fLegendMetalMask__uiUNorm", "float2"),
		("fLegendRoughness", "float"),

		("align2", "ubyte[4]"),
		("fLegendFilm__uiUNorm", "float3"),
		("fLegendSSSMask__uiUNorm", "float"),
		("fLegendHSV__uiSNorm", "float3"),
		("fLegendFilmIOR__uiUNorm", "float"),
		("fPartsMaskA__uiUNorm", "float"),
		("fPartsMaskB__uiUNorm", "float"),
		("fPartsMaskC__uiUNorm", "float"),
		("fPartsMaskD__uiUNorm", "float"),
		("fPartsMaskX__uiUNorm", "float"),
		("fPartsMaskY__uiUNorm", "float"),
		("fPartsMaskZ__uiUNorm", "float"),
		("fPartsMaskW__uiUNorm", "float"),
		("bUseOffset", "bbool"),
		("fOffsetScale", "float"),
		("bTranslucentOffset", "bbool"),
		("bAntiSSSEmit", "bbool"),
		("fFlowDirDir__uiDirection", "float3"),

		("align3", "ubyte[4]"),
		("fFlowControl__uiUNorm", "float4"),
		("fFlowTile", "float"),

		("align4", "ubyte[12]"),
		("fFlowColor__uiColor", "float4"),
		("fFlowMatControl__uiUNorm", "float4"),
		("fDisplaceControl", "float4"),
		("fDispSpeed", "float"),

		("align5", "ubyte[12]"),
		("fBlendBaseMapFactor__uiColor", "float4"),
		("bUseSpecialMode", "bbool"),
		("fFilmThickness__uiUNorm", "float"),
		("fFilmBlend__uiUNorm", "float"),
		("fFilmIOR__uiUNorm", "float"),
		("fRefraction__uiUNorm", "float"),
		("fRefractionBlend__uiUNorm", "float"),
		("fAnimEmitMin", "float"),
		("fAnimEmitSpeed", "float"),
		("bUseWaveEmit", "bbool"),
		("fAnimEmitWave", "float"),

		("align6", "ubyte[8]"),
		("fFurParam__uiUNorm", "float4"),
		("fFurTile", "float"),
		("fRimAlphaPower__uiSNorm", "float"),
		("fRimTranslucency__uiUNorm", "float"),
		("fRimNormal__uiUNorm", "float"),
		("fSnowUVTile", "float"),

		("align7", "ubyte[12]"),
		("fSnowBlendColor__uiColor", "float4"),
		("fSnowMatControl__uiUNorm", "float4"),
		("fMaterialSnowBlendB", "float"),

		("align8", "ubyte[12]"),
		("fSnowControl", "float4"),

	])


class CBHeightToNormal(EPyCStruct):
	fields = OrderedDict([


		("fFactor", "float"),

	])


class CBMhMaterialPLHairLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fTranslucency__uiUNorm", "float"),
		("bBaseColorEmissive", "bbool"),
		("bBackFaceNormalFilp", "bbool"),
		("fAnimEmitMin", "float"),
		("fAnimEmitSpeed", "float"),

		("align0", "ubyte[12]"),
		("fPrimaryColor__uiColor", "float4"),
		("fSecondaryColor__uiColor", "float4"),
		("fPrimaryExpo__uiUNorm", "float"),
		("fSecondaryExpo__uiUNorm", "float"),
		("fPrimaryShift__uiSNorm", "float"),
		("fSecondaryShift__uiSNorm", "float"),
		("fShininess", "float"),
		("fFakeLight__uiDirection", "float3"),
		("fFurNMHeight", "float"),

		("align1", "ubyte[12]"),
		("fFurParam__uiUNorm", "float4"),
		("fFurTile", "float"),

		("align2", "ubyte[12]"),
		("fVertexAO__uiColor", "float4"),
		("fVColorNormalBlend__uiUNorm", "float"),
		("fRimWidth__uiUNorm", "float"),
		("fRimNormalBlend__uiUNorm", "float"),
		("bUseRimTranslucency", "bbool"),
		("bUseOffset", "bbool"),
		("fInnerOffsetScale", "float"),
		("fDetailNormalBlend__uiUNorm", "float"),

		("align3", "ubyte[4]"),
		("fUVTransformDetailNormal", "float4"),

	])


class CBSpeedTreeGlobalWindPF_SpeedTreeGlobalWind(EPyCStruct):
	fields = OrderedDict([

		("fBillboardTexCoords", "uint4x4[3]"),
		("fWindVector", "float4"),
		("fWindGlobal", "float4"),
		("fWindBranch", "float4"),
		("fWindBranchTwitch", "float4"),
		("fWindLeaf1Tumble", "float4"),
		("fWindLeaf2Tumble", "float4"),
		("fWindBranchAnchor", "float3"),
		("fWindBranchAdherences_x", "float"),
		("fWindBranchAdherences_y", "float"),
		("fWindBranchAdherences_z", "float"),
		("fWindFrondRipple_x", "float"),
		("fWindFrondRipple_y", "float"),
		("fWindFrondRipple_z", "float"),
		("fWindLeaf1Twitch", "float3"),
		("fWindLeaf2Twitch", "float3"),
		("fLocalGlobalDistance", "float"),
		("fWindLeaf1Ripple", "float2"),
		("fWindLeaf2Ripple", "float2"),
		("fWindBranchWhip", "float2"),
		("fWindTurbulences", "float2"),
		("fLocalBranchDistance", "float2"),
		("iWindAttr", "uint"),
		("padding_0", "float"),

	])

class CBSpeedTreeGlobalWindPF  (Mod3Container):
	Mod3Class = CBSpeedTreeGlobalWindPF_SpeedTreeGlobalWind
	baseCount = 160	


class CBVRVolumeParams_VolumeParam(EPyCStruct):
	fields = OrderedDict([

		("packedData", "uint"),
		("emissive", "float3"),
		("scattering", "float3"),
		("hgEccentricity", "float"),
		("tiling", "float3"),
		("moveSpeed", "float"),
		("moveDir", "float3"),
		("dispelFactor", "float"),

	])

class CBVRVolumeParams_Constant(EPyCStruct):
	fields = OrderedDict([

		("limits", "float3"),
		("extra", "uint"),

	])

class CBVRVolumeParams_Cuboid(EPyCStruct):
	fields = OrderedDict([

		("model", "float4x4"),
		("modelI", "float4x4"),
		("minAABB", "float4"),
		("maxAABB", "float4"),

	])

class CBVRVolumeParams_Spherical(EPyCStruct):
	fields = OrderedDict([

		("model", "float4x4"),
		("modelI", "float4x4"),
		("extra", "uint4"),

	])

class CBVRVolumeParams_Spotlight(EPyCStruct):
	fields = OrderedDict([

		("origin", "float3"),
		("height", "float"),
		("dir", "float3"),
		("cosAngle", "float"),

	])
    
class CBVRVolumeParams  (Mod3Collection):
    Mod3Classes = [CBVRVolumeParams_VolumeParam, CBVRVolumeParams_Constant,
                CBVRVolumeParams_Cuboid, CBVRVolumeParams_Spherical, CBVRVolumeParams_Spotlight]
    Mod3Counts = [128,128,128,128,128]


class CB_BGTexture(EPyCStruct):
	fields = OrderedDict([


		("fBGTextureColor", "float4"),

	])


class CBHermiteCurve(EPyCStruct):
	fields = OrderedDict([


		("fHermiteParam", "float4[8]"),

	])


class CBMhMaterialScrWaterLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),

		("align0", "ubyte[4]"),
		("fCubeMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fTranslucency__uiUNorm", "float"),

		("align1", "ubyte[12]"),
		("fUVTransformA", "float4"),
		("fUVTransformB", "float4"),
		("fUVOffsetSpeedFactor", "float2"),
		("fUVOffsetSpeedFactorDetail", "float2"),
		("fDetailNormalBlend__uiUNorm", "float"),
		("fRefraction__uiUNorm", "float"),
		("fRefractionPow__uiUNorm", "float"),

		("align2", "ubyte[4]"),
		("fRefractionFactor__uiColor", "float3"),
		("bRefractionScreenFade", "bbool"),
		("fVolumeBlend__uiSNorm", "float"),
		("fFlowStrength", "float"),
		("fFlowSpeed", "float"),
		("bDecalMode", "bbool"),

	])


class CBTubeLight(EPyCStruct):
	fields = OrderedDict([


		("iTubeLightCount", "uint"),

	])


class CBModel(EPyCStruct):
	fields = OrderedDict([


		("fWorld", "float3x4"),
		("fWorldI", "float3x4"),
		("fWorldPF", "float3x4"),
		("iMatrixIndex", "uint"),
		("iMatrixIndexPF", "uint"),
		("iLightChannel", "uint"),

		("align0", "ubyte[4]"),
		("iUnitAddress", "uint2"),
		("bPositionPFValid", "bbool"),
		("bPassThrough", "bbool"),
		("bInstanceMaterialEdit", "bbool"),
		("bInstanceEffect", "bbool"),

	])


class CBPrimBufferDescription(EPyCStruct):
	fields = OrderedDict([


		("iPrimVertexBufferOffset", "uint"),
		("iPrimTotalVertexNum", "uint"),
		("iPrimRequestNum", "uint"),

	])


class CBMhMaterialSZK001Local__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fTranslucency__uiUNorm", "float"),
		("bBaseColorEmissive", "bbool"),
		("fPaintUVTile", "float2"),
		("fAddNormalBlend__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fAddNormalMaskA__uiSNorm", "float4"),
		("fAddNormalMaskB__uiSNorm", "float4"),
		("fAddNormalMaskC__uiUNorm", "float"),
		("fAddNormalMaskD__uiUNorm", "float"),
		("bBackFaceShading", "bbool"),
		("bBackFaceNormalFilp", "bbool"),
		("fKizuColor__uiColor", "float3"),

		("align1", "ubyte[4]"),
		("fKizuUVOffset__uiUNorm", "float2"),
		("fKizuMultiply", "float"),
		("bLegendary", "bbool"),
		("fLegendColor__uiColor", "float4"),
		("fLegendMetalMask__uiUNorm", "float2"),
		("fLegendRoughness", "float"),

		("align2", "ubyte[4]"),
		("fLegendFilm__uiUNorm", "float3"),
		("fLegendSSSMask__uiUNorm", "float"),
		("fLegendHSV__uiSNorm", "float3"),
		("fLegendFilmIOR__uiUNorm", "float"),
		("fPartsMaskA__uiUNorm", "float"),
		("fPartsMaskB__uiUNorm", "float"),
		("fPartsMaskC__uiUNorm", "float"),
		("fPartsMaskD__uiUNorm", "float"),
		("fPartsMaskX__uiUNorm", "float"),
		("fPartsMaskY__uiUNorm", "float"),
		("fPartsMaskZ__uiUNorm", "float"),
		("fPartsMaskW__uiUNorm", "float"),
		("bUseOffset", "bbool"),
		("fOffsetScale", "float"),
		("bTranslucentOffset", "bbool"),
		("bAntiSSSEmit", "bbool"),
		("fFlowDirDir__uiDirection", "float3"),

		("align3", "ubyte[4]"),
		("fFlowControl__uiUNorm", "float4"),
		("fFlowTile", "float"),

		("align4", "ubyte[12]"),
		("fFlowColor__uiColor", "float4"),
		("fFlowMatControl__uiUNorm", "float4"),
		("fFilmThickness__uiUNorm", "float"),
		("fFilmBlend__uiUNorm", "float"),
		("fFilmIOR__uiUNorm", "float"),
		("fRefraction__uiUNorm", "float"),
		("fRefractionBlend__uiUNorm", "float"),
		("fAnimEmitMin", "float"),
		("fAnimEmitSpeed", "float"),
		("bUseWaveEmit", "bbool"),
		("fAnimEmitWave", "float"),

		("align5", "ubyte[12]"),
		("fFurParam__uiUNorm", "float4"),
		("fFurTile", "float"),
		("fAlbedoBlend__uiUNorm", "float"),

		("align6", "ubyte[8]"),
		("fBlendBaseMapFactor__uiColor", "float4"),
		("fBlendMatFactor", "float4"),
		("bAlbedoOverUVsecondary", "bbool"),
		("bUseSpecialMode", "bbool"),
		("fRimAlphaPower__uiSNorm", "float"),
		("fRimTranslucency__uiUNorm", "float"),
		("fRimNormal__uiUNorm", "float"),
		("fSnowUVTile", "float"),

		("align7", "ubyte[8]"),
		("fSnowBlendColor__uiColor", "float4"),
		("fSnowMatControl__uiUNorm", "float4"),
		("fMaterialSnowBlendB", "float"),

		("align8", "ubyte[12]"),
		("fSnowControl", "float4"),

	])


class CBGUIDistanceField(EPyCStruct):
	fields = OrderedDict([


		("fGUIDFParam0", "float3"),

		("align0", "ubyte[4]"),
		("fGUIDFColor0", "float4"),
		("fGUIDFParam1", "float3"),

		("align1", "ubyte[4]"),
		("fGUIDFColor1", "float4"),

	])


class CBMhSky2SimplePS(EPyCStruct):
	fields = OrderedDict([


		("fSkyGlobalIntensity", "float3"),

		("align0", "ubyte[4]"),
		("fSkyWaterReflectionFactor", "float3"),
		("bSkyFog", "bbool"),
		("fSkyFogBlend", "float"),
		("bSkyDeGamma", "bbool"),
		("fGamma", "float"),

		("align1", "ubyte[4]"),
		("iSkyAddress", "uint2"),
		("fSkyTopCloudUVScale0", "float2"),
		("fSkyTopCloudUVScale1", "float2"),
		("fSkyCloudContrast", "float"),
		("fSkyCurveMapTexelHeight", "float"),
		("fSkyAlpha", "float"),

		("align2", "ubyte[12]"),
		("fSkyBaseMapFactor", "float4"),
		("fSkyBaseSideCloudUVOffset", "float2"),
		("fSkyBaseTopCloudUVOffset0", "float2"),
		("fSkyBaseTopCloudUVOffset1", "float2"),

		("align3", "ubyte[8]"),
		("fSkyCloudSpeeds", "float2[4]"),

		("align4", "ubyte[8]"),
		("fSkySunCloudHighlightColors", "float4[4]"),
		("fSkySunCloudShadowColors", "float4[4]"),
		("fSkyMiddleCloudHighlightColors", "float4[4]"),
		("fSkyMiddleCloudShadowColors", "float4[4]"),
		("fSkyBackgroundCloudHighlightColors", "float4[4]"),
		("fSkyBackgroundCloudShadowColors", "float4[4]"),
		("fSkyCloudAlpha", "float[4]"),

	])


class CBWorkaround(EPyCStruct):
	fields = OrderedDict([


		("iWorkaroundConstant", "uint"),

	])


class CBLight(EPyCStruct):
	fields = OrderedDict([


		("iLightOffset", "uint"),
		("iLightNum", "uint"),
		("iPrimaryLight", "uint"),
		("iGIDiffuseFlags", "uint"),
		("bLightSortByType", "bbool"),
		("fSHSSAOEffect", "float"),
		("fSSAOEffectGI", "float"),
		("fSHDiffuseInverseScale", "float"),
		("fSHCoef", "float4[7]"),
		("fPrimaryLightMat", "float4x4"),
		("fBroadAreaShadowMat", "float4x4"),
		("bBroadAreaShadowEnable", "bbool"),
		("bGISpecularSHDiffuseBlend", "bbool"),
		("iLightInfiniteRange", "uint2"),
		("iLightPointRange", "uint2"),
		("iLightSpotRange", "uint2"),

	])


class CBImageEvaluator(EPyCStruct):
	fields = OrderedDict([


		("fCentralRegion", "float3"),

	])


class CBMhMaterialGlobal(EPyCStruct):
	fields = OrderedDict([


		("fMaterialWetBlend", "float"),
		("fMaterialWetRoughness", "float"),
		("bMaterialCustomLighting", "bbool"),
		("iMaterialCustomLightingGBufferIdMask", "uint"),
		("fMaterialHiddenSurfaceDrawIntensity", "float"),

	])


class CBMhMaterialScrIceBlendLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fDetailNormalBlend__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fUVTransformA", "float4"),
		("fUVTransformB", "float4"),
		("fTranslucency__uiUNorm", "float"),
		("fEmissiveBlendColor__uiColor", "float3"),
		("fEmissiveBlendColorBlend__uiUNorm", "float"),
		("fEmissiveBlendRimParam", "float3"),
		("fBlendBaseMapFactor__uiColor", "float4"),
		("fBlendEmissiveMapFactor__uiColor", "float3"),
		("fBlendMetalic__uiUNorm", "float"),
		("fBlendRoughness__uiUNorm", "float"),
		("fBlendDetailNormalBlend__uiUNorm", "float"),
		("fBlendSubSurfaceBlend__uiUNorm", "float"),

		("align1", "ubyte[4]"),
		("fBlendUVTransformA", "float4"),
		("fBlendUVTransformB", "float4"),
		("fBlendDir__uiDirection", "float3"),
		("fBlendPlaneNormal__uiUNorm", "float"),
		("fBlendOp", "float3"),
		("bUseUVSecondaryMtA", "bbool"),
		("bUseUVSecondaryMtB", "bbool"),
		("bUseUVSecondaryMtBM", "bbool"),
		("fFurNormalBlend__uiUNorm", "float"),
		("fFurHeight__uiUNorm", "float"),
		("fFurMapBlend__uiUNorm", "float"),
		("fFurEdgeBlend__uiUNorm", "float"),
		("fFurTile", "float"),

		("align2", "ubyte[4]"),
		("fWetBlendDir__uiDirection", "float3"),
		("fWetBlendPlaneNormal__uiUNorm", "float"),
		("fWetBlendOp", "float3"),
		("bSpecialBlend", "bbool"),
		("bWetNormalBlend", "bbool"),
		("fWetNormalBlendRange__uiUNorm", "float2"),
		("fIceVPushScale", "float"),
		("fIceLocalVPushScale", "float"),
		("bUseNormalDisplacement", "bbool"),

		("align3", "ubyte[8]"),
		("fIceVPushDir__uiDirection", "float3"),

		("align4", "ubyte[4]"),
		("fIceLocalVPushDir__uiDirection", "float3"),

		("align5", "ubyte[4]"),
		("fIcePushOp", "float3"),

		("align6", "ubyte[4]"),
		("fUVTransformC", "float4"),
		("fIceDisplacementUVSize", "float2"),
		("bUsePositionUV", "bbool"),

		("align7", "ubyte[4]"),
		("fAlbedoBlendMapGFactor__uiColor", "float3"),
		("fIceFresnelFactor__uiUNorm", "float"),
		("fIceColorBlend__uiUNorm", "float"),
		("bUseUVSecondaryMtIce", "bbool"),

	])


class CBMhMaterialFurLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fDetailNormalBlend__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fUVTransformA", "float4"),
		("fUVTransformB", "float4"),
		("fTranslucency__uiUNorm", "float"),
		("fEmissiveBlendColor__uiColor", "float3"),
		("fEmissiveBlendColorBlend__uiUNorm", "float"),
		("fEmissiveBlendRimParam", "float3"),
		("fFurHeight__uiUNorm", "float"),
		("fFurMapBlend__uiUNorm", "float"),
		("fFurEdgeBlend__uiUNorm", "float"),
		("fFurTile", "float"),

	])


class CBMhMaterialNPCLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fTranslucency__uiUNorm", "float"),
		("bBaseColorEmissive", "bbool"),
		("bBackFaceNormalFilp", "bbool"),
		("fAnimEmitMin", "float"),
		("fAnimEmitSpeed", "float"),
		("bUseCMM", "bbool"),

		("align0", "ubyte[8]"),
		("fAddColorA__uiColor", "float4"),
		("fAddColorB__uiColor", "float4"),
		("fAddColorC__uiColor", "float4"),
		("fAddColorD__uiColor", "float4"),
		("fFurParam__uiUNorm", "float4"),
		("fFurTile", "float"),

		("align1", "ubyte[12]"),
		("fSnowControl", "float4"),
		("fMaterialSnowBlendA", "float"),
		("fMaterialSnowBlendB", "float"),
		("fSnowTile", "float"),

		("align2", "ubyte[4]"),
		("fSnowColor__uiColor", "float3"),

		("align3", "ubyte[4]"),
		("fSnowMatControl__uiUNorm", "float4"),
		("fSnowUVOffset__uiUNorm", "float2"),
		("fFilmThickness__uiUNorm", "float"),
		("fFilmBlend__uiUNorm", "float"),
		("fFilmIOR__uiUNorm", "float"),
		("fRefractBlend__uiUNorm", "float"),
		("fRefraction__uiSNorm", "float"),
		("fPanoramaTile", "float"),
		("fEmissiveBlendColor__uiColor", "float3"),
		("fEmissiveBlendColorBlend__uiUNorm", "float"),
		("fEmissiveBlendRimParam", "float3"),
		("fDetailNormalBlend__uiUNorm", "float"),
		("fUVTransformDetailNormal", "float4"),

	])


class CBTexturePosScaleFactor(EPyCStruct):
	fields = OrderedDict([


		("drawStage", "float4"),
		("sceneFFTStage", "float4"),
		("kernelFFTStage", "float4"),

	])


class CBNewDOFFilter(EPyCStruct):
	fields = OrderedDict([


		("coc_bias", "float"),
		("coc_scale", "float"),
		("pcoc", "float"),
		("quad_reduction_threshold", "float"),
		("quater_resolution_threshold", "float"),
		("near_blur_scaler", "float"),
		("depth_adjuist_factor", "float"),
		("bokeh_intensity_threshold", "float"),
		("bokeh_shape_factor", "float"),
		("dof_single_pixel_radius", "float"),
		("dof_aspect", "float"),
		("far_ignore", "bbool"),
		("near_ignore", "bbool"),
		("far_coef", "float"),
		("near_coef", "float"),
		("fVignettingOffset", "float"),
		("fVignettingPow", "float"),
		("bVignetting", "bbool"),
		("fVignettingEllipticity", "float"),

		("align0", "ubyte[4]"),
		("fVignettingColor", "float3"),

	])


class CBMhSkyLpPS(EPyCStruct):
	fields = OrderedDict([


		("fSkyGlobalIntensity", "float3"),

		("align0", "ubyte[4]"),
		("fSkySunMapFactor", "float4"),
		("fSkyStarrySkyMapFactor", "float4"),
		("fSkySunUVOffset", "float2"),
		("fSkyGlobalCloudSpeed", "float2"),
		("fSkyWaterReflectionFactor", "float3"),
		("fSkyBlend", "float"),
		("bSkyIsRenderingWater", "bbool"),
		("bSkyFog", "bbool"),

		("align1", "ubyte[8]"),
		("fSkyBaseMapFactor", "float4"),
		("fSkyCloudMapFactor0", "float4"),
		("fSkyCloudMapFactor1", "float4"),
		("fSkyCloudMapFactor2", "float4"),
		("fSkyCloudMapFactor3", "float4"),
		("fSkyCloudSpeed0", "float2"),
		("fSkyCloudSpeed1", "float2"),
		("fSkyCloudSpeed2", "float2"),
		("fSkyCloudSpeed3", "float2"),
		("fSkyBlendBaseMapFactor", "float4"),
		("fSkyBlendCloudMapFactor0", "float4"),
		("fSkyBlendCloudMapFactor1", "float4"),
		("fSkyBlendCloudMapFactor2", "float4"),
		("fSkyBlendCloudMapFactor3", "float4"),
		("fSkyBlendCloudSpeed0", "float2"),
		("fSkyBlendCloudSpeed1", "float2"),
		("fSkyBlendCloudSpeed2", "float2"),
		("fSkyBlendCloudSpeed3", "float2"),
		("iSkyAddress", "uint2"),

	])


class CBMhMaterialEM024Local__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fTranslucency__uiUNorm", "float"),
		("bBaseColorEmissive", "bbool"),
		("fPaintUVTile", "float2"),
		("fAddNormalBlend__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fAddNormalMaskA__uiSNorm", "float4"),
		("fAddNormalMaskB__uiSNorm", "float4"),
		("fAddNormalMaskC__uiUNorm", "float"),
		("fAddNormalMaskD__uiUNorm", "float"),
		("bBackFaceShading", "bbool"),
		("bBackFaceNormalFilp", "bbool"),
		("fKizuColor__uiColor", "float3"),

		("align1", "ubyte[4]"),
		("fKizuUVOffset__uiUNorm", "float2"),
		("fKizuMultiply", "float"),
		("bLegendary", "bbool"),
		("fLegendColor__uiColor", "float4"),
		("fLegendMetalMask__uiUNorm", "float2"),
		("fLegendRoughness", "float"),

		("align2", "ubyte[4]"),
		("fLegendFilm__uiUNorm", "float3"),
		("fLegendSSSMask__uiUNorm", "float"),
		("fLegendHSV__uiSNorm", "float3"),
		("fLegendFilmIOR__uiUNorm", "float"),
		("fPartsMaskA__uiUNorm", "float"),
		("fPartsMaskB__uiUNorm", "float"),
		("fPartsMaskC__uiUNorm", "float"),
		("fPartsMaskD__uiUNorm", "float"),
		("fPartsMaskX__uiUNorm", "float"),
		("fPartsMaskY__uiUNorm", "float"),
		("fPartsMaskZ__uiUNorm", "float"),
		("fPartsMaskW__uiUNorm", "float"),
		("bUseOffset", "bbool"),
		("fOffsetScale", "float"),
		("bTranslucentOffset", "bbool"),
		("bAntiSSSEmit", "bbool"),
		("fFlowDirDir__uiDirection", "float3"),

		("align3", "ubyte[4]"),
		("fFlowControl__uiUNorm", "float4"),
		("fFlowTile", "float"),

		("align4", "ubyte[12]"),
		("fFlowColor__uiColor", "float4"),
		("fFlowMatControl__uiUNorm", "float4"),
		("fMaskBlend__uiUNorm", "float4"),
		("fMaskBlend_A__uiUNorm", "float2"),
		("fMaskBlend_B__uiUNorm", "float2"),
		("fFilmThickness__uiUNorm", "float"),
		("fFilmBlend__uiUNorm", "float"),
		("fFilmIOR__uiUNorm", "float"),
		("fRefraction__uiUNorm", "float"),
		("fRefractionBlend__uiUNorm", "float"),
		("fAnimEmitMin", "float"),
		("fAnimEmitSpeed", "float"),
		("bUseWaveEmit", "bbool"),
		("fAnimEmitWave", "float"),
		("fRimAlphaPower__uiSNorm", "float"),
		("fRimTranslucency__uiUNorm", "float"),
		("fRimNormal__uiUNorm", "float"),
		("fSnowUVTile", "float"),

		("align5", "ubyte[12]"),
		("fSnowBlendColor__uiColor", "float4"),
		("fSnowMatControl__uiUNorm", "float4"),
		("fMaterialSnowBlendB", "float"),

		("align6", "ubyte[12]"),
		("fSnowControl", "float4"),

	])


class CBMhMaterialEM063Local__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fTranslucency__uiUNorm", "float"),
		("bBaseColorEmissive", "bbool"),
		("fPaintUVTile", "float2"),
		("fAddNormalBlend__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fAddNormalMaskA__uiSNorm", "float4"),
		("fAddNormalMaskB__uiSNorm", "float4"),
		("fAddNormalMaskC__uiUNorm", "float"),
		("fAddNormalMaskD__uiUNorm", "float"),
		("bBackFaceShading", "bbool"),
		("bBackFaceNormalFilp", "bbool"),
		("fKizuColor__uiColor", "float3"),

		("align1", "ubyte[4]"),
		("fKizuUVOffset__uiUNorm", "float2"),
		("fKizuMultiply", "float"),
		("bLegendary", "bbool"),
		("fLegendColor__uiColor", "float4"),
		("fLegendMetalMask__uiUNorm", "float2"),
		("fLegendRoughness", "float"),

		("align2", "ubyte[4]"),
		("fLegendFilm__uiUNorm", "float3"),
		("fLegendSSSMask__uiUNorm", "float"),
		("fLegendHSV__uiSNorm", "float3"),
		("fLegendFilmIOR__uiUNorm", "float"),
		("fPartsMaskA__uiUNorm", "float"),
		("fPartsMaskB__uiUNorm", "float"),
		("fPartsMaskC__uiUNorm", "float"),
		("fPartsMaskD__uiUNorm", "float"),
		("fPartsMaskX__uiUNorm", "float"),
		("fPartsMaskY__uiUNorm", "float"),
		("fPartsMaskZ__uiUNorm", "float"),
		("fPartsMaskW__uiUNorm", "float"),
		("bUseOffset", "bbool"),
		("fOffsetScale", "float"),
		("bTranslucentOffset", "bbool"),
		("bAntiSSSEmit", "bbool"),
		("fFlowDirDir__uiDirection", "float3"),

		("align3", "ubyte[4]"),
		("fFlowControl__uiUNorm", "float4"),
		("fFlowTile", "float"),

		("align4", "ubyte[12]"),
		("fFlowColor__uiColor", "float4"),
		("fFlowMatControl__uiUNorm", "float4"),
		("fFilmThickness__uiUNorm", "float"),
		("fFilmBlend__uiUNorm", "float"),
		("fFilmIOR__uiUNorm", "float"),
		("fRefraction__uiUNorm", "float"),
		("fRefractionBlend__uiUNorm", "float"),
		("fAlbedoBlend__uiUNorm", "float"),
		("bPartsAlpha", "bbool"),

		("align5", "ubyte[4]"),
		("fBlendBaseMapFactor__uiColor", "float4"),
		("fBlendMatFactor", "float4"),
		("fMaskSpeed", "float"),
		("fMaskWave", "float"),
		("fMaskDistortion", "float"),
		("fAnimEmitMin", "float"),
		("fAnimEmitSpeed", "float"),
		("bUseWaveEmit", "bbool"),
		("fAnimEmitWave", "float"),
		("fRimAlphaPower__uiSNorm", "float"),
		("fRimTranslucency__uiUNorm", "float"),
		("fRimNormal__uiUNorm", "float"),
		("fSnowUVTile", "float"),

		("align6", "ubyte[4]"),
		("fSnowBlendColor__uiColor", "float4"),
		("fSnowMatControl__uiUNorm", "float4"),
		("fMaterialSnowBlendB", "float"),

		("align7", "ubyte[12]"),
		("fSnowControl", "float4"),

	])


class CBMhMaterialEM011Local__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fTranslucency__uiUNorm", "float"),
		("bBaseColorEmissive", "bbool"),
		("fPaintUVTile", "float2"),
		("fAddNormalBlend__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fAddNormalMaskA__uiSNorm", "float4"),
		("fAddNormalMaskB__uiSNorm", "float4"),
		("fAddNormalMaskC__uiUNorm", "float"),
		("fAddNormalMaskD__uiUNorm", "float"),
		("bBackFaceShading", "bbool"),
		("bBackFaceNormalFilp", "bbool"),
		("fKizuColor__uiColor", "float3"),

		("align1", "ubyte[4]"),
		("fKizuUVOffset__uiUNorm", "float2"),
		("fKizuMultiply", "float"),
		("bLegendary", "bbool"),
		("fLegendColor__uiColor", "float4"),
		("fLegendMetalMask__uiUNorm", "float2"),
		("fLegendRoughness", "float"),

		("align2", "ubyte[4]"),
		("fLegendFilm__uiUNorm", "float3"),
		("fLegendSSSMask__uiUNorm", "float"),
		("fLegendHSV__uiSNorm", "float3"),
		("fLegendFilmIOR__uiUNorm", "float"),
		("fPartsMaskA__uiUNorm", "float"),
		("fPartsMaskB__uiUNorm", "float"),
		("fPartsMaskC__uiUNorm", "float"),
		("fPartsMaskD__uiUNorm", "float"),
		("fPartsMaskX__uiUNorm", "float"),
		("fPartsMaskY__uiUNorm", "float"),
		("fPartsMaskZ__uiUNorm", "float"),
		("fPartsMaskW__uiUNorm", "float"),
		("bUseOffset", "bbool"),
		("fOffsetScale", "float"),
		("bTranslucentOffset", "bbool"),
		("bAntiSSSEmit", "bbool"),
		("fFlowDirDir__uiDirection", "float3"),

		("align3", "ubyte[4]"),
		("fFlowControl__uiUNorm", "float4"),
		("fFlowTile", "float"),

		("align4", "ubyte[12]"),
		("fFlowColor__uiColor", "float4"),
		("fFlowMatControl__uiUNorm", "float4"),
		("fDisplaceControl", "float4"),
		("fDispSpeed", "float"),
		("fFilmThickness__uiUNorm", "float"),
		("fFilmBlend__uiUNorm", "float"),
		("fFilmIOR__uiUNorm", "float"),
		("fRefraction__uiUNorm", "float"),
		("fRefractionBlend__uiUNorm", "float"),
		("fAnimEmitMin", "float"),
		("fAnimEmitSpeed", "float"),
		("bUseWaveEmit", "bbool"),
		("fAnimEmitWave", "float"),

		("align5", "ubyte[8]"),
		("fFurParam__uiUNorm", "float4"),
		("fFurTile", "float"),
		("fRimAlphaPower__uiSNorm", "float"),
		("fRimTranslucency__uiUNorm", "float"),
		("fRimNormal__uiUNorm", "float"),
		("fSnowUVTile", "float"),

		("align6", "ubyte[12]"),
		("fSnowBlendColor__uiColor", "float4"),
		("fSnowMatControl__uiUNorm", "float4"),
		("fMaterialSnowBlendB", "float"),

		("align7", "ubyte[12]"),
		("fSnowControl", "float4"),

	])


class CBCSClear(EPyCStruct):
	fields = OrderedDict([


		("iSize", "uint"),

	])


class CBStarrySky(EPyCStruct):
	fields = OrderedDict([


		("fRotMatrix", "float4x4"),
		("fSize", "float2"),
		("fFactor", "float"),
		("fIntensity", "float"),
		("fScintillation", "float"),

	])


class CBROPTest(EPyCStruct):
	fields = OrderedDict([


		("bAlphaTestEnable", "bbool"),
		("fAlphaRef", "float"),
		("fDepthBias", "float"),
		("fSlopedDepthBias", "float"),
		("fMaxDepthBias", "float"),
		("fGlobalTransparency", "float"),
		("bAlphaDither", "bbool"),

		("align0", "ubyte[4]"),
		("CapturePixelOffset", "float2"),
		("CaptureScale", "float"),

	])


class CBMhMaterialSimpleLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fTranslucency__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fUVTransformA", "float4"),

	])


class CBRadialBlurFilter(EPyCStruct):
	fields = OrderedDict([


		("fRadialBlurCenter", "float2"),
		("fRadialBlurStart", "float"),
		("fRadialBlurWidth", "float"),
		("fRadialBlurColor", "float4"),
		("fRadialBlurThrethold", "float"),
		("fRadialBlurWidthScale", "float"),
		("fRadialBlurWidthOffset", "float"),
		("fRadialBlurSampleCount", "uint"),
		("fRadialBlurChromaticAberration", "float3"),
		("fRadialBlurBlurScreenAlpha", "float"),
		("fRadialBlurBlurCurve", "float4[64]"),

	])


class CBMhMaterialNPCSkinLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fTranslucency__uiUNorm", "float"),
		("bBaseColorEmissive", "bbool"),
		("bBackFaceNormalFilp", "bbool"),
		("fAnimEmitMin", "float"),
		("fAnimEmitSpeed", "float"),
		("fAddColorUV__uiUNorm", "float2"),
		("bUseCMM", "bbool"),
		("fAddColorA__uiColor", "float4"),
		("fAddColorB__uiColor", "float4"),
		("fDetailNormalBlend__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fUVTransformDetailNormal", "float4"),

	])


class CBMhSky2GBuffer(EPyCStruct):
	fields = OrderedDict([


		("iSkyGBufferId", "uint"),

	])


class CBHazeFilter(EPyCStruct):
	fields = OrderedDict([


		("iHazeTech", "uint"),
		("fHazeFilterStart", "float"),
		("fHazeFilterInverseRange", "float"),
		("fHazeFilterHeightStart", "float"),
		("fHazeFilterHeightInverseRange", "float"),

		("align0", "ubyte[12]"),
		("fHazeFilterUVWOffset", "float4"),
		("fHazeFilterScale", "float"),

	])


class CBDOFFilter(EPyCStruct):
	fields = OrderedDict([


		("fDOFPoissonOffsets", "float2[8]"),
		("fDOFPixelSizeLow", "float2"),
		("fDOFPixelSizeHigh", "float2"),

		("align0", "ubyte[8]"),
		("fDOFGradateColor", "float3"),
		("fDOFFocus", "float"),
		("fDOFNear", "float"),
		("fDOFFar", "float"),
		("fDOFNearLimit", "float"),
		("fDOFFarLimit", "float"),
		("fDOFCoCScale", "float"),
		("fDOFCoCBias", "float"),
		("fDOFRadiusScale", "float"),
		("fDOFCorrectParamNear", "float"),
		("fDOFCorrectParamFar", "float"),

		("align1", "ubyte[12]"),
		("fDOFVelocityFactor", "float4"),

	])


class CBGodRaysFilter(EPyCStruct):
	fields = OrderedDict([


		("fGodRaysOrigin", "float3"),
		("fGodRaysMaskWeight", "float"),
		("fGodRaysWorldOrigin", "float3"),
		("fGodRaysMaskRadius", "float"),
		("fGodRaysDecay", "float"),
		("fGodRaysThreshold", "float"),
		("fGodRaysSamples", "float"),
		("fGodRaysGamma", "float"),
		("fGodRaysColor", "float4"),
		("fGodRaysShadowThreshold", "float"),
		("fGodRaysBlurWidthScale", "float"),
		("fGodRaysBlurWidthOffset", "float"),

	])


class CBMhMaterialIvyFloor(EPyCStruct):
	fields = OrderedDict([


		("iIvyFloorWindIndex", "int"),
		("iIvyFloorWindIndexPF", "int"),
		("iIvyFloorId", "uint2"),
		("fIvyFloorWindScale", "float"),

	])


class CBVRFilter(EPyCStruct):
	fields = OrderedDict([


		("fDimensions", "float4"),
		("fFilterRegion", "float4"),
		("fFilterMipLevel", "float"),
		("vertical", "bbool"),

	])


class CBFilter(EPyCStruct):
	fields = OrderedDict([


		("fFilterRegion", "float4"),
		("fFilterMipLevel", "float"),

	])


class CBMhMaterialStdBlendNoFurLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fDetailNormalBlend__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fUVTransformA", "float4"),
		("fUVTransformB", "float4"),
		("fTranslucency__uiUNorm", "float"),
		("fEmissiveBlendColor__uiColor", "float3"),
		("fEmissiveBlendColorBlend__uiUNorm", "float"),
		("fEmissiveBlendRimParam", "float3"),
		("fBlendBaseMapFactor__uiColor", "float4"),
		("fBlendEmissiveMapFactor__uiColor", "float3"),
		("fBlendMetalic__uiUNorm", "float"),
		("fBlendRoughness__uiUNorm", "float"),
		("fBlendDetailNormalBlend__uiUNorm", "float"),
		("fBlendSubSurfaceBlend__uiUNorm", "float"),

		("align1", "ubyte[4]"),
		("fBlendUVTransformA", "float4"),
		("fBlendUVTransformB", "float4"),
		("fBlendDir__uiDirection", "float3"),
		("fBlendPlaneNormal__uiUNorm", "float"),
		("fBlendOp", "float3"),
		("bUseUVSecondaryMtA", "bbool"),
		("bUseUVSecondaryMtB", "bbool"),
		("bUseUVSecondaryMtBM", "bbool"),

		("align2", "ubyte[8]"),
		("fWetBlendDir__uiDirection", "float3"),
		("fWetBlendPlaneNormal__uiUNorm", "float"),
		("fWetBlendOp", "float3"),
		("bSpecialBlend", "bbool"),
		("bWetNormalBlend", "bbool"),
		("fWetNormalBlendRange__uiUNorm", "float2"),

	])


class CBMhMaterialPLEyeLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fTranslucency__uiUNorm", "float"),
		("bBaseColorEmissive", "bbool"),
		("bBackFaceNormalFilp", "bbool"),
		("fAnimEmitMin", "float"),
		("fAnimEmitSpeed", "float"),
		("fParallaxFactor__uiUNorm", "float"),
		("fDetailNormalBlend__uiUNorm", "float"),

		("align0", "ubyte[4]"),
		("fUVTransformDetailNormal", "float4"),

	])


class CBMhMaterialEM105Local__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fTranslucency__uiUNorm", "float"),
		("bBaseColorEmissive", "bbool"),
		("fPaintUVTile", "float2"),
		("fAddNormalBlend__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fAddNormalMaskA__uiSNorm", "float4"),
		("fAddNormalMaskB__uiSNorm", "float4"),
		("fAddNormalMaskC__uiUNorm", "float"),
		("fAddNormalMaskD__uiUNorm", "float"),
		("bBackFaceShading", "bbool"),
		("bBackFaceNormalFilp", "bbool"),
		("fKizuColor__uiColor", "float3"),

		("align1", "ubyte[4]"),
		("fKizuUVOffset__uiUNorm", "float2"),
		("fKizuMultiply", "float"),
		("bLegendary", "bbool"),
		("fLegendColor__uiColor", "float4"),
		("fLegendMetalMask__uiUNorm", "float2"),
		("fLegendRoughness", "float"),

		("align2", "ubyte[4]"),
		("fLegendFilm__uiUNorm", "float3"),
		("fLegendSSSMask__uiUNorm", "float"),
		("fLegendHSV__uiSNorm", "float3"),
		("fLegendFilmIOR__uiUNorm", "float"),
		("fPartsMaskA__uiUNorm", "float"),
		("fPartsMaskB__uiUNorm", "float"),
		("fPartsMaskC__uiUNorm", "float"),
		("fPartsMaskD__uiUNorm", "float"),
		("fPartsMaskX__uiUNorm", "float"),
		("fPartsMaskY__uiUNorm", "float"),
		("fPartsMaskZ__uiUNorm", "float"),
		("fPartsMaskW__uiUNorm", "float"),
		("bUseOffset", "bbool"),
		("fOffsetScale", "float"),
		("bTranslucentOffset", "bbool"),
		("bAntiSSSEmit", "bbool"),
		("fFlowDirDir__uiDirection", "float3"),

		("align3", "ubyte[4]"),
		("fFlowControl__uiUNorm", "float4"),
		("fFlowTile", "float"),

		("align4", "ubyte[12]"),
		("fFlowColor__uiColor", "float4"),
		("fFlowMatControl__uiUNorm", "float4"),
		("fMaskBlend__uiUNorm", "float4"),
		("fMaskBlend_A__uiUNorm", "float2"),
		("fMaskBlend_B__uiUNorm", "float2"),
		("fFilmThickness__uiUNorm", "float"),
		("fFilmBlend__uiUNorm", "float"),
		("fFilmIOR__uiUNorm", "float"),
		("fRefraction__uiUNorm", "float"),
		("fRefractionBlend__uiUNorm", "float"),
		("fVPushScale", "float"),
		("fVPushWave", "float"),
		("fVPushSpeed", "float"),
		("fVpivot", "float3"),
		("fInnerOffsetScale", "float"),
		("fVolumeBlend__uiSNorm", "float"),

		("align5", "ubyte[12]"),
		("fDetailEmissiveControl", "float4"),
		("fFinWave", "float"),
		("fFinSpeed", "float"),

		("align6", "ubyte[8]"),
		("fFinColor__uiColor", "float3"),
		("fAnimEmitMin", "float"),
		("fAnimEmitSpeed", "float"),
		("bUseWaveEmit", "bbool"),
		("fAnimEmitWave", "float"),
		("fRimAlphaPower__uiSNorm", "float"),
		("fRimTranslucency__uiUNorm", "float"),
		("fRimNormal__uiUNorm", "float"),
		("fSnowUVTile", "float"),

		("align7", "ubyte[4]"),
		("fSnowBlendColor__uiColor", "float4"),
		("fSnowMatControl__uiUNorm", "float4"),
		("fMaterialSnowBlendB", "float"),

		("align8", "ubyte[12]"),
		("fSnowControl", "float4"),

	])


class CBMhSkyGBuffer(EPyCStruct):
	fields = OrderedDict([


		("iSkyGBufferId", "uint"),

	])


class CB_CombinedFilter_ColorCorrect(EPyCStruct):
	fields = OrderedDict([


		("fDepthNear", "float"),
		("fDepthFar", "float"),
		("bHdrExtrapolation", "bbool"),
		("fHdrIntensityRangeInv", "float"),

	])


class CBLightShaft(EPyCStruct):
	fields = OrderedDict([


		("fModelMat", "float4x4"),
		("fInvModelMat", "float4x4"),
		("fExtinctionCoef", "float"),
		("fRayleighCoef", "float"),
		("fMieCoef", "float"),
		("fZAttnStart", "float"),
		("fZAttnEnd", "float"),
		("iFlags", "uint"),
		("fTransparency", "float"),
		("fReductionScale", "float"),
		("fMiePhaseK", "float3"),

	])


class CBWaterCustomLight(EPyCStruct):
	fields = OrderedDict([


		("bShadowCascadeBias", "bbool"),

	])


class CBMhMaterialSpeedTreeStdSnowLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fDetailNormalBlend__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fUVTransformA", "float4"),
		("fUVTransformB", "float4"),
		("fBaseMapModulation__uiUNorm", "float4"),
		("fTranslucency__uiUNorm", "float"),
		("bLightProbeEmissive", "bbool"),

		("align1", "ubyte[8]"),
		("fEmissiveBlendColor__uiColor", "float3"),
		("fEmissiveBlendColorBlend__uiUNorm", "float"),
		("fEmissiveBlendRimParam", "float3"),
		("bSpecialBlend", "bbool"),
		("fRoughnessThreshold__uiUNorm", "float"),
		("fRoughnessFillValue__uiUNorm", "float"),
		("bWetNormalBlend", "bbool"),

		("align2", "ubyte[4]"),
		("fWetNormalBlendRange__uiUNorm", "float2"),
		("fSnowAlphaRef__uiUNorm", "float"),

		("align3", "ubyte[4]"),
		("fSnowBaseMapFactor__uiColor", "float4"),
		("fSnowEmissiveMapFactor__uiColor", "float3"),
		("fSnowMetalic__uiUNorm", "float"),
		("fSnowRoughness__uiUNorm", "float"),
		("fSnowDetailNormalBlend__uiUNorm", "float"),
		("fSnowSubSurfaceBlend__uiUNorm", "float"),

		("align4", "ubyte[4]"),
		("fSnowUVTransformA", "float4"),
		("fSnowUVTransformB", "float4"),
		("fSnowDir__uiDirection", "float3"),
		("fSnowPlaneNormal__uiUNorm", "float"),
		("fSnowOp", "float3"),
		("bUseUVSecondarySnowMt", "bbool"),
		("bUseUVSecondarySnowMtBM", "bbool"),

	])


class CBSparkleParam(EPyCStruct):
	fields = OrderedDict([


		("fSparkleLightDir", "float4"),
		("fSparkleSize", "float"),

	])


class CBWaterCustom(EPyCStruct):
	fields = OrderedDict([


		("fWaterCustomBaseMapFactor", "float4"),
		("fWaterCustomBlendBaseMapFactor", "float4"),
		("fWaterCustomEmissiveMapFactor", "float3"),

		("align0", "ubyte[4]"),
		("fWaterCustomCubeMapFactor", "float3"),

		("align1", "ubyte[4]"),
		("fWaterCustomBlendCubeMapFactor", "float3"),
		("fWaterCustomMetallic", "float"),
		("fWaterCustomRoughness", "float"),
		("fWaterCustomSpecular", "float"),

		("align2", "ubyte[8]"),
		("fWaterCustomUVTransformA", "float4"),
		("fWaterCustomUVTransformB", "float4"),
		("fWaterCustomUVOffsetSpeedFactor", "float2"),
		("fWaterCustomUVOffsetSpeedFactorDetail", "float2"),
		("fWaterCustomDetailNormalBlend", "float"),
		("fWaterCustomProjectionNormalBlend", "float"),
		("fWaterCustomProjectionNormalTileSize", "float2"),
		("fWaterCustomRefraction", "float"),
		("fWaterCustomRefractionFactor", "float3"),
		("fWaterCustomBlendRefractionFactor", "float3"),
		("fWaterCustomRefractionPow", "float"),
		("bWaterCustomRefractionScreenFade", "bbool"),
		("fWaterCustomRefractionTangentNormalBlend", "float"),
		("fWaterCustomVolumeBlend", "float"),
		("fWaterCustomFlowStrength", "float"),
		("fWaterCustomFlowSpeed", "float"),
		("fWaterCustomFresnelBias", "float"),
		("fWaterCustomShadowAttn", "float"),
		("fWaterCustomNormalXZAttn", "float"),
		("iWaterCustomEnvMapAttn", "uint"),
		("fWaterCustomShadowDistortion", "float"),

	])


class CBMhMaterialEM036Local__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fTranslucency__uiUNorm", "float"),
		("bBaseColorEmissive", "bbool"),
		("fPaintUVTile", "float2"),
		("fAddNormalBlend__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fAddNormalMaskA__uiSNorm", "float4"),
		("fAddNormalMaskB__uiSNorm", "float4"),
		("fAddNormalMaskC__uiUNorm", "float"),
		("fAddNormalMaskD__uiUNorm", "float"),
		("bBackFaceShading", "bbool"),
		("bBackFaceNormalFilp", "bbool"),
		("fKizuColor__uiColor", "float3"),

		("align1", "ubyte[4]"),
		("fKizuUVOffset__uiUNorm", "float2"),
		("fKizuMultiply", "float"),
		("bLegendary", "bbool"),
		("fLegendColor__uiColor", "float4"),
		("fLegendMetalMask__uiUNorm", "float2"),
		("fLegendRoughness", "float"),

		("align2", "ubyte[4]"),
		("fLegendFilm__uiUNorm", "float3"),
		("fLegendSSSMask__uiUNorm", "float"),
		("fLegendHSV__uiSNorm", "float3"),
		("fLegendFilmIOR__uiUNorm", "float"),
		("fPartsMaskA__uiUNorm", "float"),
		("fPartsMaskB__uiUNorm", "float"),
		("fPartsMaskC__uiUNorm", "float"),
		("fPartsMaskD__uiUNorm", "float"),
		("fPartsMaskX__uiUNorm", "float"),
		("fPartsMaskY__uiUNorm", "float"),
		("fPartsMaskZ__uiUNorm", "float"),
		("fPartsMaskW__uiUNorm", "float"),
		("bUseOffset", "bbool"),
		("fOffsetScale", "float"),
		("bTranslucentOffset", "bbool"),
		("bAntiSSSEmit", "bbool"),
		("fFlowDirDir__uiDirection", "float3"),

		("align3", "ubyte[4]"),
		("fFlowControl__uiUNorm", "float4"),
		("fFlowTile", "float"),

		("align4", "ubyte[12]"),
		("fFlowColor__uiColor", "float4"),
		("fFlowMatControl__uiUNorm", "float4"),
		("fFilmThickness__uiUNorm", "float"),
		("fFilmBlend__uiUNorm", "float"),
		("fFilmIOR__uiUNorm", "float"),
		("fRefraction__uiUNorm", "float"),
		("fRefractionBlend__uiUNorm", "float"),

		("align5", "ubyte[12]"),
		("fEmitControl__uiUNorm", "float4"),
		("fAnimEmitMin", "float"),
		("fAnimEmitSpeed", "float"),
		("bUseWaveEmit", "bbool"),
		("fAnimEmitWave", "float"),
		("fRimAlphaPower__uiSNorm", "float"),
		("fRimTranslucency__uiUNorm", "float"),
		("fRimNormal__uiUNorm", "float"),
		("fSnowUVTile", "float"),
		("fSnowBlendColor__uiColor", "float4"),
		("fSnowMatControl__uiUNorm", "float4"),
		("fMaterialSnowBlendB", "float"),

		("align6", "ubyte[12]"),
		("fSnowControl", "float4"),

	])


class CBUpdateBufferFromMeshConditions(EPyCStruct):
	fields = OrderedDict([


		("fConditionsBlendAxis", "float3"),
		("fConditionsBlendHeightLimit", "float"),
		("fConditionsBlendHeightLimitOffset", "float"),
		("fConditionsBlendAngleLimit", "float"),
		("fConditionsBlendAngleScale", "float"),
		("fConditionsBlendAdd", "float"),

	])


class CBBloom(EPyCStruct):
	fields = OrderedDict([


		("fBloomThreshold", "float"),
		("fBloomRenormalize", "float"),
		("bGamutSrgb", "bbool"),

		("align0", "ubyte[4]"),
		("fDirtColor", "float4"),

	])


class CBMhMaterialBurnLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fTranslucency__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fUVTransformA", "float4"),
		("fBurnControl__uiUNorm", "float3"),

		("align1", "ubyte[4]"),
		("fBurnColor__uiColor", "float3"),

		("align2", "ubyte[4]"),
		("fSnowControl", "float4"),
		("fMaterialSnowBlendA", "float"),
		("fMaterialSnowBlendB", "float"),
		("fSnowTile", "float"),

		("align3", "ubyte[4]"),
		("fSnowColor__uiColor", "float3"),

		("align4", "ubyte[4]"),
		("fSnowMatControl__uiUNorm", "float4"),
		("fSnowUVOffset__uiUNorm", "float2"),

	])


class CBPrimCopyState(EPyCStruct):
	fields = OrderedDict([


		("fNormalSlope", "float"),

	])


class CBToneMapping(EPyCStruct):
	fields = OrderedDict([


		("iToneMapType", "uint"),
		("bLuminanceVersion", "bbool"),
		("fShouldStr", "float"),
		("fLinearStr", "float"),
		("fIntermediate", "float"),
		("fS1", "float"),
		("fS2", "float"),
		("fS3", "float"),
		("fS4", "float"),
		("iLUTSize", "uint"),
		("bIsLinearToPQ", "bbool"),
		("bIsPQToLinear", "bbool"),
		("bEnableColorGrading", "bbool"),

	])


class CBMhMaterialVfxVATDistLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float3"),

		("align0", "ubyte[4]"),
		("fDistortionFactor__uiColor", "float3"),

		("align1", "ubyte[4]"),
		("fCubeMapFactor__uiColor", "float3"),

		("align2", "ubyte[4]"),
		("fUVTransformA", "float4"),
		("fUVTransformB", "float4"),
		("fUVTransformC", "float4"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fTranslucency__uiUNorm", "float"),
		("fSpecularFactor", "float"),
		("fOpacityFactor", "float"),
		("fVertexOpacityFactor", "float"),
		("fVolumeBlend__uiSNorm", "float"),
		("fWN_RimRate__uiUNorm", "float"),
		("fWN_RimOpacityPow", "float"),
		("fPN_RimRate__uiUNorm", "float"),
		("fPN_RimOpacityPow", "float"),
		("fRimOpacityFactor", "float"),
		("fNormalBlend__uiUNorm", "float"),
		("fRaflectionRate__uiUNorm", "float"),
		("fDistortionScale__uiUNorm", "float"),
		("fDistortionPow", "float"),
		("fFlowSpeed", "float"),
		("fFlowStrength", "float"),
		("fDispFactor", "float"),
		("fDiffuseChroma__uiUNorm", "float"),
		("fSpecularChroma__uiUNorm", "float"),
		("fInnerOffsetScale", "float"),
		("fVelocityAttn", "float"),
		("fNormalDecalBlend__uiUNorm", "float"),
		("bSceneEnvMap", "bbool"),
		("bEnableOpaque", "bbool"),
		("bVertexColor", "bbool"),

	])


class CBMhMaterialEM106Local__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fTranslucency__uiUNorm", "float"),
		("bBaseColorEmissive", "bbool"),
		("fPaintUVTile", "float2"),
		("fAddNormalBlend__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fAddNormalMaskA__uiSNorm", "float4"),
		("fAddNormalMaskB__uiSNorm", "float4"),
		("fAddNormalMaskC__uiUNorm", "float"),
		("fAddNormalMaskD__uiUNorm", "float"),
		("bBackFaceShading", "bbool"),
		("bBackFaceNormalFilp", "bbool"),
		("fKizuColor__uiColor", "float3"),

		("align1", "ubyte[4]"),
		("fKizuUVOffset__uiUNorm", "float2"),
		("fKizuMultiply", "float"),
		("bLegendary", "bbool"),
		("fLegendColor__uiColor", "float4"),
		("fLegendMetalMask__uiUNorm", "float2"),
		("fLegendRoughness", "float"),

		("align2", "ubyte[4]"),
		("fLegendFilm__uiUNorm", "float3"),
		("fLegendSSSMask__uiUNorm", "float"),
		("fLegendHSV__uiSNorm", "float3"),
		("fLegendFilmIOR__uiUNorm", "float"),
		("fPartsMaskA__uiUNorm", "float"),
		("fPartsMaskB__uiUNorm", "float"),
		("fPartsMaskC__uiUNorm", "float"),
		("fPartsMaskD__uiUNorm", "float"),
		("fPartsMaskX__uiUNorm", "float"),
		("fPartsMaskY__uiUNorm", "float"),
		("fPartsMaskZ__uiUNorm", "float"),
		("fPartsMaskW__uiUNorm", "float"),
		("bUseOffset", "bbool"),
		("fOffsetScale", "float"),
		("bTranslucentOffset", "bbool"),
		("bAntiSSSEmit", "bbool"),
		("fFlowDirDir__uiDirection", "float3"),

		("align3", "ubyte[4]"),
		("fFlowControl__uiUNorm", "float4"),
		("fFlowTile", "float"),

		("align4", "ubyte[12]"),
		("fFlowColor__uiColor", "float4"),
		("fFlowMatControl__uiUNorm", "float4"),
		("fFilmThickness__uiUNorm", "float"),
		("fFilmBlend__uiUNorm", "float"),
		("fFilmIOR__uiUNorm", "float"),
		("fRefraction__uiUNorm", "float"),
		("fRefractionBlend__uiUNorm", "float"),

		("align5", "ubyte[12]"),
		("fDetailBlend__uiUNorm", "float4"),
		("fDetailTile", "float4"),
		("fDetailA_Color__uiColor", "float4"),
		("fDetailB_Color__uiColor", "float4"),
		("fDetailC_Color__uiColor", "float4"),
		("fDetailD_Color__uiColor", "float4"),
		("fDetail_Roughness__uiUNorm", "float4"),
		("fDetail_Metal__uiUNorm", "float4"),
		("bAntiEmitSSS", "bbool"),
		("fAnimEmitMin", "float"),
		("fAnimEmitSpeed", "float"),
		("bUseWaveEmit", "bbool"),
		("fAnimEmitWave", "float"),
		("fRimAlphaPower__uiSNorm", "float"),
		("fRimTranslucency__uiUNorm", "float"),
		("fRimNormal__uiUNorm", "float"),
		("fSnowUVTile", "float"),

		("align6", "ubyte[12]"),
		("fSnowBlendColor__uiColor", "float4"),
		("fSnowMatControl__uiUNorm", "float4"),
		("fMaterialSnowBlendB", "float"),

		("align7", "ubyte[12]"),
		("fSnowControl", "float4"),

	])


class CBMhMaterialVfxFakeInnerLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fEmissiveMapFactor__uiColor", "float3"),

		("align0", "ubyte[4]"),
		("fUVTransformA", "float4"),
		("fInnerOffsetScale", "float"),
		("fRimAlphaPower__uiUNorm", "float"),
		("fVolumeBlend__uiSNorm", "float"),

		("align1", "ubyte[4]"),
		("fUVanimVector", "float2"),
		("fOpacityFactor", "float"),
		("bGBufferIdMaskEnable", "bbool"),
		("iGBufferIdMask", "uint"),
		("fNormalDecalBlend__uiUNorm", "float"),

	])


class CBComputeSkinning(EPyCStruct):
	fields = OrderedDict([


		("iSrcStride", "uint"),
		("iSrcOffset", "uint"),
		("iSrcPositionOffset", "uint"),
		("iSrcNormalOffset", "uint"),
		("iSrcWeightsOffset", "uint"),
		("iSrcJointsOffset", "uint"),
		("iDestStride", "uint"),
		("iDestOffset", "uint"),
		("iDestNormalStride", "uint"),
		("iDestNormalOffset", "uint"),
		("iVertexCount", "uint"),
		("iInstanceID", "uint"),

	])


class CBBokehComposite(EPyCStruct):
	fields = OrderedDict([


		("fBokehMipBias", "float"),
		("fBokehMipScale", "float"),
		("fBokehAlphaScale", "float"),
		("fBokehRangeScale", "float"),
		("fBokehDitherScale", "float"),
		("iBokehSampleCount", "int"),

		("align0", "ubyte[8]"),
		("fBokehTap", "float2[25]"),

	])


class CBWaterWave(EPyCStruct):
	fields = OrderedDict([


		("fWorldMat", "float4x4"),
		("fHeightMapSize", "float2"),
		("fInvHeightMapSize", "float2"),
		("fMeshCenter", "float2"),
		("fEdgesPerScreenHeight", "float"),
		("fNoiseWaveAmplitude", "float"),
		("fNoiseWaveDensity", "float"),
		("fNoiseWaveSpeed", "float"),
		("fOverlapRatio", "float2"),
		("fNoiseWaveBorderX", "float2"),
		("fNoiseWaveBorderZ", "float2"),
		("fDistanceBetweenVertices", "float2"),
		("fWaveDensity", "float"),
		("fDetailWaveDensity", "float"),
		("fMeshVerticesDistance", "float2"),
		("fMaxTexcoord", "float2"),
		("fElapsedTimeSec", "float"),
		("iDebugViewType", "int"),
		("bIsAnimating", "bbool"),

		("align0", "ubyte[4]"),
		("fWorldScale", "float3"),

		("align1", "ubyte[4]"),
		("fBoundingYMinMax", "float2"),
		("bCullingByFrustum", "bbool"),
		("fFrustumCullAcceptXZ", "float"),
		("fCircleCullDistanceSq", "float"),

	])


class CBSnowField3Geometry(EPyCStruct):
	fields = OrderedDict([


		("fWorldPositionMin", "float3"),

		("align0", "ubyte[4]"),
		("fWorldPositionMax", "float3"),
		("fShovelCornerBlendRate", "float"),
		("fSDRange", "float4[10]"),
		("iSDSubdiv", "uint"),
		("iSDSubdivLevel0", "uint"),
		("fSDSubdiv", "float2"),
		("fSDSubdivLevel0", "float2"),
		("iInnerSubdiv", "uint"),

		("align1", "ubyte[4]"),
		("fInnerSubdiv", "float2"),
		("fEdgeHeightBlendRate", "float"),
		("fEdgesPerScreenHeight", "float"),

	])


class CBDecal(EPyCStruct):
	fields = OrderedDict([


		("iDecalMode", "uint"),
		("fDecalMetallic", "float"),
		("fDecalRoughness", "float"),
		("fDecalNonMetallicFresnel", "float"),
		("fDecalLimitAngle", "float"),

	])


class CBMhMaterialBTK001Local__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fTranslucency__uiUNorm", "float"),
		("bBaseColorEmissive", "bbool"),
		("fPaintUVTile", "float2"),
		("fAddNormalBlend__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fAddNormalMaskA__uiSNorm", "float4"),
		("fAddNormalMaskB__uiSNorm", "float4"),
		("fAddNormalMaskC__uiUNorm", "float"),
		("fAddNormalMaskD__uiUNorm", "float"),
		("bBackFaceShading", "bbool"),
		("bBackFaceNormalFilp", "bbool"),
		("fKizuColor__uiColor", "float3"),

		("align1", "ubyte[4]"),
		("fKizuUVOffset__uiUNorm", "float2"),
		("fKizuMultiply", "float"),
		("bLegendary", "bbool"),
		("fLegendColor__uiColor", "float4"),
		("fLegendMetalMask__uiUNorm", "float2"),
		("fLegendRoughness", "float"),

		("align2", "ubyte[4]"),
		("fLegendFilm__uiUNorm", "float3"),
		("fLegendSSSMask__uiUNorm", "float"),
		("fLegendHSV__uiSNorm", "float3"),
		("fLegendFilmIOR__uiUNorm", "float"),
		("fPartsMaskA__uiUNorm", "float"),
		("fPartsMaskB__uiUNorm", "float"),
		("fPartsMaskC__uiUNorm", "float"),
		("fPartsMaskD__uiUNorm", "float"),
		("fPartsMaskX__uiUNorm", "float"),
		("fPartsMaskY__uiUNorm", "float"),
		("fPartsMaskZ__uiUNorm", "float"),
		("fPartsMaskW__uiUNorm", "float"),
		("bUseOffset", "bbool"),
		("fOffsetScale", "float"),
		("bTranslucentOffset", "bbool"),
		("bAntiSSSEmit", "bbool"),
		("fFlowDirDir__uiDirection", "float3"),

		("align3", "ubyte[4]"),
		("fFlowControl__uiUNorm", "float4"),
		("fFlowTile", "float"),

		("align4", "ubyte[12]"),
		("fFlowColor__uiColor", "float4"),
		("fFlowMatControl__uiUNorm", "float4"),
		("fFilmThickness__uiUNorm", "float"),
		("fFilmBlend__uiUNorm", "float"),
		("fFilmIOR__uiUNorm", "float"),
		("fRefraction__uiUNorm", "float"),
		("fRefractionBlend__uiUNorm", "float"),
		("fAlbedoBlend__uiUNorm", "float"),
		("bPartsAlpha", "bbool"),

		("align5", "ubyte[4]"),
		("fBlendBaseMapFactor__uiColor", "float4"),
		("fBlendMatFactor", "float4"),
		("fMaskSpeed", "float"),
		("fMaskWave", "float"),
		("fMaskDistortion", "float"),
		("fAnimEmitMin", "float"),
		("fAnimEmitSpeed", "float"),
		("bUseWaveEmit", "bbool"),
		("fAnimEmitWave", "float"),
		("fRimAlphaPower__uiSNorm", "float"),
		("fRimTranslucency__uiUNorm", "float"),
		("fRimNormal__uiUNorm", "float"),
		("fSnowUVTile", "float"),

		("align6", "ubyte[4]"),
		("fSnowBlendColor__uiColor", "float4"),
		("fSnowMatControl__uiUNorm", "float4"),
		("fMaterialSnowBlendB", "float"),

		("align7", "ubyte[12]"),
		("fSnowControl", "float4"),

	])


class CBCAS(EPyCStruct):
	fields = OrderedDict([


		("iConst0", "uint4"),
		("iConst1", "uint4"),

	])


class CBMhMaterialEM032Local__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fTranslucency__uiUNorm", "float"),
		("bBaseColorEmissive", "bbool"),
		("fPaintUVTile", "float2"),
		("fAddNormalBlend__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fAddNormalMaskA__uiSNorm", "float4"),
		("fAddNormalMaskB__uiSNorm", "float4"),
		("fAddNormalMaskC__uiUNorm", "float"),
		("fAddNormalMaskD__uiUNorm", "float"),
		("bBackFaceShading", "bbool"),
		("bBackFaceNormalFilp", "bbool"),
		("fKizuColor__uiColor", "float3"),

		("align1", "ubyte[4]"),
		("fKizuUVOffset__uiUNorm", "float2"),
		("fKizuMultiply", "float"),
		("bLegendary", "bbool"),
		("fLegendColor__uiColor", "float4"),
		("fLegendMetalMask__uiUNorm", "float2"),
		("fLegendRoughness", "float"),

		("align2", "ubyte[4]"),
		("fLegendFilm__uiUNorm", "float3"),
		("fLegendSSSMask__uiUNorm", "float"),
		("fLegendHSV__uiSNorm", "float3"),
		("fLegendFilmIOR__uiUNorm", "float"),
		("fPartsMaskA__uiUNorm", "float"),
		("fPartsMaskB__uiUNorm", "float"),
		("fPartsMaskC__uiUNorm", "float"),
		("fPartsMaskD__uiUNorm", "float"),
		("fPartsMaskX__uiUNorm", "float"),
		("fPartsMaskY__uiUNorm", "float"),
		("fPartsMaskZ__uiUNorm", "float"),
		("fPartsMaskW__uiUNorm", "float"),
		("bUseOffset", "bbool"),
		("fOffsetScale", "float"),
		("bTranslucentOffset", "bbool"),
		("bAntiSSSEmit", "bbool"),
		("fFlowDirDir__uiDirection", "float3"),

		("align3", "ubyte[4]"),
		("fFlowControl__uiUNorm", "float4"),
		("fFlowTile", "float"),

		("align4", "ubyte[12]"),
		("fFlowColor__uiColor", "float4"),
		("fFlowMatControl__uiUNorm", "float4"),
		("fFilmThickness__uiUNorm", "float"),
		("fFilmBlend__uiUNorm", "float"),
		("fFilmIOR__uiUNorm", "float"),
		("fRefraction__uiUNorm", "float"),
		("fRefractionBlend__uiUNorm", "float"),
		("fAnimEmitMin", "float"),
		("fAnimEmitSpeed", "float"),
		("bUseWaveEmit", "bbool"),
		("fAnimEmitWave", "float"),

		("align5", "ubyte[12]"),
		("fAnimEmitControl__uiUNorm", "float4"),
		("fRimAlphaPower__uiSNorm", "float"),
		("fRimTranslucency__uiUNorm", "float"),
		("fRimNormal__uiUNorm", "float"),
		("fSnowUVTile", "float"),
		("fSnowBlendColor__uiColor", "float4"),
		("fSnowMatControl__uiUNorm", "float4"),
		("fMaterialSnowBlendB", "float"),

		("align6", "ubyte[12]"),
		("fSnowControl", "float4"),

	])


class CBMhMaterialEMGlobal(EPyCStruct):
	fields = OrderedDict([


		("fMaterialPaintNum", "uint"),

		("align0", "ubyte[12]"),
		("fMaterialPaintType", "uint[16]"),

		("align1", "ubyte[12]"),
		("fMaterialPaintColor", "float4[16]"),
		("fMaterialPaintCapsuleP0", "float4[16]"),
		("fMaterialPaintCapsuleP1", "float4[16]"),
		("fMaterialPaintCapsuleR", "float[16]"),

		("align2", "ubyte[12]"),
		("fMaterialPaintBlendRange", "float2[16]"),

		("align3", "ubyte[8]"),
		("fMaterialPaintEmissive", "float4[16]"),
		("bMaterialPaintEmissive", "bbool"),
		("fMaterialWetBlend", "float"),
		("fMaterialWetRoughness", "float"),

		("align4", "ubyte[4]"),
		("fMaterialDamageColor", "float4"),
		("fMaterialDamageBlendRange", "float2"),

	])


class CBVR_Debug(EPyCStruct):
	fields = OrderedDict([


		("iMode", "uint"),

	])


class CBMhSky2PS(EPyCStruct):
	fields = OrderedDict([


		("fSkyGlobalIntensity", "float3"),

		("align0", "ubyte[4]"),
		("fSkyStarrySkyMapFactor", "float4"),
		("fSkySunUVOffset", "float2"),

		("align1", "ubyte[8]"),
		("fSkyWaterReflectionFactor", "float3"),
		("fSkyBlend", "float"),
		("bSkyFog", "bbool"),
		("fSkyFogBlend", "float"),
		("bSkyDeGamma", "bbool"),
		("fGamma", "float"),
		("iSkyAddress", "uint2"),
		("fSkySunlightMaskAlpha", "float"),

		("align2", "ubyte[4]"),
		("fSkySunlightMaskInverseSize", "float2"),
		("fSkyTopCloudUVScale0", "float2"),
		("fSkyTopCloudUVScale1", "float2"),

		("align3", "ubyte[8]"),
		("fSkySunlightSkyColor", "float3"),

		("align4", "ubyte[4]"),
		("fSkySunlightSkyMaskInverseSize", "float2"),
		("fSkyStarThreshold", "float"),
		("fSkyStarPower", "float"),
		("fSkyCloudContrast", "float"),
		("fSkyCurveMapTexelHeight", "float"),

		("align5", "ubyte[8]"),
		("fSkyBaseMapFactor", "float4"),
		("fSkyBaseSideCloudUVOffset", "float2"),
		("fSkyBaseTopCloudUVOffset0", "float2"),
		("fSkyBaseTopCloudUVOffset1", "float2"),

		("align6", "ubyte[8]"),
		("fSkyCloudSpeeds", "float2[4]"),

		("align7", "ubyte[8]"),
		("fSkySunCloudHighlightColors", "float4[4]"),
		("fSkySunCloudShadowColors", "float4[4]"),
		("fSkyMiddleCloudHighlightColors", "float4[4]"),
		("fSkyMiddleCloudShadowColors", "float4[4]"),
		("fSkyBackgroundCloudHighlightColors", "float4[4]"),
		("fSkyBackgroundCloudShadowColors", "float4[4]"),
		("fSkyCloudAlpha", "float[4]"),

		("align8", "ubyte[12]"),
		("fSkyBlendBaseMapFactor", "float4"),
		("fSkyBlendSideCloudUVOffset", "float2"),
		("fSkyBlendTopCloudUVOffset0", "float2"),
		("fSkyBlendTopCloudUVOffset1", "float2"),

		("align9", "ubyte[8]"),
		("fSkyBlendCloudSpeeds", "float2[4]"),

		("align10", "ubyte[8]"),
		("fSkyBlendSunCloudHighlightColors", "float4[4]"),
		("fSkyBlendSunCloudShadowColors", "float4[4]"),
		("fSkyBlendMiddleCloudHighlightColors", "float4[4]"),
		("fSkyBlendMiddleCloudShadowColors", "float4[4]"),
		("fSkyBlendBackgroundCloudHighlightColors", "float4[4]"),
		("fSkyBlendBackgroundCloudShadowColors", "float4[4]"),
		("fSkyBlendCloudAlpha", "float[4]"),

	])


class CBMhMaterialPLSkinLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fTranslucency__uiUNorm", "float"),
		("bBaseColorEmissive", "bbool"),
		("bBackFaceNormalFilp", "bbool"),
		("fAnimEmitMin", "float"),
		("fAnimEmitSpeed", "float"),
		("fAddColorUV__uiUNorm", "float2"),
		("bUseCMM", "bbool"),
		("fAddColorA__uiColor", "float4"),
		("fAddColorB__uiColor", "float4"),
		("fDetailNormalBlend__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fUVTransformDetailNormal", "float4"),

	])


class CBVignetting(EPyCStruct):
	fields = OrderedDict([


		("fOffset", "float"),
		("fPow", "float"),
		("fEllipticity", "float"),

		("align0", "ubyte[4]"),
		("fColor", "float3"),

	])


class CBMhMaterialEM102Local__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fTranslucency__uiUNorm", "float"),
		("bBaseColorEmissive", "bbool"),
		("fPaintUVTile", "float2"),
		("fAddNormalBlend__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fAddNormalMaskA__uiSNorm", "float4"),
		("fAddNormalMaskB__uiSNorm", "float4"),
		("fAddNormalMaskC__uiUNorm", "float"),
		("fAddNormalMaskD__uiUNorm", "float"),
		("bBackFaceShading", "bbool"),
		("bBackFaceNormalFilp", "bbool"),
		("fKizuColor__uiColor", "float3"),

		("align1", "ubyte[4]"),
		("fKizuUVOffset__uiUNorm", "float2"),
		("fKizuMultiply", "float"),
		("bLegendary", "bbool"),
		("fLegendColor__uiColor", "float4"),
		("fLegendMetalMask__uiUNorm", "float2"),
		("fLegendRoughness", "float"),

		("align2", "ubyte[4]"),
		("fLegendFilm__uiUNorm", "float3"),
		("fLegendSSSMask__uiUNorm", "float"),
		("fLegendHSV__uiSNorm", "float3"),
		("fLegendFilmIOR__uiUNorm", "float"),
		("fPartsMaskA__uiUNorm", "float"),
		("fPartsMaskB__uiUNorm", "float"),
		("fPartsMaskC__uiUNorm", "float"),
		("fPartsMaskD__uiUNorm", "float"),
		("fPartsMaskX__uiUNorm", "float"),
		("fPartsMaskY__uiUNorm", "float"),
		("fPartsMaskZ__uiUNorm", "float"),
		("fPartsMaskW__uiUNorm", "float"),
		("bUseOffset", "bbool"),
		("fOffsetScale", "float"),
		("bTranslucentOffset", "bbool"),
		("bAntiSSSEmit", "bbool"),
		("fFlowDirDir__uiDirection", "float3"),

		("align3", "ubyte[4]"),
		("fFlowControl__uiUNorm", "float4"),
		("fFlowTile", "float"),

		("align4", "ubyte[12]"),
		("fFlowColor__uiColor", "float4"),
		("fFlowMatControl__uiUNorm", "float4"),
		("fMaskBlend__uiUNorm", "float4"),
		("fMaskBlend_A__uiUNorm", "float2"),
		("fMaskBlend_B__uiUNorm", "float2"),
		("fFilmThickness__uiUNorm", "float"),
		("fFilmBlend__uiUNorm", "float"),
		("fFilmIOR__uiUNorm", "float"),
		("fRefraction__uiUNorm", "float"),
		("fRefractionBlend__uiUNorm", "float"),
		("fAnimEmitMin", "float"),
		("fAnimEmitSpeed", "float"),
		("bUseWaveEmit", "bbool"),
		("fAnimEmitWave", "float"),

		("align5", "ubyte[12]"),
		("fFurParam__uiUNorm", "float4"),
		("fFurTile", "float"),
		("fAlbedoBlend__uiSNorm", "float"),
		("bAlbedoOverUVsecondary", "bbool"),
		("fRimAlphaPower__uiSNorm", "float"),
		("fRimTranslucency__uiUNorm", "float"),
		("fRimNormal__uiUNorm", "float"),
		("fSnowUVTile", "float"),

		("align6", "ubyte[4]"),
		("fSnowBlendColor__uiColor", "float4"),
		("fSnowMatControl__uiUNorm", "float4"),
		("fMaterialSnowBlendB", "float"),

		("align7", "ubyte[12]"),
		("fSnowControl", "float4"),

	])


class CBMhMaterialEM111Local__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fTranslucency__uiUNorm", "float"),
		("bBaseColorEmissive", "bbool"),
		("fPaintUVTile", "float2"),
		("fAddNormalBlend__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fAddNormalMaskA__uiSNorm", "float4"),
		("fAddNormalMaskB__uiSNorm", "float4"),
		("fAddNormalMaskC__uiUNorm", "float"),
		("fAddNormalMaskD__uiUNorm", "float"),
		("bBackFaceShading", "bbool"),
		("bBackFaceNormalFilp", "bbool"),
		("fKizuColor__uiColor", "float3"),

		("align1", "ubyte[4]"),
		("fKizuUVOffset__uiUNorm", "float2"),
		("fKizuMultiply", "float"),
		("bLegendary", "bbool"),
		("fLegendColor__uiColor", "float4"),
		("fLegendMetalMask__uiUNorm", "float2"),
		("fLegendRoughness", "float"),

		("align2", "ubyte[4]"),
		("fLegendFilm__uiUNorm", "float3"),
		("fLegendSSSMask__uiUNorm", "float"),
		("fLegendHSV__uiSNorm", "float3"),
		("fLegendFilmIOR__uiUNorm", "float"),
		("fPartsMaskA__uiUNorm", "float"),
		("fPartsMaskB__uiUNorm", "float"),
		("fPartsMaskC__uiUNorm", "float"),
		("fPartsMaskD__uiUNorm", "float"),
		("fPartsMaskX__uiUNorm", "float"),
		("fPartsMaskY__uiUNorm", "float"),
		("fPartsMaskZ__uiUNorm", "float"),
		("fPartsMaskW__uiUNorm", "float"),
		("bUseOffset", "bbool"),
		("fOffsetScale", "float"),
		("bTranslucentOffset", "bbool"),
		("bAntiSSSEmit", "bbool"),
		("fFlowDirDir__uiDirection", "float3"),

		("align3", "ubyte[4]"),
		("fFlowControl__uiUNorm", "float4"),
		("fFlowTile", "float"),

		("align4", "ubyte[12]"),
		("fFlowColor__uiColor", "float4"),
		("fFlowMatControl__uiUNorm", "float4"),
		("fMaskBlend__uiUNorm", "float4"),
		("fMaskBlend_A__uiUNorm", "float2"),
		("fMaskBlend_B__uiUNorm", "float2"),
		("fFilmThickness__uiUNorm", "float"),
		("fFilmBlend__uiUNorm", "float"),
		("fFilmIOR__uiUNorm", "float"),
		("fRefraction__uiUNorm", "float"),
		("fRefractionBlend__uiUNorm", "float"),
		("fAnimEmitMin", "float"),
		("fAnimEmitSpeed", "float"),
		("bUseWaveEmit", "bbool"),
		("fAnimEmitWave", "float"),

		("align5", "ubyte[12]"),
		("fFurParam__uiUNorm", "float4"),
		("fFurTile", "float"),
		("bUseFlipUV", "bbool"),
		("fRimAlphaPower__uiSNorm", "float"),
		("fRimTranslucency__uiUNorm", "float"),
		("fRimNormal__uiUNorm", "float"),
		("fSnowUVTile", "float"),

		("align6", "ubyte[8]"),
		("fSnowBlendColor__uiColor", "float4"),
		("fSnowMatControl__uiUNorm", "float4"),
		("fMaterialSnowBlendB", "float"),

		("align7", "ubyte[12]"),
		("fSnowControl", "float4"),

	])


class CBAtmosphere(EPyCStruct):
	fields = OrderedDict([


		("fLightColor", "float3"),

		("align0", "ubyte[4]"),
		("fLightDir", "float3"),
		("fEarthRadius", "float"),
		("fHeightOffset", "float"),
		("fAtmosphereHeight", "float"),
		("fAtmosphereScaleHeight", "float"),

		("align1", "ubyte[4]"),
		("fAtmosphereRayleighK", "float3"),

		("align2", "ubyte[4]"),
		("fAtmospherePhaseK", "float3"),
		("fAerosolEffect", "float"),
		("fAerosolHeight", "float"),
		("fAerosolScaleHeight", "float"),
		("fAerosolMieK", "float"),
		("fAerosolPhaseK", "float"),
		("fAerosolEccentricity", "float2"),

	])


class CBSHDiffuse(EPyCStruct):
	fields = OrderedDict([


		("fSHDiffuseScale", "float"),
		("fSHDiffuseScaleInv", "float"),
		("bSHDiffuseUpsampling", "bbool"),

	])


class CBWaterDebug(EPyCStruct):
	fields = OrderedDict([


		("iWaterDebugMode", "int"),

	])


class CBBlink(EPyCStruct):
	fields = OrderedDict([


		("fOffset", "float"),
		("fPow", "float"),

		("align0", "ubyte[8]"),
		("fColor", "float3"),
		("fBlinkRate", "float"),
		("fHeightOffset", "float"),

	])


class CBMhMaterialEM118Local__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fTranslucency__uiUNorm", "float"),
		("bBaseColorEmissive", "bbool"),
		("fPaintUVTile", "float2"),
		("fAddNormalBlend__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fAddNormalMaskA__uiSNorm", "float4"),
		("fAddNormalMaskB__uiSNorm", "float4"),
		("fAddNormalMaskC__uiUNorm", "float"),
		("fAddNormalMaskD__uiUNorm", "float"),
		("bBackFaceShading", "bbool"),
		("bBackFaceNormalFilp", "bbool"),
		("fKizuColor__uiColor", "float3"),

		("align1", "ubyte[4]"),
		("fKizuUVOffset__uiUNorm", "float2"),
		("fKizuMultiply", "float"),
		("bLegendary", "bbool"),
		("fLegendColor__uiColor", "float4"),
		("fLegendMetalMask__uiUNorm", "float2"),
		("fLegendRoughness", "float"),

		("align2", "ubyte[4]"),
		("fLegendFilm__uiUNorm", "float3"),
		("fLegendSSSMask__uiUNorm", "float"),
		("fLegendHSV__uiSNorm", "float3"),
		("fLegendFilmIOR__uiUNorm", "float"),
		("fPartsMaskA__uiUNorm", "float"),
		("fPartsMaskB__uiUNorm", "float"),
		("fPartsMaskC__uiUNorm", "float"),
		("fPartsMaskD__uiUNorm", "float"),
		("fPartsMaskX__uiUNorm", "float"),
		("fPartsMaskY__uiUNorm", "float"),
		("fPartsMaskZ__uiUNorm", "float"),
		("fPartsMaskW__uiUNorm", "float"),
		("bUseOffset", "bbool"),
		("fOffsetScale", "float"),
		("bTranslucentOffset", "bbool"),
		("bAntiSSSEmit", "bbool"),
		("fFlowDirDir__uiDirection", "float3"),

		("align3", "ubyte[4]"),
		("fFlowControl__uiUNorm", "float4"),
		("fFlowTile", "float"),

		("align4", "ubyte[12]"),
		("fFlowColor__uiColor", "float4"),
		("fFlowMatControl__uiUNorm", "float4"),
		("fMaskBlend__uiUNorm", "float4"),
		("fMaskBlend_A__uiUNorm", "float2"),
		("fMaskBlend_B__uiUNorm", "float2"),
		("fFilmThickness__uiUNorm", "float"),
		("fFilmBlend__uiUNorm", "float"),
		("fFilmIOR__uiUNorm", "float"),
		("fRefraction__uiUNorm", "float"),
		("fRefractionBlend__uiUNorm", "float"),
		("fVAnimV__uiUNorm", "float"),

		("align5", "ubyte[8]"),
		("fDisplaceControl", "float4"),
		("fEmitBlend__uiUNorm", "float"),
		("fDetailEmit__uiColor", "float3"),
		("fVPushScale", "float"),
		("fAlphaTestControl__uiUNorm", "float"),
		("fAnimEmitMin", "float"),
		("fAnimEmitSpeed", "float"),
		("bUseWaveEmit", "bbool"),
		("fAnimEmitWave", "float"),
		("fEmitControl__uiUNorm", "float"),
		("fRimAlphaPower__uiSNorm", "float"),
		("fRimTranslucency__uiUNorm", "float"),
		("fRimNormal__uiUNorm", "float"),
		("fSnowUVTile", "float"),

		("align6", "ubyte[4]"),
		("fSnowBlendColor__uiColor", "float4"),
		("fSnowMatControl__uiUNorm", "float4"),
		("fMaterialSnowBlendB", "float"),

		("align7", "ubyte[12]"),
		("fSnowControl", "float4"),

	])


class CBUpdateBufferFromMeshConditions2(EPyCStruct):
	fields = OrderedDict([


		("iConditions2TargetNum", "uint"),

		("align0", "ubyte[12]"),
		("fConditions2TargetParam", "float4[16]"),
		("fConditions2TargetParam2", "float4[16]"),

	])


class CBSnowFieldPreDepth(EPyCStruct):
	fields = OrderedDict([


		("fSnowFieldPreDepthRegion", "float4"),
		("fSnowFieldPreDepthRegionY", "float2"),
		("iSnowFieldPreDepthCount", "uint"),
		("fSnowFieldBasePositionY", "float"),
		("fSnowFieldPreDepthBoundings", "float4[16]"),
		("fSnowFieldPreDepthMinMaxY", "float4[16]"),
		("fSnowFieldResolution", "float4"),

	])


class CBMhMaterialVfxSandFallLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fCubeMapFactor__uiColor", "float3"),

		("align0", "ubyte[4]"),
		("fUVTransformA", "float4"),
		("fUVTransformB", "float4"),
		("fAlbedoBlend", "float"),
		("fOpacityFactor", "float"),
		("fNormalFactor__uiUNorm", "float"),
		("fDetailfNormalFactor__uiUNorm", "float"),
		("fDetailNormalBlend__uiUNorm", "float"),
		("fRTNormalBlend__uiUNorm", "float"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fTranslucency__uiUNorm", "float"),
		("fRaflectionAngle__uiSNorm", "float"),
		("fFlowSpeed", "float"),
		("fFlowStrength", "float"),
		("fUVOffsetSpeed", "float"),
		("fUVOffsetSpeedFactorA", "float2"),
		("fUVOffsetSpeedFactorB", "float2"),
		("fInnerOffsetScale", "float"),
		("fDispFactor", "float"),
		("fAdditinalAxis", "float3"),
		("bSceneEnvMap", "bbool"),
		("bDisplacement", "bbool"),
		("bRTBlend", "bbool"),

	])


class CBMhMaterialEMSLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fTranslucency__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fUVTransformA", "float4"),
		("fBaseMapMod__uiUNorm", "float4"),
		("fBaseMapModLimitMax__uiUNorm", "float4"),
		("fBaseMapModLimitMin__uiUNorm", "float4"),
		("fFurParam__uiUNorm", "float4"),
		("fFurTile", "float"),
		("bFurLong", "bbool"),

		("align1", "ubyte[8]"),
		("fPattern_color__uiColor", "float3"),
		("fFilmThickness__uiUNorm", "float"),
		("fFilmBlend__uiUNorm", "float"),
		("fFilmIOR__uiUNorm", "float"),
		("bBaseColorEmissive", "bbool"),
		("bUseCMM", "bbool"),
		("fMummyTile", "float"),
		("fMummyBlend__uiUNorm", "float2"),

		("align2", "ubyte[4]"),
		("fMummyColor__uiColor", "float4"),
		("fMummyMatControl__uiUNorm", "float4"),
		("fMummyEmitColor__uiColor", "float3"),

	])


class CBCubeCopy(EPyCStruct):
	fields = OrderedDict([


		("regions", "int4[6]"),

	])


class CBGUIGlobal(EPyCStruct):
	fields = OrderedDict([


		("fGUIWMatrix", "float4x4"),
		("fGUIWMatrixPF", "float4x4"),
		("fGUIMatrix", "float4x4"),
		("fGUIMatrixPF", "float4x4"),
		("fGUIStaticColor", "float4"),
		("fGUIColorScale", "float4"),
		("fGUIAmbientColor", "float4"),
		("fGUISaturationParam", "float4"),
		("fGUIAlphaMaskRect", "float4"),
		("fGUIFontFilter", "float4"),
		("fGUIUVClamp", "float4"),
		("fGUIInvTextureSize", "float2"),
		("fGUIInvTextureSize2", "float2"),
		("fGUIZBias", "float"),
		("iGUIShaderState", "uint"),

	])


class CBWater(EPyCStruct):
	fields = OrderedDict([


		("cWorldMat", "float4x4"),
		("cLodEnabled", "bbool"),
		("cAxisX", "float3"),
		("cAxisZ", "float3"),
		("cWorldScaleY", "float"),
		("cVsSubdivInv", "float"),
		("cTsSubdivInv", "float"),
		("cAttenuation", "float"),
		("cTest", "uint"),
		("cNumWaveFunctionParam", "uint"),

	])


class CBMhMaterialEM100_01Local__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fTranslucency__uiUNorm", "float"),
		("bBaseColorEmissive", "bbool"),
		("fPaintUVTile", "float2"),
		("fAddNormalBlend__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fAddNormalMaskA__uiSNorm", "float4"),
		("fAddNormalMaskB__uiSNorm", "float4"),
		("fAddNormalMaskC__uiUNorm", "float"),
		("fAddNormalMaskD__uiUNorm", "float"),
		("bBackFaceShading", "bbool"),
		("bBackFaceNormalFilp", "bbool"),
		("fKizuColor__uiColor", "float3"),

		("align1", "ubyte[4]"),
		("fKizuUVOffset__uiUNorm", "float2"),
		("fKizuMultiply", "float"),
		("bLegendary", "bbool"),
		("fLegendColor__uiColor", "float4"),
		("fLegendMetalMask__uiUNorm", "float2"),
		("fLegendRoughness", "float"),

		("align2", "ubyte[4]"),
		("fLegendFilm__uiUNorm", "float3"),
		("fLegendSSSMask__uiUNorm", "float"),
		("fLegendHSV__uiSNorm", "float3"),
		("fLegendFilmIOR__uiUNorm", "float"),
		("fPartsMaskA__uiUNorm", "float"),
		("fPartsMaskB__uiUNorm", "float"),
		("fPartsMaskC__uiUNorm", "float"),
		("fPartsMaskD__uiUNorm", "float"),
		("fPartsMaskX__uiUNorm", "float"),
		("fPartsMaskY__uiUNorm", "float"),
		("fPartsMaskZ__uiUNorm", "float"),
		("fPartsMaskW__uiUNorm", "float"),
		("bUseOffset", "bbool"),
		("fOffsetScale", "float"),
		("bTranslucentOffset", "bbool"),
		("bAntiSSSEmit", "bbool"),
		("fFlowDirDir__uiDirection", "float3"),

		("align3", "ubyte[4]"),
		("fFlowControl__uiUNorm", "float4"),
		("fFlowTile", "float"),

		("align4", "ubyte[12]"),
		("fFlowColor__uiColor", "float4"),
		("fFlowMatControl__uiUNorm", "float4"),
		("fMaskBlend__uiUNorm", "float4"),
		("fMaskBlend_A__uiUNorm", "float2"),
		("fMaskBlend_B__uiUNorm", "float2"),
		("fFilmThickness__uiUNorm", "float"),
		("fFilmBlend__uiUNorm", "float"),
		("fFilmIOR__uiUNorm", "float"),
		("fRefraction__uiUNorm", "float"),
		("fRefractionBlend__uiUNorm", "float"),
		("fVPushScale", "float"),

		("align5", "ubyte[8]"),
		("fVPushRatio", "float3"),

		("align6", "ubyte[4]"),
		("fVpivot", "float3"),
		("fVPushBlend__uiUNorm", "float"),
		("fAnimEmitMin", "float"),
		("fAnimEmitSpeed", "float"),
		("bUseWaveEmit", "bbool"),
		("fAnimEmitWave", "float"),
		("fAnimEmitControl__uiUNorm", "float4"),
		("fFurParam__uiUNorm", "float4"),
		("fFurTile", "float"),
		("fAlbedoBlend__uiSNorm", "float"),
		("bAlbedoOverUVsecondary", "bbool"),
		("fRimAlphaPower__uiSNorm", "float"),
		("fRimTranslucency__uiUNorm", "float"),
		("fRimNormal__uiUNorm", "float"),
		("fSnowUVTile", "float"),

		("align7", "ubyte[4]"),
		("fSnowBlendColor__uiColor", "float4"),
		("fSnowMatControl__uiUNorm", "float4"),
		("fMaterialSnowBlendB", "float"),

		("align8", "ubyte[12]"),
		("fSnowControl", "float4"),

	])


class CBPrimitivePick(EPyCStruct):
	fields = OrderedDict([


		("iPrimAddress", "uint2"),

	])


class CBMhMaterialFakeRefractionLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fDetailNormalBlend__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fUVTransformA", "float4"),
		("fUVTransformB", "float4"),
		("fTranslucency__uiUNorm", "float"),
		("fRefraction__uiUNorm", "float"),

	])


class CBColorCorrect(EPyCStruct):
	fields = OrderedDict([


		("fMatrix", "float4x4"),
		("fBlendRate", "float"),
		("fVignettingOffset", "float"),
		("fVignettingPow", "float"),
		("bToneCurve", "bbool"),
		("bVignetting", "bbool"),
		("bVignettingEllipse", "bbool"),
		("fScreenAlpha", "float"),

	])


class CBMhMaterialDynamicSnow__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fDetailNormalBlend__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fUVTransformA", "float4"),
		("fUVTransformB", "float4"),
		("fTranslucency__uiUNorm", "float"),
		("fEdgesPerScreenHeight", "float"),

		("align1", "ubyte[8]"),
		("fWorldPositionMax", "float3"),

		("align2", "ubyte[4]"),
		("fWorldPositionMin", "float3"),
		("fHeightScale", "float"),
		("fVertexColorMapMask__uiUNorm", "float4"),
		("fTessLevel", "float"),

	])


class CBCapsuleAOGeomParam_AOGeometryParam(EPyCStruct):
	fields = OrderedDict([

		("ppdlVectorLengthSqInv", "float4"),
		("StPointVecRadius", "float4"),
		("LineVecMaxArea", "float4"),

	])
        
class CBCapsuleAOGeomParam  (Mod3Container):
	Mod3Class = CBCapsuleAOGeomParam_AOGeometryParam
	baseCount = 160	


class CBMotionBlurReconion(EPyCStruct):
	fields = OrderedDict([


		("iTileSize", "int2"),
		("uNumSamples", "uint"),
		("fInvNumSamples", "float"),
		("fShutterSpeed", "float"),
		("fFurShutterSpeed", "float"),
		("fBlurThreshold", "float"),
		("fHalfPixelSize", "float"),
		("fMaxTexCoord", "float2"),
		("iDebugViewType", "int"),
		("bIsPrevious", "bbool"),
		("bIsLegacy", "bbool"),

	])


class CBBokehCOCSettings(EPyCStruct):
	fields = OrderedDict([


		("BokehNearColor", "float3"),
		("BokehColorFadeSmooth", "float"),
		("BokehFarColor", "float3"),
		("BokehCoCScale", "float"),
		("BokehCoCBias", "float"),
		("BokehScaler", "float2"),

		("align0", "ubyte[4]"),
		("BokehMaxTextureFetchCoord", "float2"),
		("BokehBaseImageMaxFetchPos", "float2"),
		("BokehBaseImageMaxFetchPosInv", "float2"),
		("BokehBaseImageMaxFetchPosInt", "int2"),
		("BokehContentScale", "float"),
		("BokehInfCoCSize", "float"),
		("BokehNearCoCScale", "float"),
		("BokehNearCoCBias", "float"),
		("BokehFarCoCScale", "float"),
		("BokehFarCoCBias", "float"),
		("BokehContrast", "float"),
		("BokehFarSmooth", "float"),
		("BokehNearBleedSmooth", "float"),
		("BokehSpreadOffsetCoC", "float"),
		("BokehSpreadScaleCoC", "float"),
		("BokehSpreadToePower", "float"),
		("BokehMipmapBias", "float"),
		("BokehMipmapScale", "float"),
		("BokehHorizontalStep", "float"),
		("BokehVerticalStep", "float"),
		("BokehMaxScale", "float"),
		("BokehInFocusThreshold", "float3"),
		("BokehIgnoreEffectRate", "float"),

		("align1", "ubyte[12]"),
		("BokehFarFetchOffset", "float4"),
		("AlwaysZeroValue", "int"),

	])


class CBMhMaterialVfxDistDispLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fCubeMapFactor__uiColor", "float3"),

		("align0", "ubyte[4]"),
		("fDistortionFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),

		("align1", "ubyte[8]"),
		("fUVTransformA", "float4"),
		("fUVTransformB", "float4"),
		("fDisplacementFactor", "float"),
		("fFlow_Speed", "float"),
		("fFlow_Strength", "float"),
		("fNormalFactor__uiUNorm", "float"),
		("fOpacityFactor", "float"),
		("fVolumeBlend__uiSNorm", "float"),
		("fDistortionAngle", "float"),
		("fDistortion", "float"),
		("fSpecularFactor", "float"),
		("fDiffuseChroma__uiUNorm", "float"),
		("fSpecularChroma__uiUNorm", "float"),
		("bRefractionEnable", "bbool"),
		("bVolumeBlendEnable", "bbool"),
		("fEmissiveBlendColor__uiColor", "float3"),
		("fEmissiveBlendColorBlend__uiUNorm", "float"),
		("fEmissiveBlendRimParam", "float3"),
		("fInnerOffsetScale", "float"),
		("fVelocityAttn", "float"),
		("fNormalDecalBlend__uiUNorm", "float"),

	])


class CBFXAAParam(EPyCStruct):
	fields = OrderedDict([


		("fFXAAQualitySubpix", "float"),
		("fFXAAQualityEdgeThreshold", "float"),
		("fFXAAQualityEdgeThresholdMin", "float"),

		("align0", "ubyte[4]"),
		("fFXAATexOnePitch", "float2"),

	])


class CBGUINoiseAndFade(EPyCStruct):
	fields = OrderedDict([


		("fGUINoiseOffset", "float4"),
		("fGUINoiseAndFadeParam", "float4"),
		("fGUIFadeColor", "float4"),

	])


class CBMhSky2VS(EPyCStruct):
	fields = OrderedDict([


		("fSkyWorld", "float3x4"),

	])


class CBMaterialSnow__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fEdgesPerScreenHeight", "float"),
		("fWorldPositionMax", "float3"),
		("fWorldPositionMin", "float3"),
		("fHeightScale", "float"),

	])


class CBSpeedTreeLocalWind_SpeedTreeLocalWind(EPyCStruct):
	fields = OrderedDict([

		("pos", "float3"),
		("radius", "float"),
		("dir", "float3"),
		("strength", "float"),
		("oscillateStrength", "float"),
		("oscillateSpeed", "float"),
		("moveType", "uint"),
		("padding", "float"),

	])
        
class CBSpeedTreeLocalWind  (Mod3Container):
	Mod3Class = CBSpeedTreeLocalWind_SpeedTreeLocalWind
	baseCount = 128	


class CB_CombinedFilter(EPyCStruct):
	fields = OrderedDict([


		("bEnableFXAA", "bbool"),
		("bEnableTemporalAA", "bbool"),
		("bEnableColorCorrect", "bbool"),
		("bEnableImagePlane", "bbool"),

	])


class CBBloomSample(EPyCStruct):
	fields = OrderedDict([


		("fBloomFilterRegion", "float4"),

	])


class CBMhMaterialUberIceLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fTranslucency__uiUNorm", "float"),
		("bBaseColorEmissive", "bbool"),
		("fAnimEmitMin", "float"),
		("fAnimEmitSpeed", "float"),
		("fAnimEmitWave", "float"),
		("bUseWaveEmit", "bbool"),
		("bUseWaveAlpha", "bbool"),
		("bUseCMM", "bbool"),
		("fAddColorA__uiColor", "float4"),
		("fAddColorB__uiColor", "float4"),
		("fAddColorC__uiColor", "float4"),
		("fAddColorD__uiColor", "float4"),
		("fFurParam__uiUNorm", "float4"),
		("fFurTile", "float"),
		("fSecondaryEmitColor__uiColor", "float3"),
		("fSecondaryEmit_Control", "float4"),
		("fFilmThickness__uiUNorm", "float"),
		("fFilmBlend__uiUNorm", "float"),
		("fFilmIOR__uiUNorm", "float"),

		("align0", "ubyte[4]"),
		("fEmissiveBlendColor__uiColor", "float3"),
		("fEmissiveBlendColorBlend__uiUNorm", "float"),
		("fEmissiveBlendRimParam", "float3"),
		("fRefraction__uiSNorm", "float"),
		("fRefractionRotation__uiSNorm", "float"),
		("fPanoramaTile", "float"),
		("fVPushScale", "float"),
		("fVPushWave", "float"),
		("fVPushSpeed", "float"),
		("bUseFlipUV", "bbool"),
		("bBackFaceNormalFilp", "bbool"),
		("bUseEmitMask", "bbool"),
		("bUseRoughColor", "bbool"),
		("fRoughMask__uiUNorm", "float2"),
		("bUsePaint", "bbool"),
		("fPaintMapRC", "float2"),
		("fPaintMapNum", "float"),

		("align1", "ubyte[4]"),
		("fPaintMapOffset__uiSNorm", "float4"),
		("fPaintColor__uiColor", "float4"),
		("fPaintRoughness__uiUNorm", "float"),
		("fPaintMetal__uiUNorm", "float"),
		("bUseOffset", "bbool"),
		("fInnerOffsetScale", "float"),
		("bUseFly", "bbool"),
		("iWingNum", "uint"),
		("bUseAnimAlpha", "bbool"),
		("fAnimAlphaSpeed", "float"),
		("bParallax_Refraction", "bbool"),
		("fRefractBlend__uiUNorm", "float"),
		("fParallax_height__uiUNorm", "float"),
		("fRefraction_tile", "float"),
		("fRefraction_distortion__uiUNorm", "float"),

		("align2", "ubyte[12]"),
		("fSnowControl", "float4"),
		("fMaterialSnowBlendA", "float"),
		("fMaterialSnowBlendB", "float"),
		("fSnowTile", "float"),

		("align3", "ubyte[4]"),
		("fSnowColor__uiColor", "float3"),

		("align4", "ubyte[4]"),
		("fSnowMatControl__uiUNorm", "float4"),
		("fSnowUVOffset__uiUNorm", "float2"),
		("bUseSnowDistance", "bbool"),

	])


class CBNewDOFFilter2(EPyCStruct):
	fields = OrderedDict([


		("coc_bias", "float"),
		("coc_scale", "float"),
		("pcoc", "float"),
		("quad_reduction_threshold", "float"),
		("quater_resolution_threshold", "float"),
		("near_blur_scaler", "float"),
		("depth_adjuist_factor", "float"),
		("bokeh_intensity_threshold", "float"),
		("bokeh_shape_factor", "float"),
		("dof_single_pixel_radius", "float"),
		("depth_scale_foreground", "float"),
		("dof_aspect", "float"),
		("far_ignore", "bbool"),
		("near_ignore", "bbool"),
		("far_coef", "float"),
		("near_coef", "float"),
		("out_alpha", "float"),
		("fVignettingOffset", "float"),
		("fVignettingPow", "float"),
		("bVignetting", "bbool"),
		("fVignettingEllipticity", "float"),
		("fVignettingColor", "float3"),

	])


class CBSpeedTreeSystem(EPyCStruct):
	fields = OrderedDict([


		("fSpeedTreeSystemParam", "float4"),
		("iSpeedTreeSystemParam", "uint3"),

	])


class CBLayoutCache(EPyCStruct):
	fields = OrderedDict([


		("iEmitterID", "uint"),
		("iParticleStride", "uint"),
		("iParticleMaxNum", "uint"),
		("iOutputOffset", "uint"),
		("iOutputFlags", "uint"),

	])


class CBMhMaterialVfxAuroraLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveFactor__uiColor", "float3"),
		("fOpacityFactor", "float"),
		("fVolumeBlend__uiSNorm", "float"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fTranslucency__uiUNorm", "float"),
		("fInnerOffsetScale", "float"),
		("fVelocityAttn", "float"),
		("fDispFactor", "float"),

		("align0", "ubyte[4]"),
		("fUVTransformA", "float4"),
		("fUVTransformB", "float4"),

	])


class CBMhMaterialFakeSphereLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fDetailNormalBlend__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fUVTransformA", "float4"),
		("fUVTransformB", "float4"),
		("fTranslucency__uiUNorm", "float"),
		("bForwardFog", "bbool"),
		("bAddSphere", "bbool"),

	])


class CBMhMaterialEM044Local__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fTranslucency__uiUNorm", "float"),
		("bBaseColorEmissive", "bbool"),
		("fPaintUVTile", "float2"),
		("fAddNormalBlend__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fAddNormalMaskA__uiSNorm", "float4"),
		("fAddNormalMaskB__uiSNorm", "float4"),
		("fAddNormalMaskC__uiUNorm", "float"),
		("fAddNormalMaskD__uiUNorm", "float"),
		("bBackFaceShading", "bbool"),
		("bBackFaceNormalFilp", "bbool"),
		("fKizuColor__uiColor", "float3"),

		("align1", "ubyte[4]"),
		("fKizuUVOffset__uiUNorm", "float2"),
		("fKizuMultiply", "float"),
		("bLegendary", "bbool"),
		("fLegendColor__uiColor", "float4"),
		("fLegendMetalMask__uiUNorm", "float2"),
		("fLegendRoughness", "float"),

		("align2", "ubyte[4]"),
		("fLegendFilm__uiUNorm", "float3"),
		("fLegendSSSMask__uiUNorm", "float"),
		("fLegendHSV__uiSNorm", "float3"),
		("fLegendFilmIOR__uiUNorm", "float"),
		("fPartsMaskA__uiUNorm", "float"),
		("fPartsMaskB__uiUNorm", "float"),
		("fPartsMaskC__uiUNorm", "float"),
		("fPartsMaskD__uiUNorm", "float"),
		("fPartsMaskX__uiUNorm", "float"),
		("fPartsMaskY__uiUNorm", "float"),
		("fPartsMaskZ__uiUNorm", "float"),
		("fPartsMaskW__uiUNorm", "float"),
		("bUseOffset", "bbool"),
		("fOffsetScale", "float"),
		("bTranslucentOffset", "bbool"),
		("bAntiSSSEmit", "bbool"),
		("fFlowDirDir__uiDirection", "float3"),

		("align3", "ubyte[4]"),
		("fFlowControl__uiUNorm", "float4"),
		("fFlowTile", "float"),

		("align4", "ubyte[12]"),
		("fFlowColor__uiColor", "float4"),
		("fFlowMatControl__uiUNorm", "float4"),
		("fFilmThickness__uiUNorm", "float"),
		("fFilmBlend__uiUNorm", "float"),
		("fFilmIOR__uiUNorm", "float"),
		("fRefraction__uiUNorm", "float"),
		("fRefractionBlend__uiUNorm", "float"),
		("fAnimEmitMin", "float"),
		("fAnimEmitSpeed", "float"),
		("bUseWaveEmit", "bbool"),
		("fAnimEmitWave", "float"),
		("fRimAlphaPower__uiSNorm", "float"),
		("fRimTranslucency__uiUNorm", "float"),
		("fRimNormal__uiUNorm", "float"),
		("fSnowUVTile", "float"),

		("align5", "ubyte[12]"),
		("fSnowBlendColor__uiColor", "float4"),
		("fSnowMatControl__uiUNorm", "float4"),
		("fMaterialSnowBlendB", "float"),

		("align6", "ubyte[12]"),
		("fSnowControl", "float4"),

	])


class CBMhSky2Sun(EPyCStruct):
	fields = OrderedDict([


		("fRotMatrix", "float4x4"),
		("fSize", "float2"),
		("fIntensity", "float"),

		("align0", "ubyte[4]"),
		("fSkySunMapFactor", "float4"),
		("fBloomThreshold", "float"),
		("bSkySunIsRenderingWater", "bbool"),

		("align1", "ubyte[8]"),
		("fSkySunWaterReflectionFactor", "float3"),
		("fBloomTransparencyCoefficient", "float"),
		("fRenderTargetInverseSize", "float2"),

	])


class CBSpeedTreeCollision__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fLocalHeightAdjust", "float"),
		("fLocalWindOverallFactor", "float"),
		("fLocalWindBranchlFactor", "float"),
		("fLocalWindLeafFactor", "float"),
		("fFacingLeavesShadowFactor__uiUNorm", "float"),
		("fWindOneSidedBias", "float"),
		("bWindOneSidedUvFlip", "bbool"),
		("bSpeedTreeLodSmooth", "bbool"),

	])


class CBUpdateBufferFromMeshData(EPyCStruct):
	fields = OrderedDict([


		("iUpdateBufferOffset", "uint"),

	])


class CBDepthColor(EPyCStruct):
	fields = OrderedDict([


		("fDepthColorBlendMode", "uint"),
		("fDepthColorBlendRate", "float"),

		("align0", "ubyte[8]"),
		("fDepthColorColor", "float3"),
		("fDepthColorDistanceStart", "float"),
		("fDepthColorDistanceEnd", "float"),

		("align1", "ubyte[12]"),
		("fDepthColorBlendCurve", "float[256]"),

	])


class CBLightShaft_LightParam(EPyCStruct):
	fields = OrderedDict([


		("fLightShaftPosition", "float3"),
		("fLightShaftBoundingRadius", "float"),
		("fLightShaftDirection", "float3"),
		("fLightShaftFalloff", "float"),
		("fLightShaftMisc", "uint"),
		("fLightShaftAttenuation", "float3"),
		("fLightShaftColor", "float3"),
		("fLightShaftMinRoughness", "float"),
		("fLightShaftShadowMat", "float4x4"),
		("fLightShaftShadowExtra", "float4"),
		("fLightShaftShadowMapSize", "uint"),
		("fLightShaftShadowMapRegion", "uint3"),

	])


class CBMhMaterialEM109Local__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fTranslucency__uiUNorm", "float"),
		("bBaseColorEmissive", "bbool"),
		("fPaintUVTile", "float2"),
		("fAddNormalBlend__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fAddNormalMaskA__uiSNorm", "float4"),
		("fAddNormalMaskB__uiSNorm", "float4"),
		("fAddNormalMaskC__uiUNorm", "float"),
		("fAddNormalMaskD__uiUNorm", "float"),
		("bBackFaceShading", "bbool"),
		("bBackFaceNormalFilp", "bbool"),
		("fKizuColor__uiColor", "float3"),

		("align1", "ubyte[4]"),
		("fKizuUVOffset__uiUNorm", "float2"),
		("fKizuMultiply", "float"),
		("bLegendary", "bbool"),
		("fLegendColor__uiColor", "float4"),
		("fLegendMetalMask__uiUNorm", "float2"),
		("fLegendRoughness", "float"),

		("align2", "ubyte[4]"),
		("fLegendFilm__uiUNorm", "float3"),
		("fLegendSSSMask__uiUNorm", "float"),
		("fLegendHSV__uiSNorm", "float3"),
		("fLegendFilmIOR__uiUNorm", "float"),
		("fPartsMaskA__uiUNorm", "float"),
		("fPartsMaskB__uiUNorm", "float"),
		("fPartsMaskC__uiUNorm", "float"),
		("fPartsMaskD__uiUNorm", "float"),
		("fPartsMaskX__uiUNorm", "float"),
		("fPartsMaskY__uiUNorm", "float"),
		("fPartsMaskZ__uiUNorm", "float"),
		("fPartsMaskW__uiUNorm", "float"),
		("bUseOffset", "bbool"),
		("fOffsetScale", "float"),
		("bTranslucentOffset", "bbool"),
		("bAntiSSSEmit", "bbool"),
		("fFlowDirDir__uiDirection", "float3"),

		("align3", "ubyte[4]"),
		("fFlowControl__uiUNorm", "float4"),
		("fFlowTile", "float"),

		("align4", "ubyte[12]"),
		("fFlowColor__uiColor", "float4"),
		("fFlowMatControl__uiUNorm", "float4"),
		("fDisplaceControl", "float4"),
		("fDispSpeed", "float"),
		("fFilmThickness__uiUNorm", "float"),
		("fFilmBlend__uiUNorm", "float"),
		("fFilmIOR__uiUNorm", "float"),
		("fRefraction__uiUNorm", "float"),
		("fRefractionBlend__uiUNorm", "float"),
		("bUseBlendDisplace", "bbool"),
		("fVAnimV__uiUNorm", "float"),
		("fVAnimPosScale", "float"),
		("bInvertX", "bbool"),
		("fAnimEmitMin", "float"),
		("fAnimEmitSpeed", "float"),
		("bUseWaveEmit", "bbool"),
		("fAnimEmitWave", "float"),

		("align5", "ubyte[8]"),
		("fFurParam__uiUNorm", "float4"),
		("fFurTile", "float"),
		("fRimAlphaPower__uiSNorm", "float"),
		("fRimTranslucency__uiUNorm", "float"),
		("fRimNormal__uiUNorm", "float"),
		("fSnowUVTile", "float"),

		("align6", "ubyte[12]"),
		("fSnowBlendColor__uiColor", "float4"),
		("fSnowMatControl__uiUNorm", "float4"),
		("fMaterialSnowBlendB", "float"),

		("align7", "ubyte[12]"),
		("fSnowControl", "float4"),

	])


class CBMhMaterialSpeedTreeStdBlendSnowLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fDetailNormalBlend__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fUVTransformA", "float4"),
		("fUVTransformB", "float4"),
		("fTranslucency__uiUNorm", "float"),

		("align1", "ubyte[12]"),
		("fBlendBaseMapFactor__uiColor", "float4"),
		("fBlendEmissiveMapFactor__uiColor", "float3"),
		("fBlendMetalic__uiUNorm", "float"),
		("fBlendRoughness__uiUNorm", "float"),
		("fBlendDetailNormalBlend__uiUNorm", "float"),
		("fBlendSubSurfaceBlend__uiUNorm", "float"),
		("fBlendRoughnessThreshold__uiUNorm", "float"),
		("fBlendRoughnessFillValue__uiUNorm", "float"),

		("align2", "ubyte[12]"),
		("fBlendUVTransformA", "float4"),
		("fBlendUVTransformB", "float4"),
		("bUseUVSecondaryMtA", "bbool"),
		("bUseUVSecondaryMtB", "bbool"),
		("bUseUVSecondaryMtBM", "bbool"),
		("bUseUVSecondaryDetailNMtA", "bbool"),
		("bUseUVSecondaryDetailNMtB", "bbool"),
		("bLightProbeEmissive", "bbool"),

		("align3", "ubyte[8]"),
		("fEmissiveBlendColor__uiColor", "float3"),
		("fEmissiveBlendColorBlend__uiUNorm", "float"),
		("fEmissiveBlendRimParam", "float3"),
		("bSpecialBlend", "bbool"),
		("bWetNormalBlend", "bbool"),
		("fWetNormalBlendRange__uiUNorm", "float2"),
		("fSnowAlphaRef__uiUNorm", "float"),
		("fSnowBaseMapFactor__uiColor", "float4"),
		("fSnowEmissiveMapFactor__uiColor", "float3"),
		("fSnowMetalic__uiUNorm", "float"),
		("fSnowRoughness__uiUNorm", "float"),
		("fSnowDetailNormalBlend__uiUNorm", "float"),
		("fSnowSubSurfaceBlend__uiUNorm", "float"),

		("align4", "ubyte[4]"),
		("fSnowUVTransformA", "float4"),
		("fSnowUVTransformB", "float4"),
		("fSnowDir__uiDirection", "float3"),
		("fSnowPlaneNormal__uiUNorm", "float"),
		("fSnowOp", "float3"),
		("bUseUVSecondarySnowMt", "bbool"),
		("bUseUVSecondarySnowMtBM", "bbool"),

	])


class CBGodRaysIterator(EPyCStruct):
	fields = OrderedDict([


		("fGodRayParams", "float4[8]"),

	])


class CBMhMaterialVfxDistDispWLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fCubeMapFactor__uiColor", "float3"),

		("align0", "ubyte[4]"),
		("fDistortionFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),

		("align1", "ubyte[8]"),
		("fUVTransformA", "float4"),
		("fUVTransformB", "float4"),
		("fDisplacementFactor", "float"),
		("fFlow_Speed", "float"),
		("fFlow_Strength", "float"),
		("fNormalFactor__uiUNorm", "float"),
		("fOpacityFactor", "float"),
		("fVolumeBlend__uiSNorm", "float"),
		("fDistortionAngle", "float"),
		("fDistortion", "float"),
		("fSpecularFactor", "float"),
		("fDiffuseChroma__uiUNorm", "float"),
		("fSpecularChroma__uiUNorm", "float"),
		("bRefractionEnable", "bbool"),
		("bVolumeBlendEnable", "bbool"),
		("fEmissiveBlendColor__uiColor", "float3"),
		("fEmissiveBlendColorBlend__uiUNorm", "float"),
		("fEmissiveBlendRimParam", "float3"),
		("fInnerOffsetScale", "float"),
		("fDisplacementFactorW", "float"),

		("align2", "ubyte[8]"),
		("fMudDir__uiDirection", "float3"),
		("bWorldPosOffsetScale", "bbool"),
		("fVelocityAttn", "float"),
		("fNormalDecalBlend__uiUNorm", "float"),

	])


class CBMhMaterialOZK001Local__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fBaseMapFactor__uiColor", "float4"),
		("fEmissiveMapFactor__uiColor", "float3"),
		("fMetalic__uiUNorm", "float"),
		("fRoughness__uiUNorm", "float"),
		("fSpecular__uiUNorm", "float"),
		("fSubSurfaceBlend__uiUNorm", "float"),
		("iSubSurfaceProfile", "uint"),
		("fTranslucency__uiUNorm", "float"),
		("bBaseColorEmissive", "bbool"),
		("fPaintUVTile", "float2"),
		("fAddNormalBlend__uiUNorm", "float"),

		("align0", "ubyte[12]"),
		("fAddNormalMaskA__uiSNorm", "float4"),
		("fAddNormalMaskB__uiSNorm", "float4"),
		("fAddNormalMaskC__uiUNorm", "float"),
		("fAddNormalMaskD__uiUNorm", "float"),
		("bBackFaceShading", "bbool"),
		("bBackFaceNormalFilp", "bbool"),
		("fKizuColor__uiColor", "float3"),

		("align1", "ubyte[4]"),
		("fKizuUVOffset__uiUNorm", "float2"),
		("fKizuMultiply", "float"),
		("bLegendary", "bbool"),
		("fLegendColor__uiColor", "float4"),
		("fLegendMetalMask__uiUNorm", "float2"),
		("fLegendRoughness", "float"),

		("align2", "ubyte[4]"),
		("fLegendFilm__uiUNorm", "float3"),
		("fLegendSSSMask__uiUNorm", "float"),
		("fLegendHSV__uiSNorm", "float3"),
		("fLegendFilmIOR__uiUNorm", "float"),
		("fPartsMaskA__uiUNorm", "float"),
		("fPartsMaskB__uiUNorm", "float"),
		("fPartsMaskC__uiUNorm", "float"),
		("fPartsMaskD__uiUNorm", "float"),
		("fPartsMaskX__uiUNorm", "float"),
		("fPartsMaskY__uiUNorm", "float"),
		("fPartsMaskZ__uiUNorm", "float"),
		("fPartsMaskW__uiUNorm", "float"),
		("bUseOffset", "bbool"),
		("fOffsetScale", "float"),
		("bTranslucentOffset", "bbool"),
		("bAntiSSSEmit", "bbool"),
		("fFlowDirDir__uiDirection", "float3"),

		("align3", "ubyte[4]"),
		("fFlowControl__uiUNorm", "float4"),
		("fFlowTile", "float"),

		("align4", "ubyte[12]"),
		("fFlowColor__uiColor", "float4"),
		("fFlowMatControl__uiUNorm", "float4"),
		("fMaskBlend__uiUNorm", "float4"),
		("fMaskBlend_A__uiUNorm", "float2"),
		("fMaskBlend_B__uiUNorm", "float2"),
		("fFilmThickness__uiUNorm", "float"),
		("fFilmBlend__uiUNorm", "float"),
		("fFilmIOR__uiUNorm", "float"),
		("fRefraction__uiUNorm", "float"),
		("fRefractionBlend__uiUNorm", "float"),
		("bUseBlendDisplace", "bbool"),
		("fVAnimV__uiUNorm", "float"),
		("fVAnimPosScale", "float"),
		("bInvertX", "bbool"),
		("fAnimEmitMin", "float"),
		("fAnimEmitSpeed", "float"),
		("bUseWaveEmit", "bbool"),
		("fAnimEmitWave", "float"),
		("fRimAlphaPower__uiSNorm", "float"),
		("fRimTranslucency__uiUNorm", "float"),
		("fRimNormal__uiUNorm", "float"),
		("bUseFullNormal", "bbool"),
		("fSnowUVTile", "float"),

		("align5", "ubyte[8]"),
		("fSnowBlendColor__uiColor", "float4"),
		("fSnowMatControl__uiUNorm", "float4"),
		("fMaterialSnowBlendB", "float"),

		("align6", "ubyte[12]"),
		("fSnowControl", "float4"),

	])


class CBPrimitiveMetaDataOcclusion(EPyCStruct):
	fields = OrderedDict([


		("fPrimOcclusionSphere", "float4"),

	])
shaderListing = 	{"CBSnowFieldBake":CBSnowFieldBake,
"CBUpdateBufferFromMesh":CBUpdateBufferFromMesh,
"CBMhMaterialUberLocal__disclosure":CBMhMaterialUberLocal__disclosure,
"CBSystemSnow":CBSystemSnow,
"CBMhSky2SimpleGBuffer":CBMhSky2SimpleGBuffer,
"CBWaterMaterial":CBWaterMaterial,
"CBMhMaterialVfxTornadoLocal__disclosure":CBMhMaterialVfxTornadoLocal__disclosure,
"CBMhMaterialIvyFloorLocal__disclosure":CBMhMaterialIvyFloorLocal__disclosure,
"CBMhMaterialEM057Local__disclosure":CBMhMaterialEM057Local__disclosure,
"CBDevelopColorPick":CBDevelopColorPick,
"CBPrimGpuSystem":CBPrimGpuSystem,
"CBRadialBlurFunction":CBRadialBlurFunction,
"CBFilter2":CBFilter2,
"CBMhMaterialVfxWaveLocal__disclosure":CBMhMaterialVfxWaveLocal__disclosure,
"CBMhMaterialNPCHairLocal__disclosure":CBMhMaterialNPCHairLocal__disclosure,
"CBGUIGBuffer":CBGUIGBuffer,
"CBMhSkyPS":CBMhSkyPS,
"CBGUIDevelop":CBGUIDevelop,
"CBCubeBlend":CBCubeBlend,
"CBCreateMipmap":CBCreateMipmap,
"CBMhMaterialEMLocal__disclosure":CBMhMaterialEMLocal__disclosure,
"CBMaterialCommon__disclosure":CBMaterialCommon__disclosure,
"CBGlobalIllumination":CBGlobalIllumination,
"CBMhMaterialEM117Local__disclosure":CBMhMaterialEM117Local__disclosure,
"CBMhMaterialTMG001Local__disclosure":CBMhMaterialTMG001Local__disclosure,
"CBMhMaterialSKM001Local__disclosure":CBMhMaterialSKM001Local__disclosure,
"CBSpeedTreePrimitiveInfo":CBSpeedTreePrimitiveInfo,
"CBMhMaterialEM100Local__disclosure":CBMhMaterialEM100Local__disclosure,
"CBOutline":CBOutline,
"SeaDisplacement":SeaDisplacement,
"CBBitonicSort":CBBitonicSort,
"CBDevelopFlags":CBDevelopFlags,
"CBMhMaterialVfxWaterLocal__disclosure":CBMhMaterialVfxWaterLocal__disclosure,
"cbHDAO":cbHDAO,
"CBPartialColor":CBPartialColor,
"CBSystemGamma":CBSystemGamma,
"CBVRCompute":CBVRCompute,
"CBSSSSS_Profile":CBSSSSS_Profile,
"CBMhMaterialSlantFloorLocal__disclosure":CBMhMaterialSlantFloorLocal__disclosure,
"CBConstant":CBConstant,
"CBViewProjection":CBViewProjection,
"CBMhMaterialFlowDirLocal__disclosure":CBMhMaterialFlowDirLocal__disclosure,
"CBLGTPRBDebug":CBLGTPRBDebug,
"CBVRCommon":CBVRCommon,
"CB_CombinedFilter_ImagePlane":CB_CombinedFilter_ImagePlane,
"pix_clear_constants":pix_clear_constants,
"CBPrimSystem":CBPrimSystem,
"CBMhMaterialEM080_01Local__disclosure":CBMhMaterialEM080_01Local__disclosure,
"CBLuminance":CBLuminance,
"CBMhMaterialSpeedTreeStdFurLocal__disclosure":CBMhMaterialSpeedTreeStdFurLocal__disclosure,
"CBMhMaterialPLEditFaceLocal__disclosure":CBMhMaterialPLEditFaceLocal__disclosure,
"CBMhMaterialNPCEditFaceLocal__disclosure":CBMhMaterialNPCEditFaceLocal__disclosure,
"CBMhMaterialStdLocal__disclosure":CBMhMaterialStdLocal__disclosure,
"CBGaussian":CBGaussian,
"CBTest":CBTest,
"CBTSAO":CBTSAO,
"CBMhMaterialNPCFaceLocal__disclosure":CBMhMaterialNPCFaceLocal__disclosure,
"CBGodRaysConfiguration":CBGodRaysConfiguration,
"CBMhSky2SimpleVS":CBMhSky2SimpleVS,
"CBNormalMerge":CBNormalMerge,
"CBMhMaterialEC021Local__disclosure":CBMhMaterialEC021Local__disclosure,
"CBVRGaussian":CBVRGaussian,
"CBInstancing":CBInstancing,
"CBSnowHeightPick":CBSnowHeightPick,
"CBColorCorrectToneCurve":CBColorCorrectToneCurve,
"CBShapeMesh":CBShapeMesh,
"CB_DL":CB_DL,
"CBMhMaterialLandscapeFlowLocal__disclosure":CBMhMaterialLandscapeFlowLocal__disclosure,
"CBAmbientOccluder":CBAmbientOccluder,
"CBSnowField2Material":CBSnowField2Material,
"CBToneMappingSdrSim":CBToneMappingSdrSim,
"CBMhMaterialSpeedTreeStdBlendLocal__disclosure":CBMhMaterialSpeedTreeStdBlendLocal__disclosure,
"CBSSSSS":CBSSSSS,
"CBRenderFrame":CBRenderFrame,
"CBMhMaterialFakeEyeLocal__disclosure":CBMhMaterialFakeEyeLocal__disclosure,
"CBSystem":CBSystem,
"CBModelChain":CBModelChain,
"CBPick":CBPick,
"CBSky":CBSky,
"CBSnowField2Debug":CBSnowField2Debug,
"CB_TemporalAA2":CB_TemporalAA2,
"CBLUTMaking":CBLUTMaking,
"CBMhEmissiveFog__disclosure":CBMhEmissiveFog__disclosure,
"CBNormalRecalc":CBNormalRecalc,
"CBConstantHaltonSequence":CBConstantHaltonSequence,
"CBSpeedTreeLocalWindPF":CBSpeedTreeLocalWindPF,
"CBSpeedTreeLocalWindPF_SpeedTreeLocalWind":CBSpeedTreeLocalWindPF_SpeedTreeLocalWind,
"CBMhMaterialFakeLensLocal__disclosure":CBMhMaterialFakeLensLocal__disclosure,
"CBPrimGpuOcclusionVoxelSystem":CBPrimGpuOcclusionVoxelSystem,
"CBMhMaterialVfxWave":CBMhMaterialVfxWave,
"CBTestLight":CBTestLight,
"CBMhMaterialFurnitureLocal__disclosure":CBMhMaterialFurnitureLocal__disclosure,
"CBSnowFall":CBSnowFall,
"CBSSLR":CBSSLR,
"CBGUIIcon":CBGUIIcon,
"CBSnowFieldGeometry":CBSnowFieldGeometry,
"CBResample":CBResample,
"CBMhMaterialPLLocal__disclosure":CBMhMaterialPLLocal__disclosure,
"CBMhMaterial_EM105_EVCLocal__disclosure":CBMhMaterial_EM105_EVCLocal__disclosure,
"CBSnowField4Geometry":CBSnowField4Geometry,
"CBMhMaterialTestLocal__disclosure":CBMhMaterialTestLocal__disclosure,
"CBMhDecal":CBMhDecal,
"CBViewFrustum":CBViewFrustum,
"CBFog":CBFog,
"CBMhMaterialEM124Local__disclosure":CBMhMaterialEM124Local__disclosure,
"CBVRRecompute":CBVRRecompute,
"CBLuminanceDebugDisp":CBLuminanceDebugDisp,
"CBLGTPRBGen":CBLGTPRBGen,
"CBMhMaterialStdBlendLocal__disclosure":CBMhMaterialStdBlendLocal__disclosure,
"CBBokehAutoFocus":CBBokehAutoFocus,
"CBMotionBlur":CBMotionBlur,
"CBMhMaterialEM103Local__disclosure":CBMhMaterialEM103Local__disclosure,
"CBBloomSettings":CBBloomSettings,
"CBLightProbes":CBLightProbes,
"CBSpeedTreeGlobalWind":CBSpeedTreeGlobalWind,
"CBSpeedTreeGlobalWind_SpeedTreeGlobalWind":CBSpeedTreeGlobalWind_SpeedTreeGlobalWind,
"CBMhMaterialLandscapeLocal__disclosure":CBMhMaterialLandscapeLocal__disclosure,
"CBMaterialDebug":CBMaterialDebug,
"CBPickObject":CBPickObject,
"CBHermiteCurveRGB":CBHermiteCurveRGB,
"CBMhSkyVS":CBMhSkyVS,
"CBMhMaterialIridescentBlendLocal__disclosure":CBMhMaterialIridescentBlendLocal__disclosure,
"CBMhMaterialEM002Local__disclosure":CBMhMaterialEM002Local__disclosure,
"CBMhMaterialEM080Local__disclosure":CBMhMaterialEM080Local__disclosure,
"CBCapsuleAO":CBCapsuleAO,
"CBMhMaterialFakeInnerEmitLocal__disclosure":CBMhMaterialFakeInnerEmitLocal__disclosure,
"CBImagePlane2":CBImagePlane2,
"CBMhMaterialNikuLocal__disclosure":CBMhMaterialNikuLocal__disclosure,
"CBMhMaterialVfxDispWaveLocal__disclosure":CBMhMaterialVfxDispWaveLocal__disclosure,
"CBSpeedTree":CBSpeedTree,
"CBMhMaterialVfxFloodLocal__disclosure":CBMhMaterialVfxFloodLocal__disclosure,
"CBPrimitiveDebug":CBPrimitiveDebug,
"CBSystemColor":CBSystemColor,
"CBAmbientOcclusion":CBAmbientOcclusion,
"CBMhMaterialSlantFloor":CBMhMaterialSlantFloor,
"CBMhMaterialScrIceBlendNoFurLocal__disclosure":CBMhMaterialScrIceBlendNoFurLocal__disclosure,
"CBMhMaterialFlowLavaLocal__disclosure":CBMhMaterialFlowLavaLocal__disclosure,
"CBMhMaterialSpeedTreeStdLocal__disclosure":CBMhMaterialSpeedTreeStdLocal__disclosure,
"CBWaterModel":CBWaterModel,
"CBLightParameters":CBLightParameters,
"CBLightParameters_LightParameter":CBLightParameters_LightParameter,
"CB_TemporalAA":CB_TemporalAA,
"CB_PlantOnSurface":CB_PlantOnSurface,
"CBImagePlane":CBImagePlane,
"CBMhMaterialEM125Local__disclosure":CBMhMaterialEM125Local__disclosure,
"CBPrimitiveEx":CBPrimitiveEx,
"cbHBAO":cbHBAO,
"CBMhMaterialNPCEyeLocal__disclosure":CBMhMaterialNPCEyeLocal__disclosure,
"CBMhMaterialFlagWaveLocal__disclosure":CBMhMaterialFlagWaveLocal__disclosure,
"CBMhMaterialVfxDebufBodyLocal__disclosure":CBMhMaterialVfxDebufBodyLocal__disclosure,
"CBContactShadowInfo":CBContactShadowInfo,
"CBSnowShoveler":CBSnowShoveler,
"CBLUTBlending":CBLUTBlending,
"CBPrimitive":CBPrimitive,
"CBErrorUnit":CBErrorUnit,
"CBMhMaterialSpeedTreeStdIceLocal__disclosure":CBMhMaterialSpeedTreeStdIceLocal__disclosure,
"CBSnowFieldMaterial":CBSnowFieldMaterial,
"CBWaterWaveMaterial":CBWaterWaveMaterial,
"CBSnowPreProcess":CBSnowPreProcess,
"CBMhMaterialFlagWaveBlendLocal__disclosure":CBMhMaterialFlagWaveBlendLocal__disclosure,
"CBMhMaterialScrIceLocal__disclosure":CBMhMaterialScrIceLocal__disclosure,
"CBScreen":CBScreen,
"CBDecalCommon":CBDecalCommon,
"CBMhMaterialVfxIceLocal__disclosure":CBMhMaterialVfxIceLocal__disclosure,
"CBDebug":CBDebug,
"CBMhMaterialArrayLocal__disclosure":CBMhMaterialArrayLocal__disclosure,
"CBColorCorrectCube":CBColorCorrectCube,
"CBMhDecalSM":CBMhDecalSM,
"CBWaterPick":CBWaterPick,
"CBMhMaterialEM115Local__disclosure":CBMhMaterialEM115Local__disclosure,
"CBHeightToNormal":CBHeightToNormal,
"CBMhMaterialPLHairLocal__disclosure":CBMhMaterialPLHairLocal__disclosure,
"CBSpeedTreeGlobalWindPF":CBSpeedTreeGlobalWindPF,
"CBSpeedTreeGlobalWindPF_SpeedTreeGlobalWind":CBSpeedTreeGlobalWindPF_SpeedTreeGlobalWind,
"CBVRVolumeParams":CBVRVolumeParams,
"CBVRVolumeParams_VolumeParam":CBVRVolumeParams_VolumeParam,
"CBVRVolumeParams_Constant":CBVRVolumeParams_Constant,
"CBVRVolumeParams_Cuboid":CBVRVolumeParams_Cuboid,
"CBVRVolumeParams_Spherical":CBVRVolumeParams_Spherical,
"CBVRVolumeParams_Spotlight":CBVRVolumeParams_Spotlight,
"CB_BGTexture":CB_BGTexture,
"CBHermiteCurve":CBHermiteCurve,
"CBMhMaterialScrWaterLocal__disclosure":CBMhMaterialScrWaterLocal__disclosure,
"CBTubeLight":CBTubeLight,
"CBModel":CBModel,
"CBPrimBufferDescription":CBPrimBufferDescription,
"CBMhMaterialSZK001Local__disclosure":CBMhMaterialSZK001Local__disclosure,
"CBGUIDistanceField":CBGUIDistanceField,
"CBMhSky2SimplePS":CBMhSky2SimplePS,
"CBWorkaround":CBWorkaround,
"CBLight":CBLight,
"CBImageEvaluator":CBImageEvaluator,
"CBMhMaterialGlobal":CBMhMaterialGlobal,
"CBMhMaterialScrIceBlendLocal__disclosure":CBMhMaterialScrIceBlendLocal__disclosure,
"CBMhMaterialFurLocal__disclosure":CBMhMaterialFurLocal__disclosure,
"CBMhMaterialNPCLocal__disclosure":CBMhMaterialNPCLocal__disclosure,
"CBTexturePosScaleFactor":CBTexturePosScaleFactor,
"CBNewDOFFilter":CBNewDOFFilter,
"CBMhSkyLpPS":CBMhSkyLpPS,
"CBMhMaterialEM024Local__disclosure":CBMhMaterialEM024Local__disclosure,
"CBMhMaterialEM063Local__disclosure":CBMhMaterialEM063Local__disclosure,
"CBMhMaterialEM011Local__disclosure":CBMhMaterialEM011Local__disclosure,
"CBCSClear":CBCSClear,
"CBStarrySky":CBStarrySky,
"CBROPTest":CBROPTest,
"CBMhMaterialSimpleLocal__disclosure":CBMhMaterialSimpleLocal__disclosure,
"CBRadialBlurFilter":CBRadialBlurFilter,
"CBMhMaterialNPCSkinLocal__disclosure":CBMhMaterialNPCSkinLocal__disclosure,
"CBMhSky2GBuffer":CBMhSky2GBuffer,
"CBHazeFilter":CBHazeFilter,
"CBDOFFilter":CBDOFFilter,
"CBGodRaysFilter":CBGodRaysFilter,
"CBMhMaterialIvyFloor":CBMhMaterialIvyFloor,
"CBVRFilter":CBVRFilter,
"CBFilter":CBFilter,
"CBMhMaterialStdBlendNoFurLocal__disclosure":CBMhMaterialStdBlendNoFurLocal__disclosure,
"CBMhMaterialPLEyeLocal__disclosure":CBMhMaterialPLEyeLocal__disclosure,
"CBMhMaterialEM105Local__disclosure":CBMhMaterialEM105Local__disclosure,
"CBMhSkyGBuffer":CBMhSkyGBuffer,
"CB_CombinedFilter_ColorCorrect":CB_CombinedFilter_ColorCorrect,
"CBLightShaft":CBLightShaft,
"CBWaterCustomLight":CBWaterCustomLight,
"CBMhMaterialSpeedTreeStdSnowLocal__disclosure":CBMhMaterialSpeedTreeStdSnowLocal__disclosure,
"CBSparkleParam":CBSparkleParam,
"CBWaterCustom":CBWaterCustom,
"CBMhMaterialEM036Local__disclosure":CBMhMaterialEM036Local__disclosure,
"CBUpdateBufferFromMeshConditions":CBUpdateBufferFromMeshConditions,
"CBBloom":CBBloom,
"CBMhMaterialBurnLocal__disclosure":CBMhMaterialBurnLocal__disclosure,
"CBPrimCopyState":CBPrimCopyState,
"CBToneMapping":CBToneMapping,
"CBMhMaterialVfxVATDistLocal__disclosure":CBMhMaterialVfxVATDistLocal__disclosure,
"CBMhMaterialEM106Local__disclosure":CBMhMaterialEM106Local__disclosure,
"CBMhMaterialVfxFakeInnerLocal__disclosure":CBMhMaterialVfxFakeInnerLocal__disclosure,
"CBComputeSkinning":CBComputeSkinning,
"CBBokehComposite":CBBokehComposite,
"CBWaterWave":CBWaterWave,
"CBSnowField3Geometry":CBSnowField3Geometry,
"CBDecal":CBDecal,
"CBMhMaterialBTK001Local__disclosure":CBMhMaterialBTK001Local__disclosure,
"CBCAS":CBCAS,
"CBMhMaterialEM032Local__disclosure":CBMhMaterialEM032Local__disclosure,
"CBMhMaterialEMGlobal":CBMhMaterialEMGlobal,
"CBVR_Debug":CBVR_Debug,
"CBMhSky2PS":CBMhSky2PS,
"CBMhMaterialPLSkinLocal__disclosure":CBMhMaterialPLSkinLocal__disclosure,
"CBVignetting":CBVignetting,
"CBMhMaterialEM102Local__disclosure":CBMhMaterialEM102Local__disclosure,
"CBMhMaterialEM111Local__disclosure":CBMhMaterialEM111Local__disclosure,
"CBAtmosphere":CBAtmosphere,
"CBSHDiffuse":CBSHDiffuse,
"CBWaterDebug":CBWaterDebug,
"CBBlink":CBBlink,
"CBMhMaterialEM118Local__disclosure":CBMhMaterialEM118Local__disclosure,
"CBUpdateBufferFromMeshConditions2":CBUpdateBufferFromMeshConditions2,
"CBSnowFieldPreDepth":CBSnowFieldPreDepth,
"CBMhMaterialVfxSandFallLocal__disclosure":CBMhMaterialVfxSandFallLocal__disclosure,
"CBMhMaterialEMSLocal__disclosure":CBMhMaterialEMSLocal__disclosure,
"CBCubeCopy":CBCubeCopy,
"CBGUIGlobal":CBGUIGlobal,
"CBWater":CBWater,
"CBMhMaterialEM100_01Local__disclosure":CBMhMaterialEM100_01Local__disclosure,
"CBPrimitivePick":CBPrimitivePick,
"CBMhMaterialFakeRefractionLocal__disclosure":CBMhMaterialFakeRefractionLocal__disclosure,
"CBColorCorrect":CBColorCorrect,
"CBMhMaterialDynamicSnow__disclosure":CBMhMaterialDynamicSnow__disclosure,
"CBCapsuleAOGeomParam":CBCapsuleAOGeomParam,
"CBCapsuleAOGeomParam_AOGeometryParam":CBCapsuleAOGeomParam_AOGeometryParam,
"CBMotionBlurReconion":CBMotionBlurReconion,
"CBBokehCOCSettings":CBBokehCOCSettings,
"CBMhMaterialVfxDistDispLocal__disclosure":CBMhMaterialVfxDistDispLocal__disclosure,
"CBFXAAParam":CBFXAAParam,
"CBGUINoiseAndFade":CBGUINoiseAndFade,
"CBMhSky2VS":CBMhSky2VS,
"CBMaterialSnow__disclosure":CBMaterialSnow__disclosure,
"CBSpeedTreeLocalWind":CBSpeedTreeLocalWind,
"CBSpeedTreeLocalWind_SpeedTreeLocalWind":CBSpeedTreeLocalWind_SpeedTreeLocalWind,
"CB_CombinedFilter":CB_CombinedFilter,
"CBBloomSample":CBBloomSample,
"CBMhMaterialUberIceLocal__disclosure":CBMhMaterialUberIceLocal__disclosure,
"CBNewDOFFilter2":CBNewDOFFilter2,
"CBSpeedTreeSystem":CBSpeedTreeSystem,
"CBLayoutCache":CBLayoutCache,
"CBMhMaterialVfxAuroraLocal__disclosure":CBMhMaterialVfxAuroraLocal__disclosure,
"CBMhMaterialFakeSphereLocal__disclosure":CBMhMaterialFakeSphereLocal__disclosure,
"CBMhMaterialEM044Local__disclosure":CBMhMaterialEM044Local__disclosure,
"CBMhSky2Sun":CBMhSky2Sun,
"CBSpeedTreeCollision__disclosure":CBSpeedTreeCollision__disclosure,
"CBUpdateBufferFromMeshData":CBUpdateBufferFromMeshData,
"CBDepthColor":CBDepthColor,
"CBLightShaft_LightParam":CBLightShaft_LightParam,
"CBMhMaterialEM109Local__disclosure":CBMhMaterialEM109Local__disclosure,
"CBMhMaterialSpeedTreeStdBlendSnowLocal__disclosure":CBMhMaterialSpeedTreeStdBlendSnowLocal__disclosure,
"CBGodRaysIterator":CBGodRaysIterator,
"CBMhMaterialVfxDistDispWLocal__disclosure":CBMhMaterialVfxDistDispWLocal__disclosure,
"CBMhMaterialOZK001Local__disclosure":CBMhMaterialOZK001Local__disclosure,
"CBPrimitiveMetaDataOcclusion":CBPrimitiveMetaDataOcclusion,}

generalhash =  lambda x:  CrcJamcrc.calc(x.encode())
shaderTranslation = {generalhash(key) & 0xFFFFF:shaderListing[key] for key in shaderListing}
