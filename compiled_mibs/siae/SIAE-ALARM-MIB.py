# SNMP MIB module (SIAE-ALARM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\siae\SIAE-ALARM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:26:34 2025
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

(siaeMib,
 siaeMicroelettronicaSpa) = mibBuilder.importSymbols(
    "SIAE-TREE-MIB",
    "siaeMib",
    "siaeMicroelettronicaSpa")

(accessControlLoginIpAddress,) = mibBuilder.importSymbols(
    "SIAE-USER-MIB",
    "accessControlLoginIpAddress")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

smalarm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 4)
)
if mibBuilder.loadTexts:
    smalarm.setRevisions(
        ("2016-10-04 00:00",
         "2015-07-17 00:00",
         "2015-03-23 00:00",
         "2015-03-16 00:00",
         "2014-06-23 00:00",
         "2014-03-03 00:00",
         "2014-02-03 00:00",
         "2013-04-16 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AlarmStatus(TextualConvention, Integer32):
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
        *(("cleared", 1),
          ("activeReportableStatus", 2),
          ("activeReportableWarning", 3),
          ("activeReportableMinor", 4),
          ("activeReportableMajor", 5),
          ("activeReportableCritical", 6))
    )



class AlarmSeverityCode(TextualConvention, Integer32):
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
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("statusTrapEnable", 2),
          ("warningTrapEnable", 3),
          ("minorTrapEnable", 4),
          ("majorTrapEnable", 5),
          ("criticalTrapEnable", 6),
          ("statusTrapDisable", 18),
          ("warningTrapDisable", 19),
          ("minorTrapDisable", 20),
          ("majorTrapDisable", 21),
          ("criticalTrapDisable", 22))
    )



# MIB Managed Objects in the order of their OIDs

_AlarmTrap_ObjectIdentity = ObjectIdentity
alarmTrap = _AlarmTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 0)
)


class _AlarmMibVersion_Type(Integer32):
    """Custom type alarmMibVersion based on Integer32"""
    defaultValue = 1


_AlarmMibVersion_Type.__name__ = "Integer32"
_AlarmMibVersion_Object = MibScalar
alarmMibVersion = _AlarmMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 4, 1),
    _AlarmMibVersion_Type()
)
alarmMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmMibVersion.setStatus("current")
_SiaeNotificationEntry_ObjectIdentity = ObjectIdentity
siaeNotificationEntry = _SiaeNotificationEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 4, 2)
)
_AlarmObjectId_Type = ObjectIdentifier
_AlarmObjectId_Object = MibScalar
alarmObjectId = _AlarmObjectId_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 4, 2, 1),
    _AlarmObjectId_Type()
)
alarmObjectId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmObjectId.setStatus("current")
_AlarmObjectVal_Type = AlarmStatus
_AlarmObjectVal_Object = MibScalar
alarmObjectVal = _AlarmObjectVal_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 4, 2, 2),
    _AlarmObjectVal_Type()
)
alarmObjectVal.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmObjectVal.setStatus("current")


