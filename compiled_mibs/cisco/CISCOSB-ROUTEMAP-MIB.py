# SNMP MIB module (CISCOSB-ROUTEMAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cisco\CISCOSB-ROUTEMAP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:29:09 2025
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

(switch001,) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "switch001")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressIPv6,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv6",
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

rlRouteMap = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 227)
)
if mibBuilder.loadTexts:
    rlRouteMap.setRevisions(
        ("1970-01-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RlRouteMapInetType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )



# MIB Managed Objects in the order of their OIDs

_RlRouteMapPbrTable_Object = MibTable
rlRouteMapPbrTable = _RlRouteMapPbrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 227, 1)
)
if mibBuilder.loadTexts:
    rlRouteMapPbrTable.setStatus("current")
_RlRouteMapPbrEntry_Object = MibTableRow
rlRouteMapPbrEntry = _RlRouteMapPbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 227, 1, 1)
)
rlRouteMapPbrEntry.setIndexNames(
    (0, "CISCOSB-ROUTEMAP-MIB", "rlRouteMapPbrRouteMapName"),
    (0, "CISCOSB-ROUTEMAP-MIB", "rlRouteMapPbrRouteMapSectionId"),
    (0, "CISCOSB-ROUTEMAP-MIB", "rlRouteMapPbrInetType"),
)
if mibBuilder.loadTexts:
    rlRouteMapPbrEntry.setStatus("current")


class _RlRouteMapPbrRouteMapName_Type(DisplayString):
    """Custom type rlRouteMapPbrRouteMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlRouteMapPbrRouteMapName_Type.__name__ = "DisplayString"
_RlRouteMapPbrRouteMapName_Object = MibTableColumn
rlRouteMapPbrRouteMapName = _RlRouteMapPbrRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 227, 1, 1, 1),
    _RlRouteMapPbrRouteMapName_Type()
)
rlRouteMapPbrRouteMapName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlRouteMapPbrRouteMapName.setStatus("current")


class _RlRouteMapPbrRouteMapSectionId_Type(Unsigned32):
    """Custom type rlRouteMapPbrRouteMapSectionId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RlRouteMapPbrRouteMapSectionId_Type.__name__ = "Unsigned32"
_RlRouteMapPbrRouteMapSectionId_Object = MibTableColumn
rlRouteMapPbrRouteMapSectionId = _RlRouteMapPbrRouteMapSectionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 227, 1, 1, 2),
    _RlRouteMapPbrRouteMapSectionId_Type()
)
rlRouteMapPbrRouteMapSectionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlRouteMapPbrRouteMapSectionId.setStatus("current")
_RlRouteMapPbrInetType_Type = RlRouteMapInetType
_RlRouteMapPbrInetType_Object = MibTableColumn
rlRouteMapPbrInetType = _RlRouteMapPbrInetType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 227, 1, 1, 3),
    _RlRouteMapPbrInetType_Type()
)
rlRouteMapPbrInetType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRouteMapPbrInetType.setStatus("current")


class _RlRouteMapPbrMatchAccessListName_Type(DisplayString):
    """Custom type rlRouteMapPbrMatchAccessListName based on DisplayString"""
    defaultValue = OctetString("")


_RlRouteMapPbrMatchAccessListName_Type.__name__ = "DisplayString"
_RlRouteMapPbrMatchAccessListName_Object = MibTableColumn
rlRouteMapPbrMatchAccessListName = _RlRouteMapPbrMatchAccessListName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 227, 1, 1, 4),
    _RlRouteMapPbrMatchAccessListName_Type()
)
rlRouteMapPbrMatchAccessListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRouteMapPbrMatchAccessListName.setStatus("current")
_RlRouteMapPbrActionNexthopInetAddressType_Type = InetAddressType
_RlRouteMapPbrActionNexthopInetAddressType_Object = MibTableColumn
rlRouteMapPbrActionNexthopInetAddressType = _RlRouteMapPbrActionNexthopInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 227, 1, 1, 5),
    _RlRouteMapPbrActionNexthopInetAddressType_Type()
)
rlRouteMapPbrActionNexthopInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRouteMapPbrActionNexthopInetAddressType.setStatus("current")
_RlRouteMapPbrActionNexthopInetAddress_Type = InetAddress
_RlRouteMapPbrActionNexthopInetAddress_Object = MibTableColumn
rlRouteMapPbrActionNexthopInetAddress = _RlRouteMapPbrActionNexthopInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 227, 1, 1, 6),
    _RlRouteMapPbrActionNexthopInetAddress_Type()
)
rlRouteMapPbrActionNexthopInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRouteMapPbrActionNexthopInetAddress.setStatus("current")
_RlRouteMapPbrActionNexthopIfIndex_Type = InterfaceIndexOrZero
_RlRouteMapPbrActionNexthopIfIndex_Object = MibTableColumn
rlRouteMapPbrActionNexthopIfIndex = _RlRouteMapPbrActionNexthopIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 227, 1, 1, 7),
    _RlRouteMapPbrActionNexthopIfIndex_Type()
)
rlRouteMapPbrActionNexthopIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRouteMapPbrActionNexthopIfIndex.setStatus("current")
_RlRouteMapPbrRowStatus_Type = RowStatus
_RlRouteMapPbrRowStatus_Object = MibTableColumn
rlRouteMapPbrRowStatus = _RlRouteMapPbrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 227, 1, 1, 8),
    _RlRouteMapPbrRowStatus_Type()
)
rlRouteMapPbrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRouteMapPbrRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-ROUTEMAP-MIB",
    **{"RlRouteMapInetType": RlRouteMapInetType,
       "rlRouteMap": rlRouteMap,
       "rlRouteMapPbrTable": rlRouteMapPbrTable,
       "rlRouteMapPbrEntry": rlRouteMapPbrEntry,
       "rlRouteMapPbrRouteMapName": rlRouteMapPbrRouteMapName,
       "rlRouteMapPbrRouteMapSectionId": rlRouteMapPbrRouteMapSectionId,
       "rlRouteMapPbrInetType": rlRouteMapPbrInetType,
       "rlRouteMapPbrMatchAccessListName": rlRouteMapPbrMatchAccessListName,
       "rlRouteMapPbrActionNexthopInetAddressType": rlRouteMapPbrActionNexthopInetAddressType,
       "rlRouteMapPbrActionNexthopInetAddress": rlRouteMapPbrActionNexthopInetAddress,
       "rlRouteMapPbrActionNexthopIfIndex": rlRouteMapPbrActionNexthopIfIndex,
       "rlRouteMapPbrRowStatus": rlRouteMapPbrRowStatus}
)
