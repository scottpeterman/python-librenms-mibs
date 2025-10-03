# SNMP MIB module (SIAE-SYNC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\siae\SIAE-SYNC-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:27:47 2025
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

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifIndex")

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

sync = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28)
)
if mibBuilder.loadTexts:
    sync.setRevisions(
        ("2014-04-02 00:00",
         "2014-02-17 00:00",
         "2014-02-03 00:00",
         "2013-04-16 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _SyncMibVersion_Type(Integer32):
    """Custom type syncMibVersion based on Integer32"""
    defaultValue = 1


_SyncMibVersion_Type.__name__ = "Integer32"
_SyncMibVersion_Object = MibScalar
syncMibVersion = _SyncMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 1),
    _SyncMibVersion_Type()
)
syncMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncMibVersion.setStatus("current")
_TimingGeneratorTable_Object = MibTable
timingGeneratorTable = _TimingGeneratorTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 2)
)
if mibBuilder.loadTexts:
    timingGeneratorTable.setStatus("current")
_TimingGeneratorRecord_Object = MibTableRow
timingGeneratorRecord = _TimingGeneratorRecord_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 2, 1)
)
timingGeneratorRecord.setIndexNames(
    (0, "SIAE-SYNC-MIB", "timingGeneratorId"),
)
if mibBuilder.loadTexts:
    timingGeneratorRecord.setStatus("current")
_TimingGeneratorId_Type = Integer32
_TimingGeneratorId_Object = MibTableColumn
timingGeneratorId = _TimingGeneratorId_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 2, 1, 1),
    _TimingGeneratorId_Type()
)
timingGeneratorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timingGeneratorId.setStatus("current")


class _TimingGeneratorT4vsT0_Type(Integer32):
    """Custom type timingGeneratorT4vsT0 based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("t4NotEqualT0", 1),
          ("t4EqualT0", 2))
    )


_TimingGeneratorT4vsT0_Type.__name__ = "Integer32"
_TimingGeneratorT4vsT0_Object = MibTableColumn
timingGeneratorT4vsT0 = _TimingGeneratorT4vsT0_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 2, 1, 2),
    _TimingGeneratorT4vsT0_Type()
)
timingGeneratorT4vsT0.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timingGeneratorT4vsT0.setStatus("current")


class _TimingGeneratorHoldOffTime_Type(Integer32):
    """Custom type timingGeneratorHoldOffTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 1800),
    )


_TimingGeneratorHoldOffTime_Type.__name__ = "Integer32"
_TimingGeneratorHoldOffTime_Object = MibTableColumn
timingGeneratorHoldOffTime = _TimingGeneratorHoldOffTime_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 2, 1, 3),
    _TimingGeneratorHoldOffTime_Type()
)
timingGeneratorHoldOffTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timingGeneratorHoldOffTime.setStatus("current")


class _TimingGeneratorWtrTime_Type(Integer32):
    """Custom type timingGeneratorWtrTime based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_TimingGeneratorWtrTime_Type.__name__ = "Integer32"
_TimingGeneratorWtrTime_Object = MibTableColumn
timingGeneratorWtrTime = _TimingGeneratorWtrTime_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 2, 1, 4),
    _TimingGeneratorWtrTime_Type()
)
timingGeneratorWtrTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timingGeneratorWtrTime.setStatus("current")


class _TimingGeneratorSinkLosSet_Type(Integer32):
    """Custom type timingGeneratorSinkLosSet based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_TimingGeneratorSinkLosSet_Type.__name__ = "Integer32"
_TimingGeneratorSinkLosSet_Object = MibTableColumn
timingGeneratorSinkLosSet = _TimingGeneratorSinkLosSet_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 2, 1, 5),
    _TimingGeneratorSinkLosSet_Type()
)
timingGeneratorSinkLosSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timingGeneratorSinkLosSet.setStatus("current")


