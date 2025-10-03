# SNMP MIB module (BWA-DOT11-WLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\alvarion\BWA-DOT11-WLAN-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:17:49 2025
# On host DESKTOP-ORUUBP9 platform Windows version 11 by user speterman
# Using Python version 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

bwaVLMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1)
)
if mibBuilder.loadTexts:
    bwaVLMib.setRevisions(
        ("1907-08-14 11:46",)
    )


# Types definitions



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6





class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Bwa_ObjectIdentity = ObjectIdentity
bwa = _Bwa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1)
)
_BwaVLSysInfo_ObjectIdentity = ObjectIdentity
bwaVLSysInfo = _BwaVLSysInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1)
)


class _BwaVLUnitHwVersion_Type(DisplayString):
    """Custom type bwaVLUnitHwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BwaVLUnitHwVersion_Type.__name__ = "DisplayString"
_BwaVLUnitHwVersion_Object = MibScalar
bwaVLUnitHwVersion = _BwaVLUnitHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 1),
    _BwaVLUnitHwVersion_Type()
)
bwaVLUnitHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLUnitHwVersion.setStatus("current")


class _BwaVLRunningSoftwareVersion_Type(DisplayString):
    """Custom type bwaVLRunningSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BwaVLRunningSoftwareVersion_Type.__name__ = "DisplayString"
_BwaVLRunningSoftwareVersion_Object = MibScalar
bwaVLRunningSoftwareVersion = _BwaVLRunningSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 2),
    _BwaVLRunningSoftwareVersion_Type()
)
bwaVLRunningSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLRunningSoftwareVersion.setStatus("current")


class _BwaVLRunningFrom_Type(Integer32):
    """Custom type bwaVLRunningFrom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mainVersion", 1),
          ("shadowVersion", 2))
    )


_BwaVLRunningFrom_Type.__name__ = "Integer32"
_BwaVLRunningFrom_Object = MibScalar
bwaVLRunningFrom = _BwaVLRunningFrom_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 3),
    _BwaVLRunningFrom_Type()
)
bwaVLRunningFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLRunningFrom.setStatus("current")


class _BwaVLMainVersionNumber_Type(DisplayString):
    """Custom type bwaVLMainVersionNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BwaVLMainVersionNumber_Type.__name__ = "DisplayString"
_BwaVLMainVersionNumber_Object = MibScalar
bwaVLMainVersionNumber = _BwaVLMainVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 4),
    _BwaVLMainVersionNumber_Type()
)
bwaVLMainVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLMainVersionNumber.setStatus("current")


class _BwaVLMainVersionFileName_Type(DisplayString):
    """Custom type bwaVLMainVersionFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BwaVLMainVersionFileName_Type.__name__ = "DisplayString"
_BwaVLMainVersionFileName_Object = MibScalar
bwaVLMainVersionFileName = _BwaVLMainVersionFileName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 5),
    _BwaVLMainVersionFileName_Type()
)
bwaVLMainVersionFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLMainVersionFileName.setStatus("current")


class _BwaVLShadowVersionNumber_Type(DisplayString):
    """Custom type bwaVLShadowVersionNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BwaVLShadowVersionNumber_Type.__name__ = "DisplayString"
_BwaVLShadowVersionNumber_Object = MibScalar
bwaVLShadowVersionNumber = _BwaVLShadowVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 6),
    _BwaVLShadowVersionNumber_Type()
)
bwaVLShadowVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLShadowVersionNumber.setStatus("current")


class _BwaVLShadowVersionFileName_Type(DisplayString):
    """Custom type bwaVLShadowVersionFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BwaVLShadowVersionFileName_Type.__name__ = "DisplayString"
_BwaVLShadowVersionFileName_Object = MibScalar
bwaVLShadowVersionFileName = _BwaVLShadowVersionFileName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 7),
    _BwaVLShadowVersionFileName_Type()
)
bwaVLShadowVersionFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLShadowVersionFileName.setStatus("current")
_BwaVLUnitMacAddress_Type = MacAddress
_BwaVLUnitMacAddress_Object = MibScalar
bwaVLUnitMacAddress = _BwaVLUnitMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 8),
    _BwaVLUnitMacAddress_Type()
)
bwaVLUnitMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLUnitMacAddress.setStatus("current")


class _BwaVLUnitType_Type(Integer32):
    """Custom type bwaVLUnitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("auBS", 1),
          ("auSA", 2),
          ("su-6-1D", 3),
          ("su-6-BD", 4),
          ("su-24-BD", 5),
          ("bu-B14", 6),
          ("bu-B28", 7),
          ("rb-B14", 8),
          ("rb-B28", 9),
          ("su-BD", 10),
          ("su-54-BD", 11),
          ("su-3-1D", 12),
          ("su-3-4D", 13),
          ("ausBS", 14),
          ("ausSA", 15),
          ("auBS4900", 16),
          ("auSA4900", 17),
          ("su4900", 18),
          ("bu-B100", 19),
          ("rb-B100", 20),
          ("su-I", 21),
          ("au-E", 22))
    )


_BwaVLUnitType_Type.__name__ = "Integer32"
_BwaVLUnitType_Object = MibScalar
bwaVLUnitType = _BwaVLUnitType_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 9),
    _BwaVLUnitType_Type()
)
bwaVLUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLUnitType.setStatus("current")
_BwaVLAssociatedAU_Type = MacAddress
_BwaVLAssociatedAU_Object = MibScalar
bwaVLAssociatedAU = _BwaVLAssociatedAU_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 10),
    _BwaVLAssociatedAU_Type()
)
bwaVLAssociatedAU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLAssociatedAU.setStatus("current")
_BwaVLNumOfAssociationsSinceLastReset_Type = Integer32
_BwaVLNumOfAssociationsSinceLastReset_Object = MibScalar
bwaVLNumOfAssociationsSinceLastReset = _BwaVLNumOfAssociationsSinceLastReset_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 11),
    _BwaVLNumOfAssociationsSinceLastReset_Type()
)
bwaVLNumOfAssociationsSinceLastReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLNumOfAssociationsSinceLastReset.setStatus("current")
_BwaVLCurrentNumOfAssociations_Type = Integer32
_BwaVLCurrentNumOfAssociations_Object = MibScalar
bwaVLCurrentNumOfAssociations = _BwaVLCurrentNumOfAssociations_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 13),
    _BwaVLCurrentNumOfAssociations_Type()
)
bwaVLCurrentNumOfAssociations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLCurrentNumOfAssociations.setStatus("current")


class _BwaVLUnitBootVersion_Type(DisplayString):
    """Custom type bwaVLUnitBootVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BwaVLUnitBootVersion_Type.__name__ = "DisplayString"
_BwaVLUnitBootVersion_Object = MibScalar
bwaVLUnitBootVersion = _BwaVLUnitBootVersion_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 14),
    _BwaVLUnitBootVersion_Type()
)
bwaVLUnitBootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLUnitBootVersion.setStatus("current")


class _BwaVLRadioBand_Type(Integer32):
    """Custom type bwaVLRadioBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("band-5-8GHz", 1),
          ("band-5-4GHz", 2),
          ("band-4-9GHz", 3),
          ("band-5-2GHz", 4),
          ("band-2-4GHz", 5),
          ("band-5-3GHz", 6),
          ("band-4-9GHzJapan", 7))
    )


_BwaVLRadioBand_Type.__name__ = "Integer32"
_BwaVLRadioBand_Object = MibScalar
bwaVLRadioBand = _BwaVLRadioBand_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 15),
    _BwaVLRadioBand_Type()
)
bwaVLRadioBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLRadioBand.setStatus("current")


class _BwaVLCurrentEthernetPortState_Type(Integer32):
    """Custom type bwaVLCurrentEthernetPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("halfDuplexAnd10Mbps", 1),
          ("fullDuplexAnd10Mbps", 2),
          ("halfDuplexAnd100Mbps", 3),
          ("fullDuplexAnd100Mbps", 4),
          ("linkDown", 5))
    )


_BwaVLCurrentEthernetPortState_Type.__name__ = "Integer32"
_BwaVLCurrentEthernetPortState_Object = MibScalar
bwaVLCurrentEthernetPortState = _BwaVLCurrentEthernetPortState_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 16),
    _BwaVLCurrentEthernetPortState_Type()
)
bwaVLCurrentEthernetPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLCurrentEthernetPortState.setStatus("current")


class _BwaVLTimeSinceLastReset_Type(DisplayString):
    """Custom type bwaVLTimeSinceLastReset based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BwaVLTimeSinceLastReset_Type.__name__ = "DisplayString"
_BwaVLTimeSinceLastReset_Object = MibScalar
bwaVLTimeSinceLastReset = _BwaVLTimeSinceLastReset_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 17),
    _BwaVLTimeSinceLastReset_Type()
)
bwaVLTimeSinceLastReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLTimeSinceLastReset.setStatus("current")
_BwaVLCountryDependentParameters_ObjectIdentity = ObjectIdentity
bwaVLCountryDependentParameters = _BwaVLCountryDependentParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 18)
)


class _BwaVLCountryCode_Type(DisplayString):
    """Custom type bwaVLCountryCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BwaVLCountryCode_Type.__name__ = "DisplayString"
_BwaVLCountryCode_Object = MibScalar
bwaVLCountryCode = _BwaVLCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 18, 1),
    _BwaVLCountryCode_Type()
)
bwaVLCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLCountryCode.setStatus("current")
_BwaVLCountryDependentParamsTable_Object = MibTable
bwaVLCountryDependentParamsTable = _BwaVLCountryDependentParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 18, 2)
)
if mibBuilder.loadTexts:
    bwaVLCountryDependentParamsTable.setStatus("current")
_BwaVLCountryDependentParameterEntry_Object = MibTableRow
bwaVLCountryDependentParameterEntry = _BwaVLCountryDependentParameterEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 18, 2, 1)
)
bwaVLCountryDependentParameterEntry.setIndexNames(
    (0, "BWA-DOT11-WLAN-MIB", "bwaVLCountryDependentParameterTableIdx"),
)
if mibBuilder.loadTexts:
    bwaVLCountryDependentParameterEntry.setStatus("current")


class _BwaVLCountryDependentParameterTableIdx_Type(Integer32):
    """Custom type bwaVLCountryDependentParameterTableIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_BwaVLCountryDependentParameterTableIdx_Type.__name__ = "Integer32"
_BwaVLCountryDependentParameterTableIdx_Object = MibTableColumn
bwaVLCountryDependentParameterTableIdx = _BwaVLCountryDependentParameterTableIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 18, 2, 1, 1),
    _BwaVLCountryDependentParameterTableIdx_Type()
)
bwaVLCountryDependentParameterTableIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLCountryDependentParameterTableIdx.setStatus("current")
_BwaVLCountryDependentParameterFrequencies_Type = DisplayString
_BwaVLCountryDependentParameterFrequencies_Object = MibTableColumn
bwaVLCountryDependentParameterFrequencies = _BwaVLCountryDependentParameterFrequencies_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 18, 2, 1, 2),
    _BwaVLCountryDependentParameterFrequencies_Type()
)
bwaVLCountryDependentParameterFrequencies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLCountryDependentParameterFrequencies.setStatus("current")
_BwaVLAllowedBandwidth_Type = Integer32
_BwaVLAllowedBandwidth_Object = MibTableColumn
bwaVLAllowedBandwidth = _BwaVLAllowedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 18, 2, 1, 3),
    _BwaVLAllowedBandwidth_Type()
)
bwaVLAllowedBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLAllowedBandwidth.setStatus("current")
_BwaVLRegulationMaxTxPowerAtAntennaPort_Type = Integer32
_BwaVLRegulationMaxTxPowerAtAntennaPort_Object = MibTableColumn
bwaVLRegulationMaxTxPowerAtAntennaPort = _BwaVLRegulationMaxTxPowerAtAntennaPort_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 18, 2, 1, 4),
    _BwaVLRegulationMaxTxPowerAtAntennaPort_Type()
)
bwaVLRegulationMaxTxPowerAtAntennaPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLRegulationMaxTxPowerAtAntennaPort.setStatus("current")
_BwaVLRegulationMaxEIRP_Type = Integer32
_BwaVLRegulationMaxEIRP_Object = MibTableColumn
bwaVLRegulationMaxEIRP = _BwaVLRegulationMaxEIRP_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 18, 2, 1, 5),
    _BwaVLRegulationMaxEIRP_Type()
)
bwaVLRegulationMaxEIRP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLRegulationMaxEIRP.setStatus("current")


class _BwaVLMinModulationLevel_Type(Integer32):
    """Custom type bwaVLMinModulationLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("level1", 1),
          ("level2", 2),
          ("level3", 3),
          ("level4", 4),
          ("level5", 5),
          ("level6", 6),
          ("level7", 7),
          ("level8", 8))
    )


_BwaVLMinModulationLevel_Type.__name__ = "Integer32"
_BwaVLMinModulationLevel_Object = MibTableColumn
bwaVLMinModulationLevel = _BwaVLMinModulationLevel_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 18, 2, 1, 6),
    _BwaVLMinModulationLevel_Type()
)
bwaVLMinModulationLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLMinModulationLevel.setStatus("current")


class _BwaVLMaxModulationLevel_Type(Integer32):
    """Custom type bwaVLMaxModulationLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("level1", 1),
          ("level2", 2),
          ("level3", 3),
          ("level4", 4),
          ("level5", 5),
          ("level6", 6),
          ("level7", 7),
          ("level8", 8))
    )


_BwaVLMaxModulationLevel_Type.__name__ = "Integer32"
_BwaVLMaxModulationLevel_Object = MibTableColumn
bwaVLMaxModulationLevel = _BwaVLMaxModulationLevel_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 18, 2, 1, 7),
    _BwaVLMaxModulationLevel_Type()
)
bwaVLMaxModulationLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLMaxModulationLevel.setStatus("current")


class _BwaVLBurstModeSupport_Type(Integer32):
    """Custom type bwaVLBurstModeSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("notSupported", 2))
    )


_BwaVLBurstModeSupport_Type.__name__ = "Integer32"
_BwaVLBurstModeSupport_Object = MibTableColumn
bwaVLBurstModeSupport = _BwaVLBurstModeSupport_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 18, 2, 1, 8),
    _BwaVLBurstModeSupport_Type()
)
bwaVLBurstModeSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLBurstModeSupport.setStatus("current")
_BwaVLMaximumBurstDuration_Type = Integer32
_BwaVLMaximumBurstDuration_Object = MibTableColumn
bwaVLMaximumBurstDuration = _BwaVLMaximumBurstDuration_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 18, 2, 1, 9),
    _BwaVLMaximumBurstDuration_Type()
)
bwaVLMaximumBurstDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLMaximumBurstDuration.setStatus("current")


class _BwaVLDfsSupport_Type(Integer32):
    """Custom type bwaVLDfsSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("notSupported", 2))
    )


_BwaVLDfsSupport_Type.__name__ = "Integer32"
_BwaVLDfsSupport_Object = MibTableColumn
bwaVLDfsSupport = _BwaVLDfsSupport_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 18, 2, 1, 10),
    _BwaVLDfsSupport_Type()
)
bwaVLDfsSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLDfsSupport.setStatus("current")


class _BwaVLMinimumHwRevision_Type(Integer32):
    """Custom type bwaVLMinimumHwRevision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("hwRevisionA", 1),
          ("hwRevisionB", 2),
          ("hwRevisionC", 3),
          ("hwRevisionD", 4),
          ("hwRevisionE", 5),
          ("na", 255))
    )


_BwaVLMinimumHwRevision_Type.__name__ = "Integer32"
_BwaVLMinimumHwRevision_Object = MibTableColumn
bwaVLMinimumHwRevision = _BwaVLMinimumHwRevision_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 18, 2, 1, 11),
    _BwaVLMinimumHwRevision_Type()
)
bwaVLMinimumHwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLMinimumHwRevision.setStatus("current")


class _BwaVLAuthenticationEncryptionSupport_Type(Integer32):
    """Custom type bwaVLAuthenticationEncryptionSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("notSupported", 2))
    )


_BwaVLAuthenticationEncryptionSupport_Type.__name__ = "Integer32"
_BwaVLAuthenticationEncryptionSupport_Object = MibScalar
bwaVLAuthenticationEncryptionSupport = _BwaVLAuthenticationEncryptionSupport_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 18, 3),
    _BwaVLAuthenticationEncryptionSupport_Type()
)
bwaVLAuthenticationEncryptionSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLAuthenticationEncryptionSupport.setStatus("current")


class _BwaVLDataEncryptionSupport_Type(Integer32):
    """Custom type bwaVLDataEncryptionSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("notSupported", 2))
    )


_BwaVLDataEncryptionSupport_Type.__name__ = "Integer32"
_BwaVLDataEncryptionSupport_Object = MibScalar
bwaVLDataEncryptionSupport = _BwaVLDataEncryptionSupport_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 18, 4),
    _BwaVLDataEncryptionSupport_Type()
)
bwaVLDataEncryptionSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLDataEncryptionSupport.setStatus("current")


class _BwaVLAESEncryptionSupport_Type(Integer32):
    """Custom type bwaVLAESEncryptionSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("notSupported", 2))
    )


_BwaVLAESEncryptionSupport_Type.__name__ = "Integer32"
_BwaVLAESEncryptionSupport_Object = MibScalar
bwaVLAESEncryptionSupport = _BwaVLAESEncryptionSupport_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 18, 5),
    _BwaVLAESEncryptionSupport_Type()
)
bwaVLAESEncryptionSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLAESEncryptionSupport.setStatus("current")


class _BwaVLAntennaGainChange_Type(Integer32):
    """Custom type bwaVLAntennaGainChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("notSupported", 2))
    )


_BwaVLAntennaGainChange_Type.__name__ = "Integer32"
_BwaVLAntennaGainChange_Object = MibScalar
bwaVLAntennaGainChange = _BwaVLAntennaGainChange_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 19),
    _BwaVLAntennaGainChange_Type()
)
bwaVLAntennaGainChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLAntennaGainChange.setStatus("current")


class _BwaVLAteTestResults_Type(Integer32):
    """Custom type bwaVLAteTestResults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("pass", 1),
          ("fail", 2))
    )


_BwaVLAteTestResults_Type.__name__ = "Integer32"
_BwaVLAteTestResults_Object = MibScalar
bwaVLAteTestResults = _BwaVLAteTestResults_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 20),
    _BwaVLAteTestResults_Type()
)
bwaVLAteTestResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLAteTestResults.setStatus("current")


class _BwaVLSerialNumber_Type(DisplayString):
    """Custom type bwaVLSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 35),
    )


_BwaVLSerialNumber_Type.__name__ = "DisplayString"
_BwaVLSerialNumber_Object = MibScalar
bwaVLSerialNumber = _BwaVLSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 1, 21),
    _BwaVLSerialNumber_Type()
)
bwaVLSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLSerialNumber.setStatus("current")
_BwaVLUnitControl_ObjectIdentity = ObjectIdentity
bwaVLUnitControl = _BwaVLUnitControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2)
)


class _BwaVLResetUnit_Type(Integer32):
    """Custom type bwaVLResetUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cancel", 1),
          ("resetSystemNow", 2))
    )


_BwaVLResetUnit_Type.__name__ = "Integer32"
_BwaVLResetUnit_Object = MibScalar
bwaVLResetUnit = _BwaVLResetUnit_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 1),
    _BwaVLResetUnit_Type()
)
bwaVLResetUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLResetUnit.setStatus("current")


class _BwaVLSetDefaults_Type(Integer32):
    """Custom type bwaVLSetDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("noDefaultSettingRequested", 0),
          ("completeFactory", 1),
          ("partialFactory", 2),
          ("completeOperator", 3),
          ("partialOperator", 4),
          ("cancelCurrentPendingRequest", 5))
    )


_BwaVLSetDefaults_Type.__name__ = "Integer32"
_BwaVLSetDefaults_Object = MibScalar
bwaVLSetDefaults = _BwaVLSetDefaults_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 2),
    _BwaVLSetDefaults_Type()
)
bwaVLSetDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLSetDefaults.setStatus("current")


class _BwaVLUnitName_Type(DisplayString):
    """Custom type bwaVLUnitName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BwaVLUnitName_Type.__name__ = "DisplayString"
_BwaVLUnitName_Object = MibScalar
bwaVLUnitName = _BwaVLUnitName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 3),
    _BwaVLUnitName_Type()
)
bwaVLUnitName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLUnitName.setStatus("current")


class _BwaVLFlashMemoryControl_Type(Integer32):
    """Custom type bwaVLFlashMemoryControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("resetAndBootFromShadowVersion", 1),
          ("useRunningVersionAfterReset", 2),
          ("cancel", 3))
    )


_BwaVLFlashMemoryControl_Type.__name__ = "Integer32"
_BwaVLFlashMemoryControl_Object = MibScalar
bwaVLFlashMemoryControl = _BwaVLFlashMemoryControl_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 4),
    _BwaVLFlashMemoryControl_Type()
)
bwaVLFlashMemoryControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLFlashMemoryControl.setStatus("current")
_BwaVLTelnetLogoutTimer_Type = Integer32
_BwaVLTelnetLogoutTimer_Object = MibScalar
bwaVLTelnetLogoutTimer = _BwaVLTelnetLogoutTimer_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 5),
    _BwaVLTelnetLogoutTimer_Type()
)
bwaVLTelnetLogoutTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLTelnetLogoutTimer.setStatus("current")


class _BwaVLSaveCurrentConfigurationAsOperatorDefaults_Type(Integer32):
    """Custom type bwaVLSaveCurrentConfigurationAsOperatorDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("saveAsDefaults", 1),
          ("cancel", 2))
    )


_BwaVLSaveCurrentConfigurationAsOperatorDefaults_Type.__name__ = "Integer32"
_BwaVLSaveCurrentConfigurationAsOperatorDefaults_Object = MibScalar
bwaVLSaveCurrentConfigurationAsOperatorDefaults = _BwaVLSaveCurrentConfigurationAsOperatorDefaults_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 6),
    _BwaVLSaveCurrentConfigurationAsOperatorDefaults_Type()
)
bwaVLSaveCurrentConfigurationAsOperatorDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLSaveCurrentConfigurationAsOperatorDefaults.setStatus("current")


class _BwaVLExitTelnet_Type(Integer32):
    """Custom type bwaVLExitTelnet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cancelOperation", 1),
          ("exit", 2))
    )


_BwaVLExitTelnet_Type.__name__ = "Integer32"
_BwaVLExitTelnet_Object = MibScalar
bwaVLExitTelnet = _BwaVLExitTelnet_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 7),
    _BwaVLExitTelnet_Type()
)
bwaVLExitTelnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLExitTelnet.setStatus("current")
_BwaVLUnitPasswords_ObjectIdentity = ObjectIdentity
bwaVLUnitPasswords = _BwaVLUnitPasswords_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 8)
)


class _BwaVLReadOnlyPassword_Type(DisplayString):
    """Custom type bwaVLReadOnlyPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_BwaVLReadOnlyPassword_Type.__name__ = "DisplayString"
_BwaVLReadOnlyPassword_Object = MibScalar
bwaVLReadOnlyPassword = _BwaVLReadOnlyPassword_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 8, 1),
    _BwaVLReadOnlyPassword_Type()
)
bwaVLReadOnlyPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLReadOnlyPassword.setStatus("current")


class _BwaVLInstallerPassword_Type(DisplayString):
    """Custom type bwaVLInstallerPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_BwaVLInstallerPassword_Type.__name__ = "DisplayString"
_BwaVLInstallerPassword_Object = MibScalar
bwaVLInstallerPassword = _BwaVLInstallerPassword_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 8, 2),
    _BwaVLInstallerPassword_Type()
)
bwaVLInstallerPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLInstallerPassword.setStatus("current")


class _BwaVLAdminPassword_Type(DisplayString):
    """Custom type bwaVLAdminPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_BwaVLAdminPassword_Type.__name__ = "DisplayString"
_BwaVLAdminPassword_Object = MibScalar
bwaVLAdminPassword = _BwaVLAdminPassword_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 8, 3),
    _BwaVLAdminPassword_Type()
)
bwaVLAdminPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLAdminPassword.setStatus("current")


class _BwaVLEthernetNegotiationMode_Type(Integer32):
    """Custom type bwaVLEthernetNegotiationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("force10MbpsAndHalfDuplex", 1),
          ("force10MbpsAndFullDuplex", 2),
          ("force100MbpsAndHalfDuplex", 3),
          ("force100MbpsAndFullDuplex", 4),
          ("autoNegotiationMode", 5))
    )


_BwaVLEthernetNegotiationMode_Type.__name__ = "Integer32"
_BwaVLEthernetNegotiationMode_Object = MibScalar
bwaVLEthernetNegotiationMode = _BwaVLEthernetNegotiationMode_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 9),
    _BwaVLEthernetNegotiationMode_Type()
)
bwaVLEthernetNegotiationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLEthernetNegotiationMode.setStatus("current")
_BwaVLFTPParameters_ObjectIdentity = ObjectIdentity
bwaVLFTPParameters = _BwaVLFTPParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 10)
)
_BwaVLFTPServerParams_ObjectIdentity = ObjectIdentity
bwaVLFTPServerParams = _BwaVLFTPServerParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 10, 1)
)


class _BwaVLFTPServerUserName_Type(DisplayString):
    """Custom type bwaVLFTPServerUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_BwaVLFTPServerUserName_Type.__name__ = "DisplayString"
_BwaVLFTPServerUserName_Object = MibScalar
bwaVLFTPServerUserName = _BwaVLFTPServerUserName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 10, 1, 1),
    _BwaVLFTPServerUserName_Type()
)
bwaVLFTPServerUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLFTPServerUserName.setStatus("current")


class _BwaVLFTPServerPassword_Type(DisplayString):
    """Custom type bwaVLFTPServerPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_BwaVLFTPServerPassword_Type.__name__ = "DisplayString"
_BwaVLFTPServerPassword_Object = MibScalar
bwaVLFTPServerPassword = _BwaVLFTPServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 10, 1, 2),
    _BwaVLFTPServerPassword_Type()
)
bwaVLFTPServerPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLFTPServerPassword.setStatus("current")
_BwaVLFTPClientIPAddress_Type = IpAddress
_BwaVLFTPClientIPAddress_Object = MibScalar
bwaVLFTPClientIPAddress = _BwaVLFTPClientIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 10, 1, 3),
    _BwaVLFTPClientIPAddress_Type()
)
bwaVLFTPClientIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLFTPClientIPAddress.setStatus("current")
_BwaVLFTPServerIpAddress_Type = IpAddress
_BwaVLFTPServerIpAddress_Object = MibScalar
bwaVLFTPServerIpAddress = _BwaVLFTPServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 10, 1, 4),
    _BwaVLFTPServerIpAddress_Type()
)
bwaVLFTPServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLFTPServerIpAddress.setStatus("current")
_BwaVLFTPClientMask_Type = IpAddress
_BwaVLFTPClientMask_Object = MibScalar
bwaVLFTPClientMask = _BwaVLFTPClientMask_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 10, 1, 5),
    _BwaVLFTPClientMask_Type()
)
bwaVLFTPClientMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLFTPClientMask.setStatus("current")
_BwaVLFTPGatewayIpAddress_Type = IpAddress
_BwaVLFTPGatewayIpAddress_Object = MibScalar
bwaVLFTPGatewayIpAddress = _BwaVLFTPGatewayIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 10, 1, 6),
    _BwaVLFTPGatewayIpAddress_Type()
)
bwaVLFTPGatewayIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLFTPGatewayIpAddress.setStatus("current")
_BwaVLFTPSwDownload_ObjectIdentity = ObjectIdentity
bwaVLFTPSwDownload = _BwaVLFTPSwDownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 10, 2)
)


class _BwaVLFTPSwFileName_Type(DisplayString):
    """Custom type bwaVLFTPSwFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_BwaVLFTPSwFileName_Type.__name__ = "DisplayString"
_BwaVLFTPSwFileName_Object = MibScalar
bwaVLFTPSwFileName = _BwaVLFTPSwFileName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 10, 2, 1),
    _BwaVLFTPSwFileName_Type()
)
bwaVLFTPSwFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLFTPSwFileName.setStatus("current")


class _BwaVLFTPSwSourceDir_Type(DisplayString):
    """Custom type bwaVLFTPSwSourceDir based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_BwaVLFTPSwSourceDir_Type.__name__ = "DisplayString"
_BwaVLFTPSwSourceDir_Object = MibScalar
bwaVLFTPSwSourceDir = _BwaVLFTPSwSourceDir_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 10, 2, 2),
    _BwaVLFTPSwSourceDir_Type()
)
bwaVLFTPSwSourceDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLFTPSwSourceDir.setStatus("current")


class _BwaVLFTPDownloadSwFile_Type(Integer32):
    """Custom type bwaVLFTPDownloadSwFile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("downloadFile", 1),
          ("cancel", 2))
    )


_BwaVLFTPDownloadSwFile_Type.__name__ = "Integer32"
_BwaVLFTPDownloadSwFile_Object = MibScalar
bwaVLFTPDownloadSwFile = _BwaVLFTPDownloadSwFile_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 10, 2, 3),
    _BwaVLFTPDownloadSwFile_Type()
)
bwaVLFTPDownloadSwFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLFTPDownloadSwFile.setStatus("current")
_BwaVLConfigurationFileLoading_ObjectIdentity = ObjectIdentity
bwaVLConfigurationFileLoading = _BwaVLConfigurationFileLoading_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 10, 3)
)


class _BwaVLConfigurationFileName_Type(DisplayString):
    """Custom type bwaVLConfigurationFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_BwaVLConfigurationFileName_Type.__name__ = "DisplayString"
_BwaVLConfigurationFileName_Object = MibScalar
bwaVLConfigurationFileName = _BwaVLConfigurationFileName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 10, 3, 1),
    _BwaVLConfigurationFileName_Type()
)
bwaVLConfigurationFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLConfigurationFileName.setStatus("current")


class _BwaVLOperatorDefaultsFileName_Type(DisplayString):
    """Custom type bwaVLOperatorDefaultsFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_BwaVLOperatorDefaultsFileName_Type.__name__ = "DisplayString"
_BwaVLOperatorDefaultsFileName_Object = MibScalar
bwaVLOperatorDefaultsFileName = _BwaVLOperatorDefaultsFileName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 10, 3, 2),
    _BwaVLOperatorDefaultsFileName_Type()
)
bwaVLOperatorDefaultsFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLOperatorDefaultsFileName.setStatus("current")


class _BwaVLFTPConfigurationFileSourceDir_Type(DisplayString):
    """Custom type bwaVLFTPConfigurationFileSourceDir based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_BwaVLFTPConfigurationFileSourceDir_Type.__name__ = "DisplayString"
_BwaVLFTPConfigurationFileSourceDir_Object = MibScalar
bwaVLFTPConfigurationFileSourceDir = _BwaVLFTPConfigurationFileSourceDir_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 10, 3, 3),
    _BwaVLFTPConfigurationFileSourceDir_Type()
)
bwaVLFTPConfigurationFileSourceDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLFTPConfigurationFileSourceDir.setStatus("current")


class _BwaVLExecuteFTPConfigurationFileLoading_Type(Integer32):
    """Custom type bwaVLExecuteFTPConfigurationFileLoading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("executeFTPGetConfigurationFile", 1),
          ("executeFTPPutConfigurationFile", 2),
          ("executeFTPGetOperatorDefaults", 3),
          ("executeFTPPutOperatorDefaults", 4),
          ("cancel", 5))
    )


_BwaVLExecuteFTPConfigurationFileLoading_Type.__name__ = "Integer32"
_BwaVLExecuteFTPConfigurationFileLoading_Object = MibScalar
bwaVLExecuteFTPConfigurationFileLoading = _BwaVLExecuteFTPConfigurationFileLoading_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 10, 3, 4),
    _BwaVLExecuteFTPConfigurationFileLoading_Type()
)
bwaVLExecuteFTPConfigurationFileLoading.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLExecuteFTPConfigurationFileLoading.setStatus("current")
_BwaVLEventLogFileUploading_ObjectIdentity = ObjectIdentity
bwaVLEventLogFileUploading = _BwaVLEventLogFileUploading_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 10, 4)
)


class _BwaVLEventLogFileName_Type(DisplayString):
    """Custom type bwaVLEventLogFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_BwaVLEventLogFileName_Type.__name__ = "DisplayString"
_BwaVLEventLogFileName_Object = MibScalar
bwaVLEventLogFileName = _BwaVLEventLogFileName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 10, 4, 1),
    _BwaVLEventLogFileName_Type()
)
bwaVLEventLogFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLEventLogFileName.setStatus("current")


class _BwaVLEventLogDestinationDir_Type(DisplayString):
    """Custom type bwaVLEventLogDestinationDir based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_BwaVLEventLogDestinationDir_Type.__name__ = "DisplayString"
_BwaVLEventLogDestinationDir_Object = MibScalar
bwaVLEventLogDestinationDir = _BwaVLEventLogDestinationDir_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 10, 4, 2),
    _BwaVLEventLogDestinationDir_Type()
)
bwaVLEventLogDestinationDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLEventLogDestinationDir.setStatus("current")


class _BwaVLUploadEventLogFile_Type(Integer32):
    """Custom type bwaVLUploadEventLogFile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("uploadFile", 1),
          ("cancel", 2))
    )


_BwaVLUploadEventLogFile_Type.__name__ = "Integer32"
_BwaVLUploadEventLogFile_Object = MibScalar
bwaVLUploadEventLogFile = _BwaVLUploadEventLogFile_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 10, 4, 3),
    _BwaVLUploadEventLogFile_Type()
)
bwaVLUploadEventLogFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLUploadEventLogFile.setStatus("current")


class _BwaVLLoadingStatus_Type(Integer32):
    """Custom type bwaVLLoadingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inProcess", 1),
          ("successful", 2),
          ("failed", 3))
    )


_BwaVLLoadingStatus_Type.__name__ = "Integer32"
_BwaVLLoadingStatus_Object = MibScalar
bwaVLLoadingStatus = _BwaVLLoadingStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 11),
    _BwaVLLoadingStatus_Type()
)
bwaVLLoadingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLLoadingStatus.setStatus("current")
_BwaVLEventLogFileParams_ObjectIdentity = ObjectIdentity
bwaVLEventLogFileParams = _BwaVLEventLogFileParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 12)
)


class _BwaVLEventLogPolicy_Type(Integer32):
    """Custom type bwaVLEventLogPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("message", 1),
          ("warning", 2),
          ("error", 3),
          ("fatal", 4),
          ("logNone", 5))
    )


_BwaVLEventLogPolicy_Type.__name__ = "Integer32"
_BwaVLEventLogPolicy_Object = MibScalar
bwaVLEventLogPolicy = _BwaVLEventLogPolicy_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 12, 1),
    _BwaVLEventLogPolicy_Type()
)
bwaVLEventLogPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLEventLogPolicy.setStatus("current")


class _BwaVLEraseEventLog_Type(Integer32):
    """Custom type bwaVLEraseEventLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eraseEventLog", 1),
          ("cancel", 2))
    )


_BwaVLEraseEventLog_Type.__name__ = "Integer32"
_BwaVLEraseEventLog_Object = MibScalar
bwaVLEraseEventLog = _BwaVLEraseEventLog_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 12, 2),
    _BwaVLEraseEventLog_Type()
)
bwaVLEraseEventLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLEraseEventLog.setStatus("current")


class _BwaVLSystemLocation_Type(DisplayString):
    """Custom type bwaVLSystemLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 34),
    )


_BwaVLSystemLocation_Type.__name__ = "DisplayString"
_BwaVLSystemLocation_Object = MibScalar
bwaVLSystemLocation = _BwaVLSystemLocation_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 13),
    _BwaVLSystemLocation_Type()
)
bwaVLSystemLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLSystemLocation.setStatus("current")
_BwaVLFeatureUpgrade_ObjectIdentity = ObjectIdentity
bwaVLFeatureUpgrade = _BwaVLFeatureUpgrade_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 14)
)


class _BwaVLFeatureUpgradeManually_Type(DisplayString):
    """Custom type bwaVLFeatureUpgradeManually based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 64),
    )


_BwaVLFeatureUpgradeManually_Type.__name__ = "DisplayString"
_BwaVLFeatureUpgradeManually_Object = MibScalar
bwaVLFeatureUpgradeManually = _BwaVLFeatureUpgradeManually_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 14, 1),
    _BwaVLFeatureUpgradeManually_Type()
)
bwaVLFeatureUpgradeManually.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLFeatureUpgradeManually.setStatus("current")


