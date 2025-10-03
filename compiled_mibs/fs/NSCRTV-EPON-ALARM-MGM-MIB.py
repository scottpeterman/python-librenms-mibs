# SNMP MIB module (NSCRTV-EPON-ALARM-MGM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fs\NSCRTV-EPON-ALARM-MGM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:46:50 2025
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

(AutoNegotiationTechAbility,
 EponAlarmCode,
 EponAlarmInstance,
 EponCardIndex,
 EponDeviceIndex,
 EponPortIndex,
 EponSeverityType,
 EponStats15MinRecordType,
 EponStats24HourRecordType,
 EponStatsThresholdType,
 TAddress,
 eponAlarmObjGroup,
 eponAlarmTree,
 eponManagementObjGroup,
 eponTrapObjectGroup) = mibBuilder.importSymbols(
    "NSCRTV-EPONEOC-EPON-MIB",
    "AutoNegotiationTechAbility",
    "EponAlarmCode",
    "EponAlarmInstance",
    "EponCardIndex",
    "EponDeviceIndex",
    "EponPortIndex",
    "EponSeverityType",
    "EponStats15MinRecordType",
    "EponStats24HourRecordType",
    "EponStatsThresholdType",
    "TAddress",
    "eponAlarmObjGroup",
    "eponAlarmTree",
    "eponManagementObjGroup",
    "eponTrapObjectGroup")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EponNotifications_ObjectIdentity = ObjectIdentity
eponNotifications = _EponNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 1, 1)
)
_EponTrapObjects_ObjectIdentity = ObjectIdentity
eponTrapObjects = _EponTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 1, 2)
)
_EponTrapInstance_Type = EponAlarmInstance
_EponTrapInstance_Object = MibScalar
eponTrapInstance = _EponTrapInstance_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 1, 2, 1),
    _EponTrapInstance_Type()
)
eponTrapInstance.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eponTrapInstance.setStatus("current")
_EponTrapCorrelationId_Type = Unsigned32
_EponTrapCorrelationId_Object = MibScalar
eponTrapCorrelationId = _EponTrapCorrelationId_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 1, 2, 2),
    _EponTrapCorrelationId_Type()
)
eponTrapCorrelationId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eponTrapCorrelationId.setStatus("current")


