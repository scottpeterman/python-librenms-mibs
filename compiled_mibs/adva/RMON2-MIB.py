# SNMP MIB module (RMON2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\RMON2-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:15:04 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(OwnerString,
 channelEntry,
 etherStatsEntry,
 filter,
 filterEntry,
 history,
 historyControlEntry,
 hostControlEntry,
 hosts,
 matrix,
 matrixControlEntry,
 statistics) = mibBuilder.importSymbols(
    "RMON-MIB",
    "OwnerString",
    "channelEntry",
    "etherStatsEntry",
    "filter",
    "filterEntry",
    "history",
    "historyControlEntry",
    "hostControlEntry",
    "hosts",
    "matrix",
    "matrixControlEntry",
    "statistics")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")

(ringStationControlEntry,
 sourceRoutingStatsEntry,
 tokenRing,
 tokenRingMLStatsEntry,
 tokenRingPStatsEntry) = mibBuilder.importSymbols(
    "TOKEN-RING-RMON-MIB",
    "ringStationControlEntry",
    "sourceRoutingStatsEntry",
    "tokenRing",
    "tokenRingMLStatsEntry",
    "tokenRingPStatsEntry")


# MODULE-IDENTITY

rmon = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 16)
)
if mibBuilder.loadTexts:
    rmon.setRevisions(
        ("2006-05-02 00:00",
         "2002-07-08 00:00",
         "1996-05-27 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ZeroBasedCounter32(TextualConvention, Gauge32):
    status = "current"


class LastCreateTime(TextualConvention, TimeTicks):
    status = "current"


class TimeFilter(TextualConvention, TimeTicks):
    status = "current"


class DataSource(TextualConvention, ObjectIdentifier):
    status = "current"


class ControlString(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_EtherStats2Table_Object = MibTable
etherStats2Table = _EtherStats2Table_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 4)
)
if mibBuilder.loadTexts:
    etherStats2Table.setStatus("current")
_EtherStats2Entry_Object = MibTableRow
etherStats2Entry = _EtherStats2Entry_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 4, 1)
)
if mibBuilder.loadTexts:
    etherStats2Entry.setStatus("current")
_EtherStatsDroppedFrames_Type = Counter32
_EtherStatsDroppedFrames_Object = MibTableColumn
etherStatsDroppedFrames = _EtherStatsDroppedFrames_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 4, 1, 1),
    _EtherStatsDroppedFrames_Type()
)
etherStatsDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsDroppedFrames.setStatus("current")
_EtherStatsCreateTime_Type = LastCreateTime
_EtherStatsCreateTime_Object = MibTableColumn
etherStatsCreateTime = _EtherStatsCreateTime_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 4, 1, 2),
    _EtherStatsCreateTime_Type()
)
etherStatsCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsCreateTime.setStatus("current")
_TokenRingMLStats2Table_Object = MibTable
tokenRingMLStats2Table = _TokenRingMLStats2Table_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 5)
)
if mibBuilder.loadTexts:
    tokenRingMLStats2Table.setStatus("deprecated")
_TokenRingMLStats2Entry_Object = MibTableRow
tokenRingMLStats2Entry = _TokenRingMLStats2Entry_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 5, 1)
)
if mibBuilder.loadTexts:
    tokenRingMLStats2Entry.setStatus("deprecated")
_TokenRingMLStatsDroppedFrames_Type = Counter32
_TokenRingMLStatsDroppedFrames_Object = MibTableColumn
tokenRingMLStatsDroppedFrames = _TokenRingMLStatsDroppedFrames_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 5, 1, 1),
    _TokenRingMLStatsDroppedFrames_Type()
)
tokenRingMLStatsDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingMLStatsDroppedFrames.setStatus("deprecated")
_TokenRingMLStatsCreateTime_Type = LastCreateTime
_TokenRingMLStatsCreateTime_Object = MibTableColumn
tokenRingMLStatsCreateTime = _TokenRingMLStatsCreateTime_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 5, 1, 2),
    _TokenRingMLStatsCreateTime_Type()
)
tokenRingMLStatsCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingMLStatsCreateTime.setStatus("deprecated")
_TokenRingPStats2Table_Object = MibTable
tokenRingPStats2Table = _TokenRingPStats2Table_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 6)
)
if mibBuilder.loadTexts:
    tokenRingPStats2Table.setStatus("deprecated")
_TokenRingPStats2Entry_Object = MibTableRow
tokenRingPStats2Entry = _TokenRingPStats2Entry_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 6, 1)
)
if mibBuilder.loadTexts:
    tokenRingPStats2Entry.setStatus("deprecated")
_TokenRingPStatsDroppedFrames_Type = Counter32
_TokenRingPStatsDroppedFrames_Object = MibTableColumn
tokenRingPStatsDroppedFrames = _TokenRingPStatsDroppedFrames_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 6, 1, 1),
    _TokenRingPStatsDroppedFrames_Type()
)
tokenRingPStatsDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingPStatsDroppedFrames.setStatus("deprecated")
_TokenRingPStatsCreateTime_Type = LastCreateTime
_TokenRingPStatsCreateTime_Object = MibTableColumn
tokenRingPStatsCreateTime = _TokenRingPStatsCreateTime_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 6, 1, 2),
    _TokenRingPStatsCreateTime_Type()
)
tokenRingPStatsCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingPStatsCreateTime.setStatus("deprecated")
_HistoryControl2Table_Object = MibTable
historyControl2Table = _HistoryControl2Table_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 5)
)
if mibBuilder.loadTexts:
    historyControl2Table.setStatus("current")
_HistoryControl2Entry_Object = MibTableRow
historyControl2Entry = _HistoryControl2Entry_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 5, 1)
)
if mibBuilder.loadTexts:
    historyControl2Entry.setStatus("current")
_HistoryControlDroppedFrames_Type = Counter32
_HistoryControlDroppedFrames_Object = MibTableColumn
historyControlDroppedFrames = _HistoryControlDroppedFrames_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 5, 1, 1),
    _HistoryControlDroppedFrames_Type()
)
historyControlDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyControlDroppedFrames.setStatus("current")
_HostControl2Table_Object = MibTable
hostControl2Table = _HostControl2Table_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 4)
)
if mibBuilder.loadTexts:
    hostControl2Table.setStatus("current")
_HostControl2Entry_Object = MibTableRow
hostControl2Entry = _HostControl2Entry_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 4, 1)
)
if mibBuilder.loadTexts:
    hostControl2Entry.setStatus("current")
_HostControlDroppedFrames_Type = Counter32
_HostControlDroppedFrames_Object = MibTableColumn
hostControlDroppedFrames = _HostControlDroppedFrames_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 4, 1, 1),
    _HostControlDroppedFrames_Type()
)
hostControlDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostControlDroppedFrames.setStatus("current")
_HostControlCreateTime_Type = LastCreateTime
_HostControlCreateTime_Object = MibTableColumn
hostControlCreateTime = _HostControlCreateTime_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 4, 1, 2),
    _HostControlCreateTime_Type()
)
hostControlCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostControlCreateTime.setStatus("current")
_MatrixControl2Table_Object = MibTable
matrixControl2Table = _MatrixControl2Table_Object(
    (1, 3, 6, 1, 2, 1, 16, 6, 4)
)
if mibBuilder.loadTexts:
    matrixControl2Table.setStatus("current")
_MatrixControl2Entry_Object = MibTableRow
matrixControl2Entry = _MatrixControl2Entry_Object(
    (1, 3, 6, 1, 2, 1, 16, 6, 4, 1)
)
if mibBuilder.loadTexts:
    matrixControl2Entry.setStatus("current")
_MatrixControlDroppedFrames_Type = Counter32
_MatrixControlDroppedFrames_Object = MibTableColumn
matrixControlDroppedFrames = _MatrixControlDroppedFrames_Object(
    (1, 3, 6, 1, 2, 1, 16, 6, 4, 1, 1),
    _MatrixControlDroppedFrames_Type()
)
matrixControlDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixControlDroppedFrames.setStatus("current")
_MatrixControlCreateTime_Type = LastCreateTime
_MatrixControlCreateTime_Object = MibTableColumn
matrixControlCreateTime = _MatrixControlCreateTime_Object(
    (1, 3, 6, 1, 2, 1, 16, 6, 4, 1, 2),
    _MatrixControlCreateTime_Type()
)
matrixControlCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixControlCreateTime.setStatus("current")
_Channel2Table_Object = MibTable
channel2Table = _Channel2Table_Object(
    (1, 3, 6, 1, 2, 1, 16, 7, 3)
)
if mibBuilder.loadTexts:
    channel2Table.setStatus("current")
_Channel2Entry_Object = MibTableRow
channel2Entry = _Channel2Entry_Object(
    (1, 3, 6, 1, 2, 1, 16, 7, 3, 1)
)
if mibBuilder.loadTexts:
    channel2Entry.setStatus("current")
_ChannelDroppedFrames_Type = Counter32
_ChannelDroppedFrames_Object = MibTableColumn
channelDroppedFrames = _ChannelDroppedFrames_Object(
    (1, 3, 6, 1, 2, 1, 16, 7, 3, 1, 1),
    _ChannelDroppedFrames_Type()
)
channelDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelDroppedFrames.setStatus("current")
_ChannelCreateTime_Type = LastCreateTime
_ChannelCreateTime_Object = MibTableColumn
channelCreateTime = _ChannelCreateTime_Object(
    (1, 3, 6, 1, 2, 1, 16, 7, 3, 1, 2),
    _ChannelCreateTime_Type()
)
channelCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelCreateTime.setStatus("current")
_Filter2Table_Object = MibTable
filter2Table = _Filter2Table_Object(
    (1, 3, 6, 1, 2, 1, 16, 7, 4)
)
if mibBuilder.loadTexts:
    filter2Table.setStatus("current")
_Filter2Entry_Object = MibTableRow
filter2Entry = _Filter2Entry_Object(
    (1, 3, 6, 1, 2, 1, 16, 7, 4, 1)
)
if mibBuilder.loadTexts:
    filter2Entry.setStatus("current")


class _FilterProtocolDirDataLocalIndex_Type(Integer32):
    """Custom type filterProtocolDirDataLocalIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FilterProtocolDirDataLocalIndex_Type.__name__ = "Integer32"
_FilterProtocolDirDataLocalIndex_Object = MibTableColumn
filterProtocolDirDataLocalIndex = _FilterProtocolDirDataLocalIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 7, 4, 1, 1),
    _FilterProtocolDirDataLocalIndex_Type()
)
filterProtocolDirDataLocalIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    filterProtocolDirDataLocalIndex.setStatus("current")


class _FilterProtocolDirLocalIndex_Type(Integer32):
    """Custom type filterProtocolDirLocalIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FilterProtocolDirLocalIndex_Type.__name__ = "Integer32"
_FilterProtocolDirLocalIndex_Object = MibTableColumn
filterProtocolDirLocalIndex = _FilterProtocolDirLocalIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 7, 4, 1, 2),
    _FilterProtocolDirLocalIndex_Type()
)
filterProtocolDirLocalIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    filterProtocolDirLocalIndex.setStatus("current")
_RingStationControl2Table_Object = MibTable
ringStationControl2Table = _RingStationControl2Table_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 7)
)
if mibBuilder.loadTexts:
    ringStationControl2Table.setStatus("deprecated")
_RingStationControl2Entry_Object = MibTableRow
ringStationControl2Entry = _RingStationControl2Entry_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 7, 1)
)
if mibBuilder.loadTexts:
    ringStationControl2Entry.setStatus("deprecated")
_RingStationControlDroppedFrames_Type = Counter32
_RingStationControlDroppedFrames_Object = MibTableColumn
ringStationControlDroppedFrames = _RingStationControlDroppedFrames_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 7, 1, 1),
    _RingStationControlDroppedFrames_Type()
)
ringStationControlDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationControlDroppedFrames.setStatus("deprecated")
_RingStationControlCreateTime_Type = LastCreateTime
_RingStationControlCreateTime_Object = MibTableColumn
ringStationControlCreateTime = _RingStationControlCreateTime_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 7, 1, 2),
    _RingStationControlCreateTime_Type()
)
ringStationControlCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationControlCreateTime.setStatus("deprecated")
_SourceRoutingStats2Table_Object = MibTable
sourceRoutingStats2Table = _SourceRoutingStats2Table_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 8)
)
if mibBuilder.loadTexts:
    sourceRoutingStats2Table.setStatus("deprecated")
_SourceRoutingStats2Entry_Object = MibTableRow
sourceRoutingStats2Entry = _SourceRoutingStats2Entry_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 8, 1)
)
if mibBuilder.loadTexts:
    sourceRoutingStats2Entry.setStatus("deprecated")
_SourceRoutingStatsDroppedFrames_Type = Counter32
_SourceRoutingStatsDroppedFrames_Object = MibTableColumn
sourceRoutingStatsDroppedFrames = _SourceRoutingStatsDroppedFrames_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 8, 1, 1),
    _SourceRoutingStatsDroppedFrames_Type()
)
sourceRoutingStatsDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceRoutingStatsDroppedFrames.setStatus("deprecated")
_SourceRoutingStatsCreateTime_Type = LastCreateTime
_SourceRoutingStatsCreateTime_Object = MibTableColumn
sourceRoutingStatsCreateTime = _SourceRoutingStatsCreateTime_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 8, 1, 2),
    _SourceRoutingStatsCreateTime_Type()
)
sourceRoutingStatsCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceRoutingStatsCreateTime.setStatus("deprecated")
_ProtocolDir_ObjectIdentity = ObjectIdentity
protocolDir = _ProtocolDir_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 11)
)
_ProtocolDirLastChange_Type = TimeStamp
_ProtocolDirLastChange_Object = MibScalar
protocolDirLastChange = _ProtocolDirLastChange_Object(
    (1, 3, 6, 1, 2, 1, 16, 11, 1),
    _ProtocolDirLastChange_Type()
)
protocolDirLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolDirLastChange.setStatus("current")
_ProtocolDirTable_Object = MibTable
protocolDirTable = _ProtocolDirTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 11, 2)
)
if mibBuilder.loadTexts:
    protocolDirTable.setStatus("current")
_ProtocolDirEntry_Object = MibTableRow
protocolDirEntry = _ProtocolDirEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 11, 2, 1)
)
protocolDirEntry.setIndexNames(
    (0, "RMON2-MIB", "protocolDirID"),
    (0, "RMON2-MIB", "protocolDirParameters"),
)
if mibBuilder.loadTexts:
    protocolDirEntry.setStatus("current")


class _ProtocolDirID_Type(OctetString):
    """Custom type protocolDirID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 128),
    )


_ProtocolDirID_Type.__name__ = "OctetString"
_ProtocolDirID_Object = MibTableColumn
protocolDirID = _ProtocolDirID_Object(
    (1, 3, 6, 1, 2, 1, 16, 11, 2, 1, 1),
    _ProtocolDirID_Type()
)
protocolDirID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    protocolDirID.setStatus("current")


class _ProtocolDirParameters_Type(OctetString):
    """Custom type protocolDirParameters based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ProtocolDirParameters_Type.__name__ = "OctetString"
_ProtocolDirParameters_Object = MibTableColumn
protocolDirParameters = _ProtocolDirParameters_Object(
    (1, 3, 6, 1, 2, 1, 16, 11, 2, 1, 2),
    _ProtocolDirParameters_Type()
)
protocolDirParameters.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    protocolDirParameters.setStatus("current")


class _ProtocolDirLocalIndex_Type(Integer32):
    """Custom type protocolDirLocalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ProtocolDirLocalIndex_Type.__name__ = "Integer32"
_ProtocolDirLocalIndex_Object = MibTableColumn
protocolDirLocalIndex = _ProtocolDirLocalIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 11, 2, 1, 3),
    _ProtocolDirLocalIndex_Type()
)
protocolDirLocalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolDirLocalIndex.setStatus("current")


class _ProtocolDirDescr_Type(DisplayString):
    """Custom type protocolDirDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ProtocolDirDescr_Type.__name__ = "DisplayString"
_ProtocolDirDescr_Object = MibTableColumn
protocolDirDescr = _ProtocolDirDescr_Object(
    (1, 3, 6, 1, 2, 1, 16, 11, 2, 1, 4),
    _ProtocolDirDescr_Type()
)
protocolDirDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    protocolDirDescr.setStatus("current")


class _ProtocolDirType_Type(Bits):
    """Custom type protocolDirType based on Bits"""
    namedValues = NamedValues(
        *(("extensible", 0),
          ("addressRecognitionCapable", 1))
    )

_ProtocolDirType_Type.__name__ = "Bits"
_ProtocolDirType_Object = MibTableColumn
protocolDirType = _ProtocolDirType_Object(
    (1, 3, 6, 1, 2, 1, 16, 11, 2, 1, 5),
    _ProtocolDirType_Type()
)
protocolDirType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolDirType.setStatus("current")


class _ProtocolDirAddressMapConfig_Type(Integer32):
    """Custom type protocolDirAddressMapConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("supportedOff", 2),
          ("supportedOn", 3))
    )


_ProtocolDirAddressMapConfig_Type.__name__ = "Integer32"
_ProtocolDirAddressMapConfig_Object = MibTableColumn
protocolDirAddressMapConfig = _ProtocolDirAddressMapConfig_Object(
    (1, 3, 6, 1, 2, 1, 16, 11, 2, 1, 6),
    _ProtocolDirAddressMapConfig_Type()
)
protocolDirAddressMapConfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    protocolDirAddressMapConfig.setStatus("current")


class _ProtocolDirHostConfig_Type(Integer32):
    """Custom type protocolDirHostConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("supportedOff", 2),
          ("supportedOn", 3))
    )


_ProtocolDirHostConfig_Type.__name__ = "Integer32"
_ProtocolDirHostConfig_Object = MibTableColumn
protocolDirHostConfig = _ProtocolDirHostConfig_Object(
    (1, 3, 6, 1, 2, 1, 16, 11, 2, 1, 7),
    _ProtocolDirHostConfig_Type()
)
protocolDirHostConfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    protocolDirHostConfig.setStatus("current")


