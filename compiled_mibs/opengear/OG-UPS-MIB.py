# SNMP MIB module (OG-UPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\opengear\OG-UPS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:19:32 2025
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

(ogMgmt,) = mibBuilder.importSymbols(
    "OG-SMI-MIB",
    "ogMgmt")

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

ogNetUpsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 16)
)
if mibBuilder.loadTexts:
    ogNetUpsMib.setRevisions(
        ("2013-08-11 00:00",
         "2010-03-22 11:27",
         "2008-06-13 11:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OgNetUpsMibNotificationPrefix_ObjectIdentity = ObjectIdentity
ogNetUpsMibNotificationPrefix = _OgNetUpsMibNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 16, 2)
)
_OgnupsMibNotifications_ObjectIdentity = ObjectIdentity
ognupsMibNotifications = _OgnupsMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 16, 2, 0)
)
_OgNetUpsMibConformance_ObjectIdentity = ObjectIdentity
ogNetUpsMibConformance = _OgNetUpsMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 16, 3)
)
_OgNetUpsMibCompliances_ObjectIdentity = ObjectIdentity
ogNetUpsMibCompliances = _OgNetUpsMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 16, 3, 1)
)
_OgNetUpsMibGroups_ObjectIdentity = ObjectIdentity
ogNetUpsMibGroups = _OgNetUpsMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 16, 3, 2)
)
_OgNetUpsMibObjects_ObjectIdentity = ObjectIdentity
ogNetUpsMibObjects = _OgNetUpsMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 16, 10)
)
_OgnupsEvent_ObjectIdentity = ObjectIdentity
ognupsEvent = _OgnupsEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 16, 10, 1)
)
_OgnupsEventTable_Object = MibTable
ognupsEventTable = _OgnupsEventTable_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 16, 10, 1, 1)
)
if mibBuilder.loadTexts:
    ognupsEventTable.setStatus("current")
_OgnupsEventEntry_Object = MibTableRow
ognupsEventEntry = _OgnupsEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 16, 10, 1, 1, 1)
)
ognupsEventEntry.setIndexNames(
    (0, "OG-UPS-MIB", "ognupsEventIndex"),
)
if mibBuilder.loadTexts:
    ognupsEventEntry.setStatus("current")


class _OgnupsEventIndex_Type(Integer32):
    """Custom type ognupsEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OgnupsEventIndex_Type.__name__ = "Integer32"
_OgnupsEventIndex_Object = MibTableColumn
ognupsEventIndex = _OgnupsEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 16, 10, 1, 1, 1, 1),
    _OgnupsEventIndex_Type()
)
ognupsEventIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ognupsEventIndex.setStatus("current")
_OgnupsEventName_Type = DisplayString
_OgnupsEventName_Object = MibTableColumn
ognupsEventName = _OgnupsEventName_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 16, 10, 1, 1, 1, 10),
    _OgnupsEventName_Type()
)
ognupsEventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ognupsEventName.setStatus("current")
_OgnupsEventType_Type = DisplayString
_OgnupsEventType_Object = MibTableColumn
ognupsEventType = _OgnupsEventType_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 16, 10, 1, 1, 1, 11),
    _OgnupsEventType_Type()
)
ognupsEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ognupsEventType.setStatus("current")

# Managed Objects groups

ogNetUpsMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25049, 10, 16, 3, 2, 1)
)
ogNetUpsMibGroup.setObjects(
      *(("OG-UPS-MIB", "ognupsEventName"),
        ("OG-UPS-MIB", "ognupsEventType"))
)
if mibBuilder.loadTexts:
    ogNetUpsMibGroup.setStatus("current")


# Notification objects

ognupsEventOccurred = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 10, 16, 2, 0, 200)
)
ognupsEventOccurred.setObjects(
      *(("OG-UPS-MIB", "ognupsEventName"),
        ("OG-UPS-MIB", "ognupsEventType"))
)
if mibBuilder.loadTexts:
    ognupsEventOccurred.setStatus(
        "current"
    )


# Notifications groups

ognupsNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 25049, 10, 16, 3, 2, 2)
)
ognupsNotificationsGroup.setObjects(
    ("OG-UPS-MIB", "ognupsEventOccurred")
)
if mibBuilder.loadTexts:
    ognupsNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ogNetUpsMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 25049, 10, 16, 3, 1, 1)
)
ogNetUpsMibCompliance.setObjects(
      *(("OG-UPS-MIB", "ogNetUpsMibGroup"),
        ("OG-UPS-MIB", "ognupsNotificationsGroup"))
)
if mibBuilder.loadTexts:
    ogNetUpsMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OG-UPS-MIB",
    **{"ogNetUpsMib": ogNetUpsMib,
       "ogNetUpsMibNotificationPrefix": ogNetUpsMibNotificationPrefix,
       "ognupsMibNotifications": ognupsMibNotifications,
       "ognupsEventOccurred": ognupsEventOccurred,
       "ogNetUpsMibConformance": ogNetUpsMibConformance,
       "ogNetUpsMibCompliances": ogNetUpsMibCompliances,
       "ogNetUpsMibCompliance": ogNetUpsMibCompliance,
       "ogNetUpsMibGroups": ogNetUpsMibGroups,
       "ogNetUpsMibGroup": ogNetUpsMibGroup,
       "ognupsNotificationsGroup": ognupsNotificationsGroup,
       "ogNetUpsMibObjects": ogNetUpsMibObjects,
       "ognupsEvent": ognupsEvent,
       "ognupsEventTable": ognupsEventTable,
       "ognupsEventEntry": ognupsEventEntry,
       "ognupsEventIndex": ognupsEventIndex,
       "ognupsEventName": ognupsEventName,
       "ognupsEventType": ognupsEventType}
)
