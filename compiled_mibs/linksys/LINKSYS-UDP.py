# SNMP MIB module (LINKSYS-UDP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\linksys\LINKSYS-UDP
# Produced by pysmi-1.6.2 at Thu Oct  2 12:10:11 2025
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

(ipCidrRouteDest,
 ipCidrRouteEntry,
 ipCidrRouteMask,
 ipCidrRouteNextHop,
 ipCidrRouteTos) = mibBuilder.importSymbols(
    "IP-FORWARD-MIB",
    "ipCidrRouteDest",
    "ipCidrRouteEntry",
    "ipCidrRouteMask",
    "ipCidrRouteNextHop",
    "ipCidrRouteTos")

(ipAddrEntry,) = mibBuilder.importSymbols(
    "IP-MIB",
    "ipAddrEntry")

(rnd,) = mibBuilder.importSymbols(
    "LINKSYS-MIB",
    "rnd")

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


# MODULE-IDENTITY

rsUDP = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 42)
)
if mibBuilder.loadTexts:
    rsUDP.setRevisions(
        ("2004-06-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RsUdpRelayTable_Object = MibTable
rsUdpRelayTable = _RsUdpRelayTable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 42, 1)
)
if mibBuilder.loadTexts:
    rsUdpRelayTable.setStatus("current")
_RsUdpRelayEntry_Object = MibTableRow
rsUdpRelayEntry = _RsUdpRelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 42, 1, 1)
)
rsUdpRelayEntry.setIndexNames(
    (0, "LINKSYS-UDP", "rsUdpRelayDstPort"),
    (0, "LINKSYS-UDP", "rsUdpRelaySrcIpInf"),
    (0, "LINKSYS-UDP", "rsUdpRelayDstIpAddr"),
)
if mibBuilder.loadTexts:
    rsUdpRelayEntry.setStatus("current")
_RsUdpRelayDstPort_Type = Integer32
_RsUdpRelayDstPort_Object = MibTableColumn
rsUdpRelayDstPort = _RsUdpRelayDstPort_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 42, 1, 1, 1),
    _RsUdpRelayDstPort_Type()
)
rsUdpRelayDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsUdpRelayDstPort.setStatus("current")
_RsUdpRelaySrcIpInf_Type = IpAddress
_RsUdpRelaySrcIpInf_Object = MibTableColumn
rsUdpRelaySrcIpInf = _RsUdpRelaySrcIpInf_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 42, 1, 1, 2),
    _RsUdpRelaySrcIpInf_Type()
)
rsUdpRelaySrcIpInf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsUdpRelaySrcIpInf.setStatus("current")
_RsUdpRelayDstIpAddr_Type = IpAddress
_RsUdpRelayDstIpAddr_Object = MibTableColumn
rsUdpRelayDstIpAddr = _RsUdpRelayDstIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 42, 1, 1, 3),
    _RsUdpRelayDstIpAddr_Type()
)
rsUdpRelayDstIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsUdpRelayDstIpAddr.setStatus("current")
_RsUdpRelayStatus_Type = RowStatus
_RsUdpRelayStatus_Object = MibTableColumn
rsUdpRelayStatus = _RsUdpRelayStatus_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 42, 1, 1, 4),
    _RsUdpRelayStatus_Type()
)
rsUdpRelayStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsUdpRelayStatus.setStatus("current")


class _RsUdpRelayUserInfo_Type(Integer32):
    """Custom type rsUdpRelayUserInfo based on Integer32"""
    defaultValue = 0


_RsUdpRelayUserInfo_Type.__name__ = "Integer32"
_RsUdpRelayUserInfo_Object = MibTableColumn
rsUdpRelayUserInfo = _RsUdpRelayUserInfo_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 42, 1, 1, 5),
    _RsUdpRelayUserInfo_Type()
)
rsUdpRelayUserInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsUdpRelayUserInfo.setStatus("current")
_RsUdpRelayMibVersion_Type = Integer32
_RsUdpRelayMibVersion_Object = MibScalar
rsUdpRelayMibVersion = _RsUdpRelayMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 42, 2),
    _RsUdpRelayMibVersion_Type()
)
rsUdpRelayMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsUdpRelayMibVersion.setStatus("current")
_RlUdpSessionTable_Object = MibTable
rlUdpSessionTable = _RlUdpSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 42, 3)
)
if mibBuilder.loadTexts:
    rlUdpSessionTable.setStatus("current")
