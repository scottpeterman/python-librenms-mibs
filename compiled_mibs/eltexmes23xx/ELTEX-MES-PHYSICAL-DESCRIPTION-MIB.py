# SNMP MIB module (ELTEX-MES-PHYSICAL-DESCRIPTION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\eltexmes23xx\ELTEX-MES-PHYSICAL-DESCRIPTION-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:39:38 2025
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

(eltMes,) = mibBuilder.importSymbols(
    "ELTEX-MES",
    "eltMes")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(JackType,) = mibBuilder.importSymbols(
    "MAU-MIB",
    "JackType")

(rlCascadeAdminEntry,
 rlCascadeEntry,
 rlPhdUnitGenParamEntry) = mibBuilder.importSymbols(
    "RADLAN-Physicaldescription-MIB",
    "rlCascadeAdminEntry",
    "rlCascadeEntry",
    "rlPhdUnitGenParamEntry")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

eltMesPhysicalDescription = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53)
)
if mibBuilder.loadTexts:
    eltMesPhysicalDescription.setRevisions(
        ("2021-08-04 00:00",
         "2018-04-24 00:00",
         "2017-11-11 00:00",
         "2015-09-14 00:00",
         "2013-03-21 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltMesPhdTransceiver_ObjectIdentity = ObjectIdentity
eltMesPhdTransceiver = _EltMesPhdTransceiver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 1)
)
_EltPhdTransceiverInfoTable_Object = MibTable
eltPhdTransceiverInfoTable = _EltPhdTransceiverInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 1, 1)
)
if mibBuilder.loadTexts:
    eltPhdTransceiverInfoTable.setStatus("current")
_EltPhdTransceiverInfoEntry_Object = MibTableRow
eltPhdTransceiverInfoEntry = _EltPhdTransceiverInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 1, 1, 1)
)
eltPhdTransceiverInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    eltPhdTransceiverInfoEntry.setStatus("current")


class _EltPhdTransceiverInfoConnectorType_Type(Integer32):
    """Custom type eltPhdTransceiverInfoConnectorType based on Integer32"""
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


_EltPhdTransceiverInfoConnectorType_Type.__name__ = "Integer32"
_EltPhdTransceiverInfoConnectorType_Object = MibTableColumn
eltPhdTransceiverInfoConnectorType = _EltPhdTransceiverInfoConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 1, 1, 1, 1),
    _EltPhdTransceiverInfoConnectorType_Type()
)
eltPhdTransceiverInfoConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPhdTransceiverInfoConnectorType.setStatus("current")


class _EltPhdTransceiverInfoType_Type(Integer32):
    """Custom type eltPhdTransceiverInfoType based on Integer32"""
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


_EltPhdTransceiverInfoType_Type.__name__ = "Integer32"
_EltPhdTransceiverInfoType_Object = MibTableColumn
eltPhdTransceiverInfoType = _EltPhdTransceiverInfoType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 1, 1, 1, 2),
    _EltPhdTransceiverInfoType_Type()
)
eltPhdTransceiverInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPhdTransceiverInfoType.setStatus("current")
_EltPhdTransceiverInfoComplianceCode_Type = OctetString
_EltPhdTransceiverInfoComplianceCode_Object = MibTableColumn
eltPhdTransceiverInfoComplianceCode = _EltPhdTransceiverInfoComplianceCode_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 1, 1, 1, 3),
    _EltPhdTransceiverInfoComplianceCode_Type()
)
eltPhdTransceiverInfoComplianceCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPhdTransceiverInfoComplianceCode.setStatus("current")
_EltPhdTransceiverInfoWaveLength_Type = Integer32
_EltPhdTransceiverInfoWaveLength_Object = MibTableColumn
eltPhdTransceiverInfoWaveLength = _EltPhdTransceiverInfoWaveLength_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 1, 1, 1, 4),
    _EltPhdTransceiverInfoWaveLength_Type()
)
eltPhdTransceiverInfoWaveLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPhdTransceiverInfoWaveLength.setStatus("current")
_EltPhdTransceiverInfoVendorName_Type = OctetString
_EltPhdTransceiverInfoVendorName_Object = MibTableColumn
eltPhdTransceiverInfoVendorName = _EltPhdTransceiverInfoVendorName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 1, 1, 1, 5),
    _EltPhdTransceiverInfoVendorName_Type()
)
eltPhdTransceiverInfoVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPhdTransceiverInfoVendorName.setStatus("current")
_EltPhdTransceiverInfoSerialNumber_Type = OctetString
_EltPhdTransceiverInfoSerialNumber_Object = MibTableColumn
eltPhdTransceiverInfoSerialNumber = _EltPhdTransceiverInfoSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 1, 1, 1, 6),
    _EltPhdTransceiverInfoSerialNumber_Type()
)
eltPhdTransceiverInfoSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPhdTransceiverInfoSerialNumber.setStatus("current")


