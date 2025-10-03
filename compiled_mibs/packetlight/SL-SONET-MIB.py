# SNMP MIB module (SL-SONET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\packetlight\SL-SONET-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:20:09 2025
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(PerfCurrentCount,
 PerfIntervalCount,
 PerfTotalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount",
    "PerfTotalCount")

(sitelight,) = mibBuilder.importSymbols(
    "SL-NE-MIB",
    "sitelight")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

slSonetMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SignalLabel(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              18,
              19,
              20,
              21,
              22,
              27)
        )
    )
    namedValues = NamedValues(
        *(("sigUnequipped", 0),
          ("sigEquipped", 1),
          ("sigPathFloatVt", 2),
          ("sigPathLoackedVt", 3),
          ("sigPathAsynchDs3", 4),
          ("sigPathSyntran", 5),
          ("sigPathAsyncDs4na", 18),
          ("sigPathAtm", 19),
          ("sigPathDqdb", 20),
          ("sigPathFddi", 21),
          ("sigPathHdlc", 22),
          ("sigPathGfp", 27))
    )



# MIB Managed Objects in the order of their OIDs

_SlSonetConfig_ObjectIdentity = ObjectIdentity
slSonetConfig = _SlSonetConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 1)
)
_SlSonetConfigTable_Object = MibTable
slSonetConfigTable = _SlSonetConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    slSonetConfigTable.setStatus("current")
_SlSonetConfigEntry_Object = MibTableRow
slSonetConfigEntry = _SlSonetConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 1, 1, 1)
)
slSonetConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    slSonetConfigEntry.setStatus("current")


class _SlSonetConfigFrameScramble_Type(Integer32):
    """Custom type slSonetConfigFrameScramble based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SlSonetConfigFrameScramble_Type.__name__ = "Integer32"
_SlSonetConfigFrameScramble_Object = MibTableColumn
slSonetConfigFrameScramble = _SlSonetConfigFrameScramble_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 1, 1, 1, 1),
    _SlSonetConfigFrameScramble_Type()
)
slSonetConfigFrameScramble.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slSonetConfigFrameScramble.setStatus("current")


class _SlSonetConfigType_Type(Integer32):
    """Custom type slSonetConfigType based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("sonetSts3", 1),
          ("sonetSts3c", 2),
          ("sonetSts12", 3),
          ("sonetSts12c", 4),
          ("sonetSts48c", 5),
          ("sonetSts3cx4", 6),
          ("sonetSts48", 7),
          ("sonetSts3cx16", 8),
          ("sonetSts3x16", 9),
          ("sonetSts12cx4", 10),
          ("sonetSts12x4", 11),
          ("sonetSts192c", 12),
          ("sonetStsOther", 13))
    )


_SlSonetConfigType_Type.__name__ = "Integer32"
_SlSonetConfigType_Object = MibTableColumn
slSonetConfigType = _SlSonetConfigType_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 1, 1, 1, 2),
    _SlSonetConfigType_Type()
)
slSonetConfigType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slSonetConfigType.setStatus("current")


class _SlSonetConfigDccSelection_Type(Integer32):
    """Custom type slSonetConfigDccSelection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sonetLineDcc", 1),
          ("sonetSectionDcc", 2),
          ("sonetInband", 3))
    )


_SlSonetConfigDccSelection_Type.__name__ = "Integer32"
_SlSonetConfigDccSelection_Object = MibTableColumn
slSonetConfigDccSelection = _SlSonetConfigDccSelection_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 1, 1, 1, 3),
    _SlSonetConfigDccSelection_Type()
)
slSonetConfigDccSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slSonetConfigDccSelection.setStatus("current")


class _SlSonetResetAllCounters_Type(Integer32):
    """Custom type slSonetResetAllCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("resetCounters", 1)
    )


_SlSonetResetAllCounters_Type.__name__ = "Integer32"
_SlSonetResetAllCounters_Object = MibTableColumn
slSonetResetAllCounters = _SlSonetResetAllCounters_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 1, 1, 1, 4),
    _SlSonetResetAllCounters_Type()
)
slSonetResetAllCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slSonetResetAllCounters.setStatus("current")


