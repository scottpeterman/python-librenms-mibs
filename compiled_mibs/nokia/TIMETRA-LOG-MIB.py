# SNMP MIB module (TIMETRA-LOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\TIMETRA-LOG-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:17:16 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,
 SnmpMessageProcessingModel,
 SnmpSecurityLevel) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString",
    "SnmpMessageProcessingModel",
    "SnmpSecurityLevel")

(snmpNotifyEntry,) = mibBuilder.importSymbols(
    "SNMP-NOTIFICATION-MIB",
    "snmpNotifyEntry")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysDescr,
 sysObjectID) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysDescr",
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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(TFilterAction,
 TFilterActionOrDefault) = mibBuilder.importSymbols(
    "TIMETRA-FILTER-MIB",
    "TFilterAction",
    "TFilterActionOrDefault")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(THsmdaCounterIdOrZero,
 THsmdaCounterIdOrZeroOrAll,
 TItemDescription,
 TLNamedItemOrEmpty,
 TNamedItem,
 TNamedItemOrEmpty,
 TQueueId,
 TQueueIdOrAll,
 TmnxAccPlcyAACounters,
 TmnxAccPlcyAASubAttributes,
 TmnxAccPlcyOECounters,
 TmnxAccPlcyOICounters,
 TmnxAccPlcyPolicerECounters,
 TmnxAccPlcyPolicerICounters,
 TmnxAccPlcyQECounters,
 TmnxAccPlcyQICounters,
 TmnxActionType,
 TmnxAdminState,
 TmnxOperState,
 TmnxSyslogFacility,
 TmnxSyslogSeverity,
 TmnxUdpPort) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "THsmdaCounterIdOrZero",
    "THsmdaCounterIdOrZeroOrAll",
    "TItemDescription",
    "TLNamedItemOrEmpty",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TQueueId",
    "TQueueIdOrAll",
    "TmnxAccPlcyAACounters",
    "TmnxAccPlcyAASubAttributes",
    "TmnxAccPlcyOECounters",
    "TmnxAccPlcyOICounters",
    "TmnxAccPlcyPolicerECounters",
    "TmnxAccPlcyPolicerICounters",
    "TmnxAccPlcyQECounters",
    "TmnxAccPlcyQICounters",
    "TmnxActionType",
    "TmnxAdminState",
    "TmnxOperState",
    "TmnxSyslogFacility",
    "TmnxSyslogSeverity",
    "TmnxUdpPort")


# MODULE-IDENTITY

timetraLogMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 12)
)
if mibBuilder.loadTexts:
    timetraLogMIBModule.setRevisions(
        ("2020-07-14 00:00",
         "2019-04-01 00:00",
         "2017-06-30 00:00",
         "2017-03-01 00:00",
         "2016-01-01 00:00",
         "2015-01-01 00:00",
         "2014-01-01 00:00",
         "2011-02-01 00:00",
         "2009-02-28 00:00",
         "2008-01-01 00:00",
         "2007-01-01 00:00",
         "2006-03-15 00:00",
         "2005-01-24 00:00",
         "2004-05-27 00:00",
         "2004-01-15 00:00",
         "2003-08-15 00:00",
         "2003-01-20 00:00",
         "2001-11-10 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxPerceivedSeverity(TextualConvention, Integer32):
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
              6)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("cleared", 1),
          ("indeterminate", 2),
          ("critical", 3),
          ("major", 4),
          ("minor", 5),
          ("warning", 6))
    )



class TmnxSyslogId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )



class TmnxSyslogIdOrEmpty(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 40),
    )



class TmnxLogFileId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )



class TmnxLogFileType(TextualConvention, Integer32):
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
        *(("none", 0),
          ("eventLog", 1),
          ("accountingPolicy", 2))
    )



class TmnxLogIdIndex(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 101),
    )



class TmnxStgIndex(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )



class TmnxCFlash(TextualConvention, Unsigned32):
    status = "current"


class TmnxLogFilterId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )



class TmnxLogFilterEntryId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )



class TmnxLogFilterOperator(TextualConvention, Integer32):
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
        *(("off", 1),
          ("equal", 2),
          ("notEqual", 3),
          ("lessThan", 4),
          ("lessThanOrEqual", 5),
          ("greaterThan", 6),
          ("greaterThanOrEqual", 7))
    )



class TmnxEventNumber(TextualConvention, Unsigned32):
    status = "current"


class TmnxLogExRbkOperationType(TextualConvention, Integer32):
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
        *(("unknown", 0),
          ("exec", 1),
          ("rollback", 2),
          ("vsd", 3),
          ("load", 4))
    )



class LogStorageType(StorageType):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_TmnxLogConformance_ObjectIdentity = ObjectIdentity
tmnxLogConformance = _TmnxLogConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12)
)
_TmnxLogCompliances_ObjectIdentity = ObjectIdentity
tmnxLogCompliances = _TmnxLogCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 1)
)
_TmnxLogGroups_ObjectIdentity = ObjectIdentity
tmnxLogGroups = _TmnxLogGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2)
)
_TmnxLogObjs_ObjectIdentity = ObjectIdentity
tmnxLogObjs = _TmnxLogObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12)
)
_TmnxLogNotificationObjects_ObjectIdentity = ObjectIdentity
tmnxLogNotificationObjects = _TmnxLogNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 1)
)
_TmnxLogFileDeletedLogId_Type = TmnxLogIdIndex
_TmnxLogFileDeletedLogId_Object = MibScalar
tmnxLogFileDeletedLogId = _TmnxLogFileDeletedLogId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 1, 1),
    _TmnxLogFileDeletedLogId_Type()
)
tmnxLogFileDeletedLogId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxLogFileDeletedLogId.setStatus("current")
_TmnxLogFileDeletedFileId_Type = TmnxLogFileId
_TmnxLogFileDeletedFileId_Object = MibScalar
tmnxLogFileDeletedFileId = _TmnxLogFileDeletedFileId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 1, 2),
    _TmnxLogFileDeletedFileId_Type()
)
tmnxLogFileDeletedFileId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxLogFileDeletedFileId.setStatus("current")
_TmnxLogFileDeletedLogType_Type = TmnxLogFileType
_TmnxLogFileDeletedLogType_Object = MibScalar
tmnxLogFileDeletedLogType = _TmnxLogFileDeletedLogType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 1, 3),
    _TmnxLogFileDeletedLogType_Type()
)
tmnxLogFileDeletedLogType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxLogFileDeletedLogType.setStatus("current")
_TmnxLogFileDeletedLocation_Type = TmnxCFlash
_TmnxLogFileDeletedLocation_Object = MibScalar
tmnxLogFileDeletedLocation = _TmnxLogFileDeletedLocation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 1, 4),
    _TmnxLogFileDeletedLocation_Type()
)
tmnxLogFileDeletedLocation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxLogFileDeletedLocation.setStatus("current")
_TmnxLogFileDeletedName_Type = DisplayString
_TmnxLogFileDeletedName_Object = MibScalar
tmnxLogFileDeletedName = _TmnxLogFileDeletedName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 1, 5),
    _TmnxLogFileDeletedName_Type()
)
tmnxLogFileDeletedName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxLogFileDeletedName.setStatus("current")
_TmnxLogFileDeletedCreateTime_Type = DateAndTime
_TmnxLogFileDeletedCreateTime_Object = MibScalar
tmnxLogFileDeletedCreateTime = _TmnxLogFileDeletedCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 1, 6),
    _TmnxLogFileDeletedCreateTime_Type()
)
tmnxLogFileDeletedCreateTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxLogFileDeletedCreateTime.setStatus("current")


class _TmnxLogTraceErrorTitle_Type(DisplayString):
    """Custom type tmnxLogTraceErrorTitle based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_TmnxLogTraceErrorTitle_Type.__name__ = "DisplayString"
_TmnxLogTraceErrorTitle_Object = MibScalar
tmnxLogTraceErrorTitle = _TmnxLogTraceErrorTitle_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 1, 7),
    _TmnxLogTraceErrorTitle_Type()
)
tmnxLogTraceErrorTitle.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxLogTraceErrorTitle.setStatus("current")


class _TmnxLogTraceErrorSubject_Type(DisplayString):
    """Custom type tmnxLogTraceErrorSubject based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_TmnxLogTraceErrorSubject_Type.__name__ = "DisplayString"
_TmnxLogTraceErrorSubject_Object = MibScalar
tmnxLogTraceErrorSubject = _TmnxLogTraceErrorSubject_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 1, 8),
    _TmnxLogTraceErrorSubject_Type()
)
tmnxLogTraceErrorSubject.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxLogTraceErrorSubject.setStatus("current")
_TmnxLogTraceErrorMessage_Type = DisplayString
_TmnxLogTraceErrorMessage_Object = MibScalar
tmnxLogTraceErrorMessage = _TmnxLogTraceErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 1, 9),
    _TmnxLogTraceErrorMessage_Type()
)
tmnxLogTraceErrorMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxLogTraceErrorMessage.setStatus("current")
_TmnxLogThrottledEventID_Type = ObjectIdentifier
_TmnxLogThrottledEventID_Object = MibScalar
tmnxLogThrottledEventID = _TmnxLogThrottledEventID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 1, 10),
    _TmnxLogThrottledEventID_Type()
)
tmnxLogThrottledEventID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxLogThrottledEventID.setStatus("current")
_TmnxLogThrottledEvents_Type = Unsigned32
_TmnxLogThrottledEvents_Object = MibScalar
tmnxLogThrottledEvents = _TmnxLogThrottledEvents_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 1, 11),
    _TmnxLogThrottledEvents_Type()
)
tmnxLogThrottledEvents.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxLogThrottledEvents.setStatus("current")
_TmnxSysLogTargetId_Type = TmnxSyslogId
_TmnxSysLogTargetId_Object = MibScalar
tmnxSysLogTargetId = _TmnxSysLogTargetId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 1, 12),
    _TmnxSysLogTargetId_Type()
)
tmnxSysLogTargetId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxSysLogTargetId.setStatus("current")
_TmnxSysLogTargetProblemDescr_Type = DisplayString
_TmnxSysLogTargetProblemDescr_Object = MibScalar
tmnxSysLogTargetProblemDescr = _TmnxSysLogTargetProblemDescr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 1, 13),
    _TmnxSysLogTargetProblemDescr_Type()
)
tmnxSysLogTargetProblemDescr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxSysLogTargetProblemDescr.setStatus("current")


class _TmnxLogNotifyApInterval_Type(Integer32):
    """Custom type tmnxLogNotifyApInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 120),
    )


_TmnxLogNotifyApInterval_Type.__name__ = "Integer32"
_TmnxLogNotifyApInterval_Object = MibScalar
tmnxLogNotifyApInterval = _TmnxLogNotifyApInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 1, 14),
    _TmnxLogNotifyApInterval_Type()
)
tmnxLogNotifyApInterval.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxLogNotifyApInterval.setStatus("current")
_TmnxStdReplayStartEvent_Type = Unsigned32
_TmnxStdReplayStartEvent_Object = MibScalar
tmnxStdReplayStartEvent = _TmnxStdReplayStartEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 1, 15),
    _TmnxStdReplayStartEvent_Type()
)
tmnxStdReplayStartEvent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxStdReplayStartEvent.setStatus("current")
_TmnxStdReplayEndEvent_Type = Unsigned32
_TmnxStdReplayEndEvent_Object = MibScalar
tmnxStdReplayEndEvent = _TmnxStdReplayEndEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 1, 16),
    _TmnxStdReplayEndEvent_Type()
)
tmnxStdReplayEndEvent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxStdReplayEndEvent.setStatus("current")


class _TmnxEhsHEntryMinDelayInterval_Type(Unsigned32):
    """Custom type tmnxEhsHEntryMinDelayInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 604800),
    )


_TmnxEhsHEntryMinDelayInterval_Type.__name__ = "Unsigned32"
_TmnxEhsHEntryMinDelayInterval_Object = MibScalar
tmnxEhsHEntryMinDelayInterval = _TmnxEhsHEntryMinDelayInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 1, 17),
    _TmnxEhsHEntryMinDelayInterval_Type()
)
tmnxEhsHEntryMinDelayInterval.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxEhsHEntryMinDelayInterval.setStatus("current")


class _TmnxLogMaxLogs_Type(Unsigned32):
    """Custom type tmnxLogMaxLogs based on Unsigned32"""
    defaultValue = 60


_TmnxLogMaxLogs_Type.__name__ = "Unsigned32"
_TmnxLogMaxLogs_Object = MibScalar
tmnxLogMaxLogs = _TmnxLogMaxLogs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 2),
    _TmnxLogMaxLogs_Type()
)
tmnxLogMaxLogs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLogMaxLogs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxLogMaxLogs.setUnits("logs")
_TmnxLogFileIdTable_Object = MibTable
tmnxLogFileIdTable = _TmnxLogFileIdTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 3)
)
if mibBuilder.loadTexts:
    tmnxLogFileIdTable.setStatus("current")
_TmnxLogFileIdEntry_Object = MibTableRow
tmnxLogFileIdEntry = _TmnxLogFileIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 3, 1)
)
tmnxLogFileIdEntry.setIndexNames(
    (0, "TIMETRA-LOG-MIB", "tmnxLogFileId"),
)
if mibBuilder.loadTexts:
    tmnxLogFileIdEntry.setStatus("current")
_TmnxLogFileId_Type = TmnxLogFileId
_TmnxLogFileId_Object = MibTableColumn
tmnxLogFileId = _TmnxLogFileId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 3, 1, 1),
    _TmnxLogFileId_Type()
)
tmnxLogFileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxLogFileId.setStatus("current")
_TmnxLogFileIdRowStatus_Type = RowStatus
_TmnxLogFileIdRowStatus_Object = MibTableColumn
tmnxLogFileIdRowStatus = _TmnxLogFileIdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 3, 1, 2),
    _TmnxLogFileIdRowStatus_Type()
)
tmnxLogFileIdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogFileIdRowStatus.setStatus("current")


class _TmnxLogFileIdStorageType_Type(StorageType):
    """Custom type tmnxLogFileIdStorageType based on StorageType"""
    defaultValue = 3


_TmnxLogFileIdStorageType_Type.__name__ = "StorageType"
_TmnxLogFileIdStorageType_Object = MibTableColumn
tmnxLogFileIdStorageType = _TmnxLogFileIdStorageType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 3, 1, 3),
    _TmnxLogFileIdStorageType_Type()
)
tmnxLogFileIdStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogFileIdStorageType.setStatus("current")


class _TmnxLogFileIdRolloverTime_Type(Integer32):
    """Custom type tmnxLogFileIdRolloverTime based on Integer32"""
    defaultValue = 1440

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 10080),
    )


_TmnxLogFileIdRolloverTime_Type.__name__ = "Integer32"
_TmnxLogFileIdRolloverTime_Object = MibTableColumn
tmnxLogFileIdRolloverTime = _TmnxLogFileIdRolloverTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 3, 1, 4),
    _TmnxLogFileIdRolloverTime_Type()
)
tmnxLogFileIdRolloverTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogFileIdRolloverTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxLogFileIdRolloverTime.setUnits("minutes")


class _TmnxLogFileIdRetainTime_Type(Integer32):
    """Custom type tmnxLogFileIdRetainTime based on Integer32"""
    defaultValue = 12

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_TmnxLogFileIdRetainTime_Type.__name__ = "Integer32"
_TmnxLogFileIdRetainTime_Object = MibTableColumn
tmnxLogFileIdRetainTime = _TmnxLogFileIdRetainTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 3, 1, 5),
    _TmnxLogFileIdRetainTime_Type()
)
tmnxLogFileIdRetainTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogFileIdRetainTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxLogFileIdRetainTime.setUnits("hours")


class _TmnxLogFileIdAdminLocation_Type(TmnxCFlash):
    """Custom type tmnxLogFileIdAdminLocation based on TmnxCFlash"""
    defaultValue = 0


_TmnxLogFileIdAdminLocation_Type.__name__ = "TmnxCFlash"
_TmnxLogFileIdAdminLocation_Object = MibTableColumn
tmnxLogFileIdAdminLocation = _TmnxLogFileIdAdminLocation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 3, 1, 6),
    _TmnxLogFileIdAdminLocation_Type()
)
tmnxLogFileIdAdminLocation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogFileIdAdminLocation.setStatus("current")
_TmnxLogFileIdOperLocation_Type = TmnxCFlash
_TmnxLogFileIdOperLocation_Object = MibTableColumn
tmnxLogFileIdOperLocation = _TmnxLogFileIdOperLocation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 3, 1, 7),
    _TmnxLogFileIdOperLocation_Type()
)
tmnxLogFileIdOperLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogFileIdOperLocation.setStatus("current")


class _TmnxLogFileIdDescription_Type(TItemDescription):
    """Custom type tmnxLogFileIdDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxLogFileIdDescription_Type.__name__ = "TItemDescription"
_TmnxLogFileIdDescription_Object = MibTableColumn
tmnxLogFileIdDescription = _TmnxLogFileIdDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 3, 1, 8),
    _TmnxLogFileIdDescription_Type()
)
tmnxLogFileIdDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogFileIdDescription.setStatus("current")
_TmnxLogFileIdLogType_Type = TmnxLogFileType
_TmnxLogFileIdLogType_Object = MibTableColumn
tmnxLogFileIdLogType = _TmnxLogFileIdLogType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 3, 1, 9),
    _TmnxLogFileIdLogType_Type()
)
tmnxLogFileIdLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogFileIdLogType.setStatus("current")


class _TmnxLogFileIdLogId_Type(Integer32):
    """Custom type tmnxLogFileIdLogId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_TmnxLogFileIdLogId_Type.__name__ = "Integer32"
_TmnxLogFileIdLogId_Object = MibTableColumn
tmnxLogFileIdLogId = _TmnxLogFileIdLogId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 3, 1, 10),
    _TmnxLogFileIdLogId_Type()
)
tmnxLogFileIdLogId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogFileIdLogId.setStatus("current")
_TmnxLogFileIdPathName_Type = DisplayString
_TmnxLogFileIdPathName_Object = MibTableColumn
tmnxLogFileIdPathName = _TmnxLogFileIdPathName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 3, 1, 11),
    _TmnxLogFileIdPathName_Type()
)
tmnxLogFileIdPathName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogFileIdPathName.setStatus("current")
_TmnxLogFileIdCreateTime_Type = DateAndTime
_TmnxLogFileIdCreateTime_Object = MibTableColumn
tmnxLogFileIdCreateTime = _TmnxLogFileIdCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 3, 1, 12),
    _TmnxLogFileIdCreateTime_Type()
)
tmnxLogFileIdCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogFileIdCreateTime.setStatus("current")


class _TmnxLogFileIdBackupLoc_Type(TmnxCFlash):
    """Custom type tmnxLogFileIdBackupLoc based on TmnxCFlash"""
    defaultValue = 0


_TmnxLogFileIdBackupLoc_Type.__name__ = "TmnxCFlash"
_TmnxLogFileIdBackupLoc_Object = MibTableColumn
tmnxLogFileIdBackupLoc = _TmnxLogFileIdBackupLoc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 3, 1, 13),
    _TmnxLogFileIdBackupLoc_Type()
)
tmnxLogFileIdBackupLoc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogFileIdBackupLoc.setStatus("current")


class _TmnxLogFileIdName_Type(TLNamedItemOrEmpty):
    """Custom type tmnxLogFileIdName based on TLNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxLogFileIdName_Type.__name__ = "TLNamedItemOrEmpty"
_TmnxLogFileIdName_Object = MibTableColumn
tmnxLogFileIdName = _TmnxLogFileIdName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 3, 1, 14),
    _TmnxLogFileIdName_Type()
)
tmnxLogFileIdName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogFileIdName.setStatus("current")
_TmnxLogApTable_Object = MibTable
tmnxLogApTable = _TmnxLogApTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 4)
)
if mibBuilder.loadTexts:
    tmnxLogApTable.setStatus("current")
_TmnxLogApEntry_Object = MibTableRow
tmnxLogApEntry = _TmnxLogApEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 4, 1)
)
tmnxLogApEntry.setIndexNames(
    (0, "TIMETRA-LOG-MIB", "tmnxLogApPolicyId"),
)
if mibBuilder.loadTexts:
    tmnxLogApEntry.setStatus("current")


class _TmnxLogApPolicyId_Type(Integer32):
    """Custom type tmnxLogApPolicyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_TmnxLogApPolicyId_Type.__name__ = "Integer32"
_TmnxLogApPolicyId_Object = MibTableColumn
tmnxLogApPolicyId = _TmnxLogApPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 4, 1, 1),
    _TmnxLogApPolicyId_Type()
)
tmnxLogApPolicyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxLogApPolicyId.setStatus("current")
_TmnxLogApRowStatus_Type = RowStatus
_TmnxLogApRowStatus_Object = MibTableColumn
tmnxLogApRowStatus = _TmnxLogApRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 4, 1, 2),
    _TmnxLogApRowStatus_Type()
)
tmnxLogApRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogApRowStatus.setStatus("current")


class _TmnxLogApStorageType_Type(LogStorageType):
    """Custom type tmnxLogApStorageType based on LogStorageType"""
    defaultValue = 3


_TmnxLogApStorageType_Type.__name__ = "LogStorageType"
_TmnxLogApStorageType_Object = MibTableColumn
tmnxLogApStorageType = _TmnxLogApStorageType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 4, 1, 3),
    _TmnxLogApStorageType_Type()
)
tmnxLogApStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogApStorageType.setStatus("current")


class _TmnxLogApAdminStatus_Type(TmnxAdminState):
    """Custom type tmnxLogApAdminStatus based on TmnxAdminState"""
    defaultValue = 3


_TmnxLogApAdminStatus_Type.__name__ = "TmnxAdminState"
_TmnxLogApAdminStatus_Object = MibTableColumn
tmnxLogApAdminStatus = _TmnxLogApAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 4, 1, 4),
    _TmnxLogApAdminStatus_Type()
)
tmnxLogApAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogApAdminStatus.setStatus("current")
_TmnxLogApOperStatus_Type = TmnxOperState
_TmnxLogApOperStatus_Object = MibTableColumn
tmnxLogApOperStatus = _TmnxLogApOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 4, 1, 5),
    _TmnxLogApOperStatus_Type()
)
tmnxLogApOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogApOperStatus.setStatus("current")


class _TmnxLogApInterval_Type(Integer32):
    """Custom type tmnxLogApInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_TmnxLogApInterval_Type.__name__ = "Integer32"
_TmnxLogApInterval_Object = MibTableColumn
tmnxLogApInterval = _TmnxLogApInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 4, 1, 6),
    _TmnxLogApInterval_Type()
)
tmnxLogApInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogApInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxLogApInterval.setUnits("minutes")


class _TmnxLogApDescription_Type(TItemDescription):
    """Custom type tmnxLogApDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxLogApDescription_Type.__name__ = "TItemDescription"
_TmnxLogApDescription_Object = MibTableColumn
tmnxLogApDescription = _TmnxLogApDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 4, 1, 7),
    _TmnxLogApDescription_Type()
)
tmnxLogApDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogApDescription.setStatus("current")


class _TmnxLogApDefault_Type(TruthValue):
    """Custom type tmnxLogApDefault based on TruthValue"""
    defaultValue = 2


_TmnxLogApDefault_Type.__name__ = "TruthValue"
_TmnxLogApDefault_Object = MibTableColumn
tmnxLogApDefault = _TmnxLogApDefault_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 4, 1, 8),
    _TmnxLogApDefault_Type()
)
tmnxLogApDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogApDefault.setStatus("current")


class _TmnxLogApRecord_Type(Integer32):
    """Custom type tmnxLogApRecord based on Integer32"""
    defaultValue = 0

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
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("svcIngressOctet", 1),
          ("svcEgressOctet", 2),
          ("svcIngressPkt", 3),
          ("svcEgressPkt", 4),
          ("netIngressOctet", 5),
          ("netEgressOctet", 6),
          ("netIngressPkt", 7),
          ("netEgressPkt", 8),
          ("compactSvcInOctet", 9),
          ("combinedSvcIngress", 10),
          ("combinedNetInEgOctet", 11),
          ("combinedSvcInEgOctet", 12),
          ("completeSvcInEg", 13),
          ("combinedSvcSdpInEg", 14),
          ("completeSvcSdpInEg", 15),
          ("completeSubscrIngrEgr", 16),
          ("bsxProtocol", 17),
          ("bsxApplication", 18),
          ("bsxAppGroup", 19),
          ("bsxSubscriberProtocol", 20),
          ("bsxSubscriberApplication", 21),
          ("bsxSubscriberAppGroup", 22),
          ("customRecordSubscriber", 23),
          ("customRecordService", 24),
          ("customRecordAa", 25),
          ("queueGroupOctets", 26),
          ("queueGroupPackets", 27),
          ("combinedQueueGroup", 28),
          ("combinedMplsLspIngress", 29),
          ("combinedMplsLspEgress", 30),
          ("combinedLdpLspEgress", 31),
          ("saa", 32),
          ("video", 33),
          ("kpiSystem", 34),
          ("kpiBearerMgmt", 35),
          ("kpiBearerTraffic", 36),
          ("kpiRefPoint", 37),
          ("kpiPathMgmt", 38),
          ("kciIom3", 39),
          ("kciSystem", 40),
          ("kciBearerMgmt", 41),
          ("kciPathMgmt", 42),
          ("completeKpi", 43),
          ("completeKci", 44),
          ("kpiBearerGroup", 45),
          ("kpiRefPathGroup", 46),
          ("kpiKciBearerMgmt", 47),
          ("kpiKciPathMgmt", 48),
          ("kpiKciSystem", 49),
          ("completeKpiKci", 50),
          ("aaPerformance", 51),
          ("completeEthernetPort", 52),
          ("extendedSvcIngrEgr", 53),
          ("completeNetIngrEgr", 54),
          ("aaPartition", 55),
          ("completeOamPm", 56),
          ("kpiRefPtSecErrorCauseCode", 57),
          ("kpiBearerTrafficGtpEndpoint", 58),
          ("kpiIpReas", 59),
          ("kpiRadiusGroup", 60),
          ("kpiRefPtFailureCauseCode", 61),
          ("kpiDhcpGroup", 62),
          ("aaAdmitDeny", 63),
          ("netIntfIngressOctet", 65),
          ("netIntfEgressOctet", 66),
          ("netIntfIngressPkt", 67),
          ("netIntfEgressPkt", 68),
          ("combinedNetIntfIngress", 69),
          ("combinedNetIntfEgress", 70),
          ("completeNetIntfIngrEgr", 71),
          ("accessEgressOctets", 72),
          ("accessEgressPackets", 73),
          ("combinedAccessEgress", 74),
          ("combinedNetworkEgress", 75),
          ("completeSvcActivTestHead", 76),
          ("combinedMplsSrteEgress", 77))
    )


_TmnxLogApRecord_Type.__name__ = "Integer32"
_TmnxLogApRecord_Object = MibTableColumn
tmnxLogApRecord = _TmnxLogApRecord_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 4, 1, 9),
    _TmnxLogApRecord_Type()
)
tmnxLogApRecord.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogApRecord.setStatus("current")
_TmnxLogApToFileId_Type = TmnxLogFileId
_TmnxLogApToFileId_Object = MibTableColumn
tmnxLogApToFileId = _TmnxLogApToFileId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 4, 1, 10),
    _TmnxLogApToFileId_Type()
)
tmnxLogApToFileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogApToFileId.setStatus("current")


class _TmnxLogApPortType_Type(Integer32):
    """Custom type tmnxLogApPortType based on Integer32"""
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
              14,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("access", 1),
          ("network", 2),
          ("sdp", 3),
          ("subscriber", 4),
          ("appAssure", 5),
          ("qgrp", 6),
          ("saa", 7),
          ("mplsLspIngr", 8),
          ("mplsLspEgr", 9),
          ("ldpLspEgr", 10),
          ("video", 11),
          ("mobileGateway", 12),
          ("ethernet", 13),
          ("oamPm", 14),
          ("networkIntf", 16),
          ("accessPort", 17),
          ("svcActvTest", 18),
          ("mplsSrteEgr", 19))
    )


_TmnxLogApPortType_Type.__name__ = "Integer32"
_TmnxLogApPortType_Object = MibTableColumn
tmnxLogApPortType = _TmnxLogApPortType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 4, 1, 11),
    _TmnxLogApPortType_Type()
)
tmnxLogApPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogApPortType.setStatus("current")


class _TmnxLogApDefaultInterval_Type(TruthValue):
    """Custom type tmnxLogApDefaultInterval based on TruthValue"""
    defaultValue = 1


_TmnxLogApDefaultInterval_Type.__name__ = "TruthValue"
_TmnxLogApDefaultInterval_Object = MibTableColumn
tmnxLogApDefaultInterval = _TmnxLogApDefaultInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 4, 1, 12),
    _TmnxLogApDefaultInterval_Type()
)
tmnxLogApDefaultInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogApDefaultInterval.setStatus("obsolete")
_TmnxLogApDataLossCount_Type = Counter32
_TmnxLogApDataLossCount_Object = MibTableColumn
tmnxLogApDataLossCount = _TmnxLogApDataLossCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 4, 1, 13),
    _TmnxLogApDataLossCount_Type()
)
tmnxLogApDataLossCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogApDataLossCount.setStatus("current")
_TmnxLogApLastDataLossTimeStamp_Type = TimeStamp
_TmnxLogApLastDataLossTimeStamp_Object = MibTableColumn
tmnxLogApLastDataLossTimeStamp = _TmnxLogApLastDataLossTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 4, 1, 14),
    _TmnxLogApLastDataLossTimeStamp_Type()
)
tmnxLogApLastDataLossTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogApLastDataLossTimeStamp.setStatus("current")