class _TimingGeneratorSinkLosReset_Type(Integer32):
    """Custom type timingGeneratorSinkLosReset based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_TimingGeneratorSinkLosReset_Type.__name__ = "Integer32"
_TimingGeneratorSinkLosReset_Object = MibTableColumn
timingGeneratorSinkLosReset = _TimingGeneratorSinkLosReset_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 2, 1, 6),
    _TimingGeneratorSinkLosReset_Type()
)
timingGeneratorSinkLosReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timingGeneratorSinkLosReset.setStatus("current")
_TimingGeneratorT0SquelchAlarm_Type = AlarmStatus
_TimingGeneratorT0SquelchAlarm_Object = MibTableColumn
timingGeneratorT0SquelchAlarm = _TimingGeneratorT0SquelchAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 2, 1, 7),
    _TimingGeneratorT0SquelchAlarm_Type()
)
timingGeneratorT0SquelchAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timingGeneratorT0SquelchAlarm.setStatus("current")
_TimingGeneratorT4SquelchAlarm_Type = AlarmStatus
_TimingGeneratorT4SquelchAlarm_Object = MibTableColumn
timingGeneratorT4SquelchAlarm = _TimingGeneratorT4SquelchAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 2, 1, 8),
    _TimingGeneratorT4SquelchAlarm_Type()
)
timingGeneratorT4SquelchAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timingGeneratorT4SquelchAlarm.setStatus("current")
_TimingGeneratorFreeRunningStatus_Type = AlarmStatus
_TimingGeneratorFreeRunningStatus_Object = MibTableColumn
timingGeneratorFreeRunningStatus = _TimingGeneratorFreeRunningStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 2, 1, 9),
    _TimingGeneratorFreeRunningStatus_Type()
)
timingGeneratorFreeRunningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timingGeneratorFreeRunningStatus.setStatus("current")
_TimingGeneratorHoldoverStatus_Type = AlarmStatus
_TimingGeneratorHoldoverStatus_Object = MibTableColumn
timingGeneratorHoldoverStatus = _TimingGeneratorHoldoverStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 2, 1, 10),
    _TimingGeneratorHoldoverStatus_Type()
)
timingGeneratorHoldoverStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timingGeneratorHoldoverStatus.setStatus("current")


class _TimingGeneratorActiveStatus_Type(Integer32):
    """Custom type timingGeneratorActiveStatus based on Integer32"""
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


_TimingGeneratorActiveStatus_Type.__name__ = "Integer32"
_TimingGeneratorActiveStatus_Object = MibTableColumn
timingGeneratorActiveStatus = _TimingGeneratorActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 2, 1, 11),
    _TimingGeneratorActiveStatus_Type()
)
timingGeneratorActiveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timingGeneratorActiveStatus.setStatus("current")


class _TimingGeneratorT0CurrentQuality_Type(Integer32):
    """Custom type timingGeneratorT0CurrentQuality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              4,
              8,
              11,
              15)
        )
    )
    namedValues = NamedValues(
        *(("qUNKN", 0),
          ("qPRC", 2),
          ("qSSUT", 4),
          ("qSSUL", 8),
          ("qSEC", 11),
          ("qDNU", 15))
    )


_TimingGeneratorT0CurrentQuality_Type.__name__ = "Integer32"
_TimingGeneratorT0CurrentQuality_Object = MibTableColumn
timingGeneratorT0CurrentQuality = _TimingGeneratorT0CurrentQuality_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 2, 1, 12),
    _TimingGeneratorT0CurrentQuality_Type()
)
timingGeneratorT0CurrentQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timingGeneratorT0CurrentQuality.setStatus("current")


class _TimingGeneratorT4CurrentQuality_Type(Integer32):
    """Custom type timingGeneratorT4CurrentQuality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              4,
              8,
              11,
              15)
        )
    )
    namedValues = NamedValues(
        *(("qUNKN", 0),
          ("qPRC", 2),
          ("qSSUT", 4),
          ("qSSUL", 8),
          ("qSEC", 11),
          ("qDNU", 15))
    )


_TimingGeneratorT4CurrentQuality_Type.__name__ = "Integer32"
_TimingGeneratorT4CurrentQuality_Object = MibTableColumn
timingGeneratorT4CurrentQuality = _TimingGeneratorT4CurrentQuality_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 2, 1, 13),
    _TimingGeneratorT4CurrentQuality_Type()
)
timingGeneratorT4CurrentQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timingGeneratorT4CurrentQuality.setStatus("current")


class _TimingGeneratorT4MinimumQuality_Type(Integer32):
    """Custom type timingGeneratorT4MinimumQuality based on Integer32"""
    defaultValue = 11

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              8,
              11)
        )
    )
    namedValues = NamedValues(
        *(("qPRC", 2),
          ("qSSUT", 4),
          ("qSSUL", 8),
          ("qSEC", 11))
    )


_TimingGeneratorT4MinimumQuality_Type.__name__ = "Integer32"
_TimingGeneratorT4MinimumQuality_Object = MibTableColumn
timingGeneratorT4MinimumQuality = _TimingGeneratorT4MinimumQuality_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 2, 1, 14),
    _TimingGeneratorT4MinimumQuality_Type()
)
timingGeneratorT4MinimumQuality.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timingGeneratorT4MinimumQuality.setStatus("current")
_TimingGeneratorT0PreferredSource_Type = ObjectIdentifier
_TimingGeneratorT0PreferredSource_Object = MibTableColumn
timingGeneratorT0PreferredSource = _TimingGeneratorT0PreferredSource_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 2, 1, 15),
    _TimingGeneratorT0PreferredSource_Type()
)
timingGeneratorT0PreferredSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timingGeneratorT0PreferredSource.setStatus("current")
_TimingGeneratorT4PreferredSource_Type = ObjectIdentifier
_TimingGeneratorT4PreferredSource_Object = MibTableColumn
timingGeneratorT4PreferredSource = _TimingGeneratorT4PreferredSource_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 2, 1, 16),
    _TimingGeneratorT4PreferredSource_Type()
)
timingGeneratorT4PreferredSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timingGeneratorT4PreferredSource.setStatus("current")
_TimingGeneratorRowStatus_Type = RowStatus
_TimingGeneratorRowStatus_Object = MibTableColumn
timingGeneratorRowStatus = _TimingGeneratorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 2, 1, 17),
    _TimingGeneratorRowStatus_Type()
)
timingGeneratorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timingGeneratorRowStatus.setStatus("current")
_TimingGeneratorMaintTable_Object = MibTable
timingGeneratorMaintTable = _TimingGeneratorMaintTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 3)
)
if mibBuilder.loadTexts:
    timingGeneratorMaintTable.setStatus("current")
_TimingGeneratorMaintRecord_Object = MibTableRow
timingGeneratorMaintRecord = _TimingGeneratorMaintRecord_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 3, 1)
)
timingGeneratorMaintRecord.setIndexNames(
    (0, "SIAE-SYNC-MIB", "timingGeneratorId"),
)
if mibBuilder.loadTexts:
    timingGeneratorMaintRecord.setStatus("current")


class _TimingGeneratorT4Squelch_Type(Integer32):
    """Custom type timingGeneratorT4Squelch based on Integer32"""
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


_TimingGeneratorT4Squelch_Type.__name__ = "Integer32"
_TimingGeneratorT4Squelch_Object = MibTableColumn
timingGeneratorT4Squelch = _TimingGeneratorT4Squelch_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 3, 1, 1),
    _TimingGeneratorT4Squelch_Type()
)
timingGeneratorT4Squelch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timingGeneratorT4Squelch.setStatus("current")


class _TimingGeneratorStatusControl_Type(Integer32):
    """Custom type timingGeneratorStatusControl based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("freerunning", 1),
          ("holdover", 2),
          ("locked", 3))
    )


