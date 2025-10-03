# SNMP MIB module (SIAE-PMRXPWR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\siae\SIAE-PMRXPWR-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:27:18 2025
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

pmRxPwr = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 12)
)
if mibBuilder.loadTexts:
    pmRxPwr.setRevisions(
        ("2014-10-07 00:00",
         "2014-05-13 00:00",
         "2014-02-03 00:00",
         "2013-04-16 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _PmRxPwrMibVersion_Type(Integer32):
    """Custom type pmRxPwrMibVersion based on Integer32"""
    defaultValue = 1


_PmRxPwrMibVersion_Type.__name__ = "Integer32"
_PmRxPwrMibVersion_Object = MibScalar
pmRxPwrMibVersion = _PmRxPwrMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 12, 1),
    _PmRxPwrMibVersion_Type()
)
pmRxPwrMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmRxPwrMibVersion.setStatus("current")
_PmRxPwrCounterTable_Object = MibTable
pmRxPwrCounterTable = _PmRxPwrCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 12, 2)
)
if mibBuilder.loadTexts:
    pmRxPwrCounterTable.setStatus("current")
_PmRxPwrCounterRecord_Object = MibTableRow
pmRxPwrCounterRecord = _PmRxPwrCounterRecord_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 12, 2, 1)
)
pmRxPwrCounterRecord.setIndexNames(
    (0, "SIAE-PMRXPWR-MIB", "pmRxPwrBranchId"),
    (0, "SIAE-PMRXPWR-MIB", "pmRxPwrCounterBlockId"),
)
if mibBuilder.loadTexts:
    pmRxPwrCounterRecord.setStatus("current")
_PmRxPwrBranchId_Type = Integer32
_PmRxPwrBranchId_Object = MibTableColumn
pmRxPwrBranchId = _PmRxPwrBranchId_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 12, 2, 1, 1),
    _PmRxPwrBranchId_Type()
)
pmRxPwrBranchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmRxPwrBranchId.setStatus("current")
_PmRxPwrCounterBlockId_Type = Integer32
_PmRxPwrCounterBlockId_Object = MibTableColumn
pmRxPwrCounterBlockId = _PmRxPwrCounterBlockId_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 12, 2, 1, 2),
    _PmRxPwrCounterBlockId_Type()
)
pmRxPwrCounterBlockId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmRxPwrCounterBlockId.setStatus("current")


