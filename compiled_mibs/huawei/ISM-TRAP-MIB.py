# SNMP MIB module (ISM-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\huawei\ISM-TRAP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:59:56 2025
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

huaweistorage = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 34774)
)
if mibBuilder.loadTexts:
    huaweistorage.setRevisions(
        ("2013-04-07 19:15",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class NodeCodeString(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 17),
    )



# MIB Managed Objects in the order of their OIDs

_HwStorage_ObjectIdentity = ObjectIdentity
hwStorage = _HwStorage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34774, 4)
)
_HwISM_ObjectIdentity = ObjectIdentity
hwISM = _HwISM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1)
)
_TrapAddress_ObjectIdentity = ObjectIdentity
trapAddress = _TrapAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 2)
)
_ForwardAddrTable_Object = MibTable
forwardAddrTable = _ForwardAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    forwardAddrTable.setStatus("current")
_ForwardAddrEntry_Object = MibTableRow
forwardAddrEntry = _ForwardAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 2, 1, 1)
)
forwardAddrEntry.setIndexNames(
    (0, "ISM-TRAP-MIB", "forwardAddrIndex"),
)
if mibBuilder.loadTexts:
    forwardAddrEntry.setStatus("current")
_ForwardAddrIndex_Type = OctetString
_ForwardAddrIndex_Object = MibTableColumn
forwardAddrIndex = _ForwardAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 2, 1, 1, 1),
    _ForwardAddrIndex_Type()
)
forwardAddrIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    forwardAddrIndex.setStatus("current")
_ForwardAddrIP_Type = IpAddress
_ForwardAddrIP_Object = MibTableColumn
forwardAddrIP = _ForwardAddrIP_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 2, 1, 1, 2),
    _ForwardAddrIP_Type()
)
forwardAddrIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    forwardAddrIP.setStatus("current")
_ForwardAddrPort_Type = Gauge32
_ForwardAddrPort_Object = MibTableColumn
forwardAddrPort = _ForwardAddrPort_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 2, 1, 1, 3),
    _ForwardAddrPort_Type()
)
forwardAddrPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    forwardAddrPort.setStatus("current")
_ForwardAddrTrapVer_Type = Integer32
_ForwardAddrTrapVer_Object = MibTableColumn
forwardAddrTrapVer = _ForwardAddrTrapVer_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 2, 1, 1, 4),
    _ForwardAddrTrapVer_Type()
)
forwardAddrTrapVer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    forwardAddrTrapVer.setStatus("current")
_ForwardAddrRowStatus_Type = RowStatus
_ForwardAddrRowStatus_Object = MibTableColumn
forwardAddrRowStatus = _ForwardAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 2, 1, 1, 5),
    _ForwardAddrRowStatus_Type()
)
forwardAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    forwardAddrRowStatus.setStatus("current")
_ForwardAddrIPNew_Type = OctetString
_ForwardAddrIPNew_Object = MibTableColumn
forwardAddrIPNew = _ForwardAddrIPNew_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 2, 1, 1, 6),
    _ForwardAddrIPNew_Type()
)
forwardAddrIPNew.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    forwardAddrIPNew.setStatus("current")
_ForwardAddrTrapType_Type = Integer32
_ForwardAddrTrapType_Object = MibTableColumn
forwardAddrTrapType = _ForwardAddrTrapType_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 2, 1, 1, 7),
    _ForwardAddrTrapType_Type()
)
forwardAddrTrapType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    forwardAddrTrapType.setStatus("current")
_Event_ObjectIdentity = ObjectIdentity
event = _Event_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 3)
)
_EventTable_Object = MibTable
eventTable = _EventTable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 3, 1)
)
if mibBuilder.loadTexts:
    eventTable.setStatus("current")
_EventEntry_Object = MibTableRow
eventEntry = _EventEntry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 3, 1, 1)
)
eventEntry.setIndexNames(
    (0, "ISM-TRAP-MIB", "hwIsmEventSequence"),
)
if mibBuilder.loadTexts:
    eventEntry.setStatus("current")
