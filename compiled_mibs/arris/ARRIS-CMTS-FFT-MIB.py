# SNMP MIB module (ARRIS-CMTS-FFT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arris\ARRIS-CMTS-FFT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:18:12 2025
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

(cmtsCommon,) = mibBuilder.importSymbols(
    "ARRIS-MIB",
    "cmtsCommon")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cmtsFftMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 5, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DcxFftPayloadBuffer(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



# MIB Managed Objects in the order of their OIDs

_DcxFftObjects_ObjectIdentity = ObjectIdentity
dcxFftObjects = _DcxFftObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 5, 1, 1)
)
_DcxFftUpstreamChannelTable_Object = MibTable
dcxFftUpstreamChannelTable = _DcxFftUpstreamChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 5, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dcxFftUpstreamChannelTable.setStatus("current")
_DcxFftUpstreamChannelEntry_Object = MibTableRow
dcxFftUpstreamChannelEntry = _DcxFftUpstreamChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 5, 1, 1, 1, 1)
)
dcxFftUpstreamChannelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dcxFftUpstreamChannelEntry.setStatus("current")


class _DcxFftSize_Type(Unsigned32):
    """Custom type dcxFftSize based on Unsigned32"""
    defaultValue = 2048


_DcxFftSize_Type.__name__ = "Unsigned32"
_DcxFftSize_Object = MibTableColumn
dcxFftSize = _DcxFftSize_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 5, 1, 1, 1, 1, 1),
    _DcxFftSize_Type()
)
dcxFftSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxFftSize.setStatus("current")


class _DcxFftSampleRate_Type(Integer32):
    """Custom type dcxFftSampleRate based on Integer32"""
    defaultValue = 2

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
        *(("adcRate", 1),
          ("halfAdcRate", 2),
          ("quarterAdcRate", 3),
          ("quadrupleSymbolRate", 4))
    )


_DcxFftSampleRate_Type.__name__ = "Integer32"
_DcxFftSampleRate_Object = MibTableColumn
dcxFftSampleRate = _DcxFftSampleRate_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 5, 1, 1, 1, 1, 2),
    _DcxFftSampleRate_Type()
)
dcxFftSampleRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxFftSampleRate.setStatus("current")


class _DcxFftCentreFrequency_Type(Integer32):
    """Custom type dcxFftCentreFrequency based on Integer32"""
    defaultValue = 40960000


_DcxFftCentreFrequency_Type.__name__ = "Integer32"
_DcxFftCentreFrequency_Object = MibTableColumn
dcxFftCentreFrequency = _DcxFftCentreFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 5, 1, 1, 1, 1, 3),
    _DcxFftCentreFrequency_Type()
)
dcxFftCentreFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxFftCentreFrequency.setStatus("current")
if mibBuilder.loadTexts:
    dcxFftCentreFrequency.setUnits("hertz")


class _DcxFftWindowing_Type(Integer32):
    """Custom type dcxFftWindowing based on Integer32"""
    defaultValue = 5

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
        *(("rectangular", 1),
          ("hanning", 2),
          ("hamming", 3),
          ("blackman", 4),
          ("blackmanHarris", 5))
    )


_DcxFftWindowing_Type.__name__ = "Integer32"
_DcxFftWindowing_Object = MibTableColumn
dcxFftWindowing = _DcxFftWindowing_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 5, 1, 1, 1, 1, 4),
    _DcxFftWindowing_Type()
)
dcxFftWindowing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxFftWindowing.setStatus("current")


