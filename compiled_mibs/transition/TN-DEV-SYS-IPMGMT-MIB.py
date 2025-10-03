# SNMP MIB module (TN-DEV-SYS-IPMGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TN-DEV-SYS-IPMGMT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:31:00 2025
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

(ModuleIdentity,
 ObjectIdentity,
 entPhysicalIndex) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "ModuleIdentity",
    "ObjectIdentity",
    "entPhysicalIndex")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(IpAddressOriginTC,) = mibBuilder.importSymbols(
    "IP-MIB",
    "IpAddressOriginTC")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(tnProducts,) = mibBuilder.importSymbols(
    "TRANSITION-SMI",
    "tnProducts")


# MODULE-IDENTITY

tnDevSysIpMgmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10)
)
if mibBuilder.loadTexts:
    tnDevSysIpMgmtMIB.setRevisions(
        ("2012-08-07 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnDevSysIpmgmt_ObjectIdentity = ObjectIdentity
tnDevSysIpmgmt = _TnDevSysIpmgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1)
)
_TnIpMgmtTable_Object = MibTable
tnIpMgmtTable = _TnIpMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 1)
)
if mibBuilder.loadTexts:
    tnIpMgmtTable.setStatus("current")
_TnIpMgmtEntry_Object = MibTableRow
tnIpMgmtEntry = _TnIpMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 1, 1)
)
tnIpMgmtEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    tnIpMgmtEntry.setStatus("current")


class _TnIpAddressMode_Type(Integer32):
    """Custom type tnIpAddressMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("dhcp", 1),
          ("static", 2),
          ("bootpc", 3))
    )


_TnIpAddressMode_Type.__name__ = "Integer32"
_TnIpAddressMode_Object = MibTableColumn
tnIpAddressMode = _TnIpAddressMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 1, 1, 1),
    _TnIpAddressMode_Type()
)
tnIpAddressMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIpAddressMode.setStatus("current")


class _TnIpMgmtAccess_Type(Integer32):
    """Custom type tnIpMgmtAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("enabled", 1),
          ("disabled", 2))
    )


_TnIpMgmtAccess_Type.__name__ = "Integer32"
_TnIpMgmtAccess_Object = MibTableColumn
tnIpMgmtAccess = _TnIpMgmtAccess_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 1, 1, 2),
    _TnIpMgmtAccess_Type()
)
tnIpMgmtAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIpMgmtAccess.setStatus("current")
_TnIpAddrType_Type = InetAddressType
_TnIpAddrType_Object = MibTableColumn
tnIpAddrType = _TnIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 1, 1, 3),
    _TnIpAddrType_Type()
)
tnIpAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIpAddrType.setStatus("current")
_TnIpAddr_Type = InetAddress
_TnIpAddr_Object = MibTableColumn
tnIpAddr = _TnIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 1, 1, 4),
    _TnIpAddr_Type()
)
tnIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIpAddr.setStatus("current")
_TnSubnetMask_Type = InetAddress
_TnSubnetMask_Object = MibTableColumn
tnSubnetMask = _TnSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 1, 1, 5),
    _TnSubnetMask_Type()
)
tnSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSubnetMask.setStatus("current")
_TnDefaultGateway_Type = InetAddress
_TnDefaultGateway_Object = MibTableColumn
tnDefaultGateway = _TnDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 1, 1, 6),
    _TnDefaultGateway_Type()
)
tnDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDefaultGateway.setStatus("current")
_TnDnsServerTable_Object = MibTable
tnDnsServerTable = _TnDnsServerTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 2)
)
if mibBuilder.loadTexts:
    tnDnsServerTable.setStatus("current")
_TnDnsServerEntry_Object = MibTableRow
tnDnsServerEntry = _TnDnsServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 2, 1)
)
tnDnsServerEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "TN-DEV-SYS-IPMGMT-MIB", "tnDnsServerIndex"),
)
if mibBuilder.loadTexts:
    tnDnsServerEntry.setStatus("current")
