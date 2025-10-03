# SNMP MIB module (SILVERPEAK-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\silverpeak\SILVERPEAK-MGMT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:28:08 2025
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

(silverpeakMgmt,
 silverpeakNotifications) = mibBuilder.importSymbols(
    "SILVERPEAK-SMI",
    "silverpeakMgmt",
    "silverpeakNotifications")

(SilverpeakAlarmSeverity,
 SilverpeakSeqNum,
 SilverpeakYesNo) = mibBuilder.importSymbols(
    "SILVERPEAK-TC",
    "SilverpeakAlarmSeverity",
    "SilverpeakSeqNum",
    "SilverpeakYesNo")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

silverpeakMgmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 3, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SilverpeakMgmtMIBObjects_ObjectIdentity = ObjectIdentity
silverpeakMgmtMIBObjects = _SilverpeakMgmtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 3, 1, 1)
)
_SilverpeakMgmtMIBScalars_ObjectIdentity = ObjectIdentity
silverpeakMgmtMIBScalars = _SilverpeakMgmtMIBScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 1)
)
_SpsSystemVersion_Type = DisplayString
_SpsSystemVersion_Object = MibScalar
spsSystemVersion = _SpsSystemVersion_Object(
    (1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 1, 1),
    _SpsSystemVersion_Type()
)
spsSystemVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spsSystemVersion.setStatus("current")
_SpsProductModel_Type = DisplayString
_SpsProductModel_Object = MibScalar
spsProductModel = _SpsProductModel_Object(
    (1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 1, 2),
    _SpsProductModel_Type()
)
spsProductModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spsProductModel.setStatus("current")
_SpsOperStatus_Type = DisplayString
_SpsOperStatus_Object = MibScalar
spsOperStatus = _SpsOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 1, 3),
    _SpsOperStatus_Type()
)
spsOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spsOperStatus.setStatus("current")


class _SpsActiveAlarmCount_Type(Integer32):
    """Custom type spsActiveAlarmCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SpsActiveAlarmCount_Type.__name__ = "Integer32"
_SpsActiveAlarmCount_Object = MibScalar
spsActiveAlarmCount = _SpsActiveAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 1, 4),
    _SpsActiveAlarmCount_Type()
)
spsActiveAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spsActiveAlarmCount.setStatus("current")
_SpsSystemUptime_Type = TimeTicks
_SpsSystemUptime_Object = MibScalar
spsSystemUptime = _SpsSystemUptime_Object(
    (1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 1, 5),
    _SpsSystemUptime_Type()
)
spsSystemUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spsSystemUptime.setStatus("current")
_SpsSystemSerial_Type = DisplayString
_SpsSystemSerial_Object = MibScalar
spsSystemSerial = _SpsSystemSerial_Object(
    (1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 1, 6),
    _SpsSystemSerial_Type()
)
spsSystemSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spsSystemSerial.setStatus("current")
_SilverpeakMgmtMIBTables_ObjectIdentity = ObjectIdentity
silverpeakMgmtMIBTables = _SilverpeakMgmtMIBTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 2)
)
_SpsActiveAlarmTable_Object = MibTable
spsActiveAlarmTable = _SpsActiveAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    spsActiveAlarmTable.setStatus("current")
_ActiveAlarmEntry_Object = MibTableRow
activeAlarmEntry = _ActiveAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 2, 1, 1)
)
activeAlarmEntry.setIndexNames(
    (0, "SILVERPEAK-MGMT-MIB", "spsActiveAlarmIndex"),
)
if mibBuilder.loadTexts:
    activeAlarmEntry.setStatus("current")


class _SpsActiveAlarmIndex_Type(Integer32):
    """Custom type spsActiveAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SpsActiveAlarmIndex_Type.__name__ = "Integer32"
_SpsActiveAlarmIndex_Object = MibTableColumn
spsActiveAlarmIndex = _SpsActiveAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 2, 1, 1, 1),
    _SpsActiveAlarmIndex_Type()
)
spsActiveAlarmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    spsActiveAlarmIndex.setStatus("current")
_SpsActiveAlarmSeqNum_Type = SilverpeakSeqNum
_SpsActiveAlarmSeqNum_Object = MibTableColumn
spsActiveAlarmSeqNum = _SpsActiveAlarmSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 2, 1, 1, 2),
    _SpsActiveAlarmSeqNum_Type()
)
spsActiveAlarmSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spsActiveAlarmSeqNum.setStatus("current")
_SpsActiveAlarmSeverity_Type = SilverpeakAlarmSeverity
_SpsActiveAlarmSeverity_Object = MibTableColumn
spsActiveAlarmSeverity = _SpsActiveAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 2, 1, 1, 3),
    _SpsActiveAlarmSeverity_Type()
)
spsActiveAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spsActiveAlarmSeverity.setStatus("current")


