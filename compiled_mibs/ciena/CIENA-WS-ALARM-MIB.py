# SNMP MIB module (CIENA-WS-ALARM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ciena\CIENA-WS-ALARM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:25:02 2025
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

(cienaWsConfig,) = mibBuilder.importSymbols(
    "CIENA-WS-MIB",
    "cienaWsConfig")

(StringMaxl16,
 StringMaxl32,
 StringMaxl44) = mibBuilder.importSymbols(
    "CIENA-WS-TYPEDEFS-MIB",
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

cienaWsAlarmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 4)
)
if mibBuilder.loadTexts:
    cienaWsAlarmMIB.setRevisions(
        ("2017-03-14 00:00",
         "2016-12-12 00:00",
         "2016-06-27 00:00",
         "2015-05-20 00:00")
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("reset", 1),
          ("set", 2),
          ("acknowledge", 5),
          ("clear", 6),
          ("delete", 7),
          ("config", 9))
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

_CienaWsAlarmObjects_ObjectIdentity = ObjectIdentity
cienaWsAlarmObjects = _CienaWsAlarmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 4, 1)
)
_CienaWsAlarmConformance_ObjectIdentity = ObjectIdentity
cienaWsAlarmConformance = _CienaWsAlarmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 4, 2)
)
_CienaWsAlarmGroups_ObjectIdentity = ObjectIdentity
cienaWsAlarmGroups = _CienaWsAlarmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 4, 2, 1)
)
_CienaWsAlarmCompliances_ObjectIdentity = ObjectIdentity
cienaWsAlarmCompliances = _CienaWsAlarmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 4, 2, 2)
)
_CwsAlarmActiveTable_Object = MibTable
cwsAlarmActiveTable = _CwsAlarmActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 4, 3)
)
if mibBuilder.loadTexts:
    cwsAlarmActiveTable.setStatus("current")
_CwsAlarmActiveEntry_Object = MibTableRow
cwsAlarmActiveEntry = _CwsAlarmActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 4, 3, 1)
)
cwsAlarmActiveEntry.setIndexNames(
    (0, "CIENA-WS-ALARM-MIB", "cwsAlarmActiveAlarmInstanceId"),
)
if mibBuilder.loadTexts:
    cwsAlarmActiveEntry.setStatus("current")


