# SNMP MIB module (SL-ETH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\packetlight\SL-ETH-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:19:49 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(PerfCurrentCount,
 PerfIntervalCount,
 PerfTotalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount",
    "PerfTotalCount")

(slService,) = mibBuilder.importSymbols(
    "SL-NE-MIB",
    "slService")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

slEthernet = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EthConfigTable_Object = MibTable
ethConfigTable = _EthConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ethConfigTable.setStatus("current")
_EthConfigEntry_Object = MibTableRow
ethConfigEntry = _EthConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 1, 1)
)
ethConfigEntry.setIndexNames(
    (0, "SL-ETH-MIB", "ethLineIndex"),
)
if mibBuilder.loadTexts:
    ethConfigEntry.setStatus("current")
_EthLineIndex_Type = InterfaceIndex
_EthLineIndex_Object = MibTableColumn
ethLineIndex = _EthLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 1, 1, 1),
    _EthLineIndex_Type()
)
ethLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethLineIndex.setStatus("current")


class _EthTimeElapsed_Type(Integer32):
    """Custom type ethTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_EthTimeElapsed_Type.__name__ = "Integer32"
_EthTimeElapsed_Object = MibTableColumn
ethTimeElapsed = _EthTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 1, 1, 2),
    _EthTimeElapsed_Type()
)
ethTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethTimeElapsed.setStatus("current")


class _EthValidIntervals_Type(Integer32):
    """Custom type ethValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_EthValidIntervals_Type.__name__ = "Integer32"
_EthValidIntervals_Object = MibTableColumn
ethValidIntervals = _EthValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 1, 1, 3),
    _EthValidIntervals_Type()
)
ethValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethValidIntervals.setStatus("current")
_EthResetPm_Type = Integer32
_EthResetPm_Object = MibTableColumn
ethResetPm = _EthResetPm_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 1, 1, 4),
    _EthResetPm_Type()
)
ethResetPm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethResetPm.setStatus("current")
_EthAutoNegSupported_Type = TruthValue
_EthAutoNegSupported_Object = MibTableColumn
ethAutoNegSupported = _EthAutoNegSupported_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 1, 1, 5),
    _EthAutoNegSupported_Type()
)
ethAutoNegSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethAutoNegSupported.setStatus("current")


class _EthAutoNegAdminStatus_Type(Integer32):
    """Custom type ethAutoNegAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_EthAutoNegAdminStatus_Type.__name__ = "Integer32"
_EthAutoNegAdminStatus_Object = MibTableColumn
ethAutoNegAdminStatus = _EthAutoNegAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 1, 1, 6),
    _EthAutoNegAdminStatus_Type()
)
ethAutoNegAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethAutoNegAdminStatus.setStatus("current")


class _EthConfigStatus_Type(Integer32):
    """Custom type ethConfigStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_EthConfigStatus_Type.__name__ = "Integer32"
_EthConfigStatus_Object = MibTableColumn
ethConfigStatus = _EthConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 1, 1, 7),
    _EthConfigStatus_Type()
)
ethConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethConfigStatus.setStatus("current")


class _EthTransceiverType_Type(Integer32):
    """Custom type ethTransceiverType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("base1000SX", 2),
          ("base1000LX", 3))
    )


_EthTransceiverType_Type.__name__ = "Integer32"
_EthTransceiverType_Object = MibTableColumn
ethTransceiverType = _EthTransceiverType_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 1, 1, 8),
    _EthTransceiverType_Type()
)
ethTransceiverType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethTransceiverType.setStatus("current")


class _EthPauseTime_Type(Integer32):
    """Custom type ethPauseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 16383),
    )


_EthPauseTime_Type.__name__ = "Integer32"
_EthPauseTime_Object = MibTableColumn
ethPauseTime = _EthPauseTime_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 1, 1, 9),
    _EthPauseTime_Type()
)
ethPauseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethPauseTime.setStatus("current")
_EthPauseEnable_Type = TruthValue
_EthPauseEnable_Object = MibTableColumn
ethPauseEnable = _EthPauseEnable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 1, 1, 10),
    _EthPauseEnable_Type()
)
ethPauseEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethPauseEnable.setStatus("current")
_EthResetPmCounters_Type = Integer32
_EthResetPmCounters_Object = MibTableColumn
ethResetPmCounters = _EthResetPmCounters_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 1, 1, 11),
    _EthResetPmCounters_Type()
)
ethResetPmCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethResetPmCounters.setStatus("current")