class _EponTrapAdditionalText_Type(OctetString):
    """Custom type eponTrapAdditionalText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_EponTrapAdditionalText_Type.__name__ = "OctetString"
_EponTrapAdditionalText_Object = MibScalar
eponTrapAdditionalText = _EponTrapAdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 1, 2, 3),
    _EponTrapAdditionalText_Type()
)
eponTrapAdditionalText.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eponTrapAdditionalText.setStatus("current")
_EponTrapCode_Type = EponAlarmCode
_EponTrapCode_Object = MibScalar
eponTrapCode = _EponTrapCode_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 1, 2, 4),
    _EponTrapCode_Type()
)
eponTrapCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eponTrapCode.setStatus("current")
_EponTrapSeverity_Type = EponSeverityType
_EponTrapSeverity_Object = MibScalar
eponTrapSeverity = _EponTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 1, 2, 5),
    _EponTrapSeverity_Type()
)
eponTrapSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eponTrapSeverity.setStatus("current")
_EponTrapOccurTime_Type = DateAndTime
_EponTrapOccurTime_Object = MibScalar
eponTrapOccurTime = _EponTrapOccurTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 1, 2, 6),
    _EponTrapOccurTime_Type()
)
eponTrapOccurTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eponTrapOccurTime.setStatus("current")
_EponTrapSequenceNumber_Type = Unsigned32
_EponTrapSequenceNumber_Object = MibScalar
eponTrapSequenceNumber = _EponTrapSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 1, 2, 7),
    _EponTrapSequenceNumber_Type()
)
eponTrapSequenceNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eponTrapSequenceNumber.setStatus("current")
_ActiveAlarmTable_Object = MibTable
activeAlarmTable = _ActiveAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 1)
)
if mibBuilder.loadTexts:
    activeAlarmTable.setStatus("current")
_ActiveAlarmEntry_Object = MibTableRow
activeAlarmEntry = _ActiveAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 1, 1)
)
activeAlarmEntry.setIndexNames(
    (0, "NSCRTV-EPON-ALARM-MGM-MIB", "activeAlarmSeqNum"),
    (0, "NSCRTV-EPON-ALARM-MGM-MIB", "activeAlarmRaisingNumber"),
)
if mibBuilder.loadTexts:
    activeAlarmEntry.setStatus("current")
_ActiveAlarmSeqNum_Type = Unsigned32
_ActiveAlarmSeqNum_Object = MibTableColumn
activeAlarmSeqNum = _ActiveAlarmSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 1, 1, 1),
    _ActiveAlarmSeqNum_Type()
)
activeAlarmSeqNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    activeAlarmSeqNum.setStatus("current")
_ActiveAlarmCode_Type = EponAlarmCode
_ActiveAlarmCode_Object = MibTableColumn
activeAlarmCode = _ActiveAlarmCode_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 1, 1, 2),
    _ActiveAlarmCode_Type()
)
activeAlarmCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeAlarmCode.setStatus("current")
_ActiveAlarmInstance_Type = EponAlarmInstance
_ActiveAlarmInstance_Object = MibTableColumn
activeAlarmInstance = _ActiveAlarmInstance_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 1, 1, 3),
    _ActiveAlarmInstance_Type()
)
activeAlarmInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeAlarmInstance.setStatus("current")
_ActiveAlarmSeverity_Type = EponSeverityType
_ActiveAlarmSeverity_Object = MibTableColumn
activeAlarmSeverity = _ActiveAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 1, 1, 4),
    _ActiveAlarmSeverity_Type()
)
activeAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeAlarmSeverity.setStatus("current")
_ActiveAlarmRaisingNumber_Type = Unsigned32
_ActiveAlarmRaisingNumber_Object = MibTableColumn
activeAlarmRaisingNumber = _ActiveAlarmRaisingNumber_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 1, 1, 5),
    _ActiveAlarmRaisingNumber_Type()
)
activeAlarmRaisingNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    activeAlarmRaisingNumber.setStatus("current")
_ActiveAlarmFirstOccurTime_Type = DateAndTime
_ActiveAlarmFirstOccurTime_Object = MibTableColumn
activeAlarmFirstOccurTime = _ActiveAlarmFirstOccurTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 1, 1, 6),
    _ActiveAlarmFirstOccurTime_Type()
)
activeAlarmFirstOccurTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeAlarmFirstOccurTime.setStatus("current")
_ActiveAlarmLastOccurTime_Type = DateAndTime
_ActiveAlarmLastOccurTime_Object = MibTableColumn
activeAlarmLastOccurTime = _ActiveAlarmLastOccurTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 1, 1, 7),
    _ActiveAlarmLastOccurTime_Type()
)
activeAlarmLastOccurTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeAlarmLastOccurTime.setStatus("current")
_ActiveAlarmRepeats_Type = Counter32
_ActiveAlarmRepeats_Object = MibTableColumn
activeAlarmRepeats = _ActiveAlarmRepeats_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 1, 1, 8),
    _ActiveAlarmRepeats_Type()
)
activeAlarmRepeats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeAlarmRepeats.setStatus("current")
_ActiveAlarmConfirm_Type = TruthValue
_ActiveAlarmConfirm_Object = MibTableColumn
activeAlarmConfirm = _ActiveAlarmConfirm_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 1, 1, 9),
    _ActiveAlarmConfirm_Type()
)
activeAlarmConfirm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    activeAlarmConfirm.setStatus("current")


class _ActiveAlarmAdditionalText_Type(OctetString):
    """Custom type activeAlarmAdditionalText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_ActiveAlarmAdditionalText_Type.__name__ = "OctetString"
_ActiveAlarmAdditionalText_Object = MibTableColumn
activeAlarmAdditionalText = _ActiveAlarmAdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 1, 1, 10),
    _ActiveAlarmAdditionalText_Type()
)
activeAlarmAdditionalText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeAlarmAdditionalText.setStatus("current")
_HistoryAlarmTable_Object = MibTable
historyAlarmTable = _HistoryAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 2)
)
if mibBuilder.loadTexts:
    historyAlarmTable.setStatus("current")
