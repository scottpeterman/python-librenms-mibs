# SNMP MIB module (ELTEX-PHY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\eltexmes24xx\ELTEX-PHY-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:39:50 2025
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

(eltexLtd,) = mibBuilder.importSymbols(
    "ELTEX-SMI-ACTUAL",
    "eltexLtd")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

eltexPhyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 52)
)
if mibBuilder.loadTexts:
    eltexPhyMIB.setRevisions(
        ("2020-10-15 00:00",
         "2018-10-30 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EltexPhyTransConnectorType(TextualConvention, Integer32):
    status = "current"
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
              12,
              32,
              33,
              34,
              35,
              127,
              255)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("sc", 1),
          ("fibre-ch-st1", 2),
          ("fibre-ch-st2", 3),
          ("bnc-tnc", 4),
          ("fibre-ch-coaxial-headers", 5),
          ("fibrejack", 6),
          ("lc", 7),
          ("mt-rj", 8),
          ("mu", 9),
          ("sg", 10),
          ("optical-pigtail", 11),
          ("mpo-parallel-optic", 12),
          ("hssdc-ii", 32),
          ("copper-pigtail", 33),
          ("rj45", 34),
          ("no-separable-connector", 35),
          ("unallocated", 127),
          ("vendorspec", 255))
    )



class EltexPhyTransType(TextualConvention, Integer32):
    status = "current"
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
              12,
              13,
              127,
              255)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("gbic", 1),
          ("sff", 2),
          ("sfp-sfpplus", 3),
          ("xbi-300-pin", 4),
          ("xenpak", 5),
          ("xfp", 6),
          ("xff", 7),
          ("xfp-e", 8),
          ("xpak", 9),
          ("x2", 10),
          ("dwdm-sfp", 11),
          ("qsfp", 12),
          ("qsfpplus", 13),
          ("reserved", 127),
          ("vendorspec", 255))
    )



class EltexPhyTransFiberDiameter(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("fiber9", 1),
          ("fiber50", 2),
          ("fiber625", 3),
          ("copper", 4),
          ("unknown", 65535))
    )



class EltexPhyTransDiagnosticType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("temperature", 1),
          ("supplyVoltage", 2),
          ("txBiasCurrent", 3),
          ("txOpticalPower", 4),
          ("rxOpticalPower", 5),
          ("lossOfSignal", 6))
    )



class EltexPhyTestSetType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("cableStatus", 1)
    )



class EltexPhyTestGetStatus(TextualConvention, Integer32):
    status = "current"
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
        *(("none", 1),
          ("success", 2),
          ("inProgress", 3),
          ("notSupported", 4),
          ("unableToRun", 5),
          ("aborted", 6),
          ("failed", 7))
    )



class EltexPhyTestGetUnits(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("integer", 1),
          ("boolean", 2),
          ("meter", 3))
    )



class EltexPhyTestGetType(TextualConvention, Integer32):
    status = "current"
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
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("channelAShort", 1),
          ("channelBShort", 2),
          ("channelCShort", 3),
          ("channelDShort", 4),
          ("channelAOpen", 5),
          ("channelBOpen", 6),
          ("channelCOpen", 7),
          ("channelDOpen", 8),
          ("channelAMismatch", 9),
          ("channelBMismatch", 10),
          ("channelCMismatch", 11),
          ("channelDMismatch", 12),
          ("channelALineDriver", 13),
          ("channelBLineDriver", 14),
          ("channelCLineDriver", 15),
          ("channelDLineDriver", 16),
          ("channelALength", 17),
          ("channelBLength", 18),
          ("channelCLength", 19),
          ("channelDLength", 20),
          ("channelACross", 21),
          ("channelBCross", 22),
          ("channelCCross", 23),
          ("channelDCross", 24))
    )



# MIB Managed Objects in the order of their OIDs

