# SNMP MIB module (CIENA-CES-PTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ciena\CIENA-CES-PTP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:24:49 2025
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

(cienaCesConfig,
 cienaCesNotifications) = mibBuilder.importSymbols(
    "CIENA-SMI",
    "cienaCesConfig",
    "cienaCesNotifications")

(CienaGlobalState,) = mibBuilder.importSymbols(
    "CIENA-TC",
    "CienaGlobalState")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cienaCesPtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 38)
)
if mibBuilder.loadTexts:
    cienaCesPtpMIB.setRevisions(
        ("2017-06-07 00:00",
         "2015-12-14 00:00",
         "2015-10-20 00:00",
         "2015-09-09 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PtpHundredths(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-3"


# MIB Managed Objects in the order of their OIDs

_CienaCesPtpMIBObjects_ObjectIdentity = ObjectIdentity
cienaCesPtpMIBObjects = _CienaCesPtpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 38, 1)
)
_CienaCesPtp_ObjectIdentity = ObjectIdentity
cienaCesPtp = _CienaCesPtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 38, 1, 1)
)
_CienaCesPtpTable_Object = MibTable
cienaCesPtpTable = _CienaCesPtpTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 38, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cienaCesPtpTable.setStatus("current")
_CienaCesPtpEntry_Object = MibTableRow
cienaCesPtpEntry = _CienaCesPtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 38, 1, 1, 1, 1)
)
cienaCesPtpEntry.setIndexNames(
    (0, "CIENA-CES-PTP-MIB", "cienaCesPtpIfIndex"),
)
if mibBuilder.loadTexts:
    cienaCesPtpEntry.setStatus("current")
_CienaCesPtpIfIndex_Type = InterfaceIndex
_CienaCesPtpIfIndex_Object = MibTableColumn
cienaCesPtpIfIndex = _CienaCesPtpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 38, 1, 1, 1, 1, 1),
    _CienaCesPtpIfIndex_Type()
)
cienaCesPtpIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesPtpIfIndex.setStatus("current")


class _CienaCesPtpSlotIndex_Type(Unsigned32):
    """Custom type cienaCesPtpSlotIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 38),
    )


_CienaCesPtpSlotIndex_Type.__name__ = "Unsigned32"
_CienaCesPtpSlotIndex_Object = MibTableColumn
cienaCesPtpSlotIndex = _CienaCesPtpSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 38, 1, 1, 1, 1, 2),
    _CienaCesPtpSlotIndex_Type()
)
cienaCesPtpSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPtpSlotIndex.setStatus("current")
_CienaCesPtpPortIndex_Type = Unsigned32
_CienaCesPtpPortIndex_Object = MibTableColumn
cienaCesPtpPortIndex = _CienaCesPtpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 38, 1, 1, 1, 1, 3),
    _CienaCesPtpPortIndex_Type()
)
cienaCesPtpPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPtpPortIndex.setStatus("current")


class _CienaCesPtpPortNumber_Type(Unsigned32):
    """Custom type cienaCesPtpPortNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesPtpPortNumber_Type.__name__ = "Unsigned32"
_CienaCesPtpPortNumber_Object = MibTableColumn
cienaCesPtpPortNumber = _CienaCesPtpPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 38, 1, 1, 1, 1, 4),
    _CienaCesPtpPortNumber_Type()
)
cienaCesPtpPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPtpPortNumber.setStatus("current")


class _CienaCesPtpIfDescr_Type(DisplayString):
    """Custom type cienaCesPtpIfDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CienaCesPtpIfDescr_Type.__name__ = "DisplayString"
_CienaCesPtpIfDescr_Object = MibTableColumn
cienaCesPtpIfDescr = _CienaCesPtpIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 38, 1, 1, 1, 1, 5),
    _CienaCesPtpIfDescr_Type()
)
cienaCesPtpIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPtpIfDescr.setStatus("current")


class _CienaCesPtpModulationScheme_Type(DisplayString):
    """Custom type cienaCesPtpModulationScheme based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CienaCesPtpModulationScheme_Type.__name__ = "DisplayString"