_TnDnsServerIndex_Type = Integer32
_TnDnsServerIndex_Object = MibTableColumn
tnDnsServerIndex = _TnDnsServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 2, 1, 1),
    _TnDnsServerIndex_Type()
)
tnDnsServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDnsServerIndex.setStatus("current")
_TnDnsServerIPAddrType_Type = InetAddressType
_TnDnsServerIPAddrType_Object = MibTableColumn
tnDnsServerIPAddrType = _TnDnsServerIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 2, 1, 2),
    _TnDnsServerIPAddrType_Type()
)
tnDnsServerIPAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDnsServerIPAddrType.setStatus("current")
_TnDnsServerIPAddr_Type = InetAddress
_TnDnsServerIPAddr_Object = MibTableColumn
tnDnsServerIPAddr = _TnDnsServerIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 2, 1, 3),
    _TnDnsServerIPAddr_Type()
)
tnDnsServerIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDnsServerIPAddr.setStatus("current")
_TnDnsServerStatus_Type = RowStatus
_TnDnsServerStatus_Object = MibTableColumn
tnDnsServerStatus = _TnDnsServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 2, 1, 4),
    _TnDnsServerStatus_Type()
)
tnDnsServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDnsServerStatus.setStatus("current")
_TnIpextMgmtTable_Object = MibTable
tnIpextMgmtTable = _TnIpextMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 3)
)
if mibBuilder.loadTexts:
    tnIpextMgmtTable.setStatus("current")
_TnIpextMgmtEntry_Object = MibTableRow
tnIpextMgmtEntry = _TnIpextMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 3, 1)
)
tnIpextMgmtEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    tnIpextMgmtEntry.setStatus("current")


class _TnIpv6status_Type(Integer32):
    """Custom type tnIpv6status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TnIpv6status_Type.__name__ = "Integer32"
_TnIpv6status_Object = MibTableColumn
tnIpv6status = _TnIpv6status_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 3, 1, 1),
    _TnIpv6status_Type()
)
tnIpv6status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIpv6status.setStatus("current")
_TnIpv6AddressLinklocal_Type = InetAddress
_TnIpv6AddressLinklocal_Object = MibTableColumn
tnIpv6AddressLinklocal = _TnIpv6AddressLinklocal_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 3, 1, 2),
    _TnIpv6AddressLinklocal_Type()
)
tnIpv6AddressLinklocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIpv6AddressLinklocal.setStatus("current")


class _TnIpv6Method_Type(Integer32):
    """Custom type tnIpv6Method based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dhcpv6", 2),
          ("stateless", 3))
    )


_TnIpv6Method_Type.__name__ = "Integer32"
_TnIpv6Method_Object = MibTableColumn
tnIpv6Method = _TnIpv6Method_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 3, 1, 3),
    _TnIpv6Method_Type()
)
tnIpv6Method.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIpv6Method.setStatus("current")
_TnIpv6Addr_Type = InetAddress
_TnIpv6Addr_Object = MibTableColumn
tnIpv6Addr = _TnIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 3, 1, 4),
    _TnIpv6Addr_Type()
)
tnIpv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIpv6Addr.setStatus("current")


class _TnIpv6prefix_Type(Integer32):
    """Custom type tnIpv6prefix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_TnIpv6prefix_Type.__name__ = "Integer32"
_TnIpv6prefix_Object = MibTableColumn
tnIpv6prefix = _TnIpv6prefix_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 3, 1, 5),
    _TnIpv6prefix_Type()
)
tnIpv6prefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIpv6prefix.setStatus("current")


class _TnIpv6DupAddrDetected_Type(Integer32):
    """Custom type tnIpv6DupAddrDetected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_TnIpv6DupAddrDetected_Type.__name__ = "Integer32"
_TnIpv6DupAddrDetected_Object = MibTableColumn
tnIpv6DupAddrDetected = _TnIpv6DupAddrDetected_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 3, 1, 6),
    _TnIpv6DupAddrDetected_Type()
)
tnIpv6DupAddrDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIpv6DupAddrDetected.setStatus("current")


