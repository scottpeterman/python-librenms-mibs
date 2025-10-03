# SNMP MIB module (ERICSSON-ROUTER-SFP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ericsson\ERICSSON-ROUTER-SFP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:42:31 2025
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

(EriRouterAlarmId,
 EriRouterAlarmServiceAffecting) = mibBuilder.importSymbols(
    "ERICSSON-ROUTER-ALARM-TC",
    "EriRouterAlarmId",
    "EriRouterAlarmServiceAffecting")

(eriRouterMgmt,) = mibBuilder.importSymbols(
    "ERICSSON-ROUTER-SMI",
    "eriRouterMgmt")

(EriRouterPort,
 EriRouterSlot) = mibBuilder.importSymbols(
    "ERICSSON-ROUTER-TC",
    "EriRouterPort",
    "EriRouterSlot")

(IANAItuEventType,
 IANAItuProbableCause) = mibBuilder.importSymbols(
    "IANA-ITU-ALARM-TC-MIB",
    "IANAItuEventType",
    "IANAItuProbableCause")

(ItuPerceivedSeverity,) = mibBuilder.importSymbols(
    "ITU-ALARM-TC-MIB",
    "ItuPerceivedSeverity")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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


# MODULE-IDENTITY

eriRouterSfpMonMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 49)
)
if mibBuilder.loadTexts:
    eriRouterSfpMonMIB.setRevisions(
        ("2015-01-14 18:00",
         "2010-03-02 00:00",
         "2008-08-20 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EriRouterSfpMonMIBNotifications_ObjectIdentity = ObjectIdentity
eriRouterSfpMonMIBNotifications = _EriRouterSfpMonMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 49, 0)
)
_EriRouterSfpMonMIBObjects_ObjectIdentity = ObjectIdentity
eriRouterSfpMonMIBObjects = _EriRouterSfpMonMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 49, 1)
)
_EriRouterSfpAlarmActiveTable_Object = MibTable
eriRouterSfpAlarmActiveTable = _EriRouterSfpAlarmActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 49, 1, 1)
)
if mibBuilder.loadTexts:
    eriRouterSfpAlarmActiveTable.setStatus("current")
_EriRouterSfpAlarmActiveEntry_Object = MibTableRow
eriRouterSfpAlarmActiveEntry = _EriRouterSfpAlarmActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 49, 1, 1, 1)
)
eriRouterSfpAlarmActiveEntry.setIndexNames(
    (0, "ERICSSON-ROUTER-SFP-MIB", "eriRouterSfpActiveAlarmIndex"),
)
if mibBuilder.loadTexts:
    eriRouterSfpAlarmActiveEntry.setStatus("current")


class _EriRouterSfpActiveAlarmIndex_Type(Unsigned32):
    """Custom type eriRouterSfpActiveAlarmIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_EriRouterSfpActiveAlarmIndex_Type.__name__ = "Unsigned32"
_EriRouterSfpActiveAlarmIndex_Object = MibTableColumn
eriRouterSfpActiveAlarmIndex = _EriRouterSfpActiveAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 49, 1, 1, 1, 1),
    _EriRouterSfpActiveAlarmIndex_Type()
)
eriRouterSfpActiveAlarmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eriRouterSfpActiveAlarmIndex.setStatus("current")
_EriRouterSfpAlarmCardSlot_Type = EriRouterSlot
_EriRouterSfpAlarmCardSlot_Object = MibTableColumn
eriRouterSfpAlarmCardSlot = _EriRouterSfpAlarmCardSlot_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 49, 1, 1, 1, 2),
    _EriRouterSfpAlarmCardSlot_Type()
)
eriRouterSfpAlarmCardSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterSfpAlarmCardSlot.setStatus("current")
_EriRouterSfpAlarmPort_Type = EriRouterPort
_EriRouterSfpAlarmPort_Object = MibTableColumn
eriRouterSfpAlarmPort = _EriRouterSfpAlarmPort_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 49, 1, 1, 1, 3),
    _EriRouterSfpAlarmPort_Type()
)
eriRouterSfpAlarmPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterSfpAlarmPort.setStatus("current")
_EriRouterSfpAlarmId_Type = EriRouterAlarmId
_EriRouterSfpAlarmId_Object = MibTableColumn
eriRouterSfpAlarmId = _EriRouterSfpAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 49, 1, 1, 1, 4),
    _EriRouterSfpAlarmId_Type()
)
eriRouterSfpAlarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterSfpAlarmId.setStatus("current")
_EriRouterSfpAlarmSeverity_Type = ItuPerceivedSeverity
_EriRouterSfpAlarmSeverity_Object = MibTableColumn
eriRouterSfpAlarmSeverity = _EriRouterSfpAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 49, 1, 1, 1, 5),
    _EriRouterSfpAlarmSeverity_Type()
)
eriRouterSfpAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterSfpAlarmSeverity.setStatus("current")
_EriRouterSfpAlarmType_Type = IANAItuEventType
_EriRouterSfpAlarmType_Object = MibTableColumn
eriRouterSfpAlarmType = _EriRouterSfpAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 49, 1, 1, 1, 6),
    _EriRouterSfpAlarmType_Type()
)
eriRouterSfpAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterSfpAlarmType.setStatus("current")
_EriRouterSfpAlarmDateAndTime_Type = DateAndTime
_EriRouterSfpAlarmDateAndTime_Object = MibTableColumn
eriRouterSfpAlarmDateAndTime = _EriRouterSfpAlarmDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 49, 1, 1, 1, 7),
    _EriRouterSfpAlarmDateAndTime_Type()
)
eriRouterSfpAlarmDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterSfpAlarmDateAndTime.setStatus("current")


class _EriRouterSfpAlarmDescription_Type(SnmpAdminString):
    """Custom type eriRouterSfpAlarmDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EriRouterSfpAlarmDescription_Type.__name__ = "SnmpAdminString"
