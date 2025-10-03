# SNMP MIB module (CIENA-WS-PLATFORM-ALARM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ciena\CIENA-WS-PLATFORM-ALARM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:25:07 2025
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

(cienaWsPlatformConfig,) = mibBuilder.importSymbols(
    "CIENA-WS-MIB",
    "cienaWsPlatformConfig")

(StringMaxl16,
 StringMaxl32,
 StringMaxl44) = mibBuilder.importSymbols(
    "CIENA-WS-PLATFORM-TYPEDEFS-MIB",
    "StringMaxl16",
    "StringMaxl32",
    "StringMaxl44")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cienaWsPlatformAlarmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 4)
)
if mibBuilder.loadTexts:
    cienaWsPlatformAlarmMIB.setRevisions(
        ("2018-09-20 00:00",
         "2018-08-14 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AlarmReason(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              6,
              7,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("reset", 1),
          ("set", 2),
          ("acknowledge", 5),
          ("clear", 6),
          ("delete", 7),
          ("config", 9),
          ("intermittent", 10))
    )



class AlarmSeverity(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5,
              6,
              8)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("critical", 3),
          ("major", 4),
          ("minor", 5),
          ("warning", 6),
          ("info", 8))
    )



# MIB Managed Objects in the order of their OIDs

_CienaWsPlatformAlarmObjects_ObjectIdentity = ObjectIdentity
cienaWsPlatformAlarmObjects = _CienaWsPlatformAlarmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 4, 1)
)
_CienaWsPlatformAlarmConformance_ObjectIdentity = ObjectIdentity
cienaWsPlatformAlarmConformance = _CienaWsPlatformAlarmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 4, 2)
)
_CienaWsPlatformAlarmGroups_ObjectIdentity = ObjectIdentity
cienaWsPlatformAlarmGroups = _CienaWsPlatformAlarmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 4, 2, 1)
)
_CienaWsPlatformAlarmCompliances_ObjectIdentity = ObjectIdentity
cienaWsPlatformAlarmCompliances = _CienaWsPlatformAlarmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 4, 2, 2)
)
_ActiveAlarmTable_Object = MibTable
activeAlarmTable = _ActiveAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 4, 3)
)
if mibBuilder.loadTexts:
    activeAlarmTable.setStatus("current")
_ActiveAlarmEntry_Object = MibTableRow
activeAlarmEntry = _ActiveAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 4, 3, 1)
)
activeAlarmEntry.setIndexNames(
    (0, "CIENA-WS-PLATFORM-ALARM-MIB", "activeAlarmInstanceId"),
)
if mibBuilder.loadTexts:
    activeAlarmEntry.setStatus("current")


