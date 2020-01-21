# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 18:20:27 2019

@author: AsteriskAmpersand
"""
#TODO - Missing:
#CBSpeedTreeLocalWindPF : 5123.shdr.src
#CBSpeedTreeGlobalWind : 5167.shdr.src
#CBLightParameters : 996.shdr.src
#CBSpeedTreeGlobalWindPF : 5123.shdr.src
#CBVRVolumeParams : 977.shdr.src
#CBSpeedTreeLocalWind : 5167.shdr.src

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
            
#CBViewFrustum : 6586.shdr.src
class CBViewFrustum  (EPyCStruct):
	fields = OrderedDict([
		("fViewFrustum", "float4[6]"),#
	])
#CBMhMaterialUberLocal__disclosure : 5483.shdr.src
class CBMhMaterialUberLocal__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fBaseMapFactor__uiColor", "float4"),#
		("fEmissiveMapFactor__uiColor", "float3"),#
		("fMetalic__uiUNorm", "float"),#
		("fRoughness__uiUNorm", "float"),#
		("fSpecular__uiUNorm", "float"),#
		("fSubSurfaceBlend__uiUNorm", "float"),#
		("iSubSurfaceProfile", "uint"),#
		("fTranslucency__uiUNorm", "float"),#
		("bBaseColorEmissive", "bbool"),#
		("fAnimEmitMin", "float"),#
		("fAnimEmitSpeed", "float"),#
		("bUseCMM", "bbool"),#
		("align0", "ubyte[12]"),#
		("fAddColorA__uiColor", "float4"),#
		("fAddColorB__uiColor", "float4"),#
		("fAddColorC__uiColor", "float4"),#
		("fAddColorD__uiColor", "float4"),#
		("fFurParam__uiUNorm", "float4"),#
		("fFurTile", "float"),#
		("fSecondaryEmitColor__uiColor", "float3"),#
		("fSecondaryEmit_Control", "float4"),#
		("fFilmThickness__uiUNorm", "float"),#
		("fFilmBlend__uiUNorm", "float"),#
		("align1", "ubyte[8]"),#
		("fEmissiveBlendColor__uiColor", "float3"),#
		("fEmissiveBlendColorBlend__uiUNorm", "float"),#
		("fEmissiveBlendRimParam", "float3"),#
		("fRefraction__uiSNorm", "float"),#
		("fRefractionRotation__uiSNorm", "float"),#
		("fVPushScale", "float"),#
		("fVPushWave", "float"),#
		("fVPushSpeed", "float"),#
		("bUseFlipUV", "bbool"),#
		("bUseEmitMask", "bbool"),#
		("bUseRoughColor", "bbool"),#
		("align2", "ubyte[4]"),#
		("fRoughMask__uiUNorm", "float2"),#
		("bUsePaint", "bbool"),#
		("align3", "ubyte[4]"),#
		("fPaintMapRC", "float2"),#
		("fPaintMapNum", "float"),#
		("align4", "ubyte[4]"),#
		("fPaintMapOffset__uiSNorm", "float4"),#
		("fPaintColor__uiColor", "float4"),#
		("fPaintRoughness__uiUNorm", "float"),#
		("fPaintMetal__uiUNorm", "float"),#
		("bUseOffset", "bbool"),#
		("fInnerOffsetScale", "float"),#
		("bUseFly", "bbool"),#
		("iWingNum", "uint"),#
	])
#CBToneMappingSdrSim : 4381.shdr.src
class CBToneMappingSdrSim  (EPyCStruct):
	fields = OrderedDict([
		("iToneMapType", "uint"),#
		("bLuminanceVersion", "bbool"),#
		("fShouldStr", "float"),#
		("fLinearStr", "float"),#
		("fIntermediate", "float"),#
		("fS1", "float"),#
		("fS2", "float"),#
		("fS3", "float"),#
		("fS4", "float"),#
		("iLUTSize", "uint"),#
		("bIsLinearToPQ", "bbool"),#
		("bIsPQToLinear", "bbool"),#
		("bEnableColorGrading", "bbool"),#
		("bEnableSdrSimulation", "bbool"),#
		("bEnableMaxLuminanceTest", "bbool"),#
	])
#CBWaterMaterial : 5488.shdr.src
class CBWaterMaterial  (EPyCStruct):
	fields = OrderedDict([
		("fReflectionViewProj", "float4x4"),#
		("fReflectionFactor", "float"),#
		("fCubemapBlendRate", "float"),#
		("fRefractionFactor", "float"),#
		("fRefactionIndex", "float"),#
		("fColExtinction", "float3"),#
		("align0", "ubyte[4]"),#
		("fColScatter", "float3"),#
		("fScatteringCoeff", "float"),#
		("fFresnelBias", "float"),#
		("normalATiling", "float3"),#
		("normalBTiling", "float3"),#
		("align1", "ubyte[4]"),#
		("normalAMoveDir", "float3"),#
		("align2", "ubyte[4]"),#
		("normalBMoveDir", "float3"),#
		("align3", "ubyte[4]"),#
		("materialTiling", "float2"),#
		("align4", "ubyte[8]"),#
		("materialColor", "float3"),#
		("fWaterDeltaTime", "float"),#
		("fDepthFadeInv", "float"),#
		("iLightGroup", "uint"),#
		("iFlags", "uint"),#
		("fMaxDepth", "float"),#
		("causticsTiling", "float3"),#
		("align5", "ubyte[4]"),#
		("causticsMoveDir", "float3"),#
		("fCausticsDensityLow", "float"),#
		("whitecapTiling", "float3"),#
		("align6", "ubyte[4]"),#
		("whitecapMoveDir", "float3"),#
		("fWhitecapRoughness", "float"),#
		("fWhitecapDepthThreshold", "float"),#
		("fWhitecapDepthFade", "float"),#
		("fWhitecapHeightWPosUnder", "float"),#
		("fWhitecapHeightWPosThreshold", "float"),#
		("fWhitecapHeightFade", "float"),#
		("fWhitecapHeightPower", "float"),#
	])
#CBMhMaterialVfxTornadoLocal__disclosure : 3738.shdr.src
class CBMhMaterialVfxTornadoLocal__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fBaseMapFactor__uiColor", "float4"),#
		("fEmissiveMapFactor__uiColor", "float3"),#
		("align0", "ubyte[4]"),#
		("fUVTransformA", "float4"),#
		("fUVTransformB", "float4"),#
		("fUVTransformC", "float4"),#
		("fVolumeBlend__uiSNorm", "float"),#
		("fVolumeBlendDistance", "float"),#
		("align1", "ubyte[8]"),#
		("fRGBchFactor_uiColor", "float3"),#
		("align2", "ubyte[4]"),#
		("fEmissiveRGBchFactor_uiColor", "float3"),#
		("fEmissivePow", "float"),#
		("fEmissiveGradationPow", "float"),#
		("fOpacityFactor", "float"),#
		("fOpacityPow", "float"),#
		("fVerticalOpacityPow", "float"),#
		("fVerticalOpacityPowInv", "float"),#
		("fNormalFactor__uiUNorm", "float"),#
		("fDispFactor", "float"),#
		("fFresnelPow", "float"),#
		("fFlowSpeed", "float"),#
		("fFlowStrength", "float"),#
		("fUVOffsetSpeed", "float"),#
		("align3", "ubyte[4]"),#
		("fUVOffsetSpeedFactorA", "float2"),#
		("fUVOffsetSpeedFactorB", "float2"),#
		("fUVOffsetSpeedFactorC", "float2"),#
		("fAngleFade", "float"),#
		("fTranslucency__uiUNorm", "float"),#
		("fTotalOpacity__uiUNorm", "float"),#
		("fMetalic__uiUNorm", "float"),#
		("fRoughness__uiUNorm", "float"),#
		("fSpecular__uiUNorm", "float"),#
		("fInnerOffsetScale", "float"),#
		("fVelocityAttn", "float"),#
		("bGBufferIdMaskEnable", "bbool"),#
		("iGBufferIdMask", "uint"),#
		("fNormalDecalBlend__uiUNorm", "float"),#
	])
#CBMhMaterialIvyFloorLocal__disclosure : 3226.shdr.src
class CBMhMaterialIvyFloorLocal__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fWaveLength", "float"),#
		("fSinkLength", "float"),#
		("fLocalWindWeight", "float"),#
	])
#CBDevelopColorPick : 3787.shdr.src
class CBDevelopColorPick  (EPyCStruct):
	fields = OrderedDict([
		("mousePos", "uint2"),#
		("gammaCorrect", "bbool"),#
	])
#CBPrimGpuSystem : 6105.shdr.src
class CBPrimGpuSystem  (EPyCStruct):
	fields = OrderedDict([
		("iEmitterCount", "uint"),#
		("iTotalSpawnCount", "uint"),#
		("iTotalParticleMax", "uint"),#
		("iResetUnusedIndexHead", "uint"),#
		("iResetUnusedIndexCount", "uint"),#
		("fMainCameraDir", "float3"),#
		("iGpuStateFlags", "uint"),#
		("iGpuUpdateCounter", "uint"),#
	])
#CBRadialBlurFunction : 6147.shdr.src
class CBRadialBlurFunction  (EPyCStruct):
	fields = OrderedDict([
		("iRadialFilterSampleColorScale", "int"),#
		("iRadialFilterAlpha", "int"),#
		("iRadialBlurWidth", "int"),#
		("iRadialBlurAlpha", "int"),#
	])
#CBMhMaterialNPCFaceLocal__disclosure : 3645.shdr.src
class CBMhMaterialNPCFaceLocal__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fBaseMapFactor__uiColor", "float4"),#
		("fEmissiveMapFactor__uiColor", "float3"),#
		("fMetalic__uiUNorm", "float"),#
		("fRoughness__uiUNorm", "float"),#
		("fSpecular__uiUNorm", "float"),#
		("fSubSurfaceBlend__uiUNorm", "float"),#
		("iSubSurfaceProfile", "uint"),#
		("fTranslucency__uiUNorm", "float"),#
		("bBaseColorEmissive", "bbool"),#
		("bBackFaceNormalFilp", "bbool"),#
		("fAnimEmitMin", "float"),#
		("fAnimEmitSpeed", "float"),#
		("fAddColorUV__uiUNorm", "float2"),#
		("align0", "ubyte[4]"),#
		("fAddNormalMaskA__uiUNorm", "float4"),#
		("fAddNormalMaskB__uiUNorm", "float4"),#
		("fAddNormalMaskC__uiUNorm", "float4"),#
		("fAddNormalMaskD__uiUNorm", "float4"),#
		("bUseSkin", "bbool"),#
		("fDetailNormalBlend__uiUNorm", "float"),#
		("align1", "ubyte[8]"),#
		("fUVTransformDetailNormal", "float4"),#
	])
#CBMhMaterialVfxWaveLocal__disclosure : 6653.shdr.src
class CBMhMaterialVfxWaveLocal__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fConstant", "float"),#
		("align0", "ubyte[12]"),#
		("fUVTransformA", "float4"),#
		("fUVTransformB", "float4"),#
		("fBaseMapFactor__uiColor", "float4"),#
		("fEmissiveMapFactor__uiColor", "float3"),#
		("align1", "ubyte[4]"),#
		("fEmissiveBlendColor__uiColor", "float3"),#
		("fEmissiveBlendColorBlend__uiUNorm", "float"),#
		("fDetailNormalBlend__uiUNorm", "float"),#
		("fSubSurfaceBlend__uiUNorm", "float"),#
		("fDisplacementLevel", "float"),#
		("fWriteSplash", "bbool"),#
		("fSplashAngle", "float"),#
		("align2", "ubyte[12]"),#
		("fSplashColor__uiColor", "float4"),#
		("fSplashLevel__uiUNorm", "float"),#
		("fSplashOffsetX", "float"),#
		("fWriteShadow", "bbool"),#
		("align3", "ubyte[4]"),#
		("fShadowColor__uiColor", "float4"),#
		("fShadowLevel__uiUNorm", "float"),#
		("fNoiseLength__uiUNorm", "float"),#
		("fNoiseDetail__uiUNorm", "float"),#
		("fSplashSpeed", "float"),#
	])
#CBMhMaterialNPCHairLocal__disclosure : 2675.shdr.src
class CBMhMaterialNPCHairLocal__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fBaseMapFactor__uiColor", "float4"),#
		("fEmissiveMapFactor__uiColor", "float3"),#
		("fMetalic__uiUNorm", "float"),#
		("fRoughness__uiUNorm", "float"),#
		("fSpecular__uiUNorm", "float"),#
		("fSubSurfaceBlend__uiUNorm", "float"),#
		("iSubSurfaceProfile", "uint"),#
		("fTranslucency__uiUNorm", "float"),#
		("bBaseColorEmissive", "bbool"),#
		("bBackFaceNormalFilp", "bbool"),#
		("fAnimEmitMin", "float"),#
		("fAnimEmitSpeed", "float"),#
		("align0", "ubyte[12]"),#
		("fPrimaryColor__uiColor", "float4"),#
		("fSecondaryColor__uiColor", "float4"),#
		("fPrimaryExpo__uiUNorm", "float"),#
		("fSecondaryExpo__uiUNorm", "float"),#
		("fPrimaryShift__uiSNorm", "float"),#
		("fSecondaryShift__uiSNorm", "float"),#
		("fShininess", "float"),#
		("fFakeLight__uiDirection", "float3"),#
		("fFurNMHeight", "float"),#
		("align1", "ubyte[12]"),#
		("fFurParam__uiUNorm", "float4"),#
		("fFurTile", "float"),#
		("align2", "ubyte[12]"),#
		("fVertexAO__uiColor", "float4"),#
		("fVColorNormalBlend__uiUNorm", "float"),#
		("fRimWidth__uiUNorm", "float"),#
		("fRimNormalBlend__uiUNorm", "float"),#
		("bUseRimTranslucency", "bbool"),#
		("bUseOffset", "bbool"),#
		("fInnerOffsetScale", "float"),#
		("fDetailNormalBlend__uiUNorm", "float"),#
		("align3", "ubyte[4]"),#
		("fUVTransformDetailNormal", "float4"),#
	])
#CBMhMaterialFakeLensLocal__disclosure : 1274.shdr.src
class CBMhMaterialFakeLensLocal__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fBaseMapFactor__uiColor", "float4"),#
		("fEmissiveMapFactor__uiColor", "float3"),#
		("fMetalic__uiUNorm", "float"),#
		("fRoughness__uiUNorm", "float"),#
		("fSpecular__uiUNorm", "float"),#
		("fSubSurfaceBlend__uiUNorm", "float"),#
		("iSubSurfaceProfile", "uint"),#
		("fDetailNormalBlend__uiUNorm", "float"),#
		("align0", "ubyte[12]"),#
		("fUVTransformA", "float4"),#
		("fUVTransformB", "float4"),#
		("fTranslucency__uiUNorm", "float"),#
		("fOffset_A__uiUNorm", "float"),#
		("fOffset_B__uiUNorm", "float"),#
		("align1", "ubyte[4]"),#
		("fCoating_A__uiColor", "float3"),#
		("align2", "ubyte[4]"),#
		("fCoating_B__uiColor", "float3"),#
		("align3", "ubyte[4]"),#
		("fCoating_C__uiColor", "float3"),#
		("align4", "ubyte[4]"),#
		("fCoating_D__uiColor", "float3"),#
		("fWakuIntensity__uiUNorm", "float"),#
		("fWakuSize__uiUNorm", "float"),#
	])
#CBGUIDevelop : 219.shdr.src
class CBGUIDevelop  (EPyCStruct):
	fields = OrderedDict([
		("fGUIOverlapDrawColor", "float3"),#
	])
#CBCubeBlend : 876.shdr.src
class CBCubeBlend  (EPyCStruct):
	fields = OrderedDict([
		("fCubeBlendRate", "float"),#
	])
#CBMhMaterialEMLocal__disclosure : 5647.shdr.src
class CBMhMaterialEMLocal__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fBaseMapFactor__uiColor", "float4"),#
		("fEmissiveMapFactor__uiColor", "float3"),#
		("fMetalic__uiUNorm", "float"),#
		("fRoughness__uiUNorm", "float"),#
		("fSpecular__uiUNorm", "float"),#
		("fSubSurfaceBlend__uiUNorm", "float"),#
		("iSubSurfaceProfile", "uint"),#
		("fTranslucency__uiUNorm", "float"),#
		("bBaseColorEmissive", "bbool"),#
		("fPaintUVTile", "float2"),#
		("fAddNormalBlend__uiUNorm", "float"),#
		("align0", "ubyte[12]"),#
		("fAddNormalMaskA__uiSNorm", "float4"),#
		("fAddNormalMaskB__uiSNorm", "float4"),#
		("fAddNormalMaskC__uiUNorm", "float"),#
		("fAddNormalMaskD__uiUNorm", "float"),#
		("bBackFaceShading", "bbool"),#
		("align1", "ubyte[4]"),#
		("fBackFaceColor__uiColor", "float4"),#
		("bBackFaceNormalFilp", "bbool"),#
		("fKizuColor__uiColor", "float3"),#
		("bLegendary", "bbool"),#
		("align2", "ubyte[12]"),#
		("fLegendColor__uiColor", "float4"),#
		("fLegendMetalMask__uiUNorm", "float2"),#
		("fLegendRoughness", "float"),#
		("align3", "ubyte[4]"),#
		("fLegendFilm__uiUNorm", "float2"),#
		("fLegendSSSMask__uiUNorm", "float"),#
		("fPartsMaskA__uiUNorm", "float"),#
		("fPartsMaskB__uiUNorm", "float"),#
		("fPartsMaskC__uiUNorm", "float"),#
		("fPartsMaskD__uiUNorm", "float"),#
		("fPartsMaskX__uiUNorm", "float"),#
		("fPartsMaskY__uiUNorm", "float"),#
		("fPartsMaskZ__uiUNorm", "float"),#
		("fPartsMaskW__uiUNorm", "float"),#
		("bUseOffset", "bbool"),#
		("fFlowDirDir__uiDirection", "float3"),#
		("align4", "ubyte[4]"),#
		("fFlowControl__uiUNorm", "float4"),#
		("fFlowTile", "float"),#
		("align5", "ubyte[12]"),#
		("fFlowColor__uiColor", "float4"),#
		("fFlowMatControl__uiUNorm", "float4"),#
		("fFilmThickness__uiUNorm", "float"),#
		("fFilmBlend__uiUNorm", "float"),#
		("fRefraction__uiUNorm", "float"),#
		("fRefractionBlend__uiUNorm", "float"),#
	])
#CBMaterialCommon__disclosure : 99.shdr.src
class CBMaterialCommon__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("bBypass", "bbool"),#
		("bDecalMask", "bbool"),#
		("bEmissive", "bbool"),#
		("iGBufferId", "uint"),#
		("iOutlineId", "uint"),#
	])
#CBGlobalIllumination : 4659.shdr.src
class CBGlobalIllumination  (EPyCStruct):
	fields = OrderedDict([
		("fSpecularIntensity", "float"),#
		("fSpecularTemporalBlendRate", "float"),#
		("fSpecularDifference", "float"),#
	])
#CBMhMaterialEM117Local__disclosure : 4584.shdr.src
class CBMhMaterialEM117Local__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fBaseMapFactor__uiColor", "float4"),#
		("fEmissiveMapFactor__uiColor", "float3"),#
		("fMetalic__uiUNorm", "float"),#
		("fRoughness__uiUNorm", "float"),#
		("fSpecular__uiUNorm", "float"),#
		("fSubSurfaceBlend__uiUNorm", "float"),#
		("iSubSurfaceProfile", "uint"),#
		("fTranslucency__uiUNorm", "float"),#
		("bBaseColorEmissive", "bbool"),#
		("fPaintUVTile", "float2"),#
		("fAddNormalBlend__uiUNorm", "float"),#
		("align0", "ubyte[12]"),#
		("fAddNormalMaskA__uiSNorm", "float4"),#
		("fAddNormalMaskB__uiSNorm", "float4"),#
		("fAddNormalMaskC__uiUNorm", "float"),#
		("fAddNormalMaskD__uiUNorm", "float"),#
		("bBackFaceShading", "bbool"),#
		("align1", "ubyte[4]"),#
		("fBackFaceColor__uiColor", "float4"),#
		("bBackFaceNormalFilp", "bbool"),#
		("fKizuColor__uiColor", "float3"),#
		("bLegendary", "bbool"),#
		("align2", "ubyte[12]"),#
		("fLegendColor__uiColor", "float4"),#
		("fLegendMetalMask__uiUNorm", "float2"),#
		("fLegendRoughness", "float"),#
		("align3", "ubyte[4]"),#
		("fLegendFilm__uiUNorm", "float2"),#
		("fLegendSSSMask__uiUNorm", "float"),#
		("fPartsMaskA__uiUNorm", "float"),#
		("fPartsMaskB__uiUNorm", "float"),#
		("fPartsMaskC__uiUNorm", "float"),#
		("fPartsMaskD__uiUNorm", "float"),#
		("fPartsMaskX__uiUNorm", "float"),#
		("fPartsMaskY__uiUNorm", "float"),#
		("fPartsMaskZ__uiUNorm", "float"),#
		("fPartsMaskW__uiUNorm", "float"),#
		("bUseOffset", "bbool"),#
		("fFlowDirDir__uiDirection", "float3"),#
		("align4", "ubyte[4]"),#
		("fFlowControl__uiUNorm", "float4"),#
		("fFlowTile", "float"),#
		("align5", "ubyte[12]"),#
		("fFlowColor__uiColor", "float4"),#
		("fFlowMatControl__uiUNorm", "float4"),#
		("fFilmThickness__uiUNorm", "float"),#
		("fFilmBlend__uiUNorm", "float"),#
		("fRefraction__uiUNorm", "float"),#
		("fRefractionBlend__uiUNorm", "float"),#
		("fDetailBlend__uiUNorm", "float4"),#
		("fDetailTile", "float4"),#
		("fDetailA_Color__uiColor", "float4"),#
		("fDetailB_Color__uiColor", "float4"),#
		("fDetailC_Color__uiColor", "float4"),#
		("fDetailD_Color__uiColor", "float4"),#
		("fDetail_Roughness__uiUNorm", "float4"),#
		("fDetail_Metal__uiUNorm", "float4"),#
	])
#CBMhMaterialPLLocal__disclosure : 5085.shdr.src
class CBMhMaterialPLLocal__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fBaseMapFactor__uiColor", "float4"),#
		("fEmissiveMapFactor__uiColor", "float3"),#
		("fMetalic__uiUNorm", "float"),#
		("fRoughness__uiUNorm", "float"),#
		("fSpecular__uiUNorm", "float"),#
		("fSubSurfaceBlend__uiUNorm", "float"),#
		("iSubSurfaceProfile", "uint"),#
		("fTranslucency__uiUNorm", "float"),#
		("bBaseColorEmissive", "bbool"),#
		("bBackFaceNormalFilp", "bbool"),#
		("fAnimEmitMin", "float"),#
		("fAnimEmitSpeed", "float"),#
		("bUseCMM", "bbool"),#
		("align0", "ubyte[8]"),#
		("fAddColorA__uiColor", "float4"),#
		("fAddColorB__uiColor", "float4"),#
		("fAddColorC__uiColor", "float4"),#
		("fAddColorD__uiColor", "float4"),#
		("fFurParam__uiUNorm", "float4"),#
		("fFurTile", "float"),#
		("fFilmThickness__uiUNorm", "float"),#
		("fFilmBlend__uiUNorm", "float"),#
		("align1", "ubyte[4]"),#
		("fEmissiveBlendColor__uiColor", "float3"),#
		("fEmissiveBlendColorBlend__uiUNorm", "float"),#
		("fEmissiveBlendRimParam", "float3"),#
		("fDetailNormalBlend__uiUNorm", "float"),#
		("fUVTransformDetailNormal", "float4"),#
	])
#CBSpeedTreePrimitiveInfo : 5718.shdr.src
class CBSpeedTreePrimitiveInfo  (EPyCStruct):
	fields = OrderedDict([
		("iPrimitiveInfo", "uint4"),#
	])
#CBMhMaterialEM100Local__disclosure : 1798.shdr.src
class CBMhMaterialEM100Local__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fBaseMapFactor__uiColor", "float4"),#
		("fEmissiveMapFactor__uiColor", "float3"),#
		("fMetalic__uiUNorm", "float"),#
		("fRoughness__uiUNorm", "float"),#
		("fSpecular__uiUNorm", "float"),#
		("fSubSurfaceBlend__uiUNorm", "float"),#
		("iSubSurfaceProfile", "uint"),#
		("fTranslucency__uiUNorm", "float"),#
		("bBaseColorEmissive", "bbool"),#
		("fPaintUVTile", "float2"),#
		("fAddNormalBlend__uiUNorm", "float"),#
		("align0", "ubyte[12]"),#
		("fAddNormalMaskA__uiSNorm", "float4"),#
		("fAddNormalMaskB__uiSNorm", "float4"),#
		("fAddNormalMaskC__uiUNorm", "float"),#
		("fAddNormalMaskD__uiUNorm", "float"),#
		("bBackFaceShading", "bbool"),#
		("align1", "ubyte[4]"),#
		("fBackFaceColor__uiColor", "float4"),#
		("bBackFaceNormalFilp", "bbool"),#
		("fKizuColor__uiColor", "float3"),#
		("bLegendary", "bbool"),#
		("align2", "ubyte[12]"),#
		("fLegendColor__uiColor", "float4"),#
		("fLegendMetalMask__uiUNorm", "float2"),#
		("fLegendRoughness", "float"),#
		("align3", "ubyte[4]"),#
		("fLegendFilm__uiUNorm", "float2"),#
		("fLegendSSSMask__uiUNorm", "float"),#
		("fPartsMaskA__uiUNorm", "float"),#
		("fPartsMaskB__uiUNorm", "float"),#
		("fPartsMaskC__uiUNorm", "float"),#
		("fPartsMaskD__uiUNorm", "float"),#
		("fPartsMaskX__uiUNorm", "float"),#
		("fPartsMaskY__uiUNorm", "float"),#
		("fPartsMaskZ__uiUNorm", "float"),#
		("fPartsMaskW__uiUNorm", "float"),#
		("bUseOffset", "bbool"),#
		("fFlowDirDir__uiDirection", "float3"),#
		("align4", "ubyte[4]"),#
		("fFlowControl__uiUNorm", "float4"),#
		("fFlowTile", "float"),#
		("align5", "ubyte[12]"),#
		("fFlowColor__uiColor", "float4"),#
		("fFlowMatControl__uiUNorm", "float4"),#
		("fMaskBlend__uiUNorm", "float4"),#
		("fMaskBlend_A__uiUNorm", "float2"),#
		("fMaskBlend_B__uiUNorm", "float2"),#
		("fFilmThickness__uiUNorm", "float"),#
		("fFilmBlend__uiUNorm", "float"),#
		("fRefraction__uiUNorm", "float"),#
		("fRefractionBlend__uiUNorm", "float"),#
		("fFurParam__uiUNorm", "float4"),#
		("fFurTile", "float"),#
		("bUseFlipUV", "bbool"),#
	])
#CBOutline : 5189.shdr.src
class CBOutline  (EPyCStruct):
	fields = OrderedDict([
		("fLineColor", "float4"),#
		("iTargetID", "uint"),#
		("iSampleCount", "uint"),#
		("iMarkerNum", "uint"),#
		("align0", "ubyte[4]"),#
		("fMarkerPosition", "float4[3]"),#
		("fRadius", "float"),#
		("fFadeStartLength", "float"),#
		("fBlinkSpeed", "float"),#
		("fBlinkMin", "float"),#
		("bDepthTest", "bbool"),#
	])
#SeaDisplacement : 5927.shdr.src
class SeaDisplacement  (EPyCStruct):
	fields = OrderedDict([
		("fWorldMat", "float4x4"),#
		("iVBStride", "uint"),#
		("iBaseVertexOffset", "uint"),#
		("iVertexCount", "uint"),#
		("iVBOffsetPosition", "uint"),#
		("iVBOffsetTexcoord", "uint"),#
		("fWorldScaleY", "float"),#
		("fSupposedVertexDistance", "float"),#
		("align0", "ubyte[4]"),#
		("fWindParam", "float2"),#
		("fNoiseDensity", "float"),#
		("fChoppyCoef", "float"),#
	])
#CBBitonicSort : 5650.shdr.src
class CBBitonicSort  (EPyCStruct):
	fields = OrderedDict([
		("iSortArrayLength", "uint"),#
		("iCompareFlipSize", "uint"),#
		("iCompareStride", "uint"),#
		("iCompareDir", "uint"),#
	])
#CBStarrySky : 5384.shdr.src
class CBStarrySky  (EPyCStruct):
	fields = OrderedDict([
		("fRotMatrix", "float4x4"),#
		("fSize", "float2"),#
		("fFactor", "float"),#
		("fIntensity", "float"),#
		("fScintillation", "float"),#
	])
#CBMhMaterialVfxWaterLocal__disclosure : 3117.shdr.src
class CBMhMaterialVfxWaterLocal__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fBaseMapFactor__uiColor", "float4"),#
		("fDistortionFactor__uiColor", "float3"),#
		("align0", "ubyte[4]"),#
		("fCubeMapFactor__uiColor", "float3"),#
		("fMetalic__uiUNorm", "float"),#
		("fRoughness__uiUNorm", "float"),#
		("VertexPow", "float"),#
		("fOpacityFactor", "float"),#
		("fVertexOpacityFactor", "float"),#
		("fNormalFactor__uiUNorm", "float"),#
		("align1", "ubyte[12]"),#
		("fUVTransformA", "float4"),#
		("fVolumeBlend__uiSNorm", "float"),#
		("bVertexColor", "bbool"),#
		("fSpecularFactor", "float"),#
		("fRaflectionAngle__uiSNorm", "float"),#
		("fDistortionAngle", "float"),#
		("fDistortion", "float"),#
		("fRimRate", "float"),#
		("fRimOpacityPow", "float"),#
		("fRimOpacityFactor", "float"),#
		("fTranslucency__uiUNorm", "float"),#
		("bSceneEnvMap", "bbool"),#
		("fDiffuseChroma__uiUNorm", "float"),#
		("fSpecularChroma__uiUNorm", "float"),#
		("fInnerOffsetScale", "float"),#
		("fVelocityAttn", "float"),#
		("fNormalDecalBlend__uiUNorm", "float"),#
	])
#CBPartialColor : 4359.shdr.src
class CBPartialColor  (EPyCStruct):
	fields = OrderedDict([
		("color_matrix", "float4x4"),#
		("compensate", "float"),#
	])
#CBMhMaterialFlowLavaLocal__disclosure : 6730.shdr.src
class CBMhMaterialFlowLavaLocal__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fBaseMapFactor__uiColor", "float4"),#
		("fEmissiveMapFactor__uiColor", "float3"),#
		("fMetalic__uiUNorm", "float"),#
		("fRoughness__uiUNorm", "float"),#
		("fSpecular__uiUNorm", "float"),#
		("fSubSurfaceBlend__uiUNorm", "float"),#
		("iSubSurfaceProfile", "uint"),#
		("fDetailNormalBlend__uiUNorm", "float"),#
		("align0", "ubyte[12]"),#
		("fUVTransformA", "float4"),#
		("fUVTransformB", "float4"),#
		("fTranslucency__uiUNorm", "float"),#
		("fEmissiveBlendColor__uiColor", "float3"),#
		("fEmissiveBlendColorBlend__uiUNorm", "float"),#
		("fEmissiveBlendRimParam", "float3"),#
		("fFlowDirDir__uiDirection", "float3"),#
		("fFlowDirUVPhaseShift__uiUNorm", "float"),#
		("bFlowDirLocalSpace", "bbool"),#
		("fFlowControl", "float"),#
		("fEmitControl__uiUNorm", "float2"),#
	])
#CBVRCompute : 996.shdr.src
class CBVRCompute  (EPyCStruct):
	fields = OrderedDict([
		("iCountOffset", "uint"),#
	])
#CBSSSSS_Profile : 1649.shdr.src
class CBSSSSS_Profile  (EPyCStruct):
	fields = OrderedDict([
		("fRGBBlurWeight", "float4[16]"),#
		("fBlurOffset", "float4[8]"),#
		("fBlurTargetDist", "float4"),#
	])
#CBConstant : 4787.shdr.src
class CBConstant  (EPyCStruct):
	fields = OrderedDict([
		("iUserConstant", "uint"),#
	])
#CBViewProjection : 999.shdr.src
class CBViewProjection  (EPyCStruct):
	fields = OrderedDict([
		("fViewProj", "float4x4"),#
		("fView", "float4x4"),#
		("fProj", "float4x4"),#
		("fViewI", "float4x4"),#
		("fProjI", "float4x4"),#
		("fViewProjI", "float4x4"),#
		("fCameraPos", "float3"),#
		("align0", "ubyte[4]"),#
		("fCameraDir", "float3"),#
		("align1", "ubyte[4]"),#
		("fZToLinear", "float3"),#
		("fCameraNearClip", "float"),#
		("fCameraFarClip", "float"),#
		("fCameraTargetDist", "float"),#
		("align2", "ubyte[8]"),#
		("fPassThrough", "float4"),#
		("fLODBasePos", "float3"),#
		("align3", "ubyte[4]"),#
		("fViewProjPF", "float4x4"),#
		("fViewProjIPF", "float4x4"),#
		("fViewPF", "float4x4"),#
		("fProjPF", "float4x4"),#
		("fViewProjIViewProjPF", "float4x4"),#
		("fNoJitterProj", "float4x4"),#
		("fNoJitterViewProj", "float4x4"),#
		("fNoJitterViewProjI", "float4x4"),#
		("fNoJitterViewProjIViewProjPF", "float4x4"),#
	])
#CBMhMaterialFlowDirLocal__disclosure : 1478.shdr.src
class CBMhMaterialFlowDirLocal__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fBaseMapFactor__uiColor", "float4"),#
		("fEmissiveMapFactor__uiColor", "float3"),#
		("fMetalic__uiUNorm", "float"),#
		("fRoughness__uiUNorm", "float"),#
		("fSpecular__uiUNorm", "float"),#
		("fSubSurfaceBlend__uiUNorm", "float"),#
		("iSubSurfaceProfile", "uint"),#
		("fDetailNormalBlend__uiUNorm", "float"),#
		("align0", "ubyte[12]"),#
		("fUVTransformA", "float4"),#
		("fUVTransformB", "float4"),#
		("fTranslucency__uiUNorm", "float"),#
		("fEmissiveBlendColor__uiColor", "float3"),#
		("fEmissiveBlendColorBlend__uiUNorm", "float"),#
		("fEmissiveBlendRimParam", "float3"),#
		("fFlowDirDir__uiDirection", "float3"),#
		("fFlowDirUVPhaseShift__uiUNorm", "float"),#
		("bFlowDirLocalSpace", "bbool"),#
		("fFlowDirFlowSpeed__uiUNorm", "float"),#
	])
#CBLGTPRBDebug : 5729.shdr.src
class CBLGTPRBDebug  (EPyCStruct):
	fields = OrderedDict([
		("fProbeSize", "float"),#
		("lineColor", "float3"),#
		("iProbeDebugType", "uint"),#
	])
#CBVRCommon : 997.shdr.src
class CBVRCommon  (EPyCStruct):
	fields = OrderedDict([
		("iNumVolumes", "uint"),#
		("fGIFactor", "float"),#
		("fGIFactorShadow", "float"),#
		("align0", "ubyte[4]"),#
		("froxelDim", "uint2"),#
		("checkerDim", "uint2"),#
		("froxelDimInv", "float2"),#
		("checkerDimInv", "float2"),#
		("froxelZMinMax", "float3"),#
		("align1", "ubyte[4]"),#
		("fOrdered3x3", "float[9]"),#
		("align2", "ubyte[12]"),#
		("fOrdered4x4", "float[16]"),#
		("align3", "ubyte[12]"),#
		("fOrdered8x8", "float[64]"),#
		("align4", "ubyte[12]"),#
		("haltonXY", "float2[8]"),#
		("fVRDeltaTime", "float"),#
		("iJitterType", "uint"),#
		("iFrameCount", "uint"),#
		("bAlphaDitherFarClip", "bbool"),#
	])
#CB_CombinedFilter_ImagePlane : 6309.shdr.src
class CB_CombinedFilter_ImagePlane  (EPyCStruct):
	fields = OrderedDict([
		("iBlendType", "uint"),#
		("align0", "ubyte[12]"),#
		("fUVTransform", "float4x4"),#
		("fPlaneColor", "float4"),#
	])
#CBFilter2 : 6308.shdr.src
class CBFilter2  (EPyCStruct):
	fields = OrderedDict([
		("fFilterUVMin", "float2"),#
		("fFilterUVMax", "float2"),#
		("fFilterSampleOffsets", "float[11]"),#
		("align0", "ubyte[12]"),#
		("fFilterSampleWeights", "float[11]"),#
		("fFilterThreshold", "float"),#
	])
#CBPrimSystem : 999.shdr.src
class CBPrimSystem  (EPyCStruct):
	fields = OrderedDict([
		("fPrimGammaCorrect", "float"),#
		("fPrimAlphaLowerLimit", "float"),#
		("fPrimGlobalLightReflectance", "float"),#
		("iPrimMainLightIndex", "int"),#
	])
#CBLuminance : 730.shdr.src
class CBLuminance  (EPyCStruct):
	fields = OrderedDict([
		("iView", "uint"),#
		("fKeyValue", "float"),#
		("bClearHistory", "bbool"),#
		("fLuminanceLogScale", "float"),#
		("fLuminanceLogBias", "float"),#
		("fLuminanceExpScale", "float"),#
		("fLuminanceExpBias", "float"),#
		("fWhiteRange", "float"),#
		("fExposureValue", "float"),#
		("fDarkSensitivity", "float"),#
		("fLightSensitivity", "float"),#
		("fDarkAdaptationLimit", "float"),#
		("fLightAdaptationLimit", "float"),#
	])
#CBMhMaterialPLEditFaceLocal__disclosure : 3907.shdr.src
class CBMhMaterialPLEditFaceLocal__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fBaseMapFactor__uiColor", "float4"),#
		("fEmissiveMapFactor__uiColor", "float3"),#
		("fMetalic__uiUNorm", "float"),#
		("fRoughness__uiUNorm", "float"),#
		("fSpecular__uiUNorm", "float"),#
		("fSubSurfaceBlend__uiUNorm", "float"),#
		("iSubSurfaceProfile", "uint"),#
		("fTranslucency__uiUNorm", "float"),#
		("bBaseColorEmissive", "bbool"),#
		("bBackFaceNormalFilp", "bbool"),#
		("fAnimEmitMin", "float"),#
		("fAnimEmitSpeed", "float"),#
		("fAddColorUV__uiUNorm", "float2"),#
		("align0", "ubyte[4]"),#
		("fAddNormalMaskA__uiUNorm", "float4"),#
		("fAddNormalMaskB__uiUNorm", "float4"),#
		("fAddNormalMaskC__uiUNorm", "float4"),#
		("fAddNormalMaskD__uiUNorm", "float4"),#
		("bUseSkin", "bbool"),#
		("fPaintMapRC", "float2"),#
		("fPaintMapNum", "float"),#
		("fPaintMapOffset__uiSNorm", "float4"),#
		("fPaintColor__uiColor", "float4"),#
		("fPaintRoughness__uiUNorm", "float"),#
		("fPaintMetal__uiUNorm", "float"),#
		("fPaintMapNumB", "float"),#
		("align1", "ubyte[4]"),#
		("fPaintMapOffsetB__uiSNorm", "float4"),#
		("fPaintColorB__uiColor", "float4"),#
		("fPaintRoughnessB__uiUNorm", "float"),#
		("fPaintMetalB__uiUNorm", "float"),#
		("fFaceNormalBlend__uiUNorm", "float2"),#
		("fMayuMapNum", "float"),#
		("fMayuMapOffset__uiSNorm", "float2"),#
		("align2", "ubyte[4]"),#
		("fMayuMapRC", "float2"),#
		("align3", "ubyte[8]"),#
		("fMayuColor__uiColor", "float4"),#
		("bPaintEmit", "bbool"),#
		("bPaintEmitB", "bbool"),#
		("fDetailNormalBlend__uiUNorm", "float"),#
		("align4", "ubyte[4]"),#
		("fUVTransformDetailNormal", "float4"),#
	])
#CBMhMaterialNPCEditFaceLocal__disclosure : 3782.shdr.src
class CBMhMaterialNPCEditFaceLocal__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fBaseMapFactor__uiColor", "float4"),#
		("fEmissiveMapFactor__uiColor", "float3"),#
		("fMetalic__uiUNorm", "float"),#
		("fRoughness__uiUNorm", "float"),#
		("fSpecular__uiUNorm", "float"),#
		("fSubSurfaceBlend__uiUNorm", "float"),#
		("iSubSurfaceProfile", "uint"),#
		("fTranslucency__uiUNorm", "float"),#
		("bBaseColorEmissive", "bbool"),#
		("bBackFaceNormalFilp", "bbool"),#
		("fAnimEmitMin", "float"),#
		("fAnimEmitSpeed", "float"),#
		("fAddColorUV__uiUNorm", "float2"),#
		("align0", "ubyte[4]"),#
		("fAddNormalMaskA__uiUNorm", "float4"),#
		("fAddNormalMaskB__uiUNorm", "float4"),#
		("fAddNormalMaskC__uiUNorm", "float4"),#
		("fAddNormalMaskD__uiUNorm", "float4"),#
		("bUseSkin", "bbool"),#
		("fPaintMapRC", "float2"),#
		("fPaintMapNum", "float"),#
		("fPaintMapOffset__uiSNorm", "float4"),#
		("fPaintColor__uiColor", "float4"),#
		("fPaintRoughness__uiUNorm", "float"),#
		("fPaintMetal__uiUNorm", "float"),#
		("fPaintMapNumB", "float"),#
		("align1", "ubyte[4]"),#
		("fPaintMapOffsetB__uiSNorm", "float4"),#
		("fPaintColorB__uiColor", "float4"),#
		("fPaintRoughnessB__uiUNorm", "float"),#
		("fPaintMetalB__uiUNorm", "float"),#
		("fFaceNormalBlend__uiUNorm", "float2"),#
		("fMayuMapNum", "float"),#
		("fMayuMapOffset__uiSNorm", "float2"),#
		("align2", "ubyte[4]"),#
		("fMayuMapRC", "float2"),#
		("align3", "ubyte[8]"),#
		("fMayuColor__uiColor", "float4"),#
		("bPaintEmit", "bbool"),#
		("bPaintEmitB", "bbool"),#
		("fDetailNormalBlend__uiUNorm", "float"),#
		("align4", "ubyte[4]"),#
		("fUVTransformDetailNormal", "float4"),#
	])
#CBMhMaterialStdLocal__disclosure : 3218.shdr.src
class CBMhMaterialStdLocal__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fBaseMapFactor__uiColor", "float4"),#
		("fEmissiveMapFactor__uiColor", "float3"),#
		("fMetalic__uiUNorm", "float"),#
		("fRoughness__uiUNorm", "float"),#
		("fSpecular__uiUNorm", "float"),#
		("fSubSurfaceBlend__uiUNorm", "float"),#
		("iSubSurfaceProfile", "uint"),#
		("fDetailNormalBlend__uiUNorm", "float"),#
		("align0", "ubyte[12]"),#
		("fUVTransformA", "float4"),#
		("fUVTransformB", "float4"),#
		("fBaseMapModulation__uiUNorm", "float4"),#
		("fTranslucency__uiUNorm", "float"),#
		("fEmissiveBlendColor__uiColor", "float3"),#
		("fEmissiveBlendColorBlend__uiUNorm", "float"),#
		("fEmissiveBlendRimParam", "float3"),#
		("bSpecialBlend", "bbool"),#
		("fFurNormalBlend__uiUNorm", "float"),#
		("fFurHeight__uiUNorm", "float"),#
		("fFurMapBlend__uiUNorm", "float"),#
		("fFurEdgeBlend__uiUNorm", "float"),#
		("fFurTile", "float"),#
		("bFakeRefraction", "bbool"),#
		("fRefraction__uiUNorm", "float"),#
		("fWetBlendDir__uiDirection", "float3"),#
		("fWetBlendPlaneNormal__uiUNorm", "float"),#
		("fWetBlendOp", "float3"),#
		("bWetNormalBlend", "bbool"),#
		("fWetNormalBlendRange__uiUNorm", "float2"),#
	])
#CBGaussian : 960.shdr.src
class CBGaussian  (EPyCStruct):
	fields = OrderedDict([
		("fOffset0", "float4"),#
		("fOffset1", "float4"),#
		("fWeight0", "float4"),#
		("fWeight1", "float4"),#
		("fEdgeSharpness", "float"),#
	])
#CBRadialBlurFilter : 6147.shdr.src
class CBRadialBlurFilter  (EPyCStruct):
	fields = OrderedDict([
		("fRadialBlurCenter", "float2"),#
		("fRadialBlurStart", "float"),#
		("fRadialBlurWidth", "float"),#
		("fRadialBlurColor", "float4"),#
		("fRadialBlurThrethold", "float"),#
		("fRadialBlurWidthScale", "float"),#
		("fRadialBlurWidthOffset", "float"),#
		("fRadialBlurSampleCount", "uint"),#
		("fRadialBlurChromaticAberration", "float3"),#
		("fRadialBlurBlurScreenAlpha", "float"),#
		("fRadialBlurBlurCurve", "float[256]"),#
	])
#CBGodRaysConfiguration : 599.shdr.src
class CBGodRaysConfiguration  (EPyCStruct):
	fields = OrderedDict([
		("isUseOcclusionFactorFromTexture", "bbool"),#
		("isUseAlphaOcclusion", "bbool"),#
		("isUseScaleOcclusion", "bbool"),#
		("isGrayColor", "bbool"),#
		("iThreshold", "int"),#
	])
#CBNormalMerge : 2877.shdr.src
class CBNormalMerge  (EPyCStruct):
	fields = OrderedDict([
		("iNmSrcOffset", "uint"),#
		("iNmVertexCount", "uint"),#
		("iNmDestOffset", "uint"),#
		("iNmDestStride", "uint"),#
		("iNmRedirectOffset", "uint"),#
		("iNmBlendFlag", "bbool"),#
		("iNmStride", "uint"),#
		("iNmOffset", "uint"),#
		("iNmRateOffset", "uint"),#
	])
#CBMhMaterialEC021Local__disclosure : 3279.shdr.src
class CBMhMaterialEC021Local__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fBaseMapFactor__uiColor", "float4"),#
		("fEmissiveMapFactor__uiColor", "float3"),#
		("fMetalic__uiUNorm", "float"),#
		("fRoughness__uiUNorm", "float"),#
		("fSpecular__uiUNorm", "float"),#
		("fSubSurfaceBlend__uiUNorm", "float"),#
		("iSubSurfaceProfile", "uint"),#
		("fTranslucency__uiUNorm", "float"),#
		("align0", "ubyte[12]"),#
		("fUVTransformA", "float4"),#
		("bUseColorMask", "bbool"),#
		("align1", "ubyte[12]"),#
		("fAddColorA__uiColor", "float4"),#
		("fAddColorB__uiColor", "float4"),#
		("fAddColorC__uiColor", "float4"),#
		("fAddColorD__uiColor", "float4"),#
		("fBaseMapMod__uiUNorm", "float4"),#
		("fBaseMapModLimitMax__uiUNorm", "float4"),#
		("fBaseMapModLimitMin__uiUNorm", "float4"),#
		("fEmissiveBlendColor__uiColor", "float3"),#
		("fEmissiveBlendColorBlend__uiUNorm", "float"),#
		("fEmissiveBlendRimParam", "float3"),#
		("fFilmThickness__uiUNorm", "float"),#
		("fFilmBlend__uiUNorm", "float"),#
		("bBaseColorEmissive", "bbool"),#
		("align2", "ubyte[8]"),#
		("fFurParam__uiUNorm", "float4"),#
		("fFurTile", "float"),#
		("fFinWave", "float"),#
		("fFinSpeed", "float"),#
		("align3", "ubyte[4]"),#
		("fFinColor__uiColor", "float3"),#
	])
#CBVRGaussian : 1003.shdr.src
class CBVRGaussian  (EPyCStruct):
	fields = OrderedDict([
		("fOffsets", "float4"),#
		("fWeights", "float[5]"),#
		("fEdgeSharpness", "float"),#
	])
#CBInstancing : 99.shdr.src
class CBInstancing  (EPyCStruct):
	fields = OrderedDict([
		("iInstanceIndex", "uint"),#
	])
#CBColorCorrectToneCurve : 6440.shdr.src
class CBColorCorrectToneCurve  (EPyCStruct):
	fields = OrderedDict([
		("fToneColor", "float4[256]"),#
	])
#CBMhMaterialLandscapeFlowLocal__disclosure : 1983.shdr.src
class CBMhMaterialLandscapeFlowLocal__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fBaseMapFactor__uiColor", "float4"),#
		("fEmissiveMapFactor__uiColor", "float3"),#
		("fMetalic__uiUNorm", "float"),#
		("fRoughness__uiUNorm", "float"),#
		("fSpecular__uiUNorm", "float"),#
		("fSubSurfaceBlend__uiUNorm", "float"),#
		("iSubSurfaceProfile", "uint"),#
		("fDetailNormalBlend__uiUNorm", "float"),#
		("align0", "ubyte[12]"),#
		("fUVTransformA", "float4"),#
		("fUVTransformB", "float4"),#
		("fTranslucency__uiUNorm", "float"),#
		("align1", "ubyte[12]"),#
		("fUVTransformC", "float4"),#
		("fUVTransformD", "float4"),#
		("fUVTransformE", "float4"),#
		("fParallaxFactor__uiUNorm", "float"),#
		("fParallaxMinSampleNum__uiUNorm", "float"),#
		("fParallaxMaxSampleNum__uiUNorm", "float"),#
		("fBlendHeightMin__uiUNorm", "float"),#
		("fBlendHeightMax__uiUNorm", "float"),#
		("fParallaxAttenDistanceBegin", "float"),#
		("fParallaxAttenDistanceEnd", "float"),#
		("fParallaxVertexOffset", "float"),#
		("bSpecialBlend", "bbool"),#
		("bWetNormalBlend", "bbool"),#
		("fWetNormalBlendRange__uiUNorm", "float2"),#
		("fFlowDirDir__uiDirection", "float3"),#
		("align2", "ubyte[4]"),#
		("fFlowDirUVPhaseShift__uiUNorm", "float2"),#
		("fFlowDirFlowSpeed__uiUNorm", "float"),#
		("bFlowDirVfxNormalBlend", "bbool"),#
	])
#CBMhMaterialEM103Local__disclosure : 1573.shdr.src
class CBMhMaterialEM103Local__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fBaseMapFactor__uiColor", "float4"),#
		("fEmissiveMapFactor__uiColor", "float3"),#
		("fMetalic__uiUNorm", "float"),#
		("fRoughness__uiUNorm", "float"),#
		("fSpecular__uiUNorm", "float"),#
		("fSubSurfaceBlend__uiUNorm", "float"),#
		("iSubSurfaceProfile", "uint"),#
		("fTranslucency__uiUNorm", "float"),#
		("bBaseColorEmissive", "bbool"),#
		("fPaintUVTile", "float2"),#
		("fAddNormalBlend__uiUNorm", "float"),#
		("align0", "ubyte[12]"),#
		("fAddNormalMaskA__uiSNorm", "float4"),#
		("fAddNormalMaskB__uiSNorm", "float4"),#
		("fAddNormalMaskC__uiUNorm", "float"),#
		("fAddNormalMaskD__uiUNorm", "float"),#
		("bBackFaceShading", "bbool"),#
		("align1", "ubyte[4]"),#
		("fBackFaceColor__uiColor", "float4"),#
		("bBackFaceNormalFilp", "bbool"),#
		("fKizuColor__uiColor", "float3"),#
		("bLegendary", "bbool"),#
		("align2", "ubyte[12]"),#
		("fLegendColor__uiColor", "float4"),#
		("fLegendMetalMask__uiUNorm", "float2"),#
		("fLegendRoughness", "float"),#
		("align3", "ubyte[4]"),#
		("fLegendFilm__uiUNorm", "float2"),#
		("fLegendSSSMask__uiUNorm", "float"),#
		("fPartsMaskA__uiUNorm", "float"),#
		("fPartsMaskB__uiUNorm", "float"),#
		("fPartsMaskC__uiUNorm", "float"),#
		("fPartsMaskD__uiUNorm", "float"),#
		("fPartsMaskX__uiUNorm", "float"),#
		("fPartsMaskY__uiUNorm", "float"),#
		("fPartsMaskZ__uiUNorm", "float"),#
		("fPartsMaskW__uiUNorm", "float"),#
		("bUseOffset", "bbool"),#
		("fFlowDirDir__uiDirection", "float3"),#
		("align4", "ubyte[4]"),#
		("fFlowControl__uiUNorm", "float4"),#
		("fFlowTile", "float"),#
		("align5", "ubyte[12]"),#
		("fFlowColor__uiColor", "float4"),#
		("fFlowMatControl__uiUNorm", "float4"),#
		("fFilmThickness__uiUNorm", "float"),#
		("fFilmBlend__uiUNorm", "float"),#
		("fRefraction__uiUNorm", "float"),#
		("fRefractionBlend__uiUNorm", "float"),#
		("fAlbedoBlend__uiUNorm", "float"),#
		("bPartsAlpha", "bbool"),#
		("align6", "ubyte[8]"),#
		("fBlendBaseMapFactor__uiColor", "float4"),#
		("fBlendMatFactor", "float4"),#
		("bUseBlendDisplace", "bbool"),#
		("fVAnimV__uiUNorm", "float"),#
		("fVAnimPosScale", "float"),#
		("bInvertX", "bbool"),#
	])
#CBFilter : 960.shdr.src
class CBFilter  (EPyCStruct):
	fields = OrderedDict([
		("fFilterRegion", "float4"),#
		("fFilterMipLevel", "float"),#
	])
#CBMhMaterialSpeedTreeStdBlendLocal__disclosure : 5722.shdr.src
class CBMhMaterialSpeedTreeStdBlendLocal__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fBaseMapFactor__uiColor", "float4"),#
		("fEmissiveMapFactor__uiColor", "float3"),#
		("fMetalic__uiUNorm", "float"),#
		("fRoughness__uiUNorm", "float"),#
		("fSpecular__uiUNorm", "float"),#
		("fSubSurfaceBlend__uiUNorm", "float"),#
		("iSubSurfaceProfile", "uint"),#
		("fDetailNormalBlend__uiUNorm", "float"),#
		("align0", "ubyte[12]"),#
		("fUVTransformA", "float4"),#
		("fUVTransformB", "float4"),#
		("fTranslucency__uiUNorm", "float"),#
		("align1", "ubyte[12]"),#
		("fBlendBaseMapFactor__uiColor", "float4"),#
		("fBlendEmissiveMapFactor__uiColor", "float3"),#
		("fBlendMetalic__uiUNorm", "float"),#
		("fBlendRoughness__uiUNorm", "float"),#
		("fBlendDetailNormalBlend__uiUNorm", "float"),#
		("fBlendSubSurfaceBlend__uiUNorm", "float"),#
		("fBlendRoughnessThreshold__uiUNorm", "float"),#
		("fBlendRoughnessFillValue__uiUNorm", "float"),#
		("align2", "ubyte[12]"),#
		("fBlendUVTransformA", "float4"),#
		("fBlendUVTransformB", "float4"),#
		("bUseUVSecondaryMtA", "bbool"),#
		("bUseUVSecondaryMtB", "bbool"),#
		("bUseUVSecondaryMtBM", "bbool"),#
		("bUseUVSecondaryDetailNMtA", "bbool"),#
		("bUseUVSecondaryDetailNMtB", "bbool"),#
		("bLightProbeEmissive", "bbool"),#
		("align3", "ubyte[8]"),#
		("fEmissiveBlendColor__uiColor", "float3"),#
		("fEmissiveBlendColorBlend__uiUNorm", "float"),#
		("fEmissiveBlendRimParam", "float3"),#
		("bSpecialBlend", "bbool"),#
		("bWetNormalBlend", "bbool"),#
		("fWetNormalBlendRange__uiUNorm", "float2"),#
	])
#CBSSSSS : 5840.shdr.src
class CBSSSSS  (EPyCStruct):
	fields = OrderedDict([
		("fBlurMaxDist", "float"),#
		("fBlurEdgeSharpness", "float"),#
		("iDiviserFactor", "uint"),#
	])
#CBRenderFrame : 99.shdr.src
class CBRenderFrame  (EPyCStruct):
	fields = OrderedDict([
		("iRenderFrame", "uint"),#
		("iTotalTime", "uint"),#
		("iTotalTimeEx", "uint"),#
		("fFPS", "float"),#
		("fDeltaTime", "float"),#
		("fSSAOEffect", "float"),#
		("bSSSEnable", "bbool"),#
		("bIsRenderingWater", "bbool"),#
		("fWaterDepthBias", "float"),#
		("iGpuMode", "uint"),#
		("fDitherSize", "float2"),#
		("bHdrOutput", "bbool"),#
		("fHdrOutputWhiteLevel", "float"),#
		("fHdrOutputGamutMappingRatio", "float"),#
	])
#CBMhSkyPS : 5169.shdr.src
class CBMhSkyPS  (EPyCStruct):
	fields = OrderedDict([
		("fSkyMode", "uint"),#
		("fEmissiveMapFactor", "float3"),#
		("fSkySunMapFactor", "float4"),#
		("fSkyStarrySkyMapFactor", "float4"),#
		("fSkyFlowDir", "float3"),#
		("fSkyUVPhaseShiftH", "float"),#
		("fSkyUVPhaseShiftV", "float"),#
		("fSkyBlend", "float"),#
		("fSkySunUVTransform", "float2"),#
		("fSkyFlowSpeed", "float"),#
		("fSkyFlowTime", "float"),#
		("align0", "ubyte[8]"),#
		("fSkyWaterReflectionFactor", "float3"),#
		("bSkyIsRenderingWater", "bbool"),#
		("iSkyAddress", "uint2"),#
	])
#CBSystem : 994.shdr.src
class CBSystem  (EPyCStruct):
	fields = OrderedDict([
		("iRegion", "uint4"),#
		("fSourceMipLevel", "float"),#
		("fGammaCorrect", "float"),#
		("fGammaCorrectEx", "float"),#
		("iDisplayColorSpace", "uint"),#
	])
#CBPick : 999.shdr.src
class CBPick  (EPyCStruct):
	fields = OrderedDict([
		("iPickPoint", "uint2"),#
	])
#CBSky : 5831.shdr.src
class CBSky  (EPyCStruct):
	fields = OrderedDict([
		("fSunSolidAngle", "float"),#
	])
#CBGUIGlobal : 965.shdr.src
class CBGUIGlobal  (EPyCStruct):
	fields = OrderedDict([
		("fGUIWMatrix", "float4x4"),#
		("fGUIWMatrixPF", "float4x4"),#
		("fGUIMatrix", "float4x4"),#
		("fGUIMatrixPF", "float4x4"),#
		("fGUIStaticColor", "float4"),#
		("fGUIColorScale", "float4"),#
		("fGUIAmbientColor", "float4"),#
		("fGUISaturationParam", "float4"),#
		("fGUIAlphaMaskRect", "float4"),#
		("fGUIFontFilter", "float4"),#
		("fGUIUVClamp", "float4"),#
		("fGUIInvTextureSize", "float2"),#
		("fGUIInvTextureSize2", "float2"),#
		("fGUIZBias", "float"),#
		("iGUIShaderState", "uint"),#
	])
#CBLUTMaking : 3361.shdr.src
class CBLUTMaking  (EPyCStruct):
	fields = OrderedDict([
		("iLUTSize", "uint"),#
		("iMaxWidth", "uint"),#
		("fMaxLuminance", "float"),#
		("bIsPQToLinear", "bbool"),#
	])
#CBNormalRecalc : 1017.shdr.src
class CBNormalRecalc  (EPyCStruct):
	fields = OrderedDict([
		("iIBOffset", "uint"),#
		("iSkinningVertexBase", "uint"),#
		("iTriangleCount", "uint"),#
		("iVertexOffset", "uint"),#
		("iRedirectOffset", "uint"),#
	])
#CBConstantHaltonSequence : 6434.shdr.src
class CBConstantHaltonSequence  (EPyCStruct):
	fields = OrderedDict([
		("fHaltonSequence", "float4[64]"),#
	])

#CBGUIGBuffer : 965.shdr.src
class CBGUIGBuffer  (EPyCStruct):
	fields = OrderedDict([
		("iGUIGBufferLightChannel", "uint"),#
		("fGUIGBufferEmissiveColor", "float3"),#
		("fGUIGBufferParam", "float3"),#
	])
#CBPrimCopyState : 6422.shdr.src
class CBPrimCopyState  (EPyCStruct):
	fields = OrderedDict([
		("fNormalSlope", "float"),#
	])
#CBMhMaterialVfxWave : 6653.shdr.src
class CBMhMaterialVfxWave  (EPyCStruct):
	fields = OrderedDict([
		("iPointNum", "uint"),#
		("fViewTime", "float"),#
	])
#CBTestLight : 934.shdr.src
class CBTestLight  (EPyCStruct):
	fields = OrderedDict([
		("fTestLightDir", "float3"),#
		("align0", "ubyte[4]"),#
		("fTestLightColor", "float3"),#
	])
#CBSSLR : 2582.shdr.src
class CBSSLR  (EPyCStruct):
	fields = OrderedDict([
		("iSSLRReductionLevel", "int"),#
		("fSSLRFactor", "float"),#
		("fSSLRScale", "float"),#
		("iLoopCount", "uint"),#
		("fEliminateDepth", "float"),#
		("fDitherRadius", "float"),#
		("fImportanceBias", "float"),#
		("fMipScale", "float"),#
		("fMipBias", "float"),#
		("fAccurateThreshold", "float"),#
		("fEnvMapIntensity", "float"),#
		("fSSLRIntensity", "float"),#
	])
#CBGUIIcon : 3314.shdr.src
class CBGUIIcon  (EPyCStruct):
	fields = OrderedDict([
		("fGUINoiseColor", "float4"),#
		("fGUIEmissiveColor", "float4"),#
		("fGUISpecularColor", "float3"),#
		("align0", "ubyte[4]"),#
		("fGUIIconLightColor", "float3"),#
		("align1", "ubyte[4]"),#
		("fGUIIconLightDir", "float3"),#
	])
#CBResample : 5823.shdr.src
class CBResample  (EPyCStruct):
	fields = OrderedDict([
		("fResampleScreenSize", "float2"),#
		("fResampleScale", "float2"),#
	])
#CBMhDecal : 4085.shdr.src
class CBMhDecal  (EPyCStruct):
	fields = OrderedDict([
		("iDecalShadingMode", "int"),#
		("iDecalBlendMode", "int"),#
		("fDecalNormalBlendRate", "float"),#
		("fDecalAlphaTest", "bbool"),#
		("fDecalAlphaTestRef", "float"),#
		("fDecalEmissiveMapFactor", "float3"),#
		("fDecalTransparency", "float"),#
		("fDecalFlipUV", "bbool2"),#
		("align0", "ubyte[4]"),#
		("bDecalNormalMapFlip", "bbool3"),#
		("bDecalFlowMap", "bbool"),#
		("fDecalFlowTime", "float"),#
		("fDecalFlowStrength", "float"),#
		("align1", "ubyte[8]"),#
		("fDecalUVTransform", "float4"),#
		("fDecalAlphaCorrectionMinMax", "float2"),#
		("fDecalBlendFactorIntensity", "float"),#
		("iDecalAlphaMapChannel", "int"),#
		("fDecalEdgeFade", "float"),#
		("fDecalDistanceFadeRange", "float2"),#
		("bDecalEmissiveBoost", "bbool"),#
		("fDecalEmissiveBoostParam", "float2"),#
		("fDecalNormalBlendPow", "float"),#
		("bDecalNormalBC5", "bbool"),#
	])
#CBMhMaterialFakeRefractionLocal__disclosure : 5994.shdr.src
class CBMhMaterialFakeRefractionLocal__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fBaseMapFactor__uiColor", "float4"),#
		("fEmissiveMapFactor__uiColor", "float3"),#
		("fMetalic__uiUNorm", "float"),#
		("fRoughness__uiUNorm", "float"),#
		("fSpecular__uiUNorm", "float"),#
		("fSubSurfaceBlend__uiUNorm", "float"),#
		("iSubSurfaceProfile", "uint"),#
		("fDetailNormalBlend__uiUNorm", "float"),#
		("align0", "ubyte[12]"),#
		("fUVTransformA", "float4"),#
		("fUVTransformB", "float4"),#
		("fTranslucency__uiUNorm", "float"),#
		("fRefraction__uiUNorm", "float"),#
	])
#CBFog : 998.shdr.src
class CBFog  (EPyCStruct):
	fields = OrderedDict([
		("iFogType", "uint"),#
		("iDistanceFogFlags", "uint"),#
		("fFogStart", "float"),#
		("fFogInvRange", "float"),#
		("fFogDensity", "float"),#
		("fFogColor", "float3"),#
		("fFogHStart", "float"),#
		("fFogHColor", "float3"),#
		("fFogHInvRange", "float"),#
		("fFogHDensity", "float"),#
		("fFogHUVOffset", "float2"),#
		("fFogHUVScale", "float"),#
		("fFogHSlopeBias", "float"),#
		("fFogCurveIntensity", "float"),#
		("fMipFogBlend", "float"),#
		("fMipFogIntensity", "float"),#
		("fMipFogColor", "float3"),#
		("fSkyCenter", "float3"),#
		("fSkyRadius", "float"),#
		("fMipFogRotMatrix", "float4x4"),#
	])
#CBVRRecompute : 2370.shdr.src
class CBVRRecompute  (EPyCStruct):
	fields = OrderedDict([
		("fDepthTreshold", "float"),#
		("fAngleTreshold", "float"),#
		("fMaxDepth", "float"),#
		("align0", "ubyte[4]"),#
		("fDepthTreshold2", "float3"),#
		("align1", "ubyte[4]"),#
		("fAngleTreshold2", "float3"),#
		("align2", "ubyte[4]"),#
		("fMaxDepth2", "float3"),#
	])
#CBLuminanceDebugDisp : 3334.shdr.src
class CBLuminanceDebugDisp  (EPyCStruct):
	fields = OrderedDict([
		("iLuminanceDispMode", "uint"),#
		("align0", "ubyte[12]"),#
		("fLuminanceDebugDispColor", "float4"),#
		("fLuminanceDebugDispMinMax", "float2"),#
	])
#CBLGTPRBGen : 6184.shdr.src
class CBLGTPRBGen  (EPyCStruct):
	fields = OrderedDict([
		("iCurrentIndex", "uint"),#
		("iWindowType", "uint"),#
	])
#CBMhMaterialStdBlendLocal__disclosure : 5270.shdr.src
class CBMhMaterialStdBlendLocal__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fBaseMapFactor__uiColor", "float4"),#
		("fEmissiveMapFactor__uiColor", "float3"),#
		("fMetalic__uiUNorm", "float"),#
		("fRoughness__uiUNorm", "float"),#
		("fSpecular__uiUNorm", "float"),#
		("fSubSurfaceBlend__uiUNorm", "float"),#
		("iSubSurfaceProfile", "uint"),#
		("fDetailNormalBlend__uiUNorm", "float"),#
		("align0", "ubyte[12]"),#
		("fUVTransformA", "float4"),#
		("fUVTransformB", "float4"),#
		("fTranslucency__uiUNorm", "float"),#
		("fEmissiveBlendColor__uiColor", "float3"),#
		("fEmissiveBlendColorBlend__uiUNorm", "float"),#
		("fEmissiveBlendRimParam", "float3"),#
		("fBlendBaseMapFactor__uiColor", "float4"),#
		("fBlendEmissiveMapFactor__uiColor", "float3"),#
		("fBlendMetalic__uiUNorm", "float"),#
		("fBlendRoughness__uiUNorm", "float"),#
		("fBlendDetailNormalBlend__uiUNorm", "float"),#
		("fBlendSubSurfaceBlend__uiUNorm", "float"),#
		("align1", "ubyte[4]"),#
		("fBlendUVTransformA", "float4"),#
		("fBlendUVTransformB", "float4"),#
		("fBlendDir__uiDirection", "float3"),#
		("fBlendPlaneNormal__uiUNorm", "float"),#
		("fBlendOp", "float3"),#
		("bUseUVSecondaryMtA", "bbool"),#
		("bUseUVSecondaryMtB", "bbool"),#
		("bUseUVSecondaryMtBM", "bbool"),#
		("fFurNormalBlend__uiUNorm", "float"),#
		("fFurHeight__uiUNorm", "float"),#
		("fFurMapBlend__uiUNorm", "float"),#
		("fFurEdgeBlend__uiUNorm", "float"),#
		("fFurTile", "float"),#
		("align2", "ubyte[4]"),#
		("fWetBlendDir__uiDirection", "float3"),#
		("fWetBlendPlaneNormal__uiUNorm", "float"),#
		("fWetBlendOp", "float3"),#
		("bSpecialBlend", "bbool"),#
		("bWetNormalBlend", "bbool"),#
		("fWetNormalBlendRange__uiUNorm", "float2"),#
	])
#CBMotionBlur : 3655.shdr.src
class CBMotionBlur  (EPyCStruct):
	fields = OrderedDict([
		("iMotionBlurSampleNum", "int"),#
		("fMotionBlurShutterSpeed", "float"),#
		("fMaxAdditionalVelocity", "float"),#
		("align0", "ubyte[4]"),#
		("fTransform", "float4x4"),#
		("fMotionBlurFurShutterSpeed", "float"),#
	])
#CBAmbientOccluder : 1020.shdr.src
class CBAmbientOccluder  (EPyCStruct):
	fields = OrderedDict([
		("fIntensity", "float"),#
	])
#CBLightProbes : 992.shdr.src
class CBLightProbes  (EPyCStruct):
	fields = OrderedDict([
		("bLightProbesEnable", "bbool"),#
		("probesGridInvCellSize", "float3"),#
		("probesGridPosition", "float3"),#
		("align0", "ubyte[4]"),#
		("probesGridSize", "uint3"),#
		("align1", "ubyte[4]"),#
		("fProbesGridHalf", "float3"),#
		("align2", "ubyte[4]"),#
		("probeColor", "float3"),#
		("align3", "ubyte[4]"),#
		("fOutsideSHCoef", "float4[7]"),#
		("fShadowSHCoef", "float4[7]"),#
		("lightProbesHemisphereTopIntensity", "float"),#
		("lightProbesHemisphereBottomIntensity", "float"),#
		("iProbeFlags", "uint"),#
		("fDaytimeInterpolation", "float"),#
	])

#CBMhMaterialLandscapeLocal__disclosure : 1890.shdr.src
class CBMhMaterialLandscapeLocal__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fBaseMapFactor__uiColor", "float4"),#
		("fEmissiveMapFactor__uiColor", "float3"),#
		("fMetalic__uiUNorm", "float"),#
		("fRoughness__uiUNorm", "float"),#
		("fSpecular__uiUNorm", "float"),#
		("fSubSurfaceBlend__uiUNorm", "float"),#
		("iSubSurfaceProfile", "uint"),#
		("fDetailNormalBlend__uiUNorm", "float"),#
		("align0", "ubyte[12]"),#
		("fUVTransformA", "float4"),#
		("fUVTransformB", "float4"),#
		("fTranslucency__uiUNorm", "float"),#
		("align1", "ubyte[12]"),#
		("fUVTransformC", "float4"),#
		("fUVTransformD", "float4"),#
		("fUVTransformE", "float4"),#
		("fParallaxFactor__uiUNorm", "float"),#
		("fParallaxMinSampleNum__uiUNorm", "float"),#
		("fParallaxMaxSampleNum__uiUNorm", "float"),#
		("fBlendHeightMin__uiUNorm", "float"),#
		("fBlendHeightMax__uiUNorm", "float"),#
		("fParallaxAttenDistanceBegin", "float"),#
		("fParallaxAttenDistanceEnd", "float"),#
		("fParallaxVertexOffset", "float"),#
		("bSpecialBlend", "bbool"),#
		("bWetNormalBlend", "bbool"),#
		("fWetNormalBlendRange__uiUNorm", "float2"),#
	])
#CBMhSkyVS : 5086.shdr.src
class CBMhSkyVS  (EPyCStruct):
	fields = OrderedDict([
		("fSkyWorld", "float3x4"),#
	])
#CBHermiteCurveRGB : 6353.shdr.src
class CBHermiteCurveRGB  (EPyCStruct):
	fields = OrderedDict([
		("fHermiteParamR", "float2[64]"),#
		("align0", "ubyte[8]"),#
		("fHermiteParamG", "float2[64]"),#
		("align1", "ubyte[8]"),#
		("fHermiteParamB", "float2[64]"),#
	])
#CBMhMaterialEM002Local__disclosure : 2570.shdr.src
class CBMhMaterialEM002Local__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fBaseMapFactor__uiColor", "float4"),#
		("fEmissiveMapFactor__uiColor", "float3"),#
		("fMetalic__uiUNorm", "float"),#
		("fRoughness__uiUNorm", "float"),#
		("fSpecular__uiUNorm", "float"),#
		("fSubSurfaceBlend__uiUNorm", "float"),#
		("iSubSurfaceProfile", "uint"),#
		("fTranslucency__uiUNorm", "float"),#
		("bBaseColorEmissive", "bbool"),#
		("fPaintUVTile", "float2"),#
		("fAddNormalBlend__uiUNorm", "float"),#
		("align0", "ubyte[12]"),#
		("fAddNormalMaskA__uiSNorm", "float4"),#
		("fAddNormalMaskB__uiSNorm", "float4"),#
		("fAddNormalMaskC__uiUNorm", "float"),#
		("fAddNormalMaskD__uiUNorm", "float"),#
		("bBackFaceShading", "bbool"),#
		("align1", "ubyte[4]"),#
		("fBackFaceColor__uiColor", "float4"),#
		("bBackFaceNormalFilp", "bbool"),#
		("fKizuColor__uiColor", "float3"),#
		("bLegendary", "bbool"),#
		("align2", "ubyte[12]"),#
		("fLegendColor__uiColor", "float4"),#
		("fLegendMetalMask__uiUNorm", "float2"),#
		("fLegendRoughness", "float"),#
		("align3", "ubyte[4]"),#
		("fLegendFilm__uiUNorm", "float2"),#
		("fLegendSSSMask__uiUNorm", "float"),#
		("fPartsMaskA__uiUNorm", "float"),#
		("fPartsMaskB__uiUNorm", "float"),#
		("fPartsMaskC__uiUNorm", "float"),#
		("fPartsMaskD__uiUNorm", "float"),#
		("fPartsMaskX__uiUNorm", "float"),#
		("fPartsMaskY__uiUNorm", "float"),#
		("fPartsMaskZ__uiUNorm", "float"),#
		("fPartsMaskW__uiUNorm", "float"),#
		("bUseOffset", "bbool"),#
		("fFlowDirDir__uiDirection", "float3"),#
		("align4", "ubyte[4]"),#
		("fFlowControl__uiUNorm", "float4"),#
		("fFlowTile", "float"),#
		("align5", "ubyte[12]"),#
		("fFlowColor__uiColor", "float4"),#
		("fFlowMatControl__uiUNorm", "float4"),#
		("fMaskBlend__uiUNorm", "float4"),#
		("fMaskBlend_A__uiUNorm", "float2"),#
		("fMaskBlend_B__uiUNorm", "float2"),#
		("fFilmThickness__uiUNorm", "float"),#
		("fFilmBlend__uiUNorm", "float"),#
		("fRefraction__uiUNorm", "float"),#
		("fRefractionBlend__uiUNorm", "float"),#
	])
#CBSpeedTree : 5167.shdr.src
class CBSpeedTree  (EPyCStruct):
	fields = OrderedDict([
		("fSpeedTreeParam", "float2"),#
		("align0", "ubyte[8]"),#
		("iSpeedTreeParam", "int3"),#
	])
#CBImagePlane2 : 1182.shdr.src
class CBImagePlane2  (EPyCStruct):
	fields = OrderedDict([
		("fFilterUVMin", "float2"),#
		("fFilterUVMax", "float2"),#
	])
#CBMhMaterialNikuLocal__disclosure : 4850.shdr.src
class CBMhMaterialNikuLocal__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fBaseMapFactor__uiColor", "float4"),#
		("fEmissiveMapFactor__uiColor", "float3"),#
		("fMetalic__uiUNorm", "float"),#
		("fRoughness__uiUNorm", "float"),#
		("fSpecular__uiUNorm", "float"),#
		("fSubSurfaceBlend__uiUNorm", "float"),#
		("iSubSurfaceProfile", "uint"),#
		("fTranslucency__uiUNorm", "float"),#
		("align0", "ubyte[12]"),#
		("fUVTransformA", "float4"),#
		("fNikuMode__uiUNorm", "float4"),#
	])
#CBMhMaterialVfxDispWaveLocal__disclosure : 1361.shdr.src
class CBMhMaterialVfxDispWaveLocal__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fUVTransformA", "float4"),#
		("fUVTransformB", "float4"),#
		("fAdditionalRot", "float3"),#
		("align0", "ubyte[4]"),#
		("fWaveAxis__uiSNorm", "float3"),#
		("align1", "ubyte[4]"),#
		("fWaveScale__uiUNorm", "float3"),#
		("fWaveAngle", "float"),#
		("fDetailDisplacement", "float"),#
		("fYAxisDepth", "float"),#
		("fWhiteWaterPow", "float"),#
		("fFitRange", "float"),#
		("fBaseMapFactor__uiColor", "float4"),#
		("fDistortionFactor__uiColor", "float3"),#
		("align2", "ubyte[4]"),#
		("fCubeMapFactor__uiColor", "float3"),#
		("fNormalFactor__uiUNorm", "float"),#
		("fRaflectionAngle__uiSNorm", "float"),#
		("fDistortionAngle", "float"),#
		("fDistortion", "float"),#
		("fOpacityFactor", "float"),#
		("fVolumeBlend__uiSNorm", "float"),#
		("fMetalic__uiUNorm", "float"),#
		("fRoughness__uiUNorm", "float"),#
		("fSpecularFactor", "float"),#
		("fTranslucency__uiUNorm", "float"),#
		("fDiffuseChroma__uiUNorm", "float"),#
		("fSpecularChroma__uiUNorm", "float"),#
		("bSceneEnvMap", "bbool"),#
		("fInnerOffsetScale", "float"),#
		("fVelocityAttn", "float"),#
		("fNormalDecalBlend__uiUNorm", "float"),#
	])
#CBWaterPick : 393.shdr.src
class CBWaterPick  (EPyCStruct):
	fields = OrderedDict([
		("iWaterAddress", "uint2"),#
	])
#CBPrimitiveDebug : 2380.shdr.src
class CBPrimitiveDebug  (EPyCStruct):
	fields = OrderedDict([
		("fWorldOffset", "float3"),#
	])
#CBSystemColor : 6558.shdr.src
class CBSystemColor  (EPyCStruct):
	fields = OrderedDict([
		("fSystemColor", "float4"),#
	])
#CBAmbientOcclusion : 6565.shdr.src
class CBAmbientOcclusion  (EPyCStruct):
	fields = OrderedDict([
		("iSSAOPrimaryReductionLevel", "int"),#
		("iSSAOPrimaryFactor", "uint"),#
		("fSSAOPrimaryScale", "float"),#
		("fApproximateSSAOSamplePerPixel", "float"),#
		("iApproximateSSAOMaxSampleNum", "uint"),#
		("fApproximateSSAOBias", "float"),#
		("fApproximateSSAOWeight", "float"),#
		("align0", "ubyte[4]"),#
		("fApproximateSSAORadiusMat", "float4x4"),#
		("fPrimaryShadowRadius", "float"),#
		("iPrimaryShadowSampleNum", "uint"),#
		("fPrimaryShadowUpsampleThresholdMin", "float"),#
		("fPrimaryShadowUpsampleThresholdMax", "float"),#
		("fPrimaryShadowUpsampleThresholdDiffInv", "float"),#
	])
#CB_TemporalAA : 4386.shdr.src
class CB_TemporalAA  (EPyCStruct):
	fields = OrderedDict([
		("fReprojectionOffset", "float2"),#
		("fReprojectionScale", "float2"),#
		("fTemporalOffset", "float2"),#
		("fTemporalScale", "float2"),#
		("fTemporalClampMin", "float2"),#
		("fTemporalClampMax", "float2"),#
		("fBlendRate", "float"),#
		("bVelocityBase", "bbool"),#
	])
#CBMhMaterialSpeedTreeStdLocal__disclosure : 5022.shdr.src
class CBMhMaterialSpeedTreeStdLocal__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fBaseMapFactor__uiColor", "float4"),#
		("fEmissiveMapFactor__uiColor", "float3"),#
		("fMetalic__uiUNorm", "float"),#
		("fRoughness__uiUNorm", "float"),#
		("fSpecular__uiUNorm", "float"),#
		("fSubSurfaceBlend__uiUNorm", "float"),#
		("iSubSurfaceProfile", "uint"),#
		("fDetailNormalBlend__uiUNorm", "float"),#
		("align0", "ubyte[12]"),#
		("fUVTransformA", "float4"),#
		("fUVTransformB", "float4"),#
		("fBaseMapModulation__uiUNorm", "float4"),#
		("fTranslucency__uiUNorm", "float"),#
		("bLightProbeEmissive", "bbool"),#
		("align1", "ubyte[8]"),#
		("fEmissiveBlendColor__uiColor", "float3"),#
		("fEmissiveBlendColorBlend__uiUNorm", "float"),#
		("fEmissiveBlendRimParam", "float3"),#
		("bSpecialBlend", "bbool"),#
		("fRoughnessThreshold__uiUNorm", "float"),#
		("fRoughnessFillValue__uiUNorm", "float"),#
		("bWetNormalBlend", "bbool"),#
		("align2", "ubyte[4]"),#
		("fWetNormalBlendRange__uiUNorm", "float2"),#
	])
#CBBokehComposite : 6170.shdr.src
class CBBokehComposite  (EPyCStruct):
	fields = OrderedDict([
		("fBokehMipBias", "float"),#
		("fBokehMipScale", "float"),#
		("fBokehAlphaScale", "float"),#
		("fBokehRangeScale", "float"),#
		("fBokehDitherScale", "float"),#
		("iBokehSampleCount", "int"),#
		("align0", "ubyte[8]"),#
		("fBokehTap", "float2[25]"),#
	])
#CBMhMaterialEM102Local__disclosure : 4928.shdr.src
class CBMhMaterialEM102Local__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fBaseMapFactor__uiColor", "float4"),#
		("fEmissiveMapFactor__uiColor", "float3"),#
		("fMetalic__uiUNorm", "float"),#
		("fRoughness__uiUNorm", "float"),#
		("fSpecular__uiUNorm", "float"),#
		("fSubSurfaceBlend__uiUNorm", "float"),#
		("iSubSurfaceProfile", "uint"),#
		("fTranslucency__uiUNorm", "float"),#
		("bBaseColorEmissive", "bbool"),#
		("fPaintUVTile", "float2"),#
		("fAddNormalBlend__uiUNorm", "float"),#
		("align0", "ubyte[12]"),#
		("fAddNormalMaskA__uiSNorm", "float4"),#
		("fAddNormalMaskB__uiSNorm", "float4"),#
		("fAddNormalMaskC__uiUNorm", "float"),#
		("fAddNormalMaskD__uiUNorm", "float"),#
		("bBackFaceShading", "bbool"),#
		("align1", "ubyte[4]"),#
		("fBackFaceColor__uiColor", "float4"),#
		("bBackFaceNormalFilp", "bbool"),#
		("fKizuColor__uiColor", "float3"),#
		("bLegendary", "bbool"),#
		("align2", "ubyte[12]"),#
		("fLegendColor__uiColor", "float4"),#
		("fLegendMetalMask__uiUNorm", "float2"),#
		("fLegendRoughness", "float"),#
		("align3", "ubyte[4]"),#
		("fLegendFilm__uiUNorm", "float2"),#
		("fLegendSSSMask__uiUNorm", "float"),#
		("fPartsMaskA__uiUNorm", "float"),#
		("fPartsMaskB__uiUNorm", "float"),#
		("fPartsMaskC__uiUNorm", "float"),#
		("fPartsMaskD__uiUNorm", "float"),#
		("fPartsMaskX__uiUNorm", "float"),#
		("fPartsMaskY__uiUNorm", "float"),#
		("fPartsMaskZ__uiUNorm", "float"),#
		("fPartsMaskW__uiUNorm", "float"),#
		("bUseOffset", "bbool"),#
		("fFlowDirDir__uiDirection", "float3"),#
		("align4", "ubyte[4]"),#
		("fFlowControl__uiUNorm", "float4"),#
		("fFlowTile", "float"),#
		("align5", "ubyte[12]"),#
		("fFlowColor__uiColor", "float4"),#
		("fFlowMatControl__uiUNorm", "float4"),#
		("fMaskBlend__uiUNorm", "float4"),#
		("fMaskBlend_A__uiUNorm", "float2"),#
		("fMaskBlend_B__uiUNorm", "float2"),#
		("fFilmThickness__uiUNorm", "float"),#
		("fFilmBlend__uiUNorm", "float"),#
		("fRefraction__uiUNorm", "float"),#
		("fRefractionBlend__uiUNorm", "float"),#
		("fFurParam__uiUNorm", "float4"),#
		("fFurTile", "float"),#
		("fAlbedoBlend__uiSNorm", "float"),#
		("bAlbedoOverUVsecondary", "bbool"),#
	])
#CBImagePlane : 1183.shdr.src
class CBImagePlane  (EPyCStruct):
	fields = OrderedDict([
		("fImagePlaneColor", "float4"),#
		("fImagePlaneUVTransform", "float4x4"),#
		("fImagePlaneTechnique", "uint"),#
		("fBlendType", "uint"),#
		("bIsScreenPass", "bbool"),#
		("fGamma", "float"),#
	])
#CBPrimitiveEx : 998.shdr.src
class CBPrimitiveEx  (EPyCStruct):
	fields = OrderedDict([
		("fPrimParamEx0", "float4"),#
		("fPrimParamEx1", "float4"),#
		("fPrimParamEx2", "float4"),#
		("iPrimParamEx3", "uint4"),#
	])
#CBMhMaterialNPCEyeLocal__disclosure : 2438.shdr.src
class CBMhMaterialNPCEyeLocal__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fBaseMapFactor__uiColor", "float4"),#
		("fEmissiveMapFactor__uiColor", "float3"),#
		("fMetalic__uiUNorm", "float"),#
		("fRoughness__uiUNorm", "float"),#
		("fSpecular__uiUNorm", "float"),#
		("fSubSurfaceBlend__uiUNorm", "float"),#
		("iSubSurfaceProfile", "uint"),#
		("fTranslucency__uiUNorm", "float"),#
		("bBaseColorEmissive", "bbool"),#
		("bBackFaceNormalFilp", "bbool"),#
		("fAnimEmitMin", "float"),#
		("fAnimEmitSpeed", "float"),#
		("fParallaxFactor__uiUNorm", "float"),#
		("fDetailNormalBlend__uiUNorm", "float"),#
		("align0", "ubyte[4]"),#
		("fUVTransformDetailNormal", "float4"),#
	])
#CBMhMaterialFlagWaveLocal__disclosure : 6288.shdr.src
class CBMhMaterialFlagWaveLocal__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fBaseMapFactor__uiColor", "float4"),#
		("fEmissiveMapFactor__uiColor", "float3"),#
		("fMetalic__uiUNorm", "float"),#
		("fRoughness__uiUNorm", "float"),#
		("fSpecular__uiUNorm", "float"),#
		("fSubSurfaceBlend__uiUNorm", "float"),#
		("iSubSurfaceProfile", "uint"),#
		("fTranslucency__uiUNorm", "float"),#
		("align0", "ubyte[12]"),#
		("fUVTransformA", "float4"),#
		("fVPushScale", "float"),#
		("fVPushWave", "float"),#
		("fVPushSpeed", "float"),#
		("align1", "ubyte[4]"),#
		("fFlagUvEditA", "float4"),#
		("fFlagUvEditB", "float4"),#
		("fFlagControl", "float4"),#
		("fDisplaceControl", "float4"),#
		("fDispFactor", "float"),#
	])
#CBMhMaterialVfxDebufBodyLocal__disclosure : 849.shdr.src
class CBMhMaterialVfxDebufBodyLocal__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fUVTransformA", "float4"),#
		("fBaseMapFactor__uiColor", "float4"),#
		("fEmissiveMapFactor__uiColor", "float3"),#
		("fNormalFactor__uiUNorm", "float"),#
		("fMetalic__uiUNorm", "float"),#
		("fRoughness__uiUNorm", "float"),#
		("fTranslucency__uiUNorm", "float"),#
		("fSpecularFactor", "float"),#
		("fOpacityFactor", "float"),#
		("fRimOpacityPow", "float"),#
		("fVolumeBlend__uiSNorm", "float"),#
		("align0", "ubyte[4]"),#
		("fFlowDir__uiDirection", "float3"),#
		("fFlowStrength", "float"),#
		("fFlowSpeed", "float"),#
		("fDiffuseChroma__uiUNorm", "float"),#
		("fSpecularChroma__uiUNorm", "float"),#
		("fInnerOffsetScale", "float"),#
		("fVelocityAttn", "float"),#
		("fNormalDecalBlend__uiUNorm", "float"),#
	])
#CBLUTBlending : 1081.shdr.src
class CBLUTBlending  (EPyCStruct):
	fields = OrderedDict([
		("fLUTBlend", "float"),#
		("fVfxLUTBlend", "float"),#
		("bIsBlend", "bbool"),#
		("bIsVfxBlend", "bbool"),#
	])
#CBPrimitive : 999.shdr.src
class CBPrimitive  (EPyCStruct):
	fields = OrderedDict([
		("fPrimParam0", "float4"),#
		("fPrimParam1", "float4"),#
		("fPrimParam2", "float4"),#
		("fPrimParam3", "float4"),#
		("fPrimParam4", "float4"),#
		("fPrimParam5", "float4"),#
		("fPrimParam6", "float4"),#
		("fPrimParam7", "float4"),#
		("fPrimParam8", "float4"),#
		("fPrimParam9", "float4"),#
		("iPrimParam0", "uint4"),#
	])
#CBErrorUnit : 1989.shdr.src
class CBErrorUnit  (EPyCStruct):
	fields = OrderedDict([
		("iErrorUnitAddress", "uint2"),#
		("iErrorUnitPass", "uint"),#
		("iErrorUnitPrio", "uint"),#
	])
#CBWaterWaveMaterial : 5751.shdr.src
class CBWaterWaveMaterial  (EPyCStruct):
	fields = OrderedDict([
		("fReflectionViewProj", "float4x4"),#
		("fUserNormalTiling", "float2"),#
		("fUserNormalIntensity", "float"),#
		("fUserNormalMoveSpeed", "float"),#
		("fUserNormalMoveDirection", "float2"),#
		("fUserNormal2Tiling", "float2"),#
		("fUserNormal2Intensity", "float"),#
		("fUserNormal2MoveSpeed", "float"),#
		("fUserNormal2MoveDirection", "float2"),#
		("fInvDepthMax", "float"),#
		("fReflectionDistortion", "float"),#
		("fFresnelBias", "float"),#
		("fHorizonBias", "float"),#
		("fExtinctionCoefficient", "float3"),#
		("fMurkiness", "float"),#
		("fWaterColor", "float3"),#
		("fRefractionDistortion", "float"),#
		("fCausticsTiling", "float2"),#
		("fCausticsIntensity", "float"),#
		("fCausticsMoveSpeed", "float"),#
		("fCausticsMoveDirection", "float2"),#
		("fCausticsDensityLow", "float"),#
		("fRefactionIndex", "float"),#
		("fSlopeVariance", "float2"),#
		("fSunlightReflectanceRange", "float2"),#
		("fReflectanceBiasRate", "float"),#
		("fInvDepthFade", "float"),#
		("fSunlightReflectionIntensity", "float"),#
		("fCubemapBlendRate", "float"),#
		("iLightGroup", "uint"),#
	])
#CBScreen : 998.shdr.src
class CBScreen  (EPyCStruct):
	fields = OrderedDict([
		("fScreenOffset", "float2"),#
		("fScreenScale", "float2"),#
		("fScreenSize", "float2"),#
		("fScreenInverseSize", "float2"),#
		("iViewOffset", "uint2"),#
		("iViewSize", "uint2"),#
		("fViewOffset", "float2"),#
		("fViewSize", "float2"),#
		("fViewInverseSize", "float2"),#
		("fContentScale", "float"),#
		("fContentScalePF", "float"),#
		("fContentScaleBase", "float"),#
		("fContentScaleActual", "float"),#
		("fContentScaleInverse", "float"),#
		("fContentScaleBaseInverse", "float"),#
		("fContentScaleActualInverse", "float"),#
		("fContentScalePassScreen", "float"),#
		("bCheckerboard", "bbool"),#
	])
#CBDecalCommon : 32.shdr.src
class CBDecalCommon  (EPyCStruct):
	fields = OrderedDict([
		("fDecalColor", "float4"),#
		("fDecalCenter", "float3"),#
		("align0", "ubyte[4]"),#
		("fDecalRange", "float3"),#
		("align1", "ubyte[4]"),#
		("fDecalUVRange", "float4"),#
		("fDecalTangent", "float3"),#
		("align2", "ubyte[4]"),#
		("fDecalBinormal", "float3"),#
	])
#CBDebug : 3585.shdr.src
class CBDebug  (EPyCStruct):
	fields = OrderedDict([
		("iDebugView", "int"),#
		("iDebugViewChannel", "int"),#
		("iDebugLightMaxCount", "int"),#
		("fDebugViewBgAlpha", "float"),#
		("fDebugViewFgAlpha", "float"),#
		("fDebugViewScaling", "float2"),#
	])
#CBColorCorrectCube : 6115.shdr.src
class CBColorCorrectCube  (EPyCStruct):
	fields = OrderedDict([
		("fLinearFactor", "float"),#
		("fDepthNear", "float"),#
		("fDepthFar", "float"),#
	])
#CBMhDecalSM : 4085.shdr.src
class CBMhDecalSM  (EPyCStruct):
	fields = OrderedDict([
		("fFireFactor", "float"),#
		("fFireLifeFactor", "float"),#
		("fFireAlphaFactor", "float"),#
		("fFireColorRate", "float"),#
		("bFireLighting", "bbool"),#
		("fFireColor", "float3"),#
		("fSmokeFactor", "float"),#
		("fSmokeLifeFactor", "float"),#
		("bSmokeLighting", "bbool"),#
		("align0", "ubyte[4]"),#
		("fSmokeColor", "float3"),#
		("fWaterColorRate", "float"),#
		("fWaterColorSpecular", "float3"),#
		("align1", "ubyte[4]"),#
		("fWaterColorSheet", "float3"),#
		("fWaterIntensitySpecular", "float"),#
		("fWaterLerpGtoB", "float"),#
		("fWaterIntensitySheet", "float"),#
		("fWaterSpecularLifeFactor", "float"),#
		("fWaterSheetLifeFactor", "float"),#
		("fWaterGtoBLifeFactor", "float"),#
		("fWaterIntensityCubeMap", "float"),#
		("fWaterNormalSharpness", "float"),#
		("fWaterIntensityAlpha", "float"),#
	])
#CBMhMaterial_EM105_EVCLocal__disclosure : 4506.shdr.src
class CBMhMaterial_EM105_EVCLocal__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fBaseMapFactor__uiColor", "float4"),#
		("fEmissiveMapFactor__uiColor", "float3"),#
		("fMetalic__uiUNorm", "float"),#
		("fRoughness__uiUNorm", "float"),#
		("fSpecular__uiUNorm", "float"),#
		("fSubSurfaceBlend__uiUNorm", "float"),#
		("iSubSurfaceProfile", "uint"),#
		("fTranslucency__uiUNorm", "float"),#
		("bBaseColorEmissive", "bbool"),#
		("fPaintUVTile", "float2"),#
		("fAddNormalBlend__uiUNorm", "float"),#
		("align0", "ubyte[12]"),#
		("fAddNormalMaskA__uiSNorm", "float4"),#
		("fAddNormalMaskB__uiSNorm", "float4"),#
		("fAddNormalMaskC__uiUNorm", "float"),#
		("fAddNormalMaskD__uiUNorm", "float"),#
		("bBackFaceShading", "bbool"),#
		("align1", "ubyte[4]"),#
		("fBackFaceColor__uiColor", "float4"),#
		("bBackFaceNormalFilp", "bbool"),#
		("fKizuColor__uiColor", "float3"),#
		("bLegendary", "bbool"),#
		("align2", "ubyte[12]"),#
		("fLegendColor__uiColor", "float4"),#
		("fLegendMetalMask__uiUNorm", "float2"),#
		("fLegendRoughness", "float"),#
		("align3", "ubyte[4]"),#
		("fLegendFilm__uiUNorm", "float2"),#
		("fLegendSSSMask__uiUNorm", "float"),#
		("fPartsMaskA__uiUNorm", "float"),#
		("fPartsMaskB__uiUNorm", "float"),#
		("fPartsMaskC__uiUNorm", "float"),#
		("fPartsMaskD__uiUNorm", "float"),#
		("fPartsMaskX__uiUNorm", "float"),#
		("fPartsMaskY__uiUNorm", "float"),#
		("fPartsMaskZ__uiUNorm", "float"),#
		("fPartsMaskW__uiUNorm", "float"),#
		("bUseOffset", "bbool"),#
		("fFlowDirDir__uiDirection", "float3"),#
		("align4", "ubyte[4]"),#
		("fFlowControl__uiUNorm", "float4"),#
		("fFlowTile", "float"),#
		("align5", "ubyte[12]"),#
		("fFlowColor__uiColor", "float4"),#
		("fFlowMatControl__uiUNorm", "float4"),#
		("fFilmThickness__uiUNorm", "float"),#
		("fFilmBlend__uiUNorm", "float"),#
		("fRefraction__uiUNorm", "float"),#
		("fRefractionBlend__uiUNorm", "float"),#
		("bUseBlendDisplace", "bbool"),#
		("fVAnimV__uiUNorm", "float"),#
		("fVAnimPosScale", "float"),#
		("bInvertX", "bbool"),#
		("fVPushScale", "float"),#
		("fVPushWave", "float"),#
		("fVPushSpeed", "float"),#
		("align6", "ubyte[4]"),#
		("fVpivot", "float3"),#
		("fInnerOffsetScale", "float"),#
		("fRimAlphaPower__uiSNorm", "float"),#
		("fVolumeBlend__uiSNorm", "float"),#
		("align7", "ubyte[8]"),#
		("fDetailEmissiveControl", "float4"),#
		("fRimTranslucency__uiUNorm", "float"),#
		("fFinWave", "float"),#
		("fFinSpeed", "float"),#
		("align8", "ubyte[4]"),#
		("fFinColor__uiColor", "float3"),#
		("fDetailNormalBlend__uiUNorm", "float"),#
	])
#CBMhMaterialEM115Local__disclosure : 2132.shdr.src
class CBMhMaterialEM115Local__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fBaseMapFactor__uiColor", "float4"),#
		("fEmissiveMapFactor__uiColor", "float3"),#
		("fMetalic__uiUNorm", "float"),#
		("fRoughness__uiUNorm", "float"),#
		("fSpecular__uiUNorm", "float"),#
		("fSubSurfaceBlend__uiUNorm", "float"),#
		("iSubSurfaceProfile", "uint"),#
		("fTranslucency__uiUNorm", "float"),#
		("bBaseColorEmissive", "bbool"),#
		("fPaintUVTile", "float2"),#
		("fAddNormalBlend__uiUNorm", "float"),#
		("align0", "ubyte[12]"),#
		("fAddNormalMaskA__uiSNorm", "float4"),#
		("fAddNormalMaskB__uiSNorm", "float4"),#
		("fAddNormalMaskC__uiUNorm", "float"),#
		("fAddNormalMaskD__uiUNorm", "float"),#
		("bBackFaceShading", "bbool"),#
		("align1", "ubyte[4]"),#
		("fBackFaceColor__uiColor", "float4"),#
		("bBackFaceNormalFilp", "bbool"),#
		("fKizuColor__uiColor", "float3"),#
		("bLegendary", "bbool"),#
		("align2", "ubyte[12]"),#
		("fLegendColor__uiColor", "float4"),#
		("fLegendMetalMask__uiUNorm", "float2"),#
		("fLegendRoughness", "float"),#
		("align3", "ubyte[4]"),#
		("fLegendFilm__uiUNorm", "float2"),#
		("fLegendSSSMask__uiUNorm", "float"),#
		("fPartsMaskA__uiUNorm", "float"),#
		("fPartsMaskB__uiUNorm", "float"),#
		("fPartsMaskC__uiUNorm", "float"),#
		("fPartsMaskD__uiUNorm", "float"),#
		("fPartsMaskX__uiUNorm", "float"),#
		("fPartsMaskY__uiUNorm", "float"),#
		("fPartsMaskZ__uiUNorm", "float"),#
		("fPartsMaskW__uiUNorm", "float"),#
		("bUseOffset", "bbool"),#
		("fFlowDirDir__uiDirection", "float3"),#
		("align4", "ubyte[4]"),#
		("fFlowControl__uiUNorm", "float4"),#
		("fFlowTile", "float"),#
		("align5", "ubyte[12]"),#
		("fFlowColor__uiColor", "float4"),#
		("fFlowMatControl__uiUNorm", "float4"),#
		("fDisplaceControl", "float4"),#
		("fFurParam__uiUNorm", "float4"),#
		("fFurTile", "float"),#
		("fDispSpeed", "float"),#
		("fFilmThickness__uiUNorm", "float"),#
		("fFilmBlend__uiUNorm", "float"),#
		("fRefraction__uiUNorm", "float"),#
		("fRefractionBlend__uiUNorm", "float"),#
	])
#CBHeightToNormal : 4510.shdr.src
class CBHeightToNormal  (EPyCStruct):
	fields = OrderedDict([
		("fFactor", "float"),#
	])
#CBMhMaterialPLHairLocal__disclosure : 4068.shdr.src
class CBMhMaterialPLHairLocal__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fBaseMapFactor__uiColor", "float4"),#
		("fEmissiveMapFactor__uiColor", "float3"),#
		("fMetalic__uiUNorm", "float"),#
		("fRoughness__uiUNorm", "float"),#
		("fSpecular__uiUNorm", "float"),#
		("fSubSurfaceBlend__uiUNorm", "float"),#
		("iSubSurfaceProfile", "uint"),#
		("fTranslucency__uiUNorm", "float"),#
		("bBaseColorEmissive", "bbool"),#
		("bBackFaceNormalFilp", "bbool"),#
		("fAnimEmitMin", "float"),#
		("fAnimEmitSpeed", "float"),#
		("align0", "ubyte[12]"),#
		("fPrimaryColor__uiColor", "float4"),#
		("fSecondaryColor__uiColor", "float4"),#
		("fPrimaryExpo__uiUNorm", "float"),#
		("fSecondaryExpo__uiUNorm", "float"),#
		("fPrimaryShift__uiSNorm", "float"),#
		("fSecondaryShift__uiSNorm", "float"),#
		("fShininess", "float"),#
		("fFakeLight__uiDirection", "float3"),#
		("fFurNMHeight", "float"),#
		("align1", "ubyte[12]"),#
		("fFurParam__uiUNorm", "float4"),#
		("fFurTile", "float"),#
		("align2", "ubyte[12]"),#
		("fVertexAO__uiColor", "float4"),#
		("fVColorNormalBlend__uiUNorm", "float"),#
		("fRimWidth__uiUNorm", "float"),#
		("fRimNormalBlend__uiUNorm", "float"),#
		("bUseRimTranslucency", "bbool"),#
		("bUseOffset", "bbool"),#
		("fInnerOffsetScale", "float"),#
		("fDetailNormalBlend__uiUNorm", "float"),#
		("align3", "ubyte[4]"),#
		("fUVTransformDetailNormal", "float4"),#
	])

#CB_BGTexture : 3385.shdr.src
class CB_BGTexture  (EPyCStruct):
	fields = OrderedDict([
		("fBGTextureColor", "float4"),#
	])
#CBHermiteCurve : 1985.shdr.src
class CBHermiteCurve  (EPyCStruct):
	fields = OrderedDict([
		("fHermiteParam", "float4[8]"),#
	])
#CBMhMaterialScrWaterLocal__disclosure : 4653.shdr.src
class CBMhMaterialScrWaterLocal__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fBaseMapFactor__uiColor", "float4"),#
		("fEmissiveMapFactor__uiColor", "float3"),#
		("align0", "ubyte[4]"),#
		("fCubeMapFactor__uiColor", "float3"),#
		("fMetalic__uiUNorm", "float"),#
		("fRoughness__uiUNorm", "float"),#
		("fSpecular__uiUNorm", "float"),#
		("fSubSurfaceBlend__uiUNorm", "float"),#
		("iSubSurfaceProfile", "uint"),#
		("fTranslucency__uiUNorm", "float"),#
		("align1", "ubyte[12]"),#
		("fUVTransformA", "float4"),#
		("fUVTransformB", "float4"),#
		("fUVOffsetSpeedFactor", "float2"),#
		("fUVOffsetSpeedFactorDetail", "float2"),#
		("fDetailNormalBlend__uiUNorm", "float"),#
		("fRefraction__uiUNorm", "float"),#
		("fRefractionPow__uiUNorm", "float"),#
		("align2", "ubyte[4]"),#
		("fRefractionFactor__uiColor", "float3"),#
		("bRefractionScreenFade", "bbool"),#
		("fVolumeBlend__uiSNorm", "float"),#
		("fFlowStrength", "float"),#
		("fFlowSpeed", "float"),#
		("bDecalMode", "bbool"),#
	])
#CBTubeLight : 5941.shdr.src
class CBTubeLight  (EPyCStruct):
	fields = OrderedDict([
		("iTubeLightCount", "uint"),#
	])
#CBModel : 99.shdr.src
class CBModel  (EPyCStruct):
	fields = OrderedDict([
		("fWorld", "float3x4"),#
		("fWorldI", "float3x4"),#
		("fWorldPF", "float3x4"),#
		("iMatrixIndex", "uint"),#
		("iMatrixIndexPF", "uint"),#
		("iLightChannel", "uint"),#
		("align0", "ubyte[4]"),#
		("iUnitAddress", "uint2"),#
		("bPositionPFValid", "bbool"),#
		("bPassThrough", "bbool"),#
		("bInstanceMaterialEdit", "bbool"),#
		("bInstanceEffect", "bbool"),#
	])
#CBGUIDistanceField : 3229.shdr.src
class CBGUIDistanceField  (EPyCStruct):
	fields = OrderedDict([
		("fGUIDFParam0", "float3"),#
		("align0", "ubyte[4]"),#
		("fGUIDFColor0", "float4"),#
		("fGUIDFParam1", "float3"),#
		("align1", "ubyte[4]"),#
		("fGUIDFColor1", "float4"),#
	])
#CBLight : 993.shdr.src
class CBLight  (EPyCStruct):
	fields = OrderedDict([
		("iLightOffset", "uint"),#
		("iLightNum", "uint"),#
		("iPrimaryLight", "uint"),#
		("iGIDiffuseFlags", "uint"),#
		("bLightSortByType", "bbool"),#
		("fSHSSAOEffect", "float"),#
		("fSSAOEffectGI", "float"),#F
		("align0", "ubyte[4]"),#
		("fSHCoef", "float4[7]"),#
		("fPrimaryLightMat", "float4x4"),#
		("fBroadAreaShadowMat", "float4x4"),#
		("bBroadAreaShadowEnable", "bbool"),#
		("bGISpecularSHDiffuseBlend", "bbool"),#
		("iLightInfiniteRange", "uint2"),#
		("iLightPointRange", "uint2"),#
		("iLightSpotRange", "uint2"),#
	])
#CBMhMaterialGlobal : 773.shdr.src
class CBMhMaterialGlobal  (EPyCStruct):
	fields = OrderedDict([
		("fMaterialWetBlend", "float"),#
		("fMaterialWetRoughness", "float"),#
	])
#CBMhMaterialFurLocal__disclosure : 716.shdr.src
class CBMhMaterialFurLocal__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fBaseMapFactor__uiColor", "float4"),#
		("fEmissiveMapFactor__uiColor", "float3"),#
		("fMetalic__uiUNorm", "float"),#
		("fRoughness__uiUNorm", "float"),#
		("fSpecular__uiUNorm", "float"),#
		("fSubSurfaceBlend__uiUNorm", "float"),#
		("iSubSurfaceProfile", "uint"),#
		("fDetailNormalBlend__uiUNorm", "float"),#
		("align0", "ubyte[12]"),#
		("fUVTransformA", "float4"),#
		("fUVTransformB", "float4"),#
		("fTranslucency__uiUNorm", "float"),#
		("fEmissiveBlendColor__uiColor", "float3"),#
		("fEmissiveBlendColorBlend__uiUNorm", "float"),#
		("fEmissiveBlendRimParam", "float3"),#
		("fFurHeight__uiUNorm", "float"),#
		("fFurMapBlend__uiUNorm", "float"),#
		("fFurEdgeBlend__uiUNorm", "float"),#
		("fFurTile", "float"),#
	])
#CBMhMaterialNPCLocal__disclosure : 5818.shdr.src
class CBMhMaterialNPCLocal__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fBaseMapFactor__uiColor", "float4"),#
		("fEmissiveMapFactor__uiColor", "float3"),#
		("fMetalic__uiUNorm", "float"),#
		("fRoughness__uiUNorm", "float"),#
		("fSpecular__uiUNorm", "float"),#
		("fSubSurfaceBlend__uiUNorm", "float"),#
		("iSubSurfaceProfile", "uint"),#
		("fTranslucency__uiUNorm", "float"),#
		("bBaseColorEmissive", "bbool"),#
		("bBackFaceNormalFilp", "bbool"),#
		("fAnimEmitMin", "float"),#
		("fAnimEmitSpeed", "float"),#
		("bUseCMM", "bbool"),#
		("align0", "ubyte[8]"),#
		("fAddColorA__uiColor", "float4"),#
		("fAddColorB__uiColor", "float4"),#
		("fAddColorC__uiColor", "float4"),#
		("fAddColorD__uiColor", "float4"),#
		("fFurParam__uiUNorm", "float4"),#
		("fFurTile", "float"),#
		("fFilmThickness__uiUNorm", "float"),#
		("fFilmBlend__uiUNorm", "float"),#
		("align1", "ubyte[4]"),#
		("fEmissiveBlendColor__uiColor", "float3"),#
		("fEmissiveBlendColorBlend__uiUNorm", "float"),#
		("fEmissiveBlendRimParam", "float3"),#
		("fDetailNormalBlend__uiUNorm", "float"),#
		("fUVTransformDetailNormal", "float4"),#
	])
#CBMhMaterialFakeInnerEmitLocal__disclosure : 3495.shdr.src
class CBMhMaterialFakeInnerEmitLocal__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fEmissiveMapFactor__uiColor", "float3"),#
		("fInnerOffsetScale", "float"),#
		("fRimAlphaPower__uiUNorm", "float"),#
		("fVolumeBlend__uiSNorm", "float"),#
	])
#CBNewDOFFilter : 6560.shdr.src
class CBNewDOFFilter  (EPyCStruct):
	fields = OrderedDict([
		("coc_bias", "float"),#
		("coc_scale", "float"),#
		("pcoc", "float"),#
		("quad_reduction_threshold", "float"),#
		("quater_resolution_threshold", "float"),#
		("near_blur_scaler", "float"),#
		("depth_adjuist_factor", "float"),#
		("bokeh_intensity_threshold", "float"),#
		("bokeh_shape_factor", "float"),#
		("dof_single_pixel_radius", "float"),#
		("dof_aspect", "float"),#
		("far_ignore", "bbool"),#
		("near_ignore", "bbool"),#
		("far_coef", "float"),#
		("near_coef", "float"),#
		("fVignettingOffset", "float"),#
		("fVignettingPow", "float"),#
		("bVignetting", "bbool"),#
		("fVignettingEllipticity", "float"),#
		("align0", "ubyte[4]"),#
		("fVignettingColor", "float3"),#
	])
#CBMhMaterialEM011Local__disclosure : 3568.shdr.src
class CBMhMaterialEM011Local__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fBaseMapFactor__uiColor", "float4"),#
		("fEmissiveMapFactor__uiColor", "float3"),#
		("fMetalic__uiUNorm", "float"),#
		("fRoughness__uiUNorm", "float"),#
		("fSpecular__uiUNorm", "float"),#
		("fSubSurfaceBlend__uiUNorm", "float"),#
		("iSubSurfaceProfile", "uint"),#
		("fTranslucency__uiUNorm", "float"),#
		("bBaseColorEmissive", "bbool"),#
		("fPaintUVTile", "float2"),#
		("fAddNormalBlend__uiUNorm", "float"),#
		("align0", "ubyte[12]"),#
		("fAddNormalMaskA__uiSNorm", "float4"),#
		("fAddNormalMaskB__uiSNorm", "float4"),#
		("fAddNormalMaskC__uiUNorm", "float"),#
		("fAddNormalMaskD__uiUNorm", "float"),#
		("bBackFaceShading", "bbool"),#
		("align1", "ubyte[4]"),#
		("fBackFaceColor__uiColor", "float4"),#
		("bBackFaceNormalFilp", "bbool"),#
		("fKizuColor__uiColor", "float3"),#
		("bLegendary", "bbool"),#
		("align2", "ubyte[12]"),#
		("fLegendColor__uiColor", "float4"),#
		("fLegendMetalMask__uiUNorm", "float2"),#
		("fLegendRoughness", "float"),#
		("align3", "ubyte[4]"),#
		("fLegendFilm__uiUNorm", "float2"),#
		("fLegendSSSMask__uiUNorm", "float"),#
		("fPartsMaskA__uiUNorm", "float"),#
		("fPartsMaskB__uiUNorm", "float"),#
		("fPartsMaskC__uiUNorm", "float"),#
		("fPartsMaskD__uiUNorm", "float"),#
		("fPartsMaskX__uiUNorm", "float"),#
		("fPartsMaskY__uiUNorm", "float"),#
		("fPartsMaskZ__uiUNorm", "float"),#
		("fPartsMaskW__uiUNorm", "float"),#
		("bUseOffset", "bbool"),#
		("fFlowDirDir__uiDirection", "float3"),#
		("align4", "ubyte[4]"),#
		("fFlowControl__uiUNorm", "float4"),#
		("fFlowTile", "float"),#
		("align5", "ubyte[12]"),#
		("fFlowColor__uiColor", "float4"),#
		("fFlowMatControl__uiUNorm", "float4"),#
		("fDisplaceControl", "float4"),#
		("fFurParam__uiUNorm", "float4"),#
		("fFurTile", "float"),#
		("fDispSpeed", "float"),#
		("fFilmThickness__uiUNorm", "float"),#
		("fFilmBlend__uiUNorm", "float"),#
		("fRefraction__uiUNorm", "float"),#
		("fRefractionBlend__uiUNorm", "float"),#
	])
#CBCSClear : 3300.shdr.src
class CBCSClear  (EPyCStruct):
	fields = OrderedDict([
		("iSize", "uint"),#
	])
#CBROPTest : 999.shdr.src
class CBROPTest  (EPyCStruct):
	fields = OrderedDict([
		("bAlphaTestEnable", "bbool"),#
		("fAlphaRef", "float"),#
		("fDepthBias", "float"),#
		("fSlopedDepthBias", "float"),#
		("fMaxDepthBias", "float"),#
		("fGlobalTransparency", "float"),#
		("bAlphaDither", "bbool"),#
	])
#CBMhMaterialSimpleLocal__disclosure : 2763.shdr.src
class CBMhMaterialSimpleLocal__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fBaseMapFactor__uiColor", "float4"),#
		("fEmissiveMapFactor__uiColor", "float3"),#
		("fMetalic__uiUNorm", "float"),#
		("fRoughness__uiUNorm", "float"),#
		("fSpecular__uiUNorm", "float"),#
		("fSubSurfaceBlend__uiUNorm", "float"),#
		("iSubSurfaceProfile", "uint"),#
		("fTranslucency__uiUNorm", "float"),#
		("align0", "ubyte[12]"),#
		("fUVTransformA", "float4"),#
	])
#CBMhMaterialNPCSkinLocal__disclosure : 4283.shdr.src
class CBMhMaterialNPCSkinLocal__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fBaseMapFactor__uiColor", "float4"),#
		("fEmissiveMapFactor__uiColor", "float3"),#
		("fMetalic__uiUNorm", "float"),#
		("fRoughness__uiUNorm", "float"),#
		("fSpecular__uiUNorm", "float"),#
		("fSubSurfaceBlend__uiUNorm", "float"),#
		("iSubSurfaceProfile", "uint"),#
		("fTranslucency__uiUNorm", "float"),#
		("bBaseColorEmissive", "bbool"),#
		("bBackFaceNormalFilp", "bbool"),#
		("fAnimEmitMin", "float"),#
		("fAnimEmitSpeed", "float"),#
		("fAddColorUV__uiUNorm", "float2"),#
		("bUseCMM", "bbool"),#
		("fAddColorA__uiColor", "float4"),#
		("fDetailNormalBlend__uiUNorm", "float"),#
		("align0", "ubyte[12]"),#
		("fUVTransformDetailNormal", "float4"),#
	])
#CBMhSky2GBuffer : 3331.shdr.src
class CBMhSky2GBuffer  (EPyCStruct):
	fields = OrderedDict([
		("iSkyGBufferId", "uint"),#
	])
#CBHazeFilter : 1201.shdr.src
class CBHazeFilter  (EPyCStruct):
	fields = OrderedDict([
		("iHazeTech", "uint"),#
		("fHazeFilterStart", "float"),#
		("fHazeFilterInverseRange", "float"),#
		("fHazeFilterHeightStart", "float"),#
		("fHazeFilterHeightInverseRange", "float"),#
		("align0", "ubyte[12]"),#
		("fHazeFilterUVWOffset", "float4"),#
		("fHazeFilterScale", "float"),#
	])
#CBDOFFilter : 725.shdr.src
class CBDOFFilter  (EPyCStruct):
	fields = OrderedDict([
		("fDOFPoissonOffsets", "float2[8]"),#
		("fDOFPixelSizeLow", "float2"),#
		("fDOFPixelSizeHigh", "float2"),#
		("align0", "ubyte[8]"),#
		("fDOFGradateColor", "float3"),#
		("fDOFFocus", "float"),#
		("fDOFNear", "float"),#
		("fDOFFar", "float"),#
		("fDOFNearLimit", "float"),#
		("fDOFFarLimit", "float"),#
		("fDOFCoCScale", "float"),#
		("fDOFCoCBias", "float"),#
		("fDOFRadiusScale", "float"),#
		("fDOFCorrectParamNear", "float"),#
		("fDOFCorrectParamFar", "float"),#
		("align1", "ubyte[12]"),#
		("fDOFVelocityFactor", "float4"),#
	])
#CBGodRaysFilter : 599.shdr.src
class CBGodRaysFilter  (EPyCStruct):
	fields = OrderedDict([
		("fGodRaysOrigin", "float3"),#
		("fGodRaysMaskWeight", "float"),#
		("fGodRaysWorldOrigin", "float3"),#
		("fGodRaysMaskRadius", "float"),#
		("fGodRaysDecay", "float"),#
		("fGodRaysThreshold", "float"),#
		("fGodRaysSamples", "float"),#
		("fGodRaysGamma", "float"),#
		("fGodRaysColor", "float4"),#
		("fGodRaysShadowThreshold", "float"),#
		("fGodRaysBlurWidthScale", "float"),#
		("fGodRaysBlurWidthOffset", "float"),#
	])
#CBMhMaterialIvyFloor : 3226.shdr.src
class CBMhMaterialIvyFloor  (EPyCStruct):
	fields = OrderedDict([
		("iIvyFloorWindIndex", "int"),#
		("iIvyFloorWindIndexPF", "int"),#
		("iIvyFloorId", "uint2"),#
		("fIvyFloorWindScale", "float"),#
	])
#CBVRFilter : 1003.shdr.src
class CBVRFilter  (EPyCStruct):
	fields = OrderedDict([
		("fDimensions", "float4"),#
		("fFilterRegion", "float4"),#
		("fFilterMipLevel", "float"),#
		("vertical", "bbool"),#
	])
#CBDecal : 4085.shdr.src
class CBDecal  (EPyCStruct):
	fields = OrderedDict([
		("iDecalMode", "uint"),#
		("fDecalMetallic", "float"),#
		("fDecalRoughness", "float"),#
		("fDecalNonMetallicFresnel", "float"),#
		("fDecalLimitAngle", "float"),#
	])
#CBPrimVertexOffset : 852.shdr.src
class CBPrimVertexOffset  (EPyCStruct):
	fields = OrderedDict([
		("iPrimVertexOffset", "uint"),#
		("iPrimRequestNum", "uint"),#
	])
#CBMhEmissiveFog__disclosure : 4165.shdr.src
class CBMhEmissiveFog__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fBaseMapFactor__uiColor", "float4"),#
		("fEmissiveMapFactor__uiColor", "float4"),#
		("fMetalic__uiUNorm", "float"),#
		("fSpecular__uiUNorm", "float"),#
		("fRoughness__uiUNorm", "float"),#
		("align0", "ubyte[4]"),#
		("fUVTransformA", "float4"),#
		("fUVTransformB", "float4"),#
		("fFlowSpeed", "float"),#
		("fFlowSpeedSecondary", "float"),#
		("fFlowStrength", "float"),#
		("fSecondaryFlowStrength", "float"),#
		("fLerpAlpha_BMtoEM__uiUNorm", "float"),#
		("fAlphaEdge", "bbool"),#
		("fToneAlpha__uiUNorm", "float"),#
		("fToneEdge__uiUNorm", "float"),#
		("fEdgeColor__uiColor", "float4"),#
		("fVertexAlpha", "bbool"),#
		("fVolumeBlend__uiSNorm", "float"),#
		("fDotOpacity", "float"),#
		("fDotOpacityFactor", "float"),#
		("bDotInverse", "bbool"),#
		("fNearOpacity", "float"),#
		("fNearOpacityDistance", "float"),#
		("fDiffuseChroma__uiUNorm", "float"),#
		("fSpecularChroma__uiUNorm", "float"),#
		("fInnerOffsetScale", "float"),#
		("fVelocityAttn", "float"),#
		("fNormalDecalBlend__uiUNorm", "float"),#
	])
#CBMhMaterialPLEyeLocal__disclosure : 775.shdr.src
class CBMhMaterialPLEyeLocal__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fBaseMapFactor__uiColor", "float4"),#
		("fEmissiveMapFactor__uiColor", "float3"),#
		("fMetalic__uiUNorm", "float"),#
		("fRoughness__uiUNorm", "float"),#
		("fSpecular__uiUNorm", "float"),#
		("fSubSurfaceBlend__uiUNorm", "float"),#
		("iSubSurfaceProfile", "uint"),#
		("fTranslucency__uiUNorm", "float"),#
		("bBaseColorEmissive", "bbool"),#
		("bBackFaceNormalFilp", "bbool"),#
		("fAnimEmitMin", "float"),#
		("fAnimEmitSpeed", "float"),#
		("fParallaxFactor__uiUNorm", "float"),#
		("fDetailNormalBlend__uiUNorm", "float"),#
		("align0", "ubyte[4]"),#
		("fUVTransformDetailNormal", "float4"),#
	])
#CBMhMaterialEM105Local__disclosure : 99.shdr.src
class CBMhMaterialEM105Local__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fBaseMapFactor__uiColor", "float4"),#
		("fEmissiveMapFactor__uiColor", "float3"),#
		("fMetalic__uiUNorm", "float"),#
		("fRoughness__uiUNorm", "float"),#
		("fSpecular__uiUNorm", "float"),#
		("fSubSurfaceBlend__uiUNorm", "float"),#
		("iSubSurfaceProfile", "uint"),#
		("fTranslucency__uiUNorm", "float"),#
		("bBaseColorEmissive", "bbool"),#
		("fPaintUVTile", "float2"),#
		("fAddNormalBlend__uiUNorm", "float"),#
		("align0", "ubyte[12]"),#
		("fAddNormalMaskA__uiSNorm", "float4"),#
		("fAddNormalMaskB__uiSNorm", "float4"),#
		("fAddNormalMaskC__uiUNorm", "float"),#
		("fAddNormalMaskD__uiUNorm", "float"),#
		("bBackFaceShading", "bbool"),#
		("align1", "ubyte[4]"),#
		("fBackFaceColor__uiColor", "float4"),#
		("bBackFaceNormalFilp", "bbool"),#
		("fKizuColor__uiColor", "float3"),#
		("bLegendary", "bbool"),#
		("align2", "ubyte[12]"),#
		("fLegendColor__uiColor", "float4"),#
		("fLegendMetalMask__uiUNorm", "float2"),#
		("fLegendRoughness", "float"),#
		("align3", "ubyte[4]"),#
		("fLegendFilm__uiUNorm", "float2"),#
		("fLegendSSSMask__uiUNorm", "float"),#
		("fPartsMaskA__uiUNorm", "float"),#
		("fPartsMaskB__uiUNorm", "float"),#
		("fPartsMaskC__uiUNorm", "float"),#
		("fPartsMaskD__uiUNorm", "float"),#
		("fPartsMaskX__uiUNorm", "float"),#
		("fPartsMaskY__uiUNorm", "float"),#
		("fPartsMaskZ__uiUNorm", "float"),#
		("fPartsMaskW__uiUNorm", "float"),#
		("bUseOffset", "bbool"),#
		("fFlowDirDir__uiDirection", "float3"),#
		("align4", "ubyte[4]"),#
		("fFlowControl__uiUNorm", "float4"),#
		("fFlowTile", "float"),#
		("align5", "ubyte[12]"),#
		("fFlowColor__uiColor", "float4"),#
		("fFlowMatControl__uiUNorm", "float4"),#
		("fMaskBlend__uiUNorm", "float4"),#
		("fMaskBlend_A__uiUNorm", "float2"),#
		("fMaskBlend_B__uiUNorm", "float2"),#
		("fFilmThickness__uiUNorm", "float"),#
		("fFilmBlend__uiUNorm", "float"),#
		("fRefraction__uiUNorm", "float"),#
		("fRefractionBlend__uiUNorm", "float"),#
		("fVPushScale", "float"),#
		("fVPushWave", "float"),#
		("fVPushSpeed", "float"),#
		("align6", "ubyte[4]"),#
		("fVpivot", "float3"),#
		("fInnerOffsetScale", "float"),#
		("fRimAlphaPower__uiSNorm", "float"),#
		("fVolumeBlend__uiSNorm", "float"),#
		("align7", "ubyte[8]"),#
		("fDetailEmissiveControl", "float4"),#
		("fRimTranslucency__uiUNorm", "float"),#
		("fFinWave", "float"),#
		("fFinSpeed", "float"),#
		("align8", "ubyte[4]"),#
		("fFinColor__uiColor", "float3"),#
	])
#CBMhSkyGBuffer : 6666.shdr.src
class CBMhSkyGBuffer  (EPyCStruct):
	fields = OrderedDict([
		("iSkyGBufferId", "uint"),#
	])
#CB_CombinedFilter_ColorCorrect : 6309.shdr.src
class CB_CombinedFilter_ColorCorrect  (EPyCStruct):
	fields = OrderedDict([
		("fDepthNear", "float"),#
		("fDepthFar", "float"),#
		("bHdrExtrapolation", "bbool"),#
		("fHdrIntensityRangeInv", "float"),#
	])
#CBLightShaft : 6749.shdr.src
class CBLightShaft  (EPyCStruct):
	fields = OrderedDict([
		("fModelMat", "float4x4"),#
		("fInvModelMat", "float4x4"),#
		("fExtinctionCoef", "float"),#
		("fRayleighCoef", "float"),#
		("fMieCoef", "float"),#
		("fZAttnStart", "float"),#
		("fZAttnEnd", "float"),#
		("iFlags", "uint"),#
		("fTransparency", "float"),#
		("fReductionScale", "float"),#
		("fMiePhaseK", "float3"),#
	])
#CBMhMaterialEM024Local__disclosure : 354.shdr.src
class CBMhMaterialEM024Local__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fBaseMapFactor__uiColor", "float4"),#
		("fEmissiveMapFactor__uiColor", "float3"),#
		("fMetalic__uiUNorm", "float"),#
		("fRoughness__uiUNorm", "float"),#
		("fSpecular__uiUNorm", "float"),#
		("fSubSurfaceBlend__uiUNorm", "float"),#
		("iSubSurfaceProfile", "uint"),#
		("fTranslucency__uiUNorm", "float"),#
		("bBaseColorEmissive", "bbool"),#
		("fPaintUVTile", "float2"),#
		("fAddNormalBlend__uiUNorm", "float"),#
		("align0", "ubyte[12]"),#
		("fAddNormalMaskA__uiSNorm", "float4"),#
		("fAddNormalMaskB__uiSNorm", "float4"),#
		("fAddNormalMaskC__uiUNorm", "float"),#
		("fAddNormalMaskD__uiUNorm", "float"),#
		("bBackFaceShading", "bbool"),#
		("align1", "ubyte[4]"),#
		("fBackFaceColor__uiColor", "float4"),#
		("bBackFaceNormalFilp", "bbool"),#
		("fKizuColor__uiColor", "float3"),#
		("bLegendary", "bbool"),#
		("align2", "ubyte[12]"),#
		("fLegendColor__uiColor", "float4"),#
		("fLegendMetalMask__uiUNorm", "float2"),#
		("fLegendRoughness", "float"),#
		("align3", "ubyte[4]"),#
		("fLegendFilm__uiUNorm", "float2"),#
		("fLegendSSSMask__uiUNorm", "float"),#
		("fPartsMaskA__uiUNorm", "float"),#
		("fPartsMaskB__uiUNorm", "float"),#
		("fPartsMaskC__uiUNorm", "float"),#
		("fPartsMaskD__uiUNorm", "float"),#
		("fPartsMaskX__uiUNorm", "float"),#
		("fPartsMaskY__uiUNorm", "float"),#
		("fPartsMaskZ__uiUNorm", "float"),#
		("fPartsMaskW__uiUNorm", "float"),#
		("bUseOffset", "bbool"),#
		("fFlowDirDir__uiDirection", "float3"),#
		("align4", "ubyte[4]"),#
		("fFlowControl__uiUNorm", "float4"),#
		("fFlowTile", "float"),#
		("align5", "ubyte[12]"),#
		("fFlowColor__uiColor", "float4"),#
		("fFlowMatControl__uiUNorm", "float4"),#
		("fMaskBlend__uiUNorm", "float4"),#
		("fMaskBlend_A__uiUNorm", "float2"),#
		("fMaskBlend_B__uiUNorm", "float2"),#
		("fFilmThickness__uiUNorm", "float"),#
		("fFilmBlend__uiUNorm", "float"),#
		("fRefraction__uiUNorm", "float"),#
		("fRefractionBlend__uiUNorm", "float"),#
	])
#CBWaterCustom : 5488.shdr.src
class CBWaterCustom  (EPyCStruct):
	fields = OrderedDict([
		("fWaterCustomBaseMapFactor", "float4"),#
		("fWaterCustomBlendBaseMapFactor", "float4"),#
		("fWaterCustomEmissiveMapFactor", "float3"),#
		("align0", "ubyte[4]"),#
		("fWaterCustomCubeMapFactor", "float3"),#
		("align1", "ubyte[4]"),#
		("fWaterCustomBlendCubeMapFactor", "float3"),#
		("fWaterCustomMetallic", "float"),#
		("fWaterCustomRoughness", "float"),#
		("fWaterCustomSpecular", "float"),#
		("align2", "ubyte[8]"),#
		("fWaterCustomUVTransformA", "float4"),#
		("fWaterCustomUVTransformB", "float4"),#
		("fWaterCustomUVOffsetSpeedFactor", "float2"),#
		("fWaterCustomUVOffsetSpeedFactorDetail", "float2"),#
		("fWaterCustomDetailNormalBlend", "float"),#
		("fWaterCustomProjectionNormalBlend", "float"),#
		("fWaterCustomProjectionNormalTileSize", "float2"),#
		("fWaterCustomRefraction", "float"),#
		("fWaterCustomRefractionFactor", "float3"),#
		("fWaterCustomBlendRefractionFactor", "float3"),#
		("fWaterCustomRefractionPow", "float"),#
		("bWaterCustomRefractionScreenFade", "bbool"),#
		("fWaterCustomRefractionTangentNormalBlend", "float"),#
		("fWaterCustomVolumeBlend", "float"),#
		("fWaterCustomFlowStrength", "float"),#
		("fWaterCustomFlowSpeed", "float"),#
		("bWaterCustomAlphaTest", "bbool"),#
		("fWaterCustomAlphaTestRef", "float"),#
		("bWaterCustomAlphaDither", "bbool"),#
		("fWaterCustomFresnelBias", "float"),#
	])
#CBMhMaterialEM036Local__disclosure : 4778.shdr.src
class CBMhMaterialEM036Local__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fBaseMapFactor__uiColor", "float4"),#
		("fEmissiveMapFactor__uiColor", "float3"),#
		("fMetalic__uiUNorm", "float"),#
		("fRoughness__uiUNorm", "float"),#
		("fSpecular__uiUNorm", "float"),#
		("fSubSurfaceBlend__uiUNorm", "float"),#
		("iSubSurfaceProfile", "uint"),#
		("fTranslucency__uiUNorm", "float"),#
		("bBaseColorEmissive", "bbool"),#
		("fPaintUVTile", "float2"),#
		("fAddNormalBlend__uiUNorm", "float"),#
		("align0", "ubyte[12]"),#
		("fAddNormalMaskA__uiSNorm", "float4"),#
		("fAddNormalMaskB__uiSNorm", "float4"),#
		("fAddNormalMaskC__uiUNorm", "float"),#
		("fAddNormalMaskD__uiUNorm", "float"),#
		("bBackFaceShading", "bbool"),#
		("align1", "ubyte[4]"),#
		("fBackFaceColor__uiColor", "float4"),#
		("bBackFaceNormalFilp", "bbool"),#
		("fKizuColor__uiColor", "float3"),#
		("bLegendary", "bbool"),#
		("align2", "ubyte[12]"),#
		("fLegendColor__uiColor", "float4"),#
		("fLegendMetalMask__uiUNorm", "float2"),#
		("fLegendRoughness", "float"),#
		("align3", "ubyte[4]"),#
		("fLegendFilm__uiUNorm", "float2"),#
		("fLegendSSSMask__uiUNorm", "float"),#
		("fPartsMaskA__uiUNorm", "float"),#
		("fPartsMaskB__uiUNorm", "float"),#
		("fPartsMaskC__uiUNorm", "float"),#
		("fPartsMaskD__uiUNorm", "float"),#
		("fPartsMaskX__uiUNorm", "float"),#
		("fPartsMaskY__uiUNorm", "float"),#
		("fPartsMaskZ__uiUNorm", "float"),#
		("fPartsMaskW__uiUNorm", "float"),#
		("bUseOffset", "bbool"),#
		("fFlowDirDir__uiDirection", "float3"),#
		("align4", "ubyte[4]"),#
		("fFlowControl__uiUNorm", "float4"),#
		("fFlowTile", "float"),#
		("align5", "ubyte[12]"),#
		("fFlowColor__uiColor", "float4"),#
		("fFlowMatControl__uiUNorm", "float4"),#
		("fFilmThickness__uiUNorm", "float"),#
		("fFilmBlend__uiUNorm", "float"),#
		("fRefraction__uiUNorm", "float"),#
		("fRefractionBlend__uiUNorm", "float"),#
		("fEmitControl__uiUNorm", "float4"),#
	])
#CBMhMaterialVfxFloodLocal__disclosure : 6529.shdr.src
class CBMhMaterialVfxFloodLocal__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fBaseMapFactor__uiColor", "float3"),#
		("align0", "ubyte[4]"),#
		("fDistortionFactor__uiColor", "float3"),#
		("align1", "ubyte[4]"),#
		("fCubeMapFactor__uiColor", "float3"),#
		("fOpacityFactor", "float"),#
		("fMetalic__uiUNorm", "float"),#
		("fRoughness__uiUNorm", "float"),#
		("fDispFactor", "float"),#
		("align2", "ubyte[4]"),#
		("fUVTransformA", "float4"),#
		("fUVTransformB", "float4"),#
		("fUVTransformC", "float4"),#
		("fVolumeBlend__uiSNorm", "float"),#
		("fSpecularFactor", "float"),#
		("bSceneEnvMap", "bbool"),#
		("fRaflectionAngle__uiSNorm", "float"),#
		("fDistortionAngle", "float"),#
		("fDistortion", "float"),#
		("fTranslucency__uiUNorm", "float"),#
		("fDiffuseChroma__uiUNorm", "float"),#
		("fSpecularChroma__uiUNorm", "float"),#
		("fFlowSpeed", "float"),#
		("fFlowStrength", "float"),#
		("fWhiteWaterPow", "float"),#
		("fWhiteWater", "float"),#
		("fEdgeFoamPow", "float"),#
		("fEdgeFoamFactor", "float"),#
		("bEnableLava", "bbool"),#
		("bEnableAlbedoBlend", "bbool"),#
		("fHeat", "float"),#
		("fInnerOffsetScale", "float"),#
		("fAlbedoBlendPow", "float"),#
		("fAlbedoBlendRate", "float"),#
		("fAlbedoBlendFactor", "float"),#
		("align3", "ubyte[8]"),#
		("fAlbedoBlendVector", "float3"),#
		("fVelocityAttn", "float"),#
		("fNormalDecalBlend__uiUNorm", "float"),#
	])
#CBBloom : 959.shdr.src
class CBBloom  (EPyCStruct):
	fields = OrderedDict([
		("fBloomThreshold", "float"),#
		("fBloomRenormalize", "float"),#
		("bGamutSrgb", "bbool"),#
		("align0", "ubyte[4]"),#
		("fDirtColor", "float4"),#
	])
#CBMhMaterialBurnLocal__disclosure : 5925.shdr.src
class CBMhMaterialBurnLocal__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fBaseMapFactor__uiColor", "float4"),#
		("fEmissiveMapFactor__uiColor", "float3"),#
		("fMetalic__uiUNorm", "float"),#
		("fRoughness__uiUNorm", "float"),#
		("fSpecular__uiUNorm", "float"),#
		("fSubSurfaceBlend__uiUNorm", "float"),#
		("iSubSurfaceProfile", "uint"),#
		("fTranslucency__uiUNorm", "float"),#
		("align0", "ubyte[12]"),#
		("fUVTransformA", "float4"),#
		("fBurnControl__uiUNorm", "float3"),#
		("align1", "ubyte[4]"),#
		("fBurnColor__uiColor", "float3"),#
	])
#CBPrimMaterialOffset : 6432.shdr.src
class CBPrimMaterialOffset  (EPyCStruct):
	fields = OrderedDict([
		("iPrimMaterialOffset", "uint"),#
		("iPrimMaterialCount", "uint"),#
		("_PrimMaterialReserve", "float2"),#
	])
#CBToneMapping : 2387.shdr.src
class CBToneMapping  (EPyCStruct):
	fields = OrderedDict([
		("iToneMapType", "uint"),#
		("bLuminanceVersion", "bbool"),#
		("fShouldStr", "float"),#
		("fLinearStr", "float"),#
		("fIntermediate", "float"),#
		("fS1", "float"),#
		("fS2", "float"),#
		("fS3", "float"),#
		("fS4", "float"),#
		("iLUTSize", "uint"),#
		("bIsLinearToPQ", "bbool"),#
		("bIsPQToLinear", "bbool"),#
		("bEnableColorGrading", "bbool"),#
	])
#CBMhMaterialEM106Local__disclosure : 492.shdr.src
class CBMhMaterialEM106Local__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fBaseMapFactor__uiColor", "float4"),#
		("fEmissiveMapFactor__uiColor", "float3"),#
		("fMetalic__uiUNorm", "float"),#
		("fRoughness__uiUNorm", "float"),#
		("fSpecular__uiUNorm", "float"),#
		("fSubSurfaceBlend__uiUNorm", "float"),#
		("iSubSurfaceProfile", "uint"),#
		("fTranslucency__uiUNorm", "float"),#
		("bBaseColorEmissive", "bbool"),#
		("fPaintUVTile", "float2"),#
		("fAddNormalBlend__uiUNorm", "float"),#
		("align0", "ubyte[12]"),#
		("fAddNormalMaskA__uiSNorm", "float4"),#
		("fAddNormalMaskB__uiSNorm", "float4"),#
		("fAddNormalMaskC__uiUNorm", "float"),#
		("fAddNormalMaskD__uiUNorm", "float"),#
		("bBackFaceShading", "bbool"),#
		("align1", "ubyte[4]"),#
		("fBackFaceColor__uiColor", "float4"),#
		("bBackFaceNormalFilp", "bbool"),#
		("fKizuColor__uiColor", "float3"),#
		("bLegendary", "bbool"),#
		("align2", "ubyte[12]"),#
		("fLegendColor__uiColor", "float4"),#
		("fLegendMetalMask__uiUNorm", "float2"),#
		("fLegendRoughness", "float"),#
		("align3", "ubyte[4]"),#
		("fLegendFilm__uiUNorm", "float2"),#
		("fLegendSSSMask__uiUNorm", "float"),#
		("fPartsMaskA__uiUNorm", "float"),#
		("fPartsMaskB__uiUNorm", "float"),#
		("fPartsMaskC__uiUNorm", "float"),#
		("fPartsMaskD__uiUNorm", "float"),#
		("fPartsMaskX__uiUNorm", "float"),#
		("fPartsMaskY__uiUNorm", "float"),#
		("fPartsMaskZ__uiUNorm", "float"),#
		("fPartsMaskW__uiUNorm", "float"),#
		("bUseOffset", "bbool"),#
		("fFlowDirDir__uiDirection", "float3"),#
		("align4", "ubyte[4]"),#
		("fFlowControl__uiUNorm", "float4"),#
		("fFlowTile", "float"),#
		("align5", "ubyte[12]"),#
		("fFlowColor__uiColor", "float4"),#
		("fFlowMatControl__uiUNorm", "float4"),#
		("fFilmThickness__uiUNorm", "float"),#
		("fFilmBlend__uiUNorm", "float"),#
		("fRefraction__uiUNorm", "float"),#
		("fRefractionBlend__uiUNorm", "float"),#
		("fDetailBlend__uiUNorm", "float4"),#
		("fDetailTile", "float4"),#
		("fDetailA_Color__uiColor", "float4"),#
		("fDetailB_Color__uiColor", "float4"),#
		("fDetailC_Color__uiColor", "float4"),#
		("fDetailD_Color__uiColor", "float4"),#
		("fDetail_Roughness__uiUNorm", "float4"),#
		("fDetail_Metal__uiUNorm", "float4"),#
	])
#CBMhMaterialVfxFakeInnerLocal__disclosure : 591.shdr.src
class CBMhMaterialVfxFakeInnerLocal__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fEmissiveMapFactor__uiColor", "float3"),#
		("align0", "ubyte[4]"),#
		("fUVTransformA", "float4"),#
		("fInnerOffsetScale", "float"),#
		("fRimAlphaPower__uiUNorm", "float"),#
		("fVolumeBlend__uiSNorm", "float"),#
		("align1", "ubyte[4]"),#
		("fUVanimVector", "float2"),#
		("fOpacityFactor", "float"),#
		("bGBufferIdMaskEnable", "bbool"),#
		("iGBufferIdMask", "uint"),#
		("fNormalDecalBlend__uiUNorm", "float"),#
	])
#CBCubeCopy : 6584.shdr.src
class CBCubeCopy  (EPyCStruct):
	fields = OrderedDict([
		("regions", "int4[6]"),#
	])
#CBComputeSkinning : 5199.shdr.src
class CBComputeSkinning  (EPyCStruct):
	fields = OrderedDict([
		("iSrcStride", "uint"),#
		("iSrcOffset", "uint"),#
		("iSrcPositionOffset", "uint"),#
		("iSrcNormalOffset", "uint"),#
		("iSrcWeightsOffset", "uint"),#
		("iSrcJointsOffset", "uint"),#
		("iDestStride", "uint"),#
		("iDestOffset", "uint"),#
		("iDestNormalStride", "uint"),#
		("iDestNormalOffset", "uint"),#
		("iVertexCount", "uint"),#
		("iInstanceID", "uint"),#
	])
#CBWaterModel : 989.shdr.src
class CBWaterModel  (EPyCStruct):
	fields = OrderedDict([
		("fMWorldViewProjMat", "float4x4"),#
		("fMWorldMat", "float4x4"),#
	])
#CBWaterWave : 872.shdr.src
class CBWaterWave  (EPyCStruct):
	fields = OrderedDict([
		("fWorldMat", "float4x4"),#
		("fHeightMapSize", "float2"),#
		("fInvHeightMapSize", "float2"),#
		("fMeshCenter", "float2"),#
		("fTessellationFactor", "float"),#
		("fNoiseWaveAmplitude", "float"),#
		("fNoiseWaveDensity", "float"),#
		("fNoiseWaveSpeed", "float"),#
		("fOverlapRatio", "float2"),#
		("fNoiseWaveBorderX", "float2"),#
		("fNoiseWaveBorderZ", "float2"),#
		("fDistanceBetweenVertices", "float2"),#
		("fWaveDensity", "float"),#
		("fDetailWaveDensity", "float"),#
		("fMeshVerticesDistance", "float2"),#
		("fMaxTexcoord", "float2"),#
		("fElapsedTimeSec", "float"),#
		("iDebugViewType", "int"),#
		("bIsAnimating", "bbool"),#
	])
#CBDevelopFlags : 5195.shdr.src
class CBDevelopFlags  (EPyCStruct):
	fields = OrderedDict([
		("iDispChannel", "int"),#
		("iDispCubeFace", "int"),#
		("iDispMode", "int"),#
		("fDispMipLevel", "float"),#
		("fDispArraySlice", "float"),#
	])
#CBMhMaterialVfxDistDispLocal__disclosure : 5574.shdr.src
class CBMhMaterialVfxDistDispLocal__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fBaseMapFactor__uiColor", "float4"),#
		("fCubeMapFactor__uiColor", "float3"),#
		("align0", "ubyte[4]"),#
		("fDistortionFactor__uiColor", "float3"),#
		("fMetalic__uiUNorm", "float"),#
		("fSpecular__uiUNorm", "float"),#
		("fRoughness__uiUNorm", "float"),#
		("align1", "ubyte[8]"),#
		("fUVTransformA", "float4"),#
		("fUVTransformB", "float4"),#
		("fDisplacementFactor", "float"),#
		("fFlow_Speed", "float"),#
		("fFlow_Strength", "float"),#
		("fNormalFactor__uiUNorm", "float"),#
		("fOpacityFactor", "float"),#
		("fVolumeBlend__uiSNorm", "float"),#
		("fDistortionAngle", "float"),#
		("fDistortion", "float"),#
		("fSpecularFactor", "float"),#
		("fDiffuseChroma__uiUNorm", "float"),#
		("fSpecularChroma__uiUNorm", "float"),#
		("bRefractionEnable", "bbool"),#
		("bVolumeBlendEnable", "bbool"),#
		("fEmissiveBlendColor__uiColor", "float3"),#
		("fEmissiveBlendColorBlend__uiUNorm", "float"),#
		("fEmissiveBlendRimParam", "float3"),#
		("fInnerOffsetScale", "float"),#
		("fVelocityAttn", "float"),#
		("fNormalDecalBlend__uiUNorm", "float"),#
	])
#CBMaterialDebug : 1666.shdr.src
class CBMaterialDebug  (EPyCStruct):
	fields = OrderedDict([
		("iMaterialDebugView", "uint"),#
		("bMaterialDebugZeroCheck", "bbool"),#
		("align0", "ubyte[8]"),#
		("fMaterialDebugColor", "float4"),#
	])
#CBMhMaterialEMGlobal : 99.shdr.src
class CBMhMaterialEMGlobal  (EPyCStruct):
	fields = OrderedDict([
		("fMaterialPaintNum", "uint"),#
		("align0", "ubyte[12]"),#
		("fMaterialPaintType", "uint[8]"),#
		("align1", "ubyte[12]"),#
		("fMaterialPaintColor", "float4[8]"),#
		("fMaterialPaintCapsuleP0", "float4[8]"),#
		("fMaterialPaintCapsuleP1", "float4[8]"),#
		("fMaterialPaintCapsuleR", "float[8]"),#
		("align2", "ubyte[12]"),#
		("fMaterialPaintBlendRange", "float2[8]"),#
		("align3", "ubyte[8]"),#
		("fMaterialPaintEmissive", "float4[8]"),#
		("bMaterialPaintEmissive", "bbool"),#
		("fMaterialWetBlend", "float"),#
		("fMaterialWetRoughness", "float"),#
	])
#CBVR_Debug : 131.shdr.src
class CBVR_Debug  (EPyCStruct):
	fields = OrderedDict([
		("iMode", "uint"),#
	])
#CBMhSky2PS : 6760.shdr.src
class CBMhSky2PS  (EPyCStruct):
	fields = OrderedDict([
		("fSkyGlobalIntensity", "float3"),#
		("align0", "ubyte[4]"),#
		("fSkyStarrySkyMapFactor", "float4"),#
		("fSkySunUVOffset", "float2"),#
		("fSkyGlobalCloudSpeed", "float2"),#
		("fSkyWaterReflectionFactor", "float3"),#
		("fSkyBlend", "float"),#
		("bSkyFog", "bbool"),#
		("fSkyFogBlend", "float"),#
		("bSkyDeGamma", "bbool"),#
		("fGamma", "float"),#
		("iSkyAddress", "uint2"),#
		("fSkySunlightMaskAlpha", "float"),#
		("align1", "ubyte[4]"),#
		("fSkySunlightMaskSize", "float2"),#
		("fSkyTopCloudUVScale0", "float2"),#
		("fSkyTopCloudUVScale1", "float2"),#
		("align2", "ubyte[8]"),#
		("fSkySunlightSkyColor", "float4"),#
		("fSkySunlightSkyMaskSize", "float2"),#
		("fSkyStarThreshold", "float"),#
		("fSkyStarPower", "float"),#
		("fSkyCloudHighlightIntensity", "float"),#
		("fSkyCloudShadowIntensity", "float"),#
		("fSkyCloudContrast", "float"),#
		("align3", "ubyte[4]"),#
		("fSkyBaseMapFactor", "float4"),#
		("fSkyBaseSideCloudUVOffset", "float2"),#
		("fSkyBaseTopCloudUVOffset0", "float2"),#
		("fSkyBaseTopCloudUVOffset1", "float2"),#
		("align4", "ubyte[8]"),#
		("fSkyCloudSpeeds", "float2[4]"),#
		("align5", "ubyte[8]"),#
		("fSkySunCloudHighlightColors", "float4[4]"),#
		("fSkySunCloudShadowColors", "float4[4]"),#
		("fSkyMiddleCloudHighlightColors", "float4[4]"),#
		("fSkyMiddleCloudShadowColors", "float4[4]"),#
		("fSkyBackgroundCloudHighlightColors", "float4[4]"),#
		("fSkyBackgroundCloudShadowColors", "float4[4]"),#
		("fSkyCloudAlpha", "float[4]"),#
		("align6", "ubyte[12]"),#
		("fSkyBlendBaseMapFactor", "float4"),#
		("fSkyBlendSideCloudUVOffset", "float2"),#
		("fSkyBlendTopCloudUVOffset0", "float2"),#
		("fSkyBlendTopCloudUVOffset1", "float2"),#
		("align7", "ubyte[8]"),#
		("fSkyBlendCloudSpeeds", "float2[4]"),#
		("align8", "ubyte[8]"),#
		("fSkyBlendSunCloudHighlightColors", "float4[4]"),#
		("fSkyBlendSunCloudShadowColors", "float4[4]"),#
		("fSkyBlendMiddleCloudHighlightColors", "float4[4]"),#
		("fSkyBlendMiddleCloudShadowColors", "float4[4]"),#
		("fSkyBlendBackgroundCloudHighlightColors", "float4[4]"),#
		("fSkyBlendBackgroundCloudShadowColors", "float4[4]"),#
		("fSkyBlendCloudAlpha", "float[4]"),#
	])
#CBMhMaterialPLSkinLocal__disclosure : 2824.shdr.src
class CBMhMaterialPLSkinLocal__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fBaseMapFactor__uiColor", "float4"),#
		("fEmissiveMapFactor__uiColor", "float3"),#
		("fMetalic__uiUNorm", "float"),#
		("fRoughness__uiUNorm", "float"),#
		("fSpecular__uiUNorm", "float"),#
		("fSubSurfaceBlend__uiUNorm", "float"),#
		("iSubSurfaceProfile", "uint"),#
		("fTranslucency__uiUNorm", "float"),#
		("bBaseColorEmissive", "bbool"),#
		("bBackFaceNormalFilp", "bbool"),#
		("fAnimEmitMin", "float"),#
		("fAnimEmitSpeed", "float"),#
		("fAddColorUV__uiUNorm", "float2"),#
		("bUseCMM", "bbool"),#
		("fAddColorA__uiColor", "float4"),#
		("fDetailNormalBlend__uiUNorm", "float"),#
		("align0", "ubyte[12]"),#
		("fUVTransformDetailNormal", "float4"),#
	])
#CBVignetting : 4073.shdr.src
class CBVignetting  (EPyCStruct):
	fields = OrderedDict([
		("fOffset", "float"),#
		("fPow", "float"),#
		("fEllipticity", "float"),#
		("align0", "ubyte[4]"),#
		("fColor", "float3"),#
	])
#CB_PlantOnSurface : 6660.shdr.src
class CB_PlantOnSurface  (EPyCStruct):
	fields = OrderedDict([
		("fScale", "float3"),#
		("iNumPerTriangle", "uint"),#
		("iTriangleNum", "uint"),#
		("iIndexOffset", "uint"),#
		("fRotRandomize", "float"),#
		("fDirRandomize", "float"),#
		("fScaleRandomize", "float"),#
	])
#CBMhMaterialEM111Local__disclosure : 5362.shdr.src
class CBMhMaterialEM111Local__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fBaseMapFactor__uiColor", "float4"),#
		("fEmissiveMapFactor__uiColor", "float3"),#
		("fMetalic__uiUNorm", "float"),#
		("fRoughness__uiUNorm", "float"),#
		("fSpecular__uiUNorm", "float"),#
		("fSubSurfaceBlend__uiUNorm", "float"),#
		("iSubSurfaceProfile", "uint"),#
		("fTranslucency__uiUNorm", "float"),#
		("bBaseColorEmissive", "bbool"),#
		("fPaintUVTile", "float2"),#
		("fAddNormalBlend__uiUNorm", "float"),#
		("align0", "ubyte[12]"),#
		("fAddNormalMaskA__uiSNorm", "float4"),#
		("fAddNormalMaskB__uiSNorm", "float4"),#
		("fAddNormalMaskC__uiUNorm", "float"),#
		("fAddNormalMaskD__uiUNorm", "float"),#
		("bBackFaceShading", "bbool"),#
		("align1", "ubyte[4]"),#
		("fBackFaceColor__uiColor", "float4"),#
		("bBackFaceNormalFilp", "bbool"),#
		("fKizuColor__uiColor", "float3"),#
		("bLegendary", "bbool"),#
		("align2", "ubyte[12]"),#
		("fLegendColor__uiColor", "float4"),#
		("fLegendMetalMask__uiUNorm", "float2"),#
		("fLegendRoughness", "float"),#
		("align3", "ubyte[4]"),#
		("fLegendFilm__uiUNorm", "float2"),#
		("fLegendSSSMask__uiUNorm", "float"),#
		("fPartsMaskA__uiUNorm", "float"),#
		("fPartsMaskB__uiUNorm", "float"),#
		("fPartsMaskC__uiUNorm", "float"),#
		("fPartsMaskD__uiUNorm", "float"),#
		("fPartsMaskX__uiUNorm", "float"),#
		("fPartsMaskY__uiUNorm", "float"),#
		("fPartsMaskZ__uiUNorm", "float"),#
		("fPartsMaskW__uiUNorm", "float"),#
		("bUseOffset", "bbool"),#
		("fFlowDirDir__uiDirection", "float3"),#
		("align4", "ubyte[4]"),#
		("fFlowControl__uiUNorm", "float4"),#
		("fFlowTile", "float"),#
		("align5", "ubyte[12]"),#
		("fFlowColor__uiColor", "float4"),#
		("fFlowMatControl__uiUNorm", "float4"),#
		("fMaskBlend__uiUNorm", "float4"),#
		("fMaskBlend_A__uiUNorm", "float2"),#
		("fMaskBlend_B__uiUNorm", "float2"),#
		("fFilmThickness__uiUNorm", "float"),#
		("fFilmBlend__uiUNorm", "float"),#
		("fRefraction__uiUNorm", "float"),#
		("fRefractionBlend__uiUNorm", "float"),#
		("fFurParam__uiUNorm", "float4"),#
		("fFurTile", "float"),#
		("bUseFlipUV", "bbool"),#
	])
#CBAtmosphere : 5831.shdr.src
class CBAtmosphere  (EPyCStruct):
	fields = OrderedDict([
		("fLightColor", "float3"),#
		("align0", "ubyte[4]"),#
		("fLightDir", "float3"),#
		("fEarthRadius", "float"),#
		("fHeightOffset", "float"),#
		("fAtmosphereHeight", "float"),#
		("fAtmosphereScaleHeight", "float"),#
		("align1", "ubyte[4]"),#
		("fAtmosphereRayleighK", "float3"),#
		("align2", "ubyte[4]"),#
		("fAtmospherePhaseK", "float3"),#
		("fAerosolEffect", "float"),#
		("fAerosolHeight", "float"),#
		("fAerosolScaleHeight", "float"),#
		("fAerosolMieK", "float"),#
		("fAerosolPhaseK", "float"),#
		("fAerosolEccentricity", "float2"),#
	])
#CBSHDiffuse : 6594.shdr.src
class CBSHDiffuse  (EPyCStruct):
	fields = OrderedDict([
		("fSHDiffuseScale", "float"),#
		("fSHDiffuseScaleInv", "float"),#
		("bSHDiffuseUpsampling", "bbool"),#
	])
#CBWaterDebug : 411.shdr.src
class CBWaterDebug  (EPyCStruct):
	fields = OrderedDict([
		("iWaterDebugMode", "int"),#
	])
#CBMhMaterialEM118Local__disclosure : 6090.shdr.src
class CBMhMaterialEM118Local__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fBaseMapFactor__uiColor", "float4"),#
		("fEmissiveMapFactor__uiColor", "float3"),#
		("fMetalic__uiUNorm", "float"),#
		("fRoughness__uiUNorm", "float"),#
		("fSpecular__uiUNorm", "float"),#
		("fSubSurfaceBlend__uiUNorm", "float"),#
		("iSubSurfaceProfile", "uint"),#
		("fTranslucency__uiUNorm", "float"),#
		("bBaseColorEmissive", "bbool"),#
		("fPaintUVTile", "float2"),#
		("fAddNormalBlend__uiUNorm", "float"),#
		("align0", "ubyte[12]"),#
		("fAddNormalMaskA__uiSNorm", "float4"),#
		("fAddNormalMaskB__uiSNorm", "float4"),#
		("fAddNormalMaskC__uiUNorm", "float"),#
		("fAddNormalMaskD__uiUNorm", "float"),#
		("bBackFaceShading", "bbool"),#
		("align1", "ubyte[4]"),#
		("fBackFaceColor__uiColor", "float4"),#
		("bBackFaceNormalFilp", "bbool"),#
		("fKizuColor__uiColor", "float3"),#
		("bLegendary", "bbool"),#
		("align2", "ubyte[12]"),#
		("fLegendColor__uiColor", "float4"),#
		("fLegendMetalMask__uiUNorm", "float2"),#
		("fLegendRoughness", "float"),#
		("align3", "ubyte[4]"),#
		("fLegendFilm__uiUNorm", "float2"),#
		("fLegendSSSMask__uiUNorm", "float"),#
		("fPartsMaskA__uiUNorm", "float"),#
		("fPartsMaskB__uiUNorm", "float"),#
		("fPartsMaskC__uiUNorm", "float"),#
		("fPartsMaskD__uiUNorm", "float"),#
		("fPartsMaskX__uiUNorm", "float"),#
		("fPartsMaskY__uiUNorm", "float"),#
		("fPartsMaskZ__uiUNorm", "float"),#
		("fPartsMaskW__uiUNorm", "float"),#
		("bUseOffset", "bbool"),#
		("fFlowDirDir__uiDirection", "float3"),#
		("align4", "ubyte[4]"),#
		("fFlowControl__uiUNorm", "float4"),#
		("fFlowTile", "float"),#
		("align5", "ubyte[12]"),#
		("fFlowColor__uiColor", "float4"),#
		("fFlowMatControl__uiUNorm", "float4"),#
		("fMaskBlend__uiUNorm", "float4"),#
		("fMaskBlend_A__uiUNorm", "float2"),#
		("fMaskBlend_B__uiUNorm", "float2"),#
		("fFilmThickness__uiUNorm", "float"),#
		("fFilmBlend__uiUNorm", "float"),#
		("fRefraction__uiUNorm", "float"),#
		("fRefractionBlend__uiUNorm", "float"),#
		("fVAnimV__uiUNorm", "float"),#
		("align6", "ubyte[12]"),#
		("fDisplaceControl", "float4"),#
		("fAnimEmitMin", "float"),#
		("fAnimEmitSpeed", "float"),#
		("fEmitControl__uiUNorm", "float"),#
		("fAlphaTestControl__uiUNorm", "float"),#
	])
#CBMhMaterialVfxSandFallLocal__disclosure : 3862.shdr.src
class CBMhMaterialVfxSandFallLocal__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fBaseMapFactor__uiColor", "float4"),#
		("fCubeMapFactor__uiColor", "float3"),#
		("align0", "ubyte[4]"),#
		("fUVTransformA", "float4"),#
		("fUVTransformB", "float4"),#
		("fAlbedoBlend", "float"),#
		("fOpacityFactor", "float"),#
		("fNormalFactor__uiUNorm", "float"),#
		("fDetailfNormalFactor__uiUNorm", "float"),#
		("fDetailNormalBlend__uiUNorm", "float"),#
		("fRTNormalBlend__uiUNorm", "float"),#
		("fMetalic__uiUNorm", "float"),#
		("fRoughness__uiUNorm", "float"),#
		("fSpecular__uiUNorm", "float"),#
		("fTranslucency__uiUNorm", "float"),#
		("fRaflectionAngle__uiSNorm", "float"),#
		("fFlowSpeed", "float"),#
		("fFlowStrength", "float"),#
		("fUVOffsetSpeed", "float"),#
		("fUVOffsetSpeedFactorA", "float2"),#
		("fUVOffsetSpeedFactorB", "float2"),#
		("fInnerOffsetScale", "float"),#
		("fDispFactor", "float"),#
		("fAdditinalAxis", "float3"),#
		("bSceneEnvMap", "bbool"),#
		("bDisplacement", "bbool"),#
		("bRTBlend", "bbool"),#
	])
#CBMhMaterialEMSLocal__disclosure : 1077.shdr.src
class CBMhMaterialEMSLocal__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fBaseMapFactor__uiColor", "float4"),#
		("fEmissiveMapFactor__uiColor", "float3"),#
		("fMetalic__uiUNorm", "float"),#
		("fRoughness__uiUNorm", "float"),#
		("fSpecular__uiUNorm", "float"),#
		("fSubSurfaceBlend__uiUNorm", "float"),#
		("iSubSurfaceProfile", "uint"),#
		("fTranslucency__uiUNorm", "float"),#
		("align0", "ubyte[12]"),#
		("fUVTransformA", "float4"),#
		("fBaseMapMod__uiUNorm", "float4"),#
		("fBaseMapModLimitMax__uiUNorm", "float4"),#
		("fBaseMapModLimitMin__uiUNorm", "float4"),#
		("fFurParam__uiUNorm", "float4"),#
		("fFurTile", "float"),#
		("fPattern_color__uiColor", "float3"),#
		("fFilmThickness__uiUNorm", "float"),#
		("fFilmBlend__uiUNorm", "float"),#
		("bBaseColorEmissive", "bbool"),#
		("fMummyTile", "float"),#
		("fMummyBlend__uiUNorm", "float2"),#
		("align1", "ubyte[8]"),#
		("fMummyColor__uiColor", "float4"),#
		("fMummyMatControl__uiUNorm", "float4"),#
	])
#CBMhMaterialFakeEyeLocal__disclosure : 2201.shdr.src
class CBMhMaterialFakeEyeLocal__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fBaseMapFactor__uiColor", "float4"),#
		("fEmissiveMapFactor__uiColor", "float3"),#
		("fMetalic__uiUNorm", "float"),#
		("fRoughness__uiUNorm", "float"),#
		("fSpecular__uiUNorm", "float"),#
		("fSubSurfaceBlend__uiUNorm", "float"),#
		("iSubSurfaceProfile", "uint"),#
		("fDetailNormalBlend__uiUNorm", "float"),#
		("align0", "ubyte[12]"),#
		("fUVTransformA", "float4"),#
		("fUVTransformB", "float4"),#
		("fTranslucency__uiUNorm", "float"),#
		("fParallaxFactor__uiUNorm", "float"),#
		("fUV_Blend__uiUNorm", "float"),#
		("bBaseColorEmissive", "bbool"),#
	])
#CB_TemporalAA2 : 878.shdr.src
class CB_TemporalAA2  (EPyCStruct):
	fields = OrderedDict([
		("fBlendRate", "float"),#
		("bVelocityBase", "bbool"),#
		("fSharpenAmount", "float"),#
	])
#CBWater : 4396.shdr.src
class CBWater  (EPyCStruct):
	fields = OrderedDict([
		("cWorldMat", "float4x4"),#
		("cLodEnabled", "bbool"),#
		("cAxisX", "float3"),#
		("cAxisZ", "float3"),#
		("cWorldScaleY", "float"),#
		("cVsSubdivInv", "float"),#
		("cTsSubdivInv", "float"),#
		("cAttenuation", "float"),#
		("cTest", "uint"),#
		("cNumWaveFunctionParam", "uint"),#
	])
#CBPrimitivePick : 999.shdr.src
class CBPrimitivePick  (EPyCStruct):
	fields = OrderedDict([
		("iPrimAddress", "uint2"),#
	])
#CBColorCorrect : 2061.shdr.src
class CBColorCorrect  (EPyCStruct):
	fields = OrderedDict([
		("fMatrix", "float4x4"),#
		("fBlendRate", "float"),#
		("fVignettingOffset", "float"),#
		("fVignettingPow", "float"),#
		("bToneCurve", "bbool"),#
		("bVignetting", "bbool"),#
		("bVignettingEllipse", "bbool"),#
		("fScreenAlpha", "float"),#
	])
#CBMotionBlurReconstruction : 870.shdr.src
class CBMotionBlurReconstruction  (EPyCStruct):
	fields = OrderedDict([
		("iTileSize", "int2"),#
		("uNumSamples", "uint"),#
		("fInvNumSamples", "float"),#
		("fShutterSpeed", "float"),#
		("fFurShutterSpeed", "float"),#
		("fBlurThreshold", "float"),#
		("fHalfPixelSize", "float"),#
		("fMaxTexCoord", "float2"),#
		("iDebugViewType", "int"),#
		("bIsPrevious", "bbool"),#
		("bIsLegacy", "bbool"),#
	])
#CBTest : 6586.shdr.src
class CBTest  (EPyCStruct):
	fields = OrderedDict([
		("fTestParam", "float4"),#
		("fTestDirection", "float3"),#
		("fTestType", "float"),#
		("fTestColor", "float4"),#
		("fDummyColor", "float4"),#
	])
#pix_clear_constants : 6579.shdr.src
class pix_clear_constants  (EPyCStruct):
	fields = OrderedDict([
		("m_color", "float4"),#
	])
#CBFXAAParam : 6431.shdr.src
class CBFXAAParam  (EPyCStruct):
	fields = OrderedDict([
		("fFXAAQualitySubpix", "float"),#
		("fFXAAQualityEdgeThreshold", "float"),#
		("fFXAAQualityEdgeThresholdMin", "float"),#
		("align0", "ubyte[4]"),#
		("fFXAATexOnePitch", "float2"),#
	])
#CBGUINoiseAndFade : 2899.shdr.src
class CBGUINoiseAndFade  (EPyCStruct):
	fields = OrderedDict([
		("fGUINoiseOffset", "float4"),#
		("fGUINoiseAndFadeParam", "float4"),#
		("fGUIFadeColor", "float4"),#
	])
#CBMhSky2VS : 1636.shdr.src
class CBMhSky2VS  (EPyCStruct):
	fields = OrderedDict([
		("fSkyWorld", "float3x4"),#
	])

#CB_CombinedFilter : 6309.shdr.src
class CB_CombinedFilter  (EPyCStruct):
	fields = OrderedDict([
		("bEnableFXAA", "bbool"),#
		("bEnableTemporalAA", "bbool"),#
		("bEnableColorCorrect", "bbool"),#
		("bEnableImagePlane", "bbool"),#
	])
#CBNewDOFFilter2 : 6324.shdr.src
class CBNewDOFFilter2  (EPyCStruct):
	fields = OrderedDict([
		("coc_bias", "float"),#
		("coc_scale", "float"),#
		("pcoc", "float"),#
		("quad_reduction_threshold", "float"),#
		("quater_resolution_threshold", "float"),#
		("near_blur_scaler", "float"),#
		("depth_adjuist_factor", "float"),#
		("bokeh_intensity_threshold", "float"),#
		("bokeh_shape_factor", "float"),#
		("dof_single_pixel_radius", "float"),#
		("depth_scale_foreground", "float"),#
		("dof_aspect", "float"),#
		("far_ignore", "bbool"),#
		("near_ignore", "bbool"),#
		("far_coef", "float"),#
		("near_coef", "float"),#
		("out_alpha", "float"),#
		("fVignettingOffset", "float"),#
		("fVignettingPow", "float"),#
		("bVignetting", "bbool"),#
		("fVignettingEllipticity", "float"),#
		("fVignettingColor", "float3"),#
	])
#CBSpeedTreeSystem : 5167.shdr.src
class CBSpeedTreeSystem  (EPyCStruct):
	fields = OrderedDict([
		("fSpeedTreeSystemParam", "float4"),#
		("iSpeedTreeSystemParam", "uint3"),#
	])
#CBMhMaterialFakeSphereLocal__disclosure : 6408.shdr.src
class CBMhMaterialFakeSphereLocal__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fBaseMapFactor__uiColor", "float4"),#
		("fEmissiveMapFactor__uiColor", "float3"),#
		("fMetalic__uiUNorm", "float"),#
		("fRoughness__uiUNorm", "float"),#
		("fSpecular__uiUNorm", "float"),#
		("fSubSurfaceBlend__uiUNorm", "float"),#
		("iSubSurfaceProfile", "uint"),#
		("fDetailNormalBlend__uiUNorm", "float"),#
		("align0", "ubyte[12]"),#
		("fUVTransformA", "float4"),#
		("fUVTransformB", "float4"),#
		("fTranslucency__uiUNorm", "float"),#
		("bForwardFog", "bbool"),#
	])
#CBMhMaterialEM044Local__disclosure : 3980.shdr.src
class CBMhMaterialEM044Local__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fBaseMapFactor__uiColor", "float4"),#
		("fEmissiveMapFactor__uiColor", "float3"),#
		("fMetalic__uiUNorm", "float"),#
		("fRoughness__uiUNorm", "float"),#
		("fSpecular__uiUNorm", "float"),#
		("fSubSurfaceBlend__uiUNorm", "float"),#
		("iSubSurfaceProfile", "uint"),#
		("fTranslucency__uiUNorm", "float"),#
		("bBaseColorEmissive", "bbool"),#
		("fPaintUVTile", "float2"),#
		("fAddNormalBlend__uiUNorm", "float"),#
		("align0", "ubyte[12]"),#
		("fAddNormalMaskA__uiSNorm", "float4"),#
		("fAddNormalMaskB__uiSNorm", "float4"),#
		("fAddNormalMaskC__uiUNorm", "float"),#
		("fAddNormalMaskD__uiUNorm", "float"),#
		("bBackFaceShading", "bbool"),#
		("align1", "ubyte[4]"),#
		("fBackFaceColor__uiColor", "float4"),#
		("bBackFaceNormalFilp", "bbool"),#
		("fKizuColor__uiColor", "float3"),#
		("bLegendary", "bbool"),#
		("align2", "ubyte[12]"),#
		("fLegendColor__uiColor", "float4"),#
		("fLegendMetalMask__uiUNorm", "float2"),#
		("fLegendRoughness", "float"),#
		("align3", "ubyte[4]"),#
		("fLegendFilm__uiUNorm", "float2"),#
		("fLegendSSSMask__uiUNorm", "float"),#
		("fPartsMaskA__uiUNorm", "float"),#
		("fPartsMaskB__uiUNorm", "float"),#
		("fPartsMaskC__uiUNorm", "float"),#
		("fPartsMaskD__uiUNorm", "float"),#
		("fPartsMaskX__uiUNorm", "float"),#
		("fPartsMaskY__uiUNorm", "float"),#
		("fPartsMaskZ__uiUNorm", "float"),#
		("fPartsMaskW__uiUNorm", "float"),#
		("bUseOffset", "bbool"),#
		("fFlowDirDir__uiDirection", "float3"),#
		("align4", "ubyte[4]"),#
		("fFlowControl__uiUNorm", "float4"),#
		("fFlowTile", "float"),#
		("align5", "ubyte[12]"),#
		("fFlowColor__uiColor", "float4"),#
		("fFlowMatControl__uiUNorm", "float4"),#
		("fFilmThickness__uiUNorm", "float"),#
		("fFilmBlend__uiUNorm", "float"),#
		("fRefraction__uiUNorm", "float"),#
		("fRefractionBlend__uiUNorm", "float"),#
	])
#CBMhSky2Sun : 3581.shdr.src
class CBMhSky2Sun  (EPyCStruct):
	fields = OrderedDict([
		("fRotMatrix", "float4x4"),#
		("fSize", "float2"),#
		("fIntensity", "float"),#
		("align0", "ubyte[4]"),#
		("fSkySunMapFactor", "float4"),#
		("fBloomThreshold", "float"),#
		("bSkySunIsRenderingWater", "bbool"),#
		("align1", "ubyte[8]"),#
		("fSkySunWaterReflectionFactor", "float3"),#
		("fBloomTransparencyCoefficient", "float"),#
		("iRenderTargetSize", "uint2"),#
	])
#CBSpeedTreeCollision__disclosure : 5167.shdr.src
class CBSpeedTreeCollision__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fLocalHeightAdjust", "float"),#
		("fLocalWindOverallFactor", "float"),#
		("fLocalWindBranchlFactor", "float"),#
		("fLocalWindLeafFactor", "float"),#
		("fFacingLeavesShadowFactor__uiUNorm", "float"),#
		("fWindOneSidedBias", "float"),#
		("bWindOneSidedUvFlip", "bbool"),#
		("bSpeedTreeLodSmooth", "bbool"),#
	])
#CBMhSkyLpPS : 3292.shdr.src
class CBMhSkyLpPS  (EPyCStruct):
	fields = OrderedDict([
		("fSkyGlobalIntensity", "float3"),#
		("align0", "ubyte[4]"),#
		("fSkySunMapFactor", "float4"),#
		("fSkyStarrySkyMapFactor", "float4"),#
		("fSkySunUVOffset", "float2"),#
		("fSkyGlobalCloudSpeed", "float2"),#
		("fSkyWaterReflectionFactor", "float3"),#
		("fSkyBlend", "float"),#
		("bSkyIsRenderingWater", "bbool"),#
		("bSkyFog", "bbool"),#
		("align1", "ubyte[8]"),#
		("fSkyBaseMapFactor", "float4"),#
		("fSkyCloudMapFactor0", "float4"),#
		("fSkyCloudMapFactor1", "float4"),#
		("fSkyCloudMapFactor2", "float4"),#
		("fSkyCloudMapFactor3", "float4"),#
		("fSkyCloudSpeed0", "float2"),#
		("fSkyCloudSpeed1", "float2"),#
		("fSkyCloudSpeed2", "float2"),#
		("fSkyCloudSpeed3", "float2"),#
		("fSkyBlendBaseMapFactor", "float4"),#
		("fSkyBlendCloudMapFactor0", "float4"),#
		("fSkyBlendCloudMapFactor1", "float4"),#
		("fSkyBlendCloudMapFactor2", "float4"),#
		("fSkyBlendCloudMapFactor3", "float4"),#
		("fSkyBlendCloudSpeed0", "float2"),#
		("fSkyBlendCloudSpeed1", "float2"),#
		("fSkyBlendCloudSpeed2", "float2"),#
		("fSkyBlendCloudSpeed3", "float2"),#
		("iSkyAddress", "uint2"),#
	])
#CBDepthColor : 5198.shdr.src
class CBDepthColor  (EPyCStruct):
	fields = OrderedDict([
		("fDepthColorBlendMode", "uint"),#
		("fDepthColorBlendRate", "float"),#
		("align0", "ubyte[8]"),#
		("fDepthColorColor", "float3"),#
		("fDepthColorDistanceStart", "float"),#
		("fDepthColorDistanceEnd", "float"),#
		("align1", "ubyte[12]"),#
		("fDepthColorBlendCurve", "float[256]"),#
	])
#CBLightShaft_LightParam : 1892.shdr.src
class CBLightShaft_LightParam  (EPyCStruct):
	fields = OrderedDict([
		("fLightShaftPosition", "float3"),#
		("fLightShaftBoundingRadius", "float"),#
		("fLightShaftDirection", "float3"),#
		("fLightShaftFalloff", "float"),#
		("fLightShaftAttenuation", "float4"),#
		("fLightShaftColor", "float3"),#
		("fLightShaftMisc", "uint"),#
		("fLightShaftMinRoughness", "float"),#
		("fLightShaftPadding", "uint3"),#
		("fLightShaftShadowMat", "float4x4"),#
		("fLightShaftShadowExtra", "float4"),#
		("fLightShaftShadowMapSize", "uint"),#
		("fLightShaftShadowMapRegion", "uint3"),#
	])
#CBMhMaterialEM109Local__disclosure : 2333.shdr.src
class CBMhMaterialEM109Local__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fBaseMapFactor__uiColor", "float4"),#
		("fEmissiveMapFactor__uiColor", "float3"),#
		("fMetalic__uiUNorm", "float"),#
		("fRoughness__uiUNorm", "float"),#
		("fSpecular__uiUNorm", "float"),#
		("fSubSurfaceBlend__uiUNorm", "float"),#
		("iSubSurfaceProfile", "uint"),#
		("fTranslucency__uiUNorm", "float"),#
		("bBaseColorEmissive", "bbool"),#
		("fPaintUVTile", "float2"),#
		("fAddNormalBlend__uiUNorm", "float"),#
		("align0", "ubyte[12]"),#
		("fAddNormalMaskA__uiSNorm", "float4"),#
		("fAddNormalMaskB__uiSNorm", "float4"),#
		("fAddNormalMaskC__uiUNorm", "float"),#
		("fAddNormalMaskD__uiUNorm", "float"),#
		("bBackFaceShading", "bbool"),#
		("align1", "ubyte[4]"),#
		("fBackFaceColor__uiColor", "float4"),#
		("bBackFaceNormalFilp", "bbool"),#
		("fKizuColor__uiColor", "float3"),#
		("bLegendary", "bbool"),#
		("align2", "ubyte[12]"),#
		("fLegendColor__uiColor", "float4"),#
		("fLegendMetalMask__uiUNorm", "float2"),#
		("fLegendRoughness", "float"),#
		("align3", "ubyte[4]"),#
		("fLegendFilm__uiUNorm", "float2"),#
		("fLegendSSSMask__uiUNorm", "float"),#
		("fPartsMaskA__uiUNorm", "float"),#
		("fPartsMaskB__uiUNorm", "float"),#
		("fPartsMaskC__uiUNorm", "float"),#
		("fPartsMaskD__uiUNorm", "float"),#
		("fPartsMaskX__uiUNorm", "float"),#
		("fPartsMaskY__uiUNorm", "float"),#
		("fPartsMaskZ__uiUNorm", "float"),#
		("fPartsMaskW__uiUNorm", "float"),#
		("bUseOffset", "bbool"),#
		("fFlowDirDir__uiDirection", "float3"),#
		("align4", "ubyte[4]"),#
		("fFlowControl__uiUNorm", "float4"),#
		("fFlowTile", "float"),#
		("align5", "ubyte[12]"),#
		("fFlowColor__uiColor", "float4"),#
		("fFlowMatControl__uiUNorm", "float4"),#
		("fDisplaceControl", "float4"),#
		("fFurParam__uiUNorm", "float4"),#
		("fFurTile", "float"),#
		("fDispSpeed", "float"),#
		("fFilmThickness__uiUNorm", "float"),#
		("fFilmBlend__uiUNorm", "float"),#
		("fRefraction__uiUNorm", "float"),#
		("fRefractionBlend__uiUNorm", "float"),#
		("bUseBlendDisplace", "bbool"),#
		("fVAnimV__uiUNorm", "float"),#
		("fVAnimPosScale", "float"),#
		("bInvertX", "bbool"),#
	])
#CBGodRaysIterator : 4422.shdr.src
class CBGodRaysIterator  (EPyCStruct):
	fields = OrderedDict([
		("fGodRayParams", "float4[8]"),#
	])
#CBMhMaterialVfxDistDispWLocal__disclosure : 957.shdr.src
class CBMhMaterialVfxDistDispWLocal__disclosure  (EPyCStruct):
	fields = OrderedDict([
		("fBaseMapFactor__uiColor", "float4"),#
		("fCubeMapFactor__uiColor", "float3"),#
		("align0", "ubyte[4]"),#
		("fDistortionFactor__uiColor", "float3"),#
		("fMetalic__uiUNorm", "float"),#
		("fSpecular__uiUNorm", "float"),#
		("fRoughness__uiUNorm", "float"),#
		("align1", "ubyte[8]"),#
		("fUVTransformA", "float4"),#
		("fUVTransformB", "float4"),#
		("fDisplacementFactor", "float"),#
		("fFlow_Speed", "float"),#
		("fFlow_Strength", "float"),#
		("fNormalFactor__uiUNorm", "float"),#
		("fOpacityFactor", "float"),#
		("fVolumeBlend__uiSNorm", "float"),#
		("fDistortionAngle", "float"),#
		("fDistortion", "float"),#
		("fSpecularFactor", "float"),#
		("fDiffuseChroma__uiUNorm", "float"),#
		("fSpecularChroma__uiUNorm", "float"),#
		("bRefractionEnable", "bbool"),#
		("bVolumeBlendEnable", "bbool"),#
		("fEmissiveBlendColor__uiColor", "float3"),#
		("fEmissiveBlendColorBlend__uiUNorm", "float"),#
		("fEmissiveBlendRimParam", "float3"),#
		("fInnerOffsetScale", "float"),#
		("fDisplacementFactorW", "float"),#
		("align2", "ubyte[8]"),#
		("fMudDir__uiDirection", "float3"),#
		("bWorldPosOffsetScale", "bbool"),#
		("fVelocityAttn", "float"),#
		("fNormalDecalBlend__uiUNorm", "float"),#
	])
#CBBloomSample : 1608.shdr.src
class CBBloomSample  (EPyCStruct):
	fields = OrderedDict([
		("fBloomFilterRegion", "float4"),#
	])
#CBPrimitiveMetaDataOcclusion : 4078.shdr.src
class CBPrimitiveMetaDataOcclusion  (EPyCStruct):
	fields = OrderedDict([
		("fPrimOcclusionSphere", "float4"),#
	])
    
#CBSpeedTreeLocalWindPF : 5123.shdr.src
class CBSpeedTreeLocalWindPF_SpeedTreeLocalWind   (EPyCStruct):
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

#CBSpeedTreeGlobalWind : 5167.shdr.src	
class CBSpeedTreeGlobalWind_SpeedTreeGlobalWind   (EPyCStruct):
	fields = OrderedDict([
		("fBillboardTexCoords", "uint4x4"),
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

#CBLightParameters : 996.shdr.src
class CBLightParameters_LightParameter   (Mod3Container):
	fields = OrderedDict([
		("position", "float3"),
		("boundingRadius", "float"),
		("direction", "float3"),
		("falloff", "float"),
		("attenuation", "float4"),
		("color", "float3"),
		("misc", "uint"),
		("min_roughness", "float"),
		("padding", "uint3"),
		("shadow_mat", "float4x4"),
		("texproj_mat", "float4x4"),
		("shadow_extra", "float4"),
		("shadowmap_size", "uint"),
		("shadowmap_region", "uint3"),
  ])
class CBLightParameters  (Mod3Container):
	Mod3Class = CBLightParameters_LightParameter
	baseCount = 256	

#CBSpeedTreeGlobalWindPF : 5123.shdr.src
class CBSpeedTreeGlobalWindPF_SpeedTreeGlobalWind   (EPyCStruct):
	fields = OrderedDict([
		("fBillboardTexCoords", "uint4x4"),
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
	
#CBVRVolumeParams : 977.shdr.src
class CBVRVolumeParams_VolumeParam   (EPyCStruct):
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
class CBVRVolumeParams_Constant   (EPyCStruct):
	fields = OrderedDict([
		("limits", "float3"),
		("extra", "uint"),
  ])
class CBVRVolumeParams_Cuboid   (EPyCStruct):
	fields = OrderedDict([
		("model", "float4x4"),
		("modelI", "float4x4"),
		("minAABB", "float4"),
		("maxAABB", "float4"),
  ])
class CBVRVolumeParams_Spherical   (EPyCStruct):
	fields = OrderedDict([
		("model", "float4x4"),
		("modelI", "float4x4"),
		("extra", "uint4"),
  ])
class CBVRVolumeParams_Spotlight   (EPyCStruct):
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

#CBSpeedTreeLocalWind : 5167.shdr.src
class CBSpeedTreeLocalWind_SpeedTreeLocalWind   (EPyCStruct):
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
    
class dummyShader(EPyCStruct):
    fields = OrderedDict([])
    
shaderListing = 	{"CBAmbientOccluder":CBAmbientOccluder,
	"CBAmbientOcclusion":CBAmbientOcclusion,
	"CBAtmosphere":CBAtmosphere,
	"CBBitonicSort":CBBitonicSort,
	"CBBloom":CBBloom,
	"CBBloomSample":CBBloomSample,
	"CBBokehComposite":CBBokehComposite,
	"CBCSClear":CBCSClear,
	"CBColorCorrect":CBColorCorrect,
	"CBColorCorrectCube":CBColorCorrectCube,
	"CBColorCorrectToneCurve":CBColorCorrectToneCurve,
	"CBComputeSkinning":CBComputeSkinning,
	"CBConstant":CBConstant,
	"CBConstantHaltonSequence":CBConstantHaltonSequence,
	"CBCubeBlend":CBCubeBlend,
	"CBCubeCopy":CBCubeCopy,
	"CBDOFFilter":CBDOFFilter,
	"CBDebug":CBDebug,
	"CBDecal":CBDecal,
	"CBDecalCommon":CBDecalCommon,
	"CBDepthColor":CBDepthColor,
	"CBDevelopColorPick":CBDevelopColorPick,
	"CBDevelopFlags":CBDevelopFlags,
	"CBErrorUnit":CBErrorUnit,
	"CBFXAAParam":CBFXAAParam,
	"CBFilter":CBFilter,
	"CBFilter2":CBFilter2,
	"CBFog":CBFog,
	"CBGUIDevelop":CBGUIDevelop,
	"CBGUIDistanceField":CBGUIDistanceField,
	"CBGUIGBuffer":CBGUIGBuffer,
	"CBGUIGlobal":CBGUIGlobal,
	"CBGUIIcon":CBGUIIcon,
	"CBGUINoiseAndFade":CBGUINoiseAndFade,
	"CBGaussian":CBGaussian,
	"CBGlobalIllumination":CBGlobalIllumination,
	"CBGodRaysConfiguration":CBGodRaysConfiguration,
	"CBGodRaysFilter":CBGodRaysFilter,
	"CBGodRaysIterator":CBGodRaysIterator,
	"CBHazeFilter":CBHazeFilter,
	"CBHeightToNormal":CBHeightToNormal,
	"CBHermiteCurve":CBHermiteCurve,
	"CBHermiteCurveRGB":CBHermiteCurveRGB,
	"CBImagePlane":CBImagePlane,
	"CBImagePlane2":CBImagePlane2,
	"CBInstancing":CBInstancing,
	"CBLGTPRBDebug":CBLGTPRBDebug,
	"CBLGTPRBGen":CBLGTPRBGen,
	"CBLUTBlending":CBLUTBlending,
	"CBLUTMaking":CBLUTMaking,
	"CBLight":CBLight,
	"CBLightParameters":CBLightParameters,
	"CBLightParameters_LightParameter":CBLightParameters_LightParameter,
	"CBLightProbes":CBLightProbes,
	"CBLightShaft":CBLightShaft,
	"CBLightShaft_LightParam":CBLightShaft_LightParam,
	"CBLuminance":CBLuminance,
	"CBLuminanceDebugDisp":CBLuminanceDebugDisp,
	"CBMaterialCommon__disclosure":CBMaterialCommon__disclosure,
	"CBMaterialDebug":CBMaterialDebug,
	"CBMhDecal":CBMhDecal,
	"CBMhDecalSM":CBMhDecalSM,
	"CBMhEmissiveFog__disclosure":CBMhEmissiveFog__disclosure,
	"CBMhMaterialBurnLocal__disclosure":CBMhMaterialBurnLocal__disclosure,
	"CBMhMaterialEC021Local__disclosure":CBMhMaterialEC021Local__disclosure,
	"CBMhMaterialEM002Local__disclosure":CBMhMaterialEM002Local__disclosure,
	"CBMhMaterialEM011Local__disclosure":CBMhMaterialEM011Local__disclosure,
	"CBMhMaterialEM024Local__disclosure":CBMhMaterialEM024Local__disclosure,
	"CBMhMaterialEM036Local__disclosure":CBMhMaterialEM036Local__disclosure,
	"CBMhMaterialEM044Local__disclosure":CBMhMaterialEM044Local__disclosure,
	"CBMhMaterialEM100Local__disclosure":CBMhMaterialEM100Local__disclosure,
	"CBMhMaterialEM102Local__disclosure":CBMhMaterialEM102Local__disclosure,
	"CBMhMaterialEM103Local__disclosure":CBMhMaterialEM103Local__disclosure,
	"CBMhMaterialEM105Local__disclosure":CBMhMaterialEM105Local__disclosure,
	"CBMhMaterialEM106Local__disclosure":CBMhMaterialEM106Local__disclosure,
	"CBMhMaterialEM109Local__disclosure":CBMhMaterialEM109Local__disclosure,
	"CBMhMaterialEM111Local__disclosure":CBMhMaterialEM111Local__disclosure,
	"CBMhMaterialEM115Local__disclosure":CBMhMaterialEM115Local__disclosure,
	"CBMhMaterialEM117Local__disclosure":CBMhMaterialEM117Local__disclosure,
	"CBMhMaterialEM118Local__disclosure":CBMhMaterialEM118Local__disclosure,
	"CBMhMaterialEMGlobal":CBMhMaterialEMGlobal,
	"CBMhMaterialEMLocal__disclosure":CBMhMaterialEMLocal__disclosure,
	"CBMhMaterialEMSLocal__disclosure":CBMhMaterialEMSLocal__disclosure,
	"CBMhMaterialFakeEyeLocal__disclosure":CBMhMaterialFakeEyeLocal__disclosure,
	"CBMhMaterialFakeInnerEmitLocal__disclosure":CBMhMaterialFakeInnerEmitLocal__disclosure,
	"CBMhMaterialFakeLensLocal__disclosure":CBMhMaterialFakeLensLocal__disclosure,
	"CBMhMaterialFakeRefractionLocal__disclosure":CBMhMaterialFakeRefractionLocal__disclosure,
	"CBMhMaterialFakeSphereLocal__disclosure":CBMhMaterialFakeSphereLocal__disclosure,
	"CBMhMaterialFlagWaveLocal__disclosure":CBMhMaterialFlagWaveLocal__disclosure,
	"CBMhMaterialFlowDirLocal__disclosure":CBMhMaterialFlowDirLocal__disclosure,
	"CBMhMaterialFlowLavaLocal__disclosure":CBMhMaterialFlowLavaLocal__disclosure,
	"CBMhMaterialFurLocal__disclosure":CBMhMaterialFurLocal__disclosure,
	"CBMhMaterialGlobal":CBMhMaterialGlobal,
	"CBMhMaterialIvyFloor":CBMhMaterialIvyFloor,
	"CBMhMaterialIvyFloorLocal__disclosure":CBMhMaterialIvyFloorLocal__disclosure,
	"CBMhMaterialLandscapeFlowLocal__disclosure":CBMhMaterialLandscapeFlowLocal__disclosure,
	"CBMhMaterialLandscapeLocal__disclosure":CBMhMaterialLandscapeLocal__disclosure,
	"CBMhMaterialNPCEditFaceLocal__disclosure":CBMhMaterialNPCEditFaceLocal__disclosure,
	"CBMhMaterialNPCEyeLocal__disclosure":CBMhMaterialNPCEyeLocal__disclosure,
	"CBMhMaterialNPCFaceLocal__disclosure":CBMhMaterialNPCFaceLocal__disclosure,
	"CBMhMaterialNPCHairLocal__disclosure":CBMhMaterialNPCHairLocal__disclosure,
	"CBMhMaterialNPCLocal__disclosure":CBMhMaterialNPCLocal__disclosure,
	"CBMhMaterialNPCSkinLocal__disclosure":CBMhMaterialNPCSkinLocal__disclosure,
	"CBMhMaterialNikuLocal__disclosure":CBMhMaterialNikuLocal__disclosure,
	"CBMhMaterialPLEditFaceLocal__disclosure":CBMhMaterialPLEditFaceLocal__disclosure,
	"CBMhMaterialPLEyeLocal__disclosure":CBMhMaterialPLEyeLocal__disclosure,
	"CBMhMaterialPLHairLocal__disclosure":CBMhMaterialPLHairLocal__disclosure,
	"CBMhMaterialPLLocal__disclosure":CBMhMaterialPLLocal__disclosure,
	"CBMhMaterialPLSkinLocal__disclosure":CBMhMaterialPLSkinLocal__disclosure,
	"CBMhMaterialScrWaterLocal__disclosure":CBMhMaterialScrWaterLocal__disclosure,
	"CBMhMaterialSimpleLocal__disclosure":CBMhMaterialSimpleLocal__disclosure,
	"CBMhMaterialSpeedTreeStdBlendLocal__disclosure":CBMhMaterialSpeedTreeStdBlendLocal__disclosure,
	"CBMhMaterialSpeedTreeStdLocal__disclosure":CBMhMaterialSpeedTreeStdLocal__disclosure,
	"CBMhMaterialStdBlendLocal__disclosure":CBMhMaterialStdBlendLocal__disclosure,
	"CBMhMaterialStdLocal__disclosure":CBMhMaterialStdLocal__disclosure,
	"CBMhMaterialUberLocal__disclosure":CBMhMaterialUberLocal__disclosure,
	"CBMhMaterialVfxDebufBodyLocal__disclosure":CBMhMaterialVfxDebufBodyLocal__disclosure,
	"CBMhMaterialVfxDispWaveLocal__disclosure":CBMhMaterialVfxDispWaveLocal__disclosure,
	"CBMhMaterialVfxDistDispLocal__disclosure":CBMhMaterialVfxDistDispLocal__disclosure,
	"CBMhMaterialVfxDistDispWLocal__disclosure":CBMhMaterialVfxDistDispWLocal__disclosure,
	"CBMhMaterialVfxFakeInnerLocal__disclosure":CBMhMaterialVfxFakeInnerLocal__disclosure,
	"CBMhMaterialVfxFloodLocal__disclosure":CBMhMaterialVfxFloodLocal__disclosure,
	"CBMhMaterialVfxSandFallLocal__disclosure":CBMhMaterialVfxSandFallLocal__disclosure,
	"CBMhMaterialVfxTornadoLocal__disclosure":CBMhMaterialVfxTornadoLocal__disclosure,
	"CBMhMaterialVfxWaterLocal__disclosure":CBMhMaterialVfxWaterLocal__disclosure,
	"CBMhMaterialVfxWave":CBMhMaterialVfxWave,
	"CBMhMaterialVfxWaveLocal__disclosure":CBMhMaterialVfxWaveLocal__disclosure,
	"CBMhMaterial_EM105_EVCLocal__disclosure":CBMhMaterial_EM105_EVCLocal__disclosure,
	"CBMhSky2GBuffer":CBMhSky2GBuffer,
	"CBMhSky2PS":CBMhSky2PS,
	"CBMhSky2Sun":CBMhSky2Sun,
	"CBMhSky2VS":CBMhSky2VS,
	"CBMhSkyGBuffer":CBMhSkyGBuffer,
	"CBMhSkyLpPS":CBMhSkyLpPS,
	"CBMhSkyPS":CBMhSkyPS,
	"CBMhSkyVS":CBMhSkyVS,
	"CBModel":CBModel,
	"CBMotionBlur":CBMotionBlur,
	"CBMotionBlurReconstruction":CBMotionBlurReconstruction,
	"CBNewDOFFilter":CBNewDOFFilter,
	"CBNewDOFFilter2":CBNewDOFFilter2,
	"CBNormalMerge":CBNormalMerge,
	"CBNormalRecalc":CBNormalRecalc,
	"CBOutline":CBOutline,
	"CBPartialColor":CBPartialColor,
	"CBPick":CBPick,
	"CBPrimCopyState":CBPrimCopyState,
	"CBPrimGpuSystem":CBPrimGpuSystem,
	"CBPrimMaterialOffset":CBPrimMaterialOffset,
	"CBPrimSystem":CBPrimSystem,
	"CBPrimVertexOffset":CBPrimVertexOffset,
	"CBPrimitive":CBPrimitive,
	"CBPrimitiveDebug":CBPrimitiveDebug,
	"CBPrimitiveEx":CBPrimitiveEx,
	"CBPrimitiveMetaDataOcclusion":CBPrimitiveMetaDataOcclusion,
	"CBPrimitivePick":CBPrimitivePick,
	"CBROPTest":CBROPTest,
	"CBRadialBlurFilter":CBRadialBlurFilter,
	"CBRadialBlurFunction":CBRadialBlurFunction,
	"CBRenderFrame":CBRenderFrame,
	"CBResample":CBResample,
	"CBSHDiffuse":CBSHDiffuse,
	"CBSSLR":CBSSLR,
	"CBSSSSS":CBSSSSS,
	"CBSSSSS_Profile":CBSSSSS_Profile,
	"CBScreen":CBScreen,
	"CBSky":CBSky,
	"CBSpeedTree":CBSpeedTree,
	"CBSpeedTreeCollision__disclosure":CBSpeedTreeCollision__disclosure,
	"CBSpeedTreeGlobalWind":CBSpeedTreeGlobalWind,
	"CBSpeedTreeGlobalWindPF":CBSpeedTreeGlobalWindPF,
	"CBSpeedTreeGlobalWindPF_SpeedTreeGlobalWind":CBSpeedTreeGlobalWindPF_SpeedTreeGlobalWind,
	"CBSpeedTreeGlobalWind_SpeedTreeGlobalWind":CBSpeedTreeGlobalWind_SpeedTreeGlobalWind,
	"CBSpeedTreeLocalWind":CBSpeedTreeLocalWind,
	"CBSpeedTreeLocalWindPF":CBSpeedTreeLocalWindPF,
	"CBSpeedTreeLocalWindPF_SpeedTreeLocalWind":CBSpeedTreeLocalWindPF_SpeedTreeLocalWind,
	"CBSpeedTreeLocalWind_SpeedTreeLocalWind":CBSpeedTreeLocalWind_SpeedTreeLocalWind,
	"CBSpeedTreePrimitiveInfo":CBSpeedTreePrimitiveInfo,
	"CBSpeedTreeSystem":CBSpeedTreeSystem,
	"CBStarrySky":CBStarrySky,
	"CBSystem":CBSystem,
	"CBSystemColor":CBSystemColor,
	"CBTest":CBTest,
	"CBTestLight":CBTestLight,
	"CBToneMapping":CBToneMapping,
	"CBToneMappingSdrSim":CBToneMappingSdrSim,
	"CBTubeLight":CBTubeLight,
	"CBVRCommon":CBVRCommon,
	"CBVRCompute":CBVRCompute,
	"CBVRFilter":CBVRFilter,
	"CBVRGaussian":CBVRGaussian,
	"CBVRRecompute":CBVRRecompute,
	"CBVRVolumeParams":CBVRVolumeParams,
	"CBVRVolumeParams_Constant":CBVRVolumeParams_Constant,
	"CBVRVolumeParams_Cuboid":CBVRVolumeParams_Cuboid,
	"CBVRVolumeParams_Spherical":CBVRVolumeParams_Spherical,
	"CBVRVolumeParams_Spotlight":CBVRVolumeParams_Spotlight,
	"CBVRVolumeParams_VolumeParam":CBVRVolumeParams_VolumeParam,
	"CBVR_Debug":CBVR_Debug,
	"CBViewFrustum":CBViewFrustum,
	"CBViewProjection":CBViewProjection,
	"CBVignetting":CBVignetting,
	"CBWater":CBWater,
	"CBWaterCustom":CBWaterCustom,
	"CBWaterDebug":CBWaterDebug,
	"CBWaterMaterial":CBWaterMaterial,
	"CBWaterModel":CBWaterModel,
	"CBWaterPick":CBWaterPick,
	"CBWaterWave":CBWaterWave,
	"CBWaterWaveMaterial":CBWaterWaveMaterial,
	"CB_BGTexture":CB_BGTexture,
	"CB_CombinedFilter":CB_CombinedFilter,
	"CB_CombinedFilter_ColorCorrect":CB_CombinedFilter_ColorCorrect,
	"CB_CombinedFilter_ImagePlane":CB_CombinedFilter_ImagePlane,
	"CB_PlantOnSurface":CB_PlantOnSurface,
	"CB_TemporalAA":CB_TemporalAA,
	"CB_TemporalAA2":CB_TemporalAA2,
	"SeaDisplacement":SeaDisplacement}

generalhash =  lambda x:  CrcJamcrc.calc(x.encode())
shaderTranslation = {generalhash(key) & 0xFFFFF:shaderListing[key] for key in shaderListing}