class _PmRxPwrCounterBlockType_Type(Integer32):
    """Custom type pmRxPwrCounterBlockType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("daily", 1),
          ("fifteenMin", 2))
    )


_PmRxPwrCounterBlockType_Type.__name__ = "Integer32"
_PmRxPwrCounterBlockType_Object = MibTableColumn
pmRxPwrCounterBlockType = _PmRxPwrCounterBlockType_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 12, 2, 1, 3),
    _PmRxPwrCounterBlockType_Type()
)
pmRxPwrCounterBlockType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmRxPwrCounterBlockType.setStatus("current")


class _PmRxPwrCounterBlockStatus_Type(Integer32):
    """Custom type pmRxPwrCounterBlockStatus based on Integer32"""
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


_PmRxPwrCounterBlockStatus_Type.__name__ = "Integer32"
_PmRxPwrCounterBlockStatus_Object = MibTableColumn
pmRxPwrCounterBlockStatus = _PmRxPwrCounterBlockStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 12, 2, 1, 4),
    _PmRxPwrCounterBlockStatus_Type()
)
pmRxPwrCounterBlockStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmRxPwrCounterBlockStatus.setStatus("current")
_PmRxPwrCounterTimeStamp_Type = Unsigned32
_PmRxPwrCounterTimeStamp_Object = MibTableColumn
pmRxPwrCounterTimeStamp = _PmRxPwrCounterTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 12, 2, 1, 5),
    _PmRxPwrCounterTimeStamp_Type()
)
pmRxPwrCounterTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmRxPwrCounterTimeStamp.setStatus("current")
_PmRxPwrRlts1Counter_Type = Counter32
_PmRxPwrRlts1Counter_Object = MibTableColumn
pmRxPwrRlts1Counter = _PmRxPwrRlts1Counter_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 12, 2, 1, 6),
    _PmRxPwrRlts1Counter_Type()
)
pmRxPwrRlts1Counter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmRxPwrRlts1Counter.setStatus("current")
_PmRxPwrRlts2Counter_Type = Counter32
_PmRxPwrRlts2Counter_Object = MibTableColumn
pmRxPwrRlts2Counter = _PmRxPwrRlts2Counter_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 12, 2, 1, 7),
    _PmRxPwrRlts2Counter_Type()
)
pmRxPwrRlts2Counter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmRxPwrRlts2Counter.setStatus("current")
_PmRxPwrRlts3Counter_Type = Counter32
_PmRxPwrRlts3Counter_Object = MibTableColumn
pmRxPwrRlts3Counter = _PmRxPwrRlts3Counter_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 12, 2, 1, 8),
    _PmRxPwrRlts3Counter_Type()
)
pmRxPwrRlts3Counter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmRxPwrRlts3Counter.setStatus("current")
_PmRxPwrRlts4Counter_Type = Counter32
_PmRxPwrRlts4Counter_Object = MibTableColumn
pmRxPwrRlts4Counter = _PmRxPwrRlts4Counter_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 12, 2, 1, 9),
    _PmRxPwrRlts4Counter_Type()
)
pmRxPwrRlts4Counter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmRxPwrRlts4Counter.setStatus("current")
_PmRxPwrRlts5Counter_Type = Counter32
_PmRxPwrRlts5Counter_Object = MibTableColumn
pmRxPwrRlts5Counter = _PmRxPwrRlts5Counter_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 12, 2, 1, 10),
    _PmRxPwrRlts5Counter_Type()
)
pmRxPwrRlts5Counter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmRxPwrRlts5Counter.setStatus("current")
_PmRxPwrTMMax_Type = Integer32
_PmRxPwrTMMax_Object = MibTableColumn
pmRxPwrTMMax = _PmRxPwrTMMax_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 12, 2, 1, 11),
    _PmRxPwrTMMax_Type()
)
pmRxPwrTMMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmRxPwrTMMax.setStatus("current")
_PmRxPwrTMMin_Type = Integer32
_PmRxPwrTMMin_Object = MibTableColumn
pmRxPwrTMMin = _PmRxPwrTMMin_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 12, 2, 1, 12),
    _PmRxPwrTMMin_Type()
)
pmRxPwrTMMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmRxPwrTMMin.setStatus("current")
_PmRxPwrAverageRxLevel_Type = Integer32
_PmRxPwrAverageRxLevel_Object = MibTableColumn
pmRxPwrAverageRxLevel = _PmRxPwrAverageRxLevel_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 12, 2, 1, 13),
    _PmRxPwrAverageRxLevel_Type()
)
pmRxPwrAverageRxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmRxPwrAverageRxLevel.setStatus("current")
_PmRxPwrTpClassTable_Object = MibTable
pmRxPwrTpClassTable = _PmRxPwrTpClassTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3)
)
if mibBuilder.loadTexts:
    pmRxPwrTpClassTable.setStatus("current")
_PmRxPwrTpClassRecord_Object = MibTableRow
pmRxPwrTpClassRecord = _PmRxPwrTpClassRecord_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1)
)
pmRxPwrTpClassRecord.setIndexNames(
    (0, "SIAE-PMRXPWR-MIB", "pmRxPwrTpClassBranchId"),
)
if mibBuilder.loadTexts:
    pmRxPwrTpClassRecord.setStatus("current")
_PmRxPwrTpClassBranchId_Type = Integer32
_PmRxPwrTpClassBranchId_Object = MibTableColumn
pmRxPwrTpClassBranchId = _PmRxPwrTpClassBranchId_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 1),
    _PmRxPwrTpClassBranchId_Type()
)
pmRxPwrTpClassBranchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmRxPwrTpClassBranchId.setStatus("current")


class _PmRxPwrTpClassStartStop_Type(Integer32):
    """Custom type pmRxPwrTpClassStartStop based on Integer32"""
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


_PmRxPwrTpClassStartStop_Type.__name__ = "Integer32"
_PmRxPwrTpClassStartStop_Object = MibTableColumn
pmRxPwrTpClassStartStop = _PmRxPwrTpClassStartStop_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 2),
    _PmRxPwrTpClassStartStop_Type()
)
pmRxPwrTpClassStartStop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmRxPwrTpClassStartStop.setStatus("current")


class _PmRxPwrTpClassLabel_Type(DisplayString):
    """Custom type pmRxPwrTpClassLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PmRxPwrTpClassLabel_Type.__name__ = "DisplayString"