_HwIsmEventType_Type = Unsigned32
_HwIsmEventType_Object = MibTableColumn
hwIsmEventType = _HwIsmEventType_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 3, 1, 1, 1),
    _HwIsmEventType_Type()
)
hwIsmEventType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIsmEventType.setStatus("current")
_HwIsmEventID_Type = Counter64
_HwIsmEventID_Object = MibTableColumn
hwIsmEventID = _HwIsmEventID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 3, 1, 1, 2),
    _HwIsmEventID_Type()
)
hwIsmEventID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIsmEventID.setStatus("current")
_HwIsmEventLevel_Type = Unsigned32
_HwIsmEventLevel_Object = MibTableColumn
hwIsmEventLevel = _HwIsmEventLevel_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 3, 1, 1, 3),
    _HwIsmEventLevel_Type()
)
hwIsmEventLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIsmEventLevel.setStatus("current")
_HwIsmEventSequence_Type = Unsigned32
_HwIsmEventSequence_Object = MibTableColumn
hwIsmEventSequence = _HwIsmEventSequence_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 3, 1, 1, 4),
    _HwIsmEventSequence_Type()
)
hwIsmEventSequence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIsmEventSequence.setStatus("current")
_HwIsmEventTime_Type = Unsigned32
_HwIsmEventTime_Object = MibTableColumn
hwIsmEventTime = _HwIsmEventTime_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 3, 1, 1, 5),
    _HwIsmEventTime_Type()
)
hwIsmEventTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIsmEventTime.setStatus("current")
_HwIsmEventRecoveryTime_Type = Unsigned32
_HwIsmEventRecoveryTime_Object = MibTableColumn
hwIsmEventRecoveryTime = _HwIsmEventRecoveryTime_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 3, 1, 1, 6),
    _HwIsmEventRecoveryTime_Type()
)
hwIsmEventRecoveryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIsmEventRecoveryTime.setStatus("current")
_HwIsmEventParameter_Type = OctetString
_HwIsmEventParameter_Object = MibTableColumn
hwIsmEventParameter = _HwIsmEventParameter_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 3, 1, 1, 7),
    _HwIsmEventParameter_Type()
)
hwIsmEventParameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIsmEventParameter.setStatus("current")
_HwIsmEventRowStatus_Type = RowStatus
_HwIsmEventRowStatus_Object = MibTableColumn
hwIsmEventRowStatus = _HwIsmEventRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 3, 1, 1, 20),
    _HwIsmEventRowStatus_Type()
)
hwIsmEventRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIsmEventRowStatus.setStatus("current")
_TrapEvent_ObjectIdentity = ObjectIdentity
trapEvent = _TrapEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 3, 3)
)
_HwIsmTrapEventType_Type = Unsigned32
_HwIsmTrapEventType_Object = MibScalar
hwIsmTrapEventType = _HwIsmTrapEventType_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 3, 3, 1),
    _HwIsmTrapEventType_Type()
)
hwIsmTrapEventType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIsmTrapEventType.setStatus("current")
_HwIsmTrapEventID_Type = Counter64
_HwIsmTrapEventID_Object = MibScalar
hwIsmTrapEventID = _HwIsmTrapEventID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 3, 3, 2),
    _HwIsmTrapEventID_Type()
)
hwIsmTrapEventID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIsmTrapEventID.setStatus("current")
_HwIsmTrapEventLevel_Type = Unsigned32
_HwIsmTrapEventLevel_Object = MibScalar
hwIsmTrapEventLevel = _HwIsmTrapEventLevel_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 3, 3, 3),
    _HwIsmTrapEventLevel_Type()
)
hwIsmTrapEventLevel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIsmTrapEventLevel.setStatus("current")
_HwIsmTrapEventSequence_Type = Unsigned32
_HwIsmTrapEventSequence_Object = MibScalar
hwIsmTrapEventSequence = _HwIsmTrapEventSequence_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 3, 3, 4),
    _HwIsmTrapEventSequence_Type()
)
hwIsmTrapEventSequence.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIsmTrapEventSequence.setStatus("current")
_HwIsmTrapEventTime_Type = Unsigned32
_HwIsmTrapEventTime_Object = MibScalar
hwIsmTrapEventTime = _HwIsmTrapEventTime_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 3, 3, 5),
    _HwIsmTrapEventTime_Type()
)
hwIsmTrapEventTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIsmTrapEventTime.setStatus("current")
_HwIsmTrapEventRecoveryTime_Type = Unsigned32
_HwIsmTrapEventRecoveryTime_Object = MibScalar
hwIsmTrapEventRecoveryTime = _HwIsmTrapEventRecoveryTime_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 3, 3, 6),
    _HwIsmTrapEventRecoveryTime_Type()
)
hwIsmTrapEventRecoveryTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIsmTrapEventRecoveryTime.setStatus("current")
_HwIsmTrapEventParameter_Type = OctetString
_HwIsmTrapEventParameter_Object = MibScalar
hwIsmTrapEventParameter = _HwIsmTrapEventParameter_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 3, 3, 7),
    _HwIsmTrapEventParameter_Type()
)
hwIsmTrapEventParameter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIsmTrapEventParameter.setStatus("current")
_HwIsmTrapEventID32Bit_Type = Unsigned32
_HwIsmTrapEventID32Bit_Object = MibScalar
hwIsmTrapEventID32Bit = _HwIsmTrapEventID32Bit_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 3, 3, 8),
    _HwIsmTrapEventID32Bit_Type()
)
hwIsmTrapEventID32Bit.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIsmTrapEventID32Bit.setStatus("current")
_HwIsmTrapEventTimeStr_Type = OctetString
_HwIsmTrapEventTimeStr_Object = MibScalar
hwIsmTrapEventTimeStr = _HwIsmTrapEventTimeStr_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 3, 3, 9),
    _HwIsmTrapEventTimeStr_Type()
)
hwIsmTrapEventTimeStr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIsmTrapEventTimeStr.setStatus("current")
_HwIsmTrapEventRecoveryTimeStr_Type = OctetString
_HwIsmTrapEventRecoveryTimeStr_Object = MibScalar
hwIsmTrapEventRecoveryTimeStr = _HwIsmTrapEventRecoveryTimeStr_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 3, 3, 10),
    _HwIsmTrapEventRecoveryTimeStr_Type()
)
hwIsmTrapEventRecoveryTimeStr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIsmTrapEventRecoveryTimeStr.setStatus("current")
_NotificationType_ObjectIdentity = ObjectIdentity
notificationType = _NotificationType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 4)
)
_IsoConformance_ObjectIdentity = ObjectIdentity
isoConformance = _IsoConformance_ObjectIdentity(
    (1, 6)
)
_IsoGroups_ObjectIdentity = ObjectIdentity
isoGroups = _IsoGroups_ObjectIdentity(
    (1, 6, 1)
)
_IsoCompliances_ObjectIdentity = ObjectIdentity
isoCompliances = _IsoCompliances_ObjectIdentity(
    (1, 6, 2)
)

