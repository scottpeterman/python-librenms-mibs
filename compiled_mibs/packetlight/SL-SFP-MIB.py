# SNMP MIB module (SL-SFP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\packetlight\SL-SFP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:20:06 2025
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

(Float128TC,
 Float32TC,
 Float64TC) = mibBuilder.importSymbols(
    "FLOAT-TC-MIB",
    "Float128TC",
    "Float32TC",
    "Float64TC")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(PerfCurrentCount,
 PerfIntervalCount,
 PerfTotalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount",
    "PerfTotalCount")

(CleiCode,) = mibBuilder.importSymbols(
    "SL-ENTITY-MIB",
    "CleiCode")

(sitelight,) = mibBuilder.importSymbols(
    "SL-NE-MIB",
    "sitelight")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

slSfp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SfpConf_ObjectIdentity = ObjectIdentity
sfpConf = _SfpConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1)
)
_SfpConfigTable_Object = MibTable
sfpConfigTable = _SfpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1)
)
if mibBuilder.loadTexts:
    sfpConfigTable.setStatus("current")
_SfpConfigEntry_Object = MibTableRow
sfpConfigEntry = _SfpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1)
)
sfpConfigEntry.setIndexNames(
    (0, "SL-SFP-MIB", "sfpConfigInterface"),
)
if mibBuilder.loadTexts:
    sfpConfigEntry.setStatus("current")
_SfpConfigInterface_Type = InterfaceIndex
_SfpConfigInterface_Object = MibTableColumn
sfpConfigInterface = _SfpConfigInterface_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 1),
    _SfpConfigInterface_Type()
)
sfpConfigInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigInterface.setStatus("current")


class _SfpConfigXcvrId_Type(Integer32):
    """Custom type sfpConfigXcvrId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              6,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              20)
        )
    )
    namedValues = NamedValues(
        *(("unknone", 0),
          ("gbic", 1),
          ("module", 2),
          ("sfp1310", 3),
          ("xfp", 6),
          ("sfpDwdm", 11),
          ("qsfp", 12),
          ("qsfpPlus", 13),
          ("cfp", 14),
          ("cxp", 15),
          ("coherent", 16),
          ("qsfp28", 17),
          ("cfp2", 20))
    )


_SfpConfigXcvrId_Type.__name__ = "Integer32"
_SfpConfigXcvrId_Object = MibTableColumn
sfpConfigXcvrId = _SfpConfigXcvrId_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 2),
    _SfpConfigXcvrId_Type()
)
sfpConfigXcvrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigXcvrId.setStatus("current")


class _SfpConfig1310ExtXcvrId_Type(Integer32):
    """Custom type sfpConfig1310ExtXcvrId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("modDef0", 0),
          ("modDef1", 1),
          ("modDef2", 2),
          ("modDef3", 3),
          ("modDef4", 4),
          ("modDef5", 5),
          ("modDef6", 6),
          ("modDef7", 7))
    )


_SfpConfig1310ExtXcvrId_Type.__name__ = "Integer32"
_SfpConfig1310ExtXcvrId_Object = MibTableColumn
sfpConfig1310ExtXcvrId = _SfpConfig1310ExtXcvrId_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 3),
    _SfpConfig1310ExtXcvrId_Type()
)
sfpConfig1310ExtXcvrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfig1310ExtXcvrId.setStatus("current")
_SfpConfigWdmExtXcvrId_Type = Integer32
_SfpConfigWdmExtXcvrId_Object = MibTableColumn
sfpConfigWdmExtXcvrId = _SfpConfigWdmExtXcvrId_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 4),
    _SfpConfigWdmExtXcvrId_Type()
)
sfpConfigWdmExtXcvrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigWdmExtXcvrId.setStatus("current")


class _SfpConfigConnectorCode_Type(Integer32):
    """Custom type sfpConfigConnectorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              32,
              33)
        )
    )
    namedValues = NamedValues(
        *(("conUnknown", 0),
          ("conSc", 1),
          ("conFcCopper1", 2),
          ("conFcCopper2", 3),
          ("conBncTnc", 4),
          ("conFcCoaxial", 5),
          ("conFiberJack", 6),
          ("conLc", 7),
          ("conMtRj", 8),
          ("conMu", 9),
          ("comSg", 10),
          ("conOpticalPigtail", 11),
          ("conHssdc2", 32),
          ("conCopperPigtail", 33))
    )


_SfpConfigConnectorCode_Type.__name__ = "Integer32"
_SfpConfigConnectorCode_Object = MibTableColumn
sfpConfigConnectorCode = _SfpConfigConnectorCode_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 5),
    _SfpConfigConnectorCode_Type()
)
sfpConfigConnectorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigConnectorCode.setStatus("current")
_SfpConfigInfibandCompliance_Type = Integer32
_SfpConfigInfibandCompliance_Object = MibTableColumn
sfpConfigInfibandCompliance = _SfpConfigInfibandCompliance_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 6),
    _SfpConfigInfibandCompliance_Type()
)
sfpConfigInfibandCompliance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigInfibandCompliance.setStatus("current")
_SfpConfigEsconCompliance_Type = Integer32
_SfpConfigEsconCompliance_Object = MibTableColumn
sfpConfigEsconCompliance = _SfpConfigEsconCompliance_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 7),
    _SfpConfigEsconCompliance_Type()
)
sfpConfigEsconCompliance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigEsconCompliance.setStatus("current")
_SfpConfigSonetCompliance_Type = Integer32
_SfpConfigSonetCompliance_Object = MibTableColumn
sfpConfigSonetCompliance = _SfpConfigSonetCompliance_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 8),
    _SfpConfigSonetCompliance_Type()
)
sfpConfigSonetCompliance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigSonetCompliance.setStatus("current")
_SfpConfigGbeCompliance_Type = Integer32
_SfpConfigGbeCompliance_Object = MibTableColumn
sfpConfigGbeCompliance = _SfpConfigGbeCompliance_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 9),
    _SfpConfigGbeCompliance_Type()
)
sfpConfigGbeCompliance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigGbeCompliance.setStatus("current")
_SfpConfigFcCompliance_Type = Integer32
_SfpConfigFcCompliance_Object = MibTableColumn
sfpConfigFcCompliance = _SfpConfigFcCompliance_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 10),
    _SfpConfigFcCompliance_Type()
)
sfpConfigFcCompliance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigFcCompliance.setStatus("current")


class _SfpConfigEncodingCode_Type(Integer32):
    """Custom type sfpConfigEncodingCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("encUnspecified", 0),
          ("enc8B10B", 1),
          ("enc4B5B", 2),
          ("encNrz", 3),
          ("encManchester", 4),
          ("encSonet", 5),
          ("enc64B66B", 6))
    )


_SfpConfigEncodingCode_Type.__name__ = "Integer32"
_SfpConfigEncodingCode_Object = MibTableColumn
sfpConfigEncodingCode = _SfpConfigEncodingCode_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 11),
    _SfpConfigEncodingCode_Type()
)
sfpConfigEncodingCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigEncodingCode.setStatus("current")
_SfpConfigNominalBitRate_Type = Integer32
_SfpConfigNominalBitRate_Object = MibTableColumn
sfpConfigNominalBitRate = _SfpConfigNominalBitRate_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 12),
    _SfpConfigNominalBitRate_Type()
)
sfpConfigNominalBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigNominalBitRate.setStatus("current")
_SfpConfigLength9mKm_Type = Integer32
_SfpConfigLength9mKm_Object = MibTableColumn
sfpConfigLength9mKm = _SfpConfigLength9mKm_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 13),
    _SfpConfigLength9mKm_Type()
)
sfpConfigLength9mKm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigLength9mKm.setStatus("current")
_SfpConfigLength9m100m_Type = Integer32
_SfpConfigLength9m100m_Object = MibTableColumn
sfpConfigLength9m100m = _SfpConfigLength9m100m_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 14),
    _SfpConfigLength9m100m_Type()
)
sfpConfigLength9m100m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigLength9m100m.setStatus("current")
_SfpConfigLength50m10m_Type = Integer32
_SfpConfigLength50m10m_Object = MibTableColumn
sfpConfigLength50m10m = _SfpConfigLength50m10m_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 15),
    _SfpConfigLength50m10m_Type()
)
sfpConfigLength50m10m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigLength50m10m.setStatus("current")
_SfpConfigLength62m10m_Type = Integer32
_SfpConfigLength62m10m_Object = MibTableColumn
sfpConfigLength62m10m = _SfpConfigLength62m10m_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 16),
    _SfpConfigLength62m10m_Type()
)
sfpConfigLength62m10m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigLength62m10m.setStatus("current")
_SfpConfigLengthCopper1m_Type = Integer32
_SfpConfigLengthCopper1m_Object = MibTableColumn
sfpConfigLengthCopper1m = _SfpConfigLengthCopper1m_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 17),
    _SfpConfigLengthCopper1m_Type()
)
sfpConfigLengthCopper1m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigLengthCopper1m.setStatus("current")
_SfpConfigMaxTemp_Type = Integer32
_SfpConfigMaxTemp_Object = MibTableColumn
sfpConfigMaxTemp = _SfpConfigMaxTemp_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 18),
    _SfpConfigMaxTemp_Type()
)
sfpConfigMaxTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigMaxTemp.setStatus("current")
_SfpConfigMinTemp_Type = Integer32
_SfpConfigMinTemp_Object = MibTableColumn
sfpConfigMinTemp = _SfpConfigMinTemp_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 19),
    _SfpConfigMinTemp_Type()
)
sfpConfigMinTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigMinTemp.setStatus("current")
_SfpConfigMaxSupplyCurrent_Type = Integer32
_SfpConfigMaxSupplyCurrent_Object = MibTableColumn
sfpConfigMaxSupplyCurrent = _SfpConfigMaxSupplyCurrent_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 20),
    _SfpConfigMaxSupplyCurrent_Type()
)
sfpConfigMaxSupplyCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigMaxSupplyCurrent.setStatus("current")
_SfpConfigChannelSpacing_Type = Integer32
_SfpConfigChannelSpacing_Object = MibTableColumn
sfpConfigChannelSpacing = _SfpConfigChannelSpacing_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 21),
    _SfpConfigChannelSpacing_Type()
)
sfpConfigChannelSpacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigChannelSpacing.setStatus("current")