_PmRxPwrTpClassLabel_Object = MibTableColumn
pmRxPwrTpClassLabel = _PmRxPwrTpClassLabel_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 3),
    _PmRxPwrTpClassLabel_Type()
)
pmRxPwrTpClassLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmRxPwrTpClassLabel.setStatus("current")
_PmRxPwrTpClassTimeStamp_Type = Unsigned32
_PmRxPwrTpClassTimeStamp_Object = MibTableColumn
pmRxPwrTpClassTimeStamp = _PmRxPwrTpClassTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 4),
    _PmRxPwrTpClassTimeStamp_Type()
)
pmRxPwrTpClassTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmRxPwrTpClassTimeStamp.setStatus("current")
_PmRxPwrTpClass15MRlts1Alarm_Type = AlarmStatus
_PmRxPwrTpClass15MRlts1Alarm_Object = MibTableColumn
pmRxPwrTpClass15MRlts1Alarm = _PmRxPwrTpClass15MRlts1Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 5),
    _PmRxPwrTpClass15MRlts1Alarm_Type()
)
pmRxPwrTpClass15MRlts1Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmRxPwrTpClass15MRlts1Alarm.setStatus("current")
_PmRxPwrTpClass15MRlts2Alarm_Type = AlarmStatus
_PmRxPwrTpClass15MRlts2Alarm_Object = MibTableColumn
pmRxPwrTpClass15MRlts2Alarm = _PmRxPwrTpClass15MRlts2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 6),
    _PmRxPwrTpClass15MRlts2Alarm_Type()
)
pmRxPwrTpClass15MRlts2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmRxPwrTpClass15MRlts2Alarm.setStatus("current")
_PmRxPwrTpClass15MRlts3Alarm_Type = AlarmStatus
_PmRxPwrTpClass15MRlts3Alarm_Object = MibTableColumn
pmRxPwrTpClass15MRlts3Alarm = _PmRxPwrTpClass15MRlts3Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 7),
    _PmRxPwrTpClass15MRlts3Alarm_Type()
)
pmRxPwrTpClass15MRlts3Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmRxPwrTpClass15MRlts3Alarm.setStatus("current")
_PmRxPwrTpClass15MRlts4Alarm_Type = AlarmStatus
_PmRxPwrTpClass15MRlts4Alarm_Object = MibTableColumn
pmRxPwrTpClass15MRlts4Alarm = _PmRxPwrTpClass15MRlts4Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 8),
    _PmRxPwrTpClass15MRlts4Alarm_Type()
)
pmRxPwrTpClass15MRlts4Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmRxPwrTpClass15MRlts4Alarm.setStatus("current")
_PmRxPwrTpClass15MRlts5Alarm_Type = AlarmStatus
_PmRxPwrTpClass15MRlts5Alarm_Object = MibTableColumn
pmRxPwrTpClass15MRlts5Alarm = _PmRxPwrTpClass15MRlts5Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 9),
    _PmRxPwrTpClass15MRlts5Alarm_Type()
)
pmRxPwrTpClass15MRlts5Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmRxPwrTpClass15MRlts5Alarm.setStatus("current")
_PmRxPwrTpClass24HRlts1Alarm_Type = AlarmStatus
_PmRxPwrTpClass24HRlts1Alarm_Object = MibTableColumn
pmRxPwrTpClass24HRlts1Alarm = _PmRxPwrTpClass24HRlts1Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 10),
    _PmRxPwrTpClass24HRlts1Alarm_Type()
)
pmRxPwrTpClass24HRlts1Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmRxPwrTpClass24HRlts1Alarm.setStatus("current")
_PmRxPwrTpClass24HRlts2Alarm_Type = AlarmStatus
_PmRxPwrTpClass24HRlts2Alarm_Object = MibTableColumn
pmRxPwrTpClass24HRlts2Alarm = _PmRxPwrTpClass24HRlts2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 11),
    _PmRxPwrTpClass24HRlts2Alarm_Type()
)
pmRxPwrTpClass24HRlts2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmRxPwrTpClass24HRlts2Alarm.setStatus("current")
_PmRxPwrTpClass24HRlts3Alarm_Type = AlarmStatus
_PmRxPwrTpClass24HRlts3Alarm_Object = MibTableColumn
pmRxPwrTpClass24HRlts3Alarm = _PmRxPwrTpClass24HRlts3Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 12),
    _PmRxPwrTpClass24HRlts3Alarm_Type()
)
pmRxPwrTpClass24HRlts3Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmRxPwrTpClass24HRlts3Alarm.setStatus("current")
_PmRxPwrTpClass24HRlts4Alarm_Type = AlarmStatus
_PmRxPwrTpClass24HRlts4Alarm_Object = MibTableColumn
pmRxPwrTpClass24HRlts4Alarm = _PmRxPwrTpClass24HRlts4Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 13),
    _PmRxPwrTpClass24HRlts4Alarm_Type()
)
pmRxPwrTpClass24HRlts4Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmRxPwrTpClass24HRlts4Alarm.setStatus("current")
_PmRxPwrTpClass24HRlts5Alarm_Type = AlarmStatus
_PmRxPwrTpClass24HRlts5Alarm_Object = MibTableColumn
pmRxPwrTpClass24HRlts5Alarm = _PmRxPwrTpClass24HRlts5Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 14),
    _PmRxPwrTpClass24HRlts5Alarm_Type()
)
pmRxPwrTpClass24HRlts5Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmRxPwrTpClass24HRlts5Alarm.setStatus("current")


