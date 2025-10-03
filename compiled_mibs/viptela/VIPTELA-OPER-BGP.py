# SNMP MIB module (VIPTELA-OPER-BGP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\viptela\VIPTELA-OPER-BGP
# Produced by pysmi-1.6.2 at Thu Oct  2 12:34:04 2025
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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(viptela,) = mibBuilder.importSymbols(
    "VIPTELA-GLOBAL",
    "viptela")


# MODULE-IDENTITY

viptela_oper_bgp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 14)
)
if mibBuilder.loadTexts:
    viptela_oper_bgp.setRevisions(
        ("2020-07-01 00:00",
         "2020-02-24 00:00",
         "2019-11-15 00:00",
         "2019-08-15 00:00",
         "2018-11-01 00:00",
         "2018-08-20 00:00",
         "2018-06-25 00:00",
         "2018-04-25 00:00",
         "2018-03-15 00:00",
         "2018-01-16 00:00",
         "2017-11-01 00:00",
         "2017-08-01 00:00",
         "2017-05-25 00:00",
         "2017-04-06 00:00",
         "2017-02-15 00:00",
         "2017-02-06 00:00",
         "2016-11-16 00:00",
         "2016-10-25 00:00",
         "2016-10-24 00:00",
         "2016-08-10 00:00",
         "2016-08-01 00:00",
         "2016-06-09 00:00",
         "2016-04-22 00:00",
         "2016-03-15 00:00",
         "2016-01-30 00:00",
         "2015-12-28 00:00",
         "2015-12-01 00:00",
         "2015-10-31 00:00",
         "2015-09-27 00:00",
         "2015-09-01 00:00",
         "2015-07-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class UnsignedShort(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class ConfdString(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class Ipv4Prefix(TextualConvention, OctetString):
    status = "current"
    displayHint = "1d.1d.1d.1d/1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5



class String(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class BgpRibStatusType(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("valid", 0),
          ("best", 1),
          ("internal", 2),
          ("external", 3),
          ("removed", 4),
          ("stale", 5),
          ("history", 6),
          ("damped", 7),
          ("inaccessible", 8),
          ("multipath", 9))
    )


# MIB Managed Objects in the order of their OIDs

_Bgp_ObjectIdentity = ObjectIdentity
bgp = _Bgp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 14, 1)
)
_BgpBgpSummaryTable_Object = MibTable
bgpBgpSummaryTable = _BgpBgpSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 2)
)
if mibBuilder.loadTexts:
    bgpBgpSummaryTable.setStatus("current")
_BgpBgpSummaryEntry_Object = MibTableRow
bgpBgpSummaryEntry = _BgpBgpSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 2, 1)
)
bgpBgpSummaryEntry.setIndexNames(
    (0, "VIPTELA-OPER-BGP", "bgpBgpSummaryVpnId"),
)
if mibBuilder.loadTexts:
    bgpBgpSummaryEntry.setStatus("current")


class _BgpBgpSummaryVpnId_Type(Unsigned32):
    """Custom type bgpBgpSummaryVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_BgpBgpSummaryVpnId_Type.__name__ = "Unsigned32"
_BgpBgpSummaryVpnId_Object = MibTableColumn
bgpBgpSummaryVpnId = _BgpBgpSummaryVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 2, 1, 1),
    _BgpBgpSummaryVpnId_Type()
)
bgpBgpSummaryVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpBgpSummaryVpnId.setStatus("current")
_BgpBgpSummaryBgpRouterIdentifier_Type = IpAddress
_BgpBgpSummaryBgpRouterIdentifier_Object = MibTableColumn
bgpBgpSummaryBgpRouterIdentifier = _BgpBgpSummaryBgpRouterIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 2, 1, 2),
    _BgpBgpSummaryBgpRouterIdentifier_Type()
)
bgpBgpSummaryBgpRouterIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpSummaryBgpRouterIdentifier.setStatus("current")
_BgpBgpSummaryLocalAs_Type = Unsigned32
_BgpBgpSummaryLocalAs_Object = MibTableColumn
bgpBgpSummaryLocalAs = _BgpBgpSummaryLocalAs_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 2, 1, 3),
    _BgpBgpSummaryLocalAs_Type()
)
bgpBgpSummaryLocalAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpSummaryLocalAs.setStatus("current")
_BgpBgpSummaryRibEntries_Type = Unsigned32
_BgpBgpSummaryRibEntries_Object = MibTableColumn
bgpBgpSummaryRibEntries = _BgpBgpSummaryRibEntries_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 2, 1, 4),
    _BgpBgpSummaryRibEntries_Type()
)
bgpBgpSummaryRibEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpSummaryRibEntries.setStatus("current")
_BgpBgpSummaryRibMemory_Type = Unsigned32
_BgpBgpSummaryRibMemory_Object = MibTableColumn
bgpBgpSummaryRibMemory = _BgpBgpSummaryRibMemory_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 2, 1, 5),
    _BgpBgpSummaryRibMemory_Type()
)
bgpBgpSummaryRibMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpSummaryRibMemory.setStatus("current")
_BgpBgpSummaryTotalPeers_Type = Unsigned32
_BgpBgpSummaryTotalPeers_Object = MibTableColumn
bgpBgpSummaryTotalPeers = _BgpBgpSummaryTotalPeers_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 2, 1, 6),
    _BgpBgpSummaryTotalPeers_Type()
)
bgpBgpSummaryTotalPeers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpSummaryTotalPeers.setStatus("current")
_BgpBgpSummaryPeerMemory_Type = Unsigned32
_BgpBgpSummaryPeerMemory_Object = MibTableColumn
bgpBgpSummaryPeerMemory = _BgpBgpSummaryPeerMemory_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 2, 1, 7),
    _BgpBgpSummaryPeerMemory_Type()
)
bgpBgpSummaryPeerMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpSummaryPeerMemory.setStatus("current")
_BgpBgpSummaryLocalSiteOfOrigin_Type = String
_BgpBgpSummaryLocalSiteOfOrigin_Object = MibTableColumn
bgpBgpSummaryLocalSiteOfOrigin = _BgpBgpSummaryLocalSiteOfOrigin_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 2, 1, 8),
    _BgpBgpSummaryLocalSiteOfOrigin_Type()
)
bgpBgpSummaryLocalSiteOfOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpSummaryLocalSiteOfOrigin.setStatus("current")
_BgpBgpSummaryIgnoreSiteOfOrigin_Type = TruthValue
_BgpBgpSummaryIgnoreSiteOfOrigin_Object = MibTableColumn
bgpBgpSummaryIgnoreSiteOfOrigin = _BgpBgpSummaryIgnoreSiteOfOrigin_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 2, 1, 9),
    _BgpBgpSummaryIgnoreSiteOfOrigin_Type()
)
bgpBgpSummaryIgnoreSiteOfOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpSummaryIgnoreSiteOfOrigin.setStatus("current")
_BgpBgpSummaryNeighborTable_Object = MibTable
bgpBgpSummaryNeighborTable = _BgpBgpSummaryNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 3)
)
if mibBuilder.loadTexts:
    bgpBgpSummaryNeighborTable.setStatus("current")
_BgpBgpSummaryNeighborEntry_Object = MibTableRow
bgpBgpSummaryNeighborEntry = _BgpBgpSummaryNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 3, 1)
)
bgpBgpSummaryNeighborEntry.setIndexNames(
    (0, "VIPTELA-OPER-BGP", "bgpBgpSummaryVpnId"),
    (0, "VIPTELA-OPER-BGP", "bgpBgpSummaryNeighborPeerAddr"),
)
if mibBuilder.loadTexts:
    bgpBgpSummaryNeighborEntry.setStatus("current")
_BgpBgpSummaryNeighborPeerAddr_Type = IpAddress
_BgpBgpSummaryNeighborPeerAddr_Object = MibTableColumn
bgpBgpSummaryNeighborPeerAddr = _BgpBgpSummaryNeighborPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 3, 1, 1),
    _BgpBgpSummaryNeighborPeerAddr_Type()
)
bgpBgpSummaryNeighborPeerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpBgpSummaryNeighborPeerAddr.setStatus("current")
_BgpBgpSummaryNeighborAs_Type = Unsigned32
_BgpBgpSummaryNeighborAs_Object = MibTableColumn
bgpBgpSummaryNeighborAs = _BgpBgpSummaryNeighborAs_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 3, 1, 2),
    _BgpBgpSummaryNeighborAs_Type()
)
bgpBgpSummaryNeighborAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpSummaryNeighborAs.setStatus("current")
_BgpBgpSummaryNeighborMsgRcvd_Type = Unsigned32
_BgpBgpSummaryNeighborMsgRcvd_Object = MibTableColumn
bgpBgpSummaryNeighborMsgRcvd = _BgpBgpSummaryNeighborMsgRcvd_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 3, 1, 3),
    _BgpBgpSummaryNeighborMsgRcvd_Type()
)
bgpBgpSummaryNeighborMsgRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpSummaryNeighborMsgRcvd.setStatus("current")
_BgpBgpSummaryNeighborMsgSent_Type = Unsigned32
_BgpBgpSummaryNeighborMsgSent_Object = MibTableColumn
bgpBgpSummaryNeighborMsgSent = _BgpBgpSummaryNeighborMsgSent_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 3, 1, 4),
    _BgpBgpSummaryNeighborMsgSent_Type()
)
bgpBgpSummaryNeighborMsgSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpSummaryNeighborMsgSent.setStatus("current")
_BgpBgpSummaryNeighborOutQ_Type = Unsigned32
_BgpBgpSummaryNeighborOutQ_Object = MibTableColumn
bgpBgpSummaryNeighborOutQ = _BgpBgpSummaryNeighborOutQ_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 3, 1, 5),
    _BgpBgpSummaryNeighborOutQ_Type()
)
bgpBgpSummaryNeighborOutQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpSummaryNeighborOutQ.setStatus("current")
_BgpBgpSummaryNeighborPrefixRcvd_Type = Unsigned32
_BgpBgpSummaryNeighborPrefixRcvd_Object = MibTableColumn
bgpBgpSummaryNeighborPrefixRcvd = _BgpBgpSummaryNeighborPrefixRcvd_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 3, 1, 6),
    _BgpBgpSummaryNeighborPrefixRcvd_Type()
)
bgpBgpSummaryNeighborPrefixRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpSummaryNeighborPrefixRcvd.setStatus("current")
_BgpBgpSummaryNeighborPrefixValid_Type = Unsigned32
_BgpBgpSummaryNeighborPrefixValid_Object = MibTableColumn
bgpBgpSummaryNeighborPrefixValid = _BgpBgpSummaryNeighborPrefixValid_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 3, 1, 7),
    _BgpBgpSummaryNeighborPrefixValid_Type()
)
bgpBgpSummaryNeighborPrefixValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpSummaryNeighborPrefixValid.setStatus("current")
_BgpBgpSummaryNeighborPrefixInstalled_Type = Unsigned32
_BgpBgpSummaryNeighborPrefixInstalled_Object = MibTableColumn
bgpBgpSummaryNeighborPrefixInstalled = _BgpBgpSummaryNeighborPrefixInstalled_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 3, 1, 8),
    _BgpBgpSummaryNeighborPrefixInstalled_Type()
)
bgpBgpSummaryNeighborPrefixInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpSummaryNeighborPrefixInstalled.setStatus("current")
_BgpBgpSummaryNeighborUpTime_Type = String
_BgpBgpSummaryNeighborUpTime_Object = MibTableColumn
bgpBgpSummaryNeighborUpTime = _BgpBgpSummaryNeighborUpTime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 3, 1, 9),
    _BgpBgpSummaryNeighborUpTime_Type()
)
bgpBgpSummaryNeighborUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpSummaryNeighborUpTime.setStatus("current")


class _BgpBgpSummaryNeighborState_Type(Integer32):
    """Custom type bgpBgpSummaryNeighborState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("connect", 1),
          ("active", 2),
          ("opensent", 3),
          ("openconfirm", 4),
          ("established", 5),
          ("clearing", 6),
          ("deleted", 7))
    )