class _TnIpv6GwMethod_Type(Integer32):
    """Custom type tnIpv6GwMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("routeDisc", 2))
    )


_TnIpv6GwMethod_Type.__name__ = "Integer32"
_TnIpv6GwMethod_Object = MibTableColumn
tnIpv6GwMethod = _TnIpv6GwMethod_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 3, 1, 7),
    _TnIpv6GwMethod_Type()
)
tnIpv6GwMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIpv6GwMethod.setStatus("current")
_TnIpv6defaultGW_Type = InetAddress
_TnIpv6defaultGW_Object = MibTableColumn
tnIpv6defaultGW = _TnIpv6defaultGW_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 3, 1, 8),
    _TnIpv6defaultGW_Type()
)
tnIpv6defaultGW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIpv6defaultGW.setStatus("current")
_TnIpv6DynRouteTable_Object = MibTable
tnIpv6DynRouteTable = _TnIpv6DynRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 4)
)
if mibBuilder.loadTexts:
    tnIpv6DynRouteTable.setStatus("current")
_TnIpv6DynRouteEntry_Object = MibTableRow
tnIpv6DynRouteEntry = _TnIpv6DynRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 4, 1)
)
tnIpv6DynRouteEntry.setIndexNames(
    (0, "TN-DEV-SYS-IPMGMT-MIB", "tnIpv6DynRouteIndex"),
)
if mibBuilder.loadTexts:
    tnIpv6DynRouteEntry.setStatus("current")
_TnIpv6DynRouteIndex_Type = Gauge32
_TnIpv6DynRouteIndex_Object = MibTableColumn
tnIpv6DynRouteIndex = _TnIpv6DynRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 4, 1, 1),
    _TnIpv6DynRouteIndex_Type()
)
tnIpv6DynRouteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnIpv6DynRouteIndex.setStatus("current")
_TnIpv6DynRouteDest_Type = InetAddress
_TnIpv6DynRouteDest_Object = MibTableColumn
tnIpv6DynRouteDest = _TnIpv6DynRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 4, 1, 2),
    _TnIpv6DynRouteDest_Type()
)
tnIpv6DynRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIpv6DynRouteDest.setStatus("current")
_TnIpv6DynRoutePfxLen_Type = Gauge32
_TnIpv6DynRoutePfxLen_Object = MibTableColumn
tnIpv6DynRoutePfxLen = _TnIpv6DynRoutePfxLen_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 4, 1, 3),
    _TnIpv6DynRoutePfxLen_Type()
)
tnIpv6DynRoutePfxLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIpv6DynRoutePfxLen.setStatus("current")
_TnIpv6DynRouteNextHop_Type = InetAddress
_TnIpv6DynRouteNextHop_Object = MibTableColumn
tnIpv6DynRouteNextHop = _TnIpv6DynRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 4, 1, 4),
    _TnIpv6DynRouteNextHop_Type()
)
tnIpv6DynRouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIpv6DynRouteNextHop.setStatus("current")
_TnIpv6DynRouteAge_Type = Gauge32
_TnIpv6DynRouteAge_Object = MibTableColumn
tnIpv6DynRouteAge = _TnIpv6DynRouteAge_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 4, 1, 5),
    _TnIpv6DynRouteAge_Type()
)
tnIpv6DynRouteAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIpv6DynRouteAge.setStatus("current")
_TnHostToIpTable_Object = MibTable
tnHostToIpTable = _TnHostToIpTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 7)
)
if mibBuilder.loadTexts:
    tnHostToIpTable.setStatus("current")
_TnHostToIpEntry_Object = MibTableRow
tnHostToIpEntry = _TnHostToIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 7, 1)
)
tnHostToIpEntry.setIndexNames(
    (0, "TN-DEV-SYS-IPMGMT-MIB", "tnHostToIpIndex"),
)
if mibBuilder.loadTexts:
    tnHostToIpEntry.setStatus("current")
_TnHostToIpIndex_Type = Integer32
_TnHostToIpIndex_Object = MibTableColumn
tnHostToIpIndex = _TnHostToIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 7, 1, 1),
    _TnHostToIpIndex_Type()
)
tnHostToIpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnHostToIpIndex.setStatus("current")
_TnHostIPAddrType_Type = InetAddressType
_TnHostIPAddrType_Object = MibTableColumn
tnHostIPAddrType = _TnHostIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 7, 1, 2),
    _TnHostIPAddrType_Type()
)
tnHostIPAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnHostIPAddrType.setStatus("current")
_TnHostIPAddr_Type = InetAddress
_TnHostIPAddr_Object = MibTableColumn
tnHostIPAddr = _TnHostIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 7, 1, 3),
    _TnHostIPAddr_Type()
)
tnHostIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnHostIPAddr.setStatus("current")


class _TnHostName_Type(DisplayString):
    """Custom type tnHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_TnHostName_Type.__name__ = "DisplayString"
