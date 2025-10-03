# SNMP MIB module (BROCADE-NP-TM-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\brocade\BROCADE-NP-TM-STATS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:21:52 2025
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

(platform,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-ROOT-MIB",
    "platform")

(PortPriorityTC,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-SWITCH-GROUP-MIB",
    "PortPriorityTC")

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

brocadeNPTMStatsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2)
)
if mibBuilder.loadTexts:
    brocadeNPTMStatsMIB.setRevisions(
        ("2011-11-18 00:00",
         "2011-09-28 00:00",
         "2010-09-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BrcdNPTMMIBObjects_ObjectIdentity = ObjectIdentity
brcdNPTMMIBObjects = _BrcdNPTMMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1)
)
_BrcdNPStatisticsInfo_ObjectIdentity = ObjectIdentity
brcdNPStatisticsInfo = _BrcdNPStatisticsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 1)
)
_BrcdNPStatsTable_Object = MibTable
brcdNPStatsTable = _BrcdNPStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    brcdNPStatsTable.setStatus("current")
_BrcdNPStatsEntry_Object = MibTableRow
brcdNPStatsEntry = _BrcdNPStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 1, 1, 1)
)
brcdNPStatsEntry.setIndexNames(
    (0, "BROCADE-NP-TM-STATS-MIB", "brcdNPStatsIfIndex"),
)
if mibBuilder.loadTexts:
    brcdNPStatsEntry.setStatus("current")
_BrcdNPStatsIfIndex_Type = InterfaceIndex
_BrcdNPStatsIfIndex_Object = MibTableColumn
brcdNPStatsIfIndex = _BrcdNPStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 1, 1, 1, 1),
    _BrcdNPStatsIfIndex_Type()
)
brcdNPStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdNPStatsIfIndex.setStatus("current")
_BrcdNPStatsRxRawGoodPkts_Type = Counter64
_BrcdNPStatsRxRawGoodPkts_Object = MibTableColumn
brcdNPStatsRxRawGoodPkts = _BrcdNPStatsRxRawGoodPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 1, 1, 1, 2),
    _BrcdNPStatsRxRawGoodPkts_Type()
)
brcdNPStatsRxRawGoodPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdNPStatsRxRawGoodPkts.setStatus("current")
_BrcdNPStatsRxForwardPkts_Type = Counter64
_BrcdNPStatsRxForwardPkts_Object = MibTableColumn
brcdNPStatsRxForwardPkts = _BrcdNPStatsRxForwardPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 1, 1, 1, 3),
    _BrcdNPStatsRxForwardPkts_Type()
)
brcdNPStatsRxForwardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdNPStatsRxForwardPkts.setStatus("current")
_BrcdNPStatsRxDiscardPkts_Type = Counter64
_BrcdNPStatsRxDiscardPkts_Object = MibTableColumn
brcdNPStatsRxDiscardPkts = _BrcdNPStatsRxDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 1, 1, 1, 4),
    _BrcdNPStatsRxDiscardPkts_Type()
)
brcdNPStatsRxDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdNPStatsRxDiscardPkts.setStatus("current")
_BrcdNPStatsRxMiscPkts_Type = Counter64
_BrcdNPStatsRxMiscPkts_Object = MibTableColumn
brcdNPStatsRxMiscPkts = _BrcdNPStatsRxMiscPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 1, 1, 1, 5),
    _BrcdNPStatsRxMiscPkts_Type()
)
brcdNPStatsRxMiscPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdNPStatsRxMiscPkts.setStatus("current")
_BrcdNPStatsRxUnicastPkts_Type = Counter64
_BrcdNPStatsRxUnicastPkts_Object = MibTableColumn
brcdNPStatsRxUnicastPkts = _BrcdNPStatsRxUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 1, 1, 1, 6),
    _BrcdNPStatsRxUnicastPkts_Type()
)
brcdNPStatsRxUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdNPStatsRxUnicastPkts.setStatus("current")
_BrcdNPStatsRxBroadcastPkts_Type = Counter64
_BrcdNPStatsRxBroadcastPkts_Object = MibTableColumn
brcdNPStatsRxBroadcastPkts = _BrcdNPStatsRxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 1, 1, 1, 7),
    _BrcdNPStatsRxBroadcastPkts_Type()
)
brcdNPStatsRxBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdNPStatsRxBroadcastPkts.setStatus("current")
_BrcdNPStatsRxMulticastPkts_Type = Counter64
_BrcdNPStatsRxMulticastPkts_Object = MibTableColumn
brcdNPStatsRxMulticastPkts = _BrcdNPStatsRxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 1, 1, 1, 8),
    _BrcdNPStatsRxMulticastPkts_Type()
)
brcdNPStatsRxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdNPStatsRxMulticastPkts.setStatus("current")
_BrcdNPStatsRxSendToTMPkts_Type = Counter64
_BrcdNPStatsRxSendToTMPkts_Object = MibTableColumn
brcdNPStatsRxSendToTMPkts = _BrcdNPStatsRxSendToTMPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 1, 1, 1, 9),
    _BrcdNPStatsRxSendToTMPkts_Type()
)
brcdNPStatsRxSendToTMPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdNPStatsRxSendToTMPkts.setStatus("current")
_BrcdNPStatsRxBadPkts_Type = Counter64
_BrcdNPStatsRxBadPkts_Object = MibTableColumn
brcdNPStatsRxBadPkts = _BrcdNPStatsRxBadPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 1, 1, 1, 10),
    _BrcdNPStatsRxBadPkts_Type()
)
brcdNPStatsRxBadPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdNPStatsRxBadPkts.setStatus("current")
_BrcdNPStatsRxLookupUnavailable_Type = Counter64
_BrcdNPStatsRxLookupUnavailable_Object = MibTableColumn
brcdNPStatsRxLookupUnavailable = _BrcdNPStatsRxLookupUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 1, 1, 1, 11),
    _BrcdNPStatsRxLookupUnavailable_Type()
)
brcdNPStatsRxLookupUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdNPStatsRxLookupUnavailable.setStatus("current")
_BrcdNPStatsRxACLDrop_Type = Counter64
_BrcdNPStatsRxACLDrop_Object = MibTableColumn
brcdNPStatsRxACLDrop = _BrcdNPStatsRxACLDrop_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 1, 1, 1, 12),
    _BrcdNPStatsRxACLDrop_Type()
)
brcdNPStatsRxACLDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdNPStatsRxACLDrop.setStatus("current")
_BrcdNPStatsRxPriority0And1Drop_Type = Counter64
_BrcdNPStatsRxPriority0And1Drop_Object = MibTableColumn
brcdNPStatsRxPriority0And1Drop = _BrcdNPStatsRxPriority0And1Drop_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 1, 1, 1, 13),
    _BrcdNPStatsRxPriority0And1Drop_Type()
)
brcdNPStatsRxPriority0And1Drop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdNPStatsRxPriority0And1Drop.setStatus("current")
_BrcdNPStatsRxPriority2And3Drop_Type = Counter64
_BrcdNPStatsRxPriority2And3Drop_Object = MibTableColumn
brcdNPStatsRxPriority2And3Drop = _BrcdNPStatsRxPriority2And3Drop_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 1, 1, 1, 14),
    _BrcdNPStatsRxPriority2And3Drop_Type()
)
brcdNPStatsRxPriority2And3Drop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdNPStatsRxPriority2And3Drop.setStatus("current")
_BrcdNPStatsRxPriority4And5Drop_Type = Counter64
_BrcdNPStatsRxPriority4And5Drop_Object = MibTableColumn
brcdNPStatsRxPriority4And5Drop = _BrcdNPStatsRxPriority4And5Drop_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 1, 1, 1, 15),
    _BrcdNPStatsRxPriority4And5Drop_Type()
)
brcdNPStatsRxPriority4And5Drop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdNPStatsRxPriority4And5Drop.setStatus("current")
_BrcdNPStatsRxPriority6And7Drop_Type = Counter64
_BrcdNPStatsRxPriority6And7Drop_Object = MibTableColumn
brcdNPStatsRxPriority6And7Drop = _BrcdNPStatsRxPriority6And7Drop_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 1, 1, 1, 16),
    _BrcdNPStatsRxPriority6And7Drop_Type()
)
brcdNPStatsRxPriority6And7Drop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdNPStatsRxPriority6And7Drop.setStatus("current")
_BrcdNPStatsRxSuppressRPFDrop_Type = Counter64
_BrcdNPStatsRxSuppressRPFDrop_Object = MibTableColumn
brcdNPStatsRxSuppressRPFDrop = _BrcdNPStatsRxSuppressRPFDrop_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 1, 1, 1, 17),
    _BrcdNPStatsRxSuppressRPFDrop_Type()
)
brcdNPStatsRxSuppressRPFDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdNPStatsRxSuppressRPFDrop.setStatus("current")
_BrcdNPStatsRxRPFDrop_Type = Counter64
_BrcdNPStatsRxRPFDrop_Object = MibTableColumn
brcdNPStatsRxRPFDrop = _BrcdNPStatsRxRPFDrop_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 1, 1, 1, 18),
    _BrcdNPStatsRxRPFDrop_Type()
)
brcdNPStatsRxRPFDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdNPStatsRxRPFDrop.setStatus("current")
_BrcdNPStatsRxIPv4Pkts_Type = Counter64
_BrcdNPStatsRxIPv4Pkts_Object = MibTableColumn
brcdNPStatsRxIPv4Pkts = _BrcdNPStatsRxIPv4Pkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 1, 1, 1, 19),
    _BrcdNPStatsRxIPv4Pkts_Type()
)
brcdNPStatsRxIPv4Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdNPStatsRxIPv4Pkts.setStatus("current")
_BrcdNPStatsRxIPv6Pkts_Type = Counter64
_BrcdNPStatsRxIPv6Pkts_Object = MibTableColumn
brcdNPStatsRxIPv6Pkts = _BrcdNPStatsRxIPv6Pkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 1, 1, 1, 20),
    _BrcdNPStatsRxIPv6Pkts_Type()
)
brcdNPStatsRxIPv6Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdNPStatsRxIPv6Pkts.setStatus("current")
_BrcdNPStatsRxRouteOnlyDrop_Type = Counter64
_BrcdNPStatsRxRouteOnlyDrop_Object = MibTableColumn
brcdNPStatsRxRouteOnlyDrop = _BrcdNPStatsRxRouteOnlyDrop_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 1, 1, 1, 21),
    _BrcdNPStatsRxRouteOnlyDrop_Type()
)
brcdNPStatsRxRouteOnlyDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdNPStatsRxRouteOnlyDrop.setStatus("current")
_BrcdNPStatsRxIPv6SuppressRPFDrop_Type = Counter64
_BrcdNPStatsRxIPv6SuppressRPFDrop_Object = MibTableColumn
brcdNPStatsRxIPv6SuppressRPFDrop = _BrcdNPStatsRxIPv6SuppressRPFDrop_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 1, 1, 1, 22),
    _BrcdNPStatsRxIPv6SuppressRPFDrop_Type()
)
brcdNPStatsRxIPv6SuppressRPFDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdNPStatsRxIPv6SuppressRPFDrop.setStatus("current")
_BrcdNPStatsRxIPv6RPFDropCount_Type = Counter64
_BrcdNPStatsRxIPv6RPFDropCount_Object = MibTableColumn
brcdNPStatsRxIPv6RPFDropCount = _BrcdNPStatsRxIPv6RPFDropCount_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 1, 1, 1, 23),
    _BrcdNPStatsRxIPv6RPFDropCount_Type()
)
brcdNPStatsRxIPv6RPFDropCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdNPStatsRxIPv6RPFDropCount.setStatus("current")
_BrcdNPStatsRxIPv4Bytes_Type = Counter64
_BrcdNPStatsRxIPv4Bytes_Object = MibTableColumn
brcdNPStatsRxIPv4Bytes = _BrcdNPStatsRxIPv4Bytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 1, 1, 1, 24),
    _BrcdNPStatsRxIPv4Bytes_Type()
)
brcdNPStatsRxIPv4Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdNPStatsRxIPv4Bytes.setStatus("current")
_BrcdNPStatsRxIPv6Bytes_Type = Counter64
_BrcdNPStatsRxIPv6Bytes_Object = MibTableColumn
brcdNPStatsRxIPv6Bytes = _BrcdNPStatsRxIPv6Bytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 1, 1, 1, 25),
    _BrcdNPStatsRxIPv6Bytes_Type()
)
brcdNPStatsRxIPv6Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdNPStatsRxIPv6Bytes.setStatus("current")
_BrcdNPStatsRxPOSCtrlProtocolPkts_Type = Counter64
_BrcdNPStatsRxPOSCtrlProtocolPkts_Object = MibTableColumn
brcdNPStatsRxPOSCtrlProtocolPkts = _BrcdNPStatsRxPOSCtrlProtocolPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 1, 1, 1, 26),
    _BrcdNPStatsRxPOSCtrlProtocolPkts_Type()
)
brcdNPStatsRxPOSCtrlProtocolPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdNPStatsRxPOSCtrlProtocolPkts.setStatus("current")
_BrcdNPStatsRxPOSLinkDrop_Type = Counter64
_BrcdNPStatsRxPOSLinkDrop_Object = MibTableColumn
brcdNPStatsRxPOSLinkDrop = _BrcdNPStatsRxPOSLinkDrop_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 1, 1, 1, 27),
    _BrcdNPStatsRxPOSLinkDrop_Type()
)
brcdNPStatsRxPOSLinkDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdNPStatsRxPOSLinkDrop.setStatus("current")
_BrcdNPStatsRxRoutedPktsDrop_Type = Counter64
_BrcdNPStatsRxRoutedPktsDrop_Object = MibTableColumn
brcdNPStatsRxRoutedPktsDrop = _BrcdNPStatsRxRoutedPktsDrop_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 1, 1, 1, 28),
    _BrcdNPStatsRxRoutedPktsDrop_Type()
)
brcdNPStatsRxRoutedPktsDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdNPStatsRxRoutedPktsDrop.setStatus("current")
_BrcdNPStatsTxSentToMACPkts_Type = Counter64
_BrcdNPStatsTxSentToMACPkts_Object = MibTableColumn
brcdNPStatsTxSentToMACPkts = _BrcdNPStatsTxSentToMACPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 1, 1, 1, 29),
    _BrcdNPStatsTxSentToMACPkts_Type()
)
brcdNPStatsTxSentToMACPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdNPStatsTxSentToMACPkts.setStatus("current")
_BrcdNPStatsTxRawGoodPkts_Type = Counter64
_BrcdNPStatsTxRawGoodPkts_Object = MibTableColumn
brcdNPStatsTxRawGoodPkts = _BrcdNPStatsTxRawGoodPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 1, 1, 1, 30),
    _BrcdNPStatsTxRawGoodPkts_Type()
)
brcdNPStatsTxRawGoodPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdNPStatsTxRawGoodPkts.setStatus("current")
_BrcdNPStatsTxSrcPortSupressDrop_Type = Counter64
_BrcdNPStatsTxSrcPortSupressDrop_Object = MibTableColumn
brcdNPStatsTxSrcPortSupressDrop = _BrcdNPStatsTxSrcPortSupressDrop_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 1, 1, 1, 31),
    _BrcdNPStatsTxSrcPortSupressDrop_Type()
)
brcdNPStatsTxSrcPortSupressDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdNPStatsTxSrcPortSupressDrop.setStatus("current")
_BrcdNPStatsTxBadPktsCnt_Type = Counter64
_BrcdNPStatsTxBadPktsCnt_Object = MibTableColumn
brcdNPStatsTxBadPktsCnt = _BrcdNPStatsTxBadPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 1, 1, 1, 32),
    _BrcdNPStatsTxBadPktsCnt_Type()
)
brcdNPStatsTxBadPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdNPStatsTxBadPktsCnt.setStatus("current")
_BrcdNPStatsTxUnicastPkts_Type = Counter64
_BrcdNPStatsTxUnicastPkts_Object = MibTableColumn
brcdNPStatsTxUnicastPkts = _BrcdNPStatsTxUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 1, 1, 1, 33),
    _BrcdNPStatsTxUnicastPkts_Type()
)
brcdNPStatsTxUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdNPStatsTxUnicastPkts.setStatus("current")
_BrcdNPStatsTxBroadcastPkts_Type = Counter64
_BrcdNPStatsTxBroadcastPkts_Object = MibTableColumn
brcdNPStatsTxBroadcastPkts = _BrcdNPStatsTxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 1, 1, 1, 34),
    _BrcdNPStatsTxBroadcastPkts_Type()
)
brcdNPStatsTxBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdNPStatsTxBroadcastPkts.setStatus("current")
_BrcdNPStatsTxMulticastPkts_Type = Counter64
_BrcdNPStatsTxMulticastPkts_Object = MibTableColumn
brcdNPStatsTxMulticastPkts = _BrcdNPStatsTxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 1, 1, 1, 35),
    _BrcdNPStatsTxMulticastPkts_Type()
)
brcdNPStatsTxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdNPStatsTxMulticastPkts.setStatus("current")
_BrcdNPStatsTxReceiveFromTM_Type = Counter64
_BrcdNPStatsTxReceiveFromTM_Object = MibTableColumn
brcdNPStatsTxReceiveFromTM = _BrcdNPStatsTxReceiveFromTM_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 1, 1, 1, 36),
    _BrcdNPStatsTxReceiveFromTM_Type()
)
brcdNPStatsTxReceiveFromTM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdNPStatsTxReceiveFromTM.setStatus("current")
_BrcdNPStatsTxACLDrop_Type = Counter64
_BrcdNPStatsTxACLDrop_Object = MibTableColumn
brcdNPStatsTxACLDrop = _BrcdNPStatsTxACLDrop_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 1, 1, 1, 37),
    _BrcdNPStatsTxACLDrop_Type()
)
brcdNPStatsTxACLDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdNPStatsTxACLDrop.setStatus("current")
_BrcdNPStatsTxPFCMulticastDrop_Type = Counter64
_BrcdNPStatsTxPFCMulticastDrop_Object = MibTableColumn
brcdNPStatsTxPFCMulticastDrop = _BrcdNPStatsTxPFCMulticastDrop_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 1, 1, 1, 38),
    _BrcdNPStatsTxPFCMulticastDrop_Type()
)
brcdNPStatsTxPFCMulticastDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdNPStatsTxPFCMulticastDrop.setStatus("current")
_BrcdNPStatsTxPFCMTUExceedDrop_Type = Counter64
_BrcdNPStatsTxPFCMTUExceedDrop_Object = MibTableColumn
brcdNPStatsTxPFCMTUExceedDrop = _BrcdNPStatsTxPFCMTUExceedDrop_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 1, 1, 1, 39),
    _BrcdNPStatsTxPFCMTUExceedDrop_Type()
)
brcdNPStatsTxPFCMTUExceedDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdNPStatsTxPFCMTUExceedDrop.setStatus("current")
_BrcdNPStatsTxPFCQMAPErrorDrop_Type = Counter64
_BrcdNPStatsTxPFCQMAPErrorDrop_Object = MibTableColumn
brcdNPStatsTxPFCQMAPErrorDrop = _BrcdNPStatsTxPFCQMAPErrorDrop_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 1, 1, 1, 40),
    _BrcdNPStatsTxPFCQMAPErrorDrop_Type()
)
brcdNPStatsTxPFCQMAPErrorDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdNPStatsTxPFCQMAPErrorDrop.setStatus("current")
_BrcdNPStatsTxIPv4Pkts_Type = Counter64
_BrcdNPStatsTxIPv4Pkts_Object = MibTableColumn
brcdNPStatsTxIPv4Pkts = _BrcdNPStatsTxIPv4Pkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 1, 1, 1, 41),
    _BrcdNPStatsTxIPv4Pkts_Type()
)
brcdNPStatsTxIPv4Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdNPStatsTxIPv4Pkts.setStatus("current")
_BrcdNPStatsTxIPv6Pkts_Type = Counter64
_BrcdNPStatsTxIPv6Pkts_Object = MibTableColumn
brcdNPStatsTxIPv6Pkts = _BrcdNPStatsTxIPv6Pkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 1, 1, 1, 42),
    _BrcdNPStatsTxIPv6Pkts_Type()
)
brcdNPStatsTxIPv6Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdNPStatsTxIPv6Pkts.setStatus("current")
_BrcdNPStatsTxIPv4Bytes_Type = Counter64
_BrcdNPStatsTxIPv4Bytes_Object = MibTableColumn
brcdNPStatsTxIPv4Bytes = _BrcdNPStatsTxIPv4Bytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 1, 1, 1, 43),
    _BrcdNPStatsTxIPv4Bytes_Type()
)
brcdNPStatsTxIPv4Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdNPStatsTxIPv4Bytes.setStatus("current")
_BrcdNPStatsTxIPv6Bytes_Type = Counter64
_BrcdNPStatsTxIPv6Bytes_Object = MibTableColumn
brcdNPStatsTxIPv6Bytes = _BrcdNPStatsTxIPv6Bytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 1, 1, 1, 44),
    _BrcdNPStatsTxIPv6Bytes_Type()
)
brcdNPStatsTxIPv6Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdNPStatsTxIPv6Bytes.setStatus("current")
_BrcdNPStatsTxPOSCtrlProtocolPkts_Type = Counter64
_BrcdNPStatsTxPOSCtrlProtocolPkts_Object = MibTableColumn
brcdNPStatsTxPOSCtrlProtocolPkts = _BrcdNPStatsTxPOSCtrlProtocolPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 1, 1, 1, 45),
    _BrcdNPStatsTxPOSCtrlProtocolPkts_Type()
)
brcdNPStatsTxPOSCtrlProtocolPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdNPStatsTxPOSCtrlProtocolPkts.setStatus("current")
_BrcdNPStatsTxPOSLinkDrop_Type = Counter64
_BrcdNPStatsTxPOSLinkDrop_Object = MibTableColumn
brcdNPStatsTxPOSLinkDrop = _BrcdNPStatsTxPOSLinkDrop_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 1, 1, 1, 46),
    _BrcdNPStatsTxPOSLinkDrop_Type()
)
brcdNPStatsTxPOSLinkDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdNPStatsTxPOSLinkDrop.setStatus("current")
_BrcdNPQosStatTable_Object = MibTable
brcdNPQosStatTable = _BrcdNPQosStatTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    brcdNPQosStatTable.setStatus("current")
_BrcdNPQosStatEntry_Object = MibTableRow
brcdNPQosStatEntry = _BrcdNPQosStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 1, 2, 1)
)
brcdNPQosStatEntry.setIndexNames(
    (0, "BROCADE-NP-TM-STATS-MIB", "brcdNPQosStatIfIndex"),
    (0, "BROCADE-NP-TM-STATS-MIB", "brcdNPQosStatQosPriority"),
)
if mibBuilder.loadTexts:
    brcdNPQosStatEntry.setStatus("current")
