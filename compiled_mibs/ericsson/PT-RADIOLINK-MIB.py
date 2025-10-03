# SNMP MIB module (PT-RADIOLINK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ericsson\PT-RADIOLINK-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:42:39 2025
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

(ifEntry,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifEntry")

(InetAddressIPv6,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv6")

(pt,) = mibBuilder.importSymbols(
    "PT-MIB",
    "pt")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ptRadioLink = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7)
)
if mibBuilder.loadTexts:
    ptRadioLink.setRevisions(
        ("2017-12-01 16:00",
         "2017-04-05 10:00",
         "2017-01-18 10:00",
         "2016-12-06 14:00",
         "2016-05-22 10:30")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AcmTC(TextualConvention, Integer32):
    status = "current"
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36)
        )
    )
    namedValues = NamedValues(
        *(("acmHalfBpsk", 1),
          ("acmHalfBpskLight", 2),
          ("acmHalfBpskStrong", 3),
          ("acmBpsk", 4),
          ("acmBpskLight", 5),
          ("acmBpskStrong", 6),
          ("acm4Qam", 7),
          ("acm4QamLight", 8),
          ("acm4QamStrong", 9),
          ("acm16Qam", 10),
          ("acm16QamLight", 11),
          ("acm16QamStrong", 12),
          ("acm32Qam", 13),
          ("acm32QamLight", 14),
          ("acm32QamStrong", 15),
          ("acm64Qam", 16),
          ("acm64QamLight", 17),
          ("acm64QamStrong", 18),
          ("acm128Qam", 19),
          ("acm128QamLight", 20),
          ("acm128QamStrong", 21),
          ("acm256Qam", 22),
          ("acm256QamLight", 23),
          ("acm256QamStrong", 24),
          ("acm512Qam", 25),
          ("acm512QamLight", 26),
          ("acm512QamStrong", 27),
          ("acm1024Qam", 28),
          ("acm1024QamLight", 29),
          ("acm1024QamStrong", 30),
          ("acm2048Qam", 31),
          ("acm2048QamLight", 32),
          ("acm2048QamStrong", 33),
          ("acm4096Qam", 34),
          ("acm4096QamLight", 35),
          ("acm4096QamStrong", 36))
    )



class EnableStatusTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("unknown", 3))
    )



class XpicMimoTC(TextualConvention, Integer32):
    status = "current"
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
        *(("notAvailable", 1),
          ("locked", 2),
          ("unlocked", 3),
          ("unknown", 4))
    )



# MIB Managed Objects in the order of their OIDs

_CtTable_Object = MibTable
ctTable = _CtTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1)
)
if mibBuilder.loadTexts:
    ctTable.setStatus("current")
_CtEntry_Object = MibTableRow
ctEntry = _CtEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1)
)
if mibBuilder.loadTexts:
    ctEntry.setStatus("current")
_ActualInputPower_Type = OctetString
_ActualInputPower_Object = MibTableColumn
actualInputPower = _ActualInputPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 1),
    _ActualInputPower_Type()
)
actualInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actualInputPower.setStatus("current")
_ActualOutputPower_Type = OctetString
_ActualOutputPower_Object = MibTableColumn
actualOutputPower = _ActualOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 2),
    _ActualOutputPower_Type()
)
actualOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actualOutputPower.setStatus("current")
_ActualRxAcm_Type = OctetString
_ActualRxAcm_Object = MibTableColumn
actualRxAcm = _ActualRxAcm_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 3),
    _ActualRxAcm_Type()
)
actualRxAcm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actualRxAcm.setStatus("current")
_ActualTxAcm_Type = OctetString
_ActualTxAcm_Object = MibTableColumn
actualTxAcm = _ActualTxAcm_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 4),
    _ActualTxAcm_Type()
)
actualTxAcm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actualTxAcm.setStatus("current")
_CtDistinguishedName_Type = OctetString
_CtDistinguishedName_Object = MibTableColumn
ctDistinguishedName = _CtDistinguishedName_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 5),
    _CtDistinguishedName_Type()
)
ctDistinguishedName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDistinguishedName.setStatus("current")
_Description_Type = OctetString
_Description_Object = MibTableColumn
description = _Description_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 6),
    _Description_Type()
)
description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    description.setStatus("current")


class _CarrierId_Type(Integer32):
    """Custom type carrierId based on Integer32"""
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
        *(("a", 1),
          ("b", 2),
          ("c", 3),
          ("d", 4),
          ("unknown", 5))
    )


_CarrierId_Type.__name__ = "Integer32"
_CarrierId_Object = MibTableColumn
carrierId = _CarrierId_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 7),
    _CarrierId_Type()
)
carrierId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    carrierId.setStatus("current")


class _CtStatus_Type(Integer32):
    """Custom type ctStatus based on Integer32"""
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
        *(("down", 1),
          ("up", 2),
          ("na", 3),
          ("unknown", 4),
          ("degraded", 5))
    )


_CtStatus_Type.__name__ = "Integer32"
_CtStatus_Object = MibTableColumn
ctStatus = _CtStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 8),
    _CtStatus_Type()
)
ctStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctStatus.setStatus("current")


class _FrameId_Type(Integer32):
    """Custom type frameId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_FrameId_Type.__name__ = "Integer32"
_FrameId_Object = MibTableColumn
frameId = _FrameId_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 9),
    _FrameId_Type()
)
frameId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frameId.setStatus("current")
_TxFrequency_Type = Integer32
_TxFrequency_Object = MibTableColumn
txFrequency = _TxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 10),
    _TxFrequency_Type()
)
txFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txFrequency.setStatus("current")
_MinTxFrequency_Type = Integer32
_MinTxFrequency_Object = MibTableColumn
minTxFrequency = _MinTxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 11),
    _MinTxFrequency_Type()
)
minTxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minTxFrequency.setStatus("current")
_MaxTxFrequency_Type = Integer32
_MaxTxFrequency_Object = MibTableColumn
maxTxFrequency = _MaxTxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 12),
    _MaxTxFrequency_Type()
)
maxTxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxTxFrequency.setStatus("current")
_RxFrequency_Type = Integer32
_RxFrequency_Object = MibTableColumn
rxFrequency = _RxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 13),
    _RxFrequency_Type()
)
rxFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rxFrequency.setStatus("current")
_MinRxFrequency_Type = Integer32
_MinRxFrequency_Object = MibTableColumn
minRxFrequency = _MinRxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 14),
    _MinRxFrequency_Type()
)
minRxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minRxFrequency.setStatus("current")
_MaxRxFrequency_Type = Integer32
_MaxRxFrequency_Object = MibTableColumn
maxRxFrequency = _MaxRxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 15),
    _MaxRxFrequency_Type()
)
maxRxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxRxFrequency.setStatus("current")
_FrequencyStepSize_Type = Integer32
_FrequencyStepSize_Object = MibTableColumn
frequencyStepSize = _FrequencyStepSize_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 16),
    _FrequencyStepSize_Type()
)
frequencyStepSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frequencyStepSize.setStatus("current")
_DuplexDistance_Type = Integer32
_DuplexDistance_Object = MibTableColumn
duplexDistance = _DuplexDistance_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 17),
    _DuplexDistance_Type()
)
duplexDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    duplexDistance.setStatus("current")


class _DuplexType_Type(Integer32):
    """Custom type duplexType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("variable", 1),
          ("fixed", 2),
          ("unknown", 3))
    )


