# SNMP MIB module (UBQS-IP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ubiquoss\UBQS-IP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:33:19 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

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
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(ubiMgmtv2,) = mibBuilder.importSymbols(
    "UBQS-SMI",
    "ubiMgmtv2")


# MODULE-IDENTITY

ubiIpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UbiIpMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ubiIpMIBNotificationPrefix = _UbiIpMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 0)
)
_UbiIpMIBNotifications_ObjectIdentity = ObjectIdentity
ubiIpMIBNotifications = _UbiIpMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 0, 1)
)
_UbiPingMIBNotifications_ObjectIdentity = ObjectIdentity
ubiPingMIBNotifications = _UbiPingMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 0, 2)
)
_UbiIpMIBObjects_ObjectIdentity = ObjectIdentity
ubiIpMIBObjects = _UbiIpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 1)
)
_UbiIpAddrTable_Object = MibTable
ubiIpAddrTable = _UbiIpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 1, 1)
)
if mibBuilder.loadTexts:
    ubiIpAddrTable.setStatus("current")
_UbiIpAddrEntry_Object = MibTableRow
ubiIpAddrEntry = _UbiIpAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 1, 1, 1)
)
ubiIpAddrEntry.setIndexNames(
    (0, "UBQS-IP-MIB", "ubiIpAddrType"),
    (0, "UBQS-IP-MIB", "ubiIpAddress"),
    (0, "UBQS-IP-MIB", "ubiIpAddrPrefixLen"),
)
if mibBuilder.loadTexts:
    ubiIpAddrEntry.setStatus("current")
_UbiIpAddrType_Type = InetAddressType
_UbiIpAddrType_Object = MibTableColumn
ubiIpAddrType = _UbiIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 1, 1, 1, 1),
    _UbiIpAddrType_Type()
)
ubiIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiIpAddrType.setStatus("current")
_UbiIpAddress_Type = InetAddress
_UbiIpAddress_Object = MibTableColumn
ubiIpAddress = _UbiIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 1, 1, 1, 2),
    _UbiIpAddress_Type()
)
ubiIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiIpAddress.setStatus("current")
_UbiIpAddrPrefixLen_Type = InetAddressPrefixLength
_UbiIpAddrPrefixLen_Object = MibTableColumn
ubiIpAddrPrefixLen = _UbiIpAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 1, 1, 1, 3),
    _UbiIpAddrPrefixLen_Type()
)
ubiIpAddrPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiIpAddrPrefixLen.setStatus("current")
_UbiIpAddrIfIndex_Type = InterfaceIndex
_UbiIpAddrIfIndex_Object = MibTableColumn
ubiIpAddrIfIndex = _UbiIpAddrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 1, 1, 1, 4),
    _UbiIpAddrIfIndex_Type()
)
ubiIpAddrIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ubiIpAddrIfIndex.setStatus("current")


