# SNMP MIB module (TPLINK-IPV6ADDR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\tplink\TPLINK-IPV6ADDR-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:30:31 2025
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(tplinkMgmt,) = mibBuilder.importSymbols(
    "TPLINK-MIB",
    "tplinkMgmt")


# MODULE-IDENTITY

tplinkIpv6AddrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 50)
)
if mibBuilder.loadTexts:
    tplinkIpv6AddrMIB.setRevisions(
        ("2012-12-13 09:30",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkIpv6AddrMIBObjects_ObjectIdentity = ObjectIdentity
tplinkIpv6AddrMIBObjects = _TplinkIpv6AddrMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 50, 1)
)
_Ipv6ParaConfigAddrTable_Object = MibTable
ipv6ParaConfigAddrTable = _Ipv6ParaConfigAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 50, 1, 1)
)
if mibBuilder.loadTexts:
    ipv6ParaConfigAddrTable.setStatus("current")
_Ipv6ParaConfigAddrEntry_Object = MibTableRow
ipv6ParaConfigAddrEntry = _Ipv6ParaConfigAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 50, 1, 1, 1)
)
ipv6ParaConfigAddrEntry.setIndexNames(
    (0, "TPLINK-IPV6ADDR-MIB", "ipv6ParaConfigIfIndex"),
    (0, "TPLINK-IPV6ADDR-MIB", "ipv6ParaConfigAddrType"),
    (0, "TPLINK-IPV6ADDR-MIB", "ipv6ParaConfigSourceType"),
    (0, "TPLINK-IPV6ADDR-MIB", "ipv6ParaConfigAddress"),
)
if mibBuilder.loadTexts:
    ipv6ParaConfigAddrEntry.setStatus("current")
_Ipv6ParaConfigIfIndex_Type = Integer32
_Ipv6ParaConfigIfIndex_Object = MibTableColumn
ipv6ParaConfigIfIndex = _Ipv6ParaConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 50, 1, 1, 1, 1),
    _Ipv6ParaConfigIfIndex_Type()
)
ipv6ParaConfigIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6ParaConfigIfIndex.setStatus("current")
_Ipv6ParaConfigIfDescription_Type = DisplayString
_Ipv6ParaConfigIfDescription_Object = MibTableColumn
ipv6ParaConfigIfDescription = _Ipv6ParaConfigIfDescription_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 50, 1, 1, 1, 2),
    _Ipv6ParaConfigIfDescription_Type()
)
ipv6ParaConfigIfDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6ParaConfigIfDescription.setStatus("current")
_Ipv6ParaConfigAddrType_Type = InetAddressType
_Ipv6ParaConfigAddrType_Object = MibTableColumn
ipv6ParaConfigAddrType = _Ipv6ParaConfigAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 50, 1, 1, 1, 3),
    _Ipv6ParaConfigAddrType_Type()
)
ipv6ParaConfigAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6ParaConfigAddrType.setStatus("current")
_Ipv6ParaConfigAddress_Type = InetAddress
_Ipv6ParaConfigAddress_Object = MibTableColumn
ipv6ParaConfigAddress = _Ipv6ParaConfigAddress_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 50, 1, 1, 1, 4),
    _Ipv6ParaConfigAddress_Type()
)
ipv6ParaConfigAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6ParaConfigAddress.setStatus("current")


