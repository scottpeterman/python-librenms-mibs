# SNMP MIB module (JUNIPER-FABRIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junos\JUNIPER-FABRIC-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:03:10 2025
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

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(jnxFabricMibRoot,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxFabricMibRoot")

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

jnxFabricMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 81, 1)
)
if mibBuilder.loadTexts:
    jnxFabricMib.setRevisions(
        ("2014-10-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class JnxFabricType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("switch-fabric", 1),
          ("linecard", 2))
    )



class JnxFabricStatisticsPriority(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("high", 0),
          ("low", 1),
          ("all", 255))
    )



# MIB Managed Objects in the order of their OIDs

_JnxFabricMibObjects_ObjectIdentity = ObjectIdentity
jnxFabricMibObjects = _JnxFabricMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 81, 1, 1)
)
_JnxFabricStatistics_ObjectIdentity = ObjectIdentity
jnxFabricStatistics = _JnxFabricStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 81, 1, 1, 1)
)
_JnxFabricSourceStatisticsTable_Object = MibTable
jnxFabricSourceStatisticsTable = _JnxFabricSourceStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 81, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxFabricSourceStatisticsTable.setStatus("current")
_JnxFabricSourceStatisticsEntry_Object = MibTableRow
jnxFabricSourceStatisticsEntry = _JnxFabricSourceStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 81, 1, 1, 1, 1, 1)
)
jnxFabricSourceStatisticsEntry.setIndexNames(
    (0, "JUNIPER-FABRIC-MIB", "jnxFabricSourceType"),
    (0, "JUNIPER-FABRIC-MIB", "jnxFabricSourceSlot"),
    (0, "JUNIPER-FABRIC-MIB", "jnxFabricSourcePfe"),
    (0, "JUNIPER-FABRIC-MIB", "jnxFabricDestinationType"),
    (0, "JUNIPER-FABRIC-MIB", "jnxFabricDestinationSlot"),
    (0, "JUNIPER-FABRIC-MIB", "jnxFabricDestinationPfe"),
    (0, "JUNIPER-FABRIC-MIB", "jnxFabricSourceStatisticsPriority"),
)
if mibBuilder.loadTexts:
    jnxFabricSourceStatisticsEntry.setStatus("current")
_JnxFabricSourceType_Type = JnxFabricType
_JnxFabricSourceType_Object = MibTableColumn
jnxFabricSourceType = _JnxFabricSourceType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 81, 1, 1, 1, 1, 1, 1),
    _JnxFabricSourceType_Type()
)
jnxFabricSourceType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxFabricSourceType.setStatus("current")


class _JnxFabricSourceSlot_Type(Integer32):
    """Custom type jnxFabricSourceSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
        ValueRangeConstraint(65535, 65535),
    )


_JnxFabricSourceSlot_Type.__name__ = "Integer32"
_JnxFabricSourceSlot_Object = MibTableColumn
jnxFabricSourceSlot = _JnxFabricSourceSlot_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 81, 1, 1, 1, 1, 1, 2),
    _JnxFabricSourceSlot_Type()
)
jnxFabricSourceSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxFabricSourceSlot.setStatus("current")


class _JnxFabricSourcePfe_Type(Integer32):
    """Custom type jnxFabricSourcePfe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
        ValueRangeConstraint(65535, 65535),
    )


_JnxFabricSourcePfe_Type.__name__ = "Integer32"
_JnxFabricSourcePfe_Object = MibTableColumn
jnxFabricSourcePfe = _JnxFabricSourcePfe_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 81, 1, 1, 1, 1, 1, 3),
    _JnxFabricSourcePfe_Type()
)
jnxFabricSourcePfe.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxFabricSourcePfe.setStatus("current")
_JnxFabricDestinationType_Type = JnxFabricType
_JnxFabricDestinationType_Object = MibTableColumn
jnxFabricDestinationType = _JnxFabricDestinationType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 81, 1, 1, 1, 1, 1, 4),
    _JnxFabricDestinationType_Type()
)
jnxFabricDestinationType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxFabricDestinationType.setStatus("current")


class _JnxFabricDestinationSlot_Type(Integer32):
    """Custom type jnxFabricDestinationSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
        ValueRangeConstraint(65535, 65535),
    )


_JnxFabricDestinationSlot_Type.__name__ = "Integer32"
_JnxFabricDestinationSlot_Object = MibTableColumn
jnxFabricDestinationSlot = _JnxFabricDestinationSlot_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 81, 1, 1, 1, 1, 1, 5),
    _JnxFabricDestinationSlot_Type()
)
jnxFabricDestinationSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxFabricDestinationSlot.setStatus("current")


class _JnxFabricDestinationPfe_Type(Integer32):
    """Custom type jnxFabricDestinationPfe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
        ValueRangeConstraint(65535, 65535),
    )


