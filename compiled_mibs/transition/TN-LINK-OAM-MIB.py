# SNMP MIB module (TN-LINK-OAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TN-LINK-OAM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:31:45 2025
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

(dot3OamEntry,
 dot3OamEventConfigEntry,
 dot3OamPeerEntry,
 dot3OamStatsEntry) = mibBuilder.importSymbols(
    "DOT3-OAM-MIB",
    "dot3OamEntry",
    "dot3OamEventConfigEntry",
    "dot3OamPeerEntry",
    "dot3OamStatsEntry")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(tnProducts,) = mibBuilder.importSymbols(
    "TRANSITION-SMI",
    "tnProducts")


# MODULE-IDENTITY

tnLinkOamMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 140)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnLinkOamNotifications_ObjectIdentity = ObjectIdentity
tnLinkOamNotifications = _TnLinkOamNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 140, 0)
)
_TnLinkOamObjects_ObjectIdentity = ObjectIdentity
tnLinkOamObjects = _TnLinkOamObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 140, 1)
)
_TnLinkOamPortConfigTable_Object = MibTable
tnLinkOamPortConfigTable = _TnLinkOamPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 140, 1, 1)
)
if mibBuilder.loadTexts:
    tnLinkOamPortConfigTable.setStatus("current")
_TnLinkOamPortConfigEntry_Object = MibTableRow
tnLinkOamPortConfigEntry = _TnLinkOamPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 140, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tnLinkOamPortConfigEntry.setStatus("current")


class _TnLinkOamLoopbackSupport_Type(Integer32):
    """Custom type tnLinkOamLoopbackSupport based on Integer32"""
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


_TnLinkOamLoopbackSupport_Type.__name__ = "Integer32"
_TnLinkOamLoopbackSupport_Object = MibTableColumn
tnLinkOamLoopbackSupport = _TnLinkOamLoopbackSupport_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 140, 1, 1, 1, 1),
    _TnLinkOamLoopbackSupport_Type()
)
tnLinkOamLoopbackSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLinkOamLoopbackSupport.setStatus("current")


class _TnLinkOamLinkMonitorSupport_Type(Integer32):
    """Custom type tnLinkOamLinkMonitorSupport based on Integer32"""
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


_TnLinkOamLinkMonitorSupport_Type.__name__ = "Integer32"
_TnLinkOamLinkMonitorSupport_Object = MibTableColumn
tnLinkOamLinkMonitorSupport = _TnLinkOamLinkMonitorSupport_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 140, 1, 1, 1, 2),
    _TnLinkOamLinkMonitorSupport_Type()
)
tnLinkOamLinkMonitorSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLinkOamLinkMonitorSupport.setStatus("current")


class _TnLinkMIBRetrievalSupport_Type(Integer32):
    """Custom type tnLinkMIBRetrievalSupport based on Integer32"""
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


_TnLinkMIBRetrievalSupport_Type.__name__ = "Integer32"
_TnLinkMIBRetrievalSupport_Object = MibTableColumn
tnLinkMIBRetrievalSupport = _TnLinkMIBRetrievalSupport_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 140, 1, 1, 1, 3),
    _TnLinkMIBRetrievalSupport_Type()
)
tnLinkMIBRetrievalSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLinkMIBRetrievalSupport.setStatus("current")


class _TnLinkOamLoopbackOperation_Type(Integer32):
    """Custom type tnLinkOamLoopbackOperation based on Integer32"""
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


_TnLinkOamLoopbackOperation_Type.__name__ = "Integer32"
_TnLinkOamLoopbackOperation_Object = MibTableColumn
tnLinkOamLoopbackOperation = _TnLinkOamLoopbackOperation_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 140, 1, 1, 1, 4),
    _TnLinkOamLoopbackOperation_Type()
)
tnLinkOamLoopbackOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLinkOamLoopbackOperation.setStatus("current")
_TnLinkOamStatisticsTable_Object = MibTable
tnLinkOamStatisticsTable = _TnLinkOamStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 140, 1, 2)
)
if mibBuilder.loadTexts:
    tnLinkOamStatisticsTable.setStatus("current")
