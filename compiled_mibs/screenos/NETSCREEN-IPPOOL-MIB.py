# SNMP MIB module (NETSCREEN-IPPOOL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\screenos\NETSCREEN-IPPOOL-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:25:21 2025
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

(netscreenVpn,
 netscreenVpnMibModule) = mibBuilder.importSymbols(
    "NETSCREEN-SMI",
    "netscreenVpn",
    "netscreenVpnMibModule")

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

netscreenIppoolMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 4, 0, 9)
)
if mibBuilder.loadTexts:
    netscreenIppoolMibModule.setRevisions(
        ("2004-05-03 00:00",
         "2004-03-03 00:00",
         "2003-11-13 00:00",
         "2001-09-28 00:00",
         "2000-08-27 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NsVpnIpPool_ObjectIdentity = ObjectIdentity
nsVpnIpPool = _NsVpnIpPool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 4, 9)
)
_NsVpnIpPoolTable_Object = MibTable
nsVpnIpPoolTable = _NsVpnIpPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 9, 1)
)
if mibBuilder.loadTexts:
    nsVpnIpPoolTable.setStatus("current")
_NsVpnIpPoolEntry_Object = MibTableRow
nsVpnIpPoolEntry = _NsVpnIpPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 9, 1, 1)
)
nsVpnIpPoolEntry.setIndexNames(
    (0, "NETSCREEN-IPPOOL-MIB", "nsVpnIpPoolIndex"),
)
if mibBuilder.loadTexts:
    nsVpnIpPoolEntry.setStatus("current")


class _NsVpnIpPoolIndex_Type(Integer32):
    """Custom type nsVpnIpPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsVpnIpPoolIndex_Type.__name__ = "Integer32"
_NsVpnIpPoolIndex_Object = MibTableColumn
nsVpnIpPoolIndex = _NsVpnIpPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 9, 1, 1, 1),
    _NsVpnIpPoolIndex_Type()
)
nsVpnIpPoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnIpPoolIndex.setStatus("current")


class _NsVpnIpPoolName_Type(DisplayString):
    """Custom type nsVpnIpPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsVpnIpPoolName_Type.__name__ = "DisplayString"
_NsVpnIpPoolName_Object = MibTableColumn
nsVpnIpPoolName = _NsVpnIpPoolName_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 9, 1, 1, 2),
    _NsVpnIpPoolName_Type()
)
nsVpnIpPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnIpPoolName.setStatus("current")
_NsVpnIpPoolStartIp_Type = IpAddress
_NsVpnIpPoolStartIp_Object = MibTableColumn
nsVpnIpPoolStartIp = _NsVpnIpPoolStartIp_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 9, 1, 1, 3),
    _NsVpnIpPoolStartIp_Type()
)
nsVpnIpPoolStartIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnIpPoolStartIp.setStatus("current")
_NsVpnIpPoolEndIp_Type = IpAddress
_NsVpnIpPoolEndIp_Object = MibTableColumn
nsVpnIpPoolEndIp = _NsVpnIpPoolEndIp_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 9, 1, 1, 4),
    _NsVpnIpPoolEndIp_Type()
)
nsVpnIpPoolEndIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnIpPoolEndIp.setStatus("current")
_NsVpnIpPoolIpUsed_Type = Integer32
_NsVpnIpPoolIpUsed_Object = MibTableColumn
nsVpnIpPoolIpUsed = _NsVpnIpPoolIpUsed_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 9, 1, 1, 5),
    _NsVpnIpPoolIpUsed_Type()
)
nsVpnIpPoolIpUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnIpPoolIpUsed.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSCREEN-IPPOOL-MIB",
    **{"netscreenIppoolMibModule": netscreenIppoolMibModule,
       "nsVpnIpPool": nsVpnIpPool,
       "nsVpnIpPoolTable": nsVpnIpPoolTable,
       "nsVpnIpPoolEntry": nsVpnIpPoolEntry,
       "nsVpnIpPoolIndex": nsVpnIpPoolIndex,
       "nsVpnIpPoolName": nsVpnIpPoolName,
       "nsVpnIpPoolStartIp": nsVpnIpPoolStartIp,
       "nsVpnIpPoolEndIp": nsVpnIpPoolEndIp,
       "nsVpnIpPoolIpUsed": nsVpnIpPoolIpUsed}
)