class _AlarmTrapDescription_Type(OctetString):
    """Custom type alarmTrapDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_AlarmTrapDescription_Type.__name__ = "OctetString"
_AlarmTrapDescription_Object = MibScalar
alarmTrapDescription = _AlarmTrapDescription_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 4, 2, 3),
    _AlarmTrapDescription_Type()
)
alarmTrapDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmTrapDescription.setStatus("current")
_AlarmTrapNumber_Type = Unsigned32
_AlarmTrapNumber_Object = MibScalar
alarmTrapNumber = _AlarmTrapNumber_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 4, 2, 4),
    _AlarmTrapNumber_Type()
)
alarmTrapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmTrapNumber.setStatus("current")
_AlarmIpSnmpAgentAddress_Type = IpAddress
_AlarmIpSnmpAgentAddress_Object = MibScalar
alarmIpSnmpAgentAddress = _AlarmIpSnmpAgentAddress_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 4, 2, 5),
    _AlarmIpSnmpAgentAddress_Type()
)
alarmIpSnmpAgentAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmIpSnmpAgentAddress.setStatus("current")
_AlarmLogTable_Object = MibTable
alarmLogTable = _AlarmLogTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 4, 3)
)
if mibBuilder.loadTexts:
    alarmLogTable.setStatus("current")
_AlarmLogRecord_Object = MibTableRow
alarmLogRecord = _AlarmLogRecord_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 4, 3, 1)
)
alarmLogRecord.setIndexNames(
    (0, "SIAE-ALARM-MIB", "alarmLogRecordId"),
)
if mibBuilder.loadTexts:
    alarmLogRecord.setStatus("current")
_AlarmLogRecordId_Type = Integer32
_AlarmLogRecordId_Object = MibTableColumn
alarmLogRecordId = _AlarmLogRecordId_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 4, 3, 1, 1),
    _AlarmLogRecordId_Type()
)
alarmLogRecordId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLogRecordId.setStatus("current")
_AlarmLogObjectId_Type = ObjectIdentifier
_AlarmLogObjectId_Object = MibTableColumn
alarmLogObjectId = _AlarmLogObjectId_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 4, 3, 1, 2),
    _AlarmLogObjectId_Type()
)
alarmLogObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLogObjectId.setStatus("current")
_AlarmLogObjectVal_Type = AlarmStatus
_AlarmLogObjectVal_Object = MibTableColumn
alarmLogObjectVal = _AlarmLogObjectVal_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 4, 3, 1, 3),
    _AlarmLogObjectVal_Type()
)
alarmLogObjectVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLogObjectVal.setStatus("current")
_AlarmLogObjectSev_Type = AlarmSeverityCode
_AlarmLogObjectSev_Object = MibTableColumn
alarmLogObjectSev = _AlarmLogObjectSev_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 4, 3, 1, 4),
    _AlarmLogObjectSev_Type()
)
alarmLogObjectSev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLogObjectSev.setStatus("current")


class _AlarmLogDescription_Type(DisplayString):
    """Custom type alarmLogDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_AlarmLogDescription_Type.__name__ = "DisplayString"
_AlarmLogDescription_Object = MibTableColumn
alarmLogDescription = _AlarmLogDescription_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 4, 3, 1, 5),
    _AlarmLogDescription_Type()
)
alarmLogDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLogDescription.setStatus("current")
_AlarmLogEventTime_Type = Unsigned32
_AlarmLogEventTime_Object = MibTableColumn
alarmLogEventTime = _AlarmLogEventTime_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 4, 3, 1, 6),
    _AlarmLogEventTime_Type()
)
alarmLogEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLogEventTime.setStatus("current")


class _AlarmLogActionRequest_Type(Integer32):
    """Custom type alarmLogActionRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notActive", 0),
          ("delete", 1),
          ("read", 2))
    )


_AlarmLogActionRequest_Type.__name__ = "Integer32"
_AlarmLogActionRequest_Object = MibScalar
alarmLogActionRequest = _AlarmLogActionRequest_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 4, 4),
    _AlarmLogActionRequest_Type()
)
alarmLogActionRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmLogActionRequest.setStatus("current")


class _AlarmLogFTPfile_Type(DisplayString):
    """Custom type alarmLogFTPfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlarmLogFTPfile_Type.__name__ = "DisplayString"
_AlarmLogFTPfile_Object = MibScalar
alarmLogFTPfile = _AlarmLogFTPfile_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 4, 5),
    _AlarmLogFTPfile_Type()
)
alarmLogFTPfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmLogFTPfile.setStatus("current")


class _AlarmLogAlarmSeverityEnable_Type(Integer32):
    """Custom type alarmLogAlarmSeverityEnable based on Integer32"""
    defaultValue = 31


_AlarmLogAlarmSeverityEnable_Type.__name__ = "Integer32"
_AlarmLogAlarmSeverityEnable_Object = MibScalar
alarmLogAlarmSeverityEnable = _AlarmLogAlarmSeverityEnable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 4, 6),
    _AlarmLogAlarmSeverityEnable_Type()
)
alarmLogAlarmSeverityEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmLogAlarmSeverityEnable.setStatus("current")