class _Ipv6ParaConfigPrefixLength_Type(Integer32):
    """Custom type ipv6ParaConfigPrefixLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Ipv6ParaConfigPrefixLength_Type.__name__ = "Integer32"
_Ipv6ParaConfigPrefixLength_Object = MibTableColumn
ipv6ParaConfigPrefixLength = _Ipv6ParaConfigPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 50, 1, 1, 1, 5),
    _Ipv6ParaConfigPrefixLength_Type()
)
ipv6ParaConfigPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipv6ParaConfigPrefixLength.setStatus("current")


class _Ipv6ParaConfigSourceType_Type(Integer32):
    """Custom type ipv6ParaConfigSourceType based on Integer32"""
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
        *(("assignedIp", 1),
          ("assignedEUI64Ip", 2),
          ("assignedLinklocalIp", 3),
          ("autoIp", 4),
          ("dhcpv6", 5),
          ("negotiate", 6))
    )


_Ipv6ParaConfigSourceType_Type.__name__ = "Integer32"
_Ipv6ParaConfigSourceType_Object = MibTableColumn
ipv6ParaConfigSourceType = _Ipv6ParaConfigSourceType_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 50, 1, 1, 1, 6),
    _Ipv6ParaConfigSourceType_Type()
)
ipv6ParaConfigSourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6ParaConfigSourceType.setStatus("current")
_Ipv6ParaConfigRowStatus_Type = RowStatus
_Ipv6ParaConfigRowStatus_Object = MibTableColumn
ipv6ParaConfigRowStatus = _Ipv6ParaConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 50, 1, 1, 1, 7),
    _Ipv6ParaConfigRowStatus_Type()
)
ipv6ParaConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipv6ParaConfigRowStatus.setStatus("current")
_Ipv6ParaConfigCfgTable_Object = MibTable
ipv6ParaConfigCfgTable = _Ipv6ParaConfigCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 50, 1, 2)
)
if mibBuilder.loadTexts:
    ipv6ParaConfigCfgTable.setStatus("current")
_Ipv6ParaConfigCfgEntry_Object = MibTableRow
ipv6ParaConfigCfgEntry = _Ipv6ParaConfigCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 50, 1, 2, 1)
)
ipv6ParaConfigCfgEntry.setIndexNames(
    (0, "TPLINK-IPV6ADDR-MIB", "ipv6ParaConfigCfgIfIndex"),
)
if mibBuilder.loadTexts:
    ipv6ParaConfigCfgEntry.setStatus("current")
_Ipv6ParaConfigCfgIfIndex_Type = Integer32
_Ipv6ParaConfigCfgIfIndex_Object = MibTableColumn
ipv6ParaConfigCfgIfIndex = _Ipv6ParaConfigCfgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 50, 1, 2, 1, 1),
    _Ipv6ParaConfigCfgIfIndex_Type()
)
ipv6ParaConfigCfgIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6ParaConfigCfgIfIndex.setStatus("current")
_Ipv6ParaConfigCfgIfDescription_Type = DisplayString
_Ipv6ParaConfigCfgIfDescription_Object = MibTableColumn
ipv6ParaConfigCfgIfDescription = _Ipv6ParaConfigCfgIfDescription_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 50, 1, 2, 1, 2),
    _Ipv6ParaConfigCfgIfDescription_Type()
)
ipv6ParaConfigCfgIfDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6ParaConfigCfgIfDescription.setStatus("current")


class _Ipv6ParaConfigAutoLinkLocalEnable_Type(Integer32):
    """Custom type ipv6ParaConfigAutoLinkLocalEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ipv6ParaConfigAutoLinkLocalEnable_Type.__name__ = "Integer32"
_Ipv6ParaConfigAutoLinkLocalEnable_Object = MibTableColumn
ipv6ParaConfigAutoLinkLocalEnable = _Ipv6ParaConfigAutoLinkLocalEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 50, 1, 2, 1, 3),
    _Ipv6ParaConfigAutoLinkLocalEnable_Type()
)
ipv6ParaConfigAutoLinkLocalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6ParaConfigAutoLinkLocalEnable.setStatus("current")


class _Ipv6ParaConfigDhcpEnable_Type(Integer32):
    """Custom type ipv6ParaConfigDhcpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ipv6ParaConfigDhcpEnable_Type.__name__ = "Integer32"
_Ipv6ParaConfigDhcpEnable_Object = MibTableColumn
ipv6ParaConfigDhcpEnable = _Ipv6ParaConfigDhcpEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 50, 1, 2, 1, 4),
    _Ipv6ParaConfigDhcpEnable_Type()
)
ipv6ParaConfigDhcpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6ParaConfigDhcpEnable.setStatus("current")


class _Ipv6ParaConfigNegotiateEnable_Type(Integer32):
    """Custom type ipv6ParaConfigNegotiateEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ipv6ParaConfigNegotiateEnable_Type.__name__ = "Integer32"
_Ipv6ParaConfigNegotiateEnable_Object = MibTableColumn
ipv6ParaConfigNegotiateEnable = _Ipv6ParaConfigNegotiateEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 50, 1, 2, 1, 5),
    _Ipv6ParaConfigNegotiateEnable_Type()
)
ipv6ParaConfigNegotiateEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6ParaConfigNegotiateEnable.setStatus("current")


