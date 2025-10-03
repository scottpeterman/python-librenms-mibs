# SNMP MIB module (HH3C-SAVA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-SAVA-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:32:50 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddressType,
 InetVersion) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressType",
    "InetVersion")

(Ipv6AddressPrefix,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6AddressPrefix")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hh3cSava = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 191)
)
if mibBuilder.loadTexts:
    hh3cSava.setRevisions(
        ("2020-06-30 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Hh3cSavaOwnerString(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_Hh3cSavaObjects_ObjectIdentity = ObjectIdentity
hh3cSavaObjects = _Hh3cSavaObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 191, 1)
)
_Hh3cSavaSystemTable_Object = MibTable
hh3cSavaSystemTable = _Hh3cSavaSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 191, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cSavaSystemTable.setStatus("current")
_Hh3cSavaSystemEntry_Object = MibTableRow
hh3cSavaSystemEntry = _Hh3cSavaSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 191, 1, 1, 1)
)
hh3cSavaSystemEntry.setIndexNames(
    (0, "HH3C-SAVA-MIB", "hh3cSavaSystemIPVersion"),
)
if mibBuilder.loadTexts:
    hh3cSavaSystemEntry.setStatus("current")
_Hh3cSavaSystemIPVersion_Type = InetVersion
_Hh3cSavaSystemIPVersion_Object = MibTableColumn
hh3cSavaSystemIPVersion = _Hh3cSavaSystemIPVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 191, 1, 1, 1, 1),
    _Hh3cSavaSystemIPVersion_Type()
)
hh3cSavaSystemIPVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSavaSystemIPVersion.setStatus("current")
_Hh3cSavaSystemNotify_Type = TruthValue
_Hh3cSavaSystemNotify_Object = MibTableColumn
hh3cSavaSystemNotify = _Hh3cSavaSystemNotify_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 191, 1, 1, 1, 2),
    _Hh3cSavaSystemNotify_Type()
)
hh3cSavaSystemNotify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSavaSystemNotify.setStatus("current")


class _Hh3cSavaSystemNotifyInterval_Type(Unsigned32):
    """Custom type hh3cSavaSystemNotifyInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 3600),
    )


_Hh3cSavaSystemNotifyInterval_Type.__name__ = "Unsigned32"
_Hh3cSavaSystemNotifyInterval_Object = MibTableColumn
hh3cSavaSystemNotifyInterval = _Hh3cSavaSystemNotifyInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 191, 1, 1, 1, 3),
    _Hh3cSavaSystemNotifyInterval_Type()
)
hh3cSavaSystemNotifyInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSavaSystemNotifyInterval.setStatus("current")


class _Hh3cSavaSystemNotifyNumber_Type(Unsigned32):
    """Custom type hh3cSavaSystemNotifyNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Hh3cSavaSystemNotifyNumber_Type.__name__ = "Unsigned32"
_Hh3cSavaSystemNotifyNumber_Object = MibTableColumn
hh3cSavaSystemNotifyNumber = _Hh3cSavaSystemNotifyNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 191, 1, 1, 1, 4),
    _Hh3cSavaSystemNotifyNumber_Type()
)
hh3cSavaSystemNotifyNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSavaSystemNotifyNumber.setStatus("current")
_Hh3cSavaIfTable_Object = MibTable
hh3cSavaIfTable = _Hh3cSavaIfTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 191, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cSavaIfTable.setStatus("current")
_Hh3cSavaIfEntry_Object = MibTableRow
hh3cSavaIfEntry = _Hh3cSavaIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 191, 1, 2, 1)
)
hh3cSavaIfEntry.setIndexNames(
    (0, "HH3C-SAVA-MIB", "hh3cSavaIfIPVersion"),
    (0, "HH3C-SAVA-MIB", "hh3cSavaIfIndex"),
)
if mibBuilder.loadTexts:
    hh3cSavaIfEntry.setStatus("current")
