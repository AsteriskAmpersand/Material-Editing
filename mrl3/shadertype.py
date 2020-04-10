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
#CBViewProjection : 9999.shdr.src
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


#CBScreen : 9999.shdr.src
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


#CBLightParameters : 9999.shdr.src
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
class CBLightParameters (Mod3Container):
	Mod3Classes = CBLightParameters_LightParameter
	Mod3Counts = 256



#CBVRCommon : 9999.shdr.src
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


#CBVRCompute : 9999.shdr.src
class CBVRCompute(EPyCStruct):
	fields = OrderedDict([


		("iCountOffset", "uint"),

	])


#CBVRFilter : 1279.shdr.src
class CBVRFilter(EPyCStruct):
	fields = OrderedDict([


		("fDimensions", "float4"),
		("fFilterRegion", "float4"),
		("fFilterMipLevel", "float"),
		("vertical", "bbool"),

	])


#CBModel : 9990.shdr.src
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


#CBROPTest : 999.shdr.src
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


#CBUpdateBufferFromMeshData : 999.shdr.src
class CBUpdateBufferFromMeshData(EPyCStruct):
	fields = OrderedDict([


		("iUpdateBufferOffset", "uint"),

	])


#CBMhMaterialOZK001Local__disclosure : 99.shdr.src
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


#CBMhMaterialEM032Local__disclosure : 999.shdr.src
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


#CBLight : 9999.shdr.src
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


#CBInstancing : 999.shdr.src
class CBInstancing(EPyCStruct):
	fields = OrderedDict([


		("iInstanceIndex", "uint"),

	])


#CBBokehCOCSettings : 9564.shdr.src
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


#CBLightProbes : 9998.shdr.src
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


#CBLGTPRBDebug : 905.shdr.src
class CBLGTPRBDebug(EPyCStruct):
	fields = OrderedDict([


		("fProbeSize", "float"),
		("lineColor", "float3"),
		("iProbeDebugType", "uint"),

	])


#CBPrimSystem : 9686.shdr.src
class CBPrimSystem(EPyCStruct):
	fields = OrderedDict([


		("fPrimGammaCorrect", "float"),
		("fPrimAlphaLowerLimit", "float"),
		("fPrimGlobalLightReflectance", "float"),
		("iPrimSystemFalgs", "uint"),

	])


#CBPrimitive : 9686.shdr.src
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


#CBMhMaterialVfxFloodLocal__disclosure : 10090.shdr.src
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


#CBMaterialCommon__disclosure : 9960.shdr.src
class CBMaterialCommon__disclosure(EPyCStruct):
	fields = OrderedDict([


		("bBypass", "bbool"),
		("bDecalMask", "bbool"),
		("bEmissive", "bbool"),
		("iGBufferId", "uint"),
		("iOutlineId", "uint"),

	])


#CBFog : 9981.shdr.src
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


#CBRenderFrame : 9987.shdr.src
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


#CBTestLight : 9960.shdr.src
class CBTestLight(EPyCStruct):
	fields = OrderedDict([


		("fTestLightDir", "float3"),

		("align0", "ubyte[4]"),
		("fTestLightColor", "float3"),

	])


#CBPick : 9966.shdr.src
class CBPick(EPyCStruct):
	fields = OrderedDict([


		("iPickPoint", "uint2"),

	])


#CBMhMaterialEMGlobal : 994.shdr.src
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


#CBVRVolumeParams : 9977.shdr.src
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
class CBVRVolumeParams (Mod3Collection):
	Mod3Classes = ['CBVRVolumeParams_VolumeParam', 'CBVRVolumeParams_Constant', 'CBVRVolumeParams_Cuboid', 'CBVRVolumeParams_Spherical', 'CBVRVolumeParams_Spotlight']
	Mod3Counts = ['128', '128', '128', '128', '128']



#CBGaussian : 9668.shdr.src
class CBGaussian(EPyCStruct):
	fields = OrderedDict([


		("fOffset0", "float4"),
		("fOffset1", "float4"),
		("fWeight0", "float4"),
		("fWeight1", "float4"),
		("fEdgeSharpness", "float"),

	])


#CBMhSky2SimplePS : 8007.shdr.src
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


#CBSystemColor : 54.shdr.src
class CBSystemColor(EPyCStruct):
	fields = OrderedDict([


		("fSystemColor", "float4"),

	])


#CBNewDOFFilter : 9814.shdr.src
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


#CBAmbientOcclusion : 9984.shdr.src
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


#CB_TemporalAA2 : 8845.shdr.src
class CB_TemporalAA2(EPyCStruct):
	fields = OrderedDict([


		("fBlendRate", "float"),
		("bVelocityBase", "bbool"),
		("fVarianceGamma", "float"),
		("fSharpenAmount", "float"),

	])


#pix_clear_constants : 10166.shdr.src
class pix_clear_constants(EPyCStruct):
	fields = OrderedDict([


		("m_color", "float4"),

	])


#CBWaterCustomLight : 9552.shdr.src
class CBWaterCustomLight(EPyCStruct):
	fields = OrderedDict([


		("bShadowCascadeBias", "bbool"),

	])


#CBWaterMaterial : 9981.shdr.src
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


#CBWaterCustom : 9981.shdr.src
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


#CBCubeCopy : 10173.shdr.src
class CBCubeCopy(EPyCStruct):
	fields = OrderedDict([


		("regions", "int4[6]"),

	])


#CBViewFrustum : 340.shdr.src
class CBViewFrustum(EPyCStruct):
	fields = OrderedDict([


		("fViewFrustum", "float4[6]"),

	])


#CBTest : 10178.shdr.src
class CBTest(EPyCStruct):
	fields = OrderedDict([


		("fTestParam", "float4"),
		("fTestDirection", "float3"),
		("fTestType", "float"),
		("fTestColor", "float4"),
		("fDummyColor", "float4"),

	])


#CBUpdateBufferFromMesh : 955.shdr.src
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


#CBUpdateBufferFromMeshConditions2 : 955.shdr.src
class CBUpdateBufferFromMeshConditions2(EPyCStruct):
	fields = OrderedDict([


		("iConditions2TargetNum", "uint"),

		("align0", "ubyte[12]"),
		("fConditions2TargetParam", "float4[16]"),
		("fConditions2TargetParam2", "float4[16]"),

	])


#CBLuminance : 903.shdr.src
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


#CBSHDiffuse : 6972.shdr.src
class CBSHDiffuse(EPyCStruct):
	fields = OrderedDict([


		("fSHDiffuseScale", "float"),
		("fSHDiffuseScaleInv", "float"),
		("bSHDiffuseUpsampling", "bbool"),

	])


#CBMhMaterialVfxWaveLocal__disclosure : 10254.shdr.src
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


#CBMhMaterialVfxWave : 10254.shdr.src
class CBMhMaterialVfxWave(EPyCStruct):
	fields = OrderedDict([


		("iPointNum", "uint"),
		("fViewTime", "float"),

	])


#CB_PlantOnSurface : 10260.shdr.src
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


#CBMhSkyGBuffer : 10267.shdr.src
class CBMhSkyGBuffer(EPyCStruct):
	fields = OrderedDict([


		("iSkyGBufferId", "uint"),

	])


#CBPrimGpuOcclusionVoxelSystem : 4681.shdr.src
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


#CBSnowFieldMaterial : 9165.shdr.src
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


#CBConstantHaltonSequence : 9984.shdr.src
class CBConstantHaltonSequence(EPyCStruct):
	fields = OrderedDict([


		("fHaltonSequence", "float4[64]"),

	])


#CBCapsuleAO : 9752.shdr.src
class CBCapsuleAO(EPyCStruct):
	fields = OrderedDict([


		("fLightDirectionXYZAngle", "float4"),
		("fDistanceFallCoef", "float"),
		("fCapsuleAOIntensity", "float"),
		("uGeometryNum", "uint"),
		("uLightChannelMask", "uint"),

	])


#CBCapsuleAOGeomParam : 9752.shdr.src
class CBCapsuleAOGeomParam_AOGeometryParam(EPyCStruct):
	fields = OrderedDict([


		("ppdlVectorLengthSqInv", "float4"),
		("StPointVecRadius", "float4"),
		("LineVecMaxArea", "float4"),

	])
class CBCapsuleAOGeomParam (Mod3Container):
	Mod3Classes = CBCapsuleAOGeomParam_AOGeometryParam
	Mod3Counts = 256



#CBMhMaterialFlowLavaLocal__disclosure : 10325.shdr.src
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


#CBSSLR : 9987.shdr.src
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