class _PmRxPwrTpClassRlt1Threshold_Type(Integer32):
    """Custom type pmRxPwrTpClassRlt1Threshold based on Integer32"""
    defaultValue = -40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, -20),
    )


_PmRxPwrTpClassRlt1Threshold_Type.__name__ = "Integer32"
_PmRxPwrTpClassRlt1Threshold_Object = MibTableColumn
pmRxPwrTpClassRlt1Threshold = _PmRxPwrTpClassRlt1Threshold_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 15),
    _PmRxPwrTpClassRlt1Threshold_Type()
)
pmRxPwrTpClassRlt1Threshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmRxPwrTpClassRlt1Threshold.setStatus("current")


class _PmRxPwrTpClassRlt2Threshold_Type(Integer32):
    """Custom type pmRxPwrTpClassRlt2Threshold based on Integer32"""
    defaultValue = -50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, -20),
    )


_PmRxPwrTpClassRlt2Threshold_Type.__name__ = "Integer32"
_PmRxPwrTpClassRlt2Threshold_Object = MibTableColumn
pmRxPwrTpClassRlt2Threshold = _PmRxPwrTpClassRlt2Threshold_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 16),
    _PmRxPwrTpClassRlt2Threshold_Type()
)
pmRxPwrTpClassRlt2Threshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmRxPwrTpClassRlt2Threshold.setStatus("current")


class _PmRxPwrTpClassRlt3Threshold_Type(Integer32):
    """Custom type pmRxPwrTpClassRlt3Threshold based on Integer32"""
    defaultValue = -60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, -20),
    )


_PmRxPwrTpClassRlt3Threshold_Type.__name__ = "Integer32"
_PmRxPwrTpClassRlt3Threshold_Object = MibTableColumn
pmRxPwrTpClassRlt3Threshold = _PmRxPwrTpClassRlt3Threshold_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 17),
    _PmRxPwrTpClassRlt3Threshold_Type()
)
pmRxPwrTpClassRlt3Threshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmRxPwrTpClassRlt3Threshold.setStatus("current")


class _PmRxPwrTpClassRlt4Threshold_Type(Integer32):
    """Custom type pmRxPwrTpClassRlt4Threshold based on Integer32"""
    defaultValue = -70

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, -20),
    )


_PmRxPwrTpClassRlt4Threshold_Type.__name__ = "Integer32"
_PmRxPwrTpClassRlt4Threshold_Object = MibTableColumn
pmRxPwrTpClassRlt4Threshold = _PmRxPwrTpClassRlt4Threshold_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 18),
    _PmRxPwrTpClassRlt4Threshold_Type()
)
pmRxPwrTpClassRlt4Threshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmRxPwrTpClassRlt4Threshold.setStatus("current")