class _DcxFftLogAveragingTimeConstant_Type(Unsigned32):
    """Custom type dcxFftLogAveragingTimeConstant based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DcxFftLogAveragingTimeConstant_Type.__name__ = "Unsigned32"
_DcxFftLogAveragingTimeConstant_Object = MibTableColumn
dcxFftLogAveragingTimeConstant = _DcxFftLogAveragingTimeConstant_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 5, 1, 1, 1, 1, 5),
    _DcxFftLogAveragingTimeConstant_Type()
)
dcxFftLogAveragingTimeConstant.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxFftLogAveragingTimeConstant.setStatus("current")


class _DcxFftOutputFormat_Type(Integer32):
    """Custom type dcxFftOutputFormat based on Integer32"""
    defaultValue = 4

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
        *(("raw", 1),
          ("fftIQ", 2),
          ("fftPower", 3),
          ("fftAmplitude", 4))
    )


_DcxFftOutputFormat_Type.__name__ = "Integer32"
_DcxFftOutputFormat_Object = MibTableColumn
dcxFftOutputFormat = _DcxFftOutputFormat_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 5, 1, 1, 1, 1, 6),
    _DcxFftOutputFormat_Type()
)
dcxFftOutputFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxFftOutputFormat.setStatus("current")


class _DcxFftOperatingMode_Type(Integer32):
    """Custom type dcxFftOperatingMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("baseSpectrum", 1),
          ("burstSpectrum", 2),
          ("periodicSpectrum", 3))
    )


_DcxFftOperatingMode_Type.__name__ = "Integer32"
_DcxFftOperatingMode_Object = MibTableColumn
dcxFftOperatingMode = _DcxFftOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 5, 1, 1, 1, 1, 7),
    _DcxFftOperatingMode_Type()
)
dcxFftOperatingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxFftOperatingMode.setStatus("current")


class _DcxFftIdleInterval_Type(Unsigned32):
    """Custom type dcxFftIdleInterval based on Unsigned32"""
    defaultValue = 50000


_DcxFftIdleInterval_Type.__name__ = "Unsigned32"
_DcxFftIdleInterval_Object = MibTableColumn
dcxFftIdleInterval = _DcxFftIdleInterval_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 5, 1, 1, 1, 1, 8),
    _DcxFftIdleInterval_Type()
)
dcxFftIdleInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxFftIdleInterval.setStatus("current")


class _DcxFftBurstSid_Type(Unsigned32):
    """Custom type dcxFftBurstSid based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_DcxFftBurstSid_Type.__name__ = "Unsigned32"
_DcxFftBurstSid_Object = MibTableColumn
dcxFftBurstSid = _DcxFftBurstSid_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 5, 1, 1, 1, 1, 9),
    _DcxFftBurstSid_Type()
)
dcxFftBurstSid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxFftBurstSid.setStatus("current")


class _DcxFftBurstIUC_Type(Integer32):
    """Custom type dcxFftBurstIUC based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_DcxFftBurstIUC_Type.__name__ = "Integer32"
_DcxFftBurstIUC_Object = MibTableColumn
dcxFftBurstIUC = _DcxFftBurstIUC_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 5, 1, 1, 1, 1, 10),
    _DcxFftBurstIUC_Type()
)
dcxFftBurstIUC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxFftBurstIUC.setStatus("current")