_TnLinkOamStatisticsEntry_Object = MibTableRow
tnLinkOamStatisticsEntry = _TnLinkOamStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 140, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tnLinkOamStatisticsEntry.setStatus("current")
_TnLinkOamLinkfaultPDUsRx_Type = Counter32
_TnLinkOamLinkfaultPDUsRx_Object = MibTableColumn
tnLinkOamLinkfaultPDUsRx = _TnLinkOamLinkfaultPDUsRx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 140, 1, 2, 1, 1),
    _TnLinkOamLinkfaultPDUsRx_Type()
)
tnLinkOamLinkfaultPDUsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLinkOamLinkfaultPDUsRx.setStatus("current")
if mibBuilder.loadTexts:
    tnLinkOamLinkfaultPDUsRx.setUnits("frames")
_TnLinkOamLinkfaultPDUsTx_Type = Counter32
_TnLinkOamLinkfaultPDUsTx_Object = MibTableColumn
tnLinkOamLinkfaultPDUsTx = _TnLinkOamLinkfaultPDUsTx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 140, 1, 2, 1, 2),
    _TnLinkOamLinkfaultPDUsTx_Type()
)
tnLinkOamLinkfaultPDUsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLinkOamLinkfaultPDUsTx.setStatus("current")
if mibBuilder.loadTexts:
    tnLinkOamLinkfaultPDUsTx.setUnits("frames")
_TnLinkOamDyingGaspRx_Type = Counter32
_TnLinkOamDyingGaspRx_Object = MibTableColumn
tnLinkOamDyingGaspRx = _TnLinkOamDyingGaspRx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 140, 1, 2, 1, 3),
    _TnLinkOamDyingGaspRx_Type()
)
tnLinkOamDyingGaspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLinkOamDyingGaspRx.setStatus("current")
if mibBuilder.loadTexts:
    tnLinkOamDyingGaspRx.setUnits("frames")
_TnLinkOamDyingGaspTx_Type = Counter32
_TnLinkOamDyingGaspTx_Object = MibTableColumn
tnLinkOamDyingGaspTx = _TnLinkOamDyingGaspTx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 140, 1, 2, 1, 4),
    _TnLinkOamDyingGaspTx_Type()
)
tnLinkOamDyingGaspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLinkOamDyingGaspTx.setStatus("current")
if mibBuilder.loadTexts:
    tnLinkOamDyingGaspTx.setUnits("frames")
_TnLinkOamCriticalEventPDUsRx_Type = Counter32
_TnLinkOamCriticalEventPDUsRx_Object = MibTableColumn
tnLinkOamCriticalEventPDUsRx = _TnLinkOamCriticalEventPDUsRx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 140, 1, 2, 1, 5),
    _TnLinkOamCriticalEventPDUsRx_Type()
)
tnLinkOamCriticalEventPDUsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLinkOamCriticalEventPDUsRx.setStatus("current")
if mibBuilder.loadTexts:
    tnLinkOamCriticalEventPDUsRx.setUnits("frames")
_TnLinkOamCriticalEventPDUsTx_Type = Counter32
_TnLinkOamCriticalEventPDUsTx_Object = MibTableColumn
tnLinkOamCriticalEventPDUsTx = _TnLinkOamCriticalEventPDUsTx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 140, 1, 2, 1, 6),
    _TnLinkOamCriticalEventPDUsTx_Type()
)
tnLinkOamCriticalEventPDUsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLinkOamCriticalEventPDUsTx.setStatus("current")
if mibBuilder.loadTexts:
    tnLinkOamCriticalEventPDUsTx.setUnits("frames")
_TnLinkOamLocalPortConfigStatusTable_Object = MibTable
tnLinkOamLocalPortConfigStatusTable = _TnLinkOamLocalPortConfigStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 140, 1, 3)
)
if mibBuilder.loadTexts:
    tnLinkOamLocalPortConfigStatusTable.setStatus("current")
_TnLinkOamLocalPortConfigStatusEntry_Object = MibTableRow
tnLinkOamLocalPortConfigStatusEntry = _TnLinkOamLocalPortConfigStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 140, 1, 3, 1)
)
if mibBuilder.loadTexts:
    tnLinkOamLocalPortConfigStatusEntry.setStatus("current")


class _TnLinkOamPDUPermission_Type(Integer32):
    """Custom type tnLinkOamPDUPermission based on Integer32"""
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
        *(("linkfault", 1),
          ("receiveonly", 2),
          ("informationexchangeonly", 3),
          ("any", 4))
    )