_BgpBgpSummaryNeighborState_Type.__name__ = "Integer32"
_BgpBgpSummaryNeighborState_Object = MibTableColumn
bgpBgpSummaryNeighborState = _BgpBgpSummaryNeighborState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 3, 1, 10),
    _BgpBgpSummaryNeighborState_Type()
)
bgpBgpSummaryNeighborState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpSummaryNeighborState.setStatus("current")
_BgpBgpSummaryNeighborLastUpTime_Type = String
_BgpBgpSummaryNeighborLastUpTime_Object = MibTableColumn
bgpBgpSummaryNeighborLastUpTime = _BgpBgpSummaryNeighborLastUpTime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 3, 1, 11),
    _BgpBgpSummaryNeighborLastUpTime_Type()
)
bgpBgpSummaryNeighborLastUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpSummaryNeighborLastUpTime.setStatus("current")
_BgpRoutesTableTable_Object = MibTable
bgpRoutesTableTable = _BgpRoutesTableTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 4)
)
if mibBuilder.loadTexts:
    bgpRoutesTableTable.setStatus("current")
_BgpRoutesTableEntry_Object = MibTableRow
bgpRoutesTableEntry = _BgpRoutesTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 4, 1)
)
bgpRoutesTableEntry.setIndexNames(
    (0, "VIPTELA-OPER-BGP", "bgpRoutesTableVpnId"),
    (0, "VIPTELA-OPER-BGP", "bgpRoutesTablePrefix"),
)
if mibBuilder.loadTexts:
    bgpRoutesTableEntry.setStatus("current")


class _BgpRoutesTableVpnId_Type(Unsigned32):
    """Custom type bgpRoutesTableVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_BgpRoutesTableVpnId_Type.__name__ = "Unsigned32"
_BgpRoutesTableVpnId_Object = MibTableColumn
bgpRoutesTableVpnId = _BgpRoutesTableVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 4, 1, 1),
    _BgpRoutesTableVpnId_Type()
)
bgpRoutesTableVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpRoutesTableVpnId.setStatus("current")
_BgpRoutesTablePrefix_Type = Ipv4Prefix
_BgpRoutesTablePrefix_Object = MibTableColumn
bgpRoutesTablePrefix = _BgpRoutesTablePrefix_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 4, 1, 2),
    _BgpRoutesTablePrefix_Type()
)
bgpRoutesTablePrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpRoutesTablePrefix.setStatus("current")
_BgpRoutesTableBestPath_Type = Unsigned32
_BgpRoutesTableBestPath_Object = MibTableColumn
bgpRoutesTableBestPath = _BgpRoutesTableBestPath_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 4, 1, 3),
    _BgpRoutesTableBestPath_Type()
)
bgpRoutesTableBestPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRoutesTableBestPath.setStatus("current")
_BgpRoutesTableSuppressed_Type = TruthValue
_BgpRoutesTableSuppressed_Object = MibTableColumn
bgpRoutesTableSuppressed = _BgpRoutesTableSuppressed_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 4, 1, 4),
    _BgpRoutesTableSuppressed_Type()
)
bgpRoutesTableSuppressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRoutesTableSuppressed.setStatus("current")
_BgpRoutesTableNoAdvertise_Type = TruthValue
_BgpRoutesTableNoAdvertise_Object = MibTableColumn
bgpRoutesTableNoAdvertise = _BgpRoutesTableNoAdvertise_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 4, 1, 5),
    _BgpRoutesTableNoAdvertise_Type()
)
bgpRoutesTableNoAdvertise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRoutesTableNoAdvertise.setStatus("current")
_BgpRoutesTableNoExport_Type = TruthValue
_BgpRoutesTableNoExport_Object = MibTableColumn
bgpRoutesTableNoExport = _BgpRoutesTableNoExport_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 4, 1, 6),
    _BgpRoutesTableNoExport_Type()
)
bgpRoutesTableNoExport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRoutesTableNoExport.setStatus("current")
_BgpRoutesTableNoLocalAs_Type = TruthValue
_BgpRoutesTableNoLocalAs_Object = MibTableColumn
bgpRoutesTableNoLocalAs = _BgpRoutesTableNoLocalAs_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 4, 1, 7),
    _BgpRoutesTableNoLocalAs_Type()
)
bgpRoutesTableNoLocalAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRoutesTableNoLocalAs.setStatus("current")
_BgpRoutesTableAdvertisedPeersTable_Object = MibTable
bgpRoutesTableAdvertisedPeersTable = _BgpRoutesTableAdvertisedPeersTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 5)
)
if mibBuilder.loadTexts:
    bgpRoutesTableAdvertisedPeersTable.setStatus("current")
_BgpRoutesTableAdvertisedPeersEntry_Object = MibTableRow
bgpRoutesTableAdvertisedPeersEntry = _BgpRoutesTableAdvertisedPeersEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 5, 1)
)
bgpRoutesTableAdvertisedPeersEntry.setIndexNames(
    (0, "VIPTELA-OPER-BGP", "bgpRoutesTableVpnId"),
    (0, "VIPTELA-OPER-BGP", "bgpRoutesTablePrefix"),
    (0, "VIPTELA-OPER-BGP", "bgpRoutesTableAdvertisedPeersPeerIndex"),
)
if mibBuilder.loadTexts:
    bgpRoutesTableAdvertisedPeersEntry.setStatus("current")
_BgpRoutesTableAdvertisedPeersPeerIndex_Type = Unsigned32
_BgpRoutesTableAdvertisedPeersPeerIndex_Object = MibTableColumn
bgpRoutesTableAdvertisedPeersPeerIndex = _BgpRoutesTableAdvertisedPeersPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 5, 1, 1),
    _BgpRoutesTableAdvertisedPeersPeerIndex_Type()
)
bgpRoutesTableAdvertisedPeersPeerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpRoutesTableAdvertisedPeersPeerIndex.setStatus("current")
_BgpRoutesTableAdvertisedPeersPeerAddr_Type = IpAddress
_BgpRoutesTableAdvertisedPeersPeerAddr_Object = MibTableColumn
bgpRoutesTableAdvertisedPeersPeerAddr = _BgpRoutesTableAdvertisedPeersPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 5, 1, 2),
    _BgpRoutesTableAdvertisedPeersPeerAddr_Type()
)
bgpRoutesTableAdvertisedPeersPeerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRoutesTableAdvertisedPeersPeerAddr.setStatus("current")
_BgpRoutesTableInfoTable_Object = MibTable
bgpRoutesTableInfoTable = _BgpRoutesTableInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 6)
)
if mibBuilder.loadTexts:
    bgpRoutesTableInfoTable.setStatus("current")
_BgpRoutesTableInfoEntry_Object = MibTableRow
bgpRoutesTableInfoEntry = _BgpRoutesTableInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 6, 1)
)
bgpRoutesTableInfoEntry.setIndexNames(
    (0, "VIPTELA-OPER-BGP", "bgpRoutesTableVpnId"),
    (0, "VIPTELA-OPER-BGP", "bgpRoutesTablePrefix"),
    (0, "VIPTELA-OPER-BGP", "bgpRoutesTableInfoInfoId"),
)
if mibBuilder.loadTexts:
    bgpRoutesTableInfoEntry.setStatus("current")
_BgpRoutesTableInfoInfoId_Type = Unsigned32
_BgpRoutesTableInfoInfoId_Object = MibTableColumn
bgpRoutesTableInfoInfoId = _BgpRoutesTableInfoInfoId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 6, 1, 1),
    _BgpRoutesTableInfoInfoId_Type()
)
bgpRoutesTableInfoInfoId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpRoutesTableInfoInfoId.setStatus("current")
_BgpRoutesTableInfoNexthop_Type = IpAddress
_BgpRoutesTableInfoNexthop_Object = MibTableColumn
bgpRoutesTableInfoNexthop = _BgpRoutesTableInfoNexthop_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 6, 1, 2),
    _BgpRoutesTableInfoNexthop_Type()
)
bgpRoutesTableInfoNexthop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRoutesTableInfoNexthop.setStatus("current")
_BgpRoutesTableInfoMetric_Type = Unsigned32
_BgpRoutesTableInfoMetric_Object = MibTableColumn
bgpRoutesTableInfoMetric = _BgpRoutesTableInfoMetric_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 6, 1, 3),
    _BgpRoutesTableInfoMetric_Type()
)
bgpRoutesTableInfoMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRoutesTableInfoMetric.setStatus("current")
_BgpRoutesTableInfoLocalPref_Type = Unsigned32
_BgpRoutesTableInfoLocalPref_Object = MibTableColumn
bgpRoutesTableInfoLocalPref = _BgpRoutesTableInfoLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 6, 1, 4),
    _BgpRoutesTableInfoLocalPref_Type()
)
bgpRoutesTableInfoLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRoutesTableInfoLocalPref.setStatus("current")
_BgpRoutesTableInfoWeight_Type = Unsigned32
_BgpRoutesTableInfoWeight_Object = MibTableColumn
bgpRoutesTableInfoWeight = _BgpRoutesTableInfoWeight_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 6, 1, 5),
    _BgpRoutesTableInfoWeight_Type()
)
bgpRoutesTableInfoWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRoutesTableInfoWeight.setStatus("current")


class _BgpRoutesTableInfoOrigin_Type(Integer32):
    """Custom type bgpRoutesTableInfoOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("igp", 0),
          ("egp", 1),
          ("incomplete", 2))
    )


