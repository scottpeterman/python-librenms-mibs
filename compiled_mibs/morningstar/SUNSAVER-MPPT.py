# SNMP MIB module (SUNSAVER-MPPT) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\morningstar\SUNSAVER-MPPT
# Produced by pysmi-1.6.2 at Thu Oct  2 12:10:54 2025
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

(morningstar,) = mibBuilder.importSymbols(
    "MORNINGSTAR",
    "morningstar")

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

sunsaverMppt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 33333, 3)
)
if mibBuilder.loadTexts:
    sunsaverMppt.setRevisions(
        ("2019-12-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ChargeStateEnum(TextualConvention, Integer32):
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
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("start", 0),
          ("nightCheck", 1),
          ("disconnect", 2),
          ("night", 3),
          ("fault", 4),
          ("bulkMppt", 5),
          ("absorption", 6),
          ("float", 7),
          ("equalize", 8))
    )



class LoadStateEnum(TextualConvention, Integer32):
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
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("start", 0),
          ("normal", 1),
          ("lvdWarning", 2),
          ("lvd", 3),
          ("fault", 4),
          ("disconnect", 5),
          ("normalOff", 6),
          ("override", 7),
          ("notUsed", 8))
    )



class DipSwitchesEnum(TextualConvention, Integer32):
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
        *(("off-off-off-off", 0),
          ("on-off-off-off", 1),
          ("off-on-off-off", 2),
          ("on-on-off-off", 3),
          ("off-off-on-off", 4),
          ("on-off-on-off", 5),
          ("off-on-on-off", 6),
          ("on-on-on-off", 7),
          ("off-off-off-on", 8),
          ("on-off-off-on", 9),
          ("off-on-off-on", 10),
          ("on-on-off-on", 11),
          ("off-off-on-on", 12),
          ("on-off-on-on", 13),
          ("off-on-on-on", 14),
          ("on-on-on-on", 15))
    )



class LedStateEnum(TextualConvention, Integer32):
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("ledStart", 0),
          ("ledStart2", 1),
          ("ledBranch", 2),
          ("equalizeFastGreen", 3),
          ("floatSlowGreen", 4),
          ("absorptionFlashingGreen", 5),
          ("green", 6),
          ("undefined", 7),
          ("yellow", 8),
          ("undefined1", 9),
          ("flashingRed", 10),
          ("red", 11),
          ("r-y-gError", 12),
          ("ry-gError", 13),
          ("rg-yError", 14),
          ("r-yErrorHtd", 15),
          ("r-gErrorHvd", 16),
          ("ry-gyError", 17),
          ("gyrFlashingError", 18),
          ("gyrX2", 19))
    )



class ArrayFaultsBitfield(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("overcurrent", 0),
          ("mosfetSShorted", 1),
          ("softwareFault", 2),
          ("batteryHvd", 3),
          ("arrayHvd", 4),
          ("customSettingsEdit", 5),
          ("rtsShorted", 6),
          ("rtsNoLongerValid", 7),
          ("localTempSensorDamaged", 8),
          ("fault10Undefined", 9),
          ("fault11Undefined", 10),
          ("fault12Undefined", 11),
          ("fault13Undefined", 12),
          ("fault14Undefined", 13),
          ("fault15Undefined", 14),
          ("fault16Undefined", 15))
    )


class LoadFaultsBitfield(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("externalShortCircuit", 0),
          ("overcurrent", 1),
          ("mosfetShorted", 2),
          ("software", 3),
          ("loadHvd", 4),
          ("highTempDisconnect", 5),
          ("customSettingsEdit", 6),
          ("unknownLoadFault", 7))
    )


class AlarmsBitfield(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("rtsOpen", 0),
          ("rtsShorted", 1),
          ("rtsDisconnected", 2),
          ("heatsinkTempSensorOpen", 3),
          ("heatsinkTempSensorShorted", 4),
          ("sspptHot", 5),
          ("currentLimit", 6),
          ("currentOffset", 7),
          ("undefined", 8),
          ("undefined1", 9),
          ("uncalibrated", 10),
          ("rtsMiswire", 11),
          ("undefined12", 12),
          ("undefined123", 13),
          ("systemMiswire", 14),
          ("mosfetSOpen", 15),
          ("p12VoltageReferenceOff", 16),
          ("highVaCurrentLimit", 17),
          ("alarm19Undefined", 18),
          ("alarm20Undefined", 19),
          ("alarm21Undefined", 20),
          ("alarm22Undefined", 21),
          ("alarm23Undefined", 22),
          ("alarm24Undefined", 23))
    )


