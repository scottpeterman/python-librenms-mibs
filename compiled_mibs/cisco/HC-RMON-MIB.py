# SNMP MIB module (HC-RMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\HC-RMON-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:25:35 2025
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

(CounterBasedGauge64,
 ZeroBasedCounter64) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64",
    "ZeroBasedCounter64")

(OwnerString,
 capture,
 captureBufferControlIndex,
 captureBufferIndex,
 etherHistoryIndex,
 etherHistorySampleIndex,
 etherStatsIndex,
 history,
 hostAddress,
 hostIndex,
 hostTimeCreationOrder,
 hostTimeIndex,
 hostTopN,
 hostTopNIndex,
 hostTopNReport,
 hosts,
 matrix,
 matrixDSDestAddress,
 matrixDSIndex,
 matrixDSSourceAddress,
 matrixSDDestAddress,
 matrixSDIndex,
 matrixSDSourceAddress,
 rmon,
 statistics) = mibBuilder.importSymbols(
    "RMON-MIB",
    "OwnerString",
    "capture",
    "captureBufferControlIndex",
    "captureBufferIndex",
    "etherHistoryIndex",
    "etherHistorySampleIndex",
    "etherStatsIndex",
    "history",
    "hostAddress",
    "hostIndex",
    "hostTimeCreationOrder",
    "hostTimeIndex",
    "hostTopN",
    "hostTopNIndex",
    "hostTopNReport",
    "hosts",
    "matrix",
    "matrixDSDestAddress",
    "matrixDSIndex",
    "matrixDSSourceAddress",
    "matrixSDDestAddress",
    "matrixSDIndex",
    "matrixSDSourceAddress",
    "rmon",
    "statistics")

(ZeroBasedCounter32,
 alHost,
 alHostTimeMark,
 alMatrix,
 alMatrixDSTimeMark,
 alMatrixSDTimeMark,
 alMatrixTopNControlIndex,
 alMatrixTopNIndex,
 hlHostControlIndex,
 hlMatrixControlIndex,
 nlHost,
 nlHostAddress,
 nlHostTimeMark,
 nlMatrix,
 nlMatrixDSDestAddress,
 nlMatrixDSSourceAddress,
 nlMatrixDSTimeMark,
 nlMatrixSDDestAddress,
 nlMatrixSDSourceAddress,
 nlMatrixSDTimeMark,
 nlMatrixTopNControlIndex,
 nlMatrixTopNIndex,
 probeConfig,
 protocolDirLocalIndex,
 protocolDist,
 protocolDistControlIndex,
 rmonConformance,
 usrHistory,
 usrHistoryControlIndex,
 usrHistoryObjectIndex,
 usrHistorySampleIndex) = mibBuilder.importSymbols(
    "RMON2-MIB",
    "ZeroBasedCounter32",
    "alHost",
    "alHostTimeMark",
    "alMatrix",
    "alMatrixDSTimeMark",
    "alMatrixSDTimeMark",
    "alMatrixTopNControlIndex",
    "alMatrixTopNIndex",
    "hlHostControlIndex",
    "hlMatrixControlIndex",
    "nlHost",
    "nlHostAddress",
    "nlHostTimeMark",
    "nlMatrix",
    "nlMatrixDSDestAddress",
    "nlMatrixDSSourceAddress",
    "nlMatrixDSTimeMark",
    "nlMatrixSDDestAddress",
    "nlMatrixSDSourceAddress",
    "nlMatrixSDTimeMark",
    "nlMatrixTopNControlIndex",
    "nlMatrixTopNIndex",
    "probeConfig",
    "protocolDirLocalIndex",
    "protocolDist",
    "protocolDistControlIndex",
    "rmonConformance",
    "usrHistory",
    "usrHistoryControlIndex",
    "usrHistoryObjectIndex",
    "usrHistorySampleIndex")

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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

hcRMON = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 16, 20, 5)
)
if mibBuilder.loadTexts:
    hcRMON.setRevisions(
        ("2002-05-08 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtherStatsHighCapacityTable_Object = MibTable
etherStatsHighCapacityTable = _EtherStatsHighCapacityTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 7)
)
if mibBuilder.loadTexts:
    etherStatsHighCapacityTable.setStatus("current")
_EtherStatsHighCapacityEntry_Object = MibTableRow
etherStatsHighCapacityEntry = _EtherStatsHighCapacityEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 7, 1)
)
etherStatsHighCapacityEntry.setIndexNames(
    (0, "RMON-MIB", "etherStatsIndex"),
)
if mibBuilder.loadTexts:
    etherStatsHighCapacityEntry.setStatus("current")
_EtherStatsHighCapacityOverflowPkts_Type = Counter32
_EtherStatsHighCapacityOverflowPkts_Object = MibTableColumn
etherStatsHighCapacityOverflowPkts = _EtherStatsHighCapacityOverflowPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 7, 1, 1),
    _EtherStatsHighCapacityOverflowPkts_Type()
)
etherStatsHighCapacityOverflowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsHighCapacityOverflowPkts.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsHighCapacityOverflowPkts.setUnits("Packets")
_EtherStatsHighCapacityPkts_Type = Counter64
_EtherStatsHighCapacityPkts_Object = MibTableColumn
etherStatsHighCapacityPkts = _EtherStatsHighCapacityPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 7, 1, 2),
    _EtherStatsHighCapacityPkts_Type()
)
etherStatsHighCapacityPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsHighCapacityPkts.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsHighCapacityPkts.setUnits("Packets")
_EtherStatsHighCapacityOverflowOctets_Type = Counter32
_EtherStatsHighCapacityOverflowOctets_Object = MibTableColumn
etherStatsHighCapacityOverflowOctets = _EtherStatsHighCapacityOverflowOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 7, 1, 3),
    _EtherStatsHighCapacityOverflowOctets_Type()
)
etherStatsHighCapacityOverflowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsHighCapacityOverflowOctets.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsHighCapacityOverflowOctets.setUnits("Octets")
_EtherStatsHighCapacityOctets_Type = Counter64
_EtherStatsHighCapacityOctets_Object = MibTableColumn
etherStatsHighCapacityOctets = _EtherStatsHighCapacityOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 7, 1, 4),
    _EtherStatsHighCapacityOctets_Type()
)
etherStatsHighCapacityOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsHighCapacityOctets.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsHighCapacityOctets.setUnits("Octets")
_EtherStatsHighCapacityOverflowPkts64Octets_Type = Counter32
_EtherStatsHighCapacityOverflowPkts64Octets_Object = MibTableColumn
etherStatsHighCapacityOverflowPkts64Octets = _EtherStatsHighCapacityOverflowPkts64Octets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 7, 1, 5),
    _EtherStatsHighCapacityOverflowPkts64Octets_Type()
)
etherStatsHighCapacityOverflowPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsHighCapacityOverflowPkts64Octets.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsHighCapacityOverflowPkts64Octets.setUnits("Packets")
_EtherStatsHighCapacityPkts64Octets_Type = Counter64
_EtherStatsHighCapacityPkts64Octets_Object = MibTableColumn
etherStatsHighCapacityPkts64Octets = _EtherStatsHighCapacityPkts64Octets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 7, 1, 6),
    _EtherStatsHighCapacityPkts64Octets_Type()
)
etherStatsHighCapacityPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsHighCapacityPkts64Octets.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsHighCapacityPkts64Octets.setUnits("Packets")
_EtherStatsHighCapacityOverflowPkts65to127Octets_Type = Counter32
_EtherStatsHighCapacityOverflowPkts65to127Octets_Object = MibTableColumn
etherStatsHighCapacityOverflowPkts65to127Octets = _EtherStatsHighCapacityOverflowPkts65to127Octets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 7, 1, 7),
    _EtherStatsHighCapacityOverflowPkts65to127Octets_Type()
)
etherStatsHighCapacityOverflowPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsHighCapacityOverflowPkts65to127Octets.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsHighCapacityOverflowPkts65to127Octets.setUnits("Packets")
_EtherStatsHighCapacityPkts65to127Octets_Type = Counter64
_EtherStatsHighCapacityPkts65to127Octets_Object = MibTableColumn
etherStatsHighCapacityPkts65to127Octets = _EtherStatsHighCapacityPkts65to127Octets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 7, 1, 8),
    _EtherStatsHighCapacityPkts65to127Octets_Type()
)
etherStatsHighCapacityPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsHighCapacityPkts65to127Octets.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsHighCapacityPkts65to127Octets.setUnits("Packets")
_EtherStatsHighCapacityOverflowPkts128to255Octets_Type = Counter32
_EtherStatsHighCapacityOverflowPkts128to255Octets_Object = MibTableColumn
etherStatsHighCapacityOverflowPkts128to255Octets = _EtherStatsHighCapacityOverflowPkts128to255Octets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 7, 1, 9),
    _EtherStatsHighCapacityOverflowPkts128to255Octets_Type()
)
etherStatsHighCapacityOverflowPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsHighCapacityOverflowPkts128to255Octets.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsHighCapacityOverflowPkts128to255Octets.setUnits("Packets")
_EtherStatsHighCapacityPkts128to255Octets_Type = Counter64
_EtherStatsHighCapacityPkts128to255Octets_Object = MibTableColumn
etherStatsHighCapacityPkts128to255Octets = _EtherStatsHighCapacityPkts128to255Octets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 7, 1, 10),
    _EtherStatsHighCapacityPkts128to255Octets_Type()
)
etherStatsHighCapacityPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsHighCapacityPkts128to255Octets.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsHighCapacityPkts128to255Octets.setUnits("Packets")
_EtherStatsHighCapacityOverflowPkts256to511Octets_Type = Counter32
_EtherStatsHighCapacityOverflowPkts256to511Octets_Object = MibTableColumn
etherStatsHighCapacityOverflowPkts256to511Octets = _EtherStatsHighCapacityOverflowPkts256to511Octets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 7, 1, 11),
    _EtherStatsHighCapacityOverflowPkts256to511Octets_Type()
)
etherStatsHighCapacityOverflowPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsHighCapacityOverflowPkts256to511Octets.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsHighCapacityOverflowPkts256to511Octets.setUnits("Packets")
_EtherStatsHighCapacityPkts256to511Octets_Type = Counter64
_EtherStatsHighCapacityPkts256to511Octets_Object = MibTableColumn
etherStatsHighCapacityPkts256to511Octets = _EtherStatsHighCapacityPkts256to511Octets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 7, 1, 12),
    _EtherStatsHighCapacityPkts256to511Octets_Type()
)
etherStatsHighCapacityPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsHighCapacityPkts256to511Octets.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsHighCapacityPkts256to511Octets.setUnits("Packets")
_EtherStatsHighCapacityOverflowPkts512to1023Octets_Type = Counter32
_EtherStatsHighCapacityOverflowPkts512to1023Octets_Object = MibTableColumn
etherStatsHighCapacityOverflowPkts512to1023Octets = _EtherStatsHighCapacityOverflowPkts512to1023Octets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 7, 1, 13),
    _EtherStatsHighCapacityOverflowPkts512to1023Octets_Type()
)
etherStatsHighCapacityOverflowPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsHighCapacityOverflowPkts512to1023Octets.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsHighCapacityOverflowPkts512to1023Octets.setUnits("Packets")
_EtherStatsHighCapacityPkts512to1023Octets_Type = Counter64
_EtherStatsHighCapacityPkts512to1023Octets_Object = MibTableColumn
etherStatsHighCapacityPkts512to1023Octets = _EtherStatsHighCapacityPkts512to1023Octets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 7, 1, 14),
    _EtherStatsHighCapacityPkts512to1023Octets_Type()
)
etherStatsHighCapacityPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsHighCapacityPkts512to1023Octets.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsHighCapacityPkts512to1023Octets.setUnits("Packets")
_EtherStatsHighCapacityOverflowPkts1024to1518Octets_Type = Counter32
_EtherStatsHighCapacityOverflowPkts1024to1518Octets_Object = MibTableColumn
etherStatsHighCapacityOverflowPkts1024to1518Octets = _EtherStatsHighCapacityOverflowPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 7, 1, 15),
    _EtherStatsHighCapacityOverflowPkts1024to1518Octets_Type()
)
etherStatsHighCapacityOverflowPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsHighCapacityOverflowPkts1024to1518Octets.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsHighCapacityOverflowPkts1024to1518Octets.setUnits("Packets")
_EtherStatsHighCapacityPkts1024to1518Octets_Type = Counter64
_EtherStatsHighCapacityPkts1024to1518Octets_Object = MibTableColumn
etherStatsHighCapacityPkts1024to1518Octets = _EtherStatsHighCapacityPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 7, 1, 16),
    _EtherStatsHighCapacityPkts1024to1518Octets_Type()
)
etherStatsHighCapacityPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsHighCapacityPkts1024to1518Octets.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsHighCapacityPkts1024to1518Octets.setUnits("Packets")
_EtherHistoryHighCapacityTable_Object = MibTable
etherHistoryHighCapacityTable = _EtherHistoryHighCapacityTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 6)
)
if mibBuilder.loadTexts:
    etherHistoryHighCapacityTable.setStatus("current")
_EtherHistoryHighCapacityEntry_Object = MibTableRow
etherHistoryHighCapacityEntry = _EtherHistoryHighCapacityEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 6, 1)
)
etherHistoryHighCapacityEntry.setIndexNames(
    (0, "RMON-MIB", "etherHistoryIndex"),
    (0, "RMON-MIB", "etherHistorySampleIndex"),
)
if mibBuilder.loadTexts:
    etherHistoryHighCapacityEntry.setStatus("current")
_EtherHistoryHighCapacityOverflowPkts_Type = Gauge32
_EtherHistoryHighCapacityOverflowPkts_Object = MibTableColumn
etherHistoryHighCapacityOverflowPkts = _EtherHistoryHighCapacityOverflowPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 6, 1, 1),
    _EtherHistoryHighCapacityOverflowPkts_Type()
)
etherHistoryHighCapacityOverflowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherHistoryHighCapacityOverflowPkts.setStatus("current")
if mibBuilder.loadTexts:
    etherHistoryHighCapacityOverflowPkts.setUnits("Packets")
_EtherHistoryHighCapacityPkts_Type = CounterBasedGauge64
_EtherHistoryHighCapacityPkts_Object = MibTableColumn
etherHistoryHighCapacityPkts = _EtherHistoryHighCapacityPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 6, 1, 2),
    _EtherHistoryHighCapacityPkts_Type()
)
etherHistoryHighCapacityPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherHistoryHighCapacityPkts.setStatus("current")
if mibBuilder.loadTexts:
    etherHistoryHighCapacityPkts.setUnits("Packets")
_EtherHistoryHighCapacityOverflowOctets_Type = Gauge32
_EtherHistoryHighCapacityOverflowOctets_Object = MibTableColumn
etherHistoryHighCapacityOverflowOctets = _EtherHistoryHighCapacityOverflowOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 6, 1, 3),
    _EtherHistoryHighCapacityOverflowOctets_Type()
)
etherHistoryHighCapacityOverflowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherHistoryHighCapacityOverflowOctets.setStatus("current")
if mibBuilder.loadTexts:
    etherHistoryHighCapacityOverflowOctets.setUnits("Octets")
_EtherHistoryHighCapacityOctets_Type = CounterBasedGauge64
_EtherHistoryHighCapacityOctets_Object = MibTableColumn
etherHistoryHighCapacityOctets = _EtherHistoryHighCapacityOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 6, 1, 4),
    _EtherHistoryHighCapacityOctets_Type()
)
etherHistoryHighCapacityOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherHistoryHighCapacityOctets.setStatus("current")
if mibBuilder.loadTexts:
    etherHistoryHighCapacityOctets.setUnits("Octets")
_HostHighCapacityTable_Object = MibTable
hostHighCapacityTable = _HostHighCapacityTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 5)
)
if mibBuilder.loadTexts:
    hostHighCapacityTable.setStatus("current")
_HostHighCapacityEntry_Object = MibTableRow
hostHighCapacityEntry = _HostHighCapacityEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 5, 1)
)
hostHighCapacityEntry.setIndexNames(
    (0, "RMON-MIB", "hostIndex"),
    (0, "RMON-MIB", "hostAddress"),
)
if mibBuilder.loadTexts:
    hostHighCapacityEntry.setStatus("current")
_HostHighCapacityInOverflowPkts_Type = Counter32
_HostHighCapacityInOverflowPkts_Object = MibTableColumn
hostHighCapacityInOverflowPkts = _HostHighCapacityInOverflowPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 5, 1, 1),
    _HostHighCapacityInOverflowPkts_Type()
)
hostHighCapacityInOverflowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostHighCapacityInOverflowPkts.setStatus("current")
if mibBuilder.loadTexts:
    hostHighCapacityInOverflowPkts.setUnits("Packets")
_HostHighCapacityInPkts_Type = Counter64
_HostHighCapacityInPkts_Object = MibTableColumn
hostHighCapacityInPkts = _HostHighCapacityInPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 5, 1, 2),
    _HostHighCapacityInPkts_Type()
)
hostHighCapacityInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostHighCapacityInPkts.setStatus("current")
if mibBuilder.loadTexts:
    hostHighCapacityInPkts.setUnits("Packets")
_HostHighCapacityOutOverflowPkts_Type = Counter32
_HostHighCapacityOutOverflowPkts_Object = MibTableColumn
hostHighCapacityOutOverflowPkts = _HostHighCapacityOutOverflowPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 5, 1, 3),
    _HostHighCapacityOutOverflowPkts_Type()
)
hostHighCapacityOutOverflowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostHighCapacityOutOverflowPkts.setStatus("current")
if mibBuilder.loadTexts:
    hostHighCapacityOutOverflowPkts.setUnits("Packets")