_EltexPhyObjects_ObjectIdentity = ObjectIdentity
eltexPhyObjects = _EltexPhyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 52, 1)
)
_EltexPhyTransceiverObjects_ObjectIdentity = ObjectIdentity
eltexPhyTransceiverObjects = _EltexPhyTransceiverObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 52, 1, 1)
)
_EltexPhyTransceiverGlobals_ObjectIdentity = ObjectIdentity
eltexPhyTransceiverGlobals = _EltexPhyTransceiverGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 52, 1, 1, 1)
)
_EltexPhyTransceiverConfigs_ObjectIdentity = ObjectIdentity
eltexPhyTransceiverConfigs = _EltexPhyTransceiverConfigs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 52, 1, 1, 2)
)
_EltexPhyTransceiverStatistics_ObjectIdentity = ObjectIdentity
eltexPhyTransceiverStatistics = _EltexPhyTransceiverStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 52, 1, 1, 3)
)
_EltexPhyTransceiverInfoTable_Object = MibTable
eltexPhyTransceiverInfoTable = _EltexPhyTransceiverInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 52, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    eltexPhyTransceiverInfoTable.setStatus("current")
_EltexPhyTransceiverInfoEntry_Object = MibTableRow
eltexPhyTransceiverInfoEntry = _EltexPhyTransceiverInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 52, 1, 1, 3, 1, 1)
)
eltexPhyTransceiverInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    eltexPhyTransceiverInfoEntry.setStatus("current")
_EltexPhyTransceiverInfoConnectorType_Type = EltexPhyTransConnectorType
_EltexPhyTransceiverInfoConnectorType_Object = MibTableColumn
eltexPhyTransceiverInfoConnectorType = _EltexPhyTransceiverInfoConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 52, 1, 1, 3, 1, 1, 1),
    _EltexPhyTransceiverInfoConnectorType_Type()
)
eltexPhyTransceiverInfoConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexPhyTransceiverInfoConnectorType.setStatus("current")
_EltexPhyTransceiverInfoType_Type = EltexPhyTransType
_EltexPhyTransceiverInfoType_Object = MibTableColumn
eltexPhyTransceiverInfoType = _EltexPhyTransceiverInfoType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 52, 1, 1, 3, 1, 1, 2),
    _EltexPhyTransceiverInfoType_Type()
)
eltexPhyTransceiverInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexPhyTransceiverInfoType.setStatus("current")
_EltexPhyTransceiverInfoComplianceCode_Type = OctetString
_EltexPhyTransceiverInfoComplianceCode_Object = MibTableColumn
eltexPhyTransceiverInfoComplianceCode = _EltexPhyTransceiverInfoComplianceCode_Object(
    (1, 3, 6, 1, 4, 1, 35265, 52, 1, 1, 3, 1, 1, 3),
    _EltexPhyTransceiverInfoComplianceCode_Type()
)
eltexPhyTransceiverInfoComplianceCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexPhyTransceiverInfoComplianceCode.setStatus("current")
_EltexPhyTransceiverInfoWaveLength_Type = Integer32
_EltexPhyTransceiverInfoWaveLength_Object = MibTableColumn
eltexPhyTransceiverInfoWaveLength = _EltexPhyTransceiverInfoWaveLength_Object(
    (1, 3, 6, 1, 4, 1, 35265, 52, 1, 1, 3, 1, 1, 4),
    _EltexPhyTransceiverInfoWaveLength_Type()
)
eltexPhyTransceiverInfoWaveLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexPhyTransceiverInfoWaveLength.setStatus("current")
_EltexPhyTransceiverInfoVendorName_Type = OctetString
_EltexPhyTransceiverInfoVendorName_Object = MibTableColumn
eltexPhyTransceiverInfoVendorName = _EltexPhyTransceiverInfoVendorName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 52, 1, 1, 3, 1, 1, 5),
    _EltexPhyTransceiverInfoVendorName_Type()
)
eltexPhyTransceiverInfoVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexPhyTransceiverInfoVendorName.setStatus("current")
_EltexPhyTransceiverInfoSerialNumber_Type = OctetString
_EltexPhyTransceiverInfoSerialNumber_Object = MibTableColumn
eltexPhyTransceiverInfoSerialNumber = _EltexPhyTransceiverInfoSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 35265, 52, 1, 1, 3, 1, 1, 6),
    _EltexPhyTransceiverInfoSerialNumber_Type()
)
eltexPhyTransceiverInfoSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexPhyTransceiverInfoSerialNumber.setStatus("current")
_EltexPhyTransceiverInfoFiberDiameter_Type = EltexPhyTransFiberDiameter
_EltexPhyTransceiverInfoFiberDiameter_Object = MibTableColumn
eltexPhyTransceiverInfoFiberDiameter = _EltexPhyTransceiverInfoFiberDiameter_Object(
    (1, 3, 6, 1, 4, 1, 35265, 52, 1, 1, 3, 1, 1, 7),
    _EltexPhyTransceiverInfoFiberDiameter_Type()
)
eltexPhyTransceiverInfoFiberDiameter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexPhyTransceiverInfoFiberDiameter.setStatus("current")
_EltexPhyTransceiverInfoTransferDistance_Type = Integer32
_EltexPhyTransceiverInfoTransferDistance_Object = MibTableColumn
eltexPhyTransceiverInfoTransferDistance = _EltexPhyTransceiverInfoTransferDistance_Object(
    (1, 3, 6, 1, 4, 1, 35265, 52, 1, 1, 3, 1, 1, 8),
    _EltexPhyTransceiverInfoTransferDistance_Type()
)
eltexPhyTransceiverInfoTransferDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexPhyTransceiverInfoTransferDistance.setStatus("current")
_EltexPhyTransceiverInfoDiagnosticSupported_Type = TruthValue
_EltexPhyTransceiverInfoDiagnosticSupported_Object = MibTableColumn
eltexPhyTransceiverInfoDiagnosticSupported = _EltexPhyTransceiverInfoDiagnosticSupported_Object(
    (1, 3, 6, 1, 4, 1, 35265, 52, 1, 1, 3, 1, 1, 9),
    _EltexPhyTransceiverInfoDiagnosticSupported_Type()
)
eltexPhyTransceiverInfoDiagnosticSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexPhyTransceiverInfoDiagnosticSupported.setStatus("current")
_EltexPhyTransceiverInfoPartNumber_Type = OctetString
_EltexPhyTransceiverInfoPartNumber_Object = MibTableColumn
eltexPhyTransceiverInfoPartNumber = _EltexPhyTransceiverInfoPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 35265, 52, 1, 1, 3, 1, 1, 10),
    _EltexPhyTransceiverInfoPartNumber_Type()
)
eltexPhyTransceiverInfoPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexPhyTransceiverInfoPartNumber.setStatus("current")
_EltexPhyTransceiverInfoVendorRevision_Type = OctetString
_EltexPhyTransceiverInfoVendorRevision_Object = MibTableColumn
eltexPhyTransceiverInfoVendorRevision = _EltexPhyTransceiverInfoVendorRevision_Object(
    (1, 3, 6, 1, 4, 1, 35265, 52, 1, 1, 3, 1, 1, 11),
    _EltexPhyTransceiverInfoVendorRevision_Type()
)
eltexPhyTransceiverInfoVendorRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexPhyTransceiverInfoVendorRevision.setStatus("current")
_EltexPhyTransceiverDiagnosticTable_Object = MibTable
eltexPhyTransceiverDiagnosticTable = _EltexPhyTransceiverDiagnosticTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 52, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    eltexPhyTransceiverDiagnosticTable.setStatus("current")
_EltexPhyTransceiverDiagnosticEntry_Object = MibTableRow
eltexPhyTransceiverDiagnosticEntry = _EltexPhyTransceiverDiagnosticEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 52, 1, 1, 3, 2, 1)
)
eltexPhyTransceiverDiagnosticEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ELTEX-PHY-MIB", "eltexPhyTransceiverDiagnosticType"),
    (0, "ELTEX-PHY-MIB", "eltexPhyTransceiverDiagnosticChannel"),
)
if mibBuilder.loadTexts:
    eltexPhyTransceiverDiagnosticEntry.setStatus("current")