class ArrayFaultsDailyBitfield(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("overcurrent", 0),
          ("mosfetSShorted", 1),
          ("softwareFault", 2),
          ("batteryHvd", 3),
          ("arrayHvd", 4),
          ("customSettingsEdit", 5),
          ("rtsShorted", 6),
          ("rtsNoLongerValid", 7),
          ("localTempSensorDamaged", 8),
          ("fault11Undefined", 9),
          ("fault12Undefined", 10),
          ("fault13Undefined", 11),
          ("fault14Undefined", 12),
          ("fault15Undefined", 13),
          ("fault16Undefined", 14),
          ("fault17Undefined", 15))
    )


class LoadFaultsDailyBitfield(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("externalShortCircuit", 0),
          ("overcurrent", 1),
          ("mosfetShorted", 2),
          ("software", 3),
          ("loadHvd", 4),
          ("highTempDisconnect", 5),
          ("customSettingsEdit", 6),
          ("unknownLoadFault", 7))
    )


class AlarmsDailyBitfield(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("rtsOpen", 0),
          ("rtsShorted", 1),
          ("rtsDisconnected", 2),
          ("heatsinkTempSensorOpen", 3),
          ("heatsinkTempSensorShorted", 4),
          ("sspptHot", 5),
          ("currentLimit", 6),
          ("currentOffset", 7),
          ("undefined", 8),
          ("undefined1", 9),
          ("uncalibrated", 10),
          ("rtsMiswire", 11),
          ("undefined12", 12),
          ("undefined123", 13),
          ("systemMiswire", 14),
          ("mosfetSOpen", 15),
          ("p12VoltageReferenceOff", 16),
          ("highVaCurrentLimit", 17),
          ("alarm19Undefined", 18),
          ("alarm20Undefined", 19),
          ("alarm21Undefined", 20),
          ("alarm22Undefined", 21),
          ("alarm23Undefined", 22),
          ("alarm24Undefined", 23))
    )


# MIB Managed Objects in the order of their OIDs



class _SubModel_Type(DisplayString):
    """Custom type subModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SubModel_Type.__name__ = "DisplayString"
_SubModel_Object = MibScalar
subModel = _SubModel_Object(
    (1, 3, 6, 1, 4, 1, 33333, 3, 1),
    _SubModel_Type()
)
subModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subModel.setStatus("current")


class _SerialNumber_Type(DisplayString):
    """Custom type serialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SerialNumber_Type.__name__ = "DisplayString"
_SerialNumber_Object = MibScalar
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 33333, 3, 2),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("current")


