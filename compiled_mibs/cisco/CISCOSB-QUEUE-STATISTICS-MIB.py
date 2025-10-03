# SNMP MIB module (CISCOSB-QUEUE-STATISTICS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cisco\CISCOSB-QUEUE-STATISTICS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:29:27 2025
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

(switch001,) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "switch001")

(StatisticsDPType,) = mibBuilder.importSymbols(
    "CISCOSB-POLICY-MIB",
    "StatisticsDPType")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

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

rlQueueStatistics = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 233)
)
if mibBuilder.loadTexts:
    rlQueueStatistics.setRevisions(
        ("2016-07-07 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlInterfaceQueueStatisticsClear_Type = InterfaceIndexOrZero
_RlInterfaceQueueStatisticsClear_Object = MibScalar
rlInterfaceQueueStatisticsClear = _RlInterfaceQueueStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 233, 1),
    _RlInterfaceQueueStatisticsClear_Type()
)
rlInterfaceQueueStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlInterfaceQueueStatisticsClear.setStatus("current")
_RlInterfaceQueueStatisticsTable_Object = MibTable
rlInterfaceQueueStatisticsTable = _RlInterfaceQueueStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 233, 2)
)
if mibBuilder.loadTexts:
    rlInterfaceQueueStatisticsTable.setStatus("current")
_RlInterfaceQueueStatisticsEntry_Object = MibTableRow
rlInterfaceQueueStatisticsEntry = _RlInterfaceQueueStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 233, 2, 1)
)
rlInterfaceQueueStatisticsEntry.setIndexNames(
    (0, "CISCOSB-QUEUE-STATISTICS-MIB", "rlInterfaceQueueStatisticsIfIndex"),
    (0, "CISCOSB-QUEUE-STATISTICS-MIB", "rlInterfaceQueueStatisticsQueue"),
    (0, "CISCOSB-QUEUE-STATISTICS-MIB", "rlInterfaceQueueStatisticsDP"),
)
if mibBuilder.loadTexts:
    rlInterfaceQueueStatisticsEntry.setStatus("current")
_RlInterfaceQueueStatisticsIfIndex_Type = InterfaceIndex
_RlInterfaceQueueStatisticsIfIndex_Object = MibTableColumn
rlInterfaceQueueStatisticsIfIndex = _RlInterfaceQueueStatisticsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 233, 2, 1, 1),
    _RlInterfaceQueueStatisticsIfIndex_Type()
)
rlInterfaceQueueStatisticsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlInterfaceQueueStatisticsIfIndex.setStatus("current")


class _RlInterfaceQueueStatisticsQueue_Type(Integer32):
    """Custom type rlInterfaceQueueStatisticsQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RlInterfaceQueueStatisticsQueue_Type.__name__ = "Integer32"
_RlInterfaceQueueStatisticsQueue_Object = MibTableColumn
rlInterfaceQueueStatisticsQueue = _RlInterfaceQueueStatisticsQueue_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 233, 2, 1, 2),
    _RlInterfaceQueueStatisticsQueue_Type()
)
rlInterfaceQueueStatisticsQueue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlInterfaceQueueStatisticsQueue.setStatus("current")
_RlInterfaceQueueStatisticsDP_Type = StatisticsDPType
_RlInterfaceQueueStatisticsDP_Object = MibTableColumn
rlInterfaceQueueStatisticsDP = _RlInterfaceQueueStatisticsDP_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 233, 2, 1, 3),
    _RlInterfaceQueueStatisticsDP_Type()
)
rlInterfaceQueueStatisticsDP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlInterfaceQueueStatisticsDP.setStatus("current")
_RlInterfaceQueueStatisticsTxPackets_Type = Counter64
_RlInterfaceQueueStatisticsTxPackets_Object = MibTableColumn
rlInterfaceQueueStatisticsTxPackets = _RlInterfaceQueueStatisticsTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 233, 2, 1, 4),
    _RlInterfaceQueueStatisticsTxPackets_Type()
)
rlInterfaceQueueStatisticsTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInterfaceQueueStatisticsTxPackets.setStatus("current")
_RlInterfaceQueueStatisticsTxBytes_Type = Counter64
_RlInterfaceQueueStatisticsTxBytes_Object = MibTableColumn
rlInterfaceQueueStatisticsTxBytes = _RlInterfaceQueueStatisticsTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 233, 2, 1, 5),
    _RlInterfaceQueueStatisticsTxBytes_Type()
)
rlInterfaceQueueStatisticsTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInterfaceQueueStatisticsTxBytes.setStatus("current")
_RlInterfaceQueueStatisticsDroppedPackets_Type = Counter64
_RlInterfaceQueueStatisticsDroppedPackets_Object = MibTableColumn
rlInterfaceQueueStatisticsDroppedPackets = _RlInterfaceQueueStatisticsDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 233, 2, 1, 6),
    _RlInterfaceQueueStatisticsDroppedPackets_Type()
)
rlInterfaceQueueStatisticsDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInterfaceQueueStatisticsDroppedPackets.setStatus("current")
_RlInterfaceQueueStatisticsDroppedBytes_Type = Counter64
_RlInterfaceQueueStatisticsDroppedBytes_Object = MibTableColumn
rlInterfaceQueueStatisticsDroppedBytes = _RlInterfaceQueueStatisticsDroppedBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 233, 2, 1, 7),
    _RlInterfaceQueueStatisticsDroppedBytes_Type()
)
rlInterfaceQueueStatisticsDroppedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInterfaceQueueStatisticsDroppedBytes.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-QUEUE-STATISTICS-MIB",
    **{"rlQueueStatistics": rlQueueStatistics,
       "rlInterfaceQueueStatisticsClear": rlInterfaceQueueStatisticsClear,
       "rlInterfaceQueueStatisticsTable": rlInterfaceQueueStatisticsTable,
       "rlInterfaceQueueStatisticsEntry": rlInterfaceQueueStatisticsEntry,
       "rlInterfaceQueueStatisticsIfIndex": rlInterfaceQueueStatisticsIfIndex,
       "rlInterfaceQueueStatisticsQueue": rlInterfaceQueueStatisticsQueue,
       "rlInterfaceQueueStatisticsDP": rlInterfaceQueueStatisticsDP,
       "rlInterfaceQueueStatisticsTxPackets": rlInterfaceQueueStatisticsTxPackets,
       "rlInterfaceQueueStatisticsTxBytes": rlInterfaceQueueStatisticsTxBytes,
       "rlInterfaceQueueStatisticsDroppedPackets": rlInterfaceQueueStatisticsDroppedPackets,
       "rlInterfaceQueueStatisticsDroppedBytes": rlInterfaceQueueStatisticsDroppedBytes}
)