class _PmRxPwrTpClassRlt5Threshold_Type(Integer32):
    """Custom type pmRxPwrTpClassRlt5Threshold based on Integer32"""
    defaultValue = -80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, -20),
    )


_PmRxPwrTpClassRlt5Threshold_Type.__name__ = "Integer32"
_PmRxPwrTpClassRlt5Threshold_Object = MibTableColumn
pmRxPwrTpClassRlt5Threshold = _PmRxPwrTpClassRlt5Threshold_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 19),
    _PmRxPwrTpClassRlt5Threshold_Type()
)
pmRxPwrTpClassRlt5Threshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmRxPwrTpClassRlt5Threshold.setStatus("current")


class _PmRxPwrTpClass15MRlts1Threshold_Type(Integer32):
    """Custom type pmRxPwrTpClass15MRlts1Threshold based on Integer32"""
    defaultValue = 0


_PmRxPwrTpClass15MRlts1Threshold_Type.__name__ = "Integer32"
_PmRxPwrTpClass15MRlts1Threshold_Object = MibTableColumn
pmRxPwrTpClass15MRlts1Threshold = _PmRxPwrTpClass15MRlts1Threshold_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 20),
    _PmRxPwrTpClass15MRlts1Threshold_Type()
)
pmRxPwrTpClass15MRlts1Threshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmRxPwrTpClass15MRlts1Threshold.setStatus("current")


class _PmRxPwrTpClass15MRlts2Threshold_Type(Integer32):
    """Custom type pmRxPwrTpClass15MRlts2Threshold based on Integer32"""
    defaultValue = 0


_PmRxPwrTpClass15MRlts2Threshold_Type.__name__ = "Integer32"
_PmRxPwrTpClass15MRlts2Threshold_Object = MibTableColumn
pmRxPwrTpClass15MRlts2Threshold = _PmRxPwrTpClass15MRlts2Threshold_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 21),
    _PmRxPwrTpClass15MRlts2Threshold_Type()
)
pmRxPwrTpClass15MRlts2Threshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmRxPwrTpClass15MRlts2Threshold.setStatus("current")


class _PmRxPwrTpClass15MRlts3Threshold_Type(Integer32):
    """Custom type pmRxPwrTpClass15MRlts3Threshold based on Integer32"""
    defaultValue = 0


_PmRxPwrTpClass15MRlts3Threshold_Type.__name__ = "Integer32"
_PmRxPwrTpClass15MRlts3Threshold_Object = MibTableColumn
pmRxPwrTpClass15MRlts3Threshold = _PmRxPwrTpClass15MRlts3Threshold_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 22),
    _PmRxPwrTpClass15MRlts3Threshold_Type()
)
pmRxPwrTpClass15MRlts3Threshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmRxPwrTpClass15MRlts3Threshold.setStatus("current")


class _PmRxPwrTpClass15MRlts4Threshold_Type(Integer32):
    """Custom type pmRxPwrTpClass15MRlts4Threshold based on Integer32"""
    defaultValue = 0


_PmRxPwrTpClass15MRlts4Threshold_Type.__name__ = "Integer32"
_PmRxPwrTpClass15MRlts4Threshold_Object = MibTableColumn
pmRxPwrTpClass15MRlts4Threshold = _PmRxPwrTpClass15MRlts4Threshold_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 23),
    _PmRxPwrTpClass15MRlts4Threshold_Type()
)
pmRxPwrTpClass15MRlts4Threshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmRxPwrTpClass15MRlts4Threshold.setStatus("current")


class _PmRxPwrTpClass15MRlts5Threshold_Type(Integer32):
    """Custom type pmRxPwrTpClass15MRlts5Threshold based on Integer32"""
    defaultValue = 0


_PmRxPwrTpClass15MRlts5Threshold_Type.__name__ = "Integer32"
_PmRxPwrTpClass15MRlts5Threshold_Object = MibTableColumn
pmRxPwrTpClass15MRlts5Threshold = _PmRxPwrTpClass15MRlts5Threshold_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 24),
    _PmRxPwrTpClass15MRlts5Threshold_Type()
)
pmRxPwrTpClass15MRlts5Threshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmRxPwrTpClass15MRlts5Threshold.setStatus("current")


