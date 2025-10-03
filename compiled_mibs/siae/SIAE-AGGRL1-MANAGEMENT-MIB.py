# SNMP MIB module (SIAE-AGGRL1-MANAGEMENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\siae\SIAE-AGGRL1-MANAGEMENT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:26:36 2025
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(AlarmSeverityCode,
 AlarmStatus) = mibBuilder.importSymbols(
    "SIAE-ALARM-MIB",
    "AlarmSeverityCode",
    "AlarmStatus")

(siaeMib,) = mibBuilder.importSymbols(
    "SIAE-TREE-MIB",
    "siaeMib")

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
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

aggregationL1 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 83)
)
if mibBuilder.loadTexts:
    aggregationL1.setRevisions(
        ("2014-09-29 00:00",
         "2014-05-26 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AggregableType(TextualConvention, Integer32):
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
        *(("other", 1),
          ("radio", 2),
          ("lan", 3))
    )



# MIB Managed Objects in the order of their OIDs

_AggrL1MibVersion_Type = Integer32
_AggrL1MibVersion_Object = MibScalar
aggrL1MibVersion = _AggrL1MibVersion_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 83, 1),
    _AggrL1MibVersion_Type()
)
aggrL1MibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggrL1MibVersion.setStatus("current")
_AggrL1CapabilityTable_Object = MibTable
aggrL1CapabilityTable = _AggrL1CapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 83, 2)
)
if mibBuilder.loadTexts:
    aggrL1CapabilityTable.setStatus("current")
_AggrL1CapabilityEntry_Object = MibTableRow
aggrL1CapabilityEntry = _AggrL1CapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 83, 2, 1)
)
aggrL1CapabilityEntry.setIndexNames(
    (0, "SIAE-AGGRL1-MANAGEMENT-MIB", "aggrL1CapabilityAggregableIndex"),
    (0, "SIAE-AGGRL1-MANAGEMENT-MIB", "aggrL1CapabilityAggregableType"),
    (0, "SIAE-AGGRL1-MANAGEMENT-MIB", "aggrL1CapabilityAggregatorIndex"),
)
if mibBuilder.loadTexts:
    aggrL1CapabilityEntry.setStatus("current")
_AggrL1CapabilityAggregableIndex_Type = Integer32
_AggrL1CapabilityAggregableIndex_Object = MibTableColumn
aggrL1CapabilityAggregableIndex = _AggrL1CapabilityAggregableIndex_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 83, 2, 1, 1),
    _AggrL1CapabilityAggregableIndex_Type()
)
aggrL1CapabilityAggregableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggrL1CapabilityAggregableIndex.setStatus("current")
_AggrL1CapabilityAggregableType_Type = AggregableType
_AggrL1CapabilityAggregableType_Object = MibTableColumn
aggrL1CapabilityAggregableType = _AggrL1CapabilityAggregableType_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 83, 2, 1, 2),
    _AggrL1CapabilityAggregableType_Type()
)
aggrL1CapabilityAggregableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggrL1CapabilityAggregableType.setStatus("current")
_AggrL1CapabilityAggregatorIndex_Type = InterfaceIndexOrZero
_AggrL1CapabilityAggregatorIndex_Object = MibTableColumn
aggrL1CapabilityAggregatorIndex = _AggrL1CapabilityAggregatorIndex_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 83, 2, 1, 3),
    _AggrL1CapabilityAggregatorIndex_Type()
)
aggrL1CapabilityAggregatorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggrL1CapabilityAggregatorIndex.setStatus("current")
_AggrL1Table_Object = MibTable
aggrL1Table = _AggrL1Table_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 83, 3)
)
if mibBuilder.loadTexts:
    aggrL1Table.setStatus("current")
_AggrL1Entry_Object = MibTableRow
aggrL1Entry = _AggrL1Entry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 83, 3, 1)
)
aggrL1Entry.setIndexNames(
    (0, "SIAE-AGGRL1-MANAGEMENT-MIB", "aggrL1AggregableIndex"),
    (0, "SIAE-AGGRL1-MANAGEMENT-MIB", "aggrL1AggregableType"),
)
if mibBuilder.loadTexts:
    aggrL1Entry.setStatus("current")