class _SfpConfigVendorName_Type(SnmpAdminString):
    """Custom type sfpConfigVendorName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SfpConfigVendorName_Type.__name__ = "SnmpAdminString"
_SfpConfigVendorName_Object = MibTableColumn
sfpConfigVendorName = _SfpConfigVendorName_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 22),
    _SfpConfigVendorName_Type()
)
sfpConfigVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigVendorName.setStatus("current")
_SfpConfigOptionalWdm_Type = Integer32
_SfpConfigOptionalWdm_Object = MibTableColumn
sfpConfigOptionalWdm = _SfpConfigOptionalWdm_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 23),
    _SfpConfigOptionalWdm_Type()
)
sfpConfigOptionalWdm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigOptionalWdm.setStatus("current")
_SfpConfigVendorOUI_Type = Integer32
_SfpConfigVendorOUI_Object = MibTableColumn
sfpConfigVendorOUI = _SfpConfigVendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 24),
    _SfpConfigVendorOUI_Type()
)
sfpConfigVendorOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigVendorOUI.setStatus("current")


class _SfpConfigVendorPN_Type(SnmpAdminString):
    """Custom type sfpConfigVendorPN based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SfpConfigVendorPN_Type.__name__ = "SnmpAdminString"
_SfpConfigVendorPN_Object = MibTableColumn
sfpConfigVendorPN = _SfpConfigVendorPN_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 25),
    _SfpConfigVendorPN_Type()
)
sfpConfigVendorPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigVendorPN.setStatus("current")


class _SfpConfigVendorRev_Type(SnmpAdminString):
    """Custom type sfpConfigVendorRev based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_SfpConfigVendorRev_Type.__name__ = "SnmpAdminString"
_SfpConfigVendorRev_Object = MibTableColumn
sfpConfigVendorRev = _SfpConfigVendorRev_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 26),
    _SfpConfigVendorRev_Type()
)
sfpConfigVendorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigVendorRev.setStatus("current")
_SfpConfigWaveLength_Type = Integer32
_SfpConfigWaveLength_Object = MibTableColumn
sfpConfigWaveLength = _SfpConfigWaveLength_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 27),
    _SfpConfigWaveLength_Type()
)
sfpConfigWaveLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigWaveLength.setStatus("current")
_SfpConfigExtendedOptions_Type = Integer32
_SfpConfigExtendedOptions_Object = MibTableColumn
sfpConfigExtendedOptions = _SfpConfigExtendedOptions_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 28),
    _SfpConfigExtendedOptions_Type()
)
sfpConfigExtendedOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigExtendedOptions.setStatus("current")
_SfpConfigMaxBitRate_Type = Integer32
_SfpConfigMaxBitRate_Object = MibTableColumn
sfpConfigMaxBitRate = _SfpConfigMaxBitRate_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 29),
    _SfpConfigMaxBitRate_Type()
)
sfpConfigMaxBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigMaxBitRate.setStatus("current")
_SfpConfigMinBitRate_Type = Integer32
_SfpConfigMinBitRate_Object = MibTableColumn
sfpConfigMinBitRate = _SfpConfigMinBitRate_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 30),
    _SfpConfigMinBitRate_Type()
)
sfpConfigMinBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigMinBitRate.setStatus("current")


class _SfpConfigVendorSN_Type(SnmpAdminString):
    """Custom type sfpConfigVendorSN based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SfpConfigVendorSN_Type.__name__ = "SnmpAdminString"
_SfpConfigVendorSN_Object = MibTableColumn
sfpConfigVendorSN = _SfpConfigVendorSN_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 31),
    _SfpConfigVendorSN_Type()
)
sfpConfigVendorSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigVendorSN.setStatus("current")


class _SfpConfigDateCode_Type(SnmpAdminString):
    """Custom type sfpConfigDateCode based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_SfpConfigDateCode_Type.__name__ = "SnmpAdminString"
_SfpConfigDateCode_Object = MibTableColumn
sfpConfigDateCode = _SfpConfigDateCode_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 32),
    _SfpConfigDateCode_Type()
)
sfpConfigDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigDateCode.setStatus("current")
_SfpConfigDiagnosticMonitoring_Type = Integer32
_SfpConfigDiagnosticMonitoring_Object = MibTableColumn
sfpConfigDiagnosticMonitoring = _SfpConfigDiagnosticMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 33),
    _SfpConfigDiagnosticMonitoring_Type()
)
sfpConfigDiagnosticMonitoring.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigDiagnosticMonitoring.setStatus("current")
_SfpConfigEnhanceOptions_Type = Integer32
_SfpConfigEnhanceOptions_Object = MibTableColumn
sfpConfigEnhanceOptions = _SfpConfigEnhanceOptions_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 34),
    _SfpConfigEnhanceOptions_Type()
)
sfpConfigEnhanceOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigEnhanceOptions.setStatus("current")


class _SfpConfig8472Compliance_Type(Integer32):
    """Custom type sfpConfig8472Compliance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noDiag", 0),
          ("rev93", 1),
          ("rev94", 2))
    )


_SfpConfig8472Compliance_Type.__name__ = "Integer32"
_SfpConfig8472Compliance_Object = MibTableColumn
sfpConfig8472Compliance = _SfpConfig8472Compliance_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 35),
    _SfpConfig8472Compliance_Type()
)
sfpConfig8472Compliance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfig8472Compliance.setStatus("current")
_SfpConfigTunableWaveLength_Type = Integer32
_SfpConfigTunableWaveLength_Object = MibTableColumn
sfpConfigTunableWaveLength = _SfpConfigTunableWaveLength_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 36),
    _SfpConfigTunableWaveLength_Type()
)
sfpConfigTunableWaveLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpConfigTunableWaveLength.setStatus("current")
_SfpConfigVoaControl_Type = Integer32
_SfpConfigVoaControl_Object = MibTableColumn
sfpConfigVoaControl = _SfpConfigVoaControl_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 37),
    _SfpConfigVoaControl_Type()
)
sfpConfigVoaControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpConfigVoaControl.setStatus("current")
_SfpConfigVdtControl_Type = Integer32
_SfpConfigVdtControl_Object = MibTableColumn
sfpConfigVdtControl = _SfpConfigVdtControl_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 38),
    _SfpConfigVdtControl_Type()
)
sfpConfigVdtControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpConfigVdtControl.setStatus("current")
_SfpConfigPilotToneModulation_Type = Integer32
_SfpConfigPilotToneModulation_Object = MibTableColumn
sfpConfigPilotToneModulation = _SfpConfigPilotToneModulation_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 39),
    _SfpConfigPilotToneModulation_Type()
)
sfpConfigPilotToneModulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpConfigPilotToneModulation.setStatus("current")


class _SfpConfigCleiCode_Type(DisplayString):
    """Custom type sfpConfigCleiCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_SfpConfigCleiCode_Type.__name__ = "DisplayString"
_SfpConfigCleiCode_Object = MibTableColumn
sfpConfigCleiCode = _SfpConfigCleiCode_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 40),
    _SfpConfigCleiCode_Type()
)
sfpConfigCleiCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigCleiCode.setStatus("current")
_SfpConfigXfpExtXcvrId_Type = Integer32
_SfpConfigXfpExtXcvrId_Object = MibTableColumn
sfpConfigXfpExtXcvrId = _SfpConfigXfpExtXcvrId_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 41),
    _SfpConfigXfpExtXcvrId_Type()
)
sfpConfigXfpExtXcvrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigXfpExtXcvrId.setStatus("current")
_SfpConfigXfpEncodingCode_Type = Integer32
_SfpConfigXfpEncodingCode_Object = MibTableColumn
sfpConfigXfpEncodingCode = _SfpConfigXfpEncodingCode_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 42),
    _SfpConfigXfpEncodingCode_Type()
)
sfpConfigXfpEncodingCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigXfpEncodingCode.setStatus("current")
_SfpConfigXfpMinBitRate_Type = Integer32
_SfpConfigXfpMinBitRate_Object = MibTableColumn
sfpConfigXfpMinBitRate = _SfpConfigXfpMinBitRate_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 43),
    _SfpConfigXfpMinBitRate_Type()
)
sfpConfigXfpMinBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigXfpMinBitRate.setStatus("current")
_SfpConfigXfpMaxBitRate_Type = Integer32
_SfpConfigXfpMaxBitRate_Object = MibTableColumn
sfpConfigXfpMaxBitRate = _SfpConfigXfpMaxBitRate_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 44),
    _SfpConfigXfpMaxBitRate_Type()
)
sfpConfigXfpMaxBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigXfpMaxBitRate.setStatus("current")
_SfpConfig10GSonetCompliance_Type = Integer32
_SfpConfig10GSonetCompliance_Object = MibTableColumn
sfpConfig10GSonetCompliance = _SfpConfig10GSonetCompliance_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 45),
    _SfpConfig10GSonetCompliance_Type()
)
sfpConfig10GSonetCompliance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfig10GSonetCompliance.setStatus("current")
_SfpConfig10GbeCompliance_Type = Integer32
_SfpConfig10GbeCompliance_Object = MibTableColumn
sfpConfig10GbeCompliance = _SfpConfig10GbeCompliance_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 46),
    _SfpConfig10GbeCompliance_Type()
)
sfpConfig10GbeCompliance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfig10GbeCompliance.setStatus("current")
_SfpConfig10GFcCompliance_Type = Integer32
_SfpConfig10GFcCompliance_Object = MibTableColumn
sfpConfig10GFcCompliance = _SfpConfig10GFcCompliance_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 47),
    _SfpConfig10GFcCompliance_Type()
)
sfpConfig10GFcCompliance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfig10GFcCompliance.setStatus("current")
_SfpConfigXfpDeviceTech_Type = Integer32
_SfpConfigXfpDeviceTech_Object = MibTableColumn
sfpConfigXfpDeviceTech = _SfpConfigXfpDeviceTech_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 48),
    _SfpConfigXfpDeviceTech_Type()
)
sfpConfigXfpDeviceTech.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigXfpDeviceTech.setStatus("current")
_SfpConfigXfpTuningSupported_Type = Integer32
_SfpConfigXfpTuningSupported_Object = MibTableColumn
sfpConfigXfpTuningSupported = _SfpConfigXfpTuningSupported_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 49),
    _SfpConfigXfpTuningSupported_Type()
)
sfpConfigXfpTuningSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigXfpTuningSupported.setStatus("current")
_SfpConfigXfpDesiredChannel_Type = Integer32
_SfpConfigXfpDesiredChannel_Object = MibTableColumn
sfpConfigXfpDesiredChannel = _SfpConfigXfpDesiredChannel_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 50),
    _SfpConfigXfpDesiredChannel_Type()
)
sfpConfigXfpDesiredChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpConfigXfpDesiredChannel.setStatus("current")
_SfpConfigXfpDesiredWl_Type = Integer32
_SfpConfigXfpDesiredWl_Object = MibTableColumn
sfpConfigXfpDesiredWl = _SfpConfigXfpDesiredWl_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 51),
    _SfpConfigXfpDesiredWl_Type()
)
sfpConfigXfpDesiredWl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpConfigXfpDesiredWl.setStatus("current")
_SfpConfigXfpWlError_Type = Integer32
_SfpConfigXfpWlError_Object = MibTableColumn
sfpConfigXfpWlError = _SfpConfigXfpWlError_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 52),
    _SfpConfigXfpWlError_Type()
)
sfpConfigXfpWlError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigXfpWlError.setStatus("current")
_SfpConfigXfpDesiredFreq_Type = Integer32
_SfpConfigXfpDesiredFreq_Object = MibTableColumn
sfpConfigXfpDesiredFreq = _SfpConfigXfpDesiredFreq_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 53),
    _SfpConfigXfpDesiredFreq_Type()
)
sfpConfigXfpDesiredFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpConfigXfpDesiredFreq.setStatus("current")
_SfpConfigXfpFreqError_Type = Integer32
_SfpConfigXfpFreqError_Object = MibTableColumn
sfpConfigXfpFreqError = _SfpConfigXfpFreqError_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 54),
    _SfpConfigXfpFreqError_Type()
)
sfpConfigXfpFreqError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigXfpFreqError.setStatus("current")
_SfpConfigXfpDitherSupported_Type = TruthValue
_SfpConfigXfpDitherSupported_Object = MibTableColumn
sfpConfigXfpDitherSupported = _SfpConfigXfpDitherSupported_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 55),
    _SfpConfigXfpDitherSupported_Type()
)
sfpConfigXfpDitherSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigXfpDitherSupported.setStatus("current")


class _SfpConfigXfpDitherAdmin_Type(Integer32):
    """Custom type sfpConfigXfpDitherAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_SfpConfigXfpDitherAdmin_Type.__name__ = "Integer32"