_BrcdNPQosStatIfIndex_Type = InterfaceIndex
_BrcdNPQosStatIfIndex_Object = MibTableColumn
brcdNPQosStatIfIndex = _BrcdNPQosStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 1, 2, 1, 1),
    _BrcdNPQosStatIfIndex_Type()
)
brcdNPQosStatIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdNPQosStatIfIndex.setStatus("current")
_BrcdNPQosStatQosPriority_Type = PortPriorityTC
_BrcdNPQosStatQosPriority_Object = MibTableColumn
brcdNPQosStatQosPriority = _BrcdNPQosStatQosPriority_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 1, 2, 1, 2),
    _BrcdNPQosStatQosPriority_Type()
)
brcdNPQosStatQosPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdNPQosStatQosPriority.setStatus("current")
_BrcdNPQosStatIngressPkts_Type = Counter64
_BrcdNPQosStatIngressPkts_Object = MibTableColumn
brcdNPQosStatIngressPkts = _BrcdNPQosStatIngressPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 1, 2, 1, 3),
    _BrcdNPQosStatIngressPkts_Type()
)
brcdNPQosStatIngressPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdNPQosStatIngressPkts.setStatus("current")
_BrcdNPQosStatIngressBytes_Type = Counter64
_BrcdNPQosStatIngressBytes_Object = MibTableColumn
brcdNPQosStatIngressBytes = _BrcdNPQosStatIngressBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 1, 2, 1, 4),
    _BrcdNPQosStatIngressBytes_Type()
)
brcdNPQosStatIngressBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdNPQosStatIngressBytes.setStatus("current")
_BrcdNPQosStatEgressPkts_Type = Counter64
_BrcdNPQosStatEgressPkts_Object = MibTableColumn
brcdNPQosStatEgressPkts = _BrcdNPQosStatEgressPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 1, 2, 1, 5),
    _BrcdNPQosStatEgressPkts_Type()
)
brcdNPQosStatEgressPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdNPQosStatEgressPkts.setStatus("current")
_BrcdNPQosStatEgressBytes_Type = Counter64
_BrcdNPQosStatEgressBytes_Object = MibTableColumn
brcdNPQosStatEgressBytes = _BrcdNPQosStatEgressBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 1, 2, 1, 6),
    _BrcdNPQosStatEgressBytes_Type()
)
brcdNPQosStatEgressBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdNPQosStatEgressBytes.setStatus("current")
_BrcdTMStatisticsInfo_ObjectIdentity = ObjectIdentity
brcdTMStatisticsInfo = _BrcdTMStatisticsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2)
)
_BrcdTMStatisticsInfoGroup_ObjectIdentity = ObjectIdentity
brcdTMStatisticsInfoGroup = _BrcdTMStatisticsInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 1)
)
_BrcdTMPortMappingMaxPorts_Type = Unsigned32
_BrcdTMPortMappingMaxPorts_Object = MibScalar
brcdTMPortMappingMaxPorts = _BrcdTMPortMappingMaxPorts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 1, 1),
    _BrcdTMPortMappingMaxPorts_Type()
)
brcdTMPortMappingMaxPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMPortMappingMaxPorts.setStatus("current")
_BrcdTMPortMappingUsedPorts_Type = Unsigned32
_BrcdTMPortMappingUsedPorts_Object = MibScalar
brcdTMPortMappingUsedPorts = _BrcdTMPortMappingUsedPorts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 1, 2),
    _BrcdTMPortMappingUsedPorts_Type()
)
brcdTMPortMappingUsedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMPortMappingUsedPorts.setStatus("current")
_BrcdTMPortMappingAvailablePorts_Type = Unsigned32
_BrcdTMPortMappingAvailablePorts_Object = MibScalar
brcdTMPortMappingAvailablePorts = _BrcdTMPortMappingAvailablePorts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 1, 3),
    _BrcdTMPortMappingAvailablePorts_Type()
)
brcdTMPortMappingAvailablePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMPortMappingAvailablePorts.setStatus("current")
_BrcdTMStatsTable_Object = MibTable
brcdTMStatsTable = _BrcdTMStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    brcdTMStatsTable.setStatus("current")
_BrcdTMStatsEntry_Object = MibTableRow
brcdTMStatsEntry = _BrcdTMStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 2, 1)
)
brcdTMStatsEntry.setIndexNames(
    (0, "BROCADE-NP-TM-STATS-MIB", "brcdTMStatsSlotId"),
    (0, "BROCADE-NP-TM-STATS-MIB", "brcdTMStatsTMDeviceId"),
)
if mibBuilder.loadTexts:
    brcdTMStatsEntry.setStatus("current")
