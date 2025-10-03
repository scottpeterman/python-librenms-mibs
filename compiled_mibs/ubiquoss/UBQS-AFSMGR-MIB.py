# SNMP MIB module (UBQS-AFSMGR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ubiquoss\UBQS-AFSMGR-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:33:10 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysContact,
 sysLocation,
 sysName,
 sysObjectID) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysContact",
    "sysLocation",
    "sysName",
    "sysObjectID")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(ubiMgmtv2,) = mibBuilder.importSymbols(
    "UBQS-SMI",
    "ubiMgmtv2")


# MODULE-IDENTITY

ubiAFSMGREventMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CurrentAlarmTable_Object = MibTable
currentAlarmTable = _CurrentAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 1)
)
if mibBuilder.loadTexts:
    currentAlarmTable.setStatus("current")
_CurrentAlarmEntry_Object = MibTableRow
currentAlarmEntry = _CurrentAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 1, 1)
)
currentAlarmEntry.setIndexNames(
    (0, "UBQS-AFSMGR-MIB", "AlarmIndex"),
)
if mibBuilder.loadTexts:
    currentAlarmEntry.setStatus("current")
_AlarmIndex_Type = Integer32
_AlarmIndex_Object = MibTableColumn
alarmIndex = _AlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 1, 1, 1),
    _AlarmIndex_Type()
)
alarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmIndex.setStatus("current")
_AlarmId_Type = DisplayString
_AlarmId_Object = MibTableColumn
alarmId = _AlarmId_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 1, 1, 2),
    _AlarmId_Type()
)
alarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmId.setStatus("current")


class _AlarmType_Type(Integer32):
    """Custom type alarmType based on Integer32"""
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
        *(("equipment", 1),
          ("communications", 2),
          ("qos", 3),
          ("processing", 4),
          ("environment", 5))
    )


_AlarmType_Type.__name__ = "Integer32"
_AlarmType_Object = MibTableColumn
alarmType = _AlarmType_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 1, 1, 3),
    _AlarmType_Type()
)
alarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmType.setStatus("current")


class _AlarmSeverity_Type(Integer32):
    """Custom type alarmSeverity based on Integer32"""
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
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("warning", 4),
          ("indeterminate", 5))
    )


_AlarmSeverity_Type.__name__ = "Integer32"
_AlarmSeverity_Object = MibTableColumn
alarmSeverity = _AlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 1, 1, 4),
    _AlarmSeverity_Type()
)
alarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSeverity.setStatus("current")
_AlarmPhysicalLoc_Type = DisplayString
_AlarmPhysicalLoc_Object = MibTableColumn
alarmPhysicalLoc = _AlarmPhysicalLoc_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 1, 1, 5),
    _AlarmPhysicalLoc_Type()
)
alarmPhysicalLoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmPhysicalLoc.setStatus("current")
_AlarmLogicalLoc_Type = DisplayString
_AlarmLogicalLoc_Object = MibTableColumn
alarmLogicalLoc = _AlarmLogicalLoc_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 1, 1, 6),
    _AlarmLogicalLoc_Type()
)
alarmLogicalLoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLogicalLoc.setStatus("current")
_AlarmCurStatus_Type = Integer32
_AlarmCurStatus_Object = MibTableColumn
alarmCurStatus = _AlarmCurStatus_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 1, 1, 7),
    _AlarmCurStatus_Type()
)
alarmCurStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurStatus.setStatus("current")
_AlarmAuxinfo_Type = DisplayString
_AlarmAuxinfo_Object = MibTableColumn
alarmAuxinfo = _AlarmAuxinfo_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 1, 1, 8),
    _AlarmAuxinfo_Type()
)
alarmAuxinfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmAuxinfo.setStatus("current")
_AlarmDateTime_Type = DisplayString
_AlarmDateTime_Object = MibTableColumn
alarmDateTime = _AlarmDateTime_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 1, 1, 9),
    _AlarmDateTime_Type()
)
alarmDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmDateTime.setStatus("current")
_AlarmStatus_Type = Integer32
_AlarmStatus_Object = MibTableColumn
alarmStatus = _AlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 1, 1, 10),
    _AlarmStatus_Type()
)
alarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmStatus.setStatus("current")
_EventLogTable_Object = MibTable
eventLogTable = _EventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 2)
)
if mibBuilder.loadTexts:
    eventLogTable.setStatus("current")