class _UbiIpAddrStatus_Type(Integer32):
    """Custom type ubiIpAddrStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_UbiIpAddrStatus_Type.__name__ = "Integer32"
_UbiIpAddrStatus_Object = MibTableColumn
ubiIpAddrStatus = _UbiIpAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 1, 1, 1, 5),
    _UbiIpAddrStatus_Type()
)
ubiIpAddrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ubiIpAddrStatus.setStatus("current")
_UbiIpAddrRowstatus_Type = RowStatus
_UbiIpAddrRowstatus_Object = MibTableColumn
ubiIpAddrRowstatus = _UbiIpAddrRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 1, 1, 1, 6),
    _UbiIpAddrRowstatus_Type()
)
ubiIpAddrRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ubiIpAddrRowstatus.setStatus("current")
_UbiInetRouteTable_Object = MibTable
ubiInetRouteTable = _UbiInetRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 1, 2)
)
if mibBuilder.loadTexts:
    ubiInetRouteTable.setStatus("current")
_UbiInetRouteEntry_Object = MibTableRow
ubiInetRouteEntry = _UbiInetRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 1, 2, 1)
)
ubiInetRouteEntry.setIndexNames(
    (0, "UBQS-IP-MIB", "ubiInetRouteInstance"),
    (0, "UBQS-IP-MIB", "ubiInetRouteDestType"),
    (0, "UBQS-IP-MIB", "ubiInetRouteDest"),
    (0, "UBQS-IP-MIB", "ubiInetRouteDestPfxLen"),
    (0, "UBQS-IP-MIB", "ubiInetRouteNextHopType"),
    (0, "UBQS-IP-MIB", "ubiInetRouteNextHop"),
    (0, "UBQS-IP-MIB", "ubiInetRouteIfIndex"),
)
if mibBuilder.loadTexts:
    ubiInetRouteEntry.setStatus("current")
_UbiInetRouteInstance_Type = Unsigned32
_UbiInetRouteInstance_Object = MibTableColumn
ubiInetRouteInstance = _UbiInetRouteInstance_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 1, 2, 1, 1),
    _UbiInetRouteInstance_Type()
)
ubiInetRouteInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiInetRouteInstance.setStatus("current")
_UbiInetRouteDestType_Type = InetAddressType
_UbiInetRouteDestType_Object = MibTableColumn
ubiInetRouteDestType = _UbiInetRouteDestType_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 1, 2, 1, 2),
    _UbiInetRouteDestType_Type()
)
ubiInetRouteDestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiInetRouteDestType.setStatus("current")
_UbiInetRouteDest_Type = InetAddress
_UbiInetRouteDest_Object = MibTableColumn
ubiInetRouteDest = _UbiInetRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 1, 2, 1, 3),
    _UbiInetRouteDest_Type()
)
ubiInetRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiInetRouteDest.setStatus("current")
_UbiInetRouteDestPfxLen_Type = InetAddressPrefixLength
_UbiInetRouteDestPfxLen_Object = MibTableColumn
ubiInetRouteDestPfxLen = _UbiInetRouteDestPfxLen_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 1, 2, 1, 4),
    _UbiInetRouteDestPfxLen_Type()
)
ubiInetRouteDestPfxLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiInetRouteDestPfxLen.setStatus("current")
_UbiInetRouteNextHopType_Type = InetAddressType
_UbiInetRouteNextHopType_Object = MibTableColumn
ubiInetRouteNextHopType = _UbiInetRouteNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 1, 2, 1, 5),
    _UbiInetRouteNextHopType_Type()
)
ubiInetRouteNextHopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiInetRouteNextHopType.setStatus("current")
_UbiInetRouteNextHop_Type = InetAddress
_UbiInetRouteNextHop_Object = MibTableColumn
ubiInetRouteNextHop = _UbiInetRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 1, 2, 1, 6),
    _UbiInetRouteNextHop_Type()
)
ubiInetRouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiInetRouteNextHop.setStatus("current")
_UbiInetRouteIfIndex_Type = InterfaceIndex
_UbiInetRouteIfIndex_Object = MibTableColumn
ubiInetRouteIfIndex = _UbiInetRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 1, 2, 1, 7),
    _UbiInetRouteIfIndex_Type()
)
ubiInetRouteIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiInetRouteIfIndex.setStatus("current")


class _UbiInetRoutetype_Type(Integer32):
    """Custom type ubiInetRoutetype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("invalid", 2),
          ("direct", 3),
          ("indirect", 4))
    )


_UbiInetRoutetype_Type.__name__ = "Integer32"
_UbiInetRoutetype_Object = MibTableColumn
ubiInetRoutetype = _UbiInetRoutetype_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 1, 2, 1, 8),
    _UbiInetRoutetype_Type()
)
ubiInetRoutetype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiInetRoutetype.setStatus("current")