class _ProtocolDirMatrixConfig_Type(Integer32):
    """Custom type protocolDirMatrixConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("supportedOff", 2),
          ("supportedOn", 3))
    )


_ProtocolDirMatrixConfig_Type.__name__ = "Integer32"
_ProtocolDirMatrixConfig_Object = MibTableColumn
protocolDirMatrixConfig = _ProtocolDirMatrixConfig_Object(
    (1, 3, 6, 1, 2, 1, 16, 11, 2, 1, 8),
    _ProtocolDirMatrixConfig_Type()
)
protocolDirMatrixConfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    protocolDirMatrixConfig.setStatus("current")
_ProtocolDirOwner_Type = OwnerString
_ProtocolDirOwner_Object = MibTableColumn
protocolDirOwner = _ProtocolDirOwner_Object(
    (1, 3, 6, 1, 2, 1, 16, 11, 2, 1, 9),
    _ProtocolDirOwner_Type()
)
protocolDirOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    protocolDirOwner.setStatus("current")
_ProtocolDirStatus_Type = RowStatus
_ProtocolDirStatus_Object = MibTableColumn
protocolDirStatus = _ProtocolDirStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 11, 2, 1, 10),
    _ProtocolDirStatus_Type()
)
protocolDirStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    protocolDirStatus.setStatus("current")
_ProtocolDist_ObjectIdentity = ObjectIdentity
protocolDist = _ProtocolDist_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 12)
)
_ProtocolDistControlTable_Object = MibTable
protocolDistControlTable = _ProtocolDistControlTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 12, 1)
)
if mibBuilder.loadTexts:
    protocolDistControlTable.setStatus("current")
_ProtocolDistControlEntry_Object = MibTableRow
protocolDistControlEntry = _ProtocolDistControlEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 12, 1, 1)
)
protocolDistControlEntry.setIndexNames(
    (0, "RMON2-MIB", "protocolDistControlIndex"),
)
if mibBuilder.loadTexts:
    protocolDistControlEntry.setStatus("current")


class _ProtocolDistControlIndex_Type(Integer32):
    """Custom type protocolDistControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ProtocolDistControlIndex_Type.__name__ = "Integer32"
_ProtocolDistControlIndex_Object = MibTableColumn
protocolDistControlIndex = _ProtocolDistControlIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 12, 1, 1, 1),
    _ProtocolDistControlIndex_Type()
)
protocolDistControlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    protocolDistControlIndex.setStatus("current")
_ProtocolDistControlDataSource_Type = DataSource
_ProtocolDistControlDataSource_Object = MibTableColumn
protocolDistControlDataSource = _ProtocolDistControlDataSource_Object(
    (1, 3, 6, 1, 2, 1, 16, 12, 1, 1, 2),
    _ProtocolDistControlDataSource_Type()
)
protocolDistControlDataSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    protocolDistControlDataSource.setStatus("current")
_ProtocolDistControlDroppedFrames_Type = Counter32
_ProtocolDistControlDroppedFrames_Object = MibTableColumn
protocolDistControlDroppedFrames = _ProtocolDistControlDroppedFrames_Object(
    (1, 3, 6, 1, 2, 1, 16, 12, 1, 1, 3),
    _ProtocolDistControlDroppedFrames_Type()
)
protocolDistControlDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolDistControlDroppedFrames.setStatus("current")
_ProtocolDistControlCreateTime_Type = LastCreateTime
_ProtocolDistControlCreateTime_Object = MibTableColumn
protocolDistControlCreateTime = _ProtocolDistControlCreateTime_Object(
    (1, 3, 6, 1, 2, 1, 16, 12, 1, 1, 4),
    _ProtocolDistControlCreateTime_Type()
)
protocolDistControlCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolDistControlCreateTime.setStatus("current")
_ProtocolDistControlOwner_Type = OwnerString
_ProtocolDistControlOwner_Object = MibTableColumn
protocolDistControlOwner = _ProtocolDistControlOwner_Object(
    (1, 3, 6, 1, 2, 1, 16, 12, 1, 1, 5),
    _ProtocolDistControlOwner_Type()
)
protocolDistControlOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    protocolDistControlOwner.setStatus("current")
_ProtocolDistControlStatus_Type = RowStatus
_ProtocolDistControlStatus_Object = MibTableColumn
protocolDistControlStatus = _ProtocolDistControlStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 12, 1, 1, 6),
    _ProtocolDistControlStatus_Type()
)
protocolDistControlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    protocolDistControlStatus.setStatus("current")
_ProtocolDistStatsTable_Object = MibTable
protocolDistStatsTable = _ProtocolDistStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 12, 2)
)
if mibBuilder.loadTexts:
    protocolDistStatsTable.setStatus("current")
_ProtocolDistStatsEntry_Object = MibTableRow
protocolDistStatsEntry = _ProtocolDistStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 12, 2, 1)
)
protocolDistStatsEntry.setIndexNames(
    (0, "RMON2-MIB", "protocolDistControlIndex"),
    (0, "RMON2-MIB", "protocolDirLocalIndex"),
)
if mibBuilder.loadTexts:
    protocolDistStatsEntry.setStatus("current")
_ProtocolDistStatsPkts_Type = ZeroBasedCounter32
_ProtocolDistStatsPkts_Object = MibTableColumn
protocolDistStatsPkts = _ProtocolDistStatsPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 12, 2, 1, 1),
    _ProtocolDistStatsPkts_Type()
)
protocolDistStatsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolDistStatsPkts.setStatus("current")
_ProtocolDistStatsOctets_Type = ZeroBasedCounter32
_ProtocolDistStatsOctets_Object = MibTableColumn
protocolDistStatsOctets = _ProtocolDistStatsOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 12, 2, 1, 2),
    _ProtocolDistStatsOctets_Type()
)
protocolDistStatsOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolDistStatsOctets.setStatus("current")
_AddressMap_ObjectIdentity = ObjectIdentity
addressMap = _AddressMap_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 13)
)
_AddressMapInserts_Type = Counter32
_AddressMapInserts_Object = MibScalar
addressMapInserts = _AddressMapInserts_Object(
    (1, 3, 6, 1, 2, 1, 16, 13, 1),
    _AddressMapInserts_Type()
)
addressMapInserts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addressMapInserts.setStatus("current")
_AddressMapDeletes_Type = Counter32
_AddressMapDeletes_Object = MibScalar
addressMapDeletes = _AddressMapDeletes_Object(
    (1, 3, 6, 1, 2, 1, 16, 13, 2),
    _AddressMapDeletes_Type()
)
addressMapDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addressMapDeletes.setStatus("current")


class _AddressMapMaxDesiredEntries_Type(Integer32):
    """Custom type addressMapMaxDesiredEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AddressMapMaxDesiredEntries_Type.__name__ = "Integer32"
_AddressMapMaxDesiredEntries_Object = MibScalar
addressMapMaxDesiredEntries = _AddressMapMaxDesiredEntries_Object(
    (1, 3, 6, 1, 2, 1, 16, 13, 3),
    _AddressMapMaxDesiredEntries_Type()
)
addressMapMaxDesiredEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addressMapMaxDesiredEntries.setStatus("current")
_AddressMapControlTable_Object = MibTable
addressMapControlTable = _AddressMapControlTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 13, 4)
)
if mibBuilder.loadTexts:
    addressMapControlTable.setStatus("current")
_AddressMapControlEntry_Object = MibTableRow
addressMapControlEntry = _AddressMapControlEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 13, 4, 1)
)
addressMapControlEntry.setIndexNames(
    (0, "RMON2-MIB", "addressMapControlIndex"),
)
if mibBuilder.loadTexts:
    addressMapControlEntry.setStatus("current")


class _AddressMapControlIndex_Type(Integer32):
    """Custom type addressMapControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AddressMapControlIndex_Type.__name__ = "Integer32"
_AddressMapControlIndex_Object = MibTableColumn
addressMapControlIndex = _AddressMapControlIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 13, 4, 1, 1),
    _AddressMapControlIndex_Type()
)
addressMapControlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    addressMapControlIndex.setStatus("current")
_AddressMapControlDataSource_Type = DataSource
_AddressMapControlDataSource_Object = MibTableColumn
addressMapControlDataSource = _AddressMapControlDataSource_Object(
    (1, 3, 6, 1, 2, 1, 16, 13, 4, 1, 2),
    _AddressMapControlDataSource_Type()
)
addressMapControlDataSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    addressMapControlDataSource.setStatus("current")
_AddressMapControlDroppedFrames_Type = Counter32
_AddressMapControlDroppedFrames_Object = MibTableColumn
addressMapControlDroppedFrames = _AddressMapControlDroppedFrames_Object(
    (1, 3, 6, 1, 2, 1, 16, 13, 4, 1, 3),
    _AddressMapControlDroppedFrames_Type()
)
addressMapControlDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addressMapControlDroppedFrames.setStatus("current")
_AddressMapControlOwner_Type = OwnerString
_AddressMapControlOwner_Object = MibTableColumn
addressMapControlOwner = _AddressMapControlOwner_Object(
    (1, 3, 6, 1, 2, 1, 16, 13, 4, 1, 4),
    _AddressMapControlOwner_Type()
)
addressMapControlOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    addressMapControlOwner.setStatus("current")
_AddressMapControlStatus_Type = RowStatus
_AddressMapControlStatus_Object = MibTableColumn
addressMapControlStatus = _AddressMapControlStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 13, 4, 1, 5),
    _AddressMapControlStatus_Type()
)
addressMapControlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    addressMapControlStatus.setStatus("current")
_AddressMapTable_Object = MibTable
addressMapTable = _AddressMapTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 13, 5)
)
if mibBuilder.loadTexts:
    addressMapTable.setStatus("current")
_AddressMapEntry_Object = MibTableRow
addressMapEntry = _AddressMapEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 13, 5, 1)
)
addressMapEntry.setIndexNames(
    (0, "RMON2-MIB", "addressMapTimeMark"),
    (0, "RMON2-MIB", "protocolDirLocalIndex"),
    (0, "RMON2-MIB", "addressMapNetworkAddress"),
    (0, "RMON2-MIB", "addressMapSource"),
)
if mibBuilder.loadTexts:
    addressMapEntry.setStatus("current")
_AddressMapTimeMark_Type = TimeFilter
_AddressMapTimeMark_Object = MibTableColumn
addressMapTimeMark = _AddressMapTimeMark_Object(
    (1, 3, 6, 1, 2, 1, 16, 13, 5, 1, 1),
    _AddressMapTimeMark_Type()
)
addressMapTimeMark.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    addressMapTimeMark.setStatus("current")


class _AddressMapNetworkAddress_Type(OctetString):
    """Custom type addressMapNetworkAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_AddressMapNetworkAddress_Type.__name__ = "OctetString"
_AddressMapNetworkAddress_Object = MibTableColumn
addressMapNetworkAddress = _AddressMapNetworkAddress_Object(
    (1, 3, 6, 1, 2, 1, 16, 13, 5, 1, 2),
    _AddressMapNetworkAddress_Type()
)
addressMapNetworkAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    addressMapNetworkAddress.setStatus("current")
_AddressMapSource_Type = ObjectIdentifier
_AddressMapSource_Object = MibTableColumn
addressMapSource = _AddressMapSource_Object(
    (1, 3, 6, 1, 2, 1, 16, 13, 5, 1, 3),
    _AddressMapSource_Type()
)
addressMapSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    addressMapSource.setStatus("current")
_AddressMapPhysicalAddress_Type = OctetString
_AddressMapPhysicalAddress_Object = MibTableColumn
addressMapPhysicalAddress = _AddressMapPhysicalAddress_Object(
    (1, 3, 6, 1, 2, 1, 16, 13, 5, 1, 4),
    _AddressMapPhysicalAddress_Type()
)
addressMapPhysicalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addressMapPhysicalAddress.setStatus("current")
_AddressMapLastChange_Type = TimeStamp
_AddressMapLastChange_Object = MibTableColumn
addressMapLastChange = _AddressMapLastChange_Object(
    (1, 3, 6, 1, 2, 1, 16, 13, 5, 1, 5),
    _AddressMapLastChange_Type()
)
addressMapLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addressMapLastChange.setStatus("current")
_NlHost_ObjectIdentity = ObjectIdentity
nlHost = _NlHost_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 14)
)
_HlHostControlTable_Object = MibTable
hlHostControlTable = _HlHostControlTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 14, 1)
)
if mibBuilder.loadTexts:
    hlHostControlTable.setStatus("current")
_HlHostControlEntry_Object = MibTableRow
hlHostControlEntry = _HlHostControlEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 14, 1, 1)
)
hlHostControlEntry.setIndexNames(
    (0, "RMON2-MIB", "hlHostControlIndex"),
)
if mibBuilder.loadTexts:
    hlHostControlEntry.setStatus("current")


class _HlHostControlIndex_Type(Integer32):
    """Custom type hlHostControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HlHostControlIndex_Type.__name__ = "Integer32"
_HlHostControlIndex_Object = MibTableColumn
hlHostControlIndex = _HlHostControlIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 14, 1, 1, 1),
    _HlHostControlIndex_Type()
)
hlHostControlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hlHostControlIndex.setStatus("current")
_HlHostControlDataSource_Type = DataSource
_HlHostControlDataSource_Object = MibTableColumn
hlHostControlDataSource = _HlHostControlDataSource_Object(
    (1, 3, 6, 1, 2, 1, 16, 14, 1, 1, 2),
    _HlHostControlDataSource_Type()
)
hlHostControlDataSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hlHostControlDataSource.setStatus("current")
_HlHostControlNlDroppedFrames_Type = Counter32
_HlHostControlNlDroppedFrames_Object = MibTableColumn
hlHostControlNlDroppedFrames = _HlHostControlNlDroppedFrames_Object(
    (1, 3, 6, 1, 2, 1, 16, 14, 1, 1, 3),
    _HlHostControlNlDroppedFrames_Type()
)
hlHostControlNlDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlHostControlNlDroppedFrames.setStatus("current")
_HlHostControlNlInserts_Type = Counter32
_HlHostControlNlInserts_Object = MibTableColumn
hlHostControlNlInserts = _HlHostControlNlInserts_Object(
    (1, 3, 6, 1, 2, 1, 16, 14, 1, 1, 4),
    _HlHostControlNlInserts_Type()
)
hlHostControlNlInserts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlHostControlNlInserts.setStatus("current")
_HlHostControlNlDeletes_Type = Counter32
_HlHostControlNlDeletes_Object = MibTableColumn
hlHostControlNlDeletes = _HlHostControlNlDeletes_Object(
    (1, 3, 6, 1, 2, 1, 16, 14, 1, 1, 5),
    _HlHostControlNlDeletes_Type()
)
hlHostControlNlDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlHostControlNlDeletes.setStatus("current")


class _HlHostControlNlMaxDesiredEntries_Type(Integer32):
    """Custom type hlHostControlNlMaxDesiredEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_HlHostControlNlMaxDesiredEntries_Type.__name__ = "Integer32"
_HlHostControlNlMaxDesiredEntries_Object = MibTableColumn
hlHostControlNlMaxDesiredEntries = _HlHostControlNlMaxDesiredEntries_Object(
    (1, 3, 6, 1, 2, 1, 16, 14, 1, 1, 6),
    _HlHostControlNlMaxDesiredEntries_Type()
)
hlHostControlNlMaxDesiredEntries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hlHostControlNlMaxDesiredEntries.setStatus("current")
_HlHostControlAlDroppedFrames_Type = Counter32
_HlHostControlAlDroppedFrames_Object = MibTableColumn
hlHostControlAlDroppedFrames = _HlHostControlAlDroppedFrames_Object(
    (1, 3, 6, 1, 2, 1, 16, 14, 1, 1, 7),
    _HlHostControlAlDroppedFrames_Type()
)
hlHostControlAlDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlHostControlAlDroppedFrames.setStatus("current")
_HlHostControlAlInserts_Type = Counter32
_HlHostControlAlInserts_Object = MibTableColumn
hlHostControlAlInserts = _HlHostControlAlInserts_Object(
    (1, 3, 6, 1, 2, 1, 16, 14, 1, 1, 8),
    _HlHostControlAlInserts_Type()
)
hlHostControlAlInserts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlHostControlAlInserts.setStatus("current")
_HlHostControlAlDeletes_Type = Counter32
_HlHostControlAlDeletes_Object = MibTableColumn
hlHostControlAlDeletes = _HlHostControlAlDeletes_Object(
    (1, 3, 6, 1, 2, 1, 16, 14, 1, 1, 9),
    _HlHostControlAlDeletes_Type()
)
hlHostControlAlDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlHostControlAlDeletes.setStatus("current")


class _HlHostControlAlMaxDesiredEntries_Type(Integer32):
    """Custom type hlHostControlAlMaxDesiredEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_HlHostControlAlMaxDesiredEntries_Type.__name__ = "Integer32"
_HlHostControlAlMaxDesiredEntries_Object = MibTableColumn
hlHostControlAlMaxDesiredEntries = _HlHostControlAlMaxDesiredEntries_Object(
    (1, 3, 6, 1, 2, 1, 16, 14, 1, 1, 10),
    _HlHostControlAlMaxDesiredEntries_Type()
)
hlHostControlAlMaxDesiredEntries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hlHostControlAlMaxDesiredEntries.setStatus("current")
_HlHostControlOwner_Type = OwnerString
_HlHostControlOwner_Object = MibTableColumn
hlHostControlOwner = _HlHostControlOwner_Object(
    (1, 3, 6, 1, 2, 1, 16, 14, 1, 1, 11),
    _HlHostControlOwner_Type()
)
hlHostControlOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hlHostControlOwner.setStatus("current")
_HlHostControlStatus_Type = RowStatus
_HlHostControlStatus_Object = MibTableColumn
hlHostControlStatus = _HlHostControlStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 14, 1, 1, 12),
    _HlHostControlStatus_Type()
)
hlHostControlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hlHostControlStatus.setStatus("current")
_NlHostTable_Object = MibTable
nlHostTable = _NlHostTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 14, 2)
)
if mibBuilder.loadTexts:
    nlHostTable.setStatus("current")
_NlHostEntry_Object = MibTableRow
nlHostEntry = _NlHostEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 14, 2, 1)
)
nlHostEntry.setIndexNames(
    (0, "RMON2-MIB", "hlHostControlIndex"),
    (0, "RMON2-MIB", "nlHostTimeMark"),
    (0, "RMON2-MIB", "protocolDirLocalIndex"),
    (0, "RMON2-MIB", "nlHostAddress"),
)
if mibBuilder.loadTexts:
    nlHostEntry.setStatus("current")
