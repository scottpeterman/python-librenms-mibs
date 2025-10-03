# SNMP MIB module (OG-FAILOVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\opengear\OG-FAILOVER-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:19:26 2025
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

ogFailoverMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 15)
)
if mibBuilder.loadTexts:
    ogFailoverMib.setRevisions(
        ("2013-08-11 00:00",
         "2010-03-22 11:27",
         "2008-11-27 11:40")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OgFailoverMibNotificationPrefix_ObjectIdentity = ObjectIdentity
ogFailoverMibNotificationPrefix = _OgFailoverMibNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 15, 2)
)
_OgfovrMibNotifications_ObjectIdentity = ObjectIdentity
ogfovrMibNotifications = _OgfovrMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 15, 2, 0)
)
_OgFailoverMibConformance_ObjectIdentity = ObjectIdentity
ogFailoverMibConformance = _OgFailoverMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 15, 3)
)
_OgFailoverMibCompliances_ObjectIdentity = ObjectIdentity
ogFailoverMibCompliances = _OgFailoverMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 15, 3, 1)
)
_OgFailoverMibGroups_ObjectIdentity = ObjectIdentity
ogFailoverMibGroups = _OgFailoverMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 15, 3, 2)
)
_OgFailoverMibObjects_ObjectIdentity = ObjectIdentity
ogFailoverMibObjects = _OgFailoverMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 15, 10)
)
_OgfovrEvent_ObjectIdentity = ObjectIdentity
ogfovrEvent = _OgfovrEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 15, 10, 1)
)
_OgfovrEventTable_Object = MibTable
ogfovrEventTable = _OgfovrEventTable_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 15, 10, 1, 1)
)
if mibBuilder.loadTexts:
    ogfovrEventTable.setStatus("current")
_OgfovrEventEntry_Object = MibTableRow
ogfovrEventEntry = _OgfovrEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 15, 10, 1, 1, 1)
)
ogfovrEventEntry.setIndexNames(
    (0, "OG-FAILOVER-MIB", "ogfovrEventIndex"),
)
if mibBuilder.loadTexts:
    ogfovrEventEntry.setStatus("current")


class _OgfovrEventIndex_Type(Integer32):
    """Custom type ogfovrEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OgfovrEventIndex_Type.__name__ = "Integer32"
_OgfovrEventIndex_Object = MibTableColumn
ogfovrEventIndex = _OgfovrEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 15, 10, 1, 1, 1, 1),
    _OgfovrEventIndex_Type()
)
ogfovrEventIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ogfovrEventIndex.setStatus("current")
_OgfovrEventPrimary_Type = DisplayString
_OgfovrEventPrimary_Object = MibTableColumn
ogfovrEventPrimary = _OgfovrEventPrimary_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 15, 10, 1, 1, 1, 10),
    _OgfovrEventPrimary_Type()
)
ogfovrEventPrimary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogfovrEventPrimary.setStatus("current")
_OgfovrEventSecondary_Type = DisplayString
_OgfovrEventSecondary_Object = MibTableColumn
ogfovrEventSecondary = _OgfovrEventSecondary_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 15, 10, 1, 1, 1, 11),
    _OgfovrEventSecondary_Type()
)
ogfovrEventSecondary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogfovrEventSecondary.setStatus("current")

# Managed Objects groups

ogFailoverMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25049, 10, 15, 3, 2, 1)
)
ogFailoverMibGroup.setObjects(
      *(("OG-FAILOVER-MIB", "ogfovrEventPrimary"),
        ("OG-FAILOVER-MIB", "ogfovrEventSecondary"))
)
if mibBuilder.loadTexts:
    ogFailoverMibGroup.setStatus("current")


# Notification objects

ogfovrEventOccurred = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 10, 15, 2, 0, 200)
)
ogfovrEventOccurred.setObjects(
      *(("OG-FAILOVER-MIB", "ogfovrEventPrimary"),
        ("OG-FAILOVER-MIB", "ogfovrEventSecondary"))
)
if mibBuilder.loadTexts:
    ogfovrEventOccurred.setStatus(
        "current"
    )


# Notifications groups

ogfovrNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 25049, 10, 15, 3, 2, 2)
)
ogfovrNotificationsGroup.setObjects(
    ("OG-FAILOVER-MIB", "ogfovrEventOccurred")
)
if mibBuilder.loadTexts:
    ogfovrNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ogFailoverMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 25049, 10, 15, 3, 1, 1)
)
ogFailoverMibCompliance.setObjects(
      *(("OG-FAILOVER-MIB", "ogFailoverMibGroup"),
        ("OG-FAILOVER-MIB", "ogfovrNotificationsGroup"))
)
if mibBuilder.loadTexts:
    ogFailoverMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OG-FAILOVER-MIB",
    **{"ogFailoverMib": ogFailoverMib,
       "ogFailoverMibNotificationPrefix": ogFailoverMibNotificationPrefix,
       "ogfovrMibNotifications": ogfovrMibNotifications,
       "ogfovrEventOccurred": ogfovrEventOccurred,
       "ogFailoverMibConformance": ogFailoverMibConformance,
       "ogFailoverMibCompliances": ogFailoverMibCompliances,
       "ogFailoverMibCompliance": ogFailoverMibCompliance,
       "ogFailoverMibGroups": ogFailoverMibGroups,
       "ogFailoverMibGroup": ogFailoverMibGroup,
       "ogfovrNotificationsGroup": ogfovrNotificationsGroup,
       "ogFailoverMibObjects": ogFailoverMibObjects,
       "ogfovrEvent": ogfovrEvent,
       "ogfovrEventTable": ogfovrEventTable,
       "ogfovrEventEntry": ogfovrEventEntry,
       "ogfovrEventIndex": ogfovrEventIndex,
       "ogfovrEventPrimary": ogfovrEventPrimary,
       "ogfovrEventSecondary": ogfovrEventSecondary}
)