class _SlSonetPortThresholdTrapEnable_Type(Integer32):
    """Custom type slSonetPortThresholdTrapEnable based on Integer32"""
    defaultValue = 2

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


_SlSonetPortThresholdTrapEnable_Type.__name__ = "Integer32"
_SlSonetPortThresholdTrapEnable_Object = MibTableColumn
slSonetPortThresholdTrapEnable = _SlSonetPortThresholdTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 1, 1, 1, 5),
    _SlSonetPortThresholdTrapEnable_Type()
)
slSonetPortThresholdTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slSonetPortThresholdTrapEnable.setStatus("current")


class _SlSonetConfigSdThreshold_Type(Integer32):
    """Custom type slSonetConfigSdThreshold based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 9),
    )


_SlSonetConfigSdThreshold_Type.__name__ = "Integer32"
_SlSonetConfigSdThreshold_Object = MibTableColumn
slSonetConfigSdThreshold = _SlSonetConfigSdThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 1, 1, 1, 6),
    _SlSonetConfigSdThreshold_Type()
)
slSonetConfigSdThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slSonetConfigSdThreshold.setStatus("current")


class _SlSonetConfigSfThreshold_Type(Integer32):
    """Custom type slSonetConfigSfThreshold based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 5),
    )


_SlSonetConfigSfThreshold_Type.__name__ = "Integer32"
_SlSonetConfigSfThreshold_Object = MibTableColumn
slSonetConfigSfThreshold = _SlSonetConfigSfThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 1, 1, 1, 7),
    _SlSonetConfigSfThreshold_Type()
)
slSonetConfigSfThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slSonetConfigSfThreshold.setStatus("current")


class _SlSonetCompression_Type(Integer32):
    """Custom type slSonetCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("uncompress", 0),
          ("posCompress32", 1),
          ("posCompress16", 2))
    )


_SlSonetCompression_Type.__name__ = "Integer32"
_SlSonetCompression_Object = MibTableColumn
slSonetCompression = _SlSonetCompression_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 1, 1, 1, 9),
    _SlSonetCompression_Type()
)
slSonetCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slSonetCompression.setStatus("current")


class _SlSonetOverheadTunneling_Type(Integer32):
    """Custom type slSonetOverheadTunneling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("lineDcc", 1),
          ("k1k2", 2),
          ("full", 3))
    )


_SlSonetOverheadTunneling_Type.__name__ = "Integer32"
_SlSonetOverheadTunneling_Object = MibTableColumn
slSonetOverheadTunneling = _SlSonetOverheadTunneling_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 1, 1, 1, 10),
    _SlSonetOverheadTunneling_Type()
)
slSonetOverheadTunneling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slSonetOverheadTunneling.setStatus("current")
_SlSonetLopBitmask_Type = Counter64
_SlSonetLopBitmask_Object = MibTableColumn
slSonetLopBitmask = _SlSonetLopBitmask_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 1, 1, 1, 11),
    _SlSonetLopBitmask_Type()
)
slSonetLopBitmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slSonetLopBitmask.setStatus("current")
_SlSonetTdmTrunk_Type = TruthValue
_SlSonetTdmTrunk_Object = MibTableColumn
slSonetTdmTrunk = _SlSonetTdmTrunk_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 1, 1, 1, 12),
    _SlSonetTdmTrunk_Type()
)
slSonetTdmTrunk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slSonetTdmTrunk.setStatus("current")
_SlSonetFsApply_Type = Integer32
_SlSonetFsApply_Object = MibTableColumn
slSonetFsApply = _SlSonetFsApply_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 1, 1, 1, 13),
    _SlSonetFsApply_Type()
)
slSonetFsApply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slSonetFsApply.setStatus("current")