_NlHostTimeMark_Type = TimeFilter
_NlHostTimeMark_Object = MibTableColumn
nlHostTimeMark = _NlHostTimeMark_Object(
    (1, 3, 6, 1, 2, 1, 16, 14, 2, 1, 1),
    _NlHostTimeMark_Type()
)
nlHostTimeMark.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nlHostTimeMark.setStatus("current")


class _NlHostAddress_Type(OctetString):
    """Custom type nlHostAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_NlHostAddress_Type.__name__ = "OctetString"
_NlHostAddress_Object = MibTableColumn
nlHostAddress = _NlHostAddress_Object(
    (1, 3, 6, 1, 2, 1, 16, 14, 2, 1, 2),
    _NlHostAddress_Type()
)
nlHostAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nlHostAddress.setStatus("current")
_NlHostInPkts_Type = ZeroBasedCounter32
_NlHostInPkts_Object = MibTableColumn
nlHostInPkts = _NlHostInPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 14, 2, 1, 3),
    _NlHostInPkts_Type()
)
nlHostInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlHostInPkts.setStatus("current")
_NlHostOutPkts_Type = ZeroBasedCounter32
_NlHostOutPkts_Object = MibTableColumn
nlHostOutPkts = _NlHostOutPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 14, 2, 1, 4),
    _NlHostOutPkts_Type()
)
nlHostOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlHostOutPkts.setStatus("current")
_NlHostInOctets_Type = ZeroBasedCounter32
_NlHostInOctets_Object = MibTableColumn
nlHostInOctets = _NlHostInOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 14, 2, 1, 5),
    _NlHostInOctets_Type()
)
nlHostInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlHostInOctets.setStatus("current")
_NlHostOutOctets_Type = ZeroBasedCounter32
_NlHostOutOctets_Object = MibTableColumn
nlHostOutOctets = _NlHostOutOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 14, 2, 1, 6),
    _NlHostOutOctets_Type()
)
nlHostOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlHostOutOctets.setStatus("current")
_NlHostOutMacNonUnicastPkts_Type = ZeroBasedCounter32
_NlHostOutMacNonUnicastPkts_Object = MibTableColumn
nlHostOutMacNonUnicastPkts = _NlHostOutMacNonUnicastPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 14, 2, 1, 7),
    _NlHostOutMacNonUnicastPkts_Type()
)
nlHostOutMacNonUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlHostOutMacNonUnicastPkts.setStatus("current")
_NlHostCreateTime_Type = LastCreateTime
_NlHostCreateTime_Object = MibTableColumn
nlHostCreateTime = _NlHostCreateTime_Object(
    (1, 3, 6, 1, 2, 1, 16, 14, 2, 1, 8),
    _NlHostCreateTime_Type()
)
nlHostCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlHostCreateTime.setStatus("current")
_NlMatrix_ObjectIdentity = ObjectIdentity
nlMatrix = _NlMatrix_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 15)
)
_HlMatrixControlTable_Object = MibTable
hlMatrixControlTable = _HlMatrixControlTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 1)
)
if mibBuilder.loadTexts:
    hlMatrixControlTable.setStatus("current")
_HlMatrixControlEntry_Object = MibTableRow
hlMatrixControlEntry = _HlMatrixControlEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 1, 1)
)
hlMatrixControlEntry.setIndexNames(
    (0, "RMON2-MIB", "hlMatrixControlIndex"),
)
if mibBuilder.loadTexts:
    hlMatrixControlEntry.setStatus("current")


class _HlMatrixControlIndex_Type(Integer32):
    """Custom type hlMatrixControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HlMatrixControlIndex_Type.__name__ = "Integer32"
_HlMatrixControlIndex_Object = MibTableColumn
hlMatrixControlIndex = _HlMatrixControlIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 1, 1, 1),
    _HlMatrixControlIndex_Type()
)
hlMatrixControlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hlMatrixControlIndex.setStatus("current")
_HlMatrixControlDataSource_Type = DataSource
_HlMatrixControlDataSource_Object = MibTableColumn
hlMatrixControlDataSource = _HlMatrixControlDataSource_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 1, 1, 2),
    _HlMatrixControlDataSource_Type()
)
hlMatrixControlDataSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hlMatrixControlDataSource.setStatus("current")
_HlMatrixControlNlDroppedFrames_Type = Counter32
_HlMatrixControlNlDroppedFrames_Object = MibTableColumn
hlMatrixControlNlDroppedFrames = _HlMatrixControlNlDroppedFrames_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 1, 1, 3),
    _HlMatrixControlNlDroppedFrames_Type()
)
hlMatrixControlNlDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlMatrixControlNlDroppedFrames.setStatus("current")
_HlMatrixControlNlInserts_Type = Counter32
_HlMatrixControlNlInserts_Object = MibTableColumn
hlMatrixControlNlInserts = _HlMatrixControlNlInserts_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 1, 1, 4),
    _HlMatrixControlNlInserts_Type()
)
hlMatrixControlNlInserts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlMatrixControlNlInserts.setStatus("current")
_HlMatrixControlNlDeletes_Type = Counter32
_HlMatrixControlNlDeletes_Object = MibTableColumn
hlMatrixControlNlDeletes = _HlMatrixControlNlDeletes_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 1, 1, 5),
    _HlMatrixControlNlDeletes_Type()
)
hlMatrixControlNlDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlMatrixControlNlDeletes.setStatus("current")


class _HlMatrixControlNlMaxDesiredEntries_Type(Integer32):
    """Custom type hlMatrixControlNlMaxDesiredEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_HlMatrixControlNlMaxDesiredEntries_Type.__name__ = "Integer32"
_HlMatrixControlNlMaxDesiredEntries_Object = MibTableColumn
hlMatrixControlNlMaxDesiredEntries = _HlMatrixControlNlMaxDesiredEntries_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 1, 1, 6),
    _HlMatrixControlNlMaxDesiredEntries_Type()
)
hlMatrixControlNlMaxDesiredEntries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hlMatrixControlNlMaxDesiredEntries.setStatus("current")
_HlMatrixControlAlDroppedFrames_Type = Counter32
_HlMatrixControlAlDroppedFrames_Object = MibTableColumn
hlMatrixControlAlDroppedFrames = _HlMatrixControlAlDroppedFrames_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 1, 1, 7),
    _HlMatrixControlAlDroppedFrames_Type()
)
hlMatrixControlAlDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlMatrixControlAlDroppedFrames.setStatus("current")
_HlMatrixControlAlInserts_Type = Counter32
_HlMatrixControlAlInserts_Object = MibTableColumn
hlMatrixControlAlInserts = _HlMatrixControlAlInserts_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 1, 1, 8),
    _HlMatrixControlAlInserts_Type()
)
hlMatrixControlAlInserts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlMatrixControlAlInserts.setStatus("current")
_HlMatrixControlAlDeletes_Type = Counter32
_HlMatrixControlAlDeletes_Object = MibTableColumn
hlMatrixControlAlDeletes = _HlMatrixControlAlDeletes_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 1, 1, 9),
    _HlMatrixControlAlDeletes_Type()
)
hlMatrixControlAlDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlMatrixControlAlDeletes.setStatus("current")


class _HlMatrixControlAlMaxDesiredEntries_Type(Integer32):
    """Custom type hlMatrixControlAlMaxDesiredEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_HlMatrixControlAlMaxDesiredEntries_Type.__name__ = "Integer32"
_HlMatrixControlAlMaxDesiredEntries_Object = MibTableColumn
hlMatrixControlAlMaxDesiredEntries = _HlMatrixControlAlMaxDesiredEntries_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 1, 1, 10),
    _HlMatrixControlAlMaxDesiredEntries_Type()
)
hlMatrixControlAlMaxDesiredEntries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hlMatrixControlAlMaxDesiredEntries.setStatus("current")
_HlMatrixControlOwner_Type = OwnerString
_HlMatrixControlOwner_Object = MibTableColumn
hlMatrixControlOwner = _HlMatrixControlOwner_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 1, 1, 11),
    _HlMatrixControlOwner_Type()
)
hlMatrixControlOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hlMatrixControlOwner.setStatus("current")
_HlMatrixControlStatus_Type = RowStatus
_HlMatrixControlStatus_Object = MibTableColumn
hlMatrixControlStatus = _HlMatrixControlStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 1, 1, 12),
    _HlMatrixControlStatus_Type()
)
hlMatrixControlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hlMatrixControlStatus.setStatus("current")
_NlMatrixSDTable_Object = MibTable
nlMatrixSDTable = _NlMatrixSDTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 2)
)
if mibBuilder.loadTexts:
    nlMatrixSDTable.setStatus("current")
_NlMatrixSDEntry_Object = MibTableRow
nlMatrixSDEntry = _NlMatrixSDEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 2, 1)
)
nlMatrixSDEntry.setIndexNames(
    (0, "RMON2-MIB", "hlMatrixControlIndex"),
    (0, "RMON2-MIB", "nlMatrixSDTimeMark"),
    (0, "RMON2-MIB", "protocolDirLocalIndex"),
    (0, "RMON2-MIB", "nlMatrixSDSourceAddress"),
    (0, "RMON2-MIB", "nlMatrixSDDestAddress"),
)
if mibBuilder.loadTexts:
    nlMatrixSDEntry.setStatus("current")
_NlMatrixSDTimeMark_Type = TimeFilter
_NlMatrixSDTimeMark_Object = MibTableColumn
nlMatrixSDTimeMark = _NlMatrixSDTimeMark_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 2, 1, 1),
    _NlMatrixSDTimeMark_Type()
)
nlMatrixSDTimeMark.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nlMatrixSDTimeMark.setStatus("current")


class _NlMatrixSDSourceAddress_Type(OctetString):
    """Custom type nlMatrixSDSourceAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_NlMatrixSDSourceAddress_Type.__name__ = "OctetString"
_NlMatrixSDSourceAddress_Object = MibTableColumn
nlMatrixSDSourceAddress = _NlMatrixSDSourceAddress_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 2, 1, 2),
    _NlMatrixSDSourceAddress_Type()
)
nlMatrixSDSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nlMatrixSDSourceAddress.setStatus("current")


class _NlMatrixSDDestAddress_Type(OctetString):
    """Custom type nlMatrixSDDestAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_NlMatrixSDDestAddress_Type.__name__ = "OctetString"
_NlMatrixSDDestAddress_Object = MibTableColumn
nlMatrixSDDestAddress = _NlMatrixSDDestAddress_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 2, 1, 3),
    _NlMatrixSDDestAddress_Type()
)
nlMatrixSDDestAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nlMatrixSDDestAddress.setStatus("current")
_NlMatrixSDPkts_Type = ZeroBasedCounter32
_NlMatrixSDPkts_Object = MibTableColumn
nlMatrixSDPkts = _NlMatrixSDPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 2, 1, 4),
    _NlMatrixSDPkts_Type()
)
nlMatrixSDPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlMatrixSDPkts.setStatus("current")
_NlMatrixSDOctets_Type = ZeroBasedCounter32
_NlMatrixSDOctets_Object = MibTableColumn
nlMatrixSDOctets = _NlMatrixSDOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 2, 1, 5),
    _NlMatrixSDOctets_Type()
)
nlMatrixSDOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlMatrixSDOctets.setStatus("current")
_NlMatrixSDCreateTime_Type = LastCreateTime
_NlMatrixSDCreateTime_Object = MibTableColumn
nlMatrixSDCreateTime = _NlMatrixSDCreateTime_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 2, 1, 6),
    _NlMatrixSDCreateTime_Type()
)
nlMatrixSDCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlMatrixSDCreateTime.setStatus("current")
_NlMatrixDSTable_Object = MibTable
nlMatrixDSTable = _NlMatrixDSTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 3)
)
if mibBuilder.loadTexts:
    nlMatrixDSTable.setStatus("current")
_NlMatrixDSEntry_Object = MibTableRow
nlMatrixDSEntry = _NlMatrixDSEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 3, 1)
)
nlMatrixDSEntry.setIndexNames(
    (0, "RMON2-MIB", "hlMatrixControlIndex"),
    (0, "RMON2-MIB", "nlMatrixDSTimeMark"),
    (0, "RMON2-MIB", "protocolDirLocalIndex"),
    (0, "RMON2-MIB", "nlMatrixDSDestAddress"),
    (0, "RMON2-MIB", "nlMatrixDSSourceAddress"),
)
if mibBuilder.loadTexts:
    nlMatrixDSEntry.setStatus("current")
_NlMatrixDSTimeMark_Type = TimeFilter
_NlMatrixDSTimeMark_Object = MibTableColumn
nlMatrixDSTimeMark = _NlMatrixDSTimeMark_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 3, 1, 1),
    _NlMatrixDSTimeMark_Type()
)
nlMatrixDSTimeMark.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nlMatrixDSTimeMark.setStatus("current")


class _NlMatrixDSSourceAddress_Type(OctetString):
    """Custom type nlMatrixDSSourceAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_NlMatrixDSSourceAddress_Type.__name__ = "OctetString"
_NlMatrixDSSourceAddress_Object = MibTableColumn
nlMatrixDSSourceAddress = _NlMatrixDSSourceAddress_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 3, 1, 2),
    _NlMatrixDSSourceAddress_Type()
)
nlMatrixDSSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nlMatrixDSSourceAddress.setStatus("current")


class _NlMatrixDSDestAddress_Type(OctetString):
    """Custom type nlMatrixDSDestAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_NlMatrixDSDestAddress_Type.__name__ = "OctetString"
_NlMatrixDSDestAddress_Object = MibTableColumn
nlMatrixDSDestAddress = _NlMatrixDSDestAddress_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 3, 1, 3),
    _NlMatrixDSDestAddress_Type()
)
nlMatrixDSDestAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nlMatrixDSDestAddress.setStatus("current")
_NlMatrixDSPkts_Type = ZeroBasedCounter32
_NlMatrixDSPkts_Object = MibTableColumn
nlMatrixDSPkts = _NlMatrixDSPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 3, 1, 4),
    _NlMatrixDSPkts_Type()
)
nlMatrixDSPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlMatrixDSPkts.setStatus("current")
_NlMatrixDSOctets_Type = ZeroBasedCounter32
_NlMatrixDSOctets_Object = MibTableColumn
nlMatrixDSOctets = _NlMatrixDSOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 3, 1, 5),
    _NlMatrixDSOctets_Type()
)
nlMatrixDSOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlMatrixDSOctets.setStatus("current")
_NlMatrixDSCreateTime_Type = LastCreateTime
_NlMatrixDSCreateTime_Object = MibTableColumn
nlMatrixDSCreateTime = _NlMatrixDSCreateTime_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 3, 1, 6),
    _NlMatrixDSCreateTime_Type()
)
nlMatrixDSCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlMatrixDSCreateTime.setStatus("current")
_NlMatrixTopNControlTable_Object = MibTable
nlMatrixTopNControlTable = _NlMatrixTopNControlTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 4)
)
if mibBuilder.loadTexts:
    nlMatrixTopNControlTable.setStatus("current")
_NlMatrixTopNControlEntry_Object = MibTableRow
nlMatrixTopNControlEntry = _NlMatrixTopNControlEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 4, 1)
)
nlMatrixTopNControlEntry.setIndexNames(
    (0, "RMON2-MIB", "nlMatrixTopNControlIndex"),
)
if mibBuilder.loadTexts:
    nlMatrixTopNControlEntry.setStatus("current")


class _NlMatrixTopNControlIndex_Type(Integer32):
    """Custom type nlMatrixTopNControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NlMatrixTopNControlIndex_Type.__name__ = "Integer32"
_NlMatrixTopNControlIndex_Object = MibTableColumn
nlMatrixTopNControlIndex = _NlMatrixTopNControlIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 4, 1, 1),
    _NlMatrixTopNControlIndex_Type()
)
nlMatrixTopNControlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nlMatrixTopNControlIndex.setStatus("current")


class _NlMatrixTopNControlMatrixIndex_Type(Integer32):
    """Custom type nlMatrixTopNControlMatrixIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NlMatrixTopNControlMatrixIndex_Type.__name__ = "Integer32"
_NlMatrixTopNControlMatrixIndex_Object = MibTableColumn
nlMatrixTopNControlMatrixIndex = _NlMatrixTopNControlMatrixIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 4, 1, 2),
    _NlMatrixTopNControlMatrixIndex_Type()
)
nlMatrixTopNControlMatrixIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nlMatrixTopNControlMatrixIndex.setStatus("current")


class _NlMatrixTopNControlRateBase_Type(Integer32):
    """Custom type nlMatrixTopNControlRateBase based on Integer32"""
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
        *(("nlMatrixTopNPkts", 1),
          ("nlMatrixTopNOctets", 2),
          ("nlMatrixTopNHighCapacityPkts", 3),
          ("nlMatrixTopNHighCapacityOctets", 4))
    )


_NlMatrixTopNControlRateBase_Type.__name__ = "Integer32"
_NlMatrixTopNControlRateBase_Object = MibTableColumn
nlMatrixTopNControlRateBase = _NlMatrixTopNControlRateBase_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 4, 1, 3),
    _NlMatrixTopNControlRateBase_Type()
)
nlMatrixTopNControlRateBase.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nlMatrixTopNControlRateBase.setStatus("current")


