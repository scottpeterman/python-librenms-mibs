# SNMP MIB module (TN-DEV-SYS-IP2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TN-DEV-SYS-IP2-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:30:58 2025
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
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

(TNInterfaceIndex,) = mibBuilder.importSymbols(
    "TN-TC",
    "TNInterfaceIndex")

(tnProducts,) = mibBuilder.importSymbols(
    "TRANSITION-SMI",
    "tnProducts")


# MODULE-IDENTITY

tnDevSysIpMgmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10)
)
if mibBuilder.loadTexts:
    tnDevSysIpMgmtMIB.setRevisions(
        ("2014-04-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnDevSysIp2mgmt_ObjectIdentity = ObjectIdentity
tnDevSysIp2mgmt = _TnDevSysIp2mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 8)
)


class _TnIp2Mode_Type(Integer32):
    """Custom type tnIp2Mode based on Integer32"""
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
          ("host", 1),
          ("router", 2))
    )


_TnIp2Mode_Type.__name__ = "Integer32"
_TnIp2Mode_Object = MibScalar
tnIp2Mode = _TnIp2Mode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 8, 1),
    _TnIp2Mode_Type()
)
tnIp2Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIp2Mode.setStatus("current")
_TnIp2DnsConfig_ObjectIdentity = ObjectIdentity
tnIp2DnsConfig = _TnIp2DnsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 8, 2)
)


class _TnIp2DnsProxy_Type(Integer32):
    """Custom type tnIp2DnsProxy based on Integer32"""
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


_TnIp2DnsProxy_Type.__name__ = "Integer32"
_TnIp2DnsProxy_Object = MibScalar
tnIp2DnsProxy = _TnIp2DnsProxy_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 8, 2, 1),
    _TnIp2DnsProxy_Type()
)
tnIp2DnsProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIp2DnsProxy.setStatus("current")
_TnIp2DnsServerConfTable_Object = MibTable
tnIp2DnsServerConfTable = _TnIp2DnsServerConfTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 8, 2, 2)
)
if mibBuilder.loadTexts:
    tnIp2DnsServerConfTable.setStatus("current")
_TnIp2DnsServerConfEntry_Object = MibTableRow
tnIp2DnsServerConfEntry = _TnIp2DnsServerConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 8, 2, 2, 1)
)
tnIp2DnsServerConfEntry.setIndexNames(
    (0, "TN-DEV-SYS-IP2-MIB", "tnIp2DnsServerIndex"),
)
if mibBuilder.loadTexts:
    tnIp2DnsServerConfEntry.setStatus("current")


class _TnIp2DnsServerIndex_Type(Integer32):
    """Custom type tnIp2DnsServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_TnIp2DnsServerIndex_Type.__name__ = "Integer32"
_TnIp2DnsServerIndex_Object = MibTableColumn
tnIp2DnsServerIndex = _TnIp2DnsServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 8, 2, 2, 1, 1),
    _TnIp2DnsServerIndex_Type()
)
tnIp2DnsServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnIp2DnsServerIndex.setStatus("current")


class _TnIp2DnsServerMode_Type(Integer32):
    """Custom type tnIp2DnsServerMode based on Integer32"""
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
        *(("noDNS", 1),
          ("staticIPv4", 2),
          ("staticIPv6", 3),
          ("anyDHCPv4", 4),
          ("thisDHCPv4", 5),
          ("anyDHCPv6", 6),
          ("thisDHCPv6", 7))
    )


_TnIp2DnsServerMode_Type.__name__ = "Integer32"
_TnIp2DnsServerMode_Object = MibTableColumn
tnIp2DnsServerMode = _TnIp2DnsServerMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 8, 2, 2, 1, 2),
    _TnIp2DnsServerMode_Type()
)
tnIp2DnsServerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIp2DnsServerMode.setStatus("current")
_TnIp2DnsServerAddr_Type = InetAddress
_TnIp2DnsServerAddr_Object = MibTableColumn
tnIp2DnsServerAddr = _TnIp2DnsServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 8, 2, 2, 1, 3),
    _TnIp2DnsServerAddr_Type()
)
tnIp2DnsServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIp2DnsServerAddr.setStatus("current")
_TnIp2DnsVlan_Type = TNInterfaceIndex
_TnIp2DnsVlan_Object = MibTableColumn
tnIp2DnsVlan = _TnIp2DnsVlan_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 8, 2, 2, 1, 4),
    _TnIp2DnsVlan_Type()
)
tnIp2DnsVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIp2DnsVlan.setStatus("current")
_TnIp2InterfaceTable_Object = MibTable
tnIp2InterfaceTable = _TnIp2InterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 8, 3)
)
if mibBuilder.loadTexts:
    tnIp2InterfaceTable.setStatus("current")
_TnIp2InterfaceEntry_Object = MibTableRow
tnIp2InterfaceEntry = _TnIp2InterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 8, 3, 1)
)
tnIp2InterfaceEntry.setIndexNames(
    (0, "TN-DEV-SYS-IP2-MIB", "tnIp2IntVlan"),
)
if mibBuilder.loadTexts:
    tnIp2InterfaceEntry.setStatus("current")


class _TnIp2IntVlan_Type(Integer32):
    """Custom type tnIp2IntVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_TnIp2IntVlan_Type.__name__ = "Integer32"