#CBMhMaterialVfxDebufBodyLocal__disclosure : 1084.shdr.src
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


#CBLightShaft : 2569.shdr.src
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


#CBMhSky2PS : 8095.shdr.src
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


#CBPrimBufferDescription : 9979.shdr.src
class CBPrimBufferDescription(EPyCStruct):
	fields = OrderedDict([


		("iPrimVertexBufferOffset", "uint"),
		("iPrimTotalVertexNum", "uint"),
		("iPrimRequestNum", "uint"),

	])


#CBPrimitiveEx : 954.shdr.src
class CBPrimitiveEx(EPyCStruct):
	fields = OrderedDict([


		("fPrimParamEx0", "float4"),
		("fPrimParamEx1", "float4"),
		("fPrimParamEx2", "float4"),
		("iPrimParamEx3", "uint4"),

	])


#CBPrimitivePick : 9686.shdr.src
class CBPrimitivePick(EPyCStruct):
	fields = OrderedDict([


		("iPrimAddress", "uint2"),

	])


#CBComputeSkinning : 7532.shdr.src
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


#CBCubeBlend : 685.shdr.src
class CBCubeBlend(EPyCStruct):
	fields = OrderedDict([


		("fCubeBlendRate", "float"),

	])


#CBWaterWave : 9116.shdr.src
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


#CBSystemSnow : 9892.shdr.src
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


#CBSnowField4Geometry : 567.shdr.src
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


#CBWorkaround : 564.shdr.src
class CBWorkaround(EPyCStruct):
	fields = OrderedDict([


		("iWorkaroundConstant", "uint"),

	])


#CBSnowField2Material : 665.shdr.src
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


#CBMhMaterialVfxDistDispWLocal__disclosure : 1214.shdr.src
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


#CBBloom : 6755.shdr.src
class CBBloom(EPyCStruct):
	fields = OrderedDict([


		("fBloomThreshold", "float"),
		("fBloomRenormalize", "float"),
		("bGamutSrgb", "bbool"),

		("align0", "ubyte[4]"),
		("fDirtColor", "float4"),

	])


#CBFilter : 9668.shdr.src
class CBFilter(EPyCStruct):
	fields = OrderedDict([


		("fFilterRegion", "float4"),
		("fFilterMipLevel", "float"),

	])


#CBGUIGlobal : 8867.shdr.src
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


#CBGUIGBuffer : 1225.shdr.src
class CBGUIGBuffer(EPyCStruct):
	fields = OrderedDict([


		("iGUIGBufferLightChannel", "uint"),
		("fGUIGBufferEmissiveColor", "float3"),
		("fGUIGBufferParam", "float3"),

	])


#CBWaterModel : 544.shdr.src
class CBWaterModel(EPyCStruct):
	fields = OrderedDict([


		("fMWorldViewProjMat", "float4x4"),
		("fMWorldMat", "float4x4"),

	])


#CBMhMaterialEM105Local__disclosure : 188.shdr.src
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


#CBSystem : 9807.shdr.src
class CBSystem(EPyCStruct):
	fields = OrderedDict([


		("iRegion", "uint4"),
		("fSourceMipLevel", "float"),
		("fGammaCorrect", "float"),
		("fGammaCorrectEx", "float"),

	])


#CBVRGaussian : 1279.shdr.src
class CBVRGaussian(EPyCStruct):
	fields = OrderedDict([


		("fOffsets", "float4"),
		("fWeights", "float[5]"),
		("fEdgeSharpness", "float"),

	])


#CB_DL : 1289.shdr.src
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


#CBSnowField3Geometry : 406.shdr.src
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


#CBShapeMesh : 9990.shdr.src
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


#CBNormalRecalc : 1309.shdr.src
class CBNormalRecalc(EPyCStruct):
	fields = OrderedDict([


		("iIBOffset", "uint"),
		("iSkinningVertexBase", "uint"),
		("iTriangleCount", "uint"),
		("iVertexOffset", "uint"),
		("iRedirectOffset", "uint"),

	])


#CBMhSky2Sun : 5052.shdr.src
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


#CBAmbientOccluder : 9159.shdr.src
class CBAmbientOccluder(EPyCStruct):
	fields = OrderedDict([


		("fSceneTextureScale", "float2"),
		("fIntensity", "float"),
		("fTransparency", "float"),

	])


#CBMhMaterialEMSLocal__disclosure : 1379.shdr.src
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


#CBMhMaterialGlobal : 9960.shdr.src
class CBMhMaterialGlobal(EPyCStruct):
	fields = OrderedDict([


		("fMaterialWetBlend", "float"),
		("fMaterialWetRoughness", "float"),
		("bMaterialCustomLighting", "bbool"),
		("iMaterialCustomLightingGBufferIdMask", "uint"),
		("fMaterialHiddenSurfaceDrawIntensity", "float"),

	])


#CBLUTBlending : 1388.shdr.src
class CBLUTBlending(EPyCStruct):
	fields = OrderedDict([


		("fLUTBlend", "float"),
		("fVfxLUTBlend", "float"),
		("bIsBlend", "bbool"),
		("bIsVfxBlend", "bbool"),

	])


#CBVRRecompute : 8315.shdr.src
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


#CBMhMaterialStdLocal__disclosure : 4437.shdr.src
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


#CBDOFFilter : 9040.shdr.src
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


#CBImagePlane : 1497.shdr.src
class CBImagePlane(EPyCStruct):
	fields = OrderedDict([


		("fImagePlaneColor", "float4"),
		("fImagePlaneUVTransform", "float4x4"),
		("fImagePlaneTechnique", "uint"),
		("fBlendType", "uint"),
		("bIsScreenPass", "bbool"),
		("fGamma", "float"),

	])


#CBImagePlane2 : 1496.shdr.src
class CBImagePlane2(EPyCStruct):
	fields = OrderedDict([


		("fFilterUVMin", "float2"),
		("fFilterUVMax", "float2"),

	])


#CBHazeFilter : 1524.shdr.src
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


#CBMhMaterialVfxVATDistLocal__disclosure : 1608.shdr.src
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


#CBBokehComposite : 6050.shdr.src
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


#CBDecal : 8234.shdr.src
class CBDecal(EPyCStruct):
	fields = OrderedDict([


		("iDecalMode", "uint"),
		("fDecalMetallic", "float"),
		("fDecalRoughness", "float"),
		("fDecalNonMetallicFresnel", "float"),
		("fDecalLimitAngle", "float"),

	])


#CBMhMaterialFakeLensLocal__disclosure : 1686.shdr.src
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


#CBFilter2 : 9498.shdr.src
class CBFilter2(EPyCStruct):
	fields = OrderedDict([


		("fFilterUVMin", "float2"),
		("fFilterUVMax", "float2"),
		("fFilterSampleOffsets", "float[11]"),

		("align0", "ubyte[12]"),
		("fFilterSampleWeights", "float[11]"),
		("fFilterThreshold", "float"),

	])


#CBMhMaterialVfxDispWaveLocal__disclosure : 1772.shdr.src
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


#CBMhMaterialFlowDirLocal__disclosure : 1883.shdr.src
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


#CBCreateMipmap : 9166.shdr.src
class CBCreateMipmap(EPyCStruct):
	fields = OrderedDict([


		("iRegion", "uint4"),

	])


#CBWater : 6095.shdr.src
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


#CBMhMaterialEM103Local__disclosure : 2008.shdr.src
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


#CBPrimGpuSystem : 9490.shdr.src
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


#CBVR_Debug : 202.shdr.src
class CBVR_Debug(EPyCStruct):
	fields = OrderedDict([


		("iMode", "uint"),

	])


#CBBitonicSort : 8000.shdr.src
class CBBitonicSort(EPyCStruct):
	fields = OrderedDict([


		("iSortArrayLength", "uint"),
		("iCompareFlipSize", "uint"),
		("iCompareStride", "uint"),
		("iCompareDir", "uint"),

	])


#CBTSAO : 5754.shdr.src
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


#CBMhMaterialDynamicSnow__disclosure : 2134.shdr.src
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


#CBGodRaysFilter : 779.shdr.src
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


#CBBloomSample : 2158.shdr.src
class CBBloomSample(EPyCStruct):
	fields = OrderedDict([


		("fBloomFilterRegion", "float4"),

	])


#CBMhDecal : 8234.shdr.src
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


#CBMhDecalSM : 8234.shdr.src
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