class _AlarmLogStartHourEnable_Type(Integer32):
    """Custom type alarmLogStartHourEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_AlarmLogStartHourEnable_Type.__name__ = "Integer32"
_AlarmLogStartHourEnable_Object = MibScalar
alarmLogStartHourEnable = _AlarmLogStartHourEnable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 4, 7),
    _AlarmLogStartHourEnable_Type()
)
alarmLogStartHourEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmLogStartHourEnable.setStatus("current")


class _AlarmLogEndHourEnable_Type(Integer32):
    """Custom type alarmLogEndHourEnable based on Integer32"""
    defaultValue = 23

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_AlarmLogEndHourEnable_Type.__name__ = "Integer32"
_AlarmLogEndHourEnable_Object = MibScalar
alarmLogEndHourEnable = _AlarmLogEndHourEnable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 4, 8),
    _AlarmLogEndHourEnable_Type()
)
alarmLogEndHourEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmLogEndHourEnable.setStatus("current")


class _AlarmLogStartTimeFilter_Type(Unsigned32):
    """Custom type alarmLogStartTimeFilter based on Unsigned32"""
    defaultValue = 0


_AlarmLogStartTimeFilter_Type.__name__ = "Unsigned32"
_AlarmLogStartTimeFilter_Object = MibScalar
alarmLogStartTimeFilter = _AlarmLogStartTimeFilter_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 4, 9),
    _AlarmLogStartTimeFilter_Type()
)
alarmLogStartTimeFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmLogStartTimeFilter.setStatus("current")


class _AlarmLogEndTimeFilter_Type(Unsigned32):
    """Custom type alarmLogEndTimeFilter based on Unsigned32"""
    defaultValue = 0


_AlarmLogEndTimeFilter_Type.__name__ = "Unsigned32"
_AlarmLogEndTimeFilter_Object = MibScalar
alarmLogEndTimeFilter = _AlarmLogEndTimeFilter_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 4, 10),
    _AlarmLogEndTimeFilter_Type()
)
alarmLogEndTimeFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmLogEndTimeFilter.setStatus("current")


class _AlarmLogManagedObjectFilter_Type(ObjectIdentifier):
    """Custom type alarmLogManagedObjectFilter based on ObjectIdentifier"""
    defaultValue = (1, 3, 6, 1, 4, 1, 3373)


_AlarmLogManagedObjectFilter_Type.__name__ = "ObjectIdentifier"
_AlarmLogManagedObjectFilter_Object = MibScalar
alarmLogManagedObjectFilter = _AlarmLogManagedObjectFilter_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 4, 11),
    _AlarmLogManagedObjectFilter_Type()
)
alarmLogManagedObjectFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmLogManagedObjectFilter.setStatus("current")


class _AlarmLogAlarmSeverityFilter_Type(Integer32):
    """Custom type alarmLogAlarmSeverityFilter based on Integer32"""
    defaultValue = 31


_AlarmLogAlarmSeverityFilter_Type.__name__ = "Integer32"
_AlarmLogAlarmSeverityFilter_Object = MibScalar
alarmLogAlarmSeverityFilter = _AlarmLogAlarmSeverityFilter_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 4, 12),
    _AlarmLogAlarmSeverityFilter_Type()
)
alarmLogAlarmSeverityFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmLogAlarmSeverityFilter.setStatus("current")


class _AlarmLogFTPStatus_Type(Integer32):
    """Custom type alarmLogFTPStatus based on Integer32"""
    defaultValue = 2

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
        *(("transferring", 1),
          ("completed", 2),
          ("interrupted", 3),
          ("empty", 4))
    )


_AlarmLogFTPStatus_Type.__name__ = "Integer32"
_AlarmLogFTPStatus_Object = MibScalar
alarmLogFTPStatus = _AlarmLogFTPStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 4, 14),
    _AlarmLogFTPStatus_Type()
)
alarmLogFTPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLogFTPStatus.setStatus("current")


class _AlarmLogFTPStatusTrapNotification_Type(Integer32):
    """Custom type alarmLogFTPStatusTrapNotification based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              34)
        )
    )
    namedValues = NamedValues(
        *(("trapDisable", 1),
          ("trapEnable", 2),
          ("trapEnableWithACK", 34))
    )