_TnLinkOamPDUPermission_Type.__name__ = "Integer32"
_TnLinkOamPDUPermission_Object = MibTableColumn
tnLinkOamPDUPermission = _TnLinkOamPDUPermission_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 140, 1, 3, 1, 1),
    _TnLinkOamPDUPermission_Type()
)
tnLinkOamPDUPermission.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLinkOamPDUPermission.setStatus("current")


class _TnLinkOamLocalMultiplexerState_Type(Integer32):
    """Custom type tnLinkOamLocalMultiplexerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forwarding", 1),
          ("discarding", 2))
    )


_TnLinkOamLocalMultiplexerState_Type.__name__ = "Integer32"
_TnLinkOamLocalMultiplexerState_Object = MibTableColumn
tnLinkOamLocalMultiplexerState = _TnLinkOamLocalMultiplexerState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 140, 1, 3, 1, 2),
    _TnLinkOamLocalMultiplexerState_Type()
)
tnLinkOamLocalMultiplexerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLinkOamLocalMultiplexerState.setStatus("current")


class _TnLinkOamLocalParserState_Type(Integer32):
    """Custom type tnLinkOamLocalParserState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forwarding", 1),
          ("loopback", 2),
          ("discarding", 3))
    )


_TnLinkOamLocalParserState_Type.__name__ = "Integer32"
_TnLinkOamLocalParserState_Object = MibTableColumn
tnLinkOamLocalParserState = _TnLinkOamLocalParserState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 140, 1, 3, 1, 3),
    _TnLinkOamLocalParserState_Type()
)
tnLinkOamLocalParserState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLinkOamLocalParserState.setStatus("current")
_TnLinkOamLocalOrganizationalUniqueIdentifi_Type = DisplayString
_TnLinkOamLocalOrganizationalUniqueIdentifi_Object = MibTableColumn
tnLinkOamLocalOrganizationalUniqueIdentifi = _TnLinkOamLocalOrganizationalUniqueIdentifi_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 140, 1, 3, 1, 4),
    _TnLinkOamLocalOrganizationalUniqueIdentifi_Type()
)
tnLinkOamLocalOrganizationalUniqueIdentifi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLinkOamLocalOrganizationalUniqueIdentifi.setStatus("current")
_TnLinkOamPeerPortConfigStatusTable_Object = MibTable
tnLinkOamPeerPortConfigStatusTable = _TnLinkOamPeerPortConfigStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 140, 1, 4)
)
if mibBuilder.loadTexts:
    tnLinkOamPeerPortConfigStatusTable.setStatus("current")
_TnLinkOamPeerPortConfigStatusEntry_Object = MibTableRow
tnLinkOamPeerPortConfigStatusEntry = _TnLinkOamPeerPortConfigStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 140, 1, 4, 1)
)
if mibBuilder.loadTexts:
    tnLinkOamPeerPortConfigStatusEntry.setStatus("current")


class _TnLinkOamPeerMultiplexerState_Type(Integer32):
    """Custom type tnLinkOamPeerMultiplexerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forwarding", 1),
          ("discarding", 2))
    )


_TnLinkOamPeerMultiplexerState_Type.__name__ = "Integer32"
_TnLinkOamPeerMultiplexerState_Object = MibTableColumn
tnLinkOamPeerMultiplexerState = _TnLinkOamPeerMultiplexerState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 140, 1, 4, 1, 1),
    _TnLinkOamPeerMultiplexerState_Type()
)
tnLinkOamPeerMultiplexerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLinkOamPeerMultiplexerState.setStatus("current")


class _TnLinkOamPeerParserState_Type(Integer32):
    """Custom type tnLinkOamPeerParserState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forwarding", 1),
          ("loopback", 2),
          ("discarding", 3))
    )