class _UbiInetRouteProto_Type(Integer32):
    """Custom type ubiInetRouteProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("local", 2),
          ("netmgmt", 3),
          ("icmp", 4),
          ("egp", 5),
          ("ggp", 6),
          ("hello", 7),
          ("rip", 8),
          ("isis", 9),
          ("esis", 10),
          ("ciscoIgrp", 11),
          ("bbnSpfIgp", 12),
          ("ospf", 13),
          ("bgp", 14))
    )


_UbiInetRouteProto_Type.__name__ = "Integer32"
_UbiInetRouteProto_Object = MibTableColumn
ubiInetRouteProto = _UbiInetRouteProto_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 1, 2, 1, 9),
    _UbiInetRouteProto_Type()
)
ubiInetRouteProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiInetRouteProto.setStatus("current")
_UbiInetRouteMetric1_Type = Integer32
_UbiInetRouteMetric1_Object = MibTableColumn
ubiInetRouteMetric1 = _UbiInetRouteMetric1_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 1, 2, 1, 10),
    _UbiInetRouteMetric1_Type()
)
ubiInetRouteMetric1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiInetRouteMetric1.setStatus("current")
_UbiInetRouteMetric2_Type = Integer32
_UbiInetRouteMetric2_Object = MibTableColumn
ubiInetRouteMetric2 = _UbiInetRouteMetric2_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 1, 2, 1, 11),
    _UbiInetRouteMetric2_Type()
)
ubiInetRouteMetric2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiInetRouteMetric2.setStatus("current")
_UbiInetRouteMetric3_Type = Integer32
_UbiInetRouteMetric3_Object = MibTableColumn
ubiInetRouteMetric3 = _UbiInetRouteMetric3_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 1, 2, 1, 12),
    _UbiInetRouteMetric3_Type()
)
ubiInetRouteMetric3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiInetRouteMetric3.setStatus("current")
_UbiInetRouteMetric4_Type = Integer32
_UbiInetRouteMetric4_Object = MibTableColumn
ubiInetRouteMetric4 = _UbiInetRouteMetric4_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 1, 2, 1, 13),
    _UbiInetRouteMetric4_Type()
)
ubiInetRouteMetric4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiInetRouteMetric4.setStatus("current")
_UbiInetRouteMetric5_Type = Integer32
_UbiInetRouteMetric5_Object = MibTableColumn
ubiInetRouteMetric5 = _UbiInetRouteMetric5_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 1, 2, 1, 14),
    _UbiInetRouteMetric5_Type()
)
ubiInetRouteMetric5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiInetRouteMetric5.setStatus("current")


class _UbiInetRouteStatus_Type(Integer32):
    """Custom type ubiInetRouteStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_UbiInetRouteStatus_Type.__name__ = "Integer32"
_UbiInetRouteStatus_Object = MibTableColumn
ubiInetRouteStatus = _UbiInetRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 1, 2, 1, 15),
    _UbiInetRouteStatus_Type()
)
ubiInetRouteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiInetRouteStatus.setStatus("current")


class _UbiInetRouteDistance_Type(Integer32):
    """Custom type ubiInetRouteDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_UbiInetRouteDistance_Type.__name__ = "Integer32"
_UbiInetRouteDistance_Object = MibTableColumn
ubiInetRouteDistance = _UbiInetRouteDistance_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 1, 2, 1, 16),
    _UbiInetRouteDistance_Type()
)
ubiInetRouteDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiInetRouteDistance.setStatus("current")
_UbiInetRouteTag_Type = Unsigned32
_UbiInetRouteTag_Object = MibTableColumn
ubiInetRouteTag = _UbiInetRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 1, 2, 1, 17),
    _UbiInetRouteTag_Type()
)
ubiInetRouteTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiInetRouteTag.setStatus("current")
_UbiInetRouteNextHopName_Type = DisplayString
_UbiInetRouteNextHopName_Object = MibTableColumn
ubiInetRouteNextHopName = _UbiInetRouteNextHopName_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 1, 2, 1, 18),
    _UbiInetRouteNextHopName_Type()
)
ubiInetRouteNextHopName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiInetRouteNextHopName.setStatus("current")
_UbiInetRouteRowstatus_Type = RowStatus
_UbiInetRouteRowstatus_Object = MibTableColumn
ubiInetRouteRowstatus = _UbiInetRouteRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 1, 2, 1, 19),
    _UbiInetRouteRowstatus_Type()
)
ubiInetRouteRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ubiInetRouteRowstatus.setStatus("current")
_UbiIpv6NeighborTable_Object = MibTable
ubiIpv6NeighborTable = _UbiIpv6NeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 1, 3)
)
if mibBuilder.loadTexts:
    ubiIpv6NeighborTable.setStatus("current")
_UbiIpv6NeighborEntry_Object = MibTableRow
ubiIpv6NeighborEntry = _UbiIpv6NeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 1, 3, 1)
)
ubiIpv6NeighborEntry.setIndexNames(
    (0, "UBQS-IP-MIB", "ubiIpv6NeighborIfIndex"),
    (0, "UBQS-IP-MIB", "ubiIpv6NeighborNetAddress"),
)
if mibBuilder.loadTexts:
    ubiIpv6NeighborEntry.setStatus("current")
_UbiIpv6NeighborIfIndex_Type = InterfaceIndex
_UbiIpv6NeighborIfIndex_Object = MibTableColumn
ubiIpv6NeighborIfIndex = _UbiIpv6NeighborIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 1, 3, 1, 1),
    _UbiIpv6NeighborIfIndex_Type()
)
ubiIpv6NeighborIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiIpv6NeighborIfIndex.setStatus("current")


class _UbiIpv6NeighborPhysAddress_Type(PhysAddress):
    """Custom type ubiIpv6NeighborPhysAddress based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_UbiIpv6NeighborPhysAddress_Type.__name__ = "PhysAddress"
