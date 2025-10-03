# SNMP MIB module (AV-SME-PLATFORM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\avaya\AV-SME-PLATFORM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:20:03 2025
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

(mibs,) = mibBuilder.importSymbols(
    "AVAYAGEN-MIB",
    "mibs")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

(sysDescr,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysDescr")

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

avSMEPlatformMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 48)
)
if mibBuilder.loadTexts:
    avSMEPlatformMIB.setRevisions(
        ("2013-01-11 14:05",
         "2010-07-06 13:47",
         "2010-07-02 14:37")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SmepGeneric_ObjectIdentity = ObjectIdentity
smepGeneric = _SmepGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 48, 1)
)
_SmepGenMibs_ObjectIdentity = ObjectIdentity
smepGenMibs = _SmepGenMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 1)
)
_SmepGenTraps_ObjectIdentity = ObjectIdentity
smepGenTraps = _SmepGenTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 2)
)
_SmepGTEvents_ObjectIdentity = ObjectIdentity
smepGTEvents = _SmepGTEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 2, 0)
)
_SmepGTObjects_ObjectIdentity = ObjectIdentity
smepGTObjects = _SmepGTObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 2, 1)
)
_SmepGTEventStdSeverity_Type = ItuPerceivedSeverity
_SmepGTEventStdSeverity_Object = MibScalar
smepGTEventStdSeverity = _SmepGTEventStdSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 2, 1, 1),
    _SmepGTEventStdSeverity_Type()
)
smepGTEventStdSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    smepGTEventStdSeverity.setStatus("current")
_SmepGTEventDateTime_Type = DateAndTime
_SmepGTEventDateTime_Object = MibScalar
smepGTEventDateTime = _SmepGTEventDateTime_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 2, 1, 2),
    _SmepGTEventDateTime_Type()
)
smepGTEventDateTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    smepGTEventDateTime.setStatus("current")


class _SmepGTEventDevID_Type(SnmpAdminString):
    """Custom type smepGTEventDevID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_SmepGTEventDevID_Type.__name__ = "SnmpAdminString"
_SmepGTEventDevID_Object = MibScalar
smepGTEventDevID = _SmepGTEventDevID_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 2, 1, 3),
    _SmepGTEventDevID_Type()
)
smepGTEventDevID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    smepGTEventDevID.setStatus("current")


class _SmepGTEventAppEntity_Type(Integer32):
    """Custom type smepGTEventAppEntity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("voiceMailPro", 1),
          ("onex", 2),
          ("ipOffice", 3),
          ("jade", 4),
          ("webmanagement", 5))
    )


_SmepGTEventAppEntity_Type.__name__ = "Integer32"
_SmepGTEventAppEntity_Object = MibScalar
smepGTEventAppEntity = _SmepGTEventAppEntity_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 2, 1, 4),
    _SmepGTEventAppEntity_Type()
)
smepGTEventAppEntity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    smepGTEventAppEntity.setStatus("current")