class _BwaVLChangeUnitType_Type(Integer32):
    """Custom type bwaVLChangeUnitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bu", 1),
          ("rb", 2),
          ("cancel", 3))
    )


_BwaVLChangeUnitType_Type.__name__ = "Integer32"
_BwaVLChangeUnitType_Object = MibScalar
bwaVLChangeUnitType = _BwaVLChangeUnitType_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 15),
    _BwaVLChangeUnitType_Type()
)
bwaVLChangeUnitType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLChangeUnitType.setStatus("current")
_BwaLighteAPWorkingMode_Type = Integer32
_BwaLighteAPWorkingMode_Object = MibScalar
bwaLighteAPWorkingMode = _BwaLighteAPWorkingMode_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 2, 16),
    _BwaLighteAPWorkingMode_Type()
)
bwaLighteAPWorkingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaLighteAPWorkingMode.setStatus("current")
_BwaVLNwMngParameters_ObjectIdentity = ObjectIdentity
bwaVLNwMngParameters = _BwaVLNwMngParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3)
)


class _BwaVLAccessToNwMng_Type(Integer32):
    """Custom type bwaVLAccessToNwMng based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("fromWirelessOnly", 1),
          ("fromEthernetOnly", 2),
          ("fromBothWirelessAndEthernet", 3),
          ("na", 255))
    )


_BwaVLAccessToNwMng_Type.__name__ = "Integer32"
_BwaVLAccessToNwMng_Object = MibScalar
bwaVLAccessToNwMng = _BwaVLAccessToNwMng_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 1),
    _BwaVLAccessToNwMng_Type()
)
bwaVLAccessToNwMng.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLAccessToNwMng.setStatus("current")


class _BwaVLNwMngFilter_Type(Integer32):
    """Custom type bwaVLNwMngFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("activateOnEthernetPort", 2),
          ("activateOnWirelessPort", 3),
          ("activateOnBothWirelessAndEthernet", 4),
          ("na", 255))
    )


_BwaVLNwMngFilter_Type.__name__ = "Integer32"
_BwaVLNwMngFilter_Object = MibScalar
bwaVLNwMngFilter = _BwaVLNwMngFilter_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 2),
    _BwaVLNwMngFilter_Type()
)
bwaVLNwMngFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLNwMngFilter.setStatus("current")
_MngIpFilterTable_Object = MibTable
mngIpFilterTable = _MngIpFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    mngIpFilterTable.setStatus("current")
_MngIpFilterEntry_Object = MibTableRow
mngIpFilterEntry = _MngIpFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 3, 1)
)
mngIpFilterEntry.setIndexNames(
    (0, "BWA-DOT11-WLAN-MIB", "bwaVLNwMngIpTableIdx"),
)
if mibBuilder.loadTexts:
    mngIpFilterEntry.setStatus("current")
_BwaVLNwMngIpAddress_Type = IpAddress
_BwaVLNwMngIpAddress_Object = MibTableColumn
bwaVLNwMngIpAddress = _BwaVLNwMngIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 3, 1, 1),
    _BwaVLNwMngIpAddress_Type()
)
bwaVLNwMngIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLNwMngIpAddress.setStatus("current")


class _BwaVLNwMngIpTableIdx_Type(Integer32):
    """Custom type bwaVLNwMngIpTableIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_BwaVLNwMngIpTableIdx_Type.__name__ = "Integer32"
_BwaVLNwMngIpTableIdx_Object = MibTableColumn
bwaVLNwMngIpTableIdx = _BwaVLNwMngIpTableIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 3, 1, 2),
    _BwaVLNwMngIpTableIdx_Type()
)
bwaVLNwMngIpTableIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLNwMngIpTableIdx.setStatus("current")


class _BwaVLDeleteOneNwIpAddr_Type(Integer32):
    """Custom type bwaVLDeleteOneNwIpAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 10),
        ValueRangeConstraint(255, 255),
    )


_BwaVLDeleteOneNwIpAddr_Type.__name__ = "Integer32"
_BwaVLDeleteOneNwIpAddr_Object = MibScalar
bwaVLDeleteOneNwIpAddr = _BwaVLDeleteOneNwIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 4),
    _BwaVLDeleteOneNwIpAddr_Type()
)
bwaVLDeleteOneNwIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLDeleteOneNwIpAddr.setStatus("current")


class _BwaVLDeleteAllNwIpAddrs_Type(Integer32):
    """Custom type bwaVLDeleteAllNwIpAddrs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("deleteAll", 1),
          ("cancelOperation", 2),
          ("na", 255))
    )


_BwaVLDeleteAllNwIpAddrs_Type.__name__ = "Integer32"
_BwaVLDeleteAllNwIpAddrs_Object = MibScalar
bwaVLDeleteAllNwIpAddrs = _BwaVLDeleteAllNwIpAddrs_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 5),
    _BwaVLDeleteAllNwIpAddrs_Type()
)
bwaVLDeleteAllNwIpAddrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLDeleteAllNwIpAddrs.setStatus("current")


class _BwaVLAccessToNwTrap_Type(Integer32):
    """Custom type bwaVLAccessToNwTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_BwaVLAccessToNwTrap_Type.__name__ = "Integer32"
_BwaVLAccessToNwTrap_Object = MibScalar
bwaVLAccessToNwTrap = _BwaVLAccessToNwTrap_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 6),
    _BwaVLAccessToNwTrap_Type()
)
bwaVLAccessToNwTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLAccessToNwTrap.setStatus("current")
_MngTrapTable_Object = MibTable
mngTrapTable = _MngTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 7)
)
if mibBuilder.loadTexts:
    mngTrapTable.setStatus("current")
_MngTrapEntry_Object = MibTableRow
mngTrapEntry = _MngTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 7, 1)
)
mngTrapEntry.setIndexNames(
    (0, "BWA-DOT11-WLAN-MIB", "bwaVLNwTrapTableIdx"),
)
if mibBuilder.loadTexts:
    mngTrapEntry.setStatus("current")


class _BwaVLNwMngTrapCommunity_Type(DisplayString):
    """Custom type bwaVLNwMngTrapCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_BwaVLNwMngTrapCommunity_Type.__name__ = "DisplayString"
_BwaVLNwMngTrapCommunity_Object = MibTableColumn
bwaVLNwMngTrapCommunity = _BwaVLNwMngTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 7, 1, 1),
    _BwaVLNwMngTrapCommunity_Type()
)
bwaVLNwMngTrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLNwMngTrapCommunity.setStatus("current")
_BwaVLNwMngTrapAddress_Type = IpAddress
_BwaVLNwMngTrapAddress_Object = MibTableColumn
bwaVLNwMngTrapAddress = _BwaVLNwMngTrapAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 7, 1, 2),
    _BwaVLNwMngTrapAddress_Type()
)
bwaVLNwMngTrapAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLNwMngTrapAddress.setStatus("current")


class _BwaVLNwTrapTableIdx_Type(Integer32):
    """Custom type bwaVLNwTrapTableIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_BwaVLNwTrapTableIdx_Type.__name__ = "Integer32"
_BwaVLNwTrapTableIdx_Object = MibTableColumn
bwaVLNwTrapTableIdx = _BwaVLNwTrapTableIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 7, 1, 3),
    _BwaVLNwTrapTableIdx_Type()
)
bwaVLNwTrapTableIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLNwTrapTableIdx.setStatus("current")


class _BwaVLDeleteOneTrapAddr_Type(Integer32):
    """Custom type bwaVLDeleteOneTrapAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 10),
        ValueRangeConstraint(255, 255),
    )


_BwaVLDeleteOneTrapAddr_Type.__name__ = "Integer32"
_BwaVLDeleteOneTrapAddr_Object = MibScalar
bwaVLDeleteOneTrapAddr = _BwaVLDeleteOneTrapAddr_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 8),
    _BwaVLDeleteOneTrapAddr_Type()
)
bwaVLDeleteOneTrapAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLDeleteOneTrapAddr.setStatus("current")


class _BwaVLDeleteAllTrapAddrs_Type(Integer32):
    """Custom type bwaVLDeleteAllTrapAddrs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("deleteAll", 1),
          ("cancelOperation", 2),
          ("na", 255))
    )


_BwaVLDeleteAllTrapAddrs_Type.__name__ = "Integer32"
_BwaVLDeleteAllTrapAddrs_Object = MibScalar
bwaVLDeleteAllTrapAddrs = _BwaVLDeleteAllTrapAddrs_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 9),
    _BwaVLDeleteAllTrapAddrs_Type()
)
bwaVLDeleteAllTrapAddrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLDeleteAllTrapAddrs.setStatus("current")
_BwaVLMngIpRangesTable_Object = MibTable
bwaVLMngIpRangesTable = _BwaVLMngIpRangesTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 10)
)
if mibBuilder.loadTexts:
    bwaVLMngIpRangesTable.setStatus("current")
_BwaVLMngIpRangeEntry_Object = MibTableRow
bwaVLMngIpRangeEntry = _BwaVLMngIpRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 10, 1)
)
bwaVLMngIpRangeEntry.setIndexNames(
    (0, "BWA-DOT11-WLAN-MIB", "bwaVLMngIpRangeIdx"),
)
if mibBuilder.loadTexts:
    bwaVLMngIpRangeEntry.setStatus("current")


class _BwaVLMngIpRangeIdx_Type(Integer32):
    """Custom type bwaVLMngIpRangeIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_BwaVLMngIpRangeIdx_Type.__name__ = "Integer32"
_BwaVLMngIpRangeIdx_Object = MibTableColumn
bwaVLMngIpRangeIdx = _BwaVLMngIpRangeIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 10, 1, 1),
    _BwaVLMngIpRangeIdx_Type()
)
bwaVLMngIpRangeIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLMngIpRangeIdx.setStatus("current")


class _BwaVLMngIpRangeFlag_Type(Integer32):
    """Custom type bwaVLMngIpRangeFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rangeDefinedByStartEndAddr", 1),
          ("rangeDefinedByStartAddrMask", 2))
    )


_BwaVLMngIpRangeFlag_Type.__name__ = "Integer32"
_BwaVLMngIpRangeFlag_Object = MibTableColumn
bwaVLMngIpRangeFlag = _BwaVLMngIpRangeFlag_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 10, 1, 2),
    _BwaVLMngIpRangeFlag_Type()
)
bwaVLMngIpRangeFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLMngIpRangeFlag.setStatus("current")
_BwaVLMngIpRangeStart_Type = IpAddress
_BwaVLMngIpRangeStart_Object = MibTableColumn
bwaVLMngIpRangeStart = _BwaVLMngIpRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 10, 1, 3),
    _BwaVLMngIpRangeStart_Type()
)
bwaVLMngIpRangeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLMngIpRangeStart.setStatus("current")
_BwaVLMngIpRangeEnd_Type = IpAddress
_BwaVLMngIpRangeEnd_Object = MibTableColumn
bwaVLMngIpRangeEnd = _BwaVLMngIpRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 10, 1, 4),
    _BwaVLMngIpRangeEnd_Type()
)
bwaVLMngIpRangeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLMngIpRangeEnd.setStatus("current")
_BwaVLMngIpRangeMask_Type = IpAddress
_BwaVLMngIpRangeMask_Object = MibTableColumn
bwaVLMngIpRangeMask = _BwaVLMngIpRangeMask_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 10, 1, 5),
    _BwaVLMngIpRangeMask_Type()
)
bwaVLMngIpRangeMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLMngIpRangeMask.setStatus("current")


class _BwaVLDeleteOneNwIpRange_Type(Integer32):
    """Custom type bwaVLDeleteOneNwIpRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 10),
        ValueRangeConstraint(255, 255),
    )


_BwaVLDeleteOneNwIpRange_Type.__name__ = "Integer32"
_BwaVLDeleteOneNwIpRange_Object = MibScalar
bwaVLDeleteOneNwIpRange = _BwaVLDeleteOneNwIpRange_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 11),
    _BwaVLDeleteOneNwIpRange_Type()
)
bwaVLDeleteOneNwIpRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLDeleteOneNwIpRange.setStatus("current")


class _BwaVLDeleteAllNwIpRanges_Type(Integer32):
    """Custom type bwaVLDeleteAllNwIpRanges based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("deleteAll", 1),
          ("cancelOperation", 2),
          ("na", 255))
    )


_BwaVLDeleteAllNwIpRanges_Type.__name__ = "Integer32"
_BwaVLDeleteAllNwIpRanges_Object = MibScalar
bwaVLDeleteAllNwIpRanges = _BwaVLDeleteAllNwIpRanges_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 12),
    _BwaVLDeleteAllNwIpRanges_Type()
)
bwaVLDeleteAllNwIpRanges.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLDeleteAllNwIpRanges.setStatus("current")
_BwaVLApClientIpAddress_Type = IpAddress
_BwaVLApClientIpAddress_Object = MibScalar
bwaVLApClientIpAddress = _BwaVLApClientIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 3, 13),
    _BwaVLApClientIpAddress_Type()
)
bwaVLApClientIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLApClientIpAddress.setStatus("current")
_BwaVLIpParams_ObjectIdentity = ObjectIdentity
bwaVLIpParams = _BwaVLIpParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 4)
)
_BwaVLUnitIpAddress_Type = IpAddress
_BwaVLUnitIpAddress_Object = MibScalar
bwaVLUnitIpAddress = _BwaVLUnitIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 4, 1),
    _BwaVLUnitIpAddress_Type()
)
bwaVLUnitIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLUnitIpAddress.setStatus("current")
_BwaVLSubNetMask_Type = IpAddress
_BwaVLSubNetMask_Object = MibScalar
bwaVLSubNetMask = _BwaVLSubNetMask_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 4, 2),
    _BwaVLSubNetMask_Type()
)
bwaVLSubNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLSubNetMask.setStatus("current")
_BwaVLDefaultGWAddress_Type = IpAddress
_BwaVLDefaultGWAddress_Object = MibScalar
bwaVLDefaultGWAddress = _BwaVLDefaultGWAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 4, 3),
    _BwaVLDefaultGWAddress_Type()
)
bwaVLDefaultGWAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLDefaultGWAddress.setStatus("current")


class _BwaVLUseDhcp_Type(Integer32):
    """Custom type bwaVLUseDhcp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("dhcpOnly", 2),
          ("automatic", 3))
    )


_BwaVLUseDhcp_Type.__name__ = "Integer32"
_BwaVLUseDhcp_Object = MibScalar
bwaVLUseDhcp = _BwaVLUseDhcp_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 4, 4),
    _BwaVLUseDhcp_Type()
)
bwaVLUseDhcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLUseDhcp.setStatus("current")


class _BwaVLAccessToDHCP_Type(Integer32):
    """Custom type bwaVLAccessToDHCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fromWirelessOnly", 1),
          ("fromEthernetOnly", 2),
          ("fromBothWirelessAndEthernet", 3))
    )


_BwaVLAccessToDHCP_Type.__name__ = "Integer32"
_BwaVLAccessToDHCP_Object = MibScalar
bwaVLAccessToDHCP = _BwaVLAccessToDHCP_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 4, 5),
    _BwaVLAccessToDHCP_Type()
)
bwaVLAccessToDHCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLAccessToDHCP.setStatus("current")
_BwaVLRunTimeIPaddr_Type = IpAddress
_BwaVLRunTimeIPaddr_Object = MibScalar
bwaVLRunTimeIPaddr = _BwaVLRunTimeIPaddr_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 4, 6),
    _BwaVLRunTimeIPaddr_Type()
)
bwaVLRunTimeIPaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLRunTimeIPaddr.setStatus("current")
_BwaVLRunTimeSubNetMask_Type = IpAddress
_BwaVLRunTimeSubNetMask_Object = MibScalar
bwaVLRunTimeSubNetMask = _BwaVLRunTimeSubNetMask_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 4, 7),
    _BwaVLRunTimeSubNetMask_Type()
)
bwaVLRunTimeSubNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLRunTimeSubNetMask.setStatus("current")
_BwaVLRunTimeDefaultIPGateway_Type = IpAddress
_BwaVLRunTimeDefaultIPGateway_Object = MibScalar
bwaVLRunTimeDefaultIPGateway = _BwaVLRunTimeDefaultIPGateway_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 4, 8),
    _BwaVLRunTimeDefaultIPGateway_Type()
)
bwaVLRunTimeDefaultIPGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLRunTimeDefaultIPGateway.setStatus("current")
_BwaVLBridgeParameters_ObjectIdentity = ObjectIdentity
bwaVLBridgeParameters = _BwaVLBridgeParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5)
)
_BwaVLVLANSupport_ObjectIdentity = ObjectIdentity
bwaVLVLANSupport = _BwaVLVLANSupport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1)
)
_BwaVLVlanID_Type = Integer32
_BwaVLVlanID_Object = MibScalar
bwaVLVlanID = _BwaVLVlanID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 1),
    _BwaVLVlanID_Type()
)
bwaVLVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLVlanID.setStatus("current")


class _BwaVLEthernetLinkType_Type(Integer32):
    """Custom type bwaVLEthernetLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("accessLink", 1),
          ("trunkLink", 2),
          ("hybridLink", 3),
          ("serviceProviderLink", 4))
    )


_BwaVLEthernetLinkType_Type.__name__ = "Integer32"
_BwaVLEthernetLinkType_Object = MibScalar
bwaVLEthernetLinkType = _BwaVLEthernetLinkType_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 2),
    _BwaVLEthernetLinkType_Type()
)
bwaVLEthernetLinkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLEthernetLinkType.setStatus("current")
_BwaVLManagementVlanID_Type = Integer32
_BwaVLManagementVlanID_Object = MibScalar
bwaVLManagementVlanID = _BwaVLManagementVlanID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 3),
    _BwaVLManagementVlanID_Type()
)
bwaVLManagementVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLManagementVlanID.setStatus("current")
_BwaVLVLANForwarding_ObjectIdentity = ObjectIdentity
bwaVLVLANForwarding = _BwaVLVLANForwarding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 4)
)


class _BwaVLVlanForwardingSupport_Type(Integer32):
    """Custom type bwaVLVlanForwardingSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BwaVLVlanForwardingSupport_Type.__name__ = "Integer32"
_BwaVLVlanForwardingSupport_Object = MibScalar
bwaVLVlanForwardingSupport = _BwaVLVlanForwardingSupport_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 4, 1),
    _BwaVLVlanForwardingSupport_Type()
)
bwaVLVlanForwardingSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLVlanForwardingSupport.setStatus("current")
_BwaVLVlanForwardingTable_Object = MibTable
bwaVLVlanForwardingTable = _BwaVLVlanForwardingTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 4, 2)
)
if mibBuilder.loadTexts:
    bwaVLVlanForwardingTable.setStatus("current")
_BwaVLVlanForwardingEntry_Object = MibTableRow
bwaVLVlanForwardingEntry = _BwaVLVlanForwardingEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 4, 2, 1)
)
bwaVLVlanForwardingEntry.setIndexNames(
    (0, "BWA-DOT11-WLAN-MIB", "bwaVLVlanForwardingTableIdx"),
)
if mibBuilder.loadTexts:
    bwaVLVlanForwardingEntry.setStatus("current")


class _BwaVLVlanForwardingTableIdx_Type(Integer32):
    """Custom type bwaVLVlanForwardingTableIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_BwaVLVlanForwardingTableIdx_Type.__name__ = "Integer32"
_BwaVLVlanForwardingTableIdx_Object = MibTableColumn
bwaVLVlanForwardingTableIdx = _BwaVLVlanForwardingTableIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 4, 2, 1, 1),
    _BwaVLVlanForwardingTableIdx_Type()
)
bwaVLVlanForwardingTableIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLVlanForwardingTableIdx.setStatus("current")
_BwaVLVlanIdForwarding_Type = Integer32
_BwaVLVlanIdForwarding_Object = MibTableColumn
bwaVLVlanIdForwarding = _BwaVLVlanIdForwarding_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 4, 2, 1, 2),
    _BwaVLVlanIdForwarding_Type()
)
bwaVLVlanIdForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLVlanIdForwarding.setStatus("current")
_BwaVLVlanRelaying_ObjectIdentity = ObjectIdentity
bwaVLVlanRelaying = _BwaVLVlanRelaying_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 5)
)


class _BwaVLVlanRelayingSupport_Type(Integer32):
    """Custom type bwaVLVlanRelayingSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BwaVLVlanRelayingSupport_Type.__name__ = "Integer32"
_BwaVLVlanRelayingSupport_Object = MibScalar
bwaVLVlanRelayingSupport = _BwaVLVlanRelayingSupport_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 5, 1),
    _BwaVLVlanRelayingSupport_Type()
)
bwaVLVlanRelayingSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLVlanRelayingSupport.setStatus("current")
_BwaVLVlanRelayingTable_Object = MibTable
bwaVLVlanRelayingTable = _BwaVLVlanRelayingTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 5, 2)
)
if mibBuilder.loadTexts:
    bwaVLVlanRelayingTable.setStatus("current")
_BwaVLVlanRelayingEntry_Object = MibTableRow
bwaVLVlanRelayingEntry = _BwaVLVlanRelayingEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 5, 2, 1)
)
bwaVLVlanRelayingEntry.setIndexNames(
    (0, "BWA-DOT11-WLAN-MIB", "bwaVLVlanRelayingTableIdx"),
)
if mibBuilder.loadTexts:
    bwaVLVlanRelayingEntry.setStatus("current")


class _BwaVLVlanRelayingTableIdx_Type(Integer32):
    """Custom type bwaVLVlanRelayingTableIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_BwaVLVlanRelayingTableIdx_Type.__name__ = "Integer32"
_BwaVLVlanRelayingTableIdx_Object = MibTableColumn
bwaVLVlanRelayingTableIdx = _BwaVLVlanRelayingTableIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 5, 2, 1, 1),
    _BwaVLVlanRelayingTableIdx_Type()
)
bwaVLVlanRelayingTableIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLVlanRelayingTableIdx.setStatus("current")
_BwaVLVlanIdRelaying_Type = Integer32
_BwaVLVlanIdRelaying_Object = MibTableColumn
bwaVLVlanIdRelaying = _BwaVLVlanIdRelaying_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 5, 2, 1, 2),
    _BwaVLVlanIdRelaying_Type()
)
bwaVLVlanIdRelaying.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLVlanIdRelaying.setStatus("current")
_BwaVLVLANTrafficPriority_ObjectIdentity = ObjectIdentity
bwaVLVLANTrafficPriority = _BwaVLVLANTrafficPriority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 6)
)


class _BwaVLVlanDataPriority_Type(Integer32):
    """Custom type bwaVLVlanDataPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            255
        )
    )
    namedValues = NamedValues(
        ("na", 255)
    )


_BwaVLVlanDataPriority_Type.__name__ = "Integer32"
_BwaVLVlanDataPriority_Object = MibScalar
bwaVLVlanDataPriority = _BwaVLVlanDataPriority_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 6, 1),
    _BwaVLVlanDataPriority_Type()
)
bwaVLVlanDataPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLVlanDataPriority.setStatus("current")


class _BwaVLVlanManagementPriority_Type(Integer32):
    """Custom type bwaVLVlanManagementPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            255
        )
    )
    namedValues = NamedValues(
        ("na", 255)
    )


_BwaVLVlanManagementPriority_Type.__name__ = "Integer32"
_BwaVLVlanManagementPriority_Object = MibScalar
bwaVLVlanManagementPriority = _BwaVLVlanManagementPriority_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 6, 2),
    _BwaVLVlanManagementPriority_Type()
)
bwaVLVlanManagementPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLVlanManagementPriority.setStatus("current")


class _BwaVLVlanPriorityThreshold_Type(Integer32):
    """Custom type bwaVLVlanPriorityThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            255
        )
    )
    namedValues = NamedValues(
        ("na", 255)
    )


_BwaVLVlanPriorityThreshold_Type.__name__ = "Integer32"
_BwaVLVlanPriorityThreshold_Object = MibScalar
bwaVLVlanPriorityThreshold = _BwaVLVlanPriorityThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 6, 3),
    _BwaVLVlanPriorityThreshold_Type()
)
bwaVLVlanPriorityThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLVlanPriorityThreshold.setStatus("current")
_BwaVLVLANQinQ_ObjectIdentity = ObjectIdentity
bwaVLVLANQinQ = _BwaVLVLANQinQ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 7)
)


class _BwaVLQinQEthertype_Type(Integer32):
    """Custom type bwaVLQinQEthertype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(33025, 36864),
        ValueRangeConstraint(37120, 37120),
        ValueRangeConstraint(37376, 37376),
    )


_BwaVLQinQEthertype_Type.__name__ = "Integer32"
_BwaVLQinQEthertype_Object = MibScalar
bwaVLQinQEthertype = _BwaVLQinQEthertype_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 7, 1),
    _BwaVLQinQEthertype_Type()
)
bwaVLQinQEthertype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLQinQEthertype.setStatus("current")


class _BwaVLQinQProviderVlanID_Type(Integer32):
    """Custom type bwaVLQinQProviderVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_BwaVLQinQProviderVlanID_Type.__name__ = "Integer32"
_BwaVLQinQProviderVlanID_Object = MibScalar
bwaVLQinQProviderVlanID = _BwaVLQinQProviderVlanID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 1, 7, 2),
    _BwaVLQinQProviderVlanID_Type()
)
bwaVLQinQProviderVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLQinQProviderVlanID.setStatus("current")
_BwaVLBridgeAgingTime_Type = Integer32
_BwaVLBridgeAgingTime_Object = MibScalar
bwaVLBridgeAgingTime = _BwaVLBridgeAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 2),
    _BwaVLBridgeAgingTime_Type()
)
bwaVLBridgeAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLBridgeAgingTime.setStatus("current")


class _BwaVLBroadcastRelaying_Type(Integer32):
    """Custom type bwaVLBroadcastRelaying based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("broadcastMulticastEnable", 2),
          ("broadcastEnable", 3),
          ("multicastEnable", 4),
          ("na", 255))
    )


_BwaVLBroadcastRelaying_Type.__name__ = "Integer32"
_BwaVLBroadcastRelaying_Object = MibScalar
bwaVLBroadcastRelaying = _BwaVLBroadcastRelaying_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 4),
    _BwaVLBroadcastRelaying_Type()
)
bwaVLBroadcastRelaying.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLBroadcastRelaying.setStatus("current")


class _BwaVLUnicastRelaying_Type(Integer32):
    """Custom type bwaVLUnicastRelaying based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BwaVLUnicastRelaying_Type.__name__ = "Integer32"
_BwaVLUnicastRelaying_Object = MibScalar
bwaVLUnicastRelaying = _BwaVLUnicastRelaying_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 5),
    _BwaVLUnicastRelaying_Type()
)
bwaVLUnicastRelaying.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLUnicastRelaying.setStatus("current")


class _BwaVLEthBroadcastFiltering_Type(Integer32):
    """Custom type bwaVLEthBroadcastFiltering based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("onEthernetOnly", 2),
          ("onWirelessOnly", 3),
          ("onBothWirelessAndEthernet", 4),
          ("na", 255))
    )


_BwaVLEthBroadcastFiltering_Type.__name__ = "Integer32"
_BwaVLEthBroadcastFiltering_Object = MibScalar
bwaVLEthBroadcastFiltering = _BwaVLEthBroadcastFiltering_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 6),
    _BwaVLEthBroadcastFiltering_Type()
)
bwaVLEthBroadcastFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLEthBroadcastFiltering.setStatus("current")
_BwaVLEthBroadcastingParameters_ObjectIdentity = ObjectIdentity
bwaVLEthBroadcastingParameters = _BwaVLEthBroadcastingParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 7)
)


class _BwaVLDHCPBroadcastOverrideFilter_Type(Integer32):
    """Custom type bwaVLDHCPBroadcastOverrideFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BwaVLDHCPBroadcastOverrideFilter_Type.__name__ = "Integer32"
_BwaVLDHCPBroadcastOverrideFilter_Object = MibScalar
bwaVLDHCPBroadcastOverrideFilter = _BwaVLDHCPBroadcastOverrideFilter_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 7, 1),
    _BwaVLDHCPBroadcastOverrideFilter_Type()
)
bwaVLDHCPBroadcastOverrideFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLDHCPBroadcastOverrideFilter.setStatus("current")


class _BwaVLPPPoEBroadcastOverrideFilter_Type(Integer32):
    """Custom type bwaVLPPPoEBroadcastOverrideFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BwaVLPPPoEBroadcastOverrideFilter_Type.__name__ = "Integer32"
_BwaVLPPPoEBroadcastOverrideFilter_Object = MibScalar
bwaVLPPPoEBroadcastOverrideFilter = _BwaVLPPPoEBroadcastOverrideFilter_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 7, 2),
    _BwaVLPPPoEBroadcastOverrideFilter_Type()
)
bwaVLPPPoEBroadcastOverrideFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLPPPoEBroadcastOverrideFilter.setStatus("current")


class _BwaVLARPBroadcastOverrideFilter_Type(Integer32):
    """Custom type bwaVLARPBroadcastOverrideFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BwaVLARPBroadcastOverrideFilter_Type.__name__ = "Integer32"
_BwaVLARPBroadcastOverrideFilter_Object = MibScalar
bwaVLARPBroadcastOverrideFilter = _BwaVLARPBroadcastOverrideFilter_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 7, 3),
    _BwaVLARPBroadcastOverrideFilter_Type()
)
bwaVLARPBroadcastOverrideFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLARPBroadcastOverrideFilter.setStatus("current")


class _BwaVLEthBroadcastMulticastLimiterOption_Type(Integer32):
    """Custom type bwaVLEthBroadcastMulticastLimiterOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("limitOnlyBroadcasts", 2),
          ("limitMulticastsExceptBroadcasts", 3),
          ("limitAllMulticasts", 4))
    )


_BwaVLEthBroadcastMulticastLimiterOption_Type.__name__ = "Integer32"
_BwaVLEthBroadcastMulticastLimiterOption_Object = MibScalar
bwaVLEthBroadcastMulticastLimiterOption = _BwaVLEthBroadcastMulticastLimiterOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 7, 4),
    _BwaVLEthBroadcastMulticastLimiterOption_Type()
)
bwaVLEthBroadcastMulticastLimiterOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLEthBroadcastMulticastLimiterOption.setStatus("current")
_BwaVLEthBroadcastMulticastLimiterThreshold_Type = Integer32
_BwaVLEthBroadcastMulticastLimiterThreshold_Object = MibScalar
bwaVLEthBroadcastMulticastLimiterThreshold = _BwaVLEthBroadcastMulticastLimiterThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 7, 5),
    _BwaVLEthBroadcastMulticastLimiterThreshold_Type()
)
bwaVLEthBroadcastMulticastLimiterThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLEthBroadcastMulticastLimiterThreshold.setStatus("current")
_BwaVLEthBroadcastMulticastLimiterSendTrapInterval_Type = Integer32
_BwaVLEthBroadcastMulticastLimiterSendTrapInterval_Object = MibScalar
bwaVLEthBroadcastMulticastLimiterSendTrapInterval = _BwaVLEthBroadcastMulticastLimiterSendTrapInterval_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 7, 6),
    _BwaVLEthBroadcastMulticastLimiterSendTrapInterval_Type()
)
bwaVLEthBroadcastMulticastLimiterSendTrapInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLEthBroadcastMulticastLimiterSendTrapInterval.setStatus("current")
_BwaVLToSPriorityParameters_ObjectIdentity = ObjectIdentity
bwaVLToSPriorityParameters = _BwaVLToSPriorityParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 8)
)
_BwaVLToSPrecedenceThreshold_Type = Integer32
_BwaVLToSPrecedenceThreshold_Object = MibScalar
bwaVLToSPrecedenceThreshold = _BwaVLToSPrecedenceThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 8, 1),
    _BwaVLToSPrecedenceThreshold_Type()
)
bwaVLToSPrecedenceThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLToSPrecedenceThreshold.setStatus("current")


class _BwaVLRoamingOption_Type(Integer32):
    """Custom type bwaVLRoamingOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BwaVLRoamingOption_Type.__name__ = "Integer32"
_BwaVLRoamingOption_Object = MibScalar
bwaVLRoamingOption = _BwaVLRoamingOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 9),
    _BwaVLRoamingOption_Type()
)
bwaVLRoamingOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLRoamingOption.setStatus("current")
_BwaVLMacAddressDenyList_ObjectIdentity = ObjectIdentity
bwaVLMacAddressDenyList = _BwaVLMacAddressDenyList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 10)
)
_BwaVLMacAddressDenyListTable_Object = MibTable
bwaVLMacAddressDenyListTable = _BwaVLMacAddressDenyListTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 10, 1)
)
if mibBuilder.loadTexts:
    bwaVLMacAddressDenyListTable.setStatus("current")
_BwaVLMacAddressDenyListEntry_Object = MibTableRow
bwaVLMacAddressDenyListEntry = _BwaVLMacAddressDenyListEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 10, 1, 1)
)
bwaVLMacAddressDenyListEntry.setIndexNames(
    (0, "BWA-DOT11-WLAN-MIB", "bwaVLMacAddressDenyListTableIdx"),
)
if mibBuilder.loadTexts:
    bwaVLMacAddressDenyListEntry.setStatus("current")


class _BwaVLMacAddressDenyListTableIdx_Type(Integer32):
    """Custom type bwaVLMacAddressDenyListTableIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_BwaVLMacAddressDenyListTableIdx_Type.__name__ = "Integer32"
_BwaVLMacAddressDenyListTableIdx_Object = MibTableColumn
bwaVLMacAddressDenyListTableIdx = _BwaVLMacAddressDenyListTableIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 10, 1, 1, 1),
    _BwaVLMacAddressDenyListTableIdx_Type()
)
bwaVLMacAddressDenyListTableIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLMacAddressDenyListTableIdx.setStatus("current")
_BwaVLMacAddressDenyListId_Type = MacAddress
_BwaVLMacAddressDenyListId_Object = MibTableColumn
bwaVLMacAddressDenyListId = _BwaVLMacAddressDenyListId_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 10, 1, 1, 2),
    _BwaVLMacAddressDenyListId_Type()
)
bwaVLMacAddressDenyListId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLMacAddressDenyListId.setStatus("current")
_BwaVLMacAddressDenyListAdd_Type = MacAddress
_BwaVLMacAddressDenyListAdd_Object = MibScalar
bwaVLMacAddressDenyListAdd = _BwaVLMacAddressDenyListAdd_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 10, 2),
    _BwaVLMacAddressDenyListAdd_Type()
)
bwaVLMacAddressDenyListAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLMacAddressDenyListAdd.setStatus("current")
_BwaVLMacAddressDenyListRemove_Type = MacAddress
_BwaVLMacAddressDenyListRemove_Object = MibScalar
bwaVLMacAddressDenyListRemove = _BwaVLMacAddressDenyListRemove_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 10, 3),
    _BwaVLMacAddressDenyListRemove_Type()
)
bwaVLMacAddressDenyListRemove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLMacAddressDenyListRemove.setStatus("current")


class _BwaVLNumberOfMacAddressesInDenyList_Type(Integer32):
    """Custom type bwaVLNumberOfMacAddressesInDenyList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            255
        )
    )
    namedValues = NamedValues(
        ("na", 255)
    )


_BwaVLNumberOfMacAddressesInDenyList_Type.__name__ = "Integer32"
_BwaVLNumberOfMacAddressesInDenyList_Object = MibScalar
bwaVLNumberOfMacAddressesInDenyList = _BwaVLNumberOfMacAddressesInDenyList_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 10, 4),
    _BwaVLNumberOfMacAddressesInDenyList_Type()
)
bwaVLNumberOfMacAddressesInDenyList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLNumberOfMacAddressesInDenyList.setStatus("current")


class _BwaVLMacAddressDenyListAction_Type(Integer32):
    """Custom type bwaVLMacAddressDenyListAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("denyList", 1),
          ("allowedList", 2),
          ("na", 255))
    )


_BwaVLMacAddressDenyListAction_Type.__name__ = "Integer32"
_BwaVLMacAddressDenyListAction_Object = MibScalar
bwaVLMacAddressDenyListAction = _BwaVLMacAddressDenyListAction_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 10, 5),
    _BwaVLMacAddressDenyListAction_Type()
)
bwaVLMacAddressDenyListAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLMacAddressDenyListAction.setStatus("current")
_BwaVLPortsControl_ObjectIdentity = ObjectIdentity
bwaVLPortsControl = _BwaVLPortsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 11)
)


class _BwaVLEthernetPortControl_Type(Integer32):
    """Custom type bwaVLEthernetPortControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BwaVLEthernetPortControl_Type.__name__ = "Integer32"
_BwaVLEthernetPortControl_Object = MibScalar
bwaVLEthernetPortControl = _BwaVLEthernetPortControl_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 5, 11, 1),
    _BwaVLEthernetPortControl_Type()
)
bwaVLEthernetPortControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLEthernetPortControl.setStatus("current")
_BwaVLAirInterface_ObjectIdentity = ObjectIdentity
bwaVLAirInterface = _BwaVLAirInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6)
)
_BwaVLESSIDParameters_ObjectIdentity = ObjectIdentity
bwaVLESSIDParameters = _BwaVLESSIDParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 1)
)


class _BwaVLESSID_Type(DisplayString):
    """Custom type bwaVLESSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_BwaVLESSID_Type.__name__ = "DisplayString"