_TimingGeneratorStatusControl_Type.__name__ = "Integer32"
_TimingGeneratorStatusControl_Object = MibTableColumn
timingGeneratorStatusControl = _TimingGeneratorStatusControl_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 3, 1, 2),
    _TimingGeneratorStatusControl_Type()
)
timingGeneratorStatusControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timingGeneratorStatusControl.setStatus("current")
_TimingGeneratorT0ForcedSource_Type = ObjectIdentifier
_TimingGeneratorT0ForcedSource_Object = MibTableColumn
timingGeneratorT0ForcedSource = _TimingGeneratorT0ForcedSource_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 3, 1, 3),
    _TimingGeneratorT0ForcedSource_Type()
)
timingGeneratorT0ForcedSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timingGeneratorT0ForcedSource.setStatus("current")
_TimingGeneratorT4ForcedSource_Type = ObjectIdentifier
_TimingGeneratorT4ForcedSource_Object = MibTableColumn
timingGeneratorT4ForcedSource = _TimingGeneratorT4ForcedSource_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 3, 1, 4),
    _TimingGeneratorT4ForcedSource_Type()
)
timingGeneratorT4ForcedSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timingGeneratorT4ForcedSource.setStatus("current")
_TimingGeneratorWtrClearSource_Type = ObjectIdentifier
_TimingGeneratorWtrClearSource_Object = MibTableColumn
timingGeneratorWtrClearSource = _TimingGeneratorWtrClearSource_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 3, 1, 5),
    _TimingGeneratorWtrClearSource_Type()
)
timingGeneratorWtrClearSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timingGeneratorWtrClearSource.setStatus("current")
_TimingSinkTable_Object = MibTable
timingSinkTable = _TimingSinkTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 4)
)
if mibBuilder.loadTexts:
    timingSinkTable.setStatus("current")
_TimingSinkRecord_Object = MibTableRow
timingSinkRecord = _TimingSinkRecord_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 4, 1)
)
timingSinkRecord.setIndexNames(
    (0, "SIAE-SYNC-MIB", "timingSinkGenId"),
    (0, "SIAE-SYNC-MIB", "timingSinkId"),
    (0, "SIAE-SYNC-MIB", "timingSinkType"),
)
if mibBuilder.loadTexts:
    timingSinkRecord.setStatus("current")
_TimingSinkGenId_Type = Integer32
_TimingSinkGenId_Object = MibTableColumn
timingSinkGenId = _TimingSinkGenId_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 4, 1, 1),
    _TimingSinkGenId_Type()
)
timingSinkGenId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timingSinkGenId.setStatus("current")
_TimingSinkId_Type = Integer32
_TimingSinkId_Object = MibTableColumn
timingSinkId = _TimingSinkId_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 4, 1, 2),
    _TimingSinkId_Type()
)
timingSinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timingSinkId.setStatus("current")


