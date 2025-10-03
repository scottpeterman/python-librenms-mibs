# SNMP MIB module (HH3C-CUSP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-CUSP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:30:55 2025
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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

hh3cCusp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 190)
)
if mibBuilder.loadTexts:
    hh3cCusp.setRevisions(
        ("2020-09-11 13:00",
         "2020-07-20 13:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cCuspMibTrap_ObjectIdentity = ObjectIdentity
hh3cCuspMibTrap = _Hh3cCuspMibTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 190, 1)
)
_Hh3cCuspMibTrapOid_ObjectIdentity = ObjectIdentity
hh3cCuspMibTrapOid = _Hh3cCuspMibTrapOid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 190, 1, 1)
)


class _Hh3cCuspServerDisconnectReason_Type(Integer32):
    """Custom type hh3cCuspServerDisconnectReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_Hh3cCuspServerDisconnectReason_Type.__name__ = "Integer32"
_Hh3cCuspServerDisconnectReason_Object = MibScalar
hh3cCuspServerDisconnectReason = _Hh3cCuspServerDisconnectReason_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 190, 1, 1, 1),
    _Hh3cCuspServerDisconnectReason_Type()
)
hh3cCuspServerDisconnectReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cCuspServerDisconnectReason.setStatus("current")


class _Hh3cCuspClientDisconnectReason_Type(Integer32):
    """Custom type hh3cCuspClientDisconnectReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Hh3cCuspClientDisconnectReason_Type.__name__ = "Integer32"
_Hh3cCuspClientDisconnectReason_Object = MibScalar
hh3cCuspClientDisconnectReason = _Hh3cCuspClientDisconnectReason_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 190, 1, 1, 2),
    _Hh3cCuspClientDisconnectReason_Type()
)
hh3cCuspClientDisconnectReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cCuspClientDisconnectReason.setStatus("current")