class _ActiveAlarmInstanceId_Type(Integer32):
    """Custom type activeAlarmInstanceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ActiveAlarmInstanceId_Type.__name__ = "Integer32"
_ActiveAlarmInstanceId_Object = MibTableColumn
activeAlarmInstanceId = _ActiveAlarmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 4, 3, 1, 1),
    _ActiveAlarmInstanceId_Type()
)
activeAlarmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    activeAlarmInstanceId.setStatus("current")
_ActiveAlarmAcknowledged_Type = TruthValue
_ActiveAlarmAcknowledged_Object = MibTableColumn
activeAlarmAcknowledged = _ActiveAlarmAcknowledged_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 4, 3, 1, 2),
    _ActiveAlarmAcknowledged_Type()
)
activeAlarmAcknowledged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeAlarmAcknowledged.setStatus("current")
_ActiveAlarmTableId_Type = Unsigned32
_ActiveAlarmTableId_Object = MibTableColumn
activeAlarmTableId = _ActiveAlarmTableId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 4, 3, 1, 3),
    _ActiveAlarmTableId_Type()
)
activeAlarmTableId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeAlarmTableId.setStatus("current")
_ActiveAlarmSeverity_Type = AlarmSeverity
_ActiveAlarmSeverity_Object = MibTableColumn
activeAlarmSeverity = _ActiveAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 4, 3, 1, 4),
    _ActiveAlarmSeverity_Type()
)
activeAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeAlarmSeverity.setStatus("current")
_ActiveAlarmLocalDateTime_Type = StringMaxl32
_ActiveAlarmLocalDateTime_Object = MibTableColumn
activeAlarmLocalDateTime = _ActiveAlarmLocalDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 4, 3, 1, 5),
    _ActiveAlarmLocalDateTime_Type()
)
activeAlarmLocalDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeAlarmLocalDateTime.setStatus("current")
_ActiveAlarmInstance_Type = StringMaxl32
_ActiveAlarmInstance_Object = MibTableColumn
activeAlarmInstance = _ActiveAlarmInstance_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 4, 3, 1, 6),
    _ActiveAlarmInstance_Type()
)
activeAlarmInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeAlarmInstance.setStatus("current")
_ActiveAlarmDescription_Type = StringMaxl44
_ActiveAlarmDescription_Object = MibTableColumn
activeAlarmDescription = _ActiveAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 4, 3, 1, 7),
    _ActiveAlarmDescription_Type()
)
activeAlarmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeAlarmDescription.setStatus("current")
_ActiveAlarmIntermittent_Type = TruthValue
_ActiveAlarmIntermittent_Object = MibTableColumn
activeAlarmIntermittent = _ActiveAlarmIntermittent_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 4, 3, 1, 8),
    _ActiveAlarmIntermittent_Type()
)
activeAlarmIntermittent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeAlarmIntermittent.setStatus("current")
_ActiveAlarmSiteIdentifier_Type = Unsigned32
_ActiveAlarmSiteIdentifier_Object = MibTableColumn
activeAlarmSiteIdentifier = _ActiveAlarmSiteIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 4, 3, 1, 9),
    _ActiveAlarmSiteIdentifier_Type()
)
activeAlarmSiteIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeAlarmSiteIdentifier.setStatus("current")
_ActiveAlarmGroupIdentifier_Type = Unsigned32
_ActiveAlarmGroupIdentifier_Object = MibTableColumn
activeAlarmGroupIdentifier = _ActiveAlarmGroupIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 4, 3, 1, 10),
    _ActiveAlarmGroupIdentifier_Type()
)
activeAlarmGroupIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeAlarmGroupIdentifier.setStatus("current")
_ActiveAlarmMemberIdentifier_Type = Unsigned32
_ActiveAlarmMemberIdentifier_Object = MibTableColumn
activeAlarmMemberIdentifier = _ActiveAlarmMemberIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 4, 3, 1, 11),
    _ActiveAlarmMemberIdentifier_Type()
)
activeAlarmMemberIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeAlarmMemberIdentifier.setStatus("current")
_HistoryAlarmTable_Object = MibTable
historyAlarmTable = _HistoryAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 4, 4)
)
if mibBuilder.loadTexts:
    historyAlarmTable.setStatus("current")
_HistoryAlarmEntry_Object = MibTableRow
historyAlarmEntry = _HistoryAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 4, 4, 1)
)
historyAlarmEntry.setIndexNames(
    (0, "CIENA-WS-PLATFORM-ALARM-MIB", "historyAlarmId"),
)
if mibBuilder.loadTexts:
    historyAlarmEntry.setStatus("current")


class _HistoryAlarmId_Type(Integer32):
    """Custom type historyAlarmId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HistoryAlarmId_Type.__name__ = "Integer32"