_TnHostName_Object = MibTableColumn
tnHostName = _TnHostName_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 7, 1, 4),
    _TnHostName_Type()
)
tnHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnHostName.setStatus("current")


class _TnAliasName_Type(DisplayString):
    """Custom type tnAliasName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnAliasName_Type.__name__ = "DisplayString"
_TnAliasName_Object = MibTableColumn
tnAliasName = _TnAliasName_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 7, 1, 5),
    _TnAliasName_Type()
)
tnAliasName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAliasName.setStatus("current")
_TnEntryStatus_Type = RowStatus
_TnEntryStatus_Object = MibTableColumn
tnEntryStatus = _TnEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 7, 1, 6),
    _TnEntryStatus_Type()
)
tnEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEntryStatus.setStatus("current")
_TnIPv4MgmtTable_Object = MibTable
tnIPv4MgmtTable = _TnIPv4MgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 8)
)
if mibBuilder.loadTexts:
    tnIPv4MgmtTable.setStatus("current")
_TnIPv4MgmtEntry_Object = MibTableRow
tnIPv4MgmtEntry = _TnIPv4MgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 8, 1)
)
tnIPv4MgmtEntry.setIndexNames(
    (0, "TN-DEV-SYS-IPMGMT-MIB", "tnIpv4Interface"),
    (0, "TN-DEV-SYS-IPMGMT-MIB", "tnIPv4Index"),
)
if mibBuilder.loadTexts:
    tnIPv4MgmtEntry.setStatus("current")
_TnIpv4Interface_Type = InterfaceIndex
_TnIpv4Interface_Object = MibTableColumn
tnIpv4Interface = _TnIpv4Interface_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 8, 1, 1),
    _TnIpv4Interface_Type()
)
tnIpv4Interface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIpv4Interface.setStatus("current")
_TnIPv4Index_Type = Integer32
_TnIPv4Index_Object = MibTableColumn
tnIPv4Index = _TnIPv4Index_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 8, 1, 2),
    _TnIPv4Index_Type()
)
tnIPv4Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIPv4Index.setStatus("current")


class _TnIPv4ConfigMode_Type(Integer32):
    """Custom type tnIPv4ConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 1),
          ("static", 2))
    )


_TnIPv4ConfigMode_Type.__name__ = "Integer32"
_TnIPv4ConfigMode_Object = MibTableColumn
tnIPv4ConfigMode = _TnIPv4ConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 8, 1, 3),
    _TnIPv4ConfigMode_Type()
)
tnIPv4ConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIPv4ConfigMode.setStatus("current")
_TnIPv4Origin_Type = IpAddressOriginTC
_TnIPv4Origin_Object = MibTableColumn
tnIPv4Origin = _TnIPv4Origin_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 8, 1, 4),
    _TnIPv4Origin_Type()
)
tnIPv4Origin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIPv4Origin.setStatus("current")
_TnIPv4AddrType_Type = InetAddressType
_TnIPv4AddrType_Object = MibTableColumn
tnIPv4AddrType = _TnIPv4AddrType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 8, 1, 5),
    _TnIPv4AddrType_Type()
)
tnIPv4AddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIPv4AddrType.setStatus("current")
_TnIPv4Addr_Type = InetAddress
_TnIPv4Addr_Object = MibTableColumn
tnIPv4Addr = _TnIPv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 8, 1, 6),
    _TnIPv4Addr_Type()
)
tnIPv4Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIPv4Addr.setStatus("current")
_TnIPv4SubnetMask_Type = InetAddress
_TnIPv4SubnetMask_Object = MibTableColumn
tnIPv4SubnetMask = _TnIPv4SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 8, 1, 7),
    _TnIPv4SubnetMask_Type()
)
tnIPv4SubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIPv4SubnetMask.setStatus("current")
_TnIPv4DefaultGateway_Type = InetAddress
_TnIPv4DefaultGateway_Object = MibTableColumn
tnIPv4DefaultGateway = _TnIPv4DefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 8, 1, 8),
    _TnIPv4DefaultGateway_Type()
)
tnIPv4DefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIPv4DefaultGateway.setStatus("current")


