# SNMP MIB module (DCP-ALARM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\smartoptics\DCP-ALARM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:28:19 2025
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

(dcpGeneric,) = mibBuilder.importSymbols(
    "DCP-MIB",
    "dcpGeneric")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(ItuPerceivedSeverity,) = mibBuilder.importSymbols(
    "SO-TC-MIB",
    "ItuPerceivedSeverity")


# MODULE-IDENTITY

dcpAlarm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 2)
)
if mibBuilder.loadTexts:
    dcpAlarm.setRevisions(
        ("2020-06-24 08:00",
         "2018-10-08 14:44")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class DcpAlarmIndex(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 29999),
    )



# MIB Managed Objects in the order of their OIDs

_DcpAlarmGeneral_ObjectIdentity = ObjectIdentity
dcpAlarmGeneral = _DcpAlarmGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 2, 1)
)
_DcpAlarmGeneralList_ObjectIdentity = ObjectIdentity
dcpAlarmGeneralList = _DcpAlarmGeneralList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 2, 1, 1)
)
_DcpAlarmGeneralHighestSeverity_Type = ItuPerceivedSeverity
_DcpAlarmGeneralHighestSeverity_Object = MibScalar
dcpAlarmGeneralHighestSeverity = _DcpAlarmGeneralHighestSeverity_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 2, 1, 1, 1),
    _DcpAlarmGeneralHighestSeverity_Type()
)
dcpAlarmGeneralHighestSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpAlarmGeneralHighestSeverity.setStatus("current")
_DcpAlarmGeneralActiveCritical_Type = Unsigned32
_DcpAlarmGeneralActiveCritical_Object = MibScalar
dcpAlarmGeneralActiveCritical = _DcpAlarmGeneralActiveCritical_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 2, 1, 1, 2),
    _DcpAlarmGeneralActiveCritical_Type()
)
dcpAlarmGeneralActiveCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpAlarmGeneralActiveCritical.setStatus("current")
_DcpAlarmGeneralActiveMajor_Type = Unsigned32
_DcpAlarmGeneralActiveMajor_Object = MibScalar
dcpAlarmGeneralActiveMajor = _DcpAlarmGeneralActiveMajor_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 2, 1, 1, 3),
    _DcpAlarmGeneralActiveMajor_Type()
)
dcpAlarmGeneralActiveMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpAlarmGeneralActiveMajor.setStatus("current")
_DcpAlarmGeneralActiveMinor_Type = Unsigned32
_DcpAlarmGeneralActiveMinor_Object = MibScalar
dcpAlarmGeneralActiveMinor = _DcpAlarmGeneralActiveMinor_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 2, 1, 1, 4),
    _DcpAlarmGeneralActiveMinor_Type()
)
dcpAlarmGeneralActiveMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpAlarmGeneralActiveMinor.setStatus("current")
_DcpAlarmGeneralActiveWarning_Type = Unsigned32
_DcpAlarmGeneralActiveWarning_Object = MibScalar
dcpAlarmGeneralActiveWarning = _DcpAlarmGeneralActiveWarning_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 2, 1, 1, 5),
    _DcpAlarmGeneralActiveWarning_Type()
)
dcpAlarmGeneralActiveWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpAlarmGeneralActiveWarning.setStatus("current")
_DcpAlarmGeneralNumberActiveList_Type = Unsigned32
_DcpAlarmGeneralNumberActiveList_Object = MibScalar
dcpAlarmGeneralNumberActiveList = _DcpAlarmGeneralNumberActiveList_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 2, 1, 1, 6),
    _DcpAlarmGeneralNumberActiveList_Type()
)
dcpAlarmGeneralNumberActiveList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpAlarmGeneralNumberActiveList.setStatus("current")
_DcpAlarmGeneralNumberLogList_Type = Unsigned32
_DcpAlarmGeneralNumberLogList_Object = MibScalar
dcpAlarmGeneralNumberLogList = _DcpAlarmGeneralNumberLogList_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 2, 1, 1, 7),
    _DcpAlarmGeneralNumberLogList_Type()
)
dcpAlarmGeneralNumberLogList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpAlarmGeneralNumberLogList.setStatus("current")
_DcpAlarmGeneralLastTrapSeqNumber_Type = Unsigned32
_DcpAlarmGeneralLastTrapSeqNumber_Object = MibScalar
dcpAlarmGeneralLastTrapSeqNumber = _DcpAlarmGeneralLastTrapSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 2, 1, 1, 8),
    _DcpAlarmGeneralLastTrapSeqNumber_Type()
)
dcpAlarmGeneralLastTrapSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpAlarmGeneralLastTrapSeqNumber.setStatus("current")
_DcpAlarmObjects_ObjectIdentity = ObjectIdentity
dcpAlarmObjects = _DcpAlarmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 2, 2)
)
_DcpAlarmActiveListTable_Object = MibTable
dcpAlarmActiveListTable = _DcpAlarmActiveListTable_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    dcpAlarmActiveListTable.setStatus("current")
_DcpAlarmActiveListEntry_Object = MibTableRow
dcpAlarmActiveListEntry = _DcpAlarmActiveListEntry_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 2, 2, 1, 1)
)
dcpAlarmActiveListEntry.setIndexNames(
    (0, "DCP-ALARM-MIB", "dcpAlarmActiveListIndex"),
)
if mibBuilder.loadTexts:
    dcpAlarmActiveListEntry.setStatus("current")
