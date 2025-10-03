# SNMP MIB module (ARUBAWIRED-AAA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arubaos-cx\ARUBAWIRED-AAA-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:19:01 2025
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

(wndFeatures,) = mibBuilder.importSymbols(
    "ARUBAWIRED-NETWORKING-OID",
    "wndFeatures")

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

arubaWiredAAAMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 16)
)
if mibBuilder.loadTexts:
    arubaWiredAAAMIB.setRevisions(
        ("2021-07-14 00:00",
         "2020-10-08 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ArubaWiredAAAStatusNotifications_ObjectIdentity = ObjectIdentity
arubaWiredAAAStatusNotifications = _ArubaWiredAAAStatusNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 16, 0)
)
_ArubaWiredAAAObjects_ObjectIdentity = ObjectIdentity
arubaWiredAAAObjects = _ArubaWiredAAAObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 16, 1)
)
_ArubaWiredRadiusServer_ObjectIdentity = ObjectIdentity
arubaWiredRadiusServer = _ArubaWiredRadiusServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 16, 1, 1)
)
_ArubaWiredRadiusServerTable_Object = MibTable
arubaWiredRadiusServerTable = _ArubaWiredRadiusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 16, 1, 1, 1)
)
if mibBuilder.loadTexts:
    arubaWiredRadiusServerTable.setStatus("current")
_ArubaWiredRadiusServerEntry_Object = MibTableRow
arubaWiredRadiusServerEntry = _ArubaWiredRadiusServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 16, 1, 1, 1, 1)
)
arubaWiredRadiusServerEntry.setIndexNames(
    (0, "ARUBAWIRED-AAA-MIB", "arubaWiredRadiusServerVrfName"),
    (0, "ARUBAWIRED-AAA-MIB", "arubaWiredRadiusServerAddress"),
    (0, "ARUBAWIRED-AAA-MIB", "arubaWiredRadiusServerPort"),
    (0, "ARUBAWIRED-AAA-MIB", "arubaWiredRadiusServerPortType"),
)
if mibBuilder.loadTexts:
    arubaWiredRadiusServerEntry.setStatus("current")


class _ArubaWiredRadiusServerVrfName_Type(DisplayString):
    """Custom type arubaWiredRadiusServerVrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 33),
    )


_ArubaWiredRadiusServerVrfName_Type.__name__ = "DisplayString"
_ArubaWiredRadiusServerVrfName_Object = MibTableColumn
arubaWiredRadiusServerVrfName = _ArubaWiredRadiusServerVrfName_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 16, 1, 1, 1, 1, 1),
    _ArubaWiredRadiusServerVrfName_Type()
)
arubaWiredRadiusServerVrfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredRadiusServerVrfName.setStatus("current")


class _ArubaWiredRadiusServerAddress_Type(DisplayString):
    """Custom type arubaWiredRadiusServerAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 257),
    )


_ArubaWiredRadiusServerAddress_Type.__name__ = "DisplayString"
_ArubaWiredRadiusServerAddress_Object = MibTableColumn
arubaWiredRadiusServerAddress = _ArubaWiredRadiusServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 16, 1, 1, 1, 1, 2),
    _ArubaWiredRadiusServerAddress_Type()
)
arubaWiredRadiusServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredRadiusServerAddress.setStatus("current")


class _ArubaWiredRadiusServerPort_Type(Unsigned32):
    """Custom type arubaWiredRadiusServerPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ArubaWiredRadiusServerPort_Type.__name__ = "Unsigned32"
_ArubaWiredRadiusServerPort_Object = MibTableColumn
arubaWiredRadiusServerPort = _ArubaWiredRadiusServerPort_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 16, 1, 1, 1, 1, 3),
    _ArubaWiredRadiusServerPort_Type()
)
arubaWiredRadiusServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredRadiusServerPort.setStatus("current")


class _ArubaWiredRadiusServerPortType_Type(DisplayString):
    """Custom type arubaWiredRadiusServerPortType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_ArubaWiredRadiusServerPortType_Type.__name__ = "DisplayString"
_ArubaWiredRadiusServerPortType_Object = MibTableColumn
arubaWiredRadiusServerPortType = _ArubaWiredRadiusServerPortType_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 16, 1, 1, 1, 1, 4),
    _ArubaWiredRadiusServerPortType_Type()
)
arubaWiredRadiusServerPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredRadiusServerPortType.setStatus("current")