_BwaVLESSID_Object = MibScalar
bwaVLESSID = _BwaVLESSID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 1, 1),
    _BwaVLESSID_Type()
)
bwaVLESSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLESSID.setStatus("current")


class _BwaVLOperatorESSIDOption_Type(Integer32):
    """Custom type bwaVLOperatorESSIDOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BwaVLOperatorESSIDOption_Type.__name__ = "Integer32"
_BwaVLOperatorESSIDOption_Object = MibScalar
bwaVLOperatorESSIDOption = _BwaVLOperatorESSIDOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 1, 2),
    _BwaVLOperatorESSIDOption_Type()
)
bwaVLOperatorESSIDOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLOperatorESSIDOption.setStatus("current")


class _BwaVLOperatorESSID_Type(DisplayString):
    """Custom type bwaVLOperatorESSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_BwaVLOperatorESSID_Type.__name__ = "DisplayString"
_BwaVLOperatorESSID_Object = MibScalar
bwaVLOperatorESSID = _BwaVLOperatorESSID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 1, 3),
    _BwaVLOperatorESSID_Type()
)
bwaVLOperatorESSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLOperatorESSID.setStatus("current")


class _BwaVLRunTimeESSID_Type(DisplayString):
    """Custom type bwaVLRunTimeESSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(31, 31),
    )
    fixed_length = 31


_BwaVLRunTimeESSID_Type.__name__ = "DisplayString"
_BwaVLRunTimeESSID_Object = MibScalar
bwaVLRunTimeESSID = _BwaVLRunTimeESSID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 1, 4),
    _BwaVLRunTimeESSID_Type()
)
bwaVLRunTimeESSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLRunTimeESSID.setStatus("current")
_BwaVLMaximumCellRadius_Type = Integer32
_BwaVLMaximumCellRadius_Object = MibScalar
bwaVLMaximumCellRadius = _BwaVLMaximumCellRadius_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 2),
    _BwaVLMaximumCellRadius_Type()
)
bwaVLMaximumCellRadius.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLMaximumCellRadius.setStatus("current")


class _BwaVLAIFS_Type(Integer32):
    """Custom type bwaVLAIFS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oneSlot", 1),
          ("twoSlots", 2))
    )


_BwaVLAIFS_Type.__name__ = "Integer32"
_BwaVLAIFS_Object = MibScalar
bwaVLAIFS = _BwaVLAIFS_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 3),
    _BwaVLAIFS_Type()
)
bwaVLAIFS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLAIFS.setStatus("current")
_BwaVLWirelessTrapThreshold_Type = Integer32
_BwaVLWirelessTrapThreshold_Object = MibScalar
bwaVLWirelessTrapThreshold = _BwaVLWirelessTrapThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 4),
    _BwaVLWirelessTrapThreshold_Type()
)
bwaVLWirelessTrapThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLWirelessTrapThreshold.setStatus("current")
_BwaVLTransmitPowerTable_Object = MibTable
bwaVLTransmitPowerTable = _BwaVLTransmitPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 5)
)
if mibBuilder.loadTexts:
    bwaVLTransmitPowerTable.setStatus("current")
_BwaVLTransmitPowerEntry_Object = MibTableRow
bwaVLTransmitPowerEntry = _BwaVLTransmitPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 5, 1)
)
bwaVLTransmitPowerEntry.setIndexNames(
    (0, "BWA-DOT11-WLAN-MIB", "bwaVLTransmitPowerIdx"),
)
if mibBuilder.loadTexts:
    bwaVLTransmitPowerEntry.setStatus("current")


class _BwaVLTransmitPowerIdx_Type(Integer32):
    """Custom type bwaVLTransmitPowerIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_BwaVLTransmitPowerIdx_Type.__name__ = "Integer32"
_BwaVLTransmitPowerIdx_Object = MibTableColumn
bwaVLTransmitPowerIdx = _BwaVLTransmitPowerIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 5, 1, 1),
    _BwaVLTransmitPowerIdx_Type()
)
bwaVLTransmitPowerIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLTransmitPowerIdx.setStatus("current")


class _BwaVLApplicableModulationLevel_Type(Integer32):
    """Custom type bwaVLApplicableModulationLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("level1to5", 1),
          ("level6", 2),
          ("level7", 3),
          ("level8", 4))
    )


_BwaVLApplicableModulationLevel_Type.__name__ = "Integer32"
_BwaVLApplicableModulationLevel_Object = MibTableColumn
bwaVLApplicableModulationLevel = _BwaVLApplicableModulationLevel_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 5, 1, 2),
    _BwaVLApplicableModulationLevel_Type()
)
bwaVLApplicableModulationLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLApplicableModulationLevel.setStatus("current")
_BwaVLMaximumTxPowerRange_Type = DisplayString
_BwaVLMaximumTxPowerRange_Object = MibTableColumn
bwaVLMaximumTxPowerRange = _BwaVLMaximumTxPowerRange_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 5, 1, 3),
    _BwaVLMaximumTxPowerRange_Type()
)
bwaVLMaximumTxPowerRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLMaximumTxPowerRange.setStatus("current")
_BwaVLTxPower_Type = DisplayString
_BwaVLTxPower_Object = MibTableColumn
bwaVLTxPower = _BwaVLTxPower_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 5, 1, 4),
    _BwaVLTxPower_Type()
)
bwaVLTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLTxPower.setStatus("current")
_BwaVLCurrentTxPower_Type = DisplayString
_BwaVLCurrentTxPower_Object = MibTableColumn
bwaVLCurrentTxPower = _BwaVLCurrentTxPower_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 5, 1, 5),
    _BwaVLCurrentTxPower_Type()
)
bwaVLCurrentTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLCurrentTxPower.setStatus("current")
_BwaVLMaximumTransmitPowerTable_Object = MibTable
bwaVLMaximumTransmitPowerTable = _BwaVLMaximumTransmitPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 6)
)
if mibBuilder.loadTexts:
    bwaVLMaximumTransmitPowerTable.setStatus("current")
_BwaVLMaximumTransmitPowerEntry_Object = MibTableRow
bwaVLMaximumTransmitPowerEntry = _BwaVLMaximumTransmitPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 6, 1)
)
bwaVLMaximumTransmitPowerEntry.setIndexNames(
    (0, "BWA-DOT11-WLAN-MIB", "bwaVLMaximumTransmitPowerIdx"),
)
if mibBuilder.loadTexts:
    bwaVLMaximumTransmitPowerEntry.setStatus("current")


class _BwaVLMaximumTransmitPowerIdx_Type(Integer32):
    """Custom type bwaVLMaximumTransmitPowerIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_BwaVLMaximumTransmitPowerIdx_Type.__name__ = "Integer32"
_BwaVLMaximumTransmitPowerIdx_Object = MibTableColumn
bwaVLMaximumTransmitPowerIdx = _BwaVLMaximumTransmitPowerIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 6, 1, 1),
    _BwaVLMaximumTransmitPowerIdx_Type()
)
bwaVLMaximumTransmitPowerIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLMaximumTransmitPowerIdx.setStatus("current")


class _BwaVLMaxTxApplicableModulationLevel_Type(Integer32):
    """Custom type bwaVLMaxTxApplicableModulationLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("level1to5", 1),
          ("level6", 2),
          ("level7", 3),
          ("level8", 4))
    )


_BwaVLMaxTxApplicableModulationLevel_Type.__name__ = "Integer32"
_BwaVLMaxTxApplicableModulationLevel_Object = MibTableColumn
bwaVLMaxTxApplicableModulationLevel = _BwaVLMaxTxApplicableModulationLevel_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 6, 1, 2),
    _BwaVLMaxTxApplicableModulationLevel_Type()
)
bwaVLMaxTxApplicableModulationLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLMaxTxApplicableModulationLevel.setStatus("current")
_BwaVLDefinedMaximumTxPowerRange_Type = DisplayString
_BwaVLDefinedMaximumTxPowerRange_Object = MibTableColumn
bwaVLDefinedMaximumTxPowerRange = _BwaVLDefinedMaximumTxPowerRange_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 6, 1, 3),
    _BwaVLDefinedMaximumTxPowerRange_Type()
)
bwaVLDefinedMaximumTxPowerRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLDefinedMaximumTxPowerRange.setStatus("current")
_BwaVLMaxTxPower_Type = DisplayString
_BwaVLMaxTxPower_Object = MibTableColumn
bwaVLMaxTxPower = _BwaVLMaxTxPower_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 6, 1, 4),
    _BwaVLMaxTxPower_Type()
)
bwaVLMaxTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLMaxTxPower.setStatus("current")
_BwaVLMaxNumOfAssociations_Type = Integer32
_BwaVLMaxNumOfAssociations_Object = MibScalar
bwaVLMaxNumOfAssociations = _BwaVLMaxNumOfAssociations_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 10),
    _BwaVLMaxNumOfAssociations_Type()
)
bwaVLMaxNumOfAssociations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLMaxNumOfAssociations.setStatus("current")
_BwaVLBestAu_ObjectIdentity = ObjectIdentity
bwaVLBestAu = _BwaVLBestAu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 11)
)


class _BwaVLBestAuSupport_Type(Integer32):
    """Custom type bwaVLBestAuSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BwaVLBestAuSupport_Type.__name__ = "Integer32"
_BwaVLBestAuSupport_Object = MibScalar
bwaVLBestAuSupport = _BwaVLBestAuSupport_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 11, 1),
    _BwaVLBestAuSupport_Type()
)
bwaVLBestAuSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLBestAuSupport.setStatus("current")
_BwaVLBestAuNoOfScanningAttempts_Type = Integer32
_BwaVLBestAuNoOfScanningAttempts_Object = MibScalar
bwaVLBestAuNoOfScanningAttempts = _BwaVLBestAuNoOfScanningAttempts_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 11, 2),
    _BwaVLBestAuNoOfScanningAttempts_Type()
)
bwaVLBestAuNoOfScanningAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLBestAuNoOfScanningAttempts.setStatus("current")
_BwaVLPreferredAuMacAddress_Type = MacAddress
_BwaVLPreferredAuMacAddress_Object = MibScalar
bwaVLPreferredAuMacAddress = _BwaVLPreferredAuMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 11, 3),
    _BwaVLPreferredAuMacAddress_Type()
)
bwaVLPreferredAuMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLPreferredAuMacAddress.setStatus("current")
_BwaVLNeighborAuTable_Object = MibTable
bwaVLNeighborAuTable = _BwaVLNeighborAuTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 11, 4)
)
if mibBuilder.loadTexts:
    bwaVLNeighborAuTable.setStatus("current")
_BwaVLNeighborAuEntry_Object = MibTableRow
bwaVLNeighborAuEntry = _BwaVLNeighborAuEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 11, 4, 1)
)
bwaVLNeighborAuEntry.setIndexNames(
    (0, "BWA-DOT11-WLAN-MIB", "bwaVLNeighborAuIdx"),
)
if mibBuilder.loadTexts:
    bwaVLNeighborAuEntry.setStatus("current")


class _BwaVLNeighborAuIdx_Type(Integer32):
    """Custom type bwaVLNeighborAuIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_BwaVLNeighborAuIdx_Type.__name__ = "Integer32"
_BwaVLNeighborAuIdx_Object = MibTableColumn
bwaVLNeighborAuIdx = _BwaVLNeighborAuIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 11, 4, 1, 1),
    _BwaVLNeighborAuIdx_Type()
)
bwaVLNeighborAuIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLNeighborAuIdx.setStatus("current")
_BwaVLNeighborAuMacAdd_Type = MacAddress
_BwaVLNeighborAuMacAdd_Object = MibTableColumn
bwaVLNeighborAuMacAdd = _BwaVLNeighborAuMacAdd_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 11, 4, 1, 2),
    _BwaVLNeighborAuMacAdd_Type()
)
bwaVLNeighborAuMacAdd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLNeighborAuMacAdd.setStatus("current")
_BwaVLNeighborAuESSID_Type = DisplayString
_BwaVLNeighborAuESSID_Object = MibTableColumn
bwaVLNeighborAuESSID = _BwaVLNeighborAuESSID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 11, 4, 1, 3),
    _BwaVLNeighborAuESSID_Type()
)
bwaVLNeighborAuESSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLNeighborAuESSID.setStatus("current")


class _BwaVLNeighborAuSNR_Type(Integer32):
    """Custom type bwaVLNeighborAuSNR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            255
        )
    )
    namedValues = NamedValues(
        ("na", 255)
    )


_BwaVLNeighborAuSNR_Type.__name__ = "Integer32"
_BwaVLNeighborAuSNR_Object = MibTableColumn
bwaVLNeighborAuSNR = _BwaVLNeighborAuSNR_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 11, 4, 1, 4),
    _BwaVLNeighborAuSNR_Type()
)
bwaVLNeighborAuSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLNeighborAuSNR.setStatus("current")


class _BwaVLNeighborAuAssocLoadStatus_Type(Integer32):
    """Custom type bwaVLNeighborAuAssocLoadStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("notFull", 2),
          ("na", 255))
    )


_BwaVLNeighborAuAssocLoadStatus_Type.__name__ = "Integer32"
_BwaVLNeighborAuAssocLoadStatus_Object = MibTableColumn
bwaVLNeighborAuAssocLoadStatus = _BwaVLNeighborAuAssocLoadStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 11, 4, 1, 5),
    _BwaVLNeighborAuAssocLoadStatus_Type()
)
bwaVLNeighborAuAssocLoadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLNeighborAuAssocLoadStatus.setStatus("current")
_BwaVLNeighborAuMark_Type = Integer32
_BwaVLNeighborAuMark_Object = MibTableColumn
bwaVLNeighborAuMark = _BwaVLNeighborAuMark_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 11, 4, 1, 6),
    _BwaVLNeighborAuMark_Type()
)
bwaVLNeighborAuMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLNeighborAuMark.setStatus("current")


class _BwaVLNeighborAuHwRevision_Type(Integer32):
    """Custom type bwaVLNeighborAuHwRevision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("hwRevisionA", 1),
          ("hwRevisionB", 2),
          ("hwRevisionC", 3),
          ("hwRevisionD", 4),
          ("hwRevisionE", 5),
          ("na", 255))
    )


_BwaVLNeighborAuHwRevision_Type.__name__ = "Integer32"
_BwaVLNeighborAuHwRevision_Object = MibTableColumn
bwaVLNeighborAuHwRevision = _BwaVLNeighborAuHwRevision_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 11, 4, 1, 7),
    _BwaVLNeighborAuHwRevision_Type()
)
bwaVLNeighborAuHwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLNeighborAuHwRevision.setStatus("current")
_BwaVLNeighborAuCountryCode_Type = Integer32
_BwaVLNeighborAuCountryCode_Object = MibTableColumn
bwaVLNeighborAuCountryCode = _BwaVLNeighborAuCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 11, 4, 1, 8),
    _BwaVLNeighborAuCountryCode_Type()
)
bwaVLNeighborAuCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLNeighborAuCountryCode.setStatus("current")
_BwaVLNeighborAuSwVer_Type = DisplayString
_BwaVLNeighborAuSwVer_Object = MibTableColumn
bwaVLNeighborAuSwVer = _BwaVLNeighborAuSwVer_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 11, 4, 1, 9),
    _BwaVLNeighborAuSwVer_Type()
)
bwaVLNeighborAuSwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLNeighborAuSwVer.setStatus("current")


class _BwaVLNeighborAuAtpcOption_Type(Integer32):
    """Custom type bwaVLNeighborAuAtpcOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BwaVLNeighborAuAtpcOption_Type.__name__ = "Integer32"
_BwaVLNeighborAuAtpcOption_Object = MibTableColumn
bwaVLNeighborAuAtpcOption = _BwaVLNeighborAuAtpcOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 11, 4, 1, 10),
    _BwaVLNeighborAuAtpcOption_Type()
)
bwaVLNeighborAuAtpcOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLNeighborAuAtpcOption.setStatus("current")


class _BwaVLNeighborAuAdapModOption_Type(Integer32):
    """Custom type bwaVLNeighborAuAdapModOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BwaVLNeighborAuAdapModOption_Type.__name__ = "Integer32"
_BwaVLNeighborAuAdapModOption_Object = MibTableColumn
bwaVLNeighborAuAdapModOption = _BwaVLNeighborAuAdapModOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 11, 4, 1, 11),
    _BwaVLNeighborAuAdapModOption_Type()
)
bwaVLNeighborAuAdapModOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLNeighborAuAdapModOption.setStatus("current")


class _BwaVLNeighborAuBurstModeOption_Type(Integer32):
    """Custom type bwaVLNeighborAuBurstModeOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BwaVLNeighborAuBurstModeOption_Type.__name__ = "Integer32"
_BwaVLNeighborAuBurstModeOption_Object = MibTableColumn
bwaVLNeighborAuBurstModeOption = _BwaVLNeighborAuBurstModeOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 11, 4, 1, 12),
    _BwaVLNeighborAuBurstModeOption_Type()
)
bwaVLNeighborAuBurstModeOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLNeighborAuBurstModeOption.setStatus("current")


class _BwaVLNeighborAuDfsOption_Type(Integer32):
    """Custom type bwaVLNeighborAuDfsOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BwaVLNeighborAuDfsOption_Type.__name__ = "Integer32"
_BwaVLNeighborAuDfsOption_Object = MibTableColumn
bwaVLNeighborAuDfsOption = _BwaVLNeighborAuDfsOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 11, 4, 1, 14),
    _BwaVLNeighborAuDfsOption_Type()
)
bwaVLNeighborAuDfsOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLNeighborAuDfsOption.setStatus("current")


class _BwaVLNeighborAuConcatenationOption_Type(Integer32):
    """Custom type bwaVLNeighborAuConcatenationOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BwaVLNeighborAuConcatenationOption_Type.__name__ = "Integer32"
_BwaVLNeighborAuConcatenationOption_Object = MibTableColumn
bwaVLNeighborAuConcatenationOption = _BwaVLNeighborAuConcatenationOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 11, 4, 1, 15),
    _BwaVLNeighborAuConcatenationOption_Type()
)
bwaVLNeighborAuConcatenationOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLNeighborAuConcatenationOption.setStatus("current")


class _BwaVLNeighborAuLearnCountryCodeBySU_Type(Integer32):
    """Custom type bwaVLNeighborAuLearnCountryCodeBySU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BwaVLNeighborAuLearnCountryCodeBySU_Type.__name__ = "Integer32"
_BwaVLNeighborAuLearnCountryCodeBySU_Object = MibTableColumn
bwaVLNeighborAuLearnCountryCodeBySU = _BwaVLNeighborAuLearnCountryCodeBySU_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 11, 4, 1, 17),
    _BwaVLNeighborAuLearnCountryCodeBySU_Type()
)
bwaVLNeighborAuLearnCountryCodeBySU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLNeighborAuLearnCountryCodeBySU.setStatus("current")


class _BwaVLNeighborAuSecurityMode_Type(Integer32):
    """Custom type bwaVLNeighborAuSecurityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("wep", 1),
          ("aesOCB", 2),
          ("fips197", 3),
          ("na", 255))
    )


_BwaVLNeighborAuSecurityMode_Type.__name__ = "Integer32"
_BwaVLNeighborAuSecurityMode_Object = MibTableColumn
bwaVLNeighborAuSecurityMode = _BwaVLNeighborAuSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 11, 4, 1, 18),
    _BwaVLNeighborAuSecurityMode_Type()
)
bwaVLNeighborAuSecurityMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLNeighborAuSecurityMode.setStatus("current")


class _BwaVLNeighborAuAuthOption_Type(Integer32):
    """Custom type bwaVLNeighborAuAuthOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("openSystem", 1),
          ("sharedKey", 2),
          ("na", 255))
    )


_BwaVLNeighborAuAuthOption_Type.__name__ = "Integer32"
_BwaVLNeighborAuAuthOption_Object = MibTableColumn
bwaVLNeighborAuAuthOption = _BwaVLNeighborAuAuthOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 11, 4, 1, 19),
    _BwaVLNeighborAuAuthOption_Type()
)
bwaVLNeighborAuAuthOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLNeighborAuAuthOption.setStatus("current")


class _BwaVLNeighborAuDataEncyptOption_Type(Integer32):
    """Custom type bwaVLNeighborAuDataEncyptOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BwaVLNeighborAuDataEncyptOption_Type.__name__ = "Integer32"
_BwaVLNeighborAuDataEncyptOption_Object = MibTableColumn
bwaVLNeighborAuDataEncyptOption = _BwaVLNeighborAuDataEncyptOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 11, 4, 1, 20),
    _BwaVLNeighborAuDataEncyptOption_Type()
)
bwaVLNeighborAuDataEncyptOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLNeighborAuDataEncyptOption.setStatus("current")


class _BwaVLNeighborAuPerSuDistanceLearning_Type(Integer32):
    """Custom type bwaVLNeighborAuPerSuDistanceLearning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BwaVLNeighborAuPerSuDistanceLearning_Type.__name__ = "Integer32"
_BwaVLNeighborAuPerSuDistanceLearning_Object = MibTableColumn
bwaVLNeighborAuPerSuDistanceLearning = _BwaVLNeighborAuPerSuDistanceLearning_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 11, 4, 1, 21),
    _BwaVLNeighborAuPerSuDistanceLearning_Type()
)
bwaVLNeighborAuPerSuDistanceLearning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLNeighborAuPerSuDistanceLearning.setStatus("current")
_BwaVLFrequencyDefinition_ObjectIdentity = ObjectIdentity
bwaVLFrequencyDefinition = _BwaVLFrequencyDefinition_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12)
)
_BwaVLSubBandLowerFrequency_Type = Integer32
_BwaVLSubBandLowerFrequency_Object = MibScalar
bwaVLSubBandLowerFrequency = _BwaVLSubBandLowerFrequency_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 1),
    _BwaVLSubBandLowerFrequency_Type()
)
bwaVLSubBandLowerFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLSubBandLowerFrequency.setStatus("obsolete")
_BwaVLSubBandUpperFrequency_Type = Integer32
_BwaVLSubBandUpperFrequency_Object = MibScalar
bwaVLSubBandUpperFrequency = _BwaVLSubBandUpperFrequency_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 2),
    _BwaVLSubBandUpperFrequency_Type()
)
bwaVLSubBandUpperFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLSubBandUpperFrequency.setStatus("obsolete")


class _BwaVLScanningStep_Type(Integer32):
    """Custom type bwaVLScanningStep based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("mhz-5", 1),
          ("mhz-10", 2),
          ("mhz-20", 3),
          ("na", 255))
    )


_BwaVLScanningStep_Type.__name__ = "Integer32"
_BwaVLScanningStep_Object = MibScalar
bwaVLScanningStep = _BwaVLScanningStep_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 3),
    _BwaVLScanningStep_Type()
)
bwaVLScanningStep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLScanningStep.setStatus("current")
_BwaVLFrequencySubsetTable_Object = MibTable
bwaVLFrequencySubsetTable = _BwaVLFrequencySubsetTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 4)
)
if mibBuilder.loadTexts:
    bwaVLFrequencySubsetTable.setStatus("current")
_BwaVLFrequencySubsetEntry_Object = MibTableRow
bwaVLFrequencySubsetEntry = _BwaVLFrequencySubsetEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 4, 1)
)
bwaVLFrequencySubsetEntry.setIndexNames(
    (0, "BWA-DOT11-WLAN-MIB", "bwaVLFrequencySubsetTableIdx"),
)
if mibBuilder.loadTexts:
    bwaVLFrequencySubsetEntry.setStatus("current")


class _BwaVLFrequencySubsetTableIdx_Type(Integer32):
    """Custom type bwaVLFrequencySubsetTableIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_BwaVLFrequencySubsetTableIdx_Type.__name__ = "Integer32"
_BwaVLFrequencySubsetTableIdx_Object = MibTableColumn
bwaVLFrequencySubsetTableIdx = _BwaVLFrequencySubsetTableIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 4, 1, 1),
    _BwaVLFrequencySubsetTableIdx_Type()
)
bwaVLFrequencySubsetTableIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLFrequencySubsetTableIdx.setStatus("current")
_BwaVLFrequencySubsetFrequency_Type = Integer32
_BwaVLFrequencySubsetFrequency_Object = MibTableColumn
bwaVLFrequencySubsetFrequency = _BwaVLFrequencySubsetFrequency_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 4, 1, 2),
    _BwaVLFrequencySubsetFrequency_Type()
)
bwaVLFrequencySubsetFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLFrequencySubsetFrequency.setStatus("current")


class _BwaVLFrequencySubsetActive_Type(Integer32):
    """Custom type bwaVLFrequencySubsetActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notActive", 2))
    )


_BwaVLFrequencySubsetActive_Type.__name__ = "Integer32"
_BwaVLFrequencySubsetActive_Object = MibTableColumn
bwaVLFrequencySubsetActive = _BwaVLFrequencySubsetActive_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 4, 1, 3),
    _BwaVLFrequencySubsetActive_Type()
)
bwaVLFrequencySubsetActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLFrequencySubsetActive.setStatus("current")
_BwaVLFrequencySubsetFrequencyNew_Type = DisplayString
_BwaVLFrequencySubsetFrequencyNew_Object = MibTableColumn
bwaVLFrequencySubsetFrequencyNew = _BwaVLFrequencySubsetFrequencyNew_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 4, 1, 4),
    _BwaVLFrequencySubsetFrequencyNew_Type()
)
bwaVLFrequencySubsetFrequencyNew.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLFrequencySubsetFrequencyNew.setStatus("current")


class _BwaVLSetSelectedFreqSubset_Type(Integer32):
    """Custom type bwaVLSetSelectedFreqSubset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("setSelectedFreqsSubset", 1),
          ("cancel", 2))
    )


_BwaVLSetSelectedFreqSubset_Type.__name__ = "Integer32"
_BwaVLSetSelectedFreqSubset_Object = MibScalar
bwaVLSetSelectedFreqSubset = _BwaVLSetSelectedFreqSubset_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 5),
    _BwaVLSetSelectedFreqSubset_Type()
)
bwaVLSetSelectedFreqSubset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLSetSelectedFreqSubset.setStatus("current")
_BwaVLCurrentFrequencySubsetTable_Object = MibTable
bwaVLCurrentFrequencySubsetTable = _BwaVLCurrentFrequencySubsetTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 6)
)
if mibBuilder.loadTexts:
    bwaVLCurrentFrequencySubsetTable.setStatus("current")
_BwaVLCurrentFrequencySubsetEntry_Object = MibTableRow
bwaVLCurrentFrequencySubsetEntry = _BwaVLCurrentFrequencySubsetEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 6, 1)
)
bwaVLCurrentFrequencySubsetEntry.setIndexNames(
    (0, "BWA-DOT11-WLAN-MIB", "bwaVLCurrentFrequencySubsetTableIdx"),
)
if mibBuilder.loadTexts:
    bwaVLCurrentFrequencySubsetEntry.setStatus("current")


class _BwaVLCurrentFrequencySubsetTableIdx_Type(Integer32):
    """Custom type bwaVLCurrentFrequencySubsetTableIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_BwaVLCurrentFrequencySubsetTableIdx_Type.__name__ = "Integer32"
_BwaVLCurrentFrequencySubsetTableIdx_Object = MibTableColumn
bwaVLCurrentFrequencySubsetTableIdx = _BwaVLCurrentFrequencySubsetTableIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 6, 1, 1),
    _BwaVLCurrentFrequencySubsetTableIdx_Type()
)
bwaVLCurrentFrequencySubsetTableIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLCurrentFrequencySubsetTableIdx.setStatus("current")
_BwaVLCurrentFrequencySubsetFrequency_Type = Integer32
_BwaVLCurrentFrequencySubsetFrequency_Object = MibTableColumn
bwaVLCurrentFrequencySubsetFrequency = _BwaVLCurrentFrequencySubsetFrequency_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 6, 1, 2),
    _BwaVLCurrentFrequencySubsetFrequency_Type()
)
bwaVLCurrentFrequencySubsetFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLCurrentFrequencySubsetFrequency.setStatus("current")
_BwaVLCurrentFrequencySubsetFrequencyNew_Type = DisplayString
_BwaVLCurrentFrequencySubsetFrequencyNew_Object = MibTableColumn
bwaVLCurrentFrequencySubsetFrequencyNew = _BwaVLCurrentFrequencySubsetFrequencyNew_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 6, 1, 3),
    _BwaVLCurrentFrequencySubsetFrequencyNew_Type()
)
bwaVLCurrentFrequencySubsetFrequencyNew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLCurrentFrequencySubsetFrequencyNew.setStatus("current")
_BwaVLCurrentAUOperatingFrequency_Type = Integer32
_BwaVLCurrentAUOperatingFrequency_Object = MibScalar
bwaVLCurrentAUOperatingFrequency = _BwaVLCurrentAUOperatingFrequency_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 7),
    _BwaVLCurrentAUOperatingFrequency_Type()
)
bwaVLCurrentAUOperatingFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLCurrentAUOperatingFrequency.setStatus("current")
_BwaVLAUDefinedFrequency_Type = Integer32
_BwaVLAUDefinedFrequency_Object = MibScalar
bwaVLAUDefinedFrequency = _BwaVLAUDefinedFrequency_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 8),
    _BwaVLAUDefinedFrequency_Type()
)
bwaVLAUDefinedFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLAUDefinedFrequency.setStatus("current")
_BwaVLCurrentSUOperatingFrequency_Type = DisplayString
_BwaVLCurrentSUOperatingFrequency_Object = MibScalar
bwaVLCurrentSUOperatingFrequency = _BwaVLCurrentSUOperatingFrequency_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 9),
    _BwaVLCurrentSUOperatingFrequency_Type()
)
bwaVLCurrentSUOperatingFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLCurrentSUOperatingFrequency.setStatus("current")
_BwaVLSubBandSelect_ObjectIdentity = ObjectIdentity
bwaVLSubBandSelect = _BwaVLSubBandSelect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 10)
)
_BwaVLSelectSubBandIndex_Type = Integer32
_BwaVLSelectSubBandIndex_Object = MibScalar
bwaVLSelectSubBandIndex = _BwaVLSelectSubBandIndex_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 10, 1),
    _BwaVLSelectSubBandIndex_Type()
)
bwaVLSelectSubBandIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLSelectSubBandIndex.setStatus("current")
_BwaVLDFSParameters_ObjectIdentity = ObjectIdentity
bwaVLDFSParameters = _BwaVLDFSParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 11)
)


class _BwaVLDFSOption_Type(Integer32):
    """Custom type bwaVLDFSOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BwaVLDFSOption_Type.__name__ = "Integer32"
_BwaVLDFSOption_Object = MibScalar
bwaVLDFSOption = _BwaVLDFSOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 11, 1),
    _BwaVLDFSOption_Type()
)
bwaVLDFSOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLDFSOption.setStatus("current")
_BwaVLDFSChannelCheckTime_Type = Integer32
_BwaVLDFSChannelCheckTime_Object = MibScalar
bwaVLDFSChannelCheckTime = _BwaVLDFSChannelCheckTime_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 11, 3),
    _BwaVLDFSChannelCheckTime_Type()
)
bwaVLDFSChannelCheckTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLDFSChannelCheckTime.setStatus("current")
_BwaVLDFSChannelAvoidancePeriod_Type = Integer32
_BwaVLDFSChannelAvoidancePeriod_Object = MibScalar
bwaVLDFSChannelAvoidancePeriod = _BwaVLDFSChannelAvoidancePeriod_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 11, 4),
    _BwaVLDFSChannelAvoidancePeriod_Type()
)
bwaVLDFSChannelAvoidancePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLDFSChannelAvoidancePeriod.setStatus("current")


class _BwaVLDFSSuWaitingOption_Type(Integer32):
    """Custom type bwaVLDFSSuWaitingOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BwaVLDFSSuWaitingOption_Type.__name__ = "Integer32"
_BwaVLDFSSuWaitingOption_Object = MibScalar
bwaVLDFSSuWaitingOption = _BwaVLDFSSuWaitingOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 11, 5),
    _BwaVLDFSSuWaitingOption_Type()
)
bwaVLDFSSuWaitingOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLDFSSuWaitingOption.setStatus("current")


class _BwaVLDFSClearRadarDetectedChannelsAfterReset_Type(Integer32):
    """Custom type bwaVLDFSClearRadarDetectedChannelsAfterReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("cancel", 1),
          ("clearRadarChannels", 2),
          ("na", 255))
    )


_BwaVLDFSClearRadarDetectedChannelsAfterReset_Type.__name__ = "Integer32"
_BwaVLDFSClearRadarDetectedChannelsAfterReset_Object = MibScalar
bwaVLDFSClearRadarDetectedChannelsAfterReset = _BwaVLDFSClearRadarDetectedChannelsAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 11, 6),
    _BwaVLDFSClearRadarDetectedChannelsAfterReset_Type()
)
bwaVLDFSClearRadarDetectedChannelsAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLDFSClearRadarDetectedChannelsAfterReset.setStatus("current")
_BwaVLDFSRadarDetectionChannelsTable_Object = MibTable
bwaVLDFSRadarDetectionChannelsTable = _BwaVLDFSRadarDetectionChannelsTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 11, 7)
)
if mibBuilder.loadTexts:
    bwaVLDFSRadarDetectionChannelsTable.setStatus("current")
_BwaVLDFSRadarDetectionChannelsEntry_Object = MibTableRow
bwaVLDFSRadarDetectionChannelsEntry = _BwaVLDFSRadarDetectionChannelsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 11, 7, 1)
)
bwaVLDFSRadarDetectionChannelsEntry.setIndexNames(
    (0, "BWA-DOT11-WLAN-MIB", "bwaVLDFSChannelIdx"),
)
if mibBuilder.loadTexts:
    bwaVLDFSRadarDetectionChannelsEntry.setStatus("current")


class _BwaVLDFSChannelIdx_Type(Integer32):
    """Custom type bwaVLDFSChannelIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_BwaVLDFSChannelIdx_Type.__name__ = "Integer32"
_BwaVLDFSChannelIdx_Object = MibTableColumn
bwaVLDFSChannelIdx = _BwaVLDFSChannelIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 11, 7, 1, 1),
    _BwaVLDFSChannelIdx_Type()
)
bwaVLDFSChannelIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLDFSChannelIdx.setStatus("current")
_BwaVLDFSChannelFrequency_Type = Integer32
_BwaVLDFSChannelFrequency_Object = MibTableColumn
bwaVLDFSChannelFrequency = _BwaVLDFSChannelFrequency_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 11, 7, 1, 2),
    _BwaVLDFSChannelFrequency_Type()
)
bwaVLDFSChannelFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLDFSChannelFrequency.setStatus("current")


class _BwaVLDFSChannelRadarStatus_Type(Integer32):
    """Custom type bwaVLDFSChannelRadarStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("radarFree", 1),
          ("adjacentToRadar", 2),
          ("radarDetected", 3))
    )


_BwaVLDFSChannelRadarStatus_Type.__name__ = "Integer32"
_BwaVLDFSChannelRadarStatus_Object = MibTableColumn
bwaVLDFSChannelRadarStatus = _BwaVLDFSChannelRadarStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 11, 7, 1, 3),
    _BwaVLDFSChannelRadarStatus_Type()
)
bwaVLDFSChannelRadarStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLDFSChannelRadarStatus.setStatus("current")
_BwaVLDFSChannelFrequencyNew_Type = DisplayString
_BwaVLDFSChannelFrequencyNew_Object = MibTableColumn
bwaVLDFSChannelFrequencyNew = _BwaVLDFSChannelFrequencyNew_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 11, 7, 1, 4),
    _BwaVLDFSChannelFrequencyNew_Type()
)
bwaVLDFSChannelFrequencyNew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLDFSChannelFrequencyNew.setStatus("current")
_BwaVLDFSMinimumPulsesToDetect_Type = Integer32
_BwaVLDFSMinimumPulsesToDetect_Object = MibScalar
bwaVLDFSMinimumPulsesToDetect = _BwaVLDFSMinimumPulsesToDetect_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 11, 8),
    _BwaVLDFSMinimumPulsesToDetect_Type()
)
bwaVLDFSMinimumPulsesToDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLDFSMinimumPulsesToDetect.setStatus("current")
_BwaVLDFSChannelReuseParameters_ObjectIdentity = ObjectIdentity
bwaVLDFSChannelReuseParameters = _BwaVLDFSChannelReuseParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 11, 9)
)


class _BwaVLDFSChannelReuseOption_Type(Integer32):
    """Custom type bwaVLDFSChannelReuseOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BwaVLDFSChannelReuseOption_Type.__name__ = "Integer32"