_BgpRoutesTableInfoOrigin_Type.__name__ = "Integer32"
_BgpRoutesTableInfoOrigin_Object = MibTableColumn
bgpRoutesTableInfoOrigin = _BgpRoutesTableInfoOrigin_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 6, 1, 6),
    _BgpRoutesTableInfoOrigin_Type()
)
bgpRoutesTableInfoOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRoutesTableInfoOrigin.setStatus("current")
_BgpRoutesTableInfoAsPath_Type = String
_BgpRoutesTableInfoAsPath_Object = MibTableColumn
bgpRoutesTableInfoAsPath = _BgpRoutesTableInfoAsPath_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 6, 1, 7),
    _BgpRoutesTableInfoAsPath_Type()
)
bgpRoutesTableInfoAsPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRoutesTableInfoAsPath.setStatus("current")
_BgpRoutesTableInfoRrClient_Type = TruthValue
_BgpRoutesTableInfoRrClient_Object = MibTableColumn
bgpRoutesTableInfoRrClient = _BgpRoutesTableInfoRrClient_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 6, 1, 8),
    _BgpRoutesTableInfoRrClient_Type()
)
bgpRoutesTableInfoRrClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRoutesTableInfoRrClient.setStatus("current")
_BgpRoutesTableInfoHistory_Type = TruthValue
_BgpRoutesTableInfoHistory_Object = MibTableColumn
bgpRoutesTableInfoHistory = _BgpRoutesTableInfoHistory_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 6, 1, 9),
    _BgpRoutesTableInfoHistory_Type()
)
bgpRoutesTableInfoHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRoutesTableInfoHistory.setStatus("current")
_BgpRoutesTableInfoAggregator_Type = TruthValue
_BgpRoutesTableInfoAggregator_Object = MibTableColumn
bgpRoutesTableInfoAggregator = _BgpRoutesTableInfoAggregator_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 6, 1, 10),
    _BgpRoutesTableInfoAggregator_Type()
)
bgpRoutesTableInfoAggregator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRoutesTableInfoAggregator.setStatus("current")
_BgpRoutesTableInfoAggregatorAs_Type = Unsigned32
_BgpRoutesTableInfoAggregatorAs_Object = MibTableColumn
bgpRoutesTableInfoAggregatorAs = _BgpRoutesTableInfoAggregatorAs_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 6, 1, 11),
    _BgpRoutesTableInfoAggregatorAs_Type()
)
bgpRoutesTableInfoAggregatorAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRoutesTableInfoAggregatorAs.setStatus("current")
_BgpRoutesTableInfoAggregatorIp_Type = IpAddress
_BgpRoutesTableInfoAggregatorIp_Object = MibTableColumn
bgpRoutesTableInfoAggregatorIp = _BgpRoutesTableInfoAggregatorIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 6, 1, 12),
    _BgpRoutesTableInfoAggregatorIp_Type()
)
bgpRoutesTableInfoAggregatorIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRoutesTableInfoAggregatorIp.setStatus("current")
_BgpRoutesTableInfoRiPeer_Type = IpAddress
_BgpRoutesTableInfoRiPeer_Object = MibTableColumn
bgpRoutesTableInfoRiPeer = _BgpRoutesTableInfoRiPeer_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 6, 1, 13),
    _BgpRoutesTableInfoRiPeer_Type()
)
bgpRoutesTableInfoRiPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRoutesTableInfoRiPeer.setStatus("current")
_BgpRoutesTableInfoRiRouterid_Type = IpAddress
_BgpRoutesTableInfoRiRouterid_Object = MibTableColumn
bgpRoutesTableInfoRiRouterid = _BgpRoutesTableInfoRiRouterid_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 6, 1, 14),
    _BgpRoutesTableInfoRiRouterid_Type()
)
bgpRoutesTableInfoRiRouterid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRoutesTableInfoRiRouterid.setStatus("current")
_BgpRoutesTableInfoIgpMetric_Type = Unsigned32
_BgpRoutesTableInfoIgpMetric_Object = MibTableColumn
bgpRoutesTableInfoIgpMetric = _BgpRoutesTableInfoIgpMetric_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 6, 1, 15),
    _BgpRoutesTableInfoIgpMetric_Type()
)
bgpRoutesTableInfoIgpMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRoutesTableInfoIgpMetric.setStatus("current")
_BgpRoutesTableInfoConfedExternal_Type = TruthValue
_BgpRoutesTableInfoConfedExternal_Object = MibTableColumn
bgpRoutesTableInfoConfedExternal = _BgpRoutesTableInfoConfedExternal_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 6, 1, 16),
    _BgpRoutesTableInfoConfedExternal_Type()
)
bgpRoutesTableInfoConfedExternal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRoutesTableInfoConfedExternal.setStatus("current")
_BgpRoutesTableInfoAggregated_Type = TruthValue
_BgpRoutesTableInfoAggregated_Object = MibTableColumn
bgpRoutesTableInfoAggregated = _BgpRoutesTableInfoAggregated_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 6, 1, 17),
    _BgpRoutesTableInfoAggregated_Type()
)
bgpRoutesTableInfoAggregated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRoutesTableInfoAggregated.setStatus("current")
_BgpRoutesTableInfoLocal_Type = TruthValue
_BgpRoutesTableInfoLocal_Object = MibTableColumn
bgpRoutesTableInfoLocal = _BgpRoutesTableInfoLocal_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 6, 1, 18),
    _BgpRoutesTableInfoLocal_Type()
)
bgpRoutesTableInfoLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRoutesTableInfoLocal.setStatus("current")
_BgpRoutesTableInfoSourced_Type = TruthValue
_BgpRoutesTableInfoSourced_Object = MibTableColumn
bgpRoutesTableInfoSourced = _BgpRoutesTableInfoSourced_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 6, 1, 19),
    _BgpRoutesTableInfoSourced_Type()
)
bgpRoutesTableInfoSourced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRoutesTableInfoSourced.setStatus("current")
_BgpRoutesTableInfoMultipath_Type = TruthValue
_BgpRoutesTableInfoMultipath_Object = MibTableColumn
bgpRoutesTableInfoMultipath = _BgpRoutesTableInfoMultipath_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 6, 1, 20),
    _BgpRoutesTableInfoMultipath_Type()
)
bgpRoutesTableInfoMultipath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRoutesTableInfoMultipath.setStatus("obsolete")


class _BgpRoutesTableInfoCommunity_Type(String):
    """Custom type bgpRoutesTableInfoCommunity based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_BgpRoutesTableInfoCommunity_Type.__name__ = "String"
_BgpRoutesTableInfoCommunity_Object = MibTableColumn
bgpRoutesTableInfoCommunity = _BgpRoutesTableInfoCommunity_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 6, 1, 21),
    _BgpRoutesTableInfoCommunity_Type()
)
bgpRoutesTableInfoCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRoutesTableInfoCommunity.setStatus("current")


class _BgpRoutesTableInfoExtCommunity_Type(String):
    """Custom type bgpRoutesTableInfoExtCommunity based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_BgpRoutesTableInfoExtCommunity_Type.__name__ = "String"
_BgpRoutesTableInfoExtCommunity_Object = MibTableColumn
bgpRoutesTableInfoExtCommunity = _BgpRoutesTableInfoExtCommunity_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 6, 1, 22),
    _BgpRoutesTableInfoExtCommunity_Type()
)
bgpRoutesTableInfoExtCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRoutesTableInfoExtCommunity.setStatus("current")
_BgpRoutesTableInfoOriginator_Type = IpAddress
_BgpRoutesTableInfoOriginator_Object = MibTableColumn
bgpRoutesTableInfoOriginator = _BgpRoutesTableInfoOriginator_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 6, 1, 23),
    _BgpRoutesTableInfoOriginator_Type()
)
bgpRoutesTableInfoOriginator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRoutesTableInfoOriginator.setStatus("current")


class _BgpRoutesTableInfoLastUpdate_Type(String):
    """Custom type bgpRoutesTableInfoLastUpdate based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_BgpRoutesTableInfoLastUpdate_Type.__name__ = "String"
_BgpRoutesTableInfoLastUpdate_Object = MibTableColumn
bgpRoutesTableInfoLastUpdate = _BgpRoutesTableInfoLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 6, 1, 24),
    _BgpRoutesTableInfoLastUpdate_Type()
)
bgpRoutesTableInfoLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRoutesTableInfoLastUpdate.setStatus("current")
_BgpRoutesTableInfoClusterList_Type = String
_BgpRoutesTableInfoClusterList_Object = MibTableColumn
bgpRoutesTableInfoClusterList = _BgpRoutesTableInfoClusterList_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 6, 1, 25),
    _BgpRoutesTableInfoClusterList_Type()
)
bgpRoutesTableInfoClusterList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRoutesTableInfoClusterList.setStatus("current")
_BgpRoutesTableInfoPathStatus_Type = BgpRibStatusType
_BgpRoutesTableInfoPathStatus_Object = MibTableColumn
bgpRoutesTableInfoPathStatus = _BgpRoutesTableInfoPathStatus_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 6, 1, 26),
    _BgpRoutesTableInfoPathStatus_Type()
)
bgpRoutesTableInfoPathStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRoutesTableInfoPathStatus.setStatus("current")
_BgpRoutesTableInfoTag_Type = Unsigned32
_BgpRoutesTableInfoTag_Object = MibTableColumn
bgpRoutesTableInfoTag = _BgpRoutesTableInfoTag_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 6, 1, 27),
    _BgpRoutesTableInfoTag_Type()
)
bgpRoutesTableInfoTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRoutesTableInfoTag.setStatus("current")
_BgpRoutesTableInfoOspfTag_Type = Unsigned32
_BgpRoutesTableInfoOspfTag_Object = MibTableColumn
bgpRoutesTableInfoOspfTag = _BgpRoutesTableInfoOspfTag_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 6, 1, 28),
    _BgpRoutesTableInfoOspfTag_Type()
)
bgpRoutesTableInfoOspfTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRoutesTableInfoOspfTag.setStatus("current")
_BgpBgpNeighborTable_Object = MibTable
bgpBgpNeighborTable = _BgpBgpNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9)
)
if mibBuilder.loadTexts:
    bgpBgpNeighborTable.setStatus("current")
_BgpBgpNeighborEntry_Object = MibTableRow
bgpBgpNeighborEntry = _BgpBgpNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1)
)
bgpBgpNeighborEntry.setIndexNames(
    (0, "VIPTELA-OPER-BGP", "bgpBgpNeighborVpnId"),
    (0, "VIPTELA-OPER-BGP", "bgpBgpNeighborPeerAddr"),
)
if mibBuilder.loadTexts:
    bgpBgpNeighborEntry.setStatus("current")


class _BgpBgpNeighborVpnId_Type(Unsigned32):
    """Custom type bgpBgpNeighborVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_BgpBgpNeighborVpnId_Type.__name__ = "Unsigned32"