class _EltPhdTransceiverInfoFiberDiameterType_Type(Integer32):
    """Custom type eltPhdTransceiverInfoFiberDiameterType based on Integer32"""
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


_EltPhdTransceiverInfoFiberDiameterType_Type.__name__ = "Integer32"
_EltPhdTransceiverInfoFiberDiameterType_Object = MibTableColumn
eltPhdTransceiverInfoFiberDiameterType = _EltPhdTransceiverInfoFiberDiameterType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 1, 1, 1, 7),
    _EltPhdTransceiverInfoFiberDiameterType_Type()
)
eltPhdTransceiverInfoFiberDiameterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPhdTransceiverInfoFiberDiameterType.setStatus("current")
_EltPhdTransceiverInfoTransferDistance_Type = Integer32
_EltPhdTransceiverInfoTransferDistance_Object = MibTableColumn
eltPhdTransceiverInfoTransferDistance = _EltPhdTransceiverInfoTransferDistance_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 1, 1, 1, 8),
    _EltPhdTransceiverInfoTransferDistance_Type()
)
eltPhdTransceiverInfoTransferDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPhdTransceiverInfoTransferDistance.setStatus("current")
_EltPhdTransceiverInfoDiagnostic_Type = TruthValue
_EltPhdTransceiverInfoDiagnostic_Object = MibTableColumn
eltPhdTransceiverInfoDiagnostic = _EltPhdTransceiverInfoDiagnostic_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 1, 1, 1, 9),
    _EltPhdTransceiverInfoDiagnostic_Type()
)
eltPhdTransceiverInfoDiagnostic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPhdTransceiverInfoDiagnostic.setStatus("current")
_EltPhdTransceiverInfoPartNumber_Type = OctetString
_EltPhdTransceiverInfoPartNumber_Object = MibTableColumn
eltPhdTransceiverInfoPartNumber = _EltPhdTransceiverInfoPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 1, 1, 1, 10),
    _EltPhdTransceiverInfoPartNumber_Type()
)
eltPhdTransceiverInfoPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPhdTransceiverInfoPartNumber.setStatus("current")
_EltPhdTransceiverInfoVendorRev_Type = OctetString
_EltPhdTransceiverInfoVendorRev_Object = MibTableColumn
eltPhdTransceiverInfoVendorRev = _EltPhdTransceiverInfoVendorRev_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 1, 1, 1, 11),
    _EltPhdTransceiverInfoVendorRev_Type()
)
eltPhdTransceiverInfoVendorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPhdTransceiverInfoVendorRev.setStatus("current")
_EltPhdTransceiverThresholdTable_Object = MibTable
eltPhdTransceiverThresholdTable = _EltPhdTransceiverThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 1, 2)
)
if mibBuilder.loadTexts:
    eltPhdTransceiverThresholdTable.setStatus("current")
_EltPhdTransceiverThresholdEntry_Object = MibTableRow
eltPhdTransceiverThresholdEntry = _EltPhdTransceiverThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 1, 2, 1)
)
eltPhdTransceiverThresholdEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ELTEX-MES-PHYSICAL-DESCRIPTION-MIB", "eltPhdTransceiverThresholdType"),
)
if mibBuilder.loadTexts:
    eltPhdTransceiverThresholdEntry.setStatus("current")