class _PmRxPwrTpClass24HRlts1Threshold_Type(Integer32):
    """Custom type pmRxPwrTpClass24HRlts1Threshold based on Integer32"""
    defaultValue = 0


_PmRxPwrTpClass24HRlts1Threshold_Type.__name__ = "Integer32"
_PmRxPwrTpClass24HRlts1Threshold_Object = MibTableColumn
pmRxPwrTpClass24HRlts1Threshold = _PmRxPwrTpClass24HRlts1Threshold_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 25),
    _PmRxPwrTpClass24HRlts1Threshold_Type()
)
pmRxPwrTpClass24HRlts1Threshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmRxPwrTpClass24HRlts1Threshold.setStatus("current")


class _PmRxPwrTpClass24HRlts2Threshold_Type(Integer32):
    """Custom type pmRxPwrTpClass24HRlts2Threshold based on Integer32"""
    defaultValue = 0


_PmRxPwrTpClass24HRlts2Threshold_Type.__name__ = "Integer32"
_PmRxPwrTpClass24HRlts2Threshold_Object = MibTableColumn
pmRxPwrTpClass24HRlts2Threshold = _PmRxPwrTpClass24HRlts2Threshold_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 26),
    _PmRxPwrTpClass24HRlts2Threshold_Type()
)
pmRxPwrTpClass24HRlts2Threshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmRxPwrTpClass24HRlts2Threshold.setStatus("current")


class _PmRxPwrTpClass24HRlts3Threshold_Type(Integer32):
    """Custom type pmRxPwrTpClass24HRlts3Threshold based on Integer32"""
    defaultValue = 0


_PmRxPwrTpClass24HRlts3Threshold_Type.__name__ = "Integer32"
_PmRxPwrTpClass24HRlts3Threshold_Object = MibTableColumn
pmRxPwrTpClass24HRlts3Threshold = _PmRxPwrTpClass24HRlts3Threshold_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 27),
    _PmRxPwrTpClass24HRlts3Threshold_Type()
)
pmRxPwrTpClass24HRlts3Threshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmRxPwrTpClass24HRlts3Threshold.setStatus("current")


class _PmRxPwrTpClass24HRlts4Threshold_Type(Integer32):
    """Custom type pmRxPwrTpClass24HRlts4Threshold based on Integer32"""
    defaultValue = 0


_PmRxPwrTpClass24HRlts4Threshold_Type.__name__ = "Integer32"
_PmRxPwrTpClass24HRlts4Threshold_Object = MibTableColumn
pmRxPwrTpClass24HRlts4Threshold = _PmRxPwrTpClass24HRlts4Threshold_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 28),
    _PmRxPwrTpClass24HRlts4Threshold_Type()
)
pmRxPwrTpClass24HRlts4Threshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmRxPwrTpClass24HRlts4Threshold.setStatus("current")


class _PmRxPwrTpClass24HRlts5Threshold_Type(Integer32):
    """Custom type pmRxPwrTpClass24HRlts5Threshold based on Integer32"""
    defaultValue = 0


_PmRxPwrTpClass24HRlts5Threshold_Type.__name__ = "Integer32"
_PmRxPwrTpClass24HRlts5Threshold_Object = MibTableColumn
pmRxPwrTpClass24HRlts5Threshold = _PmRxPwrTpClass24HRlts5Threshold_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 29),
    _PmRxPwrTpClass24HRlts5Threshold_Type()
)
pmRxPwrTpClass24HRlts5Threshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmRxPwrTpClass24HRlts5Threshold.setStatus("current")
_PmRxPwrTpClassRowStatus_Type = RowStatus
_PmRxPwrTpClassRowStatus_Object = MibTableColumn
pmRxPwrTpClassRowStatus = _PmRxPwrTpClassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 30),
    _PmRxPwrTpClassRowStatus_Type()
)
pmRxPwrTpClassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmRxPwrTpClassRowStatus.setStatus("current")
_PmRxPwrTpMaintTable_Object = MibTable
pmRxPwrTpMaintTable = _PmRxPwrTpMaintTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 12, 4)
)
if mibBuilder.loadTexts:
    pmRxPwrTpMaintTable.setStatus("current")