_BwaVLDFSChannelReuseOption_Object = MibScalar
bwaVLDFSChannelReuseOption = _BwaVLDFSChannelReuseOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 11, 9, 1),
    _BwaVLDFSChannelReuseOption_Type()
)
bwaVLDFSChannelReuseOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLDFSChannelReuseOption.setStatus("current")
_BwaVLDFSRadarActivityAssessmentPeriod_Type = Integer32
_BwaVLDFSRadarActivityAssessmentPeriod_Object = MibScalar
bwaVLDFSRadarActivityAssessmentPeriod = _BwaVLDFSRadarActivityAssessmentPeriod_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 11, 9, 2),
    _BwaVLDFSRadarActivityAssessmentPeriod_Type()
)
bwaVLDFSRadarActivityAssessmentPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLDFSRadarActivityAssessmentPeriod.setStatus("current")
_BwaVLDFSMaximumNumberOfDetectionsInAssessmentPeriod_Type = Integer32
_BwaVLDFSMaximumNumberOfDetectionsInAssessmentPeriod_Object = MibScalar
bwaVLDFSMaximumNumberOfDetectionsInAssessmentPeriod = _BwaVLDFSMaximumNumberOfDetectionsInAssessmentPeriod_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 11, 9, 3),
    _BwaVLDFSMaximumNumberOfDetectionsInAssessmentPeriod_Type()
)
bwaVLDFSMaximumNumberOfDetectionsInAssessmentPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLDFSMaximumNumberOfDetectionsInAssessmentPeriod.setStatus("current")


class _BwaVLCountryCodeLearningBySU_Type(Integer32):
    """Custom type bwaVLCountryCodeLearningBySU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BwaVLCountryCodeLearningBySU_Type.__name__ = "Integer32"
_BwaVLCountryCodeLearningBySU_Object = MibScalar
bwaVLCountryCodeLearningBySU = _BwaVLCountryCodeLearningBySU_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 12),
    _BwaVLCountryCodeLearningBySU_Type()
)
bwaVLCountryCodeLearningBySU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLCountryCodeLearningBySU.setStatus("current")
_BwaVLCurrentAUOperatingFrequencyNew_Type = DisplayString
_BwaVLCurrentAUOperatingFrequencyNew_Object = MibScalar
bwaVLCurrentAUOperatingFrequencyNew = _BwaVLCurrentAUOperatingFrequencyNew_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 13),
    _BwaVLCurrentAUOperatingFrequencyNew_Type()
)
bwaVLCurrentAUOperatingFrequencyNew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLCurrentAUOperatingFrequencyNew.setStatus("current")
_BwaVLAUDefinedFrequencyNew_Type = DisplayString
_BwaVLAUDefinedFrequencyNew_Object = MibScalar
bwaVLAUDefinedFrequencyNew = _BwaVLAUDefinedFrequencyNew_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 14),
    _BwaVLAUDefinedFrequencyNew_Type()
)
bwaVLAUDefinedFrequencyNew.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLAUDefinedFrequencyNew.setStatus("current")
_BwaVLAutoSubBandSelect_ObjectIdentity = ObjectIdentity
bwaVLAutoSubBandSelect = _BwaVLAutoSubBandSelect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 15)
)


class _BwaVLAutoSubBandSelectedFreqSubset_Type(Integer32):
    """Custom type bwaVLAutoSubBandSelectedFreqSubset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("setAllSelectedFreqsSubset", 1),
          ("cancel", 2))
    )


_BwaVLAutoSubBandSelectedFreqSubset_Type.__name__ = "Integer32"
_BwaVLAutoSubBandSelectedFreqSubset_Object = MibScalar
bwaVLAutoSubBandSelectedFreqSubset = _BwaVLAutoSubBandSelectedFreqSubset_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 15, 1),
    _BwaVLAutoSubBandSelectedFreqSubset_Type()
)
bwaVLAutoSubBandSelectedFreqSubset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLAutoSubBandSelectedFreqSubset.setStatus("current")
_BwaVLAutoSubBandFrequencySubsetTable_Object = MibTable
bwaVLAutoSubBandFrequencySubsetTable = _BwaVLAutoSubBandFrequencySubsetTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 15, 2)
)
if mibBuilder.loadTexts:
    bwaVLAutoSubBandFrequencySubsetTable.setStatus("current")
_BwaVLAutoSubBandFrequencySubsetEntry_Object = MibTableRow
bwaVLAutoSubBandFrequencySubsetEntry = _BwaVLAutoSubBandFrequencySubsetEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 15, 2, 1)
)
bwaVLAutoSubBandFrequencySubsetEntry.setIndexNames(
    (0, "BWA-DOT11-WLAN-MIB", "bwaVLAutoSubBandFrequencySubsetBandIdx"),
    (0, "BWA-DOT11-WLAN-MIB", "bwaVLAutoSubBandFrequencySubsetFrequencyIdx"),
)
if mibBuilder.loadTexts:
    bwaVLAutoSubBandFrequencySubsetEntry.setStatus("current")


class _BwaVLAutoSubBandFrequencySubsetBandIdx_Type(Integer32):
    """Custom type bwaVLAutoSubBandFrequencySubsetBandIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_BwaVLAutoSubBandFrequencySubsetBandIdx_Type.__name__ = "Integer32"
_BwaVLAutoSubBandFrequencySubsetBandIdx_Object = MibTableColumn
bwaVLAutoSubBandFrequencySubsetBandIdx = _BwaVLAutoSubBandFrequencySubsetBandIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 15, 2, 1, 1),
    _BwaVLAutoSubBandFrequencySubsetBandIdx_Type()
)
bwaVLAutoSubBandFrequencySubsetBandIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLAutoSubBandFrequencySubsetBandIdx.setStatus("current")


class _BwaVLAutoSubBandFrequencySubsetFrequencyIdx_Type(Integer32):
    """Custom type bwaVLAutoSubBandFrequencySubsetFrequencyIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_BwaVLAutoSubBandFrequencySubsetFrequencyIdx_Type.__name__ = "Integer32"
_BwaVLAutoSubBandFrequencySubsetFrequencyIdx_Object = MibTableColumn
bwaVLAutoSubBandFrequencySubsetFrequencyIdx = _BwaVLAutoSubBandFrequencySubsetFrequencyIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 15, 2, 1, 2),
    _BwaVLAutoSubBandFrequencySubsetFrequencyIdx_Type()
)
bwaVLAutoSubBandFrequencySubsetFrequencyIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLAutoSubBandFrequencySubsetFrequencyIdx.setStatus("current")


class _BwaVLAutoSubBandFrequencySubsetActive_Type(Integer32):
    """Custom type bwaVLAutoSubBandFrequencySubsetActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notActive", 2))
    )


_BwaVLAutoSubBandFrequencySubsetActive_Type.__name__ = "Integer32"
_BwaVLAutoSubBandFrequencySubsetActive_Object = MibTableColumn
bwaVLAutoSubBandFrequencySubsetActive = _BwaVLAutoSubBandFrequencySubsetActive_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 15, 2, 1, 3),
    _BwaVLAutoSubBandFrequencySubsetActive_Type()
)
bwaVLAutoSubBandFrequencySubsetActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLAutoSubBandFrequencySubsetActive.setStatus("current")
_BwaVLAutoSubBandFrequencySubsetFrequency_Type = DisplayString
_BwaVLAutoSubBandFrequencySubsetFrequency_Object = MibTableColumn
bwaVLAutoSubBandFrequencySubsetFrequency = _BwaVLAutoSubBandFrequencySubsetFrequency_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 12, 15, 2, 1, 4),
    _BwaVLAutoSubBandFrequencySubsetFrequency_Type()
)
bwaVLAutoSubBandFrequencySubsetFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLAutoSubBandFrequencySubsetFrequency.setStatus("current")
_BwaVLATPC_ObjectIdentity = ObjectIdentity
bwaVLATPC = _BwaVLATPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 13)
)


class _BwaVLAtpcOption_Type(Integer32):
    """Custom type bwaVLAtpcOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BwaVLAtpcOption_Type.__name__ = "Integer32"
_BwaVLAtpcOption_Object = MibScalar
bwaVLAtpcOption = _BwaVLAtpcOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 13, 1),
    _BwaVLAtpcOption_Type()
)
bwaVLAtpcOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLAtpcOption.setStatus("current")
_BwaVLDeltaFromMinSNRLevel_Type = Integer32
_BwaVLDeltaFromMinSNRLevel_Object = MibScalar
bwaVLDeltaFromMinSNRLevel = _BwaVLDeltaFromMinSNRLevel_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 13, 2),
    _BwaVLDeltaFromMinSNRLevel_Type()
)
bwaVLDeltaFromMinSNRLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLDeltaFromMinSNRLevel.setStatus("current")
_BwaVLMinimumSNRLevel_Type = Integer32
_BwaVLMinimumSNRLevel_Object = MibScalar
bwaVLMinimumSNRLevel = _BwaVLMinimumSNRLevel_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 13, 3),
    _BwaVLMinimumSNRLevel_Type()
)
bwaVLMinimumSNRLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLMinimumSNRLevel.setStatus("current")
_BwaVLMinimumIntervalBetweenATPCMessages_Type = Integer32
_BwaVLMinimumIntervalBetweenATPCMessages_Object = MibScalar
bwaVLMinimumIntervalBetweenATPCMessages = _BwaVLMinimumIntervalBetweenATPCMessages_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 13, 4),
    _BwaVLMinimumIntervalBetweenATPCMessages_Type()
)
bwaVLMinimumIntervalBetweenATPCMessages.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLMinimumIntervalBetweenATPCMessages.setStatus("current")
_BwaVLPowerLevelSteps_Type = Integer32
_BwaVLPowerLevelSteps_Object = MibScalar
bwaVLPowerLevelSteps = _BwaVLPowerLevelSteps_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 13, 6),
    _BwaVLPowerLevelSteps_Type()
)
bwaVLPowerLevelSteps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLPowerLevelSteps.setStatus("current")
_BwaVLCellDistanceParameters_ObjectIdentity = ObjectIdentity
bwaVLCellDistanceParameters = _BwaVLCellDistanceParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 15)
)


class _BwaVLCellDistanceMode_Type(Integer32):
    """Custom type bwaVLCellDistanceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 2),
          ("na", 255))
    )


_BwaVLCellDistanceMode_Type.__name__ = "Integer32"
_BwaVLCellDistanceMode_Object = MibScalar
bwaVLCellDistanceMode = _BwaVLCellDistanceMode_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 15, 1),
    _BwaVLCellDistanceMode_Type()
)
bwaVLCellDistanceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLCellDistanceMode.setStatus("current")


class _BwaVLFairnessFactor_Type(Integer32):
    """Custom type bwaVLFairnessFactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            255
        )
    )
    namedValues = NamedValues(
        ("na", 255)
    )


_BwaVLFairnessFactor_Type.__name__ = "Integer32"
_BwaVLFairnessFactor_Object = MibScalar
bwaVLFairnessFactor = _BwaVLFairnessFactor_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 15, 2),
    _BwaVLFairnessFactor_Type()
)
bwaVLFairnessFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLFairnessFactor.setStatus("current")


class _BwaVLMeasuredCellDistance_Type(Integer32):
    """Custom type bwaVLMeasuredCellDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("below-2-Km", 1)
    )


_BwaVLMeasuredCellDistance_Type.__name__ = "Integer32"
_BwaVLMeasuredCellDistance_Object = MibScalar
bwaVLMeasuredCellDistance = _BwaVLMeasuredCellDistance_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 15, 3),
    _BwaVLMeasuredCellDistance_Type()
)
bwaVLMeasuredCellDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLMeasuredCellDistance.setStatus("current")
_BwaVLUnitWithMaxDistance_Type = MacAddress
_BwaVLUnitWithMaxDistance_Object = MibScalar
bwaVLUnitWithMaxDistance = _BwaVLUnitWithMaxDistance_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 15, 4),
    _BwaVLUnitWithMaxDistance_Type()
)
bwaVLUnitWithMaxDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLUnitWithMaxDistance.setStatus("current")


class _BwaVLPerSuDistanceLearning_Type(Integer32):
    """Custom type bwaVLPerSuDistanceLearning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_BwaVLPerSuDistanceLearning_Type.__name__ = "Integer32"
_BwaVLPerSuDistanceLearning_Object = MibScalar
bwaVLPerSuDistanceLearning = _BwaVLPerSuDistanceLearning_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 15, 5),
    _BwaVLPerSuDistanceLearning_Type()
)
bwaVLPerSuDistanceLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLPerSuDistanceLearning.setStatus("current")


class _BwaVLScanningMode_Type(Integer32):
    """Custom type bwaVLScanningMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("passive", 1),
          ("active", 2))
    )


_BwaVLScanningMode_Type.__name__ = "Integer32"
_BwaVLScanningMode_Object = MibScalar
bwaVLScanningMode = _BwaVLScanningMode_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 16),
    _BwaVLScanningMode_Type()
)
bwaVLScanningMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLScanningMode.setStatus("current")
_BwaVLAntennaGain_Type = DisplayString
_BwaVLAntennaGain_Object = MibScalar
bwaVLAntennaGain = _BwaVLAntennaGain_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 17),
    _BwaVLAntennaGain_Type()
)
bwaVLAntennaGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLAntennaGain.setStatus("current")
_BwaVLSpectrumAnalysisParameters_ObjectIdentity = ObjectIdentity
bwaVLSpectrumAnalysisParameters = _BwaVLSpectrumAnalysisParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 18)
)
_BwaVLSpectrumAnalysisChannelScanPeriod_Type = Integer32
_BwaVLSpectrumAnalysisChannelScanPeriod_Object = MibScalar
bwaVLSpectrumAnalysisChannelScanPeriod = _BwaVLSpectrumAnalysisChannelScanPeriod_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 18, 1),
    _BwaVLSpectrumAnalysisChannelScanPeriod_Type()
)
bwaVLSpectrumAnalysisChannelScanPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLSpectrumAnalysisChannelScanPeriod.setStatus("current")
_BwaVLSpectrumAnalysisScanCycles_Type = Integer32
_BwaVLSpectrumAnalysisScanCycles_Object = MibScalar
bwaVLSpectrumAnalysisScanCycles = _BwaVLSpectrumAnalysisScanCycles_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 18, 2),
    _BwaVLSpectrumAnalysisScanCycles_Type()
)
bwaVLSpectrumAnalysisScanCycles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLSpectrumAnalysisScanCycles.setStatus("current")


class _BwaVLAutomaticChannelSelection_Type(Integer32):
    """Custom type bwaVLAutomaticChannelSelection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BwaVLAutomaticChannelSelection_Type.__name__ = "Integer32"
_BwaVLAutomaticChannelSelection_Object = MibScalar
bwaVLAutomaticChannelSelection = _BwaVLAutomaticChannelSelection_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 18, 3),
    _BwaVLAutomaticChannelSelection_Type()
)
bwaVLAutomaticChannelSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLAutomaticChannelSelection.setStatus("current")


class _BwaVLSpectrumAnalysisActivation_Type(Integer32):
    """Custom type bwaVLSpectrumAnalysisActivation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cancelOperation", 1),
          ("activateNow", 2))
    )


_BwaVLSpectrumAnalysisActivation_Type.__name__ = "Integer32"
_BwaVLSpectrumAnalysisActivation_Object = MibScalar
bwaVLSpectrumAnalysisActivation = _BwaVLSpectrumAnalysisActivation_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 18, 4),
    _BwaVLSpectrumAnalysisActivation_Type()
)
bwaVLSpectrumAnalysisActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLSpectrumAnalysisActivation.setStatus("current")


class _BwaVLSpectrumAnalysisStatus_Type(Integer32):
    """Custom type bwaVLSpectrumAnalysisStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("currentlyActive", 2))
    )


_BwaVLSpectrumAnalysisStatus_Type.__name__ = "Integer32"
_BwaVLSpectrumAnalysisStatus_Object = MibScalar
bwaVLSpectrumAnalysisStatus = _BwaVLSpectrumAnalysisStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 18, 5),
    _BwaVLSpectrumAnalysisStatus_Type()
)
bwaVLSpectrumAnalysisStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLSpectrumAnalysisStatus.setStatus("current")


class _BwaVLResetSpectrumCounters_Type(Integer32):
    """Custom type bwaVLResetSpectrumCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cancelOperation", 1),
          ("resetCounters", 2))
    )


_BwaVLResetSpectrumCounters_Type.__name__ = "Integer32"
_BwaVLResetSpectrumCounters_Object = MibScalar
bwaVLResetSpectrumCounters = _BwaVLResetSpectrumCounters_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 18, 6),
    _BwaVLResetSpectrumCounters_Type()
)
bwaVLResetSpectrumCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLResetSpectrumCounters.setStatus("current")
_BwaVLSpectrumAnalysisInformationTable_Object = MibTable
bwaVLSpectrumAnalysisInformationTable = _BwaVLSpectrumAnalysisInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 18, 7)
)
if mibBuilder.loadTexts:
    bwaVLSpectrumAnalysisInformationTable.setStatus("current")
_BwaVLSpectrumAnalysisInformationEntry_Object = MibTableRow
bwaVLSpectrumAnalysisInformationEntry = _BwaVLSpectrumAnalysisInformationEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 18, 7, 1)
)
bwaVLSpectrumAnalysisInformationEntry.setIndexNames(
    (0, "BWA-DOT11-WLAN-MIB", "bwaVLSpectrumAnalysisInformationTableIdx"),
)
if mibBuilder.loadTexts:
    bwaVLSpectrumAnalysisInformationEntry.setStatus("current")


class _BwaVLSpectrumAnalysisInformationTableIdx_Type(Integer32):
    """Custom type bwaVLSpectrumAnalysisInformationTableIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_BwaVLSpectrumAnalysisInformationTableIdx_Type.__name__ = "Integer32"
_BwaVLSpectrumAnalysisInformationTableIdx_Object = MibTableColumn
bwaVLSpectrumAnalysisInformationTableIdx = _BwaVLSpectrumAnalysisInformationTableIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 18, 7, 1, 1),
    _BwaVLSpectrumAnalysisInformationTableIdx_Type()
)
bwaVLSpectrumAnalysisInformationTableIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLSpectrumAnalysisInformationTableIdx.setStatus("current")
_BwaVLSpectrumAnalysisInformationChannel_Type = DisplayString
_BwaVLSpectrumAnalysisInformationChannel_Object = MibTableColumn
bwaVLSpectrumAnalysisInformationChannel = _BwaVLSpectrumAnalysisInformationChannel_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 18, 7, 1, 2),
    _BwaVLSpectrumAnalysisInformationChannel_Type()
)
bwaVLSpectrumAnalysisInformationChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLSpectrumAnalysisInformationChannel.setStatus("current")
_BwaVLSpectrumAnalysisInformationSignalCount_Type = Integer32
_BwaVLSpectrumAnalysisInformationSignalCount_Object = MibTableColumn
bwaVLSpectrumAnalysisInformationSignalCount = _BwaVLSpectrumAnalysisInformationSignalCount_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 18, 7, 1, 3),
    _BwaVLSpectrumAnalysisInformationSignalCount_Type()
)
bwaVLSpectrumAnalysisInformationSignalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLSpectrumAnalysisInformationSignalCount.setStatus("current")
_BwaVLSpectrumAnalysisInformationSignalSNR_Type = Integer32
_BwaVLSpectrumAnalysisInformationSignalSNR_Object = MibTableColumn
bwaVLSpectrumAnalysisInformationSignalSNR = _BwaVLSpectrumAnalysisInformationSignalSNR_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 18, 7, 1, 4),
    _BwaVLSpectrumAnalysisInformationSignalSNR_Type()
)
bwaVLSpectrumAnalysisInformationSignalSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLSpectrumAnalysisInformationSignalSNR.setStatus("current")
_BwaVLSpectrumAnalysisInformationSignalWidth_Type = Integer32
_BwaVLSpectrumAnalysisInformationSignalWidth_Object = MibTableColumn
bwaVLSpectrumAnalysisInformationSignalWidth = _BwaVLSpectrumAnalysisInformationSignalWidth_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 18, 7, 1, 5),
    _BwaVLSpectrumAnalysisInformationSignalWidth_Type()
)
bwaVLSpectrumAnalysisInformationSignalWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLSpectrumAnalysisInformationSignalWidth.setStatus("current")
_BwaVLSpectrumAnalysisInformationOFDMFrames_Type = Integer32
_BwaVLSpectrumAnalysisInformationOFDMFrames_Object = MibTableColumn
bwaVLSpectrumAnalysisInformationOFDMFrames = _BwaVLSpectrumAnalysisInformationOFDMFrames_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 18, 7, 1, 6),
    _BwaVLSpectrumAnalysisInformationOFDMFrames_Type()
)
bwaVLSpectrumAnalysisInformationOFDMFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLSpectrumAnalysisInformationOFDMFrames.setStatus("current")
_BwaVLMaxNumOfAssociationsLimit_Type = Integer32
_BwaVLMaxNumOfAssociationsLimit_Object = MibScalar
bwaVLMaxNumOfAssociationsLimit = _BwaVLMaxNumOfAssociationsLimit_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 19),
    _BwaVLMaxNumOfAssociationsLimit_Type()
)
bwaVLMaxNumOfAssociationsLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLMaxNumOfAssociationsLimit.setStatus("current")
_BwaVLDisassociate_ObjectIdentity = ObjectIdentity
bwaVLDisassociate = _BwaVLDisassociate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 20)
)


class _BwaVLDisassociateAllSUs_Type(Integer32):
    """Custom type bwaVLDisassociateAllSUs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cancelOperation", 1),
          ("disassociateAllSUs", 2))
    )


_BwaVLDisassociateAllSUs_Type.__name__ = "Integer32"
_BwaVLDisassociateAllSUs_Object = MibScalar
bwaVLDisassociateAllSUs = _BwaVLDisassociateAllSUs_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 20, 1),
    _BwaVLDisassociateAllSUs_Type()
)
bwaVLDisassociateAllSUs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLDisassociateAllSUs.setStatus("current")
_BwaVLDisassociateSuByMacAddress_Type = MacAddress
_BwaVLDisassociateSuByMacAddress_Object = MibScalar
bwaVLDisassociateSuByMacAddress = _BwaVLDisassociateSuByMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 20, 2),
    _BwaVLDisassociateSuByMacAddress_Type()
)
bwaVLDisassociateSuByMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLDisassociateSuByMacAddress.setStatus("current")


class _BwaVLTxControl_Type(Integer32):
    """Custom type bwaVLTxControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_BwaVLTxControl_Type.__name__ = "Integer32"
_BwaVLTxControl_Object = MibScalar
bwaVLTxControl = _BwaVLTxControl_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 21),
    _BwaVLTxControl_Type()
)
bwaVLTxControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLTxControl.setStatus("current")


class _BwaVLLostBeaconsWatchdogThreshold_Type(Integer32):
    """Custom type bwaVLLostBeaconsWatchdogThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(100, 1000),
    )


_BwaVLLostBeaconsWatchdogThreshold_Type.__name__ = "Integer32"
_BwaVLLostBeaconsWatchdogThreshold_Object = MibScalar
bwaVLLostBeaconsWatchdogThreshold = _BwaVLLostBeaconsWatchdogThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 22),
    _BwaVLLostBeaconsWatchdogThreshold_Type()
)
bwaVLLostBeaconsWatchdogThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLLostBeaconsWatchdogThreshold.setStatus("current")
_BwaVLTransmitPower_Type = Integer32
_BwaVLTransmitPower_Object = MibScalar
bwaVLTransmitPower = _BwaVLTransmitPower_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 23),
    _BwaVLTransmitPower_Type()
)
bwaVLTransmitPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLTransmitPower.setStatus("current")
_BwaVLMaximumTxPower_Type = Integer32
_BwaVLMaximumTxPower_Object = MibScalar
bwaVLMaximumTxPower = _BwaVLMaximumTxPower_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 24),
    _BwaVLMaximumTxPower_Type()
)
bwaVLMaximumTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLMaximumTxPower.setStatus("current")
_BwaVLCountryCodeParameters_ObjectIdentity = ObjectIdentity
bwaVLCountryCodeParameters = _BwaVLCountryCodeParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 25)
)


class _BwaLCountryCodeReApply_Type(Integer32):
    """Custom type bwaLCountryCodeReApply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("reapply", 1),
          ("cancel", 2),
          ("na", 255))
    )


_BwaLCountryCodeReApply_Type.__name__ = "Integer32"
_BwaLCountryCodeReApply_Object = MibScalar
bwaLCountryCodeReApply = _BwaLCountryCodeReApply_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 6, 25, 1),
    _BwaLCountryCodeReApply_Type()
)
bwaLCountryCodeReApply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaLCountryCodeReApply.setStatus("current")
_BwaVLServiceParameters_ObjectIdentity = ObjectIdentity
bwaVLServiceParameters = _BwaVLServiceParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7)
)
_BwaVLMirDownlink_Type = Integer32
_BwaVLMirDownlink_Object = MibScalar
bwaVLMirDownlink = _BwaVLMirDownlink_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 2),
    _BwaVLMirDownlink_Type()
)
bwaVLMirDownlink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLMirDownlink.setStatus("current")
_BwaVLMirUplink_Type = Integer32
_BwaVLMirUplink_Object = MibScalar
bwaVLMirUplink = _BwaVLMirUplink_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 3),
    _BwaVLMirUplink_Type()
)
bwaVLMirUplink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLMirUplink.setStatus("current")
_BwaVLCirDownlink_Type = Integer32
_BwaVLCirDownlink_Object = MibScalar
bwaVLCirDownlink = _BwaVLCirDownlink_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 4),
    _BwaVLCirDownlink_Type()
)
bwaVLCirDownlink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLCirDownlink.setStatus("current")
_BwaVLCirUplink_Type = Integer32
_BwaVLCirUplink_Object = MibScalar
bwaVLCirUplink = _BwaVLCirUplink_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 5),
    _BwaVLCirUplink_Type()
)
bwaVLCirUplink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLCirUplink.setStatus("current")
_BwaVLMaxDelay_Type = Integer32
_BwaVLMaxDelay_Object = MibScalar
bwaVLMaxDelay = _BwaVLMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 6),
    _BwaVLMaxDelay_Type()
)
bwaVLMaxDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLMaxDelay.setStatus("current")
_BwaVLMaxBurstDuration_Type = Integer32
_BwaVLMaxBurstDuration_Object = MibScalar
bwaVLMaxBurstDuration = _BwaVLMaxBurstDuration_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 7),
    _BwaVLMaxBurstDuration_Type()
)
bwaVLMaxBurstDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLMaxBurstDuration.setStatus("current")
_BwaVLGracefulDegradationLimit_Type = Integer32
_BwaVLGracefulDegradationLimit_Object = MibScalar
bwaVLGracefulDegradationLimit = _BwaVLGracefulDegradationLimit_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 8),
    _BwaVLGracefulDegradationLimit_Type()
)
bwaVLGracefulDegradationLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLGracefulDegradationLimit.setStatus("current")


class _BwaVLMirOnlyOption_Type(Integer32):
    """Custom type bwaVLMirOnlyOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BwaVLMirOnlyOption_Type.__name__ = "Integer32"
_BwaVLMirOnlyOption_Object = MibScalar
bwaVLMirOnlyOption = _BwaVLMirOnlyOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 9),
    _BwaVLMirOnlyOption_Type()
)
bwaVLMirOnlyOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLMirOnlyOption.setStatus("current")
_BwaVLTrafficPrioritization_ObjectIdentity = ObjectIdentity
bwaVLTrafficPrioritization = _BwaVLTrafficPrioritization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10)
)
_BwaVLTrafficPriVLAN_ObjectIdentity = ObjectIdentity
bwaVLTrafficPriVLAN = _BwaVLTrafficPriVLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 1)
)


class _BwaVLVLANPriorityThreshold_Type(Integer32):
    """Custom type bwaVLVLANPriorityThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_BwaVLVLANPriorityThreshold_Type.__name__ = "Integer32"
_BwaVLVLANPriorityThreshold_Object = MibScalar
bwaVLVLANPriorityThreshold = _BwaVLVLANPriorityThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 1, 1),
    _BwaVLVLANPriorityThreshold_Type()
)
bwaVLVLANPriorityThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLVLANPriorityThreshold.setStatus("current")
_BwaVLTrafficPriIPToS_ObjectIdentity = ObjectIdentity
bwaVLTrafficPriIPToS = _BwaVLTrafficPriIPToS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 2)
)


class _BwaVLToSPrioritizationOption_Type(Integer32):
    """Custom type bwaVLToSPrioritizationOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("ipPrecedence", 2),
          ("dSCP", 3))
    )


_BwaVLToSPrioritizationOption_Type.__name__ = "Integer32"
_BwaVLToSPrioritizationOption_Object = MibScalar
bwaVLToSPrioritizationOption = _BwaVLToSPrioritizationOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 2, 1),
    _BwaVLToSPrioritizationOption_Type()
)
bwaVLToSPrioritizationOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLToSPrioritizationOption.setStatus("current")


class _BwaVLIPPrecedenceThreshold_Type(Integer32):
    """Custom type bwaVLIPPrecedenceThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_BwaVLIPPrecedenceThreshold_Type.__name__ = "Integer32"
_BwaVLIPPrecedenceThreshold_Object = MibScalar
bwaVLIPPrecedenceThreshold = _BwaVLIPPrecedenceThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 2, 2),
    _BwaVLIPPrecedenceThreshold_Type()
)
bwaVLIPPrecedenceThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLIPPrecedenceThreshold.setStatus("current")


class _BwaVLIPDSCPThreshold_Type(Integer32):
    """Custom type bwaVLIPDSCPThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_BwaVLIPDSCPThreshold_Type.__name__ = "Integer32"
_BwaVLIPDSCPThreshold_Object = MibScalar
bwaVLIPDSCPThreshold = _BwaVLIPDSCPThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 2, 3),
    _BwaVLIPDSCPThreshold_Type()
)
bwaVLIPDSCPThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLIPDSCPThreshold.setStatus("current")
_BwaVLTrafficPriUdpTcpPortRange_ObjectIdentity = ObjectIdentity
bwaVLTrafficPriUdpTcpPortRange = _BwaVLTrafficPriUdpTcpPortRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 3)
)


class _BwaVLUdpTcpPortRangePrioritizationOption_Type(Integer32):
    """Custom type bwaVLUdpTcpPortRangePrioritizationOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("udpOnly", 2),
          ("tcpOnly", 3),
          ("udpANDtcp", 4))
    )


_BwaVLUdpTcpPortRangePrioritizationOption_Type.__name__ = "Integer32"
_BwaVLUdpTcpPortRangePrioritizationOption_Object = MibScalar
bwaVLUdpTcpPortRangePrioritizationOption = _BwaVLUdpTcpPortRangePrioritizationOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 3, 1),
    _BwaVLUdpTcpPortRangePrioritizationOption_Type()
)
bwaVLUdpTcpPortRangePrioritizationOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLUdpTcpPortRangePrioritizationOption.setStatus("current")
_BwaVLUdpPortRangeConfig_ObjectIdentity = ObjectIdentity
bwaVLUdpPortRangeConfig = _BwaVLUdpPortRangeConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 3, 2)
)


class _BwaVLUdpPortPriRTPRTCP_Type(Integer32):
    """Custom type bwaVLUdpPortPriRTPRTCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rtpANDrtcp", 1),
          ("rtpOnly", 2))
    )


_BwaVLUdpPortPriRTPRTCP_Type.__name__ = "Integer32"
_BwaVLUdpPortPriRTPRTCP_Object = MibScalar
bwaVLUdpPortPriRTPRTCP = _BwaVLUdpPortPriRTPRTCP_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 3, 2, 1),
    _BwaVLUdpPortPriRTPRTCP_Type()
)
bwaVLUdpPortPriRTPRTCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLUdpPortPriRTPRTCP.setStatus("current")
_BwaVLUdpPortRangeNum_Type = Integer32
_BwaVLUdpPortRangeNum_Object = MibScalar
bwaVLUdpPortRangeNum = _BwaVLUdpPortRangeNum_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 3, 2, 2),
    _BwaVLUdpPortRangeNum_Type()
)
bwaVLUdpPortRangeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLUdpPortRangeNum.setStatus("current")
_BwaVLUdpPortRangeTable_Object = MibTable
bwaVLUdpPortRangeTable = _BwaVLUdpPortRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 3, 2, 3)
)
if mibBuilder.loadTexts:
    bwaVLUdpPortRangeTable.setStatus("current")
_BwaVLUdpPortRangeEntry_Object = MibTableRow
bwaVLUdpPortRangeEntry = _BwaVLUdpPortRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 3, 2, 3, 1)
)
bwaVLUdpPortRangeEntry.setIndexNames(
    (0, "BWA-DOT11-WLAN-MIB", "bwaVLUdpPortRangeIdx"),
)
if mibBuilder.loadTexts:
    bwaVLUdpPortRangeEntry.setStatus("current")


class _BwaVLUdpPortRangeStart_Type(Integer32):
    """Custom type bwaVLUdpPortRangeStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BwaVLUdpPortRangeStart_Type.__name__ = "Integer32"
_BwaVLUdpPortRangeStart_Object = MibTableColumn
bwaVLUdpPortRangeStart = _BwaVLUdpPortRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 3, 2, 3, 1, 1),
    _BwaVLUdpPortRangeStart_Type()
)
bwaVLUdpPortRangeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLUdpPortRangeStart.setStatus("current")


class _BwaVLUdpPortRangeEnd_Type(Integer32):
    """Custom type bwaVLUdpPortRangeEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BwaVLUdpPortRangeEnd_Type.__name__ = "Integer32"
_BwaVLUdpPortRangeEnd_Object = MibTableColumn
bwaVLUdpPortRangeEnd = _BwaVLUdpPortRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 3, 2, 3, 1, 2),
    _BwaVLUdpPortRangeEnd_Type()
)
bwaVLUdpPortRangeEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLUdpPortRangeEnd.setStatus("current")


class _BwaVLUdpPortRangeIdx_Type(Integer32):
    """Custom type bwaVLUdpPortRangeIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_BwaVLUdpPortRangeIdx_Type.__name__ = "Integer32"
_BwaVLUdpPortRangeIdx_Object = MibTableColumn
bwaVLUdpPortRangeIdx = _BwaVLUdpPortRangeIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 3, 2, 3, 1, 3),
    _BwaVLUdpPortRangeIdx_Type()
)
bwaVLUdpPortRangeIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLUdpPortRangeIdx.setStatus("current")


class _BwaVLUdpPortRangeAdd_Type(DisplayString):
    """Custom type bwaVLUdpPortRangeAdd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_BwaVLUdpPortRangeAdd_Type.__name__ = "DisplayString"
_BwaVLUdpPortRangeAdd_Object = MibScalar
bwaVLUdpPortRangeAdd = _BwaVLUdpPortRangeAdd_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 3, 2, 4),
    _BwaVLUdpPortRangeAdd_Type()
)
bwaVLUdpPortRangeAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLUdpPortRangeAdd.setStatus("current")


class _BwaVLUdpPortRangeDelete_Type(DisplayString):
    """Custom type bwaVLUdpPortRangeDelete based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_BwaVLUdpPortRangeDelete_Type.__name__ = "DisplayString"
_BwaVLUdpPortRangeDelete_Object = MibScalar
bwaVLUdpPortRangeDelete = _BwaVLUdpPortRangeDelete_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 3, 2, 5),
    _BwaVLUdpPortRangeDelete_Type()
)
bwaVLUdpPortRangeDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLUdpPortRangeDelete.setStatus("current")


class _BwaVLUdpPortRangeDeleteAll_Type(Integer32):
    """Custom type bwaVLUdpPortRangeDeleteAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deleteAll", 1),
          ("cancelOperation", 2))
    )


_BwaVLUdpPortRangeDeleteAll_Type.__name__ = "Integer32"
_BwaVLUdpPortRangeDeleteAll_Object = MibScalar
bwaVLUdpPortRangeDeleteAll = _BwaVLUdpPortRangeDeleteAll_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 3, 2, 6),
    _BwaVLUdpPortRangeDeleteAll_Type()
)
bwaVLUdpPortRangeDeleteAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLUdpPortRangeDeleteAll.setStatus("current")
_BwaVLTcpPortRangeConfig_ObjectIdentity = ObjectIdentity
bwaVLTcpPortRangeConfig = _BwaVLTcpPortRangeConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 3, 3)
)


class _BwaVLTcpPortPriRTPRTCP_Type(Integer32):
    """Custom type bwaVLTcpPortPriRTPRTCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rtpANDrtcp", 1),
          ("rtpOnly", 2))
    )