_DuplexType_Type.__name__ = "Integer32"
_DuplexType_Object = MibTableColumn
duplexType = _DuplexType_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 18),
    _DuplexType_Type()
)
duplexType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    duplexType.setStatus("current")
_DuplexConfig_Type = EnableStatusTC
_DuplexConfig_Object = MibTableColumn
duplexConfig = _DuplexConfig_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 19),
    _DuplexConfig_Type()
)
duplexConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    duplexConfig.setStatus("current")


class _AutoFreqSelection_Type(Integer32):
    """Custom type autoFreqSelection based on Integer32"""
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
        *(("disabled", 1),
          ("master", 2),
          ("slave", 3),
          ("unknown", 4))
    )


_AutoFreqSelection_Type.__name__ = "Integer32"
_AutoFreqSelection_Object = MibTableColumn
autoFreqSelection = _AutoFreqSelection_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 20),
    _AutoFreqSelection_Type()
)
autoFreqSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoFreqSelection.setStatus("current")
_AutoFreqSelectedChannel_Type = Integer32
_AutoFreqSelectedChannel_Object = MibTableColumn
autoFreqSelectedChannel = _AutoFreqSelectedChannel_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 21),
    _AutoFreqSelectedChannel_Type()
)
autoFreqSelectedChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoFreqSelectedChannel.setStatus("current")


class _AutoFreqSelectionStatus_Type(Integer32):
    """Custom type autoFreqSelectionStatus based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("searchingForSlave", 2),
          ("requestingInfoFromSlave", 3),
          ("waitingForMaster", 4),
          ("waitingForChannelInfoRequest", 5),
          ("inProgress", 6),
          ("initializing", 7),
          ("finished", 8),
          ("failed", 9),
          ("unknown", 10))
    )


_AutoFreqSelectionStatus_Type.__name__ = "Integer32"
_AutoFreqSelectionStatus_Object = MibTableColumn
autoFreqSelectionStatus = _AutoFreqSelectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 22),
    _AutoFreqSelectionStatus_Type()
)
autoFreqSelectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autoFreqSelectionStatus.setStatus("current")


class _ChannelSpacing_Type(Integer32):
    """Custom type channelSpacing based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25)
        )
    )
    namedValues = NamedValues(
        *(("cs7MHz", 1),
          ("cs10MHz", 2),
          ("cs14MHz", 3),
          ("cs20MHz", 4),
          ("cs28MHz", 5),
          ("cs30MHz", 6),
          ("cs40MHz", 7),
          ("cs50MHz", 8),
          ("cs56MHz", 9),
          ("cs250MHz", 10),
          ("cs60MHz", 11),
          ("cs500MHz", 12),
          ("cs750MHz", 13),
          ("cs100MHz", 14),
          ("cs150MHz", 15),
          ("cs200MHz", 16),
          ("cs125MHz", 17),
          ("cs80MHz", 18),
          ("cs112MHz", 19),
          ("cs1000MHz", 20),
          ("cs1250MHz", 21),
          ("cs1500MHz", 22),
          ("cs62p5MHz", 23),
          ("cs2000MHz", 24),
          ("unknown", 25))
    )


_ChannelSpacing_Type.__name__ = "Integer32"
_ChannelSpacing_Object = MibTableColumn
channelSpacing = _ChannelSpacing_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 23),
    _ChannelSpacing_Type()
)
channelSpacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelSpacing.setStatus("current")


class _Polarization_Type(Integer32):
    """Custom type polarization based on Integer32"""
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
        *(("notSpecified", 1),
          ("horizontal", 2),
          ("vertical", 3),
          ("unknown", 4))
    )


_Polarization_Type.__name__ = "Integer32"
_Polarization_Object = MibTableColumn
polarization = _Polarization_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 24),
    _Polarization_Type()
)
polarization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    polarization.setStatus("current")


class _TxOperStatus_Type(Integer32):
    """Custom type txOperStatus based on Integer32"""
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
        *(("unknown", 1),
          ("off", 2),
          ("on", 3),
          ("standby", 4))
    )


_TxOperStatus_Type.__name__ = "Integer32"
_TxOperStatus_Object = MibTableColumn
txOperStatus = _TxOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 25),
    _TxOperStatus_Type()
)
txOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txOperStatus.setStatus("current")


class _TxAdminStatus_Type(Integer32):
    """Custom type txAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("unknown", 3))
    )


_TxAdminStatus_Type.__name__ = "Integer32"
_TxAdminStatus_Object = MibTableColumn
txAdminStatus = _TxAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 26),
    _TxAdminStatus_Type()
)
txAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txAdminStatus.setStatus("current")


class _SelectedOutputPowerType_Type(Integer32):
    """Custom type selectedOutputPowerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("standard", 1),
          ("high", 2),
          ("unknown", 3))
    )


_SelectedOutputPowerType_Type.__name__ = "Integer32"
_SelectedOutputPowerType_Object = MibTableColumn
selectedOutputPowerType = _SelectedOutputPowerType_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 27),
    _SelectedOutputPowerType_Type()
)
selectedOutputPowerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    selectedOutputPowerType.setStatus("current")


class _AvailableOutputPowerType_Type(Integer32):
    """Custom type availableOutputPowerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("standard", 1),
          ("high", 2),
          ("unknown", 3))
    )


_AvailableOutputPowerType_Type.__name__ = "Integer32"
_AvailableOutputPowerType_Object = MibTableColumn
availableOutputPowerType = _AvailableOutputPowerType_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 28),
    _AvailableOutputPowerType_Type()
)
availableOutputPowerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    availableOutputPowerType.setStatus("current")
_SelectedMinOutputPower_Type = Integer32
_SelectedMinOutputPower_Object = MibTableColumn
selectedMinOutputPower = _SelectedMinOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 29),
    _SelectedMinOutputPower_Type()
)
selectedMinOutputPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    selectedMinOutputPower.setStatus("current")
_SelectedMaxOutputPower_Type = Integer32
_SelectedMaxOutputPower_Object = MibTableColumn
selectedMaxOutputPower = _SelectedMaxOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 30),
    _SelectedMaxOutputPower_Type()
)
selectedMaxOutputPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    selectedMaxOutputPower.setStatus("current")
_AvailableMinOutputPower_Type = Integer32
_AvailableMinOutputPower_Object = MibTableColumn
availableMinOutputPower = _AvailableMinOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 31),
    _AvailableMinOutputPower_Type()
)
availableMinOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    availableMinOutputPower.setStatus("current")
_AvailableMaxOutputPower_Type = Integer32
_AvailableMaxOutputPower_Object = MibTableColumn
availableMaxOutputPower = _AvailableMaxOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 32),
    _AvailableMaxOutputPower_Type()
)
availableMaxOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    availableMaxOutputPower.setStatus("current")


class _ReferenceSec_Type(Integer32):
    """Custom type referenceSec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              7,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("noAvailable", 1),
          ("sec2", 2),
          ("sec4L", 4),
          ("sec4H", 5),
          ("sec5B", 7),
          ("sec6B", 9),
          ("sec5LB", 10),
          ("sec5HB", 11),
          ("sec6LB", 12),
          ("sec6HB", 13),
          ("sec7B", 14),
          ("unknown", 15))
    )


_ReferenceSec_Type.__name__ = "Integer32"
_ReferenceSec_Object = MibTableColumn
referenceSec = _ReferenceSec_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 33),
    _ReferenceSec_Type()
)
referenceSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    referenceSec.setStatus("current")
_TargetInputPowerFarEnd_Type = Integer32
_TargetInputPowerFarEnd_Object = MibTableColumn
targetInputPowerFarEnd = _TargetInputPowerFarEnd_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 34),
    _TargetInputPowerFarEnd_Type()
)
targetInputPowerFarEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    targetInputPowerFarEnd.setStatus("current")