_BrcdTMStatsSlotId_Type = Unsigned32
_BrcdTMStatsSlotId_Object = MibTableColumn
brcdTMStatsSlotId = _BrcdTMStatsSlotId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 2, 1, 1),
    _BrcdTMStatsSlotId_Type()
)
brcdTMStatsSlotId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdTMStatsSlotId.setStatus("current")
_BrcdTMStatsTMDeviceId_Type = Unsigned32
_BrcdTMStatsTMDeviceId_Object = MibTableColumn
brcdTMStatsTMDeviceId = _BrcdTMStatsTMDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 2, 1, 2),
    _BrcdTMStatsTMDeviceId_Type()
)
brcdTMStatsTMDeviceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdTMStatsTMDeviceId.setStatus("current")
_BrcdTMStatsDescription_Type = DisplayString
_BrcdTMStatsDescription_Object = MibTableColumn
brcdTMStatsDescription = _BrcdTMStatsDescription_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 2, 1, 3),
    _BrcdTMStatsDescription_Type()
)
brcdTMStatsDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMStatsDescription.setStatus("current")
_BrcdTMStatsTotalIngressPktsCnt_Type = Counter64
_BrcdTMStatsTotalIngressPktsCnt_Object = MibTableColumn
brcdTMStatsTotalIngressPktsCnt = _BrcdTMStatsTotalIngressPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 2, 1, 4),
    _BrcdTMStatsTotalIngressPktsCnt_Type()
)
brcdTMStatsTotalIngressPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMStatsTotalIngressPktsCnt.setStatus("current")
_BrcdTMStatsIngressEnqueuePkts_Type = Counter64
_BrcdTMStatsIngressEnqueuePkts_Object = MibTableColumn
brcdTMStatsIngressEnqueuePkts = _BrcdTMStatsIngressEnqueuePkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 2, 1, 5),
    _BrcdTMStatsIngressEnqueuePkts_Type()
)
brcdTMStatsIngressEnqueuePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMStatsIngressEnqueuePkts.setStatus("current")
_BrcdTMStatsEgressEnqueuePkts_Type = Counter64
_BrcdTMStatsEgressEnqueuePkts_Object = MibTableColumn
brcdTMStatsEgressEnqueuePkts = _BrcdTMStatsEgressEnqueuePkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 2, 1, 6),
    _BrcdTMStatsEgressEnqueuePkts_Type()
)
brcdTMStatsEgressEnqueuePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMStatsEgressEnqueuePkts.setStatus("current")
_BrcdTMStatsIngressEnqueueBytes_Type = Counter64
_BrcdTMStatsIngressEnqueueBytes_Object = MibTableColumn
brcdTMStatsIngressEnqueueBytes = _BrcdTMStatsIngressEnqueueBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 2, 1, 7),
    _BrcdTMStatsIngressEnqueueBytes_Type()
)
brcdTMStatsIngressEnqueueBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMStatsIngressEnqueueBytes.setStatus("current")
_BrcdTMStatsEgressEnqueueBytes_Type = Counter64
_BrcdTMStatsEgressEnqueueBytes_Object = MibTableColumn
brcdTMStatsEgressEnqueueBytes = _BrcdTMStatsEgressEnqueueBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 2, 1, 8),
    _BrcdTMStatsEgressEnqueueBytes_Type()
)
brcdTMStatsEgressEnqueueBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMStatsEgressEnqueueBytes.setStatus("current")
_BrcdTMStatsIngressDequeuePkts_Type = Counter64
_BrcdTMStatsIngressDequeuePkts_Object = MibTableColumn
brcdTMStatsIngressDequeuePkts = _BrcdTMStatsIngressDequeuePkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 2, 1, 9),
    _BrcdTMStatsIngressDequeuePkts_Type()
)
brcdTMStatsIngressDequeuePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMStatsIngressDequeuePkts.setStatus("current")
_BrcdTMStatsIngressDequeueBytes_Type = Counter64
_BrcdTMStatsIngressDequeueBytes_Object = MibTableColumn
brcdTMStatsIngressDequeueBytes = _BrcdTMStatsIngressDequeueBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 2, 1, 10),
    _BrcdTMStatsIngressDequeueBytes_Type()
)
brcdTMStatsIngressDequeueBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMStatsIngressDequeueBytes.setStatus("current")
_BrcdTMStatsIngressTotalQDiscardPkts_Type = Counter64
_BrcdTMStatsIngressTotalQDiscardPkts_Object = MibTableColumn
brcdTMStatsIngressTotalQDiscardPkts = _BrcdTMStatsIngressTotalQDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 2, 1, 11),
    _BrcdTMStatsIngressTotalQDiscardPkts_Type()
)
brcdTMStatsIngressTotalQDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMStatsIngressTotalQDiscardPkts.setStatus("current")
_BrcdTMStatsIngressTotalQDiscardBytes_Type = Counter64
_BrcdTMStatsIngressTotalQDiscardBytes_Object = MibTableColumn
brcdTMStatsIngressTotalQDiscardBytes = _BrcdTMStatsIngressTotalQDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 2, 1, 12),
    _BrcdTMStatsIngressTotalQDiscardBytes_Type()
)
brcdTMStatsIngressTotalQDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMStatsIngressTotalQDiscardBytes.setStatus("current")
_BrcdTMStatsIngressOldestDiscardPkts_Type = Counter64
_BrcdTMStatsIngressOldestDiscardPkts_Object = MibTableColumn
brcdTMStatsIngressOldestDiscardPkts = _BrcdTMStatsIngressOldestDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 2, 1, 13),
    _BrcdTMStatsIngressOldestDiscardPkts_Type()
)
brcdTMStatsIngressOldestDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMStatsIngressOldestDiscardPkts.setStatus("current")
_BrcdTMStatsIngressOldestDiscardBytes_Type = Counter64
_BrcdTMStatsIngressOldestDiscardBytes_Object = MibTableColumn
brcdTMStatsIngressOldestDiscardBytes = _BrcdTMStatsIngressOldestDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 2, 1, 14),
    _BrcdTMStatsIngressOldestDiscardBytes_Type()
)
brcdTMStatsIngressOldestDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMStatsIngressOldestDiscardBytes.setStatus("current")
_BrcdTMStatsEgressDiscardPkts_Type = Counter64
_BrcdTMStatsEgressDiscardPkts_Object = MibTableColumn
brcdTMStatsEgressDiscardPkts = _BrcdTMStatsEgressDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 2, 1, 15),
    _BrcdTMStatsEgressDiscardPkts_Type()
)
brcdTMStatsEgressDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMStatsEgressDiscardPkts.setStatus("current")
_BrcdTMStatsEgressDiscardBytes_Type = Counter64
_BrcdTMStatsEgressDiscardBytes_Object = MibTableColumn
brcdTMStatsEgressDiscardBytes = _BrcdTMStatsEgressDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 2, 1, 16),
    _BrcdTMStatsEgressDiscardBytes_Type()
)
brcdTMStatsEgressDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMStatsEgressDiscardBytes.setStatus("current")
_BrcdTMUcastQStatsTable_Object = MibTable
brcdTMUcastQStatsTable = _BrcdTMUcastQStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    brcdTMUcastQStatsTable.setStatus("current")
_BrcdTMUcastQStatsEntry_Object = MibTableRow
brcdTMUcastQStatsEntry = _BrcdTMUcastQStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 3, 1)
)
brcdTMUcastQStatsEntry.setIndexNames(
    (0, "BROCADE-NP-TM-STATS-MIB", "brcdTMUcastQStatsSlotId"),
    (0, "BROCADE-NP-TM-STATS-MIB", "brcdTMUcastQStatsTMDeviceId"),
    (0, "BROCADE-NP-TM-STATS-MIB", "brcdTMUcastQStatsDstIfIndex"),
    (0, "BROCADE-NP-TM-STATS-MIB", "brcdTMUcastQStatsPriority"),
)
if mibBuilder.loadTexts:
    brcdTMUcastQStatsEntry.setStatus("current")
_BrcdTMUcastQStatsSlotId_Type = Unsigned32
_BrcdTMUcastQStatsSlotId_Object = MibTableColumn
brcdTMUcastQStatsSlotId = _BrcdTMUcastQStatsSlotId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 3, 1, 1),
    _BrcdTMUcastQStatsSlotId_Type()
)
brcdTMUcastQStatsSlotId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdTMUcastQStatsSlotId.setStatus("current")
_BrcdTMUcastQStatsTMDeviceId_Type = Unsigned32
_BrcdTMUcastQStatsTMDeviceId_Object = MibTableColumn
brcdTMUcastQStatsTMDeviceId = _BrcdTMUcastQStatsTMDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 3, 1, 2),
    _BrcdTMUcastQStatsTMDeviceId_Type()
)
brcdTMUcastQStatsTMDeviceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdTMUcastQStatsTMDeviceId.setStatus("current")
_BrcdTMUcastQStatsDstIfIndex_Type = InterfaceIndex
_BrcdTMUcastQStatsDstIfIndex_Object = MibTableColumn
brcdTMUcastQStatsDstIfIndex = _BrcdTMUcastQStatsDstIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 3, 1, 3),
    _BrcdTMUcastQStatsDstIfIndex_Type()
)
brcdTMUcastQStatsDstIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdTMUcastQStatsDstIfIndex.setStatus("current")
_BrcdTMUcastQStatsPriority_Type = PortPriorityTC
_BrcdTMUcastQStatsPriority_Object = MibTableColumn
brcdTMUcastQStatsPriority = _BrcdTMUcastQStatsPriority_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 3, 1, 4),
    _BrcdTMUcastQStatsPriority_Type()
)
brcdTMUcastQStatsPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdTMUcastQStatsPriority.setStatus("current")
_BrcdTMUcastQStatsDescription_Type = DisplayString
_BrcdTMUcastQStatsDescription_Object = MibTableColumn
brcdTMUcastQStatsDescription = _BrcdTMUcastQStatsDescription_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 3, 1, 5),
    _BrcdTMUcastQStatsDescription_Type()
)
brcdTMUcastQStatsDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMUcastQStatsDescription.setStatus("current")
_BrcdTMUcastQStatsEnquePkts_Type = Counter64
_BrcdTMUcastQStatsEnquePkts_Object = MibTableColumn
brcdTMUcastQStatsEnquePkts = _BrcdTMUcastQStatsEnquePkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 3, 1, 6),
    _BrcdTMUcastQStatsEnquePkts_Type()
)
brcdTMUcastQStatsEnquePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMUcastQStatsEnquePkts.setStatus("current")
_BrcdTMUcastQStatsEnqueBytes_Type = Counter64
_BrcdTMUcastQStatsEnqueBytes_Object = MibTableColumn
brcdTMUcastQStatsEnqueBytes = _BrcdTMUcastQStatsEnqueBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 3, 1, 7),
    _BrcdTMUcastQStatsEnqueBytes_Type()
)
brcdTMUcastQStatsEnqueBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMUcastQStatsEnqueBytes.setStatus("current")
_BrcdTMUcastQStatsDequePkts_Type = Counter64
_BrcdTMUcastQStatsDequePkts_Object = MibTableColumn
brcdTMUcastQStatsDequePkts = _BrcdTMUcastQStatsDequePkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 3, 1, 8),
    _BrcdTMUcastQStatsDequePkts_Type()
)
brcdTMUcastQStatsDequePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMUcastQStatsDequePkts.setStatus("current")
_BrcdTMUcastQStatsDequeBytes_Type = Counter64
_BrcdTMUcastQStatsDequeBytes_Object = MibTableColumn
brcdTMUcastQStatsDequeBytes = _BrcdTMUcastQStatsDequeBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 3, 1, 9),
    _BrcdTMUcastQStatsDequeBytes_Type()
)
brcdTMUcastQStatsDequeBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMUcastQStatsDequeBytes.setStatus("current")
_BrcdTMUcastQStatsTotalQDiscardPkts_Type = Counter64
_BrcdTMUcastQStatsTotalQDiscardPkts_Object = MibTableColumn
brcdTMUcastQStatsTotalQDiscardPkts = _BrcdTMUcastQStatsTotalQDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 3, 1, 10),
    _BrcdTMUcastQStatsTotalQDiscardPkts_Type()
)
brcdTMUcastQStatsTotalQDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMUcastQStatsTotalQDiscardPkts.setStatus("current")
_BrcdTMUcastQStatsTotalQDiscardBytes_Type = Counter64
_BrcdTMUcastQStatsTotalQDiscardBytes_Object = MibTableColumn
brcdTMUcastQStatsTotalQDiscardBytes = _BrcdTMUcastQStatsTotalQDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 3, 1, 11),
    _BrcdTMUcastQStatsTotalQDiscardBytes_Type()
)
brcdTMUcastQStatsTotalQDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMUcastQStatsTotalQDiscardBytes.setStatus("current")
_BrcdTMUcastQStatsOldestDiscardPkts_Type = Counter64
_BrcdTMUcastQStatsOldestDiscardPkts_Object = MibTableColumn
brcdTMUcastQStatsOldestDiscardPkts = _BrcdTMUcastQStatsOldestDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 3, 1, 12),
    _BrcdTMUcastQStatsOldestDiscardPkts_Type()
)
brcdTMUcastQStatsOldestDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMUcastQStatsOldestDiscardPkts.setStatus("current")
_BrcdTMUcastQStatsOldestDiscardBytes_Type = Counter64
_BrcdTMUcastQStatsOldestDiscardBytes_Object = MibTableColumn
brcdTMUcastQStatsOldestDiscardBytes = _BrcdTMUcastQStatsOldestDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 3, 1, 13),
    _BrcdTMUcastQStatsOldestDiscardBytes_Type()
)
brcdTMUcastQStatsOldestDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMUcastQStatsOldestDiscardBytes.setStatus("current")
_BrcdTMUcastQStatsWREDDroppedPkts_Type = Counter64
_BrcdTMUcastQStatsWREDDroppedPkts_Object = MibTableColumn
brcdTMUcastQStatsWREDDroppedPkts = _BrcdTMUcastQStatsWREDDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 3, 1, 14),
    _BrcdTMUcastQStatsWREDDroppedPkts_Type()
)
brcdTMUcastQStatsWREDDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMUcastQStatsWREDDroppedPkts.setStatus("current")
_BrcdTMUcastQStatsWREDDroppedBytes_Type = Counter64
_BrcdTMUcastQStatsWREDDroppedBytes_Object = MibTableColumn
brcdTMUcastQStatsWREDDroppedBytes = _BrcdTMUcastQStatsWREDDroppedBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 3, 1, 15),
    _BrcdTMUcastQStatsWREDDroppedBytes_Type()
)
brcdTMUcastQStatsWREDDroppedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMUcastQStatsWREDDroppedBytes.setStatus("current")
_BrcdTMUcastQStatsMaxQDepthSinceLastRead_Type = Counter64
_BrcdTMUcastQStatsMaxQDepthSinceLastRead_Object = MibTableColumn
brcdTMUcastQStatsMaxQDepthSinceLastRead = _BrcdTMUcastQStatsMaxQDepthSinceLastRead_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 3, 1, 16),
    _BrcdTMUcastQStatsMaxQDepthSinceLastRead_Type()
)
brcdTMUcastQStatsMaxQDepthSinceLastRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMUcastQStatsMaxQDepthSinceLastRead.setStatus("current")
_BrcdTMUcastQStatsQSize_Type = Unsigned32
_BrcdTMUcastQStatsQSize_Object = MibTableColumn
brcdTMUcastQStatsQSize = _BrcdTMUcastQStatsQSize_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 3, 1, 17),
    _BrcdTMUcastQStatsQSize_Type()
)
brcdTMUcastQStatsQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMUcastQStatsQSize.setStatus("current")
_BrcdTMUcastQStatsCreditCount_Type = Unsigned32
_BrcdTMUcastQStatsCreditCount_Object = MibTableColumn
brcdTMUcastQStatsCreditCount = _BrcdTMUcastQStatsCreditCount_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 3, 1, 18),
    _BrcdTMUcastQStatsCreditCount_Type()
)
brcdTMUcastQStatsCreditCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMUcastQStatsCreditCount.setStatus("current")
_BrcdTMMcastQStatsTable_Object = MibTable
brcdTMMcastQStatsTable = _BrcdTMMcastQStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 4)
)
if mibBuilder.loadTexts:
    brcdTMMcastQStatsTable.setStatus("current")