class _ArubaWiredRadiusServerReachabilityStatus_Type(DisplayString):
    """Custom type arubaWiredRadiusServerReachabilityStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ArubaWiredRadiusServerReachabilityStatus_Type.__name__ = "DisplayString"
_ArubaWiredRadiusServerReachabilityStatus_Object = MibTableColumn
arubaWiredRadiusServerReachabilityStatus = _ArubaWiredRadiusServerReachabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 16, 1, 1, 1, 1, 5),
    _ArubaWiredRadiusServerReachabilityStatus_Type()
)
arubaWiredRadiusServerReachabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredRadiusServerReachabilityStatus.setStatus("current")
_ArubaWiredTacacsServer_ObjectIdentity = ObjectIdentity
arubaWiredTacacsServer = _ArubaWiredTacacsServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 16, 1, 2)
)
_ArubaWiredTacacsServerTable_Object = MibTable
arubaWiredTacacsServerTable = _ArubaWiredTacacsServerTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 16, 1, 2, 1)
)
if mibBuilder.loadTexts:
    arubaWiredTacacsServerTable.setStatus("current")
_ArubaWiredTacacsServerEntry_Object = MibTableRow
arubaWiredTacacsServerEntry = _ArubaWiredTacacsServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 16, 1, 2, 1, 1)
)
arubaWiredTacacsServerEntry.setIndexNames(
    (0, "ARUBAWIRED-AAA-MIB", "arubaWiredTacacsServerVrfName"),
    (0, "ARUBAWIRED-AAA-MIB", "arubaWiredTacacsServerAddress"),
    (0, "ARUBAWIRED-AAA-MIB", "arubaWiredTacacsServerPort"),
)
if mibBuilder.loadTexts:
    arubaWiredTacacsServerEntry.setStatus("current")


class _ArubaWiredTacacsServerVrfName_Type(DisplayString):
    """Custom type arubaWiredTacacsServerVrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 33),
    )


_ArubaWiredTacacsServerVrfName_Type.__name__ = "DisplayString"
_ArubaWiredTacacsServerVrfName_Object = MibTableColumn
arubaWiredTacacsServerVrfName = _ArubaWiredTacacsServerVrfName_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 16, 1, 2, 1, 1, 1),
    _ArubaWiredTacacsServerVrfName_Type()
)
arubaWiredTacacsServerVrfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredTacacsServerVrfName.setStatus("current")


class _ArubaWiredTacacsServerAddress_Type(DisplayString):
    """Custom type arubaWiredTacacsServerAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 257),
    )


_ArubaWiredTacacsServerAddress_Type.__name__ = "DisplayString"
_ArubaWiredTacacsServerAddress_Object = MibTableColumn
arubaWiredTacacsServerAddress = _ArubaWiredTacacsServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 16, 1, 2, 1, 1, 2),
    _ArubaWiredTacacsServerAddress_Type()
)
arubaWiredTacacsServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredTacacsServerAddress.setStatus("current")


class _ArubaWiredTacacsServerPort_Type(Unsigned32):
    """Custom type arubaWiredTacacsServerPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ArubaWiredTacacsServerPort_Type.__name__ = "Unsigned32"
_ArubaWiredTacacsServerPort_Object = MibTableColumn
arubaWiredTacacsServerPort = _ArubaWiredTacacsServerPort_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 16, 1, 2, 1, 1, 3),
    _ArubaWiredTacacsServerPort_Type()
)
arubaWiredTacacsServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredTacacsServerPort.setStatus("current")