class _Ipv6ParaConfigIPv6Enable_Type(Integer32):
    """Custom type ipv6ParaConfigIPv6Enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Ipv6ParaConfigIPv6Enable_Type.__name__ = "Integer32"
_Ipv6ParaConfigIPv6Enable_Object = MibTableColumn
ipv6ParaConfigIPv6Enable = _Ipv6ParaConfigIPv6Enable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 50, 1, 2, 1, 6),
    _Ipv6ParaConfigIPv6Enable_Type()
)
ipv6ParaConfigIPv6Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6ParaConfigIPv6Enable.setStatus("current")
_Ipv6GatewayConfig_ObjectIdentity = ObjectIdentity
ipv6GatewayConfig = _Ipv6GatewayConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 50, 1, 3)
)


class _Ipv6Gateway_Type(OctetString):
    """Custom type ipv6Gateway based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(46, 46),
    )
    fixed_length = 46


_Ipv6Gateway_Type.__name__ = "OctetString"
_Ipv6Gateway_Object = MibScalar
ipv6Gateway = _Ipv6Gateway_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 50, 1, 3, 1),
    _Ipv6Gateway_Type()
)
ipv6Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6Gateway.setStatus("current")
_TplinkIpv6RoutingConfig_ObjectIdentity = ObjectIdentity
tplinkIpv6RoutingConfig = _TplinkIpv6RoutingConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 50, 2)
)


class _TpIpv6Routing_Type(Integer32):
    """Custom type tpIpv6Routing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpIpv6Routing_Type.__name__ = "Integer32"
_TpIpv6Routing_Object = MibScalar
tpIpv6Routing = _TpIpv6Routing_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 50, 2, 1),
    _TpIpv6Routing_Type()
)
tpIpv6Routing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpIpv6Routing.setStatus("current")
_TplinkIpv6AddrNotifications_ObjectIdentity = ObjectIdentity
tplinkIpv6AddrNotifications = _TplinkIpv6AddrNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 50, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-IPV6ADDR-MIB",
    **{"tplinkIpv6AddrMIB": tplinkIpv6AddrMIB,
       "tplinkIpv6AddrMIBObjects": tplinkIpv6AddrMIBObjects,
       "ipv6ParaConfigAddrTable": ipv6ParaConfigAddrTable,
       "ipv6ParaConfigAddrEntry": ipv6ParaConfigAddrEntry,
       "ipv6ParaConfigIfIndex": ipv6ParaConfigIfIndex,
       "ipv6ParaConfigIfDescription": ipv6ParaConfigIfDescription,
       "ipv6ParaConfigAddrType": ipv6ParaConfigAddrType,
       "ipv6ParaConfigAddress": ipv6ParaConfigAddress,
       "ipv6ParaConfigPrefixLength": ipv6ParaConfigPrefixLength,
       "ipv6ParaConfigSourceType": ipv6ParaConfigSourceType,
       "ipv6ParaConfigRowStatus": ipv6ParaConfigRowStatus,
       "ipv6ParaConfigCfgTable": ipv6ParaConfigCfgTable,
       "ipv6ParaConfigCfgEntry": ipv6ParaConfigCfgEntry,
       "ipv6ParaConfigCfgIfIndex": ipv6ParaConfigCfgIfIndex,
       "ipv6ParaConfigCfgIfDescription": ipv6ParaConfigCfgIfDescription,
       "ipv6ParaConfigAutoLinkLocalEnable": ipv6ParaConfigAutoLinkLocalEnable,
       "ipv6ParaConfigDhcpEnable": ipv6ParaConfigDhcpEnable,
       "ipv6ParaConfigNegotiateEnable": ipv6ParaConfigNegotiateEnable,
       "ipv6ParaConfigIPv6Enable": ipv6ParaConfigIPv6Enable,
       "ipv6GatewayConfig": ipv6GatewayConfig,
       "ipv6Gateway": ipv6Gateway,
       "tplinkIpv6RoutingConfig": tplinkIpv6RoutingConfig,
       "tpIpv6Routing": tpIpv6Routing,
       "tplinkIpv6AddrNotifications": tplinkIpv6AddrNotifications}
)