class _EltPhdTransceiverThresholdType_Type(Integer32):
    """Custom type eltPhdTransceiverThresholdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("temperature", 0),
          ("supply", 1),
          ("txBias", 2),
          ("txOutput", 3),
          ("rxOpticalPower", 4))
    )


_EltPhdTransceiverThresholdType_Type.__name__ = "Integer32"
_EltPhdTransceiverThresholdType_Object = MibTableColumn
eltPhdTransceiverThresholdType = _EltPhdTransceiverThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 1, 2, 1, 1),
    _EltPhdTransceiverThresholdType_Type()
)
eltPhdTransceiverThresholdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPhdTransceiverThresholdType.setStatus("current")


class _EltPhdTransceiverThresholdAction_Type(Integer32):
    """Custom type eltPhdTransceiverThresholdAction based on Integer32"""
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
          ("log", 1),
          ("send-trap", 2))
    )


_EltPhdTransceiverThresholdAction_Type.__name__ = "Integer32"
_EltPhdTransceiverThresholdAction_Object = MibTableColumn
eltPhdTransceiverThresholdAction = _EltPhdTransceiverThresholdAction_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 1, 2, 1, 2),
    _EltPhdTransceiverThresholdAction_Type()
)
eltPhdTransceiverThresholdAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPhdTransceiverThresholdAction.setStatus("current")
_EltPhdTransceiverThresholdHighAlarm_Type = Integer32
_EltPhdTransceiverThresholdHighAlarm_Object = MibTableColumn
eltPhdTransceiverThresholdHighAlarm = _EltPhdTransceiverThresholdHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 1, 2, 1, 3),
    _EltPhdTransceiverThresholdHighAlarm_Type()
)
eltPhdTransceiverThresholdHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPhdTransceiverThresholdHighAlarm.setStatus("current")
_EltPhdTransceiverThresholdHighWarning_Type = Integer32
_EltPhdTransceiverThresholdHighWarning_Object = MibTableColumn
eltPhdTransceiverThresholdHighWarning = _EltPhdTransceiverThresholdHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 1, 2, 1, 4),
    _EltPhdTransceiverThresholdHighWarning_Type()
)
eltPhdTransceiverThresholdHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPhdTransceiverThresholdHighWarning.setStatus("current")
_EltPhdTransceiverThresholdLowWarning_Type = Integer32
_EltPhdTransceiverThresholdLowWarning_Object = MibTableColumn
eltPhdTransceiverThresholdLowWarning = _EltPhdTransceiverThresholdLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 1, 2, 1, 5),
    _EltPhdTransceiverThresholdLowWarning_Type()
)
eltPhdTransceiverThresholdLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPhdTransceiverThresholdLowWarning.setStatus("current")
_EltPhdTransceiverThresholdLowAlarm_Type = Integer32
_EltPhdTransceiverThresholdLowAlarm_Object = MibTableColumn
eltPhdTransceiverThresholdLowAlarm = _EltPhdTransceiverThresholdLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 1, 2, 1, 6),
    _EltPhdTransceiverThresholdLowAlarm_Type()
)
eltPhdTransceiverThresholdLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPhdTransceiverThresholdLowAlarm.setStatus("current")
_EltPhdUnitGenParamTable_Object = MibTable
eltPhdUnitGenParamTable = _EltPhdUnitGenParamTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 2)
)
if mibBuilder.loadTexts:
    eltPhdUnitGenParamTable.setStatus("current")
_EltPhdUnitGenParamEntry_Object = MibTableRow
eltPhdUnitGenParamEntry = _EltPhdUnitGenParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 2, 1)
)
if mibBuilder.loadTexts:
    eltPhdUnitGenParamEntry.setStatus("current")
_EltPhdUnitGenParamCommitHash_Type = DisplayString
_EltPhdUnitGenParamCommitHash_Object = MibTableColumn
eltPhdUnitGenParamCommitHash = _EltPhdUnitGenParamCommitHash_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 2, 1, 1),
    _EltPhdUnitGenParamCommitHash_Type()
)
eltPhdUnitGenParamCommitHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPhdUnitGenParamCommitHash.setStatus("current")
_EltPhdUnitGenParamBuildTag_Type = DisplayString
_EltPhdUnitGenParamBuildTag_Object = MibTableColumn
eltPhdUnitGenParamBuildTag = _EltPhdUnitGenParamBuildTag_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 2, 1, 2),
    _EltPhdUnitGenParamBuildTag_Type()
)
eltPhdUnitGenParamBuildTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPhdUnitGenParamBuildTag.setStatus("current")
_EltPhdUnitGenParamBuildNumber_Type = DisplayString
_EltPhdUnitGenParamBuildNumber_Object = MibTableColumn
eltPhdUnitGenParamBuildNumber = _EltPhdUnitGenParamBuildNumber_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 2, 1, 3),
    _EltPhdUnitGenParamBuildNumber_Type()
)
eltPhdUnitGenParamBuildNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPhdUnitGenParamBuildNumber.setStatus("current")
_EltCascadeTable_Object = MibTable
eltCascadeTable = _EltCascadeTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 3)
)
if mibBuilder.loadTexts:
    eltCascadeTable.setStatus("current")
_EltCascadeEntry_Object = MibTableRow
eltCascadeEntry = _EltCascadeEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 3, 1)
)
if mibBuilder.loadTexts:
    eltCascadeEntry.setStatus("current")
_EltCascadeLastChange_Type = TimeTicks
_EltCascadeLastChange_Object = MibTableColumn
eltCascadeLastChange = _EltCascadeLastChange_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 3, 1, 1),
    _EltCascadeLastChange_Type()
)
eltCascadeLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltCascadeLastChange.setStatus("current")


class _EltCascadeOperStatus_Type(Integer32):
    """Custom type eltCascadeOperStatus based on Integer32"""
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


_EltCascadeOperStatus_Type.__name__ = "Integer32"
_EltCascadeOperStatus_Object = MibTableColumn
eltCascadeOperStatus = _EltCascadeOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 3, 1, 2),
    _EltCascadeOperStatus_Type()
)
eltCascadeOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltCascadeOperStatus.setStatus("current")


class _EltCascadeDuplexOperMode_Type(Integer32):
    """Custom type eltCascadeDuplexOperMode based on Integer32"""
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
        *(("half", 1),
          ("full", 2),
          ("hybrid", 3),
          ("unknown", 4))
    )


_EltCascadeDuplexOperMode_Type.__name__ = "Integer32"
_EltCascadeDuplexOperMode_Object = MibTableColumn
eltCascadeDuplexOperMode = _EltCascadeDuplexOperMode_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 3, 1, 3),
    _EltCascadeDuplexOperMode_Type()
)
eltCascadeDuplexOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltCascadeDuplexOperMode.setStatus("current")


class _EltCascadeOperSpeedDuplexAutoNegotiation_Type(Integer32):
    """Custom type eltCascadeOperSpeedDuplexAutoNegotiation based on Integer32"""
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
        *(("enabled", 1),
          ("disabled", 2),
          ("hybrid", 3),
          ("unknown", 4))
    )


_EltCascadeOperSpeedDuplexAutoNegotiation_Type.__name__ = "Integer32"
_EltCascadeOperSpeedDuplexAutoNegotiation_Object = MibTableColumn
eltCascadeOperSpeedDuplexAutoNegotiation = _EltCascadeOperSpeedDuplexAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 3, 1, 4),
    _EltCascadeOperSpeedDuplexAutoNegotiation_Type()
)
eltCascadeOperSpeedDuplexAutoNegotiation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltCascadeOperSpeedDuplexAutoNegotiation.setStatus("current")


class _EltCascadeOperMdix_Type(Integer32):
    """Custom type eltCascadeOperMdix based on Integer32"""
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
        *(("normal", 1),
          ("cross", 2),
          ("auto", 3),
          ("unknown", 4))
    )


_EltCascadeOperMdix_Type.__name__ = "Integer32"
_EltCascadeOperMdix_Object = MibTableColumn
eltCascadeOperMdix = _EltCascadeOperMdix_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 3, 1, 5),
    _EltCascadeOperMdix_Type()
)
eltCascadeOperMdix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltCascadeOperMdix.setStatus("current")


class _EltCascadeTransceiverType_Type(Integer32):
    """Custom type eltCascadeTransceiverType based on Integer32"""
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
        *(("regular", 1),
          ("fiberOptics", 2),
          ("comboRegular", 3),
          ("comboFiberOptics", 4))
    )


_EltCascadeTransceiverType_Type.__name__ = "Integer32"
_EltCascadeTransceiverType_Object = MibTableColumn
eltCascadeTransceiverType = _EltCascadeTransceiverType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 3, 1, 6),
    _EltCascadeTransceiverType_Type()
)
eltCascadeTransceiverType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltCascadeTransceiverType.setStatus("current")


class _EltCascadeIfType_Type(Integer32):
    """Custom type eltCascadeIfType based on Integer32"""
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
        *(("eth10M", 1),
          ("eth100M", 2),
          ("eth1000M", 3),
          ("eth10G", 4),
          ("eth20G", 5),
          ("eth40G", 6),
          ("eth100G", 7),
          ("unknown", 8))
    )


_EltCascadeIfType_Type.__name__ = "Integer32"
_EltCascadeIfType_Object = MibTableColumn
eltCascadeIfType = _EltCascadeIfType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 3, 1, 7),
    _EltCascadeIfType_Type()
)
eltCascadeIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltCascadeIfType.setStatus("current")


class _EltCascadeFecOperMode_Type(Integer32):
    """Custom type eltCascadeFecOperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("auto", 1),
          ("cl74", 2))
    )