_AggrL1AggregableIndex_Type = Integer32
_AggrL1AggregableIndex_Object = MibTableColumn
aggrL1AggregableIndex = _AggrL1AggregableIndex_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 83, 3, 1, 1),
    _AggrL1AggregableIndex_Type()
)
aggrL1AggregableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggrL1AggregableIndex.setStatus("current")
_AggrL1AggregableType_Type = AggregableType
_AggrL1AggregableType_Object = MibTableColumn
aggrL1AggregableType = _AggrL1AggregableType_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 83, 3, 1, 2),
    _AggrL1AggregableType_Type()
)
aggrL1AggregableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggrL1AggregableType.setStatus("current")
_AggrL1AggregatorIndex_Type = InterfaceIndexOrZero
_AggrL1AggregatorIndex_Object = MibTableColumn
aggrL1AggregatorIndex = _AggrL1AggregatorIndex_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 83, 3, 1, 3),
    _AggrL1AggregatorIndex_Type()
)
aggrL1AggregatorIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aggrL1AggregatorIndex.setStatus("current")
_AggrL1StorageType_Type = StorageType
_AggrL1StorageType_Object = MibTableColumn
aggrL1StorageType = _AggrL1StorageType_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 83, 3, 1, 4),
    _AggrL1StorageType_Type()
)
aggrL1StorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aggrL1StorageType.setStatus("current")
_AggrL1Rowstatus_Type = RowStatus
_AggrL1Rowstatus_Object = MibTableColumn
aggrL1Rowstatus = _AggrL1Rowstatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 83, 3, 1, 5),
    _AggrL1Rowstatus_Type()
)
aggrL1Rowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aggrL1Rowstatus.setStatus("current")
_AggrL1AlarmTable_Object = MibTable
aggrL1AlarmTable = _AggrL1AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 83, 4)
)
if mibBuilder.loadTexts:
    aggrL1AlarmTable.setStatus("current")
_AggrL1AlarmEntry_Object = MibTableRow
aggrL1AlarmEntry = _AggrL1AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 83, 4, 1)
)
aggrL1AlarmEntry.setIndexNames(
    (0, "SIAE-AGGRL1-MANAGEMENT-MIB", "aggrL1AlarmAggregatorIndex"),
)
if mibBuilder.loadTexts:
    aggrL1AlarmEntry.setStatus("current")
_AggrL1AlarmAggregatorIndex_Type = InterfaceIndexOrZero
_AggrL1AlarmAggregatorIndex_Object = MibTableColumn
aggrL1AlarmAggregatorIndex = _AggrL1AlarmAggregatorIndex_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 83, 4, 1, 1),
    _AggrL1AlarmAggregatorIndex_Type()
)
aggrL1AlarmAggregatorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggrL1AlarmAggregatorIndex.setStatus("current")
_AggrL1FailAlarm_Type = AlarmStatus
_AggrL1FailAlarm_Object = MibTableColumn
aggrL1FailAlarm = _AggrL1FailAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 83, 4, 1, 2),
    _AggrL1FailAlarm_Type()
)
aggrL1FailAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggrL1FailAlarm.setStatus("current")
_AggrL1DegradeAlarm_Type = AlarmStatus
_AggrL1DegradeAlarm_Object = MibTableColumn
aggrL1DegradeAlarm = _AggrL1DegradeAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 83, 4, 1, 3),
    _AggrL1DegradeAlarm_Type()
)
aggrL1DegradeAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggrL1DegradeAlarm.setStatus("current")
_AggrL1RealignmentAlarm_Type = AlarmStatus
_AggrL1RealignmentAlarm_Object = MibTableColumn
aggrL1RealignmentAlarm = _AggrL1RealignmentAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 83, 4, 1, 4),
    _AggrL1RealignmentAlarm_Type()
)
aggrL1RealignmentAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggrL1RealignmentAlarm.setStatus("current")


class _AggrL1FailAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type aggrL1FailAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_AggrL1FailAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_AggrL1FailAlarmSeverityCode_Object = MibScalar
aggrL1FailAlarmSeverityCode = _AggrL1FailAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 83, 5),
    _AggrL1FailAlarmSeverityCode_Type()
)
aggrL1FailAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aggrL1FailAlarmSeverityCode.setStatus("current")


class _AggrL1DegradeAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type aggrL1DegradeAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_AggrL1DegradeAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_AggrL1DegradeAlarmSeverityCode_Object = MibScalar
aggrL1DegradeAlarmSeverityCode = _AggrL1DegradeAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 83, 6),
    _AggrL1DegradeAlarmSeverityCode_Type()
)
aggrL1DegradeAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aggrL1DegradeAlarmSeverityCode.setStatus("current")