class _CwsAlarmActiveAlarmInstanceId_Type(Integer32):
    """Custom type cwsAlarmActiveAlarmInstanceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsAlarmActiveAlarmInstanceId_Type.__name__ = "Integer32"
_CwsAlarmActiveAlarmInstanceId_Object = MibTableColumn
cwsAlarmActiveAlarmInstanceId = _CwsAlarmActiveAlarmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 4, 3, 1, 1),
    _CwsAlarmActiveAlarmInstanceId_Type()
)
cwsAlarmActiveAlarmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsAlarmActiveAlarmInstanceId.setStatus("current")
_CwsAlarmActiveAcknowledged_Type = TruthValue
_CwsAlarmActiveAcknowledged_Object = MibTableColumn
cwsAlarmActiveAcknowledged = _CwsAlarmActiveAcknowledged_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 4, 3, 1, 2),
    _CwsAlarmActiveAcknowledged_Type()
)
cwsAlarmActiveAcknowledged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsAlarmActiveAcknowledged.setStatus("current")
_CwsAlarmActiveAlarmTableId_Type = Unsigned32
_CwsAlarmActiveAlarmTableId_Object = MibTableColumn
cwsAlarmActiveAlarmTableId = _CwsAlarmActiveAlarmTableId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 4, 3, 1, 3),
    _CwsAlarmActiveAlarmTableId_Type()
)
cwsAlarmActiveAlarmTableId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsAlarmActiveAlarmTableId.setStatus("current")
_CwsAlarmActiveSeverity_Type = AlarmSeverity
_CwsAlarmActiveSeverity_Object = MibTableColumn
cwsAlarmActiveSeverity = _CwsAlarmActiveSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 4, 3, 1, 4),
    _CwsAlarmActiveSeverity_Type()
)
cwsAlarmActiveSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsAlarmActiveSeverity.setStatus("current")
_CwsAlarmActiveLocalDateTime_Type = StringMaxl32
_CwsAlarmActiveLocalDateTime_Object = MibTableColumn
cwsAlarmActiveLocalDateTime = _CwsAlarmActiveLocalDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 4, 3, 1, 5),
    _CwsAlarmActiveLocalDateTime_Type()
)
cwsAlarmActiveLocalDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsAlarmActiveLocalDateTime.setStatus("current")
_CwsAlarmActiveInstance_Type = StringMaxl32
_CwsAlarmActiveInstance_Object = MibTableColumn
cwsAlarmActiveInstance = _CwsAlarmActiveInstance_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 4, 3, 1, 6),
    _CwsAlarmActiveInstance_Type()
)
cwsAlarmActiveInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsAlarmActiveInstance.setStatus("current")
_CwsAlarmActiveDescription_Type = StringMaxl44
_CwsAlarmActiveDescription_Object = MibTableColumn
cwsAlarmActiveDescription = _CwsAlarmActiveDescription_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 4, 3, 1, 7),
    _CwsAlarmActiveDescription_Type()
)
cwsAlarmActiveDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsAlarmActiveDescription.setStatus("current")
_CwsAlarmActiveSiteIdentifier_Type = Unsigned32
_CwsAlarmActiveSiteIdentifier_Object = MibTableColumn
cwsAlarmActiveSiteIdentifier = _CwsAlarmActiveSiteIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 4, 3, 1, 8),
    _CwsAlarmActiveSiteIdentifier_Type()
)
cwsAlarmActiveSiteIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsAlarmActiveSiteIdentifier.setStatus("current")
_CwsAlarmActiveGroupIdentifier_Type = Unsigned32
_CwsAlarmActiveGroupIdentifier_Object = MibTableColumn
cwsAlarmActiveGroupIdentifier = _CwsAlarmActiveGroupIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 4, 3, 1, 9),
    _CwsAlarmActiveGroupIdentifier_Type()
)
cwsAlarmActiveGroupIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsAlarmActiveGroupIdentifier.setStatus("current")
_CwsAlarmActiveMemberIdentifier_Type = Unsigned32
_CwsAlarmActiveMemberIdentifier_Object = MibTableColumn
cwsAlarmActiveMemberIdentifier = _CwsAlarmActiveMemberIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 4, 3, 1, 10),
    _CwsAlarmActiveMemberIdentifier_Type()
)
cwsAlarmActiveMemberIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsAlarmActiveMemberIdentifier.setStatus("current")
_CwsAlarmHistoryTable_Object = MibTable
cwsAlarmHistoryTable = _CwsAlarmHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 4, 4)
)
if mibBuilder.loadTexts:
    cwsAlarmHistoryTable.setStatus("current")
_CwsAlarmHistoryEntry_Object = MibTableRow
cwsAlarmHistoryEntry = _CwsAlarmHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 4, 4, 1)
)
cwsAlarmHistoryEntry.setIndexNames(
    (0, "CIENA-WS-ALARM-MIB", "cwsAlarmHistoryHistoryId"),
)
if mibBuilder.loadTexts:
    cwsAlarmHistoryEntry.setStatus("current")


class _CwsAlarmHistoryHistoryId_Type(Integer32):
    """Custom type cwsAlarmHistoryHistoryId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsAlarmHistoryHistoryId_Type.__name__ = "Integer32"
