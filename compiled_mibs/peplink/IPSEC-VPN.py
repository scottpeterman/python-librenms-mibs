# SNMP MIB module (IPSEC-VPN) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\peplink\IPSEC-VPN
# Produced by pysmi-1.6.2 at Thu Oct  2 12:20:41 2025
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ipsecVpnMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 13)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Peplink_ObjectIdentity = ObjectIdentity
peplink = _Peplink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23695)
)
_ProductMib_ObjectIdentity = ObjectIdentity
productMib = _ProductMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23695, 200)
)
_GeneralMib_ObjectIdentity = ObjectIdentity
generalMib = _GeneralMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1)
)
_IpsecVpnStatusTable_Object = MibTable
ipsecVpnStatusTable = _IpsecVpnStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 13, 1)
)
if mibBuilder.loadTexts:
    ipsecVpnStatusTable.setStatus("current")
_IpsecVpnStatusEntry_Object = MibTableRow
ipsecVpnStatusEntry = _IpsecVpnStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 13, 1, 1)
)
ipsecVpnStatusEntry.setIndexNames(
    (0, "IPSEC-VPN", "ipsecVpnStatusId"),
)
if mibBuilder.loadTexts:
    ipsecVpnStatusEntry.setStatus("current")
_IpsecVpnStatusId_Type = Integer32
_IpsecVpnStatusId_Object = MibTableColumn
ipsecVpnStatusId = _IpsecVpnStatusId_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 13, 1, 1, 1),
    _IpsecVpnStatusId_Type()
)
ipsecVpnStatusId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecVpnStatusId.setStatus("current")
_IpsecVpnStatusProfileName_Type = OctetString
_IpsecVpnStatusProfileName_Object = MibTableColumn
ipsecVpnStatusProfileName = _IpsecVpnStatusProfileName_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 13, 1, 1, 2),
    _IpsecVpnStatusProfileName_Type()
)
ipsecVpnStatusProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecVpnStatusProfileName.setStatus("current")


class _IpsecVpnStatusConnectionState_Type(Integer32):
    """Custom type ipsecVpnStatusConnectionState based on Integer32"""
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
        *(("standby", 0),
          ("connecting", 1),
          ("established", 2),
          ("partially-established", 3))
    )


_IpsecVpnStatusConnectionState_Type.__name__ = "Integer32"
_IpsecVpnStatusConnectionState_Object = MibTableColumn
ipsecVpnStatusConnectionState = _IpsecVpnStatusConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 13, 1, 1, 3),
    _IpsecVpnStatusConnectionState_Type()
)
ipsecVpnStatusConnectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecVpnStatusConnectionState.setStatus("current")
_IpsecVpnStatusWanName_Type = OctetString
_IpsecVpnStatusWanName_Object = MibTableColumn
ipsecVpnStatusWanName = _IpsecVpnStatusWanName_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 13, 1, 1, 4),
    _IpsecVpnStatusWanName_Type()
)
ipsecVpnStatusWanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecVpnStatusWanName.setStatus("current")
_IpsecVpnRouteStatusTable_Object = MibTable
ipsecVpnRouteStatusTable = _IpsecVpnRouteStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 13, 2)
)
if mibBuilder.loadTexts:
    ipsecVpnRouteStatusTable.setStatus("current")
_IpsecVpnRouteStatusEntry_Object = MibTableRow
ipsecVpnRouteStatusEntry = _IpsecVpnRouteStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 13, 2, 1)
)
ipsecVpnRouteStatusEntry.setIndexNames(
    (0, "IPSEC-VPN", "ipsecVpnStatusId"),
    (0, "IPSEC-VPN", "ipsecVpnRouteStatusId"),
)
if mibBuilder.loadTexts:
    ipsecVpnRouteStatusEntry.setStatus("current")
_IpsecVpnRouteStatusId_Type = Integer32
_IpsecVpnRouteStatusId_Object = MibTableColumn
ipsecVpnRouteStatusId = _IpsecVpnRouteStatusId_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 13, 2, 1, 1),
    _IpsecVpnRouteStatusId_Type()
)
ipsecVpnRouteStatusId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecVpnRouteStatusId.setStatus("current")