class _SlSonetTxLte_Type(Integer32):
    """Custom type slSonetTxLte based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ssb00", 1),
          ("ssb10", 2),
          ("auto", 5))
    )


_SlSonetTxLte_Type.__name__ = "Integer32"
_SlSonetTxLte_Object = MibTableColumn
slSonetTxLte = _SlSonetTxLte_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 1, 1, 1, 14),
    _SlSonetTxLte_Type()
)
slSonetTxLte.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slSonetTxLte.setStatus("current")


class _SlSonetReceivedLte_Type(Integer32):
    """Custom type slSonetReceivedLte based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ssb00", 1),
          ("ssb10", 2),
          ("ssb01", 3),
          ("ssb11", 4),
          ("ssbinv", 5))
    )


_SlSonetReceivedLte_Type.__name__ = "Integer32"
_SlSonetReceivedLte_Object = MibTableColumn
slSonetReceivedLte = _SlSonetReceivedLte_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 1, 1, 1, 15),
    _SlSonetReceivedLte_Type()
)
slSonetReceivedLte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slSonetReceivedLte.setStatus("current")


class _SlSonetResetPmThreshold_Type(Integer32):
    """Custom type slSonetResetPmThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("resetCounters", 1)
    )


_SlSonetResetPmThreshold_Type.__name__ = "Integer32"
_SlSonetResetPmThreshold_Object = MibTableColumn
slSonetResetPmThreshold = _SlSonetResetPmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 1, 1, 1, 16),
    _SlSonetResetPmThreshold_Type()
)
slSonetResetPmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slSonetResetPmThreshold.setStatus("current")


class _SlSonetResetAlsParams_Type(Integer32):
    """Custom type slSonetResetAlsParams based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("resetCounters", 1)
    )


_SlSonetResetAlsParams_Type.__name__ = "Integer32"
_SlSonetResetAlsParams_Object = MibTableColumn
slSonetResetAlsParams = _SlSonetResetAlsParams_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 1, 1, 1, 17),
    _SlSonetResetAlsParams_Type()
)
slSonetResetAlsParams.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slSonetResetAlsParams.setStatus("current")


class _SlSonetTransceiverType_Type(Integer32):
    """Custom type slSonetTransceiverType based on Integer32"""
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
          ("shortWave", 2),
          ("longWave", 3))
    )


_SlSonetTransceiverType_Type.__name__ = "Integer32"
_SlSonetTransceiverType_Object = MibTableColumn
slSonetTransceiverType = _SlSonetTransceiverType_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 1, 1, 1, 18),
    _SlSonetTransceiverType_Type()
)
slSonetTransceiverType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slSonetTransceiverType.setStatus("current")


class _SlSonetTransceiverMedia_Type(Integer32):
    """Custom type slSonetTransceiverMedia based on Integer32"""
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
          ("sm", 2),
          ("mm", 3))
    )


_SlSonetTransceiverMedia_Type.__name__ = "Integer32"
_SlSonetTransceiverMedia_Object = MibTableColumn
slSonetTransceiverMedia = _SlSonetTransceiverMedia_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 1, 1, 1, 19),
    _SlSonetTransceiverMedia_Type()
)
slSonetTransceiverMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slSonetTransceiverMedia.setStatus("current")
_SlSonetOh_ObjectIdentity = ObjectIdentity
slSonetOh = _SlSonetOh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 2)
)
_SlSonetOhTrace_ObjectIdentity = ObjectIdentity
slSonetOhTrace = _SlSonetOhTrace_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 2, 1)
)
_SlSonetTraceTable_Object = MibTable
slSonetTraceTable = _SlSonetTraceTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 2, 1, 1)
)
if mibBuilder.loadTexts:
    slSonetTraceTable.setStatus("current")
_SlSonetTraceEntry_Object = MibTableRow
slSonetTraceEntry = _SlSonetTraceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 2, 1, 1, 1)
)
slSonetTraceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    slSonetTraceEntry.setStatus("current")