_BgpBgpNeighborVpnId_Object = MibTableColumn
bgpBgpNeighborVpnId = _BgpBgpNeighborVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 1),
    _BgpBgpNeighborVpnId_Type()
)
bgpBgpNeighborVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpBgpNeighborVpnId.setStatus("current")
_BgpBgpNeighborPeerAddr_Type = IpAddress
_BgpBgpNeighborPeerAddr_Object = MibTableColumn
bgpBgpNeighborPeerAddr = _BgpBgpNeighborPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 2),
    _BgpBgpNeighborPeerAddr_Type()
)
bgpBgpNeighborPeerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpBgpNeighborPeerAddr.setStatus("current")
_BgpBgpNeighborAs_Type = Unsigned32
_BgpBgpNeighborAs_Object = MibTableColumn
bgpBgpNeighborAs = _BgpBgpNeighborAs_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 3),
    _BgpBgpNeighborAs_Type()
)
bgpBgpNeighborAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborAs.setStatus("current")
_BgpBgpNeighborLocalAsNum_Type = Unsigned32
_BgpBgpNeighborLocalAsNum_Object = MibTableColumn
bgpBgpNeighborLocalAsNum = _BgpBgpNeighborLocalAsNum_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 4),
    _BgpBgpNeighborLocalAsNum_Type()
)
bgpBgpNeighborLocalAsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborLocalAsNum.setStatus("current")
_BgpBgpNeighborChangeLocalAsNum_Type = TruthValue
_BgpBgpNeighborChangeLocalAsNum_Object = MibTableColumn
bgpBgpNeighborChangeLocalAsNum = _BgpBgpNeighborChangeLocalAsNum_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 5),
    _BgpBgpNeighborChangeLocalAsNum_Type()
)
bgpBgpNeighborChangeLocalAsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborChangeLocalAsNum.setStatus("current")
_BgpBgpNeighborFlags_Type = Unsigned32
_BgpBgpNeighborFlags_Object = MibTableColumn
bgpBgpNeighborFlags = _BgpBgpNeighborFlags_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 6),
    _BgpBgpNeighborFlags_Type()
)
bgpBgpNeighborFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborFlags.setStatus("current")


class _BgpBgpNeighborDesc_Type(String):
    """Custom type bgpBgpNeighborDesc based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_BgpBgpNeighborDesc_Type.__name__ = "String"
_BgpBgpNeighborDesc_Object = MibTableColumn
bgpBgpNeighborDesc = _BgpBgpNeighborDesc_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 7),
    _BgpBgpNeighborDesc_Type()
)
bgpBgpNeighborDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborDesc.setStatus("current")
_BgpBgpNeighborRemoteRouterId_Type = IpAddress
_BgpBgpNeighborRemoteRouterId_Object = MibTableColumn
bgpBgpNeighborRemoteRouterId = _BgpBgpNeighborRemoteRouterId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 8),
    _BgpBgpNeighborRemoteRouterId_Type()
)
bgpBgpNeighborRemoteRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborRemoteRouterId.setStatus("current")
_BgpBgpNeighborCommonAdmin_Type = TruthValue
_BgpBgpNeighborCommonAdmin_Object = MibTableColumn
bgpBgpNeighborCommonAdmin = _BgpBgpNeighborCommonAdmin_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 9),
    _BgpBgpNeighborCommonAdmin_Type()
)
bgpBgpNeighborCommonAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborCommonAdmin.setStatus("current")
_BgpBgpNeighborLastRead_Type = Unsigned32
_BgpBgpNeighborLastRead_Object = MibTableColumn
bgpBgpNeighborLastRead = _BgpBgpNeighborLastRead_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 10),
    _BgpBgpNeighborLastRead_Type()
)
bgpBgpNeighborLastRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborLastRead.setStatus("current")
_BgpBgpNeighborKeepalive_Type = Unsigned32
_BgpBgpNeighborKeepalive_Object = MibTableColumn
bgpBgpNeighborKeepalive = _BgpBgpNeighborKeepalive_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 11),
    _BgpBgpNeighborKeepalive_Type()
)
bgpBgpNeighborKeepalive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborKeepalive.setStatus("current")
_BgpBgpNeighborHoldtime_Type = Unsigned32
_BgpBgpNeighborHoldtime_Object = MibTableColumn
bgpBgpNeighborHoldtime = _BgpBgpNeighborHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 12),
    _BgpBgpNeighborHoldtime_Type()
)
bgpBgpNeighborHoldtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborHoldtime.setStatus("current")
_BgpBgpNeighborCfgKeepalive_Type = Unsigned32
_BgpBgpNeighborCfgKeepalive_Object = MibTableColumn
bgpBgpNeighborCfgKeepalive = _BgpBgpNeighborCfgKeepalive_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 13),
    _BgpBgpNeighborCfgKeepalive_Type()
)
bgpBgpNeighborCfgKeepalive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborCfgKeepalive.setStatus("current")
_BgpBgpNeighborCfgHoldtime_Type = Unsigned32
_BgpBgpNeighborCfgHoldtime_Object = MibTableColumn
bgpBgpNeighborCfgHoldtime = _BgpBgpNeighborCfgHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 14),
    _BgpBgpNeighborCfgHoldtime_Type()
)
bgpBgpNeighborCfgHoldtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborCfgHoldtime.setStatus("current")
_BgpBgpNeighborAdv4byteAsCap_Type = TruthValue
_BgpBgpNeighborAdv4byteAsCap_Object = MibTableColumn
bgpBgpNeighborAdv4byteAsCap = _BgpBgpNeighborAdv4byteAsCap_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 15),
    _BgpBgpNeighborAdv4byteAsCap_Type()
)
bgpBgpNeighborAdv4byteAsCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborAdv4byteAsCap.setStatus("current")
_BgpBgpNeighborRec4byteAsCap_Type = TruthValue
_BgpBgpNeighborRec4byteAsCap_Object = MibTableColumn
bgpBgpNeighborRec4byteAsCap = _BgpBgpNeighborRec4byteAsCap_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 16),
    _BgpBgpNeighborRec4byteAsCap_Type()
)
bgpBgpNeighborRec4byteAsCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborRec4byteAsCap.setStatus("current")
_BgpBgpNeighborAdvDynamicCap_Type = TruthValue
_BgpBgpNeighborAdvDynamicCap_Object = MibTableColumn
bgpBgpNeighborAdvDynamicCap = _BgpBgpNeighborAdvDynamicCap_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 17),
    _BgpBgpNeighborAdvDynamicCap_Type()
)
bgpBgpNeighborAdvDynamicCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborAdvDynamicCap.setStatus("current")
_BgpBgpNeighborRecDynamicCap_Type = TruthValue
_BgpBgpNeighborRecDynamicCap_Object = MibTableColumn
bgpBgpNeighborRecDynamicCap = _BgpBgpNeighborRecDynamicCap_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 18),
    _BgpBgpNeighborRecDynamicCap_Type()
)
bgpBgpNeighborRecDynamicCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborRecDynamicCap.setStatus("current")
_BgpBgpNeighborAdvRefreshCap_Type = TruthValue
_BgpBgpNeighborAdvRefreshCap_Object = MibTableColumn
bgpBgpNeighborAdvRefreshCap = _BgpBgpNeighborAdvRefreshCap_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 19),
    _BgpBgpNeighborAdvRefreshCap_Type()
)
bgpBgpNeighborAdvRefreshCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborAdvRefreshCap.setStatus("current")
_BgpBgpNeighborRecRefreshCap_Type = TruthValue
_BgpBgpNeighborRecRefreshCap_Object = MibTableColumn
bgpBgpNeighborRecRefreshCap = _BgpBgpNeighborRecRefreshCap_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 20),
    _BgpBgpNeighborRecRefreshCap_Type()
)
bgpBgpNeighborRecRefreshCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborRecRefreshCap.setStatus("current")
_BgpBgpNeighborAdvNewRefreshCap_Type = TruthValue
_BgpBgpNeighborAdvNewRefreshCap_Object = MibTableColumn
bgpBgpNeighborAdvNewRefreshCap = _BgpBgpNeighborAdvNewRefreshCap_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 21),
    _BgpBgpNeighborAdvNewRefreshCap_Type()
)
bgpBgpNeighborAdvNewRefreshCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborAdvNewRefreshCap.setStatus("current")
_BgpBgpNeighborRecNewRefreshCap_Type = TruthValue
_BgpBgpNeighborRecNewRefreshCap_Object = MibTableColumn
bgpBgpNeighborRecNewRefreshCap = _BgpBgpNeighborRecNewRefreshCap_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 22),
    _BgpBgpNeighborRecNewRefreshCap_Type()
)
bgpBgpNeighborRecNewRefreshCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborRecNewRefreshCap.setStatus("current")
_BgpBgpNeighborAdvIpv4UnicastAddrFamily_Type = TruthValue
_BgpBgpNeighborAdvIpv4UnicastAddrFamily_Object = MibTableColumn
bgpBgpNeighborAdvIpv4UnicastAddrFamily = _BgpBgpNeighborAdvIpv4UnicastAddrFamily_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 23),
    _BgpBgpNeighborAdvIpv4UnicastAddrFamily_Type()
)
bgpBgpNeighborAdvIpv4UnicastAddrFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborAdvIpv4UnicastAddrFamily.setStatus("current")
_BgpBgpNeighborRecIpv4UnicastAddrFamily_Type = TruthValue
_BgpBgpNeighborRecIpv4UnicastAddrFamily_Object = MibTableColumn
bgpBgpNeighborRecIpv4UnicastAddrFamily = _BgpBgpNeighborRecIpv4UnicastAddrFamily_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 24),
    _BgpBgpNeighborRecIpv4UnicastAddrFamily_Type()
)
bgpBgpNeighborRecIpv4UnicastAddrFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborRecIpv4UnicastAddrFamily.setStatus("current")
_BgpBgpNeighborRestartTimeLeft_Type = Unsigned32
_BgpBgpNeighborRestartTimeLeft_Object = MibTableColumn
bgpBgpNeighborRestartTimeLeft = _BgpBgpNeighborRestartTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 25),
    _BgpBgpNeighborRestartTimeLeft_Type()
)
bgpBgpNeighborRestartTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborRestartTimeLeft.setStatus("current")
_BgpBgpNeighborStalepathTimeLeft_Type = Unsigned32
_BgpBgpNeighborStalepathTimeLeft_Object = MibTableColumn
bgpBgpNeighborStalepathTimeLeft = _BgpBgpNeighborStalepathTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 26),
    _BgpBgpNeighborStalepathTimeLeft_Type()
)
bgpBgpNeighborStalepathTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborStalepathTimeLeft.setStatus("current")
_BgpBgpNeighborMsgRcvd_Type = Unsigned32
_BgpBgpNeighborMsgRcvd_Object = MibTableColumn
bgpBgpNeighborMsgRcvd = _BgpBgpNeighborMsgRcvd_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 27),
    _BgpBgpNeighborMsgRcvd_Type()
)
bgpBgpNeighborMsgRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborMsgRcvd.setStatus("current")
_BgpBgpNeighborMsgSent_Type = Unsigned32
_BgpBgpNeighborMsgSent_Object = MibTableColumn
bgpBgpNeighborMsgSent = _BgpBgpNeighborMsgSent_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 28),
    _BgpBgpNeighborMsgSent_Type()
)
bgpBgpNeighborMsgSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborMsgSent.setStatus("current")
_BgpBgpNeighborPrefixRcvd_Type = Unsigned32
_BgpBgpNeighborPrefixRcvd_Object = MibTableColumn
bgpBgpNeighborPrefixRcvd = _BgpBgpNeighborPrefixRcvd_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 29),
    _BgpBgpNeighborPrefixRcvd_Type()
)
bgpBgpNeighborPrefixRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborPrefixRcvd.setStatus("current")
_BgpBgpNeighborPrefixValid_Type = Unsigned32
_BgpBgpNeighborPrefixValid_Object = MibTableColumn
bgpBgpNeighborPrefixValid = _BgpBgpNeighborPrefixValid_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 30),
    _BgpBgpNeighborPrefixValid_Type()
)
bgpBgpNeighborPrefixValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborPrefixValid.setStatus("current")
_BgpBgpNeighborPrefixInstalled_Type = Unsigned32
_BgpBgpNeighborPrefixInstalled_Object = MibTableColumn
bgpBgpNeighborPrefixInstalled = _BgpBgpNeighborPrefixInstalled_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 31),
    _BgpBgpNeighborPrefixInstalled_Type()
)
bgpBgpNeighborPrefixInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborPrefixInstalled.setStatus("current")
_BgpBgpNeighborOutQ_Type = Unsigned32
_BgpBgpNeighborOutQ_Object = MibTableColumn
bgpBgpNeighborOutQ = _BgpBgpNeighborOutQ_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 32),
    _BgpBgpNeighborOutQ_Type()
)
bgpBgpNeighborOutQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborOutQ.setStatus("current")
_BgpBgpNeighborUptime_Type = String
_BgpBgpNeighborUptime_Object = MibTableColumn
bgpBgpNeighborUptime = _BgpBgpNeighborUptime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 33),
    _BgpBgpNeighborUptime_Type()
)
bgpBgpNeighborUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborUptime.setStatus("current")


class _BgpBgpNeighborState_Type(Integer32):
    """Custom type bgpBgpNeighborState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("connect", 1),
          ("active", 2),
          ("opensent", 3),
          ("openconfirm", 4),
          ("established", 5),
          ("clearing", 6),
          ("deleted", 7))
    )