_CienaCesPtpModulationScheme_Object = MibTableColumn
cienaCesPtpModulationScheme = _CienaCesPtpModulationScheme_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 38, 1, 1, 1, 1, 6),
    _CienaCesPtpModulationScheme_Type()
)
cienaCesPtpModulationScheme.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPtpModulationScheme.setStatus("current")


class _CienaCesPtpSupportedOpuTypes_Type(Bits):
    """Custom type cienaCesPtpSupportedOpuTypes based on Bits"""
    namedValues = NamedValues(
        *(("experimental", 0),
          ("asynchronousCbr", 1),
          ("bitSynchronousCbr", 2),
          ("atm", 3),
          ("gfp", 4),
          ("virtualConcatenatedSignal", 5),
          ("hundredGBaseRIntoOpu4", 6),
          ("fc1200IntoOdu2e", 7),
          ("gfpIntoExtendedOpu2Payload", 8),
          ("stm1IntoOdu0", 9),
          ("stm4IntoOdu0", 10),
          ("fc100IntoOdu0", 11),
          ("fc200IntoOdu1", 12),
          ("fc400IntoOduFlex", 13),
          ("fc800IntoOduFlex", 14),
          ("bitStreamWithOctetTiming", 15),
          ("bitStreamWithoutOctetTiming", 16),
          ("ibSdrIntoOduFlex", 17),
          ("ibDdrIntoOduFlex", 18),
          ("ibQdrIntoOduFlex", 19),
          ("oduMultiplexForODTUkh", 20),
          ("oduMultiplexForODTUktsAndODTUkh", 21),
          ("nullTestSignal", 22),
          ("prbsTestSignal", 23),
          ("notAvailable", 24))
    )

_CienaCesPtpSupportedOpuTypes_Type.__name__ = "Bits"
_CienaCesPtpSupportedOpuTypes_Object = MibTableColumn
cienaCesPtpSupportedOpuTypes = _CienaCesPtpSupportedOpuTypes_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 38, 1, 1, 1, 1, 7),
    _CienaCesPtpSupportedOpuTypes_Type()
)
cienaCesPtpSupportedOpuTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPtpSupportedOpuTypes.setStatus("current")
_CienaCesPtpAdminState_Type = CienaGlobalState
_CienaCesPtpAdminState_Object = MibTableColumn
cienaCesPtpAdminState = _CienaCesPtpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 38, 1, 1, 1, 1, 8),
    _CienaCesPtpAdminState_Type()
)
cienaCesPtpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPtpAdminState.setStatus("current")
_CienaCesPtpOperState_Type = CienaGlobalState
_CienaCesPtpOperState_Object = MibTableColumn
cienaCesPtpOperState = _CienaCesPtpOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 38, 1, 1, 1, 1, 9),
    _CienaCesPtpOperState_Type()
)
cienaCesPtpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPtpOperState.setStatus("current")
_CienaCesPtpAdminWavelength_Type = PtpHundredths
_CienaCesPtpAdminWavelength_Object = MibTableColumn
cienaCesPtpAdminWavelength = _CienaCesPtpAdminWavelength_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 38, 1, 1, 1, 1, 10),
    _CienaCesPtpAdminWavelength_Type()
)
cienaCesPtpAdminWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPtpAdminWavelength.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesPtpAdminWavelength.setUnits("nm")
_CienaCesPtpAdminFrequency_Type = PtpHundredths
_CienaCesPtpAdminFrequency_Object = MibTableColumn
cienaCesPtpAdminFrequency = _CienaCesPtpAdminFrequency_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 38, 1, 1, 1, 1, 11),
    _CienaCesPtpAdminFrequency_Type()
)
cienaCesPtpAdminFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPtpAdminFrequency.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesPtpAdminFrequency.setUnits("GHz")


class _CienaCesPtpTxPowerReduction_Type(TruthValue):
    """Custom type cienaCesPtpTxPowerReduction based on TruthValue"""
    defaultValue = 2


