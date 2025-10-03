# SNMP MIB module (SIAE-ACM-STATISTICS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\siae\SIAE-ACM-STATISTICS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:26:33 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

acmStats = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 75)
)
if mibBuilder.loadTexts:
    acmStats.setRevisions(
        ("2014-11-05 00:00",
         "2014-02-11 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AcmProfile(TextualConvention, Integer32):
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
              24,
              25,
              26,
              27)
        )
    )
    namedValues = NamedValues(
        *(("unavailable", 1),
          ("downshift", 2),
          ("upshift", 3),
          ("acmBPSKstrong", 4),
          ("acmBPSK", 5),
          ("acm4QAMstrong", 6),
          ("acm4QAM", 7),
          ("acm8PSKstrong", 8),
          ("acm8PSK", 9),
          ("acm16QAMstrong", 10),
          ("acm16QAM", 11),
          ("acm32QAMstrong", 12),
          ("acm32QAM", 13),
          ("acm64QAMstrong", 14),
          ("acm64QAM", 15),
          ("acm128QAMstrong", 16),
          ("acm128QAM", 17),
          ("acm256QAMstrong", 18),
          ("acm256QAM", 19),
          ("acm512QAMstrong", 20),
          ("acm512QAM", 21),
          ("acm1024QAMstrong", 22),
          ("acm1024QAM", 23),
          ("acm2048QAMstrong", 24),
          ("acm2048QAM", 25),
          ("acm4096QAMstrong", 26),
          ("acm4096QAM", 27))
    )



# MIB Managed Objects in the order of their OIDs

_AcmsMibVersion_Type = Integer32
_AcmsMibVersion_Object = MibScalar
acmsMibVersion = _AcmsMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 75, 1),
    _AcmsMibVersion_Type()
)
acmsMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acmsMibVersion.setStatus("current")
_AcmsTpLinkTable_Object = MibTable
acmsTpLinkTable = _AcmsTpLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 75, 2)
)
if mibBuilder.loadTexts:
    acmsTpLinkTable.setStatus("current")
_AcmsTpLinkRecord_Object = MibTableRow
acmsTpLinkRecord = _AcmsTpLinkRecord_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 75, 2, 1)
)
acmsTpLinkRecord.setIndexNames(
    (0, "SIAE-ACM-STATISTICS-MIB", "acmsTpLinkId"),
    (0, "SIAE-ACM-STATISTICS-MIB", "acmsTpLinkPolId"),
)
if mibBuilder.loadTexts:
    acmsTpLinkRecord.setStatus("current")
_AcmsTpLinkId_Type = Integer32
_AcmsTpLinkId_Object = MibTableColumn
acmsTpLinkId = _AcmsTpLinkId_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 75, 2, 1, 1),
    _AcmsTpLinkId_Type()
)
acmsTpLinkId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acmsTpLinkId.setStatus("current")
_AcmsTpLinkPolId_Type = Integer32
_AcmsTpLinkPolId_Object = MibTableColumn
acmsTpLinkPolId = _AcmsTpLinkPolId_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 75, 2, 1, 2),
    _AcmsTpLinkPolId_Type()
)
acmsTpLinkPolId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acmsTpLinkPolId.setStatus("current")


class _AcmsTpLinkStartStop_Type(Integer32):
    """Custom type acmsTpLinkStartStop based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 2))
    )


_AcmsTpLinkStartStop_Type.__name__ = "Integer32"
_AcmsTpLinkStartStop_Object = MibTableColumn
acmsTpLinkStartStop = _AcmsTpLinkStartStop_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 75, 2, 1, 3),
    _AcmsTpLinkStartStop_Type()
)
acmsTpLinkStartStop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acmsTpLinkStartStop.setStatus("current")


class _AcmsTpLinkLabel_Type(DisplayString):
    """Custom type acmsTpLinkLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AcmsTpLinkLabel_Type.__name__ = "DisplayString"