_DcpAlarmActiveListIndex_Type = DcpAlarmIndex
_DcpAlarmActiveListIndex_Object = MibTableColumn
dcpAlarmActiveListIndex = _DcpAlarmActiveListIndex_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 2, 2, 1, 1, 1),
    _DcpAlarmActiveListIndex_Type()
)
dcpAlarmActiveListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpAlarmActiveListIndex.setStatus("current")
_DcpAlarmActiveListLocation_Type = DisplayString
_DcpAlarmActiveListLocation_Object = MibTableColumn
dcpAlarmActiveListLocation = _DcpAlarmActiveListLocation_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 2, 2, 1, 1, 2),
    _DcpAlarmActiveListLocation_Type()
)
dcpAlarmActiveListLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpAlarmActiveListLocation.setStatus("current")
_DcpAlarmActiveListInterfaceName_Type = DisplayString
_DcpAlarmActiveListInterfaceName_Object = MibTableColumn
dcpAlarmActiveListInterfaceName = _DcpAlarmActiveListInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 2, 2, 1, 1, 3),
    _DcpAlarmActiveListInterfaceName_Type()
)
dcpAlarmActiveListInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpAlarmActiveListInterfaceName.setStatus("current")
_DcpAlarmActiveListText_Type = DisplayString
_DcpAlarmActiveListText_Object = MibTableColumn
dcpAlarmActiveListText = _DcpAlarmActiveListText_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 2, 2, 1, 1, 4),
    _DcpAlarmActiveListText_Type()
)
dcpAlarmActiveListText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpAlarmActiveListText.setStatus("current")
_DcpAlarmActiveListSeverity_Type = ItuPerceivedSeverity
_DcpAlarmActiveListSeverity_Object = MibTableColumn
dcpAlarmActiveListSeverity = _DcpAlarmActiveListSeverity_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 2, 2, 1, 1, 5),
    _DcpAlarmActiveListSeverity_Type()
)
dcpAlarmActiveListSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpAlarmActiveListSeverity.setStatus("current")
_DcpAlarmActiveListStartTime_Type = DateAndTime
_DcpAlarmActiveListStartTime_Object = MibTableColumn
dcpAlarmActiveListStartTime = _DcpAlarmActiveListStartTime_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 2, 2, 1, 1, 6),
    _DcpAlarmActiveListStartTime_Type()
)
dcpAlarmActiveListStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpAlarmActiveListStartTime.setStatus("current")
_DcpAlarmActiveListSeqNumber_Type = Unsigned32
_DcpAlarmActiveListSeqNumber_Object = MibTableColumn
dcpAlarmActiveListSeqNumber = _DcpAlarmActiveListSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 2, 2, 1, 1, 7),
    _DcpAlarmActiveListSeqNumber_Type()
)
dcpAlarmActiveListSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpAlarmActiveListSeqNumber.setStatus("current")