#CBDebug : 5060.shdr.src
class CBDebug(EPyCStruct):
	fields = OrderedDict([


		("iDebugView", "int"),
		("iDebugViewChannel", "int"),
		("iDebugLightMaxCount", "int"),
		("fDebugViewBgAlpha", "float"),
		("fDebugViewFgAlpha", "float"),
		("fDebugViewScaling", "float2"),

	])


#CBMhSky2VS : 2210.shdr.src
class CBMhSky2VS(EPyCStruct):
	fields = OrderedDict([


		("fSkyWorld", "float3x4"),

	])


#CBMhMaterialEM100_01Local__disclosure : 2276.shdr.src
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


#CBGodRaysConfiguration : 779.shdr.src
class CBGodRaysConfiguration(EPyCStruct):
	fields = OrderedDict([


		("isUseOcclusionFactorFromTexture", "bbool"),
		("isUseAlphaOcclusion", "bbool"),
		("isUseScaleOcclusion", "bbool"),
		("isGrayColor", "bbool"),
		("iThreshold", "int"),

	])


#CBSSSSS : 8506.shdr.src
class CBSSSSS(EPyCStruct):
	fields = OrderedDict([


		("fBlurMaxDist", "float"),
		("fBlurEdgeSharpness", "float"),
		("iDiviserFactor", "uint"),

	])


#CBSSSSS_Profile : 2306.shdr.src
class CBSSSSS_Profile(EPyCStruct):
	fields = OrderedDict([


		("fRGBBlurWeight", "float4[16]"),
		("fBlurOffset", "float4[8]"),
		("fBlurTargetDist", "float4"),

	])


#CBNewDOFFilter2 : 9528.shdr.src
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


#CBMaterialDebug : 2321.shdr.src
class CBMaterialDebug(EPyCStruct):
	fields = OrderedDict([


		("iMaterialDebugView", "uint"),
		("bMaterialDebugZeroCheck", "bbool"),

		("align0", "ubyte[8]"),
		("fMaterialDebugColor", "float4"),

	])


#CBAtmosphere : 8399.shdr.src
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


#CBPrimitiveMetaDataOcclusion : 5746.shdr.src
class CBPrimitiveMetaDataOcclusion(EPyCStruct):
	fields = OrderedDict([


		("fPrimOcclusionSphere", "float4"),

	])


#CBSparkleParam : 3733.shdr.src
class CBSparkleParam(EPyCStruct):
	fields = OrderedDict([


		("fSparkleLightDir", "float4"),
		("fSparkleSize", "float"),

	])


#CBDevelopFlags : 7526.shdr.src
class CBDevelopFlags(EPyCStruct):
	fields = OrderedDict([


		("iDispChannel", "int"),
		("iDispCubeFace", "int"),
		("iDispMode", "int"),
		("fDispMipLevel", "float"),
		("fDispArraySlice", "float"),

	])


#CBMhMaterialEM100Local__disclosure : 2483.shdr.src
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


#CBMhMaterialLandscapeLocal__disclosure : 2566.shdr.src
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


#CBLightShaft_LightParam : 2569.shdr.src
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


#CBMhMaterialLandscapeFlowLocal__disclosure : 2653.shdr.src
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


#CBHermiteCurve : 2660.shdr.src
class CBHermiteCurve(EPyCStruct):
	fields = OrderedDict([


		("fHermiteParam", "float4[8]"),

	])


#CBErrorUnit : 2668.shdr.src
class CBErrorUnit(EPyCStruct):
	fields = OrderedDict([


		("iErrorUnitAddress", "uint2"),
		("iErrorUnitPass", "uint"),
		("iErrorUnitPrio", "uint"),

	])


#CBSnowFieldBake : 425.shdr.src
class CBSnowFieldBake(EPyCStruct):
	fields = OrderedDict([


		("iSnowFieldBakeAttr", "uint"),

	])


#CBHeightToNormal : 6337.shdr.src
class CBHeightToNormal(EPyCStruct):
	fields = OrderedDict([


		("fFactor", "float"),

	])


#CBColorCorrectCube : 9089.shdr.src
class CBColorCorrectCube(EPyCStruct):
	fields = OrderedDict([


		("fLinearFactor", "float"),
		("fDepthNear", "float"),
		("fDepthFar", "float"),

	])


#CBPrimCopyState : 9816.shdr.src
class CBPrimCopyState(EPyCStruct):
	fields = OrderedDict([


		("fNormalSlope", "float"),

	])


#CBColorCorrect : 2810.shdr.src
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


#CBMhMaterialEM115Local__disclosure : 2874.shdr.src
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


#CBMhMaterialFakeEyeLocal__disclosure : 2953.shdr.src
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


#CBWaterWaveMaterial : 8116.shdr.src
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


#CBStarrySky : 8773.shdr.src
class CBStarrySky(EPyCStruct):
	fields = OrderedDict([


		("fRotMatrix", "float4x4"),
		("fSize", "float2"),
		("fFactor", "float"),
		("fIntensity", "float"),
		("fScintillation", "float"),

	])


#CBMhMaterialEM109Local__disclosure : 3105.shdr.src
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


#CBUpdateBufferFromMeshConditions : 9491.shdr.src
class CBUpdateBufferFromMeshConditions(EPyCStruct):
	fields = OrderedDict([


		("fConditionsBlendAxis", "float3"),
		("fConditionsBlendHeightLimit", "float"),
		("fConditionsBlendHeightLimitOffset", "float"),
		("fConditionsBlendAngleLimit", "float"),
		("fConditionsBlendAngleScale", "float"),
		("fConditionsBlendAdd", "float"),

	])


#CBMhMaterialSZK001Local__disclosure : 3171.shdr.src
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


#CBLGTPRBGen : 9361.shdr.src
class CBLGTPRBGen(EPyCStruct):
	fields = OrderedDict([


		("iCurrentIndex", "uint"),
		("iWindowType", "uint"),

	])


#CBLUTMaking : 4731.shdr.src
class CBLUTMaking(EPyCStruct):
	fields = OrderedDict([


		("iLUTSize", "uint"),
		("iMaxWidth", "uint"),
		("fMaxLuminance", "float"),
		("bIsPQToLinear", "bbool"),

	])


#CBSnowPreProcess : 8591.shdr.src
class CBSnowPreProcess(EPyCStruct):
	fields = OrderedDict([


		("fNoiseBlendSVScale", "float"),
		("fNoiseHeightScale", "float"),
		("fNoiseBlendBias", "float"),

	])


#CBBloomSettings : 3946.shdr.src
class CBBloomSettings(EPyCStruct):
	fields = OrderedDict([


		("AdjustParams", "float4"),
		("CenterAndScale", "float4"),
		("Coefficient", "float4"),
		("TexHalfSizes", "float4"),

	])


#CBPrimitiveDebug : 3249.shdr.src
class CBPrimitiveDebug(EPyCStruct):
	fields = OrderedDict([


		("fWorldOffset", "float3"),

	])


#CBWaterDebug : 576.shdr.src
class CBWaterDebug(EPyCStruct):
	fields = OrderedDict([


		("iWaterDebugMode", "int"),

	])


#CBSnowField2Debug : 326.shdr.src
class CBSnowField2Debug(EPyCStruct):
	fields = OrderedDict([


		("iSnowField2DebugType", "uint"),

	])


#CBMaterialSnow__disclosure : 3370.shdr.src
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


#CBGUIDevelop : 334.shdr.src
class CBGUIDevelop(EPyCStruct):
	fields = OrderedDict([


		("fGUIOverlapDrawColor", "float3"),

	])


#CBToneMapping : 3371.shdr.src
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


#CB_TemporalAA : 6076.shdr.src
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


#CBMhMaterialNPCEyeLocal__disclosure : 3419.shdr.src
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


#CBSpeedTreeLocalWind : 7364.shdr.src
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
class CBSpeedTreeLocalWind (Mod3Container):
	Mod3Classes = CBSpeedTreeLocalWind_SpeedTreeLocalWind
	Mod3Counts = 128



#CBGodRaysIterator : 6159.shdr.src
class CBGodRaysIterator(EPyCStruct):
	fields = OrderedDict([


		("fGodRayParams", "float4[8]"),

	])


#CBCAS : 9471.shdr.src
class CBCAS(EPyCStruct):
	fields = OrderedDict([


		("iConst0", "uint4"),
		("iConst1", "uint4"),

	])


#CBSnowFieldGeometry : 9892.shdr.src
class CBSnowFieldGeometry(EPyCStruct):
	fields = OrderedDict([


		("fEdgesPerScreenHeight", "float"),
		("fWorldPositionMax", "float3"),
		("fWorldPositionMin", "float3"),
		("fShovelCornerBlendRate", "float"),

	])