class _EthTransceiverMedia_Type(Integer32):
    """Custom type ethTransceiverMedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("copper", 2),
          ("fiber", 3))
    )


_EthTransceiverMedia_Type.__name__ = "Integer32"
_EthTransceiverMedia_Object = MibTableColumn
ethTransceiverMedia = _EthTransceiverMedia_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 1, 1, 12),
    _EthTransceiverMedia_Type()
)
ethTransceiverMedia.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethTransceiverMedia.setStatus("current")
_EthCurrentTable_Object = MibTable
ethCurrentTable = _EthCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ethCurrentTable.setStatus("current")
_EthCurrentEntry_Object = MibTableRow
ethCurrentEntry = _EthCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1)
)
ethCurrentEntry.setIndexNames(
    (0, "SL-ETH-MIB", "ethCurrentIndex"),
)
if mibBuilder.loadTexts:
    ethCurrentEntry.setStatus("current")
_EthCurrentIndex_Type = InterfaceIndex
_EthCurrentIndex_Object = MibTableColumn
ethCurrentIndex = _EthCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 1),
    _EthCurrentIndex_Type()
)
ethCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethCurrentIndex.setStatus("current")
_EthCurrentRxDropEvents_Type = Counter64
_EthCurrentRxDropEvents_Object = MibTableColumn
ethCurrentRxDropEvents = _EthCurrentRxDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 2),
    _EthCurrentRxDropEvents_Type()
)
ethCurrentRxDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethCurrentRxDropEvents.setStatus("current")
_EthCurrentOctets_Type = Counter64
_EthCurrentOctets_Object = MibTableColumn
ethCurrentOctets = _EthCurrentOctets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 3),
    _EthCurrentOctets_Type()
)
ethCurrentOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethCurrentOctets.setStatus("current")
_EthCurrentPkts_Type = Counter64
_EthCurrentPkts_Object = MibTableColumn
ethCurrentPkts = _EthCurrentPkts_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 4),
    _EthCurrentPkts_Type()
)
ethCurrentPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethCurrentPkts.setStatus("current")
_EthCurrentBroadcastPkts_Type = Counter64
_EthCurrentBroadcastPkts_Object = MibTableColumn
ethCurrentBroadcastPkts = _EthCurrentBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 5),
    _EthCurrentBroadcastPkts_Type()
)
ethCurrentBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethCurrentBroadcastPkts.setStatus("current")
_EthCurrentMulticastPkts_Type = Counter64
_EthCurrentMulticastPkts_Object = MibTableColumn
ethCurrentMulticastPkts = _EthCurrentMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 6),
    _EthCurrentMulticastPkts_Type()
)
ethCurrentMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethCurrentMulticastPkts.setStatus("current")
_EthCurrentCRCAlignErrors_Type = Counter64
_EthCurrentCRCAlignErrors_Object = MibTableColumn
ethCurrentCRCAlignErrors = _EthCurrentCRCAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 7),
    _EthCurrentCRCAlignErrors_Type()
)
ethCurrentCRCAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethCurrentCRCAlignErrors.setStatus("current")
_EthCurrentUndersizePkts_Type = Counter64
_EthCurrentUndersizePkts_Object = MibTableColumn
ethCurrentUndersizePkts = _EthCurrentUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 8),
    _EthCurrentUndersizePkts_Type()
)
ethCurrentUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethCurrentUndersizePkts.setStatus("current")
_EthCurrentOversizePkts_Type = Counter64
_EthCurrentOversizePkts_Object = MibTableColumn
ethCurrentOversizePkts = _EthCurrentOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 9),
    _EthCurrentOversizePkts_Type()
)
ethCurrentOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethCurrentOversizePkts.setStatus("current")
_EthCurrentFragments_Type = Counter64
_EthCurrentFragments_Object = MibTableColumn
ethCurrentFragments = _EthCurrentFragments_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 10),
    _EthCurrentFragments_Type()
)
ethCurrentFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethCurrentFragments.setStatus("current")
_EthCurrentJabbers_Type = Counter64
_EthCurrentJabbers_Object = MibTableColumn
ethCurrentJabbers = _EthCurrentJabbers_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 11),
    _EthCurrentJabbers_Type()
)
ethCurrentJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethCurrentJabbers.setStatus("current")
_EthCurrentCollisions_Type = Counter64
_EthCurrentCollisions_Object = MibTableColumn
ethCurrentCollisions = _EthCurrentCollisions_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 12),
    _EthCurrentCollisions_Type()
)
ethCurrentCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethCurrentCollisions.setStatus("current")
_EthCurrentUtilization_Type = Counter64
_EthCurrentUtilization_Object = MibTableColumn
ethCurrentUtilization = _EthCurrentUtilization_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 13),
    _EthCurrentUtilization_Type()
)
ethCurrentUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethCurrentUtilization.setStatus("current")
_EthCurrentTxOctets_Type = Counter64
_EthCurrentTxOctets_Object = MibTableColumn
ethCurrentTxOctets = _EthCurrentTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 14),
    _EthCurrentTxOctets_Type()
)
ethCurrentTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethCurrentTxOctets.setStatus("current")
_EthCurrentTxPkts_Type = Counter64
_EthCurrentTxPkts_Object = MibTableColumn
ethCurrentTxPkts = _EthCurrentTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 15),
    _EthCurrentTxPkts_Type()
)
ethCurrentTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethCurrentTxPkts.setStatus("current")
_EthCurrentRxPause_Type = Counter64
_EthCurrentRxPause_Object = MibTableColumn
ethCurrentRxPause = _EthCurrentRxPause_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 16),
    _EthCurrentRxPause_Type()
)
ethCurrentRxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethCurrentRxPause.setStatus("current")
_EthCurrentTxPause_Type = Counter64
_EthCurrentTxPause_Object = MibTableColumn
ethCurrentTxPause = _EthCurrentTxPause_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 17),
    _EthCurrentTxPause_Type()
)
ethCurrentTxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethCurrentTxPause.setStatus("current")
_EthCurrentTxDropEvents_Type = Counter64
_EthCurrentTxDropEvents_Object = MibTableColumn
ethCurrentTxDropEvents = _EthCurrentTxDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 18),
    _EthCurrentTxDropEvents_Type()
)
ethCurrentTxDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethCurrentTxDropEvents.setStatus("current")
_EthCurrentRxPkts64Octets_Type = Counter64
_EthCurrentRxPkts64Octets_Object = MibTableColumn
ethCurrentRxPkts64Octets = _EthCurrentRxPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 19),
    _EthCurrentRxPkts64Octets_Type()
)
ethCurrentRxPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethCurrentRxPkts64Octets.setStatus("current")
_EthCurrentRxPkts65to127Octets_Type = Counter64
_EthCurrentRxPkts65to127Octets_Object = MibTableColumn
ethCurrentRxPkts65to127Octets = _EthCurrentRxPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 20),
    _EthCurrentRxPkts65to127Octets_Type()
)
ethCurrentRxPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethCurrentRxPkts65to127Octets.setStatus("current")
_EthCurrentRxPkts128to255Octets_Type = Counter64
_EthCurrentRxPkts128to255Octets_Object = MibTableColumn
ethCurrentRxPkts128to255Octets = _EthCurrentRxPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 21),
    _EthCurrentRxPkts128to255Octets_Type()
)
ethCurrentRxPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethCurrentRxPkts128to255Octets.setStatus("current")
_EthCurrentRxPkts256to511Octets_Type = Counter64
_EthCurrentRxPkts256to511Octets_Object = MibTableColumn
ethCurrentRxPkts256to511Octets = _EthCurrentRxPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 22),
    _EthCurrentRxPkts256to511Octets_Type()
)
ethCurrentRxPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethCurrentRxPkts256to511Octets.setStatus("current")
_EthCurrentRxPkts512to1023Octets_Type = Counter64
_EthCurrentRxPkts512to1023Octets_Object = MibTableColumn
ethCurrentRxPkts512to1023Octets = _EthCurrentRxPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 23),
    _EthCurrentRxPkts512to1023Octets_Type()
)
ethCurrentRxPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethCurrentRxPkts512to1023Octets.setStatus("current")
_EthCurrentRxPkts1024to1518Octets_Type = Counter64
_EthCurrentRxPkts1024to1518Octets_Object = MibTableColumn
ethCurrentRxPkts1024to1518Octets = _EthCurrentRxPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 24),
    _EthCurrentRxPkts1024to1518Octets_Type()
)
ethCurrentRxPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethCurrentRxPkts1024to1518Octets.setStatus("current")
_EthCurrentRxPkts1519to1522Octets_Type = Counter64
_EthCurrentRxPkts1519to1522Octets_Object = MibTableColumn
ethCurrentRxPkts1519to1522Octets = _EthCurrentRxPkts1519to1522Octets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 25),
    _EthCurrentRxPkts1519to1522Octets_Type()
)
ethCurrentRxPkts1519to1522Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethCurrentRxPkts1519to1522Octets.setStatus("current")
_EthCurrentTxPkts64Octets_Type = Counter64
_EthCurrentTxPkts64Octets_Object = MibTableColumn
ethCurrentTxPkts64Octets = _EthCurrentTxPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 26),
    _EthCurrentTxPkts64Octets_Type()
)
ethCurrentTxPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethCurrentTxPkts64Octets.setStatus("current")
_EthCurrentTxPkts65to127Octets_Type = Counter64
_EthCurrentTxPkts65to127Octets_Object = MibTableColumn
ethCurrentTxPkts65to127Octets = _EthCurrentTxPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 27),
    _EthCurrentTxPkts65to127Octets_Type()
)
ethCurrentTxPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethCurrentTxPkts65to127Octets.setStatus("current")
_EthCurrentTxPkts128to255Octets_Type = Counter64
_EthCurrentTxPkts128to255Octets_Object = MibTableColumn
ethCurrentTxPkts128to255Octets = _EthCurrentTxPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 28),
    _EthCurrentTxPkts128to255Octets_Type()
)
ethCurrentTxPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethCurrentTxPkts128to255Octets.setStatus("current")
_EthCurrentTxPkts256to511Octets_Type = Counter64
_EthCurrentTxPkts256to511Octets_Object = MibTableColumn
ethCurrentTxPkts256to511Octets = _EthCurrentTxPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 29),
    _EthCurrentTxPkts256to511Octets_Type()
)
ethCurrentTxPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethCurrentTxPkts256to511Octets.setStatus("current")
_EthCurrentTxPkts512to1023Octets_Type = Counter64
_EthCurrentTxPkts512to1023Octets_Object = MibTableColumn
ethCurrentTxPkts512to1023Octets = _EthCurrentTxPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 30),
    _EthCurrentTxPkts512to1023Octets_Type()
)
ethCurrentTxPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethCurrentTxPkts512to1023Octets.setStatus("current")
_EthCurrentTxPkts1024to1518Octets_Type = Counter64
_EthCurrentTxPkts1024to1518Octets_Object = MibTableColumn
ethCurrentTxPkts1024to1518Octets = _EthCurrentTxPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 31),
    _EthCurrentTxPkts1024to1518Octets_Type()
)
ethCurrentTxPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethCurrentTxPkts1024to1518Octets.setStatus("current")
_EthCurrentTxPkts1519to1522Octets_Type = Counter64
_EthCurrentTxPkts1519to1522Octets_Object = MibTableColumn
ethCurrentTxPkts1519to1522Octets = _EthCurrentTxPkts1519to1522Octets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 32),
    _EthCurrentTxPkts1519to1522Octets_Type()
)
ethCurrentTxPkts1519to1522Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethCurrentTxPkts1519to1522Octets.setStatus("current")
_EthCurrentRxVlanPkts_Type = Counter64
_EthCurrentRxVlanPkts_Object = MibTableColumn
ethCurrentRxVlanPkts = _EthCurrentRxVlanPkts_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 33),
    _EthCurrentRxVlanPkts_Type()
)
ethCurrentRxVlanPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethCurrentRxVlanPkts.setStatus("current")
_EthCurrentTxVlanPkts_Type = Counter64
_EthCurrentTxVlanPkts_Object = MibTableColumn
ethCurrentTxVlanPkts = _EthCurrentTxVlanPkts_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 34),
    _EthCurrentTxVlanPkts_Type()
)
ethCurrentTxVlanPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethCurrentTxVlanPkts.setStatus("current")
_EthCurrentRxJumboPkts_Type = Counter64
_EthCurrentRxJumboPkts_Object = MibTableColumn
ethCurrentRxJumboPkts = _EthCurrentRxJumboPkts_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 35),
    _EthCurrentRxJumboPkts_Type()
)
ethCurrentRxJumboPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethCurrentRxJumboPkts.setStatus("current")
_EthCurrentTxJumboPkts_Type = Counter64
_EthCurrentTxJumboPkts_Object = MibTableColumn
ethCurrentTxJumboPkts = _EthCurrentTxJumboPkts_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 36),
    _EthCurrentTxJumboPkts_Type()
)
ethCurrentTxJumboPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethCurrentTxJumboPkts.setStatus("current")
_EthIntervalTable_Object = MibTable
ethIntervalTable = _EthIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ethIntervalTable.setStatus("current")
_EthIntervalEntry_Object = MibTableRow
ethIntervalEntry = _EthIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 3, 1)
)
ethIntervalEntry.setIndexNames(
    (0, "SL-ETH-MIB", "ethIntervalIndex"),
    (0, "SL-ETH-MIB", "ethIntervalNumber"),
)
if mibBuilder.loadTexts:
    ethIntervalEntry.setStatus("current")
_EthIntervalIndex_Type = InterfaceIndex
_EthIntervalIndex_Object = MibTableColumn
ethIntervalIndex = _EthIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 3, 1, 1),
    _EthIntervalIndex_Type()
)
ethIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIntervalIndex.setStatus("current")


class _EthIntervalNumber_Type(Integer32):
    """Custom type ethIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_EthIntervalNumber_Type.__name__ = "Integer32"