_PmRxPwrTpMaintRecord_Object = MibTableRow
pmRxPwrTpMaintRecord = _PmRxPwrTpMaintRecord_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 12, 4, 1)
)
pmRxPwrTpMaintRecord.setIndexNames(
    (0, "SIAE-PMRXPWR-MIB", "pmRxPwrTpClassBranchId"),
)
if mibBuilder.loadTexts:
    pmRxPwrTpMaintRecord.setStatus("current")


class _PmRxPwrTpMaintCounterClear_Type(Integer32):
    """Custom type pmRxPwrTpMaintCounterClear based on Integer32"""
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


_PmRxPwrTpMaintCounterClear_Type.__name__ = "Integer32"
_PmRxPwrTpMaintCounterClear_Object = MibTableColumn
pmRxPwrTpMaintCounterClear = _PmRxPwrTpMaintCounterClear_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 12, 4, 1, 1),
    _PmRxPwrTpMaintCounterClear_Type()
)
pmRxPwrTpMaintCounterClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmRxPwrTpMaintCounterClear.setStatus("current")


class _PmRxPwrTpMaintAlarmClear_Type(Integer32):
    """Custom type pmRxPwrTpMaintAlarmClear based on Integer32"""
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


_PmRxPwrTpMaintAlarmClear_Type.__name__ = "Integer32"
_PmRxPwrTpMaintAlarmClear_Object = MibTableColumn
pmRxPwrTpMaintAlarmClear = _PmRxPwrTpMaintAlarmClear_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 12, 4, 1, 2),
    _PmRxPwrTpMaintAlarmClear_Type()
)
pmRxPwrTpMaintAlarmClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmRxPwrTpMaintAlarmClear.setStatus("current")


class _PmRxPwrTpClass15MRltsAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type pmRxPwrTpClass15MRltsAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_PmRxPwrTpClass15MRltsAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_PmRxPwrTpClass15MRltsAlarmSeverityCode_Object = MibScalar
pmRxPwrTpClass15MRltsAlarmSeverityCode = _PmRxPwrTpClass15MRltsAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 12, 5),
    _PmRxPwrTpClass15MRltsAlarmSeverityCode_Type()
)
pmRxPwrTpClass15MRltsAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmRxPwrTpClass15MRltsAlarmSeverityCode.setStatus("current")


