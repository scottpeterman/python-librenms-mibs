# SNMP MIB module (SIAE-PMTXPWR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\siae\SIAE-PMTXPWR-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:27:20 2025
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

pmTxPwr = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 13)
)
if mibBuilder.loadTexts:
    pmTxPwr.setRevisions(
        ("2014-10-07 00:00",
         "2014-02-03 00:00",
         "2013-04-16 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _PmTxPwrMibVersion_Type(Integer32):
    """Custom type pmTxPwrMibVersion based on Integer32"""
    defaultValue = 1


_PmTxPwrMibVersion_Type.__name__ = "Integer32"
_PmTxPwrMibVersion_Object = MibScalar
pmTxPwrMibVersion = _PmTxPwrMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 13, 1),
    _PmTxPwrMibVersion_Type()
)
pmTxPwrMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTxPwrMibVersion.setStatus("current")
_PmTxPwrCounterTable_Object = MibTable
pmTxPwrCounterTable = _PmTxPwrCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 13, 2)
)
if mibBuilder.loadTexts:
    pmTxPwrCounterTable.setStatus("current")
_PmTxPwrCounterRecord_Object = MibTableRow
pmTxPwrCounterRecord = _PmTxPwrCounterRecord_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 13, 2, 1)
)
pmTxPwrCounterRecord.setIndexNames(
    (0, "SIAE-PMTXPWR-MIB", "pmTxPwrBranchId"),
    (0, "SIAE-PMTXPWR-MIB", "pmTxPwrCounterBlockId"),
)
if mibBuilder.loadTexts:
    pmTxPwrCounterRecord.setStatus("current")
_PmTxPwrBranchId_Type = Integer32
_PmTxPwrBranchId_Object = MibTableColumn
pmTxPwrBranchId = _PmTxPwrBranchId_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 13, 2, 1, 1),
    _PmTxPwrBranchId_Type()
)
pmTxPwrBranchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTxPwrBranchId.setStatus("current")
_PmTxPwrCounterBlockId_Type = Integer32
_PmTxPwrCounterBlockId_Object = MibTableColumn
pmTxPwrCounterBlockId = _PmTxPwrCounterBlockId_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 13, 2, 1, 2),
    _PmTxPwrCounterBlockId_Type()
)
pmTxPwrCounterBlockId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTxPwrCounterBlockId.setStatus("current")


class _PmTxPwrCounterBlockType_Type(Integer32):
    """Custom type pmTxPwrCounterBlockType based on Integer32"""
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


_PmTxPwrCounterBlockType_Type.__name__ = "Integer32"
_PmTxPwrCounterBlockType_Object = MibTableColumn
pmTxPwrCounterBlockType = _PmTxPwrCounterBlockType_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 13, 2, 1, 3),
    _PmTxPwrCounterBlockType_Type()
)
pmTxPwrCounterBlockType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTxPwrCounterBlockType.setStatus("current")


class _PmTxPwrCounterBlockStatus_Type(Integer32):
    """Custom type pmTxPwrCounterBlockStatus based on Integer32"""
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