class _SlSonetTraceMode_Type(Integer32):
    """Custom type slSonetTraceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("monitoring", 3))
    )


_SlSonetTraceMode_Type.__name__ = "Integer32"
_SlSonetTraceMode_Object = MibTableColumn
slSonetTraceMode = _SlSonetTraceMode_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 2, 1, 1, 1, 1),
    _SlSonetTraceMode_Type()
)
slSonetTraceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slSonetTraceMode.setStatus("current")


class _SlSonetTraceToTransmit_Type(DisplayString):
    """Custom type slSonetTraceToTransmit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 62),
    )


_SlSonetTraceToTransmit_Type.__name__ = "DisplayString"
_SlSonetTraceToTransmit_Object = MibTableColumn
slSonetTraceToTransmit = _SlSonetTraceToTransmit_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 2, 1, 1, 1, 2),
    _SlSonetTraceToTransmit_Type()
)
slSonetTraceToTransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slSonetTraceToTransmit.setStatus("current")


class _SlSonetTraceToExpect_Type(DisplayString):
    """Custom type slSonetTraceToExpect based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 62),
    )


_SlSonetTraceToExpect_Type.__name__ = "DisplayString"
_SlSonetTraceToExpect_Object = MibTableColumn
slSonetTraceToExpect = _SlSonetTraceToExpect_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 2, 1, 1, 1, 3),
    _SlSonetTraceToExpect_Type()
)
slSonetTraceToExpect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slSonetTraceToExpect.setStatus("current")
_SlSonetTraceFailure_Type = TruthValue
_SlSonetTraceFailure_Object = MibTableColumn
slSonetTraceFailure = _SlSonetTraceFailure_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 2, 1, 1, 1, 4),
    _SlSonetTraceFailure_Type()
)
slSonetTraceFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slSonetTraceFailure.setStatus("current")


class _SlSonetTraceReceived_Type(DisplayString):
    """Custom type slSonetTraceReceived based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 62),
    )


_SlSonetTraceReceived_Type.__name__ = "DisplayString"
_SlSonetTraceReceived_Object = MibTableColumn
slSonetTraceReceived = _SlSonetTraceReceived_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 2, 1, 1, 1, 5),
    _SlSonetTraceReceived_Type()
)
slSonetTraceReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slSonetTraceReceived.setStatus("current")
_SlSonetOhSl_ObjectIdentity = ObjectIdentity
slSonetOhSl = _SlSonetOhSl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 2, 2)
)
_SlSonetSlTable_Object = MibTable
slSonetSlTable = _SlSonetSlTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 2, 2, 1)
)
if mibBuilder.loadTexts:
    slSonetSlTable.setStatus("current")
_SlSonetSlEntry_Object = MibTableRow
slSonetSlEntry = _SlSonetSlEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 2, 2, 1, 1)
)
slSonetSlEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    slSonetSlEntry.setStatus("current")
_SlSonetSlToTransmit_Type = SignalLabel
_SlSonetSlToTransmit_Object = MibTableColumn
slSonetSlToTransmit = _SlSonetSlToTransmit_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 2, 2, 1, 1, 2),
    _SlSonetSlToTransmit_Type()
)
slSonetSlToTransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slSonetSlToTransmit.setStatus("current")
_SlSonetSlToExpect_Type = SignalLabel
_SlSonetSlToExpect_Object = MibTableColumn
slSonetSlToExpect = _SlSonetSlToExpect_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 2, 2, 1, 1, 3),
    _SlSonetSlToExpect_Type()
)
slSonetSlToExpect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slSonetSlToExpect.setStatus("current")
_SlSonetSlFailure_Type = TruthValue
_SlSonetSlFailure_Object = MibTableColumn
slSonetSlFailure = _SlSonetSlFailure_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 2, 2, 1, 1, 4),
    _SlSonetSlFailure_Type()
)
slSonetSlFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slSonetSlFailure.setStatus("current")