_TnIp2IntVlan_Object = MibTableColumn
tnIp2IntVlan = _TnIp2IntVlan_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 8, 3, 1, 1),
    _TnIp2IntVlan_Type()
)
tnIp2IntVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnIp2IntVlan.setStatus("current")


class _TnIp2IntDHCPEnable_Type(Integer32):
    """Custom type tnIp2IntDHCPEnable based on Integer32"""
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


_TnIp2IntDHCPEnable_Type.__name__ = "Integer32"
_TnIp2IntDHCPEnable_Object = MibTableColumn
tnIp2IntDHCPEnable = _TnIp2IntDHCPEnable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 8, 3, 1, 2),
    _TnIp2IntDHCPEnable_Type()
)
tnIp2IntDHCPEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnIp2IntDHCPEnable.setStatus("current")
_TnIp2IntFallback_Type = Integer32
_TnIp2IntFallback_Object = MibTableColumn
tnIp2IntFallback = _TnIp2IntFallback_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 8, 3, 1, 3),
    _TnIp2IntFallback_Type()
)
tnIp2IntFallback.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnIp2IntFallback.setStatus("current")
_TnIp2AddrType_Type = InetAddressType
_TnIp2AddrType_Object = MibTableColumn
tnIp2AddrType = _TnIp2AddrType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 8, 3, 1, 4),
    _TnIp2AddrType_Type()
)
tnIp2AddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIp2AddrType.setStatus("current")
_TnIp2IntCurrentLease_Type = InetAddress
_TnIp2IntCurrentLease_Object = MibTableColumn
tnIp2IntCurrentLease = _TnIp2IntCurrentLease_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 8, 3, 1, 5),
    _TnIp2IntCurrentLease_Type()
)
tnIp2IntCurrentLease.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnIp2IntCurrentLease.setStatus("current")
_TnIp2Addr_Type = InetAddress
_TnIp2Addr_Object = MibTableColumn
tnIp2Addr = _TnIp2Addr_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 8, 3, 1, 6),
    _TnIp2Addr_Type()
)
tnIp2Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnIp2Addr.setStatus("current")
_TnIp2MaskLen_Type = Integer32
_TnIp2MaskLen_Object = MibTableColumn
tnIp2MaskLen = _TnIp2MaskLen_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 8, 3, 1, 7),
    _TnIp2MaskLen_Type()
)
tnIp2MaskLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnIp2MaskLen.setStatus("current")
_TnIp2Status_Type = RowStatus
_TnIp2Status_Object = MibTableColumn
tnIp2Status = _TnIp2Status_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 8, 3, 1, 8),
    _TnIp2Status_Type()
)
tnIp2Status.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnIp2Status.setStatus("current")
_TnIp2RoutesTable_Object = MibTable
tnIp2RoutesTable = _TnIp2RoutesTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 8, 4)
)
if mibBuilder.loadTexts:
    tnIp2RoutesTable.setStatus("current")
_TnIp2RoutesEntry_Object = MibTableRow
tnIp2RoutesEntry = _TnIp2RoutesEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 8, 4, 1)
)
tnIp2RoutesEntry.setIndexNames(
    (0, "TN-DEV-SYS-IP2-MIB", "tnIp2RoutesNetwork"),
    (0, "TN-DEV-SYS-IP2-MIB", "tnIp2RoutesMaskLen"),
    (0, "TN-DEV-SYS-IP2-MIB", "tnIp2RoutesGateway"),
    (0, "TN-DEV-SYS-IP2-MIB", "tnIp2RoutesNextHop"),
)
if mibBuilder.loadTexts:
    tnIp2RoutesEntry.setStatus("current")