class _BerAlarmThreshold_Type(Integer32):
    """Custom type berAlarmThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tenExpMinus6", 1),
          ("tenExpMinus3", 2))
    )


_BerAlarmThreshold_Type.__name__ = "Integer32"
_BerAlarmThreshold_Object = MibTableColumn
berAlarmThreshold = _BerAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 35),
    _BerAlarmThreshold_Type()
)
berAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    berAlarmThreshold.setStatus("current")
_InputPowerAlarmThreshold_Type = Integer32
_InputPowerAlarmThreshold_Object = MibTableColumn
inputPowerAlarmThreshold = _InputPowerAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 36),
    _InputPowerAlarmThreshold_Type()
)
inputPowerAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inputPowerAlarmThreshold.setStatus("current")
_PlannedAlignmentInputPower_Type = Integer32
_PlannedAlignmentInputPower_Object = MibTableColumn
plannedAlignmentInputPower = _PlannedAlignmentInputPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 37),
    _PlannedAlignmentInputPower_Type()
)
plannedAlignmentInputPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plannedAlignmentInputPower.setStatus("current")
_AtpcFallback_Type = EnableStatusTC
_AtpcFallback_Object = MibTableColumn
atpcFallback = _AtpcFallback_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 38),
    _AtpcFallback_Type()
)
atpcFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atpcFallback.setStatus("current")
_AtpcFallbackTimer_Type = Integer32
_AtpcFallbackTimer_Object = MibTableColumn
atpcFallbackTimer = _AtpcFallbackTimer_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 39),
    _AtpcFallbackTimer_Type()
)
atpcFallbackTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atpcFallbackTimer.setStatus("current")
_AtpcFallbackOutputPower_Type = Integer32
_AtpcFallbackOutputPower_Object = MibTableColumn
atpcFallbackOutputPower = _AtpcFallbackOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 40),
    _AtpcFallbackOutputPower_Type()
)
atpcFallbackOutputPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atpcFallbackOutputPower.setStatus("current")
_XpicStatus_Type = XpicMimoTC
_XpicStatus_Object = MibTableColumn
xpicStatus = _XpicStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 41),
    _XpicStatus_Type()
)
xpicStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xpicStatus.setStatus("current")
_MimoStatus_Type = XpicMimoTC
_MimoStatus_Object = MibTableColumn
mimoStatus = _MimoStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 42),
    _MimoStatus_Type()
)
mimoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimoStatus.setStatus("current")
_ActualSnir_Type = OctetString
_ActualSnir_Object = MibTableColumn
actualSnir = _ActualSnir_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 43),
    _ActualSnir_Type()
)
actualSnir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actualSnir.setStatus("current")
_ActualXpi_Type = OctetString
_ActualXpi_Object = MibTableColumn
actualXpi = _ActualXpi_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 44),
    _ActualXpi_Type()
)
actualXpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actualXpi.setStatus("current")
_ActualSi_Type = OctetString
_ActualSi_Object = MibTableColumn
actualSi = _ActualSi_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 45),
    _ActualSi_Type()
)
actualSi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actualSi.setStatus("current")
_ActualTxCapacity_Type = Integer32
_ActualTxCapacity_Object = MibTableColumn
actualTxCapacity = _ActualTxCapacity_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 46),
    _ActualTxCapacity_Type()
)
actualTxCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actualTxCapacity.setStatus("current")
_LicensedCapacity_Type = Integer32
_LicensedCapacity_Object = MibTableColumn
licensedCapacity = _LicensedCapacity_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 47),
    _LicensedCapacity_Type()
)
licensedCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licensedCapacity.setStatus("current")
_AvailableMinCapacity_Type = Integer32
_AvailableMinCapacity_Object = MibTableColumn
availableMinCapacity = _AvailableMinCapacity_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 48),
    _AvailableMinCapacity_Type()
)
availableMinCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    availableMinCapacity.setStatus("current")
_AvailableMaxCapacity_Type = Integer32
_AvailableMaxCapacity_Object = MibTableColumn
availableMaxCapacity = _AvailableMaxCapacity_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 49),
    _AvailableMaxCapacity_Type()
)
availableMaxCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    availableMaxCapacity.setStatus("current")
_SelectedMinCapacity_Type = Integer32
_SelectedMinCapacity_Object = MibTableColumn
selectedMinCapacity = _SelectedMinCapacity_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 50),
    _SelectedMinCapacity_Type()
)
selectedMinCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    selectedMinCapacity.setStatus("current")
_SelectedMaxCapacity_Type = Integer32
_SelectedMaxCapacity_Object = MibTableColumn
selectedMaxCapacity = _SelectedMaxCapacity_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 51),
    _SelectedMaxCapacity_Type()
)
selectedMaxCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    selectedMaxCapacity.setStatus("current")
_WantedLicensedCapacity_Type = Integer32
_WantedLicensedCapacity_Object = MibTableColumn
wantedLicensedCapacity = _WantedLicensedCapacity_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 52),
    _WantedLicensedCapacity_Type()
)
wantedLicensedCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wantedLicensedCapacity.setStatus("current")
_AvailableMinAcm_Type = AcmTC
_AvailableMinAcm_Object = MibTableColumn
availableMinAcm = _AvailableMinAcm_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 53),
    _AvailableMinAcm_Type()
)
availableMinAcm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    availableMinAcm.setStatus("current")
_AvailableMaxAcm_Type = AcmTC
_AvailableMaxAcm_Object = MibTableColumn
availableMaxAcm = _AvailableMaxAcm_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 54),
    _AvailableMaxAcm_Type()
)
availableMaxAcm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    availableMaxAcm.setStatus("current")
_SelectedMinAcm_Type = AcmTC
_SelectedMinAcm_Object = MibTableColumn
selectedMinAcm = _SelectedMinAcm_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 55),
    _SelectedMinAcm_Type()
)
selectedMinAcm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    selectedMinAcm.setStatus("current")
_SelectedMaxAcm_Type = AcmTC
_SelectedMaxAcm_Object = MibTableColumn
selectedMaxAcm = _SelectedMaxAcm_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 56),
    _SelectedMaxAcm_Type()
)
selectedMaxAcm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    selectedMaxAcm.setStatus("current")
_ActualRxAcmTC_Type = AcmTC
_ActualRxAcmTC_Object = MibTableColumn
actualRxAcmTC = _ActualRxAcmTC_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 57),
    _ActualRxAcmTC_Type()
)
actualRxAcmTC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actualRxAcmTC.setStatus("current")
_ActualTxAcmTC_Type = AcmTC
_ActualTxAcmTC_Object = MibTableColumn
actualTxAcmTC = _ActualTxAcmTC_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 58),
    _ActualTxAcmTC_Type()
)
actualTxAcmTC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actualTxAcmTC.setStatus("current")
_AlignmentMode_Type = EnableStatusTC
_AlignmentMode_Object = MibTableColumn
alignmentMode = _AlignmentMode_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 59),
    _AlignmentMode_Type()
)
alignmentMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alignmentMode.setStatus("current")
_RfLoop_Type = EnableStatusTC
_RfLoop_Object = MibTableColumn
rfLoop = _RfLoop_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 1, 1, 60),
    _RfLoop_Type()
)
rfLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfLoop.setStatus("current")
_PtRadioLinkConformance_ObjectIdentity = ObjectIdentity
ptRadioLinkConformance = _PtRadioLinkConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 2)
)
_PtRadioLinkCompliances_ObjectIdentity = ObjectIdentity
ptRadioLinkCompliances = _PtRadioLinkCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 2, 1)
)
_PtRadioLinkGroups_ObjectIdentity = ObjectIdentity
ptRadioLinkGroups = _PtRadioLinkGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 2, 2)
)
_RltTable_Object = MibTable
rltTable = _RltTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 3)
)
if mibBuilder.loadTexts:
    rltTable.setStatus("current")
_RltEntry_Object = MibTableRow
rltEntry = _RltEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 3, 1)
)
if mibBuilder.loadTexts:
    rltEntry.setStatus("current")
_RltDistinguishedName_Type = OctetString
_RltDistinguishedName_Object = MibTableColumn
rltDistinguishedName = _RltDistinguishedName_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 3, 1, 1),
    _RltDistinguishedName_Type()
)
rltDistinguishedName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rltDistinguishedName.setStatus("current")
_NeIpAddress_Type = IpAddress
_NeIpAddress_Object = MibTableColumn
neIpAddress = _NeIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 3, 1, 2),
    _NeIpAddress_Type()
)
neIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neIpAddress.setStatus("current")
_NeIpv6Address_Type = InetAddressIPv6
_NeIpv6Address_Object = MibTableColumn
neIpv6Address = _NeIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 3, 1, 3),
    _NeIpv6Address_Type()
)
neIpv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neIpv6Address.setStatus("current")
_NeName_Type = OctetString
_NeName_Object = MibTableColumn
neName = _NeName_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 3, 1, 4),
    _NeName_Type()
)
neName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neName.setStatus("current")


class _NeType_Type(Integer32):
    """Custom type neType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("mle", 2),
          ("xfMle", 3),
          ("tn", 4),
          ("cn", 5),
          ("pt", 6))
    )


