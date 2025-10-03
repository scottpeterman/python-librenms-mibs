# SNMP MIB module (SIAE-ECFM-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\siae\SIAE-ECFM-EXT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:26:49 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

siaeEcfmExtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 94)
)
if mibBuilder.loadTexts:
    siaeEcfmExtMib.setRevisions(
        ("2016-07-25 00:00",
         "2015-06-26 00:00",
         "2015-04-14 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SiaeEcfmExtMibVersion_Type = Integer32
_SiaeEcfmExtMibVersion_Object = MibScalar
siaeEcfmExtMibVersion = _SiaeEcfmExtMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 94, 1),
    _SiaeEcfmExtMibVersion_Type()
)
siaeEcfmExtMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siaeEcfmExtMibVersion.setStatus("current")
_SiaeMepAlarms8021agTable_Object = MibTable
siaeMepAlarms8021agTable = _SiaeMepAlarms8021agTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 94, 2)
)
if mibBuilder.loadTexts:
    siaeMepAlarms8021agTable.setStatus("current")
_SiaeMepAlarms8021agEntry_Object = MibTableRow
siaeMepAlarms8021agEntry = _SiaeMepAlarms8021agEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 94, 2, 1)
)
siaeMepAlarms8021agEntry.setIndexNames(
    (0, "SIAE-ECFM-EXT-MIB", "defMIEcfmContextId"),
    (0, "SIAE-ECFM-EXT-MIB", "defMIEcfmMdIndex"),
    (0, "SIAE-ECFM-EXT-MIB", "defMIEcfmMaIndex"),
    (0, "SIAE-ECFM-EXT-MIB", "defMIEcfmMepIdentifier"),
)
if mibBuilder.loadTexts:
    siaeMepAlarms8021agEntry.setStatus("current")
_DefMIEcfmContextId_Type = Unsigned32
_DefMIEcfmContextId_Object = MibTableColumn
defMIEcfmContextId = _DefMIEcfmContextId_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 94, 2, 1, 1),
    _DefMIEcfmContextId_Type()
)
defMIEcfmContextId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    defMIEcfmContextId.setStatus("current")
_DefMIEcfmMdIndex_Type = Unsigned32
_DefMIEcfmMdIndex_Object = MibTableColumn
defMIEcfmMdIndex = _DefMIEcfmMdIndex_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 94, 2, 1, 2),
    _DefMIEcfmMdIndex_Type()
)
defMIEcfmMdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    defMIEcfmMdIndex.setStatus("current")
_DefMIEcfmMaIndex_Type = Unsigned32
_DefMIEcfmMaIndex_Object = MibTableColumn
defMIEcfmMaIndex = _DefMIEcfmMaIndex_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 94, 2, 1, 3),
    _DefMIEcfmMaIndex_Type()
)
defMIEcfmMaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    defMIEcfmMaIndex.setStatus("current")
_DefMIEcfmMepIdentifier_Type = Unsigned32
_DefMIEcfmMepIdentifier_Object = MibTableColumn
defMIEcfmMepIdentifier = _DefMIEcfmMepIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 94, 2, 1, 4),
    _DefMIEcfmMepIdentifier_Type()
)
defMIEcfmMepIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    defMIEcfmMepIdentifier.setStatus("current")
_DefRdiCcmAlarm_Type = AlarmStatus
_DefRdiCcmAlarm_Object = MibTableColumn
defRdiCcmAlarm = _DefRdiCcmAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 94, 2, 1, 5),
    _DefRdiCcmAlarm_Type()
)
defRdiCcmAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defRdiCcmAlarm.setStatus("current")
_DefMacStatusAlarm_Type = AlarmStatus
_DefMacStatusAlarm_Object = MibTableColumn
defMacStatusAlarm = _DefMacStatusAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 94, 2, 1, 6),
    _DefMacStatusAlarm_Type()
)
defMacStatusAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defMacStatusAlarm.setStatus("current")
_DefRemoteCcmAlarm_Type = AlarmStatus
_DefRemoteCcmAlarm_Object = MibTableColumn
defRemoteCcmAlarm = _DefRemoteCcmAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 94, 2, 1, 7),
    _DefRemoteCcmAlarm_Type()
)
defRemoteCcmAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defRemoteCcmAlarm.setStatus("current")
_DefErrorCcmAlarm_Type = AlarmStatus
_DefErrorCcmAlarm_Object = MibTableColumn
defErrorCcmAlarm = _DefErrorCcmAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 94, 2, 1, 8),
    _DefErrorCcmAlarm_Type()
)
defErrorCcmAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defErrorCcmAlarm.setStatus("current")
_DefXconCcmAlarm_Type = AlarmStatus
_DefXconCcmAlarm_Object = MibTableColumn
defXconCcmAlarm = _DefXconCcmAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 94, 2, 1, 9),
    _DefXconCcmAlarm_Type()
)
defXconCcmAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defXconCcmAlarm.setStatus("current")
_SiaeMepAlarmsY1731Table_Object = MibTable
siaeMepAlarmsY1731Table = _SiaeMepAlarmsY1731Table_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 94, 3)
)
if mibBuilder.loadTexts:
    siaeMepAlarmsY1731Table.setStatus("current")