# Managed Objects groups

currentObjectGroup = ObjectGroup(
    (1, 6, 1, 1)
)
currentObjectGroup.setObjects(
      *(("ISM-TRAP-MIB", "forwardAddrIndex"),
        ("ISM-TRAP-MIB", "forwardAddrIP"),
        ("ISM-TRAP-MIB", "forwardAddrPort"),
        ("ISM-TRAP-MIB", "forwardAddrTrapVer"),
        ("ISM-TRAP-MIB", "forwardAddrRowStatus"),
        ("ISM-TRAP-MIB", "hwIsmTrapEventType"),
        ("ISM-TRAP-MIB", "hwIsmTrapEventID"),
        ("ISM-TRAP-MIB", "hwIsmTrapEventLevel"),
        ("ISM-TRAP-MIB", "hwIsmTrapEventSequence"),
        ("ISM-TRAP-MIB", "hwIsmTrapEventTime"),
        ("ISM-TRAP-MIB", "hwIsmTrapEventRecoveryTime"),
        ("ISM-TRAP-MIB", "forwardAddrIPNew"),
        ("ISM-TRAP-MIB", "forwardAddrTrapType"),
        ("ISM-TRAP-MIB", "hwIsmTrapEventID32Bit"),
        ("ISM-TRAP-MIB", "hwIsmTrapEventTimeStr"),
        ("ISM-TRAP-MIB", "hwIsmTrapEventRecoveryTimeStr"),
        ("ISM-TRAP-MIB", "hwIsmTrapEventParameter"),
        ("ISM-TRAP-MIB", "hwIsmEventType"),
        ("ISM-TRAP-MIB", "hwIsmEventID"),
        ("ISM-TRAP-MIB", "hwIsmEventLevel"),
        ("ISM-TRAP-MIB", "hwIsmEventSequence"),
        ("ISM-TRAP-MIB", "hwIsmEventTime"),
        ("ISM-TRAP-MIB", "hwIsmEventRecoveryTime"),
        ("ISM-TRAP-MIB", "hwIsmEventParameter"),
        ("ISM-TRAP-MIB", "hwIsmEventRowStatus"))
)
if mibBuilder.loadTexts:
    currentObjectGroup.setStatus("current")