_HostHighCapacityOutPkts_Type = Counter64
_HostHighCapacityOutPkts_Object = MibTableColumn
hostHighCapacityOutPkts = _HostHighCapacityOutPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 5, 1, 4),
    _HostHighCapacityOutPkts_Type()
)
hostHighCapacityOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostHighCapacityOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    hostHighCapacityOutPkts.setUnits("Packets")
_HostHighCapacityInOverflowOctets_Type = Counter32
_HostHighCapacityInOverflowOctets_Object = MibTableColumn
hostHighCapacityInOverflowOctets = _HostHighCapacityInOverflowOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 5, 1, 5),
    _HostHighCapacityInOverflowOctets_Type()
)
hostHighCapacityInOverflowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostHighCapacityInOverflowOctets.setStatus("current")
if mibBuilder.loadTexts:
    hostHighCapacityInOverflowOctets.setUnits("Octets")
_HostHighCapacityInOctets_Type = Counter64
_HostHighCapacityInOctets_Object = MibTableColumn
hostHighCapacityInOctets = _HostHighCapacityInOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 5, 1, 6),
    _HostHighCapacityInOctets_Type()
)
hostHighCapacityInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostHighCapacityInOctets.setStatus("current")
if mibBuilder.loadTexts:
    hostHighCapacityInOctets.setUnits("Octets")
_HostHighCapacityOutOverflowOctets_Type = Counter32
_HostHighCapacityOutOverflowOctets_Object = MibTableColumn
hostHighCapacityOutOverflowOctets = _HostHighCapacityOutOverflowOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 5, 1, 7),
    _HostHighCapacityOutOverflowOctets_Type()
)
hostHighCapacityOutOverflowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostHighCapacityOutOverflowOctets.setStatus("current")
if mibBuilder.loadTexts:
    hostHighCapacityOutOverflowOctets.setUnits("Octets")
_HostHighCapacityOutOctets_Type = Counter64
_HostHighCapacityOutOctets_Object = MibTableColumn
hostHighCapacityOutOctets = _HostHighCapacityOutOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 5, 1, 8),
    _HostHighCapacityOutOctets_Type()
)
hostHighCapacityOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostHighCapacityOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    hostHighCapacityOutOctets.setUnits("Octets")
_HostTimeHighCapacityTable_Object = MibTable
hostTimeHighCapacityTable = _HostTimeHighCapacityTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 6)
)
if mibBuilder.loadTexts:
    hostTimeHighCapacityTable.setStatus("current")
_HostTimeHighCapacityEntry_Object = MibTableRow
hostTimeHighCapacityEntry = _HostTimeHighCapacityEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 6, 1)
)
hostTimeHighCapacityEntry.setIndexNames(
    (0, "RMON-MIB", "hostTimeIndex"),
    (0, "RMON-MIB", "hostTimeCreationOrder"),
)
if mibBuilder.loadTexts:
    hostTimeHighCapacityEntry.setStatus("current")
_HostTimeHighCapacityInOverflowPkts_Type = Counter32
_HostTimeHighCapacityInOverflowPkts_Object = MibTableColumn
hostTimeHighCapacityInOverflowPkts = _HostTimeHighCapacityInOverflowPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 6, 1, 1),
    _HostTimeHighCapacityInOverflowPkts_Type()
)
hostTimeHighCapacityInOverflowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTimeHighCapacityInOverflowPkts.setStatus("current")
if mibBuilder.loadTexts:
    hostTimeHighCapacityInOverflowPkts.setUnits("Packets")
_HostTimeHighCapacityInPkts_Type = Counter64
_HostTimeHighCapacityInPkts_Object = MibTableColumn
hostTimeHighCapacityInPkts = _HostTimeHighCapacityInPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 6, 1, 2),
    _HostTimeHighCapacityInPkts_Type()
)
hostTimeHighCapacityInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTimeHighCapacityInPkts.setStatus("current")
if mibBuilder.loadTexts:
    hostTimeHighCapacityInPkts.setUnits("Packets")
_HostTimeHighCapacityOutOverflowPkts_Type = Counter32
_HostTimeHighCapacityOutOverflowPkts_Object = MibTableColumn
hostTimeHighCapacityOutOverflowPkts = _HostTimeHighCapacityOutOverflowPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 6, 1, 3),
    _HostTimeHighCapacityOutOverflowPkts_Type()
)
hostTimeHighCapacityOutOverflowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTimeHighCapacityOutOverflowPkts.setStatus("current")
if mibBuilder.loadTexts:
    hostTimeHighCapacityOutOverflowPkts.setUnits("Packets")
_HostTimeHighCapacityOutPkts_Type = Counter64
_HostTimeHighCapacityOutPkts_Object = MibTableColumn
hostTimeHighCapacityOutPkts = _HostTimeHighCapacityOutPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 6, 1, 4),
    _HostTimeHighCapacityOutPkts_Type()
)
hostTimeHighCapacityOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTimeHighCapacityOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    hostTimeHighCapacityOutPkts.setUnits("Packets")
_HostTimeHighCapacityInOverflowOctets_Type = Counter32
_HostTimeHighCapacityInOverflowOctets_Object = MibTableColumn
hostTimeHighCapacityInOverflowOctets = _HostTimeHighCapacityInOverflowOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 6, 1, 5),
    _HostTimeHighCapacityInOverflowOctets_Type()
)
hostTimeHighCapacityInOverflowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTimeHighCapacityInOverflowOctets.setStatus("current")
if mibBuilder.loadTexts:
    hostTimeHighCapacityInOverflowOctets.setUnits("Octets")
_HostTimeHighCapacityInOctets_Type = Counter64
_HostTimeHighCapacityInOctets_Object = MibTableColumn
hostTimeHighCapacityInOctets = _HostTimeHighCapacityInOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 6, 1, 6),
    _HostTimeHighCapacityInOctets_Type()
)
hostTimeHighCapacityInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTimeHighCapacityInOctets.setStatus("current")
if mibBuilder.loadTexts:
    hostTimeHighCapacityInOctets.setUnits("Octets")
_HostTimeHighCapacityOutOverflowOctets_Type = Counter32
_HostTimeHighCapacityOutOverflowOctets_Object = MibTableColumn
hostTimeHighCapacityOutOverflowOctets = _HostTimeHighCapacityOutOverflowOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 6, 1, 7),
    _HostTimeHighCapacityOutOverflowOctets_Type()
)
hostTimeHighCapacityOutOverflowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTimeHighCapacityOutOverflowOctets.setStatus("current")
if mibBuilder.loadTexts:
    hostTimeHighCapacityOutOverflowOctets.setUnits("Octets")
_HostTimeHighCapacityOutOctets_Type = Counter64
_HostTimeHighCapacityOutOctets_Object = MibTableColumn
hostTimeHighCapacityOutOctets = _HostTimeHighCapacityOutOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 6, 1, 8),
    _HostTimeHighCapacityOutOctets_Type()
)
hostTimeHighCapacityOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTimeHighCapacityOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    hostTimeHighCapacityOutOctets.setUnits("Octets")
_HostTopNHighCapacityTable_Object = MibTable
hostTopNHighCapacityTable = _HostTopNHighCapacityTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 5, 3)
)
if mibBuilder.loadTexts:
    hostTopNHighCapacityTable.setStatus("current")
_HostTopNHighCapacityEntry_Object = MibTableRow
hostTopNHighCapacityEntry = _HostTopNHighCapacityEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 5, 3, 1)
)
hostTopNHighCapacityEntry.setIndexNames(
    (0, "RMON-MIB", "hostTopNReport"),
    (0, "RMON-MIB", "hostTopNIndex"),
)
if mibBuilder.loadTexts:
    hostTopNHighCapacityEntry.setStatus("current")
_HostTopNHighCapacityAddress_Type = OctetString
_HostTopNHighCapacityAddress_Object = MibTableColumn
hostTopNHighCapacityAddress = _HostTopNHighCapacityAddress_Object(
    (1, 3, 6, 1, 2, 1, 16, 5, 3, 1, 1),
    _HostTopNHighCapacityAddress_Type()
)
hostTopNHighCapacityAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTopNHighCapacityAddress.setStatus("current")
_HostTopNHighCapacityBaseRate_Type = Gauge32
_HostTopNHighCapacityBaseRate_Object = MibTableColumn
hostTopNHighCapacityBaseRate = _HostTopNHighCapacityBaseRate_Object(
    (1, 3, 6, 1, 2, 1, 16, 5, 3, 1, 2),
    _HostTopNHighCapacityBaseRate_Type()
)
hostTopNHighCapacityBaseRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTopNHighCapacityBaseRate.setStatus("current")
_HostTopNHighCapacityOverflowRate_Type = Gauge32
_HostTopNHighCapacityOverflowRate_Object = MibTableColumn
hostTopNHighCapacityOverflowRate = _HostTopNHighCapacityOverflowRate_Object(
    (1, 3, 6, 1, 2, 1, 16, 5, 3, 1, 3),
    _HostTopNHighCapacityOverflowRate_Type()
)
hostTopNHighCapacityOverflowRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTopNHighCapacityOverflowRate.setStatus("current")
_HostTopNHighCapacityRate_Type = CounterBasedGauge64
_HostTopNHighCapacityRate_Object = MibTableColumn
hostTopNHighCapacityRate = _HostTopNHighCapacityRate_Object(
    (1, 3, 6, 1, 2, 1, 16, 5, 3, 1, 4),
    _HostTopNHighCapacityRate_Type()
)
hostTopNHighCapacityRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTopNHighCapacityRate.setStatus("current")
_MatrixSDHighCapacityTable_Object = MibTable
matrixSDHighCapacityTable = _MatrixSDHighCapacityTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 6, 5)
)
if mibBuilder.loadTexts:
    matrixSDHighCapacityTable.setStatus("current")
_MatrixSDHighCapacityEntry_Object = MibTableRow
matrixSDHighCapacityEntry = _MatrixSDHighCapacityEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 6, 5, 1)
)
matrixSDHighCapacityEntry.setIndexNames(
    (0, "RMON-MIB", "matrixSDIndex"),
    (0, "RMON-MIB", "matrixSDSourceAddress"),
    (0, "RMON-MIB", "matrixSDDestAddress"),
)
if mibBuilder.loadTexts:
    matrixSDHighCapacityEntry.setStatus("current")
_MatrixSDHighCapacityOverflowPkts_Type = Counter32
_MatrixSDHighCapacityOverflowPkts_Object = MibTableColumn
matrixSDHighCapacityOverflowPkts = _MatrixSDHighCapacityOverflowPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 6, 5, 1, 1),
    _MatrixSDHighCapacityOverflowPkts_Type()
)
matrixSDHighCapacityOverflowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixSDHighCapacityOverflowPkts.setStatus("current")
if mibBuilder.loadTexts:
    matrixSDHighCapacityOverflowPkts.setUnits("Packets")
_MatrixSDHighCapacityPkts_Type = Counter64
_MatrixSDHighCapacityPkts_Object = MibTableColumn
matrixSDHighCapacityPkts = _MatrixSDHighCapacityPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 6, 5, 1, 2),
    _MatrixSDHighCapacityPkts_Type()
)
matrixSDHighCapacityPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixSDHighCapacityPkts.setStatus("current")
if mibBuilder.loadTexts:
    matrixSDHighCapacityPkts.setUnits("Packets")
_MatrixSDHighCapacityOverflowOctets_Type = Counter32
_MatrixSDHighCapacityOverflowOctets_Object = MibTableColumn
matrixSDHighCapacityOverflowOctets = _MatrixSDHighCapacityOverflowOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 6, 5, 1, 3),
    _MatrixSDHighCapacityOverflowOctets_Type()
)
matrixSDHighCapacityOverflowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixSDHighCapacityOverflowOctets.setStatus("current")
if mibBuilder.loadTexts:
    matrixSDHighCapacityOverflowOctets.setUnits("Octets")
_MatrixSDHighCapacityOctets_Type = Counter64
_MatrixSDHighCapacityOctets_Object = MibTableColumn
matrixSDHighCapacityOctets = _MatrixSDHighCapacityOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 6, 5, 1, 4),
    _MatrixSDHighCapacityOctets_Type()
)
matrixSDHighCapacityOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixSDHighCapacityOctets.setStatus("current")
if mibBuilder.loadTexts:
    matrixSDHighCapacityOctets.setUnits("Octets")
_MatrixDSHighCapacityTable_Object = MibTable
matrixDSHighCapacityTable = _MatrixDSHighCapacityTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 6, 6)
)
if mibBuilder.loadTexts:
    matrixDSHighCapacityTable.setStatus("current")
_MatrixDSHighCapacityEntry_Object = MibTableRow
matrixDSHighCapacityEntry = _MatrixDSHighCapacityEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 6, 6, 1)
)
matrixDSHighCapacityEntry.setIndexNames(
    (0, "RMON-MIB", "matrixDSIndex"),
    (0, "RMON-MIB", "matrixDSDestAddress"),
    (0, "RMON-MIB", "matrixDSSourceAddress"),
)
if mibBuilder.loadTexts:
    matrixDSHighCapacityEntry.setStatus("current")
_MatrixDSHighCapacityOverflowPkts_Type = Counter32
_MatrixDSHighCapacityOverflowPkts_Object = MibTableColumn
matrixDSHighCapacityOverflowPkts = _MatrixDSHighCapacityOverflowPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 6, 6, 1, 1),
    _MatrixDSHighCapacityOverflowPkts_Type()
)
matrixDSHighCapacityOverflowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixDSHighCapacityOverflowPkts.setStatus("current")
if mibBuilder.loadTexts:
    matrixDSHighCapacityOverflowPkts.setUnits("Packets")
_MatrixDSHighCapacityPkts_Type = Counter64
_MatrixDSHighCapacityPkts_Object = MibTableColumn
matrixDSHighCapacityPkts = _MatrixDSHighCapacityPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 6, 6, 1, 2),
    _MatrixDSHighCapacityPkts_Type()
)
matrixDSHighCapacityPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixDSHighCapacityPkts.setStatus("current")
if mibBuilder.loadTexts:
    matrixDSHighCapacityPkts.setUnits("Packets")
_MatrixDSHighCapacityOverflowOctets_Type = Counter32
_MatrixDSHighCapacityOverflowOctets_Object = MibTableColumn
matrixDSHighCapacityOverflowOctets = _MatrixDSHighCapacityOverflowOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 6, 6, 1, 3),
    _MatrixDSHighCapacityOverflowOctets_Type()
)
matrixDSHighCapacityOverflowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixDSHighCapacityOverflowOctets.setStatus("current")
if mibBuilder.loadTexts:
    matrixDSHighCapacityOverflowOctets.setUnits("Octets")
_MatrixDSHighCapacityOctets_Type = Counter64
_MatrixDSHighCapacityOctets_Object = MibTableColumn
matrixDSHighCapacityOctets = _MatrixDSHighCapacityOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 6, 6, 1, 4),
    _MatrixDSHighCapacityOctets_Type()
)
matrixDSHighCapacityOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixDSHighCapacityOctets.setStatus("current")
if mibBuilder.loadTexts:
    matrixDSHighCapacityOctets.setUnits("Octets")
_CaptureBufferHighCapacityTable_Object = MibTable
captureBufferHighCapacityTable = _CaptureBufferHighCapacityTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 8, 3)
)
if mibBuilder.loadTexts:
    captureBufferHighCapacityTable.setStatus("current")
_CaptureBufferHighCapacityEntry_Object = MibTableRow
captureBufferHighCapacityEntry = _CaptureBufferHighCapacityEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 8, 3, 1)
)
captureBufferHighCapacityEntry.setIndexNames(
    (0, "RMON-MIB", "captureBufferControlIndex"),
    (0, "RMON-MIB", "captureBufferIndex"),
)
if mibBuilder.loadTexts:
    captureBufferHighCapacityEntry.setStatus("current")