class _TmnxLogApToFileType_Type(Integer32):
    """Custom type tmnxLogApToFileType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fileId", 0),
          ("noFile", 1))
    )


_TmnxLogApToFileType_Type.__name__ = "Integer32"
_TmnxLogApToFileType_Object = MibTableColumn
tmnxLogApToFileType = _TmnxLogApToFileType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 4, 1, 15),
    _TmnxLogApToFileType_Type()
)
tmnxLogApToFileType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogApToFileType.setStatus("current")


class _TmnxLogApIncludeSystemInfo_Type(TruthValue):
    """Custom type tmnxLogApIncludeSystemInfo based on TruthValue"""
    defaultValue = 2


_TmnxLogApIncludeSystemInfo_Type.__name__ = "TruthValue"
_TmnxLogApIncludeSystemInfo_Object = MibTableColumn
tmnxLogApIncludeSystemInfo = _TmnxLogApIncludeSystemInfo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 4, 1, 16),
    _TmnxLogApIncludeSystemInfo_Type()
)
tmnxLogApIncludeSystemInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogApIncludeSystemInfo.setStatus("current")


class _TmnxLogApAlign_Type(TruthValue):
    """Custom type tmnxLogApAlign based on TruthValue"""
    defaultValue = 2


_TmnxLogApAlign_Type.__name__ = "TruthValue"
_TmnxLogApAlign_Object = MibTableColumn
tmnxLogApAlign = _TmnxLogApAlign_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 4, 1, 17),
    _TmnxLogApAlign_Type()
)
tmnxLogApAlign.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogApAlign.setStatus("current")
_TmnxLogIdTable_Object = MibTable
tmnxLogIdTable = _TmnxLogIdTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 5)
)
if mibBuilder.loadTexts:
    tmnxLogIdTable.setStatus("current")
_TmnxLogIdEntry_Object = MibTableRow
tmnxLogIdEntry = _TmnxLogIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 5, 1)
)
tmnxLogIdEntry.setIndexNames(
    (0, "TIMETRA-LOG-MIB", "tmnxLogIdIndex"),
)
if mibBuilder.loadTexts:
    tmnxLogIdEntry.setStatus("current")
_TmnxLogIdIndex_Type = TmnxLogIdIndex
_TmnxLogIdIndex_Object = MibTableColumn
tmnxLogIdIndex = _TmnxLogIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 5, 1, 1),
    _TmnxLogIdIndex_Type()
)
tmnxLogIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxLogIdIndex.setStatus("current")
_TmnxLogIdRowStatus_Type = RowStatus
_TmnxLogIdRowStatus_Object = MibTableColumn
tmnxLogIdRowStatus = _TmnxLogIdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 5, 1, 2),
    _TmnxLogIdRowStatus_Type()
)
tmnxLogIdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogIdRowStatus.setStatus("current")


class _TmnxLogIdStorageType_Type(LogStorageType):
    """Custom type tmnxLogIdStorageType based on LogStorageType"""
    defaultValue = 3


_TmnxLogIdStorageType_Type.__name__ = "LogStorageType"
_TmnxLogIdStorageType_Object = MibTableColumn
tmnxLogIdStorageType = _TmnxLogIdStorageType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 5, 1, 3),
    _TmnxLogIdStorageType_Type()
)
tmnxLogIdStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogIdStorageType.setStatus("current")


class _TmnxLogIdAdminStatus_Type(TmnxAdminState):
    """Custom type tmnxLogIdAdminStatus based on TmnxAdminState"""
    defaultValue = 2


_TmnxLogIdAdminStatus_Type.__name__ = "TmnxAdminState"
_TmnxLogIdAdminStatus_Object = MibTableColumn
tmnxLogIdAdminStatus = _TmnxLogIdAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 5, 1, 4),
    _TmnxLogIdAdminStatus_Type()
)
tmnxLogIdAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogIdAdminStatus.setStatus("current")
_TmnxLogIdOperStatus_Type = TmnxOperState
_TmnxLogIdOperStatus_Object = MibTableColumn
tmnxLogIdOperStatus = _TmnxLogIdOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 5, 1, 5),
    _TmnxLogIdOperStatus_Type()
)
tmnxLogIdOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogIdOperStatus.setStatus("current")


class _TmnxLogIdDescription_Type(TItemDescription):
    """Custom type tmnxLogIdDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxLogIdDescription_Type.__name__ = "TItemDescription"
_TmnxLogIdDescription_Object = MibTableColumn
tmnxLogIdDescription = _TmnxLogIdDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 5, 1, 6),
    _TmnxLogIdDescription_Type()
)
tmnxLogIdDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogIdDescription.setStatus("current")


class _TmnxLogIdFilterId_Type(TmnxLogFilterId):
    """Custom type tmnxLogIdFilterId based on TmnxLogFilterId"""
    defaultValue = 0


_TmnxLogIdFilterId_Type.__name__ = "TmnxLogFilterId"
_TmnxLogIdFilterId_Object = MibTableColumn
tmnxLogIdFilterId = _TmnxLogIdFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 5, 1, 7),
    _TmnxLogIdFilterId_Type()
)
tmnxLogIdFilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogIdFilterId.setStatus("current")


class _TmnxLogIdSource_Type(Bits):
    """Custom type tmnxLogIdSource based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("main", 0),
          ("security", 1),
          ("change", 2),
          ("debugTrace", 3),
          ("li", 4))
    )

_TmnxLogIdSource_Type.__name__ = "Bits"
_TmnxLogIdSource_Object = MibTableColumn
tmnxLogIdSource = _TmnxLogIdSource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 5, 1, 8),
    _TmnxLogIdSource_Type()
)
tmnxLogIdSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogIdSource.setStatus("current")


class _TmnxLogIdDestination_Type(Integer32):
    """Custom type tmnxLogIdDestination based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("console", 1),
          ("syslog", 2),
          ("snmpTraps", 3),
          ("file", 4),
          ("memory", 5),
          ("netconf", 7),
          ("subscribedCli", 8))
    )


_TmnxLogIdDestination_Type.__name__ = "Integer32"
_TmnxLogIdDestination_Object = MibTableColumn
tmnxLogIdDestination = _TmnxLogIdDestination_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 5, 1, 9),
    _TmnxLogIdDestination_Type()
)
tmnxLogIdDestination.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogIdDestination.setStatus("current")
_TmnxLogIdFileId_Type = TmnxLogFileId
_TmnxLogIdFileId_Object = MibTableColumn
tmnxLogIdFileId = _TmnxLogIdFileId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 5, 1, 10),
    _TmnxLogIdFileId_Type()
)
tmnxLogIdFileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogIdFileId.setStatus("current")


class _TmnxLogIdSyslogId_Type(TmnxSyslogIdOrEmpty):
    """Custom type tmnxLogIdSyslogId based on TmnxSyslogIdOrEmpty"""
    defaultValue = 0


_TmnxLogIdSyslogId_Type.__name__ = "TmnxSyslogIdOrEmpty"
_TmnxLogIdSyslogId_Object = MibTableColumn
tmnxLogIdSyslogId = _TmnxLogIdSyslogId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 5, 1, 11),
    _TmnxLogIdSyslogId_Type()
)
tmnxLogIdSyslogId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogIdSyslogId.setStatus("current")


class _TmnxLogIdMaxMemorySize_Type(Unsigned32):
    """Custom type tmnxLogIdMaxMemorySize based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(50, 3000),
    )


_TmnxLogIdMaxMemorySize_Type.__name__ = "Unsigned32"
_TmnxLogIdMaxMemorySize_Object = MibTableColumn
tmnxLogIdMaxMemorySize = _TmnxLogIdMaxMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 5, 1, 12),
    _TmnxLogIdMaxMemorySize_Type()
)
tmnxLogIdMaxMemorySize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogIdMaxMemorySize.setStatus("current")
if mibBuilder.loadTexts:
    tmnxLogIdMaxMemorySize.setUnits("events")


class _TmnxLogIdConsoleSession_Type(TruthValue):
    """Custom type tmnxLogIdConsoleSession based on TruthValue"""
    defaultValue = 2


_TmnxLogIdConsoleSession_Type.__name__ = "TruthValue"
_TmnxLogIdConsoleSession_Object = MibTableColumn
tmnxLogIdConsoleSession = _TmnxLogIdConsoleSession_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 5, 1, 13),
    _TmnxLogIdConsoleSession_Type()
)
tmnxLogIdConsoleSession.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogIdConsoleSession.setStatus("obsolete")
_TmnxLogIdForwarded_Type = Counter64
_TmnxLogIdForwarded_Object = MibTableColumn
tmnxLogIdForwarded = _TmnxLogIdForwarded_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 5, 1, 14),
    _TmnxLogIdForwarded_Type()
)
tmnxLogIdForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogIdForwarded.setStatus("current")
_TmnxLogIdDropped_Type = Counter64
_TmnxLogIdDropped_Object = MibTableColumn
tmnxLogIdDropped = _TmnxLogIdDropped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 5, 1, 15),
    _TmnxLogIdDropped_Type()
)
tmnxLogIdDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogIdDropped.setStatus("current")


class _TmnxLogIdTimeFormat_Type(Integer32):
    """Custom type tmnxLogIdTimeFormat based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("utc", 1),
          ("local", 2))
    )


_TmnxLogIdTimeFormat_Type.__name__ = "Integer32"
_TmnxLogIdTimeFormat_Object = MibTableColumn
tmnxLogIdTimeFormat = _TmnxLogIdTimeFormat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 5, 1, 16),
    _TmnxLogIdTimeFormat_Type()
)
tmnxLogIdTimeFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogIdTimeFormat.setStatus("current")


class _TmnxLogIdPythonPolicy_Type(TNamedItemOrEmpty):
    """Custom type tmnxLogIdPythonPolicy based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxLogIdPythonPolicy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxLogIdPythonPolicy_Object = MibTableColumn
tmnxLogIdPythonPolicy = _TmnxLogIdPythonPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 5, 1, 17),
    _TmnxLogIdPythonPolicy_Type()
)
tmnxLogIdPythonPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogIdPythonPolicy.setStatus("current")


class _TmnxLogIdOperDestination_Type(Integer32):
    """Custom type tmnxLogIdOperDestination based on Integer32"""
    defaultValue = 0

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
              8)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("console", 1),
          ("syslog", 2),
          ("snmpTraps", 3),
          ("file", 4),
          ("memory", 5),
          ("cliSession", 6),
          ("netconf", 7),
          ("subscribedCli", 8))
    )


_TmnxLogIdOperDestination_Type.__name__ = "Integer32"
_TmnxLogIdOperDestination_Object = MibTableColumn
tmnxLogIdOperDestination = _TmnxLogIdOperDestination_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 5, 1, 18),
    _TmnxLogIdOperDestination_Type()
)
tmnxLogIdOperDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogIdOperDestination.setStatus("current")


class _TmnxLogIdNetconfStream_Type(TNamedItemOrEmpty):
    """Custom type tmnxLogIdNetconfStream based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxLogIdNetconfStream_Type.__name__ = "TNamedItemOrEmpty"
_TmnxLogIdNetconfStream_Object = MibTableColumn
tmnxLogIdNetconfStream = _TmnxLogIdNetconfStream_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 5, 1, 19),
    _TmnxLogIdNetconfStream_Type()
)
tmnxLogIdNetconfStream.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogIdNetconfStream.setStatus("current")


class _TmnxLogIdName_Type(TLNamedItemOrEmpty):
    """Custom type tmnxLogIdName based on TLNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxLogIdName_Type.__name__ = "TLNamedItemOrEmpty"
_TmnxLogIdName_Object = MibTableColumn
tmnxLogIdName = _TmnxLogIdName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 5, 1, 20),
    _TmnxLogIdName_Type()
)
tmnxLogIdName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogIdName.setStatus("current")
_TmnxLogFilterTable_Object = MibTable
tmnxLogFilterTable = _TmnxLogFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 6)
)
if mibBuilder.loadTexts:
    tmnxLogFilterTable.setStatus("current")
_TmnxLogFilterEntry_Object = MibTableRow
tmnxLogFilterEntry = _TmnxLogFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 6, 1)
)
tmnxLogFilterEntry.setIndexNames(
    (0, "TIMETRA-LOG-MIB", "tmnxLogFilterId"),
)
if mibBuilder.loadTexts:
    tmnxLogFilterEntry.setStatus("current")


class _TmnxLogFilterId_Type(TmnxLogFilterId):
    """Custom type tmnxLogFilterId based on TmnxLogFilterId"""
    subtypeSpec = TmnxLogFilterId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1500),
    )


_TmnxLogFilterId_Type.__name__ = "TmnxLogFilterId"
_TmnxLogFilterId_Object = MibTableColumn
tmnxLogFilterId = _TmnxLogFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 6, 1, 1),
    _TmnxLogFilterId_Type()
)
tmnxLogFilterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxLogFilterId.setStatus("current")
_TmnxLogFilterRowStatus_Type = RowStatus
_TmnxLogFilterRowStatus_Object = MibTableColumn
tmnxLogFilterRowStatus = _TmnxLogFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 6, 1, 2),
    _TmnxLogFilterRowStatus_Type()
)
tmnxLogFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogFilterRowStatus.setStatus("current")


class _TmnxLogFilterDescription_Type(TItemDescription):
    """Custom type tmnxLogFilterDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxLogFilterDescription_Type.__name__ = "TItemDescription"
_TmnxLogFilterDescription_Object = MibTableColumn
tmnxLogFilterDescription = _TmnxLogFilterDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 6, 1, 3),
    _TmnxLogFilterDescription_Type()
)
tmnxLogFilterDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogFilterDescription.setStatus("current")


class _TmnxLogFilterDefaultAction_Type(TFilterAction):
    """Custom type tmnxLogFilterDefaultAction based on TFilterAction"""
    defaultValue = 2


_TmnxLogFilterDefaultAction_Type.__name__ = "TFilterAction"
_TmnxLogFilterDefaultAction_Object = MibTableColumn
tmnxLogFilterDefaultAction = _TmnxLogFilterDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 6, 1, 4),
    _TmnxLogFilterDefaultAction_Type()
)
tmnxLogFilterDefaultAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogFilterDefaultAction.setStatus("current")
_TmnxLogFilterInUse_Type = TruthValue
_TmnxLogFilterInUse_Object = MibTableColumn
tmnxLogFilterInUse = _TmnxLogFilterInUse_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 6, 1, 5),
    _TmnxLogFilterInUse_Type()
)
tmnxLogFilterInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogFilterInUse.setStatus("current")


class _TmnxLogFilterName_Type(TLNamedItemOrEmpty):
    """Custom type tmnxLogFilterName based on TLNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxLogFilterName_Type.__name__ = "TLNamedItemOrEmpty"
_TmnxLogFilterName_Object = MibTableColumn
tmnxLogFilterName = _TmnxLogFilterName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 6, 1, 6),
    _TmnxLogFilterName_Type()
)
tmnxLogFilterName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogFilterName.setStatus("current")
_TmnxLogFilterParamsTable_Object = MibTable
tmnxLogFilterParamsTable = _TmnxLogFilterParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 7)
)
if mibBuilder.loadTexts:
    tmnxLogFilterParamsTable.setStatus("current")
_TmnxLogFilterParamsEntry_Object = MibTableRow
tmnxLogFilterParamsEntry = _TmnxLogFilterParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 7, 1)
)
tmnxLogFilterParamsEntry.setIndexNames(
    (0, "TIMETRA-LOG-MIB", "tmnxLogFilterId"),
    (0, "TIMETRA-LOG-MIB", "tmnxLogFilterParamsIndex"),
)
if mibBuilder.loadTexts:
    tmnxLogFilterParamsEntry.setStatus("current")
_TmnxLogFilterParamsIndex_Type = TmnxLogFilterEntryId
_TmnxLogFilterParamsIndex_Object = MibTableColumn
tmnxLogFilterParamsIndex = _TmnxLogFilterParamsIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 7, 1, 1),
    _TmnxLogFilterParamsIndex_Type()
)
tmnxLogFilterParamsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxLogFilterParamsIndex.setStatus("current")
_TmnxLogFilterParamsRowStatus_Type = RowStatus
_TmnxLogFilterParamsRowStatus_Object = MibTableColumn
tmnxLogFilterParamsRowStatus = _TmnxLogFilterParamsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 7, 1, 2),
    _TmnxLogFilterParamsRowStatus_Type()
)
tmnxLogFilterParamsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogFilterParamsRowStatus.setStatus("current")


class _TmnxLogFilterParamsDescription_Type(TItemDescription):
    """Custom type tmnxLogFilterParamsDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxLogFilterParamsDescription_Type.__name__ = "TItemDescription"
_TmnxLogFilterParamsDescription_Object = MibTableColumn
tmnxLogFilterParamsDescription = _TmnxLogFilterParamsDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 7, 1, 3),
    _TmnxLogFilterParamsDescription_Type()
)
tmnxLogFilterParamsDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogFilterParamsDescription.setStatus("current")


class _TmnxLogFilterParamsAction_Type(TFilterActionOrDefault):
    """Custom type tmnxLogFilterParamsAction based on TFilterActionOrDefault"""
    defaultValue = 3


_TmnxLogFilterParamsAction_Type.__name__ = "TFilterActionOrDefault"
_TmnxLogFilterParamsAction_Object = MibTableColumn
tmnxLogFilterParamsAction = _TmnxLogFilterParamsAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 7, 1, 4),
    _TmnxLogFilterParamsAction_Type()
)
tmnxLogFilterParamsAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogFilterParamsAction.setStatus("current")


class _TmnxLogFilterParamsApplication_Type(TNamedItemOrEmpty):
    """Custom type tmnxLogFilterParamsApplication based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxLogFilterParamsApplication_Type.__name__ = "TNamedItemOrEmpty"
_TmnxLogFilterParamsApplication_Object = MibTableColumn
tmnxLogFilterParamsApplication = _TmnxLogFilterParamsApplication_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 7, 1, 5),
    _TmnxLogFilterParamsApplication_Type()
)
tmnxLogFilterParamsApplication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogFilterParamsApplication.setStatus("current")


class _TmnxLogFilterParamsApplOperator_Type(TmnxLogFilterOperator):
    """Custom type tmnxLogFilterParamsApplOperator based on TmnxLogFilterOperator"""
    defaultValue = 1


_TmnxLogFilterParamsApplOperator_Type.__name__ = "TmnxLogFilterOperator"
_TmnxLogFilterParamsApplOperator_Object = MibTableColumn
tmnxLogFilterParamsApplOperator = _TmnxLogFilterParamsApplOperator_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 7, 1, 6),
    _TmnxLogFilterParamsApplOperator_Type()
)
tmnxLogFilterParamsApplOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogFilterParamsApplOperator.setStatus("current")


class _TmnxLogFilterParamsNumber_Type(TmnxEventNumber):
    """Custom type tmnxLogFilterParamsNumber based on TmnxEventNumber"""
    defaultValue = 0


_TmnxLogFilterParamsNumber_Type.__name__ = "TmnxEventNumber"
_TmnxLogFilterParamsNumber_Object = MibTableColumn
tmnxLogFilterParamsNumber = _TmnxLogFilterParamsNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 7, 1, 7),
    _TmnxLogFilterParamsNumber_Type()
)
tmnxLogFilterParamsNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogFilterParamsNumber.setStatus("current")


class _TmnxLogFilterParamsNumberOperator_Type(TmnxLogFilterOperator):
    """Custom type tmnxLogFilterParamsNumberOperator based on TmnxLogFilterOperator"""
    defaultValue = 1


_TmnxLogFilterParamsNumberOperator_Type.__name__ = "TmnxLogFilterOperator"
_TmnxLogFilterParamsNumberOperator_Object = MibTableColumn
tmnxLogFilterParamsNumberOperator = _TmnxLogFilterParamsNumberOperator_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 7, 1, 8),
    _TmnxLogFilterParamsNumberOperator_Type()
)
tmnxLogFilterParamsNumberOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogFilterParamsNumberOperator.setStatus("current")


class _TmnxLogFilterParamsSeverity_Type(TmnxPerceivedSeverity):
    """Custom type tmnxLogFilterParamsSeverity based on TmnxPerceivedSeverity"""
    defaultValue = 0


_TmnxLogFilterParamsSeverity_Type.__name__ = "TmnxPerceivedSeverity"
_TmnxLogFilterParamsSeverity_Object = MibTableColumn
tmnxLogFilterParamsSeverity = _TmnxLogFilterParamsSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 7, 1, 9),
    _TmnxLogFilterParamsSeverity_Type()
)
tmnxLogFilterParamsSeverity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogFilterParamsSeverity.setStatus("current")


class _TmnxLogFilterParamsSeverityOperator_Type(TmnxLogFilterOperator):
    """Custom type tmnxLogFilterParamsSeverityOperator based on TmnxLogFilterOperator"""
    defaultValue = 1


_TmnxLogFilterParamsSeverityOperator_Type.__name__ = "TmnxLogFilterOperator"
_TmnxLogFilterParamsSeverityOperator_Object = MibTableColumn
tmnxLogFilterParamsSeverityOperator = _TmnxLogFilterParamsSeverityOperator_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 7, 1, 10),
    _TmnxLogFilterParamsSeverityOperator_Type()
)
tmnxLogFilterParamsSeverityOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogFilterParamsSeverityOperator.setStatus("current")


class _TmnxLogFilterParamsSubject_Type(TNamedItemOrEmpty):
    """Custom type tmnxLogFilterParamsSubject based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxLogFilterParamsSubject_Type.__name__ = "TNamedItemOrEmpty"
_TmnxLogFilterParamsSubject_Object = MibTableColumn
tmnxLogFilterParamsSubject = _TmnxLogFilterParamsSubject_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 7, 1, 11),
    _TmnxLogFilterParamsSubject_Type()
)
tmnxLogFilterParamsSubject.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogFilterParamsSubject.setStatus("current")


class _TmnxLogFilterParamsSubjectOperator_Type(TmnxLogFilterOperator):
    """Custom type tmnxLogFilterParamsSubjectOperator based on TmnxLogFilterOperator"""
    defaultValue = 1


_TmnxLogFilterParamsSubjectOperator_Type.__name__ = "TmnxLogFilterOperator"
_TmnxLogFilterParamsSubjectOperator_Object = MibTableColumn
tmnxLogFilterParamsSubjectOperator = _TmnxLogFilterParamsSubjectOperator_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 7, 1, 12),
    _TmnxLogFilterParamsSubjectOperator_Type()
)
tmnxLogFilterParamsSubjectOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogFilterParamsSubjectOperator.setStatus("current")


class _TmnxLogFilterParamsSubjectRegexp_Type(TruthValue):
    """Custom type tmnxLogFilterParamsSubjectRegexp based on TruthValue"""
    defaultValue = 2


_TmnxLogFilterParamsSubjectRegexp_Type.__name__ = "TruthValue"
_TmnxLogFilterParamsSubjectRegexp_Object = MibTableColumn
tmnxLogFilterParamsSubjectRegexp = _TmnxLogFilterParamsSubjectRegexp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 7, 1, 13),
    _TmnxLogFilterParamsSubjectRegexp_Type()
)
tmnxLogFilterParamsSubjectRegexp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogFilterParamsSubjectRegexp.setStatus("current")


class _TmnxLogFilterParamsRouter_Type(TNamedItemOrEmpty):
    """Custom type tmnxLogFilterParamsRouter based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxLogFilterParamsRouter_Type.__name__ = "TNamedItemOrEmpty"
_TmnxLogFilterParamsRouter_Object = MibTableColumn
tmnxLogFilterParamsRouter = _TmnxLogFilterParamsRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 7, 1, 14),
    _TmnxLogFilterParamsRouter_Type()
)
tmnxLogFilterParamsRouter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogFilterParamsRouter.setStatus("current")


class _TmnxLogFilterParamsRouterOperator_Type(TmnxLogFilterOperator):
    """Custom type tmnxLogFilterParamsRouterOperator based on TmnxLogFilterOperator"""
    defaultValue = 1


_TmnxLogFilterParamsRouterOperator_Type.__name__ = "TmnxLogFilterOperator"
_TmnxLogFilterParamsRouterOperator_Object = MibTableColumn
tmnxLogFilterParamsRouterOperator = _TmnxLogFilterParamsRouterOperator_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 7, 1, 15),
    _TmnxLogFilterParamsRouterOperator_Type()
)
tmnxLogFilterParamsRouterOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogFilterParamsRouterOperator.setStatus("current")


class _TmnxLogFilterParamsRouterRegexp_Type(TruthValue):
    """Custom type tmnxLogFilterParamsRouterRegexp based on TruthValue"""
    defaultValue = 2


_TmnxLogFilterParamsRouterRegexp_Type.__name__ = "TruthValue"
_TmnxLogFilterParamsRouterRegexp_Object = MibTableColumn
tmnxLogFilterParamsRouterRegexp = _TmnxLogFilterParamsRouterRegexp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 7, 1, 16),
    _TmnxLogFilterParamsRouterRegexp_Type()
)
tmnxLogFilterParamsRouterRegexp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogFilterParamsRouterRegexp.setStatus("current")


class _TmnxLogFilterParamsMsg_Type(OctetString):
    """Custom type tmnxLogFilterParamsMsg based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 400),
    )


_TmnxLogFilterParamsMsg_Type.__name__ = "OctetString"
_TmnxLogFilterParamsMsg_Object = MibTableColumn
tmnxLogFilterParamsMsg = _TmnxLogFilterParamsMsg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 7, 1, 17),
    _TmnxLogFilterParamsMsg_Type()
)
tmnxLogFilterParamsMsg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogFilterParamsMsg.setStatus("current")


class _TmnxLogFilterParamsMsgOperator_Type(TmnxLogFilterOperator):
    """Custom type tmnxLogFilterParamsMsgOperator based on TmnxLogFilterOperator"""
    defaultValue = 1


_TmnxLogFilterParamsMsgOperator_Type.__name__ = "TmnxLogFilterOperator"
_TmnxLogFilterParamsMsgOperator_Object = MibTableColumn
tmnxLogFilterParamsMsgOperator = _TmnxLogFilterParamsMsgOperator_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 7, 1, 18),
    _TmnxLogFilterParamsMsgOperator_Type()
)
tmnxLogFilterParamsMsgOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogFilterParamsMsgOperator.setStatus("current")


class _TmnxLogFilterParamsMsgRegexp_Type(TruthValue):
    """Custom type tmnxLogFilterParamsMsgRegexp based on TruthValue"""
    defaultValue = 2


_TmnxLogFilterParamsMsgRegexp_Type.__name__ = "TruthValue"
_TmnxLogFilterParamsMsgRegexp_Object = MibTableColumn
tmnxLogFilterParamsMsgRegexp = _TmnxLogFilterParamsMsgRegexp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 7, 1, 19),
    _TmnxLogFilterParamsMsgRegexp_Type()
)
tmnxLogFilterParamsMsgRegexp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogFilterParamsMsgRegexp.setStatus("current")


class _TmnxLogFilterParamsName_Type(TLNamedItemOrEmpty):
    """Custom type tmnxLogFilterParamsName based on TLNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxLogFilterParamsName_Type.__name__ = "TLNamedItemOrEmpty"
_TmnxLogFilterParamsName_Object = MibTableColumn
tmnxLogFilterParamsName = _TmnxLogFilterParamsName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 7, 1, 20),
    _TmnxLogFilterParamsName_Type()
)
tmnxLogFilterParamsName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogFilterParamsName.setStatus("current")
_TmnxSyslogTargetTable_Object = MibTable
tmnxSyslogTargetTable = _TmnxSyslogTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 8)
)
if mibBuilder.loadTexts:
    tmnxSyslogTargetTable.setStatus("current")
_TmnxSyslogTargetEntry_Object = MibTableRow
tmnxSyslogTargetEntry = _TmnxSyslogTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 8, 1)
)
tmnxSyslogTargetEntry.setIndexNames(
    (0, "TIMETRA-LOG-MIB", "tmnxSyslogTargetIndex"),
)
if mibBuilder.loadTexts:
    tmnxSyslogTargetEntry.setStatus("current")
_TmnxSyslogTargetIndex_Type = TmnxSyslogId
_TmnxSyslogTargetIndex_Object = MibTableColumn
tmnxSyslogTargetIndex = _TmnxSyslogTargetIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 8, 1, 1),
    _TmnxSyslogTargetIndex_Type()
)
tmnxSyslogTargetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSyslogTargetIndex.setStatus("current")
_TmnxSyslogTargetRowStatus_Type = RowStatus
_TmnxSyslogTargetRowStatus_Object = MibTableColumn
tmnxSyslogTargetRowStatus = _TmnxSyslogTargetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 8, 1, 2),
    _TmnxSyslogTargetRowStatus_Type()
)
tmnxSyslogTargetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSyslogTargetRowStatus.setStatus("current")


class _TmnxSyslogTargetDescription_Type(TItemDescription):
    """Custom type tmnxSyslogTargetDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxSyslogTargetDescription_Type.__name__ = "TItemDescription"
_TmnxSyslogTargetDescription_Object = MibTableColumn
tmnxSyslogTargetDescription = _TmnxSyslogTargetDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 8, 1, 3),
    _TmnxSyslogTargetDescription_Type()
)
tmnxSyslogTargetDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSyslogTargetDescription.setStatus("current")


class _TmnxSyslogTargetAddress_Type(IpAddress):
    """Custom type tmnxSyslogTargetAddress based on IpAddress"""
    defaultHexValue = "00000000"


_TmnxSyslogTargetAddress_Type.__name__ = "IpAddress"
_TmnxSyslogTargetAddress_Object = MibTableColumn
tmnxSyslogTargetAddress = _TmnxSyslogTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 8, 1, 4),
    _TmnxSyslogTargetAddress_Type()
)
tmnxSyslogTargetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSyslogTargetAddress.setStatus("obsolete")


class _TmnxSyslogTargetUdpPort_Type(TmnxUdpPort):
    """Custom type tmnxSyslogTargetUdpPort based on TmnxUdpPort"""
    defaultValue = 514


_TmnxSyslogTargetUdpPort_Type.__name__ = "TmnxUdpPort"
_TmnxSyslogTargetUdpPort_Object = MibTableColumn
tmnxSyslogTargetUdpPort = _TmnxSyslogTargetUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 8, 1, 5),
    _TmnxSyslogTargetUdpPort_Type()
)
tmnxSyslogTargetUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSyslogTargetUdpPort.setStatus("current")


class _TmnxSyslogTargetFacility_Type(TmnxSyslogFacility):
    """Custom type tmnxSyslogTargetFacility based on TmnxSyslogFacility"""
    defaultValue = 23


_TmnxSyslogTargetFacility_Type.__name__ = "TmnxSyslogFacility"
_TmnxSyslogTargetFacility_Object = MibTableColumn
tmnxSyslogTargetFacility = _TmnxSyslogTargetFacility_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 8, 1, 6),
    _TmnxSyslogTargetFacility_Type()
)
tmnxSyslogTargetFacility.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSyslogTargetFacility.setStatus("current")


class _TmnxSyslogTargetSeverity_Type(TmnxSyslogSeverity):
    """Custom type tmnxSyslogTargetSeverity based on TmnxSyslogSeverity"""
    defaultValue = 6


_TmnxSyslogTargetSeverity_Type.__name__ = "TmnxSyslogSeverity"
_TmnxSyslogTargetSeverity_Object = MibTableColumn
tmnxSyslogTargetSeverity = _TmnxSyslogTargetSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 8, 1, 7),
    _TmnxSyslogTargetSeverity_Type()
)
tmnxSyslogTargetSeverity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSyslogTargetSeverity.setStatus("current")


class _TmnxSyslogTargetMessagePrefix_Type(TNamedItemOrEmpty):
    """Custom type tmnxSyslogTargetMessagePrefix based on TNamedItemOrEmpty"""
    defaultValue = OctetString("TMNX")


_TmnxSyslogTargetMessagePrefix_Type.__name__ = "TNamedItemOrEmpty"
_TmnxSyslogTargetMessagePrefix_Object = MibTableColumn
tmnxSyslogTargetMessagePrefix = _TmnxSyslogTargetMessagePrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 8, 1, 8),
    _TmnxSyslogTargetMessagePrefix_Type()
)
tmnxSyslogTargetMessagePrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSyslogTargetMessagePrefix.setStatus("current")
_TmnxSyslogTargetMessagesDropped_Type = Counter32
_TmnxSyslogTargetMessagesDropped_Object = MibTableColumn
tmnxSyslogTargetMessagesDropped = _TmnxSyslogTargetMessagesDropped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 8, 1, 9),
    _TmnxSyslogTargetMessagesDropped_Type()
)
tmnxSyslogTargetMessagesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyslogTargetMessagesDropped.setStatus("current")