class _Hh3cCuspVpnInstanceName_Type(OctetString):
    """Custom type hh3cCuspVpnInstanceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Hh3cCuspVpnInstanceName_Type.__name__ = "OctetString"
_Hh3cCuspVpnInstanceName_Object = MibScalar
hh3cCuspVpnInstanceName = _Hh3cCuspVpnInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 190, 1, 1, 3),
    _Hh3cCuspVpnInstanceName_Type()
)
hh3cCuspVpnInstanceName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cCuspVpnInstanceName.setStatus("current")
_Hh3cCuspLocalIPaddressType_Type = InetAddressType
_Hh3cCuspLocalIPaddressType_Object = MibScalar
hh3cCuspLocalIPaddressType = _Hh3cCuspLocalIPaddressType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 190, 1, 1, 4),
    _Hh3cCuspLocalIPaddressType_Type()
)
hh3cCuspLocalIPaddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cCuspLocalIPaddressType.setStatus("current")
_Hh3cCuspLocalIPaddress_Type = InetAddress
_Hh3cCuspLocalIPaddress_Object = MibScalar
hh3cCuspLocalIPaddress = _Hh3cCuspLocalIPaddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 190, 1, 1, 5),
    _Hh3cCuspLocalIPaddress_Type()
)
hh3cCuspLocalIPaddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cCuspLocalIPaddress.setStatus("current")
_Hh3cCuspRemoteIPaddressType_Type = InetAddressType
_Hh3cCuspRemoteIPaddressType_Object = MibScalar
hh3cCuspRemoteIPaddressType = _Hh3cCuspRemoteIPaddressType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 190, 1, 1, 6),
    _Hh3cCuspRemoteIPaddressType_Type()
)
hh3cCuspRemoteIPaddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cCuspRemoteIPaddressType.setStatus("current")
_Hh3cCuspRemoteIPaddress_Type = InetAddress
_Hh3cCuspRemoteIPaddress_Object = MibScalar
hh3cCuspRemoteIPaddress = _Hh3cCuspRemoteIPaddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 190, 1, 1, 7),
    _Hh3cCuspRemoteIPaddress_Type()
)
hh3cCuspRemoteIPaddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cCuspRemoteIPaddress.setStatus("current")
_Hh3cCuspTraps_ObjectIdentity = ObjectIdentity
hh3cCuspTraps = _Hh3cCuspTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 190, 1, 2)
)
_Hh3cCuspTrapsPrefix_ObjectIdentity = ObjectIdentity
hh3cCuspTrapsPrefix = _Hh3cCuspTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 190, 1, 2, 0)
)

# Managed Objects groups


# Notification objects

hh3cCuspServerDisconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 190, 1, 2, 0, 1)
)
hh3cCuspServerDisconnect.setObjects(
      *(("HH3C-CUSP-MIB", "hh3cCuspLocalIPaddressType"),
        ("HH3C-CUSP-MIB", "hh3cCuspLocalIPaddress"),
        ("HH3C-CUSP-MIB", "hh3cCuspRemoteIPaddressType"),
        ("HH3C-CUSP-MIB", "hh3cCuspRemoteIPaddress"),
        ("HH3C-CUSP-MIB", "hh3cCuspVpnInstanceName"),
        ("HH3C-CUSP-MIB", "hh3cCuspServerDisconnectReason"))
)
if mibBuilder.loadTexts:
    hh3cCuspServerDisconnect.setStatus(
        "current"
    )

hh3cCuspServerConnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 190, 1, 2, 0, 2)
)
hh3cCuspServerConnect.setObjects(
      *(("HH3C-CUSP-MIB", "hh3cCuspLocalIPaddressType"),
        ("HH3C-CUSP-MIB", "hh3cCuspLocalIPaddress"),
        ("HH3C-CUSP-MIB", "hh3cCuspRemoteIPaddressType"),
        ("HH3C-CUSP-MIB", "hh3cCuspRemoteIPaddress"),
        ("HH3C-CUSP-MIB", "hh3cCuspVpnInstanceName"))
)
if mibBuilder.loadTexts:
    hh3cCuspServerConnect.setStatus(
        "current"
    )

hh3cCuspClientDisconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 190, 1, 2, 0, 3)
)
hh3cCuspClientDisconnect.setObjects(
      *(("HH3C-CUSP-MIB", "hh3cCuspLocalIPaddressType"),
        ("HH3C-CUSP-MIB", "hh3cCuspLocalIPaddress"),
        ("HH3C-CUSP-MIB", "hh3cCuspRemoteIPaddressType"),
        ("HH3C-CUSP-MIB", "hh3cCuspRemoteIPaddress"),
        ("HH3C-CUSP-MIB", "hh3cCuspVpnInstanceName"),
        ("HH3C-CUSP-MIB", "hh3cCuspClientDisconnectReason"))
)
if mibBuilder.loadTexts:
    hh3cCuspClientDisconnect.setStatus(
        "current"
    )

hh3cCuspClientConnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 190, 1, 2, 0, 4)
)
hh3cCuspClientConnect.setObjects(
      *(("HH3C-CUSP-MIB", "hh3cCuspLocalIPaddressType"),
        ("HH3C-CUSP-MIB", "hh3cCuspLocalIPaddress"),
        ("HH3C-CUSP-MIB", "hh3cCuspRemoteIPaddressType"),
        ("HH3C-CUSP-MIB", "hh3cCuspRemoteIPaddress"),
        ("HH3C-CUSP-MIB", "hh3cCuspVpnInstanceName"))
)
if mibBuilder.loadTexts:
    hh3cCuspClientConnect.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-CUSP-MIB",
    **{"hh3cCusp": hh3cCusp,
       "hh3cCuspMibTrap": hh3cCuspMibTrap,
       "hh3cCuspMibTrapOid": hh3cCuspMibTrapOid,
       "hh3cCuspServerDisconnectReason": hh3cCuspServerDisconnectReason,
       "hh3cCuspClientDisconnectReason": hh3cCuspClientDisconnectReason,
       "hh3cCuspVpnInstanceName": hh3cCuspVpnInstanceName,
       "hh3cCuspLocalIPaddressType": hh3cCuspLocalIPaddressType,
       "hh3cCuspLocalIPaddress": hh3cCuspLocalIPaddress,
       "hh3cCuspRemoteIPaddressType": hh3cCuspRemoteIPaddressType,
       "hh3cCuspRemoteIPaddress": hh3cCuspRemoteIPaddress,
       "hh3cCuspTraps": hh3cCuspTraps,
       "hh3cCuspTrapsPrefix": hh3cCuspTrapsPrefix,
       "hh3cCuspServerDisconnect": hh3cCuspServerDisconnect,
       "hh3cCuspServerConnect": hh3cCuspServerConnect,
       "hh3cCuspClientDisconnect": hh3cCuspClientDisconnect,
       "hh3cCuspClientConnect": hh3cCuspClientConnect}
)