_TnLinkOamPeerParserState_Type.__name__ = "Integer32"
_TnLinkOamPeerParserState_Object = MibTableColumn
tnLinkOamPeerParserState = _TnLinkOamPeerParserState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 140, 1, 4, 1, 2),
    _TnLinkOamPeerParserState_Type()
)
tnLinkOamPeerParserState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLinkOamPeerParserState.setStatus("current")
_TnLinkOamPeerOrganizationalUniqueIdentifi_Type = DisplayString
_TnLinkOamPeerOrganizationalUniqueIdentifi_Object = MibTableColumn
tnLinkOamPeerOrganizationalUniqueIdentifi = _TnLinkOamPeerOrganizationalUniqueIdentifi_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 140, 1, 4, 1, 3),
    _TnLinkOamPeerOrganizationalUniqueIdentifi_Type()
)
tnLinkOamPeerOrganizationalUniqueIdentifi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLinkOamPeerOrganizationalUniqueIdentifi.setStatus("current")
_TnLinkOamLinkEventStatusTable_Object = MibTable
tnLinkOamLinkEventStatusTable = _TnLinkOamLinkEventStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 140, 1, 5)
)
if mibBuilder.loadTexts:
    tnLinkOamLinkEventStatusTable.setStatus("current")
_TnLinkOamLinkEventStatusEntry_Object = MibTableRow
tnLinkOamLinkEventStatusEntry = _TnLinkOamLinkEventStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 140, 1, 5, 1)
)
tnLinkOamLinkEventStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TN-LINK-OAM-MIB", "tnLinkOamLocationIndex"),
)
if mibBuilder.loadTexts:
    tnLinkOamLinkEventStatusEntry.setStatus("current")