_EthIntervalNumber_Object = MibTableColumn
ethIntervalNumber = _EthIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 3, 1, 2),
    _EthIntervalNumber_Type()
)
ethIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIntervalNumber.setStatus("current")
_EthIntervalDropEvents_Type = Counter64
_EthIntervalDropEvents_Object = MibTableColumn
ethIntervalDropEvents = _EthIntervalDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 3, 1, 3),
    _EthIntervalDropEvents_Type()
)
ethIntervalDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIntervalDropEvents.setStatus("current")
_EthIntervalOctets_Type = Counter64
_EthIntervalOctets_Object = MibTableColumn
ethIntervalOctets = _EthIntervalOctets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 3, 1, 4),
    _EthIntervalOctets_Type()
)
ethIntervalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIntervalOctets.setStatus("current")
_EthIntervalPkts_Type = Counter64
_EthIntervalPkts_Object = MibTableColumn
ethIntervalPkts = _EthIntervalPkts_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 3, 1, 5),
    _EthIntervalPkts_Type()
)
ethIntervalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIntervalPkts.setStatus("current")
_EthIntervalBroadcastPkts_Type = Counter64
_EthIntervalBroadcastPkts_Object = MibTableColumn
ethIntervalBroadcastPkts = _EthIntervalBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 3, 1, 6),
    _EthIntervalBroadcastPkts_Type()
)
ethIntervalBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIntervalBroadcastPkts.setStatus("current")
_EthIntervalMulticastPkts_Type = Counter64
_EthIntervalMulticastPkts_Object = MibTableColumn
ethIntervalMulticastPkts = _EthIntervalMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 3, 1, 7),
    _EthIntervalMulticastPkts_Type()
)
ethIntervalMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIntervalMulticastPkts.setStatus("current")
_EthIntervalCRCAlignErrors_Type = Counter64
_EthIntervalCRCAlignErrors_Object = MibTableColumn
ethIntervalCRCAlignErrors = _EthIntervalCRCAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 3, 1, 8),
    _EthIntervalCRCAlignErrors_Type()
)
ethIntervalCRCAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIntervalCRCAlignErrors.setStatus("current")
_EthIntervalUndersizePkts_Type = Counter64
_EthIntervalUndersizePkts_Object = MibTableColumn
ethIntervalUndersizePkts = _EthIntervalUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 3, 1, 9),
    _EthIntervalUndersizePkts_Type()
)
ethIntervalUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIntervalUndersizePkts.setStatus("current")
_EthIntervalOversizePkts_Type = Counter64
_EthIntervalOversizePkts_Object = MibTableColumn
ethIntervalOversizePkts = _EthIntervalOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 3, 1, 10),
    _EthIntervalOversizePkts_Type()
)
ethIntervalOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIntervalOversizePkts.setStatus("current")
_EthIntervalFragments_Type = Counter64
_EthIntervalFragments_Object = MibTableColumn
ethIntervalFragments = _EthIntervalFragments_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 3, 1, 11),
    _EthIntervalFragments_Type()
)
ethIntervalFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIntervalFragments.setStatus("current")
_EthIntervalJabbers_Type = Counter64
_EthIntervalJabbers_Object = MibTableColumn
ethIntervalJabbers = _EthIntervalJabbers_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 3, 1, 12),
    _EthIntervalJabbers_Type()
)
ethIntervalJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIntervalJabbers.setStatus("current")
_EthIntervalCollisions_Type = Counter64
_EthIntervalCollisions_Object = MibTableColumn
ethIntervalCollisions = _EthIntervalCollisions_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 3, 1, 13),
    _EthIntervalCollisions_Type()
)
ethIntervalCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIntervalCollisions.setStatus("current")
_EthIntervalUtilization_Type = Counter64
_EthIntervalUtilization_Object = MibTableColumn
ethIntervalUtilization = _EthIntervalUtilization_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 3, 1, 14),
    _EthIntervalUtilization_Type()
)
ethIntervalUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIntervalUtilization.setStatus("current")
_EthIntervalTxOctets_Type = Counter64
_EthIntervalTxOctets_Object = MibTableColumn
ethIntervalTxOctets = _EthIntervalTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 3, 1, 15),
    _EthIntervalTxOctets_Type()
)
ethIntervalTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIntervalTxOctets.setStatus("current")
_EthIntervalTxPkts_Type = Counter64
_EthIntervalTxPkts_Object = MibTableColumn
ethIntervalTxPkts = _EthIntervalTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 3, 1, 16),
    _EthIntervalTxPkts_Type()
)
ethIntervalTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIntervalTxPkts.setStatus("current")
_EthIntervalRxPause_Type = Counter64
_EthIntervalRxPause_Object = MibTableColumn
ethIntervalRxPause = _EthIntervalRxPause_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 3, 1, 17),
    _EthIntervalRxPause_Type()
)
ethIntervalRxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIntervalRxPause.setStatus("current")
_EthIntervalTxPause_Type = Counter64
_EthIntervalTxPause_Object = MibTableColumn
ethIntervalTxPause = _EthIntervalTxPause_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 3, 1, 18),
    _EthIntervalTxPause_Type()
)
ethIntervalTxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIntervalTxPause.setStatus("current")
_EthIntervalValidData_Type = TruthValue
_EthIntervalValidData_Object = MibTableColumn
ethIntervalValidData = _EthIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 3, 1, 19),
    _EthIntervalValidData_Type()
)
ethIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIntervalValidData.setStatus("current")
_EthIntervalTcaFlag_Type = TruthValue
_EthIntervalTcaFlag_Object = MibTableColumn
ethIntervalTcaFlag = _EthIntervalTcaFlag_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 3, 1, 20),
    _EthIntervalTcaFlag_Type()
)
ethIntervalTcaFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIntervalTcaFlag.setStatus("current")
_EthTotalTable_Object = MibTable
ethTotalTable = _EthTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    ethTotalTable.setStatus("current")
_EthTotalEntry_Object = MibTableRow
ethTotalEntry = _EthTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 4, 1)
)
ethTotalEntry.setIndexNames(
    (0, "SL-ETH-MIB", "ethTotalIndex"),
    (0, "SL-ETH-MIB", "ethTotalDayNumber"),
)
if mibBuilder.loadTexts:
    ethTotalEntry.setStatus("current")