_CwsAlarmHistoryHistoryId_Object = MibTableColumn
cwsAlarmHistoryHistoryId = _CwsAlarmHistoryHistoryId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 4, 4, 1, 1),
    _CwsAlarmHistoryHistoryId_Type()
)
cwsAlarmHistoryHistoryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsAlarmHistoryHistoryId.setStatus("current")
_CwsAlarmHistoryReason_Type = AlarmReason
_CwsAlarmHistoryReason_Object = MibTableColumn
cwsAlarmHistoryReason = _CwsAlarmHistoryReason_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 4, 4, 1, 2),
    _CwsAlarmHistoryReason_Type()
)
cwsAlarmHistoryReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsAlarmHistoryReason.setStatus("current")
_CwsAlarmHistoryAlarmInstanceId_Type = Unsigned32
_CwsAlarmHistoryAlarmInstanceId_Object = MibTableColumn
cwsAlarmHistoryAlarmInstanceId = _CwsAlarmHistoryAlarmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 4, 4, 1, 3),
    _CwsAlarmHistoryAlarmInstanceId_Type()
)
cwsAlarmHistoryAlarmInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsAlarmHistoryAlarmInstanceId.setStatus("current")
_CwsAlarmHistoryAlarmTableId_Type = Unsigned32
_CwsAlarmHistoryAlarmTableId_Object = MibTableColumn
cwsAlarmHistoryAlarmTableId = _CwsAlarmHistoryAlarmTableId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 4, 4, 1, 4),
    _CwsAlarmHistoryAlarmTableId_Type()
)
cwsAlarmHistoryAlarmTableId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsAlarmHistoryAlarmTableId.setStatus("current")
_CwsAlarmHistorySeverity_Type = AlarmSeverity
_CwsAlarmHistorySeverity_Object = MibTableColumn
cwsAlarmHistorySeverity = _CwsAlarmHistorySeverity_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 4, 4, 1, 5),
    _CwsAlarmHistorySeverity_Type()
)
cwsAlarmHistorySeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsAlarmHistorySeverity.setStatus("current")
_CwsAlarmHistoryLocalDateTime_Type = StringMaxl32
_CwsAlarmHistoryLocalDateTime_Object = MibTableColumn
cwsAlarmHistoryLocalDateTime = _CwsAlarmHistoryLocalDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 4, 4, 1, 6),
    _CwsAlarmHistoryLocalDateTime_Type()
)
cwsAlarmHistoryLocalDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsAlarmHistoryLocalDateTime.setStatus("current")
_CwsAlarmHistoryInstance_Type = StringMaxl32
_CwsAlarmHistoryInstance_Object = MibTableColumn
cwsAlarmHistoryInstance = _CwsAlarmHistoryInstance_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 4, 4, 1, 7),
    _CwsAlarmHistoryInstance_Type()
)
cwsAlarmHistoryInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsAlarmHistoryInstance.setStatus("current")
_CwsAlarmHistoryDescription_Type = StringMaxl44
_CwsAlarmHistoryDescription_Object = MibTableColumn
cwsAlarmHistoryDescription = _CwsAlarmHistoryDescription_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 4, 4, 1, 8),
    _CwsAlarmHistoryDescription_Type()
)
cwsAlarmHistoryDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsAlarmHistoryDescription.setStatus("current")
_CwsAlarmHistorySiteIdentifier_Type = Unsigned32
_CwsAlarmHistorySiteIdentifier_Object = MibTableColumn
cwsAlarmHistorySiteIdentifier = _CwsAlarmHistorySiteIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 4, 4, 1, 9),
    _CwsAlarmHistorySiteIdentifier_Type()
)
cwsAlarmHistorySiteIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsAlarmHistorySiteIdentifier.setStatus("current")
_CwsAlarmHistoryGroupIdentifier_Type = Unsigned32
_CwsAlarmHistoryGroupIdentifier_Object = MibTableColumn
cwsAlarmHistoryGroupIdentifier = _CwsAlarmHistoryGroupIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 4, 4, 1, 10),
    _CwsAlarmHistoryGroupIdentifier_Type()
)
cwsAlarmHistoryGroupIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsAlarmHistoryGroupIdentifier.setStatus("current")
_CwsAlarmHistoryMemberIdentifier_Type = Unsigned32
_CwsAlarmHistoryMemberIdentifier_Object = MibTableColumn
cwsAlarmHistoryMemberIdentifier = _CwsAlarmHistoryMemberIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 4, 4, 1, 11),
    _CwsAlarmHistoryMemberIdentifier_Type()
)
cwsAlarmHistoryMemberIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsAlarmHistoryMemberIdentifier.setStatus("current")
_CwsAlarmDefinedTable_Object = MibTable
cwsAlarmDefinedTable = _CwsAlarmDefinedTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 4, 5)
)
if mibBuilder.loadTexts:
    cwsAlarmDefinedTable.setStatus("current")
