# SNMP MIB module (TN-S-FLOW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TN-S-FLOW-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:32:19 2025
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
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

(tnProducts,) = mibBuilder.importSymbols(
    "TRANSITION-SMI",
    "tnProducts")


# MODULE-IDENTITY

tnSFlowMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 119)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnSFlowMIBObjects_ObjectIdentity = ObjectIdentity
tnSFlowMIBObjects = _TnSFlowMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 119, 1)
)
_TnSFlowMIBMgmt_ObjectIdentity = ObjectIdentity
tnSFlowMIBMgmt = _TnSFlowMIBMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 119, 1, 1)
)
_TnSFlowReceiverConfigTable_Object = MibTable
tnSFlowReceiverConfigTable = _TnSFlowReceiverConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 119, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tnSFlowReceiverConfigTable.setStatus("current")
_TnSFlowReceiverConfigEntry_Object = MibTableRow
tnSFlowReceiverConfigEntry = _TnSFlowReceiverConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 119, 1, 1, 1, 1)
)
tnSFlowReceiverConfigEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    tnSFlowReceiverConfigEntry.setStatus("current")
_TnSFlowReceiverOwner_Type = DisplayString
_TnSFlowReceiverOwner_Object = MibTableColumn
tnSFlowReceiverOwner = _TnSFlowReceiverOwner_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 119, 1, 1, 1, 1, 1),
    _TnSFlowReceiverOwner_Type()
)
tnSFlowReceiverOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSFlowReceiverOwner.setStatus("current")
_TnSFlowReceiverRelease_Type = TruthValue
_TnSFlowReceiverRelease_Object = MibTableColumn
tnSFlowReceiverRelease = _TnSFlowReceiverRelease_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 119, 1, 1, 1, 1, 2),
    _TnSFlowReceiverRelease_Type()
)
tnSFlowReceiverRelease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSFlowReceiverRelease.setStatus("current")
_TnSFlowReceiverAddressType_Type = InetAddressType
_TnSFlowReceiverAddressType_Object = MibTableColumn
tnSFlowReceiverAddressType = _TnSFlowReceiverAddressType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 119, 1, 1, 1, 1, 3),
    _TnSFlowReceiverAddressType_Type()
)
tnSFlowReceiverAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSFlowReceiverAddressType.setStatus("current")
_TnSFlowReceiverAddress_Type = InetAddress
_TnSFlowReceiverAddress_Object = MibTableColumn
tnSFlowReceiverAddress = _TnSFlowReceiverAddress_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 119, 1, 1, 1, 1, 4),
    _TnSFlowReceiverAddress_Type()
)
tnSFlowReceiverAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSFlowReceiverAddress.setStatus("current")


class _TnSFlowReceiverUDPPort_Type(Integer32):
    """Custom type tnSFlowReceiverUDPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnSFlowReceiverUDPPort_Type.__name__ = "Integer32"
_TnSFlowReceiverUDPPort_Object = MibTableColumn
tnSFlowReceiverUDPPort = _TnSFlowReceiverUDPPort_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 119, 1, 1, 1, 1, 5),
    _TnSFlowReceiverUDPPort_Type()
)
tnSFlowReceiverUDPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSFlowReceiverUDPPort.setStatus("current")


class _TnSFlowReceiverTimeout_Type(Unsigned32):
    """Custom type tnSFlowReceiverTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TnSFlowReceiverTimeout_Type.__name__ = "Unsigned32"
_TnSFlowReceiverTimeout_Object = MibTableColumn
tnSFlowReceiverTimeout = _TnSFlowReceiverTimeout_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 119, 1, 1, 1, 1, 6),
    _TnSFlowReceiverTimeout_Type()
)
tnSFlowReceiverTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSFlowReceiverTimeout.setStatus("current")


class _TnSFlowReceiverMaxDatagramSize_Type(Integer32):
    """Custom type tnSFlowReceiverMaxDatagramSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 1468),
    )


_TnSFlowReceiverMaxDatagramSize_Type.__name__ = "Integer32"
_TnSFlowReceiverMaxDatagramSize_Object = MibTableColumn
tnSFlowReceiverMaxDatagramSize = _TnSFlowReceiverMaxDatagramSize_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 119, 1, 1, 1, 1, 7),
    _TnSFlowReceiverMaxDatagramSize_Type()
)
tnSFlowReceiverMaxDatagramSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSFlowReceiverMaxDatagramSize.setStatus("current")
_TnSFlowPortConfigTable_Object = MibTable
tnSFlowPortConfigTable = _TnSFlowPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 119, 1, 1, 2)
)
if mibBuilder.loadTexts:
    tnSFlowPortConfigTable.setStatus("current")
_TnSFlowPortConfigEntry_Object = MibTableRow
tnSFlowPortConfigEntry = _TnSFlowPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 119, 1, 1, 2, 1)
)
tnSFlowPortConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnSFlowPortConfigEntry.setStatus("current")
_TnSFlowSamplerEnabled_Type = TruthValue
_TnSFlowSamplerEnabled_Object = MibTableColumn
tnSFlowSamplerEnabled = _TnSFlowSamplerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 119, 1, 1, 2, 1, 1),
    _TnSFlowSamplerEnabled_Type()
)
tnSFlowSamplerEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSFlowSamplerEnabled.setStatus("current")


class _TnSFlowFlowRate_Type(Unsigned32):
    """Custom type tnSFlowFlowRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TnSFlowFlowRate_Type.__name__ = "Unsigned32"