class _TimingSinkType_Type(Integer32):
    """Custom type timingSinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("t0", 1),
          ("t4", 2))
    )


_TimingSinkType_Type.__name__ = "Integer32"
_TimingSinkType_Object = MibTableColumn
timingSinkType = _TimingSinkType_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 4, 1, 3),
    _TimingSinkType_Type()
)
timingSinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timingSinkType.setStatus("current")
_TimingSinkIfIndex_Type = InterfaceIndexOrZero
_TimingSinkIfIndex_Object = MibTableColumn
timingSinkIfIndex = _TimingSinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 4, 1, 4),
    _TimingSinkIfIndex_Type()
)
timingSinkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timingSinkIfIndex.setStatus("current")
_TimingSinkSelector_Type = Integer32
_TimingSinkSelector_Object = MibTableColumn
timingSinkSelector = _TimingSinkSelector_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 4, 1, 5),
    _TimingSinkSelector_Type()
)
timingSinkSelector.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timingSinkSelector.setStatus("current")


class _TimingSinkPriority_Type(Integer32):
    """Custom type timingSinkPriority based on Integer32"""
    defaultValue = 16

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
              16)
        )
    )
    namedValues = NamedValues(
        *(("p1", 1),
          ("p2", 2),
          ("p3", 3),
          ("p4", 4),
          ("p5", 5),
          ("p6", 6),
          ("p7", 7),
          ("p8", 8),
          ("p9", 9),
          ("p10", 10),
          ("p11", 11),
          ("p12", 12),
          ("p13", 13),
          ("p14", 14),
          ("p15", 15),
          ("disable", 16))
    )


_TimingSinkPriority_Type.__name__ = "Integer32"
_TimingSinkPriority_Object = MibTableColumn
timingSinkPriority = _TimingSinkPriority_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 4, 1, 6),
    _TimingSinkPriority_Type()
)
timingSinkPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timingSinkPriority.setStatus("current")


class _TimingSinkLabel_Type(DisplayString):
    """Custom type timingSinkLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TimingSinkLabel_Type.__name__ = "DisplayString"
_TimingSinkLabel_Object = MibTableColumn
timingSinkLabel = _TimingSinkLabel_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 4, 1, 7),
    _TimingSinkLabel_Type()
)
timingSinkLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timingSinkLabel.setStatus("current")
_TimingSinkLosAlarm_Type = AlarmStatus
_TimingSinkLosAlarm_Object = MibTableColumn
timingSinkLosAlarm = _TimingSinkLosAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 4, 1, 8),
    _TimingSinkLosAlarm_Type()
)
timingSinkLosAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timingSinkLosAlarm.setStatus("current")
_TimingSinkDriftAlarm_Type = AlarmStatus
_TimingSinkDriftAlarm_Object = MibTableColumn
timingSinkDriftAlarm = _TimingSinkDriftAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 4, 1, 9),
    _TimingSinkDriftAlarm_Type()
)
timingSinkDriftAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timingSinkDriftAlarm.setStatus("current")


class _TimingSinkActiveStatus_Type(Integer32):
    """Custom type timingSinkActiveStatus based on Integer32"""
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


_TimingSinkActiveStatus_Type.__name__ = "Integer32"
_TimingSinkActiveStatus_Object = MibTableColumn
timingSinkActiveStatus = _TimingSinkActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 4, 1, 10),
    _TimingSinkActiveStatus_Type()
)
timingSinkActiveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timingSinkActiveStatus.setStatus("current")


class _TimingSinkCurrentQuality_Type(Integer32):
    """Custom type timingSinkCurrentQuality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              4,
              8,
              11,
              15)
        )
    )
    namedValues = NamedValues(
        *(("qUNKN", 0),
          ("qPRC", 2),
          ("qSSUT", 4),
          ("qSSUL", 8),
          ("qSEC", 11),
          ("qDNU", 15))
    )


_TimingSinkCurrentQuality_Type.__name__ = "Integer32"
_TimingSinkCurrentQuality_Object = MibTableColumn
timingSinkCurrentQuality = _TimingSinkCurrentQuality_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 4, 1, 11),
    _TimingSinkCurrentQuality_Type()
)
timingSinkCurrentQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timingSinkCurrentQuality.setStatus("current")


class _TimingSinkOverwriteTxQuality_Type(Integer32):
    """Custom type timingSinkOverwriteTxQuality based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              4,
              8,
              11,
              15)
        )
    )
    namedValues = NamedValues(
        *(("noOverwrite", 0),
          ("qPRC", 2),
          ("qSSUT", 4),
          ("qSSUL", 8),
          ("qSEC", 11),
          ("qDNU", 15))
    )


_TimingSinkOverwriteTxQuality_Type.__name__ = "Integer32"
_TimingSinkOverwriteTxQuality_Object = MibTableColumn
timingSinkOverwriteTxQuality = _TimingSinkOverwriteTxQuality_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 4, 1, 12),
    _TimingSinkOverwriteTxQuality_Type()
)
timingSinkOverwriteTxQuality.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timingSinkOverwriteTxQuality.setStatus("current")


