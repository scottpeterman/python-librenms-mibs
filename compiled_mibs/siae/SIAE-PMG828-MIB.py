# SNMP MIB module (SIAE-PMG828-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\siae\SIAE-PMG828-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:27:15 2025
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

pmG828 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 11)
)
if mibBuilder.loadTexts:
    pmG828.setRevisions(
        ("2014-10-07 00:00",
         "2014-02-03 00:00",
         "2013-04-16 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _PmG828MibVersion_Type(Integer32):
    """Custom type pmG828MibVersion based on Integer32"""
    defaultValue = 1


_PmG828MibVersion_Type.__name__ = "Integer32"
_PmG828MibVersion_Object = MibScalar
pmG828MibVersion = _PmG828MibVersion_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 11, 1),
    _PmG828MibVersion_Type()
)
pmG828MibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmG828MibVersion.setStatus("current")
_PmG828CounterTable_Object = MibTable
pmG828CounterTable = _PmG828CounterTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 11, 2)
)
if mibBuilder.loadTexts:
    pmG828CounterTable.setStatus("current")
_PmG828CounterRecord_Object = MibTableRow
pmG828CounterRecord = _PmG828CounterRecord_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 11, 2, 1)
)
pmG828CounterRecord.setIndexNames(
    (0, "SIAE-PMG828-MIB", "pmG828TPointId"),
    (0, "SIAE-PMG828-MIB", "pmG828CounterBlockId"),
)
if mibBuilder.loadTexts:
    pmG828CounterRecord.setStatus("current")
_PmG828TPointId_Type = Integer32
_PmG828TPointId_Object = MibTableColumn
pmG828TPointId = _PmG828TPointId_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 11, 2, 1, 1),
    _PmG828TPointId_Type()
)
pmG828TPointId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmG828TPointId.setStatus("current")
_PmG828CounterBlockId_Type = Integer32
_PmG828CounterBlockId_Object = MibTableColumn
pmG828CounterBlockId = _PmG828CounterBlockId_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 11, 2, 1, 2),
    _PmG828CounterBlockId_Type()
)
pmG828CounterBlockId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmG828CounterBlockId.setStatus("current")


class _PmG828CounterBlockType_Type(Integer32):
    """Custom type pmG828CounterBlockType based on Integer32"""
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


_PmG828CounterBlockType_Type.__name__ = "Integer32"
_PmG828CounterBlockType_Object = MibTableColumn
pmG828CounterBlockType = _PmG828CounterBlockType_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 11, 2, 1, 3),
    _PmG828CounterBlockType_Type()
)
pmG828CounterBlockType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmG828CounterBlockType.setStatus("current")


class _PmG828CounterBlockStatus_Type(Integer32):
    """Custom type pmG828CounterBlockStatus based on Integer32"""
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