_RlUdpSessionEntry_Object = MibTableRow
rlUdpSessionEntry = _RlUdpSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 42, 3, 1)
)
rlUdpSessionEntry.setIndexNames(
    (0, "LINKSYS-UDP", "rlUdpSessionLocalAddrType"),
    (0, "LINKSYS-UDP", "rlUdpSessionLocalAddr"),
    (0, "LINKSYS-UDP", "rlUdpSessionLocalPort"),
    (0, "LINKSYS-UDP", "rlUdpSessionAppInst"),
)
if mibBuilder.loadTexts:
    rlUdpSessionEntry.setStatus("current")
_RlUdpSessionLocalAddrType_Type = InetAddressType
_RlUdpSessionLocalAddrType_Object = MibTableColumn
rlUdpSessionLocalAddrType = _RlUdpSessionLocalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 42, 3, 1, 1),
    _RlUdpSessionLocalAddrType_Type()
)
rlUdpSessionLocalAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlUdpSessionLocalAddrType.setStatus("current")
_RlUdpSessionLocalAddr_Type = InetAddress
_RlUdpSessionLocalAddr_Object = MibTableColumn
rlUdpSessionLocalAddr = _RlUdpSessionLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 42, 3, 1, 2),
    _RlUdpSessionLocalAddr_Type()
)
rlUdpSessionLocalAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlUdpSessionLocalAddr.setStatus("current")
_RlUdpSessionLocalPort_Type = Integer32
_RlUdpSessionLocalPort_Object = MibTableColumn
rlUdpSessionLocalPort = _RlUdpSessionLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 42, 3, 1, 3),
    _RlUdpSessionLocalPort_Type()
)
rlUdpSessionLocalPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlUdpSessionLocalPort.setStatus("current")


class _RlUdpSessionAppInst_Type(Integer32):
    """Custom type rlUdpSessionAppInst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RlUdpSessionAppInst_Type.__name__ = "Integer32"
_RlUdpSessionAppInst_Object = MibTableColumn
rlUdpSessionAppInst = _RlUdpSessionAppInst_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 42, 3, 1, 4),
    _RlUdpSessionAppInst_Type()
)
rlUdpSessionAppInst.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlUdpSessionAppInst.setStatus("current")


class _RlUdpSessionAppName_Type(DisplayString):
    """Custom type rlUdpSessionAppName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_RlUdpSessionAppName_Type.__name__ = "DisplayString"
_RlUdpSessionAppName_Object = MibTableColumn
rlUdpSessionAppName = _RlUdpSessionAppName_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 42, 3, 1, 5),
    _RlUdpSessionAppName_Type()
)
rlUdpSessionAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlUdpSessionAppName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LINKSYS-UDP",
    **{"rsUDP": rsUDP,
       "rsUdpRelayTable": rsUdpRelayTable,
       "rsUdpRelayEntry": rsUdpRelayEntry,
       "rsUdpRelayDstPort": rsUdpRelayDstPort,
       "rsUdpRelaySrcIpInf": rsUdpRelaySrcIpInf,
       "rsUdpRelayDstIpAddr": rsUdpRelayDstIpAddr,
       "rsUdpRelayStatus": rsUdpRelayStatus,
       "rsUdpRelayUserInfo": rsUdpRelayUserInfo,
       "rsUdpRelayMibVersion": rsUdpRelayMibVersion,
       "rlUdpSessionTable": rlUdpSessionTable,
       "rlUdpSessionEntry": rlUdpSessionEntry,
       "rlUdpSessionLocalAddrType": rlUdpSessionLocalAddrType,
       "rlUdpSessionLocalAddr": rlUdpSessionLocalAddr,
       "rlUdpSessionLocalPort": rlUdpSessionLocalPort,
       "rlUdpSessionAppInst": rlUdpSessionAppInst,
       "rlUdpSessionAppName": rlUdpSessionAppName}
)