_UbiIpv6NeighborPhysAddress_Object = MibTableColumn
ubiIpv6NeighborPhysAddress = _UbiIpv6NeighborPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 1, 3, 1, 2),
    _UbiIpv6NeighborPhysAddress_Type()
)
ubiIpv6NeighborPhysAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ubiIpv6NeighborPhysAddress.setStatus("current")
_UbiIpv6NeighborNetAddress_Type = InetAddress
_UbiIpv6NeighborNetAddress_Object = MibTableColumn
ubiIpv6NeighborNetAddress = _UbiIpv6NeighborNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 1, 3, 1, 3),
    _UbiIpv6NeighborNetAddress_Type()
)
ubiIpv6NeighborNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiIpv6NeighborNetAddress.setStatus("current")


class _UbiIpv6NeighborType_Type(Integer32):
    """Custom type ubiIpv6NeighborType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 0),
          ("static", 1))
    )


_UbiIpv6NeighborType_Type.__name__ = "Integer32"
_UbiIpv6NeighborType_Object = MibTableColumn
ubiIpv6NeighborType = _UbiIpv6NeighborType_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 1, 3, 1, 4),
    _UbiIpv6NeighborType_Type()
)
ubiIpv6NeighborType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiIpv6NeighborType.setStatus("current")


class _UbiIpv6NeighborState_Type(Integer32):
    """Custom type ubiIpv6NeighborState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("reachable", 1),
          ("stale", 2),
          ("delay", 3),
          ("probe", 4),
          ("invalid", 5),
          ("unknown", 6),
          ("incomplete", 7))
    )


_UbiIpv6NeighborState_Type.__name__ = "Integer32"
_UbiIpv6NeighborState_Object = MibTableColumn
ubiIpv6NeighborState = _UbiIpv6NeighborState_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 1, 3, 1, 5),
    _UbiIpv6NeighborState_Type()
)
ubiIpv6NeighborState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiIpv6NeighborState.setStatus("current")
_UbiIpv6NeighborLastUpdated_Type = TimeStamp
_UbiIpv6NeighborLastUpdated_Object = MibTableColumn
ubiIpv6NeighborLastUpdated = _UbiIpv6NeighborLastUpdated_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 1, 3, 1, 6),
    _UbiIpv6NeighborLastUpdated_Type()
)
ubiIpv6NeighborLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiIpv6NeighborLastUpdated.setStatus("current")
_UbiIpv6NeighborRowstatus_Type = RowStatus
_UbiIpv6NeighborRowstatus_Object = MibTableColumn
ubiIpv6NeighborRowstatus = _UbiIpv6NeighborRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 1, 3, 1, 7),
    _UbiIpv6NeighborRowstatus_Type()
)
ubiIpv6NeighborRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ubiIpv6NeighborRowstatus.setStatus("current")
_UbiPingMIBObjects_ObjectIdentity = ObjectIdentity
ubiPingMIBObjects = _UbiPingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 2)
)
_UbiPingGlobal_ObjectIdentity = ObjectIdentity
ubiPingGlobal = _UbiPingGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 2, 1)
)
_UbiPingSend_ObjectIdentity = ObjectIdentity
ubiPingSend = _UbiPingSend_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 2, 2)
)