_SiaeMepAlarmsY1731Entry_Object = MibTableRow
siaeMepAlarmsY1731Entry = _SiaeMepAlarmsY1731Entry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 94, 3, 1)
)
siaeMepAlarmsY1731Entry.setIndexNames(
    (0, "SIAE-ECFM-EXT-MIB", "defMIEcfmY1731ContextId"),
    (0, "SIAE-ECFM-EXT-MIB", "defMIEcfmY1731MegIndex"),
    (0, "SIAE-ECFM-EXT-MIB", "defMIEcfmY1731MeIndex"),
    (0, "SIAE-ECFM-EXT-MIB", "defMIEcfmY1731MepIdentifier"),
)
if mibBuilder.loadTexts:
    siaeMepAlarmsY1731Entry.setStatus("current")
_DefMIEcfmY1731ContextId_Type = Unsigned32
_DefMIEcfmY1731ContextId_Object = MibTableColumn
defMIEcfmY1731ContextId = _DefMIEcfmY1731ContextId_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 94, 3, 1, 1),
    _DefMIEcfmY1731ContextId_Type()
)
defMIEcfmY1731ContextId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    defMIEcfmY1731ContextId.setStatus("current")
_DefMIEcfmY1731MegIndex_Type = Unsigned32
_DefMIEcfmY1731MegIndex_Object = MibTableColumn
defMIEcfmY1731MegIndex = _DefMIEcfmY1731MegIndex_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 94, 3, 1, 2),
    _DefMIEcfmY1731MegIndex_Type()
)
defMIEcfmY1731MegIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    defMIEcfmY1731MegIndex.setStatus("current")
_DefMIEcfmY1731MeIndex_Type = Unsigned32
_DefMIEcfmY1731MeIndex_Object = MibTableColumn
defMIEcfmY1731MeIndex = _DefMIEcfmY1731MeIndex_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 94, 3, 1, 3),
    _DefMIEcfmY1731MeIndex_Type()
)
defMIEcfmY1731MeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    defMIEcfmY1731MeIndex.setStatus("current")
_DefMIEcfmY1731MepIdentifier_Type = Unsigned32
_DefMIEcfmY1731MepIdentifier_Object = MibTableColumn
defMIEcfmY1731MepIdentifier = _DefMIEcfmY1731MepIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 94, 3, 1, 4),
    _DefMIEcfmY1731MepIdentifier_Type()
)
defMIEcfmY1731MepIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    defMIEcfmY1731MepIdentifier.setStatus("current")
_DefRdiConditionAlarm_Type = AlarmStatus
_DefRdiConditionAlarm_Object = MibTableColumn
defRdiConditionAlarm = _DefRdiConditionAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 94, 3, 1, 5),
    _DefRdiConditionAlarm_Type()
)
defRdiConditionAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defRdiConditionAlarm.setStatus("current")
_DefLossOfContinuityAlarm_Type = AlarmStatus
_DefLossOfContinuityAlarm_Object = MibTableColumn
defLossOfContinuityAlarm = _DefLossOfContinuityAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 94, 3, 1, 6),
    _DefLossOfContinuityAlarm_Type()
)
defLossOfContinuityAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defLossOfContinuityAlarm.setStatus("current")
_DefUnexpectedPeriodAlarm_Type = AlarmStatus
_DefUnexpectedPeriodAlarm_Object = MibTableColumn
defUnexpectedPeriodAlarm = _DefUnexpectedPeriodAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 94, 3, 1, 7),
    _DefUnexpectedPeriodAlarm_Type()
)
defUnexpectedPeriodAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defUnexpectedPeriodAlarm.setStatus("current")
_DefUnexpectedMepAlarm_Type = AlarmStatus
_DefUnexpectedMepAlarm_Object = MibTableColumn
defUnexpectedMepAlarm = _DefUnexpectedMepAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 94, 3, 1, 8),
    _DefUnexpectedMepAlarm_Type()
)
defUnexpectedMepAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defUnexpectedMepAlarm.setStatus("current")
_DefMisMergeAlarm_Type = AlarmStatus
_DefMisMergeAlarm_Object = MibTableColumn
defMisMergeAlarm = _DefMisMergeAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 94, 3, 1, 9),
    _DefMisMergeAlarm_Type()
)
defMisMergeAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defMisMergeAlarm.setStatus("current")
_DefUnexpectedMegLevelAlarm_Type = AlarmStatus
_DefUnexpectedMegLevelAlarm_Object = MibTableColumn
defUnexpectedMegLevelAlarm = _DefUnexpectedMegLevelAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 94, 3, 1, 10),
    _DefUnexpectedMegLevelAlarm_Type()
)
defUnexpectedMegLevelAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defUnexpectedMegLevelAlarm.setStatus("current")
_DefAisConditionAlarm_Type = AlarmStatus
_DefAisConditionAlarm_Object = MibTableColumn
defAisConditionAlarm = _DefAisConditionAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 94, 3, 1, 11),
    _DefAisConditionAlarm_Type()
)
defAisConditionAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defAisConditionAlarm.setStatus("current")
_DefLckConditionAlarm_Type = AlarmStatus
_DefLckConditionAlarm_Object = MibTableColumn
defLckConditionAlarm = _DefLckConditionAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 94, 3, 1, 12),
    _DefLckConditionAlarm_Type()
)
defLckConditionAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defLckConditionAlarm.setStatus("current")