_TnLinkOamLocationIndex_Type = Unsigned32
_TnLinkOamLocationIndex_Object = MibTableColumn
tnLinkOamLocationIndex = _TnLinkOamLocationIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 140, 1, 5, 1, 1),
    _TnLinkOamLocationIndex_Type()
)
tnLinkOamLocationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnLinkOamLocationIndex.setStatus("current")
_TnLinkOamSequenceNumber_Type = Counter32
_TnLinkOamSequenceNumber_Object = MibTableColumn
tnLinkOamSequenceNumber = _TnLinkOamSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 140, 1, 5, 1, 2),
    _TnLinkOamSequenceNumber_Type()
)
tnLinkOamSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLinkOamSequenceNumber.setStatus("current")
_TnLinkOamFrameErrorEventTimestamp_Type = TimeStamp
_TnLinkOamFrameErrorEventTimestamp_Object = MibTableColumn
tnLinkOamFrameErrorEventTimestamp = _TnLinkOamFrameErrorEventTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 140, 1, 5, 1, 3),
    _TnLinkOamFrameErrorEventTimestamp_Type()
)
tnLinkOamFrameErrorEventTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLinkOamFrameErrorEventTimestamp.setStatus("current")
_TnLinkOamFrameErrorEventWindow_Type = Counter32
_TnLinkOamFrameErrorEventWindow_Object = MibTableColumn
tnLinkOamFrameErrorEventWindow = _TnLinkOamFrameErrorEventWindow_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 140, 1, 5, 1, 4),
    _TnLinkOamFrameErrorEventWindow_Type()
)
tnLinkOamFrameErrorEventWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLinkOamFrameErrorEventWindow.setStatus("current")
_TnLinkOamFrameErrorEventThreshold_Type = Counter32
_TnLinkOamFrameErrorEventThreshold_Object = MibTableColumn
tnLinkOamFrameErrorEventThreshold = _TnLinkOamFrameErrorEventThreshold_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 140, 1, 5, 1, 5),
    _TnLinkOamFrameErrorEventThreshold_Type()
)
tnLinkOamFrameErrorEventThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLinkOamFrameErrorEventThreshold.setStatus("current")
_TnLinkOamFrameErrors_Type = Counter32
_TnLinkOamFrameErrors_Object = MibTableColumn
tnLinkOamFrameErrors = _TnLinkOamFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 140, 1, 5, 1, 6),
    _TnLinkOamFrameErrors_Type()
)
tnLinkOamFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLinkOamFrameErrors.setStatus("current")
_TnLinkOamTotalFrameErrors_Type = Counter64
_TnLinkOamTotalFrameErrors_Object = MibTableColumn
tnLinkOamTotalFrameErrors = _TnLinkOamTotalFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 140, 1, 5, 1, 7),
    _TnLinkOamTotalFrameErrors_Type()
)
tnLinkOamTotalFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLinkOamTotalFrameErrors.setStatus("current")
_TnLinkOamTotalFrameErrorEvents_Type = Counter32
_TnLinkOamTotalFrameErrorEvents_Object = MibTableColumn
tnLinkOamTotalFrameErrorEvents = _TnLinkOamTotalFrameErrorEvents_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 140, 1, 5, 1, 8),
    _TnLinkOamTotalFrameErrorEvents_Type()
)
tnLinkOamTotalFrameErrorEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLinkOamTotalFrameErrorEvents.setStatus("current")
_TnLinkOamFramePeriodErrorEventTimestamp_Type = TimeStamp
_TnLinkOamFramePeriodErrorEventTimestamp_Object = MibTableColumn
tnLinkOamFramePeriodErrorEventTimestamp = _TnLinkOamFramePeriodErrorEventTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 140, 1, 5, 1, 9),
    _TnLinkOamFramePeriodErrorEventTimestamp_Type()
)
tnLinkOamFramePeriodErrorEventTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLinkOamFramePeriodErrorEventTimestamp.setStatus("current")
_TnLinkOamFramePeriodErrorEventWindow_Type = Counter32
_TnLinkOamFramePeriodErrorEventWindow_Object = MibTableColumn
tnLinkOamFramePeriodErrorEventWindow = _TnLinkOamFramePeriodErrorEventWindow_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 140, 1, 5, 1, 10),
    _TnLinkOamFramePeriodErrorEventWindow_Type()
)
tnLinkOamFramePeriodErrorEventWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLinkOamFramePeriodErrorEventWindow.setStatus("current")
_TnLinkOamFramePeriodErrorEventThreshold_Type = Counter32
_TnLinkOamFramePeriodErrorEventThreshold_Object = MibTableColumn
tnLinkOamFramePeriodErrorEventThreshold = _TnLinkOamFramePeriodErrorEventThreshold_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 140, 1, 5, 1, 11),
    _TnLinkOamFramePeriodErrorEventThreshold_Type()
)
tnLinkOamFramePeriodErrorEventThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLinkOamFramePeriodErrorEventThreshold.setStatus("current")
_TnLinkOamFramePeriodsErrors_Type = Counter32
_TnLinkOamFramePeriodsErrors_Object = MibTableColumn
tnLinkOamFramePeriodsErrors = _TnLinkOamFramePeriodsErrors_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 140, 1, 5, 1, 12),
    _TnLinkOamFramePeriodsErrors_Type()
)
tnLinkOamFramePeriodsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLinkOamFramePeriodsErrors.setStatus("current")
_TnLinkOamTotalFramePeriodsErrors_Type = Counter64
_TnLinkOamTotalFramePeriodsErrors_Object = MibTableColumn
tnLinkOamTotalFramePeriodsErrors = _TnLinkOamTotalFramePeriodsErrors_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 140, 1, 5, 1, 13),
    _TnLinkOamTotalFramePeriodsErrors_Type()
)
tnLinkOamTotalFramePeriodsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLinkOamTotalFramePeriodsErrors.setStatus("current")
_TnLinkOamTotalFramePerioderrorEvents_Type = Counter32
_TnLinkOamTotalFramePerioderrorEvents_Object = MibTableColumn
tnLinkOamTotalFramePerioderrorEvents = _TnLinkOamTotalFramePerioderrorEvents_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 140, 1, 5, 1, 14),
    _TnLinkOamTotalFramePerioderrorEvents_Type()
)
tnLinkOamTotalFramePerioderrorEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLinkOamTotalFramePerioderrorEvents.setStatus("current")
_TnLinkOamSymbolPeriodErrorEventTimestamp_Type = TimeStamp
_TnLinkOamSymbolPeriodErrorEventTimestamp_Object = MibTableColumn
tnLinkOamSymbolPeriodErrorEventTimestamp = _TnLinkOamSymbolPeriodErrorEventTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 140, 1, 5, 1, 15),
    _TnLinkOamSymbolPeriodErrorEventTimestamp_Type()
)
tnLinkOamSymbolPeriodErrorEventTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLinkOamSymbolPeriodErrorEventTimestamp.setStatus("current")
_TnLinkOamSymbolPeriodErrorEventWindow_Type = Counter64
_TnLinkOamSymbolPeriodErrorEventWindow_Object = MibTableColumn
tnLinkOamSymbolPeriodErrorEventWindow = _TnLinkOamSymbolPeriodErrorEventWindow_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 140, 1, 5, 1, 16),
    _TnLinkOamSymbolPeriodErrorEventWindow_Type()
)
tnLinkOamSymbolPeriodErrorEventWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLinkOamSymbolPeriodErrorEventWindow.setStatus("current")
_TnLinkOamSymbolPeriodErrorEventThreshold_Type = Counter64
_TnLinkOamSymbolPeriodErrorEventThreshold_Object = MibTableColumn
tnLinkOamSymbolPeriodErrorEventThreshold = _TnLinkOamSymbolPeriodErrorEventThreshold_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 140, 1, 5, 1, 17),
    _TnLinkOamSymbolPeriodErrorEventThreshold_Type()
)
tnLinkOamSymbolPeriodErrorEventThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLinkOamSymbolPeriodErrorEventThreshold.setStatus("current")
_TnLinkOamSymbolPeriodsErrors_Type = Counter64
_TnLinkOamSymbolPeriodsErrors_Object = MibTableColumn
tnLinkOamSymbolPeriodsErrors = _TnLinkOamSymbolPeriodsErrors_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 140, 1, 5, 1, 18),
    _TnLinkOamSymbolPeriodsErrors_Type()
)
tnLinkOamSymbolPeriodsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLinkOamSymbolPeriodsErrors.setStatus("current")
_TnLinkOamSymbolFramePeriodErrors_Type = Counter64
_TnLinkOamSymbolFramePeriodErrors_Object = MibTableColumn
tnLinkOamSymbolFramePeriodErrors = _TnLinkOamSymbolFramePeriodErrors_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 140, 1, 5, 1, 19),
    _TnLinkOamSymbolFramePeriodErrors_Type()
)
tnLinkOamSymbolFramePeriodErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLinkOamSymbolFramePeriodErrors.setStatus("current")
_TnLinkOamTotalSymbolFramePerioderrorEvents_Type = Counter32
_TnLinkOamTotalSymbolFramePerioderrorEvents_Object = MibTableColumn
tnLinkOamTotalSymbolFramePerioderrorEvents = _TnLinkOamTotalSymbolFramePerioderrorEvents_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 140, 1, 5, 1, 20),
    _TnLinkOamTotalSymbolFramePerioderrorEvents_Type()
)
tnLinkOamTotalSymbolFramePerioderrorEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLinkOamTotalSymbolFramePerioderrorEvents.setStatus("current")
_TnLinkOamEventSecondsSummaryTimestamp_Type = TimeStamp
_TnLinkOamEventSecondsSummaryTimestamp_Object = MibTableColumn
tnLinkOamEventSecondsSummaryTimestamp = _TnLinkOamEventSecondsSummaryTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 140, 1, 5, 1, 21),
    _TnLinkOamEventSecondsSummaryTimestamp_Type()
)
tnLinkOamEventSecondsSummaryTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLinkOamEventSecondsSummaryTimestamp.setStatus("current")
_TnLinkOamEventSecondsSummaryWindow_Type = Counter32
_TnLinkOamEventSecondsSummaryWindow_Object = MibTableColumn
tnLinkOamEventSecondsSummaryWindow = _TnLinkOamEventSecondsSummaryWindow_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 140, 1, 5, 1, 22),
    _TnLinkOamEventSecondsSummaryWindow_Type()
)
tnLinkOamEventSecondsSummaryWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLinkOamEventSecondsSummaryWindow.setStatus("current")
_TnLinkOamEventSecondsSummaryThreshold_Type = Counter32
_TnLinkOamEventSecondsSummaryThreshold_Object = MibTableColumn
tnLinkOamEventSecondsSummaryThreshold = _TnLinkOamEventSecondsSummaryThreshold_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 140, 1, 5, 1, 23),
    _TnLinkOamEventSecondsSummaryThreshold_Type()
)
tnLinkOamEventSecondsSummaryThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLinkOamEventSecondsSummaryThreshold.setStatus("current")
_TnLinkOamEventSecondsSummarysEvents_Type = Counter32
_TnLinkOamEventSecondsSummarysEvents_Object = MibTableColumn
tnLinkOamEventSecondsSummarysEvents = _TnLinkOamEventSecondsSummarysEvents_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 140, 1, 5, 1, 24),
    _TnLinkOamEventSecondsSummarysEvents_Type()
)
tnLinkOamEventSecondsSummarysEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLinkOamEventSecondsSummarysEvents.setStatus("current")
_TnLinkOamEventSecondsSummaryErrorTotal_Type = Counter32
_TnLinkOamEventSecondsSummaryErrorTotal_Object = MibTableColumn
tnLinkOamEventSecondsSummaryErrorTotal = _TnLinkOamEventSecondsSummaryErrorTotal_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 140, 1, 5, 1, 25),
    _TnLinkOamEventSecondsSummaryErrorTotal_Type()
)
tnLinkOamEventSecondsSummaryErrorTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLinkOamEventSecondsSummaryErrorTotal.setStatus("current")
_TnLinkOamTotalEventSecondsSummaryEventTotal_Type = Counter32
_TnLinkOamTotalEventSecondsSummaryEventTotal_Object = MibTableColumn
tnLinkOamTotalEventSecondsSummaryEventTotal = _TnLinkOamTotalEventSecondsSummaryEventTotal_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 140, 1, 5, 1, 26),
    _TnLinkOamTotalEventSecondsSummaryEventTotal_Type()
)
tnLinkOamTotalEventSecondsSummaryEventTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLinkOamTotalEventSecondsSummaryEventTotal.setStatus("current")
_TnLinkOamConformance_ObjectIdentity = ObjectIdentity
tnLinkOamConformance = _TnLinkOamConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 140, 2)
)
dot3OamEntry.registerAugmentions(
    ("TN-LINK-OAM-MIB",
     "tnLinkOamPortConfigEntry")
)
tnLinkOamPortConfigEntry.setIndexNames(*dot3OamEntry.getIndexNames())
dot3OamStatsEntry.registerAugmentions(
    ("TN-LINK-OAM-MIB",
     "tnLinkOamStatisticsEntry")
)
tnLinkOamStatisticsEntry.setIndexNames(*dot3OamStatsEntry.getIndexNames())
dot3OamEntry.registerAugmentions(
    ("TN-LINK-OAM-MIB",
     "tnLinkOamLocalPortConfigStatusEntry")
)
tnLinkOamLocalPortConfigStatusEntry.setIndexNames(*dot3OamEntry.getIndexNames())
dot3OamPeerEntry.registerAugmentions(
    ("TN-LINK-OAM-MIB",
     "tnLinkOamPeerPortConfigStatusEntry")
)
tnLinkOamPeerPortConfigStatusEntry.setIndexNames(*dot3OamPeerEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-LINK-OAM-MIB",
    **{"tnLinkOamMIB": tnLinkOamMIB,
       "tnLinkOamNotifications": tnLinkOamNotifications,
       "tnLinkOamObjects": tnLinkOamObjects,
       "tnLinkOamPortConfigTable": tnLinkOamPortConfigTable,
       "tnLinkOamPortConfigEntry": tnLinkOamPortConfigEntry,
       "tnLinkOamLoopbackSupport": tnLinkOamLoopbackSupport,
       "tnLinkOamLinkMonitorSupport": tnLinkOamLinkMonitorSupport,
       "tnLinkMIBRetrievalSupport": tnLinkMIBRetrievalSupport,
       "tnLinkOamLoopbackOperation": tnLinkOamLoopbackOperation,
       "tnLinkOamStatisticsTable": tnLinkOamStatisticsTable,
       "tnLinkOamStatisticsEntry": tnLinkOamStatisticsEntry,
       "tnLinkOamLinkfaultPDUsRx": tnLinkOamLinkfaultPDUsRx,
       "tnLinkOamLinkfaultPDUsTx": tnLinkOamLinkfaultPDUsTx,
       "tnLinkOamDyingGaspRx": tnLinkOamDyingGaspRx,
       "tnLinkOamDyingGaspTx": tnLinkOamDyingGaspTx,
       "tnLinkOamCriticalEventPDUsRx": tnLinkOamCriticalEventPDUsRx,
       "tnLinkOamCriticalEventPDUsTx": tnLinkOamCriticalEventPDUsTx,
       "tnLinkOamLocalPortConfigStatusTable": tnLinkOamLocalPortConfigStatusTable,
       "tnLinkOamLocalPortConfigStatusEntry": tnLinkOamLocalPortConfigStatusEntry,
       "tnLinkOamPDUPermission": tnLinkOamPDUPermission,
       "tnLinkOamLocalMultiplexerState": tnLinkOamLocalMultiplexerState,
       "tnLinkOamLocalParserState": tnLinkOamLocalParserState,
       "tnLinkOamLocalOrganizationalUniqueIdentifi": tnLinkOamLocalOrganizationalUniqueIdentifi,
       "tnLinkOamPeerPortConfigStatusTable": tnLinkOamPeerPortConfigStatusTable,
       "tnLinkOamPeerPortConfigStatusEntry": tnLinkOamPeerPortConfigStatusEntry,
       "tnLinkOamPeerMultiplexerState": tnLinkOamPeerMultiplexerState,
       "tnLinkOamPeerParserState": tnLinkOamPeerParserState,
       "tnLinkOamPeerOrganizationalUniqueIdentifi": tnLinkOamPeerOrganizationalUniqueIdentifi,
       "tnLinkOamLinkEventStatusTable": tnLinkOamLinkEventStatusTable,
       "tnLinkOamLinkEventStatusEntry": tnLinkOamLinkEventStatusEntry,
       "tnLinkOamLocationIndex": tnLinkOamLocationIndex,
       "tnLinkOamSequenceNumber": tnLinkOamSequenceNumber,
       "tnLinkOamFrameErrorEventTimestamp": tnLinkOamFrameErrorEventTimestamp,
       "tnLinkOamFrameErrorEventWindow": tnLinkOamFrameErrorEventWindow,
       "tnLinkOamFrameErrorEventThreshold": tnLinkOamFrameErrorEventThreshold,
       "tnLinkOamFrameErrors": tnLinkOamFrameErrors,
       "tnLinkOamTotalFrameErrors": tnLinkOamTotalFrameErrors,
       "tnLinkOamTotalFrameErrorEvents": tnLinkOamTotalFrameErrorEvents,
       "tnLinkOamFramePeriodErrorEventTimestamp": tnLinkOamFramePeriodErrorEventTimestamp,
       "tnLinkOamFramePeriodErrorEventWindow": tnLinkOamFramePeriodErrorEventWindow,
       "tnLinkOamFramePeriodErrorEventThreshold": tnLinkOamFramePeriodErrorEventThreshold,
       "tnLinkOamFramePeriodsErrors": tnLinkOamFramePeriodsErrors,
       "tnLinkOamTotalFramePeriodsErrors": tnLinkOamTotalFramePeriodsErrors,
       "tnLinkOamTotalFramePerioderrorEvents": tnLinkOamTotalFramePerioderrorEvents,
       "tnLinkOamSymbolPeriodErrorEventTimestamp": tnLinkOamSymbolPeriodErrorEventTimestamp,
       "tnLinkOamSymbolPeriodErrorEventWindow": tnLinkOamSymbolPeriodErrorEventWindow,
       "tnLinkOamSymbolPeriodErrorEventThreshold": tnLinkOamSymbolPeriodErrorEventThreshold,
       "tnLinkOamSymbolPeriodsErrors": tnLinkOamSymbolPeriodsErrors,
       "tnLinkOamSymbolFramePeriodErrors": tnLinkOamSymbolFramePeriodErrors,
       "tnLinkOamTotalSymbolFramePerioderrorEvents": tnLinkOamTotalSymbolFramePerioderrorEvents,
       "tnLinkOamEventSecondsSummaryTimestamp": tnLinkOamEventSecondsSummaryTimestamp,
       "tnLinkOamEventSecondsSummaryWindow": tnLinkOamEventSecondsSummaryWindow,
       "tnLinkOamEventSecondsSummaryThreshold": tnLinkOamEventSecondsSummaryThreshold,
       "tnLinkOamEventSecondsSummarysEvents": tnLinkOamEventSecondsSummarysEvents,
       "tnLinkOamEventSecondsSummaryErrorTotal": tnLinkOamEventSecondsSummaryErrorTotal,
       "tnLinkOamTotalEventSecondsSummaryEventTotal": tnLinkOamTotalEventSecondsSummaryEventTotal,
       "tnLinkOamConformance": tnLinkOamConformance}
)