class _DcpAlarmActiveListInterfaceDescription_Type(DisplayString):
    """Custom type dcpAlarmActiveListInterfaceDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_DcpAlarmActiveListInterfaceDescription_Type.__name__ = "DisplayString"
_DcpAlarmActiveListInterfaceDescription_Object = MibTableColumn
dcpAlarmActiveListInterfaceDescription = _DcpAlarmActiveListInterfaceDescription_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 2, 2, 1, 1, 8),
    _DcpAlarmActiveListInterfaceDescription_Type()
)
dcpAlarmActiveListInterfaceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpAlarmActiveListInterfaceDescription.setStatus("current")
_DcpAlarmLogTable_Object = MibTable
dcpAlarmLogTable = _DcpAlarmLogTable_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 2, 2, 2)
)
if mibBuilder.loadTexts:
    dcpAlarmLogTable.setStatus("current")
_DcpAlarmLogEntry_Object = MibTableRow
dcpAlarmLogEntry = _DcpAlarmLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 2, 2, 2, 1)
)
dcpAlarmLogEntry.setIndexNames(
    (0, "DCP-ALARM-MIB", "dcpAlarmLogListIndex"),
)
if mibBuilder.loadTexts:
    dcpAlarmLogEntry.setStatus("current")
_DcpAlarmLogListIndex_Type = DcpAlarmIndex
_DcpAlarmLogListIndex_Object = MibTableColumn
dcpAlarmLogListIndex = _DcpAlarmLogListIndex_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 2, 2, 2, 1, 1),
    _DcpAlarmLogListIndex_Type()
)
dcpAlarmLogListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpAlarmLogListIndex.setStatus("current")
_DcpAlarmLogListLocation_Type = DisplayString
_DcpAlarmLogListLocation_Object = MibTableColumn
dcpAlarmLogListLocation = _DcpAlarmLogListLocation_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 2, 2, 2, 1, 2),
    _DcpAlarmLogListLocation_Type()
)
dcpAlarmLogListLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpAlarmLogListLocation.setStatus("current")
_DcpAlarmLogListInterfaceName_Type = DisplayString
_DcpAlarmLogListInterfaceName_Object = MibTableColumn
dcpAlarmLogListInterfaceName = _DcpAlarmLogListInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 2, 2, 2, 1, 3),
    _DcpAlarmLogListInterfaceName_Type()
)
dcpAlarmLogListInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpAlarmLogListInterfaceName.setStatus("current")
_DcpAlarmLogListText_Type = DisplayString
_DcpAlarmLogListText_Object = MibTableColumn
dcpAlarmLogListText = _DcpAlarmLogListText_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 2, 2, 2, 1, 4),
    _DcpAlarmLogListText_Type()
)
dcpAlarmLogListText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpAlarmLogListText.setStatus("current")
_DcpAlarmLogListSeverity_Type = ItuPerceivedSeverity
_DcpAlarmLogListSeverity_Object = MibTableColumn
dcpAlarmLogListSeverity = _DcpAlarmLogListSeverity_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 2, 2, 2, 1, 5),
    _DcpAlarmLogListSeverity_Type()
)
dcpAlarmLogListSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpAlarmLogListSeverity.setStatus("current")
_DcpAlarmLogListStartTime_Type = DateAndTime
_DcpAlarmLogListStartTime_Object = MibTableColumn
dcpAlarmLogListStartTime = _DcpAlarmLogListStartTime_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 2, 2, 2, 1, 6),
    _DcpAlarmLogListStartTime_Type()
)
dcpAlarmLogListStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpAlarmLogListStartTime.setStatus("current")
_DcpAlarmLogListEndTime_Type = DateAndTime
_DcpAlarmLogListEndTime_Object = MibTableColumn
dcpAlarmLogListEndTime = _DcpAlarmLogListEndTime_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 2, 2, 2, 1, 7),
    _DcpAlarmLogListEndTime_Type()
)
dcpAlarmLogListEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpAlarmLogListEndTime.setStatus("current")
_DcpAlarmLogListSeqNumber_Type = Unsigned32
_DcpAlarmLogListSeqNumber_Object = MibTableColumn
dcpAlarmLogListSeqNumber = _DcpAlarmLogListSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 2, 2, 2, 1, 8),
    _DcpAlarmLogListSeqNumber_Type()
)
dcpAlarmLogListSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpAlarmLogListSeqNumber.setStatus("current")


class _DcpAlarmLogListInterfaceDescription_Type(DisplayString):
    """Custom type dcpAlarmLogListInterfaceDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_DcpAlarmLogListInterfaceDescription_Type.__name__ = "DisplayString"