_Hh3cSavaIfIPVersion_Type = InetVersion
_Hh3cSavaIfIPVersion_Object = MibTableColumn
hh3cSavaIfIPVersion = _Hh3cSavaIfIPVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 191, 1, 2, 1, 1),
    _Hh3cSavaIfIPVersion_Type()
)
hh3cSavaIfIPVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSavaIfIPVersion.setStatus("current")
_Hh3cSavaIfIndex_Type = InterfaceIndex
_Hh3cSavaIfIndex_Object = MibTableColumn
hh3cSavaIfIndex = _Hh3cSavaIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 191, 1, 2, 1, 2),
    _Hh3cSavaIfIndex_Type()
)
hh3cSavaIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSavaIfIndex.setStatus("current")
_Hh3cSavaIfEnable_Type = TruthValue
_Hh3cSavaIfEnable_Object = MibTableColumn
hh3cSavaIfEnable = _Hh3cSavaIfEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 191, 1, 2, 1, 3),
    _Hh3cSavaIfEnable_Type()
)
hh3cSavaIfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSavaIfEnable.setStatus("current")
_Hh3cSavaIfRemoteRoutetag_Type = Unsigned32
_Hh3cSavaIfRemoteRoutetag_Object = MibTableColumn
hh3cSavaIfRemoteRoutetag = _Hh3cSavaIfRemoteRoutetag_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 191, 1, 2, 1, 4),
    _Hh3cSavaIfRemoteRoutetag_Type()
)
hh3cSavaIfRemoteRoutetag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSavaIfRemoteRoutetag.setStatus("current")
_Hh3cSavaIfAccessSubnet_Type = Hh3cSavaOwnerString
_Hh3cSavaIfAccessSubnet_Object = MibTableColumn
hh3cSavaIfAccessSubnet = _Hh3cSavaIfAccessSubnet_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 191, 1, 2, 1, 5),
    _Hh3cSavaIfAccessSubnet_Type()
)
hh3cSavaIfAccessSubnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSavaIfAccessSubnet.setStatus("current")
_Hh3cSavaPrefixTable_Object = MibTable
hh3cSavaPrefixTable = _Hh3cSavaPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 191, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cSavaPrefixTable.setStatus("current")
_Hh3cSavaPrefixEntry_Object = MibTableRow
hh3cSavaPrefixEntry = _Hh3cSavaPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 191, 1, 3, 1)
)
hh3cSavaPrefixEntry.setIndexNames(
    (0, "HH3C-SAVA-MIB", "hh3cSavaPrefixAddressType"),
    (0, "HH3C-SAVA-MIB", "hh3cSavaPrefixIfIndex"),
    (0, "HH3C-SAVA-MIB", "hh3cSavaPrefixAddress"),
    (0, "HH3C-SAVA-MIB", "hh3cSavaPrefixLength"),
)
if mibBuilder.loadTexts:
    hh3cSavaPrefixEntry.setStatus("current")
_Hh3cSavaPrefixAddressType_Type = InetAddressType
_Hh3cSavaPrefixAddressType_Object = MibTableColumn
hh3cSavaPrefixAddressType = _Hh3cSavaPrefixAddressType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 191, 1, 3, 1, 1),
    _Hh3cSavaPrefixAddressType_Type()
)
hh3cSavaPrefixAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSavaPrefixAddressType.setStatus("current")
_Hh3cSavaPrefixIfIndex_Type = InterfaceIndex
_Hh3cSavaPrefixIfIndex_Object = MibTableColumn
hh3cSavaPrefixIfIndex = _Hh3cSavaPrefixIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 191, 1, 3, 1, 2),
    _Hh3cSavaPrefixIfIndex_Type()
)
hh3cSavaPrefixIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSavaPrefixIfIndex.setStatus("current")
_Hh3cSavaPrefixAddress_Type = Ipv6AddressPrefix
_Hh3cSavaPrefixAddress_Object = MibTableColumn
hh3cSavaPrefixAddress = _Hh3cSavaPrefixAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 191, 1, 3, 1, 3),
    _Hh3cSavaPrefixAddress_Type()
)
hh3cSavaPrefixAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSavaPrefixAddress.setStatus("current")
_Hh3cSavaPrefixLength_Type = Unsigned32
_Hh3cSavaPrefixLength_Object = MibTableColumn
hh3cSavaPrefixLength = _Hh3cSavaPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 191, 1, 3, 1, 4),
    _Hh3cSavaPrefixLength_Type()
)
hh3cSavaPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSavaPrefixLength.setStatus("current")