_PmG828CounterBlockStatus_Type.__name__ = "Integer32"
_PmG828CounterBlockStatus_Object = MibTableColumn
pmG828CounterBlockStatus = _PmG828CounterBlockStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 11, 2, 1, 4),
    _PmG828CounterBlockStatus_Type()
)
pmG828CounterBlockStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmG828CounterBlockStatus.setStatus("current")
_PmG828CounterTimeStamp_Type = Unsigned32
_PmG828CounterTimeStamp_Object = MibTableColumn
pmG828CounterTimeStamp = _PmG828CounterTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 11, 2, 1, 5),
    _PmG828CounterTimeStamp_Type()
)
pmG828CounterTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmG828CounterTimeStamp.setStatus("current")
_PmG828BBECounter_Type = Counter32
_PmG828BBECounter_Object = MibTableColumn
pmG828BBECounter = _PmG828BBECounter_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 11, 2, 1, 6),
    _PmG828BBECounter_Type()
)
pmG828BBECounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmG828BBECounter.setStatus("current")
_PmG828ESCounter_Type = Counter32
_PmG828ESCounter_Object = MibTableColumn
pmG828ESCounter = _PmG828ESCounter_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 11, 2, 1, 7),
    _PmG828ESCounter_Type()
)
pmG828ESCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmG828ESCounter.setStatus("current")
_PmG828SESCounter_Type = Counter32
_PmG828SESCounter_Object = MibTableColumn
pmG828SESCounter = _PmG828SESCounter_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 11, 2, 1, 8),
    _PmG828SESCounter_Type()
)
pmG828SESCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmG828SESCounter.setStatus("current")
_PmG828UASCounter_Type = Counter32
_PmG828UASCounter_Object = MibTableColumn
pmG828UASCounter = _PmG828UASCounter_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 11, 2, 1, 9),
    _PmG828UASCounter_Type()
)
pmG828UASCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmG828UASCounter.setStatus("current")
_PmG828SEPCounter_Type = Counter32
_PmG828SEPCounter_Object = MibTableColumn
pmG828SEPCounter = _PmG828SEPCounter_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 11, 2, 1, 10),
    _PmG828SEPCounter_Type()
)
pmG828SEPCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmG828SEPCounter.setStatus("current")
_PmG828TpClassTable_Object = MibTable
pmG828TpClassTable = _PmG828TpClassTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3)
)
if mibBuilder.loadTexts:
    pmG828TpClassTable.setStatus("current")
_PmG828TpClassRecord_Object = MibTableRow
pmG828TpClassRecord = _PmG828TpClassRecord_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3, 1)
)
pmG828TpClassRecord.setIndexNames(
    (0, "SIAE-PMG828-MIB", "pmG828TpClassId"),
)
if mibBuilder.loadTexts:
    pmG828TpClassRecord.setStatus("current")
_PmG828TpClassId_Type = Integer32
_PmG828TpClassId_Object = MibTableColumn
pmG828TpClassId = _PmG828TpClassId_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3, 1, 1),
    _PmG828TpClassId_Type()
)
pmG828TpClassId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmG828TpClassId.setStatus("current")


class _PmG828TpClassStartStop_Type(Integer32):
    """Custom type pmG828TpClassStartStop based on Integer32"""
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


_PmG828TpClassStartStop_Type.__name__ = "Integer32"
_PmG828TpClassStartStop_Object = MibTableColumn
pmG828TpClassStartStop = _PmG828TpClassStartStop_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3, 1, 2),
    _PmG828TpClassStartStop_Type()
)
pmG828TpClassStartStop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmG828TpClassStartStop.setStatus("current")