class _UbiPingSendProto_Type(Integer32):
    """Custom type ubiPingSendProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("ip", 2),
          ("ipv6", 3))
    )


_UbiPingSendProto_Type.__name__ = "Integer32"
_UbiPingSendProto_Object = MibScalar
ubiPingSendProto = _UbiPingSendProto_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 2, 2, 1),
    _UbiPingSendProto_Type()
)
ubiPingSendProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiPingSendProto.setStatus("current")
_UbiPingSendTarget_Type = DisplayString
_UbiPingSendTarget_Object = MibScalar
ubiPingSendTarget = _UbiPingSendTarget_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 2, 2, 2),
    _UbiPingSendTarget_Type()
)
ubiPingSendTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiPingSendTarget.setStatus("current")


class _UbiPingSendRepeat_Type(Integer32):
    """Custom type ubiPingSendRepeat based on Integer32"""
    defaultValue = 5


_UbiPingSendRepeat_Type.__name__ = "Integer32"
_UbiPingSendRepeat_Object = MibScalar
ubiPingSendRepeat = _UbiPingSendRepeat_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 2, 2, 3),
    _UbiPingSendRepeat_Type()
)
ubiPingSendRepeat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiPingSendRepeat.setStatus("current")


class _UbiPingSendPacketSize_Type(Integer32):
    """Custom type ubiPingSendPacketSize based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_UbiPingSendPacketSize_Type.__name__ = "Integer32"
_UbiPingSendPacketSize_Object = MibScalar
ubiPingSendPacketSize = _UbiPingSendPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 2, 2, 4),
    _UbiPingSendPacketSize_Type()
)
ubiPingSendPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiPingSendPacketSize.setStatus("current")


class _UbiPingSendTimeout_Type(Integer32):
    """Custom type ubiPingSendTimeout based on Integer32"""
    defaultValue = 2000


_UbiPingSendTimeout_Type.__name__ = "Integer32"
_UbiPingSendTimeout_Object = MibScalar
ubiPingSendTimeout = _UbiPingSendTimeout_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 2, 2, 5),
    _UbiPingSendTimeout_Type()
)
ubiPingSendTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiPingSendTimeout.setStatus("current")
if mibBuilder.loadTexts:
    ubiPingSendTimeout.setUnits("seconds")
_UbiPingSendInterval_Type = Integer32
_UbiPingSendInterval_Object = MibScalar
ubiPingSendInterval = _UbiPingSendInterval_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 2, 2, 6),
    _UbiPingSendInterval_Type()
)
ubiPingSendInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiPingSendInterval.setStatus("current")
if mibBuilder.loadTexts:
    ubiPingSendInterval.setUnits("seconds")
_UbiPingSendSrcAddr_Type = DisplayString
_UbiPingSendSrcAddr_Object = MibScalar
ubiPingSendSrcAddr = _UbiPingSendSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 2, 2, 7),
    _UbiPingSendSrcAddr_Type()
)
ubiPingSendSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiPingSendSrcAddr.setStatus("current")
_UbiPingSendTTL_Type = Integer32
_UbiPingSendTTL_Object = MibScalar
ubiPingSendTTL = _UbiPingSendTTL_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 2, 2, 8),
    _UbiPingSendTTL_Type()
)
ubiPingSendTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiPingSendTTL.setStatus("current")
_UbiPingSendTos_Type = Integer32
_UbiPingSendTos_Object = MibScalar
ubiPingSendTos = _UbiPingSendTos_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 2, 2, 9),
    _UbiPingSendTos_Type()
)
ubiPingSendTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiPingSendTos.setStatus("current")


class _UbiPingSendDF_Type(Integer32):
    """Custom type ubiPingSendDF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("do", 1),
          ("dont", 2))
    )


_UbiPingSendDF_Type.__name__ = "Integer32"
_UbiPingSendDF_Object = MibScalar
ubiPingSendDF = _UbiPingSendDF_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 2, 2, 10),
    _UbiPingSendDF_Type()
)
ubiPingSendDF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiPingSendDF.setStatus("current")


class _UbiPingSendExecute_Type(Integer32):
    """Custom type ubiPingSendExecute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("send", 1)
    )


