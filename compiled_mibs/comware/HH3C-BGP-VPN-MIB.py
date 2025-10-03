# SNMP MIB module (HH3C-BGP-VPN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-BGP-VPN-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:30:48 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

hh3cBgpVpn = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 202)
)
if mibBuilder.loadTexts:
    hh3cBgpVpn.setRevisions(
        ("2021-02-04 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Hh3cBgpAFI(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              25,
              196)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2),
          ("l2vpn", 25),
          ("l2vpnDraft", 196))
    )



class Hh3cBgpSAFI(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              65,
              66,
              70,
              128,
              132)
        )
    )
    namedValues = NamedValues(
        *(("unicast", 1),
          ("multicast", 2),
          ("mpls", 4),
          ("mcastVpn", 5),
          ("l2vpn", 65),
          ("mdt", 66),
          ("evpn", 70),
          ("vpn", 128),
          ("routeTarget", 132))
    )



class Hh3cBgpVpnId(TextualConvention, OctetString):
    status = "current"
    displayHint = "31a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )



# MIB Managed Objects in the order of their OIDs

_Hh3cBgpVpnObjects_ObjectIdentity = ObjectIdentity
hh3cBgpVpnObjects = _Hh3cBgpVpnObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 202, 1)
)
_Hh3cBgpPeers_ObjectIdentity = ObjectIdentity
hh3cBgpPeers = _Hh3cBgpPeers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 202, 1, 1)
)
_Hh3cBgpPeerAddrFamilyTable_Object = MibTable
hh3cBgpPeerAddrFamilyTable = _Hh3cBgpPeerAddrFamilyTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 202, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cBgpPeerAddrFamilyTable.setStatus("current")
_Hh3cBgpPeerAddrFamilyEntry_Object = MibTableRow
hh3cBgpPeerAddrFamilyEntry = _Hh3cBgpPeerAddrFamilyEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 202, 1, 1, 1, 1)
)
hh3cBgpPeerAddrFamilyEntry.setIndexNames(
    (0, "HH3C-BGP-VPN-MIB", "hh3cBgpPeerInstanceId"),
    (0, "HH3C-BGP-VPN-MIB", "hh3cBgpPeerVpnIndex"),
    (0, "HH3C-BGP-VPN-MIB", "hh3cBgpPeerAddrFamilyId"),
    (0, "HH3C-BGP-VPN-MIB", "hh3cBgpPeerSubAddrFamilyId"),
    (0, "HH3C-BGP-VPN-MIB", "hh3cBgpPeerType"),
    (0, "HH3C-BGP-VPN-MIB", "hh3cBgpPeerIPAddr"),
)
if mibBuilder.loadTexts:
    hh3cBgpPeerAddrFamilyEntry.setStatus("current")