_CwsAlarmDefinedEntry_Object = MibTableRow
cwsAlarmDefinedEntry = _CwsAlarmDefinedEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 4, 5, 1)
)
cwsAlarmDefinedEntry.setIndexNames(
    (0, "CIENA-WS-ALARM-MIB", "cwsAlarmDefinedAlarmTableId"),
)
if mibBuilder.loadTexts:
    cwsAlarmDefinedEntry.setStatus("current")


class _CwsAlarmDefinedAlarmTableId_Type(Integer32):
    """Custom type cwsAlarmDefinedAlarmTableId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsAlarmDefinedAlarmTableId_Type.__name__ = "Integer32"
_CwsAlarmDefinedAlarmTableId_Object = MibTableColumn
cwsAlarmDefinedAlarmTableId = _CwsAlarmDefinedAlarmTableId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 4, 5, 1, 1),
    _CwsAlarmDefinedAlarmTableId_Type()
)
cwsAlarmDefinedAlarmTableId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsAlarmDefinedAlarmTableId.setStatus("current")
_CwsAlarmDefinedEnabled_Type = TruthValue
_CwsAlarmDefinedEnabled_Object = MibTableColumn
cwsAlarmDefinedEnabled = _CwsAlarmDefinedEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 4, 5, 1, 2),
    _CwsAlarmDefinedEnabled_Type()
)
cwsAlarmDefinedEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsAlarmDefinedEnabled.setStatus("current")
_CwsAlarmDefinedActive_Type = TruthValue
_CwsAlarmDefinedActive_Object = MibTableColumn
cwsAlarmDefinedActive = _CwsAlarmDefinedActive_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 4, 5, 1, 3),
    _CwsAlarmDefinedActive_Type()
)
cwsAlarmDefinedActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsAlarmDefinedActive.setStatus("current")
_CwsAlarmDefinedThreshold_Type = Unsigned32
_CwsAlarmDefinedThreshold_Object = MibTableColumn
cwsAlarmDefinedThreshold = _CwsAlarmDefinedThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 4, 5, 1, 4),
    _CwsAlarmDefinedThreshold_Type()
)
cwsAlarmDefinedThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsAlarmDefinedThreshold.setStatus("current")
_CwsAlarmDefinedCap_Type = Unsigned32
_CwsAlarmDefinedCap_Object = MibTableColumn
cwsAlarmDefinedCap = _CwsAlarmDefinedCap_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 4, 5, 1, 5),
    _CwsAlarmDefinedCap_Type()
)
cwsAlarmDefinedCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsAlarmDefinedCap.setStatus("current")
_CwsAlarmDefinedSeverity_Type = AlarmSeverity
_CwsAlarmDefinedSeverity_Object = MibTableColumn
cwsAlarmDefinedSeverity = _CwsAlarmDefinedSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 4, 5, 1, 6),
    _CwsAlarmDefinedSeverity_Type()
)
cwsAlarmDefinedSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsAlarmDefinedSeverity.setStatus("current")
_CwsAlarmDefinedInstance_Type = StringMaxl16
_CwsAlarmDefinedInstance_Object = MibTableColumn
cwsAlarmDefinedInstance = _CwsAlarmDefinedInstance_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 4, 5, 1, 7),
    _CwsAlarmDefinedInstance_Type()
)
cwsAlarmDefinedInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsAlarmDefinedInstance.setStatus("current")
_CwsAlarmDefinedDescription_Type = StringMaxl44
_CwsAlarmDefinedDescription_Object = MibTableColumn
cwsAlarmDefinedDescription = _CwsAlarmDefinedDescription_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 4, 5, 1, 8),
    _CwsAlarmDefinedDescription_Type()
)
cwsAlarmDefinedDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsAlarmDefinedDescription.setStatus("current")
_CwsAlarmStatisticsTable_Object = MibTable
cwsAlarmStatisticsTable = _CwsAlarmStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 4, 6)
)
if mibBuilder.loadTexts:
    cwsAlarmStatisticsTable.setStatus("current")
_CwsAlarmStatisticsEntry_Object = MibTableRow
cwsAlarmStatisticsEntry = _CwsAlarmStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 4, 6, 1)
)
cwsAlarmStatisticsEntry.setIndexNames(
    (0, "CIENA-WS-ALARM-MIB", "cwsAlarmStatisticsIndex"),
)
if mibBuilder.loadTexts:
    cwsAlarmStatisticsEntry.setStatus("current")


class _CwsAlarmStatisticsIndex_Type(Integer32):
    """Custom type cwsAlarmStatisticsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsAlarmStatisticsIndex_Type.__name__ = "Integer32"