_BwaVLTcpPortPriRTPRTCP_Type.__name__ = "Integer32"
_BwaVLTcpPortPriRTPRTCP_Object = MibScalar
bwaVLTcpPortPriRTPRTCP = _BwaVLTcpPortPriRTPRTCP_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 3, 3, 1),
    _BwaVLTcpPortPriRTPRTCP_Type()
)
bwaVLTcpPortPriRTPRTCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLTcpPortPriRTPRTCP.setStatus("current")
_BwaVLTcpPortRangeNum_Type = Integer32
_BwaVLTcpPortRangeNum_Object = MibScalar
bwaVLTcpPortRangeNum = _BwaVLTcpPortRangeNum_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 3, 3, 2),
    _BwaVLTcpPortRangeNum_Type()
)
bwaVLTcpPortRangeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLTcpPortRangeNum.setStatus("current")
_BwaVLTcpPortRangeTable_Object = MibTable
bwaVLTcpPortRangeTable = _BwaVLTcpPortRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 3, 3, 3)
)
if mibBuilder.loadTexts:
    bwaVLTcpPortRangeTable.setStatus("current")
_BwaVLTcpPortRangeEntry_Object = MibTableRow
bwaVLTcpPortRangeEntry = _BwaVLTcpPortRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 3, 3, 3, 1)
)
bwaVLTcpPortRangeEntry.setIndexNames(
    (0, "BWA-DOT11-WLAN-MIB", "bwaVLTcpPortRangeIdx"),
)
if mibBuilder.loadTexts:
    bwaVLTcpPortRangeEntry.setStatus("current")


class _BwaVLTcpPortRangeStart_Type(Integer32):
    """Custom type bwaVLTcpPortRangeStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BwaVLTcpPortRangeStart_Type.__name__ = "Integer32"
_BwaVLTcpPortRangeStart_Object = MibTableColumn
bwaVLTcpPortRangeStart = _BwaVLTcpPortRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 3, 3, 3, 1, 1),
    _BwaVLTcpPortRangeStart_Type()
)
bwaVLTcpPortRangeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLTcpPortRangeStart.setStatus("current")


class _BwaVLTcpPortRangeEnd_Type(Integer32):
    """Custom type bwaVLTcpPortRangeEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BwaVLTcpPortRangeEnd_Type.__name__ = "Integer32"
_BwaVLTcpPortRangeEnd_Object = MibTableColumn
bwaVLTcpPortRangeEnd = _BwaVLTcpPortRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 3, 3, 3, 1, 2),
    _BwaVLTcpPortRangeEnd_Type()
)
bwaVLTcpPortRangeEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLTcpPortRangeEnd.setStatus("current")


class _BwaVLTcpPortRangeIdx_Type(Integer32):
    """Custom type bwaVLTcpPortRangeIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_BwaVLTcpPortRangeIdx_Type.__name__ = "Integer32"
_BwaVLTcpPortRangeIdx_Object = MibTableColumn
bwaVLTcpPortRangeIdx = _BwaVLTcpPortRangeIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 3, 3, 3, 1, 3),
    _BwaVLTcpPortRangeIdx_Type()
)
bwaVLTcpPortRangeIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLTcpPortRangeIdx.setStatus("current")


class _BwaVLTcpPortRangeAdd_Type(DisplayString):
    """Custom type bwaVLTcpPortRangeAdd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_BwaVLTcpPortRangeAdd_Type.__name__ = "DisplayString"
_BwaVLTcpPortRangeAdd_Object = MibScalar
bwaVLTcpPortRangeAdd = _BwaVLTcpPortRangeAdd_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 3, 3, 4),
    _BwaVLTcpPortRangeAdd_Type()
)
bwaVLTcpPortRangeAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLTcpPortRangeAdd.setStatus("current")


class _BwaVLTcpPortRangeDelete_Type(DisplayString):
    """Custom type bwaVLTcpPortRangeDelete based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_BwaVLTcpPortRangeDelete_Type.__name__ = "DisplayString"
_BwaVLTcpPortRangeDelete_Object = MibScalar
bwaVLTcpPortRangeDelete = _BwaVLTcpPortRangeDelete_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 3, 3, 5),
    _BwaVLTcpPortRangeDelete_Type()
)
bwaVLTcpPortRangeDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLTcpPortRangeDelete.setStatus("current")


class _BwaVLTcpPortRangeDeleteAll_Type(Integer32):
    """Custom type bwaVLTcpPortRangeDeleteAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deleteAll", 1),
          ("cancelOperation", 2))
    )


_BwaVLTcpPortRangeDeleteAll_Type.__name__ = "Integer32"
_BwaVLTcpPortRangeDeleteAll_Object = MibScalar
bwaVLTcpPortRangeDeleteAll = _BwaVLTcpPortRangeDeleteAll_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 3, 3, 6),
    _BwaVLTcpPortRangeDeleteAll_Type()
)
bwaVLTcpPortRangeDeleteAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLTcpPortRangeDeleteAll.setStatus("current")
_BwaVLWirelessLinkPrioritization_ObjectIdentity = ObjectIdentity
bwaVLWirelessLinkPrioritization = _BwaVLWirelessLinkPrioritization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 4)
)


class _BwaVLWirelessLinkPrioritizationOption_Type(Integer32):
    """Custom type bwaVLWirelessLinkPrioritizationOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BwaVLWirelessLinkPrioritizationOption_Type.__name__ = "Integer32"
_BwaVLWirelessLinkPrioritizationOption_Object = MibScalar
bwaVLWirelessLinkPrioritizationOption = _BwaVLWirelessLinkPrioritizationOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 4, 1),
    _BwaVLWirelessLinkPrioritizationOption_Type()
)
bwaVLWirelessLinkPrioritizationOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLWirelessLinkPrioritizationOption.setStatus("current")


class _BwaVLlowPriorityAIFS_Type(Integer32):
    """Custom type bwaVLlowPriorityAIFS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 254),
    )


_BwaVLlowPriorityAIFS_Type.__name__ = "Integer32"
_BwaVLlowPriorityAIFS_Object = MibScalar
bwaVLlowPriorityAIFS = _BwaVLlowPriorityAIFS_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 4, 2),
    _BwaVLlowPriorityAIFS_Type()
)
bwaVLlowPriorityAIFS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLlowPriorityAIFS.setStatus("current")


class _BwaVLHWRetriesHighPriority_Type(Integer32):
    """Custom type bwaVLHWRetriesHighPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_BwaVLHWRetriesHighPriority_Type.__name__ = "Integer32"
_BwaVLHWRetriesHighPriority_Object = MibScalar
bwaVLHWRetriesHighPriority = _BwaVLHWRetriesHighPriority_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 4, 3),
    _BwaVLHWRetriesHighPriority_Type()
)
bwaVLHWRetriesHighPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLHWRetriesHighPriority.setStatus("current")


class _BwaVLHWRetriesLowPriority_Type(Integer32):
    """Custom type bwaVLHWRetriesLowPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_BwaVLHWRetriesLowPriority_Type.__name__ = "Integer32"
_BwaVLHWRetriesLowPriority_Object = MibScalar
bwaVLHWRetriesLowPriority = _BwaVLHWRetriesLowPriority_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 4, 4),
    _BwaVLHWRetriesLowPriority_Type()
)
bwaVLHWRetriesLowPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLHWRetriesLowPriority.setStatus("current")


class _BwaVLAUBurstDurationHighPriority_Type(Integer32):
    """Custom type bwaVLAUBurstDurationHighPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40),
    )


_BwaVLAUBurstDurationHighPriority_Type.__name__ = "Integer32"
_BwaVLAUBurstDurationHighPriority_Object = MibScalar
bwaVLAUBurstDurationHighPriority = _BwaVLAUBurstDurationHighPriority_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 4, 5),
    _BwaVLAUBurstDurationHighPriority_Type()
)
bwaVLAUBurstDurationHighPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLAUBurstDurationHighPriority.setStatus("current")


class _BwaVLAUBurstDurationLowPriority_Type(Integer32):
    """Custom type bwaVLAUBurstDurationLowPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40),
    )


_BwaVLAUBurstDurationLowPriority_Type.__name__ = "Integer32"
_BwaVLAUBurstDurationLowPriority_Object = MibScalar
bwaVLAUBurstDurationLowPriority = _BwaVLAUBurstDurationLowPriority_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 4, 6),
    _BwaVLAUBurstDurationLowPriority_Type()
)
bwaVLAUBurstDurationLowPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLAUBurstDurationLowPriority.setStatus("current")


class _BwaVLSUBurstDurationHighPriority_Type(Integer32):
    """Custom type bwaVLSUBurstDurationHighPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40),
    )


_BwaVLSUBurstDurationHighPriority_Type.__name__ = "Integer32"
_BwaVLSUBurstDurationHighPriority_Object = MibScalar
bwaVLSUBurstDurationHighPriority = _BwaVLSUBurstDurationHighPriority_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 4, 7),
    _BwaVLSUBurstDurationHighPriority_Type()
)
bwaVLSUBurstDurationHighPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLSUBurstDurationHighPriority.setStatus("current")


class _BwaVLSUBurstDurationLowPriority_Type(Integer32):
    """Custom type bwaVLSUBurstDurationLowPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40),
    )


_BwaVLSUBurstDurationLowPriority_Type.__name__ = "Integer32"
_BwaVLSUBurstDurationLowPriority_Object = MibScalar
bwaVLSUBurstDurationLowPriority = _BwaVLSUBurstDurationLowPriority_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 10, 4, 8),
    _BwaVLSUBurstDurationLowPriority_Type()
)
bwaVLSUBurstDurationLowPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLSUBurstDurationLowPriority.setStatus("current")
_BwaVLDrap_ObjectIdentity = ObjectIdentity
bwaVLDrap = _BwaVLDrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 11)
)


class _BwaVLDrapSupport_Type(Integer32):
    """Custom type bwaVLDrapSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BwaVLDrapSupport_Type.__name__ = "Integer32"
_BwaVLDrapSupport_Object = MibScalar
bwaVLDrapSupport = _BwaVLDrapSupport_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 11, 1),
    _BwaVLDrapSupport_Type()
)
bwaVLDrapSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLDrapSupport.setStatus("current")


class _BwaVLDrapUdpPort_Type(Integer32):
    """Custom type bwaVLDrapUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8000, 8200),
    )


_BwaVLDrapUdpPort_Type.__name__ = "Integer32"
_BwaVLDrapUdpPort_Object = MibScalar
bwaVLDrapUdpPort = _BwaVLDrapUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 11, 2),
    _BwaVLDrapUdpPort_Type()
)
bwaVLDrapUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLDrapUdpPort.setStatus("current")


class _BwaVLDrapMaxNumberOfVoiceCalls_Type(Integer32):
    """Custom type bwaVLDrapMaxNumberOfVoiceCalls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BwaVLDrapMaxNumberOfVoiceCalls_Type.__name__ = "Integer32"
_BwaVLDrapMaxNumberOfVoiceCalls_Object = MibScalar
bwaVLDrapMaxNumberOfVoiceCalls = _BwaVLDrapMaxNumberOfVoiceCalls_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 11, 3),
    _BwaVLDrapMaxNumberOfVoiceCalls_Type()
)
bwaVLDrapMaxNumberOfVoiceCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLDrapMaxNumberOfVoiceCalls.setStatus("current")


class _BwaVLDrapTTL_Type(Integer32):
    """Custom type bwaVLDrapTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BwaVLDrapTTL_Type.__name__ = "Integer32"
_BwaVLDrapTTL_Object = MibScalar
bwaVLDrapTTL = _BwaVLDrapTTL_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 11, 4),
    _BwaVLDrapTTL_Type()
)
bwaVLDrapTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLDrapTTL.setStatus("current")
_BwaVLDrapNoOfActiveVoiceCalls_Type = Integer32
_BwaVLDrapNoOfActiveVoiceCalls_Object = MibScalar
bwaVLDrapNoOfActiveVoiceCalls = _BwaVLDrapNoOfActiveVoiceCalls_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 11, 5),
    _BwaVLDrapNoOfActiveVoiceCalls_Type()
)
bwaVLDrapNoOfActiveVoiceCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLDrapNoOfActiveVoiceCalls.setStatus("current")


class _BwaVLLowPriorityTrafficMinimumPercent_Type(Integer32):
    """Custom type bwaVLLowPriorityTrafficMinimumPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BwaVLLowPriorityTrafficMinimumPercent_Type.__name__ = "Integer32"
_BwaVLLowPriorityTrafficMinimumPercent_Object = MibScalar
bwaVLLowPriorityTrafficMinimumPercent = _BwaVLLowPriorityTrafficMinimumPercent_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 12),
    _BwaVLLowPriorityTrafficMinimumPercent_Type()
)
bwaVLLowPriorityTrafficMinimumPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLLowPriorityTrafficMinimumPercent.setStatus("current")
_BwaVLSUPMirDownlink_Type = Integer32
_BwaVLSUPMirDownlink_Object = MibScalar
bwaVLSUPMirDownlink = _BwaVLSUPMirDownlink_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 13),
    _BwaVLSUPMirDownlink_Type()
)
bwaVLSUPMirDownlink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLSUPMirDownlink.setStatus("current")


class _BwaVLMIRThresholdPercent_Type(Integer32):
    """Custom type bwaVLMIRThresholdPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BwaVLMIRThresholdPercent_Type.__name__ = "Integer32"
_BwaVLMIRThresholdPercent_Object = MibScalar
bwaVLMIRThresholdPercent = _BwaVLMIRThresholdPercent_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 7, 14),
    _BwaVLMIRThresholdPercent_Type()
)
bwaVLMIRThresholdPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLMIRThresholdPercent.setStatus("current")
_BwaVLUserFilterParams_ObjectIdentity = ObjectIdentity
bwaVLUserFilterParams = _BwaVLUserFilterParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 8)
)


class _BwaVLUserFilterOption_Type(Integer32):
    """Custom type bwaVLUserFilterOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("ipOnly", 2),
          ("userDefinedAddrOnly", 3),
          ("pPPoEOnly", 4),
          ("na", 255))
    )


_BwaVLUserFilterOption_Type.__name__ = "Integer32"
_BwaVLUserFilterOption_Object = MibScalar
bwaVLUserFilterOption = _BwaVLUserFilterOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 8, 1),
    _BwaVLUserFilterOption_Type()
)
bwaVLUserFilterOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLUserFilterOption.setStatus("current")
_BwaVLIpFilterTable_Object = MibTable
bwaVLIpFilterTable = _BwaVLIpFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 8, 2)
)
if mibBuilder.loadTexts:
    bwaVLIpFilterTable.setStatus("current")
_BwaVLIpFilterEntry_Object = MibTableRow
bwaVLIpFilterEntry = _BwaVLIpFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 8, 2, 1)
)
bwaVLIpFilterEntry.setIndexNames(
    (0, "BWA-DOT11-WLAN-MIB", "bwaVLIpFilterIdx"),
)
if mibBuilder.loadTexts:
    bwaVLIpFilterEntry.setStatus("current")
_BwaVLIpID_Type = IpAddress
_BwaVLIpID_Object = MibTableColumn
bwaVLIpID = _BwaVLIpID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 8, 2, 1, 1),
    _BwaVLIpID_Type()
)
bwaVLIpID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLIpID.setStatus("current")
_BwaVLMaskID_Type = IpAddress
_BwaVLMaskID_Object = MibTableColumn
bwaVLMaskID = _BwaVLMaskID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 8, 2, 1, 2),
    _BwaVLMaskID_Type()
)
bwaVLMaskID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLMaskID.setStatus("current")
_BwaVLIpFilterRange_Type = Integer32
_BwaVLIpFilterRange_Object = MibTableColumn
bwaVLIpFilterRange = _BwaVLIpFilterRange_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 8, 2, 1, 3),
    _BwaVLIpFilterRange_Type()
)
bwaVLIpFilterRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLIpFilterRange.setStatus("current")


class _BwaVLIpFilterIdx_Type(Integer32):
    """Custom type bwaVLIpFilterIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_BwaVLIpFilterIdx_Type.__name__ = "Integer32"
_BwaVLIpFilterIdx_Object = MibTableColumn
bwaVLIpFilterIdx = _BwaVLIpFilterIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 8, 2, 1, 4),
    _BwaVLIpFilterIdx_Type()
)
bwaVLIpFilterIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLIpFilterIdx.setStatus("current")


class _BwaVLDeleteOneUserFilter_Type(Integer32):
    """Custom type bwaVLDeleteOneUserFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              255)
        )
    )
    namedValues = NamedValues(
        *(("deletefirstEntry", 1),
          ("deletesecondEntry", 2),
          ("deletethirdEntry", 3),
          ("deletefourthEntry", 4),
          ("deletefifthEntry", 5),
          ("deletesixthEntry", 6),
          ("deleteseventhEntry", 7),
          ("deleteeighthEntry", 8),
          ("cancelOperation", 9),
          ("na", 255))
    )


_BwaVLDeleteOneUserFilter_Type.__name__ = "Integer32"
_BwaVLDeleteOneUserFilter_Object = MibScalar
bwaVLDeleteOneUserFilter = _BwaVLDeleteOneUserFilter_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 8, 3),
    _BwaVLDeleteOneUserFilter_Type()
)
bwaVLDeleteOneUserFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLDeleteOneUserFilter.setStatus("current")


class _BwaVLDeleteAllUserFilters_Type(Integer32):
    """Custom type bwaVLDeleteAllUserFilters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("deleteAll", 1),
          ("cancelOperation", 2),
          ("na", 255))
    )


_BwaVLDeleteAllUserFilters_Type.__name__ = "Integer32"
_BwaVLDeleteAllUserFilters_Object = MibScalar
bwaVLDeleteAllUserFilters = _BwaVLDeleteAllUserFilters_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 8, 4),
    _BwaVLDeleteAllUserFilters_Type()
)
bwaVLDeleteAllUserFilters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLDeleteAllUserFilters.setStatus("current")


class _BwaVLDHCPUnicastOverrideFilter_Type(Integer32):
    """Custom type bwaVLDHCPUnicastOverrideFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BwaVLDHCPUnicastOverrideFilter_Type.__name__ = "Integer32"
_BwaVLDHCPUnicastOverrideFilter_Object = MibScalar
bwaVLDHCPUnicastOverrideFilter = _BwaVLDHCPUnicastOverrideFilter_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 8, 5),
    _BwaVLDHCPUnicastOverrideFilter_Type()
)
bwaVLDHCPUnicastOverrideFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLDHCPUnicastOverrideFilter.setStatus("current")
_BwaVLSecurityParameters_ObjectIdentity = ObjectIdentity
bwaVLSecurityParameters = _BwaVLSecurityParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 9)
)


class _BwaVLAuthenticationAlgorithm_Type(Integer32):
    """Custom type bwaVLAuthenticationAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("openSystem", 1),
          ("sharedKey", 2))
    )


_BwaVLAuthenticationAlgorithm_Type.__name__ = "Integer32"
_BwaVLAuthenticationAlgorithm_Object = MibScalar
bwaVLAuthenticationAlgorithm = _BwaVLAuthenticationAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 9, 1),
    _BwaVLAuthenticationAlgorithm_Type()
)
bwaVLAuthenticationAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLAuthenticationAlgorithm.setStatus("current")
_BwaVLSUDefaultKeyID_Type = Integer32
_BwaVLSUDefaultKeyID_Object = MibScalar
bwaVLSUDefaultKeyID = _BwaVLSUDefaultKeyID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 9, 2),
    _BwaVLSUDefaultKeyID_Type()
)
bwaVLSUDefaultKeyID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLSUDefaultKeyID.setStatus("current")


class _BwaVLDataEncryptionOption_Type(Integer32):
    """Custom type bwaVLDataEncryptionOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_BwaVLDataEncryptionOption_Type.__name__ = "Integer32"
_BwaVLDataEncryptionOption_Object = MibScalar
bwaVLDataEncryptionOption = _BwaVLDataEncryptionOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 9, 3),
    _BwaVLDataEncryptionOption_Type()
)
bwaVLDataEncryptionOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLDataEncryptionOption.setStatus("current")
_BwaVLAUDefaultMulticastKeyID_Type = Integer32
_BwaVLAUDefaultMulticastKeyID_Object = MibScalar
bwaVLAUDefaultMulticastKeyID = _BwaVLAUDefaultMulticastKeyID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 9, 4),
    _BwaVLAUDefaultMulticastKeyID_Type()
)
bwaVLAUDefaultMulticastKeyID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLAUDefaultMulticastKeyID.setStatus("current")


class _BwaVLSecurityMode_Type(Integer32):
    """Custom type bwaVLSecurityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("wep", 1),
          ("aesOCB", 2),
          ("fips197", 3))
    )


_BwaVLSecurityMode_Type.__name__ = "Integer32"
_BwaVLSecurityMode_Object = MibScalar
bwaVLSecurityMode = _BwaVLSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 9, 5),
    _BwaVLSecurityMode_Type()
)
bwaVLSecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLSecurityMode.setStatus("current")


class _BwaVLAuthenticationPromiscuousMode_Type(Integer32):
    """Custom type bwaVLAuthenticationPromiscuousMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_BwaVLAuthenticationPromiscuousMode_Type.__name__ = "Integer32"
_BwaVLAuthenticationPromiscuousMode_Object = MibScalar
bwaVLAuthenticationPromiscuousMode = _BwaVLAuthenticationPromiscuousMode_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 9, 6),
    _BwaVLAuthenticationPromiscuousMode_Type()
)
bwaVLAuthenticationPromiscuousMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLAuthenticationPromiscuousMode.setStatus("current")


class _BwaVLKey1_Type(DisplayString):
    """Custom type bwaVLKey1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_BwaVLKey1_Type.__name__ = "DisplayString"
_BwaVLKey1_Object = MibScalar
bwaVLKey1 = _BwaVLKey1_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 9, 7),
    _BwaVLKey1_Type()
)
bwaVLKey1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLKey1.setStatus("current")


class _BwaVLKey2_Type(DisplayString):
    """Custom type bwaVLKey2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_BwaVLKey2_Type.__name__ = "DisplayString"
_BwaVLKey2_Object = MibScalar
bwaVLKey2 = _BwaVLKey2_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 9, 8),
    _BwaVLKey2_Type()
)
bwaVLKey2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLKey2.setStatus("current")


class _BwaVLKey3_Type(DisplayString):
    """Custom type bwaVLKey3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_BwaVLKey3_Type.__name__ = "DisplayString"
_BwaVLKey3_Object = MibScalar
bwaVLKey3 = _BwaVLKey3_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 9, 9),
    _BwaVLKey3_Type()
)
bwaVLKey3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLKey3.setStatus("current")


class _BwaVLKey4_Type(DisplayString):
    """Custom type bwaVLKey4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_BwaVLKey4_Type.__name__ = "DisplayString"
_BwaVLKey4_Object = MibScalar
bwaVLKey4 = _BwaVLKey4_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 9, 10),
    _BwaVLKey4_Type()
)
bwaVLKey4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLKey4.setStatus("current")


class _BwaVLSecurityModeSupport_Type(Integer32):
    """Custom type bwaVLSecurityModeSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_BwaVLSecurityModeSupport_Type.__name__ = "Integer32"
_BwaVLSecurityModeSupport_Object = MibScalar
bwaVLSecurityModeSupport = _BwaVLSecurityModeSupport_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 9, 12),
    _BwaVLSecurityModeSupport_Type()
)
bwaVLSecurityModeSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLSecurityModeSupport.setStatus("current")
_BwaVLPerformanceParams_ObjectIdentity = ObjectIdentity
bwaVLPerformanceParams = _BwaVLPerformanceParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 10)
)
_BwaVLRTSThreshold_Type = Integer32
_BwaVLRTSThreshold_Object = MibScalar
bwaVLRTSThreshold = _BwaVLRTSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 10, 1),
    _BwaVLRTSThreshold_Type()
)
bwaVLRTSThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLRTSThreshold.setStatus("current")
_BwaVLMinContentionWindow_Type = Integer32
_BwaVLMinContentionWindow_Object = MibScalar
bwaVLMinContentionWindow = _BwaVLMinContentionWindow_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 10, 3),
    _BwaVLMinContentionWindow_Type()
)
bwaVLMinContentionWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLMinContentionWindow.setStatus("current")
_BwaVLMaxContentionWindow_Type = Integer32
_BwaVLMaxContentionWindow_Object = MibScalar
bwaVLMaxContentionWindow = _BwaVLMaxContentionWindow_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 10, 4),
    _BwaVLMaxContentionWindow_Type()
)
bwaVLMaxContentionWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLMaxContentionWindow.setStatus("current")


class _BwaVLMaximumModulationLevel_Type(Integer32):
    """Custom type bwaVLMaximumModulationLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("level1", 1),
          ("level2", 2),
          ("level3", 3),
          ("level4", 4),
          ("level5", 5),
          ("level6", 6),
          ("level7", 7),
          ("level8", 8))
    )


_BwaVLMaximumModulationLevel_Type.__name__ = "Integer32"
_BwaVLMaximumModulationLevel_Object = MibScalar
bwaVLMaximumModulationLevel = _BwaVLMaximumModulationLevel_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 10, 5),
    _BwaVLMaximumModulationLevel_Type()
)
bwaVLMaximumModulationLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLMaximumModulationLevel.setStatus("current")


class _BwaVLMulticastModulationLevel_Type(Integer32):
    """Custom type bwaVLMulticastModulationLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("level1", 1),
          ("level2", 2),
          ("level3", 3),
          ("level4", 4),
          ("level5", 5),
          ("level6", 6),
          ("level7", 7),
          ("level8", 8))
    )


_BwaVLMulticastModulationLevel_Type.__name__ = "Integer32"
_BwaVLMulticastModulationLevel_Object = MibScalar
bwaVLMulticastModulationLevel = _BwaVLMulticastModulationLevel_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 10, 6),
    _BwaVLMulticastModulationLevel_Type()
)
bwaVLMulticastModulationLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLMulticastModulationLevel.setStatus("current")
_BwaVLAvgSNRMemoryFactor_Type = DisplayString
_BwaVLAvgSNRMemoryFactor_Object = MibScalar
bwaVLAvgSNRMemoryFactor = _BwaVLAvgSNRMemoryFactor_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 10, 7),
    _BwaVLAvgSNRMemoryFactor_Type()
)
bwaVLAvgSNRMemoryFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLAvgSNRMemoryFactor.setStatus("current")
_BwaVLHardwareRetries_Type = Integer32
_BwaVLHardwareRetries_Object = MibScalar
bwaVLHardwareRetries = _BwaVLHardwareRetries_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 10, 8),
    _BwaVLHardwareRetries_Type()
)
bwaVLHardwareRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLHardwareRetries.setStatus("current")
_BwaVLAdaptiveModulationParams_ObjectIdentity = ObjectIdentity
bwaVLAdaptiveModulationParams = _BwaVLAdaptiveModulationParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 10, 9)
)


class _BwaVLAdaptiveModulationAlgorithmOption_Type(Integer32):
    """Custom type bwaVLAdaptiveModulationAlgorithmOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BwaVLAdaptiveModulationAlgorithmOption_Type.__name__ = "Integer32"
_BwaVLAdaptiveModulationAlgorithmOption_Object = MibScalar
bwaVLAdaptiveModulationAlgorithmOption = _BwaVLAdaptiveModulationAlgorithmOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 10, 9, 1),
    _BwaVLAdaptiveModulationAlgorithmOption_Type()
)
bwaVLAdaptiveModulationAlgorithmOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLAdaptiveModulationAlgorithmOption.setStatus("current")


class _BwaVLSoftwareRetrySupport_Type(Integer32):
    """Custom type bwaVLSoftwareRetrySupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BwaVLSoftwareRetrySupport_Type.__name__ = "Integer32"
_BwaVLSoftwareRetrySupport_Object = MibScalar
bwaVLSoftwareRetrySupport = _BwaVLSoftwareRetrySupport_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 10, 9, 2),
    _BwaVLSoftwareRetrySupport_Type()
)
bwaVLSoftwareRetrySupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLSoftwareRetrySupport.setStatus("current")


class _BwaVLNumOfSoftwareRetries_Type(Integer32):
    """Custom type bwaVLNumOfSoftwareRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            255
        )
    )
    namedValues = NamedValues(
        ("na", 255)
    )


_BwaVLNumOfSoftwareRetries_Type.__name__ = "Integer32"
_BwaVLNumOfSoftwareRetries_Object = MibScalar
bwaVLNumOfSoftwareRetries = _BwaVLNumOfSoftwareRetries_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 10, 9, 3),
    _BwaVLNumOfSoftwareRetries_Type()
)
bwaVLNumOfSoftwareRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLNumOfSoftwareRetries.setStatus("current")
_BwaVLMinIntervalBetweenAdaptiveModulationAlgorithmMessages_Type = Integer32
_BwaVLMinIntervalBetweenAdaptiveModulationAlgorithmMessages_Object = MibScalar
bwaVLMinIntervalBetweenAdaptiveModulationAlgorithmMessages = _BwaVLMinIntervalBetweenAdaptiveModulationAlgorithmMessages_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 10, 9, 4),
    _BwaVLMinIntervalBetweenAdaptiveModulationAlgorithmMessages_Type()
)
bwaVLMinIntervalBetweenAdaptiveModulationAlgorithmMessages.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLMinIntervalBetweenAdaptiveModulationAlgorithmMessages.setStatus("current")


class _BwaVLAdaptiveModulationDecisionThresholds_Type(Integer32):
    """Custom type bwaVLAdaptiveModulationDecisionThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("high", 2),
          ("na", 255))
    )


_BwaVLAdaptiveModulationDecisionThresholds_Type.__name__ = "Integer32"
_BwaVLAdaptiveModulationDecisionThresholds_Object = MibScalar
bwaVLAdaptiveModulationDecisionThresholds = _BwaVLAdaptiveModulationDecisionThresholds_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 10, 9, 5),
    _BwaVLAdaptiveModulationDecisionThresholds_Type()
)
bwaVLAdaptiveModulationDecisionThresholds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLAdaptiveModulationDecisionThresholds.setStatus("current")
_BwaVLBurstMode_ObjectIdentity = ObjectIdentity
bwaVLBurstMode = _BwaVLBurstMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 10, 10)
)


class _BwaVLBurstModeOption_Type(Integer32):
    """Custom type bwaVLBurstModeOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("blocked", 3),
          ("na", 255))
    )


_BwaVLBurstModeOption_Type.__name__ = "Integer32"
_BwaVLBurstModeOption_Object = MibScalar
bwaVLBurstModeOption = _BwaVLBurstModeOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 10, 10, 1),
    _BwaVLBurstModeOption_Type()
)
bwaVLBurstModeOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLBurstModeOption.setStatus("current")
_BwaVLBurstInterval_Type = Integer32
_BwaVLBurstInterval_Object = MibScalar
bwaVLBurstInterval = _BwaVLBurstInterval_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 10, 10, 2),
    _BwaVLBurstInterval_Type()
)
bwaVLBurstInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLBurstInterval.setStatus("current")
_BwaVLConcatenationParameters_ObjectIdentity = ObjectIdentity
bwaVLConcatenationParameters = _BwaVLConcatenationParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 10, 11)
)


class _BwaVLConcatenationOption_Type(Integer32):
    """Custom type bwaVLConcatenationOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BwaVLConcatenationOption_Type.__name__ = "Integer32"
_BwaVLConcatenationOption_Object = MibScalar
bwaVLConcatenationOption = _BwaVLConcatenationOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 10, 11, 1),
    _BwaVLConcatenationOption_Type()
)
bwaVLConcatenationOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLConcatenationOption.setStatus("current")


class _BwaVLConcatenationMaximumNumberOfFrames_Type(Integer32):
    """Custom type bwaVLConcatenationMaximumNumberOfFrames based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 8),
    )


_BwaVLConcatenationMaximumNumberOfFrames_Type.__name__ = "Integer32"
_BwaVLConcatenationMaximumNumberOfFrames_Object = MibScalar
bwaVLConcatenationMaximumNumberOfFrames = _BwaVLConcatenationMaximumNumberOfFrames_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 10, 11, 2),
    _BwaVLConcatenationMaximumNumberOfFrames_Type()
)
bwaVLConcatenationMaximumNumberOfFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLConcatenationMaximumNumberOfFrames.setStatus("current")
_BwaVLConcatenationMaxFrameSize_Type = Integer32
_BwaVLConcatenationMaxFrameSize_Object = MibScalar
bwaVLConcatenationMaxFrameSize = _BwaVLConcatenationMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 10, 11, 3),
    _BwaVLConcatenationMaxFrameSize_Type()
)
bwaVLConcatenationMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLConcatenationMaxFrameSize.setStatus("current")
_BwaVLSiteSurvey_ObjectIdentity = ObjectIdentity
bwaVLSiteSurvey = _BwaVLSiteSurvey_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11)
)
_BwaVLAverageReceiveSNR_Type = Integer32
_BwaVLAverageReceiveSNR_Object = MibScalar
bwaVLAverageReceiveSNR = _BwaVLAverageReceiveSNR_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 1),
    _BwaVLAverageReceiveSNR_Type()
)
bwaVLAverageReceiveSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLAverageReceiveSNR.setStatus("current")
_BwaVLTrafficStatistics_ObjectIdentity = ObjectIdentity
bwaVLTrafficStatistics = _BwaVLTrafficStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2)
)


class _BwaVLResetTrafficCounters_Type(Integer32):
    """Custom type bwaVLResetTrafficCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reset", 1),
          ("cancel", 2))
    )