class _NlMatrixTopNControlTimeRemaining_Type(Integer32):
    """Custom type nlMatrixTopNControlTimeRemaining based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NlMatrixTopNControlTimeRemaining_Type.__name__ = "Integer32"
_NlMatrixTopNControlTimeRemaining_Object = MibTableColumn
nlMatrixTopNControlTimeRemaining = _NlMatrixTopNControlTimeRemaining_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 4, 1, 4),
    _NlMatrixTopNControlTimeRemaining_Type()
)
nlMatrixTopNControlTimeRemaining.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nlMatrixTopNControlTimeRemaining.setStatus("current")
_NlMatrixTopNControlGeneratedReports_Type = Counter32
_NlMatrixTopNControlGeneratedReports_Object = MibTableColumn
nlMatrixTopNControlGeneratedReports = _NlMatrixTopNControlGeneratedReports_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 4, 1, 5),
    _NlMatrixTopNControlGeneratedReports_Type()
)
nlMatrixTopNControlGeneratedReports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlMatrixTopNControlGeneratedReports.setStatus("current")
_NlMatrixTopNControlDuration_Type = Integer32
_NlMatrixTopNControlDuration_Object = MibTableColumn
nlMatrixTopNControlDuration = _NlMatrixTopNControlDuration_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 4, 1, 6),
    _NlMatrixTopNControlDuration_Type()
)
nlMatrixTopNControlDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlMatrixTopNControlDuration.setStatus("current")


class _NlMatrixTopNControlRequestedSize_Type(Integer32):
    """Custom type nlMatrixTopNControlRequestedSize based on Integer32"""
    defaultValue = 150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NlMatrixTopNControlRequestedSize_Type.__name__ = "Integer32"
_NlMatrixTopNControlRequestedSize_Object = MibTableColumn
nlMatrixTopNControlRequestedSize = _NlMatrixTopNControlRequestedSize_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 4, 1, 7),
    _NlMatrixTopNControlRequestedSize_Type()
)
nlMatrixTopNControlRequestedSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nlMatrixTopNControlRequestedSize.setStatus("current")


class _NlMatrixTopNControlGrantedSize_Type(Integer32):
    """Custom type nlMatrixTopNControlGrantedSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NlMatrixTopNControlGrantedSize_Type.__name__ = "Integer32"
_NlMatrixTopNControlGrantedSize_Object = MibTableColumn
nlMatrixTopNControlGrantedSize = _NlMatrixTopNControlGrantedSize_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 4, 1, 8),
    _NlMatrixTopNControlGrantedSize_Type()
)
nlMatrixTopNControlGrantedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlMatrixTopNControlGrantedSize.setStatus("current")
_NlMatrixTopNControlStartTime_Type = TimeStamp
_NlMatrixTopNControlStartTime_Object = MibTableColumn
nlMatrixTopNControlStartTime = _NlMatrixTopNControlStartTime_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 4, 1, 9),
    _NlMatrixTopNControlStartTime_Type()
)
nlMatrixTopNControlStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlMatrixTopNControlStartTime.setStatus("current")
_NlMatrixTopNControlOwner_Type = OwnerString
_NlMatrixTopNControlOwner_Object = MibTableColumn
nlMatrixTopNControlOwner = _NlMatrixTopNControlOwner_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 4, 1, 10),
    _NlMatrixTopNControlOwner_Type()
)
nlMatrixTopNControlOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nlMatrixTopNControlOwner.setStatus("current")
_NlMatrixTopNControlStatus_Type = RowStatus
_NlMatrixTopNControlStatus_Object = MibTableColumn
nlMatrixTopNControlStatus = _NlMatrixTopNControlStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 4, 1, 11),
    _NlMatrixTopNControlStatus_Type()
)
nlMatrixTopNControlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nlMatrixTopNControlStatus.setStatus("current")
_NlMatrixTopNTable_Object = MibTable
nlMatrixTopNTable = _NlMatrixTopNTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 5)
)
if mibBuilder.loadTexts:
    nlMatrixTopNTable.setStatus("current")
_NlMatrixTopNEntry_Object = MibTableRow
nlMatrixTopNEntry = _NlMatrixTopNEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 5, 1)
)
nlMatrixTopNEntry.setIndexNames(
    (0, "RMON2-MIB", "nlMatrixTopNControlIndex"),
    (0, "RMON2-MIB", "nlMatrixTopNIndex"),
)
if mibBuilder.loadTexts:
    nlMatrixTopNEntry.setStatus("current")


class _NlMatrixTopNIndex_Type(Integer32):
    """Custom type nlMatrixTopNIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NlMatrixTopNIndex_Type.__name__ = "Integer32"
_NlMatrixTopNIndex_Object = MibTableColumn
nlMatrixTopNIndex = _NlMatrixTopNIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 5, 1, 1),
    _NlMatrixTopNIndex_Type()
)
nlMatrixTopNIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nlMatrixTopNIndex.setStatus("current")


class _NlMatrixTopNProtocolDirLocalIndex_Type(Integer32):
    """Custom type nlMatrixTopNProtocolDirLocalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NlMatrixTopNProtocolDirLocalIndex_Type.__name__ = "Integer32"
_NlMatrixTopNProtocolDirLocalIndex_Object = MibTableColumn
nlMatrixTopNProtocolDirLocalIndex = _NlMatrixTopNProtocolDirLocalIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 5, 1, 2),
    _NlMatrixTopNProtocolDirLocalIndex_Type()
)
nlMatrixTopNProtocolDirLocalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlMatrixTopNProtocolDirLocalIndex.setStatus("current")


class _NlMatrixTopNSourceAddress_Type(OctetString):
    """Custom type nlMatrixTopNSourceAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_NlMatrixTopNSourceAddress_Type.__name__ = "OctetString"
_NlMatrixTopNSourceAddress_Object = MibTableColumn
nlMatrixTopNSourceAddress = _NlMatrixTopNSourceAddress_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 5, 1, 3),
    _NlMatrixTopNSourceAddress_Type()
)
nlMatrixTopNSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlMatrixTopNSourceAddress.setStatus("current")


class _NlMatrixTopNDestAddress_Type(OctetString):
    """Custom type nlMatrixTopNDestAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_NlMatrixTopNDestAddress_Type.__name__ = "OctetString"
_NlMatrixTopNDestAddress_Object = MibTableColumn
nlMatrixTopNDestAddress = _NlMatrixTopNDestAddress_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 5, 1, 4),
    _NlMatrixTopNDestAddress_Type()
)
nlMatrixTopNDestAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlMatrixTopNDestAddress.setStatus("current")
_NlMatrixTopNPktRate_Type = Gauge32
_NlMatrixTopNPktRate_Object = MibTableColumn
nlMatrixTopNPktRate = _NlMatrixTopNPktRate_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 5, 1, 5),
    _NlMatrixTopNPktRate_Type()
)
nlMatrixTopNPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlMatrixTopNPktRate.setStatus("current")
_NlMatrixTopNReversePktRate_Type = Gauge32
_NlMatrixTopNReversePktRate_Object = MibTableColumn
nlMatrixTopNReversePktRate = _NlMatrixTopNReversePktRate_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 5, 1, 6),
    _NlMatrixTopNReversePktRate_Type()
)
nlMatrixTopNReversePktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlMatrixTopNReversePktRate.setStatus("current")
_NlMatrixTopNOctetRate_Type = Gauge32
_NlMatrixTopNOctetRate_Object = MibTableColumn
nlMatrixTopNOctetRate = _NlMatrixTopNOctetRate_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 5, 1, 7),
    _NlMatrixTopNOctetRate_Type()
)
nlMatrixTopNOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlMatrixTopNOctetRate.setStatus("current")
_NlMatrixTopNReverseOctetRate_Type = Gauge32
_NlMatrixTopNReverseOctetRate_Object = MibTableColumn
nlMatrixTopNReverseOctetRate = _NlMatrixTopNReverseOctetRate_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 5, 1, 8),
    _NlMatrixTopNReverseOctetRate_Type()
)
nlMatrixTopNReverseOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlMatrixTopNReverseOctetRate.setStatus("current")
_AlHost_ObjectIdentity = ObjectIdentity
alHost = _AlHost_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 16)
)
_AlHostTable_Object = MibTable
alHostTable = _AlHostTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 16, 1)
)
if mibBuilder.loadTexts:
    alHostTable.setStatus("current")
_AlHostEntry_Object = MibTableRow
alHostEntry = _AlHostEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 16, 1, 1)
)
alHostEntry.setIndexNames(
    (0, "RMON2-MIB", "hlHostControlIndex"),
    (0, "RMON2-MIB", "alHostTimeMark"),
    (0, "RMON2-MIB", "protocolDirLocalIndex"),
    (0, "RMON2-MIB", "nlHostAddress"),
    (0, "RMON2-MIB", "protocolDirLocalIndex"),
)
if mibBuilder.loadTexts:
    alHostEntry.setStatus("current")
_AlHostTimeMark_Type = TimeFilter
_AlHostTimeMark_Object = MibTableColumn
alHostTimeMark = _AlHostTimeMark_Object(
    (1, 3, 6, 1, 2, 1, 16, 16, 1, 1, 1),
    _AlHostTimeMark_Type()
)
alHostTimeMark.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alHostTimeMark.setStatus("current")
_AlHostInPkts_Type = ZeroBasedCounter32
_AlHostInPkts_Object = MibTableColumn
alHostInPkts = _AlHostInPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 16, 1, 1, 2),
    _AlHostInPkts_Type()
)
alHostInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHostInPkts.setStatus("current")
_AlHostOutPkts_Type = ZeroBasedCounter32
_AlHostOutPkts_Object = MibTableColumn
alHostOutPkts = _AlHostOutPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 16, 1, 1, 3),
    _AlHostOutPkts_Type()
)
alHostOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHostOutPkts.setStatus("current")
_AlHostInOctets_Type = ZeroBasedCounter32
_AlHostInOctets_Object = MibTableColumn
alHostInOctets = _AlHostInOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 16, 1, 1, 4),
    _AlHostInOctets_Type()
)
alHostInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHostInOctets.setStatus("current")
_AlHostOutOctets_Type = ZeroBasedCounter32
_AlHostOutOctets_Object = MibTableColumn
alHostOutOctets = _AlHostOutOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 16, 1, 1, 5),
    _AlHostOutOctets_Type()
)
alHostOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHostOutOctets.setStatus("current")
_AlHostCreateTime_Type = LastCreateTime
_AlHostCreateTime_Object = MibTableColumn
alHostCreateTime = _AlHostCreateTime_Object(
    (1, 3, 6, 1, 2, 1, 16, 16, 1, 1, 6),
    _AlHostCreateTime_Type()
)
alHostCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHostCreateTime.setStatus("current")
_AlMatrix_ObjectIdentity = ObjectIdentity
alMatrix = _AlMatrix_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 17)
)
_AlMatrixSDTable_Object = MibTable
alMatrixSDTable = _AlMatrixSDTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 1)
)
if mibBuilder.loadTexts:
    alMatrixSDTable.setStatus("current")
_AlMatrixSDEntry_Object = MibTableRow
alMatrixSDEntry = _AlMatrixSDEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 1, 1)
)
alMatrixSDEntry.setIndexNames(
    (0, "RMON2-MIB", "hlMatrixControlIndex"),
    (0, "RMON2-MIB", "alMatrixSDTimeMark"),
    (0, "RMON2-MIB", "protocolDirLocalIndex"),
    (0, "RMON2-MIB", "nlMatrixSDSourceAddress"),
    (0, "RMON2-MIB", "nlMatrixSDDestAddress"),
    (0, "RMON2-MIB", "protocolDirLocalIndex"),
)
if mibBuilder.loadTexts:
    alMatrixSDEntry.setStatus("current")
_AlMatrixSDTimeMark_Type = TimeFilter
_AlMatrixSDTimeMark_Object = MibTableColumn
alMatrixSDTimeMark = _AlMatrixSDTimeMark_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 1, 1, 1),
    _AlMatrixSDTimeMark_Type()
)
alMatrixSDTimeMark.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alMatrixSDTimeMark.setStatus("current")
_AlMatrixSDPkts_Type = ZeroBasedCounter32
_AlMatrixSDPkts_Object = MibTableColumn
alMatrixSDPkts = _AlMatrixSDPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 1, 1, 2),
    _AlMatrixSDPkts_Type()
)
alMatrixSDPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMatrixSDPkts.setStatus("current")
_AlMatrixSDOctets_Type = ZeroBasedCounter32
_AlMatrixSDOctets_Object = MibTableColumn
alMatrixSDOctets = _AlMatrixSDOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 1, 1, 3),
    _AlMatrixSDOctets_Type()
)
alMatrixSDOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMatrixSDOctets.setStatus("current")
_AlMatrixSDCreateTime_Type = LastCreateTime
_AlMatrixSDCreateTime_Object = MibTableColumn
alMatrixSDCreateTime = _AlMatrixSDCreateTime_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 1, 1, 4),
    _AlMatrixSDCreateTime_Type()
)
alMatrixSDCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMatrixSDCreateTime.setStatus("current")
_AlMatrixDSTable_Object = MibTable
alMatrixDSTable = _AlMatrixDSTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 2)
)
if mibBuilder.loadTexts:
    alMatrixDSTable.setStatus("current")
_AlMatrixDSEntry_Object = MibTableRow
alMatrixDSEntry = _AlMatrixDSEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 2, 1)
)
alMatrixDSEntry.setIndexNames(
    (0, "RMON2-MIB", "hlMatrixControlIndex"),
    (0, "RMON2-MIB", "alMatrixDSTimeMark"),
    (0, "RMON2-MIB", "protocolDirLocalIndex"),
    (0, "RMON2-MIB", "nlMatrixDSDestAddress"),
    (0, "RMON2-MIB", "nlMatrixDSSourceAddress"),
    (0, "RMON2-MIB", "protocolDirLocalIndex"),
)
if mibBuilder.loadTexts:
    alMatrixDSEntry.setStatus("current")
_AlMatrixDSTimeMark_Type = TimeFilter
_AlMatrixDSTimeMark_Object = MibTableColumn
alMatrixDSTimeMark = _AlMatrixDSTimeMark_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 2, 1, 1),
    _AlMatrixDSTimeMark_Type()
)
alMatrixDSTimeMark.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alMatrixDSTimeMark.setStatus("current")
_AlMatrixDSPkts_Type = ZeroBasedCounter32
_AlMatrixDSPkts_Object = MibTableColumn
alMatrixDSPkts = _AlMatrixDSPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 2, 1, 2),
    _AlMatrixDSPkts_Type()
)
alMatrixDSPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMatrixDSPkts.setStatus("current")
_AlMatrixDSOctets_Type = ZeroBasedCounter32
_AlMatrixDSOctets_Object = MibTableColumn
alMatrixDSOctets = _AlMatrixDSOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 2, 1, 3),
    _AlMatrixDSOctets_Type()
)
alMatrixDSOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMatrixDSOctets.setStatus("current")
_AlMatrixDSCreateTime_Type = LastCreateTime
_AlMatrixDSCreateTime_Object = MibTableColumn
alMatrixDSCreateTime = _AlMatrixDSCreateTime_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 2, 1, 4),
    _AlMatrixDSCreateTime_Type()
)
alMatrixDSCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMatrixDSCreateTime.setStatus("current")
_AlMatrixTopNControlTable_Object = MibTable
alMatrixTopNControlTable = _AlMatrixTopNControlTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 3)
)
if mibBuilder.loadTexts:
    alMatrixTopNControlTable.setStatus("current")
_AlMatrixTopNControlEntry_Object = MibTableRow
alMatrixTopNControlEntry = _AlMatrixTopNControlEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 3, 1)
)
alMatrixTopNControlEntry.setIndexNames(
    (0, "RMON2-MIB", "alMatrixTopNControlIndex"),
)
if mibBuilder.loadTexts:
    alMatrixTopNControlEntry.setStatus("current")


class _AlMatrixTopNControlIndex_Type(Integer32):
    """Custom type alMatrixTopNControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AlMatrixTopNControlIndex_Type.__name__ = "Integer32"
_AlMatrixTopNControlIndex_Object = MibTableColumn
alMatrixTopNControlIndex = _AlMatrixTopNControlIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 3, 1, 1),
    _AlMatrixTopNControlIndex_Type()
)
alMatrixTopNControlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alMatrixTopNControlIndex.setStatus("current")


class _AlMatrixTopNControlMatrixIndex_Type(Integer32):
    """Custom type alMatrixTopNControlMatrixIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AlMatrixTopNControlMatrixIndex_Type.__name__ = "Integer32"
_AlMatrixTopNControlMatrixIndex_Object = MibTableColumn
alMatrixTopNControlMatrixIndex = _AlMatrixTopNControlMatrixIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 3, 1, 2),
    _AlMatrixTopNControlMatrixIndex_Type()
)
alMatrixTopNControlMatrixIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alMatrixTopNControlMatrixIndex.setStatus("current")


class _AlMatrixTopNControlRateBase_Type(Integer32):
    """Custom type alMatrixTopNControlRateBase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("alMatrixTopNTerminalsPkts", 1),
          ("alMatrixTopNTerminalsOctets", 2),
          ("alMatrixTopNAllPkts", 3),
          ("alMatrixTopNAllOctets", 4),
          ("alMatrixTopNTerminalsHighCapacityPkts", 5),
          ("alMatrixTopNTerminalsHighCapacityOctets", 6),
          ("alMatrixTopNAllHighCapacityPkts", 7),
          ("alMatrixTopNAllHighCapacityOctets", 8))
    )


_AlMatrixTopNControlRateBase_Type.__name__ = "Integer32"
_AlMatrixTopNControlRateBase_Object = MibTableColumn
alMatrixTopNControlRateBase = _AlMatrixTopNControlRateBase_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 3, 1, 3),
    _AlMatrixTopNControlRateBase_Type()
)
alMatrixTopNControlRateBase.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alMatrixTopNControlRateBase.setStatus("current")


class _AlMatrixTopNControlTimeRemaining_Type(Integer32):
    """Custom type alMatrixTopNControlTimeRemaining based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlMatrixTopNControlTimeRemaining_Type.__name__ = "Integer32"
_AlMatrixTopNControlTimeRemaining_Object = MibTableColumn
alMatrixTopNControlTimeRemaining = _AlMatrixTopNControlTimeRemaining_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 3, 1, 4),
    _AlMatrixTopNControlTimeRemaining_Type()
)
alMatrixTopNControlTimeRemaining.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alMatrixTopNControlTimeRemaining.setStatus("current")
_AlMatrixTopNControlGeneratedReports_Type = Counter32
_AlMatrixTopNControlGeneratedReports_Object = MibTableColumn
alMatrixTopNControlGeneratedReports = _AlMatrixTopNControlGeneratedReports_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 3, 1, 5),
    _AlMatrixTopNControlGeneratedReports_Type()
)
alMatrixTopNControlGeneratedReports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMatrixTopNControlGeneratedReports.setStatus("current")
_AlMatrixTopNControlDuration_Type = Integer32
_AlMatrixTopNControlDuration_Object = MibTableColumn
alMatrixTopNControlDuration = _AlMatrixTopNControlDuration_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 3, 1, 6),
    _AlMatrixTopNControlDuration_Type()
)
alMatrixTopNControlDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMatrixTopNControlDuration.setStatus("current")