class _SmepGTEventAppEvent_Type(Integer32):
    """Custom type smepGTEventAppEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("crash", 1)
    )


_SmepGTEventAppEvent_Type.__name__ = "Integer32"
_SmepGTEventAppEvent_Object = MibScalar
smepGTEventAppEvent = _SmepGTEventAppEvent_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 2, 1, 5),
    _SmepGTEventAppEvent_Type()
)
smepGTEventAppEvent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    smepGTEventAppEvent.setStatus("current")
_SmepGenConformance_ObjectIdentity = ObjectIdentity
smepGenConformance = _SmepGenConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 3)
)
_SmepGenCompliances_ObjectIdentity = ObjectIdentity
smepGenCompliances = _SmepGenCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 3, 1)
)
_SmepGenGroups_ObjectIdentity = ObjectIdentity
smepGenGroups = _SmepGenGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 3, 2)
)

# Managed Objects groups

smepGenNotificationObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 3, 2, 1)
)
smepGenNotificationObjectsGroup.setObjects(
      *(("AV-SME-PLATFORM-MIB", "smepGTEventStdSeverity"),
        ("AV-SME-PLATFORM-MIB", "smepGTEventDevID"),
        ("AV-SME-PLATFORM-MIB", "smepGTEventDateTime"),
        ("AV-SME-PLATFORM-MIB", "smepGTEventAppEntity"),
        ("AV-SME-PLATFORM-MIB", "smepGTEventAppEvent"))
)
if mibBuilder.loadTexts:
    smepGenNotificationObjectsGroup.setStatus("current")


# Notification objects

smepGenColdStartEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 2, 0, 1)
)
smepGenColdStartEvent.setObjects(
      *(("AV-SME-PLATFORM-MIB", "smepGTEventStdSeverity"),
        ("AV-SME-PLATFORM-MIB", "smepGTEventDateTime"),
        ("AV-SME-PLATFORM-MIB", "smepGTEventDevID"),
        ("SNMPv2-MIB", "sysDescr"))
)
if mibBuilder.loadTexts:
    smepGenColdStartEvent.setStatus(
        "current"
    )

smepGenWarmStartEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 2, 0, 2)
)
smepGenWarmStartEvent.setObjects(
      *(("AV-SME-PLATFORM-MIB", "smepGTEventStdSeverity"),
        ("AV-SME-PLATFORM-MIB", "smepGTEventDateTime"),
        ("AV-SME-PLATFORM-MIB", "smepGTEventDevID"),
        ("SNMPv2-MIB", "sysDescr"))
)
if mibBuilder.loadTexts:
    smepGenWarmStartEvent.setStatus(
        "current"
    )

smepGenLinkDownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 2, 0, 3)
)
smepGenLinkDownEvent.setObjects(
      *(("AV-SME-PLATFORM-MIB", "smepGTEventStdSeverity"),
        ("AV-SME-PLATFORM-MIB", "smepGTEventDateTime"),
        ("AV-SME-PLATFORM-MIB", "smepGTEventDevID"),
        ("SNMPv2-MIB", "sysDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    smepGenLinkDownEvent.setStatus(
        "current"
    )

smepGenLinkUpEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 2, 0, 4)
)
smepGenLinkUpEvent.setObjects(
      *(("AV-SME-PLATFORM-MIB", "smepGTEventStdSeverity"),
        ("AV-SME-PLATFORM-MIB", "smepGTEventDateTime"),
        ("AV-SME-PLATFORM-MIB", "smepGTEventDevID"),
        ("SNMPv2-MIB", "sysDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    smepGenLinkUpEvent.setStatus(
        "current"
    )

smepGenAuthFailureEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 2, 0, 5)
)
smepGenAuthFailureEvent.setObjects(
      *(("AV-SME-PLATFORM-MIB", "smepGTEventStdSeverity"),
        ("AV-SME-PLATFORM-MIB", "smepGTEventDateTime"),
        ("AV-SME-PLATFORM-MIB", "smepGTEventDevID"),
        ("SNMPv2-MIB", "sysDescr"))
)
if mibBuilder.loadTexts:
    smepGenAuthFailureEvent.setStatus(
        "current"
    )

smepGenAppEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 2, 0, 6)
)
smepGenAppEvent.setObjects(
      *(("AV-SME-PLATFORM-MIB", "smepGTEventStdSeverity"),
        ("AV-SME-PLATFORM-MIB", "smepGTEventDateTime"),
        ("AV-SME-PLATFORM-MIB", "smepGTEventDevID"),
        ("SNMPv2-MIB", "sysDescr"),
        ("AV-SME-PLATFORM-MIB", "smepGTEventAppEntity"),
        ("AV-SME-PLATFORM-MIB", "smepGTEventAppEvent"))
)
if mibBuilder.loadTexts:
    smepGenAppEvent.setStatus(
        "current"
    )


# Notifications groups

smepGenEntGenNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 3, 2, 2)
)
smepGenEntGenNotificationsGroup.setObjects(
      *(("AV-SME-PLATFORM-MIB", "smepGenColdStartEvent"),
        ("AV-SME-PLATFORM-MIB", "smepGenWarmStartEvent"),
        ("AV-SME-PLATFORM-MIB", "smepGenLinkDownEvent"),
        ("AV-SME-PLATFORM-MIB", "smepGenLinkUpEvent"),
        ("AV-SME-PLATFORM-MIB", "smepGenAuthFailureEvent"))
)
if mibBuilder.loadTexts:
    smepGenEntGenNotificationsGroup.setStatus(
        "current"
    )

smepGenAppNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 3, 2, 3)
)
smepGenAppNotificationsGroup.setObjects(
    ("AV-SME-PLATFORM-MIB", "smepGenAppEvent")
)
if mibBuilder.loadTexts:
    smepGenAppNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

smepGenCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 3, 1, 1)
)
smepGenCompliance.setObjects(
      *(("AV-SME-PLATFORM-MIB", "smepGenNotificationObjectsGroup"),
        ("AV-SME-PLATFORM-MIB", "smepGenEntGenNotificationsGroup"),
        ("AV-SME-PLATFORM-MIB", "smepGenAppNotificationsGroup"))
)
if mibBuilder.loadTexts:
    smepGenCompliance.setStatus(
        "deprecated"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AV-SME-PLATFORM-MIB",
    **{"avSMEPlatformMIB": avSMEPlatformMIB,
       "smepGeneric": smepGeneric,
       "smepGenMibs": smepGenMibs,
       "smepGenTraps": smepGenTraps,
       "smepGTEvents": smepGTEvents,
       "smepGenColdStartEvent": smepGenColdStartEvent,
       "smepGenWarmStartEvent": smepGenWarmStartEvent,
       "smepGenLinkDownEvent": smepGenLinkDownEvent,
       "smepGenLinkUpEvent": smepGenLinkUpEvent,
       "smepGenAuthFailureEvent": smepGenAuthFailureEvent,
       "smepGenAppEvent": smepGenAppEvent,
       "smepGTObjects": smepGTObjects,
       "smepGTEventStdSeverity": smepGTEventStdSeverity,
       "smepGTEventDateTime": smepGTEventDateTime,
       "smepGTEventDevID": smepGTEventDevID,
       "smepGTEventAppEntity": smepGTEventAppEntity,
       "smepGTEventAppEvent": smepGTEventAppEvent,
       "smepGenConformance": smepGenConformance,
       "smepGenCompliances": smepGenCompliances,
       "smepGenCompliance": smepGenCompliance,
       "smepGenGroups": smepGenGroups,
       "smepGenNotificationObjectsGroup": smepGenNotificationObjectsGroup,
       "smepGenEntGenNotificationsGroup": smepGenEntGenNotificationsGroup,
       "smepGenAppNotificationsGroup": smepGenAppNotificationsGroup}
)