_EltexPhyTransceiverDiagnosticType_Type = EltexPhyTransDiagnosticType
_EltexPhyTransceiverDiagnosticType_Object = MibTableColumn
eltexPhyTransceiverDiagnosticType = _EltexPhyTransceiverDiagnosticType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 52, 1, 1, 3, 2, 1, 1),
    _EltexPhyTransceiverDiagnosticType_Type()
)
eltexPhyTransceiverDiagnosticType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexPhyTransceiverDiagnosticType.setStatus("current")


class _EltexPhyTransceiverDiagnosticChannel_Type(Integer32):
    """Custom type eltexPhyTransceiverDiagnosticChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_EltexPhyTransceiverDiagnosticChannel_Type.__name__ = "Integer32"
_EltexPhyTransceiverDiagnosticChannel_Object = MibTableColumn
eltexPhyTransceiverDiagnosticChannel = _EltexPhyTransceiverDiagnosticChannel_Object(
    (1, 3, 6, 1, 4, 1, 35265, 52, 1, 1, 3, 2, 1, 2),
    _EltexPhyTransceiverDiagnosticChannel_Type()
)
eltexPhyTransceiverDiagnosticChannel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexPhyTransceiverDiagnosticChannel.setStatus("current")
_EltexPhyTransceiverDiagnosticUnits_Type = DisplayString
_EltexPhyTransceiverDiagnosticUnits_Object = MibTableColumn
eltexPhyTransceiverDiagnosticUnits = _EltexPhyTransceiverDiagnosticUnits_Object(
    (1, 3, 6, 1, 4, 1, 35265, 52, 1, 1, 3, 2, 1, 3),
    _EltexPhyTransceiverDiagnosticUnits_Type()
)
eltexPhyTransceiverDiagnosticUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexPhyTransceiverDiagnosticUnits.setStatus("current")
_EltexPhyTransceiverDiagnosticHighAlarmThreshold_Type = Integer32
_EltexPhyTransceiverDiagnosticHighAlarmThreshold_Object = MibTableColumn
eltexPhyTransceiverDiagnosticHighAlarmThreshold = _EltexPhyTransceiverDiagnosticHighAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 35265, 52, 1, 1, 3, 2, 1, 4),
    _EltexPhyTransceiverDiagnosticHighAlarmThreshold_Type()
)
eltexPhyTransceiverDiagnosticHighAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexPhyTransceiverDiagnosticHighAlarmThreshold.setStatus("current")
_EltexPhyTransceiverDiagnosticHighWarningThreshold_Type = Integer32
_EltexPhyTransceiverDiagnosticHighWarningThreshold_Object = MibTableColumn
eltexPhyTransceiverDiagnosticHighWarningThreshold = _EltexPhyTransceiverDiagnosticHighWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 35265, 52, 1, 1, 3, 2, 1, 5),
    _EltexPhyTransceiverDiagnosticHighWarningThreshold_Type()
)
eltexPhyTransceiverDiagnosticHighWarningThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexPhyTransceiverDiagnosticHighWarningThreshold.setStatus("current")
_EltexPhyTransceiverDiagnosticLowWarningThreshold_Type = Integer32
_EltexPhyTransceiverDiagnosticLowWarningThreshold_Object = MibTableColumn
eltexPhyTransceiverDiagnosticLowWarningThreshold = _EltexPhyTransceiverDiagnosticLowWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 35265, 52, 1, 1, 3, 2, 1, 6),
    _EltexPhyTransceiverDiagnosticLowWarningThreshold_Type()
)
eltexPhyTransceiverDiagnosticLowWarningThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexPhyTransceiverDiagnosticLowWarningThreshold.setStatus("current")
_EltexPhyTransceiverDiagnosticLowAlarmThreshold_Type = Integer32
_EltexPhyTransceiverDiagnosticLowAlarmThreshold_Object = MibTableColumn
eltexPhyTransceiverDiagnosticLowAlarmThreshold = _EltexPhyTransceiverDiagnosticLowAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 35265, 52, 1, 1, 3, 2, 1, 7),
    _EltexPhyTransceiverDiagnosticLowAlarmThreshold_Type()
)
eltexPhyTransceiverDiagnosticLowAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexPhyTransceiverDiagnosticLowAlarmThreshold.setStatus("current")
_EltexPhyTransceiverDiagnosticCurrentValue_Type = Integer32
_EltexPhyTransceiverDiagnosticCurrentValue_Object = MibTableColumn
eltexPhyTransceiverDiagnosticCurrentValue = _EltexPhyTransceiverDiagnosticCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 35265, 52, 1, 1, 3, 2, 1, 8),
    _EltexPhyTransceiverDiagnosticCurrentValue_Type()
)
eltexPhyTransceiverDiagnosticCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexPhyTransceiverDiagnosticCurrentValue.setStatus("current")
_EltexPhyTestObjects_ObjectIdentity = ObjectIdentity
eltexPhyTestObjects = _EltexPhyTestObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 52, 1, 2)
)
_EltexPhyTestGlobals_ObjectIdentity = ObjectIdentity
eltexPhyTestGlobals = _EltexPhyTestGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 52, 1, 2, 1)
)
_EltexPhyTestSetTable_Object = MibTable
eltexPhyTestSetTable = _EltexPhyTestSetTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 52, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    eltexPhyTestSetTable.setStatus("current")
_EltexPhyTestSetEntry_Object = MibTableRow
eltexPhyTestSetEntry = _EltexPhyTestSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 52, 1, 2, 1, 1, 1)
)
eltexPhyTestSetEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    eltexPhyTestSetEntry.setStatus("current")
_EltexPhyTestSetType_Type = EltexPhyTestSetType
_EltexPhyTestSetType_Object = MibTableColumn
eltexPhyTestSetType = _EltexPhyTestSetType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 52, 1, 2, 1, 1, 1, 1),
    _EltexPhyTestSetType_Type()
)
eltexPhyTestSetType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexPhyTestSetType.setStatus("current")
_EltexPhyTestGetTable_Object = MibTable
eltexPhyTestGetTable = _EltexPhyTestGetTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 52, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    eltexPhyTestGetTable.setStatus("current")
_EltexPhyTestGetEntry_Object = MibTableRow
eltexPhyTestGetEntry = _EltexPhyTestGetEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 52, 1, 2, 1, 2, 1)
)
eltexPhyTestGetEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ELTEX-PHY-MIB", "eltexPhyTestGetType"),
)
if mibBuilder.loadTexts:
    eltexPhyTestGetEntry.setStatus("current")
_EltexPhyTestGetType_Type = EltexPhyTestGetType
_EltexPhyTestGetType_Object = MibTableColumn
eltexPhyTestGetType = _EltexPhyTestGetType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 52, 1, 2, 1, 2, 1, 1),
    _EltexPhyTestGetType_Type()
)
eltexPhyTestGetType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexPhyTestGetType.setStatus("current")
_EltexPhyTestGetStatus_Type = EltexPhyTestGetStatus
_EltexPhyTestGetStatus_Object = MibTableColumn
eltexPhyTestGetStatus = _EltexPhyTestGetStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 52, 1, 2, 1, 2, 1, 2),
    _EltexPhyTestGetStatus_Type()
)
eltexPhyTestGetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexPhyTestGetStatus.setStatus("current")
_EltexPhyTestGetResult_Type = Integer32
_EltexPhyTestGetResult_Object = MibTableColumn
eltexPhyTestGetResult = _EltexPhyTestGetResult_Object(
    (1, 3, 6, 1, 4, 1, 35265, 52, 1, 2, 1, 2, 1, 3),
    _EltexPhyTestGetResult_Type()
)
eltexPhyTestGetResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexPhyTestGetResult.setStatus("current")
_EltexPhyTestGetUnits_Type = EltexPhyTestGetUnits
_EltexPhyTestGetUnits_Object = MibTableColumn
eltexPhyTestGetUnits = _EltexPhyTestGetUnits_Object(
    (1, 3, 6, 1, 4, 1, 35265, 52, 1, 2, 1, 2, 1, 4),
    _EltexPhyTestGetUnits_Type()
)
eltexPhyTestGetUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexPhyTestGetUnits.setStatus("current")


class _EltexPhyTestGetTimeStamp_Type(DisplayString):
    """Custom type eltexPhyTestGetTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_EltexPhyTestGetTimeStamp_Type.__name__ = "DisplayString"