class _PmG828TpClassLabel_Type(DisplayString):
    """Custom type pmG828TpClassLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PmG828TpClassLabel_Type.__name__ = "DisplayString"
_PmG828TpClassLabel_Object = MibTableColumn
pmG828TpClassLabel = _PmG828TpClassLabel_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3, 1, 3),
    _PmG828TpClassLabel_Type()
)
pmG828TpClassLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmG828TpClassLabel.setStatus("current")
_PmG828TpClassTimeStamp_Type = Unsigned32
_PmG828TpClassTimeStamp_Object = MibTableColumn
pmG828TpClassTimeStamp = _PmG828TpClassTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3, 1, 4),
    _PmG828TpClassTimeStamp_Type()
)
pmG828TpClassTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmG828TpClassTimeStamp.setStatus("current")
_PmG828TpClass15MEsAlarm_Type = AlarmStatus
_PmG828TpClass15MEsAlarm_Object = MibTableColumn
pmG828TpClass15MEsAlarm = _PmG828TpClass15MEsAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3, 1, 5),
    _PmG828TpClass15MEsAlarm_Type()
)
pmG828TpClass15MEsAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmG828TpClass15MEsAlarm.setStatus("current")
_PmG828TpClass15MSesAlarm_Type = AlarmStatus
_PmG828TpClass15MSesAlarm_Object = MibTableColumn
pmG828TpClass15MSesAlarm = _PmG828TpClass15MSesAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3, 1, 6),
    _PmG828TpClass15MSesAlarm_Type()
)
pmG828TpClass15MSesAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmG828TpClass15MSesAlarm.setStatus("current")
_PmG828TpClass15MSepAlarm_Type = AlarmStatus
_PmG828TpClass15MSepAlarm_Object = MibTableColumn
pmG828TpClass15MSepAlarm = _PmG828TpClass15MSepAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3, 1, 7),
    _PmG828TpClass15MSepAlarm_Type()
)
pmG828TpClass15MSepAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmG828TpClass15MSepAlarm.setStatus("current")
_PmG828TpClass24HEsAlarm_Type = AlarmStatus
_PmG828TpClass24HEsAlarm_Object = MibTableColumn
pmG828TpClass24HEsAlarm = _PmG828TpClass24HEsAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3, 1, 8),
    _PmG828TpClass24HEsAlarm_Type()
)
pmG828TpClass24HEsAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmG828TpClass24HEsAlarm.setStatus("current")
_PmG828TpClass24HSesAlarm_Type = AlarmStatus
_PmG828TpClass24HSesAlarm_Object = MibTableColumn
pmG828TpClass24HSesAlarm = _PmG828TpClass24HSesAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3, 1, 9),
    _PmG828TpClass24HSesAlarm_Type()
)
pmG828TpClass24HSesAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmG828TpClass24HSesAlarm.setStatus("current")
_PmG828TpClass24HSepAlarm_Type = AlarmStatus
_PmG828TpClass24HSepAlarm_Object = MibTableColumn
pmG828TpClass24HSepAlarm = _PmG828TpClass24HSepAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3, 1, 10),
    _PmG828TpClass24HSepAlarm_Type()
)
pmG828TpClass24HSepAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmG828TpClass24HSepAlarm.setStatus("current")
_PmG828TpClassUasAlarm_Type = AlarmStatus
_PmG828TpClassUasAlarm_Object = MibTableColumn
pmG828TpClassUasAlarm = _PmG828TpClassUasAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3, 1, 11),
    _PmG828TpClassUasAlarm_Type()
)
pmG828TpClassUasAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmG828TpClassUasAlarm.setStatus("current")


class _PmG828TpClass15MEsThreshold_Type(Integer32):
    """Custom type pmG828TpClass15MEsThreshold based on Integer32"""
    defaultValue = 0


_PmG828TpClass15MEsThreshold_Type.__name__ = "Integer32"
_PmG828TpClass15MEsThreshold_Object = MibTableColumn
pmG828TpClass15MEsThreshold = _PmG828TpClass15MEsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3, 1, 12),
    _PmG828TpClass15MEsThreshold_Type()
)
pmG828TpClass15MEsThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmG828TpClass15MEsThreshold.setStatus("current")


class _PmG828TpClass15MSesThreshold_Type(Integer32):
    """Custom type pmG828TpClass15MSesThreshold based on Integer32"""
    defaultValue = 0


_PmG828TpClass15MSesThreshold_Type.__name__ = "Integer32"
_PmG828TpClass15MSesThreshold_Object = MibTableColumn
pmG828TpClass15MSesThreshold = _PmG828TpClass15MSesThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3, 1, 13),
    _PmG828TpClass15MSesThreshold_Type()
)
pmG828TpClass15MSesThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmG828TpClass15MSesThreshold.setStatus("current")


class _PmG828TpClass15MSepThreshold_Type(Integer32):
    """Custom type pmG828TpClass15MSepThreshold based on Integer32"""
    defaultValue = 0


_PmG828TpClass15MSepThreshold_Type.__name__ = "Integer32"
_PmG828TpClass15MSepThreshold_Object = MibTableColumn
pmG828TpClass15MSepThreshold = _PmG828TpClass15MSepThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3, 1, 14),
    _PmG828TpClass15MSepThreshold_Type()
)
pmG828TpClass15MSepThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmG828TpClass15MSepThreshold.setStatus("current")


class _PmG828TpClass24HEsThreshold_Type(Integer32):
    """Custom type pmG828TpClass24HEsThreshold based on Integer32"""
    defaultValue = 0


_PmG828TpClass24HEsThreshold_Type.__name__ = "Integer32"
_PmG828TpClass24HEsThreshold_Object = MibTableColumn
pmG828TpClass24HEsThreshold = _PmG828TpClass24HEsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3, 1, 15),
    _PmG828TpClass24HEsThreshold_Type()
)
pmG828TpClass24HEsThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmG828TpClass24HEsThreshold.setStatus("current")


class _PmG828TpClass24HSesThreshold_Type(Integer32):
    """Custom type pmG828TpClass24HSesThreshold based on Integer32"""
    defaultValue = 0


_PmG828TpClass24HSesThreshold_Type.__name__ = "Integer32"
_PmG828TpClass24HSesThreshold_Object = MibTableColumn
pmG828TpClass24HSesThreshold = _PmG828TpClass24HSesThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3, 1, 16),
    _PmG828TpClass24HSesThreshold_Type()
)
pmG828TpClass24HSesThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmG828TpClass24HSesThreshold.setStatus("current")


class _PmG828TpClass24HSepThreshold_Type(Integer32):
    """Custom type pmG828TpClass24HSepThreshold based on Integer32"""
    defaultValue = 0


_PmG828TpClass24HSepThreshold_Type.__name__ = "Integer32"
_PmG828TpClass24HSepThreshold_Object = MibTableColumn
pmG828TpClass24HSepThreshold = _PmG828TpClass24HSepThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3, 1, 17),
    _PmG828TpClass24HSepThreshold_Type()
)
pmG828TpClass24HSepThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmG828TpClass24HSepThreshold.setStatus("current")
_PmG828TpClassRowStatus_Type = RowStatus
_PmG828TpClassRowStatus_Object = MibTableColumn
pmG828TpClassRowStatus = _PmG828TpClassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3, 1, 18),
    _PmG828TpClassRowStatus_Type()
)
pmG828TpClassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmG828TpClassRowStatus.setStatus("current")
_PmG828TpMaintTable_Object = MibTable
pmG828TpMaintTable = _PmG828TpMaintTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 11, 4)
)
if mibBuilder.loadTexts:
    pmG828TpMaintTable.setStatus("current")
_PmG828TpMaintRecord_Object = MibTableRow
pmG828TpMaintRecord = _PmG828TpMaintRecord_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 11, 4, 1)
)
pmG828TpMaintRecord.setIndexNames(
    (0, "SIAE-PMG828-MIB", "pmG828TpClassId"),
)
if mibBuilder.loadTexts:
    pmG828TpMaintRecord.setStatus("current")


class _PmG828TpMaintCounterClear_Type(Integer32):
    """Custom type pmG828TpMaintCounterClear based on Integer32"""
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


_PmG828TpMaintCounterClear_Type.__name__ = "Integer32"
_PmG828TpMaintCounterClear_Object = MibTableColumn
pmG828TpMaintCounterClear = _PmG828TpMaintCounterClear_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 11, 4, 1, 1),
    _PmG828TpMaintCounterClear_Type()
)
pmG828TpMaintCounterClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmG828TpMaintCounterClear.setStatus("current")


class _PmG828TpMaintAlarmClear_Type(Integer32):
    """Custom type pmG828TpMaintAlarmClear based on Integer32"""
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


_PmG828TpMaintAlarmClear_Type.__name__ = "Integer32"
_PmG828TpMaintAlarmClear_Object = MibTableColumn
pmG828TpMaintAlarmClear = _PmG828TpMaintAlarmClear_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 11, 4, 1, 2),
    _PmG828TpMaintAlarmClear_Type()
)
pmG828TpMaintAlarmClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmG828TpMaintAlarmClear.setStatus("current")


class _PmG828NSesSetUAS_Type(Integer32):
    """Custom type pmG828NSesSetUAS based on Integer32"""
    defaultValue = 10


_PmG828NSesSetUAS_Type.__name__ = "Integer32"
_PmG828NSesSetUAS_Object = MibScalar
pmG828NSesSetUAS = _PmG828NSesSetUAS_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 11, 5),
    _PmG828NSesSetUAS_Type()
)
pmG828NSesSetUAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmG828NSesSetUAS.setStatus("current")


class _PmG828NSesResetUAS_Type(Integer32):
    """Custom type pmG828NSesResetUAS based on Integer32"""
    defaultValue = 10


_PmG828NSesResetUAS_Type.__name__ = "Integer32"
_PmG828NSesResetUAS_Object = MibScalar
pmG828NSesResetUAS = _PmG828NSesResetUAS_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 11, 6),
    _PmG828NSesResetUAS_Type()
)
pmG828NSesResetUAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmG828NSesResetUAS.setStatus("current")


class _PmG828TpClass15MEsAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type pmG828TpClass15MEsAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_PmG828TpClass15MEsAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_PmG828TpClass15MEsAlarmSeverityCode_Object = MibScalar
pmG828TpClass15MEsAlarmSeverityCode = _PmG828TpClass15MEsAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 11, 7),
    _PmG828TpClass15MEsAlarmSeverityCode_Type()
)
pmG828TpClass15MEsAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmG828TpClass15MEsAlarmSeverityCode.setStatus("current")


class _PmG828TpClass15MSesAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type pmG828TpClass15MSesAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_PmG828TpClass15MSesAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_PmG828TpClass15MSesAlarmSeverityCode_Object = MibScalar
pmG828TpClass15MSesAlarmSeverityCode = _PmG828TpClass15MSesAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 11, 8),
    _PmG828TpClass15MSesAlarmSeverityCode_Type()
)
pmG828TpClass15MSesAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmG828TpClass15MSesAlarmSeverityCode.setStatus("current")


class _PmG828TpClass24HEsAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type pmG828TpClass24HEsAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_PmG828TpClass24HEsAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_PmG828TpClass24HEsAlarmSeverityCode_Object = MibScalar
pmG828TpClass24HEsAlarmSeverityCode = _PmG828TpClass24HEsAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 11, 9),
    _PmG828TpClass24HEsAlarmSeverityCode_Type()
)
pmG828TpClass24HEsAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmG828TpClass24HEsAlarmSeverityCode.setStatus("current")


class _PmG828TpClass24HSesAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type pmG828TpClass24HSesAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_PmG828TpClass24HSesAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_PmG828TpClass24HSesAlarmSeverityCode_Object = MibScalar
pmG828TpClass24HSesAlarmSeverityCode = _PmG828TpClass24HSesAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 11, 10),
    _PmG828TpClass24HSesAlarmSeverityCode_Type()
)
pmG828TpClass24HSesAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmG828TpClass24HSesAlarmSeverityCode.setStatus("current")


class _PmG828TpClassUASAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type pmG828TpClassUASAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_PmG828TpClassUASAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_PmG828TpClassUASAlarmSeverityCode_Object = MibScalar
pmG828TpClassUASAlarmSeverityCode = _PmG828TpClassUASAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 11, 11),
    _PmG828TpClassUASAlarmSeverityCode_Type()
)
pmG828TpClassUASAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmG828TpClassUASAlarmSeverityCode.setStatus("current")


class _PmG828TpClass15MSepAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type pmG828TpClass15MSepAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_PmG828TpClass15MSepAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_PmG828TpClass15MSepAlarmSeverityCode_Object = MibScalar
pmG828TpClass15MSepAlarmSeverityCode = _PmG828TpClass15MSepAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 11, 12),
    _PmG828TpClass15MSepAlarmSeverityCode_Type()
)
pmG828TpClass15MSepAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmG828TpClass15MSepAlarmSeverityCode.setStatus("current")


class _PmG828TpClass24HSepAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type pmG828TpClass24HSepAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_PmG828TpClass24HSepAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_PmG828TpClass24HSepAlarmSeverityCode_Object = MibScalar
pmG828TpClass24HSepAlarmSeverityCode = _PmG828TpClass24HSepAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 11, 13),
    _PmG828TpClass24HSepAlarmSeverityCode_Type()
)
pmG828TpClass24HSepAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmG828TpClass24HSepAlarmSeverityCode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SIAE-PMG828-MIB",
    **{"pmG828": pmG828,
       "pmG828MibVersion": pmG828MibVersion,
       "pmG828CounterTable": pmG828CounterTable,
       "pmG828CounterRecord": pmG828CounterRecord,
       "pmG828TPointId": pmG828TPointId,
       "pmG828CounterBlockId": pmG828CounterBlockId,
       "pmG828CounterBlockType": pmG828CounterBlockType,
       "pmG828CounterBlockStatus": pmG828CounterBlockStatus,
       "pmG828CounterTimeStamp": pmG828CounterTimeStamp,
       "pmG828BBECounter": pmG828BBECounter,
       "pmG828ESCounter": pmG828ESCounter,
       "pmG828SESCounter": pmG828SESCounter,
       "pmG828UASCounter": pmG828UASCounter,
       "pmG828SEPCounter": pmG828SEPCounter,
       "pmG828TpClassTable": pmG828TpClassTable,
       "pmG828TpClassRecord": pmG828TpClassRecord,
       "pmG828TpClassId": pmG828TpClassId,
       "pmG828TpClassStartStop": pmG828TpClassStartStop,
       "pmG828TpClassLabel": pmG828TpClassLabel,
       "pmG828TpClassTimeStamp": pmG828TpClassTimeStamp,
       "pmG828TpClass15MEsAlarm": pmG828TpClass15MEsAlarm,
       "pmG828TpClass15MSesAlarm": pmG828TpClass15MSesAlarm,
       "pmG828TpClass15MSepAlarm": pmG828TpClass15MSepAlarm,
       "pmG828TpClass24HEsAlarm": pmG828TpClass24HEsAlarm,
       "pmG828TpClass24HSesAlarm": pmG828TpClass24HSesAlarm,
       "pmG828TpClass24HSepAlarm": pmG828TpClass24HSepAlarm,
       "pmG828TpClassUasAlarm": pmG828TpClassUasAlarm,
       "pmG828TpClass15MEsThreshold": pmG828TpClass15MEsThreshold,
       "pmG828TpClass15MSesThreshold": pmG828TpClass15MSesThreshold,
       "pmG828TpClass15MSepThreshold": pmG828TpClass15MSepThreshold,
       "pmG828TpClass24HEsThreshold": pmG828TpClass24HEsThreshold,
       "pmG828TpClass24HSesThreshold": pmG828TpClass24HSesThreshold,
       "pmG828TpClass24HSepThreshold": pmG828TpClass24HSepThreshold,
       "pmG828TpClassRowStatus": pmG828TpClassRowStatus,
       "pmG828TpMaintTable": pmG828TpMaintTable,
       "pmG828TpMaintRecord": pmG828TpMaintRecord,
       "pmG828TpMaintCounterClear": pmG828TpMaintCounterClear,
       "pmG828TpMaintAlarmClear": pmG828TpMaintAlarmClear,
       "pmG828NSesSetUAS": pmG828NSesSetUAS,
       "pmG828NSesResetUAS": pmG828NSesResetUAS,
       "pmG828TpClass15MEsAlarmSeverityCode": pmG828TpClass15MEsAlarmSeverityCode,
       "pmG828TpClass15MSesAlarmSeverityCode": pmG828TpClass15MSesAlarmSeverityCode,
       "pmG828TpClass24HEsAlarmSeverityCode": pmG828TpClass24HEsAlarmSeverityCode,
       "pmG828TpClass24HSesAlarmSeverityCode": pmG828TpClass24HSesAlarmSeverityCode,
       "pmG828TpClassUASAlarmSeverityCode": pmG828TpClassUASAlarmSeverityCode,
       "pmG828TpClass15MSepAlarmSeverityCode": pmG828TpClass15MSepAlarmSeverityCode,
       "pmG828TpClass24HSepAlarmSeverityCode": pmG828TpClass24HSepAlarmSeverityCode}
)