class _TmnxSyslogTargetAddrType_Type(InetAddressType):
    """Custom type tmnxSyslogTargetAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxSyslogTargetAddrType_Type.__name__ = "InetAddressType"
_TmnxSyslogTargetAddrType_Object = MibTableColumn
tmnxSyslogTargetAddrType = _TmnxSyslogTargetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 8, 1, 10),
    _TmnxSyslogTargetAddrType_Type()
)
tmnxSyslogTargetAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSyslogTargetAddrType.setStatus("current")


class _TmnxSyslogTargetAddr_Type(InetAddress):
    """Custom type tmnxSyslogTargetAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxSyslogTargetAddr_Type.__name__ = "InetAddress"
_TmnxSyslogTargetAddr_Object = MibTableColumn
tmnxSyslogTargetAddr = _TmnxSyslogTargetAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 8, 1, 11),
    _TmnxSyslogTargetAddr_Type()
)
tmnxSyslogTargetAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSyslogTargetAddr.setStatus("current")


class _TmnxSyslogTargetName_Type(TLNamedItemOrEmpty):
    """Custom type tmnxSyslogTargetName based on TLNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxSyslogTargetName_Type.__name__ = "TLNamedItemOrEmpty"
_TmnxSyslogTargetName_Object = MibTableColumn
tmnxSyslogTargetName = _TmnxSyslogTargetName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 8, 1, 12),
    _TmnxSyslogTargetName_Type()
)
tmnxSyslogTargetName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSyslogTargetName.setStatus("current")


class _TmnxSyslogTlsClntProfileName_Type(TNamedItemOrEmpty):
    """Custom type tmnxSyslogTlsClntProfileName based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxSyslogTlsClntProfileName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxSyslogTlsClntProfileName_Object = MibTableColumn
tmnxSyslogTlsClntProfileName = _TmnxSyslogTlsClntProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 8, 1, 13),
    _TmnxSyslogTlsClntProfileName_Type()
)
tmnxSyslogTlsClntProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSyslogTlsClntProfileName.setStatus("current")
_TmnxEventAppTable_Object = MibTable
tmnxEventAppTable = _TmnxEventAppTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 9)
)
if mibBuilder.loadTexts:
    tmnxEventAppTable.setStatus("current")
_TmnxEventAppEntry_Object = MibTableRow
tmnxEventAppEntry = _TmnxEventAppEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 9, 1)
)
tmnxEventAppEntry.setIndexNames(
    (0, "TIMETRA-LOG-MIB", "tmnxEventAppIndex"),
)
if mibBuilder.loadTexts:
    tmnxEventAppEntry.setStatus("current")
_TmnxEventAppIndex_Type = Unsigned32
_TmnxEventAppIndex_Object = MibTableColumn
tmnxEventAppIndex = _TmnxEventAppIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 9, 1, 1),
    _TmnxEventAppIndex_Type()
)
tmnxEventAppIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxEventAppIndex.setStatus("current")
_TmnxEventAppName_Type = TNamedItem
_TmnxEventAppName_Object = MibTableColumn
tmnxEventAppName = _TmnxEventAppName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 9, 1, 2),
    _TmnxEventAppName_Type()
)
tmnxEventAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEventAppName.setStatus("current")
_TmnxEventTable_Object = MibTable
tmnxEventTable = _TmnxEventTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 10)
)
if mibBuilder.loadTexts:
    tmnxEventTable.setStatus("current")
_TmnxEventEntry_Object = MibTableRow
tmnxEventEntry = _TmnxEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 10, 1)
)
tmnxEventEntry.setIndexNames(
    (0, "TIMETRA-LOG-MIB", "tmnxEventAppIndex"),
    (0, "TIMETRA-LOG-MIB", "tmnxEventID"),
)
if mibBuilder.loadTexts:
    tmnxEventEntry.setStatus("current")
_TmnxEventID_Type = Unsigned32
_TmnxEventID_Object = MibTableColumn
tmnxEventID = _TmnxEventID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 10, 1, 1),
    _TmnxEventID_Type()
)
tmnxEventID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxEventID.setStatus("current")
_TmnxEventName_Type = TNamedItem
_TmnxEventName_Object = MibTableColumn
tmnxEventName = _TmnxEventName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 10, 1, 2),
    _TmnxEventName_Type()
)
tmnxEventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEventName.setStatus("current")
_TmnxEventSeverity_Type = TmnxPerceivedSeverity
_TmnxEventSeverity_Object = MibTableColumn
tmnxEventSeverity = _TmnxEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 10, 1, 3),
    _TmnxEventSeverity_Type()
)
tmnxEventSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxEventSeverity.setStatus("current")
_TmnxEventControl_Type = TruthValue
_TmnxEventControl_Object = MibTableColumn
tmnxEventControl = _TmnxEventControl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 10, 1, 4),
    _TmnxEventControl_Type()
)
tmnxEventControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxEventControl.setStatus("current")
_TmnxEventCounter_Type = Counter32
_TmnxEventCounter_Object = MibTableColumn
tmnxEventCounter = _TmnxEventCounter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 10, 1, 5),
    _TmnxEventCounter_Type()
)
tmnxEventCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEventCounter.setStatus("current")
_TmnxEventDropCount_Type = Counter32
_TmnxEventDropCount_Object = MibTableColumn
tmnxEventDropCount = _TmnxEventDropCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 10, 1, 6),
    _TmnxEventDropCount_Type()
)
tmnxEventDropCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEventDropCount.setStatus("current")


class _TmnxEventReset_Type(TmnxActionType):
    """Custom type tmnxEventReset based on TmnxActionType"""
    defaultValue = 2


_TmnxEventReset_Type.__name__ = "TmnxActionType"
_TmnxEventReset_Object = MibTableColumn
tmnxEventReset = _TmnxEventReset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 10, 1, 7),
    _TmnxEventReset_Type()
)
tmnxEventReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxEventReset.setStatus("current")


class _TmnxEventThrottle_Type(TruthValue):
    """Custom type tmnxEventThrottle based on TruthValue"""
    defaultValue = 2


_TmnxEventThrottle_Type.__name__ = "TruthValue"
_TmnxEventThrottle_Object = MibTableColumn
tmnxEventThrottle = _TmnxEventThrottle_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 10, 1, 8),
    _TmnxEventThrottle_Type()
)
tmnxEventThrottle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxEventThrottle.setStatus("current")
_TmnxEventSpecThrottle_Type = TruthValue
_TmnxEventSpecThrottle_Object = MibTableColumn
tmnxEventSpecThrottle = _TmnxEventSpecThrottle_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 10, 1, 9),
    _TmnxEventSpecThrottle_Type()
)
tmnxEventSpecThrottle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxEventSpecThrottle.setStatus("current")


class _TmnxEventSpecThrottleLimit_Type(Unsigned32):
    """Custom type tmnxEventSpecThrottleLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 20000),
    )


_TmnxEventSpecThrottleLimit_Type.__name__ = "Unsigned32"
_TmnxEventSpecThrottleLimit_Object = MibTableColumn
tmnxEventSpecThrottleLimit = _TmnxEventSpecThrottleLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 10, 1, 10),
    _TmnxEventSpecThrottleLimit_Type()
)
tmnxEventSpecThrottleLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxEventSpecThrottleLimit.setStatus("current")
if mibBuilder.loadTexts:
    tmnxEventSpecThrottleLimit.setUnits("events")


class _TmnxEventSpecThrottleIntval_Type(Unsigned32):
    """Custom type tmnxEventSpecThrottleIntval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1200),
    )


_TmnxEventSpecThrottleIntval_Type.__name__ = "Unsigned32"
_TmnxEventSpecThrottleIntval_Object = MibTableColumn
tmnxEventSpecThrottleIntval = _TmnxEventSpecThrottleIntval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 10, 1, 11),
    _TmnxEventSpecThrottleIntval_Type()
)
tmnxEventSpecThrottleIntval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxEventSpecThrottleIntval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxEventSpecThrottleIntval.setUnits("seconds")
_TmnxEventSpecThrottleDef_Type = TruthValue
_TmnxEventSpecThrottleDef_Object = MibTableColumn
tmnxEventSpecThrottleDef = _TmnxEventSpecThrottleDef_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 10, 1, 12),
    _TmnxEventSpecThrottleDef_Type()
)
tmnxEventSpecThrottleDef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEventSpecThrottleDef.setStatus("current")


class _TmnxEventSpecThrottleLimitDef_Type(Unsigned32):
    """Custom type tmnxEventSpecThrottleLimitDef based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 20000),
    )


_TmnxEventSpecThrottleLimitDef_Type.__name__ = "Unsigned32"
_TmnxEventSpecThrottleLimitDef_Object = MibTableColumn
tmnxEventSpecThrottleLimitDef = _TmnxEventSpecThrottleLimitDef_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 10, 1, 13),
    _TmnxEventSpecThrottleLimitDef_Type()
)
tmnxEventSpecThrottleLimitDef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEventSpecThrottleLimitDef.setStatus("current")
if mibBuilder.loadTexts:
    tmnxEventSpecThrottleLimitDef.setUnits("events")


class _TmnxEventSpecThrottleIntvalDef_Type(Unsigned32):
    """Custom type tmnxEventSpecThrottleIntvalDef based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1200),
    )


_TmnxEventSpecThrottleIntvalDef_Type.__name__ = "Unsigned32"
_TmnxEventSpecThrottleIntvalDef_Object = MibTableColumn
tmnxEventSpecThrottleIntvalDef = _TmnxEventSpecThrottleIntvalDef_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 10, 1, 14),
    _TmnxEventSpecThrottleIntvalDef_Type()
)
tmnxEventSpecThrottleIntvalDef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEventSpecThrottleIntvalDef.setStatus("current")
if mibBuilder.loadTexts:
    tmnxEventSpecThrottleIntvalDef.setUnits("seconds")


class _TmnxEventRepeat_Type(TruthValue):
    """Custom type tmnxEventRepeat based on TruthValue"""
    defaultValue = 2


_TmnxEventRepeat_Type.__name__ = "TruthValue"
_TmnxEventRepeat_Object = MibTableColumn
tmnxEventRepeat = _TmnxEventRepeat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 10, 1, 15),
    _TmnxEventRepeat_Type()
)
tmnxEventRepeat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxEventRepeat.setStatus("current")
_TmnxSnmpTrapGroupTable_Object = MibTable
tmnxSnmpTrapGroupTable = _TmnxSnmpTrapGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 11)
)
if mibBuilder.loadTexts:
    tmnxSnmpTrapGroupTable.setStatus("obsolete")
_TmnxSnmpTrapGroupEntry_Object = MibTableRow
tmnxSnmpTrapGroupEntry = _TmnxSnmpTrapGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 11, 1)
)
tmnxSnmpTrapGroupEntry.setIndexNames(
    (0, "TIMETRA-LOG-MIB", "tmnxStgIndex"),
    (0, "TIMETRA-LOG-MIB", "tmnxStgDestAddress"),
    (0, "TIMETRA-LOG-MIB", "tmnxStgDestPort"),
)
if mibBuilder.loadTexts:
    tmnxSnmpTrapGroupEntry.setStatus("obsolete")
_TmnxStgIndex_Type = TmnxStgIndex
_TmnxStgIndex_Object = MibTableColumn
tmnxStgIndex = _TmnxStgIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 11, 1, 1),
    _TmnxStgIndex_Type()
)
tmnxStgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxStgIndex.setStatus("obsolete")


class _TmnxStgDestAddress_Type(IpAddress):
    """Custom type tmnxStgDestAddress based on IpAddress"""
    defaultHexValue = "00000000"


_TmnxStgDestAddress_Type.__name__ = "IpAddress"
_TmnxStgDestAddress_Object = MibTableColumn
tmnxStgDestAddress = _TmnxStgDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 11, 1, 2),
    _TmnxStgDestAddress_Type()
)
tmnxStgDestAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxStgDestAddress.setStatus("obsolete")


class _TmnxStgDestPort_Type(TmnxUdpPort):
    """Custom type tmnxStgDestPort based on TmnxUdpPort"""
    defaultValue = 162


_TmnxStgDestPort_Type.__name__ = "TmnxUdpPort"
_TmnxStgDestPort_Object = MibTableColumn
tmnxStgDestPort = _TmnxStgDestPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 11, 1, 3),
    _TmnxStgDestPort_Type()
)
tmnxStgDestPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxStgDestPort.setStatus("obsolete")
_TmnxStgRowStatus_Type = RowStatus
_TmnxStgRowStatus_Object = MibTableColumn
tmnxStgRowStatus = _TmnxStgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 11, 1, 4),
    _TmnxStgRowStatus_Type()
)
tmnxStgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxStgRowStatus.setStatus("obsolete")


class _TmnxStgDescription_Type(TItemDescription):
    """Custom type tmnxStgDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxStgDescription_Type.__name__ = "TItemDescription"
_TmnxStgDescription_Object = MibTableColumn
tmnxStgDescription = _TmnxStgDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 11, 1, 5),
    _TmnxStgDescription_Type()
)
tmnxStgDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxStgDescription.setStatus("obsolete")


class _TmnxStgVersion_Type(SnmpMessageProcessingModel):
    """Custom type tmnxStgVersion based on SnmpMessageProcessingModel"""
    defaultValue = 3


_TmnxStgVersion_Type.__name__ = "SnmpMessageProcessingModel"
_TmnxStgVersion_Object = MibTableColumn
tmnxStgVersion = _TmnxStgVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 11, 1, 6),
    _TmnxStgVersion_Type()
)
tmnxStgVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxStgVersion.setStatus("obsolete")


class _TmnxStgNotifyCommunity_Type(OctetString):
    """Custom type tmnxStgNotifyCommunity based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TmnxStgNotifyCommunity_Type.__name__ = "OctetString"
_TmnxStgNotifyCommunity_Object = MibTableColumn
tmnxStgNotifyCommunity = _TmnxStgNotifyCommunity_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 11, 1, 7),
    _TmnxStgNotifyCommunity_Type()
)
tmnxStgNotifyCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxStgNotifyCommunity.setStatus("obsolete")


class _TmnxStgSecurityLevel_Type(SnmpSecurityLevel):
    """Custom type tmnxStgSecurityLevel based on SnmpSecurityLevel"""
    defaultValue = 1


_TmnxStgSecurityLevel_Type.__name__ = "SnmpSecurityLevel"
_TmnxStgSecurityLevel_Object = MibTableColumn
tmnxStgSecurityLevel = _TmnxStgSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 11, 1, 8),
    _TmnxStgSecurityLevel_Type()
)
tmnxStgSecurityLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxStgSecurityLevel.setStatus("obsolete")


class _TmnxEventTest_Type(TmnxActionType):
    """Custom type tmnxEventTest based on TmnxActionType"""
    defaultValue = 2


_TmnxEventTest_Type.__name__ = "TmnxActionType"
_TmnxEventTest_Object = MibScalar
tmnxEventTest = _TmnxEventTest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 12),
    _TmnxEventTest_Type()
)
tmnxEventTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxEventTest.setStatus("current")


class _TmnxEventThrottleLimit_Type(Unsigned32):
    """Custom type tmnxEventThrottleLimit based on Unsigned32"""
    defaultValue = 2000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20000),
    )


_TmnxEventThrottleLimit_Type.__name__ = "Unsigned32"
_TmnxEventThrottleLimit_Object = MibScalar
tmnxEventThrottleLimit = _TmnxEventThrottleLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 13),
    _TmnxEventThrottleLimit_Type()
)
tmnxEventThrottleLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxEventThrottleLimit.setStatus("current")
if mibBuilder.loadTexts:
    tmnxEventThrottleLimit.setUnits("events")


class _TmnxEventThrottleInterval_Type(Unsigned32):
    """Custom type tmnxEventThrottleInterval based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1200),
    )


_TmnxEventThrottleInterval_Type.__name__ = "Unsigned32"
_TmnxEventThrottleInterval_Object = MibScalar
tmnxEventThrottleInterval = _TmnxEventThrottleInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 14),
    _TmnxEventThrottleInterval_Type()
)
tmnxEventThrottleInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxEventThrottleInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxEventThrottleInterval.setUnits("seconds")
_TmnxSnmpSetErrsMax_Type = Unsigned32
_TmnxSnmpSetErrsMax_Object = MibScalar
tmnxSnmpSetErrsMax = _TmnxSnmpSetErrsMax_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 15),
    _TmnxSnmpSetErrsMax_Type()
)
tmnxSnmpSetErrsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSnmpSetErrsMax.setStatus("current")
_TmnxSnmpSetErrsTable_Object = MibTable
tmnxSnmpSetErrsTable = _TmnxSnmpSetErrsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 16)
)
if mibBuilder.loadTexts:
    tmnxSnmpSetErrsTable.setStatus("current")
_TmnxSnmpSetErrsEntry_Object = MibTableRow
tmnxSnmpSetErrsEntry = _TmnxSnmpSetErrsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 16, 1)
)
tmnxSnmpSetErrsEntry.setIndexNames(
    (0, "TIMETRA-LOG-MIB", "tmnxSseAddressType"),
    (0, "TIMETRA-LOG-MIB", "tmnxSseAddress"),
    (0, "TIMETRA-LOG-MIB", "tmnxSseSnmpPort"),
    (0, "TIMETRA-LOG-MIB", "tmnxSseRequestId"),
)
if mibBuilder.loadTexts:
    tmnxSnmpSetErrsEntry.setStatus("current")
_TmnxSseAddressType_Type = InetAddressType
_TmnxSseAddressType_Object = MibTableColumn
tmnxSseAddressType = _TmnxSseAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 16, 1, 1),
    _TmnxSseAddressType_Type()
)
tmnxSseAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSseAddressType.setStatus("current")


class _TmnxSseAddress_Type(InetAddress):
    """Custom type tmnxSseAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxSseAddress_Type.__name__ = "InetAddress"
_TmnxSseAddress_Object = MibTableColumn
tmnxSseAddress = _TmnxSseAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 16, 1, 2),
    _TmnxSseAddress_Type()
)
tmnxSseAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSseAddress.setStatus("current")
_TmnxSseSnmpPort_Type = TmnxUdpPort
_TmnxSseSnmpPort_Object = MibTableColumn
tmnxSseSnmpPort = _TmnxSseSnmpPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 16, 1, 3),
    _TmnxSseSnmpPort_Type()
)
tmnxSseSnmpPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSseSnmpPort.setStatus("current")
_TmnxSseRequestId_Type = Unsigned32
_TmnxSseRequestId_Object = MibTableColumn
tmnxSseRequestId = _TmnxSseRequestId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 16, 1, 4),
    _TmnxSseRequestId_Type()
)
tmnxSseRequestId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSseRequestId.setStatus("current")
_TmnxSseVersion_Type = SnmpMessageProcessingModel
_TmnxSseVersion_Object = MibTableColumn
tmnxSseVersion = _TmnxSseVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 16, 1, 5),
    _TmnxSseVersion_Type()
)
tmnxSseVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSseVersion.setStatus("current")
_TmnxSseSeverityLevel_Type = TmnxPerceivedSeverity
_TmnxSseSeverityLevel_Object = MibTableColumn
tmnxSseSeverityLevel = _TmnxSseSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 16, 1, 6),
    _TmnxSseSeverityLevel_Type()
)
tmnxSseSeverityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSseSeverityLevel.setStatus("current")
_TmnxSseModuleId_Type = Unsigned32
_TmnxSseModuleId_Object = MibTableColumn
tmnxSseModuleId = _TmnxSseModuleId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 16, 1, 7),
    _TmnxSseModuleId_Type()
)
tmnxSseModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSseModuleId.setStatus("current")
_TmnxSseModuleName_Type = TNamedItem
_TmnxSseModuleName_Object = MibTableColumn
tmnxSseModuleName = _TmnxSseModuleName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 16, 1, 8),
    _TmnxSseModuleName_Type()
)
tmnxSseModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSseModuleName.setStatus("current")
_TmnxSseErrorCode_Type = Unsigned32
_TmnxSseErrorCode_Object = MibTableColumn
tmnxSseErrorCode = _TmnxSseErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 16, 1, 9),
    _TmnxSseErrorCode_Type()
)
tmnxSseErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSseErrorCode.setStatus("current")


class _TmnxSseErrorName_Type(DisplayString):
    """Custom type tmnxSseErrorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TmnxSseErrorName_Type.__name__ = "DisplayString"
_TmnxSseErrorName_Object = MibTableColumn
tmnxSseErrorName = _TmnxSseErrorName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 16, 1, 10),
    _TmnxSseErrorName_Type()
)
tmnxSseErrorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSseErrorName.setStatus("current")


class _TmnxSseErrorMsg_Type(DisplayString):
    """Custom type tmnxSseErrorMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_TmnxSseErrorMsg_Type.__name__ = "DisplayString"
_TmnxSseErrorMsg_Object = MibTableColumn
tmnxSseErrorMsg = _TmnxSseErrorMsg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 16, 1, 11),
    _TmnxSseErrorMsg_Type()
)
tmnxSseErrorMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSseErrorMsg.setStatus("current")


class _TmnxSseExtraText_Type(OctetString):
    """Custom type tmnxSseExtraText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 320),
    )


_TmnxSseExtraText_Type.__name__ = "OctetString"
_TmnxSseExtraText_Object = MibTableColumn
tmnxSseExtraText = _TmnxSseExtraText_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 16, 1, 12),
    _TmnxSseExtraText_Type()
)
tmnxSseExtraText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSseExtraText.setStatus("current")
_TmnxSseTimestamp_Type = TimeStamp
_TmnxSseTimestamp_Object = MibTableColumn
tmnxSseTimestamp = _TmnxSseTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 16, 1, 13),
    _TmnxSseTimestamp_Type()
)
tmnxSseTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSseTimestamp.setStatus("current")
_TmnxSnmpTrapLogTable_Object = MibTable
tmnxSnmpTrapLogTable = _TmnxSnmpTrapLogTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 17)
)
if mibBuilder.loadTexts:
    tmnxSnmpTrapLogTable.setStatus("current")
_TmnxSnmpTrapLogEntry_Object = MibTableRow
tmnxSnmpTrapLogEntry = _TmnxSnmpTrapLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 17, 1)
)
if mibBuilder.loadTexts:
    tmnxSnmpTrapLogEntry.setStatus("current")


class _TmnxSnmpTrapLogDescription_Type(TItemDescription):
    """Custom type tmnxSnmpTrapLogDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxSnmpTrapLogDescription_Type.__name__ = "TItemDescription"
_TmnxSnmpTrapLogDescription_Object = MibTableColumn
tmnxSnmpTrapLogDescription = _TmnxSnmpTrapLogDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 17, 1, 1),
    _TmnxSnmpTrapLogDescription_Type()
)
tmnxSnmpTrapLogDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSnmpTrapLogDescription.setStatus("current")


class _SnmpNotifyId_Type(TmnxLogIdIndex):
    """Custom type snmpNotifyId based on TmnxLogIdIndex"""
    subtypeSpec = TmnxLogIdIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SnmpNotifyId_Type.__name__ = "TmnxLogIdIndex"
_SnmpNotifyId_Object = MibTableColumn
snmpNotifyId = _SnmpNotifyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 17, 1, 2),
    _SnmpNotifyId_Type()
)
snmpNotifyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpNotifyId.setStatus("current")
_TmnxSnmpTrapDestTable_Object = MibTable
tmnxSnmpTrapDestTable = _TmnxSnmpTrapDestTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 18)
)
if mibBuilder.loadTexts:
    tmnxSnmpTrapDestTable.setStatus("current")
_TmnxSnmpTrapDestEntry_Object = MibTableRow
tmnxSnmpTrapDestEntry = _TmnxSnmpTrapDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 18, 1)
)
tmnxSnmpTrapDestEntry.setIndexNames(
    (0, "TIMETRA-LOG-MIB", "tmnxStdIndex"),
    (1, "TIMETRA-LOG-MIB", "tmnxStdName"),
)
if mibBuilder.loadTexts:
    tmnxSnmpTrapDestEntry.setStatus("current")
_TmnxStdIndex_Type = TmnxStgIndex
_TmnxStdIndex_Object = MibTableColumn
tmnxStdIndex = _TmnxStdIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 18, 1, 1),
    _TmnxStdIndex_Type()
)
tmnxStdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxStdIndex.setStatus("current")


class _TmnxStdName_Type(SnmpAdminString):
    """Custom type tmnxStdName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 28),
    )


_TmnxStdName_Type.__name__ = "SnmpAdminString"
_TmnxStdName_Object = MibTableColumn
tmnxStdName = _TmnxStdName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 18, 1, 2),
    _TmnxStdName_Type()
)
tmnxStdName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxStdName.setStatus("current")
_TmnxStdRowStatus_Type = RowStatus
_TmnxStdRowStatus_Object = MibTableColumn
tmnxStdRowStatus = _TmnxStdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 18, 1, 3),
    _TmnxStdRowStatus_Type()
)
tmnxStdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxStdRowStatus.setStatus("current")
_TmnxStdRowLastChanged_Type = TimeStamp
_TmnxStdRowLastChanged_Object = MibTableColumn
tmnxStdRowLastChanged = _TmnxStdRowLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 18, 1, 4),
    _TmnxStdRowLastChanged_Type()
)
tmnxStdRowLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxStdRowLastChanged.setStatus("current")


class _TmnxStdDestAddrType_Type(InetAddressType):
    """Custom type tmnxStdDestAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxStdDestAddrType_Type.__name__ = "InetAddressType"
_TmnxStdDestAddrType_Object = MibTableColumn
tmnxStdDestAddrType = _TmnxStdDestAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 18, 1, 5),
    _TmnxStdDestAddrType_Type()
)
tmnxStdDestAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxStdDestAddrType.setStatus("current")


class _TmnxStdDestAddr_Type(InetAddress):
    """Custom type tmnxStdDestAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxStdDestAddr_Type.__name__ = "InetAddress"
_TmnxStdDestAddr_Object = MibTableColumn
tmnxStdDestAddr = _TmnxStdDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 18, 1, 6),
    _TmnxStdDestAddr_Type()
)
tmnxStdDestAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxStdDestAddr.setStatus("current")


class _TmnxStdDestPort_Type(TmnxUdpPort):
    """Custom type tmnxStdDestPort based on TmnxUdpPort"""
    defaultValue = 162


_TmnxStdDestPort_Type.__name__ = "TmnxUdpPort"
_TmnxStdDestPort_Object = MibTableColumn
tmnxStdDestPort = _TmnxStdDestPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 18, 1, 7),
    _TmnxStdDestPort_Type()
)
tmnxStdDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxStdDestPort.setStatus("current")


class _TmnxStdDescription_Type(TItemDescription):
    """Custom type tmnxStdDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxStdDescription_Type.__name__ = "TItemDescription"
_TmnxStdDescription_Object = MibTableColumn
tmnxStdDescription = _TmnxStdDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 18, 1, 8),
    _TmnxStdDescription_Type()
)
tmnxStdDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxStdDescription.setStatus("current")


class _TmnxStdVersion_Type(SnmpMessageProcessingModel):
    """Custom type tmnxStdVersion based on SnmpMessageProcessingModel"""
    defaultValue = 3


_TmnxStdVersion_Type.__name__ = "SnmpMessageProcessingModel"
_TmnxStdVersion_Object = MibTableColumn
tmnxStdVersion = _TmnxStdVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 18, 1, 9),
    _TmnxStdVersion_Type()
)
tmnxStdVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxStdVersion.setStatus("current")