_BwaVLResetTrafficCounters_Type.__name__ = "Integer32"
_BwaVLResetTrafficCounters_Object = MibScalar
bwaVLResetTrafficCounters = _BwaVLResetTrafficCounters_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 1),
    _BwaVLResetTrafficCounters_Type()
)
bwaVLResetTrafficCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLResetTrafficCounters.setStatus("current")
_BwaVLEthCounters_ObjectIdentity = ObjectIdentity
bwaVLEthCounters = _BwaVLEthCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 2)
)
_BwaVLTotalRxFramesViaEthernet_Type = Counter32
_BwaVLTotalRxFramesViaEthernet_Object = MibScalar
bwaVLTotalRxFramesViaEthernet = _BwaVLTotalRxFramesViaEthernet_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 2, 1),
    _BwaVLTotalRxFramesViaEthernet_Type()
)
bwaVLTotalRxFramesViaEthernet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLTotalRxFramesViaEthernet.setStatus("current")
_BwaVLTxWirelessToEthernet_Type = Counter32
_BwaVLTxWirelessToEthernet_Object = MibScalar
bwaVLTxWirelessToEthernet = _BwaVLTxWirelessToEthernet_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 2, 2),
    _BwaVLTxWirelessToEthernet_Type()
)
bwaVLTxWirelessToEthernet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLTxWirelessToEthernet.setStatus("current")
_BwaVLWirelessLinkCounters_ObjectIdentity = ObjectIdentity
bwaVLWirelessLinkCounters = _BwaVLWirelessLinkCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 3)
)
_BwaVLTxFramesToWireless_ObjectIdentity = ObjectIdentity
bwaVLTxFramesToWireless = _BwaVLTxFramesToWireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 3, 1)
)
_BwaVLAUBeaconsToWireless_Type = Counter32
_BwaVLAUBeaconsToWireless_Object = MibScalar
bwaVLAUBeaconsToWireless = _BwaVLAUBeaconsToWireless_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 3, 1, 1),
    _BwaVLAUBeaconsToWireless_Type()
)
bwaVLAUBeaconsToWireless.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLAUBeaconsToWireless.setStatus("current")
_BwaVLDataAndOtherMngFramesToWireless_Type = Counter32
_BwaVLDataAndOtherMngFramesToWireless_Object = MibScalar
bwaVLDataAndOtherMngFramesToWireless = _BwaVLDataAndOtherMngFramesToWireless_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 3, 1, 3),
    _BwaVLDataAndOtherMngFramesToWireless_Type()
)
bwaVLDataAndOtherMngFramesToWireless.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLDataAndOtherMngFramesToWireless.setStatus("current")
_BwaVLTotalTxFramesToWireless_Type = Counter32
_BwaVLTotalTxFramesToWireless_Object = MibScalar
bwaVLTotalTxFramesToWireless = _BwaVLTotalTxFramesToWireless_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 3, 1, 4),
    _BwaVLTotalTxFramesToWireless_Type()
)
bwaVLTotalTxFramesToWireless.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLTotalTxFramesToWireless.setStatus("current")
_BwaVLTotalTransmittedUnicasts_Type = Counter32
_BwaVLTotalTransmittedUnicasts_Object = MibScalar
bwaVLTotalTransmittedUnicasts = _BwaVLTotalTransmittedUnicasts_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 3, 1, 5),
    _BwaVLTotalTransmittedUnicasts_Type()
)
bwaVLTotalTransmittedUnicasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLTotalTransmittedUnicasts.setStatus("current")
_BwaVLTotalTransmittedConcatenatedFramesDouble_Type = Counter32
_BwaVLTotalTransmittedConcatenatedFramesDouble_Object = MibScalar
bwaVLTotalTransmittedConcatenatedFramesDouble = _BwaVLTotalTransmittedConcatenatedFramesDouble_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 3, 1, 6),
    _BwaVLTotalTransmittedConcatenatedFramesDouble_Type()
)
bwaVLTotalTransmittedConcatenatedFramesDouble.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLTotalTransmittedConcatenatedFramesDouble.setStatus("current")
_BwaVLTotalTransmittedConcatenatedFramesSingle_Type = Counter32
_BwaVLTotalTransmittedConcatenatedFramesSingle_Object = MibScalar
bwaVLTotalTransmittedConcatenatedFramesSingle = _BwaVLTotalTransmittedConcatenatedFramesSingle_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 3, 1, 7),
    _BwaVLTotalTransmittedConcatenatedFramesSingle_Type()
)
bwaVLTotalTransmittedConcatenatedFramesSingle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLTotalTransmittedConcatenatedFramesSingle.setStatus("current")
_BwaVLTotalTransmittedConcatenatedFramesMore_Type = Counter32
_BwaVLTotalTransmittedConcatenatedFramesMore_Object = MibScalar
bwaVLTotalTransmittedConcatenatedFramesMore = _BwaVLTotalTransmittedConcatenatedFramesMore_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 3, 1, 8),
    _BwaVLTotalTransmittedConcatenatedFramesMore_Type()
)
bwaVLTotalTransmittedConcatenatedFramesMore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLTotalTransmittedConcatenatedFramesMore.setStatus("current")
_BwaVLTotalRxFramesFromWireless_Type = Counter32
_BwaVLTotalRxFramesFromWireless_Object = MibScalar
bwaVLTotalRxFramesFromWireless = _BwaVLTotalRxFramesFromWireless_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 3, 2),
    _BwaVLTotalRxFramesFromWireless_Type()
)
bwaVLTotalRxFramesFromWireless.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLTotalRxFramesFromWireless.setStatus("current")
_BwaVLTotalRetransmittedFrames_Type = Counter32
_BwaVLTotalRetransmittedFrames_Object = MibScalar
bwaVLTotalRetransmittedFrames = _BwaVLTotalRetransmittedFrames_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 3, 3),
    _BwaVLTotalRetransmittedFrames_Type()
)
bwaVLTotalRetransmittedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLTotalRetransmittedFrames.setStatus("current")
_BwaVLFramesDropped_Type = Counter32
_BwaVLFramesDropped_Object = MibScalar
bwaVLFramesDropped = _BwaVLFramesDropped_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 3, 4),
    _BwaVLFramesDropped_Type()
)
bwaVLFramesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLFramesDropped.setStatus("current")
_BwaVLDataFramesSubmittedToBridge_ObjectIdentity = ObjectIdentity
bwaVLDataFramesSubmittedToBridge = _BwaVLDataFramesSubmittedToBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 3, 5)
)
_BwaVLFramesSubmittedViaHighQueue_Type = Counter32
_BwaVLFramesSubmittedViaHighQueue_Object = MibScalar
bwaVLFramesSubmittedViaHighQueue = _BwaVLFramesSubmittedViaHighQueue_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 3, 5, 1),
    _BwaVLFramesSubmittedViaHighQueue_Type()
)
bwaVLFramesSubmittedViaHighQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLFramesSubmittedViaHighQueue.setStatus("current")
_BwaVLFramesSubmittedViaMidQueue_Type = Counter32
_BwaVLFramesSubmittedViaMidQueue_Object = MibScalar
bwaVLFramesSubmittedViaMidQueue = _BwaVLFramesSubmittedViaMidQueue_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 3, 5, 2),
    _BwaVLFramesSubmittedViaMidQueue_Type()
)
bwaVLFramesSubmittedViaMidQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLFramesSubmittedViaMidQueue.setStatus("current")
_BwaVLFramesSubmittedViaLowQueue_Type = Counter32
_BwaVLFramesSubmittedViaLowQueue_Object = MibScalar
bwaVLFramesSubmittedViaLowQueue = _BwaVLFramesSubmittedViaLowQueue_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 3, 5, 3),
    _BwaVLFramesSubmittedViaLowQueue_Type()
)
bwaVLFramesSubmittedViaLowQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLFramesSubmittedViaLowQueue.setStatus("current")
_BwaVLTotalNoOfDataFramesSubmitted_Type = Counter32
_BwaVLTotalNoOfDataFramesSubmitted_Object = MibScalar
bwaVLTotalNoOfDataFramesSubmitted = _BwaVLTotalNoOfDataFramesSubmitted_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 3, 5, 4),
    _BwaVLTotalNoOfDataFramesSubmitted_Type()
)
bwaVLTotalNoOfDataFramesSubmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLTotalNoOfDataFramesSubmitted.setStatus("current")
_BwaVLTotalRecievedDataFrames_Type = Counter32
_BwaVLTotalRecievedDataFrames_Object = MibScalar
bwaVLTotalRecievedDataFrames = _BwaVLTotalRecievedDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 3, 6),
    _BwaVLTotalRecievedDataFrames_Type()
)
bwaVLTotalRecievedDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLTotalRecievedDataFrames.setStatus("current")
_BwaVLRecievedBadFrames_Type = Counter32
_BwaVLRecievedBadFrames_Object = MibScalar
bwaVLRecievedBadFrames = _BwaVLRecievedBadFrames_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 3, 7),
    _BwaVLRecievedBadFrames_Type()
)
bwaVLRecievedBadFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLRecievedBadFrames.setStatus("current")
_BwaVLNoOfDuplicateFramesDiscarded_Type = Counter32
_BwaVLNoOfDuplicateFramesDiscarded_Object = MibScalar
bwaVLNoOfDuplicateFramesDiscarded = _BwaVLNoOfDuplicateFramesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 3, 8),
    _BwaVLNoOfDuplicateFramesDiscarded_Type()
)
bwaVLNoOfDuplicateFramesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLNoOfDuplicateFramesDiscarded.setStatus("current")
_BwaVLNoOfInternallyDiscardedMirCir_Type = Counter32
_BwaVLNoOfInternallyDiscardedMirCir_Object = MibScalar
bwaVLNoOfInternallyDiscardedMirCir = _BwaVLNoOfInternallyDiscardedMirCir_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 3, 9),
    _BwaVLNoOfInternallyDiscardedMirCir_Type()
)
bwaVLNoOfInternallyDiscardedMirCir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLNoOfInternallyDiscardedMirCir.setStatus("current")
_BwaVLTotalRxConcatenatedFramesDouble_Type = Counter32
_BwaVLTotalRxConcatenatedFramesDouble_Object = MibScalar
bwaVLTotalRxConcatenatedFramesDouble = _BwaVLTotalRxConcatenatedFramesDouble_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 3, 10),
    _BwaVLTotalRxConcatenatedFramesDouble_Type()
)
bwaVLTotalRxConcatenatedFramesDouble.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLTotalRxConcatenatedFramesDouble.setStatus("current")
_BwaVLTotalRxConcatenatedFramesSingle_Type = Counter32
_BwaVLTotalRxConcatenatedFramesSingle_Object = MibScalar
bwaVLTotalRxConcatenatedFramesSingle = _BwaVLTotalRxConcatenatedFramesSingle_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 3, 11),
    _BwaVLTotalRxConcatenatedFramesSingle_Type()
)
bwaVLTotalRxConcatenatedFramesSingle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLTotalRxConcatenatedFramesSingle.setStatus("current")
_BwaVLTotalRxConcatenatedFramesMore_Type = Counter32
_BwaVLTotalRxConcatenatedFramesMore_Object = MibScalar
bwaVLTotalRxConcatenatedFramesMore = _BwaVLTotalRxConcatenatedFramesMore_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 3, 12),
    _BwaVLTotalRxConcatenatedFramesMore_Type()
)
bwaVLTotalRxConcatenatedFramesMore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLTotalRxConcatenatedFramesMore.setStatus("current")
_BwaVLWirelessLinkEvents_ObjectIdentity = ObjectIdentity
bwaVLWirelessLinkEvents = _BwaVLWirelessLinkEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 4)
)
_BwaVLTxEvents_ObjectIdentity = ObjectIdentity
bwaVLTxEvents = _BwaVLTxEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 4, 1)
)
_BwaVLDroppedFrameEvents_Type = Counter32
_BwaVLDroppedFrameEvents_Object = MibScalar
bwaVLDroppedFrameEvents = _BwaVLDroppedFrameEvents_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 4, 1, 1),
    _BwaVLDroppedFrameEvents_Type()
)
bwaVLDroppedFrameEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLDroppedFrameEvents.setStatus("current")
_BwaVLFramesDelayedDueToSwRetry_Type = Counter32
_BwaVLFramesDelayedDueToSwRetry_Object = MibScalar
bwaVLFramesDelayedDueToSwRetry = _BwaVLFramesDelayedDueToSwRetry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 4, 1, 2),
    _BwaVLFramesDelayedDueToSwRetry_Type()
)
bwaVLFramesDelayedDueToSwRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLFramesDelayedDueToSwRetry.setStatus("current")
_BwaVLUnderrunEvents_Type = Counter32
_BwaVLUnderrunEvents_Object = MibScalar
bwaVLUnderrunEvents = _BwaVLUnderrunEvents_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 4, 1, 3),
    _BwaVLUnderrunEvents_Type()
)
bwaVLUnderrunEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLUnderrunEvents.setStatus("current")
_BwaVLOthersTxEvents_Type = Counter32
_BwaVLOthersTxEvents_Object = MibScalar
bwaVLOthersTxEvents = _BwaVLOthersTxEvents_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 4, 1, 4),
    _BwaVLOthersTxEvents_Type()
)
bwaVLOthersTxEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLOthersTxEvents.setStatus("current")
_BwaVLTotalTxEvents_Type = Counter32
_BwaVLTotalTxEvents_Object = MibScalar
bwaVLTotalTxEvents = _BwaVLTotalTxEvents_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 4, 1, 5),
    _BwaVLTotalTxEvents_Type()
)
bwaVLTotalTxEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLTotalTxEvents.setStatus("current")
_BwaVLRxEvents_ObjectIdentity = ObjectIdentity
bwaVLRxEvents = _BwaVLRxEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 4, 2)
)
_BwaVLPhyErrors_Type = Counter32
_BwaVLPhyErrors_Object = MibScalar
bwaVLPhyErrors = _BwaVLPhyErrors_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 4, 2, 1),
    _BwaVLPhyErrors_Type()
)
bwaVLPhyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLPhyErrors.setStatus("current")
_BwaVLCRCErrors_Type = Counter32
_BwaVLCRCErrors_Object = MibScalar
bwaVLCRCErrors = _BwaVLCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 4, 2, 2),
    _BwaVLCRCErrors_Type()
)
bwaVLCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLCRCErrors.setStatus("current")
_BwaVLOverrunEvents_Type = Counter32
_BwaVLOverrunEvents_Object = MibScalar
bwaVLOverrunEvents = _BwaVLOverrunEvents_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 4, 2, 3),
    _BwaVLOverrunEvents_Type()
)
bwaVLOverrunEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLOverrunEvents.setStatus("current")
_BwaVLRxDecryptEvents_Type = Counter32
_BwaVLRxDecryptEvents_Object = MibScalar
bwaVLRxDecryptEvents = _BwaVLRxDecryptEvents_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 4, 2, 4),
    _BwaVLRxDecryptEvents_Type()
)
bwaVLRxDecryptEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLRxDecryptEvents.setStatus("current")
_BwaVLTotalRxEvents_Type = Counter32
_BwaVLTotalRxEvents_Object = MibScalar
bwaVLTotalRxEvents = _BwaVLTotalRxEvents_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 4, 2, 5),
    _BwaVLTotalRxEvents_Type()
)
bwaVLTotalRxEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLTotalRxEvents.setStatus("current")
_BwaVLPerModulationLevelCounters_ObjectIdentity = ObjectIdentity
bwaVLPerModulationLevelCounters = _BwaVLPerModulationLevelCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 5)
)


class _BwaVLResetPerModulationLevelCounters_Type(Integer32):
    """Custom type bwaVLResetPerModulationLevelCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("resetCounters", 1),
          ("cancel", 2))
    )


_BwaVLResetPerModulationLevelCounters_Type.__name__ = "Integer32"
_BwaVLResetPerModulationLevelCounters_Object = MibScalar
bwaVLResetPerModulationLevelCounters = _BwaVLResetPerModulationLevelCounters_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 5, 1),
    _BwaVLResetPerModulationLevelCounters_Type()
)
bwaVLResetPerModulationLevelCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLResetPerModulationLevelCounters.setStatus("current")
_BwaVLSUPerModulationLevelCountersTable_Object = MibTable
bwaVLSUPerModulationLevelCountersTable = _BwaVLSUPerModulationLevelCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 5, 2)
)
if mibBuilder.loadTexts:
    bwaVLSUPerModulationLevelCountersTable.setStatus("current")
_BwaVLSUPerModulationLevelCountersEntry_Object = MibTableRow
bwaVLSUPerModulationLevelCountersEntry = _BwaVLSUPerModulationLevelCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 5, 2, 1)
)
bwaVLSUPerModulationLevelCountersEntry.setIndexNames(
    (0, "BWA-DOT11-WLAN-MIB", "bwaVLSUPerModulationLevelCountersTableIdx"),
)
if mibBuilder.loadTexts:
    bwaVLSUPerModulationLevelCountersEntry.setStatus("current")


class _BwaVLSUPerModulationLevelCountersTableIdx_Type(Integer32):
    """Custom type bwaVLSUPerModulationLevelCountersTableIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_BwaVLSUPerModulationLevelCountersTableIdx_Type.__name__ = "Integer32"
_BwaVLSUPerModulationLevelCountersTableIdx_Object = MibTableColumn
bwaVLSUPerModulationLevelCountersTableIdx = _BwaVLSUPerModulationLevelCountersTableIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 5, 2, 1, 1),
    _BwaVLSUPerModulationLevelCountersTableIdx_Type()
)
bwaVLSUPerModulationLevelCountersTableIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLSUPerModulationLevelCountersTableIdx.setStatus("current")


class _BwaVLSUPerModulationLevelCountersApplicableModLevel_Type(Integer32):
    """Custom type bwaVLSUPerModulationLevelCountersApplicableModLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("modLevel-1", 1),
          ("modLevel-2", 2),
          ("modLevel-3", 3),
          ("modLevel-4", 4),
          ("modLevel-5", 5),
          ("modLevel-6", 6),
          ("modLevel-7", 7),
          ("modLevel-8", 8))
    )


_BwaVLSUPerModulationLevelCountersApplicableModLevel_Type.__name__ = "Integer32"
_BwaVLSUPerModulationLevelCountersApplicableModLevel_Object = MibTableColumn
bwaVLSUPerModulationLevelCountersApplicableModLevel = _BwaVLSUPerModulationLevelCountersApplicableModLevel_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 5, 2, 1, 2),
    _BwaVLSUPerModulationLevelCountersApplicableModLevel_Type()
)
bwaVLSUPerModulationLevelCountersApplicableModLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLSUPerModulationLevelCountersApplicableModLevel.setStatus("current")
_BwaVLSUPerModulationLevelCountersTxSuccess_Type = Counter32
_BwaVLSUPerModulationLevelCountersTxSuccess_Object = MibTableColumn
bwaVLSUPerModulationLevelCountersTxSuccess = _BwaVLSUPerModulationLevelCountersTxSuccess_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 5, 2, 1, 3),
    _BwaVLSUPerModulationLevelCountersTxSuccess_Type()
)
bwaVLSUPerModulationLevelCountersTxSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLSUPerModulationLevelCountersTxSuccess.setStatus("current")
_BwaVLSUPerModulationLevelCountersTxFailed_Type = Counter32
_BwaVLSUPerModulationLevelCountersTxFailed_Object = MibTableColumn
bwaVLSUPerModulationLevelCountersTxFailed = _BwaVLSUPerModulationLevelCountersTxFailed_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 5, 2, 1, 4),
    _BwaVLSUPerModulationLevelCountersTxFailed_Type()
)
bwaVLSUPerModulationLevelCountersTxFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLSUPerModulationLevelCountersTxFailed.setStatus("current")
_BwaVLAverageModulationLevel_Type = Integer32
_BwaVLAverageModulationLevel_Object = MibScalar
bwaVLAverageModulationLevel = _BwaVLAverageModulationLevel_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 2, 5, 3),
    _BwaVLAverageModulationLevel_Type()
)
bwaVLAverageModulationLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLAverageModulationLevel.setStatus("current")
_BwaVLMacAddressDatabase_ObjectIdentity = ObjectIdentity
bwaVLMacAddressDatabase = _BwaVLMacAddressDatabase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5)
)
_BwaVLAUMacAddressDatabase_ObjectIdentity = ObjectIdentity
bwaVLAUMacAddressDatabase = _BwaVLAUMacAddressDatabase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1)
)


class _BwaVLAUAdbResetAllModulationLevelCounters_Type(Integer32):
    """Custom type bwaVLAUAdbResetAllModulationLevelCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reset", 1),
          ("cancel", 2))
    )


_BwaVLAUAdbResetAllModulationLevelCounters_Type.__name__ = "Integer32"
_BwaVLAUAdbResetAllModulationLevelCounters_Object = MibScalar
bwaVLAUAdbResetAllModulationLevelCounters = _BwaVLAUAdbResetAllModulationLevelCounters_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 1),
    _BwaVLAUAdbResetAllModulationLevelCounters_Type()
)
bwaVLAUAdbResetAllModulationLevelCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLAUAdbResetAllModulationLevelCounters.setStatus("current")
_BwaVLAUAdbTable_Object = MibTable
bwaVLAUAdbTable = _BwaVLAUAdbTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2)
)
if mibBuilder.loadTexts:
    bwaVLAUAdbTable.setStatus("current")
_BwaVLAUAdbEntry_Object = MibTableRow
bwaVLAUAdbEntry = _BwaVLAUAdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1)
)
bwaVLAUAdbEntry.setIndexNames(
    (0, "BWA-DOT11-WLAN-MIB", "bwaVLAdbIndex"),
)
if mibBuilder.loadTexts:
    bwaVLAUAdbEntry.setStatus("current")


class _BwaVLAdbIndex_Type(Integer32):
    """Custom type bwaVLAdbIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_BwaVLAdbIndex_Type.__name__ = "Integer32"
_BwaVLAdbIndex_Object = MibTableColumn
bwaVLAdbIndex = _BwaVLAdbIndex_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 1),
    _BwaVLAdbIndex_Type()
)
bwaVLAdbIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLAdbIndex.setStatus("current")
_BwaVLAdbMacAddress_Type = MacAddress
_BwaVLAdbMacAddress_Object = MibTableColumn
bwaVLAdbMacAddress = _BwaVLAdbMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 2),
    _BwaVLAdbMacAddress_Type()
)
bwaVLAdbMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLAdbMacAddress.setStatus("current")


class _BwaVLAdbStatus_Type(Integer32):
    """Custom type bwaVLAdbStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("associated", 1),
          ("authenticated", 2),
          ("notAuthenticated", 3))
    )


_BwaVLAdbStatus_Type.__name__ = "Integer32"
_BwaVLAdbStatus_Object = MibTableColumn
bwaVLAdbStatus = _BwaVLAdbStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 3),
    _BwaVLAdbStatus_Type()
)
bwaVLAdbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLAdbStatus.setStatus("current")
_BwaVLAdbSwVersion_Type = DisplayString
_BwaVLAdbSwVersion_Object = MibTableColumn
bwaVLAdbSwVersion = _BwaVLAdbSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 4),
    _BwaVLAdbSwVersion_Type()
)
bwaVLAdbSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLAdbSwVersion.setStatus("current")
_BwaVLAdbSNR_Type = Integer32
_BwaVLAdbSNR_Object = MibTableColumn
bwaVLAdbSNR = _BwaVLAdbSNR_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 5),
    _BwaVLAdbSNR_Type()
)
bwaVLAdbSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLAdbSNR.setStatus("current")


class _BwaVLAdbMaxModulationLevel_Type(Integer32):
    """Custom type bwaVLAdbMaxModulationLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("modLevel-1", 1),
          ("modLevel-2", 2),
          ("modLevel-3", 3),
          ("modLevel-4", 4),
          ("modLevel-5", 5),
          ("modLevel-6", 6),
          ("modLevel-7", 7),
          ("modLevel-8", 8))
    )


_BwaVLAdbMaxModulationLevel_Type.__name__ = "Integer32"
_BwaVLAdbMaxModulationLevel_Object = MibTableColumn
bwaVLAdbMaxModulationLevel = _BwaVLAdbMaxModulationLevel_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 6),
    _BwaVLAdbMaxModulationLevel_Type()
)
bwaVLAdbMaxModulationLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLAdbMaxModulationLevel.setStatus("current")
_BwaVLAdbTxFramesTotal_Type = Counter32
_BwaVLAdbTxFramesTotal_Object = MibTableColumn
bwaVLAdbTxFramesTotal = _BwaVLAdbTxFramesTotal_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 7),
    _BwaVLAdbTxFramesTotal_Type()
)
bwaVLAdbTxFramesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLAdbTxFramesTotal.setStatus("current")
_BwaVLAdbDroppedFramesTotal_Type = Counter32
_BwaVLAdbDroppedFramesTotal_Object = MibTableColumn
bwaVLAdbDroppedFramesTotal = _BwaVLAdbDroppedFramesTotal_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 8),
    _BwaVLAdbDroppedFramesTotal_Type()
)
bwaVLAdbDroppedFramesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLAdbDroppedFramesTotal.setStatus("current")
_BwaVLAdbTxSuccessModLevel1_Type = Counter32
_BwaVLAdbTxSuccessModLevel1_Object = MibTableColumn
bwaVLAdbTxSuccessModLevel1 = _BwaVLAdbTxSuccessModLevel1_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 9),
    _BwaVLAdbTxSuccessModLevel1_Type()
)
bwaVLAdbTxSuccessModLevel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLAdbTxSuccessModLevel1.setStatus("current")
_BwaVLAdbTxSuccessModLevel2_Type = Counter32
_BwaVLAdbTxSuccessModLevel2_Object = MibTableColumn
bwaVLAdbTxSuccessModLevel2 = _BwaVLAdbTxSuccessModLevel2_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 10),
    _BwaVLAdbTxSuccessModLevel2_Type()
)
bwaVLAdbTxSuccessModLevel2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLAdbTxSuccessModLevel2.setStatus("current")
_BwaVLAdbTxSuccessModLevel3_Type = Counter32
_BwaVLAdbTxSuccessModLevel3_Object = MibTableColumn
bwaVLAdbTxSuccessModLevel3 = _BwaVLAdbTxSuccessModLevel3_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 11),
    _BwaVLAdbTxSuccessModLevel3_Type()
)
bwaVLAdbTxSuccessModLevel3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLAdbTxSuccessModLevel3.setStatus("current")
_BwaVLAdbTxSuccessModLevel4_Type = Counter32
_BwaVLAdbTxSuccessModLevel4_Object = MibTableColumn
bwaVLAdbTxSuccessModLevel4 = _BwaVLAdbTxSuccessModLevel4_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 12),
    _BwaVLAdbTxSuccessModLevel4_Type()
)
bwaVLAdbTxSuccessModLevel4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLAdbTxSuccessModLevel4.setStatus("current")
_BwaVLAdbTxSuccessModLevel5_Type = Counter32
_BwaVLAdbTxSuccessModLevel5_Object = MibTableColumn
bwaVLAdbTxSuccessModLevel5 = _BwaVLAdbTxSuccessModLevel5_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 13),
    _BwaVLAdbTxSuccessModLevel5_Type()
)
bwaVLAdbTxSuccessModLevel5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLAdbTxSuccessModLevel5.setStatus("current")
_BwaVLAdbTxSuccessModLevel6_Type = Counter32
_BwaVLAdbTxSuccessModLevel6_Object = MibTableColumn
bwaVLAdbTxSuccessModLevel6 = _BwaVLAdbTxSuccessModLevel6_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 14),
    _BwaVLAdbTxSuccessModLevel6_Type()
)
bwaVLAdbTxSuccessModLevel6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLAdbTxSuccessModLevel6.setStatus("current")
_BwaVLAdbTxSuccessModLevel7_Type = Counter32
_BwaVLAdbTxSuccessModLevel7_Object = MibTableColumn
bwaVLAdbTxSuccessModLevel7 = _BwaVLAdbTxSuccessModLevel7_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 15),
    _BwaVLAdbTxSuccessModLevel7_Type()
)
bwaVLAdbTxSuccessModLevel7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLAdbTxSuccessModLevel7.setStatus("current")
_BwaVLAdbTxSuccessModLevel8_Type = Counter32
_BwaVLAdbTxSuccessModLevel8_Object = MibTableColumn
bwaVLAdbTxSuccessModLevel8 = _BwaVLAdbTxSuccessModLevel8_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 16),
    _BwaVLAdbTxSuccessModLevel8_Type()
)
bwaVLAdbTxSuccessModLevel8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLAdbTxSuccessModLevel8.setStatus("current")
_BwaVLAdbTxFailedModLevel1_Type = Counter32
_BwaVLAdbTxFailedModLevel1_Object = MibTableColumn
bwaVLAdbTxFailedModLevel1 = _BwaVLAdbTxFailedModLevel1_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 17),
    _BwaVLAdbTxFailedModLevel1_Type()
)
bwaVLAdbTxFailedModLevel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLAdbTxFailedModLevel1.setStatus("current")
_BwaVLAdbTxFailedModLevel2_Type = Counter32
_BwaVLAdbTxFailedModLevel2_Object = MibTableColumn
bwaVLAdbTxFailedModLevel2 = _BwaVLAdbTxFailedModLevel2_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 18),
    _BwaVLAdbTxFailedModLevel2_Type()
)
bwaVLAdbTxFailedModLevel2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLAdbTxFailedModLevel2.setStatus("current")
_BwaVLAdbTxFailedModLevel3_Type = Counter32
_BwaVLAdbTxFailedModLevel3_Object = MibTableColumn
bwaVLAdbTxFailedModLevel3 = _BwaVLAdbTxFailedModLevel3_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 19),
    _BwaVLAdbTxFailedModLevel3_Type()
)
bwaVLAdbTxFailedModLevel3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLAdbTxFailedModLevel3.setStatus("current")
_BwaVLAdbTxFailedModLevel4_Type = Counter32
_BwaVLAdbTxFailedModLevel4_Object = MibTableColumn
bwaVLAdbTxFailedModLevel4 = _BwaVLAdbTxFailedModLevel4_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 20),
    _BwaVLAdbTxFailedModLevel4_Type()
)
bwaVLAdbTxFailedModLevel4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLAdbTxFailedModLevel4.setStatus("current")
_BwaVLAdbTxFailedModLevel5_Type = Counter32
_BwaVLAdbTxFailedModLevel5_Object = MibTableColumn
bwaVLAdbTxFailedModLevel5 = _BwaVLAdbTxFailedModLevel5_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 21),
    _BwaVLAdbTxFailedModLevel5_Type()
)
bwaVLAdbTxFailedModLevel5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLAdbTxFailedModLevel5.setStatus("current")
_BwaVLAdbTxFailedModLevel6_Type = Counter32
_BwaVLAdbTxFailedModLevel6_Object = MibTableColumn
bwaVLAdbTxFailedModLevel6 = _BwaVLAdbTxFailedModLevel6_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 22),
    _BwaVLAdbTxFailedModLevel6_Type()
)
bwaVLAdbTxFailedModLevel6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLAdbTxFailedModLevel6.setStatus("current")
_BwaVLAdbTxFailedModLevel7_Type = Counter32
_BwaVLAdbTxFailedModLevel7_Object = MibTableColumn
bwaVLAdbTxFailedModLevel7 = _BwaVLAdbTxFailedModLevel7_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 23),
    _BwaVLAdbTxFailedModLevel7_Type()
)
bwaVLAdbTxFailedModLevel7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLAdbTxFailedModLevel7.setStatus("current")
_BwaVLAdbTxFailedModLevel8_Type = Counter32
_BwaVLAdbTxFailedModLevel8_Object = MibTableColumn
bwaVLAdbTxFailedModLevel8 = _BwaVLAdbTxFailedModLevel8_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 24),
    _BwaVLAdbTxFailedModLevel8_Type()
)
bwaVLAdbTxFailedModLevel8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLAdbTxFailedModLevel8.setStatus("current")
_BwaVLAdbCirTx_Type = Integer32
_BwaVLAdbCirTx_Object = MibTableColumn
bwaVLAdbCirTx = _BwaVLAdbCirTx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 25),
    _BwaVLAdbCirTx_Type()
)
bwaVLAdbCirTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLAdbCirTx.setStatus("current")
_BwaVLAdbMirTx_Type = Integer32
_BwaVLAdbMirTx_Object = MibTableColumn
bwaVLAdbMirTx = _BwaVLAdbMirTx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 26),
    _BwaVLAdbMirTx_Type()
)
bwaVLAdbMirTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLAdbMirTx.setStatus("current")
_BwaVLAdbCirRx_Type = Integer32
_BwaVLAdbCirRx_Object = MibTableColumn
bwaVLAdbCirRx = _BwaVLAdbCirRx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 27),
    _BwaVLAdbCirRx_Type()
)
bwaVLAdbCirRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLAdbCirRx.setStatus("current")
_BwaVLAdbMirRx_Type = Integer32
_BwaVLAdbMirRx_Object = MibTableColumn
bwaVLAdbMirRx = _BwaVLAdbMirRx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 28),
    _BwaVLAdbMirRx_Type()
)
bwaVLAdbMirRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLAdbMirRx.setStatus("current")
_BwaVLAdbCirMaxDelay_Type = Integer32
_BwaVLAdbCirMaxDelay_Object = MibTableColumn
bwaVLAdbCirMaxDelay = _BwaVLAdbCirMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 29),
    _BwaVLAdbCirMaxDelay_Type()
)
bwaVLAdbCirMaxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLAdbCirMaxDelay.setStatus("current")


class _BwaVLAdbDistance_Type(Integer32):
    """Custom type bwaVLAdbDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("below-2-Km", 1)
    )


_BwaVLAdbDistance_Type.__name__ = "Integer32"
_BwaVLAdbDistance_Object = MibTableColumn
bwaVLAdbDistance = _BwaVLAdbDistance_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 30),
    _BwaVLAdbDistance_Type()
)
bwaVLAdbDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLAdbDistance.setStatus("current")


class _BwaVLAdbHwRevision_Type(Integer32):
    """Custom type bwaVLAdbHwRevision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("hwRevisionA", 1),
          ("hwRevisionB", 2),
          ("hwRevisionC", 3),
          ("hwRevisionD", 4),
          ("hwRevisionE", 5),
          ("na", 255))
    )


_BwaVLAdbHwRevision_Type.__name__ = "Integer32"
_BwaVLAdbHwRevision_Object = MibTableColumn
bwaVLAdbHwRevision = _BwaVLAdbHwRevision_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 31),
    _BwaVLAdbHwRevision_Type()
)
bwaVLAdbHwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLAdbHwRevision.setStatus("current")
_BwaVLAdbCpldVer_Type = DisplayString
_BwaVLAdbCpldVer_Object = MibTableColumn
bwaVLAdbCpldVer = _BwaVLAdbCpldVer_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 32),
    _BwaVLAdbCpldVer_Type()
)
bwaVLAdbCpldVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLAdbCpldVer.setStatus("current")
_BwaVLAdbCountryCode_Type = Integer32
_BwaVLAdbCountryCode_Object = MibTableColumn
bwaVLAdbCountryCode = _BwaVLAdbCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 33),
    _BwaVLAdbCountryCode_Type()
)
bwaVLAdbCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLAdbCountryCode.setStatus("current")
_BwaVLAdbBootVer_Type = DisplayString
_BwaVLAdbBootVer_Object = MibTableColumn
bwaVLAdbBootVer = _BwaVLAdbBootVer_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 34),
    _BwaVLAdbBootVer_Type()
)
bwaVLAdbBootVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLAdbBootVer.setStatus("current")


class _BwaVLAdbAtpcOption_Type(Integer32):
    """Custom type bwaVLAdbAtpcOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BwaVLAdbAtpcOption_Type.__name__ = "Integer32"
_BwaVLAdbAtpcOption_Object = MibTableColumn
bwaVLAdbAtpcOption = _BwaVLAdbAtpcOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 35),
    _BwaVLAdbAtpcOption_Type()
)
bwaVLAdbAtpcOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLAdbAtpcOption.setStatus("current")


class _BwaVLAdbAdapModOption_Type(Integer32):
    """Custom type bwaVLAdbAdapModOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BwaVLAdbAdapModOption_Type.__name__ = "Integer32"
_BwaVLAdbAdapModOption_Object = MibTableColumn
bwaVLAdbAdapModOption = _BwaVLAdbAdapModOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 36),
    _BwaVLAdbAdapModOption_Type()
)
bwaVLAdbAdapModOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLAdbAdapModOption.setStatus("current")


class _BwaVLAdbBurstModeOption_Type(Integer32):
    """Custom type bwaVLAdbBurstModeOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BwaVLAdbBurstModeOption_Type.__name__ = "Integer32"
_BwaVLAdbBurstModeOption_Object = MibTableColumn
bwaVLAdbBurstModeOption = _BwaVLAdbBurstModeOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 37),
    _BwaVLAdbBurstModeOption_Type()
)
bwaVLAdbBurstModeOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLAdbBurstModeOption.setStatus("current")


class _BwaVLAdbConcatenationOption_Type(Integer32):
    """Custom type bwaVLAdbConcatenationOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BwaVLAdbConcatenationOption_Type.__name__ = "Integer32"
_BwaVLAdbConcatenationOption_Object = MibTableColumn
bwaVLAdbConcatenationOption = _BwaVLAdbConcatenationOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 39),
    _BwaVLAdbConcatenationOption_Type()
)
bwaVLAdbConcatenationOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLAdbConcatenationOption.setStatus("current")


class _BwaVLAdbSecurityMode_Type(Integer32):
    """Custom type bwaVLAdbSecurityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("wep", 1),
          ("aes", 2),
          ("fips197", 3),
          ("na", 255))
    )


_BwaVLAdbSecurityMode_Type.__name__ = "Integer32"
_BwaVLAdbSecurityMode_Object = MibTableColumn
bwaVLAdbSecurityMode = _BwaVLAdbSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 41),
    _BwaVLAdbSecurityMode_Type()
)
bwaVLAdbSecurityMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLAdbSecurityMode.setStatus("current")


class _BwaVLAdbAuthOption_Type(Integer32):
    """Custom type bwaVLAdbAuthOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("openSystem", 1),
          ("sharedKey", 2),
          ("na", 255))
    )


_BwaVLAdbAuthOption_Type.__name__ = "Integer32"
_BwaVLAdbAuthOption_Object = MibTableColumn
bwaVLAdbAuthOption = _BwaVLAdbAuthOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 42),
    _BwaVLAdbAuthOption_Type()
)
bwaVLAdbAuthOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLAdbAuthOption.setStatus("current")


class _BwaVLAdbDataEncyptOption_Type(Integer32):
    """Custom type bwaVLAdbDataEncyptOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("na", 255))
    )


_BwaVLAdbDataEncyptOption_Type.__name__ = "Integer32"
_BwaVLAdbDataEncyptOption_Object = MibTableColumn
bwaVLAdbDataEncyptOption = _BwaVLAdbDataEncyptOption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 43),
    _BwaVLAdbDataEncyptOption_Type()
)
bwaVLAdbDataEncyptOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLAdbDataEncyptOption.setStatus("current")
_BwaVLAdbAge_Type = Integer32
_BwaVLAdbAge_Object = MibTableColumn
bwaVLAdbAge = _BwaVLAdbAge_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 44),
    _BwaVLAdbAge_Type()
)
bwaVLAdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLAdbAge.setStatus("current")
_BwaVLAdbUnitName_Type = DisplayString
_BwaVLAdbUnitName_Object = MibTableColumn
bwaVLAdbUnitName = _BwaVLAdbUnitName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 5, 1, 2, 1, 45),
    _BwaVLAdbUnitName_Type()
)
bwaVLAdbUnitName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLAdbUnitName.setStatus("current")
_BwaVLUpLinkQualityIndicator_ObjectIdentity = ObjectIdentity
bwaVLUpLinkQualityIndicator = _BwaVLUpLinkQualityIndicator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 6)
)


class _BwaVLMeasureUpLinkQualityIndicator_Type(Integer32):
    """Custom type bwaVLMeasureUpLinkQualityIndicator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("cancel", 2))
    )


_BwaVLMeasureUpLinkQualityIndicator_Type.__name__ = "Integer32"
_BwaVLMeasureUpLinkQualityIndicator_Object = MibScalar
bwaVLMeasureUpLinkQualityIndicator = _BwaVLMeasureUpLinkQualityIndicator_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 6, 1),
    _BwaVLMeasureUpLinkQualityIndicator_Type()
)
bwaVLMeasureUpLinkQualityIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwaVLMeasureUpLinkQualityIndicator.setStatus("current")
_BwaVLReadUpLinkQualityIndicator_Type = Integer32
_BwaVLReadUpLinkQualityIndicator_Object = MibScalar
bwaVLReadUpLinkQualityIndicator = _BwaVLReadUpLinkQualityIndicator_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 6, 2),
    _BwaVLReadUpLinkQualityIndicator_Type()
)
bwaVLReadUpLinkQualityIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLReadUpLinkQualityIndicator.setStatus("current")


class _BwaVLUpLinkQualityIndicatorStatus_Type(Integer32):
    """Custom type bwaVLUpLinkQualityIndicatorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fullTest", 1),
          ("limitedTest", 2))
    )