_BrcdTMMcastQStatsEntry_Object = MibTableRow
brcdTMMcastQStatsEntry = _BrcdTMMcastQStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 4, 1)
)
brcdTMMcastQStatsEntry.setIndexNames(
    (0, "BROCADE-NP-TM-STATS-MIB", "brcdTMMcastQStatsSlotId"),
    (0, "BROCADE-NP-TM-STATS-MIB", "brcdTMMcastQStatsTMDeviceId"),
    (0, "BROCADE-NP-TM-STATS-MIB", "brcdTMMcastQStatsPriority"),
)
if mibBuilder.loadTexts:
    brcdTMMcastQStatsEntry.setStatus("current")
_BrcdTMMcastQStatsSlotId_Type = Unsigned32
_BrcdTMMcastQStatsSlotId_Object = MibTableColumn
brcdTMMcastQStatsSlotId = _BrcdTMMcastQStatsSlotId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 4, 1, 1),
    _BrcdTMMcastQStatsSlotId_Type()
)
brcdTMMcastQStatsSlotId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdTMMcastQStatsSlotId.setStatus("current")
_BrcdTMMcastQStatsTMDeviceId_Type = Unsigned32
_BrcdTMMcastQStatsTMDeviceId_Object = MibTableColumn
brcdTMMcastQStatsTMDeviceId = _BrcdTMMcastQStatsTMDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 4, 1, 2),
    _BrcdTMMcastQStatsTMDeviceId_Type()
)
brcdTMMcastQStatsTMDeviceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdTMMcastQStatsTMDeviceId.setStatus("current")