_AlarmLogFTPStatusTrapNotification_Type.__name__ = "Integer32"
_AlarmLogFTPStatusTrapNotification_Object = MibScalar
alarmLogFTPStatusTrapNotification = _AlarmLogFTPStatusTrapNotification_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 4, 15),
    _AlarmLogFTPStatusTrapNotification_Type()
)
alarmLogFTPStatusTrapNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmLogFTPStatusTrapNotification.setStatus("current")
_AlarmLogLastEventTime_Type = Unsigned32
_AlarmLogLastEventTime_Object = MibScalar
alarmLogLastEventTime = _AlarmLogLastEventTime_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 4, 16),
    _AlarmLogLastEventTime_Type()
)
alarmLogLastEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLogLastEventTime.setStatus("current")
_AlarmActiveTable_Object = MibTable
alarmActiveTable = _AlarmActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 4, 17)
)
if mibBuilder.loadTexts:
    alarmActiveTable.setStatus("current")
_AlarmActiveRecord_Object = MibTableRow
alarmActiveRecord = _AlarmActiveRecord_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 4, 17, 1)
)
alarmActiveRecord.setIndexNames(
    (0, "SIAE-ALARM-MIB", "alarmActiveObjectId"),
)
if mibBuilder.loadTexts:
    alarmActiveRecord.setStatus("current")
_AlarmActiveObjectId_Type = ObjectIdentifier
_AlarmActiveObjectId_Object = MibTableColumn
alarmActiveObjectId = _AlarmActiveObjectId_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 4, 17, 1, 1),
    _AlarmActiveObjectId_Type()
)
alarmActiveObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmActiveObjectId.setStatus("current")
_AlarmActiveObjectVal_Type = AlarmStatus
_AlarmActiveObjectVal_Object = MibTableColumn
alarmActiveObjectVal = _AlarmActiveObjectVal_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 4, 17, 1, 2),
    _AlarmActiveObjectVal_Type()
)
alarmActiveObjectVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmActiveObjectVal.setStatus("current")


class _AlarmActiveDescription_Type(DisplayString):
    """Custom type alarmActiveDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_AlarmActiveDescription_Type.__name__ = "DisplayString"
_AlarmActiveDescription_Object = MibTableColumn
alarmActiveDescription = _AlarmActiveDescription_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 4, 17, 1, 3),
    _AlarmActiveDescription_Type()
)
alarmActiveDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmActiveDescription.setStatus("current")
_AlarmActiveEventTime_Type = Unsigned32
_AlarmActiveEventTime_Object = MibTableColumn
alarmActiveEventTime = _AlarmActiveEventTime_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 4, 17, 1, 4),
    _AlarmActiveEventTime_Type()
)
alarmActiveEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmActiveEventTime.setStatus("current")


class _AlarmActiveFloodingStatus_Type(Integer32):
    """Custom type alarmActiveFloodingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_AlarmActiveFloodingStatus_Type.__name__ = "Integer32"
_AlarmActiveFloodingStatus_Object = MibTableColumn
alarmActiveFloodingStatus = _AlarmActiveFloodingStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 4, 17, 1, 5),
    _AlarmActiveFloodingStatus_Type()
)
alarmActiveFloodingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmActiveFloodingStatus.setStatus("current")


class _AlarmSyntesysCritical_Type(Integer32):
    """Custom type alarmSyntesysCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("activeReportableCritical", 6))
    )


_AlarmSyntesysCritical_Type.__name__ = "Integer32"
_AlarmSyntesysCritical_Object = MibScalar
alarmSyntesysCritical = _AlarmSyntesysCritical_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 4, 18),
    _AlarmSyntesysCritical_Type()
)
alarmSyntesysCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSyntesysCritical.setStatus("current")


class _AlarmSyntesysCriticalSeverityCode_Type(Integer32):
    """Custom type alarmSyntesysCriticalSeverityCode based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6,
              22)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("criticalTrapEnable", 6),
          ("criticalTrapDisable", 22))
    )


_AlarmSyntesysCriticalSeverityCode_Type.__name__ = "Integer32"
_AlarmSyntesysCriticalSeverityCode_Object = MibScalar
alarmSyntesysCriticalSeverityCode = _AlarmSyntesysCriticalSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 4, 19),
    _AlarmSyntesysCriticalSeverityCode_Type()
)
alarmSyntesysCriticalSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSyntesysCriticalSeverityCode.setStatus("current")