_BwaVLUpLinkQualityIndicatorStatus_Type.__name__ = "Integer32"
_BwaVLUpLinkQualityIndicatorStatus_Object = MibScalar
bwaVLUpLinkQualityIndicatorStatus = _BwaVLUpLinkQualityIndicatorStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 6, 3),
    _BwaVLUpLinkQualityIndicatorStatus_Type()
)
bwaVLUpLinkQualityIndicatorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLUpLinkQualityIndicatorStatus.setStatus("current")
_BwaVLMacPinpoint_ObjectIdentity = ObjectIdentity
bwaVLMacPinpoint = _BwaVLMacPinpoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 7)
)
_BwaVLMacPinpointTable_Object = MibTable
bwaVLMacPinpointTable = _BwaVLMacPinpointTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 7, 1)
)
if mibBuilder.loadTexts:
    bwaVLMacPinpointTable.setStatus("current")
_BwaVLMacPinpointEntry_Object = MibTableRow
bwaVLMacPinpointEntry = _BwaVLMacPinpointEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 7, 1, 1)
)
bwaVLMacPinpointEntry.setIndexNames(
    (0, "BWA-DOT11-WLAN-MIB", "mptEthernetStationMACAddress"),
)
if mibBuilder.loadTexts:
    bwaVLMacPinpointEntry.setStatus("current")
_MptEthernetStationMACAddress_Type = MacAddress
_MptEthernetStationMACAddress_Object = MibTableColumn
mptEthernetStationMACAddress = _MptEthernetStationMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 7, 1, 1, 1),
    _MptEthernetStationMACAddress_Type()
)
mptEthernetStationMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mptEthernetStationMACAddress.setStatus("current")
_MptUnitMACAddress_Type = MacAddress
_MptUnitMACAddress_Object = MibTableColumn
mptUnitMACAddress = _MptUnitMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 7, 1, 1, 2),
    _MptUnitMACAddress_Type()
)
mptUnitMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mptUnitMACAddress.setStatus("current")
_BwaVLDrapGatewaysTable_Object = MibTable
bwaVLDrapGatewaysTable = _BwaVLDrapGatewaysTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 8)
)
if mibBuilder.loadTexts:
    bwaVLDrapGatewaysTable.setStatus("current")
_BwaVLDrapGatewayEntry_Object = MibTableRow
bwaVLDrapGatewayEntry = _BwaVLDrapGatewayEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 8, 1)
)
bwaVLDrapGatewayEntry.setIndexNames(
    (0, "BWA-DOT11-WLAN-MIB", "bwaVLDrapGatewayIndex"),
)
if mibBuilder.loadTexts:
    bwaVLDrapGatewayEntry.setStatus("current")


class _BwaVLDrapGatewayIndex_Type(Integer32):
    """Custom type bwaVLDrapGatewayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_BwaVLDrapGatewayIndex_Type.__name__ = "Integer32"
_BwaVLDrapGatewayIndex_Object = MibTableColumn
bwaVLDrapGatewayIndex = _BwaVLDrapGatewayIndex_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 8, 1, 1),
    _BwaVLDrapGatewayIndex_Type()
)
bwaVLDrapGatewayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLDrapGatewayIndex.setStatus("current")
_BwaVLDrapGatewayIP_Type = IpAddress
_BwaVLDrapGatewayIP_Object = MibTableColumn
bwaVLDrapGatewayIP = _BwaVLDrapGatewayIP_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 8, 1, 2),
    _BwaVLDrapGatewayIP_Type()
)
bwaVLDrapGatewayIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLDrapGatewayIP.setStatus("current")


class _BwaVLDrapGatewayType_Type(Integer32):
    """Custom type bwaVLDrapGatewayType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5,
              6,
              7,
              11,
              255)
        )
    )
    namedValues = NamedValues(
        *(("vgDataVoice", 4),
          ("vgData1Voice1", 5),
          ("vgData4Voice2", 6),
          ("vgDataVoice2", 7),
          ("ngData4Wireless", 11),
          ("vgUnknown", 255))
    )


_BwaVLDrapGatewayType_Type.__name__ = "Integer32"
_BwaVLDrapGatewayType_Object = MibTableColumn
bwaVLDrapGatewayType = _BwaVLDrapGatewayType_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 8, 1, 3),
    _BwaVLDrapGatewayType_Type()
)
bwaVLDrapGatewayType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLDrapGatewayType.setStatus("current")
_BwaVLDrapGatewayNoOfActiveVoiceCalls_Type = Integer32
_BwaVLDrapGatewayNoOfActiveVoiceCalls_Object = MibTableColumn
bwaVLDrapGatewayNoOfActiveVoiceCalls = _BwaVLDrapGatewayNoOfActiveVoiceCalls_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 11, 8, 1, 4),
    _BwaVLDrapGatewayNoOfActiveVoiceCalls_Type()
)
bwaVLDrapGatewayNoOfActiveVoiceCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLDrapGatewayNoOfActiveVoiceCalls.setStatus("current")
_BwaVLTraps_ObjectIdentity = ObjectIdentity
bwaVLTraps = _BwaVLTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 14)
)
_BwaVLTrapSUMacAddr_Type = MacAddress
_BwaVLTrapSUMacAddr_Object = MibScalar
bwaVLTrapSUMacAddr = _BwaVLTrapSUMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 14, 1),
    _BwaVLTrapSUMacAddr_Type()
)
bwaVLTrapSUMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLTrapSUMacAddr.setStatus("current")
_BwaVLTrapText_Type = DisplayString
_BwaVLTrapText_Object = MibScalar
bwaVLTrapText = _BwaVLTrapText_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 14, 3),
    _BwaVLTrapText_Type()
)
bwaVLTrapText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLTrapText.setStatus("current")


class _BwaVLTrapToggle_Type(Integer32):
    """Custom type bwaVLTrapToggle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_BwaVLTrapToggle_Type.__name__ = "Integer32"
_BwaVLTrapToggle_Object = MibScalar
bwaVLTrapToggle = _BwaVLTrapToggle_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 14, 4),
    _BwaVLTrapToggle_Type()
)
bwaVLTrapToggle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLTrapToggle.setStatus("current")


class _BwaVLTrapParameterChanged_Type(Integer32):
    """Custom type bwaVLTrapParameterChanged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("cirOrMir", 1),
          ("ipFilter", 2),
          ("vlan", 4))
    )


_BwaVLTrapParameterChanged_Type.__name__ = "Integer32"
_BwaVLTrapParameterChanged_Object = MibScalar
bwaVLTrapParameterChanged = _BwaVLTrapParameterChanged_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 14, 5),
    _BwaVLTrapParameterChanged_Type()
)
bwaVLTrapParameterChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLTrapParameterChanged.setStatus("current")


class _BwaVLTrapAccessRights_Type(Integer32):
    """Custom type bwaVLTrapAccessRights based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notLoggedIn", 1),
          ("readOnly", 2),
          ("installer", 3),
          ("administrator", 4),
          ("factory", 5))
    )


_BwaVLTrapAccessRights_Type.__name__ = "Integer32"
_BwaVLTrapAccessRights_Object = MibScalar
bwaVLTrapAccessRights = _BwaVLTrapAccessRights_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 14, 6),
    _BwaVLTrapAccessRights_Type()
)
bwaVLTrapAccessRights.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLTrapAccessRights.setStatus("current")


class _BwaVLTrapLog_Type(Integer32):
    """Custom type bwaVLTrapLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("telnetLogin", 3),
          ("telnetLogout", 4))
    )


_BwaVLTrapLog_Type.__name__ = "Integer32"
_BwaVLTrapLog_Object = MibScalar
bwaVLTrapLog = _BwaVLTrapLog_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 14, 7),
    _BwaVLTrapLog_Type()
)
bwaVLTrapLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLTrapLog.setStatus("current")
_BwaVLTrapTelnetUserIpAddress_Type = IpAddress
_BwaVLTrapTelnetUserIpAddress_Object = MibScalar
bwaVLTrapTelnetUserIpAddress = _BwaVLTrapTelnetUserIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 14, 8),
    _BwaVLTrapTelnetUserIpAddress_Type()
)
bwaVLTrapTelnetUserIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLTrapTelnetUserIpAddress.setStatus("current")
_BwaVLTrapRTx_Type = Integer32
_BwaVLTrapRTx_Object = MibScalar
bwaVLTrapRTx = _BwaVLTrapRTx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 14, 9),
    _BwaVLTrapRTx_Type()
)
bwaVLTrapRTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLTrapRTx.setStatus("current")


class _BwaVLTrapFtpOrTftpStatus_Type(Integer32):
    """Custom type bwaVLTrapFtpOrTftpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("successful", 1),
          ("failed", 2))
    )


_BwaVLTrapFtpOrTftpStatus_Type.__name__ = "Integer32"
_BwaVLTrapFtpOrTftpStatus_Object = MibScalar
bwaVLTrapFtpOrTftpStatus = _BwaVLTrapFtpOrTftpStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 14, 10),
    _BwaVLTrapFtpOrTftpStatus_Type()
)
bwaVLTrapFtpOrTftpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLTrapFtpOrTftpStatus.setStatus("current")
_BwaVLDFSMoveFreq_Type = Integer32
_BwaVLDFSMoveFreq_Object = MibScalar
bwaVLDFSMoveFreq = _BwaVLDFSMoveFreq_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 14, 11),
    _BwaVLDFSMoveFreq_Type()
)
bwaVLDFSMoveFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLDFSMoveFreq.setStatus("current")
_BwaVLDFSMoveFreqNew_Type = DisplayString
_BwaVLDFSMoveFreqNew_Object = MibScalar
bwaVLDFSMoveFreqNew = _BwaVLDFSMoveFreqNew_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 14, 12),
    _BwaVLDFSMoveFreqNew_Type()
)
bwaVLDFSMoveFreqNew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLDFSMoveFreqNew.setStatus("current")
_BwaVLEthBroadcastThresholdExceeded_Type = Integer32
_BwaVLEthBroadcastThresholdExceeded_Object = MibScalar
bwaVLEthBroadcastThresholdExceeded = _BwaVLEthBroadcastThresholdExceeded_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 14, 13),
    _BwaVLEthBroadcastThresholdExceeded_Type()
)
bwaVLEthBroadcastThresholdExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLEthBroadcastThresholdExceeded.setStatus("current")


class _BwaVLTrapSubscriberType_Type(Integer32):
    """Custom type bwaVLTrapSubscriberType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              6,
              14,
              24,
              28,
              54,
              100)
        )
    )
    namedValues = NamedValues(
        *(("unknownSubscriberType", 0),
          ("su-3", 3),
          ("su-6", 6),
          ("rb-14", 14),
          ("su-24", 24),
          ("rb-28", 28),
          ("su-54", 54),
          ("rb-100", 100))
    )


_BwaVLTrapSubscriberType_Type.__name__ = "Integer32"
_BwaVLTrapSubscriberType_Object = MibScalar
bwaVLTrapSubscriberType = _BwaVLTrapSubscriberType_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 14, 14),
    _BwaVLTrapSubscriberType_Type()
)
bwaVLTrapSubscriberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLTrapSubscriberType.setStatus("current")
_BwaVLTrapMACAddress_Type = MacAddress
_BwaVLTrapMACAddress_Object = MibScalar
bwaVLTrapMACAddress = _BwaVLTrapMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 14, 15),
    _BwaVLTrapMACAddress_Type()
)
bwaVLTrapMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLTrapMACAddress.setStatus("current")