class _CaptureBufferPacketHighCapacityTime_Type(Integer32):
    """Custom type captureBufferPacketHighCapacityTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999),
    )


_CaptureBufferPacketHighCapacityTime_Type.__name__ = "Integer32"
_CaptureBufferPacketHighCapacityTime_Object = MibTableColumn
captureBufferPacketHighCapacityTime = _CaptureBufferPacketHighCapacityTime_Object(
    (1, 3, 6, 1, 2, 1, 16, 8, 3, 1, 1),
    _CaptureBufferPacketHighCapacityTime_Type()
)
captureBufferPacketHighCapacityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    captureBufferPacketHighCapacityTime.setStatus("current")
if mibBuilder.loadTexts:
    captureBufferPacketHighCapacityTime.setUnits("nanoseconds")
_ProtocolDistStatsHighCapacityTable_Object = MibTable
protocolDistStatsHighCapacityTable = _ProtocolDistStatsHighCapacityTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 12, 3)
)
if mibBuilder.loadTexts:
    protocolDistStatsHighCapacityTable.setStatus("current")
_ProtocolDistStatsHighCapacityEntry_Object = MibTableRow
protocolDistStatsHighCapacityEntry = _ProtocolDistStatsHighCapacityEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 12, 3, 1)
)
protocolDistStatsHighCapacityEntry.setIndexNames(
    (0, "RMON2-MIB", "protocolDistControlIndex"),
    (0, "RMON2-MIB", "protocolDirLocalIndex"),
)
if mibBuilder.loadTexts:
    protocolDistStatsHighCapacityEntry.setStatus("current")
_ProtocolDistStatsHighCapacityOverflowPkts_Type = ZeroBasedCounter32
_ProtocolDistStatsHighCapacityOverflowPkts_Object = MibTableColumn
protocolDistStatsHighCapacityOverflowPkts = _ProtocolDistStatsHighCapacityOverflowPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 12, 3, 1, 1),
    _ProtocolDistStatsHighCapacityOverflowPkts_Type()
)
protocolDistStatsHighCapacityOverflowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolDistStatsHighCapacityOverflowPkts.setStatus("current")
if mibBuilder.loadTexts:
    protocolDistStatsHighCapacityOverflowPkts.setUnits("Packets")
_ProtocolDistStatsHighCapacityPkts_Type = ZeroBasedCounter64
_ProtocolDistStatsHighCapacityPkts_Object = MibTableColumn
protocolDistStatsHighCapacityPkts = _ProtocolDistStatsHighCapacityPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 12, 3, 1, 2),
    _ProtocolDistStatsHighCapacityPkts_Type()
)
protocolDistStatsHighCapacityPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolDistStatsHighCapacityPkts.setStatus("current")
if mibBuilder.loadTexts:
    protocolDistStatsHighCapacityPkts.setUnits("Packets")
_ProtocolDistStatsHighCapacityOverflowOctets_Type = ZeroBasedCounter32
_ProtocolDistStatsHighCapacityOverflowOctets_Object = MibTableColumn
protocolDistStatsHighCapacityOverflowOctets = _ProtocolDistStatsHighCapacityOverflowOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 12, 3, 1, 3),
    _ProtocolDistStatsHighCapacityOverflowOctets_Type()
)
protocolDistStatsHighCapacityOverflowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolDistStatsHighCapacityOverflowOctets.setStatus("current")
if mibBuilder.loadTexts:
    protocolDistStatsHighCapacityOverflowOctets.setUnits("Octets")
_ProtocolDistStatsHighCapacityOctets_Type = ZeroBasedCounter64
_ProtocolDistStatsHighCapacityOctets_Object = MibTableColumn
protocolDistStatsHighCapacityOctets = _ProtocolDistStatsHighCapacityOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 12, 3, 1, 4),
    _ProtocolDistStatsHighCapacityOctets_Type()
)
protocolDistStatsHighCapacityOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolDistStatsHighCapacityOctets.setStatus("current")
if mibBuilder.loadTexts:
    protocolDistStatsHighCapacityOctets.setUnits("Octets")
_NlHostHighCapacityTable_Object = MibTable
nlHostHighCapacityTable = _NlHostHighCapacityTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 14, 3)
)
if mibBuilder.loadTexts:
    nlHostHighCapacityTable.setStatus("current")
_NlHostHighCapacityEntry_Object = MibTableRow
nlHostHighCapacityEntry = _NlHostHighCapacityEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 14, 3, 1)
)
nlHostHighCapacityEntry.setIndexNames(
    (0, "RMON2-MIB", "hlHostControlIndex"),
    (0, "RMON2-MIB", "nlHostTimeMark"),
    (0, "RMON2-MIB", "protocolDirLocalIndex"),
    (0, "RMON2-MIB", "nlHostAddress"),
)
if mibBuilder.loadTexts:
    nlHostHighCapacityEntry.setStatus("current")
_NlHostHighCapacityInOverflowPkts_Type = ZeroBasedCounter32
_NlHostHighCapacityInOverflowPkts_Object = MibTableColumn
nlHostHighCapacityInOverflowPkts = _NlHostHighCapacityInOverflowPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 14, 3, 1, 1),
    _NlHostHighCapacityInOverflowPkts_Type()
)
nlHostHighCapacityInOverflowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlHostHighCapacityInOverflowPkts.setStatus("current")
if mibBuilder.loadTexts:
    nlHostHighCapacityInOverflowPkts.setUnits("Packets")
_NlHostHighCapacityInPkts_Type = ZeroBasedCounter64
_NlHostHighCapacityInPkts_Object = MibTableColumn
nlHostHighCapacityInPkts = _NlHostHighCapacityInPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 14, 3, 1, 2),
    _NlHostHighCapacityInPkts_Type()
)
nlHostHighCapacityInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlHostHighCapacityInPkts.setStatus("current")
if mibBuilder.loadTexts:
    nlHostHighCapacityInPkts.setUnits("Packets")
_NlHostHighCapacityOutOverflowPkts_Type = ZeroBasedCounter32
_NlHostHighCapacityOutOverflowPkts_Object = MibTableColumn
nlHostHighCapacityOutOverflowPkts = _NlHostHighCapacityOutOverflowPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 14, 3, 1, 3),
    _NlHostHighCapacityOutOverflowPkts_Type()
)
nlHostHighCapacityOutOverflowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlHostHighCapacityOutOverflowPkts.setStatus("current")
if mibBuilder.loadTexts:
    nlHostHighCapacityOutOverflowPkts.setUnits("Packets")
_NlHostHighCapacityOutPkts_Type = ZeroBasedCounter64
_NlHostHighCapacityOutPkts_Object = MibTableColumn
nlHostHighCapacityOutPkts = _NlHostHighCapacityOutPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 14, 3, 1, 4),
    _NlHostHighCapacityOutPkts_Type()
)
nlHostHighCapacityOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlHostHighCapacityOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    nlHostHighCapacityOutPkts.setUnits("Packets")
_NlHostHighCapacityInOverflowOctets_Type = ZeroBasedCounter32
_NlHostHighCapacityInOverflowOctets_Object = MibTableColumn
nlHostHighCapacityInOverflowOctets = _NlHostHighCapacityInOverflowOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 14, 3, 1, 5),
    _NlHostHighCapacityInOverflowOctets_Type()
)
nlHostHighCapacityInOverflowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlHostHighCapacityInOverflowOctets.setStatus("current")
if mibBuilder.loadTexts:
    nlHostHighCapacityInOverflowOctets.setUnits("Octets")
_NlHostHighCapacityInOctets_Type = ZeroBasedCounter64
_NlHostHighCapacityInOctets_Object = MibTableColumn
nlHostHighCapacityInOctets = _NlHostHighCapacityInOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 14, 3, 1, 6),
    _NlHostHighCapacityInOctets_Type()
)
nlHostHighCapacityInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlHostHighCapacityInOctets.setStatus("current")
if mibBuilder.loadTexts:
    nlHostHighCapacityInOctets.setUnits("Octets")
_NlHostHighCapacityOutOverflowOctets_Type = ZeroBasedCounter32
_NlHostHighCapacityOutOverflowOctets_Object = MibTableColumn
nlHostHighCapacityOutOverflowOctets = _NlHostHighCapacityOutOverflowOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 14, 3, 1, 7),
    _NlHostHighCapacityOutOverflowOctets_Type()
)
nlHostHighCapacityOutOverflowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlHostHighCapacityOutOverflowOctets.setStatus("current")
if mibBuilder.loadTexts:
    nlHostHighCapacityOutOverflowOctets.setUnits("Octets")
_NlHostHighCapacityOutOctets_Type = ZeroBasedCounter64
_NlHostHighCapacityOutOctets_Object = MibTableColumn
nlHostHighCapacityOutOctets = _NlHostHighCapacityOutOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 14, 3, 1, 8),
    _NlHostHighCapacityOutOctets_Type()
)
nlHostHighCapacityOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlHostHighCapacityOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    nlHostHighCapacityOutOctets.setUnits("Octets")
_NlMatrixSDHighCapacityTable_Object = MibTable
nlMatrixSDHighCapacityTable = _NlMatrixSDHighCapacityTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 6)
)
if mibBuilder.loadTexts:
    nlMatrixSDHighCapacityTable.setStatus("current")
_NlMatrixSDHighCapacityEntry_Object = MibTableRow
nlMatrixSDHighCapacityEntry = _NlMatrixSDHighCapacityEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 6, 1)
)
nlMatrixSDHighCapacityEntry.setIndexNames(
    (0, "RMON2-MIB", "hlMatrixControlIndex"),
    (0, "RMON2-MIB", "nlMatrixSDTimeMark"),
    (0, "RMON2-MIB", "protocolDirLocalIndex"),
    (0, "RMON2-MIB", "nlMatrixSDSourceAddress"),
    (0, "RMON2-MIB", "nlMatrixSDDestAddress"),
)
if mibBuilder.loadTexts:
    nlMatrixSDHighCapacityEntry.setStatus("current")
_NlMatrixSDHighCapacityOverflowPkts_Type = ZeroBasedCounter32
_NlMatrixSDHighCapacityOverflowPkts_Object = MibTableColumn
nlMatrixSDHighCapacityOverflowPkts = _NlMatrixSDHighCapacityOverflowPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 6, 1, 1),
    _NlMatrixSDHighCapacityOverflowPkts_Type()
)
nlMatrixSDHighCapacityOverflowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlMatrixSDHighCapacityOverflowPkts.setStatus("current")
if mibBuilder.loadTexts:
    nlMatrixSDHighCapacityOverflowPkts.setUnits("Packets")
_NlMatrixSDHighCapacityPkts_Type = ZeroBasedCounter64
_NlMatrixSDHighCapacityPkts_Object = MibTableColumn
nlMatrixSDHighCapacityPkts = _NlMatrixSDHighCapacityPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 6, 1, 2),
    _NlMatrixSDHighCapacityPkts_Type()
)
nlMatrixSDHighCapacityPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlMatrixSDHighCapacityPkts.setStatus("current")
if mibBuilder.loadTexts:
    nlMatrixSDHighCapacityPkts.setUnits("Packets")
_NlMatrixSDHighCapacityOverflowOctets_Type = ZeroBasedCounter32
_NlMatrixSDHighCapacityOverflowOctets_Object = MibTableColumn
nlMatrixSDHighCapacityOverflowOctets = _NlMatrixSDHighCapacityOverflowOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 6, 1, 3),
    _NlMatrixSDHighCapacityOverflowOctets_Type()
)
nlMatrixSDHighCapacityOverflowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlMatrixSDHighCapacityOverflowOctets.setStatus("current")
if mibBuilder.loadTexts:
    nlMatrixSDHighCapacityOverflowOctets.setUnits("Octets")
_NlMatrixSDHighCapacityOctets_Type = ZeroBasedCounter64
_NlMatrixSDHighCapacityOctets_Object = MibTableColumn
nlMatrixSDHighCapacityOctets = _NlMatrixSDHighCapacityOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 6, 1, 4),
    _NlMatrixSDHighCapacityOctets_Type()
)
nlMatrixSDHighCapacityOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlMatrixSDHighCapacityOctets.setStatus("current")
if mibBuilder.loadTexts:
    nlMatrixSDHighCapacityOctets.setUnits("Octets")
_NlMatrixDSHighCapacityTable_Object = MibTable
nlMatrixDSHighCapacityTable = _NlMatrixDSHighCapacityTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 7)
)
if mibBuilder.loadTexts:
    nlMatrixDSHighCapacityTable.setStatus("current")
_NlMatrixDSHighCapacityEntry_Object = MibTableRow
nlMatrixDSHighCapacityEntry = _NlMatrixDSHighCapacityEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 7, 1)
)
nlMatrixDSHighCapacityEntry.setIndexNames(
    (0, "RMON2-MIB", "hlMatrixControlIndex"),
    (0, "RMON2-MIB", "nlMatrixDSTimeMark"),
    (0, "RMON2-MIB", "protocolDirLocalIndex"),
    (0, "RMON2-MIB", "nlMatrixDSDestAddress"),
    (0, "RMON2-MIB", "nlMatrixDSSourceAddress"),
)
if mibBuilder.loadTexts:
    nlMatrixDSHighCapacityEntry.setStatus("current")
_NlMatrixDSHighCapacityOverflowPkts_Type = ZeroBasedCounter32
_NlMatrixDSHighCapacityOverflowPkts_Object = MibTableColumn
nlMatrixDSHighCapacityOverflowPkts = _NlMatrixDSHighCapacityOverflowPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 7, 1, 1),
    _NlMatrixDSHighCapacityOverflowPkts_Type()
)
nlMatrixDSHighCapacityOverflowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlMatrixDSHighCapacityOverflowPkts.setStatus("current")
if mibBuilder.loadTexts:
    nlMatrixDSHighCapacityOverflowPkts.setUnits("Packets")
_NlMatrixDSHighCapacityPkts_Type = ZeroBasedCounter64
_NlMatrixDSHighCapacityPkts_Object = MibTableColumn
nlMatrixDSHighCapacityPkts = _NlMatrixDSHighCapacityPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 7, 1, 2),
    _NlMatrixDSHighCapacityPkts_Type()
)
nlMatrixDSHighCapacityPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlMatrixDSHighCapacityPkts.setStatus("current")
if mibBuilder.loadTexts:
    nlMatrixDSHighCapacityPkts.setUnits("Packets")
_NlMatrixDSHighCapacityOverflowOctets_Type = ZeroBasedCounter32
_NlMatrixDSHighCapacityOverflowOctets_Object = MibTableColumn
nlMatrixDSHighCapacityOverflowOctets = _NlMatrixDSHighCapacityOverflowOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 7, 1, 3),
    _NlMatrixDSHighCapacityOverflowOctets_Type()
)
nlMatrixDSHighCapacityOverflowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlMatrixDSHighCapacityOverflowOctets.setStatus("current")
if mibBuilder.loadTexts:
    nlMatrixDSHighCapacityOverflowOctets.setUnits("Octets")
_NlMatrixDSHighCapacityOctets_Type = ZeroBasedCounter64
_NlMatrixDSHighCapacityOctets_Object = MibTableColumn
nlMatrixDSHighCapacityOctets = _NlMatrixDSHighCapacityOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 7, 1, 4),
    _NlMatrixDSHighCapacityOctets_Type()
)
nlMatrixDSHighCapacityOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlMatrixDSHighCapacityOctets.setStatus("current")
if mibBuilder.loadTexts:
    nlMatrixDSHighCapacityOctets.setUnits("Octets")
_NlMatrixTopNHighCapacityTable_Object = MibTable
nlMatrixTopNHighCapacityTable = _NlMatrixTopNHighCapacityTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 8)
)
if mibBuilder.loadTexts:
    nlMatrixTopNHighCapacityTable.setStatus("current")
_NlMatrixTopNHighCapacityEntry_Object = MibTableRow
nlMatrixTopNHighCapacityEntry = _NlMatrixTopNHighCapacityEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 8, 1)
)
nlMatrixTopNHighCapacityEntry.setIndexNames(
    (0, "RMON2-MIB", "nlMatrixTopNControlIndex"),
    (0, "RMON2-MIB", "nlMatrixTopNIndex"),
)
if mibBuilder.loadTexts:
    nlMatrixTopNHighCapacityEntry.setStatus("current")


class _NlMatrixTopNHighCapacityProtocolDirLocalIndex_Type(Integer32):
    """Custom type nlMatrixTopNHighCapacityProtocolDirLocalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NlMatrixTopNHighCapacityProtocolDirLocalIndex_Type.__name__ = "Integer32"
_NlMatrixTopNHighCapacityProtocolDirLocalIndex_Object = MibTableColumn
nlMatrixTopNHighCapacityProtocolDirLocalIndex = _NlMatrixTopNHighCapacityProtocolDirLocalIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 8, 1, 1),
    _NlMatrixTopNHighCapacityProtocolDirLocalIndex_Type()
)
nlMatrixTopNHighCapacityProtocolDirLocalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlMatrixTopNHighCapacityProtocolDirLocalIndex.setStatus("current")
_NlMatrixTopNHighCapacitySourceAddress_Type = OctetString
_NlMatrixTopNHighCapacitySourceAddress_Object = MibTableColumn
nlMatrixTopNHighCapacitySourceAddress = _NlMatrixTopNHighCapacitySourceAddress_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 8, 1, 2),
    _NlMatrixTopNHighCapacitySourceAddress_Type()
)
nlMatrixTopNHighCapacitySourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlMatrixTopNHighCapacitySourceAddress.setStatus("current")
_NlMatrixTopNHighCapacityDestAddress_Type = OctetString
_NlMatrixTopNHighCapacityDestAddress_Object = MibTableColumn
nlMatrixTopNHighCapacityDestAddress = _NlMatrixTopNHighCapacityDestAddress_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 8, 1, 3),
    _NlMatrixTopNHighCapacityDestAddress_Type()
)
nlMatrixTopNHighCapacityDestAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlMatrixTopNHighCapacityDestAddress.setStatus("current")
_NlMatrixTopNHighCapacityBasePktRate_Type = Gauge32
_NlMatrixTopNHighCapacityBasePktRate_Object = MibTableColumn
nlMatrixTopNHighCapacityBasePktRate = _NlMatrixTopNHighCapacityBasePktRate_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 8, 1, 4),
    _NlMatrixTopNHighCapacityBasePktRate_Type()
)
nlMatrixTopNHighCapacityBasePktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlMatrixTopNHighCapacityBasePktRate.setStatus("current")
if mibBuilder.loadTexts:
    nlMatrixTopNHighCapacityBasePktRate.setUnits("Packets")
_NlMatrixTopNHighCapacityOverflowPktRate_Type = Gauge32
_NlMatrixTopNHighCapacityOverflowPktRate_Object = MibTableColumn
nlMatrixTopNHighCapacityOverflowPktRate = _NlMatrixTopNHighCapacityOverflowPktRate_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 8, 1, 5),
    _NlMatrixTopNHighCapacityOverflowPktRate_Type()
)
nlMatrixTopNHighCapacityOverflowPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlMatrixTopNHighCapacityOverflowPktRate.setStatus("current")
if mibBuilder.loadTexts:
    nlMatrixTopNHighCapacityOverflowPktRate.setUnits("Packets")