_EltexPhyTestGetTimeStamp_Object = MibTableColumn
eltexPhyTestGetTimeStamp = _EltexPhyTestGetTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 35265, 52, 1, 2, 1, 2, 1, 5),
    _EltexPhyTestGetTimeStamp_Type()
)
eltexPhyTestGetTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexPhyTestGetTimeStamp.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-PHY-MIB",
    **{"EltexPhyTransConnectorType": EltexPhyTransConnectorType,
       "EltexPhyTransType": EltexPhyTransType,
       "EltexPhyTransFiberDiameter": EltexPhyTransFiberDiameter,
       "EltexPhyTransDiagnosticType": EltexPhyTransDiagnosticType,
       "EltexPhyTestSetType": EltexPhyTestSetType,
       "EltexPhyTestGetStatus": EltexPhyTestGetStatus,
       "EltexPhyTestGetUnits": EltexPhyTestGetUnits,
       "EltexPhyTestGetType": EltexPhyTestGetType,
       "eltexPhyMIB": eltexPhyMIB,
       "eltexPhyObjects": eltexPhyObjects,
       "eltexPhyTransceiverObjects": eltexPhyTransceiverObjects,
       "eltexPhyTransceiverGlobals": eltexPhyTransceiverGlobals,
       "eltexPhyTransceiverConfigs": eltexPhyTransceiverConfigs,
       "eltexPhyTransceiverStatistics": eltexPhyTransceiverStatistics,
       "eltexPhyTransceiverInfoTable": eltexPhyTransceiverInfoTable,
       "eltexPhyTransceiverInfoEntry": eltexPhyTransceiverInfoEntry,
       "eltexPhyTransceiverInfoConnectorType": eltexPhyTransceiverInfoConnectorType,
       "eltexPhyTransceiverInfoType": eltexPhyTransceiverInfoType,
       "eltexPhyTransceiverInfoComplianceCode": eltexPhyTransceiverInfoComplianceCode,
       "eltexPhyTransceiverInfoWaveLength": eltexPhyTransceiverInfoWaveLength,
       "eltexPhyTransceiverInfoVendorName": eltexPhyTransceiverInfoVendorName,
       "eltexPhyTransceiverInfoSerialNumber": eltexPhyTransceiverInfoSerialNumber,
       "eltexPhyTransceiverInfoFiberDiameter": eltexPhyTransceiverInfoFiberDiameter,
       "eltexPhyTransceiverInfoTransferDistance": eltexPhyTransceiverInfoTransferDistance,
       "eltexPhyTransceiverInfoDiagnosticSupported": eltexPhyTransceiverInfoDiagnosticSupported,
       "eltexPhyTransceiverInfoPartNumber": eltexPhyTransceiverInfoPartNumber,
       "eltexPhyTransceiverInfoVendorRevision": eltexPhyTransceiverInfoVendorRevision,
       "eltexPhyTransceiverDiagnosticTable": eltexPhyTransceiverDiagnosticTable,
       "eltexPhyTransceiverDiagnosticEntry": eltexPhyTransceiverDiagnosticEntry,
       "eltexPhyTransceiverDiagnosticType": eltexPhyTransceiverDiagnosticType,
       "eltexPhyTransceiverDiagnosticChannel": eltexPhyTransceiverDiagnosticChannel,
       "eltexPhyTransceiverDiagnosticUnits": eltexPhyTransceiverDiagnosticUnits,
       "eltexPhyTransceiverDiagnosticHighAlarmThreshold": eltexPhyTransceiverDiagnosticHighAlarmThreshold,
       "eltexPhyTransceiverDiagnosticHighWarningThreshold": eltexPhyTransceiverDiagnosticHighWarningThreshold,
       "eltexPhyTransceiverDiagnosticLowWarningThreshold": eltexPhyTransceiverDiagnosticLowWarningThreshold,
       "eltexPhyTransceiverDiagnosticLowAlarmThreshold": eltexPhyTransceiverDiagnosticLowAlarmThreshold,
       "eltexPhyTransceiverDiagnosticCurrentValue": eltexPhyTransceiverDiagnosticCurrentValue,
       "eltexPhyTestObjects": eltexPhyTestObjects,
       "eltexPhyTestGlobals": eltexPhyTestGlobals,
       "eltexPhyTestSetTable": eltexPhyTestSetTable,
       "eltexPhyTestSetEntry": eltexPhyTestSetEntry,
       "eltexPhyTestSetType": eltexPhyTestSetType,
       "eltexPhyTestGetTable": eltexPhyTestGetTable,
       "eltexPhyTestGetEntry": eltexPhyTestGetEntry,
       "eltexPhyTestGetType": eltexPhyTestGetType,
       "eltexPhyTestGetStatus": eltexPhyTestGetStatus,
       "eltexPhyTestGetResult": eltexPhyTestGetResult,
       "eltexPhyTestGetUnits": eltexPhyTestGetUnits,
       "eltexPhyTestGetTimeStamp": eltexPhyTestGetTimeStamp}
)