_TnIp2RoutesNetwork_Type = InetAddress
_TnIp2RoutesNetwork_Object = MibTableColumn
tnIp2RoutesNetwork = _TnIp2RoutesNetwork_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 8, 4, 1, 1),
    _TnIp2RoutesNetwork_Type()
)
tnIp2RoutesNetwork.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnIp2RoutesNetwork.setStatus("current")
_TnIp2RoutesMaskLen_Type = Integer32
_TnIp2RoutesMaskLen_Object = MibTableColumn
tnIp2RoutesMaskLen = _TnIp2RoutesMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 8, 4, 1, 2),
    _TnIp2RoutesMaskLen_Type()
)
tnIp2RoutesMaskLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnIp2RoutesMaskLen.setStatus("current")
_TnIp2RoutesGateway_Type = InetAddress
_TnIp2RoutesGateway_Object = MibTableColumn
tnIp2RoutesGateway = _TnIp2RoutesGateway_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 8, 4, 1, 3),
    _TnIp2RoutesGateway_Type()
)
tnIp2RoutesGateway.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnIp2RoutesGateway.setStatus("current")
_TnIp2RoutesNextHop_Type = Integer32
_TnIp2RoutesNextHop_Object = MibTableColumn
tnIp2RoutesNextHop = _TnIp2RoutesNextHop_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 8, 4, 1, 4),
    _TnIp2RoutesNextHop_Type()
)
tnIp2RoutesNextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnIp2RoutesNextHop.setStatus("current")
_TnIp2RoutesType_Type = InetAddressType
_TnIp2RoutesType_Object = MibTableColumn
tnIp2RoutesType = _TnIp2RoutesType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 8, 4, 1, 5),
    _TnIp2RoutesType_Type()
)
tnIp2RoutesType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnIp2RoutesType.setStatus("current")
_TnIp2RoutesStatus_Type = RowStatus
_TnIp2RoutesStatus_Object = MibTableColumn
tnIp2RoutesStatus = _TnIp2RoutesStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 10, 8, 4, 1, 6),
    _TnIp2RoutesStatus_Type()
)
tnIp2RoutesStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnIp2RoutesStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-DEV-SYS-IP2-MIB",
    **{"tnDevSysIpMgmtMIB": tnDevSysIpMgmtMIB,
       "tnDevSysIp2mgmt": tnDevSysIp2mgmt,
       "tnIp2Mode": tnIp2Mode,
       "tnIp2DnsConfig": tnIp2DnsConfig,
       "tnIp2DnsProxy": tnIp2DnsProxy,
       "tnIp2DnsServerConfTable": tnIp2DnsServerConfTable,
       "tnIp2DnsServerConfEntry": tnIp2DnsServerConfEntry,
       "tnIp2DnsServerIndex": tnIp2DnsServerIndex,
       "tnIp2DnsServerMode": tnIp2DnsServerMode,
       "tnIp2DnsServerAddr": tnIp2DnsServerAddr,
       "tnIp2DnsVlan": tnIp2DnsVlan,
       "tnIp2InterfaceTable": tnIp2InterfaceTable,
       "tnIp2InterfaceEntry": tnIp2InterfaceEntry,
       "tnIp2IntVlan": tnIp2IntVlan,
       "tnIp2IntDHCPEnable": tnIp2IntDHCPEnable,
       "tnIp2IntFallback": tnIp2IntFallback,
       "tnIp2AddrType": tnIp2AddrType,
       "tnIp2IntCurrentLease": tnIp2IntCurrentLease,
       "tnIp2Addr": tnIp2Addr,
       "tnIp2MaskLen": tnIp2MaskLen,
       "tnIp2Status": tnIp2Status,
       "tnIp2RoutesTable": tnIp2RoutesTable,
       "tnIp2RoutesEntry": tnIp2RoutesEntry,
       "tnIp2RoutesNetwork": tnIp2RoutesNetwork,
       "tnIp2RoutesMaskLen": tnIp2RoutesMaskLen,
       "tnIp2RoutesGateway": tnIp2RoutesGateway,
       "tnIp2RoutesNextHop": tnIp2RoutesNextHop,
       "tnIp2RoutesType": tnIp2RoutesType,
       "tnIp2RoutesStatus": tnIp2RoutesStatus}
)