#CBSnowShoveler : 3494.shdr.src
class CBSnowShoveler(EPyCStruct):
	fields = OrderedDict([


		("fMinMaxRangeWorldY", "float4"),

	])


#CBSnowFall : 3494.shdr.src
class CBSnowFall(EPyCStruct):
	fields = OrderedDict([


		("SnowAmount", "float"),

	])


#CBMhMaterialEM002Local__disclosure : 3581.shdr.src
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


#CBMhMaterialNPCHairLocal__disclosure : 3686.shdr.src
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


#CBBokehAutoFocus : 3713.shdr.src
class CBBokehAutoFocus(EPyCStruct):
	fields = OrderedDict([


		("SelectedFocusPoint", "uint2"),

	])


#CBTexturePosScaleFactor : 5740.shdr.src
class CBTexturePosScaleFactor(EPyCStruct):
	fields = OrderedDict([


		("drawStage", "float4"),
		("sceneFFTStage", "float4"),
		("kernelFFTStage", "float4"),

	])


#CBMhMaterialSimpleLocal__disclosure : 3785.shdr.src
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


#CBMhMaterialPLSkinLocal__disclosure : 3848.shdr.src
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


#CBSnowHeightPick : 389.shdr.src
class CBSnowHeightPick(EPyCStruct):
	fields = OrderedDict([


		("WriteOffset", "uint"),
		("SnowPickRenderFrame", "uint"),
		("PickRequestCount", "uint"),

		("align0", "ubyte[4]"),
		("PickPositionArray", "int4[31]"),

	])


#CBNormalMerge : 3941.shdr.src
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


#CBMhMaterialStdBlendNoFurLocal__disclosure : 4004.shdr.src
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


#CBDecalCommon : 40.shdr.src
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


#CBGUINoiseAndFade : 4032.shdr.src
class CBGUINoiseAndFade(EPyCStruct):
	fields = OrderedDict([


		("fGUINoiseOffset", "float4"),
		("fGUINoiseAndFadeParam", "float4"),
		("fGUIFadeColor", "float4"),

	])


#CBMhMaterialEM063Local__disclosure : 4092.shdr.src
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


#CBMhSkyVS : 7177.shdr.src
class CBMhSkyVS(EPyCStruct):
	fields = OrderedDict([


		("fSkyWorld", "float3x4"),

	])


#CBMhSkyLpPS : 4517.shdr.src
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


#CBSnowFieldPreDepth : 4152.shdr.src
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


#CBSpeedTreeCollision__disclosure : 7364.shdr.src
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


#CBSpeedTreePrimitiveInfo : 8768.shdr.src
class CBSpeedTreePrimitiveInfo(EPyCStruct):
	fields = OrderedDict([


		("iPrimitiveInfo", "uint4"),

	])


#CBSpeedTreeSystem : 7364.shdr.src
class CBSpeedTreeSystem(EPyCStruct):
	fields = OrderedDict([


		("fSpeedTreeSystemParam", "float4"),
		("iSpeedTreeSystemParam", "uint3"),

	])


#CBMhMaterialSpeedTreeStdBlendLocal__disclosure : 8071.shdr.src
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


#CBSpeedTree : 7364.shdr.src
class CBSpeedTree(EPyCStruct):
	fields = OrderedDict([


		("fSpeedTreeParam", "float2"),

		("align0", "ubyte[8]"),
		("iSpeedTreeParam", "int3"),

	])


#CBSpeedTreeGlobalWind : 7364.shdr.src
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
class CBSpeedTreeGlobalWind (Mod3Container):
	Mod3Classes = CBSpeedTreeGlobalWind_SpeedTreeGlobalWind
	Mod3Counts = 160



#CBSpeedTreeGlobalWindPF : 7324.shdr.src
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
class CBSpeedTreeGlobalWindPF (Mod3Container):
	Mod3Classes = CBSpeedTreeGlobalWindPF_SpeedTreeGlobalWind
	Mod3Counts = 160



#CBSpeedTreeLocalWindPF : 7324.shdr.src
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
class CBSpeedTreeLocalWindPF (Mod3Container):
	Mod3Classes = CBSpeedTreeLocalWindPF_SpeedTreeLocalWind
	Mod3Counts = 128



#CBGlobalIllumination : 8864.shdr.src
class CBGlobalIllumination(EPyCStruct):
	fields = OrderedDict([


		("fSpecularIntensity", "float"),
		("fSpecularTemporalBlendRate", "float"),
		("fSpecularDifference", "float"),

	])


#CBMhMaterialEM024Local__disclosure : 488.shdr.src
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


#CBMhMaterialVfxWaterLocal__disclosure : 4332.shdr.src
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


#CBMhMaterialIvyFloorLocal__disclosure : 4445.shdr.src
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


#CBMhMaterialIvyFloor : 4445.shdr.src
class CBMhMaterialIvyFloor(EPyCStruct):
	fields = OrderedDict([


		("iIvyFloorWindIndex", "int"),
		("iIvyFloorWindIndexPF", "int"),
		("iIvyFloorId", "uint2"),
		("fIvyFloorWindScale", "float"),

	])


#CBGUIDistanceField : 4448.shdr.src
class CBGUIDistanceField(EPyCStruct):
	fields = OrderedDict([


		("fGUIDFParam0", "float3"),

		("align0", "ubyte[4]"),
		("fGUIDFColor0", "float4"),
		("fGUIDFParam1", "float3"),

		("align1", "ubyte[4]"),
		("fGUIDFColor1", "float4"),

	])


#CBMhMaterialEC021Local__disclosure : 4489.shdr.src
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


#CBMhMaterialSpeedTreeStdFurLocal__disclosure : 4572.shdr.src
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


#CBCSClear : 4584.shdr.src
class CBCSClear(EPyCStruct):
	fields = OrderedDict([


		("iSize", "uint"),

	])


#CBGUIIcon : 4605.shdr.src
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


#CBMhMaterialSlantFloorLocal__disclosure : 4643.shdr.src
class CBMhMaterialSlantFloorLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fSinkLength", "float"),
		("fConstSinkLength", "float"),
		("fMaxSlant", "float"),
		("fSlantRange", "float"),

	])


#CBMhMaterialSlantFloor : 4643.shdr.src
class CBMhMaterialSlantFloor(EPyCStruct):
	fields = OrderedDict([


		("iSlantFloorWindIndex", "int"),
		("fSlantFloorWindScale", "float"),

	])


#CBMhSky2GBuffer : 4667.shdr.src
class CBMhSky2GBuffer(EPyCStruct):
	fields = OrderedDict([


		("iSkyGBufferId", "uint"),

	])


#CBLuminanceDebugDisp : 4673.shdr.src
class CBLuminanceDebugDisp(EPyCStruct):
	fields = OrderedDict([


		("iLuminanceDispMode", "uint"),

		("align0", "ubyte[12]"),
		("fLuminanceDebugDispColor", "float4"),
		("fLuminanceDebugDispMinMax", "float2"),

	])


#CBOutline : 7518.shdr.src
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


#CBMhMaterialEM125Local__disclosure : 4823.shdr.src
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


#CB_BGTexture : 4843.shdr.src
class CB_BGTexture(EPyCStruct):
	fields = OrderedDict([


		("fBGTextureColor", "float4"),

	])


#CBMhMaterialFakeInnerEmitLocal__disclosure : 4951.shdr.src
class CBMhMaterialFakeInnerEmitLocal__disclosure(EPyCStruct):
	fields = OrderedDict([


		("fEmissiveMapFactor__uiColor", "float3"),
		("fInnerOffsetScale", "float"),
		("fRimAlphaPower__uiUNorm", "float"),
		("fVolumeBlend__uiSNorm", "float"),

	])


#CBBlink : 491.shdr.src
class CBBlink(EPyCStruct):
	fields = OrderedDict([


		("fOffset", "float"),
		("fPow", "float"),

		("align0", "ubyte[8]"),
		("fColor", "float3"),
		("fBlinkRate", "float"),
		("fHeightOffset", "float"),

	])


#CBMhMaterialEM011Local__disclosure : 5017.shdr.src
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


#CBMhMaterialNPCFaceLocal__disclosure : 5133.shdr.src
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


#CBMotionBlur : 5151.shdr.src
class CBMotionBlur(EPyCStruct):
	fields = OrderedDict([


		("iMotionBlurSampleNum", "int"),
		("fMotionBlurShutterSpeed", "float"),
		("fMaxAdditionalVelocity", "float"),

		("align0", "ubyte[4]"),
		("fTransform", "float4x4"),
		("fMotionBlurFurShutterSpeed", "float"),

	])