class _MepRdiCcmAlarmsSeverityCode_Type(AlarmSeverityCode):
    """Custom type mepRdiCcmAlarmsSeverityCode based on AlarmSeverityCode"""
    defaultValue = 3


_MepRdiCcmAlarmsSeverityCode_Type.__name__ = "AlarmSeverityCode"
_MepRdiCcmAlarmsSeverityCode_Object = MibScalar
mepRdiCcmAlarmsSeverityCode = _MepRdiCcmAlarmsSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 94, 4),
    _MepRdiCcmAlarmsSeverityCode_Type()
)
mepRdiCcmAlarmsSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mepRdiCcmAlarmsSeverityCode.setStatus("current")


class _MepMacStatusAlarmsSeverityCode_Type(AlarmSeverityCode):
    """Custom type mepMacStatusAlarmsSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_MepMacStatusAlarmsSeverityCode_Type.__name__ = "AlarmSeverityCode"
_MepMacStatusAlarmsSeverityCode_Object = MibScalar
mepMacStatusAlarmsSeverityCode = _MepMacStatusAlarmsSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 94, 5),
    _MepMacStatusAlarmsSeverityCode_Type()
)
mepMacStatusAlarmsSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mepMacStatusAlarmsSeverityCode.setStatus("current")


class _MepRemoteCcmAlarmsSeverityCode_Type(AlarmSeverityCode):
    """Custom type mepRemoteCcmAlarmsSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_MepRemoteCcmAlarmsSeverityCode_Type.__name__ = "AlarmSeverityCode"
_MepRemoteCcmAlarmsSeverityCode_Object = MibScalar
mepRemoteCcmAlarmsSeverityCode = _MepRemoteCcmAlarmsSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 94, 6),
    _MepRemoteCcmAlarmsSeverityCode_Type()
)
mepRemoteCcmAlarmsSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mepRemoteCcmAlarmsSeverityCode.setStatus("current")


class _MepErrorCcmAlarmsSeverityCode_Type(AlarmSeverityCode):
    """Custom type mepErrorCcmAlarmsSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_MepErrorCcmAlarmsSeverityCode_Type.__name__ = "AlarmSeverityCode"
_MepErrorCcmAlarmsSeverityCode_Object = MibScalar
mepErrorCcmAlarmsSeverityCode = _MepErrorCcmAlarmsSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 94, 7),
    _MepErrorCcmAlarmsSeverityCode_Type()
)
mepErrorCcmAlarmsSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mepErrorCcmAlarmsSeverityCode.setStatus("current")


class _MepXconCcmAlarmsSeverityCode_Type(AlarmSeverityCode):
    """Custom type mepXconCcmAlarmsSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_MepXconCcmAlarmsSeverityCode_Type.__name__ = "AlarmSeverityCode"