_SfpConfigXfpDitherAdmin_Object = MibTableColumn
sfpConfigXfpDitherAdmin = _SfpConfigXfpDitherAdmin_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 56),
    _SfpConfigXfpDitherAdmin_Type()
)
sfpConfigXfpDitherAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpConfigXfpDitherAdmin.setStatus("current")
_SfpConfigXfpCapFreqFirstThz_Type = Integer32
_SfpConfigXfpCapFreqFirstThz_Object = MibTableColumn
sfpConfigXfpCapFreqFirstThz = _SfpConfigXfpCapFreqFirstThz_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 57),
    _SfpConfigXfpCapFreqFirstThz_Type()
)
sfpConfigXfpCapFreqFirstThz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigXfpCapFreqFirstThz.setStatus("current")
_SfpConfigXfpCapFreqFirst10Ghz_Type = Integer32
_SfpConfigXfpCapFreqFirst10Ghz_Object = MibTableColumn
sfpConfigXfpCapFreqFirst10Ghz = _SfpConfigXfpCapFreqFirst10Ghz_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 58),
    _SfpConfigXfpCapFreqFirst10Ghz_Type()
)
sfpConfigXfpCapFreqFirst10Ghz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigXfpCapFreqFirst10Ghz.setStatus("current")
_SfpConfigXfpCapFreqLastThz_Type = Integer32
_SfpConfigXfpCapFreqLastThz_Object = MibTableColumn
sfpConfigXfpCapFreqLastThz = _SfpConfigXfpCapFreqLastThz_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 59),
    _SfpConfigXfpCapFreqLastThz_Type()
)
sfpConfigXfpCapFreqLastThz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigXfpCapFreqLastThz.setStatus("current")
_SfpConfigXfpCapFreqLast10Ghz_Type = Integer32
_SfpConfigXfpCapFreqLast10Ghz_Object = MibTableColumn
sfpConfigXfpCapFreqLast10Ghz = _SfpConfigXfpCapFreqLast10Ghz_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 60),
    _SfpConfigXfpCapFreqLast10Ghz_Type()
)
sfpConfigXfpCapFreqLast10Ghz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigXfpCapFreqLast10Ghz.setStatus("current")
_SfpConfigXfpCapMaxSpacing10Ghz_Type = Integer32
_SfpConfigXfpCapMaxSpacing10Ghz_Object = MibTableColumn
sfpConfigXfpCapMaxSpacing10Ghz = _SfpConfigXfpCapMaxSpacing10Ghz_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 61),
    _SfpConfigXfpCapMaxSpacing10Ghz_Type()
)
sfpConfigXfpCapMaxSpacing10Ghz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigXfpCapMaxSpacing10Ghz.setStatus("current")
_SfpConfigXfpCalibrationSupported_Type = TruthValue
_SfpConfigXfpCalibrationSupported_Object = MibTableColumn
sfpConfigXfpCalibrationSupported = _SfpConfigXfpCalibrationSupported_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 62),
    _SfpConfigXfpCalibrationSupported_Type()
)
sfpConfigXfpCalibrationSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigXfpCalibrationSupported.setStatus("current")
_SfpConfigXfpCalibrationEnabled_Type = TruthValue
_SfpConfigXfpCalibrationEnabled_Object = MibTableColumn
sfpConfigXfpCalibrationEnabled = _SfpConfigXfpCalibrationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 63),
    _SfpConfigXfpCalibrationEnabled_Type()
)
sfpConfigXfpCalibrationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpConfigXfpCalibrationEnabled.setStatus("current")
_SfpConfigCfpExtId_Type = Integer32
_SfpConfigCfpExtId_Object = MibTableColumn
sfpConfigCfpExtId = _SfpConfigCfpExtId_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 70),
    _SfpConfigCfpExtId_Type()
)
sfpConfigCfpExtId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigCfpExtId.setStatus("current")
_SfpConfigCfpConnectorType_Type = Integer32
_SfpConfigCfpConnectorType_Object = MibTableColumn
sfpConfigCfpConnectorType = _SfpConfigCfpConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 71),
    _SfpConfigCfpConnectorType_Type()
)
sfpConfigCfpConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigCfpConnectorType.setStatus("current")
_SfpConfigCfpEthernetCode_Type = Integer32
_SfpConfigCfpEthernetCode_Object = MibTableColumn
sfpConfigCfpEthernetCode = _SfpConfigCfpEthernetCode_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 72),
    _SfpConfigCfpEthernetCode_Type()
)
sfpConfigCfpEthernetCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigCfpEthernetCode.setStatus("current")
_SfpConfigCfpFcCode_Type = Integer32
_SfpConfigCfpFcCode_Object = MibTableColumn
sfpConfigCfpFcCode = _SfpConfigCfpFcCode_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 73),
    _SfpConfigCfpFcCode_Type()
)
sfpConfigCfpFcCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigCfpFcCode.setStatus("current")
_SfpConfigCfpCopperCode_Type = Integer32
_SfpConfigCfpCopperCode_Object = MibTableColumn
sfpConfigCfpCopperCode = _SfpConfigCfpCopperCode_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 74),
    _SfpConfigCfpCopperCode_Type()
)
sfpConfigCfpCopperCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigCfpCopperCode.setStatus("current")
_SfpConfigCfpSonetCode_Type = Integer32
_SfpConfigCfpSonetCode_Object = MibTableColumn
sfpConfigCfpSonetCode = _SfpConfigCfpSonetCode_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 75),
    _SfpConfigCfpSonetCode_Type()
)
sfpConfigCfpSonetCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigCfpSonetCode.setStatus("current")
_SfpConfigCfpOtnCode_Type = Integer32
_SfpConfigCfpOtnCode_Object = MibTableColumn
sfpConfigCfpOtnCode = _SfpConfigCfpOtnCode_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 76),
    _SfpConfigCfpOtnCode_Type()
)
sfpConfigCfpOtnCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigCfpOtnCode.setStatus("current")
_SfpConfigCfpSupportedRates_Type = Integer32
_SfpConfigCfpSupportedRates_Object = MibTableColumn
sfpConfigCfpSupportedRates = _SfpConfigCfpSupportedRates_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 77),
    _SfpConfigCfpSupportedRates_Type()
)
sfpConfigCfpSupportedRates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigCfpSupportedRates.setStatus("current")
_SfpConfigCfpSupportedLanes_Type = Integer32
_SfpConfigCfpSupportedLanes_Object = MibTableColumn
sfpConfigCfpSupportedLanes = _SfpConfigCfpSupportedLanes_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 78),
    _SfpConfigCfpSupportedLanes_Type()
)
sfpConfigCfpSupportedLanes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigCfpSupportedLanes.setStatus("current")
_SfpConfigCfpMediaProperties_Type = Integer32
_SfpConfigCfpMediaProperties_Object = MibTableColumn
sfpConfigCfpMediaProperties = _SfpConfigCfpMediaProperties_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 79),
    _SfpConfigCfpMediaProperties_Type()
)
sfpConfigCfpMediaProperties.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigCfpMediaProperties.setStatus("current")
_SfpConfigCfpMaxNetworkLaneRate_Type = Integer32
_SfpConfigCfpMaxNetworkLaneRate_Object = MibTableColumn
sfpConfigCfpMaxNetworkLaneRate = _SfpConfigCfpMaxNetworkLaneRate_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 80),
    _SfpConfigCfpMaxNetworkLaneRate_Type()
)
sfpConfigCfpMaxNetworkLaneRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigCfpMaxNetworkLaneRate.setStatus("current")
_SfpConfigCfpMaxHostLaneRate_Type = Integer32
_SfpConfigCfpMaxHostLaneRate_Object = MibTableColumn
sfpConfigCfpMaxHostLaneRate = _SfpConfigCfpMaxHostLaneRate_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 81),
    _SfpConfigCfpMaxHostLaneRate_Type()
)
sfpConfigCfpMaxHostLaneRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigCfpMaxHostLaneRate.setStatus("current")
_SfpConfigCfpMaxSmFiberLength_Type = Integer32
_SfpConfigCfpMaxSmFiberLength_Object = MibTableColumn
sfpConfigCfpMaxSmFiberLength = _SfpConfigCfpMaxSmFiberLength_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 82),
    _SfpConfigCfpMaxSmFiberLength_Type()
)
sfpConfigCfpMaxSmFiberLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigCfpMaxSmFiberLength.setStatus("current")
_SfpConfigCfpMaxMmFiberLength_Type = Integer32
_SfpConfigCfpMaxMmFiberLength_Object = MibTableColumn
sfpConfigCfpMaxMmFiberLength = _SfpConfigCfpMaxMmFiberLength_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 83),
    _SfpConfigCfpMaxMmFiberLength_Type()
)
sfpConfigCfpMaxMmFiberLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigCfpMaxMmFiberLength.setStatus("current")
_SfpConfigCfpMaxCopperCableLength_Type = Integer32
_SfpConfigCfpMaxCopperCableLength_Object = MibTableColumn
sfpConfigCfpMaxCopperCableLength = _SfpConfigCfpMaxCopperCableLength_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 84),
    _SfpConfigCfpMaxCopperCableLength_Type()
)
sfpConfigCfpMaxCopperCableLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigCfpMaxCopperCableLength.setStatus("current")
_SfpConfigCfpMinWavelenPerActive_Type = Integer32
_SfpConfigCfpMinWavelenPerActive_Object = MibTableColumn
sfpConfigCfpMinWavelenPerActive = _SfpConfigCfpMinWavelenPerActive_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 85),
    _SfpConfigCfpMinWavelenPerActive_Type()
)
sfpConfigCfpMinWavelenPerActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigCfpMinWavelenPerActive.setStatus("current")
_SfpConfigCfpMaxWavelenPerActive_Type = Integer32
_SfpConfigCfpMaxWavelenPerActive_Object = MibTableColumn
sfpConfigCfpMaxWavelenPerActive = _SfpConfigCfpMaxWavelenPerActive_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 86),
    _SfpConfigCfpMaxWavelenPerActive_Type()
)
sfpConfigCfpMaxWavelenPerActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigCfpMaxWavelenPerActive.setStatus("current")
_SfpConfigCfpMaxLenOpticalWidth_Type = Integer32
_SfpConfigCfpMaxLenOpticalWidth_Object = MibTableColumn
sfpConfigCfpMaxLenOpticalWidth = _SfpConfigCfpMaxLenOpticalWidth_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 87),
    _SfpConfigCfpMaxLenOpticalWidth_Type()
)
sfpConfigCfpMaxLenOpticalWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigCfpMaxLenOpticalWidth.setStatus("current")
_SfpConfigCfpSpacing_Type = Integer32
_SfpConfigCfpSpacing_Object = MibTableColumn
sfpConfigCfpSpacing = _SfpConfigCfpSpacing_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 88),
    _SfpConfigCfpSpacing_Type()
)
sfpConfigCfpSpacing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpConfigCfpSpacing.setStatus("current")
_SfpConfigQsfppEthernetCode_Type = Integer32
_SfpConfigQsfppEthernetCode_Object = MibTableColumn
sfpConfigQsfppEthernetCode = _SfpConfigQsfppEthernetCode_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 100),
    _SfpConfigQsfppEthernetCode_Type()
)
sfpConfigQsfppEthernetCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigQsfppEthernetCode.setStatus("current")
_SfpConfigQsfppSonetCode_Type = Integer32
_SfpConfigQsfppSonetCode_Object = MibTableColumn
sfpConfigQsfppSonetCode = _SfpConfigQsfppSonetCode_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 101),
    _SfpConfigQsfppSonetCode_Type()
)
sfpConfigQsfppSonetCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpConfigQsfppSonetCode.setStatus("current")
_SfpConfigCxpExtId_Type = Integer32
_SfpConfigCxpExtId_Object = MibTableColumn
sfpConfigCxpExtId = _SfpConfigCxpExtId_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 110),
    _SfpConfigCxpExtId_Type()
)
sfpConfigCxpExtId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpConfigCxpExtId.setStatus("current")
_SfpConfigCxpConnectorType_Type = Integer32
_SfpConfigCxpConnectorType_Object = MibTableColumn
sfpConfigCxpConnectorType = _SfpConfigCxpConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 111),
    _SfpConfigCxpConnectorType_Type()
)
sfpConfigCxpConnectorType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpConfigCxpConnectorType.setStatus("current")
_SfpConfigCxpMaxSupportedRate_Type = Integer32
_SfpConfigCxpMaxSupportedRate_Object = MibTableColumn
sfpConfigCxpMaxSupportedRate = _SfpConfigCxpMaxSupportedRate_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 112),
    _SfpConfigCxpMaxSupportedRate_Type()
)
sfpConfigCxpMaxSupportedRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpConfigCxpMaxSupportedRate.setStatus("current")
_SfpConfigCxpNominalWavelength_Type = Integer32
_SfpConfigCxpNominalWavelength_Object = MibTableColumn
sfpConfigCxpNominalWavelength = _SfpConfigCxpNominalWavelength_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 113),
    _SfpConfigCxpNominalWavelength_Type()
)
sfpConfigCxpNominalWavelength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpConfigCxpNominalWavelength.setStatus("current")
_SfpConfigCxpDeviceTech_Type = Integer32
_SfpConfigCxpDeviceTech_Object = MibTableColumn
sfpConfigCxpDeviceTech = _SfpConfigCxpDeviceTech_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 114),
    _SfpConfigCxpDeviceTech_Type()
)
sfpConfigCxpDeviceTech.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpConfigCxpDeviceTech.setStatus("current")
_SfpConfigCohRxDesiredChannel_Type = Integer32
_SfpConfigCohRxDesiredChannel_Object = MibTableColumn
sfpConfigCohRxDesiredChannel = _SfpConfigCohRxDesiredChannel_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 115),
    _SfpConfigCohRxDesiredChannel_Type()
)
sfpConfigCohRxDesiredChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpConfigCohRxDesiredChannel.setStatus("current")
_SfpConfigCohRxDesiredWl_Type = Integer32
_SfpConfigCohRxDesiredWl_Object = MibTableColumn
sfpConfigCohRxDesiredWl = _SfpConfigCohRxDesiredWl_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 116),
    _SfpConfigCohRxDesiredWl_Type()
)
sfpConfigCohRxDesiredWl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpConfigCohRxDesiredWl.setStatus("current")
_SfpConfigCohRxDesiredFreq_Type = Integer32
_SfpConfigCohRxDesiredFreq_Object = MibTableColumn
sfpConfigCohRxDesiredFreq = _SfpConfigCohRxDesiredFreq_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 117),
    _SfpConfigCohRxDesiredFreq_Type()
)
sfpConfigCohRxDesiredFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpConfigCohRxDesiredFreq.setStatus("current")
_SfpConfigCohCurrentCD_Type = Integer32
_SfpConfigCohCurrentCD_Object = MibTableColumn
sfpConfigCohCurrentCD = _SfpConfigCohCurrentCD_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 118),
    _SfpConfigCohCurrentCD_Type()
)
sfpConfigCohCurrentCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigCohCurrentCD.setStatus("current")
_SfpConfigCohCurrentOSNR_Type = Integer32
_SfpConfigCohCurrentOSNR_Object = MibTableColumn
sfpConfigCohCurrentOSNR = _SfpConfigCohCurrentOSNR_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 119),
    _SfpConfigCohCurrentOSNR_Type()
)
sfpConfigCohCurrentOSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigCohCurrentOSNR.setStatus("current")
_SfpConfigCohAverageOSNR_Type = Integer32
_SfpConfigCohAverageOSNR_Object = MibTableColumn
sfpConfigCohAverageOSNR = _SfpConfigCohAverageOSNR_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 120),
    _SfpConfigCohAverageOSNR_Type()
)
sfpConfigCohAverageOSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigCohAverageOSNR.setStatus("current")
_SfpConfigCohMaxCD_Type = Integer32
_SfpConfigCohMaxCD_Object = MibTableColumn
sfpConfigCohMaxCD = _SfpConfigCohMaxCD_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 121),
    _SfpConfigCohMaxCD_Type()
)
sfpConfigCohMaxCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConfigCohMaxCD.setStatus("current")
_SfpConfigNyquist_Type = TruthValue
_SfpConfigNyquist_Object = MibTableColumn
sfpConfigNyquist = _SfpConfigNyquist_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 1, 1, 1, 122),
    _SfpConfigNyquist_Type()
)
sfpConfigNyquist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpConfigNyquist.setStatus("current")
_SfpDiag_ObjectIdentity = ObjectIdentity
sfpDiag = _SfpDiag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 2)
)
_SfpDiagTable_Object = MibTable
sfpDiagTable = _SfpDiagTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 2, 1)
)
if mibBuilder.loadTexts:
    sfpDiagTable.setStatus("current")