class _PmRxPwrTpClass24HRltsAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type pmRxPwrTpClass24HRltsAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_PmRxPwrTpClass24HRltsAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_PmRxPwrTpClass24HRltsAlarmSeverityCode_Object = MibScalar
pmRxPwrTpClass24HRltsAlarmSeverityCode = _PmRxPwrTpClass24HRltsAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 12, 6),
    _PmRxPwrTpClass24HRltsAlarmSeverityCode_Type()
)
pmRxPwrTpClass24HRltsAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmRxPwrTpClass24HRltsAlarmSeverityCode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SIAE-PMRXPWR-MIB",
    **{"pmRxPwr": pmRxPwr,
       "pmRxPwrMibVersion": pmRxPwrMibVersion,
       "pmRxPwrCounterTable": pmRxPwrCounterTable,
       "pmRxPwrCounterRecord": pmRxPwrCounterRecord,
       "pmRxPwrBranchId": pmRxPwrBranchId,
       "pmRxPwrCounterBlockId": pmRxPwrCounterBlockId,
       "pmRxPwrCounterBlockType": pmRxPwrCounterBlockType,
       "pmRxPwrCounterBlockStatus": pmRxPwrCounterBlockStatus,
       "pmRxPwrCounterTimeStamp": pmRxPwrCounterTimeStamp,
       "pmRxPwrRlts1Counter": pmRxPwrRlts1Counter,
       "pmRxPwrRlts2Counter": pmRxPwrRlts2Counter,
       "pmRxPwrRlts3Counter": pmRxPwrRlts3Counter,
       "pmRxPwrRlts4Counter": pmRxPwrRlts4Counter,
       "pmRxPwrRlts5Counter": pmRxPwrRlts5Counter,
       "pmRxPwrTMMax": pmRxPwrTMMax,
       "pmRxPwrTMMin": pmRxPwrTMMin,
       "pmRxPwrAverageRxLevel": pmRxPwrAverageRxLevel,
       "pmRxPwrTpClassTable": pmRxPwrTpClassTable,
       "pmRxPwrTpClassRecord": pmRxPwrTpClassRecord,
       "pmRxPwrTpClassBranchId": pmRxPwrTpClassBranchId,
       "pmRxPwrTpClassStartStop": pmRxPwrTpClassStartStop,
       "pmRxPwrTpClassLabel": pmRxPwrTpClassLabel,
       "pmRxPwrTpClassTimeStamp": pmRxPwrTpClassTimeStamp,
       "pmRxPwrTpClass15MRlts1Alarm": pmRxPwrTpClass15MRlts1Alarm,
       "pmRxPwrTpClass15MRlts2Alarm": pmRxPwrTpClass15MRlts2Alarm,
       "pmRxPwrTpClass15MRlts3Alarm": pmRxPwrTpClass15MRlts3Alarm,
       "pmRxPwrTpClass15MRlts4Alarm": pmRxPwrTpClass15MRlts4Alarm,
       "pmRxPwrTpClass15MRlts5Alarm": pmRxPwrTpClass15MRlts5Alarm,
       "pmRxPwrTpClass24HRlts1Alarm": pmRxPwrTpClass24HRlts1Alarm,
       "pmRxPwrTpClass24HRlts2Alarm": pmRxPwrTpClass24HRlts2Alarm,
       "pmRxPwrTpClass24HRlts3Alarm": pmRxPwrTpClass24HRlts3Alarm,
       "pmRxPwrTpClass24HRlts4Alarm": pmRxPwrTpClass24HRlts4Alarm,
       "pmRxPwrTpClass24HRlts5Alarm": pmRxPwrTpClass24HRlts5Alarm,
       "pmRxPwrTpClassRlt1Threshold": pmRxPwrTpClassRlt1Threshold,
       "pmRxPwrTpClassRlt2Threshold": pmRxPwrTpClassRlt2Threshold,
       "pmRxPwrTpClassRlt3Threshold": pmRxPwrTpClassRlt3Threshold,
       "pmRxPwrTpClassRlt4Threshold": pmRxPwrTpClassRlt4Threshold,
       "pmRxPwrTpClassRlt5Threshold": pmRxPwrTpClassRlt5Threshold,
       "pmRxPwrTpClass15MRlts1Threshold": pmRxPwrTpClass15MRlts1Threshold,
       "pmRxPwrTpClass15MRlts2Threshold": pmRxPwrTpClass15MRlts2Threshold,
       "pmRxPwrTpClass15MRlts3Threshold": pmRxPwrTpClass15MRlts3Threshold,
       "pmRxPwrTpClass15MRlts4Threshold": pmRxPwrTpClass15MRlts4Threshold,
       "pmRxPwrTpClass15MRlts5Threshold": pmRxPwrTpClass15MRlts5Threshold,
       "pmRxPwrTpClass24HRlts1Threshold": pmRxPwrTpClass24HRlts1Threshold,
       "pmRxPwrTpClass24HRlts2Threshold": pmRxPwrTpClass24HRlts2Threshold,
       "pmRxPwrTpClass24HRlts3Threshold": pmRxPwrTpClass24HRlts3Threshold,
       "pmRxPwrTpClass24HRlts4Threshold": pmRxPwrTpClass24HRlts4Threshold,
       "pmRxPwrTpClass24HRlts5Threshold": pmRxPwrTpClass24HRlts5Threshold,
       "pmRxPwrTpClassRowStatus": pmRxPwrTpClassRowStatus,
       "pmRxPwrTpMaintTable": pmRxPwrTpMaintTable,
       "pmRxPwrTpMaintRecord": pmRxPwrTpMaintRecord,
       "pmRxPwrTpMaintCounterClear": pmRxPwrTpMaintCounterClear,
       "pmRxPwrTpMaintAlarmClear": pmRxPwrTpMaintAlarmClear,
       "pmRxPwrTpClass15MRltsAlarmSeverityCode": pmRxPwrTpClass15MRltsAlarmSeverityCode,
       "pmRxPwrTpClass24HRltsAlarmSeverityCode": pmRxPwrTpClass24HRltsAlarmSeverityCode}
)