class _Hh3cBgpPeerInstanceId_Type(Unsigned32):
    """Custom type hh3cBgpPeerInstanceId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3cBgpPeerInstanceId_Type.__name__ = "Unsigned32"
_Hh3cBgpPeerInstanceId_Object = MibTableColumn
hh3cBgpPeerInstanceId = _Hh3cBgpPeerInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 202, 1, 1, 1, 1, 1),
    _Hh3cBgpPeerInstanceId_Type()
)
hh3cBgpPeerInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cBgpPeerInstanceId.setStatus("current")
_Hh3cBgpPeerVpnIndex_Type = Unsigned32
_Hh3cBgpPeerVpnIndex_Object = MibTableColumn
hh3cBgpPeerVpnIndex = _Hh3cBgpPeerVpnIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 202, 1, 1, 1, 1, 2),
    _Hh3cBgpPeerVpnIndex_Type()
)
hh3cBgpPeerVpnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cBgpPeerVpnIndex.setStatus("current")
_Hh3cBgpPeerAddrFamilyId_Type = Hh3cBgpAFI
_Hh3cBgpPeerAddrFamilyId_Object = MibTableColumn
hh3cBgpPeerAddrFamilyId = _Hh3cBgpPeerAddrFamilyId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 202, 1, 1, 1, 1, 3),
    _Hh3cBgpPeerAddrFamilyId_Type()
)
hh3cBgpPeerAddrFamilyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cBgpPeerAddrFamilyId.setStatus("current")
_Hh3cBgpPeerSubAddrFamilyId_Type = Hh3cBgpSAFI
_Hh3cBgpPeerSubAddrFamilyId_Object = MibTableColumn
hh3cBgpPeerSubAddrFamilyId = _Hh3cBgpPeerSubAddrFamilyId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 202, 1, 1, 1, 1, 4),
    _Hh3cBgpPeerSubAddrFamilyId_Type()
)
hh3cBgpPeerSubAddrFamilyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cBgpPeerSubAddrFamilyId.setStatus("current")
_Hh3cBgpPeerType_Type = InetAddressType
_Hh3cBgpPeerType_Object = MibTableColumn
hh3cBgpPeerType = _Hh3cBgpPeerType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 202, 1, 1, 1, 1, 5),
    _Hh3cBgpPeerType_Type()
)
hh3cBgpPeerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cBgpPeerType.setStatus("current")
_Hh3cBgpPeerIPAddr_Type = InetAddress
_Hh3cBgpPeerIPAddr_Object = MibTableColumn
hh3cBgpPeerIPAddr = _Hh3cBgpPeerIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 202, 1, 1, 1, 1, 6),
    _Hh3cBgpPeerIPAddr_Type()
)
hh3cBgpPeerIPAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cBgpPeerIPAddr.setStatus("current")
_Hh3cBgpPeerVpnName_Type = Hh3cBgpVpnId
_Hh3cBgpPeerVpnName_Object = MibTableColumn
hh3cBgpPeerVpnName = _Hh3cBgpPeerVpnName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 202, 1, 1, 1, 1, 7),
    _Hh3cBgpPeerVpnName_Type()
)
hh3cBgpPeerVpnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBgpPeerVpnName.setStatus("current")
_Hh3cBgpPeerRouteTable_Object = MibTable
hh3cBgpPeerRouteTable = _Hh3cBgpPeerRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 202, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cBgpPeerRouteTable.setStatus("current")
_Hh3cBgpPeerRouteEntry_Object = MibTableRow
hh3cBgpPeerRouteEntry = _Hh3cBgpPeerRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 202, 1, 1, 3, 1)
)
hh3cBgpPeerRouteEntry.setIndexNames(
    (0, "HH3C-BGP-VPN-MIB", "hh3cBgpPeerInstanceId"),
    (0, "HH3C-BGP-VPN-MIB", "hh3cBgpPeerVpnIndex"),
    (0, "HH3C-BGP-VPN-MIB", "hh3cBgpPeerAddrFamilyId"),
    (0, "HH3C-BGP-VPN-MIB", "hh3cBgpPeerSubAddrFamilyId"),
    (0, "HH3C-BGP-VPN-MIB", "hh3cBgpPeerType"),
    (0, "HH3C-BGP-VPN-MIB", "hh3cBgpPeerIPAddr"),
)
if mibBuilder.loadTexts:
    hh3cBgpPeerRouteEntry.setStatus("current")
_Hh3cBgpPeerRouteRcvCount_Type = Counter32
_Hh3cBgpPeerRouteRcvCount_Object = MibTableColumn
hh3cBgpPeerRouteRcvCount = _Hh3cBgpPeerRouteRcvCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 202, 1, 1, 3, 1, 1),
    _Hh3cBgpPeerRouteRcvCount_Type()
)
hh3cBgpPeerRouteRcvCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBgpPeerRouteRcvCount.setStatus("current")
_Hh3cBgpPeerRouteActiveCount_Type = Counter32
_Hh3cBgpPeerRouteActiveCount_Object = MibTableColumn
hh3cBgpPeerRouteActiveCount = _Hh3cBgpPeerRouteActiveCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 202, 1, 1, 3, 1, 2),
    _Hh3cBgpPeerRouteActiveCount_Type()
)
hh3cBgpPeerRouteActiveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBgpPeerRouteActiveCount.setStatus("current")
_Hh3cBgpPeerRouteAdvCount_Type = Counter32
_Hh3cBgpPeerRouteAdvCount_Object = MibTableColumn
hh3cBgpPeerRouteAdvCount = _Hh3cBgpPeerRouteAdvCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 202, 1, 1, 3, 1, 3),
    _Hh3cBgpPeerRouteAdvCount_Type()
)
hh3cBgpPeerRouteAdvCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBgpPeerRouteAdvCount.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-BGP-VPN-MIB",
    **{"Hh3cBgpAFI": Hh3cBgpAFI,
       "Hh3cBgpSAFI": Hh3cBgpSAFI,
       "Hh3cBgpVpnId": Hh3cBgpVpnId,
       "hh3cBgpVpn": hh3cBgpVpn,
       "hh3cBgpVpnObjects": hh3cBgpVpnObjects,
       "hh3cBgpPeers": hh3cBgpPeers,
       "hh3cBgpPeerAddrFamilyTable": hh3cBgpPeerAddrFamilyTable,
       "hh3cBgpPeerAddrFamilyEntry": hh3cBgpPeerAddrFamilyEntry,
       "hh3cBgpPeerInstanceId": hh3cBgpPeerInstanceId,
       "hh3cBgpPeerVpnIndex": hh3cBgpPeerVpnIndex,
       "hh3cBgpPeerAddrFamilyId": hh3cBgpPeerAddrFamilyId,
       "hh3cBgpPeerSubAddrFamilyId": hh3cBgpPeerSubAddrFamilyId,
       "hh3cBgpPeerType": hh3cBgpPeerType,
       "hh3cBgpPeerIPAddr": hh3cBgpPeerIPAddr,
       "hh3cBgpPeerVpnName": hh3cBgpPeerVpnName,
       "hh3cBgpPeerRouteTable": hh3cBgpPeerRouteTable,
       "hh3cBgpPeerRouteEntry": hh3cBgpPeerRouteEntry,
       "hh3cBgpPeerRouteRcvCount": hh3cBgpPeerRouteRcvCount,
       "hh3cBgpPeerRouteActiveCount": hh3cBgpPeerRouteActiveCount,
       "hh3cBgpPeerRouteAdvCount": hh3cBgpPeerRouteAdvCount}
)