_DcpAlarmLogListInterfaceDescription_Object = MibTableColumn
dcpAlarmLogListInterfaceDescription = _DcpAlarmLogListInterfaceDescription_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 2, 2, 2, 1, 9),
    _DcpAlarmLogListInterfaceDescription_Type()
)
dcpAlarmLogListInterfaceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpAlarmLogListInterfaceDescription.setStatus("current")
_DcpAlarmMIBNotifications_ObjectIdentity = ObjectIdentity
dcpAlarmMIBNotifications = _DcpAlarmMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 2, 3)
)
_DcpAlarmNotification_ObjectIdentity = ObjectIdentity
dcpAlarmNotification = _DcpAlarmNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 2, 3, 0)
)
_DcpAlarmMIBCompliance_ObjectIdentity = ObjectIdentity
dcpAlarmMIBCompliance = _DcpAlarmMIBCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 2, 4)
)
_DcpAlarmMIBGroups_ObjectIdentity = ObjectIdentity
dcpAlarmMIBGroups = _DcpAlarmMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 2, 4, 1)
)
_DcpAlarmMIBCompliances_ObjectIdentity = ObjectIdentity
dcpAlarmMIBCompliances = _DcpAlarmMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 2, 4, 2)
)

# Managed Objects groups

dcpAlarmGeneralGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 2, 4, 1, 1)
)
dcpAlarmGeneralGroupV1.setObjects(
      *(("DCP-ALARM-MIB", "dcpAlarmGeneralHighestSeverity"),
        ("DCP-ALARM-MIB", "dcpAlarmGeneralActiveCritical"),
        ("DCP-ALARM-MIB", "dcpAlarmGeneralActiveMajor"),
        ("DCP-ALARM-MIB", "dcpAlarmGeneralActiveMinor"),
        ("DCP-ALARM-MIB", "dcpAlarmGeneralActiveWarning"),
        ("DCP-ALARM-MIB", "dcpAlarmGeneralNumberActiveList"),
        ("DCP-ALARM-MIB", "dcpAlarmGeneralNumberLogList"),
        ("DCP-ALARM-MIB", "dcpAlarmGeneralLastTrapSeqNumber"))
)
if mibBuilder.loadTexts:
    dcpAlarmGeneralGroupV1.setStatus("current")

dcpAlarmActiveListGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 2, 4, 1, 3)
)
dcpAlarmActiveListGroupV1.setObjects(
      *(("DCP-ALARM-MIB", "dcpAlarmActiveListIndex"),
        ("DCP-ALARM-MIB", "dcpAlarmActiveListLocation"),
        ("DCP-ALARM-MIB", "dcpAlarmActiveListInterfaceName"),
        ("DCP-ALARM-MIB", "dcpAlarmActiveListText"),
        ("DCP-ALARM-MIB", "dcpAlarmActiveListSeverity"),
        ("DCP-ALARM-MIB", "dcpAlarmActiveListStartTime"),
        ("DCP-ALARM-MIB", "dcpAlarmActiveListSeqNumber"))
)
if mibBuilder.loadTexts:
    dcpAlarmActiveListGroupV1.setStatus("deprecated")

dcpAlarmLogListGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 2, 4, 1, 4)
)
dcpAlarmLogListGroupV1.setObjects(
      *(("DCP-ALARM-MIB", "dcpAlarmLogListIndex"),
        ("DCP-ALARM-MIB", "dcpAlarmLogListLocation"),
        ("DCP-ALARM-MIB", "dcpAlarmLogListInterfaceName"),
        ("DCP-ALARM-MIB", "dcpAlarmLogListText"),
        ("DCP-ALARM-MIB", "dcpAlarmLogListSeverity"),
        ("DCP-ALARM-MIB", "dcpAlarmLogListStartTime"),
        ("DCP-ALARM-MIB", "dcpAlarmLogListEndTime"),
        ("DCP-ALARM-MIB", "dcpAlarmLogListSeqNumber"))
)
if mibBuilder.loadTexts:
    dcpAlarmLogListGroupV1.setStatus("deprecated")

dcpAlarmLogListGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 2, 4, 1, 5)
)
dcpAlarmLogListGroupV2.setObjects(
      *(("DCP-ALARM-MIB", "dcpAlarmLogListIndex"),
        ("DCP-ALARM-MIB", "dcpAlarmLogListLocation"),
        ("DCP-ALARM-MIB", "dcpAlarmLogListInterfaceName"),
        ("DCP-ALARM-MIB", "dcpAlarmLogListInterfaceDescription"),
        ("DCP-ALARM-MIB", "dcpAlarmLogListText"),
        ("DCP-ALARM-MIB", "dcpAlarmLogListSeverity"),
        ("DCP-ALARM-MIB", "dcpAlarmLogListStartTime"),
        ("DCP-ALARM-MIB", "dcpAlarmLogListEndTime"),
        ("DCP-ALARM-MIB", "dcpAlarmLogListSeqNumber"),
        ("DCP-ALARM-MIB", "dcpAlarmLogListInterfaceDescription"))
)
if mibBuilder.loadTexts:
    dcpAlarmLogListGroupV2.setStatus("current")

dcpAlarmActiveListGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 2, 4, 1, 6)
)
dcpAlarmActiveListGroupV2.setObjects(
      *(("DCP-ALARM-MIB", "dcpAlarmActiveListIndex"),
        ("DCP-ALARM-MIB", "dcpAlarmActiveListLocation"),
        ("DCP-ALARM-MIB", "dcpAlarmActiveListInterfaceName"),
        ("DCP-ALARM-MIB", "dcpAlarmActiveListText"),
        ("DCP-ALARM-MIB", "dcpAlarmActiveListSeverity"),
        ("DCP-ALARM-MIB", "dcpAlarmActiveListStartTime"),
        ("DCP-ALARM-MIB", "dcpAlarmActiveListSeqNumber"),
        ("DCP-ALARM-MIB", "dcpAlarmActiveListInterfaceDescription"))
)
if mibBuilder.loadTexts:
    dcpAlarmActiveListGroupV2.setStatus("current")


# Notification objects

dcpAlarmNotificationCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 2, 3, 0, 1)
)
dcpAlarmNotificationCleared.setObjects(
      *(("DCP-ALARM-MIB", "dcpAlarmLogListIndex"),
        ("DCP-ALARM-MIB", "dcpAlarmLogListLocation"),
        ("DCP-ALARM-MIB", "dcpAlarmLogListInterfaceName"),
        ("DCP-ALARM-MIB", "dcpAlarmLogListText"),
        ("DCP-ALARM-MIB", "dcpAlarmLogListSeverity"),
        ("DCP-ALARM-MIB", "dcpAlarmLogListStartTime"),
        ("DCP-ALARM-MIB", "dcpAlarmLogListEndTime"),
        ("DCP-ALARM-MIB", "dcpAlarmLogListSeqNumber"),
        ("DCP-ALARM-MIB", "dcpAlarmLogListInterfaceDescription"))
)
if mibBuilder.loadTexts:
    dcpAlarmNotificationCleared.setStatus(
        "current"
    )

dcpAlarmNotificationCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 2, 3, 0, 2)
)
dcpAlarmNotificationCritical.setObjects(
      *(("DCP-ALARM-MIB", "dcpAlarmLogListIndex"),
        ("DCP-ALARM-MIB", "dcpAlarmLogListLocation"),
        ("DCP-ALARM-MIB", "dcpAlarmLogListInterfaceName"),
        ("DCP-ALARM-MIB", "dcpAlarmLogListText"),
        ("DCP-ALARM-MIB", "dcpAlarmLogListSeverity"),
        ("DCP-ALARM-MIB", "dcpAlarmLogListStartTime"),
        ("DCP-ALARM-MIB", "dcpAlarmLogListSeqNumber"),
        ("DCP-ALARM-MIB", "dcpAlarmLogListInterfaceDescription"))
)
if mibBuilder.loadTexts:
    dcpAlarmNotificationCritical.setStatus(
        "current"
    )

dcpAlarmNotificationMajor = NotificationType(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 2, 3, 0, 3)
)
dcpAlarmNotificationMajor.setObjects(
      *(("DCP-ALARM-MIB", "dcpAlarmLogListIndex"),
        ("DCP-ALARM-MIB", "dcpAlarmLogListLocation"),
        ("DCP-ALARM-MIB", "dcpAlarmLogListInterfaceName"),
        ("DCP-ALARM-MIB", "dcpAlarmLogListText"),
        ("DCP-ALARM-MIB", "dcpAlarmLogListSeverity"),
        ("DCP-ALARM-MIB", "dcpAlarmLogListStartTime"),
        ("DCP-ALARM-MIB", "dcpAlarmLogListSeqNumber"),
        ("DCP-ALARM-MIB", "dcpAlarmLogListInterfaceDescription"))
)
if mibBuilder.loadTexts:
    dcpAlarmNotificationMajor.setStatus(
        "current"
    )