_BgpBgpNeighborState_Type.__name__ = "Integer32"
_BgpBgpNeighborState_Object = MibTableColumn
bgpBgpNeighborState = _BgpBgpNeighborState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 34),
    _BgpBgpNeighborState_Type()
)
bgpBgpNeighborState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborState.setStatus("current")
_BgpBgpNeighborOpenInCount_Type = Unsigned32
_BgpBgpNeighborOpenInCount_Object = MibTableColumn
bgpBgpNeighborOpenInCount = _BgpBgpNeighborOpenInCount_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 35),
    _BgpBgpNeighborOpenInCount_Type()
)
bgpBgpNeighborOpenInCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborOpenInCount.setStatus("current")
_BgpBgpNeighborOpenOutCount_Type = Unsigned32
_BgpBgpNeighborOpenOutCount_Object = MibTableColumn
bgpBgpNeighborOpenOutCount = _BgpBgpNeighborOpenOutCount_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 36),
    _BgpBgpNeighborOpenOutCount_Type()
)
bgpBgpNeighborOpenOutCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborOpenOutCount.setStatus("current")
_BgpBgpNeighborNotifyInCount_Type = Unsigned32
_BgpBgpNeighborNotifyInCount_Object = MibTableColumn
bgpBgpNeighborNotifyInCount = _BgpBgpNeighborNotifyInCount_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 37),
    _BgpBgpNeighborNotifyInCount_Type()
)
bgpBgpNeighborNotifyInCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborNotifyInCount.setStatus("current")
_BgpBgpNeighborNotifyOutCount_Type = Unsigned32
_BgpBgpNeighborNotifyOutCount_Object = MibTableColumn
bgpBgpNeighborNotifyOutCount = _BgpBgpNeighborNotifyOutCount_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 38),
    _BgpBgpNeighborNotifyOutCount_Type()
)
bgpBgpNeighborNotifyOutCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborNotifyOutCount.setStatus("current")
_BgpBgpNeighborUpdateInCount_Type = Unsigned32
_BgpBgpNeighborUpdateInCount_Object = MibTableColumn
bgpBgpNeighborUpdateInCount = _BgpBgpNeighborUpdateInCount_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 39),
    _BgpBgpNeighborUpdateInCount_Type()
)
bgpBgpNeighborUpdateInCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborUpdateInCount.setStatus("current")
_BgpBgpNeighborUpdateOutCount_Type = Unsigned32
_BgpBgpNeighborUpdateOutCount_Object = MibTableColumn
bgpBgpNeighborUpdateOutCount = _BgpBgpNeighborUpdateOutCount_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 40),
    _BgpBgpNeighborUpdateOutCount_Type()
)
bgpBgpNeighborUpdateOutCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborUpdateOutCount.setStatus("current")
_BgpBgpNeighborKeepaliveInCount_Type = Unsigned32
_BgpBgpNeighborKeepaliveInCount_Object = MibTableColumn
bgpBgpNeighborKeepaliveInCount = _BgpBgpNeighborKeepaliveInCount_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 41),
    _BgpBgpNeighborKeepaliveInCount_Type()
)
bgpBgpNeighborKeepaliveInCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborKeepaliveInCount.setStatus("current")
_BgpBgpNeighborKeepaliveOutCount_Type = Unsigned32
_BgpBgpNeighborKeepaliveOutCount_Object = MibTableColumn
bgpBgpNeighborKeepaliveOutCount = _BgpBgpNeighborKeepaliveOutCount_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 42),
    _BgpBgpNeighborKeepaliveOutCount_Type()
)
bgpBgpNeighborKeepaliveOutCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborKeepaliveOutCount.setStatus("current")
_BgpBgpNeighborRefreshInCount_Type = Unsigned32
_BgpBgpNeighborRefreshInCount_Object = MibTableColumn
bgpBgpNeighborRefreshInCount = _BgpBgpNeighborRefreshInCount_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 43),
    _BgpBgpNeighborRefreshInCount_Type()
)
bgpBgpNeighborRefreshInCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborRefreshInCount.setStatus("current")
_BgpBgpNeighborRefreshOutCount_Type = Unsigned32
_BgpBgpNeighborRefreshOutCount_Object = MibTableColumn
bgpBgpNeighborRefreshOutCount = _BgpBgpNeighborRefreshOutCount_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 44),
    _BgpBgpNeighborRefreshOutCount_Type()
)
bgpBgpNeighborRefreshOutCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborRefreshOutCount.setStatus("current")
_BgpBgpNeighborDynamicInCount_Type = Unsigned32
_BgpBgpNeighborDynamicInCount_Object = MibTableColumn
bgpBgpNeighborDynamicInCount = _BgpBgpNeighborDynamicInCount_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 45),
    _BgpBgpNeighborDynamicInCount_Type()
)
bgpBgpNeighborDynamicInCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborDynamicInCount.setStatus("current")
_BgpBgpNeighborDynamicOutCount_Type = Unsigned32
_BgpBgpNeighborDynamicOutCount_Object = MibTableColumn
bgpBgpNeighborDynamicOutCount = _BgpBgpNeighborDynamicOutCount_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 46),
    _BgpBgpNeighborDynamicOutCount_Type()
)
bgpBgpNeighborDynamicOutCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborDynamicOutCount.setStatus("current")
_BgpBgpNeighborAdvInterval_Type = Unsigned32
_BgpBgpNeighborAdvInterval_Object = MibTableColumn
bgpBgpNeighborAdvInterval = _BgpBgpNeighborAdvInterval_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 47),
    _BgpBgpNeighborAdvInterval_Type()
)
bgpBgpNeighborAdvInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborAdvInterval.setStatus("current")
_BgpBgpNeighborUpdateSource_Type = IpAddress
_BgpBgpNeighborUpdateSource_Object = MibTableColumn
bgpBgpNeighborUpdateSource = _BgpBgpNeighborUpdateSource_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 48),
    _BgpBgpNeighborUpdateSource_Type()
)
bgpBgpNeighborUpdateSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborUpdateSource.setStatus("current")


class _BgpBgpNeighborUpdateIf_Type(String):
    """Custom type bgpBgpNeighborUpdateIf based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_BgpBgpNeighborUpdateIf_Type.__name__ = "String"
_BgpBgpNeighborUpdateIf_Object = MibTableColumn
bgpBgpNeighborUpdateIf = _BgpBgpNeighborUpdateIf_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 49),
    _BgpBgpNeighborUpdateIf_Type()
)
bgpBgpNeighborUpdateIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborUpdateIf.setStatus("current")
_BgpBgpNeighborWeight_Type = Unsigned32
_BgpBgpNeighborWeight_Object = MibTableColumn
bgpBgpNeighborWeight = _BgpBgpNeighborWeight_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 50),
    _BgpBgpNeighborWeight_Type()
)
bgpBgpNeighborWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborWeight.setStatus("current")
_BgpBgpNeighborConnEstablished_Type = Unsigned32
_BgpBgpNeighborConnEstablished_Object = MibTableColumn
bgpBgpNeighborConnEstablished = _BgpBgpNeighborConnEstablished_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 51),
    _BgpBgpNeighborConnEstablished_Type()
)
bgpBgpNeighborConnEstablished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborConnEstablished.setStatus("current")
_BgpBgpNeighborConnDropped_Type = Unsigned32
_BgpBgpNeighborConnDropped_Object = MibTableColumn
bgpBgpNeighborConnDropped = _BgpBgpNeighborConnDropped_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 52),
    _BgpBgpNeighborConnDropped_Type()
)
bgpBgpNeighborConnDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborConnDropped.setStatus("current")
_BgpBgpNeighborLastResetTime_Type = Unsigned32
_BgpBgpNeighborLastResetTime_Object = MibTableColumn
bgpBgpNeighborLastResetTime = _BgpBgpNeighborLastResetTime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 53),
    _BgpBgpNeighborLastResetTime_Type()
)
bgpBgpNeighborLastResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborLastResetTime.setStatus("current")


class _BgpBgpNeighborLastResetReason_Type(String):
    """Custom type bgpBgpNeighborLastResetReason based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_BgpBgpNeighborLastResetReason_Type.__name__ = "String"
