# SNMP MIB module (CPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cyberpower\CPS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:33:48 2025
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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cps_ObjectIdentity = ObjectIdentity
cps = _Cps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1)
)
_Hardware_ObjectIdentity = ObjectIdentity
hardware = _Hardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1)
)
_Ups_ObjectIdentity = ObjectIdentity
ups = _Ups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1)
)
_UpsIdent_ObjectIdentity = ObjectIdentity
upsIdent = _UpsIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 1)
)
_UpsBaseIdent_ObjectIdentity = ObjectIdentity
upsBaseIdent = _UpsBaseIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 1, 1)
)
_UpsBaseIdentModel_Type = DisplayString
_UpsBaseIdentModel_Object = MibScalar
upsBaseIdentModel = _UpsBaseIdentModel_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 1, 1, 1),
    _UpsBaseIdentModel_Type()
)
upsBaseIdentModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBaseIdentModel.setStatus("mandatory")
_UpsBaseIdentName_Type = DisplayString
_UpsBaseIdentName_Object = MibScalar
upsBaseIdentName = _UpsBaseIdentName_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 1, 1, 2),
    _UpsBaseIdentName_Type()
)
upsBaseIdentName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsBaseIdentName.setStatus("mandatory")
_UpsAdvanceIdent_ObjectIdentity = ObjectIdentity
upsAdvanceIdent = _UpsAdvanceIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 1, 2)
)
_UpsAdvanceIdentFirmwareRevision_Type = DisplayString
_UpsAdvanceIdentFirmwareRevision_Object = MibScalar
upsAdvanceIdentFirmwareRevision = _UpsAdvanceIdentFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 1, 2, 1),
    _UpsAdvanceIdentFirmwareRevision_Type()
)
upsAdvanceIdentFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAdvanceIdentFirmwareRevision.setStatus("mandatory")
_UpsAdvanceIdentDateOfManufacture_Type = DisplayString
_UpsAdvanceIdentDateOfManufacture_Object = MibScalar
upsAdvanceIdentDateOfManufacture = _UpsAdvanceIdentDateOfManufacture_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 1, 2, 2),
    _UpsAdvanceIdentDateOfManufacture_Type()
)
upsAdvanceIdentDateOfManufacture.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAdvanceIdentDateOfManufacture.setStatus("mandatory")
_UpsAdvanceIdentSerialNumber_Type = DisplayString
_UpsAdvanceIdentSerialNumber_Object = MibScalar
upsAdvanceIdentSerialNumber = _UpsAdvanceIdentSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 1, 2, 3),
    _UpsAdvanceIdentSerialNumber_Type()
)
upsAdvanceIdentSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAdvanceIdentSerialNumber.setStatus("mandatory")
_UpsAdvanceIdentAgentFirmwareRevision_Type = DisplayString
_UpsAdvanceIdentAgentFirmwareRevision_Object = MibScalar
upsAdvanceIdentAgentFirmwareRevision = _UpsAdvanceIdentAgentFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 1, 2, 4),
    _UpsAdvanceIdentAgentFirmwareRevision_Type()
)
upsAdvanceIdentAgentFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAdvanceIdentAgentFirmwareRevision.setStatus("mandatory")
_UpsAdvanceIdentLCDFirmwareVersion_Type = DisplayString
_UpsAdvanceIdentLCDFirmwareVersion_Object = MibScalar
upsAdvanceIdentLCDFirmwareVersion = _UpsAdvanceIdentLCDFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 1, 2, 5),
    _UpsAdvanceIdentLCDFirmwareVersion_Type()
)
upsAdvanceIdentLCDFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAdvanceIdentLCDFirmwareVersion.setStatus("mandatory")
_UpsAdvanceIdentPowerRating_Type = Integer32
_UpsAdvanceIdentPowerRating_Object = MibScalar
upsAdvanceIdentPowerRating = _UpsAdvanceIdentPowerRating_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 1, 2, 6),
    _UpsAdvanceIdentPowerRating_Type()
)
upsAdvanceIdentPowerRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAdvanceIdentPowerRating.setStatus("mandatory")
_UpsAdvanceIdentLoadPower_Type = Integer32
_UpsAdvanceIdentLoadPower_Object = MibScalar
upsAdvanceIdentLoadPower = _UpsAdvanceIdentLoadPower_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 1, 2, 7),
    _UpsAdvanceIdentLoadPower_Type()
)
upsAdvanceIdentLoadPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAdvanceIdentLoadPower.setStatus("mandatory")
_UpsAdvanceIdentCurrentRating_Type = Integer32
_UpsAdvanceIdentCurrentRating_Object = MibScalar
upsAdvanceIdentCurrentRating = _UpsAdvanceIdentCurrentRating_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 1, 2, 8),
    _UpsAdvanceIdentCurrentRating_Type()
)
upsAdvanceIdentCurrentRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAdvanceIdentCurrentRating.setStatus("mandatory")
_UpsAdvanceIdentAgentSerialNumber_Type = DisplayString
_UpsAdvanceIdentAgentSerialNumber_Object = MibScalar
upsAdvanceIdentAgentSerialNumber = _UpsAdvanceIdentAgentSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 1, 2, 9),
    _UpsAdvanceIdentAgentSerialNumber_Type()
)
upsAdvanceIdentAgentSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAdvanceIdentAgentSerialNumber.setStatus("mandatory")
_UpsBattery_ObjectIdentity = ObjectIdentity
upsBattery = _UpsBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 2)
)
_UpsBaseBattery_ObjectIdentity = ObjectIdentity
upsBaseBattery = _UpsBaseBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 2, 1)
)


class _UpsBaseBatteryStatus_Type(Integer32):
    """Custom type upsBaseBatteryStatus based on Integer32"""
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
          ("batteryNormal", 2),
          ("batteryLow", 3),
          ("batteryNotPresent", 4))
    )


_UpsBaseBatteryStatus_Type.__name__ = "Integer32"
_UpsBaseBatteryStatus_Object = MibScalar
upsBaseBatteryStatus = _UpsBaseBatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 2, 1, 1),
    _UpsBaseBatteryStatus_Type()
)
upsBaseBatteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBaseBatteryStatus.setStatus("mandatory")
_UpsBaseBatteryTimeOnBattery_Type = TimeTicks
_UpsBaseBatteryTimeOnBattery_Object = MibScalar
upsBaseBatteryTimeOnBattery = _UpsBaseBatteryTimeOnBattery_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 2, 1, 2),
    _UpsBaseBatteryTimeOnBattery_Type()
)
upsBaseBatteryTimeOnBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBaseBatteryTimeOnBattery.setStatus("mandatory")
_UpsBaseBatteryLastReplaceDate_Type = DisplayString
_UpsBaseBatteryLastReplaceDate_Object = MibScalar
upsBaseBatteryLastReplaceDate = _UpsBaseBatteryLastReplaceDate_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 2, 1, 3),
    _UpsBaseBatteryLastReplaceDate_Type()
)
upsBaseBatteryLastReplaceDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsBaseBatteryLastReplaceDate.setStatus("mandatory")
_UpsBaseBatteryAgeRecommand_Type = Integer32
_UpsBaseBatteryAgeRecommand_Object = MibScalar
upsBaseBatteryAgeRecommand = _UpsBaseBatteryAgeRecommand_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 2, 1, 4),
    _UpsBaseBatteryAgeRecommand_Type()
)
upsBaseBatteryAgeRecommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBaseBatteryAgeRecommand.setStatus("mandatory")
_UpsAdvanceBattery_ObjectIdentity = ObjectIdentity
upsAdvanceBattery = _UpsAdvanceBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 2, 2)
)
_UpsAdvanceBatteryCapacity_Type = Gauge32
_UpsAdvanceBatteryCapacity_Object = MibScalar
upsAdvanceBatteryCapacity = _UpsAdvanceBatteryCapacity_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 2, 2, 1),
    _UpsAdvanceBatteryCapacity_Type()
)
upsAdvanceBatteryCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAdvanceBatteryCapacity.setStatus("mandatory")
_UpsAdvanceBatteryVoltage_Type = Integer32
_UpsAdvanceBatteryVoltage_Object = MibScalar
upsAdvanceBatteryVoltage = _UpsAdvanceBatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 2, 2, 2),
    _UpsAdvanceBatteryVoltage_Type()
)
upsAdvanceBatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAdvanceBatteryVoltage.setStatus("mandatory")
_UpsAdvanceBatteryTemperature_Type = Gauge32
_UpsAdvanceBatteryTemperature_Object = MibScalar
upsAdvanceBatteryTemperature = _UpsAdvanceBatteryTemperature_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 2, 2, 3),
    _UpsAdvanceBatteryTemperature_Type()
)
upsAdvanceBatteryTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAdvanceBatteryTemperature.setStatus("mandatory")
_UpsAdvanceBatteryRunTimeRemaining_Type = TimeTicks
_UpsAdvanceBatteryRunTimeRemaining_Object = MibScalar
upsAdvanceBatteryRunTimeRemaining = _UpsAdvanceBatteryRunTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 2, 2, 4),
    _UpsAdvanceBatteryRunTimeRemaining_Type()
)
upsAdvanceBatteryRunTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAdvanceBatteryRunTimeRemaining.setStatus("mandatory")


class _UpsAdvanceBatteryReplaceIndicator_Type(Integer32):
    """Custom type upsAdvanceBatteryReplaceIndicator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noBatteryNeedsReplacing", 1),
          ("batteryNeedsReplacing", 2))
    )


_UpsAdvanceBatteryReplaceIndicator_Type.__name__ = "Integer32"
_UpsAdvanceBatteryReplaceIndicator_Object = MibScalar
upsAdvanceBatteryReplaceIndicator = _UpsAdvanceBatteryReplaceIndicator_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 2, 2, 5),
    _UpsAdvanceBatteryReplaceIndicator_Type()
)
upsAdvanceBatteryReplaceIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAdvanceBatteryReplaceIndicator.setStatus("mandatory")
_UpsAdvanceBatteryFullChargeVoltage_Type = Integer32
_UpsAdvanceBatteryFullChargeVoltage_Object = MibScalar
upsAdvanceBatteryFullChargeVoltage = _UpsAdvanceBatteryFullChargeVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 2, 2, 6),
    _UpsAdvanceBatteryFullChargeVoltage_Type()
)
upsAdvanceBatteryFullChargeVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAdvanceBatteryFullChargeVoltage.setStatus("mandatory")
_UpsAdvanceBatteryCurrent_Type = Integer32
_UpsAdvanceBatteryCurrent_Object = MibScalar
upsAdvanceBatteryCurrent = _UpsAdvanceBatteryCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 2, 2, 7),
    _UpsAdvanceBatteryCurrent_Type()
)
upsAdvanceBatteryCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAdvanceBatteryCurrent.setStatus("mandatory")
_UpsAdvanceBatteryVoltageRating_Type = Integer32
_UpsAdvanceBatteryVoltageRating_Object = MibScalar
upsAdvanceBatteryVoltageRating = _UpsAdvanceBatteryVoltageRating_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 2, 2, 8),
    _UpsAdvanceBatteryVoltageRating_Type()
)
upsAdvanceBatteryVoltageRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAdvanceBatteryVoltageRating.setStatus("mandatory")
_UpsAdvanceBatteryLife_Type = Integer32
_UpsAdvanceBatteryLife_Object = MibScalar
upsAdvanceBatteryLife = _UpsAdvanceBatteryLife_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 2, 2, 9),
    _UpsAdvanceBatteryLife_Type()
)
upsAdvanceBatteryLife.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAdvanceBatteryLife.setStatus("mandatory")
_UpsInput_ObjectIdentity = ObjectIdentity
upsInput = _UpsInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 3)
)
_UpsBaseInput_ObjectIdentity = ObjectIdentity
upsBaseInput = _UpsBaseInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 3, 1)
)
_UpsBaseInputPhase_Type = Integer32
_UpsBaseInputPhase_Object = MibScalar
upsBaseInputPhase = _UpsBaseInputPhase_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 3, 1, 1),
    _UpsBaseInputPhase_Type()
)
upsBaseInputPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBaseInputPhase.setStatus("mandatory")
_UpsAdvanceInput_ObjectIdentity = ObjectIdentity
upsAdvanceInput = _UpsAdvanceInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 3, 2)
)
_UpsAdvanceInputLineVoltage_Type = Gauge32
_UpsAdvanceInputLineVoltage_Object = MibScalar
upsAdvanceInputLineVoltage = _UpsAdvanceInputLineVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 3, 2, 1),
    _UpsAdvanceInputLineVoltage_Type()
)
upsAdvanceInputLineVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAdvanceInputLineVoltage.setStatus("mandatory")
_UpsAdvanceInputMaxLineVoltage_Type = Gauge32
_UpsAdvanceInputMaxLineVoltage_Object = MibScalar
upsAdvanceInputMaxLineVoltage = _UpsAdvanceInputMaxLineVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 3, 2, 2),
    _UpsAdvanceInputMaxLineVoltage_Type()
)
upsAdvanceInputMaxLineVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAdvanceInputMaxLineVoltage.setStatus("mandatory")
_UpsAdvanceInputMinLineVoltage_Type = Gauge32
_UpsAdvanceInputMinLineVoltage_Object = MibScalar
upsAdvanceInputMinLineVoltage = _UpsAdvanceInputMinLineVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 3, 2, 3),
    _UpsAdvanceInputMinLineVoltage_Type()
)
upsAdvanceInputMinLineVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAdvanceInputMinLineVoltage.setStatus("mandatory")
_UpsAdvanceInputFrequency_Type = Gauge32
_UpsAdvanceInputFrequency_Object = MibScalar
upsAdvanceInputFrequency = _UpsAdvanceInputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 3, 2, 4),
    _UpsAdvanceInputFrequency_Type()
)
upsAdvanceInputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAdvanceInputFrequency.setStatus("mandatory")


class _UpsAdvanceInputLineFailCause_Type(Integer32):
    """Custom type upsAdvanceInputLineFailCause based on Integer32"""
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
        *(("noTransfer", 1),
          ("highLineVoltage", 2),
          ("brownout", 3),
          ("selfTest", 4))
    )


_UpsAdvanceInputLineFailCause_Type.__name__ = "Integer32"
_UpsAdvanceInputLineFailCause_Object = MibScalar
upsAdvanceInputLineFailCause = _UpsAdvanceInputLineFailCause_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 3, 2, 5),
    _UpsAdvanceInputLineFailCause_Type()
)
upsAdvanceInputLineFailCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAdvanceInputLineFailCause.setStatus("mandatory")


class _UpsAdvanceInputStatus_Type(Integer32):
    """Custom type upsAdvanceInputStatus based on Integer32"""
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
        *(("normal", 1),
          ("overVoltage", 2),
          ("underVoltage", 3),
          ("frequencyFailure", 4),
          ("blackout", 5))
    )


_UpsAdvanceInputStatus_Type.__name__ = "Integer32"
_UpsAdvanceInputStatus_Object = MibScalar
upsAdvanceInputStatus = _UpsAdvanceInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 3, 2, 6),
    _UpsAdvanceInputStatus_Type()
)
upsAdvanceInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAdvanceInputStatus.setStatus("mandatory")
_UpsOutput_ObjectIdentity = ObjectIdentity
upsOutput = _UpsOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 4)
)
_UpsBaseOutput_ObjectIdentity = ObjectIdentity
upsBaseOutput = _UpsBaseOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 4, 1)
)


class _UpsBaseOutputStatus_Type(Integer32):
    """Custom type upsBaseOutputStatus based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("onLine", 2),
          ("onBattery", 3),
          ("onBoost", 4),
          ("onSleep", 5),
          ("off", 6),
          ("rebooting", 7),
          ("onECO", 8),
          ("onBypass", 9),
          ("onBuck", 10),
          ("onOverload", 11))
    )


_UpsBaseOutputStatus_Type.__name__ = "Integer32"
_UpsBaseOutputStatus_Object = MibScalar
upsBaseOutputStatus = _UpsBaseOutputStatus_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 4, 1, 1),
    _UpsBaseOutputStatus_Type()
)
upsBaseOutputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBaseOutputStatus.setStatus("mandatory")
_UpsBaseOutputPhase_Type = Integer32
_UpsBaseOutputPhase_Object = MibScalar
upsBaseOutputPhase = _UpsBaseOutputPhase_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 4, 1, 2),
    _UpsBaseOutputPhase_Type()
)
upsBaseOutputPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBaseOutputPhase.setStatus("mandatory")
_UpsBaseOutputWorkingFrequency_Type = DisplayString
_UpsBaseOutputWorkingFrequency_Object = MibScalar
upsBaseOutputWorkingFrequency = _UpsBaseOutputWorkingFrequency_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 4, 1, 3),
    _UpsBaseOutputWorkingFrequency_Type()
)
upsBaseOutputWorkingFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBaseOutputWorkingFrequency.setStatus("mandatory")
_UpsAdvanceOutput_ObjectIdentity = ObjectIdentity
upsAdvanceOutput = _UpsAdvanceOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 4, 2)
)
_UpsAdvanceOutputVoltage_Type = Gauge32
_UpsAdvanceOutputVoltage_Object = MibScalar
upsAdvanceOutputVoltage = _UpsAdvanceOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 4, 2, 1),
    _UpsAdvanceOutputVoltage_Type()
)
upsAdvanceOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAdvanceOutputVoltage.setStatus("mandatory")
_UpsAdvanceOutputFrequency_Type = Gauge32
_UpsAdvanceOutputFrequency_Object = MibScalar
upsAdvanceOutputFrequency = _UpsAdvanceOutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 4, 2, 2),
    _UpsAdvanceOutputFrequency_Type()
)
upsAdvanceOutputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAdvanceOutputFrequency.setStatus("mandatory")
_UpsAdvanceOutputLoad_Type = Gauge32
_UpsAdvanceOutputLoad_Object = MibScalar
upsAdvanceOutputLoad = _UpsAdvanceOutputLoad_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 4, 2, 3),
    _UpsAdvanceOutputLoad_Type()
)
upsAdvanceOutputLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAdvanceOutputLoad.setStatus("mandatory")
_UpsAdvanceOutputCurrent_Type = Gauge32
_UpsAdvanceOutputCurrent_Object = MibScalar
upsAdvanceOutputCurrent = _UpsAdvanceOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 4, 2, 4),
    _UpsAdvanceOutputCurrent_Type()
)
upsAdvanceOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAdvanceOutputCurrent.setStatus("mandatory")
_UpsAdvanceOutputPower_Type = Gauge32
_UpsAdvanceOutputPower_Object = MibScalar
upsAdvanceOutputPower = _UpsAdvanceOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 4, 2, 5),
    _UpsAdvanceOutputPower_Type()
)
upsAdvanceOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAdvanceOutputPower.setStatus("mandatory")
_UpsConfig_ObjectIdentity = ObjectIdentity
upsConfig = _UpsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 5)
)
_UpsBaseConfig_ObjectIdentity = ObjectIdentity
upsBaseConfig = _UpsBaseConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 5, 1)
)
_UpsBaseConfigNumDevices_Type = Integer32
_UpsBaseConfigNumDevices_Object = MibScalar
upsBaseConfigNumDevices = _UpsBaseConfigNumDevices_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 5, 1, 1),
    _UpsBaseConfigNumDevices_Type()
)
upsBaseConfigNumDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBaseConfigNumDevices.setStatus("mandatory")
_UpsBaseConfigDeviceTable_Object = MibTable
upsBaseConfigDeviceTable = _UpsBaseConfigDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 5, 1, 2)
)
if mibBuilder.loadTexts:
    upsBaseConfigDeviceTable.setStatus("mandatory")
_UpsBaseConfigDeviceEntry_Object = MibTableRow
upsBaseConfigDeviceEntry = _UpsBaseConfigDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 5, 1, 2, 1)
)
upsBaseConfigDeviceEntry.setIndexNames(
    (0, "CPS-MIB", "deviceIndex"),
)
if mibBuilder.loadTexts:
    upsBaseConfigDeviceEntry.setStatus("mandatory")


class _DeviceIndex_Type(Integer32):
    """Custom type deviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DeviceIndex_Type.__name__ = "Integer32"
_DeviceIndex_Object = MibTableColumn
deviceIndex = _DeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 5, 1, 2, 1, 1),
    _DeviceIndex_Type()
)
deviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceIndex.setStatus("mandatory")
_DeviceName_Type = DisplayString
_DeviceName_Object = MibTableColumn
deviceName = _DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 5, 1, 2, 1, 2),
    _DeviceName_Type()
)
deviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceName.setStatus("mandatory")
_VaRating_Type = Integer32
_VaRating_Object = MibTableColumn
vaRating = _VaRating_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 5, 1, 2, 1, 3),
    _VaRating_Type()
)
vaRating.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vaRating.setStatus("mandatory")


class _AcceptThisDevice_Type(Integer32):
    """Custom type acceptThisDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AcceptThisDevice_Type.__name__ = "Integer32"
_AcceptThisDevice_Object = MibTableColumn
acceptThisDevice = _AcceptThisDevice_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 5, 1, 2, 1, 4),
    _AcceptThisDevice_Type()
)
acceptThisDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acceptThisDevice.setStatus("mandatory")
_UpsAdvanceConfig_ObjectIdentity = ObjectIdentity
upsAdvanceConfig = _UpsAdvanceConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 5, 2)
)
_UpsAdvanceConfigOutputVoltage_Type = Integer32
_UpsAdvanceConfigOutputVoltage_Object = MibScalar
upsAdvanceConfigOutputVoltage = _UpsAdvanceConfigOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 5, 2, 1),
    _UpsAdvanceConfigOutputVoltage_Type()
)
upsAdvanceConfigOutputVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAdvanceConfigOutputVoltage.setStatus("mandatory")
_UpsAdvanceConfigHighTransferVolt_Type = Integer32
_UpsAdvanceConfigHighTransferVolt_Object = MibScalar
upsAdvanceConfigHighTransferVolt = _UpsAdvanceConfigHighTransferVolt_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 5, 2, 2),
    _UpsAdvanceConfigHighTransferVolt_Type()
)
upsAdvanceConfigHighTransferVolt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAdvanceConfigHighTransferVolt.setStatus("mandatory")
_UpsAdvanceConfigLowTransferVolt_Type = Integer32
_UpsAdvanceConfigLowTransferVolt_Object = MibScalar
upsAdvanceConfigLowTransferVolt = _UpsAdvanceConfigLowTransferVolt_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 5, 2, 3),
    _UpsAdvanceConfigLowTransferVolt_Type()
)
upsAdvanceConfigLowTransferVolt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAdvanceConfigLowTransferVolt.setStatus("mandatory")


class _UpsAdvanceConfigAlarm_Type(Integer32):
    """Custom type upsAdvanceConfigAlarm based on Integer32"""
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
        *(("timed", 1),
          ("enable", 2),
          ("disable", 3),
          ("mute", 4))
    )


_UpsAdvanceConfigAlarm_Type.__name__ = "Integer32"
_UpsAdvanceConfigAlarm_Object = MibScalar
upsAdvanceConfigAlarm = _UpsAdvanceConfigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 5, 2, 4),
    _UpsAdvanceConfigAlarm_Type()
)
upsAdvanceConfigAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAdvanceConfigAlarm.setStatus("mandatory")
_UpsAdvanceConfigAlarmTimer_Type = TimeTicks
_UpsAdvanceConfigAlarmTimer_Object = MibScalar
upsAdvanceConfigAlarmTimer = _UpsAdvanceConfigAlarmTimer_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 5, 2, 5),
    _UpsAdvanceConfigAlarmTimer_Type()
)
upsAdvanceConfigAlarmTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAdvanceConfigAlarmTimer.setStatus("mandatory")
_UpsAdvanceConfigMinReturnCapacity_Type = Integer32
_UpsAdvanceConfigMinReturnCapacity_Object = MibScalar
upsAdvanceConfigMinReturnCapacity = _UpsAdvanceConfigMinReturnCapacity_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 5, 2, 6),
    _UpsAdvanceConfigMinReturnCapacity_Type()
)
upsAdvanceConfigMinReturnCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAdvanceConfigMinReturnCapacity.setStatus("mandatory")


class _UpsAdvanceConfigSensitivity_Type(Integer32):
    """Custom type upsAdvanceConfigSensitivity based on Integer32"""
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
        *(("auto", 1),
          ("low", 2),
          ("medium", 3),
          ("high", 4))
    )


_UpsAdvanceConfigSensitivity_Type.__name__ = "Integer32"
_UpsAdvanceConfigSensitivity_Object = MibScalar
upsAdvanceConfigSensitivity = _UpsAdvanceConfigSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 5, 2, 7),
    _UpsAdvanceConfigSensitivity_Type()
)
upsAdvanceConfigSensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAdvanceConfigSensitivity.setStatus("mandatory")
_UpsAdvanceConfigLowBatteryRunTime_Type = TimeTicks
_UpsAdvanceConfigLowBatteryRunTime_Object = MibScalar
upsAdvanceConfigLowBatteryRunTime = _UpsAdvanceConfigLowBatteryRunTime_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 5, 2, 8),
    _UpsAdvanceConfigLowBatteryRunTime_Type()
)
upsAdvanceConfigLowBatteryRunTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAdvanceConfigLowBatteryRunTime.setStatus("mandatory")
_UpsAdvanceConfigReturnDelay_Type = TimeTicks
_UpsAdvanceConfigReturnDelay_Object = MibScalar
upsAdvanceConfigReturnDelay = _UpsAdvanceConfigReturnDelay_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 5, 2, 9),
    _UpsAdvanceConfigReturnDelay_Type()
)
upsAdvanceConfigReturnDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAdvanceConfigReturnDelay.setStatus("mandatory")
_UpsAdvanceConfigShutoffDelay_Type = TimeTicks
_UpsAdvanceConfigShutoffDelay_Object = MibScalar
upsAdvanceConfigShutoffDelay = _UpsAdvanceConfigShutoffDelay_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 5, 2, 10),
    _UpsAdvanceConfigShutoffDelay_Type()
)
upsAdvanceConfigShutoffDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAdvanceConfigShutoffDelay.setStatus("mandatory")
_UpsAdvanceConfigSleepDelay_Type = TimeTicks
_UpsAdvanceConfigSleepDelay_Object = MibScalar
upsAdvanceConfigSleepDelay = _UpsAdvanceConfigSleepDelay_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 5, 2, 11),
    _UpsAdvanceConfigSleepDelay_Type()
)
upsAdvanceConfigSleepDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAdvanceConfigSleepDelay.setStatus("mandatory")


class _UpsAdvanceConfigSetEEPROMDefaults_Type(Integer32):
    """Custom type upsAdvanceConfigSetEEPROMDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noSetEEPROMDefaults", 1),
          ("setEEPROMDefaults", 2))
    )


_UpsAdvanceConfigSetEEPROMDefaults_Type.__name__ = "Integer32"
_UpsAdvanceConfigSetEEPROMDefaults_Object = MibScalar
upsAdvanceConfigSetEEPROMDefaults = _UpsAdvanceConfigSetEEPROMDefaults_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 5, 2, 12),
    _UpsAdvanceConfigSetEEPROMDefaults_Type()
)
upsAdvanceConfigSetEEPROMDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAdvanceConfigSetEEPROMDefaults.setStatus("mandatory")


class _UpsAdvanceConfigAutoRestore_Type(Integer32):
    """Custom type upsAdvanceConfigAutoRestore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_UpsAdvanceConfigAutoRestore_Type.__name__ = "Integer32"
_UpsAdvanceConfigAutoRestore_Object = MibScalar
upsAdvanceConfigAutoRestore = _UpsAdvanceConfigAutoRestore_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 5, 2, 13),
    _UpsAdvanceConfigAutoRestore_Type()
)
upsAdvanceConfigAutoRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAdvanceConfigAutoRestore.setStatus("mandatory")
_UpsAdvanceConfigRechargedCapacity_Type = Integer32
_UpsAdvanceConfigRechargedCapacity_Object = MibScalar
upsAdvanceConfigRechargedCapacity = _UpsAdvanceConfigRechargedCapacity_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 5, 2, 14),
    _UpsAdvanceConfigRechargedCapacity_Type()
)
upsAdvanceConfigRechargedCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAdvanceConfigRechargedCapacity.setStatus("mandatory")


class _UpsAdvanceConfigColdStart_Type(Integer32):
    """Custom type upsAdvanceConfigColdStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_UpsAdvanceConfigColdStart_Type.__name__ = "Integer32"
_UpsAdvanceConfigColdStart_Object = MibScalar
upsAdvanceConfigColdStart = _UpsAdvanceConfigColdStart_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 5, 2, 15),
    _UpsAdvanceConfigColdStart_Type()
)
upsAdvanceConfigColdStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAdvanceConfigColdStart.setStatus("mandatory")
_UpsAdvanceConfigDeepDischargeProtection_Type = Integer32
_UpsAdvanceConfigDeepDischargeProtection_Object = MibScalar
upsAdvanceConfigDeepDischargeProtection = _UpsAdvanceConfigDeepDischargeProtection_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 5, 2, 16),
    _UpsAdvanceConfigDeepDischargeProtection_Type()
)
upsAdvanceConfigDeepDischargeProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAdvanceConfigDeepDischargeProtection.setStatus("mandatory")


class _UpsAdvanceConfigSleepAfterAllClientShut_Type(Integer32):
    """Custom type upsAdvanceConfigSleepAfterAllClientShut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_UpsAdvanceConfigSleepAfterAllClientShut_Type.__name__ = "Integer32"
_UpsAdvanceConfigSleepAfterAllClientShut_Object = MibScalar
upsAdvanceConfigSleepAfterAllClientShut = _UpsAdvanceConfigSleepAfterAllClientShut_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 5, 2, 17),
    _UpsAdvanceConfigSleepAfterAllClientShut_Type()
)
upsAdvanceConfigSleepAfterAllClientShut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAdvanceConfigSleepAfterAllClientShut.setStatus("mandatory")
_UpsAdvanceConfigLowBatteryThreshold_Type = Integer32
_UpsAdvanceConfigLowBatteryThreshold_Object = MibScalar
upsAdvanceConfigLowBatteryThreshold = _UpsAdvanceConfigLowBatteryThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 5, 2, 18),
    _UpsAdvanceConfigLowBatteryThreshold_Type()
)
upsAdvanceConfigLowBatteryThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAdvanceConfigLowBatteryThreshold.setStatus("mandatory")
_UpsControl_ObjectIdentity = ObjectIdentity
upsControl = _UpsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 6)
)
_UpsBaseControl_ObjectIdentity = ObjectIdentity
upsBaseControl = _UpsBaseControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 6, 1)
)


class _UpsBaseControlConserveBattery_Type(Integer32):
    """Custom type upsBaseControlConserveBattery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noTurnOffUps", 1),
          ("turnOffUpsToConserveBattery", 2))
    )


_UpsBaseControlConserveBattery_Type.__name__ = "Integer32"
_UpsBaseControlConserveBattery_Object = MibScalar
upsBaseControlConserveBattery = _UpsBaseControlConserveBattery_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 6, 1, 1),
    _UpsBaseControlConserveBattery_Type()
)
upsBaseControlConserveBattery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsBaseControlConserveBattery.setStatus("mandatory")
_UpsAdvanceControl_ObjectIdentity = ObjectIdentity
upsAdvanceControl = _UpsAdvanceControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 6, 2)
)


class _UpsAdvanceControlUpsOff_Type(Integer32):
    """Custom type upsAdvanceControlUpsOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noTurnUpsOff", 1),
          ("turnUpsOff", 2),
          ("turnUpsOffGracefully", 3))
    )


_UpsAdvanceControlUpsOff_Type.__name__ = "Integer32"
_UpsAdvanceControlUpsOff_Object = MibScalar
upsAdvanceControlUpsOff = _UpsAdvanceControlUpsOff_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 6, 2, 1),
    _UpsAdvanceControlUpsOff_Type()
)
upsAdvanceControlUpsOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAdvanceControlUpsOff.setStatus("mandatory")


class _UpsAdvanceControlRebootUps_Type(Integer32):
    """Custom type upsAdvanceControlRebootUps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noRebootUps", 1),
          ("rebootUps", 2))
    )


_UpsAdvanceControlRebootUps_Type.__name__ = "Integer32"
_UpsAdvanceControlRebootUps_Object = MibScalar
upsAdvanceControlRebootUps = _UpsAdvanceControlRebootUps_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 6, 2, 2),
    _UpsAdvanceControlRebootUps_Type()
)
upsAdvanceControlRebootUps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAdvanceControlRebootUps.setStatus("mandatory")


class _UpsAdvanceControlUpsSleep_Type(Integer32):
    """Custom type upsAdvanceControlUpsSleep based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noPutUpsToSleep", 1),
          ("putUpsToSleep", 2),
          ("putUpsToSleepGracefully", 3))
    )


_UpsAdvanceControlUpsSleep_Type.__name__ = "Integer32"
_UpsAdvanceControlUpsSleep_Object = MibScalar
upsAdvanceControlUpsSleep = _UpsAdvanceControlUpsSleep_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 6, 2, 3),
    _UpsAdvanceControlUpsSleep_Type()
)
upsAdvanceControlUpsSleep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAdvanceControlUpsSleep.setStatus("mandatory")


class _UpsAdvanceControlSimulatePowerFail_Type(Integer32):
    """Custom type upsAdvanceControlSimulatePowerFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noSimulatePowerFailure", 1),
          ("simulatePowerFailure", 2))
    )


_UpsAdvanceControlSimulatePowerFail_Type.__name__ = "Integer32"
_UpsAdvanceControlSimulatePowerFail_Object = MibScalar
upsAdvanceControlSimulatePowerFail = _UpsAdvanceControlSimulatePowerFail_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 6, 2, 4),
    _UpsAdvanceControlSimulatePowerFail_Type()
)
upsAdvanceControlSimulatePowerFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAdvanceControlSimulatePowerFail.setStatus("mandatory")


class _UpsAdvanceControlFlashAndBeep_Type(Integer32):
    """Custom type upsAdvanceControlFlashAndBeep based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noFlashAndBeep", 1),
          ("flashAndBeep", 2))
    )


_UpsAdvanceControlFlashAndBeep_Type.__name__ = "Integer32"
_UpsAdvanceControlFlashAndBeep_Object = MibScalar
upsAdvanceControlFlashAndBeep = _UpsAdvanceControlFlashAndBeep_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 6, 2, 5),
    _UpsAdvanceControlFlashAndBeep_Type()
)
upsAdvanceControlFlashAndBeep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAdvanceControlFlashAndBeep.setStatus("mandatory")


class _UpsAdvanceControlTurnOnUPS_Type(Integer32):
    """Custom type upsAdvanceControlTurnOnUPS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noTurnOnUPS", 1),
          ("turnOnUPS", 2))
    )


_UpsAdvanceControlTurnOnUPS_Type.__name__ = "Integer32"
_UpsAdvanceControlTurnOnUPS_Object = MibScalar
upsAdvanceControlTurnOnUPS = _UpsAdvanceControlTurnOnUPS_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 6, 2, 6),
    _UpsAdvanceControlTurnOnUPS_Type()
)
upsAdvanceControlTurnOnUPS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAdvanceControlTurnOnUPS.setStatus("mandatory")


class _UpsAdvanceSleepAfterDelay_Type(Integer32):
    """Custom type upsAdvanceSleepAfterDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 600),
    )


_UpsAdvanceSleepAfterDelay_Type.__name__ = "Integer32"
_UpsAdvanceSleepAfterDelay_Object = MibScalar
upsAdvanceSleepAfterDelay = _UpsAdvanceSleepAfterDelay_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 6, 2, 7),
    _UpsAdvanceSleepAfterDelay_Type()
)
upsAdvanceSleepAfterDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAdvanceSleepAfterDelay.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsAdvanceSleepAfterDelay.setUnits("seconds")
_UpsTest_ObjectIdentity = ObjectIdentity
upsTest = _UpsTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 7)
)
_UpsBaseTest_ObjectIdentity = ObjectIdentity
upsBaseTest = _UpsBaseTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 7, 1)
)
_UpsAdvanceTest_ObjectIdentity = ObjectIdentity
upsAdvanceTest = _UpsAdvanceTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 7, 2)
)


class _UpsAdvanceTestDiagnosticSchedule_Type(Integer32):
    """Custom type upsAdvanceTestDiagnosticSchedule based on Integer32"""
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
        *(("unknown", 1),
          ("biweekly", 2),
          ("weekly", 3),
          ("atTurnOn", 4),
          ("never", 5))
    )


_UpsAdvanceTestDiagnosticSchedule_Type.__name__ = "Integer32"
_UpsAdvanceTestDiagnosticSchedule_Object = MibScalar
upsAdvanceTestDiagnosticSchedule = _UpsAdvanceTestDiagnosticSchedule_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 7, 2, 1),
    _UpsAdvanceTestDiagnosticSchedule_Type()
)
upsAdvanceTestDiagnosticSchedule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAdvanceTestDiagnosticSchedule.setStatus("mandatory")


class _UpsAdvanceTestDiagnostics_Type(Integer32):
    """Custom type upsAdvanceTestDiagnostics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noTestDiagnostics", 1),
          ("testDiagnostics", 2))
    )


_UpsAdvanceTestDiagnostics_Type.__name__ = "Integer32"
_UpsAdvanceTestDiagnostics_Object = MibScalar
upsAdvanceTestDiagnostics = _UpsAdvanceTestDiagnostics_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 7, 2, 2),
    _UpsAdvanceTestDiagnostics_Type()
)
upsAdvanceTestDiagnostics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAdvanceTestDiagnostics.setStatus("mandatory")


class _UpsAdvanceTestDiagnosticsResults_Type(Integer32):
    """Custom type upsAdvanceTestDiagnosticsResults based on Integer32"""
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
        *(("ok", 1),
          ("failed", 2),
          ("invalidTest", 3),
          ("testInProgress", 4))
    )


_UpsAdvanceTestDiagnosticsResults_Type.__name__ = "Integer32"
_UpsAdvanceTestDiagnosticsResults_Object = MibScalar
upsAdvanceTestDiagnosticsResults = _UpsAdvanceTestDiagnosticsResults_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 7, 2, 3),
    _UpsAdvanceTestDiagnosticsResults_Type()
)
upsAdvanceTestDiagnosticsResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAdvanceTestDiagnosticsResults.setStatus("mandatory")
_UpsAdvanceTestLastDiagnosticsDate_Type = DisplayString
_UpsAdvanceTestLastDiagnosticsDate_Object = MibScalar
upsAdvanceTestLastDiagnosticsDate = _UpsAdvanceTestLastDiagnosticsDate_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 7, 2, 4),
    _UpsAdvanceTestLastDiagnosticsDate_Type()
)
upsAdvanceTestLastDiagnosticsDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAdvanceTestLastDiagnosticsDate.setStatus("mandatory")


class _UpsAdvanceTestIndicators_Type(Integer32):
    """Custom type upsAdvanceTestIndicators based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noTestIndicators", 1),
          ("testIndicators", 2))
    )


_UpsAdvanceTestIndicators_Type.__name__ = "Integer32"
_UpsAdvanceTestIndicators_Object = MibScalar
upsAdvanceTestIndicators = _UpsAdvanceTestIndicators_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 7, 2, 5),
    _UpsAdvanceTestIndicators_Type()
)
upsAdvanceTestIndicators.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAdvanceTestIndicators.setStatus("mandatory")


class _UpsAdvanceTestRuntimeEstimation_Type(Integer32):
    """Custom type upsAdvanceTestRuntimeEstimation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noPerformEstimation", 1),
          ("performEstimation", 2),
          ("cancelCurrentEstimation", 3))
    )


_UpsAdvanceTestRuntimeEstimation_Type.__name__ = "Integer32"
_UpsAdvanceTestRuntimeEstimation_Object = MibScalar
upsAdvanceTestRuntimeEstimation = _UpsAdvanceTestRuntimeEstimation_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 7, 2, 6),
    _UpsAdvanceTestRuntimeEstimation_Type()
)
upsAdvanceTestRuntimeEstimation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAdvanceTestRuntimeEstimation.setStatus("mandatory")


class _UpsAdvanceTestEstimationResults_Type(Integer32):
    """Custom type upsAdvanceTestEstimationResults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("invalidEstimation", 2),
          ("estimationInProgress", 3))
    )


_UpsAdvanceTestEstimationResults_Type.__name__ = "Integer32"
_UpsAdvanceTestEstimationResults_Object = MibScalar
upsAdvanceTestEstimationResults = _UpsAdvanceTestEstimationResults_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 7, 2, 7),
    _UpsAdvanceTestEstimationResults_Type()
)
upsAdvanceTestEstimationResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAdvanceTestEstimationResults.setStatus("mandatory")
_UpsAdvanceTestEstimationDate_Type = DisplayString
_UpsAdvanceTestEstimationDate_Object = MibScalar
upsAdvanceTestEstimationDate = _UpsAdvanceTestEstimationDate_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 7, 2, 8),
    _UpsAdvanceTestEstimationDate_Type()
)
upsAdvanceTestEstimationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAdvanceTestEstimationDate.setStatus("mandatory")
_UpsOutlet_ObjectIdentity = ObjectIdentity
upsOutlet = _UpsOutlet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 8)
)
_UpsBankOutletControl_ObjectIdentity = ObjectIdentity
upsBankOutletControl = _UpsBankOutletControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 8, 1)
)
_UpsBankOutletControlTable_Object = MibTable
upsBankOutletControlTable = _UpsBankOutletControlTable_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 8, 1, 1)
)
if mibBuilder.loadTexts:
    upsBankOutletControlTable.setStatus("mandatory")
_UpsBankOutletControlEntry_Object = MibTableRow
upsBankOutletControlEntry = _UpsBankOutletControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 8, 1, 1, 1)
)
upsBankOutletControlEntry.setIndexNames(
    (0, "CPS-MIB", "upsBankControlIndex"),
)
if mibBuilder.loadTexts:
    upsBankOutletControlEntry.setStatus("mandatory")


class _UpsBankControlIndex_Type(Integer32):
    """Custom type upsBankControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_UpsBankControlIndex_Type.__name__ = "Integer32"
_UpsBankControlIndex_Object = MibTableColumn
upsBankControlIndex = _UpsBankControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 8, 1, 1, 1, 1),
    _UpsBankControlIndex_Type()
)
upsBankControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBankControlIndex.setStatus("mandatory")


class _UpsBankControlOutletCommand_Type(Integer32):
    """Custom type upsBankControlOutletCommand based on Integer32"""
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
        *(("immediateOn", 1),
          ("immediateOff", 2),
          ("bankNotExist", 3),
          ("criticalBank", 4))
    )


_UpsBankControlOutletCommand_Type.__name__ = "Integer32"
_UpsBankControlOutletCommand_Object = MibTableColumn
upsBankControlOutletCommand = _UpsBankControlOutletCommand_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 8, 1, 1, 1, 2),
    _UpsBankControlOutletCommand_Type()
)
upsBankControlOutletCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsBankControlOutletCommand.setStatus("mandatory")
_UpsPhase_ObjectIdentity = ObjectIdentity
upsPhase = _UpsPhase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 9)
)
_UpsPhaseInput_ObjectIdentity = ObjectIdentity
upsPhaseInput = _UpsPhaseInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 9, 1)
)
_UpsPhaseInputTableSize_Type = Integer32
_UpsPhaseInputTableSize_Object = MibScalar
upsPhaseInputTableSize = _UpsPhaseInputTableSize_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 9, 1, 1),
    _UpsPhaseInputTableSize_Type()
)
upsPhaseInputTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsPhaseInputTableSize.setStatus("mandatory")
_UpsPhaseInputTable_Object = MibTable
upsPhaseInputTable = _UpsPhaseInputTable_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 9, 1, 2)
)
if mibBuilder.loadTexts:
    upsPhaseInputTable.setStatus("mandatory")
_UpsPhaseInputEntry_Object = MibTableRow
upsPhaseInputEntry = _UpsPhaseInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 9, 1, 2, 1)
)
upsPhaseInputEntry.setIndexNames(
    (0, "CPS-MIB", "upsPhaseInputTableIndex"),
)
if mibBuilder.loadTexts:
    upsPhaseInputEntry.setStatus("mandatory")


class _UpsPhaseInputTableIndex_Type(Integer32):
    """Custom type upsPhaseInputTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 3),
    )


_UpsPhaseInputTableIndex_Type.__name__ = "Integer32"
_UpsPhaseInputTableIndex_Object = MibTableColumn
upsPhaseInputTableIndex = _UpsPhaseInputTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 9, 1, 2, 1, 1),
    _UpsPhaseInputTableIndex_Type()
)
upsPhaseInputTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsPhaseInputTableIndex.setStatus("mandatory")
_UpsPhaseInputVoltage_Type = Integer32
_UpsPhaseInputVoltage_Object = MibTableColumn
upsPhaseInputVoltage = _UpsPhaseInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 9, 1, 2, 1, 2),
    _UpsPhaseInputVoltage_Type()
)
upsPhaseInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsPhaseInputVoltage.setStatus("mandatory")
_UpsPhaseInputCurrent_Type = Integer32
_UpsPhaseInputCurrent_Object = MibTableColumn
upsPhaseInputCurrent = _UpsPhaseInputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 9, 1, 2, 1, 3),
    _UpsPhaseInputCurrent_Type()
)
upsPhaseInputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsPhaseInputCurrent.setStatus("mandatory")
_UpsPhaseInputFrequency_Type = Integer32
_UpsPhaseInputFrequency_Object = MibTableColumn
upsPhaseInputFrequency = _UpsPhaseInputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 9, 1, 2, 1, 4),
    _UpsPhaseInputFrequency_Type()
)
upsPhaseInputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsPhaseInputFrequency.setStatus("mandatory")
_UpsPhaseInputPowerFactor_Type = Integer32
_UpsPhaseInputPowerFactor_Object = MibTableColumn
upsPhaseInputPowerFactor = _UpsPhaseInputPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 9, 1, 2, 1, 5),
    _UpsPhaseInputPowerFactor_Type()
)
upsPhaseInputPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsPhaseInputPowerFactor.setStatus("mandatory")
_UpsPhaseOutput_ObjectIdentity = ObjectIdentity
upsPhaseOutput = _UpsPhaseOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 9, 2)
)
_UpsPhaseOutputTableSize_Type = Integer32
_UpsPhaseOutputTableSize_Object = MibScalar
upsPhaseOutputTableSize = _UpsPhaseOutputTableSize_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 9, 2, 1),
    _UpsPhaseOutputTableSize_Type()
)
upsPhaseOutputTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsPhaseOutputTableSize.setStatus("mandatory")
_UpsPhaseOutputTable_Object = MibTable
upsPhaseOutputTable = _UpsPhaseOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 9, 2, 2)
)
if mibBuilder.loadTexts:
    upsPhaseOutputTable.setStatus("mandatory")
_UpsPhaseOutputEntry_Object = MibTableRow
upsPhaseOutputEntry = _UpsPhaseOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 9, 2, 2, 1)
)
upsPhaseOutputEntry.setIndexNames(
    (0, "CPS-MIB", "upsPhaseOutputTableIndex"),
)
if mibBuilder.loadTexts:
    upsPhaseOutputEntry.setStatus("mandatory")


class _UpsPhaseOutputTableIndex_Type(Integer32):
    """Custom type upsPhaseOutputTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 3),
    )


_UpsPhaseOutputTableIndex_Type.__name__ = "Integer32"
_UpsPhaseOutputTableIndex_Object = MibTableColumn
upsPhaseOutputTableIndex = _UpsPhaseOutputTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 9, 2, 2, 1, 1),
    _UpsPhaseOutputTableIndex_Type()
)
upsPhaseOutputTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsPhaseOutputTableIndex.setStatus("mandatory")
_UpsPhaseOutputVoltage_Type = Integer32
_UpsPhaseOutputVoltage_Object = MibTableColumn
upsPhaseOutputVoltage = _UpsPhaseOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 9, 2, 2, 1, 2),
    _UpsPhaseOutputVoltage_Type()
)
upsPhaseOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsPhaseOutputVoltage.setStatus("mandatory")
_UpsPhaseOutputCurrent_Type = Integer32
_UpsPhaseOutputCurrent_Object = MibTableColumn
upsPhaseOutputCurrent = _UpsPhaseOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 9, 2, 2, 1, 3),
    _UpsPhaseOutputCurrent_Type()
)
upsPhaseOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsPhaseOutputCurrent.setStatus("mandatory")
_UpsPhaseOutputFrequency_Type = Integer32
_UpsPhaseOutputFrequency_Object = MibTableColumn
upsPhaseOutputFrequency = _UpsPhaseOutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 9, 2, 2, 1, 4),
    _UpsPhaseOutputFrequency_Type()
)
upsPhaseOutputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsPhaseOutputFrequency.setStatus("mandatory")
_UpsPhaseOutputPowerFactor_Type = Integer32
_UpsPhaseOutputPowerFactor_Object = MibTableColumn
upsPhaseOutputPowerFactor = _UpsPhaseOutputPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 9, 2, 2, 1, 5),
    _UpsPhaseOutputPowerFactor_Type()
)
upsPhaseOutputPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsPhaseOutputPowerFactor.setStatus("mandatory")
_UpsPhaseOutputPower_Type = Integer32
_UpsPhaseOutputPower_Object = MibTableColumn
upsPhaseOutputPower = _UpsPhaseOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 9, 2, 2, 1, 6),
    _UpsPhaseOutputPower_Type()
)
upsPhaseOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsPhaseOutputPower.setStatus("mandatory")
_UpsPhaseBypass_ObjectIdentity = ObjectIdentity
upsPhaseBypass = _UpsPhaseBypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 9, 3)
)
_UpsPhaseBypassTableSize_Type = Integer32
_UpsPhaseBypassTableSize_Object = MibScalar
upsPhaseBypassTableSize = _UpsPhaseBypassTableSize_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 9, 3, 1),
    _UpsPhaseBypassTableSize_Type()
)
upsPhaseBypassTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsPhaseBypassTableSize.setStatus("mandatory")
_UpsPhaseBypassTable_Object = MibTable
upsPhaseBypassTable = _UpsPhaseBypassTable_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 9, 3, 2)
)
if mibBuilder.loadTexts:
    upsPhaseBypassTable.setStatus("mandatory")
_UpsPhaseBypassEntry_Object = MibTableRow
upsPhaseBypassEntry = _UpsPhaseBypassEntry_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 9, 3, 2, 1)
)
upsPhaseBypassEntry.setIndexNames(
    (0, "CPS-MIB", "upsPhaseBypassTableIndex"),
)
if mibBuilder.loadTexts:
    upsPhaseBypassEntry.setStatus("mandatory")


class _UpsPhaseBypassTableIndex_Type(Integer32):
    """Custom type upsPhaseBypassTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 3),
    )


_UpsPhaseBypassTableIndex_Type.__name__ = "Integer32"
_UpsPhaseBypassTableIndex_Object = MibTableColumn
upsPhaseBypassTableIndex = _UpsPhaseBypassTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 9, 3, 2, 1, 1),
    _UpsPhaseBypassTableIndex_Type()
)
upsPhaseBypassTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsPhaseBypassTableIndex.setStatus("mandatory")
_UpsPhaseBypassVoltage_Type = Integer32
_UpsPhaseBypassVoltage_Object = MibTableColumn
upsPhaseBypassVoltage = _UpsPhaseBypassVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 9, 3, 2, 1, 2),
    _UpsPhaseBypassVoltage_Type()
)
upsPhaseBypassVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsPhaseBypassVoltage.setStatus("mandatory")
_UpsPhaseBypassCurrent_Type = Integer32
_UpsPhaseBypassCurrent_Object = MibTableColumn
upsPhaseBypassCurrent = _UpsPhaseBypassCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 9, 3, 2, 1, 3),
    _UpsPhaseBypassCurrent_Type()
)
upsPhaseBypassCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsPhaseBypassCurrent.setStatus("mandatory")
_UpsPhaseBypassFrequency_Type = Integer32
_UpsPhaseBypassFrequency_Object = MibTableColumn
upsPhaseBypassFrequency = _UpsPhaseBypassFrequency_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 9, 3, 2, 1, 4),
    _UpsPhaseBypassFrequency_Type()
)
upsPhaseBypassFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsPhaseBypassFrequency.setStatus("mandatory")
_UpsPhaseBypassPowerFactor_Type = Integer32
_UpsPhaseBypassPowerFactor_Object = MibTableColumn
upsPhaseBypassPowerFactor = _UpsPhaseBypassPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 9, 3, 2, 1, 5),
    _UpsPhaseBypassPowerFactor_Type()
)
upsPhaseBypassPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsPhaseBypassPowerFactor.setStatus("mandatory")
_UpsSystem_ObjectIdentity = ObjectIdentity
upsSystem = _UpsSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 10)
)


class _UpsStatus_Type(Integer32):
    """Custom type upsStatus based on Integer32"""
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
          ("overheat", 2),
          ("hardwarefault", 3))
    )


_UpsStatus_Type.__name__ = "Integer32"
_UpsStatus_Object = MibScalar
upsStatus = _UpsStatus_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 1, 10, 1),
    _UpsStatus_Type()
)
upsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsStatus.setStatus("mandatory")
_Eswitch_ObjectIdentity = ObjectIdentity
eswitch = _Eswitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 2)
)
_ESwitchIdent_ObjectIdentity = ObjectIdentity
eSwitchIdent = _ESwitchIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 2, 1)
)
_ESwitchIdentHardwareRev_Type = DisplayString
_ESwitchIdentHardwareRev_Object = MibScalar
eSwitchIdentHardwareRev = _ESwitchIdentHardwareRev_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 2, 1, 1),
    _ESwitchIdentHardwareRev_Type()
)
eSwitchIdentHardwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSwitchIdentHardwareRev.setStatus("mandatory")
_ESwitchIdentFirmwareRev_Type = DisplayString
_ESwitchIdentFirmwareRev_Object = MibScalar
eSwitchIdentFirmwareRev = _ESwitchIdentFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 2, 1, 2),
    _ESwitchIdentFirmwareRev_Type()
)
eSwitchIdentFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSwitchIdentFirmwareRev.setStatus("mandatory")
_ESwitchIdentDateOfManufacture_Type = DisplayString
_ESwitchIdentDateOfManufacture_Object = MibScalar
eSwitchIdentDateOfManufacture = _ESwitchIdentDateOfManufacture_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 2, 1, 3),
    _ESwitchIdentDateOfManufacture_Type()
)
eSwitchIdentDateOfManufacture.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSwitchIdentDateOfManufacture.setStatus("mandatory")
_ESwitchIdentModelName_Type = DisplayString
_ESwitchIdentModelName_Object = MibScalar
eSwitchIdentModelName = _ESwitchIdentModelName_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 2, 1, 4),
    _ESwitchIdentModelName_Type()
)
eSwitchIdentModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSwitchIdentModelName.setStatus("mandatory")
_ESwitchBase_ObjectIdentity = ObjectIdentity
eSwitchBase = _ESwitchBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 2, 2)
)
_ESwitchNumber_Type = Integer32
_ESwitchNumber_Object = MibScalar
eSwitchNumber = _ESwitchNumber_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 2, 2, 1),
    _ESwitchNumber_Type()
)
eSwitchNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSwitchNumber.setStatus("mandatory")
_ESwitchBaseTable_Object = MibTable
eSwitchBaseTable = _ESwitchBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    eSwitchBaseTable.setStatus("mandatory")
_ESwitchBaseEntry_Object = MibTableRow
eSwitchBaseEntry = _ESwitchBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 2, 2, 2, 1)
)
eSwitchBaseEntry.setIndexNames(
    (0, "CPS-MIB", "eSwitchID"),
)
if mibBuilder.loadTexts:
    eSwitchBaseEntry.setStatus("mandatory")


class _ESwitchID_Type(Integer32):
    """Custom type eSwitchID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_ESwitchID_Type.__name__ = "Integer32"
_ESwitchID_Object = MibTableColumn
eSwitchID = _ESwitchID_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 2, 2, 2, 1, 1),
    _ESwitchID_Type()
)
eSwitchID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSwitchID.setStatus("mandatory")
_ESwitchOutletNum_Type = Integer32
_ESwitchOutletNum_Object = MibTableColumn
eSwitchOutletNum = _ESwitchOutletNum_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 2, 2, 2, 1, 2),
    _ESwitchOutletNum_Type()
)
eSwitchOutletNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSwitchOutletNum.setStatus("mandatory")
_ESwitchOutletState_Type = DisplayString
_ESwitchOutletState_Object = MibTableColumn
eSwitchOutletState = _ESwitchOutletState_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 2, 2, 2, 1, 3),
    _ESwitchOutletState_Type()
)
eSwitchOutletState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSwitchOutletState.setStatus("mandatory")
_ESwitchBaseCtrTable_Object = MibTable
eSwitchBaseCtrTable = _ESwitchBaseCtrTable_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    eSwitchBaseCtrTable.setStatus("mandatory")
_ESwitchBaseCtrEntry_Object = MibTableRow
eSwitchBaseCtrEntry = _ESwitchBaseCtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 2, 2, 3, 1)
)
eSwitchBaseCtrEntry.setIndexNames(
    (0, "CPS-MIB", "eSwitchCtrID"),
)
if mibBuilder.loadTexts:
    eSwitchBaseCtrEntry.setStatus("mandatory")


class _ESwitchCtrID_Type(Integer32):
    """Custom type eSwitchCtrID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_ESwitchCtrID_Type.__name__ = "Integer32"
_ESwitchCtrID_Object = MibTableColumn
eSwitchCtrID = _ESwitchCtrID_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 2, 2, 3, 1, 1),
    _ESwitchCtrID_Type()
)
eSwitchCtrID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSwitchCtrID.setStatus("mandatory")
_ESwitchActOutlet_Type = Integer32
_ESwitchActOutlet_Object = MibTableColumn
eSwitchActOutlet = _ESwitchActOutlet_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 2, 2, 3, 1, 2),
    _ESwitchActOutlet_Type()
)
eSwitchActOutlet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSwitchActOutlet.setStatus("mandatory")
_ESwitchActType_Type = Integer32
_ESwitchActType_Object = MibTableColumn
eSwitchActType = _ESwitchActType_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 2, 2, 3, 1, 3),
    _ESwitchActType_Type()
)
eSwitchActType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSwitchActType.setStatus("mandatory")
_EPDU_ObjectIdentity = ObjectIdentity
ePDU = _EPDU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3)
)
_EPDUIdent_ObjectIdentity = ObjectIdentity
ePDUIdent = _EPDUIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 1)
)
_EPDUIdentName_Type = DisplayString
_EPDUIdentName_Object = MibScalar
ePDUIdentName = _EPDUIdentName_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 1, 1),
    _EPDUIdentName_Type()
)
ePDUIdentName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDUIdentName.setStatus("mandatory")
_EPDUIdentHardwareRev_Type = DisplayString
_EPDUIdentHardwareRev_Object = MibScalar
ePDUIdentHardwareRev = _EPDUIdentHardwareRev_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 1, 2),
    _EPDUIdentHardwareRev_Type()
)
ePDUIdentHardwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDUIdentHardwareRev.setStatus("mandatory")
_EPDUIdentFirmwareRev_Type = DisplayString
_EPDUIdentFirmwareRev_Object = MibScalar
ePDUIdentFirmwareRev = _EPDUIdentFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 1, 3),
    _EPDUIdentFirmwareRev_Type()
)
ePDUIdentFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDUIdentFirmwareRev.setStatus("mandatory")
_EPDUIdentDateOfManufacture_Type = DisplayString
_EPDUIdentDateOfManufacture_Object = MibScalar
ePDUIdentDateOfManufacture = _EPDUIdentDateOfManufacture_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 1, 4),
    _EPDUIdentDateOfManufacture_Type()
)
ePDUIdentDateOfManufacture.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDUIdentDateOfManufacture.setStatus("mandatory")
_EPDUIdentModelNumber_Type = DisplayString
_EPDUIdentModelNumber_Object = MibScalar
ePDUIdentModelNumber = _EPDUIdentModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 1, 5),
    _EPDUIdentModelNumber_Type()
)
ePDUIdentModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDUIdentModelNumber.setStatus("mandatory")
_EPDUIdentSerialNumber_Type = DisplayString
_EPDUIdentSerialNumber_Object = MibScalar
ePDUIdentSerialNumber = _EPDUIdentSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 1, 6),
    _EPDUIdentSerialNumber_Type()
)
ePDUIdentSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDUIdentSerialNumber.setStatus("mandatory")
_EPDUIdentDeviceRating_Type = Integer32
_EPDUIdentDeviceRating_Object = MibScalar
ePDUIdentDeviceRating = _EPDUIdentDeviceRating_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 1, 7),
    _EPDUIdentDeviceRating_Type()
)
ePDUIdentDeviceRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDUIdentDeviceRating.setStatus("mandatory")
_EPDUIdentDeviceNumOutlets_Type = Integer32
_EPDUIdentDeviceNumOutlets_Object = MibScalar
ePDUIdentDeviceNumOutlets = _EPDUIdentDeviceNumOutlets_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 1, 8),
    _EPDUIdentDeviceNumOutlets_Type()
)
ePDUIdentDeviceNumOutlets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDUIdentDeviceNumOutlets.setStatus("mandatory")
_EPDUIdentDeviceNumPhases_Type = Integer32
_EPDUIdentDeviceNumPhases_Object = MibScalar
ePDUIdentDeviceNumPhases = _EPDUIdentDeviceNumPhases_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 1, 9),
    _EPDUIdentDeviceNumPhases_Type()
)
ePDUIdentDeviceNumPhases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDUIdentDeviceNumPhases.setStatus("mandatory")
_EPDUIdentDeviceNumBreakers_Type = Integer32
_EPDUIdentDeviceNumBreakers_Object = MibScalar
ePDUIdentDeviceNumBreakers = _EPDUIdentDeviceNumBreakers_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 1, 10),
    _EPDUIdentDeviceNumBreakers_Type()
)
ePDUIdentDeviceNumBreakers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDUIdentDeviceNumBreakers.setStatus("mandatory")
_EPDUIdentDeviceBreakerRating_Type = Integer32
_EPDUIdentDeviceBreakerRating_Object = MibScalar
ePDUIdentDeviceBreakerRating = _EPDUIdentDeviceBreakerRating_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 1, 11),
    _EPDUIdentDeviceBreakerRating_Type()
)
ePDUIdentDeviceBreakerRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDUIdentDeviceBreakerRating.setStatus("mandatory")


class _EPDUIdentDeviceOrientation_Type(Integer32):
    """Custom type ePDUIdentDeviceOrientation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("orientHorizontal", 1),
          ("orientVertical", 2))
    )


_EPDUIdentDeviceOrientation_Type.__name__ = "Integer32"
_EPDUIdentDeviceOrientation_Object = MibScalar
ePDUIdentDeviceOrientation = _EPDUIdentDeviceOrientation_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 1, 12),
    _EPDUIdentDeviceOrientation_Type()
)
ePDUIdentDeviceOrientation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDUIdentDeviceOrientation.setStatus("mandatory")


class _EPDUIdentDeviceOutletLayout_Type(Integer32):
    """Custom type ePDUIdentDeviceOutletLayout based on Integer32"""
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
        *(("seqPhaseToNeutral", 1),
          ("seqPhaseToPhase", 2),
          ("seqPhToNeu21PhToPh", 3),
          ("seqPhToPhGrouped", 4))
    )


_EPDUIdentDeviceOutletLayout_Type.__name__ = "Integer32"
_EPDUIdentDeviceOutletLayout_Object = MibScalar
ePDUIdentDeviceOutletLayout = _EPDUIdentDeviceOutletLayout_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 1, 13),
    _EPDUIdentDeviceOutletLayout_Type()
)
ePDUIdentDeviceOutletLayout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDUIdentDeviceOutletLayout.setStatus("mandatory")


class _EPDUIdentDeviceDisplayOrientation_Type(Integer32):
    """Custom type ePDUIdentDeviceDisplayOrientation based on Integer32"""
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
        *(("displayNormal", 1),
          ("displayReverse", 2),
          ("displayRotate90", 3),
          ("displayRotate270", 4),
          ("displayAuto", 5))
    )


_EPDUIdentDeviceDisplayOrientation_Type.__name__ = "Integer32"
_EPDUIdentDeviceDisplayOrientation_Object = MibScalar
ePDUIdentDeviceDisplayOrientation = _EPDUIdentDeviceDisplayOrientation_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 1, 14),
    _EPDUIdentDeviceDisplayOrientation_Type()
)
ePDUIdentDeviceDisplayOrientation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDUIdentDeviceDisplayOrientation.setStatus("mandatory")
_EPDUIdentDeviceLinetoLineVoltage_Type = Integer32
_EPDUIdentDeviceLinetoLineVoltage_Object = MibScalar
ePDUIdentDeviceLinetoLineVoltage = _EPDUIdentDeviceLinetoLineVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 1, 15),
    _EPDUIdentDeviceLinetoLineVoltage_Type()
)
ePDUIdentDeviceLinetoLineVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDUIdentDeviceLinetoLineVoltage.setStatus("mandatory")


class _EPDUIdentIndicator_Type(Integer32):
    """Custom type ePDUIdentIndicator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noTestIndicators", 1),
          ("testIndicators", 2))
    )


_EPDUIdentIndicator_Type.__name__ = "Integer32"
_EPDUIdentIndicator_Object = MibScalar
ePDUIdentIndicator = _EPDUIdentIndicator_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 1, 16),
    _EPDUIdentIndicator_Type()
)
ePDUIdentIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDUIdentIndicator.setStatus("mandatory")
_EPDULoad_ObjectIdentity = ObjectIdentity
ePDULoad = _EPDULoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 2)
)
_EPDULoadDevice_ObjectIdentity = ObjectIdentity
ePDULoadDevice = _EPDULoadDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 2, 1)
)
_EPDULoadDevMaxPhaseLoad_Type = Integer32
_EPDULoadDevMaxPhaseLoad_Object = MibScalar
ePDULoadDevMaxPhaseLoad = _EPDULoadDevMaxPhaseLoad_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 2, 1, 1),
    _EPDULoadDevMaxPhaseLoad_Type()
)
ePDULoadDevMaxPhaseLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDULoadDevMaxPhaseLoad.setStatus("mandatory")
_EPDULoadDevNumPhases_Type = Integer32
_EPDULoadDevNumPhases_Object = MibScalar
ePDULoadDevNumPhases = _EPDULoadDevNumPhases_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 2, 1, 2),
    _EPDULoadDevNumPhases_Type()
)
ePDULoadDevNumPhases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDULoadDevNumPhases.setStatus("mandatory")
_EPDULoadDevMaxBankLoad_Type = Integer32
_EPDULoadDevMaxBankLoad_Object = MibScalar
ePDULoadDevMaxBankLoad = _EPDULoadDevMaxBankLoad_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 2, 1, 3),
    _EPDULoadDevMaxBankLoad_Type()
)
ePDULoadDevMaxBankLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDULoadDevMaxBankLoad.setStatus("mandatory")
_EPDULoadDevNumBanks_Type = Integer32
_EPDULoadDevNumBanks_Object = MibScalar
ePDULoadDevNumBanks = _EPDULoadDevNumBanks_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 2, 1, 4),
    _EPDULoadDevNumBanks_Type()
)
ePDULoadDevNumBanks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDULoadDevNumBanks.setStatus("mandatory")
_EPDULoadDevBankTableSize_Type = Integer32
_EPDULoadDevBankTableSize_Object = MibScalar
ePDULoadDevBankTableSize = _EPDULoadDevBankTableSize_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 2, 1, 5),
    _EPDULoadDevBankTableSize_Type()
)
ePDULoadDevBankTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDULoadDevBankTableSize.setStatus("mandatory")
_EPDULoadDevBankTable_Object = MibTable
ePDULoadDevBankTable = _EPDULoadDevBankTable_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 2, 1, 6)
)
if mibBuilder.loadTexts:
    ePDULoadDevBankTable.setStatus("mandatory")
_EPDULoadDevBankEntry_Object = MibTableRow
ePDULoadDevBankEntry = _EPDULoadDevBankEntry_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 2, 1, 6, 1)
)
ePDULoadDevBankEntry.setIndexNames(
    (0, "CPS-MIB", "ePDULoadDevBankIndex"),
)
if mibBuilder.loadTexts:
    ePDULoadDevBankEntry.setStatus("mandatory")


class _EPDULoadDevBankIndex_Type(Integer32):
    """Custom type ePDULoadDevBankIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_EPDULoadDevBankIndex_Type.__name__ = "Integer32"
_EPDULoadDevBankIndex_Object = MibTableColumn
ePDULoadDevBankIndex = _EPDULoadDevBankIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 2, 1, 6, 1, 1),
    _EPDULoadDevBankIndex_Type()
)
ePDULoadDevBankIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDULoadDevBankIndex.setStatus("mandatory")
_EPDULoadDevBankNumber_Type = Integer32
_EPDULoadDevBankNumber_Object = MibTableColumn
ePDULoadDevBankNumber = _EPDULoadDevBankNumber_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 2, 1, 6, 1, 2),
    _EPDULoadDevBankNumber_Type()
)
ePDULoadDevBankNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDULoadDevBankNumber.setStatus("mandatory")
_EPDULoadDevBankMaxLoad_Type = Integer32
_EPDULoadDevBankMaxLoad_Object = MibTableColumn
ePDULoadDevBankMaxLoad = _EPDULoadDevBankMaxLoad_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 2, 1, 6, 1, 3),
    _EPDULoadDevBankMaxLoad_Type()
)
ePDULoadDevBankMaxLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDULoadDevBankMaxLoad.setStatus("mandatory")
_EPDULoadDevMaxOutletTableSize_Type = Integer32
_EPDULoadDevMaxOutletTableSize_Object = MibScalar
ePDULoadDevMaxOutletTableSize = _EPDULoadDevMaxOutletTableSize_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 2, 1, 7),
    _EPDULoadDevMaxOutletTableSize_Type()
)
ePDULoadDevMaxOutletTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDULoadDevMaxOutletTableSize.setStatus("mandatory")
_EPDULoadDevMaxOutletTable_Object = MibTable
ePDULoadDevMaxOutletTable = _EPDULoadDevMaxOutletTable_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 2, 1, 8)
)
if mibBuilder.loadTexts:
    ePDULoadDevMaxOutletTable.setStatus("mandatory")
_EPDULoadDevMaxOutletEntry_Object = MibTableRow
ePDULoadDevMaxOutletEntry = _EPDULoadDevMaxOutletEntry_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 2, 1, 8, 1)
)
ePDULoadDevMaxOutletEntry.setIndexNames(
    (0, "CPS-MIB", "ePDULoadDevOutletIndex"),
)
if mibBuilder.loadTexts:
    ePDULoadDevMaxOutletEntry.setStatus("mandatory")


class _EPDULoadDevOutletIndex_Type(Integer32):
    """Custom type ePDULoadDevOutletIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_EPDULoadDevOutletIndex_Type.__name__ = "Integer32"
_EPDULoadDevOutletIndex_Object = MibTableColumn
ePDULoadDevOutletIndex = _EPDULoadDevOutletIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 2, 1, 8, 1, 1),
    _EPDULoadDevOutletIndex_Type()
)
ePDULoadDevOutletIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDULoadDevOutletIndex.setStatus("mandatory")
_EPDULoadDevOutletNumber_Type = Integer32
_EPDULoadDevOutletNumber_Object = MibTableColumn
ePDULoadDevOutletNumber = _EPDULoadDevOutletNumber_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 2, 1, 8, 1, 2),
    _EPDULoadDevOutletNumber_Type()
)
ePDULoadDevOutletNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDULoadDevOutletNumber.setStatus("mandatory")
_EPDULoadDevMaxOutletLoad_Type = Integer32
_EPDULoadDevMaxOutletLoad_Object = MibTableColumn
ePDULoadDevMaxOutletLoad = _EPDULoadDevMaxOutletLoad_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 2, 1, 8, 1, 3),
    _EPDULoadDevMaxOutletLoad_Type()
)
ePDULoadDevMaxOutletLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDULoadDevMaxOutletLoad.setStatus("mandatory")
_EPDULoadPhaseConfig_ObjectIdentity = ObjectIdentity
ePDULoadPhaseConfig = _EPDULoadPhaseConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 2, 2)
)
_EPDULoadPhaseConfigTable_Object = MibTable
ePDULoadPhaseConfigTable = _EPDULoadPhaseConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ePDULoadPhaseConfigTable.setStatus("mandatory")
_EPDULoadPhaseConfigEntry_Object = MibTableRow
ePDULoadPhaseConfigEntry = _EPDULoadPhaseConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 2, 2, 1, 1)
)
ePDULoadPhaseConfigEntry.setIndexNames(
    (0, "CPS-MIB", "ePDULoadPhaseConfigIndex"),
)
if mibBuilder.loadTexts:
    ePDULoadPhaseConfigEntry.setStatus("mandatory")


class _EPDULoadPhaseConfigIndex_Type(Integer32):
    """Custom type ePDULoadPhaseConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("phase1", 1),
          ("phase2", 2),
          ("phase3", 3))
    )


_EPDULoadPhaseConfigIndex_Type.__name__ = "Integer32"
_EPDULoadPhaseConfigIndex_Object = MibTableColumn
ePDULoadPhaseConfigIndex = _EPDULoadPhaseConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 2, 2, 1, 1, 1),
    _EPDULoadPhaseConfigIndex_Type()
)
ePDULoadPhaseConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDULoadPhaseConfigIndex.setStatus("mandatory")
_EPDULoadPhaseConfigLowLoadThreshold_Type = Integer32
_EPDULoadPhaseConfigLowLoadThreshold_Object = MibTableColumn
ePDULoadPhaseConfigLowLoadThreshold = _EPDULoadPhaseConfigLowLoadThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 2, 2, 1, 1, 2),
    _EPDULoadPhaseConfigLowLoadThreshold_Type()
)
ePDULoadPhaseConfigLowLoadThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDULoadPhaseConfigLowLoadThreshold.setStatus("mandatory")
_EPDULoadPhaseConfigNearOverloadThreshold_Type = Integer32
_EPDULoadPhaseConfigNearOverloadThreshold_Object = MibTableColumn
ePDULoadPhaseConfigNearOverloadThreshold = _EPDULoadPhaseConfigNearOverloadThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 2, 2, 1, 1, 3),
    _EPDULoadPhaseConfigNearOverloadThreshold_Type()
)
ePDULoadPhaseConfigNearOverloadThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDULoadPhaseConfigNearOverloadThreshold.setStatus("mandatory")
_EPDULoadPhaseConfigOverloadThreshold_Type = Integer32
_EPDULoadPhaseConfigOverloadThreshold_Object = MibTableColumn
ePDULoadPhaseConfigOverloadThreshold = _EPDULoadPhaseConfigOverloadThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 2, 2, 1, 1, 4),
    _EPDULoadPhaseConfigOverloadThreshold_Type()
)
ePDULoadPhaseConfigOverloadThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDULoadPhaseConfigOverloadThreshold.setStatus("mandatory")


class _EPDULoadPhaseConfigAlarm_Type(Integer32):
    """Custom type ePDULoadPhaseConfigAlarm based on Integer32"""
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
        *(("noLoadAlarm", 1),
          ("underCurrentAlarm", 2),
          ("nearOverCurrentAlarm", 3),
          ("overCurrentAlarm", 4))
    )


_EPDULoadPhaseConfigAlarm_Type.__name__ = "Integer32"
_EPDULoadPhaseConfigAlarm_Object = MibTableColumn
ePDULoadPhaseConfigAlarm = _EPDULoadPhaseConfigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 2, 2, 1, 1, 5),
    _EPDULoadPhaseConfigAlarm_Type()
)
ePDULoadPhaseConfigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDULoadPhaseConfigAlarm.setStatus("mandatory")
_EPDULoadStatus_ObjectIdentity = ObjectIdentity
ePDULoadStatus = _EPDULoadStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 2, 3)
)
_EPDULoadStatusTable_Object = MibTable
ePDULoadStatusTable = _EPDULoadStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 2, 3, 1)
)
if mibBuilder.loadTexts:
    ePDULoadStatusTable.setStatus("mandatory")
_EPDULoadStatusEntry_Object = MibTableRow
ePDULoadStatusEntry = _EPDULoadStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 2, 3, 1, 1)
)
ePDULoadStatusEntry.setIndexNames(
    (0, "CPS-MIB", "ePDULoadStatusIndex"),
)
if mibBuilder.loadTexts:
    ePDULoadStatusEntry.setStatus("mandatory")


class _EPDULoadStatusIndex_Type(Integer32):
    """Custom type ePDULoadStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_EPDULoadStatusIndex_Type.__name__ = "Integer32"
_EPDULoadStatusIndex_Object = MibTableColumn
ePDULoadStatusIndex = _EPDULoadStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 2, 3, 1, 1, 1),
    _EPDULoadStatusIndex_Type()
)
ePDULoadStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDULoadStatusIndex.setStatus("mandatory")
_EPDULoadStatusLoad_Type = Gauge32
_EPDULoadStatusLoad_Object = MibTableColumn
ePDULoadStatusLoad = _EPDULoadStatusLoad_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 2, 3, 1, 1, 2),
    _EPDULoadStatusLoad_Type()
)
ePDULoadStatusLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDULoadStatusLoad.setStatus("mandatory")


class _EPDULoadStatusLoadState_Type(Integer32):
    """Custom type ePDULoadStatusLoadState based on Integer32"""
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
        *(("loadNormal", 1),
          ("loadLow", 2),
          ("loadNearOverload", 3),
          ("loadOverload", 4))
    )


_EPDULoadStatusLoadState_Type.__name__ = "Integer32"
_EPDULoadStatusLoadState_Object = MibTableColumn
ePDULoadStatusLoadState = _EPDULoadStatusLoadState_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 2, 3, 1, 1, 3),
    _EPDULoadStatusLoadState_Type()
)
ePDULoadStatusLoadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDULoadStatusLoadState.setStatus("mandatory")
_EPDULoadStatusPhaseNumber_Type = Integer32
_EPDULoadStatusPhaseNumber_Object = MibTableColumn
ePDULoadStatusPhaseNumber = _EPDULoadStatusPhaseNumber_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 2, 3, 1, 1, 4),
    _EPDULoadStatusPhaseNumber_Type()
)
ePDULoadStatusPhaseNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDULoadStatusPhaseNumber.setStatus("mandatory")
_EPDULoadStatusBankNumber_Type = Integer32
_EPDULoadStatusBankNumber_Object = MibTableColumn
ePDULoadStatusBankNumber = _EPDULoadStatusBankNumber_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 2, 3, 1, 1, 5),
    _EPDULoadStatusBankNumber_Type()
)
ePDULoadStatusBankNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDULoadStatusBankNumber.setStatus("mandatory")
_EPDULoadStatusVoltage_Type = Integer32
_EPDULoadStatusVoltage_Object = MibTableColumn
ePDULoadStatusVoltage = _EPDULoadStatusVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 2, 3, 1, 1, 6),
    _EPDULoadStatusVoltage_Type()
)
ePDULoadStatusVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDULoadStatusVoltage.setStatus("mandatory")
_EPDULoadStatusActivePower_Type = Integer32
_EPDULoadStatusActivePower_Object = MibTableColumn
ePDULoadStatusActivePower = _EPDULoadStatusActivePower_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 2, 3, 1, 1, 7),
    _EPDULoadStatusActivePower_Type()
)
ePDULoadStatusActivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDULoadStatusActivePower.setStatus("mandatory")
_EPDULoadStatusApparentPower_Type = Integer32
_EPDULoadStatusApparentPower_Object = MibTableColumn
ePDULoadStatusApparentPower = _EPDULoadStatusApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 2, 3, 1, 1, 8),
    _EPDULoadStatusApparentPower_Type()
)
ePDULoadStatusApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDULoadStatusApparentPower.setStatus("mandatory")
_EPDULoadStatusPowerFactor_Type = Integer32
_EPDULoadStatusPowerFactor_Object = MibTableColumn
ePDULoadStatusPowerFactor = _EPDULoadStatusPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 2, 3, 1, 1, 9),
    _EPDULoadStatusPowerFactor_Type()
)
ePDULoadStatusPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDULoadStatusPowerFactor.setStatus("mandatory")
_EPDULoadStatusEnergy_Type = Integer32
_EPDULoadStatusEnergy_Object = MibTableColumn
ePDULoadStatusEnergy = _EPDULoadStatusEnergy_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 2, 3, 1, 1, 10),
    _EPDULoadStatusEnergy_Type()
)
ePDULoadStatusEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDULoadStatusEnergy.setStatus("mandatory")
_EPDULoadStatusEnergyStartTime_Type = DisplayString
_EPDULoadStatusEnergyStartTime_Object = MibTableColumn
ePDULoadStatusEnergyStartTime = _EPDULoadStatusEnergyStartTime_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 2, 3, 1, 1, 11),
    _EPDULoadStatusEnergyStartTime_Type()
)
ePDULoadStatusEnergyStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDULoadStatusEnergyStartTime.setStatus("mandatory")
_EPDULoadBankConfig_ObjectIdentity = ObjectIdentity
ePDULoadBankConfig = _EPDULoadBankConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 2, 4)
)
_EPDULoadBankConfigTable_Object = MibTable
ePDULoadBankConfigTable = _EPDULoadBankConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 2, 4, 1)
)
if mibBuilder.loadTexts:
    ePDULoadBankConfigTable.setStatus("mandatory")
_EPDULoadBankConfigEntry_Object = MibTableRow
ePDULoadBankConfigEntry = _EPDULoadBankConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 2, 4, 1, 1)
)
ePDULoadBankConfigEntry.setIndexNames(
    (0, "CPS-MIB", "ePDULoadBankConfigIndex"),
)
if mibBuilder.loadTexts:
    ePDULoadBankConfigEntry.setStatus("mandatory")


class _EPDULoadBankConfigIndex_Type(Integer32):
    """Custom type ePDULoadBankConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_EPDULoadBankConfigIndex_Type.__name__ = "Integer32"
_EPDULoadBankConfigIndex_Object = MibTableColumn
ePDULoadBankConfigIndex = _EPDULoadBankConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 2, 4, 1, 1, 1),
    _EPDULoadBankConfigIndex_Type()
)
ePDULoadBankConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDULoadBankConfigIndex.setStatus("mandatory")
_EPDULoadBankConfigLowLoadThreshold_Type = Integer32
_EPDULoadBankConfigLowLoadThreshold_Object = MibTableColumn
ePDULoadBankConfigLowLoadThreshold = _EPDULoadBankConfigLowLoadThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 2, 4, 1, 1, 2),
    _EPDULoadBankConfigLowLoadThreshold_Type()
)
ePDULoadBankConfigLowLoadThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDULoadBankConfigLowLoadThreshold.setStatus("mandatory")
_EPDULoadBankConfigNearOverloadThreshold_Type = Integer32
_EPDULoadBankConfigNearOverloadThreshold_Object = MibTableColumn
ePDULoadBankConfigNearOverloadThreshold = _EPDULoadBankConfigNearOverloadThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 2, 4, 1, 1, 3),
    _EPDULoadBankConfigNearOverloadThreshold_Type()
)
ePDULoadBankConfigNearOverloadThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDULoadBankConfigNearOverloadThreshold.setStatus("mandatory")
_EPDULoadBankConfigOverloadThreshold_Type = Integer32
_EPDULoadBankConfigOverloadThreshold_Object = MibTableColumn
ePDULoadBankConfigOverloadThreshold = _EPDULoadBankConfigOverloadThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 2, 4, 1, 1, 4),
    _EPDULoadBankConfigOverloadThreshold_Type()
)
ePDULoadBankConfigOverloadThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDULoadBankConfigOverloadThreshold.setStatus("mandatory")


class _EPDULoadBankConfigAlarm_Type(Integer32):
    """Custom type ePDULoadBankConfigAlarm based on Integer32"""
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
        *(("noLoadAlarm", 1),
          ("underCurrentAlarm", 2),
          ("nearOverCurrentAlarm", 3),
          ("overCurrentAlarm", 4))
    )


_EPDULoadBankConfigAlarm_Type.__name__ = "Integer32"
_EPDULoadBankConfigAlarm_Object = MibTableColumn
ePDULoadBankConfigAlarm = _EPDULoadBankConfigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 2, 4, 1, 1, 5),
    _EPDULoadBankConfigAlarm_Type()
)
ePDULoadBankConfigAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDULoadBankConfigAlarm.setStatus("mandatory")
_EPDUOutlet_ObjectIdentity = ObjectIdentity
ePDUOutlet = _EPDUOutlet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3)
)
_EPDUOutletDevice_ObjectIdentity = ObjectIdentity
ePDUOutletDevice = _EPDUOutletDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 1)
)


class _EPDUOutletDevCommand_Type(Integer32):
    """Custom type ePDUOutletDevCommand based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("noCommandAll", 1),
          ("immediateAllOn", 2),
          ("immediateAllOff", 3),
          ("immediateAllReboot", 4),
          ("delayedAllOn", 5),
          ("delayedAllOff", 6),
          ("delayedAllReboot", 7),
          ("cancelAllPendingCommands", 8))
    )


_EPDUOutletDevCommand_Type.__name__ = "Integer32"
_EPDUOutletDevCommand_Object = MibScalar
ePDUOutletDevCommand = _EPDUOutletDevCommand_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 1, 1),
    _EPDUOutletDevCommand_Type()
)
ePDUOutletDevCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDUOutletDevCommand.setStatus("mandatory")
_EPDUOutletDevColdstartDelay_Type = Integer32
_EPDUOutletDevColdstartDelay_Object = MibScalar
ePDUOutletDevColdstartDelay = _EPDUOutletDevColdstartDelay_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 1, 2),
    _EPDUOutletDevColdstartDelay_Type()
)
ePDUOutletDevColdstartDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDUOutletDevColdstartDelay.setStatus("mandatory")
_EPDUOutletDevNumCntrlOutlets_Type = Integer32
_EPDUOutletDevNumCntrlOutlets_Object = MibScalar
ePDUOutletDevNumCntrlOutlets = _EPDUOutletDevNumCntrlOutlets_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 1, 3),
    _EPDUOutletDevNumCntrlOutlets_Type()
)
ePDUOutletDevNumCntrlOutlets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDUOutletDevNumCntrlOutlets.setStatus("mandatory")
_EPDUOutletDevNumTotalOutlets_Type = Integer32
_EPDUOutletDevNumTotalOutlets_Object = MibScalar
ePDUOutletDevNumTotalOutlets = _EPDUOutletDevNumTotalOutlets_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 1, 4),
    _EPDUOutletDevNumTotalOutlets_Type()
)
ePDUOutletDevNumTotalOutlets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDUOutletDevNumTotalOutlets.setStatus("mandatory")
_EPDUOutletDevMonitoredOutlets_Type = Integer32
_EPDUOutletDevMonitoredOutlets_Object = MibScalar
ePDUOutletDevMonitoredOutlets = _EPDUOutletDevMonitoredOutlets_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 1, 5),
    _EPDUOutletDevMonitoredOutlets_Type()
)
ePDUOutletDevMonitoredOutlets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDUOutletDevMonitoredOutlets.setStatus("mandatory")


class _EPDUOutletDevColdstartState_Type(Integer32):
    """Custom type ePDUOutletDevColdstartState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allOn", 1),
          ("previous", 2))
    )


_EPDUOutletDevColdstartState_Type.__name__ = "Integer32"
_EPDUOutletDevColdstartState_Object = MibScalar
ePDUOutletDevColdstartState = _EPDUOutletDevColdstartState_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 1, 6),
    _EPDUOutletDevColdstartState_Type()
)
ePDUOutletDevColdstartState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDUOutletDevColdstartState.setStatus("mandatory")
_EPDUOutletPhase_ObjectIdentity = ObjectIdentity
ePDUOutletPhase = _EPDUOutletPhase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 2)
)
_EPDUOutletPhaseTable_Object = MibTable
ePDUOutletPhaseTable = _EPDUOutletPhaseTable_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 2, 1)
)
if mibBuilder.loadTexts:
    ePDUOutletPhaseTable.setStatus("mandatory")
_EPDUOutletPhaseEntry_Object = MibTableRow
ePDUOutletPhaseEntry = _EPDUOutletPhaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 2, 1, 1)
)
ePDUOutletPhaseEntry.setIndexNames(
    (0, "CPS-MIB", "ePDUOutletPhaseIndex"),
)
if mibBuilder.loadTexts:
    ePDUOutletPhaseEntry.setStatus("mandatory")


class _EPDUOutletPhaseIndex_Type(Integer32):
    """Custom type ePDUOutletPhaseIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("phase1", 1),
          ("phase2", 2),
          ("phase3", 3))
    )


_EPDUOutletPhaseIndex_Type.__name__ = "Integer32"
_EPDUOutletPhaseIndex_Object = MibTableColumn
ePDUOutletPhaseIndex = _EPDUOutletPhaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 2, 1, 1, 1),
    _EPDUOutletPhaseIndex_Type()
)
ePDUOutletPhaseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDUOutletPhaseIndex.setStatus("mandatory")


class _EPDUOutletPhaseOverloadRestriction_Type(Integer32):
    """Custom type ePDUOutletPhaseOverloadRestriction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alwaysAllowTurnON", 1),
          ("restrictOnNearOverload", 2),
          ("restrictOnOverload", 3))
    )


_EPDUOutletPhaseOverloadRestriction_Type.__name__ = "Integer32"
_EPDUOutletPhaseOverloadRestriction_Object = MibTableColumn
ePDUOutletPhaseOverloadRestriction = _EPDUOutletPhaseOverloadRestriction_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 2, 1, 1, 2),
    _EPDUOutletPhaseOverloadRestriction_Type()
)
ePDUOutletPhaseOverloadRestriction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDUOutletPhaseOverloadRestriction.setStatus("mandatory")
_EPDUOutletControl_ObjectIdentity = ObjectIdentity
ePDUOutletControl = _EPDUOutletControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 3)
)
_EPDUOutletControlTable_Object = MibTable
ePDUOutletControlTable = _EPDUOutletControlTable_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 3, 1)
)
if mibBuilder.loadTexts:
    ePDUOutletControlTable.setStatus("mandatory")
_EPDUOutletControlEntry_Object = MibTableRow
ePDUOutletControlEntry = _EPDUOutletControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 3, 1, 1)
)
ePDUOutletControlEntry.setIndexNames(
    (0, "CPS-MIB", "ePDUOutletControlIndex"),
)
if mibBuilder.loadTexts:
    ePDUOutletControlEntry.setStatus("mandatory")


class _EPDUOutletControlIndex_Type(Integer32):
    """Custom type ePDUOutletControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_EPDUOutletControlIndex_Type.__name__ = "Integer32"
_EPDUOutletControlIndex_Object = MibTableColumn
ePDUOutletControlIndex = _EPDUOutletControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 3, 1, 1, 1),
    _EPDUOutletControlIndex_Type()
)
ePDUOutletControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDUOutletControlIndex.setStatus("mandatory")
_EPDUOutletControlOutletName_Type = DisplayString
_EPDUOutletControlOutletName_Object = MibTableColumn
ePDUOutletControlOutletName = _EPDUOutletControlOutletName_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 3, 1, 1, 2),
    _EPDUOutletControlOutletName_Type()
)
ePDUOutletControlOutletName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDUOutletControlOutletName.setStatus("mandatory")


class _EPDUOutletControlOutletPhase_Type(Integer32):
    """Custom type ePDUOutletControlOutletPhase based on Integer32"""
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
        *(("phase1", 1),
          ("phase2", 2),
          ("phase3", 3),
          ("phase1-2", 4),
          ("phase2-3", 5),
          ("phase3-1", 6))
    )


_EPDUOutletControlOutletPhase_Type.__name__ = "Integer32"
_EPDUOutletControlOutletPhase_Object = MibTableColumn
ePDUOutletControlOutletPhase = _EPDUOutletControlOutletPhase_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 3, 1, 1, 3),
    _EPDUOutletControlOutletPhase_Type()
)
ePDUOutletControlOutletPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDUOutletControlOutletPhase.setStatus("mandatory")


class _EPDUOutletControlOutletCommand_Type(Integer32):
    """Custom type ePDUOutletControlOutletCommand based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("immediateOn", 1),
          ("immediateOff", 2),
          ("immediateReboot", 3),
          ("delayedOn", 4),
          ("delayedOff", 5),
          ("delayedReboot", 6),
          ("cancelPendingCommand", 7),
          ("outletIdentify", 8))
    )


_EPDUOutletControlOutletCommand_Type.__name__ = "Integer32"
_EPDUOutletControlOutletCommand_Object = MibTableColumn
ePDUOutletControlOutletCommand = _EPDUOutletControlOutletCommand_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 3, 1, 1, 4),
    _EPDUOutletControlOutletCommand_Type()
)
ePDUOutletControlOutletCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDUOutletControlOutletCommand.setStatus("mandatory")
_EPDUOutletControlOutletBank_Type = Integer32
_EPDUOutletControlOutletBank_Object = MibTableColumn
ePDUOutletControlOutletBank = _EPDUOutletControlOutletBank_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 3, 1, 1, 5),
    _EPDUOutletControlOutletBank_Type()
)
ePDUOutletControlOutletBank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDUOutletControlOutletBank.setStatus("mandatory")
_EPDUOutletConfig_ObjectIdentity = ObjectIdentity
ePDUOutletConfig = _EPDUOutletConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 4)
)
_EPDUOutletConfigTable_Object = MibTable
ePDUOutletConfigTable = _EPDUOutletConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 4, 1)
)
if mibBuilder.loadTexts:
    ePDUOutletConfigTable.setStatus("mandatory")
_EPDUOutletConfigEntry_Object = MibTableRow
ePDUOutletConfigEntry = _EPDUOutletConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 4, 1, 1)
)
ePDUOutletConfigEntry.setIndexNames(
    (0, "CPS-MIB", "ePDUOutletConfigIndex"),
)
if mibBuilder.loadTexts:
    ePDUOutletConfigEntry.setStatus("mandatory")


class _EPDUOutletConfigIndex_Type(Integer32):
    """Custom type ePDUOutletConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_EPDUOutletConfigIndex_Type.__name__ = "Integer32"
_EPDUOutletConfigIndex_Object = MibTableColumn
ePDUOutletConfigIndex = _EPDUOutletConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 4, 1, 1, 1),
    _EPDUOutletConfigIndex_Type()
)
ePDUOutletConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDUOutletConfigIndex.setStatus("mandatory")
_EPDUOutletConfigOutletName_Type = DisplayString
_EPDUOutletConfigOutletName_Object = MibTableColumn
ePDUOutletConfigOutletName = _EPDUOutletConfigOutletName_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 4, 1, 1, 2),
    _EPDUOutletConfigOutletName_Type()
)
ePDUOutletConfigOutletName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDUOutletConfigOutletName.setStatus("mandatory")


class _EPDUOutletConfigOutletPhase_Type(Integer32):
    """Custom type ePDUOutletConfigOutletPhase based on Integer32"""
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
        *(("phase1", 1),
          ("phase2", 2),
          ("phase3", 3),
          ("phase1-2", 4),
          ("phase2-3", 5),
          ("phase3-1", 6))
    )


_EPDUOutletConfigOutletPhase_Type.__name__ = "Integer32"
_EPDUOutletConfigOutletPhase_Object = MibTableColumn
ePDUOutletConfigOutletPhase = _EPDUOutletConfigOutletPhase_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 4, 1, 1, 3),
    _EPDUOutletConfigOutletPhase_Type()
)
ePDUOutletConfigOutletPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDUOutletConfigOutletPhase.setStatus("mandatory")
_EPDUOutletConfigPowerOnTime_Type = Integer32
_EPDUOutletConfigPowerOnTime_Object = MibTableColumn
ePDUOutletConfigPowerOnTime = _EPDUOutletConfigPowerOnTime_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 4, 1, 1, 4),
    _EPDUOutletConfigPowerOnTime_Type()
)
ePDUOutletConfigPowerOnTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDUOutletConfigPowerOnTime.setStatus("mandatory")
_EPDUOutletConfigPowerOffTime_Type = Integer32
_EPDUOutletConfigPowerOffTime_Object = MibTableColumn
ePDUOutletConfigPowerOffTime = _EPDUOutletConfigPowerOffTime_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 4, 1, 1, 5),
    _EPDUOutletConfigPowerOffTime_Type()
)
ePDUOutletConfigPowerOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDUOutletConfigPowerOffTime.setStatus("mandatory")
_EPDUOutletConfigRebootDuration_Type = Integer32
_EPDUOutletConfigRebootDuration_Object = MibTableColumn
ePDUOutletConfigRebootDuration = _EPDUOutletConfigRebootDuration_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 4, 1, 1, 6),
    _EPDUOutletConfigRebootDuration_Type()
)
ePDUOutletConfigRebootDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDUOutletConfigRebootDuration.setStatus("mandatory")
_EPDUOutletConfigOutletBank_Type = Integer32
_EPDUOutletConfigOutletBank_Object = MibTableColumn
ePDUOutletConfigOutletBank = _EPDUOutletConfigOutletBank_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 4, 1, 1, 7),
    _EPDUOutletConfigOutletBank_Type()
)
ePDUOutletConfigOutletBank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDUOutletConfigOutletBank.setStatus("mandatory")
_EPDUOutletConfigMonitoredTableSize_Type = Integer32
_EPDUOutletConfigMonitoredTableSize_Object = MibScalar
ePDUOutletConfigMonitoredTableSize = _EPDUOutletConfigMonitoredTableSize_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 4, 2),
    _EPDUOutletConfigMonitoredTableSize_Type()
)
ePDUOutletConfigMonitoredTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDUOutletConfigMonitoredTableSize.setStatus("mandatory")
_EPDUOutletConfigMonitoredTable_Object = MibTable
ePDUOutletConfigMonitoredTable = _EPDUOutletConfigMonitoredTable_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 4, 3)
)
if mibBuilder.loadTexts:
    ePDUOutletConfigMonitoredTable.setStatus("mandatory")
_EPDUOutletConfigMonitoredEntry_Object = MibTableRow
ePDUOutletConfigMonitoredEntry = _EPDUOutletConfigMonitoredEntry_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 4, 3, 1)
)
ePDUOutletConfigMonitoredEntry.setIndexNames(
    (0, "CPS-MIB", "ePDUOutletConfigMonitoredIndex"),
)
if mibBuilder.loadTexts:
    ePDUOutletConfigMonitoredEntry.setStatus("mandatory")


class _EPDUOutletConfigMonitoredIndex_Type(Integer32):
    """Custom type ePDUOutletConfigMonitoredIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_EPDUOutletConfigMonitoredIndex_Type.__name__ = "Integer32"
_EPDUOutletConfigMonitoredIndex_Object = MibTableColumn
ePDUOutletConfigMonitoredIndex = _EPDUOutletConfigMonitoredIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 4, 3, 1, 1),
    _EPDUOutletConfigMonitoredIndex_Type()
)
ePDUOutletConfigMonitoredIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDUOutletConfigMonitoredIndex.setStatus("mandatory")
_EPDUOutletConfigMonitoredName_Type = DisplayString
_EPDUOutletConfigMonitoredName_Object = MibTableColumn
ePDUOutletConfigMonitoredName = _EPDUOutletConfigMonitoredName_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 4, 3, 1, 2),
    _EPDUOutletConfigMonitoredName_Type()
)
ePDUOutletConfigMonitoredName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDUOutletConfigMonitoredName.setStatus("mandatory")
_EPDUOutletConfigMonitoredNumber_Type = Integer32
_EPDUOutletConfigMonitoredNumber_Object = MibTableColumn
ePDUOutletConfigMonitoredNumber = _EPDUOutletConfigMonitoredNumber_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 4, 3, 1, 3),
    _EPDUOutletConfigMonitoredNumber_Type()
)
ePDUOutletConfigMonitoredNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDUOutletConfigMonitoredNumber.setStatus("mandatory")
_EPDUOutletConfigMonitoredLowLoadThreshold_Type = Integer32
_EPDUOutletConfigMonitoredLowLoadThreshold_Object = MibTableColumn
ePDUOutletConfigMonitoredLowLoadThreshold = _EPDUOutletConfigMonitoredLowLoadThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 4, 3, 1, 4),
    _EPDUOutletConfigMonitoredLowLoadThreshold_Type()
)
ePDUOutletConfigMonitoredLowLoadThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDUOutletConfigMonitoredLowLoadThreshold.setStatus("mandatory")
_EPDUOutletConfigMonitoredNearOverloadThreshold_Type = Integer32
_EPDUOutletConfigMonitoredNearOverloadThreshold_Object = MibTableColumn
ePDUOutletConfigMonitoredNearOverloadThreshold = _EPDUOutletConfigMonitoredNearOverloadThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 4, 3, 1, 5),
    _EPDUOutletConfigMonitoredNearOverloadThreshold_Type()
)
ePDUOutletConfigMonitoredNearOverloadThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDUOutletConfigMonitoredNearOverloadThreshold.setStatus("mandatory")
_EPDUOutletConfigMonitoredOverloadThreshold_Type = Integer32
_EPDUOutletConfigMonitoredOverloadThreshold_Object = MibTableColumn
ePDUOutletConfigMonitoredOverloadThreshold = _EPDUOutletConfigMonitoredOverloadThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 4, 3, 1, 6),
    _EPDUOutletConfigMonitoredOverloadThreshold_Type()
)
ePDUOutletConfigMonitoredOverloadThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDUOutletConfigMonitoredOverloadThreshold.setStatus("mandatory")


class _EPDUOutletConfigMonitoredPeakLoadReset_Type(Integer32):
    """Custom type ePDUOutletConfigMonitoredPeakLoadReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("reset", 2),
          ("notSupport", 3))
    )


_EPDUOutletConfigMonitoredPeakLoadReset_Type.__name__ = "Integer32"
_EPDUOutletConfigMonitoredPeakLoadReset_Object = MibTableColumn
ePDUOutletConfigMonitoredPeakLoadReset = _EPDUOutletConfigMonitoredPeakLoadReset_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 4, 3, 1, 7),
    _EPDUOutletConfigMonitoredPeakLoadReset_Type()
)
ePDUOutletConfigMonitoredPeakLoadReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDUOutletConfigMonitoredPeakLoadReset.setStatus("mandatory")


class _EPDUOutletConfigMonitoredEnergyReset_Type(Integer32):
    """Custom type ePDUOutletConfigMonitoredEnergyReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("reset", 2),
          ("notSupport", 3))
    )


_EPDUOutletConfigMonitoredEnergyReset_Type.__name__ = "Integer32"
_EPDUOutletConfigMonitoredEnergyReset_Object = MibTableColumn
ePDUOutletConfigMonitoredEnergyReset = _EPDUOutletConfigMonitoredEnergyReset_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 4, 3, 1, 8),
    _EPDUOutletConfigMonitoredEnergyReset_Type()
)
ePDUOutletConfigMonitoredEnergyReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDUOutletConfigMonitoredEnergyReset.setStatus("mandatory")
_EPDUOutletStatus_ObjectIdentity = ObjectIdentity
ePDUOutletStatus = _EPDUOutletStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 5)
)
_EPDUOutletStatusTable_Object = MibTable
ePDUOutletStatusTable = _EPDUOutletStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 5, 1)
)
if mibBuilder.loadTexts:
    ePDUOutletStatusTable.setStatus("mandatory")
_EPDUOutletStatusEntry_Object = MibTableRow
ePDUOutletStatusEntry = _EPDUOutletStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 5, 1, 1)
)
ePDUOutletStatusEntry.setIndexNames(
    (0, "CPS-MIB", "ePDUOutletStatusIndex"),
)
if mibBuilder.loadTexts:
    ePDUOutletStatusEntry.setStatus("mandatory")


class _EPDUOutletStatusIndex_Type(Integer32):
    """Custom type ePDUOutletStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_EPDUOutletStatusIndex_Type.__name__ = "Integer32"
_EPDUOutletStatusIndex_Object = MibTableColumn
ePDUOutletStatusIndex = _EPDUOutletStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 5, 1, 1, 1),
    _EPDUOutletStatusIndex_Type()
)
ePDUOutletStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDUOutletStatusIndex.setStatus("mandatory")
_EPDUOutletStatusOutletName_Type = DisplayString
_EPDUOutletStatusOutletName_Object = MibTableColumn
ePDUOutletStatusOutletName = _EPDUOutletStatusOutletName_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 5, 1, 1, 2),
    _EPDUOutletStatusOutletName_Type()
)
ePDUOutletStatusOutletName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDUOutletStatusOutletName.setStatus("mandatory")


class _EPDUOutletStatusOutletPhase_Type(Integer32):
    """Custom type ePDUOutletStatusOutletPhase based on Integer32"""
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
        *(("phase1", 1),
          ("phase2", 2),
          ("phase3", 3),
          ("phase1-2", 4),
          ("phase2-3", 5),
          ("phase3-1", 6))
    )


_EPDUOutletStatusOutletPhase_Type.__name__ = "Integer32"
_EPDUOutletStatusOutletPhase_Object = MibTableColumn
ePDUOutletStatusOutletPhase = _EPDUOutletStatusOutletPhase_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 5, 1, 1, 3),
    _EPDUOutletStatusOutletPhase_Type()
)
ePDUOutletStatusOutletPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDUOutletStatusOutletPhase.setStatus("mandatory")


class _EPDUOutletStatusOutletState_Type(Integer32):
    """Custom type ePDUOutletStatusOutletState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("outletStatusOn", 1),
          ("outletStatusOff", 2))
    )


_EPDUOutletStatusOutletState_Type.__name__ = "Integer32"
_EPDUOutletStatusOutletState_Object = MibTableColumn
ePDUOutletStatusOutletState = _EPDUOutletStatusOutletState_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 5, 1, 1, 4),
    _EPDUOutletStatusOutletState_Type()
)
ePDUOutletStatusOutletState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDUOutletStatusOutletState.setStatus("mandatory")


class _EPDUOutletStatusCommandPending_Type(Integer32):
    """Custom type ePDUOutletStatusCommandPending based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("outletStatusCommandPending", 1),
          ("outletStatusNoCommandPending", 2))
    )


_EPDUOutletStatusCommandPending_Type.__name__ = "Integer32"
_EPDUOutletStatusCommandPending_Object = MibTableColumn
ePDUOutletStatusCommandPending = _EPDUOutletStatusCommandPending_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 5, 1, 1, 5),
    _EPDUOutletStatusCommandPending_Type()
)
ePDUOutletStatusCommandPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDUOutletStatusCommandPending.setStatus("mandatory")
_EPDUOutletStatusOutletBank_Type = Integer32
_EPDUOutletStatusOutletBank_Object = MibTableColumn
ePDUOutletStatusOutletBank = _EPDUOutletStatusOutletBank_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 5, 1, 1, 6),
    _EPDUOutletStatusOutletBank_Type()
)
ePDUOutletStatusOutletBank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDUOutletStatusOutletBank.setStatus("mandatory")
_EPDUOutletStatusLoad_Type = Gauge32
_EPDUOutletStatusLoad_Object = MibTableColumn
ePDUOutletStatusLoad = _EPDUOutletStatusLoad_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 5, 1, 1, 7),
    _EPDUOutletStatusLoad_Type()
)
ePDUOutletStatusLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDUOutletStatusLoad.setStatus("mandatory")
_EPDUOutletStatusActivePower_Type = Gauge32
_EPDUOutletStatusActivePower_Object = MibTableColumn
ePDUOutletStatusActivePower = _EPDUOutletStatusActivePower_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 5, 1, 1, 8),
    _EPDUOutletStatusActivePower_Type()
)
ePDUOutletStatusActivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDUOutletStatusActivePower.setStatus("mandatory")


class _EPDUOutletStatusAlarm_Type(Integer32):
    """Custom type ePDUOutletStatusAlarm based on Integer32"""
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
        *(("noLoadAlarm", 1),
          ("underCurrentAlarm", 2),
          ("nearOverCurrentAlarm", 3),
          ("overCurrentAlarm", 4))
    )


_EPDUOutletStatusAlarm_Type.__name__ = "Integer32"
_EPDUOutletStatusAlarm_Object = MibTableColumn
ePDUOutletStatusAlarm = _EPDUOutletStatusAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 5, 1, 1, 9),
    _EPDUOutletStatusAlarm_Type()
)
ePDUOutletStatusAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDUOutletStatusAlarm.setStatus("mandatory")
_EPDUOutletStatusPeakPower_Type = Gauge32
_EPDUOutletStatusPeakPower_Object = MibTableColumn
ePDUOutletStatusPeakPower = _EPDUOutletStatusPeakPower_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 5, 1, 1, 10),
    _EPDUOutletStatusPeakPower_Type()
)
ePDUOutletStatusPeakPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDUOutletStatusPeakPower.setStatus("mandatory")
_EPDUOutletStatusPeakPowerTime_Type = DisplayString
_EPDUOutletStatusPeakPowerTime_Object = MibTableColumn
ePDUOutletStatusPeakPowerTime = _EPDUOutletStatusPeakPowerTime_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 5, 1, 1, 11),
    _EPDUOutletStatusPeakPowerTime_Type()
)
ePDUOutletStatusPeakPowerTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDUOutletStatusPeakPowerTime.setStatus("mandatory")
_EPDUOutletStatusPeakPowerStart_Type = DisplayString
_EPDUOutletStatusPeakPowerStart_Object = MibTableColumn
ePDUOutletStatusPeakPowerStart = _EPDUOutletStatusPeakPowerStart_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 5, 1, 1, 12),
    _EPDUOutletStatusPeakPowerStart_Type()
)
ePDUOutletStatusPeakPowerStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDUOutletStatusPeakPowerStart.setStatus("mandatory")
_EPDUOutletStatusEnergy_Type = Gauge32
_EPDUOutletStatusEnergy_Object = MibTableColumn
ePDUOutletStatusEnergy = _EPDUOutletStatusEnergy_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 5, 1, 1, 13),
    _EPDUOutletStatusEnergy_Type()
)
ePDUOutletStatusEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDUOutletStatusEnergy.setStatus("mandatory")
_EPDUOutletStatusEnergyStartTime_Type = DisplayString
_EPDUOutletStatusEnergyStartTime_Object = MibTableColumn
ePDUOutletStatusEnergyStartTime = _EPDUOutletStatusEnergyStartTime_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 5, 1, 1, 14),
    _EPDUOutletStatusEnergyStartTime_Type()
)
ePDUOutletStatusEnergyStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDUOutletStatusEnergyStartTime.setStatus("mandatory")
_EPDUOutletBank_ObjectIdentity = ObjectIdentity
ePDUOutletBank = _EPDUOutletBank_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 6)
)
_EPDUOutletBankTable_Object = MibTable
ePDUOutletBankTable = _EPDUOutletBankTable_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 6, 1)
)
if mibBuilder.loadTexts:
    ePDUOutletBankTable.setStatus("mandatory")
_EPDUOutletBankEntry_Object = MibTableRow
ePDUOutletBankEntry = _EPDUOutletBankEntry_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 6, 1, 1)
)
ePDUOutletBankEntry.setIndexNames(
    (0, "CPS-MIB", "ePDUOutletBankIndex"),
)
if mibBuilder.loadTexts:
    ePDUOutletBankEntry.setStatus("mandatory")


class _EPDUOutletBankIndex_Type(Integer32):
    """Custom type ePDUOutletBankIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_EPDUOutletBankIndex_Type.__name__ = "Integer32"
_EPDUOutletBankIndex_Object = MibTableColumn
ePDUOutletBankIndex = _EPDUOutletBankIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 6, 1, 1, 1),
    _EPDUOutletBankIndex_Type()
)
ePDUOutletBankIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDUOutletBankIndex.setStatus("mandatory")


class _EPDUOutletBankOverloadRestriction_Type(Integer32):
    """Custom type ePDUOutletBankOverloadRestriction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alwaysAllowTurnON", 1),
          ("restrictOnNearOverload", 2),
          ("restrictOnOverload", 3))
    )


_EPDUOutletBankOverloadRestriction_Type.__name__ = "Integer32"
_EPDUOutletBankOverloadRestriction_Object = MibTableColumn
ePDUOutletBankOverloadRestriction = _EPDUOutletBankOverloadRestriction_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 3, 6, 1, 1, 2),
    _EPDUOutletBankOverloadRestriction_Type()
)
ePDUOutletBankOverloadRestriction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDUOutletBankOverloadRestriction.setStatus("mandatory")
_EPDUPowerSupply_ObjectIdentity = ObjectIdentity
ePDUPowerSupply = _EPDUPowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 4)
)
_EPDUPowerSupplyDevice_ObjectIdentity = ObjectIdentity
ePDUPowerSupplyDevice = _EPDUPowerSupplyDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 4, 1)
)


class _EPDUPowerSupply1Status_Type(Integer32):
    """Custom type ePDUPowerSupply1Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("powerSupplyOneOk", 1),
          ("powerSupplyOneFailed", 2))
    )


_EPDUPowerSupply1Status_Type.__name__ = "Integer32"
_EPDUPowerSupply1Status_Object = MibScalar
ePDUPowerSupply1Status = _EPDUPowerSupply1Status_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 4, 1, 1),
    _EPDUPowerSupply1Status_Type()
)
ePDUPowerSupply1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDUPowerSupply1Status.setStatus("mandatory")


class _EPDUPowerSupply2Status_Type(Integer32):
    """Custom type ePDUPowerSupply2Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("powerSupplyTwoOk", 1),
          ("powerSupplyTwoFailed", 2),
          ("powerSupplyTwoNotPresent", 3))
    )


_EPDUPowerSupply2Status_Type.__name__ = "Integer32"
_EPDUPowerSupply2Status_Object = MibScalar
ePDUPowerSupply2Status = _EPDUPowerSupply2Status_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 4, 1, 2),
    _EPDUPowerSupply2Status_Type()
)
ePDUPowerSupply2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDUPowerSupply2Status.setStatus("mandatory")


class _EPDUPowerSupplyAlarm_Type(Integer32):
    """Custom type ePDUPowerSupplyAlarm based on Integer32"""
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
        *(("allAvailablePowerSuppliesOK", 1),
          ("powerSupplyOneFailed", 2),
          ("powerSupplyTwoFailed", 3),
          ("powerSupplyOneandTwoFailed", 4))
    )


_EPDUPowerSupplyAlarm_Type.__name__ = "Integer32"
_EPDUPowerSupplyAlarm_Object = MibScalar
ePDUPowerSupplyAlarm = _EPDUPowerSupplyAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 4, 1, 3),
    _EPDUPowerSupplyAlarm_Type()
)
ePDUPowerSupplyAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDUPowerSupplyAlarm.setStatus("mandatory")
_EPDUStatus_ObjectIdentity = ObjectIdentity
ePDUStatus = _EPDUStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 5)
)
_EPDUStatusBankTableSize_Type = Integer32
_EPDUStatusBankTableSize_Object = MibScalar
ePDUStatusBankTableSize = _EPDUStatusBankTableSize_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 5, 1),
    _EPDUStatusBankTableSize_Type()
)
ePDUStatusBankTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDUStatusBankTableSize.setStatus("mandatory")
_EPDUStatusBankTable_Object = MibTable
ePDUStatusBankTable = _EPDUStatusBankTable_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 5, 2)
)
if mibBuilder.loadTexts:
    ePDUStatusBankTable.setStatus("mandatory")
_EPDUStatusBankEntry_Object = MibTableRow
ePDUStatusBankEntry = _EPDUStatusBankEntry_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 5, 2, 1)
)
ePDUStatusBankEntry.setIndexNames(
    (0, "CPS-MIB", "ePDUStatusBankIndex"),
)
if mibBuilder.loadTexts:
    ePDUStatusBankEntry.setStatus("mandatory")


class _EPDUStatusBankIndex_Type(Integer32):
    """Custom type ePDUStatusBankIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_EPDUStatusBankIndex_Type.__name__ = "Integer32"
_EPDUStatusBankIndex_Object = MibTableColumn
ePDUStatusBankIndex = _EPDUStatusBankIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 5, 2, 1, 1),
    _EPDUStatusBankIndex_Type()
)
ePDUStatusBankIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDUStatusBankIndex.setStatus("mandatory")
_EPDUStatusBankNumber_Type = Integer32
_EPDUStatusBankNumber_Object = MibTableColumn
ePDUStatusBankNumber = _EPDUStatusBankNumber_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 5, 2, 1, 2),
    _EPDUStatusBankNumber_Type()
)
ePDUStatusBankNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDUStatusBankNumber.setStatus("mandatory")


class _EPDUStatusBankState_Type(Integer32):
    """Custom type ePDUStatusBankState based on Integer32"""
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
        *(("bankLoadNormal", 1),
          ("bankLoadLow", 2),
          ("bankLoadNearOverload", 3),
          ("bankLoadOverload", 4))
    )


_EPDUStatusBankState_Type.__name__ = "Integer32"
_EPDUStatusBankState_Object = MibTableColumn
ePDUStatusBankState = _EPDUStatusBankState_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 5, 2, 1, 3),
    _EPDUStatusBankState_Type()
)
ePDUStatusBankState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDUStatusBankState.setStatus("mandatory")
_EPDUStatusPhaseTableSize_Type = Integer32
_EPDUStatusPhaseTableSize_Object = MibScalar
ePDUStatusPhaseTableSize = _EPDUStatusPhaseTableSize_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 5, 3),
    _EPDUStatusPhaseTableSize_Type()
)
ePDUStatusPhaseTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDUStatusPhaseTableSize.setStatus("mandatory")
_EPDUStatusPhaseTable_Object = MibTable
ePDUStatusPhaseTable = _EPDUStatusPhaseTable_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 5, 4)
)
if mibBuilder.loadTexts:
    ePDUStatusPhaseTable.setStatus("mandatory")
_EPDUStatusPhaseEntry_Object = MibTableRow
ePDUStatusPhaseEntry = _EPDUStatusPhaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 5, 4, 1)
)
ePDUStatusPhaseEntry.setIndexNames(
    (0, "CPS-MIB", "ePDUStatusPhaseIndex"),
)
if mibBuilder.loadTexts:
    ePDUStatusPhaseEntry.setStatus("mandatory")


class _EPDUStatusPhaseIndex_Type(Integer32):
    """Custom type ePDUStatusPhaseIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_EPDUStatusPhaseIndex_Type.__name__ = "Integer32"
_EPDUStatusPhaseIndex_Object = MibTableColumn
ePDUStatusPhaseIndex = _EPDUStatusPhaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 5, 4, 1, 1),
    _EPDUStatusPhaseIndex_Type()
)
ePDUStatusPhaseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDUStatusPhaseIndex.setStatus("mandatory")
_EPDUStatusPhaseNumber_Type = Integer32
_EPDUStatusPhaseNumber_Object = MibTableColumn
ePDUStatusPhaseNumber = _EPDUStatusPhaseNumber_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 5, 4, 1, 2),
    _EPDUStatusPhaseNumber_Type()
)
ePDUStatusPhaseNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDUStatusPhaseNumber.setStatus("mandatory")


class _EPDUStatusPhaseState_Type(Integer32):
    """Custom type ePDUStatusPhaseState based on Integer32"""
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
        *(("phaseLoadNormal", 1),
          ("phaseLoadLow", 2),
          ("phaseLoadNearOverload", 3),
          ("phaseLoadOverload", 4))
    )


_EPDUStatusPhaseState_Type.__name__ = "Integer32"
_EPDUStatusPhaseState_Object = MibTableColumn
ePDUStatusPhaseState = _EPDUStatusPhaseState_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 5, 4, 1, 3),
    _EPDUStatusPhaseState_Type()
)
ePDUStatusPhaseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDUStatusPhaseState.setStatus("mandatory")
_EPDUStatusOutletTableSize_Type = Integer32
_EPDUStatusOutletTableSize_Object = MibScalar
ePDUStatusOutletTableSize = _EPDUStatusOutletTableSize_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 5, 5),
    _EPDUStatusOutletTableSize_Type()
)
ePDUStatusOutletTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDUStatusOutletTableSize.setStatus("mandatory")
_EPDUStatusOutletTable_Object = MibTable
ePDUStatusOutletTable = _EPDUStatusOutletTable_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 5, 6)
)
if mibBuilder.loadTexts:
    ePDUStatusOutletTable.setStatus("mandatory")
_EPDUStatusOutletEntry_Object = MibTableRow
ePDUStatusOutletEntry = _EPDUStatusOutletEntry_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 5, 6, 1)
)
ePDUStatusOutletEntry.setIndexNames(
    (0, "CPS-MIB", "ePDUStatusOutletIndex"),
)
if mibBuilder.loadTexts:
    ePDUStatusOutletEntry.setStatus("mandatory")


class _EPDUStatusOutletIndex_Type(Integer32):
    """Custom type ePDUStatusOutletIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_EPDUStatusOutletIndex_Type.__name__ = "Integer32"
_EPDUStatusOutletIndex_Object = MibTableColumn
ePDUStatusOutletIndex = _EPDUStatusOutletIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 5, 6, 1, 1),
    _EPDUStatusOutletIndex_Type()
)
ePDUStatusOutletIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDUStatusOutletIndex.setStatus("mandatory")
_EPDUStatusOutletNumber_Type = Integer32
_EPDUStatusOutletNumber_Object = MibTableColumn
ePDUStatusOutletNumber = _EPDUStatusOutletNumber_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 5, 6, 1, 2),
    _EPDUStatusOutletNumber_Type()
)
ePDUStatusOutletNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDUStatusOutletNumber.setStatus("mandatory")


class _EPDUStatusOutletState_Type(Integer32):
    """Custom type ePDUStatusOutletState based on Integer32"""
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
        *(("outletLoadNormal", 1),
          ("outletLoadLow", 2),
          ("outletLoadNearOverload", 3),
          ("outletLoadOverload", 4))
    )


_EPDUStatusOutletState_Type.__name__ = "Integer32"
_EPDUStatusOutletState_Object = MibTableColumn
ePDUStatusOutletState = _EPDUStatusOutletState_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 5, 6, 1, 3),
    _EPDUStatusOutletState_Type()
)
ePDUStatusOutletState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDUStatusOutletState.setStatus("mandatory")
_EPDUStatusInputVoltage_Type = Integer32
_EPDUStatusInputVoltage_Object = MibScalar
ePDUStatusInputVoltage = _EPDUStatusInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 5, 7),
    _EPDUStatusInputVoltage_Type()
)
ePDUStatusInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDUStatusInputVoltage.setStatus("mandatory")
_EPDUStatusInputFrequency_Type = Integer32
_EPDUStatusInputFrequency_Object = MibScalar
ePDUStatusInputFrequency = _EPDUStatusInputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 3, 5, 8),
    _EPDUStatusInputFrequency_Type()
)
ePDUStatusInputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDUStatusInputFrequency.setStatus("mandatory")
_EnvironmentSensor_ObjectIdentity = ObjectIdentity
environmentSensor = _EnvironmentSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 4)
)
_EnvirIdent_ObjectIdentity = ObjectIdentity
envirIdent = _EnvirIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 4, 1)
)
_EnvirIdentName_Type = DisplayString
_EnvirIdentName_Object = MibScalar
envirIdentName = _EnvirIdentName_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 4, 1, 1),
    _EnvirIdentName_Type()
)
envirIdentName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envirIdentName.setStatus("mandatory")
_EnvirIdentLocation_Type = DisplayString
_EnvirIdentLocation_Object = MibScalar
envirIdentLocation = _EnvirIdentLocation_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 4, 1, 2),
    _EnvirIdentLocation_Type()
)
envirIdentLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envirIdentLocation.setStatus("mandatory")
_EnvirTemp_ObjectIdentity = ObjectIdentity
envirTemp = _EnvirTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 4, 2)
)
_EnvirTemperature_Type = Integer32
_EnvirTemperature_Object = MibScalar
envirTemperature = _EnvirTemperature_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 4, 2, 1),
    _EnvirTemperature_Type()
)
envirTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envirTemperature.setStatus("mandatory")
_EnvirTempHighThreshold_Type = Integer32
_EnvirTempHighThreshold_Object = MibScalar
envirTempHighThreshold = _EnvirTempHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 4, 2, 2),
    _EnvirTempHighThreshold_Type()
)
envirTempHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envirTempHighThreshold.setStatus("mandatory")
_EnvirTempLowThreshold_Type = Integer32
_EnvirTempLowThreshold_Object = MibScalar
envirTempLowThreshold = _EnvirTempLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 4, 2, 3),
    _EnvirTempLowThreshold_Type()
)
envirTempLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envirTempLowThreshold.setStatus("mandatory")
_EnvirTempRateOfChange_Type = Integer32
_EnvirTempRateOfChange_Object = MibScalar
envirTempRateOfChange = _EnvirTempRateOfChange_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 4, 2, 4),
    _EnvirTempRateOfChange_Type()
)
envirTempRateOfChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envirTempRateOfChange.setStatus("mandatory")
_EnvirTempHysteresis_Type = Integer32
_EnvirTempHysteresis_Object = MibScalar
envirTempHysteresis = _EnvirTempHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 4, 2, 5),
    _EnvirTempHysteresis_Type()
)
envirTempHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envirTempHysteresis.setStatus("mandatory")
_EnvirTemperatureCelsius_Type = Integer32
_EnvirTemperatureCelsius_Object = MibScalar
envirTemperatureCelsius = _EnvirTemperatureCelsius_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 4, 2, 6),
    _EnvirTemperatureCelsius_Type()
)
envirTemperatureCelsius.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envirTemperatureCelsius.setStatus("mandatory")
_EnvirTempCelsiusHighThreshold_Type = Integer32
_EnvirTempCelsiusHighThreshold_Object = MibScalar
envirTempCelsiusHighThreshold = _EnvirTempCelsiusHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 4, 2, 7),
    _EnvirTempCelsiusHighThreshold_Type()
)
envirTempCelsiusHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envirTempCelsiusHighThreshold.setStatus("mandatory")
_EnvirTempCelsiusLowThreshold_Type = Integer32
_EnvirTempCelsiusLowThreshold_Object = MibScalar
envirTempCelsiusLowThreshold = _EnvirTempCelsiusLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 4, 2, 8),
    _EnvirTempCelsiusLowThreshold_Type()
)
envirTempCelsiusLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envirTempCelsiusLowThreshold.setStatus("mandatory")
_EnvirTempCelsiusRateOfChange_Type = Integer32
_EnvirTempCelsiusRateOfChange_Object = MibScalar
envirTempCelsiusRateOfChange = _EnvirTempCelsiusRateOfChange_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 4, 2, 9),
    _EnvirTempCelsiusRateOfChange_Type()
)
envirTempCelsiusRateOfChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envirTempCelsiusRateOfChange.setStatus("mandatory")
_EnvirTempCelsiusHysteresis_Type = Integer32
_EnvirTempCelsiusHysteresis_Object = MibScalar
envirTempCelsiusHysteresis = _EnvirTempCelsiusHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 4, 2, 10),
    _EnvirTempCelsiusHysteresis_Type()
)
envirTempCelsiusHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envirTempCelsiusHysteresis.setStatus("mandatory")
_EnvirHumid_ObjectIdentity = ObjectIdentity
envirHumid = _EnvirHumid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 4, 3)
)
_EnvirHumidity_Type = Integer32
_EnvirHumidity_Object = MibScalar
envirHumidity = _EnvirHumidity_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 4, 3, 1),
    _EnvirHumidity_Type()
)
envirHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envirHumidity.setStatus("mandatory")
_EnvirHumidHighThreshold_Type = Integer32
_EnvirHumidHighThreshold_Object = MibScalar
envirHumidHighThreshold = _EnvirHumidHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 4, 3, 2),
    _EnvirHumidHighThreshold_Type()
)
envirHumidHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envirHumidHighThreshold.setStatus("mandatory")
_EnvirHumidLowThreshold_Type = Integer32
_EnvirHumidLowThreshold_Object = MibScalar
envirHumidLowThreshold = _EnvirHumidLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 4, 3, 3),
    _EnvirHumidLowThreshold_Type()
)
envirHumidLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envirHumidLowThreshold.setStatus("mandatory")
_EnvirHumidRateOfChange_Type = Integer32
_EnvirHumidRateOfChange_Object = MibScalar
envirHumidRateOfChange = _EnvirHumidRateOfChange_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 4, 3, 4),
    _EnvirHumidRateOfChange_Type()
)
envirHumidRateOfChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envirHumidRateOfChange.setStatus("mandatory")
_EnvirHumidHysteresis_Type = Integer32
_EnvirHumidHysteresis_Object = MibScalar
envirHumidHysteresis = _EnvirHumidHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 4, 3, 5),
    _EnvirHumidHysteresis_Type()
)
envirHumidHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envirHumidHysteresis.setStatus("mandatory")
_EnvirContact_ObjectIdentity = ObjectIdentity
envirContact = _EnvirContact_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 4, 4)
)
_EnvirContactTableSize_Type = Integer32
_EnvirContactTableSize_Object = MibScalar
envirContactTableSize = _EnvirContactTableSize_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 4, 4, 1),
    _EnvirContactTableSize_Type()
)
envirContactTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envirContactTableSize.setStatus("mandatory")
_EnvirContactTable_Object = MibTable
envirContactTable = _EnvirContactTable_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 4, 4, 2)
)
if mibBuilder.loadTexts:
    envirContactTable.setStatus("mandatory")
_EnvirContactEntry_Object = MibTableRow
envirContactEntry = _EnvirContactEntry_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 4, 4, 2, 1)
)
envirContactEntry.setIndexNames(
    (0, "CPS-MIB", "envirContactIndex"),
)
if mibBuilder.loadTexts:
    envirContactEntry.setStatus("mandatory")


class _EnvirContactIndex_Type(Integer32):
    """Custom type envirContactIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_EnvirContactIndex_Type.__name__ = "Integer32"
_EnvirContactIndex_Object = MibTableColumn
envirContactIndex = _EnvirContactIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 4, 4, 2, 1, 1),
    _EnvirContactIndex_Type()
)
envirContactIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envirContactIndex.setStatus("mandatory")
_EnvirContactName_Type = DisplayString
_EnvirContactName_Object = MibTableColumn
envirContactName = _EnvirContactName_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 4, 4, 2, 1, 2),
    _EnvirContactName_Type()
)
envirContactName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envirContactName.setStatus("mandatory")


class _EnvirContactStatus_Type(Integer32):
    """Custom type envirContactStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("contactNormal", 1),
          ("contactAbnormal", 2))
    )


_EnvirContactStatus_Type.__name__ = "Integer32"
_EnvirContactStatus_Object = MibTableColumn
envirContactStatus = _EnvirContactStatus_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 4, 4, 2, 1, 3),
    _EnvirContactStatus_Type()
)
envirContactStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envirContactStatus.setStatus("mandatory")


class _EnvirContactNormalState_Type(Integer32):
    """Custom type envirContactNormalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normalOpen", 1),
          ("normalClose", 2))
    )


_EnvirContactNormalState_Type.__name__ = "Integer32"
_EnvirContactNormalState_Object = MibTableColumn
envirContactNormalState = _EnvirContactNormalState_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 4, 4, 2, 1, 4),
    _EnvirContactNormalState_Type()
)
envirContactNormalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envirContactNormalState.setStatus("mandatory")
_Ats_ObjectIdentity = ObjectIdentity
ats = _Ats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5)
)
_AtsIdent_ObjectIdentity = ObjectIdentity
atsIdent = _AtsIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 1)
)
_AtsIdentName_Type = DisplayString
_AtsIdentName_Object = MibScalar
atsIdentName = _AtsIdentName_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 1, 1),
    _AtsIdentName_Type()
)
atsIdentName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atsIdentName.setStatus("mandatory")
_AtsIdentModelName_Type = DisplayString
_AtsIdentModelName_Object = MibScalar
atsIdentModelName = _AtsIdentModelName_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 1, 2),
    _AtsIdentModelName_Type()
)
atsIdentModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsIdentModelName.setStatus("mandatory")
_AtsIdentHardwareRev_Type = DisplayString
_AtsIdentHardwareRev_Object = MibScalar
atsIdentHardwareRev = _AtsIdentHardwareRev_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 1, 3),
    _AtsIdentHardwareRev_Type()
)
atsIdentHardwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsIdentHardwareRev.setStatus("mandatory")
_AtsIdentFirmwareRev_Type = DisplayString
_AtsIdentFirmwareRev_Object = MibScalar
atsIdentFirmwareRev = _AtsIdentFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 1, 4),
    _AtsIdentFirmwareRev_Type()
)
atsIdentFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsIdentFirmwareRev.setStatus("mandatory")
_AtsIdentSerialNumber_Type = DisplayString
_AtsIdentSerialNumber_Object = MibScalar
atsIdentSerialNumber = _AtsIdentSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 1, 5),
    _AtsIdentSerialNumber_Type()
)
atsIdentSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsIdentSerialNumber.setStatus("mandatory")
_AtsIdentDateOfManufacture_Type = DisplayString
_AtsIdentDateOfManufacture_Object = MibScalar
atsIdentDateOfManufacture = _AtsIdentDateOfManufacture_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 1, 6),
    _AtsIdentDateOfManufacture_Type()
)
atsIdentDateOfManufacture.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsIdentDateOfManufacture.setStatus("mandatory")
_AtsIdentDeviceRatingVoltage_Type = DisplayString
_AtsIdentDeviceRatingVoltage_Object = MibScalar
atsIdentDeviceRatingVoltage = _AtsIdentDeviceRatingVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 1, 7),
    _AtsIdentDeviceRatingVoltage_Type()
)
atsIdentDeviceRatingVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsIdentDeviceRatingVoltage.setStatus("mandatory")
_AtsIdentDeviceRatingCurrent_Type = Integer32
_AtsIdentDeviceRatingCurrent_Object = MibScalar
atsIdentDeviceRatingCurrent = _AtsIdentDeviceRatingCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 1, 8),
    _AtsIdentDeviceRatingCurrent_Type()
)
atsIdentDeviceRatingCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsIdentDeviceRatingCurrent.setStatus("mandatory")
_AtsIdentDeviceOutletNum_Type = Integer32
_AtsIdentDeviceOutletNum_Object = MibScalar
atsIdentDeviceOutletNum = _AtsIdentDeviceOutletNum_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 1, 9),
    _AtsIdentDeviceOutletNum_Type()
)
atsIdentDeviceOutletNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsIdentDeviceOutletNum.setStatus("mandatory")
_AtsIdentAgentModelName_Type = DisplayString
_AtsIdentAgentModelName_Object = MibScalar
atsIdentAgentModelName = _AtsIdentAgentModelName_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 1, 10),
    _AtsIdentAgentModelName_Type()
)
atsIdentAgentModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsIdentAgentModelName.setStatus("mandatory")
_AtsIdentAgentHardwareRevision_Type = DisplayString
_AtsIdentAgentHardwareRevision_Object = MibScalar
atsIdentAgentHardwareRevision = _AtsIdentAgentHardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 1, 11),
    _AtsIdentAgentHardwareRevision_Type()
)
atsIdentAgentHardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsIdentAgentHardwareRevision.setStatus("mandatory")
_AtsIdentAgentFirmwareRevision_Type = DisplayString
_AtsIdentAgentFirmwareRevision_Object = MibScalar
atsIdentAgentFirmwareRevision = _AtsIdentAgentFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 1, 12),
    _AtsIdentAgentFirmwareRevision_Type()
)
atsIdentAgentFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsIdentAgentFirmwareRevision.setStatus("mandatory")
_AtsIdentAgentSerialNumber_Type = DisplayString
_AtsIdentAgentSerialNumber_Object = MibScalar
atsIdentAgentSerialNumber = _AtsIdentAgentSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 1, 13),
    _AtsIdentAgentSerialNumber_Type()
)
atsIdentAgentSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsIdentAgentSerialNumber.setStatus("mandatory")
_AtsStatus_ObjectIdentity = ObjectIdentity
atsStatus = _AtsStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 2)
)
_AtsStatusDevice_ObjectIdentity = ObjectIdentity
atsStatusDevice = _AtsStatusDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 2, 1)
)


class _AtsStatusCommStatus_Type(Integer32):
    """Custom type atsStatusCommStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("atsNeverDiscovered", 1),
          ("atsCommEstablished", 2),
          ("atsCommLost", 3))
    )


_AtsStatusCommStatus_Type.__name__ = "Integer32"
_AtsStatusCommStatus_Object = MibScalar
atsStatusCommStatus = _AtsStatusCommStatus_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 2, 1, 1),
    _AtsStatusCommStatus_Type()
)
atsStatusCommStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsStatusCommStatus.setStatus("mandatory")


class _AtsStatusSelectedSource_Type(Integer32):
    """Custom type atsStatusSelectedSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sourceA", 1),
          ("sourceB", 2))
    )


_AtsStatusSelectedSource_Type.__name__ = "Integer32"
_AtsStatusSelectedSource_Object = MibScalar
atsStatusSelectedSource = _AtsStatusSelectedSource_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 2, 1, 2),
    _AtsStatusSelectedSource_Type()
)
atsStatusSelectedSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsStatusSelectedSource.setStatus("mandatory")


class _AtsStatusRedundancyState_Type(Integer32):
    """Custom type atsStatusRedundancyState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("atsRedundancyLost", 1),
          ("atsFullyRedundant", 2))
    )


_AtsStatusRedundancyState_Type.__name__ = "Integer32"
_AtsStatusRedundancyState_Object = MibScalar
atsStatusRedundancyState = _AtsStatusRedundancyState_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 2, 1, 3),
    _AtsStatusRedundancyState_Type()
)
atsStatusRedundancyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsStatusRedundancyState.setStatus("mandatory")


class _AtsStatusPhaseSyncStatus_Type(Integer32):
    """Custom type atsStatusPhaseSyncStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inSync", 1),
          ("outOfSync", 2))
    )


_AtsStatusPhaseSyncStatus_Type.__name__ = "Integer32"
_AtsStatusPhaseSyncStatus_Object = MibScalar
atsStatusPhaseSyncStatus = _AtsStatusPhaseSyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 2, 1, 4),
    _AtsStatusPhaseSyncStatus_Type()
)
atsStatusPhaseSyncStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsStatusPhaseSyncStatus.setStatus("mandatory")


class _AtsStatusDevSourceRelayStatus_Type(Integer32):
    """Custom type atsStatusDevSourceRelayStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sourceRelayNormal", 1),
          ("sourceRelayFail", 2))
    )


_AtsStatusDevSourceRelayStatus_Type.__name__ = "Integer32"
_AtsStatusDevSourceRelayStatus_Object = MibScalar
atsStatusDevSourceRelayStatus = _AtsStatusDevSourceRelayStatus_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 2, 1, 5),
    _AtsStatusDevSourceRelayStatus_Type()
)
atsStatusDevSourceRelayStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsStatusDevSourceRelayStatus.setStatus("mandatory")


class _AtsStatusDevInRelayStatus_Type(Integer32):
    """Custom type atsStatusDevInRelayStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inputRelayNormal", 1),
          ("inputRelayFail", 2))
    )


_AtsStatusDevInRelayStatus_Type.__name__ = "Integer32"
_AtsStatusDevInRelayStatus_Object = MibScalar
atsStatusDevInRelayStatus = _AtsStatusDevInRelayStatus_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 2, 1, 6),
    _AtsStatusDevInRelayStatus_Type()
)
atsStatusDevInRelayStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsStatusDevInRelayStatus.setStatus("mandatory")


class _AtsStatusDevOutRelayStatus_Type(Integer32):
    """Custom type atsStatusDevOutRelayStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("outputRelayNormal", 1),
          ("outputRelayFail", 2))
    )


_AtsStatusDevOutRelayStatus_Type.__name__ = "Integer32"
_AtsStatusDevOutRelayStatus_Object = MibScalar
atsStatusDevOutRelayStatus = _AtsStatusDevOutRelayStatus_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 2, 1, 7),
    _AtsStatusDevOutRelayStatus_Type()
)
atsStatusDevOutRelayStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsStatusDevOutRelayStatus.setStatus("mandatory")


class _AtsStatusDevLCDCommStatus_Type(Integer32):
    """Custom type atsStatusDevLCDCommStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lcdCommNormal", 1),
          ("lcdCommFail", 2))
    )


_AtsStatusDevLCDCommStatus_Type.__name__ = "Integer32"
_AtsStatusDevLCDCommStatus_Object = MibScalar
atsStatusDevLCDCommStatus = _AtsStatusDevLCDCommStatus_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 2, 1, 8),
    _AtsStatusDevLCDCommStatus_Type()
)
atsStatusDevLCDCommStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsStatusDevLCDCommStatus.setStatus("mandatory")


class _AtsStatusDevDB9CommStatus_Type(Integer32):
    """Custom type atsStatusDevDB9CommStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("db9CommNormal", 1),
          ("db9CommFail", 2))
    )


_AtsStatusDevDB9CommStatus_Type.__name__ = "Integer32"
_AtsStatusDevDB9CommStatus_Object = MibScalar
atsStatusDevDB9CommStatus = _AtsStatusDevDB9CommStatus_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 2, 1, 9),
    _AtsStatusDevDB9CommStatus_Type()
)
atsStatusDevDB9CommStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsStatusDevDB9CommStatus.setStatus("mandatory")
_AtsStatusPowerSupplyTable_Object = MibTable
atsStatusPowerSupplyTable = _AtsStatusPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 2, 1, 10)
)
if mibBuilder.loadTexts:
    atsStatusPowerSupplyTable.setStatus("mandatory")
_AtsStatusPowerSupplyEntry_Object = MibTableRow
atsStatusPowerSupplyEntry = _AtsStatusPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 2, 1, 10, 1)
)
atsStatusPowerSupplyEntry.setIndexNames(
    (0, "CPS-MIB", "atsStatusPowerSupplyTableIndex"),
)
if mibBuilder.loadTexts:
    atsStatusPowerSupplyEntry.setStatus("mandatory")


class _AtsStatusPowerSupplyTableIndex_Type(Integer32):
    """Custom type atsStatusPowerSupplyTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AtsStatusPowerSupplyTableIndex_Type.__name__ = "Integer32"
_AtsStatusPowerSupplyTableIndex_Object = MibTableColumn
atsStatusPowerSupplyTableIndex = _AtsStatusPowerSupplyTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 2, 1, 10, 1, 1),
    _AtsStatusPowerSupplyTableIndex_Type()
)
atsStatusPowerSupplyTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsStatusPowerSupplyTableIndex.setStatus("mandatory")


class _AtsStatusPowerSupplyInputSource_Type(Integer32):
    """Custom type atsStatusPowerSupplyInputSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sourceA", 1),
          ("sourceB", 2))
    )


_AtsStatusPowerSupplyInputSource_Type.__name__ = "Integer32"
_AtsStatusPowerSupplyInputSource_Object = MibTableColumn
atsStatusPowerSupplyInputSource = _AtsStatusPowerSupplyInputSource_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 2, 1, 10, 1, 2),
    _AtsStatusPowerSupplyInputSource_Type()
)
atsStatusPowerSupplyInputSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsStatusPowerSupplyInputSource.setStatus("mandatory")


class _AtsStatusPowerSupply12VStatus_Type(Integer32):
    """Custom type atsStatusPowerSupply12VStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("powerSupplyOK", 1),
          ("powerSupplyFailure", 2))
    )


_AtsStatusPowerSupply12VStatus_Type.__name__ = "Integer32"
_AtsStatusPowerSupply12VStatus_Object = MibTableColumn
atsStatusPowerSupply12VStatus = _AtsStatusPowerSupply12VStatus_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 2, 1, 10, 1, 3),
    _AtsStatusPowerSupply12VStatus_Type()
)
atsStatusPowerSupply12VStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsStatusPowerSupply12VStatus.setStatus("mandatory")


class _AtsStatusPowerSupply5VStatus_Type(Integer32):
    """Custom type atsStatusPowerSupply5VStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("powerSupplyOK", 1),
          ("powerSupplyFailure", 2))
    )


_AtsStatusPowerSupply5VStatus_Type.__name__ = "Integer32"
_AtsStatusPowerSupply5VStatus_Object = MibTableColumn
atsStatusPowerSupply5VStatus = _AtsStatusPowerSupply5VStatus_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 2, 1, 10, 1, 4),
    _AtsStatusPowerSupply5VStatus_Type()
)
atsStatusPowerSupply5VStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsStatusPowerSupply5VStatus.setStatus("mandatory")


class _AtsStatusPowerSupply3p3VStatus_Type(Integer32):
    """Custom type atsStatusPowerSupply3p3VStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("powerSupplyOK", 1),
          ("powerSupplyFailure", 2))
    )


_AtsStatusPowerSupply3p3VStatus_Type.__name__ = "Integer32"
_AtsStatusPowerSupply3p3VStatus_Object = MibTableColumn
atsStatusPowerSupply3p3VStatus = _AtsStatusPowerSupply3p3VStatus_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 2, 1, 10, 1, 5),
    _AtsStatusPowerSupply3p3VStatus_Type()
)
atsStatusPowerSupply3p3VStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsStatusPowerSupply3p3VStatus.setStatus("mandatory")
_AtsStatusInput_ObjectIdentity = ObjectIdentity
atsStatusInput = _AtsStatusInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 2, 2)
)
_AtsStatusInputNum_Type = Integer32
_AtsStatusInputNum_Object = MibScalar
atsStatusInputNum = _AtsStatusInputNum_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 2, 2, 1),
    _AtsStatusInputNum_Type()
)
atsStatusInputNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsStatusInputNum.setStatus("mandatory")
_AtsStatusInputTable_Object = MibTable
atsStatusInputTable = _AtsStatusInputTable_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 2, 2, 2)
)
if mibBuilder.loadTexts:
    atsStatusInputTable.setStatus("mandatory")
_AtsStatusInputEntry_Object = MibTableRow
atsStatusInputEntry = _AtsStatusInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 2, 2, 2, 1)
)
atsStatusInputEntry.setIndexNames(
    (0, "CPS-MIB", "atsStatusInputTableIndex"),
)
if mibBuilder.loadTexts:
    atsStatusInputEntry.setStatus("mandatory")


class _AtsStatusInputTableIndex_Type(Integer32):
    """Custom type atsStatusInputTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AtsStatusInputTableIndex_Type.__name__ = "Integer32"
_AtsStatusInputTableIndex_Object = MibTableColumn
atsStatusInputTableIndex = _AtsStatusInputTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 2, 2, 2, 1, 1),
    _AtsStatusInputTableIndex_Type()
)
atsStatusInputTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsStatusInputTableIndex.setStatus("mandatory")
_AtsStatusInputName_Type = DisplayString
_AtsStatusInputName_Object = MibTableColumn
atsStatusInputName = _AtsStatusInputName_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 2, 2, 2, 1, 2),
    _AtsStatusInputName_Type()
)
atsStatusInputName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atsStatusInputName.setStatus("mandatory")
_AtsStatusNumInputPhase_Type = Integer32
_AtsStatusNumInputPhase_Object = MibTableColumn
atsStatusNumInputPhase = _AtsStatusNumInputPhase_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 2, 2, 2, 1, 3),
    _AtsStatusNumInputPhase_Type()
)
atsStatusNumInputPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsStatusNumInputPhase.setStatus("mandatory")


class _AtsStatusInputVoltageOrientation_Type(Integer32):
    """Custom type atsStatusInputVoltageOrientation based on Integer32"""
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
        *(("unknown", 1),
          ("singlePhase", 2),
          ("splitPhase", 3),
          ("threePhasePhaseToNeutral", 4),
          ("threePhasePhaseToPhase", 5))
    )


_AtsStatusInputVoltageOrientation_Type.__name__ = "Integer32"
_AtsStatusInputVoltageOrientation_Object = MibTableColumn
atsStatusInputVoltageOrientation = _AtsStatusInputVoltageOrientation_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 2, 2, 2, 1, 4),
    _AtsStatusInputVoltageOrientation_Type()
)
atsStatusInputVoltageOrientation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsStatusInputVoltageOrientation.setStatus("mandatory")
_AtsStatusInputVoltage_Type = Integer32
_AtsStatusInputVoltage_Object = MibTableColumn
atsStatusInputVoltage = _AtsStatusInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 2, 2, 2, 1, 5),
    _AtsStatusInputVoltage_Type()
)
atsStatusInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsStatusInputVoltage.setStatus("mandatory")
_AtsStatusInputFrequency_Type = Integer32
_AtsStatusInputFrequency_Object = MibTableColumn
atsStatusInputFrequency = _AtsStatusInputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 2, 2, 2, 1, 6),
    _AtsStatusInputFrequency_Type()
)
atsStatusInputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsStatusInputFrequency.setStatus("mandatory")


class _AtsStatusInputVolState_Type(Integer32):
    """Custom type atsStatusInputVolState based on Integer32"""
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
          ("overVoltage", 2),
          ("underVoltage", 3))
    )


_AtsStatusInputVolState_Type.__name__ = "Integer32"
_AtsStatusInputVolState_Object = MibTableColumn
atsStatusInputVolState = _AtsStatusInputVolState_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 2, 2, 2, 1, 7),
    _AtsStatusInputVolState_Type()
)
atsStatusInputVolState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsStatusInputVolState.setStatus("mandatory")


class _AtsStatusInputFreqState_Type(Integer32):
    """Custom type atsStatusInputFreqState based on Integer32"""
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
          ("overFrequency", 2),
          ("underFrequency", 3))
    )


_AtsStatusInputFreqState_Type.__name__ = "Integer32"
_AtsStatusInputFreqState_Object = MibTableColumn
atsStatusInputFreqState = _AtsStatusInputFreqState_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 2, 2, 2, 1, 8),
    _AtsStatusInputFreqState_Type()
)
atsStatusInputFreqState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsStatusInputFreqState.setStatus("mandatory")
_AtsStatusInputPhaseTable_Object = MibTable
atsStatusInputPhaseTable = _AtsStatusInputPhaseTable_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 2, 2, 3)
)
if mibBuilder.loadTexts:
    atsStatusInputPhaseTable.setStatus("mandatory")
_AtsStatusInputPhaseEntry_Object = MibTableRow
atsStatusInputPhaseEntry = _AtsStatusInputPhaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 2, 2, 3, 1)
)
atsStatusInputPhaseEntry.setIndexNames(
    (0, "CPS-MIB", "atsStatusInputPhaseTableIndex"),
    (0, "CPS-MIB", "atsStatusInputPhaseIndex"),
)
if mibBuilder.loadTexts:
    atsStatusInputPhaseEntry.setStatus("mandatory")


class _AtsStatusInputPhaseTableIndex_Type(Integer32):
    """Custom type atsStatusInputPhaseTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AtsStatusInputPhaseTableIndex_Type.__name__ = "Integer32"
_AtsStatusInputPhaseTableIndex_Object = MibTableColumn
atsStatusInputPhaseTableIndex = _AtsStatusInputPhaseTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 2, 2, 3, 1, 1),
    _AtsStatusInputPhaseTableIndex_Type()
)
atsStatusInputPhaseTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsStatusInputPhaseTableIndex.setStatus("mandatory")


class _AtsStatusInputPhaseIndex_Type(Integer32):
    """Custom type atsStatusInputPhaseIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AtsStatusInputPhaseIndex_Type.__name__ = "Integer32"
_AtsStatusInputPhaseIndex_Object = MibTableColumn
atsStatusInputPhaseIndex = _AtsStatusInputPhaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 2, 2, 3, 1, 2),
    _AtsStatusInputPhaseIndex_Type()
)
atsStatusInputPhaseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsStatusInputPhaseIndex.setStatus("mandatory")
_AtsStatusInputPhaseVoltage_Type = Integer32
_AtsStatusInputPhaseVoltage_Object = MibTableColumn
atsStatusInputPhaseVoltage = _AtsStatusInputPhaseVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 2, 2, 3, 1, 3),
    _AtsStatusInputPhaseVoltage_Type()
)
atsStatusInputPhaseVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsStatusInputPhaseVoltage.setStatus("mandatory")
_AtsStatusInputPhaseCurrent_Type = Integer32
_AtsStatusInputPhaseCurrent_Object = MibTableColumn
atsStatusInputPhaseCurrent = _AtsStatusInputPhaseCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 2, 2, 3, 1, 4),
    _AtsStatusInputPhaseCurrent_Type()
)
atsStatusInputPhaseCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsStatusInputPhaseCurrent.setStatus("mandatory")
_AtsStatusInputPhasePower_Type = Integer32
_AtsStatusInputPhasePower_Object = MibTableColumn
atsStatusInputPhasePower = _AtsStatusInputPhasePower_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 2, 2, 3, 1, 5),
    _AtsStatusInputPhasePower_Type()
)
atsStatusInputPhasePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsStatusInputPhasePower.setStatus("mandatory")
_AtsConfig_ObjectIdentity = ObjectIdentity
atsConfig = _AtsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 3)
)


class _AtsConfigPreferredSource_Type(Integer32):
    """Custom type atsConfigPreferredSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sourceA", 1),
          ("sourceB", 2),
          ("none", 3))
    )


_AtsConfigPreferredSource_Type.__name__ = "Integer32"
_AtsConfigPreferredSource_Object = MibScalar
atsConfigPreferredSource = _AtsConfigPreferredSource_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 3, 1),
    _AtsConfigPreferredSource_Type()
)
atsConfigPreferredSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atsConfigPreferredSource.setStatus("mandatory")
_AtsConfigNominalVoltage_Type = Integer32
_AtsConfigNominalVoltage_Object = MibScalar
atsConfigNominalVoltage = _AtsConfigNominalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 3, 2),
    _AtsConfigNominalVoltage_Type()
)
atsConfigNominalVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atsConfigNominalVoltage.setStatus("mandatory")


class _AtsConfigVoltageSensitivity_Type(Integer32):
    """Custom type atsConfigVoltageSensitivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("medium", 2),
          ("low", 3))
    )


_AtsConfigVoltageSensitivity_Type.__name__ = "Integer32"
_AtsConfigVoltageSensitivity_Object = MibScalar
atsConfigVoltageSensitivity = _AtsConfigVoltageSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 3, 3),
    _AtsConfigVoltageSensitivity_Type()
)
atsConfigVoltageSensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atsConfigVoltageSensitivity.setStatus("mandatory")


class _AtsConfigTransferVoltageRange_Type(Integer32):
    """Custom type atsConfigTransferVoltageRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("wide", 1),
          ("medium", 2),
          ("narrow", 3))
    )


_AtsConfigTransferVoltageRange_Type.__name__ = "Integer32"
_AtsConfigTransferVoltageRange_Object = MibScalar
atsConfigTransferVoltageRange = _AtsConfigTransferVoltageRange_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 3, 4),
    _AtsConfigTransferVoltageRange_Type()
)
atsConfigTransferVoltageRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atsConfigTransferVoltageRange.setStatus("mandatory")
_AtsConfigNarrowRangeValue_Type = Integer32
_AtsConfigNarrowRangeValue_Object = MibScalar
atsConfigNarrowRangeValue = _AtsConfigNarrowRangeValue_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 3, 5),
    _AtsConfigNarrowRangeValue_Type()
)
atsConfigNarrowRangeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atsConfigNarrowRangeValue.setStatus("mandatory")
_AtsConfigMediumRangeValue_Type = Integer32
_AtsConfigMediumRangeValue_Object = MibScalar
atsConfigMediumRangeValue = _AtsConfigMediumRangeValue_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 3, 6),
    _AtsConfigMediumRangeValue_Type()
)
atsConfigMediumRangeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atsConfigMediumRangeValue.setStatus("mandatory")
_AtsConfigWideRangeValue_Type = Integer32
_AtsConfigWideRangeValue_Object = MibScalar
atsConfigWideRangeValue = _AtsConfigWideRangeValue_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 3, 7),
    _AtsConfigWideRangeValue_Type()
)
atsConfigWideRangeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atsConfigWideRangeValue.setStatus("mandatory")


class _AtsConfigFrequencyDeviation_Type(Integer32):
    """Custom type atsConfigFrequencyDeviation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_AtsConfigFrequencyDeviation_Type.__name__ = "Integer32"
_AtsConfigFrequencyDeviation_Object = MibScalar
atsConfigFrequencyDeviation = _AtsConfigFrequencyDeviation_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 3, 8),
    _AtsConfigFrequencyDeviation_Type()
)
atsConfigFrequencyDeviation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atsConfigFrequencyDeviation.setStatus("mandatory")
_AtsConfigDevLCDOffTime_Type = Integer32
_AtsConfigDevLCDOffTime_Object = MibScalar
atsConfigDevLCDOffTime = _AtsConfigDevLCDOffTime_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 3, 9),
    _AtsConfigDevLCDOffTime_Type()
)
atsConfigDevLCDOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atsConfigDevLCDOffTime.setStatus("mandatory")
_AtsControl_ObjectIdentity = ObjectIdentity
atsControl = _AtsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 4)
)


class _AtsCtrlResetATS_Type(Integer32):
    """Custom type atsCtrlResetATS based on Integer32"""
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
          ("rboot", 2),
          ("reset", 3))
    )


_AtsCtrlResetATS_Type.__name__ = "Integer32"
_AtsCtrlResetATS_Object = MibScalar
atsCtrlResetATS = _AtsCtrlResetATS_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 4, 1),
    _AtsCtrlResetATS_Type()
)
atsCtrlResetATS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atsCtrlResetATS.setStatus("mandatory")


class _AtsCtrlClearEventCounts_Type(Integer32):
    """Custom type atsCtrlClearEventCounts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("clear", 2))
    )


_AtsCtrlClearEventCounts_Type.__name__ = "Integer32"
_AtsCtrlClearEventCounts_Object = MibScalar
atsCtrlClearEventCounts = _AtsCtrlClearEventCounts_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 4, 2),
    _AtsCtrlClearEventCounts_Type()
)
atsCtrlClearEventCounts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atsCtrlClearEventCounts.setStatus("mandatory")
_AtsLoad_ObjectIdentity = ObjectIdentity
atsLoad = _AtsLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 5)
)
_AtsLoadDevice_ObjectIdentity = ObjectIdentity
atsLoadDevice = _AtsLoadDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 5, 1)
)
_AtsLoadDevPhaseTableSize_Type = Integer32
_AtsLoadDevPhaseTableSize_Object = MibScalar
atsLoadDevPhaseTableSize = _AtsLoadDevPhaseTableSize_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 5, 1, 1),
    _AtsLoadDevPhaseTableSize_Type()
)
atsLoadDevPhaseTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsLoadDevPhaseTableSize.setStatus("mandatory")
_AtsLoadDevPhaseTable_Object = MibTable
atsLoadDevPhaseTable = _AtsLoadDevPhaseTable_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 5, 1, 2)
)
if mibBuilder.loadTexts:
    atsLoadDevPhaseTable.setStatus("mandatory")
_AtsLoadDevPhaseEntry_Object = MibTableRow
atsLoadDevPhaseEntry = _AtsLoadDevPhaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 5, 1, 2, 1)
)
atsLoadDevPhaseEntry.setIndexNames(
    (0, "CPS-MIB", "atsLoadDevPhaseTableIndex"),
)
if mibBuilder.loadTexts:
    atsLoadDevPhaseEntry.setStatus("mandatory")


class _AtsLoadDevPhaseTableIndex_Type(Integer32):
    """Custom type atsLoadDevPhaseTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AtsLoadDevPhaseTableIndex_Type.__name__ = "Integer32"
_AtsLoadDevPhaseTableIndex_Object = MibTableColumn
atsLoadDevPhaseTableIndex = _AtsLoadDevPhaseTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 5, 1, 2, 1, 1),
    _AtsLoadDevPhaseTableIndex_Type()
)
atsLoadDevPhaseTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsLoadDevPhaseTableIndex.setStatus("mandatory")


class _AtsLoadDevPhase_Type(Integer32):
    """Custom type atsLoadDevPhase based on Integer32"""
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
        *(("phase1", 1),
          ("phase2", 2),
          ("phase3", 3),
          ("phase1-2", 4),
          ("phase2-3", 5),
          ("phase3-1", 6))
    )


_AtsLoadDevPhase_Type.__name__ = "Integer32"
_AtsLoadDevPhase_Object = MibTableColumn
atsLoadDevPhase = _AtsLoadDevPhase_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 5, 1, 2, 1, 2),
    _AtsLoadDevPhase_Type()
)
atsLoadDevPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsLoadDevPhase.setStatus("mandatory")
_AtsLoadDevPhaseMaxLoad_Type = Integer32
_AtsLoadDevPhaseMaxLoad_Object = MibTableColumn
atsLoadDevPhaseMaxLoad = _AtsLoadDevPhaseMaxLoad_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 5, 1, 2, 1, 3),
    _AtsLoadDevPhaseMaxLoad_Type()
)
atsLoadDevPhaseMaxLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsLoadDevPhaseMaxLoad.setStatus("mandatory")
_AtsLoadDevBankTableSize_Type = Integer32
_AtsLoadDevBankTableSize_Object = MibScalar
atsLoadDevBankTableSize = _AtsLoadDevBankTableSize_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 5, 1, 3),
    _AtsLoadDevBankTableSize_Type()
)
atsLoadDevBankTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsLoadDevBankTableSize.setStatus("mandatory")
_AtsLoadDevBankTable_Object = MibTable
atsLoadDevBankTable = _AtsLoadDevBankTable_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 5, 1, 4)
)
if mibBuilder.loadTexts:
    atsLoadDevBankTable.setStatus("mandatory")
_AtsLoadDevBankEntry_Object = MibTableRow
atsLoadDevBankEntry = _AtsLoadDevBankEntry_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 5, 1, 4, 1)
)
atsLoadDevBankEntry.setIndexNames(
    (0, "CPS-MIB", "atsLoadDevBankTableIndex"),
)
if mibBuilder.loadTexts:
    atsLoadDevBankEntry.setStatus("mandatory")


class _AtsLoadDevBankTableIndex_Type(Integer32):
    """Custom type atsLoadDevBankTableIndex based on Integer32"""
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
        *(("total", 1),
          ("bank1", 2),
          ("bank2", 3),
          ("bank3", 4))
    )


_AtsLoadDevBankTableIndex_Type.__name__ = "Integer32"
_AtsLoadDevBankTableIndex_Object = MibTableColumn
atsLoadDevBankTableIndex = _AtsLoadDevBankTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 5, 1, 4, 1, 1),
    _AtsLoadDevBankTableIndex_Type()
)
atsLoadDevBankTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsLoadDevBankTableIndex.setStatus("mandatory")
_AtsLoadDevBankMaxLoad_Type = Integer32
_AtsLoadDevBankMaxLoad_Object = MibTableColumn
atsLoadDevBankMaxLoad = _AtsLoadDevBankMaxLoad_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 5, 1, 4, 1, 2),
    _AtsLoadDevBankMaxLoad_Type()
)
atsLoadDevBankMaxLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsLoadDevBankMaxLoad.setStatus("mandatory")
_AtsLoadStatus_ObjectIdentity = ObjectIdentity
atsLoadStatus = _AtsLoadStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 5, 2)
)
_AtsLoadStatusPhaseTableSize_Type = Integer32
_AtsLoadStatusPhaseTableSize_Object = MibScalar
atsLoadStatusPhaseTableSize = _AtsLoadStatusPhaseTableSize_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 5, 2, 1),
    _AtsLoadStatusPhaseTableSize_Type()
)
atsLoadStatusPhaseTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsLoadStatusPhaseTableSize.setStatus("mandatory")
_AtsLoadStatusPhaseTable_Object = MibTable
atsLoadStatusPhaseTable = _AtsLoadStatusPhaseTable_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 5, 2, 2)
)
if mibBuilder.loadTexts:
    atsLoadStatusPhaseTable.setStatus("mandatory")
_AtsLoadStatusPhaseEntry_Object = MibTableRow
atsLoadStatusPhaseEntry = _AtsLoadStatusPhaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 5, 2, 2, 1)
)
atsLoadStatusPhaseEntry.setIndexNames(
    (0, "CPS-MIB", "atsLoadStatusPhaseTableIndex"),
)
if mibBuilder.loadTexts:
    atsLoadStatusPhaseEntry.setStatus("mandatory")


class _AtsLoadStatusPhaseTableIndex_Type(Integer32):
    """Custom type atsLoadStatusPhaseTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AtsLoadStatusPhaseTableIndex_Type.__name__ = "Integer32"
_AtsLoadStatusPhaseTableIndex_Object = MibTableColumn
atsLoadStatusPhaseTableIndex = _AtsLoadStatusPhaseTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 5, 2, 2, 1, 1),
    _AtsLoadStatusPhaseTableIndex_Type()
)
atsLoadStatusPhaseTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsLoadStatusPhaseTableIndex.setStatus("mandatory")


class _AtsLoadStatusPhase_Type(Integer32):
    """Custom type atsLoadStatusPhase based on Integer32"""
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
        *(("phase1", 1),
          ("phase2", 2),
          ("phase3", 3),
          ("phase1-2", 4),
          ("phase2-3", 5),
          ("phase3-1", 6))
    )


_AtsLoadStatusPhase_Type.__name__ = "Integer32"
_AtsLoadStatusPhase_Object = MibTableColumn
atsLoadStatusPhase = _AtsLoadStatusPhase_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 5, 2, 2, 1, 2),
    _AtsLoadStatusPhase_Type()
)
atsLoadStatusPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsLoadStatusPhase.setStatus("mandatory")
_AtsLoadStatusPhaseLoad_Type = Integer32
_AtsLoadStatusPhaseLoad_Object = MibTableColumn
atsLoadStatusPhaseLoad = _AtsLoadStatusPhaseLoad_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 5, 2, 2, 1, 3),
    _AtsLoadStatusPhaseLoad_Type()
)
atsLoadStatusPhaseLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsLoadStatusPhaseLoad.setStatus("mandatory")


class _AtsLoadStatusPhaseLoadState_Type(Integer32):
    """Custom type atsLoadStatusPhaseLoadState based on Integer32"""
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
        *(("normal", 1),
          ("lowLoad", 2),
          ("nearOverLoad", 3),
          ("overLoad", 4))
    )


_AtsLoadStatusPhaseLoadState_Type.__name__ = "Integer32"
_AtsLoadStatusPhaseLoadState_Object = MibTableColumn
atsLoadStatusPhaseLoadState = _AtsLoadStatusPhaseLoadState_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 5, 2, 2, 1, 4),
    _AtsLoadStatusPhaseLoadState_Type()
)
atsLoadStatusPhaseLoadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsLoadStatusPhaseLoadState.setStatus("mandatory")
_AtsLoadStatusPhasePower_Type = Integer32
_AtsLoadStatusPhasePower_Object = MibTableColumn
atsLoadStatusPhasePower = _AtsLoadStatusPhasePower_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 5, 2, 2, 1, 5),
    _AtsLoadStatusPhasePower_Type()
)
atsLoadStatusPhasePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsLoadStatusPhasePower.setStatus("mandatory")
_AtsLoadStatusBankTableSize_Type = Integer32
_AtsLoadStatusBankTableSize_Object = MibScalar
atsLoadStatusBankTableSize = _AtsLoadStatusBankTableSize_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 5, 2, 3),
    _AtsLoadStatusBankTableSize_Type()
)
atsLoadStatusBankTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsLoadStatusBankTableSize.setStatus("mandatory")
_AtsLoadStatusBankTable_Object = MibTable
atsLoadStatusBankTable = _AtsLoadStatusBankTable_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 5, 2, 4)
)
if mibBuilder.loadTexts:
    atsLoadStatusBankTable.setStatus("mandatory")
_AtsLoadStatusBankEntry_Object = MibTableRow
atsLoadStatusBankEntry = _AtsLoadStatusBankEntry_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 5, 2, 4, 1)
)
atsLoadStatusBankEntry.setIndexNames(
    (0, "CPS-MIB", "atsLoadStatusBankTableIndex"),
)
if mibBuilder.loadTexts:
    atsLoadStatusBankEntry.setStatus("mandatory")


class _AtsLoadStatusBankTableIndex_Type(Integer32):
    """Custom type atsLoadStatusBankTableIndex based on Integer32"""
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
        *(("total", 1),
          ("bank1", 2),
          ("bank2", 3),
          ("bank3", 4))
    )


_AtsLoadStatusBankTableIndex_Type.__name__ = "Integer32"
_AtsLoadStatusBankTableIndex_Object = MibTableColumn
atsLoadStatusBankTableIndex = _AtsLoadStatusBankTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 5, 2, 4, 1, 1),
    _AtsLoadStatusBankTableIndex_Type()
)
atsLoadStatusBankTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsLoadStatusBankTableIndex.setStatus("mandatory")


class _AtsLoadStatusBankPhase_Type(Integer32):
    """Custom type atsLoadStatusBankPhase based on Integer32"""
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
        *(("phase1", 1),
          ("phase2", 2),
          ("phase3", 3),
          ("phase1-2", 4),
          ("phase2-3", 5),
          ("phase3-1", 6))
    )


_AtsLoadStatusBankPhase_Type.__name__ = "Integer32"
_AtsLoadStatusBankPhase_Object = MibTableColumn
atsLoadStatusBankPhase = _AtsLoadStatusBankPhase_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 5, 2, 4, 1, 2),
    _AtsLoadStatusBankPhase_Type()
)
atsLoadStatusBankPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsLoadStatusBankPhase.setStatus("mandatory")
_AtsLoadStatusBankLoad_Type = Integer32
_AtsLoadStatusBankLoad_Object = MibTableColumn
atsLoadStatusBankLoad = _AtsLoadStatusBankLoad_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 5, 2, 4, 1, 3),
    _AtsLoadStatusBankLoad_Type()
)
atsLoadStatusBankLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsLoadStatusBankLoad.setStatus("mandatory")


class _AtsLoadStatusBankLoadState_Type(Integer32):
    """Custom type atsLoadStatusBankLoadState based on Integer32"""
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
        *(("normal", 1),
          ("lowLoad", 2),
          ("nearOverLoad", 3),
          ("overLoad", 4))
    )


_AtsLoadStatusBankLoadState_Type.__name__ = "Integer32"
_AtsLoadStatusBankLoadState_Object = MibTableColumn
atsLoadStatusBankLoadState = _AtsLoadStatusBankLoadState_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 5, 2, 4, 1, 4),
    _AtsLoadStatusBankLoadState_Type()
)
atsLoadStatusBankLoadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsLoadStatusBankLoadState.setStatus("mandatory")
_AtsLoadStatusBankPower_Type = Integer32
_AtsLoadStatusBankPower_Object = MibTableColumn
atsLoadStatusBankPower = _AtsLoadStatusBankPower_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 5, 2, 4, 1, 5),
    _AtsLoadStatusBankPower_Type()
)
atsLoadStatusBankPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsLoadStatusBankPower.setStatus("mandatory")
_AtsLoadStatusBankEnergy_Type = Integer32
_AtsLoadStatusBankEnergy_Object = MibTableColumn
atsLoadStatusBankEnergy = _AtsLoadStatusBankEnergy_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 5, 2, 4, 1, 6),
    _AtsLoadStatusBankEnergy_Type()
)
atsLoadStatusBankEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsLoadStatusBankEnergy.setStatus("mandatory")
_AtsLoadStatusBankStartTime_Type = Integer32
_AtsLoadStatusBankStartTime_Object = MibTableColumn
atsLoadStatusBankStartTime = _AtsLoadStatusBankStartTime_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 5, 2, 4, 1, 7),
    _AtsLoadStatusBankStartTime_Type()
)
atsLoadStatusBankStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsLoadStatusBankStartTime.setStatus("mandatory")
_AtsLoadConfig_ObjectIdentity = ObjectIdentity
atsLoadConfig = _AtsLoadConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 5, 3)
)
_AtsLoadCfgPhaseTableSize_Type = Integer32
_AtsLoadCfgPhaseTableSize_Object = MibScalar
atsLoadCfgPhaseTableSize = _AtsLoadCfgPhaseTableSize_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 5, 3, 1),
    _AtsLoadCfgPhaseTableSize_Type()
)
atsLoadCfgPhaseTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsLoadCfgPhaseTableSize.setStatus("mandatory")
_AtsLoadCfgPhaseTable_Object = MibTable
atsLoadCfgPhaseTable = _AtsLoadCfgPhaseTable_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 5, 3, 2)
)
if mibBuilder.loadTexts:
    atsLoadCfgPhaseTable.setStatus("mandatory")
_AtsLoadCfgPhaseEntry_Object = MibTableRow
atsLoadCfgPhaseEntry = _AtsLoadCfgPhaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 5, 3, 2, 1)
)
atsLoadCfgPhaseEntry.setIndexNames(
    (0, "CPS-MIB", "atsLoadCfgPhaseTableIndex"),
)
if mibBuilder.loadTexts:
    atsLoadCfgPhaseEntry.setStatus("mandatory")


class _AtsLoadCfgPhaseTableIndex_Type(Integer32):
    """Custom type atsLoadCfgPhaseTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AtsLoadCfgPhaseTableIndex_Type.__name__ = "Integer32"
_AtsLoadCfgPhaseTableIndex_Object = MibTableColumn
atsLoadCfgPhaseTableIndex = _AtsLoadCfgPhaseTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 5, 3, 2, 1, 1),
    _AtsLoadCfgPhaseTableIndex_Type()
)
atsLoadCfgPhaseTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsLoadCfgPhaseTableIndex.setStatus("mandatory")


class _AtsLoadCfgPhase_Type(Integer32):
    """Custom type atsLoadCfgPhase based on Integer32"""
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
        *(("phase1", 1),
          ("phase2", 2),
          ("phase3", 3),
          ("phase1-2", 4),
          ("phase2-3", 5),
          ("phase3-1", 6))
    )


_AtsLoadCfgPhase_Type.__name__ = "Integer32"
_AtsLoadCfgPhase_Object = MibTableColumn
atsLoadCfgPhase = _AtsLoadCfgPhase_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 5, 3, 2, 1, 2),
    _AtsLoadCfgPhase_Type()
)
atsLoadCfgPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsLoadCfgPhase.setStatus("mandatory")
_AtsLoadCfgPhaseLowLoad_Type = Integer32
_AtsLoadCfgPhaseLowLoad_Object = MibTableColumn
atsLoadCfgPhaseLowLoad = _AtsLoadCfgPhaseLowLoad_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 5, 3, 2, 1, 3),
    _AtsLoadCfgPhaseLowLoad_Type()
)
atsLoadCfgPhaseLowLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atsLoadCfgPhaseLowLoad.setStatus("mandatory")
_AtsLoadCfgPhaseNearOverLoad_Type = Integer32
_AtsLoadCfgPhaseNearOverLoad_Object = MibTableColumn
atsLoadCfgPhaseNearOverLoad = _AtsLoadCfgPhaseNearOverLoad_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 5, 3, 2, 1, 4),
    _AtsLoadCfgPhaseNearOverLoad_Type()
)
atsLoadCfgPhaseNearOverLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atsLoadCfgPhaseNearOverLoad.setStatus("mandatory")
_AtsLoadCfgPhaseOverLoad_Type = Integer32
_AtsLoadCfgPhaseOverLoad_Object = MibTableColumn
atsLoadCfgPhaseOverLoad = _AtsLoadCfgPhaseOverLoad_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 5, 3, 2, 1, 5),
    _AtsLoadCfgPhaseOverLoad_Type()
)
atsLoadCfgPhaseOverLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atsLoadCfgPhaseOverLoad.setStatus("mandatory")


class _AtsLoadCfgPhaseOutletRestriction_Type(Integer32):
    """Custom type atsLoadCfgPhaseOutletRestriction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alwaysAllowTurnON", 1),
          ("restrictOnNearOverload", 2),
          ("restrictOnOverload", 3))
    )


_AtsLoadCfgPhaseOutletRestriction_Type.__name__ = "Integer32"
_AtsLoadCfgPhaseOutletRestriction_Object = MibTableColumn
atsLoadCfgPhaseOutletRestriction = _AtsLoadCfgPhaseOutletRestriction_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 5, 3, 2, 1, 6),
    _AtsLoadCfgPhaseOutletRestriction_Type()
)
atsLoadCfgPhaseOutletRestriction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atsLoadCfgPhaseOutletRestriction.setStatus("mandatory")
_AtsLoadCfgBankTableSize_Type = Integer32
_AtsLoadCfgBankTableSize_Object = MibScalar
atsLoadCfgBankTableSize = _AtsLoadCfgBankTableSize_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 5, 3, 3),
    _AtsLoadCfgBankTableSize_Type()
)
atsLoadCfgBankTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsLoadCfgBankTableSize.setStatus("mandatory")
_AtsLoadCfgBankTable_Object = MibTable
atsLoadCfgBankTable = _AtsLoadCfgBankTable_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 5, 3, 4)
)
if mibBuilder.loadTexts:
    atsLoadCfgBankTable.setStatus("mandatory")
_AtsLoadCfgBankEntry_Object = MibTableRow
atsLoadCfgBankEntry = _AtsLoadCfgBankEntry_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 5, 3, 4, 1)
)
atsLoadCfgBankEntry.setIndexNames(
    (0, "CPS-MIB", "atsLoadCfgBankTableIndex"),
)
if mibBuilder.loadTexts:
    atsLoadCfgBankEntry.setStatus("mandatory")


class _AtsLoadCfgBankTableIndex_Type(Integer32):
    """Custom type atsLoadCfgBankTableIndex based on Integer32"""
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
        *(("total", 1),
          ("bank1", 2),
          ("bank2", 3),
          ("bank3", 4))
    )


_AtsLoadCfgBankTableIndex_Type.__name__ = "Integer32"
_AtsLoadCfgBankTableIndex_Object = MibTableColumn
atsLoadCfgBankTableIndex = _AtsLoadCfgBankTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 5, 3, 4, 1, 1),
    _AtsLoadCfgBankTableIndex_Type()
)
atsLoadCfgBankTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsLoadCfgBankTableIndex.setStatus("mandatory")
_AtsLoadCfgBankLowLoad_Type = Integer32
_AtsLoadCfgBankLowLoad_Object = MibTableColumn
atsLoadCfgBankLowLoad = _AtsLoadCfgBankLowLoad_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 5, 3, 4, 1, 2),
    _AtsLoadCfgBankLowLoad_Type()
)
atsLoadCfgBankLowLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atsLoadCfgBankLowLoad.setStatus("mandatory")
_AtsLoadCfgBankNearOverLoad_Type = Integer32
_AtsLoadCfgBankNearOverLoad_Object = MibTableColumn
atsLoadCfgBankNearOverLoad = _AtsLoadCfgBankNearOverLoad_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 5, 3, 4, 1, 3),
    _AtsLoadCfgBankNearOverLoad_Type()
)
atsLoadCfgBankNearOverLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atsLoadCfgBankNearOverLoad.setStatus("mandatory")
_AtsLoadCfgBankOverLoad_Type = Integer32
_AtsLoadCfgBankOverLoad_Object = MibTableColumn
atsLoadCfgBankOverLoad = _AtsLoadCfgBankOverLoad_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 5, 3, 4, 1, 4),
    _AtsLoadCfgBankOverLoad_Type()
)
atsLoadCfgBankOverLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atsLoadCfgBankOverLoad.setStatus("mandatory")


class _AtsLoadCfgBankOutletRestriction_Type(Integer32):
    """Custom type atsLoadCfgBankOutletRestriction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alwaysAllowTurnON", 1),
          ("restrictOnNearOverload", 2),
          ("restrictOnOverload", 3))
    )


_AtsLoadCfgBankOutletRestriction_Type.__name__ = "Integer32"
_AtsLoadCfgBankOutletRestriction_Object = MibTableColumn
atsLoadCfgBankOutletRestriction = _AtsLoadCfgBankOutletRestriction_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 5, 3, 4, 1, 5),
    _AtsLoadCfgBankOutletRestriction_Type()
)
atsLoadCfgBankOutletRestriction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atsLoadCfgBankOutletRestriction.setStatus("mandatory")
_AtsOutlet_ObjectIdentity = ObjectIdentity
atsOutlet = _AtsOutlet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 6)
)
_AtsOutletDevice_ObjectIdentity = ObjectIdentity
atsOutletDevice = _AtsOutletDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 6, 1)
)
_AtsOutletDevTotalOutletNum_Type = Integer32
_AtsOutletDevTotalOutletNum_Object = MibScalar
atsOutletDevTotalOutletNum = _AtsOutletDevTotalOutletNum_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 6, 1, 1),
    _AtsOutletDevTotalOutletNum_Type()
)
atsOutletDevTotalOutletNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsOutletDevTotalOutletNum.setStatus("mandatory")
_AtsOutletDevCtrlOutletNum_Type = Integer32
_AtsOutletDevCtrlOutletNum_Object = MibScalar
atsOutletDevCtrlOutletNum = _AtsOutletDevCtrlOutletNum_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 6, 1, 2),
    _AtsOutletDevCtrlOutletNum_Type()
)
atsOutletDevCtrlOutletNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsOutletDevCtrlOutletNum.setStatus("mandatory")
_AtsOutletDevColdStartDelay_Type = Integer32
_AtsOutletDevColdStartDelay_Object = MibScalar
atsOutletDevColdStartDelay = _AtsOutletDevColdStartDelay_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 6, 1, 3),
    _AtsOutletDevColdStartDelay_Type()
)
atsOutletDevColdStartDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atsOutletDevColdStartDelay.setStatus("mandatory")


class _AtsOutletDevColdStartState_Type(Integer32):
    """Custom type atsOutletDevColdStartState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allOn", 1),
          ("previous", 2))
    )


_AtsOutletDevColdStartState_Type.__name__ = "Integer32"
_AtsOutletDevColdStartState_Object = MibScalar
atsOutletDevColdStartState = _AtsOutletDevColdStartState_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 6, 1, 4),
    _AtsOutletDevColdStartState_Type()
)
atsOutletDevColdStartState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atsOutletDevColdStartState.setStatus("mandatory")


class _AtsOutletDevLocalCtrl_Type(Integer32):
    """Custom type atsOutletDevLocalCtrl based on Integer32"""
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


_AtsOutletDevLocalCtrl_Type.__name__ = "Integer32"
_AtsOutletDevLocalCtrl_Object = MibScalar
atsOutletDevLocalCtrl = _AtsOutletDevLocalCtrl_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 6, 1, 5),
    _AtsOutletDevLocalCtrl_Type()
)
atsOutletDevLocalCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atsOutletDevLocalCtrl.setStatus("mandatory")


class _AtsOutletDevCommand_Type(Integer32):
    """Custom type atsOutletDevCommand based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("noCommandAll", 1),
          ("immediateAllOn", 2),
          ("immediateAllOff", 3),
          ("immediateAllReboot", 4),
          ("delayedAllOn", 5),
          ("delayedAllOff", 6),
          ("delayedAllReboot", 7),
          ("cancelAllPendingCommands", 8))
    )


_AtsOutletDevCommand_Type.__name__ = "Integer32"
_AtsOutletDevCommand_Object = MibScalar
atsOutletDevCommand = _AtsOutletDevCommand_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 6, 1, 6),
    _AtsOutletDevCommand_Type()
)
atsOutletDevCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atsOutletDevCommand.setStatus("mandatory")
_AtsOutletStatusTableSize_Type = Integer32
_AtsOutletStatusTableSize_Object = MibScalar
atsOutletStatusTableSize = _AtsOutletStatusTableSize_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 6, 2),
    _AtsOutletStatusTableSize_Type()
)
atsOutletStatusTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsOutletStatusTableSize.setStatus("mandatory")
_AtsOutletStatusTable_Object = MibTable
atsOutletStatusTable = _AtsOutletStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 6, 3)
)
if mibBuilder.loadTexts:
    atsOutletStatusTable.setStatus("mandatory")
_AtsOutletStatusEntry_Object = MibTableRow
atsOutletStatusEntry = _AtsOutletStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 6, 3, 1)
)
atsOutletStatusEntry.setIndexNames(
    (0, "CPS-MIB", "atsOutletStatusTableIndex"),
)
if mibBuilder.loadTexts:
    atsOutletStatusEntry.setStatus("mandatory")


class _AtsOutletStatusTableIndex_Type(Integer32):
    """Custom type atsOutletStatusTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 19),
    )


_AtsOutletStatusTableIndex_Type.__name__ = "Integer32"
_AtsOutletStatusTableIndex_Object = MibTableColumn
atsOutletStatusTableIndex = _AtsOutletStatusTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 6, 3, 1, 1),
    _AtsOutletStatusTableIndex_Type()
)
atsOutletStatusTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsOutletStatusTableIndex.setStatus("mandatory")
_AtsOutletStatusOutletName_Type = DisplayString
_AtsOutletStatusOutletName_Object = MibTableColumn
atsOutletStatusOutletName = _AtsOutletStatusOutletName_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 6, 3, 1, 2),
    _AtsOutletStatusOutletName_Type()
)
atsOutletStatusOutletName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsOutletStatusOutletName.setStatus("mandatory")


class _AtsOutletStatusOutletState_Type(Integer32):
    """Custom type atsOutletStatusOutletState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("outletStatusOn", 1),
          ("outletStatusOff", 2))
    )


_AtsOutletStatusOutletState_Type.__name__ = "Integer32"
_AtsOutletStatusOutletState_Object = MibTableColumn
atsOutletStatusOutletState = _AtsOutletStatusOutletState_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 6, 3, 1, 3),
    _AtsOutletStatusOutletState_Type()
)
atsOutletStatusOutletState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsOutletStatusOutletState.setStatus("mandatory")


class _AtsOutletStatusOutletCmdPending_Type(Integer32):
    """Custom type atsOutletStatusOutletCmdPending based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("outletStatusCommandPending", 1),
          ("outletStatusNoCommandPending", 2))
    )


_AtsOutletStatusOutletCmdPending_Type.__name__ = "Integer32"
_AtsOutletStatusOutletCmdPending_Object = MibTableColumn
atsOutletStatusOutletCmdPending = _AtsOutletStatusOutletCmdPending_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 6, 3, 1, 4),
    _AtsOutletStatusOutletCmdPending_Type()
)
atsOutletStatusOutletCmdPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsOutletStatusOutletCmdPending.setStatus("mandatory")


class _AtsOutletStatusOutletPhase_Type(Integer32):
    """Custom type atsOutletStatusOutletPhase based on Integer32"""
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
        *(("phase1", 1),
          ("phase2", 2),
          ("phase3", 3),
          ("phase1-2", 4),
          ("phase2-3", 5),
          ("phase3-1", 6))
    )


_AtsOutletStatusOutletPhase_Type.__name__ = "Integer32"
_AtsOutletStatusOutletPhase_Object = MibTableColumn
atsOutletStatusOutletPhase = _AtsOutletStatusOutletPhase_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 6, 3, 1, 5),
    _AtsOutletStatusOutletPhase_Type()
)
atsOutletStatusOutletPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsOutletStatusOutletPhase.setStatus("mandatory")
_AtsOutletStatusOutletBank_Type = Integer32
_AtsOutletStatusOutletBank_Object = MibTableColumn
atsOutletStatusOutletBank = _AtsOutletStatusOutletBank_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 6, 3, 1, 6),
    _AtsOutletStatusOutletBank_Type()
)
atsOutletStatusOutletBank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsOutletStatusOutletBank.setStatus("mandatory")
_AtsOutletCtrlTableSize_Type = Integer32
_AtsOutletCtrlTableSize_Object = MibScalar
atsOutletCtrlTableSize = _AtsOutletCtrlTableSize_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 6, 4),
    _AtsOutletCtrlTableSize_Type()
)
atsOutletCtrlTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsOutletCtrlTableSize.setStatus("mandatory")
_AtsOutletCtrlTable_Object = MibTable
atsOutletCtrlTable = _AtsOutletCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 6, 5)
)
if mibBuilder.loadTexts:
    atsOutletCtrlTable.setStatus("mandatory")
_AtsOutletCtrlEntry_Object = MibTableRow
atsOutletCtrlEntry = _AtsOutletCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 6, 5, 1)
)
atsOutletCtrlEntry.setIndexNames(
    (0, "CPS-MIB", "atsOutletCtrlTableIndex"),
)
if mibBuilder.loadTexts:
    atsOutletCtrlEntry.setStatus("mandatory")


class _AtsOutletCtrlTableIndex_Type(Integer32):
    """Custom type atsOutletCtrlTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 19),
    )


_AtsOutletCtrlTableIndex_Type.__name__ = "Integer32"
_AtsOutletCtrlTableIndex_Object = MibTableColumn
atsOutletCtrlTableIndex = _AtsOutletCtrlTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 6, 5, 1, 1),
    _AtsOutletCtrlTableIndex_Type()
)
atsOutletCtrlTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsOutletCtrlTableIndex.setStatus("mandatory")
_AtsOutletCtrlOutletName_Type = DisplayString
_AtsOutletCtrlOutletName_Object = MibTableColumn
atsOutletCtrlOutletName = _AtsOutletCtrlOutletName_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 6, 5, 1, 2),
    _AtsOutletCtrlOutletName_Type()
)
atsOutletCtrlOutletName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsOutletCtrlOutletName.setStatus("mandatory")


class _AtsOutletCtrlCommand_Type(Integer32):
    """Custom type atsOutletCtrlCommand based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("immediateOn", 2),
          ("immediateOff", 3),
          ("immediateReboot", 4),
          ("delayedOn", 5),
          ("delayedOff", 6),
          ("delayedReboot", 7),
          ("cancelPendingCommand", 8))
    )


_AtsOutletCtrlCommand_Type.__name__ = "Integer32"
_AtsOutletCtrlCommand_Object = MibTableColumn
atsOutletCtrlCommand = _AtsOutletCtrlCommand_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 6, 5, 1, 3),
    _AtsOutletCtrlCommand_Type()
)
atsOutletCtrlCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atsOutletCtrlCommand.setStatus("mandatory")
_AtsOutletCfgTableSize_Type = Integer32
_AtsOutletCfgTableSize_Object = MibScalar
atsOutletCfgTableSize = _AtsOutletCfgTableSize_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 6, 6),
    _AtsOutletCfgTableSize_Type()
)
atsOutletCfgTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsOutletCfgTableSize.setStatus("mandatory")
_AtsOutletCfgTable_Object = MibTable
atsOutletCfgTable = _AtsOutletCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 6, 7)
)
if mibBuilder.loadTexts:
    atsOutletCfgTable.setStatus("mandatory")
_AtsOutletCfgEntry_Object = MibTableRow
atsOutletCfgEntry = _AtsOutletCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 6, 7, 1)
)
atsOutletCfgEntry.setIndexNames(
    (0, "CPS-MIB", "atsOutletCfgTableIndex"),
)
if mibBuilder.loadTexts:
    atsOutletCfgEntry.setStatus("mandatory")


class _AtsOutletCfgTableIndex_Type(Integer32):
    """Custom type atsOutletCfgTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 19),
    )


_AtsOutletCfgTableIndex_Type.__name__ = "Integer32"
_AtsOutletCfgTableIndex_Object = MibTableColumn
atsOutletCfgTableIndex = _AtsOutletCfgTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 6, 7, 1, 1),
    _AtsOutletCfgTableIndex_Type()
)
atsOutletCfgTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsOutletCfgTableIndex.setStatus("mandatory")
_AtsOutletCfgOutletName_Type = DisplayString
_AtsOutletCfgOutletName_Object = MibTableColumn
atsOutletCfgOutletName = _AtsOutletCfgOutletName_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 6, 7, 1, 2),
    _AtsOutletCfgOutletName_Type()
)
atsOutletCfgOutletName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atsOutletCfgOutletName.setStatus("mandatory")
_AtsOutletCfgPowerOnTime_Type = Integer32
_AtsOutletCfgPowerOnTime_Object = MibTableColumn
atsOutletCfgPowerOnTime = _AtsOutletCfgPowerOnTime_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 6, 7, 1, 3),
    _AtsOutletCfgPowerOnTime_Type()
)
atsOutletCfgPowerOnTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atsOutletCfgPowerOnTime.setStatus("mandatory")
_AtsOutletCfgPowerOffTime_Type = Integer32
_AtsOutletCfgPowerOffTime_Object = MibTableColumn
atsOutletCfgPowerOffTime = _AtsOutletCfgPowerOffTime_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 6, 7, 1, 4),
    _AtsOutletCfgPowerOffTime_Type()
)
atsOutletCfgPowerOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atsOutletCfgPowerOffTime.setStatus("mandatory")
_AtsOutletCfgRebootDuration_Type = Integer32
_AtsOutletCfgRebootDuration_Object = MibTableColumn
atsOutletCfgRebootDuration = _AtsOutletCfgRebootDuration_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 5, 6, 7, 1, 5),
    _AtsOutletCfgRebootDuration_Type()
)
atsOutletCfgRebootDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atsOutletCfgRebootDuration.setStatus("mandatory")
_EPDU2_ObjectIdentity = ObjectIdentity
ePDU2 = _EPDU2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6)
)


class _EPDU2Role_Type(Integer32):
    """Custom type ePDU2Role based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("standalone", 1),
          ("host", 2),
          ("slave", 3))
    )


_EPDU2Role_Type.__name__ = "Integer32"
_EPDU2Role_Object = MibScalar
ePDU2Role = _EPDU2Role_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 1),
    _EPDU2Role_Type()
)
ePDU2Role.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2Role.setStatus("mandatory")
_EPDU2Ident_ObjectIdentity = ObjectIdentity
ePDU2Ident = _EPDU2Ident_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 2)
)
_EPDU2IdentTableSize_Type = Integer32
_EPDU2IdentTableSize_Object = MibScalar
ePDU2IdentTableSize = _EPDU2IdentTableSize_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 2, 1),
    _EPDU2IdentTableSize_Type()
)
ePDU2IdentTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2IdentTableSize.setStatus("mandatory")
_EPDU2IdentTable_Object = MibTable
ePDU2IdentTable = _EPDU2IdentTable_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 2, 2)
)
if mibBuilder.loadTexts:
    ePDU2IdentTable.setStatus("mandatory")
_EPDU2IdentEntry_Object = MibTableRow
ePDU2IdentEntry = _EPDU2IdentEntry_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 2, 2, 1)
)
ePDU2IdentEntry.setIndexNames(
    (0, "CPS-MIB", "ePDU2IdentIndex"),
)
if mibBuilder.loadTexts:
    ePDU2IdentEntry.setStatus("mandatory")


class _EPDU2IdentIndex_Type(Integer32):
    """Custom type ePDU2IdentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_EPDU2IdentIndex_Type.__name__ = "Integer32"
_EPDU2IdentIndex_Object = MibTableColumn
ePDU2IdentIndex = _EPDU2IdentIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 2, 2, 1, 1),
    _EPDU2IdentIndex_Type()
)
ePDU2IdentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2IdentIndex.setStatus("mandatory")
_EPDU2IdentModuleIndex_Type = Integer32
_EPDU2IdentModuleIndex_Object = MibTableColumn
ePDU2IdentModuleIndex = _EPDU2IdentModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 2, 2, 1, 2),
    _EPDU2IdentModuleIndex_Type()
)
ePDU2IdentModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2IdentModuleIndex.setStatus("mandatory")
_EPDU2IdentName_Type = DisplayString
_EPDU2IdentName_Object = MibTableColumn
ePDU2IdentName = _EPDU2IdentName_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 2, 2, 1, 3),
    _EPDU2IdentName_Type()
)
ePDU2IdentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2IdentName.setStatus("mandatory")
_EPDU2IdentLocation_Type = DisplayString
_EPDU2IdentLocation_Object = MibTableColumn
ePDU2IdentLocation = _EPDU2IdentLocation_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 2, 2, 1, 4),
    _EPDU2IdentLocation_Type()
)
ePDU2IdentLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2IdentLocation.setStatus("mandatory")
_EPDU2IdentContact_Type = DisplayString
_EPDU2IdentContact_Object = MibTableColumn
ePDU2IdentContact = _EPDU2IdentContact_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 2, 2, 1, 5),
    _EPDU2IdentContact_Type()
)
ePDU2IdentContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2IdentContact.setStatus("mandatory")
_EPDU2IdentHardwareRev_Type = DisplayString
_EPDU2IdentHardwareRev_Object = MibTableColumn
ePDU2IdentHardwareRev = _EPDU2IdentHardwareRev_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 2, 2, 1, 6),
    _EPDU2IdentHardwareRev_Type()
)
ePDU2IdentHardwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2IdentHardwareRev.setStatus("mandatory")
_EPDU2IdentFirmwareRev_Type = DisplayString
_EPDU2IdentFirmwareRev_Object = MibTableColumn
ePDU2IdentFirmwareRev = _EPDU2IdentFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 2, 2, 1, 7),
    _EPDU2IdentFirmwareRev_Type()
)
ePDU2IdentFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2IdentFirmwareRev.setStatus("mandatory")
_EPDU2IdentDateOfManufacture_Type = DisplayString
_EPDU2IdentDateOfManufacture_Object = MibTableColumn
ePDU2IdentDateOfManufacture = _EPDU2IdentDateOfManufacture_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 2, 2, 1, 8),
    _EPDU2IdentDateOfManufacture_Type()
)
ePDU2IdentDateOfManufacture.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2IdentDateOfManufacture.setStatus("mandatory")
_EPDU2IdentModelName_Type = DisplayString
_EPDU2IdentModelName_Object = MibTableColumn
ePDU2IdentModelName = _EPDU2IdentModelName_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 2, 2, 1, 9),
    _EPDU2IdentModelName_Type()
)
ePDU2IdentModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2IdentModelName.setStatus("mandatory")
_EPDU2IdentSerialNumber_Type = DisplayString
_EPDU2IdentSerialNumber_Object = MibTableColumn
ePDU2IdentSerialNumber = _EPDU2IdentSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 2, 2, 1, 10),
    _EPDU2IdentSerialNumber_Type()
)
ePDU2IdentSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2IdentSerialNumber.setStatus("mandatory")


class _EPDU2IdentIndicator_Type(Integer32):
    """Custom type ePDU2IdentIndicator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noTestIndicators", 1),
          ("testIndicators", 2))
    )


_EPDU2IdentIndicator_Type.__name__ = "Integer32"
_EPDU2IdentIndicator_Object = MibTableColumn
ePDU2IdentIndicator = _EPDU2IdentIndicator_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 2, 2, 1, 11),
    _EPDU2IdentIndicator_Type()
)
ePDU2IdentIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDU2IdentIndicator.setStatus("mandatory")
_EPDU2Device_ObjectIdentity = ObjectIdentity
ePDU2Device = _EPDU2Device_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3)
)
_EPDU2DeviceTableSize_Type = Integer32
_EPDU2DeviceTableSize_Object = MibScalar
ePDU2DeviceTableSize = _EPDU2DeviceTableSize_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3, 1),
    _EPDU2DeviceTableSize_Type()
)
ePDU2DeviceTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2DeviceTableSize.setStatus("mandatory")
_EPDU2DeviceConfigTable_Object = MibTable
ePDU2DeviceConfigTable = _EPDU2DeviceConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3, 2)
)
if mibBuilder.loadTexts:
    ePDU2DeviceConfigTable.setStatus("mandatory")
_EPDU2DeviceConfigEntry_Object = MibTableRow
ePDU2DeviceConfigEntry = _EPDU2DeviceConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3, 2, 1)
)
ePDU2DeviceConfigEntry.setIndexNames(
    (0, "CPS-MIB", "ePDU2DeviceConfigIndex"),
)
if mibBuilder.loadTexts:
    ePDU2DeviceConfigEntry.setStatus("mandatory")


class _EPDU2DeviceConfigIndex_Type(Integer32):
    """Custom type ePDU2DeviceConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_EPDU2DeviceConfigIndex_Type.__name__ = "Integer32"
_EPDU2DeviceConfigIndex_Object = MibTableColumn
ePDU2DeviceConfigIndex = _EPDU2DeviceConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3, 2, 1, 1),
    _EPDU2DeviceConfigIndex_Type()
)
ePDU2DeviceConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2DeviceConfigIndex.setStatus("mandatory")
_EPDU2DeviceConfigModuleIndex_Type = Integer32
_EPDU2DeviceConfigModuleIndex_Object = MibTableColumn
ePDU2DeviceConfigModuleIndex = _EPDU2DeviceConfigModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3, 2, 1, 2),
    _EPDU2DeviceConfigModuleIndex_Type()
)
ePDU2DeviceConfigModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2DeviceConfigModuleIndex.setStatus("mandatory")
_EPDU2DeviceConfigName_Type = DisplayString
_EPDU2DeviceConfigName_Object = MibTableColumn
ePDU2DeviceConfigName = _EPDU2DeviceConfigName_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3, 2, 1, 3),
    _EPDU2DeviceConfigName_Type()
)
ePDU2DeviceConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDU2DeviceConfigName.setStatus("mandatory")
_EPDU2DeviceConfigLocation_Type = DisplayString
_EPDU2DeviceConfigLocation_Object = MibTableColumn
ePDU2DeviceConfigLocation = _EPDU2DeviceConfigLocation_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3, 2, 1, 4),
    _EPDU2DeviceConfigLocation_Type()
)
ePDU2DeviceConfigLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDU2DeviceConfigLocation.setStatus("mandatory")
_EPDU2DeviceConfigContact_Type = DisplayString
_EPDU2DeviceConfigContact_Object = MibTableColumn
ePDU2DeviceConfigContact = _EPDU2DeviceConfigContact_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3, 2, 1, 5),
    _EPDU2DeviceConfigContact_Type()
)
ePDU2DeviceConfigContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDU2DeviceConfigContact.setStatus("mandatory")


class _EPDU2DeviceConfigDisplayOrientation_Type(Integer32):
    """Custom type ePDU2DeviceConfigDisplayOrientation based on Integer32"""
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
        *(("displayNormal", 1),
          ("displayReverse", 2),
          ("displayRotate90", 3),
          ("displayRotate270", 4),
          ("displayAuto", 5))
    )


_EPDU2DeviceConfigDisplayOrientation_Type.__name__ = "Integer32"
_EPDU2DeviceConfigDisplayOrientation_Object = MibTableColumn
ePDU2DeviceConfigDisplayOrientation = _EPDU2DeviceConfigDisplayOrientation_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3, 2, 1, 6),
    _EPDU2DeviceConfigDisplayOrientation_Type()
)
ePDU2DeviceConfigDisplayOrientation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDU2DeviceConfigDisplayOrientation.setStatus("mandatory")
_EPDU2DeviceConfigColdstartDelay_Type = Integer32
_EPDU2DeviceConfigColdstartDelay_Object = MibTableColumn
ePDU2DeviceConfigColdstartDelay = _EPDU2DeviceConfigColdstartDelay_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3, 2, 1, 7),
    _EPDU2DeviceConfigColdstartDelay_Type()
)
ePDU2DeviceConfigColdstartDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDU2DeviceConfigColdstartDelay.setStatus("mandatory")
_EPDU2DeviceConfigCurrentLowLoadThreshold_Type = Integer32
_EPDU2DeviceConfigCurrentLowLoadThreshold_Object = MibTableColumn
ePDU2DeviceConfigCurrentLowLoadThreshold = _EPDU2DeviceConfigCurrentLowLoadThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3, 2, 1, 8),
    _EPDU2DeviceConfigCurrentLowLoadThreshold_Type()
)
ePDU2DeviceConfigCurrentLowLoadThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDU2DeviceConfigCurrentLowLoadThreshold.setStatus("mandatory")
_EPDU2DeviceConfigCurrentNearOverloadThreshold_Type = Integer32
_EPDU2DeviceConfigCurrentNearOverloadThreshold_Object = MibTableColumn
ePDU2DeviceConfigCurrentNearOverloadThreshold = _EPDU2DeviceConfigCurrentNearOverloadThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3, 2, 1, 9),
    _EPDU2DeviceConfigCurrentNearOverloadThreshold_Type()
)
ePDU2DeviceConfigCurrentNearOverloadThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDU2DeviceConfigCurrentNearOverloadThreshold.setStatus("mandatory")
_EPDU2DeviceConfigCurrentOverloadThreshold_Type = Integer32
_EPDU2DeviceConfigCurrentOverloadThreshold_Object = MibTableColumn
ePDU2DeviceConfigCurrentOverloadThreshold = _EPDU2DeviceConfigCurrentOverloadThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3, 2, 1, 10),
    _EPDU2DeviceConfigCurrentOverloadThreshold_Type()
)
ePDU2DeviceConfigCurrentOverloadThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDU2DeviceConfigCurrentOverloadThreshold.setStatus("mandatory")


class _EPDU2DeviceConfigPeakLoadReset_Type(Integer32):
    """Custom type ePDU2DeviceConfigPeakLoadReset based on Integer32"""
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
        *(("noOperation", 1),
          ("resetAll", 2),
          ("resetDevice", 3),
          ("resetOutlets", 4))
    )


_EPDU2DeviceConfigPeakLoadReset_Type.__name__ = "Integer32"
_EPDU2DeviceConfigPeakLoadReset_Object = MibTableColumn
ePDU2DeviceConfigPeakLoadReset = _EPDU2DeviceConfigPeakLoadReset_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3, 2, 1, 11),
    _EPDU2DeviceConfigPeakLoadReset_Type()
)
ePDU2DeviceConfigPeakLoadReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDU2DeviceConfigPeakLoadReset.setStatus("mandatory")


class _EPDU2DeviceConfigEnergyReset_Type(Integer32):
    """Custom type ePDU2DeviceConfigEnergyReset based on Integer32"""
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
        *(("noOperation", 1),
          ("resetAll", 2),
          ("resetDevice", 3),
          ("resetOutlets", 4))
    )


_EPDU2DeviceConfigEnergyReset_Type.__name__ = "Integer32"
_EPDU2DeviceConfigEnergyReset_Object = MibTableColumn
ePDU2DeviceConfigEnergyReset = _EPDU2DeviceConfigEnergyReset_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3, 2, 1, 12),
    _EPDU2DeviceConfigEnergyReset_Type()
)
ePDU2DeviceConfigEnergyReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDU2DeviceConfigEnergyReset.setStatus("mandatory")
_EPDU2DeviceConfigPowerLowLoadThreshold_Type = Integer32
_EPDU2DeviceConfigPowerLowLoadThreshold_Object = MibTableColumn
ePDU2DeviceConfigPowerLowLoadThreshold = _EPDU2DeviceConfigPowerLowLoadThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3, 2, 1, 13),
    _EPDU2DeviceConfigPowerLowLoadThreshold_Type()
)
ePDU2DeviceConfigPowerLowLoadThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDU2DeviceConfigPowerLowLoadThreshold.setStatus("mandatory")
_EPDU2DeviceConfigPowerNearOverloadThreshold_Type = Integer32
_EPDU2DeviceConfigPowerNearOverloadThreshold_Object = MibTableColumn
ePDU2DeviceConfigPowerNearOverloadThreshold = _EPDU2DeviceConfigPowerNearOverloadThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3, 2, 1, 14),
    _EPDU2DeviceConfigPowerNearOverloadThreshold_Type()
)
ePDU2DeviceConfigPowerNearOverloadThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDU2DeviceConfigPowerNearOverloadThreshold.setStatus("mandatory")
_EPDU2DeviceConfigPowerOverloadThreshold_Type = Integer32
_EPDU2DeviceConfigPowerOverloadThreshold_Object = MibTableColumn
ePDU2DeviceConfigPowerOverloadThreshold = _EPDU2DeviceConfigPowerOverloadThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3, 2, 1, 15),
    _EPDU2DeviceConfigPowerOverloadThreshold_Type()
)
ePDU2DeviceConfigPowerOverloadThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDU2DeviceConfigPowerOverloadThreshold.setStatus("mandatory")
_EPDU2DeviceInfoTable_Object = MibTable
ePDU2DeviceInfoTable = _EPDU2DeviceInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3, 3)
)
if mibBuilder.loadTexts:
    ePDU2DeviceInfoTable.setStatus("mandatory")
_EPDU2DeviceInfoEntry_Object = MibTableRow
ePDU2DeviceInfoEntry = _EPDU2DeviceInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3, 3, 1)
)
ePDU2DeviceInfoEntry.setIndexNames(
    (0, "CPS-MIB", "ePDU2DeviceInfoIndex"),
)
if mibBuilder.loadTexts:
    ePDU2DeviceInfoEntry.setStatus("mandatory")


class _EPDU2DeviceInfoIndex_Type(Integer32):
    """Custom type ePDU2DeviceInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_EPDU2DeviceInfoIndex_Type.__name__ = "Integer32"
_EPDU2DeviceInfoIndex_Object = MibTableColumn
ePDU2DeviceInfoIndex = _EPDU2DeviceInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3, 3, 1, 1),
    _EPDU2DeviceInfoIndex_Type()
)
ePDU2DeviceInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2DeviceInfoIndex.setStatus("mandatory")
_EPDU2DeviceInfoModuleIndex_Type = Integer32
_EPDU2DeviceInfoModuleIndex_Object = MibTableColumn
ePDU2DeviceInfoModuleIndex = _EPDU2DeviceInfoModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3, 3, 1, 2),
    _EPDU2DeviceInfoModuleIndex_Type()
)
ePDU2DeviceInfoModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2DeviceInfoModuleIndex.setStatus("mandatory")
_EPDU2DeviceInfoName_Type = DisplayString
_EPDU2DeviceInfoName_Object = MibTableColumn
ePDU2DeviceInfoName = _EPDU2DeviceInfoName_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3, 3, 1, 3),
    _EPDU2DeviceInfoName_Type()
)
ePDU2DeviceInfoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2DeviceInfoName.setStatus("mandatory")
_EPDU2DeviceInfoRating_Type = Integer32
_EPDU2DeviceInfoRating_Object = MibTableColumn
ePDU2DeviceInfoRating = _EPDU2DeviceInfoRating_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3, 3, 1, 4),
    _EPDU2DeviceInfoRating_Type()
)
ePDU2DeviceInfoRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2DeviceInfoRating.setStatus("mandatory")
_EPDU2DeviceInfoNumOutlets_Type = Integer32
_EPDU2DeviceInfoNumOutlets_Object = MibTableColumn
ePDU2DeviceInfoNumOutlets = _EPDU2DeviceInfoNumOutlets_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3, 3, 1, 5),
    _EPDU2DeviceInfoNumOutlets_Type()
)
ePDU2DeviceInfoNumOutlets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2DeviceInfoNumOutlets.setStatus("mandatory")
_EPDU2DeviceInfoSwitchedOutlets_Type = Integer32
_EPDU2DeviceInfoSwitchedOutlets_Object = MibTableColumn
ePDU2DeviceInfoSwitchedOutlets = _EPDU2DeviceInfoSwitchedOutlets_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3, 3, 1, 6),
    _EPDU2DeviceInfoSwitchedOutlets_Type()
)
ePDU2DeviceInfoSwitchedOutlets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2DeviceInfoSwitchedOutlets.setStatus("mandatory")
_EPDU2DeviceInfoMeteredOutlets_Type = Integer32
_EPDU2DeviceInfoMeteredOutlets_Object = MibTableColumn
ePDU2DeviceInfoMeteredOutlets = _EPDU2DeviceInfoMeteredOutlets_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3, 3, 1, 7),
    _EPDU2DeviceInfoMeteredOutlets_Type()
)
ePDU2DeviceInfoMeteredOutlets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2DeviceInfoMeteredOutlets.setStatus("mandatory")
_EPDU2DeviceInfoNumPhases_Type = Integer32
_EPDU2DeviceInfoNumPhases_Object = MibTableColumn
ePDU2DeviceInfoNumPhases = _EPDU2DeviceInfoNumPhases_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3, 3, 1, 8),
    _EPDU2DeviceInfoNumPhases_Type()
)
ePDU2DeviceInfoNumPhases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2DeviceInfoNumPhases.setStatus("mandatory")
_EPDU2DeviceInfoNumBreakers_Type = Integer32
_EPDU2DeviceInfoNumBreakers_Object = MibTableColumn
ePDU2DeviceInfoNumBreakers = _EPDU2DeviceInfoNumBreakers_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3, 3, 1, 9),
    _EPDU2DeviceInfoNumBreakers_Type()
)
ePDU2DeviceInfoNumBreakers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2DeviceInfoNumBreakers.setStatus("mandatory")
_EPDU2DeviceInfoBreakerRating_Type = Integer32
_EPDU2DeviceInfoBreakerRating_Object = MibTableColumn
ePDU2DeviceInfoBreakerRating = _EPDU2DeviceInfoBreakerRating_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3, 3, 1, 10),
    _EPDU2DeviceInfoBreakerRating_Type()
)
ePDU2DeviceInfoBreakerRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2DeviceInfoBreakerRating.setStatus("mandatory")


class _EPDU2DeviceInfoOrientation_Type(Integer32):
    """Custom type ePDU2DeviceInfoOrientation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("orientHorizontal", 1),
          ("orientVertical", 2))
    )


_EPDU2DeviceInfoOrientation_Type.__name__ = "Integer32"
_EPDU2DeviceInfoOrientation_Object = MibTableColumn
ePDU2DeviceInfoOrientation = _EPDU2DeviceInfoOrientation_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3, 3, 1, 11),
    _EPDU2DeviceInfoOrientation_Type()
)
ePDU2DeviceInfoOrientation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2DeviceInfoOrientation.setStatus("mandatory")


class _EPDU2DeviceInfoOutletLayout_Type(Integer32):
    """Custom type ePDU2DeviceInfoOutletLayout based on Integer32"""
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
        *(("seqPhaseToNeutral", 1),
          ("seqPhaseToPhase", 2),
          ("seqPhToNeu21PhToPh", 3),
          ("seqPhToPhGrouped", 4))
    )


_EPDU2DeviceInfoOutletLayout_Type.__name__ = "Integer32"
_EPDU2DeviceInfoOutletLayout_Object = MibTableColumn
ePDU2DeviceInfoOutletLayout = _EPDU2DeviceInfoOutletLayout_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3, 3, 1, 12),
    _EPDU2DeviceInfoOutletLayout_Type()
)
ePDU2DeviceInfoOutletLayout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2DeviceInfoOutletLayout.setStatus("mandatory")
_EPDU2DeviceStatusTable_Object = MibTable
ePDU2DeviceStatusTable = _EPDU2DeviceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3, 4)
)
if mibBuilder.loadTexts:
    ePDU2DeviceStatusTable.setStatus("mandatory")
_EPDU2DeviceStatusEntry_Object = MibTableRow
ePDU2DeviceStatusEntry = _EPDU2DeviceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3, 4, 1)
)
ePDU2DeviceStatusEntry.setIndexNames(
    (0, "CPS-MIB", "ePDU2DeviceStatusIndex"),
)
if mibBuilder.loadTexts:
    ePDU2DeviceStatusEntry.setStatus("mandatory")


class _EPDU2DeviceStatusIndex_Type(Integer32):
    """Custom type ePDU2DeviceStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_EPDU2DeviceStatusIndex_Type.__name__ = "Integer32"
_EPDU2DeviceStatusIndex_Object = MibTableColumn
ePDU2DeviceStatusIndex = _EPDU2DeviceStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3, 4, 1, 1),
    _EPDU2DeviceStatusIndex_Type()
)
ePDU2DeviceStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2DeviceStatusIndex.setStatus("mandatory")
_EPDU2DeviceStatusModuleIndex_Type = Integer32
_EPDU2DeviceStatusModuleIndex_Object = MibTableColumn
ePDU2DeviceStatusModuleIndex = _EPDU2DeviceStatusModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3, 4, 1, 2),
    _EPDU2DeviceStatusModuleIndex_Type()
)
ePDU2DeviceStatusModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2DeviceStatusModuleIndex.setStatus("mandatory")
_EPDU2DeviceStatusName_Type = DisplayString
_EPDU2DeviceStatusName_Object = MibTableColumn
ePDU2DeviceStatusName = _EPDU2DeviceStatusName_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3, 4, 1, 3),
    _EPDU2DeviceStatusName_Type()
)
ePDU2DeviceStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2DeviceStatusName.setStatus("mandatory")


class _EPDU2DeviceStatusLoadState_Type(Integer32):
    """Custom type ePDU2DeviceStatusLoadState based on Integer32"""
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
        *(("noLoadAlarm", 1),
          ("underCurrentAlarm", 2),
          ("nearOverCurrentAlarm", 3),
          ("overCurrentAlarm", 4))
    )


_EPDU2DeviceStatusLoadState_Type.__name__ = "Integer32"
_EPDU2DeviceStatusLoadState_Object = MibTableColumn
ePDU2DeviceStatusLoadState = _EPDU2DeviceStatusLoadState_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3, 4, 1, 4),
    _EPDU2DeviceStatusLoadState_Type()
)
ePDU2DeviceStatusLoadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2DeviceStatusLoadState.setStatus("mandatory")
_EPDU2DeviceStatusCurrentLoad_Type = Gauge32
_EPDU2DeviceStatusCurrentLoad_Object = MibTableColumn
ePDU2DeviceStatusCurrentLoad = _EPDU2DeviceStatusCurrentLoad_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3, 4, 1, 5),
    _EPDU2DeviceStatusCurrentLoad_Type()
)
ePDU2DeviceStatusCurrentLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2DeviceStatusCurrentLoad.setStatus("mandatory")
_EPDU2DeviceStatusCurrentPeakLoad_Type = Gauge32
_EPDU2DeviceStatusCurrentPeakLoad_Object = MibTableColumn
ePDU2DeviceStatusCurrentPeakLoad = _EPDU2DeviceStatusCurrentPeakLoad_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3, 4, 1, 6),
    _EPDU2DeviceStatusCurrentPeakLoad_Type()
)
ePDU2DeviceStatusCurrentPeakLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2DeviceStatusCurrentPeakLoad.setStatus("mandatory")
_EPDU2DeviceStatusPeakLoadTimestamp_Type = DisplayString
_EPDU2DeviceStatusPeakLoadTimestamp_Object = MibTableColumn
ePDU2DeviceStatusPeakLoadTimestamp = _EPDU2DeviceStatusPeakLoadTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3, 4, 1, 7),
    _EPDU2DeviceStatusPeakLoadTimestamp_Type()
)
ePDU2DeviceStatusPeakLoadTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2DeviceStatusPeakLoadTimestamp.setStatus("mandatory")
_EPDU2DeviceStatusPeakLoadStartTime_Type = DisplayString
_EPDU2DeviceStatusPeakLoadStartTime_Object = MibTableColumn
ePDU2DeviceStatusPeakLoadStartTime = _EPDU2DeviceStatusPeakLoadStartTime_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3, 4, 1, 8),
    _EPDU2DeviceStatusPeakLoadStartTime_Type()
)
ePDU2DeviceStatusPeakLoadStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2DeviceStatusPeakLoadStartTime.setStatus("mandatory")
_EPDU2DeviceStatusEnergy_Type = Gauge32
_EPDU2DeviceStatusEnergy_Object = MibTableColumn
ePDU2DeviceStatusEnergy = _EPDU2DeviceStatusEnergy_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3, 4, 1, 9),
    _EPDU2DeviceStatusEnergy_Type()
)
ePDU2DeviceStatusEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2DeviceStatusEnergy.setStatus("mandatory")
_EPDU2DeviceStatusEnergyStartTime_Type = DisplayString
_EPDU2DeviceStatusEnergyStartTime_Object = MibTableColumn
ePDU2DeviceStatusEnergyStartTime = _EPDU2DeviceStatusEnergyStartTime_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3, 4, 1, 10),
    _EPDU2DeviceStatusEnergyStartTime_Type()
)
ePDU2DeviceStatusEnergyStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2DeviceStatusEnergyStartTime.setStatus("mandatory")


class _EPDU2DeviceStatusCommandPending_Type(Integer32):
    """Custom type ePDU2DeviceStatusCommandPending based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("commandPending", 1),
          ("noCommandPending", 2))
    )


_EPDU2DeviceStatusCommandPending_Type.__name__ = "Integer32"
_EPDU2DeviceStatusCommandPending_Object = MibTableColumn
ePDU2DeviceStatusCommandPending = _EPDU2DeviceStatusCommandPending_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3, 4, 1, 11),
    _EPDU2DeviceStatusCommandPending_Type()
)
ePDU2DeviceStatusCommandPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2DeviceStatusCommandPending.setStatus("mandatory")


class _EPDU2DeviceStatusPowerSupplyAlarm_Type(Integer32):
    """Custom type ePDU2DeviceStatusPowerSupplyAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("alarm", 2))
    )


_EPDU2DeviceStatusPowerSupplyAlarm_Type.__name__ = "Integer32"
_EPDU2DeviceStatusPowerSupplyAlarm_Object = MibTableColumn
ePDU2DeviceStatusPowerSupplyAlarm = _EPDU2DeviceStatusPowerSupplyAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3, 4, 1, 12),
    _EPDU2DeviceStatusPowerSupplyAlarm_Type()
)
ePDU2DeviceStatusPowerSupplyAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2DeviceStatusPowerSupplyAlarm.setStatus("mandatory")


class _EPDU2DeviceStatusPowerSupply1Status_Type(Integer32):
    """Custom type ePDU2DeviceStatusPowerSupply1Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("alarm", 2))
    )


_EPDU2DeviceStatusPowerSupply1Status_Type.__name__ = "Integer32"
_EPDU2DeviceStatusPowerSupply1Status_Object = MibTableColumn
ePDU2DeviceStatusPowerSupply1Status = _EPDU2DeviceStatusPowerSupply1Status_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3, 4, 1, 13),
    _EPDU2DeviceStatusPowerSupply1Status_Type()
)
ePDU2DeviceStatusPowerSupply1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2DeviceStatusPowerSupply1Status.setStatus("mandatory")


class _EPDU2DeviceStatusPowerSupply2Status_Type(Integer32):
    """Custom type ePDU2DeviceStatusPowerSupply2Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("alarm", 2))
    )


_EPDU2DeviceStatusPowerSupply2Status_Type.__name__ = "Integer32"
_EPDU2DeviceStatusPowerSupply2Status_Object = MibTableColumn
ePDU2DeviceStatusPowerSupply2Status = _EPDU2DeviceStatusPowerSupply2Status_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3, 4, 1, 14),
    _EPDU2DeviceStatusPowerSupply2Status_Type()
)
ePDU2DeviceStatusPowerSupply2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2DeviceStatusPowerSupply2Status.setStatus("mandatory")
_EPDU2DeviceStatusApparentPower_Type = Gauge32
_EPDU2DeviceStatusApparentPower_Object = MibTableColumn
ePDU2DeviceStatusApparentPower = _EPDU2DeviceStatusApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3, 4, 1, 15),
    _EPDU2DeviceStatusApparentPower_Type()
)
ePDU2DeviceStatusApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2DeviceStatusApparentPower.setStatus("mandatory")
_EPDU2DeviceStatusPowerFactor_Type = Gauge32
_EPDU2DeviceStatusPowerFactor_Object = MibTableColumn
ePDU2DeviceStatusPowerFactor = _EPDU2DeviceStatusPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3, 4, 1, 16),
    _EPDU2DeviceStatusPowerFactor_Type()
)
ePDU2DeviceStatusPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2DeviceStatusPowerFactor.setStatus("mandatory")


class _EPDU2DeviceStatusRoleType_Type(Integer32):
    """Custom type ePDU2DeviceStatusRoleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("standalone", 1),
          ("host", 2),
          ("slave", 3))
    )


_EPDU2DeviceStatusRoleType_Type.__name__ = "Integer32"
_EPDU2DeviceStatusRoleType_Object = MibTableColumn
ePDU2DeviceStatusRoleType = _EPDU2DeviceStatusRoleType_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3, 4, 1, 17),
    _EPDU2DeviceStatusRoleType_Type()
)
ePDU2DeviceStatusRoleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2DeviceStatusRoleType.setStatus("mandatory")
_EPDU2DeviceStatusPowerLoad_Type = Gauge32
_EPDU2DeviceStatusPowerLoad_Object = MibTableColumn
ePDU2DeviceStatusPowerLoad = _EPDU2DeviceStatusPowerLoad_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3, 4, 1, 18),
    _EPDU2DeviceStatusPowerLoad_Type()
)
ePDU2DeviceStatusPowerLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2DeviceStatusPowerLoad.setStatus("mandatory")
_EPDU2DeviceStatusPowerPeakLoad_Type = Gauge32
_EPDU2DeviceStatusPowerPeakLoad_Object = MibTableColumn
ePDU2DeviceStatusPowerPeakLoad = _EPDU2DeviceStatusPowerPeakLoad_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3, 4, 1, 19),
    _EPDU2DeviceStatusPowerPeakLoad_Type()
)
ePDU2DeviceStatusPowerPeakLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2DeviceStatusPowerPeakLoad.setStatus("mandatory")
_EPDU2DeviceControlTable_Object = MibTable
ePDU2DeviceControlTable = _EPDU2DeviceControlTable_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3, 5)
)
if mibBuilder.loadTexts:
    ePDU2DeviceControlTable.setStatus("mandatory")
_EPDU2DeviceControlEntry_Object = MibTableRow
ePDU2DeviceControlEntry = _EPDU2DeviceControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3, 5, 1)
)
ePDU2DeviceControlEntry.setIndexNames(
    (0, "CPS-MIB", "ePDU2DeviceControlIndex"),
)
if mibBuilder.loadTexts:
    ePDU2DeviceControlEntry.setStatus("mandatory")


class _EPDU2DeviceControlIndex_Type(Integer32):
    """Custom type ePDU2DeviceControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_EPDU2DeviceControlIndex_Type.__name__ = "Integer32"
_EPDU2DeviceControlIndex_Object = MibTableColumn
ePDU2DeviceControlIndex = _EPDU2DeviceControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3, 5, 1, 1),
    _EPDU2DeviceControlIndex_Type()
)
ePDU2DeviceControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2DeviceControlIndex.setStatus("mandatory")
_EPDU2DeviceControlModuleIndex_Type = Integer32
_EPDU2DeviceControlModuleIndex_Object = MibTableColumn
ePDU2DeviceControlModuleIndex = _EPDU2DeviceControlModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3, 5, 1, 2),
    _EPDU2DeviceControlModuleIndex_Type()
)
ePDU2DeviceControlModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2DeviceControlModuleIndex.setStatus("mandatory")
_EPDU2DeviceControlName_Type = DisplayString
_EPDU2DeviceControlName_Object = MibTableColumn
ePDU2DeviceControlName = _EPDU2DeviceControlName_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3, 5, 1, 3),
    _EPDU2DeviceControlName_Type()
)
ePDU2DeviceControlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2DeviceControlName.setStatus("mandatory")


class _EPDU2DeviceControlCommand_Type(Integer32):
    """Custom type ePDU2DeviceControlCommand based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("immediateAllOn", 1),
          ("immediateAllOff", 2),
          ("immediateAllReboot", 3),
          ("delayedAllOn", 4),
          ("delayedAllOff", 5),
          ("delayedAllReboot", 6),
          ("cancelAllPendingCommand", 7),
          ("noCommand", 8))
    )


_EPDU2DeviceControlCommand_Type.__name__ = "Integer32"
_EPDU2DeviceControlCommand_Object = MibTableColumn
ePDU2DeviceControlCommand = _EPDU2DeviceControlCommand_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 3, 5, 1, 4),
    _EPDU2DeviceControlCommand_Type()
)
ePDU2DeviceControlCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDU2DeviceControlCommand.setStatus("mandatory")
_EPDU2Phase_ObjectIdentity = ObjectIdentity
ePDU2Phase = _EPDU2Phase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 4)
)
_EPDU2PhaseTableSize_Type = Integer32
_EPDU2PhaseTableSize_Object = MibScalar
ePDU2PhaseTableSize = _EPDU2PhaseTableSize_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 4, 1),
    _EPDU2PhaseTableSize_Type()
)
ePDU2PhaseTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2PhaseTableSize.setStatus("mandatory")
_EPDU2PhaseConfigTable_Object = MibTable
ePDU2PhaseConfigTable = _EPDU2PhaseConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 4, 2)
)
if mibBuilder.loadTexts:
    ePDU2PhaseConfigTable.setStatus("mandatory")
_EPDU2PhaseConfigEntry_Object = MibTableRow
ePDU2PhaseConfigEntry = _EPDU2PhaseConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 4, 2, 1)
)
ePDU2PhaseConfigEntry.setIndexNames(
    (0, "CPS-MIB", "ePDU2PhaseConfigIndex"),
)
if mibBuilder.loadTexts:
    ePDU2PhaseConfigEntry.setStatus("mandatory")


class _EPDU2PhaseConfigIndex_Type(Integer32):
    """Custom type ePDU2PhaseConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_EPDU2PhaseConfigIndex_Type.__name__ = "Integer32"
_EPDU2PhaseConfigIndex_Object = MibTableColumn
ePDU2PhaseConfigIndex = _EPDU2PhaseConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 4, 2, 1, 1),
    _EPDU2PhaseConfigIndex_Type()
)
ePDU2PhaseConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2PhaseConfigIndex.setStatus("mandatory")
_EPDU2PhaseConfigModuleIndex_Type = Integer32
_EPDU2PhaseConfigModuleIndex_Object = MibTableColumn
ePDU2PhaseConfigModuleIndex = _EPDU2PhaseConfigModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 4, 2, 1, 2),
    _EPDU2PhaseConfigModuleIndex_Type()
)
ePDU2PhaseConfigModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2PhaseConfigModuleIndex.setStatus("mandatory")
_EPDU2PhaseConfigNumber_Type = Integer32
_EPDU2PhaseConfigNumber_Object = MibTableColumn
ePDU2PhaseConfigNumber = _EPDU2PhaseConfigNumber_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 4, 2, 1, 3),
    _EPDU2PhaseConfigNumber_Type()
)
ePDU2PhaseConfigNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2PhaseConfigNumber.setStatus("mandatory")


class _EPDU2PhaseConfigOverloadRestriction_Type(Integer32):
    """Custom type ePDU2PhaseConfigOverloadRestriction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", -1),
          ("alwaysAllowTurnON", 1),
          ("restrictOnNearOverload", 2),
          ("restrictOnOverload", 3))
    )


_EPDU2PhaseConfigOverloadRestriction_Type.__name__ = "Integer32"
_EPDU2PhaseConfigOverloadRestriction_Object = MibTableColumn
ePDU2PhaseConfigOverloadRestriction = _EPDU2PhaseConfigOverloadRestriction_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 4, 2, 1, 4),
    _EPDU2PhaseConfigOverloadRestriction_Type()
)
ePDU2PhaseConfigOverloadRestriction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDU2PhaseConfigOverloadRestriction.setStatus("mandatory")
_EPDU2PhaseConfigLowLoadThreshold_Type = Integer32
_EPDU2PhaseConfigLowLoadThreshold_Object = MibTableColumn
ePDU2PhaseConfigLowLoadThreshold = _EPDU2PhaseConfigLowLoadThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 4, 2, 1, 5),
    _EPDU2PhaseConfigLowLoadThreshold_Type()
)
ePDU2PhaseConfigLowLoadThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDU2PhaseConfigLowLoadThreshold.setStatus("mandatory")
_EPDU2PhaseConfigNearOverloadThreshold_Type = Integer32
_EPDU2PhaseConfigNearOverloadThreshold_Object = MibTableColumn
ePDU2PhaseConfigNearOverloadThreshold = _EPDU2PhaseConfigNearOverloadThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 4, 2, 1, 6),
    _EPDU2PhaseConfigNearOverloadThreshold_Type()
)
ePDU2PhaseConfigNearOverloadThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDU2PhaseConfigNearOverloadThreshold.setStatus("mandatory")
_EPDU2PhaseConfigOverloadThreshold_Type = Integer32
_EPDU2PhaseConfigOverloadThreshold_Object = MibTableColumn
ePDU2PhaseConfigOverloadThreshold = _EPDU2PhaseConfigOverloadThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 4, 2, 1, 7),
    _EPDU2PhaseConfigOverloadThreshold_Type()
)
ePDU2PhaseConfigOverloadThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDU2PhaseConfigOverloadThreshold.setStatus("mandatory")


class _EPDU2PhaseConfigPhasePeakLoadReset_Type(Integer32):
    """Custom type ePDU2PhaseConfigPhasePeakLoadReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noOperation", 1),
          ("reset", 2))
    )


_EPDU2PhaseConfigPhasePeakLoadReset_Type.__name__ = "Integer32"
_EPDU2PhaseConfigPhasePeakLoadReset_Object = MibTableColumn
ePDU2PhaseConfigPhasePeakLoadReset = _EPDU2PhaseConfigPhasePeakLoadReset_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 4, 2, 1, 8),
    _EPDU2PhaseConfigPhasePeakLoadReset_Type()
)
ePDU2PhaseConfigPhasePeakLoadReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDU2PhaseConfigPhasePeakLoadReset.setStatus("mandatory")
_EPDU2PhaseInfoTable_Object = MibTable
ePDU2PhaseInfoTable = _EPDU2PhaseInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 4, 3)
)
if mibBuilder.loadTexts:
    ePDU2PhaseInfoTable.setStatus("mandatory")
_EPDU2PhaseInfoEntry_Object = MibTableRow
ePDU2PhaseInfoEntry = _EPDU2PhaseInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 4, 3, 1)
)
ePDU2PhaseInfoEntry.setIndexNames(
    (0, "CPS-MIB", "ePDU2PhaseInfoIndex"),
)
if mibBuilder.loadTexts:
    ePDU2PhaseInfoEntry.setStatus("mandatory")


class _EPDU2PhaseInfoIndex_Type(Integer32):
    """Custom type ePDU2PhaseInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_EPDU2PhaseInfoIndex_Type.__name__ = "Integer32"
_EPDU2PhaseInfoIndex_Object = MibTableColumn
ePDU2PhaseInfoIndex = _EPDU2PhaseInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 4, 3, 1, 1),
    _EPDU2PhaseInfoIndex_Type()
)
ePDU2PhaseInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2PhaseInfoIndex.setStatus("mandatory")
_EPDU2PhaseInfoModuleIndex_Type = Integer32
_EPDU2PhaseInfoModuleIndex_Object = MibTableColumn
ePDU2PhaseInfoModuleIndex = _EPDU2PhaseInfoModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 4, 3, 1, 2),
    _EPDU2PhaseInfoModuleIndex_Type()
)
ePDU2PhaseInfoModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2PhaseInfoModuleIndex.setStatus("mandatory")
_EPDU2PhaseInfoNumber_Type = Integer32
_EPDU2PhaseInfoNumber_Object = MibTableColumn
ePDU2PhaseInfoNumber = _EPDU2PhaseInfoNumber_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 4, 3, 1, 3),
    _EPDU2PhaseInfoNumber_Type()
)
ePDU2PhaseInfoNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2PhaseInfoNumber.setStatus("mandatory")
_EPDU2PhaseStatusTable_Object = MibTable
ePDU2PhaseStatusTable = _EPDU2PhaseStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 4, 4)
)
if mibBuilder.loadTexts:
    ePDU2PhaseStatusTable.setStatus("mandatory")
_EPDU2PhaseStatusEntry_Object = MibTableRow
ePDU2PhaseStatusEntry = _EPDU2PhaseStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 4, 4, 1)
)
ePDU2PhaseStatusEntry.setIndexNames(
    (0, "CPS-MIB", "ePDU2PhaseStatusIndex"),
)
if mibBuilder.loadTexts:
    ePDU2PhaseStatusEntry.setStatus("mandatory")


class _EPDU2PhaseStatusIndex_Type(Integer32):
    """Custom type ePDU2PhaseStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 13),
    )


_EPDU2PhaseStatusIndex_Type.__name__ = "Integer32"
_EPDU2PhaseStatusIndex_Object = MibTableColumn
ePDU2PhaseStatusIndex = _EPDU2PhaseStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 4, 4, 1, 1),
    _EPDU2PhaseStatusIndex_Type()
)
ePDU2PhaseStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2PhaseStatusIndex.setStatus("mandatory")
_EPDU2PhaseStatusModuleIndex_Type = Integer32
_EPDU2PhaseStatusModuleIndex_Object = MibTableColumn
ePDU2PhaseStatusModuleIndex = _EPDU2PhaseStatusModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 4, 4, 1, 2),
    _EPDU2PhaseStatusModuleIndex_Type()
)
ePDU2PhaseStatusModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2PhaseStatusModuleIndex.setStatus("mandatory")
_EPDU2PhaseStatusNumber_Type = Integer32
_EPDU2PhaseStatusNumber_Object = MibTableColumn
ePDU2PhaseStatusNumber = _EPDU2PhaseStatusNumber_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 4, 4, 1, 3),
    _EPDU2PhaseStatusNumber_Type()
)
ePDU2PhaseStatusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2PhaseStatusNumber.setStatus("mandatory")


class _EPDU2PhaseStatusLoadState_Type(Integer32):
    """Custom type ePDU2PhaseStatusLoadState based on Integer32"""
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
        *(("normal", 1),
          ("lowLoad", 2),
          ("nearOverload", 3),
          ("overload", 4))
    )


_EPDU2PhaseStatusLoadState_Type.__name__ = "Integer32"
_EPDU2PhaseStatusLoadState_Object = MibTableColumn
ePDU2PhaseStatusLoadState = _EPDU2PhaseStatusLoadState_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 4, 4, 1, 4),
    _EPDU2PhaseStatusLoadState_Type()
)
ePDU2PhaseStatusLoadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2PhaseStatusLoadState.setStatus("mandatory")
_EPDU2PhaseStatusLoad_Type = Gauge32
_EPDU2PhaseStatusLoad_Object = MibTableColumn
ePDU2PhaseStatusLoad = _EPDU2PhaseStatusLoad_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 4, 4, 1, 5),
    _EPDU2PhaseStatusLoad_Type()
)
ePDU2PhaseStatusLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2PhaseStatusLoad.setStatus("mandatory")
_EPDU2PhaseStatusVoltage_Type = Gauge32
_EPDU2PhaseStatusVoltage_Object = MibTableColumn
ePDU2PhaseStatusVoltage = _EPDU2PhaseStatusVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 4, 4, 1, 6),
    _EPDU2PhaseStatusVoltage_Type()
)
ePDU2PhaseStatusVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2PhaseStatusVoltage.setStatus("mandatory")
_EPDU2PhaseStatusPower_Type = Gauge32
_EPDU2PhaseStatusPower_Object = MibTableColumn
ePDU2PhaseStatusPower = _EPDU2PhaseStatusPower_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 4, 4, 1, 7),
    _EPDU2PhaseStatusPower_Type()
)
ePDU2PhaseStatusPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2PhaseStatusPower.setStatus("mandatory")
_EPDU2PhaseStatusApparentPower_Type = Gauge32
_EPDU2PhaseStatusApparentPower_Object = MibTableColumn
ePDU2PhaseStatusApparentPower = _EPDU2PhaseStatusApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 4, 4, 1, 8),
    _EPDU2PhaseStatusApparentPower_Type()
)
ePDU2PhaseStatusApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2PhaseStatusApparentPower.setStatus("mandatory")
_EPDU2PhaseStatusPowerFactor_Type = Gauge32
_EPDU2PhaseStatusPowerFactor_Object = MibTableColumn
ePDU2PhaseStatusPowerFactor = _EPDU2PhaseStatusPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 4, 4, 1, 9),
    _EPDU2PhaseStatusPowerFactor_Type()
)
ePDU2PhaseStatusPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2PhaseStatusPowerFactor.setStatus("mandatory")
_EPDU2PhaseStatusPeakLoad_Type = Gauge32
_EPDU2PhaseStatusPeakLoad_Object = MibTableColumn
ePDU2PhaseStatusPeakLoad = _EPDU2PhaseStatusPeakLoad_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 4, 4, 1, 10),
    _EPDU2PhaseStatusPeakLoad_Type()
)
ePDU2PhaseStatusPeakLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2PhaseStatusPeakLoad.setStatus("mandatory")
_EPDU2PhaseStatusPeakLoadTimestamp_Type = DisplayString
_EPDU2PhaseStatusPeakLoadTimestamp_Object = MibTableColumn
ePDU2PhaseStatusPeakLoadTimestamp = _EPDU2PhaseStatusPeakLoadTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 4, 4, 1, 11),
    _EPDU2PhaseStatusPeakLoadTimestamp_Type()
)
ePDU2PhaseStatusPeakLoadTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2PhaseStatusPeakLoadTimestamp.setStatus("mandatory")
_EPDU2PhaseStatusPeakLoadStartTime_Type = DisplayString
_EPDU2PhaseStatusPeakLoadStartTime_Object = MibTableColumn
ePDU2PhaseStatusPeakLoadStartTime = _EPDU2PhaseStatusPeakLoadStartTime_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 4, 4, 1, 12),
    _EPDU2PhaseStatusPeakLoadStartTime_Type()
)
ePDU2PhaseStatusPeakLoadStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2PhaseStatusPeakLoadStartTime.setStatus("mandatory")
_EPDU2PhaseStatusLineToLineVoltage_Type = Gauge32
_EPDU2PhaseStatusLineToLineVoltage_Object = MibTableColumn
ePDU2PhaseStatusLineToLineVoltage = _EPDU2PhaseStatusLineToLineVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 4, 4, 1, 13),
    _EPDU2PhaseStatusLineToLineVoltage_Type()
)
ePDU2PhaseStatusLineToLineVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2PhaseStatusLineToLineVoltage.setStatus("mandatory")
_EPDU2Bank_ObjectIdentity = ObjectIdentity
ePDU2Bank = _EPDU2Bank_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 5)
)
_EPDU2BankTableSize_Type = Integer32
_EPDU2BankTableSize_Object = MibScalar
ePDU2BankTableSize = _EPDU2BankTableSize_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 5, 1),
    _EPDU2BankTableSize_Type()
)
ePDU2BankTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2BankTableSize.setStatus("mandatory")
_EPDU2BankConfigTable_Object = MibTable
ePDU2BankConfigTable = _EPDU2BankConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 5, 2)
)
if mibBuilder.loadTexts:
    ePDU2BankConfigTable.setStatus("mandatory")
_EPDU2BankConfigEntry_Object = MibTableRow
ePDU2BankConfigEntry = _EPDU2BankConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 5, 2, 1)
)
ePDU2BankConfigEntry.setIndexNames(
    (0, "CPS-MIB", "ePDU2BankConfigIndex"),
)
if mibBuilder.loadTexts:
    ePDU2BankConfigEntry.setStatus("mandatory")


class _EPDU2BankConfigIndex_Type(Integer32):
    """Custom type ePDU2BankConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_EPDU2BankConfigIndex_Type.__name__ = "Integer32"
_EPDU2BankConfigIndex_Object = MibTableColumn
ePDU2BankConfigIndex = _EPDU2BankConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 5, 2, 1, 1),
    _EPDU2BankConfigIndex_Type()
)
ePDU2BankConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2BankConfigIndex.setStatus("mandatory")
_EPDU2BankConfigModuleIndex_Type = Integer32
_EPDU2BankConfigModuleIndex_Object = MibTableColumn
ePDU2BankConfigModuleIndex = _EPDU2BankConfigModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 5, 2, 1, 2),
    _EPDU2BankConfigModuleIndex_Type()
)
ePDU2BankConfigModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2BankConfigModuleIndex.setStatus("mandatory")
_EPDU2BankConfigNumber_Type = Integer32
_EPDU2BankConfigNumber_Object = MibTableColumn
ePDU2BankConfigNumber = _EPDU2BankConfigNumber_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 5, 2, 1, 3),
    _EPDU2BankConfigNumber_Type()
)
ePDU2BankConfigNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2BankConfigNumber.setStatus("mandatory")


class _EPDU2BankConfigOverloadRestriction_Type(Integer32):
    """Custom type ePDU2BankConfigOverloadRestriction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alwaysAllowTurnON", 1),
          ("restrictOnNearOverload", 2),
          ("restrictOnOverload", 3))
    )


_EPDU2BankConfigOverloadRestriction_Type.__name__ = "Integer32"
_EPDU2BankConfigOverloadRestriction_Object = MibTableColumn
ePDU2BankConfigOverloadRestriction = _EPDU2BankConfigOverloadRestriction_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 5, 2, 1, 4),
    _EPDU2BankConfigOverloadRestriction_Type()
)
ePDU2BankConfigOverloadRestriction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDU2BankConfigOverloadRestriction.setStatus("mandatory")
_EPDU2BankConfigLowLoadThreshold_Type = Integer32
_EPDU2BankConfigLowLoadThreshold_Object = MibTableColumn
ePDU2BankConfigLowLoadThreshold = _EPDU2BankConfigLowLoadThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 5, 2, 1, 5),
    _EPDU2BankConfigLowLoadThreshold_Type()
)
ePDU2BankConfigLowLoadThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDU2BankConfigLowLoadThreshold.setStatus("mandatory")
_EPDU2BankConfigNearOverloadThreshold_Type = Integer32
_EPDU2BankConfigNearOverloadThreshold_Object = MibTableColumn
ePDU2BankConfigNearOverloadThreshold = _EPDU2BankConfigNearOverloadThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 5, 2, 1, 6),
    _EPDU2BankConfigNearOverloadThreshold_Type()
)
ePDU2BankConfigNearOverloadThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDU2BankConfigNearOverloadThreshold.setStatus("mandatory")
_EPDU2BankConfigOverloadThreshold_Type = Integer32
_EPDU2BankConfigOverloadThreshold_Object = MibTableColumn
ePDU2BankConfigOverloadThreshold = _EPDU2BankConfigOverloadThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 5, 2, 1, 7),
    _EPDU2BankConfigOverloadThreshold_Type()
)
ePDU2BankConfigOverloadThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDU2BankConfigOverloadThreshold.setStatus("mandatory")


class _EPDU2BankConfigPeakLoadReset_Type(Integer32):
    """Custom type ePDU2BankConfigPeakLoadReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noOperation", 1),
          ("reset", 2))
    )


_EPDU2BankConfigPeakLoadReset_Type.__name__ = "Integer32"
_EPDU2BankConfigPeakLoadReset_Object = MibTableColumn
ePDU2BankConfigPeakLoadReset = _EPDU2BankConfigPeakLoadReset_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 5, 2, 1, 8),
    _EPDU2BankConfigPeakLoadReset_Type()
)
ePDU2BankConfigPeakLoadReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDU2BankConfigPeakLoadReset.setStatus("mandatory")
_EPDU2BankInfoTable_Object = MibTable
ePDU2BankInfoTable = _EPDU2BankInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 5, 3)
)
if mibBuilder.loadTexts:
    ePDU2BankInfoTable.setStatus("mandatory")
_EPDU2BankInfoEntry_Object = MibTableRow
ePDU2BankInfoEntry = _EPDU2BankInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 5, 3, 1)
)
ePDU2BankInfoEntry.setIndexNames(
    (0, "CPS-MIB", "ePDU2BankInfoIndex"),
)
if mibBuilder.loadTexts:
    ePDU2BankInfoEntry.setStatus("mandatory")


class _EPDU2BankInfoIndex_Type(Integer32):
    """Custom type ePDU2BankInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_EPDU2BankInfoIndex_Type.__name__ = "Integer32"
_EPDU2BankInfoIndex_Object = MibTableColumn
ePDU2BankInfoIndex = _EPDU2BankInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 5, 3, 1, 1),
    _EPDU2BankInfoIndex_Type()
)
ePDU2BankInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2BankInfoIndex.setStatus("mandatory")
_EPDU2BankInfoModuleIndex_Type = Integer32
_EPDU2BankInfoModuleIndex_Object = MibTableColumn
ePDU2BankInfoModuleIndex = _EPDU2BankInfoModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 5, 3, 1, 2),
    _EPDU2BankInfoModuleIndex_Type()
)
ePDU2BankInfoModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2BankInfoModuleIndex.setStatus("mandatory")
_EPDU2BankInfoNumber_Type = Integer32
_EPDU2BankInfoNumber_Object = MibTableColumn
ePDU2BankInfoNumber = _EPDU2BankInfoNumber_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 5, 3, 1, 3),
    _EPDU2BankInfoNumber_Type()
)
ePDU2BankInfoNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2BankInfoNumber.setStatus("mandatory")
_EPDU2BankStatusTable_Object = MibTable
ePDU2BankStatusTable = _EPDU2BankStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 5, 4)
)
if mibBuilder.loadTexts:
    ePDU2BankStatusTable.setStatus("mandatory")
_EPDU2BankStatusEntry_Object = MibTableRow
ePDU2BankStatusEntry = _EPDU2BankStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 5, 4, 1)
)
ePDU2BankStatusEntry.setIndexNames(
    (0, "CPS-MIB", "ePDU2BankStatusIndex"),
)
if mibBuilder.loadTexts:
    ePDU2BankStatusEntry.setStatus("mandatory")


class _EPDU2BankStatusIndex_Type(Integer32):
    """Custom type ePDU2BankStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_EPDU2BankStatusIndex_Type.__name__ = "Integer32"
_EPDU2BankStatusIndex_Object = MibTableColumn
ePDU2BankStatusIndex = _EPDU2BankStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 5, 4, 1, 1),
    _EPDU2BankStatusIndex_Type()
)
ePDU2BankStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2BankStatusIndex.setStatus("mandatory")
_EPDU2BankStatusModuleIndex_Type = Integer32
_EPDU2BankStatusModuleIndex_Object = MibTableColumn
ePDU2BankStatusModuleIndex = _EPDU2BankStatusModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 5, 4, 1, 2),
    _EPDU2BankStatusModuleIndex_Type()
)
ePDU2BankStatusModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2BankStatusModuleIndex.setStatus("mandatory")
_EPDU2BankStatusNumber_Type = Integer32
_EPDU2BankStatusNumber_Object = MibTableColumn
ePDU2BankStatusNumber = _EPDU2BankStatusNumber_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 5, 4, 1, 3),
    _EPDU2BankStatusNumber_Type()
)
ePDU2BankStatusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2BankStatusNumber.setStatus("mandatory")


class _EPDU2BankStatusLoadState_Type(Integer32):
    """Custom type ePDU2BankStatusLoadState based on Integer32"""
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
        *(("normal", 1),
          ("lowLoad", 2),
          ("nearOverload", 3),
          ("overload", 4))
    )


_EPDU2BankStatusLoadState_Type.__name__ = "Integer32"
_EPDU2BankStatusLoadState_Object = MibTableColumn
ePDU2BankStatusLoadState = _EPDU2BankStatusLoadState_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 5, 4, 1, 4),
    _EPDU2BankStatusLoadState_Type()
)
ePDU2BankStatusLoadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2BankStatusLoadState.setStatus("mandatory")
_EPDU2BankStatusLoad_Type = Gauge32
_EPDU2BankStatusLoad_Object = MibTableColumn
ePDU2BankStatusLoad = _EPDU2BankStatusLoad_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 5, 4, 1, 5),
    _EPDU2BankStatusLoad_Type()
)
ePDU2BankStatusLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2BankStatusLoad.setStatus("mandatory")
_EPDU2BankStatusPeakLoad_Type = Gauge32
_EPDU2BankStatusPeakLoad_Object = MibTableColumn
ePDU2BankStatusPeakLoad = _EPDU2BankStatusPeakLoad_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 5, 4, 1, 6),
    _EPDU2BankStatusPeakLoad_Type()
)
ePDU2BankStatusPeakLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2BankStatusPeakLoad.setStatus("mandatory")
_EPDU2BankStatusPeakLoadTimestamp_Type = DisplayString
_EPDU2BankStatusPeakLoadTimestamp_Object = MibTableColumn
ePDU2BankStatusPeakLoadTimestamp = _EPDU2BankStatusPeakLoadTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 5, 4, 1, 7),
    _EPDU2BankStatusPeakLoadTimestamp_Type()
)
ePDU2BankStatusPeakLoadTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2BankStatusPeakLoadTimestamp.setStatus("mandatory")
_EPDU2BankStatusPeakLoadStartTime_Type = DisplayString
_EPDU2BankStatusPeakLoadStartTime_Object = MibTableColumn
ePDU2BankStatusPeakLoadStartTime = _EPDU2BankStatusPeakLoadStartTime_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 5, 4, 1, 8),
    _EPDU2BankStatusPeakLoadStartTime_Type()
)
ePDU2BankStatusPeakLoadStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2BankStatusPeakLoadStartTime.setStatus("mandatory")
_EPDU2Outlet_ObjectIdentity = ObjectIdentity
ePDU2Outlet = _EPDU2Outlet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6)
)
_EPDU2OutletSwitched_ObjectIdentity = ObjectIdentity
ePDU2OutletSwitched = _EPDU2OutletSwitched_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 1)
)
_EPDU2OutletSwitchedTableSize_Type = Integer32
_EPDU2OutletSwitchedTableSize_Object = MibScalar
ePDU2OutletSwitchedTableSize = _EPDU2OutletSwitchedTableSize_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 1, 1),
    _EPDU2OutletSwitchedTableSize_Type()
)
ePDU2OutletSwitchedTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2OutletSwitchedTableSize.setStatus("mandatory")
_EPDU2OutletSwitchedConfigTable_Object = MibTable
ePDU2OutletSwitchedConfigTable = _EPDU2OutletSwitchedConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 1, 2)
)
if mibBuilder.loadTexts:
    ePDU2OutletSwitchedConfigTable.setStatus("mandatory")
_EPDU2OutletSwitchedConfigEntry_Object = MibTableRow
ePDU2OutletSwitchedConfigEntry = _EPDU2OutletSwitchedConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 1, 2, 1)
)
ePDU2OutletSwitchedConfigEntry.setIndexNames(
    (0, "CPS-MIB", "ePDU2OutletSwitchedConfigIndex"),
)
if mibBuilder.loadTexts:
    ePDU2OutletSwitchedConfigEntry.setStatus("mandatory")


class _EPDU2OutletSwitchedConfigIndex_Type(Integer32):
    """Custom type ePDU2OutletSwitchedConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_EPDU2OutletSwitchedConfigIndex_Type.__name__ = "Integer32"
_EPDU2OutletSwitchedConfigIndex_Object = MibTableColumn
ePDU2OutletSwitchedConfigIndex = _EPDU2OutletSwitchedConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 1, 2, 1, 1),
    _EPDU2OutletSwitchedConfigIndex_Type()
)
ePDU2OutletSwitchedConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2OutletSwitchedConfigIndex.setStatus("mandatory")
_EPDU2OutletSwitchedConfigModuleIndex_Type = Integer32
_EPDU2OutletSwitchedConfigModuleIndex_Object = MibTableColumn
ePDU2OutletSwitchedConfigModuleIndex = _EPDU2OutletSwitchedConfigModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 1, 2, 1, 2),
    _EPDU2OutletSwitchedConfigModuleIndex_Type()
)
ePDU2OutletSwitchedConfigModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2OutletSwitchedConfigModuleIndex.setStatus("mandatory")
_EPDU2OutletSwitchedConfigNumber_Type = Integer32
_EPDU2OutletSwitchedConfigNumber_Object = MibTableColumn
ePDU2OutletSwitchedConfigNumber = _EPDU2OutletSwitchedConfigNumber_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 1, 2, 1, 3),
    _EPDU2OutletSwitchedConfigNumber_Type()
)
ePDU2OutletSwitchedConfigNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2OutletSwitchedConfigNumber.setStatus("mandatory")
_EPDU2OutletSwitchedConfigName_Type = DisplayString
_EPDU2OutletSwitchedConfigName_Object = MibTableColumn
ePDU2OutletSwitchedConfigName = _EPDU2OutletSwitchedConfigName_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 1, 2, 1, 4),
    _EPDU2OutletSwitchedConfigName_Type()
)
ePDU2OutletSwitchedConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDU2OutletSwitchedConfigName.setStatus("mandatory")
_EPDU2OutletSwitchedConfigPowerOnTime_Type = Integer32
_EPDU2OutletSwitchedConfigPowerOnTime_Object = MibTableColumn
ePDU2OutletSwitchedConfigPowerOnTime = _EPDU2OutletSwitchedConfigPowerOnTime_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 1, 2, 1, 5),
    _EPDU2OutletSwitchedConfigPowerOnTime_Type()
)
ePDU2OutletSwitchedConfigPowerOnTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDU2OutletSwitchedConfigPowerOnTime.setStatus("mandatory")
_EPDU2OutletSwitchedConfigPowerOffTime_Type = Integer32
_EPDU2OutletSwitchedConfigPowerOffTime_Object = MibTableColumn
ePDU2OutletSwitchedConfigPowerOffTime = _EPDU2OutletSwitchedConfigPowerOffTime_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 1, 2, 1, 6),
    _EPDU2OutletSwitchedConfigPowerOffTime_Type()
)
ePDU2OutletSwitchedConfigPowerOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDU2OutletSwitchedConfigPowerOffTime.setStatus("mandatory")
_EPDU2OutletSwitchedConfigRebootDuration_Type = Integer32
_EPDU2OutletSwitchedConfigRebootDuration_Object = MibTableColumn
ePDU2OutletSwitchedConfigRebootDuration = _EPDU2OutletSwitchedConfigRebootDuration_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 1, 2, 1, 7),
    _EPDU2OutletSwitchedConfigRebootDuration_Type()
)
ePDU2OutletSwitchedConfigRebootDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDU2OutletSwitchedConfigRebootDuration.setStatus("mandatory")
_EPDU2OutletSwitchedInfoTable_Object = MibTable
ePDU2OutletSwitchedInfoTable = _EPDU2OutletSwitchedInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 1, 3)
)
if mibBuilder.loadTexts:
    ePDU2OutletSwitchedInfoTable.setStatus("mandatory")
_EPDU2OutletSwitchedInfoEntry_Object = MibTableRow
ePDU2OutletSwitchedInfoEntry = _EPDU2OutletSwitchedInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 1, 3, 1)
)
ePDU2OutletSwitchedInfoEntry.setIndexNames(
    (0, "CPS-MIB", "ePDU2OutletSwitchedInfoIndex"),
)
if mibBuilder.loadTexts:
    ePDU2OutletSwitchedInfoEntry.setStatus("mandatory")


class _EPDU2OutletSwitchedInfoIndex_Type(Integer32):
    """Custom type ePDU2OutletSwitchedInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_EPDU2OutletSwitchedInfoIndex_Type.__name__ = "Integer32"
_EPDU2OutletSwitchedInfoIndex_Object = MibTableColumn
ePDU2OutletSwitchedInfoIndex = _EPDU2OutletSwitchedInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 1, 3, 1, 1),
    _EPDU2OutletSwitchedInfoIndex_Type()
)
ePDU2OutletSwitchedInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2OutletSwitchedInfoIndex.setStatus("mandatory")
_EPDU2OutletSwitchedInfoModuleIndex_Type = Integer32
_EPDU2OutletSwitchedInfoModuleIndex_Object = MibTableColumn
ePDU2OutletSwitchedInfoModuleIndex = _EPDU2OutletSwitchedInfoModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 1, 3, 1, 2),
    _EPDU2OutletSwitchedInfoModuleIndex_Type()
)
ePDU2OutletSwitchedInfoModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2OutletSwitchedInfoModuleIndex.setStatus("mandatory")
_EPDU2OutletSwitchedInfoNumber_Type = Integer32
_EPDU2OutletSwitchedInfoNumber_Object = MibTableColumn
ePDU2OutletSwitchedInfoNumber = _EPDU2OutletSwitchedInfoNumber_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 1, 3, 1, 3),
    _EPDU2OutletSwitchedInfoNumber_Type()
)
ePDU2OutletSwitchedInfoNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2OutletSwitchedInfoNumber.setStatus("mandatory")
_EPDU2OutletSwitchedInfoName_Type = DisplayString
_EPDU2OutletSwitchedInfoName_Object = MibTableColumn
ePDU2OutletSwitchedInfoName = _EPDU2OutletSwitchedInfoName_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 1, 3, 1, 4),
    _EPDU2OutletSwitchedInfoName_Type()
)
ePDU2OutletSwitchedInfoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2OutletSwitchedInfoName.setStatus("mandatory")
_EPDU2OutletSwitchedInfoPhaseLayout_Type = Integer32
_EPDU2OutletSwitchedInfoPhaseLayout_Object = MibTableColumn
ePDU2OutletSwitchedInfoPhaseLayout = _EPDU2OutletSwitchedInfoPhaseLayout_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 1, 3, 1, 5),
    _EPDU2OutletSwitchedInfoPhaseLayout_Type()
)
ePDU2OutletSwitchedInfoPhaseLayout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2OutletSwitchedInfoPhaseLayout.setStatus("mandatory")
_EPDU2OutletSwitchedInfoBank_Type = Integer32
_EPDU2OutletSwitchedInfoBank_Object = MibTableColumn
ePDU2OutletSwitchedInfoBank = _EPDU2OutletSwitchedInfoBank_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 1, 3, 1, 6),
    _EPDU2OutletSwitchedInfoBank_Type()
)
ePDU2OutletSwitchedInfoBank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2OutletSwitchedInfoBank.setStatus("mandatory")
_EPDU2OutletSwitchedStatusTable_Object = MibTable
ePDU2OutletSwitchedStatusTable = _EPDU2OutletSwitchedStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 1, 4)
)
if mibBuilder.loadTexts:
    ePDU2OutletSwitchedStatusTable.setStatus("mandatory")
_EPDU2OutletSwitchedStatusEntry_Object = MibTableRow
ePDU2OutletSwitchedStatusEntry = _EPDU2OutletSwitchedStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 1, 4, 1)
)
ePDU2OutletSwitchedStatusEntry.setIndexNames(
    (0, "CPS-MIB", "ePDU2OutletSwitchedStatusIndex"),
)
if mibBuilder.loadTexts:
    ePDU2OutletSwitchedStatusEntry.setStatus("mandatory")


class _EPDU2OutletSwitchedStatusIndex_Type(Integer32):
    """Custom type ePDU2OutletSwitchedStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_EPDU2OutletSwitchedStatusIndex_Type.__name__ = "Integer32"
_EPDU2OutletSwitchedStatusIndex_Object = MibTableColumn
ePDU2OutletSwitchedStatusIndex = _EPDU2OutletSwitchedStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 1, 4, 1, 1),
    _EPDU2OutletSwitchedStatusIndex_Type()
)
ePDU2OutletSwitchedStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2OutletSwitchedStatusIndex.setStatus("mandatory")
_EPDU2OutletSwitchedStatusModuleIndex_Type = Integer32
_EPDU2OutletSwitchedStatusModuleIndex_Object = MibTableColumn
ePDU2OutletSwitchedStatusModuleIndex = _EPDU2OutletSwitchedStatusModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 1, 4, 1, 2),
    _EPDU2OutletSwitchedStatusModuleIndex_Type()
)
ePDU2OutletSwitchedStatusModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2OutletSwitchedStatusModuleIndex.setStatus("mandatory")
_EPDU2OutletSwitchedStatusNumber_Type = Integer32
_EPDU2OutletSwitchedStatusNumber_Object = MibTableColumn
ePDU2OutletSwitchedStatusNumber = _EPDU2OutletSwitchedStatusNumber_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 1, 4, 1, 3),
    _EPDU2OutletSwitchedStatusNumber_Type()
)
ePDU2OutletSwitchedStatusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2OutletSwitchedStatusNumber.setStatus("mandatory")
_EPDU2OutletSwitchedStatusName_Type = DisplayString
_EPDU2OutletSwitchedStatusName_Object = MibTableColumn
ePDU2OutletSwitchedStatusName = _EPDU2OutletSwitchedStatusName_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 1, 4, 1, 4),
    _EPDU2OutletSwitchedStatusName_Type()
)
ePDU2OutletSwitchedStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2OutletSwitchedStatusName.setStatus("mandatory")


class _EPDU2OutletSwitchedStatusState_Type(Integer32):
    """Custom type ePDU2OutletSwitchedStatusState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("outletStatusOn", 1),
          ("outletStatusOff", 2))
    )


_EPDU2OutletSwitchedStatusState_Type.__name__ = "Integer32"
_EPDU2OutletSwitchedStatusState_Object = MibTableColumn
ePDU2OutletSwitchedStatusState = _EPDU2OutletSwitchedStatusState_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 1, 4, 1, 5),
    _EPDU2OutletSwitchedStatusState_Type()
)
ePDU2OutletSwitchedStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2OutletSwitchedStatusState.setStatus("mandatory")


class _EPDU2OutletSwitchedStatusCommandPending_Type(Integer32):
    """Custom type ePDU2OutletSwitchedStatusCommandPending based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("outletStatusCommandPending", 1),
          ("outletStatusNoCommandPending", 2))
    )


_EPDU2OutletSwitchedStatusCommandPending_Type.__name__ = "Integer32"
_EPDU2OutletSwitchedStatusCommandPending_Object = MibTableColumn
ePDU2OutletSwitchedStatusCommandPending = _EPDU2OutletSwitchedStatusCommandPending_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 1, 4, 1, 6),
    _EPDU2OutletSwitchedStatusCommandPending_Type()
)
ePDU2OutletSwitchedStatusCommandPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2OutletSwitchedStatusCommandPending.setStatus("mandatory")
_EPDU2OutletSwitchedControlTable_Object = MibTable
ePDU2OutletSwitchedControlTable = _EPDU2OutletSwitchedControlTable_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 1, 5)
)
if mibBuilder.loadTexts:
    ePDU2OutletSwitchedControlTable.setStatus("mandatory")
_EPDU2OutletSwitchedControlEntry_Object = MibTableRow
ePDU2OutletSwitchedControlEntry = _EPDU2OutletSwitchedControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 1, 5, 1)
)
ePDU2OutletSwitchedControlEntry.setIndexNames(
    (0, "CPS-MIB", "ePDU2OutletSwitchedControlIndex"),
)
if mibBuilder.loadTexts:
    ePDU2OutletSwitchedControlEntry.setStatus("mandatory")


class _EPDU2OutletSwitchedControlIndex_Type(Integer32):
    """Custom type ePDU2OutletSwitchedControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_EPDU2OutletSwitchedControlIndex_Type.__name__ = "Integer32"
_EPDU2OutletSwitchedControlIndex_Object = MibTableColumn
ePDU2OutletSwitchedControlIndex = _EPDU2OutletSwitchedControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 1, 5, 1, 1),
    _EPDU2OutletSwitchedControlIndex_Type()
)
ePDU2OutletSwitchedControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2OutletSwitchedControlIndex.setStatus("mandatory")
_EPDU2OutletSwitchedControlModuleIndex_Type = Integer32
_EPDU2OutletSwitchedControlModuleIndex_Object = MibTableColumn
ePDU2OutletSwitchedControlModuleIndex = _EPDU2OutletSwitchedControlModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 1, 5, 1, 2),
    _EPDU2OutletSwitchedControlModuleIndex_Type()
)
ePDU2OutletSwitchedControlModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2OutletSwitchedControlModuleIndex.setStatus("mandatory")
_EPDU2OutletSwitchedControlNumber_Type = Integer32
_EPDU2OutletSwitchedControlNumber_Object = MibTableColumn
ePDU2OutletSwitchedControlNumber = _EPDU2OutletSwitchedControlNumber_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 1, 5, 1, 3),
    _EPDU2OutletSwitchedControlNumber_Type()
)
ePDU2OutletSwitchedControlNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2OutletSwitchedControlNumber.setStatus("mandatory")
_EPDU2OutletSwitchedControlName_Type = DisplayString
_EPDU2OutletSwitchedControlName_Object = MibTableColumn
ePDU2OutletSwitchedControlName = _EPDU2OutletSwitchedControlName_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 1, 5, 1, 4),
    _EPDU2OutletSwitchedControlName_Type()
)
ePDU2OutletSwitchedControlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2OutletSwitchedControlName.setStatus("mandatory")


class _EPDU2OutletSwitchedControlCommand_Type(Integer32):
    """Custom type ePDU2OutletSwitchedControlCommand based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("immediateOn", 1),
          ("immediateOff", 2),
          ("immediateReboot", 3),
          ("delayedOn", 4),
          ("delayedOff", 5),
          ("delayedReboot", 6),
          ("cancelPendingCommand", 7),
          ("outletIdentify", 8))
    )


_EPDU2OutletSwitchedControlCommand_Type.__name__ = "Integer32"
_EPDU2OutletSwitchedControlCommand_Object = MibTableColumn
ePDU2OutletSwitchedControlCommand = _EPDU2OutletSwitchedControlCommand_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 1, 5, 1, 5),
    _EPDU2OutletSwitchedControlCommand_Type()
)
ePDU2OutletSwitchedControlCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDU2OutletSwitchedControlCommand.setStatus("mandatory")
_EPDU2OutletMetered_ObjectIdentity = ObjectIdentity
ePDU2OutletMetered = _EPDU2OutletMetered_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 2)
)
_EPDU2OutletMeteredTableSize_Type = Integer32
_EPDU2OutletMeteredTableSize_Object = MibScalar
ePDU2OutletMeteredTableSize = _EPDU2OutletMeteredTableSize_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 2, 1),
    _EPDU2OutletMeteredTableSize_Type()
)
ePDU2OutletMeteredTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2OutletMeteredTableSize.setStatus("mandatory")
_EPDU2OutletMeteredConfigTable_Object = MibTable
ePDU2OutletMeteredConfigTable = _EPDU2OutletMeteredConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 2, 2)
)
if mibBuilder.loadTexts:
    ePDU2OutletMeteredConfigTable.setStatus("mandatory")
_EPDU2OutletMeteredConfigEntry_Object = MibTableRow
ePDU2OutletMeteredConfigEntry = _EPDU2OutletMeteredConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 2, 2, 1)
)
ePDU2OutletMeteredConfigEntry.setIndexNames(
    (0, "CPS-MIB", "ePDU2OutletMeteredConfigIndex"),
)
if mibBuilder.loadTexts:
    ePDU2OutletMeteredConfigEntry.setStatus("mandatory")


class _EPDU2OutletMeteredConfigIndex_Type(Integer32):
    """Custom type ePDU2OutletMeteredConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_EPDU2OutletMeteredConfigIndex_Type.__name__ = "Integer32"
_EPDU2OutletMeteredConfigIndex_Object = MibTableColumn
ePDU2OutletMeteredConfigIndex = _EPDU2OutletMeteredConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 2, 2, 1, 1),
    _EPDU2OutletMeteredConfigIndex_Type()
)
ePDU2OutletMeteredConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2OutletMeteredConfigIndex.setStatus("mandatory")
_EPDU2OutletMeteredConfigModuleIndex_Type = Integer32
_EPDU2OutletMeteredConfigModuleIndex_Object = MibTableColumn
ePDU2OutletMeteredConfigModuleIndex = _EPDU2OutletMeteredConfigModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 2, 2, 1, 2),
    _EPDU2OutletMeteredConfigModuleIndex_Type()
)
ePDU2OutletMeteredConfigModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2OutletMeteredConfigModuleIndex.setStatus("mandatory")
_EPDU2OutletMeteredConfigNumber_Type = Integer32
_EPDU2OutletMeteredConfigNumber_Object = MibTableColumn
ePDU2OutletMeteredConfigNumber = _EPDU2OutletMeteredConfigNumber_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 2, 2, 1, 3),
    _EPDU2OutletMeteredConfigNumber_Type()
)
ePDU2OutletMeteredConfigNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2OutletMeteredConfigNumber.setStatus("mandatory")
_EPDU2OutletMeteredConfigName_Type = DisplayString
_EPDU2OutletMeteredConfigName_Object = MibTableColumn
ePDU2OutletMeteredConfigName = _EPDU2OutletMeteredConfigName_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 2, 2, 1, 4),
    _EPDU2OutletMeteredConfigName_Type()
)
ePDU2OutletMeteredConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDU2OutletMeteredConfigName.setStatus("mandatory")
_EPDU2OutletMeteredConfigLowLoadThreshold_Type = Integer32
_EPDU2OutletMeteredConfigLowLoadThreshold_Object = MibTableColumn
ePDU2OutletMeteredConfigLowLoadThreshold = _EPDU2OutletMeteredConfigLowLoadThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 2, 2, 1, 5),
    _EPDU2OutletMeteredConfigLowLoadThreshold_Type()
)
ePDU2OutletMeteredConfigLowLoadThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDU2OutletMeteredConfigLowLoadThreshold.setStatus("mandatory")
_EPDU2OutletMeteredConfigNearOverloadThreshold_Type = Integer32
_EPDU2OutletMeteredConfigNearOverloadThreshold_Object = MibTableColumn
ePDU2OutletMeteredConfigNearOverloadThreshold = _EPDU2OutletMeteredConfigNearOverloadThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 2, 2, 1, 6),
    _EPDU2OutletMeteredConfigNearOverloadThreshold_Type()
)
ePDU2OutletMeteredConfigNearOverloadThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDU2OutletMeteredConfigNearOverloadThreshold.setStatus("mandatory")
_EPDU2OutletMeteredConfigOverloadThreshold_Type = Integer32
_EPDU2OutletMeteredConfigOverloadThreshold_Object = MibTableColumn
ePDU2OutletMeteredConfigOverloadThreshold = _EPDU2OutletMeteredConfigOverloadThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 2, 2, 1, 7),
    _EPDU2OutletMeteredConfigOverloadThreshold_Type()
)
ePDU2OutletMeteredConfigOverloadThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDU2OutletMeteredConfigOverloadThreshold.setStatus("mandatory")
_EPDU2OutletMeteredInfoTable_Object = MibTable
ePDU2OutletMeteredInfoTable = _EPDU2OutletMeteredInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 2, 3)
)
if mibBuilder.loadTexts:
    ePDU2OutletMeteredInfoTable.setStatus("mandatory")
_EPDU2OutletMeteredInfoEntry_Object = MibTableRow
ePDU2OutletMeteredInfoEntry = _EPDU2OutletMeteredInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 2, 3, 1)
)
ePDU2OutletMeteredInfoEntry.setIndexNames(
    (0, "CPS-MIB", "ePDU2OutletMeteredInfoIndex"),
)
if mibBuilder.loadTexts:
    ePDU2OutletMeteredInfoEntry.setStatus("mandatory")


class _EPDU2OutletMeteredInfoIndex_Type(Integer32):
    """Custom type ePDU2OutletMeteredInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_EPDU2OutletMeteredInfoIndex_Type.__name__ = "Integer32"
_EPDU2OutletMeteredInfoIndex_Object = MibTableColumn
ePDU2OutletMeteredInfoIndex = _EPDU2OutletMeteredInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 2, 3, 1, 1),
    _EPDU2OutletMeteredInfoIndex_Type()
)
ePDU2OutletMeteredInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2OutletMeteredInfoIndex.setStatus("mandatory")
_EPDU2OutletMeteredInfoModuleIndex_Type = Integer32
_EPDU2OutletMeteredInfoModuleIndex_Object = MibTableColumn
ePDU2OutletMeteredInfoModuleIndex = _EPDU2OutletMeteredInfoModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 2, 3, 1, 2),
    _EPDU2OutletMeteredInfoModuleIndex_Type()
)
ePDU2OutletMeteredInfoModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2OutletMeteredInfoModuleIndex.setStatus("mandatory")
_EPDU2OutletMeteredInfoNumber_Type = Integer32
_EPDU2OutletMeteredInfoNumber_Object = MibTableColumn
ePDU2OutletMeteredInfoNumber = _EPDU2OutletMeteredInfoNumber_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 2, 3, 1, 3),
    _EPDU2OutletMeteredInfoNumber_Type()
)
ePDU2OutletMeteredInfoNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2OutletMeteredInfoNumber.setStatus("mandatory")
_EPDU2OutletMeteredInfoName_Type = DisplayString
_EPDU2OutletMeteredInfoName_Object = MibTableColumn
ePDU2OutletMeteredInfoName = _EPDU2OutletMeteredInfoName_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 2, 3, 1, 4),
    _EPDU2OutletMeteredInfoName_Type()
)
ePDU2OutletMeteredInfoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2OutletMeteredInfoName.setStatus("mandatory")
_EPDU2OutletMeteredInfoLayout_Type = Integer32
_EPDU2OutletMeteredInfoLayout_Object = MibTableColumn
ePDU2OutletMeteredInfoLayout = _EPDU2OutletMeteredInfoLayout_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 2, 3, 1, 5),
    _EPDU2OutletMeteredInfoLayout_Type()
)
ePDU2OutletMeteredInfoLayout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2OutletMeteredInfoLayout.setStatus("mandatory")
_EPDU2OutletMeteredInfoRating_Type = Integer32
_EPDU2OutletMeteredInfoRating_Object = MibTableColumn
ePDU2OutletMeteredInfoRating = _EPDU2OutletMeteredInfoRating_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 2, 3, 1, 6),
    _EPDU2OutletMeteredInfoRating_Type()
)
ePDU2OutletMeteredInfoRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2OutletMeteredInfoRating.setStatus("mandatory")
_EPDU2OutletMeteredInfoBank_Type = Integer32
_EPDU2OutletMeteredInfoBank_Object = MibTableColumn
ePDU2OutletMeteredInfoBank = _EPDU2OutletMeteredInfoBank_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 2, 3, 1, 7),
    _EPDU2OutletMeteredInfoBank_Type()
)
ePDU2OutletMeteredInfoBank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2OutletMeteredInfoBank.setStatus("mandatory")
_EPDU2OutletMeteredStatusTable_Object = MibTable
ePDU2OutletMeteredStatusTable = _EPDU2OutletMeteredStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 2, 4)
)
if mibBuilder.loadTexts:
    ePDU2OutletMeteredStatusTable.setStatus("mandatory")
_EPDU2OutletMeteredStatusEntry_Object = MibTableRow
ePDU2OutletMeteredStatusEntry = _EPDU2OutletMeteredStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 2, 4, 1)
)
ePDU2OutletMeteredStatusEntry.setIndexNames(
    (0, "CPS-MIB", "ePDU2OutletMeteredStatusIndex"),
)
if mibBuilder.loadTexts:
    ePDU2OutletMeteredStatusEntry.setStatus("mandatory")


class _EPDU2OutletMeteredStatusIndex_Type(Integer32):
    """Custom type ePDU2OutletMeteredStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_EPDU2OutletMeteredStatusIndex_Type.__name__ = "Integer32"
_EPDU2OutletMeteredStatusIndex_Object = MibTableColumn
ePDU2OutletMeteredStatusIndex = _EPDU2OutletMeteredStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 2, 4, 1, 1),
    _EPDU2OutletMeteredStatusIndex_Type()
)
ePDU2OutletMeteredStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2OutletMeteredStatusIndex.setStatus("mandatory")
_EPDU2OutletMeteredStatusModuleIndex_Type = Integer32
_EPDU2OutletMeteredStatusModuleIndex_Object = MibTableColumn
ePDU2OutletMeteredStatusModuleIndex = _EPDU2OutletMeteredStatusModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 2, 4, 1, 2),
    _EPDU2OutletMeteredStatusModuleIndex_Type()
)
ePDU2OutletMeteredStatusModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2OutletMeteredStatusModuleIndex.setStatus("mandatory")
_EPDU2OutletMeteredStatusNumber_Type = Integer32
_EPDU2OutletMeteredStatusNumber_Object = MibTableColumn
ePDU2OutletMeteredStatusNumber = _EPDU2OutletMeteredStatusNumber_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 2, 4, 1, 3),
    _EPDU2OutletMeteredStatusNumber_Type()
)
ePDU2OutletMeteredStatusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2OutletMeteredStatusNumber.setStatus("mandatory")
_EPDU2OutletMeteredStatusName_Type = DisplayString
_EPDU2OutletMeteredStatusName_Object = MibTableColumn
ePDU2OutletMeteredStatusName = _EPDU2OutletMeteredStatusName_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 2, 4, 1, 4),
    _EPDU2OutletMeteredStatusName_Type()
)
ePDU2OutletMeteredStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2OutletMeteredStatusName.setStatus("mandatory")


class _EPDU2OutletMeteredStatusAlarm_Type(Integer32):
    """Custom type ePDU2OutletMeteredStatusAlarm based on Integer32"""
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
        *(("noLoadAlarm", 1),
          ("underCurrentAlarm", 2),
          ("nearOverCurrentAlarm", 3),
          ("overCurrentAlarm", 4))
    )


_EPDU2OutletMeteredStatusAlarm_Type.__name__ = "Integer32"
_EPDU2OutletMeteredStatusAlarm_Object = MibTableColumn
ePDU2OutletMeteredStatusAlarm = _EPDU2OutletMeteredStatusAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 2, 4, 1, 5),
    _EPDU2OutletMeteredStatusAlarm_Type()
)
ePDU2OutletMeteredStatusAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2OutletMeteredStatusAlarm.setStatus("mandatory")
_EPDU2OutletMeteredStatusLoad_Type = Gauge32
_EPDU2OutletMeteredStatusLoad_Object = MibTableColumn
ePDU2OutletMeteredStatusLoad = _EPDU2OutletMeteredStatusLoad_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 2, 4, 1, 6),
    _EPDU2OutletMeteredStatusLoad_Type()
)
ePDU2OutletMeteredStatusLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2OutletMeteredStatusLoad.setStatus("mandatory")
_EPDU2OutletMeteredStatusActivePower_Type = Gauge32
_EPDU2OutletMeteredStatusActivePower_Object = MibTableColumn
ePDU2OutletMeteredStatusActivePower = _EPDU2OutletMeteredStatusActivePower_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 2, 4, 1, 7),
    _EPDU2OutletMeteredStatusActivePower_Type()
)
ePDU2OutletMeteredStatusActivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2OutletMeteredStatusActivePower.setStatus("mandatory")
_EPDU2OutletMeteredStatusPeakPower_Type = Gauge32
_EPDU2OutletMeteredStatusPeakPower_Object = MibTableColumn
ePDU2OutletMeteredStatusPeakPower = _EPDU2OutletMeteredStatusPeakPower_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 2, 4, 1, 8),
    _EPDU2OutletMeteredStatusPeakPower_Type()
)
ePDU2OutletMeteredStatusPeakPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2OutletMeteredStatusPeakPower.setStatus("mandatory")
_EPDU2OutletMeteredStatusPeakPowerTimestamp_Type = DisplayString
_EPDU2OutletMeteredStatusPeakPowerTimestamp_Object = MibTableColumn
ePDU2OutletMeteredStatusPeakPowerTimestamp = _EPDU2OutletMeteredStatusPeakPowerTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 2, 4, 1, 9),
    _EPDU2OutletMeteredStatusPeakPowerTimestamp_Type()
)
ePDU2OutletMeteredStatusPeakPowerTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2OutletMeteredStatusPeakPowerTimestamp.setStatus("mandatory")
_EPDU2OutletMeteredStatusPeakPowerStartTime_Type = DisplayString
_EPDU2OutletMeteredStatusPeakPowerStartTime_Object = MibTableColumn
ePDU2OutletMeteredStatusPeakPowerStartTime = _EPDU2OutletMeteredStatusPeakPowerStartTime_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 2, 4, 1, 10),
    _EPDU2OutletMeteredStatusPeakPowerStartTime_Type()
)
ePDU2OutletMeteredStatusPeakPowerStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2OutletMeteredStatusPeakPowerStartTime.setStatus("mandatory")
_EPDU2OutletMeteredStatusEnergy_Type = Gauge32
_EPDU2OutletMeteredStatusEnergy_Object = MibTableColumn
ePDU2OutletMeteredStatusEnergy = _EPDU2OutletMeteredStatusEnergy_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 2, 4, 1, 11),
    _EPDU2OutletMeteredStatusEnergy_Type()
)
ePDU2OutletMeteredStatusEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2OutletMeteredStatusEnergy.setStatus("mandatory")
_EPDU2OutletMeteredStatusEnergyStart_Type = DisplayString
_EPDU2OutletMeteredStatusEnergyStart_Object = MibTableColumn
ePDU2OutletMeteredStatusEnergyStart = _EPDU2OutletMeteredStatusEnergyStart_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 6, 2, 4, 1, 12),
    _EPDU2OutletMeteredStatusEnergyStart_Type()
)
ePDU2OutletMeteredStatusEnergyStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2OutletMeteredStatusEnergyStart.setStatus("mandatory")
_EPDU2Sensor_ObjectIdentity = ObjectIdentity
ePDU2Sensor = _EPDU2Sensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 7)
)
_EPDU2SensorTableSize_Type = Integer32
_EPDU2SensorTableSize_Object = MibScalar
ePDU2SensorTableSize = _EPDU2SensorTableSize_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 7, 1),
    _EPDU2SensorTableSize_Type()
)
ePDU2SensorTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2SensorTableSize.setStatus("mandatory")
_EPDU2Group_ObjectIdentity = ObjectIdentity
ePDU2Group = _EPDU2Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 8)
)
_EPDU2GroupNumberOfDevices_Type = Integer32
_EPDU2GroupNumberOfDevices_Object = MibScalar
ePDU2GroupNumberOfDevices = _EPDU2GroupNumberOfDevices_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 8, 1),
    _EPDU2GroupNumberOfDevices_Type()
)
ePDU2GroupNumberOfDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2GroupNumberOfDevices.setStatus("mandatory")
_EPDU2GroupTotalPower_Type = Gauge32
_EPDU2GroupTotalPower_Object = MibScalar
ePDU2GroupTotalPower = _EPDU2GroupTotalPower_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 8, 2),
    _EPDU2GroupTotalPower_Type()
)
ePDU2GroupTotalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2GroupTotalPower.setStatus("mandatory")
_EPDU2GroupTotalEnergy_Type = Gauge32
_EPDU2GroupTotalEnergy_Object = MibScalar
ePDU2GroupTotalEnergy = _EPDU2GroupTotalEnergy_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 8, 3),
    _EPDU2GroupTotalEnergy_Type()
)
ePDU2GroupTotalEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePDU2GroupTotalEnergy.setStatus("mandatory")


class _EPDU2GroupEnergyReset_Type(Integer32):
    """Custom type ePDU2GroupEnergyReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noOperation", 1),
          ("reset", 2))
    )


_EPDU2GroupEnergyReset_Type.__name__ = "Integer32"
_EPDU2GroupEnergyReset_Object = MibScalar
ePDU2GroupEnergyReset = _EPDU2GroupEnergyReset_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 8, 4),
    _EPDU2GroupEnergyReset_Type()
)
ePDU2GroupEnergyReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDU2GroupEnergyReset.setStatus("mandatory")


class _EPDU2GroupPeakRecordReset_Type(Integer32):
    """Custom type ePDU2GroupPeakRecordReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noOperation", 1),
          ("reset", 2))
    )


_EPDU2GroupPeakRecordReset_Type.__name__ = "Integer32"
_EPDU2GroupPeakRecordReset_Object = MibScalar
ePDU2GroupPeakRecordReset = _EPDU2GroupPeakRecordReset_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 6, 8, 5),
    _EPDU2GroupPeakRecordReset_Type()
)
ePDU2GroupPeakRecordReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePDU2GroupPeakRecordReset.setStatus("mandatory")
_Battmgr_ObjectIdentity = ObjectIdentity
battmgr = _Battmgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7)
)
_BmIdent_ObjectIdentity = ObjectIdentity
bmIdent = _BmIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 1)
)
_BmIdentModelName_Type = DisplayString
_BmIdentModelName_Object = MibScalar
bmIdentModelName = _BmIdentModelName_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 1, 1),
    _BmIdentModelName_Type()
)
bmIdentModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmIdentModelName.setStatus("mandatory")
_BmIdentHardwareRev_Type = DisplayString
_BmIdentHardwareRev_Object = MibScalar
bmIdentHardwareRev = _BmIdentHardwareRev_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 1, 2),
    _BmIdentHardwareRev_Type()
)
bmIdentHardwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmIdentHardwareRev.setStatus("mandatory")
_BmIdentFirmwareRev_Type = DisplayString
_BmIdentFirmwareRev_Object = MibScalar
bmIdentFirmwareRev = _BmIdentFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 1, 3),
    _BmIdentFirmwareRev_Type()
)
bmIdentFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmIdentFirmwareRev.setStatus("mandatory")
_BmIdentLCDHardwareRev_Type = DisplayString
_BmIdentLCDHardwareRev_Object = MibScalar
bmIdentLCDHardwareRev = _BmIdentLCDHardwareRev_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 1, 4),
    _BmIdentLCDHardwareRev_Type()
)
bmIdentLCDHardwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmIdentLCDHardwareRev.setStatus("mandatory")
_BmIdentLCDFirmwareRev_Type = DisplayString
_BmIdentLCDFirmwareRev_Object = MibScalar
bmIdentLCDFirmwareRev = _BmIdentLCDFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 1, 5),
    _BmIdentLCDFirmwareRev_Type()
)
bmIdentLCDFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmIdentLCDFirmwareRev.setStatus("mandatory")
_BmIdentDateOfManufacture_Type = DisplayString
_BmIdentDateOfManufacture_Object = MibScalar
bmIdentDateOfManufacture = _BmIdentDateOfManufacture_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 1, 6),
    _BmIdentDateOfManufacture_Type()
)
bmIdentDateOfManufacture.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmIdentDateOfManufacture.setStatus("mandatory")
_BmIdentSerialNumber_Type = DisplayString
_BmIdentSerialNumber_Object = MibScalar
bmIdentSerialNumber = _BmIdentSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 1, 7),
    _BmIdentSerialNumber_Type()
)
bmIdentSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmIdentSerialNumber.setStatus("mandatory")
_BmIdentName_Type = DisplayString
_BmIdentName_Object = MibScalar
bmIdentName = _BmIdentName_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 1, 8),
    _BmIdentName_Type()
)
bmIdentName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmIdentName.setStatus("mandatory")
_BmIdentLocation_Type = DisplayString
_BmIdentLocation_Object = MibScalar
bmIdentLocation = _BmIdentLocation_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 1, 9),
    _BmIdentLocation_Type()
)
bmIdentLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmIdentLocation.setStatus("mandatory")
_BmProperty_ObjectIdentity = ObjectIdentity
bmProperty = _BmProperty_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 2)
)
_BmPropertyStringMax_Type = Integer32
_BmPropertyStringMax_Object = MibScalar
bmPropertyStringMax = _BmPropertyStringMax_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 2, 1),
    _BmPropertyStringMax_Type()
)
bmPropertyStringMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmPropertyStringMax.setStatus("mandatory")
_BmPropertyMaxProbeOnString_Type = Integer32
_BmPropertyMaxProbeOnString_Object = MibScalar
bmPropertyMaxProbeOnString = _BmPropertyMaxProbeOnString_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 2, 2),
    _BmPropertyMaxProbeOnString_Type()
)
bmPropertyMaxProbeOnString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmPropertyMaxProbeOnString.setStatus("mandatory")
_BmPropertyInputVoltageRange_Type = DisplayString
_BmPropertyInputVoltageRange_Object = MibScalar
bmPropertyInputVoltageRange = _BmPropertyInputVoltageRange_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 2, 3),
    _BmPropertyInputVoltageRange_Type()
)
bmPropertyInputVoltageRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmPropertyInputVoltageRange.setStatus("mandatory")


class _BmPropertyProbesRating_Type(Integer32):
    """Custom type bmPropertyProbesRating based on Integer32"""
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
        *(("probeUnknown", 1),
          ("probe2V", 2),
          ("probe4V", 3),
          ("probe6V", 4),
          ("probe12V", 5),
          ("probeMixed", 6))
    )


_BmPropertyProbesRating_Type.__name__ = "Integer32"
_BmPropertyProbesRating_Object = MibScalar
bmPropertyProbesRating = _BmPropertyProbesRating_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 2, 4),
    _BmPropertyProbesRating_Type()
)
bmPropertyProbesRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmPropertyProbesRating.setStatus("mandatory")
_BmConfig_ObjectIdentity = ObjectIdentity
bmConfig = _BmConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 3)
)
_BmConfigBattAH_Type = Integer32
_BmConfigBattAH_Object = MibScalar
bmConfigBattAH = _BmConfigBattAH_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 3, 1),
    _BmConfigBattAH_Type()
)
bmConfigBattAH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmConfigBattAH.setStatus("mandatory")
_BmConfigStringCount_Type = Integer32
_BmConfigStringCount_Object = MibScalar
bmConfigStringCount = _BmConfigStringCount_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 3, 2),
    _BmConfigStringCount_Type()
)
bmConfigStringCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmConfigStringCount.setStatus("mandatory")
_BmConfigProbesCountOnString_Type = Integer32
_BmConfigProbesCountOnString_Object = MibScalar
bmConfigProbesCountOnString = _BmConfigProbesCountOnString_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 3, 3),
    _BmConfigProbesCountOnString_Type()
)
bmConfigProbesCountOnString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmConfigProbesCountOnString.setStatus("mandatory")
_BmConfigLowVoltAlarmThreshold_Type = Integer32
_BmConfigLowVoltAlarmThreshold_Object = MibScalar
bmConfigLowVoltAlarmThreshold = _BmConfigLowVoltAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 3, 4),
    _BmConfigLowVoltAlarmThreshold_Type()
)
bmConfigLowVoltAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmConfigLowVoltAlarmThreshold.setStatus("mandatory")
_BmConfigHighVoltAlarmThreshold_Type = Integer32
_BmConfigHighVoltAlarmThreshold_Object = MibScalar
bmConfigHighVoltAlarmThreshold = _BmConfigHighVoltAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 3, 5),
    _BmConfigHighVoltAlarmThreshold_Type()
)
bmConfigHighVoltAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmConfigHighVoltAlarmThreshold.setStatus("mandatory")
_BmConfigVoltDiffAlarmThreshold_Type = Integer32
_BmConfigVoltDiffAlarmThreshold_Object = MibScalar
bmConfigVoltDiffAlarmThreshold = _BmConfigVoltDiffAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 3, 6),
    _BmConfigVoltDiffAlarmThreshold_Type()
)
bmConfigVoltDiffAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmConfigVoltDiffAlarmThreshold.setStatus("mandatory")
_BmConfigLowTempAlarmThreshold_Type = Integer32
_BmConfigLowTempAlarmThreshold_Object = MibScalar
bmConfigLowTempAlarmThreshold = _BmConfigLowTempAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 3, 7),
    _BmConfigLowTempAlarmThreshold_Type()
)
bmConfigLowTempAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmConfigLowTempAlarmThreshold.setStatus("mandatory")
_BmConfigHighTempAlarmThreshold_Type = Integer32
_BmConfigHighTempAlarmThreshold_Object = MibScalar
bmConfigHighTempAlarmThreshold = _BmConfigHighTempAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 3, 8),
    _BmConfigHighTempAlarmThreshold_Type()
)
bmConfigHighTempAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmConfigHighTempAlarmThreshold.setStatus("mandatory")
_BmConfigLowResAlarmThreshold_Type = Integer32
_BmConfigLowResAlarmThreshold_Object = MibScalar
bmConfigLowResAlarmThreshold = _BmConfigLowResAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 3, 9),
    _BmConfigLowResAlarmThreshold_Type()
)
bmConfigLowResAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmConfigLowResAlarmThreshold.setStatus("mandatory")
_BmConfigHighResAlarmThreshold_Type = Integer32
_BmConfigHighResAlarmThreshold_Object = MibScalar
bmConfigHighResAlarmThreshold = _BmConfigHighResAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 3, 10),
    _BmConfigHighResAlarmThreshold_Type()
)
bmConfigHighResAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmConfigHighResAlarmThreshold.setStatus("mandatory")
_BmConfigLowResWarnThreshold_Type = Integer32
_BmConfigLowResWarnThreshold_Object = MibScalar
bmConfigLowResWarnThreshold = _BmConfigLowResWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 3, 11),
    _BmConfigLowResWarnThreshold_Type()
)
bmConfigLowResWarnThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmConfigLowResWarnThreshold.setStatus("mandatory")
_BmConfigHighResWarnThreshold_Type = Integer32
_BmConfigHighResWarnThreshold_Object = MibScalar
bmConfigHighResWarnThreshold = _BmConfigHighResWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 3, 12),
    _BmConfigHighResWarnThreshold_Type()
)
bmConfigHighResWarnThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmConfigHighResWarnThreshold.setStatus("mandatory")
_BmConfigResHealthAlarmThreshold_Type = Integer32
_BmConfigResHealthAlarmThreshold_Object = MibScalar
bmConfigResHealthAlarmThreshold = _BmConfigResHealthAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 3, 13),
    _BmConfigResHealthAlarmThreshold_Type()
)
bmConfigResHealthAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmConfigResHealthAlarmThreshold.setStatus("mandatory")
_BmConfigResHealthWarnThreshold_Type = Integer32
_BmConfigResHealthWarnThreshold_Object = MibScalar
bmConfigResHealthWarnThreshold = _BmConfigResHealthWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 3, 14),
    _BmConfigResHealthWarnThreshold_Type()
)
bmConfigResHealthWarnThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmConfigResHealthWarnThreshold.setStatus("mandatory")
_BmConfigLowVoltAlarmThreshold10mV_Type = Integer32
_BmConfigLowVoltAlarmThreshold10mV_Object = MibScalar
bmConfigLowVoltAlarmThreshold10mV = _BmConfigLowVoltAlarmThreshold10mV_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 3, 15),
    _BmConfigLowVoltAlarmThreshold10mV_Type()
)
bmConfigLowVoltAlarmThreshold10mV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmConfigLowVoltAlarmThreshold10mV.setStatus("mandatory")
_BmConfigHighVoltAlarmThreshold10mV_Type = Integer32
_BmConfigHighVoltAlarmThreshold10mV_Object = MibScalar
bmConfigHighVoltAlarmThreshold10mV = _BmConfigHighVoltAlarmThreshold10mV_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 3, 16),
    _BmConfigHighVoltAlarmThreshold10mV_Type()
)
bmConfigHighVoltAlarmThreshold10mV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmConfigHighVoltAlarmThreshold10mV.setStatus("mandatory")


class _BmConfigMergeFeature_Type(Integer32):
    """Custom type bmConfigMergeFeature based on Integer32"""
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


_BmConfigMergeFeature_Type.__name__ = "Integer32"
_BmConfigMergeFeature_Object = MibScalar
bmConfigMergeFeature = _BmConfigMergeFeature_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 3, 17),
    _BmConfigMergeFeature_Type()
)
bmConfigMergeFeature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmConfigMergeFeature.setStatus("mandatory")
_BmControl_ObjectIdentity = ObjectIdentity
bmControl = _BmControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 4)
)


class _BmControlSysytemIdenticator_Type(Integer32):
    """Custom type bmControlSysytemIdenticator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noTestIndicators", 1),
          ("testIndicators", 2))
    )


_BmControlSysytemIdenticator_Type.__name__ = "Integer32"
_BmControlSysytemIdenticator_Object = MibScalar
bmControlSysytemIdenticator = _BmControlSysytemIdenticator_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 4, 1),
    _BmControlSysytemIdenticator_Type()
)
bmControlSysytemIdenticator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmControlSysytemIdenticator.setStatus("mandatory")


class _BmControlProbeIndicator_Type(Integer32):
    """Custom type bmControlProbeIndicator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noTestIndicators", 1),
          ("testIndicators", 2))
    )


_BmControlProbeIndicator_Type.__name__ = "Integer32"
_BmControlProbeIndicator_Object = MibScalar
bmControlProbeIndicator = _BmControlProbeIndicator_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 4, 2),
    _BmControlProbeIndicator_Type()
)
bmControlProbeIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmControlProbeIndicator.setStatus("mandatory")
_BmProbes_ObjectIdentity = ObjectIdentity
bmProbes = _BmProbes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 5)
)
_BmProbesNum_Type = Integer32
_BmProbesNum_Object = MibScalar
bmProbesNum = _BmProbesNum_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 5, 1),
    _BmProbesNum_Type()
)
bmProbesNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmProbesNum.setStatus("mandatory")
_BmProbesTableSize_Type = Integer32
_BmProbesTableSize_Object = MibScalar
bmProbesTableSize = _BmProbesTableSize_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 5, 2),
    _BmProbesTableSize_Type()
)
bmProbesTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmProbesTableSize.setStatus("mandatory")
_BmProbesTable_Object = MibTable
bmProbesTable = _BmProbesTable_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 5, 3)
)
if mibBuilder.loadTexts:
    bmProbesTable.setStatus("mandatory")
_BmProbesEntry_Object = MibTableRow
bmProbesEntry = _BmProbesEntry_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 5, 3, 1)
)
bmProbesEntry.setIndexNames(
    (0, "CPS-MIB", "bmProbesIndex"),
)
if mibBuilder.loadTexts:
    bmProbesEntry.setStatus("mandatory")


class _BmProbesIndex_Type(Integer32):
    """Custom type bmProbesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 960),
    )


_BmProbesIndex_Type.__name__ = "Integer32"
_BmProbesIndex_Object = MibTableColumn
bmProbesIndex = _BmProbesIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 5, 3, 1, 1),
    _BmProbesIndex_Type()
)
bmProbesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmProbesIndex.setStatus("mandatory")


class _BmProbesPackIndex_Type(Integer32):
    """Custom type bmProbesPackIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_BmProbesPackIndex_Type.__name__ = "Integer32"
_BmProbesPackIndex_Object = MibTableColumn
bmProbesPackIndex = _BmProbesPackIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 5, 3, 1, 2),
    _BmProbesPackIndex_Type()
)
bmProbesPackIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmProbesPackIndex.setStatus("mandatory")


class _BmProbesStringIndex_Type(Integer32):
    """Custom type bmProbesStringIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_BmProbesStringIndex_Type.__name__ = "Integer32"
_BmProbesStringIndex_Object = MibTableColumn
bmProbesStringIndex = _BmProbesStringIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 5, 3, 1, 3),
    _BmProbesStringIndex_Type()
)
bmProbesStringIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmProbesStringIndex.setStatus("mandatory")


class _BmProbesBattIndex_Type(Integer32):
    """Custom type bmProbesBattIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 960),
    )


_BmProbesBattIndex_Type.__name__ = "Integer32"
_BmProbesBattIndex_Object = MibTableColumn
bmProbesBattIndex = _BmProbesBattIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 5, 3, 1, 4),
    _BmProbesBattIndex_Type()
)
bmProbesBattIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmProbesBattIndex.setStatus("mandatory")
_BmProbesVoltageTableSize_Type = Integer32
_BmProbesVoltageTableSize_Object = MibScalar
bmProbesVoltageTableSize = _BmProbesVoltageTableSize_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 5, 4),
    _BmProbesVoltageTableSize_Type()
)
bmProbesVoltageTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmProbesVoltageTableSize.setStatus("mandatory")
_BmProbesVoltageTable_Object = MibTable
bmProbesVoltageTable = _BmProbesVoltageTable_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 5, 5)
)
if mibBuilder.loadTexts:
    bmProbesVoltageTable.setStatus("mandatory")
_BmProbesVoltageEntry_Object = MibTableRow
bmProbesVoltageEntry = _BmProbesVoltageEntry_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 5, 5, 1)
)
bmProbesVoltageEntry.setIndexNames(
    (0, "CPS-MIB", "bmProbesVoltageIndex"),
)
if mibBuilder.loadTexts:
    bmProbesVoltageEntry.setStatus("mandatory")


class _BmProbesVoltageIndex_Type(Integer32):
    """Custom type bmProbesVoltageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 960),
    )


_BmProbesVoltageIndex_Type.__name__ = "Integer32"
_BmProbesVoltageIndex_Object = MibTableColumn
bmProbesVoltageIndex = _BmProbesVoltageIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 5, 5, 1, 1),
    _BmProbesVoltageIndex_Type()
)
bmProbesVoltageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmProbesVoltageIndex.setStatus("mandatory")


class _BmProbesVoltagePackIndex_Type(Integer32):
    """Custom type bmProbesVoltagePackIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_BmProbesVoltagePackIndex_Type.__name__ = "Integer32"
_BmProbesVoltagePackIndex_Object = MibTableColumn
bmProbesVoltagePackIndex = _BmProbesVoltagePackIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 5, 5, 1, 2),
    _BmProbesVoltagePackIndex_Type()
)
bmProbesVoltagePackIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmProbesVoltagePackIndex.setStatus("mandatory")


class _BmProbesVoltageStringIndex_Type(Integer32):
    """Custom type bmProbesVoltageStringIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_BmProbesVoltageStringIndex_Type.__name__ = "Integer32"
_BmProbesVoltageStringIndex_Object = MibTableColumn
bmProbesVoltageStringIndex = _BmProbesVoltageStringIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 5, 5, 1, 3),
    _BmProbesVoltageStringIndex_Type()
)
bmProbesVoltageStringIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmProbesVoltageStringIndex.setStatus("mandatory")


class _BmProbesVoltageBattIndex_Type(Integer32):
    """Custom type bmProbesVoltageBattIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 960),
    )


_BmProbesVoltageBattIndex_Type.__name__ = "Integer32"
_BmProbesVoltageBattIndex_Object = MibTableColumn
bmProbesVoltageBattIndex = _BmProbesVoltageBattIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 5, 5, 1, 4),
    _BmProbesVoltageBattIndex_Type()
)
bmProbesVoltageBattIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmProbesVoltageBattIndex.setStatus("mandatory")


class _BmProbesVoltageProbeIndex_Type(Integer32):
    """Custom type bmProbesVoltageProbeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 960),
    )


_BmProbesVoltageProbeIndex_Type.__name__ = "Integer32"
_BmProbesVoltageProbeIndex_Object = MibTableColumn
bmProbesVoltageProbeIndex = _BmProbesVoltageProbeIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 5, 5, 1, 5),
    _BmProbesVoltageProbeIndex_Type()
)
bmProbesVoltageProbeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmProbesVoltageProbeIndex.setStatus("mandatory")


class _BmProbesVoltageAlarmStatus_Type(Integer32):
    """Custom type bmProbesVoltageAlarmStatus based on Integer32"""
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
        *(("voltageNormal", 1),
          ("voltageWarnLow", 2),
          ("voltageWarnHigh", 3),
          ("voltageAlarmLow", 4),
          ("voltageAlarmHigh", 5))
    )


_BmProbesVoltageAlarmStatus_Type.__name__ = "Integer32"
_BmProbesVoltageAlarmStatus_Object = MibTableColumn
bmProbesVoltageAlarmStatus = _BmProbesVoltageAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 5, 5, 1, 6),
    _BmProbesVoltageAlarmStatus_Type()
)
bmProbesVoltageAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmProbesVoltageAlarmStatus.setStatus("mandatory")
_BmProbesVoltage_Type = Integer32
_BmProbesVoltage_Object = MibTableColumn
bmProbesVoltage = _BmProbesVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 5, 5, 1, 7),
    _BmProbesVoltage_Type()
)
bmProbesVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmProbesVoltage.setStatus("mandatory")
_BmProbesVoltageEqualPercentage_Type = Integer32
_BmProbesVoltageEqualPercentage_Object = MibTableColumn
bmProbesVoltageEqualPercentage = _BmProbesVoltageEqualPercentage_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 5, 5, 1, 8),
    _BmProbesVoltageEqualPercentage_Type()
)
bmProbesVoltageEqualPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmProbesVoltageEqualPercentage.setStatus("mandatory")
_BmProbesTempTableSize_Type = Integer32
_BmProbesTempTableSize_Object = MibScalar
bmProbesTempTableSize = _BmProbesTempTableSize_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 5, 6),
    _BmProbesTempTableSize_Type()
)
bmProbesTempTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmProbesTempTableSize.setStatus("mandatory")
_BmProbesTempTable_Object = MibTable
bmProbesTempTable = _BmProbesTempTable_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 5, 7)
)
if mibBuilder.loadTexts:
    bmProbesTempTable.setStatus("mandatory")
_BmProbesTempEntry_Object = MibTableRow
bmProbesTempEntry = _BmProbesTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 5, 7, 1)
)
bmProbesTempEntry.setIndexNames(
    (0, "CPS-MIB", "bmProbesTempIndex"),
)
if mibBuilder.loadTexts:
    bmProbesTempEntry.setStatus("mandatory")


class _BmProbesTempIndex_Type(Integer32):
    """Custom type bmProbesTempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 960),
    )


_BmProbesTempIndex_Type.__name__ = "Integer32"
_BmProbesTempIndex_Object = MibTableColumn
bmProbesTempIndex = _BmProbesTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 5, 7, 1, 1),
    _BmProbesTempIndex_Type()
)
bmProbesTempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmProbesTempIndex.setStatus("mandatory")


class _BmProbesTempPackIndex_Type(Integer32):
    """Custom type bmProbesTempPackIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_BmProbesTempPackIndex_Type.__name__ = "Integer32"
_BmProbesTempPackIndex_Object = MibTableColumn
bmProbesTempPackIndex = _BmProbesTempPackIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 5, 7, 1, 2),
    _BmProbesTempPackIndex_Type()
)
bmProbesTempPackIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmProbesTempPackIndex.setStatus("mandatory")


class _BmProbesTempStringIndex_Type(Integer32):
    """Custom type bmProbesTempStringIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_BmProbesTempStringIndex_Type.__name__ = "Integer32"
_BmProbesTempStringIndex_Object = MibTableColumn
bmProbesTempStringIndex = _BmProbesTempStringIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 5, 7, 1, 3),
    _BmProbesTempStringIndex_Type()
)
bmProbesTempStringIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmProbesTempStringIndex.setStatus("mandatory")


class _BmProbesTempBattIndex_Type(Integer32):
    """Custom type bmProbesTempBattIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 960),
    )


_BmProbesTempBattIndex_Type.__name__ = "Integer32"
_BmProbesTempBattIndex_Object = MibTableColumn
bmProbesTempBattIndex = _BmProbesTempBattIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 5, 7, 1, 4),
    _BmProbesTempBattIndex_Type()
)
bmProbesTempBattIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmProbesTempBattIndex.setStatus("mandatory")


class _BmProbesTempProbeIndex_Type(Integer32):
    """Custom type bmProbesTempProbeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 960),
    )


_BmProbesTempProbeIndex_Type.__name__ = "Integer32"
_BmProbesTempProbeIndex_Object = MibTableColumn
bmProbesTempProbeIndex = _BmProbesTempProbeIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 5, 7, 1, 5),
    _BmProbesTempProbeIndex_Type()
)
bmProbesTempProbeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmProbesTempProbeIndex.setStatus("mandatory")


class _BmProbesTempAlarmStatus_Type(Integer32):
    """Custom type bmProbesTempAlarmStatus based on Integer32"""
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
        *(("temperatureNormal", 1),
          ("temperatureWarnLow", 2),
          ("temperatureWarnHigh", 3),
          ("temperatureAlarmLow", 4),
          ("temperatureAlarmHigh", 5))
    )


_BmProbesTempAlarmStatus_Type.__name__ = "Integer32"
_BmProbesTempAlarmStatus_Object = MibTableColumn
bmProbesTempAlarmStatus = _BmProbesTempAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 5, 7, 1, 6),
    _BmProbesTempAlarmStatus_Type()
)
bmProbesTempAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmProbesTempAlarmStatus.setStatus("mandatory")


class _BmProbesTemperature_Type(Integer32):
    """Custom type bmProbesTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 60),
    )


_BmProbesTemperature_Type.__name__ = "Integer32"
_BmProbesTemperature_Object = MibTableColumn
bmProbesTemperature = _BmProbesTemperature_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 5, 7, 1, 7),
    _BmProbesTemperature_Type()
)
bmProbesTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmProbesTemperature.setStatus("mandatory")
_BmProbesResTableSize_Type = Integer32
_BmProbesResTableSize_Object = MibScalar
bmProbesResTableSize = _BmProbesResTableSize_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 5, 8),
    _BmProbesResTableSize_Type()
)
bmProbesResTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmProbesResTableSize.setStatus("mandatory")
_BmProbesResTable_Object = MibTable
bmProbesResTable = _BmProbesResTable_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 5, 9)
)
if mibBuilder.loadTexts:
    bmProbesResTable.setStatus("mandatory")
_BmProbesResEntry_Object = MibTableRow
bmProbesResEntry = _BmProbesResEntry_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 5, 9, 1)
)
bmProbesResEntry.setIndexNames(
    (0, "CPS-MIB", "bmProbesResIndex"),
)
if mibBuilder.loadTexts:
    bmProbesResEntry.setStatus("mandatory")


class _BmProbesResIndex_Type(Integer32):
    """Custom type bmProbesResIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 960),
    )


_BmProbesResIndex_Type.__name__ = "Integer32"
_BmProbesResIndex_Object = MibTableColumn
bmProbesResIndex = _BmProbesResIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 5, 9, 1, 1),
    _BmProbesResIndex_Type()
)
bmProbesResIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmProbesResIndex.setStatus("mandatory")


class _BmProbesResPackIndex_Type(Integer32):
    """Custom type bmProbesResPackIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_BmProbesResPackIndex_Type.__name__ = "Integer32"
_BmProbesResPackIndex_Object = MibTableColumn
bmProbesResPackIndex = _BmProbesResPackIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 5, 9, 1, 2),
    _BmProbesResPackIndex_Type()
)
bmProbesResPackIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmProbesResPackIndex.setStatus("mandatory")


class _BmProbesResStringIndex_Type(Integer32):
    """Custom type bmProbesResStringIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_BmProbesResStringIndex_Type.__name__ = "Integer32"
_BmProbesResStringIndex_Object = MibTableColumn
bmProbesResStringIndex = _BmProbesResStringIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 5, 9, 1, 3),
    _BmProbesResStringIndex_Type()
)
bmProbesResStringIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmProbesResStringIndex.setStatus("mandatory")


class _BmProbesResBattIndex_Type(Integer32):
    """Custom type bmProbesResBattIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 960),
    )


_BmProbesResBattIndex_Type.__name__ = "Integer32"
_BmProbesResBattIndex_Object = MibTableColumn
bmProbesResBattIndex = _BmProbesResBattIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 5, 9, 1, 4),
    _BmProbesResBattIndex_Type()
)
bmProbesResBattIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmProbesResBattIndex.setStatus("mandatory")


class _BmProbesResProbeIndex_Type(Integer32):
    """Custom type bmProbesResProbeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 960),
    )


_BmProbesResProbeIndex_Type.__name__ = "Integer32"
_BmProbesResProbeIndex_Object = MibTableColumn
bmProbesResProbeIndex = _BmProbesResProbeIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 5, 9, 1, 5),
    _BmProbesResProbeIndex_Type()
)
bmProbesResProbeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmProbesResProbeIndex.setStatus("mandatory")


class _BmProbesResAlarmStatus_Type(Integer32):
    """Custom type bmProbesResAlarmStatus based on Integer32"""
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
        *(("resistanceNormal", 1),
          ("resistanceWarnLow", 2),
          ("resistanceWarnHigh", 3),
          ("resistanceAlarmLow", 4),
          ("resistanceAlarmHigh", 5))
    )


_BmProbesResAlarmStatus_Type.__name__ = "Integer32"
_BmProbesResAlarmStatus_Object = MibTableColumn
bmProbesResAlarmStatus = _BmProbesResAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 5, 9, 1, 6),
    _BmProbesResAlarmStatus_Type()
)
bmProbesResAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmProbesResAlarmStatus.setStatus("mandatory")


class _BmProbesResistance_Type(Integer32):
    """Custom type bmProbesResistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 60),
    )


_BmProbesResistance_Type.__name__ = "Integer32"
_BmProbesResistance_Object = MibTableColumn
bmProbesResistance = _BmProbesResistance_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 5, 9, 1, 7),
    _BmProbesResistance_Type()
)
bmProbesResistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmProbesResistance.setStatus("mandatory")


class _BmProbesResHealth_Type(Integer32):
    """Custom type bmProbesResHealth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 60),
    )


_BmProbesResHealth_Type.__name__ = "Integer32"
_BmProbesResHealth_Object = MibTableColumn
bmProbesResHealth = _BmProbesResHealth_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 5, 9, 1, 8),
    _BmProbesResHealth_Type()
)
bmProbesResHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmProbesResHealth.setStatus("mandatory")
_BmFuncRes_ObjectIdentity = ObjectIdentity
bmFuncRes = _BmFuncRes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 6)
)
_BmFuncResMeasure_ObjectIdentity = ObjectIdentity
bmFuncResMeasure = _BmFuncResMeasure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 6, 1)
)
_BmFuncResMeasureInterval_Type = Integer32
_BmFuncResMeasureInterval_Object = MibScalar
bmFuncResMeasureInterval = _BmFuncResMeasureInterval_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 6, 1, 1),
    _BmFuncResMeasureInterval_Type()
)
bmFuncResMeasureInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmFuncResMeasureInterval.setStatus("mandatory")


class _BmFuncResMeasureManualCmd_Type(Integer32):
    """Custom type bmFuncResMeasureManualCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noResMeasure", 1),
          ("resMeasureNow", 2))
    )


_BmFuncResMeasureManualCmd_Type.__name__ = "Integer32"
_BmFuncResMeasureManualCmd_Object = MibScalar
bmFuncResMeasureManualCmd = _BmFuncResMeasureManualCmd_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 6, 1, 2),
    _BmFuncResMeasureManualCmd_Type()
)
bmFuncResMeasureManualCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmFuncResMeasureManualCmd.setStatus("mandatory")


class _BmFuncResMeasureManualResult_Type(Integer32):
    """Custom type bmFuncResMeasureManualResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              9)
        )
    )
    namedValues = NamedValues(
        *(("resNoManualResult", 1),
          ("resManualProcessing", 2),
          ("resManualComplete", 3),
          ("resManualReject", 9))
    )


_BmFuncResMeasureManualResult_Type.__name__ = "Integer32"
_BmFuncResMeasureManualResult_Object = MibScalar
bmFuncResMeasureManualResult = _BmFuncResMeasureManualResult_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 6, 1, 3),
    _BmFuncResMeasureManualResult_Type()
)
bmFuncResMeasureManualResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmFuncResMeasureManualResult.setStatus("mandatory")
_BmFuncResMeasureLastUpdate_Type = DisplayString
_BmFuncResMeasureLastUpdate_Object = MibScalar
bmFuncResMeasureLastUpdate = _BmFuncResMeasureLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 6, 1, 4),
    _BmFuncResMeasureLastUpdate_Type()
)
bmFuncResMeasureLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmFuncResMeasureLastUpdate.setStatus("mandatory")
_BmFuncEqual_ObjectIdentity = ObjectIdentity
bmFuncEqual = _BmFuncEqual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 7)
)


class _BmFuncEqualEnable_Type(Integer32):
    """Custom type bmFuncEqualEnable based on Integer32"""
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


_BmFuncEqualEnable_Type.__name__ = "Integer32"
_BmFuncEqualEnable_Object = MibScalar
bmFuncEqualEnable = _BmFuncEqualEnable_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 7, 1),
    _BmFuncEqualEnable_Type()
)
bmFuncEqualEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmFuncEqualEnable.setStatus("mandatory")
_BmFuncEqualActiveCond_Type = Integer32
_BmFuncEqualActiveCond_Object = MibScalar
bmFuncEqualActiveCond = _BmFuncEqualActiveCond_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 7, 2),
    _BmFuncEqualActiveCond_Type()
)
bmFuncEqualActiveCond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmFuncEqualActiveCond.setStatus("mandatory")


class _BmFuncEqualStatus_Type(Integer32):
    """Custom type bmFuncEqualStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              9)
        )
    )
    namedValues = NamedValues(
        *(("equalActive", 1),
          ("equalFailed", 2),
          ("equalNotActive", 3),
          ("equalNotSupport", 9))
    )


_BmFuncEqualStatus_Type.__name__ = "Integer32"
_BmFuncEqualStatus_Object = MibScalar
bmFuncEqualStatus = _BmFuncEqualStatus_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 7, 3),
    _BmFuncEqualStatus_Type()
)
bmFuncEqualStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmFuncEqualStatus.setStatus("mandatory")
_BmFuncEqualStartTime_Type = DisplayString
_BmFuncEqualStartTime_Object = MibScalar
bmFuncEqualStartTime = _BmFuncEqualStartTime_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 7, 4),
    _BmFuncEqualStartTime_Type()
)
bmFuncEqualStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmFuncEqualStartTime.setStatus("mandatory")
_BmFuncEqualElapseTime_Type = TimeTicks
_BmFuncEqualElapseTime_Object = MibScalar
bmFuncEqualElapseTime = _BmFuncEqualElapseTime_Object(
    (1, 3, 6, 1, 4, 1, 3808, 1, 1, 7, 7, 5),
    _BmFuncEqualElapseTime_Type()
)
bmFuncEqualElapseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmFuncEqualElapseTime.setStatus("mandatory")
_Cpsmgmt_ObjectIdentity = ObjectIdentity
cpsmgmt = _Cpsmgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 2)
)
_Mconfig_ObjectIdentity = ObjectIdentity
mconfig = _Mconfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 2, 1)
)
_MconfigNumTrapAccepters_Type = Integer32
_MconfigNumTrapAccepters_Object = MibScalar
mconfigNumTrapAccepters = _MconfigNumTrapAccepters_Object(
    (1, 3, 6, 1, 4, 1, 3808, 2, 1, 1),
    _MconfigNumTrapAccepters_Type()
)
mconfigNumTrapAccepters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mconfigNumTrapAccepters.setStatus("mandatory")
_MconfigTrapAccepterTable_Object = MibTable
mconfigTrapAccepterTable = _MconfigTrapAccepterTable_Object(
    (1, 3, 6, 1, 4, 1, 3808, 2, 1, 2)
)
if mibBuilder.loadTexts:
    mconfigTrapAccepterTable.setStatus("mandatory")
_MconfigTrapAccepterEntry_Object = MibTableRow
mconfigTrapAccepterEntry = _MconfigTrapAccepterEntry_Object(
    (1, 3, 6, 1, 4, 1, 3808, 2, 1, 2, 1)
)
mconfigTrapAccepterEntry.setIndexNames(
    (0, "CPS-MIB", "trapIndex"),
)
if mibBuilder.loadTexts:
    mconfigTrapAccepterEntry.setStatus("mandatory")


class _TrapIndex_Type(Integer32):
    """Custom type trapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TrapIndex_Type.__name__ = "Integer32"
_TrapIndex_Object = MibTableColumn
trapIndex = _TrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 3808, 2, 1, 2, 1, 1),
    _TrapIndex_Type()
)
trapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapIndex.setStatus("mandatory")
_AccepterAddr_Type = IpAddress
_AccepterAddr_Object = MibTableColumn
accepterAddr = _AccepterAddr_Object(
    (1, 3, 6, 1, 4, 1, 3808, 2, 1, 2, 1, 2),
    _AccepterAddr_Type()
)
accepterAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accepterAddr.setStatus("mandatory")
_CommunityString_Type = DisplayString
_CommunityString_Object = MibTableColumn
communityString = _CommunityString_Object(
    (1, 3, 6, 1, 4, 1, 3808, 2, 1, 2, 1, 3),
    _CommunityString_Type()
)
communityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    communityString.setStatus("mandatory")


class _SeverityDegree_Type(Integer32):
    """Custom type severityDegree based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("information", 1),
          ("warning", 2),
          ("severe", 3))
    )


_SeverityDegree_Type.__name__ = "Integer32"
_SeverityDegree_Object = MibTableColumn
severityDegree = _SeverityDegree_Object(
    (1, 3, 6, 1, 4, 1, 3808, 2, 1, 2, 1, 4),
    _SeverityDegree_Type()
)
severityDegree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    severityDegree.setStatus("mandatory")


class _AccepterActive_Type(Integer32):
    """Custom type accepterActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AccepterActive_Type.__name__ = "Integer32"
_AccepterActive_Object = MibTableColumn
accepterActive = _AccepterActive_Object(
    (1, 3, 6, 1, 4, 1, 3808, 2, 1, 2, 1, 5),
    _AccepterActive_Type()
)
accepterActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accepterActive.setStatus("mandatory")


class _MconfigDHCPEnabled_Type(Integer32):
    """Custom type mconfigDHCPEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_MconfigDHCPEnabled_Type.__name__ = "Integer32"
_MconfigDHCPEnabled_Object = MibScalar
mconfigDHCPEnabled = _MconfigDHCPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3808, 2, 1, 3),
    _MconfigDHCPEnabled_Type()
)
mconfigDHCPEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mconfigDHCPEnabled.setStatus("mandatory")
_MconfigMyAddr_Type = IpAddress
_MconfigMyAddr_Object = MibScalar
mconfigMyAddr = _MconfigMyAddr_Object(
    (1, 3, 6, 1, 4, 1, 3808, 2, 1, 4),
    _MconfigMyAddr_Type()
)
mconfigMyAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mconfigMyAddr.setStatus("mandatory")
_MconfigClock_ObjectIdentity = ObjectIdentity
mconfigClock = _MconfigClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 2, 1, 5)
)
_MconfigClockDate_Type = DisplayString
_MconfigClockDate_Object = MibScalar
mconfigClockDate = _MconfigClockDate_Object(
    (1, 3, 6, 1, 4, 1, 3808, 2, 1, 5, 1),
    _MconfigClockDate_Type()
)
mconfigClockDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mconfigClockDate.setStatus("mandatory")
_MconfigClockTime_Type = DisplayString
_MconfigClockTime_Object = MibScalar
mconfigClockTime = _MconfigClockTime_Object(
    (1, 3, 6, 1, 4, 1, 3808, 2, 1, 5, 2),
    _MconfigClockTime_Type()
)
mconfigClockTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mconfigClockTime.setStatus("mandatory")
_Mtrapinfo_ObjectIdentity = ObjectIdentity
mtrapinfo = _Mtrapinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 2, 2)
)
_MtrapinfoInteger_Type = Integer32
_MtrapinfoInteger_Object = MibScalar
mtrapinfoInteger = _MtrapinfoInteger_Object(
    (1, 3, 6, 1, 4, 1, 3808, 2, 2, 1),
    _MtrapinfoInteger_Type()
)
mtrapinfoInteger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtrapinfoInteger.setStatus("mandatory")
_MtrapinfoIpAddress_Type = IpAddress
_MtrapinfoIpAddress_Object = MibScalar
mtrapinfoIpAddress = _MtrapinfoIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3808, 2, 2, 2),
    _MtrapinfoIpAddress_Type()
)
mtrapinfoIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtrapinfoIpAddress.setStatus("mandatory")
_MtrapinfoString_Type = DisplayString
_MtrapinfoString_Object = MibScalar
mtrapinfoString = _MtrapinfoString_Object(
    (1, 3, 6, 1, 4, 1, 3808, 2, 2, 3),
    _MtrapinfoString_Type()
)
mtrapinfoString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtrapinfoString.setStatus("mandatory")
_MtrapinfoGauge_Type = Gauge32
_MtrapinfoGauge_Object = MibScalar
mtrapinfoGauge = _MtrapinfoGauge_Object(
    (1, 3, 6, 1, 4, 1, 3808, 2, 2, 4),
    _MtrapinfoGauge_Type()
)
mtrapinfoGauge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtrapinfoGauge.setStatus("mandatory")
_MtrapinfoTimeTicks_Type = TimeTicks
_MtrapinfoTimeTicks_Object = MibScalar
mtrapinfoTimeTicks = _MtrapinfoTimeTicks_Object(
    (1, 3, 6, 1, 4, 1, 3808, 2, 2, 5),
    _MtrapinfoTimeTicks_Type()
)
mtrapinfoTimeTicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtrapinfoTimeTicks.setStatus("mandatory")
_MtrapinfoBmEventId_Type = Integer32
_MtrapinfoBmEventId_Object = MibScalar
mtrapinfoBmEventId = _MtrapinfoBmEventId_Object(
    (1, 3, 6, 1, 4, 1, 3808, 2, 2, 6),
    _MtrapinfoBmEventId_Type()
)
mtrapinfoBmEventId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtrapinfoBmEventId.setStatus("mandatory")
_Mcontrol_ObjectIdentity = ObjectIdentity
mcontrol = _Mcontrol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3808, 2, 3)
)


class _McontrolRestart_Type(Integer32):
    """Custom type mcontrolRestart based on Integer32"""
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
        *(("none", 1),
          ("restartCurrentSystem", 2),
          ("restartCurrentAgent", 3),
          ("restartCurrentSystemAndAgent", 4))
    )


_McontrolRestart_Type.__name__ = "Integer32"
_McontrolRestart_Object = MibScalar
mcontrolRestart = _McontrolRestart_Object(
    (1, 3, 6, 1, 4, 1, 3808, 2, 3, 1),
    _McontrolRestart_Type()
)
mcontrolRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcontrolRestart.setStatus("mandatory")


class _McontrolReset_Type(Integer32):
    """Custom type mcontrolReset based on Integer32"""
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
        *(("none", 1),
          ("resetCurrentSystem", 2),
          ("resetCurrentAgent", 3),
          ("resetCurrentSystemAndAgent", 4))
    )


_McontrolReset_Type.__name__ = "Integer32"
_McontrolReset_Object = MibScalar
mcontrolReset = _McontrolReset_Object(
    (1, 3, 6, 1, 4, 1, 3808, 2, 3, 2),
    _McontrolReset_Type()
)
mcontrolReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcontrolReset.setStatus("mandatory")

# Managed Objects groups


# Notification objects

communicationLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 1)
)
communicationLost.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    communicationLost.setStatus(
        ""
    )

upsOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 2)
)
upsOverload.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    upsOverload.setStatus(
        ""
    )

upsDiagnosticsFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 3)
)
upsDiagnosticsFailed.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    upsDiagnosticsFailed.setStatus(
        ""
    )

upsDischarged = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 4)
)
upsDischarged.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    upsDischarged.setStatus(
        ""
    )

upsOnBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 5)
)
upsOnBattery.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    upsOnBattery.setStatus(
        ""
    )

upsBoostOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 6)
)
upsBoostOn.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    upsBoostOn.setStatus(
        ""
    )

lowBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 7)
)
lowBattery.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    lowBattery.setStatus(
        ""
    )

communicationEstablished = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 8)
)
communicationEstablished.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    communicationEstablished.setStatus(
        ""
    )

powerRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 9)
)
powerRestored.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    powerRestored.setStatus(
        ""
    )

upsDiagnosticsPassed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 10)
)
upsDiagnosticsPassed.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    upsDiagnosticsPassed.setStatus(
        ""
    )

returnFromLowBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 11)
)
returnFromLowBattery.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    returnFromLowBattery.setStatus(
        ""
    )

upsTurnedOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 12)
)
upsTurnedOff.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    upsTurnedOff.setStatus(
        ""
    )

upsSleeping = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 13)
)
upsSleeping.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    upsSleeping.setStatus(
        ""
    )

upsWokeUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 14)
)
upsWokeUp.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    upsWokeUp.setStatus(
        ""
    )

upsRebootStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 15)
)
upsRebootStarted.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    upsRebootStarted.setStatus(
        ""
    )

upsOverTemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 16)
)
upsOverTemp.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    upsOverTemp.setStatus(
        ""
    )

returnFromOverTemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 17)
)
returnFromOverTemp.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    returnFromOverTemp.setStatus(
        ""
    )

upsBuckOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 18)
)
upsBuckOn.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    upsBuckOn.setStatus(
        ""
    )

returnFromOverLoad = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 19)
)
returnFromOverLoad.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    returnFromOverLoad.setStatus(
        ""
    )

returnFromDischarged = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 20)
)
returnFromDischarged.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    returnFromDischarged.setStatus(
        ""
    )

upsScheduleShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 21)
)
upsScheduleShutdown.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    upsScheduleShutdown.setStatus(
        ""
    )

upsEnterSleep = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 22)
)
upsEnterSleep.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    upsEnterSleep.setStatus(
        ""
    )

upsChargerFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 23)
)
upsChargerFailure.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    upsChargerFailure.setStatus(
        ""
    )

returnFromChargerFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 24)
)
returnFromChargerFailure.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    returnFromChargerFailure.setStatus(
        ""
    )

upsTurnoffStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 25)
)
upsTurnoffStarted.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    upsTurnoffStarted.setStatus(
        ""
    )

upsTurnedOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 26)
)
upsTurnedOn.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    upsTurnedOn.setStatus(
        ""
    )

upsRemoteCommandFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 27)
)
upsRemoteCommandFailed.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    upsRemoteCommandFailed.setStatus(
        ""
    )

upsLostRedundant = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 28)
)
upsLostRedundant.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    upsLostRedundant.setStatus(
        ""
    )

upsSignalClientShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 29)
)
upsSignalClientShutdown.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    upsSignalClientShutdown.setStatus(
        ""
    )

upsEmergencyPowerOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 30)
)
upsEmergencyPowerOff.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    upsEmergencyPowerOff.setStatus(
        ""
    )

nclBankOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 31)
)
nclBankOn.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    nclBankOn.setStatus(
        ""
    )

nclBankOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 32)
)
nclBankOff.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    nclBankOff.setStatus(
        ""
    )

upsCommandCancel = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 33)
)
upsCommandCancel.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    upsCommandCancel.setStatus(
        ""
    )

upsStartBatteryTest = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 34)
)
upsStartBatteryTest.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    upsStartBatteryTest.setStatus(
        ""
    )

upsRemainRuntimeLowThanThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 35)
)
upsRemainRuntimeLowThanThreshold.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    upsRemainRuntimeLowThanThreshold.setStatus(
        ""
    )

nclBankStartScheduleOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 36)
)
nclBankStartScheduleOff.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    nclBankStartScheduleOff.setStatus(
        ""
    )

upsEstimationAbort = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 37)
)
upsEstimationAbort.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    upsEstimationAbort.setStatus(
        ""
    )

upsHardwareFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 38)
)
upsHardwareFault.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    upsHardwareFault.setStatus(
        ""
    )

upsBatteryNotPresent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 39)
)
upsBatteryNotPresent.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    upsBatteryNotPresent.setStatus(
        ""
    )

upsWiringFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 40)
)
upsWiringFault.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    upsWiringFault.setStatus(
        ""
    )

upsWiringFaultCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 41)
)
upsWiringFaultCleared.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    upsWiringFaultCleared.setStatus(
        ""
    )

upsEnterBypassMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 42)
)
upsEnterBypassMode.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    upsEnterBypassMode.setStatus(
        ""
    )

upsReturnFromBypassMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 43)
)
upsReturnFromBypassMode.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    upsReturnFromBypassMode.setStatus(
        ""
    )

upsBypassOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 44)
)
upsBypassOverload.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    upsBypassOverload.setStatus(
        ""
    )

upsBypassOverloadCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 45)
)
upsBypassOverloadCleared.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    upsBypassOverloadCleared.setStatus(
        ""
    )

upsEnterECOMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 46)
)
upsEnterECOMode.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    upsEnterECOMode.setStatus(
        ""
    )

upsReturnFromECOMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 47)
)
upsReturnFromECOMode.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    upsReturnFromECOMode.setStatus(
        ""
    )

upsBatteryOverThreeYear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 48)
)
upsBatteryOverThreeYear.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    upsBatteryOverThreeYear.setStatus(
        ""
    )

upsBatteryExpiration = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 49)
)
upsBatteryExpiration.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    upsBatteryExpiration.setStatus(
        ""
    )

upsBatteryReplacement = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 50)
)
upsBatteryReplacement.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    upsBatteryReplacement.setStatus(
        ""
    )

upsModuleInvertorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 51)
)
upsModuleInvertorAlarm.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    upsModuleInvertorAlarm.setStatus(
        ""
    )

upsModuleRectifierAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 52)
)
upsModuleRectifierAlarm.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    upsModuleRectifierAlarm.setStatus(
        ""
    )

upsModuleFanAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 53)
)
upsModuleFanAlarm.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    upsModuleFanAlarm.setStatus(
        ""
    )

upsModuleManualShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 54)
)
upsModuleManualShutdown.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    upsModuleManualShutdown.setStatus(
        ""
    )

upsModuleOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 55)
)
upsModuleOverload.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    upsModuleOverload.setStatus(
        ""
    )

upsFirmwareUpgradeStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 56)
)
upsFirmwareUpgradeStart.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    upsFirmwareUpgradeStart.setStatus(
        ""
    )

upsFirmwareUpgradeEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 57)
)
upsFirmwareUpgradeEnd.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    upsFirmwareUpgradeEnd.setStatus(
        ""
    )

upsRFC1628TrapOnBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 58)
)
upsRFC1628TrapOnBattery.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    upsRFC1628TrapOnBattery.setStatus(
        ""
    )

upsRFC1628TrapTestCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 59)
)
upsRFC1628TrapTestCompleted.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    upsRFC1628TrapTestCompleted.setStatus(
        ""
    )

upsRFC1628TrapAlarmEntryAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 60)
)
upsRFC1628TrapAlarmEntryAdded.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    upsRFC1628TrapAlarmEntryAdded.setStatus(
        ""
    )

failAuthViaHTTP = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 61)
)
failAuthViaHTTP.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    failAuthViaHTTP.setStatus(
        ""
    )

passwordChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 62)
)
passwordChange.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    passwordChange.setStatus(
        ""
    )

failAuthViaConsole = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 63)
)
failAuthViaConsole.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    failAuthViaConsole.setStatus(
        ""
    )

configFileUpload = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 64)
)
configFileUpload.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    configFileUpload.setStatus(
        ""
    )

adminLoginInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 65)
)
adminLoginInfo.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    adminLoginInfo.setStatus(
        ""
    )

adminLogoutInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 66)
)
adminLogoutInfo.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    adminLogoutInfo.setStatus(
        ""
    )

deviceLoginInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 67)
)
deviceLoginInfo.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    deviceLoginInfo.setStatus(
        ""
    )

deviceLogoutInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 68)
)
deviceLogoutInfo.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    deviceLogoutInfo.setStatus(
        ""
    )

configurationChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 69)
)
configurationChanged.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    configurationChanged.setStatus(
        ""
    )

clientRegistered = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 70)
)
clientRegistered.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    clientRegistered.setStatus(
        ""
    )

clientRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 71)
)
clientRemoved.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    clientRemoved.setStatus(
        ""
    )

testEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 72)
)
testEvent.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    testEvent.setStatus(
        ""
    )

outletUserLoginInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 73)
)
outletUserLoginInfo.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    outletUserLoginInfo.setStatus(
        ""
    )

outletUserLogoutInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 74)
)
outletUserLogoutInfo.setObjects(
    ("CPS-MIB", "mtrapinfoString")
)
if mibBuilder.loadTexts:
    outletUserLogoutInfo.setStatus(
        ""
    )

ePDUCommunicationEstablished = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 100)
)
ePDUCommunicationEstablished.setObjects(
      *(("CPS-MIB", "ePDUIdentSerialNumber"),
        ("CPS-MIB", "ePDUIdentName"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    ePDUCommunicationEstablished.setStatus(
        ""
    )

ePDUCommunicationLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 101)
)
ePDUCommunicationLost.setObjects(
      *(("CPS-MIB", "ePDUIdentSerialNumber"),
        ("CPS-MIB", "ePDUIdentName"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    ePDUCommunicationLost.setStatus(
        ""
    )

ePDUOutletOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 102)
)
ePDUOutletOn.setObjects(
      *(("CPS-MIB", "ePDUIdentSerialNumber"),
        ("CPS-MIB", "ePDUIdentName"),
        ("CPS-MIB", "ePDUOutletControlIndex"),
        ("CPS-MIB", "ePDUOutletControlOutletName"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    ePDUOutletOn.setStatus(
        ""
    )

ePDUOutletOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 103)
)
ePDUOutletOff.setObjects(
      *(("CPS-MIB", "ePDUIdentSerialNumber"),
        ("CPS-MIB", "ePDUIdentName"),
        ("CPS-MIB", "ePDUOutletControlIndex"),
        ("CPS-MIB", "ePDUOutletControlOutletName"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    ePDUOutletOff.setStatus(
        ""
    )

ePDUDeviceConfigChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 104)
)
ePDUDeviceConfigChange.setObjects(
      *(("CPS-MIB", "ePDUIdentSerialNumber"),
        ("CPS-MIB", "ePDUIdentName"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    ePDUDeviceConfigChange.setStatus(
        ""
    )

ePDUOutletConfigChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 105)
)
ePDUOutletConfigChange.setObjects(
      *(("CPS-MIB", "ePDUIdentSerialNumber"),
        ("CPS-MIB", "ePDUIdentName"),
        ("CPS-MIB", "ePDUOutletControlIndex"),
        ("CPS-MIB", "ePDUOutletControlOutletName"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    ePDUOutletConfigChange.setStatus(
        ""
    )

ePDULowLoad = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 106)
)
ePDULowLoad.setObjects(
      *(("CPS-MIB", "ePDUIdentSerialNumber"),
        ("CPS-MIB", "ePDUIdentName"),
        ("CPS-MIB", "ePDULoadStatusPhaseNumber"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    ePDULowLoad.setStatus(
        ""
    )

ePDULowLoadCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 107)
)
ePDULowLoadCleared.setObjects(
      *(("CPS-MIB", "ePDUIdentSerialNumber"),
        ("CPS-MIB", "ePDUIdentName"),
        ("CPS-MIB", "ePDULoadStatusPhaseNumber"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    ePDULowLoadCleared.setStatus(
        ""
    )

ePDUNearOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 108)
)
ePDUNearOverload.setObjects(
      *(("CPS-MIB", "ePDUIdentSerialNumber"),
        ("CPS-MIB", "ePDUIdentName"),
        ("CPS-MIB", "ePDULoadStatusPhaseNumber"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    ePDUNearOverload.setStatus(
        ""
    )

ePDUNearOverloadCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 109)
)
ePDUNearOverloadCleared.setObjects(
      *(("CPS-MIB", "ePDUIdentSerialNumber"),
        ("CPS-MIB", "ePDUIdentName"),
        ("CPS-MIB", "ePDULoadStatusPhaseNumber"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    ePDUNearOverloadCleared.setStatus(
        ""
    )

ePDUOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 110)
)
ePDUOverload.setObjects(
      *(("CPS-MIB", "ePDUIdentSerialNumber"),
        ("CPS-MIB", "ePDUIdentName"),
        ("CPS-MIB", "ePDULoadStatusPhaseNumber"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    ePDUOverload.setStatus(
        ""
    )

ePDUOverloadCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 111)
)
ePDUOverloadCleared.setObjects(
      *(("CPS-MIB", "ePDUIdentSerialNumber"),
        ("CPS-MIB", "ePDUIdentName"),
        ("CPS-MIB", "ePDULoadStatusPhaseNumber"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    ePDUOverloadCleared.setStatus(
        ""
    )

ePDUDelayOutletOnCommand = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 112)
)
ePDUDelayOutletOnCommand.setObjects(
      *(("CPS-MIB", "ePDUIdentSerialNumber"),
        ("CPS-MIB", "ePDUIdentName"),
        ("CPS-MIB", "ePDUOutletControlIndex"),
        ("CPS-MIB", "ePDUOutletControlOutletName"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    ePDUDelayOutletOnCommand.setStatus(
        ""
    )

ePDUDelayOutletOffCommand = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 113)
)
ePDUDelayOutletOffCommand.setObjects(
      *(("CPS-MIB", "ePDUIdentSerialNumber"),
        ("CPS-MIB", "ePDUIdentName"),
        ("CPS-MIB", "ePDUOutletControlIndex"),
        ("CPS-MIB", "ePDUOutletControlOutletName"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    ePDUDelayOutletOffCommand.setStatus(
        ""
    )

ePDUDelayOutletRebootCommand = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 114)
)
ePDUDelayOutletRebootCommand.setObjects(
      *(("CPS-MIB", "ePDUIdentSerialNumber"),
        ("CPS-MIB", "ePDUIdentName"),
        ("CPS-MIB", "ePDUOutletControlIndex"),
        ("CPS-MIB", "ePDUOutletControlOutletName"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    ePDUDelayOutletRebootCommand.setStatus(
        ""
    )

ePDUCancelPendingCommand = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 115)
)
ePDUCancelPendingCommand.setObjects(
      *(("CPS-MIB", "ePDUIdentSerialNumber"),
        ("CPS-MIB", "ePDUIdentName"),
        ("CPS-MIB", "ePDUOutletControlIndex"),
        ("CPS-MIB", "ePDUOutletControlOutletName"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    ePDUCancelPendingCommand.setStatus(
        ""
    )

ePDULineUndervoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 116)
)
ePDULineUndervoltage.setObjects(
      *(("CPS-MIB", "ePDUIdentSerialNumber"),
        ("CPS-MIB", "ePDUIdentName"),
        ("CPS-MIB", "ePDULoadStatusPhaseNumber"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    ePDULineUndervoltage.setStatus(
        ""
    )

ePDULineUndervoltageCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 117)
)
ePDULineUndervoltageCleared.setObjects(
      *(("CPS-MIB", "ePDUIdentSerialNumber"),
        ("CPS-MIB", "ePDUIdentName"),
        ("CPS-MIB", "ePDULoadStatusPhaseNumber"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    ePDULineUndervoltageCleared.setStatus(
        ""
    )

ePDULineOvervoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 118)
)
ePDULineOvervoltage.setObjects(
      *(("CPS-MIB", "ePDUIdentSerialNumber"),
        ("CPS-MIB", "ePDUIdentName"),
        ("CPS-MIB", "ePDULoadStatusPhaseNumber"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    ePDULineOvervoltage.setStatus(
        ""
    )

ePDULineOvervoltageCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 119)
)
ePDULineOvervoltageCleared.setObjects(
      *(("CPS-MIB", "ePDUIdentSerialNumber"),
        ("CPS-MIB", "ePDUIdentName"),
        ("CPS-MIB", "ePDULoadStatusPhaseNumber"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    ePDULineOvervoltageCleared.setStatus(
        ""
    )

ePDUPowerSupply1Fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 120)
)
ePDUPowerSupply1Fail.setObjects(
      *(("CPS-MIB", "ePDUIdentSerialNumber"),
        ("CPS-MIB", "ePDUIdentName"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    ePDUPowerSupply1Fail.setStatus(
        ""
    )

ePDUPowerSupply1Ok = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 121)
)
ePDUPowerSupply1Ok.setObjects(
      *(("CPS-MIB", "ePDUIdentSerialNumber"),
        ("CPS-MIB", "ePDUIdentName"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    ePDUPowerSupply1Ok.setStatus(
        ""
    )

ePDUPowerSupply2Fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 122)
)
ePDUPowerSupply2Fail.setObjects(
      *(("CPS-MIB", "ePDUIdentSerialNumber"),
        ("CPS-MIB", "ePDUIdentName"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    ePDUPowerSupply2Fail.setStatus(
        ""
    )

ePDUPowerSupply2Ok = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 123)
)
ePDUPowerSupply2Ok.setObjects(
      *(("CPS-MIB", "ePDUIdentSerialNumber"),
        ("CPS-MIB", "ePDUIdentName"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    ePDUPowerSupply2Ok.setStatus(
        ""
    )

ePDUBankLowLoad = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 124)
)
ePDUBankLowLoad.setObjects(
      *(("CPS-MIB", "ePDUIdentSerialNumber"),
        ("CPS-MIB", "ePDUIdentName"),
        ("CPS-MIB", "ePDULoadStatusBankNumber"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    ePDUBankLowLoad.setStatus(
        ""
    )

ePDUBankLowLoadCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 125)
)
ePDUBankLowLoadCleared.setObjects(
      *(("CPS-MIB", "ePDUIdentSerialNumber"),
        ("CPS-MIB", "ePDUIdentName"),
        ("CPS-MIB", "ePDULoadStatusBankNumber"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    ePDUBankLowLoadCleared.setStatus(
        ""
    )

ePDUBankNearOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 126)
)
ePDUBankNearOverload.setObjects(
      *(("CPS-MIB", "ePDUIdentSerialNumber"),
        ("CPS-MIB", "ePDUIdentName"),
        ("CPS-MIB", "ePDULoadStatusBankNumber"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    ePDUBankNearOverload.setStatus(
        ""
    )

ePDUBankNearOverloadCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 127)
)
ePDUBankNearOverloadCleared.setObjects(
      *(("CPS-MIB", "ePDUIdentSerialNumber"),
        ("CPS-MIB", "ePDUIdentName"),
        ("CPS-MIB", "ePDULoadStatusBankNumber"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    ePDUBankNearOverloadCleared.setStatus(
        ""
    )

ePDUBankOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 128)
)
ePDUBankOverload.setObjects(
      *(("CPS-MIB", "ePDUIdentSerialNumber"),
        ("CPS-MIB", "ePDUIdentName"),
        ("CPS-MIB", "ePDULoadStatusBankNumber"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    ePDUBankOverload.setStatus(
        ""
    )

ePDUBankOverloadCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 129)
)
ePDUBankOverloadCleared.setObjects(
      *(("CPS-MIB", "ePDUIdentSerialNumber"),
        ("CPS-MIB", "ePDUIdentName"),
        ("CPS-MIB", "ePDULoadStatusBankNumber"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    ePDUBankOverloadCleared.setStatus(
        ""
    )

ePDUComponentCommunicationEstablished = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 130)
)
ePDUComponentCommunicationEstablished.setObjects(
      *(("CPS-MIB", "ePDUIdentSerialNumber"),
        ("CPS-MIB", "ePDUIdentName"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    ePDUComponentCommunicationEstablished.setStatus(
        ""
    )

ePDUComponentCommunicationLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 131)
)
ePDUComponentCommunicationLost.setObjects(
      *(("CPS-MIB", "ePDUIdentSerialNumber"),
        ("CPS-MIB", "ePDUIdentName"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    ePDUComponentCommunicationLost.setStatus(
        ""
    )

ePDUOutletLowLoad = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 132)
)
ePDUOutletLowLoad.setObjects(
      *(("CPS-MIB", "ePDUIdentSerialNumber"),
        ("CPS-MIB", "ePDUIdentName"),
        ("CPS-MIB", "ePDUOutletConfigMonitoredNumber"),
        ("CPS-MIB", "ePDUOutletConfigMonitoredName"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    ePDUOutletLowLoad.setStatus(
        ""
    )

ePDUOutletLowLoadCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 133)
)
ePDUOutletLowLoadCleared.setObjects(
      *(("CPS-MIB", "ePDUIdentSerialNumber"),
        ("CPS-MIB", "ePDUIdentName"),
        ("CPS-MIB", "ePDUOutletConfigMonitoredNumber"),
        ("CPS-MIB", "ePDUOutletConfigMonitoredName"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    ePDUOutletLowLoadCleared.setStatus(
        ""
    )

ePDUOutletNearOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 134)
)
ePDUOutletNearOverload.setObjects(
      *(("CPS-MIB", "ePDUIdentSerialNumber"),
        ("CPS-MIB", "ePDUIdentName"),
        ("CPS-MIB", "ePDUOutletConfigMonitoredNumber"),
        ("CPS-MIB", "ePDUOutletConfigMonitoredName"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    ePDUOutletNearOverload.setStatus(
        ""
    )

ePDUOutletNearOverloadCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 135)
)
ePDUOutletNearOverloadCleared.setObjects(
      *(("CPS-MIB", "ePDUIdentSerialNumber"),
        ("CPS-MIB", "ePDUIdentName"),
        ("CPS-MIB", "ePDUOutletConfigMonitoredNumber"),
        ("CPS-MIB", "ePDUOutletConfigMonitoredName"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    ePDUOutletNearOverloadCleared.setStatus(
        ""
    )

ePDUOutletOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 136)
)
ePDUOutletOverload.setObjects(
      *(("CPS-MIB", "ePDUIdentSerialNumber"),
        ("CPS-MIB", "ePDUIdentName"),
        ("CPS-MIB", "ePDUOutletConfigMonitoredNumber"),
        ("CPS-MIB", "ePDUOutletConfigMonitoredName"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    ePDUOutletOverload.setStatus(
        ""
    )

ePDUOutletOverloadCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 137)
)
ePDUOutletOverloadCleared.setObjects(
      *(("CPS-MIB", "ePDUIdentSerialNumber"),
        ("CPS-MIB", "ePDUIdentName"),
        ("CPS-MIB", "ePDUOutletConfigMonitoredNumber"),
        ("CPS-MIB", "ePDUOutletConfigMonitoredName"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    ePDUOutletOverloadCleared.setStatus(
        ""
    )

envHighTemperatureViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 200)
)
envHighTemperatureViolation.setObjects(
      *(("CPS-MIB", "envirIdentName"),
        ("CPS-MIB", "envirIdentLocation"),
        ("CPS-MIB", "envirTemperature"))
)
if mibBuilder.loadTexts:
    envHighTemperatureViolation.setStatus(
        ""
    )

envHighTemperatureBack = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 201)
)
envHighTemperatureBack.setObjects(
      *(("CPS-MIB", "envirIdentName"),
        ("CPS-MIB", "envirIdentLocation"),
        ("CPS-MIB", "envirTemperature"))
)
if mibBuilder.loadTexts:
    envHighTemperatureBack.setStatus(
        ""
    )

envLowTemperatureViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 202)
)
envLowTemperatureViolation.setObjects(
      *(("CPS-MIB", "envirIdentName"),
        ("CPS-MIB", "envirIdentLocation"),
        ("CPS-MIB", "envirTemperature"))
)
if mibBuilder.loadTexts:
    envLowTemperatureViolation.setStatus(
        ""
    )

envLowTempBack = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 203)
)
envLowTempBack.setObjects(
      *(("CPS-MIB", "envirIdentName"),
        ("CPS-MIB", "envirIdentLocation"),
        ("CPS-MIB", "envirTemperature"))
)
if mibBuilder.loadTexts:
    envLowTempBack.setStatus(
        ""
    )

envHighHumidityViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 204)
)
envHighHumidityViolation.setObjects(
      *(("CPS-MIB", "envirIdentName"),
        ("CPS-MIB", "envirIdentLocation"),
        ("CPS-MIB", "envirHumidity"))
)
if mibBuilder.loadTexts:
    envHighHumidityViolation.setStatus(
        ""
    )

envHighHumidityBack = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 205)
)
envHighHumidityBack.setObjects(
      *(("CPS-MIB", "envirIdentName"),
        ("CPS-MIB", "envirIdentLocation"),
        ("CPS-MIB", "envirHumidity"))
)
if mibBuilder.loadTexts:
    envHighHumidityBack.setStatus(
        ""
    )

envLowHumidityViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 206)
)
envLowHumidityViolation.setObjects(
      *(("CPS-MIB", "envirIdentName"),
        ("CPS-MIB", "envirIdentLocation"),
        ("CPS-MIB", "envirHumidity"))
)
if mibBuilder.loadTexts:
    envLowHumidityViolation.setStatus(
        ""
    )

envLowHumdBack = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 207)
)
envLowHumdBack.setObjects(
      *(("CPS-MIB", "envirIdentName"),
        ("CPS-MIB", "envirIdentLocation"),
        ("CPS-MIB", "envirHumidity"))
)
if mibBuilder.loadTexts:
    envLowHumdBack.setStatus(
        ""
    )

envDryContactAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 208)
)
envDryContactAbnormal.setObjects(
      *(("CPS-MIB", "envirIdentName"),
        ("CPS-MIB", "envirIdentLocation"),
        ("CPS-MIB", "envirContactIndex"),
        ("CPS-MIB", "envirContactName"))
)
if mibBuilder.loadTexts:
    envDryContactAbnormal.setStatus(
        ""
    )

envDryContactNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 209)
)
envDryContactNormal.setObjects(
      *(("CPS-MIB", "envirIdentName"),
        ("CPS-MIB", "envirIdentLocation"),
        ("CPS-MIB", "envirContactIndex"),
        ("CPS-MIB", "envirContactName"))
)
if mibBuilder.loadTexts:
    envDryContactNormal.setStatus(
        ""
    )

envConntected = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 210)
)
envConntected.setObjects(
      *(("CPS-MIB", "envirIdentName"),
        ("CPS-MIB", "envirIdentLocation"))
)
if mibBuilder.loadTexts:
    envConntected.setStatus(
        ""
    )

envDisconntected = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 211)
)
envDisconntected.setObjects(
      *(("CPS-MIB", "envirIdentName"),
        ("CPS-MIB", "envirIdentLocation"))
)
if mibBuilder.loadTexts:
    envDisconntected.setStatus(
        ""
    )

envRateOfTemperatureChangeAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 212)
)
envRateOfTemperatureChangeAbnormal.setObjects(
      *(("CPS-MIB", "envirIdentName"),
        ("CPS-MIB", "envirIdentLocation"),
        ("CPS-MIB", "envirTemperature"))
)
if mibBuilder.loadTexts:
    envRateOfTemperatureChangeAbnormal.setStatus(
        ""
    )

envRateOfHumdChangeAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 213)
)
envRateOfHumdChangeAbnormal.setObjects(
      *(("CPS-MIB", "envirIdentName"),
        ("CPS-MIB", "envirIdentLocation"),
        ("CPS-MIB", "envirHumidity"))
)
if mibBuilder.loadTexts:
    envRateOfHumdChangeAbnormal.setStatus(
        ""
    )

atsSwitchSource = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 301)
)
atsSwitchSource.setObjects(
      *(("CPS-MIB", "atsIdentName"),
        ("CPS-MIB", "atsIdentSerialNumber"),
        ("CPS-MIB", "atsStatusSelectedSource"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    atsSwitchSource.setStatus(
        ""
    )

atsSourceFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 302)
)
atsSourceFault.setObjects(
      *(("CPS-MIB", "atsIdentName"),
        ("CPS-MIB", "atsIdentSerialNumber"),
        ("CPS-MIB", "atsStatusInputName"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    atsSourceFault.setStatus(
        ""
    )

atsSourceFaultCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 303)
)
atsSourceFaultCleared.setObjects(
      *(("CPS-MIB", "atsIdentName"),
        ("CPS-MIB", "atsIdentSerialNumber"),
        ("CPS-MIB", "atsStatusInputName"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    atsSourceFaultCleared.setStatus(
        ""
    )

atsRedundancyFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 304)
)
atsRedundancyFail.setObjects(
      *(("CPS-MIB", "atsIdentName"),
        ("CPS-MIB", "atsIdentSerialNumber"),
        ("CPS-MIB", "atsStatusInputName"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    atsRedundancyFail.setStatus(
        ""
    )

atsRedundancyRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 305)
)
atsRedundancyRestored.setObjects(
      *(("CPS-MIB", "atsIdentName"),
        ("CPS-MIB", "atsIdentSerialNumber"),
        ("CPS-MIB", "atsStatusInputName"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    atsRedundancyRestored.setStatus(
        ""
    )

atsInputHighVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 306)
)
atsInputHighVoltage.setObjects(
      *(("CPS-MIB", "atsIdentName"),
        ("CPS-MIB", "atsIdentSerialNumber"),
        ("CPS-MIB", "atsStatusInputName"),
        ("CPS-MIB", "atsStatusInputVoltage"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    atsInputHighVoltage.setStatus(
        ""
    )

atsInputHighVoltageCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 307)
)
atsInputHighVoltageCleared.setObjects(
      *(("CPS-MIB", "atsIdentName"),
        ("CPS-MIB", "atsIdentSerialNumber"),
        ("CPS-MIB", "atsStatusInputName"),
        ("CPS-MIB", "atsStatusInputVoltage"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    atsInputHighVoltageCleared.setStatus(
        ""
    )

atsInputLowVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 308)
)
atsInputLowVoltage.setObjects(
      *(("CPS-MIB", "atsIdentName"),
        ("CPS-MIB", "atsIdentSerialNumber"),
        ("CPS-MIB", "atsStatusInputName"),
        ("CPS-MIB", "atsStatusInputVoltage"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    atsInputLowVoltage.setStatus(
        ""
    )

atsInputLowVoltageCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 309)
)
atsInputLowVoltageCleared.setObjects(
      *(("CPS-MIB", "atsIdentName"),
        ("CPS-MIB", "atsIdentSerialNumber"),
        ("CPS-MIB", "atsStatusInputName"),
        ("CPS-MIB", "atsStatusInputVoltage"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    atsInputLowVoltageCleared.setStatus(
        ""
    )

atsInputHighFrequency = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 310)
)
atsInputHighFrequency.setObjects(
      *(("CPS-MIB", "atsIdentName"),
        ("CPS-MIB", "atsIdentSerialNumber"),
        ("CPS-MIB", "atsStatusInputName"),
        ("CPS-MIB", "atsStatusInputFrequency"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    atsInputHighFrequency.setStatus(
        ""
    )

atsInputHighFrequencyCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 311)
)
atsInputHighFrequencyCleared.setObjects(
      *(("CPS-MIB", "atsIdentName"),
        ("CPS-MIB", "atsIdentSerialNumber"),
        ("CPS-MIB", "atsStatusInputName"),
        ("CPS-MIB", "atsStatusInputFrequency"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    atsInputHighFrequencyCleared.setStatus(
        ""
    )

atsInputLowFrequency = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 312)
)
atsInputLowFrequency.setObjects(
      *(("CPS-MIB", "atsIdentName"),
        ("CPS-MIB", "atsIdentSerialNumber"),
        ("CPS-MIB", "atsStatusInputName"),
        ("CPS-MIB", "atsStatusInputFrequency"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    atsInputLowFrequency.setStatus(
        ""
    )

atsInputLowFrequencyCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 313)
)
atsInputLowFrequencyCleared.setObjects(
      *(("CPS-MIB", "atsIdentName"),
        ("CPS-MIB", "atsIdentSerialNumber"),
        ("CPS-MIB", "atsStatusInputName"),
        ("CPS-MIB", "atsStatusInputFrequency"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    atsInputLowFrequencyCleared.setStatus(
        ""
    )

atsCommunicationLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 314)
)
atsCommunicationLost.setObjects(
      *(("CPS-MIB", "atsIdentName"),
        ("CPS-MIB", "atsIdentSerialNumber"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    atsCommunicationLost.setStatus(
        ""
    )

atsCommunicationEstablished = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 315)
)
atsCommunicationEstablished.setObjects(
      *(("CPS-MIB", "atsIdentName"),
        ("CPS-MIB", "atsIdentSerialNumber"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    atsCommunicationEstablished.setStatus(
        ""
    )

atsLCDCommunicationLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 316)
)
atsLCDCommunicationLost.setObjects(
      *(("CPS-MIB", "atsIdentName"),
        ("CPS-MIB", "atsIdentSerialNumber"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    atsLCDCommunicationLost.setStatus(
        ""
    )

atsLCDCommunicationLostCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 317)
)
atsLCDCommunicationLostCleared.setObjects(
      *(("CPS-MIB", "atsIdentName"),
        ("CPS-MIB", "atsIdentSerialNumber"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    atsLCDCommunicationLostCleared.setStatus(
        ""
    )

atsDB9CommunicationLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 318)
)
atsDB9CommunicationLost.setObjects(
      *(("CPS-MIB", "atsIdentName"),
        ("CPS-MIB", "atsIdentSerialNumber"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    atsDB9CommunicationLost.setStatus(
        ""
    )

atsDB9CommunicationLostCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 319)
)
atsDB9CommunicationLostCleared.setObjects(
      *(("CPS-MIB", "atsIdentName"),
        ("CPS-MIB", "atsIdentSerialNumber"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    atsDB9CommunicationLostCleared.setStatus(
        ""
    )

atsPowerSupplyFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 320)
)
atsPowerSupplyFault.setObjects(
      *(("CPS-MIB", "atsIdentName"),
        ("CPS-MIB", "atsIdentSerialNumber"),
        ("CPS-MIB", "atsStatusPowerSupplyInputSource"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    atsPowerSupplyFault.setStatus(
        ""
    )

atsPowerSupplyFaultCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 321)
)
atsPowerSupplyFaultCleared.setObjects(
      *(("CPS-MIB", "atsIdentName"),
        ("CPS-MIB", "atsIdentSerialNumber"),
        ("CPS-MIB", "atsStatusPowerSupplyInputSource"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    atsPowerSupplyFaultCleared.setStatus(
        ""
    )

atsDevHardwareFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 322)
)
atsDevHardwareFault.setObjects(
      *(("CPS-MIB", "atsIdentName"),
        ("CPS-MIB", "atsIdentSerialNumber"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    atsDevHardwareFault.setStatus(
        ""
    )

atsDevHardwareFaultCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 323)
)
atsDevHardwareFaultCleared.setObjects(
      *(("CPS-MIB", "atsIdentName"),
        ("CPS-MIB", "atsIdentSerialNumber"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    atsDevHardwareFaultCleared.setStatus(
        ""
    )

atsSourceConfigChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 324)
)
atsSourceConfigChanged.setObjects(
      *(("CPS-MIB", "atsIdentName"),
        ("CPS-MIB", "atsIdentSerialNumber"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    atsSourceConfigChanged.setStatus(
        ""
    )

atsDeviceConfigChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 325)
)
atsDeviceConfigChanged.setObjects(
      *(("CPS-MIB", "atsIdentName"),
        ("CPS-MIB", "atsIdentSerialNumber"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    atsDeviceConfigChanged.setStatus(
        ""
    )

atsOutletConfigChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 326)
)
atsOutletConfigChanged.setObjects(
      *(("CPS-MIB", "atsIdentName"),
        ("CPS-MIB", "atsIdentSerialNumber"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    atsOutletConfigChanged.setStatus(
        ""
    )

atsEventCountsCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 327)
)
atsEventCountsCleared.setObjects(
      *(("CPS-MIB", "atsIdentName"),
        ("CPS-MIB", "atsIdentSerialNumber"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    atsEventCountsCleared.setStatus(
        ""
    )

atsOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 328)
)
atsOverload.setObjects(
      *(("CPS-MIB", "atsIdentName"),
        ("CPS-MIB", "atsIdentSerialNumber"),
        ("CPS-MIB", "atsLoadStatusBankTableIndex"),
        ("CPS-MIB", "atsLoadStatusBankLoad"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    atsOverload.setStatus(
        ""
    )

atsOverloadCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 329)
)
atsOverloadCleared.setObjects(
      *(("CPS-MIB", "atsIdentName"),
        ("CPS-MIB", "atsIdentSerialNumber"),
        ("CPS-MIB", "atsLoadStatusBankTableIndex"),
        ("CPS-MIB", "atsLoadStatusBankLoad"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    atsOverloadCleared.setStatus(
        ""
    )

atsNearOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 330)
)
atsNearOverload.setObjects(
      *(("CPS-MIB", "atsIdentName"),
        ("CPS-MIB", "atsIdentSerialNumber"),
        ("CPS-MIB", "atsLoadStatusBankTableIndex"),
        ("CPS-MIB", "atsLoadStatusBankLoad"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    atsNearOverload.setStatus(
        ""
    )

atsNearOverloadCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 331)
)
atsNearOverloadCleared.setObjects(
      *(("CPS-MIB", "atsIdentName"),
        ("CPS-MIB", "atsIdentSerialNumber"),
        ("CPS-MIB", "atsLoadStatusBankTableIndex"),
        ("CPS-MIB", "atsLoadStatusBankLoad"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    atsNearOverloadCleared.setStatus(
        ""
    )

atsLowLoad = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 332)
)
atsLowLoad.setObjects(
      *(("CPS-MIB", "atsIdentName"),
        ("CPS-MIB", "atsIdentSerialNumber"),
        ("CPS-MIB", "atsLoadStatusBankTableIndex"),
        ("CPS-MIB", "atsLoadStatusBankLoad"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    atsLowLoad.setStatus(
        ""
    )

atsLowLoadCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 333)
)
atsLowLoadCleared.setObjects(
      *(("CPS-MIB", "atsIdentName"),
        ("CPS-MIB", "atsIdentSerialNumber"),
        ("CPS-MIB", "atsLoadStatusBankTableIndex"),
        ("CPS-MIB", "atsLoadStatusBankLoad"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    atsLowLoadCleared.setStatus(
        ""
    )

atsOutletOnCommand = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 334)
)
atsOutletOnCommand.setObjects(
      *(("CPS-MIB", "atsIdentName"),
        ("CPS-MIB", "atsIdentSerialNumber"),
        ("CPS-MIB", "atsOutletCtrlTableIndex"),
        ("CPS-MIB", "atsOutletCtrlOutletName"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    atsOutletOnCommand.setStatus(
        ""
    )

atsOutletOffCommand = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 335)
)
atsOutletOffCommand.setObjects(
      *(("CPS-MIB", "atsIdentName"),
        ("CPS-MIB", "atsIdentSerialNumber"),
        ("CPS-MIB", "atsOutletCtrlTableIndex"),
        ("CPS-MIB", "atsOutletCtrlOutletName"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    atsOutletOffCommand.setStatus(
        ""
    )

atsOutletRebootCommand = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 336)
)
atsOutletRebootCommand.setObjects(
      *(("CPS-MIB", "atsIdentName"),
        ("CPS-MIB", "atsIdentSerialNumber"),
        ("CPS-MIB", "atsOutletCtrlTableIndex"),
        ("CPS-MIB", "atsOutletCtrlOutletName"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    atsOutletRebootCommand.setStatus(
        ""
    )

atsCancelPendingCommand = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 337)
)
atsCancelPendingCommand.setObjects(
      *(("CPS-MIB", "atsIdentName"),
        ("CPS-MIB", "atsIdentSerialNumber"),
        ("CPS-MIB", "atsOutletCtrlTableIndex"),
        ("CPS-MIB", "atsOutletCtrlOutletName"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    atsCancelPendingCommand.setStatus(
        ""
    )

atsOutletOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 338)
)
atsOutletOn.setObjects(
      *(("CPS-MIB", "atsIdentName"),
        ("CPS-MIB", "atsIdentSerialNumber"),
        ("CPS-MIB", "atsOutletCtrlTableIndex"),
        ("CPS-MIB", "atsOutletCtrlOutletName"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    atsOutletOn.setStatus(
        ""
    )

atsOutletOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 339)
)
atsOutletOff.setObjects(
      *(("CPS-MIB", "atsIdentName"),
        ("CPS-MIB", "atsIdentSerialNumber"),
        ("CPS-MIB", "atsOutletCtrlTableIndex"),
        ("CPS-MIB", "atsOutletCtrlOutletName"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    atsOutletOff.setStatus(
        ""
    )

pduDeviceEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 400)
)
pduDeviceEvent.setObjects(
      *(("CPS-MIB", "ePDU2IdentSerialNumber"),
        ("CPS-MIB", "ePDU2IdentName"),
        ("CPS-MIB", "ePDU2DeviceConfigIndex"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    pduDeviceEvent.setStatus(
        ""
    )

pduDeviceAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 401)
)
pduDeviceAlarm.setObjects(
      *(("CPS-MIB", "ePDU2IdentSerialNumber"),
        ("CPS-MIB", "ePDU2IdentName"),
        ("CPS-MIB", "ePDU2DeviceStatusIndex"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    pduDeviceAlarm.setStatus(
        ""
    )

pduDeviceAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 402)
)
pduDeviceAlarmClear.setObjects(
      *(("CPS-MIB", "ePDU2IdentSerialNumber"),
        ("CPS-MIB", "ePDU2IdentName"),
        ("CPS-MIB", "ePDU2DeviceStatusIndex"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    pduDeviceAlarmClear.setStatus(
        ""
    )

pduPhaseEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 403)
)
pduPhaseEvent.setObjects(
      *(("CPS-MIB", "ePDU2IdentSerialNumber"),
        ("CPS-MIB", "ePDU2IdentName"),
        ("CPS-MIB", "ePDU2PhaseConfigIndex"),
        ("CPS-MIB", "ePDU2PhaseConfigNumber"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    pduPhaseEvent.setStatus(
        ""
    )

pduPhaseAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 404)
)
pduPhaseAlarm.setObjects(
      *(("CPS-MIB", "ePDU2IdentSerialNumber"),
        ("CPS-MIB", "ePDU2IdentName"),
        ("CPS-MIB", "ePDU2PhaseStatusIndex"),
        ("CPS-MIB", "ePDU2PhaseStatusNumber"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    pduPhaseAlarm.setStatus(
        ""
    )

pduPhaseAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 405)
)
pduPhaseAlarmClear.setObjects(
      *(("CPS-MIB", "ePDU2IdentSerialNumber"),
        ("CPS-MIB", "ePDU2IdentName"),
        ("CPS-MIB", "ePDU2PhaseStatusIndex"),
        ("CPS-MIB", "ePDU2PhaseStatusNumber"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    pduPhaseAlarmClear.setStatus(
        ""
    )

pduBankEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 406)
)
pduBankEvent.setObjects(
      *(("CPS-MIB", "ePDU2IdentSerialNumber"),
        ("CPS-MIB", "ePDU2IdentName"),
        ("CPS-MIB", "ePDU2BankConfigIndex"),
        ("CPS-MIB", "ePDU2BankConfigNumber"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    pduBankEvent.setStatus(
        ""
    )

pduBankAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 407)
)
pduBankAlarm.setObjects(
      *(("CPS-MIB", "ePDU2IdentSerialNumber"),
        ("CPS-MIB", "ePDU2IdentName"),
        ("CPS-MIB", "ePDU2BankStatusIndex"),
        ("CPS-MIB", "ePDU2BankStatusNumber"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    pduBankAlarm.setStatus(
        ""
    )

pduBankAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 408)
)
pduBankAlarmClear.setObjects(
      *(("CPS-MIB", "ePDU2IdentSerialNumber"),
        ("CPS-MIB", "ePDU2IdentName"),
        ("CPS-MIB", "ePDU2BankStatusIndex"),
        ("CPS-MIB", "ePDU2BankStatusNumber"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    pduBankAlarmClear.setStatus(
        ""
    )

pduOutletSwitchedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 409)
)
pduOutletSwitchedEvent.setObjects(
      *(("CPS-MIB", "ePDU2IdentSerialNumber"),
        ("CPS-MIB", "ePDU2IdentName"),
        ("CPS-MIB", "ePDU2OutletSwitchedControlIndex"),
        ("CPS-MIB", "ePDU2OutletSwitchedControlNumber"),
        ("CPS-MIB", "ePDU2OutletSwitchedControlName"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    pduOutletSwitchedEvent.setStatus(
        ""
    )

pduOutletSwitchedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 410)
)
pduOutletSwitchedAlarm.setObjects(
      *(("CPS-MIB", "ePDU2IdentSerialNumber"),
        ("CPS-MIB", "ePDU2IdentName"),
        ("CPS-MIB", "ePDU2OutletSwitchedStatusIndex"),
        ("CPS-MIB", "ePDU2OutletSwitchedStatusNumber"),
        ("CPS-MIB", "ePDU2OutletSwitchedStatusName"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    pduOutletSwitchedAlarm.setStatus(
        ""
    )

pduOutletSwitchedAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 411)
)
pduOutletSwitchedAlarmClear.setObjects(
      *(("CPS-MIB", "ePDU2IdentSerialNumber"),
        ("CPS-MIB", "ePDU2IdentName"),
        ("CPS-MIB", "ePDU2OutletSwitchedStatusIndex"),
        ("CPS-MIB", "ePDU2OutletSwitchedStatusNumber"),
        ("CPS-MIB", "ePDU2OutletSwitchedStatusName"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    pduOutletSwitchedAlarmClear.setStatus(
        ""
    )

pduOutletMeteredEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 412)
)
pduOutletMeteredEvent.setObjects(
      *(("CPS-MIB", "ePDU2IdentSerialNumber"),
        ("CPS-MIB", "ePDU2IdentName"),
        ("CPS-MIB", "ePDU2OutletMeteredConfigIndex"),
        ("CPS-MIB", "ePDU2OutletMeteredConfigNumber"),
        ("CPS-MIB", "ePDU2OutletMeteredConfigName"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    pduOutletMeteredEvent.setStatus(
        ""
    )

pduOutletMeteredAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 413)
)
pduOutletMeteredAlarm.setObjects(
      *(("CPS-MIB", "ePDU2IdentSerialNumber"),
        ("CPS-MIB", "ePDU2IdentName"),
        ("CPS-MIB", "ePDU2OutletMeteredStatusIndex"),
        ("CPS-MIB", "ePDU2OutletMeteredStatusNumber"),
        ("CPS-MIB", "ePDU2OutletMeteredStatusName"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    pduOutletMeteredAlarm.setStatus(
        ""
    )

pduOutletMeteredAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 414)
)
pduOutletMeteredAlarmClear.setObjects(
      *(("CPS-MIB", "ePDU2IdentSerialNumber"),
        ("CPS-MIB", "ePDU2IdentName"),
        ("CPS-MIB", "ePDU2OutletMeteredStatusIndex"),
        ("CPS-MIB", "ePDU2OutletMeteredStatusNumber"),
        ("CPS-MIB", "ePDU2OutletMeteredStatusName"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    pduOutletMeteredAlarmClear.setStatus(
        ""
    )

pduDaisyChainEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 415)
)
pduDaisyChainEvent.setObjects(
      *(("CPS-MIB", "ePDU2IdentSerialNumber"),
        ("CPS-MIB", "ePDU2IdentName"),
        ("CPS-MIB", "ePDU2IdentIndex"),
        ("CPS-MIB", "ePDU2IdentSerialNumber"),
        ("CPS-MIB", "ePDU2IdentName"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    pduDaisyChainEvent.setStatus(
        ""
    )

pduDaisyChainAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 416)
)
pduDaisyChainAlarm.setObjects(
      *(("CPS-MIB", "ePDU2IdentSerialNumber"),
        ("CPS-MIB", "ePDU2IdentName"),
        ("CPS-MIB", "ePDU2IdentIndex"),
        ("CPS-MIB", "ePDU2IdentSerialNumber"),
        ("CPS-MIB", "ePDU2IdentName"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    pduDaisyChainAlarm.setStatus(
        ""
    )

pduDaisyChainAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 417)
)
pduDaisyChainAlarmClear.setObjects(
      *(("CPS-MIB", "ePDU2IdentSerialNumber"),
        ("CPS-MIB", "ePDU2IdentName"),
        ("CPS-MIB", "ePDU2IdentIndex"),
        ("CPS-MIB", "ePDU2IdentSerialNumber"),
        ("CPS-MIB", "ePDU2IdentName"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    pduDaisyChainAlarmClear.setStatus(
        ""
    )

bmSystemAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 600)
)
bmSystemAlarm.setObjects(
      *(("CPS-MIB", "bmIdentSerialNumber"),
        ("CPS-MIB", "bmIdentName"),
        ("CPS-MIB", "bmIdentLocation"),
        ("CPS-MIB", "mtrapinfoBmEventId"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    bmSystemAlarm.setStatus(
        ""
    )

bmSystemWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 601)
)
bmSystemWarning.setObjects(
      *(("CPS-MIB", "bmIdentSerialNumber"),
        ("CPS-MIB", "bmIdentName"),
        ("CPS-MIB", "bmIdentLocation"),
        ("CPS-MIB", "mtrapinfoBmEventId"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    bmSystemWarning.setStatus(
        ""
    )

bmSystemInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 602)
)
bmSystemInfo.setObjects(
      *(("CPS-MIB", "bmIdentSerialNumber"),
        ("CPS-MIB", "bmIdentName"),
        ("CPS-MIB", "bmIdentLocation"),
        ("CPS-MIB", "mtrapinfoBmEventId"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    bmSystemInfo.setStatus(
        ""
    )

bmProbesAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 603)
)
bmProbesAlarm.setObjects(
      *(("CPS-MIB", "bmIdentSerialNumber"),
        ("CPS-MIB", "bmIdentName"),
        ("CPS-MIB", "bmIdentLocation"),
        ("CPS-MIB", "bmProbesStringIndex"),
        ("CPS-MIB", "bmProbesBattIndex"),
        ("CPS-MIB", "mtrapinfoBmEventId"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    bmProbesAlarm.setStatus(
        ""
    )

bmSProbesWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 604)
)
bmSProbesWarning.setObjects(
      *(("CPS-MIB", "bmIdentSerialNumber"),
        ("CPS-MIB", "bmIdentName"),
        ("CPS-MIB", "bmIdentLocation"),
        ("CPS-MIB", "bmProbesStringIndex"),
        ("CPS-MIB", "bmProbesBattIndex"),
        ("CPS-MIB", "mtrapinfoBmEventId"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    bmSProbesWarning.setStatus(
        ""
    )

bmProbesInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 3808, 0, 605)
)
bmProbesInfo.setObjects(
      *(("CPS-MIB", "bmIdentSerialNumber"),
        ("CPS-MIB", "bmIdentName"),
        ("CPS-MIB", "bmIdentLocation"),
        ("CPS-MIB", "bmProbesStringIndex"),
        ("CPS-MIB", "bmProbesBattIndex"),
        ("CPS-MIB", "mtrapinfoBmEventId"),
        ("CPS-MIB", "mtrapinfoString"))
)
if mibBuilder.loadTexts:
    bmProbesInfo.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CPS-MIB",
    **{"cps": cps,
       "communicationLost": communicationLost,
       "upsOverload": upsOverload,
       "upsDiagnosticsFailed": upsDiagnosticsFailed,
       "upsDischarged": upsDischarged,
       "upsOnBattery": upsOnBattery,
       "upsBoostOn": upsBoostOn,
       "lowBattery": lowBattery,
       "communicationEstablished": communicationEstablished,
       "powerRestored": powerRestored,
       "upsDiagnosticsPassed": upsDiagnosticsPassed,
       "returnFromLowBattery": returnFromLowBattery,
       "upsTurnedOff": upsTurnedOff,
       "upsSleeping": upsSleeping,
       "upsWokeUp": upsWokeUp,
       "upsRebootStarted": upsRebootStarted,
       "upsOverTemp": upsOverTemp,
       "returnFromOverTemp": returnFromOverTemp,
       "upsBuckOn": upsBuckOn,
       "returnFromOverLoad": returnFromOverLoad,
       "returnFromDischarged": returnFromDischarged,
       "upsScheduleShutdown": upsScheduleShutdown,
       "upsEnterSleep": upsEnterSleep,
       "upsChargerFailure": upsChargerFailure,
       "returnFromChargerFailure": returnFromChargerFailure,
       "upsTurnoffStarted": upsTurnoffStarted,
       "upsTurnedOn": upsTurnedOn,
       "upsRemoteCommandFailed": upsRemoteCommandFailed,
       "upsLostRedundant": upsLostRedundant,
       "upsSignalClientShutdown": upsSignalClientShutdown,
       "upsEmergencyPowerOff": upsEmergencyPowerOff,
       "nclBankOn": nclBankOn,
       "nclBankOff": nclBankOff,
       "upsCommandCancel": upsCommandCancel,
       "upsStartBatteryTest": upsStartBatteryTest,
       "upsRemainRuntimeLowThanThreshold": upsRemainRuntimeLowThanThreshold,
       "nclBankStartScheduleOff": nclBankStartScheduleOff,
       "upsEstimationAbort": upsEstimationAbort,
       "upsHardwareFault": upsHardwareFault,
       "upsBatteryNotPresent": upsBatteryNotPresent,
       "upsWiringFault": upsWiringFault,
       "upsWiringFaultCleared": upsWiringFaultCleared,
       "upsEnterBypassMode": upsEnterBypassMode,
       "upsReturnFromBypassMode": upsReturnFromBypassMode,
       "upsBypassOverload": upsBypassOverload,
       "upsBypassOverloadCleared": upsBypassOverloadCleared,
       "upsEnterECOMode": upsEnterECOMode,
       "upsReturnFromECOMode": upsReturnFromECOMode,
       "upsBatteryOverThreeYear": upsBatteryOverThreeYear,
       "upsBatteryExpiration": upsBatteryExpiration,
       "upsBatteryReplacement": upsBatteryReplacement,
       "upsModuleInvertorAlarm": upsModuleInvertorAlarm,
       "upsModuleRectifierAlarm": upsModuleRectifierAlarm,
       "upsModuleFanAlarm": upsModuleFanAlarm,
       "upsModuleManualShutdown": upsModuleManualShutdown,
       "upsModuleOverload": upsModuleOverload,
       "upsFirmwareUpgradeStart": upsFirmwareUpgradeStart,
       "upsFirmwareUpgradeEnd": upsFirmwareUpgradeEnd,
       "upsRFC1628TrapOnBattery": upsRFC1628TrapOnBattery,
       "upsRFC1628TrapTestCompleted": upsRFC1628TrapTestCompleted,
       "upsRFC1628TrapAlarmEntryAdded": upsRFC1628TrapAlarmEntryAdded,
       "failAuthViaHTTP": failAuthViaHTTP,
       "passwordChange": passwordChange,
       "failAuthViaConsole": failAuthViaConsole,
       "configFileUpload": configFileUpload,
       "adminLoginInfo": adminLoginInfo,
       "adminLogoutInfo": adminLogoutInfo,
       "deviceLoginInfo": deviceLoginInfo,
       "deviceLogoutInfo": deviceLogoutInfo,
       "configurationChanged": configurationChanged,
       "clientRegistered": clientRegistered,
       "clientRemoved": clientRemoved,
       "testEvent": testEvent,
       "outletUserLoginInfo": outletUserLoginInfo,
       "outletUserLogoutInfo": outletUserLogoutInfo,
       "ePDUCommunicationEstablished": ePDUCommunicationEstablished,
       "ePDUCommunicationLost": ePDUCommunicationLost,
       "ePDUOutletOn": ePDUOutletOn,
       "ePDUOutletOff": ePDUOutletOff,
       "ePDUDeviceConfigChange": ePDUDeviceConfigChange,
       "ePDUOutletConfigChange": ePDUOutletConfigChange,
       "ePDULowLoad": ePDULowLoad,
       "ePDULowLoadCleared": ePDULowLoadCleared,
       "ePDUNearOverload": ePDUNearOverload,
       "ePDUNearOverloadCleared": ePDUNearOverloadCleared,
       "ePDUOverload": ePDUOverload,
       "ePDUOverloadCleared": ePDUOverloadCleared,
       "ePDUDelayOutletOnCommand": ePDUDelayOutletOnCommand,
       "ePDUDelayOutletOffCommand": ePDUDelayOutletOffCommand,
       "ePDUDelayOutletRebootCommand": ePDUDelayOutletRebootCommand,
       "ePDUCancelPendingCommand": ePDUCancelPendingCommand,
       "ePDULineUndervoltage": ePDULineUndervoltage,
       "ePDULineUndervoltageCleared": ePDULineUndervoltageCleared,
       "ePDULineOvervoltage": ePDULineOvervoltage,
       "ePDULineOvervoltageCleared": ePDULineOvervoltageCleared,
       "ePDUPowerSupply1Fail": ePDUPowerSupply1Fail,
       "ePDUPowerSupply1Ok": ePDUPowerSupply1Ok,
       "ePDUPowerSupply2Fail": ePDUPowerSupply2Fail,
       "ePDUPowerSupply2Ok": ePDUPowerSupply2Ok,
       "ePDUBankLowLoad": ePDUBankLowLoad,
       "ePDUBankLowLoadCleared": ePDUBankLowLoadCleared,
       "ePDUBankNearOverload": ePDUBankNearOverload,
       "ePDUBankNearOverloadCleared": ePDUBankNearOverloadCleared,
       "ePDUBankOverload": ePDUBankOverload,
       "ePDUBankOverloadCleared": ePDUBankOverloadCleared,
       "ePDUComponentCommunicationEstablished": ePDUComponentCommunicationEstablished,
       "ePDUComponentCommunicationLost": ePDUComponentCommunicationLost,
       "ePDUOutletLowLoad": ePDUOutletLowLoad,
       "ePDUOutletLowLoadCleared": ePDUOutletLowLoadCleared,
       "ePDUOutletNearOverload": ePDUOutletNearOverload,
       "ePDUOutletNearOverloadCleared": ePDUOutletNearOverloadCleared,
       "ePDUOutletOverload": ePDUOutletOverload,
       "ePDUOutletOverloadCleared": ePDUOutletOverloadCleared,
       "envHighTemperatureViolation": envHighTemperatureViolation,
       "envHighTemperatureBack": envHighTemperatureBack,
       "envLowTemperatureViolation": envLowTemperatureViolation,
       "envLowTempBack": envLowTempBack,
       "envHighHumidityViolation": envHighHumidityViolation,
       "envHighHumidityBack": envHighHumidityBack,
       "envLowHumidityViolation": envLowHumidityViolation,
       "envLowHumdBack": envLowHumdBack,
       "envDryContactAbnormal": envDryContactAbnormal,
       "envDryContactNormal": envDryContactNormal,
       "envConntected": envConntected,
       "envDisconntected": envDisconntected,
       "envRateOfTemperatureChangeAbnormal": envRateOfTemperatureChangeAbnormal,
       "envRateOfHumdChangeAbnormal": envRateOfHumdChangeAbnormal,
       "atsSwitchSource": atsSwitchSource,
       "atsSourceFault": atsSourceFault,
       "atsSourceFaultCleared": atsSourceFaultCleared,
       "atsRedundancyFail": atsRedundancyFail,
       "atsRedundancyRestored": atsRedundancyRestored,
       "atsInputHighVoltage": atsInputHighVoltage,
       "atsInputHighVoltageCleared": atsInputHighVoltageCleared,
       "atsInputLowVoltage": atsInputLowVoltage,
       "atsInputLowVoltageCleared": atsInputLowVoltageCleared,
       "atsInputHighFrequency": atsInputHighFrequency,
       "atsInputHighFrequencyCleared": atsInputHighFrequencyCleared,
       "atsInputLowFrequency": atsInputLowFrequency,
       "atsInputLowFrequencyCleared": atsInputLowFrequencyCleared,
       "atsCommunicationLost": atsCommunicationLost,
       "atsCommunicationEstablished": atsCommunicationEstablished,
       "atsLCDCommunicationLost": atsLCDCommunicationLost,
       "atsLCDCommunicationLostCleared": atsLCDCommunicationLostCleared,
       "atsDB9CommunicationLost": atsDB9CommunicationLost,
       "atsDB9CommunicationLostCleared": atsDB9CommunicationLostCleared,
       "atsPowerSupplyFault": atsPowerSupplyFault,
       "atsPowerSupplyFaultCleared": atsPowerSupplyFaultCleared,
       "atsDevHardwareFault": atsDevHardwareFault,
       "atsDevHardwareFaultCleared": atsDevHardwareFaultCleared,
       "atsSourceConfigChanged": atsSourceConfigChanged,
       "atsDeviceConfigChanged": atsDeviceConfigChanged,
       "atsOutletConfigChanged": atsOutletConfigChanged,
       "atsEventCountsCleared": atsEventCountsCleared,
       "atsOverload": atsOverload,
       "atsOverloadCleared": atsOverloadCleared,
       "atsNearOverload": atsNearOverload,
       "atsNearOverloadCleared": atsNearOverloadCleared,
       "atsLowLoad": atsLowLoad,
       "atsLowLoadCleared": atsLowLoadCleared,
       "atsOutletOnCommand": atsOutletOnCommand,
       "atsOutletOffCommand": atsOutletOffCommand,
       "atsOutletRebootCommand": atsOutletRebootCommand,
       "atsCancelPendingCommand": atsCancelPendingCommand,
       "atsOutletOn": atsOutletOn,
       "atsOutletOff": atsOutletOff,
       "pduDeviceEvent": pduDeviceEvent,
       "pduDeviceAlarm": pduDeviceAlarm,
       "pduDeviceAlarmClear": pduDeviceAlarmClear,
       "pduPhaseEvent": pduPhaseEvent,
       "pduPhaseAlarm": pduPhaseAlarm,
       "pduPhaseAlarmClear": pduPhaseAlarmClear,
       "pduBankEvent": pduBankEvent,
       "pduBankAlarm": pduBankAlarm,
       "pduBankAlarmClear": pduBankAlarmClear,
       "pduOutletSwitchedEvent": pduOutletSwitchedEvent,
       "pduOutletSwitchedAlarm": pduOutletSwitchedAlarm,
       "pduOutletSwitchedAlarmClear": pduOutletSwitchedAlarmClear,
       "pduOutletMeteredEvent": pduOutletMeteredEvent,
       "pduOutletMeteredAlarm": pduOutletMeteredAlarm,
       "pduOutletMeteredAlarmClear": pduOutletMeteredAlarmClear,
       "pduDaisyChainEvent": pduDaisyChainEvent,
       "pduDaisyChainAlarm": pduDaisyChainAlarm,
       "pduDaisyChainAlarmClear": pduDaisyChainAlarmClear,
       "bmSystemAlarm": bmSystemAlarm,
       "bmSystemWarning": bmSystemWarning,
       "bmSystemInfo": bmSystemInfo,
       "bmProbesAlarm": bmProbesAlarm,
       "bmSProbesWarning": bmSProbesWarning,
       "bmProbesInfo": bmProbesInfo,
       "products": products,
       "hardware": hardware,
       "ups": ups,
       "upsIdent": upsIdent,
       "upsBaseIdent": upsBaseIdent,
       "upsBaseIdentModel": upsBaseIdentModel,
       "upsBaseIdentName": upsBaseIdentName,
       "upsAdvanceIdent": upsAdvanceIdent,
       "upsAdvanceIdentFirmwareRevision": upsAdvanceIdentFirmwareRevision,
       "upsAdvanceIdentDateOfManufacture": upsAdvanceIdentDateOfManufacture,
       "upsAdvanceIdentSerialNumber": upsAdvanceIdentSerialNumber,
       "upsAdvanceIdentAgentFirmwareRevision": upsAdvanceIdentAgentFirmwareRevision,
       "upsAdvanceIdentLCDFirmwareVersion": upsAdvanceIdentLCDFirmwareVersion,
       "upsAdvanceIdentPowerRating": upsAdvanceIdentPowerRating,
       "upsAdvanceIdentLoadPower": upsAdvanceIdentLoadPower,
       "upsAdvanceIdentCurrentRating": upsAdvanceIdentCurrentRating,
       "upsAdvanceIdentAgentSerialNumber": upsAdvanceIdentAgentSerialNumber,
       "upsBattery": upsBattery,
       "upsBaseBattery": upsBaseBattery,
       "upsBaseBatteryStatus": upsBaseBatteryStatus,
       "upsBaseBatteryTimeOnBattery": upsBaseBatteryTimeOnBattery,
       "upsBaseBatteryLastReplaceDate": upsBaseBatteryLastReplaceDate,
       "upsBaseBatteryAgeRecommand": upsBaseBatteryAgeRecommand,
       "upsAdvanceBattery": upsAdvanceBattery,
       "upsAdvanceBatteryCapacity": upsAdvanceBatteryCapacity,
       "upsAdvanceBatteryVoltage": upsAdvanceBatteryVoltage,
       "upsAdvanceBatteryTemperature": upsAdvanceBatteryTemperature,
       "upsAdvanceBatteryRunTimeRemaining": upsAdvanceBatteryRunTimeRemaining,
       "upsAdvanceBatteryReplaceIndicator": upsAdvanceBatteryReplaceIndicator,
       "upsAdvanceBatteryFullChargeVoltage": upsAdvanceBatteryFullChargeVoltage,
       "upsAdvanceBatteryCurrent": upsAdvanceBatteryCurrent,
       "upsAdvanceBatteryVoltageRating": upsAdvanceBatteryVoltageRating,
       "upsAdvanceBatteryLife": upsAdvanceBatteryLife,
       "upsInput": upsInput,
       "upsBaseInput": upsBaseInput,
       "upsBaseInputPhase": upsBaseInputPhase,
       "upsAdvanceInput": upsAdvanceInput,
       "upsAdvanceInputLineVoltage": upsAdvanceInputLineVoltage,
       "upsAdvanceInputMaxLineVoltage": upsAdvanceInputMaxLineVoltage,
       "upsAdvanceInputMinLineVoltage": upsAdvanceInputMinLineVoltage,
       "upsAdvanceInputFrequency": upsAdvanceInputFrequency,
       "upsAdvanceInputLineFailCause": upsAdvanceInputLineFailCause,
       "upsAdvanceInputStatus": upsAdvanceInputStatus,
       "upsOutput": upsOutput,
       "upsBaseOutput": upsBaseOutput,
       "upsBaseOutputStatus": upsBaseOutputStatus,
       "upsBaseOutputPhase": upsBaseOutputPhase,
       "upsBaseOutputWorkingFrequency": upsBaseOutputWorkingFrequency,
       "upsAdvanceOutput": upsAdvanceOutput,
       "upsAdvanceOutputVoltage": upsAdvanceOutputVoltage,
       "upsAdvanceOutputFrequency": upsAdvanceOutputFrequency,
       "upsAdvanceOutputLoad": upsAdvanceOutputLoad,
       "upsAdvanceOutputCurrent": upsAdvanceOutputCurrent,
       "upsAdvanceOutputPower": upsAdvanceOutputPower,
       "upsConfig": upsConfig,
       "upsBaseConfig": upsBaseConfig,
       "upsBaseConfigNumDevices": upsBaseConfigNumDevices,
       "upsBaseConfigDeviceTable": upsBaseConfigDeviceTable,
       "upsBaseConfigDeviceEntry": upsBaseConfigDeviceEntry,
       "deviceIndex": deviceIndex,
       "deviceName": deviceName,
       "vaRating": vaRating,
       "acceptThisDevice": acceptThisDevice,
       "upsAdvanceConfig": upsAdvanceConfig,
       "upsAdvanceConfigOutputVoltage": upsAdvanceConfigOutputVoltage,
       "upsAdvanceConfigHighTransferVolt": upsAdvanceConfigHighTransferVolt,
       "upsAdvanceConfigLowTransferVolt": upsAdvanceConfigLowTransferVolt,
       "upsAdvanceConfigAlarm": upsAdvanceConfigAlarm,
       "upsAdvanceConfigAlarmTimer": upsAdvanceConfigAlarmTimer,
       "upsAdvanceConfigMinReturnCapacity": upsAdvanceConfigMinReturnCapacity,
       "upsAdvanceConfigSensitivity": upsAdvanceConfigSensitivity,
       "upsAdvanceConfigLowBatteryRunTime": upsAdvanceConfigLowBatteryRunTime,
       "upsAdvanceConfigReturnDelay": upsAdvanceConfigReturnDelay,
       "upsAdvanceConfigShutoffDelay": upsAdvanceConfigShutoffDelay,
       "upsAdvanceConfigSleepDelay": upsAdvanceConfigSleepDelay,
       "upsAdvanceConfigSetEEPROMDefaults": upsAdvanceConfigSetEEPROMDefaults,
       "upsAdvanceConfigAutoRestore": upsAdvanceConfigAutoRestore,
       "upsAdvanceConfigRechargedCapacity": upsAdvanceConfigRechargedCapacity,
       "upsAdvanceConfigColdStart": upsAdvanceConfigColdStart,
       "upsAdvanceConfigDeepDischargeProtection": upsAdvanceConfigDeepDischargeProtection,
       "upsAdvanceConfigSleepAfterAllClientShut": upsAdvanceConfigSleepAfterAllClientShut,
       "upsAdvanceConfigLowBatteryThreshold": upsAdvanceConfigLowBatteryThreshold,
       "upsControl": upsControl,
       "upsBaseControl": upsBaseControl,
       "upsBaseControlConserveBattery": upsBaseControlConserveBattery,
       "upsAdvanceControl": upsAdvanceControl,
       "upsAdvanceControlUpsOff": upsAdvanceControlUpsOff,
       "upsAdvanceControlRebootUps": upsAdvanceControlRebootUps,
       "upsAdvanceControlUpsSleep": upsAdvanceControlUpsSleep,
       "upsAdvanceControlSimulatePowerFail": upsAdvanceControlSimulatePowerFail,
       "upsAdvanceControlFlashAndBeep": upsAdvanceControlFlashAndBeep,
       "upsAdvanceControlTurnOnUPS": upsAdvanceControlTurnOnUPS,
       "upsAdvanceSleepAfterDelay": upsAdvanceSleepAfterDelay,
       "upsTest": upsTest,
       "upsBaseTest": upsBaseTest,
       "upsAdvanceTest": upsAdvanceTest,
       "upsAdvanceTestDiagnosticSchedule": upsAdvanceTestDiagnosticSchedule,
       "upsAdvanceTestDiagnostics": upsAdvanceTestDiagnostics,
       "upsAdvanceTestDiagnosticsResults": upsAdvanceTestDiagnosticsResults,
       "upsAdvanceTestLastDiagnosticsDate": upsAdvanceTestLastDiagnosticsDate,
       "upsAdvanceTestIndicators": upsAdvanceTestIndicators,
       "upsAdvanceTestRuntimeEstimation": upsAdvanceTestRuntimeEstimation,
       "upsAdvanceTestEstimationResults": upsAdvanceTestEstimationResults,
       "upsAdvanceTestEstimationDate": upsAdvanceTestEstimationDate,
       "upsOutlet": upsOutlet,
       "upsBankOutletControl": upsBankOutletControl,
       "upsBankOutletControlTable": upsBankOutletControlTable,
       "upsBankOutletControlEntry": upsBankOutletControlEntry,
       "upsBankControlIndex": upsBankControlIndex,
       "upsBankControlOutletCommand": upsBankControlOutletCommand,
       "upsPhase": upsPhase,
       "upsPhaseInput": upsPhaseInput,
       "upsPhaseInputTableSize": upsPhaseInputTableSize,
       "upsPhaseInputTable": upsPhaseInputTable,
       "upsPhaseInputEntry": upsPhaseInputEntry,
       "upsPhaseInputTableIndex": upsPhaseInputTableIndex,
       "upsPhaseInputVoltage": upsPhaseInputVoltage,
       "upsPhaseInputCurrent": upsPhaseInputCurrent,
       "upsPhaseInputFrequency": upsPhaseInputFrequency,
       "upsPhaseInputPowerFactor": upsPhaseInputPowerFactor,
       "upsPhaseOutput": upsPhaseOutput,
       "upsPhaseOutputTableSize": upsPhaseOutputTableSize,
       "upsPhaseOutputTable": upsPhaseOutputTable,
       "upsPhaseOutputEntry": upsPhaseOutputEntry,
       "upsPhaseOutputTableIndex": upsPhaseOutputTableIndex,
       "upsPhaseOutputVoltage": upsPhaseOutputVoltage,
       "upsPhaseOutputCurrent": upsPhaseOutputCurrent,
       "upsPhaseOutputFrequency": upsPhaseOutputFrequency,
       "upsPhaseOutputPowerFactor": upsPhaseOutputPowerFactor,
       "upsPhaseOutputPower": upsPhaseOutputPower,
       "upsPhaseBypass": upsPhaseBypass,
       "upsPhaseBypassTableSize": upsPhaseBypassTableSize,
       "upsPhaseBypassTable": upsPhaseBypassTable,
       "upsPhaseBypassEntry": upsPhaseBypassEntry,
       "upsPhaseBypassTableIndex": upsPhaseBypassTableIndex,
       "upsPhaseBypassVoltage": upsPhaseBypassVoltage,
       "upsPhaseBypassCurrent": upsPhaseBypassCurrent,
       "upsPhaseBypassFrequency": upsPhaseBypassFrequency,
       "upsPhaseBypassPowerFactor": upsPhaseBypassPowerFactor,
       "upsSystem": upsSystem,
       "upsStatus": upsStatus,
       "eswitch": eswitch,
       "eSwitchIdent": eSwitchIdent,
       "eSwitchIdentHardwareRev": eSwitchIdentHardwareRev,
       "eSwitchIdentFirmwareRev": eSwitchIdentFirmwareRev,
       "eSwitchIdentDateOfManufacture": eSwitchIdentDateOfManufacture,
       "eSwitchIdentModelName": eSwitchIdentModelName,
       "eSwitchBase": eSwitchBase,
       "eSwitchNumber": eSwitchNumber,
       "eSwitchBaseTable": eSwitchBaseTable,
       "eSwitchBaseEntry": eSwitchBaseEntry,
       "eSwitchID": eSwitchID,
       "eSwitchOutletNum": eSwitchOutletNum,
       "eSwitchOutletState": eSwitchOutletState,
       "eSwitchBaseCtrTable": eSwitchBaseCtrTable,
       "eSwitchBaseCtrEntry": eSwitchBaseCtrEntry,
       "eSwitchCtrID": eSwitchCtrID,
       "eSwitchActOutlet": eSwitchActOutlet,
       "eSwitchActType": eSwitchActType,
       "ePDU": ePDU,
       "ePDUIdent": ePDUIdent,
       "ePDUIdentName": ePDUIdentName,
       "ePDUIdentHardwareRev": ePDUIdentHardwareRev,
       "ePDUIdentFirmwareRev": ePDUIdentFirmwareRev,
       "ePDUIdentDateOfManufacture": ePDUIdentDateOfManufacture,
       "ePDUIdentModelNumber": ePDUIdentModelNumber,
       "ePDUIdentSerialNumber": ePDUIdentSerialNumber,
       "ePDUIdentDeviceRating": ePDUIdentDeviceRating,
       "ePDUIdentDeviceNumOutlets": ePDUIdentDeviceNumOutlets,
       "ePDUIdentDeviceNumPhases": ePDUIdentDeviceNumPhases,
       "ePDUIdentDeviceNumBreakers": ePDUIdentDeviceNumBreakers,
       "ePDUIdentDeviceBreakerRating": ePDUIdentDeviceBreakerRating,
       "ePDUIdentDeviceOrientation": ePDUIdentDeviceOrientation,
       "ePDUIdentDeviceOutletLayout": ePDUIdentDeviceOutletLayout,
       "ePDUIdentDeviceDisplayOrientation": ePDUIdentDeviceDisplayOrientation,
       "ePDUIdentDeviceLinetoLineVoltage": ePDUIdentDeviceLinetoLineVoltage,
       "ePDUIdentIndicator": ePDUIdentIndicator,
       "ePDULoad": ePDULoad,
       "ePDULoadDevice": ePDULoadDevice,
       "ePDULoadDevMaxPhaseLoad": ePDULoadDevMaxPhaseLoad,
       "ePDULoadDevNumPhases": ePDULoadDevNumPhases,
       "ePDULoadDevMaxBankLoad": ePDULoadDevMaxBankLoad,
       "ePDULoadDevNumBanks": ePDULoadDevNumBanks,
       "ePDULoadDevBankTableSize": ePDULoadDevBankTableSize,
       "ePDULoadDevBankTable": ePDULoadDevBankTable,
       "ePDULoadDevBankEntry": ePDULoadDevBankEntry,
       "ePDULoadDevBankIndex": ePDULoadDevBankIndex,
       "ePDULoadDevBankNumber": ePDULoadDevBankNumber,
       "ePDULoadDevBankMaxLoad": ePDULoadDevBankMaxLoad,
       "ePDULoadDevMaxOutletTableSize": ePDULoadDevMaxOutletTableSize,
       "ePDULoadDevMaxOutletTable": ePDULoadDevMaxOutletTable,
       "ePDULoadDevMaxOutletEntry": ePDULoadDevMaxOutletEntry,
       "ePDULoadDevOutletIndex": ePDULoadDevOutletIndex,
       "ePDULoadDevOutletNumber": ePDULoadDevOutletNumber,
       "ePDULoadDevMaxOutletLoad": ePDULoadDevMaxOutletLoad,
       "ePDULoadPhaseConfig": ePDULoadPhaseConfig,
       "ePDULoadPhaseConfigTable": ePDULoadPhaseConfigTable,
       "ePDULoadPhaseConfigEntry": ePDULoadPhaseConfigEntry,
       "ePDULoadPhaseConfigIndex": ePDULoadPhaseConfigIndex,
       "ePDULoadPhaseConfigLowLoadThreshold": ePDULoadPhaseConfigLowLoadThreshold,
       "ePDULoadPhaseConfigNearOverloadThreshold": ePDULoadPhaseConfigNearOverloadThreshold,
       "ePDULoadPhaseConfigOverloadThreshold": ePDULoadPhaseConfigOverloadThreshold,
       "ePDULoadPhaseConfigAlarm": ePDULoadPhaseConfigAlarm,
       "ePDULoadStatus": ePDULoadStatus,
       "ePDULoadStatusTable": ePDULoadStatusTable,
       "ePDULoadStatusEntry": ePDULoadStatusEntry,
       "ePDULoadStatusIndex": ePDULoadStatusIndex,
       "ePDULoadStatusLoad": ePDULoadStatusLoad,
       "ePDULoadStatusLoadState": ePDULoadStatusLoadState,
       "ePDULoadStatusPhaseNumber": ePDULoadStatusPhaseNumber,
       "ePDULoadStatusBankNumber": ePDULoadStatusBankNumber,
       "ePDULoadStatusVoltage": ePDULoadStatusVoltage,
       "ePDULoadStatusActivePower": ePDULoadStatusActivePower,
       "ePDULoadStatusApparentPower": ePDULoadStatusApparentPower,
       "ePDULoadStatusPowerFactor": ePDULoadStatusPowerFactor,
       "ePDULoadStatusEnergy": ePDULoadStatusEnergy,
       "ePDULoadStatusEnergyStartTime": ePDULoadStatusEnergyStartTime,
       "ePDULoadBankConfig": ePDULoadBankConfig,
       "ePDULoadBankConfigTable": ePDULoadBankConfigTable,
       "ePDULoadBankConfigEntry": ePDULoadBankConfigEntry,
       "ePDULoadBankConfigIndex": ePDULoadBankConfigIndex,
       "ePDULoadBankConfigLowLoadThreshold": ePDULoadBankConfigLowLoadThreshold,
       "ePDULoadBankConfigNearOverloadThreshold": ePDULoadBankConfigNearOverloadThreshold,
       "ePDULoadBankConfigOverloadThreshold": ePDULoadBankConfigOverloadThreshold,
       "ePDULoadBankConfigAlarm": ePDULoadBankConfigAlarm,
       "ePDUOutlet": ePDUOutlet,
       "ePDUOutletDevice": ePDUOutletDevice,
       "ePDUOutletDevCommand": ePDUOutletDevCommand,
       "ePDUOutletDevColdstartDelay": ePDUOutletDevColdstartDelay,
       "ePDUOutletDevNumCntrlOutlets": ePDUOutletDevNumCntrlOutlets,
       "ePDUOutletDevNumTotalOutlets": ePDUOutletDevNumTotalOutlets,
       "ePDUOutletDevMonitoredOutlets": ePDUOutletDevMonitoredOutlets,
       "ePDUOutletDevColdstartState": ePDUOutletDevColdstartState,
       "ePDUOutletPhase": ePDUOutletPhase,
       "ePDUOutletPhaseTable": ePDUOutletPhaseTable,
       "ePDUOutletPhaseEntry": ePDUOutletPhaseEntry,
       "ePDUOutletPhaseIndex": ePDUOutletPhaseIndex,
       "ePDUOutletPhaseOverloadRestriction": ePDUOutletPhaseOverloadRestriction,
       "ePDUOutletControl": ePDUOutletControl,
       "ePDUOutletControlTable": ePDUOutletControlTable,
       "ePDUOutletControlEntry": ePDUOutletControlEntry,
       "ePDUOutletControlIndex": ePDUOutletControlIndex,
       "ePDUOutletControlOutletName": ePDUOutletControlOutletName,
       "ePDUOutletControlOutletPhase": ePDUOutletControlOutletPhase,
       "ePDUOutletControlOutletCommand": ePDUOutletControlOutletCommand,
       "ePDUOutletControlOutletBank": ePDUOutletControlOutletBank,
       "ePDUOutletConfig": ePDUOutletConfig,
       "ePDUOutletConfigTable": ePDUOutletConfigTable,
       "ePDUOutletConfigEntry": ePDUOutletConfigEntry,
       "ePDUOutletConfigIndex": ePDUOutletConfigIndex,
       "ePDUOutletConfigOutletName": ePDUOutletConfigOutletName,
       "ePDUOutletConfigOutletPhase": ePDUOutletConfigOutletPhase,
       "ePDUOutletConfigPowerOnTime": ePDUOutletConfigPowerOnTime,
       "ePDUOutletConfigPowerOffTime": ePDUOutletConfigPowerOffTime,
       "ePDUOutletConfigRebootDuration": ePDUOutletConfigRebootDuration,
       "ePDUOutletConfigOutletBank": ePDUOutletConfigOutletBank,
       "ePDUOutletConfigMonitoredTableSize": ePDUOutletConfigMonitoredTableSize,
       "ePDUOutletConfigMonitoredTable": ePDUOutletConfigMonitoredTable,
       "ePDUOutletConfigMonitoredEntry": ePDUOutletConfigMonitoredEntry,
       "ePDUOutletConfigMonitoredIndex": ePDUOutletConfigMonitoredIndex,
       "ePDUOutletConfigMonitoredName": ePDUOutletConfigMonitoredName,
       "ePDUOutletConfigMonitoredNumber": ePDUOutletConfigMonitoredNumber,
       "ePDUOutletConfigMonitoredLowLoadThreshold": ePDUOutletConfigMonitoredLowLoadThreshold,
       "ePDUOutletConfigMonitoredNearOverloadThreshold": ePDUOutletConfigMonitoredNearOverloadThreshold,
       "ePDUOutletConfigMonitoredOverloadThreshold": ePDUOutletConfigMonitoredOverloadThreshold,
       "ePDUOutletConfigMonitoredPeakLoadReset": ePDUOutletConfigMonitoredPeakLoadReset,
       "ePDUOutletConfigMonitoredEnergyReset": ePDUOutletConfigMonitoredEnergyReset,
       "ePDUOutletStatus": ePDUOutletStatus,
       "ePDUOutletStatusTable": ePDUOutletStatusTable,
       "ePDUOutletStatusEntry": ePDUOutletStatusEntry,
       "ePDUOutletStatusIndex": ePDUOutletStatusIndex,
       "ePDUOutletStatusOutletName": ePDUOutletStatusOutletName,
       "ePDUOutletStatusOutletPhase": ePDUOutletStatusOutletPhase,
       "ePDUOutletStatusOutletState": ePDUOutletStatusOutletState,
       "ePDUOutletStatusCommandPending": ePDUOutletStatusCommandPending,
       "ePDUOutletStatusOutletBank": ePDUOutletStatusOutletBank,
       "ePDUOutletStatusLoad": ePDUOutletStatusLoad,
       "ePDUOutletStatusActivePower": ePDUOutletStatusActivePower,
       "ePDUOutletStatusAlarm": ePDUOutletStatusAlarm,
       "ePDUOutletStatusPeakPower": ePDUOutletStatusPeakPower,
       "ePDUOutletStatusPeakPowerTime": ePDUOutletStatusPeakPowerTime,
       "ePDUOutletStatusPeakPowerStart": ePDUOutletStatusPeakPowerStart,
       "ePDUOutletStatusEnergy": ePDUOutletStatusEnergy,
       "ePDUOutletStatusEnergyStartTime": ePDUOutletStatusEnergyStartTime,
       "ePDUOutletBank": ePDUOutletBank,
       "ePDUOutletBankTable": ePDUOutletBankTable,
       "ePDUOutletBankEntry": ePDUOutletBankEntry,
       "ePDUOutletBankIndex": ePDUOutletBankIndex,
       "ePDUOutletBankOverloadRestriction": ePDUOutletBankOverloadRestriction,
       "ePDUPowerSupply": ePDUPowerSupply,
       "ePDUPowerSupplyDevice": ePDUPowerSupplyDevice,
       "ePDUPowerSupply1Status": ePDUPowerSupply1Status,
       "ePDUPowerSupply2Status": ePDUPowerSupply2Status,
       "ePDUPowerSupplyAlarm": ePDUPowerSupplyAlarm,
       "ePDUStatus": ePDUStatus,
       "ePDUStatusBankTableSize": ePDUStatusBankTableSize,
       "ePDUStatusBankTable": ePDUStatusBankTable,
       "ePDUStatusBankEntry": ePDUStatusBankEntry,
       "ePDUStatusBankIndex": ePDUStatusBankIndex,
       "ePDUStatusBankNumber": ePDUStatusBankNumber,
       "ePDUStatusBankState": ePDUStatusBankState,
       "ePDUStatusPhaseTableSize": ePDUStatusPhaseTableSize,
       "ePDUStatusPhaseTable": ePDUStatusPhaseTable,
       "ePDUStatusPhaseEntry": ePDUStatusPhaseEntry,
       "ePDUStatusPhaseIndex": ePDUStatusPhaseIndex,
       "ePDUStatusPhaseNumber": ePDUStatusPhaseNumber,
       "ePDUStatusPhaseState": ePDUStatusPhaseState,
       "ePDUStatusOutletTableSize": ePDUStatusOutletTableSize,
       "ePDUStatusOutletTable": ePDUStatusOutletTable,
       "ePDUStatusOutletEntry": ePDUStatusOutletEntry,
       "ePDUStatusOutletIndex": ePDUStatusOutletIndex,
       "ePDUStatusOutletNumber": ePDUStatusOutletNumber,
       "ePDUStatusOutletState": ePDUStatusOutletState,
       "ePDUStatusInputVoltage": ePDUStatusInputVoltage,
       "ePDUStatusInputFrequency": ePDUStatusInputFrequency,
       "environmentSensor": environmentSensor,
       "envirIdent": envirIdent,
       "envirIdentName": envirIdentName,
       "envirIdentLocation": envirIdentLocation,
       "envirTemp": envirTemp,
       "envirTemperature": envirTemperature,
       "envirTempHighThreshold": envirTempHighThreshold,
       "envirTempLowThreshold": envirTempLowThreshold,
       "envirTempRateOfChange": envirTempRateOfChange,
       "envirTempHysteresis": envirTempHysteresis,
       "envirTemperatureCelsius": envirTemperatureCelsius,
       "envirTempCelsiusHighThreshold": envirTempCelsiusHighThreshold,
       "envirTempCelsiusLowThreshold": envirTempCelsiusLowThreshold,
       "envirTempCelsiusRateOfChange": envirTempCelsiusRateOfChange,
       "envirTempCelsiusHysteresis": envirTempCelsiusHysteresis,
       "envirHumid": envirHumid,
       "envirHumidity": envirHumidity,
       "envirHumidHighThreshold": envirHumidHighThreshold,
       "envirHumidLowThreshold": envirHumidLowThreshold,
       "envirHumidRateOfChange": envirHumidRateOfChange,
       "envirHumidHysteresis": envirHumidHysteresis,
       "envirContact": envirContact,
       "envirContactTableSize": envirContactTableSize,
       "envirContactTable": envirContactTable,
       "envirContactEntry": envirContactEntry,
       "envirContactIndex": envirContactIndex,
       "envirContactName": envirContactName,
       "envirContactStatus": envirContactStatus,
       "envirContactNormalState": envirContactNormalState,
       "ats": ats,
       "atsIdent": atsIdent,
       "atsIdentName": atsIdentName,
       "atsIdentModelName": atsIdentModelName,
       "atsIdentHardwareRev": atsIdentHardwareRev,
       "atsIdentFirmwareRev": atsIdentFirmwareRev,
       "atsIdentSerialNumber": atsIdentSerialNumber,
       "atsIdentDateOfManufacture": atsIdentDateOfManufacture,
       "atsIdentDeviceRatingVoltage": atsIdentDeviceRatingVoltage,
       "atsIdentDeviceRatingCurrent": atsIdentDeviceRatingCurrent,
       "atsIdentDeviceOutletNum": atsIdentDeviceOutletNum,
       "atsIdentAgentModelName": atsIdentAgentModelName,
       "atsIdentAgentHardwareRevision": atsIdentAgentHardwareRevision,
       "atsIdentAgentFirmwareRevision": atsIdentAgentFirmwareRevision,
       "atsIdentAgentSerialNumber": atsIdentAgentSerialNumber,
       "atsStatus": atsStatus,
       "atsStatusDevice": atsStatusDevice,
       "atsStatusCommStatus": atsStatusCommStatus,
       "atsStatusSelectedSource": atsStatusSelectedSource,
       "atsStatusRedundancyState": atsStatusRedundancyState,
       "atsStatusPhaseSyncStatus": atsStatusPhaseSyncStatus,
       "atsStatusDevSourceRelayStatus": atsStatusDevSourceRelayStatus,
       "atsStatusDevInRelayStatus": atsStatusDevInRelayStatus,
       "atsStatusDevOutRelayStatus": atsStatusDevOutRelayStatus,
       "atsStatusDevLCDCommStatus": atsStatusDevLCDCommStatus,
       "atsStatusDevDB9CommStatus": atsStatusDevDB9CommStatus,
       "atsStatusPowerSupplyTable": atsStatusPowerSupplyTable,
       "atsStatusPowerSupplyEntry": atsStatusPowerSupplyEntry,
       "atsStatusPowerSupplyTableIndex": atsStatusPowerSupplyTableIndex,
       "atsStatusPowerSupplyInputSource": atsStatusPowerSupplyInputSource,
       "atsStatusPowerSupply12VStatus": atsStatusPowerSupply12VStatus,
       "atsStatusPowerSupply5VStatus": atsStatusPowerSupply5VStatus,
       "atsStatusPowerSupply3p3VStatus": atsStatusPowerSupply3p3VStatus,
       "atsStatusInput": atsStatusInput,
       "atsStatusInputNum": atsStatusInputNum,
       "atsStatusInputTable": atsStatusInputTable,
       "atsStatusInputEntry": atsStatusInputEntry,
       "atsStatusInputTableIndex": atsStatusInputTableIndex,
       "atsStatusInputName": atsStatusInputName,
       "atsStatusNumInputPhase": atsStatusNumInputPhase,
       "atsStatusInputVoltageOrientation": atsStatusInputVoltageOrientation,
       "atsStatusInputVoltage": atsStatusInputVoltage,
       "atsStatusInputFrequency": atsStatusInputFrequency,
       "atsStatusInputVolState": atsStatusInputVolState,
       "atsStatusInputFreqState": atsStatusInputFreqState,
       "atsStatusInputPhaseTable": atsStatusInputPhaseTable,
       "atsStatusInputPhaseEntry": atsStatusInputPhaseEntry,
       "atsStatusInputPhaseTableIndex": atsStatusInputPhaseTableIndex,
       "atsStatusInputPhaseIndex": atsStatusInputPhaseIndex,
       "atsStatusInputPhaseVoltage": atsStatusInputPhaseVoltage,
       "atsStatusInputPhaseCurrent": atsStatusInputPhaseCurrent,
       "atsStatusInputPhasePower": atsStatusInputPhasePower,
       "atsConfig": atsConfig,
       "atsConfigPreferredSource": atsConfigPreferredSource,
       "atsConfigNominalVoltage": atsConfigNominalVoltage,
       "atsConfigVoltageSensitivity": atsConfigVoltageSensitivity,
       "atsConfigTransferVoltageRange": atsConfigTransferVoltageRange,
       "atsConfigNarrowRangeValue": atsConfigNarrowRangeValue,
       "atsConfigMediumRangeValue": atsConfigMediumRangeValue,
       "atsConfigWideRangeValue": atsConfigWideRangeValue,
       "atsConfigFrequencyDeviation": atsConfigFrequencyDeviation,
       "atsConfigDevLCDOffTime": atsConfigDevLCDOffTime,
       "atsControl": atsControl,
       "atsCtrlResetATS": atsCtrlResetATS,
       "atsCtrlClearEventCounts": atsCtrlClearEventCounts,
       "atsLoad": atsLoad,
       "atsLoadDevice": atsLoadDevice,
       "atsLoadDevPhaseTableSize": atsLoadDevPhaseTableSize,
       "atsLoadDevPhaseTable": atsLoadDevPhaseTable,
       "atsLoadDevPhaseEntry": atsLoadDevPhaseEntry,
       "atsLoadDevPhaseTableIndex": atsLoadDevPhaseTableIndex,
       "atsLoadDevPhase": atsLoadDevPhase,
       "atsLoadDevPhaseMaxLoad": atsLoadDevPhaseMaxLoad,
       "atsLoadDevBankTableSize": atsLoadDevBankTableSize,
       "atsLoadDevBankTable": atsLoadDevBankTable,
       "atsLoadDevBankEntry": atsLoadDevBankEntry,
       "atsLoadDevBankTableIndex": atsLoadDevBankTableIndex,
       "atsLoadDevBankMaxLoad": atsLoadDevBankMaxLoad,
       "atsLoadStatus": atsLoadStatus,
       "atsLoadStatusPhaseTableSize": atsLoadStatusPhaseTableSize,
       "atsLoadStatusPhaseTable": atsLoadStatusPhaseTable,
       "atsLoadStatusPhaseEntry": atsLoadStatusPhaseEntry,
       "atsLoadStatusPhaseTableIndex": atsLoadStatusPhaseTableIndex,
       "atsLoadStatusPhase": atsLoadStatusPhase,
       "atsLoadStatusPhaseLoad": atsLoadStatusPhaseLoad,
       "atsLoadStatusPhaseLoadState": atsLoadStatusPhaseLoadState,
       "atsLoadStatusPhasePower": atsLoadStatusPhasePower,
       "atsLoadStatusBankTableSize": atsLoadStatusBankTableSize,
       "atsLoadStatusBankTable": atsLoadStatusBankTable,
       "atsLoadStatusBankEntry": atsLoadStatusBankEntry,
       "atsLoadStatusBankTableIndex": atsLoadStatusBankTableIndex,
       "atsLoadStatusBankPhase": atsLoadStatusBankPhase,
       "atsLoadStatusBankLoad": atsLoadStatusBankLoad,
       "atsLoadStatusBankLoadState": atsLoadStatusBankLoadState,
       "atsLoadStatusBankPower": atsLoadStatusBankPower,
       "atsLoadStatusBankEnergy": atsLoadStatusBankEnergy,
       "atsLoadStatusBankStartTime": atsLoadStatusBankStartTime,
       "atsLoadConfig": atsLoadConfig,
       "atsLoadCfgPhaseTableSize": atsLoadCfgPhaseTableSize,
       "atsLoadCfgPhaseTable": atsLoadCfgPhaseTable,
       "atsLoadCfgPhaseEntry": atsLoadCfgPhaseEntry,
       "atsLoadCfgPhaseTableIndex": atsLoadCfgPhaseTableIndex,
       "atsLoadCfgPhase": atsLoadCfgPhase,
       "atsLoadCfgPhaseLowLoad": atsLoadCfgPhaseLowLoad,
       "atsLoadCfgPhaseNearOverLoad": atsLoadCfgPhaseNearOverLoad,
       "atsLoadCfgPhaseOverLoad": atsLoadCfgPhaseOverLoad,
       "atsLoadCfgPhaseOutletRestriction": atsLoadCfgPhaseOutletRestriction,
       "atsLoadCfgBankTableSize": atsLoadCfgBankTableSize,
       "atsLoadCfgBankTable": atsLoadCfgBankTable,
       "atsLoadCfgBankEntry": atsLoadCfgBankEntry,
       "atsLoadCfgBankTableIndex": atsLoadCfgBankTableIndex,
       "atsLoadCfgBankLowLoad": atsLoadCfgBankLowLoad,
       "atsLoadCfgBankNearOverLoad": atsLoadCfgBankNearOverLoad,
       "atsLoadCfgBankOverLoad": atsLoadCfgBankOverLoad,
       "atsLoadCfgBankOutletRestriction": atsLoadCfgBankOutletRestriction,
       "atsOutlet": atsOutlet,
       "atsOutletDevice": atsOutletDevice,
       "atsOutletDevTotalOutletNum": atsOutletDevTotalOutletNum,
       "atsOutletDevCtrlOutletNum": atsOutletDevCtrlOutletNum,
       "atsOutletDevColdStartDelay": atsOutletDevColdStartDelay,
       "atsOutletDevColdStartState": atsOutletDevColdStartState,
       "atsOutletDevLocalCtrl": atsOutletDevLocalCtrl,
       "atsOutletDevCommand": atsOutletDevCommand,
       "atsOutletStatusTableSize": atsOutletStatusTableSize,
       "atsOutletStatusTable": atsOutletStatusTable,
       "atsOutletStatusEntry": atsOutletStatusEntry,
       "atsOutletStatusTableIndex": atsOutletStatusTableIndex,
       "atsOutletStatusOutletName": atsOutletStatusOutletName,
       "atsOutletStatusOutletState": atsOutletStatusOutletState,
       "atsOutletStatusOutletCmdPending": atsOutletStatusOutletCmdPending,
       "atsOutletStatusOutletPhase": atsOutletStatusOutletPhase,
       "atsOutletStatusOutletBank": atsOutletStatusOutletBank,
       "atsOutletCtrlTableSize": atsOutletCtrlTableSize,
       "atsOutletCtrlTable": atsOutletCtrlTable,
       "atsOutletCtrlEntry": atsOutletCtrlEntry,
       "atsOutletCtrlTableIndex": atsOutletCtrlTableIndex,
       "atsOutletCtrlOutletName": atsOutletCtrlOutletName,
       "atsOutletCtrlCommand": atsOutletCtrlCommand,
       "atsOutletCfgTableSize": atsOutletCfgTableSize,
       "atsOutletCfgTable": atsOutletCfgTable,
       "atsOutletCfgEntry": atsOutletCfgEntry,
       "atsOutletCfgTableIndex": atsOutletCfgTableIndex,
       "atsOutletCfgOutletName": atsOutletCfgOutletName,
       "atsOutletCfgPowerOnTime": atsOutletCfgPowerOnTime,
       "atsOutletCfgPowerOffTime": atsOutletCfgPowerOffTime,
       "atsOutletCfgRebootDuration": atsOutletCfgRebootDuration,
       "ePDU2": ePDU2,
       "ePDU2Role": ePDU2Role,
       "ePDU2Ident": ePDU2Ident,
       "ePDU2IdentTableSize": ePDU2IdentTableSize,
       "ePDU2IdentTable": ePDU2IdentTable,
       "ePDU2IdentEntry": ePDU2IdentEntry,
       "ePDU2IdentIndex": ePDU2IdentIndex,
       "ePDU2IdentModuleIndex": ePDU2IdentModuleIndex,
       "ePDU2IdentName": ePDU2IdentName,
       "ePDU2IdentLocation": ePDU2IdentLocation,
       "ePDU2IdentContact": ePDU2IdentContact,
       "ePDU2IdentHardwareRev": ePDU2IdentHardwareRev,
       "ePDU2IdentFirmwareRev": ePDU2IdentFirmwareRev,
       "ePDU2IdentDateOfManufacture": ePDU2IdentDateOfManufacture,
       "ePDU2IdentModelName": ePDU2IdentModelName,
       "ePDU2IdentSerialNumber": ePDU2IdentSerialNumber,
       "ePDU2IdentIndicator": ePDU2IdentIndicator,
       "ePDU2Device": ePDU2Device,
       "ePDU2DeviceTableSize": ePDU2DeviceTableSize,
       "ePDU2DeviceConfigTable": ePDU2DeviceConfigTable,
       "ePDU2DeviceConfigEntry": ePDU2DeviceConfigEntry,
       "ePDU2DeviceConfigIndex": ePDU2DeviceConfigIndex,
       "ePDU2DeviceConfigModuleIndex": ePDU2DeviceConfigModuleIndex,
       "ePDU2DeviceConfigName": ePDU2DeviceConfigName,
       "ePDU2DeviceConfigLocation": ePDU2DeviceConfigLocation,
       "ePDU2DeviceConfigContact": ePDU2DeviceConfigContact,
       "ePDU2DeviceConfigDisplayOrientation": ePDU2DeviceConfigDisplayOrientation,
       "ePDU2DeviceConfigColdstartDelay": ePDU2DeviceConfigColdstartDelay,
       "ePDU2DeviceConfigCurrentLowLoadThreshold": ePDU2DeviceConfigCurrentLowLoadThreshold,
       "ePDU2DeviceConfigCurrentNearOverloadThreshold": ePDU2DeviceConfigCurrentNearOverloadThreshold,
       "ePDU2DeviceConfigCurrentOverloadThreshold": ePDU2DeviceConfigCurrentOverloadThreshold,
       "ePDU2DeviceConfigPeakLoadReset": ePDU2DeviceConfigPeakLoadReset,
       "ePDU2DeviceConfigEnergyReset": ePDU2DeviceConfigEnergyReset,
       "ePDU2DeviceConfigPowerLowLoadThreshold": ePDU2DeviceConfigPowerLowLoadThreshold,
       "ePDU2DeviceConfigPowerNearOverloadThreshold": ePDU2DeviceConfigPowerNearOverloadThreshold,
       "ePDU2DeviceConfigPowerOverloadThreshold": ePDU2DeviceConfigPowerOverloadThreshold,
       "ePDU2DeviceInfoTable": ePDU2DeviceInfoTable,
       "ePDU2DeviceInfoEntry": ePDU2DeviceInfoEntry,
       "ePDU2DeviceInfoIndex": ePDU2DeviceInfoIndex,
       "ePDU2DeviceInfoModuleIndex": ePDU2DeviceInfoModuleIndex,
       "ePDU2DeviceInfoName": ePDU2DeviceInfoName,
       "ePDU2DeviceInfoRating": ePDU2DeviceInfoRating,
       "ePDU2DeviceInfoNumOutlets": ePDU2DeviceInfoNumOutlets,
       "ePDU2DeviceInfoSwitchedOutlets": ePDU2DeviceInfoSwitchedOutlets,
       "ePDU2DeviceInfoMeteredOutlets": ePDU2DeviceInfoMeteredOutlets,
       "ePDU2DeviceInfoNumPhases": ePDU2DeviceInfoNumPhases,
       "ePDU2DeviceInfoNumBreakers": ePDU2DeviceInfoNumBreakers,
       "ePDU2DeviceInfoBreakerRating": ePDU2DeviceInfoBreakerRating,
       "ePDU2DeviceInfoOrientation": ePDU2DeviceInfoOrientation,
       "ePDU2DeviceInfoOutletLayout": ePDU2DeviceInfoOutletLayout,
       "ePDU2DeviceStatusTable": ePDU2DeviceStatusTable,
       "ePDU2DeviceStatusEntry": ePDU2DeviceStatusEntry,
       "ePDU2DeviceStatusIndex": ePDU2DeviceStatusIndex,
       "ePDU2DeviceStatusModuleIndex": ePDU2DeviceStatusModuleIndex,
       "ePDU2DeviceStatusName": ePDU2DeviceStatusName,
       "ePDU2DeviceStatusLoadState": ePDU2DeviceStatusLoadState,
       "ePDU2DeviceStatusCurrentLoad": ePDU2DeviceStatusCurrentLoad,
       "ePDU2DeviceStatusCurrentPeakLoad": ePDU2DeviceStatusCurrentPeakLoad,
       "ePDU2DeviceStatusPeakLoadTimestamp": ePDU2DeviceStatusPeakLoadTimestamp,
       "ePDU2DeviceStatusPeakLoadStartTime": ePDU2DeviceStatusPeakLoadStartTime,
       "ePDU2DeviceStatusEnergy": ePDU2DeviceStatusEnergy,
       "ePDU2DeviceStatusEnergyStartTime": ePDU2DeviceStatusEnergyStartTime,
       "ePDU2DeviceStatusCommandPending": ePDU2DeviceStatusCommandPending,
       "ePDU2DeviceStatusPowerSupplyAlarm": ePDU2DeviceStatusPowerSupplyAlarm,
       "ePDU2DeviceStatusPowerSupply1Status": ePDU2DeviceStatusPowerSupply1Status,
       "ePDU2DeviceStatusPowerSupply2Status": ePDU2DeviceStatusPowerSupply2Status,
       "ePDU2DeviceStatusApparentPower": ePDU2DeviceStatusApparentPower,
       "ePDU2DeviceStatusPowerFactor": ePDU2DeviceStatusPowerFactor,
       "ePDU2DeviceStatusRoleType": ePDU2DeviceStatusRoleType,
       "ePDU2DeviceStatusPowerLoad": ePDU2DeviceStatusPowerLoad,
       "ePDU2DeviceStatusPowerPeakLoad": ePDU2DeviceStatusPowerPeakLoad,
       "ePDU2DeviceControlTable": ePDU2DeviceControlTable,
       "ePDU2DeviceControlEntry": ePDU2DeviceControlEntry,
       "ePDU2DeviceControlIndex": ePDU2DeviceControlIndex,
       "ePDU2DeviceControlModuleIndex": ePDU2DeviceControlModuleIndex,
       "ePDU2DeviceControlName": ePDU2DeviceControlName,
       "ePDU2DeviceControlCommand": ePDU2DeviceControlCommand,
       "ePDU2Phase": ePDU2Phase,
       "ePDU2PhaseTableSize": ePDU2PhaseTableSize,
       "ePDU2PhaseConfigTable": ePDU2PhaseConfigTable,
       "ePDU2PhaseConfigEntry": ePDU2PhaseConfigEntry,
       "ePDU2PhaseConfigIndex": ePDU2PhaseConfigIndex,
       "ePDU2PhaseConfigModuleIndex": ePDU2PhaseConfigModuleIndex,
       "ePDU2PhaseConfigNumber": ePDU2PhaseConfigNumber,
       "ePDU2PhaseConfigOverloadRestriction": ePDU2PhaseConfigOverloadRestriction,
       "ePDU2PhaseConfigLowLoadThreshold": ePDU2PhaseConfigLowLoadThreshold,
       "ePDU2PhaseConfigNearOverloadThreshold": ePDU2PhaseConfigNearOverloadThreshold,
       "ePDU2PhaseConfigOverloadThreshold": ePDU2PhaseConfigOverloadThreshold,
       "ePDU2PhaseConfigPhasePeakLoadReset": ePDU2PhaseConfigPhasePeakLoadReset,
       "ePDU2PhaseInfoTable": ePDU2PhaseInfoTable,
       "ePDU2PhaseInfoEntry": ePDU2PhaseInfoEntry,
       "ePDU2PhaseInfoIndex": ePDU2PhaseInfoIndex,
       "ePDU2PhaseInfoModuleIndex": ePDU2PhaseInfoModuleIndex,
       "ePDU2PhaseInfoNumber": ePDU2PhaseInfoNumber,
       "ePDU2PhaseStatusTable": ePDU2PhaseStatusTable,
       "ePDU2PhaseStatusEntry": ePDU2PhaseStatusEntry,
       "ePDU2PhaseStatusIndex": ePDU2PhaseStatusIndex,
       "ePDU2PhaseStatusModuleIndex": ePDU2PhaseStatusModuleIndex,
       "ePDU2PhaseStatusNumber": ePDU2PhaseStatusNumber,
       "ePDU2PhaseStatusLoadState": ePDU2PhaseStatusLoadState,
       "ePDU2PhaseStatusLoad": ePDU2PhaseStatusLoad,
       "ePDU2PhaseStatusVoltage": ePDU2PhaseStatusVoltage,
       "ePDU2PhaseStatusPower": ePDU2PhaseStatusPower,
       "ePDU2PhaseStatusApparentPower": ePDU2PhaseStatusApparentPower,
       "ePDU2PhaseStatusPowerFactor": ePDU2PhaseStatusPowerFactor,
       "ePDU2PhaseStatusPeakLoad": ePDU2PhaseStatusPeakLoad,
       "ePDU2PhaseStatusPeakLoadTimestamp": ePDU2PhaseStatusPeakLoadTimestamp,
       "ePDU2PhaseStatusPeakLoadStartTime": ePDU2PhaseStatusPeakLoadStartTime,
       "ePDU2PhaseStatusLineToLineVoltage": ePDU2PhaseStatusLineToLineVoltage,
       "ePDU2Bank": ePDU2Bank,
       "ePDU2BankTableSize": ePDU2BankTableSize,
       "ePDU2BankConfigTable": ePDU2BankConfigTable,
       "ePDU2BankConfigEntry": ePDU2BankConfigEntry,
       "ePDU2BankConfigIndex": ePDU2BankConfigIndex,
       "ePDU2BankConfigModuleIndex": ePDU2BankConfigModuleIndex,
       "ePDU2BankConfigNumber": ePDU2BankConfigNumber,
       "ePDU2BankConfigOverloadRestriction": ePDU2BankConfigOverloadRestriction,
       "ePDU2BankConfigLowLoadThreshold": ePDU2BankConfigLowLoadThreshold,
       "ePDU2BankConfigNearOverloadThreshold": ePDU2BankConfigNearOverloadThreshold,
       "ePDU2BankConfigOverloadThreshold": ePDU2BankConfigOverloadThreshold,
       "ePDU2BankConfigPeakLoadReset": ePDU2BankConfigPeakLoadReset,
       "ePDU2BankInfoTable": ePDU2BankInfoTable,
       "ePDU2BankInfoEntry": ePDU2BankInfoEntry,
       "ePDU2BankInfoIndex": ePDU2BankInfoIndex,
       "ePDU2BankInfoModuleIndex": ePDU2BankInfoModuleIndex,
       "ePDU2BankInfoNumber": ePDU2BankInfoNumber,
       "ePDU2BankStatusTable": ePDU2BankStatusTable,
       "ePDU2BankStatusEntry": ePDU2BankStatusEntry,
       "ePDU2BankStatusIndex": ePDU2BankStatusIndex,
       "ePDU2BankStatusModuleIndex": ePDU2BankStatusModuleIndex,
       "ePDU2BankStatusNumber": ePDU2BankStatusNumber,
       "ePDU2BankStatusLoadState": ePDU2BankStatusLoadState,
       "ePDU2BankStatusLoad": ePDU2BankStatusLoad,
       "ePDU2BankStatusPeakLoad": ePDU2BankStatusPeakLoad,
       "ePDU2BankStatusPeakLoadTimestamp": ePDU2BankStatusPeakLoadTimestamp,
       "ePDU2BankStatusPeakLoadStartTime": ePDU2BankStatusPeakLoadStartTime,
       "ePDU2Outlet": ePDU2Outlet,
       "ePDU2OutletSwitched": ePDU2OutletSwitched,
       "ePDU2OutletSwitchedTableSize": ePDU2OutletSwitchedTableSize,
       "ePDU2OutletSwitchedConfigTable": ePDU2OutletSwitchedConfigTable,
       "ePDU2OutletSwitchedConfigEntry": ePDU2OutletSwitchedConfigEntry,
       "ePDU2OutletSwitchedConfigIndex": ePDU2OutletSwitchedConfigIndex,
       "ePDU2OutletSwitchedConfigModuleIndex": ePDU2OutletSwitchedConfigModuleIndex,
       "ePDU2OutletSwitchedConfigNumber": ePDU2OutletSwitchedConfigNumber,
       "ePDU2OutletSwitchedConfigName": ePDU2OutletSwitchedConfigName,
       "ePDU2OutletSwitchedConfigPowerOnTime": ePDU2OutletSwitchedConfigPowerOnTime,
       "ePDU2OutletSwitchedConfigPowerOffTime": ePDU2OutletSwitchedConfigPowerOffTime,
       "ePDU2OutletSwitchedConfigRebootDuration": ePDU2OutletSwitchedConfigRebootDuration,
       "ePDU2OutletSwitchedInfoTable": ePDU2OutletSwitchedInfoTable,
       "ePDU2OutletSwitchedInfoEntry": ePDU2OutletSwitchedInfoEntry,
       "ePDU2OutletSwitchedInfoIndex": ePDU2OutletSwitchedInfoIndex,
       "ePDU2OutletSwitchedInfoModuleIndex": ePDU2OutletSwitchedInfoModuleIndex,
       "ePDU2OutletSwitchedInfoNumber": ePDU2OutletSwitchedInfoNumber,
       "ePDU2OutletSwitchedInfoName": ePDU2OutletSwitchedInfoName,
       "ePDU2OutletSwitchedInfoPhaseLayout": ePDU2OutletSwitchedInfoPhaseLayout,
       "ePDU2OutletSwitchedInfoBank": ePDU2OutletSwitchedInfoBank,
       "ePDU2OutletSwitchedStatusTable": ePDU2OutletSwitchedStatusTable,
       "ePDU2OutletSwitchedStatusEntry": ePDU2OutletSwitchedStatusEntry,
       "ePDU2OutletSwitchedStatusIndex": ePDU2OutletSwitchedStatusIndex,
       "ePDU2OutletSwitchedStatusModuleIndex": ePDU2OutletSwitchedStatusModuleIndex,
       "ePDU2OutletSwitchedStatusNumber": ePDU2OutletSwitchedStatusNumber,
       "ePDU2OutletSwitchedStatusName": ePDU2OutletSwitchedStatusName,
       "ePDU2OutletSwitchedStatusState": ePDU2OutletSwitchedStatusState,
       "ePDU2OutletSwitchedStatusCommandPending": ePDU2OutletSwitchedStatusCommandPending,
       "ePDU2OutletSwitchedControlTable": ePDU2OutletSwitchedControlTable,
       "ePDU2OutletSwitchedControlEntry": ePDU2OutletSwitchedControlEntry,
       "ePDU2OutletSwitchedControlIndex": ePDU2OutletSwitchedControlIndex,
       "ePDU2OutletSwitchedControlModuleIndex": ePDU2OutletSwitchedControlModuleIndex,
       "ePDU2OutletSwitchedControlNumber": ePDU2OutletSwitchedControlNumber,
       "ePDU2OutletSwitchedControlName": ePDU2OutletSwitchedControlName,
       "ePDU2OutletSwitchedControlCommand": ePDU2OutletSwitchedControlCommand,
       "ePDU2OutletMetered": ePDU2OutletMetered,
       "ePDU2OutletMeteredTableSize": ePDU2OutletMeteredTableSize,
       "ePDU2OutletMeteredConfigTable": ePDU2OutletMeteredConfigTable,
       "ePDU2OutletMeteredConfigEntry": ePDU2OutletMeteredConfigEntry,
       "ePDU2OutletMeteredConfigIndex": ePDU2OutletMeteredConfigIndex,
       "ePDU2OutletMeteredConfigModuleIndex": ePDU2OutletMeteredConfigModuleIndex,
       "ePDU2OutletMeteredConfigNumber": ePDU2OutletMeteredConfigNumber,
       "ePDU2OutletMeteredConfigName": ePDU2OutletMeteredConfigName,
       "ePDU2OutletMeteredConfigLowLoadThreshold": ePDU2OutletMeteredConfigLowLoadThreshold,
       "ePDU2OutletMeteredConfigNearOverloadThreshold": ePDU2OutletMeteredConfigNearOverloadThreshold,
       "ePDU2OutletMeteredConfigOverloadThreshold": ePDU2OutletMeteredConfigOverloadThreshold,
       "ePDU2OutletMeteredInfoTable": ePDU2OutletMeteredInfoTable,
       "ePDU2OutletMeteredInfoEntry": ePDU2OutletMeteredInfoEntry,
       "ePDU2OutletMeteredInfoIndex": ePDU2OutletMeteredInfoIndex,
       "ePDU2OutletMeteredInfoModuleIndex": ePDU2OutletMeteredInfoModuleIndex,
       "ePDU2OutletMeteredInfoNumber": ePDU2OutletMeteredInfoNumber,
       "ePDU2OutletMeteredInfoName": ePDU2OutletMeteredInfoName,
       "ePDU2OutletMeteredInfoLayout": ePDU2OutletMeteredInfoLayout,
       "ePDU2OutletMeteredInfoRating": ePDU2OutletMeteredInfoRating,
       "ePDU2OutletMeteredInfoBank": ePDU2OutletMeteredInfoBank,
       "ePDU2OutletMeteredStatusTable": ePDU2OutletMeteredStatusTable,
       "ePDU2OutletMeteredStatusEntry": ePDU2OutletMeteredStatusEntry,
       "ePDU2OutletMeteredStatusIndex": ePDU2OutletMeteredStatusIndex,
       "ePDU2OutletMeteredStatusModuleIndex": ePDU2OutletMeteredStatusModuleIndex,
       "ePDU2OutletMeteredStatusNumber": ePDU2OutletMeteredStatusNumber,
       "ePDU2OutletMeteredStatusName": ePDU2OutletMeteredStatusName,
       "ePDU2OutletMeteredStatusAlarm": ePDU2OutletMeteredStatusAlarm,
       "ePDU2OutletMeteredStatusLoad": ePDU2OutletMeteredStatusLoad,
       "ePDU2OutletMeteredStatusActivePower": ePDU2OutletMeteredStatusActivePower,
       "ePDU2OutletMeteredStatusPeakPower": ePDU2OutletMeteredStatusPeakPower,
       "ePDU2OutletMeteredStatusPeakPowerTimestamp": ePDU2OutletMeteredStatusPeakPowerTimestamp,
       "ePDU2OutletMeteredStatusPeakPowerStartTime": ePDU2OutletMeteredStatusPeakPowerStartTime,
       "ePDU2OutletMeteredStatusEnergy": ePDU2OutletMeteredStatusEnergy,
       "ePDU2OutletMeteredStatusEnergyStart": ePDU2OutletMeteredStatusEnergyStart,
       "ePDU2Sensor": ePDU2Sensor,
       "ePDU2SensorTableSize": ePDU2SensorTableSize,
       "ePDU2Group": ePDU2Group,
       "ePDU2GroupNumberOfDevices": ePDU2GroupNumberOfDevices,
       "ePDU2GroupTotalPower": ePDU2GroupTotalPower,
       "ePDU2GroupTotalEnergy": ePDU2GroupTotalEnergy,
       "ePDU2GroupEnergyReset": ePDU2GroupEnergyReset,
       "ePDU2GroupPeakRecordReset": ePDU2GroupPeakRecordReset,
       "battmgr": battmgr,
       "bmIdent": bmIdent,
       "bmIdentModelName": bmIdentModelName,
       "bmIdentHardwareRev": bmIdentHardwareRev,
       "bmIdentFirmwareRev": bmIdentFirmwareRev,
       "bmIdentLCDHardwareRev": bmIdentLCDHardwareRev,
       "bmIdentLCDFirmwareRev": bmIdentLCDFirmwareRev,
       "bmIdentDateOfManufacture": bmIdentDateOfManufacture,
       "bmIdentSerialNumber": bmIdentSerialNumber,
       "bmIdentName": bmIdentName,
       "bmIdentLocation": bmIdentLocation,
       "bmProperty": bmProperty,
       "bmPropertyStringMax": bmPropertyStringMax,
       "bmPropertyMaxProbeOnString": bmPropertyMaxProbeOnString,
       "bmPropertyInputVoltageRange": bmPropertyInputVoltageRange,
       "bmPropertyProbesRating": bmPropertyProbesRating,
       "bmConfig": bmConfig,
       "bmConfigBattAH": bmConfigBattAH,
       "bmConfigStringCount": bmConfigStringCount,
       "bmConfigProbesCountOnString": bmConfigProbesCountOnString,
       "bmConfigLowVoltAlarmThreshold": bmConfigLowVoltAlarmThreshold,
       "bmConfigHighVoltAlarmThreshold": bmConfigHighVoltAlarmThreshold,
       "bmConfigVoltDiffAlarmThreshold": bmConfigVoltDiffAlarmThreshold,
       "bmConfigLowTempAlarmThreshold": bmConfigLowTempAlarmThreshold,
       "bmConfigHighTempAlarmThreshold": bmConfigHighTempAlarmThreshold,
       "bmConfigLowResAlarmThreshold": bmConfigLowResAlarmThreshold,
       "bmConfigHighResAlarmThreshold": bmConfigHighResAlarmThreshold,
       "bmConfigLowResWarnThreshold": bmConfigLowResWarnThreshold,
       "bmConfigHighResWarnThreshold": bmConfigHighResWarnThreshold,
       "bmConfigResHealthAlarmThreshold": bmConfigResHealthAlarmThreshold,
       "bmConfigResHealthWarnThreshold": bmConfigResHealthWarnThreshold,
       "bmConfigLowVoltAlarmThreshold10mV": bmConfigLowVoltAlarmThreshold10mV,
       "bmConfigHighVoltAlarmThreshold10mV": bmConfigHighVoltAlarmThreshold10mV,
       "bmConfigMergeFeature": bmConfigMergeFeature,
       "bmControl": bmControl,
       "bmControlSysytemIdenticator": bmControlSysytemIdenticator,
       "bmControlProbeIndicator": bmControlProbeIndicator,
       "bmProbes": bmProbes,
       "bmProbesNum": bmProbesNum,
       "bmProbesTableSize": bmProbesTableSize,
       "bmProbesTable": bmProbesTable,
       "bmProbesEntry": bmProbesEntry,
       "bmProbesIndex": bmProbesIndex,
       "bmProbesPackIndex": bmProbesPackIndex,
       "bmProbesStringIndex": bmProbesStringIndex,
       "bmProbesBattIndex": bmProbesBattIndex,
       "bmProbesVoltageTableSize": bmProbesVoltageTableSize,
       "bmProbesVoltageTable": bmProbesVoltageTable,
       "bmProbesVoltageEntry": bmProbesVoltageEntry,
       "bmProbesVoltageIndex": bmProbesVoltageIndex,
       "bmProbesVoltagePackIndex": bmProbesVoltagePackIndex,
       "bmProbesVoltageStringIndex": bmProbesVoltageStringIndex,
       "bmProbesVoltageBattIndex": bmProbesVoltageBattIndex,
       "bmProbesVoltageProbeIndex": bmProbesVoltageProbeIndex,
       "bmProbesVoltageAlarmStatus": bmProbesVoltageAlarmStatus,
       "bmProbesVoltage": bmProbesVoltage,
       "bmProbesVoltageEqualPercentage": bmProbesVoltageEqualPercentage,
       "bmProbesTempTableSize": bmProbesTempTableSize,
       "bmProbesTempTable": bmProbesTempTable,
       "bmProbesTempEntry": bmProbesTempEntry,
       "bmProbesTempIndex": bmProbesTempIndex,
       "bmProbesTempPackIndex": bmProbesTempPackIndex,
       "bmProbesTempStringIndex": bmProbesTempStringIndex,
       "bmProbesTempBattIndex": bmProbesTempBattIndex,
       "bmProbesTempProbeIndex": bmProbesTempProbeIndex,
       "bmProbesTempAlarmStatus": bmProbesTempAlarmStatus,
       "bmProbesTemperature": bmProbesTemperature,
       "bmProbesResTableSize": bmProbesResTableSize,
       "bmProbesResTable": bmProbesResTable,
       "bmProbesResEntry": bmProbesResEntry,
       "bmProbesResIndex": bmProbesResIndex,
       "bmProbesResPackIndex": bmProbesResPackIndex,
       "bmProbesResStringIndex": bmProbesResStringIndex,
       "bmProbesResBattIndex": bmProbesResBattIndex,
       "bmProbesResProbeIndex": bmProbesResProbeIndex,
       "bmProbesResAlarmStatus": bmProbesResAlarmStatus,
       "bmProbesResistance": bmProbesResistance,
       "bmProbesResHealth": bmProbesResHealth,
       "bmFuncRes": bmFuncRes,
       "bmFuncResMeasure": bmFuncResMeasure,
       "bmFuncResMeasureInterval": bmFuncResMeasureInterval,
       "bmFuncResMeasureManualCmd": bmFuncResMeasureManualCmd,
       "bmFuncResMeasureManualResult": bmFuncResMeasureManualResult,
       "bmFuncResMeasureLastUpdate": bmFuncResMeasureLastUpdate,
       "bmFuncEqual": bmFuncEqual,
       "bmFuncEqualEnable": bmFuncEqualEnable,
       "bmFuncEqualActiveCond": bmFuncEqualActiveCond,
       "bmFuncEqualStatus": bmFuncEqualStatus,
       "bmFuncEqualStartTime": bmFuncEqualStartTime,
       "bmFuncEqualElapseTime": bmFuncEqualElapseTime,
       "cpsmgmt": cpsmgmt,
       "mconfig": mconfig,
       "mconfigNumTrapAccepters": mconfigNumTrapAccepters,
       "mconfigTrapAccepterTable": mconfigTrapAccepterTable,
       "mconfigTrapAccepterEntry": mconfigTrapAccepterEntry,
       "trapIndex": trapIndex,
       "accepterAddr": accepterAddr,
       "communityString": communityString,
       "severityDegree": severityDegree,
       "accepterActive": accepterActive,
       "mconfigDHCPEnabled": mconfigDHCPEnabled,
       "mconfigMyAddr": mconfigMyAddr,
       "mconfigClock": mconfigClock,
       "mconfigClockDate": mconfigClockDate,
       "mconfigClockTime": mconfigClockTime,
       "mtrapinfo": mtrapinfo,
       "mtrapinfoInteger": mtrapinfoInteger,
       "mtrapinfoIpAddress": mtrapinfoIpAddress,
       "mtrapinfoString": mtrapinfoString,
       "mtrapinfoGauge": mtrapinfoGauge,
       "mtrapinfoTimeTicks": mtrapinfoTimeTicks,
       "mtrapinfoBmEventId": mtrapinfoBmEventId,
       "mcontrol": mcontrol,
       "mcontrolRestart": mcontrolRestart,
       "mcontrolReset": mcontrolReset}
)