_NlMatrixTopNHighCapacityPktRate_Type = CounterBasedGauge64
_NlMatrixTopNHighCapacityPktRate_Object = MibTableColumn
nlMatrixTopNHighCapacityPktRate = _NlMatrixTopNHighCapacityPktRate_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 8, 1, 6),
    _NlMatrixTopNHighCapacityPktRate_Type()
)
nlMatrixTopNHighCapacityPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlMatrixTopNHighCapacityPktRate.setStatus("current")
if mibBuilder.loadTexts:
    nlMatrixTopNHighCapacityPktRate.setUnits("Packets")
_NlMatrixTopNHighCapacityReverseBasePktRate_Type = Gauge32
_NlMatrixTopNHighCapacityReverseBasePktRate_Object = MibTableColumn
nlMatrixTopNHighCapacityReverseBasePktRate = _NlMatrixTopNHighCapacityReverseBasePktRate_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 8, 1, 7),
    _NlMatrixTopNHighCapacityReverseBasePktRate_Type()
)
nlMatrixTopNHighCapacityReverseBasePktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlMatrixTopNHighCapacityReverseBasePktRate.setStatus("current")
if mibBuilder.loadTexts:
    nlMatrixTopNHighCapacityReverseBasePktRate.setUnits("Packets")
_NlMatrixTopNHighCapacityReverseOverflowPktRate_Type = Gauge32
_NlMatrixTopNHighCapacityReverseOverflowPktRate_Object = MibTableColumn
nlMatrixTopNHighCapacityReverseOverflowPktRate = _NlMatrixTopNHighCapacityReverseOverflowPktRate_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 8, 1, 8),
    _NlMatrixTopNHighCapacityReverseOverflowPktRate_Type()
)
nlMatrixTopNHighCapacityReverseOverflowPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlMatrixTopNHighCapacityReverseOverflowPktRate.setStatus("current")
if mibBuilder.loadTexts:
    nlMatrixTopNHighCapacityReverseOverflowPktRate.setUnits("Packets")
_NlMatrixTopNHighCapacityReversePktRate_Type = CounterBasedGauge64
_NlMatrixTopNHighCapacityReversePktRate_Object = MibTableColumn
nlMatrixTopNHighCapacityReversePktRate = _NlMatrixTopNHighCapacityReversePktRate_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 8, 1, 9),
    _NlMatrixTopNHighCapacityReversePktRate_Type()
)
nlMatrixTopNHighCapacityReversePktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlMatrixTopNHighCapacityReversePktRate.setStatus("current")
if mibBuilder.loadTexts:
    nlMatrixTopNHighCapacityReversePktRate.setUnits("Packets")
_NlMatrixTopNHighCapacityBaseOctetRate_Type = Gauge32
_NlMatrixTopNHighCapacityBaseOctetRate_Object = MibTableColumn
nlMatrixTopNHighCapacityBaseOctetRate = _NlMatrixTopNHighCapacityBaseOctetRate_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 8, 1, 10),
    _NlMatrixTopNHighCapacityBaseOctetRate_Type()
)
nlMatrixTopNHighCapacityBaseOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlMatrixTopNHighCapacityBaseOctetRate.setStatus("current")
if mibBuilder.loadTexts:
    nlMatrixTopNHighCapacityBaseOctetRate.setUnits("Octets")
_NlMatrixTopNHighCapacityOverflowOctetRate_Type = Gauge32
_NlMatrixTopNHighCapacityOverflowOctetRate_Object = MibTableColumn
nlMatrixTopNHighCapacityOverflowOctetRate = _NlMatrixTopNHighCapacityOverflowOctetRate_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 8, 1, 11),
    _NlMatrixTopNHighCapacityOverflowOctetRate_Type()
)
nlMatrixTopNHighCapacityOverflowOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlMatrixTopNHighCapacityOverflowOctetRate.setStatus("current")
if mibBuilder.loadTexts:
    nlMatrixTopNHighCapacityOverflowOctetRate.setUnits("Octets")
_NlMatrixTopNHighCapacityOctetRate_Type = CounterBasedGauge64
_NlMatrixTopNHighCapacityOctetRate_Object = MibTableColumn
nlMatrixTopNHighCapacityOctetRate = _NlMatrixTopNHighCapacityOctetRate_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 8, 1, 12),
    _NlMatrixTopNHighCapacityOctetRate_Type()
)
nlMatrixTopNHighCapacityOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlMatrixTopNHighCapacityOctetRate.setStatus("current")
if mibBuilder.loadTexts:
    nlMatrixTopNHighCapacityOctetRate.setUnits("Octets")
_NlMatrixTopNHighCapacityReverseBaseOctetRate_Type = Gauge32
_NlMatrixTopNHighCapacityReverseBaseOctetRate_Object = MibTableColumn
nlMatrixTopNHighCapacityReverseBaseOctetRate = _NlMatrixTopNHighCapacityReverseBaseOctetRate_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 8, 1, 13),
    _NlMatrixTopNHighCapacityReverseBaseOctetRate_Type()
)
nlMatrixTopNHighCapacityReverseBaseOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlMatrixTopNHighCapacityReverseBaseOctetRate.setStatus("current")
if mibBuilder.loadTexts:
    nlMatrixTopNHighCapacityReverseBaseOctetRate.setUnits("Octets")
_NlMatrixTopNHighCapacityReverseOverflowOctetRate_Type = Gauge32
_NlMatrixTopNHighCapacityReverseOverflowOctetRate_Object = MibTableColumn
nlMatrixTopNHighCapacityReverseOverflowOctetRate = _NlMatrixTopNHighCapacityReverseOverflowOctetRate_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 8, 1, 14),
    _NlMatrixTopNHighCapacityReverseOverflowOctetRate_Type()
)
nlMatrixTopNHighCapacityReverseOverflowOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlMatrixTopNHighCapacityReverseOverflowOctetRate.setStatus("current")
if mibBuilder.loadTexts:
    nlMatrixTopNHighCapacityReverseOverflowOctetRate.setUnits("Octets")
_NlMatrixTopNHighCapacityReverseOctetRate_Type = CounterBasedGauge64
_NlMatrixTopNHighCapacityReverseOctetRate_Object = MibTableColumn
nlMatrixTopNHighCapacityReverseOctetRate = _NlMatrixTopNHighCapacityReverseOctetRate_Object(
    (1, 3, 6, 1, 2, 1, 16, 15, 8, 1, 15),
    _NlMatrixTopNHighCapacityReverseOctetRate_Type()
)
nlMatrixTopNHighCapacityReverseOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlMatrixTopNHighCapacityReverseOctetRate.setStatus("current")
if mibBuilder.loadTexts:
    nlMatrixTopNHighCapacityReverseOctetRate.setUnits("Octets")
_AlHostHighCapacityTable_Object = MibTable
alHostHighCapacityTable = _AlHostHighCapacityTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 16, 2)
)
if mibBuilder.loadTexts:
    alHostHighCapacityTable.setStatus("current")
_AlHostHighCapacityEntry_Object = MibTableRow
alHostHighCapacityEntry = _AlHostHighCapacityEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 16, 2, 1)
)
alHostHighCapacityEntry.setIndexNames(
    (0, "RMON2-MIB", "hlHostControlIndex"),
    (0, "RMON2-MIB", "alHostTimeMark"),
    (0, "RMON2-MIB", "protocolDirLocalIndex"),
    (0, "RMON2-MIB", "nlHostAddress"),
    (0, "RMON2-MIB", "protocolDirLocalIndex"),
)
if mibBuilder.loadTexts:
    alHostHighCapacityEntry.setStatus("current")
_AlHostHighCapacityInOverflowPkts_Type = ZeroBasedCounter32
_AlHostHighCapacityInOverflowPkts_Object = MibTableColumn
alHostHighCapacityInOverflowPkts = _AlHostHighCapacityInOverflowPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 16, 2, 1, 1),
    _AlHostHighCapacityInOverflowPkts_Type()
)
alHostHighCapacityInOverflowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHostHighCapacityInOverflowPkts.setStatus("current")
if mibBuilder.loadTexts:
    alHostHighCapacityInOverflowPkts.setUnits("Packets")
_AlHostHighCapacityInPkts_Type = ZeroBasedCounter64
_AlHostHighCapacityInPkts_Object = MibTableColumn
alHostHighCapacityInPkts = _AlHostHighCapacityInPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 16, 2, 1, 2),
    _AlHostHighCapacityInPkts_Type()
)
alHostHighCapacityInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHostHighCapacityInPkts.setStatus("current")
if mibBuilder.loadTexts:
    alHostHighCapacityInPkts.setUnits("Packets")
_AlHostHighCapacityOutOverflowPkts_Type = ZeroBasedCounter32
_AlHostHighCapacityOutOverflowPkts_Object = MibTableColumn
alHostHighCapacityOutOverflowPkts = _AlHostHighCapacityOutOverflowPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 16, 2, 1, 3),
    _AlHostHighCapacityOutOverflowPkts_Type()
)
alHostHighCapacityOutOverflowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHostHighCapacityOutOverflowPkts.setStatus("current")
if mibBuilder.loadTexts:
    alHostHighCapacityOutOverflowPkts.setUnits("Packets")
_AlHostHighCapacityOutPkts_Type = ZeroBasedCounter64
_AlHostHighCapacityOutPkts_Object = MibTableColumn
alHostHighCapacityOutPkts = _AlHostHighCapacityOutPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 16, 2, 1, 4),
    _AlHostHighCapacityOutPkts_Type()
)
alHostHighCapacityOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHostHighCapacityOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    alHostHighCapacityOutPkts.setUnits("Packets")
_AlHostHighCapacityInOverflowOctets_Type = ZeroBasedCounter32
_AlHostHighCapacityInOverflowOctets_Object = MibTableColumn
alHostHighCapacityInOverflowOctets = _AlHostHighCapacityInOverflowOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 16, 2, 1, 5),
    _AlHostHighCapacityInOverflowOctets_Type()
)
alHostHighCapacityInOverflowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHostHighCapacityInOverflowOctets.setStatus("current")
if mibBuilder.loadTexts:
    alHostHighCapacityInOverflowOctets.setUnits("Octets")
_AlHostHighCapacityInOctets_Type = ZeroBasedCounter64
_AlHostHighCapacityInOctets_Object = MibTableColumn
alHostHighCapacityInOctets = _AlHostHighCapacityInOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 16, 2, 1, 6),
    _AlHostHighCapacityInOctets_Type()
)
alHostHighCapacityInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHostHighCapacityInOctets.setStatus("current")
if mibBuilder.loadTexts:
    alHostHighCapacityInOctets.setUnits("Octets")
_AlHostHighCapacityOutOverflowOctets_Type = ZeroBasedCounter32
_AlHostHighCapacityOutOverflowOctets_Object = MibTableColumn
alHostHighCapacityOutOverflowOctets = _AlHostHighCapacityOutOverflowOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 16, 2, 1, 7),
    _AlHostHighCapacityOutOverflowOctets_Type()
)
alHostHighCapacityOutOverflowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHostHighCapacityOutOverflowOctets.setStatus("current")
if mibBuilder.loadTexts:
    alHostHighCapacityOutOverflowOctets.setUnits("Octets")
_AlHostHighCapacityOutOctets_Type = ZeroBasedCounter64
_AlHostHighCapacityOutOctets_Object = MibTableColumn
alHostHighCapacityOutOctets = _AlHostHighCapacityOutOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 16, 2, 1, 8),
    _AlHostHighCapacityOutOctets_Type()
)
alHostHighCapacityOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alHostHighCapacityOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    alHostHighCapacityOutOctets.setUnits("Octets")
_AlMatrixSDHighCapacityTable_Object = MibTable
alMatrixSDHighCapacityTable = _AlMatrixSDHighCapacityTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 5)
)
if mibBuilder.loadTexts:
    alMatrixSDHighCapacityTable.setStatus("current")
_AlMatrixSDHighCapacityEntry_Object = MibTableRow
alMatrixSDHighCapacityEntry = _AlMatrixSDHighCapacityEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 5, 1)
)
alMatrixSDHighCapacityEntry.setIndexNames(
    (0, "RMON2-MIB", "hlMatrixControlIndex"),
    (0, "RMON2-MIB", "alMatrixSDTimeMark"),
    (0, "RMON2-MIB", "protocolDirLocalIndex"),
    (0, "RMON2-MIB", "nlMatrixSDSourceAddress"),
    (0, "RMON2-MIB", "nlMatrixSDDestAddress"),
    (0, "RMON2-MIB", "protocolDirLocalIndex"),
)
if mibBuilder.loadTexts:
    alMatrixSDHighCapacityEntry.setStatus("current")
_AlMatrixSDHighCapacityOverflowPkts_Type = ZeroBasedCounter32
_AlMatrixSDHighCapacityOverflowPkts_Object = MibTableColumn
alMatrixSDHighCapacityOverflowPkts = _AlMatrixSDHighCapacityOverflowPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 5, 1, 1),
    _AlMatrixSDHighCapacityOverflowPkts_Type()
)
alMatrixSDHighCapacityOverflowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMatrixSDHighCapacityOverflowPkts.setStatus("current")
if mibBuilder.loadTexts:
    alMatrixSDHighCapacityOverflowPkts.setUnits("Packets")
_AlMatrixSDHighCapacityPkts_Type = ZeroBasedCounter64
_AlMatrixSDHighCapacityPkts_Object = MibTableColumn
alMatrixSDHighCapacityPkts = _AlMatrixSDHighCapacityPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 5, 1, 2),
    _AlMatrixSDHighCapacityPkts_Type()
)
alMatrixSDHighCapacityPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMatrixSDHighCapacityPkts.setStatus("current")
if mibBuilder.loadTexts:
    alMatrixSDHighCapacityPkts.setUnits("Packets")
_AlMatrixSDHighCapacityOverflowOctets_Type = ZeroBasedCounter32
_AlMatrixSDHighCapacityOverflowOctets_Object = MibTableColumn
alMatrixSDHighCapacityOverflowOctets = _AlMatrixSDHighCapacityOverflowOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 5, 1, 3),
    _AlMatrixSDHighCapacityOverflowOctets_Type()
)
alMatrixSDHighCapacityOverflowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMatrixSDHighCapacityOverflowOctets.setStatus("current")
if mibBuilder.loadTexts:
    alMatrixSDHighCapacityOverflowOctets.setUnits("Octets")
_AlMatrixSDHighCapacityOctets_Type = ZeroBasedCounter64
_AlMatrixSDHighCapacityOctets_Object = MibTableColumn
alMatrixSDHighCapacityOctets = _AlMatrixSDHighCapacityOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 5, 1, 4),
    _AlMatrixSDHighCapacityOctets_Type()
)
alMatrixSDHighCapacityOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMatrixSDHighCapacityOctets.setStatus("current")
if mibBuilder.loadTexts:
    alMatrixSDHighCapacityOctets.setUnits("Octets")
_AlMatrixDSHighCapacityTable_Object = MibTable
alMatrixDSHighCapacityTable = _AlMatrixDSHighCapacityTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 6)
)
if mibBuilder.loadTexts:
    alMatrixDSHighCapacityTable.setStatus("current")
_AlMatrixDSHighCapacityEntry_Object = MibTableRow
alMatrixDSHighCapacityEntry = _AlMatrixDSHighCapacityEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 6, 1)
)
alMatrixDSHighCapacityEntry.setIndexNames(
    (0, "RMON2-MIB", "hlMatrixControlIndex"),
    (0, "RMON2-MIB", "alMatrixDSTimeMark"),
    (0, "RMON2-MIB", "protocolDirLocalIndex"),
    (0, "RMON2-MIB", "nlMatrixDSDestAddress"),
    (0, "RMON2-MIB", "nlMatrixDSSourceAddress"),
    (0, "RMON2-MIB", "protocolDirLocalIndex"),
)
if mibBuilder.loadTexts:
    alMatrixDSHighCapacityEntry.setStatus("current")
_AlMatrixDSHighCapacityOverflowPkts_Type = ZeroBasedCounter32
_AlMatrixDSHighCapacityOverflowPkts_Object = MibTableColumn
alMatrixDSHighCapacityOverflowPkts = _AlMatrixDSHighCapacityOverflowPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 6, 1, 1),
    _AlMatrixDSHighCapacityOverflowPkts_Type()
)
alMatrixDSHighCapacityOverflowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMatrixDSHighCapacityOverflowPkts.setStatus("current")
if mibBuilder.loadTexts:
    alMatrixDSHighCapacityOverflowPkts.setUnits("Packets")
_AlMatrixDSHighCapacityPkts_Type = ZeroBasedCounter64
_AlMatrixDSHighCapacityPkts_Object = MibTableColumn
alMatrixDSHighCapacityPkts = _AlMatrixDSHighCapacityPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 6, 1, 2),
    _AlMatrixDSHighCapacityPkts_Type()
)
alMatrixDSHighCapacityPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMatrixDSHighCapacityPkts.setStatus("current")
if mibBuilder.loadTexts:
    alMatrixDSHighCapacityPkts.setUnits("Packets")
_AlMatrixDSHighCapacityOverflowOctets_Type = ZeroBasedCounter32
_AlMatrixDSHighCapacityOverflowOctets_Object = MibTableColumn
alMatrixDSHighCapacityOverflowOctets = _AlMatrixDSHighCapacityOverflowOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 6, 1, 3),
    _AlMatrixDSHighCapacityOverflowOctets_Type()
)
alMatrixDSHighCapacityOverflowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMatrixDSHighCapacityOverflowOctets.setStatus("current")
if mibBuilder.loadTexts:
    alMatrixDSHighCapacityOverflowOctets.setUnits("Octets")