class _AlarmSyntesysMajor_Type(Integer32):
    """Custom type alarmSyntesysMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("activeReportableMajor", 5))
    )


_AlarmSyntesysMajor_Type.__name__ = "Integer32"
_AlarmSyntesysMajor_Object = MibScalar
alarmSyntesysMajor = _AlarmSyntesysMajor_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 4, 20),
    _AlarmSyntesysMajor_Type()
)
alarmSyntesysMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSyntesysMajor.setStatus("current")


class _AlarmSyntesysMajorSeverityCode_Type(Integer32):
    """Custom type alarmSyntesysMajorSeverityCode based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              21)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("majorTrapEnable", 5),
          ("majorTrapDisable", 21))
    )


_AlarmSyntesysMajorSeverityCode_Type.__name__ = "Integer32"
_AlarmSyntesysMajorSeverityCode_Object = MibScalar
alarmSyntesysMajorSeverityCode = _AlarmSyntesysMajorSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 4, 21),
    _AlarmSyntesysMajorSeverityCode_Type()
)
alarmSyntesysMajorSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSyntesysMajorSeverityCode.setStatus("current")


class _AlarmSyntesysMinor_Type(Integer32):
    """Custom type alarmSyntesysMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("activeReportableMinor", 4))
    )


_AlarmSyntesysMinor_Type.__name__ = "Integer32"
_AlarmSyntesysMinor_Object = MibScalar
alarmSyntesysMinor = _AlarmSyntesysMinor_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 4, 22),
    _AlarmSyntesysMinor_Type()
)
alarmSyntesysMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSyntesysMinor.setStatus("current")


class _AlarmSyntesysMinorSeverityCode_Type(Integer32):
    """Custom type alarmSyntesysMinorSeverityCode based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              20)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("minorTrapEnable", 4),
          ("minorTrapDisable", 20))
    )


_AlarmSyntesysMinorSeverityCode_Type.__name__ = "Integer32"
_AlarmSyntesysMinorSeverityCode_Object = MibScalar
alarmSyntesysMinorSeverityCode = _AlarmSyntesysMinorSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 4, 23),
    _AlarmSyntesysMinorSeverityCode_Type()
)
alarmSyntesysMinorSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSyntesysMinorSeverityCode.setStatus("current")


class _AlarmSyntesysWarning_Type(Integer32):
    """Custom type alarmSyntesysWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("activeReportableWarning", 3))
    )


_AlarmSyntesysWarning_Type.__name__ = "Integer32"
_AlarmSyntesysWarning_Object = MibScalar
alarmSyntesysWarning = _AlarmSyntesysWarning_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 4, 24),
    _AlarmSyntesysWarning_Type()
)
alarmSyntesysWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSyntesysWarning.setStatus("current")


class _AlarmSyntesysWarningSeverityCode_Type(Integer32):
    """Custom type alarmSyntesysWarningSeverityCode based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              19)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("warningTrapEnable", 3),
          ("warningTrapDisable", 19))
    )


_AlarmSyntesysWarningSeverityCode_Type.__name__ = "Integer32"
_AlarmSyntesysWarningSeverityCode_Object = MibScalar
alarmSyntesysWarningSeverityCode = _AlarmSyntesysWarningSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 4, 25),
    _AlarmSyntesysWarningSeverityCode_Type()
)
alarmSyntesysWarningSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSyntesysWarningSeverityCode.setStatus("current")


class _AlarmSyntesysStatus_Type(Integer32):
    """Custom type alarmSyntesysStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("activeReportableStatus", 2))
    )


_AlarmSyntesysStatus_Type.__name__ = "Integer32"
_AlarmSyntesysStatus_Object = MibScalar
alarmSyntesysStatus = _AlarmSyntesysStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 4, 26),
    _AlarmSyntesysStatus_Type()
)
alarmSyntesysStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSyntesysStatus.setStatus("current")


class _AlarmSyntesysStatusSeverityCode_Type(Integer32):
    """Custom type alarmSyntesysStatusSeverityCode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              18)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("statusTrapEnable", 2),
          ("statusTrapDisable", 18))
    )


