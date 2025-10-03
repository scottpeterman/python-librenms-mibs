# SNMP MIB module (SIAE-LLF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\siae\SIAE-LLF-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:27:06 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

llf = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 85)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _LlfMibVersion_Type(Integer32):
    """Custom type llfMibVersion based on Integer32"""
    defaultValue = 1


_LlfMibVersion_Type.__name__ = "Integer32"
_LlfMibVersion_Object = MibScalar
llfMibVersion = _LlfMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 85, 1),
    _LlfMibVersion_Type()
)
llfMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llfMibVersion.setStatus("current")
_LlfTable_Object = MibTable
llfTable = _LlfTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 85, 2)
)
if mibBuilder.loadTexts:
    llfTable.setStatus("current")
_LlfEntry_Object = MibTableRow
llfEntry = _LlfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 85, 2, 1)
)
llfEntry.setIndexNames(
    (0, "SIAE-LLF-MIB", "llfIndex"),
)
if mibBuilder.loadTexts:
    llfEntry.setStatus("current")
_LlfIndex_Type = InterfaceIndex
_LlfIndex_Object = MibTableColumn
llfIndex = _LlfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 85, 2, 1, 1),
    _LlfIndex_Type()
)
llfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    llfIndex.setStatus("current")


class _LlfEnable_Type(Integer32):
    """Custom type llfEnable based on Integer32"""
    defaultValue = 1

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


_LlfEnable_Type.__name__ = "Integer32"
_LlfEnable_Object = MibTableColumn
llfEnable = _LlfEnable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 85, 2, 1, 2),
    _LlfEnable_Type()
)
llfEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    llfEnable.setStatus("current")


class _LlfUnidirectionalFault_Type(Integer32):
    """Custom type llfUnidirectionalFault based on Integer32"""
    defaultValue = 1

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


_LlfUnidirectionalFault_Type.__name__ = "Integer32"
_LlfUnidirectionalFault_Object = MibTableColumn
llfUnidirectionalFault = _LlfUnidirectionalFault_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 85, 2, 1, 3),
    _LlfUnidirectionalFault_Type()
)
llfUnidirectionalFault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    llfUnidirectionalFault.setStatus("current")


class _LlfDelayTime_Type(Integer32):
    """Custom type llfDelayTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_LlfDelayTime_Type.__name__ = "Integer32"
_LlfDelayTime_Object = MibTableColumn
llfDelayTime = _LlfDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 85, 2, 1, 4),
    _LlfDelayTime_Type()
)
llfDelayTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    llfDelayTime.setStatus("current")


class _LlfProtectionMode_Type(Integer32):
    """Custom type llfProtectionMode based on Integer32"""
    defaultValue = 1

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


_LlfProtectionMode_Type.__name__ = "Integer32"
_LlfProtectionMode_Object = MibTableColumn
llfProtectionMode = _LlfProtectionMode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 85, 2, 1, 5),
    _LlfProtectionMode_Type()
)
llfProtectionMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    llfProtectionMode.setStatus("current")
_LlfAlarm_Type = AlarmStatus
_LlfAlarm_Object = MibTableColumn
llfAlarm = _LlfAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 85, 2, 1, 6),
    _LlfAlarm_Type()
)
llfAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llfAlarm.setStatus("current")
_LlfRowStatus_Type = RowStatus
_LlfRowStatus_Object = MibTableColumn
llfRowStatus = _LlfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 85, 2, 1, 7),
    _LlfRowStatus_Type()
)
llfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    llfRowStatus.setStatus("current")
_LlfMapTable_Object = MibTable
llfMapTable = _LlfMapTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 85, 3)
)
if mibBuilder.loadTexts:
    llfMapTable.setStatus("current")
_LlfMapEntry_Object = MibTableRow
llfMapEntry = _LlfMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 85, 3, 1)
)
llfMapEntry.setIndexNames(
    (0, "SIAE-LLF-MIB", "llfIndex"),
    (0, "SIAE-LLF-MIB", "llfMapLinkIndex"),
    (0, "SIAE-LLF-MIB", "llfMapPolIndex"),
    (0, "SIAE-LLF-MIB", "llfMapCircuitIndex"),
)
if mibBuilder.loadTexts:
    llfMapEntry.setStatus("current")
_LlfMapLinkIndex_Type = Integer32
_LlfMapLinkIndex_Object = MibTableColumn
llfMapLinkIndex = _LlfMapLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 85, 3, 1, 1),
    _LlfMapLinkIndex_Type()
)
llfMapLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llfMapLinkIndex.setStatus("current")
_LlfMapPolIndex_Type = Integer32
_LlfMapPolIndex_Object = MibTableColumn
llfMapPolIndex = _LlfMapPolIndex_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 85, 3, 1, 2),
    _LlfMapPolIndex_Type()
)
llfMapPolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llfMapPolIndex.setStatus("current")
_LlfMapCircuitIndex_Type = Integer32
_LlfMapCircuitIndex_Object = MibTableColumn
llfMapCircuitIndex = _LlfMapCircuitIndex_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 85, 3, 1, 3),
    _LlfMapCircuitIndex_Type()
)
llfMapCircuitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llfMapCircuitIndex.setStatus("current")


class _LlfMapLosInsertion_Type(Integer32):
    """Custom type llfMapLosInsertion based on Integer32"""
    defaultValue = 2

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


_LlfMapLosInsertion_Type.__name__ = "Integer32"
_LlfMapLosInsertion_Object = MibTableColumn
llfMapLosInsertion = _LlfMapLosInsertion_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 85, 3, 1, 4),
    _LlfMapLosInsertion_Type()
)
llfMapLosInsertion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    llfMapLosInsertion.setStatus("current")


class _LlfMapInsertionMode_Type(Integer32):
    """Custom type llfMapInsertionMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("single", 1),
          ("group", 2))
    )