class _TnIPv4Status_Type(Integer32):
    """Custom type tnIPv4Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("disabled", 2),
          ("renew", 3))
    )


_TnIPv4Status_Type.__name__ = "Integer32"
_TnIPv4Status_Object = MibTableColumn
tnIPv4Status = _TnIPv4Status_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 8, 1, 9),
    _TnIPv4Status_Type()
)
tnIPv4Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIPv4Status.setStatus("current")
_TnIPv6MgmtTable_Object = MibTable
tnIPv6MgmtTable = _TnIPv6MgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 9)
)
if mibBuilder.loadTexts:
    tnIPv6MgmtTable.setStatus("current")
_TnIPv6MgmtEntry_Object = MibTableRow
tnIPv6MgmtEntry = _TnIPv6MgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 9, 1)
)
tnIPv6MgmtEntry.setIndexNames(
    (0, "TN-DEV-SYS-IPMGMT-MIB", "tnIpv6Interface"),
    (0, "TN-DEV-SYS-IPMGMT-MIB", "tnIPv6Index"),
)
if mibBuilder.loadTexts:
    tnIPv6MgmtEntry.setStatus("current")
_TnIpv6Interface_Type = InterfaceIndex
_TnIpv6Interface_Object = MibTableColumn
tnIpv6Interface = _TnIpv6Interface_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 9, 1, 1),
    _TnIpv6Interface_Type()
)
tnIpv6Interface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIpv6Interface.setStatus("current")
_TnIPv6Index_Type = Integer32
_TnIPv6Index_Object = MibTableColumn
tnIPv6Index = _TnIPv6Index_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 9, 1, 2),
    _TnIPv6Index_Type()
)
tnIPv6Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIPv6Index.setStatus("current")
_TnIPv6Origin_Type = IpAddressOriginTC
_TnIPv6Origin_Object = MibTableColumn
tnIPv6Origin = _TnIPv6Origin_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 9, 1, 3),
    _TnIPv6Origin_Type()
)
tnIPv6Origin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIPv6Origin.setStatus("current")


class _TnIPv6CfgMethod_Type(Integer32):
    """Custom type tnIPv6CfgMethod based on Integer32"""
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
        *(("link-local", 1),
          ("stateless", 2),
          ("auto", 3),
          ("manual", 4))
    )


_TnIPv6CfgMethod_Type.__name__ = "Integer32"
_TnIPv6CfgMethod_Object = MibTableColumn
tnIPv6CfgMethod = _TnIPv6CfgMethod_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 9, 1, 4),
    _TnIPv6CfgMethod_Type()
)
tnIPv6CfgMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIPv6CfgMethod.setStatus("current")


class _TnIPv6AddressType_Type(Integer32):
    """Custom type tnIPv6AddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("anycast", 1),
          ("unicast", 2),
          ("multicast", 3))
    )