class _TimingSinkOverwriteRxQuality_Type(Integer32):
    """Custom type timingSinkOverwriteRxQuality based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              4,
              8,
              11,
              15)
        )
    )
    namedValues = NamedValues(
        *(("noOverwrite", 0),
          ("qPRC", 2),
          ("qSSUT", 4),
          ("qSSUL", 8),
          ("qSEC", 11),
          ("qDNU", 15))
    )


_TimingSinkOverwriteRxQuality_Type.__name__ = "Integer32"
_TimingSinkOverwriteRxQuality_Object = MibTableColumn
timingSinkOverwriteRxQuality = _TimingSinkOverwriteRxQuality_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 4, 1, 13),
    _TimingSinkOverwriteRxQuality_Type()
)
timingSinkOverwriteRxQuality.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timingSinkOverwriteRxQuality.setStatus("current")


class _TimingSinkSentQuality_Type(Integer32):
    """Custom type timingSinkSentQuality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              4,
              8,
              11,
              15)
        )
    )
    namedValues = NamedValues(
        *(("qUNKN", 0),
          ("qPRC", 2),
          ("qSSUT", 4),
          ("qSSUL", 8),
          ("qSEC", 11),
          ("qDNU", 15))
    )


_TimingSinkSentQuality_Type.__name__ = "Integer32"
_TimingSinkSentQuality_Object = MibTableColumn
timingSinkSentQuality = _TimingSinkSentQuality_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 4, 1, 14),
    _TimingSinkSentQuality_Type()
)
timingSinkSentQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timingSinkSentQuality.setStatus("current")


class _TimingSinkE1Sabit_Type(Integer32):
    """Custom type timingSinkE1Sabit based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 8),
    )


_TimingSinkE1Sabit_Type.__name__ = "Integer32"
_TimingSinkE1Sabit_Object = MibTableColumn
timingSinkE1Sabit = _TimingSinkE1Sabit_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 4, 1, 15),
    _TimingSinkE1Sabit_Type()
)
timingSinkE1Sabit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timingSinkE1Sabit.setStatus("current")


class _TimingSinkEthPortRole_Type(Integer32):
    """Custom type timingSinkEthPortRole based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2))
    )


_TimingSinkEthPortRole_Type.__name__ = "Integer32"
_TimingSinkEthPortRole_Object = MibTableColumn
timingSinkEthPortRole = _TimingSinkEthPortRole_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 4, 1, 16),
    _TimingSinkEthPortRole_Type()
)
timingSinkEthPortRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timingSinkEthPortRole.setStatus("deprecated")
_TimingSinkRowStatus_Type = RowStatus
_TimingSinkRowStatus_Object = MibTableColumn
timingSinkRowStatus = _TimingSinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 4, 1, 17),
    _TimingSinkRowStatus_Type()
)
timingSinkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timingSinkRowStatus.setStatus("current")
_TimingGeneratorManualSwitch_Type = Integer32
_TimingGeneratorManualSwitch_Object = MibScalar
timingGeneratorManualSwitch = _TimingGeneratorManualSwitch_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 5),
    _TimingGeneratorManualSwitch_Type()
)
timingGeneratorManualSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timingGeneratorManualSwitch.setStatus("current")
_TimingGeneratorForcedSwitch_Type = Integer32
_TimingGeneratorForcedSwitch_Object = MibScalar
timingGeneratorForcedSwitch = _TimingGeneratorForcedSwitch_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 6),
    _TimingGeneratorForcedSwitch_Type()
)
timingGeneratorForcedSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timingGeneratorForcedSwitch.setStatus("current")


class _TimingGeneratorT0SquelchAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type timingGeneratorT0SquelchAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_TimingGeneratorT0SquelchAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_TimingGeneratorT0SquelchAlarmSeverityCode_Object = MibScalar
timingGeneratorT0SquelchAlarmSeverityCode = _TimingGeneratorT0SquelchAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 7),
    _TimingGeneratorT0SquelchAlarmSeverityCode_Type()
)
timingGeneratorT0SquelchAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timingGeneratorT0SquelchAlarmSeverityCode.setStatus("current")


class _TimingGeneratorT4SquelchAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type timingGeneratorT4SquelchAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_TimingGeneratorT4SquelchAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_TimingGeneratorT4SquelchAlarmSeverityCode_Object = MibScalar
timingGeneratorT4SquelchAlarmSeverityCode = _TimingGeneratorT4SquelchAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 8),
    _TimingGeneratorT4SquelchAlarmSeverityCode_Type()
)
timingGeneratorT4SquelchAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timingGeneratorT4SquelchAlarmSeverityCode.setStatus("current")


class _TimingGeneratorFreeRunningStatusSeverityCode_Type(AlarmSeverityCode):
    """Custom type timingGeneratorFreeRunningStatusSeverityCode based on AlarmSeverityCode"""
    defaultValue = 3