_NeType_Type.__name__ = "Integer32"
_NeType_Object = MibTableColumn
neType = _NeType_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 3, 1, 5),
    _NeType_Type()
)
neType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neType.setStatus("current")
_Id_Type = OctetString
_Id_Object = MibTableColumn
id = _Id_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 3, 1, 6),
    _Id_Type()
)
id.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    id.setStatus("current")


class _RltStatus_Type(Integer32):
    """Custom type rltStatus based on Integer32"""
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
        *(("down", 1),
          ("up", 2),
          ("na", 3),
          ("unknown", 4),
          ("degraded", 5))
    )


_RltStatus_Type.__name__ = "Integer32"
_RltStatus_Object = MibTableColumn
rltStatus = _RltStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 3, 1, 7),
    _RltStatus_Type()
)
rltStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rltStatus.setStatus("current")


class _Mode_Type(Integer32):
    """Custom type mode based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35)
        )
    )
    namedValues = NamedValues(
        *(("mode1plus0", 1),
          ("mode1plus1CSB", 2),
          ("mode1plus1RLP", 3),
          ("mode2plus0RLB", 4),
          ("mode2plus1CSB", 5),
          ("mode2plus1RLP", 6),
          ("mode2plus2CSB", 7),
          ("mode2plus2RLP", 8),
          ("mode3plus0RLB", 9),
          ("mode4plus0RLB", 10),
          ("notAvailable11", 11),
          ("notAvailable12", 12),
          ("notAvailable13", 13),
          ("notAvailable14", 14),
          ("mode3plus1RLP", 15),
          ("mode3plus2RLP", 16),
          ("mode3plus3RLP", 17),
          ("mode4plus1RLP", 18),
          ("mode4plus2RLP", 19),
          ("mode4plus3RLP", 20),
          ("mode4plus4RLP", 21),
          ("notAvailable22", 22),
          ("notAvailable23", 23),
          ("notAvailable24", 24),
          ("notAvailable25", 25),
          ("notAvailable26", 26),
          ("notAvailable27", 27),
          ("mode3plus1CSB", 28),
          ("mode3plus2CSB", 29),
          ("mode3plus3CSB", 30),
          ("mode4plus1CSB", 31),
          ("mode4plus2CSB", 32),
          ("mode4plus3CSB", 33),
          ("mode4plus4CSB", 34),
          ("unknown", 35))
    )


_Mode_Type.__name__ = "Integer32"
_Mode_Object = MibTableColumn
mode = _Mode_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 3, 1, 8),
    _Mode_Type()
)
mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mode.setStatus("current")
_ActualTxTotalCapacity_Type = Integer32
_ActualTxTotalCapacity_Object = MibTableColumn
actualTxTotalCapacity = _ActualTxTotalCapacity_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 3, 1, 9),
    _ActualTxTotalCapacity_Type()
)
actualTxTotalCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actualTxTotalCapacity.setStatus("current")
_LimitedTotalCapacity_Type = Integer32
_LimitedTotalCapacity_Object = MibTableColumn
limitedTotalCapacity = _LimitedTotalCapacity_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 3, 1, 10),
    _LimitedTotalCapacity_Type()
)
limitedTotalCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    limitedTotalCapacity.setStatus("current")


class _ProtectionStatus_Type(Integer32):
    """Custom type protectionStatus based on Integer32"""
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
        *(("unprotected", 1),
          ("protected", 2),
          ("unableToProtect", 3),
          ("unknown", 4))
    )


_ProtectionStatus_Type.__name__ = "Integer32"
_ProtectionStatus_Object = MibTableColumn
protectionStatus = _ProtectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 3, 1, 11),
    _ProtectionStatus_Type()
)
protectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protectionStatus.setStatus("current")
_RevertiveWaitToRestore_Type = Integer32
_RevertiveWaitToRestore_Object = MibTableColumn
revertiveWaitToRestore = _RevertiveWaitToRestore_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 3, 1, 12),
    _RevertiveWaitToRestore_Type()
)
revertiveWaitToRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    revertiveWaitToRestore.setStatus("current")


class _RevertivePreferredTx_Type(Integer32):
    """Custom type revertivePreferredTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ct11", 1),
          ("ct12", 2),
          ("ct21", 3),
          ("ct22", 4),
          ("notApplicable", 5),
          ("unknown", 6))
    )


_RevertivePreferredTx_Type.__name__ = "Integer32"
_RevertivePreferredTx_Object = MibTableColumn
revertivePreferredTx = _RevertivePreferredTx_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 3, 1, 13),
    _RevertivePreferredTx_Type()
)
revertivePreferredTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    revertivePreferredTx.setStatus("current")


class _ProtectionSwitchMode_Type(Integer32):
    """Custom type protectionSwitchMode based on Integer32"""
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
        *(("auto", 1),
          ("manual", 2),
          ("autoAndRevertive", 3),
          ("unknown", 4),
          ("notApplicable", 5))
    )


_ProtectionSwitchMode_Type.__name__ = "Integer32"
_ProtectionSwitchMode_Object = MibTableColumn
protectionSwitchMode = _ProtectionSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 3, 1, 14),
    _ProtectionSwitchMode_Type()
)
protectionSwitchMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protectionSwitchMode.setStatus("current")
_FadeNotificationTimer_Type = Integer32
_FadeNotificationTimer_Object = MibTableColumn
fadeNotificationTimer = _FadeNotificationTimer_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 3, 1, 15),
    _FadeNotificationTimer_Type()
)
fadeNotificationTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadeNotificationTimer.setStatus("current")
_ExpectedFarEndId_Type = OctetString
_ExpectedFarEndId_Object = MibTableColumn
expectedFarEndId = _ExpectedFarEndId_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 3, 1, 16),
    _ExpectedFarEndId_Type()
)
expectedFarEndId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expectedFarEndId.setStatus("current")