_BgpBgpNeighborLastResetReason_Object = MibTableColumn
bgpBgpNeighborLastResetReason = _BgpBgpNeighborLastResetReason_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 54),
    _BgpBgpNeighborLastResetReason_Type()
)
bgpBgpNeighborLastResetReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborLastResetReason.setStatus("current")
_BgpBgpNeighborMaxPrefixRestartTime_Type = Unsigned32
_BgpBgpNeighborMaxPrefixRestartTime_Object = MibTableColumn
bgpBgpNeighborMaxPrefixRestartTime = _BgpBgpNeighborMaxPrefixRestartTime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 55),
    _BgpBgpNeighborMaxPrefixRestartTime_Type()
)
bgpBgpNeighborMaxPrefixRestartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborMaxPrefixRestartTime.setStatus("current")
_BgpBgpNeighborExtPeerHops_Type = Unsigned32
_BgpBgpNeighborExtPeerHops_Object = MibTableColumn
bgpBgpNeighborExtPeerHops = _BgpBgpNeighborExtPeerHops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 56),
    _BgpBgpNeighborExtPeerHops_Type()
)
bgpBgpNeighborExtPeerHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborExtPeerHops.setStatus("current")
_BgpBgpNeighborLocalHost_Type = IpAddress
_BgpBgpNeighborLocalHost_Object = MibTableColumn
bgpBgpNeighborLocalHost = _BgpBgpNeighborLocalHost_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 57),
    _BgpBgpNeighborLocalHost_Type()
)
bgpBgpNeighborLocalHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborLocalHost.setStatus("current")
_BgpBgpNeighborLocalPort_Type = UnsignedShort
_BgpBgpNeighborLocalPort_Object = MibTableColumn
bgpBgpNeighborLocalPort = _BgpBgpNeighborLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 58),
    _BgpBgpNeighborLocalPort_Type()
)
bgpBgpNeighborLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborLocalPort.setStatus("current")
_BgpBgpNeighborRemoteHost_Type = IpAddress
_BgpBgpNeighborRemoteHost_Object = MibTableColumn
bgpBgpNeighborRemoteHost = _BgpBgpNeighborRemoteHost_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 59),
    _BgpBgpNeighborRemoteHost_Type()
)
bgpBgpNeighborRemoteHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborRemoteHost.setStatus("current")
_BgpBgpNeighborRemotePort_Type = UnsignedShort
_BgpBgpNeighborRemotePort_Object = MibTableColumn
bgpBgpNeighborRemotePort = _BgpBgpNeighborRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 60),
    _BgpBgpNeighborRemotePort_Type()
)
bgpBgpNeighborRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborRemotePort.setStatus("current")
_BgpBgpNeighborNextHop_Type = IpAddress
_BgpBgpNeighborNextHop_Object = MibTableColumn
bgpBgpNeighborNextHop = _BgpBgpNeighborNextHop_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 61),
    _BgpBgpNeighborNextHop_Type()
)
bgpBgpNeighborNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborNextHop.setStatus("current")
_BgpBgpNeighborNextStartTimer_Type = Unsigned32
_BgpBgpNeighborNextStartTimer_Object = MibTableColumn
bgpBgpNeighborNextStartTimer = _BgpBgpNeighborNextStartTimer_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 62),
    _BgpBgpNeighborNextStartTimer_Type()
)
bgpBgpNeighborNextStartTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborNextStartTimer.setStatus("current")
_BgpBgpNeighborNextConnectTimer_Type = Unsigned32
_BgpBgpNeighborNextConnectTimer_Object = MibTableColumn
bgpBgpNeighborNextConnectTimer = _BgpBgpNeighborNextConnectTimer_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 63),
    _BgpBgpNeighborNextConnectTimer_Type()
)
bgpBgpNeighborNextConnectTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborNextConnectTimer.setStatus("current")
_BgpBgpNeighborReadThreadOn_Type = TruthValue
_BgpBgpNeighborReadThreadOn_Object = MibTableColumn
bgpBgpNeighborReadThreadOn = _BgpBgpNeighborReadThreadOn_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 64),
    _BgpBgpNeighborReadThreadOn_Type()
)
bgpBgpNeighborReadThreadOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborReadThreadOn.setStatus("current")
_BgpBgpNeighborWriteThreadOn_Type = TruthValue
_BgpBgpNeighborWriteThreadOn_Object = MibTableColumn
bgpBgpNeighborWriteThreadOn = _BgpBgpNeighborWriteThreadOn_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 65),
    _BgpBgpNeighborWriteThreadOn_Type()
)
bgpBgpNeighborWriteThreadOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborWriteThreadOn.setStatus("current")


class _BgpBgpNeighborPassword_Type(String):
    """Custom type bgpBgpNeighborPassword based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_BgpBgpNeighborPassword_Type.__name__ = "String"
_BgpBgpNeighborPassword_Object = MibTableColumn
bgpBgpNeighborPassword = _BgpBgpNeighborPassword_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 66),
    _BgpBgpNeighborPassword_Type()
)
bgpBgpNeighborPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborPassword.setStatus("current")
_BgpBgpNeighborLastUptime_Type = String
_BgpBgpNeighborLastUptime_Object = MibTableColumn
bgpBgpNeighborLastUptime = _BgpBgpNeighborLastUptime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 9, 1, 67),
    _BgpBgpNeighborLastUptime_Type()
)
bgpBgpNeighborLastUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborLastUptime.setStatus("current")
_BgpBgpNeighborAddressFamilyTable_Object = MibTable
bgpBgpNeighborAddressFamilyTable = _BgpBgpNeighborAddressFamilyTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 10)
)
if mibBuilder.loadTexts:
    bgpBgpNeighborAddressFamilyTable.setStatus("current")
_BgpBgpNeighborAddressFamilyEntry_Object = MibTableRow
bgpBgpNeighborAddressFamilyEntry = _BgpBgpNeighborAddressFamilyEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 10, 1)
)
bgpBgpNeighborAddressFamilyEntry.setIndexNames(
    (0, "VIPTELA-OPER-BGP", "bgpBgpNeighborVpnId"),
    (0, "VIPTELA-OPER-BGP", "bgpBgpNeighborPeerAddr"),
    (0, "VIPTELA-OPER-BGP", "bgpBgpNeighborAddressFamilyAfiId"),
)
if mibBuilder.loadTexts:
    bgpBgpNeighborAddressFamilyEntry.setStatus("current")
_BgpBgpNeighborAddressFamilyAfiId_Type = Unsigned32
_BgpBgpNeighborAddressFamilyAfiId_Object = MibTableColumn
bgpBgpNeighborAddressFamilyAfiId = _BgpBgpNeighborAddressFamilyAfiId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 10, 1, 1),
    _BgpBgpNeighborAddressFamilyAfiId_Type()
)
bgpBgpNeighborAddressFamilyAfiId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpBgpNeighborAddressFamilyAfiId.setStatus("current")


class _BgpBgpNeighborAddressFamilyAfi_Type(Integer32):
    """Custom type bgpBgpNeighborAddressFamilyAfi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("ipv4-unicast", 0)
    )


_BgpBgpNeighborAddressFamilyAfi_Type.__name__ = "Integer32"
_BgpBgpNeighborAddressFamilyAfi_Object = MibTableColumn
bgpBgpNeighborAddressFamilyAfi = _BgpBgpNeighborAddressFamilyAfi_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 10, 1, 2),
    _BgpBgpNeighborAddressFamilyAfi_Type()
)
bgpBgpNeighborAddressFamilyAfi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborAddressFamilyAfi.setStatus("current")
_BgpBgpNeighborAddressFamilyRouteReflectorClient_Type = TruthValue
_BgpBgpNeighborAddressFamilyRouteReflectorClient_Object = MibTableColumn
bgpBgpNeighborAddressFamilyRouteReflectorClient = _BgpBgpNeighborAddressFamilyRouteReflectorClient_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 10, 1, 3),
    _BgpBgpNeighborAddressFamilyRouteReflectorClient_Type()
)
bgpBgpNeighborAddressFamilyRouteReflectorClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborAddressFamilyRouteReflectorClient.setStatus("current")
_BgpBgpNeighborAddressFamilyInboundSoftReconfig_Type = TruthValue
_BgpBgpNeighborAddressFamilyInboundSoftReconfig_Object = MibTableColumn
bgpBgpNeighborAddressFamilyInboundSoftReconfig = _BgpBgpNeighborAddressFamilyInboundSoftReconfig_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 10, 1, 4),
    _BgpBgpNeighborAddressFamilyInboundSoftReconfig_Type()
)
bgpBgpNeighborAddressFamilyInboundSoftReconfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborAddressFamilyInboundSoftReconfig.setStatus("current")
_BgpBgpNeighborAddressFamilyPrivateAs_Type = TruthValue
_BgpBgpNeighborAddressFamilyPrivateAs_Object = MibTableColumn
bgpBgpNeighborAddressFamilyPrivateAs = _BgpBgpNeighborAddressFamilyPrivateAs_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 10, 1, 5),
    _BgpBgpNeighborAddressFamilyPrivateAs_Type()
)
bgpBgpNeighborAddressFamilyPrivateAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborAddressFamilyPrivateAs.setStatus("current")
_BgpBgpNeighborAddressFamilyNexthopSelf_Type = TruthValue
_BgpBgpNeighborAddressFamilyNexthopSelf_Object = MibTableColumn
bgpBgpNeighborAddressFamilyNexthopSelf = _BgpBgpNeighborAddressFamilyNexthopSelf_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 10, 1, 6),
    _BgpBgpNeighborAddressFamilyNexthopSelf_Type()
)
bgpBgpNeighborAddressFamilyNexthopSelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborAddressFamilyNexthopSelf.setStatus("current")
_BgpBgpNeighborAddressFamilyAsPathUnchanged_Type = TruthValue
_BgpBgpNeighborAddressFamilyAsPathUnchanged_Object = MibTableColumn
bgpBgpNeighborAddressFamilyAsPathUnchanged = _BgpBgpNeighborAddressFamilyAsPathUnchanged_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 10, 1, 7),
    _BgpBgpNeighborAddressFamilyAsPathUnchanged_Type()
)
bgpBgpNeighborAddressFamilyAsPathUnchanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborAddressFamilyAsPathUnchanged.setStatus("current")
_BgpBgpNeighborAddressFamilyNexthopUnchanged_Type = TruthValue
_BgpBgpNeighborAddressFamilyNexthopUnchanged_Object = MibTableColumn
bgpBgpNeighborAddressFamilyNexthopUnchanged = _BgpBgpNeighborAddressFamilyNexthopUnchanged_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 10, 1, 8),
    _BgpBgpNeighborAddressFamilyNexthopUnchanged_Type()
)
bgpBgpNeighborAddressFamilyNexthopUnchanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborAddressFamilyNexthopUnchanged.setStatus("current")
_BgpBgpNeighborAddressFamilyMedUnchanged_Type = TruthValue
_BgpBgpNeighborAddressFamilyMedUnchanged_Object = MibTableColumn
bgpBgpNeighborAddressFamilyMedUnchanged = _BgpBgpNeighborAddressFamilyMedUnchanged_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 10, 1, 9),
    _BgpBgpNeighborAddressFamilyMedUnchanged_Type()
)
bgpBgpNeighborAddressFamilyMedUnchanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborAddressFamilyMedUnchanged.setStatus("current")
_BgpBgpNeighborAddressFamilySentCommunity_Type = TruthValue
_BgpBgpNeighborAddressFamilySentCommunity_Object = MibTableColumn
bgpBgpNeighborAddressFamilySentCommunity = _BgpBgpNeighborAddressFamilySentCommunity_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 10, 1, 10),
    _BgpBgpNeighborAddressFamilySentCommunity_Type()
)
bgpBgpNeighborAddressFamilySentCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborAddressFamilySentCommunity.setStatus("current")