class _BrcdTMMcastQStatsPriority_Type(Integer32):
    """Custom type brcdTMMcastQStatsPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5,
              7)
        )
    )
    namedValues = NamedValues(
        *(("priority1And2", 1),
          ("priority3And4", 3),
          ("priority5And6", 5),
          ("priority7And8", 7))
    )


_BrcdTMMcastQStatsPriority_Type.__name__ = "Integer32"
_BrcdTMMcastQStatsPriority_Object = MibTableColumn
brcdTMMcastQStatsPriority = _BrcdTMMcastQStatsPriority_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 4, 1, 3),
    _BrcdTMMcastQStatsPriority_Type()
)
brcdTMMcastQStatsPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdTMMcastQStatsPriority.setStatus("current")
_BrcdTMMcastQStatsDescription_Type = DisplayString
_BrcdTMMcastQStatsDescription_Object = MibTableColumn
brcdTMMcastQStatsDescription = _BrcdTMMcastQStatsDescription_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 4, 1, 4),
    _BrcdTMMcastQStatsDescription_Type()
)
brcdTMMcastQStatsDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMMcastQStatsDescription.setStatus("current")
_BrcdTMMcastQStatsEnquePkts_Type = Counter64
_BrcdTMMcastQStatsEnquePkts_Object = MibTableColumn
brcdTMMcastQStatsEnquePkts = _BrcdTMMcastQStatsEnquePkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 4, 1, 5),
    _BrcdTMMcastQStatsEnquePkts_Type()
)
brcdTMMcastQStatsEnquePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMMcastQStatsEnquePkts.setStatus("current")
_BrcdTMMcastQStatsEnqueBytes_Type = Counter64
_BrcdTMMcastQStatsEnqueBytes_Object = MibTableColumn
brcdTMMcastQStatsEnqueBytes = _BrcdTMMcastQStatsEnqueBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 4, 1, 6),
    _BrcdTMMcastQStatsEnqueBytes_Type()
)
brcdTMMcastQStatsEnqueBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMMcastQStatsEnqueBytes.setStatus("current")
_BrcdTMMcastQStatsDequePkts_Type = Counter64
_BrcdTMMcastQStatsDequePkts_Object = MibTableColumn
brcdTMMcastQStatsDequePkts = _BrcdTMMcastQStatsDequePkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 4, 1, 7),
    _BrcdTMMcastQStatsDequePkts_Type()
)
brcdTMMcastQStatsDequePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMMcastQStatsDequePkts.setStatus("current")
_BrcdTMMcastQStatsDequeBytes_Type = Counter64
_BrcdTMMcastQStatsDequeBytes_Object = MibTableColumn
brcdTMMcastQStatsDequeBytes = _BrcdTMMcastQStatsDequeBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 4, 1, 8),
    _BrcdTMMcastQStatsDequeBytes_Type()
)
brcdTMMcastQStatsDequeBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMMcastQStatsDequeBytes.setStatus("current")
_BrcdTMMcastQStatsTotalQDiscardPkts_Type = Counter64
_BrcdTMMcastQStatsTotalQDiscardPkts_Object = MibTableColumn
brcdTMMcastQStatsTotalQDiscardPkts = _BrcdTMMcastQStatsTotalQDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 4, 1, 9),
    _BrcdTMMcastQStatsTotalQDiscardPkts_Type()
)
brcdTMMcastQStatsTotalQDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMMcastQStatsTotalQDiscardPkts.setStatus("current")
_BrcdTMMcastQStatsTotalQDiscardBytes_Type = Counter64
_BrcdTMMcastQStatsTotalQDiscardBytes_Object = MibTableColumn
brcdTMMcastQStatsTotalQDiscardBytes = _BrcdTMMcastQStatsTotalQDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 4, 1, 10),
    _BrcdTMMcastQStatsTotalQDiscardBytes_Type()
)
brcdTMMcastQStatsTotalQDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMMcastQStatsTotalQDiscardBytes.setStatus("current")
_BrcdTMMcastQStatsOldestDiscardPkts_Type = Counter64
_BrcdTMMcastQStatsOldestDiscardPkts_Object = MibTableColumn
brcdTMMcastQStatsOldestDiscardPkts = _BrcdTMMcastQStatsOldestDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 4, 1, 11),
    _BrcdTMMcastQStatsOldestDiscardPkts_Type()
)
brcdTMMcastQStatsOldestDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMMcastQStatsOldestDiscardPkts.setStatus("current")
_BrcdTMMcastQStatsOldestDiscardBytes_Type = Counter64
_BrcdTMMcastQStatsOldestDiscardBytes_Object = MibTableColumn
brcdTMMcastQStatsOldestDiscardBytes = _BrcdTMMcastQStatsOldestDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 4, 1, 12),
    _BrcdTMMcastQStatsOldestDiscardBytes_Type()
)
brcdTMMcastQStatsOldestDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMMcastQStatsOldestDiscardBytes.setStatus("current")
_BrcdTMMcastQStatsWREDDroppedPkts_Type = Counter64
_BrcdTMMcastQStatsWREDDroppedPkts_Object = MibTableColumn
brcdTMMcastQStatsWREDDroppedPkts = _BrcdTMMcastQStatsWREDDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 4, 1, 13),
    _BrcdTMMcastQStatsWREDDroppedPkts_Type()
)
brcdTMMcastQStatsWREDDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMMcastQStatsWREDDroppedPkts.setStatus("current")
_BrcdTMMcastQStatsWREDDroppedBytes_Type = Counter64
_BrcdTMMcastQStatsWREDDroppedBytes_Object = MibTableColumn
brcdTMMcastQStatsWREDDroppedBytes = _BrcdTMMcastQStatsWREDDroppedBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 4, 1, 14),
    _BrcdTMMcastQStatsWREDDroppedBytes_Type()
)
brcdTMMcastQStatsWREDDroppedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMMcastQStatsWREDDroppedBytes.setStatus("current")
_BrcdTMMcastQStatsMaxQDepthSinceLastRead_Type = Counter64
_BrcdTMMcastQStatsMaxQDepthSinceLastRead_Object = MibTableColumn
brcdTMMcastQStatsMaxQDepthSinceLastRead = _BrcdTMMcastQStatsMaxQDepthSinceLastRead_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 4, 1, 15),
    _BrcdTMMcastQStatsMaxQDepthSinceLastRead_Type()
)
brcdTMMcastQStatsMaxQDepthSinceLastRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMMcastQStatsMaxQDepthSinceLastRead.setStatus("current")
_BrcdTMMcastQStatsQSize_Type = Unsigned32
_BrcdTMMcastQStatsQSize_Object = MibTableColumn
brcdTMMcastQStatsQSize = _BrcdTMMcastQStatsQSize_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 4, 1, 16),
    _BrcdTMMcastQStatsQSize_Type()
)
brcdTMMcastQStatsQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMMcastQStatsQSize.setStatus("current")
_BrcdTMMcastQStatsCreditCount_Type = Unsigned32
_BrcdTMMcastQStatsCreditCount_Object = MibTableColumn
brcdTMMcastQStatsCreditCount = _BrcdTMMcastQStatsCreditCount_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 4, 1, 17),
    _BrcdTMMcastQStatsCreditCount_Type()
)
brcdTMMcastQStatsCreditCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMMcastQStatsCreditCount.setStatus("current")
_BrcdTMCpuQStatsTable_Object = MibTable
brcdTMCpuQStatsTable = _BrcdTMCpuQStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 5)
)
if mibBuilder.loadTexts:
    brcdTMCpuQStatsTable.setStatus("current")
_BrcdTMCpuQStatsEntry_Object = MibTableRow
brcdTMCpuQStatsEntry = _BrcdTMCpuQStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 5, 1)
)
brcdTMCpuQStatsEntry.setIndexNames(
    (0, "BROCADE-NP-TM-STATS-MIB", "brcdTMCpuQStatsSlotId"),
    (0, "BROCADE-NP-TM-STATS-MIB", "brcdTMCpuQStatsTMDeviceId"),
    (0, "BROCADE-NP-TM-STATS-MIB", "brcdTMCpuQStatsType"),
    (0, "BROCADE-NP-TM-STATS-MIB", "brcdTMCpuQStatsPriority"),
)
if mibBuilder.loadTexts:
    brcdTMCpuQStatsEntry.setStatus("current")
_BrcdTMCpuQStatsSlotId_Type = Unsigned32
_BrcdTMCpuQStatsSlotId_Object = MibTableColumn
brcdTMCpuQStatsSlotId = _BrcdTMCpuQStatsSlotId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 5, 1, 1),
    _BrcdTMCpuQStatsSlotId_Type()
)
brcdTMCpuQStatsSlotId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdTMCpuQStatsSlotId.setStatus("current")
_BrcdTMCpuQStatsTMDeviceId_Type = Unsigned32
_BrcdTMCpuQStatsTMDeviceId_Object = MibTableColumn
brcdTMCpuQStatsTMDeviceId = _BrcdTMCpuQStatsTMDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 5, 1, 2),
    _BrcdTMCpuQStatsTMDeviceId_Type()
)
brcdTMCpuQStatsTMDeviceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdTMCpuQStatsTMDeviceId.setStatus("current")


class _BrcdTMCpuQStatsType_Type(Integer32):
    """Custom type brcdTMCpuQStatsType based on Integer32"""
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
        *(("cpuQ", 1),
          ("cpuCopyQ", 2),
          ("cpuManagementQ", 3),
          ("cpuProtocolQ", 4))
    )


_BrcdTMCpuQStatsType_Type.__name__ = "Integer32"
_BrcdTMCpuQStatsType_Object = MibTableColumn
brcdTMCpuQStatsType = _BrcdTMCpuQStatsType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 5, 1, 3),
    _BrcdTMCpuQStatsType_Type()
)
brcdTMCpuQStatsType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdTMCpuQStatsType.setStatus("current")
_BrcdTMCpuQStatsPriority_Type = PortPriorityTC
_BrcdTMCpuQStatsPriority_Object = MibTableColumn
brcdTMCpuQStatsPriority = _BrcdTMCpuQStatsPriority_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 5, 1, 4),
    _BrcdTMCpuQStatsPriority_Type()
)
brcdTMCpuQStatsPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdTMCpuQStatsPriority.setStatus("current")
_BrcdTMCpuQStatsDescription_Type = DisplayString
_BrcdTMCpuQStatsDescription_Object = MibTableColumn
brcdTMCpuQStatsDescription = _BrcdTMCpuQStatsDescription_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 5, 1, 5),
    _BrcdTMCpuQStatsDescription_Type()
)
brcdTMCpuQStatsDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMCpuQStatsDescription.setStatus("current")
_BrcdTMCpuQStatsEnquePkts_Type = Counter64
_BrcdTMCpuQStatsEnquePkts_Object = MibTableColumn
brcdTMCpuQStatsEnquePkts = _BrcdTMCpuQStatsEnquePkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 5, 1, 6),
    _BrcdTMCpuQStatsEnquePkts_Type()
)
brcdTMCpuQStatsEnquePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMCpuQStatsEnquePkts.setStatus("current")
_BrcdTMCpuQStatsEnqueBytes_Type = Counter64
_BrcdTMCpuQStatsEnqueBytes_Object = MibTableColumn
brcdTMCpuQStatsEnqueBytes = _BrcdTMCpuQStatsEnqueBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 5, 1, 7),
    _BrcdTMCpuQStatsEnqueBytes_Type()
)
brcdTMCpuQStatsEnqueBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMCpuQStatsEnqueBytes.setStatus("current")
_BrcdTMCpuQStatsDequePkts_Type = Counter64
_BrcdTMCpuQStatsDequePkts_Object = MibTableColumn
brcdTMCpuQStatsDequePkts = _BrcdTMCpuQStatsDequePkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 5, 1, 8),
    _BrcdTMCpuQStatsDequePkts_Type()
)
brcdTMCpuQStatsDequePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMCpuQStatsDequePkts.setStatus("current")
_BrcdTMCpuQStatsDequeBytes_Type = Counter64
_BrcdTMCpuQStatsDequeBytes_Object = MibTableColumn
brcdTMCpuQStatsDequeBytes = _BrcdTMCpuQStatsDequeBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 5, 1, 9),
    _BrcdTMCpuQStatsDequeBytes_Type()
)
brcdTMCpuQStatsDequeBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMCpuQStatsDequeBytes.setStatus("current")
_BrcdTMCpuQStatsTotalQDiscardPkts_Type = Counter64
_BrcdTMCpuQStatsTotalQDiscardPkts_Object = MibTableColumn
brcdTMCpuQStatsTotalQDiscardPkts = _BrcdTMCpuQStatsTotalQDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 5, 1, 10),
    _BrcdTMCpuQStatsTotalQDiscardPkts_Type()
)
brcdTMCpuQStatsTotalQDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMCpuQStatsTotalQDiscardPkts.setStatus("current")
_BrcdTMCpuQStatsTotalQDiscardBytes_Type = Counter64
_BrcdTMCpuQStatsTotalQDiscardBytes_Object = MibTableColumn
brcdTMCpuQStatsTotalQDiscardBytes = _BrcdTMCpuQStatsTotalQDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 5, 1, 11),
    _BrcdTMCpuQStatsTotalQDiscardBytes_Type()
)
brcdTMCpuQStatsTotalQDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMCpuQStatsTotalQDiscardBytes.setStatus("current")
_BrcdTMCpuQStatsOldestDiscardPkts_Type = Counter64
_BrcdTMCpuQStatsOldestDiscardPkts_Object = MibTableColumn
brcdTMCpuQStatsOldestDiscardPkts = _BrcdTMCpuQStatsOldestDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 5, 1, 12),
    _BrcdTMCpuQStatsOldestDiscardPkts_Type()
)
brcdTMCpuQStatsOldestDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMCpuQStatsOldestDiscardPkts.setStatus("current")
_BrcdTMCpuQStatsOldestDiscardBytes_Type = Counter64
_BrcdTMCpuQStatsOldestDiscardBytes_Object = MibTableColumn
brcdTMCpuQStatsOldestDiscardBytes = _BrcdTMCpuQStatsOldestDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 5, 1, 13),
    _BrcdTMCpuQStatsOldestDiscardBytes_Type()
)
brcdTMCpuQStatsOldestDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMCpuQStatsOldestDiscardBytes.setStatus("current")
_BrcdTMCpuQStatsWREDDroppedPkts_Type = Counter64
_BrcdTMCpuQStatsWREDDroppedPkts_Object = MibTableColumn
brcdTMCpuQStatsWREDDroppedPkts = _BrcdTMCpuQStatsWREDDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 5, 1, 14),
    _BrcdTMCpuQStatsWREDDroppedPkts_Type()
)
brcdTMCpuQStatsWREDDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMCpuQStatsWREDDroppedPkts.setStatus("current")
_BrcdTMCpuQStatsWREDDroppedBytes_Type = Counter64
_BrcdTMCpuQStatsWREDDroppedBytes_Object = MibTableColumn
brcdTMCpuQStatsWREDDroppedBytes = _BrcdTMCpuQStatsWREDDroppedBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 5, 1, 15),
    _BrcdTMCpuQStatsWREDDroppedBytes_Type()
)
brcdTMCpuQStatsWREDDroppedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMCpuQStatsWREDDroppedBytes.setStatus("current")
_BrcdTMCpuQStatsMaxQDepthSinceLastRead_Type = Counter64
_BrcdTMCpuQStatsMaxQDepthSinceLastRead_Object = MibTableColumn
brcdTMCpuQStatsMaxQDepthSinceLastRead = _BrcdTMCpuQStatsMaxQDepthSinceLastRead_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 5, 1, 16),
    _BrcdTMCpuQStatsMaxQDepthSinceLastRead_Type()
)
brcdTMCpuQStatsMaxQDepthSinceLastRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMCpuQStatsMaxQDepthSinceLastRead.setStatus("current")
_BrcdTMCpuQStatsQSize_Type = Unsigned32
_BrcdTMCpuQStatsQSize_Object = MibTableColumn
brcdTMCpuQStatsQSize = _BrcdTMCpuQStatsQSize_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 5, 1, 17),
    _BrcdTMCpuQStatsQSize_Type()
)
brcdTMCpuQStatsQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMCpuQStatsQSize.setStatus("current")
_BrcdTMCpuQStatsCreditCount_Type = Unsigned32
_BrcdTMCpuQStatsCreditCount_Object = MibTableColumn
brcdTMCpuQStatsCreditCount = _BrcdTMCpuQStatsCreditCount_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 5, 1, 18),
    _BrcdTMCpuQStatsCreditCount_Type()
)
brcdTMCpuQStatsCreditCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMCpuQStatsCreditCount.setStatus("current")
_BrcdTMMcastStreamQStatsTable_Object = MibTable
brcdTMMcastStreamQStatsTable = _BrcdTMMcastStreamQStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 6)
)
if mibBuilder.loadTexts:
    brcdTMMcastStreamQStatsTable.setStatus("current")
_BrcdTMMcastStreamQStatsEntry_Object = MibTableRow
brcdTMMcastStreamQStatsEntry = _BrcdTMMcastStreamQStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 6, 1)
)
brcdTMMcastStreamQStatsEntry.setIndexNames(
    (0, "BROCADE-NP-TM-STATS-MIB", "brcdTMMcastStreamQStatsAddressType"),
    (0, "BROCADE-NP-TM-STATS-MIB", "brcdTMMcastStreamQStatsSource"),
    (0, "BROCADE-NP-TM-STATS-MIB", "brcdTMMcastStreamQStatsGroup"),
    (0, "BROCADE-NP-TM-STATS-MIB", "brcdTMMcastStreamQStatsGroupPrefixLength"),
)
if mibBuilder.loadTexts:
    brcdTMMcastStreamQStatsEntry.setStatus("current")
_BrcdTMMcastStreamQStatsAddressType_Type = InetAddressType
_BrcdTMMcastStreamQStatsAddressType_Object = MibTableColumn
brcdTMMcastStreamQStatsAddressType = _BrcdTMMcastStreamQStatsAddressType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 6, 1, 1),
    _BrcdTMMcastStreamQStatsAddressType_Type()
)
brcdTMMcastStreamQStatsAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdTMMcastStreamQStatsAddressType.setStatus("current")
_BrcdTMMcastStreamQStatsSource_Type = InetAddress
_BrcdTMMcastStreamQStatsSource_Object = MibTableColumn
brcdTMMcastStreamQStatsSource = _BrcdTMMcastStreamQStatsSource_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 6, 1, 2),
    _BrcdTMMcastStreamQStatsSource_Type()
)
brcdTMMcastStreamQStatsSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdTMMcastStreamQStatsSource.setStatus("current")
_BrcdTMMcastStreamQStatsGroup_Type = InetAddress
_BrcdTMMcastStreamQStatsGroup_Object = MibTableColumn
brcdTMMcastStreamQStatsGroup = _BrcdTMMcastStreamQStatsGroup_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 6, 1, 3),
    _BrcdTMMcastStreamQStatsGroup_Type()
)
brcdTMMcastStreamQStatsGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdTMMcastStreamQStatsGroup.setStatus("current")
_BrcdTMMcastStreamQStatsGroupPrefixLength_Type = InetAddressPrefixLength
_BrcdTMMcastStreamQStatsGroupPrefixLength_Object = MibTableColumn
brcdTMMcastStreamQStatsGroupPrefixLength = _BrcdTMMcastStreamQStatsGroupPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 6, 1, 4),
    _BrcdTMMcastStreamQStatsGroupPrefixLength_Type()
)
brcdTMMcastStreamQStatsGroupPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdTMMcastStreamQStatsGroupPrefixLength.setStatus("current")


class _BrcdTMMcastStreamQStatsPriority_Type(Integer32):
    """Custom type brcdTMMcastStreamQStatsPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5,
              7)
        )
    )
    namedValues = NamedValues(
        *(("priority1And2", 1),
          ("priority3And4", 3),
          ("priority5And6", 5),
          ("priority7And8", 7))
    )