_MepXconCcmAlarmsSeverityCode_Object = MibScalar
mepXconCcmAlarmsSeverityCode = _MepXconCcmAlarmsSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 94, 8),
    _MepXconCcmAlarmsSeverityCode_Type()
)
mepXconCcmAlarmsSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mepXconCcmAlarmsSeverityCode.setStatus("current")


class _MepRdiConditionAlarmsSeverityCode_Type(AlarmSeverityCode):
    """Custom type mepRdiConditionAlarmsSeverityCode based on AlarmSeverityCode"""
    defaultValue = 3


_MepRdiConditionAlarmsSeverityCode_Type.__name__ = "AlarmSeverityCode"
_MepRdiConditionAlarmsSeverityCode_Object = MibScalar
mepRdiConditionAlarmsSeverityCode = _MepRdiConditionAlarmsSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 94, 9),
    _MepRdiConditionAlarmsSeverityCode_Type()
)
mepRdiConditionAlarmsSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mepRdiConditionAlarmsSeverityCode.setStatus("current")


class _MepLossOfContinuityAlarmsSeverityCode_Type(AlarmSeverityCode):
    """Custom type mepLossOfContinuityAlarmsSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_MepLossOfContinuityAlarmsSeverityCode_Type.__name__ = "AlarmSeverityCode"
_MepLossOfContinuityAlarmsSeverityCode_Object = MibScalar
mepLossOfContinuityAlarmsSeverityCode = _MepLossOfContinuityAlarmsSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 94, 10),
    _MepLossOfContinuityAlarmsSeverityCode_Type()
)
mepLossOfContinuityAlarmsSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mepLossOfContinuityAlarmsSeverityCode.setStatus("current")


class _MepUnexpectedPeriodAlarmsSeverityCode_Type(AlarmSeverityCode):
    """Custom type mepUnexpectedPeriodAlarmsSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_MepUnexpectedPeriodAlarmsSeverityCode_Type.__name__ = "AlarmSeverityCode"
_MepUnexpectedPeriodAlarmsSeverityCode_Object = MibScalar
mepUnexpectedPeriodAlarmsSeverityCode = _MepUnexpectedPeriodAlarmsSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 94, 11),
    _MepUnexpectedPeriodAlarmsSeverityCode_Type()
)
mepUnexpectedPeriodAlarmsSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mepUnexpectedPeriodAlarmsSeverityCode.setStatus("current")


class _MepUnexpectedMepAlarmsSeverityCode_Type(AlarmSeverityCode):
    """Custom type mepUnexpectedMepAlarmsSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_MepUnexpectedMepAlarmsSeverityCode_Type.__name__ = "AlarmSeverityCode"
_MepUnexpectedMepAlarmsSeverityCode_Object = MibScalar
mepUnexpectedMepAlarmsSeverityCode = _MepUnexpectedMepAlarmsSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 94, 12),
    _MepUnexpectedMepAlarmsSeverityCode_Type()
)
mepUnexpectedMepAlarmsSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mepUnexpectedMepAlarmsSeverityCode.setStatus("current")


class _MepMisMergeAlarmsSeverityCode_Type(AlarmSeverityCode):
    """Custom type mepMisMergeAlarmsSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_MepMisMergeAlarmsSeverityCode_Type.__name__ = "AlarmSeverityCode"
_MepMisMergeAlarmsSeverityCode_Object = MibScalar
mepMisMergeAlarmsSeverityCode = _MepMisMergeAlarmsSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 94, 13),
    _MepMisMergeAlarmsSeverityCode_Type()
)
mepMisMergeAlarmsSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mepMisMergeAlarmsSeverityCode.setStatus("current")


class _MepUnexpectedMegLevelAlarmsSeverityCode_Type(AlarmSeverityCode):
    """Custom type mepUnexpectedMegLevelAlarmsSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_MepUnexpectedMegLevelAlarmsSeverityCode_Type.__name__ = "AlarmSeverityCode"
_MepUnexpectedMegLevelAlarmsSeverityCode_Object = MibScalar
mepUnexpectedMegLevelAlarmsSeverityCode = _MepUnexpectedMegLevelAlarmsSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 94, 14),
    _MepUnexpectedMegLevelAlarmsSeverityCode_Type()
)
mepUnexpectedMegLevelAlarmsSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mepUnexpectedMegLevelAlarmsSeverityCode.setStatus("current")


class _MepAisConditionAlarmsSeverityCode_Type(AlarmSeverityCode):
    """Custom type mepAisConditionAlarmsSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_MepAisConditionAlarmsSeverityCode_Type.__name__ = "AlarmSeverityCode"
