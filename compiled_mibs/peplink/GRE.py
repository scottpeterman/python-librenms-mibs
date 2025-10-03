# SNMP MIB module (GRE) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\peplink\GRE
# Produced by pysmi-1.6.2 at Thu Oct  2 12:20:40 2025
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

greInfo = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 11, 1)
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
_GreMib_ObjectIdentity = ObjectIdentity
greMib = _GreMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 11)
)
_GreStatusTable_Object = MibTable
greStatusTable = _GreStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 11, 1, 1)
)
if mibBuilder.loadTexts:
    greStatusTable.setStatus("current")
_GreStatusEntry_Object = MibTableRow
greStatusEntry = _GreStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 11, 1, 1, 1)
)
greStatusEntry.setIndexNames(
    (0, "GRE", "greStatusId"),
)
if mibBuilder.loadTexts:
    greStatusEntry.setStatus("current")
_GreStatusId_Type = Integer32
_GreStatusId_Object = MibTableColumn
greStatusId = _GreStatusId_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 11, 1, 1, 1, 1),
    _GreStatusId_Type()
)
greStatusId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    greStatusId.setStatus("current")


class _GreStatusProfileName_Type(OctetString):
    """Custom type greStatusProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_GreStatusProfileName_Type.__name__ = "OctetString"
_GreStatusProfileName_Object = MibTableColumn
greStatusProfileName = _GreStatusProfileName_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 11, 1, 1, 1, 2),
    _GreStatusProfileName_Type()
)
greStatusProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    greStatusProfileName.setStatus("current")


class _GreStatusConnectionState_Type(Integer32):
    """Custom type greStatusConnectionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disconnected", 0),
          ("connected", 1),
          ("connecting", 2))
    )


_GreStatusConnectionState_Type.__name__ = "Integer32"
_GreStatusConnectionState_Object = MibTableColumn
greStatusConnectionState = _GreStatusConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 11, 1, 1, 1, 3),
    _GreStatusConnectionState_Type()
)
greStatusConnectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    greStatusConnectionState.setStatus("current")
_GreStatusLocalIpAddress_Type = IpAddress
_GreStatusLocalIpAddress_Object = MibTableColumn
greStatusLocalIpAddress = _GreStatusLocalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 11, 1, 1, 1, 4),
    _GreStatusLocalIpAddress_Type()
)
greStatusLocalIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    greStatusLocalIpAddress.setStatus("current")
_GreStatusRemoteIpAddress_Type = IpAddress
_GreStatusRemoteIpAddress_Object = MibTableColumn
greStatusRemoteIpAddress = _GreStatusRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 11, 1, 1, 1, 5),
    _GreStatusRemoteIpAddress_Type()
)
greStatusRemoteIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    greStatusRemoteIpAddress.setStatus("current")
_GreStatusTunnelLocalIpAddress_Type = IpAddress
_GreStatusTunnelLocalIpAddress_Object = MibTableColumn
greStatusTunnelLocalIpAddress = _GreStatusTunnelLocalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 11, 1, 1, 1, 6),
    _GreStatusTunnelLocalIpAddress_Type()
)
greStatusTunnelLocalIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    greStatusTunnelLocalIpAddress.setStatus("current")
_GreStatusTunnelRemoteIpAddress_Type = IpAddress
_GreStatusTunnelRemoteIpAddress_Object = MibTableColumn
greStatusTunnelRemoteIpAddress = _GreStatusTunnelRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 11, 1, 1, 1, 7),
    _GreStatusTunnelRemoteIpAddress_Type()
)
greStatusTunnelRemoteIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    greStatusTunnelRemoteIpAddress.setStatus("current")
_GreStatusRemoteNetworkTable_Object = MibTable
greStatusRemoteNetworkTable = _GreStatusRemoteNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 11, 1, 2)
)
if mibBuilder.loadTexts:
    greStatusRemoteNetworkTable.setStatus("current")
_GreStatusRemoteNetworkEntry_Object = MibTableRow
greStatusRemoteNetworkEntry = _GreStatusRemoteNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 11, 1, 2, 1)
)
greStatusRemoteNetworkEntry.setIndexNames(
    (0, "GRE", "greStatusId"),
    (0, "GRE", "greStatusRemoteNetworkId"),
)
if mibBuilder.loadTexts:
    greStatusRemoteNetworkEntry.setStatus("current")
_GreStatusRemoteNetworkId_Type = Integer32
_GreStatusRemoteNetworkId_Object = MibTableColumn
greStatusRemoteNetworkId = _GreStatusRemoteNetworkId_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 11, 1, 2, 1, 1),
    _GreStatusRemoteNetworkId_Type()
)
greStatusRemoteNetworkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    greStatusRemoteNetworkId.setStatus("current")
_GreStatusRemoteNetwork_Type = IpAddress
_GreStatusRemoteNetwork_Object = MibTableColumn
greStatusRemoteNetwork = _GreStatusRemoteNetwork_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 11, 1, 2, 1, 2),
    _GreStatusRemoteNetwork_Type()
)
greStatusRemoteNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    greStatusRemoteNetwork.setStatus("current")
_GreStatusRemoteSubnet_Type = IpAddress
_GreStatusRemoteSubnet_Object = MibTableColumn
greStatusRemoteSubnet = _GreStatusRemoteSubnet_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 11, 1, 2, 1, 3),
    _GreStatusRemoteSubnet_Type()
)
greStatusRemoteSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    greStatusRemoteSubnet.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GRE",
    **{"peplink": peplink,
       "productMib": productMib,
       "generalMib": generalMib,
       "greMib": greMib,
       "greInfo": greInfo,
       "greStatusTable": greStatusTable,
       "greStatusEntry": greStatusEntry,
       "greStatusId": greStatusId,
       "greStatusProfileName": greStatusProfileName,
       "greStatusConnectionState": greStatusConnectionState,
       "greStatusLocalIpAddress": greStatusLocalIpAddress,
       "greStatusRemoteIpAddress": greStatusRemoteIpAddress,
       "greStatusTunnelLocalIpAddress": greStatusTunnelLocalIpAddress,
       "greStatusTunnelRemoteIpAddress": greStatusTunnelRemoteIpAddress,
       "greStatusRemoteNetworkTable": greStatusRemoteNetworkTable,
       "greStatusRemoteNetworkEntry": greStatusRemoteNetworkEntry,
       "greStatusRemoteNetworkId": greStatusRemoteNetworkId,
       "greStatusRemoteNetwork": greStatusRemoteNetwork,
       "greStatusRemoteSubnet": greStatusRemoteSubnet}
)