class _Hh3cSavaPrefixSource_Type(Integer32):
    """Custom type hh3cSavaPrefixSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("localroute", 1),
          ("remoteroute", 2),
          ("otherif", 3))
    )


_Hh3cSavaPrefixSource_Type.__name__ = "Integer32"
_Hh3cSavaPrefixSource_Object = MibTableColumn
hh3cSavaPrefixSource = _Hh3cSavaPrefixSource_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 191, 1, 3, 1, 5),
    _Hh3cSavaPrefixSource_Type()
)
hh3cSavaPrefixSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSavaPrefixSource.setStatus("current")
_Hh3cSavaCountTable_Object = MibTable
hh3cSavaCountTable = _Hh3cSavaCountTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 191, 1, 4)
)
if mibBuilder.loadTexts:
    hh3cSavaCountTable.setStatus("current")
_Hh3cSavaCountEntry_Object = MibTableRow
hh3cSavaCountEntry = _Hh3cSavaCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 191, 1, 4, 1)
)
hh3cSavaCountEntry.setIndexNames(
    (0, "HH3C-SAVA-MIB", "hh3cSavaCountIPVersion"),
    (0, "HH3C-SAVA-MIB", "hh3cSavaCountIfIndex"),
)
if mibBuilder.loadTexts:
    hh3cSavaCountEntry.setStatus("current")
_Hh3cSavaCountIPVersion_Type = InetVersion
_Hh3cSavaCountIPVersion_Object = MibTableColumn
hh3cSavaCountIPVersion = _Hh3cSavaCountIPVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 191, 1, 4, 1, 1),
    _Hh3cSavaCountIPVersion_Type()
)
hh3cSavaCountIPVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSavaCountIPVersion.setStatus("current")
_Hh3cSavaCountIfIndex_Type = InterfaceIndex
_Hh3cSavaCountIfIndex_Object = MibTableColumn
hh3cSavaCountIfIndex = _Hh3cSavaCountIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 191, 1, 4, 1, 2),
    _Hh3cSavaCountIfIndex_Type()
)
hh3cSavaCountIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSavaCountIfIndex.setStatus("current")
_Hh3cSavaCountFilterPkt_Type = Counter64
_Hh3cSavaCountFilterPkt_Object = MibTableColumn
hh3cSavaCountFilterPkt = _Hh3cSavaCountFilterPkt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 191, 1, 4, 1, 3),
    _Hh3cSavaCountFilterPkt_Type()
)
hh3cSavaCountFilterPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSavaCountFilterPkt.setStatus("current")
_Hh3cSavaCountFilterOctets_Type = Counter64
_Hh3cSavaCountFilterOctets_Object = MibTableColumn
hh3cSavaCountFilterOctets = _Hh3cSavaCountFilterOctets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 191, 1, 4, 1, 4),
    _Hh3cSavaCountFilterOctets_Type()
)
hh3cSavaCountFilterOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSavaCountFilterOctets.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-SAVA-MIB",
    **{"Hh3cSavaOwnerString": Hh3cSavaOwnerString,
       "hh3cSava": hh3cSava,
       "hh3cSavaObjects": hh3cSavaObjects,
       "hh3cSavaSystemTable": hh3cSavaSystemTable,
       "hh3cSavaSystemEntry": hh3cSavaSystemEntry,
       "hh3cSavaSystemIPVersion": hh3cSavaSystemIPVersion,
       "hh3cSavaSystemNotify": hh3cSavaSystemNotify,
       "hh3cSavaSystemNotifyInterval": hh3cSavaSystemNotifyInterval,
       "hh3cSavaSystemNotifyNumber": hh3cSavaSystemNotifyNumber,
       "hh3cSavaIfTable": hh3cSavaIfTable,
       "hh3cSavaIfEntry": hh3cSavaIfEntry,
       "hh3cSavaIfIPVersion": hh3cSavaIfIPVersion,
       "hh3cSavaIfIndex": hh3cSavaIfIndex,
       "hh3cSavaIfEnable": hh3cSavaIfEnable,
       "hh3cSavaIfRemoteRoutetag": hh3cSavaIfRemoteRoutetag,
       "hh3cSavaIfAccessSubnet": hh3cSavaIfAccessSubnet,
       "hh3cSavaPrefixTable": hh3cSavaPrefixTable,
       "hh3cSavaPrefixEntry": hh3cSavaPrefixEntry,
       "hh3cSavaPrefixAddressType": hh3cSavaPrefixAddressType,
       "hh3cSavaPrefixIfIndex": hh3cSavaPrefixIfIndex,
       "hh3cSavaPrefixAddress": hh3cSavaPrefixAddress,
       "hh3cSavaPrefixLength": hh3cSavaPrefixLength,
       "hh3cSavaPrefixSource": hh3cSavaPrefixSource,
       "hh3cSavaCountTable": hh3cSavaCountTable,
       "hh3cSavaCountEntry": hh3cSavaCountEntry,
       "hh3cSavaCountIPVersion": hh3cSavaCountIPVersion,
       "hh3cSavaCountIfIndex": hh3cSavaCountIfIndex,
       "hh3cSavaCountFilterPkt": hh3cSavaCountFilterPkt,
       "hh3cSavaCountFilterOctets": hh3cSavaCountFilterOctets}
)