class _IpsecVpnRouteState_Type(Integer32):
    """Custom type ipsecVpnRouteState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1),
          ("standby", 2))
    )


_IpsecVpnRouteState_Type.__name__ = "Integer32"
_IpsecVpnRouteState_Object = MibTableColumn
ipsecVpnRouteState = _IpsecVpnRouteState_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 13, 2, 1, 2),
    _IpsecVpnRouteState_Type()
)
ipsecVpnRouteState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecVpnRouteState.setStatus("current")
_IpsecVpnRouteStatusLocalNetwork_Type = IpAddress
_IpsecVpnRouteStatusLocalNetwork_Object = MibTableColumn
ipsecVpnRouteStatusLocalNetwork = _IpsecVpnRouteStatusLocalNetwork_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 13, 2, 1, 3),
    _IpsecVpnRouteStatusLocalNetwork_Type()
)
ipsecVpnRouteStatusLocalNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecVpnRouteStatusLocalNetwork.setStatus("current")
_IpsecVpnRouteStatusLocalSubnet_Type = IpAddress
_IpsecVpnRouteStatusLocalSubnet_Object = MibTableColumn
ipsecVpnRouteStatusLocalSubnet = _IpsecVpnRouteStatusLocalSubnet_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 13, 2, 1, 4),
    _IpsecVpnRouteStatusLocalSubnet_Type()
)
ipsecVpnRouteStatusLocalSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecVpnRouteStatusLocalSubnet.setStatus("current")
_IpsecVpnRouteStatusRemoteNetwork_Type = IpAddress
_IpsecVpnRouteStatusRemoteNetwork_Object = MibTableColumn
ipsecVpnRouteStatusRemoteNetwork = _IpsecVpnRouteStatusRemoteNetwork_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 13, 2, 1, 5),
    _IpsecVpnRouteStatusRemoteNetwork_Type()
)
ipsecVpnRouteStatusRemoteNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecVpnRouteStatusRemoteNetwork.setStatus("current")
_IpsecVpnRouteStatusRemoteSubnet_Type = IpAddress
_IpsecVpnRouteStatusRemoteSubnet_Object = MibTableColumn
ipsecVpnRouteStatusRemoteSubnet = _IpsecVpnRouteStatusRemoteSubnet_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 13, 2, 1, 6),
    _IpsecVpnRouteStatusRemoteSubnet_Type()
)
ipsecVpnRouteStatusRemoteSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecVpnRouteStatusRemoteSubnet.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPSEC-VPN",
    **{"peplink": peplink,
       "productMib": productMib,
       "generalMib": generalMib,
       "ipsecVpnMib": ipsecVpnMib,
       "ipsecVpnStatusTable": ipsecVpnStatusTable,
       "ipsecVpnStatusEntry": ipsecVpnStatusEntry,
       "ipsecVpnStatusId": ipsecVpnStatusId,
       "ipsecVpnStatusProfileName": ipsecVpnStatusProfileName,
       "ipsecVpnStatusConnectionState": ipsecVpnStatusConnectionState,
       "ipsecVpnStatusWanName": ipsecVpnStatusWanName,
       "ipsecVpnRouteStatusTable": ipsecVpnRouteStatusTable,
       "ipsecVpnRouteStatusEntry": ipsecVpnRouteStatusEntry,
       "ipsecVpnRouteStatusId": ipsecVpnRouteStatusId,
       "ipsecVpnRouteState": ipsecVpnRouteState,
       "ipsecVpnRouteStatusLocalNetwork": ipsecVpnRouteStatusLocalNetwork,
       "ipsecVpnRouteStatusLocalSubnet": ipsecVpnRouteStatusLocalSubnet,
       "ipsecVpnRouteStatusRemoteNetwork": ipsecVpnRouteStatusRemoteNetwork,
       "ipsecVpnRouteStatusRemoteSubnet": ipsecVpnRouteStatusRemoteSubnet}
)