_SfpDiagEntry_Object = MibTableRow
sfpDiagEntry = _SfpDiagEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 2, 1, 1)
)
sfpDiagEntry.setIndexNames(
    (0, "SL-SFP-MIB", "sfpDiagInterface"),
)
if mibBuilder.loadTexts:
    sfpDiagEntry.setStatus("current")
_SfpDiagInterface_Type = InterfaceIndex
_SfpDiagInterface_Object = MibTableColumn
sfpDiagInterface = _SfpDiagInterface_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 2, 1, 1, 1),
    _SfpDiagInterface_Type()
)
sfpDiagInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDiagInterface.setStatus("current")


class _SfpDiagHighTempAlmThreshold_Type(Integer32):
    """Custom type sfpDiagHighTempAlmThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SfpDiagHighTempAlmThreshold_Type.__name__ = "Integer32"
_SfpDiagHighTempAlmThreshold_Object = MibTableColumn
sfpDiagHighTempAlmThreshold = _SfpDiagHighTempAlmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 2, 1, 1, 2),
    _SfpDiagHighTempAlmThreshold_Type()
)
sfpDiagHighTempAlmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDiagHighTempAlmThreshold.setStatus("current")


class _SfpDiagLowTempAlmThreshold_Type(Integer32):
    """Custom type sfpDiagLowTempAlmThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SfpDiagLowTempAlmThreshold_Type.__name__ = "Integer32"
_SfpDiagLowTempAlmThreshold_Object = MibTableColumn
sfpDiagLowTempAlmThreshold = _SfpDiagLowTempAlmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 2, 1, 1, 3),
    _SfpDiagLowTempAlmThreshold_Type()
)
sfpDiagLowTempAlmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDiagLowTempAlmThreshold.setStatus("current")


class _SfpDiagHighTempWrnThreshold_Type(Integer32):
    """Custom type sfpDiagHighTempWrnThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SfpDiagHighTempWrnThreshold_Type.__name__ = "Integer32"
_SfpDiagHighTempWrnThreshold_Object = MibTableColumn
sfpDiagHighTempWrnThreshold = _SfpDiagHighTempWrnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 2, 1, 1, 4),
    _SfpDiagHighTempWrnThreshold_Type()
)
sfpDiagHighTempWrnThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDiagHighTempWrnThreshold.setStatus("current")


class _SfpDiagLowTempWrnThreshold_Type(Integer32):
    """Custom type sfpDiagLowTempWrnThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SfpDiagLowTempWrnThreshold_Type.__name__ = "Integer32"
