# SNMP MIB module (HH3C-DHCP6-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-DHCP6-SERVER-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:30:58 2025
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

(InetAddressIPv6,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv6")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hh3cDHCP6Server = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 159)
)
if mibBuilder.loadTexts:
    hh3cDHCP6Server.setRevisions(
        ("2014-10-30 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cDHCP6ServerTables_ObjectIdentity = ObjectIdentity
hh3cDHCP6ServerTables = _Hh3cDHCP6ServerTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 159, 1)
)
_Hh3cDHCPS6PoolTable_Object = MibTable
hh3cDHCPS6PoolTable = _Hh3cDHCPS6PoolTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 159, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cDHCPS6PoolTable.setStatus("current")
_Hh3cDHCPS6PoolEntry_Object = MibTableRow
hh3cDHCPS6PoolEntry = _Hh3cDHCPS6PoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 159, 1, 1, 1)
)
hh3cDHCPS6PoolEntry.setIndexNames(
    (0, "HH3C-DHCP6-SERVER-MIB", "hh3cDHCPS6PoolName"),
)
if mibBuilder.loadTexts:
    hh3cDHCPS6PoolEntry.setStatus("current")


class _Hh3cDHCPS6PoolName_Type(OctetString):
    """Custom type hh3cDHCPS6PoolName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_Hh3cDHCPS6PoolName_Type.__name__ = "OctetString"
_Hh3cDHCPS6PoolName_Object = MibTableColumn
hh3cDHCPS6PoolName = _Hh3cDHCPS6PoolName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 159, 1, 1, 1, 1),
    _Hh3cDHCPS6PoolName_Type()
)
hh3cDHCPS6PoolName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDHCPS6PoolName.setStatus("current")
_Hh3cDHCPS6PoolRowStatus_Type = RowStatus
_Hh3cDHCPS6PoolRowStatus_Object = MibTableColumn
hh3cDHCPS6PoolRowStatus = _Hh3cDHCPS6PoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 159, 1, 1, 1, 2),
    _Hh3cDHCPS6PoolRowStatus_Type()
)
hh3cDHCPS6PoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDHCPS6PoolRowStatus.setStatus("current")
_Hh3cDHCPS6PoolConfigTable_Object = MibTable
hh3cDHCPS6PoolConfigTable = _Hh3cDHCPS6PoolConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 159, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cDHCPS6PoolConfigTable.setStatus("current")
_Hh3cDHCPS6PoolConfigEntry_Object = MibTableRow
hh3cDHCPS6PoolConfigEntry = _Hh3cDHCPS6PoolConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 159, 1, 2, 1)
)
hh3cDHCPS6PoolConfigEntry.setIndexNames(
    (0, "HH3C-DHCP6-SERVER-MIB", "hh3cDHCPS6PoolName"),
)
if mibBuilder.loadTexts:
    hh3cDHCPS6PoolConfigEntry.setStatus("current")
_Hh3cDHCPS6PoolPrimaryDNSIP_Type = InetAddressIPv6
_Hh3cDHCPS6PoolPrimaryDNSIP_Object = MibTableColumn
hh3cDHCPS6PoolPrimaryDNSIP = _Hh3cDHCPS6PoolPrimaryDNSIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 159, 1, 2, 1, 1),
    _Hh3cDHCPS6PoolPrimaryDNSIP_Type()
)
hh3cDHCPS6PoolPrimaryDNSIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPS6PoolPrimaryDNSIP.setStatus("current")
_Hh3cDHCPS6PoolSecondDNSIP_Type = InetAddressIPv6
_Hh3cDHCPS6PoolSecondDNSIP_Object = MibTableColumn
hh3cDHCPS6PoolSecondDNSIP = _Hh3cDHCPS6PoolSecondDNSIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 159, 1, 2, 1, 2),
    _Hh3cDHCPS6PoolSecondDNSIP_Type()
)
hh3cDHCPS6PoolSecondDNSIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPS6PoolSecondDNSIP.setStatus("current")
_Hh3cDHCPS6PoolNetworkTable_Object = MibTable
hh3cDHCPS6PoolNetworkTable = _Hh3cDHCPS6PoolNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 159, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cDHCPS6PoolNetworkTable.setStatus("current")
_Hh3cDHCPS6PoolNetworkEntry_Object = MibTableRow
hh3cDHCPS6PoolNetworkEntry = _Hh3cDHCPS6PoolNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 159, 1, 3, 1)
)
hh3cDHCPS6PoolNetworkEntry.setIndexNames(
    (0, "HH3C-DHCP6-SERVER-MIB", "hh3cDHCPS6PoolName"),
)
if mibBuilder.loadTexts:
    hh3cDHCPS6PoolNetworkEntry.setStatus("current")
_Hh3cDHCPS6PoolStartAddr_Type = InetAddressIPv6
_Hh3cDHCPS6PoolStartAddr_Object = MibTableColumn
hh3cDHCPS6PoolStartAddr = _Hh3cDHCPS6PoolStartAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 159, 1, 3, 1, 1),
    _Hh3cDHCPS6PoolStartAddr_Type()
)
hh3cDHCPS6PoolStartAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPS6PoolStartAddr.setStatus("current")
_Hh3cDHCPS6PoolStopAddr_Type = InetAddressIPv6
_Hh3cDHCPS6PoolStopAddr_Object = MibTableColumn
hh3cDHCPS6PoolStopAddr = _Hh3cDHCPS6PoolStopAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 159, 1, 3, 1, 2),
    _Hh3cDHCPS6PoolStopAddr_Type()
)
hh3cDHCPS6PoolStopAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPS6PoolStopAddr.setStatus("current")


class _Hh3cDHCPS6PoolNetPrefixLen_Type(Integer32):
    """Custom type hh3cDHCPS6PoolNetPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Hh3cDHCPS6PoolNetPrefixLen_Type.__name__ = "Integer32"