_EltCascadeFecOperMode_Type.__name__ = "Integer32"
_EltCascadeFecOperMode_Object = MibTableColumn
eltCascadeFecOperMode = _EltCascadeFecOperMode_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 3, 1, 8),
    _EltCascadeFecOperMode_Type()
)
eltCascadeFecOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltCascadeFecOperMode.setStatus("current")
_EltMesPhdNsf_ObjectIdentity = ObjectIdentity
eltMesPhdNsf = _EltMesPhdNsf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 4)
)


class _EltPhdNsfEnable_Type(TruthValue):
    """Custom type eltPhdNsfEnable based on TruthValue"""
    defaultValue = 2


_EltPhdNsfEnable_Type.__name__ = "TruthValue"
_EltPhdNsfEnable_Object = MibScalar
eltPhdNsfEnable = _EltPhdNsfEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 4, 1),
    _EltPhdNsfEnable_Type()
)
eltPhdNsfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltPhdNsfEnable.setStatus("current")


class _EltPhdNsfTime_Type(Integer32):
    """Custom type eltPhdNsfTime based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 600),
    )


_EltPhdNsfTime_Type.__name__ = "Integer32"
_EltPhdNsfTime_Object = MibScalar
eltPhdNsfTime = _EltPhdNsfTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 4, 2),
    _EltPhdNsfTime_Type()
)
eltPhdNsfTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltPhdNsfTime.setStatus("current")
_EltCascadeAdminTable_Object = MibTable
eltCascadeAdminTable = _EltCascadeAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 6)
)
if mibBuilder.loadTexts:
    eltCascadeAdminTable.setStatus("current")
_EltCascadeAdminEntry_Object = MibTableRow
eltCascadeAdminEntry = _EltCascadeAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 6, 1)
)
if mibBuilder.loadTexts:
    eltCascadeAdminEntry.setStatus("current")


class _EltCascadeAdminFec_Type(Integer32):
    """Custom type eltCascadeAdminFec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("auto", 1),
          ("cl74", 2))
    )