_SfpDiagLowTempWrnThreshold_Object = MibTableColumn
sfpDiagLowTempWrnThreshold = _SfpDiagLowTempWrnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 2, 1, 1, 5),
    _SfpDiagLowTempWrnThreshold_Type()
)
sfpDiagLowTempWrnThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDiagLowTempWrnThreshold.setStatus("current")


class _SfpDiagHighVoltAlmThreshold_Type(Integer32):
    """Custom type sfpDiagHighVoltAlmThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SfpDiagHighVoltAlmThreshold_Type.__name__ = "Integer32"
_SfpDiagHighVoltAlmThreshold_Object = MibTableColumn
sfpDiagHighVoltAlmThreshold = _SfpDiagHighVoltAlmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 2, 1, 1, 6),
    _SfpDiagHighVoltAlmThreshold_Type()
)
sfpDiagHighVoltAlmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDiagHighVoltAlmThreshold.setStatus("current")


class _SfpDiagLowVoltAlmThreshold_Type(Integer32):
    """Custom type sfpDiagLowVoltAlmThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SfpDiagLowVoltAlmThreshold_Type.__name__ = "Integer32"
_SfpDiagLowVoltAlmThreshold_Object = MibTableColumn
sfpDiagLowVoltAlmThreshold = _SfpDiagLowVoltAlmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 2, 1, 1, 7),
    _SfpDiagLowVoltAlmThreshold_Type()
)
sfpDiagLowVoltAlmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDiagLowVoltAlmThreshold.setStatus("current")


class _SfpDiagHighVoltWrnThreshold_Type(Integer32):
    """Custom type sfpDiagHighVoltWrnThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SfpDiagHighVoltWrnThreshold_Type.__name__ = "Integer32"
_SfpDiagHighVoltWrnThreshold_Object = MibTableColumn
sfpDiagHighVoltWrnThreshold = _SfpDiagHighVoltWrnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 2, 1, 1, 8),
    _SfpDiagHighVoltWrnThreshold_Type()
)
sfpDiagHighVoltWrnThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDiagHighVoltWrnThreshold.setStatus("current")


class _SfpDiagLowVoltWrnThreshold_Type(Integer32):
    """Custom type sfpDiagLowVoltWrnThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SfpDiagLowVoltWrnThreshold_Type.__name__ = "Integer32"
_SfpDiagLowVoltWrnThreshold_Object = MibTableColumn
sfpDiagLowVoltWrnThreshold = _SfpDiagLowVoltWrnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 2, 1, 1, 9),
    _SfpDiagLowVoltWrnThreshold_Type()
)
sfpDiagLowVoltWrnThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDiagLowVoltWrnThreshold.setStatus("current")


class _SfpDiagHighTxBiasAlmThreshold_Type(Integer32):
    """Custom type sfpDiagHighTxBiasAlmThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SfpDiagHighTxBiasAlmThreshold_Type.__name__ = "Integer32"
_SfpDiagHighTxBiasAlmThreshold_Object = MibTableColumn
sfpDiagHighTxBiasAlmThreshold = _SfpDiagHighTxBiasAlmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 2, 1, 1, 10),
    _SfpDiagHighTxBiasAlmThreshold_Type()
)
sfpDiagHighTxBiasAlmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDiagHighTxBiasAlmThreshold.setStatus("current")


class _SfpDiagLowTxBiasAlmThreshold_Type(Integer32):
    """Custom type sfpDiagLowTxBiasAlmThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SfpDiagLowTxBiasAlmThreshold_Type.__name__ = "Integer32"
_SfpDiagLowTxBiasAlmThreshold_Object = MibTableColumn
sfpDiagLowTxBiasAlmThreshold = _SfpDiagLowTxBiasAlmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 2, 1, 1, 11),
    _SfpDiagLowTxBiasAlmThreshold_Type()
)
sfpDiagLowTxBiasAlmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDiagLowTxBiasAlmThreshold.setStatus("current")


class _SfpDiagHighTxBiasWrnThreshold_Type(Integer32):
    """Custom type sfpDiagHighTxBiasWrnThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SfpDiagHighTxBiasWrnThreshold_Type.__name__ = "Integer32"
_SfpDiagHighTxBiasWrnThreshold_Object = MibTableColumn
sfpDiagHighTxBiasWrnThreshold = _SfpDiagHighTxBiasWrnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 2, 1, 1, 12),
    _SfpDiagHighTxBiasWrnThreshold_Type()
)
sfpDiagHighTxBiasWrnThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDiagHighTxBiasWrnThreshold.setStatus("current")


class _SfpDiagLowTxBiasWrnThreshold_Type(Integer32):
    """Custom type sfpDiagLowTxBiasWrnThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SfpDiagLowTxBiasWrnThreshold_Type.__name__ = "Integer32"
_SfpDiagLowTxBiasWrnThreshold_Object = MibTableColumn
sfpDiagLowTxBiasWrnThreshold = _SfpDiagLowTxBiasWrnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 2, 1, 1, 13),
    _SfpDiagLowTxBiasWrnThreshold_Type()
)
sfpDiagLowTxBiasWrnThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDiagLowTxBiasWrnThreshold.setStatus("current")


class _SfpDiagHighTxPowerAlmThreshold_Type(Integer32):
    """Custom type sfpDiagHighTxPowerAlmThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SfpDiagHighTxPowerAlmThreshold_Type.__name__ = "Integer32"
_SfpDiagHighTxPowerAlmThreshold_Object = MibTableColumn
sfpDiagHighTxPowerAlmThreshold = _SfpDiagHighTxPowerAlmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 2, 1, 1, 14),
    _SfpDiagHighTxPowerAlmThreshold_Type()
)
sfpDiagHighTxPowerAlmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDiagHighTxPowerAlmThreshold.setStatus("current")


class _SfpDiagLowTxPowerAlmThreshold_Type(Integer32):
    """Custom type sfpDiagLowTxPowerAlmThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SfpDiagLowTxPowerAlmThreshold_Type.__name__ = "Integer32"
_SfpDiagLowTxPowerAlmThreshold_Object = MibTableColumn
sfpDiagLowTxPowerAlmThreshold = _SfpDiagLowTxPowerAlmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 2, 1, 1, 15),
    _SfpDiagLowTxPowerAlmThreshold_Type()
)
sfpDiagLowTxPowerAlmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDiagLowTxPowerAlmThreshold.setStatus("current")


class _SfpDiagHighTxPowerWrnThreshold_Type(Integer32):
    """Custom type sfpDiagHighTxPowerWrnThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SfpDiagHighTxPowerWrnThreshold_Type.__name__ = "Integer32"
_SfpDiagHighTxPowerWrnThreshold_Object = MibTableColumn
sfpDiagHighTxPowerWrnThreshold = _SfpDiagHighTxPowerWrnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 2, 1, 1, 16),
    _SfpDiagHighTxPowerWrnThreshold_Type()
)
sfpDiagHighTxPowerWrnThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDiagHighTxPowerWrnThreshold.setStatus("current")


class _SfpDiagLowTxPowerWrnThreshold_Type(Integer32):
    """Custom type sfpDiagLowTxPowerWrnThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SfpDiagLowTxPowerWrnThreshold_Type.__name__ = "Integer32"
_SfpDiagLowTxPowerWrnThreshold_Object = MibTableColumn
sfpDiagLowTxPowerWrnThreshold = _SfpDiagLowTxPowerWrnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 2, 1, 1, 17),
    _SfpDiagLowTxPowerWrnThreshold_Type()
)
sfpDiagLowTxPowerWrnThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDiagLowTxPowerWrnThreshold.setStatus("current")


class _SfpDiagHighRxPowerAlmThreshold_Type(Integer32):
    """Custom type sfpDiagHighRxPowerAlmThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SfpDiagHighRxPowerAlmThreshold_Type.__name__ = "Integer32"
_SfpDiagHighRxPowerAlmThreshold_Object = MibTableColumn
sfpDiagHighRxPowerAlmThreshold = _SfpDiagHighRxPowerAlmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 2, 1, 1, 18),
    _SfpDiagHighRxPowerAlmThreshold_Type()
)
sfpDiagHighRxPowerAlmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDiagHighRxPowerAlmThreshold.setStatus("current")


class _SfpDiagLowRxPowerAlmThreshold_Type(Integer32):
    """Custom type sfpDiagLowRxPowerAlmThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SfpDiagLowRxPowerAlmThreshold_Type.__name__ = "Integer32"
_SfpDiagLowRxPowerAlmThreshold_Object = MibTableColumn
sfpDiagLowRxPowerAlmThreshold = _SfpDiagLowRxPowerAlmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 2, 1, 1, 19),
    _SfpDiagLowRxPowerAlmThreshold_Type()
)
sfpDiagLowRxPowerAlmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDiagLowRxPowerAlmThreshold.setStatus("current")


class _SfpDiagHighRxPowerWrnThreshold_Type(Integer32):
    """Custom type sfpDiagHighRxPowerWrnThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SfpDiagHighRxPowerWrnThreshold_Type.__name__ = "Integer32"
_SfpDiagHighRxPowerWrnThreshold_Object = MibTableColumn
sfpDiagHighRxPowerWrnThreshold = _SfpDiagHighRxPowerWrnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 2, 1, 1, 20),
    _SfpDiagHighRxPowerWrnThreshold_Type()
)
sfpDiagHighRxPowerWrnThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDiagHighRxPowerWrnThreshold.setStatus("current")


class _SfpDiagLowRxPowerWrnThreshold_Type(Integer32):
    """Custom type sfpDiagLowRxPowerWrnThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SfpDiagLowRxPowerWrnThreshold_Type.__name__ = "Integer32"
_SfpDiagLowRxPowerWrnThreshold_Object = MibTableColumn
sfpDiagLowRxPowerWrnThreshold = _SfpDiagLowRxPowerWrnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 2, 1, 1, 21),
    _SfpDiagLowRxPowerWrnThreshold_Type()
)
sfpDiagLowRxPowerWrnThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDiagLowRxPowerWrnThreshold.setStatus("current")