_EventLogEntry_Object = MibTableRow
eventLogEntry = _EventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 2, 1)
)
eventLogEntry.setIndexNames(
    (0, "UBQS-AFSMGR-MIB", "EventIndex"),
)
if mibBuilder.loadTexts:
    eventLogEntry.setStatus("current")
_EventIndex_Type = Integer32
_EventIndex_Object = MibTableColumn
eventIndex = _EventIndex_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 2, 1, 1),
    _EventIndex_Type()
)
eventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventIndex.setStatus("current")
_EventId_Type = DisplayString
_EventId_Object = MibTableColumn
eventId = _EventId_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 2, 1, 2),
    _EventId_Type()
)
eventId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventId.setStatus("current")


class _EventType_Type(Integer32):
    """Custom type eventType based on Integer32"""
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
        *(("equipment", 1),
          ("communications", 2),
          ("qos", 3),
          ("processing", 4),
          ("environment", 5))
    )


_EventType_Type.__name__ = "Integer32"
_EventType_Object = MibTableColumn
eventType = _EventType_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 2, 1, 3),
    _EventType_Type()
)
eventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventType.setStatus("current")


class _EventSeverity_Type(Integer32):
    """Custom type eventSeverity based on Integer32"""
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
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("warning", 4),
          ("indeterminate", 5))
    )


_EventSeverity_Type.__name__ = "Integer32"
_EventSeverity_Object = MibTableColumn
eventSeverity = _EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 2, 1, 4),
    _EventSeverity_Type()
)
eventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventSeverity.setStatus("current")
_EventValue_Type = DisplayString
_EventValue_Object = MibTableColumn
eventValue = _EventValue_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 2, 1, 5),
    _EventValue_Type()
)
eventValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventValue.setStatus("current")
_EventDateTime_Type = DisplayString
_EventDateTime_Object = MibTableColumn
eventDateTime = _EventDateTime_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 2, 1, 6),
    _EventDateTime_Type()
)
eventDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventDateTime.setStatus("current")
_EventStatus_Type = Integer32
_EventStatus_Object = MibTableColumn
eventStatus = _EventStatus_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 2, 1, 7),
    _EventStatus_Type()
)
eventStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventStatus.setStatus("current")
_AfsmgrEventManagerTrap_ObjectIdentity = ObjectIdentity
afsmgrEventManagerTrap = _AfsmgrEventManagerTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3)
)

# Managed Objects groups


# Notification objects

sysWarmStartNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 1)
)
sysWarmStartNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    sysWarmStartNoti.setStatus(
        "current"
    )

sysColdStartNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 2)
)
sysColdStartNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    sysColdStartNoti.setStatus(
        "current"
    )

linkUpNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 3)
)
linkUpNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    linkUpNoti.setStatus(
        "current"
    )

linkDownNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 4)
)
linkDownNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    linkDownNoti.setStatus(
        "current"
    )

cpuOverloadFallingNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 5)
)
cpuOverloadFallingNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    cpuOverloadFallingNoti.setStatus(
        "current"
    )

cpuOverloadRisingNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 6)
)
cpuOverloadRisingNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    cpuOverloadRisingNoti.setStatus(
        "current"
    )

gbicOperNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 7)
)
gbicOperNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    gbicOperNoti.setStatus(
        "current"
    )

memoryOverloadNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 8)
)
memoryOverloadNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    memoryOverloadNoti.setStatus(
        "current"
    )

slotOperNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 9)
)
slotOperNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    slotOperNoti.setStatus(
        "current"
    )

tempLowNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 10)
)
tempLowNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    tempLowNoti.setStatus(
        "current"
    )

tempHighNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 11)
)
tempHighNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    tempHighNoti.setStatus(
        "current"
    )

fanAlarmNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 12)
)
fanAlarmNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    fanAlarmNoti.setStatus(
        "current"
    )

fmuEquipStatusNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 13)
)
fmuEquipStatusNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    fmuEquipStatusNoti.setStatus(
        "current"
    )

psuAlarmNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 14)
)
psuAlarmNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    psuAlarmNoti.setStatus(
        "current"
    )

psuEquipStatusNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 15)
)
psuEquipStatusNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    psuEquipStatusNoti.setStatus(
        "current"
    )

portAdminNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 16)
)
portAdminNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    portAdminNoti.setStatus(
        "current"
    )

fanOperStatusNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 17)
)
fanOperStatusNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    fanOperStatusNoti.setStatus(
        "current"
    )

rmonRisingNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 18)
)
rmonRisingNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    rmonRisingNoti.setStatus(
        "current"
    )

rmonFallingNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 19)
)
rmonFallingNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    rmonFallingNoti.setStatus(
        "current"
    )

portSLDNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 20)
)
portSLDNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    portSLDNoti.setStatus(
        "current"
    )

remoteConnection = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 30)
)
remoteConnection.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    remoteConnection.setStatus(
        "current"
    )

ponDriftWindowNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 41)
)
ponDriftWindowNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    ponDriftWindowNoti.setStatus(
        "current"
    )

ponGemChannelLossNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 42)
)
ponGemChannelLossNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    ponGemChannelLossNoti.setStatus(
        "current"
    )

ponAckLossNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 43)
)
ponAckLossNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    ponAckLossNoti.setStatus(
        "current"
    )

ponSigDegradeNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 44)
)
ponSigDegradeNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    ponSigDegradeNoti.setStatus(
        "current"
    )

ponSigFailNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 45)
)
ponSigFailNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    ponSigFailNoti.setStatus(
        "current"
    )

ponPhysEquipErrNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 46)
)
ponPhysEquipErrNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    ponPhysEquipErrNoti.setStatus(
        "current"
    )

ponKeySyncLossNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 47)
)
ponKeySyncLossNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    ponKeySyncLossNoti.setStatus(
        "current"
    )

ponTransIfWarmNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 48)
)
ponTransIfWarmNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    ponTransIfWarmNoti.setStatus(
        "current"
    )

ponTransIfAlarmNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 49)
)
ponTransIfAlarmNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    ponTransIfAlarmNoti.setStatus(
        "current"
    )

ponRemoDefectIndNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 50)
)
ponRemoDefectIndNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    ponRemoDefectIndNoti.setStatus(
        "current"
    )

onuOperStatusNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 51)
)
onuOperStatusNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    onuOperStatusNoti.setStatus(
        "current"
    )

oltAlarmNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 52)
)
oltAlarmNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    oltAlarmNoti.setStatus(
        "current"
    )

oltLinkFaultNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 53)
)
oltLinkFaultNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    oltLinkFaultNoti.setStatus(
        "current"
    )

ontDyingGaspNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 54)
)
ontDyingGaspNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    ontDyingGaspNoti.setStatus(
        "current"
    )

ponLinkStatusNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 55)
)
ponLinkStatusNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    ponLinkStatusNoti.setStatus(
        "current"
    )

linkLoopbackTestNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 57)
)
linkLoopbackTestNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    linkLoopbackTestNoti.setStatus(
        "current"
    )

ponOltOperStatusNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 68)
)
ponOltOperStatusNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    ponOltOperStatusNoti.setStatus(
        "current"
    )

ponOltAdminStatusNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 69)
)
ponOltAdminStatusNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    ponOltAdminStatusNoti.setStatus(
        "current"
    )

ponOnuAdminStatusNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 70)
)
ponOnuAdminStatusNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    ponOnuAdminStatusNoti.setStatus(
        "current"
    )

ponOnuRegisterSubMacNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 71)
)
ponOnuRegisterSubMacNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    ponOnuRegisterSubMacNoti.setStatus(
        "current"
    )

linkLoopbackTestFailNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 73)
)
linkLoopbackTestFailNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    linkLoopbackTestFailNoti.setStatus(
        "current"
    )

ponOnuRegOverloadNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 93)
)
ponOnuRegOverloadNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    ponOnuRegOverloadNoti.setStatus(
        "current"
    )

ponLinkRegNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 96)
)
ponLinkRegNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    ponLinkRegNoti.setStatus(
        "current"
    )

ponOnuLoopDetectNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 97)
)
ponOnuLoopDetectNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    ponOnuLoopDetectNoti.setStatus(
        "current"
    )

ponOltImageUpgrageNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 98)
)
ponOltImageUpgrageNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    ponOltImageUpgrageNoti.setStatus(
        "current"
    )

ponOltImageUpgrageFailNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 99)
)
ponOltImageUpgrageFailNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    ponOltImageUpgrageFailNoti.setStatus(
        "current"
    )

onuImageUpgradeNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 100)
)
onuImageUpgradeNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    onuImageUpgradeNoti.setStatus(
        "current"
    )

onuImageUpgradeFailNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 101)
)
onuImageUpgradeFailNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    onuImageUpgradeFailNoti.setStatus(
        "current"
    )

onuLdShutdownNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 102)
)
onuLdShutdownNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    onuLdShutdownNoti.setStatus(
        "current"
    )

ponUnadminMacRegNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 103)
)
ponUnadminMacRegNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    ponUnadminMacRegNoti.setStatus(
        "current"
    )

ponDupMacRegNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 104)
)
ponDupMacRegNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    ponDupMacRegNoti.setStatus(
        "current"
    )

ponOnuTypeMismatchNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 105)
)
ponOnuTypeMismatchNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    ponOnuTypeMismatchNoti.setStatus(
        "current"
    )

ponOltDyingGaspNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 106)
)
ponOltDyingGaspNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    ponOltDyingGaspNoti.setStatus(
        "current"
    )

ponOltCableDownNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 107)
)
ponOltCableDownNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    ponOltCableDownNoti.setStatus(
        "current"
    )

ponPMCcrc32MonitorNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 108)
)
ponPMCcrc32MonitorNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    ponPMCcrc32MonitorNoti.setStatus(
        "current"
    )

imageUpDownloadStatusNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 109)
)
imageUpDownloadStatusNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    imageUpDownloadStatusNoti.setStatus(
        "current"
    )

imageUpDownloadFailNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 110)
)
imageUpDownloadFailNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    imageUpDownloadFailNoti.setStatus(
        "current"
    )

configUpDownloadStatusNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 111)
)
configUpDownloadStatusNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    configUpDownloadStatusNoti.setStatus(
        "current"
    )

sysRebootMaxTempNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 112)
)
sysRebootMaxTempNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    sysRebootMaxTempNoti.setStatus(
        "current"
    )

ponRogueOnuLdShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 113)
)
ponRogueOnuLdShutdown.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    ponRogueOnuLdShutdown.setStatus(
        "current"
    )

scuOperStatusNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 114)
)
scuOperStatusNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    scuOperStatusNoti.setStatus(
        "current"
    )

configUpDownloadFailNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 115)
)
configUpDownloadFailNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    configUpDownloadFailNoti.setStatus(
        "current"
    )

ponOntRxPowerStatusNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 116)
)
ponOntRxPowerStatusNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    ponOntRxPowerStatusNoti.setStatus(
        "current"
    )

ponOltRxPowerStatusNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 117)
)
ponOltRxPowerStatusNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    ponOltRxPowerStatusNoti.setStatus(
        "current"
    )

ponOntTxPowerStatusNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 118)
)
ponOntTxPowerStatusNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    ponOntTxPowerStatusNoti.setStatus(
        "current"
    )

ponOntTemperatureStatusNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 119)
)
ponOntTemperatureStatusNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    ponOntTemperatureStatusNoti.setStatus(
        "current"
    )

ponOntVoltageStatusNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 120)
)
ponOntVoltageStatusNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    ponOntVoltageStatusNoti.setStatus(
        "current"
    )

ponOntBiasStatusNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 121)
)
ponOntBiasStatusNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    ponOntBiasStatusNoti.setStatus(
        "current"
    )

ponOltRedSlaveFaultNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 122)
)
ponOltRedSlaveFaultNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    ponOltRedSlaveFaultNoti.setStatus(
        "current"
    )

ponOltRedSwitchoverNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 123)
)
ponOltRedSwitchoverNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    ponOltRedSwitchoverNoti.setStatus(
        "current"
    )

ponOnuOpticRxPowerOnusNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 124)
)
ponOnuOpticRxPowerOnusNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    ponOnuOpticRxPowerOnusNoti.setStatus(
        "current"
    )

ponOnuDownThresholdNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 127)
)
ponOnuDownThresholdNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    ponOnuDownThresholdNoti.setStatus(
        "current"
    )

ponOnuFanStatusNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 128)
)
ponOnuFanStatusNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    ponOnuFanStatusNoti.setStatus(
        "current"
    )

ExternalACAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 129)
)
ExternalACAlarm.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    ExternalACAlarm.setStatus(
        "current"
    )

ExternalUnitAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 130)
)
ExternalUnitAlarm.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    ExternalUnitAlarm.setStatus(
        "current"
    )

ponLoopCntThresholdNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 131)
)
ponLoopCntThresholdNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    ponLoopCntThresholdNoti.setStatus(
        "current"
    )

scuUnequipNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 132)
)
scuUnequipNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    scuUnequipNoti.setStatus(
        "current"
    )

liuUnequipNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 133)
)
liuUnequipNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    liuUnequipNoti.setStatus(
        "current"
    )

fmuUnequipNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 134)
)
fmuUnequipNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    fmuUnequipNoti.setStatus(
        "current"
    )

ponOltLineCodeErrorMonitorNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 135)
)
ponOltLineCodeErrorMonitorNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    ponOltLineCodeErrorMonitorNoti.setStatus(
        "current"
    )

ponOltAlignmentErrorMonitorNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 136)
)
ponOltAlignmentErrorMonitorNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    ponOltAlignmentErrorMonitorNoti.setStatus(
        "current"
    )

scuEjectorAlarmNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 137)
)
scuEjectorAlarmNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    scuEjectorAlarmNoti.setStatus(
        "current"
    )

systemCheckAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 138)
)
systemCheckAlarm.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    systemCheckAlarm.setStatus(
        "current"
    )

ponOnuRegThreshOverNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 139)
)
ponOnuRegThreshOverNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    ponOnuRegThreshOverNoti.setStatus(
        "current"
    )

dcTempHighNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 140)
)
dcTempHighNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    dcTempHighNoti.setStatus(
        "current"
    )

dcTempLowNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 141)
)
dcTempLowNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    dcTempLowNoti.setStatus(
        "current"
    )

humidityHighNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 142)
)
humidityHighNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    humidityHighNoti.setStatus(
        "current"
    )

humidityLowNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 143)
)
humidityLowNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    humidityLowNoti.setStatus(
        "current"
    )

dcHumidityHighNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 144)
)
dcHumidityHighNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    dcHumidityHighNoti.setStatus(
        "current"
    )

dcHumidityLowNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 145)
)
dcHumidityLowNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    dcHumidityLowNoti.setStatus(
        "current"
    )

sysRebootMaxDcTempNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 146)
)
sysRebootMaxDcTempNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    sysRebootMaxDcTempNoti.setStatus(
        "current"
    )

sysRebootMaxHumidNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 147)
)
sysRebootMaxHumidNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    sysRebootMaxHumidNoti.setStatus(
        "current"
    )

sysRebootMaxDcHumidNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 148)
)
sysRebootMaxDcHumidNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    sysRebootMaxDcHumidNoti.setStatus(
        "current"
    )

fanSpeedHighNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 149)
)
fanSpeedHighNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    fanSpeedHighNoti.setStatus(
        "current"
    )

psuUnequipNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 150)
)
psuUnequipNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    psuUnequipNoti.setStatus(
        "current"
    )

doorOpenAlarmNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 151)
)
doorOpenAlarmNoti.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    doorOpenAlarmNoti.setStatus(
        "current"
    )

ExternalMajorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 152)
)
ExternalMajorAlarm.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    ExternalMajorAlarm.setStatus(
        "current"
    )