class _AlMatrixTopNControlRequestedSize_Type(Integer32):
    """Custom type alMatrixTopNControlRequestedSize based on Integer32"""
    defaultValue = 150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlMatrixTopNControlRequestedSize_Type.__name__ = "Integer32"
_AlMatrixTopNControlRequestedSize_Object = MibTableColumn
alMatrixTopNControlRequestedSize = _AlMatrixTopNControlRequestedSize_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 3, 1, 7),
    _AlMatrixTopNControlRequestedSize_Type()
)
alMatrixTopNControlRequestedSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alMatrixTopNControlRequestedSize.setStatus("current")


class _AlMatrixTopNControlGrantedSize_Type(Integer32):
    """Custom type alMatrixTopNControlGrantedSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlMatrixTopNControlGrantedSize_Type.__name__ = "Integer32"
_AlMatrixTopNControlGrantedSize_Object = MibTableColumn
alMatrixTopNControlGrantedSize = _AlMatrixTopNControlGrantedSize_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 3, 1, 8),
    _AlMatrixTopNControlGrantedSize_Type()
)
alMatrixTopNControlGrantedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMatrixTopNControlGrantedSize.setStatus("current")
_AlMatrixTopNControlStartTime_Type = TimeStamp
_AlMatrixTopNControlStartTime_Object = MibTableColumn
alMatrixTopNControlStartTime = _AlMatrixTopNControlStartTime_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 3, 1, 9),
    _AlMatrixTopNControlStartTime_Type()
)
alMatrixTopNControlStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMatrixTopNControlStartTime.setStatus("current")
_AlMatrixTopNControlOwner_Type = OwnerString
_AlMatrixTopNControlOwner_Object = MibTableColumn
alMatrixTopNControlOwner = _AlMatrixTopNControlOwner_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 3, 1, 10),
    _AlMatrixTopNControlOwner_Type()
)
alMatrixTopNControlOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alMatrixTopNControlOwner.setStatus("current")
_AlMatrixTopNControlStatus_Type = RowStatus
_AlMatrixTopNControlStatus_Object = MibTableColumn
alMatrixTopNControlStatus = _AlMatrixTopNControlStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 3, 1, 11),
    _AlMatrixTopNControlStatus_Type()
)
alMatrixTopNControlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alMatrixTopNControlStatus.setStatus("current")
_AlMatrixTopNTable_Object = MibTable
alMatrixTopNTable = _AlMatrixTopNTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 4)
)
if mibBuilder.loadTexts:
    alMatrixTopNTable.setStatus("current")
_AlMatrixTopNEntry_Object = MibTableRow
alMatrixTopNEntry = _AlMatrixTopNEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 4, 1)
)
alMatrixTopNEntry.setIndexNames(
    (0, "RMON2-MIB", "alMatrixTopNControlIndex"),
    (0, "RMON2-MIB", "alMatrixTopNIndex"),
)
if mibBuilder.loadTexts:
    alMatrixTopNEntry.setStatus("current")


class _AlMatrixTopNIndex_Type(Integer32):
    """Custom type alMatrixTopNIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AlMatrixTopNIndex_Type.__name__ = "Integer32"
_AlMatrixTopNIndex_Object = MibTableColumn
alMatrixTopNIndex = _AlMatrixTopNIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 4, 1, 1),
    _AlMatrixTopNIndex_Type()
)
alMatrixTopNIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alMatrixTopNIndex.setStatus("current")


class _AlMatrixTopNProtocolDirLocalIndex_Type(Integer32):
    """Custom type alMatrixTopNProtocolDirLocalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AlMatrixTopNProtocolDirLocalIndex_Type.__name__ = "Integer32"
_AlMatrixTopNProtocolDirLocalIndex_Object = MibTableColumn
alMatrixTopNProtocolDirLocalIndex = _AlMatrixTopNProtocolDirLocalIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 4, 1, 2),
    _AlMatrixTopNProtocolDirLocalIndex_Type()
)
alMatrixTopNProtocolDirLocalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMatrixTopNProtocolDirLocalIndex.setStatus("current")


class _AlMatrixTopNSourceAddress_Type(OctetString):
    """Custom type alMatrixTopNSourceAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_AlMatrixTopNSourceAddress_Type.__name__ = "OctetString"
_AlMatrixTopNSourceAddress_Object = MibTableColumn
alMatrixTopNSourceAddress = _AlMatrixTopNSourceAddress_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 4, 1, 3),
    _AlMatrixTopNSourceAddress_Type()
)
alMatrixTopNSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMatrixTopNSourceAddress.setStatus("current")


class _AlMatrixTopNDestAddress_Type(OctetString):
    """Custom type alMatrixTopNDestAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_AlMatrixTopNDestAddress_Type.__name__ = "OctetString"
_AlMatrixTopNDestAddress_Object = MibTableColumn
alMatrixTopNDestAddress = _AlMatrixTopNDestAddress_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 4, 1, 4),
    _AlMatrixTopNDestAddress_Type()
)
alMatrixTopNDestAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMatrixTopNDestAddress.setStatus("current")


class _AlMatrixTopNAppProtocolDirLocalIndex_Type(Integer32):
    """Custom type alMatrixTopNAppProtocolDirLocalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AlMatrixTopNAppProtocolDirLocalIndex_Type.__name__ = "Integer32"
_AlMatrixTopNAppProtocolDirLocalIndex_Object = MibTableColumn
alMatrixTopNAppProtocolDirLocalIndex = _AlMatrixTopNAppProtocolDirLocalIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 4, 1, 5),
    _AlMatrixTopNAppProtocolDirLocalIndex_Type()
)
alMatrixTopNAppProtocolDirLocalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMatrixTopNAppProtocolDirLocalIndex.setStatus("current")
_AlMatrixTopNPktRate_Type = Gauge32
_AlMatrixTopNPktRate_Object = MibTableColumn
alMatrixTopNPktRate = _AlMatrixTopNPktRate_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 4, 1, 6),
    _AlMatrixTopNPktRate_Type()
)
alMatrixTopNPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMatrixTopNPktRate.setStatus("current")
_AlMatrixTopNReversePktRate_Type = Gauge32
_AlMatrixTopNReversePktRate_Object = MibTableColumn
alMatrixTopNReversePktRate = _AlMatrixTopNReversePktRate_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 4, 1, 7),
    _AlMatrixTopNReversePktRate_Type()
)
alMatrixTopNReversePktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMatrixTopNReversePktRate.setStatus("current")
_AlMatrixTopNOctetRate_Type = Gauge32
_AlMatrixTopNOctetRate_Object = MibTableColumn
alMatrixTopNOctetRate = _AlMatrixTopNOctetRate_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 4, 1, 8),
    _AlMatrixTopNOctetRate_Type()
)
alMatrixTopNOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMatrixTopNOctetRate.setStatus("current")
_AlMatrixTopNReverseOctetRate_Type = Gauge32
_AlMatrixTopNReverseOctetRate_Object = MibTableColumn
alMatrixTopNReverseOctetRate = _AlMatrixTopNReverseOctetRate_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 4, 1, 9),
    _AlMatrixTopNReverseOctetRate_Type()
)
alMatrixTopNReverseOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMatrixTopNReverseOctetRate.setStatus("current")
_UsrHistory_ObjectIdentity = ObjectIdentity
usrHistory = _UsrHistory_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 18)
)
_UsrHistoryControlTable_Object = MibTable
usrHistoryControlTable = _UsrHistoryControlTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 18, 1)
)
if mibBuilder.loadTexts:
    usrHistoryControlTable.setStatus("current")
_UsrHistoryControlEntry_Object = MibTableRow
usrHistoryControlEntry = _UsrHistoryControlEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 18, 1, 1)
)
usrHistoryControlEntry.setIndexNames(
    (0, "RMON2-MIB", "usrHistoryControlIndex"),
)
if mibBuilder.loadTexts:
    usrHistoryControlEntry.setStatus("current")


class _UsrHistoryControlIndex_Type(Integer32):
    """Custom type usrHistoryControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UsrHistoryControlIndex_Type.__name__ = "Integer32"
_UsrHistoryControlIndex_Object = MibTableColumn
usrHistoryControlIndex = _UsrHistoryControlIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 18, 1, 1, 1),
    _UsrHistoryControlIndex_Type()
)
usrHistoryControlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usrHistoryControlIndex.setStatus("current")


class _UsrHistoryControlObjects_Type(Integer32):
    """Custom type usrHistoryControlObjects based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UsrHistoryControlObjects_Type.__name__ = "Integer32"
_UsrHistoryControlObjects_Object = MibTableColumn
usrHistoryControlObjects = _UsrHistoryControlObjects_Object(
    (1, 3, 6, 1, 2, 1, 16, 18, 1, 1, 2),
    _UsrHistoryControlObjects_Type()
)
usrHistoryControlObjects.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usrHistoryControlObjects.setStatus("current")


class _UsrHistoryControlBucketsRequested_Type(Integer32):
    """Custom type usrHistoryControlBucketsRequested based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UsrHistoryControlBucketsRequested_Type.__name__ = "Integer32"
_UsrHistoryControlBucketsRequested_Object = MibTableColumn
usrHistoryControlBucketsRequested = _UsrHistoryControlBucketsRequested_Object(
    (1, 3, 6, 1, 2, 1, 16, 18, 1, 1, 3),
    _UsrHistoryControlBucketsRequested_Type()
)
usrHistoryControlBucketsRequested.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usrHistoryControlBucketsRequested.setStatus("current")


class _UsrHistoryControlBucketsGranted_Type(Integer32):
    """Custom type usrHistoryControlBucketsGranted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UsrHistoryControlBucketsGranted_Type.__name__ = "Integer32"
_UsrHistoryControlBucketsGranted_Object = MibTableColumn
usrHistoryControlBucketsGranted = _UsrHistoryControlBucketsGranted_Object(
    (1, 3, 6, 1, 2, 1, 16, 18, 1, 1, 4),
    _UsrHistoryControlBucketsGranted_Type()
)
usrHistoryControlBucketsGranted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usrHistoryControlBucketsGranted.setStatus("current")


class _UsrHistoryControlInterval_Type(Integer32):
    """Custom type usrHistoryControlInterval based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_UsrHistoryControlInterval_Type.__name__ = "Integer32"
_UsrHistoryControlInterval_Object = MibTableColumn
usrHistoryControlInterval = _UsrHistoryControlInterval_Object(
    (1, 3, 6, 1, 2, 1, 16, 18, 1, 1, 5),
    _UsrHistoryControlInterval_Type()
)
usrHistoryControlInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usrHistoryControlInterval.setStatus("current")
_UsrHistoryControlOwner_Type = OwnerString
_UsrHistoryControlOwner_Object = MibTableColumn
usrHistoryControlOwner = _UsrHistoryControlOwner_Object(
    (1, 3, 6, 1, 2, 1, 16, 18, 1, 1, 6),
    _UsrHistoryControlOwner_Type()
)
usrHistoryControlOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usrHistoryControlOwner.setStatus("current")
_UsrHistoryControlStatus_Type = RowStatus
_UsrHistoryControlStatus_Object = MibTableColumn
usrHistoryControlStatus = _UsrHistoryControlStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 18, 1, 1, 7),
    _UsrHistoryControlStatus_Type()
)
usrHistoryControlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usrHistoryControlStatus.setStatus("current")
_UsrHistoryObjectTable_Object = MibTable
usrHistoryObjectTable = _UsrHistoryObjectTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 18, 2)
)
if mibBuilder.loadTexts:
    usrHistoryObjectTable.setStatus("current")
_UsrHistoryObjectEntry_Object = MibTableRow
usrHistoryObjectEntry = _UsrHistoryObjectEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 18, 2, 1)
)
usrHistoryObjectEntry.setIndexNames(
    (0, "RMON2-MIB", "usrHistoryControlIndex"),
    (0, "RMON2-MIB", "usrHistoryObjectIndex"),
)
if mibBuilder.loadTexts:
    usrHistoryObjectEntry.setStatus("current")


class _UsrHistoryObjectIndex_Type(Integer32):
    """Custom type usrHistoryObjectIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UsrHistoryObjectIndex_Type.__name__ = "Integer32"
_UsrHistoryObjectIndex_Object = MibTableColumn
usrHistoryObjectIndex = _UsrHistoryObjectIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 18, 2, 1, 1),
    _UsrHistoryObjectIndex_Type()
)
usrHistoryObjectIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usrHistoryObjectIndex.setStatus("current")
_UsrHistoryObjectVariable_Type = ObjectIdentifier
_UsrHistoryObjectVariable_Object = MibTableColumn
usrHistoryObjectVariable = _UsrHistoryObjectVariable_Object(
    (1, 3, 6, 1, 2, 1, 16, 18, 2, 1, 2),
    _UsrHistoryObjectVariable_Type()
)
usrHistoryObjectVariable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usrHistoryObjectVariable.setStatus("current")


class _UsrHistoryObjectSampleType_Type(Integer32):
    """Custom type usrHistoryObjectSampleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absoluteValue", 1),
          ("deltaValue", 2))
    )


_UsrHistoryObjectSampleType_Type.__name__ = "Integer32"
_UsrHistoryObjectSampleType_Object = MibTableColumn
usrHistoryObjectSampleType = _UsrHistoryObjectSampleType_Object(
    (1, 3, 6, 1, 2, 1, 16, 18, 2, 1, 3),
    _UsrHistoryObjectSampleType_Type()
)
usrHistoryObjectSampleType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usrHistoryObjectSampleType.setStatus("current")
_UsrHistoryTable_Object = MibTable
usrHistoryTable = _UsrHistoryTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 18, 3)
)
if mibBuilder.loadTexts:
    usrHistoryTable.setStatus("current")
_UsrHistoryEntry_Object = MibTableRow
usrHistoryEntry = _UsrHistoryEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 18, 3, 1)
)
usrHistoryEntry.setIndexNames(
    (0, "RMON2-MIB", "usrHistoryControlIndex"),
    (0, "RMON2-MIB", "usrHistorySampleIndex"),
    (0, "RMON2-MIB", "usrHistoryObjectIndex"),
)
if mibBuilder.loadTexts:
    usrHistoryEntry.setStatus("current")


class _UsrHistorySampleIndex_Type(Integer32):
    """Custom type usrHistorySampleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_UsrHistorySampleIndex_Type.__name__ = "Integer32"
_UsrHistorySampleIndex_Object = MibTableColumn
usrHistorySampleIndex = _UsrHistorySampleIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 18, 3, 1, 1),
    _UsrHistorySampleIndex_Type()
)
usrHistorySampleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usrHistorySampleIndex.setStatus("current")
_UsrHistoryIntervalStart_Type = TimeStamp
_UsrHistoryIntervalStart_Object = MibTableColumn
usrHistoryIntervalStart = _UsrHistoryIntervalStart_Object(
    (1, 3, 6, 1, 2, 1, 16, 18, 3, 1, 2),
    _UsrHistoryIntervalStart_Type()
)
usrHistoryIntervalStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usrHistoryIntervalStart.setStatus("current")
_UsrHistoryIntervalEnd_Type = TimeStamp
_UsrHistoryIntervalEnd_Object = MibTableColumn
usrHistoryIntervalEnd = _UsrHistoryIntervalEnd_Object(
    (1, 3, 6, 1, 2, 1, 16, 18, 3, 1, 3),
    _UsrHistoryIntervalEnd_Type()
)
usrHistoryIntervalEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usrHistoryIntervalEnd.setStatus("current")
_UsrHistoryAbsValue_Type = Gauge32
_UsrHistoryAbsValue_Object = MibTableColumn
usrHistoryAbsValue = _UsrHistoryAbsValue_Object(
    (1, 3, 6, 1, 2, 1, 16, 18, 3, 1, 4),
    _UsrHistoryAbsValue_Type()
)
usrHistoryAbsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usrHistoryAbsValue.setStatus("current")


class _UsrHistoryValStatus_Type(Integer32):
    """Custom type usrHistoryValStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("valueNotAvailable", 1),
          ("valuePositive", 2),
          ("valueNegative", 3))
    )


_UsrHistoryValStatus_Type.__name__ = "Integer32"
_UsrHistoryValStatus_Object = MibTableColumn
usrHistoryValStatus = _UsrHistoryValStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 18, 3, 1, 5),
    _UsrHistoryValStatus_Type()
)
usrHistoryValStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usrHistoryValStatus.setStatus("current")
_ProbeConfig_ObjectIdentity = ObjectIdentity
probeConfig = _ProbeConfig_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 19)
)


class _ProbeCapabilities_Type(Bits):
    """Custom type probeCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("etherStats", 0),
          ("historyControl", 1),
          ("etherHistory", 2),
          ("alarm", 3),
          ("hosts", 4),
          ("hostTopN", 5),
          ("matrix", 6),
          ("filter", 7),
          ("capture", 8),
          ("event", 9),
          ("tokenRingMLStats", 10),
          ("tokenRingPStats", 11),
          ("tokenRingMLHistory", 12),
          ("tokenRingPHistory", 13),
          ("ringStation", 14),
          ("ringStationOrder", 15),
          ("ringStationConfig", 16),
          ("sourceRouting", 17),
          ("protocolDirectory", 18),
          ("protocolDistribution", 19),
          ("addressMapping", 20),
          ("nlHost", 21),
          ("nlMatrix", 22),
          ("alHost", 23),
          ("alMatrix", 24),
          ("usrHistory", 25),
          ("probeConfig", 26))
    )

_ProbeCapabilities_Type.__name__ = "Bits"
_ProbeCapabilities_Object = MibScalar
probeCapabilities = _ProbeCapabilities_Object(
    (1, 3, 6, 1, 2, 1, 16, 19, 1),
    _ProbeCapabilities_Type()
)
probeCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probeCapabilities.setStatus("current")


class _ProbeSoftwareRev_Type(DisplayString):
    """Custom type probeSoftwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ProbeSoftwareRev_Type.__name__ = "DisplayString"
_ProbeSoftwareRev_Object = MibScalar
probeSoftwareRev = _ProbeSoftwareRev_Object(
    (1, 3, 6, 1, 2, 1, 16, 19, 2),
    _ProbeSoftwareRev_Type()
)
probeSoftwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probeSoftwareRev.setStatus("current")


class _ProbeHardwareRev_Type(DisplayString):
    """Custom type probeHardwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ProbeHardwareRev_Type.__name__ = "DisplayString"