_MepAisConditionAlarmsSeverityCode_Object = MibScalar
mepAisConditionAlarmsSeverityCode = _MepAisConditionAlarmsSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 94, 15),
    _MepAisConditionAlarmsSeverityCode_Type()
)
mepAisConditionAlarmsSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mepAisConditionAlarmsSeverityCode.setStatus("current")


class _MepLckConditionAlarmsSeverityCode_Type(AlarmSeverityCode):
    """Custom type mepLckConditionAlarmsSeverityCode based on AlarmSeverityCode"""
    defaultValue = 2


_MepLckConditionAlarmsSeverityCode_Type.__name__ = "AlarmSeverityCode"
_MepLckConditionAlarmsSeverityCode_Object = MibScalar
mepLckConditionAlarmsSeverityCode = _MepLckConditionAlarmsSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 94, 16),
    _MepLckConditionAlarmsSeverityCode_Type()
)
mepLckConditionAlarmsSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mepLckConditionAlarmsSeverityCode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SIAE-ECFM-EXT-MIB",
    **{"siaeEcfmExtMib": siaeEcfmExtMib,
       "siaeEcfmExtMibVersion": siaeEcfmExtMibVersion,
       "siaeMepAlarms8021agTable": siaeMepAlarms8021agTable,
       "siaeMepAlarms8021agEntry": siaeMepAlarms8021agEntry,
       "defMIEcfmContextId": defMIEcfmContextId,
       "defMIEcfmMdIndex": defMIEcfmMdIndex,
       "defMIEcfmMaIndex": defMIEcfmMaIndex,
       "defMIEcfmMepIdentifier": defMIEcfmMepIdentifier,
       "defRdiCcmAlarm": defRdiCcmAlarm,
       "defMacStatusAlarm": defMacStatusAlarm,
       "defRemoteCcmAlarm": defRemoteCcmAlarm,
       "defErrorCcmAlarm": defErrorCcmAlarm,
       "defXconCcmAlarm": defXconCcmAlarm,
       "siaeMepAlarmsY1731Table": siaeMepAlarmsY1731Table,
       "siaeMepAlarmsY1731Entry": siaeMepAlarmsY1731Entry,
       "defMIEcfmY1731ContextId": defMIEcfmY1731ContextId,
       "defMIEcfmY1731MegIndex": defMIEcfmY1731MegIndex,
       "defMIEcfmY1731MeIndex": defMIEcfmY1731MeIndex,
       "defMIEcfmY1731MepIdentifier": defMIEcfmY1731MepIdentifier,
       "defRdiConditionAlarm": defRdiConditionAlarm,
       "defLossOfContinuityAlarm": defLossOfContinuityAlarm,
       "defUnexpectedPeriodAlarm": defUnexpectedPeriodAlarm,
       "defUnexpectedMepAlarm": defUnexpectedMepAlarm,
       "defMisMergeAlarm": defMisMergeAlarm,
       "defUnexpectedMegLevelAlarm": defUnexpectedMegLevelAlarm,
       "defAisConditionAlarm": defAisConditionAlarm,
       "defLckConditionAlarm": defLckConditionAlarm,
       "mepRdiCcmAlarmsSeverityCode": mepRdiCcmAlarmsSeverityCode,
       "mepMacStatusAlarmsSeverityCode": mepMacStatusAlarmsSeverityCode,
       "mepRemoteCcmAlarmsSeverityCode": mepRemoteCcmAlarmsSeverityCode,
       "mepErrorCcmAlarmsSeverityCode": mepErrorCcmAlarmsSeverityCode,
       "mepXconCcmAlarmsSeverityCode": mepXconCcmAlarmsSeverityCode,
       "mepRdiConditionAlarmsSeverityCode": mepRdiConditionAlarmsSeverityCode,
       "mepLossOfContinuityAlarmsSeverityCode": mepLossOfContinuityAlarmsSeverityCode,
       "mepUnexpectedPeriodAlarmsSeverityCode": mepUnexpectedPeriodAlarmsSeverityCode,
       "mepUnexpectedMepAlarmsSeverityCode": mepUnexpectedMepAlarmsSeverityCode,
       "mepMisMergeAlarmsSeverityCode": mepMisMergeAlarmsSeverityCode,
       "mepUnexpectedMegLevelAlarmsSeverityCode": mepUnexpectedMegLevelAlarmsSeverityCode,
       "mepAisConditionAlarmsSeverityCode": mepAisConditionAlarmsSeverityCode,
       "mepLckConditionAlarmsSeverityCode": mepLckConditionAlarmsSeverityCode}
)