class _SfpDiagHighLaserTempAlmThreshold_Type(Integer32):
    """Custom type sfpDiagHighLaserTempAlmThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SfpDiagHighLaserTempAlmThreshold_Type.__name__ = "Integer32"
_SfpDiagHighLaserTempAlmThreshold_Object = MibTableColumn
sfpDiagHighLaserTempAlmThreshold = _SfpDiagHighLaserTempAlmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 2, 1, 1, 22),
    _SfpDiagHighLaserTempAlmThreshold_Type()
)
sfpDiagHighLaserTempAlmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDiagHighLaserTempAlmThreshold.setStatus("current")


class _SfpDiagLowLaserTempAlmThreshold_Type(Integer32):
    """Custom type sfpDiagLowLaserTempAlmThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SfpDiagLowLaserTempAlmThreshold_Type.__name__ = "Integer32"
_SfpDiagLowLaserTempAlmThreshold_Object = MibTableColumn
sfpDiagLowLaserTempAlmThreshold = _SfpDiagLowLaserTempAlmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 2, 1, 1, 23),
    _SfpDiagLowLaserTempAlmThreshold_Type()
)
sfpDiagLowLaserTempAlmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDiagLowLaserTempAlmThreshold.setStatus("current")


class _SfpDiagHighLaserTempWrnThreshold_Type(Integer32):
    """Custom type sfpDiagHighLaserTempWrnThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SfpDiagHighLaserTempWrnThreshold_Type.__name__ = "Integer32"
_SfpDiagHighLaserTempWrnThreshold_Object = MibTableColumn
sfpDiagHighLaserTempWrnThreshold = _SfpDiagHighLaserTempWrnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 2, 1, 1, 24),
    _SfpDiagHighLaserTempWrnThreshold_Type()
)
sfpDiagHighLaserTempWrnThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDiagHighLaserTempWrnThreshold.setStatus("current")


class _SfpDiagLowLaserTempWrnThreshold_Type(Integer32):
    """Custom type sfpDiagLowLaserTempWrnThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SfpDiagLowLaserTempWrnThreshold_Type.__name__ = "Integer32"
_SfpDiagLowLaserTempWrnThreshold_Object = MibTableColumn
sfpDiagLowLaserTempWrnThreshold = _SfpDiagLowLaserTempWrnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 2, 1, 1, 25),
    _SfpDiagLowLaserTempWrnThreshold_Type()
)
sfpDiagLowLaserTempWrnThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDiagLowLaserTempWrnThreshold.setStatus("current")


class _SfpDiagHighWaveLenAlmThreshold_Type(Integer32):
    """Custom type sfpDiagHighWaveLenAlmThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SfpDiagHighWaveLenAlmThreshold_Type.__name__ = "Integer32"
_SfpDiagHighWaveLenAlmThreshold_Object = MibTableColumn
sfpDiagHighWaveLenAlmThreshold = _SfpDiagHighWaveLenAlmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 2, 1, 1, 26),
    _SfpDiagHighWaveLenAlmThreshold_Type()
)
sfpDiagHighWaveLenAlmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDiagHighWaveLenAlmThreshold.setStatus("current")


class _SfpDiagLowWaveLenAlmThreshold_Type(Integer32):
    """Custom type sfpDiagLowWaveLenAlmThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SfpDiagLowWaveLenAlmThreshold_Type.__name__ = "Integer32"
_SfpDiagLowWaveLenAlmThreshold_Object = MibTableColumn
sfpDiagLowWaveLenAlmThreshold = _SfpDiagLowWaveLenAlmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 2, 1, 1, 27),
    _SfpDiagLowWaveLenAlmThreshold_Type()
)
sfpDiagLowWaveLenAlmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDiagLowWaveLenAlmThreshold.setStatus("current")


class _SfpDiagHighWaveLenWrnThreshold_Type(Integer32):
    """Custom type sfpDiagHighWaveLenWrnThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SfpDiagHighWaveLenWrnThreshold_Type.__name__ = "Integer32"
_SfpDiagHighWaveLenWrnThreshold_Object = MibTableColumn
sfpDiagHighWaveLenWrnThreshold = _SfpDiagHighWaveLenWrnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 2, 1, 1, 28),
    _SfpDiagHighWaveLenWrnThreshold_Type()
)
sfpDiagHighWaveLenWrnThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDiagHighWaveLenWrnThreshold.setStatus("current")


class _SfpDiagLowWaveLenWrnThreshold_Type(Integer32):
    """Custom type sfpDiagLowWaveLenWrnThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SfpDiagLowWaveLenWrnThreshold_Type.__name__ = "Integer32"
_SfpDiagLowWaveLenWrnThreshold_Object = MibTableColumn
sfpDiagLowWaveLenWrnThreshold = _SfpDiagLowWaveLenWrnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 2, 1, 1, 29),
    _SfpDiagLowWaveLenWrnThreshold_Type()
)
sfpDiagLowWaveLenWrnThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDiagLowWaveLenWrnThreshold.setStatus("current")


class _SfpDiagHighTecCurrAlmThreshold_Type(Integer32):
    """Custom type sfpDiagHighTecCurrAlmThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SfpDiagHighTecCurrAlmThreshold_Type.__name__ = "Integer32"
_SfpDiagHighTecCurrAlmThreshold_Object = MibTableColumn
sfpDiagHighTecCurrAlmThreshold = _SfpDiagHighTecCurrAlmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 2, 1, 1, 30),
    _SfpDiagHighTecCurrAlmThreshold_Type()
)
sfpDiagHighTecCurrAlmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDiagHighTecCurrAlmThreshold.setStatus("current")


class _SfpDiagLowTecCurrAlmThreshold_Type(Integer32):
    """Custom type sfpDiagLowTecCurrAlmThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SfpDiagLowTecCurrAlmThreshold_Type.__name__ = "Integer32"
_SfpDiagLowTecCurrAlmThreshold_Object = MibTableColumn
sfpDiagLowTecCurrAlmThreshold = _SfpDiagLowTecCurrAlmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 2, 1, 1, 31),
    _SfpDiagLowTecCurrAlmThreshold_Type()
)
sfpDiagLowTecCurrAlmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDiagLowTecCurrAlmThreshold.setStatus("current")


class _SfpDiagHighTecCurrWrnThreshold_Type(Integer32):
    """Custom type sfpDiagHighTecCurrWrnThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SfpDiagHighTecCurrWrnThreshold_Type.__name__ = "Integer32"
_SfpDiagHighTecCurrWrnThreshold_Object = MibTableColumn
sfpDiagHighTecCurrWrnThreshold = _SfpDiagHighTecCurrWrnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 2, 1, 1, 32),
    _SfpDiagHighTecCurrWrnThreshold_Type()
)
sfpDiagHighTecCurrWrnThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDiagHighTecCurrWrnThreshold.setStatus("current")


class _SfpDiagLowTecCurrWrnThreshold_Type(Integer32):
    """Custom type sfpDiagLowTecCurrWrnThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SfpDiagLowTecCurrWrnThreshold_Type.__name__ = "Integer32"
_SfpDiagLowTecCurrWrnThreshold_Object = MibTableColumn
sfpDiagLowTecCurrWrnThreshold = _SfpDiagLowTecCurrWrnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 2, 1, 1, 33),
    _SfpDiagLowTecCurrWrnThreshold_Type()
)
sfpDiagLowTecCurrWrnThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDiagLowTecCurrWrnThreshold.setStatus("current")


class _SfpDiagModuleTemperature_Type(Integer32):
    """Custom type sfpDiagModuleTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SfpDiagModuleTemperature_Type.__name__ = "Integer32"
_SfpDiagModuleTemperature_Object = MibTableColumn
sfpDiagModuleTemperature = _SfpDiagModuleTemperature_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 2, 1, 1, 34),
    _SfpDiagModuleTemperature_Type()
)
sfpDiagModuleTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDiagModuleTemperature.setStatus("current")


class _SfpDiagSupplyVoltage_Type(Integer32):
    """Custom type sfpDiagSupplyVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SfpDiagSupplyVoltage_Type.__name__ = "Integer32"
_SfpDiagSupplyVoltage_Object = MibTableColumn
sfpDiagSupplyVoltage = _SfpDiagSupplyVoltage_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 2, 1, 1, 35),
    _SfpDiagSupplyVoltage_Type()
)
sfpDiagSupplyVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDiagSupplyVoltage.setStatus("current")


class _SfpDiagTxBias_Type(Integer32):
    """Custom type sfpDiagTxBias based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SfpDiagTxBias_Type.__name__ = "Integer32"
_SfpDiagTxBias_Object = MibTableColumn
sfpDiagTxBias = _SfpDiagTxBias_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 2, 1, 1, 36),
    _SfpDiagTxBias_Type()
)
sfpDiagTxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDiagTxBias.setStatus("current")


class _SfpDiagTxOutputPower_Type(Integer32):
    """Custom type sfpDiagTxOutputPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SfpDiagTxOutputPower_Type.__name__ = "Integer32"
_SfpDiagTxOutputPower_Object = MibTableColumn
sfpDiagTxOutputPower = _SfpDiagTxOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 2, 1, 1, 37),
    _SfpDiagTxOutputPower_Type()
)
sfpDiagTxOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDiagTxOutputPower.setStatus("current")


class _SfpDiagRxInputPower_Type(Integer32):
    """Custom type sfpDiagRxInputPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SfpDiagRxInputPower_Type.__name__ = "Integer32"
_SfpDiagRxInputPower_Object = MibTableColumn
sfpDiagRxInputPower = _SfpDiagRxInputPower_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 2, 1, 1, 38),
    _SfpDiagRxInputPower_Type()
)
sfpDiagRxInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDiagRxInputPower.setStatus("current")


class _SfpDiagRxLaserTemperature_Type(Integer32):
    """Custom type sfpDiagRxLaserTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SfpDiagRxLaserTemperature_Type.__name__ = "Integer32"
_SfpDiagRxLaserTemperature_Object = MibTableColumn
sfpDiagRxLaserTemperature = _SfpDiagRxLaserTemperature_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 2, 1, 1, 39),
    _SfpDiagRxLaserTemperature_Type()
)
sfpDiagRxLaserTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDiagRxLaserTemperature.setStatus("current")


class _SfpDiagRxMeasuredWavelength_Type(Integer32):
    """Custom type sfpDiagRxMeasuredWavelength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SfpDiagRxMeasuredWavelength_Type.__name__ = "Integer32"
_SfpDiagRxMeasuredWavelength_Object = MibTableColumn
sfpDiagRxMeasuredWavelength = _SfpDiagRxMeasuredWavelength_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 2, 1, 1, 40),
    _SfpDiagRxMeasuredWavelength_Type()
)
sfpDiagRxMeasuredWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDiagRxMeasuredWavelength.setStatus("current")


class _SfpDiagRxTecCurrent_Type(Integer32):
    """Custom type sfpDiagRxTecCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SfpDiagRxTecCurrent_Type.__name__ = "Integer32"