_HistoryAlarmEntry_Object = MibTableRow
historyAlarmEntry = _HistoryAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 2, 1)
)
historyAlarmEntry.setIndexNames(
    (0, "NSCRTV-EPON-ALARM-MGM-MIB", "historyAlarmSeqNum"),
    (0, "NSCRTV-EPON-ALARM-MGM-MIB", "historyAlarmRaisingNumber"),
)
if mibBuilder.loadTexts:
    historyAlarmEntry.setStatus("current")
_HistoryAlarmSeqNum_Type = Unsigned32
_HistoryAlarmSeqNum_Object = MibTableColumn
historyAlarmSeqNum = _HistoryAlarmSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 2, 1, 1),
    _HistoryAlarmSeqNum_Type()
)
historyAlarmSeqNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    historyAlarmSeqNum.setStatus("current")
_HistoryAlarmCode_Type = EponAlarmCode
_HistoryAlarmCode_Object = MibTableColumn
historyAlarmCode = _HistoryAlarmCode_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 2, 1, 2),
    _HistoryAlarmCode_Type()
)
historyAlarmCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyAlarmCode.setStatus("current")
_HistoryAlarmInstance_Type = EponAlarmInstance
_HistoryAlarmInstance_Object = MibTableColumn
historyAlarmInstance = _HistoryAlarmInstance_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 2, 1, 3),
    _HistoryAlarmInstance_Type()
)
historyAlarmInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyAlarmInstance.setStatus("current")
_HistoryAlarmSeverity_Type = EponSeverityType
_HistoryAlarmSeverity_Object = MibTableColumn
historyAlarmSeverity = _HistoryAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 2, 1, 4),
    _HistoryAlarmSeverity_Type()
)
historyAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyAlarmSeverity.setStatus("current")
_HistoryAlarmRaisingNumber_Type = Unsigned32
_HistoryAlarmRaisingNumber_Object = MibTableColumn
historyAlarmRaisingNumber = _HistoryAlarmRaisingNumber_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 2, 1, 5),
    _HistoryAlarmRaisingNumber_Type()
)
historyAlarmRaisingNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    historyAlarmRaisingNumber.setStatus("current")
_HistoryAlarmFirstOccurTime_Type = DateAndTime
_HistoryAlarmFirstOccurTime_Object = MibTableColumn
historyAlarmFirstOccurTime = _HistoryAlarmFirstOccurTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 2, 1, 6),
    _HistoryAlarmFirstOccurTime_Type()
)
historyAlarmFirstOccurTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyAlarmFirstOccurTime.setStatus("current")
_HistoryAlarmLastOccurTime_Type = DateAndTime
_HistoryAlarmLastOccurTime_Object = MibTableColumn
historyAlarmLastOccurTime = _HistoryAlarmLastOccurTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 2, 1, 7),
    _HistoryAlarmLastOccurTime_Type()
)
historyAlarmLastOccurTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyAlarmLastOccurTime.setStatus("current")
_HistoryAlarmRepeats_Type = Counter32
_HistoryAlarmRepeats_Object = MibTableColumn
historyAlarmRepeats = _HistoryAlarmRepeats_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 2, 1, 8),
    _HistoryAlarmRepeats_Type()
)
historyAlarmRepeats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyAlarmRepeats.setStatus("current")
_HistoryAlarmCorrelationId_Type = Unsigned32
_HistoryAlarmCorrelationId_Object = MibTableColumn
historyAlarmCorrelationId = _HistoryAlarmCorrelationId_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 2, 1, 9),
    _HistoryAlarmCorrelationId_Type()
)
historyAlarmCorrelationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyAlarmCorrelationId.setStatus("current")