_UbiPingSendExecute_Type.__name__ = "Integer32"
_UbiPingSendExecute_Object = MibScalar
ubiPingSendExecute = _UbiPingSendExecute_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 2, 2, 15),
    _UbiPingSendExecute_Type()
)
ubiPingSendExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiPingSendExecute.setStatus("current")
_UbiPingResults_ObjectIdentity = ObjectIdentity
ubiPingResults = _UbiPingResults_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 2, 3)
)
_UbiPingSendCompleted_Type = TruthValue
_UbiPingSendCompleted_Object = MibScalar
ubiPingSendCompleted = _UbiPingSendCompleted_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 2, 3, 1),
    _UbiPingSendCompleted_Type()
)
ubiPingSendCompleted.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ubiPingSendCompleted.setStatus("current")
_UbiPingSendPackets_Type = Counter32
_UbiPingSendPackets_Object = MibScalar
ubiPingSendPackets = _UbiPingSendPackets_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 2, 3, 2),
    _UbiPingSendPackets_Type()
)
ubiPingSendPackets.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ubiPingSendPackets.setStatus("current")
_UbiPingReceivedPackets_Type = Counter32
_UbiPingReceivedPackets_Object = MibScalar
ubiPingReceivedPackets = _UbiPingReceivedPackets_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 2, 3, 3),
    _UbiPingReceivedPackets_Type()
)
ubiPingReceivedPackets.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ubiPingReceivedPackets.setStatus("current")
_UbiIpMIBConformance_ObjectIdentity = ObjectIdentity
ubiIpMIBConformance = _UbiIpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 3)
)
_UbiIpMIBCompliances_ObjectIdentity = ObjectIdentity
ubiIpMIBCompliances = _UbiIpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 3, 1)
)
_UbiIpMIBGroups_ObjectIdentity = ObjectIdentity
ubiIpMIBGroups = _UbiIpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 3, 2)
)

# Managed Objects groups

ubiIpAddrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 3, 2, 1)
)
ubiIpAddrGroup.setObjects(
      *(("UBQS-IP-MIB", "ubiIpAddrType"),
        ("UBQS-IP-MIB", "ubiIpAddress"),
        ("UBQS-IP-MIB", "ubiIpAddrIfIndex"),
        ("UBQS-IP-MIB", "ubiIpAddrPrefixLen"),
        ("UBQS-IP-MIB", "ubiIpAddrStatus"),
        ("UBQS-IP-MIB", "ubiIpAddrRowstatus"))
)
if mibBuilder.loadTexts:
    ubiIpAddrGroup.setStatus("current")

ubiPingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 3, 2, 2)
)
ubiPingGroup.setObjects(
      *(("UBQS-IP-MIB", "ubiPingSendProto"),
        ("UBQS-IP-MIB", "ubiPingSendTarget"),
        ("UBQS-IP-MIB", "ubiPingSendRepeat"),
        ("UBQS-IP-MIB", "ubiPingSendPacketSize"),
        ("UBQS-IP-MIB", "ubiPingSendTimeout"),
        ("UBQS-IP-MIB", "ubiPingSendInterval"),
        ("UBQS-IP-MIB", "ubiPingSendSrcAddr"),
        ("UBQS-IP-MIB", "ubiPingSendTtl"),
        ("UBQS-IP-MIB", "ubiPingSendTos"),
        ("UBQS-IP-MIB", "ubiPingSendDF"),
        ("UBQS-IP-MIB", "ubiPingSendExecute"),
        ("UBQS-IP-MIB", "ubiPingSendCompleted"),
        ("UBQS-IP-MIB", "ubiPingSendPackets"),
        ("UBQS-IP-MIB", "ubiPingReceivedPackets"))
)
if mibBuilder.loadTexts:
    ubiPingGroup.setStatus("current")


# Notification objects

ubiPingSendCompletion = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 0, 2, 1)
)
ubiPingSendCompletion.setObjects(
      *(("UBQS-IP-MIB", "ubiPingSendCompleted"),
        ("UBQS-IP-MIB", "ubiPingSendPackets"),
        ("UBQS-IP-MIB", "ubiPingReceivedPackets"))
)
if mibBuilder.loadTexts:
    ubiPingSendCompletion.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

ubiIpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7800, 100, 14, 3, 1, 2)
)
ubiIpMIBCompliance.setObjects(
      *(("UBQS-IP-MIB", "ubiIpAddrGroup"),
        ("UBQS-IP-MIB", "ubiPingGroup"),
        ("UBQS-IP-MIB", "ubiIpAddrGroup"),
        ("UBQS-IP-MIB", "ubiPingGroup"))
)
if mibBuilder.loadTexts:
    ubiIpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UBQS-IP-MIB",
    **{"ubiIpMIB": ubiIpMIB,
       "ubiIpMIBNotificationPrefix": ubiIpMIBNotificationPrefix,
       "ubiIpMIBNotifications": ubiIpMIBNotifications,
       "ubiPingMIBNotifications": ubiPingMIBNotifications,
       "ubiPingSendCompletion": ubiPingSendCompletion,
       "ubiIpMIBObjects": ubiIpMIBObjects,
       "ubiIpAddrTable": ubiIpAddrTable,
       "ubiIpAddrEntry": ubiIpAddrEntry,
       "ubiIpAddrType": ubiIpAddrType,
       "ubiIpAddress": ubiIpAddress,
       "ubiIpAddrPrefixLen": ubiIpAddrPrefixLen,
       "ubiIpAddrIfIndex": ubiIpAddrIfIndex,
       "ubiIpAddrStatus": ubiIpAddrStatus,
       "ubiIpAddrRowstatus": ubiIpAddrRowstatus,
       "ubiInetRouteTable": ubiInetRouteTable,
       "ubiInetRouteEntry": ubiInetRouteEntry,
       "ubiInetRouteInstance": ubiInetRouteInstance,
       "ubiInetRouteDestType": ubiInetRouteDestType,
       "ubiInetRouteDest": ubiInetRouteDest,
       "ubiInetRouteDestPfxLen": ubiInetRouteDestPfxLen,
       "ubiInetRouteNextHopType": ubiInetRouteNextHopType,
       "ubiInetRouteNextHop": ubiInetRouteNextHop,
       "ubiInetRouteIfIndex": ubiInetRouteIfIndex,
       "ubiInetRoutetype": ubiInetRoutetype,
       "ubiInetRouteProto": ubiInetRouteProto,
       "ubiInetRouteMetric1": ubiInetRouteMetric1,
       "ubiInetRouteMetric2": ubiInetRouteMetric2,
       "ubiInetRouteMetric3": ubiInetRouteMetric3,
       "ubiInetRouteMetric4": ubiInetRouteMetric4,
       "ubiInetRouteMetric5": ubiInetRouteMetric5,
       "ubiInetRouteStatus": ubiInetRouteStatus,
       "ubiInetRouteDistance": ubiInetRouteDistance,
       "ubiInetRouteTag": ubiInetRouteTag,
       "ubiInetRouteNextHopName": ubiInetRouteNextHopName,
       "ubiInetRouteRowstatus": ubiInetRouteRowstatus,
       "ubiIpv6NeighborTable": ubiIpv6NeighborTable,
       "ubiIpv6NeighborEntry": ubiIpv6NeighborEntry,
       "ubiIpv6NeighborIfIndex": ubiIpv6NeighborIfIndex,
       "ubiIpv6NeighborPhysAddress": ubiIpv6NeighborPhysAddress,
       "ubiIpv6NeighborNetAddress": ubiIpv6NeighborNetAddress,
       "ubiIpv6NeighborType": ubiIpv6NeighborType,
       "ubiIpv6NeighborState": ubiIpv6NeighborState,
       "ubiIpv6NeighborLastUpdated": ubiIpv6NeighborLastUpdated,
       "ubiIpv6NeighborRowstatus": ubiIpv6NeighborRowstatus,
       "ubiPingMIBObjects": ubiPingMIBObjects,
       "ubiPingGlobal": ubiPingGlobal,
       "ubiPingSend": ubiPingSend,
       "ubiPingSendProto": ubiPingSendProto,
       "ubiPingSendTarget": ubiPingSendTarget,
       "ubiPingSendRepeat": ubiPingSendRepeat,
       "ubiPingSendPacketSize": ubiPingSendPacketSize,
       "ubiPingSendTimeout": ubiPingSendTimeout,
       "ubiPingSendInterval": ubiPingSendInterval,
       "ubiPingSendSrcAddr": ubiPingSendSrcAddr,
       "ubiPingSendTTL": ubiPingSendTTL,
       "ubiPingSendTos": ubiPingSendTos,
       "ubiPingSendDF": ubiPingSendDF,
       "ubiPingSendExecute": ubiPingSendExecute,
       "ubiPingResults": ubiPingResults,
       "ubiPingSendCompleted": ubiPingSendCompleted,
       "ubiPingSendPackets": ubiPingSendPackets,
       "ubiPingReceivedPackets": ubiPingReceivedPackets,
       "ubiIpMIBConformance": ubiIpMIBConformance,
       "ubiIpMIBCompliances": ubiIpMIBCompliances,
       "ubiIpMIBCompliance": ubiIpMIBCompliance,
       "ubiIpMIBGroups": ubiIpMIBGroups,
       "ubiIpAddrGroup": ubiIpAddrGroup,
       "ubiPingGroup": ubiPingGroup}
)