_HistoryAlarmId_Object = MibTableColumn
historyAlarmId = _HistoryAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 4, 4, 1, 1),
    _HistoryAlarmId_Type()
)
historyAlarmId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    historyAlarmId.setStatus("current")
_HistoryAlarmReason_Type = AlarmReason
_HistoryAlarmReason_Object = MibTableColumn
historyAlarmReason = _HistoryAlarmReason_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 4, 4, 1, 2),
    _HistoryAlarmReason_Type()
)
historyAlarmReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyAlarmReason.setStatus("current")
_HistoryAlarmInstanceId_Type = Unsigned32
_HistoryAlarmInstanceId_Object = MibTableColumn
historyAlarmInstanceId = _HistoryAlarmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 4, 4, 1, 3),
    _HistoryAlarmInstanceId_Type()
)
historyAlarmInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyAlarmInstanceId.setStatus("current")
_HistoryAlarmTableId_Type = Unsigned32
_HistoryAlarmTableId_Object = MibTableColumn
historyAlarmTableId = _HistoryAlarmTableId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 4, 4, 1, 4),
    _HistoryAlarmTableId_Type()
)
historyAlarmTableId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyAlarmTableId.setStatus("current")
_HistoryAlarmSeverity_Type = AlarmSeverity
_HistoryAlarmSeverity_Object = MibTableColumn
historyAlarmSeverity = _HistoryAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 4, 4, 1, 5),
    _HistoryAlarmSeverity_Type()
)
historyAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyAlarmSeverity.setStatus("current")
_HistoryAlarmLocalDateTime_Type = StringMaxl32
_HistoryAlarmLocalDateTime_Object = MibTableColumn
historyAlarmLocalDateTime = _HistoryAlarmLocalDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 4, 4, 1, 6),
    _HistoryAlarmLocalDateTime_Type()
)
historyAlarmLocalDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyAlarmLocalDateTime.setStatus("current")
_HistoryAlarmInstance_Type = StringMaxl32
_HistoryAlarmInstance_Object = MibTableColumn
historyAlarmInstance = _HistoryAlarmInstance_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 4, 4, 1, 7),
    _HistoryAlarmInstance_Type()
)
historyAlarmInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyAlarmInstance.setStatus("current")
_HistoryAlarmDescription_Type = StringMaxl44
_HistoryAlarmDescription_Object = MibTableColumn
historyAlarmDescription = _HistoryAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 4, 4, 1, 8),
    _HistoryAlarmDescription_Type()
)
historyAlarmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyAlarmDescription.setStatus("current")
_HistoryAlarmSiteIdentifier_Type = Unsigned32
_HistoryAlarmSiteIdentifier_Object = MibTableColumn
historyAlarmSiteIdentifier = _HistoryAlarmSiteIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 4, 4, 1, 9),
    _HistoryAlarmSiteIdentifier_Type()
)
historyAlarmSiteIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyAlarmSiteIdentifier.setStatus("current")
_HistoryAlarmGroupIdentifier_Type = Unsigned32
_HistoryAlarmGroupIdentifier_Object = MibTableColumn
historyAlarmGroupIdentifier = _HistoryAlarmGroupIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 4, 4, 1, 10),
    _HistoryAlarmGroupIdentifier_Type()
)
historyAlarmGroupIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyAlarmGroupIdentifier.setStatus("current")
_HistoryAlarmMemberIdentifier_Type = Unsigned32
_HistoryAlarmMemberIdentifier_Object = MibTableColumn
historyAlarmMemberIdentifier = _HistoryAlarmMemberIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 4, 4, 1, 11),
    _HistoryAlarmMemberIdentifier_Type()
)
historyAlarmMemberIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyAlarmMemberIdentifier.setStatus("current")
_DefinedAlarmTable_Object = MibTable
definedAlarmTable = _DefinedAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 4, 5)
)
if mibBuilder.loadTexts:
    definedAlarmTable.setStatus("current")
_DefinedAlarmEntry_Object = MibTableRow
definedAlarmEntry = _DefinedAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 4, 5, 1)
)
definedAlarmEntry.setIndexNames(
    (0, "CIENA-WS-PLATFORM-ALARM-MIB", "definedAlarmId"),
)
if mibBuilder.loadTexts:
    definedAlarmEntry.setStatus("current")


class _DefinedAlarmId_Type(Integer32):
    """Custom type definedAlarmId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DefinedAlarmId_Type.__name__ = "Integer32"
_DefinedAlarmId_Object = MibTableColumn
definedAlarmId = _DefinedAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 4, 5, 1, 1),
    _DefinedAlarmId_Type()
)
definedAlarmId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    definedAlarmId.setStatus("current")


class _DefinedAlarmTableId_Type(Integer32):
    """Custom type definedAlarmTableId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DefinedAlarmTableId_Type.__name__ = "Integer32"