_JnxFabricDestinationPfe_Type.__name__ = "Integer32"
_JnxFabricDestinationPfe_Object = MibTableColumn
jnxFabricDestinationPfe = _JnxFabricDestinationPfe_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 81, 1, 1, 1, 1, 1, 6),
    _JnxFabricDestinationPfe_Type()
)
jnxFabricDestinationPfe.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxFabricDestinationPfe.setStatus("current")
_JnxFabricSourceStatisticsPriority_Type = JnxFabricStatisticsPriority
_JnxFabricSourceStatisticsPriority_Object = MibTableColumn
jnxFabricSourceStatisticsPriority = _JnxFabricSourceStatisticsPriority_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 81, 1, 1, 1, 1, 1, 7),
    _JnxFabricSourceStatisticsPriority_Type()
)
jnxFabricSourceStatisticsPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxFabricSourceStatisticsPriority.setStatus("current")
_JnxFabricSourceStatisticsPackets_Type = Counter64
_JnxFabricSourceStatisticsPackets_Object = MibTableColumn
jnxFabricSourceStatisticsPackets = _JnxFabricSourceStatisticsPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 81, 1, 1, 1, 1, 1, 8),
    _JnxFabricSourceStatisticsPackets_Type()
)
jnxFabricSourceStatisticsPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricSourceStatisticsPackets.setStatus("current")
_JnxFabricSourceStatisticsBytes_Type = Counter64
_JnxFabricSourceStatisticsBytes_Object = MibTableColumn
jnxFabricSourceStatisticsBytes = _JnxFabricSourceStatisticsBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 81, 1, 1, 1, 1, 1, 9),
    _JnxFabricSourceStatisticsBytes_Type()
)
jnxFabricSourceStatisticsBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricSourceStatisticsBytes.setStatus("current")
_JnxFabricSourceStatisticsPps_Type = CounterBasedGauge64
_JnxFabricSourceStatisticsPps_Object = MibTableColumn
jnxFabricSourceStatisticsPps = _JnxFabricSourceStatisticsPps_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 81, 1, 1, 1, 1, 1, 10),
    _JnxFabricSourceStatisticsPps_Type()
)
jnxFabricSourceStatisticsPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricSourceStatisticsPps.setStatus("current")
_JnxFabricSourceStatisticsBps_Type = CounterBasedGauge64
_JnxFabricSourceStatisticsBps_Object = MibTableColumn
jnxFabricSourceStatisticsBps = _JnxFabricSourceStatisticsBps_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 81, 1, 1, 1, 1, 1, 11),
    _JnxFabricSourceStatisticsBps_Type()
)
jnxFabricSourceStatisticsBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricSourceStatisticsBps.setStatus("current")
_JnxFabricSourceStatisticsDropPackets_Type = Counter64
_JnxFabricSourceStatisticsDropPackets_Object = MibTableColumn
jnxFabricSourceStatisticsDropPackets = _JnxFabricSourceStatisticsDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 81, 1, 1, 1, 1, 1, 12),
    _JnxFabricSourceStatisticsDropPackets_Type()
)
jnxFabricSourceStatisticsDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricSourceStatisticsDropPackets.setStatus("current")
_JnxFabricSourceStatisticsDropBytes_Type = Counter64
_JnxFabricSourceStatisticsDropBytes_Object = MibTableColumn
jnxFabricSourceStatisticsDropBytes = _JnxFabricSourceStatisticsDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 81, 1, 1, 1, 1, 1, 13),
    _JnxFabricSourceStatisticsDropBytes_Type()
)
jnxFabricSourceStatisticsDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricSourceStatisticsDropBytes.setStatus("current")
_JnxFabricSourceStatisticsDropPps_Type = CounterBasedGauge64
_JnxFabricSourceStatisticsDropPps_Object = MibTableColumn
jnxFabricSourceStatisticsDropPps = _JnxFabricSourceStatisticsDropPps_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 81, 1, 1, 1, 1, 1, 14),
    _JnxFabricSourceStatisticsDropPps_Type()
)
jnxFabricSourceStatisticsDropPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricSourceStatisticsDropPps.setStatus("current")
_JnxFabricSourceStatisticsDropBps_Type = CounterBasedGauge64
_JnxFabricSourceStatisticsDropBps_Object = MibTableColumn
jnxFabricSourceStatisticsDropBps = _JnxFabricSourceStatisticsDropBps_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 81, 1, 1, 1, 1, 1, 15),
    _JnxFabricSourceStatisticsDropBps_Type()
)
jnxFabricSourceStatisticsDropBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricSourceStatisticsDropBps.setStatus("current")
_JnxFabricSourceStatisticsQueueDepthAverage_Type = CounterBasedGauge64
_JnxFabricSourceStatisticsQueueDepthAverage_Object = MibTableColumn
jnxFabricSourceStatisticsQueueDepthAverage = _JnxFabricSourceStatisticsQueueDepthAverage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 81, 1, 1, 1, 1, 1, 16),
    _JnxFabricSourceStatisticsQueueDepthAverage_Type()
)
jnxFabricSourceStatisticsQueueDepthAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricSourceStatisticsQueueDepthAverage.setStatus("current")
_JnxFabricSourceStatisticsQueueDepthCurrent_Type = CounterBasedGauge64
_JnxFabricSourceStatisticsQueueDepthCurrent_Object = MibTableColumn
jnxFabricSourceStatisticsQueueDepthCurrent = _JnxFabricSourceStatisticsQueueDepthCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 81, 1, 1, 1, 1, 1, 17),
    _JnxFabricSourceStatisticsQueueDepthCurrent_Type()
)
jnxFabricSourceStatisticsQueueDepthCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricSourceStatisticsQueueDepthCurrent.setStatus("current")
_JnxFabricSourceStatisticsQueueDepthPeak_Type = CounterBasedGauge64
_JnxFabricSourceStatisticsQueueDepthPeak_Object = MibTableColumn
jnxFabricSourceStatisticsQueueDepthPeak = _JnxFabricSourceStatisticsQueueDepthPeak_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 81, 1, 1, 1, 1, 1, 18),
    _JnxFabricSourceStatisticsQueueDepthPeak_Type()
)
jnxFabricSourceStatisticsQueueDepthPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricSourceStatisticsQueueDepthPeak.setStatus("current")
_JnxFabricSourceStatisticsQueueDepthMaximum_Type = CounterBasedGauge64
_JnxFabricSourceStatisticsQueueDepthMaximum_Object = MibTableColumn
jnxFabricSourceStatisticsQueueDepthMaximum = _JnxFabricSourceStatisticsQueueDepthMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 81, 1, 1, 1, 1, 1, 19),
    _JnxFabricSourceStatisticsQueueDepthMaximum_Type()
)
jnxFabricSourceStatisticsQueueDepthMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricSourceStatisticsQueueDepthMaximum.setStatus("current")
_JnxFabricSourceStatisticsErrorPackets_Type = Counter64
_JnxFabricSourceStatisticsErrorPackets_Object = MibTableColumn
jnxFabricSourceStatisticsErrorPackets = _JnxFabricSourceStatisticsErrorPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 81, 1, 1, 1, 1, 1, 20),
    _JnxFabricSourceStatisticsErrorPackets_Type()
)
jnxFabricSourceStatisticsErrorPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricSourceStatisticsErrorPackets.setStatus("current")
_JnxFabricSourceStatisticsErrorPps_Type = CounterBasedGauge64
_JnxFabricSourceStatisticsErrorPps_Object = MibTableColumn
jnxFabricSourceStatisticsErrorPps = _JnxFabricSourceStatisticsErrorPps_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 81, 1, 1, 1, 1, 1, 21),
    _JnxFabricSourceStatisticsErrorPps_Type()
)
jnxFabricSourceStatisticsErrorPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricSourceStatisticsErrorPps.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-FABRIC-MIB",
    **{"JnxFabricType": JnxFabricType,
       "JnxFabricStatisticsPriority": JnxFabricStatisticsPriority,
       "jnxFabricMib": jnxFabricMib,
       "jnxFabricMibObjects": jnxFabricMibObjects,
       "jnxFabricStatistics": jnxFabricStatistics,
       "jnxFabricSourceStatisticsTable": jnxFabricSourceStatisticsTable,
       "jnxFabricSourceStatisticsEntry": jnxFabricSourceStatisticsEntry,
       "jnxFabricSourceType": jnxFabricSourceType,
       "jnxFabricSourceSlot": jnxFabricSourceSlot,
       "jnxFabricSourcePfe": jnxFabricSourcePfe,
       "jnxFabricDestinationType": jnxFabricDestinationType,
       "jnxFabricDestinationSlot": jnxFabricDestinationSlot,
       "jnxFabricDestinationPfe": jnxFabricDestinationPfe,
       "jnxFabricSourceStatisticsPriority": jnxFabricSourceStatisticsPriority,
       "jnxFabricSourceStatisticsPackets": jnxFabricSourceStatisticsPackets,
       "jnxFabricSourceStatisticsBytes": jnxFabricSourceStatisticsBytes,
       "jnxFabricSourceStatisticsPps": jnxFabricSourceStatisticsPps,
       "jnxFabricSourceStatisticsBps": jnxFabricSourceStatisticsBps,
       "jnxFabricSourceStatisticsDropPackets": jnxFabricSourceStatisticsDropPackets,
       "jnxFabricSourceStatisticsDropBytes": jnxFabricSourceStatisticsDropBytes,
       "jnxFabricSourceStatisticsDropPps": jnxFabricSourceStatisticsDropPps,
       "jnxFabricSourceStatisticsDropBps": jnxFabricSourceStatisticsDropBps,
       "jnxFabricSourceStatisticsQueueDepthAverage": jnxFabricSourceStatisticsQueueDepthAverage,
       "jnxFabricSourceStatisticsQueueDepthCurrent": jnxFabricSourceStatisticsQueueDepthCurrent,
       "jnxFabricSourceStatisticsQueueDepthPeak": jnxFabricSourceStatisticsQueueDepthPeak,
       "jnxFabricSourceStatisticsQueueDepthMaximum": jnxFabricSourceStatisticsQueueDepthMaximum,
       "jnxFabricSourceStatisticsErrorPackets": jnxFabricSourceStatisticsErrorPackets,
       "jnxFabricSourceStatisticsErrorPps": jnxFabricSourceStatisticsErrorPps}
)