_AlMatrixDSHighCapacityOctets_Type = ZeroBasedCounter64
_AlMatrixDSHighCapacityOctets_Object = MibTableColumn
alMatrixDSHighCapacityOctets = _AlMatrixDSHighCapacityOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 6, 1, 4),
    _AlMatrixDSHighCapacityOctets_Type()
)
alMatrixDSHighCapacityOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMatrixDSHighCapacityOctets.setStatus("current")
if mibBuilder.loadTexts:
    alMatrixDSHighCapacityOctets.setUnits("Octets")
_AlMatrixTopNHighCapacityTable_Object = MibTable
alMatrixTopNHighCapacityTable = _AlMatrixTopNHighCapacityTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 7)
)
if mibBuilder.loadTexts:
    alMatrixTopNHighCapacityTable.setStatus("current")
_AlMatrixTopNHighCapacityEntry_Object = MibTableRow
alMatrixTopNHighCapacityEntry = _AlMatrixTopNHighCapacityEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 7, 1)
)
alMatrixTopNHighCapacityEntry.setIndexNames(
    (0, "RMON2-MIB", "alMatrixTopNControlIndex"),
    (0, "RMON2-MIB", "alMatrixTopNIndex"),
)
if mibBuilder.loadTexts:
    alMatrixTopNHighCapacityEntry.setStatus("current")


class _AlMatrixTopNHighCapacityProtocolDirLocalIndex_Type(Integer32):
    """Custom type alMatrixTopNHighCapacityProtocolDirLocalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AlMatrixTopNHighCapacityProtocolDirLocalIndex_Type.__name__ = "Integer32"
_AlMatrixTopNHighCapacityProtocolDirLocalIndex_Object = MibTableColumn
alMatrixTopNHighCapacityProtocolDirLocalIndex = _AlMatrixTopNHighCapacityProtocolDirLocalIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 7, 1, 1),
    _AlMatrixTopNHighCapacityProtocolDirLocalIndex_Type()
)
alMatrixTopNHighCapacityProtocolDirLocalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMatrixTopNHighCapacityProtocolDirLocalIndex.setStatus("current")
_AlMatrixTopNHighCapacitySourceAddress_Type = OctetString
_AlMatrixTopNHighCapacitySourceAddress_Object = MibTableColumn
alMatrixTopNHighCapacitySourceAddress = _AlMatrixTopNHighCapacitySourceAddress_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 7, 1, 2),
    _AlMatrixTopNHighCapacitySourceAddress_Type()
)
alMatrixTopNHighCapacitySourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMatrixTopNHighCapacitySourceAddress.setStatus("current")
_AlMatrixTopNHighCapacityDestAddress_Type = OctetString
_AlMatrixTopNHighCapacityDestAddress_Object = MibTableColumn
alMatrixTopNHighCapacityDestAddress = _AlMatrixTopNHighCapacityDestAddress_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 7, 1, 3),
    _AlMatrixTopNHighCapacityDestAddress_Type()
)
alMatrixTopNHighCapacityDestAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMatrixTopNHighCapacityDestAddress.setStatus("current")
_AlMatrixTopNHighCapacityAppProtocolDirLocalIndex_Type = Integer32
_AlMatrixTopNHighCapacityAppProtocolDirLocalIndex_Object = MibTableColumn
alMatrixTopNHighCapacityAppProtocolDirLocalIndex = _AlMatrixTopNHighCapacityAppProtocolDirLocalIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 7, 1, 4),
    _AlMatrixTopNHighCapacityAppProtocolDirLocalIndex_Type()
)
alMatrixTopNHighCapacityAppProtocolDirLocalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMatrixTopNHighCapacityAppProtocolDirLocalIndex.setStatus("current")
_AlMatrixTopNHighCapacityBasePktRate_Type = Gauge32
_AlMatrixTopNHighCapacityBasePktRate_Object = MibTableColumn
alMatrixTopNHighCapacityBasePktRate = _AlMatrixTopNHighCapacityBasePktRate_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 7, 1, 5),
    _AlMatrixTopNHighCapacityBasePktRate_Type()
)
alMatrixTopNHighCapacityBasePktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMatrixTopNHighCapacityBasePktRate.setStatus("current")
if mibBuilder.loadTexts:
    alMatrixTopNHighCapacityBasePktRate.setUnits("Packets")
_AlMatrixTopNHighCapacityOverflowPktRate_Type = Gauge32
_AlMatrixTopNHighCapacityOverflowPktRate_Object = MibTableColumn
alMatrixTopNHighCapacityOverflowPktRate = _AlMatrixTopNHighCapacityOverflowPktRate_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 7, 1, 6),
    _AlMatrixTopNHighCapacityOverflowPktRate_Type()
)
alMatrixTopNHighCapacityOverflowPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMatrixTopNHighCapacityOverflowPktRate.setStatus("current")
if mibBuilder.loadTexts:
    alMatrixTopNHighCapacityOverflowPktRate.setUnits("Packets")
_AlMatrixTopNHighCapacityPktRate_Type = CounterBasedGauge64
_AlMatrixTopNHighCapacityPktRate_Object = MibTableColumn
alMatrixTopNHighCapacityPktRate = _AlMatrixTopNHighCapacityPktRate_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 7, 1, 7),
    _AlMatrixTopNHighCapacityPktRate_Type()
)
alMatrixTopNHighCapacityPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMatrixTopNHighCapacityPktRate.setStatus("current")
if mibBuilder.loadTexts:
    alMatrixTopNHighCapacityPktRate.setUnits("Packets")
_AlMatrixTopNHighCapacityReverseBasePktRate_Type = Gauge32
_AlMatrixTopNHighCapacityReverseBasePktRate_Object = MibTableColumn
alMatrixTopNHighCapacityReverseBasePktRate = _AlMatrixTopNHighCapacityReverseBasePktRate_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 7, 1, 8),
    _AlMatrixTopNHighCapacityReverseBasePktRate_Type()
)
alMatrixTopNHighCapacityReverseBasePktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMatrixTopNHighCapacityReverseBasePktRate.setStatus("current")
if mibBuilder.loadTexts:
    alMatrixTopNHighCapacityReverseBasePktRate.setUnits("Packets")
_AlMatrixTopNHighCapacityReverseOverflowPktRate_Type = Gauge32
_AlMatrixTopNHighCapacityReverseOverflowPktRate_Object = MibTableColumn
alMatrixTopNHighCapacityReverseOverflowPktRate = _AlMatrixTopNHighCapacityReverseOverflowPktRate_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 7, 1, 9),
    _AlMatrixTopNHighCapacityReverseOverflowPktRate_Type()
)
alMatrixTopNHighCapacityReverseOverflowPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMatrixTopNHighCapacityReverseOverflowPktRate.setStatus("current")
if mibBuilder.loadTexts:
    alMatrixTopNHighCapacityReverseOverflowPktRate.setUnits("Packets")
_AlMatrixTopNHighCapacityReversePktRate_Type = CounterBasedGauge64
_AlMatrixTopNHighCapacityReversePktRate_Object = MibTableColumn
alMatrixTopNHighCapacityReversePktRate = _AlMatrixTopNHighCapacityReversePktRate_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 7, 1, 10),
    _AlMatrixTopNHighCapacityReversePktRate_Type()
)
alMatrixTopNHighCapacityReversePktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMatrixTopNHighCapacityReversePktRate.setStatus("current")
if mibBuilder.loadTexts:
    alMatrixTopNHighCapacityReversePktRate.setUnits("Packets")
_AlMatrixTopNHighCapacityBaseOctetRate_Type = Gauge32
_AlMatrixTopNHighCapacityBaseOctetRate_Object = MibTableColumn
alMatrixTopNHighCapacityBaseOctetRate = _AlMatrixTopNHighCapacityBaseOctetRate_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 7, 1, 11),
    _AlMatrixTopNHighCapacityBaseOctetRate_Type()
)
alMatrixTopNHighCapacityBaseOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMatrixTopNHighCapacityBaseOctetRate.setStatus("current")
if mibBuilder.loadTexts:
    alMatrixTopNHighCapacityBaseOctetRate.setUnits("Octets")
_AlMatrixTopNHighCapacityOverflowOctetRate_Type = Gauge32
_AlMatrixTopNHighCapacityOverflowOctetRate_Object = MibTableColumn
alMatrixTopNHighCapacityOverflowOctetRate = _AlMatrixTopNHighCapacityOverflowOctetRate_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 7, 1, 12),
    _AlMatrixTopNHighCapacityOverflowOctetRate_Type()
)
alMatrixTopNHighCapacityOverflowOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMatrixTopNHighCapacityOverflowOctetRate.setStatus("current")
if mibBuilder.loadTexts:
    alMatrixTopNHighCapacityOverflowOctetRate.setUnits("Octets")
_AlMatrixTopNHighCapacityOctetRate_Type = CounterBasedGauge64
_AlMatrixTopNHighCapacityOctetRate_Object = MibTableColumn
alMatrixTopNHighCapacityOctetRate = _AlMatrixTopNHighCapacityOctetRate_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 7, 1, 13),
    _AlMatrixTopNHighCapacityOctetRate_Type()
)
alMatrixTopNHighCapacityOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMatrixTopNHighCapacityOctetRate.setStatus("current")
if mibBuilder.loadTexts:
    alMatrixTopNHighCapacityOctetRate.setUnits("Octets")
_AlMatrixTopNHighCapacityReverseBaseOctetRate_Type = Gauge32
_AlMatrixTopNHighCapacityReverseBaseOctetRate_Object = MibTableColumn
alMatrixTopNHighCapacityReverseBaseOctetRate = _AlMatrixTopNHighCapacityReverseBaseOctetRate_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 7, 1, 14),
    _AlMatrixTopNHighCapacityReverseBaseOctetRate_Type()
)
alMatrixTopNHighCapacityReverseBaseOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMatrixTopNHighCapacityReverseBaseOctetRate.setStatus("current")
if mibBuilder.loadTexts:
    alMatrixTopNHighCapacityReverseBaseOctetRate.setUnits("Octets")
_AlMatrixTopNHighCapacityReverseOverflowOctetRate_Type = Gauge32
_AlMatrixTopNHighCapacityReverseOverflowOctetRate_Object = MibTableColumn
alMatrixTopNHighCapacityReverseOverflowOctetRate = _AlMatrixTopNHighCapacityReverseOverflowOctetRate_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 7, 1, 15),
    _AlMatrixTopNHighCapacityReverseOverflowOctetRate_Type()
)
alMatrixTopNHighCapacityReverseOverflowOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMatrixTopNHighCapacityReverseOverflowOctetRate.setStatus("current")
if mibBuilder.loadTexts:
    alMatrixTopNHighCapacityReverseOverflowOctetRate.setUnits("Octets")
_AlMatrixTopNHighCapacityReverseOctetRate_Type = CounterBasedGauge64
_AlMatrixTopNHighCapacityReverseOctetRate_Object = MibTableColumn
alMatrixTopNHighCapacityReverseOctetRate = _AlMatrixTopNHighCapacityReverseOctetRate_Object(
    (1, 3, 6, 1, 2, 1, 16, 17, 7, 1, 16),
    _AlMatrixTopNHighCapacityReverseOctetRate_Type()
)
alMatrixTopNHighCapacityReverseOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMatrixTopNHighCapacityReverseOctetRate.setStatus("current")
if mibBuilder.loadTexts:
    alMatrixTopNHighCapacityReverseOctetRate.setUnits("Octets")
_UsrHistoryHighCapacityTable_Object = MibTable
usrHistoryHighCapacityTable = _UsrHistoryHighCapacityTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 18, 4)
)
if mibBuilder.loadTexts:
    usrHistoryHighCapacityTable.setStatus("current")
_UsrHistoryHighCapacityEntry_Object = MibTableRow
usrHistoryHighCapacityEntry = _UsrHistoryHighCapacityEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 18, 4, 1)
)
usrHistoryHighCapacityEntry.setIndexNames(
    (0, "RMON2-MIB", "usrHistoryControlIndex"),
    (0, "RMON2-MIB", "usrHistorySampleIndex"),
    (0, "RMON2-MIB", "usrHistoryObjectIndex"),
)
if mibBuilder.loadTexts:
    usrHistoryHighCapacityEntry.setStatus("current")
_UsrHistoryHighCapacityOverflowAbsValue_Type = Gauge32
_UsrHistoryHighCapacityOverflowAbsValue_Object = MibTableColumn
usrHistoryHighCapacityOverflowAbsValue = _UsrHistoryHighCapacityOverflowAbsValue_Object(
    (1, 3, 6, 1, 2, 1, 16, 18, 4, 1, 1),
    _UsrHistoryHighCapacityOverflowAbsValue_Type()
)
usrHistoryHighCapacityOverflowAbsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usrHistoryHighCapacityOverflowAbsValue.setStatus("current")
_UsrHistoryHighCapacityAbsValue_Type = CounterBasedGauge64
_UsrHistoryHighCapacityAbsValue_Object = MibTableColumn
usrHistoryHighCapacityAbsValue = _UsrHistoryHighCapacityAbsValue_Object(
    (1, 3, 6, 1, 2, 1, 16, 18, 4, 1, 2),
    _UsrHistoryHighCapacityAbsValue_Type()
)
usrHistoryHighCapacityAbsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usrHistoryHighCapacityAbsValue.setStatus("current")


class _HcRMONCapabilities_Type(Bits):
    """Custom type hcRMONCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("mediaIndependentGroup", 0),
          ("etherStatsHighCapacityGroup", 1),
          ("etherHistoryHighCapacityGroup", 2),
          ("hostHighCapacityGroup", 3),
          ("hostTopNHighCapacityGroup", 4),
          ("matrixHighCapacityGroup", 5),
          ("captureBufferHighCapacityGroup", 6),
          ("protocolDistributionHighCapacityGroup", 7),
          ("nlHostHighCapacityGroup", 8),
          ("nlMatrixHighCapacityGroup", 9),
          ("nlMatrixTopNHighCapacityGroup", 10),
          ("alHostHighCapacityGroup", 11),
          ("alMatrixHighCapacityGroup", 12),
          ("alMatrixTopNHighCapacityGroup", 13),
          ("usrHistoryHighCapacityGroup", 14))
    )

_HcRMONCapabilities_Type.__name__ = "Bits"
_HcRMONCapabilities_Object = MibScalar
hcRMONCapabilities = _HcRMONCapabilities_Object(
    (1, 3, 6, 1, 2, 1, 16, 19, 16),
    _HcRMONCapabilities_Type()
)
hcRMONCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcRMONCapabilities.setStatus("current")
_HcRmonMIBCompliances_ObjectIdentity = ObjectIdentity
hcRmonMIBCompliances = _HcRmonMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 20, 6)
)
_HcRmonMIBGroups_ObjectIdentity = ObjectIdentity
hcRmonMIBGroups = _HcRmonMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 20, 7)
)
_MediaIndependentStats_ObjectIdentity = ObjectIdentity
mediaIndependentStats = _MediaIndependentStats_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 21)
)
_MediaIndependentTable_Object = MibTable
mediaIndependentTable = _MediaIndependentTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1)
)
if mibBuilder.loadTexts:
    mediaIndependentTable.setStatus("current")
_MediaIndependentEntry_Object = MibTableRow
mediaIndependentEntry = _MediaIndependentEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1)
)
mediaIndependentEntry.setIndexNames(
    (0, "HC-RMON-MIB", "mediaIndependentIndex"),
)
if mibBuilder.loadTexts:
    mediaIndependentEntry.setStatus("current")