_AlarmSyntesysStatusSeverityCode_Type.__name__ = "Integer32"
_AlarmSyntesysStatusSeverityCode_Object = MibScalar
alarmSyntesysStatusSeverityCode = _AlarmSyntesysStatusSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 4, 27),
    _AlarmSyntesysStatusSeverityCode_Type()
)
alarmSyntesysStatusSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSyntesysStatusSeverityCode.setStatus("current")


class _AlarmAntiFlooding_Type(Integer32):
    """Custom type alarmAntiFlooding based on Integer32"""
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


_AlarmAntiFlooding_Type.__name__ = "Integer32"
_AlarmAntiFlooding_Object = MibScalar
alarmAntiFlooding = _AlarmAntiFlooding_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 4, 28),
    _AlarmAntiFlooding_Type()
)
alarmAntiFlooding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmAntiFlooding.setStatus("current")


class _AlarmAntiFloodingWindow_Type(Integer32):
    """Custom type alarmAntiFloodingWindow based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 120),
    )


_AlarmAntiFloodingWindow_Type.__name__ = "Integer32"
_AlarmAntiFloodingWindow_Object = MibScalar
alarmAntiFloodingWindow = _AlarmAntiFloodingWindow_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 4, 29),
    _AlarmAntiFloodingWindow_Type()
)
alarmAntiFloodingWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmAntiFloodingWindow.setStatus("current")


class _AlarmAntiFloodingHighWater_Type(Integer32):
    """Custom type alarmAntiFloodingHighWater based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 10),
    )


_AlarmAntiFloodingHighWater_Type.__name__ = "Integer32"
_AlarmAntiFloodingHighWater_Object = MibScalar
alarmAntiFloodingHighWater = _AlarmAntiFloodingHighWater_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 4, 30),
    _AlarmAntiFloodingHighWater_Type()
)
alarmAntiFloodingHighWater.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmAntiFloodingHighWater.setStatus("current")


class _AlarmAntiFloodingLowWater_Type(Integer32):
    """Custom type alarmAntiFloodingLowWater based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AlarmAntiFloodingLowWater_Type.__name__ = "Integer32"
_AlarmAntiFloodingLowWater_Object = MibScalar
alarmAntiFloodingLowWater = _AlarmAntiFloodingLowWater_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 4, 31),
    _AlarmAntiFloodingLowWater_Type()
)
alarmAntiFloodingLowWater.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmAntiFloodingLowWater.setStatus("current")
_AlarmItemTable_Object = MibTable
alarmItemTable = _AlarmItemTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 4, 32)
)
if mibBuilder.loadTexts:
    alarmItemTable.setStatus("current")
_AlarmRecord_Object = MibTableRow
alarmRecord = _AlarmRecord_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 4, 32, 1)
)
alarmRecord.setIndexNames(
    (0, "SIAE-ALARM-MIB", "alarmOid"),
)
if mibBuilder.loadTexts:
    alarmRecord.setStatus("current")
_AlarmOid_Type = ObjectIdentifier
_AlarmOid_Object = MibTableColumn
alarmOid = _AlarmOid_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 4, 32, 1, 1),
    _AlarmOid_Type()
)
alarmOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmOid.setStatus("current")


class _AlarmDescription_Type(DisplayString):
    """Custom type alarmDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_AlarmDescription_Type.__name__ = "DisplayString"
_AlarmDescription_Object = MibTableColumn
alarmDescription = _AlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 4, 32, 1, 2),
    _AlarmDescription_Type()
)
alarmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmDescription.setStatus("current")

# Managed Objects groups


# Notification objects

alarmLogFTPStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 0, 401)
)
alarmLogFTPStatusTrap.setObjects(
      *(("SIAE-ALARM-MIB", "alarmIpSnmpAgentAddress"),
        ("SIAE-ALARM-MIB", "alarmLogFTPStatus"),
        ("SIAE-USER-MIB", "accessControlLoginIpAddress"))
)
if mibBuilder.loadTexts:
    alarmLogFTPStatusTrap.setStatus(
        "current"
    )

