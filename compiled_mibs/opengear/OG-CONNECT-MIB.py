# SNMP MIB module (OG-CONNECT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\opengear\OG-CONNECT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:19:24 2025
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

ogConnectMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 10)
)
if mibBuilder.loadTexts:
    ogConnectMib.setRevisions(
        ("2013-08-11 00:00",
         "2010-03-22 11:27",
         "2008-11-27 11:40")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OgConnectMibNotificationPrefix_ObjectIdentity = ObjectIdentity
ogConnectMibNotificationPrefix = _OgConnectMibNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 10, 2)
)
_OgconnMibNotifications_ObjectIdentity = ObjectIdentity
ogconnMibNotifications = _OgconnMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 10, 2, 0)
)
_OgConnectMibConformance_ObjectIdentity = ObjectIdentity
ogConnectMibConformance = _OgConnectMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 10, 3)
)
_OgConnectMibCompliances_ObjectIdentity = ObjectIdentity
ogConnectMibCompliances = _OgConnectMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 10, 3, 1)
)
_OgConnectMibGroups_ObjectIdentity = ObjectIdentity
ogConnectMibGroups = _OgConnectMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 10, 3, 2)
)
_OgConnectMibObjects_ObjectIdentity = ObjectIdentity
ogConnectMibObjects = _OgConnectMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 10, 10)
)
_OgconnEvent_ObjectIdentity = ObjectIdentity
ogconnEvent = _OgconnEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 10, 10, 1)
)
_OgconnEventTable_Object = MibTable
ogconnEventTable = _OgconnEventTable_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 10, 10, 1, 1)
)
if mibBuilder.loadTexts:
    ogconnEventTable.setStatus("current")
_OgconnEventEntry_Object = MibTableRow
ogconnEventEntry = _OgconnEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 10, 10, 1, 1, 1)
)
ogconnEventEntry.setIndexNames(
    (0, "OG-CONNECT-MIB", "ogconnEventIndex"),
)
if mibBuilder.loadTexts:
    ogconnEventEntry.setStatus("current")


class _OgconnEventIndex_Type(Integer32):
    """Custom type ogconnEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OgconnEventIndex_Type.__name__ = "Integer32"
_OgconnEventIndex_Object = MibTableColumn
ogconnEventIndex = _OgconnEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 10, 10, 1, 1, 1, 1),
    _OgconnEventIndex_Type()
)
ogconnEventIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ogconnEventIndex.setStatus("current")
_OgconnEventUsername_Type = DisplayString
_OgconnEventUsername_Object = MibTableColumn
ogconnEventUsername = _OgconnEventUsername_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 10, 10, 1, 1, 1, 10),
    _OgconnEventUsername_Type()
)
ogconnEventUsername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogconnEventUsername.setStatus("current")
_OgconnEventType_Type = DisplayString
_OgconnEventType_Object = MibTableColumn
ogconnEventType = _OgconnEventType_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 10, 10, 1, 1, 1, 11),
    _OgconnEventType_Type()
)
ogconnEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogconnEventType.setStatus("current")
_OgconnEventPortNumber_Type = Integer32
_OgconnEventPortNumber_Object = MibTableColumn
ogconnEventPortNumber = _OgconnEventPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 10, 10, 1, 1, 1, 12),
    _OgconnEventPortNumber_Type()
)
ogconnEventPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogconnEventPortNumber.setStatus("current")
_OgconnEventPortLabel_Type = DisplayString
_OgconnEventPortLabel_Object = MibTableColumn
ogconnEventPortLabel = _OgconnEventPortLabel_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 10, 10, 1, 1, 1, 13),
    _OgconnEventPortLabel_Type()
)
ogconnEventPortLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogconnEventPortLabel.setStatus("current")

# Managed Objects groups

ogConnectMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25049, 10, 10, 3, 2, 1)
)
ogConnectMibGroup.setObjects(
      *(("OG-CONNECT-MIB", "ogconnEventUsername"),
        ("OG-CONNECT-MIB", "ogconnEventType"),
        ("OG-CONNECT-MIB", "ogconnEventPortNumber"),
        ("OG-CONNECT-MIB", "ogconnEventPortLabel"))
)
if mibBuilder.loadTexts:
    ogConnectMibGroup.setStatus("current")


# Notification objects

ogconnEventOccurred = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 10, 10, 2, 0, 200)
)
ogconnEventOccurred.setObjects(
      *(("OG-CONNECT-MIB", "ogconnEventUsername"),
        ("OG-CONNECT-MIB", "ogconnEventType"),
        ("OG-CONNECT-MIB", "ogconnEventPortNumber"),
        ("OG-CONNECT-MIB", "ogconnEventPortLabel"))
)
if mibBuilder.loadTexts:
    ogconnEventOccurred.setStatus(
        "current"
    )


# Notifications groups

ogconnNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 25049, 10, 10, 3, 2, 2)
)
ogconnNotificationsGroup.setObjects(
    ("OG-CONNECT-MIB", "ogconnEventOccurred")
)
if mibBuilder.loadTexts:
    ogconnNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ogConnectMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 25049, 10, 10, 3, 1, 1)
)
ogConnectMibCompliance.setObjects(
      *(("OG-CONNECT-MIB", "ogConnectMibGroup"),
        ("OG-CONNECT-MIB", "ogconnNotificationsGroup"))
)
if mibBuilder.loadTexts:
    ogConnectMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OG-CONNECT-MIB",
    **{"ogConnectMib": ogConnectMib,
       "ogConnectMibNotificationPrefix": ogConnectMibNotificationPrefix,
       "ogconnMibNotifications": ogconnMibNotifications,
       "ogconnEventOccurred": ogconnEventOccurred,
       "ogConnectMibConformance": ogConnectMibConformance,
       "ogConnectMibCompliances": ogConnectMibCompliances,
       "ogConnectMibCompliance": ogConnectMibCompliance,
       "ogConnectMibGroups": ogConnectMibGroups,
       "ogConnectMibGroup": ogConnectMibGroup,
       "ogconnNotificationsGroup": ogconnNotificationsGroup,
       "ogConnectMibObjects": ogConnectMibObjects,
       "ogconnEvent": ogconnEvent,
       "ogconnEventTable": ogconnEventTable,
       "ogconnEventEntry": ogconnEventEntry,
       "ogconnEventIndex": ogconnEventIndex,
       "ogconnEventUsername": ogconnEventUsername,
       "ogconnEventType": ogconnEventType,
       "ogconnEventPortNumber": ogconnEventPortNumber,
       "ogconnEventPortLabel": ogconnEventPortLabel}
)