class _MediaIndependentIndex_Type(Integer32):
    """Custom type mediaIndependentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MediaIndependentIndex_Type.__name__ = "Integer32"
_MediaIndependentIndex_Object = MibTableColumn
mediaIndependentIndex = _MediaIndependentIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 1),
    _MediaIndependentIndex_Type()
)
mediaIndependentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mediaIndependentIndex.setStatus("current")
_MediaIndependentDataSource_Type = ObjectIdentifier
_MediaIndependentDataSource_Object = MibTableColumn
mediaIndependentDataSource = _MediaIndependentDataSource_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 2),
    _MediaIndependentDataSource_Type()
)
mediaIndependentDataSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mediaIndependentDataSource.setStatus("current")
_MediaIndependentDropEvents_Type = Counter32
_MediaIndependentDropEvents_Object = MibTableColumn
mediaIndependentDropEvents = _MediaIndependentDropEvents_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 3),
    _MediaIndependentDropEvents_Type()
)
mediaIndependentDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaIndependentDropEvents.setStatus("current")
if mibBuilder.loadTexts:
    mediaIndependentDropEvents.setUnits("Events")
_MediaIndependentDroppedFrames_Type = Counter32
_MediaIndependentDroppedFrames_Object = MibTableColumn
mediaIndependentDroppedFrames = _MediaIndependentDroppedFrames_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 4),
    _MediaIndependentDroppedFrames_Type()
)
mediaIndependentDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaIndependentDroppedFrames.setStatus("current")
if mibBuilder.loadTexts:
    mediaIndependentDroppedFrames.setUnits("Packets")
_MediaIndependentInPkts_Type = Counter32
_MediaIndependentInPkts_Object = MibTableColumn
mediaIndependentInPkts = _MediaIndependentInPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 5),
    _MediaIndependentInPkts_Type()
)
mediaIndependentInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaIndependentInPkts.setStatus("current")
if mibBuilder.loadTexts:
    mediaIndependentInPkts.setUnits("Packets")
_MediaIndependentInOverflowPkts_Type = Counter32
_MediaIndependentInOverflowPkts_Object = MibTableColumn
mediaIndependentInOverflowPkts = _MediaIndependentInOverflowPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 6),
    _MediaIndependentInOverflowPkts_Type()
)
mediaIndependentInOverflowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaIndependentInOverflowPkts.setStatus("current")
if mibBuilder.loadTexts:
    mediaIndependentInOverflowPkts.setUnits("Packets")
_MediaIndependentInHighCapacityPkts_Type = Counter64
_MediaIndependentInHighCapacityPkts_Object = MibTableColumn
mediaIndependentInHighCapacityPkts = _MediaIndependentInHighCapacityPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 7),
    _MediaIndependentInHighCapacityPkts_Type()
)
mediaIndependentInHighCapacityPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaIndependentInHighCapacityPkts.setStatus("current")
if mibBuilder.loadTexts:
    mediaIndependentInHighCapacityPkts.setUnits("Packets")
_MediaIndependentOutPkts_Type = Counter32
_MediaIndependentOutPkts_Object = MibTableColumn
mediaIndependentOutPkts = _MediaIndependentOutPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 8),
    _MediaIndependentOutPkts_Type()
)
mediaIndependentOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaIndependentOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    mediaIndependentOutPkts.setUnits("Packets")
_MediaIndependentOutOverflowPkts_Type = Counter32
_MediaIndependentOutOverflowPkts_Object = MibTableColumn
mediaIndependentOutOverflowPkts = _MediaIndependentOutOverflowPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 9),
    _MediaIndependentOutOverflowPkts_Type()
)
mediaIndependentOutOverflowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaIndependentOutOverflowPkts.setStatus("current")
if mibBuilder.loadTexts:
    mediaIndependentOutOverflowPkts.setUnits("Packets")
_MediaIndependentOutHighCapacityPkts_Type = Counter64
_MediaIndependentOutHighCapacityPkts_Object = MibTableColumn
mediaIndependentOutHighCapacityPkts = _MediaIndependentOutHighCapacityPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 10),
    _MediaIndependentOutHighCapacityPkts_Type()
)
mediaIndependentOutHighCapacityPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaIndependentOutHighCapacityPkts.setStatus("current")
if mibBuilder.loadTexts:
    mediaIndependentOutHighCapacityPkts.setUnits("Packets")
_MediaIndependentInOctets_Type = Counter32
_MediaIndependentInOctets_Object = MibTableColumn
mediaIndependentInOctets = _MediaIndependentInOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 11),
    _MediaIndependentInOctets_Type()
)
mediaIndependentInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaIndependentInOctets.setStatus("current")
if mibBuilder.loadTexts:
    mediaIndependentInOctets.setUnits("Octets")
_MediaIndependentInOverflowOctets_Type = Counter32
_MediaIndependentInOverflowOctets_Object = MibTableColumn
mediaIndependentInOverflowOctets = _MediaIndependentInOverflowOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 12),
    _MediaIndependentInOverflowOctets_Type()
)
mediaIndependentInOverflowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaIndependentInOverflowOctets.setStatus("current")
if mibBuilder.loadTexts:
    mediaIndependentInOverflowOctets.setUnits("Octets")
_MediaIndependentInHighCapacityOctets_Type = Counter64
_MediaIndependentInHighCapacityOctets_Object = MibTableColumn
mediaIndependentInHighCapacityOctets = _MediaIndependentInHighCapacityOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 13),
    _MediaIndependentInHighCapacityOctets_Type()
)
mediaIndependentInHighCapacityOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaIndependentInHighCapacityOctets.setStatus("current")
if mibBuilder.loadTexts:
    mediaIndependentInHighCapacityOctets.setUnits("Octets")
_MediaIndependentOutOctets_Type = Counter32
_MediaIndependentOutOctets_Object = MibTableColumn
mediaIndependentOutOctets = _MediaIndependentOutOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 14),
    _MediaIndependentOutOctets_Type()
)
mediaIndependentOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaIndependentOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    mediaIndependentOutOctets.setUnits("Octets")
_MediaIndependentOutOverflowOctets_Type = Counter32
_MediaIndependentOutOverflowOctets_Object = MibTableColumn
mediaIndependentOutOverflowOctets = _MediaIndependentOutOverflowOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 15),
    _MediaIndependentOutOverflowOctets_Type()
)
mediaIndependentOutOverflowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaIndependentOutOverflowOctets.setStatus("current")
if mibBuilder.loadTexts:
    mediaIndependentOutOverflowOctets.setUnits("Octets")
_MediaIndependentOutHighCapacityOctets_Type = Counter64
_MediaIndependentOutHighCapacityOctets_Object = MibTableColumn
mediaIndependentOutHighCapacityOctets = _MediaIndependentOutHighCapacityOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 16),
    _MediaIndependentOutHighCapacityOctets_Type()
)
mediaIndependentOutHighCapacityOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaIndependentOutHighCapacityOctets.setStatus("current")
if mibBuilder.loadTexts:
    mediaIndependentOutHighCapacityOctets.setUnits("Octets")
_MediaIndependentInNUCastPkts_Type = Counter32
_MediaIndependentInNUCastPkts_Object = MibTableColumn
mediaIndependentInNUCastPkts = _MediaIndependentInNUCastPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 17),
    _MediaIndependentInNUCastPkts_Type()
)
mediaIndependentInNUCastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaIndependentInNUCastPkts.setStatus("current")
if mibBuilder.loadTexts:
    mediaIndependentInNUCastPkts.setUnits("Packets")
_MediaIndependentInNUCastOverflowPkts_Type = Counter32
_MediaIndependentInNUCastOverflowPkts_Object = MibTableColumn
mediaIndependentInNUCastOverflowPkts = _MediaIndependentInNUCastOverflowPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 18),
    _MediaIndependentInNUCastOverflowPkts_Type()
)
mediaIndependentInNUCastOverflowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaIndependentInNUCastOverflowPkts.setStatus("current")
if mibBuilder.loadTexts:
    mediaIndependentInNUCastOverflowPkts.setUnits("Packets")
_MediaIndependentInNUCastHighCapacityPkts_Type = Counter64
_MediaIndependentInNUCastHighCapacityPkts_Object = MibTableColumn
mediaIndependentInNUCastHighCapacityPkts = _MediaIndependentInNUCastHighCapacityPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 19),
    _MediaIndependentInNUCastHighCapacityPkts_Type()
)
mediaIndependentInNUCastHighCapacityPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaIndependentInNUCastHighCapacityPkts.setStatus("current")
if mibBuilder.loadTexts:
    mediaIndependentInNUCastHighCapacityPkts.setUnits("Packets")
_MediaIndependentOutNUCastPkts_Type = Counter32
_MediaIndependentOutNUCastPkts_Object = MibTableColumn
mediaIndependentOutNUCastPkts = _MediaIndependentOutNUCastPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 20),
    _MediaIndependentOutNUCastPkts_Type()
)
mediaIndependentOutNUCastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaIndependentOutNUCastPkts.setStatus("current")
if mibBuilder.loadTexts:
    mediaIndependentOutNUCastPkts.setUnits("Packets")
_MediaIndependentOutNUCastOverflowPkts_Type = Counter32
_MediaIndependentOutNUCastOverflowPkts_Object = MibTableColumn
mediaIndependentOutNUCastOverflowPkts = _MediaIndependentOutNUCastOverflowPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 21),
    _MediaIndependentOutNUCastOverflowPkts_Type()
)
mediaIndependentOutNUCastOverflowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaIndependentOutNUCastOverflowPkts.setStatus("current")
if mibBuilder.loadTexts:
    mediaIndependentOutNUCastOverflowPkts.setUnits("Packets")
_MediaIndependentOutNUCastHighCapacityPkts_Type = Counter64
_MediaIndependentOutNUCastHighCapacityPkts_Object = MibTableColumn
mediaIndependentOutNUCastHighCapacityPkts = _MediaIndependentOutNUCastHighCapacityPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 22),
    _MediaIndependentOutNUCastHighCapacityPkts_Type()
)
mediaIndependentOutNUCastHighCapacityPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaIndependentOutNUCastHighCapacityPkts.setStatus("current")
if mibBuilder.loadTexts:
    mediaIndependentOutNUCastHighCapacityPkts.setUnits("Packets")
_MediaIndependentInErrors_Type = Counter32
_MediaIndependentInErrors_Object = MibTableColumn
mediaIndependentInErrors = _MediaIndependentInErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 23),
    _MediaIndependentInErrors_Type()
)
mediaIndependentInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaIndependentInErrors.setStatus("current")
if mibBuilder.loadTexts:
    mediaIndependentInErrors.setUnits("Packets")
_MediaIndependentOutErrors_Type = Counter32
_MediaIndependentOutErrors_Object = MibTableColumn
mediaIndependentOutErrors = _MediaIndependentOutErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 24),
    _MediaIndependentOutErrors_Type()
)
mediaIndependentOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaIndependentOutErrors.setStatus("current")
if mibBuilder.loadTexts:
    mediaIndependentOutErrors.setUnits("Packets")
_MediaIndependentInputSpeed_Type = Gauge32
_MediaIndependentInputSpeed_Object = MibTableColumn
mediaIndependentInputSpeed = _MediaIndependentInputSpeed_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 25),
    _MediaIndependentInputSpeed_Type()
)
mediaIndependentInputSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaIndependentInputSpeed.setStatus("current")
if mibBuilder.loadTexts:
    mediaIndependentInputSpeed.setUnits("Kilobits per Second")
_MediaIndependentOutputSpeed_Type = Gauge32
_MediaIndependentOutputSpeed_Object = MibTableColumn
mediaIndependentOutputSpeed = _MediaIndependentOutputSpeed_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 26),
    _MediaIndependentOutputSpeed_Type()
)
mediaIndependentOutputSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaIndependentOutputSpeed.setStatus("current")
if mibBuilder.loadTexts:
    mediaIndependentOutputSpeed.setUnits("Kilobits per Second")


class _MediaIndependentDuplexMode_Type(Integer32):
    """Custom type mediaIndependentDuplexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("halfduplex", 1),
          ("fullduplex", 2))
    )


_MediaIndependentDuplexMode_Type.__name__ = "Integer32"
_MediaIndependentDuplexMode_Object = MibTableColumn
mediaIndependentDuplexMode = _MediaIndependentDuplexMode_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 27),
    _MediaIndependentDuplexMode_Type()
)
mediaIndependentDuplexMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaIndependentDuplexMode.setStatus("current")
_MediaIndependentDuplexChanges_Type = Counter32
_MediaIndependentDuplexChanges_Object = MibTableColumn
mediaIndependentDuplexChanges = _MediaIndependentDuplexChanges_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 28),
    _MediaIndependentDuplexChanges_Type()
)
mediaIndependentDuplexChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaIndependentDuplexChanges.setStatus("current")
if mibBuilder.loadTexts:
    mediaIndependentDuplexChanges.setUnits("Events")
_MediaIndependentDuplexLastChange_Type = TimeStamp
_MediaIndependentDuplexLastChange_Object = MibTableColumn
mediaIndependentDuplexLastChange = _MediaIndependentDuplexLastChange_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 29),
    _MediaIndependentDuplexLastChange_Type()
)
mediaIndependentDuplexLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaIndependentDuplexLastChange.setStatus("current")
_MediaIndependentOwner_Type = OwnerString
_MediaIndependentOwner_Object = MibTableColumn
mediaIndependentOwner = _MediaIndependentOwner_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 30),
    _MediaIndependentOwner_Type()
)
mediaIndependentOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mediaIndependentOwner.setStatus("current")
_MediaIndependentStatus_Type = RowStatus
_MediaIndependentStatus_Object = MibTableColumn
mediaIndependentStatus = _MediaIndependentStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 31),
    _MediaIndependentStatus_Type()
)
mediaIndependentStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mediaIndependentStatus.setStatus("current")

# Managed Objects groups

mediaIndependentGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 20, 7, 1)
)
mediaIndependentGroup.setObjects(
      *(("HC-RMON-MIB", "mediaIndependentDataSource"),
        ("HC-RMON-MIB", "mediaIndependentDropEvents"),
        ("HC-RMON-MIB", "mediaIndependentDroppedFrames"),
        ("HC-RMON-MIB", "mediaIndependentInPkts"),
        ("HC-RMON-MIB", "mediaIndependentInOverflowPkts"),
        ("HC-RMON-MIB", "mediaIndependentInHighCapacityPkts"),
        ("HC-RMON-MIB", "mediaIndependentOutPkts"),
        ("HC-RMON-MIB", "mediaIndependentOutOverflowPkts"),
        ("HC-RMON-MIB", "mediaIndependentOutHighCapacityPkts"),
        ("HC-RMON-MIB", "mediaIndependentInOctets"),
        ("HC-RMON-MIB", "mediaIndependentInOverflowOctets"),
        ("HC-RMON-MIB", "mediaIndependentInHighCapacityOctets"),
        ("HC-RMON-MIB", "mediaIndependentOutOctets"),
        ("HC-RMON-MIB", "mediaIndependentOutOverflowOctets"),
        ("HC-RMON-MIB", "mediaIndependentOutHighCapacityOctets"),
        ("HC-RMON-MIB", "mediaIndependentInNUCastPkts"),
        ("HC-RMON-MIB", "mediaIndependentInNUCastOverflowPkts"),
        ("HC-RMON-MIB", "mediaIndependentInNUCastHighCapacityPkts"),
        ("HC-RMON-MIB", "mediaIndependentOutNUCastPkts"),
        ("HC-RMON-MIB", "mediaIndependentOutNUCastOverflowPkts"),
        ("HC-RMON-MIB", "mediaIndependentOutNUCastHighCapacityPkts"),
        ("HC-RMON-MIB", "mediaIndependentInErrors"),
        ("HC-RMON-MIB", "mediaIndependentOutErrors"),
        ("HC-RMON-MIB", "mediaIndependentInputSpeed"),
        ("HC-RMON-MIB", "mediaIndependentOutputSpeed"),
        ("HC-RMON-MIB", "mediaIndependentDuplexMode"),
        ("HC-RMON-MIB", "mediaIndependentDuplexChanges"),
        ("HC-RMON-MIB", "mediaIndependentDuplexLastChange"),
        ("HC-RMON-MIB", "mediaIndependentOwner"),
        ("HC-RMON-MIB", "mediaIndependentStatus"))
)
if mibBuilder.loadTexts:
    mediaIndependentGroup.setStatus("current")

etherStatsHighCapacityGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 20, 7, 2)
)
etherStatsHighCapacityGroup.setObjects(
      *(("HC-RMON-MIB", "etherStatsHighCapacityOverflowPkts"),
        ("HC-RMON-MIB", "etherStatsHighCapacityPkts"),
        ("HC-RMON-MIB", "etherStatsHighCapacityOverflowOctets"),
        ("HC-RMON-MIB", "etherStatsHighCapacityOctets"),
        ("HC-RMON-MIB", "etherStatsHighCapacityOverflowPkts64Octets"),
        ("HC-RMON-MIB", "etherStatsHighCapacityPkts64Octets"),
        ("HC-RMON-MIB", "etherStatsHighCapacityOverflowPkts65to127Octets"),
        ("HC-RMON-MIB", "etherStatsHighCapacityPkts65to127Octets"),
        ("HC-RMON-MIB", "etherStatsHighCapacityOverflowPkts128to255Octets"),
        ("HC-RMON-MIB", "etherStatsHighCapacityPkts128to255Octets"),
        ("HC-RMON-MIB", "etherStatsHighCapacityOverflowPkts256to511Octets"),
        ("HC-RMON-MIB", "etherStatsHighCapacityPkts256to511Octets"),
        ("HC-RMON-MIB", "etherStatsHighCapacityOverflowPkts512to1023Octets"),
        ("HC-RMON-MIB", "etherStatsHighCapacityPkts512to1023Octets"),
        ("HC-RMON-MIB", "etherStatsHighCapacityOverflowPkts1024to1518Octets"),
        ("HC-RMON-MIB", "etherStatsHighCapacityPkts1024to1518Octets"))
)
if mibBuilder.loadTexts:
    etherStatsHighCapacityGroup.setStatus("current")

etherHistoryHighCapacityGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 20, 7, 3)
)
etherHistoryHighCapacityGroup.setObjects(
      *(("HC-RMON-MIB", "etherHistoryHighCapacityOverflowPkts"),
        ("HC-RMON-MIB", "etherHistoryHighCapacityPkts"),
        ("HC-RMON-MIB", "etherHistoryHighCapacityOverflowOctets"),
        ("HC-RMON-MIB", "etherHistoryHighCapacityOctets"))
)
if mibBuilder.loadTexts:
    etherHistoryHighCapacityGroup.setStatus("current")

hostHighCapacityGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 20, 7, 4)
)
hostHighCapacityGroup.setObjects(
      *(("HC-RMON-MIB", "hostHighCapacityInOverflowPkts"),
        ("HC-RMON-MIB", "hostHighCapacityInPkts"),
        ("HC-RMON-MIB", "hostHighCapacityOutOverflowPkts"),
        ("HC-RMON-MIB", "hostHighCapacityOutPkts"),
        ("HC-RMON-MIB", "hostHighCapacityInOverflowOctets"),
        ("HC-RMON-MIB", "hostHighCapacityInOctets"),
        ("HC-RMON-MIB", "hostHighCapacityOutOverflowOctets"),
        ("HC-RMON-MIB", "hostHighCapacityOutOctets"),
        ("HC-RMON-MIB", "hostTimeHighCapacityInOverflowPkts"),
        ("HC-RMON-MIB", "hostTimeHighCapacityInPkts"),
        ("HC-RMON-MIB", "hostTimeHighCapacityOutOverflowPkts"),
        ("HC-RMON-MIB", "hostTimeHighCapacityOutPkts"),
        ("HC-RMON-MIB", "hostTimeHighCapacityInOverflowOctets"),
        ("HC-RMON-MIB", "hostTimeHighCapacityInOctets"),
        ("HC-RMON-MIB", "hostTimeHighCapacityOutOverflowOctets"),
        ("HC-RMON-MIB", "hostTimeHighCapacityOutOctets"))
)
if mibBuilder.loadTexts:
    hostHighCapacityGroup.setStatus("current")

hostTopNHighCapacityGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 20, 7, 5)
)
hostTopNHighCapacityGroup.setObjects(
      *(("HC-RMON-MIB", "hostTopNHighCapacityAddress"),
        ("HC-RMON-MIB", "hostTopNHighCapacityBaseRate"),
        ("HC-RMON-MIB", "hostTopNHighCapacityOverflowRate"),
        ("HC-RMON-MIB", "hostTopNHighCapacityRate"))
)
if mibBuilder.loadTexts:
    hostTopNHighCapacityGroup.setStatus("current")

matrixHighCapacityGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 20, 7, 6)
)
matrixHighCapacityGroup.setObjects(
      *(("HC-RMON-MIB", "matrixSDHighCapacityOverflowPkts"),
        ("HC-RMON-MIB", "matrixSDHighCapacityPkts"),
        ("HC-RMON-MIB", "matrixSDHighCapacityOverflowOctets"),
        ("HC-RMON-MIB", "matrixSDHighCapacityOctets"),
        ("HC-RMON-MIB", "matrixDSHighCapacityOverflowPkts"),
        ("HC-RMON-MIB", "matrixDSHighCapacityPkts"),
        ("HC-RMON-MIB", "matrixDSHighCapacityOverflowOctets"),
        ("HC-RMON-MIB", "matrixDSHighCapacityOctets"))
)
if mibBuilder.loadTexts:
    matrixHighCapacityGroup.setStatus("current")

captureBufferHighCapacityGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 20, 7, 7)
)
captureBufferHighCapacityGroup.setObjects(
    ("HC-RMON-MIB", "captureBufferPacketHighCapacityTime")
)
if mibBuilder.loadTexts:
    captureBufferHighCapacityGroup.setStatus("current")

protocolDistributionHighCapacityGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 20, 7, 8)
)
protocolDistributionHighCapacityGroup.setObjects(
      *(("HC-RMON-MIB", "protocolDistStatsHighCapacityOverflowPkts"),
        ("HC-RMON-MIB", "protocolDistStatsHighCapacityPkts"),
        ("HC-RMON-MIB", "protocolDistStatsHighCapacityOverflowOctets"),
        ("HC-RMON-MIB", "protocolDistStatsHighCapacityOctets"))
)
if mibBuilder.loadTexts:
    protocolDistributionHighCapacityGroup.setStatus("current")

nlHostHighCapacityGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 20, 7, 9)
)
nlHostHighCapacityGroup.setObjects(
      *(("HC-RMON-MIB", "nlHostHighCapacityInOverflowPkts"),
        ("HC-RMON-MIB", "nlHostHighCapacityInPkts"),
        ("HC-RMON-MIB", "nlHostHighCapacityOutOverflowPkts"),
        ("HC-RMON-MIB", "nlHostHighCapacityOutPkts"),
        ("HC-RMON-MIB", "nlHostHighCapacityInOverflowOctets"),
        ("HC-RMON-MIB", "nlHostHighCapacityInOctets"),
        ("HC-RMON-MIB", "nlHostHighCapacityOutOverflowOctets"),
        ("HC-RMON-MIB", "nlHostHighCapacityOutOctets"))
)
if mibBuilder.loadTexts:
    nlHostHighCapacityGroup.setStatus("current")

nlMatrixHighCapacityGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 20, 7, 10)
)
nlMatrixHighCapacityGroup.setObjects(
      *(("HC-RMON-MIB", "nlMatrixSDHighCapacityOverflowPkts"),
        ("HC-RMON-MIB", "nlMatrixSDHighCapacityPkts"),
        ("HC-RMON-MIB", "nlMatrixSDHighCapacityOverflowOctets"),
        ("HC-RMON-MIB", "nlMatrixSDHighCapacityOctets"),
        ("HC-RMON-MIB", "nlMatrixDSHighCapacityOverflowPkts"),
        ("HC-RMON-MIB", "nlMatrixDSHighCapacityPkts"),
        ("HC-RMON-MIB", "nlMatrixDSHighCapacityOverflowOctets"),
        ("HC-RMON-MIB", "nlMatrixDSHighCapacityOctets"))
)
if mibBuilder.loadTexts:
    nlMatrixHighCapacityGroup.setStatus("current")

nlMatrixTopNHighCapacityGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 20, 7, 11)
)
nlMatrixTopNHighCapacityGroup.setObjects(
      *(("HC-RMON-MIB", "nlMatrixTopNHighCapacityProtocolDirLocalIndex"),
        ("HC-RMON-MIB", "nlMatrixTopNHighCapacitySourceAddress"),
        ("HC-RMON-MIB", "nlMatrixTopNHighCapacityDestAddress"),
        ("HC-RMON-MIB", "nlMatrixTopNHighCapacityBasePktRate"),
        ("HC-RMON-MIB", "nlMatrixTopNHighCapacityOverflowPktRate"),
        ("HC-RMON-MIB", "nlMatrixTopNHighCapacityPktRate"),
        ("HC-RMON-MIB", "nlMatrixTopNHighCapacityReverseBasePktRate"),
        ("HC-RMON-MIB", "nlMatrixTopNHighCapacityReverseOverflowPktRate"),
        ("HC-RMON-MIB", "nlMatrixTopNHighCapacityReversePktRate"),
        ("HC-RMON-MIB", "nlMatrixTopNHighCapacityBaseOctetRate"),
        ("HC-RMON-MIB", "nlMatrixTopNHighCapacityOverflowOctetRate"),
        ("HC-RMON-MIB", "nlMatrixTopNHighCapacityOctetRate"),
        ("HC-RMON-MIB", "nlMatrixTopNHighCapacityReverseBaseOctetRate"),
        ("HC-RMON-MIB", "nlMatrixTopNHighCapacityReverseOverflowOctetRate"),
        ("HC-RMON-MIB", "nlMatrixTopNHighCapacityReverseOctetRate"))
)
if mibBuilder.loadTexts:
    nlMatrixTopNHighCapacityGroup.setStatus("current")

alHostHighCapacityGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 20, 7, 12)
)
alHostHighCapacityGroup.setObjects(
      *(("HC-RMON-MIB", "alHostHighCapacityInOverflowPkts"),
        ("HC-RMON-MIB", "alHostHighCapacityInPkts"),
        ("HC-RMON-MIB", "alHostHighCapacityOutOverflowPkts"),
        ("HC-RMON-MIB", "alHostHighCapacityOutPkts"),
        ("HC-RMON-MIB", "alHostHighCapacityInOverflowOctets"),
        ("HC-RMON-MIB", "alHostHighCapacityInOctets"),
        ("HC-RMON-MIB", "alHostHighCapacityOutOverflowOctets"),
        ("HC-RMON-MIB", "alHostHighCapacityOutOctets"))
)
if mibBuilder.loadTexts:
    alHostHighCapacityGroup.setStatus("current")

alMatrixHighCapacityGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 20, 7, 13)
)
alMatrixHighCapacityGroup.setObjects(
      *(("HC-RMON-MIB", "alMatrixSDHighCapacityOverflowPkts"),
        ("HC-RMON-MIB", "alMatrixSDHighCapacityPkts"),
        ("HC-RMON-MIB", "alMatrixSDHighCapacityOverflowOctets"),
        ("HC-RMON-MIB", "alMatrixSDHighCapacityOctets"),
        ("HC-RMON-MIB", "alMatrixDSHighCapacityOverflowPkts"),
        ("HC-RMON-MIB", "alMatrixDSHighCapacityPkts"),
        ("HC-RMON-MIB", "alMatrixDSHighCapacityOverflowOctets"),
        ("HC-RMON-MIB", "alMatrixDSHighCapacityOctets"))
)
if mibBuilder.loadTexts:
    alMatrixHighCapacityGroup.setStatus("current")

alMatrixTopNHighCapacityGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 20, 7, 14)
)
alMatrixTopNHighCapacityGroup.setObjects(
      *(("HC-RMON-MIB", "alMatrixTopNHighCapacityProtocolDirLocalIndex"),
        ("HC-RMON-MIB", "alMatrixTopNHighCapacitySourceAddress"),
        ("HC-RMON-MIB", "alMatrixTopNHighCapacityDestAddress"),
        ("HC-RMON-MIB", "alMatrixTopNHighCapacityAppProtocolDirLocalIndex"),
        ("HC-RMON-MIB", "alMatrixTopNHighCapacityBasePktRate"),
        ("HC-RMON-MIB", "alMatrixTopNHighCapacityOverflowPktRate"),
        ("HC-RMON-MIB", "alMatrixTopNHighCapacityPktRate"),
        ("HC-RMON-MIB", "alMatrixTopNHighCapacityReverseBasePktRate"),
        ("HC-RMON-MIB", "alMatrixTopNHighCapacityReverseOverflowPktRate"),
        ("HC-RMON-MIB", "alMatrixTopNHighCapacityReversePktRate"),
        ("HC-RMON-MIB", "alMatrixTopNHighCapacityBaseOctetRate"),
        ("HC-RMON-MIB", "alMatrixTopNHighCapacityOverflowOctetRate"),
        ("HC-RMON-MIB", "alMatrixTopNHighCapacityOctetRate"),
        ("HC-RMON-MIB", "alMatrixTopNHighCapacityReverseBaseOctetRate"),
        ("HC-RMON-MIB", "alMatrixTopNHighCapacityReverseOverflowOctetRate"),
        ("HC-RMON-MIB", "alMatrixTopNHighCapacityReverseOctetRate"))
)
if mibBuilder.loadTexts:
    alMatrixTopNHighCapacityGroup.setStatus("current")

usrHistoryHighCapacityGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 20, 7, 15)
)
usrHistoryHighCapacityGroup.setObjects(
      *(("HC-RMON-MIB", "usrHistoryHighCapacityOverflowAbsValue"),
        ("HC-RMON-MIB", "usrHistoryHighCapacityAbsValue"))
)
if mibBuilder.loadTexts:
    usrHistoryHighCapacityGroup.setStatus("current")

hcRMONInformationGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 20, 7, 16)
)
hcRMONInformationGroup.setObjects(
    ("HC-RMON-MIB", "hcRMONCapabilities")
)
if mibBuilder.loadTexts:
    hcRMONInformationGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hcMediaIndependentCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 16, 20, 6, 1)
)
hcMediaIndependentCompliance.setObjects(
      *(("HC-RMON-MIB", "mediaIndependentGroup"),
        ("HC-RMON-MIB", "hcRMONInformationGroup"))
)
if mibBuilder.loadTexts:
    hcMediaIndependentCompliance.setStatus(
        "current"
    )

hcRmon1MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 16, 20, 6, 2)
)
hcRmon1MIBCompliance.setObjects(
      *(("HC-RMON-MIB", "etherStatsHighCapacityGroup"),
        ("HC-RMON-MIB", "etherHistoryHighCapacityGroup"),
        ("HC-RMON-MIB", "hostHighCapacityGroup"),
        ("HC-RMON-MIB", "hostTopNHighCapacityGroup"),
        ("HC-RMON-MIB", "matrixHighCapacityGroup"),
        ("HC-RMON-MIB", "captureBufferHighCapacityGroup"),
        ("RMON-MIB", "rmonEtherStatsGroup"),
        ("RMON-MIB", "rmonHistoryControlGroup"),
        ("RMON-MIB", "rmonEthernetHistoryGroup"),
        ("RMON-MIB", "rmonHostGroup"),
        ("RMON-MIB", "rmonHostTopNGroup"),
        ("RMON-MIB", "rmonMatrixGroup"),
        ("RMON-MIB", "rmonFilterGroup"),
        ("RMON-MIB", "rmonPacketCaptureGroup"))
)
if mibBuilder.loadTexts:
    hcRmon1MIBCompliance.setStatus(
        "current"
    )

hcRmon2MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 16, 20, 6, 3)
)
hcRmon2MIBCompliance.setObjects(
      *(("HC-RMON-MIB", "protocolDistributionHighCapacityGroup"),
        ("HC-RMON-MIB", "nlHostHighCapacityGroup"),
        ("HC-RMON-MIB", "nlMatrixHighCapacityGroup"),
        ("HC-RMON-MIB", "nlMatrixTopNHighCapacityGroup"),
        ("HC-RMON-MIB", "usrHistoryHighCapacityGroup"),
        ("HC-RMON-MIB", "hcRMONInformationGroup"),
        ("RMON2-MIB", "protocolDirectoryGroup"),
        ("RMON2-MIB", "protocolDistributionGroup"),
        ("RMON2-MIB", "addressMapGroup"),
        ("RMON2-MIB", "nlHostGroup"),
        ("RMON2-MIB", "nlMatrixGroup"),
        ("RMON2-MIB", "usrHistoryGroup"),
        ("RMON2-MIB", "probeInformationGroup"),
        ("RMON2-MIB", "rmon1EnhancementGroup"))
)
if mibBuilder.loadTexts:
    hcRmon2MIBCompliance.setStatus(
        "current"
    )