_TnSFlowFlowRate_Object = MibTableColumn
tnSFlowFlowRate = _TnSFlowFlowRate_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 119, 1, 1, 2, 1, 2),
    _TnSFlowFlowRate_Type()
)
tnSFlowFlowRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSFlowFlowRate.setStatus("current")


class _TnSFlowFlowMaxHeader_Type(Integer32):
    """Custom type tnSFlowFlowMaxHeader based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(14, 200),
    )


_TnSFlowFlowMaxHeader_Type.__name__ = "Integer32"
_TnSFlowFlowMaxHeader_Object = MibTableColumn
tnSFlowFlowMaxHeader = _TnSFlowFlowMaxHeader_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 119, 1, 1, 2, 1, 3),
    _TnSFlowFlowMaxHeader_Type()
)
tnSFlowFlowMaxHeader.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSFlowFlowMaxHeader.setStatus("current")
_TnSFlowCounterEnabled_Type = TruthValue
_TnSFlowCounterEnabled_Object = MibTableColumn
tnSFlowCounterEnabled = _TnSFlowCounterEnabled_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 119, 1, 1, 2, 1, 4),
    _TnSFlowCounterEnabled_Type()
)
tnSFlowCounterEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSFlowCounterEnabled.setStatus("current")


class _TnSFlowCounterInteval_Type(Integer32):
    """Custom type tnSFlowCounterInteval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_TnSFlowCounterInteval_Type.__name__ = "Integer32"
_TnSFlowCounterInteval_Object = MibTableColumn
tnSFlowCounterInteval = _TnSFlowCounterInteval_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 119, 1, 1, 2, 1, 5),
    _TnSFlowCounterInteval_Type()
)
tnSFlowCounterInteval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSFlowCounterInteval.setStatus("current")
_TnSFlowReceiverStatisticsTable_Object = MibTable
tnSFlowReceiverStatisticsTable = _TnSFlowReceiverStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 119, 1, 1, 3)
)
if mibBuilder.loadTexts:
    tnSFlowReceiverStatisticsTable.setStatus("current")
_TnSFlowReceiverStatisticsEntry_Object = MibTableRow
tnSFlowReceiverStatisticsEntry = _TnSFlowReceiverStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 119, 1, 1, 3, 1)
)
tnSFlowReceiverStatisticsEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    tnSFlowReceiverStatisticsEntry.setStatus("current")
_TnSFlowReceiverTxSuccesses_Type = Unsigned32
_TnSFlowReceiverTxSuccesses_Object = MibTableColumn
tnSFlowReceiverTxSuccesses = _TnSFlowReceiverTxSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 119, 1, 1, 3, 1, 1),
    _TnSFlowReceiverTxSuccesses_Type()
)
tnSFlowReceiverTxSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSFlowReceiverTxSuccesses.setStatus("current")
_TnSFlowReceiverTxErrors_Type = Unsigned32
_TnSFlowReceiverTxErrors_Object = MibTableColumn
tnSFlowReceiverTxErrors = _TnSFlowReceiverTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 119, 1, 1, 3, 1, 2),
    _TnSFlowReceiverTxErrors_Type()
)
tnSFlowReceiverTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSFlowReceiverTxErrors.setStatus("current")
_TnSFlowReceiverFlowSamples_Type = Unsigned32
_TnSFlowReceiverFlowSamples_Object = MibTableColumn
tnSFlowReceiverFlowSamples = _TnSFlowReceiverFlowSamples_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 119, 1, 1, 3, 1, 3),
    _TnSFlowReceiverFlowSamples_Type()
)
tnSFlowReceiverFlowSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSFlowReceiverFlowSamples.setStatus("current")
_TnSFlowReceiverCounterSamples_Type = Unsigned32
_TnSFlowReceiverCounterSamples_Object = MibTableColumn
tnSFlowReceiverCounterSamples = _TnSFlowReceiverCounterSamples_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 119, 1, 1, 3, 1, 4),
    _TnSFlowReceiverCounterSamples_Type()
)
tnSFlowReceiverCounterSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSFlowReceiverCounterSamples.setStatus("current")
_TnSFlowClearReceiverStatistics_Type = TruthValue
_TnSFlowClearReceiverStatistics_Object = MibTableColumn
tnSFlowClearReceiverStatistics = _TnSFlowClearReceiverStatistics_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 119, 1, 1, 3, 1, 5),
    _TnSFlowClearReceiverStatistics_Type()
)
tnSFlowClearReceiverStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSFlowClearReceiverStatistics.setStatus("current")
_TnSFlowPortStatisticsTable_Object = MibTable
tnSFlowPortStatisticsTable = _TnSFlowPortStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 119, 1, 1, 4)
)
if mibBuilder.loadTexts:
    tnSFlowPortStatisticsTable.setStatus("current")