Piu10gFanFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 7, 3, 157)
)
Piu10gFanFailAlarm.setObjects(
      *(("UBQS-AFSMGR-MIB", "alarmIndex"),
        ("UBQS-AFSMGR-MIB", "alarmId"),
        ("UBQS-AFSMGR-MIB", "alarmType"),
        ("UBQS-AFSMGR-MIB", "alarmSeverity"),
        ("UBQS-AFSMGR-MIB", "alarmPhysicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmLogicalLoc"),
        ("UBQS-AFSMGR-MIB", "alarmCurStatus"),
        ("UBQS-AFSMGR-MIB", "alarmAuxinfo"),
        ("UBQS-AFSMGR-MIB", "alarmDateTime"),
        ("UBQS-AFSMGR-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    Piu10gFanFailAlarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UBQS-AFSMGR-MIB",
    **{"ubiAFSMGREventMIB": ubiAFSMGREventMIB,
       "currentAlarmTable": currentAlarmTable,
       "currentAlarmEntry": currentAlarmEntry,
       "alarmIndex": alarmIndex,
       "alarmId": alarmId,
       "alarmType": alarmType,
       "alarmSeverity": alarmSeverity,
       "alarmPhysicalLoc": alarmPhysicalLoc,
       "alarmLogicalLoc": alarmLogicalLoc,
       "alarmCurStatus": alarmCurStatus,
       "alarmAuxinfo": alarmAuxinfo,
       "alarmDateTime": alarmDateTime,
       "alarmStatus": alarmStatus,
       "eventLogTable": eventLogTable,
       "eventLogEntry": eventLogEntry,
       "eventIndex": eventIndex,
       "eventId": eventId,
       "eventType": eventType,
       "eventSeverity": eventSeverity,
       "eventValue": eventValue,
       "eventDateTime": eventDateTime,
       "eventStatus": eventStatus,
       "afsmgrEventManagerTrap": afsmgrEventManagerTrap,
       "sysWarmStartNoti": sysWarmStartNoti,
       "sysColdStartNoti": sysColdStartNoti,
       "linkUpNoti": linkUpNoti,
       "linkDownNoti": linkDownNoti,
       "cpuOverloadFallingNoti": cpuOverloadFallingNoti,
       "cpuOverloadRisingNoti": cpuOverloadRisingNoti,
       "gbicOperNoti": gbicOperNoti,
       "memoryOverloadNoti": memoryOverloadNoti,
       "slotOperNoti": slotOperNoti,
       "tempLowNoti": tempLowNoti,
       "tempHighNoti": tempHighNoti,
       "fanAlarmNoti": fanAlarmNoti,
       "fmuEquipStatusNoti": fmuEquipStatusNoti,
       "psuAlarmNoti": psuAlarmNoti,
       "psuEquipStatusNoti": psuEquipStatusNoti,
       "portAdminNoti": portAdminNoti,
       "fanOperStatusNoti": fanOperStatusNoti,
       "rmonRisingNoti": rmonRisingNoti,
       "rmonFallingNoti": rmonFallingNoti,
       "portSLDNoti": portSLDNoti,
       "remoteConnection": remoteConnection,
       "ponDriftWindowNoti": ponDriftWindowNoti,
       "ponGemChannelLossNoti": ponGemChannelLossNoti,
       "ponAckLossNoti": ponAckLossNoti,
       "ponSigDegradeNoti": ponSigDegradeNoti,
       "ponSigFailNoti": ponSigFailNoti,
       "ponPhysEquipErrNoti": ponPhysEquipErrNoti,
       "ponKeySyncLossNoti": ponKeySyncLossNoti,
       "ponTransIfWarmNoti": ponTransIfWarmNoti,
       "ponTransIfAlarmNoti": ponTransIfAlarmNoti,
       "ponRemoDefectIndNoti": ponRemoDefectIndNoti,
       "onuOperStatusNoti": onuOperStatusNoti,
       "oltAlarmNoti": oltAlarmNoti,
       "oltLinkFaultNoti": oltLinkFaultNoti,
       "ontDyingGaspNoti": ontDyingGaspNoti,
       "ponLinkStatusNoti": ponLinkStatusNoti,
       "linkLoopbackTestNoti": linkLoopbackTestNoti,
       "ponOltOperStatusNoti": ponOltOperStatusNoti,
       "ponOltAdminStatusNoti": ponOltAdminStatusNoti,
       "ponOnuAdminStatusNoti": ponOnuAdminStatusNoti,
       "ponOnuRegisterSubMacNoti": ponOnuRegisterSubMacNoti,
       "linkLoopbackTestFailNoti": linkLoopbackTestFailNoti,
       "ponOnuRegOverloadNoti": ponOnuRegOverloadNoti,
       "ponLinkRegNoti": ponLinkRegNoti,
       "ponOnuLoopDetectNoti": ponOnuLoopDetectNoti,
       "ponOltImageUpgrageNoti": ponOltImageUpgrageNoti,
       "ponOltImageUpgrageFailNoti": ponOltImageUpgrageFailNoti,
       "onuImageUpgradeNoti": onuImageUpgradeNoti,
       "onuImageUpgradeFailNoti": onuImageUpgradeFailNoti,
       "onuLdShutdownNoti": onuLdShutdownNoti,
       "ponUnadminMacRegNoti": ponUnadminMacRegNoti,
       "ponDupMacRegNoti": ponDupMacRegNoti,
       "ponOnuTypeMismatchNoti": ponOnuTypeMismatchNoti,
       "ponOltDyingGaspNoti": ponOltDyingGaspNoti,
       "ponOltCableDownNoti": ponOltCableDownNoti,
       "ponPMCcrc32MonitorNoti": ponPMCcrc32MonitorNoti,
       "imageUpDownloadStatusNoti": imageUpDownloadStatusNoti,
       "imageUpDownloadFailNoti": imageUpDownloadFailNoti,
       "configUpDownloadStatusNoti": configUpDownloadStatusNoti,
       "sysRebootMaxTempNoti": sysRebootMaxTempNoti,
       "ponRogueOnuLdShutdown": ponRogueOnuLdShutdown,
       "scuOperStatusNoti": scuOperStatusNoti,
       "configUpDownloadFailNoti": configUpDownloadFailNoti,
       "ponOntRxPowerStatusNoti": ponOntRxPowerStatusNoti,
       "ponOltRxPowerStatusNoti": ponOltRxPowerStatusNoti,
       "ponOntTxPowerStatusNoti": ponOntTxPowerStatusNoti,
       "ponOntTemperatureStatusNoti": ponOntTemperatureStatusNoti,
       "ponOntVoltageStatusNoti": ponOntVoltageStatusNoti,
       "ponOntBiasStatusNoti": ponOntBiasStatusNoti,
       "ponOltRedSlaveFaultNoti": ponOltRedSlaveFaultNoti,
       "ponOltRedSwitchoverNoti": ponOltRedSwitchoverNoti,
       "ponOnuOpticRxPowerOnusNoti": ponOnuOpticRxPowerOnusNoti,
       "ponOnuDownThresholdNoti": ponOnuDownThresholdNoti,
       "ponOnuFanStatusNoti": ponOnuFanStatusNoti,
       "ExternalACAlarm": ExternalACAlarm,
       "ExternalUnitAlarm": ExternalUnitAlarm,
       "ponLoopCntThresholdNoti": ponLoopCntThresholdNoti,
       "scuUnequipNoti": scuUnequipNoti,
       "liuUnequipNoti": liuUnequipNoti,
       "fmuUnequipNoti": fmuUnequipNoti,
       "ponOltLineCodeErrorMonitorNoti": ponOltLineCodeErrorMonitorNoti,
       "ponOltAlignmentErrorMonitorNoti": ponOltAlignmentErrorMonitorNoti,
       "scuEjectorAlarmNoti": scuEjectorAlarmNoti,
       "systemCheckAlarm": systemCheckAlarm,
       "ponOnuRegThreshOverNoti": ponOnuRegThreshOverNoti,
       "dcTempHighNoti": dcTempHighNoti,
       "dcTempLowNoti": dcTempLowNoti,
       "humidityHighNoti": humidityHighNoti,
       "humidityLowNoti": humidityLowNoti,
       "dcHumidityHighNoti": dcHumidityHighNoti,
       "dcHumidityLowNoti": dcHumidityLowNoti,
       "sysRebootMaxDcTempNoti": sysRebootMaxDcTempNoti,
       "sysRebootMaxHumidNoti": sysRebootMaxHumidNoti,
       "sysRebootMaxDcHumidNoti": sysRebootMaxDcHumidNoti,
       "fanSpeedHighNoti": fanSpeedHighNoti,
       "psuUnequipNoti": psuUnequipNoti,
       "doorOpenAlarmNoti": doorOpenAlarmNoti,
       "ExternalMajorAlarm": ExternalMajorAlarm,
       "Piu10gFanFailAlarm": Piu10gFanFailAlarm}
)