_DefinedAlarmTableId_Object = MibTableColumn
definedAlarmTableId = _DefinedAlarmTableId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 4, 5, 1, 2),
    _DefinedAlarmTableId_Type()
)
definedAlarmTableId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    definedAlarmTableId.setStatus("current")
_DefinedAlarmEnabled_Type = TruthValue
_DefinedAlarmEnabled_Object = MibTableColumn
definedAlarmEnabled = _DefinedAlarmEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 4, 5, 1, 3),
    _DefinedAlarmEnabled_Type()
)
definedAlarmEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    definedAlarmEnabled.setStatus("current")
_DefinedAlarmActive_Type = TruthValue
_DefinedAlarmActive_Object = MibTableColumn
definedAlarmActive = _DefinedAlarmActive_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 4, 5, 1, 4),
    _DefinedAlarmActive_Type()
)
definedAlarmActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    definedAlarmActive.setStatus("current")
_DefinedAlarmThreshold_Type = Unsigned32
_DefinedAlarmThreshold_Object = MibTableColumn
definedAlarmThreshold = _DefinedAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 4, 5, 1, 5),
    _DefinedAlarmThreshold_Type()
)
definedAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    definedAlarmThreshold.setStatus("current")
_DefinedAlarmCap_Type = Unsigned32
_DefinedAlarmCap_Object = MibTableColumn
definedAlarmCap = _DefinedAlarmCap_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 4, 5, 1, 6),
    _DefinedAlarmCap_Type()
)
definedAlarmCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    definedAlarmCap.setStatus("current")
_DefinedAlarmSeverity_Type = AlarmSeverity
_DefinedAlarmSeverity_Object = MibTableColumn
definedAlarmSeverity = _DefinedAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 4, 5, 1, 7),
    _DefinedAlarmSeverity_Type()
)
definedAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    definedAlarmSeverity.setStatus("current")
_DefinedAlarmInstance_Type = StringMaxl16
_DefinedAlarmInstance_Object = MibTableColumn
definedAlarmInstance = _DefinedAlarmInstance_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 4, 5, 1, 8),
    _DefinedAlarmInstance_Type()
)
definedAlarmInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    definedAlarmInstance.setStatus("current")
_DefinedAlarmDescription_Type = StringMaxl44
_DefinedAlarmDescription_Object = MibTableColumn
definedAlarmDescription = _DefinedAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 4, 5, 1, 9),
    _DefinedAlarmDescription_Type()
)
definedAlarmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    definedAlarmDescription.setStatus("current")
_AlarmStatisticsTable_Object = MibTable
alarmStatisticsTable = _AlarmStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 4, 6)
)
if mibBuilder.loadTexts:
    alarmStatisticsTable.setStatus("current")
_AlarmStatisticsEntry_Object = MibTableRow
alarmStatisticsEntry = _AlarmStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 4, 6, 1)
)
alarmStatisticsEntry.setIndexNames(
    (0, "CIENA-WS-PLATFORM-ALARM-MIB", "alarmStatisticsIndex"),
)
if mibBuilder.loadTexts:
    alarmStatisticsEntry.setStatus("current")


