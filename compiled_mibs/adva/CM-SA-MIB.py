# SNMP MIB module (CM-SA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\adva\CM-SA-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:15:27 2025
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

(fsp150cm,) = mibBuilder.importSymbols(
    "ADVA-MIB",
    "fsp150cm")

(AdminState,
 ClassOfServiceType,
 CmPmBinAction,
 IpPriorityMapMode,
 IpVersion,
 MepDestinationType,
 OperationalState,
 PerfCounter32,
 PerfCounter64,
 SchedActivityStatus,
 ScheduleType,
 SecondaryState,
 TrafficDirection,
 VlanId,
 VlanPriority) = mibBuilder.importSymbols(
    "CM-COMMON-MIB",
    "AdminState",
    "ClassOfServiceType",
    "CmPmBinAction",
    "IpPriorityMapMode",
    "IpVersion",
    "MepDestinationType",
    "OperationalState",
    "PerfCounter32",
    "PerfCounter64",
    "SchedActivityStatus",
    "ScheduleType",
    "SecondaryState",
    "TrafficDirection",
    "VlanId",
    "VlanPriority")

(neIndex,
 shelfIndex,
 slotIndex) = mibBuilder.importSymbols(
    "CM-ENTITY-MIB",
    "neIndex",
    "shelfIndex",
    "slotIndex")

(BitErrRate,
 PolicerColorMode) = mibBuilder.importSymbols(
    "CM-FACILITY-MIB",
    "BitErrRate",
    "PolicerColorMode")

(Dot1agCfmMepIdOrZero,) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "Dot1agCfmMepIdOrZero")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue",
    "VariablePointer")


# MODULE-IDENTITY

cmServiceAssuranceMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8)
)
if mibBuilder.loadTexts:
    cmServiceAssuranceMIB.setRevisions(
        ("2019-12-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EcpaTestStatus(TextualConvention, Integer32):
    status = "current"
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
        *(("initial", 1),
          ("in-progress", 2),
          ("stopped", 3),
          ("completed", 4),
          ("aborted", 5))
    )



class EcpaPayloadType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 1),
          ("random", 2))
    )



class EcpaTestType(TextualConvention, Integer32):
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
        *(("duration", 1),
          ("numframes", 2),
          ("continuous", 3))
    )



class EcpaType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("regular", 1),
          ("enhanced", 2))
    )



class EcpaMonitorPortType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("source", 2))
    )



class EcpaControlAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 0),
          ("start", 1),
          ("stop", 2))
    )



class EsaProbeProtocol(TextualConvention, Integer32):
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
        *(("icmpEcho", 1),
          ("udpEcho", 2),
          ("icmpTimestamp", 3),
          ("y1731", 4),
          ("y1731-slm-slr", 5),
          ("y1731-slm-dmm", 6))
    )



class EsaProbeDirection(TextualConvention, Integer32):
    status = "current"
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



class EsaReflectorDirection(TextualConvention, Integer32):
    status = "current"
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



class EsaProbePmIntervalType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("current", 1),
          ("rollover", 2))
    )



class EsaProbeHistoryIntervalType(TextualConvention, Integer32):
    status = "current"
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
        *(("interval-1min", 1),
          ("interval-5min", 2),
          ("interval-10min", 3),
          ("interval-15min", 4),
          ("interval-60min", 5))
    )



class EsaProbeDistStatsType(TextualConvention, Integer32):
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("roundtrip-delay", 1),
          ("oneway-p2r-delay", 2),
          ("oneway-r2p-delay", 3),
          ("oneway-p2r-jitter", 4),
          ("oneway-r2p-jitter", 5),
          ("oneway-p2r-absjitter", 6),
          ("oneway-r2p-absjitter", 7),
          ("roundtrip-absjitter", 8),
          ("oneway-p2r-fdr", 9),
          ("oneway-r2p-fdr", 10),
          ("roundtrip-fdr", 11))
    )



class EsaAction(TextualConvention, Integer32):
    status = "current"
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
        *(("not-applicable", 0),
          ("suspend", 1),
          ("resume", 2),
          ("addEsaProbe", 3),
          ("removeEsaProbe", 4))
    )



class EsaProbePktIntervalType(TextualConvention, Integer32):
    status = "current"
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
        *(("not-applicable", 0),
          ("interval-10ms", 1),
          ("interval-100ms", 2),
          ("interval-1sec", 3),
          ("interval-10sec", 4),
          ("interval-1min", 5))
    )



class EsaProbeSLAMonitorType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 0),
          ("point-to-point", 1),
          ("point-to-multipoint", 2))
    )



class BerTestStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 0),
          ("running", 1),
          ("not-running", 2))
    )



class BerTestMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 0),
          ("generator", 1),
          ("monitor", 2),
          ("singleend", 3))
    )



class BertControlAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 0),
          ("start", 1),
          ("stop", 2))
    )



class BertPattern(TextualConvention, Integer32):
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 0),
          ("all-0", 1),
          ("all-1", 2),
          ("alt-1100", 3),
          ("bit-1in8", 4),
          ("bit-3in24", 5),
          ("bit-2exp20-qrss", 6),
          ("bit-2exp11-prbs", 7),
          ("bit-2exp15-prbs", 8),
          ("bit-2exp23-prbs", 9),
          ("userdefined", 10))
    )



class BertUserPatternLength(TextualConvention, Integer32):
    status = "current"
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
        *(("not-applicable", 0),
          ("length-1byte", 1),
          ("length-2byte", 2),
          ("length-3byte", 3),
          ("length-4byte", 4))
    )



class BertSyncState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 0),
          ("sync", 1),
          ("outofsync", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CmServAssuranceObjects_ObjectIdentity = ObjectIdentity
cmServAssuranceObjects = _CmServAssuranceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1)
)
_EcpaControlTable_Object = MibTable
ecpaControlTable = _EcpaControlTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 1)
)
if mibBuilder.loadTexts:
    ecpaControlTable.setStatus("current")
_EcpaControlEntry_Object = MibTableRow
ecpaControlEntry = _EcpaControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 1, 1)
)
ecpaControlEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-SA-MIB", "ecpaControlIndex"),
)
if mibBuilder.loadTexts:
    ecpaControlEntry.setStatus("current")
_EcpaControlIndex_Type = Integer32
_EcpaControlIndex_Object = MibTableColumn
ecpaControlIndex = _EcpaControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 1, 1, 1),
    _EcpaControlIndex_Type()
)
ecpaControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpaControlIndex.setStatus("current")
_EcpaControlSourcePort_Type = VariablePointer
_EcpaControlSourcePort_Object = MibTableColumn
ecpaControlSourcePort = _EcpaControlSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 1, 1, 2),
    _EcpaControlSourcePort_Type()
)
ecpaControlSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaControlSourcePort.setStatus("current")
_EcpaControlTestType_Type = EcpaTestType
_EcpaControlTestType_Object = MibTableColumn
ecpaControlTestType = _EcpaControlTestType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 1, 1, 3),
    _EcpaControlTestType_Type()
)
ecpaControlTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaControlTestType.setStatus("current")


class _EcpaControlNumFrames_Type(Integer32):
    """Custom type ecpaControlNumFrames based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EcpaControlNumFrames_Type.__name__ = "Integer32"
_EcpaControlNumFrames_Object = MibTableColumn
ecpaControlNumFrames = _EcpaControlNumFrames_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 1, 1, 4),
    _EcpaControlNumFrames_Type()
)
ecpaControlNumFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaControlNumFrames.setStatus("current")


class _EcpaControlDuration_Type(Integer32):
    """Custom type ecpaControlDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 259200),
    )


_EcpaControlDuration_Type.__name__ = "Integer32"
_EcpaControlDuration_Object = MibTableColumn
ecpaControlDuration = _EcpaControlDuration_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 1, 1, 5),
    _EcpaControlDuration_Type()
)
ecpaControlDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaControlDuration.setStatus("current")
_EcpaControlInjectorDirection_Type = TrafficDirection
_EcpaControlInjectorDirection_Object = MibTableColumn
ecpaControlInjectorDirection = _EcpaControlInjectorDirection_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 1, 1, 6),
    _EcpaControlInjectorDirection_Type()
)
ecpaControlInjectorDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaControlInjectorDirection.setStatus("current")
_EcpaControlMonitorDirection_Type = TrafficDirection
_EcpaControlMonitorDirection_Object = MibTableColumn
ecpaControlMonitorDirection = _EcpaControlMonitorDirection_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 1, 1, 7),
    _EcpaControlMonitorDirection_Type()
)
ecpaControlMonitorDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaControlMonitorDirection.setStatus("current")


class _EcpaControlStream1_Type(Integer32):
    """Custom type ecpaControlStream1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_EcpaControlStream1_Type.__name__ = "Integer32"
_EcpaControlStream1_Object = MibTableColumn
ecpaControlStream1 = _EcpaControlStream1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 1, 1, 8),
    _EcpaControlStream1_Type()
)
ecpaControlStream1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaControlStream1.setStatus("current")


class _EcpaControlStream2_Type(Integer32):
    """Custom type ecpaControlStream2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_EcpaControlStream2_Type.__name__ = "Integer32"
_EcpaControlStream2_Object = MibTableColumn
ecpaControlStream2 = _EcpaControlStream2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 1, 1, 9),
    _EcpaControlStream2_Type()
)
ecpaControlStream2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaControlStream2.setStatus("current")


class _EcpaControlStream3_Type(Integer32):
    """Custom type ecpaControlStream3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_EcpaControlStream3_Type.__name__ = "Integer32"
_EcpaControlStream3_Object = MibTableColumn
ecpaControlStream3 = _EcpaControlStream3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 1, 1, 10),
    _EcpaControlStream3_Type()
)
ecpaControlStream3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaControlStream3.setStatus("current")
_EcpaControlAction_Type = EcpaControlAction
_EcpaControlAction_Object = MibTableColumn
ecpaControlAction = _EcpaControlAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 1, 1, 11),
    _EcpaControlAction_Type()
)
ecpaControlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaControlAction.setStatus("current")
_EcpaControlTestStatus_Type = EcpaTestStatus
_EcpaControlTestStatus_Object = MibTableColumn
ecpaControlTestStatus = _EcpaControlTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 1, 1, 12),
    _EcpaControlTestStatus_Type()
)
ecpaControlTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpaControlTestStatus.setStatus("current")
_EcpaControlStorageType_Type = StorageType
_EcpaControlStorageType_Object = MibTableColumn
ecpaControlStorageType = _EcpaControlStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 1, 1, 13),
    _EcpaControlStorageType_Type()
)
ecpaControlStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ecpaControlStorageType.setStatus("current")
_EcpaControlRowStatus_Type = RowStatus
_EcpaControlRowStatus_Object = MibTableColumn
ecpaControlRowStatus = _EcpaControlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 1, 1, 14),
    _EcpaControlRowStatus_Type()
)
ecpaControlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ecpaControlRowStatus.setStatus("current")
_EcpaControlEcpaType_Type = EcpaType
_EcpaControlEcpaType_Object = MibTableColumn
ecpaControlEcpaType = _EcpaControlEcpaType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 1, 1, 15),
    _EcpaControlEcpaType_Type()
)
ecpaControlEcpaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaControlEcpaType.setStatus("current")
_EcpaControlMonitorPortType_Type = EcpaMonitorPortType
_EcpaControlMonitorPortType_Object = MibTableColumn
ecpaControlMonitorPortType = _EcpaControlMonitorPortType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 1, 1, 16),
    _EcpaControlMonitorPortType_Type()
)
ecpaControlMonitorPortType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ecpaControlMonitorPortType.setStatus("current")
_EcpaConfigStreamTable_Object = MibTable
ecpaConfigStreamTable = _EcpaConfigStreamTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 2)
)
if mibBuilder.loadTexts:
    ecpaConfigStreamTable.setStatus("current")
_EcpaConfigStreamEntry_Object = MibTableRow
ecpaConfigStreamEntry = _EcpaConfigStreamEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 2, 1)
)
ecpaConfigStreamEntry.setIndexNames(
    (0, "CM-SA-MIB", "ecpaConfigStreamIndex"),
)
if mibBuilder.loadTexts:
    ecpaConfigStreamEntry.setStatus("current")


class _EcpaConfigStreamIndex_Type(Integer32):
    """Custom type ecpaConfigStreamIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_EcpaConfigStreamIndex_Type.__name__ = "Integer32"
_EcpaConfigStreamIndex_Object = MibTableColumn
ecpaConfigStreamIndex = _EcpaConfigStreamIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 2, 1, 1),
    _EcpaConfigStreamIndex_Type()
)
ecpaConfigStreamIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaConfigStreamIndex.setStatus("current")


class _EcpaConfigStreamName_Type(DisplayString):
    """Custom type ecpaConfigStreamName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EcpaConfigStreamName_Type.__name__ = "DisplayString"
_EcpaConfigStreamName_Object = MibTableColumn
ecpaConfigStreamName = _EcpaConfigStreamName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 2, 1, 2),
    _EcpaConfigStreamName_Type()
)
ecpaConfigStreamName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaConfigStreamName.setStatus("current")


class _EcpaConfigStreamFrameSize_Type(Integer32):
    """Custom type ecpaConfigStreamFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 9612),
    )


_EcpaConfigStreamFrameSize_Type.__name__ = "Integer32"
_EcpaConfigStreamFrameSize_Object = MibTableColumn
ecpaConfigStreamFrameSize = _EcpaConfigStreamFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 2, 1, 3),
    _EcpaConfigStreamFrameSize_Type()
)
ecpaConfigStreamFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaConfigStreamFrameSize.setStatus("current")
_EcpaConfigStreamRate_Type = Unsigned32
_EcpaConfigStreamRate_Object = MibTableColumn
ecpaConfigStreamRate = _EcpaConfigStreamRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 2, 1, 4),
    _EcpaConfigStreamRate_Type()
)
ecpaConfigStreamRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaConfigStreamRate.setStatus("current")
_EcpaConfigStreamPayloadType_Type = EcpaPayloadType
_EcpaConfigStreamPayloadType_Object = MibTableColumn
ecpaConfigStreamPayloadType = _EcpaConfigStreamPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 2, 1, 5),
    _EcpaConfigStreamPayloadType_Type()
)
ecpaConfigStreamPayloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaConfigStreamPayloadType.setStatus("current")


class _EcpaConfigStreamSignature_Type(DisplayString):
    """Custom type ecpaConfigStreamSignature based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_EcpaConfigStreamSignature_Type.__name__ = "DisplayString"
_EcpaConfigStreamSignature_Object = MibTableColumn
ecpaConfigStreamSignature = _EcpaConfigStreamSignature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 2, 1, 6),
    _EcpaConfigStreamSignature_Type()
)
ecpaConfigStreamSignature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaConfigStreamSignature.setStatus("current")
_EcpaConfigStreamDestinationMAC_Type = MacAddress
_EcpaConfigStreamDestinationMAC_Object = MibTableColumn
ecpaConfigStreamDestinationMAC = _EcpaConfigStreamDestinationMAC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 2, 1, 7),
    _EcpaConfigStreamDestinationMAC_Type()
)
ecpaConfigStreamDestinationMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaConfigStreamDestinationMAC.setStatus("current")
_EcpaConfigStreamSourceMAC_Type = MacAddress
_EcpaConfigStreamSourceMAC_Object = MibTableColumn
ecpaConfigStreamSourceMAC = _EcpaConfigStreamSourceMAC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 2, 1, 8),
    _EcpaConfigStreamSourceMAC_Type()
)
ecpaConfigStreamSourceMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaConfigStreamSourceMAC.setStatus("current")
_EcpaConfigStreamOuterVlanEnabled_Type = TruthValue
_EcpaConfigStreamOuterVlanEnabled_Object = MibTableColumn
ecpaConfigStreamOuterVlanEnabled = _EcpaConfigStreamOuterVlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 2, 1, 9),
    _EcpaConfigStreamOuterVlanEnabled_Type()
)
ecpaConfigStreamOuterVlanEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaConfigStreamOuterVlanEnabled.setStatus("current")
_EcpaConfigStreamOuterVlanId_Type = VlanId
_EcpaConfigStreamOuterVlanId_Object = MibTableColumn
ecpaConfigStreamOuterVlanId = _EcpaConfigStreamOuterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 2, 1, 10),
    _EcpaConfigStreamOuterVlanId_Type()
)
ecpaConfigStreamOuterVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaConfigStreamOuterVlanId.setStatus("current")
_EcpaConfigStreamOuterVlanPrio_Type = VlanPriority
_EcpaConfigStreamOuterVlanPrio_Object = MibTableColumn
ecpaConfigStreamOuterVlanPrio = _EcpaConfigStreamOuterVlanPrio_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 2, 1, 11),
    _EcpaConfigStreamOuterVlanPrio_Type()
)
ecpaConfigStreamOuterVlanPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaConfigStreamOuterVlanPrio.setStatus("current")


class _EcpaConfigStreamOuterVlanEtherType_Type(Integer32):
    """Custom type ecpaConfigStreamOuterVlanEtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EcpaConfigStreamOuterVlanEtherType_Type.__name__ = "Integer32"
_EcpaConfigStreamOuterVlanEtherType_Object = MibTableColumn
ecpaConfigStreamOuterVlanEtherType = _EcpaConfigStreamOuterVlanEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 2, 1, 12),
    _EcpaConfigStreamOuterVlanEtherType_Type()
)
ecpaConfigStreamOuterVlanEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaConfigStreamOuterVlanEtherType.setStatus("current")
_EcpaConfigStreamInnerVlanEnabled_Type = TruthValue
_EcpaConfigStreamInnerVlanEnabled_Object = MibTableColumn
ecpaConfigStreamInnerVlanEnabled = _EcpaConfigStreamInnerVlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 2, 1, 13),
    _EcpaConfigStreamInnerVlanEnabled_Type()
)
ecpaConfigStreamInnerVlanEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaConfigStreamInnerVlanEnabled.setStatus("current")
_EcpaConfigStreamInnerVlanId_Type = VlanId
_EcpaConfigStreamInnerVlanId_Object = MibTableColumn
ecpaConfigStreamInnerVlanId = _EcpaConfigStreamInnerVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 2, 1, 14),
    _EcpaConfigStreamInnerVlanId_Type()
)
ecpaConfigStreamInnerVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaConfigStreamInnerVlanId.setStatus("current")
_EcpaConfigStreamInnerVlanPrio_Type = VlanPriority
_EcpaConfigStreamInnerVlanPrio_Object = MibTableColumn
ecpaConfigStreamInnerVlanPrio = _EcpaConfigStreamInnerVlanPrio_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 2, 1, 15),
    _EcpaConfigStreamInnerVlanPrio_Type()
)
ecpaConfigStreamInnerVlanPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaConfigStreamInnerVlanPrio.setStatus("current")


class _EcpaConfigStreamInnerVlanEtherType_Type(Integer32):
    """Custom type ecpaConfigStreamInnerVlanEtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EcpaConfigStreamInnerVlanEtherType_Type.__name__ = "Integer32"
_EcpaConfigStreamInnerVlanEtherType_Object = MibTableColumn
ecpaConfigStreamInnerVlanEtherType = _EcpaConfigStreamInnerVlanEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 2, 1, 16),
    _EcpaConfigStreamInnerVlanEtherType_Type()
)
ecpaConfigStreamInnerVlanEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaConfigStreamInnerVlanEtherType.setStatus("current")
_EcpaConfigStreamIpVersion_Type = IpVersion
_EcpaConfigStreamIpVersion_Object = MibTableColumn
ecpaConfigStreamIpVersion = _EcpaConfigStreamIpVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 2, 1, 17),
    _EcpaConfigStreamIpVersion_Type()
)
ecpaConfigStreamIpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaConfigStreamIpVersion.setStatus("current")
_EcpaConfigStreamIpV4Address_Type = IpAddress
_EcpaConfigStreamIpV4Address_Object = MibTableColumn
ecpaConfigStreamIpV4Address = _EcpaConfigStreamIpV4Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 2, 1, 18),
    _EcpaConfigStreamIpV4Address_Type()
)
ecpaConfigStreamIpV4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaConfigStreamIpV4Address.setStatus("current")
_EcpaConfigStreamIpV6Address_Type = Ipv6Address
_EcpaConfigStreamIpV6Address_Object = MibTableColumn
ecpaConfigStreamIpV6Address = _EcpaConfigStreamIpV6Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 2, 1, 19),
    _EcpaConfigStreamIpV6Address_Type()
)
ecpaConfigStreamIpV6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaConfigStreamIpV6Address.setStatus("current")
_EcpaConfigStreamPrioMapMode_Type = IpPriorityMapMode
_EcpaConfigStreamPrioMapMode_Object = MibTableColumn
ecpaConfigStreamPrioMapMode = _EcpaConfigStreamPrioMapMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 2, 1, 20),
    _EcpaConfigStreamPrioMapMode_Type()
)
ecpaConfigStreamPrioMapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaConfigStreamPrioMapMode.setStatus("current")


class _EcpaConfigStreamPrioVal_Type(Integer32):
    """Custom type ecpaConfigStreamPrioVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_EcpaConfigStreamPrioVal_Type.__name__ = "Integer32"
_EcpaConfigStreamPrioVal_Object = MibTableColumn
ecpaConfigStreamPrioVal = _EcpaConfigStreamPrioVal_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 2, 1, 21),
    _EcpaConfigStreamPrioVal_Type()
)
ecpaConfigStreamPrioVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaConfigStreamPrioVal.setStatus("current")
_EcpaConfigStreamInnerVlan2Enabled_Type = TruthValue
_EcpaConfigStreamInnerVlan2Enabled_Object = MibTableColumn
ecpaConfigStreamInnerVlan2Enabled = _EcpaConfigStreamInnerVlan2Enabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 2, 1, 22),
    _EcpaConfigStreamInnerVlan2Enabled_Type()
)
ecpaConfigStreamInnerVlan2Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaConfigStreamInnerVlan2Enabled.setStatus("current")
_EcpaConfigStreamInnerVlan2Id_Type = VlanId
_EcpaConfigStreamInnerVlan2Id_Object = MibTableColumn
ecpaConfigStreamInnerVlan2Id = _EcpaConfigStreamInnerVlan2Id_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 2, 1, 23),
    _EcpaConfigStreamInnerVlan2Id_Type()
)
ecpaConfigStreamInnerVlan2Id.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaConfigStreamInnerVlan2Id.setStatus("current")
_EcpaConfigStreamInnerVlan2Prio_Type = VlanPriority
_EcpaConfigStreamInnerVlan2Prio_Object = MibTableColumn
ecpaConfigStreamInnerVlan2Prio = _EcpaConfigStreamInnerVlan2Prio_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 2, 1, 24),
    _EcpaConfigStreamInnerVlan2Prio_Type()
)
ecpaConfigStreamInnerVlan2Prio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaConfigStreamInnerVlan2Prio.setStatus("current")


class _EcpaConfigStreamInnerVlan2EtherType_Type(Integer32):
    """Custom type ecpaConfigStreamInnerVlan2EtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EcpaConfigStreamInnerVlan2EtherType_Type.__name__ = "Integer32"
_EcpaConfigStreamInnerVlan2EtherType_Object = MibTableColumn
ecpaConfigStreamInnerVlan2EtherType = _EcpaConfigStreamInnerVlan2EtherType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 2, 1, 25),
    _EcpaConfigStreamInnerVlan2EtherType_Type()
)
ecpaConfigStreamInnerVlan2EtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaConfigStreamInnerVlan2EtherType.setStatus("current")
_EcpaConfigStreamDestIpV4Address_Type = IpAddress
_EcpaConfigStreamDestIpV4Address_Object = MibTableColumn
ecpaConfigStreamDestIpV4Address = _EcpaConfigStreamDestIpV4Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 2, 1, 26),
    _EcpaConfigStreamDestIpV4Address_Type()
)
ecpaConfigStreamDestIpV4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaConfigStreamDestIpV4Address.setStatus("current")
_EcpaConfigStreamDestIpV6Address_Type = Ipv6Address
_EcpaConfigStreamDestIpV6Address_Object = MibTableColumn
ecpaConfigStreamDestIpV6Address = _EcpaConfigStreamDestIpV6Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 2, 1, 27),
    _EcpaConfigStreamDestIpV6Address_Type()
)
ecpaConfigStreamDestIpV6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaConfigStreamDestIpV6Address.setStatus("current")
_EcpaConfigStreamUsePortSourceMAC_Type = TruthValue
_EcpaConfigStreamUsePortSourceMAC_Object = MibTableColumn
ecpaConfigStreamUsePortSourceMAC = _EcpaConfigStreamUsePortSourceMAC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 2, 1, 28),
    _EcpaConfigStreamUsePortSourceMAC_Type()
)
ecpaConfigStreamUsePortSourceMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaConfigStreamUsePortSourceMAC.setStatus("current")
_EcpaConfigStreamRateHi_Type = Unsigned32
_EcpaConfigStreamRateHi_Object = MibTableColumn
ecpaConfigStreamRateHi = _EcpaConfigStreamRateHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 2, 1, 29),
    _EcpaConfigStreamRateHi_Type()
)
ecpaConfigStreamRateHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaConfigStreamRateHi.setStatus("current")
_EcpaConfigStreamUdpControl_Type = TruthValue
_EcpaConfigStreamUdpControl_Object = MibTableColumn
ecpaConfigStreamUdpControl = _EcpaConfigStreamUdpControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 2, 1, 30),
    _EcpaConfigStreamUdpControl_Type()
)
ecpaConfigStreamUdpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaConfigStreamUdpControl.setStatus("current")


class _EcpaConfigStreamUdpSrcPort_Type(Integer32):
    """Custom type ecpaConfigStreamUdpSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EcpaConfigStreamUdpSrcPort_Type.__name__ = "Integer32"
_EcpaConfigStreamUdpSrcPort_Object = MibTableColumn
ecpaConfigStreamUdpSrcPort = _EcpaConfigStreamUdpSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 2, 1, 31),
    _EcpaConfigStreamUdpSrcPort_Type()
)
ecpaConfigStreamUdpSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaConfigStreamUdpSrcPort.setStatus("current")


class _EcpaConfigStreamUdpDstPort_Type(Integer32):
    """Custom type ecpaConfigStreamUdpDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EcpaConfigStreamUdpDstPort_Type.__name__ = "Integer32"
_EcpaConfigStreamUdpDstPort_Object = MibTableColumn
ecpaConfigStreamUdpDstPort = _EcpaConfigStreamUdpDstPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 2, 1, 32),
    _EcpaConfigStreamUdpDstPort_Type()
)
ecpaConfigStreamUdpDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaConfigStreamUdpDstPort.setStatus("current")
_EcpaTestStreamTable_Object = MibTable
ecpaTestStreamTable = _EcpaTestStreamTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 3)
)
if mibBuilder.loadTexts:
    ecpaTestStreamTable.setStatus("current")
_EcpaTestStreamEntry_Object = MibTableRow
ecpaTestStreamEntry = _EcpaTestStreamEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 3, 1)
)
ecpaTestStreamEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-SA-MIB", "ecpaControlIndex"),
    (0, "CM-SA-MIB", "ecpaTestStreamIndex"),
)
if mibBuilder.loadTexts:
    ecpaTestStreamEntry.setStatus("current")


class _EcpaTestStreamIndex_Type(Integer32):
    """Custom type ecpaTestStreamIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_EcpaTestStreamIndex_Type.__name__ = "Integer32"
_EcpaTestStreamIndex_Object = MibTableColumn
ecpaTestStreamIndex = _EcpaTestStreamIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 3, 1, 1),
    _EcpaTestStreamIndex_Type()
)
ecpaTestStreamIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpaTestStreamIndex.setStatus("current")
_EcpaTestStreamSourcePort_Type = VariablePointer
_EcpaTestStreamSourcePort_Object = MibTableColumn
ecpaTestStreamSourcePort = _EcpaTestStreamSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 3, 1, 2),
    _EcpaTestStreamSourcePort_Type()
)
ecpaTestStreamSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpaTestStreamSourcePort.setStatus("current")


class _EcpaTestStreamName_Type(DisplayString):
    """Custom type ecpaTestStreamName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EcpaTestStreamName_Type.__name__ = "DisplayString"
_EcpaTestStreamName_Object = MibTableColumn
ecpaTestStreamName = _EcpaTestStreamName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 3, 1, 3),
    _EcpaTestStreamName_Type()
)
ecpaTestStreamName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaTestStreamName.setStatus("current")


class _EcpaTestStreamFrameSize_Type(Integer32):
    """Custom type ecpaTestStreamFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 9612),
    )


_EcpaTestStreamFrameSize_Type.__name__ = "Integer32"
_EcpaTestStreamFrameSize_Object = MibTableColumn
ecpaTestStreamFrameSize = _EcpaTestStreamFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 3, 1, 4),
    _EcpaTestStreamFrameSize_Type()
)
ecpaTestStreamFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaTestStreamFrameSize.setStatus("current")
_EcpaTestStreamRate_Type = Unsigned32
_EcpaTestStreamRate_Object = MibTableColumn
ecpaTestStreamRate = _EcpaTestStreamRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 3, 1, 5),
    _EcpaTestStreamRate_Type()
)
ecpaTestStreamRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaTestStreamRate.setStatus("current")
_EcpaTestStreamPayloadType_Type = EcpaPayloadType
_EcpaTestStreamPayloadType_Object = MibTableColumn
ecpaTestStreamPayloadType = _EcpaTestStreamPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 3, 1, 6),
    _EcpaTestStreamPayloadType_Type()
)
ecpaTestStreamPayloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaTestStreamPayloadType.setStatus("current")


class _EcpaTestStreamSignature_Type(DisplayString):
    """Custom type ecpaTestStreamSignature based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_EcpaTestStreamSignature_Type.__name__ = "DisplayString"
_EcpaTestStreamSignature_Object = MibTableColumn
ecpaTestStreamSignature = _EcpaTestStreamSignature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 3, 1, 7),
    _EcpaTestStreamSignature_Type()
)
ecpaTestStreamSignature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaTestStreamSignature.setStatus("current")
_EcpaTestStreamDestinationMAC_Type = MacAddress
_EcpaTestStreamDestinationMAC_Object = MibTableColumn
ecpaTestStreamDestinationMAC = _EcpaTestStreamDestinationMAC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 3, 1, 8),
    _EcpaTestStreamDestinationMAC_Type()
)
ecpaTestStreamDestinationMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaTestStreamDestinationMAC.setStatus("current")
_EcpaTestStreamSourceMAC_Type = MacAddress
_EcpaTestStreamSourceMAC_Object = MibTableColumn
ecpaTestStreamSourceMAC = _EcpaTestStreamSourceMAC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 3, 1, 9),
    _EcpaTestStreamSourceMAC_Type()
)
ecpaTestStreamSourceMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaTestStreamSourceMAC.setStatus("current")
_EcpaTestStreamOuterVlanEnabled_Type = TruthValue
_EcpaTestStreamOuterVlanEnabled_Object = MibTableColumn
ecpaTestStreamOuterVlanEnabled = _EcpaTestStreamOuterVlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 3, 1, 10),
    _EcpaTestStreamOuterVlanEnabled_Type()
)
ecpaTestStreamOuterVlanEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaTestStreamOuterVlanEnabled.setStatus("current")
_EcpaTestStreamOuterVlanId_Type = VlanId
_EcpaTestStreamOuterVlanId_Object = MibTableColumn
ecpaTestStreamOuterVlanId = _EcpaTestStreamOuterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 3, 1, 11),
    _EcpaTestStreamOuterVlanId_Type()
)
ecpaTestStreamOuterVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaTestStreamOuterVlanId.setStatus("current")
_EcpaTestStreamOuterVlanPrio_Type = VlanPriority
_EcpaTestStreamOuterVlanPrio_Object = MibTableColumn
ecpaTestStreamOuterVlanPrio = _EcpaTestStreamOuterVlanPrio_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 3, 1, 12),
    _EcpaTestStreamOuterVlanPrio_Type()
)
ecpaTestStreamOuterVlanPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaTestStreamOuterVlanPrio.setStatus("current")


class _EcpaTestStreamOuterVlanEtherType_Type(Integer32):
    """Custom type ecpaTestStreamOuterVlanEtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EcpaTestStreamOuterVlanEtherType_Type.__name__ = "Integer32"
_EcpaTestStreamOuterVlanEtherType_Object = MibTableColumn
ecpaTestStreamOuterVlanEtherType = _EcpaTestStreamOuterVlanEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 3, 1, 13),
    _EcpaTestStreamOuterVlanEtherType_Type()
)
ecpaTestStreamOuterVlanEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaTestStreamOuterVlanEtherType.setStatus("current")
_EcpaTestStreamInnerVlanEnabled_Type = TruthValue
_EcpaTestStreamInnerVlanEnabled_Object = MibTableColumn
ecpaTestStreamInnerVlanEnabled = _EcpaTestStreamInnerVlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 3, 1, 14),
    _EcpaTestStreamInnerVlanEnabled_Type()
)
ecpaTestStreamInnerVlanEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaTestStreamInnerVlanEnabled.setStatus("current")
_EcpaTestStreamInnerVlanId_Type = VlanId
_EcpaTestStreamInnerVlanId_Object = MibTableColumn
ecpaTestStreamInnerVlanId = _EcpaTestStreamInnerVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 3, 1, 15),
    _EcpaTestStreamInnerVlanId_Type()
)
ecpaTestStreamInnerVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaTestStreamInnerVlanId.setStatus("current")
_EcpaTestStreamInnerVlanPrio_Type = VlanPriority
_EcpaTestStreamInnerVlanPrio_Object = MibTableColumn
ecpaTestStreamInnerVlanPrio = _EcpaTestStreamInnerVlanPrio_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 3, 1, 16),
    _EcpaTestStreamInnerVlanPrio_Type()
)
ecpaTestStreamInnerVlanPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaTestStreamInnerVlanPrio.setStatus("current")


class _EcpaTestStreamInnerVlanEtherType_Type(Integer32):
    """Custom type ecpaTestStreamInnerVlanEtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EcpaTestStreamInnerVlanEtherType_Type.__name__ = "Integer32"
_EcpaTestStreamInnerVlanEtherType_Object = MibTableColumn
ecpaTestStreamInnerVlanEtherType = _EcpaTestStreamInnerVlanEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 3, 1, 17),
    _EcpaTestStreamInnerVlanEtherType_Type()
)
ecpaTestStreamInnerVlanEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaTestStreamInnerVlanEtherType.setStatus("current")
_EcpaTestStreamIpVersion_Type = IpVersion
_EcpaTestStreamIpVersion_Object = MibTableColumn
ecpaTestStreamIpVersion = _EcpaTestStreamIpVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 3, 1, 18),
    _EcpaTestStreamIpVersion_Type()
)
ecpaTestStreamIpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaTestStreamIpVersion.setStatus("current")
_EcpaTestStreamIpV4Address_Type = IpAddress
_EcpaTestStreamIpV4Address_Object = MibTableColumn
ecpaTestStreamIpV4Address = _EcpaTestStreamIpV4Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 3, 1, 19),
    _EcpaTestStreamIpV4Address_Type()
)
ecpaTestStreamIpV4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaTestStreamIpV4Address.setStatus("current")
_EcpaTestStreamIpV6Address_Type = Ipv6Address
_EcpaTestStreamIpV6Address_Object = MibTableColumn
ecpaTestStreamIpV6Address = _EcpaTestStreamIpV6Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 3, 1, 20),
    _EcpaTestStreamIpV6Address_Type()
)
ecpaTestStreamIpV6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaTestStreamIpV6Address.setStatus("current")
_EcpaTestStreamPrioMapMode_Type = IpPriorityMapMode
_EcpaTestStreamPrioMapMode_Object = MibTableColumn
ecpaTestStreamPrioMapMode = _EcpaTestStreamPrioMapMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 3, 1, 21),
    _EcpaTestStreamPrioMapMode_Type()
)
ecpaTestStreamPrioMapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaTestStreamPrioMapMode.setStatus("current")


class _EcpaTestStreamPrioVal_Type(Integer32):
    """Custom type ecpaTestStreamPrioVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_EcpaTestStreamPrioVal_Type.__name__ = "Integer32"
_EcpaTestStreamPrioVal_Object = MibTableColumn
ecpaTestStreamPrioVal = _EcpaTestStreamPrioVal_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 3, 1, 22),
    _EcpaTestStreamPrioVal_Type()
)
ecpaTestStreamPrioVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaTestStreamPrioVal.setStatus("current")
_EcpaTestStreamMonStartTime_Type = DateAndTime
_EcpaTestStreamMonStartTime_Object = MibTableColumn
ecpaTestStreamMonStartTime = _EcpaTestStreamMonStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 3, 1, 23),
    _EcpaTestStreamMonStartTime_Type()
)
ecpaTestStreamMonStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpaTestStreamMonStartTime.setStatus("current")
_EcpaTestStreamMonEndTime_Type = DateAndTime
_EcpaTestStreamMonEndTime_Object = MibTableColumn
ecpaTestStreamMonEndTime = _EcpaTestStreamMonEndTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 3, 1, 24),
    _EcpaTestStreamMonEndTime_Type()
)
ecpaTestStreamMonEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpaTestStreamMonEndTime.setStatus("current")
_EcpaTestStreamMonElapsedTime_Type = Integer32
_EcpaTestStreamMonElapsedTime_Object = MibTableColumn
ecpaTestStreamMonElapsedTime = _EcpaTestStreamMonElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 3, 1, 25),
    _EcpaTestStreamMonElapsedTime_Type()
)
ecpaTestStreamMonElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpaTestStreamMonElapsedTime.setStatus("current")
_EcpaTestStreamMonTxFrames_Type = PerfCounter64
_EcpaTestStreamMonTxFrames_Object = MibTableColumn
ecpaTestStreamMonTxFrames = _EcpaTestStreamMonTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 3, 1, 26),
    _EcpaTestStreamMonTxFrames_Type()
)
ecpaTestStreamMonTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpaTestStreamMonTxFrames.setStatus("current")
_EcpaTestStreamMonRxFrames_Type = PerfCounter64
_EcpaTestStreamMonRxFrames_Object = MibTableColumn
ecpaTestStreamMonRxFrames = _EcpaTestStreamMonRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 3, 1, 27),
    _EcpaTestStreamMonRxFrames_Type()
)
ecpaTestStreamMonRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpaTestStreamMonRxFrames.setStatus("current")
_EcpaTestStreamMonRxPercentSuccess_Type = Integer32
_EcpaTestStreamMonRxPercentSuccess_Object = MibTableColumn
ecpaTestStreamMonRxPercentSuccess = _EcpaTestStreamMonRxPercentSuccess_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 3, 1, 28),
    _EcpaTestStreamMonRxPercentSuccess_Type()
)
ecpaTestStreamMonRxPercentSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpaTestStreamMonRxPercentSuccess.setStatus("current")
_EcpaTestStreamMonRxOutOfSeqErrs_Type = PerfCounter64
_EcpaTestStreamMonRxOutOfSeqErrs_Object = MibTableColumn
ecpaTestStreamMonRxOutOfSeqErrs = _EcpaTestStreamMonRxOutOfSeqErrs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 3, 1, 29),
    _EcpaTestStreamMonRxOutOfSeqErrs_Type()
)
ecpaTestStreamMonRxOutOfSeqErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpaTestStreamMonRxOutOfSeqErrs.setStatus("current")
_EcpaTestStreamMonRxSeqGaps_Type = PerfCounter64
_EcpaTestStreamMonRxSeqGaps_Object = MibTableColumn
ecpaTestStreamMonRxSeqGaps = _EcpaTestStreamMonRxSeqGaps_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 3, 1, 30),
    _EcpaTestStreamMonRxSeqGaps_Type()
)
ecpaTestStreamMonRxSeqGaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpaTestStreamMonRxSeqGaps.setStatus("current")
_EcpaTestStreamMonRxNonEcpaFrames_Type = PerfCounter64
_EcpaTestStreamMonRxNonEcpaFrames_Object = MibTableColumn
ecpaTestStreamMonRxNonEcpaFrames = _EcpaTestStreamMonRxNonEcpaFrames_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 3, 1, 31),
    _EcpaTestStreamMonRxNonEcpaFrames_Type()
)
ecpaTestStreamMonRxNonEcpaFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpaTestStreamMonRxNonEcpaFrames.setStatus("current")
_EcpaTestStreamMonRxMinDelay_Type = Unsigned32
_EcpaTestStreamMonRxMinDelay_Object = MibTableColumn
ecpaTestStreamMonRxMinDelay = _EcpaTestStreamMonRxMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 3, 1, 32),
    _EcpaTestStreamMonRxMinDelay_Type()
)
ecpaTestStreamMonRxMinDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpaTestStreamMonRxMinDelay.setStatus("current")
_EcpaTestStreamMonRxMaxDelay_Type = Unsigned32
_EcpaTestStreamMonRxMaxDelay_Object = MibTableColumn
ecpaTestStreamMonRxMaxDelay = _EcpaTestStreamMonRxMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 3, 1, 33),
    _EcpaTestStreamMonRxMaxDelay_Type()
)
ecpaTestStreamMonRxMaxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpaTestStreamMonRxMaxDelay.setStatus("current")
_EcpaTestStreamMonRxAvgDelay_Type = Unsigned32
_EcpaTestStreamMonRxAvgDelay_Object = MibTableColumn
ecpaTestStreamMonRxAvgDelay = _EcpaTestStreamMonRxAvgDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 3, 1, 34),
    _EcpaTestStreamMonRxAvgDelay_Type()
)
ecpaTestStreamMonRxAvgDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpaTestStreamMonRxAvgDelay.setStatus("current")


class _EcpaTestStreamMonRx1stFrameSize_Type(Integer32):
    """Custom type ecpaTestStreamMonRx1stFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 9612),
    )


_EcpaTestStreamMonRx1stFrameSize_Type.__name__ = "Integer32"
_EcpaTestStreamMonRx1stFrameSize_Object = MibTableColumn
ecpaTestStreamMonRx1stFrameSize = _EcpaTestStreamMonRx1stFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 3, 1, 35),
    _EcpaTestStreamMonRx1stFrameSize_Type()
)
ecpaTestStreamMonRx1stFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpaTestStreamMonRx1stFrameSize.setStatus("current")


class _EcpaTestStreamMonRx1stFrame1Octets_Type(DisplayString):
    """Custom type ecpaTestStreamMonRx1stFrame1Octets based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2048),
    )


_EcpaTestStreamMonRx1stFrame1Octets_Type.__name__ = "DisplayString"
_EcpaTestStreamMonRx1stFrame1Octets_Object = MibTableColumn
ecpaTestStreamMonRx1stFrame1Octets = _EcpaTestStreamMonRx1stFrame1Octets_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 3, 1, 36),
    _EcpaTestStreamMonRx1stFrame1Octets_Type()
)
ecpaTestStreamMonRx1stFrame1Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpaTestStreamMonRx1stFrame1Octets.setStatus("current")


class _EcpaTestStreamMonRx1stFrame2Octets_Type(DisplayString):
    """Custom type ecpaTestStreamMonRx1stFrame2Octets based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2048),
    )


_EcpaTestStreamMonRx1stFrame2Octets_Type.__name__ = "DisplayString"
_EcpaTestStreamMonRx1stFrame2Octets_Object = MibTableColumn
ecpaTestStreamMonRx1stFrame2Octets = _EcpaTestStreamMonRx1stFrame2Octets_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 3, 1, 37),
    _EcpaTestStreamMonRx1stFrame2Octets_Type()
)
ecpaTestStreamMonRx1stFrame2Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpaTestStreamMonRx1stFrame2Octets.setStatus("current")


class _EcpaTestStreamMonRx1stFrame3Octets_Type(DisplayString):
    """Custom type ecpaTestStreamMonRx1stFrame3Octets based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2048),
    )


_EcpaTestStreamMonRx1stFrame3Octets_Type.__name__ = "DisplayString"
_EcpaTestStreamMonRx1stFrame3Octets_Object = MibTableColumn
ecpaTestStreamMonRx1stFrame3Octets = _EcpaTestStreamMonRx1stFrame3Octets_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 3, 1, 38),
    _EcpaTestStreamMonRx1stFrame3Octets_Type()
)
ecpaTestStreamMonRx1stFrame3Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpaTestStreamMonRx1stFrame3Octets.setStatus("current")


class _EcpaTestStreamMonRx1stFrame4Octets_Type(DisplayString):
    """Custom type ecpaTestStreamMonRx1stFrame4Octets based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2048),
    )


_EcpaTestStreamMonRx1stFrame4Octets_Type.__name__ = "DisplayString"
_EcpaTestStreamMonRx1stFrame4Octets_Object = MibTableColumn
ecpaTestStreamMonRx1stFrame4Octets = _EcpaTestStreamMonRx1stFrame4Octets_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 3, 1, 39),
    _EcpaTestStreamMonRx1stFrame4Octets_Type()
)
ecpaTestStreamMonRx1stFrame4Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpaTestStreamMonRx1stFrame4Octets.setStatus("current")


class _EcpaTestStreamMonRx1stFrame5Octets_Type(DisplayString):
    """Custom type ecpaTestStreamMonRx1stFrame5Octets based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2048),
    )


_EcpaTestStreamMonRx1stFrame5Octets_Type.__name__ = "DisplayString"
_EcpaTestStreamMonRx1stFrame5Octets_Object = MibTableColumn
ecpaTestStreamMonRx1stFrame5Octets = _EcpaTestStreamMonRx1stFrame5Octets_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 3, 1, 40),
    _EcpaTestStreamMonRx1stFrame5Octets_Type()
)
ecpaTestStreamMonRx1stFrame5Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpaTestStreamMonRx1stFrame5Octets.setStatus("current")


class _EcpaTestStreamMonRx1stFrame6Octets_Type(DisplayString):
    """Custom type ecpaTestStreamMonRx1stFrame6Octets based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2048),
    )


_EcpaTestStreamMonRx1stFrame6Octets_Type.__name__ = "DisplayString"
_EcpaTestStreamMonRx1stFrame6Octets_Object = MibTableColumn
ecpaTestStreamMonRx1stFrame6Octets = _EcpaTestStreamMonRx1stFrame6Octets_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 3, 1, 41),
    _EcpaTestStreamMonRx1stFrame6Octets_Type()
)
ecpaTestStreamMonRx1stFrame6Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpaTestStreamMonRx1stFrame6Octets.setStatus("current")


class _EcpaTestStreamMonRx1stFrame7Octets_Type(DisplayString):
    """Custom type ecpaTestStreamMonRx1stFrame7Octets based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2048),
    )


_EcpaTestStreamMonRx1stFrame7Octets_Type.__name__ = "DisplayString"
_EcpaTestStreamMonRx1stFrame7Octets_Object = MibTableColumn
ecpaTestStreamMonRx1stFrame7Octets = _EcpaTestStreamMonRx1stFrame7Octets_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 3, 1, 42),
    _EcpaTestStreamMonRx1stFrame7Octets_Type()
)
ecpaTestStreamMonRx1stFrame7Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpaTestStreamMonRx1stFrame7Octets.setStatus("current")


class _EcpaTestStreamMonRx1stFrame8Octets_Type(DisplayString):
    """Custom type ecpaTestStreamMonRx1stFrame8Octets based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2048),
    )


_EcpaTestStreamMonRx1stFrame8Octets_Type.__name__ = "DisplayString"
_EcpaTestStreamMonRx1stFrame8Octets_Object = MibTableColumn
ecpaTestStreamMonRx1stFrame8Octets = _EcpaTestStreamMonRx1stFrame8Octets_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 3, 1, 43),
    _EcpaTestStreamMonRx1stFrame8Octets_Type()
)
ecpaTestStreamMonRx1stFrame8Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpaTestStreamMonRx1stFrame8Octets.setStatus("current")


class _EcpaTestStreamMonRx1stFrame9Octets_Type(DisplayString):
    """Custom type ecpaTestStreamMonRx1stFrame9Octets based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2048),
    )


_EcpaTestStreamMonRx1stFrame9Octets_Type.__name__ = "DisplayString"
_EcpaTestStreamMonRx1stFrame9Octets_Object = MibTableColumn
ecpaTestStreamMonRx1stFrame9Octets = _EcpaTestStreamMonRx1stFrame9Octets_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 3, 1, 44),
    _EcpaTestStreamMonRx1stFrame9Octets_Type()
)
ecpaTestStreamMonRx1stFrame9Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpaTestStreamMonRx1stFrame9Octets.setStatus("current")


class _EcpaTestStreamMonRx1stFrame10Octets_Type(DisplayString):
    """Custom type ecpaTestStreamMonRx1stFrame10Octets based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2048),
    )


_EcpaTestStreamMonRx1stFrame10Octets_Type.__name__ = "DisplayString"
_EcpaTestStreamMonRx1stFrame10Octets_Object = MibTableColumn
ecpaTestStreamMonRx1stFrame10Octets = _EcpaTestStreamMonRx1stFrame10Octets_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 3, 1, 45),
    _EcpaTestStreamMonRx1stFrame10Octets_Type()
)
ecpaTestStreamMonRx1stFrame10Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpaTestStreamMonRx1stFrame10Octets.setStatus("current")
_EcpaTestStreamMonRxBitRate_Type = PerfCounter64
_EcpaTestStreamMonRxBitRate_Object = MibTableColumn
ecpaTestStreamMonRxBitRate = _EcpaTestStreamMonRxBitRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 3, 1, 46),
    _EcpaTestStreamMonRxBitRate_Type()
)
ecpaTestStreamMonRxBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpaTestStreamMonRxBitRate.setStatus("current")
_EcpaTestStreamInnerVlan2Enabled_Type = TruthValue
_EcpaTestStreamInnerVlan2Enabled_Object = MibTableColumn
ecpaTestStreamInnerVlan2Enabled = _EcpaTestStreamInnerVlan2Enabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 3, 1, 47),
    _EcpaTestStreamInnerVlan2Enabled_Type()
)
ecpaTestStreamInnerVlan2Enabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpaTestStreamInnerVlan2Enabled.setStatus("current")
_EcpaTestStreamInnerVlan2Id_Type = VlanId
_EcpaTestStreamInnerVlan2Id_Object = MibTableColumn
ecpaTestStreamInnerVlan2Id = _EcpaTestStreamInnerVlan2Id_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 3, 1, 48),
    _EcpaTestStreamInnerVlan2Id_Type()
)
ecpaTestStreamInnerVlan2Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpaTestStreamInnerVlan2Id.setStatus("current")
_EcpaTestStreamInnerVlan2Prio_Type = VlanPriority
_EcpaTestStreamInnerVlan2Prio_Object = MibTableColumn
ecpaTestStreamInnerVlan2Prio = _EcpaTestStreamInnerVlan2Prio_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 3, 1, 49),
    _EcpaTestStreamInnerVlan2Prio_Type()
)
ecpaTestStreamInnerVlan2Prio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpaTestStreamInnerVlan2Prio.setStatus("current")


class _EcpaTestStreamInnerVlan2EtherType_Type(Integer32):
    """Custom type ecpaTestStreamInnerVlan2EtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EcpaTestStreamInnerVlan2EtherType_Type.__name__ = "Integer32"
_EcpaTestStreamInnerVlan2EtherType_Object = MibTableColumn
ecpaTestStreamInnerVlan2EtherType = _EcpaTestStreamInnerVlan2EtherType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 3, 1, 50),
    _EcpaTestStreamInnerVlan2EtherType_Type()
)
ecpaTestStreamInnerVlan2EtherType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpaTestStreamInnerVlan2EtherType.setStatus("current")
_EcpaTestStreamDestIpV4Address_Type = IpAddress
_EcpaTestStreamDestIpV4Address_Object = MibTableColumn
ecpaTestStreamDestIpV4Address = _EcpaTestStreamDestIpV4Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 3, 1, 51),
    _EcpaTestStreamDestIpV4Address_Type()
)
ecpaTestStreamDestIpV4Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpaTestStreamDestIpV4Address.setStatus("current")
_EcpaTestStreamDestIpV6Address_Type = Ipv6Address
_EcpaTestStreamDestIpV6Address_Object = MibTableColumn
ecpaTestStreamDestIpV6Address = _EcpaTestStreamDestIpV6Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 3, 1, 52),
    _EcpaTestStreamDestIpV6Address_Type()
)
ecpaTestStreamDestIpV6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpaTestStreamDestIpV6Address.setStatus("current")
_EcpaTestStreamConfigChanged_Type = TruthValue
_EcpaTestStreamConfigChanged_Object = MibTableColumn
ecpaTestStreamConfigChanged = _EcpaTestStreamConfigChanged_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 3, 1, 53),
    _EcpaTestStreamConfigChanged_Type()
)
ecpaTestStreamConfigChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpaTestStreamConfigChanged.setStatus("current")
_EcpaTestStreamRateHi_Type = Unsigned32
_EcpaTestStreamRateHi_Object = MibTableColumn
ecpaTestStreamRateHi = _EcpaTestStreamRateHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 3, 1, 54),
    _EcpaTestStreamRateHi_Type()
)
ecpaTestStreamRateHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaTestStreamRateHi.setStatus("current")
_EcpaTestStreamUdpControl_Type = TruthValue
_EcpaTestStreamUdpControl_Object = MibTableColumn
ecpaTestStreamUdpControl = _EcpaTestStreamUdpControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 3, 1, 55),
    _EcpaTestStreamUdpControl_Type()
)
ecpaTestStreamUdpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaTestStreamUdpControl.setStatus("current")


class _EcpaTestStreamUdpSrcPort_Type(Integer32):
    """Custom type ecpaTestStreamUdpSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EcpaTestStreamUdpSrcPort_Type.__name__ = "Integer32"
_EcpaTestStreamUdpSrcPort_Object = MibTableColumn
ecpaTestStreamUdpSrcPort = _EcpaTestStreamUdpSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 3, 1, 56),
    _EcpaTestStreamUdpSrcPort_Type()
)
ecpaTestStreamUdpSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaTestStreamUdpSrcPort.setStatus("current")


class _EcpaTestStreamUdpDstPort_Type(Integer32):
    """Custom type ecpaTestStreamUdpDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EcpaTestStreamUdpDstPort_Type.__name__ = "Integer32"
_EcpaTestStreamUdpDstPort_Object = MibTableColumn
ecpaTestStreamUdpDstPort = _EcpaTestStreamUdpDstPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 3, 1, 57),
    _EcpaTestStreamUdpDstPort_Type()
)
ecpaTestStreamUdpDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpaTestStreamUdpDstPort.setStatus("current")
_EsaProbeTable_Object = MibTable
esaProbeTable = _EsaProbeTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 4)
)
if mibBuilder.loadTexts:
    esaProbeTable.setStatus("current")
_EsaProbeEntry_Object = MibTableRow
esaProbeEntry = _EsaProbeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 4, 1)
)
esaProbeEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-SA-MIB", "esaProbeIndex"),
)
if mibBuilder.loadTexts:
    esaProbeEntry.setStatus("current")
_EsaProbeIndex_Type = Integer32
_EsaProbeIndex_Object = MibTableColumn
esaProbeIndex = _EsaProbeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 4, 1, 1),
    _EsaProbeIndex_Type()
)
esaProbeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeIndex.setStatus("current")


class _EsaProbeName_Type(DisplayString):
    """Custom type esaProbeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_EsaProbeName_Type.__name__ = "DisplayString"
_EsaProbeName_Object = MibTableColumn
esaProbeName = _EsaProbeName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 4, 1, 2),
    _EsaProbeName_Type()
)
esaProbeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esaProbeName.setStatus("current")
_EsaProbeSourcePort_Type = VariablePointer
_EsaProbeSourcePort_Object = MibTableColumn
esaProbeSourcePort = _EsaProbeSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 4, 1, 3),
    _EsaProbeSourcePort_Type()
)
esaProbeSourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esaProbeSourcePort.setStatus("current")
_EsaProbeAssocSchedGroup_Type = VariablePointer
_EsaProbeAssocSchedGroup_Object = MibTableColumn
esaProbeAssocSchedGroup = _EsaProbeAssocSchedGroup_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 4, 1, 4),
    _EsaProbeAssocSchedGroup_Type()
)
esaProbeAssocSchedGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeAssocSchedGroup.setStatus("current")
_EsaProbeDirection_Type = EsaProbeDirection
_EsaProbeDirection_Object = MibTableColumn
esaProbeDirection = _EsaProbeDirection_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 4, 1, 5),
    _EsaProbeDirection_Type()
)
esaProbeDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esaProbeDirection.setStatus("current")
_EsaProbeProtocol_Type = EsaProbeProtocol
_EsaProbeProtocol_Object = MibTableColumn
esaProbeProtocol = _EsaProbeProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 4, 1, 6),
    _EsaProbeProtocol_Type()
)
esaProbeProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esaProbeProtocol.setStatus("current")
_EsaProbeSrcIpAddress_Type = IpAddress
_EsaProbeSrcIpAddress_Object = MibTableColumn
esaProbeSrcIpAddress = _EsaProbeSrcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 4, 1, 7),
    _EsaProbeSrcIpAddress_Type()
)
esaProbeSrcIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esaProbeSrcIpAddress.setStatus("current")
_EsaProbeSrcSubnetMask_Type = IpAddress
_EsaProbeSrcSubnetMask_Object = MibTableColumn
esaProbeSrcSubnetMask = _EsaProbeSrcSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 4, 1, 8),
    _EsaProbeSrcSubnetMask_Type()
)
esaProbeSrcSubnetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esaProbeSrcSubnetMask.setStatus("current")
_EsaProbeDestIpAddress_Type = IpAddress
_EsaProbeDestIpAddress_Object = MibTableColumn
esaProbeDestIpAddress = _EsaProbeDestIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 4, 1, 9),
    _EsaProbeDestIpAddress_Type()
)
esaProbeDestIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esaProbeDestIpAddress.setStatus("current")
_EsaProbeSrcMep_Type = VariablePointer
_EsaProbeSrcMep_Object = MibTableColumn
esaProbeSrcMep = _EsaProbeSrcMep_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 4, 1, 10),
    _EsaProbeSrcMep_Type()
)
esaProbeSrcMep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esaProbeSrcMep.setStatus("current")
_EsaProbeDestMepType_Type = MepDestinationType
_EsaProbeDestMepType_Object = MibTableColumn
esaProbeDestMepType = _EsaProbeDestMepType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 4, 1, 11),
    _EsaProbeDestMepType_Type()
)
esaProbeDestMepType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esaProbeDestMepType.setStatus("current")
_EsaProbeDestMepMacAddr_Type = MacAddress
_EsaProbeDestMepMacAddr_Object = MibTableColumn
esaProbeDestMepMacAddr = _EsaProbeDestMepMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 4, 1, 12),
    _EsaProbeDestMepMacAddr_Type()
)
esaProbeDestMepMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esaProbeDestMepMacAddr.setStatus("current")
_EsaProbeDestMepId_Type = Dot1agCfmMepIdOrZero
_EsaProbeDestMepId_Object = MibTableColumn
esaProbeDestMepId = _EsaProbeDestMepId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 4, 1, 13),
    _EsaProbeDestMepId_Type()
)
esaProbeDestMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esaProbeDestMepId.setStatus("current")
_EsaProbeVlanTagEnabled_Type = TruthValue
_EsaProbeVlanTagEnabled_Object = MibTableColumn
esaProbeVlanTagEnabled = _EsaProbeVlanTagEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 4, 1, 14),
    _EsaProbeVlanTagEnabled_Type()
)
esaProbeVlanTagEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esaProbeVlanTagEnabled.setStatus("current")
_EsaProbeVlanTagEtherType_Type = Unsigned32
_EsaProbeVlanTagEtherType_Object = MibTableColumn
esaProbeVlanTagEtherType = _EsaProbeVlanTagEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 4, 1, 15),
    _EsaProbeVlanTagEtherType_Type()
)
esaProbeVlanTagEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esaProbeVlanTagEtherType.setStatus("current")
_EsaProbeVlanId_Type = VlanId
_EsaProbeVlanId_Object = MibTableColumn
esaProbeVlanId = _EsaProbeVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 4, 1, 16),
    _EsaProbeVlanId_Type()
)
esaProbeVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esaProbeVlanId.setStatus("current")
_EsaProbeVlanPrio_Type = VlanPriority
_EsaProbeVlanPrio_Object = MibTableColumn
esaProbeVlanPrio = _EsaProbeVlanPrio_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 4, 1, 17),
    _EsaProbeVlanPrio_Type()
)
esaProbeVlanPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esaProbeVlanPrio.setStatus("current")
_EsaProbeInnerVlanTagEnabled_Type = TruthValue
_EsaProbeInnerVlanTagEnabled_Object = MibTableColumn
esaProbeInnerVlanTagEnabled = _EsaProbeInnerVlanTagEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 4, 1, 18),
    _EsaProbeInnerVlanTagEnabled_Type()
)
esaProbeInnerVlanTagEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esaProbeInnerVlanTagEnabled.setStatus("current")
_EsaProbeInnerVlanTagEtherType_Type = Unsigned32
_EsaProbeInnerVlanTagEtherType_Object = MibTableColumn
esaProbeInnerVlanTagEtherType = _EsaProbeInnerVlanTagEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 4, 1, 19),
    _EsaProbeInnerVlanTagEtherType_Type()
)
esaProbeInnerVlanTagEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esaProbeInnerVlanTagEtherType.setStatus("current")
_EsaProbeInnerVlanId_Type = VlanId
_EsaProbeInnerVlanId_Object = MibTableColumn
esaProbeInnerVlanId = _EsaProbeInnerVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 4, 1, 20),
    _EsaProbeInnerVlanId_Type()
)
esaProbeInnerVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esaProbeInnerVlanId.setStatus("current")
_EsaProbeInnerVlanPrio_Type = VlanPriority
_EsaProbeInnerVlanPrio_Object = MibTableColumn
esaProbeInnerVlanPrio = _EsaProbeInnerVlanPrio_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 4, 1, 21),
    _EsaProbeInnerVlanPrio_Type()
)
esaProbeInnerVlanPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esaProbeInnerVlanPrio.setStatus("current")
_EsaProbeIpPrioMapMode_Type = IpPriorityMapMode
_EsaProbeIpPrioMapMode_Object = MibTableColumn
esaProbeIpPrioMapMode = _EsaProbeIpPrioMapMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 4, 1, 22),
    _EsaProbeIpPrioMapMode_Type()
)
esaProbeIpPrioMapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esaProbeIpPrioMapMode.setStatus("current")


class _EsaProbeIpPriority_Type(Integer32):
    """Custom type esaProbeIpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_EsaProbeIpPriority_Type.__name__ = "Integer32"
_EsaProbeIpPriority_Object = MibTableColumn
esaProbeIpPriority = _EsaProbeIpPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 4, 1, 23),
    _EsaProbeIpPriority_Type()
)
esaProbeIpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esaProbeIpPriority.setStatus("current")
_EsaProbePktsPerSample_Type = Integer32
_EsaProbePktsPerSample_Object = MibTableColumn
esaProbePktsPerSample = _EsaProbePktsPerSample_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 4, 1, 24),
    _EsaProbePktsPerSample_Type()
)
esaProbePktsPerSample.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esaProbePktsPerSample.setStatus("current")


class _EsaProbePktSize_Type(Integer32):
    """Custom type esaProbePktSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(64, 2000),
    )


_EsaProbePktSize_Type.__name__ = "Integer32"
_EsaProbePktSize_Object = MibTableColumn
esaProbePktSize = _EsaProbePktSize_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 4, 1, 25),
    _EsaProbePktSize_Type()
)
esaProbePktSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esaProbePktSize.setStatus("current")
_EsaProbeInterPktGap_Type = Integer32
_EsaProbeInterPktGap_Object = MibTableColumn
esaProbeInterPktGap = _EsaProbeInterPktGap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 4, 1, 26),
    _EsaProbeInterPktGap_Type()
)
esaProbeInterPktGap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esaProbeInterPktGap.setStatus("current")
_EsaProbePktDeadInterval_Type = Integer32
_EsaProbePktDeadInterval_Object = MibTableColumn
esaProbePktDeadInterval = _EsaProbePktDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 4, 1, 27),
    _EsaProbePktDeadInterval_Type()
)
esaProbePktDeadInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esaProbePktDeadInterval.setStatus("current")
_EsaProbeResponseTimeout_Type = Integer32
_EsaProbeResponseTimeout_Object = MibTableColumn
esaProbeResponseTimeout = _EsaProbeResponseTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 4, 1, 28),
    _EsaProbeResponseTimeout_Type()
)
esaProbeResponseTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esaProbeResponseTimeout.setStatus("current")


class _EsaProbeY1731DmmPktSize_Type(Integer32):
    """Custom type esaProbeY1731DmmPktSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(64, 9600),
    )


_EsaProbeY1731DmmPktSize_Type.__name__ = "Integer32"
_EsaProbeY1731DmmPktSize_Object = MibTableColumn
esaProbeY1731DmmPktSize = _EsaProbeY1731DmmPktSize_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 4, 1, 29),
    _EsaProbeY1731DmmPktSize_Type()
)
esaProbeY1731DmmPktSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esaProbeY1731DmmPktSize.setStatus("current")


class _EsaProbeY1731LmmInterval_Type(EsaProbePktIntervalType):
    """Custom type esaProbeY1731LmmInterval based on EsaProbePktIntervalType"""
    defaultValue = 3


_EsaProbeY1731LmmInterval_Type.__name__ = "EsaProbePktIntervalType"
_EsaProbeY1731LmmInterval_Object = MibTableColumn
esaProbeY1731LmmInterval = _EsaProbeY1731LmmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 4, 1, 30),
    _EsaProbeY1731LmmInterval_Type()
)
esaProbeY1731LmmInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esaProbeY1731LmmInterval.setStatus("current")


class _EsaProbeY1731DmmInterval_Type(EsaProbePktIntervalType):
    """Custom type esaProbeY1731DmmInterval based on EsaProbePktIntervalType"""
    defaultValue = 2


_EsaProbeY1731DmmInterval_Type.__name__ = "EsaProbePktIntervalType"
_EsaProbeY1731DmmInterval_Object = MibTableColumn
esaProbeY1731DmmInterval = _EsaProbeY1731DmmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 4, 1, 31),
    _EsaProbeY1731DmmInterval_Type()
)
esaProbeY1731DmmInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esaProbeY1731DmmInterval.setStatus("current")


class _EsaProbeHistoryBins_Type(Integer32):
    """Custom type esaProbeHistoryBins based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_EsaProbeHistoryBins_Type.__name__ = "Integer32"
_EsaProbeHistoryBins_Object = MibTableColumn
esaProbeHistoryBins = _EsaProbeHistoryBins_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 4, 1, 32),
    _EsaProbeHistoryBins_Type()
)
esaProbeHistoryBins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esaProbeHistoryBins.setStatus("current")
_EsaProbeHistoryInterval_Type = EsaProbeHistoryIntervalType
_EsaProbeHistoryInterval_Object = MibTableColumn
esaProbeHistoryInterval = _EsaProbeHistoryInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 4, 1, 33),
    _EsaProbeHistoryInterval_Type()
)
esaProbeHistoryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esaProbeHistoryInterval.setStatus("current")


class _EsaProbeDistHistoryBins_Type(Integer32):
    """Custom type esaProbeDistHistoryBins based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_EsaProbeDistHistoryBins_Type.__name__ = "Integer32"
_EsaProbeDistHistoryBins_Object = MibTableColumn
esaProbeDistHistoryBins = _EsaProbeDistHistoryBins_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 4, 1, 34),
    _EsaProbeDistHistoryBins_Type()
)
esaProbeDistHistoryBins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esaProbeDistHistoryBins.setStatus("current")
_EsaProbeDistHistoryInterval_Type = EsaProbeHistoryIntervalType
_EsaProbeDistHistoryInterval_Object = MibTableColumn
esaProbeDistHistoryInterval = _EsaProbeDistHistoryInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 4, 1, 35),
    _EsaProbeDistHistoryInterval_Type()
)
esaProbeDistHistoryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esaProbeDistHistoryInterval.setStatus("current")
_EsaProbeCreationTime_Type = DateAndTime
_EsaProbeCreationTime_Object = MibTableColumn
esaProbeCreationTime = _EsaProbeCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 4, 1, 36),
    _EsaProbeCreationTime_Type()
)
esaProbeCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeCreationTime.setStatus("current")
_EsaProbeStorageType_Type = StorageType
_EsaProbeStorageType_Object = MibTableColumn
esaProbeStorageType = _EsaProbeStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 4, 1, 37),
    _EsaProbeStorageType_Type()
)
esaProbeStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esaProbeStorageType.setStatus("current")
_EsaProbeRowStatus_Type = RowStatus
_EsaProbeRowStatus_Object = MibTableColumn
esaProbeRowStatus = _EsaProbeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 4, 1, 38),
    _EsaProbeRowStatus_Type()
)
esaProbeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esaProbeRowStatus.setStatus("current")
_EsaProbeMultiCOSEnabled_Type = TruthValue
_EsaProbeMultiCOSEnabled_Object = MibTableColumn
esaProbeMultiCOSEnabled = _EsaProbeMultiCOSEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 4, 1, 39),
    _EsaProbeMultiCOSEnabled_Type()
)
esaProbeMultiCOSEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esaProbeMultiCOSEnabled.setStatus("current")
_EsaProbeSLAMonitorType_Type = EsaProbeSLAMonitorType
_EsaProbeSLAMonitorType_Object = MibTableColumn
esaProbeSLAMonitorType = _EsaProbeSLAMonitorType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 4, 1, 40),
    _EsaProbeSLAMonitorType_Type()
)
esaProbeSLAMonitorType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esaProbeSLAMonitorType.setStatus("current")
_EsaProbeCOSType_Type = ClassOfServiceType
_EsaProbeCOSType_Object = MibTableColumn
esaProbeCOSType = _EsaProbeCOSType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 4, 1, 41),
    _EsaProbeCOSType_Type()
)
esaProbeCOSType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esaProbeCOSType.setStatus("current")
_EsaProbeSLMMulticastMACEnabled_Type = TruthValue
_EsaProbeSLMMulticastMACEnabled_Object = MibTableColumn
esaProbeSLMMulticastMACEnabled = _EsaProbeSLMMulticastMACEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 4, 1, 42),
    _EsaProbeSLMMulticastMACEnabled_Type()
)
esaProbeSLMMulticastMACEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esaProbeSLMMulticastMACEnabled.setStatus("current")
_EsaProbeSOAMInterval_Type = EsaProbePktIntervalType
_EsaProbeSOAMInterval_Object = MibTableColumn
esaProbeSOAMInterval = _EsaProbeSOAMInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 4, 1, 43),
    _EsaProbeSOAMInterval_Type()
)
esaProbeSOAMInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esaProbeSOAMInterval.setStatus("current")


class _EsaProbeSOAMPktSize_Type(Integer32):
    """Custom type esaProbeSOAMPktSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(64, 9612),
    )


_EsaProbeSOAMPktSize_Type.__name__ = "Integer32"
_EsaProbeSOAMPktSize_Object = MibTableColumn
esaProbeSOAMPktSize = _EsaProbeSOAMPktSize_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 4, 1, 44),
    _EsaProbeSOAMPktSize_Type()
)
esaProbeSOAMPktSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esaProbeSOAMPktSize.setStatus("current")
_EsaProbeInner2VlanTagEnabled_Type = TruthValue
_EsaProbeInner2VlanTagEnabled_Object = MibTableColumn
esaProbeInner2VlanTagEnabled = _EsaProbeInner2VlanTagEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 4, 1, 45),
    _EsaProbeInner2VlanTagEnabled_Type()
)
esaProbeInner2VlanTagEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esaProbeInner2VlanTagEnabled.setStatus("current")
_EsaProbeInner2VlanTagEtherType_Type = Unsigned32
_EsaProbeInner2VlanTagEtherType_Object = MibTableColumn
esaProbeInner2VlanTagEtherType = _EsaProbeInner2VlanTagEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 4, 1, 46),
    _EsaProbeInner2VlanTagEtherType_Type()
)
esaProbeInner2VlanTagEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esaProbeInner2VlanTagEtherType.setStatus("current")
_EsaProbeInner2VlanId_Type = VlanId
_EsaProbeInner2VlanId_Object = MibTableColumn
esaProbeInner2VlanId = _EsaProbeInner2VlanId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 4, 1, 47),
    _EsaProbeInner2VlanId_Type()
)
esaProbeInner2VlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esaProbeInner2VlanId.setStatus("current")
_EsaProbeInner2VlanPrio_Type = VlanPriority
_EsaProbeInner2VlanPrio_Object = MibTableColumn
esaProbeInner2VlanPrio = _EsaProbeInner2VlanPrio_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 4, 1, 48),
    _EsaProbeInner2VlanPrio_Type()
)
esaProbeInner2VlanPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esaProbeInner2VlanPrio.setStatus("current")
_EsaProbeAdminState_Type = AdminState
_EsaProbeAdminState_Object = MibTableColumn
esaProbeAdminState = _EsaProbeAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 4, 1, 49),
    _EsaProbeAdminState_Type()
)
esaProbeAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeAdminState.setStatus("current")
_EsaProbeOperationalState_Type = OperationalState
_EsaProbeOperationalState_Object = MibTableColumn
esaProbeOperationalState = _EsaProbeOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 4, 1, 50),
    _EsaProbeOperationalState_Type()
)
esaProbeOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeOperationalState.setStatus("current")
_EsaProbeSecondaryState_Type = SecondaryState
_EsaProbeSecondaryState_Object = MibTableColumn
esaProbeSecondaryState = _EsaProbeSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 4, 1, 51),
    _EsaProbeSecondaryState_Type()
)
esaProbeSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeSecondaryState.setStatus("current")
_EsaProbeMacAddress_Type = MacAddress
_EsaProbeMacAddress_Object = MibTableColumn
esaProbeMacAddress = _EsaProbeMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 4, 1, 52),
    _EsaProbeMacAddress_Type()
)
esaProbeMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeMacAddress.setStatus("current")


class _EsaProbeAlias_Type(DisplayString):
    """Custom type esaProbeAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EsaProbeAlias_Type.__name__ = "DisplayString"
_EsaProbeAlias_Object = MibTableColumn
esaProbeAlias = _EsaProbeAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 4, 1, 53),
    _EsaProbeAlias_Type()
)
esaProbeAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esaProbeAlias.setStatus("current")
_EsaProbeScheduleGroupTable_Object = MibTable
esaProbeScheduleGroupTable = _EsaProbeScheduleGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 5)
)
if mibBuilder.loadTexts:
    esaProbeScheduleGroupTable.setStatus("current")
_EsaProbeScheduleGroupEntry_Object = MibTableRow
esaProbeScheduleGroupEntry = _EsaProbeScheduleGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 5, 1)
)
esaProbeScheduleGroupEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-SA-MIB", "esaProbeScheduleGroupIndex"),
)
if mibBuilder.loadTexts:
    esaProbeScheduleGroupEntry.setStatus("current")
_EsaProbeScheduleGroupIndex_Type = Integer32
_EsaProbeScheduleGroupIndex_Object = MibTableColumn
esaProbeScheduleGroupIndex = _EsaProbeScheduleGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 5, 1, 1),
    _EsaProbeScheduleGroupIndex_Type()
)
esaProbeScheduleGroupIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esaProbeScheduleGroupIndex.setStatus("current")


class _EsaProbeScheduleGroupDescr_Type(DisplayString):
    """Custom type esaProbeScheduleGroupDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_EsaProbeScheduleGroupDescr_Type.__name__ = "DisplayString"
_EsaProbeScheduleGroupDescr_Object = MibTableColumn
esaProbeScheduleGroupDescr = _EsaProbeScheduleGroupDescr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 5, 1, 2),
    _EsaProbeScheduleGroupDescr_Type()
)
esaProbeScheduleGroupDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esaProbeScheduleGroupDescr.setStatus("current")


class _EsaProbeScheduleGroupProbeList_Type(DisplayString):
    """Custom type esaProbeScheduleGroupProbeList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 512),
    )


_EsaProbeScheduleGroupProbeList_Type.__name__ = "DisplayString"
_EsaProbeScheduleGroupProbeList_Object = MibTableColumn
esaProbeScheduleGroupProbeList = _EsaProbeScheduleGroupProbeList_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 5, 1, 3),
    _EsaProbeScheduleGroupProbeList_Type()
)
esaProbeScheduleGroupProbeList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esaProbeScheduleGroupProbeList.setStatus("current")
_EsaProbeScheduleGroupType_Type = ScheduleType
_EsaProbeScheduleGroupType_Object = MibTableColumn
esaProbeScheduleGroupType = _EsaProbeScheduleGroupType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 5, 1, 4),
    _EsaProbeScheduleGroupType_Type()
)
esaProbeScheduleGroupType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esaProbeScheduleGroupType.setStatus("current")
_EsaProbeScheduleGroupStartTime_Type = DateAndTime
_EsaProbeScheduleGroupStartTime_Object = MibTableColumn
esaProbeScheduleGroupStartTime = _EsaProbeScheduleGroupStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 5, 1, 5),
    _EsaProbeScheduleGroupStartTime_Type()
)
esaProbeScheduleGroupStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esaProbeScheduleGroupStartTime.setStatus("current")
_EsaProbeScheduleGroupDuration_Type = Unsigned32
_EsaProbeScheduleGroupDuration_Object = MibTableColumn
esaProbeScheduleGroupDuration = _EsaProbeScheduleGroupDuration_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 5, 1, 6),
    _EsaProbeScheduleGroupDuration_Type()
)
esaProbeScheduleGroupDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esaProbeScheduleGroupDuration.setStatus("current")
_EsaProbeScheduleGroupInterval_Type = Unsigned32
_EsaProbeScheduleGroupInterval_Object = MibTableColumn
esaProbeScheduleGroupInterval = _EsaProbeScheduleGroupInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 5, 1, 7),
    _EsaProbeScheduleGroupInterval_Type()
)
esaProbeScheduleGroupInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esaProbeScheduleGroupInterval.setStatus("current")
_EsaProbeScheduleGroupAction_Type = EsaAction
_EsaProbeScheduleGroupAction_Object = MibTableColumn
esaProbeScheduleGroupAction = _EsaProbeScheduleGroupAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 5, 1, 8),
    _EsaProbeScheduleGroupAction_Type()
)
esaProbeScheduleGroupAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esaProbeScheduleGroupAction.setStatus("current")
_EsaProbeScheduleGroupStatus_Type = SchedActivityStatus
_EsaProbeScheduleGroupStatus_Object = MibTableColumn
esaProbeScheduleGroupStatus = _EsaProbeScheduleGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 5, 1, 9),
    _EsaProbeScheduleGroupStatus_Type()
)
esaProbeScheduleGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeScheduleGroupStatus.setStatus("current")
_EsaProbeScheduleGroupStorageType_Type = StorageType
_EsaProbeScheduleGroupStorageType_Object = MibTableColumn
esaProbeScheduleGroupStorageType = _EsaProbeScheduleGroupStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 5, 1, 10),
    _EsaProbeScheduleGroupStorageType_Type()
)
esaProbeScheduleGroupStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esaProbeScheduleGroupStorageType.setStatus("current")
_EsaProbeScheduleGroupRowStatus_Type = RowStatus
_EsaProbeScheduleGroupRowStatus_Object = MibTableColumn
esaProbeScheduleGroupRowStatus = _EsaProbeScheduleGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 5, 1, 11),
    _EsaProbeScheduleGroupRowStatus_Type()
)
esaProbeScheduleGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esaProbeScheduleGroupRowStatus.setStatus("current")


class _EsaProbeScheduleGroupActionProbeList_Type(DisplayString):
    """Custom type esaProbeScheduleGroupActionProbeList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 512),
    )


_EsaProbeScheduleGroupActionProbeList_Type.__name__ = "DisplayString"
_EsaProbeScheduleGroupActionProbeList_Object = MibTableColumn
esaProbeScheduleGroupActionProbeList = _EsaProbeScheduleGroupActionProbeList_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 5, 1, 12),
    _EsaProbeScheduleGroupActionProbeList_Type()
)
esaProbeScheduleGroupActionProbeList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esaProbeScheduleGroupActionProbeList.setStatus("current")
_EsaReflectorTable_Object = MibTable
esaReflectorTable = _EsaReflectorTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 6)
)
if mibBuilder.loadTexts:
    esaReflectorTable.setStatus("current")
_EsaReflectorEntry_Object = MibTableRow
esaReflectorEntry = _EsaReflectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 6, 1)
)
esaReflectorEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-SA-MIB", "esaReflectorIndex"),
)
if mibBuilder.loadTexts:
    esaReflectorEntry.setStatus("current")
_EsaReflectorIndex_Type = Integer32
_EsaReflectorIndex_Object = MibTableColumn
esaReflectorIndex = _EsaReflectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 6, 1, 1),
    _EsaReflectorIndex_Type()
)
esaReflectorIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esaReflectorIndex.setStatus("current")


class _EsaReflectorName_Type(DisplayString):
    """Custom type esaReflectorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_EsaReflectorName_Type.__name__ = "DisplayString"
_EsaReflectorName_Object = MibTableColumn
esaReflectorName = _EsaReflectorName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 6, 1, 2),
    _EsaReflectorName_Type()
)
esaReflectorName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esaReflectorName.setStatus("current")
_EsaReflectorIpAddress_Type = IpAddress
_EsaReflectorIpAddress_Object = MibTableColumn
esaReflectorIpAddress = _EsaReflectorIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 6, 1, 3),
    _EsaReflectorIpAddress_Type()
)
esaReflectorIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esaReflectorIpAddress.setStatus("current")
_EsaReflectorSubnetMask_Type = IpAddress
_EsaReflectorSubnetMask_Object = MibTableColumn
esaReflectorSubnetMask = _EsaReflectorSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 6, 1, 4),
    _EsaReflectorSubnetMask_Type()
)
esaReflectorSubnetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esaReflectorSubnetMask.setStatus("current")
_EsaReflectorSourcePort_Type = VariablePointer
_EsaReflectorSourcePort_Object = MibTableColumn
esaReflectorSourcePort = _EsaReflectorSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 6, 1, 5),
    _EsaReflectorSourcePort_Type()
)
esaReflectorSourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esaReflectorSourcePort.setStatus("current")
_EsaReflectorIpPrioMapMode_Type = IpPriorityMapMode
_EsaReflectorIpPrioMapMode_Object = MibTableColumn
esaReflectorIpPrioMapMode = _EsaReflectorIpPrioMapMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 6, 1, 6),
    _EsaReflectorIpPrioMapMode_Type()
)
esaReflectorIpPrioMapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esaReflectorIpPrioMapMode.setStatus("current")


class _EsaReflectorIpPriority_Type(Integer32):
    """Custom type esaReflectorIpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_EsaReflectorIpPriority_Type.__name__ = "Integer32"
_EsaReflectorIpPriority_Object = MibTableColumn
esaReflectorIpPriority = _EsaReflectorIpPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 6, 1, 7),
    _EsaReflectorIpPriority_Type()
)
esaReflectorIpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esaReflectorIpPriority.setStatus("current")
_EsaReflectorAction_Type = EsaAction
_EsaReflectorAction_Object = MibTableColumn
esaReflectorAction = _EsaReflectorAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 6, 1, 8),
    _EsaReflectorAction_Type()
)
esaReflectorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esaReflectorAction.setStatus("current")
_EsaReflectorSuspended_Type = TruthValue
_EsaReflectorSuspended_Object = MibTableColumn
esaReflectorSuspended = _EsaReflectorSuspended_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 6, 1, 9),
    _EsaReflectorSuspended_Type()
)
esaReflectorSuspended.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaReflectorSuspended.setStatus("current")
_EsaReflectorCreationTime_Type = DateAndTime
_EsaReflectorCreationTime_Object = MibTableColumn
esaReflectorCreationTime = _EsaReflectorCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 6, 1, 10),
    _EsaReflectorCreationTime_Type()
)
esaReflectorCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaReflectorCreationTime.setStatus("current")
_EsaReflectorStorageType_Type = StorageType
_EsaReflectorStorageType_Object = MibTableColumn
esaReflectorStorageType = _EsaReflectorStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 6, 1, 11),
    _EsaReflectorStorageType_Type()
)
esaReflectorStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esaReflectorStorageType.setStatus("current")
_EsaReflectorRowStatus_Type = RowStatus
_EsaReflectorRowStatus_Object = MibTableColumn
esaReflectorRowStatus = _EsaReflectorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 6, 1, 12),
    _EsaReflectorRowStatus_Type()
)
esaReflectorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esaReflectorRowStatus.setStatus("current")
_EsaReflectorDirection_Type = EsaReflectorDirection
_EsaReflectorDirection_Object = MibTableColumn
esaReflectorDirection = _EsaReflectorDirection_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 6, 1, 13),
    _EsaReflectorDirection_Type()
)
esaReflectorDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esaReflectorDirection.setStatus("current")
_EsaReflectorAdminState_Type = AdminState
_EsaReflectorAdminState_Object = MibTableColumn
esaReflectorAdminState = _EsaReflectorAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 6, 1, 14),
    _EsaReflectorAdminState_Type()
)
esaReflectorAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaReflectorAdminState.setStatus("current")
_EsaReflectorOperationalState_Type = OperationalState
_EsaReflectorOperationalState_Object = MibTableColumn
esaReflectorOperationalState = _EsaReflectorOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 6, 1, 15),
    _EsaReflectorOperationalState_Type()
)
esaReflectorOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaReflectorOperationalState.setStatus("current")
_EsaReflectorSecondaryState_Type = SecondaryState
_EsaReflectorSecondaryState_Object = MibTableColumn
esaReflectorSecondaryState = _EsaReflectorSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 6, 1, 16),
    _EsaReflectorSecondaryState_Type()
)
esaReflectorSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaReflectorSecondaryState.setStatus("current")
_EsaReflectorMacAddress_Type = MacAddress
_EsaReflectorMacAddress_Object = MibTableColumn
esaReflectorMacAddress = _EsaReflectorMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 6, 1, 17),
    _EsaReflectorMacAddress_Type()
)
esaReflectorMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaReflectorMacAddress.setStatus("current")


class _EsaReflectorAlias_Type(DisplayString):
    """Custom type esaReflectorAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EsaReflectorAlias_Type.__name__ = "DisplayString"
_EsaReflectorAlias_Object = MibTableColumn
esaReflectorAlias = _EsaReflectorAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 6, 1, 18),
    _EsaReflectorAlias_Type()
)
esaReflectorAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esaReflectorAlias.setStatus("current")
_EsaProbeStatsTable_Object = MibTable
esaProbeStatsTable = _EsaProbeStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7)
)
if mibBuilder.loadTexts:
    esaProbeStatsTable.setStatus("current")
_EsaProbeStatsEntry_Object = MibTableRow
esaProbeStatsEntry = _EsaProbeStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1)
)
esaProbeStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-SA-MIB", "esaProbeIndex"),
    (0, "CM-SA-MIB", "esaProbeStatsDestinationIndex"),
    (0, "CM-SA-MIB", "esaProbeStatsCOSIndex"),
    (0, "CM-SA-MIB", "esaProbeStatsIndex"),
)
if mibBuilder.loadTexts:
    esaProbeStatsEntry.setStatus("current")
_EsaProbeStatsDestinationIndex_Type = Integer32
_EsaProbeStatsDestinationIndex_Object = MibTableColumn
esaProbeStatsDestinationIndex = _EsaProbeStatsDestinationIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 1),
    _EsaProbeStatsDestinationIndex_Type()
)
esaProbeStatsDestinationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsDestinationIndex.setStatus("current")
_EsaProbeStatsCOSIndex_Type = Integer32
_EsaProbeStatsCOSIndex_Object = MibTableColumn
esaProbeStatsCOSIndex = _EsaProbeStatsCOSIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 2),
    _EsaProbeStatsCOSIndex_Type()
)
esaProbeStatsCOSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsCOSIndex.setStatus("current")


class _EsaProbeStatsIndex_Type(Integer32):
    """Custom type esaProbeStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_EsaProbeStatsIndex_Type.__name__ = "Integer32"
_EsaProbeStatsIndex_Object = MibTableColumn
esaProbeStatsIndex = _EsaProbeStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 3),
    _EsaProbeStatsIndex_Type()
)
esaProbeStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsIndex.setStatus("current")
_EsaProbeStatsIntervalType_Type = EsaProbePmIntervalType
_EsaProbeStatsIntervalType_Object = MibTableColumn
esaProbeStatsIntervalType = _EsaProbeStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 4),
    _EsaProbeStatsIntervalType_Type()
)
esaProbeStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsIntervalType.setStatus("current")
_EsaProbeStatsCOS_Type = ClassOfServiceType
_EsaProbeStatsCOS_Object = MibTableColumn
esaProbeStatsCOS = _EsaProbeStatsCOS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 5),
    _EsaProbeStatsCOS_Type()
)
esaProbeStatsCOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsCOS.setStatus("current")
_EsaProbeStatsValid_Type = TruthValue
_EsaProbeStatsValid_Object = MibTableColumn
esaProbeStatsValid = _EsaProbeStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 6),
    _EsaProbeStatsValid_Type()
)
esaProbeStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsValid.setStatus("current")
_EsaProbeStatsAction_Type = CmPmBinAction
_EsaProbeStatsAction_Object = MibTableColumn
esaProbeStatsAction = _EsaProbeStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 7),
    _EsaProbeStatsAction_Type()
)
esaProbeStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esaProbeStatsAction.setStatus("current")
_EsaProbeStatsP2RPkts_Type = PerfCounter64
_EsaProbeStatsP2RPkts_Object = MibTableColumn
esaProbeStatsP2RPkts = _EsaProbeStatsP2RPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 8),
    _EsaProbeStatsP2RPkts_Type()
)
esaProbeStatsP2RPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsP2RPkts.setStatus("current")
_EsaProbeStatsP2RErredPkts_Type = PerfCounter64
_EsaProbeStatsP2RErredPkts_Object = MibTableColumn
esaProbeStatsP2RErredPkts = _EsaProbeStatsP2RErredPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 9),
    _EsaProbeStatsP2RErredPkts_Type()
)
esaProbeStatsP2RErredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsP2RErredPkts.setStatus("current")
_EsaProbeStatsP2RSyncErrs_Type = PerfCounter64
_EsaProbeStatsP2RSyncErrs_Object = MibTableColumn
esaProbeStatsP2RSyncErrs = _EsaProbeStatsP2RSyncErrs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 10),
    _EsaProbeStatsP2RSyncErrs_Type()
)
esaProbeStatsP2RSyncErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsP2RSyncErrs.setStatus("current")
_EsaProbeStatsP2RLostPkts_Type = PerfCounter64
_EsaProbeStatsP2RLostPkts_Object = MibTableColumn
esaProbeStatsP2RLostPkts = _EsaProbeStatsP2RLostPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 11),
    _EsaProbeStatsP2RLostPkts_Type()
)
esaProbeStatsP2RLostPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsP2RLostPkts.setStatus("current")
_EsaProbeStatsR2PPkts_Type = PerfCounter64
_EsaProbeStatsR2PPkts_Object = MibTableColumn
esaProbeStatsR2PPkts = _EsaProbeStatsR2PPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 12),
    _EsaProbeStatsR2PPkts_Type()
)
esaProbeStatsR2PPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsR2PPkts.setStatus("current")
_EsaProbeStatsR2PErredPkts_Type = PerfCounter64
_EsaProbeStatsR2PErredPkts_Object = MibTableColumn
esaProbeStatsR2PErredPkts = _EsaProbeStatsR2PErredPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 13),
    _EsaProbeStatsR2PErredPkts_Type()
)
esaProbeStatsR2PErredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsR2PErredPkts.setStatus("current")
_EsaProbeStatsR2PSyncErrs_Type = PerfCounter64
_EsaProbeStatsR2PSyncErrs_Object = MibTableColumn
esaProbeStatsR2PSyncErrs = _EsaProbeStatsR2PSyncErrs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 14),
    _EsaProbeStatsR2PSyncErrs_Type()
)
esaProbeStatsR2PSyncErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsR2PSyncErrs.setStatus("current")
_EsaProbeStatsR2PLostPkts_Type = PerfCounter64
_EsaProbeStatsR2PLostPkts_Object = MibTableColumn
esaProbeStatsR2PLostPkts = _EsaProbeStatsR2PLostPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 15),
    _EsaProbeStatsR2PLostPkts_Type()
)
esaProbeStatsR2PLostPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsR2PLostPkts.setStatus("current")
_EsaProbeStatsLostPkts_Type = PerfCounter64
_EsaProbeStatsLostPkts_Object = MibTableColumn
esaProbeStatsLostPkts = _EsaProbeStatsLostPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 16),
    _EsaProbeStatsLostPkts_Type()
)
esaProbeStatsLostPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsLostPkts.setStatus("current")
_EsaProbeStatsSeqGaps_Type = PerfCounter64
_EsaProbeStatsSeqGaps_Object = MibTableColumn
esaProbeStatsSeqGaps = _EsaProbeStatsSeqGaps_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 17),
    _EsaProbeStatsSeqGaps_Type()
)
esaProbeStatsSeqGaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsSeqGaps.setStatus("current")
_EsaProbeStatsOutOfSeqErrs_Type = PerfCounter64
_EsaProbeStatsOutOfSeqErrs_Object = MibTableColumn
esaProbeStatsOutOfSeqErrs = _EsaProbeStatsOutOfSeqErrs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 18),
    _EsaProbeStatsOutOfSeqErrs_Type()
)
esaProbeStatsOutOfSeqErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsOutOfSeqErrs.setStatus("current")
_EsaProbeStatsMinRoundTripDelay_Type = Unsigned32
_EsaProbeStatsMinRoundTripDelay_Object = MibTableColumn
esaProbeStatsMinRoundTripDelay = _EsaProbeStatsMinRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 19),
    _EsaProbeStatsMinRoundTripDelay_Type()
)
esaProbeStatsMinRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsMinRoundTripDelay.setStatus("current")
_EsaProbeStatsMaxRoundTripDelay_Type = Unsigned32
_EsaProbeStatsMaxRoundTripDelay_Object = MibTableColumn
esaProbeStatsMaxRoundTripDelay = _EsaProbeStatsMaxRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 20),
    _EsaProbeStatsMaxRoundTripDelay_Type()
)
esaProbeStatsMaxRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsMaxRoundTripDelay.setStatus("current")
_EsaProbeStatsAvgRoundTripDelay_Type = Unsigned32
_EsaProbeStatsAvgRoundTripDelay_Object = MibTableColumn
esaProbeStatsAvgRoundTripDelay = _EsaProbeStatsAvgRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 21),
    _EsaProbeStatsAvgRoundTripDelay_Type()
)
esaProbeStatsAvgRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsAvgRoundTripDelay.setStatus("current")
_EsaProbeStatsSumRoundTripDelay_Type = PerfCounter64
_EsaProbeStatsSumRoundTripDelay_Object = MibTableColumn
esaProbeStatsSumRoundTripDelay = _EsaProbeStatsSumRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 22),
    _EsaProbeStatsSumRoundTripDelay_Type()
)
esaProbeStatsSumRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsSumRoundTripDelay.setStatus("current")
_EsaProbeStatsSumOfSqRoundTripDelay_Type = PerfCounter64
_EsaProbeStatsSumOfSqRoundTripDelay_Object = MibTableColumn
esaProbeStatsSumOfSqRoundTripDelay = _EsaProbeStatsSumOfSqRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 23),
    _EsaProbeStatsSumOfSqRoundTripDelay_Type()
)
esaProbeStatsSumOfSqRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsSumOfSqRoundTripDelay.setStatus("current")
_EsaProbeStatsMinOnewayP2RDelay_Type = Unsigned32
_EsaProbeStatsMinOnewayP2RDelay_Object = MibTableColumn
esaProbeStatsMinOnewayP2RDelay = _EsaProbeStatsMinOnewayP2RDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 24),
    _EsaProbeStatsMinOnewayP2RDelay_Type()
)
esaProbeStatsMinOnewayP2RDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsMinOnewayP2RDelay.setStatus("current")
_EsaProbeStatsMaxOnewayP2RDelay_Type = Unsigned32
_EsaProbeStatsMaxOnewayP2RDelay_Object = MibTableColumn
esaProbeStatsMaxOnewayP2RDelay = _EsaProbeStatsMaxOnewayP2RDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 25),
    _EsaProbeStatsMaxOnewayP2RDelay_Type()
)
esaProbeStatsMaxOnewayP2RDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsMaxOnewayP2RDelay.setStatus("current")
_EsaProbeStatsAvgOnewayP2RDelay_Type = Unsigned32
_EsaProbeStatsAvgOnewayP2RDelay_Object = MibTableColumn
esaProbeStatsAvgOnewayP2RDelay = _EsaProbeStatsAvgOnewayP2RDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 26),
    _EsaProbeStatsAvgOnewayP2RDelay_Type()
)
esaProbeStatsAvgOnewayP2RDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsAvgOnewayP2RDelay.setStatus("current")
_EsaProbeStatsSumOnewayP2RDelay_Type = PerfCounter64
_EsaProbeStatsSumOnewayP2RDelay_Object = MibTableColumn
esaProbeStatsSumOnewayP2RDelay = _EsaProbeStatsSumOnewayP2RDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 27),
    _EsaProbeStatsSumOnewayP2RDelay_Type()
)
esaProbeStatsSumOnewayP2RDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsSumOnewayP2RDelay.setStatus("current")
_EsaProbeStatsSumOfSqOnewayP2RDelay_Type = PerfCounter64
_EsaProbeStatsSumOfSqOnewayP2RDelay_Object = MibTableColumn
esaProbeStatsSumOfSqOnewayP2RDelay = _EsaProbeStatsSumOfSqOnewayP2RDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 28),
    _EsaProbeStatsSumOfSqOnewayP2RDelay_Type()
)
esaProbeStatsSumOfSqOnewayP2RDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsSumOfSqOnewayP2RDelay.setStatus("current")
_EsaProbeStatsMinOnewayR2PDelay_Type = Unsigned32
_EsaProbeStatsMinOnewayR2PDelay_Object = MibTableColumn
esaProbeStatsMinOnewayR2PDelay = _EsaProbeStatsMinOnewayR2PDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 29),
    _EsaProbeStatsMinOnewayR2PDelay_Type()
)
esaProbeStatsMinOnewayR2PDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsMinOnewayR2PDelay.setStatus("current")
_EsaProbeStatsMaxOnewayR2PDelay_Type = Unsigned32
_EsaProbeStatsMaxOnewayR2PDelay_Object = MibTableColumn
esaProbeStatsMaxOnewayR2PDelay = _EsaProbeStatsMaxOnewayR2PDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 30),
    _EsaProbeStatsMaxOnewayR2PDelay_Type()
)
esaProbeStatsMaxOnewayR2PDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsMaxOnewayR2PDelay.setStatus("current")
_EsaProbeStatsAvgOnewayR2PDelay_Type = Unsigned32
_EsaProbeStatsAvgOnewayR2PDelay_Object = MibTableColumn
esaProbeStatsAvgOnewayR2PDelay = _EsaProbeStatsAvgOnewayR2PDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 31),
    _EsaProbeStatsAvgOnewayR2PDelay_Type()
)
esaProbeStatsAvgOnewayR2PDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsAvgOnewayR2PDelay.setStatus("current")
_EsaProbeStatsSumOnewayR2PDelay_Type = PerfCounter64
_EsaProbeStatsSumOnewayR2PDelay_Object = MibTableColumn
esaProbeStatsSumOnewayR2PDelay = _EsaProbeStatsSumOnewayR2PDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 32),
    _EsaProbeStatsSumOnewayR2PDelay_Type()
)
esaProbeStatsSumOnewayR2PDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsSumOnewayR2PDelay.setStatus("current")
_EsaProbeStatsSumOfSqOnewayR2PDelay_Type = PerfCounter64
_EsaProbeStatsSumOfSqOnewayR2PDelay_Object = MibTableColumn
esaProbeStatsSumOfSqOnewayR2PDelay = _EsaProbeStatsSumOfSqOnewayR2PDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 33),
    _EsaProbeStatsSumOfSqOnewayR2PDelay_Type()
)
esaProbeStatsSumOfSqOnewayR2PDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsSumOfSqOnewayR2PDelay.setStatus("current")
_EsaProbeStatsMinPosP2RJitter_Type = Unsigned32
_EsaProbeStatsMinPosP2RJitter_Object = MibTableColumn
esaProbeStatsMinPosP2RJitter = _EsaProbeStatsMinPosP2RJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 34),
    _EsaProbeStatsMinPosP2RJitter_Type()
)
esaProbeStatsMinPosP2RJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsMinPosP2RJitter.setStatus("current")
_EsaProbeStatsMaxPosP2RJitter_Type = Unsigned32
_EsaProbeStatsMaxPosP2RJitter_Object = MibTableColumn
esaProbeStatsMaxPosP2RJitter = _EsaProbeStatsMaxPosP2RJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 35),
    _EsaProbeStatsMaxPosP2RJitter_Type()
)
esaProbeStatsMaxPosP2RJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsMaxPosP2RJitter.setStatus("current")
_EsaProbeStatsNumPosP2RJitter_Type = PerfCounter64
_EsaProbeStatsNumPosP2RJitter_Object = MibTableColumn
esaProbeStatsNumPosP2RJitter = _EsaProbeStatsNumPosP2RJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 36),
    _EsaProbeStatsNumPosP2RJitter_Type()
)
esaProbeStatsNumPosP2RJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsNumPosP2RJitter.setStatus("current")
_EsaProbeStatsSumPosP2RJitter_Type = PerfCounter64
_EsaProbeStatsSumPosP2RJitter_Object = MibTableColumn
esaProbeStatsSumPosP2RJitter = _EsaProbeStatsSumPosP2RJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 37),
    _EsaProbeStatsSumPosP2RJitter_Type()
)
esaProbeStatsSumPosP2RJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsSumPosP2RJitter.setStatus("current")
_EsaProbeStatsSumOfSqPosP2RJitter_Type = PerfCounter64
_EsaProbeStatsSumOfSqPosP2RJitter_Object = MibTableColumn
esaProbeStatsSumOfSqPosP2RJitter = _EsaProbeStatsSumOfSqPosP2RJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 38),
    _EsaProbeStatsSumOfSqPosP2RJitter_Type()
)
esaProbeStatsSumOfSqPosP2RJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsSumOfSqPosP2RJitter.setStatus("current")
_EsaProbeStatsMinNegP2RJitter_Type = Unsigned32
_EsaProbeStatsMinNegP2RJitter_Object = MibTableColumn
esaProbeStatsMinNegP2RJitter = _EsaProbeStatsMinNegP2RJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 39),
    _EsaProbeStatsMinNegP2RJitter_Type()
)
esaProbeStatsMinNegP2RJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsMinNegP2RJitter.setStatus("current")
_EsaProbeStatsMaxNegP2RJitter_Type = Unsigned32
_EsaProbeStatsMaxNegP2RJitter_Object = MibTableColumn
esaProbeStatsMaxNegP2RJitter = _EsaProbeStatsMaxNegP2RJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 40),
    _EsaProbeStatsMaxNegP2RJitter_Type()
)
esaProbeStatsMaxNegP2RJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsMaxNegP2RJitter.setStatus("current")
_EsaProbeStatsNumNegP2RJitter_Type = PerfCounter64
_EsaProbeStatsNumNegP2RJitter_Object = MibTableColumn
esaProbeStatsNumNegP2RJitter = _EsaProbeStatsNumNegP2RJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 41),
    _EsaProbeStatsNumNegP2RJitter_Type()
)
esaProbeStatsNumNegP2RJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsNumNegP2RJitter.setStatus("current")
_EsaProbeStatsSumNegP2RJitter_Type = PerfCounter64
_EsaProbeStatsSumNegP2RJitter_Object = MibTableColumn
esaProbeStatsSumNegP2RJitter = _EsaProbeStatsSumNegP2RJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 42),
    _EsaProbeStatsSumNegP2RJitter_Type()
)
esaProbeStatsSumNegP2RJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsSumNegP2RJitter.setStatus("current")
_EsaProbeStatsSumOfSqNegP2RJitter_Type = PerfCounter64
_EsaProbeStatsSumOfSqNegP2RJitter_Object = MibTableColumn
esaProbeStatsSumOfSqNegP2RJitter = _EsaProbeStatsSumOfSqNegP2RJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 43),
    _EsaProbeStatsSumOfSqNegP2RJitter_Type()
)
esaProbeStatsSumOfSqNegP2RJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsSumOfSqNegP2RJitter.setStatus("current")
_EsaProbeStatsMinPosR2PJitter_Type = Unsigned32
_EsaProbeStatsMinPosR2PJitter_Object = MibTableColumn
esaProbeStatsMinPosR2PJitter = _EsaProbeStatsMinPosR2PJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 44),
    _EsaProbeStatsMinPosR2PJitter_Type()
)
esaProbeStatsMinPosR2PJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsMinPosR2PJitter.setStatus("current")
_EsaProbeStatsMaxPosR2PJitter_Type = Unsigned32
_EsaProbeStatsMaxPosR2PJitter_Object = MibTableColumn
esaProbeStatsMaxPosR2PJitter = _EsaProbeStatsMaxPosR2PJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 45),
    _EsaProbeStatsMaxPosR2PJitter_Type()
)
esaProbeStatsMaxPosR2PJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsMaxPosR2PJitter.setStatus("current")
_EsaProbeStatsNumPosR2PJitter_Type = PerfCounter64
_EsaProbeStatsNumPosR2PJitter_Object = MibTableColumn
esaProbeStatsNumPosR2PJitter = _EsaProbeStatsNumPosR2PJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 46),
    _EsaProbeStatsNumPosR2PJitter_Type()
)
esaProbeStatsNumPosR2PJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsNumPosR2PJitter.setStatus("current")
_EsaProbeStatsSumPosR2PJitter_Type = PerfCounter64
_EsaProbeStatsSumPosR2PJitter_Object = MibTableColumn
esaProbeStatsSumPosR2PJitter = _EsaProbeStatsSumPosR2PJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 47),
    _EsaProbeStatsSumPosR2PJitter_Type()
)
esaProbeStatsSumPosR2PJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsSumPosR2PJitter.setStatus("current")
_EsaProbeStatsSumOfSqPosR2PJitter_Type = PerfCounter64
_EsaProbeStatsSumOfSqPosR2PJitter_Object = MibTableColumn
esaProbeStatsSumOfSqPosR2PJitter = _EsaProbeStatsSumOfSqPosR2PJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 48),
    _EsaProbeStatsSumOfSqPosR2PJitter_Type()
)
esaProbeStatsSumOfSqPosR2PJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsSumOfSqPosR2PJitter.setStatus("current")
_EsaProbeStatsMinNegR2PJitter_Type = Unsigned32
_EsaProbeStatsMinNegR2PJitter_Object = MibTableColumn
esaProbeStatsMinNegR2PJitter = _EsaProbeStatsMinNegR2PJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 49),
    _EsaProbeStatsMinNegR2PJitter_Type()
)
esaProbeStatsMinNegR2PJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsMinNegR2PJitter.setStatus("current")
_EsaProbeStatsMaxNegR2PJitter_Type = Unsigned32
_EsaProbeStatsMaxNegR2PJitter_Object = MibTableColumn
esaProbeStatsMaxNegR2PJitter = _EsaProbeStatsMaxNegR2PJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 50),
    _EsaProbeStatsMaxNegR2PJitter_Type()
)
esaProbeStatsMaxNegR2PJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsMaxNegR2PJitter.setStatus("current")
_EsaProbeStatsNumNegR2PJitter_Type = PerfCounter64
_EsaProbeStatsNumNegR2PJitter_Object = MibTableColumn
esaProbeStatsNumNegR2PJitter = _EsaProbeStatsNumNegR2PJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 51),
    _EsaProbeStatsNumNegR2PJitter_Type()
)
esaProbeStatsNumNegR2PJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsNumNegR2PJitter.setStatus("current")
_EsaProbeStatsSumNegR2PJitter_Type = PerfCounter64
_EsaProbeStatsSumNegR2PJitter_Object = MibTableColumn
esaProbeStatsSumNegR2PJitter = _EsaProbeStatsSumNegR2PJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 52),
    _EsaProbeStatsSumNegR2PJitter_Type()
)
esaProbeStatsSumNegR2PJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsSumNegR2PJitter.setStatus("current")
_EsaProbeStatsSumOfSqNegR2PJitter_Type = PerfCounter64
_EsaProbeStatsSumOfSqNegR2PJitter_Object = MibTableColumn
esaProbeStatsSumOfSqNegR2PJitter = _EsaProbeStatsSumOfSqNegR2PJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 53),
    _EsaProbeStatsSumOfSqNegR2PJitter_Type()
)
esaProbeStatsSumOfSqNegR2PJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsSumOfSqNegR2PJitter.setStatus("current")
_EsaProbeStatsY1731P2RNegLossOccurrences_Type = PerfCounter64
_EsaProbeStatsY1731P2RNegLossOccurrences_Object = MibTableColumn
esaProbeStatsY1731P2RNegLossOccurrences = _EsaProbeStatsY1731P2RNegLossOccurrences_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 54),
    _EsaProbeStatsY1731P2RNegLossOccurrences_Type()
)
esaProbeStatsY1731P2RNegLossOccurrences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsY1731P2RNegLossOccurrences.setStatus("current")
_EsaProbeStatsY1731R2PNegLossOccurrences_Type = PerfCounter64
_EsaProbeStatsY1731R2PNegLossOccurrences_Object = MibTableColumn
esaProbeStatsY1731R2PNegLossOccurrences = _EsaProbeStatsY1731R2PNegLossOccurrences_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 55),
    _EsaProbeStatsY1731R2PNegLossOccurrences_Type()
)
esaProbeStatsY1731R2PNegLossOccurrences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsY1731R2PNegLossOccurrences.setStatus("current")
_EsaProbeStatsY1731RxLmSamples_Type = TruthValue
_EsaProbeStatsY1731RxLmSamples_Object = MibTableColumn
esaProbeStatsY1731RxLmSamples = _EsaProbeStatsY1731RxLmSamples_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 56),
    _EsaProbeStatsY1731RxLmSamples_Type()
)
esaProbeStatsY1731RxLmSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsY1731RxLmSamples.setStatus("current")
_EsaProbeStatsY1731RxDmSamples_Type = TruthValue
_EsaProbeStatsY1731RxDmSamples_Object = MibTableColumn
esaProbeStatsY1731RxDmSamples = _EsaProbeStatsY1731RxDmSamples_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 57),
    _EsaProbeStatsY1731RxDmSamples_Type()
)
esaProbeStatsY1731RxDmSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsY1731RxDmSamples.setStatus("current")
_EsaProbeStatsY1731P2RFrames_Type = PerfCounter64
_EsaProbeStatsY1731P2RFrames_Object = MibTableColumn
esaProbeStatsY1731P2RFrames = _EsaProbeStatsY1731P2RFrames_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 58),
    _EsaProbeStatsY1731P2RFrames_Type()
)
esaProbeStatsY1731P2RFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsY1731P2RFrames.setStatus("current")
_EsaProbeStatsY1731R2PFrames_Type = PerfCounter64
_EsaProbeStatsY1731R2PFrames_Object = MibTableColumn
esaProbeStatsY1731R2PFrames = _EsaProbeStatsY1731R2PFrames_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 59),
    _EsaProbeStatsY1731R2PFrames_Type()
)
esaProbeStatsY1731R2PFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsY1731R2PFrames.setStatus("current")
_EsaProbeStatsAvgAbsP2RJitter_Type = Unsigned32
_EsaProbeStatsAvgAbsP2RJitter_Object = MibTableColumn
esaProbeStatsAvgAbsP2RJitter = _EsaProbeStatsAvgAbsP2RJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 60),
    _EsaProbeStatsAvgAbsP2RJitter_Type()
)
esaProbeStatsAvgAbsP2RJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsAvgAbsP2RJitter.setStatus("current")
_EsaProbeStatsAvgAbsR2PJitter_Type = Unsigned32
_EsaProbeStatsAvgAbsR2PJitter_Object = MibTableColumn
esaProbeStatsAvgAbsR2PJitter = _EsaProbeStatsAvgAbsR2PJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 61),
    _EsaProbeStatsAvgAbsR2PJitter_Type()
)
esaProbeStatsAvgAbsR2PJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsAvgAbsR2PJitter.setStatus("current")
_EsaProbeStatsMinAbsP2RJitter_Type = Unsigned32
_EsaProbeStatsMinAbsP2RJitter_Object = MibTableColumn
esaProbeStatsMinAbsP2RJitter = _EsaProbeStatsMinAbsP2RJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 62),
    _EsaProbeStatsMinAbsP2RJitter_Type()
)
esaProbeStatsMinAbsP2RJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsMinAbsP2RJitter.setStatus("current")
_EsaProbeStatsMinAbsR2PJitter_Type = Unsigned32
_EsaProbeStatsMinAbsR2PJitter_Object = MibTableColumn
esaProbeStatsMinAbsR2PJitter = _EsaProbeStatsMinAbsR2PJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 63),
    _EsaProbeStatsMinAbsR2PJitter_Type()
)
esaProbeStatsMinAbsR2PJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsMinAbsR2PJitter.setStatus("current")
_EsaProbeStatsMaxAbsP2RJitter_Type = Unsigned32
_EsaProbeStatsMaxAbsP2RJitter_Object = MibTableColumn
esaProbeStatsMaxAbsP2RJitter = _EsaProbeStatsMaxAbsP2RJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 64),
    _EsaProbeStatsMaxAbsP2RJitter_Type()
)
esaProbeStatsMaxAbsP2RJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsMaxAbsP2RJitter.setStatus("current")
_EsaProbeStatsMaxAbsR2PJitter_Type = Unsigned32
_EsaProbeStatsMaxAbsR2PJitter_Object = MibTableColumn
esaProbeStatsMaxAbsR2PJitter = _EsaProbeStatsMaxAbsR2PJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 65),
    _EsaProbeStatsMaxAbsR2PJitter_Type()
)
esaProbeStatsMaxAbsR2PJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsMaxAbsR2PJitter.setStatus("current")
_EsaProbeStatsNumAbsP2RJitter_Type = PerfCounter64
_EsaProbeStatsNumAbsP2RJitter_Object = MibTableColumn
esaProbeStatsNumAbsP2RJitter = _EsaProbeStatsNumAbsP2RJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 66),
    _EsaProbeStatsNumAbsP2RJitter_Type()
)
esaProbeStatsNumAbsP2RJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsNumAbsP2RJitter.setStatus("current")
_EsaProbeStatsNumAbsR2PJitter_Type = PerfCounter64
_EsaProbeStatsNumAbsR2PJitter_Object = MibTableColumn
esaProbeStatsNumAbsR2PJitter = _EsaProbeStatsNumAbsR2PJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 67),
    _EsaProbeStatsNumAbsR2PJitter_Type()
)
esaProbeStatsNumAbsR2PJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsNumAbsR2PJitter.setStatus("current")
_EsaProbeStatsSumAbsP2RJitter_Type = PerfCounter64
_EsaProbeStatsSumAbsP2RJitter_Object = MibTableColumn
esaProbeStatsSumAbsP2RJitter = _EsaProbeStatsSumAbsP2RJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 68),
    _EsaProbeStatsSumAbsP2RJitter_Type()
)
esaProbeStatsSumAbsP2RJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsSumAbsP2RJitter.setStatus("current")
_EsaProbeStatsSumAbsR2PJitter_Type = PerfCounter64
_EsaProbeStatsSumAbsR2PJitter_Object = MibTableColumn
esaProbeStatsSumAbsR2PJitter = _EsaProbeStatsSumAbsR2PJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 69),
    _EsaProbeStatsSumAbsR2PJitter_Type()
)
esaProbeStatsSumAbsR2PJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsSumAbsR2PJitter.setStatus("current")
_EsaProbeStatsSumOfSqAbsP2RJitter_Type = PerfCounter64
_EsaProbeStatsSumOfSqAbsP2RJitter_Object = MibTableColumn
esaProbeStatsSumOfSqAbsP2RJitter = _EsaProbeStatsSumOfSqAbsP2RJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 70),
    _EsaProbeStatsSumOfSqAbsP2RJitter_Type()
)
esaProbeStatsSumOfSqAbsP2RJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsSumOfSqAbsP2RJitter.setStatus("current")
_EsaProbeStatsSumOfSqAbsR2PJitter_Type = PerfCounter64
_EsaProbeStatsSumOfSqAbsR2PJitter_Object = MibTableColumn
esaProbeStatsSumOfSqAbsR2PJitter = _EsaProbeStatsSumOfSqAbsR2PJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 7, 1, 71),
    _EsaProbeStatsSumOfSqAbsR2PJitter_Type()
)
esaProbeStatsSumOfSqAbsR2PJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsSumOfSqAbsR2PJitter.setStatus("current")
_EsaProbeHistoryTable_Object = MibTable
esaProbeHistoryTable = _EsaProbeHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8)
)
if mibBuilder.loadTexts:
    esaProbeHistoryTable.setStatus("current")
_EsaProbeHistoryEntry_Object = MibTableRow
esaProbeHistoryEntry = _EsaProbeHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1)
)
esaProbeHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-SA-MIB", "esaProbeIndex"),
    (0, "CM-SA-MIB", "esaProbeHistoryDestinationIndex"),
    (0, "CM-SA-MIB", "esaProbeHistoryCOSIndex"),
    (0, "CM-SA-MIB", "esaProbeHistoryIndex"),
)
if mibBuilder.loadTexts:
    esaProbeHistoryEntry.setStatus("current")
_EsaProbeHistoryDestinationIndex_Type = Integer32
_EsaProbeHistoryDestinationIndex_Object = MibTableColumn
esaProbeHistoryDestinationIndex = _EsaProbeHistoryDestinationIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 1),
    _EsaProbeHistoryDestinationIndex_Type()
)
esaProbeHistoryDestinationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistoryDestinationIndex.setStatus("current")
_EsaProbeHistoryCOSIndex_Type = Integer32
_EsaProbeHistoryCOSIndex_Object = MibTableColumn
esaProbeHistoryCOSIndex = _EsaProbeHistoryCOSIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 2),
    _EsaProbeHistoryCOSIndex_Type()
)
esaProbeHistoryCOSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistoryCOSIndex.setStatus("current")
_EsaProbeHistoryIndex_Type = Integer32
_EsaProbeHistoryIndex_Object = MibTableColumn
esaProbeHistoryIndex = _EsaProbeHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 3),
    _EsaProbeHistoryIndex_Type()
)
esaProbeHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistoryIndex.setStatus("current")
_EsaProbeHistoryTime_Type = DateAndTime
_EsaProbeHistoryTime_Object = MibTableColumn
esaProbeHistoryTime = _EsaProbeHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 4),
    _EsaProbeHistoryTime_Type()
)
esaProbeHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistoryTime.setStatus("current")
_EsaProbeHistoryValid_Type = TruthValue
_EsaProbeHistoryValid_Object = MibTableColumn
esaProbeHistoryValid = _EsaProbeHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 5),
    _EsaProbeHistoryValid_Type()
)
esaProbeHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistoryValid.setStatus("current")
_EsaProbeHistoryAction_Type = CmPmBinAction
_EsaProbeHistoryAction_Object = MibTableColumn
esaProbeHistoryAction = _EsaProbeHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 6),
    _EsaProbeHistoryAction_Type()
)
esaProbeHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esaProbeHistoryAction.setStatus("current")
_EsaProbeHistoryCOS_Type = ClassOfServiceType
_EsaProbeHistoryCOS_Object = MibTableColumn
esaProbeHistoryCOS = _EsaProbeHistoryCOS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 7),
    _EsaProbeHistoryCOS_Type()
)
esaProbeHistoryCOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistoryCOS.setStatus("current")
_EsaProbeHistoryP2RPkts_Type = PerfCounter64
_EsaProbeHistoryP2RPkts_Object = MibTableColumn
esaProbeHistoryP2RPkts = _EsaProbeHistoryP2RPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 8),
    _EsaProbeHistoryP2RPkts_Type()
)
esaProbeHistoryP2RPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistoryP2RPkts.setStatus("current")
_EsaProbeHistoryP2RErredPkts_Type = PerfCounter64
_EsaProbeHistoryP2RErredPkts_Object = MibTableColumn
esaProbeHistoryP2RErredPkts = _EsaProbeHistoryP2RErredPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 9),
    _EsaProbeHistoryP2RErredPkts_Type()
)
esaProbeHistoryP2RErredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistoryP2RErredPkts.setStatus("current")
_EsaProbeHistoryP2RSyncErrs_Type = PerfCounter64
_EsaProbeHistoryP2RSyncErrs_Object = MibTableColumn
esaProbeHistoryP2RSyncErrs = _EsaProbeHistoryP2RSyncErrs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 10),
    _EsaProbeHistoryP2RSyncErrs_Type()
)
esaProbeHistoryP2RSyncErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistoryP2RSyncErrs.setStatus("current")
_EsaProbeHistoryP2RLostPkts_Type = PerfCounter64
_EsaProbeHistoryP2RLostPkts_Object = MibTableColumn
esaProbeHistoryP2RLostPkts = _EsaProbeHistoryP2RLostPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 11),
    _EsaProbeHistoryP2RLostPkts_Type()
)
esaProbeHistoryP2RLostPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistoryP2RLostPkts.setStatus("current")
_EsaProbeHistoryR2PPkts_Type = PerfCounter64
_EsaProbeHistoryR2PPkts_Object = MibTableColumn
esaProbeHistoryR2PPkts = _EsaProbeHistoryR2PPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 12),
    _EsaProbeHistoryR2PPkts_Type()
)
esaProbeHistoryR2PPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistoryR2PPkts.setStatus("current")
_EsaProbeHistoryR2PErredPkts_Type = PerfCounter64
_EsaProbeHistoryR2PErredPkts_Object = MibTableColumn
esaProbeHistoryR2PErredPkts = _EsaProbeHistoryR2PErredPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 13),
    _EsaProbeHistoryR2PErredPkts_Type()
)
esaProbeHistoryR2PErredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistoryR2PErredPkts.setStatus("current")
_EsaProbeHistoryR2PSyncErrs_Type = PerfCounter64
_EsaProbeHistoryR2PSyncErrs_Object = MibTableColumn
esaProbeHistoryR2PSyncErrs = _EsaProbeHistoryR2PSyncErrs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 14),
    _EsaProbeHistoryR2PSyncErrs_Type()
)
esaProbeHistoryR2PSyncErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistoryR2PSyncErrs.setStatus("current")
_EsaProbeHistoryR2PLostPkts_Type = PerfCounter64
_EsaProbeHistoryR2PLostPkts_Object = MibTableColumn
esaProbeHistoryR2PLostPkts = _EsaProbeHistoryR2PLostPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 15),
    _EsaProbeHistoryR2PLostPkts_Type()
)
esaProbeHistoryR2PLostPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistoryR2PLostPkts.setStatus("current")
_EsaProbeHistoryLostPkts_Type = PerfCounter64
_EsaProbeHistoryLostPkts_Object = MibTableColumn
esaProbeHistoryLostPkts = _EsaProbeHistoryLostPkts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 16),
    _EsaProbeHistoryLostPkts_Type()
)
esaProbeHistoryLostPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistoryLostPkts.setStatus("current")
_EsaProbeHistorySeqGaps_Type = PerfCounter64
_EsaProbeHistorySeqGaps_Object = MibTableColumn
esaProbeHistorySeqGaps = _EsaProbeHistorySeqGaps_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 17),
    _EsaProbeHistorySeqGaps_Type()
)
esaProbeHistorySeqGaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistorySeqGaps.setStatus("current")
_EsaProbeHistoryOutOfSeqErrs_Type = PerfCounter64
_EsaProbeHistoryOutOfSeqErrs_Object = MibTableColumn
esaProbeHistoryOutOfSeqErrs = _EsaProbeHistoryOutOfSeqErrs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 18),
    _EsaProbeHistoryOutOfSeqErrs_Type()
)
esaProbeHistoryOutOfSeqErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistoryOutOfSeqErrs.setStatus("current")
_EsaProbeHistoryMinRoundTripDelay_Type = Unsigned32
_EsaProbeHistoryMinRoundTripDelay_Object = MibTableColumn
esaProbeHistoryMinRoundTripDelay = _EsaProbeHistoryMinRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 19),
    _EsaProbeHistoryMinRoundTripDelay_Type()
)
esaProbeHistoryMinRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistoryMinRoundTripDelay.setStatus("current")
_EsaProbeHistoryMaxRoundTripDelay_Type = Unsigned32
_EsaProbeHistoryMaxRoundTripDelay_Object = MibTableColumn
esaProbeHistoryMaxRoundTripDelay = _EsaProbeHistoryMaxRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 20),
    _EsaProbeHistoryMaxRoundTripDelay_Type()
)
esaProbeHistoryMaxRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistoryMaxRoundTripDelay.setStatus("current")
_EsaProbeHistoryAvgRoundTripDelay_Type = Unsigned32
_EsaProbeHistoryAvgRoundTripDelay_Object = MibTableColumn
esaProbeHistoryAvgRoundTripDelay = _EsaProbeHistoryAvgRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 21),
    _EsaProbeHistoryAvgRoundTripDelay_Type()
)
esaProbeHistoryAvgRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistoryAvgRoundTripDelay.setStatus("current")
_EsaProbeHistorySumRoundTripDelay_Type = PerfCounter64
_EsaProbeHistorySumRoundTripDelay_Object = MibTableColumn
esaProbeHistorySumRoundTripDelay = _EsaProbeHistorySumRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 22),
    _EsaProbeHistorySumRoundTripDelay_Type()
)
esaProbeHistorySumRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistorySumRoundTripDelay.setStatus("current")
_EsaProbeHistorySumOfSqRoundTripDelay_Type = PerfCounter64
_EsaProbeHistorySumOfSqRoundTripDelay_Object = MibTableColumn
esaProbeHistorySumOfSqRoundTripDelay = _EsaProbeHistorySumOfSqRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 23),
    _EsaProbeHistorySumOfSqRoundTripDelay_Type()
)
esaProbeHistorySumOfSqRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistorySumOfSqRoundTripDelay.setStatus("current")
_EsaProbeHistoryMinOnewayP2RDelay_Type = Unsigned32
_EsaProbeHistoryMinOnewayP2RDelay_Object = MibTableColumn
esaProbeHistoryMinOnewayP2RDelay = _EsaProbeHistoryMinOnewayP2RDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 24),
    _EsaProbeHistoryMinOnewayP2RDelay_Type()
)
esaProbeHistoryMinOnewayP2RDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistoryMinOnewayP2RDelay.setStatus("current")
_EsaProbeHistoryMaxOnewayP2RDelay_Type = Unsigned32
_EsaProbeHistoryMaxOnewayP2RDelay_Object = MibTableColumn
esaProbeHistoryMaxOnewayP2RDelay = _EsaProbeHistoryMaxOnewayP2RDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 25),
    _EsaProbeHistoryMaxOnewayP2RDelay_Type()
)
esaProbeHistoryMaxOnewayP2RDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistoryMaxOnewayP2RDelay.setStatus("current")
_EsaProbeHistoryAvgOnewayP2RDelay_Type = Unsigned32
_EsaProbeHistoryAvgOnewayP2RDelay_Object = MibTableColumn
esaProbeHistoryAvgOnewayP2RDelay = _EsaProbeHistoryAvgOnewayP2RDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 26),
    _EsaProbeHistoryAvgOnewayP2RDelay_Type()
)
esaProbeHistoryAvgOnewayP2RDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistoryAvgOnewayP2RDelay.setStatus("current")
_EsaProbeHistorySumOnewayP2RDelay_Type = PerfCounter64
_EsaProbeHistorySumOnewayP2RDelay_Object = MibTableColumn
esaProbeHistorySumOnewayP2RDelay = _EsaProbeHistorySumOnewayP2RDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 27),
    _EsaProbeHistorySumOnewayP2RDelay_Type()
)
esaProbeHistorySumOnewayP2RDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistorySumOnewayP2RDelay.setStatus("current")
_EsaProbeHistorySumOfSqOnewayP2RDelay_Type = PerfCounter64
_EsaProbeHistorySumOfSqOnewayP2RDelay_Object = MibTableColumn
esaProbeHistorySumOfSqOnewayP2RDelay = _EsaProbeHistorySumOfSqOnewayP2RDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 28),
    _EsaProbeHistorySumOfSqOnewayP2RDelay_Type()
)
esaProbeHistorySumOfSqOnewayP2RDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistorySumOfSqOnewayP2RDelay.setStatus("current")
_EsaProbeHistoryMinOnewayR2PDelay_Type = Unsigned32
_EsaProbeHistoryMinOnewayR2PDelay_Object = MibTableColumn
esaProbeHistoryMinOnewayR2PDelay = _EsaProbeHistoryMinOnewayR2PDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 29),
    _EsaProbeHistoryMinOnewayR2PDelay_Type()
)
esaProbeHistoryMinOnewayR2PDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistoryMinOnewayR2PDelay.setStatus("current")
_EsaProbeHistoryMaxOnewayR2PDelay_Type = Unsigned32
_EsaProbeHistoryMaxOnewayR2PDelay_Object = MibTableColumn
esaProbeHistoryMaxOnewayR2PDelay = _EsaProbeHistoryMaxOnewayR2PDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 30),
    _EsaProbeHistoryMaxOnewayR2PDelay_Type()
)
esaProbeHistoryMaxOnewayR2PDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistoryMaxOnewayR2PDelay.setStatus("current")
_EsaProbeHistoryAvgOnewayR2PDelay_Type = Unsigned32
_EsaProbeHistoryAvgOnewayR2PDelay_Object = MibTableColumn
esaProbeHistoryAvgOnewayR2PDelay = _EsaProbeHistoryAvgOnewayR2PDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 31),
    _EsaProbeHistoryAvgOnewayR2PDelay_Type()
)
esaProbeHistoryAvgOnewayR2PDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistoryAvgOnewayR2PDelay.setStatus("current")
_EsaProbeHistorySumOnewayR2PDelay_Type = PerfCounter64
_EsaProbeHistorySumOnewayR2PDelay_Object = MibTableColumn
esaProbeHistorySumOnewayR2PDelay = _EsaProbeHistorySumOnewayR2PDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 32),
    _EsaProbeHistorySumOnewayR2PDelay_Type()
)
esaProbeHistorySumOnewayR2PDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistorySumOnewayR2PDelay.setStatus("current")
_EsaProbeHistorySumOfSqOnewayR2PDelay_Type = PerfCounter64
_EsaProbeHistorySumOfSqOnewayR2PDelay_Object = MibTableColumn
esaProbeHistorySumOfSqOnewayR2PDelay = _EsaProbeHistorySumOfSqOnewayR2PDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 33),
    _EsaProbeHistorySumOfSqOnewayR2PDelay_Type()
)
esaProbeHistorySumOfSqOnewayR2PDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistorySumOfSqOnewayR2PDelay.setStatus("current")
_EsaProbeHistoryMinPosP2RJitter_Type = Unsigned32
_EsaProbeHistoryMinPosP2RJitter_Object = MibTableColumn
esaProbeHistoryMinPosP2RJitter = _EsaProbeHistoryMinPosP2RJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 34),
    _EsaProbeHistoryMinPosP2RJitter_Type()
)
esaProbeHistoryMinPosP2RJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistoryMinPosP2RJitter.setStatus("current")
_EsaProbeHistoryMaxPosP2RJitter_Type = Unsigned32
_EsaProbeHistoryMaxPosP2RJitter_Object = MibTableColumn
esaProbeHistoryMaxPosP2RJitter = _EsaProbeHistoryMaxPosP2RJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 35),
    _EsaProbeHistoryMaxPosP2RJitter_Type()
)
esaProbeHistoryMaxPosP2RJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistoryMaxPosP2RJitter.setStatus("current")
_EsaProbeHistoryNumPosP2RJitter_Type = PerfCounter64
_EsaProbeHistoryNumPosP2RJitter_Object = MibTableColumn
esaProbeHistoryNumPosP2RJitter = _EsaProbeHistoryNumPosP2RJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 36),
    _EsaProbeHistoryNumPosP2RJitter_Type()
)
esaProbeHistoryNumPosP2RJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistoryNumPosP2RJitter.setStatus("current")
_EsaProbeHistorySumPosP2RJitter_Type = PerfCounter64
_EsaProbeHistorySumPosP2RJitter_Object = MibTableColumn
esaProbeHistorySumPosP2RJitter = _EsaProbeHistorySumPosP2RJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 37),
    _EsaProbeHistorySumPosP2RJitter_Type()
)
esaProbeHistorySumPosP2RJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistorySumPosP2RJitter.setStatus("current")
_EsaProbeHistorySumOfSqPosP2RJitter_Type = PerfCounter64
_EsaProbeHistorySumOfSqPosP2RJitter_Object = MibTableColumn
esaProbeHistorySumOfSqPosP2RJitter = _EsaProbeHistorySumOfSqPosP2RJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 38),
    _EsaProbeHistorySumOfSqPosP2RJitter_Type()
)
esaProbeHistorySumOfSqPosP2RJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistorySumOfSqPosP2RJitter.setStatus("current")
_EsaProbeHistoryMinNegP2RJitter_Type = Unsigned32
_EsaProbeHistoryMinNegP2RJitter_Object = MibTableColumn
esaProbeHistoryMinNegP2RJitter = _EsaProbeHistoryMinNegP2RJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 39),
    _EsaProbeHistoryMinNegP2RJitter_Type()
)
esaProbeHistoryMinNegP2RJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistoryMinNegP2RJitter.setStatus("current")
_EsaProbeHistoryMaxNegP2RJitter_Type = Unsigned32
_EsaProbeHistoryMaxNegP2RJitter_Object = MibTableColumn
esaProbeHistoryMaxNegP2RJitter = _EsaProbeHistoryMaxNegP2RJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 40),
    _EsaProbeHistoryMaxNegP2RJitter_Type()
)
esaProbeHistoryMaxNegP2RJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistoryMaxNegP2RJitter.setStatus("current")
_EsaProbeHistoryNumNegP2RJitter_Type = PerfCounter64
_EsaProbeHistoryNumNegP2RJitter_Object = MibTableColumn
esaProbeHistoryNumNegP2RJitter = _EsaProbeHistoryNumNegP2RJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 41),
    _EsaProbeHistoryNumNegP2RJitter_Type()
)
esaProbeHistoryNumNegP2RJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistoryNumNegP2RJitter.setStatus("current")
_EsaProbeHistorySumNegP2RJitter_Type = PerfCounter64
_EsaProbeHistorySumNegP2RJitter_Object = MibTableColumn
esaProbeHistorySumNegP2RJitter = _EsaProbeHistorySumNegP2RJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 42),
    _EsaProbeHistorySumNegP2RJitter_Type()
)
esaProbeHistorySumNegP2RJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistorySumNegP2RJitter.setStatus("current")
_EsaProbeHistorySumOfSqNegP2RJitter_Type = PerfCounter64
_EsaProbeHistorySumOfSqNegP2RJitter_Object = MibTableColumn
esaProbeHistorySumOfSqNegP2RJitter = _EsaProbeHistorySumOfSqNegP2RJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 43),
    _EsaProbeHistorySumOfSqNegP2RJitter_Type()
)
esaProbeHistorySumOfSqNegP2RJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistorySumOfSqNegP2RJitter.setStatus("current")
_EsaProbeHistoryMinPosR2PJitter_Type = Unsigned32
_EsaProbeHistoryMinPosR2PJitter_Object = MibTableColumn
esaProbeHistoryMinPosR2PJitter = _EsaProbeHistoryMinPosR2PJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 44),
    _EsaProbeHistoryMinPosR2PJitter_Type()
)
esaProbeHistoryMinPosR2PJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistoryMinPosR2PJitter.setStatus("current")
_EsaProbeHistoryMaxPosR2PJitter_Type = Unsigned32
_EsaProbeHistoryMaxPosR2PJitter_Object = MibTableColumn
esaProbeHistoryMaxPosR2PJitter = _EsaProbeHistoryMaxPosR2PJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 45),
    _EsaProbeHistoryMaxPosR2PJitter_Type()
)
esaProbeHistoryMaxPosR2PJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistoryMaxPosR2PJitter.setStatus("current")
_EsaProbeHistoryNumPosR2PJitter_Type = PerfCounter64
_EsaProbeHistoryNumPosR2PJitter_Object = MibTableColumn
esaProbeHistoryNumPosR2PJitter = _EsaProbeHistoryNumPosR2PJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 46),
    _EsaProbeHistoryNumPosR2PJitter_Type()
)
esaProbeHistoryNumPosR2PJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistoryNumPosR2PJitter.setStatus("current")
_EsaProbeHistorySumPosR2PJitter_Type = PerfCounter64
_EsaProbeHistorySumPosR2PJitter_Object = MibTableColumn
esaProbeHistorySumPosR2PJitter = _EsaProbeHistorySumPosR2PJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 47),
    _EsaProbeHistorySumPosR2PJitter_Type()
)
esaProbeHistorySumPosR2PJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistorySumPosR2PJitter.setStatus("current")
_EsaProbeHistorySumOfSqPosR2PJitter_Type = PerfCounter64
_EsaProbeHistorySumOfSqPosR2PJitter_Object = MibTableColumn
esaProbeHistorySumOfSqPosR2PJitter = _EsaProbeHistorySumOfSqPosR2PJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 48),
    _EsaProbeHistorySumOfSqPosR2PJitter_Type()
)
esaProbeHistorySumOfSqPosR2PJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistorySumOfSqPosR2PJitter.setStatus("current")
_EsaProbeHistoryMinNegR2PJitter_Type = Unsigned32
_EsaProbeHistoryMinNegR2PJitter_Object = MibTableColumn
esaProbeHistoryMinNegR2PJitter = _EsaProbeHistoryMinNegR2PJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 49),
    _EsaProbeHistoryMinNegR2PJitter_Type()
)
esaProbeHistoryMinNegR2PJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistoryMinNegR2PJitter.setStatus("current")
_EsaProbeHistoryMaxNegR2PJitter_Type = Unsigned32
_EsaProbeHistoryMaxNegR2PJitter_Object = MibTableColumn
esaProbeHistoryMaxNegR2PJitter = _EsaProbeHistoryMaxNegR2PJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 50),
    _EsaProbeHistoryMaxNegR2PJitter_Type()
)
esaProbeHistoryMaxNegR2PJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistoryMaxNegR2PJitter.setStatus("current")
_EsaProbeHistoryNumNegR2PJitter_Type = PerfCounter64
_EsaProbeHistoryNumNegR2PJitter_Object = MibTableColumn
esaProbeHistoryNumNegR2PJitter = _EsaProbeHistoryNumNegR2PJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 51),
    _EsaProbeHistoryNumNegR2PJitter_Type()
)
esaProbeHistoryNumNegR2PJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistoryNumNegR2PJitter.setStatus("current")
_EsaProbeHistorySumNegR2PJitter_Type = PerfCounter64
_EsaProbeHistorySumNegR2PJitter_Object = MibTableColumn
esaProbeHistorySumNegR2PJitter = _EsaProbeHistorySumNegR2PJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 52),
    _EsaProbeHistorySumNegR2PJitter_Type()
)
esaProbeHistorySumNegR2PJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistorySumNegR2PJitter.setStatus("current")
_EsaProbeHistorySumOfSqNegR2PJitter_Type = PerfCounter64
_EsaProbeHistorySumOfSqNegR2PJitter_Object = MibTableColumn
esaProbeHistorySumOfSqNegR2PJitter = _EsaProbeHistorySumOfSqNegR2PJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 53),
    _EsaProbeHistorySumOfSqNegR2PJitter_Type()
)
esaProbeHistorySumOfSqNegR2PJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistorySumOfSqNegR2PJitter.setStatus("current")
_EsaProbeHistoryY1731P2RNegLossOccurrences_Type = PerfCounter64
_EsaProbeHistoryY1731P2RNegLossOccurrences_Object = MibTableColumn
esaProbeHistoryY1731P2RNegLossOccurrences = _EsaProbeHistoryY1731P2RNegLossOccurrences_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 54),
    _EsaProbeHistoryY1731P2RNegLossOccurrences_Type()
)
esaProbeHistoryY1731P2RNegLossOccurrences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistoryY1731P2RNegLossOccurrences.setStatus("current")
_EsaProbeHistoryY1731R2PNegLossOccurrences_Type = PerfCounter64
_EsaProbeHistoryY1731R2PNegLossOccurrences_Object = MibTableColumn
esaProbeHistoryY1731R2PNegLossOccurrences = _EsaProbeHistoryY1731R2PNegLossOccurrences_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 55),
    _EsaProbeHistoryY1731R2PNegLossOccurrences_Type()
)
esaProbeHistoryY1731R2PNegLossOccurrences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistoryY1731R2PNegLossOccurrences.setStatus("current")
_EsaProbeHistoryY1731RxLmSamples_Type = TruthValue
_EsaProbeHistoryY1731RxLmSamples_Object = MibTableColumn
esaProbeHistoryY1731RxLmSamples = _EsaProbeHistoryY1731RxLmSamples_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 56),
    _EsaProbeHistoryY1731RxLmSamples_Type()
)
esaProbeHistoryY1731RxLmSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistoryY1731RxLmSamples.setStatus("current")
_EsaProbeHistoryY1731RxDmSamples_Type = TruthValue
_EsaProbeHistoryY1731RxDmSamples_Object = MibTableColumn
esaProbeHistoryY1731RxDmSamples = _EsaProbeHistoryY1731RxDmSamples_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 57),
    _EsaProbeHistoryY1731RxDmSamples_Type()
)
esaProbeHistoryY1731RxDmSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistoryY1731RxDmSamples.setStatus("current")
_EsaProbeHistoryY1731P2RFrames_Type = PerfCounter64
_EsaProbeHistoryY1731P2RFrames_Object = MibTableColumn
esaProbeHistoryY1731P2RFrames = _EsaProbeHistoryY1731P2RFrames_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 58),
    _EsaProbeHistoryY1731P2RFrames_Type()
)
esaProbeHistoryY1731P2RFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistoryY1731P2RFrames.setStatus("current")
_EsaProbeHistoryY1731R2PFrames_Type = PerfCounter64
_EsaProbeHistoryY1731R2PFrames_Object = MibTableColumn
esaProbeHistoryY1731R2PFrames = _EsaProbeHistoryY1731R2PFrames_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 59),
    _EsaProbeHistoryY1731R2PFrames_Type()
)
esaProbeHistoryY1731R2PFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistoryY1731R2PFrames.setStatus("current")
_EsaProbeHistoryAvgAbsP2RJitter_Type = Unsigned32
_EsaProbeHistoryAvgAbsP2RJitter_Object = MibTableColumn
esaProbeHistoryAvgAbsP2RJitter = _EsaProbeHistoryAvgAbsP2RJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 60),
    _EsaProbeHistoryAvgAbsP2RJitter_Type()
)
esaProbeHistoryAvgAbsP2RJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistoryAvgAbsP2RJitter.setStatus("current")
_EsaProbeHistoryAvgAbsR2PJitter_Type = Unsigned32
_EsaProbeHistoryAvgAbsR2PJitter_Object = MibTableColumn
esaProbeHistoryAvgAbsR2PJitter = _EsaProbeHistoryAvgAbsR2PJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 61),
    _EsaProbeHistoryAvgAbsR2PJitter_Type()
)
esaProbeHistoryAvgAbsR2PJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistoryAvgAbsR2PJitter.setStatus("current")
_EsaProbeHistoryMinAbsP2RJitter_Type = Unsigned32
_EsaProbeHistoryMinAbsP2RJitter_Object = MibTableColumn
esaProbeHistoryMinAbsP2RJitter = _EsaProbeHistoryMinAbsP2RJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 62),
    _EsaProbeHistoryMinAbsP2RJitter_Type()
)
esaProbeHistoryMinAbsP2RJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistoryMinAbsP2RJitter.setStatus("current")
_EsaProbeHistoryMinAbsR2PJitter_Type = Unsigned32
_EsaProbeHistoryMinAbsR2PJitter_Object = MibTableColumn
esaProbeHistoryMinAbsR2PJitter = _EsaProbeHistoryMinAbsR2PJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 63),
    _EsaProbeHistoryMinAbsR2PJitter_Type()
)
esaProbeHistoryMinAbsR2PJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistoryMinAbsR2PJitter.setStatus("current")
_EsaProbeHistoryMaxAbsP2RJitter_Type = Unsigned32
_EsaProbeHistoryMaxAbsP2RJitter_Object = MibTableColumn
esaProbeHistoryMaxAbsP2RJitter = _EsaProbeHistoryMaxAbsP2RJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 64),
    _EsaProbeHistoryMaxAbsP2RJitter_Type()
)
esaProbeHistoryMaxAbsP2RJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistoryMaxAbsP2RJitter.setStatus("current")
_EsaProbeHistoryMaxAbsR2PJitter_Type = Unsigned32
_EsaProbeHistoryMaxAbsR2PJitter_Object = MibTableColumn
esaProbeHistoryMaxAbsR2PJitter = _EsaProbeHistoryMaxAbsR2PJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 65),
    _EsaProbeHistoryMaxAbsR2PJitter_Type()
)
esaProbeHistoryMaxAbsR2PJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistoryMaxAbsR2PJitter.setStatus("current")
_EsaProbeHistoryNumAbsP2RJitter_Type = PerfCounter64
_EsaProbeHistoryNumAbsP2RJitter_Object = MibTableColumn
esaProbeHistoryNumAbsP2RJitter = _EsaProbeHistoryNumAbsP2RJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 66),
    _EsaProbeHistoryNumAbsP2RJitter_Type()
)
esaProbeHistoryNumAbsP2RJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistoryNumAbsP2RJitter.setStatus("current")
_EsaProbeHistoryNumAbsR2PJitter_Type = PerfCounter64
_EsaProbeHistoryNumAbsR2PJitter_Object = MibTableColumn
esaProbeHistoryNumAbsR2PJitter = _EsaProbeHistoryNumAbsR2PJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 67),
    _EsaProbeHistoryNumAbsR2PJitter_Type()
)
esaProbeHistoryNumAbsR2PJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistoryNumAbsR2PJitter.setStatus("current")
_EsaProbeHistorySumAbsP2RJitter_Type = PerfCounter64
_EsaProbeHistorySumAbsP2RJitter_Object = MibTableColumn
esaProbeHistorySumAbsP2RJitter = _EsaProbeHistorySumAbsP2RJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 68),
    _EsaProbeHistorySumAbsP2RJitter_Type()
)
esaProbeHistorySumAbsP2RJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistorySumAbsP2RJitter.setStatus("current")
_EsaProbeHistorySumAbsR2PJitter_Type = PerfCounter64
_EsaProbeHistorySumAbsR2PJitter_Object = MibTableColumn
esaProbeHistorySumAbsR2PJitter = _EsaProbeHistorySumAbsR2PJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 69),
    _EsaProbeHistorySumAbsR2PJitter_Type()
)
esaProbeHistorySumAbsR2PJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistorySumAbsR2PJitter.setStatus("current")
_EsaProbeHistorySumOfSqAbsP2RJitter_Type = PerfCounter64
_EsaProbeHistorySumOfSqAbsP2RJitter_Object = MibTableColumn
esaProbeHistorySumOfSqAbsP2RJitter = _EsaProbeHistorySumOfSqAbsP2RJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 70),
    _EsaProbeHistorySumOfSqAbsP2RJitter_Type()
)
esaProbeHistorySumOfSqAbsP2RJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistorySumOfSqAbsP2RJitter.setStatus("current")
_EsaProbeHistorySumOfSqAbsR2PJitter_Type = PerfCounter64
_EsaProbeHistorySumOfSqAbsR2PJitter_Object = MibTableColumn
esaProbeHistorySumOfSqAbsR2PJitter = _EsaProbeHistorySumOfSqAbsR2PJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 8, 1, 71),
    _EsaProbeHistorySumOfSqAbsR2PJitter_Type()
)
esaProbeHistorySumOfSqAbsR2PJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeHistorySumOfSqAbsR2PJitter.setStatus("current")
_EsaProbeDistStatsConfigTable_Object = MibTable
esaProbeDistStatsConfigTable = _EsaProbeDistStatsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 9)
)
if mibBuilder.loadTexts:
    esaProbeDistStatsConfigTable.setStatus("current")
_EsaProbeDistStatsConfigEntry_Object = MibTableRow
esaProbeDistStatsConfigEntry = _EsaProbeDistStatsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 9, 1)
)
esaProbeDistStatsConfigEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-SA-MIB", "esaProbeIndex"),
    (0, "CM-SA-MIB", "esaProbeDistStatsConfigIndex"),
)
if mibBuilder.loadTexts:
    esaProbeDistStatsConfigEntry.setStatus("current")


class _EsaProbeDistStatsConfigIndex_Type(Integer32):
    """Custom type esaProbeDistStatsConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_EsaProbeDistStatsConfigIndex_Type.__name__ = "Integer32"
_EsaProbeDistStatsConfigIndex_Object = MibTableColumn
esaProbeDistStatsConfigIndex = _EsaProbeDistStatsConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 9, 1, 1),
    _EsaProbeDistStatsConfigIndex_Type()
)
esaProbeDistStatsConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeDistStatsConfigIndex.setStatus("current")
_EsaProbeDistStatsConfigType_Type = EsaProbeDistStatsType
_EsaProbeDistStatsConfigType_Object = MibTableColumn
esaProbeDistStatsConfigType = _EsaProbeDistStatsConfigType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 9, 1, 2),
    _EsaProbeDistStatsConfigType_Type()
)
esaProbeDistStatsConfigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeDistStatsConfigType.setStatus("current")
_EsaProbeDistStatsConfigMinVal_Type = Integer32
_EsaProbeDistStatsConfigMinVal_Object = MibTableColumn
esaProbeDistStatsConfigMinVal = _EsaProbeDistStatsConfigMinVal_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 9, 1, 3),
    _EsaProbeDistStatsConfigMinVal_Type()
)
esaProbeDistStatsConfigMinVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esaProbeDistStatsConfigMinVal.setStatus("current")
_EsaProbeDistStatsConfigMaxVal_Type = Integer32
_EsaProbeDistStatsConfigMaxVal_Object = MibTableColumn
esaProbeDistStatsConfigMaxVal = _EsaProbeDistStatsConfigMaxVal_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 9, 1, 4),
    _EsaProbeDistStatsConfigMaxVal_Type()
)
esaProbeDistStatsConfigMaxVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esaProbeDistStatsConfigMaxVal.setStatus("current")
_EsaProbeDistStatsConfigNumBins_Type = Unsigned32
_EsaProbeDistStatsConfigNumBins_Object = MibTableColumn
esaProbeDistStatsConfigNumBins = _EsaProbeDistStatsConfigNumBins_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 9, 1, 5),
    _EsaProbeDistStatsConfigNumBins_Type()
)
esaProbeDistStatsConfigNumBins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esaProbeDistStatsConfigNumBins.setStatus("current")
_EsaProbeDistStatsConfigLowBoundOfBin1_Type = Integer32
_EsaProbeDistStatsConfigLowBoundOfBin1_Object = MibTableColumn
esaProbeDistStatsConfigLowBoundOfBin1 = _EsaProbeDistStatsConfigLowBoundOfBin1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 9, 1, 6),
    _EsaProbeDistStatsConfigLowBoundOfBin1_Type()
)
esaProbeDistStatsConfigLowBoundOfBin1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esaProbeDistStatsConfigLowBoundOfBin1.setStatus("current")
_EsaProbeDistStatsConfigLowBoundOfBin2_Type = Integer32
_EsaProbeDistStatsConfigLowBoundOfBin2_Object = MibTableColumn
esaProbeDistStatsConfigLowBoundOfBin2 = _EsaProbeDistStatsConfigLowBoundOfBin2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 9, 1, 7),
    _EsaProbeDistStatsConfigLowBoundOfBin2_Type()
)
esaProbeDistStatsConfigLowBoundOfBin2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esaProbeDistStatsConfigLowBoundOfBin2.setStatus("current")
_EsaProbeDistStatsConfigLowBoundOfBin3_Type = Integer32
_EsaProbeDistStatsConfigLowBoundOfBin3_Object = MibTableColumn
esaProbeDistStatsConfigLowBoundOfBin3 = _EsaProbeDistStatsConfigLowBoundOfBin3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 9, 1, 8),
    _EsaProbeDistStatsConfigLowBoundOfBin3_Type()
)
esaProbeDistStatsConfigLowBoundOfBin3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esaProbeDistStatsConfigLowBoundOfBin3.setStatus("current")
_EsaProbeDistStatsConfigLowBoundOfBin4_Type = Integer32
_EsaProbeDistStatsConfigLowBoundOfBin4_Object = MibTableColumn
esaProbeDistStatsConfigLowBoundOfBin4 = _EsaProbeDistStatsConfigLowBoundOfBin4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 9, 1, 9),
    _EsaProbeDistStatsConfigLowBoundOfBin4_Type()
)
esaProbeDistStatsConfigLowBoundOfBin4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esaProbeDistStatsConfigLowBoundOfBin4.setStatus("current")
_EsaProbeDistStatsConfigLowBoundOfBin5_Type = Integer32
_EsaProbeDistStatsConfigLowBoundOfBin5_Object = MibTableColumn
esaProbeDistStatsConfigLowBoundOfBin5 = _EsaProbeDistStatsConfigLowBoundOfBin5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 9, 1, 10),
    _EsaProbeDistStatsConfigLowBoundOfBin5_Type()
)
esaProbeDistStatsConfigLowBoundOfBin5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esaProbeDistStatsConfigLowBoundOfBin5.setStatus("current")
_EsaProbeDistStatsConfigLowBoundOfBin6_Type = Integer32
_EsaProbeDistStatsConfigLowBoundOfBin6_Object = MibTableColumn
esaProbeDistStatsConfigLowBoundOfBin6 = _EsaProbeDistStatsConfigLowBoundOfBin6_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 9, 1, 11),
    _EsaProbeDistStatsConfigLowBoundOfBin6_Type()
)
esaProbeDistStatsConfigLowBoundOfBin6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esaProbeDistStatsConfigLowBoundOfBin6.setStatus("current")
_EsaProbeDistStatsConfigLowBoundOfBin7_Type = Integer32
_EsaProbeDistStatsConfigLowBoundOfBin7_Object = MibTableColumn
esaProbeDistStatsConfigLowBoundOfBin7 = _EsaProbeDistStatsConfigLowBoundOfBin7_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 9, 1, 12),
    _EsaProbeDistStatsConfigLowBoundOfBin7_Type()
)
esaProbeDistStatsConfigLowBoundOfBin7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esaProbeDistStatsConfigLowBoundOfBin7.setStatus("current")
_EsaProbeDistStatsConfigLowBoundOfBin8_Type = Integer32
_EsaProbeDistStatsConfigLowBoundOfBin8_Object = MibTableColumn
esaProbeDistStatsConfigLowBoundOfBin8 = _EsaProbeDistStatsConfigLowBoundOfBin8_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 9, 1, 13),
    _EsaProbeDistStatsConfigLowBoundOfBin8_Type()
)
esaProbeDistStatsConfigLowBoundOfBin8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esaProbeDistStatsConfigLowBoundOfBin8.setStatus("current")
_EsaProbeDistStatsConfigLowBoundOfBin9_Type = Integer32
_EsaProbeDistStatsConfigLowBoundOfBin9_Object = MibTableColumn
esaProbeDistStatsConfigLowBoundOfBin9 = _EsaProbeDistStatsConfigLowBoundOfBin9_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 9, 1, 14),
    _EsaProbeDistStatsConfigLowBoundOfBin9_Type()
)
esaProbeDistStatsConfigLowBoundOfBin9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esaProbeDistStatsConfigLowBoundOfBin9.setStatus("current")
_EsaProbeDistStatsTable_Object = MibTable
esaProbeDistStatsTable = _EsaProbeDistStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 10)
)
if mibBuilder.loadTexts:
    esaProbeDistStatsTable.setStatus("current")
_EsaProbeDistStatsEntry_Object = MibTableRow
esaProbeDistStatsEntry = _EsaProbeDistStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 10, 1)
)
esaProbeDistStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-SA-MIB", "esaProbeIndex"),
    (0, "CM-SA-MIB", "esaProbeDistStatsConfigIndex"),
    (0, "CM-SA-MIB", "esaProbeDistStatsDestinationIndex"),
    (0, "CM-SA-MIB", "esaProbeDistStatsCOSIndex"),
)
if mibBuilder.loadTexts:
    esaProbeDistStatsEntry.setStatus("current")
_EsaProbeDistStatsDestinationIndex_Type = Integer32
_EsaProbeDistStatsDestinationIndex_Object = MibTableColumn
esaProbeDistStatsDestinationIndex = _EsaProbeDistStatsDestinationIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 10, 1, 1),
    _EsaProbeDistStatsDestinationIndex_Type()
)
esaProbeDistStatsDestinationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeDistStatsDestinationIndex.setStatus("current")
_EsaProbeDistStatsCOSIndex_Type = Integer32
_EsaProbeDistStatsCOSIndex_Object = MibTableColumn
esaProbeDistStatsCOSIndex = _EsaProbeDistStatsCOSIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 10, 1, 2),
    _EsaProbeDistStatsCOSIndex_Type()
)
esaProbeDistStatsCOSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeDistStatsCOSIndex.setStatus("current")
_EsaProbeDistStatsAction_Type = CmPmBinAction
_EsaProbeDistStatsAction_Object = MibTableColumn
esaProbeDistStatsAction = _EsaProbeDistStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 10, 1, 3),
    _EsaProbeDistStatsAction_Type()
)
esaProbeDistStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esaProbeDistStatsAction.setStatus("current")
_EsaProbeDistStatsCOS_Type = ClassOfServiceType
_EsaProbeDistStatsCOS_Object = MibTableColumn
esaProbeDistStatsCOS = _EsaProbeDistStatsCOS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 10, 1, 4),
    _EsaProbeDistStatsCOS_Type()
)
esaProbeDistStatsCOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeDistStatsCOS.setStatus("current")
_EsaProbeDistStatsNumBins_Type = Integer32
_EsaProbeDistStatsNumBins_Object = MibTableColumn
esaProbeDistStatsNumBins = _EsaProbeDistStatsNumBins_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 10, 1, 5),
    _EsaProbeDistStatsNumBins_Type()
)
esaProbeDistStatsNumBins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeDistStatsNumBins.setStatus("current")
_EsaProbeDistStatsLTMin_Type = PerfCounter64
_EsaProbeDistStatsLTMin_Object = MibTableColumn
esaProbeDistStatsLTMin = _EsaProbeDistStatsLTMin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 10, 1, 6),
    _EsaProbeDistStatsLTMin_Type()
)
esaProbeDistStatsLTMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeDistStatsLTMin.setStatus("current")
_EsaProbeDistStatsGTMax_Type = PerfCounter64
_EsaProbeDistStatsGTMax_Object = MibTableColumn
esaProbeDistStatsGTMax = _EsaProbeDistStatsGTMax_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 10, 1, 7),
    _EsaProbeDistStatsGTMax_Type()
)
esaProbeDistStatsGTMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeDistStatsGTMax.setStatus("current")
_EsaProbeDistStatsBinTable_Object = MibTable
esaProbeDistStatsBinTable = _EsaProbeDistStatsBinTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 11)
)
if mibBuilder.loadTexts:
    esaProbeDistStatsBinTable.setStatus("current")
_EsaProbeDistStatsBinEntry_Object = MibTableRow
esaProbeDistStatsBinEntry = _EsaProbeDistStatsBinEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 11, 1)
)
esaProbeDistStatsBinEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-SA-MIB", "esaProbeIndex"),
    (0, "CM-SA-MIB", "esaProbeDistStatsConfigIndex"),
    (0, "CM-SA-MIB", "esaProbeDistStatsDestinationIndex"),
    (0, "CM-SA-MIB", "esaProbeDistStatsCOSIndex"),
    (0, "CM-SA-MIB", "esaProbeDistStatsBinIndex"),
)
if mibBuilder.loadTexts:
    esaProbeDistStatsBinEntry.setStatus("current")


class _EsaProbeDistStatsBinIndex_Type(Integer32):
    """Custom type esaProbeDistStatsBinIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EsaProbeDistStatsBinIndex_Type.__name__ = "Integer32"
_EsaProbeDistStatsBinIndex_Object = MibTableColumn
esaProbeDistStatsBinIndex = _EsaProbeDistStatsBinIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 11, 1, 1),
    _EsaProbeDistStatsBinIndex_Type()
)
esaProbeDistStatsBinIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeDistStatsBinIndex.setStatus("current")
_EsaProbeDistStatsBinLower_Type = Integer32
_EsaProbeDistStatsBinLower_Object = MibTableColumn
esaProbeDistStatsBinLower = _EsaProbeDistStatsBinLower_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 11, 1, 2),
    _EsaProbeDistStatsBinLower_Type()
)
esaProbeDistStatsBinLower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeDistStatsBinLower.setStatus("current")
_EsaProbeDistStatsBinUpper_Type = Integer32
_EsaProbeDistStatsBinUpper_Object = MibTableColumn
esaProbeDistStatsBinUpper = _EsaProbeDistStatsBinUpper_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 11, 1, 3),
    _EsaProbeDistStatsBinUpper_Type()
)
esaProbeDistStatsBinUpper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeDistStatsBinUpper.setStatus("current")
_EsaProbeDistStatsBinNumSamples_Type = PerfCounter64
_EsaProbeDistStatsBinNumSamples_Object = MibTableColumn
esaProbeDistStatsBinNumSamples = _EsaProbeDistStatsBinNumSamples_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 11, 1, 4),
    _EsaProbeDistStatsBinNumSamples_Type()
)
esaProbeDistStatsBinNumSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeDistStatsBinNumSamples.setStatus("current")
_EsaProbeDistHistoryTable_Object = MibTable
esaProbeDistHistoryTable = _EsaProbeDistHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 12)
)
if mibBuilder.loadTexts:
    esaProbeDistHistoryTable.setStatus("current")
_EsaProbeDistHistoryEntry_Object = MibTableRow
esaProbeDistHistoryEntry = _EsaProbeDistHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 12, 1)
)
esaProbeDistHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-SA-MIB", "esaProbeIndex"),
    (0, "CM-SA-MIB", "esaProbeDistStatsConfigIndex"),
    (0, "CM-SA-MIB", "esaProbeDistHistoryDestinationIndex"),
    (0, "CM-SA-MIB", "esaProbeDistHistoryCOSIndex"),
    (0, "CM-SA-MIB", "esaProbeDistHistoryIndex"),
)
if mibBuilder.loadTexts:
    esaProbeDistHistoryEntry.setStatus("current")
_EsaProbeDistHistoryDestinationIndex_Type = Integer32
_EsaProbeDistHistoryDestinationIndex_Object = MibTableColumn
esaProbeDistHistoryDestinationIndex = _EsaProbeDistHistoryDestinationIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 12, 1, 1),
    _EsaProbeDistHistoryDestinationIndex_Type()
)
esaProbeDistHistoryDestinationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeDistHistoryDestinationIndex.setStatus("current")
_EsaProbeDistHistoryCOSIndex_Type = Integer32
_EsaProbeDistHistoryCOSIndex_Object = MibTableColumn
esaProbeDistHistoryCOSIndex = _EsaProbeDistHistoryCOSIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 12, 1, 2),
    _EsaProbeDistHistoryCOSIndex_Type()
)
esaProbeDistHistoryCOSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeDistHistoryCOSIndex.setStatus("current")


class _EsaProbeDistHistoryIndex_Type(Integer32):
    """Custom type esaProbeDistHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EsaProbeDistHistoryIndex_Type.__name__ = "Integer32"
_EsaProbeDistHistoryIndex_Object = MibTableColumn
esaProbeDistHistoryIndex = _EsaProbeDistHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 12, 1, 3),
    _EsaProbeDistHistoryIndex_Type()
)
esaProbeDistHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeDistHistoryIndex.setStatus("current")
_EsaProbeDistHistoryTime_Type = DateAndTime
_EsaProbeDistHistoryTime_Object = MibTableColumn
esaProbeDistHistoryTime = _EsaProbeDistHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 12, 1, 4),
    _EsaProbeDistHistoryTime_Type()
)
esaProbeDistHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeDistHistoryTime.setStatus("current")
_EsaProbeDistHistoryAction_Type = CmPmBinAction
_EsaProbeDistHistoryAction_Object = MibTableColumn
esaProbeDistHistoryAction = _EsaProbeDistHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 12, 1, 5),
    _EsaProbeDistHistoryAction_Type()
)
esaProbeDistHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esaProbeDistHistoryAction.setStatus("current")
_EsaProbeDistHistoryCOS_Type = ClassOfServiceType
_EsaProbeDistHistoryCOS_Object = MibTableColumn
esaProbeDistHistoryCOS = _EsaProbeDistHistoryCOS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 12, 1, 6),
    _EsaProbeDistHistoryCOS_Type()
)
esaProbeDistHistoryCOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeDistHistoryCOS.setStatus("current")
_EsaProbeDistHistoryNumBins_Type = Integer32
_EsaProbeDistHistoryNumBins_Object = MibTableColumn
esaProbeDistHistoryNumBins = _EsaProbeDistHistoryNumBins_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 12, 1, 7),
    _EsaProbeDistHistoryNumBins_Type()
)
esaProbeDistHistoryNumBins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeDistHistoryNumBins.setStatus("current")
_EsaProbeDistHistoryLTMin_Type = PerfCounter64
_EsaProbeDistHistoryLTMin_Object = MibTableColumn
esaProbeDistHistoryLTMin = _EsaProbeDistHistoryLTMin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 12, 1, 8),
    _EsaProbeDistHistoryLTMin_Type()
)
esaProbeDistHistoryLTMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeDistHistoryLTMin.setStatus("current")
_EsaProbeDistHistoryGTMax_Type = PerfCounter64
_EsaProbeDistHistoryGTMax_Object = MibTableColumn
esaProbeDistHistoryGTMax = _EsaProbeDistHistoryGTMax_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 12, 1, 9),
    _EsaProbeDistHistoryGTMax_Type()
)
esaProbeDistHistoryGTMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeDistHistoryGTMax.setStatus("current")
_EsaProbeDistHistoryBinTable_Object = MibTable
esaProbeDistHistoryBinTable = _EsaProbeDistHistoryBinTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 13)
)
if mibBuilder.loadTexts:
    esaProbeDistHistoryBinTable.setStatus("current")
_EsaProbeDistHistoryBinEntry_Object = MibTableRow
esaProbeDistHistoryBinEntry = _EsaProbeDistHistoryBinEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 13, 1)
)
esaProbeDistHistoryBinEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-SA-MIB", "esaProbeIndex"),
    (0, "CM-SA-MIB", "esaProbeDistStatsConfigIndex"),
    (0, "CM-SA-MIB", "esaProbeDistHistoryDestinationIndex"),
    (0, "CM-SA-MIB", "esaProbeDistHistoryCOSIndex"),
    (0, "CM-SA-MIB", "esaProbeDistHistoryIndex"),
    (0, "CM-SA-MIB", "esaProbeDistHistoryBinIndex"),
)
if mibBuilder.loadTexts:
    esaProbeDistHistoryBinEntry.setStatus("current")


class _EsaProbeDistHistoryBinIndex_Type(Integer32):
    """Custom type esaProbeDistHistoryBinIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EsaProbeDistHistoryBinIndex_Type.__name__ = "Integer32"
_EsaProbeDistHistoryBinIndex_Object = MibTableColumn
esaProbeDistHistoryBinIndex = _EsaProbeDistHistoryBinIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 13, 1, 1),
    _EsaProbeDistHistoryBinIndex_Type()
)
esaProbeDistHistoryBinIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeDistHistoryBinIndex.setStatus("current")
_EsaProbeDistHistoryBinLower_Type = Integer32
_EsaProbeDistHistoryBinLower_Object = MibTableColumn
esaProbeDistHistoryBinLower = _EsaProbeDistHistoryBinLower_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 13, 1, 2),
    _EsaProbeDistHistoryBinLower_Type()
)
esaProbeDistHistoryBinLower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeDistHistoryBinLower.setStatus("current")
_EsaProbeDistHistoryBinUpper_Type = Integer32
_EsaProbeDistHistoryBinUpper_Object = MibTableColumn
esaProbeDistHistoryBinUpper = _EsaProbeDistHistoryBinUpper_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 13, 1, 3),
    _EsaProbeDistHistoryBinUpper_Type()
)
esaProbeDistHistoryBinUpper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeDistHistoryBinUpper.setStatus("current")
_EsaProbeDistHistoryBinNumSamples_Type = PerfCounter64
_EsaProbeDistHistoryBinNumSamples_Object = MibTableColumn
esaProbeDistHistoryBinNumSamples = _EsaProbeDistHistoryBinNumSamples_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 13, 1, 4),
    _EsaProbeDistHistoryBinNumSamples_Type()
)
esaProbeDistHistoryBinNumSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeDistHistoryBinNumSamples.setStatus("current")
_EsaProbeStatsThresholdTable_Object = MibTable
esaProbeStatsThresholdTable = _EsaProbeStatsThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 14)
)
if mibBuilder.loadTexts:
    esaProbeStatsThresholdTable.setStatus("current")
_EsaProbeStatsThresholdEntry_Object = MibTableRow
esaProbeStatsThresholdEntry = _EsaProbeStatsThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 14, 1)
)
esaProbeStatsThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-SA-MIB", "esaProbeIndex"),
    (0, "CM-SA-MIB", "esaProbeStatsThresholdIndex"),
)
if mibBuilder.loadTexts:
    esaProbeStatsThresholdEntry.setStatus("current")


class _EsaProbeStatsThresholdIndex_Type(Integer32):
    """Custom type esaProbeStatsThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EsaProbeStatsThresholdIndex_Type.__name__ = "Integer32"
_EsaProbeStatsThresholdIndex_Object = MibTableColumn
esaProbeStatsThresholdIndex = _EsaProbeStatsThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 14, 1, 1),
    _EsaProbeStatsThresholdIndex_Type()
)
esaProbeStatsThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsThresholdIndex.setStatus("current")
_EsaProbeStatsThresholdVariable_Type = VariablePointer
_EsaProbeStatsThresholdVariable_Object = MibTableColumn
esaProbeStatsThresholdVariable = _EsaProbeStatsThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 14, 1, 2),
    _EsaProbeStatsThresholdVariable_Type()
)
esaProbeStatsThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsThresholdVariable.setStatus("current")
_EsaProbeStatsThresholdAbsValueLo_Type = Unsigned32
_EsaProbeStatsThresholdAbsValueLo_Object = MibTableColumn
esaProbeStatsThresholdAbsValueLo = _EsaProbeStatsThresholdAbsValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 14, 1, 3),
    _EsaProbeStatsThresholdAbsValueLo_Type()
)
esaProbeStatsThresholdAbsValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esaProbeStatsThresholdAbsValueLo.setStatus("current")
_EsaProbeStatsThresholdAbsValueHi_Type = Unsigned32
_EsaProbeStatsThresholdAbsValueHi_Object = MibTableColumn
esaProbeStatsThresholdAbsValueHi = _EsaProbeStatsThresholdAbsValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 14, 1, 4),
    _EsaProbeStatsThresholdAbsValueHi_Type()
)
esaProbeStatsThresholdAbsValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esaProbeStatsThresholdAbsValueHi.setStatus("current")
_EsaProbeStatsThresholdMonValue_Type = PerfCounter64
_EsaProbeStatsThresholdMonValue_Object = MibTableColumn
esaProbeStatsThresholdMonValue = _EsaProbeStatsThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 14, 1, 5),
    _EsaProbeStatsThresholdMonValue_Type()
)
esaProbeStatsThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esaProbeStatsThresholdMonValue.setStatus("current")
_EsaProbeCOSConfigTable_Object = MibTable
esaProbeCOSConfigTable = _EsaProbeCOSConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 15)
)
if mibBuilder.loadTexts:
    esaProbeCOSConfigTable.setStatus("current")
_EsaProbeCOSConfigEntry_Object = MibTableRow
esaProbeCOSConfigEntry = _EsaProbeCOSConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 15, 1)
)
esaProbeCOSConfigEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-SA-MIB", "esaProbeIndex"),
    (0, "CM-SA-MIB", "esaProbeCOSConfigIndex"),
)
if mibBuilder.loadTexts:
    esaProbeCOSConfigEntry.setStatus("current")


class _EsaProbeCOSConfigIndex_Type(Integer32):
    """Custom type esaProbeCOSConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_EsaProbeCOSConfigIndex_Type.__name__ = "Integer32"
_EsaProbeCOSConfigIndex_Object = MibTableColumn
esaProbeCOSConfigIndex = _EsaProbeCOSConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 15, 1, 1),
    _EsaProbeCOSConfigIndex_Type()
)
esaProbeCOSConfigIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esaProbeCOSConfigIndex.setStatus("current")
_EsaProbeCOSConfigType_Type = ClassOfServiceType
_EsaProbeCOSConfigType_Object = MibTableColumn
esaProbeCOSConfigType = _EsaProbeCOSConfigType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 15, 1, 2),
    _EsaProbeCOSConfigType_Type()
)
esaProbeCOSConfigType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esaProbeCOSConfigType.setStatus("current")
_EsaProbeCOSConfigInterval_Type = EsaProbePktIntervalType
_EsaProbeCOSConfigInterval_Object = MibTableColumn
esaProbeCOSConfigInterval = _EsaProbeCOSConfigInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 15, 1, 3),
    _EsaProbeCOSConfigInterval_Type()
)
esaProbeCOSConfigInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esaProbeCOSConfigInterval.setStatus("current")


class _EsaProbeCOSConfigPktSize_Type(Integer32):
    """Custom type esaProbeCOSConfigPktSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 9612),
    )


_EsaProbeCOSConfigPktSize_Type.__name__ = "Integer32"
_EsaProbeCOSConfigPktSize_Object = MibTableColumn
esaProbeCOSConfigPktSize = _EsaProbeCOSConfigPktSize_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 15, 1, 4),
    _EsaProbeCOSConfigPktSize_Type()
)
esaProbeCOSConfigPktSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esaProbeCOSConfigPktSize.setStatus("current")
_EsaProbeCOSConfigStorageType_Type = StorageType
_EsaProbeCOSConfigStorageType_Object = MibTableColumn
esaProbeCOSConfigStorageType = _EsaProbeCOSConfigStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 15, 1, 5),
    _EsaProbeCOSConfigStorageType_Type()
)
esaProbeCOSConfigStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esaProbeCOSConfigStorageType.setStatus("current")
_EsaProbeCOSConfigRowStatus_Type = RowStatus
_EsaProbeCOSConfigRowStatus_Object = MibTableColumn
esaProbeCOSConfigRowStatus = _EsaProbeCOSConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 15, 1, 6),
    _EsaProbeCOSConfigRowStatus_Type()
)
esaProbeCOSConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esaProbeCOSConfigRowStatus.setStatus("current")
_EsaProbeCOSConfigslmInterval_Type = EsaProbePktIntervalType
_EsaProbeCOSConfigslmInterval_Object = MibTableColumn
esaProbeCOSConfigslmInterval = _EsaProbeCOSConfigslmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 15, 1, 7),
    _EsaProbeCOSConfigslmInterval_Type()
)
esaProbeCOSConfigslmInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esaProbeCOSConfigslmInterval.setStatus("current")
_EsaProbeCOSConfigslmPktSize_Type = Integer32
_EsaProbeCOSConfigslmPktSize_Object = MibTableColumn
esaProbeCOSConfigslmPktSize = _EsaProbeCOSConfigslmPktSize_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 15, 1, 8),
    _EsaProbeCOSConfigslmPktSize_Type()
)
esaProbeCOSConfigslmPktSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esaProbeCOSConfigslmPktSize.setStatus("current")


class _EsaProbeCOSConfigSoamPmExtAvailFlrThreshold_Type(Unsigned32):
    """Custom type esaProbeCOSConfigSoamPmExtAvailFlrThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_EsaProbeCOSConfigSoamPmExtAvailFlrThreshold_Type.__name__ = "Unsigned32"
_EsaProbeCOSConfigSoamPmExtAvailFlrThreshold_Object = MibTableColumn
esaProbeCOSConfigSoamPmExtAvailFlrThreshold = _EsaProbeCOSConfigSoamPmExtAvailFlrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 15, 1, 9),
    _EsaProbeCOSConfigSoamPmExtAvailFlrThreshold_Type()
)
esaProbeCOSConfigSoamPmExtAvailFlrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esaProbeCOSConfigSoamPmExtAvailFlrThreshold.setStatus("current")


class _EsaProbeCOSConfigSoamPmExtFlrDeltaTNumLmPdus_Type(Unsigned32):
    """Custom type esaProbeCOSConfigSoamPmExtFlrDeltaTNumLmPdus based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_EsaProbeCOSConfigSoamPmExtFlrDeltaTNumLmPdus_Type.__name__ = "Unsigned32"
_EsaProbeCOSConfigSoamPmExtFlrDeltaTNumLmPdus_Object = MibTableColumn
esaProbeCOSConfigSoamPmExtFlrDeltaTNumLmPdus = _EsaProbeCOSConfigSoamPmExtFlrDeltaTNumLmPdus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 15, 1, 10),
    _EsaProbeCOSConfigSoamPmExtFlrDeltaTNumLmPdus_Type()
)
esaProbeCOSConfigSoamPmExtFlrDeltaTNumLmPdus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esaProbeCOSConfigSoamPmExtFlrDeltaTNumLmPdus.setStatus("current")


class _EsaProbeCOSConfigSoamPmExtConDeltaTsForAvail_Type(Unsigned32):
    """Custom type esaProbeCOSConfigSoamPmExtConDeltaTsForAvail based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_EsaProbeCOSConfigSoamPmExtConDeltaTsForAvail_Type.__name__ = "Unsigned32"
_EsaProbeCOSConfigSoamPmExtConDeltaTsForAvail_Object = MibTableColumn
esaProbeCOSConfigSoamPmExtConDeltaTsForAvail = _EsaProbeCOSConfigSoamPmExtConDeltaTsForAvail_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 15, 1, 11),
    _EsaProbeCOSConfigSoamPmExtConDeltaTsForAvail_Type()
)
esaProbeCOSConfigSoamPmExtConDeltaTsForAvail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esaProbeCOSConfigSoamPmExtConDeltaTsForAvail.setStatus("current")
_EsaProbeMultiDestinationTable_Object = MibTable
esaProbeMultiDestinationTable = _EsaProbeMultiDestinationTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 16)
)
if mibBuilder.loadTexts:
    esaProbeMultiDestinationTable.setStatus("current")
_EsaProbeMultiDestinationEntry_Object = MibTableRow
esaProbeMultiDestinationEntry = _EsaProbeMultiDestinationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 16, 1)
)
esaProbeMultiDestinationEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-SA-MIB", "esaProbeIndex"),
    (0, "CM-SA-MIB", "esaProbeDestinationIndex"),
)
if mibBuilder.loadTexts:
    esaProbeMultiDestinationEntry.setStatus("current")
_EsaProbeDestinationIndex_Type = Integer32
_EsaProbeDestinationIndex_Object = MibTableColumn
esaProbeDestinationIndex = _EsaProbeDestinationIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 16, 1, 1),
    _EsaProbeDestinationIndex_Type()
)
esaProbeDestinationIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esaProbeDestinationIndex.setStatus("current")
_EsaProbeDestinationMepType_Type = MepDestinationType
_EsaProbeDestinationMepType_Object = MibTableColumn
esaProbeDestinationMepType = _EsaProbeDestinationMepType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 16, 1, 2),
    _EsaProbeDestinationMepType_Type()
)
esaProbeDestinationMepType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esaProbeDestinationMepType.setStatus("current")
_EsaProbeDestinationMepMacAddr_Type = MacAddress
_EsaProbeDestinationMepMacAddr_Object = MibTableColumn
esaProbeDestinationMepMacAddr = _EsaProbeDestinationMepMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 16, 1, 3),
    _EsaProbeDestinationMepMacAddr_Type()
)
esaProbeDestinationMepMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esaProbeDestinationMepMacAddr.setStatus("current")
_EsaProbeDestinationMepId_Type = Dot1agCfmMepIdOrZero
_EsaProbeDestinationMepId_Object = MibTableColumn
esaProbeDestinationMepId = _EsaProbeDestinationMepId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 16, 1, 4),
    _EsaProbeDestinationMepId_Type()
)
esaProbeDestinationMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esaProbeDestinationMepId.setStatus("current")
_EsaProbeDestinationStorageType_Type = StorageType
_EsaProbeDestinationStorageType_Object = MibTableColumn
esaProbeDestinationStorageType = _EsaProbeDestinationStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 16, 1, 5),
    _EsaProbeDestinationStorageType_Type()
)
esaProbeDestinationStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esaProbeDestinationStorageType.setStatus("current")
_EsaProbeDestinationRowStatus_Type = RowStatus
_EsaProbeDestinationRowStatus_Object = MibTableColumn
esaProbeDestinationRowStatus = _EsaProbeDestinationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 16, 1, 6),
    _EsaProbeDestinationRowStatus_Type()
)
esaProbeDestinationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esaProbeDestinationRowStatus.setStatus("current")
_BertControlTable_Object = MibTable
bertControlTable = _BertControlTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 17)
)
if mibBuilder.loadTexts:
    bertControlTable.setStatus("current")
_BertControlEntry_Object = MibTableRow
bertControlEntry = _BertControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 17, 1)
)
bertControlEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-SA-MIB", "ecpaControlIndex"),
)
if mibBuilder.loadTexts:
    bertControlEntry.setStatus("current")
_BertControlIndex_Type = Integer32
_BertControlIndex_Object = MibTableColumn
bertControlIndex = _BertControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 17, 1, 1),
    _BertControlIndex_Type()
)
bertControlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bertControlIndex.setStatus("current")
_BertControlSourceEntity_Type = VariablePointer
_BertControlSourceEntity_Object = MibTableColumn
bertControlSourceEntity = _BertControlSourceEntity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 17, 1, 2),
    _BertControlSourceEntity_Type()
)
bertControlSourceEntity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bertControlSourceEntity.setStatus("current")
_BertControlTestMode_Type = BerTestMode
_BertControlTestMode_Object = MibTableColumn
bertControlTestMode = _BertControlTestMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 17, 1, 3),
    _BertControlTestMode_Type()
)
bertControlTestMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bertControlTestMode.setStatus("current")


class _BertControlDuration_Type(Integer32):
    """Custom type bertControlDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 259200),
    )


_BertControlDuration_Type.__name__ = "Integer32"
_BertControlDuration_Object = MibTableColumn
bertControlDuration = _BertControlDuration_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 17, 1, 4),
    _BertControlDuration_Type()
)
bertControlDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bertControlDuration.setStatus("current")
_BertControlStream_Type = Integer32
_BertControlStream_Object = MibTableColumn
bertControlStream = _BertControlStream_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 17, 1, 5),
    _BertControlStream_Type()
)
bertControlStream.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bertControlStream.setStatus("current")
_BertControlAction_Type = BertControlAction
_BertControlAction_Object = MibTableColumn
bertControlAction = _BertControlAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 17, 1, 6),
    _BertControlAction_Type()
)
bertControlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bertControlAction.setStatus("current")
_BertControlTestStatus_Type = BerTestStatus
_BertControlTestStatus_Object = MibTableColumn
bertControlTestStatus = _BertControlTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 17, 1, 7),
    _BertControlTestStatus_Type()
)
bertControlTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertControlTestStatus.setStatus("current")
_BertConfigStreamTable_Object = MibTable
bertConfigStreamTable = _BertConfigStreamTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 18)
)
if mibBuilder.loadTexts:
    bertConfigStreamTable.setStatus("current")
_BertConfigStreamEntry_Object = MibTableRow
bertConfigStreamEntry = _BertConfigStreamEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 18, 1)
)
bertConfigStreamEntry.setIndexNames(
    (0, "CM-SA-MIB", "bertConfigStreamIndex"),
)
if mibBuilder.loadTexts:
    bertConfigStreamEntry.setStatus("current")
_BertConfigStreamIndex_Type = Integer32
_BertConfigStreamIndex_Object = MibTableColumn
bertConfigStreamIndex = _BertConfigStreamIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 18, 1, 1),
    _BertConfigStreamIndex_Type()
)
bertConfigStreamIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bertConfigStreamIndex.setStatus("current")


class _BertConfigStreamName_Type(DisplayString):
    """Custom type bertConfigStreamName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BertConfigStreamName_Type.__name__ = "DisplayString"
_BertConfigStreamName_Object = MibTableColumn
bertConfigStreamName = _BertConfigStreamName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 18, 1, 2),
    _BertConfigStreamName_Type()
)
bertConfigStreamName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bertConfigStreamName.setStatus("current")
_BertConfigStreamTxPattern_Type = BertPattern
_BertConfigStreamTxPattern_Object = MibTableColumn
bertConfigStreamTxPattern = _BertConfigStreamTxPattern_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 18, 1, 3),
    _BertConfigStreamTxPattern_Type()
)
bertConfigStreamTxPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bertConfigStreamTxPattern.setStatus("current")
_BertConfigStreamErrInjectEnabled_Type = TruthValue
_BertConfigStreamErrInjectEnabled_Object = MibTableColumn
bertConfigStreamErrInjectEnabled = _BertConfigStreamErrInjectEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 18, 1, 4),
    _BertConfigStreamErrInjectEnabled_Type()
)
bertConfigStreamErrInjectEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bertConfigStreamErrInjectEnabled.setStatus("current")
_BertConfigStreamErrInjectRate_Type = BitErrRate
_BertConfigStreamErrInjectRate_Object = MibTableColumn
bertConfigStreamErrInjectRate = _BertConfigStreamErrInjectRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 18, 1, 5),
    _BertConfigStreamErrInjectRate_Type()
)
bertConfigStreamErrInjectRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bertConfigStreamErrInjectRate.setStatus("current")
_BertConfigStreamErrInjectRateMultiplier_Type = Integer32
_BertConfigStreamErrInjectRateMultiplier_Object = MibTableColumn
bertConfigStreamErrInjectRateMultiplier = _BertConfigStreamErrInjectRateMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 18, 1, 6),
    _BertConfigStreamErrInjectRateMultiplier_Type()
)
bertConfigStreamErrInjectRateMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bertConfigStreamErrInjectRateMultiplier.setStatus("current")
_BertConfigStreamUserPatternLength_Type = BertUserPatternLength
_BertConfigStreamUserPatternLength_Object = MibTableColumn
bertConfigStreamUserPatternLength = _BertConfigStreamUserPatternLength_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 18, 1, 7),
    _BertConfigStreamUserPatternLength_Type()
)
bertConfigStreamUserPatternLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bertConfigStreamUserPatternLength.setStatus("current")
_BertConfigStreamUserPattern_Type = DisplayString
_BertConfigStreamUserPattern_Object = MibTableColumn
bertConfigStreamUserPattern = _BertConfigStreamUserPattern_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 18, 1, 8),
    _BertConfigStreamUserPattern_Type()
)
bertConfigStreamUserPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bertConfigStreamUserPattern.setStatus("current")
_BertTestStreamTable_Object = MibTable
bertTestStreamTable = _BertTestStreamTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 19)
)
if mibBuilder.loadTexts:
    bertTestStreamTable.setStatus("current")
_BertTestStreamEntry_Object = MibTableRow
bertTestStreamEntry = _BertTestStreamEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 19, 1)
)
bertTestStreamEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-SA-MIB", "bertControlIndex"),
    (0, "CM-SA-MIB", "bertTestStreamIndex"),
)
if mibBuilder.loadTexts:
    bertTestStreamEntry.setStatus("current")
_BertTestStreamIndex_Type = Integer32
_BertTestStreamIndex_Object = MibTableColumn
bertTestStreamIndex = _BertTestStreamIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 19, 1, 1),
    _BertTestStreamIndex_Type()
)
bertTestStreamIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bertTestStreamIndex.setStatus("current")


class _BertTestStreamName_Type(DisplayString):
    """Custom type bertTestStreamName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BertTestStreamName_Type.__name__ = "DisplayString"
_BertTestStreamName_Object = MibTableColumn
bertTestStreamName = _BertTestStreamName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 19, 1, 2),
    _BertTestStreamName_Type()
)
bertTestStreamName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bertTestStreamName.setStatus("current")
_BertTestStreamTxPattern_Type = BertPattern
_BertTestStreamTxPattern_Object = MibTableColumn
bertTestStreamTxPattern = _BertTestStreamTxPattern_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 19, 1, 3),
    _BertTestStreamTxPattern_Type()
)
bertTestStreamTxPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertTestStreamTxPattern.setStatus("current")
_BertTestStreamErrInjectEnabled_Type = TruthValue
_BertTestStreamErrInjectEnabled_Object = MibTableColumn
bertTestStreamErrInjectEnabled = _BertTestStreamErrInjectEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 19, 1, 4),
    _BertTestStreamErrInjectEnabled_Type()
)
bertTestStreamErrInjectEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertTestStreamErrInjectEnabled.setStatus("current")
_BertTestStreamErrInjectRate_Type = BitErrRate
_BertTestStreamErrInjectRate_Object = MibTableColumn
bertTestStreamErrInjectRate = _BertTestStreamErrInjectRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 19, 1, 5),
    _BertTestStreamErrInjectRate_Type()
)
bertTestStreamErrInjectRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertTestStreamErrInjectRate.setStatus("current")
_BertTestStreamErrInjectRateMultiplier_Type = Integer32
_BertTestStreamErrInjectRateMultiplier_Object = MibTableColumn
bertTestStreamErrInjectRateMultiplier = _BertTestStreamErrInjectRateMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 19, 1, 6),
    _BertTestStreamErrInjectRateMultiplier_Type()
)
bertTestStreamErrInjectRateMultiplier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertTestStreamErrInjectRateMultiplier.setStatus("current")
_BertTestStreamUserPatternLength_Type = BertUserPatternLength
_BertTestStreamUserPatternLength_Object = MibTableColumn
bertTestStreamUserPatternLength = _BertTestStreamUserPatternLength_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 19, 1, 7),
    _BertTestStreamUserPatternLength_Type()
)
bertTestStreamUserPatternLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertTestStreamUserPatternLength.setStatus("current")
_BertTestStreamUserPattern_Type = DisplayString
_BertTestStreamUserPattern_Object = MibTableColumn
bertTestStreamUserPattern = _BertTestStreamUserPattern_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 19, 1, 8),
    _BertTestStreamUserPattern_Type()
)
bertTestStreamUserPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertTestStreamUserPattern.setStatus("current")
_BertTestStreamMonStartTime_Type = DateAndTime
_BertTestStreamMonStartTime_Object = MibTableColumn
bertTestStreamMonStartTime = _BertTestStreamMonStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 19, 1, 9),
    _BertTestStreamMonStartTime_Type()
)
bertTestStreamMonStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertTestStreamMonStartTime.setStatus("current")
_BertTestStreamMonEndTime_Type = DateAndTime
_BertTestStreamMonEndTime_Object = MibTableColumn
bertTestStreamMonEndTime = _BertTestStreamMonEndTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 19, 1, 10),
    _BertTestStreamMonEndTime_Type()
)
bertTestStreamMonEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertTestStreamMonEndTime.setStatus("current")
_BertTestStreamMonElapsedTime_Type = Integer32
_BertTestStreamMonElapsedTime_Object = MibTableColumn
bertTestStreamMonElapsedTime = _BertTestStreamMonElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 19, 1, 11),
    _BertTestStreamMonElapsedTime_Type()
)
bertTestStreamMonElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertTestStreamMonElapsedTime.setStatus("current")
_BertTestStreamMonSyncState_Type = BertSyncState
_BertTestStreamMonSyncState_Object = MibTableColumn
bertTestStreamMonSyncState = _BertTestStreamMonSyncState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 19, 1, 12),
    _BertTestStreamMonSyncState_Type()
)
bertTestStreamMonSyncState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertTestStreamMonSyncState.setStatus("current")
_BertTestStreamMonRxPattern_Type = BertPattern
_BertTestStreamMonRxPattern_Object = MibTableColumn
bertTestStreamMonRxPattern = _BertTestStreamMonRxPattern_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 19, 1, 13),
    _BertTestStreamMonRxPattern_Type()
)
bertTestStreamMonRxPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertTestStreamMonRxPattern.setStatus("current")
_BertTestStreamMonSyncCounts_Type = Unsigned32
_BertTestStreamMonSyncCounts_Object = MibTableColumn
bertTestStreamMonSyncCounts = _BertTestStreamMonSyncCounts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 19, 1, 14),
    _BertTestStreamMonSyncCounts_Type()
)
bertTestStreamMonSyncCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertTestStreamMonSyncCounts.setStatus("current")
_BertTestStreamMonRxBitErrsSinceStart_Type = PerfCounter64
_BertTestStreamMonRxBitErrsSinceStart_Object = MibTableColumn
bertTestStreamMonRxBitErrsSinceStart = _BertTestStreamMonRxBitErrsSinceStart_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 19, 1, 15),
    _BertTestStreamMonRxBitErrsSinceStart_Type()
)
bertTestStreamMonRxBitErrsSinceStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertTestStreamMonRxBitErrsSinceStart.setStatus("current")
_BertTestStreamMonRxBitsSinceStart_Type = PerfCounter64
_BertTestStreamMonRxBitsSinceStart_Object = MibTableColumn
bertTestStreamMonRxBitsSinceStart = _BertTestStreamMonRxBitsSinceStart_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 19, 1, 16),
    _BertTestStreamMonRxBitsSinceStart_Type()
)
bertTestStreamMonRxBitsSinceStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertTestStreamMonRxBitsSinceStart.setStatus("current")
_BertTestStreamMonRxESsSinceStart_Type = Unsigned32
_BertTestStreamMonRxESsSinceStart_Object = MibTableColumn
bertTestStreamMonRxESsSinceStart = _BertTestStreamMonRxESsSinceStart_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 19, 1, 17),
    _BertTestStreamMonRxESsSinceStart_Type()
)
bertTestStreamMonRxESsSinceStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertTestStreamMonRxESsSinceStart.setStatus("current")
_BertTestStreamMonRxErrRateSinceStart_Type = BitErrRate
_BertTestStreamMonRxErrRateSinceStart_Object = MibTableColumn
bertTestStreamMonRxErrRateSinceStart = _BertTestStreamMonRxErrRateSinceStart_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 19, 1, 18),
    _BertTestStreamMonRxErrRateSinceStart_Type()
)
bertTestStreamMonRxErrRateSinceStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertTestStreamMonRxErrRateSinceStart.setStatus("current")
_BertTestStreamMonRxErrRateMultiplierSinceStart_Type = Integer32
_BertTestStreamMonRxErrRateMultiplierSinceStart_Object = MibTableColumn
bertTestStreamMonRxErrRateMultiplierSinceStart = _BertTestStreamMonRxErrRateMultiplierSinceStart_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 19, 1, 19),
    _BertTestStreamMonRxErrRateMultiplierSinceStart_Type()
)
bertTestStreamMonRxErrRateMultiplierSinceStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertTestStreamMonRxErrRateMultiplierSinceStart.setStatus("current")
_BertTestStreamMonRxBitErrsSinceLastSync_Type = PerfCounter64
_BertTestStreamMonRxBitErrsSinceLastSync_Object = MibTableColumn
bertTestStreamMonRxBitErrsSinceLastSync = _BertTestStreamMonRxBitErrsSinceLastSync_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 19, 1, 20),
    _BertTestStreamMonRxBitErrsSinceLastSync_Type()
)
bertTestStreamMonRxBitErrsSinceLastSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertTestStreamMonRxBitErrsSinceLastSync.setStatus("current")
_BertTestStreamMonRxBitsSinceLastSync_Type = PerfCounter64
_BertTestStreamMonRxBitsSinceLastSync_Object = MibTableColumn
bertTestStreamMonRxBitsSinceLastSync = _BertTestStreamMonRxBitsSinceLastSync_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 19, 1, 21),
    _BertTestStreamMonRxBitsSinceLastSync_Type()
)
bertTestStreamMonRxBitsSinceLastSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertTestStreamMonRxBitsSinceLastSync.setStatus("current")
_BertTestStreamMonRxESsSinceLastSync_Type = Unsigned32
_BertTestStreamMonRxESsSinceLastSync_Object = MibTableColumn
bertTestStreamMonRxESsSinceLastSync = _BertTestStreamMonRxESsSinceLastSync_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 19, 1, 22),
    _BertTestStreamMonRxESsSinceLastSync_Type()
)
bertTestStreamMonRxESsSinceLastSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertTestStreamMonRxESsSinceLastSync.setStatus("current")
_BertTestStreamMonRxErrRateSinceLastSync_Type = BitErrRate
_BertTestStreamMonRxErrRateSinceLastSync_Object = MibTableColumn
bertTestStreamMonRxErrRateSinceLastSync = _BertTestStreamMonRxErrRateSinceLastSync_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 19, 1, 23),
    _BertTestStreamMonRxErrRateSinceLastSync_Type()
)
bertTestStreamMonRxErrRateSinceLastSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertTestStreamMonRxErrRateSinceLastSync.setStatus("current")
_BertTestStreamMonRxErrRateMultiplierSinceLastSync_Type = Unsigned32
_BertTestStreamMonRxErrRateMultiplierSinceLastSync_Object = MibTableColumn
bertTestStreamMonRxErrRateMultiplierSinceLastSync = _BertTestStreamMonRxErrRateMultiplierSinceLastSync_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 19, 1, 24),
    _BertTestStreamMonRxErrRateMultiplierSinceLastSync_Type()
)
bertTestStreamMonRxErrRateMultiplierSinceLastSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertTestStreamMonRxErrRateMultiplierSinceLastSync.setStatus("current")
_BertTestStreamConfigChangedFlag_Type = TruthValue
_BertTestStreamConfigChangedFlag_Object = MibTableColumn
bertTestStreamConfigChangedFlag = _BertTestStreamConfigChangedFlag_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 19, 1, 25),
    _BertTestStreamConfigChangedFlag_Type()
)
bertTestStreamConfigChangedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertTestStreamConfigChangedFlag.setStatus("current")
_BertTestStreamMonOOSSsSinceStart_Type = Unsigned32
_BertTestStreamMonOOSSsSinceStart_Object = MibTableColumn
bertTestStreamMonOOSSsSinceStart = _BertTestStreamMonOOSSsSinceStart_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 19, 1, 26),
    _BertTestStreamMonOOSSsSinceStart_Type()
)
bertTestStreamMonOOSSsSinceStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertTestStreamMonOOSSsSinceStart.setStatus("current")
_F3EsaProbeCOSConfigSoamPmExtTable_Object = MibTable
f3EsaProbeCOSConfigSoamPmExtTable = _F3EsaProbeCOSConfigSoamPmExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 20)
)
if mibBuilder.loadTexts:
    f3EsaProbeCOSConfigSoamPmExtTable.setStatus("current")
_F3EsaProbeCOSConfigSoamPmExtEntry_Object = MibTableRow
f3EsaProbeCOSConfigSoamPmExtEntry = _F3EsaProbeCOSConfigSoamPmExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 20, 1)
)
if mibBuilder.loadTexts:
    f3EsaProbeCOSConfigSoamPmExtEntry.setStatus("current")


class _F3EsaProbeCOSConfigSoamPmExtAvailFlrThreshold_Type(Unsigned32):
    """Custom type f3EsaProbeCOSConfigSoamPmExtAvailFlrThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_F3EsaProbeCOSConfigSoamPmExtAvailFlrThreshold_Type.__name__ = "Unsigned32"
_F3EsaProbeCOSConfigSoamPmExtAvailFlrThreshold_Object = MibTableColumn
f3EsaProbeCOSConfigSoamPmExtAvailFlrThreshold = _F3EsaProbeCOSConfigSoamPmExtAvailFlrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 20, 1, 1),
    _F3EsaProbeCOSConfigSoamPmExtAvailFlrThreshold_Type()
)
f3EsaProbeCOSConfigSoamPmExtAvailFlrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3EsaProbeCOSConfigSoamPmExtAvailFlrThreshold.setStatus("current")


class _F3EsaProbeCOSConfigSoamPmExtFlrDeltaTNumLmPdus_Type(Unsigned32):
    """Custom type f3EsaProbeCOSConfigSoamPmExtFlrDeltaTNumLmPdus based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_F3EsaProbeCOSConfigSoamPmExtFlrDeltaTNumLmPdus_Type.__name__ = "Unsigned32"
_F3EsaProbeCOSConfigSoamPmExtFlrDeltaTNumLmPdus_Object = MibTableColumn
f3EsaProbeCOSConfigSoamPmExtFlrDeltaTNumLmPdus = _F3EsaProbeCOSConfigSoamPmExtFlrDeltaTNumLmPdus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 20, 1, 2),
    _F3EsaProbeCOSConfigSoamPmExtFlrDeltaTNumLmPdus_Type()
)
f3EsaProbeCOSConfigSoamPmExtFlrDeltaTNumLmPdus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3EsaProbeCOSConfigSoamPmExtFlrDeltaTNumLmPdus.setStatus("current")


class _F3EsaProbeCOSConfigSoamPmExtConDeltaTsForAvail_Type(Unsigned32):
    """Custom type f3EsaProbeCOSConfigSoamPmExtConDeltaTsForAvail based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_F3EsaProbeCOSConfigSoamPmExtConDeltaTsForAvail_Type.__name__ = "Unsigned32"
_F3EsaProbeCOSConfigSoamPmExtConDeltaTsForAvail_Object = MibTableColumn
f3EsaProbeCOSConfigSoamPmExtConDeltaTsForAvail = _F3EsaProbeCOSConfigSoamPmExtConDeltaTsForAvail_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 20, 1, 3),
    _F3EsaProbeCOSConfigSoamPmExtConDeltaTsForAvail_Type()
)
f3EsaProbeCOSConfigSoamPmExtConDeltaTsForAvail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3EsaProbeCOSConfigSoamPmExtConDeltaTsForAvail.setStatus("current")
_F3EsaProbeStatsSoamPmExtTable_Object = MibTable
f3EsaProbeStatsSoamPmExtTable = _F3EsaProbeStatsSoamPmExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 21)
)
if mibBuilder.loadTexts:
    f3EsaProbeStatsSoamPmExtTable.setStatus("current")
_F3EsaProbeStatsSoamPmExtEntry_Object = MibTableRow
f3EsaProbeStatsSoamPmExtEntry = _F3EsaProbeStatsSoamPmExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 21, 1)
)
if mibBuilder.loadTexts:
    f3EsaProbeStatsSoamPmExtEntry.setStatus("current")
_F3EsaProbeStatsSoamPmExtMinP2RFlr_Type = PerfCounter64
_F3EsaProbeStatsSoamPmExtMinP2RFlr_Object = MibTableColumn
f3EsaProbeStatsSoamPmExtMinP2RFlr = _F3EsaProbeStatsSoamPmExtMinP2RFlr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 21, 1, 1),
    _F3EsaProbeStatsSoamPmExtMinP2RFlr_Type()
)
f3EsaProbeStatsSoamPmExtMinP2RFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeStatsSoamPmExtMinP2RFlr.setStatus("current")
_F3EsaProbeStatsSoamPmExtMaxP2RFlr_Type = PerfCounter64
_F3EsaProbeStatsSoamPmExtMaxP2RFlr_Object = MibTableColumn
f3EsaProbeStatsSoamPmExtMaxP2RFlr = _F3EsaProbeStatsSoamPmExtMaxP2RFlr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 21, 1, 2),
    _F3EsaProbeStatsSoamPmExtMaxP2RFlr_Type()
)
f3EsaProbeStatsSoamPmExtMaxP2RFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeStatsSoamPmExtMaxP2RFlr.setStatus("current")
_F3EsaProbeStatsSoamPmExtAvgP2RFlr_Type = PerfCounter64
_F3EsaProbeStatsSoamPmExtAvgP2RFlr_Object = MibTableColumn
f3EsaProbeStatsSoamPmExtAvgP2RFlr = _F3EsaProbeStatsSoamPmExtAvgP2RFlr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 21, 1, 3),
    _F3EsaProbeStatsSoamPmExtAvgP2RFlr_Type()
)
f3EsaProbeStatsSoamPmExtAvgP2RFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeStatsSoamPmExtAvgP2RFlr.setStatus("current")
_F3EsaProbeStatsSoamPmExtMinR2PFlr_Type = PerfCounter64
_F3EsaProbeStatsSoamPmExtMinR2PFlr_Object = MibTableColumn
f3EsaProbeStatsSoamPmExtMinR2PFlr = _F3EsaProbeStatsSoamPmExtMinR2PFlr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 21, 1, 4),
    _F3EsaProbeStatsSoamPmExtMinR2PFlr_Type()
)
f3EsaProbeStatsSoamPmExtMinR2PFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeStatsSoamPmExtMinR2PFlr.setStatus("current")
_F3EsaProbeStatsSoamPmExtMaxR2PFlr_Type = PerfCounter64
_F3EsaProbeStatsSoamPmExtMaxR2PFlr_Object = MibTableColumn
f3EsaProbeStatsSoamPmExtMaxR2PFlr = _F3EsaProbeStatsSoamPmExtMaxR2PFlr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 21, 1, 5),
    _F3EsaProbeStatsSoamPmExtMaxR2PFlr_Type()
)
f3EsaProbeStatsSoamPmExtMaxR2PFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeStatsSoamPmExtMaxR2PFlr.setStatus("current")
_F3EsaProbeStatsSoamPmExtAvgR2PFlr_Type = PerfCounter64
_F3EsaProbeStatsSoamPmExtAvgR2PFlr_Object = MibTableColumn
f3EsaProbeStatsSoamPmExtAvgR2PFlr = _F3EsaProbeStatsSoamPmExtAvgR2PFlr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 21, 1, 6),
    _F3EsaProbeStatsSoamPmExtAvgR2PFlr_Type()
)
f3EsaProbeStatsSoamPmExtAvgR2PFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeStatsSoamPmExtAvgR2PFlr.setStatus("current")
_F3EsaProbeStatsSoamPmExtP2rSeverelyErroredDeltaTs_Type = PerfCounter64
_F3EsaProbeStatsSoamPmExtP2rSeverelyErroredDeltaTs_Object = MibTableColumn
f3EsaProbeStatsSoamPmExtP2rSeverelyErroredDeltaTs = _F3EsaProbeStatsSoamPmExtP2rSeverelyErroredDeltaTs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 21, 1, 7),
    _F3EsaProbeStatsSoamPmExtP2rSeverelyErroredDeltaTs_Type()
)
f3EsaProbeStatsSoamPmExtP2rSeverelyErroredDeltaTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeStatsSoamPmExtP2rSeverelyErroredDeltaTs.setStatus("current")
_F3EsaProbeStatsSoamPmExtR2PSeverelyErroredDeltaTs_Type = PerfCounter64
_F3EsaProbeStatsSoamPmExtR2PSeverelyErroredDeltaTs_Object = MibTableColumn
f3EsaProbeStatsSoamPmExtR2PSeverelyErroredDeltaTs = _F3EsaProbeStatsSoamPmExtR2PSeverelyErroredDeltaTs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 21, 1, 8),
    _F3EsaProbeStatsSoamPmExtR2PSeverelyErroredDeltaTs_Type()
)
f3EsaProbeStatsSoamPmExtR2PSeverelyErroredDeltaTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeStatsSoamPmExtR2PSeverelyErroredDeltaTs.setStatus("current")
_F3EsaProbeStatsSoamPmExtP2rAvailableTime_Type = PerfCounter64
_F3EsaProbeStatsSoamPmExtP2rAvailableTime_Object = MibTableColumn
f3EsaProbeStatsSoamPmExtP2rAvailableTime = _F3EsaProbeStatsSoamPmExtP2rAvailableTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 21, 1, 9),
    _F3EsaProbeStatsSoamPmExtP2rAvailableTime_Type()
)
f3EsaProbeStatsSoamPmExtP2rAvailableTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeStatsSoamPmExtP2rAvailableTime.setStatus("current")
_F3EsaProbeStatsSoamPmExtR2PAvailableTime_Type = PerfCounter64
_F3EsaProbeStatsSoamPmExtR2PAvailableTime_Object = MibTableColumn
f3EsaProbeStatsSoamPmExtR2PAvailableTime = _F3EsaProbeStatsSoamPmExtR2PAvailableTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 21, 1, 10),
    _F3EsaProbeStatsSoamPmExtR2PAvailableTime_Type()
)
f3EsaProbeStatsSoamPmExtR2PAvailableTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeStatsSoamPmExtR2PAvailableTime.setStatus("current")
_F3EsaProbeStatsSoamPmExtP2rUnavailableTime_Type = PerfCounter64
_F3EsaProbeStatsSoamPmExtP2rUnavailableTime_Object = MibTableColumn
f3EsaProbeStatsSoamPmExtP2rUnavailableTime = _F3EsaProbeStatsSoamPmExtP2rUnavailableTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 21, 1, 11),
    _F3EsaProbeStatsSoamPmExtP2rUnavailableTime_Type()
)
f3EsaProbeStatsSoamPmExtP2rUnavailableTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeStatsSoamPmExtP2rUnavailableTime.setStatus("current")
_F3EsaProbeStatsSoamPmExtR2PUnavailableTime_Type = PerfCounter64
_F3EsaProbeStatsSoamPmExtR2PUnavailableTime_Object = MibTableColumn
f3EsaProbeStatsSoamPmExtR2PUnavailableTime = _F3EsaProbeStatsSoamPmExtR2PUnavailableTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 21, 1, 12),
    _F3EsaProbeStatsSoamPmExtR2PUnavailableTime_Type()
)
f3EsaProbeStatsSoamPmExtR2PUnavailableTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeStatsSoamPmExtR2PUnavailableTime.setStatus("current")
_F3EsaProbeStatsSoamPmExtMinAbsRTJitter_Type = PerfCounter64
_F3EsaProbeStatsSoamPmExtMinAbsRTJitter_Object = MibTableColumn
f3EsaProbeStatsSoamPmExtMinAbsRTJitter = _F3EsaProbeStatsSoamPmExtMinAbsRTJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 21, 1, 13),
    _F3EsaProbeStatsSoamPmExtMinAbsRTJitter_Type()
)
f3EsaProbeStatsSoamPmExtMinAbsRTJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeStatsSoamPmExtMinAbsRTJitter.setStatus("current")
_F3EsaProbeStatsSoamPmExtMaxAbsRTJitter_Type = PerfCounter64
_F3EsaProbeStatsSoamPmExtMaxAbsRTJitter_Object = MibTableColumn
f3EsaProbeStatsSoamPmExtMaxAbsRTJitter = _F3EsaProbeStatsSoamPmExtMaxAbsRTJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 21, 1, 14),
    _F3EsaProbeStatsSoamPmExtMaxAbsRTJitter_Type()
)
f3EsaProbeStatsSoamPmExtMaxAbsRTJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeStatsSoamPmExtMaxAbsRTJitter.setStatus("current")
_F3EsaProbeStatsSoamPmExtAvgAbsRTJitter_Type = PerfCounter64
_F3EsaProbeStatsSoamPmExtAvgAbsRTJitter_Object = MibTableColumn
f3EsaProbeStatsSoamPmExtAvgAbsRTJitter = _F3EsaProbeStatsSoamPmExtAvgAbsRTJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 21, 1, 15),
    _F3EsaProbeStatsSoamPmExtAvgAbsRTJitter_Type()
)
f3EsaProbeStatsSoamPmExtAvgAbsRTJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeStatsSoamPmExtAvgAbsRTJitter.setStatus("current")
_F3EsaProbeStatsSoamPmExtNumAbsRTJitter_Type = PerfCounter64
_F3EsaProbeStatsSoamPmExtNumAbsRTJitter_Object = MibTableColumn
f3EsaProbeStatsSoamPmExtNumAbsRTJitter = _F3EsaProbeStatsSoamPmExtNumAbsRTJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 21, 1, 16),
    _F3EsaProbeStatsSoamPmExtNumAbsRTJitter_Type()
)
f3EsaProbeStatsSoamPmExtNumAbsRTJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeStatsSoamPmExtNumAbsRTJitter.setStatus("current")
_F3EsaProbeStatsSoamPmExtSumAbsRTJitter_Type = PerfCounter64
_F3EsaProbeStatsSoamPmExtSumAbsRTJitter_Object = MibTableColumn
f3EsaProbeStatsSoamPmExtSumAbsRTJitter = _F3EsaProbeStatsSoamPmExtSumAbsRTJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 21, 1, 17),
    _F3EsaProbeStatsSoamPmExtSumAbsRTJitter_Type()
)
f3EsaProbeStatsSoamPmExtSumAbsRTJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeStatsSoamPmExtSumAbsRTJitter.setStatus("current")
_F3EsaProbeStatsSoamPmExtSumOfSqAbsRTJitter_Type = PerfCounter64
_F3EsaProbeStatsSoamPmExtSumOfSqAbsRTJitter_Object = MibTableColumn
f3EsaProbeStatsSoamPmExtSumOfSqAbsRTJitter = _F3EsaProbeStatsSoamPmExtSumOfSqAbsRTJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 21, 1, 18),
    _F3EsaProbeStatsSoamPmExtSumOfSqAbsRTJitter_Type()
)
f3EsaProbeStatsSoamPmExtSumOfSqAbsRTJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeStatsSoamPmExtSumOfSqAbsRTJitter.setStatus("current")
_F3EsaProbeStatsSoamPmExtMaxP2RFDR_Type = PerfCounter64
_F3EsaProbeStatsSoamPmExtMaxP2RFDR_Object = MibTableColumn
f3EsaProbeStatsSoamPmExtMaxP2RFDR = _F3EsaProbeStatsSoamPmExtMaxP2RFDR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 21, 1, 19),
    _F3EsaProbeStatsSoamPmExtMaxP2RFDR_Type()
)
f3EsaProbeStatsSoamPmExtMaxP2RFDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeStatsSoamPmExtMaxP2RFDR.setStatus("current")
_F3EsaProbeStatsSoamPmExtAvgP2RFDR_Type = PerfCounter64
_F3EsaProbeStatsSoamPmExtAvgP2RFDR_Object = MibTableColumn
f3EsaProbeStatsSoamPmExtAvgP2RFDR = _F3EsaProbeStatsSoamPmExtAvgP2RFDR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 21, 1, 20),
    _F3EsaProbeStatsSoamPmExtAvgP2RFDR_Type()
)
f3EsaProbeStatsSoamPmExtAvgP2RFDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeStatsSoamPmExtAvgP2RFDR.setStatus("current")
_F3EsaProbeStatsSoamPmExtNumP2RFDR_Type = PerfCounter64
_F3EsaProbeStatsSoamPmExtNumP2RFDR_Object = MibTableColumn
f3EsaProbeStatsSoamPmExtNumP2RFDR = _F3EsaProbeStatsSoamPmExtNumP2RFDR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 21, 1, 21),
    _F3EsaProbeStatsSoamPmExtNumP2RFDR_Type()
)
f3EsaProbeStatsSoamPmExtNumP2RFDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeStatsSoamPmExtNumP2RFDR.setStatus("current")
_F3EsaProbeStatsSoamPmExtSumP2RFDR_Type = PerfCounter64
_F3EsaProbeStatsSoamPmExtSumP2RFDR_Object = MibTableColumn
f3EsaProbeStatsSoamPmExtSumP2RFDR = _F3EsaProbeStatsSoamPmExtSumP2RFDR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 21, 1, 22),
    _F3EsaProbeStatsSoamPmExtSumP2RFDR_Type()
)
f3EsaProbeStatsSoamPmExtSumP2RFDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeStatsSoamPmExtSumP2RFDR.setStatus("current")
_F3EsaProbeStatsSoamPmExtSumOfSqP2RFDR_Type = PerfCounter64
_F3EsaProbeStatsSoamPmExtSumOfSqP2RFDR_Object = MibTableColumn
f3EsaProbeStatsSoamPmExtSumOfSqP2RFDR = _F3EsaProbeStatsSoamPmExtSumOfSqP2RFDR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 21, 1, 23),
    _F3EsaProbeStatsSoamPmExtSumOfSqP2RFDR_Type()
)
f3EsaProbeStatsSoamPmExtSumOfSqP2RFDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeStatsSoamPmExtSumOfSqP2RFDR.setStatus("current")
_F3EsaProbeStatsSoamPmExtMaxR2PFDR_Type = PerfCounter64
_F3EsaProbeStatsSoamPmExtMaxR2PFDR_Object = MibTableColumn
f3EsaProbeStatsSoamPmExtMaxR2PFDR = _F3EsaProbeStatsSoamPmExtMaxR2PFDR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 21, 1, 24),
    _F3EsaProbeStatsSoamPmExtMaxR2PFDR_Type()
)
f3EsaProbeStatsSoamPmExtMaxR2PFDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeStatsSoamPmExtMaxR2PFDR.setStatus("current")
_F3EsaProbeStatsSoamPmExtAvgR2PFDR_Type = PerfCounter64
_F3EsaProbeStatsSoamPmExtAvgR2PFDR_Object = MibTableColumn
f3EsaProbeStatsSoamPmExtAvgR2PFDR = _F3EsaProbeStatsSoamPmExtAvgR2PFDR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 21, 1, 25),
    _F3EsaProbeStatsSoamPmExtAvgR2PFDR_Type()
)
f3EsaProbeStatsSoamPmExtAvgR2PFDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeStatsSoamPmExtAvgR2PFDR.setStatus("current")
_F3EsaProbeStatsSoamPmExtNumR2PFDR_Type = PerfCounter64
_F3EsaProbeStatsSoamPmExtNumR2PFDR_Object = MibTableColumn
f3EsaProbeStatsSoamPmExtNumR2PFDR = _F3EsaProbeStatsSoamPmExtNumR2PFDR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 21, 1, 26),
    _F3EsaProbeStatsSoamPmExtNumR2PFDR_Type()
)
f3EsaProbeStatsSoamPmExtNumR2PFDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeStatsSoamPmExtNumR2PFDR.setStatus("current")
_F3EsaProbeStatsSoamPmExtSumR2PFDR_Type = PerfCounter64
_F3EsaProbeStatsSoamPmExtSumR2PFDR_Object = MibTableColumn
f3EsaProbeStatsSoamPmExtSumR2PFDR = _F3EsaProbeStatsSoamPmExtSumR2PFDR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 21, 1, 27),
    _F3EsaProbeStatsSoamPmExtSumR2PFDR_Type()
)
f3EsaProbeStatsSoamPmExtSumR2PFDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeStatsSoamPmExtSumR2PFDR.setStatus("current")
_F3EsaProbeStatsSoamPmExtSumOfSqR2PFDR_Type = PerfCounter64
_F3EsaProbeStatsSoamPmExtSumOfSqR2PFDR_Object = MibTableColumn
f3EsaProbeStatsSoamPmExtSumOfSqR2PFDR = _F3EsaProbeStatsSoamPmExtSumOfSqR2PFDR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 21, 1, 28),
    _F3EsaProbeStatsSoamPmExtSumOfSqR2PFDR_Type()
)
f3EsaProbeStatsSoamPmExtSumOfSqR2PFDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeStatsSoamPmExtSumOfSqR2PFDR.setStatus("current")
_F3EsaProbeStatsSoamPmExtMaxRTFDR_Type = PerfCounter64
_F3EsaProbeStatsSoamPmExtMaxRTFDR_Object = MibTableColumn
f3EsaProbeStatsSoamPmExtMaxRTFDR = _F3EsaProbeStatsSoamPmExtMaxRTFDR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 21, 1, 29),
    _F3EsaProbeStatsSoamPmExtMaxRTFDR_Type()
)
f3EsaProbeStatsSoamPmExtMaxRTFDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeStatsSoamPmExtMaxRTFDR.setStatus("current")
_F3EsaProbeStatsSoamPmExtAvgRTFDR_Type = PerfCounter64
_F3EsaProbeStatsSoamPmExtAvgRTFDR_Object = MibTableColumn
f3EsaProbeStatsSoamPmExtAvgRTFDR = _F3EsaProbeStatsSoamPmExtAvgRTFDR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 21, 1, 30),
    _F3EsaProbeStatsSoamPmExtAvgRTFDR_Type()
)
f3EsaProbeStatsSoamPmExtAvgRTFDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeStatsSoamPmExtAvgRTFDR.setStatus("current")
_F3EsaProbeStatsSoamPmExtNumRTFDR_Type = PerfCounter64
_F3EsaProbeStatsSoamPmExtNumRTFDR_Object = MibTableColumn
f3EsaProbeStatsSoamPmExtNumRTFDR = _F3EsaProbeStatsSoamPmExtNumRTFDR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 21, 1, 31),
    _F3EsaProbeStatsSoamPmExtNumRTFDR_Type()
)
f3EsaProbeStatsSoamPmExtNumRTFDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeStatsSoamPmExtNumRTFDR.setStatus("current")
_F3EsaProbeStatsSoamPmExtSumRTFDR_Type = PerfCounter64
_F3EsaProbeStatsSoamPmExtSumRTFDR_Object = MibTableColumn
f3EsaProbeStatsSoamPmExtSumRTFDR = _F3EsaProbeStatsSoamPmExtSumRTFDR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 21, 1, 32),
    _F3EsaProbeStatsSoamPmExtSumRTFDR_Type()
)
f3EsaProbeStatsSoamPmExtSumRTFDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeStatsSoamPmExtSumRTFDR.setStatus("current")
_F3EsaProbeStatsSoamPmExtSumOfSqRTFDR_Type = PerfCounter64
_F3EsaProbeStatsSoamPmExtSumOfSqRTFDR_Object = MibTableColumn
f3EsaProbeStatsSoamPmExtSumOfSqRTFDR = _F3EsaProbeStatsSoamPmExtSumOfSqRTFDR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 21, 1, 33),
    _F3EsaProbeStatsSoamPmExtSumOfSqRTFDR_Type()
)
f3EsaProbeStatsSoamPmExtSumOfSqRTFDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeStatsSoamPmExtSumOfSqRTFDR.setStatus("current")
_F3EsaProbeStatsSoamPmExtP2rAvailableDeltaTs_Type = PerfCounter64
_F3EsaProbeStatsSoamPmExtP2rAvailableDeltaTs_Object = MibTableColumn
f3EsaProbeStatsSoamPmExtP2rAvailableDeltaTs = _F3EsaProbeStatsSoamPmExtP2rAvailableDeltaTs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 21, 1, 34),
    _F3EsaProbeStatsSoamPmExtP2rAvailableDeltaTs_Type()
)
f3EsaProbeStatsSoamPmExtP2rAvailableDeltaTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeStatsSoamPmExtP2rAvailableDeltaTs.setStatus("current")
_F3EsaProbeStatsSoamPmExtR2pAvailableDeltaTs_Type = PerfCounter64
_F3EsaProbeStatsSoamPmExtR2pAvailableDeltaTs_Object = MibTableColumn
f3EsaProbeStatsSoamPmExtR2pAvailableDeltaTs = _F3EsaProbeStatsSoamPmExtR2pAvailableDeltaTs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 21, 1, 35),
    _F3EsaProbeStatsSoamPmExtR2pAvailableDeltaTs_Type()
)
f3EsaProbeStatsSoamPmExtR2pAvailableDeltaTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeStatsSoamPmExtR2pAvailableDeltaTs.setStatus("current")
_F3EsaProbeStatsSoamPmExtP2rUnavailableDeltaTs_Type = PerfCounter64
_F3EsaProbeStatsSoamPmExtP2rUnavailableDeltaTs_Object = MibTableColumn
f3EsaProbeStatsSoamPmExtP2rUnavailableDeltaTs = _F3EsaProbeStatsSoamPmExtP2rUnavailableDeltaTs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 21, 1, 36),
    _F3EsaProbeStatsSoamPmExtP2rUnavailableDeltaTs_Type()
)
f3EsaProbeStatsSoamPmExtP2rUnavailableDeltaTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeStatsSoamPmExtP2rUnavailableDeltaTs.setStatus("current")
_F3EsaProbeStatsSoamPmExtR2pUnavailableDeltaTs_Type = PerfCounter64
_F3EsaProbeStatsSoamPmExtR2pUnavailableDeltaTs_Object = MibTableColumn
f3EsaProbeStatsSoamPmExtR2pUnavailableDeltaTs = _F3EsaProbeStatsSoamPmExtR2pUnavailableDeltaTs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 21, 1, 37),
    _F3EsaProbeStatsSoamPmExtR2pUnavailableDeltaTs_Type()
)
f3EsaProbeStatsSoamPmExtR2pUnavailableDeltaTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeStatsSoamPmExtR2pUnavailableDeltaTs.setStatus("current")
_F3EsaProbeStatsSoamPmExtElapsedTime_Type = PerfCounter64
_F3EsaProbeStatsSoamPmExtElapsedTime_Object = MibTableColumn
f3EsaProbeStatsSoamPmExtElapsedTime = _F3EsaProbeStatsSoamPmExtElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 21, 1, 38),
    _F3EsaProbeStatsSoamPmExtElapsedTime_Type()
)
f3EsaProbeStatsSoamPmExtElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeStatsSoamPmExtElapsedTime.setStatus("current")
_F3EsaProbeHistorySoamPmExtTable_Object = MibTable
f3EsaProbeHistorySoamPmExtTable = _F3EsaProbeHistorySoamPmExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 22)
)
if mibBuilder.loadTexts:
    f3EsaProbeHistorySoamPmExtTable.setStatus("current")
_F3EsaProbeHistorySoamPmExtEntry_Object = MibTableRow
f3EsaProbeHistorySoamPmExtEntry = _F3EsaProbeHistorySoamPmExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 22, 1)
)
if mibBuilder.loadTexts:
    f3EsaProbeHistorySoamPmExtEntry.setStatus("current")
_F3EsaProbeHistorySoamPmExtMinP2RFlr_Type = PerfCounter64
_F3EsaProbeHistorySoamPmExtMinP2RFlr_Object = MibTableColumn
f3EsaProbeHistorySoamPmExtMinP2RFlr = _F3EsaProbeHistorySoamPmExtMinP2RFlr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 22, 1, 1),
    _F3EsaProbeHistorySoamPmExtMinP2RFlr_Type()
)
f3EsaProbeHistorySoamPmExtMinP2RFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeHistorySoamPmExtMinP2RFlr.setStatus("current")
_F3EsaProbeHistorySoamPmExtMaxP2RFlr_Type = PerfCounter64
_F3EsaProbeHistorySoamPmExtMaxP2RFlr_Object = MibTableColumn
f3EsaProbeHistorySoamPmExtMaxP2RFlr = _F3EsaProbeHistorySoamPmExtMaxP2RFlr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 22, 1, 2),
    _F3EsaProbeHistorySoamPmExtMaxP2RFlr_Type()
)
f3EsaProbeHistorySoamPmExtMaxP2RFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeHistorySoamPmExtMaxP2RFlr.setStatus("current")
_F3EsaProbeHistorySoamPmExtAvgP2RFlr_Type = PerfCounter64
_F3EsaProbeHistorySoamPmExtAvgP2RFlr_Object = MibTableColumn
f3EsaProbeHistorySoamPmExtAvgP2RFlr = _F3EsaProbeHistorySoamPmExtAvgP2RFlr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 22, 1, 3),
    _F3EsaProbeHistorySoamPmExtAvgP2RFlr_Type()
)
f3EsaProbeHistorySoamPmExtAvgP2RFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeHistorySoamPmExtAvgP2RFlr.setStatus("current")
_F3EsaProbeHistorySoamPmExtMinR2PFlr_Type = PerfCounter64
_F3EsaProbeHistorySoamPmExtMinR2PFlr_Object = MibTableColumn
f3EsaProbeHistorySoamPmExtMinR2PFlr = _F3EsaProbeHistorySoamPmExtMinR2PFlr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 22, 1, 4),
    _F3EsaProbeHistorySoamPmExtMinR2PFlr_Type()
)
f3EsaProbeHistorySoamPmExtMinR2PFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeHistorySoamPmExtMinR2PFlr.setStatus("current")
_F3EsaProbeHistorySoamPmExtMaxR2PFlr_Type = PerfCounter64
_F3EsaProbeHistorySoamPmExtMaxR2PFlr_Object = MibTableColumn
f3EsaProbeHistorySoamPmExtMaxR2PFlr = _F3EsaProbeHistorySoamPmExtMaxR2PFlr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 22, 1, 5),
    _F3EsaProbeHistorySoamPmExtMaxR2PFlr_Type()
)
f3EsaProbeHistorySoamPmExtMaxR2PFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeHistorySoamPmExtMaxR2PFlr.setStatus("current")
_F3EsaProbeHistorySoamPmExtAvgR2PFlr_Type = PerfCounter64
_F3EsaProbeHistorySoamPmExtAvgR2PFlr_Object = MibTableColumn
f3EsaProbeHistorySoamPmExtAvgR2PFlr = _F3EsaProbeHistorySoamPmExtAvgR2PFlr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 22, 1, 6),
    _F3EsaProbeHistorySoamPmExtAvgR2PFlr_Type()
)
f3EsaProbeHistorySoamPmExtAvgR2PFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeHistorySoamPmExtAvgR2PFlr.setStatus("current")
_F3EsaProbeHistorySoamPmExtP2rSeverelyErroredDeltaTs_Type = PerfCounter64
_F3EsaProbeHistorySoamPmExtP2rSeverelyErroredDeltaTs_Object = MibTableColumn
f3EsaProbeHistorySoamPmExtP2rSeverelyErroredDeltaTs = _F3EsaProbeHistorySoamPmExtP2rSeverelyErroredDeltaTs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 22, 1, 7),
    _F3EsaProbeHistorySoamPmExtP2rSeverelyErroredDeltaTs_Type()
)
f3EsaProbeHistorySoamPmExtP2rSeverelyErroredDeltaTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeHistorySoamPmExtP2rSeverelyErroredDeltaTs.setStatus("current")
_F3EsaProbeHistorySoamPmExtR2PSeverelyErroredDeltaTs_Type = PerfCounter64
_F3EsaProbeHistorySoamPmExtR2PSeverelyErroredDeltaTs_Object = MibTableColumn
f3EsaProbeHistorySoamPmExtR2PSeverelyErroredDeltaTs = _F3EsaProbeHistorySoamPmExtR2PSeverelyErroredDeltaTs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 22, 1, 8),
    _F3EsaProbeHistorySoamPmExtR2PSeverelyErroredDeltaTs_Type()
)
f3EsaProbeHistorySoamPmExtR2PSeverelyErroredDeltaTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeHistorySoamPmExtR2PSeverelyErroredDeltaTs.setStatus("current")
_F3EsaProbeHistorySoamPmExtP2rAvailableTime_Type = PerfCounter64
_F3EsaProbeHistorySoamPmExtP2rAvailableTime_Object = MibTableColumn
f3EsaProbeHistorySoamPmExtP2rAvailableTime = _F3EsaProbeHistorySoamPmExtP2rAvailableTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 22, 1, 9),
    _F3EsaProbeHistorySoamPmExtP2rAvailableTime_Type()
)
f3EsaProbeHistorySoamPmExtP2rAvailableTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeHistorySoamPmExtP2rAvailableTime.setStatus("current")
_F3EsaProbeHistorySoamPmExtR2PAvailableTime_Type = PerfCounter64
_F3EsaProbeHistorySoamPmExtR2PAvailableTime_Object = MibTableColumn
f3EsaProbeHistorySoamPmExtR2PAvailableTime = _F3EsaProbeHistorySoamPmExtR2PAvailableTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 22, 1, 10),
    _F3EsaProbeHistorySoamPmExtR2PAvailableTime_Type()
)
f3EsaProbeHistorySoamPmExtR2PAvailableTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeHistorySoamPmExtR2PAvailableTime.setStatus("current")
_F3EsaProbeHistorySoamPmExtP2rUnavailableTime_Type = PerfCounter64
_F3EsaProbeHistorySoamPmExtP2rUnavailableTime_Object = MibTableColumn
f3EsaProbeHistorySoamPmExtP2rUnavailableTime = _F3EsaProbeHistorySoamPmExtP2rUnavailableTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 22, 1, 11),
    _F3EsaProbeHistorySoamPmExtP2rUnavailableTime_Type()
)
f3EsaProbeHistorySoamPmExtP2rUnavailableTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeHistorySoamPmExtP2rUnavailableTime.setStatus("current")
_F3EsaProbeHistorySoamPmExtR2PUnavailableTime_Type = PerfCounter64
_F3EsaProbeHistorySoamPmExtR2PUnavailableTime_Object = MibTableColumn
f3EsaProbeHistorySoamPmExtR2PUnavailableTime = _F3EsaProbeHistorySoamPmExtR2PUnavailableTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 22, 1, 12),
    _F3EsaProbeHistorySoamPmExtR2PUnavailableTime_Type()
)
f3EsaProbeHistorySoamPmExtR2PUnavailableTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeHistorySoamPmExtR2PUnavailableTime.setStatus("current")
_F3EsaProbeHistorySoamPmExtMinAbsRTJitter_Type = PerfCounter64
_F3EsaProbeHistorySoamPmExtMinAbsRTJitter_Object = MibTableColumn
f3EsaProbeHistorySoamPmExtMinAbsRTJitter = _F3EsaProbeHistorySoamPmExtMinAbsRTJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 22, 1, 13),
    _F3EsaProbeHistorySoamPmExtMinAbsRTJitter_Type()
)
f3EsaProbeHistorySoamPmExtMinAbsRTJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeHistorySoamPmExtMinAbsRTJitter.setStatus("current")
_F3EsaProbeHistorySoamPmExtMaxAbsRTJitter_Type = PerfCounter64
_F3EsaProbeHistorySoamPmExtMaxAbsRTJitter_Object = MibTableColumn
f3EsaProbeHistorySoamPmExtMaxAbsRTJitter = _F3EsaProbeHistorySoamPmExtMaxAbsRTJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 22, 1, 14),
    _F3EsaProbeHistorySoamPmExtMaxAbsRTJitter_Type()
)
f3EsaProbeHistorySoamPmExtMaxAbsRTJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeHistorySoamPmExtMaxAbsRTJitter.setStatus("current")
_F3EsaProbeHistorySoamPmExtAvgAbsRTJitter_Type = PerfCounter64
_F3EsaProbeHistorySoamPmExtAvgAbsRTJitter_Object = MibTableColumn
f3EsaProbeHistorySoamPmExtAvgAbsRTJitter = _F3EsaProbeHistorySoamPmExtAvgAbsRTJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 22, 1, 15),
    _F3EsaProbeHistorySoamPmExtAvgAbsRTJitter_Type()
)
f3EsaProbeHistorySoamPmExtAvgAbsRTJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeHistorySoamPmExtAvgAbsRTJitter.setStatus("current")
_F3EsaProbeHistorySoamPmExtNumAbsRTJitter_Type = PerfCounter64
_F3EsaProbeHistorySoamPmExtNumAbsRTJitter_Object = MibTableColumn
f3EsaProbeHistorySoamPmExtNumAbsRTJitter = _F3EsaProbeHistorySoamPmExtNumAbsRTJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 22, 1, 16),
    _F3EsaProbeHistorySoamPmExtNumAbsRTJitter_Type()
)
f3EsaProbeHistorySoamPmExtNumAbsRTJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeHistorySoamPmExtNumAbsRTJitter.setStatus("current")
_F3EsaProbeHistorySoamPmExtSumAbsRTJitter_Type = PerfCounter64
_F3EsaProbeHistorySoamPmExtSumAbsRTJitter_Object = MibTableColumn
f3EsaProbeHistorySoamPmExtSumAbsRTJitter = _F3EsaProbeHistorySoamPmExtSumAbsRTJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 22, 1, 17),
    _F3EsaProbeHistorySoamPmExtSumAbsRTJitter_Type()
)
f3EsaProbeHistorySoamPmExtSumAbsRTJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeHistorySoamPmExtSumAbsRTJitter.setStatus("current")
_F3EsaProbeHistorySoamPmExtSumOfSqAbsRTJitter_Type = PerfCounter64
_F3EsaProbeHistorySoamPmExtSumOfSqAbsRTJitter_Object = MibTableColumn
f3EsaProbeHistorySoamPmExtSumOfSqAbsRTJitter = _F3EsaProbeHistorySoamPmExtSumOfSqAbsRTJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 22, 1, 18),
    _F3EsaProbeHistorySoamPmExtSumOfSqAbsRTJitter_Type()
)
f3EsaProbeHistorySoamPmExtSumOfSqAbsRTJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeHistorySoamPmExtSumOfSqAbsRTJitter.setStatus("current")
_F3EsaProbeHistorySoamPmExtMaxP2RFDR_Type = PerfCounter64
_F3EsaProbeHistorySoamPmExtMaxP2RFDR_Object = MibTableColumn
f3EsaProbeHistorySoamPmExtMaxP2RFDR = _F3EsaProbeHistorySoamPmExtMaxP2RFDR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 22, 1, 19),
    _F3EsaProbeHistorySoamPmExtMaxP2RFDR_Type()
)
f3EsaProbeHistorySoamPmExtMaxP2RFDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeHistorySoamPmExtMaxP2RFDR.setStatus("current")
_F3EsaProbeHistorySoamPmExtAvgP2RFDR_Type = PerfCounter64
_F3EsaProbeHistorySoamPmExtAvgP2RFDR_Object = MibTableColumn
f3EsaProbeHistorySoamPmExtAvgP2RFDR = _F3EsaProbeHistorySoamPmExtAvgP2RFDR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 22, 1, 20),
    _F3EsaProbeHistorySoamPmExtAvgP2RFDR_Type()
)
f3EsaProbeHistorySoamPmExtAvgP2RFDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeHistorySoamPmExtAvgP2RFDR.setStatus("current")
_F3EsaProbeHistorySoamPmExtNumP2RFDR_Type = PerfCounter64
_F3EsaProbeHistorySoamPmExtNumP2RFDR_Object = MibTableColumn
f3EsaProbeHistorySoamPmExtNumP2RFDR = _F3EsaProbeHistorySoamPmExtNumP2RFDR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 22, 1, 21),
    _F3EsaProbeHistorySoamPmExtNumP2RFDR_Type()
)
f3EsaProbeHistorySoamPmExtNumP2RFDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeHistorySoamPmExtNumP2RFDR.setStatus("current")
_F3EsaProbeHistorySoamPmExtSumP2RFDR_Type = PerfCounter64
_F3EsaProbeHistorySoamPmExtSumP2RFDR_Object = MibTableColumn
f3EsaProbeHistorySoamPmExtSumP2RFDR = _F3EsaProbeHistorySoamPmExtSumP2RFDR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 22, 1, 22),
    _F3EsaProbeHistorySoamPmExtSumP2RFDR_Type()
)
f3EsaProbeHistorySoamPmExtSumP2RFDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeHistorySoamPmExtSumP2RFDR.setStatus("current")
_F3EsaProbeHistorySoamPmExtSumOfSqP2RFDR_Type = PerfCounter64
_F3EsaProbeHistorySoamPmExtSumOfSqP2RFDR_Object = MibTableColumn
f3EsaProbeHistorySoamPmExtSumOfSqP2RFDR = _F3EsaProbeHistorySoamPmExtSumOfSqP2RFDR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 22, 1, 23),
    _F3EsaProbeHistorySoamPmExtSumOfSqP2RFDR_Type()
)
f3EsaProbeHistorySoamPmExtSumOfSqP2RFDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeHistorySoamPmExtSumOfSqP2RFDR.setStatus("current")
_F3EsaProbeHistorySoamPmExtMaxR2PFDR_Type = PerfCounter64
_F3EsaProbeHistorySoamPmExtMaxR2PFDR_Object = MibTableColumn
f3EsaProbeHistorySoamPmExtMaxR2PFDR = _F3EsaProbeHistorySoamPmExtMaxR2PFDR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 22, 1, 24),
    _F3EsaProbeHistorySoamPmExtMaxR2PFDR_Type()
)
f3EsaProbeHistorySoamPmExtMaxR2PFDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeHistorySoamPmExtMaxR2PFDR.setStatus("current")
_F3EsaProbeHistorySoamPmExtAvgR2PFDR_Type = PerfCounter64
_F3EsaProbeHistorySoamPmExtAvgR2PFDR_Object = MibTableColumn
f3EsaProbeHistorySoamPmExtAvgR2PFDR = _F3EsaProbeHistorySoamPmExtAvgR2PFDR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 22, 1, 25),
    _F3EsaProbeHistorySoamPmExtAvgR2PFDR_Type()
)
f3EsaProbeHistorySoamPmExtAvgR2PFDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeHistorySoamPmExtAvgR2PFDR.setStatus("current")
_F3EsaProbeHistorySoamPmExtNumR2PFDR_Type = PerfCounter64
_F3EsaProbeHistorySoamPmExtNumR2PFDR_Object = MibTableColumn
f3EsaProbeHistorySoamPmExtNumR2PFDR = _F3EsaProbeHistorySoamPmExtNumR2PFDR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 22, 1, 26),
    _F3EsaProbeHistorySoamPmExtNumR2PFDR_Type()
)
f3EsaProbeHistorySoamPmExtNumR2PFDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeHistorySoamPmExtNumR2PFDR.setStatus("current")
_F3EsaProbeHistorySoamPmExtSumR2PFDR_Type = PerfCounter64
_F3EsaProbeHistorySoamPmExtSumR2PFDR_Object = MibTableColumn
f3EsaProbeHistorySoamPmExtSumR2PFDR = _F3EsaProbeHistorySoamPmExtSumR2PFDR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 22, 1, 27),
    _F3EsaProbeHistorySoamPmExtSumR2PFDR_Type()
)
f3EsaProbeHistorySoamPmExtSumR2PFDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeHistorySoamPmExtSumR2PFDR.setStatus("current")
_F3EsaProbeHistorySoamPmExtSumOfSqR2PFDR_Type = PerfCounter64
_F3EsaProbeHistorySoamPmExtSumOfSqR2PFDR_Object = MibTableColumn
f3EsaProbeHistorySoamPmExtSumOfSqR2PFDR = _F3EsaProbeHistorySoamPmExtSumOfSqR2PFDR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 22, 1, 28),
    _F3EsaProbeHistorySoamPmExtSumOfSqR2PFDR_Type()
)
f3EsaProbeHistorySoamPmExtSumOfSqR2PFDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeHistorySoamPmExtSumOfSqR2PFDR.setStatus("current")
_F3EsaProbeHistorySoamPmExtMaxRTFDR_Type = PerfCounter64
_F3EsaProbeHistorySoamPmExtMaxRTFDR_Object = MibTableColumn
f3EsaProbeHistorySoamPmExtMaxRTFDR = _F3EsaProbeHistorySoamPmExtMaxRTFDR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 22, 1, 29),
    _F3EsaProbeHistorySoamPmExtMaxRTFDR_Type()
)
f3EsaProbeHistorySoamPmExtMaxRTFDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeHistorySoamPmExtMaxRTFDR.setStatus("current")
_F3EsaProbeHistorySoamPmExtAvgRTFDR_Type = PerfCounter64
_F3EsaProbeHistorySoamPmExtAvgRTFDR_Object = MibTableColumn
f3EsaProbeHistorySoamPmExtAvgRTFDR = _F3EsaProbeHistorySoamPmExtAvgRTFDR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 22, 1, 30),
    _F3EsaProbeHistorySoamPmExtAvgRTFDR_Type()
)
f3EsaProbeHistorySoamPmExtAvgRTFDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeHistorySoamPmExtAvgRTFDR.setStatus("current")
_F3EsaProbeHistorySoamPmExtNumRTFDR_Type = PerfCounter64
_F3EsaProbeHistorySoamPmExtNumRTFDR_Object = MibTableColumn
f3EsaProbeHistorySoamPmExtNumRTFDR = _F3EsaProbeHistorySoamPmExtNumRTFDR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 22, 1, 31),
    _F3EsaProbeHistorySoamPmExtNumRTFDR_Type()
)
f3EsaProbeHistorySoamPmExtNumRTFDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeHistorySoamPmExtNumRTFDR.setStatus("current")
_F3EsaProbeHistorySoamPmExtSumRTFDR_Type = PerfCounter64
_F3EsaProbeHistorySoamPmExtSumRTFDR_Object = MibTableColumn
f3EsaProbeHistorySoamPmExtSumRTFDR = _F3EsaProbeHistorySoamPmExtSumRTFDR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 22, 1, 32),
    _F3EsaProbeHistorySoamPmExtSumRTFDR_Type()
)
f3EsaProbeHistorySoamPmExtSumRTFDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeHistorySoamPmExtSumRTFDR.setStatus("current")
_F3EsaProbeHistorySoamPmExtSumOfSqRTFDR_Type = PerfCounter64
_F3EsaProbeHistorySoamPmExtSumOfSqRTFDR_Object = MibTableColumn
f3EsaProbeHistorySoamPmExtSumOfSqRTFDR = _F3EsaProbeHistorySoamPmExtSumOfSqRTFDR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 22, 1, 33),
    _F3EsaProbeHistorySoamPmExtSumOfSqRTFDR_Type()
)
f3EsaProbeHistorySoamPmExtSumOfSqRTFDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeHistorySoamPmExtSumOfSqRTFDR.setStatus("current")
_F3EsaProbeHistorySoamPmExtP2rAvailableDeltaTs_Type = PerfCounter64
_F3EsaProbeHistorySoamPmExtP2rAvailableDeltaTs_Object = MibTableColumn
f3EsaProbeHistorySoamPmExtP2rAvailableDeltaTs = _F3EsaProbeHistorySoamPmExtP2rAvailableDeltaTs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 22, 1, 34),
    _F3EsaProbeHistorySoamPmExtP2rAvailableDeltaTs_Type()
)
f3EsaProbeHistorySoamPmExtP2rAvailableDeltaTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeHistorySoamPmExtP2rAvailableDeltaTs.setStatus("current")
_F3EsaProbeHistorySoamPmExtR2pAvailableDeltaTs_Type = PerfCounter64
_F3EsaProbeHistorySoamPmExtR2pAvailableDeltaTs_Object = MibTableColumn
f3EsaProbeHistorySoamPmExtR2pAvailableDeltaTs = _F3EsaProbeHistorySoamPmExtR2pAvailableDeltaTs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 22, 1, 35),
    _F3EsaProbeHistorySoamPmExtR2pAvailableDeltaTs_Type()
)
f3EsaProbeHistorySoamPmExtR2pAvailableDeltaTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeHistorySoamPmExtR2pAvailableDeltaTs.setStatus("current")
_F3EsaProbeHistorySoamPmExtP2rUnavailableDeltaTs_Type = PerfCounter64
_F3EsaProbeHistorySoamPmExtP2rUnavailableDeltaTs_Object = MibTableColumn
f3EsaProbeHistorySoamPmExtP2rUnavailableDeltaTs = _F3EsaProbeHistorySoamPmExtP2rUnavailableDeltaTs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 22, 1, 36),
    _F3EsaProbeHistorySoamPmExtP2rUnavailableDeltaTs_Type()
)
f3EsaProbeHistorySoamPmExtP2rUnavailableDeltaTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeHistorySoamPmExtP2rUnavailableDeltaTs.setStatus("current")
_F3EsaProbeHistorySoamPmExtR2pUnavailableDeltaTs_Type = PerfCounter64
_F3EsaProbeHistorySoamPmExtR2pUnavailableDeltaTs_Object = MibTableColumn
f3EsaProbeHistorySoamPmExtR2pUnavailableDeltaTs = _F3EsaProbeHistorySoamPmExtR2pUnavailableDeltaTs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 22, 1, 37),
    _F3EsaProbeHistorySoamPmExtR2pUnavailableDeltaTs_Type()
)
f3EsaProbeHistorySoamPmExtR2pUnavailableDeltaTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeHistorySoamPmExtR2pUnavailableDeltaTs.setStatus("current")
_F3EsaProbeHistorySoamPmExtElapsedTime_Type = PerfCounter64
_F3EsaProbeHistorySoamPmExtElapsedTime_Object = MibTableColumn
f3EsaProbeHistorySoamPmExtElapsedTime = _F3EsaProbeHistorySoamPmExtElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 1, 22, 1, 38),
    _F3EsaProbeHistorySoamPmExtElapsedTime_Type()
)
f3EsaProbeHistorySoamPmExtElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EsaProbeHistorySoamPmExtElapsedTime.setStatus("current")
_CmServAssuranceNotifications_ObjectIdentity = ObjectIdentity
cmServAssuranceNotifications = _CmServAssuranceNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 2)
)
_CmServAssuranceConformance_ObjectIdentity = ObjectIdentity
cmServAssuranceConformance = _CmServAssuranceConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 3)
)
_CmServAssuranceCompliances_ObjectIdentity = ObjectIdentity
cmServAssuranceCompliances = _CmServAssuranceCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 3, 1)
)
_CmServAssuranceGroups_ObjectIdentity = ObjectIdentity
cmServAssuranceGroups = _CmServAssuranceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 3, 2)
)
esaProbeCOSConfigEntry.registerAugmentions(
    ("CM-SA-MIB",
     "f3EsaProbeCOSConfigSoamPmExtEntry")
)
f3EsaProbeCOSConfigSoamPmExtEntry.setIndexNames(*esaProbeCOSConfigEntry.getIndexNames())
esaProbeStatsEntry.registerAugmentions(
    ("CM-SA-MIB",
     "f3EsaProbeStatsSoamPmExtEntry")
)
f3EsaProbeStatsSoamPmExtEntry.setIndexNames(*esaProbeStatsEntry.getIndexNames())
esaProbeHistoryEntry.registerAugmentions(
    ("CM-SA-MIB",
     "f3EsaProbeHistorySoamPmExtEntry")
)
f3EsaProbeHistorySoamPmExtEntry.setIndexNames(*esaProbeHistoryEntry.getIndexNames())

# Managed Objects groups

cmServAssuranceObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 3, 2, 1)
)
cmServAssuranceObjectGroup.setObjects(
      *(("CM-SA-MIB", "ecpaControlIndex"),
        ("CM-SA-MIB", "ecpaControlSourcePort"),
        ("CM-SA-MIB", "ecpaControlTestType"),
        ("CM-SA-MIB", "ecpaControlNumFrames"),
        ("CM-SA-MIB", "ecpaControlDuration"),
        ("CM-SA-MIB", "ecpaControlInjectorDirection"),
        ("CM-SA-MIB", "ecpaControlMonitorDirection"),
        ("CM-SA-MIB", "ecpaControlStream1"),
        ("CM-SA-MIB", "ecpaControlStream2"),
        ("CM-SA-MIB", "ecpaControlStream3"),
        ("CM-SA-MIB", "ecpaControlAction"),
        ("CM-SA-MIB", "ecpaControlTestStatus"),
        ("CM-SA-MIB", "ecpaControlEcpaType"),
        ("CM-SA-MIB", "ecpaControlMonitorPortType"),
        ("CM-SA-MIB", "ecpaConfigStreamIndex"),
        ("CM-SA-MIB", "ecpaConfigStreamName"),
        ("CM-SA-MIB", "ecpaConfigStreamFrameSize"),
        ("CM-SA-MIB", "ecpaConfigStreamRate"),
        ("CM-SA-MIB", "ecpaConfigStreamPayloadType"),
        ("CM-SA-MIB", "ecpaConfigStreamSignature"),
        ("CM-SA-MIB", "ecpaConfigStreamDestinationMAC"),
        ("CM-SA-MIB", "ecpaConfigStreamSourceMAC"),
        ("CM-SA-MIB", "ecpaConfigStreamOuterVlanEnabled"),
        ("CM-SA-MIB", "ecpaConfigStreamOuterVlanId"),
        ("CM-SA-MIB", "ecpaConfigStreamOuterVlanPrio"),
        ("CM-SA-MIB", "ecpaConfigStreamOuterVlanEtherType"),
        ("CM-SA-MIB", "ecpaConfigStreamInnerVlanEnabled"),
        ("CM-SA-MIB", "ecpaConfigStreamInnerVlanId"),
        ("CM-SA-MIB", "ecpaConfigStreamInnerVlanPrio"),
        ("CM-SA-MIB", "ecpaConfigStreamInnerVlanEtherType"),
        ("CM-SA-MIB", "ecpaConfigStreamIpVersion"),
        ("CM-SA-MIB", "ecpaConfigStreamIpV4Address"),
        ("CM-SA-MIB", "ecpaConfigStreamIpV6Address"),
        ("CM-SA-MIB", "ecpaConfigStreamPrioMapMode"),
        ("CM-SA-MIB", "ecpaConfigStreamPrioVal"),
        ("CM-SA-MIB", "ecpaConfigStreamInnerVlan2Enabled"),
        ("CM-SA-MIB", "ecpaConfigStreamInnerVlan2Id"),
        ("CM-SA-MIB", "ecpaConfigStreamInnerVlan2Prio"),
        ("CM-SA-MIB", "ecpaConfigStreamInnerVlan2EtherType"),
        ("CM-SA-MIB", "ecpaConfigStreamDestIpV4Address"),
        ("CM-SA-MIB", "ecpaConfigStreamDestIpV6Address"),
        ("CM-SA-MIB", "ecpaConfigStreamUsePortSourceMAC"),
        ("CM-SA-MIB", "ecpaConfigStreamRateHi"),
        ("CM-SA-MIB", "ecpaConfigStreamUdpControl"),
        ("CM-SA-MIB", "ecpaConfigStreamUdpSrcPort"),
        ("CM-SA-MIB", "ecpaConfigStreamUdpDstPort"),
        ("CM-SA-MIB", "ecpaTestStreamIndex"),
        ("CM-SA-MIB", "ecpaTestStreamSourcePort"),
        ("CM-SA-MIB", "ecpaTestStreamName"),
        ("CM-SA-MIB", "ecpaTestStreamFrameSize"),
        ("CM-SA-MIB", "ecpaTestStreamRate"),
        ("CM-SA-MIB", "ecpaTestStreamPayloadType"),
        ("CM-SA-MIB", "ecpaTestStreamSignature"),
        ("CM-SA-MIB", "ecpaTestStreamDestinationMAC"),
        ("CM-SA-MIB", "ecpaTestStreamSourceMAC"),
        ("CM-SA-MIB", "ecpaTestStreamOuterVlanEnabled"),
        ("CM-SA-MIB", "ecpaTestStreamOuterVlanId"),
        ("CM-SA-MIB", "ecpaTestStreamOuterVlanPrio"),
        ("CM-SA-MIB", "ecpaTestStreamOuterVlanEtherType"),
        ("CM-SA-MIB", "ecpaTestStreamInnerVlanEnabled"),
        ("CM-SA-MIB", "ecpaTestStreamInnerVlanId"),
        ("CM-SA-MIB", "ecpaTestStreamInnerVlanPrio"),
        ("CM-SA-MIB", "ecpaTestStreamInnerVlanEtherType"),
        ("CM-SA-MIB", "ecpaTestStreamIpVersion"),
        ("CM-SA-MIB", "ecpaTestStreamIpV4Address"),
        ("CM-SA-MIB", "ecpaTestStreamIpV6Address"),
        ("CM-SA-MIB", "ecpaTestStreamPrioMapMode"),
        ("CM-SA-MIB", "ecpaTestStreamPrioVal"),
        ("CM-SA-MIB", "ecpaTestStreamMonStartTime"),
        ("CM-SA-MIB", "ecpaTestStreamMonEndTime"),
        ("CM-SA-MIB", "ecpaTestStreamMonElapsedTime"),
        ("CM-SA-MIB", "ecpaTestStreamMonTxFrames"),
        ("CM-SA-MIB", "ecpaTestStreamMonRxFrames"),
        ("CM-SA-MIB", "ecpaTestStreamMonRxPercentSuccess"),
        ("CM-SA-MIB", "ecpaTestStreamMonRxOutOfSeqErrs"),
        ("CM-SA-MIB", "ecpaTestStreamMonRxSeqGaps"),
        ("CM-SA-MIB", "ecpaTestStreamMonRxNonEcpaFrames"),
        ("CM-SA-MIB", "ecpaTestStreamMonRxMinDelay"),
        ("CM-SA-MIB", "ecpaTestStreamMonRxMaxDelay"),
        ("CM-SA-MIB", "ecpaTestStreamMonRxAvgDelay"),
        ("CM-SA-MIB", "ecpaTestStreamMonRx1stFrameSize"),
        ("CM-SA-MIB", "ecpaTestStreamMonRx1stFrame1Octets"),
        ("CM-SA-MIB", "ecpaTestStreamMonRx1stFrame2Octets"),
        ("CM-SA-MIB", "ecpaTestStreamMonRx1stFrame3Octets"),
        ("CM-SA-MIB", "ecpaTestStreamMonRx1stFrame4Octets"),
        ("CM-SA-MIB", "ecpaTestStreamMonRx1stFrame5Octets"),
        ("CM-SA-MIB", "ecpaTestStreamMonRx1stFrame6Octets"),
        ("CM-SA-MIB", "ecpaTestStreamMonRx1stFrame7Octets"),
        ("CM-SA-MIB", "ecpaTestStreamMonRx1stFrame8Octets"),
        ("CM-SA-MIB", "ecpaTestStreamMonRx1stFrame9Octets"),
        ("CM-SA-MIB", "ecpaTestStreamMonRx1stFrame10Octets"),
        ("CM-SA-MIB", "ecpaTestStreamMonRxBitRate"),
        ("CM-SA-MIB", "ecpaTestStreamInnerVlan2Enabled"),
        ("CM-SA-MIB", "ecpaTestStreamInnerVlan2Id"),
        ("CM-SA-MIB", "ecpaTestStreamInnerVlan2Prio"),
        ("CM-SA-MIB", "ecpaTestStreamInnerVlan2EtherType"),
        ("CM-SA-MIB", "ecpaTestStreamDestIpV4Address"),
        ("CM-SA-MIB", "ecpaTestStreamDestIpV6Address"),
        ("CM-SA-MIB", "ecpaTestStreamConfigChanged"),
        ("CM-SA-MIB", "ecpaTestStreamRateHi"),
        ("CM-SA-MIB", "ecpaTestStreamUdpControl"),
        ("CM-SA-MIB", "ecpaTestStreamUdpSrcPort"),
        ("CM-SA-MIB", "ecpaTestStreamUdpDstPort"),
        ("CM-SA-MIB", "esaProbeIndex"),
        ("CM-SA-MIB", "esaProbeName"),
        ("CM-SA-MIB", "esaProbeSourcePort"),
        ("CM-SA-MIB", "esaProbeAssocSchedGroup"),
        ("CM-SA-MIB", "esaProbeDirection"),
        ("CM-SA-MIB", "esaProbeProtocol"),
        ("CM-SA-MIB", "esaProbeSrcIpAddress"),
        ("CM-SA-MIB", "esaProbeSrcSubnetMask"),
        ("CM-SA-MIB", "esaProbeDestIpAddress"),
        ("CM-SA-MIB", "esaProbeSrcMep"),
        ("CM-SA-MIB", "esaProbeDestMepType"),
        ("CM-SA-MIB", "esaProbeDestMepMacAddr"),
        ("CM-SA-MIB", "esaProbeDestMepId"),
        ("CM-SA-MIB", "esaProbeVlanTagEnabled"),
        ("CM-SA-MIB", "esaProbeVlanTagEtherType"),
        ("CM-SA-MIB", "esaProbeVlanId"),
        ("CM-SA-MIB", "esaProbeVlanPrio"),
        ("CM-SA-MIB", "esaProbeInnerVlanTagEnabled"),
        ("CM-SA-MIB", "esaProbeInnerVlanTagEtherType"),
        ("CM-SA-MIB", "esaProbeInnerVlanId"),
        ("CM-SA-MIB", "esaProbeInnerVlanPrio"),
        ("CM-SA-MIB", "esaProbeIpPrioMapMode"),
        ("CM-SA-MIB", "esaProbeIpPriority"),
        ("CM-SA-MIB", "esaProbePktsPerSample"),
        ("CM-SA-MIB", "esaProbePktSize"),
        ("CM-SA-MIB", "esaProbeInterPktGap"),
        ("CM-SA-MIB", "esaProbePktDeadInterval"),
        ("CM-SA-MIB", "esaProbeResponseTimeout"),
        ("CM-SA-MIB", "esaProbeY1731DmmPktSize"),
        ("CM-SA-MIB", "esaProbeY1731LmmInterval"),
        ("CM-SA-MIB", "esaProbeY1731DmmInterval"),
        ("CM-SA-MIB", "esaProbeHistoryBins"),
        ("CM-SA-MIB", "esaProbeHistoryInterval"),
        ("CM-SA-MIB", "esaProbeDistHistoryBins"),
        ("CM-SA-MIB", "esaProbeDistHistoryInterval"),
        ("CM-SA-MIB", "esaProbeCreationTime"),
        ("CM-SA-MIB", "esaProbeStorageType"),
        ("CM-SA-MIB", "esaProbeRowStatus"),
        ("CM-SA-MIB", "esaProbeInner2VlanTagEnabled"),
        ("CM-SA-MIB", "esaProbeInner2VlanTagEtherType"),
        ("CM-SA-MIB", "esaProbeInner2VlanId"),
        ("CM-SA-MIB", "esaProbeInner2VlanPrio"),
        ("CM-SA-MIB", "esaProbeAdminState"),
        ("CM-SA-MIB", "esaProbeOperationalState"),
        ("CM-SA-MIB", "esaProbeSecondaryState"),
        ("CM-SA-MIB", "esaProbeScheduleGroupIndex"),
        ("CM-SA-MIB", "esaProbeScheduleGroupDescr"),
        ("CM-SA-MIB", "esaProbeScheduleGroupProbeList"),
        ("CM-SA-MIB", "esaProbeScheduleGroupType"),
        ("CM-SA-MIB", "esaProbeScheduleGroupStartTime"),
        ("CM-SA-MIB", "esaProbeScheduleGroupDuration"),
        ("CM-SA-MIB", "esaProbeScheduleGroupInterval"),
        ("CM-SA-MIB", "esaProbeScheduleGroupAction"),
        ("CM-SA-MIB", "esaProbeScheduleGroupStatus"),
        ("CM-SA-MIB", "esaProbeScheduleGroupStorageType"),
        ("CM-SA-MIB", "esaProbeScheduleGroupRowStatus"),
        ("CM-SA-MIB", "esaProbeScheduleGroupActionProbeList"),
        ("CM-SA-MIB", "esaReflectorIndex"),
        ("CM-SA-MIB", "esaReflectorName"),
        ("CM-SA-MIB", "esaReflectorIpAddress"),
        ("CM-SA-MIB", "esaReflectorSubnetMask"),
        ("CM-SA-MIB", "esaReflectorSourcePort"),
        ("CM-SA-MIB", "esaReflectorIpPrioMapMode"),
        ("CM-SA-MIB", "esaReflectorIpPriority"),
        ("CM-SA-MIB", "esaReflectorAction"),
        ("CM-SA-MIB", "esaReflectorSuspended"),
        ("CM-SA-MIB", "esaReflectorCreationTime"),
        ("CM-SA-MIB", "esaReflectorStorageType"),
        ("CM-SA-MIB", "esaReflectorRowStatus"),
        ("CM-SA-MIB", "esaReflectorDirection"),
        ("CM-SA-MIB", "esaReflectorAdminState"),
        ("CM-SA-MIB", "esaReflectorOperationalState"),
        ("CM-SA-MIB", "esaReflectorSecondaryState"),
        ("CM-SA-MIB", "esaProbeStatsDestinationIndex"),
        ("CM-SA-MIB", "esaProbeStatsCOSIndex"),
        ("CM-SA-MIB", "esaProbeStatsIndex"),
        ("CM-SA-MIB", "esaProbeStatsIntervalType"),
        ("CM-SA-MIB", "esaProbeStatsCOS"),
        ("CM-SA-MIB", "esaProbeStatsValid"),
        ("CM-SA-MIB", "esaProbeStatsAction"),
        ("CM-SA-MIB", "esaProbeStatsP2RPkts"),
        ("CM-SA-MIB", "esaProbeStatsP2RErredPkts"),
        ("CM-SA-MIB", "esaProbeStatsP2RSyncErrs"),
        ("CM-SA-MIB", "esaProbeStatsP2RLostPkts"),
        ("CM-SA-MIB", "esaProbeStatsR2PPkts"),
        ("CM-SA-MIB", "esaProbeStatsR2PErredPkts"),
        ("CM-SA-MIB", "esaProbeStatsR2PSyncErrs"),
        ("CM-SA-MIB", "esaProbeStatsR2PLostPkts"),
        ("CM-SA-MIB", "esaProbeStatsLostPkts"),
        ("CM-SA-MIB", "esaProbeStatsSeqGaps"),
        ("CM-SA-MIB", "esaProbeStatsOutOfSeqErrs"),
        ("CM-SA-MIB", "esaProbeStatsMinRoundTripDelay"),
        ("CM-SA-MIB", "esaProbeStatsMaxRoundTripDelay"),
        ("CM-SA-MIB", "esaProbeStatsAvgRoundTripDelay"),
        ("CM-SA-MIB", "esaProbeStatsSumRoundTripDelay"),
        ("CM-SA-MIB", "esaProbeStatsSumOfSqRoundTripDelay"),
        ("CM-SA-MIB", "esaProbeStatsMinOnewayP2RDelay"),
        ("CM-SA-MIB", "esaProbeStatsMaxOnewayP2RDelay"),
        ("CM-SA-MIB", "esaProbeStatsAvgOnewayP2RDelay"),
        ("CM-SA-MIB", "esaProbeStatsSumOnewayP2RDelay"),
        ("CM-SA-MIB", "esaProbeStatsSumOfSqOnewayP2RDelay"),
        ("CM-SA-MIB", "esaProbeStatsMinOnewayR2PDelay"),
        ("CM-SA-MIB", "esaProbeStatsMaxOnewayR2PDelay"),
        ("CM-SA-MIB", "esaProbeStatsAvgOnewayR2PDelay"),
        ("CM-SA-MIB", "esaProbeStatsSumOnewayR2PDelay"),
        ("CM-SA-MIB", "esaProbeStatsSumOfSqOnewayR2PDelay"),
        ("CM-SA-MIB", "esaProbeStatsMinPosP2RJitter"),
        ("CM-SA-MIB", "esaProbeStatsMaxPosP2RJitter"),
        ("CM-SA-MIB", "esaProbeStatsNumPosP2RJitter"),
        ("CM-SA-MIB", "esaProbeStatsSumPosP2RJitter"),
        ("CM-SA-MIB", "esaProbeStatsSumOfSqPosP2RJitter"),
        ("CM-SA-MIB", "esaProbeStatsMinNegP2RJitter"),
        ("CM-SA-MIB", "esaProbeStatsMaxNegP2RJitter"),
        ("CM-SA-MIB", "esaProbeStatsNumNegP2RJitter"),
        ("CM-SA-MIB", "esaProbeStatsSumNegP2RJitter"),
        ("CM-SA-MIB", "esaProbeStatsSumOfSqNegP2RJitter"),
        ("CM-SA-MIB", "esaProbeStatsMinPosR2PJitter"),
        ("CM-SA-MIB", "esaProbeStatsMaxPosR2PJitter"),
        ("CM-SA-MIB", "esaProbeStatsNumPosR2PJitter"),
        ("CM-SA-MIB", "esaProbeStatsSumPosR2PJitter"),
        ("CM-SA-MIB", "esaProbeStatsSumOfSqPosR2PJitter"),
        ("CM-SA-MIB", "esaProbeStatsMinNegR2PJitter"),
        ("CM-SA-MIB", "esaProbeStatsMaxNegR2PJitter"),
        ("CM-SA-MIB", "esaProbeStatsNumNegR2PJitter"),
        ("CM-SA-MIB", "esaProbeStatsSumNegR2PJitter"),
        ("CM-SA-MIB", "esaProbeStatsSumOfSqNegR2PJitter"),
        ("CM-SA-MIB", "esaProbeStatsY1731P2RNegLossOccurrences"),
        ("CM-SA-MIB", "esaProbeStatsY1731R2PNegLossOccurrences"),
        ("CM-SA-MIB", "esaProbeStatsY1731RxLmSamples"),
        ("CM-SA-MIB", "esaProbeStatsY1731RxDmSamples"),
        ("CM-SA-MIB", "esaProbeStatsY1731P2RFrames"),
        ("CM-SA-MIB", "esaProbeStatsY1731R2PFrames"),
        ("CM-SA-MIB", "esaProbeStatsAvgAbsP2RJitter"),
        ("CM-SA-MIB", "esaProbeStatsAvgAbsR2PJitter"),
        ("CM-SA-MIB", "esaProbeStatsMaxAbsP2RJitter"),
        ("CM-SA-MIB", "esaProbeStatsMaxAbsR2PJitter"),
        ("CM-SA-MIB", "esaProbeStatsMinAbsP2RJitter"),
        ("CM-SA-MIB", "esaProbeStatsMinAbsR2PJitter"),
        ("CM-SA-MIB", "esaProbeStatsNumAbsP2RJitter"),
        ("CM-SA-MIB", "esaProbeStatsNumAbsR2PJitter"),
        ("CM-SA-MIB", "esaProbeStatsSumAbsP2RJitter"),
        ("CM-SA-MIB", "esaProbeStatsSumAbsR2PJitter"),
        ("CM-SA-MIB", "esaProbeStatsSumOfSqAbsP2RJitter"),
        ("CM-SA-MIB", "esaProbeStatsSumOfSqAbsR2PJitter"),
        ("CM-SA-MIB", "esaProbeHistoryDestinationIndex"),
        ("CM-SA-MIB", "esaProbeHistoryCOSIndex"),
        ("CM-SA-MIB", "esaProbeHistoryIndex"),
        ("CM-SA-MIB", "esaProbeHistoryTime"),
        ("CM-SA-MIB", "esaProbeHistoryValid"),
        ("CM-SA-MIB", "esaProbeHistoryAction"),
        ("CM-SA-MIB", "esaProbeHistoryCOS"),
        ("CM-SA-MIB", "esaProbeHistoryP2RPkts"),
        ("CM-SA-MIB", "esaProbeHistoryP2RErredPkts"),
        ("CM-SA-MIB", "esaProbeHistoryP2RSyncErrs"),
        ("CM-SA-MIB", "esaProbeHistoryP2RLostPkts"),
        ("CM-SA-MIB", "esaProbeHistoryR2PPkts"),
        ("CM-SA-MIB", "esaProbeHistoryR2PErredPkts"),
        ("CM-SA-MIB", "esaProbeHistoryR2PSyncErrs"),
        ("CM-SA-MIB", "esaProbeHistoryR2PLostPkts"),
        ("CM-SA-MIB", "esaProbeHistoryLostPkts"),
        ("CM-SA-MIB", "esaProbeHistorySeqGaps"),
        ("CM-SA-MIB", "esaProbeHistoryOutOfSeqErrs"),
        ("CM-SA-MIB", "esaProbeHistoryMinRoundTripDelay"),
        ("CM-SA-MIB", "esaProbeHistoryMaxRoundTripDelay"),
        ("CM-SA-MIB", "esaProbeHistoryAvgRoundTripDelay"),
        ("CM-SA-MIB", "esaProbeHistorySumRoundTripDelay"),
        ("CM-SA-MIB", "esaProbeHistorySumOfSqRoundTripDelay"),
        ("CM-SA-MIB", "esaProbeHistoryMinOnewayP2RDelay"),
        ("CM-SA-MIB", "esaProbeHistoryMaxOnewayP2RDelay"),
        ("CM-SA-MIB", "esaProbeHistoryAvgOnewayP2RDelay"),
        ("CM-SA-MIB", "esaProbeHistorySumOnewayP2RDelay"),
        ("CM-SA-MIB", "esaProbeHistorySumOfSqOnewayP2RDelay"),
        ("CM-SA-MIB", "esaProbeHistoryMinOnewayR2PDelay"),
        ("CM-SA-MIB", "esaProbeHistoryMaxOnewayR2PDelay"),
        ("CM-SA-MIB", "esaProbeHistoryAvgOnewayR2PDelay"),
        ("CM-SA-MIB", "esaProbeHistorySumOnewayR2PDelay"),
        ("CM-SA-MIB", "esaProbeHistorySumOfSqOnewayR2PDelay"),
        ("CM-SA-MIB", "esaProbeHistoryMinPosP2RJitter"),
        ("CM-SA-MIB", "esaProbeHistoryMaxPosP2RJitter"),
        ("CM-SA-MIB", "esaProbeHistoryNumPosP2RJitter"),
        ("CM-SA-MIB", "esaProbeHistorySumPosP2RJitter"),
        ("CM-SA-MIB", "esaProbeHistorySumOfSqPosP2RJitter"),
        ("CM-SA-MIB", "esaProbeHistoryMinNegP2RJitter"),
        ("CM-SA-MIB", "esaProbeHistoryMaxNegP2RJitter"),
        ("CM-SA-MIB", "esaProbeHistoryNumNegP2RJitter"),
        ("CM-SA-MIB", "esaProbeHistorySumNegP2RJitter"),
        ("CM-SA-MIB", "esaProbeHistorySumOfSqNegP2RJitter"),
        ("CM-SA-MIB", "esaProbeHistoryMinPosR2PJitter"),
        ("CM-SA-MIB", "esaProbeHistoryMaxPosR2PJitter"),
        ("CM-SA-MIB", "esaProbeHistoryNumPosR2PJitter"),
        ("CM-SA-MIB", "esaProbeHistorySumPosR2PJitter"),
        ("CM-SA-MIB", "esaProbeHistorySumOfSqPosR2PJitter"),
        ("CM-SA-MIB", "esaProbeHistoryMinNegR2PJitter"),
        ("CM-SA-MIB", "esaProbeHistoryMaxNegR2PJitter"),
        ("CM-SA-MIB", "esaProbeHistoryNumNegR2PJitter"),
        ("CM-SA-MIB", "esaProbeHistorySumNegR2PJitter"),
        ("CM-SA-MIB", "esaProbeHistorySumOfSqNegR2PJitter"),
        ("CM-SA-MIB", "esaProbeHistoryY1731P2RNegLossOccurrences"),
        ("CM-SA-MIB", "esaProbeHistoryY1731R2PNegLossOccurrences"),
        ("CM-SA-MIB", "esaProbeHistoryY1731RxLmSamples"),
        ("CM-SA-MIB", "esaProbeHistoryY1731RxDmSamples"),
        ("CM-SA-MIB", "esaProbeHistoryY1731P2RFrames"),
        ("CM-SA-MIB", "esaProbeHistoryY1731R2PFrames"),
        ("CM-SA-MIB", "esaProbeHistoryAvgAbsP2RJitter"),
        ("CM-SA-MIB", "esaProbeHistoryAvgAbsR2PJitter"),
        ("CM-SA-MIB", "esaProbeHistoryMaxAbsP2RJitter"),
        ("CM-SA-MIB", "esaProbeHistoryMaxAbsR2PJitter"),
        ("CM-SA-MIB", "esaProbeHistoryMinAbsP2RJitter"),
        ("CM-SA-MIB", "esaProbeHistoryMinAbsR2PJitter"),
        ("CM-SA-MIB", "esaProbeHistoryNumAbsP2RJitter"),
        ("CM-SA-MIB", "esaProbeHistoryNumAbsR2PJitter"),
        ("CM-SA-MIB", "esaProbeHistorySumAbsP2RJitter"),
        ("CM-SA-MIB", "esaProbeHistorySumAbsR2PJitter"),
        ("CM-SA-MIB", "esaProbeHistorySumOfSqAbsP2RJitter"),
        ("CM-SA-MIB", "esaProbeHistorySumOfSqAbsR2PJitter"),
        ("CM-SA-MIB", "esaProbeDistStatsConfigIndex"),
        ("CM-SA-MIB", "esaProbeDistStatsConfigType"),
        ("CM-SA-MIB", "esaProbeDistStatsConfigMinVal"),
        ("CM-SA-MIB", "esaProbeDistStatsConfigMaxVal"),
        ("CM-SA-MIB", "esaProbeDistStatsConfigNumBins"),
        ("CM-SA-MIB", "esaProbeDistStatsDestinationIndex"),
        ("CM-SA-MIB", "esaProbeDistStatsCOSIndex"),
        ("CM-SA-MIB", "esaProbeDistStatsCOS"),
        ("CM-SA-MIB", "esaProbeDistStatsNumBins"),
        ("CM-SA-MIB", "esaProbeDistStatsLTMin"),
        ("CM-SA-MIB", "esaProbeDistStatsGTMax"),
        ("CM-SA-MIB", "esaProbeDistStatsBinIndex"),
        ("CM-SA-MIB", "esaProbeDistStatsBinLower"),
        ("CM-SA-MIB", "esaProbeDistStatsBinUpper"),
        ("CM-SA-MIB", "esaProbeDistStatsBinNumSamples"),
        ("CM-SA-MIB", "esaProbeDistHistoryDestinationIndex"),
        ("CM-SA-MIB", "esaProbeDistHistoryCOSIndex"),
        ("CM-SA-MIB", "esaProbeDistHistoryCOS"),
        ("CM-SA-MIB", "esaProbeDistHistoryIndex"),
        ("CM-SA-MIB", "esaProbeDistHistoryTime"),
        ("CM-SA-MIB", "esaProbeDistHistoryAction"),
        ("CM-SA-MIB", "esaProbeDistHistoryNumBins"),
        ("CM-SA-MIB", "esaProbeDistHistoryLTMin"),
        ("CM-SA-MIB", "esaProbeDistHistoryGTMax"),
        ("CM-SA-MIB", "esaProbeDistHistoryBinIndex"),
        ("CM-SA-MIB", "esaProbeDistHistoryBinLower"),
        ("CM-SA-MIB", "esaProbeDistHistoryBinUpper"),
        ("CM-SA-MIB", "esaProbeDistHistoryBinNumSamples"),
        ("CM-SA-MIB", "esaProbeStatsThresholdIndex"),
        ("CM-SA-MIB", "esaProbeStatsThresholdVariable"),
        ("CM-SA-MIB", "esaProbeStatsThresholdAbsValueLo"),
        ("CM-SA-MIB", "esaProbeStatsThresholdAbsValueHi"),
        ("CM-SA-MIB", "esaProbeStatsThresholdMonValue"),
        ("CM-SA-MIB", "esaProbeCOSConfigIndex"),
        ("CM-SA-MIB", "esaProbeCOSConfigType"),
        ("CM-SA-MIB", "esaProbeCOSConfigInterval"),
        ("CM-SA-MIB", "esaProbeCOSConfigPktSize"),
        ("CM-SA-MIB", "esaProbeCOSConfigStorageType"),
        ("CM-SA-MIB", "esaProbeCOSConfigRowStatus"),
        ("CM-SA-MIB", "esaProbeDestinationIndex"),
        ("CM-SA-MIB", "esaProbeDestinationMepType"),
        ("CM-SA-MIB", "esaProbeDestinationMepMacAddr"),
        ("CM-SA-MIB", "esaProbeDestinationMepId"),
        ("CM-SA-MIB", "esaProbeDestinationStorageType"),
        ("CM-SA-MIB", "esaProbeDestinationRowStatus"))
)
if mibBuilder.loadTexts:
    cmServAssuranceObjectGroup.setStatus("deprecated")

cmEcpaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 3, 2, 3)
)
cmEcpaGroup.setObjects(
      *(("CM-SA-MIB", "ecpaControlIndex"),
        ("CM-SA-MIB", "ecpaControlSourcePort"),
        ("CM-SA-MIB", "ecpaControlTestType"),
        ("CM-SA-MIB", "ecpaControlNumFrames"),
        ("CM-SA-MIB", "ecpaControlDuration"),
        ("CM-SA-MIB", "ecpaControlInjectorDirection"),
        ("CM-SA-MIB", "ecpaControlMonitorDirection"),
        ("CM-SA-MIB", "ecpaControlStream1"),
        ("CM-SA-MIB", "ecpaControlStream2"),
        ("CM-SA-MIB", "ecpaControlStream3"),
        ("CM-SA-MIB", "ecpaControlAction"),
        ("CM-SA-MIB", "ecpaControlTestStatus"),
        ("CM-SA-MIB", "ecpaControlStorageType"),
        ("CM-SA-MIB", "ecpaControlRowStatus"),
        ("CM-SA-MIB", "ecpaControlEcpaType"),
        ("CM-SA-MIB", "ecpaConfigStreamIndex"),
        ("CM-SA-MIB", "ecpaConfigStreamName"),
        ("CM-SA-MIB", "ecpaConfigStreamFrameSize"),
        ("CM-SA-MIB", "ecpaConfigStreamRate"),
        ("CM-SA-MIB", "ecpaConfigStreamPayloadType"),
        ("CM-SA-MIB", "ecpaConfigStreamSignature"),
        ("CM-SA-MIB", "ecpaConfigStreamDestinationMAC"),
        ("CM-SA-MIB", "ecpaConfigStreamSourceMAC"),
        ("CM-SA-MIB", "ecpaConfigStreamOuterVlanEnabled"),
        ("CM-SA-MIB", "ecpaConfigStreamOuterVlanId"),
        ("CM-SA-MIB", "ecpaConfigStreamOuterVlanPrio"),
        ("CM-SA-MIB", "ecpaConfigStreamOuterVlanEtherType"),
        ("CM-SA-MIB", "ecpaConfigStreamInnerVlanEnabled"),
        ("CM-SA-MIB", "ecpaConfigStreamInnerVlanId"),
        ("CM-SA-MIB", "ecpaConfigStreamInnerVlanPrio"),
        ("CM-SA-MIB", "ecpaConfigStreamInnerVlanEtherType"),
        ("CM-SA-MIB", "ecpaConfigStreamIpVersion"),
        ("CM-SA-MIB", "ecpaConfigStreamIpV4Address"),
        ("CM-SA-MIB", "ecpaConfigStreamIpV6Address"),
        ("CM-SA-MIB", "ecpaConfigStreamPrioMapMode"),
        ("CM-SA-MIB", "ecpaConfigStreamPrioVal"),
        ("CM-SA-MIB", "ecpaConfigStreamInnerVlan2Enabled"),
        ("CM-SA-MIB", "ecpaConfigStreamInnerVlan2Id"),
        ("CM-SA-MIB", "ecpaConfigStreamInnerVlan2Prio"),
        ("CM-SA-MIB", "ecpaConfigStreamInnerVlan2EtherType"),
        ("CM-SA-MIB", "ecpaConfigStreamDestIpV4Address"),
        ("CM-SA-MIB", "ecpaConfigStreamDestIpV6Address"),
        ("CM-SA-MIB", "ecpaConfigStreamUsePortSourceMAC"),
        ("CM-SA-MIB", "ecpaConfigStreamRateHi"),
        ("CM-SA-MIB", "ecpaConfigStreamUdpControl"),
        ("CM-SA-MIB", "ecpaConfigStreamUdpSrcPort"),
        ("CM-SA-MIB", "ecpaConfigStreamUdpDstPort"),
        ("CM-SA-MIB", "ecpaTestStreamIndex"),
        ("CM-SA-MIB", "ecpaTestStreamSourcePort"),
        ("CM-SA-MIB", "ecpaTestStreamName"),
        ("CM-SA-MIB", "ecpaTestStreamFrameSize"),
        ("CM-SA-MIB", "ecpaTestStreamRate"),
        ("CM-SA-MIB", "ecpaTestStreamPayloadType"),
        ("CM-SA-MIB", "ecpaTestStreamSignature"),
        ("CM-SA-MIB", "ecpaTestStreamDestinationMAC"),
        ("CM-SA-MIB", "ecpaTestStreamSourceMAC"),
        ("CM-SA-MIB", "ecpaTestStreamOuterVlanEnabled"),
        ("CM-SA-MIB", "ecpaTestStreamOuterVlanId"),
        ("CM-SA-MIB", "ecpaTestStreamOuterVlanPrio"),
        ("CM-SA-MIB", "ecpaTestStreamOuterVlanEtherType"),
        ("CM-SA-MIB", "ecpaTestStreamInnerVlanEnabled"),
        ("CM-SA-MIB", "ecpaTestStreamInnerVlanId"),
        ("CM-SA-MIB", "ecpaTestStreamInnerVlanPrio"),
        ("CM-SA-MIB", "ecpaTestStreamInnerVlanEtherType"),
        ("CM-SA-MIB", "ecpaTestStreamIpVersion"),
        ("CM-SA-MIB", "ecpaTestStreamIpV4Address"),
        ("CM-SA-MIB", "ecpaTestStreamIpV6Address"),
        ("CM-SA-MIB", "ecpaTestStreamPrioMapMode"),
        ("CM-SA-MIB", "ecpaTestStreamPrioVal"),
        ("CM-SA-MIB", "ecpaTestStreamMonStartTime"),
        ("CM-SA-MIB", "ecpaTestStreamMonEndTime"),
        ("CM-SA-MIB", "ecpaTestStreamMonElapsedTime"),
        ("CM-SA-MIB", "ecpaTestStreamMonTxFrames"),
        ("CM-SA-MIB", "ecpaTestStreamMonRxFrames"),
        ("CM-SA-MIB", "ecpaTestStreamMonRxPercentSuccess"),
        ("CM-SA-MIB", "ecpaTestStreamMonRxOutOfSeqErrs"),
        ("CM-SA-MIB", "ecpaTestStreamMonRxSeqGaps"),
        ("CM-SA-MIB", "ecpaTestStreamMonRxNonEcpaFrames"),
        ("CM-SA-MIB", "ecpaTestStreamMonRxMinDelay"),
        ("CM-SA-MIB", "ecpaTestStreamMonRxMaxDelay"),
        ("CM-SA-MIB", "ecpaTestStreamMonRxAvgDelay"),
        ("CM-SA-MIB", "ecpaTestStreamMonRx1stFrameSize"),
        ("CM-SA-MIB", "ecpaTestStreamMonRx1stFrame1Octets"),
        ("CM-SA-MIB", "ecpaTestStreamMonRx1stFrame2Octets"),
        ("CM-SA-MIB", "ecpaTestStreamMonRx1stFrame3Octets"),
        ("CM-SA-MIB", "ecpaTestStreamMonRx1stFrame4Octets"),
        ("CM-SA-MIB", "ecpaTestStreamMonRx1stFrame5Octets"),
        ("CM-SA-MIB", "ecpaTestStreamMonRx1stFrame6Octets"),
        ("CM-SA-MIB", "ecpaTestStreamMonRx1stFrame7Octets"),
        ("CM-SA-MIB", "ecpaTestStreamMonRx1stFrame8Octets"),
        ("CM-SA-MIB", "ecpaTestStreamMonRx1stFrame9Octets"),
        ("CM-SA-MIB", "ecpaTestStreamMonRx1stFrame10Octets"),
        ("CM-SA-MIB", "ecpaTestStreamMonRxBitRate"),
        ("CM-SA-MIB", "ecpaTestStreamInnerVlan2Enabled"),
        ("CM-SA-MIB", "ecpaTestStreamInnerVlan2Id"),
        ("CM-SA-MIB", "ecpaTestStreamInnerVlan2Prio"),
        ("CM-SA-MIB", "ecpaTestStreamInnerVlan2EtherType"),
        ("CM-SA-MIB", "ecpaTestStreamDestIpV4Address"),
        ("CM-SA-MIB", "ecpaTestStreamDestIpV6Address"),
        ("CM-SA-MIB", "ecpaTestStreamConfigChanged"),
        ("CM-SA-MIB", "ecpaTestStreamRateHi"),
        ("CM-SA-MIB", "ecpaTestStreamUdpControl"),
        ("CM-SA-MIB", "ecpaTestStreamUdpSrcPort"),
        ("CM-SA-MIB", "ecpaTestStreamUdpDstPort"))
)
if mibBuilder.loadTexts:
    cmEcpaGroup.setStatus("current")

cmEsaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 3, 2, 4)
)
cmEsaGroup.setObjects(
      *(("CM-SA-MIB", "esaProbeIndex"),
        ("CM-SA-MIB", "esaProbeName"),
        ("CM-SA-MIB", "esaProbeSourcePort"),
        ("CM-SA-MIB", "esaProbeAssocSchedGroup"),
        ("CM-SA-MIB", "esaProbeDirection"),
        ("CM-SA-MIB", "esaProbeProtocol"),
        ("CM-SA-MIB", "esaProbeSrcIpAddress"),
        ("CM-SA-MIB", "esaProbeSrcSubnetMask"),
        ("CM-SA-MIB", "esaProbeDestIpAddress"),
        ("CM-SA-MIB", "esaProbeSrcMep"),
        ("CM-SA-MIB", "esaProbeDestMepType"),
        ("CM-SA-MIB", "esaProbeDestMepMacAddr"),
        ("CM-SA-MIB", "esaProbeDestMepId"),
        ("CM-SA-MIB", "esaProbeVlanTagEnabled"),
        ("CM-SA-MIB", "esaProbeVlanTagEtherType"),
        ("CM-SA-MIB", "esaProbeVlanId"),
        ("CM-SA-MIB", "esaProbeVlanPrio"),
        ("CM-SA-MIB", "esaProbeInnerVlanTagEnabled"),
        ("CM-SA-MIB", "esaProbeInnerVlanTagEtherType"),
        ("CM-SA-MIB", "esaProbeInnerVlanId"),
        ("CM-SA-MIB", "esaProbeInnerVlanPrio"),
        ("CM-SA-MIB", "esaProbeIpPrioMapMode"),
        ("CM-SA-MIB", "esaProbeIpPriority"),
        ("CM-SA-MIB", "esaProbePktsPerSample"),
        ("CM-SA-MIB", "esaProbePktSize"),
        ("CM-SA-MIB", "esaProbeInterPktGap"),
        ("CM-SA-MIB", "esaProbePktDeadInterval"),
        ("CM-SA-MIB", "esaProbeResponseTimeout"),
        ("CM-SA-MIB", "esaProbeY1731DmmPktSize"),
        ("CM-SA-MIB", "esaProbeY1731LmmInterval"),
        ("CM-SA-MIB", "esaProbeY1731DmmInterval"),
        ("CM-SA-MIB", "esaProbeHistoryBins"),
        ("CM-SA-MIB", "esaProbeHistoryInterval"),
        ("CM-SA-MIB", "esaProbeDistHistoryBins"),
        ("CM-SA-MIB", "esaProbeDistHistoryInterval"),
        ("CM-SA-MIB", "esaProbeCreationTime"),
        ("CM-SA-MIB", "esaProbeStorageType"),
        ("CM-SA-MIB", "esaProbeRowStatus"),
        ("CM-SA-MIB", "esaProbeMultiCOSEnabled"),
        ("CM-SA-MIB", "esaProbeSLAMonitorType"),
        ("CM-SA-MIB", "esaProbeCOSType"),
        ("CM-SA-MIB", "esaProbeSLMMulticastMACEnabled"),
        ("CM-SA-MIB", "esaProbeSOAMInterval"),
        ("CM-SA-MIB", "esaProbeSOAMPktSize"),
        ("CM-SA-MIB", "esaProbeAdminState"),
        ("CM-SA-MIB", "esaProbeOperationalState"),
        ("CM-SA-MIB", "esaProbeSecondaryState"),
        ("CM-SA-MIB", "esaProbeAlias"),
        ("CM-SA-MIB", "esaProbeScheduleGroupIndex"),
        ("CM-SA-MIB", "esaProbeScheduleGroupDescr"),
        ("CM-SA-MIB", "esaProbeScheduleGroupProbeList"),
        ("CM-SA-MIB", "esaProbeScheduleGroupType"),
        ("CM-SA-MIB", "esaProbeScheduleGroupStartTime"),
        ("CM-SA-MIB", "esaProbeScheduleGroupDuration"),
        ("CM-SA-MIB", "esaProbeScheduleGroupInterval"),
        ("CM-SA-MIB", "esaProbeScheduleGroupAction"),
        ("CM-SA-MIB", "esaProbeScheduleGroupStatus"),
        ("CM-SA-MIB", "esaProbeScheduleGroupStorageType"),
        ("CM-SA-MIB", "esaProbeScheduleGroupRowStatus"),
        ("CM-SA-MIB", "esaReflectorIndex"),
        ("CM-SA-MIB", "esaReflectorName"),
        ("CM-SA-MIB", "esaReflectorIpAddress"),
        ("CM-SA-MIB", "esaReflectorSubnetMask"),
        ("CM-SA-MIB", "esaReflectorSourcePort"),
        ("CM-SA-MIB", "esaReflectorIpPrioMapMode"),
        ("CM-SA-MIB", "esaReflectorIpPriority"),
        ("CM-SA-MIB", "esaReflectorAction"),
        ("CM-SA-MIB", "esaReflectorSuspended"),
        ("CM-SA-MIB", "esaReflectorCreationTime"),
        ("CM-SA-MIB", "esaReflectorStorageType"),
        ("CM-SA-MIB", "esaReflectorRowStatus"),
        ("CM-SA-MIB", "esaReflectorDirection"),
        ("CM-SA-MIB", "esaReflectorAdminState"),
        ("CM-SA-MIB", "esaReflectorOperationalState"),
        ("CM-SA-MIB", "esaReflectorSecondaryState"),
        ("CM-SA-MIB", "esaReflectorAlias"),
        ("CM-SA-MIB", "esaProbeStatsDestinationIndex"),
        ("CM-SA-MIB", "esaProbeStatsCOSIndex"),
        ("CM-SA-MIB", "esaProbeStatsIndex"),
        ("CM-SA-MIB", "esaProbeStatsIntervalType"),
        ("CM-SA-MIB", "esaProbeStatsCOS"),
        ("CM-SA-MIB", "esaProbeStatsValid"),
        ("CM-SA-MIB", "esaProbeStatsAction"),
        ("CM-SA-MIB", "esaProbeStatsP2RPkts"),
        ("CM-SA-MIB", "esaProbeStatsP2RErredPkts"),
        ("CM-SA-MIB", "esaProbeStatsP2RSyncErrs"),
        ("CM-SA-MIB", "esaProbeStatsP2RLostPkts"),
        ("CM-SA-MIB", "esaProbeStatsR2PPkts"),
        ("CM-SA-MIB", "esaProbeStatsR2PErredPkts"),
        ("CM-SA-MIB", "esaProbeStatsR2PSyncErrs"),
        ("CM-SA-MIB", "esaProbeStatsR2PLostPkts"),
        ("CM-SA-MIB", "esaProbeStatsLostPkts"),
        ("CM-SA-MIB", "esaProbeStatsSeqGaps"),
        ("CM-SA-MIB", "esaProbeStatsOutOfSeqErrs"),
        ("CM-SA-MIB", "esaProbeStatsMinRoundTripDelay"),
        ("CM-SA-MIB", "esaProbeStatsMaxRoundTripDelay"),
        ("CM-SA-MIB", "esaProbeStatsAvgRoundTripDelay"),
        ("CM-SA-MIB", "esaProbeStatsSumRoundTripDelay"),
        ("CM-SA-MIB", "esaProbeStatsSumOfSqRoundTripDelay"),
        ("CM-SA-MIB", "esaProbeStatsMinOnewayP2RDelay"),
        ("CM-SA-MIB", "esaProbeStatsMaxOnewayP2RDelay"),
        ("CM-SA-MIB", "esaProbeStatsAvgOnewayP2RDelay"),
        ("CM-SA-MIB", "esaProbeStatsSumOnewayP2RDelay"),
        ("CM-SA-MIB", "esaProbeStatsSumOfSqOnewayP2RDelay"),
        ("CM-SA-MIB", "esaProbeStatsMinOnewayR2PDelay"),
        ("CM-SA-MIB", "esaProbeStatsMaxOnewayR2PDelay"),
        ("CM-SA-MIB", "esaProbeStatsAvgOnewayR2PDelay"),
        ("CM-SA-MIB", "esaProbeStatsSumOnewayR2PDelay"),
        ("CM-SA-MIB", "esaProbeStatsSumOfSqOnewayR2PDelay"),
        ("CM-SA-MIB", "esaProbeStatsMinPosP2RJitter"),
        ("CM-SA-MIB", "esaProbeStatsMaxPosP2RJitter"),
        ("CM-SA-MIB", "esaProbeStatsNumPosP2RJitter"),
        ("CM-SA-MIB", "esaProbeStatsSumPosP2RJitter"),
        ("CM-SA-MIB", "esaProbeStatsSumOfSqPosP2RJitter"),
        ("CM-SA-MIB", "esaProbeStatsMinNegP2RJitter"),
        ("CM-SA-MIB", "esaProbeStatsMaxNegP2RJitter"),
        ("CM-SA-MIB", "esaProbeStatsNumNegP2RJitter"),
        ("CM-SA-MIB", "esaProbeStatsSumNegP2RJitter"),
        ("CM-SA-MIB", "esaProbeStatsSumOfSqNegP2RJitter"),
        ("CM-SA-MIB", "esaProbeStatsMinPosR2PJitter"),
        ("CM-SA-MIB", "esaProbeStatsMaxPosR2PJitter"),
        ("CM-SA-MIB", "esaProbeStatsNumPosR2PJitter"),
        ("CM-SA-MIB", "esaProbeStatsSumPosR2PJitter"),
        ("CM-SA-MIB", "esaProbeStatsSumOfSqPosR2PJitter"),
        ("CM-SA-MIB", "esaProbeStatsMinNegR2PJitter"),
        ("CM-SA-MIB", "esaProbeStatsMaxNegR2PJitter"),
        ("CM-SA-MIB", "esaProbeStatsNumNegR2PJitter"),
        ("CM-SA-MIB", "esaProbeStatsSumNegR2PJitter"),
        ("CM-SA-MIB", "esaProbeStatsSumOfSqNegR2PJitter"),
        ("CM-SA-MIB", "esaProbeStatsY1731P2RNegLossOccurrences"),
        ("CM-SA-MIB", "esaProbeStatsY1731R2PNegLossOccurrences"),
        ("CM-SA-MIB", "esaProbeStatsY1731RxLmSamples"),
        ("CM-SA-MIB", "esaProbeStatsY1731RxDmSamples"),
        ("CM-SA-MIB", "esaProbeStatsY1731P2RFrames"),
        ("CM-SA-MIB", "esaProbeStatsY1731R2PFrames"),
        ("CM-SA-MIB", "esaProbeStatsAvgAbsP2RJitter"),
        ("CM-SA-MIB", "esaProbeStatsAvgAbsR2PJitter"),
        ("CM-SA-MIB", "esaProbeStatsMaxAbsP2RJitter"),
        ("CM-SA-MIB", "esaProbeStatsMaxAbsR2PJitter"),
        ("CM-SA-MIB", "esaProbeStatsMinAbsP2RJitter"),
        ("CM-SA-MIB", "esaProbeStatsMinAbsR2PJitter"),
        ("CM-SA-MIB", "esaProbeStatsNumAbsP2RJitter"),
        ("CM-SA-MIB", "esaProbeStatsNumAbsR2PJitter"),
        ("CM-SA-MIB", "esaProbeStatsSumAbsP2RJitter"),
        ("CM-SA-MIB", "esaProbeStatsSumAbsR2PJitter"),
        ("CM-SA-MIB", "esaProbeStatsSumOfSqAbsP2RJitter"),
        ("CM-SA-MIB", "esaProbeStatsSumOfSqAbsR2PJitter"),
        ("CM-SA-MIB", "esaProbeHistoryDestinationIndex"),
        ("CM-SA-MIB", "esaProbeHistoryCOSIndex"),
        ("CM-SA-MIB", "esaProbeHistoryIndex"),
        ("CM-SA-MIB", "esaProbeHistoryTime"),
        ("CM-SA-MIB", "esaProbeHistoryValid"),
        ("CM-SA-MIB", "esaProbeHistoryAction"),
        ("CM-SA-MIB", "esaProbeHistoryCOS"),
        ("CM-SA-MIB", "esaProbeHistoryP2RPkts"),
        ("CM-SA-MIB", "esaProbeHistoryP2RErredPkts"),
        ("CM-SA-MIB", "esaProbeHistoryP2RSyncErrs"),
        ("CM-SA-MIB", "esaProbeHistoryP2RLostPkts"),
        ("CM-SA-MIB", "esaProbeHistoryR2PPkts"),
        ("CM-SA-MIB", "esaProbeHistoryR2PErredPkts"),
        ("CM-SA-MIB", "esaProbeHistoryR2PSyncErrs"),
        ("CM-SA-MIB", "esaProbeHistoryR2PLostPkts"),
        ("CM-SA-MIB", "esaProbeHistoryLostPkts"),
        ("CM-SA-MIB", "esaProbeHistorySeqGaps"),
        ("CM-SA-MIB", "esaProbeHistoryOutOfSeqErrs"),
        ("CM-SA-MIB", "esaProbeHistoryMinRoundTripDelay"),
        ("CM-SA-MIB", "esaProbeHistoryMaxRoundTripDelay"),
        ("CM-SA-MIB", "esaProbeHistoryAvgRoundTripDelay"),
        ("CM-SA-MIB", "esaProbeHistorySumRoundTripDelay"),
        ("CM-SA-MIB", "esaProbeHistorySumOfSqRoundTripDelay"),
        ("CM-SA-MIB", "esaProbeHistoryMinOnewayP2RDelay"),
        ("CM-SA-MIB", "esaProbeHistoryMaxOnewayP2RDelay"),
        ("CM-SA-MIB", "esaProbeHistoryAvgOnewayP2RDelay"),
        ("CM-SA-MIB", "esaProbeHistorySumOnewayP2RDelay"),
        ("CM-SA-MIB", "esaProbeHistorySumOfSqOnewayP2RDelay"),
        ("CM-SA-MIB", "esaProbeHistoryMinOnewayR2PDelay"),
        ("CM-SA-MIB", "esaProbeHistoryMaxOnewayR2PDelay"),
        ("CM-SA-MIB", "esaProbeHistoryAvgOnewayR2PDelay"),
        ("CM-SA-MIB", "esaProbeHistorySumOnewayR2PDelay"),
        ("CM-SA-MIB", "esaProbeHistorySumOfSqOnewayR2PDelay"),
        ("CM-SA-MIB", "esaProbeHistoryMinPosP2RJitter"),
        ("CM-SA-MIB", "esaProbeHistoryMaxPosP2RJitter"),
        ("CM-SA-MIB", "esaProbeHistoryNumPosP2RJitter"),
        ("CM-SA-MIB", "esaProbeHistorySumPosP2RJitter"),
        ("CM-SA-MIB", "esaProbeHistorySumOfSqPosP2RJitter"),
        ("CM-SA-MIB", "esaProbeHistoryMinNegP2RJitter"),
        ("CM-SA-MIB", "esaProbeHistoryMaxNegP2RJitter"),
        ("CM-SA-MIB", "esaProbeHistoryNumNegP2RJitter"),
        ("CM-SA-MIB", "esaProbeHistorySumNegP2RJitter"),
        ("CM-SA-MIB", "esaProbeHistorySumOfSqNegP2RJitter"),
        ("CM-SA-MIB", "esaProbeHistoryMinPosR2PJitter"),
        ("CM-SA-MIB", "esaProbeHistoryMaxPosR2PJitter"),
        ("CM-SA-MIB", "esaProbeHistoryNumPosR2PJitter"),
        ("CM-SA-MIB", "esaProbeHistorySumPosR2PJitter"),
        ("CM-SA-MIB", "esaProbeHistorySumOfSqPosR2PJitter"),
        ("CM-SA-MIB", "esaProbeHistoryMinNegR2PJitter"),
        ("CM-SA-MIB", "esaProbeHistoryMaxNegR2PJitter"),
        ("CM-SA-MIB", "esaProbeHistoryNumNegR2PJitter"),
        ("CM-SA-MIB", "esaProbeHistorySumNegR2PJitter"),
        ("CM-SA-MIB", "esaProbeHistorySumOfSqNegR2PJitter"),
        ("CM-SA-MIB", "esaProbeHistoryY1731P2RNegLossOccurrences"),
        ("CM-SA-MIB", "esaProbeHistoryY1731R2PNegLossOccurrences"),
        ("CM-SA-MIB", "esaProbeHistoryY1731RxLmSamples"),
        ("CM-SA-MIB", "esaProbeHistoryY1731RxDmSamples"),
        ("CM-SA-MIB", "esaProbeHistoryY1731P2RFrames"),
        ("CM-SA-MIB", "esaProbeHistoryY1731R2PFrames"),
        ("CM-SA-MIB", "esaProbeHistoryAvgAbsP2RJitter"),
        ("CM-SA-MIB", "esaProbeHistoryAvgAbsR2PJitter"),
        ("CM-SA-MIB", "esaProbeHistoryMaxAbsP2RJitter"),
        ("CM-SA-MIB", "esaProbeHistoryMaxAbsR2PJitter"),
        ("CM-SA-MIB", "esaProbeHistoryMinAbsP2RJitter"),
        ("CM-SA-MIB", "esaProbeHistoryMinAbsR2PJitter"),
        ("CM-SA-MIB", "esaProbeHistoryNumAbsP2RJitter"),
        ("CM-SA-MIB", "esaProbeHistoryNumAbsR2PJitter"),
        ("CM-SA-MIB", "esaProbeHistorySumAbsP2RJitter"),
        ("CM-SA-MIB", "esaProbeHistorySumAbsR2PJitter"),
        ("CM-SA-MIB", "esaProbeHistorySumOfSqAbsP2RJitter"),
        ("CM-SA-MIB", "esaProbeHistorySumOfSqAbsR2PJitter"),
        ("CM-SA-MIB", "esaProbeDistStatsConfigIndex"),
        ("CM-SA-MIB", "esaProbeDistStatsConfigType"),
        ("CM-SA-MIB", "esaProbeDistStatsConfigMinVal"),
        ("CM-SA-MIB", "esaProbeDistStatsConfigMaxVal"),
        ("CM-SA-MIB", "esaProbeDistStatsConfigNumBins"),
        ("CM-SA-MIB", "esaProbeDistStatsDestinationIndex"),
        ("CM-SA-MIB", "esaProbeDistStatsCOSIndex"),
        ("CM-SA-MIB", "esaProbeDistStatsCOS"),
        ("CM-SA-MIB", "esaProbeDistStatsNumBins"),
        ("CM-SA-MIB", "esaProbeDistStatsLTMin"),
        ("CM-SA-MIB", "esaProbeDistStatsGTMax"),
        ("CM-SA-MIB", "esaProbeDistStatsBinIndex"),
        ("CM-SA-MIB", "esaProbeDistStatsBinLower"),
        ("CM-SA-MIB", "esaProbeDistStatsBinUpper"),
        ("CM-SA-MIB", "esaProbeDistStatsBinNumSamples"),
        ("CM-SA-MIB", "esaProbeDistHistoryDestinationIndex"),
        ("CM-SA-MIB", "esaProbeDistHistoryCOSIndex"),
        ("CM-SA-MIB", "esaProbeDistHistoryCOS"),
        ("CM-SA-MIB", "esaProbeDistHistoryIndex"),
        ("CM-SA-MIB", "esaProbeDistHistoryTime"),
        ("CM-SA-MIB", "esaProbeDistHistoryAction"),
        ("CM-SA-MIB", "esaProbeDistHistoryNumBins"),
        ("CM-SA-MIB", "esaProbeDistHistoryLTMin"),
        ("CM-SA-MIB", "esaProbeDistHistoryGTMax"),
        ("CM-SA-MIB", "esaProbeDistHistoryBinIndex"),
        ("CM-SA-MIB", "esaProbeDistHistoryBinLower"),
        ("CM-SA-MIB", "esaProbeDistHistoryBinUpper"),
        ("CM-SA-MIB", "esaProbeDistHistoryBinNumSamples"),
        ("CM-SA-MIB", "esaProbeStatsThresholdIndex"),
        ("CM-SA-MIB", "esaProbeStatsThresholdVariable"),
        ("CM-SA-MIB", "esaProbeStatsThresholdAbsValueLo"),
        ("CM-SA-MIB", "esaProbeStatsThresholdAbsValueHi"),
        ("CM-SA-MIB", "esaProbeStatsThresholdMonValue"),
        ("CM-SA-MIB", "esaProbeCOSConfigIndex"),
        ("CM-SA-MIB", "esaProbeCOSConfigType"),
        ("CM-SA-MIB", "esaProbeCOSConfigInterval"),
        ("CM-SA-MIB", "esaProbeCOSConfigPktSize"),
        ("CM-SA-MIB", "esaProbeCOSConfigStorageType"),
        ("CM-SA-MIB", "esaProbeCOSConfigRowStatus"),
        ("CM-SA-MIB", "esaProbeCOSConfigslmInterval"),
        ("CM-SA-MIB", "esaProbeCOSConfigslmPktSize"),
        ("CM-SA-MIB", "esaProbeCOSConfigSoamPmExtAvailFlrThreshold"),
        ("CM-SA-MIB", "esaProbeCOSConfigSoamPmExtFlrDeltaTNumLmPdus"),
        ("CM-SA-MIB", "esaProbeCOSConfigSoamPmExtConDeltaTsForAvail"),
        ("CM-SA-MIB", "esaProbeDestinationIndex"),
        ("CM-SA-MIB", "esaProbeDestinationMepType"),
        ("CM-SA-MIB", "esaProbeDestinationMepMacAddr"),
        ("CM-SA-MIB", "esaProbeDestinationMepId"),
        ("CM-SA-MIB", "esaProbeDestinationStorageType"),
        ("CM-SA-MIB", "esaProbeDestinationRowStatus"),
        ("CM-SA-MIB", "f3EsaProbeCOSConfigSoamPmExtAvailFlrThreshold"),
        ("CM-SA-MIB", "f3EsaProbeCOSConfigSoamPmExtFlrDeltaTNumLmPdus"),
        ("CM-SA-MIB", "f3EsaProbeCOSConfigSoamPmExtConDeltaTsForAvail"),
        ("CM-SA-MIB", "f3EsaProbeStatsSoamPmExtMinP2RFlr"),
        ("CM-SA-MIB", "f3EsaProbeStatsSoamPmExtMaxP2RFlr"),
        ("CM-SA-MIB", "f3EsaProbeStatsSoamPmExtAvgP2RFlr"),
        ("CM-SA-MIB", "f3EsaProbeStatsSoamPmExtMinR2PFlr"),
        ("CM-SA-MIB", "f3EsaProbeStatsSoamPmExtMaxR2PFlr"),
        ("CM-SA-MIB", "f3EsaProbeStatsSoamPmExtAvgR2PFlr"),
        ("CM-SA-MIB", "f3EsaProbeStatsSoamPmExtP2rSeverelyErroredDeltaTs"),
        ("CM-SA-MIB", "f3EsaProbeStatsSoamPmExtR2PSeverelyErroredDeltaTs"),
        ("CM-SA-MIB", "f3EsaProbeStatsSoamPmExtP2rAvailableTime"),
        ("CM-SA-MIB", "f3EsaProbeStatsSoamPmExtR2PAvailableTime"),
        ("CM-SA-MIB", "f3EsaProbeStatsSoamPmExtP2rUnavailableTime"),
        ("CM-SA-MIB", "f3EsaProbeStatsSoamPmExtR2PUnavailableTime"),
        ("CM-SA-MIB", "f3EsaProbeStatsSoamPmExtMinAbsRTJitter"),
        ("CM-SA-MIB", "f3EsaProbeStatsSoamPmExtMaxAbsRTJitter"),
        ("CM-SA-MIB", "f3EsaProbeStatsSoamPmExtAvgAbsRTJitter"),
        ("CM-SA-MIB", "f3EsaProbeStatsSoamPmExtNumAbsRTJitter"),
        ("CM-SA-MIB", "f3EsaProbeStatsSoamPmExtSumAbsRTJitter"),
        ("CM-SA-MIB", "f3EsaProbeStatsSoamPmExtSumOfSqAbsRTJitter"),
        ("CM-SA-MIB", "f3EsaProbeStatsSoamPmExtMaxP2RFDR"),
        ("CM-SA-MIB", "f3EsaProbeStatsSoamPmExtAvgP2RFDR"),
        ("CM-SA-MIB", "f3EsaProbeStatsSoamPmExtNumP2RFDR"),
        ("CM-SA-MIB", "f3EsaProbeStatsSoamPmExtSumP2RFDR"),
        ("CM-SA-MIB", "f3EsaProbeStatsSoamPmExtSumOfSqP2RFDR"),
        ("CM-SA-MIB", "f3EsaProbeStatsSoamPmExtMaxR2PFDR"),
        ("CM-SA-MIB", "f3EsaProbeStatsSoamPmExtAvgR2PFDR"),
        ("CM-SA-MIB", "f3EsaProbeStatsSoamPmExtNumR2PFDR"),
        ("CM-SA-MIB", "f3EsaProbeStatsSoamPmExtSumR2PFDR"),
        ("CM-SA-MIB", "f3EsaProbeStatsSoamPmExtSumOfSqR2PFDR"),
        ("CM-SA-MIB", "f3EsaProbeStatsSoamPmExtMaxRTFDR"),
        ("CM-SA-MIB", "f3EsaProbeStatsSoamPmExtAvgRTFDR"),
        ("CM-SA-MIB", "f3EsaProbeStatsSoamPmExtNumRTFDR"),
        ("CM-SA-MIB", "f3EsaProbeStatsSoamPmExtSumRTFDR"),
        ("CM-SA-MIB", "f3EsaProbeStatsSoamPmExtSumOfSqRTFDR"),
        ("CM-SA-MIB", "f3EsaProbeStatsSoamPmExtP2rAvailableDeltaTs"),
        ("CM-SA-MIB", "f3EsaProbeStatsSoamPmExtR2pAvailableDeltaTs"),
        ("CM-SA-MIB", "f3EsaProbeStatsSoamPmExtP2rUnavailableDeltaTs"),
        ("CM-SA-MIB", "f3EsaProbeStatsSoamPmExtR2pUnavailableDeltaTs"),
        ("CM-SA-MIB", "f3EsaProbeStatsSoamPmExtElapsedTime"),
        ("CM-SA-MIB", "f3EsaProbeHistorySoamPmExtMinP2RFlr"),
        ("CM-SA-MIB", "f3EsaProbeHistorySoamPmExtMaxP2RFlr"),
        ("CM-SA-MIB", "f3EsaProbeHistorySoamPmExtAvgP2RFlr"),
        ("CM-SA-MIB", "f3EsaProbeHistorySoamPmExtMinR2PFlr"),
        ("CM-SA-MIB", "f3EsaProbeHistorySoamPmExtMaxR2PFlr"),
        ("CM-SA-MIB", "f3EsaProbeHistorySoamPmExtAvgR2PFlr"),
        ("CM-SA-MIB", "f3EsaProbeHistorySoamPmExtP2rSeverelyErroredDeltaTs"),
        ("CM-SA-MIB", "f3EsaProbeHistorySoamPmExtR2PSeverelyErroredDeltaTs"),
        ("CM-SA-MIB", "f3EsaProbeHistorySoamPmExtP2rAvailableTime"),
        ("CM-SA-MIB", "f3EsaProbeHistorySoamPmExtR2PAvailableTime"),
        ("CM-SA-MIB", "f3EsaProbeHistorySoamPmExtP2rUnavailableTime"),
        ("CM-SA-MIB", "f3EsaProbeHistorySoamPmExtR2PUnavailableTime"),
        ("CM-SA-MIB", "f3EsaProbeHistorySoamPmExtMinAbsRTJitter"),
        ("CM-SA-MIB", "f3EsaProbeHistorySoamPmExtMaxAbsRTJitter"),
        ("CM-SA-MIB", "f3EsaProbeHistorySoamPmExtAvgAbsRTJitter"),
        ("CM-SA-MIB", "f3EsaProbeHistorySoamPmExtNumAbsRTJitter"),
        ("CM-SA-MIB", "f3EsaProbeHistorySoamPmExtSumAbsRTJitter"),
        ("CM-SA-MIB", "f3EsaProbeHistorySoamPmExtSumOfSqAbsRTJitter"),
        ("CM-SA-MIB", "f3EsaProbeHistorySoamPmExtMaxP2RFDR"),
        ("CM-SA-MIB", "f3EsaProbeHistorySoamPmExtAvgP2RFDR"),
        ("CM-SA-MIB", "f3EsaProbeHistorySoamPmExtNumP2RFDR"),
        ("CM-SA-MIB", "f3EsaProbeHistorySoamPmExtSumP2RFDR"),
        ("CM-SA-MIB", "f3EsaProbeHistorySoamPmExtSumOfSqP2RFDR"),
        ("CM-SA-MIB", "f3EsaProbeHistorySoamPmExtMaxR2PFDR"),
        ("CM-SA-MIB", "f3EsaProbeHistorySoamPmExtAvgR2PFDR"),
        ("CM-SA-MIB", "f3EsaProbeHistorySoamPmExtNumR2PFDR"),
        ("CM-SA-MIB", "f3EsaProbeHistorySoamPmExtSumR2PFDR"),
        ("CM-SA-MIB", "f3EsaProbeHistorySoamPmExtSumOfSqR2PFDR"),
        ("CM-SA-MIB", "f3EsaProbeHistorySoamPmExtMaxRTFDR"),
        ("CM-SA-MIB", "f3EsaProbeHistorySoamPmExtAvgRTFDR"),
        ("CM-SA-MIB", "f3EsaProbeHistorySoamPmExtNumRTFDR"),
        ("CM-SA-MIB", "f3EsaProbeHistorySoamPmExtSumRTFDR"),
        ("CM-SA-MIB", "f3EsaProbeHistorySoamPmExtSumOfSqRTFDR"),
        ("CM-SA-MIB", "f3EsaProbeHistorySoamPmExtP2rAvailableDeltaTs"),
        ("CM-SA-MIB", "f3EsaProbeHistorySoamPmExtR2pAvailableDeltaTs"),
        ("CM-SA-MIB", "f3EsaProbeHistorySoamPmExtP2rUnavailableDeltaTs"),
        ("CM-SA-MIB", "f3EsaProbeHistorySoamPmExtR2pUnavailableDeltaTs"),
        ("CM-SA-MIB", "f3EsaProbeHistorySoamPmExtElapsedTime"))
)
if mibBuilder.loadTexts:
    cmEsaGroup.setStatus("current")

cmBertGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 3, 2, 7)
)
cmBertGroup.setObjects(
      *(("CM-SA-MIB", "bertControlIndex"),
        ("CM-SA-MIB", "bertControlSourceEntity"),
        ("CM-SA-MIB", "bertControlTestMode"),
        ("CM-SA-MIB", "bertControlDuration"),
        ("CM-SA-MIB", "bertControlStream"),
        ("CM-SA-MIB", "bertControlAction"),
        ("CM-SA-MIB", "bertControlTestStatus"),
        ("CM-SA-MIB", "bertConfigStreamIndex"),
        ("CM-SA-MIB", "bertConfigStreamName"),
        ("CM-SA-MIB", "bertConfigStreamTxPattern"),
        ("CM-SA-MIB", "bertConfigStreamErrInjectEnabled"),
        ("CM-SA-MIB", "bertConfigStreamErrInjectRate"),
        ("CM-SA-MIB", "bertConfigStreamErrInjectRateMultiplier"),
        ("CM-SA-MIB", "bertConfigStreamUserPatternLength"),
        ("CM-SA-MIB", "bertConfigStreamUserPattern"),
        ("CM-SA-MIB", "bertTestStreamIndex"),
        ("CM-SA-MIB", "bertTestStreamName"),
        ("CM-SA-MIB", "bertTestStreamTxPattern"),
        ("CM-SA-MIB", "bertTestStreamErrInjectEnabled"),
        ("CM-SA-MIB", "bertTestStreamErrInjectRate"),
        ("CM-SA-MIB", "bertTestStreamErrInjectRateMultiplier"),
        ("CM-SA-MIB", "bertTestStreamUserPatternLength"),
        ("CM-SA-MIB", "bertTestStreamUserPattern"),
        ("CM-SA-MIB", "bertTestStreamMonStartTime"),
        ("CM-SA-MIB", "bertTestStreamMonEndTime"),
        ("CM-SA-MIB", "bertTestStreamMonElapsedTime"),
        ("CM-SA-MIB", "bertTestStreamMonSyncState"),
        ("CM-SA-MIB", "bertTestStreamMonRxPattern"),
        ("CM-SA-MIB", "bertTestStreamMonSyncCounts"),
        ("CM-SA-MIB", "bertTestStreamMonRxBitErrsSinceStart"),
        ("CM-SA-MIB", "bertTestStreamMonRxBitsSinceStart"),
        ("CM-SA-MIB", "bertTestStreamMonRxESsSinceStart"),
        ("CM-SA-MIB", "bertTestStreamMonRxErrRateSinceStart"),
        ("CM-SA-MIB", "bertTestStreamMonRxErrRateMultiplierSinceStart"),
        ("CM-SA-MIB", "bertTestStreamMonRxBitErrsSinceLastSync"),
        ("CM-SA-MIB", "bertTestStreamMonRxBitsSinceLastSync"),
        ("CM-SA-MIB", "bertTestStreamMonRxESsSinceLastSync"),
        ("CM-SA-MIB", "bertTestStreamMonRxErrRateSinceLastSync"),
        ("CM-SA-MIB", "bertTestStreamMonRxErrRateMultiplierSinceLastSync"),
        ("CM-SA-MIB", "bertTestStreamConfigChangedFlag"),
        ("CM-SA-MIB", "bertTestStreamMonOOSSsSinceStart"))
)
if mibBuilder.loadTexts:
    cmBertGroup.setStatus("current")


# Notification objects

cmOperateLoopbackTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 2, 1)
)
if mibBuilder.loadTexts:
    cmOperateLoopbackTrap.setStatus(
        "current"
    )

cmReleaseLoopbackTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 2, 2)
)
if mibBuilder.loadTexts:
    cmReleaseLoopbackTrap.setStatus(
        "current"
    )

esaProbeThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 2, 3)
)
esaProbeThresholdCrossingAlert.setObjects(
      *(("CM-SA-MIB", "esaProbeStatsThresholdIndex"),
        ("CM-SA-MIB", "esaProbeStatsThresholdVariable"),
        ("CM-SA-MIB", "esaProbeStatsThresholdAbsValueLo"),
        ("CM-SA-MIB", "esaProbeStatsThresholdAbsValueHi"),
        ("CM-SA-MIB", "esaProbeStatsThresholdMonValue"))
)
if mibBuilder.loadTexts:
    esaProbeThresholdCrossingAlert.setStatus(
        "current"
    )


# Notifications groups

cmServAssuranceNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 3, 2, 2)
)
cmServAssuranceNotifGroup.setObjects(
      *(("CM-SA-MIB", "cmOperateLoopbackTrap"),
        ("CM-SA-MIB", "cmReleaseLoopbackTrap"),
        ("CM-SA-MIB", "esaProbeThresholdCrossingAlert"))
)
if mibBuilder.loadTexts:
    cmServAssuranceNotifGroup.setStatus(
        "deprecated"
    )

cmServAssuranceGenNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 3, 2, 5)
)
cmServAssuranceGenNotifGroup.setObjects(
      *(("CM-SA-MIB", "cmOperateLoopbackTrap"),
        ("CM-SA-MIB", "cmReleaseLoopbackTrap"))
)
if mibBuilder.loadTexts:
    cmServAssuranceGenNotifGroup.setStatus(
        "current"
    )

cmServAssuranceEsaNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 3, 2, 6)
)
cmServAssuranceEsaNotifGroup.setObjects(
    ("CM-SA-MIB", "esaProbeThresholdCrossingAlert")
)
if mibBuilder.loadTexts:
    cmServAssuranceEsaNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cmServAssuranceCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 8, 3, 1, 1)
)
cmServAssuranceCompliance.setObjects(
      *(("CM-SA-MIB", "cmServAssuranceObjectGroup"),
        ("CM-SA-MIB", "cmServAssuranceNotifGroup"),
        ("CM-SA-MIB", "cmEcpaGroup"),
        ("CM-SA-MIB", "cmEsaGroup"),
        ("CM-SA-MIB", "cmServAssuranceGenNotifGroup"),
        ("CM-SA-MIB", "cmServAssuranceEsaNotifGroup"))
)
if mibBuilder.loadTexts:
    cmServAssuranceCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CM-SA-MIB",
    **{"EcpaTestStatus": EcpaTestStatus,
       "EcpaPayloadType": EcpaPayloadType,
       "EcpaTestType": EcpaTestType,
       "EcpaType": EcpaType,
       "EcpaMonitorPortType": EcpaMonitorPortType,
       "EcpaControlAction": EcpaControlAction,
       "EsaProbeProtocol": EsaProbeProtocol,
       "EsaProbeDirection": EsaProbeDirection,
       "EsaReflectorDirection": EsaReflectorDirection,
       "EsaProbePmIntervalType": EsaProbePmIntervalType,
       "EsaProbeHistoryIntervalType": EsaProbeHistoryIntervalType,
       "EsaProbeDistStatsType": EsaProbeDistStatsType,
       "EsaAction": EsaAction,
       "EsaProbePktIntervalType": EsaProbePktIntervalType,
       "EsaProbeSLAMonitorType": EsaProbeSLAMonitorType,
       "BerTestStatus": BerTestStatus,
       "BerTestMode": BerTestMode,
       "BertControlAction": BertControlAction,
       "BertPattern": BertPattern,
       "BertUserPatternLength": BertUserPatternLength,
       "BertSyncState": BertSyncState,
       "cmServiceAssuranceMIB": cmServiceAssuranceMIB,
       "cmServAssuranceObjects": cmServAssuranceObjects,
       "ecpaControlTable": ecpaControlTable,
       "ecpaControlEntry": ecpaControlEntry,
       "ecpaControlIndex": ecpaControlIndex,
       "ecpaControlSourcePort": ecpaControlSourcePort,
       "ecpaControlTestType": ecpaControlTestType,
       "ecpaControlNumFrames": ecpaControlNumFrames,
       "ecpaControlDuration": ecpaControlDuration,
       "ecpaControlInjectorDirection": ecpaControlInjectorDirection,
       "ecpaControlMonitorDirection": ecpaControlMonitorDirection,
       "ecpaControlStream1": ecpaControlStream1,
       "ecpaControlStream2": ecpaControlStream2,
       "ecpaControlStream3": ecpaControlStream3,
       "ecpaControlAction": ecpaControlAction,
       "ecpaControlTestStatus": ecpaControlTestStatus,
       "ecpaControlStorageType": ecpaControlStorageType,
       "ecpaControlRowStatus": ecpaControlRowStatus,
       "ecpaControlEcpaType": ecpaControlEcpaType,
       "ecpaControlMonitorPortType": ecpaControlMonitorPortType,
       "ecpaConfigStreamTable": ecpaConfigStreamTable,
       "ecpaConfigStreamEntry": ecpaConfigStreamEntry,
       "ecpaConfigStreamIndex": ecpaConfigStreamIndex,
       "ecpaConfigStreamName": ecpaConfigStreamName,
       "ecpaConfigStreamFrameSize": ecpaConfigStreamFrameSize,
       "ecpaConfigStreamRate": ecpaConfigStreamRate,
       "ecpaConfigStreamPayloadType": ecpaConfigStreamPayloadType,
       "ecpaConfigStreamSignature": ecpaConfigStreamSignature,
       "ecpaConfigStreamDestinationMAC": ecpaConfigStreamDestinationMAC,
       "ecpaConfigStreamSourceMAC": ecpaConfigStreamSourceMAC,
       "ecpaConfigStreamOuterVlanEnabled": ecpaConfigStreamOuterVlanEnabled,
       "ecpaConfigStreamOuterVlanId": ecpaConfigStreamOuterVlanId,
       "ecpaConfigStreamOuterVlanPrio": ecpaConfigStreamOuterVlanPrio,
       "ecpaConfigStreamOuterVlanEtherType": ecpaConfigStreamOuterVlanEtherType,
       "ecpaConfigStreamInnerVlanEnabled": ecpaConfigStreamInnerVlanEnabled,
       "ecpaConfigStreamInnerVlanId": ecpaConfigStreamInnerVlanId,
       "ecpaConfigStreamInnerVlanPrio": ecpaConfigStreamInnerVlanPrio,
       "ecpaConfigStreamInnerVlanEtherType": ecpaConfigStreamInnerVlanEtherType,
       "ecpaConfigStreamIpVersion": ecpaConfigStreamIpVersion,
       "ecpaConfigStreamIpV4Address": ecpaConfigStreamIpV4Address,
       "ecpaConfigStreamIpV6Address": ecpaConfigStreamIpV6Address,
       "ecpaConfigStreamPrioMapMode": ecpaConfigStreamPrioMapMode,
       "ecpaConfigStreamPrioVal": ecpaConfigStreamPrioVal,
       "ecpaConfigStreamInnerVlan2Enabled": ecpaConfigStreamInnerVlan2Enabled,
       "ecpaConfigStreamInnerVlan2Id": ecpaConfigStreamInnerVlan2Id,
       "ecpaConfigStreamInnerVlan2Prio": ecpaConfigStreamInnerVlan2Prio,
       "ecpaConfigStreamInnerVlan2EtherType": ecpaConfigStreamInnerVlan2EtherType,
       "ecpaConfigStreamDestIpV4Address": ecpaConfigStreamDestIpV4Address,
       "ecpaConfigStreamDestIpV6Address": ecpaConfigStreamDestIpV6Address,
       "ecpaConfigStreamUsePortSourceMAC": ecpaConfigStreamUsePortSourceMAC,
       "ecpaConfigStreamRateHi": ecpaConfigStreamRateHi,
       "ecpaConfigStreamUdpControl": ecpaConfigStreamUdpControl,
       "ecpaConfigStreamUdpSrcPort": ecpaConfigStreamUdpSrcPort,
       "ecpaConfigStreamUdpDstPort": ecpaConfigStreamUdpDstPort,
       "ecpaTestStreamTable": ecpaTestStreamTable,
       "ecpaTestStreamEntry": ecpaTestStreamEntry,
       "ecpaTestStreamIndex": ecpaTestStreamIndex,
       "ecpaTestStreamSourcePort": ecpaTestStreamSourcePort,
       "ecpaTestStreamName": ecpaTestStreamName,
       "ecpaTestStreamFrameSize": ecpaTestStreamFrameSize,
       "ecpaTestStreamRate": ecpaTestStreamRate,
       "ecpaTestStreamPayloadType": ecpaTestStreamPayloadType,
       "ecpaTestStreamSignature": ecpaTestStreamSignature,
       "ecpaTestStreamDestinationMAC": ecpaTestStreamDestinationMAC,
       "ecpaTestStreamSourceMAC": ecpaTestStreamSourceMAC,
       "ecpaTestStreamOuterVlanEnabled": ecpaTestStreamOuterVlanEnabled,
       "ecpaTestStreamOuterVlanId": ecpaTestStreamOuterVlanId,
       "ecpaTestStreamOuterVlanPrio": ecpaTestStreamOuterVlanPrio,
       "ecpaTestStreamOuterVlanEtherType": ecpaTestStreamOuterVlanEtherType,
       "ecpaTestStreamInnerVlanEnabled": ecpaTestStreamInnerVlanEnabled,
       "ecpaTestStreamInnerVlanId": ecpaTestStreamInnerVlanId,
       "ecpaTestStreamInnerVlanPrio": ecpaTestStreamInnerVlanPrio,
       "ecpaTestStreamInnerVlanEtherType": ecpaTestStreamInnerVlanEtherType,
       "ecpaTestStreamIpVersion": ecpaTestStreamIpVersion,
       "ecpaTestStreamIpV4Address": ecpaTestStreamIpV4Address,
       "ecpaTestStreamIpV6Address": ecpaTestStreamIpV6Address,
       "ecpaTestStreamPrioMapMode": ecpaTestStreamPrioMapMode,
       "ecpaTestStreamPrioVal": ecpaTestStreamPrioVal,
       "ecpaTestStreamMonStartTime": ecpaTestStreamMonStartTime,
       "ecpaTestStreamMonEndTime": ecpaTestStreamMonEndTime,
       "ecpaTestStreamMonElapsedTime": ecpaTestStreamMonElapsedTime,
       "ecpaTestStreamMonTxFrames": ecpaTestStreamMonTxFrames,
       "ecpaTestStreamMonRxFrames": ecpaTestStreamMonRxFrames,
       "ecpaTestStreamMonRxPercentSuccess": ecpaTestStreamMonRxPercentSuccess,
       "ecpaTestStreamMonRxOutOfSeqErrs": ecpaTestStreamMonRxOutOfSeqErrs,
       "ecpaTestStreamMonRxSeqGaps": ecpaTestStreamMonRxSeqGaps,
       "ecpaTestStreamMonRxNonEcpaFrames": ecpaTestStreamMonRxNonEcpaFrames,
       "ecpaTestStreamMonRxMinDelay": ecpaTestStreamMonRxMinDelay,
       "ecpaTestStreamMonRxMaxDelay": ecpaTestStreamMonRxMaxDelay,
       "ecpaTestStreamMonRxAvgDelay": ecpaTestStreamMonRxAvgDelay,
       "ecpaTestStreamMonRx1stFrameSize": ecpaTestStreamMonRx1stFrameSize,
       "ecpaTestStreamMonRx1stFrame1Octets": ecpaTestStreamMonRx1stFrame1Octets,
       "ecpaTestStreamMonRx1stFrame2Octets": ecpaTestStreamMonRx1stFrame2Octets,
       "ecpaTestStreamMonRx1stFrame3Octets": ecpaTestStreamMonRx1stFrame3Octets,
       "ecpaTestStreamMonRx1stFrame4Octets": ecpaTestStreamMonRx1stFrame4Octets,
       "ecpaTestStreamMonRx1stFrame5Octets": ecpaTestStreamMonRx1stFrame5Octets,
       "ecpaTestStreamMonRx1stFrame6Octets": ecpaTestStreamMonRx1stFrame6Octets,
       "ecpaTestStreamMonRx1stFrame7Octets": ecpaTestStreamMonRx1stFrame7Octets,
       "ecpaTestStreamMonRx1stFrame8Octets": ecpaTestStreamMonRx1stFrame8Octets,
       "ecpaTestStreamMonRx1stFrame9Octets": ecpaTestStreamMonRx1stFrame9Octets,
       "ecpaTestStreamMonRx1stFrame10Octets": ecpaTestStreamMonRx1stFrame10Octets,
       "ecpaTestStreamMonRxBitRate": ecpaTestStreamMonRxBitRate,
       "ecpaTestStreamInnerVlan2Enabled": ecpaTestStreamInnerVlan2Enabled,
       "ecpaTestStreamInnerVlan2Id": ecpaTestStreamInnerVlan2Id,
       "ecpaTestStreamInnerVlan2Prio": ecpaTestStreamInnerVlan2Prio,
       "ecpaTestStreamInnerVlan2EtherType": ecpaTestStreamInnerVlan2EtherType,
       "ecpaTestStreamDestIpV4Address": ecpaTestStreamDestIpV4Address,
       "ecpaTestStreamDestIpV6Address": ecpaTestStreamDestIpV6Address,
       "ecpaTestStreamConfigChanged": ecpaTestStreamConfigChanged,
       "ecpaTestStreamRateHi": ecpaTestStreamRateHi,
       "ecpaTestStreamUdpControl": ecpaTestStreamUdpControl,
       "ecpaTestStreamUdpSrcPort": ecpaTestStreamUdpSrcPort,
       "ecpaTestStreamUdpDstPort": ecpaTestStreamUdpDstPort,
       "esaProbeTable": esaProbeTable,
       "esaProbeEntry": esaProbeEntry,
       "esaProbeIndex": esaProbeIndex,
       "esaProbeName": esaProbeName,
       "esaProbeSourcePort": esaProbeSourcePort,
       "esaProbeAssocSchedGroup": esaProbeAssocSchedGroup,
       "esaProbeDirection": esaProbeDirection,
       "esaProbeProtocol": esaProbeProtocol,
       "esaProbeSrcIpAddress": esaProbeSrcIpAddress,
       "esaProbeSrcSubnetMask": esaProbeSrcSubnetMask,
       "esaProbeDestIpAddress": esaProbeDestIpAddress,
       "esaProbeSrcMep": esaProbeSrcMep,
       "esaProbeDestMepType": esaProbeDestMepType,
       "esaProbeDestMepMacAddr": esaProbeDestMepMacAddr,
       "esaProbeDestMepId": esaProbeDestMepId,
       "esaProbeVlanTagEnabled": esaProbeVlanTagEnabled,
       "esaProbeVlanTagEtherType": esaProbeVlanTagEtherType,
       "esaProbeVlanId": esaProbeVlanId,
       "esaProbeVlanPrio": esaProbeVlanPrio,
       "esaProbeInnerVlanTagEnabled": esaProbeInnerVlanTagEnabled,
       "esaProbeInnerVlanTagEtherType": esaProbeInnerVlanTagEtherType,
       "esaProbeInnerVlanId": esaProbeInnerVlanId,
       "esaProbeInnerVlanPrio": esaProbeInnerVlanPrio,
       "esaProbeIpPrioMapMode": esaProbeIpPrioMapMode,
       "esaProbeIpPriority": esaProbeIpPriority,
       "esaProbePktsPerSample": esaProbePktsPerSample,
       "esaProbePktSize": esaProbePktSize,
       "esaProbeInterPktGap": esaProbeInterPktGap,
       "esaProbePktDeadInterval": esaProbePktDeadInterval,
       "esaProbeResponseTimeout": esaProbeResponseTimeout,
       "esaProbeY1731DmmPktSize": esaProbeY1731DmmPktSize,
       "esaProbeY1731LmmInterval": esaProbeY1731LmmInterval,
       "esaProbeY1731DmmInterval": esaProbeY1731DmmInterval,
       "esaProbeHistoryBins": esaProbeHistoryBins,
       "esaProbeHistoryInterval": esaProbeHistoryInterval,
       "esaProbeDistHistoryBins": esaProbeDistHistoryBins,
       "esaProbeDistHistoryInterval": esaProbeDistHistoryInterval,
       "esaProbeCreationTime": esaProbeCreationTime,
       "esaProbeStorageType": esaProbeStorageType,
       "esaProbeRowStatus": esaProbeRowStatus,
       "esaProbeMultiCOSEnabled": esaProbeMultiCOSEnabled,
       "esaProbeSLAMonitorType": esaProbeSLAMonitorType,
       "esaProbeCOSType": esaProbeCOSType,
       "esaProbeSLMMulticastMACEnabled": esaProbeSLMMulticastMACEnabled,
       "esaProbeSOAMInterval": esaProbeSOAMInterval,
       "esaProbeSOAMPktSize": esaProbeSOAMPktSize,
       "esaProbeInner2VlanTagEnabled": esaProbeInner2VlanTagEnabled,
       "esaProbeInner2VlanTagEtherType": esaProbeInner2VlanTagEtherType,
       "esaProbeInner2VlanId": esaProbeInner2VlanId,
       "esaProbeInner2VlanPrio": esaProbeInner2VlanPrio,
       "esaProbeAdminState": esaProbeAdminState,
       "esaProbeOperationalState": esaProbeOperationalState,
       "esaProbeSecondaryState": esaProbeSecondaryState,
       "esaProbeMacAddress": esaProbeMacAddress,
       "esaProbeAlias": esaProbeAlias,
       "esaProbeScheduleGroupTable": esaProbeScheduleGroupTable,
       "esaProbeScheduleGroupEntry": esaProbeScheduleGroupEntry,
       "esaProbeScheduleGroupIndex": esaProbeScheduleGroupIndex,
       "esaProbeScheduleGroupDescr": esaProbeScheduleGroupDescr,
       "esaProbeScheduleGroupProbeList": esaProbeScheduleGroupProbeList,
       "esaProbeScheduleGroupType": esaProbeScheduleGroupType,
       "esaProbeScheduleGroupStartTime": esaProbeScheduleGroupStartTime,
       "esaProbeScheduleGroupDuration": esaProbeScheduleGroupDuration,
       "esaProbeScheduleGroupInterval": esaProbeScheduleGroupInterval,
       "esaProbeScheduleGroupAction": esaProbeScheduleGroupAction,
       "esaProbeScheduleGroupStatus": esaProbeScheduleGroupStatus,
       "esaProbeScheduleGroupStorageType": esaProbeScheduleGroupStorageType,
       "esaProbeScheduleGroupRowStatus": esaProbeScheduleGroupRowStatus,
       "esaProbeScheduleGroupActionProbeList": esaProbeScheduleGroupActionProbeList,
       "esaReflectorTable": esaReflectorTable,
       "esaReflectorEntry": esaReflectorEntry,
       "esaReflectorIndex": esaReflectorIndex,
       "esaReflectorName": esaReflectorName,
       "esaReflectorIpAddress": esaReflectorIpAddress,
       "esaReflectorSubnetMask": esaReflectorSubnetMask,
       "esaReflectorSourcePort": esaReflectorSourcePort,
       "esaReflectorIpPrioMapMode": esaReflectorIpPrioMapMode,
       "esaReflectorIpPriority": esaReflectorIpPriority,
       "esaReflectorAction": esaReflectorAction,
       "esaReflectorSuspended": esaReflectorSuspended,
       "esaReflectorCreationTime": esaReflectorCreationTime,
       "esaReflectorStorageType": esaReflectorStorageType,
       "esaReflectorRowStatus": esaReflectorRowStatus,
       "esaReflectorDirection": esaReflectorDirection,
       "esaReflectorAdminState": esaReflectorAdminState,
       "esaReflectorOperationalState": esaReflectorOperationalState,
       "esaReflectorSecondaryState": esaReflectorSecondaryState,
       "esaReflectorMacAddress": esaReflectorMacAddress,
       "esaReflectorAlias": esaReflectorAlias,
       "esaProbeStatsTable": esaProbeStatsTable,
       "esaProbeStatsEntry": esaProbeStatsEntry,
       "esaProbeStatsDestinationIndex": esaProbeStatsDestinationIndex,
       "esaProbeStatsCOSIndex": esaProbeStatsCOSIndex,
       "esaProbeStatsIndex": esaProbeStatsIndex,
       "esaProbeStatsIntervalType": esaProbeStatsIntervalType,
       "esaProbeStatsCOS": esaProbeStatsCOS,
       "esaProbeStatsValid": esaProbeStatsValid,
       "esaProbeStatsAction": esaProbeStatsAction,
       "esaProbeStatsP2RPkts": esaProbeStatsP2RPkts,
       "esaProbeStatsP2RErredPkts": esaProbeStatsP2RErredPkts,
       "esaProbeStatsP2RSyncErrs": esaProbeStatsP2RSyncErrs,
       "esaProbeStatsP2RLostPkts": esaProbeStatsP2RLostPkts,
       "esaProbeStatsR2PPkts": esaProbeStatsR2PPkts,
       "esaProbeStatsR2PErredPkts": esaProbeStatsR2PErredPkts,
       "esaProbeStatsR2PSyncErrs": esaProbeStatsR2PSyncErrs,
       "esaProbeStatsR2PLostPkts": esaProbeStatsR2PLostPkts,
       "esaProbeStatsLostPkts": esaProbeStatsLostPkts,
       "esaProbeStatsSeqGaps": esaProbeStatsSeqGaps,
       "esaProbeStatsOutOfSeqErrs": esaProbeStatsOutOfSeqErrs,
       "esaProbeStatsMinRoundTripDelay": esaProbeStatsMinRoundTripDelay,
       "esaProbeStatsMaxRoundTripDelay": esaProbeStatsMaxRoundTripDelay,
       "esaProbeStatsAvgRoundTripDelay": esaProbeStatsAvgRoundTripDelay,
       "esaProbeStatsSumRoundTripDelay": esaProbeStatsSumRoundTripDelay,
       "esaProbeStatsSumOfSqRoundTripDelay": esaProbeStatsSumOfSqRoundTripDelay,
       "esaProbeStatsMinOnewayP2RDelay": esaProbeStatsMinOnewayP2RDelay,
       "esaProbeStatsMaxOnewayP2RDelay": esaProbeStatsMaxOnewayP2RDelay,
       "esaProbeStatsAvgOnewayP2RDelay": esaProbeStatsAvgOnewayP2RDelay,
       "esaProbeStatsSumOnewayP2RDelay": esaProbeStatsSumOnewayP2RDelay,
       "esaProbeStatsSumOfSqOnewayP2RDelay": esaProbeStatsSumOfSqOnewayP2RDelay,
       "esaProbeStatsMinOnewayR2PDelay": esaProbeStatsMinOnewayR2PDelay,
       "esaProbeStatsMaxOnewayR2PDelay": esaProbeStatsMaxOnewayR2PDelay,
       "esaProbeStatsAvgOnewayR2PDelay": esaProbeStatsAvgOnewayR2PDelay,
       "esaProbeStatsSumOnewayR2PDelay": esaProbeStatsSumOnewayR2PDelay,
       "esaProbeStatsSumOfSqOnewayR2PDelay": esaProbeStatsSumOfSqOnewayR2PDelay,
       "esaProbeStatsMinPosP2RJitter": esaProbeStatsMinPosP2RJitter,
       "esaProbeStatsMaxPosP2RJitter": esaProbeStatsMaxPosP2RJitter,
       "esaProbeStatsNumPosP2RJitter": esaProbeStatsNumPosP2RJitter,
       "esaProbeStatsSumPosP2RJitter": esaProbeStatsSumPosP2RJitter,
       "esaProbeStatsSumOfSqPosP2RJitter": esaProbeStatsSumOfSqPosP2RJitter,
       "esaProbeStatsMinNegP2RJitter": esaProbeStatsMinNegP2RJitter,
       "esaProbeStatsMaxNegP2RJitter": esaProbeStatsMaxNegP2RJitter,
       "esaProbeStatsNumNegP2RJitter": esaProbeStatsNumNegP2RJitter,
       "esaProbeStatsSumNegP2RJitter": esaProbeStatsSumNegP2RJitter,
       "esaProbeStatsSumOfSqNegP2RJitter": esaProbeStatsSumOfSqNegP2RJitter,
       "esaProbeStatsMinPosR2PJitter": esaProbeStatsMinPosR2PJitter,
       "esaProbeStatsMaxPosR2PJitter": esaProbeStatsMaxPosR2PJitter,
       "esaProbeStatsNumPosR2PJitter": esaProbeStatsNumPosR2PJitter,
       "esaProbeStatsSumPosR2PJitter": esaProbeStatsSumPosR2PJitter,
       "esaProbeStatsSumOfSqPosR2PJitter": esaProbeStatsSumOfSqPosR2PJitter,
       "esaProbeStatsMinNegR2PJitter": esaProbeStatsMinNegR2PJitter,
       "esaProbeStatsMaxNegR2PJitter": esaProbeStatsMaxNegR2PJitter,
       "esaProbeStatsNumNegR2PJitter": esaProbeStatsNumNegR2PJitter,
       "esaProbeStatsSumNegR2PJitter": esaProbeStatsSumNegR2PJitter,
       "esaProbeStatsSumOfSqNegR2PJitter": esaProbeStatsSumOfSqNegR2PJitter,
       "esaProbeStatsY1731P2RNegLossOccurrences": esaProbeStatsY1731P2RNegLossOccurrences,
       "esaProbeStatsY1731R2PNegLossOccurrences": esaProbeStatsY1731R2PNegLossOccurrences,
       "esaProbeStatsY1731RxLmSamples": esaProbeStatsY1731RxLmSamples,
       "esaProbeStatsY1731RxDmSamples": esaProbeStatsY1731RxDmSamples,
       "esaProbeStatsY1731P2RFrames": esaProbeStatsY1731P2RFrames,
       "esaProbeStatsY1731R2PFrames": esaProbeStatsY1731R2PFrames,
       "esaProbeStatsAvgAbsP2RJitter": esaProbeStatsAvgAbsP2RJitter,
       "esaProbeStatsAvgAbsR2PJitter": esaProbeStatsAvgAbsR2PJitter,
       "esaProbeStatsMinAbsP2RJitter": esaProbeStatsMinAbsP2RJitter,
       "esaProbeStatsMinAbsR2PJitter": esaProbeStatsMinAbsR2PJitter,
       "esaProbeStatsMaxAbsP2RJitter": esaProbeStatsMaxAbsP2RJitter,
       "esaProbeStatsMaxAbsR2PJitter": esaProbeStatsMaxAbsR2PJitter,
       "esaProbeStatsNumAbsP2RJitter": esaProbeStatsNumAbsP2RJitter,
       "esaProbeStatsNumAbsR2PJitter": esaProbeStatsNumAbsR2PJitter,
       "esaProbeStatsSumAbsP2RJitter": esaProbeStatsSumAbsP2RJitter,
       "esaProbeStatsSumAbsR2PJitter": esaProbeStatsSumAbsR2PJitter,
       "esaProbeStatsSumOfSqAbsP2RJitter": esaProbeStatsSumOfSqAbsP2RJitter,
       "esaProbeStatsSumOfSqAbsR2PJitter": esaProbeStatsSumOfSqAbsR2PJitter,
       "esaProbeHistoryTable": esaProbeHistoryTable,
       "esaProbeHistoryEntry": esaProbeHistoryEntry,
       "esaProbeHistoryDestinationIndex": esaProbeHistoryDestinationIndex,
       "esaProbeHistoryCOSIndex": esaProbeHistoryCOSIndex,
       "esaProbeHistoryIndex": esaProbeHistoryIndex,
       "esaProbeHistoryTime": esaProbeHistoryTime,
       "esaProbeHistoryValid": esaProbeHistoryValid,
       "esaProbeHistoryAction": esaProbeHistoryAction,
       "esaProbeHistoryCOS": esaProbeHistoryCOS,
       "esaProbeHistoryP2RPkts": esaProbeHistoryP2RPkts,
       "esaProbeHistoryP2RErredPkts": esaProbeHistoryP2RErredPkts,
       "esaProbeHistoryP2RSyncErrs": esaProbeHistoryP2RSyncErrs,
       "esaProbeHistoryP2RLostPkts": esaProbeHistoryP2RLostPkts,
       "esaProbeHistoryR2PPkts": esaProbeHistoryR2PPkts,
       "esaProbeHistoryR2PErredPkts": esaProbeHistoryR2PErredPkts,
       "esaProbeHistoryR2PSyncErrs": esaProbeHistoryR2PSyncErrs,
       "esaProbeHistoryR2PLostPkts": esaProbeHistoryR2PLostPkts,
       "esaProbeHistoryLostPkts": esaProbeHistoryLostPkts,
       "esaProbeHistorySeqGaps": esaProbeHistorySeqGaps,
       "esaProbeHistoryOutOfSeqErrs": esaProbeHistoryOutOfSeqErrs,
       "esaProbeHistoryMinRoundTripDelay": esaProbeHistoryMinRoundTripDelay,
       "esaProbeHistoryMaxRoundTripDelay": esaProbeHistoryMaxRoundTripDelay,
       "esaProbeHistoryAvgRoundTripDelay": esaProbeHistoryAvgRoundTripDelay,
       "esaProbeHistorySumRoundTripDelay": esaProbeHistorySumRoundTripDelay,
       "esaProbeHistorySumOfSqRoundTripDelay": esaProbeHistorySumOfSqRoundTripDelay,
       "esaProbeHistoryMinOnewayP2RDelay": esaProbeHistoryMinOnewayP2RDelay,
       "esaProbeHistoryMaxOnewayP2RDelay": esaProbeHistoryMaxOnewayP2RDelay,
       "esaProbeHistoryAvgOnewayP2RDelay": esaProbeHistoryAvgOnewayP2RDelay,
       "esaProbeHistorySumOnewayP2RDelay": esaProbeHistorySumOnewayP2RDelay,
       "esaProbeHistorySumOfSqOnewayP2RDelay": esaProbeHistorySumOfSqOnewayP2RDelay,
       "esaProbeHistoryMinOnewayR2PDelay": esaProbeHistoryMinOnewayR2PDelay,
       "esaProbeHistoryMaxOnewayR2PDelay": esaProbeHistoryMaxOnewayR2PDelay,
       "esaProbeHistoryAvgOnewayR2PDelay": esaProbeHistoryAvgOnewayR2PDelay,
       "esaProbeHistorySumOnewayR2PDelay": esaProbeHistorySumOnewayR2PDelay,
       "esaProbeHistorySumOfSqOnewayR2PDelay": esaProbeHistorySumOfSqOnewayR2PDelay,
       "esaProbeHistoryMinPosP2RJitter": esaProbeHistoryMinPosP2RJitter,
       "esaProbeHistoryMaxPosP2RJitter": esaProbeHistoryMaxPosP2RJitter,
       "esaProbeHistoryNumPosP2RJitter": esaProbeHistoryNumPosP2RJitter,
       "esaProbeHistorySumPosP2RJitter": esaProbeHistorySumPosP2RJitter,
       "esaProbeHistorySumOfSqPosP2RJitter": esaProbeHistorySumOfSqPosP2RJitter,
       "esaProbeHistoryMinNegP2RJitter": esaProbeHistoryMinNegP2RJitter,
       "esaProbeHistoryMaxNegP2RJitter": esaProbeHistoryMaxNegP2RJitter,
       "esaProbeHistoryNumNegP2RJitter": esaProbeHistoryNumNegP2RJitter,
       "esaProbeHistorySumNegP2RJitter": esaProbeHistorySumNegP2RJitter,
       "esaProbeHistorySumOfSqNegP2RJitter": esaProbeHistorySumOfSqNegP2RJitter,
       "esaProbeHistoryMinPosR2PJitter": esaProbeHistoryMinPosR2PJitter,
       "esaProbeHistoryMaxPosR2PJitter": esaProbeHistoryMaxPosR2PJitter,
       "esaProbeHistoryNumPosR2PJitter": esaProbeHistoryNumPosR2PJitter,
       "esaProbeHistorySumPosR2PJitter": esaProbeHistorySumPosR2PJitter,
       "esaProbeHistorySumOfSqPosR2PJitter": esaProbeHistorySumOfSqPosR2PJitter,
       "esaProbeHistoryMinNegR2PJitter": esaProbeHistoryMinNegR2PJitter,
       "esaProbeHistoryMaxNegR2PJitter": esaProbeHistoryMaxNegR2PJitter,
       "esaProbeHistoryNumNegR2PJitter": esaProbeHistoryNumNegR2PJitter,
       "esaProbeHistorySumNegR2PJitter": esaProbeHistorySumNegR2PJitter,
       "esaProbeHistorySumOfSqNegR2PJitter": esaProbeHistorySumOfSqNegR2PJitter,
       "esaProbeHistoryY1731P2RNegLossOccurrences": esaProbeHistoryY1731P2RNegLossOccurrences,
       "esaProbeHistoryY1731R2PNegLossOccurrences": esaProbeHistoryY1731R2PNegLossOccurrences,
       "esaProbeHistoryY1731RxLmSamples": esaProbeHistoryY1731RxLmSamples,
       "esaProbeHistoryY1731RxDmSamples": esaProbeHistoryY1731RxDmSamples,
       "esaProbeHistoryY1731P2RFrames": esaProbeHistoryY1731P2RFrames,
       "esaProbeHistoryY1731R2PFrames": esaProbeHistoryY1731R2PFrames,
       "esaProbeHistoryAvgAbsP2RJitter": esaProbeHistoryAvgAbsP2RJitter,
       "esaProbeHistoryAvgAbsR2PJitter": esaProbeHistoryAvgAbsR2PJitter,
       "esaProbeHistoryMinAbsP2RJitter": esaProbeHistoryMinAbsP2RJitter,
       "esaProbeHistoryMinAbsR2PJitter": esaProbeHistoryMinAbsR2PJitter,
       "esaProbeHistoryMaxAbsP2RJitter": esaProbeHistoryMaxAbsP2RJitter,
       "esaProbeHistoryMaxAbsR2PJitter": esaProbeHistoryMaxAbsR2PJitter,
       "esaProbeHistoryNumAbsP2RJitter": esaProbeHistoryNumAbsP2RJitter,
       "esaProbeHistoryNumAbsR2PJitter": esaProbeHistoryNumAbsR2PJitter,
       "esaProbeHistorySumAbsP2RJitter": esaProbeHistorySumAbsP2RJitter,
       "esaProbeHistorySumAbsR2PJitter": esaProbeHistorySumAbsR2PJitter,
       "esaProbeHistorySumOfSqAbsP2RJitter": esaProbeHistorySumOfSqAbsP2RJitter,
       "esaProbeHistorySumOfSqAbsR2PJitter": esaProbeHistorySumOfSqAbsR2PJitter,
       "esaProbeDistStatsConfigTable": esaProbeDistStatsConfigTable,
       "esaProbeDistStatsConfigEntry": esaProbeDistStatsConfigEntry,
       "esaProbeDistStatsConfigIndex": esaProbeDistStatsConfigIndex,
       "esaProbeDistStatsConfigType": esaProbeDistStatsConfigType,
       "esaProbeDistStatsConfigMinVal": esaProbeDistStatsConfigMinVal,
       "esaProbeDistStatsConfigMaxVal": esaProbeDistStatsConfigMaxVal,
       "esaProbeDistStatsConfigNumBins": esaProbeDistStatsConfigNumBins,
       "esaProbeDistStatsConfigLowBoundOfBin1": esaProbeDistStatsConfigLowBoundOfBin1,
       "esaProbeDistStatsConfigLowBoundOfBin2": esaProbeDistStatsConfigLowBoundOfBin2,
       "esaProbeDistStatsConfigLowBoundOfBin3": esaProbeDistStatsConfigLowBoundOfBin3,
       "esaProbeDistStatsConfigLowBoundOfBin4": esaProbeDistStatsConfigLowBoundOfBin4,
       "esaProbeDistStatsConfigLowBoundOfBin5": esaProbeDistStatsConfigLowBoundOfBin5,
       "esaProbeDistStatsConfigLowBoundOfBin6": esaProbeDistStatsConfigLowBoundOfBin6,
       "esaProbeDistStatsConfigLowBoundOfBin7": esaProbeDistStatsConfigLowBoundOfBin7,
       "esaProbeDistStatsConfigLowBoundOfBin8": esaProbeDistStatsConfigLowBoundOfBin8,
       "esaProbeDistStatsConfigLowBoundOfBin9": esaProbeDistStatsConfigLowBoundOfBin9,
       "esaProbeDistStatsTable": esaProbeDistStatsTable,
       "esaProbeDistStatsEntry": esaProbeDistStatsEntry,
       "esaProbeDistStatsDestinationIndex": esaProbeDistStatsDestinationIndex,
       "esaProbeDistStatsCOSIndex": esaProbeDistStatsCOSIndex,
       "esaProbeDistStatsAction": esaProbeDistStatsAction,
       "esaProbeDistStatsCOS": esaProbeDistStatsCOS,
       "esaProbeDistStatsNumBins": esaProbeDistStatsNumBins,
       "esaProbeDistStatsLTMin": esaProbeDistStatsLTMin,
       "esaProbeDistStatsGTMax": esaProbeDistStatsGTMax,
       "esaProbeDistStatsBinTable": esaProbeDistStatsBinTable,
       "esaProbeDistStatsBinEntry": esaProbeDistStatsBinEntry,
       "esaProbeDistStatsBinIndex": esaProbeDistStatsBinIndex,
       "esaProbeDistStatsBinLower": esaProbeDistStatsBinLower,
       "esaProbeDistStatsBinUpper": esaProbeDistStatsBinUpper,
       "esaProbeDistStatsBinNumSamples": esaProbeDistStatsBinNumSamples,
       "esaProbeDistHistoryTable": esaProbeDistHistoryTable,
       "esaProbeDistHistoryEntry": esaProbeDistHistoryEntry,
       "esaProbeDistHistoryDestinationIndex": esaProbeDistHistoryDestinationIndex,
       "esaProbeDistHistoryCOSIndex": esaProbeDistHistoryCOSIndex,
       "esaProbeDistHistoryIndex": esaProbeDistHistoryIndex,
       "esaProbeDistHistoryTime": esaProbeDistHistoryTime,
       "esaProbeDistHistoryAction": esaProbeDistHistoryAction,
       "esaProbeDistHistoryCOS": esaProbeDistHistoryCOS,
       "esaProbeDistHistoryNumBins": esaProbeDistHistoryNumBins,
       "esaProbeDistHistoryLTMin": esaProbeDistHistoryLTMin,
       "esaProbeDistHistoryGTMax": esaProbeDistHistoryGTMax,
       "esaProbeDistHistoryBinTable": esaProbeDistHistoryBinTable,
       "esaProbeDistHistoryBinEntry": esaProbeDistHistoryBinEntry,
       "esaProbeDistHistoryBinIndex": esaProbeDistHistoryBinIndex,
       "esaProbeDistHistoryBinLower": esaProbeDistHistoryBinLower,
       "esaProbeDistHistoryBinUpper": esaProbeDistHistoryBinUpper,
       "esaProbeDistHistoryBinNumSamples": esaProbeDistHistoryBinNumSamples,
       "esaProbeStatsThresholdTable": esaProbeStatsThresholdTable,
       "esaProbeStatsThresholdEntry": esaProbeStatsThresholdEntry,
       "esaProbeStatsThresholdIndex": esaProbeStatsThresholdIndex,
       "esaProbeStatsThresholdVariable": esaProbeStatsThresholdVariable,
       "esaProbeStatsThresholdAbsValueLo": esaProbeStatsThresholdAbsValueLo,
       "esaProbeStatsThresholdAbsValueHi": esaProbeStatsThresholdAbsValueHi,
       "esaProbeStatsThresholdMonValue": esaProbeStatsThresholdMonValue,
       "esaProbeCOSConfigTable": esaProbeCOSConfigTable,
       "esaProbeCOSConfigEntry": esaProbeCOSConfigEntry,
       "esaProbeCOSConfigIndex": esaProbeCOSConfigIndex,
       "esaProbeCOSConfigType": esaProbeCOSConfigType,
       "esaProbeCOSConfigInterval": esaProbeCOSConfigInterval,
       "esaProbeCOSConfigPktSize": esaProbeCOSConfigPktSize,
       "esaProbeCOSConfigStorageType": esaProbeCOSConfigStorageType,
       "esaProbeCOSConfigRowStatus": esaProbeCOSConfigRowStatus,
       "esaProbeCOSConfigslmInterval": esaProbeCOSConfigslmInterval,
       "esaProbeCOSConfigslmPktSize": esaProbeCOSConfigslmPktSize,
       "esaProbeCOSConfigSoamPmExtAvailFlrThreshold": esaProbeCOSConfigSoamPmExtAvailFlrThreshold,
       "esaProbeCOSConfigSoamPmExtFlrDeltaTNumLmPdus": esaProbeCOSConfigSoamPmExtFlrDeltaTNumLmPdus,
       "esaProbeCOSConfigSoamPmExtConDeltaTsForAvail": esaProbeCOSConfigSoamPmExtConDeltaTsForAvail,
       "esaProbeMultiDestinationTable": esaProbeMultiDestinationTable,
       "esaProbeMultiDestinationEntry": esaProbeMultiDestinationEntry,
       "esaProbeDestinationIndex": esaProbeDestinationIndex,
       "esaProbeDestinationMepType": esaProbeDestinationMepType,
       "esaProbeDestinationMepMacAddr": esaProbeDestinationMepMacAddr,
       "esaProbeDestinationMepId": esaProbeDestinationMepId,
       "esaProbeDestinationStorageType": esaProbeDestinationStorageType,
       "esaProbeDestinationRowStatus": esaProbeDestinationRowStatus,
       "bertControlTable": bertControlTable,
       "bertControlEntry": bertControlEntry,
       "bertControlIndex": bertControlIndex,
       "bertControlSourceEntity": bertControlSourceEntity,
       "bertControlTestMode": bertControlTestMode,
       "bertControlDuration": bertControlDuration,
       "bertControlStream": bertControlStream,
       "bertControlAction": bertControlAction,
       "bertControlTestStatus": bertControlTestStatus,
       "bertConfigStreamTable": bertConfigStreamTable,
       "bertConfigStreamEntry": bertConfigStreamEntry,
       "bertConfigStreamIndex": bertConfigStreamIndex,
       "bertConfigStreamName": bertConfigStreamName,
       "bertConfigStreamTxPattern": bertConfigStreamTxPattern,
       "bertConfigStreamErrInjectEnabled": bertConfigStreamErrInjectEnabled,
       "bertConfigStreamErrInjectRate": bertConfigStreamErrInjectRate,
       "bertConfigStreamErrInjectRateMultiplier": bertConfigStreamErrInjectRateMultiplier,
       "bertConfigStreamUserPatternLength": bertConfigStreamUserPatternLength,
       "bertConfigStreamUserPattern": bertConfigStreamUserPattern,
       "bertTestStreamTable": bertTestStreamTable,
       "bertTestStreamEntry": bertTestStreamEntry,
       "bertTestStreamIndex": bertTestStreamIndex,
       "bertTestStreamName": bertTestStreamName,
       "bertTestStreamTxPattern": bertTestStreamTxPattern,
       "bertTestStreamErrInjectEnabled": bertTestStreamErrInjectEnabled,
       "bertTestStreamErrInjectRate": bertTestStreamErrInjectRate,
       "bertTestStreamErrInjectRateMultiplier": bertTestStreamErrInjectRateMultiplier,
       "bertTestStreamUserPatternLength": bertTestStreamUserPatternLength,
       "bertTestStreamUserPattern": bertTestStreamUserPattern,
       "bertTestStreamMonStartTime": bertTestStreamMonStartTime,
       "bertTestStreamMonEndTime": bertTestStreamMonEndTime,
       "bertTestStreamMonElapsedTime": bertTestStreamMonElapsedTime,
       "bertTestStreamMonSyncState": bertTestStreamMonSyncState,
       "bertTestStreamMonRxPattern": bertTestStreamMonRxPattern,
       "bertTestStreamMonSyncCounts": bertTestStreamMonSyncCounts,
       "bertTestStreamMonRxBitErrsSinceStart": bertTestStreamMonRxBitErrsSinceStart,
       "bertTestStreamMonRxBitsSinceStart": bertTestStreamMonRxBitsSinceStart,
       "bertTestStreamMonRxESsSinceStart": bertTestStreamMonRxESsSinceStart,
       "bertTestStreamMonRxErrRateSinceStart": bertTestStreamMonRxErrRateSinceStart,
       "bertTestStreamMonRxErrRateMultiplierSinceStart": bertTestStreamMonRxErrRateMultiplierSinceStart,
       "bertTestStreamMonRxBitErrsSinceLastSync": bertTestStreamMonRxBitErrsSinceLastSync,
       "bertTestStreamMonRxBitsSinceLastSync": bertTestStreamMonRxBitsSinceLastSync,
       "bertTestStreamMonRxESsSinceLastSync": bertTestStreamMonRxESsSinceLastSync,
       "bertTestStreamMonRxErrRateSinceLastSync": bertTestStreamMonRxErrRateSinceLastSync,
       "bertTestStreamMonRxErrRateMultiplierSinceLastSync": bertTestStreamMonRxErrRateMultiplierSinceLastSync,
       "bertTestStreamConfigChangedFlag": bertTestStreamConfigChangedFlag,
       "bertTestStreamMonOOSSsSinceStart": bertTestStreamMonOOSSsSinceStart,
       "f3EsaProbeCOSConfigSoamPmExtTable": f3EsaProbeCOSConfigSoamPmExtTable,
       "f3EsaProbeCOSConfigSoamPmExtEntry": f3EsaProbeCOSConfigSoamPmExtEntry,
       "f3EsaProbeCOSConfigSoamPmExtAvailFlrThreshold": f3EsaProbeCOSConfigSoamPmExtAvailFlrThreshold,
       "f3EsaProbeCOSConfigSoamPmExtFlrDeltaTNumLmPdus": f3EsaProbeCOSConfigSoamPmExtFlrDeltaTNumLmPdus,
       "f3EsaProbeCOSConfigSoamPmExtConDeltaTsForAvail": f3EsaProbeCOSConfigSoamPmExtConDeltaTsForAvail,
       "f3EsaProbeStatsSoamPmExtTable": f3EsaProbeStatsSoamPmExtTable,
       "f3EsaProbeStatsSoamPmExtEntry": f3EsaProbeStatsSoamPmExtEntry,
       "f3EsaProbeStatsSoamPmExtMinP2RFlr": f3EsaProbeStatsSoamPmExtMinP2RFlr,
       "f3EsaProbeStatsSoamPmExtMaxP2RFlr": f3EsaProbeStatsSoamPmExtMaxP2RFlr,
       "f3EsaProbeStatsSoamPmExtAvgP2RFlr": f3EsaProbeStatsSoamPmExtAvgP2RFlr,
       "f3EsaProbeStatsSoamPmExtMinR2PFlr": f3EsaProbeStatsSoamPmExtMinR2PFlr,
       "f3EsaProbeStatsSoamPmExtMaxR2PFlr": f3EsaProbeStatsSoamPmExtMaxR2PFlr,
       "f3EsaProbeStatsSoamPmExtAvgR2PFlr": f3EsaProbeStatsSoamPmExtAvgR2PFlr,
       "f3EsaProbeStatsSoamPmExtP2rSeverelyErroredDeltaTs": f3EsaProbeStatsSoamPmExtP2rSeverelyErroredDeltaTs,
       "f3EsaProbeStatsSoamPmExtR2PSeverelyErroredDeltaTs": f3EsaProbeStatsSoamPmExtR2PSeverelyErroredDeltaTs,
       "f3EsaProbeStatsSoamPmExtP2rAvailableTime": f3EsaProbeStatsSoamPmExtP2rAvailableTime,
       "f3EsaProbeStatsSoamPmExtR2PAvailableTime": f3EsaProbeStatsSoamPmExtR2PAvailableTime,
       "f3EsaProbeStatsSoamPmExtP2rUnavailableTime": f3EsaProbeStatsSoamPmExtP2rUnavailableTime,
       "f3EsaProbeStatsSoamPmExtR2PUnavailableTime": f3EsaProbeStatsSoamPmExtR2PUnavailableTime,
       "f3EsaProbeStatsSoamPmExtMinAbsRTJitter": f3EsaProbeStatsSoamPmExtMinAbsRTJitter,
       "f3EsaProbeStatsSoamPmExtMaxAbsRTJitter": f3EsaProbeStatsSoamPmExtMaxAbsRTJitter,
       "f3EsaProbeStatsSoamPmExtAvgAbsRTJitter": f3EsaProbeStatsSoamPmExtAvgAbsRTJitter,
       "f3EsaProbeStatsSoamPmExtNumAbsRTJitter": f3EsaProbeStatsSoamPmExtNumAbsRTJitter,
       "f3EsaProbeStatsSoamPmExtSumAbsRTJitter": f3EsaProbeStatsSoamPmExtSumAbsRTJitter,
       "f3EsaProbeStatsSoamPmExtSumOfSqAbsRTJitter": f3EsaProbeStatsSoamPmExtSumOfSqAbsRTJitter,
       "f3EsaProbeStatsSoamPmExtMaxP2RFDR": f3EsaProbeStatsSoamPmExtMaxP2RFDR,
       "f3EsaProbeStatsSoamPmExtAvgP2RFDR": f3EsaProbeStatsSoamPmExtAvgP2RFDR,
       "f3EsaProbeStatsSoamPmExtNumP2RFDR": f3EsaProbeStatsSoamPmExtNumP2RFDR,
       "f3EsaProbeStatsSoamPmExtSumP2RFDR": f3EsaProbeStatsSoamPmExtSumP2RFDR,
       "f3EsaProbeStatsSoamPmExtSumOfSqP2RFDR": f3EsaProbeStatsSoamPmExtSumOfSqP2RFDR,
       "f3EsaProbeStatsSoamPmExtMaxR2PFDR": f3EsaProbeStatsSoamPmExtMaxR2PFDR,
       "f3EsaProbeStatsSoamPmExtAvgR2PFDR": f3EsaProbeStatsSoamPmExtAvgR2PFDR,
       "f3EsaProbeStatsSoamPmExtNumR2PFDR": f3EsaProbeStatsSoamPmExtNumR2PFDR,
       "f3EsaProbeStatsSoamPmExtSumR2PFDR": f3EsaProbeStatsSoamPmExtSumR2PFDR,
       "f3EsaProbeStatsSoamPmExtSumOfSqR2PFDR": f3EsaProbeStatsSoamPmExtSumOfSqR2PFDR,
       "f3EsaProbeStatsSoamPmExtMaxRTFDR": f3EsaProbeStatsSoamPmExtMaxRTFDR,
       "f3EsaProbeStatsSoamPmExtAvgRTFDR": f3EsaProbeStatsSoamPmExtAvgRTFDR,
       "f3EsaProbeStatsSoamPmExtNumRTFDR": f3EsaProbeStatsSoamPmExtNumRTFDR,
       "f3EsaProbeStatsSoamPmExtSumRTFDR": f3EsaProbeStatsSoamPmExtSumRTFDR,
       "f3EsaProbeStatsSoamPmExtSumOfSqRTFDR": f3EsaProbeStatsSoamPmExtSumOfSqRTFDR,
       "f3EsaProbeStatsSoamPmExtP2rAvailableDeltaTs": f3EsaProbeStatsSoamPmExtP2rAvailableDeltaTs,
       "f3EsaProbeStatsSoamPmExtR2pAvailableDeltaTs": f3EsaProbeStatsSoamPmExtR2pAvailableDeltaTs,
       "f3EsaProbeStatsSoamPmExtP2rUnavailableDeltaTs": f3EsaProbeStatsSoamPmExtP2rUnavailableDeltaTs,
       "f3EsaProbeStatsSoamPmExtR2pUnavailableDeltaTs": f3EsaProbeStatsSoamPmExtR2pUnavailableDeltaTs,
       "f3EsaProbeStatsSoamPmExtElapsedTime": f3EsaProbeStatsSoamPmExtElapsedTime,
       "f3EsaProbeHistorySoamPmExtTable": f3EsaProbeHistorySoamPmExtTable,
       "f3EsaProbeHistorySoamPmExtEntry": f3EsaProbeHistorySoamPmExtEntry,
       "f3EsaProbeHistorySoamPmExtMinP2RFlr": f3EsaProbeHistorySoamPmExtMinP2RFlr,
       "f3EsaProbeHistorySoamPmExtMaxP2RFlr": f3EsaProbeHistorySoamPmExtMaxP2RFlr,
       "f3EsaProbeHistorySoamPmExtAvgP2RFlr": f3EsaProbeHistorySoamPmExtAvgP2RFlr,
       "f3EsaProbeHistorySoamPmExtMinR2PFlr": f3EsaProbeHistorySoamPmExtMinR2PFlr,
       "f3EsaProbeHistorySoamPmExtMaxR2PFlr": f3EsaProbeHistorySoamPmExtMaxR2PFlr,
       "f3EsaProbeHistorySoamPmExtAvgR2PFlr": f3EsaProbeHistorySoamPmExtAvgR2PFlr,
       "f3EsaProbeHistorySoamPmExtP2rSeverelyErroredDeltaTs": f3EsaProbeHistorySoamPmExtP2rSeverelyErroredDeltaTs,
       "f3EsaProbeHistorySoamPmExtR2PSeverelyErroredDeltaTs": f3EsaProbeHistorySoamPmExtR2PSeverelyErroredDeltaTs,
       "f3EsaProbeHistorySoamPmExtP2rAvailableTime": f3EsaProbeHistorySoamPmExtP2rAvailableTime,
       "f3EsaProbeHistorySoamPmExtR2PAvailableTime": f3EsaProbeHistorySoamPmExtR2PAvailableTime,
       "f3EsaProbeHistorySoamPmExtP2rUnavailableTime": f3EsaProbeHistorySoamPmExtP2rUnavailableTime,
       "f3EsaProbeHistorySoamPmExtR2PUnavailableTime": f3EsaProbeHistorySoamPmExtR2PUnavailableTime,
       "f3EsaProbeHistorySoamPmExtMinAbsRTJitter": f3EsaProbeHistorySoamPmExtMinAbsRTJitter,
       "f3EsaProbeHistorySoamPmExtMaxAbsRTJitter": f3EsaProbeHistorySoamPmExtMaxAbsRTJitter,
       "f3EsaProbeHistorySoamPmExtAvgAbsRTJitter": f3EsaProbeHistorySoamPmExtAvgAbsRTJitter,
       "f3EsaProbeHistorySoamPmExtNumAbsRTJitter": f3EsaProbeHistorySoamPmExtNumAbsRTJitter,
       "f3EsaProbeHistorySoamPmExtSumAbsRTJitter": f3EsaProbeHistorySoamPmExtSumAbsRTJitter,
       "f3EsaProbeHistorySoamPmExtSumOfSqAbsRTJitter": f3EsaProbeHistorySoamPmExtSumOfSqAbsRTJitter,
       "f3EsaProbeHistorySoamPmExtMaxP2RFDR": f3EsaProbeHistorySoamPmExtMaxP2RFDR,
       "f3EsaProbeHistorySoamPmExtAvgP2RFDR": f3EsaProbeHistorySoamPmExtAvgP2RFDR,
       "f3EsaProbeHistorySoamPmExtNumP2RFDR": f3EsaProbeHistorySoamPmExtNumP2RFDR,
       "f3EsaProbeHistorySoamPmExtSumP2RFDR": f3EsaProbeHistorySoamPmExtSumP2RFDR,
       "f3EsaProbeHistorySoamPmExtSumOfSqP2RFDR": f3EsaProbeHistorySoamPmExtSumOfSqP2RFDR,
       "f3EsaProbeHistorySoamPmExtMaxR2PFDR": f3EsaProbeHistorySoamPmExtMaxR2PFDR,
       "f3EsaProbeHistorySoamPmExtAvgR2PFDR": f3EsaProbeHistorySoamPmExtAvgR2PFDR,
       "f3EsaProbeHistorySoamPmExtNumR2PFDR": f3EsaProbeHistorySoamPmExtNumR2PFDR,
       "f3EsaProbeHistorySoamPmExtSumR2PFDR": f3EsaProbeHistorySoamPmExtSumR2PFDR,
       "f3EsaProbeHistorySoamPmExtSumOfSqR2PFDR": f3EsaProbeHistorySoamPmExtSumOfSqR2PFDR,
       "f3EsaProbeHistorySoamPmExtMaxRTFDR": f3EsaProbeHistorySoamPmExtMaxRTFDR,
       "f3EsaProbeHistorySoamPmExtAvgRTFDR": f3EsaProbeHistorySoamPmExtAvgRTFDR,
       "f3EsaProbeHistorySoamPmExtNumRTFDR": f3EsaProbeHistorySoamPmExtNumRTFDR,
       "f3EsaProbeHistorySoamPmExtSumRTFDR": f3EsaProbeHistorySoamPmExtSumRTFDR,
       "f3EsaProbeHistorySoamPmExtSumOfSqRTFDR": f3EsaProbeHistorySoamPmExtSumOfSqRTFDR,
       "f3EsaProbeHistorySoamPmExtP2rAvailableDeltaTs": f3EsaProbeHistorySoamPmExtP2rAvailableDeltaTs,
       "f3EsaProbeHistorySoamPmExtR2pAvailableDeltaTs": f3EsaProbeHistorySoamPmExtR2pAvailableDeltaTs,
       "f3EsaProbeHistorySoamPmExtP2rUnavailableDeltaTs": f3EsaProbeHistorySoamPmExtP2rUnavailableDeltaTs,
       "f3EsaProbeHistorySoamPmExtR2pUnavailableDeltaTs": f3EsaProbeHistorySoamPmExtR2pUnavailableDeltaTs,
       "f3EsaProbeHistorySoamPmExtElapsedTime": f3EsaProbeHistorySoamPmExtElapsedTime,
       "cmServAssuranceNotifications": cmServAssuranceNotifications,
       "cmOperateLoopbackTrap": cmOperateLoopbackTrap,
       "cmReleaseLoopbackTrap": cmReleaseLoopbackTrap,
       "esaProbeThresholdCrossingAlert": esaProbeThresholdCrossingAlert,
       "cmServAssuranceConformance": cmServAssuranceConformance,
       "cmServAssuranceCompliances": cmServAssuranceCompliances,
       "cmServAssuranceCompliance": cmServAssuranceCompliance,
       "cmServAssuranceGroups": cmServAssuranceGroups,
       "cmServAssuranceObjectGroup": cmServAssuranceObjectGroup,
       "cmServAssuranceNotifGroup": cmServAssuranceNotifGroup,
       "cmEcpaGroup": cmEcpaGroup,
       "cmEsaGroup": cmEsaGroup,
       "cmServAssuranceGenNotifGroup": cmServAssuranceGenNotifGroup,
       "cmServAssuranceEsaNotifGroup": cmServAssuranceEsaNotifGroup,
       "cmBertGroup": cmBertGroup}
)