class _FarEndIdCheck_Type(Integer32):
    """Custom type farEndIdCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("unknown", 3))
    )


_FarEndIdCheck_Type.__name__ = "Integer32"
_FarEndIdCheck_Object = MibTableColumn
farEndIdCheck = _FarEndIdCheck_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 3, 1, 17),
    _FarEndIdCheck_Type()
)
farEndIdCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    farEndIdCheck.setStatus("current")


class _CpriMode_Type(Integer32):
    """Custom type cpriMode based on Integer32"""
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
        *(("master", 1),
          ("slave", 2),
          ("notApplicable", 3),
          ("unknown", 4))
    )


_CpriMode_Type.__name__ = "Integer32"
_CpriMode_Object = MibTableColumn
cpriMode = _CpriMode_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 3, 1, 18),
    _CpriMode_Type()
)
cpriMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpriMode.setStatus("current")


class _CpriStatus_Type(Integer32):
    """Custom type cpriStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("waitingOnRtcSync", 2),
          ("waitingOnCpri", 3),
          ("waitingOnRxRequest", 4),
          ("waitingOnTxRequest", 5),
          ("inSync", 6),
          ("unknown", 7))
    )


_CpriStatus_Type.__name__ = "Integer32"
_CpriStatus_Object = MibTableColumn
cpriStatus = _CpriStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 3, 1, 19),
    _CpriStatus_Type()
)
cpriStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpriStatus.setStatus("current")


class _ManualSwitch_Type(Integer32):
    """Custom type manualSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ct11", 1),
          ("ct12", 2),
          ("ct21", 3),
          ("ct22", 4),
          ("notApplicable", 5),
          ("unknown", 6))
    )


_ManualSwitch_Type.__name__ = "Integer32"
_ManualSwitch_Object = MibTableColumn
manualSwitch = _ManualSwitch_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 3, 1, 20),
    _ManualSwitch_Type()
)
manualSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    manualSwitch.setStatus("current")


class _MlhcOperStatus_Type(Integer32):
    """Custom type mlhcOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("unknown", 3))
    )


_MlhcOperStatus_Type.__name__ = "Integer32"
_MlhcOperStatus_Object = MibTableColumn
mlhcOperStatus = _MlhcOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 3, 1, 21),
    _MlhcOperStatus_Type()
)
mlhcOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlhcOperStatus.setStatus("current")


class _MlhcAdminStatus_Type(Integer32):
    """Custom type mlhcAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("unknown", 3))
    )


_MlhcAdminStatus_Type.__name__ = "Integer32"
_MlhcAdminStatus_Object = MibTableColumn
mlhcAdminStatus = _MlhcAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 3, 1, 22),
    _MlhcAdminStatus_Type()
)
mlhcAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlhcAdminStatus.setStatus("current")


class _MlhcMplsConfig_Type(Integer32):
    """Custom type mlhcMplsConfig based on Integer32"""
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
        *(("controlWord", 1),
          ("l2", 2),
          ("l3", 3),
          ("mplsOnly", 4),
          ("unknown", 5))
    )


_MlhcMplsConfig_Type.__name__ = "Integer32"
_MlhcMplsConfig_Object = MibTableColumn
mlhcMplsConfig = _MlhcMplsConfig_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 3, 1, 23),
    _MlhcMplsConfig_Type()
)
mlhcMplsConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlhcMplsConfig.setStatus("current")


class _PlcOperStatus_Type(Integer32):
    """Custom type plcOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("unknown", 3))
    )


_PlcOperStatus_Type.__name__ = "Integer32"
_PlcOperStatus_Object = MibTableColumn
plcOperStatus = _PlcOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 3, 1, 24),
    _PlcOperStatus_Type()
)
plcOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcOperStatus.setStatus("current")