class _TmnxStdNotifyCommunity_Type(OctetString):
    """Custom type tmnxStdNotifyCommunity based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TmnxStdNotifyCommunity_Type.__name__ = "OctetString"
_TmnxStdNotifyCommunity_Object = MibTableColumn
tmnxStdNotifyCommunity = _TmnxStdNotifyCommunity_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 18, 1, 10),
    _TmnxStdNotifyCommunity_Type()
)
tmnxStdNotifyCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxStdNotifyCommunity.setStatus("current")


class _TmnxStdSecurityLevel_Type(SnmpSecurityLevel):
    """Custom type tmnxStdSecurityLevel based on SnmpSecurityLevel"""
    defaultValue = 1


_TmnxStdSecurityLevel_Type.__name__ = "SnmpSecurityLevel"
_TmnxStdSecurityLevel_Object = MibTableColumn
tmnxStdSecurityLevel = _TmnxStdSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 18, 1, 11),
    _TmnxStdSecurityLevel_Type()
)
tmnxStdSecurityLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxStdSecurityLevel.setStatus("current")


class _TmnxStdReplay_Type(TruthValue):
    """Custom type tmnxStdReplay based on TruthValue"""
    defaultValue = 2


_TmnxStdReplay_Type.__name__ = "TruthValue"
_TmnxStdReplay_Object = MibTableColumn
tmnxStdReplay = _TmnxStdReplay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 18, 1, 12),
    _TmnxStdReplay_Type()
)
tmnxStdReplay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxStdReplay.setStatus("current")
_TmnxStdReplayStart_Type = Unsigned32
_TmnxStdReplayStart_Object = MibTableColumn
tmnxStdReplayStart = _TmnxStdReplayStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 18, 1, 13),
    _TmnxStdReplayStart_Type()
)
tmnxStdReplayStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxStdReplayStart.setStatus("current")
_TmnxStdReplayLastTime_Type = TimeStamp
_TmnxStdReplayLastTime_Object = MibTableColumn
tmnxStdReplayLastTime = _TmnxStdReplayLastTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 18, 1, 14),
    _TmnxStdReplayLastTime_Type()
)
tmnxStdReplayLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxStdReplayLastTime.setStatus("current")


class _TmnxStdDyingGasp_Type(TruthValue):
    """Custom type tmnxStdDyingGasp based on TruthValue"""
    defaultValue = 2


_TmnxStdDyingGasp_Type.__name__ = "TruthValue"
_TmnxStdDyingGasp_Object = MibTableColumn
tmnxStdDyingGasp = _TmnxStdDyingGasp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 18, 1, 15),
    _TmnxStdDyingGasp_Type()
)
tmnxStdDyingGasp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxStdDyingGasp.setStatus("current")


class _TmnxStdMaxTargets_Type(Unsigned32):
    """Custom type tmnxStdMaxTargets based on Unsigned32"""
    defaultValue = 25

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100),
    )


_TmnxStdMaxTargets_Type.__name__ = "Unsigned32"
_TmnxStdMaxTargets_Object = MibScalar
tmnxStdMaxTargets = _TmnxStdMaxTargets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 19),
    _TmnxStdMaxTargets_Type()
)
tmnxStdMaxTargets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxStdMaxTargets.setStatus("current")
if mibBuilder.loadTexts:
    tmnxStdMaxTargets.setUnits("trap-targets")
_TmnxLogApCustRecordTable_Object = MibTable
tmnxLogApCustRecordTable = _TmnxLogApCustRecordTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 20)
)
if mibBuilder.loadTexts:
    tmnxLogApCustRecordTable.setStatus("current")
_TmnxLogApCustRecordEntry_Object = MibTableRow
tmnxLogApCustRecordEntry = _TmnxLogApCustRecordEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 20, 1)
)
if mibBuilder.loadTexts:
    tmnxLogApCustRecordEntry.setStatus("current")
_TmnxLogApCrLastChanged_Type = TimeStamp
_TmnxLogApCrLastChanged_Object = MibTableColumn
tmnxLogApCrLastChanged = _TmnxLogApCrLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 20, 1, 1),
    _TmnxLogApCrLastChanged_Type()
)
tmnxLogApCrLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogApCrLastChanged.setStatus("current")


class _TmnxLogApCrSignChangeDelta_Type(Unsigned32):
    """Custom type tmnxLogApCrSignChangeDelta based on Unsigned32"""
    defaultValue = 0


_TmnxLogApCrSignChangeDelta_Type.__name__ = "Unsigned32"
_TmnxLogApCrSignChangeDelta_Object = MibTableColumn
tmnxLogApCrSignChangeDelta = _TmnxLogApCrSignChangeDelta_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 20, 1, 2),
    _TmnxLogApCrSignChangeDelta_Type()
)
tmnxLogApCrSignChangeDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLogApCrSignChangeDelta.setStatus("current")


class _TmnxLogApCrSignChangeQueue_Type(TQueueIdOrAll):
    """Custom type tmnxLogApCrSignChangeQueue based on TQueueIdOrAll"""
    defaultValue = 0


_TmnxLogApCrSignChangeQueue_Type.__name__ = "TQueueIdOrAll"
_TmnxLogApCrSignChangeQueue_Object = MibTableColumn
tmnxLogApCrSignChangeQueue = _TmnxLogApCrSignChangeQueue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 20, 1, 3),
    _TmnxLogApCrSignChangeQueue_Type()
)
tmnxLogApCrSignChangeQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLogApCrSignChangeQueue.setStatus("current")


class _TmnxLogApCrSignChangeOCntr_Type(THsmdaCounterIdOrZeroOrAll):
    """Custom type tmnxLogApCrSignChangeOCntr based on THsmdaCounterIdOrZeroOrAll"""
    defaultValue = 0


_TmnxLogApCrSignChangeOCntr_Type.__name__ = "THsmdaCounterIdOrZeroOrAll"
_TmnxLogApCrSignChangeOCntr_Object = MibTableColumn
tmnxLogApCrSignChangeOCntr = _TmnxLogApCrSignChangeOCntr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 20, 1, 4),
    _TmnxLogApCrSignChangeOCntr_Type()
)
tmnxLogApCrSignChangeOCntr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLogApCrSignChangeOCntr.setStatus("obsolete")


class _TmnxLogApCrSignChangeQICounters_Type(TmnxAccPlcyQICounters):
    """Custom type tmnxLogApCrSignChangeQICounters based on TmnxAccPlcyQICounters"""
    defaultBinValue = "0"


_TmnxLogApCrSignChangeQICounters_Type.__name__ = "TmnxAccPlcyQICounters"
_TmnxLogApCrSignChangeQICounters_Object = MibTableColumn
tmnxLogApCrSignChangeQICounters = _TmnxLogApCrSignChangeQICounters_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 20, 1, 5),
    _TmnxLogApCrSignChangeQICounters_Type()
)
tmnxLogApCrSignChangeQICounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLogApCrSignChangeQICounters.setStatus("current")


class _TmnxLogApCrSignChangeQECounters_Type(TmnxAccPlcyQECounters):
    """Custom type tmnxLogApCrSignChangeQECounters based on TmnxAccPlcyQECounters"""
    defaultBinValue = "0"


_TmnxLogApCrSignChangeQECounters_Type.__name__ = "TmnxAccPlcyQECounters"
_TmnxLogApCrSignChangeQECounters_Object = MibTableColumn
tmnxLogApCrSignChangeQECounters = _TmnxLogApCrSignChangeQECounters_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 20, 1, 6),
    _TmnxLogApCrSignChangeQECounters_Type()
)
tmnxLogApCrSignChangeQECounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLogApCrSignChangeQECounters.setStatus("current")


class _TmnxLogApCrSignChangeOICounters_Type(TmnxAccPlcyOICounters):
    """Custom type tmnxLogApCrSignChangeOICounters based on TmnxAccPlcyOICounters"""
    defaultBinValue = "0"


_TmnxLogApCrSignChangeOICounters_Type.__name__ = "TmnxAccPlcyOICounters"
_TmnxLogApCrSignChangeOICounters_Object = MibTableColumn
tmnxLogApCrSignChangeOICounters = _TmnxLogApCrSignChangeOICounters_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 20, 1, 7),
    _TmnxLogApCrSignChangeOICounters_Type()
)
tmnxLogApCrSignChangeOICounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLogApCrSignChangeOICounters.setStatus("obsolete")


class _TmnxLogApCrSignChangeOECounters_Type(TmnxAccPlcyOECounters):
    """Custom type tmnxLogApCrSignChangeOECounters based on TmnxAccPlcyOECounters"""
    defaultBinValue = "0"


_TmnxLogApCrSignChangeOECounters_Type.__name__ = "TmnxAccPlcyOECounters"
_TmnxLogApCrSignChangeOECounters_Object = MibTableColumn
tmnxLogApCrSignChangeOECounters = _TmnxLogApCrSignChangeOECounters_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 20, 1, 8),
    _TmnxLogApCrSignChangeOECounters_Type()
)
tmnxLogApCrSignChangeOECounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLogApCrSignChangeOECounters.setStatus("obsolete")


class _TmnxLogApCrSignChangeAACounters_Type(TmnxAccPlcyAACounters):
    """Custom type tmnxLogApCrSignChangeAACounters based on TmnxAccPlcyAACounters"""
    defaultBinValue = "0"


_TmnxLogApCrSignChangeAACounters_Type.__name__ = "TmnxAccPlcyAACounters"
_TmnxLogApCrSignChangeAACounters_Object = MibTableColumn
tmnxLogApCrSignChangeAACounters = _TmnxLogApCrSignChangeAACounters_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 20, 1, 9),
    _TmnxLogApCrSignChangeAACounters_Type()
)
tmnxLogApCrSignChangeAACounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLogApCrSignChangeAACounters.setStatus("current")


class _TmnxLogApCrAACounters_Type(TmnxAccPlcyAACounters):
    """Custom type tmnxLogApCrAACounters based on TmnxAccPlcyAACounters"""
    defaultBinValue = "0"


_TmnxLogApCrAACounters_Type.__name__ = "TmnxAccPlcyAACounters"
_TmnxLogApCrAACounters_Object = MibTableColumn
tmnxLogApCrAACounters = _TmnxLogApCrAACounters_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 20, 1, 10),
    _TmnxLogApCrAACounters_Type()
)
tmnxLogApCrAACounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLogApCrAACounters.setStatus("current")


class _TmnxLogApCrAASubAttributes_Type(TmnxAccPlcyAASubAttributes):
    """Custom type tmnxLogApCrAASubAttributes based on TmnxAccPlcyAASubAttributes"""
    defaultBinValue = "0"


_TmnxLogApCrAASubAttributes_Type.__name__ = "TmnxAccPlcyAASubAttributes"
_TmnxLogApCrAASubAttributes_Object = MibTableColumn
tmnxLogApCrAASubAttributes = _TmnxLogApCrAASubAttributes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 20, 1, 11),
    _TmnxLogApCrAASubAttributes_Type()
)
tmnxLogApCrAASubAttributes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLogApCrAASubAttributes.setStatus("current")


class _TmnxLogApCrSignChangePolicer_Type(Integer32):
    """Custom type tmnxLogApCrSignChangePolicer based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 63),
    )


_TmnxLogApCrSignChangePolicer_Type.__name__ = "Integer32"
_TmnxLogApCrSignChangePolicer_Object = MibTableColumn
tmnxLogApCrSignChangePolicer = _TmnxLogApCrSignChangePolicer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 20, 1, 12),
    _TmnxLogApCrSignChangePolicer_Type()
)
tmnxLogApCrSignChangePolicer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLogApCrSignChangePolicer.setStatus("current")


class _TmnxLogApCrSignChangePICounters_Type(TmnxAccPlcyPolicerICounters):
    """Custom type tmnxLogApCrSignChangePICounters based on TmnxAccPlcyPolicerICounters"""
    defaultBinValue = "0"


_TmnxLogApCrSignChangePICounters_Type.__name__ = "TmnxAccPlcyPolicerICounters"
_TmnxLogApCrSignChangePICounters_Object = MibTableColumn
tmnxLogApCrSignChangePICounters = _TmnxLogApCrSignChangePICounters_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 20, 1, 13),
    _TmnxLogApCrSignChangePICounters_Type()
)
tmnxLogApCrSignChangePICounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLogApCrSignChangePICounters.setStatus("current")


class _TmnxLogApCrSignChangePECounters_Type(TmnxAccPlcyPolicerECounters):
    """Custom type tmnxLogApCrSignChangePECounters based on TmnxAccPlcyPolicerECounters"""
    defaultBinValue = "0"


_TmnxLogApCrSignChangePECounters_Type.__name__ = "TmnxAccPlcyPolicerECounters"
_TmnxLogApCrSignChangePECounters_Object = MibTableColumn
tmnxLogApCrSignChangePECounters = _TmnxLogApCrSignChangePECounters_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 20, 1, 14),
    _TmnxLogApCrSignChangePECounters_Type()
)
tmnxLogApCrSignChangePECounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLogApCrSignChangePECounters.setStatus("current")
_TmnxLogApCustRecordQueueTable_Object = MibTable
tmnxLogApCustRecordQueueTable = _TmnxLogApCustRecordQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 21)
)
if mibBuilder.loadTexts:
    tmnxLogApCustRecordQueueTable.setStatus("current")
_TmnxLogApCustRecordQueueEntry_Object = MibTableRow
tmnxLogApCustRecordQueueEntry = _TmnxLogApCustRecordQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 21, 1)
)
tmnxLogApCustRecordQueueEntry.setIndexNames(
    (0, "TIMETRA-LOG-MIB", "tmnxLogApPolicyId"),
    (0, "TIMETRA-LOG-MIB", "tmnxLogApCrQueueId"),
)
if mibBuilder.loadTexts:
    tmnxLogApCustRecordQueueEntry.setStatus("current")


class _TmnxLogApCrQueueId_Type(TQueueId):
    """Custom type tmnxLogApCrQueueId based on TQueueId"""
    subtypeSpec = TQueueId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_TmnxLogApCrQueueId_Type.__name__ = "TQueueId"
_TmnxLogApCrQueueId_Object = MibTableColumn
tmnxLogApCrQueueId = _TmnxLogApCrQueueId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 21, 1, 1),
    _TmnxLogApCrQueueId_Type()
)
tmnxLogApCrQueueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxLogApCrQueueId.setStatus("current")
_TmnxLogApCrQueueRowStatus_Type = RowStatus
_TmnxLogApCrQueueRowStatus_Object = MibTableColumn
tmnxLogApCrQueueRowStatus = _TmnxLogApCrQueueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 21, 1, 2),
    _TmnxLogApCrQueueRowStatus_Type()
)
tmnxLogApCrQueueRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogApCrQueueRowStatus.setStatus("current")
_TmnxLogApCrQueueLastChanged_Type = TimeStamp
_TmnxLogApCrQueueLastChanged_Object = MibTableColumn
tmnxLogApCrQueueLastChanged = _TmnxLogApCrQueueLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 21, 1, 3),
    _TmnxLogApCrQueueLastChanged_Type()
)
tmnxLogApCrQueueLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogApCrQueueLastChanged.setStatus("current")


class _TmnxLogApCrQueueICounters_Type(TmnxAccPlcyQICounters):
    """Custom type tmnxLogApCrQueueICounters based on TmnxAccPlcyQICounters"""
    defaultBinValue = "0"


_TmnxLogApCrQueueICounters_Type.__name__ = "TmnxAccPlcyQICounters"
_TmnxLogApCrQueueICounters_Object = MibTableColumn
tmnxLogApCrQueueICounters = _TmnxLogApCrQueueICounters_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 21, 1, 4),
    _TmnxLogApCrQueueICounters_Type()
)
tmnxLogApCrQueueICounters.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogApCrQueueICounters.setStatus("current")


class _TmnxLogApCrQueueECounters_Type(TmnxAccPlcyQECounters):
    """Custom type tmnxLogApCrQueueECounters based on TmnxAccPlcyQECounters"""
    defaultBinValue = "0"


_TmnxLogApCrQueueECounters_Type.__name__ = "TmnxAccPlcyQECounters"
_TmnxLogApCrQueueECounters_Object = MibTableColumn
tmnxLogApCrQueueECounters = _TmnxLogApCrQueueECounters_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 21, 1, 5),
    _TmnxLogApCrQueueECounters_Type()
)
tmnxLogApCrQueueECounters.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogApCrQueueECounters.setStatus("current")
_TmnxLogApCrOverrideCntrTable_Object = MibTable
tmnxLogApCrOverrideCntrTable = _TmnxLogApCrOverrideCntrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 22)
)
if mibBuilder.loadTexts:
    tmnxLogApCrOverrideCntrTable.setStatus("obsolete")
_TmnxLogApCrOverrideCntrEntry_Object = MibTableRow
tmnxLogApCrOverrideCntrEntry = _TmnxLogApCrOverrideCntrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 22, 1)
)
tmnxLogApCrOverrideCntrEntry.setIndexNames(
    (0, "TIMETRA-LOG-MIB", "tmnxLogApPolicyId"),
    (0, "TIMETRA-LOG-MIB", "tmnxLogApCrOverrideCntrId"),
)
if mibBuilder.loadTexts:
    tmnxLogApCrOverrideCntrEntry.setStatus("obsolete")


class _TmnxLogApCrOverrideCntrId_Type(THsmdaCounterIdOrZero):
    """Custom type tmnxLogApCrOverrideCntrId based on THsmdaCounterIdOrZero"""
    subtypeSpec = THsmdaCounterIdOrZero.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TmnxLogApCrOverrideCntrId_Type.__name__ = "THsmdaCounterIdOrZero"
_TmnxLogApCrOverrideCntrId_Object = MibTableColumn
tmnxLogApCrOverrideCntrId = _TmnxLogApCrOverrideCntrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 22, 1, 1),
    _TmnxLogApCrOverrideCntrId_Type()
)
tmnxLogApCrOverrideCntrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxLogApCrOverrideCntrId.setStatus("current")
_TmnxLogApCrOverrideCntrRowStatus_Type = RowStatus
_TmnxLogApCrOverrideCntrRowStatus_Object = MibTableColumn
tmnxLogApCrOverrideCntrRowStatus = _TmnxLogApCrOverrideCntrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 22, 1, 2),
    _TmnxLogApCrOverrideCntrRowStatus_Type()
)
tmnxLogApCrOverrideCntrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogApCrOverrideCntrRowStatus.setStatus("obsolete")
_TmnxLogApCrOverrideCntrLastChngd_Type = TimeStamp
_TmnxLogApCrOverrideCntrLastChngd_Object = MibTableColumn
tmnxLogApCrOverrideCntrLastChngd = _TmnxLogApCrOverrideCntrLastChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 22, 1, 3),
    _TmnxLogApCrOverrideCntrLastChngd_Type()
)
tmnxLogApCrOverrideCntrLastChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogApCrOverrideCntrLastChngd.setStatus("obsolete")


class _TmnxLogApCrOverrideCntrICounters_Type(TmnxAccPlcyOICounters):
    """Custom type tmnxLogApCrOverrideCntrICounters based on TmnxAccPlcyOICounters"""
    defaultBinValue = "0"


_TmnxLogApCrOverrideCntrICounters_Type.__name__ = "TmnxAccPlcyOICounters"
_TmnxLogApCrOverrideCntrICounters_Object = MibTableColumn
tmnxLogApCrOverrideCntrICounters = _TmnxLogApCrOverrideCntrICounters_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 22, 1, 4),
    _TmnxLogApCrOverrideCntrICounters_Type()
)
tmnxLogApCrOverrideCntrICounters.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogApCrOverrideCntrICounters.setStatus("obsolete")


class _TmnxLogApCrOverrideCntrECounters_Type(TmnxAccPlcyOECounters):
    """Custom type tmnxLogApCrOverrideCntrECounters based on TmnxAccPlcyOECounters"""
    defaultBinValue = "0"


_TmnxLogApCrOverrideCntrECounters_Type.__name__ = "TmnxAccPlcyOECounters"
_TmnxLogApCrOverrideCntrECounters_Object = MibTableColumn
tmnxLogApCrOverrideCntrECounters = _TmnxLogApCrOverrideCntrECounters_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 22, 1, 5),
    _TmnxLogApCrOverrideCntrECounters_Type()
)
tmnxLogApCrOverrideCntrECounters.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogApCrOverrideCntrECounters.setStatus("obsolete")


class _TmnxEventPrimaryRoutePref_Type(Integer32):
    """Custom type tmnxEventPrimaryRoutePref based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inband", 1),
          ("outband", 2))
    )


_TmnxEventPrimaryRoutePref_Type.__name__ = "Integer32"
_TmnxEventPrimaryRoutePref_Object = MibScalar
tmnxEventPrimaryRoutePref = _TmnxEventPrimaryRoutePref_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 23),
    _TmnxEventPrimaryRoutePref_Type()
)
tmnxEventPrimaryRoutePref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxEventPrimaryRoutePref.setStatus("current")


class _TmnxEventSecondaryRoutePref_Type(Integer32):
    """Custom type tmnxEventSecondaryRoutePref based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inband", 1),
          ("outband", 2),
          ("none", 3))
    )


_TmnxEventSecondaryRoutePref_Type.__name__ = "Integer32"
_TmnxEventSecondaryRoutePref_Object = MibScalar
tmnxEventSecondaryRoutePref = _TmnxEventSecondaryRoutePref_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 24),
    _TmnxEventSecondaryRoutePref_Type()
)
tmnxEventSecondaryRoutePref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxEventSecondaryRoutePref.setStatus("current")


class _TmnxLogConfigEventsDamped_Type(TruthValue):
    """Custom type tmnxLogConfigEventsDamped based on TruthValue"""
    defaultValue = 1


_TmnxLogConfigEventsDamped_Type.__name__ = "TruthValue"
_TmnxLogConfigEventsDamped_Object = MibScalar
tmnxLogConfigEventsDamped = _TmnxLogConfigEventsDamped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 25),
    _TmnxLogConfigEventsDamped_Type()
)
tmnxLogConfigEventsDamped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLogConfigEventsDamped.setStatus("current")
_TmnxLogEventHistoryObjs_ObjectIdentity = ObjectIdentity
tmnxLogEventHistoryObjs = _TmnxLogEventHistoryObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 26)
)
_TmnxLogEventHistGeneralObjs_ObjectIdentity = ObjectIdentity
tmnxLogEventHistGeneralObjs = _TmnxLogEventHistGeneralObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 26, 1)
)
_TmnxLogExRbkOpTblLastChange_Type = TimeStamp
_TmnxLogExRbkOpTblLastChange_Object = MibScalar
tmnxLogExRbkOpTblLastChange = _TmnxLogExRbkOpTblLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 26, 1, 1),
    _TmnxLogExRbkOpTblLastChange_Type()
)
tmnxLogExRbkOpTblLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogExRbkOpTblLastChange.setStatus("current")


class _TmnxLogExRbkOpMaxEntries_Type(Unsigned32):
    """Custom type tmnxLogExRbkOpMaxEntries based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxLogExRbkOpMaxEntries_Type.__name__ = "Unsigned32"
_TmnxLogExRbkOpMaxEntries_Object = MibScalar
tmnxLogExRbkOpMaxEntries = _TmnxLogExRbkOpMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 26, 1, 2),
    _TmnxLogExRbkOpMaxEntries_Type()
)
tmnxLogExRbkOpMaxEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLogExRbkOpMaxEntries.setStatus("current")
_TmnxLogExecRollbackOpTable_Object = MibTable
tmnxLogExecRollbackOpTable = _TmnxLogExecRollbackOpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 26, 3)
)
if mibBuilder.loadTexts:
    tmnxLogExecRollbackOpTable.setStatus("current")
_TmnxLogExecRollbackOpEntry_Object = MibTableRow
tmnxLogExecRollbackOpEntry = _TmnxLogExecRollbackOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 26, 3, 1)
)
tmnxLogExecRollbackOpEntry.setIndexNames(
    (0, "TIMETRA-LOG-MIB", "tmnxLogExRbkOpIndex"),
)
if mibBuilder.loadTexts:
    tmnxLogExecRollbackOpEntry.setStatus("current")
_TmnxLogExRbkOpIndex_Type = Unsigned32
_TmnxLogExRbkOpIndex_Object = MibTableColumn
tmnxLogExRbkOpIndex = _TmnxLogExRbkOpIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 26, 3, 1, 1),
    _TmnxLogExRbkOpIndex_Type()
)
tmnxLogExRbkOpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxLogExRbkOpIndex.setStatus("current")
_TmnxLogExRbkOpLastChanged_Type = TimeStamp
_TmnxLogExRbkOpLastChanged_Object = MibTableColumn
tmnxLogExRbkOpLastChanged = _TmnxLogExRbkOpLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 26, 3, 1, 2),
    _TmnxLogExRbkOpLastChanged_Type()
)
tmnxLogExRbkOpLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogExRbkOpLastChanged.setStatus("current")
_TmnxLogExRbkOpType_Type = TmnxLogExRbkOperationType
_TmnxLogExRbkOpType_Object = MibTableColumn
tmnxLogExRbkOpType = _TmnxLogExRbkOpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 26, 3, 1, 3),
    _TmnxLogExRbkOpType_Type()
)
tmnxLogExRbkOpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogExRbkOpType.setStatus("current")


class _TmnxLogExRbkOpStatus_Type(Integer32):
    """Custom type tmnxLogExRbkOpStatus based on Integer32"""
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
        *(("unknown", 0),
          ("inProgress", 1),
          ("success", 2),
          ("failed", 3))
    )


_TmnxLogExRbkOpStatus_Type.__name__ = "Integer32"
_TmnxLogExRbkOpStatus_Object = MibTableColumn
tmnxLogExRbkOpStatus = _TmnxLogExRbkOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 26, 3, 1, 4),
    _TmnxLogExRbkOpStatus_Type()
)
tmnxLogExRbkOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogExRbkOpStatus.setStatus("current")
_TmnxLogExRbkOpBegin_Type = TimeStamp
_TmnxLogExRbkOpBegin_Object = MibTableColumn
tmnxLogExRbkOpBegin = _TmnxLogExRbkOpBegin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 26, 3, 1, 5),
    _TmnxLogExRbkOpBegin_Type()
)
tmnxLogExRbkOpBegin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogExRbkOpBegin.setStatus("current")
_TmnxLogExRbkOpEnd_Type = TimeStamp
_TmnxLogExRbkOpEnd_Object = MibTableColumn
tmnxLogExRbkOpEnd = _TmnxLogExRbkOpEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 26, 3, 1, 6),
    _TmnxLogExRbkOpEnd_Type()
)
tmnxLogExRbkOpEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogExRbkOpEnd.setStatus("current")
_TmnxLogExRbkOpFile_Type = DisplayString
_TmnxLogExRbkOpFile_Object = MibTableColumn
tmnxLogExRbkOpFile = _TmnxLogExRbkOpFile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 26, 3, 1, 7),
    _TmnxLogExRbkOpFile_Type()
)
tmnxLogExRbkOpFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogExRbkOpFile.setStatus("current")
_TmnxLogExRbkOpUser_Type = TNamedItemOrEmpty
_TmnxLogExRbkOpUser_Object = MibTableColumn
tmnxLogExRbkOpUser = _TmnxLogExRbkOpUser_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 26, 3, 1, 8),
    _TmnxLogExRbkOpUser_Type()
)
tmnxLogExRbkOpUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogExRbkOpUser.setStatus("current")
_TmnxLogExRbkOpNumEvents_Type = Unsigned32
_TmnxLogExRbkOpNumEvents_Object = MibTableColumn
tmnxLogExRbkOpNumEvents = _TmnxLogExRbkOpNumEvents_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 26, 3, 1, 9),
    _TmnxLogExRbkOpNumEvents_Type()
)
tmnxLogExRbkOpNumEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogExRbkOpNumEvents.setStatus("current")
_TmnxLogExecRollbackEventTable_Object = MibTable
tmnxLogExecRollbackEventTable = _TmnxLogExecRollbackEventTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 26, 4)
)
if mibBuilder.loadTexts:
    tmnxLogExecRollbackEventTable.setStatus("current")
_TmnxLogExecRollbackEventEntry_Object = MibTableRow
tmnxLogExecRollbackEventEntry = _TmnxLogExecRollbackEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 26, 4, 1)
)
tmnxLogExecRollbackEventEntry.setIndexNames(
    (0, "TIMETRA-LOG-MIB", "tmnxLogExRbkOpIndex"),
    (0, "TIMETRA-LOG-MIB", "tmnxLogExRbkEventIndex"),
)
if mibBuilder.loadTexts:
    tmnxLogExecRollbackEventEntry.setStatus("current")
_TmnxLogExRbkEventIndex_Type = Unsigned32
_TmnxLogExRbkEventIndex_Object = MibTableColumn
tmnxLogExRbkEventIndex = _TmnxLogExRbkEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 26, 4, 1, 1),
    _TmnxLogExRbkEventIndex_Type()
)
tmnxLogExRbkEventIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxLogExRbkEventIndex.setStatus("current")
_TmnxLogExRbkEventOID_Type = ObjectIdentifier
_TmnxLogExRbkEventOID_Object = MibTableColumn
tmnxLogExRbkEventOID = _TmnxLogExRbkEventOID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 26, 4, 1, 2),
    _TmnxLogExRbkEventOID_Type()
)
tmnxLogExRbkEventOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogExRbkEventOID.setStatus("current")
_TmnxLogExRbkNotifyObjects_ObjectIdentity = ObjectIdentity
tmnxLogExRbkNotifyObjects = _TmnxLogExRbkNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 26, 5)
)
_TmnxLogExecRollbackOpIndex_Type = Unsigned32
_TmnxLogExecRollbackOpIndex_Object = MibScalar
tmnxLogExecRollbackOpIndex = _TmnxLogExecRollbackOpIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 26, 5, 1),
    _TmnxLogExecRollbackOpIndex_Type()
)
tmnxLogExecRollbackOpIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxLogExecRollbackOpIndex.setStatus("current")
_TmnxLogExecRollbackOpType_Type = TmnxLogExRbkOperationType
_TmnxLogExecRollbackOpType_Object = MibScalar
tmnxLogExecRollbackOpType = _TmnxLogExecRollbackOpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 26, 5, 2),
    _TmnxLogExecRollbackOpType_Type()
)
tmnxLogExecRollbackOpType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxLogExecRollbackOpType.setStatus("current")


class _TmnxLogColdStartWaitTime_Type(Unsigned32):
    """Custom type tmnxLogColdStartWaitTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_TmnxLogColdStartWaitTime_Type.__name__ = "Unsigned32"
_TmnxLogColdStartWaitTime_Object = MibScalar
tmnxLogColdStartWaitTime = _TmnxLogColdStartWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 27),
    _TmnxLogColdStartWaitTime_Type()
)
tmnxLogColdStartWaitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLogColdStartWaitTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxLogColdStartWaitTime.setUnits("seconds")


class _TmnxLogRouteRecoveryWaitTime_Type(Unsigned32):
    """Custom type tmnxLogRouteRecoveryWaitTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxLogRouteRecoveryWaitTime_Type.__name__ = "Unsigned32"
_TmnxLogRouteRecoveryWaitTime_Object = MibScalar
tmnxLogRouteRecoveryWaitTime = _TmnxLogRouteRecoveryWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 28),
    _TmnxLogRouteRecoveryWaitTime_Type()
)
tmnxLogRouteRecoveryWaitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLogRouteRecoveryWaitTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxLogRouteRecoveryWaitTime.setUnits("seconds")
_TmnxEhsObjs_ObjectIdentity = ObjectIdentity
tmnxEhsObjs = _TmnxEhsObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29)
)
_TmnxEhsGeneralObjs_ObjectIdentity = ObjectIdentity
tmnxEhsGeneralObjs = _TmnxEhsGeneralObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 1)
)
_TmnxEhsHandlerTblLastChange_Type = TimeStamp
_TmnxEhsHandlerTblLastChange_Object = MibScalar
tmnxEhsHandlerTblLastChange = _TmnxEhsHandlerTblLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 1, 1),
    _TmnxEhsHandlerTblLastChange_Type()
)
tmnxEhsHandlerTblLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEhsHandlerTblLastChange.setStatus("current")


class _TmnxEhsHandlerMaxEntries_Type(Unsigned32):
    """Custom type tmnxEhsHandlerMaxEntries based on Unsigned32"""
    defaultValue = 1500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_TmnxEhsHandlerMaxEntries_Type.__name__ = "Unsigned32"
_TmnxEhsHandlerMaxEntries_Object = MibScalar
tmnxEhsHandlerMaxEntries = _TmnxEhsHandlerMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 1, 2),
    _TmnxEhsHandlerMaxEntries_Type()
)
tmnxEhsHandlerMaxEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxEhsHandlerMaxEntries.setStatus("current")
_TmnxEhsHEntryTblLastChange_Type = TimeStamp
_TmnxEhsHEntryTblLastChange_Object = MibScalar
tmnxEhsHEntryTblLastChange = _TmnxEhsHEntryTblLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 1, 3),
    _TmnxEhsHEntryTblLastChange_Type()
)
tmnxEhsHEntryTblLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEhsHEntryTblLastChange.setStatus("current")


class _TmnxEhsHEntryMaxEntries_Type(Unsigned32):
    """Custom type tmnxEhsHEntryMaxEntries based on Unsigned32"""
    defaultValue = 1500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_TmnxEhsHEntryMaxEntries_Type.__name__ = "Unsigned32"
_TmnxEhsHEntryMaxEntries_Object = MibScalar
tmnxEhsHEntryMaxEntries = _TmnxEhsHEntryMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 1, 4),
    _TmnxEhsHEntryMaxEntries_Type()
)
tmnxEhsHEntryMaxEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxEhsHEntryMaxEntries.setStatus("current")
_TmnxEhsTriggerTblLastChange_Type = TimeStamp
_TmnxEhsTriggerTblLastChange_Object = MibScalar
tmnxEhsTriggerTblLastChange = _TmnxEhsTriggerTblLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 1, 5),
    _TmnxEhsTriggerTblLastChange_Type()
)
tmnxEhsTriggerTblLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEhsTriggerTblLastChange.setStatus("current")


class _TmnxEhsTriggerMaxEntries_Type(Unsigned32):
    """Custom type tmnxEhsTriggerMaxEntries based on Unsigned32"""
    defaultValue = 1500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_TmnxEhsTriggerMaxEntries_Type.__name__ = "Unsigned32"
_TmnxEhsTriggerMaxEntries_Object = MibScalar
tmnxEhsTriggerMaxEntries = _TmnxEhsTriggerMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 1, 6),
    _TmnxEhsTriggerMaxEntries_Type()
)
tmnxEhsTriggerMaxEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxEhsTriggerMaxEntries.setStatus("current")
_TmnxEhsTEntryTblLastChange_Type = TimeStamp
_TmnxEhsTEntryTblLastChange_Object = MibScalar
tmnxEhsTEntryTblLastChange = _TmnxEhsTEntryTblLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 1, 7),
    _TmnxEhsTEntryTblLastChange_Type()
)
tmnxEhsTEntryTblLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEhsTEntryTblLastChange.setStatus("current")


class _TmnxEhsTEntryMaxEntries_Type(Unsigned32):
    """Custom type tmnxEhsTEntryMaxEntries based on Unsigned32"""
    defaultValue = 1500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_TmnxEhsTEntryMaxEntries_Type.__name__ = "Unsigned32"
_TmnxEhsTEntryMaxEntries_Object = MibScalar
tmnxEhsTEntryMaxEntries = _TmnxEhsTEntryMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 1, 8),
    _TmnxEhsTEntryMaxEntries_Type()
)
tmnxEhsTEntryMaxEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxEhsTEntryMaxEntries.setStatus("current")
_TmnxEhsHandlerTable_Object = MibTable
tmnxEhsHandlerTable = _TmnxEhsHandlerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 2)
)
if mibBuilder.loadTexts:
    tmnxEhsHandlerTable.setStatus("current")
_TmnxEhsHandlerEntry_Object = MibTableRow
tmnxEhsHandlerEntry = _TmnxEhsHandlerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 2, 1)
)
tmnxEhsHandlerEntry.setIndexNames(
    (0, "TIMETRA-LOG-MIB", "tmnxEhsHandlerName"),
)
if mibBuilder.loadTexts:
    tmnxEhsHandlerEntry.setStatus("current")
_TmnxEhsHandlerName_Type = TNamedItem
_TmnxEhsHandlerName_Object = MibTableColumn
tmnxEhsHandlerName = _TmnxEhsHandlerName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 2, 1, 1),
    _TmnxEhsHandlerName_Type()
)
tmnxEhsHandlerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxEhsHandlerName.setStatus("current")
_TmnxEhsHandlerRowStatus_Type = RowStatus
_TmnxEhsHandlerRowStatus_Object = MibTableColumn
tmnxEhsHandlerRowStatus = _TmnxEhsHandlerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 2, 1, 2),
    _TmnxEhsHandlerRowStatus_Type()
)
tmnxEhsHandlerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxEhsHandlerRowStatus.setStatus("current")


class _TmnxEhsHandlerDescription_Type(TItemDescription):
    """Custom type tmnxEhsHandlerDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxEhsHandlerDescription_Type.__name__ = "TItemDescription"