class _BgpBgpNeighborAddressFamilyDefOriginateRoutemap_Type(String):
    """Custom type bgpBgpNeighborAddressFamilyDefOriginateRoutemap based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_BgpBgpNeighborAddressFamilyDefOriginateRoutemap_Type.__name__ = "String"
_BgpBgpNeighborAddressFamilyDefOriginateRoutemap_Object = MibTableColumn
bgpBgpNeighborAddressFamilyDefOriginateRoutemap = _BgpBgpNeighborAddressFamilyDefOriginateRoutemap_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 10, 1, 11),
    _BgpBgpNeighborAddressFamilyDefOriginateRoutemap_Type()
)
bgpBgpNeighborAddressFamilyDefOriginateRoutemap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborAddressFamilyDefOriginateRoutemap.setStatus("current")
_BgpBgpNeighborAddressFamilySentDefOriginate_Type = TruthValue
_BgpBgpNeighborAddressFamilySentDefOriginate_Object = MibTableColumn
bgpBgpNeighborAddressFamilySentDefOriginate = _BgpBgpNeighborAddressFamilySentDefOriginate_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 10, 1, 12),
    _BgpBgpNeighborAddressFamilySentDefOriginate_Type()
)
bgpBgpNeighborAddressFamilySentDefOriginate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborAddressFamilySentDefOriginate.setStatus("current")
_BgpBgpNeighborAddressFamilyPolicyIn_Type = TruthValue
_BgpBgpNeighborAddressFamilyPolicyIn_Object = MibTableColumn
bgpBgpNeighborAddressFamilyPolicyIn = _BgpBgpNeighborAddressFamilyPolicyIn_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 10, 1, 13),
    _BgpBgpNeighborAddressFamilyPolicyIn_Type()
)
bgpBgpNeighborAddressFamilyPolicyIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborAddressFamilyPolicyIn.setStatus("current")
_BgpBgpNeighborAddressFamilyPolicyOut_Type = TruthValue
_BgpBgpNeighborAddressFamilyPolicyOut_Object = MibTableColumn
bgpBgpNeighborAddressFamilyPolicyOut = _BgpBgpNeighborAddressFamilyPolicyOut_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 10, 1, 14),
    _BgpBgpNeighborAddressFamilyPolicyOut_Type()
)
bgpBgpNeighborAddressFamilyPolicyOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborAddressFamilyPolicyOut.setStatus("current")
_BgpBgpNeighborAddressFamilyAcceptedPrefixCount_Type = Unsigned32
_BgpBgpNeighborAddressFamilyAcceptedPrefixCount_Object = MibTableColumn
bgpBgpNeighborAddressFamilyAcceptedPrefixCount = _BgpBgpNeighborAddressFamilyAcceptedPrefixCount_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 10, 1, 15),
    _BgpBgpNeighborAddressFamilyAcceptedPrefixCount_Type()
)
bgpBgpNeighborAddressFamilyAcceptedPrefixCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborAddressFamilyAcceptedPrefixCount.setStatus("current")
_BgpBgpNeighborAddressFamilyMaximumPrefixCount_Type = Unsigned32
_BgpBgpNeighborAddressFamilyMaximumPrefixCount_Object = MibTableColumn
bgpBgpNeighborAddressFamilyMaximumPrefixCount = _BgpBgpNeighborAddressFamilyMaximumPrefixCount_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 10, 1, 16),
    _BgpBgpNeighborAddressFamilyMaximumPrefixCount_Type()
)
bgpBgpNeighborAddressFamilyMaximumPrefixCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborAddressFamilyMaximumPrefixCount.setStatus("current")
_BgpBgpNeighborAddressFamilyMaxPrefixWarningOnly_Type = TruthValue
_BgpBgpNeighborAddressFamilyMaxPrefixWarningOnly_Object = MibTableColumn
bgpBgpNeighborAddressFamilyMaxPrefixWarningOnly = _BgpBgpNeighborAddressFamilyMaxPrefixWarningOnly_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 10, 1, 17),
    _BgpBgpNeighborAddressFamilyMaxPrefixWarningOnly_Type()
)
bgpBgpNeighborAddressFamilyMaxPrefixWarningOnly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborAddressFamilyMaxPrefixWarningOnly.setStatus("current")
_BgpBgpNeighborAddressFamilyMaxPrefixThresholdWarning_Type = Unsigned32
_BgpBgpNeighborAddressFamilyMaxPrefixThresholdWarning_Object = MibTableColumn
bgpBgpNeighborAddressFamilyMaxPrefixThresholdWarning = _BgpBgpNeighborAddressFamilyMaxPrefixThresholdWarning_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 10, 1, 18),
    _BgpBgpNeighborAddressFamilyMaxPrefixThresholdWarning_Type()
)
bgpBgpNeighborAddressFamilyMaxPrefixThresholdWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborAddressFamilyMaxPrefixThresholdWarning.setStatus("current")
_BgpBgpNeighborAddressFamilyMaxPrefixRestartInterval_Type = Unsigned32
_BgpBgpNeighborAddressFamilyMaxPrefixRestartInterval_Object = MibTableColumn
bgpBgpNeighborAddressFamilyMaxPrefixRestartInterval = _BgpBgpNeighborAddressFamilyMaxPrefixRestartInterval_Object(
    (1, 3, 6, 1, 4, 1, 41916, 14, 10, 1, 19),
    _BgpBgpNeighborAddressFamilyMaxPrefixRestartInterval_Type()
)
bgpBgpNeighborAddressFamilyMaxPrefixRestartInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpBgpNeighborAddressFamilyMaxPrefixRestartInterval.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VIPTELA-OPER-BGP",
    **{"UnsignedShort": UnsignedShort,
       "ConfdString": ConfdString,
       "Ipv4Prefix": Ipv4Prefix,
       "String": String,
       "BgpRibStatusType": BgpRibStatusType,
       "viptela-oper-bgp": viptela_oper_bgp,
       "bgp": bgp,
       "bgpBgpSummaryTable": bgpBgpSummaryTable,
       "bgpBgpSummaryEntry": bgpBgpSummaryEntry,
       "bgpBgpSummaryVpnId": bgpBgpSummaryVpnId,
       "bgpBgpSummaryBgpRouterIdentifier": bgpBgpSummaryBgpRouterIdentifier,
       "bgpBgpSummaryLocalAs": bgpBgpSummaryLocalAs,
       "bgpBgpSummaryRibEntries": bgpBgpSummaryRibEntries,
       "bgpBgpSummaryRibMemory": bgpBgpSummaryRibMemory,
       "bgpBgpSummaryTotalPeers": bgpBgpSummaryTotalPeers,
       "bgpBgpSummaryPeerMemory": bgpBgpSummaryPeerMemory,
       "bgpBgpSummaryLocalSiteOfOrigin": bgpBgpSummaryLocalSiteOfOrigin,
       "bgpBgpSummaryIgnoreSiteOfOrigin": bgpBgpSummaryIgnoreSiteOfOrigin,
       "bgpBgpSummaryNeighborTable": bgpBgpSummaryNeighborTable,
       "bgpBgpSummaryNeighborEntry": bgpBgpSummaryNeighborEntry,
       "bgpBgpSummaryNeighborPeerAddr": bgpBgpSummaryNeighborPeerAddr,
       "bgpBgpSummaryNeighborAs": bgpBgpSummaryNeighborAs,
       "bgpBgpSummaryNeighborMsgRcvd": bgpBgpSummaryNeighborMsgRcvd,
       "bgpBgpSummaryNeighborMsgSent": bgpBgpSummaryNeighborMsgSent,
       "bgpBgpSummaryNeighborOutQ": bgpBgpSummaryNeighborOutQ,
       "bgpBgpSummaryNeighborPrefixRcvd": bgpBgpSummaryNeighborPrefixRcvd,
       "bgpBgpSummaryNeighborPrefixValid": bgpBgpSummaryNeighborPrefixValid,
       "bgpBgpSummaryNeighborPrefixInstalled": bgpBgpSummaryNeighborPrefixInstalled,
       "bgpBgpSummaryNeighborUpTime": bgpBgpSummaryNeighborUpTime,
       "bgpBgpSummaryNeighborState": bgpBgpSummaryNeighborState,
       "bgpBgpSummaryNeighborLastUpTime": bgpBgpSummaryNeighborLastUpTime,
       "bgpRoutesTableTable": bgpRoutesTableTable,
       "bgpRoutesTableEntry": bgpRoutesTableEntry,
       "bgpRoutesTableVpnId": bgpRoutesTableVpnId,
       "bgpRoutesTablePrefix": bgpRoutesTablePrefix,
       "bgpRoutesTableBestPath": bgpRoutesTableBestPath,
       "bgpRoutesTableSuppressed": bgpRoutesTableSuppressed,
       "bgpRoutesTableNoAdvertise": bgpRoutesTableNoAdvertise,
       "bgpRoutesTableNoExport": bgpRoutesTableNoExport,
       "bgpRoutesTableNoLocalAs": bgpRoutesTableNoLocalAs,
       "bgpRoutesTableAdvertisedPeersTable": bgpRoutesTableAdvertisedPeersTable,
       "bgpRoutesTableAdvertisedPeersEntry": bgpRoutesTableAdvertisedPeersEntry,
       "bgpRoutesTableAdvertisedPeersPeerIndex": bgpRoutesTableAdvertisedPeersPeerIndex,
       "bgpRoutesTableAdvertisedPeersPeerAddr": bgpRoutesTableAdvertisedPeersPeerAddr,
       "bgpRoutesTableInfoTable": bgpRoutesTableInfoTable,
       "bgpRoutesTableInfoEntry": bgpRoutesTableInfoEntry,
       "bgpRoutesTableInfoInfoId": bgpRoutesTableInfoInfoId,
       "bgpRoutesTableInfoNexthop": bgpRoutesTableInfoNexthop,
       "bgpRoutesTableInfoMetric": bgpRoutesTableInfoMetric,
       "bgpRoutesTableInfoLocalPref": bgpRoutesTableInfoLocalPref,
       "bgpRoutesTableInfoWeight": bgpRoutesTableInfoWeight,
       "bgpRoutesTableInfoOrigin": bgpRoutesTableInfoOrigin,
       "bgpRoutesTableInfoAsPath": bgpRoutesTableInfoAsPath,
       "bgpRoutesTableInfoRrClient": bgpRoutesTableInfoRrClient,
       "bgpRoutesTableInfoHistory": bgpRoutesTableInfoHistory,
       "bgpRoutesTableInfoAggregator": bgpRoutesTableInfoAggregator,
       "bgpRoutesTableInfoAggregatorAs": bgpRoutesTableInfoAggregatorAs,
       "bgpRoutesTableInfoAggregatorIp": bgpRoutesTableInfoAggregatorIp,
       "bgpRoutesTableInfoRiPeer": bgpRoutesTableInfoRiPeer,
       "bgpRoutesTableInfoRiRouterid": bgpRoutesTableInfoRiRouterid,
       "bgpRoutesTableInfoIgpMetric": bgpRoutesTableInfoIgpMetric,
       "bgpRoutesTableInfoConfedExternal": bgpRoutesTableInfoConfedExternal,
       "bgpRoutesTableInfoAggregated": bgpRoutesTableInfoAggregated,
       "bgpRoutesTableInfoLocal": bgpRoutesTableInfoLocal,
       "bgpRoutesTableInfoSourced": bgpRoutesTableInfoSourced,
       "bgpRoutesTableInfoMultipath": bgpRoutesTableInfoMultipath,
       "bgpRoutesTableInfoCommunity": bgpRoutesTableInfoCommunity,
       "bgpRoutesTableInfoExtCommunity": bgpRoutesTableInfoExtCommunity,
       "bgpRoutesTableInfoOriginator": bgpRoutesTableInfoOriginator,
       "bgpRoutesTableInfoLastUpdate": bgpRoutesTableInfoLastUpdate,
       "bgpRoutesTableInfoClusterList": bgpRoutesTableInfoClusterList,
       "bgpRoutesTableInfoPathStatus": bgpRoutesTableInfoPathStatus,
       "bgpRoutesTableInfoTag": bgpRoutesTableInfoTag,
       "bgpRoutesTableInfoOspfTag": bgpRoutesTableInfoOspfTag,
       "bgpBgpNeighborTable": bgpBgpNeighborTable,
       "bgpBgpNeighborEntry": bgpBgpNeighborEntry,
       "bgpBgpNeighborVpnId": bgpBgpNeighborVpnId,
       "bgpBgpNeighborPeerAddr": bgpBgpNeighborPeerAddr,
       "bgpBgpNeighborAs": bgpBgpNeighborAs,
       "bgpBgpNeighborLocalAsNum": bgpBgpNeighborLocalAsNum,
       "bgpBgpNeighborChangeLocalAsNum": bgpBgpNeighborChangeLocalAsNum,
       "bgpBgpNeighborFlags": bgpBgpNeighborFlags,
       "bgpBgpNeighborDesc": bgpBgpNeighborDesc,
       "bgpBgpNeighborRemoteRouterId": bgpBgpNeighborRemoteRouterId,
       "bgpBgpNeighborCommonAdmin": bgpBgpNeighborCommonAdmin,
       "bgpBgpNeighborLastRead": bgpBgpNeighborLastRead,
       "bgpBgpNeighborKeepalive": bgpBgpNeighborKeepalive,
       "bgpBgpNeighborHoldtime": bgpBgpNeighborHoldtime,
       "bgpBgpNeighborCfgKeepalive": bgpBgpNeighborCfgKeepalive,
       "bgpBgpNeighborCfgHoldtime": bgpBgpNeighborCfgHoldtime,
       "bgpBgpNeighborAdv4byteAsCap": bgpBgpNeighborAdv4byteAsCap,
       "bgpBgpNeighborRec4byteAsCap": bgpBgpNeighborRec4byteAsCap,
       "bgpBgpNeighborAdvDynamicCap": bgpBgpNeighborAdvDynamicCap,
       "bgpBgpNeighborRecDynamicCap": bgpBgpNeighborRecDynamicCap,
       "bgpBgpNeighborAdvRefreshCap": bgpBgpNeighborAdvRefreshCap,
       "bgpBgpNeighborRecRefreshCap": bgpBgpNeighborRecRefreshCap,
       "bgpBgpNeighborAdvNewRefreshCap": bgpBgpNeighborAdvNewRefreshCap,
       "bgpBgpNeighborRecNewRefreshCap": bgpBgpNeighborRecNewRefreshCap,
       "bgpBgpNeighborAdvIpv4UnicastAddrFamily": bgpBgpNeighborAdvIpv4UnicastAddrFamily,
       "bgpBgpNeighborRecIpv4UnicastAddrFamily": bgpBgpNeighborRecIpv4UnicastAddrFamily,
       "bgpBgpNeighborRestartTimeLeft": bgpBgpNeighborRestartTimeLeft,
       "bgpBgpNeighborStalepathTimeLeft": bgpBgpNeighborStalepathTimeLeft,
       "bgpBgpNeighborMsgRcvd": bgpBgpNeighborMsgRcvd,
       "bgpBgpNeighborMsgSent": bgpBgpNeighborMsgSent,
       "bgpBgpNeighborPrefixRcvd": bgpBgpNeighborPrefixRcvd,
       "bgpBgpNeighborPrefixValid": bgpBgpNeighborPrefixValid,
       "bgpBgpNeighborPrefixInstalled": bgpBgpNeighborPrefixInstalled,
       "bgpBgpNeighborOutQ": bgpBgpNeighborOutQ,
       "bgpBgpNeighborUptime": bgpBgpNeighborUptime,
       "bgpBgpNeighborState": bgpBgpNeighborState,
       "bgpBgpNeighborOpenInCount": bgpBgpNeighborOpenInCount,
       "bgpBgpNeighborOpenOutCount": bgpBgpNeighborOpenOutCount,
       "bgpBgpNeighborNotifyInCount": bgpBgpNeighborNotifyInCount,
       "bgpBgpNeighborNotifyOutCount": bgpBgpNeighborNotifyOutCount,
       "bgpBgpNeighborUpdateInCount": bgpBgpNeighborUpdateInCount,
       "bgpBgpNeighborUpdateOutCount": bgpBgpNeighborUpdateOutCount,
       "bgpBgpNeighborKeepaliveInCount": bgpBgpNeighborKeepaliveInCount,
       "bgpBgpNeighborKeepaliveOutCount": bgpBgpNeighborKeepaliveOutCount,
       "bgpBgpNeighborRefreshInCount": bgpBgpNeighborRefreshInCount,
       "bgpBgpNeighborRefreshOutCount": bgpBgpNeighborRefreshOutCount,
       "bgpBgpNeighborDynamicInCount": bgpBgpNeighborDynamicInCount,
       "bgpBgpNeighborDynamicOutCount": bgpBgpNeighborDynamicOutCount,
       "bgpBgpNeighborAdvInterval": bgpBgpNeighborAdvInterval,
       "bgpBgpNeighborUpdateSource": bgpBgpNeighborUpdateSource,
       "bgpBgpNeighborUpdateIf": bgpBgpNeighborUpdateIf,
       "bgpBgpNeighborWeight": bgpBgpNeighborWeight,
       "bgpBgpNeighborConnEstablished": bgpBgpNeighborConnEstablished,
       "bgpBgpNeighborConnDropped": bgpBgpNeighborConnDropped,
       "bgpBgpNeighborLastResetTime": bgpBgpNeighborLastResetTime,
       "bgpBgpNeighborLastResetReason": bgpBgpNeighborLastResetReason,
       "bgpBgpNeighborMaxPrefixRestartTime": bgpBgpNeighborMaxPrefixRestartTime,
       "bgpBgpNeighborExtPeerHops": bgpBgpNeighborExtPeerHops,
       "bgpBgpNeighborLocalHost": bgpBgpNeighborLocalHost,
       "bgpBgpNeighborLocalPort": bgpBgpNeighborLocalPort,
       "bgpBgpNeighborRemoteHost": bgpBgpNeighborRemoteHost,
       "bgpBgpNeighborRemotePort": bgpBgpNeighborRemotePort,
       "bgpBgpNeighborNextHop": bgpBgpNeighborNextHop,
       "bgpBgpNeighborNextStartTimer": bgpBgpNeighborNextStartTimer,
       "bgpBgpNeighborNextConnectTimer": bgpBgpNeighborNextConnectTimer,
       "bgpBgpNeighborReadThreadOn": bgpBgpNeighborReadThreadOn,
       "bgpBgpNeighborWriteThreadOn": bgpBgpNeighborWriteThreadOn,
       "bgpBgpNeighborPassword": bgpBgpNeighborPassword,
       "bgpBgpNeighborLastUptime": bgpBgpNeighborLastUptime,
       "bgpBgpNeighborAddressFamilyTable": bgpBgpNeighborAddressFamilyTable,
       "bgpBgpNeighborAddressFamilyEntry": bgpBgpNeighborAddressFamilyEntry,
       "bgpBgpNeighborAddressFamilyAfiId": bgpBgpNeighborAddressFamilyAfiId,
       "bgpBgpNeighborAddressFamilyAfi": bgpBgpNeighborAddressFamilyAfi,
       "bgpBgpNeighborAddressFamilyRouteReflectorClient": bgpBgpNeighborAddressFamilyRouteReflectorClient,
       "bgpBgpNeighborAddressFamilyInboundSoftReconfig": bgpBgpNeighborAddressFamilyInboundSoftReconfig,
       "bgpBgpNeighborAddressFamilyPrivateAs": bgpBgpNeighborAddressFamilyPrivateAs,
       "bgpBgpNeighborAddressFamilyNexthopSelf": bgpBgpNeighborAddressFamilyNexthopSelf,
       "bgpBgpNeighborAddressFamilyAsPathUnchanged": bgpBgpNeighborAddressFamilyAsPathUnchanged,
       "bgpBgpNeighborAddressFamilyNexthopUnchanged": bgpBgpNeighborAddressFamilyNexthopUnchanged,
       "bgpBgpNeighborAddressFamilyMedUnchanged": bgpBgpNeighborAddressFamilyMedUnchanged,
       "bgpBgpNeighborAddressFamilySentCommunity": bgpBgpNeighborAddressFamilySentCommunity,
       "bgpBgpNeighborAddressFamilyDefOriginateRoutemap": bgpBgpNeighborAddressFamilyDefOriginateRoutemap,
       "bgpBgpNeighborAddressFamilySentDefOriginate": bgpBgpNeighborAddressFamilySentDefOriginate,
       "bgpBgpNeighborAddressFamilyPolicyIn": bgpBgpNeighborAddressFamilyPolicyIn,
       "bgpBgpNeighborAddressFamilyPolicyOut": bgpBgpNeighborAddressFamilyPolicyOut,
       "bgpBgpNeighborAddressFamilyAcceptedPrefixCount": bgpBgpNeighborAddressFamilyAcceptedPrefixCount,
       "bgpBgpNeighborAddressFamilyMaximumPrefixCount": bgpBgpNeighborAddressFamilyMaximumPrefixCount,
       "bgpBgpNeighborAddressFamilyMaxPrefixWarningOnly": bgpBgpNeighborAddressFamilyMaxPrefixWarningOnly,
       "bgpBgpNeighborAddressFamilyMaxPrefixThresholdWarning": bgpBgpNeighborAddressFamilyMaxPrefixThresholdWarning,
       "bgpBgpNeighborAddressFamilyMaxPrefixRestartInterval": bgpBgpNeighborAddressFamilyMaxPrefixRestartInterval}
)