dcpAlarmNotificationMinor = NotificationType(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 2, 3, 0, 4)
)
dcpAlarmNotificationMinor.setObjects(
      *(("DCP-ALARM-MIB", "dcpAlarmLogListIndex"),
        ("DCP-ALARM-MIB", "dcpAlarmLogListLocation"),
        ("DCP-ALARM-MIB", "dcpAlarmLogListInterfaceName"),
        ("DCP-ALARM-MIB", "dcpAlarmLogListText"),
        ("DCP-ALARM-MIB", "dcpAlarmLogListSeverity"),
        ("DCP-ALARM-MIB", "dcpAlarmLogListStartTime"),
        ("DCP-ALARM-MIB", "dcpAlarmLogListSeqNumber"),
        ("DCP-ALARM-MIB", "dcpAlarmLogListInterfaceDescription"))
)
if mibBuilder.loadTexts:
    dcpAlarmNotificationMinor.setStatus(
        "current"
    )

dcpAlarmNotificationWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 2, 3, 0, 5)
)
dcpAlarmNotificationWarning.setObjects(
      *(("DCP-ALARM-MIB", "dcpAlarmLogListIndex"),
        ("DCP-ALARM-MIB", "dcpAlarmLogListLocation"),
        ("DCP-ALARM-MIB", "dcpAlarmLogListInterfaceName"),
        ("DCP-ALARM-MIB", "dcpAlarmLogListText"),
        ("DCP-ALARM-MIB", "dcpAlarmLogListSeverity"),
        ("DCP-ALARM-MIB", "dcpAlarmLogListStartTime"),
        ("DCP-ALARM-MIB", "dcpAlarmLogListSeqNumber"),
        ("DCP-ALARM-MIB", "dcpAlarmLogListInterfaceDescription"))
)
if mibBuilder.loadTexts:
    dcpAlarmNotificationWarning.setStatus(
        "current"
    )


# Notifications groups

dcpAlarmNotificationGroupV1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 2, 4, 1, 2)
)
dcpAlarmNotificationGroupV1.setObjects(
      *(("DCP-ALARM-MIB", "dcpAlarmNotificationCleared"),
        ("DCP-ALARM-MIB", "dcpAlarmNotificationCritical"),
        ("DCP-ALARM-MIB", "dcpAlarmNotificationMajor"),
        ("DCP-ALARM-MIB", "dcpAlarmNotificationMinor"),
        ("DCP-ALARM-MIB", "dcpAlarmNotificationWarning"))
)
if mibBuilder.loadTexts:
    dcpAlarmNotificationGroupV1.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

dcpAlarmBasicComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 2, 4, 2, 1)
)
dcpAlarmBasicComplV1.setObjects(
      *(("DCP-ALARM-MIB", "dcpAlarmGeneralGroupV1"),
        ("DCP-ALARM-MIB", "dcpAlarmNotificationGroupV1"),
        ("DCP-ALARM-MIB", "dcpAlarmActiveListGroupV1"),
        ("DCP-ALARM-MIB", "dcpAlarmLogListGroupV1"))
)
if mibBuilder.loadTexts:
    dcpAlarmBasicComplV1.setStatus(
        "deprecated"
    )

dcpAlarmBasicComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 2, 4, 2, 2)
)
dcpAlarmBasicComplV2.setObjects(
      *(("DCP-ALARM-MIB", "dcpAlarmGeneralGroupV1"),
        ("DCP-ALARM-MIB", "dcpAlarmNotificationGroupV1"),
        ("DCP-ALARM-MIB", "dcpAlarmActiveListGroupV1"),
        ("DCP-ALARM-MIB", "dcpAlarmLogListGroupV2"))
)
if mibBuilder.loadTexts:
    dcpAlarmBasicComplV2.setStatus(
        "deprecated"
    )