_SfpDiagRxTecCurrent_Object = MibTableColumn
sfpDiagRxTecCurrent = _SfpDiagRxTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 2, 1, 1, 41),
    _SfpDiagRxTecCurrent_Type()
)
sfpDiagRxTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDiagRxTecCurrent.setStatus("current")
_SfpDiagAlarms_Type = Integer32
_SfpDiagAlarms_Object = MibTableColumn
sfpDiagAlarms = _SfpDiagAlarms_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 2, 1, 1, 42),
    _SfpDiagAlarms_Type()
)
sfpDiagAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDiagAlarms.setStatus("current")
_SfpDiagAlarmsMask_Type = Integer32
_SfpDiagAlarmsMask_Object = MibTableColumn
sfpDiagAlarmsMask = _SfpDiagAlarmsMask_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 2, 1, 1, 43),
    _SfpDiagAlarmsMask_Type()
)
sfpDiagAlarmsMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDiagAlarmsMask.setStatus("current")
_SfpDiagWarnings_Type = Integer32
_SfpDiagWarnings_Object = MibTableColumn
sfpDiagWarnings = _SfpDiagWarnings_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 2, 1, 1, 44),
    _SfpDiagWarnings_Type()
)
sfpDiagWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDiagWarnings.setStatus("current")
_SfpDiagWarningsMask_Type = Integer32
_SfpDiagWarningsMask_Object = MibTableColumn
sfpDiagWarningsMask = _SfpDiagWarningsMask_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 2, 1, 1, 45),
    _SfpDiagWarningsMask_Type()
)
sfpDiagWarningsMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDiagWarningsMask.setStatus("current")
_SfpDiagConfLowRxPowerAlmThreshold_Type = Integer32
_SfpDiagConfLowRxPowerAlmThreshold_Object = MibTableColumn
sfpDiagConfLowRxPowerAlmThreshold = _SfpDiagConfLowRxPowerAlmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 2, 1, 1, 46),
    _SfpDiagConfLowRxPowerAlmThreshold_Type()
)
sfpDiagConfLowRxPowerAlmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpDiagConfLowRxPowerAlmThreshold.setStatus("current")
_SfpDiagRxInputPowerFloat_Type = Float32TC
_SfpDiagRxInputPowerFloat_Object = MibTableColumn
sfpDiagRxInputPowerFloat = _SfpDiagRxInputPowerFloat_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 2, 1, 1, 47),
    _SfpDiagRxInputPowerFloat_Type()
)
sfpDiagRxInputPowerFloat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDiagRxInputPowerFloat.setStatus("current")
_SfpDiagCxpTxTemp_Type = Integer32
_SfpDiagCxpTxTemp_Object = MibTableColumn
sfpDiagCxpTxTemp = _SfpDiagCxpTxTemp_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 2, 1, 1, 50),
    _SfpDiagCxpTxTemp_Type()
)
sfpDiagCxpTxTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDiagCxpTxTemp.setStatus("current")
_SfpDiagCxpHighTxTempAlmThreshold_Type = Integer32
_SfpDiagCxpHighTxTempAlmThreshold_Object = MibTableColumn
sfpDiagCxpHighTxTempAlmThreshold = _SfpDiagCxpHighTxTempAlmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 2, 1, 1, 51),
    _SfpDiagCxpHighTxTempAlmThreshold_Type()
)
sfpDiagCxpHighTxTempAlmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDiagCxpHighTxTempAlmThreshold.setStatus("current")
_SfpDiagCxpLowTxTempAlmThreshold_Type = Integer32
_SfpDiagCxpLowTxTempAlmThreshold_Object = MibTableColumn
sfpDiagCxpLowTxTempAlmThreshold = _SfpDiagCxpLowTxTempAlmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 2, 1, 1, 52),
    _SfpDiagCxpLowTxTempAlmThreshold_Type()
)
sfpDiagCxpLowTxTempAlmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDiagCxpLowTxTempAlmThreshold.setStatus("current")
_SfpDiagCxpRxTemp_Type = Integer32
_SfpDiagCxpRxTemp_Object = MibTableColumn
sfpDiagCxpRxTemp = _SfpDiagCxpRxTemp_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 2, 1, 1, 53),
    _SfpDiagCxpRxTemp_Type()
)
sfpDiagCxpRxTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDiagCxpRxTemp.setStatus("current")
_SfpDiagCxpHighRxTempAlmThreshold_Type = Integer32
_SfpDiagCxpHighRxTempAlmThreshold_Object = MibTableColumn
sfpDiagCxpHighRxTempAlmThreshold = _SfpDiagCxpHighRxTempAlmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 2, 1, 1, 54),
    _SfpDiagCxpHighRxTempAlmThreshold_Type()
)
sfpDiagCxpHighRxTempAlmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDiagCxpHighRxTempAlmThreshold.setStatus("current")
_SfpDiagCxpLowRxTempAlmThreshold_Type = Integer32
_SfpDiagCxpLowRxTempAlmThreshold_Object = MibTableColumn
sfpDiagCxpLowRxTempAlmThreshold = _SfpDiagCxpLowRxTempAlmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 2, 1, 1, 55),
    _SfpDiagCxpLowRxTempAlmThreshold_Type()
)
sfpDiagCxpLowRxTempAlmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDiagCxpLowRxTempAlmThreshold.setStatus("current")
_SfpDiagOtdrFiberCutRange_Type = Integer32
_SfpDiagOtdrFiberCutRange_Object = MibTableColumn
sfpDiagOtdrFiberCutRange = _SfpDiagOtdrFiberCutRange_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 2, 1, 1, 56),
    _SfpDiagOtdrFiberCutRange_Type()
)
sfpDiagOtdrFiberCutRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDiagOtdrFiberCutRange.setStatus("current")
_SfpDiagModuleTemperatureCelsius_Type = Integer32
_SfpDiagModuleTemperatureCelsius_Object = MibTableColumn
sfpDiagModuleTemperatureCelsius = _SfpDiagModuleTemperatureCelsius_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 2, 1, 1, 57),
    _SfpDiagModuleTemperatureCelsius_Type()
)
sfpDiagModuleTemperatureCelsius.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDiagModuleTemperatureCelsius.setStatus("current")
_SfpTraps_ObjectIdentity = ObjectIdentity
sfpTraps = _SfpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 3)
)
_SfpTune_ObjectIdentity = ObjectIdentity
sfpTune = _SfpTune_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 4)
)

# Managed Objects groups


# Notification objects

sfpConfigChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 1, 10, 3, 1)
)
sfpConfigChangeTrap.setObjects(
    ("SL-SFP-MIB", "sfpConfigInterface")
)
if mibBuilder.loadTexts:
    sfpConfigChangeTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SL-SFP-MIB",
    **{"slSfp": slSfp,
       "sfpConf": sfpConf,
       "sfpConfigTable": sfpConfigTable,
       "sfpConfigEntry": sfpConfigEntry,
       "sfpConfigInterface": sfpConfigInterface,
       "sfpConfigXcvrId": sfpConfigXcvrId,
       "sfpConfig1310ExtXcvrId": sfpConfig1310ExtXcvrId,
       "sfpConfigWdmExtXcvrId": sfpConfigWdmExtXcvrId,
       "sfpConfigConnectorCode": sfpConfigConnectorCode,
       "sfpConfigInfibandCompliance": sfpConfigInfibandCompliance,
       "sfpConfigEsconCompliance": sfpConfigEsconCompliance,
       "sfpConfigSonetCompliance": sfpConfigSonetCompliance,
       "sfpConfigGbeCompliance": sfpConfigGbeCompliance,
       "sfpConfigFcCompliance": sfpConfigFcCompliance,
       "sfpConfigEncodingCode": sfpConfigEncodingCode,
       "sfpConfigNominalBitRate": sfpConfigNominalBitRate,
       "sfpConfigLength9mKm": sfpConfigLength9mKm,
       "sfpConfigLength9m100m": sfpConfigLength9m100m,
       "sfpConfigLength50m10m": sfpConfigLength50m10m,
       "sfpConfigLength62m10m": sfpConfigLength62m10m,
       "sfpConfigLengthCopper1m": sfpConfigLengthCopper1m,
       "sfpConfigMaxTemp": sfpConfigMaxTemp,
       "sfpConfigMinTemp": sfpConfigMinTemp,
       "sfpConfigMaxSupplyCurrent": sfpConfigMaxSupplyCurrent,
       "sfpConfigChannelSpacing": sfpConfigChannelSpacing,
       "sfpConfigVendorName": sfpConfigVendorName,
       "sfpConfigOptionalWdm": sfpConfigOptionalWdm,
       "sfpConfigVendorOUI": sfpConfigVendorOUI,
       "sfpConfigVendorPN": sfpConfigVendorPN,
       "sfpConfigVendorRev": sfpConfigVendorRev,
       "sfpConfigWaveLength": sfpConfigWaveLength,
       "sfpConfigExtendedOptions": sfpConfigExtendedOptions,
       "sfpConfigMaxBitRate": sfpConfigMaxBitRate,
       "sfpConfigMinBitRate": sfpConfigMinBitRate,
       "sfpConfigVendorSN": sfpConfigVendorSN,
       "sfpConfigDateCode": sfpConfigDateCode,
       "sfpConfigDiagnosticMonitoring": sfpConfigDiagnosticMonitoring,
       "sfpConfigEnhanceOptions": sfpConfigEnhanceOptions,
       "sfpConfig8472Compliance": sfpConfig8472Compliance,
       "sfpConfigTunableWaveLength": sfpConfigTunableWaveLength,
       "sfpConfigVoaControl": sfpConfigVoaControl,
       "sfpConfigVdtControl": sfpConfigVdtControl,
       "sfpConfigPilotToneModulation": sfpConfigPilotToneModulation,
       "sfpConfigCleiCode": sfpConfigCleiCode,
       "sfpConfigXfpExtXcvrId": sfpConfigXfpExtXcvrId,
       "sfpConfigXfpEncodingCode": sfpConfigXfpEncodingCode,
       "sfpConfigXfpMinBitRate": sfpConfigXfpMinBitRate,
       "sfpConfigXfpMaxBitRate": sfpConfigXfpMaxBitRate,
       "sfpConfig10GSonetCompliance": sfpConfig10GSonetCompliance,
       "sfpConfig10GbeCompliance": sfpConfig10GbeCompliance,
       "sfpConfig10GFcCompliance": sfpConfig10GFcCompliance,
       "sfpConfigXfpDeviceTech": sfpConfigXfpDeviceTech,
       "sfpConfigXfpTuningSupported": sfpConfigXfpTuningSupported,
       "sfpConfigXfpDesiredChannel": sfpConfigXfpDesiredChannel,
       "sfpConfigXfpDesiredWl": sfpConfigXfpDesiredWl,
       "sfpConfigXfpWlError": sfpConfigXfpWlError,
       "sfpConfigXfpDesiredFreq": sfpConfigXfpDesiredFreq,
       "sfpConfigXfpFreqError": sfpConfigXfpFreqError,
       "sfpConfigXfpDitherSupported": sfpConfigXfpDitherSupported,
       "sfpConfigXfpDitherAdmin": sfpConfigXfpDitherAdmin,
       "sfpConfigXfpCapFreqFirstThz": sfpConfigXfpCapFreqFirstThz,
       "sfpConfigXfpCapFreqFirst10Ghz": sfpConfigXfpCapFreqFirst10Ghz,
       "sfpConfigXfpCapFreqLastThz": sfpConfigXfpCapFreqLastThz,
       "sfpConfigXfpCapFreqLast10Ghz": sfpConfigXfpCapFreqLast10Ghz,
       "sfpConfigXfpCapMaxSpacing10Ghz": sfpConfigXfpCapMaxSpacing10Ghz,
       "sfpConfigXfpCalibrationSupported": sfpConfigXfpCalibrationSupported,
       "sfpConfigXfpCalibrationEnabled": sfpConfigXfpCalibrationEnabled,
       "sfpConfigCfpExtId": sfpConfigCfpExtId,
       "sfpConfigCfpConnectorType": sfpConfigCfpConnectorType,
       "sfpConfigCfpEthernetCode": sfpConfigCfpEthernetCode,
       "sfpConfigCfpFcCode": sfpConfigCfpFcCode,
       "sfpConfigCfpCopperCode": sfpConfigCfpCopperCode,
       "sfpConfigCfpSonetCode": sfpConfigCfpSonetCode,
       "sfpConfigCfpOtnCode": sfpConfigCfpOtnCode,
       "sfpConfigCfpSupportedRates": sfpConfigCfpSupportedRates,
       "sfpConfigCfpSupportedLanes": sfpConfigCfpSupportedLanes,
       "sfpConfigCfpMediaProperties": sfpConfigCfpMediaProperties,
       "sfpConfigCfpMaxNetworkLaneRate": sfpConfigCfpMaxNetworkLaneRate,
       "sfpConfigCfpMaxHostLaneRate": sfpConfigCfpMaxHostLaneRate,
       "sfpConfigCfpMaxSmFiberLength": sfpConfigCfpMaxSmFiberLength,
       "sfpConfigCfpMaxMmFiberLength": sfpConfigCfpMaxMmFiberLength,
       "sfpConfigCfpMaxCopperCableLength": sfpConfigCfpMaxCopperCableLength,
       "sfpConfigCfpMinWavelenPerActive": sfpConfigCfpMinWavelenPerActive,
       "sfpConfigCfpMaxWavelenPerActive": sfpConfigCfpMaxWavelenPerActive,
       "sfpConfigCfpMaxLenOpticalWidth": sfpConfigCfpMaxLenOpticalWidth,
       "sfpConfigCfpSpacing": sfpConfigCfpSpacing,
       "sfpConfigQsfppEthernetCode": sfpConfigQsfppEthernetCode,
       "sfpConfigQsfppSonetCode": sfpConfigQsfppSonetCode,
       "sfpConfigCxpExtId": sfpConfigCxpExtId,
       "sfpConfigCxpConnectorType": sfpConfigCxpConnectorType,
       "sfpConfigCxpMaxSupportedRate": sfpConfigCxpMaxSupportedRate,
       "sfpConfigCxpNominalWavelength": sfpConfigCxpNominalWavelength,
       "sfpConfigCxpDeviceTech": sfpConfigCxpDeviceTech,
       "sfpConfigCohRxDesiredChannel": sfpConfigCohRxDesiredChannel,
       "sfpConfigCohRxDesiredWl": sfpConfigCohRxDesiredWl,
       "sfpConfigCohRxDesiredFreq": sfpConfigCohRxDesiredFreq,
       "sfpConfigCohCurrentCD": sfpConfigCohCurrentCD,
       "sfpConfigCohCurrentOSNR": sfpConfigCohCurrentOSNR,
       "sfpConfigCohAverageOSNR": sfpConfigCohAverageOSNR,
       "sfpConfigCohMaxCD": sfpConfigCohMaxCD,
       "sfpConfigNyquist": sfpConfigNyquist,
       "sfpDiag": sfpDiag,
       "sfpDiagTable": sfpDiagTable,
       "sfpDiagEntry": sfpDiagEntry,
       "sfpDiagInterface": sfpDiagInterface,
       "sfpDiagHighTempAlmThreshold": sfpDiagHighTempAlmThreshold,
       "sfpDiagLowTempAlmThreshold": sfpDiagLowTempAlmThreshold,
       "sfpDiagHighTempWrnThreshold": sfpDiagHighTempWrnThreshold,
       "sfpDiagLowTempWrnThreshold": sfpDiagLowTempWrnThreshold,
       "sfpDiagHighVoltAlmThreshold": sfpDiagHighVoltAlmThreshold,
       "sfpDiagLowVoltAlmThreshold": sfpDiagLowVoltAlmThreshold,
       "sfpDiagHighVoltWrnThreshold": sfpDiagHighVoltWrnThreshold,
       "sfpDiagLowVoltWrnThreshold": sfpDiagLowVoltWrnThreshold,
       "sfpDiagHighTxBiasAlmThreshold": sfpDiagHighTxBiasAlmThreshold,
       "sfpDiagLowTxBiasAlmThreshold": sfpDiagLowTxBiasAlmThreshold,
       "sfpDiagHighTxBiasWrnThreshold": sfpDiagHighTxBiasWrnThreshold,
       "sfpDiagLowTxBiasWrnThreshold": sfpDiagLowTxBiasWrnThreshold,
       "sfpDiagHighTxPowerAlmThreshold": sfpDiagHighTxPowerAlmThreshold,
       "sfpDiagLowTxPowerAlmThreshold": sfpDiagLowTxPowerAlmThreshold,
       "sfpDiagHighTxPowerWrnThreshold": sfpDiagHighTxPowerWrnThreshold,
       "sfpDiagLowTxPowerWrnThreshold": sfpDiagLowTxPowerWrnThreshold,
       "sfpDiagHighRxPowerAlmThreshold": sfpDiagHighRxPowerAlmThreshold,
       "sfpDiagLowRxPowerAlmThreshold": sfpDiagLowRxPowerAlmThreshold,
       "sfpDiagHighRxPowerWrnThreshold": sfpDiagHighRxPowerWrnThreshold,
       "sfpDiagLowRxPowerWrnThreshold": sfpDiagLowRxPowerWrnThreshold,
       "sfpDiagHighLaserTempAlmThreshold": sfpDiagHighLaserTempAlmThreshold,
       "sfpDiagLowLaserTempAlmThreshold": sfpDiagLowLaserTempAlmThreshold,
       "sfpDiagHighLaserTempWrnThreshold": sfpDiagHighLaserTempWrnThreshold,
       "sfpDiagLowLaserTempWrnThreshold": sfpDiagLowLaserTempWrnThreshold,
       "sfpDiagHighWaveLenAlmThreshold": sfpDiagHighWaveLenAlmThreshold,
       "sfpDiagLowWaveLenAlmThreshold": sfpDiagLowWaveLenAlmThreshold,
       "sfpDiagHighWaveLenWrnThreshold": sfpDiagHighWaveLenWrnThreshold,
       "sfpDiagLowWaveLenWrnThreshold": sfpDiagLowWaveLenWrnThreshold,
       "sfpDiagHighTecCurrAlmThreshold": sfpDiagHighTecCurrAlmThreshold,
       "sfpDiagLowTecCurrAlmThreshold": sfpDiagLowTecCurrAlmThreshold,
       "sfpDiagHighTecCurrWrnThreshold": sfpDiagHighTecCurrWrnThreshold,
       "sfpDiagLowTecCurrWrnThreshold": sfpDiagLowTecCurrWrnThreshold,
       "sfpDiagModuleTemperature": sfpDiagModuleTemperature,
       "sfpDiagSupplyVoltage": sfpDiagSupplyVoltage,
       "sfpDiagTxBias": sfpDiagTxBias,
       "sfpDiagTxOutputPower": sfpDiagTxOutputPower,
       "sfpDiagRxInputPower": sfpDiagRxInputPower,
       "sfpDiagRxLaserTemperature": sfpDiagRxLaserTemperature,
       "sfpDiagRxMeasuredWavelength": sfpDiagRxMeasuredWavelength,
       "sfpDiagRxTecCurrent": sfpDiagRxTecCurrent,
       "sfpDiagAlarms": sfpDiagAlarms,
       "sfpDiagAlarmsMask": sfpDiagAlarmsMask,
       "sfpDiagWarnings": sfpDiagWarnings,
       "sfpDiagWarningsMask": sfpDiagWarningsMask,
       "sfpDiagConfLowRxPowerAlmThreshold": sfpDiagConfLowRxPowerAlmThreshold,
       "sfpDiagRxInputPowerFloat": sfpDiagRxInputPowerFloat,
       "sfpDiagCxpTxTemp": sfpDiagCxpTxTemp,
       "sfpDiagCxpHighTxTempAlmThreshold": sfpDiagCxpHighTxTempAlmThreshold,
       "sfpDiagCxpLowTxTempAlmThreshold": sfpDiagCxpLowTxTempAlmThreshold,
       "sfpDiagCxpRxTemp": sfpDiagCxpRxTemp,
       "sfpDiagCxpHighRxTempAlmThreshold": sfpDiagCxpHighRxTempAlmThreshold,
       "sfpDiagCxpLowRxTempAlmThreshold": sfpDiagCxpLowRxTempAlmThreshold,
       "sfpDiagOtdrFiberCutRange": sfpDiagOtdrFiberCutRange,
       "sfpDiagModuleTemperatureCelsius": sfpDiagModuleTemperatureCelsius,
       "sfpTraps": sfpTraps,
       "sfpConfigChangeTrap": sfpConfigChangeTrap,
       "sfpTune": sfpTune}
)