_AcmsTpLinkLabel_Object = MibTableColumn
acmsTpLinkLabel = _AcmsTpLinkLabel_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 75, 2, 1, 4),
    _AcmsTpLinkLabel_Type()
)
acmsTpLinkLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acmsTpLinkLabel.setStatus("current")
_AcmsTpLinkRowStatus_Type = RowStatus
_AcmsTpLinkRowStatus_Object = MibTableColumn
acmsTpLinkRowStatus = _AcmsTpLinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 75, 2, 1, 5),
    _AcmsTpLinkRowStatus_Type()
)
acmsTpLinkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acmsTpLinkRowStatus.setStatus("current")
_AcmsTpProfileTable_Object = MibTable
acmsTpProfileTable = _AcmsTpProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 75, 3)
)
if mibBuilder.loadTexts:
    acmsTpProfileTable.setStatus("current")
_AcmsTpProfileRecord_Object = MibTableRow
acmsTpProfileRecord = _AcmsTpProfileRecord_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 75, 3, 1)
)
acmsTpProfileRecord.setIndexNames(
    (0, "SIAE-ACM-STATISTICS-MIB", "acmsTpLinkId"),
    (0, "SIAE-ACM-STATISTICS-MIB", "acmsTpLinkPolId"),
    (0, "SIAE-ACM-STATISTICS-MIB", "acmsTpProfileId"),
)
if mibBuilder.loadTexts:
    acmsTpProfileRecord.setStatus("current")
_AcmsTpProfileId_Type = AcmProfile
_AcmsTpProfileId_Object = MibTableColumn
acmsTpProfileId = _AcmsTpProfileId_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 75, 3, 1, 1),
    _AcmsTpProfileId_Type()
)
acmsTpProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acmsTpProfileId.setStatus("current")
_AcmsTpProfile15mAlarm_Type = AlarmStatus
_AcmsTpProfile15mAlarm_Object = MibTableColumn
acmsTpProfile15mAlarm = _AcmsTpProfile15mAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 75, 3, 1, 2),
    _AcmsTpProfile15mAlarm_Type()
)
acmsTpProfile15mAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acmsTpProfile15mAlarm.setStatus("current")
_AcmsTpProfile24hAlarm_Type = AlarmStatus
_AcmsTpProfile24hAlarm_Object = MibTableColumn
acmsTpProfile24hAlarm = _AcmsTpProfile24hAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 75, 3, 1, 3),
    _AcmsTpProfile24hAlarm_Type()
)
acmsTpProfile24hAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acmsTpProfile24hAlarm.setStatus("current")
_AcmsTpProfile15mThreshold_Type = Integer32
_AcmsTpProfile15mThreshold_Object = MibTableColumn
acmsTpProfile15mThreshold = _AcmsTpProfile15mThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 75, 3, 1, 4),
    _AcmsTpProfile15mThreshold_Type()
)
acmsTpProfile15mThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acmsTpProfile15mThreshold.setStatus("current")
_AcmsTpProfile24hThreshold_Type = Integer32
_AcmsTpProfile24hThreshold_Object = MibTableColumn
acmsTpProfile24hThreshold = _AcmsTpProfile24hThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 75, 3, 1, 5),
    _AcmsTpProfile24hThreshold_Type()
)
acmsTpProfile24hThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acmsTpProfile24hThreshold.setStatus("current")
_AcmsTpProfileRowStatus_Type = RowStatus
_AcmsTpProfileRowStatus_Object = MibTableColumn
acmsTpProfileRowStatus = _AcmsTpProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 75, 3, 1, 6),
    _AcmsTpProfileRowStatus_Type()
)
acmsTpProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acmsTpProfileRowStatus.setStatus("current")
_AcmsTpMaintTable_Object = MibTable
acmsTpMaintTable = _AcmsTpMaintTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 75, 4)
)
if mibBuilder.loadTexts:
    acmsTpMaintTable.setStatus("current")
_AcmsTpMaintRecord_Object = MibTableRow
acmsTpMaintRecord = _AcmsTpMaintRecord_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 75, 4, 1)
)
acmsTpMaintRecord.setIndexNames(
    (0, "SIAE-ACM-STATISTICS-MIB", "acmsTpLinkId"),
    (0, "SIAE-ACM-STATISTICS-MIB", "acmsTpLinkPolId"),
)
if mibBuilder.loadTexts:
    acmsTpMaintRecord.setStatus("current")