#CBMhMaterialVfxTornadoLocal__disclosure : 5228.shdr.src
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


#CBContactShadowInfo : 5469.shdr.src
class CBContactShadowInfo(EPyCStruct):
	fields = OrderedDict([


		("fContactShadowLengthCoefs", "float4"),
		("fContactShadowOptimizeParams", "float3"),

		("align0", "ubyte[4]"),
		("fContactShadowDirection", "float3"),
		("bIsUseNoise", "bbool"),
		("bIsUseContactShadow", "bbool"),

	])


#CBMhMaterialNPCEditFaceLocal__disclosure : 5265.shdr.src
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


#CBDevelopColorPick : 5273.shdr.src
class CBDevelopColorPick(EPyCStruct):
	fields = OrderedDict([


		("mousePos", "uint2"),
		("gammaCorrect", "bbool"),

	])


#CBMhMaterialVfxSandFallLocal__disclosure : 5338.shdr.src
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


#CBMhMaterialSpeedTreeStdBlendSnowLocal__disclosure : 5395.shdr.src
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


#CBMhMaterialPLEditFaceLocal__disclosure : 5471.shdr.src
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


#CBWaterPick : 545.shdr.src
class CBWaterPick(EPyCStruct):
	fields = OrderedDict([


		("iWaterAddress", "uint2"),

	])


#CBMhMaterialEM044Local__disclosure : 5540.shdr.src
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


#CBMhMaterialPLHairLocal__disclosure : 5623.shdr.src
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


#CBMhMaterialArrayLocal__disclosure : 5735.shdr.src
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


#CBVignetting : 5742.shdr.src
class CBVignetting(EPyCStruct):
	fields = OrderedDict([


		("fOffset", "float"),
		("fPow", "float"),
		("fEllipticity", "float"),

		("align0", "ubyte[4]"),
		("fColor", "float3"),

	])


#CBMhEmissiveFog__disclosure : 5840.shdr.src
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


#CBMhMaterialSpeedTreeStdLocal__disclosure : 7063.shdr.src
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


#CBMhMaterialNPCSkinLocal__disclosure : 5940.shdr.src
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


#CBMhMaterialScrWaterLocal__disclosure : 6557.shdr.src
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


#CBMhMaterialEM106Local__disclosure : 658.shdr.src
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


#CBMhSky2SimpleVS : 6013.shdr.src
class CBMhSky2SimpleVS(EPyCStruct):
	fields = OrderedDict([


		("fSkyWorld", "float3x4"),

	])


#CBPartialColor : 6016.shdr.src
class CBPartialColor(EPyCStruct):
	fields = OrderedDict([


		("color_matrix", "float4x4"),
		("compensate", "float"),

	])


#CBToneMappingSdrSim : 6067.shdr.src
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


#CB_CombinedFilter_ImagePlane : 9499.shdr.src
class CB_CombinedFilter_ImagePlane(EPyCStruct):
	fields = OrderedDict([


		("iBlendType", "uint"),

		("align0", "ubyte[12]"),
		("fUVTransform", "float4x4"),
		("fPlaneColor", "float4"),

	])


#CB_CombinedFilter : 9499.shdr.src
class CB_CombinedFilter(EPyCStruct):
	fields = OrderedDict([


		("bEnableFXAA", "bbool"),
		("bEnableTemporalAA", "bbool"),
		("bEnableColorCorrect", "bbool"),
		("bEnableImagePlane", "bbool"),

	])


#CB_CombinedFilter_ColorCorrect : 9499.shdr.src
class CB_CombinedFilter_ColorCorrect(EPyCStruct):
	fields = OrderedDict([


		("fDepthNear", "float"),
		("fDepthFar", "float"),
		("bHdrExtrapolation", "bbool"),
		("fHdrIntensityRangeInv", "float"),

	])


#cbHBAO : 9669.shdr.src
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


#CBMhMaterialFlagWaveBlendLocal__disclosure : 6261.shdr.src
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


#CBMhMaterial_EM105_EVCLocal__disclosure : 6329.shdr.src
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


#cbHDAO : 9168.shdr.src
class cbHDAO(EPyCStruct):
	fields = OrderedDict([


		("HDAORejectRadius", "float"),
		("HDAOAcceptRadius", "float"),
		("HDAOIntensity", "float"),
		("HDAOAcceptAngle", "float"),
		("HDAONormalScale", "float"),
		("HDAOUseNormal", "int"),

	])


#CBMhMaterialScrIceBlendNoFurLocal__disclosure : 6425.shdr.src
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


#CBMhMaterialEM117Local__disclosure : 6486.shdr.src
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


#CBMhMaterialSKM001Local__disclosure : 6676.shdr.src
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


#CBMhMaterialEM036Local__disclosure : 6752.shdr.src
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


#CBConstant : 6769.shdr.src
class CBConstant(EPyCStruct):
	fields = OrderedDict([


		("iUserConstant", "uint"),

	])


#CBMhMaterialTMG001Local__disclosure : 6836.shdr.src
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


#CBMhMaterialNikuLocal__disclosure : 6889.shdr.src
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


#CBMhMaterialVfxFakeInnerLocal__disclosure : 766.shdr.src
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


#CBMhMaterialEM102Local__disclosure : 6964.shdr.src
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


#CBMhMaterialPLLocal__disclosure : 7169.shdr.src
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


#CBMhSkyPS : 7419.shdr.src
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


#CBMhMaterialScrIceBlendLocal__disclosure : 7290.shdr.src
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


#CBMhSky2SimpleGBuffer : 7292.shdr.src
class CBMhSky2SimpleGBuffer(EPyCStruct):
	fields = OrderedDict([


		("iSkyGBufferId", "uint"),

	])


#CBMhMaterialIridescentBlendLocal__disclosure : 7417.shdr.src
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


#CBMhMaterialEM057Local__disclosure : 7517.shdr.src
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


#CBDepthColor : 7531.shdr.src
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


#CBMhMaterialStdBlendLocal__disclosure : 7603.shdr.src
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


#CBMhMaterialEM111Local__disclosure : 7695.shdr.src
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


#CBMhMaterialUberLocal__disclosure : 7827.shdr.src
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


#CBMhMaterialFurLocal__disclosure : 886.shdr.src
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


#CBMhMaterialVfxDistDispLocal__disclosure : 7927.shdr.src
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


#CBMhMaterialEMLocal__disclosure : 7993.shdr.src
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


#CBMhMaterialSpeedTreeStdIceLocal__disclosure : 8224.shdr.src
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


#CBMhMaterialNPCLocal__disclosure : 8309.shdr.src
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


#CBResample : 8320.shdr.src
class CBResample(EPyCStruct):
	fields = OrderedDict([


		("fResampleScreenSize", "float2"),
		("fResampleScale", "float2"),

	])


#CBMhMaterialEM124Local__disclosure : 8387.shdr.src
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


#CBSky : 8399.shdr.src
class CBSky(EPyCStruct):
	fields = OrderedDict([


		("fSunSolidAngle", "float"),

	])


#CBMhMaterialTestLocal__disclosure : 8491.shdr.src
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


#CBMhMaterialFurnitureLocal__disclosure : 8572.shdr.src
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


#CBMhMaterialBurnLocal__disclosure : 8709.shdr.src
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


#SeaDisplacement : 8711.shdr.src
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


#CBMhMaterialSpeedTreeStdSnowLocal__disclosure : 8772.shdr.src
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


#CBTubeLight : 8794.shdr.src
class CBTubeLight(EPyCStruct):
	fields = OrderedDict([


		("iTubeLightCount", "uint"),

	])


#CBMhMaterialFakeRefractionLocal__disclosure : 8844.shdr.src
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


#CBImageEvaluator : 8880.shdr.src
class CBImageEvaluator(EPyCStruct):
	fields = OrderedDict([


		("fCentralRegion", "float3"),

	])


#CBMhMaterialEM118Local__disclosure : 8948.shdr.src
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


#CBMhMaterialEM080Local__disclosure : 9014.shdr.src
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


#CBModelChain : 9081.shdr.src
class CBModelChain(EPyCStruct):
	fields = OrderedDict([


		("fStartFrame", "float"),
		("fMotionKeyAlpha", "float"),
		("fStartRotation", "float"),
		("fNextModelFrame", "float"),
		("fNextModelRotation", "float"),
		("iMotionDataNum", "int"),

	])


#CBMhMaterialPLEyeLocal__disclosure : 940.shdr.src
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