class _SlSonetSlReceived_Type(Integer32):
    """Custom type slSonetSlReceived based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SlSonetSlReceived_Type.__name__ = "Integer32"
_SlSonetSlReceived_Object = MibTableColumn
slSonetSlReceived = _SlSonetSlReceived_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 2, 2, 1, 1, 5),
    _SlSonetSlReceived_Type()
)
slSonetSlReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slSonetSlReceived.setStatus("current")
_SlSonetOhTraps_ObjectIdentity = ObjectIdentity
slSonetOhTraps = _SlSonetOhTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 2, 3)
)
_SlSonetPos_ObjectIdentity = ObjectIdentity
slSonetPos = _SlSonetPos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 6)
)
_SlSonetPosTable_Object = MibTable
slSonetPosTable = _SlSonetPosTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 6, 1)
)
if mibBuilder.loadTexts:
    slSonetPosTable.setStatus("current")
_SlSonetPosEntry_Object = MibTableRow
slSonetPosEntry = _SlSonetPosEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 6, 1, 1)
)
slSonetPosEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    slSonetPosEntry.setStatus("current")
_SlSonetPosFcs_Type = Gauge32
_SlSonetPosFcs_Object = MibTableColumn
slSonetPosFcs = _SlSonetPosFcs_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 6, 1, 1, 1),
    _SlSonetPosFcs_Type()
)
slSonetPosFcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slSonetPosFcs.setStatus("current")
_SlSonetPosAbort_Type = Gauge32
_SlSonetPosAbort_Object = MibTableColumn
slSonetPosAbort = _SlSonetPosAbort_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 6, 1, 1, 2),
    _SlSonetPosAbort_Type()
)
slSonetPosAbort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slSonetPosAbort.setStatus("current")
_SlSonetPosMinViolation_Type = Gauge32
_SlSonetPosMinViolation_Object = MibTableColumn
slSonetPosMinViolation = _SlSonetPosMinViolation_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 6, 1, 1, 3),
    _SlSonetPosMinViolation_Type()
)
slSonetPosMinViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slSonetPosMinViolation.setStatus("current")
_SlSonetPosMaxViolation_Type = Gauge32
_SlSonetPosMaxViolation_Object = MibTableColumn
slSonetPosMaxViolation = _SlSonetPosMaxViolation_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 6, 1, 1, 4),
    _SlSonetPosMaxViolation_Type()
)
slSonetPosMaxViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slSonetPosMaxViolation.setStatus("current")
_SlSonetPosRxfifoDiscard_Type = Gauge32
_SlSonetPosRxfifoDiscard_Object = MibTableColumn
slSonetPosRxfifoDiscard = _SlSonetPosRxfifoDiscard_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 6, 1, 1, 5),
    _SlSonetPosRxfifoDiscard_Type()
)
slSonetPosRxfifoDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slSonetPosRxfifoDiscard.setStatus("current")
_SlSonetPosPacketReceived_Type = Counter64
_SlSonetPosPacketReceived_Object = MibTableColumn
slSonetPosPacketReceived = _SlSonetPosPacketReceived_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 6, 1, 1, 6),
    _SlSonetPosPacketReceived_Type()
)
slSonetPosPacketReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slSonetPosPacketReceived.setStatus("current")
_SlSonetPosPacketReceivedOk_Type = Counter64
_SlSonetPosPacketReceivedOk_Object = MibTableColumn
slSonetPosPacketReceivedOk = _SlSonetPosPacketReceivedOk_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 6, 1, 1, 7),
    _SlSonetPosPacketReceivedOk_Type()
)
slSonetPosPacketReceivedOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slSonetPosPacketReceivedOk.setStatus("current")
_SlSonetAls_ObjectIdentity = ObjectIdentity
slSonetAls = _SlSonetAls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 7)
)
_SlSonetAlsTable_Object = MibTable
slSonetAlsTable = _SlSonetAlsTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 7, 1)
)
if mibBuilder.loadTexts:
    slSonetAlsTable.setStatus("current")
_SlSonetAlsEntry_Object = MibTableRow
slSonetAlsEntry = _SlSonetAlsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 7, 1, 1)
)
slSonetAlsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    slSonetAlsEntry.setStatus("current")


class _SlSonetAlsMode_Type(Integer32):
    """Custom type slSonetAlsMode based on Integer32"""
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


_SlSonetAlsMode_Type.__name__ = "Integer32"
_SlSonetAlsMode_Object = MibTableColumn
slSonetAlsMode = _SlSonetAlsMode_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 7, 1, 1, 1),
    _SlSonetAlsMode_Type()
)
slSonetAlsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slSonetAlsMode.setStatus("current")


class _SlSonetLosDeclareTime_Type(Integer32):
    """Custom type slSonetLosDeclareTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ms500", 1),
          ("ms550", 2),
          ("ms600", 3))
    )