class _SpsActiveAlarmName_Type(DisplayString):
    """Custom type spsActiveAlarmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SpsActiveAlarmName_Type.__name__ = "DisplayString"
_SpsActiveAlarmName_Object = MibTableColumn
spsActiveAlarmName = _SpsActiveAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 2, 1, 1, 4),
    _SpsActiveAlarmName_Type()
)
spsActiveAlarmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spsActiveAlarmName.setStatus("current")


class _SpsActiveAlarmDescr_Type(DisplayString):
    """Custom type spsActiveAlarmDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SpsActiveAlarmDescr_Type.__name__ = "DisplayString"
_SpsActiveAlarmDescr_Object = MibTableColumn
spsActiveAlarmDescr = _SpsActiveAlarmDescr_Object(
    (1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 2, 1, 1, 5),
    _SpsActiveAlarmDescr_Type()
)
spsActiveAlarmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spsActiveAlarmDescr.setStatus("current")


class _SpsActiveAlarmSource_Type(DisplayString):
    """Custom type spsActiveAlarmSource based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SpsActiveAlarmSource_Type.__name__ = "DisplayString"
_SpsActiveAlarmSource_Object = MibTableColumn
spsActiveAlarmSource = _SpsActiveAlarmSource_Object(
    (1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 2, 1, 1, 6),
    _SpsActiveAlarmSource_Type()
)
spsActiveAlarmSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spsActiveAlarmSource.setStatus("current")


class _SpsActiveAlarmType_Type(DisplayString):
    """Custom type spsActiveAlarmType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SpsActiveAlarmType_Type.__name__ = "DisplayString"
_SpsActiveAlarmType_Object = MibTableColumn
spsActiveAlarmType = _SpsActiveAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 2, 1, 1, 7),
    _SpsActiveAlarmType_Type()
)
spsActiveAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spsActiveAlarmType.setStatus("current")
_SpsActiveAlarmAcked_Type = SilverpeakYesNo
_SpsActiveAlarmAcked_Object = MibTableColumn
spsActiveAlarmAcked = _SpsActiveAlarmAcked_Object(
    (1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 2, 1, 1, 8),
    _SpsActiveAlarmAcked_Type()
)
spsActiveAlarmAcked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spsActiveAlarmAcked.setStatus("current")
_SpsActiveAlarmActive_Type = SilverpeakYesNo
_SpsActiveAlarmActive_Object = MibTableColumn
spsActiveAlarmActive = _SpsActiveAlarmActive_Object(
    (1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 2, 1, 1, 9),
    _SpsActiveAlarmActive_Type()
)
spsActiveAlarmActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spsActiveAlarmActive.setStatus("current")
_SpsActiveAlarmClearable_Type = SilverpeakYesNo
_SpsActiveAlarmClearable_Object = MibTableColumn
spsActiveAlarmClearable = _SpsActiveAlarmClearable_Object(
    (1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 2, 1, 1, 10),
    _SpsActiveAlarmClearable_Type()
)
spsActiveAlarmClearable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spsActiveAlarmClearable.setStatus("current")