_BrcdTMMcastStreamQStatsPriority_Type.__name__ = "Integer32"
_BrcdTMMcastStreamQStatsPriority_Object = MibTableColumn
brcdTMMcastStreamQStatsPriority = _BrcdTMMcastStreamQStatsPriority_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 6, 1, 5),
    _BrcdTMMcastStreamQStatsPriority_Type()
)
brcdTMMcastStreamQStatsPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMMcastStreamQStatsPriority.setStatus("current")
_BrcdTMMcastStreamQStatsEnquePkts_Type = Counter64
_BrcdTMMcastStreamQStatsEnquePkts_Object = MibTableColumn
brcdTMMcastStreamQStatsEnquePkts = _BrcdTMMcastStreamQStatsEnquePkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 6, 1, 6),
    _BrcdTMMcastStreamQStatsEnquePkts_Type()
)
brcdTMMcastStreamQStatsEnquePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMMcastStreamQStatsEnquePkts.setStatus("current")
_BrcdTMMcastStreamQStatsEnqueBytes_Type = Counter64
_BrcdTMMcastStreamQStatsEnqueBytes_Object = MibTableColumn
brcdTMMcastStreamQStatsEnqueBytes = _BrcdTMMcastStreamQStatsEnqueBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 6, 1, 7),
    _BrcdTMMcastStreamQStatsEnqueBytes_Type()
)
brcdTMMcastStreamQStatsEnqueBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMMcastStreamQStatsEnqueBytes.setStatus("current")
_BrcdTMMcastStreamQStatsDequePkts_Type = Counter64
_BrcdTMMcastStreamQStatsDequePkts_Object = MibTableColumn
brcdTMMcastStreamQStatsDequePkts = _BrcdTMMcastStreamQStatsDequePkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 6, 1, 8),
    _BrcdTMMcastStreamQStatsDequePkts_Type()
)
brcdTMMcastStreamQStatsDequePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMMcastStreamQStatsDequePkts.setStatus("current")
_BrcdTMMcastStreamQStatsDequeBytes_Type = Counter64
_BrcdTMMcastStreamQStatsDequeBytes_Object = MibTableColumn
brcdTMMcastStreamQStatsDequeBytes = _BrcdTMMcastStreamQStatsDequeBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 6, 1, 9),
    _BrcdTMMcastStreamQStatsDequeBytes_Type()
)
brcdTMMcastStreamQStatsDequeBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMMcastStreamQStatsDequeBytes.setStatus("current")
_BrcdTMMcastStreamQStatsTotalQDiscardPkts_Type = Counter64
_BrcdTMMcastStreamQStatsTotalQDiscardPkts_Object = MibTableColumn
brcdTMMcastStreamQStatsTotalQDiscardPkts = _BrcdTMMcastStreamQStatsTotalQDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 6, 1, 10),
    _BrcdTMMcastStreamQStatsTotalQDiscardPkts_Type()
)
brcdTMMcastStreamQStatsTotalQDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMMcastStreamQStatsTotalQDiscardPkts.setStatus("current")
_BrcdTMMcastStreamQStatsTotalQDiscardBytes_Type = Counter64
_BrcdTMMcastStreamQStatsTotalQDiscardBytes_Object = MibTableColumn
brcdTMMcastStreamQStatsTotalQDiscardBytes = _BrcdTMMcastStreamQStatsTotalQDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 6, 1, 11),
    _BrcdTMMcastStreamQStatsTotalQDiscardBytes_Type()
)
brcdTMMcastStreamQStatsTotalQDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMMcastStreamQStatsTotalQDiscardBytes.setStatus("current")
_BrcdTMMcastStreamQStatsOldestDiscardPkts_Type = Counter64
_BrcdTMMcastStreamQStatsOldestDiscardPkts_Object = MibTableColumn
brcdTMMcastStreamQStatsOldestDiscardPkts = _BrcdTMMcastStreamQStatsOldestDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 6, 1, 12),
    _BrcdTMMcastStreamQStatsOldestDiscardPkts_Type()
)
brcdTMMcastStreamQStatsOldestDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMMcastStreamQStatsOldestDiscardPkts.setStatus("current")
_BrcdTMMcastStreamQStatsOldestDiscardBytes_Type = Counter64
_BrcdTMMcastStreamQStatsOldestDiscardBytes_Object = MibTableColumn
brcdTMMcastStreamQStatsOldestDiscardBytes = _BrcdTMMcastStreamQStatsOldestDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 6, 1, 13),
    _BrcdTMMcastStreamQStatsOldestDiscardBytes_Type()
)
brcdTMMcastStreamQStatsOldestDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMMcastStreamQStatsOldestDiscardBytes.setStatus("current")
_BrcdTMMcastStreamQStatsWREDDroppedPkts_Type = Counter64
_BrcdTMMcastStreamQStatsWREDDroppedPkts_Object = MibTableColumn
brcdTMMcastStreamQStatsWREDDroppedPkts = _BrcdTMMcastStreamQStatsWREDDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 6, 1, 14),
    _BrcdTMMcastStreamQStatsWREDDroppedPkts_Type()
)
brcdTMMcastStreamQStatsWREDDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMMcastStreamQStatsWREDDroppedPkts.setStatus("current")
_BrcdTMMcastStreamQStatsWREDDroppedBytes_Type = Counter64
_BrcdTMMcastStreamQStatsWREDDroppedBytes_Object = MibTableColumn
brcdTMMcastStreamQStatsWREDDroppedBytes = _BrcdTMMcastStreamQStatsWREDDroppedBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 6, 1, 15),
    _BrcdTMMcastStreamQStatsWREDDroppedBytes_Type()
)
brcdTMMcastStreamQStatsWREDDroppedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMMcastStreamQStatsWREDDroppedBytes.setStatus("current")
_BrcdTMMcastStreamQStatsMaxQDepthSinceLastRead_Type = Counter64
_BrcdTMMcastStreamQStatsMaxQDepthSinceLastRead_Object = MibTableColumn
brcdTMMcastStreamQStatsMaxQDepthSinceLastRead = _BrcdTMMcastStreamQStatsMaxQDepthSinceLastRead_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 6, 1, 16),
    _BrcdTMMcastStreamQStatsMaxQDepthSinceLastRead_Type()
)
brcdTMMcastStreamQStatsMaxQDepthSinceLastRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMMcastStreamQStatsMaxQDepthSinceLastRead.setStatus("current")
_BrcdTMMcastStreamQStatsQSize_Type = Unsigned32
_BrcdTMMcastStreamQStatsQSize_Object = MibTableColumn
brcdTMMcastStreamQStatsQSize = _BrcdTMMcastStreamQStatsQSize_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 6, 1, 17),
    _BrcdTMMcastStreamQStatsQSize_Type()
)
brcdTMMcastStreamQStatsQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMMcastStreamQStatsQSize.setStatus("current")
_BrcdTMMcastStreamQStatsCreditCount_Type = Unsigned32
_BrcdTMMcastStreamQStatsCreditCount_Object = MibTableColumn
brcdTMMcastStreamQStatsCreditCount = _BrcdTMMcastStreamQStatsCreditCount_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 6, 1, 18),
    _BrcdTMMcastStreamQStatsCreditCount_Type()
)
brcdTMMcastStreamQStatsCreditCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMMcastStreamQStatsCreditCount.setStatus("current")
_BrcdTMCpuQInfoTable_Object = MibTable
brcdTMCpuQInfoTable = _BrcdTMCpuQInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 7)
)
if mibBuilder.loadTexts:
    brcdTMCpuQInfoTable.setStatus("current")
_BrcdTMCpuQInfoEntry_Object = MibTableRow
brcdTMCpuQInfoEntry = _BrcdTMCpuQInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 7, 1)
)
brcdTMCpuQInfoEntry.setIndexNames(
    (0, "BROCADE-NP-TM-STATS-MIB", "brcdTMCpuQInfoSlotId"),
    (0, "BROCADE-NP-TM-STATS-MIB", "brcdTMCpuQInfoTMDeviceId"),
)
if mibBuilder.loadTexts:
    brcdTMCpuQInfoEntry.setStatus("current")
_BrcdTMCpuQInfoSlotId_Type = Unsigned32
_BrcdTMCpuQInfoSlotId_Object = MibTableColumn
brcdTMCpuQInfoSlotId = _BrcdTMCpuQInfoSlotId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 7, 1, 1),
    _BrcdTMCpuQInfoSlotId_Type()
)
brcdTMCpuQInfoSlotId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdTMCpuQInfoSlotId.setStatus("current")
_BrcdTMCpuQInfoTMDeviceId_Type = Unsigned32
_BrcdTMCpuQInfoTMDeviceId_Object = MibTableColumn
brcdTMCpuQInfoTMDeviceId = _BrcdTMCpuQInfoTMDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 7, 1, 2),
    _BrcdTMCpuQInfoTMDeviceId_Type()
)
brcdTMCpuQInfoTMDeviceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdTMCpuQInfoTMDeviceId.setStatus("current")
_BrcdTMCpuQInfoPriority0QSize_Type = Unsigned32
_BrcdTMCpuQInfoPriority0QSize_Object = MibTableColumn
brcdTMCpuQInfoPriority0QSize = _BrcdTMCpuQInfoPriority0QSize_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 7, 1, 3),
    _BrcdTMCpuQInfoPriority0QSize_Type()
)
brcdTMCpuQInfoPriority0QSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMCpuQInfoPriority0QSize.setStatus("current")
_BrcdTMCpuQInfoPriority0CreditCount_Type = Unsigned32
_BrcdTMCpuQInfoPriority0CreditCount_Object = MibTableColumn
brcdTMCpuQInfoPriority0CreditCount = _BrcdTMCpuQInfoPriority0CreditCount_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 7, 1, 4),
    _BrcdTMCpuQInfoPriority0CreditCount_Type()
)
brcdTMCpuQInfoPriority0CreditCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMCpuQInfoPriority0CreditCount.setStatus("current")
_BrcdTMCpuQInfoPriority1QSize_Type = Unsigned32
_BrcdTMCpuQInfoPriority1QSize_Object = MibTableColumn
brcdTMCpuQInfoPriority1QSize = _BrcdTMCpuQInfoPriority1QSize_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 7, 1, 5),
    _BrcdTMCpuQInfoPriority1QSize_Type()
)
brcdTMCpuQInfoPriority1QSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMCpuQInfoPriority1QSize.setStatus("current")
_BrcdTMCpuQInfoPriority1CreditCount_Type = Unsigned32
_BrcdTMCpuQInfoPriority1CreditCount_Object = MibTableColumn
brcdTMCpuQInfoPriority1CreditCount = _BrcdTMCpuQInfoPriority1CreditCount_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 7, 1, 6),
    _BrcdTMCpuQInfoPriority1CreditCount_Type()
)
brcdTMCpuQInfoPriority1CreditCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMCpuQInfoPriority1CreditCount.setStatus("current")
_BrcdTMCpuQInfoPriority2QSize_Type = Unsigned32
_BrcdTMCpuQInfoPriority2QSize_Object = MibTableColumn
brcdTMCpuQInfoPriority2QSize = _BrcdTMCpuQInfoPriority2QSize_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 7, 1, 7),
    _BrcdTMCpuQInfoPriority2QSize_Type()
)
brcdTMCpuQInfoPriority2QSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMCpuQInfoPriority2QSize.setStatus("current")
_BrcdTMCpuQInfoPriority2CreditCount_Type = Unsigned32
_BrcdTMCpuQInfoPriority2CreditCount_Object = MibTableColumn
brcdTMCpuQInfoPriority2CreditCount = _BrcdTMCpuQInfoPriority2CreditCount_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 7, 1, 8),
    _BrcdTMCpuQInfoPriority2CreditCount_Type()
)
brcdTMCpuQInfoPriority2CreditCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMCpuQInfoPriority2CreditCount.setStatus("current")
_BrcdTMCpuQInfoPriority3QSize_Type = Unsigned32
_BrcdTMCpuQInfoPriority3QSize_Object = MibTableColumn
brcdTMCpuQInfoPriority3QSize = _BrcdTMCpuQInfoPriority3QSize_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 7, 1, 9),
    _BrcdTMCpuQInfoPriority3QSize_Type()
)
brcdTMCpuQInfoPriority3QSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMCpuQInfoPriority3QSize.setStatus("current")
_BrcdTMCpuQInfoPriority3CreditCount_Type = Unsigned32
_BrcdTMCpuQInfoPriority3CreditCount_Object = MibTableColumn
brcdTMCpuQInfoPriority3CreditCount = _BrcdTMCpuQInfoPriority3CreditCount_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 7, 1, 10),
    _BrcdTMCpuQInfoPriority3CreditCount_Type()
)
brcdTMCpuQInfoPriority3CreditCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMCpuQInfoPriority3CreditCount.setStatus("current")
_BrcdTMCpuQInfoPriority4QSize_Type = Unsigned32
_BrcdTMCpuQInfoPriority4QSize_Object = MibTableColumn
brcdTMCpuQInfoPriority4QSize = _BrcdTMCpuQInfoPriority4QSize_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 7, 1, 11),
    _BrcdTMCpuQInfoPriority4QSize_Type()
)
brcdTMCpuQInfoPriority4QSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMCpuQInfoPriority4QSize.setStatus("current")
_BrcdTMCpuQInfoPriority4CreditCount_Type = Unsigned32
_BrcdTMCpuQInfoPriority4CreditCount_Object = MibTableColumn
brcdTMCpuQInfoPriority4CreditCount = _BrcdTMCpuQInfoPriority4CreditCount_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 7, 1, 12),
    _BrcdTMCpuQInfoPriority4CreditCount_Type()
)
brcdTMCpuQInfoPriority4CreditCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMCpuQInfoPriority4CreditCount.setStatus("current")
_BrcdTMCpuQInfoPriority5QSize_Type = Unsigned32
_BrcdTMCpuQInfoPriority5QSize_Object = MibTableColumn
brcdTMCpuQInfoPriority5QSize = _BrcdTMCpuQInfoPriority5QSize_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 7, 1, 13),
    _BrcdTMCpuQInfoPriority5QSize_Type()
)
brcdTMCpuQInfoPriority5QSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMCpuQInfoPriority5QSize.setStatus("current")
_BrcdTMCpuQInfoPriority5CreditCount_Type = Unsigned32
_BrcdTMCpuQInfoPriority5CreditCount_Object = MibTableColumn
brcdTMCpuQInfoPriority5CreditCount = _BrcdTMCpuQInfoPriority5CreditCount_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 7, 1, 14),
    _BrcdTMCpuQInfoPriority5CreditCount_Type()
)
brcdTMCpuQInfoPriority5CreditCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMCpuQInfoPriority5CreditCount.setStatus("current")
_BrcdTMCpuQInfoPriority6QSize_Type = Unsigned32
_BrcdTMCpuQInfoPriority6QSize_Object = MibTableColumn
brcdTMCpuQInfoPriority6QSize = _BrcdTMCpuQInfoPriority6QSize_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 7, 1, 15),
    _BrcdTMCpuQInfoPriority6QSize_Type()
)
brcdTMCpuQInfoPriority6QSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMCpuQInfoPriority6QSize.setStatus("current")
_BrcdTMCpuQInfoPriority6CreditCount_Type = Unsigned32
_BrcdTMCpuQInfoPriority6CreditCount_Object = MibTableColumn
brcdTMCpuQInfoPriority6CreditCount = _BrcdTMCpuQInfoPriority6CreditCount_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 7, 1, 16),
    _BrcdTMCpuQInfoPriority6CreditCount_Type()
)
brcdTMCpuQInfoPriority6CreditCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMCpuQInfoPriority6CreditCount.setStatus("current")
_BrcdTMCpuQInfoPriority7QSize_Type = Unsigned32
_BrcdTMCpuQInfoPriority7QSize_Object = MibTableColumn
brcdTMCpuQInfoPriority7QSize = _BrcdTMCpuQInfoPriority7QSize_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 7, 1, 17),
    _BrcdTMCpuQInfoPriority7QSize_Type()
)
brcdTMCpuQInfoPriority7QSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMCpuQInfoPriority7QSize.setStatus("current")
_BrcdTMCpuQInfoPriority7CreditCount_Type = Unsigned32
_BrcdTMCpuQInfoPriority7CreditCount_Object = MibTableColumn
brcdTMCpuQInfoPriority7CreditCount = _BrcdTMCpuQInfoPriority7CreditCount_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 7, 1, 18),
    _BrcdTMCpuQInfoPriority7CreditCount_Type()
)
brcdTMCpuQInfoPriority7CreditCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMCpuQInfoPriority7CreditCount.setStatus("current")
_BrcdTMDestUcastQStatTable_Object = MibTable
brcdTMDestUcastQStatTable = _BrcdTMDestUcastQStatTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 8)
)
if mibBuilder.loadTexts:
    brcdTMDestUcastQStatTable.setStatus("current")