_ProbeHardwareRev_Object = MibScalar
probeHardwareRev = _ProbeHardwareRev_Object(
    (1, 3, 6, 1, 2, 1, 16, 19, 3),
    _ProbeHardwareRev_Type()
)
probeHardwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probeHardwareRev.setStatus("current")


class _ProbeDateTime_Type(OctetString):
    """Custom type probeDateTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(11, 11),
    )


_ProbeDateTime_Type.__name__ = "OctetString"
_ProbeDateTime_Object = MibScalar
probeDateTime = _ProbeDateTime_Object(
    (1, 3, 6, 1, 2, 1, 16, 19, 4),
    _ProbeDateTime_Type()
)
probeDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    probeDateTime.setStatus("current")


class _ProbeResetControl_Type(Integer32):
    """Custom type probeResetControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("warmBoot", 2),
          ("coldBoot", 3))
    )


_ProbeResetControl_Type.__name__ = "Integer32"
_ProbeResetControl_Object = MibScalar
probeResetControl = _ProbeResetControl_Object(
    (1, 3, 6, 1, 2, 1, 16, 19, 5),
    _ProbeResetControl_Type()
)
probeResetControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    probeResetControl.setStatus("current")


class _ProbeDownloadFile_Type(DisplayString):
    """Custom type probeDownloadFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_ProbeDownloadFile_Type.__name__ = "DisplayString"
_ProbeDownloadFile_Object = MibScalar
probeDownloadFile = _ProbeDownloadFile_Object(
    (1, 3, 6, 1, 2, 1, 16, 19, 6),
    _ProbeDownloadFile_Type()
)
probeDownloadFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    probeDownloadFile.setStatus("deprecated")
_ProbeDownloadTFTPServer_Type = IpAddress
_ProbeDownloadTFTPServer_Object = MibScalar
probeDownloadTFTPServer = _ProbeDownloadTFTPServer_Object(
    (1, 3, 6, 1, 2, 1, 16, 19, 7),
    _ProbeDownloadTFTPServer_Type()
)
probeDownloadTFTPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    probeDownloadTFTPServer.setStatus("deprecated")


class _ProbeDownloadAction_Type(Integer32):
    """Custom type probeDownloadAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notDownloading", 1),
          ("downloadToPROM", 2),
          ("downloadToRAM", 3))
    )


_ProbeDownloadAction_Type.__name__ = "Integer32"
_ProbeDownloadAction_Object = MibScalar
probeDownloadAction = _ProbeDownloadAction_Object(
    (1, 3, 6, 1, 2, 1, 16, 19, 8),
    _ProbeDownloadAction_Type()
)
probeDownloadAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    probeDownloadAction.setStatus("deprecated")


class _ProbeDownloadStatus_Type(Integer32):
    """Custom type probeDownloadStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("downloadSuccess", 1),
          ("downloadStatusUnknown", 2),
          ("downloadGeneralError", 3),
          ("downloadNoResponseFromServer", 4),
          ("downloadChecksumError", 5),
          ("downloadIncompatibleImage", 6),
          ("downloadTftpFileNotFound", 7),
          ("downloadTftpAccessViolation", 8))
    )


_ProbeDownloadStatus_Type.__name__ = "Integer32"
_ProbeDownloadStatus_Object = MibScalar
probeDownloadStatus = _ProbeDownloadStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 19, 9),
    _ProbeDownloadStatus_Type()
)
probeDownloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probeDownloadStatus.setStatus("deprecated")
_SerialConfigTable_Object = MibTable
serialConfigTable = _SerialConfigTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 19, 10)
)
if mibBuilder.loadTexts:
    serialConfigTable.setStatus("deprecated")
_SerialConfigEntry_Object = MibTableRow
serialConfigEntry = _SerialConfigEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 19, 10, 1)
)
serialConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    serialConfigEntry.setStatus("deprecated")


class _SerialMode_Type(Integer32):
    """Custom type serialMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("direct", 1),
          ("modem", 2))
    )


_SerialMode_Type.__name__ = "Integer32"
_SerialMode_Object = MibTableColumn
serialMode = _SerialMode_Object(
    (1, 3, 6, 1, 2, 1, 16, 19, 10, 1, 1),
    _SerialMode_Type()
)
serialMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    serialMode.setStatus("deprecated")


class _SerialProtocol_Type(Integer32):
    """Custom type serialProtocol based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("slip", 2),
          ("ppp", 3))
    )


_SerialProtocol_Type.__name__ = "Integer32"
_SerialProtocol_Object = MibTableColumn
serialProtocol = _SerialProtocol_Object(
    (1, 3, 6, 1, 2, 1, 16, 19, 10, 1, 2),
    _SerialProtocol_Type()
)
serialProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    serialProtocol.setStatus("deprecated")


class _SerialTimeout_Type(Integer32):
    """Custom type serialTimeout based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SerialTimeout_Type.__name__ = "Integer32"
_SerialTimeout_Object = MibTableColumn
serialTimeout = _SerialTimeout_Object(
    (1, 3, 6, 1, 2, 1, 16, 19, 10, 1, 3),
    _SerialTimeout_Type()
)
serialTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    serialTimeout.setStatus("deprecated")


class _SerialModemInitString_Type(ControlString):
    """Custom type serialModemInitString based on ControlString"""
    subtypeSpec = ControlString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SerialModemInitString_Type.__name__ = "ControlString"
_SerialModemInitString_Object = MibTableColumn
serialModemInitString = _SerialModemInitString_Object(
    (1, 3, 6, 1, 2, 1, 16, 19, 10, 1, 4),
    _SerialModemInitString_Type()
)
serialModemInitString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    serialModemInitString.setStatus("deprecated")


class _SerialModemHangUpString_Type(ControlString):
    """Custom type serialModemHangUpString based on ControlString"""
    subtypeSpec = ControlString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SerialModemHangUpString_Type.__name__ = "ControlString"
_SerialModemHangUpString_Object = MibTableColumn
serialModemHangUpString = _SerialModemHangUpString_Object(
    (1, 3, 6, 1, 2, 1, 16, 19, 10, 1, 5),
    _SerialModemHangUpString_Type()
)
serialModemHangUpString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    serialModemHangUpString.setStatus("deprecated")


class _SerialModemConnectResp_Type(DisplayString):
    """Custom type serialModemConnectResp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SerialModemConnectResp_Type.__name__ = "DisplayString"
_SerialModemConnectResp_Object = MibTableColumn
serialModemConnectResp = _SerialModemConnectResp_Object(
    (1, 3, 6, 1, 2, 1, 16, 19, 10, 1, 6),
    _SerialModemConnectResp_Type()
)
serialModemConnectResp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    serialModemConnectResp.setStatus("deprecated")


class _SerialModemNoConnectResp_Type(DisplayString):
    """Custom type serialModemNoConnectResp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SerialModemNoConnectResp_Type.__name__ = "DisplayString"
_SerialModemNoConnectResp_Object = MibTableColumn
serialModemNoConnectResp = _SerialModemNoConnectResp_Object(
    (1, 3, 6, 1, 2, 1, 16, 19, 10, 1, 7),
    _SerialModemNoConnectResp_Type()
)
serialModemNoConnectResp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    serialModemNoConnectResp.setStatus("deprecated")


class _SerialDialoutTimeout_Type(Integer32):
    """Custom type serialDialoutTimeout based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SerialDialoutTimeout_Type.__name__ = "Integer32"
_SerialDialoutTimeout_Object = MibTableColumn
serialDialoutTimeout = _SerialDialoutTimeout_Object(
    (1, 3, 6, 1, 2, 1, 16, 19, 10, 1, 8),
    _SerialDialoutTimeout_Type()
)
serialDialoutTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    serialDialoutTimeout.setStatus("deprecated")
_SerialStatus_Type = RowStatus
_SerialStatus_Object = MibTableColumn
serialStatus = _SerialStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 19, 10, 1, 9),
    _SerialStatus_Type()
)
serialStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    serialStatus.setStatus("deprecated")
_NetConfigTable_Object = MibTable
netConfigTable = _NetConfigTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 19, 11)
)
if mibBuilder.loadTexts:
    netConfigTable.setStatus("deprecated")
_NetConfigEntry_Object = MibTableRow
netConfigEntry = _NetConfigEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 19, 11, 1)
)
netConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    netConfigEntry.setStatus("deprecated")
_NetConfigIPAddress_Type = IpAddress
_NetConfigIPAddress_Object = MibTableColumn
netConfigIPAddress = _NetConfigIPAddress_Object(
    (1, 3, 6, 1, 2, 1, 16, 19, 11, 1, 1),
    _NetConfigIPAddress_Type()
)
netConfigIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    netConfigIPAddress.setStatus("deprecated")
_NetConfigSubnetMask_Type = IpAddress
_NetConfigSubnetMask_Object = MibTableColumn
netConfigSubnetMask = _NetConfigSubnetMask_Object(
    (1, 3, 6, 1, 2, 1, 16, 19, 11, 1, 2),
    _NetConfigSubnetMask_Type()
)
netConfigSubnetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    netConfigSubnetMask.setStatus("deprecated")
_NetConfigStatus_Type = RowStatus
_NetConfigStatus_Object = MibTableColumn
netConfigStatus = _NetConfigStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 19, 11, 1, 3),
    _NetConfigStatus_Type()
)
netConfigStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    netConfigStatus.setStatus("deprecated")
_NetDefaultGateway_Type = IpAddress
_NetDefaultGateway_Object = MibScalar
netDefaultGateway = _NetDefaultGateway_Object(
    (1, 3, 6, 1, 2, 1, 16, 19, 12),
    _NetDefaultGateway_Type()
)
netDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netDefaultGateway.setStatus("deprecated")
_TrapDestTable_Object = MibTable
trapDestTable = _TrapDestTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 19, 13)
)
if mibBuilder.loadTexts:
    trapDestTable.setStatus("deprecated")
_TrapDestEntry_Object = MibTableRow
trapDestEntry = _TrapDestEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 19, 13, 1)
)
trapDestEntry.setIndexNames(
    (0, "RMON2-MIB", "trapDestIndex"),
)
if mibBuilder.loadTexts:
    trapDestEntry.setStatus("deprecated")


class _TrapDestIndex_Type(Integer32):
    """Custom type trapDestIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TrapDestIndex_Type.__name__ = "Integer32"
_TrapDestIndex_Object = MibTableColumn
trapDestIndex = _TrapDestIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 19, 13, 1, 1),
    _TrapDestIndex_Type()
)
trapDestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapDestIndex.setStatus("deprecated")


class _TrapDestCommunity_Type(OctetString):
    """Custom type trapDestCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_TrapDestCommunity_Type.__name__ = "OctetString"
_TrapDestCommunity_Object = MibTableColumn
trapDestCommunity = _TrapDestCommunity_Object(
    (1, 3, 6, 1, 2, 1, 16, 19, 13, 1, 2),
    _TrapDestCommunity_Type()
)
trapDestCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trapDestCommunity.setStatus("deprecated")


class _TrapDestProtocol_Type(Integer32):
    """Custom type trapDestProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("ipx", 2))
    )


_TrapDestProtocol_Type.__name__ = "Integer32"
_TrapDestProtocol_Object = MibTableColumn
trapDestProtocol = _TrapDestProtocol_Object(
    (1, 3, 6, 1, 2, 1, 16, 19, 13, 1, 3),
    _TrapDestProtocol_Type()
)
trapDestProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trapDestProtocol.setStatus("deprecated")
_TrapDestAddress_Type = OctetString
_TrapDestAddress_Object = MibTableColumn
trapDestAddress = _TrapDestAddress_Object(
    (1, 3, 6, 1, 2, 1, 16, 19, 13, 1, 4),
    _TrapDestAddress_Type()
)
trapDestAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trapDestAddress.setStatus("deprecated")
_TrapDestOwner_Type = OwnerString
_TrapDestOwner_Object = MibTableColumn
trapDestOwner = _TrapDestOwner_Object(
    (1, 3, 6, 1, 2, 1, 16, 19, 13, 1, 5),
    _TrapDestOwner_Type()
)
trapDestOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trapDestOwner.setStatus("deprecated")
_TrapDestStatus_Type = RowStatus
_TrapDestStatus_Object = MibTableColumn
trapDestStatus = _TrapDestStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 19, 13, 1, 6),
    _TrapDestStatus_Type()
)
trapDestStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trapDestStatus.setStatus("deprecated")
_SerialConnectionTable_Object = MibTable
serialConnectionTable = _SerialConnectionTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 19, 14)
)
if mibBuilder.loadTexts:
    serialConnectionTable.setStatus("deprecated")
_SerialConnectionEntry_Object = MibTableRow
serialConnectionEntry = _SerialConnectionEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 19, 14, 1)
)
serialConnectionEntry.setIndexNames(
    (0, "RMON2-MIB", "serialConnectIndex"),
)
if mibBuilder.loadTexts:
    serialConnectionEntry.setStatus("deprecated")