class _SpsActiveAlarmLogTime_Type(OctetString):
    """Custom type spsActiveAlarmLogTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SpsActiveAlarmLogTime_Type.__name__ = "OctetString"
_SpsActiveAlarmLogTime_Object = MibTableColumn
spsActiveAlarmLogTime = _SpsActiveAlarmLogTime_Object(
    (1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 2, 1, 1, 11),
    _SpsActiveAlarmLogTime_Type()
)
spsActiveAlarmLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spsActiveAlarmLogTime.setStatus("current")
_SpsActiveAlarmServiceAffect_Type = SilverpeakYesNo
_SpsActiveAlarmServiceAffect_Object = MibTableColumn
spsActiveAlarmServiceAffect = _SpsActiveAlarmServiceAffect_Object(
    (1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 2, 1, 1, 12),
    _SpsActiveAlarmServiceAffect_Type()
)
spsActiveAlarmServiceAffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spsActiveAlarmServiceAffect.setStatus("current")
_SpsActiveAlarmTypeId_Type = Integer32
_SpsActiveAlarmTypeId_Object = MibTableColumn
spsActiveAlarmTypeId = _SpsActiveAlarmTypeId_Object(
    (1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 2, 1, 1, 13),
    _SpsActiveAlarmTypeId_Type()
)
spsActiveAlarmTypeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spsActiveAlarmTypeId.setStatus("current")
_SilverpeakMgmtMIBConformance_ObjectIdentity = ObjectIdentity
silverpeakMgmtMIBConformance = _SilverpeakMgmtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 3, 1, 2)
)
_SilverpeakMgmtMIBCompliances_ObjectIdentity = ObjectIdentity
silverpeakMgmtMIBCompliances = _SilverpeakMgmtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 3, 1, 2, 1)
)
_SilverpeakMgmtMIBGroups_ObjectIdentity = ObjectIdentity
silverpeakMgmtMIBGroups = _SilverpeakMgmtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 3, 1, 2, 2)
)
_SilverpeakMgmtMIBNotifications_ObjectIdentity = ObjectIdentity
silverpeakMgmtMIBNotifications = _SilverpeakMgmtMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 4, 1)
)

# Managed Objects groups

silverpeakMgmtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 23867, 3, 1, 2, 2, 1)
)
silverpeakMgmtGroup.setObjects(
      *(("SILVERPEAK-MGMT-MIB", "spsSystemVersion"),
        ("SILVERPEAK-MGMT-MIB", "spsProductModel"),
        ("SILVERPEAK-MGMT-MIB", "spsOperStatus"),
        ("SILVERPEAK-MGMT-MIB", "spsActiveAlarmSeqNum"),
        ("SILVERPEAK-MGMT-MIB", "spsActiveAlarmSeverity"),
        ("SILVERPEAK-MGMT-MIB", "spsActiveAlarmName"),
        ("SILVERPEAK-MGMT-MIB", "spsActiveAlarmDescr"),
        ("SILVERPEAK-MGMT-MIB", "spsActiveAlarmSource"),
        ("SILVERPEAK-MGMT-MIB", "spsActiveAlarmType"),
        ("SILVERPEAK-MGMT-MIB", "spsActiveAlarmAcked"),
        ("SILVERPEAK-MGMT-MIB", "spsActiveAlarmActive"),
        ("SILVERPEAK-MGMT-MIB", "spsActiveAlarmClearable"),
        ("SILVERPEAK-MGMT-MIB", "spsActiveAlarmLogTime"),
        ("SILVERPEAK-MGMT-MIB", "spsActiveAlarmServiceAffect"))
)
if mibBuilder.loadTexts:
    silverpeakMgmtGroup.setStatus("current")


# Notification objects

spsNotifyAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 23867, 4, 1, 1)
)
spsNotifyAlarm.setObjects(
      *(("SILVERPEAK-MGMT-MIB", "spsActiveAlarmSource"),
        ("SILVERPEAK-MGMT-MIB", "spsActiveAlarmSeverity"),
        ("SILVERPEAK-MGMT-MIB", "spsActiveAlarmDescr"))
)
if mibBuilder.loadTexts:
    spsNotifyAlarm.setStatus(
        "current"
    )


# Notifications groups

silverpeakMgmtNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 23867, 3, 1, 2, 2, 3)
)
silverpeakMgmtNotifyGroup.setObjects(
    ("SILVERPEAK-MGMT-MIB", "spsNotifyAlarm")
)
if mibBuilder.loadTexts:
    silverpeakMgmtNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

silverpeakMgmtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 23867, 3, 1, 2, 1, 1)
)
silverpeakMgmtCompliance.setObjects(
      *(("SILVERPEAK-MGMT-MIB", "silverpeakMgmtGroup"),
        ("SILVERPEAK-MGMT-MIB", "silverpeakMgmtNotifyGroup"))
)
if mibBuilder.loadTexts:
    silverpeakMgmtCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SILVERPEAK-MGMT-MIB",
    **{"silverpeakMgmtMIB": silverpeakMgmtMIB,
       "silverpeakMgmtMIBObjects": silverpeakMgmtMIBObjects,
       "silverpeakMgmtMIBScalars": silverpeakMgmtMIBScalars,
       "spsSystemVersion": spsSystemVersion,
       "spsProductModel": spsProductModel,
       "spsOperStatus": spsOperStatus,
       "spsActiveAlarmCount": spsActiveAlarmCount,
       "spsSystemUptime": spsSystemUptime,
       "spsSystemSerial": spsSystemSerial,
       "silverpeakMgmtMIBTables": silverpeakMgmtMIBTables,
       "spsActiveAlarmTable": spsActiveAlarmTable,
       "activeAlarmEntry": activeAlarmEntry,
       "spsActiveAlarmIndex": spsActiveAlarmIndex,
       "spsActiveAlarmSeqNum": spsActiveAlarmSeqNum,
       "spsActiveAlarmSeverity": spsActiveAlarmSeverity,
       "spsActiveAlarmName": spsActiveAlarmName,
       "spsActiveAlarmDescr": spsActiveAlarmDescr,
       "spsActiveAlarmSource": spsActiveAlarmSource,
       "spsActiveAlarmType": spsActiveAlarmType,
       "spsActiveAlarmAcked": spsActiveAlarmAcked,
       "spsActiveAlarmActive": spsActiveAlarmActive,
       "spsActiveAlarmClearable": spsActiveAlarmClearable,
       "spsActiveAlarmLogTime": spsActiveAlarmLogTime,
       "spsActiveAlarmServiceAffect": spsActiveAlarmServiceAffect,
       "spsActiveAlarmTypeId": spsActiveAlarmTypeId,
       "silverpeakMgmtMIBConformance": silverpeakMgmtMIBConformance,
       "silverpeakMgmtMIBCompliances": silverpeakMgmtMIBCompliances,
       "silverpeakMgmtCompliance": silverpeakMgmtCompliance,
       "silverpeakMgmtMIBGroups": silverpeakMgmtMIBGroups,
       "silverpeakMgmtGroup": silverpeakMgmtGroup,
       "silverpeakMgmtNotifyGroup": silverpeakMgmtNotifyGroup,
       "silverpeakMgmtMIBNotifications": silverpeakMgmtMIBNotifications,
       "spsNotifyAlarm": spsNotifyAlarm}
)