#CBLayoutCache : 9107.shdr.src
class CBLayoutCache(EPyCStruct):
	fields = OrderedDict([


		("iEmitterID", "uint"),
		("iParticleStride", "uint"),
		("iParticleMaxNum", "uint"),
		("iOutputOffset", "uint"),
		("iOutputFlags", "uint"),

	])


#CBRadialBlurFilter : 9147.shdr.src
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


#CBRadialBlurFunction : 9147.shdr.src
class CBRadialBlurFunction(EPyCStruct):
	fields = OrderedDict([


		("iRadialFilterSampleColorScale", "int"),
		("iRadialFilterAlpha", "int"),
		("iRadialBlurWidth", "int"),
		("iRadialBlurAlpha", "int"),

	])


#CBPickObject : 9151.shdr.src
class CBPickObject(EPyCStruct):
	fields = OrderedDict([


		("fPickObjectColor", "float4"),

	])


#CBMhMaterialVfxAuroraLocal__disclosure : 9239.shdr.src
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


#CBMhMaterialVfxIceLocal__disclosure : 9357.shdr.src
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


#CBMhMaterialFlagWaveLocal__disclosure : 9457.shdr.src
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


#CBFXAAParam : 9890.shdr.src
class CBFXAAParam(EPyCStruct):
	fields = OrderedDict([


		("fFXAAQualitySubpix", "float"),
		("fFXAAQualityEdgeThreshold", "float"),
		("fFXAAQualityEdgeThresholdMin", "float"),

		("align0", "ubyte[4]"),
		("fFXAATexOnePitch", "float2"),

	])


#CBSystemGamma : 9522.shdr.src
class CBSystemGamma(EPyCStruct):
	fields = OrderedDict([


		("fSystemCopyGamma", "float"),

	])


#CBHermiteCurveRGB : 9580.shdr.src
class CBHermiteCurveRGB(EPyCStruct):
	fields = OrderedDict([


		("fHermiteParamR", "float2[64]"),

		("align0", "ubyte[8]"),
		("fHermiteParamG", "float2[64]"),

		("align1", "ubyte[8]"),
		("fHermiteParamB", "float2[64]"),

	])


#CBMhMaterialScrIceLocal__disclosure : 9666.shdr.src
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


#CBMhMaterialBTK001Local__disclosure : 9749.shdr.src
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


#CBMhMaterialFakeSphereLocal__disclosure : 9789.shdr.src
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


#CBMhMaterialEM080_01Local__disclosure : 9879.shdr.src
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


#CBMhMaterialUberIceLocal__disclosure : 9974.shdr.src
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


#CBColorCorrectToneCurve : 9993.shdr.src
class CBColorCorrectToneCurve(EPyCStruct):
	fields = OrderedDict([


		("fToneColor", "float4[256]"),

	])