class _AlarmStatisticsIndex_Type(Integer32):
    """Custom type alarmStatisticsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AlarmStatisticsIndex_Type.__name__ = "Integer32"
_AlarmStatisticsIndex_Object = MibTableColumn
alarmStatisticsIndex = _AlarmStatisticsIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 4, 6, 1, 1),
    _AlarmStatisticsIndex_Type()
)
alarmStatisticsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alarmStatisticsIndex.setStatus("current")
_AlarmStatisticsActive_Type = TruthValue
_AlarmStatisticsActive_Object = MibTableColumn
alarmStatisticsActive = _AlarmStatisticsActive_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 4, 6, 1, 2),
    _AlarmStatisticsActive_Type()
)
alarmStatisticsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmStatisticsActive.setStatus("current")
_AlarmStatisticsDisabled_Type = TruthValue
_AlarmStatisticsDisabled_Object = MibTableColumn
alarmStatisticsDisabled = _AlarmStatisticsDisabled_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 4, 6, 1, 3),
    _AlarmStatisticsDisabled_Type()
)
alarmStatisticsDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmStatisticsDisabled.setStatus("current")
_AlarmStatisticsCount_Type = Unsigned32
_AlarmStatisticsCount_Object = MibTableColumn
alarmStatisticsCount = _AlarmStatisticsCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 4, 6, 1, 4),
    _AlarmStatisticsCount_Type()
)
alarmStatisticsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmStatisticsCount.setStatus("current")
_AlarmStatisticsCumulative_Type = Unsigned32
_AlarmStatisticsCumulative_Object = MibTableColumn
alarmStatisticsCumulative = _AlarmStatisticsCumulative_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 4, 6, 1, 5),
    _AlarmStatisticsCumulative_Type()
)
alarmStatisticsCumulative.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmStatisticsCumulative.setStatus("current")
_AlarmStatisticsType_Type = StringMaxl32
_AlarmStatisticsType_Object = MibTableColumn
alarmStatisticsType = _AlarmStatisticsType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 4, 6, 1, 6),
    _AlarmStatisticsType_Type()
)
alarmStatisticsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmStatisticsType.setStatus("current")

# Managed Objects groups

cienaWsPlatformAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 4, 2, 1, 1)
)
cienaWsPlatformAlarmGroup.setObjects(
      *(("CIENA-WS-PLATFORM-ALARM-MIB", "activeAlarmAcknowledged"),
        ("CIENA-WS-PLATFORM-ALARM-MIB", "activeAlarmTableId"),
        ("CIENA-WS-PLATFORM-ALARM-MIB", "activeAlarmSeverity"),
        ("CIENA-WS-PLATFORM-ALARM-MIB", "activeAlarmLocalDateTime"),
        ("CIENA-WS-PLATFORM-ALARM-MIB", "activeAlarmInstance"),
        ("CIENA-WS-PLATFORM-ALARM-MIB", "activeAlarmDescription"),
        ("CIENA-WS-PLATFORM-ALARM-MIB", "activeAlarmIntermittent"),
        ("CIENA-WS-PLATFORM-ALARM-MIB", "activeAlarmSiteIdentifier"),
        ("CIENA-WS-PLATFORM-ALARM-MIB", "activeAlarmGroupIdentifier"),
        ("CIENA-WS-PLATFORM-ALARM-MIB", "activeAlarmMemberIdentifier"),
        ("CIENA-WS-PLATFORM-ALARM-MIB", "historyAlarmReason"),
        ("CIENA-WS-PLATFORM-ALARM-MIB", "historyAlarmInstanceId"),
        ("CIENA-WS-PLATFORM-ALARM-MIB", "historyAlarmTableId"),
        ("CIENA-WS-PLATFORM-ALARM-MIB", "historyAlarmSeverity"),
        ("CIENA-WS-PLATFORM-ALARM-MIB", "historyAlarmLocalDateTime"),
        ("CIENA-WS-PLATFORM-ALARM-MIB", "historyAlarmInstance"),
        ("CIENA-WS-PLATFORM-ALARM-MIB", "historyAlarmDescription"),
        ("CIENA-WS-PLATFORM-ALARM-MIB", "historyAlarmSiteIdentifier"),
        ("CIENA-WS-PLATFORM-ALARM-MIB", "historyAlarmGroupIdentifier"),
        ("CIENA-WS-PLATFORM-ALARM-MIB", "historyAlarmMemberIdentifier"),
        ("CIENA-WS-PLATFORM-ALARM-MIB", "definedAlarmTableId"),
        ("CIENA-WS-PLATFORM-ALARM-MIB", "definedAlarmEnabled"),
        ("CIENA-WS-PLATFORM-ALARM-MIB", "definedAlarmActive"),
        ("CIENA-WS-PLATFORM-ALARM-MIB", "definedAlarmThreshold"),
        ("CIENA-WS-PLATFORM-ALARM-MIB", "definedAlarmCap"),
        ("CIENA-WS-PLATFORM-ALARM-MIB", "definedAlarmSeverity"),
        ("CIENA-WS-PLATFORM-ALARM-MIB", "definedAlarmInstance"),
        ("CIENA-WS-PLATFORM-ALARM-MIB", "definedAlarmDescription"),
        ("CIENA-WS-PLATFORM-ALARM-MIB", "alarmStatisticsActive"),
        ("CIENA-WS-PLATFORM-ALARM-MIB", "alarmStatisticsDisabled"),
        ("CIENA-WS-PLATFORM-ALARM-MIB", "alarmStatisticsCount"),
        ("CIENA-WS-PLATFORM-ALARM-MIB", "alarmStatisticsCumulative"),
        ("CIENA-WS-PLATFORM-ALARM-MIB", "alarmStatisticsType"))
)
if mibBuilder.loadTexts:
    cienaWsPlatformAlarmGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cienaWsPlatformAlarmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 4, 2, 2, 1)
)
cienaWsPlatformAlarmCompliance.setObjects(
    ("CIENA-WS-PLATFORM-ALARM-MIB", "cienaWsPlatformAlarmGroup")
)
if mibBuilder.loadTexts:
    cienaWsPlatformAlarmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-WS-PLATFORM-ALARM-MIB",
    **{"AlarmReason": AlarmReason,
       "AlarmSeverity": AlarmSeverity,
       "cienaWsPlatformAlarmMIB": cienaWsPlatformAlarmMIB,
       "cienaWsPlatformAlarmObjects": cienaWsPlatformAlarmObjects,
       "cienaWsPlatformAlarmConformance": cienaWsPlatformAlarmConformance,
       "cienaWsPlatformAlarmGroups": cienaWsPlatformAlarmGroups,
       "cienaWsPlatformAlarmGroup": cienaWsPlatformAlarmGroup,
       "cienaWsPlatformAlarmCompliances": cienaWsPlatformAlarmCompliances,
       "cienaWsPlatformAlarmCompliance": cienaWsPlatformAlarmCompliance,
       "activeAlarmTable": activeAlarmTable,
       "activeAlarmEntry": activeAlarmEntry,
       "activeAlarmInstanceId": activeAlarmInstanceId,
       "activeAlarmAcknowledged": activeAlarmAcknowledged,
       "activeAlarmTableId": activeAlarmTableId,
       "activeAlarmSeverity": activeAlarmSeverity,
       "activeAlarmLocalDateTime": activeAlarmLocalDateTime,
       "activeAlarmInstance": activeAlarmInstance,
       "activeAlarmDescription": activeAlarmDescription,
       "activeAlarmIntermittent": activeAlarmIntermittent,
       "activeAlarmSiteIdentifier": activeAlarmSiteIdentifier,
       "activeAlarmGroupIdentifier": activeAlarmGroupIdentifier,
       "activeAlarmMemberIdentifier": activeAlarmMemberIdentifier,
       "historyAlarmTable": historyAlarmTable,
       "historyAlarmEntry": historyAlarmEntry,
       "historyAlarmId": historyAlarmId,
       "historyAlarmReason": historyAlarmReason,
       "historyAlarmInstanceId": historyAlarmInstanceId,
       "historyAlarmTableId": historyAlarmTableId,
       "historyAlarmSeverity": historyAlarmSeverity,
       "historyAlarmLocalDateTime": historyAlarmLocalDateTime,
       "historyAlarmInstance": historyAlarmInstance,
       "historyAlarmDescription": historyAlarmDescription,
       "historyAlarmSiteIdentifier": historyAlarmSiteIdentifier,
       "historyAlarmGroupIdentifier": historyAlarmGroupIdentifier,
       "historyAlarmMemberIdentifier": historyAlarmMemberIdentifier,
       "definedAlarmTable": definedAlarmTable,
       "definedAlarmEntry": definedAlarmEntry,
       "definedAlarmId": definedAlarmId,
       "definedAlarmTableId": definedAlarmTableId,
       "definedAlarmEnabled": definedAlarmEnabled,
       "definedAlarmActive": definedAlarmActive,
       "definedAlarmThreshold": definedAlarmThreshold,
       "definedAlarmCap": definedAlarmCap,
       "definedAlarmSeverity": definedAlarmSeverity,
       "definedAlarmInstance": definedAlarmInstance,
       "definedAlarmDescription": definedAlarmDescription,
       "alarmStatisticsTable": alarmStatisticsTable,
       "alarmStatisticsEntry": alarmStatisticsEntry,
       "alarmStatisticsIndex": alarmStatisticsIndex,
       "alarmStatisticsActive": alarmStatisticsActive,
       "alarmStatisticsDisabled": alarmStatisticsDisabled,
       "alarmStatisticsCount": alarmStatisticsCount,
       "alarmStatisticsCumulative": alarmStatisticsCumulative,
       "alarmStatisticsType": alarmStatisticsType}
)