_TnIPv6AddressType_Type.__name__ = "Integer32"
_TnIPv6AddressType_Object = MibTableColumn
tnIPv6AddressType = _TnIPv6AddressType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 9, 1, 5),
    _TnIPv6AddressType_Type()
)
tnIPv6AddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIPv6AddressType.setStatus("current")
_TnIPv6Prefix_Type = InetAddress
_TnIPv6Prefix_Object = MibTableColumn
tnIPv6Prefix = _TnIPv6Prefix_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 9, 1, 6),
    _TnIPv6Prefix_Type()
)
tnIPv6Prefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIPv6Prefix.setStatus("current")


class _TnIPv6PrefixLen_Type(Integer32):
    """Custom type tnIPv6PrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_TnIPv6PrefixLen_Type.__name__ = "Integer32"
_TnIPv6PrefixLen_Object = MibTableColumn
tnIPv6PrefixLen = _TnIPv6PrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 9, 1, 7),
    _TnIPv6PrefixLen_Type()
)
tnIPv6PrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIPv6PrefixLen.setStatus("current")
_TnIPv6Address_Type = InetAddress
_TnIPv6Address_Object = MibTableColumn
tnIPv6Address = _TnIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 9, 1, 8),
    _TnIPv6Address_Type()
)
tnIPv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIPv6Address.setStatus("current")
_TnIPv6RouterAddr_Type = InetAddress
_TnIPv6RouterAddr_Object = MibTableColumn
tnIPv6RouterAddr = _TnIPv6RouterAddr_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 9, 1, 9),
    _TnIPv6RouterAddr_Type()
)
tnIPv6RouterAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIPv6RouterAddr.setStatus("current")


class _TnIPv6DupAddressDetected_Type(Integer32):
    """Custom type tnIPv6DupAddressDetected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_TnIPv6DupAddressDetected_Type.__name__ = "Integer32"
_TnIPv6DupAddressDetected_Object = MibTableColumn
tnIPv6DupAddressDetected = _TnIPv6DupAddressDetected_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 9, 1, 10),
    _TnIPv6DupAddressDetected_Type()
)
tnIPv6DupAddressDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIPv6DupAddressDetected.setStatus("current")


class _TnIPv6Scope_Type(Integer32):
    """Custom type tnIPv6Scope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("node", 1),
          ("link", 2),
          ("site", 3),
          ("organization", 4),
          ("host", 5),
          ("global", 6))
    )


_TnIPv6Scope_Type.__name__ = "Integer32"
_TnIPv6Scope_Object = MibTableColumn
tnIPv6Scope = _TnIPv6Scope_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 9, 1, 11),
    _TnIPv6Scope_Type()
)
tnIPv6Scope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIPv6Scope.setStatus("current")
_TnIPv6MTU_Type = Integer32
_TnIPv6MTU_Object = MibTableColumn
tnIPv6MTU = _TnIPv6MTU_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 9, 1, 12),
    _TnIPv6MTU_Type()
)
tnIPv6MTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIPv6MTU.setStatus("current")
_TnIPv6LinkMTU_Type = Integer32
_TnIPv6LinkMTU_Object = MibTableColumn
tnIPv6LinkMTU = _TnIPv6LinkMTU_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 9, 1, 13),
    _TnIPv6LinkMTU_Type()
)
tnIPv6LinkMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIPv6LinkMTU.setStatus("current")


class _TnIPv6Status_Type(Integer32):
    """Custom type tnIPv6Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("disabled", 2),
          ("renew", 3))
    )