_SlSonetLosDeclareTime_Type.__name__ = "Integer32"
_SlSonetLosDeclareTime_Object = MibTableColumn
slSonetLosDeclareTime = _SlSonetLosDeclareTime_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 7, 1, 1, 2),
    _SlSonetLosDeclareTime_Type()
)
slSonetLosDeclareTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slSonetLosDeclareTime.setStatus("current")


class _SlSonetTestPulseTime_Type(Integer32):
    """Custom type slSonetTestPulseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("s80", 1),
          ("s90", 2),
          ("s100", 3))
    )


_SlSonetTestPulseTime_Type.__name__ = "Integer32"
_SlSonetTestPulseTime_Object = MibTableColumn
slSonetTestPulseTime = _SlSonetTestPulseTime_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 7, 1, 1, 3),
    _SlSonetTestPulseTime_Type()
)
slSonetTestPulseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slSonetTestPulseTime.setStatus("current")


class _SlSonetManualPulseTime_Type(Integer32):
    """Custom type slSonetManualPulseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ms1750", 1),
          ("ms2000", 2),
          ("ms2250", 3))
    )


_SlSonetManualPulseTime_Type.__name__ = "Integer32"
_SlSonetManualPulseTime_Object = MibTableColumn
slSonetManualPulseTime = _SlSonetManualPulseTime_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 7, 1, 1, 4),
    _SlSonetManualPulseTime_Type()
)
slSonetManualPulseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slSonetManualPulseTime.setStatus("current")


class _SlSonetAutomaticPulseTime_Type(Integer32):
    """Custom type slSonetAutomaticPulseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ms1750", 1),
          ("ms2000", 2),
          ("ms2250", 3))
    )


_SlSonetAutomaticPulseTime_Type.__name__ = "Integer32"
_SlSonetAutomaticPulseTime_Object = MibTableColumn
slSonetAutomaticPulseTime = _SlSonetAutomaticPulseTime_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 7, 1, 1, 5),
    _SlSonetAutomaticPulseTime_Type()
)
slSonetAutomaticPulseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slSonetAutomaticPulseTime.setStatus("current")


class _SlSonetAutomaticDelayTime_Type(Integer32):
    """Custom type slSonetAutomaticDelayTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 300),
    )


_SlSonetAutomaticDelayTime_Type.__name__ = "Integer32"
_SlSonetAutomaticDelayTime_Object = MibTableColumn
slSonetAutomaticDelayTime = _SlSonetAutomaticDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 7, 1, 1, 6),
    _SlSonetAutomaticDelayTime_Type()
)
slSonetAutomaticDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slSonetAutomaticDelayTime.setStatus("current")


class _SlSonetLaserTestActivate_Type(Integer32):
    """Custom type slSonetLaserTestActivate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("activate", 1)
    )


_SlSonetLaserTestActivate_Type.__name__ = "Integer32"
_SlSonetLaserTestActivate_Object = MibTableColumn
slSonetLaserTestActivate = _SlSonetLaserTestActivate_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 7, 1, 1, 7),
    _SlSonetLaserTestActivate_Type()
)
slSonetLaserTestActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slSonetLaserTestActivate.setStatus("current")


class _SlSonetLaserManualActivate_Type(Integer32):
    """Custom type slSonetLaserManualActivate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("activate", 1)
    )