_TmnxEhsHandlerDescription_Object = MibTableColumn
tmnxEhsHandlerDescription = _TmnxEhsHandlerDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 2, 1, 3),
    _TmnxEhsHandlerDescription_Type()
)
tmnxEhsHandlerDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxEhsHandlerDescription.setStatus("current")
_TmnxEhsHandlerLastChange_Type = TimeStamp
_TmnxEhsHandlerLastChange_Object = MibTableColumn
tmnxEhsHandlerLastChange = _TmnxEhsHandlerLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 2, 1, 4),
    _TmnxEhsHandlerLastChange_Type()
)
tmnxEhsHandlerLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEhsHandlerLastChange.setStatus("current")


class _TmnxEhsHandlerAdminStatus_Type(TmnxAdminState):
    """Custom type tmnxEhsHandlerAdminStatus based on TmnxAdminState"""
    defaultValue = 3


_TmnxEhsHandlerAdminStatus_Type.__name__ = "TmnxAdminState"
_TmnxEhsHandlerAdminStatus_Object = MibTableColumn
tmnxEhsHandlerAdminStatus = _TmnxEhsHandlerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 2, 1, 5),
    _TmnxEhsHandlerAdminStatus_Type()
)
tmnxEhsHandlerAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxEhsHandlerAdminStatus.setStatus("current")
_TmnxEhsHandlerOperStatus_Type = TmnxOperState
_TmnxEhsHandlerOperStatus_Object = MibTableColumn
tmnxEhsHandlerOperStatus = _TmnxEhsHandlerOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 2, 1, 6),
    _TmnxEhsHandlerOperStatus_Type()
)
tmnxEhsHandlerOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEhsHandlerOperStatus.setStatus("current")
_TmnxEhsHandlerStatsTable_Object = MibTable
tmnxEhsHandlerStatsTable = _TmnxEhsHandlerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 3)
)
if mibBuilder.loadTexts:
    tmnxEhsHandlerStatsTable.setStatus("current")
_TmnxEhsHandlerStatsEntry_Object = MibTableRow
tmnxEhsHandlerStatsEntry = _TmnxEhsHandlerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxEhsHandlerStatsEntry.setStatus("current")
_TmnxEhsHandlerStatsSuccess_Type = Unsigned32
_TmnxEhsHandlerStatsSuccess_Object = MibTableColumn
tmnxEhsHandlerStatsSuccess = _TmnxEhsHandlerStatsSuccess_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 3, 1, 1),
    _TmnxEhsHandlerStatsSuccess_Type()
)
tmnxEhsHandlerStatsSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEhsHandlerStatsSuccess.setStatus("current")
_TmnxEhsHandlerStatsErrNoEntry_Type = Unsigned32
_TmnxEhsHandlerStatsErrNoEntry_Object = MibTableColumn
tmnxEhsHandlerStatsErrNoEntry = _TmnxEhsHandlerStatsErrNoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 3, 1, 2),
    _TmnxEhsHandlerStatsErrNoEntry_Type()
)
tmnxEhsHandlerStatsErrNoEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEhsHandlerStatsErrNoEntry.setStatus("current")
_TmnxEhsHandlerStatsErrAdmStatus_Type = Unsigned32
_TmnxEhsHandlerStatsErrAdmStatus_Object = MibTableColumn
tmnxEhsHandlerStatsErrAdmStatus = _TmnxEhsHandlerStatsErrAdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 3, 1, 3),
    _TmnxEhsHandlerStatsErrAdmStatus_Type()
)
tmnxEhsHandlerStatsErrAdmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEhsHandlerStatsErrAdmStatus.setStatus("current")
_TmnxEhsHEntryTable_Object = MibTable
tmnxEhsHEntryTable = _TmnxEhsHEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 4)
)
if mibBuilder.loadTexts:
    tmnxEhsHEntryTable.setStatus("current")
_TmnxEhsHEntryEntry_Object = MibTableRow
tmnxEhsHEntryEntry = _TmnxEhsHEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 4, 1)
)
tmnxEhsHEntryEntry.setIndexNames(
    (0, "TIMETRA-LOG-MIB", "tmnxEhsHandlerName"),
    (0, "TIMETRA-LOG-MIB", "tmnxEhsHEntryId"),
)
if mibBuilder.loadTexts:
    tmnxEhsHEntryEntry.setStatus("current")
_TmnxEhsHEntryId_Type = Unsigned32
_TmnxEhsHEntryId_Object = MibTableColumn
tmnxEhsHEntryId = _TmnxEhsHEntryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 4, 1, 1),
    _TmnxEhsHEntryId_Type()
)
tmnxEhsHEntryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxEhsHEntryId.setStatus("current")
_TmnxEhsHEntryRowStatus_Type = RowStatus
_TmnxEhsHEntryRowStatus_Object = MibTableColumn
tmnxEhsHEntryRowStatus = _TmnxEhsHEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 4, 1, 2),
    _TmnxEhsHEntryRowStatus_Type()
)
tmnxEhsHEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxEhsHEntryRowStatus.setStatus("current")


class _TmnxEhsHEntryDescription_Type(TItemDescription):
    """Custom type tmnxEhsHEntryDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxEhsHEntryDescription_Type.__name__ = "TItemDescription"
_TmnxEhsHEntryDescription_Object = MibTableColumn
tmnxEhsHEntryDescription = _TmnxEhsHEntryDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 4, 1, 3),
    _TmnxEhsHEntryDescription_Type()
)
tmnxEhsHEntryDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxEhsHEntryDescription.setStatus("current")
_TmnxEhsHEntryLastChange_Type = TimeStamp
_TmnxEhsHEntryLastChange_Object = MibTableColumn
tmnxEhsHEntryLastChange = _TmnxEhsHEntryLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 4, 1, 4),
    _TmnxEhsHEntryLastChange_Type()
)
tmnxEhsHEntryLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEhsHEntryLastChange.setStatus("current")


class _TmnxEhsHEntryAdminStatus_Type(TmnxAdminState):
    """Custom type tmnxEhsHEntryAdminStatus based on TmnxAdminState"""
    defaultValue = 2


_TmnxEhsHEntryAdminStatus_Type.__name__ = "TmnxAdminState"
_TmnxEhsHEntryAdminStatus_Object = MibTableColumn
tmnxEhsHEntryAdminStatus = _TmnxEhsHEntryAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 4, 1, 5),
    _TmnxEhsHEntryAdminStatus_Type()
)
tmnxEhsHEntryAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxEhsHEntryAdminStatus.setStatus("current")
_TmnxEhsHEntryOperStatus_Type = TmnxOperState
_TmnxEhsHEntryOperStatus_Object = MibTableColumn
tmnxEhsHEntryOperStatus = _TmnxEhsHEntryOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 4, 1, 6),
    _TmnxEhsHEntryOperStatus_Type()
)
tmnxEhsHEntryOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEhsHEntryOperStatus.setStatus("current")


class _TmnxEhsHEntryScriptPlcyName_Type(TNamedItemOrEmpty):
    """Custom type tmnxEhsHEntryScriptPlcyName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxEhsHEntryScriptPlcyName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxEhsHEntryScriptPlcyName_Object = MibTableColumn
tmnxEhsHEntryScriptPlcyName = _TmnxEhsHEntryScriptPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 4, 1, 7),
    _TmnxEhsHEntryScriptPlcyName_Type()
)
tmnxEhsHEntryScriptPlcyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxEhsHEntryScriptPlcyName.setStatus("current")


class _TmnxEhsHEntryScriptPlcyOwner_Type(TNamedItemOrEmpty):
    """Custom type tmnxEhsHEntryScriptPlcyOwner based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxEhsHEntryScriptPlcyOwner_Type.__name__ = "TNamedItemOrEmpty"
_TmnxEhsHEntryScriptPlcyOwner_Object = MibTableColumn
tmnxEhsHEntryScriptPlcyOwner = _TmnxEhsHEntryScriptPlcyOwner_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 4, 1, 8),
    _TmnxEhsHEntryScriptPlcyOwner_Type()
)
tmnxEhsHEntryScriptPlcyOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxEhsHEntryScriptPlcyOwner.setStatus("current")


class _TmnxEhsHEntryMinDelay_Type(Unsigned32):
    """Custom type tmnxEhsHEntryMinDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800),
    )


_TmnxEhsHEntryMinDelay_Type.__name__ = "Unsigned32"
_TmnxEhsHEntryMinDelay_Object = MibTableColumn
tmnxEhsHEntryMinDelay = _TmnxEhsHEntryMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 4, 1, 9),
    _TmnxEhsHEntryMinDelay_Type()
)
tmnxEhsHEntryMinDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxEhsHEntryMinDelay.setStatus("current")
if mibBuilder.loadTexts:
    tmnxEhsHEntryMinDelay.setUnits("seconds")
_TmnxEhsHEntryLastExecuted_Type = TimeStamp
_TmnxEhsHEntryLastExecuted_Object = MibTableColumn
tmnxEhsHEntryLastExecuted = _TmnxEhsHEntryLastExecuted_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 4, 1, 10),
    _TmnxEhsHEntryLastExecuted_Type()
)
tmnxEhsHEntryLastExecuted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEhsHEntryLastExecuted.setStatus("current")
_TmnxEhsHEntryStatsTable_Object = MibTable
tmnxEhsHEntryStatsTable = _TmnxEhsHEntryStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 5)
)
if mibBuilder.loadTexts:
    tmnxEhsHEntryStatsTable.setStatus("current")
_TmnxEhsHEntryStatsEntry_Object = MibTableRow
tmnxEhsHEntryStatsEntry = _TmnxEhsHEntryStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 5, 1)
)
if mibBuilder.loadTexts:
    tmnxEhsHEntryStatsEntry.setStatus("current")
_TmnxEhsHEntryStatsLaunchSuccess_Type = Unsigned32
_TmnxEhsHEntryStatsLaunchSuccess_Object = MibTableColumn
tmnxEhsHEntryStatsLaunchSuccess = _TmnxEhsHEntryStatsLaunchSuccess_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 5, 1, 1),
    _TmnxEhsHEntryStatsLaunchSuccess_Type()
)
tmnxEhsHEntryStatsLaunchSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEhsHEntryStatsLaunchSuccess.setStatus("current")
_TmnxEhsHEntryStatsErrMinDelay_Type = Unsigned32
_TmnxEhsHEntryStatsErrMinDelay_Object = MibTableColumn
tmnxEhsHEntryStatsErrMinDelay = _TmnxEhsHEntryStatsErrMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 5, 1, 2),
    _TmnxEhsHEntryStatsErrMinDelay_Type()
)
tmnxEhsHEntryStatsErrMinDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEhsHEntryStatsErrMinDelay.setStatus("current")
_TmnxEhsHEntryStatsErrLaunch_Type = Unsigned32
_TmnxEhsHEntryStatsErrLaunch_Object = MibTableColumn
tmnxEhsHEntryStatsErrLaunch = _TmnxEhsHEntryStatsErrLaunch_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 5, 1, 3),
    _TmnxEhsHEntryStatsErrLaunch_Type()
)
tmnxEhsHEntryStatsErrLaunch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEhsHEntryStatsErrLaunch.setStatus("current")
_TmnxEhsHEntryStatsErrAdmStatus_Type = Unsigned32
_TmnxEhsHEntryStatsErrAdmStatus_Object = MibTableColumn
tmnxEhsHEntryStatsErrAdmStatus = _TmnxEhsHEntryStatsErrAdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 5, 1, 4),
    _TmnxEhsHEntryStatsErrAdmStatus_Type()
)
tmnxEhsHEntryStatsErrAdmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEhsHEntryStatsErrAdmStatus.setStatus("current")
_TmnxEhsTriggerTable_Object = MibTable
tmnxEhsTriggerTable = _TmnxEhsTriggerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 6)
)
if mibBuilder.loadTexts:
    tmnxEhsTriggerTable.setStatus("current")
_TmnxEhsTriggerEntry_Object = MibTableRow
tmnxEhsTriggerEntry = _TmnxEhsTriggerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 6, 1)
)
tmnxEhsTriggerEntry.setIndexNames(
    (0, "TIMETRA-LOG-MIB", "tmnxEventAppIndex"),
    (0, "TIMETRA-LOG-MIB", "tmnxEventID"),
)
if mibBuilder.loadTexts:
    tmnxEhsTriggerEntry.setStatus("current")
_TmnxEhsTriggerRowStatus_Type = RowStatus
_TmnxEhsTriggerRowStatus_Object = MibTableColumn
tmnxEhsTriggerRowStatus = _TmnxEhsTriggerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 6, 1, 1),
    _TmnxEhsTriggerRowStatus_Type()
)
tmnxEhsTriggerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxEhsTriggerRowStatus.setStatus("current")


class _TmnxEhsTriggerDescription_Type(TItemDescription):
    """Custom type tmnxEhsTriggerDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxEhsTriggerDescription_Type.__name__ = "TItemDescription"
_TmnxEhsTriggerDescription_Object = MibTableColumn
tmnxEhsTriggerDescription = _TmnxEhsTriggerDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 6, 1, 2),
    _TmnxEhsTriggerDescription_Type()
)
tmnxEhsTriggerDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxEhsTriggerDescription.setStatus("current")
_TmnxEhsTriggerLastChange_Type = TimeStamp
_TmnxEhsTriggerLastChange_Object = MibTableColumn
tmnxEhsTriggerLastChange = _TmnxEhsTriggerLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 6, 1, 3),
    _TmnxEhsTriggerLastChange_Type()
)
tmnxEhsTriggerLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEhsTriggerLastChange.setStatus("current")


class _TmnxEhsTriggerAdminStatus_Type(TmnxAdminState):
    """Custom type tmnxEhsTriggerAdminStatus based on TmnxAdminState"""
    defaultValue = 3


_TmnxEhsTriggerAdminStatus_Type.__name__ = "TmnxAdminState"
_TmnxEhsTriggerAdminStatus_Object = MibTableColumn
tmnxEhsTriggerAdminStatus = _TmnxEhsTriggerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 6, 1, 4),
    _TmnxEhsTriggerAdminStatus_Type()
)
tmnxEhsTriggerAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxEhsTriggerAdminStatus.setStatus("current")
_TmnxEhsTriggerOperStatus_Type = TmnxOperState
_TmnxEhsTriggerOperStatus_Object = MibTableColumn
tmnxEhsTriggerOperStatus = _TmnxEhsTriggerOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 6, 1, 5),
    _TmnxEhsTriggerOperStatus_Type()
)
tmnxEhsTriggerOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEhsTriggerOperStatus.setStatus("current")
_TmnxEhsTriggerStatsTable_Object = MibTable
tmnxEhsTriggerStatsTable = _TmnxEhsTriggerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 7)
)
if mibBuilder.loadTexts:
    tmnxEhsTriggerStatsTable.setStatus("current")
_TmnxEhsTriggerStatsEntry_Object = MibTableRow
tmnxEhsTriggerStatsEntry = _TmnxEhsTriggerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 7, 1)
)
if mibBuilder.loadTexts:
    tmnxEhsTriggerStatsEntry.setStatus("current")
_TmnxEhsTriggerStatsSuccess_Type = Unsigned32
_TmnxEhsTriggerStatsSuccess_Object = MibTableColumn
tmnxEhsTriggerStatsSuccess = _TmnxEhsTriggerStatsSuccess_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 7, 1, 1),
    _TmnxEhsTriggerStatsSuccess_Type()
)
tmnxEhsTriggerStatsSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEhsTriggerStatsSuccess.setStatus("current")
_TmnxEhsTriggerStatsErrNoEntry_Type = Unsigned32
_TmnxEhsTriggerStatsErrNoEntry_Object = MibTableColumn
tmnxEhsTriggerStatsErrNoEntry = _TmnxEhsTriggerStatsErrNoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 7, 1, 2),
    _TmnxEhsTriggerStatsErrNoEntry_Type()
)
tmnxEhsTriggerStatsErrNoEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEhsTriggerStatsErrNoEntry.setStatus("current")
_TmnxEhsTriggerStatsErrAdmStatus_Type = Unsigned32
_TmnxEhsTriggerStatsErrAdmStatus_Object = MibTableColumn
tmnxEhsTriggerStatsErrAdmStatus = _TmnxEhsTriggerStatsErrAdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 7, 1, 3),
    _TmnxEhsTriggerStatsErrAdmStatus_Type()
)
tmnxEhsTriggerStatsErrAdmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEhsTriggerStatsErrAdmStatus.setStatus("current")
_TmnxEhsTEntryTable_Object = MibTable
tmnxEhsTEntryTable = _TmnxEhsTEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 8)
)
if mibBuilder.loadTexts:
    tmnxEhsTEntryTable.setStatus("current")
_TmnxEhsTEntryEntry_Object = MibTableRow
tmnxEhsTEntryEntry = _TmnxEhsTEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 8, 1)
)
tmnxEhsTEntryEntry.setIndexNames(
    (0, "TIMETRA-LOG-MIB", "tmnxEventAppIndex"),
    (0, "TIMETRA-LOG-MIB", "tmnxEventID"),
    (0, "TIMETRA-LOG-MIB", "tmnxEhsTEntryId"),
)
if mibBuilder.loadTexts:
    tmnxEhsTEntryEntry.setStatus("current")
_TmnxEhsTEntryId_Type = Unsigned32
_TmnxEhsTEntryId_Object = MibTableColumn
tmnxEhsTEntryId = _TmnxEhsTEntryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 8, 1, 1),
    _TmnxEhsTEntryId_Type()
)
tmnxEhsTEntryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxEhsTEntryId.setStatus("current")
_TmnxEhsTEntryRowStatus_Type = RowStatus
_TmnxEhsTEntryRowStatus_Object = MibTableColumn
tmnxEhsTEntryRowStatus = _TmnxEhsTEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 8, 1, 2),
    _TmnxEhsTEntryRowStatus_Type()
)
tmnxEhsTEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxEhsTEntryRowStatus.setStatus("current")


class _TmnxEhsTEntryDescription_Type(TItemDescription):
    """Custom type tmnxEhsTEntryDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxEhsTEntryDescription_Type.__name__ = "TItemDescription"
_TmnxEhsTEntryDescription_Object = MibTableColumn
tmnxEhsTEntryDescription = _TmnxEhsTEntryDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 8, 1, 3),
    _TmnxEhsTEntryDescription_Type()
)
tmnxEhsTEntryDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxEhsTEntryDescription.setStatus("current")
_TmnxEhsTEntryLastChange_Type = TimeStamp
_TmnxEhsTEntryLastChange_Object = MibTableColumn
tmnxEhsTEntryLastChange = _TmnxEhsTEntryLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 8, 1, 4),
    _TmnxEhsTEntryLastChange_Type()
)
tmnxEhsTEntryLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEhsTEntryLastChange.setStatus("current")


class _TmnxEhsTEntryAdminStatus_Type(TmnxAdminState):
    """Custom type tmnxEhsTEntryAdminStatus based on TmnxAdminState"""
    defaultValue = 2


_TmnxEhsTEntryAdminStatus_Type.__name__ = "TmnxAdminState"
_TmnxEhsTEntryAdminStatus_Object = MibTableColumn
tmnxEhsTEntryAdminStatus = _TmnxEhsTEntryAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 8, 1, 5),
    _TmnxEhsTEntryAdminStatus_Type()
)
tmnxEhsTEntryAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxEhsTEntryAdminStatus.setStatus("current")
_TmnxEhsTEntryOperStatus_Type = TmnxOperState
_TmnxEhsTEntryOperStatus_Object = MibTableColumn
tmnxEhsTEntryOperStatus = _TmnxEhsTEntryOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 8, 1, 6),
    _TmnxEhsTEntryOperStatus_Type()
)
tmnxEhsTEntryOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEhsTEntryOperStatus.setStatus("current")


class _TmnxEhsTEntryLogFilterId_Type(TmnxLogFilterId):
    """Custom type tmnxEhsTEntryLogFilterId based on TmnxLogFilterId"""
    defaultValue = 0


_TmnxEhsTEntryLogFilterId_Type.__name__ = "TmnxLogFilterId"
_TmnxEhsTEntryLogFilterId_Object = MibTableColumn
tmnxEhsTEntryLogFilterId = _TmnxEhsTEntryLogFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 8, 1, 7),
    _TmnxEhsTEntryLogFilterId_Type()
)
tmnxEhsTEntryLogFilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxEhsTEntryLogFilterId.setStatus("current")


class _TmnxEhsTEntryHandlerName_Type(TNamedItemOrEmpty):
    """Custom type tmnxEhsTEntryHandlerName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxEhsTEntryHandlerName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxEhsTEntryHandlerName_Object = MibTableColumn
tmnxEhsTEntryHandlerName = _TmnxEhsTEntryHandlerName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 8, 1, 8),
    _TmnxEhsTEntryHandlerName_Type()
)
tmnxEhsTEntryHandlerName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxEhsTEntryHandlerName.setStatus("current")


class _TmnxEhsTEntryDebounceVal_Type(Unsigned32):
    """Custom type tmnxEhsTEntryDebounceVal based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 15),
    )


_TmnxEhsTEntryDebounceVal_Type.__name__ = "Unsigned32"
_TmnxEhsTEntryDebounceVal_Object = MibTableColumn
tmnxEhsTEntryDebounceVal = _TmnxEhsTEntryDebounceVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 8, 1, 9),
    _TmnxEhsTEntryDebounceVal_Type()
)
tmnxEhsTEntryDebounceVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxEhsTEntryDebounceVal.setStatus("current")


class _TmnxEhsTEntryDebounceTime_Type(Unsigned32):
    """Custom type tmnxEhsTEntryDebounceTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800),
    )


_TmnxEhsTEntryDebounceTime_Type.__name__ = "Unsigned32"
_TmnxEhsTEntryDebounceTime_Object = MibTableColumn
tmnxEhsTEntryDebounceTime = _TmnxEhsTEntryDebounceTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 8, 1, 10),
    _TmnxEhsTEntryDebounceTime_Type()
)
tmnxEhsTEntryDebounceTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxEhsTEntryDebounceTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxEhsTEntryDebounceTime.setUnits("seconds")
_TmnxEhsTEntryStatsTable_Object = MibTable
tmnxEhsTEntryStatsTable = _TmnxEhsTEntryStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 9)
)
if mibBuilder.loadTexts:
    tmnxEhsTEntryStatsTable.setStatus("current")
_TmnxEhsTEntryStatsEntry_Object = MibTableRow
tmnxEhsTEntryStatsEntry = _TmnxEhsTEntryStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 9, 1)
)
if mibBuilder.loadTexts:
    tmnxEhsTEntryStatsEntry.setStatus("current")
_TmnxEhsTEntryStatsFilterMatch_Type = Unsigned32
_TmnxEhsTEntryStatsFilterMatch_Object = MibTableColumn
tmnxEhsTEntryStatsFilterMatch = _TmnxEhsTEntryStatsFilterMatch_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 9, 1, 1),
    _TmnxEhsTEntryStatsFilterMatch_Type()
)
tmnxEhsTEntryStatsFilterMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEhsTEntryStatsFilterMatch.setStatus("current")
_TmnxEhsTEntryStatsFilterFail_Type = Unsigned32
_TmnxEhsTEntryStatsFilterFail_Object = MibTableColumn
tmnxEhsTEntryStatsFilterFail = _TmnxEhsTEntryStatsFilterFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 9, 1, 2),
    _TmnxEhsTEntryStatsFilterFail_Type()
)
tmnxEhsTEntryStatsFilterFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEhsTEntryStatsFilterFail.setStatus("current")
_TmnxEhsTEntryStatsErrAdminStatus_Type = Unsigned32
_TmnxEhsTEntryStatsErrAdminStatus_Object = MibTableColumn
tmnxEhsTEntryStatsErrAdminStatus = _TmnxEhsTEntryStatsErrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 9, 1, 3),
    _TmnxEhsTEntryStatsErrAdminStatus_Type()
)
tmnxEhsTEntryStatsErrAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEhsTEntryStatsErrAdminStatus.setStatus("current")
_TmnxEhsTEntryStatsErrFilter_Type = Unsigned32
_TmnxEhsTEntryStatsErrFilter_Object = MibTableColumn
tmnxEhsTEntryStatsErrFilter = _TmnxEhsTEntryStatsErrFilter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 9, 1, 4),
    _TmnxEhsTEntryStatsErrFilter_Type()
)
tmnxEhsTEntryStatsErrFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEhsTEntryStatsErrFilter.setStatus("current")
_TmnxEhsTEntryStatsErrHandler_Type = Unsigned32
_TmnxEhsTEntryStatsErrHandler_Object = MibTableColumn
tmnxEhsTEntryStatsErrHandler = _TmnxEhsTEntryStatsErrHandler_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 9, 1, 5),
    _TmnxEhsTEntryStatsErrHandler_Type()
)
tmnxEhsTEntryStatsErrHandler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEhsTEntryStatsErrHandler.setStatus("current")
_TmnxEhsTEntryStatsTriggerCount_Type = Unsigned32
_TmnxEhsTEntryStatsTriggerCount_Object = MibTableColumn
tmnxEhsTEntryStatsTriggerCount = _TmnxEhsTEntryStatsTriggerCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 9, 1, 6),
    _TmnxEhsTEntryStatsTriggerCount_Type()
)
tmnxEhsTEntryStatsTriggerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEhsTEntryStatsTriggerCount.setStatus("current")
_TmnxEhsTEntryStatsDebounce_Type = Unsigned32
_TmnxEhsTEntryStatsDebounce_Object = MibTableColumn
tmnxEhsTEntryStatsDebounce = _TmnxEhsTEntryStatsDebounce_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 29, 9, 1, 7),
    _TmnxEhsTEntryStatsDebounce_Type()
)
tmnxEhsTEntryStatsDebounce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxEhsTEntryStatsDebounce.setStatus("current")
_TmnxLogCliSubscrTable_Object = MibTable
tmnxLogCliSubscrTable = _TmnxLogCliSubscrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 30)
)
if mibBuilder.loadTexts:
    tmnxLogCliSubscrTable.setStatus("current")
_TmnxLogCliSubscrEntry_Object = MibTableRow
tmnxLogCliSubscrEntry = _TmnxLogCliSubscrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 30, 1)
)
tmnxLogCliSubscrEntry.setIndexNames(
    (0, "TIMETRA-LOG-MIB", "tmnxLogCliSubscrSession"),
    (0, "TIMETRA-LOG-MIB", "tmnxLogCliSubscrLog"),
)
if mibBuilder.loadTexts:
    tmnxLogCliSubscrEntry.setStatus("current")
_TmnxLogCliSubscrSession_Type = Unsigned32
_TmnxLogCliSubscrSession_Object = MibTableColumn
tmnxLogCliSubscrSession = _TmnxLogCliSubscrSession_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 30, 1, 1),
    _TmnxLogCliSubscrSession_Type()
)
tmnxLogCliSubscrSession.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxLogCliSubscrSession.setStatus("current")
_TmnxLogCliSubscrLog_Type = TmnxLogIdIndex
_TmnxLogCliSubscrLog_Object = MibTableColumn
tmnxLogCliSubscrLog = _TmnxLogCliSubscrLog_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 30, 1, 2),
    _TmnxLogCliSubscrLog_Type()
)
tmnxLogCliSubscrLog.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxLogCliSubscrLog.setStatus("current")


class _TmnxLogCliSubscrType_Type(Integer32):
    """Custom type tmnxLogCliSubscrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("telnet", 1),
          ("console", 2),
          ("ssh", 4))
    )


_TmnxLogCliSubscrType_Type.__name__ = "Integer32"
_TmnxLogCliSubscrType_Object = MibTableColumn
tmnxLogCliSubscrType = _TmnxLogCliSubscrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 30, 1, 3),
    _TmnxLogCliSubscrType_Type()
)
tmnxLogCliSubscrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogCliSubscrType.setStatus("current")
_TmnxLogCliSubscrUser_Type = TNamedItem
_TmnxLogCliSubscrUser_Object = MibTableColumn
tmnxLogCliSubscrUser = _TmnxLogCliSubscrUser_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 30, 1, 4),
    _TmnxLogCliSubscrUser_Type()
)
tmnxLogCliSubscrUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogCliSubscrUser.setStatus("current")


class _TmnxLogCliSubscrUserLoginTime_Type(DateAndTime):
    """Custom type tmnxLogCliSubscrUserLoginTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )
    fixed_length = 11


_TmnxLogCliSubscrUserLoginTime_Type.__name__ = "DateAndTime"
_TmnxLogCliSubscrUserLoginTime_Object = MibTableColumn
tmnxLogCliSubscrUserLoginTime = _TmnxLogCliSubscrUserLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 30, 1, 5),
    _TmnxLogCliSubscrUserLoginTime_Type()
)
tmnxLogCliSubscrUserLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogCliSubscrUserLoginTime.setStatus("current")
_TmnxLogCliSubscrUserIpAddrType_Type = InetAddressType
_TmnxLogCliSubscrUserIpAddrType_Object = MibTableColumn
tmnxLogCliSubscrUserIpAddrType = _TmnxLogCliSubscrUserIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 30, 1, 6),
    _TmnxLogCliSubscrUserIpAddrType_Type()
)
tmnxLogCliSubscrUserIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogCliSubscrUserIpAddrType.setStatus("current")


class _TmnxLogCliSubscrUserIpAddr_Type(InetAddress):
    """Custom type tmnxLogCliSubscrUserIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxLogCliSubscrUserIpAddr_Type.__name__ = "InetAddress"