# Notification objects

eventType = NotificationType(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 4, 2)
)
eventType.setObjects(
      *(("ISM-TRAP-MIB", "hwIsmTrapEventType"),
        ("ISM-TRAP-MIB", "hwIsmTrapEventID"),
        ("ISM-TRAP-MIB", "hwIsmTrapEventLevel"),
        ("ISM-TRAP-MIB", "hwIsmTrapEventSequence"),
        ("ISM-TRAP-MIB", "hwIsmTrapEventTime"),
        ("ISM-TRAP-MIB", "hwIsmTrapEventRecoveryTime"),
        ("ISM-TRAP-MIB", "hwIsmTrapEventParameter"))
)
if mibBuilder.loadTexts:
    eventType.setStatus(
        "current"
    )


# Notifications groups

currentNotificationGroup = NotificationGroup(
    (1, 6, 1, 2)
)
currentNotificationGroup.setObjects(
    ("ISM-TRAP-MIB", "eventType")
)
if mibBuilder.loadTexts:
    currentNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

basicCompliance = ModuleCompliance(
    (1, 6, 2, 1)
)
basicCompliance.setObjects(
      *(("ISM-TRAP-MIB", "currentObjectGroup"),
        ("ISM-TRAP-MIB", "currentNotificationGroup"))
)
if mibBuilder.loadTexts:
    basicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ISM-TRAP-MIB",
    **{"NodeCodeString": NodeCodeString,
       "huaweistorage": huaweistorage,
       "hwStorage": hwStorage,
       "hwISM": hwISM,
       "trapAddress": trapAddress,
       "forwardAddrTable": forwardAddrTable,
       "forwardAddrEntry": forwardAddrEntry,
       "forwardAddrIndex": forwardAddrIndex,
       "forwardAddrIP": forwardAddrIP,
       "forwardAddrPort": forwardAddrPort,
       "forwardAddrTrapVer": forwardAddrTrapVer,
       "forwardAddrRowStatus": forwardAddrRowStatus,
       "forwardAddrIPNew": forwardAddrIPNew,
       "forwardAddrTrapType": forwardAddrTrapType,
       "event": event,
       "eventTable": eventTable,
       "eventEntry": eventEntry,
       "hwIsmEventType": hwIsmEventType,
       "hwIsmEventID": hwIsmEventID,
       "hwIsmEventLevel": hwIsmEventLevel,
       "hwIsmEventSequence": hwIsmEventSequence,
       "hwIsmEventTime": hwIsmEventTime,
       "hwIsmEventRecoveryTime": hwIsmEventRecoveryTime,
       "hwIsmEventParameter": hwIsmEventParameter,
       "hwIsmEventRowStatus": hwIsmEventRowStatus,
       "trapEvent": trapEvent,
       "hwIsmTrapEventType": hwIsmTrapEventType,
       "hwIsmTrapEventID": hwIsmTrapEventID,
       "hwIsmTrapEventLevel": hwIsmTrapEventLevel,
       "hwIsmTrapEventSequence": hwIsmTrapEventSequence,
       "hwIsmTrapEventTime": hwIsmTrapEventTime,
       "hwIsmTrapEventRecoveryTime": hwIsmTrapEventRecoveryTime,
       "hwIsmTrapEventParameter": hwIsmTrapEventParameter,
       "hwIsmTrapEventID32Bit": hwIsmTrapEventID32Bit,
       "hwIsmTrapEventTimeStr": hwIsmTrapEventTimeStr,
       "hwIsmTrapEventRecoveryTimeStr": hwIsmTrapEventRecoveryTimeStr,
       "notificationType": notificationType,
       "eventType": eventType,
       "isoConformance": isoConformance,
       "isoGroups": isoGroups,
       "currentObjectGroup": currentObjectGroup,
       "currentNotificationGroup": currentNotificationGroup,
       "isoCompliances": isoCompliances,
       "basicCompliance": basicCompliance}
)