_EriRouterSfpAlarmDescription_Object = MibTableColumn
eriRouterSfpAlarmDescription = _EriRouterSfpAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 49, 1, 1, 1, 8),
    _EriRouterSfpAlarmDescription_Type()
)
eriRouterSfpAlarmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterSfpAlarmDescription.setStatus("current")
_EriRouterSfpAlarmProbableCause_Type = IANAItuProbableCause
_EriRouterSfpAlarmProbableCause_Object = MibTableColumn
eriRouterSfpAlarmProbableCause = _EriRouterSfpAlarmProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 49, 1, 1, 1, 9),
    _EriRouterSfpAlarmProbableCause_Type()
)
eriRouterSfpAlarmProbableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterSfpAlarmProbableCause.setStatus("current")
_EriRouterSfpAlarmServiceAffecting_Type = EriRouterAlarmServiceAffecting
_EriRouterSfpAlarmServiceAffecting_Object = MibTableColumn
eriRouterSfpAlarmServiceAffecting = _EriRouterSfpAlarmServiceAffecting_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 49, 1, 1, 1, 10),
    _EriRouterSfpAlarmServiceAffecting_Type()
)
eriRouterSfpAlarmServiceAffecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterSfpAlarmServiceAffecting.setStatus("current")
_EriRouterSfpMonMIBConformance_ObjectIdentity = ObjectIdentity
eriRouterSfpMonMIBConformance = _EriRouterSfpMonMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 49, 2)
)
_EriRouterSfpMonMIBGroups_ObjectIdentity = ObjectIdentity
eriRouterSfpMonMIBGroups = _EriRouterSfpMonMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 49, 2, 1)
)
_EriRouterSfpMonMIBCompliances_ObjectIdentity = ObjectIdentity
eriRouterSfpMonMIBCompliances = _EriRouterSfpMonMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 49, 2, 2)
)

# Managed Objects groups

eriRouterSfpMonMIBObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 49, 2, 1, 1)
)
eriRouterSfpMonMIBObjectGroup.setObjects(
      *(("ERICSSON-ROUTER-SFP-MIB", "eriRouterSfpAlarmCardSlot"),
        ("ERICSSON-ROUTER-SFP-MIB", "eriRouterSfpAlarmPort"),
        ("ERICSSON-ROUTER-SFP-MIB", "eriRouterSfpAlarmId"),
        ("ERICSSON-ROUTER-SFP-MIB", "eriRouterSfpAlarmType"),
        ("ERICSSON-ROUTER-SFP-MIB", "eriRouterSfpAlarmDateAndTime"),
        ("ERICSSON-ROUTER-SFP-MIB", "eriRouterSfpAlarmDescription"),
        ("ERICSSON-ROUTER-SFP-MIB", "eriRouterSfpAlarmProbableCause"),
        ("ERICSSON-ROUTER-SFP-MIB", "eriRouterSfpAlarmSeverity"),
        ("ERICSSON-ROUTER-SFP-MIB", "eriRouterSfpAlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    eriRouterSfpMonMIBObjectGroup.setStatus("current")


# Notification objects

eriRouterSfpAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 49, 0, 1)
)
eriRouterSfpAlarm.setObjects(
      *(("ERICSSON-ROUTER-SFP-MIB", "eriRouterSfpAlarmCardSlot"),
        ("ERICSSON-ROUTER-SFP-MIB", "eriRouterSfpAlarmPort"),
        ("ERICSSON-ROUTER-SFP-MIB", "eriRouterSfpAlarmId"),
        ("ERICSSON-ROUTER-SFP-MIB", "eriRouterSfpAlarmSeverity"),
        ("ERICSSON-ROUTER-SFP-MIB", "eriRouterSfpAlarmType"),
        ("ERICSSON-ROUTER-SFP-MIB", "eriRouterSfpAlarmDateAndTime"),
        ("ERICSSON-ROUTER-SFP-MIB", "eriRouterSfpAlarmDescription"),
        ("ERICSSON-ROUTER-SFP-MIB", "eriRouterSfpAlarmProbableCause"))
)
if mibBuilder.loadTexts:
    eriRouterSfpAlarm.setStatus(
        "current"
    )


# Notifications groups

eriRouterSfpMonMIBNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 49, 2, 1, 2)
)
eriRouterSfpMonMIBNotificationGroup.setObjects(
    ("ERICSSON-ROUTER-SFP-MIB", "eriRouterSfpAlarm")
)
if mibBuilder.loadTexts:
    eriRouterSfpMonMIBNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

eriRouterSfpMonMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 49, 2, 2, 1)
)
eriRouterSfpMonMIBCompliance.setObjects(
      *(("ERICSSON-ROUTER-SFP-MIB", "eriRouterSfpMonMIBObjectGroup"),
        ("ERICSSON-ROUTER-SFP-MIB", "eriRouterSfpMonMIBNotificationGroup"))
)
if mibBuilder.loadTexts:
    eriRouterSfpMonMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ERICSSON-ROUTER-SFP-MIB",
    **{"eriRouterSfpMonMIB": eriRouterSfpMonMIB,
       "eriRouterSfpMonMIBNotifications": eriRouterSfpMonMIBNotifications,
       "eriRouterSfpAlarm": eriRouterSfpAlarm,
       "eriRouterSfpMonMIBObjects": eriRouterSfpMonMIBObjects,
       "eriRouterSfpAlarmActiveTable": eriRouterSfpAlarmActiveTable,
       "eriRouterSfpAlarmActiveEntry": eriRouterSfpAlarmActiveEntry,
       "eriRouterSfpActiveAlarmIndex": eriRouterSfpActiveAlarmIndex,
       "eriRouterSfpAlarmCardSlot": eriRouterSfpAlarmCardSlot,
       "eriRouterSfpAlarmPort": eriRouterSfpAlarmPort,
       "eriRouterSfpAlarmId": eriRouterSfpAlarmId,
       "eriRouterSfpAlarmSeverity": eriRouterSfpAlarmSeverity,
       "eriRouterSfpAlarmType": eriRouterSfpAlarmType,
       "eriRouterSfpAlarmDateAndTime": eriRouterSfpAlarmDateAndTime,
       "eriRouterSfpAlarmDescription": eriRouterSfpAlarmDescription,
       "eriRouterSfpAlarmProbableCause": eriRouterSfpAlarmProbableCause,
       "eriRouterSfpAlarmServiceAffecting": eriRouterSfpAlarmServiceAffecting,
       "eriRouterSfpMonMIBConformance": eriRouterSfpMonMIBConformance,
       "eriRouterSfpMonMIBGroups": eriRouterSfpMonMIBGroups,
       "eriRouterSfpMonMIBObjectGroup": eriRouterSfpMonMIBObjectGroup,
       "eriRouterSfpMonMIBNotificationGroup": eriRouterSfpMonMIBNotificationGroup,
       "eriRouterSfpMonMIBCompliances": eriRouterSfpMonMIBCompliances,
       "eriRouterSfpMonMIBCompliance": eriRouterSfpMonMIBCompliance}
)