_TimingGeneratorFreeRunningStatusSeverityCode_Type.__name__ = "AlarmSeverityCode"
_TimingGeneratorFreeRunningStatusSeverityCode_Object = MibScalar
timingGeneratorFreeRunningStatusSeverityCode = _TimingGeneratorFreeRunningStatusSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 9),
    _TimingGeneratorFreeRunningStatusSeverityCode_Type()
)
timingGeneratorFreeRunningStatusSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timingGeneratorFreeRunningStatusSeverityCode.setStatus("current")


class _TimingGeneratorHoldoverStatusSeverityCode_Type(AlarmSeverityCode):
    """Custom type timingGeneratorHoldoverStatusSeverityCode based on AlarmSeverityCode"""
    defaultValue = 3


_TimingGeneratorHoldoverStatusSeverityCode_Type.__name__ = "AlarmSeverityCode"
_TimingGeneratorHoldoverStatusSeverityCode_Object = MibScalar
timingGeneratorHoldoverStatusSeverityCode = _TimingGeneratorHoldoverStatusSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 10),
    _TimingGeneratorHoldoverStatusSeverityCode_Type()
)
timingGeneratorHoldoverStatusSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timingGeneratorHoldoverStatusSeverityCode.setStatus("current")


class _TimingGeneratorActiveStatusSeverityCode_Type(Integer32):
    """Custom type timingGeneratorActiveStatusSeverityCode based on Integer32"""
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
          ("statusTrapEnable", 2))
    )


_TimingGeneratorActiveStatusSeverityCode_Type.__name__ = "Integer32"
_TimingGeneratorActiveStatusSeverityCode_Object = MibScalar
timingGeneratorActiveStatusSeverityCode = _TimingGeneratorActiveStatusSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 11),
    _TimingGeneratorActiveStatusSeverityCode_Type()
)
timingGeneratorActiveStatusSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timingGeneratorActiveStatusSeverityCode.setStatus("current")


class _TimingGeneratorQualityEnable_Type(Integer32):
    """Custom type timingGeneratorQualityEnable based on Integer32"""
    defaultValue = 1

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


_TimingGeneratorQualityEnable_Type.__name__ = "Integer32"
_TimingGeneratorQualityEnable_Object = MibScalar
timingGeneratorQualityEnable = _TimingGeneratorQualityEnable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 12),
    _TimingGeneratorQualityEnable_Type()
)
timingGeneratorQualityEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timingGeneratorQualityEnable.setStatus("current")


class _TimingSinkLosAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type timingSinkLosAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_TimingSinkLosAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_TimingSinkLosAlarmSeverityCode_Object = MibScalar
timingSinkLosAlarmSeverityCode = _TimingSinkLosAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 13),
    _TimingSinkLosAlarmSeverityCode_Type()
)
timingSinkLosAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timingSinkLosAlarmSeverityCode.setStatus("current")


class _TimingSinkDriftAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type timingSinkDriftAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 3


_TimingSinkDriftAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_TimingSinkDriftAlarmSeverityCode_Object = MibScalar
timingSinkDriftAlarmSeverityCode = _TimingSinkDriftAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 14),
    _TimingSinkDriftAlarmSeverityCode_Type()
)
timingSinkDriftAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timingSinkDriftAlarmSeverityCode.setStatus("current")


class _TimingSinkActiveStatusSeverityCode_Type(Integer32):
    """Custom type timingSinkActiveStatusSeverityCode based on Integer32"""
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
          ("statusTrapEnable", 2))
    )


_TimingSinkActiveStatusSeverityCode_Type.__name__ = "Integer32"
_TimingSinkActiveStatusSeverityCode_Object = MibScalar
timingSinkActiveStatusSeverityCode = _TimingSinkActiveStatusSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 15),
    _TimingSinkActiveStatusSeverityCode_Type()
)
timingSinkActiveStatusSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timingSinkActiveStatusSeverityCode.setStatus("current")
_TimingSinkSelectorTable_Object = MibTable
timingSinkSelectorTable = _TimingSinkSelectorTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 16)
)
if mibBuilder.loadTexts:
    timingSinkSelectorTable.setStatus("current")
_TimingSinkSelectorRecord_Object = MibTableRow
timingSinkSelectorRecord = _TimingSinkSelectorRecord_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 16, 1)
)
timingSinkSelectorRecord.setIndexNames(
    (0, "SIAE-SYNC-MIB", "timingSinkGenId"),
    (0, "SIAE-SYNC-MIB", "timingSinkId"),
    (0, "SIAE-SYNC-MIB", "timingSinkType"),
    (0, "SIAE-SYNC-MIB", "timingSinkSelectorId"),
)
if mibBuilder.loadTexts:
    timingSinkSelectorRecord.setStatus("current")
_TimingSinkSelectorId_Type = Integer32
_TimingSinkSelectorId_Object = MibTableColumn
timingSinkSelectorId = _TimingSinkSelectorId_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 16, 1, 1),
    _TimingSinkSelectorId_Type()
)
timingSinkSelectorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timingSinkSelectorId.setStatus("current")