class _AggrL1RealignmentAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type aggrL1RealignmentAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_AggrL1RealignmentAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_AggrL1RealignmentAlarmSeverityCode_Object = MibScalar
aggrL1RealignmentAlarmSeverityCode = _AggrL1RealignmentAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 83, 7),
    _AggrL1RealignmentAlarmSeverityCode_Type()
)
aggrL1RealignmentAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aggrL1RealignmentAlarmSeverityCode.setStatus("current")
_AggrL1ConnectionTable_Object = MibTable
aggrL1ConnectionTable = _AggrL1ConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 83, 8)
)
if mibBuilder.loadTexts:
    aggrL1ConnectionTable.setStatus("current")
_AggrL1ConnectionEntry_Object = MibTableRow
aggrL1ConnectionEntry = _AggrL1ConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 83, 8, 1)
)
aggrL1ConnectionEntry.setIndexNames(
    (0, "SIAE-AGGRL1-MANAGEMENT-MIB", "aggrL1ConnAggregableIndex"),
    (0, "SIAE-AGGRL1-MANAGEMENT-MIB", "aggrL1ConnAggregableType"),
)
if mibBuilder.loadTexts:
    aggrL1ConnectionEntry.setStatus("current")
_AggrL1ConnAggregableIndex_Type = Integer32
_AggrL1ConnAggregableIndex_Object = MibTableColumn
aggrL1ConnAggregableIndex = _AggrL1ConnAggregableIndex_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 83, 8, 1, 1),
    _AggrL1ConnAggregableIndex_Type()
)
aggrL1ConnAggregableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggrL1ConnAggregableIndex.setStatus("current")
_AggrL1ConnAggregableType_Type = AggregableType
_AggrL1ConnAggregableType_Object = MibTableColumn
aggrL1ConnAggregableType = _AggrL1ConnAggregableType_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 83, 8, 1, 2),
    _AggrL1ConnAggregableType_Type()
)
aggrL1ConnAggregableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggrL1ConnAggregableType.setStatus("current")
_AggrL1ConnAggregatorIndex_Type = InterfaceIndexOrZero
_AggrL1ConnAggregatorIndex_Object = MibTableColumn
aggrL1ConnAggregatorIndex = _AggrL1ConnAggregatorIndex_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 83, 8, 1, 3),
    _AggrL1ConnAggregatorIndex_Type()
)
aggrL1ConnAggregatorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggrL1ConnAggregatorIndex.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SIAE-AGGRL1-MANAGEMENT-MIB",
    **{"AggregableType": AggregableType,
       "aggregationL1": aggregationL1,
       "aggrL1MibVersion": aggrL1MibVersion,
       "aggrL1CapabilityTable": aggrL1CapabilityTable,
       "aggrL1CapabilityEntry": aggrL1CapabilityEntry,
       "aggrL1CapabilityAggregableIndex": aggrL1CapabilityAggregableIndex,
       "aggrL1CapabilityAggregableType": aggrL1CapabilityAggregableType,
       "aggrL1CapabilityAggregatorIndex": aggrL1CapabilityAggregatorIndex,
       "aggrL1Table": aggrL1Table,
       "aggrL1Entry": aggrL1Entry,
       "aggrL1AggregableIndex": aggrL1AggregableIndex,
       "aggrL1AggregableType": aggrL1AggregableType,
       "aggrL1AggregatorIndex": aggrL1AggregatorIndex,
       "aggrL1StorageType": aggrL1StorageType,
       "aggrL1Rowstatus": aggrL1Rowstatus,
       "aggrL1AlarmTable": aggrL1AlarmTable,
       "aggrL1AlarmEntry": aggrL1AlarmEntry,
       "aggrL1AlarmAggregatorIndex": aggrL1AlarmAggregatorIndex,
       "aggrL1FailAlarm": aggrL1FailAlarm,
       "aggrL1DegradeAlarm": aggrL1DegradeAlarm,
       "aggrL1RealignmentAlarm": aggrL1RealignmentAlarm,
       "aggrL1FailAlarmSeverityCode": aggrL1FailAlarmSeverityCode,
       "aggrL1DegradeAlarmSeverityCode": aggrL1DegradeAlarmSeverityCode,
       "aggrL1RealignmentAlarmSeverityCode": aggrL1RealignmentAlarmSeverityCode,
       "aggrL1ConnectionTable": aggrL1ConnectionTable,
       "aggrL1ConnectionEntry": aggrL1ConnectionEntry,
       "aggrL1ConnAggregableIndex": aggrL1ConnAggregableIndex,
       "aggrL1ConnAggregableType": aggrL1ConnAggregableType,
       "aggrL1ConnAggregatorIndex": aggrL1ConnAggregatorIndex}
)