class _ArubaWiredTacacsServerReachabilityStatus_Type(DisplayString):
    """Custom type arubaWiredTacacsServerReachabilityStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ArubaWiredTacacsServerReachabilityStatus_Type.__name__ = "DisplayString"
_ArubaWiredTacacsServerReachabilityStatus_Object = MibTableColumn
arubaWiredTacacsServerReachabilityStatus = _ArubaWiredTacacsServerReachabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 16, 1, 2, 1, 1, 4),
    _ArubaWiredTacacsServerReachabilityStatus_Type()
)
arubaWiredTacacsServerReachabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredTacacsServerReachabilityStatus.setStatus("current")
_ArubaWiredAAAServerConformance_ObjectIdentity = ObjectIdentity
arubaWiredAAAServerConformance = _ArubaWiredAAAServerConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 16, 2)
)
_ArubaWiredRadiusServerGroups_ObjectIdentity = ObjectIdentity
arubaWiredRadiusServerGroups = _ArubaWiredRadiusServerGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 16, 2, 1)
)
_ArubaWiredRadiusServerCompliances_ObjectIdentity = ObjectIdentity
arubaWiredRadiusServerCompliances = _ArubaWiredRadiusServerCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 16, 2, 2)
)
_ArubaWiredTacacsServerGroups_ObjectIdentity = ObjectIdentity
arubaWiredTacacsServerGroups = _ArubaWiredTacacsServerGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 16, 2, 3)
)
_ArubaWiredTacacsServerCompliances_ObjectIdentity = ObjectIdentity
arubaWiredTacacsServerCompliances = _ArubaWiredTacacsServerCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 16, 2, 4)
)

# Managed Objects groups

arubaWiredRadiusServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 16, 2, 1, 1)
)
arubaWiredRadiusServerGroup.setObjects(
      *(("ARUBAWIRED-AAA-MIB", "arubaWiredRadiusServerVrfName"),
        ("ARUBAWIRED-AAA-MIB", "arubaWiredRadiusServerAddress"),
        ("ARUBAWIRED-AAA-MIB", "arubaWiredRadiusServerPort"),
        ("ARUBAWIRED-AAA-MIB", "arubaWiredRadiusServerPortType"),
        ("ARUBAWIRED-AAA-MIB", "arubaWiredRadiusServerReachabilityStatus"))
)
if mibBuilder.loadTexts:
    arubaWiredRadiusServerGroup.setStatus("current")

arubaWiredTacacsServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 16, 2, 1, 3)
)
arubaWiredTacacsServerGroup.setObjects(
      *(("ARUBAWIRED-AAA-MIB", "arubaWiredTacacsServerVrfName"),
        ("ARUBAWIRED-AAA-MIB", "arubaWiredTacacsServerAddress"),
        ("ARUBAWIRED-AAA-MIB", "arubaWiredTacacsServerPort"),
        ("ARUBAWIRED-AAA-MIB", "arubaWiredTacacsServerReachabilityStatus"))
)
if mibBuilder.loadTexts:
    arubaWiredTacacsServerGroup.setStatus("current")


# Notification objects

arubaWiredRadiusServerStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 16, 0, 1)
)
arubaWiredRadiusServerStatusChange.setObjects(
      *(("ARUBAWIRED-AAA-MIB", "arubaWiredRadiusServerVrfName"),
        ("ARUBAWIRED-AAA-MIB", "arubaWiredRadiusServerAddress"),
        ("ARUBAWIRED-AAA-MIB", "arubaWiredRadiusServerPort"),
        ("ARUBAWIRED-AAA-MIB", "arubaWiredRadiusServerPortType"),
        ("ARUBAWIRED-AAA-MIB", "arubaWiredRadiusServerReachabilityStatus"))
)
if mibBuilder.loadTexts:
    arubaWiredRadiusServerStatusChange.setStatus(
        "current"
    )

arubaWiredTacacsServerStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 16, 0, 2)
)
arubaWiredTacacsServerStatusChange.setObjects(
      *(("ARUBAWIRED-AAA-MIB", "arubaWiredTacacsServerVrfName"),
        ("ARUBAWIRED-AAA-MIB", "arubaWiredTacacsServerAddress"),
        ("ARUBAWIRED-AAA-MIB", "arubaWiredTacacsServerPort"),
        ("ARUBAWIRED-AAA-MIB", "arubaWiredTacacsServerReachabilityStatus"))
)
if mibBuilder.loadTexts:
    arubaWiredTacacsServerStatusChange.setStatus(
        "current"
    )


# Notifications groups

arubaWiredAAARadiusStatusNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 16, 2, 1, 2)
)
arubaWiredAAARadiusStatusNotificationsGroup.setObjects(
    ("ARUBAWIRED-AAA-MIB", "arubaWiredRadiusServerStatusChange")
)
if mibBuilder.loadTexts:
    arubaWiredAAARadiusStatusNotificationsGroup.setStatus(
        "current"
    )

arubaWiredAAATacacsStatusNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 16, 2, 1, 4)
)
arubaWiredAAATacacsStatusNotificationsGroup.setObjects(
    ("ARUBAWIRED-AAA-MIB", "arubaWiredTacacsServerStatusChange")
)
if mibBuilder.loadTexts:
    arubaWiredAAATacacsStatusNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

arubaWiredRadiusServerCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 16, 2, 2, 1)
)
arubaWiredRadiusServerCompliance.setObjects(
      *(("ARUBAWIRED-AAA-MIB", "arubaWiredRadiusServerGroup"),
        ("ARUBAWIRED-AAA-MIB", "arubaWiredAAARadiusStatusNotificationsGroup"))
)
if mibBuilder.loadTexts:
    arubaWiredRadiusServerCompliance.setStatus(
        "current"
    )

arubaWiredTacacsServerCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 16, 2, 2, 2)
)
arubaWiredTacacsServerCompliance.setObjects(
      *(("ARUBAWIRED-AAA-MIB", "arubaWiredTacacsServerGroup"),
        ("ARUBAWIRED-AAA-MIB", "arubaWiredAAATacacsStatusNotificationsGroup"))
)
if mibBuilder.loadTexts:
    arubaWiredTacacsServerCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARUBAWIRED-AAA-MIB",
    **{"arubaWiredAAAMIB": arubaWiredAAAMIB,
       "arubaWiredAAAStatusNotifications": arubaWiredAAAStatusNotifications,
       "arubaWiredRadiusServerStatusChange": arubaWiredRadiusServerStatusChange,
       "arubaWiredTacacsServerStatusChange": arubaWiredTacacsServerStatusChange,
       "arubaWiredAAAObjects": arubaWiredAAAObjects,
       "arubaWiredRadiusServer": arubaWiredRadiusServer,
       "arubaWiredRadiusServerTable": arubaWiredRadiusServerTable,
       "arubaWiredRadiusServerEntry": arubaWiredRadiusServerEntry,
       "arubaWiredRadiusServerVrfName": arubaWiredRadiusServerVrfName,
       "arubaWiredRadiusServerAddress": arubaWiredRadiusServerAddress,
       "arubaWiredRadiusServerPort": arubaWiredRadiusServerPort,
       "arubaWiredRadiusServerPortType": arubaWiredRadiusServerPortType,
       "arubaWiredRadiusServerReachabilityStatus": arubaWiredRadiusServerReachabilityStatus,
       "arubaWiredTacacsServer": arubaWiredTacacsServer,
       "arubaWiredTacacsServerTable": arubaWiredTacacsServerTable,
       "arubaWiredTacacsServerEntry": arubaWiredTacacsServerEntry,
       "arubaWiredTacacsServerVrfName": arubaWiredTacacsServerVrfName,
       "arubaWiredTacacsServerAddress": arubaWiredTacacsServerAddress,
       "arubaWiredTacacsServerPort": arubaWiredTacacsServerPort,
       "arubaWiredTacacsServerReachabilityStatus": arubaWiredTacacsServerReachabilityStatus,
       "arubaWiredAAAServerConformance": arubaWiredAAAServerConformance,
       "arubaWiredRadiusServerGroups": arubaWiredRadiusServerGroups,
       "arubaWiredRadiusServerGroup": arubaWiredRadiusServerGroup,
       "arubaWiredAAARadiusStatusNotificationsGroup": arubaWiredAAARadiusStatusNotificationsGroup,
       "arubaWiredTacacsServerGroup": arubaWiredTacacsServerGroup,
       "arubaWiredAAATacacsStatusNotificationsGroup": arubaWiredAAATacacsStatusNotificationsGroup,
       "arubaWiredRadiusServerCompliances": arubaWiredRadiusServerCompliances,
       "arubaWiredRadiusServerCompliance": arubaWiredRadiusServerCompliance,
       "arubaWiredTacacsServerCompliance": arubaWiredTacacsServerCompliance,
       "arubaWiredTacacsServerGroups": arubaWiredTacacsServerGroups,
       "arubaWiredTacacsServerCompliances": arubaWiredTacacsServerCompliances}
)