_BrcdTMDestUcastQStatEntry_Object = MibTableRow
brcdTMDestUcastQStatEntry = _BrcdTMDestUcastQStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 8, 1)
)
brcdTMDestUcastQStatEntry.setIndexNames(
    (0, "BROCADE-NP-TM-STATS-MIB", "brcdTMDestUcastQStatDestIfIndex"),
    (0, "BROCADE-NP-TM-STATS-MIB", "brcdTMDestUcastQStatPriority"),
)
if mibBuilder.loadTexts:
    brcdTMDestUcastQStatEntry.setStatus("current")
_BrcdTMDestUcastQStatDestIfIndex_Type = InterfaceIndex
_BrcdTMDestUcastQStatDestIfIndex_Object = MibTableColumn
brcdTMDestUcastQStatDestIfIndex = _BrcdTMDestUcastQStatDestIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 8, 1, 1),
    _BrcdTMDestUcastQStatDestIfIndex_Type()
)
brcdTMDestUcastQStatDestIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdTMDestUcastQStatDestIfIndex.setStatus("current")
_BrcdTMDestUcastQStatPriority_Type = PortPriorityTC
_BrcdTMDestUcastQStatPriority_Object = MibTableColumn
brcdTMDestUcastQStatPriority = _BrcdTMDestUcastQStatPriority_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 8, 1, 2),
    _BrcdTMDestUcastQStatPriority_Type()
)
brcdTMDestUcastQStatPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdTMDestUcastQStatPriority.setStatus("current")
_BrcdTMDestUcastQStatEnquePkts_Type = Counter64
_BrcdTMDestUcastQStatEnquePkts_Object = MibTableColumn
brcdTMDestUcastQStatEnquePkts = _BrcdTMDestUcastQStatEnquePkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 8, 1, 3),
    _BrcdTMDestUcastQStatEnquePkts_Type()
)
brcdTMDestUcastQStatEnquePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMDestUcastQStatEnquePkts.setStatus("current")
_BrcdTMDestUcastQStatEnqueBytes_Type = Counter64
_BrcdTMDestUcastQStatEnqueBytes_Object = MibTableColumn
brcdTMDestUcastQStatEnqueBytes = _BrcdTMDestUcastQStatEnqueBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 8, 1, 4),
    _BrcdTMDestUcastQStatEnqueBytes_Type()
)
brcdTMDestUcastQStatEnqueBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMDestUcastQStatEnqueBytes.setStatus("current")
_BrcdTMDestUcastQStatDequePkts_Type = Counter64
_BrcdTMDestUcastQStatDequePkts_Object = MibTableColumn
brcdTMDestUcastQStatDequePkts = _BrcdTMDestUcastQStatDequePkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 8, 1, 5),
    _BrcdTMDestUcastQStatDequePkts_Type()
)
brcdTMDestUcastQStatDequePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMDestUcastQStatDequePkts.setStatus("current")
_BrcdTMDestUcastQStatDequeBytes_Type = Counter64
_BrcdTMDestUcastQStatDequeBytes_Object = MibTableColumn
brcdTMDestUcastQStatDequeBytes = _BrcdTMDestUcastQStatDequeBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 8, 1, 6),
    _BrcdTMDestUcastQStatDequeBytes_Type()
)
brcdTMDestUcastQStatDequeBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMDestUcastQStatDequeBytes.setStatus("current")
_BrcdTMDestUcastQStatTotalQDiscardPkts_Type = Counter64
_BrcdTMDestUcastQStatTotalQDiscardPkts_Object = MibTableColumn
brcdTMDestUcastQStatTotalQDiscardPkts = _BrcdTMDestUcastQStatTotalQDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 8, 1, 7),
    _BrcdTMDestUcastQStatTotalQDiscardPkts_Type()
)
brcdTMDestUcastQStatTotalQDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMDestUcastQStatTotalQDiscardPkts.setStatus("current")
_BrcdTMDestUcastQStatTotalQDiscardBytes_Type = Counter64
_BrcdTMDestUcastQStatTotalQDiscardBytes_Object = MibTableColumn
brcdTMDestUcastQStatTotalQDiscardBytes = _BrcdTMDestUcastQStatTotalQDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 2, 1, 2, 8, 1, 8),
    _BrcdTMDestUcastQStatTotalQDiscardBytes_Type()
)
brcdTMDestUcastQStatTotalQDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdTMDestUcastQStatTotalQDiscardBytes.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BROCADE-NP-TM-STATS-MIB",
    **{"brocadeNPTMStatsMIB": brocadeNPTMStatsMIB,
       "brcdNPTMMIBObjects": brcdNPTMMIBObjects,
       "brcdNPStatisticsInfo": brcdNPStatisticsInfo,
       "brcdNPStatsTable": brcdNPStatsTable,
       "brcdNPStatsEntry": brcdNPStatsEntry,
       "brcdNPStatsIfIndex": brcdNPStatsIfIndex,
       "brcdNPStatsRxRawGoodPkts": brcdNPStatsRxRawGoodPkts,
       "brcdNPStatsRxForwardPkts": brcdNPStatsRxForwardPkts,
       "brcdNPStatsRxDiscardPkts": brcdNPStatsRxDiscardPkts,
       "brcdNPStatsRxMiscPkts": brcdNPStatsRxMiscPkts,
       "brcdNPStatsRxUnicastPkts": brcdNPStatsRxUnicastPkts,
       "brcdNPStatsRxBroadcastPkts": brcdNPStatsRxBroadcastPkts,
       "brcdNPStatsRxMulticastPkts": brcdNPStatsRxMulticastPkts,
       "brcdNPStatsRxSendToTMPkts": brcdNPStatsRxSendToTMPkts,
       "brcdNPStatsRxBadPkts": brcdNPStatsRxBadPkts,
       "brcdNPStatsRxLookupUnavailable": brcdNPStatsRxLookupUnavailable,
       "brcdNPStatsRxACLDrop": brcdNPStatsRxACLDrop,
       "brcdNPStatsRxPriority0And1Drop": brcdNPStatsRxPriority0And1Drop,
       "brcdNPStatsRxPriority2And3Drop": brcdNPStatsRxPriority2And3Drop,
       "brcdNPStatsRxPriority4And5Drop": brcdNPStatsRxPriority4And5Drop,
       "brcdNPStatsRxPriority6And7Drop": brcdNPStatsRxPriority6And7Drop,
       "brcdNPStatsRxSuppressRPFDrop": brcdNPStatsRxSuppressRPFDrop,
       "brcdNPStatsRxRPFDrop": brcdNPStatsRxRPFDrop,
       "brcdNPStatsRxIPv4Pkts": brcdNPStatsRxIPv4Pkts,
       "brcdNPStatsRxIPv6Pkts": brcdNPStatsRxIPv6Pkts,
       "brcdNPStatsRxRouteOnlyDrop": brcdNPStatsRxRouteOnlyDrop,
       "brcdNPStatsRxIPv6SuppressRPFDrop": brcdNPStatsRxIPv6SuppressRPFDrop,
       "brcdNPStatsRxIPv6RPFDropCount": brcdNPStatsRxIPv6RPFDropCount,
       "brcdNPStatsRxIPv4Bytes": brcdNPStatsRxIPv4Bytes,
       "brcdNPStatsRxIPv6Bytes": brcdNPStatsRxIPv6Bytes,
       "brcdNPStatsRxPOSCtrlProtocolPkts": brcdNPStatsRxPOSCtrlProtocolPkts,
       "brcdNPStatsRxPOSLinkDrop": brcdNPStatsRxPOSLinkDrop,
       "brcdNPStatsRxRoutedPktsDrop": brcdNPStatsRxRoutedPktsDrop,
       "brcdNPStatsTxSentToMACPkts": brcdNPStatsTxSentToMACPkts,
       "brcdNPStatsTxRawGoodPkts": brcdNPStatsTxRawGoodPkts,
       "brcdNPStatsTxSrcPortSupressDrop": brcdNPStatsTxSrcPortSupressDrop,
       "brcdNPStatsTxBadPktsCnt": brcdNPStatsTxBadPktsCnt,
       "brcdNPStatsTxUnicastPkts": brcdNPStatsTxUnicastPkts,
       "brcdNPStatsTxBroadcastPkts": brcdNPStatsTxBroadcastPkts,
       "brcdNPStatsTxMulticastPkts": brcdNPStatsTxMulticastPkts,
       "brcdNPStatsTxReceiveFromTM": brcdNPStatsTxReceiveFromTM,
       "brcdNPStatsTxACLDrop": brcdNPStatsTxACLDrop,
       "brcdNPStatsTxPFCMulticastDrop": brcdNPStatsTxPFCMulticastDrop,
       "brcdNPStatsTxPFCMTUExceedDrop": brcdNPStatsTxPFCMTUExceedDrop,
       "brcdNPStatsTxPFCQMAPErrorDrop": brcdNPStatsTxPFCQMAPErrorDrop,
       "brcdNPStatsTxIPv4Pkts": brcdNPStatsTxIPv4Pkts,
       "brcdNPStatsTxIPv6Pkts": brcdNPStatsTxIPv6Pkts,
       "brcdNPStatsTxIPv4Bytes": brcdNPStatsTxIPv4Bytes,
       "brcdNPStatsTxIPv6Bytes": brcdNPStatsTxIPv6Bytes,
       "brcdNPStatsTxPOSCtrlProtocolPkts": brcdNPStatsTxPOSCtrlProtocolPkts,
       "brcdNPStatsTxPOSLinkDrop": brcdNPStatsTxPOSLinkDrop,
       "brcdNPQosStatTable": brcdNPQosStatTable,
       "brcdNPQosStatEntry": brcdNPQosStatEntry,
       "brcdNPQosStatIfIndex": brcdNPQosStatIfIndex,
       "brcdNPQosStatQosPriority": brcdNPQosStatQosPriority,
       "brcdNPQosStatIngressPkts": brcdNPQosStatIngressPkts,
       "brcdNPQosStatIngressBytes": brcdNPQosStatIngressBytes,
       "brcdNPQosStatEgressPkts": brcdNPQosStatEgressPkts,
       "brcdNPQosStatEgressBytes": brcdNPQosStatEgressBytes,
       "brcdTMStatisticsInfo": brcdTMStatisticsInfo,
       "brcdTMStatisticsInfoGroup": brcdTMStatisticsInfoGroup,
       "brcdTMPortMappingMaxPorts": brcdTMPortMappingMaxPorts,
       "brcdTMPortMappingUsedPorts": brcdTMPortMappingUsedPorts,
       "brcdTMPortMappingAvailablePorts": brcdTMPortMappingAvailablePorts,
       "brcdTMStatsTable": brcdTMStatsTable,
       "brcdTMStatsEntry": brcdTMStatsEntry,
       "brcdTMStatsSlotId": brcdTMStatsSlotId,
       "brcdTMStatsTMDeviceId": brcdTMStatsTMDeviceId,
       "brcdTMStatsDescription": brcdTMStatsDescription,
       "brcdTMStatsTotalIngressPktsCnt": brcdTMStatsTotalIngressPktsCnt,
       "brcdTMStatsIngressEnqueuePkts": brcdTMStatsIngressEnqueuePkts,
       "brcdTMStatsEgressEnqueuePkts": brcdTMStatsEgressEnqueuePkts,
       "brcdTMStatsIngressEnqueueBytes": brcdTMStatsIngressEnqueueBytes,
       "brcdTMStatsEgressEnqueueBytes": brcdTMStatsEgressEnqueueBytes,
       "brcdTMStatsIngressDequeuePkts": brcdTMStatsIngressDequeuePkts,
       "brcdTMStatsIngressDequeueBytes": brcdTMStatsIngressDequeueBytes,
       "brcdTMStatsIngressTotalQDiscardPkts": brcdTMStatsIngressTotalQDiscardPkts,
       "brcdTMStatsIngressTotalQDiscardBytes": brcdTMStatsIngressTotalQDiscardBytes,
       "brcdTMStatsIngressOldestDiscardPkts": brcdTMStatsIngressOldestDiscardPkts,
       "brcdTMStatsIngressOldestDiscardBytes": brcdTMStatsIngressOldestDiscardBytes,
       "brcdTMStatsEgressDiscardPkts": brcdTMStatsEgressDiscardPkts,
       "brcdTMStatsEgressDiscardBytes": brcdTMStatsEgressDiscardBytes,
       "brcdTMUcastQStatsTable": brcdTMUcastQStatsTable,
       "brcdTMUcastQStatsEntry": brcdTMUcastQStatsEntry,
       "brcdTMUcastQStatsSlotId": brcdTMUcastQStatsSlotId,
       "brcdTMUcastQStatsTMDeviceId": brcdTMUcastQStatsTMDeviceId,
       "brcdTMUcastQStatsDstIfIndex": brcdTMUcastQStatsDstIfIndex,
       "brcdTMUcastQStatsPriority": brcdTMUcastQStatsPriority,
       "brcdTMUcastQStatsDescription": brcdTMUcastQStatsDescription,
       "brcdTMUcastQStatsEnquePkts": brcdTMUcastQStatsEnquePkts,
       "brcdTMUcastQStatsEnqueBytes": brcdTMUcastQStatsEnqueBytes,
       "brcdTMUcastQStatsDequePkts": brcdTMUcastQStatsDequePkts,
       "brcdTMUcastQStatsDequeBytes": brcdTMUcastQStatsDequeBytes,
       "brcdTMUcastQStatsTotalQDiscardPkts": brcdTMUcastQStatsTotalQDiscardPkts,
       "brcdTMUcastQStatsTotalQDiscardBytes": brcdTMUcastQStatsTotalQDiscardBytes,
       "brcdTMUcastQStatsOldestDiscardPkts": brcdTMUcastQStatsOldestDiscardPkts,
       "brcdTMUcastQStatsOldestDiscardBytes": brcdTMUcastQStatsOldestDiscardBytes,
       "brcdTMUcastQStatsWREDDroppedPkts": brcdTMUcastQStatsWREDDroppedPkts,
       "brcdTMUcastQStatsWREDDroppedBytes": brcdTMUcastQStatsWREDDroppedBytes,
       "brcdTMUcastQStatsMaxQDepthSinceLastRead": brcdTMUcastQStatsMaxQDepthSinceLastRead,
       "brcdTMUcastQStatsQSize": brcdTMUcastQStatsQSize,
       "brcdTMUcastQStatsCreditCount": brcdTMUcastQStatsCreditCount,
       "brcdTMMcastQStatsTable": brcdTMMcastQStatsTable,
       "brcdTMMcastQStatsEntry": brcdTMMcastQStatsEntry,
       "brcdTMMcastQStatsSlotId": brcdTMMcastQStatsSlotId,
       "brcdTMMcastQStatsTMDeviceId": brcdTMMcastQStatsTMDeviceId,
       "brcdTMMcastQStatsPriority": brcdTMMcastQStatsPriority,
       "brcdTMMcastQStatsDescription": brcdTMMcastQStatsDescription,
       "brcdTMMcastQStatsEnquePkts": brcdTMMcastQStatsEnquePkts,
       "brcdTMMcastQStatsEnqueBytes": brcdTMMcastQStatsEnqueBytes,
       "brcdTMMcastQStatsDequePkts": brcdTMMcastQStatsDequePkts,
       "brcdTMMcastQStatsDequeBytes": brcdTMMcastQStatsDequeBytes,
       "brcdTMMcastQStatsTotalQDiscardPkts": brcdTMMcastQStatsTotalQDiscardPkts,
       "brcdTMMcastQStatsTotalQDiscardBytes": brcdTMMcastQStatsTotalQDiscardBytes,
       "brcdTMMcastQStatsOldestDiscardPkts": brcdTMMcastQStatsOldestDiscardPkts,
       "brcdTMMcastQStatsOldestDiscardBytes": brcdTMMcastQStatsOldestDiscardBytes,
       "brcdTMMcastQStatsWREDDroppedPkts": brcdTMMcastQStatsWREDDroppedPkts,
       "brcdTMMcastQStatsWREDDroppedBytes": brcdTMMcastQStatsWREDDroppedBytes,
       "brcdTMMcastQStatsMaxQDepthSinceLastRead": brcdTMMcastQStatsMaxQDepthSinceLastRead,
       "brcdTMMcastQStatsQSize": brcdTMMcastQStatsQSize,
       "brcdTMMcastQStatsCreditCount": brcdTMMcastQStatsCreditCount,
       "brcdTMCpuQStatsTable": brcdTMCpuQStatsTable,
       "brcdTMCpuQStatsEntry": brcdTMCpuQStatsEntry,
       "brcdTMCpuQStatsSlotId": brcdTMCpuQStatsSlotId,
       "brcdTMCpuQStatsTMDeviceId": brcdTMCpuQStatsTMDeviceId,
       "brcdTMCpuQStatsType": brcdTMCpuQStatsType,
       "brcdTMCpuQStatsPriority": brcdTMCpuQStatsPriority,
       "brcdTMCpuQStatsDescription": brcdTMCpuQStatsDescription,
       "brcdTMCpuQStatsEnquePkts": brcdTMCpuQStatsEnquePkts,
       "brcdTMCpuQStatsEnqueBytes": brcdTMCpuQStatsEnqueBytes,
       "brcdTMCpuQStatsDequePkts": brcdTMCpuQStatsDequePkts,
       "brcdTMCpuQStatsDequeBytes": brcdTMCpuQStatsDequeBytes,
       "brcdTMCpuQStatsTotalQDiscardPkts": brcdTMCpuQStatsTotalQDiscardPkts,
       "brcdTMCpuQStatsTotalQDiscardBytes": brcdTMCpuQStatsTotalQDiscardBytes,
       "brcdTMCpuQStatsOldestDiscardPkts": brcdTMCpuQStatsOldestDiscardPkts,
       "brcdTMCpuQStatsOldestDiscardBytes": brcdTMCpuQStatsOldestDiscardBytes,
       "brcdTMCpuQStatsWREDDroppedPkts": brcdTMCpuQStatsWREDDroppedPkts,
       "brcdTMCpuQStatsWREDDroppedBytes": brcdTMCpuQStatsWREDDroppedBytes,
       "brcdTMCpuQStatsMaxQDepthSinceLastRead": brcdTMCpuQStatsMaxQDepthSinceLastRead,
       "brcdTMCpuQStatsQSize": brcdTMCpuQStatsQSize,
       "brcdTMCpuQStatsCreditCount": brcdTMCpuQStatsCreditCount,
       "brcdTMMcastStreamQStatsTable": brcdTMMcastStreamQStatsTable,
       "brcdTMMcastStreamQStatsEntry": brcdTMMcastStreamQStatsEntry,
       "brcdTMMcastStreamQStatsAddressType": brcdTMMcastStreamQStatsAddressType,
       "brcdTMMcastStreamQStatsSource": brcdTMMcastStreamQStatsSource,
       "brcdTMMcastStreamQStatsGroup": brcdTMMcastStreamQStatsGroup,
       "brcdTMMcastStreamQStatsGroupPrefixLength": brcdTMMcastStreamQStatsGroupPrefixLength,
       "brcdTMMcastStreamQStatsPriority": brcdTMMcastStreamQStatsPriority,
       "brcdTMMcastStreamQStatsEnquePkts": brcdTMMcastStreamQStatsEnquePkts,
       "brcdTMMcastStreamQStatsEnqueBytes": brcdTMMcastStreamQStatsEnqueBytes,
       "brcdTMMcastStreamQStatsDequePkts": brcdTMMcastStreamQStatsDequePkts,
       "brcdTMMcastStreamQStatsDequeBytes": brcdTMMcastStreamQStatsDequeBytes,
       "brcdTMMcastStreamQStatsTotalQDiscardPkts": brcdTMMcastStreamQStatsTotalQDiscardPkts,
       "brcdTMMcastStreamQStatsTotalQDiscardBytes": brcdTMMcastStreamQStatsTotalQDiscardBytes,
       "brcdTMMcastStreamQStatsOldestDiscardPkts": brcdTMMcastStreamQStatsOldestDiscardPkts,
       "brcdTMMcastStreamQStatsOldestDiscardBytes": brcdTMMcastStreamQStatsOldestDiscardBytes,
       "brcdTMMcastStreamQStatsWREDDroppedPkts": brcdTMMcastStreamQStatsWREDDroppedPkts,
       "brcdTMMcastStreamQStatsWREDDroppedBytes": brcdTMMcastStreamQStatsWREDDroppedBytes,
       "brcdTMMcastStreamQStatsMaxQDepthSinceLastRead": brcdTMMcastStreamQStatsMaxQDepthSinceLastRead,
       "brcdTMMcastStreamQStatsQSize": brcdTMMcastStreamQStatsQSize,
       "brcdTMMcastStreamQStatsCreditCount": brcdTMMcastStreamQStatsCreditCount,
       "brcdTMCpuQInfoTable": brcdTMCpuQInfoTable,
       "brcdTMCpuQInfoEntry": brcdTMCpuQInfoEntry,
       "brcdTMCpuQInfoSlotId": brcdTMCpuQInfoSlotId,
       "brcdTMCpuQInfoTMDeviceId": brcdTMCpuQInfoTMDeviceId,
       "brcdTMCpuQInfoPriority0QSize": brcdTMCpuQInfoPriority0QSize,
       "brcdTMCpuQInfoPriority0CreditCount": brcdTMCpuQInfoPriority0CreditCount,
       "brcdTMCpuQInfoPriority1QSize": brcdTMCpuQInfoPriority1QSize,
       "brcdTMCpuQInfoPriority1CreditCount": brcdTMCpuQInfoPriority1CreditCount,
       "brcdTMCpuQInfoPriority2QSize": brcdTMCpuQInfoPriority2QSize,
       "brcdTMCpuQInfoPriority2CreditCount": brcdTMCpuQInfoPriority2CreditCount,
       "brcdTMCpuQInfoPriority3QSize": brcdTMCpuQInfoPriority3QSize,
       "brcdTMCpuQInfoPriority3CreditCount": brcdTMCpuQInfoPriority3CreditCount,
       "brcdTMCpuQInfoPriority4QSize": brcdTMCpuQInfoPriority4QSize,
       "brcdTMCpuQInfoPriority4CreditCount": brcdTMCpuQInfoPriority4CreditCount,
       "brcdTMCpuQInfoPriority5QSize": brcdTMCpuQInfoPriority5QSize,
       "brcdTMCpuQInfoPriority5CreditCount": brcdTMCpuQInfoPriority5CreditCount,
       "brcdTMCpuQInfoPriority6QSize": brcdTMCpuQInfoPriority6QSize,
       "brcdTMCpuQInfoPriority6CreditCount": brcdTMCpuQInfoPriority6CreditCount,
       "brcdTMCpuQInfoPriority7QSize": brcdTMCpuQInfoPriority7QSize,
       "brcdTMCpuQInfoPriority7CreditCount": brcdTMCpuQInfoPriority7CreditCount,
       "brcdTMDestUcastQStatTable": brcdTMDestUcastQStatTable,
       "brcdTMDestUcastQStatEntry": brcdTMDestUcastQStatEntry,
       "brcdTMDestUcastQStatDestIfIndex": brcdTMDestUcastQStatDestIfIndex,
       "brcdTMDestUcastQStatPriority": brcdTMDestUcastQStatPriority,
       "brcdTMDestUcastQStatEnquePkts": brcdTMDestUcastQStatEnquePkts,
       "brcdTMDestUcastQStatEnqueBytes": brcdTMDestUcastQStatEnqueBytes,
       "brcdTMDestUcastQStatDequePkts": brcdTMDestUcastQStatDequePkts,
       "brcdTMDestUcastQStatDequeBytes": brcdTMDestUcastQStatDequeBytes,
       "brcdTMDestUcastQStatTotalQDiscardPkts": brcdTMDestUcastQStatTotalQDiscardPkts,
       "brcdTMDestUcastQStatTotalQDiscardBytes": brcdTMDestUcastQStatTotalQDiscardBytes}
)