dcpAlarmBasicComplV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 2, 4, 2, 3)
)
dcpAlarmBasicComplV3.setObjects(
      *(("DCP-ALARM-MIB", "dcpAlarmGeneralGroupV1"),
        ("DCP-ALARM-MIB", "dcpAlarmNotificationGroupV1"),
        ("DCP-ALARM-MIB", "dcpAlarmActiveListGroupV2"),
        ("DCP-ALARM-MIB", "dcpAlarmLogListGroupV2"))
)
if mibBuilder.loadTexts:
    dcpAlarmBasicComplV3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DCP-ALARM-MIB",
    **{"DcpAlarmIndex": DcpAlarmIndex,
       "dcpAlarm": dcpAlarm,
       "dcpAlarmGeneral": dcpAlarmGeneral,
       "dcpAlarmGeneralList": dcpAlarmGeneralList,
       "dcpAlarmGeneralHighestSeverity": dcpAlarmGeneralHighestSeverity,
       "dcpAlarmGeneralActiveCritical": dcpAlarmGeneralActiveCritical,
       "dcpAlarmGeneralActiveMajor": dcpAlarmGeneralActiveMajor,
       "dcpAlarmGeneralActiveMinor": dcpAlarmGeneralActiveMinor,
       "dcpAlarmGeneralActiveWarning": dcpAlarmGeneralActiveWarning,
       "dcpAlarmGeneralNumberActiveList": dcpAlarmGeneralNumberActiveList,
       "dcpAlarmGeneralNumberLogList": dcpAlarmGeneralNumberLogList,
       "dcpAlarmGeneralLastTrapSeqNumber": dcpAlarmGeneralLastTrapSeqNumber,
       "dcpAlarmObjects": dcpAlarmObjects,
       "dcpAlarmActiveListTable": dcpAlarmActiveListTable,
       "dcpAlarmActiveListEntry": dcpAlarmActiveListEntry,
       "dcpAlarmActiveListIndex": dcpAlarmActiveListIndex,
       "dcpAlarmActiveListLocation": dcpAlarmActiveListLocation,
       "dcpAlarmActiveListInterfaceName": dcpAlarmActiveListInterfaceName,
       "dcpAlarmActiveListText": dcpAlarmActiveListText,
       "dcpAlarmActiveListSeverity": dcpAlarmActiveListSeverity,
       "dcpAlarmActiveListStartTime": dcpAlarmActiveListStartTime,
       "dcpAlarmActiveListSeqNumber": dcpAlarmActiveListSeqNumber,
       "dcpAlarmActiveListInterfaceDescription": dcpAlarmActiveListInterfaceDescription,
       "dcpAlarmLogTable": dcpAlarmLogTable,
       "dcpAlarmLogEntry": dcpAlarmLogEntry,
       "dcpAlarmLogListIndex": dcpAlarmLogListIndex,
       "dcpAlarmLogListLocation": dcpAlarmLogListLocation,
       "dcpAlarmLogListInterfaceName": dcpAlarmLogListInterfaceName,
       "dcpAlarmLogListText": dcpAlarmLogListText,
       "dcpAlarmLogListSeverity": dcpAlarmLogListSeverity,
       "dcpAlarmLogListStartTime": dcpAlarmLogListStartTime,
       "dcpAlarmLogListEndTime": dcpAlarmLogListEndTime,
       "dcpAlarmLogListSeqNumber": dcpAlarmLogListSeqNumber,
       "dcpAlarmLogListInterfaceDescription": dcpAlarmLogListInterfaceDescription,
       "dcpAlarmMIBNotifications": dcpAlarmMIBNotifications,
       "dcpAlarmNotification": dcpAlarmNotification,
       "dcpAlarmNotificationCleared": dcpAlarmNotificationCleared,
       "dcpAlarmNotificationCritical": dcpAlarmNotificationCritical,
       "dcpAlarmNotificationMajor": dcpAlarmNotificationMajor,
       "dcpAlarmNotificationMinor": dcpAlarmNotificationMinor,
       "dcpAlarmNotificationWarning": dcpAlarmNotificationWarning,
       "dcpAlarmMIBCompliance": dcpAlarmMIBCompliance,
       "dcpAlarmMIBGroups": dcpAlarmMIBGroups,
       "dcpAlarmGeneralGroupV1": dcpAlarmGeneralGroupV1,
       "dcpAlarmNotificationGroupV1": dcpAlarmNotificationGroupV1,
       "dcpAlarmActiveListGroupV1": dcpAlarmActiveListGroupV1,
       "dcpAlarmLogListGroupV1": dcpAlarmLogListGroupV1,
       "dcpAlarmLogListGroupV2": dcpAlarmLogListGroupV2,
       "dcpAlarmActiveListGroupV2": dcpAlarmActiveListGroupV2,
       "dcpAlarmMIBCompliances": dcpAlarmMIBCompliances,
       "dcpAlarmBasicComplV1": dcpAlarmBasicComplV1,
       "dcpAlarmBasicComplV2": dcpAlarmBasicComplV2,
       "dcpAlarmBasicComplV3": dcpAlarmBasicComplV3}
)