class _PlcAdminStatus_Type(Integer32):
    """Custom type plcAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("unknown", 3))
    )


_PlcAdminStatus_Type.__name__ = "Integer32"
_PlcAdminStatus_Object = MibTableColumn
plcAdminStatus = _PlcAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 3, 1, 25),
    _PlcAdminStatus_Type()
)
plcAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcAdminStatus.setStatus("current")
_CtPerformance_ObjectIdentity = ObjectIdentity
ctPerformance = _CtPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 4)
)
_CtG826ContinuousTable_Object = MibTable
ctG826ContinuousTable = _CtG826ContinuousTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 4, 1)
)
if mibBuilder.loadTexts:
    ctG826ContinuousTable.setStatus("current")
_CtG826ContinuousEntry_Object = MibTableRow
ctG826ContinuousEntry = _CtG826ContinuousEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 4, 1, 1)
)
if mibBuilder.loadTexts:
    ctG826ContinuousEntry.setStatus("current")
_CtG826TimeElapsed_Type = Counter32
_CtG826TimeElapsed_Object = MibTableColumn
ctG826TimeElapsed = _CtG826TimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 4, 1, 1, 1),
    _CtG826TimeElapsed_Type()
)
ctG826TimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctG826TimeElapsed.setStatus("current")
_CtBBE_Type = Counter32
_CtBBE_Object = MibTableColumn
ctBBE = _CtBBE_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 4, 1, 1, 2),
    _CtBBE_Type()
)
ctBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctBBE.setStatus("current")
_CtBBER_Type = OctetString
_CtBBER_Object = MibTableColumn
ctBBER = _CtBBER_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 4, 1, 1, 3),
    _CtBBER_Type()
)
ctBBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctBBER.setStatus("current")
_CtES_Type = Counter32
_CtES_Object = MibTableColumn
ctES = _CtES_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 4, 1, 1, 4),
    _CtES_Type()
)
ctES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctES.setStatus("current")
_CtESR_Type = OctetString
_CtESR_Object = MibTableColumn
ctESR = _CtESR_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 4, 1, 1, 5),
    _CtESR_Type()
)
ctESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctESR.setStatus("current")
_CtSES_Type = Counter32
_CtSES_Object = MibTableColumn
ctSES = _CtSES_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 4, 1, 1, 6),
    _CtSES_Type()
)
ctSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctSES.setStatus("current")
_CtSESR_Type = OctetString
_CtSESR_Object = MibTableColumn
ctSESR = _CtSESR_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 4, 1, 1, 7),
    _CtSESR_Type()
)
ctSESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctSESR.setStatus("current")
_CtBB_Type = OctetString
_CtBB_Object = MibTableColumn
ctBB = _CtBB_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 4, 1, 1, 8),
    _CtBB_Type()
)
ctBB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctBB.setStatus("current")
_CtUAS_Type = Counter32
_CtUAS_Object = MibTableColumn
ctUAS = _CtUAS_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 4, 1, 1, 9),
    _CtUAS_Type()
)
ctUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctUAS.setStatus("current")


class _CtG826Reset_Type(Integer32):
    """Custom type ctG826Reset based on Integer32"""
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
          ("noReset", 2),
          ("reset", 3))
    )


_CtG826Reset_Type.__name__ = "Integer32"
_CtG826Reset_Object = MibTableColumn
ctG826Reset = _CtG826Reset_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 4, 1, 1, 10),
    _CtG826Reset_Type()
)
ctG826Reset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctG826Reset.setStatus("current")
_CtG826Current15mTable_Object = MibTable
ctG826Current15mTable = _CtG826Current15mTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 4, 2)
)
if mibBuilder.loadTexts:
    ctG826Current15mTable.setStatus("current")
_CtG826Current15mEntry_Object = MibTableRow
ctG826Current15mEntry = _CtG826Current15mEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 4, 2, 1)
)
if mibBuilder.loadTexts:
    ctG826Current15mEntry.setStatus("current")
_CtG826Current15mTimeElapsed_Type = Counter32
_CtG826Current15mTimeElapsed_Object = MibTableColumn
ctG826Current15mTimeElapsed = _CtG826Current15mTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 4, 2, 1, 1),
    _CtG826Current15mTimeElapsed_Type()
)
ctG826Current15mTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctG826Current15mTimeElapsed.setStatus("current")
_CtCurrent15mBBE_Type = Counter32
_CtCurrent15mBBE_Object = MibTableColumn
ctCurrent15mBBE = _CtCurrent15mBBE_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 4, 2, 1, 2),
    _CtCurrent15mBBE_Type()
)
ctCurrent15mBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctCurrent15mBBE.setStatus("current")
_CtCurrent15mBBER_Type = OctetString
_CtCurrent15mBBER_Object = MibTableColumn
ctCurrent15mBBER = _CtCurrent15mBBER_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 4, 2, 1, 3),
    _CtCurrent15mBBER_Type()
)
ctCurrent15mBBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctCurrent15mBBER.setStatus("current")
_CtCurrent15mES_Type = Counter32
_CtCurrent15mES_Object = MibTableColumn
ctCurrent15mES = _CtCurrent15mES_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 4, 2, 1, 4),
    _CtCurrent15mES_Type()
)
ctCurrent15mES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctCurrent15mES.setStatus("current")
_CtCurrent15mESR_Type = OctetString
_CtCurrent15mESR_Object = MibTableColumn
ctCurrent15mESR = _CtCurrent15mESR_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 4, 2, 1, 5),
    _CtCurrent15mESR_Type()
)
ctCurrent15mESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctCurrent15mESR.setStatus("current")
_CtCurrent15mSES_Type = Counter32
_CtCurrent15mSES_Object = MibTableColumn
ctCurrent15mSES = _CtCurrent15mSES_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 4, 2, 1, 6),
    _CtCurrent15mSES_Type()
)
ctCurrent15mSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctCurrent15mSES.setStatus("current")
_CtCurrent15mSESR_Type = OctetString
_CtCurrent15mSESR_Object = MibTableColumn
ctCurrent15mSESR = _CtCurrent15mSESR_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 4, 2, 1, 7),
    _CtCurrent15mSESR_Type()
)
ctCurrent15mSESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctCurrent15mSESR.setStatus("current")
_CtCurrent15mBB_Type = Counter32
_CtCurrent15mBB_Object = MibTableColumn
ctCurrent15mBB = _CtCurrent15mBB_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 4, 2, 1, 8),
    _CtCurrent15mBB_Type()
)
ctCurrent15mBB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctCurrent15mBB.setStatus("current")
_CtCurrent15mUAS_Type = Counter32
_CtCurrent15mUAS_Object = MibTableColumn
ctCurrent15mUAS = _CtCurrent15mUAS_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 4, 2, 1, 9),
    _CtCurrent15mUAS_Type()
)
ctCurrent15mUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctCurrent15mUAS.setStatus("current")
_CtG826Current24hTable_Object = MibTable
ctG826Current24hTable = _CtG826Current24hTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 4, 3)
)
if mibBuilder.loadTexts:
    ctG826Current24hTable.setStatus("current")
_CtG826Current24hEntry_Object = MibTableRow
ctG826Current24hEntry = _CtG826Current24hEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 4, 3, 1)
)
if mibBuilder.loadTexts:
    ctG826Current24hEntry.setStatus("current")
_CtG826Current24hTimeElapsed_Type = Counter32
_CtG826Current24hTimeElapsed_Object = MibTableColumn
ctG826Current24hTimeElapsed = _CtG826Current24hTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 4, 3, 1, 1),
    _CtG826Current24hTimeElapsed_Type()
)
ctG826Current24hTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctG826Current24hTimeElapsed.setStatus("current")
_CtCurrent24hBBE_Type = Counter32
_CtCurrent24hBBE_Object = MibTableColumn
ctCurrent24hBBE = _CtCurrent24hBBE_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 4, 3, 1, 2),
    _CtCurrent24hBBE_Type()
)
ctCurrent24hBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctCurrent24hBBE.setStatus("current")
_CtCurrent24hBBER_Type = OctetString
_CtCurrent24hBBER_Object = MibTableColumn
ctCurrent24hBBER = _CtCurrent24hBBER_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 4, 3, 1, 3),
    _CtCurrent24hBBER_Type()
)
ctCurrent24hBBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctCurrent24hBBER.setStatus("current")
_CtCurrent24hES_Type = Counter32
_CtCurrent24hES_Object = MibTableColumn
ctCurrent24hES = _CtCurrent24hES_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 4, 3, 1, 4),
    _CtCurrent24hES_Type()
)
ctCurrent24hES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctCurrent24hES.setStatus("current")
_CtCurrent24hESR_Type = OctetString
_CtCurrent24hESR_Object = MibTableColumn
ctCurrent24hESR = _CtCurrent24hESR_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 4, 3, 1, 5),
    _CtCurrent24hESR_Type()
)
ctCurrent24hESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctCurrent24hESR.setStatus("current")
_CtCurrent24hSES_Type = Counter32
_CtCurrent24hSES_Object = MibTableColumn
ctCurrent24hSES = _CtCurrent24hSES_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 4, 3, 1, 6),
    _CtCurrent24hSES_Type()
)
ctCurrent24hSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctCurrent24hSES.setStatus("current")
_CtCurrent24hSESR_Type = OctetString
_CtCurrent24hSESR_Object = MibTableColumn
ctCurrent24hSESR = _CtCurrent24hSESR_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 4, 3, 1, 7),
    _CtCurrent24hSESR_Type()
)
ctCurrent24hSESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctCurrent24hSESR.setStatus("current")
_CtCurrent24hBB_Type = Counter32
_CtCurrent24hBB_Object = MibTableColumn
ctCurrent24hBB = _CtCurrent24hBB_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 4, 3, 1, 8),
    _CtCurrent24hBB_Type()
)
ctCurrent24hBB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctCurrent24hBB.setStatus("current")
_CtCurrent24hUAS_Type = Counter32
_CtCurrent24hUAS_Object = MibTableColumn
ctCurrent24hUAS = _CtCurrent24hUAS_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 4, 3, 1, 9),
    _CtCurrent24hUAS_Type()
)
ctCurrent24hUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctCurrent24hUAS.setStatus("current")
ifEntry.registerAugmentions(
    ("PT-RADIOLINK-MIB",
     "ctEntry")
)
ctEntry.setIndexNames(*ifEntry.getIndexNames())
ifEntry.registerAugmentions(
    ("PT-RADIOLINK-MIB",
     "rltEntry")
)
rltEntry.setIndexNames(*ifEntry.getIndexNames())
ifEntry.registerAugmentions(
    ("PT-RADIOLINK-MIB",
     "ctG826ContinuousEntry")
)
ctG826ContinuousEntry.setIndexNames(*ifEntry.getIndexNames())
ifEntry.registerAugmentions(
    ("PT-RADIOLINK-MIB",
     "ctG826Current15mEntry")
)
ctG826Current15mEntry.setIndexNames(*ifEntry.getIndexNames())
ifEntry.registerAugmentions(
    ("PT-RADIOLINK-MIB",
     "ctG826Current24hEntry")
)
ctG826Current24hEntry.setIndexNames(*ifEntry.getIndexNames())

# Managed Objects groups

ptRadioLinkCompleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 2, 2, 1)
)
ptRadioLinkCompleteGroup.setObjects(
      *(("PT-RADIOLINK-MIB", "actualInputPower"),
        ("PT-RADIOLINK-MIB", "actualOutputPower"),
        ("PT-RADIOLINK-MIB", "actualRxAcm"),
        ("PT-RADIOLINK-MIB", "actualRxAcmTC"),
        ("PT-RADIOLINK-MIB", "actualSi"),
        ("PT-RADIOLINK-MIB", "actualSnir"),
        ("PT-RADIOLINK-MIB", "actualTxAcm"),
        ("PT-RADIOLINK-MIB", "actualTxAcmTC"),
        ("PT-RADIOLINK-MIB", "actualTxCapacity"),
        ("PT-RADIOLINK-MIB", "actualTxTotalCapacity"),
        ("PT-RADIOLINK-MIB", "actualXpi"),
        ("PT-RADIOLINK-MIB", "alignmentMode"),
        ("PT-RADIOLINK-MIB", "atpcFallback"),
        ("PT-RADIOLINK-MIB", "atpcFallbackTimer"),
        ("PT-RADIOLINK-MIB", "atpcFallbackOutputPower"),
        ("PT-RADIOLINK-MIB", "autoFreqSelectedChannel"),
        ("PT-RADIOLINK-MIB", "autoFreqSelection"),
        ("PT-RADIOLINK-MIB", "autoFreqSelectionStatus"),
        ("PT-RADIOLINK-MIB", "availableMaxAcm"),
        ("PT-RADIOLINK-MIB", "availableMaxCapacity"),
        ("PT-RADIOLINK-MIB", "availableMaxOutputPower"),
        ("PT-RADIOLINK-MIB", "availableMinAcm"),
        ("PT-RADIOLINK-MIB", "availableMinCapacity"),
        ("PT-RADIOLINK-MIB", "availableMinOutputPower"),
        ("PT-RADIOLINK-MIB", "availableOutputPowerType"),
        ("PT-RADIOLINK-MIB", "berAlarmThreshold"),
        ("PT-RADIOLINK-MIB", "carrierId"),
        ("PT-RADIOLINK-MIB", "channelSpacing"),
        ("PT-RADIOLINK-MIB", "cpriMode"),
        ("PT-RADIOLINK-MIB", "cpriStatus"),
        ("PT-RADIOLINK-MIB", "ctDistinguishedName"),
        ("PT-RADIOLINK-MIB", "ctCurrent15mBB"),
        ("PT-RADIOLINK-MIB", "ctCurrent15mBBE"),
        ("PT-RADIOLINK-MIB", "ctCurrent15mBBER"),
        ("PT-RADIOLINK-MIB", "ctCurrent15mES"),
        ("PT-RADIOLINK-MIB", "ctCurrent15mESR"),
        ("PT-RADIOLINK-MIB", "ctCurrent15mSES"),
        ("PT-RADIOLINK-MIB", "ctCurrent15mSESR"),
        ("PT-RADIOLINK-MIB", "ctCurrent15mUAS"),
        ("PT-RADIOLINK-MIB", "ctG826Current15mTimeElapsed"),
        ("PT-RADIOLINK-MIB", "ctCurrent24hBB"),
        ("PT-RADIOLINK-MIB", "ctCurrent24hBBE"),
        ("PT-RADIOLINK-MIB", "ctCurrent24hBBER"),
        ("PT-RADIOLINK-MIB", "ctCurrent24hES"),
        ("PT-RADIOLINK-MIB", "ctCurrent24hESR"),
        ("PT-RADIOLINK-MIB", "ctCurrent24hSES"),
        ("PT-RADIOLINK-MIB", "ctCurrent24hSESR"),
        ("PT-RADIOLINK-MIB", "ctCurrent24hUAS"),
        ("PT-RADIOLINK-MIB", "ctG826Current24hTimeElapsed"),
        ("PT-RADIOLINK-MIB", "ctBB"),
        ("PT-RADIOLINK-MIB", "ctBBE"),
        ("PT-RADIOLINK-MIB", "ctBBER"),
        ("PT-RADIOLINK-MIB", "ctES"),
        ("PT-RADIOLINK-MIB", "ctESR"),
        ("PT-RADIOLINK-MIB", "ctG826Reset"),
        ("PT-RADIOLINK-MIB", "ctSES"),
        ("PT-RADIOLINK-MIB", "ctSESR"),
        ("PT-RADIOLINK-MIB", "ctG826TimeElapsed"),
        ("PT-RADIOLINK-MIB", "ctUAS"),
        ("PT-RADIOLINK-MIB", "ctStatus"),
        ("PT-RADIOLINK-MIB", "description"),
        ("PT-RADIOLINK-MIB", "duplexConfig"),
        ("PT-RADIOLINK-MIB", "duplexDistance"),
        ("PT-RADIOLINK-MIB", "duplexType"),
        ("PT-RADIOLINK-MIB", "expectedFarEndId"),
        ("PT-RADIOLINK-MIB", "fadeNotificationTimer"),
        ("PT-RADIOLINK-MIB", "farEndIdCheck"),
        ("PT-RADIOLINK-MIB", "frameId"),
        ("PT-RADIOLINK-MIB", "frequencyStepSize"),
        ("PT-RADIOLINK-MIB", "id"),
        ("PT-RADIOLINK-MIB", "inputPowerAlarmThreshold"),
        ("PT-RADIOLINK-MIB", "licensedCapacity"),
        ("PT-RADIOLINK-MIB", "limitedTotalCapacity"),
        ("PT-RADIOLINK-MIB", "manualSwitch"),
        ("PT-RADIOLINK-MIB", "maxRxFrequency"),
        ("PT-RADIOLINK-MIB", "maxTxFrequency"),
        ("PT-RADIOLINK-MIB", "mimoStatus"),
        ("PT-RADIOLINK-MIB", "minRxFrequency"),
        ("PT-RADIOLINK-MIB", "minTxFrequency"),
        ("PT-RADIOLINK-MIB", "mlhcAdminStatus"),
        ("PT-RADIOLINK-MIB", "mlhcMplsConfig"),
        ("PT-RADIOLINK-MIB", "mlhcOperStatus"),
        ("PT-RADIOLINK-MIB", "plcAdminStatus"),
        ("PT-RADIOLINK-MIB", "plcOperStatus"),
        ("PT-RADIOLINK-MIB", "mode"),
        ("PT-RADIOLINK-MIB", "neIpAddress"),
        ("PT-RADIOLINK-MIB", "neIpv6Address"),
        ("PT-RADIOLINK-MIB", "neName"),
        ("PT-RADIOLINK-MIB", "neType"),
        ("PT-RADIOLINK-MIB", "plannedAlignmentInputPower"),
        ("PT-RADIOLINK-MIB", "polarization"),
        ("PT-RADIOLINK-MIB", "protectionStatus"),
        ("PT-RADIOLINK-MIB", "protectionSwitchMode"),
        ("PT-RADIOLINK-MIB", "referenceSec"),
        ("PT-RADIOLINK-MIB", "revertivePreferredTx"),
        ("PT-RADIOLINK-MIB", "revertiveWaitToRestore"),
        ("PT-RADIOLINK-MIB", "rfLoop"),
        ("PT-RADIOLINK-MIB", "rltDistinguishedName"),
        ("PT-RADIOLINK-MIB", "rltStatus"),
        ("PT-RADIOLINK-MIB", "rxFrequency"),
        ("PT-RADIOLINK-MIB", "selectedMaxAcm"),
        ("PT-RADIOLINK-MIB", "selectedMaxCapacity"),
        ("PT-RADIOLINK-MIB", "selectedMaxOutputPower"),
        ("PT-RADIOLINK-MIB", "selectedMinAcm"),
        ("PT-RADIOLINK-MIB", "selectedMinCapacity"),
        ("PT-RADIOLINK-MIB", "selectedMinOutputPower"),
        ("PT-RADIOLINK-MIB", "selectedOutputPowerType"),
        ("PT-RADIOLINK-MIB", "targetInputPowerFarEnd"),
        ("PT-RADIOLINK-MIB", "txAdminStatus"),
        ("PT-RADIOLINK-MIB", "txFrequency"),
        ("PT-RADIOLINK-MIB", "txOperStatus"),
        ("PT-RADIOLINK-MIB", "wantedLicensedCapacity"),
        ("PT-RADIOLINK-MIB", "xpicStatus"))
)
if mibBuilder.loadTexts:
    ptRadioLinkCompleteGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ptRadioLinkFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 7, 2, 1, 1)
)
ptRadioLinkFullCompliance.setObjects(
    ("PT-RADIOLINK-MIB", "ptRadioLinkCompleteGroup")
)
if mibBuilder.loadTexts:
    ptRadioLinkFullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PT-RADIOLINK-MIB",
    **{"AcmTC": AcmTC,
       "EnableStatusTC": EnableStatusTC,
       "XpicMimoTC": XpicMimoTC,
       "ptRadioLink": ptRadioLink,
       "ctTable": ctTable,
       "ctEntry": ctEntry,
       "actualInputPower": actualInputPower,
       "actualOutputPower": actualOutputPower,
       "actualRxAcm": actualRxAcm,
       "actualTxAcm": actualTxAcm,
       "ctDistinguishedName": ctDistinguishedName,
       "description": description,
       "carrierId": carrierId,
       "ctStatus": ctStatus,
       "frameId": frameId,
       "txFrequency": txFrequency,
       "minTxFrequency": minTxFrequency,
       "maxTxFrequency": maxTxFrequency,
       "rxFrequency": rxFrequency,
       "minRxFrequency": minRxFrequency,
       "maxRxFrequency": maxRxFrequency,
       "frequencyStepSize": frequencyStepSize,
       "duplexDistance": duplexDistance,
       "duplexType": duplexType,
       "duplexConfig": duplexConfig,
       "autoFreqSelection": autoFreqSelection,
       "autoFreqSelectedChannel": autoFreqSelectedChannel,
       "autoFreqSelectionStatus": autoFreqSelectionStatus,
       "channelSpacing": channelSpacing,
       "polarization": polarization,
       "txOperStatus": txOperStatus,
       "txAdminStatus": txAdminStatus,
       "selectedOutputPowerType": selectedOutputPowerType,
       "availableOutputPowerType": availableOutputPowerType,
       "selectedMinOutputPower": selectedMinOutputPower,
       "selectedMaxOutputPower": selectedMaxOutputPower,
       "availableMinOutputPower": availableMinOutputPower,
       "availableMaxOutputPower": availableMaxOutputPower,
       "referenceSec": referenceSec,
       "targetInputPowerFarEnd": targetInputPowerFarEnd,
       "berAlarmThreshold": berAlarmThreshold,
       "inputPowerAlarmThreshold": inputPowerAlarmThreshold,
       "plannedAlignmentInputPower": plannedAlignmentInputPower,
       "atpcFallback": atpcFallback,
       "atpcFallbackTimer": atpcFallbackTimer,
       "atpcFallbackOutputPower": atpcFallbackOutputPower,
       "xpicStatus": xpicStatus,
       "mimoStatus": mimoStatus,
       "actualSnir": actualSnir,
       "actualXpi": actualXpi,
       "actualSi": actualSi,
       "actualTxCapacity": actualTxCapacity,
       "licensedCapacity": licensedCapacity,
       "availableMinCapacity": availableMinCapacity,
       "availableMaxCapacity": availableMaxCapacity,
       "selectedMinCapacity": selectedMinCapacity,
       "selectedMaxCapacity": selectedMaxCapacity,
       "wantedLicensedCapacity": wantedLicensedCapacity,
       "availableMinAcm": availableMinAcm,
       "availableMaxAcm": availableMaxAcm,
       "selectedMinAcm": selectedMinAcm,
       "selectedMaxAcm": selectedMaxAcm,
       "actualRxAcmTC": actualRxAcmTC,
       "actualTxAcmTC": actualTxAcmTC,
       "alignmentMode": alignmentMode,
       "rfLoop": rfLoop,
       "ptRadioLinkConformance": ptRadioLinkConformance,
       "ptRadioLinkCompliances": ptRadioLinkCompliances,
       "ptRadioLinkFullCompliance": ptRadioLinkFullCompliance,
       "ptRadioLinkGroups": ptRadioLinkGroups,
       "ptRadioLinkCompleteGroup": ptRadioLinkCompleteGroup,
       "rltTable": rltTable,
       "rltEntry": rltEntry,
       "rltDistinguishedName": rltDistinguishedName,
       "neIpAddress": neIpAddress,
       "neIpv6Address": neIpv6Address,
       "neName": neName,
       "neType": neType,
       "id": id,
       "rltStatus": rltStatus,
       "mode": mode,
       "actualTxTotalCapacity": actualTxTotalCapacity,
       "limitedTotalCapacity": limitedTotalCapacity,
       "protectionStatus": protectionStatus,
       "revertiveWaitToRestore": revertiveWaitToRestore,
       "revertivePreferredTx": revertivePreferredTx,
       "protectionSwitchMode": protectionSwitchMode,
       "fadeNotificationTimer": fadeNotificationTimer,
       "expectedFarEndId": expectedFarEndId,
       "farEndIdCheck": farEndIdCheck,
       "cpriMode": cpriMode,
       "cpriStatus": cpriStatus,
       "manualSwitch": manualSwitch,
       "mlhcOperStatus": mlhcOperStatus,
       "mlhcAdminStatus": mlhcAdminStatus,
       "mlhcMplsConfig": mlhcMplsConfig,
       "plcOperStatus": plcOperStatus,
       "plcAdminStatus": plcAdminStatus,
       "ctPerformance": ctPerformance,
       "ctG826ContinuousTable": ctG826ContinuousTable,
       "ctG826ContinuousEntry": ctG826ContinuousEntry,
       "ctG826TimeElapsed": ctG826TimeElapsed,
       "ctBBE": ctBBE,
       "ctBBER": ctBBER,
       "ctES": ctES,
       "ctESR": ctESR,
       "ctSES": ctSES,
       "ctSESR": ctSESR,
       "ctBB": ctBB,
       "ctUAS": ctUAS,
       "ctG826Reset": ctG826Reset,
       "ctG826Current15mTable": ctG826Current15mTable,
       "ctG826Current15mEntry": ctG826Current15mEntry,
       "ctG826Current15mTimeElapsed": ctG826Current15mTimeElapsed,
       "ctCurrent15mBBE": ctCurrent15mBBE,
       "ctCurrent15mBBER": ctCurrent15mBBER,
       "ctCurrent15mES": ctCurrent15mES,
       "ctCurrent15mESR": ctCurrent15mESR,
       "ctCurrent15mSES": ctCurrent15mSES,
       "ctCurrent15mSESR": ctCurrent15mSESR,
       "ctCurrent15mBB": ctCurrent15mBB,
       "ctCurrent15mUAS": ctCurrent15mUAS,
       "ctG826Current24hTable": ctG826Current24hTable,
       "ctG826Current24hEntry": ctG826Current24hEntry,
       "ctG826Current24hTimeElapsed": ctG826Current24hTimeElapsed,
       "ctCurrent24hBBE": ctCurrent24hBBE,
       "ctCurrent24hBBER": ctCurrent24hBBER,
       "ctCurrent24hES": ctCurrent24hES,
       "ctCurrent24hESR": ctCurrent24hESR,
       "ctCurrent24hSES": ctCurrent24hSES,
       "ctCurrent24hSESR": ctCurrent24hSESR,
       "ctCurrent24hBB": ctCurrent24hBB,
       "ctCurrent24hUAS": ctCurrent24hUAS}
)