class _HistoryAlarmAdditionalText_Type(OctetString):
    """Custom type historyAlarmAdditionalText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HistoryAlarmAdditionalText_Type.__name__ = "OctetString"
_HistoryAlarmAdditionalText_Object = MibTableColumn
historyAlarmAdditionalText = _HistoryAlarmAdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 2, 1, 10),
    _HistoryAlarmAdditionalText_Type()
)
historyAlarmAdditionalText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyAlarmAdditionalText.setStatus("current")
_HistoryAlarmClearTime_Type = DateAndTime
_HistoryAlarmClearTime_Object = MibTableColumn
historyAlarmClearTime = _HistoryAlarmClearTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 2, 1, 11),
    _HistoryAlarmClearTime_Type()
)
historyAlarmClearTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyAlarmClearTime.setStatus("current")
_EventLogTable_Object = MibTable
eventLogTable = _EventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 3)
)
if mibBuilder.loadTexts:
    eventLogTable.setStatus("current")
_EventLogEntry_Object = MibTableRow
eventLogEntry = _EventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 3, 1)
)
eventLogEntry.setIndexNames(
    (0, "NSCRTV-EPON-ALARM-MGM-MIB", "eventSeqNum"),
)
if mibBuilder.loadTexts:
    eventLogEntry.setStatus("current")
_EventSeqNum_Type = Unsigned32
_EventSeqNum_Object = MibTableColumn
eventSeqNum = _EventSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 3, 1, 1),
    _EventSeqNum_Type()
)
eventSeqNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eventSeqNum.setStatus("current")
_EventCode_Type = EponAlarmCode
_EventCode_Object = MibTableColumn
eventCode = _EventCode_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 3, 1, 2),
    _EventCode_Type()
)
eventCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventCode.setStatus("current")
_EventInstance_Type = EponAlarmInstance
_EventInstance_Object = MibTableColumn
eventInstance = _EventInstance_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 3, 1, 3),
    _EventInstance_Type()
)
eventInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventInstance.setStatus("current")
_EventOccurTime_Type = DateAndTime
_EventOccurTime_Object = MibTableColumn
eventOccurTime = _EventOccurTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 3, 1, 4),
    _EventOccurTime_Type()
)
eventOccurTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventOccurTime.setStatus("current")


class _EventAdditionalText_Type(OctetString):
    """Custom type eventAdditionalText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_EventAdditionalText_Type.__name__ = "OctetString"
_EventAdditionalText_Object = MibTableColumn
eventAdditionalText = _EventAdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 3, 1, 5),
    _EventAdditionalText_Type()
)
eventAdditionalText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventAdditionalText.setStatus("current")
_EponManagementAddrTable_Object = MibTable
eponManagementAddrTable = _EponManagementAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 3, 1)
)
if mibBuilder.loadTexts:
    eponManagementAddrTable.setStatus("current")
_EponManagementAddrEntry_Object = MibTableRow
eponManagementAddrEntry = _EponManagementAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 3, 1, 1)
)
eponManagementAddrEntry.setIndexNames(
    (0, "NSCRTV-EPON-ALARM-MGM-MIB", "eponManagementAddrName"),
)
if mibBuilder.loadTexts:
    eponManagementAddrEntry.setStatus("current")


class _EponManagementAddrName_Type(OctetString):
    """Custom type eponManagementAddrName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_EponManagementAddrName_Type.__name__ = "OctetString"
_EponManagementAddrName_Object = MibTableColumn
eponManagementAddrName = _EponManagementAddrName_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 3, 1, 1, 1),
    _EponManagementAddrName_Type()
)
eponManagementAddrName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eponManagementAddrName.setStatus("current")
_EponManagementAddrTAddress_Type = TAddress
_EponManagementAddrTAddress_Object = MibTableColumn
eponManagementAddrTAddress = _EponManagementAddrTAddress_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 3, 1, 1, 2),
    _EponManagementAddrTAddress_Type()
)
eponManagementAddrTAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponManagementAddrTAddress.setStatus("current")


class _EponManagementAddrCommunity_Type(OctetString):
    """Custom type eponManagementAddrCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EponManagementAddrCommunity_Type.__name__ = "OctetString"
_EponManagementAddrCommunity_Object = MibTableColumn
eponManagementAddrCommunity = _EponManagementAddrCommunity_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 3, 1, 1, 3),
    _EponManagementAddrCommunity_Type()
)
eponManagementAddrCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponManagementAddrCommunity.setStatus("current")
_EponManagementAddrRowStatus_Type = RowStatus
_EponManagementAddrRowStatus_Object = MibTableColumn
eponManagementAddrRowStatus = _EponManagementAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 3, 1, 1, 4),
    _EponManagementAddrRowStatus_Type()
)
eponManagementAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponManagementAddrRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects

eponAlarmNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 1, 1, 1)
)
eponAlarmNotification.setObjects(
      *(("NSCRTV-EPON-ALARM-MGM-MIB", "eponTrapSequenceNumber"),
        ("NSCRTV-EPON-ALARM-MGM-MIB", "eponTrapOccurTime"),
        ("NSCRTV-EPON-ALARM-MGM-MIB", "eponTrapCode"),
        ("NSCRTV-EPON-ALARM-MGM-MIB", "eponTrapInstance"),
        ("NSCRTV-EPON-ALARM-MGM-MIB", "eponTrapSeverity"),
        ("NSCRTV-EPON-ALARM-MGM-MIB", "eponTrapCorrelationId"),
        ("NSCRTV-EPON-ALARM-MGM-MIB", "eponTrapAdditionalText"))
)
if mibBuilder.loadTexts:
    eponAlarmNotification.setStatus(
        "current"
    )

eponEventNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 1, 1, 2)
)
eponEventNotification.setObjects(
      *(("NSCRTV-EPON-ALARM-MGM-MIB", "eponTrapSequenceNumber"),
        ("NSCRTV-EPON-ALARM-MGM-MIB", "eponTrapOccurTime"),
        ("NSCRTV-EPON-ALARM-MGM-MIB", "eponTrapCode"),
        ("NSCRTV-EPON-ALARM-MGM-MIB", "eponTrapInstance"),
        ("NSCRTV-EPON-ALARM-MGM-MIB", "eponTrapAdditionalText"))
)
if mibBuilder.loadTexts:
    eponEventNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NSCRTV-EPON-ALARM-MGM-MIB",
    **{"eponNotifications": eponNotifications,
       "eponAlarmNotification": eponAlarmNotification,
       "eponEventNotification": eponEventNotification,
       "eponTrapObjects": eponTrapObjects,
       "eponTrapInstance": eponTrapInstance,
       "eponTrapCorrelationId": eponTrapCorrelationId,
       "eponTrapAdditionalText": eponTrapAdditionalText,
       "eponTrapCode": eponTrapCode,
       "eponTrapSeverity": eponTrapSeverity,
       "eponTrapOccurTime": eponTrapOccurTime,
       "eponTrapSequenceNumber": eponTrapSequenceNumber,
       "activeAlarmTable": activeAlarmTable,
       "activeAlarmEntry": activeAlarmEntry,
       "activeAlarmSeqNum": activeAlarmSeqNum,
       "activeAlarmCode": activeAlarmCode,
       "activeAlarmInstance": activeAlarmInstance,
       "activeAlarmSeverity": activeAlarmSeverity,
       "activeAlarmRaisingNumber": activeAlarmRaisingNumber,
       "activeAlarmFirstOccurTime": activeAlarmFirstOccurTime,
       "activeAlarmLastOccurTime": activeAlarmLastOccurTime,
       "activeAlarmRepeats": activeAlarmRepeats,
       "activeAlarmConfirm": activeAlarmConfirm,
       "activeAlarmAdditionalText": activeAlarmAdditionalText,
       "historyAlarmTable": historyAlarmTable,
       "historyAlarmEntry": historyAlarmEntry,
       "historyAlarmSeqNum": historyAlarmSeqNum,
       "historyAlarmCode": historyAlarmCode,
       "historyAlarmInstance": historyAlarmInstance,
       "historyAlarmSeverity": historyAlarmSeverity,
       "historyAlarmRaisingNumber": historyAlarmRaisingNumber,
       "historyAlarmFirstOccurTime": historyAlarmFirstOccurTime,
       "historyAlarmLastOccurTime": historyAlarmLastOccurTime,
       "historyAlarmRepeats": historyAlarmRepeats,
       "historyAlarmCorrelationId": historyAlarmCorrelationId,
       "historyAlarmAdditionalText": historyAlarmAdditionalText,
       "historyAlarmClearTime": historyAlarmClearTime,
       "eventLogTable": eventLogTable,
       "eventLogEntry": eventLogEntry,
       "eventSeqNum": eventSeqNum,
       "eventCode": eventCode,
       "eventInstance": eventInstance,
       "eventOccurTime": eventOccurTime,
       "eventAdditionalText": eventAdditionalText,
       "eponManagementAddrTable": eponManagementAddrTable,
       "eponManagementAddrEntry": eponManagementAddrEntry,
       "eponManagementAddrName": eponManagementAddrName,
       "eponManagementAddrTAddress": eponManagementAddrTAddress,
       "eponManagementAddrCommunity": eponManagementAddrCommunity,
       "eponManagementAddrRowStatus": eponManagementAddrRowStatus}
)