_Hh3cDHCPS6PoolNetPrefixLen_Object = MibTableColumn
hh3cDHCPS6PoolNetPrefixLen = _Hh3cDHCPS6PoolNetPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 159, 1, 3, 1, 3),
    _Hh3cDHCPS6PoolNetPrefixLen_Type()
)
hh3cDHCPS6PoolNetPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPS6PoolNetPrefixLen.setStatus("current")
_Hh3cDHCPS6PoolLeaseTime_Type = TimeTicks
_Hh3cDHCPS6PoolLeaseTime_Object = MibTableColumn
hh3cDHCPS6PoolLeaseTime = _Hh3cDHCPS6PoolLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 159, 1, 3, 1, 4),
    _Hh3cDHCPS6PoolLeaseTime_Type()
)
hh3cDHCPS6PoolLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPS6PoolLeaseTime.setStatus("current")
_Hh3cDHCPS6PoolStatTable_Object = MibTable
hh3cDHCPS6PoolStatTable = _Hh3cDHCPS6PoolStatTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 159, 1, 4)
)
if mibBuilder.loadTexts:
    hh3cDHCPS6PoolStatTable.setStatus("current")
_Hh3cDHCPS6PoolStatEntry_Object = MibTableRow
hh3cDHCPS6PoolStatEntry = _Hh3cDHCPS6PoolStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 159, 1, 4, 1)
)
hh3cDHCPS6PoolStatEntry.setIndexNames(
    (0, "HH3C-DHCP6-SERVER-MIB", "hh3cDHCPS6PoolName"),
)
if mibBuilder.loadTexts:
    hh3cDHCPS6PoolStatEntry.setStatus("current")
_Hh3cDHCPS6PoolIPPoolUsage_Type = Integer32
_Hh3cDHCPS6PoolIPPoolUsage_Object = MibTableColumn
hh3cDHCPS6PoolIPPoolUsage = _Hh3cDHCPS6PoolIPPoolUsage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 159, 1, 4, 1, 1),
    _Hh3cDHCPS6PoolIPPoolUsage_Type()
)
hh3cDHCPS6PoolIPPoolUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPS6PoolIPPoolUsage.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-DHCP6-SERVER-MIB",
    **{"hh3cDHCP6Server": hh3cDHCP6Server,
       "hh3cDHCP6ServerTables": hh3cDHCP6ServerTables,
       "hh3cDHCPS6PoolTable": hh3cDHCPS6PoolTable,
       "hh3cDHCPS6PoolEntry": hh3cDHCPS6PoolEntry,
       "hh3cDHCPS6PoolName": hh3cDHCPS6PoolName,
       "hh3cDHCPS6PoolRowStatus": hh3cDHCPS6PoolRowStatus,
       "hh3cDHCPS6PoolConfigTable": hh3cDHCPS6PoolConfigTable,
       "hh3cDHCPS6PoolConfigEntry": hh3cDHCPS6PoolConfigEntry,
       "hh3cDHCPS6PoolPrimaryDNSIP": hh3cDHCPS6PoolPrimaryDNSIP,
       "hh3cDHCPS6PoolSecondDNSIP": hh3cDHCPS6PoolSecondDNSIP,
       "hh3cDHCPS6PoolNetworkTable": hh3cDHCPS6PoolNetworkTable,
       "hh3cDHCPS6PoolNetworkEntry": hh3cDHCPS6PoolNetworkEntry,
       "hh3cDHCPS6PoolStartAddr": hh3cDHCPS6PoolStartAddr,
       "hh3cDHCPS6PoolStopAddr": hh3cDHCPS6PoolStopAddr,
       "hh3cDHCPS6PoolNetPrefixLen": hh3cDHCPS6PoolNetPrefixLen,
       "hh3cDHCPS6PoolLeaseTime": hh3cDHCPS6PoolLeaseTime,
       "hh3cDHCPS6PoolStatTable": hh3cDHCPS6PoolStatTable,
       "hh3cDHCPS6PoolStatEntry": hh3cDHCPS6PoolStatEntry,
       "hh3cDHCPS6PoolIPPoolUsage": hh3cDHCPS6PoolIPPoolUsage}
)