class _SerialConnectIndex_Type(Integer32):
    """Custom type serialConnectIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SerialConnectIndex_Type.__name__ = "Integer32"
_SerialConnectIndex_Object = MibTableColumn
serialConnectIndex = _SerialConnectIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 19, 14, 1, 1),
    _SerialConnectIndex_Type()
)
serialConnectIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    serialConnectIndex.setStatus("deprecated")
_SerialConnectDestIpAddress_Type = IpAddress
_SerialConnectDestIpAddress_Object = MibTableColumn
serialConnectDestIpAddress = _SerialConnectDestIpAddress_Object(
    (1, 3, 6, 1, 2, 1, 16, 19, 14, 1, 2),
    _SerialConnectDestIpAddress_Type()
)
serialConnectDestIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    serialConnectDestIpAddress.setStatus("deprecated")


class _SerialConnectType_Type(Integer32):
    """Custom type serialConnectType based on Integer32"""
    defaultValue = 1

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
        *(("direct", 1),
          ("modem", 2),
          ("switch", 3),
          ("modemSwitch", 4))
    )


_SerialConnectType_Type.__name__ = "Integer32"
_SerialConnectType_Object = MibTableColumn
serialConnectType = _SerialConnectType_Object(
    (1, 3, 6, 1, 2, 1, 16, 19, 14, 1, 3),
    _SerialConnectType_Type()
)
serialConnectType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    serialConnectType.setStatus("deprecated")


class _SerialConnectDialString_Type(ControlString):
    """Custom type serialConnectDialString based on ControlString"""
    subtypeSpec = ControlString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SerialConnectDialString_Type.__name__ = "ControlString"
_SerialConnectDialString_Object = MibTableColumn
serialConnectDialString = _SerialConnectDialString_Object(
    (1, 3, 6, 1, 2, 1, 16, 19, 14, 1, 4),
    _SerialConnectDialString_Type()
)
serialConnectDialString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    serialConnectDialString.setStatus("deprecated")


class _SerialConnectSwitchConnectSeq_Type(ControlString):
    """Custom type serialConnectSwitchConnectSeq based on ControlString"""
    subtypeSpec = ControlString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SerialConnectSwitchConnectSeq_Type.__name__ = "ControlString"
_SerialConnectSwitchConnectSeq_Object = MibTableColumn
serialConnectSwitchConnectSeq = _SerialConnectSwitchConnectSeq_Object(
    (1, 3, 6, 1, 2, 1, 16, 19, 14, 1, 5),
    _SerialConnectSwitchConnectSeq_Type()
)
serialConnectSwitchConnectSeq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    serialConnectSwitchConnectSeq.setStatus("deprecated")


class _SerialConnectSwitchDisconnectSeq_Type(ControlString):
    """Custom type serialConnectSwitchDisconnectSeq based on ControlString"""
    subtypeSpec = ControlString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SerialConnectSwitchDisconnectSeq_Type.__name__ = "ControlString"
_SerialConnectSwitchDisconnectSeq_Object = MibTableColumn
serialConnectSwitchDisconnectSeq = _SerialConnectSwitchDisconnectSeq_Object(
    (1, 3, 6, 1, 2, 1, 16, 19, 14, 1, 6),
    _SerialConnectSwitchDisconnectSeq_Type()
)
serialConnectSwitchDisconnectSeq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    serialConnectSwitchDisconnectSeq.setStatus("deprecated")


class _SerialConnectSwitchResetSeq_Type(ControlString):
    """Custom type serialConnectSwitchResetSeq based on ControlString"""
    subtypeSpec = ControlString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SerialConnectSwitchResetSeq_Type.__name__ = "ControlString"
_SerialConnectSwitchResetSeq_Object = MibTableColumn
serialConnectSwitchResetSeq = _SerialConnectSwitchResetSeq_Object(
    (1, 3, 6, 1, 2, 1, 16, 19, 14, 1, 7),
    _SerialConnectSwitchResetSeq_Type()
)
serialConnectSwitchResetSeq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    serialConnectSwitchResetSeq.setStatus("deprecated")
_SerialConnectOwner_Type = OwnerString
_SerialConnectOwner_Object = MibTableColumn
serialConnectOwner = _SerialConnectOwner_Object(
    (1, 3, 6, 1, 2, 1, 16, 19, 14, 1, 8),
    _SerialConnectOwner_Type()
)
serialConnectOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    serialConnectOwner.setStatus("deprecated")
_SerialConnectStatus_Type = RowStatus
_SerialConnectStatus_Object = MibTableColumn
serialConnectStatus = _SerialConnectStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 19, 14, 1, 9),
    _SerialConnectStatus_Type()
)
serialConnectStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    serialConnectStatus.setStatus("deprecated")
_RmonConformance_ObjectIdentity = ObjectIdentity
rmonConformance = _RmonConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 20)
)
_Rmon2MIBCompliances_ObjectIdentity = ObjectIdentity
rmon2MIBCompliances = _Rmon2MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 20, 1)
)
_Rmon2MIBGroups_ObjectIdentity = ObjectIdentity
rmon2MIBGroups = _Rmon2MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 20, 2)
)
etherStatsEntry.registerAugmentions(
    ("RMON2-MIB",
     "etherStats2Entry")
)
etherStats2Entry.setIndexNames(*etherStatsEntry.getIndexNames())
tokenRingMLStatsEntry.registerAugmentions(
    ("RMON2-MIB",
     "tokenRingMLStats2Entry")
)
tokenRingMLStats2Entry.setIndexNames(*tokenRingMLStatsEntry.getIndexNames())
tokenRingPStatsEntry.registerAugmentions(
    ("RMON2-MIB",
     "tokenRingPStats2Entry")
)
tokenRingPStats2Entry.setIndexNames(*tokenRingPStatsEntry.getIndexNames())
historyControlEntry.registerAugmentions(
    ("RMON2-MIB",
     "historyControl2Entry")
)
historyControl2Entry.setIndexNames(*historyControlEntry.getIndexNames())
hostControlEntry.registerAugmentions(
    ("RMON2-MIB",
     "hostControl2Entry")
)
hostControl2Entry.setIndexNames(*hostControlEntry.getIndexNames())
matrixControlEntry.registerAugmentions(
    ("RMON2-MIB",
     "matrixControl2Entry")
)
matrixControl2Entry.setIndexNames(*matrixControlEntry.getIndexNames())
channelEntry.registerAugmentions(
    ("RMON2-MIB",
     "channel2Entry")
)
channel2Entry.setIndexNames(*channelEntry.getIndexNames())
filterEntry.registerAugmentions(
    ("RMON2-MIB",
     "filter2Entry")
)
filter2Entry.setIndexNames(*filterEntry.getIndexNames())
ringStationControlEntry.registerAugmentions(
    ("RMON2-MIB",
     "ringStationControl2Entry")
)
ringStationControl2Entry.setIndexNames(*ringStationControlEntry.getIndexNames())
sourceRoutingStatsEntry.registerAugmentions(
    ("RMON2-MIB",
     "sourceRoutingStats2Entry")
)
sourceRoutingStats2Entry.setIndexNames(*sourceRoutingStatsEntry.getIndexNames())

# Managed Objects groups

protocolDirectoryGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 20, 2, 1)
)
protocolDirectoryGroup.setObjects(
      *(("RMON2-MIB", "protocolDirLastChange"),
        ("RMON2-MIB", "protocolDirLocalIndex"),
        ("RMON2-MIB", "protocolDirDescr"),
        ("RMON2-MIB", "protocolDirType"),
        ("RMON2-MIB", "protocolDirAddressMapConfig"),
        ("RMON2-MIB", "protocolDirHostConfig"),
        ("RMON2-MIB", "protocolDirMatrixConfig"),
        ("RMON2-MIB", "protocolDirOwner"),
        ("RMON2-MIB", "protocolDirStatus"))
)
if mibBuilder.loadTexts:
    protocolDirectoryGroup.setStatus("current")

protocolDistributionGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 20, 2, 2)
)
protocolDistributionGroup.setObjects(
      *(("RMON2-MIB", "protocolDistControlDataSource"),
        ("RMON2-MIB", "protocolDistControlDroppedFrames"),
        ("RMON2-MIB", "protocolDistControlCreateTime"),
        ("RMON2-MIB", "protocolDistControlOwner"),
        ("RMON2-MIB", "protocolDistControlStatus"),
        ("RMON2-MIB", "protocolDistStatsPkts"),
        ("RMON2-MIB", "protocolDistStatsOctets"))
)
if mibBuilder.loadTexts:
    protocolDistributionGroup.setStatus("current")

addressMapGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 20, 2, 3)
)
addressMapGroup.setObjects(
      *(("RMON2-MIB", "addressMapInserts"),
        ("RMON2-MIB", "addressMapDeletes"),
        ("RMON2-MIB", "addressMapMaxDesiredEntries"),
        ("RMON2-MIB", "addressMapControlDataSource"),
        ("RMON2-MIB", "addressMapControlDroppedFrames"),
        ("RMON2-MIB", "addressMapControlOwner"),
        ("RMON2-MIB", "addressMapControlStatus"),
        ("RMON2-MIB", "addressMapPhysicalAddress"),
        ("RMON2-MIB", "addressMapLastChange"))
)
if mibBuilder.loadTexts:
    addressMapGroup.setStatus("current")

nlHostGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 20, 2, 4)
)
nlHostGroup.setObjects(
      *(("RMON2-MIB", "hlHostControlDataSource"),
        ("RMON2-MIB", "hlHostControlNlDroppedFrames"),
        ("RMON2-MIB", "hlHostControlNlInserts"),
        ("RMON2-MIB", "hlHostControlNlDeletes"),
        ("RMON2-MIB", "hlHostControlNlMaxDesiredEntries"),
        ("RMON2-MIB", "hlHostControlAlDroppedFrames"),
        ("RMON2-MIB", "hlHostControlAlInserts"),
        ("RMON2-MIB", "hlHostControlAlDeletes"),
        ("RMON2-MIB", "hlHostControlAlMaxDesiredEntries"),
        ("RMON2-MIB", "hlHostControlOwner"),
        ("RMON2-MIB", "hlHostControlStatus"),
        ("RMON2-MIB", "nlHostInPkts"),
        ("RMON2-MIB", "nlHostOutPkts"),
        ("RMON2-MIB", "nlHostInOctets"),
        ("RMON2-MIB", "nlHostOutOctets"),
        ("RMON2-MIB", "nlHostOutMacNonUnicastPkts"),
        ("RMON2-MIB", "nlHostCreateTime"))
)
if mibBuilder.loadTexts:
    nlHostGroup.setStatus("current")

nlMatrixGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 20, 2, 5)
)
nlMatrixGroup.setObjects(
      *(("RMON2-MIB", "hlMatrixControlDataSource"),
        ("RMON2-MIB", "hlMatrixControlNlDroppedFrames"),
        ("RMON2-MIB", "hlMatrixControlNlInserts"),
        ("RMON2-MIB", "hlMatrixControlNlDeletes"),
        ("RMON2-MIB", "hlMatrixControlNlMaxDesiredEntries"),
        ("RMON2-MIB", "hlMatrixControlAlDroppedFrames"),
        ("RMON2-MIB", "hlMatrixControlAlInserts"),
        ("RMON2-MIB", "hlMatrixControlAlDeletes"),
        ("RMON2-MIB", "hlMatrixControlAlMaxDesiredEntries"),
        ("RMON2-MIB", "hlMatrixControlOwner"),
        ("RMON2-MIB", "hlMatrixControlStatus"),
        ("RMON2-MIB", "nlMatrixSDPkts"),
        ("RMON2-MIB", "nlMatrixSDOctets"),
        ("RMON2-MIB", "nlMatrixSDCreateTime"),
        ("RMON2-MIB", "nlMatrixDSPkts"),
        ("RMON2-MIB", "nlMatrixDSOctets"),
        ("RMON2-MIB", "nlMatrixDSCreateTime"),
        ("RMON2-MIB", "nlMatrixTopNControlMatrixIndex"),
        ("RMON2-MIB", "nlMatrixTopNControlRateBase"),
        ("RMON2-MIB", "nlMatrixTopNControlTimeRemaining"),
        ("RMON2-MIB", "nlMatrixTopNControlGeneratedReports"),
        ("RMON2-MIB", "nlMatrixTopNControlDuration"),
        ("RMON2-MIB", "nlMatrixTopNControlRequestedSize"),
        ("RMON2-MIB", "nlMatrixTopNControlGrantedSize"),
        ("RMON2-MIB", "nlMatrixTopNControlStartTime"),
        ("RMON2-MIB", "nlMatrixTopNControlOwner"),
        ("RMON2-MIB", "nlMatrixTopNControlStatus"),
        ("RMON2-MIB", "nlMatrixTopNProtocolDirLocalIndex"),
        ("RMON2-MIB", "nlMatrixTopNSourceAddress"),
        ("RMON2-MIB", "nlMatrixTopNDestAddress"),
        ("RMON2-MIB", "nlMatrixTopNPktRate"),
        ("RMON2-MIB", "nlMatrixTopNReversePktRate"),
        ("RMON2-MIB", "nlMatrixTopNOctetRate"),
        ("RMON2-MIB", "nlMatrixTopNReverseOctetRate"))
)
if mibBuilder.loadTexts:
    nlMatrixGroup.setStatus("current")

alHostGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 20, 2, 6)
)
alHostGroup.setObjects(
      *(("RMON2-MIB", "alHostInPkts"),
        ("RMON2-MIB", "alHostOutPkts"),
        ("RMON2-MIB", "alHostInOctets"),
        ("RMON2-MIB", "alHostOutOctets"),
        ("RMON2-MIB", "alHostCreateTime"))
)
if mibBuilder.loadTexts:
    alHostGroup.setStatus("current")

alMatrixGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 20, 2, 7)
)
alMatrixGroup.setObjects(
      *(("RMON2-MIB", "alMatrixSDPkts"),
        ("RMON2-MIB", "alMatrixSDOctets"),
        ("RMON2-MIB", "alMatrixSDCreateTime"),
        ("RMON2-MIB", "alMatrixDSPkts"),
        ("RMON2-MIB", "alMatrixDSOctets"),
        ("RMON2-MIB", "alMatrixDSCreateTime"),
        ("RMON2-MIB", "alMatrixTopNControlMatrixIndex"),
        ("RMON2-MIB", "alMatrixTopNControlRateBase"),
        ("RMON2-MIB", "alMatrixTopNControlTimeRemaining"),
        ("RMON2-MIB", "alMatrixTopNControlGeneratedReports"),
        ("RMON2-MIB", "alMatrixTopNControlDuration"),
        ("RMON2-MIB", "alMatrixTopNControlRequestedSize"),
        ("RMON2-MIB", "alMatrixTopNControlGrantedSize"),
        ("RMON2-MIB", "alMatrixTopNControlStartTime"),
        ("RMON2-MIB", "alMatrixTopNControlOwner"),
        ("RMON2-MIB", "alMatrixTopNControlStatus"),
        ("RMON2-MIB", "alMatrixTopNProtocolDirLocalIndex"),
        ("RMON2-MIB", "alMatrixTopNSourceAddress"),
        ("RMON2-MIB", "alMatrixTopNDestAddress"),
        ("RMON2-MIB", "alMatrixTopNAppProtocolDirLocalIndex"),
        ("RMON2-MIB", "alMatrixTopNPktRate"),
        ("RMON2-MIB", "alMatrixTopNReversePktRate"),
        ("RMON2-MIB", "alMatrixTopNOctetRate"),
        ("RMON2-MIB", "alMatrixTopNReverseOctetRate"))
)
if mibBuilder.loadTexts:
    alMatrixGroup.setStatus("current")

usrHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 20, 2, 8)
)
usrHistoryGroup.setObjects(
      *(("RMON2-MIB", "usrHistoryControlObjects"),
        ("RMON2-MIB", "usrHistoryControlBucketsRequested"),
        ("RMON2-MIB", "usrHistoryControlBucketsGranted"),
        ("RMON2-MIB", "usrHistoryControlInterval"),
        ("RMON2-MIB", "usrHistoryControlOwner"),
        ("RMON2-MIB", "usrHistoryControlStatus"),
        ("RMON2-MIB", "usrHistoryObjectVariable"),
        ("RMON2-MIB", "usrHistoryObjectSampleType"),
        ("RMON2-MIB", "usrHistoryIntervalStart"),
        ("RMON2-MIB", "usrHistoryIntervalEnd"),
        ("RMON2-MIB", "usrHistoryAbsValue"),
        ("RMON2-MIB", "usrHistoryValStatus"))
)
if mibBuilder.loadTexts:
    usrHistoryGroup.setStatus("current")

probeInformationGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 20, 2, 9)
)
probeInformationGroup.setObjects(
      *(("RMON2-MIB", "probeCapabilities"),
        ("RMON2-MIB", "probeSoftwareRev"),
        ("RMON2-MIB", "probeHardwareRev"),
        ("RMON2-MIB", "probeDateTime"))
)
if mibBuilder.loadTexts:
    probeInformationGroup.setStatus("current")

probeConfigurationGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 20, 2, 10)
)
probeConfigurationGroup.setObjects(
      *(("RMON2-MIB", "probeResetControl"),
        ("RMON2-MIB", "probeDownloadFile"),
        ("RMON2-MIB", "probeDownloadTFTPServer"),
        ("RMON2-MIB", "probeDownloadAction"),
        ("RMON2-MIB", "probeDownloadStatus"),
        ("RMON2-MIB", "serialMode"),
        ("RMON2-MIB", "serialProtocol"),
        ("RMON2-MIB", "serialTimeout"),
        ("RMON2-MIB", "serialModemInitString"),
        ("RMON2-MIB", "serialModemHangUpString"),
        ("RMON2-MIB", "serialModemConnectResp"),
        ("RMON2-MIB", "serialModemNoConnectResp"),
        ("RMON2-MIB", "serialDialoutTimeout"),
        ("RMON2-MIB", "serialStatus"),
        ("RMON2-MIB", "netConfigIPAddress"),
        ("RMON2-MIB", "netConfigSubnetMask"),
        ("RMON2-MIB", "netConfigStatus"),
        ("RMON2-MIB", "netDefaultGateway"),
        ("RMON2-MIB", "trapDestCommunity"),
        ("RMON2-MIB", "trapDestProtocol"),
        ("RMON2-MIB", "trapDestAddress"),
        ("RMON2-MIB", "trapDestOwner"),
        ("RMON2-MIB", "trapDestStatus"),
        ("RMON2-MIB", "serialConnectDestIpAddress"),
        ("RMON2-MIB", "serialConnectType"),
        ("RMON2-MIB", "serialConnectDialString"),
        ("RMON2-MIB", "serialConnectSwitchConnectSeq"),
        ("RMON2-MIB", "serialConnectSwitchDisconnectSeq"),
        ("RMON2-MIB", "serialConnectSwitchResetSeq"),
        ("RMON2-MIB", "serialConnectOwner"),
        ("RMON2-MIB", "serialConnectStatus"))
)
if mibBuilder.loadTexts:
    probeConfigurationGroup.setStatus("deprecated")

rmon1EnhancementGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 20, 2, 11)
)
rmon1EnhancementGroup.setObjects(
      *(("RMON2-MIB", "historyControlDroppedFrames"),
        ("RMON2-MIB", "hostControlDroppedFrames"),
        ("RMON2-MIB", "hostControlCreateTime"),
        ("RMON2-MIB", "matrixControlDroppedFrames"),
        ("RMON2-MIB", "matrixControlCreateTime"),
        ("RMON2-MIB", "channelDroppedFrames"),
        ("RMON2-MIB", "channelCreateTime"),
        ("RMON2-MIB", "filterProtocolDirDataLocalIndex"),
        ("RMON2-MIB", "filterProtocolDirLocalIndex"))
)
if mibBuilder.loadTexts:
    rmon1EnhancementGroup.setStatus("current")

rmon1EthernetEnhancementGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 20, 2, 12)
)
rmon1EthernetEnhancementGroup.setObjects(
      *(("RMON2-MIB", "etherStatsDroppedFrames"),
        ("RMON2-MIB", "etherStatsCreateTime"))
)
if mibBuilder.loadTexts:
    rmon1EthernetEnhancementGroup.setStatus("current")

rmon1TokenRingEnhancementGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 20, 2, 13)
)
rmon1TokenRingEnhancementGroup.setObjects(
      *(("RMON2-MIB", "tokenRingMLStatsDroppedFrames"),
        ("RMON2-MIB", "tokenRingMLStatsCreateTime"),
        ("RMON2-MIB", "tokenRingPStatsDroppedFrames"),
        ("RMON2-MIB", "tokenRingPStatsCreateTime"),
        ("RMON2-MIB", "ringStationControlDroppedFrames"),
        ("RMON2-MIB", "ringStationControlCreateTime"),
        ("RMON2-MIB", "sourceRoutingStatsDroppedFrames"),
        ("RMON2-MIB", "sourceRoutingStatsCreateTime"))
)
if mibBuilder.loadTexts:
    rmon1TokenRingEnhancementGroup.setStatus("deprecated")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rmon2MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 16, 20, 1, 1)
)
rmon2MIBCompliance.setObjects(
      *(("RMON2-MIB", "protocolDirectoryGroup"),
        ("RMON2-MIB", "protocolDistributionGroup"),
        ("RMON2-MIB", "addressMapGroup"),
        ("RMON2-MIB", "nlHostGroup"),
        ("RMON2-MIB", "nlMatrixGroup"),
        ("RMON2-MIB", "usrHistoryGroup"),
        ("RMON2-MIB", "probeInformationGroup"))
)
if mibBuilder.loadTexts:
    rmon2MIBCompliance.setStatus(
        "current"
    )

rmon2MIBApplicationLayerCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 16, 20, 1, 2)
)
rmon2MIBApplicationLayerCompliance.setObjects(
      *(("RMON2-MIB", "protocolDirectoryGroup"),
        ("RMON2-MIB", "protocolDistributionGroup"),
        ("RMON2-MIB", "addressMapGroup"),
        ("RMON2-MIB", "nlHostGroup"),
        ("RMON2-MIB", "nlMatrixGroup"),
        ("RMON2-MIB", "alHostGroup"),
        ("RMON2-MIB", "alMatrixGroup"),
        ("RMON2-MIB", "usrHistoryGroup"),
        ("RMON2-MIB", "probeInformationGroup"))
)
if mibBuilder.loadTexts:
    rmon2MIBApplicationLayerCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RMON2-MIB",
    **{"ZeroBasedCounter32": ZeroBasedCounter32,
       "LastCreateTime": LastCreateTime,
       "TimeFilter": TimeFilter,
       "DataSource": DataSource,
       "ControlString": ControlString,
       "rmon": rmon,
       "etherStats2Table": etherStats2Table,
       "etherStats2Entry": etherStats2Entry,
       "etherStatsDroppedFrames": etherStatsDroppedFrames,
       "etherStatsCreateTime": etherStatsCreateTime,
       "tokenRingMLStats2Table": tokenRingMLStats2Table,
       "tokenRingMLStats2Entry": tokenRingMLStats2Entry,
       "tokenRingMLStatsDroppedFrames": tokenRingMLStatsDroppedFrames,
       "tokenRingMLStatsCreateTime": tokenRingMLStatsCreateTime,
       "tokenRingPStats2Table": tokenRingPStats2Table,
       "tokenRingPStats2Entry": tokenRingPStats2Entry,
       "tokenRingPStatsDroppedFrames": tokenRingPStatsDroppedFrames,
       "tokenRingPStatsCreateTime": tokenRingPStatsCreateTime,
       "historyControl2Table": historyControl2Table,
       "historyControl2Entry": historyControl2Entry,
       "historyControlDroppedFrames": historyControlDroppedFrames,
       "hostControl2Table": hostControl2Table,
       "hostControl2Entry": hostControl2Entry,
       "hostControlDroppedFrames": hostControlDroppedFrames,
       "hostControlCreateTime": hostControlCreateTime,
       "matrixControl2Table": matrixControl2Table,
       "matrixControl2Entry": matrixControl2Entry,
       "matrixControlDroppedFrames": matrixControlDroppedFrames,
       "matrixControlCreateTime": matrixControlCreateTime,
       "channel2Table": channel2Table,
       "channel2Entry": channel2Entry,
       "channelDroppedFrames": channelDroppedFrames,
       "channelCreateTime": channelCreateTime,
       "filter2Table": filter2Table,
       "filter2Entry": filter2Entry,
       "filterProtocolDirDataLocalIndex": filterProtocolDirDataLocalIndex,
       "filterProtocolDirLocalIndex": filterProtocolDirLocalIndex,
       "ringStationControl2Table": ringStationControl2Table,
       "ringStationControl2Entry": ringStationControl2Entry,
       "ringStationControlDroppedFrames": ringStationControlDroppedFrames,
       "ringStationControlCreateTime": ringStationControlCreateTime,
       "sourceRoutingStats2Table": sourceRoutingStats2Table,
       "sourceRoutingStats2Entry": sourceRoutingStats2Entry,
       "sourceRoutingStatsDroppedFrames": sourceRoutingStatsDroppedFrames,
       "sourceRoutingStatsCreateTime": sourceRoutingStatsCreateTime,
       "protocolDir": protocolDir,
       "protocolDirLastChange": protocolDirLastChange,
       "protocolDirTable": protocolDirTable,
       "protocolDirEntry": protocolDirEntry,
       "protocolDirID": protocolDirID,
       "protocolDirParameters": protocolDirParameters,
       "protocolDirLocalIndex": protocolDirLocalIndex,
       "protocolDirDescr": protocolDirDescr,
       "protocolDirType": protocolDirType,
       "protocolDirAddressMapConfig": protocolDirAddressMapConfig,
       "protocolDirHostConfig": protocolDirHostConfig,
       "protocolDirMatrixConfig": protocolDirMatrixConfig,
       "protocolDirOwner": protocolDirOwner,
       "protocolDirStatus": protocolDirStatus,
       "protocolDist": protocolDist,
       "protocolDistControlTable": protocolDistControlTable,
       "protocolDistControlEntry": protocolDistControlEntry,
       "protocolDistControlIndex": protocolDistControlIndex,
       "protocolDistControlDataSource": protocolDistControlDataSource,
       "protocolDistControlDroppedFrames": protocolDistControlDroppedFrames,
       "protocolDistControlCreateTime": protocolDistControlCreateTime,
       "protocolDistControlOwner": protocolDistControlOwner,
       "protocolDistControlStatus": protocolDistControlStatus,
       "protocolDistStatsTable": protocolDistStatsTable,
       "protocolDistStatsEntry": protocolDistStatsEntry,
       "protocolDistStatsPkts": protocolDistStatsPkts,
       "protocolDistStatsOctets": protocolDistStatsOctets,
       "addressMap": addressMap,
       "addressMapInserts": addressMapInserts,
       "addressMapDeletes": addressMapDeletes,
       "addressMapMaxDesiredEntries": addressMapMaxDesiredEntries,
       "addressMapControlTable": addressMapControlTable,
       "addressMapControlEntry": addressMapControlEntry,
       "addressMapControlIndex": addressMapControlIndex,
       "addressMapControlDataSource": addressMapControlDataSource,
       "addressMapControlDroppedFrames": addressMapControlDroppedFrames,
       "addressMapControlOwner": addressMapControlOwner,
       "addressMapControlStatus": addressMapControlStatus,
       "addressMapTable": addressMapTable,
       "addressMapEntry": addressMapEntry,
       "addressMapTimeMark": addressMapTimeMark,
       "addressMapNetworkAddress": addressMapNetworkAddress,
       "addressMapSource": addressMapSource,
       "addressMapPhysicalAddress": addressMapPhysicalAddress,
       "addressMapLastChange": addressMapLastChange,
       "nlHost": nlHost,
       "hlHostControlTable": hlHostControlTable,
       "hlHostControlEntry": hlHostControlEntry,
       "hlHostControlIndex": hlHostControlIndex,
       "hlHostControlDataSource": hlHostControlDataSource,
       "hlHostControlNlDroppedFrames": hlHostControlNlDroppedFrames,
       "hlHostControlNlInserts": hlHostControlNlInserts,
       "hlHostControlNlDeletes": hlHostControlNlDeletes,
       "hlHostControlNlMaxDesiredEntries": hlHostControlNlMaxDesiredEntries,
       "hlHostControlAlDroppedFrames": hlHostControlAlDroppedFrames,
       "hlHostControlAlInserts": hlHostControlAlInserts,
       "hlHostControlAlDeletes": hlHostControlAlDeletes,
       "hlHostControlAlMaxDesiredEntries": hlHostControlAlMaxDesiredEntries,
       "hlHostControlOwner": hlHostControlOwner,
       "hlHostControlStatus": hlHostControlStatus,
       "nlHostTable": nlHostTable,
       "nlHostEntry": nlHostEntry,
       "nlHostTimeMark": nlHostTimeMark,
       "nlHostAddress": nlHostAddress,
       "nlHostInPkts": nlHostInPkts,
       "nlHostOutPkts": nlHostOutPkts,
       "nlHostInOctets": nlHostInOctets,
       "nlHostOutOctets": nlHostOutOctets,
       "nlHostOutMacNonUnicastPkts": nlHostOutMacNonUnicastPkts,
       "nlHostCreateTime": nlHostCreateTime,
       "nlMatrix": nlMatrix,
       "hlMatrixControlTable": hlMatrixControlTable,
       "hlMatrixControlEntry": hlMatrixControlEntry,
       "hlMatrixControlIndex": hlMatrixControlIndex,
       "hlMatrixControlDataSource": hlMatrixControlDataSource,
       "hlMatrixControlNlDroppedFrames": hlMatrixControlNlDroppedFrames,
       "hlMatrixControlNlInserts": hlMatrixControlNlInserts,
       "hlMatrixControlNlDeletes": hlMatrixControlNlDeletes,
       "hlMatrixControlNlMaxDesiredEntries": hlMatrixControlNlMaxDesiredEntries,
       "hlMatrixControlAlDroppedFrames": hlMatrixControlAlDroppedFrames,
       "hlMatrixControlAlInserts": hlMatrixControlAlInserts,
       "hlMatrixControlAlDeletes": hlMatrixControlAlDeletes,
       "hlMatrixControlAlMaxDesiredEntries": hlMatrixControlAlMaxDesiredEntries,
       "hlMatrixControlOwner": hlMatrixControlOwner,
       "hlMatrixControlStatus": hlMatrixControlStatus,
       "nlMatrixSDTable": nlMatrixSDTable,
       "nlMatrixSDEntry": nlMatrixSDEntry,
       "nlMatrixSDTimeMark": nlMatrixSDTimeMark,
       "nlMatrixSDSourceAddress": nlMatrixSDSourceAddress,
       "nlMatrixSDDestAddress": nlMatrixSDDestAddress,
       "nlMatrixSDPkts": nlMatrixSDPkts,
       "nlMatrixSDOctets": nlMatrixSDOctets,
       "nlMatrixSDCreateTime": nlMatrixSDCreateTime,
       "nlMatrixDSTable": nlMatrixDSTable,
       "nlMatrixDSEntry": nlMatrixDSEntry,
       "nlMatrixDSTimeMark": nlMatrixDSTimeMark,
       "nlMatrixDSSourceAddress": nlMatrixDSSourceAddress,
       "nlMatrixDSDestAddress": nlMatrixDSDestAddress,
       "nlMatrixDSPkts": nlMatrixDSPkts,
       "nlMatrixDSOctets": nlMatrixDSOctets,
       "nlMatrixDSCreateTime": nlMatrixDSCreateTime,
       "nlMatrixTopNControlTable": nlMatrixTopNControlTable,
       "nlMatrixTopNControlEntry": nlMatrixTopNControlEntry,
       "nlMatrixTopNControlIndex": nlMatrixTopNControlIndex,
       "nlMatrixTopNControlMatrixIndex": nlMatrixTopNControlMatrixIndex,
       "nlMatrixTopNControlRateBase": nlMatrixTopNControlRateBase,
       "nlMatrixTopNControlTimeRemaining": nlMatrixTopNControlTimeRemaining,
       "nlMatrixTopNControlGeneratedReports": nlMatrixTopNControlGeneratedReports,
       "nlMatrixTopNControlDuration": nlMatrixTopNControlDuration,
       "nlMatrixTopNControlRequestedSize": nlMatrixTopNControlRequestedSize,
       "nlMatrixTopNControlGrantedSize": nlMatrixTopNControlGrantedSize,
       "nlMatrixTopNControlStartTime": nlMatrixTopNControlStartTime,
       "nlMatrixTopNControlOwner": nlMatrixTopNControlOwner,
       "nlMatrixTopNControlStatus": nlMatrixTopNControlStatus,
       "nlMatrixTopNTable": nlMatrixTopNTable,
       "nlMatrixTopNEntry": nlMatrixTopNEntry,
       "nlMatrixTopNIndex": nlMatrixTopNIndex,
       "nlMatrixTopNProtocolDirLocalIndex": nlMatrixTopNProtocolDirLocalIndex,
       "nlMatrixTopNSourceAddress": nlMatrixTopNSourceAddress,
       "nlMatrixTopNDestAddress": nlMatrixTopNDestAddress,
       "nlMatrixTopNPktRate": nlMatrixTopNPktRate,
       "nlMatrixTopNReversePktRate": nlMatrixTopNReversePktRate,
       "nlMatrixTopNOctetRate": nlMatrixTopNOctetRate,
       "nlMatrixTopNReverseOctetRate": nlMatrixTopNReverseOctetRate,
       "alHost": alHost,
       "alHostTable": alHostTable,
       "alHostEntry": alHostEntry,
       "alHostTimeMark": alHostTimeMark,
       "alHostInPkts": alHostInPkts,
       "alHostOutPkts": alHostOutPkts,
       "alHostInOctets": alHostInOctets,
       "alHostOutOctets": alHostOutOctets,
       "alHostCreateTime": alHostCreateTime,
       "alMatrix": alMatrix,
       "alMatrixSDTable": alMatrixSDTable,
       "alMatrixSDEntry": alMatrixSDEntry,
       "alMatrixSDTimeMark": alMatrixSDTimeMark,
       "alMatrixSDPkts": alMatrixSDPkts,
       "alMatrixSDOctets": alMatrixSDOctets,
       "alMatrixSDCreateTime": alMatrixSDCreateTime,
       "alMatrixDSTable": alMatrixDSTable,
       "alMatrixDSEntry": alMatrixDSEntry,
       "alMatrixDSTimeMark": alMatrixDSTimeMark,
       "alMatrixDSPkts": alMatrixDSPkts,
       "alMatrixDSOctets": alMatrixDSOctets,
       "alMatrixDSCreateTime": alMatrixDSCreateTime,
       "alMatrixTopNControlTable": alMatrixTopNControlTable,
       "alMatrixTopNControlEntry": alMatrixTopNControlEntry,
       "alMatrixTopNControlIndex": alMatrixTopNControlIndex,
       "alMatrixTopNControlMatrixIndex": alMatrixTopNControlMatrixIndex,
       "alMatrixTopNControlRateBase": alMatrixTopNControlRateBase,
       "alMatrixTopNControlTimeRemaining": alMatrixTopNControlTimeRemaining,
       "alMatrixTopNControlGeneratedReports": alMatrixTopNControlGeneratedReports,
       "alMatrixTopNControlDuration": alMatrixTopNControlDuration,
       "alMatrixTopNControlRequestedSize": alMatrixTopNControlRequestedSize,
       "alMatrixTopNControlGrantedSize": alMatrixTopNControlGrantedSize,
       "alMatrixTopNControlStartTime": alMatrixTopNControlStartTime,
       "alMatrixTopNControlOwner": alMatrixTopNControlOwner,
       "alMatrixTopNControlStatus": alMatrixTopNControlStatus,
       "alMatrixTopNTable": alMatrixTopNTable,
       "alMatrixTopNEntry": alMatrixTopNEntry,
       "alMatrixTopNIndex": alMatrixTopNIndex,
       "alMatrixTopNProtocolDirLocalIndex": alMatrixTopNProtocolDirLocalIndex,
       "alMatrixTopNSourceAddress": alMatrixTopNSourceAddress,
       "alMatrixTopNDestAddress": alMatrixTopNDestAddress,
       "alMatrixTopNAppProtocolDirLocalIndex": alMatrixTopNAppProtocolDirLocalIndex,
       "alMatrixTopNPktRate": alMatrixTopNPktRate,
       "alMatrixTopNReversePktRate": alMatrixTopNReversePktRate,
       "alMatrixTopNOctetRate": alMatrixTopNOctetRate,
       "alMatrixTopNReverseOctetRate": alMatrixTopNReverseOctetRate,
       "usrHistory": usrHistory,
       "usrHistoryControlTable": usrHistoryControlTable,
       "usrHistoryControlEntry": usrHistoryControlEntry,
       "usrHistoryControlIndex": usrHistoryControlIndex,
       "usrHistoryControlObjects": usrHistoryControlObjects,
       "usrHistoryControlBucketsRequested": usrHistoryControlBucketsRequested,
       "usrHistoryControlBucketsGranted": usrHistoryControlBucketsGranted,
       "usrHistoryControlInterval": usrHistoryControlInterval,
       "usrHistoryControlOwner": usrHistoryControlOwner,
       "usrHistoryControlStatus": usrHistoryControlStatus,
       "usrHistoryObjectTable": usrHistoryObjectTable,
       "usrHistoryObjectEntry": usrHistoryObjectEntry,
       "usrHistoryObjectIndex": usrHistoryObjectIndex,
       "usrHistoryObjectVariable": usrHistoryObjectVariable,
       "usrHistoryObjectSampleType": usrHistoryObjectSampleType,
       "usrHistoryTable": usrHistoryTable,
       "usrHistoryEntry": usrHistoryEntry,
       "usrHistorySampleIndex": usrHistorySampleIndex,
       "usrHistoryIntervalStart": usrHistoryIntervalStart,
       "usrHistoryIntervalEnd": usrHistoryIntervalEnd,
       "usrHistoryAbsValue": usrHistoryAbsValue,
       "usrHistoryValStatus": usrHistoryValStatus,
       "probeConfig": probeConfig,
       "probeCapabilities": probeCapabilities,
       "probeSoftwareRev": probeSoftwareRev,
       "probeHardwareRev": probeHardwareRev,
       "probeDateTime": probeDateTime,
       "probeResetControl": probeResetControl,
       "probeDownloadFile": probeDownloadFile,
       "probeDownloadTFTPServer": probeDownloadTFTPServer,
       "probeDownloadAction": probeDownloadAction,
       "probeDownloadStatus": probeDownloadStatus,
       "serialConfigTable": serialConfigTable,
       "serialConfigEntry": serialConfigEntry,
       "serialMode": serialMode,
       "serialProtocol": serialProtocol,
       "serialTimeout": serialTimeout,
       "serialModemInitString": serialModemInitString,
       "serialModemHangUpString": serialModemHangUpString,
       "serialModemConnectResp": serialModemConnectResp,
       "serialModemNoConnectResp": serialModemNoConnectResp,
       "serialDialoutTimeout": serialDialoutTimeout,
       "serialStatus": serialStatus,
       "netConfigTable": netConfigTable,
       "netConfigEntry": netConfigEntry,
       "netConfigIPAddress": netConfigIPAddress,
       "netConfigSubnetMask": netConfigSubnetMask,
       "netConfigStatus": netConfigStatus,
       "netDefaultGateway": netDefaultGateway,
       "trapDestTable": trapDestTable,
       "trapDestEntry": trapDestEntry,
       "trapDestIndex": trapDestIndex,
       "trapDestCommunity": trapDestCommunity,
       "trapDestProtocol": trapDestProtocol,
       "trapDestAddress": trapDestAddress,
       "trapDestOwner": trapDestOwner,
       "trapDestStatus": trapDestStatus,
       "serialConnectionTable": serialConnectionTable,
       "serialConnectionEntry": serialConnectionEntry,
       "serialConnectIndex": serialConnectIndex,
       "serialConnectDestIpAddress": serialConnectDestIpAddress,
       "serialConnectType": serialConnectType,
       "serialConnectDialString": serialConnectDialString,
       "serialConnectSwitchConnectSeq": serialConnectSwitchConnectSeq,
       "serialConnectSwitchDisconnectSeq": serialConnectSwitchDisconnectSeq,
       "serialConnectSwitchResetSeq": serialConnectSwitchResetSeq,
       "serialConnectOwner": serialConnectOwner,
       "serialConnectStatus": serialConnectStatus,
       "rmonConformance": rmonConformance,
       "rmon2MIBCompliances": rmon2MIBCompliances,
       "rmon2MIBCompliance": rmon2MIBCompliance,
       "rmon2MIBApplicationLayerCompliance": rmon2MIBApplicationLayerCompliance,
       "rmon2MIBGroups": rmon2MIBGroups,
       "protocolDirectoryGroup": protocolDirectoryGroup,
       "protocolDistributionGroup": protocolDistributionGroup,
       "addressMapGroup": addressMapGroup,
       "nlHostGroup": nlHostGroup,
       "nlMatrixGroup": nlMatrixGroup,
       "alHostGroup": alHostGroup,
       "alMatrixGroup": alMatrixGroup,
       "usrHistoryGroup": usrHistoryGroup,
       "probeInformationGroup": probeInformationGroup,
       "probeConfigurationGroup": probeConfigurationGroup,
       "rmon1EnhancementGroup": rmon1EnhancementGroup,
       "rmon1EthernetEnhancementGroup": rmon1EthernetEnhancementGroup,
       "rmon1TokenRingEnhancementGroup": rmon1TokenRingEnhancementGroup}
)