class _AcmsTpMaintCounterClear_Type(Integer32):
    """Custom type acmsTpMaintCounterClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notActive", 0),
          ("clear", 1))
    )


_AcmsTpMaintCounterClear_Type.__name__ = "Integer32"
_AcmsTpMaintCounterClear_Object = MibTableColumn
acmsTpMaintCounterClear = _AcmsTpMaintCounterClear_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 75, 4, 1, 1),
    _AcmsTpMaintCounterClear_Type()
)
acmsTpMaintCounterClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acmsTpMaintCounterClear.setStatus("current")


class _AcmsTpMaintAlarmClear_Type(Integer32):
    """Custom type acmsTpMaintAlarmClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notActive", 0),
          ("clear", 1))
    )


_AcmsTpMaintAlarmClear_Type.__name__ = "Integer32"
_AcmsTpMaintAlarmClear_Object = MibTableColumn
acmsTpMaintAlarmClear = _AcmsTpMaintAlarmClear_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 75, 4, 1, 2),
    _AcmsTpMaintAlarmClear_Type()
)
acmsTpMaintAlarmClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acmsTpMaintAlarmClear.setStatus("current")
_AcmsIntervalTable_Object = MibTable
acmsIntervalTable = _AcmsIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 75, 5)
)
if mibBuilder.loadTexts:
    acmsIntervalTable.setStatus("current")
_AcmsIntervalRecord_Object = MibTableRow
acmsIntervalRecord = _AcmsIntervalRecord_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 75, 5, 1)
)
acmsIntervalRecord.setIndexNames(
    (0, "SIAE-ACM-STATISTICS-MIB", "acmsTpLinkId"),
    (0, "SIAE-ACM-STATISTICS-MIB", "acmsTpLinkPolId"),
    (0, "SIAE-ACM-STATISTICS-MIB", "acmsIntervalId"),
)
if mibBuilder.loadTexts:
    acmsIntervalRecord.setStatus("current")


class _AcmsIntervalId_Type(Integer32):
    """Custom type acmsIntervalId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 19),
    )


_AcmsIntervalId_Type.__name__ = "Integer32"
_AcmsIntervalId_Object = MibTableColumn
acmsIntervalId = _AcmsIntervalId_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 75, 5, 1, 1),
    _AcmsIntervalId_Type()
)
acmsIntervalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acmsIntervalId.setStatus("current")


class _AcmsIntervalType_Type(Integer32):
    """Custom type acmsIntervalType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("daily", 1),
          ("fifteen-min", 2))
    )


_AcmsIntervalType_Type.__name__ = "Integer32"
_AcmsIntervalType_Object = MibTableColumn
acmsIntervalType = _AcmsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 75, 5, 1, 2),
    _AcmsIntervalType_Type()
)
acmsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acmsIntervalType.setStatus("current")


class _AcmsIntervalStatus_Type(Integer32):
    """Custom type acmsIntervalStatus based on Integer32"""
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
        *(("meaningless", 1),
          ("meaningfull", 2),
          ("incomplete", 3),
          ("dummy", 4),
          ("lost", 5),
          ("restarted", 6))
    )


_AcmsIntervalStatus_Type.__name__ = "Integer32"
_AcmsIntervalStatus_Object = MibTableColumn
acmsIntervalStatus = _AcmsIntervalStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 75, 5, 1, 3),
    _AcmsIntervalStatus_Type()
)
acmsIntervalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acmsIntervalStatus.setStatus("current")
_AcmsIntervalTimeStamp_Type = Unsigned32
_AcmsIntervalTimeStamp_Object = MibTableColumn
acmsIntervalTimeStamp = _AcmsIntervalTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 75, 5, 1, 4),
    _AcmsIntervalTimeStamp_Type()
)
acmsIntervalTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acmsIntervalTimeStamp.setStatus("current")
_AcmsProfileCounterTable_Object = MibTable
acmsProfileCounterTable = _AcmsProfileCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 75, 6)
)
if mibBuilder.loadTexts:
    acmsProfileCounterTable.setStatus("current")
