# SNMP MIB module (JUNIPER-IPFORWARD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junos\JUNIPER-IPFORWARD-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:03:19 2025
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

(inetCidrRouteEntry,
 ipCidrRouteEntry) = mibBuilder.importSymbols(
    "IP-FORWARD-MIB",
    "inetCidrRouteEntry",
    "ipCidrRouteEntry")

(jnxMibs,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxMibs")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

jnxIpForwardMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 38)
)
if mibBuilder.loadTexts:
    jnxIpForwardMIB.setRevisions(
        ("2011-11-13 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxIpCidrRouteTable_Object = MibTable
jnxIpCidrRouteTable = _JnxIpCidrRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 38, 1)
)
if mibBuilder.loadTexts:
    jnxIpCidrRouteTable.setStatus("deprecated")
_JnxIpCidrRouteEntry_Object = MibTableRow
jnxIpCidrRouteEntry = _JnxIpCidrRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 38, 1, 1)
)
if mibBuilder.loadTexts:
    jnxIpCidrRouteEntry.setStatus("deprecated")


class _JnxIpCidrRouteTunnelName_Type(SnmpAdminString):
    """Custom type jnxIpCidrRouteTunnelName based on SnmpAdminString"""
    defaultValue = OctetString("")


_JnxIpCidrRouteTunnelName_Type.__name__ = "SnmpAdminString"
_JnxIpCidrRouteTunnelName_Object = MibTableColumn
jnxIpCidrRouteTunnelName = _JnxIpCidrRouteTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 38, 1, 1, 1),
    _JnxIpCidrRouteTunnelName_Type()
)
jnxIpCidrRouteTunnelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpCidrRouteTunnelName.setStatus("deprecated")
_JnxInetCidrRouteTable_Object = MibTable
jnxInetCidrRouteTable = _JnxInetCidrRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 38, 2)
)
if mibBuilder.loadTexts:
    jnxInetCidrRouteTable.setStatus("current")
_JnxInetCidrRouteEntry_Object = MibTableRow
jnxInetCidrRouteEntry = _JnxInetCidrRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 38, 2, 1)
)
if mibBuilder.loadTexts:
    jnxInetCidrRouteEntry.setStatus("current")


class _JnxInetCidrRouteTunnelName_Type(SnmpAdminString):
    """Custom type jnxInetCidrRouteTunnelName based on SnmpAdminString"""
    defaultValue = OctetString("")


_JnxInetCidrRouteTunnelName_Type.__name__ = "SnmpAdminString"
_JnxInetCidrRouteTunnelName_Object = MibTableColumn
jnxInetCidrRouteTunnelName = _JnxInetCidrRouteTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 38, 2, 1, 1),
    _JnxInetCidrRouteTunnelName_Type()
)
jnxInetCidrRouteTunnelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxInetCidrRouteTunnelName.setStatus("current")
ipCidrRouteEntry.registerAugmentions(
    ("JUNIPER-IPFORWARD-MIB",
     "jnxIpCidrRouteEntry")
)
jnxIpCidrRouteEntry.setIndexNames(*ipCidrRouteEntry.getIndexNames())
inetCidrRouteEntry.registerAugmentions(
    ("JUNIPER-IPFORWARD-MIB",
     "jnxInetCidrRouteEntry")
)
jnxInetCidrRouteEntry.setIndexNames(*inetCidrRouteEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-IPFORWARD-MIB",
    **{"jnxIpForwardMIB": jnxIpForwardMIB,
       "jnxIpCidrRouteTable": jnxIpCidrRouteTable,
       "jnxIpCidrRouteEntry": jnxIpCidrRouteEntry,
       "jnxIpCidrRouteTunnelName": jnxIpCidrRouteTunnelName,
       "jnxInetCidrRouteTable": jnxInetCidrRouteTable,
       "jnxInetCidrRouteEntry": jnxInetCidrRouteEntry,
       "jnxInetCidrRouteTunnelName": jnxInetCidrRouteTunnelName}
)