class _TimingSinkSelectorLabel_Type(DisplayString):
    """Custom type timingSinkSelectorLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TimingSinkSelectorLabel_Type.__name__ = "DisplayString"
_TimingSinkSelectorLabel_Object = MibTableColumn
timingSinkSelectorLabel = _TimingSinkSelectorLabel_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 16, 1, 2),
    _TimingSinkSelectorLabel_Type()
)
timingSinkSelectorLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timingSinkSelectorLabel.setStatus("current")
_EsmcTable_Object = MibTable
esmcTable = _EsmcTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 17)
)
if mibBuilder.loadTexts:
    esmcTable.setStatus("current")
_EsmcRecord_Object = MibTableRow
esmcRecord = _EsmcRecord_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 17, 1)
)
esmcRecord.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    esmcRecord.setStatus("current")


class _EsmcSsmEnable_Type(Integer32):
    """Custom type esmcSsmEnable based on Integer32"""
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


_EsmcSsmEnable_Type.__name__ = "Integer32"
_EsmcSsmEnable_Object = MibTableColumn
esmcSsmEnable = _EsmcSsmEnable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 17, 1, 1),
    _EsmcSsmEnable_Type()
)
esmcSsmEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esmcSsmEnable.setStatus("current")


class _EsmcQlRx_Type(Integer32):
    """Custom type esmcQlRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              4,
              8,
              11,
              15)
        )
    )
    namedValues = NamedValues(
        *(("qUNKN", 0),
          ("qPRC", 2),
          ("qSSUT", 4),
          ("qSSUL", 8),
          ("qSEC", 11),
          ("qDNU", 15))
    )


_EsmcQlRx_Type.__name__ = "Integer32"
_EsmcQlRx_Object = MibTableColumn
esmcQlRx = _EsmcQlRx_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 17, 1, 2),
    _EsmcQlRx_Type()
)
esmcQlRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esmcQlRx.setStatus("current")


class _EsmcQlTx_Type(Integer32):
    """Custom type esmcQlTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              4,
              8,
              11,
              15)
        )
    )
    namedValues = NamedValues(
        *(("qUNKN", 0),
          ("qPRC", 2),
          ("qSSUT", 4),
          ("qSSUL", 8),
          ("qSEC", 11),
          ("qDNU", 15))
    )


_EsmcQlTx_Type.__name__ = "Integer32"
_EsmcQlTx_Object = MibTableColumn
esmcQlTx = _EsmcQlTx_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 17, 1, 3),
    _EsmcQlTx_Type()
)
esmcQlTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esmcQlTx.setStatus("current")
_EsmcPktsRx_Type = Counter32
_EsmcPktsRx_Object = MibTableColumn
esmcPktsRx = _EsmcPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 17, 1, 4),
    _EsmcPktsRx_Type()
)
esmcPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esmcPktsRx.setStatus("current")
_EsmcPktsTx_Type = Counter32
_EsmcPktsTx_Object = MibTableColumn
esmcPktsTx = _EsmcPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 17, 1, 5),
    _EsmcPktsTx_Type()
)
esmcPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esmcPktsTx.setStatus("current")
_EsmcPktsRxDropped_Type = Counter32
_EsmcPktsRxDropped_Object = MibTableColumn
esmcPktsRxDropped = _EsmcPktsRxDropped_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 17, 1, 6),
    _EsmcPktsRxDropped_Type()
)
esmcPktsRxDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esmcPktsRxDropped.setStatus("current")
_EsmcPktsRxErrored_Type = Counter32
_EsmcPktsRxErrored_Object = MibTableColumn
esmcPktsRxErrored = _EsmcPktsRxErrored_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 17, 1, 7),
    _EsmcPktsRxErrored_Type()
)
esmcPktsRxErrored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esmcPktsRxErrored.setStatus("current")


class _Esmc1000BaseTRole_Type(Integer32):
    """Custom type esmc1000BaseTRole based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("slave", 1),
          ("master", 2),
          ("auto", 3))
    )