_AcmsProfileCounterRecord_Object = MibTableRow
acmsProfileCounterRecord = _AcmsProfileCounterRecord_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 75, 6, 1)
)
acmsProfileCounterRecord.setIndexNames(
    (0, "SIAE-ACM-STATISTICS-MIB", "acmsTpLinkId"),
    (0, "SIAE-ACM-STATISTICS-MIB", "acmsTpLinkPolId"),
    (0, "SIAE-ACM-STATISTICS-MIB", "acmsTpProfileId"),
    (0, "SIAE-ACM-STATISTICS-MIB", "acmsIntervalId"),
)
if mibBuilder.loadTexts:
    acmsProfileCounterRecord.setStatus("current")
_AcmsProfileCounterValue_Type = Counter32
_AcmsProfileCounterValue_Object = MibTableColumn
acmsProfileCounterValue = _AcmsProfileCounterValue_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 75, 6, 1, 1),
    _AcmsProfileCounterValue_Type()
)
acmsProfileCounterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acmsProfileCounterValue.setStatus("current")


class _AcmsTpProfile15mAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type acmsTpProfile15mAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_AcmsTpProfile15mAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_AcmsTpProfile15mAlarmSeverityCode_Object = MibScalar
acmsTpProfile15mAlarmSeverityCode = _AcmsTpProfile15mAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 75, 7),
    _AcmsTpProfile15mAlarmSeverityCode_Type()
)
acmsTpProfile15mAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acmsTpProfile15mAlarmSeverityCode.setStatus("current")


class _AcmsTpProfile24hAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type acmsTpProfile24hAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_AcmsTpProfile24hAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_AcmsTpProfile24hAlarmSeverityCode_Object = MibScalar
acmsTpProfile24hAlarmSeverityCode = _AcmsTpProfile24hAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 75, 8),
    _AcmsTpProfile24hAlarmSeverityCode_Type()
)
acmsTpProfile24hAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acmsTpProfile24hAlarmSeverityCode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SIAE-ACM-STATISTICS-MIB",
    **{"AcmProfile": AcmProfile,
       "acmStats": acmStats,
       "acmsMibVersion": acmsMibVersion,
       "acmsTpLinkTable": acmsTpLinkTable,
       "acmsTpLinkRecord": acmsTpLinkRecord,
       "acmsTpLinkId": acmsTpLinkId,
       "acmsTpLinkPolId": acmsTpLinkPolId,
       "acmsTpLinkStartStop": acmsTpLinkStartStop,
       "acmsTpLinkLabel": acmsTpLinkLabel,
       "acmsTpLinkRowStatus": acmsTpLinkRowStatus,
       "acmsTpProfileTable": acmsTpProfileTable,
       "acmsTpProfileRecord": acmsTpProfileRecord,
       "acmsTpProfileId": acmsTpProfileId,
       "acmsTpProfile15mAlarm": acmsTpProfile15mAlarm,
       "acmsTpProfile24hAlarm": acmsTpProfile24hAlarm,
       "acmsTpProfile15mThreshold": acmsTpProfile15mThreshold,
       "acmsTpProfile24hThreshold": acmsTpProfile24hThreshold,
       "acmsTpProfileRowStatus": acmsTpProfileRowStatus,
       "acmsTpMaintTable": acmsTpMaintTable,
       "acmsTpMaintRecord": acmsTpMaintRecord,
       "acmsTpMaintCounterClear": acmsTpMaintCounterClear,
       "acmsTpMaintAlarmClear": acmsTpMaintAlarmClear,
       "acmsIntervalTable": acmsIntervalTable,
       "acmsIntervalRecord": acmsIntervalRecord,
       "acmsIntervalId": acmsIntervalId,
       "acmsIntervalType": acmsIntervalType,
       "acmsIntervalStatus": acmsIntervalStatus,
       "acmsIntervalTimeStamp": acmsIntervalTimeStamp,
       "acmsProfileCounterTable": acmsProfileCounterTable,
       "acmsProfileCounterRecord": acmsProfileCounterRecord,
       "acmsProfileCounterValue": acmsProfileCounterValue,
       "acmsTpProfile15mAlarmSeverityCode": acmsTpProfile15mAlarmSeverityCode,
       "acmsTpProfile24hAlarmSeverityCode": acmsTpProfile24hAlarmSeverityCode}
)