_SlSonetLaserManualActivate_Type.__name__ = "Integer32"
_SlSonetLaserManualActivate_Object = MibTableColumn
slSonetLaserManualActivate = _SlSonetLaserManualActivate_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 7, 1, 1, 8),
    _SlSonetLaserManualActivate_Type()
)
slSonetLaserManualActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slSonetLaserManualActivate.setStatus("current")
_SlSonetFs_ObjectIdentity = ObjectIdentity
slSonetFs = _SlSonetFs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 8)
)
_SlSonetFsTable_Object = MibTable
slSonetFsTable = _SlSonetFsTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 8, 1)
)
if mibBuilder.loadTexts:
    slSonetFsTable.setStatus("current")
_SlSonetFsEntry_Object = MibTableRow
slSonetFsEntry = _SlSonetFsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 8, 1, 1)
)
slSonetFsEntry.setIndexNames(
    (0, "SL-SONET-MIB", "slSonetFsIfIndex"),
    (0, "SL-SONET-MIB", "slSonetFsSts"),
)
if mibBuilder.loadTexts:
    slSonetFsEntry.setStatus("current")
_SlSonetFsIfIndex_Type = InterfaceIndex
_SlSonetFsIfIndex_Object = MibTableColumn
slSonetFsIfIndex = _SlSonetFsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 8, 1, 1, 1),
    _SlSonetFsIfIndex_Type()
)
slSonetFsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slSonetFsIfIndex.setStatus("current")
_SlSonetFsSts_Type = Integer32
_SlSonetFsSts_Object = MibTableColumn
slSonetFsSts = _SlSonetFsSts_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 8, 1, 1, 2),
    _SlSonetFsSts_Type()
)
slSonetFsSts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slSonetFsSts.setStatus("current")
_SlSonetFsWidth_Type = Integer32
_SlSonetFsWidth_Object = MibTableColumn
slSonetFsWidth = _SlSonetFsWidth_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 8, 1, 1, 3),
    _SlSonetFsWidth_Type()
)
slSonetFsWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slSonetFsWidth.setStatus("current")
_SlSonetFsFullPathTermination_Type = TruthValue
_SlSonetFsFullPathTermination_Object = MibTableColumn
slSonetFsFullPathTermination = _SlSonetFsFullPathTermination_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 8, 1, 1, 4),
    _SlSonetFsFullPathTermination_Type()
)
slSonetFsFullPathTermination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slSonetFsFullPathTermination.setStatus("current")


