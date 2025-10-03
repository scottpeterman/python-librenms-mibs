# SNMP MIB module (BENU-KAFKA-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\benuos\BENU-KAFKA-CLIENT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:21:06 2025
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

(benuWAG,) = mibBuilder.importSymbols(
    "BENU-WAG-MIB",
    "benuWAG")

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

benuKafkaClientMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 12)
)
if mibBuilder.loadTexts:
    benuKafkaClientMIB.setRevisions(
        ("2015-10-21 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BKafkaClientObjects_ObjectIdentity = ObjectIdentity
bKafkaClientObjects = _BKafkaClientObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 12, 1)
)
if mibBuilder.loadTexts:
    bKafkaClientObjects.setStatus("current")
_BKafkaClientLatencyTable_Object = MibTable
bKafkaClientLatencyTable = _BKafkaClientLatencyTable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 12, 1, 1)
)
if mibBuilder.loadTexts:
    bKafkaClientLatencyTable.setStatus("current")
_BKafkaClientLatencyEntry_Object = MibTableRow
bKafkaClientLatencyEntry = _BKafkaClientLatencyEntry_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 12, 1, 1, 1)
)
bKafkaClientLatencyEntry.setIndexNames(
    (0, "BENU-KAFKA-CLIENT-MIB", "bKafkaClientLatencyStatsInterval"),
)
if mibBuilder.loadTexts:
    bKafkaClientLatencyEntry.setStatus("current")
_BKafkaClientLatencyStatsInterval_Type = Integer32
_BKafkaClientLatencyStatsInterval_Object = MibTableColumn
bKafkaClientLatencyStatsInterval = _BKafkaClientLatencyStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 12, 1, 1, 1, 1),
    _BKafkaClientLatencyStatsInterval_Type()
)
bKafkaClientLatencyStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bKafkaClientLatencyStatsInterval.setStatus("current")
_BKafkaClientLatencyStatsIntervalDuration_Type = Integer32
_BKafkaClientLatencyStatsIntervalDuration_Object = MibTableColumn
bKafkaClientLatencyStatsIntervalDuration = _BKafkaClientLatencyStatsIntervalDuration_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 12, 1, 1, 1, 2),
    _BKafkaClientLatencyStatsIntervalDuration_Type()
)
bKafkaClientLatencyStatsIntervalDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bKafkaClientLatencyStatsIntervalDuration.setStatus("current")
_BKafkaClientLatencyTotalPktCount_Type = Unsigned32
_BKafkaClientLatencyTotalPktCount_Object = MibTableColumn
bKafkaClientLatencyTotalPktCount = _BKafkaClientLatencyTotalPktCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 12, 1, 1, 1, 3),
    _BKafkaClientLatencyTotalPktCount_Type()
)
bKafkaClientLatencyTotalPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bKafkaClientLatencyTotalPktCount.setStatus("current")
_BKafkaClientLatencyMaxProcessingTime_Type = Unsigned32
_BKafkaClientLatencyMaxProcessingTime_Object = MibTableColumn
bKafkaClientLatencyMaxProcessingTime = _BKafkaClientLatencyMaxProcessingTime_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 12, 1, 1, 1, 4),
    _BKafkaClientLatencyMaxProcessingTime_Type()
)
bKafkaClientLatencyMaxProcessingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bKafkaClientLatencyMaxProcessingTime.setStatus("current")
_BKafkaClientLatencyMinProcessingTime_Type = Unsigned32
_BKafkaClientLatencyMinProcessingTime_Object = MibTableColumn
bKafkaClientLatencyMinProcessingTime = _BKafkaClientLatencyMinProcessingTime_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 12, 1, 1, 1, 5),
    _BKafkaClientLatencyMinProcessingTime_Type()
)
bKafkaClientLatencyMinProcessingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bKafkaClientLatencyMinProcessingTime.setStatus("current")
_BKafkaClientLatencyAvgProcessingTime_Type = Unsigned32
_BKafkaClientLatencyAvgProcessingTime_Object = MibTableColumn
bKafkaClientLatencyAvgProcessingTime = _BKafkaClientLatencyAvgProcessingTime_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 12, 1, 1, 1, 6),
    _BKafkaClientLatencyAvgProcessingTime_Type()
)
bKafkaClientLatencyAvgProcessingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bKafkaClientLatencyAvgProcessingTime.setStatus("current")
_BKafkaClientLatencyProcessTimeMorethan1MSPktCount_Type = Unsigned32
_BKafkaClientLatencyProcessTimeMorethan1MSPktCount_Object = MibTableColumn
bKafkaClientLatencyProcessTimeMorethan1MSPktCount = _BKafkaClientLatencyProcessTimeMorethan1MSPktCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 12, 1, 1, 1, 7),
    _BKafkaClientLatencyProcessTimeMorethan1MSPktCount_Type()
)
bKafkaClientLatencyProcessTimeMorethan1MSPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bKafkaClientLatencyProcessTimeMorethan1MSPktCount.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BENU-KAFKA-CLIENT-MIB",
    **{"benuKafkaClientMIB": benuKafkaClientMIB,
       "bKafkaClientObjects": bKafkaClientObjects,
       "bKafkaClientLatencyTable": bKafkaClientLatencyTable,
       "bKafkaClientLatencyEntry": bKafkaClientLatencyEntry,
       "bKafkaClientLatencyStatsInterval": bKafkaClientLatencyStatsInterval,
       "bKafkaClientLatencyStatsIntervalDuration": bKafkaClientLatencyStatsIntervalDuration,
       "bKafkaClientLatencyTotalPktCount": bKafkaClientLatencyTotalPktCount,
       "bKafkaClientLatencyMaxProcessingTime": bKafkaClientLatencyMaxProcessingTime,
       "bKafkaClientLatencyMinProcessingTime": bKafkaClientLatencyMinProcessingTime,
       "bKafkaClientLatencyAvgProcessingTime": bKafkaClientLatencyAvgProcessingTime,
       "bKafkaClientLatencyProcessTimeMorethan1MSPktCount": bKafkaClientLatencyProcessTimeMorethan1MSPktCount}
)