alarmTrapObject = NotificationType(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 0, 3373)
)
alarmTrapObject.setObjects(
      *(("SIAE-ALARM-MIB", "alarmIpSnmpAgentAddress"),
        ("SIAE-ALARM-MIB", "alarmObjectId"),
        ("SIAE-ALARM-MIB", "alarmObjectVal"),
        ("SIAE-ALARM-MIB", "alarmTrapDescription"),
        ("SIAE-ALARM-MIB", "alarmTrapNumber"))
)
if mibBuilder.loadTexts:
    alarmTrapObject.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SIAE-ALARM-MIB",
    **{"AlarmStatus": AlarmStatus,
       "AlarmSeverityCode": AlarmSeverityCode,
       "alarmTrap": alarmTrap,
       "alarmLogFTPStatusTrap": alarmLogFTPStatusTrap,
       "alarmTrapObject": alarmTrapObject,
       "smalarm": smalarm,
       "alarmMibVersion": alarmMibVersion,
       "siaeNotificationEntry": siaeNotificationEntry,
       "alarmObjectId": alarmObjectId,
       "alarmObjectVal": alarmObjectVal,
       "alarmTrapDescription": alarmTrapDescription,
       "alarmTrapNumber": alarmTrapNumber,
       "alarmIpSnmpAgentAddress": alarmIpSnmpAgentAddress,
       "alarmLogTable": alarmLogTable,
       "alarmLogRecord": alarmLogRecord,
       "alarmLogRecordId": alarmLogRecordId,
       "alarmLogObjectId": alarmLogObjectId,
       "alarmLogObjectVal": alarmLogObjectVal,
       "alarmLogObjectSev": alarmLogObjectSev,
       "alarmLogDescription": alarmLogDescription,
       "alarmLogEventTime": alarmLogEventTime,
       "alarmLogActionRequest": alarmLogActionRequest,
       "alarmLogFTPfile": alarmLogFTPfile,
       "alarmLogAlarmSeverityEnable": alarmLogAlarmSeverityEnable,
       "alarmLogStartHourEnable": alarmLogStartHourEnable,
       "alarmLogEndHourEnable": alarmLogEndHourEnable,
       "alarmLogStartTimeFilter": alarmLogStartTimeFilter,
       "alarmLogEndTimeFilter": alarmLogEndTimeFilter,
       "alarmLogManagedObjectFilter": alarmLogManagedObjectFilter,
       "alarmLogAlarmSeverityFilter": alarmLogAlarmSeverityFilter,
       "alarmLogFTPStatus": alarmLogFTPStatus,
       "alarmLogFTPStatusTrapNotification": alarmLogFTPStatusTrapNotification,
       "alarmLogLastEventTime": alarmLogLastEventTime,
       "alarmActiveTable": alarmActiveTable,
       "alarmActiveRecord": alarmActiveRecord,
       "alarmActiveObjectId": alarmActiveObjectId,
       "alarmActiveObjectVal": alarmActiveObjectVal,
       "alarmActiveDescription": alarmActiveDescription,
       "alarmActiveEventTime": alarmActiveEventTime,
       "alarmActiveFloodingStatus": alarmActiveFloodingStatus,
       "alarmSyntesysCritical": alarmSyntesysCritical,
       "alarmSyntesysCriticalSeverityCode": alarmSyntesysCriticalSeverityCode,
       "alarmSyntesysMajor": alarmSyntesysMajor,
       "alarmSyntesysMajorSeverityCode": alarmSyntesysMajorSeverityCode,
       "alarmSyntesysMinor": alarmSyntesysMinor,
       "alarmSyntesysMinorSeverityCode": alarmSyntesysMinorSeverityCode,
       "alarmSyntesysWarning": alarmSyntesysWarning,
       "alarmSyntesysWarningSeverityCode": alarmSyntesysWarningSeverityCode,
       "alarmSyntesysStatus": alarmSyntesysStatus,
       "alarmSyntesysStatusSeverityCode": alarmSyntesysStatusSeverityCode,
       "alarmAntiFlooding": alarmAntiFlooding,
       "alarmAntiFloodingWindow": alarmAntiFloodingWindow,
       "alarmAntiFloodingHighWater": alarmAntiFloodingHighWater,
       "alarmAntiFloodingLowWater": alarmAntiFloodingLowWater,
       "alarmItemTable": alarmItemTable,
       "alarmRecord": alarmRecord,
       "alarmOid": alarmOid,
       "alarmDescription": alarmDescription}
)