_PmTxPwrCounterBlockStatus_Type.__name__ = "Integer32"
_PmTxPwrCounterBlockStatus_Object = MibTableColumn
pmTxPwrCounterBlockStatus = _PmTxPwrCounterBlockStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 13, 2, 1, 4),
    _PmTxPwrCounterBlockStatus_Type()
)
pmTxPwrCounterBlockStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTxPwrCounterBlockStatus.setStatus("current")
_PmTxPwrCounterTimeStamp_Type = Unsigned32
_PmTxPwrCounterTimeStamp_Object = MibTableColumn
pmTxPwrCounterTimeStamp = _PmTxPwrCounterTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 13, 2, 1, 5),
    _PmTxPwrCounterTimeStamp_Type()
)
pmTxPwrCounterTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTxPwrCounterTimeStamp.setStatus("current")
_PmTxPwrTlts1Counter_Type = Counter32
_PmTxPwrTlts1Counter_Object = MibTableColumn
pmTxPwrTlts1Counter = _PmTxPwrTlts1Counter_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 13, 2, 1, 6),
    _PmTxPwrTlts1Counter_Type()
)
pmTxPwrTlts1Counter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTxPwrTlts1Counter.setStatus("current")
_PmTxPwrTlts2Counter_Type = Counter32
_PmTxPwrTlts2Counter_Object = MibTableColumn
pmTxPwrTlts2Counter = _PmTxPwrTlts2Counter_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 13, 2, 1, 7),
    _PmTxPwrTlts2Counter_Type()
)
pmTxPwrTlts2Counter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTxPwrTlts2Counter.setStatus("current")
_PmTxPwrTlts3Counter_Type = Counter32
_PmTxPwrTlts3Counter_Object = MibTableColumn
pmTxPwrTlts3Counter = _PmTxPwrTlts3Counter_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 13, 2, 1, 8),
    _PmTxPwrTlts3Counter_Type()
)
pmTxPwrTlts3Counter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTxPwrTlts3Counter.setStatus("current")
_PmTxPwrTlts4Counter_Type = Counter32
_PmTxPwrTlts4Counter_Object = MibTableColumn
pmTxPwrTlts4Counter = _PmTxPwrTlts4Counter_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 13, 2, 1, 9),
    _PmTxPwrTlts4Counter_Type()
)
pmTxPwrTlts4Counter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTxPwrTlts4Counter.setStatus("current")
_PmTxPwrTMMax_Type = Integer32
_PmTxPwrTMMax_Object = MibTableColumn
pmTxPwrTMMax = _PmTxPwrTMMax_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 13, 2, 1, 10),
    _PmTxPwrTMMax_Type()
)
pmTxPwrTMMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTxPwrTMMax.setStatus("current")
_PmTxPwrTMMin_Type = Integer32
_PmTxPwrTMMin_Object = MibTableColumn
pmTxPwrTMMin = _PmTxPwrTMMin_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 13, 2, 1, 11),
    _PmTxPwrTMMin_Type()
)
pmTxPwrTMMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTxPwrTMMin.setStatus("current")
_PmTxPwrAverageTxLevel_Type = Integer32
_PmTxPwrAverageTxLevel_Object = MibTableColumn
pmTxPwrAverageTxLevel = _PmTxPwrAverageTxLevel_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 13, 2, 1, 12),
    _PmTxPwrAverageTxLevel_Type()
)
pmTxPwrAverageTxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTxPwrAverageTxLevel.setStatus("current")
_PmTxPwrTpClassTable_Object = MibTable
pmTxPwrTpClassTable = _PmTxPwrTpClassTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3)
)
if mibBuilder.loadTexts:
    pmTxPwrTpClassTable.setStatus("current")
_PmTxPwrTpClassRecord_Object = MibTableRow
pmTxPwrTpClassRecord = _PmTxPwrTpClassRecord_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1)
)
pmTxPwrTpClassRecord.setIndexNames(
    (0, "SIAE-PMTXPWR-MIB", "pmTxPwrTpClassBranchId"),
)
if mibBuilder.loadTexts:
    pmTxPwrTpClassRecord.setStatus("current")
_PmTxPwrTpClassBranchId_Type = Integer32
_PmTxPwrTpClassBranchId_Object = MibTableColumn
pmTxPwrTpClassBranchId = _PmTxPwrTpClassBranchId_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 1),
    _PmTxPwrTpClassBranchId_Type()
)
pmTxPwrTpClassBranchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTxPwrTpClassBranchId.setStatus("current")


class _PmTxPwrTpClassStartStop_Type(Integer32):
    """Custom type pmTxPwrTpClassStartStop based on Integer32"""
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


_PmTxPwrTpClassStartStop_Type.__name__ = "Integer32"
_PmTxPwrTpClassStartStop_Object = MibTableColumn
pmTxPwrTpClassStartStop = _PmTxPwrTpClassStartStop_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 2),
    _PmTxPwrTpClassStartStop_Type()
)
pmTxPwrTpClassStartStop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmTxPwrTpClassStartStop.setStatus("current")