_LlfMapInsertionMode_Type.__name__ = "Integer32"
_LlfMapInsertionMode_Object = MibTableColumn
llfMapInsertionMode = _LlfMapInsertionMode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 85, 3, 1, 5),
    _LlfMapInsertionMode_Type()
)
llfMapInsertionMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    llfMapInsertionMode.setStatus("current")
_LlfMapSignalFail_Type = TruthValue
_LlfMapSignalFail_Object = MibTableColumn
llfMapSignalFail = _LlfMapSignalFail_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 85, 3, 1, 6),
    _LlfMapSignalFail_Type()
)
llfMapSignalFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llfMapSignalFail.setStatus("current")
_LlfMapRowStatus_Type = RowStatus
_LlfMapRowStatus_Object = MibTableColumn
llfMapRowStatus = _LlfMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 85, 3, 1, 7),
    _LlfMapRowStatus_Type()
)
llfMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    llfMapRowStatus.setStatus("current")
_LlfCircuitTable_Object = MibTable
llfCircuitTable = _LlfCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 85, 4)
)
if mibBuilder.loadTexts:
    llfCircuitTable.setStatus("current")
_LlfCircuitEntry_Object = MibTableRow
llfCircuitEntry = _LlfCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 85, 4, 1)
)
llfCircuitEntry.setIndexNames(
    (0, "SIAE-LLF-MIB", "llfCircuitLinkIndex"),
    (0, "SIAE-LLF-MIB", "llfCircuitPolIndex"),
    (0, "SIAE-LLF-MIB", "llfCircuitIndex"),
)
if mibBuilder.loadTexts:
    llfCircuitEntry.setStatus("current")
_LlfCircuitLinkIndex_Type = Integer32
_LlfCircuitLinkIndex_Object = MibTableColumn
llfCircuitLinkIndex = _LlfCircuitLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 85, 4, 1, 1),
    _LlfCircuitLinkIndex_Type()
)
llfCircuitLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llfCircuitLinkIndex.setStatus("current")
_LlfCircuitPolIndex_Type = Integer32
_LlfCircuitPolIndex_Object = MibTableColumn
llfCircuitPolIndex = _LlfCircuitPolIndex_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 85, 4, 1, 2),
    _LlfCircuitPolIndex_Type()
)
llfCircuitPolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llfCircuitPolIndex.setStatus("current")
_LlfCircuitIndex_Type = Integer32
_LlfCircuitIndex_Object = MibTableColumn
llfCircuitIndex = _LlfCircuitIndex_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 85, 4, 1, 3),
    _LlfCircuitIndex_Type()
)
llfCircuitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llfCircuitIndex.setStatus("current")


class _LlfCircuitLinkLabel_Type(DisplayString):
    """Custom type llfCircuitLinkLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LlfCircuitLinkLabel_Type.__name__ = "DisplayString"
_LlfCircuitLinkLabel_Object = MibTableColumn
llfCircuitLinkLabel = _LlfCircuitLinkLabel_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 85, 4, 1, 4),
    _LlfCircuitLinkLabel_Type()
)
llfCircuitLinkLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llfCircuitLinkLabel.setStatus("current")
_LlfCircuitRowStatus_Type = RowStatus
_LlfCircuitRowStatus_Object = MibTableColumn
llfCircuitRowStatus = _LlfCircuitRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 85, 4, 1, 5),
    _LlfCircuitRowStatus_Type()
)
llfCircuitRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    llfCircuitRowStatus.setStatus("current")


class _LlfAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type llfAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_LlfAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_LlfAlarmSeverityCode_Object = MibScalar
llfAlarmSeverityCode = _LlfAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 85, 5),
    _LlfAlarmSeverityCode_Type()
)
llfAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llfAlarmSeverityCode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SIAE-LLF-MIB",
    **{"llf": llf,
       "llfMibVersion": llfMibVersion,
       "llfTable": llfTable,
       "llfEntry": llfEntry,
       "llfIndex": llfIndex,
       "llfEnable": llfEnable,
       "llfUnidirectionalFault": llfUnidirectionalFault,
       "llfDelayTime": llfDelayTime,
       "llfProtectionMode": llfProtectionMode,
       "llfAlarm": llfAlarm,
       "llfRowStatus": llfRowStatus,
       "llfMapTable": llfMapTable,
       "llfMapEntry": llfMapEntry,
       "llfMapLinkIndex": llfMapLinkIndex,
       "llfMapPolIndex": llfMapPolIndex,
       "llfMapCircuitIndex": llfMapCircuitIndex,
       "llfMapLosInsertion": llfMapLosInsertion,
       "llfMapInsertionMode": llfMapInsertionMode,
       "llfMapSignalFail": llfMapSignalFail,
       "llfMapRowStatus": llfMapRowStatus,
       "llfCircuitTable": llfCircuitTable,
       "llfCircuitEntry": llfCircuitEntry,
       "llfCircuitLinkIndex": llfCircuitLinkIndex,
       "llfCircuitPolIndex": llfCircuitPolIndex,
       "llfCircuitIndex": llfCircuitIndex,
       "llfCircuitLinkLabel": llfCircuitLinkLabel,
       "llfCircuitRowStatus": llfCircuitRowStatus,
       "llfAlarmSeverityCode": llfAlarmSeverityCode}
)