_TmnxLogCliSubscrUserIpAddr_Object = MibTableColumn
tmnxLogCliSubscrUserIpAddr = _TmnxLogCliSubscrUserIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 30, 1, 7),
    _TmnxLogCliSubscrUserIpAddr_Type()
)
tmnxLogCliSubscrUserIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogCliSubscrUserIpAddr.setStatus("current")
_TmnxLogApCustRecordPolicerTable_Object = MibTable
tmnxLogApCustRecordPolicerTable = _TmnxLogApCustRecordPolicerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 31)
)
if mibBuilder.loadTexts:
    tmnxLogApCustRecordPolicerTable.setStatus("current")
_TmnxLogApCustRecordPolicerEntry_Object = MibTableRow
tmnxLogApCustRecordPolicerEntry = _TmnxLogApCustRecordPolicerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 31, 1)
)
tmnxLogApCustRecordPolicerEntry.setIndexNames(
    (0, "TIMETRA-LOG-MIB", "tmnxLogApPolicyId"),
    (0, "TIMETRA-LOG-MIB", "tmnxLogApCrPolicerId"),
)
if mibBuilder.loadTexts:
    tmnxLogApCustRecordPolicerEntry.setStatus("current")


class _TmnxLogApCrPolicerId_Type(Unsigned32):
    """Custom type tmnxLogApCrPolicerId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_TmnxLogApCrPolicerId_Type.__name__ = "Unsigned32"
_TmnxLogApCrPolicerId_Object = MibTableColumn
tmnxLogApCrPolicerId = _TmnxLogApCrPolicerId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 31, 1, 1),
    _TmnxLogApCrPolicerId_Type()
)
tmnxLogApCrPolicerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxLogApCrPolicerId.setStatus("current")
_TmnxLogApCrPolicerLastChanged_Type = TimeStamp
_TmnxLogApCrPolicerLastChanged_Object = MibTableColumn
tmnxLogApCrPolicerLastChanged = _TmnxLogApCrPolicerLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 31, 1, 2),
    _TmnxLogApCrPolicerLastChanged_Type()
)
tmnxLogApCrPolicerLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogApCrPolicerLastChanged.setStatus("current")
_TmnxLogApCrPolicerRowStatus_Type = RowStatus
_TmnxLogApCrPolicerRowStatus_Object = MibTableColumn
tmnxLogApCrPolicerRowStatus = _TmnxLogApCrPolicerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 31, 1, 3),
    _TmnxLogApCrPolicerRowStatus_Type()
)
tmnxLogApCrPolicerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogApCrPolicerRowStatus.setStatus("current")


class _TmnxLogApCrPolicerICounters_Type(TmnxAccPlcyPolicerICounters):
    """Custom type tmnxLogApCrPolicerICounters based on TmnxAccPlcyPolicerICounters"""
    defaultBinValue = "0"


_TmnxLogApCrPolicerICounters_Type.__name__ = "TmnxAccPlcyPolicerICounters"
_TmnxLogApCrPolicerICounters_Object = MibTableColumn
tmnxLogApCrPolicerICounters = _TmnxLogApCrPolicerICounters_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 31, 1, 4),
    _TmnxLogApCrPolicerICounters_Type()
)
tmnxLogApCrPolicerICounters.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogApCrPolicerICounters.setStatus("current")


class _TmnxLogApCrPolicerECounters_Type(TmnxAccPlcyPolicerECounters):
    """Custom type tmnxLogApCrPolicerECounters based on TmnxAccPlcyPolicerECounters"""
    defaultBinValue = "0"


_TmnxLogApCrPolicerECounters_Type.__name__ = "TmnxAccPlcyPolicerECounters"
_TmnxLogApCrPolicerECounters_Object = MibTableColumn
tmnxLogApCrPolicerECounters = _TmnxLogApCrPolicerECounters_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 12, 31, 1, 5),
    _TmnxLogApCrPolicerECounters_Type()
)
tmnxLogApCrPolicerECounters.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogApCrPolicerECounters.setStatus("current")
_TmnxLogNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxLogNotifyPrefix = _TmnxLogNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 12)
)
_TmnxLogNotifications_ObjectIdentity = ObjectIdentity
tmnxLogNotifications = _TmnxLogNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 12, 0)
)
snmpNotifyEntry.registerAugmentions(
    ("TIMETRA-LOG-MIB",
     "tmnxSnmpTrapLogEntry")
)
tmnxSnmpTrapLogEntry.setIndexNames(*snmpNotifyEntry.getIndexNames())
tmnxLogApEntry.registerAugmentions(
    ("TIMETRA-LOG-MIB",
     "tmnxLogApCustRecordEntry")
)
tmnxLogApCustRecordEntry.setIndexNames(*tmnxLogApEntry.getIndexNames())
tmnxEhsHandlerEntry.registerAugmentions(
    ("TIMETRA-LOG-MIB",
     "tmnxEhsHandlerStatsEntry")
)
tmnxEhsHandlerStatsEntry.setIndexNames(*tmnxEhsHandlerEntry.getIndexNames())
tmnxEhsHEntryEntry.registerAugmentions(
    ("TIMETRA-LOG-MIB",
     "tmnxEhsHEntryStatsEntry")
)
tmnxEhsHEntryStatsEntry.setIndexNames(*tmnxEhsHEntryEntry.getIndexNames())
tmnxEhsTriggerEntry.registerAugmentions(
    ("TIMETRA-LOG-MIB",
     "tmnxEhsTriggerStatsEntry")
)
tmnxEhsTriggerStatsEntry.setIndexNames(*tmnxEhsTriggerEntry.getIndexNames())
tmnxEhsTEntryEntry.registerAugmentions(
    ("TIMETRA-LOG-MIB",
     "tmnxEhsTEntryStatsEntry")
)
tmnxEhsTEntryStatsEntry.setIndexNames(*tmnxEhsTEntryEntry.getIndexNames())

# Managed Objects groups

tmnxLogGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 1)
)
tmnxLogGlobalGroup.setObjects(
    ("TIMETRA-LOG-MIB", "tmnxLogMaxLogs")
)
if mibBuilder.loadTexts:
    tmnxLogGlobalGroup.setStatus("current")

tmnxLogAccountingPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 3)
)
tmnxLogAccountingPolicyGroup.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogApRowStatus"),
        ("TIMETRA-LOG-MIB", "tmnxLogApStorageType"),
        ("TIMETRA-LOG-MIB", "tmnxLogApAdminStatus"),
        ("TIMETRA-LOG-MIB", "tmnxLogApOperStatus"),
        ("TIMETRA-LOG-MIB", "tmnxLogApInterval"),
        ("TIMETRA-LOG-MIB", "tmnxLogApDescription"),
        ("TIMETRA-LOG-MIB", "tmnxLogApDefault"),
        ("TIMETRA-LOG-MIB", "tmnxLogApRecord"),
        ("TIMETRA-LOG-MIB", "tmnxLogApToFileId"),
        ("TIMETRA-LOG-MIB", "tmnxLogApPortType"),
        ("TIMETRA-LOG-MIB", "tmnxLogApAlign"))
)
if mibBuilder.loadTexts:
    tmnxLogAccountingPolicyGroup.setStatus("current")

tmnxLogFileIdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 4)
)
tmnxLogFileIdGroup.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogFileIdRowStatus"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdStorageType"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdRolloverTime"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdRetainTime"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdAdminLocation"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdOperLocation"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdDescription"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdLogType"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdLogId"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdPathName"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdCreateTime"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdBackupLoc"))
)
if mibBuilder.loadTexts:
    tmnxLogFileIdGroup.setStatus("current")

tmnxLogSyslogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 5)
)
tmnxLogSyslogGroup.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxSyslogTargetRowStatus"),
        ("TIMETRA-LOG-MIB", "tmnxSyslogTargetDescription"),
        ("TIMETRA-LOG-MIB", "tmnxSyslogTargetAddress"),
        ("TIMETRA-LOG-MIB", "tmnxSyslogTargetUdpPort"),
        ("TIMETRA-LOG-MIB", "tmnxSyslogTargetFacility"),
        ("TIMETRA-LOG-MIB", "tmnxSyslogTargetSeverity"),
        ("TIMETRA-LOG-MIB", "tmnxSyslogTargetMessagePrefix"),
        ("TIMETRA-LOG-MIB", "tmnxSyslogTargetMessagesDropped"))
)
if mibBuilder.loadTexts:
    tmnxLogSyslogGroup.setStatus("obsolete")

tmnxSnmpTrapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 6)
)
tmnxSnmpTrapGroup.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxStgRowStatus"),
        ("TIMETRA-LOG-MIB", "tmnxStgDescription"),
        ("TIMETRA-LOG-MIB", "tmnxStgVersion"),
        ("TIMETRA-LOG-MIB", "tmnxStgNotifyCommunity"),
        ("TIMETRA-LOG-MIB", "tmnxStgSecurityLevel"))
)
if mibBuilder.loadTexts:
    tmnxSnmpTrapGroup.setStatus("obsolete")

tmnxLogEventsR2r1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 10)
)
tmnxLogEventsR2r1Group.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxEventAppName"),
        ("TIMETRA-LOG-MIB", "tmnxEventName"),
        ("TIMETRA-LOG-MIB", "tmnxEventSeverity"),
        ("TIMETRA-LOG-MIB", "tmnxEventControl"),
        ("TIMETRA-LOG-MIB", "tmnxEventCounter"),
        ("TIMETRA-LOG-MIB", "tmnxEventDropCount"),
        ("TIMETRA-LOG-MIB", "tmnxEventReset"),
        ("TIMETRA-LOG-MIB", "tmnxEventTest"))
)
if mibBuilder.loadTexts:
    tmnxLogEventsR2r1Group.setStatus("obsolete")

tmnxLogNotifyObjsR3r0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 13)
)
tmnxLogNotifyObjsR3r0Group.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogFileDeletedLogId"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileDeletedFileId"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileDeletedLogType"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileDeletedLocation"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileDeletedName"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileDeletedCreateTime"),
        ("TIMETRA-LOG-MIB", "tmnxLogTraceErrorTitle"),
        ("TIMETRA-LOG-MIB", "tmnxLogTraceErrorMessage"))
)
if mibBuilder.loadTexts:
    tmnxLogNotifyObjsR3r0Group.setStatus("obsolete")

tmnxLogV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 15)
)
tmnxLogV4v0Group.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogIdRowStatus"),
        ("TIMETRA-LOG-MIB", "tmnxLogIdStorageType"),
        ("TIMETRA-LOG-MIB", "tmnxLogIdAdminStatus"),
        ("TIMETRA-LOG-MIB", "tmnxLogIdOperStatus"),
        ("TIMETRA-LOG-MIB", "tmnxLogIdDescription"),
        ("TIMETRA-LOG-MIB", "tmnxLogIdFilterId"),
        ("TIMETRA-LOG-MIB", "tmnxLogIdSource"),
        ("TIMETRA-LOG-MIB", "tmnxLogIdDestination"),
        ("TIMETRA-LOG-MIB", "tmnxLogIdFileId"),
        ("TIMETRA-LOG-MIB", "tmnxLogIdSyslogId"),
        ("TIMETRA-LOG-MIB", "tmnxLogIdMaxMemorySize"),
        ("TIMETRA-LOG-MIB", "tmnxLogIdConsoleSession"),
        ("TIMETRA-LOG-MIB", "tmnxLogIdForwarded"),
        ("TIMETRA-LOG-MIB", "tmnxLogIdDropped"),
        ("TIMETRA-LOG-MIB", "tmnxLogIdTimeFormat"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterRowStatus"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterDescription"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterDefaultAction"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterInUse"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterParamsRowStatus"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterParamsDescription"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterParamsAction"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterParamsApplication"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterParamsApplOperator"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterParamsNumber"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterParamsNumberOperator"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterParamsSeverity"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterParamsSeverityOperator"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterParamsSubject"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterParamsSubjectOperator"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterParamsSubjectRegexp"))
)
if mibBuilder.loadTexts:
    tmnxLogV4v0Group.setStatus("obsolete")

tmnxSnmpSetErrsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 16)
)
tmnxSnmpSetErrsGroup.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxSnmpSetErrsMax"),
        ("TIMETRA-LOG-MIB", "tmnxSseVersion"),
        ("TIMETRA-LOG-MIB", "tmnxSseSeverityLevel"),
        ("TIMETRA-LOG-MIB", "tmnxSseModuleId"),
        ("TIMETRA-LOG-MIB", "tmnxSseModuleName"),
        ("TIMETRA-LOG-MIB", "tmnxSseErrorCode"),
        ("TIMETRA-LOG-MIB", "tmnxSseErrorName"),
        ("TIMETRA-LOG-MIB", "tmnxSseErrorMsg"),
        ("TIMETRA-LOG-MIB", "tmnxSseExtraText"),
        ("TIMETRA-LOG-MIB", "tmnxSseTimestamp"))
)
if mibBuilder.loadTexts:
    tmnxSnmpSetErrsGroup.setStatus("current")

tmnxLogEventsV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 17)
)
tmnxLogEventsV5v0Group.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxEventAppName"),
        ("TIMETRA-LOG-MIB", "tmnxEventName"),
        ("TIMETRA-LOG-MIB", "tmnxEventSeverity"),
        ("TIMETRA-LOG-MIB", "tmnxEventControl"),
        ("TIMETRA-LOG-MIB", "tmnxEventCounter"),
        ("TIMETRA-LOG-MIB", "tmnxEventDropCount"),
        ("TIMETRA-LOG-MIB", "tmnxEventReset"),
        ("TIMETRA-LOG-MIB", "tmnxEventThrottle"),
        ("TIMETRA-LOG-MIB", "tmnxEventTest"),
        ("TIMETRA-LOG-MIB", "tmnxEventThrottleLimit"),
        ("TIMETRA-LOG-MIB", "tmnxEventThrottleInterval"))
)
if mibBuilder.loadTexts:
    tmnxLogEventsV5v0Group.setStatus("current")

tmnxLogNotifyObjsV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 18)
)
tmnxLogNotifyObjsV5v0Group.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogFileDeletedLogId"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileDeletedFileId"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileDeletedLogType"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileDeletedLocation"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileDeletedName"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileDeletedCreateTime"),
        ("TIMETRA-LOG-MIB", "tmnxLogTraceErrorTitle"),
        ("TIMETRA-LOG-MIB", "tmnxLogTraceErrorMessage"),
        ("TIMETRA-LOG-MIB", "tmnxLogThrottledEventID"),
        ("TIMETRA-LOG-MIB", "tmnxLogThrottledEvents"),
        ("TIMETRA-LOG-MIB", "tmnxSysLogTargetId"),
        ("TIMETRA-LOG-MIB", "tmnxSysLogTargetProblemDescr"))
)
if mibBuilder.loadTexts:
    tmnxLogNotifyObjsV5v0Group.setStatus("obsolete")

tmnxLogSyslogV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 20)
)
tmnxLogSyslogV5v0Group.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxSyslogTargetRowStatus"),
        ("TIMETRA-LOG-MIB", "tmnxSyslogTargetDescription"),
        ("TIMETRA-LOG-MIB", "tmnxSyslogTargetUdpPort"),
        ("TIMETRA-LOG-MIB", "tmnxSyslogTargetFacility"),
        ("TIMETRA-LOG-MIB", "tmnxSyslogTargetSeverity"),
        ("TIMETRA-LOG-MIB", "tmnxSyslogTargetMessagePrefix"),
        ("TIMETRA-LOG-MIB", "tmnxSyslogTargetMessagesDropped"),
        ("TIMETRA-LOG-MIB", "tmnxSyslogTargetAddrType"),
        ("TIMETRA-LOG-MIB", "tmnxSyslogTargetAddr"))
)
if mibBuilder.loadTexts:
    tmnxLogSyslogV5v0Group.setStatus("current")

tmnxSnmpTrapV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 21)
)
tmnxSnmpTrapV5v0Group.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxSnmpTrapLogDescription"),
        ("TIMETRA-LOG-MIB", "tmnxStdRowStatus"),
        ("TIMETRA-LOG-MIB", "tmnxStdRowLastChanged"),
        ("TIMETRA-LOG-MIB", "tmnxStdDestAddrType"),
        ("TIMETRA-LOG-MIB", "tmnxStdDestAddr"),
        ("TIMETRA-LOG-MIB", "tmnxStdDestPort"),
        ("TIMETRA-LOG-MIB", "tmnxStdDescription"),
        ("TIMETRA-LOG-MIB", "tmnxStdVersion"),
        ("TIMETRA-LOG-MIB", "tmnxStdNotifyCommunity"),
        ("TIMETRA-LOG-MIB", "tmnxStdSecurityLevel"),
        ("TIMETRA-LOG-MIB", "tmnxStdMaxTargets"))
)
if mibBuilder.loadTexts:
    tmnxSnmpTrapV5v0Group.setStatus("current")

tmnxLogV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 22)
)
tmnxLogV5v0Group.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogIdRowStatus"),
        ("TIMETRA-LOG-MIB", "tmnxLogIdStorageType"),
        ("TIMETRA-LOG-MIB", "tmnxLogIdAdminStatus"),
        ("TIMETRA-LOG-MIB", "tmnxLogIdOperStatus"),
        ("TIMETRA-LOG-MIB", "tmnxLogIdDescription"),
        ("TIMETRA-LOG-MIB", "tmnxLogIdFilterId"),
        ("TIMETRA-LOG-MIB", "tmnxLogIdSource"),
        ("TIMETRA-LOG-MIB", "tmnxLogIdDestination"),
        ("TIMETRA-LOG-MIB", "tmnxLogIdFileId"),
        ("TIMETRA-LOG-MIB", "tmnxLogIdSyslogId"),
        ("TIMETRA-LOG-MIB", "tmnxLogIdMaxMemorySize"),
        ("TIMETRA-LOG-MIB", "tmnxLogIdConsoleSession"),
        ("TIMETRA-LOG-MIB", "tmnxLogIdForwarded"),
        ("TIMETRA-LOG-MIB", "tmnxLogIdDropped"),
        ("TIMETRA-LOG-MIB", "tmnxLogIdTimeFormat"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterRowStatus"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterDescription"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterDefaultAction"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterInUse"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterParamsRowStatus"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterParamsDescription"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterParamsAction"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterParamsApplication"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterParamsApplOperator"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterParamsNumber"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterParamsNumberOperator"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterParamsSeverity"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterParamsSeverityOperator"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterParamsSubject"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterParamsSubjectOperator"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterParamsSubjectRegexp"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterParamsRouter"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterParamsRouterOperator"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterParamsRouterRegexp"))
)
if mibBuilder.loadTexts:
    tmnxLogV5v0Group.setStatus("current")

tmnxLogObsoleteObjsV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 23)
)
tmnxLogObsoleteObjsV5v0Group.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxSyslogTargetAddress"),
        ("TIMETRA-LOG-MIB", "tmnxStgRowStatus"),
        ("TIMETRA-LOG-MIB", "tmnxStgDescription"),
        ("TIMETRA-LOG-MIB", "tmnxStgVersion"),
        ("TIMETRA-LOG-MIB", "tmnxStgNotifyCommunity"),
        ("TIMETRA-LOG-MIB", "tmnxStgSecurityLevel"))
)
if mibBuilder.loadTexts:
    tmnxLogObsoleteObjsV5v0Group.setStatus("current")

tmnxLogNotifyObjsV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 24)
)
tmnxLogNotifyObjsV6v0Group.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogFileDeletedLogId"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileDeletedFileId"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileDeletedLogType"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileDeletedLocation"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileDeletedName"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileDeletedCreateTime"),
        ("TIMETRA-LOG-MIB", "tmnxLogTraceErrorTitle"),
        ("TIMETRA-LOG-MIB", "tmnxLogTraceErrorMessage"),
        ("TIMETRA-LOG-MIB", "tmnxLogThrottledEventID"),
        ("TIMETRA-LOG-MIB", "tmnxLogThrottledEvents"),
        ("TIMETRA-LOG-MIB", "tmnxSysLogTargetId"),
        ("TIMETRA-LOG-MIB", "tmnxSysLogTargetProblemDescr"),
        ("TIMETRA-LOG-MIB", "tmnxLogNotifyApInterval"),
        ("TIMETRA-LOG-MIB", "tmnxStdReplayStartEvent"),
        ("TIMETRA-LOG-MIB", "tmnxStdReplayEndEvent"))
)
if mibBuilder.loadTexts:
    tmnxLogNotifyObjsV6v0Group.setStatus("obsolete")

tmnxSnmpTrapDestV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 26)
)
tmnxSnmpTrapDestV6v0Group.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxStdReplay"),
        ("TIMETRA-LOG-MIB", "tmnxStdReplayStart"),
        ("TIMETRA-LOG-MIB", "tmnxStdReplayLastTime"))
)
if mibBuilder.loadTexts:
    tmnxSnmpTrapDestV6v0Group.setStatus("current")

tmnxLogAccountingPolicyV6v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 27)
)
tmnxLogAccountingPolicyV6v1Group.setObjects(
    ("TIMETRA-LOG-MIB", "tmnxLogApDefaultInterval")
)
if mibBuilder.loadTexts:
    tmnxLogAccountingPolicyV6v1Group.setStatus("obsolete")

tmnxLogAccountingPolicyCRV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 28)
)
tmnxLogAccountingPolicyCRV7v0Group.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogApCrLastChanged"),
        ("TIMETRA-LOG-MIB", "tmnxLogApCrSignChangeDelta"),
        ("TIMETRA-LOG-MIB", "tmnxLogApCrSignChangeQueue"),
        ("TIMETRA-LOG-MIB", "tmnxLogApCrSignChangeQICounters"),
        ("TIMETRA-LOG-MIB", "tmnxLogApCrSignChangeQECounters"),
        ("TIMETRA-LOG-MIB", "tmnxLogApCrSignChangeAACounters"),
        ("TIMETRA-LOG-MIB", "tmnxLogApCrAACounters"),
        ("TIMETRA-LOG-MIB", "tmnxLogApCrQueueRowStatus"),
        ("TIMETRA-LOG-MIB", "tmnxLogApCrQueueLastChanged"),
        ("TIMETRA-LOG-MIB", "tmnxLogApCrQueueICounters"),
        ("TIMETRA-LOG-MIB", "tmnxLogApCrQueueECounters"))
)
if mibBuilder.loadTexts:
    tmnxLogAccountingPolicyCRV7v0Group.setStatus("current")

tmnxLogRoutePreferenceV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 29)
)
tmnxLogRoutePreferenceV7v0Group.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxEventPrimaryRoutePref"),
        ("TIMETRA-LOG-MIB", "tmnxEventSecondaryRoutePref"))
)
if mibBuilder.loadTexts:
    tmnxLogRoutePreferenceV7v0Group.setStatus("current")

tmnxLogNotifyObjsV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 30)
)
tmnxLogNotifyObjsV8v0Group.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogFileDeletedLogId"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileDeletedFileId"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileDeletedLogType"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileDeletedLocation"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileDeletedName"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileDeletedCreateTime"),
        ("TIMETRA-LOG-MIB", "tmnxLogTraceErrorTitle"),
        ("TIMETRA-LOG-MIB", "tmnxLogTraceErrorSubject"),
        ("TIMETRA-LOG-MIB", "tmnxLogTraceErrorMessage"),
        ("TIMETRA-LOG-MIB", "tmnxLogThrottledEventID"),
        ("TIMETRA-LOG-MIB", "tmnxLogThrottledEvents"),
        ("TIMETRA-LOG-MIB", "tmnxSysLogTargetId"),
        ("TIMETRA-LOG-MIB", "tmnxSysLogTargetProblemDescr"),
        ("TIMETRA-LOG-MIB", "tmnxLogNotifyApInterval"),
        ("TIMETRA-LOG-MIB", "tmnxStdReplayStartEvent"),
        ("TIMETRA-LOG-MIB", "tmnxStdReplayEndEvent"))
)
if mibBuilder.loadTexts:
    tmnxLogNotifyObjsV8v0Group.setStatus("current")

tmnxLogEventDampedV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 32)
)
tmnxLogEventDampedV8v0Group.setObjects(
    ("TIMETRA-LOG-MIB", "tmnxLogConfigEventsDamped")
)
if mibBuilder.loadTexts:
    tmnxLogEventDampedV8v0Group.setStatus("current")

tmnxLogApV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 33)
)
tmnxLogApV9v0Group.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogApDataLossCount"),
        ("TIMETRA-LOG-MIB", "tmnxLogApLastDataLossTimeStamp"))
)
if mibBuilder.loadTexts:
    tmnxLogApV9v0Group.setStatus("current")

tmnxLogExRbkOpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 34)
)
tmnxLogExRbkOpGroup.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogExRbkOpTblLastChange"),
        ("TIMETRA-LOG-MIB", "tmnxLogExRbkOpMaxEntries"),
        ("TIMETRA-LOG-MIB", "tmnxLogExRbkOpLastChanged"),
        ("TIMETRA-LOG-MIB", "tmnxLogExRbkOpType"),
        ("TIMETRA-LOG-MIB", "tmnxLogExRbkOpStatus"),
        ("TIMETRA-LOG-MIB", "tmnxLogExRbkOpBegin"),
        ("TIMETRA-LOG-MIB", "tmnxLogExRbkOpEnd"),
        ("TIMETRA-LOG-MIB", "tmnxLogExRbkOpFile"),
        ("TIMETRA-LOG-MIB", "tmnxLogExRbkOpUser"),
        ("TIMETRA-LOG-MIB", "tmnxLogExRbkOpNumEvents"),
        ("TIMETRA-LOG-MIB", "tmnxLogExRbkEventOID"))
)
if mibBuilder.loadTexts:
    tmnxLogExRbkOpGroup.setStatus("current")

tmnxLogNotifyObjsV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 35)
)
tmnxLogNotifyObjsV10v0Group.setObjects(
    ("TIMETRA-LOG-MIB", "tmnxLogExecRollbackOpIndex")
)
if mibBuilder.loadTexts:
    tmnxLogNotifyObjsV10v0Group.setStatus("current")

tmnxLogApExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 36)
)
tmnxLogApExtGroup.setObjects(
    ("TIMETRA-LOG-MIB", "tmnxLogApToFileType")
)
if mibBuilder.loadTexts:
    tmnxLogApExtGroup.setStatus("current")

tmnxLogAppRouteNotifV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 37)
)
tmnxLogAppRouteNotifV10v0Group.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogColdStartWaitTime"),
        ("TIMETRA-LOG-MIB", "tmnxLogRouteRecoveryWaitTime"))
)
if mibBuilder.loadTexts:
    tmnxLogAppRouteNotifV10v0Group.setStatus("current")

tmnxLogApV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 38)
)
tmnxLogApV11v0Group.setObjects(
    ("TIMETRA-LOG-MIB", "tmnxLogApIncludeSystemInfo")
)
if mibBuilder.loadTexts:
    tmnxLogApV11v0Group.setStatus("current")

tmnxLogEventsV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 40)
)
tmnxLogEventsV11v0Group.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxEventSpecThrottle"),
        ("TIMETRA-LOG-MIB", "tmnxEventSpecThrottleLimit"),
        ("TIMETRA-LOG-MIB", "tmnxEventSpecThrottleIntval"),
        ("TIMETRA-LOG-MIB", "tmnxEventSpecThrottleDef"),
        ("TIMETRA-LOG-MIB", "tmnxEventSpecThrottleLimitDef"),
        ("TIMETRA-LOG-MIB", "tmnxEventSpecThrottleIntvalDef"))
)
if mibBuilder.loadTexts:
    tmnxLogEventsV11v0Group.setStatus("current")

tmnxLogApCrV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 41)
)
tmnxLogApCrV11v0Group.setObjects(
    ("TIMETRA-LOG-MIB", "tmnxLogApCrAASubAttributes")
)
if mibBuilder.loadTexts:
    tmnxLogApCrV11v0Group.setStatus("current")

tmnxLogFilterMsgV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 42)
)
tmnxLogFilterMsgV13v0Group.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogFilterParamsMsg"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterParamsMsgOperator"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterParamsMsgRegexp"))
)
if mibBuilder.loadTexts:
    tmnxLogFilterMsgV13v0Group.setStatus("current")

tmnxLogNotifyObjsV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 43)
)
tmnxLogNotifyObjsV13v0Group.setObjects(
    ("TIMETRA-LOG-MIB", "tmnxLogExecRollbackOpType")
)
if mibBuilder.loadTexts:
    tmnxLogNotifyObjsV13v0Group.setStatus("current")

tmnxLogEHSV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 44)
)
tmnxLogEHSV13v0Group.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxEhsHandlerTblLastChange"),
        ("TIMETRA-LOG-MIB", "tmnxEhsHandlerMaxEntries"),
        ("TIMETRA-LOG-MIB", "tmnxEhsHandlerRowStatus"),
        ("TIMETRA-LOG-MIB", "tmnxEhsHandlerDescription"),
        ("TIMETRA-LOG-MIB", "tmnxEhsHandlerLastChange"),
        ("TIMETRA-LOG-MIB", "tmnxEhsHandlerAdminStatus"),
        ("TIMETRA-LOG-MIB", "tmnxEhsHandlerOperStatus"),
        ("TIMETRA-LOG-MIB", "tmnxEhsHandlerStatsSuccess"),
        ("TIMETRA-LOG-MIB", "tmnxEhsHandlerStatsErrNoEntry"),
        ("TIMETRA-LOG-MIB", "tmnxEhsHandlerStatsErrAdmStatus"),
        ("TIMETRA-LOG-MIB", "tmnxEhsHEntryTblLastChange"),
        ("TIMETRA-LOG-MIB", "tmnxEhsHEntryMaxEntries"),
        ("TIMETRA-LOG-MIB", "tmnxEhsHEntryRowStatus"),
        ("TIMETRA-LOG-MIB", "tmnxEhsHEntryDescription"),
        ("TIMETRA-LOG-MIB", "tmnxEhsHEntryLastChange"),
        ("TIMETRA-LOG-MIB", "tmnxEhsHEntryAdminStatus"),
        ("TIMETRA-LOG-MIB", "tmnxEhsHEntryOperStatus"),
        ("TIMETRA-LOG-MIB", "tmnxEhsHEntryScriptPlcyName"),
        ("TIMETRA-LOG-MIB", "tmnxEhsHEntryScriptPlcyOwner"),
        ("TIMETRA-LOG-MIB", "tmnxEhsHEntryMinDelay"),
        ("TIMETRA-LOG-MIB", "tmnxEhsHEntryLastExecuted"),
        ("TIMETRA-LOG-MIB", "tmnxEhsHEntryStatsLaunchSuccess"),
        ("TIMETRA-LOG-MIB", "tmnxEhsHEntryStatsErrMinDelay"),
        ("TIMETRA-LOG-MIB", "tmnxEhsHEntryStatsErrLaunch"),
        ("TIMETRA-LOG-MIB", "tmnxEhsHEntryStatsErrAdmStatus"),
        ("TIMETRA-LOG-MIB", "tmnxEhsTriggerTblLastChange"),
        ("TIMETRA-LOG-MIB", "tmnxEhsTriggerMaxEntries"),
        ("TIMETRA-LOG-MIB", "tmnxEhsTriggerRowStatus"),
        ("TIMETRA-LOG-MIB", "tmnxEhsTriggerDescription"),
        ("TIMETRA-LOG-MIB", "tmnxEhsTriggerLastChange"),
        ("TIMETRA-LOG-MIB", "tmnxEhsTriggerAdminStatus"),
        ("TIMETRA-LOG-MIB", "tmnxEhsTriggerOperStatus"),
        ("TIMETRA-LOG-MIB", "tmnxEhsTriggerStatsSuccess"),
        ("TIMETRA-LOG-MIB", "tmnxEhsTriggerStatsErrNoEntry"),
        ("TIMETRA-LOG-MIB", "tmnxEhsTriggerStatsErrAdmStatus"),
        ("TIMETRA-LOG-MIB", "tmnxEhsTEntryTblLastChange"),
        ("TIMETRA-LOG-MIB", "tmnxEhsTEntryMaxEntries"),
        ("TIMETRA-LOG-MIB", "tmnxEhsTEntryRowStatus"),
        ("TIMETRA-LOG-MIB", "tmnxEhsTEntryDescription"),
        ("TIMETRA-LOG-MIB", "tmnxEhsTEntryLastChange"),
        ("TIMETRA-LOG-MIB", "tmnxEhsTEntryAdminStatus"),
        ("TIMETRA-LOG-MIB", "tmnxEhsTEntryOperStatus"),
        ("TIMETRA-LOG-MIB", "tmnxEhsTEntryLogFilterId"),
        ("TIMETRA-LOG-MIB", "tmnxEhsTEntryHandlerName"),
        ("TIMETRA-LOG-MIB", "tmnxEhsTEntryStatsFilterMatch"),
        ("TIMETRA-LOG-MIB", "tmnxEhsTEntryStatsFilterFail"),
        ("TIMETRA-LOG-MIB", "tmnxEhsTEntryStatsErrAdminStatus"),
        ("TIMETRA-LOG-MIB", "tmnxEhsTEntryStatsErrFilter"),
        ("TIMETRA-LOG-MIB", "tmnxEhsTEntryStatsErrHandler"),
        ("TIMETRA-LOG-MIB", "tmnxEhsTEntryStatsTriggerCount"))
)
if mibBuilder.loadTexts:
    tmnxLogEHSV13v0Group.setStatus("current")

tmnxLogNotifyObjsV14v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 45)
)
tmnxLogNotifyObjsV14v0Group.setObjects(
    ("TIMETRA-LOG-MIB", "tmnxEhsHEntryMinDelayInterval")
)
if mibBuilder.loadTexts:
    tmnxLogNotifyObjsV14v0Group.setStatus("current")

tmnxLogEHSV14v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 46)
)
tmnxLogEHSV14v0Group.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxEhsTEntryDebounceVal"),
        ("TIMETRA-LOG-MIB", "tmnxEhsTEntryDebounceTime"),
        ("TIMETRA-LOG-MIB", "tmnxEhsTEntryStatsDebounce"))
)
if mibBuilder.loadTexts:
    tmnxLogEHSV14v0Group.setStatus("current")

tmnxLogPythonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 50)
)
tmnxLogPythonGroup.setObjects(
    ("TIMETRA-LOG-MIB", "tmnxLogIdPythonPolicy")
)
if mibBuilder.loadTexts:
    tmnxLogPythonGroup.setStatus("current")

tmnxLogToSessionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 51)
)
tmnxLogToSessionGroup.setObjects(
    ("TIMETRA-LOG-MIB", "tmnxLogIdOperDestination")
)
if mibBuilder.loadTexts:
    tmnxLogToSessionGroup.setStatus("current")

tmnxLogObsoleteObjsV15v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 52)
)
tmnxLogObsoleteObjsV15v0Group.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogIdConsoleSession"),
        ("TIMETRA-LOG-MIB", "tmnxLogApDefaultInterval"))
)
if mibBuilder.loadTexts:
    tmnxLogObsoleteObjsV15v0Group.setStatus("current")

tmnxLogToNetconfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 53)
)
tmnxLogToNetconfGroup.setObjects(
    ("TIMETRA-LOG-MIB", "tmnxLogIdNetconfStream")
)
if mibBuilder.loadTexts:
    tmnxLogToNetconfGroup.setStatus("current")

tmnxLogEventsV16v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 54)
)
tmnxLogEventsV16v0Group.setObjects(
    ("TIMETRA-LOG-MIB", "tmnxEventRepeat")
)
if mibBuilder.loadTexts:
    tmnxLogEventsV16v0Group.setStatus("current")

tmnxLogCliSubscrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 55)
)
tmnxLogCliSubscrGroup.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogCliSubscrType"),
        ("TIMETRA-LOG-MIB", "tmnxLogCliSubscrUser"),
        ("TIMETRA-LOG-MIB", "tmnxLogCliSubscrUserLoginTime"),
        ("TIMETRA-LOG-MIB", "tmnxLogCliSubscrUserIpAddrType"),
        ("TIMETRA-LOG-MIB", "tmnxLogCliSubscrUserIpAddr"))
)
if mibBuilder.loadTexts:
    tmnxLogCliSubscrGroup.setStatus("current")

tmnxLogAcctPolicyCrV19v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 56)
)
tmnxLogAcctPolicyCrV19v0Group.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogApCrPolicerLastChanged"),
        ("TIMETRA-LOG-MIB", "tmnxLogApCrPolicerRowStatus"),
        ("TIMETRA-LOG-MIB", "tmnxLogApCrPolicerICounters"),
        ("TIMETRA-LOG-MIB", "tmnxLogApCrPolicerECounters"),
        ("TIMETRA-LOG-MIB", "tmnxLogApCrSignChangePolicer"),
        ("TIMETRA-LOG-MIB", "tmnxLogApCrSignChangePICounters"),
        ("TIMETRA-LOG-MIB", "tmnxLogApCrSignChangePECounters"))
)
if mibBuilder.loadTexts:
    tmnxLogAcctPolicyCrV19v0Group.setStatus("current")

tmnxLogApV19v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 57)
)
tmnxLogApV19v0Group.setObjects(
    ("TIMETRA-LOG-MIB", "tmnxLogApAlign")
)
if mibBuilder.loadTexts:
    tmnxLogApV19v0Group.setStatus("current")

tmnxLogNameGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 58)
)
tmnxLogNameGroup.setObjects(
    ("TIMETRA-LOG-MIB", "tmnxLogIdName")
)
if mibBuilder.loadTexts:
    tmnxLogNameGroup.setStatus("current")

tmnxLogFilterNameGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 59)
)
tmnxLogFilterNameGroup.setObjects(
    ("TIMETRA-LOG-MIB", "tmnxLogFilterName")
)
if mibBuilder.loadTexts:
    tmnxLogFilterNameGroup.setStatus("current")

tmnxLogSnmpTrapGroupNameGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 60)
)
tmnxLogSnmpTrapGroupNameGroup.setObjects(
    ("TIMETRA-LOG-MIB", "snmpNotifyId")
)
if mibBuilder.loadTexts:
    tmnxLogSnmpTrapGroupNameGroup.setStatus("current")

tmnxLogFilterParamsNameGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 61)
)
tmnxLogFilterParamsNameGroup.setObjects(
    ("TIMETRA-LOG-MIB", "tmnxLogFilterParamsName")
)
if mibBuilder.loadTexts:
    tmnxLogFilterParamsNameGroup.setStatus("current")

tmnxSyslogTargetNameGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 63)
)
tmnxSyslogTargetNameGroup.setObjects(
    ("TIMETRA-LOG-MIB", "tmnxSyslogTargetName")
)
if mibBuilder.loadTexts:
    tmnxSyslogTargetNameGroup.setStatus("current")

tmnxSyslogTlsClntProfilNameGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 64)
)
tmnxSyslogTlsClntProfilNameGroup.setObjects(
    ("TIMETRA-LOG-MIB", "tmnxSyslogTlsClntProfileName")
)
if mibBuilder.loadTexts:
    tmnxSyslogTlsClntProfilNameGroup.setStatus("current")

tmnxLogApObsoleteObjsV21v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 65)
)
tmnxLogApObsoleteObjsV21v0Group.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogApCrSignChangeOCntr"),
        ("TIMETRA-LOG-MIB", "tmnxLogApCrSignChangeOECounters"),
        ("TIMETRA-LOG-MIB", "tmnxLogApCrSignChangeOICounters"),
        ("TIMETRA-LOG-MIB", "tmnxLogApCrOverrideCntrRowStatus"),
        ("TIMETRA-LOG-MIB", "tmnxLogApCrOverrideCntrLastChngd"),
        ("TIMETRA-LOG-MIB", "tmnxLogApCrOverrideCntrICounters"),
        ("TIMETRA-LOG-MIB", "tmnxLogApCrOverrideCntrECounters"))
)
if mibBuilder.loadTexts:
    tmnxLogApObsoleteObjsV21v0Group.setStatus("current")

tmnxLogFileNameGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 66)
)
tmnxLogFileNameGroup.setObjects(
    ("TIMETRA-LOG-MIB", "tmnxLogFileIdName")
)
if mibBuilder.loadTexts:
    tmnxLogFileNameGroup.setStatus("current")

tmnxSnmpTrapDestV22v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 67)
)
tmnxSnmpTrapDestV22v0Group.setObjects(
    ("TIMETRA-LOG-MIB", "tmnxStdDyingGasp")
)
if mibBuilder.loadTexts:
    tmnxSnmpTrapDestV22v0Group.setStatus("current")


# Notification objects

tmnxLogSpaceContention = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 12, 0, 1)
)
tmnxLogSpaceContention.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogFileIdRolloverTime"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdRetainTime"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdAdminLocation"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdBackupLoc"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdOperLocation"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdLogId"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdLogType"))
)
if mibBuilder.loadTexts:
    tmnxLogSpaceContention.setStatus(
        "current"
    )

tmnxLogAdminLocFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 12, 0, 2)
)
tmnxLogAdminLocFailed.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogFileIdAdminLocation"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdBackupLoc"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdOperLocation"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdLogId"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdLogType"))
)
if mibBuilder.loadTexts:
    tmnxLogAdminLocFailed.setStatus(
        "current"
    )

tmnxLogBackupLocFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 12, 0, 3)
)
tmnxLogBackupLocFailed.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogFileIdAdminLocation"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdBackupLoc"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdOperLocation"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdLogId"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdLogType"))
)
if mibBuilder.loadTexts:
    tmnxLogBackupLocFailed.setStatus(
        "current"
    )

tmnxLogFileRollover = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 12, 0, 4)
)
tmnxLogFileRollover.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogFileIdRolloverTime"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdRetainTime"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdAdminLocation"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdBackupLoc"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdOperLocation"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdLogId"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdLogType"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdPathName"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdCreateTime"))
)
if mibBuilder.loadTexts:
    tmnxLogFileRollover.setStatus(
        "current"
    )

tmnxLogFileDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 12, 0, 5)
)
tmnxLogFileDeleted.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogFileDeletedLogId"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileDeletedFileId"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileDeletedLogType"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileDeletedLocation"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileDeletedName"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileDeletedCreateTime"))
)
if mibBuilder.loadTexts:
    tmnxLogFileDeleted.setStatus(
        "current"
    )

tmnxTestEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 12, 0, 6)
)
tmnxTestEvent.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysObjectID"))
)
if mibBuilder.loadTexts:
    tmnxTestEvent.setStatus(
        "current"
    )

tmnxLogTraceError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 12, 0, 7)
)
tmnxLogTraceError.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogTraceErrorTitle"),
        ("TIMETRA-LOG-MIB", "tmnxLogTraceErrorMessage"),
        ("TIMETRA-LOG-MIB", "tmnxLogTraceErrorSubject"))
)
if mibBuilder.loadTexts:
    tmnxLogTraceError.setStatus(
        "current"
    )

tmnxLogEventThrottled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 12, 0, 8)
)
tmnxLogEventThrottled.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogThrottledEventID"),
        ("TIMETRA-LOG-MIB", "tmnxLogThrottledEvents"))
)
if mibBuilder.loadTexts:
    tmnxLogEventThrottled.setStatus(
        "current"
    )

tmnxSysLogTargetProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 12, 0, 9)
)
tmnxSysLogTargetProblem.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxSysLogTargetId"),
        ("TIMETRA-LOG-MIB", "tmnxSysLogTargetProblemDescr"))
)
if mibBuilder.loadTexts:
    tmnxSysLogTargetProblem.setStatus(
        "current"
    )

tmnxLogAccountingDataLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 12, 0, 10)
)
tmnxLogAccountingDataLoss.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogFileIdRolloverTime"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdRetainTime"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdAdminLocation"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdBackupLoc"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdOperLocation"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdLogId"),
        ("TIMETRA-LOG-MIB", "tmnxLogNotifyApInterval"))
)
if mibBuilder.loadTexts:
    tmnxLogAccountingDataLoss.setStatus(
        "current"
    )

tmnxStdEventsReplayed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 12, 0, 11)
)
tmnxStdEventsReplayed.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxStdDestAddrType"),
        ("TIMETRA-LOG-MIB", "tmnxStdDestAddr"),
        ("TIMETRA-LOG-MIB", "tmnxStdReplayStartEvent"),
        ("TIMETRA-LOG-MIB", "tmnxStdReplayEndEvent"),
        ("TIMETRA-LOG-MIB", "tmnxStdReplayStart"))
)
if mibBuilder.loadTexts:
    tmnxStdEventsReplayed.setStatus(
        "current"
    )

tmnxLogEventOverrun = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 12, 0, 12)
)
tmnxLogEventOverrun.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogThrottledEventID"),
        ("TIMETRA-LOG-MIB", "tmnxLogThrottledEvents"))
)
if mibBuilder.loadTexts:
    tmnxLogEventOverrun.setStatus(
        "current"
    )


# Notifications groups

tmnxLogNotificationR3r0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 14)
)
tmnxLogNotificationR3r0Group.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogSpaceContention"),
        ("TIMETRA-LOG-MIB", "tmnxLogAdminLocFailed"),
        ("TIMETRA-LOG-MIB", "tmnxLogBackupLocFailed"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileRollover"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileDeleted"),
        ("TIMETRA-LOG-MIB", "tmnxTestEvent"),
        ("TIMETRA-LOG-MIB", "tmnxLogTraceError"))
)
if mibBuilder.loadTexts:
    tmnxLogNotificationR3r0Group.setStatus(
        "obsolete"
    )

tmnxLogNotificationV5v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 19)
)
tmnxLogNotificationV5v0Group.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogSpaceContention"),
        ("TIMETRA-LOG-MIB", "tmnxLogAdminLocFailed"),
        ("TIMETRA-LOG-MIB", "tmnxLogBackupLocFailed"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileRollover"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileDeleted"),
        ("TIMETRA-LOG-MIB", "tmnxTestEvent"),
        ("TIMETRA-LOG-MIB", "tmnxLogTraceError"),
        ("TIMETRA-LOG-MIB", "tmnxLogEventThrottled"),
        ("TIMETRA-LOG-MIB", "tmnxSysLogTargetProblem"))
)
if mibBuilder.loadTexts:
    tmnxLogNotificationV5v0Group.setStatus(
        "obsolete"
    )

tmnxLogNotificationV6v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 25)
)
tmnxLogNotificationV6v0Group.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogSpaceContention"),
        ("TIMETRA-LOG-MIB", "tmnxLogAdminLocFailed"),
        ("TIMETRA-LOG-MIB", "tmnxLogBackupLocFailed"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileRollover"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileDeleted"),
        ("TIMETRA-LOG-MIB", "tmnxTestEvent"),
        ("TIMETRA-LOG-MIB", "tmnxLogTraceError"),
        ("TIMETRA-LOG-MIB", "tmnxLogEventThrottled"),
        ("TIMETRA-LOG-MIB", "tmnxSysLogTargetProblem"),
        ("TIMETRA-LOG-MIB", "tmnxLogAccountingDataLoss"),
        ("TIMETRA-LOG-MIB", "tmnxStdEventsReplayed"))
)
if mibBuilder.loadTexts:
    tmnxLogNotificationV6v0Group.setStatus(
        "current"
    )

tmnxLogNotificationV9v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 2, 31)
)
tmnxLogNotificationV9v0Group.setObjects(
    ("TIMETRA-LOG-MIB", "tmnxLogEventOverrun")
)
if mibBuilder.loadTexts:
    tmnxLogNotificationV9v0Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxLogV4v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 1, 4)
)
tmnxLogV4v0Compliance.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogGlobalGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogV4v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogAccountingPolicyGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogSyslogGroup"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpTrapGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogEventsR2r1Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogNotificationR3r0Group"))
)
if mibBuilder.loadTexts:
    tmnxLogV4v0Compliance.setStatus(
        "obsolete"
    )

tmnxLogV5v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 1, 5)
)
tmnxLogV5v0Compliance.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogGlobalGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogAccountingPolicyGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogSyslogV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpTrapV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpSetErrsGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogEventsV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogNotificationV5v0Group"))
)
if mibBuilder.loadTexts:
    tmnxLogV5v0Compliance.setStatus(
        "obsolete"
    )

tmnxLogV6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 1, 6)
)
tmnxLogV6v0Compliance.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogGlobalGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogAccountingPolicyGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogSyslogV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpTrapV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpTrapDestV6v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpSetErrsGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogEventsV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogNotificationV6v0Group"))
)
if mibBuilder.loadTexts:
    tmnxLogV6v0Compliance.setStatus(
        "obsolete"
    )

tmnxLogV6v1Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 1, 7)
)
tmnxLogV6v1Compliance.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogGlobalGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogAccountingPolicyGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogSyslogV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpTrapV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpTrapDestV6v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpSetErrsGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogEventsV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogNotificationV6v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogAccountingPolicyV6v1Group"))
)
if mibBuilder.loadTexts:
    tmnxLogV6v1Compliance.setStatus(
        "obsolete"
    )

tmnxLogV7v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 1, 8)
)
tmnxLogV7v0Compliance.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogGlobalGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogAccountingPolicyGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogSyslogV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpTrapV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpTrapDestV6v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpSetErrsGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogEventsV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogNotificationV6v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogAccountingPolicyV6v1Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogAccountingPolicyCRV7v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogRoutePreferenceV7v0Group"))
)
if mibBuilder.loadTexts:
    tmnxLogV7v0Compliance.setStatus(
        "obsolete"
    )

tmnxLogV9v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 1, 9)
)
tmnxLogV9v0Compliance.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogGlobalGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogAccountingPolicyGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogAccountingPolicyV6v1Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogAccountingPolicyCRV7v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogSyslogV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpTrapV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpTrapDestV6v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpSetErrsGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogEventsV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogNotificationV6v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogNotificationV9v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogRoutePreferenceV7v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogEventDampedV8v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogApV9v0Group"))
)
if mibBuilder.loadTexts:
    tmnxLogV9v0Compliance.setStatus(
        "obsolete"
    )

tmnxLogV8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 1, 10)
)
tmnxLogV8v0Compliance.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogGlobalGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogAccountingPolicyGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogSyslogV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpTrapV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpTrapDestV6v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpSetErrsGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogEventsV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogNotificationV6v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogAccountingPolicyV6v1Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogAccountingPolicyCRV7v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogRoutePreferenceV7v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogEventDampedV8v0Group"))
)
if mibBuilder.loadTexts:
    tmnxLogV8v0Compliance.setStatus(
        "obsolete"
    )

tmnxLogV10v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 1, 11)
)
tmnxLogV10v0Compliance.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogGlobalGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogAccountingPolicyGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogAccountingPolicyV6v1Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogAccountingPolicyCRV7v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogSyslogV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpTrapV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpTrapDestV6v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpSetErrsGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogEventsV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogNotificationV6v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogNotificationV9v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogRoutePreferenceV7v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogEventDampedV8v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogApV9v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogExRbkOpGroup"))
)
if mibBuilder.loadTexts:
    tmnxLogV10v0Compliance.setStatus(
        "obsolete"
    )

tmnxLogV11v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 1, 12)
)
tmnxLogV11v0Compliance.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogGlobalGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogAccountingPolicyGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogAccountingPolicyV6v1Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogAccountingPolicyCRV7v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogSyslogV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpTrapV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpTrapDestV6v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpSetErrsGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogEventsV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogEventsV11v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogNotificationV6v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogNotificationV9v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogRoutePreferenceV7v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogEventDampedV8v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogApV9v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogExRbkOpGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogApExtGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogAppRouteNotifV10v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogApV11v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogApCrV11v0Group"))
)
if mibBuilder.loadTexts:
    tmnxLogV11v0Compliance.setStatus(
        "obsolete"
    )

tmnxLogV13v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 1, 13)
)
tmnxLogV13v0Compliance.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogGlobalGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogAccountingPolicyGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogAccountingPolicyV6v1Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogAccountingPolicyCRV7v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogSyslogV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpTrapV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpTrapDestV6v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpSetErrsGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogEventsV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogEventsV11v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogNotificationV6v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogNotificationV9v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogRoutePreferenceV7v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogEventDampedV8v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogApV9v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogExRbkOpGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogApExtGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogAppRouteNotifV10v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogApV11v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogApCrV11v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterMsgV13v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogEHSV13v0Group"))
)
if mibBuilder.loadTexts:
    tmnxLogV13v0Compliance.setStatus(
        "obsolete"
    )

tmnxLogV14v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 1, 14)
)
tmnxLogV14v0Compliance.setObjects(
    ("TIMETRA-LOG-MIB", "tmnxLogEHSV14v0Group")
)
if mibBuilder.loadTexts:
    tmnxLogV14v0Compliance.setStatus(
        "obsolete"
    )

tmnxLogV15v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 1, 15)
)
tmnxLogV15v0Compliance.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogGlobalGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogAccountingPolicyGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogAccountingPolicyCRV7v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogSyslogV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpTrapV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpTrapDestV6v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpSetErrsGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogEventsV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogEventsV11v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogNotificationV6v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogNotificationV9v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogRoutePreferenceV7v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogEventDampedV8v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogApV9v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogExRbkOpGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogApExtGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogAppRouteNotifV10v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogApV11v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogApCrV11v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterMsgV13v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogEHSV13v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogEHSV14v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogPythonGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogToSessionGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogToNetconfGroup"))
)
if mibBuilder.loadTexts:
    tmnxLogV15v0Compliance.setStatus(
        "obsolete"
    )

tmnxLogV16v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 1, 16)
)
tmnxLogV16v0Compliance.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogGlobalGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogAccountingPolicyGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogAccountingPolicyCRV7v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogSyslogV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpTrapV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpTrapDestV6v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpSetErrsGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogEventsV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogEventsV11v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogNotificationV6v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogNotificationV9v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogRoutePreferenceV7v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogEventDampedV8v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogApV9v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogExRbkOpGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogApExtGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogAppRouteNotifV10v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogApV11v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogApCrV11v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterMsgV13v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogEHSV13v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogEHSV14v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogPythonGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogToSessionGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogToNetconfGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogEventsV16v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogCliSubscrGroup"))
)
if mibBuilder.loadTexts:
    tmnxLogV16v0Compliance.setStatus(
        "obsolete"
    )

tmnxLogV19v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 1, 17)
)
tmnxLogV19v0Compliance.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogGlobalGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogAccountingPolicyGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogAccountingPolicyCRV7v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileIdGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogSyslogV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpTrapV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpTrapDestV6v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxSnmpSetErrsGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogEventsV5v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogEventsV11v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogNotificationV6v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogNotificationV9v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogRoutePreferenceV7v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogEventDampedV8v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogApV9v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogExRbkOpGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogApExtGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogAppRouteNotifV10v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogApV11v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogApCrV11v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterMsgV13v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogEHSV13v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogEHSV14v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogPythonGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogToSessionGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogToNetconfGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogEventsV16v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogCliSubscrGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogAcctPolicyCrV19v0Group"),
        ("TIMETRA-LOG-MIB", "tmnxLogApV19v0Group"))
)
if mibBuilder.loadTexts:
    tmnxLogV19v0Compliance.setStatus(
        "current"
    )

tmnxLogV20v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 1, 18)
)
tmnxLogV20v0Compliance.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogNameGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterNameGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogSnmpTrapGroupNameGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogFilterParamsNameGroup"),
        ("TIMETRA-LOG-MIB", "tmnxSyslogTargetNameGroup"))
)
if mibBuilder.loadTexts:
    tmnxLogV20v0Compliance.setStatus(
        "current"
    )

tmnxLogV21v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 1, 19)
)
tmnxLogV21v0Compliance.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxSyslogTlsClntProfilNameGroup"),
        ("TIMETRA-LOG-MIB", "tmnxLogFileNameGroup"))
)
if mibBuilder.loadTexts:
    tmnxLogV21v0Compliance.setStatus(
        "current"
    )

tmnxLogV22v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 12, 1, 20)
)
tmnxLogV22v0Compliance.setObjects(
    ("TIMETRA-LOG-MIB", "tmnxSnmpTrapDestV22v0Group")
)
if mibBuilder.loadTexts:
    tmnxLogV22v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-LOG-MIB",
    **{"TmnxPerceivedSeverity": TmnxPerceivedSeverity,
       "TmnxSyslogId": TmnxSyslogId,
       "TmnxSyslogIdOrEmpty": TmnxSyslogIdOrEmpty,
       "TmnxLogFileId": TmnxLogFileId,
       "TmnxLogFileType": TmnxLogFileType,
       "TmnxLogIdIndex": TmnxLogIdIndex,
       "TmnxStgIndex": TmnxStgIndex,
       "TmnxCFlash": TmnxCFlash,
       "TmnxLogFilterId": TmnxLogFilterId,
       "TmnxLogFilterEntryId": TmnxLogFilterEntryId,
       "TmnxLogFilterOperator": TmnxLogFilterOperator,
       "TmnxEventNumber": TmnxEventNumber,
       "TmnxLogExRbkOperationType": TmnxLogExRbkOperationType,
       "LogStorageType": LogStorageType,
       "timetraLogMIBModule": timetraLogMIBModule,
       "tmnxLogConformance": tmnxLogConformance,
       "tmnxLogCompliances": tmnxLogCompliances,
       "tmnxLogV4v0Compliance": tmnxLogV4v0Compliance,
       "tmnxLogV5v0Compliance": tmnxLogV5v0Compliance,
       "tmnxLogV6v0Compliance": tmnxLogV6v0Compliance,
       "tmnxLogV6v1Compliance": tmnxLogV6v1Compliance,
       "tmnxLogV7v0Compliance": tmnxLogV7v0Compliance,
       "tmnxLogV9v0Compliance": tmnxLogV9v0Compliance,
       "tmnxLogV8v0Compliance": tmnxLogV8v0Compliance,
       "tmnxLogV10v0Compliance": tmnxLogV10v0Compliance,
       "tmnxLogV11v0Compliance": tmnxLogV11v0Compliance,
       "tmnxLogV13v0Compliance": tmnxLogV13v0Compliance,
       "tmnxLogV14v0Compliance": tmnxLogV14v0Compliance,
       "tmnxLogV15v0Compliance": tmnxLogV15v0Compliance,
       "tmnxLogV16v0Compliance": tmnxLogV16v0Compliance,
       "tmnxLogV19v0Compliance": tmnxLogV19v0Compliance,
       "tmnxLogV20v0Compliance": tmnxLogV20v0Compliance,
       "tmnxLogV21v0Compliance": tmnxLogV21v0Compliance,
       "tmnxLogV22v0Compliance": tmnxLogV22v0Compliance,
       "tmnxLogGroups": tmnxLogGroups,
       "tmnxLogGlobalGroup": tmnxLogGlobalGroup,
       "tmnxLogAccountingPolicyGroup": tmnxLogAccountingPolicyGroup,
       "tmnxLogFileIdGroup": tmnxLogFileIdGroup,
       "tmnxLogSyslogGroup": tmnxLogSyslogGroup,
       "tmnxSnmpTrapGroup": tmnxSnmpTrapGroup,
       "tmnxLogEventsR2r1Group": tmnxLogEventsR2r1Group,
       "tmnxLogNotifyObjsR3r0Group": tmnxLogNotifyObjsR3r0Group,
       "tmnxLogNotificationR3r0Group": tmnxLogNotificationR3r0Group,
       "tmnxLogV4v0Group": tmnxLogV4v0Group,
       "tmnxSnmpSetErrsGroup": tmnxSnmpSetErrsGroup,
       "tmnxLogEventsV5v0Group": tmnxLogEventsV5v0Group,
       "tmnxLogNotifyObjsV5v0Group": tmnxLogNotifyObjsV5v0Group,
       "tmnxLogNotificationV5v0Group": tmnxLogNotificationV5v0Group,
       "tmnxLogSyslogV5v0Group": tmnxLogSyslogV5v0Group,
       "tmnxSnmpTrapV5v0Group": tmnxSnmpTrapV5v0Group,
       "tmnxLogV5v0Group": tmnxLogV5v0Group,
       "tmnxLogObsoleteObjsV5v0Group": tmnxLogObsoleteObjsV5v0Group,
       "tmnxLogNotifyObjsV6v0Group": tmnxLogNotifyObjsV6v0Group,
       "tmnxLogNotificationV6v0Group": tmnxLogNotificationV6v0Group,
       "tmnxSnmpTrapDestV6v0Group": tmnxSnmpTrapDestV6v0Group,
       "tmnxLogAccountingPolicyV6v1Group": tmnxLogAccountingPolicyV6v1Group,
       "tmnxLogAccountingPolicyCRV7v0Group": tmnxLogAccountingPolicyCRV7v0Group,
       "tmnxLogRoutePreferenceV7v0Group": tmnxLogRoutePreferenceV7v0Group,
       "tmnxLogNotifyObjsV8v0Group": tmnxLogNotifyObjsV8v0Group,
       "tmnxLogNotificationV9v0Group": tmnxLogNotificationV9v0Group,
       "tmnxLogEventDampedV8v0Group": tmnxLogEventDampedV8v0Group,
       "tmnxLogApV9v0Group": tmnxLogApV9v0Group,
       "tmnxLogExRbkOpGroup": tmnxLogExRbkOpGroup,
       "tmnxLogNotifyObjsV10v0Group": tmnxLogNotifyObjsV10v0Group,
       "tmnxLogApExtGroup": tmnxLogApExtGroup,
       "tmnxLogAppRouteNotifV10v0Group": tmnxLogAppRouteNotifV10v0Group,
       "tmnxLogApV11v0Group": tmnxLogApV11v0Group,
       "tmnxLogEventsV11v0Group": tmnxLogEventsV11v0Group,
       "tmnxLogApCrV11v0Group": tmnxLogApCrV11v0Group,
       "tmnxLogFilterMsgV13v0Group": tmnxLogFilterMsgV13v0Group,
       "tmnxLogNotifyObjsV13v0Group": tmnxLogNotifyObjsV13v0Group,
       "tmnxLogEHSV13v0Group": tmnxLogEHSV13v0Group,
       "tmnxLogNotifyObjsV14v0Group": tmnxLogNotifyObjsV14v0Group,
       "tmnxLogEHSV14v0Group": tmnxLogEHSV14v0Group,
       "tmnxLogPythonGroup": tmnxLogPythonGroup,
       "tmnxLogToSessionGroup": tmnxLogToSessionGroup,
       "tmnxLogObsoleteObjsV15v0Group": tmnxLogObsoleteObjsV15v0Group,
       "tmnxLogToNetconfGroup": tmnxLogToNetconfGroup,
       "tmnxLogEventsV16v0Group": tmnxLogEventsV16v0Group,
       "tmnxLogCliSubscrGroup": tmnxLogCliSubscrGroup,
       "tmnxLogAcctPolicyCrV19v0Group": tmnxLogAcctPolicyCrV19v0Group,
       "tmnxLogApV19v0Group": tmnxLogApV19v0Group,
       "tmnxLogNameGroup": tmnxLogNameGroup,
       "tmnxLogFilterNameGroup": tmnxLogFilterNameGroup,
       "tmnxLogSnmpTrapGroupNameGroup": tmnxLogSnmpTrapGroupNameGroup,
       "tmnxLogFilterParamsNameGroup": tmnxLogFilterParamsNameGroup,
       "tmnxSyslogTargetNameGroup": tmnxSyslogTargetNameGroup,
       "tmnxSyslogTlsClntProfilNameGroup": tmnxSyslogTlsClntProfilNameGroup,
       "tmnxLogApObsoleteObjsV21v0Group": tmnxLogApObsoleteObjsV21v0Group,
       "tmnxLogFileNameGroup": tmnxLogFileNameGroup,
       "tmnxSnmpTrapDestV22v0Group": tmnxSnmpTrapDestV22v0Group,
       "tmnxLogObjs": tmnxLogObjs,
       "tmnxLogNotificationObjects": tmnxLogNotificationObjects,
       "tmnxLogFileDeletedLogId": tmnxLogFileDeletedLogId,
       "tmnxLogFileDeletedFileId": tmnxLogFileDeletedFileId,
       "tmnxLogFileDeletedLogType": tmnxLogFileDeletedLogType,
       "tmnxLogFileDeletedLocation": tmnxLogFileDeletedLocation,
       "tmnxLogFileDeletedName": tmnxLogFileDeletedName,
       "tmnxLogFileDeletedCreateTime": tmnxLogFileDeletedCreateTime,
       "tmnxLogTraceErrorTitle": tmnxLogTraceErrorTitle,
       "tmnxLogTraceErrorSubject": tmnxLogTraceErrorSubject,
       "tmnxLogTraceErrorMessage": tmnxLogTraceErrorMessage,
       "tmnxLogThrottledEventID": tmnxLogThrottledEventID,
       "tmnxLogThrottledEvents": tmnxLogThrottledEvents,
       "tmnxSysLogTargetId": tmnxSysLogTargetId,
       "tmnxSysLogTargetProblemDescr": tmnxSysLogTargetProblemDescr,
       "tmnxLogNotifyApInterval": tmnxLogNotifyApInterval,
       "tmnxStdReplayStartEvent": tmnxStdReplayStartEvent,
       "tmnxStdReplayEndEvent": tmnxStdReplayEndEvent,
       "tmnxEhsHEntryMinDelayInterval": tmnxEhsHEntryMinDelayInterval,
       "tmnxLogMaxLogs": tmnxLogMaxLogs,
       "tmnxLogFileIdTable": tmnxLogFileIdTable,
       "tmnxLogFileIdEntry": tmnxLogFileIdEntry,
       "tmnxLogFileId": tmnxLogFileId,
       "tmnxLogFileIdRowStatus": tmnxLogFileIdRowStatus,
       "tmnxLogFileIdStorageType": tmnxLogFileIdStorageType,
       "tmnxLogFileIdRolloverTime": tmnxLogFileIdRolloverTime,
       "tmnxLogFileIdRetainTime": tmnxLogFileIdRetainTime,
       "tmnxLogFileIdAdminLocation": tmnxLogFileIdAdminLocation,
       "tmnxLogFileIdOperLocation": tmnxLogFileIdOperLocation,
       "tmnxLogFileIdDescription": tmnxLogFileIdDescription,
       "tmnxLogFileIdLogType": tmnxLogFileIdLogType,
       "tmnxLogFileIdLogId": tmnxLogFileIdLogId,
       "tmnxLogFileIdPathName": tmnxLogFileIdPathName,
       "tmnxLogFileIdCreateTime": tmnxLogFileIdCreateTime,
       "tmnxLogFileIdBackupLoc": tmnxLogFileIdBackupLoc,
       "tmnxLogFileIdName": tmnxLogFileIdName,
       "tmnxLogApTable": tmnxLogApTable,
       "tmnxLogApEntry": tmnxLogApEntry,
       "tmnxLogApPolicyId": tmnxLogApPolicyId,
       "tmnxLogApRowStatus": tmnxLogApRowStatus,
       "tmnxLogApStorageType": tmnxLogApStorageType,
       "tmnxLogApAdminStatus": tmnxLogApAdminStatus,
       "tmnxLogApOperStatus": tmnxLogApOperStatus,
       "tmnxLogApInterval": tmnxLogApInterval,
       "tmnxLogApDescription": tmnxLogApDescription,
       "tmnxLogApDefault": tmnxLogApDefault,
       "tmnxLogApRecord": tmnxLogApRecord,
       "tmnxLogApToFileId": tmnxLogApToFileId,
       "tmnxLogApPortType": tmnxLogApPortType,
       "tmnxLogApDefaultInterval": tmnxLogApDefaultInterval,
       "tmnxLogApDataLossCount": tmnxLogApDataLossCount,
       "tmnxLogApLastDataLossTimeStamp": tmnxLogApLastDataLossTimeStamp,
       "tmnxLogApToFileType": tmnxLogApToFileType,
       "tmnxLogApIncludeSystemInfo": tmnxLogApIncludeSystemInfo,
       "tmnxLogApAlign": tmnxLogApAlign,
       "tmnxLogIdTable": tmnxLogIdTable,
       "tmnxLogIdEntry": tmnxLogIdEntry,
       "tmnxLogIdIndex": tmnxLogIdIndex,
       "tmnxLogIdRowStatus": tmnxLogIdRowStatus,
       "tmnxLogIdStorageType": tmnxLogIdStorageType,
       "tmnxLogIdAdminStatus": tmnxLogIdAdminStatus,
       "tmnxLogIdOperStatus": tmnxLogIdOperStatus,
       "tmnxLogIdDescription": tmnxLogIdDescription,
       "tmnxLogIdFilterId": tmnxLogIdFilterId,
       "tmnxLogIdSource": tmnxLogIdSource,
       "tmnxLogIdDestination": tmnxLogIdDestination,
       "tmnxLogIdFileId": tmnxLogIdFileId,
       "tmnxLogIdSyslogId": tmnxLogIdSyslogId,
       "tmnxLogIdMaxMemorySize": tmnxLogIdMaxMemorySize,
       "tmnxLogIdConsoleSession": tmnxLogIdConsoleSession,
       "tmnxLogIdForwarded": tmnxLogIdForwarded,
       "tmnxLogIdDropped": tmnxLogIdDropped,
       "tmnxLogIdTimeFormat": tmnxLogIdTimeFormat,
       "tmnxLogIdPythonPolicy": tmnxLogIdPythonPolicy,
       "tmnxLogIdOperDestination": tmnxLogIdOperDestination,
       "tmnxLogIdNetconfStream": tmnxLogIdNetconfStream,
       "tmnxLogIdName": tmnxLogIdName,
       "tmnxLogFilterTable": tmnxLogFilterTable,
       "tmnxLogFilterEntry": tmnxLogFilterEntry,
       "tmnxLogFilterId": tmnxLogFilterId,
       "tmnxLogFilterRowStatus": tmnxLogFilterRowStatus,
       "tmnxLogFilterDescription": tmnxLogFilterDescription,
       "tmnxLogFilterDefaultAction": tmnxLogFilterDefaultAction,
       "tmnxLogFilterInUse": tmnxLogFilterInUse,
       "tmnxLogFilterName": tmnxLogFilterName,
       "tmnxLogFilterParamsTable": tmnxLogFilterParamsTable,
       "tmnxLogFilterParamsEntry": tmnxLogFilterParamsEntry,
       "tmnxLogFilterParamsIndex": tmnxLogFilterParamsIndex,
       "tmnxLogFilterParamsRowStatus": tmnxLogFilterParamsRowStatus,
       "tmnxLogFilterParamsDescription": tmnxLogFilterParamsDescription,
       "tmnxLogFilterParamsAction": tmnxLogFilterParamsAction,
       "tmnxLogFilterParamsApplication": tmnxLogFilterParamsApplication,
       "tmnxLogFilterParamsApplOperator": tmnxLogFilterParamsApplOperator,
       "tmnxLogFilterParamsNumber": tmnxLogFilterParamsNumber,
       "tmnxLogFilterParamsNumberOperator": tmnxLogFilterParamsNumberOperator,
       "tmnxLogFilterParamsSeverity": tmnxLogFilterParamsSeverity,
       "tmnxLogFilterParamsSeverityOperator": tmnxLogFilterParamsSeverityOperator,
       "tmnxLogFilterParamsSubject": tmnxLogFilterParamsSubject,
       "tmnxLogFilterParamsSubjectOperator": tmnxLogFilterParamsSubjectOperator,
       "tmnxLogFilterParamsSubjectRegexp": tmnxLogFilterParamsSubjectRegexp,
       "tmnxLogFilterParamsRouter": tmnxLogFilterParamsRouter,
       "tmnxLogFilterParamsRouterOperator": tmnxLogFilterParamsRouterOperator,
       "tmnxLogFilterParamsRouterRegexp": tmnxLogFilterParamsRouterRegexp,
       "tmnxLogFilterParamsMsg": tmnxLogFilterParamsMsg,
       "tmnxLogFilterParamsMsgOperator": tmnxLogFilterParamsMsgOperator,
       "tmnxLogFilterParamsMsgRegexp": tmnxLogFilterParamsMsgRegexp,
       "tmnxLogFilterParamsName": tmnxLogFilterParamsName,
       "tmnxSyslogTargetTable": tmnxSyslogTargetTable,
       "tmnxSyslogTargetEntry": tmnxSyslogTargetEntry,
       "tmnxSyslogTargetIndex": tmnxSyslogTargetIndex,
       "tmnxSyslogTargetRowStatus": tmnxSyslogTargetRowStatus,
       "tmnxSyslogTargetDescription": tmnxSyslogTargetDescription,
       "tmnxSyslogTargetAddress": tmnxSyslogTargetAddress,
       "tmnxSyslogTargetUdpPort": tmnxSyslogTargetUdpPort,
       "tmnxSyslogTargetFacility": tmnxSyslogTargetFacility,
       "tmnxSyslogTargetSeverity": tmnxSyslogTargetSeverity,
       "tmnxSyslogTargetMessagePrefix": tmnxSyslogTargetMessagePrefix,
       "tmnxSyslogTargetMessagesDropped": tmnxSyslogTargetMessagesDropped,
       "tmnxSyslogTargetAddrType": tmnxSyslogTargetAddrType,
       "tmnxSyslogTargetAddr": tmnxSyslogTargetAddr,
       "tmnxSyslogTargetName": tmnxSyslogTargetName,
       "tmnxSyslogTlsClntProfileName": tmnxSyslogTlsClntProfileName,
       "tmnxEventAppTable": tmnxEventAppTable,
       "tmnxEventAppEntry": tmnxEventAppEntry,
       "tmnxEventAppIndex": tmnxEventAppIndex,
       "tmnxEventAppName": tmnxEventAppName,
       "tmnxEventTable": tmnxEventTable,
       "tmnxEventEntry": tmnxEventEntry,
       "tmnxEventID": tmnxEventID,
       "tmnxEventName": tmnxEventName,
       "tmnxEventSeverity": tmnxEventSeverity,
       "tmnxEventControl": tmnxEventControl,
       "tmnxEventCounter": tmnxEventCounter,
       "tmnxEventDropCount": tmnxEventDropCount,
       "tmnxEventReset": tmnxEventReset,
       "tmnxEventThrottle": tmnxEventThrottle,
       "tmnxEventSpecThrottle": tmnxEventSpecThrottle,
       "tmnxEventSpecThrottleLimit": tmnxEventSpecThrottleLimit,
       "tmnxEventSpecThrottleIntval": tmnxEventSpecThrottleIntval,
       "tmnxEventSpecThrottleDef": tmnxEventSpecThrottleDef,
       "tmnxEventSpecThrottleLimitDef": tmnxEventSpecThrottleLimitDef,
       "tmnxEventSpecThrottleIntvalDef": tmnxEventSpecThrottleIntvalDef,
       "tmnxEventRepeat": tmnxEventRepeat,
       "tmnxSnmpTrapGroupTable": tmnxSnmpTrapGroupTable,
       "tmnxSnmpTrapGroupEntry": tmnxSnmpTrapGroupEntry,
       "tmnxStgIndex": tmnxStgIndex,
       "tmnxStgDestAddress": tmnxStgDestAddress,
       "tmnxStgDestPort": tmnxStgDestPort,
       "tmnxStgRowStatus": tmnxStgRowStatus,
       "tmnxStgDescription": tmnxStgDescription,
       "tmnxStgVersion": tmnxStgVersion,
       "tmnxStgNotifyCommunity": tmnxStgNotifyCommunity,
       "tmnxStgSecurityLevel": tmnxStgSecurityLevel,
       "tmnxEventTest": tmnxEventTest,
       "tmnxEventThrottleLimit": tmnxEventThrottleLimit,
       "tmnxEventThrottleInterval": tmnxEventThrottleInterval,
       "tmnxSnmpSetErrsMax": tmnxSnmpSetErrsMax,
       "tmnxSnmpSetErrsTable": tmnxSnmpSetErrsTable,
       "tmnxSnmpSetErrsEntry": tmnxSnmpSetErrsEntry,
       "tmnxSseAddressType": tmnxSseAddressType,
       "tmnxSseAddress": tmnxSseAddress,
       "tmnxSseSnmpPort": tmnxSseSnmpPort,
       "tmnxSseRequestId": tmnxSseRequestId,
       "tmnxSseVersion": tmnxSseVersion,
       "tmnxSseSeverityLevel": tmnxSseSeverityLevel,
       "tmnxSseModuleId": tmnxSseModuleId,
       "tmnxSseModuleName": tmnxSseModuleName,
       "tmnxSseErrorCode": tmnxSseErrorCode,
       "tmnxSseErrorName": tmnxSseErrorName,
       "tmnxSseErrorMsg": tmnxSseErrorMsg,
       "tmnxSseExtraText": tmnxSseExtraText,
       "tmnxSseTimestamp": tmnxSseTimestamp,
       "tmnxSnmpTrapLogTable": tmnxSnmpTrapLogTable,
       "tmnxSnmpTrapLogEntry": tmnxSnmpTrapLogEntry,
       "tmnxSnmpTrapLogDescription": tmnxSnmpTrapLogDescription,
       "snmpNotifyId": snmpNotifyId,
       "tmnxSnmpTrapDestTable": tmnxSnmpTrapDestTable,
       "tmnxSnmpTrapDestEntry": tmnxSnmpTrapDestEntry,
       "tmnxStdIndex": tmnxStdIndex,
       "tmnxStdName": tmnxStdName,
       "tmnxStdRowStatus": tmnxStdRowStatus,
       "tmnxStdRowLastChanged": tmnxStdRowLastChanged,
       "tmnxStdDestAddrType": tmnxStdDestAddrType,
       "tmnxStdDestAddr": tmnxStdDestAddr,
       "tmnxStdDestPort": tmnxStdDestPort,
       "tmnxStdDescription": tmnxStdDescription,
       "tmnxStdVersion": tmnxStdVersion,
       "tmnxStdNotifyCommunity": tmnxStdNotifyCommunity,
       "tmnxStdSecurityLevel": tmnxStdSecurityLevel,
       "tmnxStdReplay": tmnxStdReplay,
       "tmnxStdReplayStart": tmnxStdReplayStart,
       "tmnxStdReplayLastTime": tmnxStdReplayLastTime,
       "tmnxStdDyingGasp": tmnxStdDyingGasp,
       "tmnxStdMaxTargets": tmnxStdMaxTargets,
       "tmnxLogApCustRecordTable": tmnxLogApCustRecordTable,
       "tmnxLogApCustRecordEntry": tmnxLogApCustRecordEntry,
       "tmnxLogApCrLastChanged": tmnxLogApCrLastChanged,
       "tmnxLogApCrSignChangeDelta": tmnxLogApCrSignChangeDelta,
       "tmnxLogApCrSignChangeQueue": tmnxLogApCrSignChangeQueue,
       "tmnxLogApCrSignChangeOCntr": tmnxLogApCrSignChangeOCntr,
       "tmnxLogApCrSignChangeQICounters": tmnxLogApCrSignChangeQICounters,
       "tmnxLogApCrSignChangeQECounters": tmnxLogApCrSignChangeQECounters,
       "tmnxLogApCrSignChangeOICounters": tmnxLogApCrSignChangeOICounters,
       "tmnxLogApCrSignChangeOECounters": tmnxLogApCrSignChangeOECounters,
       "tmnxLogApCrSignChangeAACounters": tmnxLogApCrSignChangeAACounters,
       "tmnxLogApCrAACounters": tmnxLogApCrAACounters,
       "tmnxLogApCrAASubAttributes": tmnxLogApCrAASubAttributes,
       "tmnxLogApCrSignChangePolicer": tmnxLogApCrSignChangePolicer,
       "tmnxLogApCrSignChangePICounters": tmnxLogApCrSignChangePICounters,
       "tmnxLogApCrSignChangePECounters": tmnxLogApCrSignChangePECounters,
       "tmnxLogApCustRecordQueueTable": tmnxLogApCustRecordQueueTable,
       "tmnxLogApCustRecordQueueEntry": tmnxLogApCustRecordQueueEntry,
       "tmnxLogApCrQueueId": tmnxLogApCrQueueId,
       "tmnxLogApCrQueueRowStatus": tmnxLogApCrQueueRowStatus,
       "tmnxLogApCrQueueLastChanged": tmnxLogApCrQueueLastChanged,
       "tmnxLogApCrQueueICounters": tmnxLogApCrQueueICounters,
       "tmnxLogApCrQueueECounters": tmnxLogApCrQueueECounters,
       "tmnxLogApCrOverrideCntrTable": tmnxLogApCrOverrideCntrTable,
       "tmnxLogApCrOverrideCntrEntry": tmnxLogApCrOverrideCntrEntry,
       "tmnxLogApCrOverrideCntrId": tmnxLogApCrOverrideCntrId,
       "tmnxLogApCrOverrideCntrRowStatus": tmnxLogApCrOverrideCntrRowStatus,
       "tmnxLogApCrOverrideCntrLastChngd": tmnxLogApCrOverrideCntrLastChngd,
       "tmnxLogApCrOverrideCntrICounters": tmnxLogApCrOverrideCntrICounters,
       "tmnxLogApCrOverrideCntrECounters": tmnxLogApCrOverrideCntrECounters,
       "tmnxEventPrimaryRoutePref": tmnxEventPrimaryRoutePref,
       "tmnxEventSecondaryRoutePref": tmnxEventSecondaryRoutePref,
       "tmnxLogConfigEventsDamped": tmnxLogConfigEventsDamped,
       "tmnxLogEventHistoryObjs": tmnxLogEventHistoryObjs,
       "tmnxLogEventHistGeneralObjs": tmnxLogEventHistGeneralObjs,
       "tmnxLogExRbkOpTblLastChange": tmnxLogExRbkOpTblLastChange,
       "tmnxLogExRbkOpMaxEntries": tmnxLogExRbkOpMaxEntries,
       "tmnxLogExecRollbackOpTable": tmnxLogExecRollbackOpTable,
       "tmnxLogExecRollbackOpEntry": tmnxLogExecRollbackOpEntry,
       "tmnxLogExRbkOpIndex": tmnxLogExRbkOpIndex,
       "tmnxLogExRbkOpLastChanged": tmnxLogExRbkOpLastChanged,
       "tmnxLogExRbkOpType": tmnxLogExRbkOpType,
       "tmnxLogExRbkOpStatus": tmnxLogExRbkOpStatus,
       "tmnxLogExRbkOpBegin": tmnxLogExRbkOpBegin,
       "tmnxLogExRbkOpEnd": tmnxLogExRbkOpEnd,
       "tmnxLogExRbkOpFile": tmnxLogExRbkOpFile,
       "tmnxLogExRbkOpUser": tmnxLogExRbkOpUser,
       "tmnxLogExRbkOpNumEvents": tmnxLogExRbkOpNumEvents,
       "tmnxLogExecRollbackEventTable": tmnxLogExecRollbackEventTable,
       "tmnxLogExecRollbackEventEntry": tmnxLogExecRollbackEventEntry,
       "tmnxLogExRbkEventIndex": tmnxLogExRbkEventIndex,
       "tmnxLogExRbkEventOID": tmnxLogExRbkEventOID,
       "tmnxLogExRbkNotifyObjects": tmnxLogExRbkNotifyObjects,
       "tmnxLogExecRollbackOpIndex": tmnxLogExecRollbackOpIndex,
       "tmnxLogExecRollbackOpType": tmnxLogExecRollbackOpType,
       "tmnxLogColdStartWaitTime": tmnxLogColdStartWaitTime,
       "tmnxLogRouteRecoveryWaitTime": tmnxLogRouteRecoveryWaitTime,
       "tmnxEhsObjs": tmnxEhsObjs,
       "tmnxEhsGeneralObjs": tmnxEhsGeneralObjs,
       "tmnxEhsHandlerTblLastChange": tmnxEhsHandlerTblLastChange,
       "tmnxEhsHandlerMaxEntries": tmnxEhsHandlerMaxEntries,
       "tmnxEhsHEntryTblLastChange": tmnxEhsHEntryTblLastChange,
       "tmnxEhsHEntryMaxEntries": tmnxEhsHEntryMaxEntries,
       "tmnxEhsTriggerTblLastChange": tmnxEhsTriggerTblLastChange,
       "tmnxEhsTriggerMaxEntries": tmnxEhsTriggerMaxEntries,
       "tmnxEhsTEntryTblLastChange": tmnxEhsTEntryTblLastChange,
       "tmnxEhsTEntryMaxEntries": tmnxEhsTEntryMaxEntries,
       "tmnxEhsHandlerTable": tmnxEhsHandlerTable,
       "tmnxEhsHandlerEntry": tmnxEhsHandlerEntry,
       "tmnxEhsHandlerName": tmnxEhsHandlerName,
       "tmnxEhsHandlerRowStatus": tmnxEhsHandlerRowStatus,
       "tmnxEhsHandlerDescription": tmnxEhsHandlerDescription,
       "tmnxEhsHandlerLastChange": tmnxEhsHandlerLastChange,
       "tmnxEhsHandlerAdminStatus": tmnxEhsHandlerAdminStatus,
       "tmnxEhsHandlerOperStatus": tmnxEhsHandlerOperStatus,
       "tmnxEhsHandlerStatsTable": tmnxEhsHandlerStatsTable,
       "tmnxEhsHandlerStatsEntry": tmnxEhsHandlerStatsEntry,
       "tmnxEhsHandlerStatsSuccess": tmnxEhsHandlerStatsSuccess,
       "tmnxEhsHandlerStatsErrNoEntry": tmnxEhsHandlerStatsErrNoEntry,
       "tmnxEhsHandlerStatsErrAdmStatus": tmnxEhsHandlerStatsErrAdmStatus,
       "tmnxEhsHEntryTable": tmnxEhsHEntryTable,
       "tmnxEhsHEntryEntry": tmnxEhsHEntryEntry,
       "tmnxEhsHEntryId": tmnxEhsHEntryId,
       "tmnxEhsHEntryRowStatus": tmnxEhsHEntryRowStatus,
       "tmnxEhsHEntryDescription": tmnxEhsHEntryDescription,
       "tmnxEhsHEntryLastChange": tmnxEhsHEntryLastChange,
       "tmnxEhsHEntryAdminStatus": tmnxEhsHEntryAdminStatus,
       "tmnxEhsHEntryOperStatus": tmnxEhsHEntryOperStatus,
       "tmnxEhsHEntryScriptPlcyName": tmnxEhsHEntryScriptPlcyName,
       "tmnxEhsHEntryScriptPlcyOwner": tmnxEhsHEntryScriptPlcyOwner,
       "tmnxEhsHEntryMinDelay": tmnxEhsHEntryMinDelay,
       "tmnxEhsHEntryLastExecuted": tmnxEhsHEntryLastExecuted,
       "tmnxEhsHEntryStatsTable": tmnxEhsHEntryStatsTable,
       "tmnxEhsHEntryStatsEntry": tmnxEhsHEntryStatsEntry,
       "tmnxEhsHEntryStatsLaunchSuccess": tmnxEhsHEntryStatsLaunchSuccess,
       "tmnxEhsHEntryStatsErrMinDelay": tmnxEhsHEntryStatsErrMinDelay,
       "tmnxEhsHEntryStatsErrLaunch": tmnxEhsHEntryStatsErrLaunch,
       "tmnxEhsHEntryStatsErrAdmStatus": tmnxEhsHEntryStatsErrAdmStatus,
       "tmnxEhsTriggerTable": tmnxEhsTriggerTable,
       "tmnxEhsTriggerEntry": tmnxEhsTriggerEntry,
       "tmnxEhsTriggerRowStatus": tmnxEhsTriggerRowStatus,
       "tmnxEhsTriggerDescription": tmnxEhsTriggerDescription,
       "tmnxEhsTriggerLastChange": tmnxEhsTriggerLastChange,
       "tmnxEhsTriggerAdminStatus": tmnxEhsTriggerAdminStatus,
       "tmnxEhsTriggerOperStatus": tmnxEhsTriggerOperStatus,
       "tmnxEhsTriggerStatsTable": tmnxEhsTriggerStatsTable,
       "tmnxEhsTriggerStatsEntry": tmnxEhsTriggerStatsEntry,
       "tmnxEhsTriggerStatsSuccess": tmnxEhsTriggerStatsSuccess,
       "tmnxEhsTriggerStatsErrNoEntry": tmnxEhsTriggerStatsErrNoEntry,
       "tmnxEhsTriggerStatsErrAdmStatus": tmnxEhsTriggerStatsErrAdmStatus,
       "tmnxEhsTEntryTable": tmnxEhsTEntryTable,
       "tmnxEhsTEntryEntry": tmnxEhsTEntryEntry,
       "tmnxEhsTEntryId": tmnxEhsTEntryId,
       "tmnxEhsTEntryRowStatus": tmnxEhsTEntryRowStatus,
       "tmnxEhsTEntryDescription": tmnxEhsTEntryDescription,
       "tmnxEhsTEntryLastChange": tmnxEhsTEntryLastChange,
       "tmnxEhsTEntryAdminStatus": tmnxEhsTEntryAdminStatus,
       "tmnxEhsTEntryOperStatus": tmnxEhsTEntryOperStatus,
       "tmnxEhsTEntryLogFilterId": tmnxEhsTEntryLogFilterId,
       "tmnxEhsTEntryHandlerName": tmnxEhsTEntryHandlerName,
       "tmnxEhsTEntryDebounceVal": tmnxEhsTEntryDebounceVal,
       "tmnxEhsTEntryDebounceTime": tmnxEhsTEntryDebounceTime,
       "tmnxEhsTEntryStatsTable": tmnxEhsTEntryStatsTable,
       "tmnxEhsTEntryStatsEntry": tmnxEhsTEntryStatsEntry,
       "tmnxEhsTEntryStatsFilterMatch": tmnxEhsTEntryStatsFilterMatch,
       "tmnxEhsTEntryStatsFilterFail": tmnxEhsTEntryStatsFilterFail,
       "tmnxEhsTEntryStatsErrAdminStatus": tmnxEhsTEntryStatsErrAdminStatus,
       "tmnxEhsTEntryStatsErrFilter": tmnxEhsTEntryStatsErrFilter,
       "tmnxEhsTEntryStatsErrHandler": tmnxEhsTEntryStatsErrHandler,
       "tmnxEhsTEntryStatsTriggerCount": tmnxEhsTEntryStatsTriggerCount,
       "tmnxEhsTEntryStatsDebounce": tmnxEhsTEntryStatsDebounce,
       "tmnxLogCliSubscrTable": tmnxLogCliSubscrTable,
       "tmnxLogCliSubscrEntry": tmnxLogCliSubscrEntry,
       "tmnxLogCliSubscrSession": tmnxLogCliSubscrSession,
       "tmnxLogCliSubscrLog": tmnxLogCliSubscrLog,
       "tmnxLogCliSubscrType": tmnxLogCliSubscrType,
       "tmnxLogCliSubscrUser": tmnxLogCliSubscrUser,
       "tmnxLogCliSubscrUserLoginTime": tmnxLogCliSubscrUserLoginTime,
       "tmnxLogCliSubscrUserIpAddrType": tmnxLogCliSubscrUserIpAddrType,
       "tmnxLogCliSubscrUserIpAddr": tmnxLogCliSubscrUserIpAddr,
       "tmnxLogApCustRecordPolicerTable": tmnxLogApCustRecordPolicerTable,
       "tmnxLogApCustRecordPolicerEntry": tmnxLogApCustRecordPolicerEntry,
       "tmnxLogApCrPolicerId": tmnxLogApCrPolicerId,
       "tmnxLogApCrPolicerLastChanged": tmnxLogApCrPolicerLastChanged,
       "tmnxLogApCrPolicerRowStatus": tmnxLogApCrPolicerRowStatus,
       "tmnxLogApCrPolicerICounters": tmnxLogApCrPolicerICounters,
       "tmnxLogApCrPolicerECounters": tmnxLogApCrPolicerECounters,
       "tmnxLogNotifyPrefix": tmnxLogNotifyPrefix,
       "tmnxLogNotifications": tmnxLogNotifications,
       "tmnxLogSpaceContention": tmnxLogSpaceContention,
       "tmnxLogAdminLocFailed": tmnxLogAdminLocFailed,
       "tmnxLogBackupLocFailed": tmnxLogBackupLocFailed,
       "tmnxLogFileRollover": tmnxLogFileRollover,
       "tmnxLogFileDeleted": tmnxLogFileDeleted,
       "tmnxTestEvent": tmnxTestEvent,
       "tmnxLogTraceError": tmnxLogTraceError,
       "tmnxLogEventThrottled": tmnxLogEventThrottled,
       "tmnxSysLogTargetProblem": tmnxSysLogTargetProblem,
       "tmnxLogAccountingDataLoss": tmnxLogAccountingDataLoss,
       "tmnxStdEventsReplayed": tmnxStdEventsReplayed,
       "tmnxLogEventOverrun": tmnxLogEventOverrun}
)