class _SlSonetFsGranularity_Type(Integer32):
    """Custom type slSonetFsGranularity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vc4", 1),
          ("vc3", 2))
    )


_SlSonetFsGranularity_Type.__name__ = "Integer32"
_SlSonetFsGranularity_Object = MibTableColumn
slSonetFsGranularity = _SlSonetFsGranularity_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 8, 1, 1, 5),
    _SlSonetFsGranularity_Type()
)
slSonetFsGranularity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slSonetFsGranularity.setStatus("current")
_SlSonetTraps_ObjectIdentity = ObjectIdentity
slSonetTraps = _SlSonetTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 11)
)

# Managed Objects groups


# Notification objects

slSonetFsTableChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 11, 1)
)
slSonetFsTableChange.setObjects(
    ("SL-SONET-MIB", "slSonetFsIfIndex")
)
if mibBuilder.loadTexts:
    slSonetFsTableChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SL-SONET-MIB",
    **{"SignalLabel": SignalLabel,
       "slSonetMib": slSonetMib,
       "slSonetConfig": slSonetConfig,
       "slSonetConfigTable": slSonetConfigTable,
       "slSonetConfigEntry": slSonetConfigEntry,
       "slSonetConfigFrameScramble": slSonetConfigFrameScramble,
       "slSonetConfigType": slSonetConfigType,
       "slSonetConfigDccSelection": slSonetConfigDccSelection,
       "slSonetResetAllCounters": slSonetResetAllCounters,
       "slSonetPortThresholdTrapEnable": slSonetPortThresholdTrapEnable,
       "slSonetConfigSdThreshold": slSonetConfigSdThreshold,
       "slSonetConfigSfThreshold": slSonetConfigSfThreshold,
       "slSonetCompression": slSonetCompression,
       "slSonetOverheadTunneling": slSonetOverheadTunneling,
       "slSonetLopBitmask": slSonetLopBitmask,
       "slSonetTdmTrunk": slSonetTdmTrunk,
       "slSonetFsApply": slSonetFsApply,
       "slSonetTxLte": slSonetTxLte,
       "slSonetReceivedLte": slSonetReceivedLte,
       "slSonetResetPmThreshold": slSonetResetPmThreshold,
       "slSonetResetAlsParams": slSonetResetAlsParams,
       "slSonetTransceiverType": slSonetTransceiverType,
       "slSonetTransceiverMedia": slSonetTransceiverMedia,
       "slSonetOh": slSonetOh,
       "slSonetOhTrace": slSonetOhTrace,
       "slSonetTraceTable": slSonetTraceTable,
       "slSonetTraceEntry": slSonetTraceEntry,
       "slSonetTraceMode": slSonetTraceMode,
       "slSonetTraceToTransmit": slSonetTraceToTransmit,
       "slSonetTraceToExpect": slSonetTraceToExpect,
       "slSonetTraceFailure": slSonetTraceFailure,
       "slSonetTraceReceived": slSonetTraceReceived,
       "slSonetOhSl": slSonetOhSl,
       "slSonetSlTable": slSonetSlTable,
       "slSonetSlEntry": slSonetSlEntry,
       "slSonetSlToTransmit": slSonetSlToTransmit,
       "slSonetSlToExpect": slSonetSlToExpect,
       "slSonetSlFailure": slSonetSlFailure,
       "slSonetSlReceived": slSonetSlReceived,
       "slSonetOhTraps": slSonetOhTraps,
       "slSonetPos": slSonetPos,
       "slSonetPosTable": slSonetPosTable,
       "slSonetPosEntry": slSonetPosEntry,
       "slSonetPosFcs": slSonetPosFcs,
       "slSonetPosAbort": slSonetPosAbort,
       "slSonetPosMinViolation": slSonetPosMinViolation,
       "slSonetPosMaxViolation": slSonetPosMaxViolation,
       "slSonetPosRxfifoDiscard": slSonetPosRxfifoDiscard,
       "slSonetPosPacketReceived": slSonetPosPacketReceived,
       "slSonetPosPacketReceivedOk": slSonetPosPacketReceivedOk,
       "slSonetAls": slSonetAls,
       "slSonetAlsTable": slSonetAlsTable,
       "slSonetAlsEntry": slSonetAlsEntry,
       "slSonetAlsMode": slSonetAlsMode,
       "slSonetLosDeclareTime": slSonetLosDeclareTime,
       "slSonetTestPulseTime": slSonetTestPulseTime,
       "slSonetManualPulseTime": slSonetManualPulseTime,
       "slSonetAutomaticPulseTime": slSonetAutomaticPulseTime,
       "slSonetAutomaticDelayTime": slSonetAutomaticDelayTime,
       "slSonetLaserTestActivate": slSonetLaserTestActivate,
       "slSonetLaserManualActivate": slSonetLaserManualActivate,
       "slSonetFs": slSonetFs,
       "slSonetFsTable": slSonetFsTable,
       "slSonetFsEntry": slSonetFsEntry,
       "slSonetFsIfIndex": slSonetFsIfIndex,
       "slSonetFsSts": slSonetFsSts,
       "slSonetFsWidth": slSonetFsWidth,
       "slSonetFsFullPathTermination": slSonetFsFullPathTermination,
       "slSonetFsGranularity": slSonetFsGranularity,
       "slSonetTraps": slSonetTraps,
       "slSonetFsTableChange": slSonetFsTableChange}
)