_CienaCesPtpTxPowerReduction_Type.__name__ = "TruthValue"
_CienaCesPtpTxPowerReduction_Object = MibTableColumn
cienaCesPtpTxPowerReduction = _CienaCesPtpTxPowerReduction_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 38, 1, 1, 1, 1, 12),
    _CienaCesPtpTxPowerReduction_Type()
)
cienaCesPtpTxPowerReduction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPtpTxPowerReduction.setStatus("current")
_CienaCesPtpTxPower_Type = PtpHundredths
_CienaCesPtpTxPower_Object = MibTableColumn
cienaCesPtpTxPower = _CienaCesPtpTxPower_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 38, 1, 1, 1, 1, 13),
    _CienaCesPtpTxPower_Type()
)
cienaCesPtpTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPtpTxPower.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesPtpTxPower.setUnits("dBm")


class _CienaCesPtpLineSysType_Type(Integer32):
    """Custom type cienaCesPtpLineSysType based on Integer32"""
    defaultValue = 1

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
        *(("color", 1),
          ("colorless", 2),
          ("contentionless", 3),
          ("csColor", 4),
          ("csColorless", 5),
          ("max", 6))
    )


_CienaCesPtpLineSysType_Type.__name__ = "Integer32"
_CienaCesPtpLineSysType_Object = MibTableColumn
cienaCesPtpLineSysType = _CienaCesPtpLineSysType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 38, 1, 1, 1, 1, 14),
    _CienaCesPtpLineSysType_Type()
)
cienaCesPtpLineSysType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPtpLineSysType.setStatus("current")


class _CienaCesPtpOptimizationMode_Type(Integer32):
    """Custom type cienaCesPtpOptimizationMode based on Integer32"""
    defaultValue = 1

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
              15)
        )
    )
    namedValues = NamedValues(
        *(("mode1", 1),
          ("mode2", 2),
          ("mode3", 3),
          ("mode4", 4),
          ("mode5", 5),
          ("mode6", 6),
          ("mode7", 7),
          ("mode8", 8),
          ("mode9", 9),
          ("mode10", 10),
          ("mode11", 11),
          ("mode12", 12),
          ("mode13", 13),
          ("mode14", 14),
          ("max", 15))
    )


_CienaCesPtpOptimizationMode_Type.__name__ = "Integer32"
_CienaCesPtpOptimizationMode_Object = MibTableColumn
cienaCesPtpOptimizationMode = _CienaCesPtpOptimizationMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 38, 1, 1, 1, 1, 15),
    _CienaCesPtpOptimizationMode_Type()
)
cienaCesPtpOptimizationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPtpOptimizationMode.setStatus("current")


class _CienaCesPtpWavelengthSpacing_Type(Integer32):
    """Custom type cienaCesPtpWavelengthSpacing based on Integer32"""
    defaultValue = 3

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
        *(("twelvePointFiveGHz", 1),
          ("twentyFiveGHz", 2),
          ("fiftyGHz", 3),
          ("oneHundredGHz", 4),
          ("max", 5))
    )


_CienaCesPtpWavelengthSpacing_Type.__name__ = "Integer32"
_CienaCesPtpWavelengthSpacing_Object = MibTableColumn
cienaCesPtpWavelengthSpacing = _CienaCesPtpWavelengthSpacing_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 38, 1, 1, 1, 1, 16),
    _CienaCesPtpWavelengthSpacing_Type()
)
cienaCesPtpWavelengthSpacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPtpWavelengthSpacing.setStatus("current")


class _CienaCesPtpSpectralOccupancy_Type(Integer32):
    """Custom type cienaCesPtpSpectralOccupancy based on Integer32"""
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
        *(("narrow", 1),
          ("wide", 2),
          ("max", 3))
    )


_CienaCesPtpSpectralOccupancy_Type.__name__ = "Integer32"
_CienaCesPtpSpectralOccupancy_Object = MibTableColumn
cienaCesPtpSpectralOccupancy = _CienaCesPtpSpectralOccupancy_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 38, 1, 1, 1, 1, 17),
    _CienaCesPtpSpectralOccupancy_Type()
)
cienaCesPtpSpectralOccupancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPtpSpectralOccupancy.setStatus("current")