_EltCascadeAdminFec_Type.__name__ = "Integer32"
_EltCascadeAdminFec_Object = MibTableColumn
eltCascadeAdminFec = _EltCascadeAdminFec_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 6, 1, 1),
    _EltCascadeAdminFec_Type()
)
eltCascadeAdminFec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltCascadeAdminFec.setStatus("current")
rlPhdUnitGenParamEntry.registerAugmentions(
    ("ELTEX-MES-PHYSICAL-DESCRIPTION-MIB",
     "eltPhdUnitGenParamEntry")
)
eltPhdUnitGenParamEntry.setIndexNames(*rlPhdUnitGenParamEntry.getIndexNames())
rlCascadeEntry.registerAugmentions(
    ("ELTEX-MES-PHYSICAL-DESCRIPTION-MIB",
     "eltCascadeEntry")
)
eltCascadeEntry.setIndexNames(*rlCascadeEntry.getIndexNames())
rlCascadeAdminEntry.registerAugmentions(
    ("ELTEX-MES-PHYSICAL-DESCRIPTION-MIB",
     "eltCascadeAdminEntry")
)
eltCascadeAdminEntry.setIndexNames(*rlCascadeAdminEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-PHYSICAL-DESCRIPTION-MIB",
    **{"eltMesPhysicalDescription": eltMesPhysicalDescription,
       "eltMesPhdTransceiver": eltMesPhdTransceiver,
       "eltPhdTransceiverInfoTable": eltPhdTransceiverInfoTable,
       "eltPhdTransceiverInfoEntry": eltPhdTransceiverInfoEntry,
       "eltPhdTransceiverInfoConnectorType": eltPhdTransceiverInfoConnectorType,
       "eltPhdTransceiverInfoType": eltPhdTransceiverInfoType,
       "eltPhdTransceiverInfoComplianceCode": eltPhdTransceiverInfoComplianceCode,
       "eltPhdTransceiverInfoWaveLength": eltPhdTransceiverInfoWaveLength,
       "eltPhdTransceiverInfoVendorName": eltPhdTransceiverInfoVendorName,
       "eltPhdTransceiverInfoSerialNumber": eltPhdTransceiverInfoSerialNumber,
       "eltPhdTransceiverInfoFiberDiameterType": eltPhdTransceiverInfoFiberDiameterType,
       "eltPhdTransceiverInfoTransferDistance": eltPhdTransceiverInfoTransferDistance,
       "eltPhdTransceiverInfoDiagnostic": eltPhdTransceiverInfoDiagnostic,
       "eltPhdTransceiverInfoPartNumber": eltPhdTransceiverInfoPartNumber,
       "eltPhdTransceiverInfoVendorRev": eltPhdTransceiverInfoVendorRev,
       "eltPhdTransceiverThresholdTable": eltPhdTransceiverThresholdTable,
       "eltPhdTransceiverThresholdEntry": eltPhdTransceiverThresholdEntry,
       "eltPhdTransceiverThresholdType": eltPhdTransceiverThresholdType,
       "eltPhdTransceiverThresholdAction": eltPhdTransceiverThresholdAction,
       "eltPhdTransceiverThresholdHighAlarm": eltPhdTransceiverThresholdHighAlarm,
       "eltPhdTransceiverThresholdHighWarning": eltPhdTransceiverThresholdHighWarning,
       "eltPhdTransceiverThresholdLowWarning": eltPhdTransceiverThresholdLowWarning,
       "eltPhdTransceiverThresholdLowAlarm": eltPhdTransceiverThresholdLowAlarm,
       "eltPhdUnitGenParamTable": eltPhdUnitGenParamTable,
       "eltPhdUnitGenParamEntry": eltPhdUnitGenParamEntry,
       "eltPhdUnitGenParamCommitHash": eltPhdUnitGenParamCommitHash,
       "eltPhdUnitGenParamBuildTag": eltPhdUnitGenParamBuildTag,
       "eltPhdUnitGenParamBuildNumber": eltPhdUnitGenParamBuildNumber,
       "eltCascadeTable": eltCascadeTable,
       "eltCascadeEntry": eltCascadeEntry,
       "eltCascadeLastChange": eltCascadeLastChange,
       "eltCascadeOperStatus": eltCascadeOperStatus,
       "eltCascadeDuplexOperMode": eltCascadeDuplexOperMode,
       "eltCascadeOperSpeedDuplexAutoNegotiation": eltCascadeOperSpeedDuplexAutoNegotiation,
       "eltCascadeOperMdix": eltCascadeOperMdix,
       "eltCascadeTransceiverType": eltCascadeTransceiverType,
       "eltCascadeIfType": eltCascadeIfType,
       "eltCascadeFecOperMode": eltCascadeFecOperMode,
       "eltMesPhdNsf": eltMesPhdNsf,
       "eltPhdNsfEnable": eltPhdNsfEnable,
       "eltPhdNsfTime": eltPhdNsfTime,
       "eltCascadeAdminTable": eltCascadeAdminTable,
       "eltCascadeAdminEntry": eltCascadeAdminEntry,
       "eltCascadeAdminFec": eltCascadeAdminFec}
)