hcRmon2MIBApplicationLayerCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 16, 20, 6, 4)
)
hcRmon2MIBApplicationLayerCompliance.setObjects(
      *(("HC-RMON-MIB", "protocolDistributionHighCapacityGroup"),
        ("HC-RMON-MIB", "nlHostHighCapacityGroup"),
        ("HC-RMON-MIB", "nlMatrixHighCapacityGroup"),
        ("HC-RMON-MIB", "nlMatrixTopNHighCapacityGroup"),
        ("HC-RMON-MIB", "alHostHighCapacityGroup"),
        ("HC-RMON-MIB", "alMatrixHighCapacityGroup"),
        ("HC-RMON-MIB", "alMatrixTopNHighCapacityGroup"),
        ("HC-RMON-MIB", "usrHistoryHighCapacityGroup"),
        ("HC-RMON-MIB", "hcRMONInformationGroup"),
        ("RMON2-MIB", "protocolDirectoryGroup"),
        ("RMON2-MIB", "protocolDistributionGroup"),
        ("RMON2-MIB", "addressMapGroup"),
        ("RMON2-MIB", "nlHostGroup"),
        ("RMON2-MIB", "nlMatrixGroup"),
        ("RMON2-MIB", "alHostGroup"),
        ("RMON2-MIB", "alMatrixGroup"),
        ("RMON2-MIB", "usrHistoryGroup"),
        ("RMON2-MIB", "probeInformationGroup"),
        ("RMON2-MIB", "rmon1EnhancementGroup"))
)
if mibBuilder.loadTexts:
    hcRmon2MIBApplicationLayerCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HC-RMON-MIB",
    **{"etherStatsHighCapacityTable": etherStatsHighCapacityTable,
       "etherStatsHighCapacityEntry": etherStatsHighCapacityEntry,
       "etherStatsHighCapacityOverflowPkts": etherStatsHighCapacityOverflowPkts,
       "etherStatsHighCapacityPkts": etherStatsHighCapacityPkts,
       "etherStatsHighCapacityOverflowOctets": etherStatsHighCapacityOverflowOctets,
       "etherStatsHighCapacityOctets": etherStatsHighCapacityOctets,
       "etherStatsHighCapacityOverflowPkts64Octets": etherStatsHighCapacityOverflowPkts64Octets,
       "etherStatsHighCapacityPkts64Octets": etherStatsHighCapacityPkts64Octets,
       "etherStatsHighCapacityOverflowPkts65to127Octets": etherStatsHighCapacityOverflowPkts65to127Octets,
       "etherStatsHighCapacityPkts65to127Octets": etherStatsHighCapacityPkts65to127Octets,
       "etherStatsHighCapacityOverflowPkts128to255Octets": etherStatsHighCapacityOverflowPkts128to255Octets,
       "etherStatsHighCapacityPkts128to255Octets": etherStatsHighCapacityPkts128to255Octets,
       "etherStatsHighCapacityOverflowPkts256to511Octets": etherStatsHighCapacityOverflowPkts256to511Octets,
       "etherStatsHighCapacityPkts256to511Octets": etherStatsHighCapacityPkts256to511Octets,
       "etherStatsHighCapacityOverflowPkts512to1023Octets": etherStatsHighCapacityOverflowPkts512to1023Octets,
       "etherStatsHighCapacityPkts512to1023Octets": etherStatsHighCapacityPkts512to1023Octets,
       "etherStatsHighCapacityOverflowPkts1024to1518Octets": etherStatsHighCapacityOverflowPkts1024to1518Octets,
       "etherStatsHighCapacityPkts1024to1518Octets": etherStatsHighCapacityPkts1024to1518Octets,
       "etherHistoryHighCapacityTable": etherHistoryHighCapacityTable,
       "etherHistoryHighCapacityEntry": etherHistoryHighCapacityEntry,
       "etherHistoryHighCapacityOverflowPkts": etherHistoryHighCapacityOverflowPkts,
       "etherHistoryHighCapacityPkts": etherHistoryHighCapacityPkts,
       "etherHistoryHighCapacityOverflowOctets": etherHistoryHighCapacityOverflowOctets,
       "etherHistoryHighCapacityOctets": etherHistoryHighCapacityOctets,
       "hostHighCapacityTable": hostHighCapacityTable,
       "hostHighCapacityEntry": hostHighCapacityEntry,
       "hostHighCapacityInOverflowPkts": hostHighCapacityInOverflowPkts,
       "hostHighCapacityInPkts": hostHighCapacityInPkts,
       "hostHighCapacityOutOverflowPkts": hostHighCapacityOutOverflowPkts,
       "hostHighCapacityOutPkts": hostHighCapacityOutPkts,
       "hostHighCapacityInOverflowOctets": hostHighCapacityInOverflowOctets,
       "hostHighCapacityInOctets": hostHighCapacityInOctets,
       "hostHighCapacityOutOverflowOctets": hostHighCapacityOutOverflowOctets,
       "hostHighCapacityOutOctets": hostHighCapacityOutOctets,
       "hostTimeHighCapacityTable": hostTimeHighCapacityTable,
       "hostTimeHighCapacityEntry": hostTimeHighCapacityEntry,
       "hostTimeHighCapacityInOverflowPkts": hostTimeHighCapacityInOverflowPkts,
       "hostTimeHighCapacityInPkts": hostTimeHighCapacityInPkts,
       "hostTimeHighCapacityOutOverflowPkts": hostTimeHighCapacityOutOverflowPkts,
       "hostTimeHighCapacityOutPkts": hostTimeHighCapacityOutPkts,
       "hostTimeHighCapacityInOverflowOctets": hostTimeHighCapacityInOverflowOctets,
       "hostTimeHighCapacityInOctets": hostTimeHighCapacityInOctets,
       "hostTimeHighCapacityOutOverflowOctets": hostTimeHighCapacityOutOverflowOctets,
       "hostTimeHighCapacityOutOctets": hostTimeHighCapacityOutOctets,
       "hostTopNHighCapacityTable": hostTopNHighCapacityTable,
       "hostTopNHighCapacityEntry": hostTopNHighCapacityEntry,
       "hostTopNHighCapacityAddress": hostTopNHighCapacityAddress,
       "hostTopNHighCapacityBaseRate": hostTopNHighCapacityBaseRate,
       "hostTopNHighCapacityOverflowRate": hostTopNHighCapacityOverflowRate,
       "hostTopNHighCapacityRate": hostTopNHighCapacityRate,
       "matrixSDHighCapacityTable": matrixSDHighCapacityTable,
       "matrixSDHighCapacityEntry": matrixSDHighCapacityEntry,
       "matrixSDHighCapacityOverflowPkts": matrixSDHighCapacityOverflowPkts,
       "matrixSDHighCapacityPkts": matrixSDHighCapacityPkts,
       "matrixSDHighCapacityOverflowOctets": matrixSDHighCapacityOverflowOctets,
       "matrixSDHighCapacityOctets": matrixSDHighCapacityOctets,
       "matrixDSHighCapacityTable": matrixDSHighCapacityTable,
       "matrixDSHighCapacityEntry": matrixDSHighCapacityEntry,
       "matrixDSHighCapacityOverflowPkts": matrixDSHighCapacityOverflowPkts,
       "matrixDSHighCapacityPkts": matrixDSHighCapacityPkts,
       "matrixDSHighCapacityOverflowOctets": matrixDSHighCapacityOverflowOctets,
       "matrixDSHighCapacityOctets": matrixDSHighCapacityOctets,
       "captureBufferHighCapacityTable": captureBufferHighCapacityTable,
       "captureBufferHighCapacityEntry": captureBufferHighCapacityEntry,
       "captureBufferPacketHighCapacityTime": captureBufferPacketHighCapacityTime,
       "protocolDistStatsHighCapacityTable": protocolDistStatsHighCapacityTable,
       "protocolDistStatsHighCapacityEntry": protocolDistStatsHighCapacityEntry,
       "protocolDistStatsHighCapacityOverflowPkts": protocolDistStatsHighCapacityOverflowPkts,
       "protocolDistStatsHighCapacityPkts": protocolDistStatsHighCapacityPkts,
       "protocolDistStatsHighCapacityOverflowOctets": protocolDistStatsHighCapacityOverflowOctets,
       "protocolDistStatsHighCapacityOctets": protocolDistStatsHighCapacityOctets,
       "nlHostHighCapacityTable": nlHostHighCapacityTable,
       "nlHostHighCapacityEntry": nlHostHighCapacityEntry,
       "nlHostHighCapacityInOverflowPkts": nlHostHighCapacityInOverflowPkts,
       "nlHostHighCapacityInPkts": nlHostHighCapacityInPkts,
       "nlHostHighCapacityOutOverflowPkts": nlHostHighCapacityOutOverflowPkts,
       "nlHostHighCapacityOutPkts": nlHostHighCapacityOutPkts,
       "nlHostHighCapacityInOverflowOctets": nlHostHighCapacityInOverflowOctets,
       "nlHostHighCapacityInOctets": nlHostHighCapacityInOctets,
       "nlHostHighCapacityOutOverflowOctets": nlHostHighCapacityOutOverflowOctets,
       "nlHostHighCapacityOutOctets": nlHostHighCapacityOutOctets,
       "nlMatrixSDHighCapacityTable": nlMatrixSDHighCapacityTable,
       "nlMatrixSDHighCapacityEntry": nlMatrixSDHighCapacityEntry,
       "nlMatrixSDHighCapacityOverflowPkts": nlMatrixSDHighCapacityOverflowPkts,
       "nlMatrixSDHighCapacityPkts": nlMatrixSDHighCapacityPkts,
       "nlMatrixSDHighCapacityOverflowOctets": nlMatrixSDHighCapacityOverflowOctets,
       "nlMatrixSDHighCapacityOctets": nlMatrixSDHighCapacityOctets,
       "nlMatrixDSHighCapacityTable": nlMatrixDSHighCapacityTable,
       "nlMatrixDSHighCapacityEntry": nlMatrixDSHighCapacityEntry,
       "nlMatrixDSHighCapacityOverflowPkts": nlMatrixDSHighCapacityOverflowPkts,
       "nlMatrixDSHighCapacityPkts": nlMatrixDSHighCapacityPkts,
       "nlMatrixDSHighCapacityOverflowOctets": nlMatrixDSHighCapacityOverflowOctets,
       "nlMatrixDSHighCapacityOctets": nlMatrixDSHighCapacityOctets,
       "nlMatrixTopNHighCapacityTable": nlMatrixTopNHighCapacityTable,
       "nlMatrixTopNHighCapacityEntry": nlMatrixTopNHighCapacityEntry,
       "nlMatrixTopNHighCapacityProtocolDirLocalIndex": nlMatrixTopNHighCapacityProtocolDirLocalIndex,
       "nlMatrixTopNHighCapacitySourceAddress": nlMatrixTopNHighCapacitySourceAddress,
       "nlMatrixTopNHighCapacityDestAddress": nlMatrixTopNHighCapacityDestAddress,
       "nlMatrixTopNHighCapacityBasePktRate": nlMatrixTopNHighCapacityBasePktRate,
       "nlMatrixTopNHighCapacityOverflowPktRate": nlMatrixTopNHighCapacityOverflowPktRate,
       "nlMatrixTopNHighCapacityPktRate": nlMatrixTopNHighCapacityPktRate,
       "nlMatrixTopNHighCapacityReverseBasePktRate": nlMatrixTopNHighCapacityReverseBasePktRate,
       "nlMatrixTopNHighCapacityReverseOverflowPktRate": nlMatrixTopNHighCapacityReverseOverflowPktRate,
       "nlMatrixTopNHighCapacityReversePktRate": nlMatrixTopNHighCapacityReversePktRate,
       "nlMatrixTopNHighCapacityBaseOctetRate": nlMatrixTopNHighCapacityBaseOctetRate,
       "nlMatrixTopNHighCapacityOverflowOctetRate": nlMatrixTopNHighCapacityOverflowOctetRate,
       "nlMatrixTopNHighCapacityOctetRate": nlMatrixTopNHighCapacityOctetRate,
       "nlMatrixTopNHighCapacityReverseBaseOctetRate": nlMatrixTopNHighCapacityReverseBaseOctetRate,
       "nlMatrixTopNHighCapacityReverseOverflowOctetRate": nlMatrixTopNHighCapacityReverseOverflowOctetRate,
       "nlMatrixTopNHighCapacityReverseOctetRate": nlMatrixTopNHighCapacityReverseOctetRate,
       "alHostHighCapacityTable": alHostHighCapacityTable,
       "alHostHighCapacityEntry": alHostHighCapacityEntry,
       "alHostHighCapacityInOverflowPkts": alHostHighCapacityInOverflowPkts,
       "alHostHighCapacityInPkts": alHostHighCapacityInPkts,
       "alHostHighCapacityOutOverflowPkts": alHostHighCapacityOutOverflowPkts,
       "alHostHighCapacityOutPkts": alHostHighCapacityOutPkts,
       "alHostHighCapacityInOverflowOctets": alHostHighCapacityInOverflowOctets,
       "alHostHighCapacityInOctets": alHostHighCapacityInOctets,
       "alHostHighCapacityOutOverflowOctets": alHostHighCapacityOutOverflowOctets,
       "alHostHighCapacityOutOctets": alHostHighCapacityOutOctets,
       "alMatrixSDHighCapacityTable": alMatrixSDHighCapacityTable,
       "alMatrixSDHighCapacityEntry": alMatrixSDHighCapacityEntry,
       "alMatrixSDHighCapacityOverflowPkts": alMatrixSDHighCapacityOverflowPkts,
       "alMatrixSDHighCapacityPkts": alMatrixSDHighCapacityPkts,
       "alMatrixSDHighCapacityOverflowOctets": alMatrixSDHighCapacityOverflowOctets,
       "alMatrixSDHighCapacityOctets": alMatrixSDHighCapacityOctets,
       "alMatrixDSHighCapacityTable": alMatrixDSHighCapacityTable,
       "alMatrixDSHighCapacityEntry": alMatrixDSHighCapacityEntry,
       "alMatrixDSHighCapacityOverflowPkts": alMatrixDSHighCapacityOverflowPkts,
       "alMatrixDSHighCapacityPkts": alMatrixDSHighCapacityPkts,
       "alMatrixDSHighCapacityOverflowOctets": alMatrixDSHighCapacityOverflowOctets,
       "alMatrixDSHighCapacityOctets": alMatrixDSHighCapacityOctets,
       "alMatrixTopNHighCapacityTable": alMatrixTopNHighCapacityTable,
       "alMatrixTopNHighCapacityEntry": alMatrixTopNHighCapacityEntry,
       "alMatrixTopNHighCapacityProtocolDirLocalIndex": alMatrixTopNHighCapacityProtocolDirLocalIndex,
       "alMatrixTopNHighCapacitySourceAddress": alMatrixTopNHighCapacitySourceAddress,
       "alMatrixTopNHighCapacityDestAddress": alMatrixTopNHighCapacityDestAddress,
       "alMatrixTopNHighCapacityAppProtocolDirLocalIndex": alMatrixTopNHighCapacityAppProtocolDirLocalIndex,
       "alMatrixTopNHighCapacityBasePktRate": alMatrixTopNHighCapacityBasePktRate,
       "alMatrixTopNHighCapacityOverflowPktRate": alMatrixTopNHighCapacityOverflowPktRate,
       "alMatrixTopNHighCapacityPktRate": alMatrixTopNHighCapacityPktRate,
       "alMatrixTopNHighCapacityReverseBasePktRate": alMatrixTopNHighCapacityReverseBasePktRate,
       "alMatrixTopNHighCapacityReverseOverflowPktRate": alMatrixTopNHighCapacityReverseOverflowPktRate,
       "alMatrixTopNHighCapacityReversePktRate": alMatrixTopNHighCapacityReversePktRate,
       "alMatrixTopNHighCapacityBaseOctetRate": alMatrixTopNHighCapacityBaseOctetRate,
       "alMatrixTopNHighCapacityOverflowOctetRate": alMatrixTopNHighCapacityOverflowOctetRate,
       "alMatrixTopNHighCapacityOctetRate": alMatrixTopNHighCapacityOctetRate,
       "alMatrixTopNHighCapacityReverseBaseOctetRate": alMatrixTopNHighCapacityReverseBaseOctetRate,
       "alMatrixTopNHighCapacityReverseOverflowOctetRate": alMatrixTopNHighCapacityReverseOverflowOctetRate,
       "alMatrixTopNHighCapacityReverseOctetRate": alMatrixTopNHighCapacityReverseOctetRate,
       "usrHistoryHighCapacityTable": usrHistoryHighCapacityTable,
       "usrHistoryHighCapacityEntry": usrHistoryHighCapacityEntry,
       "usrHistoryHighCapacityOverflowAbsValue": usrHistoryHighCapacityOverflowAbsValue,
       "usrHistoryHighCapacityAbsValue": usrHistoryHighCapacityAbsValue,
       "hcRMONCapabilities": hcRMONCapabilities,
       "hcRMON": hcRMON,
       "hcRmonMIBCompliances": hcRmonMIBCompliances,
       "hcMediaIndependentCompliance": hcMediaIndependentCompliance,
       "hcRmon1MIBCompliance": hcRmon1MIBCompliance,
       "hcRmon2MIBCompliance": hcRmon2MIBCompliance,
       "hcRmon2MIBApplicationLayerCompliance": hcRmon2MIBApplicationLayerCompliance,
       "hcRmonMIBGroups": hcRmonMIBGroups,
       "mediaIndependentGroup": mediaIndependentGroup,
       "etherStatsHighCapacityGroup": etherStatsHighCapacityGroup,
       "etherHistoryHighCapacityGroup": etherHistoryHighCapacityGroup,
       "hostHighCapacityGroup": hostHighCapacityGroup,
       "hostTopNHighCapacityGroup": hostTopNHighCapacityGroup,
       "matrixHighCapacityGroup": matrixHighCapacityGroup,
       "captureBufferHighCapacityGroup": captureBufferHighCapacityGroup,
       "protocolDistributionHighCapacityGroup": protocolDistributionHighCapacityGroup,
       "nlHostHighCapacityGroup": nlHostHighCapacityGroup,
       "nlMatrixHighCapacityGroup": nlMatrixHighCapacityGroup,
       "nlMatrixTopNHighCapacityGroup": nlMatrixTopNHighCapacityGroup,
       "alHostHighCapacityGroup": alHostHighCapacityGroup,
       "alMatrixHighCapacityGroup": alMatrixHighCapacityGroup,
       "alMatrixTopNHighCapacityGroup": alMatrixTopNHighCapacityGroup,
       "usrHistoryHighCapacityGroup": usrHistoryHighCapacityGroup,
       "hcRMONInformationGroup": hcRMONInformationGroup,
       "mediaIndependentStats": mediaIndependentStats,
       "mediaIndependentTable": mediaIndependentTable,
       "mediaIndependentEntry": mediaIndependentEntry,
       "mediaIndependentIndex": mediaIndependentIndex,
       "mediaIndependentDataSource": mediaIndependentDataSource,
       "mediaIndependentDropEvents": mediaIndependentDropEvents,
       "mediaIndependentDroppedFrames": mediaIndependentDroppedFrames,
       "mediaIndependentInPkts": mediaIndependentInPkts,
       "mediaIndependentInOverflowPkts": mediaIndependentInOverflowPkts,
       "mediaIndependentInHighCapacityPkts": mediaIndependentInHighCapacityPkts,
       "mediaIndependentOutPkts": mediaIndependentOutPkts,
       "mediaIndependentOutOverflowPkts": mediaIndependentOutOverflowPkts,
       "mediaIndependentOutHighCapacityPkts": mediaIndependentOutHighCapacityPkts,
       "mediaIndependentInOctets": mediaIndependentInOctets,
       "mediaIndependentInOverflowOctets": mediaIndependentInOverflowOctets,
       "mediaIndependentInHighCapacityOctets": mediaIndependentInHighCapacityOctets,
       "mediaIndependentOutOctets": mediaIndependentOutOctets,
       "mediaIndependentOutOverflowOctets": mediaIndependentOutOverflowOctets,
       "mediaIndependentOutHighCapacityOctets": mediaIndependentOutHighCapacityOctets,
       "mediaIndependentInNUCastPkts": mediaIndependentInNUCastPkts,
       "mediaIndependentInNUCastOverflowPkts": mediaIndependentInNUCastOverflowPkts,
       "mediaIndependentInNUCastHighCapacityPkts": mediaIndependentInNUCastHighCapacityPkts,
       "mediaIndependentOutNUCastPkts": mediaIndependentOutNUCastPkts,
       "mediaIndependentOutNUCastOverflowPkts": mediaIndependentOutNUCastOverflowPkts,
       "mediaIndependentOutNUCastHighCapacityPkts": mediaIndependentOutNUCastHighCapacityPkts,
       "mediaIndependentInErrors": mediaIndependentInErrors,
       "mediaIndependentOutErrors": mediaIndependentOutErrors,
       "mediaIndependentInputSpeed": mediaIndependentInputSpeed,
       "mediaIndependentOutputSpeed": mediaIndependentOutputSpeed,
       "mediaIndependentDuplexMode": mediaIndependentDuplexMode,
       "mediaIndependentDuplexChanges": mediaIndependentDuplexChanges,
       "mediaIndependentDuplexLastChange": mediaIndependentDuplexLastChange,
       "mediaIndependentOwner": mediaIndependentOwner,
       "mediaIndependentStatus": mediaIndependentStatus}
)