class _BwaVLNewUnitTypeTrap_Type(Integer32):
    """Custom type bwaVLNewUnitTypeTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bu", 1),
          ("rb", 2))
    )


_BwaVLNewUnitTypeTrap_Type.__name__ = "Integer32"
_BwaVLNewUnitTypeTrap_Object = MibScalar
bwaVLNewUnitTypeTrap = _BwaVLNewUnitTypeTrap_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 14, 16),
    _BwaVLNewUnitTypeTrap_Type()
)
bwaVLNewUnitTypeTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLNewUnitTypeTrap.setStatus("current")
_BwaVLTrapSWVersion_Type = DisplayString
_BwaVLTrapSWVersion_Object = MibScalar
bwaVLTrapSWVersion = _BwaVLTrapSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 1, 14, 17),
    _BwaVLTrapSWVersion_Type()
)
bwaVLTrapSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwaVLTrapSWVersion.setStatus("current")
_BwaOID_ObjectIdentity = ObjectIdentity
bwaOID = _BwaOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4)
)
_BwaVLOID_ObjectIdentity = ObjectIdentity
bwaVLOID = _BwaVLOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1)
)
_BwaVLAU_ObjectIdentity = ObjectIdentity
bwaVLAU = _BwaVLAU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 1)
)
_BwaVLSU_ObjectIdentity = ObjectIdentity
bwaVLSU = _BwaVLSU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 2)
)
_BwaVLProducts_ObjectIdentity = ObjectIdentity
bwaVLProducts = _BwaVLProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 3)
)
_BwaVLAU_BS_ObjectIdentity = ObjectIdentity
bwaVLAU_BS = _BwaVLAU_BS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 4)
)
_BwaVLAU_SA_ObjectIdentity = ObjectIdentity
bwaVLAU_SA = _BwaVLAU_SA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 5)
)
_BwaVLAUS_BS_ObjectIdentity = ObjectIdentity
bwaVLAUS_BS = _BwaVLAUS_BS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 6)
)
_BwaVLAUS_SA_ObjectIdentity = ObjectIdentity
bwaVLAUS_SA = _BwaVLAUS_SA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 7)
)
_BwaVLAU_EZ_ObjectIdentity = ObjectIdentity
bwaVLAU_EZ = _BwaVLAU_EZ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 8)
)
_BwaVLSU_6_1D_ObjectIdentity = ObjectIdentity
bwaVLSU_6_1D = _BwaVLSU_6_1D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 11)
)
_BwaVLSU_6_BD_ObjectIdentity = ObjectIdentity
bwaVLSU_6_BD = _BwaVLSU_6_BD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 12)
)
_BwaVLSU_24_BD_ObjectIdentity = ObjectIdentity
bwaVLSU_24_BD = _BwaVLSU_24_BD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 13)
)
_BwaVLSU_BD_ObjectIdentity = ObjectIdentity
bwaVLSU_BD = _BwaVLSU_BD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 14)
)
_BwaVLSU_54_BD_ObjectIdentity = ObjectIdentity
bwaVLSU_54_BD = _BwaVLSU_54_BD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 15)
)
_BwaVLSU_3_1D_ObjectIdentity = ObjectIdentity
bwaVLSU_3_1D = _BwaVLSU_3_1D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 16)
)
_BwaVLSU_3_4D_ObjectIdentity = ObjectIdentity
bwaVLSU_3_4D = _BwaVLSU_3_4D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 17)
)
_BwaVLSU_I_ObjectIdentity = ObjectIdentity
bwaVLSU_I = _BwaVLSU_I_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 18)
)
_Ptp_BU_B14_ObjectIdentity = ObjectIdentity
ptp_BU_B14 = _Ptp_BU_B14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 21)
)
_Ptp_BU_B28_ObjectIdentity = ObjectIdentity
ptp_BU_B28 = _Ptp_BU_B28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 22)
)
_Ptp_BU_B100_ObjectIdentity = ObjectIdentity
ptp_BU_B100 = _Ptp_BU_B100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 23)
)
_Ptp_RB_B14_ObjectIdentity = ObjectIdentity
ptp_RB_B14 = _Ptp_RB_B14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 31)
)
_Ptp_RB_B28_ObjectIdentity = ObjectIdentity
ptp_RB_B28 = _Ptp_RB_B28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 32)
)
_Ptp_RB_B100_ObjectIdentity = ObjectIdentity
ptp_RB_B100 = _Ptp_RB_B100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 33)
)
_Bwa4900_AU_BS_ObjectIdentity = ObjectIdentity
bwa4900_AU_BS = _Bwa4900_AU_BS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 41)
)
_Bwa4900_AU_SA_ObjectIdentity = ObjectIdentity
bwa4900_AU_SA = _Bwa4900_AU_SA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 42)
)
_Bwa4900_SU_BD_ObjectIdentity = ObjectIdentity
bwa4900_SU_BD = _Bwa4900_SU_BD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 51)
)

# Managed Objects groups


# Notification objects

bwaVLSUassociatedAUTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 3, 2)
)
bwaVLSUassociatedAUTRAP.setObjects(
    ("BWA-DOT11-WLAN-MIB", "bwaVLTrapSUMacAddr")
)
if mibBuilder.loadTexts:
    bwaVLSUassociatedAUTRAP.setStatus(
        "current"
    )

bwaVLAUdisassociatedTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 3, 3)
)
bwaVLAUdisassociatedTRAP.setObjects(
    ("BWA-DOT11-WLAN-MIB", "bwaVLTrapSUMacAddr")
)
if mibBuilder.loadTexts:
    bwaVLAUdisassociatedTRAP.setStatus(
        "current"
    )

bwaVLAUagingTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 3, 4)
)
bwaVLAUagingTRAP.setObjects(
    ("BWA-DOT11-WLAN-MIB", "bwaVLTrapSUMacAddr")
)
if mibBuilder.loadTexts:
    bwaVLAUagingTRAP.setStatus(
        "current"
    )

bwaVLSUassociatedTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 3, 6)
)
bwaVLSUassociatedTRAP.setObjects(
    ("BWA-DOT11-WLAN-MIB", "bwaVLAssociatedAU")
)
if mibBuilder.loadTexts:
    bwaVLSUassociatedTRAP.setStatus(
        "current"
    )

bwaVLAUwirelessQualityTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 3, 20)
)
bwaVLAUwirelessQualityTRAP.setObjects(
      *(("BWA-DOT11-WLAN-MIB", "bwaVLTrapToggle"),
        ("BWA-DOT11-WLAN-MIB", "bwaVLTrapRTx"))
)
if mibBuilder.loadTexts:
    bwaVLAUwirelessQualityTRAP.setStatus(
        "current"
    )

bwaVLPowerUpFromReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 3, 101)
)
bwaVLPowerUpFromReset.setObjects(
    ("BWA-DOT11-WLAN-MIB", "bwaVLUnitMacAddress")
)
if mibBuilder.loadTexts:
    bwaVLPowerUpFromReset.setStatus(
        "current"
    )

bwaVLTelnetStatusTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 3, 102)
)
bwaVLTelnetStatusTRAP.setObjects(
      *(("BWA-DOT11-WLAN-MIB", "bwaVLTrapLog"),
        ("BWA-DOT11-WLAN-MIB", "bwaVLTrapAccessRights"),
        ("BWA-DOT11-WLAN-MIB", "bwaVLTrapTelnetUserIpAddress"))
)
if mibBuilder.loadTexts:
    bwaVLTelnetStatusTRAP.setStatus(
        "current"
    )

bwaVLParameterChangedTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 3, 103)
)
bwaVLParameterChangedTRAP.setObjects(
    ("BWA-DOT11-WLAN-MIB", "bwaVLTrapParameterChanged")
)
if mibBuilder.loadTexts:
    bwaVLParameterChangedTRAP.setStatus(
        "current"
    )

bwaVLLoadingStatusTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 3, 104)
)
bwaVLLoadingStatusTRAP.setObjects(
      *(("BWA-DOT11-WLAN-MIB", "bwaVLTrapFtpOrTftpStatus"),
        ("BWA-DOT11-WLAN-MIB", "bwaVLUnitMacAddress"))
)
if mibBuilder.loadTexts:
    bwaVLLoadingStatusTRAP.setStatus(
        "current"
    )

bwaVLPromiscuousModeTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 3, 105)
)
bwaVLPromiscuousModeTRAP.setObjects(
      *(("BWA-DOT11-WLAN-MIB", "bwaVLTrapToggle"),
        ("BWA-DOT11-WLAN-MIB", "bwaVLUnitMacAddress"))
)
if mibBuilder.loadTexts:
    bwaVLPromiscuousModeTRAP.setStatus(
        "current"
    )

bwaVLDFSRadarDetecetedTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 3, 106)
)
if mibBuilder.loadTexts:
    bwaVLDFSRadarDetecetedTRAP.setStatus(
        "current"
    )

bwaVLDFSFrequcnyTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 3, 107)
)
bwaVLDFSFrequcnyTRAP.setObjects(
      *(("BWA-DOT11-WLAN-MIB", "bwaVLDFSMoveFreq"),
        ("BWA-DOT11-WLAN-MIB", "bwaVLDFSMoveFreqNew"))
)
if mibBuilder.loadTexts:
    bwaVLDFSFrequcnyTRAP.setStatus(
        "current"
    )

bwaVLDFSNoFreeChannelsExistsTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 3, 108)
)
if mibBuilder.loadTexts:
    bwaVLDFSNoFreeChannelsExistsTRAP.setStatus(
        "current"
    )

bwaVLEthBroadcastMulticatLimiterTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 3, 109)
)
bwaVLEthBroadcastMulticatLimiterTRAP.setObjects(
    ("BWA-DOT11-WLAN-MIB", "bwaVLEthBroadcastThresholdExceeded")
)
if mibBuilder.loadTexts:
    bwaVLEthBroadcastMulticatLimiterTRAP.setStatus(
        "current"
    )

bwaVLAUSUnsupportedSubscriberTypeTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 3, 110)
)
bwaVLAUSUnsupportedSubscriberTypeTRAP.setObjects(
      *(("BWA-DOT11-WLAN-MIB", "bwaVLTrapSUMacAddr"),
        ("BWA-DOT11-WLAN-MIB", "bwaVLTrapSubscriberType"))
)
if mibBuilder.loadTexts:
    bwaVLAUSUnsupportedSubscriberTypeTRAP.setStatus(
        "current"
    )

bwaVLUnitTypeChangedTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 3, 111)
)
bwaVLUnitTypeChangedTRAP.setObjects(
      *(("BWA-DOT11-WLAN-MIB", "bwaVLTrapMACAddress"),
        ("BWA-DOT11-WLAN-MIB", "bwaVLNewUnitTypeTrap"))
)
if mibBuilder.loadTexts:
    bwaVLUnitTypeChangedTRAP.setStatus(
        "current"
    )

bwaVLWLPrioritizationNotSupportedBySUTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 4, 1, 3, 112)
)
bwaVLWLPrioritizationNotSupportedBySUTRAP.setObjects(
      *(("BWA-DOT11-WLAN-MIB", "bwaVLTrapSUMacAddr"),
        ("BWA-DOT11-WLAN-MIB", "bwaVLTrapSWVersion"))
)
if mibBuilder.loadTexts:
    bwaVLWLPrioritizationNotSupportedBySUTRAP.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BWA-DOT11-WLAN-MIB",
    **{"MacAddress": MacAddress,
       "DisplayString": DisplayString,
       "bwa": bwa,
       "products": products,
       "bwaVLMib": bwaVLMib,
       "bwaVLSysInfo": bwaVLSysInfo,
       "bwaVLUnitHwVersion": bwaVLUnitHwVersion,
       "bwaVLRunningSoftwareVersion": bwaVLRunningSoftwareVersion,
       "bwaVLRunningFrom": bwaVLRunningFrom,
       "bwaVLMainVersionNumber": bwaVLMainVersionNumber,
       "bwaVLMainVersionFileName": bwaVLMainVersionFileName,
       "bwaVLShadowVersionNumber": bwaVLShadowVersionNumber,
       "bwaVLShadowVersionFileName": bwaVLShadowVersionFileName,
       "bwaVLUnitMacAddress": bwaVLUnitMacAddress,
       "bwaVLUnitType": bwaVLUnitType,
       "bwaVLAssociatedAU": bwaVLAssociatedAU,
       "bwaVLNumOfAssociationsSinceLastReset": bwaVLNumOfAssociationsSinceLastReset,
       "bwaVLCurrentNumOfAssociations": bwaVLCurrentNumOfAssociations,
       "bwaVLUnitBootVersion": bwaVLUnitBootVersion,
       "bwaVLRadioBand": bwaVLRadioBand,
       "bwaVLCurrentEthernetPortState": bwaVLCurrentEthernetPortState,
       "bwaVLTimeSinceLastReset": bwaVLTimeSinceLastReset,
       "bwaVLCountryDependentParameters": bwaVLCountryDependentParameters,
       "bwaVLCountryCode": bwaVLCountryCode,
       "bwaVLCountryDependentParamsTable": bwaVLCountryDependentParamsTable,
       "bwaVLCountryDependentParameterEntry": bwaVLCountryDependentParameterEntry,
       "bwaVLCountryDependentParameterTableIdx": bwaVLCountryDependentParameterTableIdx,
       "bwaVLCountryDependentParameterFrequencies": bwaVLCountryDependentParameterFrequencies,
       "bwaVLAllowedBandwidth": bwaVLAllowedBandwidth,
       "bwaVLRegulationMaxTxPowerAtAntennaPort": bwaVLRegulationMaxTxPowerAtAntennaPort,
       "bwaVLRegulationMaxEIRP": bwaVLRegulationMaxEIRP,
       "bwaVLMinModulationLevel": bwaVLMinModulationLevel,
       "bwaVLMaxModulationLevel": bwaVLMaxModulationLevel,
       "bwaVLBurstModeSupport": bwaVLBurstModeSupport,
       "bwaVLMaximumBurstDuration": bwaVLMaximumBurstDuration,
       "bwaVLDfsSupport": bwaVLDfsSupport,
       "bwaVLMinimumHwRevision": bwaVLMinimumHwRevision,
       "bwaVLAuthenticationEncryptionSupport": bwaVLAuthenticationEncryptionSupport,
       "bwaVLDataEncryptionSupport": bwaVLDataEncryptionSupport,
       "bwaVLAESEncryptionSupport": bwaVLAESEncryptionSupport,
       "bwaVLAntennaGainChange": bwaVLAntennaGainChange,
       "bwaVLAteTestResults": bwaVLAteTestResults,
       "bwaVLSerialNumber": bwaVLSerialNumber,
       "bwaVLUnitControl": bwaVLUnitControl,
       "bwaVLResetUnit": bwaVLResetUnit,
       "bwaVLSetDefaults": bwaVLSetDefaults,
       "bwaVLUnitName": bwaVLUnitName,
       "bwaVLFlashMemoryControl": bwaVLFlashMemoryControl,
       "bwaVLTelnetLogoutTimer": bwaVLTelnetLogoutTimer,
       "bwaVLSaveCurrentConfigurationAsOperatorDefaults": bwaVLSaveCurrentConfigurationAsOperatorDefaults,
       "bwaVLExitTelnet": bwaVLExitTelnet,
       "bwaVLUnitPasswords": bwaVLUnitPasswords,
       "bwaVLReadOnlyPassword": bwaVLReadOnlyPassword,
       "bwaVLInstallerPassword": bwaVLInstallerPassword,
       "bwaVLAdminPassword": bwaVLAdminPassword,
       "bwaVLEthernetNegotiationMode": bwaVLEthernetNegotiationMode,
       "bwaVLFTPParameters": bwaVLFTPParameters,
       "bwaVLFTPServerParams": bwaVLFTPServerParams,
       "bwaVLFTPServerUserName": bwaVLFTPServerUserName,
       "bwaVLFTPServerPassword": bwaVLFTPServerPassword,
       "bwaVLFTPClientIPAddress": bwaVLFTPClientIPAddress,
       "bwaVLFTPServerIpAddress": bwaVLFTPServerIpAddress,
       "bwaVLFTPClientMask": bwaVLFTPClientMask,
       "bwaVLFTPGatewayIpAddress": bwaVLFTPGatewayIpAddress,
       "bwaVLFTPSwDownload": bwaVLFTPSwDownload,
       "bwaVLFTPSwFileName": bwaVLFTPSwFileName,
       "bwaVLFTPSwSourceDir": bwaVLFTPSwSourceDir,
       "bwaVLFTPDownloadSwFile": bwaVLFTPDownloadSwFile,
       "bwaVLConfigurationFileLoading": bwaVLConfigurationFileLoading,
       "bwaVLConfigurationFileName": bwaVLConfigurationFileName,
       "bwaVLOperatorDefaultsFileName": bwaVLOperatorDefaultsFileName,
       "bwaVLFTPConfigurationFileSourceDir": bwaVLFTPConfigurationFileSourceDir,
       "bwaVLExecuteFTPConfigurationFileLoading": bwaVLExecuteFTPConfigurationFileLoading,
       "bwaVLEventLogFileUploading": bwaVLEventLogFileUploading,
       "bwaVLEventLogFileName": bwaVLEventLogFileName,
       "bwaVLEventLogDestinationDir": bwaVLEventLogDestinationDir,
       "bwaVLUploadEventLogFile": bwaVLUploadEventLogFile,
       "bwaVLLoadingStatus": bwaVLLoadingStatus,
       "bwaVLEventLogFileParams": bwaVLEventLogFileParams,
       "bwaVLEventLogPolicy": bwaVLEventLogPolicy,
       "bwaVLEraseEventLog": bwaVLEraseEventLog,
       "bwaVLSystemLocation": bwaVLSystemLocation,
       "bwaVLFeatureUpgrade": bwaVLFeatureUpgrade,
       "bwaVLFeatureUpgradeManually": bwaVLFeatureUpgradeManually,
       "bwaVLChangeUnitType": bwaVLChangeUnitType,
       "bwaLighteAPWorkingMode": bwaLighteAPWorkingMode,
       "bwaVLNwMngParameters": bwaVLNwMngParameters,
       "bwaVLAccessToNwMng": bwaVLAccessToNwMng,
       "bwaVLNwMngFilter": bwaVLNwMngFilter,
       "mngIpFilterTable": mngIpFilterTable,
       "mngIpFilterEntry": mngIpFilterEntry,
       "bwaVLNwMngIpAddress": bwaVLNwMngIpAddress,
       "bwaVLNwMngIpTableIdx": bwaVLNwMngIpTableIdx,
       "bwaVLDeleteOneNwIpAddr": bwaVLDeleteOneNwIpAddr,
       "bwaVLDeleteAllNwIpAddrs": bwaVLDeleteAllNwIpAddrs,
       "bwaVLAccessToNwTrap": bwaVLAccessToNwTrap,
       "mngTrapTable": mngTrapTable,
       "mngTrapEntry": mngTrapEntry,
       "bwaVLNwMngTrapCommunity": bwaVLNwMngTrapCommunity,
       "bwaVLNwMngTrapAddress": bwaVLNwMngTrapAddress,
       "bwaVLNwTrapTableIdx": bwaVLNwTrapTableIdx,
       "bwaVLDeleteOneTrapAddr": bwaVLDeleteOneTrapAddr,
       "bwaVLDeleteAllTrapAddrs": bwaVLDeleteAllTrapAddrs,
       "bwaVLMngIpRangesTable": bwaVLMngIpRangesTable,
       "bwaVLMngIpRangeEntry": bwaVLMngIpRangeEntry,
       "bwaVLMngIpRangeIdx": bwaVLMngIpRangeIdx,
       "bwaVLMngIpRangeFlag": bwaVLMngIpRangeFlag,
       "bwaVLMngIpRangeStart": bwaVLMngIpRangeStart,
       "bwaVLMngIpRangeEnd": bwaVLMngIpRangeEnd,
       "bwaVLMngIpRangeMask": bwaVLMngIpRangeMask,
       "bwaVLDeleteOneNwIpRange": bwaVLDeleteOneNwIpRange,
       "bwaVLDeleteAllNwIpRanges": bwaVLDeleteAllNwIpRanges,
       "bwaVLApClientIpAddress": bwaVLApClientIpAddress,
       "bwaVLIpParams": bwaVLIpParams,
       "bwaVLUnitIpAddress": bwaVLUnitIpAddress,
       "bwaVLSubNetMask": bwaVLSubNetMask,
       "bwaVLDefaultGWAddress": bwaVLDefaultGWAddress,
       "bwaVLUseDhcp": bwaVLUseDhcp,
       "bwaVLAccessToDHCP": bwaVLAccessToDHCP,
       "bwaVLRunTimeIPaddr": bwaVLRunTimeIPaddr,
       "bwaVLRunTimeSubNetMask": bwaVLRunTimeSubNetMask,
       "bwaVLRunTimeDefaultIPGateway": bwaVLRunTimeDefaultIPGateway,
       "bwaVLBridgeParameters": bwaVLBridgeParameters,
       "bwaVLVLANSupport": bwaVLVLANSupport,
       "bwaVLVlanID": bwaVLVlanID,
       "bwaVLEthernetLinkType": bwaVLEthernetLinkType,
       "bwaVLManagementVlanID": bwaVLManagementVlanID,
       "bwaVLVLANForwarding": bwaVLVLANForwarding,
       "bwaVLVlanForwardingSupport": bwaVLVlanForwardingSupport,
       "bwaVLVlanForwardingTable": bwaVLVlanForwardingTable,
       "bwaVLVlanForwardingEntry": bwaVLVlanForwardingEntry,
       "bwaVLVlanForwardingTableIdx": bwaVLVlanForwardingTableIdx,
       "bwaVLVlanIdForwarding": bwaVLVlanIdForwarding,
       "bwaVLVlanRelaying": bwaVLVlanRelaying,
       "bwaVLVlanRelayingSupport": bwaVLVlanRelayingSupport,
       "bwaVLVlanRelayingTable": bwaVLVlanRelayingTable,
       "bwaVLVlanRelayingEntry": bwaVLVlanRelayingEntry,
       "bwaVLVlanRelayingTableIdx": bwaVLVlanRelayingTableIdx,
       "bwaVLVlanIdRelaying": bwaVLVlanIdRelaying,
       "bwaVLVLANTrafficPriority": bwaVLVLANTrafficPriority,
       "bwaVLVlanDataPriority": bwaVLVlanDataPriority,
       "bwaVLVlanManagementPriority": bwaVLVlanManagementPriority,
       "bwaVLVlanPriorityThreshold": bwaVLVlanPriorityThreshold,
       "bwaVLVLANQinQ": bwaVLVLANQinQ,
       "bwaVLQinQEthertype": bwaVLQinQEthertype,
       "bwaVLQinQProviderVlanID": bwaVLQinQProviderVlanID,
       "bwaVLBridgeAgingTime": bwaVLBridgeAgingTime,
       "bwaVLBroadcastRelaying": bwaVLBroadcastRelaying,
       "bwaVLUnicastRelaying": bwaVLUnicastRelaying,
       "bwaVLEthBroadcastFiltering": bwaVLEthBroadcastFiltering,
       "bwaVLEthBroadcastingParameters": bwaVLEthBroadcastingParameters,
       "bwaVLDHCPBroadcastOverrideFilter": bwaVLDHCPBroadcastOverrideFilter,
       "bwaVLPPPoEBroadcastOverrideFilter": bwaVLPPPoEBroadcastOverrideFilter,
       "bwaVLARPBroadcastOverrideFilter": bwaVLARPBroadcastOverrideFilter,
       "bwaVLEthBroadcastMulticastLimiterOption": bwaVLEthBroadcastMulticastLimiterOption,
       "bwaVLEthBroadcastMulticastLimiterThreshold": bwaVLEthBroadcastMulticastLimiterThreshold,
       "bwaVLEthBroadcastMulticastLimiterSendTrapInterval": bwaVLEthBroadcastMulticastLimiterSendTrapInterval,
       "bwaVLToSPriorityParameters": bwaVLToSPriorityParameters,
       "bwaVLToSPrecedenceThreshold": bwaVLToSPrecedenceThreshold,
       "bwaVLRoamingOption": bwaVLRoamingOption,
       "bwaVLMacAddressDenyList": bwaVLMacAddressDenyList,
       "bwaVLMacAddressDenyListTable": bwaVLMacAddressDenyListTable,
       "bwaVLMacAddressDenyListEntry": bwaVLMacAddressDenyListEntry,
       "bwaVLMacAddressDenyListTableIdx": bwaVLMacAddressDenyListTableIdx,
       "bwaVLMacAddressDenyListId": bwaVLMacAddressDenyListId,
       "bwaVLMacAddressDenyListAdd": bwaVLMacAddressDenyListAdd,
       "bwaVLMacAddressDenyListRemove": bwaVLMacAddressDenyListRemove,
       "bwaVLNumberOfMacAddressesInDenyList": bwaVLNumberOfMacAddressesInDenyList,
       "bwaVLMacAddressDenyListAction": bwaVLMacAddressDenyListAction,
       "bwaVLPortsControl": bwaVLPortsControl,
       "bwaVLEthernetPortControl": bwaVLEthernetPortControl,
       "bwaVLAirInterface": bwaVLAirInterface,
       "bwaVLESSIDParameters": bwaVLESSIDParameters,
       "bwaVLESSID": bwaVLESSID,
       "bwaVLOperatorESSIDOption": bwaVLOperatorESSIDOption,
       "bwaVLOperatorESSID": bwaVLOperatorESSID,
       "bwaVLRunTimeESSID": bwaVLRunTimeESSID,
       "bwaVLMaximumCellRadius": bwaVLMaximumCellRadius,
       "bwaVLAIFS": bwaVLAIFS,
       "bwaVLWirelessTrapThreshold": bwaVLWirelessTrapThreshold,
       "bwaVLTransmitPowerTable": bwaVLTransmitPowerTable,
       "bwaVLTransmitPowerEntry": bwaVLTransmitPowerEntry,
       "bwaVLTransmitPowerIdx": bwaVLTransmitPowerIdx,
       "bwaVLApplicableModulationLevel": bwaVLApplicableModulationLevel,
       "bwaVLMaximumTxPowerRange": bwaVLMaximumTxPowerRange,
       "bwaVLTxPower": bwaVLTxPower,
       "bwaVLCurrentTxPower": bwaVLCurrentTxPower,
       "bwaVLMaximumTransmitPowerTable": bwaVLMaximumTransmitPowerTable,
       "bwaVLMaximumTransmitPowerEntry": bwaVLMaximumTransmitPowerEntry,
       "bwaVLMaximumTransmitPowerIdx": bwaVLMaximumTransmitPowerIdx,
       "bwaVLMaxTxApplicableModulationLevel": bwaVLMaxTxApplicableModulationLevel,
       "bwaVLDefinedMaximumTxPowerRange": bwaVLDefinedMaximumTxPowerRange,
       "bwaVLMaxTxPower": bwaVLMaxTxPower,
       "bwaVLMaxNumOfAssociations": bwaVLMaxNumOfAssociations,
       "bwaVLBestAu": bwaVLBestAu,
       "bwaVLBestAuSupport": bwaVLBestAuSupport,
       "bwaVLBestAuNoOfScanningAttempts": bwaVLBestAuNoOfScanningAttempts,
       "bwaVLPreferredAuMacAddress": bwaVLPreferredAuMacAddress,
       "bwaVLNeighborAuTable": bwaVLNeighborAuTable,
       "bwaVLNeighborAuEntry": bwaVLNeighborAuEntry,
       "bwaVLNeighborAuIdx": bwaVLNeighborAuIdx,
       "bwaVLNeighborAuMacAdd": bwaVLNeighborAuMacAdd,
       "bwaVLNeighborAuESSID": bwaVLNeighborAuESSID,
       "bwaVLNeighborAuSNR": bwaVLNeighborAuSNR,
       "bwaVLNeighborAuAssocLoadStatus": bwaVLNeighborAuAssocLoadStatus,
       "bwaVLNeighborAuMark": bwaVLNeighborAuMark,
       "bwaVLNeighborAuHwRevision": bwaVLNeighborAuHwRevision,
       "bwaVLNeighborAuCountryCode": bwaVLNeighborAuCountryCode,
       "bwaVLNeighborAuSwVer": bwaVLNeighborAuSwVer,
       "bwaVLNeighborAuAtpcOption": bwaVLNeighborAuAtpcOption,
       "bwaVLNeighborAuAdapModOption": bwaVLNeighborAuAdapModOption,
       "bwaVLNeighborAuBurstModeOption": bwaVLNeighborAuBurstModeOption,
       "bwaVLNeighborAuDfsOption": bwaVLNeighborAuDfsOption,
       "bwaVLNeighborAuConcatenationOption": bwaVLNeighborAuConcatenationOption,
       "bwaVLNeighborAuLearnCountryCodeBySU": bwaVLNeighborAuLearnCountryCodeBySU,
       "bwaVLNeighborAuSecurityMode": bwaVLNeighborAuSecurityMode,
       "bwaVLNeighborAuAuthOption": bwaVLNeighborAuAuthOption,
       "bwaVLNeighborAuDataEncyptOption": bwaVLNeighborAuDataEncyptOption,
       "bwaVLNeighborAuPerSuDistanceLearning": bwaVLNeighborAuPerSuDistanceLearning,
       "bwaVLFrequencyDefinition": bwaVLFrequencyDefinition,
       "bwaVLSubBandLowerFrequency": bwaVLSubBandLowerFrequency,
       "bwaVLSubBandUpperFrequency": bwaVLSubBandUpperFrequency,
       "bwaVLScanningStep": bwaVLScanningStep,
       "bwaVLFrequencySubsetTable": bwaVLFrequencySubsetTable,
       "bwaVLFrequencySubsetEntry": bwaVLFrequencySubsetEntry,
       "bwaVLFrequencySubsetTableIdx": bwaVLFrequencySubsetTableIdx,
       "bwaVLFrequencySubsetFrequency": bwaVLFrequencySubsetFrequency,
       "bwaVLFrequencySubsetActive": bwaVLFrequencySubsetActive,
       "bwaVLFrequencySubsetFrequencyNew": bwaVLFrequencySubsetFrequencyNew,
       "bwaVLSetSelectedFreqSubset": bwaVLSetSelectedFreqSubset,
       "bwaVLCurrentFrequencySubsetTable": bwaVLCurrentFrequencySubsetTable,
       "bwaVLCurrentFrequencySubsetEntry": bwaVLCurrentFrequencySubsetEntry,
       "bwaVLCurrentFrequencySubsetTableIdx": bwaVLCurrentFrequencySubsetTableIdx,
       "bwaVLCurrentFrequencySubsetFrequency": bwaVLCurrentFrequencySubsetFrequency,
       "bwaVLCurrentFrequencySubsetFrequencyNew": bwaVLCurrentFrequencySubsetFrequencyNew,
       "bwaVLCurrentAUOperatingFrequency": bwaVLCurrentAUOperatingFrequency,
       "bwaVLAUDefinedFrequency": bwaVLAUDefinedFrequency,
       "bwaVLCurrentSUOperatingFrequency": bwaVLCurrentSUOperatingFrequency,
       "bwaVLSubBandSelect": bwaVLSubBandSelect,
       "bwaVLSelectSubBandIndex": bwaVLSelectSubBandIndex,
       "bwaVLDFSParameters": bwaVLDFSParameters,
       "bwaVLDFSOption": bwaVLDFSOption,
       "bwaVLDFSChannelCheckTime": bwaVLDFSChannelCheckTime,
       "bwaVLDFSChannelAvoidancePeriod": bwaVLDFSChannelAvoidancePeriod,
       "bwaVLDFSSuWaitingOption": bwaVLDFSSuWaitingOption,
       "bwaVLDFSClearRadarDetectedChannelsAfterReset": bwaVLDFSClearRadarDetectedChannelsAfterReset,
       "bwaVLDFSRadarDetectionChannelsTable": bwaVLDFSRadarDetectionChannelsTable,
       "bwaVLDFSRadarDetectionChannelsEntry": bwaVLDFSRadarDetectionChannelsEntry,
       "bwaVLDFSChannelIdx": bwaVLDFSChannelIdx,
       "bwaVLDFSChannelFrequency": bwaVLDFSChannelFrequency,
       "bwaVLDFSChannelRadarStatus": bwaVLDFSChannelRadarStatus,
       "bwaVLDFSChannelFrequencyNew": bwaVLDFSChannelFrequencyNew,
       "bwaVLDFSMinimumPulsesToDetect": bwaVLDFSMinimumPulsesToDetect,
       "bwaVLDFSChannelReuseParameters": bwaVLDFSChannelReuseParameters,
       "bwaVLDFSChannelReuseOption": bwaVLDFSChannelReuseOption,
       "bwaVLDFSRadarActivityAssessmentPeriod": bwaVLDFSRadarActivityAssessmentPeriod,
       "bwaVLDFSMaximumNumberOfDetectionsInAssessmentPeriod": bwaVLDFSMaximumNumberOfDetectionsInAssessmentPeriod,
       "bwaVLCountryCodeLearningBySU": bwaVLCountryCodeLearningBySU,
       "bwaVLCurrentAUOperatingFrequencyNew": bwaVLCurrentAUOperatingFrequencyNew,
       "bwaVLAUDefinedFrequencyNew": bwaVLAUDefinedFrequencyNew,
       "bwaVLAutoSubBandSelect": bwaVLAutoSubBandSelect,
       "bwaVLAutoSubBandSelectedFreqSubset": bwaVLAutoSubBandSelectedFreqSubset,
       "bwaVLAutoSubBandFrequencySubsetTable": bwaVLAutoSubBandFrequencySubsetTable,
       "bwaVLAutoSubBandFrequencySubsetEntry": bwaVLAutoSubBandFrequencySubsetEntry,
       "bwaVLAutoSubBandFrequencySubsetBandIdx": bwaVLAutoSubBandFrequencySubsetBandIdx,
       "bwaVLAutoSubBandFrequencySubsetFrequencyIdx": bwaVLAutoSubBandFrequencySubsetFrequencyIdx,
       "bwaVLAutoSubBandFrequencySubsetActive": bwaVLAutoSubBandFrequencySubsetActive,
       "bwaVLAutoSubBandFrequencySubsetFrequency": bwaVLAutoSubBandFrequencySubsetFrequency,
       "bwaVLATPC": bwaVLATPC,
       "bwaVLAtpcOption": bwaVLAtpcOption,
       "bwaVLDeltaFromMinSNRLevel": bwaVLDeltaFromMinSNRLevel,
       "bwaVLMinimumSNRLevel": bwaVLMinimumSNRLevel,
       "bwaVLMinimumIntervalBetweenATPCMessages": bwaVLMinimumIntervalBetweenATPCMessages,
       "bwaVLPowerLevelSteps": bwaVLPowerLevelSteps,
       "bwaVLCellDistanceParameters": bwaVLCellDistanceParameters,
       "bwaVLCellDistanceMode": bwaVLCellDistanceMode,
       "bwaVLFairnessFactor": bwaVLFairnessFactor,
       "bwaVLMeasuredCellDistance": bwaVLMeasuredCellDistance,
       "bwaVLUnitWithMaxDistance": bwaVLUnitWithMaxDistance,
       "bwaVLPerSuDistanceLearning": bwaVLPerSuDistanceLearning,
       "bwaVLScanningMode": bwaVLScanningMode,
       "bwaVLAntennaGain": bwaVLAntennaGain,
       "bwaVLSpectrumAnalysisParameters": bwaVLSpectrumAnalysisParameters,
       "bwaVLSpectrumAnalysisChannelScanPeriod": bwaVLSpectrumAnalysisChannelScanPeriod,
       "bwaVLSpectrumAnalysisScanCycles": bwaVLSpectrumAnalysisScanCycles,
       "bwaVLAutomaticChannelSelection": bwaVLAutomaticChannelSelection,
       "bwaVLSpectrumAnalysisActivation": bwaVLSpectrumAnalysisActivation,
       "bwaVLSpectrumAnalysisStatus": bwaVLSpectrumAnalysisStatus,
       "bwaVLResetSpectrumCounters": bwaVLResetSpectrumCounters,
       "bwaVLSpectrumAnalysisInformationTable": bwaVLSpectrumAnalysisInformationTable,
       "bwaVLSpectrumAnalysisInformationEntry": bwaVLSpectrumAnalysisInformationEntry,
       "bwaVLSpectrumAnalysisInformationTableIdx": bwaVLSpectrumAnalysisInformationTableIdx,
       "bwaVLSpectrumAnalysisInformationChannel": bwaVLSpectrumAnalysisInformationChannel,
       "bwaVLSpectrumAnalysisInformationSignalCount": bwaVLSpectrumAnalysisInformationSignalCount,
       "bwaVLSpectrumAnalysisInformationSignalSNR": bwaVLSpectrumAnalysisInformationSignalSNR,
       "bwaVLSpectrumAnalysisInformationSignalWidth": bwaVLSpectrumAnalysisInformationSignalWidth,
       "bwaVLSpectrumAnalysisInformationOFDMFrames": bwaVLSpectrumAnalysisInformationOFDMFrames,
       "bwaVLMaxNumOfAssociationsLimit": bwaVLMaxNumOfAssociationsLimit,
       "bwaVLDisassociate": bwaVLDisassociate,
       "bwaVLDisassociateAllSUs": bwaVLDisassociateAllSUs,
       "bwaVLDisassociateSuByMacAddress": bwaVLDisassociateSuByMacAddress,
       "bwaVLTxControl": bwaVLTxControl,
       "bwaVLLostBeaconsWatchdogThreshold": bwaVLLostBeaconsWatchdogThreshold,
       "bwaVLTransmitPower": bwaVLTransmitPower,
       "bwaVLMaximumTxPower": bwaVLMaximumTxPower,
       "bwaVLCountryCodeParameters": bwaVLCountryCodeParameters,
       "bwaLCountryCodeReApply": bwaLCountryCodeReApply,
       "bwaVLServiceParameters": bwaVLServiceParameters,
       "bwaVLMirDownlink": bwaVLMirDownlink,
       "bwaVLMirUplink": bwaVLMirUplink,
       "bwaVLCirDownlink": bwaVLCirDownlink,
       "bwaVLCirUplink": bwaVLCirUplink,
       "bwaVLMaxDelay": bwaVLMaxDelay,
       "bwaVLMaxBurstDuration": bwaVLMaxBurstDuration,
       "bwaVLGracefulDegradationLimit": bwaVLGracefulDegradationLimit,
       "bwaVLMirOnlyOption": bwaVLMirOnlyOption,
       "bwaVLTrafficPrioritization": bwaVLTrafficPrioritization,
       "bwaVLTrafficPriVLAN": bwaVLTrafficPriVLAN,
       "bwaVLVLANPriorityThreshold": bwaVLVLANPriorityThreshold,
       "bwaVLTrafficPriIPToS": bwaVLTrafficPriIPToS,
       "bwaVLToSPrioritizationOption": bwaVLToSPrioritizationOption,
       "bwaVLIPPrecedenceThreshold": bwaVLIPPrecedenceThreshold,
       "bwaVLIPDSCPThreshold": bwaVLIPDSCPThreshold,
       "bwaVLTrafficPriUdpTcpPortRange": bwaVLTrafficPriUdpTcpPortRange,
       "bwaVLUdpTcpPortRangePrioritizationOption": bwaVLUdpTcpPortRangePrioritizationOption,
       "bwaVLUdpPortRangeConfig": bwaVLUdpPortRangeConfig,
       "bwaVLUdpPortPriRTPRTCP": bwaVLUdpPortPriRTPRTCP,
       "bwaVLUdpPortRangeNum": bwaVLUdpPortRangeNum,
       "bwaVLUdpPortRangeTable": bwaVLUdpPortRangeTable,
       "bwaVLUdpPortRangeEntry": bwaVLUdpPortRangeEntry,
       "bwaVLUdpPortRangeStart": bwaVLUdpPortRangeStart,
       "bwaVLUdpPortRangeEnd": bwaVLUdpPortRangeEnd,
       "bwaVLUdpPortRangeIdx": bwaVLUdpPortRangeIdx,
       "bwaVLUdpPortRangeAdd": bwaVLUdpPortRangeAdd,
       "bwaVLUdpPortRangeDelete": bwaVLUdpPortRangeDelete,
       "bwaVLUdpPortRangeDeleteAll": bwaVLUdpPortRangeDeleteAll,
       "bwaVLTcpPortRangeConfig": bwaVLTcpPortRangeConfig,
       "bwaVLTcpPortPriRTPRTCP": bwaVLTcpPortPriRTPRTCP,
       "bwaVLTcpPortRangeNum": bwaVLTcpPortRangeNum,
       "bwaVLTcpPortRangeTable": bwaVLTcpPortRangeTable,
       "bwaVLTcpPortRangeEntry": bwaVLTcpPortRangeEntry,
       "bwaVLTcpPortRangeStart": bwaVLTcpPortRangeStart,
       "bwaVLTcpPortRangeEnd": bwaVLTcpPortRangeEnd,
       "bwaVLTcpPortRangeIdx": bwaVLTcpPortRangeIdx,
       "bwaVLTcpPortRangeAdd": bwaVLTcpPortRangeAdd,
       "bwaVLTcpPortRangeDelete": bwaVLTcpPortRangeDelete,
       "bwaVLTcpPortRangeDeleteAll": bwaVLTcpPortRangeDeleteAll,
       "bwaVLWirelessLinkPrioritization": bwaVLWirelessLinkPrioritization,
       "bwaVLWirelessLinkPrioritizationOption": bwaVLWirelessLinkPrioritizationOption,
       "bwaVLlowPriorityAIFS": bwaVLlowPriorityAIFS,
       "bwaVLHWRetriesHighPriority": bwaVLHWRetriesHighPriority,
       "bwaVLHWRetriesLowPriority": bwaVLHWRetriesLowPriority,
       "bwaVLAUBurstDurationHighPriority": bwaVLAUBurstDurationHighPriority,
       "bwaVLAUBurstDurationLowPriority": bwaVLAUBurstDurationLowPriority,
       "bwaVLSUBurstDurationHighPriority": bwaVLSUBurstDurationHighPriority,
       "bwaVLSUBurstDurationLowPriority": bwaVLSUBurstDurationLowPriority,
       "bwaVLDrap": bwaVLDrap,
       "bwaVLDrapSupport": bwaVLDrapSupport,
       "bwaVLDrapUdpPort": bwaVLDrapUdpPort,
       "bwaVLDrapMaxNumberOfVoiceCalls": bwaVLDrapMaxNumberOfVoiceCalls,
       "bwaVLDrapTTL": bwaVLDrapTTL,
       "bwaVLDrapNoOfActiveVoiceCalls": bwaVLDrapNoOfActiveVoiceCalls,
       "bwaVLLowPriorityTrafficMinimumPercent": bwaVLLowPriorityTrafficMinimumPercent,
       "bwaVLSUPMirDownlink": bwaVLSUPMirDownlink,
       "bwaVLMIRThresholdPercent": bwaVLMIRThresholdPercent,
       "bwaVLUserFilterParams": bwaVLUserFilterParams,
       "bwaVLUserFilterOption": bwaVLUserFilterOption,
       "bwaVLIpFilterTable": bwaVLIpFilterTable,
       "bwaVLIpFilterEntry": bwaVLIpFilterEntry,
       "bwaVLIpID": bwaVLIpID,
       "bwaVLMaskID": bwaVLMaskID,
       "bwaVLIpFilterRange": bwaVLIpFilterRange,
       "bwaVLIpFilterIdx": bwaVLIpFilterIdx,
       "bwaVLDeleteOneUserFilter": bwaVLDeleteOneUserFilter,
       "bwaVLDeleteAllUserFilters": bwaVLDeleteAllUserFilters,
       "bwaVLDHCPUnicastOverrideFilter": bwaVLDHCPUnicastOverrideFilter,
       "bwaVLSecurityParameters": bwaVLSecurityParameters,
       "bwaVLAuthenticationAlgorithm": bwaVLAuthenticationAlgorithm,
       "bwaVLSUDefaultKeyID": bwaVLSUDefaultKeyID,
       "bwaVLDataEncryptionOption": bwaVLDataEncryptionOption,
       "bwaVLAUDefaultMulticastKeyID": bwaVLAUDefaultMulticastKeyID,
       "bwaVLSecurityMode": bwaVLSecurityMode,
       "bwaVLAuthenticationPromiscuousMode": bwaVLAuthenticationPromiscuousMode,
       "bwaVLKey1": bwaVLKey1,
       "bwaVLKey2": bwaVLKey2,
       "bwaVLKey3": bwaVLKey3,
       "bwaVLKey4": bwaVLKey4,
       "bwaVLSecurityModeSupport": bwaVLSecurityModeSupport,
       "bwaVLPerformanceParams": bwaVLPerformanceParams,
       "bwaVLRTSThreshold": bwaVLRTSThreshold,
       "bwaVLMinContentionWindow": bwaVLMinContentionWindow,
       "bwaVLMaxContentionWindow": bwaVLMaxContentionWindow,
       "bwaVLMaximumModulationLevel": bwaVLMaximumModulationLevel,
       "bwaVLMulticastModulationLevel": bwaVLMulticastModulationLevel,
       "bwaVLAvgSNRMemoryFactor": bwaVLAvgSNRMemoryFactor,
       "bwaVLHardwareRetries": bwaVLHardwareRetries,
       "bwaVLAdaptiveModulationParams": bwaVLAdaptiveModulationParams,
       "bwaVLAdaptiveModulationAlgorithmOption": bwaVLAdaptiveModulationAlgorithmOption,
       "bwaVLSoftwareRetrySupport": bwaVLSoftwareRetrySupport,
       "bwaVLNumOfSoftwareRetries": bwaVLNumOfSoftwareRetries,
       "bwaVLMinIntervalBetweenAdaptiveModulationAlgorithmMessages": bwaVLMinIntervalBetweenAdaptiveModulationAlgorithmMessages,
       "bwaVLAdaptiveModulationDecisionThresholds": bwaVLAdaptiveModulationDecisionThresholds,
       "bwaVLBurstMode": bwaVLBurstMode,
       "bwaVLBurstModeOption": bwaVLBurstModeOption,
       "bwaVLBurstInterval": bwaVLBurstInterval,
       "bwaVLConcatenationParameters": bwaVLConcatenationParameters,
       "bwaVLConcatenationOption": bwaVLConcatenationOption,
       "bwaVLConcatenationMaximumNumberOfFrames": bwaVLConcatenationMaximumNumberOfFrames,
       "bwaVLConcatenationMaxFrameSize": bwaVLConcatenationMaxFrameSize,
       "bwaVLSiteSurvey": bwaVLSiteSurvey,
       "bwaVLAverageReceiveSNR": bwaVLAverageReceiveSNR,
       "bwaVLTrafficStatistics": bwaVLTrafficStatistics,
       "bwaVLResetTrafficCounters": bwaVLResetTrafficCounters,
       "bwaVLEthCounters": bwaVLEthCounters,
       "bwaVLTotalRxFramesViaEthernet": bwaVLTotalRxFramesViaEthernet,
       "bwaVLTxWirelessToEthernet": bwaVLTxWirelessToEthernet,
       "bwaVLWirelessLinkCounters": bwaVLWirelessLinkCounters,
       "bwaVLTxFramesToWireless": bwaVLTxFramesToWireless,
       "bwaVLAUBeaconsToWireless": bwaVLAUBeaconsToWireless,
       "bwaVLDataAndOtherMngFramesToWireless": bwaVLDataAndOtherMngFramesToWireless,
       "bwaVLTotalTxFramesToWireless": bwaVLTotalTxFramesToWireless,
       "bwaVLTotalTransmittedUnicasts": bwaVLTotalTransmittedUnicasts,
       "bwaVLTotalTransmittedConcatenatedFramesDouble": bwaVLTotalTransmittedConcatenatedFramesDouble,
       "bwaVLTotalTransmittedConcatenatedFramesSingle": bwaVLTotalTransmittedConcatenatedFramesSingle,
       "bwaVLTotalTransmittedConcatenatedFramesMore": bwaVLTotalTransmittedConcatenatedFramesMore,
       "bwaVLTotalRxFramesFromWireless": bwaVLTotalRxFramesFromWireless,
       "bwaVLTotalRetransmittedFrames": bwaVLTotalRetransmittedFrames,
       "bwaVLFramesDropped": bwaVLFramesDropped,
       "bwaVLDataFramesSubmittedToBridge": bwaVLDataFramesSubmittedToBridge,
       "bwaVLFramesSubmittedViaHighQueue": bwaVLFramesSubmittedViaHighQueue,
       "bwaVLFramesSubmittedViaMidQueue": bwaVLFramesSubmittedViaMidQueue,
       "bwaVLFramesSubmittedViaLowQueue": bwaVLFramesSubmittedViaLowQueue,
       "bwaVLTotalNoOfDataFramesSubmitted": bwaVLTotalNoOfDataFramesSubmitted,
       "bwaVLTotalRecievedDataFrames": bwaVLTotalRecievedDataFrames,
       "bwaVLRecievedBadFrames": bwaVLRecievedBadFrames,
       "bwaVLNoOfDuplicateFramesDiscarded": bwaVLNoOfDuplicateFramesDiscarded,
       "bwaVLNoOfInternallyDiscardedMirCir": bwaVLNoOfInternallyDiscardedMirCir,
       "bwaVLTotalRxConcatenatedFramesDouble": bwaVLTotalRxConcatenatedFramesDouble,
       "bwaVLTotalRxConcatenatedFramesSingle": bwaVLTotalRxConcatenatedFramesSingle,
       "bwaVLTotalRxConcatenatedFramesMore": bwaVLTotalRxConcatenatedFramesMore,
       "bwaVLWirelessLinkEvents": bwaVLWirelessLinkEvents,
       "bwaVLTxEvents": bwaVLTxEvents,
       "bwaVLDroppedFrameEvents": bwaVLDroppedFrameEvents,
       "bwaVLFramesDelayedDueToSwRetry": bwaVLFramesDelayedDueToSwRetry,
       "bwaVLUnderrunEvents": bwaVLUnderrunEvents,
       "bwaVLOthersTxEvents": bwaVLOthersTxEvents,
       "bwaVLTotalTxEvents": bwaVLTotalTxEvents,
       "bwaVLRxEvents": bwaVLRxEvents,
       "bwaVLPhyErrors": bwaVLPhyErrors,
       "bwaVLCRCErrors": bwaVLCRCErrors,
       "bwaVLOverrunEvents": bwaVLOverrunEvents,
       "bwaVLRxDecryptEvents": bwaVLRxDecryptEvents,
       "bwaVLTotalRxEvents": bwaVLTotalRxEvents,
       "bwaVLPerModulationLevelCounters": bwaVLPerModulationLevelCounters,
       "bwaVLResetPerModulationLevelCounters": bwaVLResetPerModulationLevelCounters,
       "bwaVLSUPerModulationLevelCountersTable": bwaVLSUPerModulationLevelCountersTable,
       "bwaVLSUPerModulationLevelCountersEntry": bwaVLSUPerModulationLevelCountersEntry,
       "bwaVLSUPerModulationLevelCountersTableIdx": bwaVLSUPerModulationLevelCountersTableIdx,
       "bwaVLSUPerModulationLevelCountersApplicableModLevel": bwaVLSUPerModulationLevelCountersApplicableModLevel,
       "bwaVLSUPerModulationLevelCountersTxSuccess": bwaVLSUPerModulationLevelCountersTxSuccess,
       "bwaVLSUPerModulationLevelCountersTxFailed": bwaVLSUPerModulationLevelCountersTxFailed,
       "bwaVLAverageModulationLevel": bwaVLAverageModulationLevel,
       "bwaVLMacAddressDatabase": bwaVLMacAddressDatabase,
       "bwaVLAUMacAddressDatabase": bwaVLAUMacAddressDatabase,
       "bwaVLAUAdbResetAllModulationLevelCounters": bwaVLAUAdbResetAllModulationLevelCounters,
       "bwaVLAUAdbTable": bwaVLAUAdbTable,
       "bwaVLAUAdbEntry": bwaVLAUAdbEntry,
       "bwaVLAdbIndex": bwaVLAdbIndex,
       "bwaVLAdbMacAddress": bwaVLAdbMacAddress,
       "bwaVLAdbStatus": bwaVLAdbStatus,
       "bwaVLAdbSwVersion": bwaVLAdbSwVersion,
       "bwaVLAdbSNR": bwaVLAdbSNR,
       "bwaVLAdbMaxModulationLevel": bwaVLAdbMaxModulationLevel,
       "bwaVLAdbTxFramesTotal": bwaVLAdbTxFramesTotal,
       "bwaVLAdbDroppedFramesTotal": bwaVLAdbDroppedFramesTotal,
       "bwaVLAdbTxSuccessModLevel1": bwaVLAdbTxSuccessModLevel1,
       "bwaVLAdbTxSuccessModLevel2": bwaVLAdbTxSuccessModLevel2,
       "bwaVLAdbTxSuccessModLevel3": bwaVLAdbTxSuccessModLevel3,
       "bwaVLAdbTxSuccessModLevel4": bwaVLAdbTxSuccessModLevel4,
       "bwaVLAdbTxSuccessModLevel5": bwaVLAdbTxSuccessModLevel5,
       "bwaVLAdbTxSuccessModLevel6": bwaVLAdbTxSuccessModLevel6,
       "bwaVLAdbTxSuccessModLevel7": bwaVLAdbTxSuccessModLevel7,
       "bwaVLAdbTxSuccessModLevel8": bwaVLAdbTxSuccessModLevel8,
       "bwaVLAdbTxFailedModLevel1": bwaVLAdbTxFailedModLevel1,
       "bwaVLAdbTxFailedModLevel2": bwaVLAdbTxFailedModLevel2,
       "bwaVLAdbTxFailedModLevel3": bwaVLAdbTxFailedModLevel3,
       "bwaVLAdbTxFailedModLevel4": bwaVLAdbTxFailedModLevel4,
       "bwaVLAdbTxFailedModLevel5": bwaVLAdbTxFailedModLevel5,
       "bwaVLAdbTxFailedModLevel6": bwaVLAdbTxFailedModLevel6,
       "bwaVLAdbTxFailedModLevel7": bwaVLAdbTxFailedModLevel7,
       "bwaVLAdbTxFailedModLevel8": bwaVLAdbTxFailedModLevel8,
       "bwaVLAdbCirTx": bwaVLAdbCirTx,
       "bwaVLAdbMirTx": bwaVLAdbMirTx,
       "bwaVLAdbCirRx": bwaVLAdbCirRx,
       "bwaVLAdbMirRx": bwaVLAdbMirRx,
       "bwaVLAdbCirMaxDelay": bwaVLAdbCirMaxDelay,
       "bwaVLAdbDistance": bwaVLAdbDistance,
       "bwaVLAdbHwRevision": bwaVLAdbHwRevision,
       "bwaVLAdbCpldVer": bwaVLAdbCpldVer,
       "bwaVLAdbCountryCode": bwaVLAdbCountryCode,
       "bwaVLAdbBootVer": bwaVLAdbBootVer,
       "bwaVLAdbAtpcOption": bwaVLAdbAtpcOption,
       "bwaVLAdbAdapModOption": bwaVLAdbAdapModOption,
       "bwaVLAdbBurstModeOption": bwaVLAdbBurstModeOption,
       "bwaVLAdbConcatenationOption": bwaVLAdbConcatenationOption,
       "bwaVLAdbSecurityMode": bwaVLAdbSecurityMode,
       "bwaVLAdbAuthOption": bwaVLAdbAuthOption,
       "bwaVLAdbDataEncyptOption": bwaVLAdbDataEncyptOption,
       "bwaVLAdbAge": bwaVLAdbAge,
       "bwaVLAdbUnitName": bwaVLAdbUnitName,
       "bwaVLUpLinkQualityIndicator": bwaVLUpLinkQualityIndicator,
       "bwaVLMeasureUpLinkQualityIndicator": bwaVLMeasureUpLinkQualityIndicator,
       "bwaVLReadUpLinkQualityIndicator": bwaVLReadUpLinkQualityIndicator,
       "bwaVLUpLinkQualityIndicatorStatus": bwaVLUpLinkQualityIndicatorStatus,
       "bwaVLMacPinpoint": bwaVLMacPinpoint,
       "bwaVLMacPinpointTable": bwaVLMacPinpointTable,
       "bwaVLMacPinpointEntry": bwaVLMacPinpointEntry,
       "mptEthernetStationMACAddress": mptEthernetStationMACAddress,
       "mptUnitMACAddress": mptUnitMACAddress,
       "bwaVLDrapGatewaysTable": bwaVLDrapGatewaysTable,
       "bwaVLDrapGatewayEntry": bwaVLDrapGatewayEntry,
       "bwaVLDrapGatewayIndex": bwaVLDrapGatewayIndex,
       "bwaVLDrapGatewayIP": bwaVLDrapGatewayIP,
       "bwaVLDrapGatewayType": bwaVLDrapGatewayType,
       "bwaVLDrapGatewayNoOfActiveVoiceCalls": bwaVLDrapGatewayNoOfActiveVoiceCalls,
       "bwaVLTraps": bwaVLTraps,
       "bwaVLTrapSUMacAddr": bwaVLTrapSUMacAddr,
       "bwaVLTrapText": bwaVLTrapText,
       "bwaVLTrapToggle": bwaVLTrapToggle,
       "bwaVLTrapParameterChanged": bwaVLTrapParameterChanged,
       "bwaVLTrapAccessRights": bwaVLTrapAccessRights,
       "bwaVLTrapLog": bwaVLTrapLog,
       "bwaVLTrapTelnetUserIpAddress": bwaVLTrapTelnetUserIpAddress,
       "bwaVLTrapRTx": bwaVLTrapRTx,
       "bwaVLTrapFtpOrTftpStatus": bwaVLTrapFtpOrTftpStatus,
       "bwaVLDFSMoveFreq": bwaVLDFSMoveFreq,
       "bwaVLDFSMoveFreqNew": bwaVLDFSMoveFreqNew,
       "bwaVLEthBroadcastThresholdExceeded": bwaVLEthBroadcastThresholdExceeded,
       "bwaVLTrapSubscriberType": bwaVLTrapSubscriberType,
       "bwaVLTrapMACAddress": bwaVLTrapMACAddress,
       "bwaVLNewUnitTypeTrap": bwaVLNewUnitTypeTrap,
       "bwaVLTrapSWVersion": bwaVLTrapSWVersion,
       "bwaOID": bwaOID,
       "bwaVLOID": bwaVLOID,
       "bwaVLAU": bwaVLAU,
       "bwaVLSU": bwaVLSU,
       "bwaVLProducts": bwaVLProducts,
       "bwaVLSUassociatedAUTRAP": bwaVLSUassociatedAUTRAP,
       "bwaVLAUdisassociatedTRAP": bwaVLAUdisassociatedTRAP,
       "bwaVLAUagingTRAP": bwaVLAUagingTRAP,
       "bwaVLSUassociatedTRAP": bwaVLSUassociatedTRAP,
       "bwaVLAUwirelessQualityTRAP": bwaVLAUwirelessQualityTRAP,
       "bwaVLPowerUpFromReset": bwaVLPowerUpFromReset,
       "bwaVLTelnetStatusTRAP": bwaVLTelnetStatusTRAP,
       "bwaVLParameterChangedTRAP": bwaVLParameterChangedTRAP,
       "bwaVLLoadingStatusTRAP": bwaVLLoadingStatusTRAP,
       "bwaVLPromiscuousModeTRAP": bwaVLPromiscuousModeTRAP,
       "bwaVLDFSRadarDetecetedTRAP": bwaVLDFSRadarDetecetedTRAP,
       "bwaVLDFSFrequcnyTRAP": bwaVLDFSFrequcnyTRAP,
       "bwaVLDFSNoFreeChannelsExistsTRAP": bwaVLDFSNoFreeChannelsExistsTRAP,
       "bwaVLEthBroadcastMulticatLimiterTRAP": bwaVLEthBroadcastMulticatLimiterTRAP,
       "bwaVLAUSUnsupportedSubscriberTypeTRAP": bwaVLAUSUnsupportedSubscriberTypeTRAP,
       "bwaVLUnitTypeChangedTRAP": bwaVLUnitTypeChangedTRAP,
       "bwaVLWLPrioritizationNotSupportedBySUTRAP": bwaVLWLPrioritizationNotSupportedBySUTRAP,
       "bwaVLAU-BS": bwaVLAU_BS,
       "bwaVLAU-SA": bwaVLAU_SA,
       "bwaVLAUS-BS": bwaVLAUS_BS,
       "bwaVLAUS-SA": bwaVLAUS_SA,
       "bwaVLAU-EZ": bwaVLAU_EZ,
       "bwaVLSU-6-1D": bwaVLSU_6_1D,
       "bwaVLSU-6-BD": bwaVLSU_6_BD,
       "bwaVLSU-24-BD": bwaVLSU_24_BD,
       "bwaVLSU-BD": bwaVLSU_BD,
       "bwaVLSU-54-BD": bwaVLSU_54_BD,
       "bwaVLSU-3-1D": bwaVLSU_3_1D,
       "bwaVLSU-3-4D": bwaVLSU_3_4D,
       "bwaVLSU-I": bwaVLSU_I,
       "ptp-BU-B14": ptp_BU_B14,
       "ptp-BU-B28": ptp_BU_B28,
       "ptp-BU-B100": ptp_BU_B100,
       "ptp-RB-B14": ptp_RB_B14,
       "ptp-RB-B28": ptp_RB_B28,
       "ptp-RB-B100": ptp_RB_B100,
       "bwa4900-AU-BS": bwa4900_AU_BS,
       "bwa4900-AU-SA": bwa4900_AU_SA,
       "bwa4900-SU-BD": bwa4900_SU_BD}
)