class _PmTxPwrTpClassLabel_Type(DisplayString):
    """Custom type pmTxPwrTpClassLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PmTxPwrTpClassLabel_Type.__name__ = "DisplayString"
_PmTxPwrTpClassLabel_Object = MibTableColumn
pmTxPwrTpClassLabel = _PmTxPwrTpClassLabel_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 3),
    _PmTxPwrTpClassLabel_Type()
)
pmTxPwrTpClassLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTxPwrTpClassLabel.setStatus("current")
_PmTxPwrTpClassTimeStamp_Type = Unsigned32
_PmTxPwrTpClassTimeStamp_Object = MibTableColumn
pmTxPwrTpClassTimeStamp = _PmTxPwrTpClassTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 4),
    _PmTxPwrTpClassTimeStamp_Type()
)
pmTxPwrTpClassTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTxPwrTpClassTimeStamp.setStatus("current")
_PmTxPwrTpClass15MTlts1Alarm_Type = AlarmStatus
_PmTxPwrTpClass15MTlts1Alarm_Object = MibTableColumn
pmTxPwrTpClass15MTlts1Alarm = _PmTxPwrTpClass15MTlts1Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 5),
    _PmTxPwrTpClass15MTlts1Alarm_Type()
)
pmTxPwrTpClass15MTlts1Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTxPwrTpClass15MTlts1Alarm.setStatus("current")
_PmTxPwrTpClass15MTlts2Alarm_Type = AlarmStatus
_PmTxPwrTpClass15MTlts2Alarm_Object = MibTableColumn
pmTxPwrTpClass15MTlts2Alarm = _PmTxPwrTpClass15MTlts2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 6),
    _PmTxPwrTpClass15MTlts2Alarm_Type()
)
pmTxPwrTpClass15MTlts2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTxPwrTpClass15MTlts2Alarm.setStatus("current")
_PmTxPwrTpClass15MTlts3Alarm_Type = AlarmStatus
_PmTxPwrTpClass15MTlts3Alarm_Object = MibTableColumn
pmTxPwrTpClass15MTlts3Alarm = _PmTxPwrTpClass15MTlts3Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 7),
    _PmTxPwrTpClass15MTlts3Alarm_Type()
)
pmTxPwrTpClass15MTlts3Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTxPwrTpClass15MTlts3Alarm.setStatus("current")
_PmTxPwrTpClass15MTlts4Alarm_Type = AlarmStatus
_PmTxPwrTpClass15MTlts4Alarm_Object = MibTableColumn
pmTxPwrTpClass15MTlts4Alarm = _PmTxPwrTpClass15MTlts4Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 8),
    _PmTxPwrTpClass15MTlts4Alarm_Type()
)
pmTxPwrTpClass15MTlts4Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTxPwrTpClass15MTlts4Alarm.setStatus("current")
_PmTxPwrTpClass24HTlts1Alarm_Type = AlarmStatus
_PmTxPwrTpClass24HTlts1Alarm_Object = MibTableColumn
pmTxPwrTpClass24HTlts1Alarm = _PmTxPwrTpClass24HTlts1Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 9),
    _PmTxPwrTpClass24HTlts1Alarm_Type()
)
pmTxPwrTpClass24HTlts1Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTxPwrTpClass24HTlts1Alarm.setStatus("current")
_PmTxPwrTpClass24HTlts2Alarm_Type = AlarmStatus
_PmTxPwrTpClass24HTlts2Alarm_Object = MibTableColumn
pmTxPwrTpClass24HTlts2Alarm = _PmTxPwrTpClass24HTlts2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 10),
    _PmTxPwrTpClass24HTlts2Alarm_Type()
)
pmTxPwrTpClass24HTlts2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTxPwrTpClass24HTlts2Alarm.setStatus("current")
_PmTxPwrTpClass24HTlts3Alarm_Type = AlarmStatus
_PmTxPwrTpClass24HTlts3Alarm_Object = MibTableColumn
pmTxPwrTpClass24HTlts3Alarm = _PmTxPwrTpClass24HTlts3Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 11),
    _PmTxPwrTpClass24HTlts3Alarm_Type()
)
pmTxPwrTpClass24HTlts3Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTxPwrTpClass24HTlts3Alarm.setStatus("current")
_PmTxPwrTpClass24HTlts4Alarm_Type = AlarmStatus
_PmTxPwrTpClass24HTlts4Alarm_Object = MibTableColumn
pmTxPwrTpClass24HTlts4Alarm = _PmTxPwrTpClass24HTlts4Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 12),
    _PmTxPwrTpClass24HTlts4Alarm_Type()
)
pmTxPwrTpClass24HTlts4Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmTxPwrTpClass24HTlts4Alarm.setStatus("current")


class _PmTxPwrTpClassTlt1Threshold_Type(Integer32):
    """Custom type pmTxPwrTpClassTlt1Threshold based on Integer32"""
    defaultValue = -30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, -20),
    )


_PmTxPwrTpClassTlt1Threshold_Type.__name__ = "Integer32"
_PmTxPwrTpClassTlt1Threshold_Object = MibTableColumn
pmTxPwrTpClassTlt1Threshold = _PmTxPwrTpClassTlt1Threshold_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 13),
    _PmTxPwrTpClassTlt1Threshold_Type()
)
pmTxPwrTpClassTlt1Threshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmTxPwrTpClassTlt1Threshold.setStatus("current")


class _PmTxPwrTpClassTlt2Threshold_Type(Integer32):
    """Custom type pmTxPwrTpClassTlt2Threshold based on Integer32"""
    defaultValue = -40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, -20),
    )


_PmTxPwrTpClassTlt2Threshold_Type.__name__ = "Integer32"
_PmTxPwrTpClassTlt2Threshold_Object = MibTableColumn
pmTxPwrTpClassTlt2Threshold = _PmTxPwrTpClassTlt2Threshold_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 14),
    _PmTxPwrTpClassTlt2Threshold_Type()
)
pmTxPwrTpClassTlt2Threshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmTxPwrTpClassTlt2Threshold.setStatus("current")


class _PmTxPwrTpClassTlt3Threshold_Type(Integer32):
    """Custom type pmTxPwrTpClassTlt3Threshold based on Integer32"""
    defaultValue = -50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, -20),
    )


_PmTxPwrTpClassTlt3Threshold_Type.__name__ = "Integer32"
_PmTxPwrTpClassTlt3Threshold_Object = MibTableColumn
pmTxPwrTpClassTlt3Threshold = _PmTxPwrTpClassTlt3Threshold_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 15),
    _PmTxPwrTpClassTlt3Threshold_Type()
)
pmTxPwrTpClassTlt3Threshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmTxPwrTpClassTlt3Threshold.setStatus("current")


class _PmTxPwrTpClassTlt4Threshold_Type(Integer32):
    """Custom type pmTxPwrTpClassTlt4Threshold based on Integer32"""
    defaultValue = -60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, -20),
    )


_PmTxPwrTpClassTlt4Threshold_Type.__name__ = "Integer32"
_PmTxPwrTpClassTlt4Threshold_Object = MibTableColumn
pmTxPwrTpClassTlt4Threshold = _PmTxPwrTpClassTlt4Threshold_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 16),
    _PmTxPwrTpClassTlt4Threshold_Type()
)
pmTxPwrTpClassTlt4Threshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmTxPwrTpClassTlt4Threshold.setStatus("current")


class _PmTxPwrTpClass15MTlts1Threshold_Type(Integer32):
    """Custom type pmTxPwrTpClass15MTlts1Threshold based on Integer32"""
    defaultValue = 0


_PmTxPwrTpClass15MTlts1Threshold_Type.__name__ = "Integer32"
_PmTxPwrTpClass15MTlts1Threshold_Object = MibTableColumn
pmTxPwrTpClass15MTlts1Threshold = _PmTxPwrTpClass15MTlts1Threshold_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 17),
    _PmTxPwrTpClass15MTlts1Threshold_Type()
)
pmTxPwrTpClass15MTlts1Threshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmTxPwrTpClass15MTlts1Threshold.setStatus("current")


class _PmTxPwrTpClass15MTlts2Threshold_Type(Integer32):
    """Custom type pmTxPwrTpClass15MTlts2Threshold based on Integer32"""
    defaultValue = 0


_PmTxPwrTpClass15MTlts2Threshold_Type.__name__ = "Integer32"
_PmTxPwrTpClass15MTlts2Threshold_Object = MibTableColumn
pmTxPwrTpClass15MTlts2Threshold = _PmTxPwrTpClass15MTlts2Threshold_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 18),
    _PmTxPwrTpClass15MTlts2Threshold_Type()
)
pmTxPwrTpClass15MTlts2Threshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmTxPwrTpClass15MTlts2Threshold.setStatus("current")


class _PmTxPwrTpClass15MTlts3Threshold_Type(Integer32):
    """Custom type pmTxPwrTpClass15MTlts3Threshold based on Integer32"""
    defaultValue = 0


_PmTxPwrTpClass15MTlts3Threshold_Type.__name__ = "Integer32"
_PmTxPwrTpClass15MTlts3Threshold_Object = MibTableColumn
pmTxPwrTpClass15MTlts3Threshold = _PmTxPwrTpClass15MTlts3Threshold_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 19),
    _PmTxPwrTpClass15MTlts3Threshold_Type()
)
pmTxPwrTpClass15MTlts3Threshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmTxPwrTpClass15MTlts3Threshold.setStatus("current")


class _PmTxPwrTpClass15MTlts4Threshold_Type(Integer32):
    """Custom type pmTxPwrTpClass15MTlts4Threshold based on Integer32"""
    defaultValue = 0


_PmTxPwrTpClass15MTlts4Threshold_Type.__name__ = "Integer32"
_PmTxPwrTpClass15MTlts4Threshold_Object = MibTableColumn
pmTxPwrTpClass15MTlts4Threshold = _PmTxPwrTpClass15MTlts4Threshold_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 20),
    _PmTxPwrTpClass15MTlts4Threshold_Type()
)
pmTxPwrTpClass15MTlts4Threshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmTxPwrTpClass15MTlts4Threshold.setStatus("current")


class _PmTxPwrTpClass24HTlts1Threshold_Type(Integer32):
    """Custom type pmTxPwrTpClass24HTlts1Threshold based on Integer32"""
    defaultValue = 0


_PmTxPwrTpClass24HTlts1Threshold_Type.__name__ = "Integer32"
_PmTxPwrTpClass24HTlts1Threshold_Object = MibTableColumn
pmTxPwrTpClass24HTlts1Threshold = _PmTxPwrTpClass24HTlts1Threshold_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 21),
    _PmTxPwrTpClass24HTlts1Threshold_Type()
)
pmTxPwrTpClass24HTlts1Threshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmTxPwrTpClass24HTlts1Threshold.setStatus("current")


class _PmTxPwrTpClass24HTlts2Threshold_Type(Integer32):
    """Custom type pmTxPwrTpClass24HTlts2Threshold based on Integer32"""
    defaultValue = 0


_PmTxPwrTpClass24HTlts2Threshold_Type.__name__ = "Integer32"
_PmTxPwrTpClass24HTlts2Threshold_Object = MibTableColumn
pmTxPwrTpClass24HTlts2Threshold = _PmTxPwrTpClass24HTlts2Threshold_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 22),
    _PmTxPwrTpClass24HTlts2Threshold_Type()
)
pmTxPwrTpClass24HTlts2Threshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmTxPwrTpClass24HTlts2Threshold.setStatus("current")


class _PmTxPwrTpClass24HTlts3Threshold_Type(Integer32):
    """Custom type pmTxPwrTpClass24HTlts3Threshold based on Integer32"""
    defaultValue = 0


_PmTxPwrTpClass24HTlts3Threshold_Type.__name__ = "Integer32"
_PmTxPwrTpClass24HTlts3Threshold_Object = MibTableColumn
pmTxPwrTpClass24HTlts3Threshold = _PmTxPwrTpClass24HTlts3Threshold_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 23),
    _PmTxPwrTpClass24HTlts3Threshold_Type()
)
pmTxPwrTpClass24HTlts3Threshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmTxPwrTpClass24HTlts3Threshold.setStatus("current")


class _PmTxPwrTpClass24HTlts4Threshold_Type(Integer32):
    """Custom type pmTxPwrTpClass24HTlts4Threshold based on Integer32"""
    defaultValue = 0


_PmTxPwrTpClass24HTlts4Threshold_Type.__name__ = "Integer32"
_PmTxPwrTpClass24HTlts4Threshold_Object = MibTableColumn
pmTxPwrTpClass24HTlts4Threshold = _PmTxPwrTpClass24HTlts4Threshold_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 24),
    _PmTxPwrTpClass24HTlts4Threshold_Type()
)
pmTxPwrTpClass24HTlts4Threshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmTxPwrTpClass24HTlts4Threshold.setStatus("current")
_PmTxPwrTpClassRowStatus_Type = RowStatus
_PmTxPwrTpClassRowStatus_Object = MibTableColumn
pmTxPwrTpClassRowStatus = _PmTxPwrTpClassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 25),
    _PmTxPwrTpClassRowStatus_Type()
)
pmTxPwrTpClassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmTxPwrTpClassRowStatus.setStatus("current")
_PmTxPwrTpMaintTable_Object = MibTable
pmTxPwrTpMaintTable = _PmTxPwrTpMaintTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 13, 4)
)
if mibBuilder.loadTexts:
    pmTxPwrTpMaintTable.setStatus("current")
_PmTxPwrTpMaintRecord_Object = MibTableRow
pmTxPwrTpMaintRecord = _PmTxPwrTpMaintRecord_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 13, 4, 1)
)
pmTxPwrTpMaintRecord.setIndexNames(
    (0, "SIAE-PMTXPWR-MIB", "pmTxPwrTpClassBranchId"),
)
if mibBuilder.loadTexts:
    pmTxPwrTpMaintRecord.setStatus("current")


class _PmTxPwrTpMaintCounterClear_Type(Integer32):
    """Custom type pmTxPwrTpMaintCounterClear based on Integer32"""
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


_PmTxPwrTpMaintCounterClear_Type.__name__ = "Integer32"
_PmTxPwrTpMaintCounterClear_Object = MibTableColumn
pmTxPwrTpMaintCounterClear = _PmTxPwrTpMaintCounterClear_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 13, 4, 1, 1),
    _PmTxPwrTpMaintCounterClear_Type()
)
pmTxPwrTpMaintCounterClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmTxPwrTpMaintCounterClear.setStatus("current")


class _PmTxPwrTpMaintAlarmClear_Type(Integer32):
    """Custom type pmTxPwrTpMaintAlarmClear based on Integer32"""
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


_PmTxPwrTpMaintAlarmClear_Type.__name__ = "Integer32"
_PmTxPwrTpMaintAlarmClear_Object = MibTableColumn
pmTxPwrTpMaintAlarmClear = _PmTxPwrTpMaintAlarmClear_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 13, 4, 1, 2),
    _PmTxPwrTpMaintAlarmClear_Type()
)
pmTxPwrTpMaintAlarmClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmTxPwrTpMaintAlarmClear.setStatus("current")


class _PmTxPwrTpClass15MTltsAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type pmTxPwrTpClass15MTltsAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_PmTxPwrTpClass15MTltsAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_PmTxPwrTpClass15MTltsAlarmSeverityCode_Object = MibScalar
pmTxPwrTpClass15MTltsAlarmSeverityCode = _PmTxPwrTpClass15MTltsAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 13, 5),
    _PmTxPwrTpClass15MTltsAlarmSeverityCode_Type()
)
pmTxPwrTpClass15MTltsAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmTxPwrTpClass15MTltsAlarmSeverityCode.setStatus("current")


class _PmTxPwrTpClass24HTltsAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type pmTxPwrTpClass24HTltsAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_PmTxPwrTpClass24HTltsAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_PmTxPwrTpClass24HTltsAlarmSeverityCode_Object = MibScalar
pmTxPwrTpClass24HTltsAlarmSeverityCode = _PmTxPwrTpClass24HTltsAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 13, 6),
    _PmTxPwrTpClass24HTltsAlarmSeverityCode_Type()
)
pmTxPwrTpClass24HTltsAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmTxPwrTpClass24HTltsAlarmSeverityCode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SIAE-PMTXPWR-MIB",
    **{"pmTxPwr": pmTxPwr,
       "pmTxPwrMibVersion": pmTxPwrMibVersion,
       "pmTxPwrCounterTable": pmTxPwrCounterTable,
       "pmTxPwrCounterRecord": pmTxPwrCounterRecord,
       "pmTxPwrBranchId": pmTxPwrBranchId,
       "pmTxPwrCounterBlockId": pmTxPwrCounterBlockId,
       "pmTxPwrCounterBlockType": pmTxPwrCounterBlockType,
       "pmTxPwrCounterBlockStatus": pmTxPwrCounterBlockStatus,
       "pmTxPwrCounterTimeStamp": pmTxPwrCounterTimeStamp,
       "pmTxPwrTlts1Counter": pmTxPwrTlts1Counter,
       "pmTxPwrTlts2Counter": pmTxPwrTlts2Counter,
       "pmTxPwrTlts3Counter": pmTxPwrTlts3Counter,
       "pmTxPwrTlts4Counter": pmTxPwrTlts4Counter,
       "pmTxPwrTMMax": pmTxPwrTMMax,
       "pmTxPwrTMMin": pmTxPwrTMMin,
       "pmTxPwrAverageTxLevel": pmTxPwrAverageTxLevel,
       "pmTxPwrTpClassTable": pmTxPwrTpClassTable,
       "pmTxPwrTpClassRecord": pmTxPwrTpClassRecord,
       "pmTxPwrTpClassBranchId": pmTxPwrTpClassBranchId,
       "pmTxPwrTpClassStartStop": pmTxPwrTpClassStartStop,
       "pmTxPwrTpClassLabel": pmTxPwrTpClassLabel,
       "pmTxPwrTpClassTimeStamp": pmTxPwrTpClassTimeStamp,
       "pmTxPwrTpClass15MTlts1Alarm": pmTxPwrTpClass15MTlts1Alarm,
       "pmTxPwrTpClass15MTlts2Alarm": pmTxPwrTpClass15MTlts2Alarm,
       "pmTxPwrTpClass15MTlts3Alarm": pmTxPwrTpClass15MTlts3Alarm,
       "pmTxPwrTpClass15MTlts4Alarm": pmTxPwrTpClass15MTlts4Alarm,
       "pmTxPwrTpClass24HTlts1Alarm": pmTxPwrTpClass24HTlts1Alarm,
       "pmTxPwrTpClass24HTlts2Alarm": pmTxPwrTpClass24HTlts2Alarm,
       "pmTxPwrTpClass24HTlts3Alarm": pmTxPwrTpClass24HTlts3Alarm,
       "pmTxPwrTpClass24HTlts4Alarm": pmTxPwrTpClass24HTlts4Alarm,
       "pmTxPwrTpClassTlt1Threshold": pmTxPwrTpClassTlt1Threshold,
       "pmTxPwrTpClassTlt2Threshold": pmTxPwrTpClassTlt2Threshold,
       "pmTxPwrTpClassTlt3Threshold": pmTxPwrTpClassTlt3Threshold,
       "pmTxPwrTpClassTlt4Threshold": pmTxPwrTpClassTlt4Threshold,
       "pmTxPwrTpClass15MTlts1Threshold": pmTxPwrTpClass15MTlts1Threshold,
       "pmTxPwrTpClass15MTlts2Threshold": pmTxPwrTpClass15MTlts2Threshold,
       "pmTxPwrTpClass15MTlts3Threshold": pmTxPwrTpClass15MTlts3Threshold,
       "pmTxPwrTpClass15MTlts4Threshold": pmTxPwrTpClass15MTlts4Threshold,
       "pmTxPwrTpClass24HTlts1Threshold": pmTxPwrTpClass24HTlts1Threshold,
       "pmTxPwrTpClass24HTlts2Threshold": pmTxPwrTpClass24HTlts2Threshold,
       "pmTxPwrTpClass24HTlts3Threshold": pmTxPwrTpClass24HTlts3Threshold,
       "pmTxPwrTpClass24HTlts4Threshold": pmTxPwrTpClass24HTlts4Threshold,
       "pmTxPwrTpClassRowStatus": pmTxPwrTpClassRowStatus,
       "pmTxPwrTpMaintTable": pmTxPwrTpMaintTable,
       "pmTxPwrTpMaintRecord": pmTxPwrTpMaintRecord,
       "pmTxPwrTpMaintCounterClear": pmTxPwrTpMaintCounterClear,
       "pmTxPwrTpMaintAlarmClear": pmTxPwrTpMaintAlarmClear,
       "pmTxPwrTpClass15MTltsAlarmSeverityCode": pmTxPwrTpClass15MTltsAlarmSeverityCode,
       "pmTxPwrTpClass24HTltsAlarmSeverityCode": pmTxPwrTpClass24HTltsAlarmSeverityCode}
)