_TnIPv6Status_Type.__name__ = "Integer32"
_TnIPv6Status_Object = MibTableColumn
tnIPv6Status = _TnIPv6Status_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 1, 9, 1, 14),
    _TnIPv6Status_Type()
)
tnIPv6Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIPv6Status.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-DEV-SYS-IPMGMT-MIB",
    **{"tnDevSysIpMgmtMIB": tnDevSysIpMgmtMIB,
       "tnDevSysIpmgmt": tnDevSysIpmgmt,
       "tnIpMgmtTable": tnIpMgmtTable,
       "tnIpMgmtEntry": tnIpMgmtEntry,
       "tnIpAddressMode": tnIpAddressMode,
       "tnIpMgmtAccess": tnIpMgmtAccess,
       "tnIpAddrType": tnIpAddrType,
       "tnIpAddr": tnIpAddr,
       "tnSubnetMask": tnSubnetMask,
       "tnDefaultGateway": tnDefaultGateway,
       "tnDnsServerTable": tnDnsServerTable,
       "tnDnsServerEntry": tnDnsServerEntry,
       "tnDnsServerIndex": tnDnsServerIndex,
       "tnDnsServerIPAddrType": tnDnsServerIPAddrType,
       "tnDnsServerIPAddr": tnDnsServerIPAddr,
       "tnDnsServerStatus": tnDnsServerStatus,
       "tnIpextMgmtTable": tnIpextMgmtTable,
       "tnIpextMgmtEntry": tnIpextMgmtEntry,
       "tnIpv6status": tnIpv6status,
       "tnIpv6AddressLinklocal": tnIpv6AddressLinklocal,
       "tnIpv6Method": tnIpv6Method,
       "tnIpv6Addr": tnIpv6Addr,
       "tnIpv6prefix": tnIpv6prefix,
       "tnIpv6DupAddrDetected": tnIpv6DupAddrDetected,
       "tnIpv6GwMethod": tnIpv6GwMethod,
       "tnIpv6defaultGW": tnIpv6defaultGW,
       "tnIpv6DynRouteTable": tnIpv6DynRouteTable,
       "tnIpv6DynRouteEntry": tnIpv6DynRouteEntry,
       "tnIpv6DynRouteIndex": tnIpv6DynRouteIndex,
       "tnIpv6DynRouteDest": tnIpv6DynRouteDest,
       "tnIpv6DynRoutePfxLen": tnIpv6DynRoutePfxLen,
       "tnIpv6DynRouteNextHop": tnIpv6DynRouteNextHop,
       "tnIpv6DynRouteAge": tnIpv6DynRouteAge,
       "tnHostToIpTable": tnHostToIpTable,
       "tnHostToIpEntry": tnHostToIpEntry,
       "tnHostToIpIndex": tnHostToIpIndex,
       "tnHostIPAddrType": tnHostIPAddrType,
       "tnHostIPAddr": tnHostIPAddr,
       "tnHostName": tnHostName,
       "tnAliasName": tnAliasName,
       "tnEntryStatus": tnEntryStatus,
       "tnIPv4MgmtTable": tnIPv4MgmtTable,
       "tnIPv4MgmtEntry": tnIPv4MgmtEntry,
       "tnIpv4Interface": tnIpv4Interface,
       "tnIPv4Index": tnIPv4Index,
       "tnIPv4ConfigMode": tnIPv4ConfigMode,
       "tnIPv4Origin": tnIPv4Origin,
       "tnIPv4AddrType": tnIPv4AddrType,
       "tnIPv4Addr": tnIPv4Addr,
       "tnIPv4SubnetMask": tnIPv4SubnetMask,
       "tnIPv4DefaultGateway": tnIPv4DefaultGateway,
       "tnIPv4Status": tnIPv4Status,
       "tnIPv6MgmtTable": tnIPv6MgmtTable,
       "tnIPv6MgmtEntry": tnIPv6MgmtEntry,
       "tnIpv6Interface": tnIpv6Interface,
       "tnIPv6Index": tnIPv6Index,
       "tnIPv6Origin": tnIPv6Origin,
       "tnIPv6CfgMethod": tnIPv6CfgMethod,
       "tnIPv6AddressType": tnIPv6AddressType,
       "tnIPv6Prefix": tnIPv6Prefix,
       "tnIPv6PrefixLen": tnIPv6PrefixLen,
       "tnIPv6Address": tnIPv6Address,
       "tnIPv6RouterAddr": tnIPv6RouterAddr,
       "tnIPv6DupAddressDetected": tnIPv6DupAddressDetected,
       "tnIPv6Scope": tnIPv6Scope,
       "tnIPv6MTU": tnIPv6MTU,
       "tnIPv6LinkMTU": tnIPv6LinkMTU,
       "tnIPv6Status": tnIPv6Status}
)