shaderListing = 	{"CBViewProjection":CBViewProjection,
"CBScreen":CBScreen,
"CBLightParameters":CBLightParameters,
"CBLightParameters_LightParameter":CBLightParameters_LightParameter,
"CBVRCommon":CBVRCommon,
"CBVRCompute":CBVRCompute,
"CBVRFilter":CBVRFilter,
"CBModel":CBModel,
"CBROPTest":CBROPTest,
"CBUpdateBufferFromMeshData":CBUpdateBufferFromMeshData,
"CBMhMaterialOZK001Local__disclosure":CBMhMaterialOZK001Local__disclosure,
"CBMhMaterialEM032Local__disclosure":CBMhMaterialEM032Local__disclosure,
"CBLight":CBLight,
"CBInstancing":CBInstancing,
"CBBokehCOCSettings":CBBokehCOCSettings,
"CBLightProbes":CBLightProbes,
"CBLGTPRBDebug":CBLGTPRBDebug,
"CBPrimSystem":CBPrimSystem,
"CBPrimitive":CBPrimitive,
"CBMhMaterialVfxFloodLocal__disclosure":CBMhMaterialVfxFloodLocal__disclosure,
"CBMaterialCommon__disclosure":CBMaterialCommon__disclosure,
"CBFog":CBFog,
"CBRenderFrame":CBRenderFrame,
"CBTestLight":CBTestLight,
"CBPick":CBPick,
"CBMhMaterialEMGlobal":CBMhMaterialEMGlobal,
"CBMotionBlurReconion":CBMotionBlurReconion,
"CBVRVolumeParams":CBVRVolumeParams,
"CBVRVolumeParams_VolumeParam":CBVRVolumeParams_VolumeParam,
"CBVRVolumeParams_Constant":CBVRVolumeParams_Constant,
"CBVRVolumeParams_Cuboid":CBVRVolumeParams_Cuboid,
"CBVRVolumeParams_Spherical":CBVRVolumeParams_Spherical,
"CBVRVolumeParams_Spotlight":CBVRVolumeParams_Spotlight,
"CBGaussian":CBGaussian,
"CBMhSky2SimplePS":CBMhSky2SimplePS,
"CBSystemColor":CBSystemColor,
"CBNewDOFFilter":CBNewDOFFilter,
"CBAmbientOcclusion":CBAmbientOcclusion,
"CB_TemporalAA2":CB_TemporalAA2,
"pix_clear_constants":pix_clear_constants,
"CBWaterCustomLight":CBWaterCustomLight,
"CBWaterMaterial":CBWaterMaterial,
"CBWaterCustom":CBWaterCustom,
"CBCubeCopy":CBCubeCopy,
"CBViewFrustum":CBViewFrustum,
"CBTest":CBTest,
"CBUpdateBufferFromMesh":CBUpdateBufferFromMesh,
"CBUpdateBufferFromMeshConditions2":CBUpdateBufferFromMeshConditions2,
"CBLuminance":CBLuminance,
"CBSHDiffuse":CBSHDiffuse,
"CBMhMaterialVfxWaveLocal__disclosure":CBMhMaterialVfxWaveLocal__disclosure,
"CBMhMaterialVfxWave":CBMhMaterialVfxWave,
"CB_PlantOnSurface":CB_PlantOnSurface,
"CBMhSkyGBuffer":CBMhSkyGBuffer,
"CBPrimGpuOcclusionVoxelSystem":CBPrimGpuOcclusionVoxelSystem,
"CBSnowFieldMaterial":CBSnowFieldMaterial,
"CBConstantHaltonSequence":CBConstantHaltonSequence,
"CBCapsuleAO":CBCapsuleAO,
"CBCapsuleAOGeomParam":CBCapsuleAOGeomParam,
"CBCapsuleAOGeomParam_AOGeometryParam":CBCapsuleAOGeomParam_AOGeometryParam,
"CBMhMaterialFlowLavaLocal__disclosure":CBMhMaterialFlowLavaLocal__disclosure,
"CBSSLR":CBSSLR,
"CBMhMaterialVfxDebufBodyLocal__disclosure":CBMhMaterialVfxDebufBodyLocal__disclosure,
"CBLightShaft":CBLightShaft,
"CBMhSky2PS":CBMhSky2PS,
"CBPrimBufferDescription":CBPrimBufferDescription,
"CBPrimitiveEx":CBPrimitiveEx,
"CBPrimitivePick":CBPrimitivePick,
"CBComputeSkinning":CBComputeSkinning,
"CBCubeBlend":CBCubeBlend,
"CBWaterWave":CBWaterWave,
"CBSystemSnow":CBSystemSnow,
"CBSnowField4Geometry":CBSnowField4Geometry,
"CBWorkaround":CBWorkaround,
"CBSnowField2Material":CBSnowField2Material,
"CBMhMaterialVfxDistDispWLocal__disclosure":CBMhMaterialVfxDistDispWLocal__disclosure,
"CBBloom":CBBloom,
"CBFilter":CBFilter,
"CBGUIGlobal":CBGUIGlobal,
"CBGUIGBuffer":CBGUIGBuffer,
"CBWaterModel":CBWaterModel,
"CBMhMaterialEM105Local__disclosure":CBMhMaterialEM105Local__disclosure,
"CBSystem":CBSystem,
"CBVRGaussian":CBVRGaussian,
"CB_DL":CB_DL,
"CBSnowField3Geometry":CBSnowField3Geometry,
"CBShapeMesh":CBShapeMesh,
"CBNormalRecalc":CBNormalRecalc,
"CBMhSky2Sun":CBMhSky2Sun,
"CBAmbientOccluder":CBAmbientOccluder,
"CBMhMaterialEMSLocal__disclosure":CBMhMaterialEMSLocal__disclosure,
"CBMhMaterialGlobal":CBMhMaterialGlobal,
"CBLUTBlending":CBLUTBlending,
"CBVRRecompute":CBVRRecompute,
"CBMhMaterialStdLocal__disclosure":CBMhMaterialStdLocal__disclosure,
"CBDOFFilter":CBDOFFilter,
"CBImagePlane":CBImagePlane,
"CBImagePlane2":CBImagePlane2,
"CBHazeFilter":CBHazeFilter,
"CBMhMaterialVfxVATDistLocal__disclosure":CBMhMaterialVfxVATDistLocal__disclosure,
"CBBokehComposite":CBBokehComposite,
"CBDecal":CBDecal,
"CBMhMaterialFakeLensLocal__disclosure":CBMhMaterialFakeLensLocal__disclosure,
"CBFilter2":CBFilter2,
"CBMhMaterialVfxDispWaveLocal__disclosure":CBMhMaterialVfxDispWaveLocal__disclosure,
"CBMhMaterialFlowDirLocal__disclosure":CBMhMaterialFlowDirLocal__disclosure,
"CBCreateMipmap":CBCreateMipmap,
"CBWater":CBWater,
"CBMhMaterialEM103Local__disclosure":CBMhMaterialEM103Local__disclosure,
"CBPrimGpuSystem":CBPrimGpuSystem,
"CBVR_Debug":CBVR_Debug,
"CBBitonicSort":CBBitonicSort,
"CBTSAO":CBTSAO,
"CBMhMaterialDynamicSnow__disclosure":CBMhMaterialDynamicSnow__disclosure,
"CBGodRaysFilter":CBGodRaysFilter,
"CBBloomSample":CBBloomSample,
"CBMhDecal":CBMhDecal,
"CBMhDecalSM":CBMhDecalSM,
"CBDebug":CBDebug,
"CBMhSky2VS":CBMhSky2VS,
"CBMhMaterialEM100_01Local__disclosure":CBMhMaterialEM100_01Local__disclosure,
"CBGodRaysConfiguration":CBGodRaysConfiguration,
"CBSSSSS":CBSSSSS,
"CBSSSSS_Profile":CBSSSSS_Profile,
"CBNewDOFFilter2":CBNewDOFFilter2,
"CBMaterialDebug":CBMaterialDebug,
"CBAtmosphere":CBAtmosphere,
"CBPrimitiveMetaDataOcclusion":CBPrimitiveMetaDataOcclusion,
"CBSparkleParam":CBSparkleParam,
"CBDevelopFlags":CBDevelopFlags,
"CBMhMaterialEM100Local__disclosure":CBMhMaterialEM100Local__disclosure,
"CBMhMaterialLandscapeLocal__disclosure":CBMhMaterialLandscapeLocal__disclosure,
"CBLightShaft_LightParam":CBLightShaft_LightParam,
"CBMhMaterialLandscapeFlowLocal__disclosure":CBMhMaterialLandscapeFlowLocal__disclosure,
"CBHermiteCurve":CBHermiteCurve,
"CBErrorUnit":CBErrorUnit,
"CBSnowFieldBake":CBSnowFieldBake,
"CBHeightToNormal":CBHeightToNormal,
"CBColorCorrectCube":CBColorCorrectCube,
"CBPrimCopyState":CBPrimCopyState,
"CBColorCorrect":CBColorCorrect,
"CBMhMaterialEM115Local__disclosure":CBMhMaterialEM115Local__disclosure,
"CBMhMaterialFakeEyeLocal__disclosure":CBMhMaterialFakeEyeLocal__disclosure,
"CBWaterWaveMaterial":CBWaterWaveMaterial,
"CBStarrySky":CBStarrySky,
"CBMhMaterialEM109Local__disclosure":CBMhMaterialEM109Local__disclosure,
"CBUpdateBufferFromMeshConditions":CBUpdateBufferFromMeshConditions,
"CBMhMaterialSZK001Local__disclosure":CBMhMaterialSZK001Local__disclosure,
"CBLGTPRBGen":CBLGTPRBGen,
"CBLUTMaking":CBLUTMaking,
"CBSnowPreProcess":CBSnowPreProcess,
"CBBloomSettings":CBBloomSettings,
"CBPrimitiveDebug":CBPrimitiveDebug,
"CBWaterDebug":CBWaterDebug,
"CBSnowField2Debug":CBSnowField2Debug,
"CBMaterialSnow__disclosure":CBMaterialSnow__disclosure,
"CBGUIDevelop":CBGUIDevelop,
"CBToneMapping":CBToneMapping,
"CB_TemporalAA":CB_TemporalAA,
"CBMhMaterialNPCEyeLocal__disclosure":CBMhMaterialNPCEyeLocal__disclosure,
"CBSpeedTreeLocalWind":CBSpeedTreeLocalWind,
"CBSpeedTreeLocalWind_SpeedTreeLocalWind":CBSpeedTreeLocalWind_SpeedTreeLocalWind,
"CBGodRaysIterator":CBGodRaysIterator,
"CBCAS":CBCAS,
"CBSnowFieldGeometry":CBSnowFieldGeometry,
"CBSnowShoveler":CBSnowShoveler,
"CBSnowFall":CBSnowFall,
"CBMhMaterialEM002Local__disclosure":CBMhMaterialEM002Local__disclosure,
"CBMhMaterialNPCHairLocal__disclosure":CBMhMaterialNPCHairLocal__disclosure,
"CBBokehAutoFocus":CBBokehAutoFocus,
"CBTexturePosScaleFactor":CBTexturePosScaleFactor,
"CBMhMaterialSimpleLocal__disclosure":CBMhMaterialSimpleLocal__disclosure,
"CBMhMaterialPLSkinLocal__disclosure":CBMhMaterialPLSkinLocal__disclosure,
"CBSnowHeightPick":CBSnowHeightPick,
"CBNormalMerge":CBNormalMerge,
"CBMhMaterialStdBlendNoFurLocal__disclosure":CBMhMaterialStdBlendNoFurLocal__disclosure,
"CBDecalCommon":CBDecalCommon,
"CBGUINoiseAndFade":CBGUINoiseAndFade,
"CBMhMaterialEM063Local__disclosure":CBMhMaterialEM063Local__disclosure,
"CBMhSkyVS":CBMhSkyVS,
"CBMhSkyLpPS":CBMhSkyLpPS,
"CBSnowFieldPreDepth":CBSnowFieldPreDepth,
"CBSpeedTreeCollision__disclosure":CBSpeedTreeCollision__disclosure,
"CBSpeedTreePrimitiveInfo":CBSpeedTreePrimitiveInfo,
"CBSpeedTreeSystem":CBSpeedTreeSystem,
"CBMhMaterialSpeedTreeStdBlendLocal__disclosure":CBMhMaterialSpeedTreeStdBlendLocal__disclosure,
"CBSpeedTree":CBSpeedTree,
"CBSpeedTreeGlobalWind":CBSpeedTreeGlobalWind,
"CBSpeedTreeGlobalWind_SpeedTreeGlobalWind":CBSpeedTreeGlobalWind_SpeedTreeGlobalWind,
"CBSpeedTreeGlobalWindPF":CBSpeedTreeGlobalWindPF,
"CBSpeedTreeGlobalWindPF_SpeedTreeGlobalWind":CBSpeedTreeGlobalWindPF_SpeedTreeGlobalWind,
"CBSpeedTreeLocalWindPF":CBSpeedTreeLocalWindPF,
"CBSpeedTreeLocalWindPF_SpeedTreeLocalWind":CBSpeedTreeLocalWindPF_SpeedTreeLocalWind,
"CBGlobalIllumination":CBGlobalIllumination,
"CBMhMaterialEM024Local__disclosure":CBMhMaterialEM024Local__disclosure,
"CBMhMaterialVfxWaterLocal__disclosure":CBMhMaterialVfxWaterLocal__disclosure,
"CBMhMaterialIvyFloorLocal__disclosure":CBMhMaterialIvyFloorLocal__disclosure,
"CBMhMaterialIvyFloor":CBMhMaterialIvyFloor,
"CBGUIDistanceField":CBGUIDistanceField,
"CBMhMaterialEC021Local__disclosure":CBMhMaterialEC021Local__disclosure,
"CBMhMaterialSpeedTreeStdFurLocal__disclosure":CBMhMaterialSpeedTreeStdFurLocal__disclosure,
"CBCSClear":CBCSClear,
"CBGUIIcon":CBGUIIcon,
"CBMhMaterialSlantFloorLocal__disclosure":CBMhMaterialSlantFloorLocal__disclosure,
"CBMhMaterialSlantFloor":CBMhMaterialSlantFloor,
"CBMhSky2GBuffer":CBMhSky2GBuffer,
"CBLuminanceDebugDisp":CBLuminanceDebugDisp,
"CBOutline":CBOutline,
"CBMhMaterialEM125Local__disclosure":CBMhMaterialEM125Local__disclosure,
"CB_BGTexture":CB_BGTexture,
"CBMhMaterialFakeInnerEmitLocal__disclosure":CBMhMaterialFakeInnerEmitLocal__disclosure,
"CBBlink":CBBlink,
"CBMhMaterialEM011Local__disclosure":CBMhMaterialEM011Local__disclosure,
"CBMhMaterialNPCFaceLocal__disclosure":CBMhMaterialNPCFaceLocal__disclosure,
"CBMotionBlur":CBMotionBlur,
"CBMhMaterialVfxTornadoLocal__disclosure":CBMhMaterialVfxTornadoLocal__disclosure,
"CBContactShadowInfo":CBContactShadowInfo,
"CBMhMaterialNPCEditFaceLocal__disclosure":CBMhMaterialNPCEditFaceLocal__disclosure,
"CBDevelopColorPick":CBDevelopColorPick,
"CBMhMaterialVfxSandFallLocal__disclosure":CBMhMaterialVfxSandFallLocal__disclosure,
"CBMhMaterialSpeedTreeStdBlendSnowLocal__disclosure":CBMhMaterialSpeedTreeStdBlendSnowLocal__disclosure,
"CBMhMaterialPLEditFaceLocal__disclosure":CBMhMaterialPLEditFaceLocal__disclosure,
"CBWaterPick":CBWaterPick,
"CBMhMaterialEM044Local__disclosure":CBMhMaterialEM044Local__disclosure,
"CBMhMaterialPLHairLocal__disclosure":CBMhMaterialPLHairLocal__disclosure,
"CBMhMaterialArrayLocal__disclosure":CBMhMaterialArrayLocal__disclosure,
"CBVignetting":CBVignetting,
"CBMhEmissiveFog__disclosure":CBMhEmissiveFog__disclosure,
"CBMhMaterialSpeedTreeStdLocal__disclosure":CBMhMaterialSpeedTreeStdLocal__disclosure,
"CBMhMaterialNPCSkinLocal__disclosure":CBMhMaterialNPCSkinLocal__disclosure,
"CBMhMaterialScrWaterLocal__disclosure":CBMhMaterialScrWaterLocal__disclosure,
"CBMhMaterialEM106Local__disclosure":CBMhMaterialEM106Local__disclosure,
"CBMhSky2SimpleVS":CBMhSky2SimpleVS,
"CBPartialColor":CBPartialColor,
"CBToneMappingSdrSim":CBToneMappingSdrSim,
"CB_CombinedFilter_ImagePlane":CB_CombinedFilter_ImagePlane,
"CB_CombinedFilter":CB_CombinedFilter,
"CB_CombinedFilter_ColorCorrect":CB_CombinedFilter_ColorCorrect,
"cbHBAO":cbHBAO,
"CBMhMaterialFlagWaveBlendLocal__disclosure":CBMhMaterialFlagWaveBlendLocal__disclosure,
"CBMhMaterial_EM105_EVCLocal__disclosure":CBMhMaterial_EM105_EVCLocal__disclosure,
"cbHDAO":cbHDAO,
"CBMhMaterialScrIceBlendNoFurLocal__disclosure":CBMhMaterialScrIceBlendNoFurLocal__disclosure,
"CBMhMaterialEM117Local__disclosure":CBMhMaterialEM117Local__disclosure,
"CBMhMaterialSKM001Local__disclosure":CBMhMaterialSKM001Local__disclosure,
"CBMhMaterialEM036Local__disclosure":CBMhMaterialEM036Local__disclosure,
"CBConstant":CBConstant,
"CBMhMaterialTMG001Local__disclosure":CBMhMaterialTMG001Local__disclosure,
"CBMhMaterialNikuLocal__disclosure":CBMhMaterialNikuLocal__disclosure,
"CBMhMaterialVfxFakeInnerLocal__disclosure":CBMhMaterialVfxFakeInnerLocal__disclosure,
"CBMhMaterialEM102Local__disclosure":CBMhMaterialEM102Local__disclosure,
"CBMhMaterialPLLocal__disclosure":CBMhMaterialPLLocal__disclosure,
"CBMhSkyPS":CBMhSkyPS,
"CBMhMaterialScrIceBlendLocal__disclosure":CBMhMaterialScrIceBlendLocal__disclosure,
"CBMhSky2SimpleGBuffer":CBMhSky2SimpleGBuffer,
"CBMhMaterialIridescentBlendLocal__disclosure":CBMhMaterialIridescentBlendLocal__disclosure,
"CBMhMaterialEM057Local__disclosure":CBMhMaterialEM057Local__disclosure,
"CBDepthColor":CBDepthColor,
"CBMhMaterialStdBlendLocal__disclosure":CBMhMaterialStdBlendLocal__disclosure,
"CBMhMaterialEM111Local__disclosure":CBMhMaterialEM111Local__disclosure,
"CBMhMaterialUberLocal__disclosure":CBMhMaterialUberLocal__disclosure,
"CBMhMaterialFurLocal__disclosure":CBMhMaterialFurLocal__disclosure,
"CBMhMaterialVfxDistDispLocal__disclosure":CBMhMaterialVfxDistDispLocal__disclosure,
"CBMhMaterialEMLocal__disclosure":CBMhMaterialEMLocal__disclosure,
"CBMhMaterialSpeedTreeStdIceLocal__disclosure":CBMhMaterialSpeedTreeStdIceLocal__disclosure,
"CBMhMaterialNPCLocal__disclosure":CBMhMaterialNPCLocal__disclosure,
"CBResample":CBResample,
"CBMhMaterialEM124Local__disclosure":CBMhMaterialEM124Local__disclosure,
"CBSky":CBSky,
"CBMhMaterialTestLocal__disclosure":CBMhMaterialTestLocal__disclosure,
"CBMhMaterialFurnitureLocal__disclosure":CBMhMaterialFurnitureLocal__disclosure,
"CBMhMaterialBurnLocal__disclosure":CBMhMaterialBurnLocal__disclosure,
"SeaDisplacement":SeaDisplacement,
"CBMhMaterialSpeedTreeStdSnowLocal__disclosure":CBMhMaterialSpeedTreeStdSnowLocal__disclosure,
"CBTubeLight":CBTubeLight,
"CBMhMaterialFakeRefractionLocal__disclosure":CBMhMaterialFakeRefractionLocal__disclosure,
"CBImageEvaluator":CBImageEvaluator,
"CBMhMaterialEM118Local__disclosure":CBMhMaterialEM118Local__disclosure,
"CBMhMaterialEM080Local__disclosure":CBMhMaterialEM080Local__disclosure,
"CBModelChain":CBModelChain,
"CBMhMaterialPLEyeLocal__disclosure":CBMhMaterialPLEyeLocal__disclosure,
"CBLayoutCache":CBLayoutCache,
"CBRadialBlurFilter":CBRadialBlurFilter,
"CBRadialBlurFunction":CBRadialBlurFunction,
"CBPickObject":CBPickObject,
"CBMhMaterialVfxAuroraLocal__disclosure":CBMhMaterialVfxAuroraLocal__disclosure,
"CBMhMaterialVfxIceLocal__disclosure":CBMhMaterialVfxIceLocal__disclosure,
"CBMhMaterialFlagWaveLocal__disclosure":CBMhMaterialFlagWaveLocal__disclosure,
"CBFXAAParam":CBFXAAParam,
"CBSystemGamma":CBSystemGamma,
"CBHermiteCurveRGB":CBHermiteCurveRGB,
"CBMhMaterialScrIceLocal__disclosure":CBMhMaterialScrIceLocal__disclosure,
"CBMhMaterialBTK001Local__disclosure":CBMhMaterialBTK001Local__disclosure,
"CBMhMaterialFakeSphereLocal__disclosure":CBMhMaterialFakeSphereLocal__disclosure,
"CBMhMaterialEM080_01Local__disclosure":CBMhMaterialEM080_01Local__disclosure,
"CBMhMaterialUberIceLocal__disclosure":CBMhMaterialUberIceLocal__disclosure,
"CBColorCorrectToneCurve":CBColorCorrectToneCurve,}

generalhash =  lambda x:  CrcJamcrc.calc(x.encode())
shaderTranslation = {generalhash(key) & 0xFFFFF:shaderListing[key] for key in shaderListing}