_TnSFlowPortStatisticsEntry_Object = MibTableRow
tnSFlowPortStatisticsEntry = _TnSFlowPortStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 119, 1, 1, 4, 1)
)
tnSFlowPortStatisticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnSFlowPortStatisticsEntry.setStatus("current")
_TnSFlowRxSamples_Type = Unsigned32
_TnSFlowRxSamples_Object = MibTableColumn
tnSFlowRxSamples = _TnSFlowRxSamples_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 119, 1, 1, 4, 1, 1),
    _TnSFlowRxSamples_Type()
)
tnSFlowRxSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSFlowRxSamples.setStatus("current")
_TnSFlowTxSamples_Type = Unsigned32
_TnSFlowTxSamples_Object = MibTableColumn
tnSFlowTxSamples = _TnSFlowTxSamples_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 119, 1, 1, 4, 1, 2),
    _TnSFlowTxSamples_Type()
)
tnSFlowTxSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSFlowTxSamples.setStatus("current")
_TnSFlowCounterSamples_Type = Unsigned32
_TnSFlowCounterSamples_Object = MibTableColumn
tnSFlowCounterSamples = _TnSFlowCounterSamples_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 119, 1, 1, 4, 1, 3),
    _TnSFlowCounterSamples_Type()
)
tnSFlowCounterSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSFlowCounterSamples.setStatus("current")
_TnSFlowClearPortsStatistics_Type = TruthValue
_TnSFlowClearPortsStatistics_Object = MibTableColumn
tnSFlowClearPortsStatistics = _TnSFlowClearPortsStatistics_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 119, 1, 1, 4, 1, 4),
    _TnSFlowClearPortsStatistics_Type()
)
tnSFlowClearPortsStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSFlowClearPortsStatistics.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-S-FLOW-MIB",
    **{"tnSFlowMIB": tnSFlowMIB,
       "tnSFlowMIBObjects": tnSFlowMIBObjects,
       "tnSFlowMIBMgmt": tnSFlowMIBMgmt,
       "tnSFlowReceiverConfigTable": tnSFlowReceiverConfigTable,
       "tnSFlowReceiverConfigEntry": tnSFlowReceiverConfigEntry,
       "tnSFlowReceiverOwner": tnSFlowReceiverOwner,
       "tnSFlowReceiverRelease": tnSFlowReceiverRelease,
       "tnSFlowReceiverAddressType": tnSFlowReceiverAddressType,
       "tnSFlowReceiverAddress": tnSFlowReceiverAddress,
       "tnSFlowReceiverUDPPort": tnSFlowReceiverUDPPort,
       "tnSFlowReceiverTimeout": tnSFlowReceiverTimeout,
       "tnSFlowReceiverMaxDatagramSize": tnSFlowReceiverMaxDatagramSize,
       "tnSFlowPortConfigTable": tnSFlowPortConfigTable,
       "tnSFlowPortConfigEntry": tnSFlowPortConfigEntry,
       "tnSFlowSamplerEnabled": tnSFlowSamplerEnabled,
       "tnSFlowFlowRate": tnSFlowFlowRate,
       "tnSFlowFlowMaxHeader": tnSFlowFlowMaxHeader,
       "tnSFlowCounterEnabled": tnSFlowCounterEnabled,
       "tnSFlowCounterInteval": tnSFlowCounterInteval,
       "tnSFlowReceiverStatisticsTable": tnSFlowReceiverStatisticsTable,
       "tnSFlowReceiverStatisticsEntry": tnSFlowReceiverStatisticsEntry,
       "tnSFlowReceiverTxSuccesses": tnSFlowReceiverTxSuccesses,
       "tnSFlowReceiverTxErrors": tnSFlowReceiverTxErrors,
       "tnSFlowReceiverFlowSamples": tnSFlowReceiverFlowSamples,
       "tnSFlowReceiverCounterSamples": tnSFlowReceiverCounterSamples,
       "tnSFlowClearReceiverStatistics": tnSFlowClearReceiverStatistics,
       "tnSFlowPortStatisticsTable": tnSFlowPortStatisticsTable,
       "tnSFlowPortStatisticsEntry": tnSFlowPortStatisticsEntry,
       "tnSFlowRxSamples": tnSFlowRxSamples,
       "tnSFlowTxSamples": tnSFlowTxSamples,
       "tnSFlowCounterSamples": tnSFlowCounterSamples,
       "tnSFlowClearPortsStatistics": tnSFlowClearPortsStatistics}
)