class _DcxFftLogicalChannel_Type(Integer32):
    """Custom type dcxFftLogicalChannel based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 3),
    )


_DcxFftLogicalChannel_Type.__name__ = "Integer32"
_DcxFftLogicalChannel_Object = MibTableColumn
dcxFftLogicalChannel = _DcxFftLogicalChannel_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 5, 1, 1, 1, 1, 11),
    _DcxFftLogicalChannel_Type()
)
dcxFftLogicalChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxFftLogicalChannel.setStatus("current")


class _DcxFftTriggerCount_Type(Unsigned32):
    """Custom type dcxFftTriggerCount based on Unsigned32"""
    defaultValue = 0


_DcxFftTriggerCount_Type.__name__ = "Unsigned32"
_DcxFftTriggerCount_Object = MibTableColumn
dcxFftTriggerCount = _DcxFftTriggerCount_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 5, 1, 1, 1, 1, 12),
    _DcxFftTriggerCount_Type()
)
dcxFftTriggerCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxFftTriggerCount.setStatus("current")


class _DcxFftEnable_Type(TruthValue):
    """Custom type dcxFftEnable based on TruthValue"""
    defaultValue = 2


_DcxFftEnable_Type.__name__ = "TruthValue"
_DcxFftEnable_Object = MibTableColumn
dcxFftEnable = _DcxFftEnable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 5, 1, 1, 1, 1, 13),
    _DcxFftEnable_Type()
)
dcxFftEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxFftEnable.setStatus("current")
_DcxFftApplyConfig_Type = TruthValue
_DcxFftApplyConfig_Object = MibTableColumn
dcxFftApplyConfig = _DcxFftApplyConfig_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 5, 1, 1, 1, 1, 14),
    _DcxFftApplyConfig_Type()
)
dcxFftApplyConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxFftApplyConfig.setStatus("current")
_DcxFftInProgress_Type = TruthValue
_DcxFftInProgress_Object = MibTableColumn
dcxFftInProgress = _DcxFftInProgress_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 5, 1, 1, 1, 1, 15),
    _DcxFftInProgress_Type()
)
dcxFftInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxFftInProgress.setStatus("current")
_DcxFftCurrentTriggers_Type = Unsigned32
_DcxFftCurrentTriggers_Object = MibTableColumn
dcxFftCurrentTriggers = _DcxFftCurrentTriggers_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 5, 1, 1, 1, 1, 16),
    _DcxFftCurrentTriggers_Type()
)
dcxFftCurrentTriggers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxFftCurrentTriggers.setStatus("current")
_DcxFftPayloadTable_Object = MibTable
dcxFftPayloadTable = _DcxFftPayloadTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 5, 1, 1, 2)
)
if mibBuilder.loadTexts:
    dcxFftPayloadTable.setStatus("current")
_DcxFftPayloadEntry_Object = MibTableRow
dcxFftPayloadEntry = _DcxFftPayloadEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 5, 1, 1, 2, 1)
)
dcxFftPayloadEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ARRIS-CMTS-FFT-MIB", "dcxFftPayloadIndex"),
)
if mibBuilder.loadTexts:
    dcxFftPayloadEntry.setStatus("current")
_DcxFftPayloadIndex_Type = Unsigned32
_DcxFftPayloadIndex_Object = MibTableColumn
dcxFftPayloadIndex = _DcxFftPayloadIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 5, 1, 1, 2, 1, 1),
    _DcxFftPayloadIndex_Type()
)
dcxFftPayloadIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcxFftPayloadIndex.setStatus("current")
_DcxFftPayloadData_Type = DcxFftPayloadBuffer
_DcxFftPayloadData_Object = MibTableColumn
dcxFftPayloadData = _DcxFftPayloadData_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 5, 1, 1, 2, 1, 2),
    _DcxFftPayloadData_Type()
)
dcxFftPayloadData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxFftPayloadData.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARRIS-CMTS-FFT-MIB",
    **{"DcxFftPayloadBuffer": DcxFftPayloadBuffer,
       "cmtsFftMIB": cmtsFftMIB,
       "dcxFftObjects": dcxFftObjects,
       "dcxFftUpstreamChannelTable": dcxFftUpstreamChannelTable,
       "dcxFftUpstreamChannelEntry": dcxFftUpstreamChannelEntry,
       "dcxFftSize": dcxFftSize,
       "dcxFftSampleRate": dcxFftSampleRate,
       "dcxFftCentreFrequency": dcxFftCentreFrequency,
       "dcxFftWindowing": dcxFftWindowing,
       "dcxFftLogAveragingTimeConstant": dcxFftLogAveragingTimeConstant,
       "dcxFftOutputFormat": dcxFftOutputFormat,
       "dcxFftOperatingMode": dcxFftOperatingMode,
       "dcxFftIdleInterval": dcxFftIdleInterval,
       "dcxFftBurstSid": dcxFftBurstSid,
       "dcxFftBurstIUC": dcxFftBurstIUC,
       "dcxFftLogicalChannel": dcxFftLogicalChannel,
       "dcxFftTriggerCount": dcxFftTriggerCount,
       "dcxFftEnable": dcxFftEnable,
       "dcxFftApplyConfig": dcxFftApplyConfig,
       "dcxFftInProgress": dcxFftInProgress,
       "dcxFftCurrentTriggers": dcxFftCurrentTriggers,
       "dcxFftPayloadTable": dcxFftPayloadTable,
       "dcxFftPayloadEntry": dcxFftPayloadEntry,
       "dcxFftPayloadIndex": dcxFftPayloadIndex,
       "dcxFftPayloadData": dcxFftPayloadData}
)