class _CienaCesPtpTxTuningMode_Type(Integer32):
    """Custom type cienaCesPtpTxTuningMode based on Integer32"""
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
        *(("normal", 1),
          ("accelerated", 2),
          ("max", 3))
    )


_CienaCesPtpTxTuningMode_Type.__name__ = "Integer32"
_CienaCesPtpTxTuningMode_Object = MibTableColumn
cienaCesPtpTxTuningMode = _CienaCesPtpTxTuningMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 38, 1, 1, 1, 1, 18),
    _CienaCesPtpTxTuningMode_Type()
)
cienaCesPtpTxTuningMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPtpTxTuningMode.setStatus("current")


class _CienaCesPtpRotation_Type(TruthValue):
    """Custom type cienaCesPtpRotation based on TruthValue"""
    defaultValue = 2


_CienaCesPtpRotation_Type.__name__ = "TruthValue"
_CienaCesPtpRotation_Object = MibTableColumn
cienaCesPtpRotation = _CienaCesPtpRotation_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 38, 1, 1, 1, 1, 19),
    _CienaCesPtpRotation_Type()
)
cienaCesPtpRotation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPtpRotation.setStatus("current")


class _CienaCesPtpCarrierCentering_Type(Integer32):
    """Custom type cienaCesPtpCarrierCentering based on Integer32"""
    defaultValue = 1

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
        *(("none", 1),
          ("mode1", 2),
          ("mode2", 3),
          ("mode3", 4),
          ("max", 5))
    )


_CienaCesPtpCarrierCentering_Type.__name__ = "Integer32"
_CienaCesPtpCarrierCentering_Object = MibTableColumn
cienaCesPtpCarrierCentering = _CienaCesPtpCarrierCentering_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 38, 1, 1, 1, 1, 20),
    _CienaCesPtpCarrierCentering_Type()
)
cienaCesPtpCarrierCentering.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPtpCarrierCentering.setStatus("current")


class _CienaCesPtpOchEnmMode_Type(Integer32):
    """Custom type cienaCesPtpOchEnmMode based on Integer32"""
    defaultValue = 3

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
        *(("none", 1),
          ("mode1", 2),
          ("mode2", 3),
          ("auto", 4),
          ("max", 5))
    )


_CienaCesPtpOchEnmMode_Type.__name__ = "Integer32"
_CienaCesPtpOchEnmMode_Object = MibTableColumn
cienaCesPtpOchEnmMode = _CienaCesPtpOchEnmMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 38, 1, 1, 1, 1, 21),
    _CienaCesPtpOchEnmMode_Type()
)
cienaCesPtpOchEnmMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPtpOchEnmMode.setStatus("current")


class _CienaCesPtpChContentionDetect_Type(TruthValue):
    """Custom type cienaCesPtpChContentionDetect based on TruthValue"""
    defaultValue = 2


_CienaCesPtpChContentionDetect_Type.__name__ = "TruthValue"
_CienaCesPtpChContentionDetect_Object = MibTableColumn
cienaCesPtpChContentionDetect = _CienaCesPtpChContentionDetect_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 38, 1, 1, 1, 1, 22),
    _CienaCesPtpChContentionDetect_Type()
)
cienaCesPtpChContentionDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPtpChContentionDetect.setStatus("current")
_CienaCesPtpStormControl_Type = TruthValue
_CienaCesPtpStormControl_Object = MibTableColumn
cienaCesPtpStormControl = _CienaCesPtpStormControl_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 38, 1, 1, 1, 1, 23),
    _CienaCesPtpStormControl_Type()
)
cienaCesPtpStormControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPtpStormControl.setStatus("current")