_EthTotalIndex_Type = InterfaceIndex
_EthTotalIndex_Object = MibTableColumn
ethTotalIndex = _EthTotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 4, 1, 1),
    _EthTotalIndex_Type()
)
ethTotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethTotalIndex.setStatus("current")


class _EthTotalDayNumber_Type(Integer32):
    """Custom type ethTotalDayNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 33),
    )


_EthTotalDayNumber_Type.__name__ = "Integer32"
_EthTotalDayNumber_Object = MibTableColumn
ethTotalDayNumber = _EthTotalDayNumber_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 4, 1, 2),
    _EthTotalDayNumber_Type()
)
ethTotalDayNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ethTotalDayNumber.setStatus("current")
_EthTotalDropEvents_Type = Counter64
_EthTotalDropEvents_Object = MibTableColumn
ethTotalDropEvents = _EthTotalDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 4, 1, 3),
    _EthTotalDropEvents_Type()
)
ethTotalDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethTotalDropEvents.setStatus("current")
_EthTotalOctets_Type = Counter64
_EthTotalOctets_Object = MibTableColumn
ethTotalOctets = _EthTotalOctets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 4, 1, 4),
    _EthTotalOctets_Type()
)
ethTotalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethTotalOctets.setStatus("current")
_EthTotalPkts_Type = Counter64
_EthTotalPkts_Object = MibTableColumn
ethTotalPkts = _EthTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 4, 1, 5),
    _EthTotalPkts_Type()
)
ethTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethTotalPkts.setStatus("current")
_EthTotalBroadcastPkts_Type = Counter64
_EthTotalBroadcastPkts_Object = MibTableColumn
ethTotalBroadcastPkts = _EthTotalBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 4, 1, 6),
    _EthTotalBroadcastPkts_Type()
)
ethTotalBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethTotalBroadcastPkts.setStatus("current")
_EthTotalMulticastPkts_Type = Counter64
_EthTotalMulticastPkts_Object = MibTableColumn
ethTotalMulticastPkts = _EthTotalMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 4, 1, 7),
    _EthTotalMulticastPkts_Type()
)
ethTotalMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethTotalMulticastPkts.setStatus("current")
_EthTotalCRCAlignErrors_Type = Counter64
_EthTotalCRCAlignErrors_Object = MibTableColumn
ethTotalCRCAlignErrors = _EthTotalCRCAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 4, 1, 8),
    _EthTotalCRCAlignErrors_Type()
)
ethTotalCRCAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethTotalCRCAlignErrors.setStatus("current")
_EthTotalUndersizePkts_Type = Counter64
_EthTotalUndersizePkts_Object = MibTableColumn
ethTotalUndersizePkts = _EthTotalUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 4, 1, 9),
    _EthTotalUndersizePkts_Type()
)
ethTotalUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethTotalUndersizePkts.setStatus("current")
_EthTotalOversizePkts_Type = Counter64
_EthTotalOversizePkts_Object = MibTableColumn
ethTotalOversizePkts = _EthTotalOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 4, 1, 10),
    _EthTotalOversizePkts_Type()
)
ethTotalOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethTotalOversizePkts.setStatus("current")
_EthTotalFragments_Type = Counter64
_EthTotalFragments_Object = MibTableColumn
ethTotalFragments = _EthTotalFragments_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 4, 1, 11),
    _EthTotalFragments_Type()
)
ethTotalFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethTotalFragments.setStatus("current")
_EthTotalJabbers_Type = Counter64
_EthTotalJabbers_Object = MibTableColumn
ethTotalJabbers = _EthTotalJabbers_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 4, 1, 12),
    _EthTotalJabbers_Type()
)
ethTotalJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethTotalJabbers.setStatus("current")
_EthTotalCollisions_Type = Counter64
_EthTotalCollisions_Object = MibTableColumn
ethTotalCollisions = _EthTotalCollisions_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 4, 1, 13),
    _EthTotalCollisions_Type()
)
ethTotalCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethTotalCollisions.setStatus("current")
_EthTotalUtilization_Type = Counter64
_EthTotalUtilization_Object = MibTableColumn
ethTotalUtilization = _EthTotalUtilization_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 4, 1, 14),
    _EthTotalUtilization_Type()
)
ethTotalUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethTotalUtilization.setStatus("current")
_EthTotalTxOctets_Type = Counter64
_EthTotalTxOctets_Object = MibTableColumn
ethTotalTxOctets = _EthTotalTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 4, 1, 15),
    _EthTotalTxOctets_Type()
)
ethTotalTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethTotalTxOctets.setStatus("current")
_EthTotalTxPkts_Type = Counter64
_EthTotalTxPkts_Object = MibTableColumn
ethTotalTxPkts = _EthTotalTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 4, 1, 16),
    _EthTotalTxPkts_Type()
)
ethTotalTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethTotalTxPkts.setStatus("current")
_EthTotalRxPause_Type = Counter64
_EthTotalRxPause_Object = MibTableColumn
ethTotalRxPause = _EthTotalRxPause_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 4, 1, 17),
    _EthTotalRxPause_Type()
)
ethTotalRxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethTotalRxPause.setStatus("current")
_EthTotalTxPause_Type = Counter64
_EthTotalTxPause_Object = MibTableColumn
ethTotalTxPause = _EthTotalTxPause_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 4, 1, 18),
    _EthTotalTxPause_Type()
)
ethTotalTxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethTotalTxPause.setStatus("current")
_EthTotalValidData_Type = TruthValue
_EthTotalValidData_Object = MibTableColumn
ethTotalValidData = _EthTotalValidData_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 4, 1, 19),
    _EthTotalValidData_Type()
)
ethTotalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethTotalValidData.setStatus("current")
_EthTraps_ObjectIdentity = ObjectIdentity
ethTraps = _EthTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 7)
)

# Managed Objects groups


# Notification objects

ethStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 7, 1)
)
ethStatusChange.setObjects(
      *(("SL-ETH-MIB", "ethLineIndex"),
        ("SL-ETH-MIB", "ethConfigStatus"))
)
if mibBuilder.loadTexts:
    ethStatusChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SL-ETH-MIB",
    **{"slEthernet": slEthernet,
       "ethConfigTable": ethConfigTable,
       "ethConfigEntry": ethConfigEntry,
       "ethLineIndex": ethLineIndex,
       "ethTimeElapsed": ethTimeElapsed,
       "ethValidIntervals": ethValidIntervals,
       "ethResetPm": ethResetPm,
       "ethAutoNegSupported": ethAutoNegSupported,
       "ethAutoNegAdminStatus": ethAutoNegAdminStatus,
       "ethConfigStatus": ethConfigStatus,
       "ethTransceiverType": ethTransceiverType,
       "ethPauseTime": ethPauseTime,
       "ethPauseEnable": ethPauseEnable,
       "ethResetPmCounters": ethResetPmCounters,
       "ethTransceiverMedia": ethTransceiverMedia,
       "ethCurrentTable": ethCurrentTable,
       "ethCurrentEntry": ethCurrentEntry,
       "ethCurrentIndex": ethCurrentIndex,
       "ethCurrentRxDropEvents": ethCurrentRxDropEvents,
       "ethCurrentOctets": ethCurrentOctets,
       "ethCurrentPkts": ethCurrentPkts,
       "ethCurrentBroadcastPkts": ethCurrentBroadcastPkts,
       "ethCurrentMulticastPkts": ethCurrentMulticastPkts,
       "ethCurrentCRCAlignErrors": ethCurrentCRCAlignErrors,
       "ethCurrentUndersizePkts": ethCurrentUndersizePkts,
       "ethCurrentOversizePkts": ethCurrentOversizePkts,
       "ethCurrentFragments": ethCurrentFragments,
       "ethCurrentJabbers": ethCurrentJabbers,
       "ethCurrentCollisions": ethCurrentCollisions,
       "ethCurrentUtilization": ethCurrentUtilization,
       "ethCurrentTxOctets": ethCurrentTxOctets,
       "ethCurrentTxPkts": ethCurrentTxPkts,
       "ethCurrentRxPause": ethCurrentRxPause,
       "ethCurrentTxPause": ethCurrentTxPause,
       "ethCurrentTxDropEvents": ethCurrentTxDropEvents,
       "ethCurrentRxPkts64Octets": ethCurrentRxPkts64Octets,
       "ethCurrentRxPkts65to127Octets": ethCurrentRxPkts65to127Octets,
       "ethCurrentRxPkts128to255Octets": ethCurrentRxPkts128to255Octets,
       "ethCurrentRxPkts256to511Octets": ethCurrentRxPkts256to511Octets,
       "ethCurrentRxPkts512to1023Octets": ethCurrentRxPkts512to1023Octets,
       "ethCurrentRxPkts1024to1518Octets": ethCurrentRxPkts1024to1518Octets,
       "ethCurrentRxPkts1519to1522Octets": ethCurrentRxPkts1519to1522Octets,
       "ethCurrentTxPkts64Octets": ethCurrentTxPkts64Octets,
       "ethCurrentTxPkts65to127Octets": ethCurrentTxPkts65to127Octets,
       "ethCurrentTxPkts128to255Octets": ethCurrentTxPkts128to255Octets,
       "ethCurrentTxPkts256to511Octets": ethCurrentTxPkts256to511Octets,
       "ethCurrentTxPkts512to1023Octets": ethCurrentTxPkts512to1023Octets,
       "ethCurrentTxPkts1024to1518Octets": ethCurrentTxPkts1024to1518Octets,
       "ethCurrentTxPkts1519to1522Octets": ethCurrentTxPkts1519to1522Octets,
       "ethCurrentRxVlanPkts": ethCurrentRxVlanPkts,
       "ethCurrentTxVlanPkts": ethCurrentTxVlanPkts,
       "ethCurrentRxJumboPkts": ethCurrentRxJumboPkts,
       "ethCurrentTxJumboPkts": ethCurrentTxJumboPkts,
       "ethIntervalTable": ethIntervalTable,
       "ethIntervalEntry": ethIntervalEntry,
       "ethIntervalIndex": ethIntervalIndex,
       "ethIntervalNumber": ethIntervalNumber,
       "ethIntervalDropEvents": ethIntervalDropEvents,
       "ethIntervalOctets": ethIntervalOctets,
       "ethIntervalPkts": ethIntervalPkts,
       "ethIntervalBroadcastPkts": ethIntervalBroadcastPkts,
       "ethIntervalMulticastPkts": ethIntervalMulticastPkts,
       "ethIntervalCRCAlignErrors": ethIntervalCRCAlignErrors,
       "ethIntervalUndersizePkts": ethIntervalUndersizePkts,
       "ethIntervalOversizePkts": ethIntervalOversizePkts,
       "ethIntervalFragments": ethIntervalFragments,
       "ethIntervalJabbers": ethIntervalJabbers,
       "ethIntervalCollisions": ethIntervalCollisions,
       "ethIntervalUtilization": ethIntervalUtilization,
       "ethIntervalTxOctets": ethIntervalTxOctets,
       "ethIntervalTxPkts": ethIntervalTxPkts,
       "ethIntervalRxPause": ethIntervalRxPause,
       "ethIntervalTxPause": ethIntervalTxPause,
       "ethIntervalValidData": ethIntervalValidData,
       "ethIntervalTcaFlag": ethIntervalTcaFlag,
       "ethTotalTable": ethTotalTable,
       "ethTotalEntry": ethTotalEntry,
       "ethTotalIndex": ethTotalIndex,
       "ethTotalDayNumber": ethTotalDayNumber,
       "ethTotalDropEvents": ethTotalDropEvents,
       "ethTotalOctets": ethTotalOctets,
       "ethTotalPkts": ethTotalPkts,
       "ethTotalBroadcastPkts": ethTotalBroadcastPkts,
       "ethTotalMulticastPkts": ethTotalMulticastPkts,
       "ethTotalCRCAlignErrors": ethTotalCRCAlignErrors,
       "ethTotalUndersizePkts": ethTotalUndersizePkts,
       "ethTotalOversizePkts": ethTotalOversizePkts,
       "ethTotalFragments": ethTotalFragments,
       "ethTotalJabbers": ethTotalJabbers,
       "ethTotalCollisions": ethTotalCollisions,
       "ethTotalUtilization": ethTotalUtilization,
       "ethTotalTxOctets": ethTotalTxOctets,
       "ethTotalTxPkts": ethTotalTxPkts,
       "ethTotalRxPause": ethTotalRxPause,
       "ethTotalTxPause": ethTotalTxPause,
       "ethTotalValidData": ethTotalValidData,
       "ethTraps": ethTraps,
       "ethStatusChange": ethStatusChange}
)