_CwsAlarmStatisticsIndex_Object = MibTableColumn
cwsAlarmStatisticsIndex = _CwsAlarmStatisticsIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 4, 6, 1, 1),
    _CwsAlarmStatisticsIndex_Type()
)
cwsAlarmStatisticsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsAlarmStatisticsIndex.setStatus("current")
_CwsAlarmStatisticsActive_Type = TruthValue
_CwsAlarmStatisticsActive_Object = MibTableColumn
cwsAlarmStatisticsActive = _CwsAlarmStatisticsActive_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 4, 6, 1, 2),
    _CwsAlarmStatisticsActive_Type()
)
cwsAlarmStatisticsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsAlarmStatisticsActive.setStatus("current")
_CwsAlarmStatisticsDisabled_Type = TruthValue
_CwsAlarmStatisticsDisabled_Object = MibTableColumn
cwsAlarmStatisticsDisabled = _CwsAlarmStatisticsDisabled_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 4, 6, 1, 3),
    _CwsAlarmStatisticsDisabled_Type()
)
cwsAlarmStatisticsDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsAlarmStatisticsDisabled.setStatus("current")
_CwsAlarmStatisticsCount_Type = Unsigned32
_CwsAlarmStatisticsCount_Object = MibTableColumn
cwsAlarmStatisticsCount = _CwsAlarmStatisticsCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 4, 6, 1, 4),
    _CwsAlarmStatisticsCount_Type()
)
cwsAlarmStatisticsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsAlarmStatisticsCount.setStatus("current")
_CwsAlarmStatisticsCumulative_Type = Unsigned32
_CwsAlarmStatisticsCumulative_Object = MibTableColumn
cwsAlarmStatisticsCumulative = _CwsAlarmStatisticsCumulative_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 4, 6, 1, 5),
    _CwsAlarmStatisticsCumulative_Type()
)
cwsAlarmStatisticsCumulative.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsAlarmStatisticsCumulative.setStatus("current")
_CwsAlarmStatisticsType_Type = StringMaxl32
_CwsAlarmStatisticsType_Object = MibTableColumn
cwsAlarmStatisticsType = _CwsAlarmStatisticsType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 4, 6, 1, 6),
    _CwsAlarmStatisticsType_Type()
)
cwsAlarmStatisticsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsAlarmStatisticsType.setStatus("current")

# Managed Objects groups

cienaWsAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 4, 2, 1, 1)
)
cienaWsAlarmGroup.setObjects(
      *(("CIENA-WS-ALARM-MIB", "cwsAlarmActiveAcknowledged"),
        ("CIENA-WS-ALARM-MIB", "cwsAlarmActiveAlarmTableId"),
        ("CIENA-WS-ALARM-MIB", "cwsAlarmActiveSeverity"),
        ("CIENA-WS-ALARM-MIB", "cwsAlarmActiveLocalDateTime"),
        ("CIENA-WS-ALARM-MIB", "cwsAlarmActiveInstance"),
        ("CIENA-WS-ALARM-MIB", "cwsAlarmActiveDescription"),
        ("CIENA-WS-ALARM-MIB", "cwsAlarmActiveSiteIdentifier"),
        ("CIENA-WS-ALARM-MIB", "cwsAlarmActiveGroupIdentifier"),
        ("CIENA-WS-ALARM-MIB", "cwsAlarmActiveMemberIdentifier"),
        ("CIENA-WS-ALARM-MIB", "cwsAlarmHistoryReason"),
        ("CIENA-WS-ALARM-MIB", "cwsAlarmHistoryAlarmInstanceId"),
        ("CIENA-WS-ALARM-MIB", "cwsAlarmHistoryAlarmTableId"),
        ("CIENA-WS-ALARM-MIB", "cwsAlarmHistorySeverity"),
        ("CIENA-WS-ALARM-MIB", "cwsAlarmHistoryLocalDateTime"),
        ("CIENA-WS-ALARM-MIB", "cwsAlarmHistoryInstance"),
        ("CIENA-WS-ALARM-MIB", "cwsAlarmHistoryDescription"),
        ("CIENA-WS-ALARM-MIB", "cwsAlarmHistorySiteIdentifier"),
        ("CIENA-WS-ALARM-MIB", "cwsAlarmHistoryGroupIdentifier"),
        ("CIENA-WS-ALARM-MIB", "cwsAlarmHistoryMemberIdentifier"),
        ("CIENA-WS-ALARM-MIB", "cwsAlarmDefinedEnabled"),
        ("CIENA-WS-ALARM-MIB", "cwsAlarmDefinedActive"),
        ("CIENA-WS-ALARM-MIB", "cwsAlarmDefinedThreshold"),
        ("CIENA-WS-ALARM-MIB", "cwsAlarmDefinedCap"),
        ("CIENA-WS-ALARM-MIB", "cwsAlarmDefinedSeverity"),
        ("CIENA-WS-ALARM-MIB", "cwsAlarmDefinedInstance"),
        ("CIENA-WS-ALARM-MIB", "cwsAlarmDefinedDescription"),
        ("CIENA-WS-ALARM-MIB", "cwsAlarmStatisticsActive"),
        ("CIENA-WS-ALARM-MIB", "cwsAlarmStatisticsDisabled"),
        ("CIENA-WS-ALARM-MIB", "cwsAlarmStatisticsCount"),
        ("CIENA-WS-ALARM-MIB", "cwsAlarmStatisticsCumulative"),
        ("CIENA-WS-ALARM-MIB", "cwsAlarmStatisticsType"))
)
if mibBuilder.loadTexts:
    cienaWsAlarmGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cienaWsAlarmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 4, 2, 2, 1)
)
cienaWsAlarmCompliance.setObjects(
    ("CIENA-WS-ALARM-MIB", "cienaWsAlarmGroup")
)
if mibBuilder.loadTexts:
    cienaWsAlarmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-WS-ALARM-MIB",
    **{"AlarmReason": AlarmReason,
       "AlarmSeverity": AlarmSeverity,
       "cienaWsAlarmMIB": cienaWsAlarmMIB,
       "cienaWsAlarmObjects": cienaWsAlarmObjects,
       "cienaWsAlarmConformance": cienaWsAlarmConformance,
       "cienaWsAlarmGroups": cienaWsAlarmGroups,
       "cienaWsAlarmGroup": cienaWsAlarmGroup,
       "cienaWsAlarmCompliances": cienaWsAlarmCompliances,
       "cienaWsAlarmCompliance": cienaWsAlarmCompliance,
       "cwsAlarmActiveTable": cwsAlarmActiveTable,
       "cwsAlarmActiveEntry": cwsAlarmActiveEntry,
       "cwsAlarmActiveAlarmInstanceId": cwsAlarmActiveAlarmInstanceId,
       "cwsAlarmActiveAcknowledged": cwsAlarmActiveAcknowledged,
       "cwsAlarmActiveAlarmTableId": cwsAlarmActiveAlarmTableId,
       "cwsAlarmActiveSeverity": cwsAlarmActiveSeverity,
       "cwsAlarmActiveLocalDateTime": cwsAlarmActiveLocalDateTime,
       "cwsAlarmActiveInstance": cwsAlarmActiveInstance,
       "cwsAlarmActiveDescription": cwsAlarmActiveDescription,
       "cwsAlarmActiveSiteIdentifier": cwsAlarmActiveSiteIdentifier,
       "cwsAlarmActiveGroupIdentifier": cwsAlarmActiveGroupIdentifier,
       "cwsAlarmActiveMemberIdentifier": cwsAlarmActiveMemberIdentifier,
       "cwsAlarmHistoryTable": cwsAlarmHistoryTable,
       "cwsAlarmHistoryEntry": cwsAlarmHistoryEntry,
       "cwsAlarmHistoryHistoryId": cwsAlarmHistoryHistoryId,
       "cwsAlarmHistoryReason": cwsAlarmHistoryReason,
       "cwsAlarmHistoryAlarmInstanceId": cwsAlarmHistoryAlarmInstanceId,
       "cwsAlarmHistoryAlarmTableId": cwsAlarmHistoryAlarmTableId,
       "cwsAlarmHistorySeverity": cwsAlarmHistorySeverity,
       "cwsAlarmHistoryLocalDateTime": cwsAlarmHistoryLocalDateTime,
       "cwsAlarmHistoryInstance": cwsAlarmHistoryInstance,
       "cwsAlarmHistoryDescription": cwsAlarmHistoryDescription,
       "cwsAlarmHistorySiteIdentifier": cwsAlarmHistorySiteIdentifier,
       "cwsAlarmHistoryGroupIdentifier": cwsAlarmHistoryGroupIdentifier,
       "cwsAlarmHistoryMemberIdentifier": cwsAlarmHistoryMemberIdentifier,
       "cwsAlarmDefinedTable": cwsAlarmDefinedTable,
       "cwsAlarmDefinedEntry": cwsAlarmDefinedEntry,
       "cwsAlarmDefinedAlarmTableId": cwsAlarmDefinedAlarmTableId,
       "cwsAlarmDefinedEnabled": cwsAlarmDefinedEnabled,
       "cwsAlarmDefinedActive": cwsAlarmDefinedActive,
       "cwsAlarmDefinedThreshold": cwsAlarmDefinedThreshold,
       "cwsAlarmDefinedCap": cwsAlarmDefinedCap,
       "cwsAlarmDefinedSeverity": cwsAlarmDefinedSeverity,
       "cwsAlarmDefinedInstance": cwsAlarmDefinedInstance,
       "cwsAlarmDefinedDescription": cwsAlarmDefinedDescription,
       "cwsAlarmStatisticsTable": cwsAlarmStatisticsTable,
       "cwsAlarmStatisticsEntry": cwsAlarmStatisticsEntry,
       "cwsAlarmStatisticsIndex": cwsAlarmStatisticsIndex,
       "cwsAlarmStatisticsActive": cwsAlarmStatisticsActive,
       "cwsAlarmStatisticsDisabled": cwsAlarmStatisticsDisabled,
       "cwsAlarmStatisticsCount": cwsAlarmStatisticsCount,
       "cwsAlarmStatisticsCumulative": cwsAlarmStatisticsCumulative,
       "cwsAlarmStatisticsType": cwsAlarmStatisticsType}
)