_Esmc1000BaseTRole_Type.__name__ = "Integer32"
_Esmc1000BaseTRole_Object = MibTableColumn
esmc1000BaseTRole = _Esmc1000BaseTRole_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 17, 1, 8),
    _Esmc1000BaseTRole_Type()
)
esmc1000BaseTRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esmc1000BaseTRole.setStatus("current")
_EsmcRowStatus_Type = RowStatus
_EsmcRowStatus_Object = MibTableColumn
esmcRowStatus = _EsmcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 28, 17, 1, 9),
    _EsmcRowStatus_Type()
)
esmcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esmcRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SIAE-SYNC-MIB",
    **{"sync": sync,
       "syncMibVersion": syncMibVersion,
       "timingGeneratorTable": timingGeneratorTable,
       "timingGeneratorRecord": timingGeneratorRecord,
       "timingGeneratorId": timingGeneratorId,
       "timingGeneratorT4vsT0": timingGeneratorT4vsT0,
       "timingGeneratorHoldOffTime": timingGeneratorHoldOffTime,
       "timingGeneratorWtrTime": timingGeneratorWtrTime,
       "timingGeneratorSinkLosSet": timingGeneratorSinkLosSet,
       "timingGeneratorSinkLosReset": timingGeneratorSinkLosReset,
       "timingGeneratorT0SquelchAlarm": timingGeneratorT0SquelchAlarm,
       "timingGeneratorT4SquelchAlarm": timingGeneratorT4SquelchAlarm,
       "timingGeneratorFreeRunningStatus": timingGeneratorFreeRunningStatus,
       "timingGeneratorHoldoverStatus": timingGeneratorHoldoverStatus,
       "timingGeneratorActiveStatus": timingGeneratorActiveStatus,
       "timingGeneratorT0CurrentQuality": timingGeneratorT0CurrentQuality,
       "timingGeneratorT4CurrentQuality": timingGeneratorT4CurrentQuality,
       "timingGeneratorT4MinimumQuality": timingGeneratorT4MinimumQuality,
       "timingGeneratorT0PreferredSource": timingGeneratorT0PreferredSource,
       "timingGeneratorT4PreferredSource": timingGeneratorT4PreferredSource,
       "timingGeneratorRowStatus": timingGeneratorRowStatus,
       "timingGeneratorMaintTable": timingGeneratorMaintTable,
       "timingGeneratorMaintRecord": timingGeneratorMaintRecord,
       "timingGeneratorT4Squelch": timingGeneratorT4Squelch,
       "timingGeneratorStatusControl": timingGeneratorStatusControl,
       "timingGeneratorT0ForcedSource": timingGeneratorT0ForcedSource,
       "timingGeneratorT4ForcedSource": timingGeneratorT4ForcedSource,
       "timingGeneratorWtrClearSource": timingGeneratorWtrClearSource,
       "timingSinkTable": timingSinkTable,
       "timingSinkRecord": timingSinkRecord,
       "timingSinkGenId": timingSinkGenId,
       "timingSinkId": timingSinkId,
       "timingSinkType": timingSinkType,
       "timingSinkIfIndex": timingSinkIfIndex,
       "timingSinkSelector": timingSinkSelector,
       "timingSinkPriority": timingSinkPriority,
       "timingSinkLabel": timingSinkLabel,
       "timingSinkLosAlarm": timingSinkLosAlarm,
       "timingSinkDriftAlarm": timingSinkDriftAlarm,
       "timingSinkActiveStatus": timingSinkActiveStatus,
       "timingSinkCurrentQuality": timingSinkCurrentQuality,
       "timingSinkOverwriteTxQuality": timingSinkOverwriteTxQuality,
       "timingSinkOverwriteRxQuality": timingSinkOverwriteRxQuality,
       "timingSinkSentQuality": timingSinkSentQuality,
       "timingSinkE1Sabit": timingSinkE1Sabit,
       "timingSinkEthPortRole": timingSinkEthPortRole,
       "timingSinkRowStatus": timingSinkRowStatus,
       "timingGeneratorManualSwitch": timingGeneratorManualSwitch,
       "timingGeneratorForcedSwitch": timingGeneratorForcedSwitch,
       "timingGeneratorT0SquelchAlarmSeverityCode": timingGeneratorT0SquelchAlarmSeverityCode,
       "timingGeneratorT4SquelchAlarmSeverityCode": timingGeneratorT4SquelchAlarmSeverityCode,
       "timingGeneratorFreeRunningStatusSeverityCode": timingGeneratorFreeRunningStatusSeverityCode,
       "timingGeneratorHoldoverStatusSeverityCode": timingGeneratorHoldoverStatusSeverityCode,
       "timingGeneratorActiveStatusSeverityCode": timingGeneratorActiveStatusSeverityCode,
       "timingGeneratorQualityEnable": timingGeneratorQualityEnable,
       "timingSinkLosAlarmSeverityCode": timingSinkLosAlarmSeverityCode,
       "timingSinkDriftAlarmSeverityCode": timingSinkDriftAlarmSeverityCode,
       "timingSinkActiveStatusSeverityCode": timingSinkActiveStatusSeverityCode,
       "timingSinkSelectorTable": timingSinkSelectorTable,
       "timingSinkSelectorRecord": timingSinkSelectorRecord,
       "timingSinkSelectorId": timingSinkSelectorId,
       "timingSinkSelectorLabel": timingSinkSelectorLabel,
       "esmcTable": esmcTable,
       "esmcRecord": esmcRecord,
       "esmcSsmEnable": esmcSsmEnable,
       "esmcQlRx": esmcQlRx,
       "esmcQlTx": esmcQlTx,
       "esmcPktsRx": esmcPktsRx,
       "esmcPktsTx": esmcPktsTx,
       "esmcPktsRxDropped": esmcPktsRxDropped,
       "esmcPktsRxErrored": esmcPktsRxErrored,
       "esmc1000BaseTRole": esmc1000BaseTRole,
       "esmcRowStatus": esmcRowStatus}
)