class _CienaCesPtpStormMode_Type(Integer32):
    """Custom type cienaCesPtpStormMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("matched", 1),
          ("diverse", 2),
          ("max", 3))
    )


_CienaCesPtpStormMode_Type.__name__ = "Integer32"
_CienaCesPtpStormMode_Object = MibTableColumn
cienaCesPtpStormMode = _CienaCesPtpStormMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 38, 1, 1, 1, 1, 24),
    _CienaCesPtpStormMode_Type()
)
cienaCesPtpStormMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPtpStormMode.setStatus("current")
_CienaCesPtpStormPath1_Type = Integer32
_CienaCesPtpStormPath1_Object = MibTableColumn
cienaCesPtpStormPath1 = _CienaCesPtpStormPath1_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 38, 1, 1, 1, 1, 25),
    _CienaCesPtpStormPath1_Type()
)
cienaCesPtpStormPath1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPtpStormPath1.setStatus("current")
_CienaCesPtpStormPath2_Type = Integer32
_CienaCesPtpStormPath2_Object = MibTableColumn
cienaCesPtpStormPath2 = _CienaCesPtpStormPath2_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 38, 1, 1, 1, 1, 26),
    _CienaCesPtpStormPath2_Type()
)
cienaCesPtpStormPath2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPtpStormPath2.setStatus("current")
_CienaCesPtpSpliCntrl_Type = TruthValue
_CienaCesPtpSpliCntrl_Object = MibTableColumn
cienaCesPtpSpliCntrl = _CienaCesPtpSpliCntrl_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 38, 1, 1, 1, 1, 27),
    _CienaCesPtpSpliCntrl_Type()
)
cienaCesPtpSpliCntrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPtpSpliCntrl.setStatus("current")
_CienaCesPtpChildOtuIfIndex_Type = InterfaceIndex
_CienaCesPtpChildOtuIfIndex_Object = MibTableColumn
cienaCesPtpChildOtuIfIndex = _CienaCesPtpChildOtuIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 38, 1, 1, 1, 1, 28),
    _CienaCesPtpChildOtuIfIndex_Type()
)
cienaCesPtpChildOtuIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPtpChildOtuIfIndex.setStatus("current")
_CienaCesPtpMIBConformance_ObjectIdentity = ObjectIdentity
cienaCesPtpMIBConformance = _CienaCesPtpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 38, 2)
)
_CienaCesPtpMIBCompliances_ObjectIdentity = ObjectIdentity
cienaCesPtpMIBCompliances = _CienaCesPtpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 38, 2, 1)
)
_CienaCesPtpMIBGroups_ObjectIdentity = ObjectIdentity
cienaCesPtpMIBGroups = _CienaCesPtpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 38, 2, 2)
)
_CienaCesPtpMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
cienaCesPtpMIBNotificationsPrefix = _CienaCesPtpMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 38)
)
_CienaCesPtpMIBNotifications_ObjectIdentity = ObjectIdentity
cienaCesPtpMIBNotifications = _CienaCesPtpMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 38, 0)
)

# Managed Objects groups


# Notification objects

cienaCesPtpAdminStateChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 38, 0, 1)
)
cienaCesPtpAdminStateChangeNotification.setObjects(
      *(("CIENA-CES-PTP-MIB", "cienaGlobalSeverity"),
        ("CIENA-CES-PTP-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-PTP-MIB", "cienaCesPtpIfIndex"),
        ("CIENA-CES-PTP-MIB", "cienaCesPtpAdminState"))
)
if mibBuilder.loadTexts:
    cienaCesPtpAdminStateChangeNotification.setStatus(
        "current"
    )

cienaCesPtpOperStateChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 38, 0, 2)
)
cienaCesPtpOperStateChangeNotification.setObjects(
      *(("CIENA-CES-PTP-MIB", "cienaGlobalSeverity"),
        ("CIENA-CES-PTP-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-PTP-MIB", "cienaCesPtpIfIndex"),
        ("CIENA-CES-PTP-MIB", "cienaCesPtpOperState"))
)
if mibBuilder.loadTexts:
    cienaCesPtpOperStateChangeNotification.setStatus(
        "current"
    )

cienaCesPtpAdminWavelengthChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 38, 0, 3)
)
cienaCesPtpAdminWavelengthChangeNotification.setObjects(
      *(("CIENA-CES-PTP-MIB", "cienaGlobalSeverity"),
        ("CIENA-CES-PTP-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-PTP-MIB", "cienaCesPtpIfIndex"),
        ("CIENA-CES-PTP-MIB", "cienaCesPtpAdminWavelength"))
)
if mibBuilder.loadTexts:
    cienaCesPtpAdminWavelengthChangeNotification.setStatus(
        "current"
    )

cienaCesPtpAdminFrequencyChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 38, 0, 4)
)
cienaCesPtpAdminFrequencyChangeNotification.setObjects(
      *(("CIENA-CES-PTP-MIB", "cienaGlobalSeverity"),
        ("CIENA-CES-PTP-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-PTP-MIB", "cienaCesPtpIfIndex"),
        ("CIENA-CES-PTP-MIB", "cienaCesPtpAdminFrequency"))
)
if mibBuilder.loadTexts:
    cienaCesPtpAdminFrequencyChangeNotification.setStatus(
        "current"
    )

cienaCesPtpTxPowerChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 38, 0, 5)
)
cienaCesPtpTxPowerChangeNotification.setObjects(
      *(("CIENA-CES-PTP-MIB", "cienaGlobalSeverity"),
        ("CIENA-CES-PTP-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-PTP-MIB", "cienaCesPtpIfIndex"),
        ("CIENA-CES-PTP-MIB", "cienaCesPtpTxPower"))
)
if mibBuilder.loadTexts:
    cienaCesPtpTxPowerChangeNotification.setStatus(
        "current"
    )

cienaCesPtpLineSysTypeChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 38, 0, 6)
)
cienaCesPtpLineSysTypeChangeNotification.setObjects(
      *(("CIENA-CES-PTP-MIB", "cienaGlobalSeverity"),
        ("CIENA-CES-PTP-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-PTP-MIB", "cienaCesPtpIfIndex"),
        ("CIENA-CES-PTP-MIB", "cienaCesPtpLineSysType"))
)
if mibBuilder.loadTexts:
    cienaCesPtpLineSysTypeChangeNotification.setStatus(
        "current"
    )

cienaCesPtpOptimizationModeChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 38, 0, 7)
)
cienaCesPtpOptimizationModeChangeNotification.setObjects(
      *(("CIENA-CES-PTP-MIB", "cienaGlobalSeverity"),
        ("CIENA-CES-PTP-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-PTP-MIB", "cienaCesPtpIfIndex"),
        ("CIENA-CES-PTP-MIB", "cienaCesPtpOptimizationMode"))
)
if mibBuilder.loadTexts:
    cienaCesPtpOptimizationModeChangeNotification.setStatus(
        "current"
    )

cienaCesPtpWavelengthSpacingChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 38, 0, 8)
)
cienaCesPtpWavelengthSpacingChangeNotification.setObjects(
      *(("CIENA-CES-PTP-MIB", "cienaGlobalSeverity"),
        ("CIENA-CES-PTP-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-PTP-MIB", "cienaCesPtpIfIndex"),
        ("CIENA-CES-PTP-MIB", "cienaCesPtpWavelengthSpacing"))
)
if mibBuilder.loadTexts:
    cienaCesPtpWavelengthSpacingChangeNotification.setStatus(
        "current"
    )

cienaCesPtpCreatedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 38, 0, 9)
)
cienaCesPtpCreatedNotification.setObjects(
      *(("CIENA-CES-PTP-MIB", "cienaGlobalSeverity"),
        ("CIENA-CES-PTP-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-PTP-MIB", "cienaCesPtpIfIndex"))
)
if mibBuilder.loadTexts:
    cienaCesPtpCreatedNotification.setStatus(
        "current"
    )

cienaCesPtpDeletedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 38, 0, 10)
)
cienaCesPtpDeletedNotification.setObjects(
      *(("CIENA-CES-PTP-MIB", "cienaGlobalSeverity"),
        ("CIENA-CES-PTP-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-PTP-MIB", "cienaCesPtpIfIndex"))
)
if mibBuilder.loadTexts:
    cienaCesPtpDeletedNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-CES-PTP-MIB",
    **{"PtpHundredths": PtpHundredths,
       "cienaCesPtpMIB": cienaCesPtpMIB,
       "cienaCesPtpMIBObjects": cienaCesPtpMIBObjects,
       "cienaCesPtp": cienaCesPtp,
       "cienaCesPtpTable": cienaCesPtpTable,
       "cienaCesPtpEntry": cienaCesPtpEntry,
       "cienaCesPtpIfIndex": cienaCesPtpIfIndex,
       "cienaCesPtpSlotIndex": cienaCesPtpSlotIndex,
       "cienaCesPtpPortIndex": cienaCesPtpPortIndex,
       "cienaCesPtpPortNumber": cienaCesPtpPortNumber,
       "cienaCesPtpIfDescr": cienaCesPtpIfDescr,
       "cienaCesPtpModulationScheme": cienaCesPtpModulationScheme,
       "cienaCesPtpSupportedOpuTypes": cienaCesPtpSupportedOpuTypes,
       "cienaCesPtpAdminState": cienaCesPtpAdminState,
       "cienaCesPtpOperState": cienaCesPtpOperState,
       "cienaCesPtpAdminWavelength": cienaCesPtpAdminWavelength,
       "cienaCesPtpAdminFrequency": cienaCesPtpAdminFrequency,
       "cienaCesPtpTxPowerReduction": cienaCesPtpTxPowerReduction,
       "cienaCesPtpTxPower": cienaCesPtpTxPower,
       "cienaCesPtpLineSysType": cienaCesPtpLineSysType,
       "cienaCesPtpOptimizationMode": cienaCesPtpOptimizationMode,
       "cienaCesPtpWavelengthSpacing": cienaCesPtpWavelengthSpacing,
       "cienaCesPtpSpectralOccupancy": cienaCesPtpSpectralOccupancy,
       "cienaCesPtpTxTuningMode": cienaCesPtpTxTuningMode,
       "cienaCesPtpRotation": cienaCesPtpRotation,
       "cienaCesPtpCarrierCentering": cienaCesPtpCarrierCentering,
       "cienaCesPtpOchEnmMode": cienaCesPtpOchEnmMode,
       "cienaCesPtpChContentionDetect": cienaCesPtpChContentionDetect,
       "cienaCesPtpStormControl": cienaCesPtpStormControl,
       "cienaCesPtpStormMode": cienaCesPtpStormMode,
       "cienaCesPtpStormPath1": cienaCesPtpStormPath1,
       "cienaCesPtpStormPath2": cienaCesPtpStormPath2,
       "cienaCesPtpSpliCntrl": cienaCesPtpSpliCntrl,
       "cienaCesPtpChildOtuIfIndex": cienaCesPtpChildOtuIfIndex,
       "cienaCesPtpMIBConformance": cienaCesPtpMIBConformance,
       "cienaCesPtpMIBCompliances": cienaCesPtpMIBCompliances,
       "cienaCesPtpMIBGroups": cienaCesPtpMIBGroups,
       "cienaCesPtpMIBNotificationsPrefix": cienaCesPtpMIBNotificationsPrefix,
       "cienaCesPtpMIBNotifications": cienaCesPtpMIBNotifications,
       "cienaCesPtpAdminStateChangeNotification": cienaCesPtpAdminStateChangeNotification,
       "cienaCesPtpOperStateChangeNotification": cienaCesPtpOperStateChangeNotification,
       "cienaCesPtpAdminWavelengthChangeNotification": cienaCesPtpAdminWavelengthChangeNotification,
       "cienaCesPtpAdminFrequencyChangeNotification": cienaCesPtpAdminFrequencyChangeNotification,
       "cienaCesPtpTxPowerChangeNotification": cienaCesPtpTxPowerChangeNotification,
       "cienaCesPtpLineSysTypeChangeNotification": cienaCesPtpLineSysTypeChangeNotification,
       "cienaCesPtpOptimizationModeChangeNotification": cienaCesPtpOptimizationModeChangeNotification,
       "cienaCesPtpWavelengthSpacingChangeNotification": cienaCesPtpWavelengthSpacingChangeNotification,
       "cienaCesPtpCreatedNotification": cienaCesPtpCreatedNotification,
       "cienaCesPtpDeletedNotification": cienaCesPtpDeletedNotification}
)
