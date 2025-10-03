# SNMP MIB module (HH3C-SRV6-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-SRV6-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:33:00 2025
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

(InetAddressIPv6,
 InetAddressPrefixLength) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv6",
    "InetAddressPrefixLength")

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

hh3cSrv6 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 197)
)
if mibBuilder.loadTexts:
    hh3cSrv6.setRevisions(
        ("2020-08-31 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cSrv6Notifications_ObjectIdentity = ObjectIdentity
hh3cSrv6Notifications = _Hh3cSrv6Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 197, 0)
)
_Hh3cSrv6Objects_ObjectIdentity = ObjectIdentity
hh3cSrv6Objects = _Hh3cSrv6Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 197, 1)
)
_Hh3cSrv6NotificationEntry_ObjectIdentity = ObjectIdentity
hh3cSrv6NotificationEntry = _Hh3cSrv6NotificationEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 197, 1, 1)
)
_Hh3cSrv6NotificationSid_Type = InetAddressIPv6
_Hh3cSrv6NotificationSid_Object = MibScalar
hh3cSrv6NotificationSid = _Hh3cSrv6NotificationSid_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 197, 1, 1, 1),
    _Hh3cSrv6NotificationSid_Type()
)
hh3cSrv6NotificationSid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSrv6NotificationSid.setStatus("current")
_Hh3cSrv6NotificationSidPrefixLen_Type = InetAddressPrefixLength
_Hh3cSrv6NotificationSidPrefixLen_Object = MibScalar
hh3cSrv6NotificationSidPrefixLen = _Hh3cSrv6NotificationSidPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 197, 1, 1, 2),
    _Hh3cSrv6NotificationSidPrefixLen_Type()
)
hh3cSrv6NotificationSidPrefixLen.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSrv6NotificationSidPrefixLen.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cSrv6SidRouteConflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 197, 0, 1)
)
hh3cSrv6SidRouteConflict.setObjects(
      *(("HH3C-SRV6-MIB", "hh3cSrv6NotificationSid"),
        ("HH3C-SRV6-MIB", "hh3cSrv6NotificationSidPrefixLen"))
)
if mibBuilder.loadTexts:
    hh3cSrv6SidRouteConflict.setStatus(
        "current"
    )

hh3cSrv6SidRouteConflictClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 197, 0, 2)
)
hh3cSrv6SidRouteConflictClear.setObjects(
      *(("HH3C-SRV6-MIB", "hh3cSrv6NotificationSid"),
        ("HH3C-SRV6-MIB", "hh3cSrv6NotificationSidPrefixLen"))
)
if mibBuilder.loadTexts:
    hh3cSrv6SidRouteConflictClear.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-SRV6-MIB",
    **{"hh3cSrv6": hh3cSrv6,
       "hh3cSrv6Notifications": hh3cSrv6Notifications,
       "hh3cSrv6SidRouteConflict": hh3cSrv6SidRouteConflict,
       "hh3cSrv6SidRouteConflictClear": hh3cSrv6SidRouteConflictClear,
       "hh3cSrv6Objects": hh3cSrv6Objects,
       "hh3cSrv6NotificationEntry": hh3cSrv6NotificationEntry,
       "hh3cSrv6NotificationSid": hh3cSrv6NotificationSid,
       "hh3cSrv6NotificationSidPrefixLen": hh3cSrv6NotificationSidPrefixLen}
)