class _DeviceVersion_Type(DisplayString):
    """Custom type deviceVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DeviceVersion_Type.__name__ = "DisplayString"
_DeviceVersion_Object = MibScalar
deviceVersion = _DeviceVersion_Object(
    (1, 3, 6, 1, 4, 1, 33333, 3, 3),
    _DeviceVersion_Type()
)
deviceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceVersion.setStatus("current")
_BatteryVoltage_Type = Unsigned32
_BatteryVoltage_Object = MibScalar
batteryVoltage = _BatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 33333, 3, 30),
    _BatteryVoltage_Type()
)
batteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryVoltage.setStatus("current")
_ArrayVoltage_Type = Unsigned32
_ArrayVoltage_Object = MibScalar
arrayVoltage = _ArrayVoltage_Object(
    (1, 3, 6, 1, 4, 1, 33333, 3, 31),
    _ArrayVoltage_Type()
)
arrayVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayVoltage.setStatus("current")
_LoadVoltage_Type = Unsigned32
_LoadVoltage_Object = MibScalar
loadVoltage = _LoadVoltage_Object(
    (1, 3, 6, 1, 4, 1, 33333, 3, 32),
    _LoadVoltage_Type()
)
loadVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadVoltage.setStatus("current")
_ChargeCurrent_Type = Unsigned32
_ChargeCurrent_Object = MibScalar
chargeCurrent = _ChargeCurrent_Object(
    (1, 3, 6, 1, 4, 1, 33333, 3, 33),
    _ChargeCurrent_Type()
)
chargeCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chargeCurrent.setStatus("current")
_LoadCurrent_Type = Unsigned32
_LoadCurrent_Object = MibScalar
loadCurrent = _LoadCurrent_Object(
    (1, 3, 6, 1, 4, 1, 33333, 3, 34),
    _LoadCurrent_Type()
)
loadCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadCurrent.setStatus("current")
_HeatsinkTemperature_Type = Integer32
_HeatsinkTemperature_Object = MibScalar
heatsinkTemperature = _HeatsinkTemperature_Object(
    (1, 3, 6, 1, 4, 1, 33333, 3, 35),
    _HeatsinkTemperature_Type()
)
heatsinkTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heatsinkTemperature.setStatus("current")
_BatteryTemperature_Type = Integer32
_BatteryTemperature_Object = MibScalar
batteryTemperature = _BatteryTemperature_Object(
    (1, 3, 6, 1, 4, 1, 33333, 3, 36),
    _BatteryTemperature_Type()
)
batteryTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTemperature.setStatus("current")
_AmbientTemperature_Type = Integer32
_AmbientTemperature_Object = MibScalar
ambientTemperature = _AmbientTemperature_Object(
    (1, 3, 6, 1, 4, 1, 33333, 3, 37),
    _AmbientTemperature_Type()
)
ambientTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ambientTemperature.setStatus("current")
_RtsTemperature_Type = Integer32
_RtsTemperature_Object = MibScalar
rtsTemperature = _RtsTemperature_Object(
    (1, 3, 6, 1, 4, 1, 33333, 3, 38),
    _RtsTemperature_Type()
)
rtsTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtsTemperature.setStatus("current")
_ChargeState_Type = ChargeStateEnum
_ChargeState_Object = MibScalar
chargeState = _ChargeState_Object(
    (1, 3, 6, 1, 4, 1, 33333, 3, 39),
    _ChargeState_Type()
)
chargeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chargeState.setStatus("current")
_ArrayFaults_Type = ArrayFaultsBitfield
_ArrayFaults_Object = MibScalar
arrayFaults = _ArrayFaults_Object(
    (1, 3, 6, 1, 4, 1, 33333, 3, 40),
    _ArrayFaults_Type()
)
arrayFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayFaults.setStatus("current")
_BatteryVoltageSlow_Type = Unsigned32
_BatteryVoltageSlow_Object = MibScalar
batteryVoltageSlow = _BatteryVoltageSlow_Object(
    (1, 3, 6, 1, 4, 1, 33333, 3, 41),
    _BatteryVoltageSlow_Type()
)
batteryVoltageSlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryVoltageSlow.setStatus("current")
_TargetVoltage_Type = Unsigned32
_TargetVoltage_Object = MibScalar
targetVoltage = _TargetVoltage_Object(
    (1, 3, 6, 1, 4, 1, 33333, 3, 42),
    _TargetVoltage_Type()
)
targetVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    targetVoltage.setStatus("current")
_AhChargeResettable_Type = Unsigned32
_AhChargeResettable_Object = MibScalar
ahChargeResettable = _AhChargeResettable_Object(
    (1, 3, 6, 1, 4, 1, 33333, 3, 43),
    _AhChargeResettable_Type()
)
ahChargeResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahChargeResettable.setStatus("current")
_AhChargeTotal_Type = Unsigned32
_AhChargeTotal_Object = MibScalar
ahChargeTotal = _AhChargeTotal_Object(
    (1, 3, 6, 1, 4, 1, 33333, 3, 44),
    _AhChargeTotal_Type()
)
ahChargeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahChargeTotal.setStatus("current")
_KwhCharge_Type = Unsigned32
_KwhCharge_Object = MibScalar
kwhCharge = _KwhCharge_Object(
    (1, 3, 6, 1, 4, 1, 33333, 3, 45),
    _KwhCharge_Type()
)
kwhCharge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kwhCharge.setStatus("current")
_LoadState_Type = LoadStateEnum
_LoadState_Object = MibScalar
loadState = _LoadState_Object(
    (1, 3, 6, 1, 4, 1, 33333, 3, 46),
    _LoadState_Type()
)
loadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadState.setStatus("current")
_LoadFaults_Type = LoadFaultsBitfield
_LoadFaults_Object = MibScalar
loadFaults = _LoadFaults_Object(
    (1, 3, 6, 1, 4, 1, 33333, 3, 47),
    _LoadFaults_Type()
)
loadFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadFaults.setStatus("current")
_LvdSetpoint_Type = Unsigned32
_LvdSetpoint_Object = MibScalar
lvdSetpoint = _LvdSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 33333, 3, 48),
    _LvdSetpoint_Type()
)
lvdSetpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lvdSetpoint.setStatus("current")
_AhLoadResettable_Type = Unsigned32
_AhLoadResettable_Object = MibScalar
ahLoadResettable = _AhLoadResettable_Object(
    (1, 3, 6, 1, 4, 1, 33333, 3, 49),
    _AhLoadResettable_Type()
)
ahLoadResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahLoadResettable.setStatus("current")
_AhLoadTotal_Type = Unsigned32
_AhLoadTotal_Object = MibScalar
ahLoadTotal = _AhLoadTotal_Object(
    (1, 3, 6, 1, 4, 1, 33333, 3, 50),
    _AhLoadTotal_Type()
)
ahLoadTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahLoadTotal.setStatus("current")
_Hourmeter_Type = Unsigned32
_Hourmeter_Object = MibScalar
hourmeter = _Hourmeter_Object(
    (1, 3, 6, 1, 4, 1, 33333, 3, 51),
    _Hourmeter_Type()
)
hourmeter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hourmeter.setStatus("current")
_Alarms_Type = AlarmsBitfield
_Alarms_Object = MibScalar
alarms = _Alarms_Object(
    (1, 3, 6, 1, 4, 1, 33333, 3, 52),
    _Alarms_Type()
)
alarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarms.setStatus("current")
_DipSwitches_Type = DipSwitchesEnum
_DipSwitches_Object = MibScalar
dipSwitches = _DipSwitches_Object(
    (1, 3, 6, 1, 4, 1, 33333, 3, 53),
    _DipSwitches_Type()
)
dipSwitches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dipSwitches.setStatus("current")
_LedState_Type = LedStateEnum
_LedState_Object = MibScalar
ledState = _LedState_Object(
    (1, 3, 6, 1, 4, 1, 33333, 3, 54),
    _LedState_Type()
)
ledState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledState.setStatus("current")
_ArrayPower_Type = Unsigned32
_ArrayPower_Object = MibScalar
arrayPower = _ArrayPower_Object(
    (1, 3, 6, 1, 4, 1, 33333, 3, 55),
    _ArrayPower_Type()
)
arrayPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayPower.setStatus("current")
_ArrayVmp_Type = Unsigned32
_ArrayVmp_Object = MibScalar
arrayVmp = _ArrayVmp_Object(
    (1, 3, 6, 1, 4, 1, 33333, 3, 56),
    _ArrayVmp_Type()
)
arrayVmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayVmp.setStatus("current")
_ArrayMaxPowerSweep_Type = Unsigned32
_ArrayMaxPowerSweep_Object = MibScalar
arrayMaxPowerSweep = _ArrayMaxPowerSweep_Object(
    (1, 3, 6, 1, 4, 1, 33333, 3, 57),
    _ArrayMaxPowerSweep_Type()
)
arrayMaxPowerSweep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayMaxPowerSweep.setStatus("current")
_ArrayVoc_Type = Unsigned32
_ArrayVoc_Object = MibScalar
arrayVoc = _ArrayVoc_Object(
    (1, 3, 6, 1, 4, 1, 33333, 3, 58),
    _ArrayVoc_Type()
)
arrayVoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayVoc.setStatus("current")
_VbMinDaily_Type = Unsigned32
_VbMinDaily_Object = MibScalar
vbMinDaily = _VbMinDaily_Object(
    (1, 3, 6, 1, 4, 1, 33333, 3, 59),
    _VbMinDaily_Type()
)
vbMinDaily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vbMinDaily.setStatus("current")
_VbMaxDaily_Type = Unsigned32
_VbMaxDaily_Object = MibScalar
vbMaxDaily = _VbMaxDaily_Object(
    (1, 3, 6, 1, 4, 1, 33333, 3, 60),
    _VbMaxDaily_Type()
)
vbMaxDaily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vbMaxDaily.setStatus("current")
_AhChargeDaily_Type = Unsigned32
_AhChargeDaily_Object = MibScalar
ahChargeDaily = _AhChargeDaily_Object(
    (1, 3, 6, 1, 4, 1, 33333, 3, 61),
    _AhChargeDaily_Type()
)
ahChargeDaily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahChargeDaily.setStatus("current")
_AhLoadDaily_Type = Unsigned32
_AhLoadDaily_Object = MibScalar
ahLoadDaily = _AhLoadDaily_Object(
    (1, 3, 6, 1, 4, 1, 33333, 3, 62),
    _AhLoadDaily_Type()
)
ahLoadDaily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahLoadDaily.setStatus("current")
_ArrayFaultsDaily_Type = ArrayFaultsDailyBitfield
_ArrayFaultsDaily_Object = MibScalar
arrayFaultsDaily = _ArrayFaultsDaily_Object(
    (1, 3, 6, 1, 4, 1, 33333, 3, 63),
    _ArrayFaultsDaily_Type()
)
arrayFaultsDaily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayFaultsDaily.setStatus("current")
_LoadFaultsDaily_Type = LoadFaultsDailyBitfield
_LoadFaultsDaily_Object = MibScalar
loadFaultsDaily = _LoadFaultsDaily_Object(
    (1, 3, 6, 1, 4, 1, 33333, 3, 64),
    _LoadFaultsDaily_Type()
)
loadFaultsDaily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadFaultsDaily.setStatus("current")
_AlarmsDaily_Type = AlarmsDailyBitfield
_AlarmsDaily_Object = MibScalar
alarmsDaily = _AlarmsDaily_Object(
    (1, 3, 6, 1, 4, 1, 33333, 3, 65),
    _AlarmsDaily_Type()
)
alarmsDaily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmsDaily.setStatus("current")
_VbMin_Type = Unsigned32
_VbMin_Object = MibScalar
vbMin = _VbMin_Object(
    (1, 3, 6, 1, 4, 1, 33333, 3, 66),
    _VbMin_Type()
)
vbMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vbMin.setStatus("current")
_VbMax_Type = Unsigned32
_VbMax_Object = MibScalar
vbMax = _VbMax_Object(
    (1, 3, 6, 1, 4, 1, 33333, 3, 67),
    _VbMax_Type()
)
vbMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vbMax.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUNSAVER-MPPT",
    **{"ChargeStateEnum": ChargeStateEnum,
       "LoadStateEnum": LoadStateEnum,
       "DipSwitchesEnum": DipSwitchesEnum,
       "LedStateEnum": LedStateEnum,
       "ArrayFaultsBitfield": ArrayFaultsBitfield,
       "LoadFaultsBitfield": LoadFaultsBitfield,
       "AlarmsBitfield": AlarmsBitfield,
       "ArrayFaultsDailyBitfield": ArrayFaultsDailyBitfield,
       "LoadFaultsDailyBitfield": LoadFaultsDailyBitfield,
       "AlarmsDailyBitfield": AlarmsDailyBitfield,
       "sunsaverMppt": sunsaverMppt,
       "subModel": subModel,
       "serialNumber": serialNumber,
       "deviceVersion": deviceVersion,
       "batteryVoltage": batteryVoltage,
       "arrayVoltage": arrayVoltage,
       "loadVoltage": loadVoltage,
       "chargeCurrent": chargeCurrent,
       "loadCurrent": loadCurrent,
       "heatsinkTemperature": heatsinkTemperature,
       "batteryTemperature": batteryTemperature,
       "ambientTemperature": ambientTemperature,
       "rtsTemperature": rtsTemperature,
       "chargeState": chargeState,
       "arrayFaults": arrayFaults,
       "batteryVoltageSlow": batteryVoltageSlow,
       "targetVoltage": targetVoltage,
       "ahChargeResettable": ahChargeResettable,
       "ahChargeTotal": ahChargeTotal,
       "kwhCharge": kwhCharge,
       "loadState": loadState,
       "loadFaults": loadFaults,
       "lvdSetpoint": lvdSetpoint,
       "ahLoadResettable": ahLoadResettable,
       "ahLoadTotal": ahLoadTotal,
       "hourmeter": hourmeter,
       "alarms": alarms,
       "dipSwitches": dipSwitches,
       "ledState": ledState,
       "arrayPower": arrayPower,
       "arrayVmp": arrayVmp,
       "arrayMaxPowerSweep": arrayMaxPowerSweep,
       "arrayVoc": arrayVoc,
       "vbMinDaily": vbMinDaily,
       "vbMaxDaily": vbMaxDaily,
       "ahChargeDaily": ahChargeDaily,
       "ahLoadDaily": ahLoadDaily,
       "arrayFaultsDaily": arrayFaultsDaily,
       "loadFaultsDaily": loadFaultsDaily,
       "alarmsDaily": alarmsDaily,
       "vbMin": vbMin,
       "vbMax": vbMax}
)
