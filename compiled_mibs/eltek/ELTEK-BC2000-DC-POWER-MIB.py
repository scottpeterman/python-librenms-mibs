# SNMP MIB module (ELTEK-BC2000-DC-POWER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\eltek\ELTEK-BC2000-DC-POWER-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:39:14 2025
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

(AutonomousType,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

eltek = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13858)
)
if mibBuilder.loadTexts:
    eltek.setRevisions(
        ("2014-03-27 10:38",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PositiveInteger(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class NonNegativeInteger(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class GenericEnableDisableTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )



class SysInputValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-127,
              -126,
              -125,
              -124,
              -123,
              -122,
              -121,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", -127),
          ("removed", -126),
          ("shorted", -125),
          ("auxAlarm", -124),
          ("auxNormal", -123),
          ("distAlarm", -122),
          ("distNormal", -121),
          ("undefined", 255))
    )



class VpwrPMCnfgValue(TextualConvention, Integer32):
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("tProbe", 1),
          ("auxNO", 2),
          ("auxNC", 3),
          ("distNO", 4),
          ("distNC", 5),
          ("undefined", 255))
    )



class BDTStartSourceTC(TextualConvention, Integer32):
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("bdtInactive", 0),
          ("bdtManualStart", 1),
          ("bdtSched01Start1", 2),
          ("bdtSched02Start2", 3),
          ("bdtSched03Start3", 4),
          ("bdtSched04Start4", 5),
          ("bdtSched05Start5", 6),
          ("bdtSched06Start6", 7),
          ("bdtSched07Start7", 8),
          ("bdtSched08Start8", 9),
          ("bdtSched09Start9", 10),
          ("bdtSched10Start10", 11),
          ("bdtSched11Start11", 12),
          ("bdtSched12Start12", 13),
          ("bdtACFailStart", 14))
    )



class BDTResultTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("bdtResultCleared", 0),
          ("bdtResultPassed", 1),
          ("bdtResultFailed", 2),
          ("bdtResultStopped", 3),
          ("bdtResultAborted", 4),
          ("bdtResultInProgress", 5))
    )



# MIB Managed Objects in the order of their OIDs

_VpwrDcPowerSystem_ObjectIdentity = ObjectIdentity
vpwrDcPowerSystem = _VpwrDcPowerSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 2)
)
_VpwrSystemIdentGroup_ObjectIdentity = ObjectIdentity
vpwrSystemIdentGroup = _VpwrSystemIdentGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 2, 1)
)


class _VpwrIdentManufacturer_Type(DisplayString):
    """Custom type vpwrIdentManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_VpwrIdentManufacturer_Type.__name__ = "DisplayString"
_VpwrIdentManufacturer_Object = MibScalar
vpwrIdentManufacturer = _VpwrIdentManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 1, 1),
    _VpwrIdentManufacturer_Type()
)
vpwrIdentManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrIdentManufacturer.setStatus("current")


class _VpwrIdentModel_Type(DisplayString):
    """Custom type vpwrIdentModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_VpwrIdentModel_Type.__name__ = "DisplayString"
_VpwrIdentModel_Object = MibScalar
vpwrIdentModel = _VpwrIdentModel_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 1, 2),
    _VpwrIdentModel_Type()
)
vpwrIdentModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrIdentModel.setStatus("current")


class _VpwrIdentControllerVersion_Type(DisplayString):
    """Custom type vpwrIdentControllerVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_VpwrIdentControllerVersion_Type.__name__ = "DisplayString"
_VpwrIdentControllerVersion_Object = MibScalar
vpwrIdentControllerVersion = _VpwrIdentControllerVersion_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 1, 3),
    _VpwrIdentControllerVersion_Type()
)
vpwrIdentControllerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrIdentControllerVersion.setStatus("current")


class _VpwrIdentAgentSoftwareVersion_Type(DisplayString):
    """Custom type vpwrIdentAgentSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_VpwrIdentAgentSoftwareVersion_Type.__name__ = "DisplayString"
_VpwrIdentAgentSoftwareVersion_Object = MibScalar
vpwrIdentAgentSoftwareVersion = _VpwrIdentAgentSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 1, 4),
    _VpwrIdentAgentSoftwareVersion_Type()
)
vpwrIdentAgentSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrIdentAgentSoftwareVersion.setStatus("current")


class _VpwrIdentName_Type(DisplayString):
    """Custom type vpwrIdentName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_VpwrIdentName_Type.__name__ = "DisplayString"
_VpwrIdentName_Object = MibScalar
vpwrIdentName = _VpwrIdentName_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 1, 5),
    _VpwrIdentName_Type()
)
vpwrIdentName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrIdentName.setStatus("current")
_VpwrSystemIdentTable_Object = MibTable
vpwrSystemIdentTable = _VpwrSystemIdentTable_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 1, 6)
)
if mibBuilder.loadTexts:
    vpwrSystemIdentTable.setStatus("current")
_VpwrSystemIdentEntry_Object = MibTableRow
vpwrSystemIdentEntry = _VpwrSystemIdentEntry_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 1, 6, 1)
)
vpwrSystemIdentEntry.setIndexNames(
    (0, "ELTEK-BC2000-DC-POWER-MIB", "vpwrBayIndex"),
    (0, "ELTEK-BC2000-DC-POWER-MIB", "vpwrModuleIndex"),
)
if mibBuilder.loadTexts:
    vpwrSystemIdentEntry.setStatus("current")
_VpwrBayIndex_Type = PositiveInteger
_VpwrBayIndex_Object = MibTableColumn
vpwrBayIndex = _VpwrBayIndex_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 1, 6, 1, 1),
    _VpwrBayIndex_Type()
)
vpwrBayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrBayIndex.setStatus("current")
_VpwrModuleIndex_Type = PositiveInteger
_VpwrModuleIndex_Object = MibTableColumn
vpwrModuleIndex = _VpwrModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 1, 6, 1, 2),
    _VpwrModuleIndex_Type()
)
vpwrModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrModuleIndex.setStatus("current")
_VpwrModuleOID_Type = ObjectIdentifier
_VpwrModuleOID_Object = MibTableColumn
vpwrModuleOID = _VpwrModuleOID_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 1, 6, 1, 3),
    _VpwrModuleOID_Type()
)
vpwrModuleOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrModuleOID.setStatus("current")
_VpwrModuleCurrent_Type = Integer32
_VpwrModuleCurrent_Object = MibTableColumn
vpwrModuleCurrent = _VpwrModuleCurrent_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 1, 6, 1, 4),
    _VpwrModuleCurrent_Type()
)
vpwrModuleCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrModuleCurrent.setStatus("current")


class _VpwrModuleOperStatus_Type(Integer32):
    """Custom type vpwrModuleOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("moduleStatusOK", 0),
          ("moduleStatusAlarm", 1),
          ("moduleStatusDisabled", 2),
          ("moduleStatusRingerAOn", 3),
          ("moduleStatusRingerBOn", 4),
          ("moduleStatusUnknown", 5))
    )


_VpwrModuleOperStatus_Type.__name__ = "Integer32"
_VpwrModuleOperStatus_Object = MibTableColumn
vpwrModuleOperStatus = _VpwrModuleOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 1, 6, 1, 5),
    _VpwrModuleOperStatus_Type()
)
vpwrModuleOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrModuleOperStatus.setStatus("current")
_VpwrModuleCapacity_Type = Integer32
_VpwrModuleCapacity_Object = MibTableColumn
vpwrModuleCapacity = _VpwrModuleCapacity_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 1, 6, 1, 6),
    _VpwrModuleCapacity_Type()
)
vpwrModuleCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrModuleCapacity.setStatus("current")
_VpwrSystemConfigGroup_ObjectIdentity = ObjectIdentity
vpwrSystemConfigGroup = _VpwrSystemConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 2, 2)
)


class _VpwrSystemTempCompensation_Type(Integer32):
    """Custom type vpwrSystemTempCompensation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("tempCompDisabled", 0),
          ("tempCompEnabled", 1))
    )


_VpwrSystemTempCompensation_Type.__name__ = "Integer32"
_VpwrSystemTempCompensation_Object = MibScalar
vpwrSystemTempCompensation = _VpwrSystemTempCompensation_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 2, 1),
    _VpwrSystemTempCompensation_Type()
)
vpwrSystemTempCompensation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrSystemTempCompensation.setStatus("current")


class _VpwrSystemTempCompStartTemperature_Type(Integer32):
    """Custom type vpwrSystemTempCompStartTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25, 60),
    )


_VpwrSystemTempCompStartTemperature_Type.__name__ = "Integer32"
_VpwrSystemTempCompStartTemperature_Object = MibScalar
vpwrSystemTempCompStartTemperature = _VpwrSystemTempCompStartTemperature_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 2, 2),
    _VpwrSystemTempCompStartTemperature_Type()
)
vpwrSystemTempCompStartTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrSystemTempCompStartTemperature.setStatus("current")
if mibBuilder.loadTexts:
    vpwrSystemTempCompStartTemperature.setUnits("degrees Centigrade")
_VpwrSystemTempCompStopVoltage_Type = Integer32
_VpwrSystemTempCompStopVoltage_Object = MibScalar
vpwrSystemTempCompStopVoltage = _VpwrSystemTempCompStopVoltage_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 2, 3),
    _VpwrSystemTempCompStopVoltage_Type()
)
vpwrSystemTempCompStopVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrSystemTempCompStopVoltage.setStatus("current")
if mibBuilder.loadTexts:
    vpwrSystemTempCompStopVoltage.setUnits(" *.01 Volts")


class _VpwrSystemTempCompensationSlope_Type(Integer32):
    """Custom type vpwrSystemTempCompensationSlope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 250),
    )


_VpwrSystemTempCompensationSlope_Type.__name__ = "Integer32"
_VpwrSystemTempCompensationSlope_Object = MibScalar
vpwrSystemTempCompensationSlope = _VpwrSystemTempCompensationSlope_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 2, 4),
    _VpwrSystemTempCompensationSlope_Type()
)
vpwrSystemTempCompensationSlope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrSystemTempCompensationSlope.setStatus("current")
if mibBuilder.loadTexts:
    vpwrSystemTempCompensationSlope.setUnits(" milli-Volts per degrees Centigrade")


class _VpwrSystemThermalSenseType_Type(Integer32):
    """Custom type vpwrSystemThermalSenseType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("internal", 0),
          ("external", 1))
    )


_VpwrSystemThermalSenseType_Type.__name__ = "Integer32"
_VpwrSystemThermalSenseType_Object = MibScalar
vpwrSystemThermalSenseType = _VpwrSystemThermalSenseType_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 2, 5),
    _VpwrSystemThermalSenseType_Type()
)
vpwrSystemThermalSenseType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrSystemThermalSenseType.setStatus("current")
_VpwrSystemHVAlarmSetpoint_Type = Integer32
_VpwrSystemHVAlarmSetpoint_Object = MibScalar
vpwrSystemHVAlarmSetpoint = _VpwrSystemHVAlarmSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 2, 6),
    _VpwrSystemHVAlarmSetpoint_Type()
)
vpwrSystemHVAlarmSetpoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrSystemHVAlarmSetpoint.setStatus("current")
if mibBuilder.loadTexts:
    vpwrSystemHVAlarmSetpoint.setUnits(" *.01 Volts")
_VpwrSystemBDAlarmSetpoint_Type = Integer32
_VpwrSystemBDAlarmSetpoint_Object = MibScalar
vpwrSystemBDAlarmSetpoint = _VpwrSystemBDAlarmSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 2, 7),
    _VpwrSystemBDAlarmSetpoint_Type()
)
vpwrSystemBDAlarmSetpoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrSystemBDAlarmSetpoint.setStatus("current")
if mibBuilder.loadTexts:
    vpwrSystemBDAlarmSetpoint.setUnits(" *.01 Volts")
_VpwrSystemInternalTempLThreshold_Type = Integer32
_VpwrSystemInternalTempLThreshold_Object = MibScalar
vpwrSystemInternalTempLThreshold = _VpwrSystemInternalTempLThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 2, 8),
    _VpwrSystemInternalTempLThreshold_Type()
)
vpwrSystemInternalTempLThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrSystemInternalTempLThreshold.setStatus("current")
if mibBuilder.loadTexts:
    vpwrSystemInternalTempLThreshold.setUnits("degrees Centigrade")
_VpwrSystemInternalTempUThreshold_Type = Integer32
_VpwrSystemInternalTempUThreshold_Object = MibScalar
vpwrSystemInternalTempUThreshold = _VpwrSystemInternalTempUThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 2, 9),
    _VpwrSystemInternalTempUThreshold_Type()
)
vpwrSystemInternalTempUThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrSystemInternalTempUThreshold.setStatus("current")
if mibBuilder.loadTexts:
    vpwrSystemInternalTempUThreshold.setUnits("degrees Centigrade")
_VpwrSystemParameterGroup_ObjectIdentity = ObjectIdentity
vpwrSystemParameterGroup = _VpwrSystemParameterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 2, 3)
)


class _VpwrSystemShelfCapacity_Type(Integer32):
    """Custom type vpwrSystemShelfCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_VpwrSystemShelfCapacity_Type.__name__ = "Integer32"
_VpwrSystemShelfCapacity_Object = MibScalar
vpwrSystemShelfCapacity = _VpwrSystemShelfCapacity_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 3, 1),
    _VpwrSystemShelfCapacity_Type()
)
vpwrSystemShelfCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrSystemShelfCapacity.setStatus("current")
_VpwrSystemVoltage_Type = Integer32
_VpwrSystemVoltage_Object = MibScalar
vpwrSystemVoltage = _VpwrSystemVoltage_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 3, 2),
    _VpwrSystemVoltage_Type()
)
vpwrSystemVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrSystemVoltage.setStatus("current")
if mibBuilder.loadTexts:
    vpwrSystemVoltage.setUnits(" *.01 Volts")
_VpwrSystemCurrent_Type = Integer32
_VpwrSystemCurrent_Object = MibScalar
vpwrSystemCurrent = _VpwrSystemCurrent_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 3, 3),
    _VpwrSystemCurrent_Type()
)
vpwrSystemCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrSystemCurrent.setStatus("current")
if mibBuilder.loadTexts:
    vpwrSystemCurrent.setUnits(" Amperes")


class _VpwrSystemControllerState_Type(Integer32):
    """Custom type vpwrSystemControllerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("systemControllerStateUnknown", 0),
          ("systemControllerStateNormal", 1),
          ("systemControllerStateChange", 2),
          ("systemControllerStateAlarm", 3),
          ("systemControllerStateMenu", 4),
          ("systemControllerStateIrActive", 5))
    )


_VpwrSystemControllerState_Type.__name__ = "Integer32"
_VpwrSystemControllerState_Object = MibScalar
vpwrSystemControllerState = _VpwrSystemControllerState_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 3, 4),
    _VpwrSystemControllerState_Type()
)
vpwrSystemControllerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrSystemControllerState.setStatus("current")
_VpwrSystemInternalTemperature_Type = Integer32
_VpwrSystemInternalTemperature_Object = MibScalar
vpwrSystemInternalTemperature = _VpwrSystemInternalTemperature_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 3, 5),
    _VpwrSystemInternalTemperature_Type()
)
vpwrSystemInternalTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrSystemInternalTemperature.setStatus("current")
if mibBuilder.loadTexts:
    vpwrSystemInternalTemperature.setUnits("degrees Centigrade")


class _VpwrSystemTempCompensationState_Type(Integer32):
    """Custom type vpwrSystemTempCompensationState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("systemTempCompInactive", 0),
          ("systemTempCompActive", 1))
    )


_VpwrSystemTempCompensationState_Type.__name__ = "Integer32"
_VpwrSystemTempCompensationState_Object = MibScalar
vpwrSystemTempCompensationState = _VpwrSystemTempCompensationState_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 3, 6),
    _VpwrSystemTempCompensationState_Type()
)
vpwrSystemTempCompensationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrSystemTempCompensationState.setStatus("current")


class _VpwrSystemType_Type(Integer32):
    """Custom type vpwrSystemType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sysType48V", 0),
          ("sysType24V", 1),
          ("sysType12V", 2))
    )


_VpwrSystemType_Type.__name__ = "Integer32"
_VpwrSystemType_Object = MibScalar
vpwrSystemType = _VpwrSystemType_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 3, 7),
    _VpwrSystemType_Type()
)
vpwrSystemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrSystemType.setStatus("current")
_VpwrSystemCumulativeUpTime_Type = Gauge32
_VpwrSystemCumulativeUpTime_Object = MibScalar
vpwrSystemCumulativeUpTime = _VpwrSystemCumulativeUpTime_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 3, 8),
    _VpwrSystemCumulativeUpTime_Type()
)
vpwrSystemCumulativeUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrSystemCumulativeUpTime.setStatus("current")
_VpwrSystemBatteryRemainingTime_Type = PositiveInteger
_VpwrSystemBatteryRemainingTime_Object = MibScalar
vpwrSystemBatteryRemainingTime = _VpwrSystemBatteryRemainingTime_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 3, 9),
    _VpwrSystemBatteryRemainingTime_Type()
)
vpwrSystemBatteryRemainingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrSystemBatteryRemainingTime.setStatus("current")
if mibBuilder.loadTexts:
    vpwrSystemBatteryRemainingTime.setUnits("Hours")
_VpwrSystemPanelIdentGroup_ObjectIdentity = ObjectIdentity
vpwrSystemPanelIdentGroup = _VpwrSystemPanelIdentGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 2, 4)
)
_VpwrPanelStatusTable_Object = MibTable
vpwrPanelStatusTable = _VpwrPanelStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 4, 1)
)
if mibBuilder.loadTexts:
    vpwrPanelStatusTable.setStatus("current")
_VpwrPanelStatus_Object = MibTableRow
vpwrPanelStatus = _VpwrPanelStatus_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 4, 1, 1)
)
vpwrPanelStatus.setIndexNames(
    (0, "ELTEK-BC2000-DC-POWER-MIB", "vpwrPanelStatusIndex"),
    (0, "ELTEK-BC2000-DC-POWER-MIB", "vpwrPanelStatusModuleIndex"),
)
if mibBuilder.loadTexts:
    vpwrPanelStatus.setStatus("current")
_VpwrPanelStatusIndex_Type = PositiveInteger
_VpwrPanelStatusIndex_Object = MibTableColumn
vpwrPanelStatusIndex = _VpwrPanelStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 4, 1, 1, 1),
    _VpwrPanelStatusIndex_Type()
)
vpwrPanelStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrPanelStatusIndex.setStatus("current")
_VpwrPanelStatusModuleIndex_Type = PositiveInteger
_VpwrPanelStatusModuleIndex_Object = MibTableColumn
vpwrPanelStatusModuleIndex = _VpwrPanelStatusModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 4, 1, 1, 2),
    _VpwrPanelStatusModuleIndex_Type()
)
vpwrPanelStatusModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrPanelStatusModuleIndex.setStatus("current")
_VpwrPanelStatusModuleOID_Type = ObjectIdentifier
_VpwrPanelStatusModuleOID_Object = MibTableColumn
vpwrPanelStatusModuleOID = _VpwrPanelStatusModuleOID_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 4, 1, 1, 3),
    _VpwrPanelStatusModuleOID_Type()
)
vpwrPanelStatusModuleOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrPanelStatusModuleOID.setStatus("current")
_VpwrPanelStatusModuleCurrent_Type = Integer32
_VpwrPanelStatusModuleCurrent_Object = MibTableColumn
vpwrPanelStatusModuleCurrent = _VpwrPanelStatusModuleCurrent_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 4, 1, 1, 4),
    _VpwrPanelStatusModuleCurrent_Type()
)
vpwrPanelStatusModuleCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrPanelStatusModuleCurrent.setStatus("current")


class _VpwrpanelStatusModuleOperStatus_Type(Integer32):
    """Custom type vpwrpanelStatusModuleOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("moduleStatusOK", 0),
          ("moduleStatusAlarm", 1),
          ("moduleStatusDisabled", 2),
          ("moduleStatusRingerAOn", 3),
          ("moduleStatusRingerBOn", 4),
          ("moduleStatusUnknown", 5))
    )


_VpwrpanelStatusModuleOperStatus_Type.__name__ = "Integer32"
_VpwrpanelStatusModuleOperStatus_Object = MibTableColumn
vpwrpanelStatusModuleOperStatus = _VpwrpanelStatusModuleOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 4, 1, 1, 5),
    _VpwrpanelStatusModuleOperStatus_Type()
)
vpwrpanelStatusModuleOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrpanelStatusModuleOperStatus.setStatus("current")
_VpwrPanelStatusModuleCapacity_Type = Integer32
_VpwrPanelStatusModuleCapacity_Object = MibTableColumn
vpwrPanelStatusModuleCapacity = _VpwrPanelStatusModuleCapacity_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 4, 1, 1, 6),
    _VpwrPanelStatusModuleCapacity_Type()
)
vpwrPanelStatusModuleCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrPanelStatusModuleCapacity.setStatus("current")
_VpwrPanelIdentTable_Object = MibTable
vpwrPanelIdentTable = _VpwrPanelIdentTable_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 4, 2)
)
if mibBuilder.loadTexts:
    vpwrPanelIdentTable.setStatus("current")
_VpwrPanelIdentEntry_Object = MibTableRow
vpwrPanelIdentEntry = _VpwrPanelIdentEntry_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 4, 2, 1)
)
vpwrPanelIdentEntry.setIndexNames(
    (0, "ELTEK-BC2000-DC-POWER-MIB", "vpwrPanelIndex"),
    (0, "ELTEK-BC2000-DC-POWER-MIB", "vpwrPanelModuleIndex"),
)
if mibBuilder.loadTexts:
    vpwrPanelIdentEntry.setStatus("current")
_VpwrPanelIndex_Type = PositiveInteger
_VpwrPanelIndex_Object = MibTableColumn
vpwrPanelIndex = _VpwrPanelIndex_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 4, 2, 1, 1),
    _VpwrPanelIndex_Type()
)
vpwrPanelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrPanelIndex.setStatus("current")
_VpwrPanelModuleIndex_Type = PositiveInteger
_VpwrPanelModuleIndex_Object = MibTableColumn
vpwrPanelModuleIndex = _VpwrPanelModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 4, 2, 1, 2),
    _VpwrPanelModuleIndex_Type()
)
vpwrPanelModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrPanelModuleIndex.setStatus("current")
_VpwrPanelModuleSerNum_Type = ObjectIdentifier
_VpwrPanelModuleSerNum_Object = MibTableColumn
vpwrPanelModuleSerNum = _VpwrPanelModuleSerNum_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 4, 2, 1, 3),
    _VpwrPanelModuleSerNum_Type()
)
vpwrPanelModuleSerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrPanelModuleSerNum.setStatus("current")
_VpwrPanelModuleModelName_Type = ObjectIdentifier
_VpwrPanelModuleModelName_Object = MibTableColumn
vpwrPanelModuleModelName = _VpwrPanelModuleModelName_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 4, 2, 1, 4),
    _VpwrPanelModuleModelName_Type()
)
vpwrPanelModuleModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrPanelModuleModelName.setStatus("current")
_VpwrPanelModuleFWVer_Type = ObjectIdentifier
_VpwrPanelModuleFWVer_Object = MibTableColumn
vpwrPanelModuleFWVer = _VpwrPanelModuleFWVer_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 4, 2, 1, 5),
    _VpwrPanelModuleFWVer_Type()
)
vpwrPanelModuleFWVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrPanelModuleFWVer.setStatus("current")
_VpwrPanelModuleTestDate_Type = Integer32
_VpwrPanelModuleTestDate_Object = MibTableColumn
vpwrPanelModuleTestDate = _VpwrPanelModuleTestDate_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 4, 2, 1, 6),
    _VpwrPanelModuleTestDate_Type()
)
vpwrPanelModuleTestDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrPanelModuleTestDate.setStatus("current")
_VpwrSystemHistoryGroup_ObjectIdentity = ObjectIdentity
vpwrSystemHistoryGroup = _VpwrSystemHistoryGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 2, 5)
)
_VpwrSysHistAlarmTable_Object = MibTable
vpwrSysHistAlarmTable = _VpwrSysHistAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 5, 1)
)
if mibBuilder.loadTexts:
    vpwrSysHistAlarmTable.setStatus("current")
_VpwrSysHistAlarmEntry_Object = MibTableRow
vpwrSysHistAlarmEntry = _VpwrSysHistAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 5, 1, 1)
)
vpwrSysHistAlarmEntry.setIndexNames(
    (0, "ELTEK-BC2000-DC-POWER-MIB", "vpwrSysHistAlarmIndex"),
)
if mibBuilder.loadTexts:
    vpwrSysHistAlarmEntry.setStatus("current")
_VpwrSysHistAlarmIndex_Type = PositiveInteger
_VpwrSysHistAlarmIndex_Object = MibTableColumn
vpwrSysHistAlarmIndex = _VpwrSysHistAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 5, 1, 1, 1),
    _VpwrSysHistAlarmIndex_Type()
)
vpwrSysHistAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrSysHistAlarmIndex.setStatus("current")
_VpwrSysHistAlarmDescription_Type = DisplayString
_VpwrSysHistAlarmDescription_Object = MibTableColumn
vpwrSysHistAlarmDescription = _VpwrSysHistAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 5, 1, 1, 2),
    _VpwrSysHistAlarmDescription_Type()
)
vpwrSysHistAlarmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrSysHistAlarmDescription.setStatus("current")
_VpwrSystemAlarmGroup_ObjectIdentity = ObjectIdentity
vpwrSystemAlarmGroup = _VpwrSystemAlarmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 2, 6)
)
_VpwrSystemAlarmMajor_Type = Integer32
_VpwrSystemAlarmMajor_Object = MibScalar
vpwrSystemAlarmMajor = _VpwrSystemAlarmMajor_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 6, 1),
    _VpwrSystemAlarmMajor_Type()
)
vpwrSystemAlarmMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrSystemAlarmMajor.setStatus("current")
_VpwrSystemAlarmMinor_Type = Integer32
_VpwrSystemAlarmMinor_Object = MibScalar
vpwrSystemAlarmMinor = _VpwrSystemAlarmMinor_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 6, 2),
    _VpwrSystemAlarmMinor_Type()
)
vpwrSystemAlarmMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrSystemAlarmMinor.setStatus("current")
_VpwrSystemACFailAlarm_Type = Integer32
_VpwrSystemACFailAlarm_Object = MibScalar
vpwrSystemACFailAlarm = _VpwrSystemACFailAlarm_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 6, 3),
    _VpwrSystemACFailAlarm_Type()
)
vpwrSystemACFailAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrSystemACFailAlarm.setStatus("current")
_VpwrSystemHighVoltageWarningAlarm_Type = Integer32
_VpwrSystemHighVoltageWarningAlarm_Object = MibScalar
vpwrSystemHighVoltageWarningAlarm = _VpwrSystemHighVoltageWarningAlarm_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 6, 4),
    _VpwrSystemHighVoltageWarningAlarm_Type()
)
vpwrSystemHighVoltageWarningAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrSystemHighVoltageWarningAlarm.setStatus("current")
_VpwrSystemHighVoltageShutdownAlarm_Type = Integer32
_VpwrSystemHighVoltageShutdownAlarm_Object = MibScalar
vpwrSystemHighVoltageShutdownAlarm = _VpwrSystemHighVoltageShutdownAlarm_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 6, 5),
    _VpwrSystemHighVoltageShutdownAlarm_Type()
)
vpwrSystemHighVoltageShutdownAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrSystemHighVoltageShutdownAlarm.setStatus("current")


class _VpwrSystemBatteryonDischargeAlarm_Type(Integer32):
    """Custom type vpwrSystemBatteryonDischargeAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("systemTempCompInactive", 0),
          ("systemTempCompActive", 1))
    )


_VpwrSystemBatteryonDischargeAlarm_Type.__name__ = "Integer32"
_VpwrSystemBatteryonDischargeAlarm_Object = MibScalar
vpwrSystemBatteryonDischargeAlarm = _VpwrSystemBatteryonDischargeAlarm_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 6, 6),
    _VpwrSystemBatteryonDischargeAlarm_Type()
)
vpwrSystemBatteryonDischargeAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrSystemBatteryonDischargeAlarm.setStatus("current")


class _VpwrSystemLowVoltageWarningAlarm_Type(Integer32):
    """Custom type vpwrSystemLowVoltageWarningAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sysType48V", 0),
          ("sysType24V", 1),
          ("sysType12V", 2))
    )


_VpwrSystemLowVoltageWarningAlarm_Type.__name__ = "Integer32"
_VpwrSystemLowVoltageWarningAlarm_Object = MibScalar
vpwrSystemLowVoltageWarningAlarm = _VpwrSystemLowVoltageWarningAlarm_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 6, 7),
    _VpwrSystemLowVoltageWarningAlarm_Type()
)
vpwrSystemLowVoltageWarningAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrSystemLowVoltageWarningAlarm.setStatus("current")
_VpwrSystemLVDOpenAlarm_Type = Gauge32
_VpwrSystemLVDOpenAlarm_Object = MibScalar
vpwrSystemLVDOpenAlarm = _VpwrSystemLVDOpenAlarm_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 6, 8),
    _VpwrSystemLVDOpenAlarm_Type()
)
vpwrSystemLVDOpenAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrSystemLVDOpenAlarm.setStatus("current")
_VpwrSystemDistributionAlarm_Type = PositiveInteger
_VpwrSystemDistributionAlarm_Object = MibScalar
vpwrSystemDistributionAlarm = _VpwrSystemDistributionAlarm_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 6, 9),
    _VpwrSystemDistributionAlarm_Type()
)
vpwrSystemDistributionAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrSystemDistributionAlarm.setStatus("current")
_VpwrSystemAuxiliaryAlarm_Type = PositiveInteger
_VpwrSystemAuxiliaryAlarm_Object = MibScalar
vpwrSystemAuxiliaryAlarm = _VpwrSystemAuxiliaryAlarm_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 6, 10),
    _VpwrSystemAuxiliaryAlarm_Type()
)
vpwrSystemAuxiliaryAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrSystemAuxiliaryAlarm.setStatus("current")
_VpwrSystemRedundantCapAlarm_Type = PositiveInteger
_VpwrSystemRedundantCapAlarm_Object = MibScalar
vpwrSystemRedundantCapAlarm = _VpwrSystemRedundantCapAlarm_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 6, 11),
    _VpwrSystemRedundantCapAlarm_Type()
)
vpwrSystemRedundantCapAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrSystemRedundantCapAlarm.setStatus("current")
_VpwrSystemRectIShareAlarm_Type = PositiveInteger
_VpwrSystemRectIShareAlarm_Object = MibScalar
vpwrSystemRectIShareAlarm = _VpwrSystemRectIShareAlarm_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 6, 12),
    _VpwrSystemRectIShareAlarm_Type()
)
vpwrSystemRectIShareAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrSystemRectIShareAlarm.setStatus("current")
_VpwrSystemSnglRectAlarm_Type = PositiveInteger
_VpwrSystemSnglRectAlarm_Object = MibScalar
vpwrSystemSnglRectAlarm = _VpwrSystemSnglRectAlarm_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 6, 13),
    _VpwrSystemSnglRectAlarm_Type()
)
vpwrSystemSnglRectAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrSystemSnglRectAlarm.setStatus("current")
_VpwrSystemMultRectAlarm_Type = PositiveInteger
_VpwrSystemMultRectAlarm_Object = MibScalar
vpwrSystemMultRectAlarm = _VpwrSystemMultRectAlarm_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 6, 14),
    _VpwrSystemMultRectAlarm_Type()
)
vpwrSystemMultRectAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrSystemMultRectAlarm.setStatus("current")
_VpwrSystemModlCommAlarm_Type = PositiveInteger
_VpwrSystemModlCommAlarm_Object = MibScalar
vpwrSystemModlCommAlarm = _VpwrSystemModlCommAlarm_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 6, 15),
    _VpwrSystemModlCommAlarm_Type()
)
vpwrSystemModlCommAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrSystemModlCommAlarm.setStatus("current")
_VpwrSystemOverTempAlarm_Type = PositiveInteger
_VpwrSystemOverTempAlarm_Object = MibScalar
vpwrSystemOverTempAlarm = _VpwrSystemOverTempAlarm_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 6, 16),
    _VpwrSystemOverTempAlarm_Type()
)
vpwrSystemOverTempAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrSystemOverTempAlarm.setStatus("current")
_VpwrSystemThermRAAlarm_Type = PositiveInteger
_VpwrSystemThermRAAlarm_Object = MibScalar
vpwrSystemThermRAAlarm = _VpwrSystemThermRAAlarm_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 6, 17),
    _VpwrSystemThermRAAlarm_Type()
)
vpwrSystemThermRAAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrSystemThermRAAlarm.setStatus("current")
_VpwrSystemBDTAlarm_Type = PositiveInteger
_VpwrSystemBDTAlarm_Object = MibScalar
vpwrSystemBDTAlarm = _VpwrSystemBDTAlarm_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 6, 18),
    _VpwrSystemBDTAlarm_Type()
)
vpwrSystemBDTAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrSystemBDTAlarm.setStatus("current")
_VpwrSystemRectUVAlarm_Type = PositiveInteger
_VpwrSystemRectUVAlarm_Object = MibScalar
vpwrSystemRectUVAlarm = _VpwrSystemRectUVAlarm_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 6, 19),
    _VpwrSystemRectUVAlarm_Type()
)
vpwrSystemRectUVAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrSystemRectUVAlarm.setStatus("current")
_VpwrSystemMultRectUVAlarm_Type = PositiveInteger
_VpwrSystemMultRectUVAlarm_Object = MibScalar
vpwrSystemMultRectUVAlarm = _VpwrSystemMultRectUVAlarm_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 6, 20),
    _VpwrSystemMultRectUVAlarm_Type()
)
vpwrSystemMultRectUVAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrSystemMultRectUVAlarm.setStatus("current")
_VpwrSystemSnglRngrAlarm_Type = PositiveInteger
_VpwrSystemSnglRngrAlarm_Object = MibScalar
vpwrSystemSnglRngrAlarm = _VpwrSystemSnglRngrAlarm_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 6, 21),
    _VpwrSystemSnglRngrAlarm_Type()
)
vpwrSystemSnglRngrAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrSystemSnglRngrAlarm.setStatus("current")
_VpwrSystemMultRngrAlarm_Type = PositiveInteger
_VpwrSystemMultRngrAlarm_Object = MibScalar
vpwrSystemMultRngrAlarm = _VpwrSystemMultRngrAlarm_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 6, 22),
    _VpwrSystemMultRngrAlarm_Type()
)
vpwrSystemMultRngrAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrSystemMultRngrAlarm.setStatus("current")
_VpwrSystemTempProbeAlarm_Type = PositiveInteger
_VpwrSystemTempProbeAlarm_Object = MibScalar
vpwrSystemTempProbeAlarm = _VpwrSystemTempProbeAlarm_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 6, 23),
    _VpwrSystemTempProbeAlarm_Type()
)
vpwrSystemTempProbeAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrSystemTempProbeAlarm.setStatus("current")
_VpwrSystemRngrCommAlarm_Type = PositiveInteger
_VpwrSystemRngrCommAlarm_Object = MibScalar
vpwrSystemRngrCommAlarm = _VpwrSystemRngrCommAlarm_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 6, 24),
    _VpwrSystemRngrCommAlarm_Type()
)
vpwrSystemRngrCommAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrSystemRngrCommAlarm.setStatus("current")
_VpwrSystemDistPMCommAlarm_Type = PositiveInteger
_VpwrSystemDistPMCommAlarm_Object = MibScalar
vpwrSystemDistPMCommAlarm = _VpwrSystemDistPMCommAlarm_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 6, 25),
    _VpwrSystemDistPMCommAlarm_Type()
)
vpwrSystemDistPMCommAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrSystemDistPMCommAlarm.setStatus("current")
_VpwrSystemRectILimitAlarm_Type = PositiveInteger
_VpwrSystemRectILimitAlarm_Object = MibScalar
vpwrSystemRectILimitAlarm = _VpwrSystemRectILimitAlarm_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 6, 26),
    _VpwrSystemRectILimitAlarm_Type()
)
vpwrSystemRectILimitAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrSystemRectILimitAlarm.setStatus("current")
_VpwrSystemMultRectILimitAlarm_Type = PositiveInteger
_VpwrSystemMultRectILimitAlarm_Object = MibScalar
vpwrSystemMultRectILimitAlarm = _VpwrSystemMultRectILimitAlarm_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 6, 27),
    _VpwrSystemMultRectILimitAlarm_Type()
)
vpwrSystemMultRectILimitAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrSystemMultRectILimitAlarm.setStatus("current")
_VpwrSystemUnmappedI2CCANAlarm_Type = PositiveInteger
_VpwrSystemUnmappedI2CCANAlarm_Object = MibScalar
vpwrSystemUnmappedI2CCANAlarm = _VpwrSystemUnmappedI2CCANAlarm_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 6, 28),
    _VpwrSystemUnmappedI2CCANAlarm_Type()
)
vpwrSystemUnmappedI2CCANAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrSystemUnmappedI2CCANAlarm.setStatus("current")
_VpwrSystemConfigErrAlarm_Type = PositiveInteger
_VpwrSystemConfigErrAlarm_Object = MibScalar
vpwrSystemConfigErrAlarm = _VpwrSystemConfigErrAlarm_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 6, 29),
    _VpwrSystemConfigErrAlarm_Type()
)
vpwrSystemConfigErrAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrSystemConfigErrAlarm.setStatus("current")
_VpwrSystemDispFWAlarm_Type = PositiveInteger
_VpwrSystemDispFWAlarm_Object = MibScalar
vpwrSystemDispFWAlarm = _VpwrSystemDispFWAlarm_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 6, 30),
    _VpwrSystemDispFWAlarm_Type()
)
vpwrSystemDispFWAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrSystemDispFWAlarm.setStatus("current")
_VpwrSystemUndefinedAlarm_Type = PositiveInteger
_VpwrSystemUndefinedAlarm_Object = MibScalar
vpwrSystemUndefinedAlarm = _VpwrSystemUndefinedAlarm_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 6, 31),
    _VpwrSystemUndefinedAlarm_Type()
)
vpwrSystemUndefinedAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrSystemUndefinedAlarm.setStatus("current")
_VpwrDcPowerRectifier_ObjectIdentity = ObjectIdentity
vpwrDcPowerRectifier = _VpwrDcPowerRectifier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 3)
)
_VpwrRectifierConfigGroup_ObjectIdentity = ObjectIdentity
vpwrRectifierConfigGroup = _VpwrRectifierConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 3, 1)
)
_VpwrRectifierFVSetpoint_Type = Integer32
_VpwrRectifierFVSetpoint_Object = MibScalar
vpwrRectifierFVSetpoint = _VpwrRectifierFVSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 13858, 3, 1, 1),
    _VpwrRectifierFVSetpoint_Type()
)
vpwrRectifierFVSetpoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrRectifierFVSetpoint.setStatus("current")
if mibBuilder.loadTexts:
    vpwrRectifierFVSetpoint.setUnits(" *.01 Volts")
_VpwrRectifierHVSDSetpoint_Type = Integer32
_VpwrRectifierHVSDSetpoint_Object = MibScalar
vpwrRectifierHVSDSetpoint = _VpwrRectifierHVSDSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 13858, 3, 1, 2),
    _VpwrRectifierHVSDSetpoint_Type()
)
vpwrRectifierHVSDSetpoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrRectifierHVSDSetpoint.setStatus("current")
if mibBuilder.loadTexts:
    vpwrRectifierHVSDSetpoint.setUnits(" *.01 Volts")


class _VpwrRectifierCurrentLimitAdminState_Type(Integer32):
    """Custom type vpwrRectifierCurrentLimitAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("rectCurrentLimitDisabled", 0),
          ("rectCurrentLimitEnabled", 1))
    )


_VpwrRectifierCurrentLimitAdminState_Type.__name__ = "Integer32"
_VpwrRectifierCurrentLimitAdminState_Object = MibScalar
vpwrRectifierCurrentLimitAdminState = _VpwrRectifierCurrentLimitAdminState_Object(
    (1, 3, 6, 1, 4, 1, 13858, 3, 1, 3),
    _VpwrRectifierCurrentLimitAdminState_Type()
)
vpwrRectifierCurrentLimitAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrRectifierCurrentLimitAdminState.setStatus("current")


class _VpwrRectifierCurrentLimit_Type(Integer32):
    """Custom type vpwrRectifierCurrentLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 220),
    )


_VpwrRectifierCurrentLimit_Type.__name__ = "Integer32"
_VpwrRectifierCurrentLimit_Object = MibScalar
vpwrRectifierCurrentLimit = _VpwrRectifierCurrentLimit_Object(
    (1, 3, 6, 1, 4, 1, 13858, 3, 1, 4),
    _VpwrRectifierCurrentLimit_Type()
)
vpwrRectifierCurrentLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrRectifierCurrentLimit.setStatus("current")
if mibBuilder.loadTexts:
    vpwrRectifierCurrentLimit.setUnits("Amperes")
_VpwrRectifierFallbackAdminState_Type = GenericEnableDisableTC
_VpwrRectifierFallbackAdminState_Object = MibScalar
vpwrRectifierFallbackAdminState = _VpwrRectifierFallbackAdminState_Object(
    (1, 3, 6, 1, 4, 1, 13858, 3, 1, 5),
    _VpwrRectifierFallbackAdminState_Type()
)
vpwrRectifierFallbackAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrRectifierFallbackAdminState.setStatus("current")
_VpwrRectifierFallbackVoltage_Type = Integer32
_VpwrRectifierFallbackVoltage_Object = MibScalar
vpwrRectifierFallbackVoltage = _VpwrRectifierFallbackVoltage_Object(
    (1, 3, 6, 1, 4, 1, 13858, 3, 1, 6),
    _VpwrRectifierFallbackVoltage_Type()
)
vpwrRectifierFallbackVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrRectifierFallbackVoltage.setStatus("current")
if mibBuilder.loadTexts:
    vpwrRectifierFallbackVoltage.setUnits(" *.01 Volts")
_VpwrRectifierAlarmGroup_ObjectIdentity = ObjectIdentity
vpwrRectifierAlarmGroup = _VpwrRectifierAlarmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 3, 2)
)
_VpwrRectAlarmDCFail_ObjectIdentity = ObjectIdentity
vpwrRectAlarmDCFail = _VpwrRectAlarmDCFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 3, 2, 1)
)
if mibBuilder.loadTexts:
    vpwrRectAlarmDCFail.setStatus("current")
_VpwrRectAlarmBoostFail_ObjectIdentity = ObjectIdentity
vpwrRectAlarmBoostFail = _VpwrRectAlarmBoostFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 3, 2, 2)
)
if mibBuilder.loadTexts:
    vpwrRectAlarmBoostFail.setStatus("current")
_VpwrRectAlarmACFail_ObjectIdentity = ObjectIdentity
vpwrRectAlarmACFail = _VpwrRectAlarmACFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 3, 2, 3)
)
if mibBuilder.loadTexts:
    vpwrRectAlarmACFail.setStatus("current")
_VpwrRectAlarmHVSD_ObjectIdentity = ObjectIdentity
vpwrRectAlarmHVSD = _VpwrRectAlarmHVSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 3, 2, 4)
)
if mibBuilder.loadTexts:
    vpwrRectAlarmHVSD.setStatus("current")
_VpwrRectAlarmFanFail_ObjectIdentity = ObjectIdentity
vpwrRectAlarmFanFail = _VpwrRectAlarmFanFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 3, 2, 5)
)
if mibBuilder.loadTexts:
    vpwrRectAlarmFanFail.setStatus("current")
_VpwrRectAlarmAmbTemp_ObjectIdentity = ObjectIdentity
vpwrRectAlarmAmbTemp = _VpwrRectAlarmAmbTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 3, 2, 6)
)
if mibBuilder.loadTexts:
    vpwrRectAlarmAmbTemp.setStatus("current")
_VpwrRectAlarmIntTemp_ObjectIdentity = ObjectIdentity
vpwrRectAlarmIntTemp = _VpwrRectAlarmIntTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 3, 2, 7)
)
if mibBuilder.loadTexts:
    vpwrRectAlarmIntTemp.setStatus("current")
_VpwrRectAlarmIShare_ObjectIdentity = ObjectIdentity
vpwrRectAlarmIShare = _VpwrRectAlarmIShare_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 3, 2, 8)
)
if mibBuilder.loadTexts:
    vpwrRectAlarmIShare.setStatus("current")
_VpwrRectAlarmUV_ObjectIdentity = ObjectIdentity
vpwrRectAlarmUV = _VpwrRectAlarmUV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 3, 2, 9)
)
if mibBuilder.loadTexts:
    vpwrRectAlarmUV.setStatus("current")
_VpwrRectAlarmLowVoltage_ObjectIdentity = ObjectIdentity
vpwrRectAlarmLowVoltage = _VpwrRectAlarmLowVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 3, 2, 10)
)
if mibBuilder.loadTexts:
    vpwrRectAlarmLowVoltage.setStatus("current")
_VpwrRectAlarmReserved_ObjectIdentity = ObjectIdentity
vpwrRectAlarmReserved = _VpwrRectAlarmReserved_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 3, 2, 11)
)
if mibBuilder.loadTexts:
    vpwrRectAlarmReserved.setStatus("current")
_VpwrRectAlarmDCEnable_ObjectIdentity = ObjectIdentity
vpwrRectAlarmDCEnable = _VpwrRectAlarmDCEnable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 3, 2, 12)
)
if mibBuilder.loadTexts:
    vpwrRectAlarmDCEnable.setStatus("current")
_VpwrRectAlarmRemoteShutdown_ObjectIdentity = ObjectIdentity
vpwrRectAlarmRemoteShutdown = _VpwrRectAlarmRemoteShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 3, 2, 13)
)
if mibBuilder.loadTexts:
    vpwrRectAlarmRemoteShutdown.setStatus("current")
_VpwrRectAlarmModDisableShutdown_ObjectIdentity = ObjectIdentity
vpwrRectAlarmModDisableShutdown = _VpwrRectAlarmModDisableShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 3, 2, 14)
)
if mibBuilder.loadTexts:
    vpwrRectAlarmModDisableShutdown.setStatus("current")
_VpwrRectAlarmShortPinShutdown_ObjectIdentity = ObjectIdentity
vpwrRectAlarmShortPinShutdown = _VpwrRectAlarmShortPinShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 3, 2, 15)
)
if mibBuilder.loadTexts:
    vpwrRectAlarmShortPinShutdown.setStatus("current")
_VpwrRectAlarmBoostComm_ObjectIdentity = ObjectIdentity
vpwrRectAlarmBoostComm = _VpwrRectAlarmBoostComm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 3, 2, 16)
)
if mibBuilder.loadTexts:
    vpwrRectAlarmBoostComm.setStatus("current")
_VpwrDcPowerLvd_ObjectIdentity = ObjectIdentity
vpwrDcPowerLvd = _VpwrDcPowerLvd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 4)
)
_VpwrLvdConfigGroup_ObjectIdentity = ObjectIdentity
vpwrLvdConfigGroup = _VpwrLvdConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 4, 1)
)
_VpwrLvdWarningSetpoint_Type = Integer32
_VpwrLvdWarningSetpoint_Object = MibScalar
vpwrLvdWarningSetpoint = _VpwrLvdWarningSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 13858, 4, 1, 1),
    _VpwrLvdWarningSetpoint_Type()
)
vpwrLvdWarningSetpoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrLvdWarningSetpoint.setStatus("current")
if mibBuilder.loadTexts:
    vpwrLvdWarningSetpoint.setUnits(" * .01 Volts")
_VpwrLvdDisconnectSetpoint_Type = Integer32
_VpwrLvdDisconnectSetpoint_Object = MibScalar
vpwrLvdDisconnectSetpoint = _VpwrLvdDisconnectSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 13858, 4, 1, 2),
    _VpwrLvdDisconnectSetpoint_Type()
)
vpwrLvdDisconnectSetpoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrLvdDisconnectSetpoint.setStatus("current")
if mibBuilder.loadTexts:
    vpwrLvdDisconnectSetpoint.setUnits(" *.01 Volts")
_VpwrLvdReconnectSetpoint_Type = Integer32
_VpwrLvdReconnectSetpoint_Object = MibScalar
vpwrLvdReconnectSetpoint = _VpwrLvdReconnectSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 13858, 4, 1, 3),
    _VpwrLvdReconnectSetpoint_Type()
)
vpwrLvdReconnectSetpoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrLvdReconnectSetpoint.setStatus("current")
if mibBuilder.loadTexts:
    vpwrLvdReconnectSetpoint.setUnits(" *.01 Volts")


class _VpwrLvdReconnectDelayTimer_Type(Integer32):
    """Custom type vpwrLvdReconnectDelayTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 240),
    )


_VpwrLvdReconnectDelayTimer_Type.__name__ = "Integer32"
_VpwrLvdReconnectDelayTimer_Object = MibScalar
vpwrLvdReconnectDelayTimer = _VpwrLvdReconnectDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 13858, 4, 1, 4),
    _VpwrLvdReconnectDelayTimer_Type()
)
vpwrLvdReconnectDelayTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrLvdReconnectDelayTimer.setStatus("current")
if mibBuilder.loadTexts:
    vpwrLvdReconnectDelayTimer.setUnits(" Seconds")
_VpwrLvd2DisconnectSetpoint_Type = Integer32
_VpwrLvd2DisconnectSetpoint_Object = MibScalar
vpwrLvd2DisconnectSetpoint = _VpwrLvd2DisconnectSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 13858, 4, 1, 7),
    _VpwrLvd2DisconnectSetpoint_Type()
)
vpwrLvd2DisconnectSetpoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrLvd2DisconnectSetpoint.setStatus("current")
if mibBuilder.loadTexts:
    vpwrLvd2DisconnectSetpoint.setUnits(" *.01 Volts")
_VpwrLvd2ReconnectSetpoint_Type = Integer32
_VpwrLvd2ReconnectSetpoint_Object = MibScalar
vpwrLvd2ReconnectSetpoint = _VpwrLvd2ReconnectSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 13858, 4, 1, 8),
    _VpwrLvd2ReconnectSetpoint_Type()
)
vpwrLvd2ReconnectSetpoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrLvd2ReconnectSetpoint.setStatus("current")
if mibBuilder.loadTexts:
    vpwrLvd2ReconnectSetpoint.setUnits(" *.01 Volts")


class _VpwrLvd2ReconnectDelayTimer_Type(Integer32):
    """Custom type vpwrLvd2ReconnectDelayTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 240),
    )


_VpwrLvd2ReconnectDelayTimer_Type.__name__ = "Integer32"
_VpwrLvd2ReconnectDelayTimer_Object = MibScalar
vpwrLvd2ReconnectDelayTimer = _VpwrLvd2ReconnectDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 13858, 4, 1, 9),
    _VpwrLvd2ReconnectDelayTimer_Type()
)
vpwrLvd2ReconnectDelayTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrLvd2ReconnectDelayTimer.setStatus("current")
if mibBuilder.loadTexts:
    vpwrLvd2ReconnectDelayTimer.setUnits(" Seconds")
_VpwrLvd3DisconnectSetpoint_Type = Integer32
_VpwrLvd3DisconnectSetpoint_Object = MibScalar
vpwrLvd3DisconnectSetpoint = _VpwrLvd3DisconnectSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 13858, 4, 1, 11),
    _VpwrLvd3DisconnectSetpoint_Type()
)
vpwrLvd3DisconnectSetpoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrLvd3DisconnectSetpoint.setStatus("current")
if mibBuilder.loadTexts:
    vpwrLvd3DisconnectSetpoint.setUnits(" *.01 Volts")
_VpwrLvd3ReconnectSetpoint_Type = Integer32
_VpwrLvd3ReconnectSetpoint_Object = MibScalar
vpwrLvd3ReconnectSetpoint = _VpwrLvd3ReconnectSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 13858, 4, 1, 12),
    _VpwrLvd3ReconnectSetpoint_Type()
)
vpwrLvd3ReconnectSetpoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrLvd3ReconnectSetpoint.setStatus("current")
if mibBuilder.loadTexts:
    vpwrLvd3ReconnectSetpoint.setUnits(" *.01 Volts")


class _VpwrLvd3ReconnectDelayTimer_Type(Integer32):
    """Custom type vpwrLvd3ReconnectDelayTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 240),
    )


_VpwrLvd3ReconnectDelayTimer_Type.__name__ = "Integer32"
_VpwrLvd3ReconnectDelayTimer_Object = MibScalar
vpwrLvd3ReconnectDelayTimer = _VpwrLvd3ReconnectDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 13858, 4, 1, 13),
    _VpwrLvd3ReconnectDelayTimer_Type()
)
vpwrLvd3ReconnectDelayTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrLvd3ReconnectDelayTimer.setStatus("current")
if mibBuilder.loadTexts:
    vpwrLvd3ReconnectDelayTimer.setUnits(" Seconds")
_VpwrLvd4DisconnectSetpoint_Type = Integer32
_VpwrLvd4DisconnectSetpoint_Object = MibScalar
vpwrLvd4DisconnectSetpoint = _VpwrLvd4DisconnectSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 13858, 4, 1, 15),
    _VpwrLvd4DisconnectSetpoint_Type()
)
vpwrLvd4DisconnectSetpoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrLvd4DisconnectSetpoint.setStatus("current")
if mibBuilder.loadTexts:
    vpwrLvd4DisconnectSetpoint.setUnits(" *.01 Volts")
_VpwrLvd4ReconnectSetpoint_Type = Integer32
_VpwrLvd4ReconnectSetpoint_Object = MibScalar
vpwrLvd4ReconnectSetpoint = _VpwrLvd4ReconnectSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 13858, 4, 1, 16),
    _VpwrLvd4ReconnectSetpoint_Type()
)
vpwrLvd4ReconnectSetpoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrLvd4ReconnectSetpoint.setStatus("current")
if mibBuilder.loadTexts:
    vpwrLvd4ReconnectSetpoint.setUnits(" *.01 Volts")


class _VpwrLvd4ReconnectDelayTimer_Type(Integer32):
    """Custom type vpwrLvd4ReconnectDelayTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 240),
    )


_VpwrLvd4ReconnectDelayTimer_Type.__name__ = "Integer32"
_VpwrLvd4ReconnectDelayTimer_Object = MibScalar
vpwrLvd4ReconnectDelayTimer = _VpwrLvd4ReconnectDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 13858, 4, 1, 17),
    _VpwrLvd4ReconnectDelayTimer_Type()
)
vpwrLvd4ReconnectDelayTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrLvd4ReconnectDelayTimer.setStatus("current")
if mibBuilder.loadTexts:
    vpwrLvd4ReconnectDelayTimer.setUnits(" Seconds")


class _VpwrDCPowerLampTest_Type(Integer32):
    """Custom type vpwrDCPowerLampTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_VpwrDCPowerLampTest_Type.__name__ = "Integer32"
_VpwrDCPowerLampTest_Object = MibScalar
vpwrDCPowerLampTest = _VpwrDCPowerLampTest_Object(
    (1, 3, 6, 1, 4, 1, 13858, 5),
    _VpwrDCPowerLampTest_Type()
)
vpwrDCPowerLampTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrDCPowerLampTest.setStatus("current")
_VpwrDcPowerModuleIdent_ObjectIdentity = ObjectIdentity
vpwrDcPowerModuleIdent = _VpwrDcPowerModuleIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 6)
)
_VpwrDcPowerModuleIdentTable_Object = MibTable
vpwrDcPowerModuleIdentTable = _VpwrDcPowerModuleIdentTable_Object(
    (1, 3, 6, 1, 4, 1, 13858, 6, 1)
)
if mibBuilder.loadTexts:
    vpwrDcPowerModuleIdentTable.setStatus("current")
_VpwrDcPowerModuleIdentEntry_Object = MibTableRow
vpwrDcPowerModuleIdentEntry = _VpwrDcPowerModuleIdentEntry_Object(
    (1, 3, 6, 1, 4, 1, 13858, 6, 1, 1)
)
vpwrDcPowerModuleIdentEntry.setIndexNames(
    (0, "ELTEK-BC2000-DC-POWER-MIB", "vpwrBayIndex1"),
    (0, "ELTEK-BC2000-DC-POWER-MIB", "vpwrDCModuleIndex"),
)
if mibBuilder.loadTexts:
    vpwrDcPowerModuleIdentEntry.setStatus("current")
_VpwrBayIndex1_Type = PositiveInteger
_VpwrBayIndex1_Object = MibTableColumn
vpwrBayIndex1 = _VpwrBayIndex1_Object(
    (1, 3, 6, 1, 4, 1, 13858, 6, 1, 1, 1),
    _VpwrBayIndex1_Type()
)
vpwrBayIndex1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrBayIndex1.setStatus("current")
_VpwrDCModuleIndex_Type = PositiveInteger
_VpwrDCModuleIndex_Object = MibTableColumn
vpwrDCModuleIndex = _VpwrDCModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 13858, 6, 1, 1, 2),
    _VpwrDCModuleIndex_Type()
)
vpwrDCModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrDCModuleIndex.setStatus("current")
_VpwrModuleSerialNumber_Type = DisplayString
_VpwrModuleSerialNumber_Object = MibTableColumn
vpwrModuleSerialNumber = _VpwrModuleSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 13858, 6, 1, 1, 3),
    _VpwrModuleSerialNumber_Type()
)
vpwrModuleSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrModuleSerialNumber.setStatus("current")
_VpwrModuleModelNumber_Type = DisplayString
_VpwrModuleModelNumber_Object = MibTableColumn
vpwrModuleModelNumber = _VpwrModuleModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 13858, 6, 1, 1, 4),
    _VpwrModuleModelNumber_Type()
)
vpwrModuleModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrModuleModelNumber.setStatus("current")
_VpwrModuleFwVersion_Type = DisplayString
_VpwrModuleFwVersion_Object = MibTableColumn
vpwrModuleFwVersion = _VpwrModuleFwVersion_Object(
    (1, 3, 6, 1, 4, 1, 13858, 6, 1, 1, 5),
    _VpwrModuleFwVersion_Type()
)
vpwrModuleFwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrModuleFwVersion.setStatus("current")
_VpwrModuleTestDate_Type = DisplayString
_VpwrModuleTestDate_Object = MibTableColumn
vpwrModuleTestDate = _VpwrModuleTestDate_Object(
    (1, 3, 6, 1, 4, 1, 13858, 6, 1, 1, 6),
    _VpwrModuleTestDate_Type()
)
vpwrModuleTestDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrModuleTestDate.setStatus("current")
_VpwrModuleOperHours_Type = Counter32
_VpwrModuleOperHours_Object = MibTableColumn
vpwrModuleOperHours = _VpwrModuleOperHours_Object(
    (1, 3, 6, 1, 4, 1, 13858, 6, 1, 1, 7),
    _VpwrModuleOperHours_Type()
)
vpwrModuleOperHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrModuleOperHours.setStatus("current")
_VpwrDcPowerBatteryGroup_ObjectIdentity = ObjectIdentity
vpwrDcPowerBatteryGroup = _VpwrDcPowerBatteryGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 7)
)
_VpwrBatteryTempGroup_ObjectIdentity = ObjectIdentity
vpwrBatteryTempGroup = _VpwrBatteryTempGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 7, 1)
)
_VpwrBatteryTempTable_Object = MibTable
vpwrBatteryTempTable = _VpwrBatteryTempTable_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 1, 1)
)
if mibBuilder.loadTexts:
    vpwrBatteryTempTable.setStatus("current")
_VpwrBatteryTempEntry_Object = MibTableRow
vpwrBatteryTempEntry = _VpwrBatteryTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 1, 1, 1)
)
vpwrBatteryTempEntry.setIndexNames(
    (0, "ELTEK-BC2000-DC-POWER-MIB", "vpwrBatteryTempIndex"),
)
if mibBuilder.loadTexts:
    vpwrBatteryTempEntry.setStatus("current")


class _VpwrBatteryTempIndex_Type(Integer32):
    """Custom type vpwrBatteryTempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VpwrBatteryTempIndex_Type.__name__ = "Integer32"
_VpwrBatteryTempIndex_Object = MibTableColumn
vpwrBatteryTempIndex = _VpwrBatteryTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 1, 1, 1, 1),
    _VpwrBatteryTempIndex_Type()
)
vpwrBatteryTempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrBatteryTempIndex.setStatus("current")


class _VpwrBatteryTempName_Type(DisplayString):
    """Custom type vpwrBatteryTempName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_VpwrBatteryTempName_Type.__name__ = "DisplayString"
_VpwrBatteryTempName_Object = MibTableColumn
vpwrBatteryTempName = _VpwrBatteryTempName_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 1, 1, 1, 2),
    _VpwrBatteryTempName_Type()
)
vpwrBatteryTempName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrBatteryTempName.setStatus("current")
_VpwrBatteryTemp_Type = SysInputValue
_VpwrBatteryTemp_Object = MibTableColumn
vpwrBatteryTemp = _VpwrBatteryTemp_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 1, 1, 1, 3),
    _VpwrBatteryTemp_Type()
)
vpwrBatteryTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrBatteryTemp.setStatus("current")
if mibBuilder.loadTexts:
    vpwrBatteryTemp.setUnits("degrees Celsius")
_VpwrBatteryTempLThreshold_Type = Integer32
_VpwrBatteryTempLThreshold_Object = MibScalar
vpwrBatteryTempLThreshold = _VpwrBatteryTempLThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 1, 2),
    _VpwrBatteryTempLThreshold_Type()
)
vpwrBatteryTempLThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrBatteryTempLThreshold.setStatus("current")
if mibBuilder.loadTexts:
    vpwrBatteryTempLThreshold.setUnits("degrees Celsius")
_VpwrBatteryTempUThreshold_Type = Integer32
_VpwrBatteryTempUThreshold_Object = MibScalar
vpwrBatteryTempUThreshold = _VpwrBatteryTempUThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 1, 3),
    _VpwrBatteryTempUThreshold_Type()
)
vpwrBatteryTempUThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrBatteryTempUThreshold.setStatus("current")
if mibBuilder.loadTexts:
    vpwrBatteryTempUThreshold.setUnits("degrees Celsius")


class _BatteryTempCompensation_Type(Integer32):
    """Custom type batteryTempCompensation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("tempCompDisabled", 0),
          ("tempCompEnabled", 1))
    )


_BatteryTempCompensation_Type.__name__ = "Integer32"
_BatteryTempCompensation_Object = MibScalar
batteryTempCompensation = _BatteryTempCompensation_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 1, 4),
    _BatteryTempCompensation_Type()
)
batteryTempCompensation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTempCompensation.setStatus("current")


class _BatteryTempCompHighStartTemperature_Type(Integer32):
    """Custom type batteryTempCompHighStartTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25, 60),
    )


_BatteryTempCompHighStartTemperature_Type.__name__ = "Integer32"
_BatteryTempCompHighStartTemperature_Object = MibScalar
batteryTempCompHighStartTemperature = _BatteryTempCompHighStartTemperature_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 1, 5),
    _BatteryTempCompHighStartTemperature_Type()
)
batteryTempCompHighStartTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTempCompHighStartTemperature.setStatus("current")
if mibBuilder.loadTexts:
    batteryTempCompHighStartTemperature.setUnits("degrees Celsius")
_BatteryTempCompHighStopVoltage_Type = Integer32
_BatteryTempCompHighStopVoltage_Object = MibScalar
batteryTempCompHighStopVoltage = _BatteryTempCompHighStopVoltage_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 1, 6),
    _BatteryTempCompHighStopVoltage_Type()
)
batteryTempCompHighStopVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTempCompHighStopVoltage.setStatus("current")
if mibBuilder.loadTexts:
    batteryTempCompHighStopVoltage.setUnits(" *.01 Volts")


class _BatteryTempCompHighSlope_Type(Integer32):
    """Custom type batteryTempCompHighSlope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 250),
    )


_BatteryTempCompHighSlope_Type.__name__ = "Integer32"
_BatteryTempCompHighSlope_Object = MibScalar
batteryTempCompHighSlope = _BatteryTempCompHighSlope_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 1, 7),
    _BatteryTempCompHighSlope_Type()
)
batteryTempCompHighSlope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTempCompHighSlope.setStatus("current")
if mibBuilder.loadTexts:
    batteryTempCompHighSlope.setUnits(" milli-Volts per degrees Celsius")
_BatteryTempCompLowStartTemperature_Type = Integer32
_BatteryTempCompLowStartTemperature_Object = MibScalar
batteryTempCompLowStartTemperature = _BatteryTempCompLowStartTemperature_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 1, 8),
    _BatteryTempCompLowStartTemperature_Type()
)
batteryTempCompLowStartTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTempCompLowStartTemperature.setStatus("current")
if mibBuilder.loadTexts:
    batteryTempCompLowStartTemperature.setUnits("degrees Celsius")
_BatteryTempCompLowStopVoltage_Type = Integer32
_BatteryTempCompLowStopVoltage_Object = MibScalar
batteryTempCompLowStopVoltage = _BatteryTempCompLowStopVoltage_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 1, 9),
    _BatteryTempCompLowStopVoltage_Type()
)
batteryTempCompLowStopVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTempCompLowStopVoltage.setStatus("current")
if mibBuilder.loadTexts:
    batteryTempCompLowStopVoltage.setUnits(" *.01 Volts")


class _BatteryTempCompLowSlope_Type(Integer32):
    """Custom type batteryTempCompLowSlope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 250),
    )


_BatteryTempCompLowSlope_Type.__name__ = "Integer32"
_BatteryTempCompLowSlope_Object = MibScalar
batteryTempCompLowSlope = _BatteryTempCompLowSlope_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 1, 10),
    _BatteryTempCompLowSlope_Type()
)
batteryTempCompLowSlope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTempCompLowSlope.setStatus("current")
if mibBuilder.loadTexts:
    batteryTempCompLowSlope.setUnits(" milli-Volts per degrees Celsius")


class _BatteryTempCompRunawayTemperature_Type(Integer32):
    """Custom type batteryTempCompRunawayTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25, 60),
    )


_BatteryTempCompRunawayTemperature_Type.__name__ = "Integer32"
_BatteryTempCompRunawayTemperature_Object = MibScalar
batteryTempCompRunawayTemperature = _BatteryTempCompRunawayTemperature_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 1, 11),
    _BatteryTempCompRunawayTemperature_Type()
)
batteryTempCompRunawayTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTempCompRunawayTemperature.setStatus("current")
if mibBuilder.loadTexts:
    batteryTempCompRunawayTemperature.setUnits("degrees Celsius")
_BatteryTempCompRunawayStopVoltage_Type = Integer32
_BatteryTempCompRunawayStopVoltage_Object = MibScalar
batteryTempCompRunawayStopVoltage = _BatteryTempCompRunawayStopVoltage_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 1, 12),
    _BatteryTempCompRunawayStopVoltage_Type()
)
batteryTempCompRunawayStopVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTempCompRunawayStopVoltage.setStatus("current")
if mibBuilder.loadTexts:
    batteryTempCompRunawayStopVoltage.setUnits(" *.01 Volts")


class _BatteryTempCompSenseSource_Type(Integer32):
    """Custom type batteryTempCompSenseSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("internal", 0),
          ("external", 1))
    )


_BatteryTempCompSenseSource_Type.__name__ = "Integer32"
_BatteryTempCompSenseSource_Object = MibScalar
batteryTempCompSenseSource = _BatteryTempCompSenseSource_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 1, 13),
    _BatteryTempCompSenseSource_Type()
)
batteryTempCompSenseSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTempCompSenseSource.setStatus("current")


class _BatteryTempCompRunawayState_Type(Integer32):
    """Custom type batteryTempCompRunawayState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_BatteryTempCompRunawayState_Type.__name__ = "Integer32"
_BatteryTempCompRunawayState_Object = MibScalar
batteryTempCompRunawayState = _BatteryTempCompRunawayState_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 1, 14),
    _BatteryTempCompRunawayState_Type()
)
batteryTempCompRunawayState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTempCompRunawayState.setStatus("current")
_VpwrBatteryCurrentGroup_ObjectIdentity = ObjectIdentity
vpwrBatteryCurrentGroup = _VpwrBatteryCurrentGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 7, 2)
)


class _VpwrBatteryCurrentLimitAdminState_Type(Integer32):
    """Custom type vpwrBatteryCurrentLimitAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("batteryCurrentLimitDisabled", 0),
          ("batteryCurrentLimitEnabled", 1))
    )


_VpwrBatteryCurrentLimitAdminState_Type.__name__ = "Integer32"
_VpwrBatteryCurrentLimitAdminState_Object = MibScalar
vpwrBatteryCurrentLimitAdminState = _VpwrBatteryCurrentLimitAdminState_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 2, 1),
    _VpwrBatteryCurrentLimitAdminState_Type()
)
vpwrBatteryCurrentLimitAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrBatteryCurrentLimitAdminState.setStatus("current")


class _VpwrBatteryCurrentLimit_Type(Integer32):
    """Custom type vpwrBatteryCurrentLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 600),
    )


_VpwrBatteryCurrentLimit_Type.__name__ = "Integer32"
_VpwrBatteryCurrentLimit_Object = MibScalar
vpwrBatteryCurrentLimit = _VpwrBatteryCurrentLimit_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 2, 2),
    _VpwrBatteryCurrentLimit_Type()
)
vpwrBatteryCurrentLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrBatteryCurrentLimit.setStatus("current")
if mibBuilder.loadTexts:
    vpwrBatteryCurrentLimit.setUnits("Ampere")
_VpwrBatteryCurrent_Type = Integer32
_VpwrBatteryCurrent_Object = MibScalar
vpwrBatteryCurrent = _VpwrBatteryCurrent_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 2, 3),
    _VpwrBatteryCurrent_Type()
)
vpwrBatteryCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrBatteryCurrent.setStatus("current")
if mibBuilder.loadTexts:
    vpwrBatteryCurrent.setUnits("Ampere")
_VpwrBatteryBoostGroup_ObjectIdentity = ObjectIdentity
vpwrBatteryBoostGroup = _VpwrBatteryBoostGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 7, 3)
)


class _VpwrBoostAdminState_Type(Integer32):
    """Custom type vpwrBoostAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("boostDisabled", 0),
          ("boostEnabled", 1))
    )


_VpwrBoostAdminState_Type.__name__ = "Integer32"
_VpwrBoostAdminState_Object = MibScalar
vpwrBoostAdminState = _VpwrBoostAdminState_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 3, 1),
    _VpwrBoostAdminState_Type()
)
vpwrBoostAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrBoostAdminState.setStatus("current")
_VpwrBoostVoltage_Type = Integer32
_VpwrBoostVoltage_Object = MibScalar
vpwrBoostVoltage = _VpwrBoostVoltage_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 3, 2),
    _VpwrBoostVoltage_Type()
)
vpwrBoostVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrBoostVoltage.setStatus("current")
if mibBuilder.loadTexts:
    vpwrBoostVoltage.setUnits(" *.01 Volts")


class _VpwrBoostDuration_Type(Integer32):
    """Custom type vpwrBoostDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 921599),
    )


_VpwrBoostDuration_Type.__name__ = "Integer32"
_VpwrBoostDuration_Object = MibScalar
vpwrBoostDuration = _VpwrBoostDuration_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 3, 3),
    _VpwrBoostDuration_Type()
)
vpwrBoostDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrBoostDuration.setStatus("current")
if mibBuilder.loadTexts:
    vpwrBoostDuration.setUnits("Seconds")


class _VpwrBoostOperState_Type(Integer32):
    """Custom type vpwrBoostOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("boostInactive", 0),
          ("boostActive", 1))
    )


_VpwrBoostOperState_Type.__name__ = "Integer32"
_VpwrBoostOperState_Object = MibScalar
vpwrBoostOperState = _VpwrBoostOperState_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 3, 4),
    _VpwrBoostOperState_Type()
)
vpwrBoostOperState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrBoostOperState.setStatus("current")
_VpwrBatteryDischargeTestGroup_ObjectIdentity = ObjectIdentity
vpwrBatteryDischargeTestGroup = _VpwrBatteryDischargeTestGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 7, 4)
)


class _VpwrBDTAdminState_Type(Integer32):
    """Custom type vpwrBDTAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bdtManualDisabled", 0),
          ("bdtManualEnabled", 1))
    )


_VpwrBDTAdminState_Type.__name__ = "Integer32"
_VpwrBDTAdminState_Object = MibScalar
vpwrBDTAdminState = _VpwrBDTAdminState_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 4, 1),
    _VpwrBDTAdminState_Type()
)
vpwrBDTAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrBDTAdminState.setStatus("current")


class _VpwrBDTDuration_Type(Integer32):
    """Custom type vpwrBDTDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64799),
    )


_VpwrBDTDuration_Type.__name__ = "Integer32"
_VpwrBDTDuration_Object = MibScalar
vpwrBDTDuration = _VpwrBDTDuration_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 4, 2),
    _VpwrBDTDuration_Type()
)
vpwrBDTDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrBDTDuration.setStatus("current")
if mibBuilder.loadTexts:
    vpwrBDTDuration.setUnits("Seconds")
_VpwrBDTAlarmVoltage_Type = Integer32
_VpwrBDTAlarmVoltage_Object = MibScalar
vpwrBDTAlarmVoltage = _VpwrBDTAlarmVoltage_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 4, 3),
    _VpwrBDTAlarmVoltage_Type()
)
vpwrBDTAlarmVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrBDTAlarmVoltage.setStatus("current")
if mibBuilder.loadTexts:
    vpwrBDTAlarmVoltage.setUnits(" *.01 Volts")
_VpwrBDTAbortVoltage_Type = Integer32
_VpwrBDTAbortVoltage_Object = MibScalar
vpwrBDTAbortVoltage = _VpwrBDTAbortVoltage_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 4, 4),
    _VpwrBDTAbortVoltage_Type()
)
vpwrBDTAbortVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrBDTAbortVoltage.setStatus("current")
if mibBuilder.loadTexts:
    vpwrBDTAbortVoltage.setUnits(" *.01 Volts")
_VpwrBDTAlarmCoefficient_Type = Integer32
_VpwrBDTAlarmCoefficient_Object = MibScalar
vpwrBDTAlarmCoefficient = _VpwrBDTAlarmCoefficient_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 4, 5),
    _VpwrBDTAlarmCoefficient_Type()
)
vpwrBDTAlarmCoefficient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrBDTAlarmCoefficient.setStatus("current")
if mibBuilder.loadTexts:
    vpwrBDTAlarmCoefficient.setUnits("None")


class _VpwrBDTOperState_Type(Integer32):
    """Custom type vpwrBDTOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              14)
        )
    )
    namedValues = NamedValues(
        *(("bdtInactive", 0),
          ("bdtManualStart", 1),
          ("bdtACFailStart", 14))
    )


_VpwrBDTOperState_Type.__name__ = "Integer32"
_VpwrBDTOperState_Object = MibScalar
vpwrBDTOperState = _VpwrBDTOperState_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 4, 6),
    _VpwrBDTOperState_Type()
)
vpwrBDTOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrBDTOperState.setStatus("current")


class _VpwrBDTClearAlarm_Type(Integer32):
    """Custom type vpwrBDTClearAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bdtNoAlarm", 0),
          ("bdtAlarmPresent", 1))
    )


_VpwrBDTClearAlarm_Type.__name__ = "Integer32"
_VpwrBDTClearAlarm_Object = MibScalar
vpwrBDTClearAlarm = _VpwrBDTClearAlarm_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 4, 7),
    _VpwrBDTClearAlarm_Type()
)
vpwrBDTClearAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrBDTClearAlarm.setStatus("current")
_VpwrBDTActualTime_Type = Integer32
_VpwrBDTActualTime_Object = MibScalar
vpwrBDTActualTime = _VpwrBDTActualTime_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 4, 8),
    _VpwrBDTActualTime_Type()
)
vpwrBDTActualTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrBDTActualTime.setStatus("current")
if mibBuilder.loadTexts:
    vpwrBDTActualTime.setUnits("minutes")
_VpwrBDTAlarmDelay_Type = Integer32
_VpwrBDTAlarmDelay_Object = MibScalar
vpwrBDTAlarmDelay = _VpwrBDTAlarmDelay_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 4, 9),
    _VpwrBDTAlarmDelay_Type()
)
vpwrBDTAlarmDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrBDTAlarmDelay.setStatus("current")
if mibBuilder.loadTexts:
    vpwrBDTAlarmDelay.setUnits("minutes")
_VpwrBDTResult_Type = BDTResultTC
_VpwrBDTResult_Object = MibScalar
vpwrBDTResult = _VpwrBDTResult_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 4, 10),
    _VpwrBDTResult_Type()
)
vpwrBDTResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrBDTResult.setStatus("current")


class _VpwrBDTAutoAdminState_Type(Integer32):
    """Custom type vpwrBDTAutoAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bdtAutoDisabled", 0),
          ("bdtAutoEnabled", 1))
    )


_VpwrBDTAutoAdminState_Type.__name__ = "Integer32"
_VpwrBDTAutoAdminState_Object = MibScalar
vpwrBDTAutoAdminState = _VpwrBDTAutoAdminState_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 4, 11),
    _VpwrBDTAutoAdminState_Type()
)
vpwrBDTAutoAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrBDTAutoAdminState.setStatus("current")
_VpwrBDTHistTable_Object = MibTable
vpwrBDTHistTable = _VpwrBDTHistTable_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 4, 12)
)
if mibBuilder.loadTexts:
    vpwrBDTHistTable.setStatus("current")
_VpwrBDTHistEntry_Object = MibTableRow
vpwrBDTHistEntry = _VpwrBDTHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 4, 12, 1)
)
vpwrBDTHistEntry.setIndexNames(
    (0, "ELTEK-BC2000-DC-POWER-MIB", "vpwrBDTHistIndex"),
)
if mibBuilder.loadTexts:
    vpwrBDTHistEntry.setStatus("current")
_VpwrBDTHistIndex_Type = PositiveInteger
_VpwrBDTHistIndex_Object = MibTableColumn
vpwrBDTHistIndex = _VpwrBDTHistIndex_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 4, 12, 1, 1),
    _VpwrBDTHistIndex_Type()
)
vpwrBDTHistIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrBDTHistIndex.setStatus("current")
_VpwrBDTHistDateTime_Type = DisplayString
_VpwrBDTHistDateTime_Object = MibTableColumn
vpwrBDTHistDateTime = _VpwrBDTHistDateTime_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 4, 12, 1, 2),
    _VpwrBDTHistDateTime_Type()
)
vpwrBDTHistDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrBDTHistDateTime.setStatus("current")
_VpwrBDTHistDuration_Type = PositiveInteger
_VpwrBDTHistDuration_Object = MibTableColumn
vpwrBDTHistDuration = _VpwrBDTHistDuration_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 4, 12, 1, 3),
    _VpwrBDTHistDuration_Type()
)
vpwrBDTHistDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrBDTHistDuration.setStatus("current")
if mibBuilder.loadTexts:
    vpwrBDTHistDuration.setUnits("Minutes")
_VpwrBDTHistAlarmVoltage_Type = PositiveInteger
_VpwrBDTHistAlarmVoltage_Object = MibTableColumn
vpwrBDTHistAlarmVoltage = _VpwrBDTHistAlarmVoltage_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 4, 12, 1, 4),
    _VpwrBDTHistAlarmVoltage_Type()
)
vpwrBDTHistAlarmVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrBDTHistAlarmVoltage.setStatus("current")
if mibBuilder.loadTexts:
    vpwrBDTHistAlarmVoltage.setUnits(" *.01 Volts")
_VpwrBDTHistAbortVoltage_Type = PositiveInteger
_VpwrBDTHistAbortVoltage_Object = MibTableColumn
vpwrBDTHistAbortVoltage = _VpwrBDTHistAbortVoltage_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 4, 12, 1, 5),
    _VpwrBDTHistAbortVoltage_Type()
)
vpwrBDTHistAbortVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrBDTHistAbortVoltage.setStatus("current")
if mibBuilder.loadTexts:
    vpwrBDTHistAbortVoltage.setUnits(" *.01 Volts")
_VpwrBDTHistStartMethod_Type = BDTStartSourceTC
_VpwrBDTHistStartMethod_Object = MibTableColumn
vpwrBDTHistStartMethod = _VpwrBDTHistStartMethod_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 4, 12, 1, 6),
    _VpwrBDTHistStartMethod_Type()
)
vpwrBDTHistStartMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrBDTHistStartMethod.setStatus("current")
_VpwrBDTHistResult_Type = BDTResultTC
_VpwrBDTHistResult_Object = MibTableColumn
vpwrBDTHistResult = _VpwrBDTHistResult_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 4, 12, 1, 7),
    _VpwrBDTHistResult_Type()
)
vpwrBDTHistResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrBDTHistResult.setStatus("current")
_VpwrBDTHistActualTime_Type = PositiveInteger
_VpwrBDTHistActualTime_Object = MibTableColumn
vpwrBDTHistActualTime = _VpwrBDTHistActualTime_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 4, 12, 1, 8),
    _VpwrBDTHistActualTime_Type()
)
vpwrBDTHistActualTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrBDTHistActualTime.setStatus("current")
if mibBuilder.loadTexts:
    vpwrBDTHistActualTime.setUnits("minutes")
_VpwrBDTHistStartVoltage_Type = PositiveInteger
_VpwrBDTHistStartVoltage_Object = MibTableColumn
vpwrBDTHistStartVoltage = _VpwrBDTHistStartVoltage_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 4, 12, 1, 9),
    _VpwrBDTHistStartVoltage_Type()
)
vpwrBDTHistStartVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrBDTHistStartVoltage.setStatus("current")
if mibBuilder.loadTexts:
    vpwrBDTHistStartVoltage.setUnits(" *.01 Volts")
_VpwrBDTHistEndVoltage_Type = PositiveInteger
_VpwrBDTHistEndVoltage_Object = MibTableColumn
vpwrBDTHistEndVoltage = _VpwrBDTHistEndVoltage_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 4, 12, 1, 10),
    _VpwrBDTHistEndVoltage_Type()
)
vpwrBDTHistEndVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrBDTHistEndVoltage.setStatus("current")
if mibBuilder.loadTexts:
    vpwrBDTHistEndVoltage.setUnits(" *.01 Volts")
_VpwrBDTSchedTable_Object = MibTable
vpwrBDTSchedTable = _VpwrBDTSchedTable_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 4, 13)
)
if mibBuilder.loadTexts:
    vpwrBDTSchedTable.setStatus("current")
_VpwrBDTSchedEntry_Object = MibTableRow
vpwrBDTSchedEntry = _VpwrBDTSchedEntry_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 4, 13, 1)
)
vpwrBDTSchedEntry.setIndexNames(
    (0, "ELTEK-BC2000-DC-POWER-MIB", "vpwrBDTSchedIndex"),
)
if mibBuilder.loadTexts:
    vpwrBDTSchedEntry.setStatus("current")
_VpwrBDTSchedIndex_Type = PositiveInteger
_VpwrBDTSchedIndex_Object = MibTableColumn
vpwrBDTSchedIndex = _VpwrBDTSchedIndex_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 4, 13, 1, 1),
    _VpwrBDTSchedIndex_Type()
)
vpwrBDTSchedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrBDTSchedIndex.setStatus("current")
_VpwrBDTSchedDay_Type = PositiveInteger
_VpwrBDTSchedDay_Object = MibTableColumn
vpwrBDTSchedDay = _VpwrBDTSchedDay_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 4, 13, 1, 2),
    _VpwrBDTSchedDay_Type()
)
vpwrBDTSchedDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrBDTSchedDay.setStatus("current")
_VpwrBDTSchedMonth_Type = PositiveInteger
_VpwrBDTSchedMonth_Object = MibTableColumn
vpwrBDTSchedMonth = _VpwrBDTSchedMonth_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 4, 13, 1, 3),
    _VpwrBDTSchedMonth_Type()
)
vpwrBDTSchedMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrBDTSchedMonth.setStatus("current")
_VpwrBDTSchedHour_Type = PositiveInteger
_VpwrBDTSchedHour_Object = MibTableColumn
vpwrBDTSchedHour = _VpwrBDTSchedHour_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 4, 13, 1, 4),
    _VpwrBDTSchedHour_Type()
)
vpwrBDTSchedHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrBDTSchedHour.setStatus("current")
_VpwrBDTSchedMinute_Type = PositiveInteger
_VpwrBDTSchedMinute_Object = MibTableColumn
vpwrBDTSchedMinute = _VpwrBDTSchedMinute_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 4, 13, 1, 5),
    _VpwrBDTSchedMinute_Type()
)
vpwrBDTSchedMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrBDTSchedMinute.setStatus("current")
_VpwrDcPowerAlarmGroup_ObjectIdentity = ObjectIdentity
vpwrDcPowerAlarmGroup = _VpwrDcPowerAlarmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 8)
)
_VpwrAlarmsPresent_Type = Gauge32
_VpwrAlarmsPresent_Object = MibScalar
vpwrAlarmsPresent = _VpwrAlarmsPresent_Object(
    (1, 3, 6, 1, 4, 1, 13858, 8, 1),
    _VpwrAlarmsPresent_Type()
)
vpwrAlarmsPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrAlarmsPresent.setStatus("current")
_VpwrAlarmTable_Object = MibTable
vpwrAlarmTable = _VpwrAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 13858, 8, 2)
)
if mibBuilder.loadTexts:
    vpwrAlarmTable.setStatus("current")
_VpwrAlarmEntry_Object = MibTableRow
vpwrAlarmEntry = _VpwrAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 13858, 8, 2, 1)
)
vpwrAlarmEntry.setIndexNames(
    (0, "ELTEK-BC2000-DC-POWER-MIB", "vpwrBayIndex"),
    (0, "ELTEK-BC2000-DC-POWER-MIB", "vpwrModuleIndex"),
    (0, "ELTEK-BC2000-DC-POWER-MIB", "vpwrAlarmIndex"),
)
if mibBuilder.loadTexts:
    vpwrAlarmEntry.setStatus("current")
_VpwrAlarmIndex_Type = PositiveInteger
_VpwrAlarmIndex_Object = MibTableColumn
vpwrAlarmIndex = _VpwrAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 13858, 8, 2, 1, 1),
    _VpwrAlarmIndex_Type()
)
vpwrAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrAlarmIndex.setStatus("current")
_VpwrAlarmDescr_Type = AutonomousType
_VpwrAlarmDescr_Object = MibTableColumn
vpwrAlarmDescr = _VpwrAlarmDescr_Object(
    (1, 3, 6, 1, 4, 1, 13858, 8, 2, 1, 2),
    _VpwrAlarmDescr_Type()
)
vpwrAlarmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrAlarmDescr.setStatus("current")
_VpwrAlarmTime_Type = TimeStamp
_VpwrAlarmTime_Object = MibTableColumn
vpwrAlarmTime = _VpwrAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 13858, 8, 2, 1, 3),
    _VpwrAlarmTime_Type()
)
vpwrAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrAlarmTime.setStatus("current")
_SysAlarmConfigTable_Object = MibTable
sysAlarmConfigTable = _SysAlarmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 13858, 8, 3)
)
if mibBuilder.loadTexts:
    sysAlarmConfigTable.setStatus("current")
_SysAlarmConfigEntry_Object = MibTableRow
sysAlarmConfigEntry = _SysAlarmConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 13858, 8, 3, 1)
)
sysAlarmConfigEntry.setIndexNames(
    (0, "ELTEK-BC2000-DC-POWER-MIB", "sysAlarmIndex"),
)
if mibBuilder.loadTexts:
    sysAlarmConfigEntry.setStatus("current")


class _SysAlarmIndex_Type(Integer32):
    """Custom type sysAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SysAlarmIndex_Type.__name__ = "Integer32"
_SysAlarmIndex_Object = MibTableColumn
sysAlarmIndex = _SysAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 13858, 8, 3, 1, 1),
    _SysAlarmIndex_Type()
)
sysAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAlarmIndex.setStatus("current")


class _SysAlarmDefaultName_Type(DisplayString):
    """Custom type sysAlarmDefaultName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_SysAlarmDefaultName_Type.__name__ = "DisplayString"
_SysAlarmDefaultName_Object = MibTableColumn
sysAlarmDefaultName = _SysAlarmDefaultName_Object(
    (1, 3, 6, 1, 4, 1, 13858, 8, 3, 1, 2),
    _SysAlarmDefaultName_Type()
)
sysAlarmDefaultName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAlarmDefaultName.setStatus("current")


class _SysAlarmCustomName_Type(DisplayString):
    """Custom type sysAlarmCustomName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_SysAlarmCustomName_Type.__name__ = "DisplayString"
_SysAlarmCustomName_Object = MibTableColumn
sysAlarmCustomName = _SysAlarmCustomName_Object(
    (1, 3, 6, 1, 4, 1, 13858, 8, 3, 1, 3),
    _SysAlarmCustomName_Type()
)
sysAlarmCustomName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysAlarmCustomName.setStatus("current")


class _SysAlarmSeverity_Type(Integer32):
    """Custom type sysAlarmSeverity based on Integer32"""
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
          ("major", 1),
          ("minor", 2),
          ("majorAndMinor", 3))
    )


_SysAlarmSeverity_Type.__name__ = "Integer32"
_SysAlarmSeverity_Object = MibTableColumn
sysAlarmSeverity = _SysAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 13858, 8, 3, 1, 4),
    _SysAlarmSeverity_Type()
)
sysAlarmSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysAlarmSeverity.setStatus("current")


class _SysAlarmToRelayMapping_Type(DisplayString):
    """Custom type sysAlarmToRelayMapping based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_SysAlarmToRelayMapping_Type.__name__ = "DisplayString"
_SysAlarmToRelayMapping_Object = MibTableColumn
sysAlarmToRelayMapping = _SysAlarmToRelayMapping_Object(
    (1, 3, 6, 1, 4, 1, 13858, 8, 3, 1, 5),
    _SysAlarmToRelayMapping_Type()
)
sysAlarmToRelayMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysAlarmToRelayMapping.setStatus("current")


class _SysAlarmOperStatus_Type(Integer32):
    """Custom type sysAlarmOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_SysAlarmOperStatus_Type.__name__ = "Integer32"
_SysAlarmOperStatus_Object = MibTableColumn
sysAlarmOperStatus = _SysAlarmOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 13858, 8, 3, 1, 6),
    _SysAlarmOperStatus_Type()
)
sysAlarmOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAlarmOperStatus.setStatus("current")


class _SysAlarmComFailState_Type(Integer32):
    """Custom type sysAlarmComFailState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("other", 2))
    )


_SysAlarmComFailState_Type.__name__ = "Integer32"
_SysAlarmComFailState_Object = MibScalar
sysAlarmComFailState = _SysAlarmComFailState_Object(
    (1, 3, 6, 1, 4, 1, 13858, 8, 4),
    _SysAlarmComFailState_Type()
)
sysAlarmComFailState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysAlarmComFailState.setStatus("current")


class _SysAlarmIShareState_Type(Integer32):
    """Custom type sysAlarmIShareState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("other", 2))
    )


_SysAlarmIShareState_Type.__name__ = "Integer32"
_SysAlarmIShareState_Object = MibScalar
sysAlarmIShareState = _SysAlarmIShareState_Object(
    (1, 3, 6, 1, 4, 1, 13858, 8, 5),
    _SysAlarmIShareState_Type()
)
sysAlarmIShareState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysAlarmIShareState.setStatus("current")


class _SysAlarmRedundancyState_Type(Integer32):
    """Custom type sysAlarmRedundancyState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("nPlus1", 1),
          ("nPlus2", 2))
    )


_SysAlarmRedundancyState_Type.__name__ = "Integer32"
_SysAlarmRedundancyState_Object = MibScalar
sysAlarmRedundancyState = _SysAlarmRedundancyState_Object(
    (1, 3, 6, 1, 4, 1, 13858, 8, 6),
    _SysAlarmRedundancyState_Type()
)
sysAlarmRedundancyState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysAlarmRedundancyState.setStatus("current")


class _SysAlarmComFailToACFailState_Type(Integer32):
    """Custom type sysAlarmComFailToACFailState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SysAlarmComFailToACFailState_Type.__name__ = "Integer32"
_SysAlarmComFailToACFailState_Object = MibScalar
sysAlarmComFailToACFailState = _SysAlarmComFailToACFailState_Object(
    (1, 3, 6, 1, 4, 1, 13858, 8, 7),
    _SysAlarmComFailToACFailState_Type()
)
sysAlarmComFailToACFailState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysAlarmComFailToACFailState.setStatus("current")
_VpwrDcPowerSnmpConfig_ObjectIdentity = ObjectIdentity
vpwrDcPowerSnmpConfig = _VpwrDcPowerSnmpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 9)
)
_VpwrTrapTable_Object = MibTable
vpwrTrapTable = _VpwrTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 13858, 9, 1)
)
if mibBuilder.loadTexts:
    vpwrTrapTable.setStatus("current")
_VpwrTrapEntry_Object = MibTableRow
vpwrTrapEntry = _VpwrTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 13858, 9, 1, 1)
)
vpwrTrapEntry.setIndexNames(
    (0, "ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapIpIndex"),
)
if mibBuilder.loadTexts:
    vpwrTrapEntry.setStatus("current")


class _VpwrTrapIpIndex_Type(Integer32):
    """Custom type vpwrTrapIpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VpwrTrapIpIndex_Type.__name__ = "Integer32"
_VpwrTrapIpIndex_Object = MibTableColumn
vpwrTrapIpIndex = _VpwrTrapIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 13858, 9, 1, 1, 1),
    _VpwrTrapIpIndex_Type()
)
vpwrTrapIpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrTrapIpIndex.setStatus("current")
_VpwrTrapIpAddress_Type = IpAddress
_VpwrTrapIpAddress_Object = MibTableColumn
vpwrTrapIpAddress = _VpwrTrapIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 13858, 9, 1, 1, 2),
    _VpwrTrapIpAddress_Type()
)
vpwrTrapIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrTrapIpAddress.setStatus("current")
_VpwrTrapCriticality_Type = Integer32
_VpwrTrapCriticality_Object = MibTableColumn
vpwrTrapCriticality = _VpwrTrapCriticality_Object(
    (1, 3, 6, 1, 4, 1, 13858, 9, 1, 1, 3),
    _VpwrTrapCriticality_Type()
)
vpwrTrapCriticality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrTrapCriticality.setStatus("current")


class _VpwrReadCommunityString_Type(DisplayString):
    """Custom type vpwrReadCommunityString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 8),
    )


_VpwrReadCommunityString_Type.__name__ = "DisplayString"
_VpwrReadCommunityString_Object = MibScalar
vpwrReadCommunityString = _VpwrReadCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 13858, 9, 2),
    _VpwrReadCommunityString_Type()
)
vpwrReadCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrReadCommunityString.setStatus("current")


class _VpwrWriteCommunityString_Type(DisplayString):
    """Custom type vpwrWriteCommunityString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 8),
    )


_VpwrWriteCommunityString_Type.__name__ = "DisplayString"
_VpwrWriteCommunityString_Object = MibScalar
vpwrWriteCommunityString = _VpwrWriteCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 13858, 9, 3),
    _VpwrWriteCommunityString_Type()
)
vpwrWriteCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrWriteCommunityString.setStatus("current")


class _VpwrTrapCommunityString_Type(DisplayString):
    """Custom type vpwrTrapCommunityString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 8),
    )


_VpwrTrapCommunityString_Type.__name__ = "DisplayString"
_VpwrTrapCommunityString_Object = MibScalar
vpwrTrapCommunityString = _VpwrTrapCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 13858, 9, 4),
    _VpwrTrapCommunityString_Type()
)
vpwrTrapCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrTrapCommunityString.setStatus("current")
_VpwrTrapVersion_Type = Integer32
_VpwrTrapVersion_Object = MibScalar
vpwrTrapVersion = _VpwrTrapVersion_Object(
    (1, 3, 6, 1, 4, 1, 13858, 9, 5),
    _VpwrTrapVersion_Type()
)
vpwrTrapVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrTrapVersion.setStatus("current")
_VpwrDcPowerTraps_ObjectIdentity = ObjectIdentity
vpwrDcPowerTraps = _VpwrDcPowerTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 10)
)
_VpwrDcPowerTrapVars_ObjectIdentity = ObjectIdentity
vpwrDcPowerTrapVars = _VpwrDcPowerTrapVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 11)
)


class _VpwrTrapsMsgString_Type(DisplayString):
    """Custom type vpwrTrapsMsgString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_VpwrTrapsMsgString_Type.__name__ = "DisplayString"
_VpwrTrapsMsgString_Object = MibScalar
vpwrTrapsMsgString = _VpwrTrapsMsgString_Object(
    (1, 3, 6, 1, 4, 1, 13858, 11, 1),
    _VpwrTrapsMsgString_Type()
)
vpwrTrapsMsgString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrTrapsMsgString.setStatus("current")
_VpwrTrapUserIpAddress_Type = IpAddress
_VpwrTrapUserIpAddress_Object = MibScalar
vpwrTrapUserIpAddress = _VpwrTrapUserIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 13858, 11, 2),
    _VpwrTrapUserIpAddress_Type()
)
vpwrTrapUserIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vpwrTrapUserIpAddress.setStatus("current")
_VpwrTrapAcfDuration_Type = NonNegativeInteger
_VpwrTrapAcfDuration_Object = MibScalar
vpwrTrapAcfDuration = _VpwrTrapAcfDuration_Object(
    (1, 3, 6, 1, 4, 1, 13858, 11, 3),
    _VpwrTrapAcfDuration_Type()
)
vpwrTrapAcfDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrTrapAcfDuration.setStatus("current")
_VpwrAlarmingSubModuleBitMap_Type = PositiveInteger
_VpwrAlarmingSubModuleBitMap_Object = MibScalar
vpwrAlarmingSubModuleBitMap = _VpwrAlarmingSubModuleBitMap_Object(
    (1, 3, 6, 1, 4, 1, 13858, 11, 4),
    _VpwrAlarmingSubModuleBitMap_Type()
)
vpwrAlarmingSubModuleBitMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrAlarmingSubModuleBitMap.setStatus("current")
_VpwrBatteryCurrentCapacity_Type = PositiveInteger
_VpwrBatteryCurrentCapacity_Object = MibScalar
vpwrBatteryCurrentCapacity = _VpwrBatteryCurrentCapacity_Object(
    (1, 3, 6, 1, 4, 1, 13858, 11, 5),
    _VpwrBatteryCurrentCapacity_Type()
)
vpwrBatteryCurrentCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrBatteryCurrentCapacity.setStatus("current")
_VpwrAlarmingModuleIndex_Type = PositiveInteger
_VpwrAlarmingModuleIndex_Object = MibScalar
vpwrAlarmingModuleIndex = _VpwrAlarmingModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 13858, 11, 6),
    _VpwrAlarmingModuleIndex_Type()
)
vpwrAlarmingModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrAlarmingModuleIndex.setStatus("current")
_VpwrAlarmingModuleOID_Type = ObjectIdentifier
_VpwrAlarmingModuleOID_Object = MibScalar
vpwrAlarmingModuleOID = _VpwrAlarmingModuleOID_Object(
    (1, 3, 6, 1, 4, 1, 13858, 11, 7),
    _VpwrAlarmingModuleOID_Type()
)
vpwrAlarmingModuleOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrAlarmingModuleOID.setStatus("current")
_VpwrAlarmingModuleBitMap_Type = PositiveInteger
_VpwrAlarmingModuleBitMap_Object = MibScalar
vpwrAlarmingModuleBitMap = _VpwrAlarmingModuleBitMap_Object(
    (1, 3, 6, 1, 4, 1, 13858, 11, 8),
    _VpwrAlarmingModuleBitMap_Type()
)
vpwrAlarmingModuleBitMap.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vpwrAlarmingModuleBitMap.setStatus("current")
_VpwrBatteryRemainingTime_Type = PositiveInteger
_VpwrBatteryRemainingTime_Object = MibScalar
vpwrBatteryRemainingTime = _VpwrBatteryRemainingTime_Object(
    (1, 3, 6, 1, 4, 1, 13858, 11, 9),
    _VpwrBatteryRemainingTime_Type()
)
vpwrBatteryRemainingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrBatteryRemainingTime.setStatus("current")
_VpwrDcPowerRinger_ObjectIdentity = ObjectIdentity
vpwrDcPowerRinger = _VpwrDcPowerRinger_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 12)
)
_VpwrRingerConfigGroup_ObjectIdentity = ObjectIdentity
vpwrRingerConfigGroup = _VpwrRingerConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 12, 1)
)


class _VpwrRingerIndex_Type(Integer32):
    """Custom type vpwrRingerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_VpwrRingerIndex_Type.__name__ = "Integer32"
_VpwrRingerIndex_Object = MibScalar
vpwrRingerIndex = _VpwrRingerIndex_Object(
    (1, 3, 6, 1, 4, 1, 13858, 12, 1, 1),
    _VpwrRingerIndex_Type()
)
vpwrRingerIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrRingerIndex.setStatus("current")


class _VpwrRingerParameterAdminState_Type(Integer32):
    """Custom type vpwrRingerParameterAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ringerDisabled", 0),
          ("ringerAOn", 1),
          ("ringerBOn", 2))
    )


_VpwrRingerParameterAdminState_Type.__name__ = "Integer32"
_VpwrRingerParameterAdminState_Object = MibScalar
vpwrRingerParameterAdminState = _VpwrRingerParameterAdminState_Object(
    (1, 3, 6, 1, 4, 1, 13858, 12, 1, 2),
    _VpwrRingerParameterAdminState_Type()
)
vpwrRingerParameterAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrRingerParameterAdminState.setStatus("current")


class _VpwrRingerParameterAcVoltage_Type(Integer32):
    """Custom type vpwrRingerParameterAcVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7000, 10000),
    )


_VpwrRingerParameterAcVoltage_Type.__name__ = "Integer32"
_VpwrRingerParameterAcVoltage_Object = MibScalar
vpwrRingerParameterAcVoltage = _VpwrRingerParameterAcVoltage_Object(
    (1, 3, 6, 1, 4, 1, 13858, 12, 1, 3),
    _VpwrRingerParameterAcVoltage_Type()
)
vpwrRingerParameterAcVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrRingerParameterAcVoltage.setStatus("current")
if mibBuilder.loadTexts:
    vpwrRingerParameterAcVoltage.setUnits(" *.01 Volts")


class _VpwrRingerParameterDcVoltage_Type(Integer32):
    """Custom type vpwrRingerParameterDcVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5500),
    )


_VpwrRingerParameterDcVoltage_Type.__name__ = "Integer32"
_VpwrRingerParameterDcVoltage_Object = MibScalar
vpwrRingerParameterDcVoltage = _VpwrRingerParameterDcVoltage_Object(
    (1, 3, 6, 1, 4, 1, 13858, 12, 1, 4),
    _VpwrRingerParameterDcVoltage_Type()
)
vpwrRingerParameterDcVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrRingerParameterDcVoltage.setStatus("current")
if mibBuilder.loadTexts:
    vpwrRingerParameterDcVoltage.setUnits(" *.01 Volts")


class _VpwrRingerParameterFrequency_Type(Integer32):
    """Custom type vpwrRingerParameterFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(17, 50),
    )


_VpwrRingerParameterFrequency_Type.__name__ = "Integer32"
_VpwrRingerParameterFrequency_Object = MibScalar
vpwrRingerParameterFrequency = _VpwrRingerParameterFrequency_Object(
    (1, 3, 6, 1, 4, 1, 13858, 12, 1, 5),
    _VpwrRingerParameterFrequency_Type()
)
vpwrRingerParameterFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrRingerParameterFrequency.setStatus("current")
if mibBuilder.loadTexts:
    vpwrRingerParameterFrequency.setUnits(" Hz")
_VpwrRingerNumberPresent_Type = Gauge32
_VpwrRingerNumberPresent_Object = MibScalar
vpwrRingerNumberPresent = _VpwrRingerNumberPresent_Object(
    (1, 3, 6, 1, 4, 1, 13858, 12, 1, 6),
    _VpwrRingerNumberPresent_Type()
)
vpwrRingerNumberPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrRingerNumberPresent.setStatus("current")
_VpwrRingerAlarmGroup_ObjectIdentity = ObjectIdentity
vpwrRingerAlarmGroup = _VpwrRingerAlarmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 12, 2)
)
_VpwrRingerAlarmAFailed_ObjectIdentity = ObjectIdentity
vpwrRingerAlarmAFailed = _VpwrRingerAlarmAFailed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 12, 2, 1)
)
if mibBuilder.loadTexts:
    vpwrRingerAlarmAFailed.setStatus("current")
_VpwrRingerAlarmAOverTemp_ObjectIdentity = ObjectIdentity
vpwrRingerAlarmAOverTemp = _VpwrRingerAlarmAOverTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 12, 2, 2)
)
if mibBuilder.loadTexts:
    vpwrRingerAlarmAOverTemp.setStatus("current")
_VpwrRingerAlarmAOverCurrent_ObjectIdentity = ObjectIdentity
vpwrRingerAlarmAOverCurrent = _VpwrRingerAlarmAOverCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 12, 2, 3)
)
if mibBuilder.loadTexts:
    vpwrRingerAlarmAOverCurrent.setStatus("current")
_VpwrRingerAlarmBFailed_ObjectIdentity = ObjectIdentity
vpwrRingerAlarmBFailed = _VpwrRingerAlarmBFailed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 12, 2, 4)
)
if mibBuilder.loadTexts:
    vpwrRingerAlarmBFailed.setStatus("current")
_VpwrRingerAlarmBOverTemp_ObjectIdentity = ObjectIdentity
vpwrRingerAlarmBOverTemp = _VpwrRingerAlarmBOverTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 12, 2, 5)
)
if mibBuilder.loadTexts:
    vpwrRingerAlarmBOverTemp.setStatus("current")
_VpwrRingerAlarmBOverCurrent_ObjectIdentity = ObjectIdentity
vpwrRingerAlarmBOverCurrent = _VpwrRingerAlarmBOverCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 12, 2, 6)
)
if mibBuilder.loadTexts:
    vpwrRingerAlarmBOverCurrent.setStatus("current")
_VpwrRingerTestGroup_ObjectIdentity = ObjectIdentity
vpwrRingerTestGroup = _VpwrRingerTestGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 12, 3)
)
_VpwrDcPowerDcDcConverter_ObjectIdentity = ObjectIdentity
vpwrDcPowerDcDcConverter = _VpwrDcPowerDcDcConverter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 13)
)
_VpwrDcDcConverterConfigGroup_ObjectIdentity = ObjectIdentity
vpwrDcDcConverterConfigGroup = _VpwrDcDcConverterConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 13, 1)
)
_VpwrDcDcConverterAlarmGroup_ObjectIdentity = ObjectIdentity
vpwrDcDcConverterAlarmGroup = _VpwrDcDcConverterAlarmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 13, 2)
)
_VpwrDcDcConverterTestGroup_ObjectIdentity = ObjectIdentity
vpwrDcDcConverterTestGroup = _VpwrDcDcConverterTestGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 13, 3)
)
_VpwrDcPowerDcAcInverter_ObjectIdentity = ObjectIdentity
vpwrDcPowerDcAcInverter = _VpwrDcPowerDcAcInverter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 14)
)
_VpwrDcAcInverterConfigGroup_ObjectIdentity = ObjectIdentity
vpwrDcAcInverterConfigGroup = _VpwrDcAcInverterConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 14, 1)
)
_VpwrDcAcInverterAlarmGroup_ObjectIdentity = ObjectIdentity
vpwrDcAcInverterAlarmGroup = _VpwrDcAcInverterAlarmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 14, 2)
)
_VpwrDcAcInverterTestGroup_ObjectIdentity = ObjectIdentity
vpwrDcAcInverterTestGroup = _VpwrDcAcInverterTestGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 14, 3)
)
_VpwrDcPowerAcLineModule_ObjectIdentity = ObjectIdentity
vpwrDcPowerAcLineModule = _VpwrDcPowerAcLineModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 15)
)
_VpwrAcLineModuleConfigGroup_ObjectIdentity = ObjectIdentity
vpwrAcLineModuleConfigGroup = _VpwrAcLineModuleConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 15, 1)
)
_VpwrAcLineModuleAlarmGroup_ObjectIdentity = ObjectIdentity
vpwrAcLineModuleAlarmGroup = _VpwrAcLineModuleAlarmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 15, 2)
)
_VpwrAcLineModuleTestGroup_ObjectIdentity = ObjectIdentity
vpwrAcLineModuleTestGroup = _VpwrAcLineModuleTestGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 15, 3)
)
_VpwrDcPowerIoModule_ObjectIdentity = ObjectIdentity
vpwrDcPowerIoModule = _VpwrDcPowerIoModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 16)
)
_VpwrIoModuleConfigGroup_ObjectIdentity = ObjectIdentity
vpwrIoModuleConfigGroup = _VpwrIoModuleConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 16, 1)
)
_VpwrIoModuleAlarmGroup_ObjectIdentity = ObjectIdentity
vpwrIoModuleAlarmGroup = _VpwrIoModuleAlarmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 16, 2)
)
_VpwrIoModuleTestGroup_ObjectIdentity = ObjectIdentity
vpwrIoModuleTestGroup = _VpwrIoModuleTestGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 16, 3)
)
_VpwrDcPowerPMModule_ObjectIdentity = ObjectIdentity
vpwrDcPowerPMModule = _VpwrDcPowerPMModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 17)
)
_VpwrPMCnfgTable_Object = MibTable
vpwrPMCnfgTable = _VpwrPMCnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 13858, 17, 1)
)
if mibBuilder.loadTexts:
    vpwrPMCnfgTable.setStatus("current")
_VpwrPMCnfgEntry_Object = MibTableRow
vpwrPMCnfgEntry = _VpwrPMCnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 13858, 17, 1, 1)
)
vpwrPMCnfgEntry.setIndexNames(
    (0, "ELTEK-BC2000-DC-POWER-MIB", "vpwrPMIndex"),
)
if mibBuilder.loadTexts:
    vpwrPMCnfgEntry.setStatus("current")
_VpwrPMIndex_Type = NonNegativeInteger
_VpwrPMIndex_Object = MibTableColumn
vpwrPMIndex = _VpwrPMIndex_Object(
    (1, 3, 6, 1, 4, 1, 13858, 17, 1, 1, 1),
    _VpwrPMIndex_Type()
)
vpwrPMIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrPMIndex.setStatus("current")
_VpwrPMDescription_Type = DisplayString
_VpwrPMDescription_Object = MibTableColumn
vpwrPMDescription = _VpwrPMDescription_Object(
    (1, 3, 6, 1, 4, 1, 13858, 17, 1, 1, 2),
    _VpwrPMDescription_Type()
)
vpwrPMDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrPMDescription.setStatus("current")
_VpwrPMCnfg1_Type = VpwrPMCnfgValue
_VpwrPMCnfg1_Object = MibTableColumn
vpwrPMCnfg1 = _VpwrPMCnfg1_Object(
    (1, 3, 6, 1, 4, 1, 13858, 17, 1, 1, 3),
    _VpwrPMCnfg1_Type()
)
vpwrPMCnfg1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrPMCnfg1.setStatus("current")
_VpwrPMCnfg2_Type = VpwrPMCnfgValue
_VpwrPMCnfg2_Object = MibTableColumn
vpwrPMCnfg2 = _VpwrPMCnfg2_Object(
    (1, 3, 6, 1, 4, 1, 13858, 17, 1, 1, 4),
    _VpwrPMCnfg2_Type()
)
vpwrPMCnfg2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrPMCnfg2.setStatus("current")
_VpwrPMCnfg3_Type = VpwrPMCnfgValue
_VpwrPMCnfg3_Object = MibTableColumn
vpwrPMCnfg3 = _VpwrPMCnfg3_Object(
    (1, 3, 6, 1, 4, 1, 13858, 17, 1, 1, 5),
    _VpwrPMCnfg3_Type()
)
vpwrPMCnfg3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrPMCnfg3.setStatus("current")
_VpwrPMCnfg4_Type = VpwrPMCnfgValue
_VpwrPMCnfg4_Object = MibTableColumn
vpwrPMCnfg4 = _VpwrPMCnfg4_Object(
    (1, 3, 6, 1, 4, 1, 13858, 17, 1, 1, 6),
    _VpwrPMCnfg4_Type()
)
vpwrPMCnfg4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrPMCnfg4.setStatus("current")
_VpwrPMCnfg5_Type = VpwrPMCnfgValue
_VpwrPMCnfg5_Object = MibTableColumn
vpwrPMCnfg5 = _VpwrPMCnfg5_Object(
    (1, 3, 6, 1, 4, 1, 13858, 17, 1, 1, 7),
    _VpwrPMCnfg5_Type()
)
vpwrPMCnfg5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrPMCnfg5.setStatus("current")
_VpwrPMCnfg6_Type = VpwrPMCnfgValue
_VpwrPMCnfg6_Object = MibTableColumn
vpwrPMCnfg6 = _VpwrPMCnfg6_Object(
    (1, 3, 6, 1, 4, 1, 13858, 17, 1, 1, 8),
    _VpwrPMCnfg6_Type()
)
vpwrPMCnfg6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrPMCnfg6.setStatus("current")
_VpwrPMCnfg7_Type = VpwrPMCnfgValue
_VpwrPMCnfg7_Object = MibTableColumn
vpwrPMCnfg7 = _VpwrPMCnfg7_Object(
    (1, 3, 6, 1, 4, 1, 13858, 17, 1, 1, 9),
    _VpwrPMCnfg7_Type()
)
vpwrPMCnfg7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrPMCnfg7.setStatus("current")
_VpwrPMCnfg8_Type = VpwrPMCnfgValue
_VpwrPMCnfg8_Object = MibTableColumn
vpwrPMCnfg8 = _VpwrPMCnfg8_Object(
    (1, 3, 6, 1, 4, 1, 13858, 17, 1, 1, 10),
    _VpwrPMCnfg8_Type()
)
vpwrPMCnfg8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrPMCnfg8.setStatus("current")
_VpwrPMInputStatusTable_Object = MibTable
vpwrPMInputStatusTable = _VpwrPMInputStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 13858, 17, 2)
)
if mibBuilder.loadTexts:
    vpwrPMInputStatusTable.setStatus("current")
_VpwrPMInputStatusEntry_Object = MibTableRow
vpwrPMInputStatusEntry = _VpwrPMInputStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 13858, 17, 2, 1)
)
vpwrPMInputStatusEntry.setIndexNames(
    (0, "ELTEK-BC2000-DC-POWER-MIB", "vpwrPMIndex1"),
)
if mibBuilder.loadTexts:
    vpwrPMInputStatusEntry.setStatus("current")
_VpwrPMIndex1_Type = NonNegativeInteger
_VpwrPMIndex1_Object = MibTableColumn
vpwrPMIndex1 = _VpwrPMIndex1_Object(
    (1, 3, 6, 1, 4, 1, 13858, 17, 2, 1, 1),
    _VpwrPMIndex1_Type()
)
vpwrPMIndex1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrPMIndex1.setStatus("current")
_VpwrPMDescription1_Type = DisplayString
_VpwrPMDescription1_Object = MibTableColumn
vpwrPMDescription1 = _VpwrPMDescription1_Object(
    (1, 3, 6, 1, 4, 1, 13858, 17, 2, 1, 2),
    _VpwrPMDescription1_Type()
)
vpwrPMDescription1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrPMDescription1.setStatus("current")
_VpwrPMInput1State_Type = SysInputValue
_VpwrPMInput1State_Object = MibTableColumn
vpwrPMInput1State = _VpwrPMInput1State_Object(
    (1, 3, 6, 1, 4, 1, 13858, 17, 2, 1, 3),
    _VpwrPMInput1State_Type()
)
vpwrPMInput1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrPMInput1State.setStatus("current")
_VpwrPMInput2State_Type = SysInputValue
_VpwrPMInput2State_Object = MibTableColumn
vpwrPMInput2State = _VpwrPMInput2State_Object(
    (1, 3, 6, 1, 4, 1, 13858, 17, 2, 1, 4),
    _VpwrPMInput2State_Type()
)
vpwrPMInput2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrPMInput2State.setStatus("current")
_VpwrPMInput3State_Type = SysInputValue
_VpwrPMInput3State_Object = MibTableColumn
vpwrPMInput3State = _VpwrPMInput3State_Object(
    (1, 3, 6, 1, 4, 1, 13858, 17, 2, 1, 5),
    _VpwrPMInput3State_Type()
)
vpwrPMInput3State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrPMInput3State.setStatus("current")
_VpwrPMInput4State_Type = SysInputValue
_VpwrPMInput4State_Object = MibTableColumn
vpwrPMInput4State = _VpwrPMInput4State_Object(
    (1, 3, 6, 1, 4, 1, 13858, 17, 2, 1, 6),
    _VpwrPMInput4State_Type()
)
vpwrPMInput4State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrPMInput4State.setStatus("current")
_VpwrPMInput5State_Type = SysInputValue
_VpwrPMInput5State_Object = MibTableColumn
vpwrPMInput5State = _VpwrPMInput5State_Object(
    (1, 3, 6, 1, 4, 1, 13858, 17, 2, 1, 7),
    _VpwrPMInput5State_Type()
)
vpwrPMInput5State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrPMInput5State.setStatus("current")
_VpwrPMInput6State_Type = SysInputValue
_VpwrPMInput6State_Object = MibTableColumn
vpwrPMInput6State = _VpwrPMInput6State_Object(
    (1, 3, 6, 1, 4, 1, 13858, 17, 2, 1, 8),
    _VpwrPMInput6State_Type()
)
vpwrPMInput6State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrPMInput6State.setStatus("current")
_VpwrPMInput7State_Type = SysInputValue
_VpwrPMInput7State_Object = MibTableColumn
vpwrPMInput7State = _VpwrPMInput7State_Object(
    (1, 3, 6, 1, 4, 1, 13858, 17, 2, 1, 9),
    _VpwrPMInput7State_Type()
)
vpwrPMInput7State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrPMInput7State.setStatus("current")
_VpwrPMInput8State_Type = SysInputValue
_VpwrPMInput8State_Object = MibTableColumn
vpwrPMInput8State = _VpwrPMInput8State_Object(
    (1, 3, 6, 1, 4, 1, 13858, 17, 2, 1, 10),
    _VpwrPMInput8State_Type()
)
vpwrPMInput8State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrPMInput8State.setStatus("current")
_VpwrPMRelayCtrlTable_Object = MibTable
vpwrPMRelayCtrlTable = _VpwrPMRelayCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 13858, 17, 3)
)
if mibBuilder.loadTexts:
    vpwrPMRelayCtrlTable.setStatus("current")
_VpwrPMRelayCtrlEntry_Object = MibTableRow
vpwrPMRelayCtrlEntry = _VpwrPMRelayCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 13858, 17, 3, 1)
)
vpwrPMRelayCtrlEntry.setIndexNames(
    (0, "ELTEK-BC2000-DC-POWER-MIB", "vpwrPMIndex2"),
)
if mibBuilder.loadTexts:
    vpwrPMRelayCtrlEntry.setStatus("current")
_VpwrPMIndex2_Type = NonNegativeInteger
_VpwrPMIndex2_Object = MibTableColumn
vpwrPMIndex2 = _VpwrPMIndex2_Object(
    (1, 3, 6, 1, 4, 1, 13858, 17, 3, 1, 1),
    _VpwrPMIndex2_Type()
)
vpwrPMIndex2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrPMIndex2.setStatus("current")
_VpwrPMDescription2_Type = DisplayString
_VpwrPMDescription2_Object = MibTableColumn
vpwrPMDescription2 = _VpwrPMDescription2_Object(
    (1, 3, 6, 1, 4, 1, 13858, 17, 3, 1, 2),
    _VpwrPMDescription2_Type()
)
vpwrPMDescription2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrPMDescription2.setStatus("current")


class _VpwrPMRelay1State_Type(Integer32):
    """Custom type vpwrPMRelay1State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("vpwrPMRelayOff", 0),
          ("vpwrPMRelayOn", 1),
          ("undefined", 255))
    )


_VpwrPMRelay1State_Type.__name__ = "Integer32"
_VpwrPMRelay1State_Object = MibTableColumn
vpwrPMRelay1State = _VpwrPMRelay1State_Object(
    (1, 3, 6, 1, 4, 1, 13858, 17, 3, 1, 3),
    _VpwrPMRelay1State_Type()
)
vpwrPMRelay1State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrPMRelay1State.setStatus("current")


class _VpwrPMRelay2State_Type(Integer32):
    """Custom type vpwrPMRelay2State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("vpwrPMRelayOff", 0),
          ("vpwrPMRelayOn", 1),
          ("undefined", 255))
    )


_VpwrPMRelay2State_Type.__name__ = "Integer32"
_VpwrPMRelay2State_Object = MibTableColumn
vpwrPMRelay2State = _VpwrPMRelay2State_Object(
    (1, 3, 6, 1, 4, 1, 13858, 17, 3, 1, 4),
    _VpwrPMRelay2State_Type()
)
vpwrPMRelay2State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrPMRelay2State.setStatus("current")


class _VpwrPMRelay3State_Type(Integer32):
    """Custom type vpwrPMRelay3State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("vpwrPMRelayOff", 0),
          ("vpwrPMRelayOn", 1),
          ("undefined", 255))
    )


_VpwrPMRelay3State_Type.__name__ = "Integer32"
_VpwrPMRelay3State_Object = MibTableColumn
vpwrPMRelay3State = _VpwrPMRelay3State_Object(
    (1, 3, 6, 1, 4, 1, 13858, 17, 3, 1, 5),
    _VpwrPMRelay3State_Type()
)
vpwrPMRelay3State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrPMRelay3State.setStatus("current")


class _VpwrPMRelay4State_Type(Integer32):
    """Custom type vpwrPMRelay4State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("vpwrPMRelayOff", 0),
          ("vpwrPMRelayOn", 1),
          ("undefined", 255))
    )


_VpwrPMRelay4State_Type.__name__ = "Integer32"
_VpwrPMRelay4State_Object = MibTableColumn
vpwrPMRelay4State = _VpwrPMRelay4State_Object(
    (1, 3, 6, 1, 4, 1, 13858, 17, 3, 1, 6),
    _VpwrPMRelay4State_Type()
)
vpwrPMRelay4State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrPMRelay4State.setStatus("current")


class _VpwrPMRelay5State_Type(Integer32):
    """Custom type vpwrPMRelay5State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("vpwrPMRelayOff", 0),
          ("vpwrPMRelayOn", 1),
          ("undefined", 255))
    )


_VpwrPMRelay5State_Type.__name__ = "Integer32"
_VpwrPMRelay5State_Object = MibTableColumn
vpwrPMRelay5State = _VpwrPMRelay5State_Object(
    (1, 3, 6, 1, 4, 1, 13858, 17, 3, 1, 7),
    _VpwrPMRelay5State_Type()
)
vpwrPMRelay5State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrPMRelay5State.setStatus("current")


class _VpwrPMRelay6State_Type(Integer32):
    """Custom type vpwrPMRelay6State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("vpwrPMRelayOff", 0),
          ("vpwrPMRelayOn", 1),
          ("undefined", 255))
    )


_VpwrPMRelay6State_Type.__name__ = "Integer32"
_VpwrPMRelay6State_Object = MibTableColumn
vpwrPMRelay6State = _VpwrPMRelay6State_Object(
    (1, 3, 6, 1, 4, 1, 13858, 17, 3, 1, 8),
    _VpwrPMRelay6State_Type()
)
vpwrPMRelay6State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrPMRelay6State.setStatus("current")
_VpwrPMModuleAlarmGroup_ObjectIdentity = ObjectIdentity
vpwrPMModuleAlarmGroup = _VpwrPMModuleAlarmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 17, 4)
)
_VpwrPMModuleTestGroup_ObjectIdentity = ObjectIdentity
vpwrPMModuleTestGroup = _VpwrPMModuleTestGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 17, 5)
)
_VpwrDcPowerDistModule_ObjectIdentity = ObjectIdentity
vpwrDcPowerDistModule = _VpwrDcPowerDistModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 18)
)
_VpwrDcPowerBattery_ObjectIdentity = ObjectIdentity
vpwrDcPowerBattery = _VpwrDcPowerBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 19)
)
_VpwrDcPowerController_ObjectIdentity = ObjectIdentity
vpwrDcPowerController = _VpwrDcPowerController_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 20)
)
_VpwrDcPowerUnkModule_ObjectIdentity = ObjectIdentity
vpwrDcPowerUnkModule = _VpwrDcPowerUnkModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 499)
)
_ThirdPartyProduct_ObjectIdentity = ObjectIdentity
thirdPartyProduct = _ThirdPartyProduct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 500)
)

# Managed Objects groups


# Notification objects

vpwrTrapPowerMajorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 1)
)
vpwrTrapPowerMajorAlarm.setObjects(
    ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapPowerMajorAlarm.setStatus(
        "current"
    )

vpwrTrapPowerMinorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 2)
)
vpwrTrapPowerMinorAlarm.setObjects(
    ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapPowerMinorAlarm.setStatus(
        "current"
    )

vpwrTrapACFAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 3)
)
vpwrTrapACFAlarm.setObjects(
    ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapACFAlarm.setStatus(
        "current"
    )

vpwrTrapHVAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 4)
)
vpwrTrapHVAlarm.setObjects(
    ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapHVAlarm.setStatus(
        "current"
    )

vpwrTrapHVSDAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 5)
)
vpwrTrapHVSDAlarm.setObjects(
    ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapHVSDAlarm.setStatus(
        "current"
    )

vpwrTrapBDAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 6)
)
vpwrTrapBDAlarm.setObjects(
    ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapBDAlarm.setStatus(
        "current"
    )

vpwrTrapLVDWarningAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 7)
)
vpwrTrapLVDWarningAlarm.setObjects(
    ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapLVDWarningAlarm.setStatus(
        "current"
    )

vpwrTrapLVDOpenAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 8)
)
vpwrTrapLVDOpenAlarm.setObjects(
    ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapLVDOpenAlarm.setStatus(
        "current"
    )

vpwrTrapDistAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 9)
)
vpwrTrapDistAlarm.setObjects(
    ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapDistAlarm.setStatus(
        "current"
    )

vpwrTrapAuxAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 10)
)
vpwrTrapAuxAlarm.setObjects(
    ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapAuxAlarm.setStatus(
        "current"
    )

vpwrTrapSystemRedundancyAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 11)
)
vpwrTrapSystemRedundancyAlarm.setObjects(
    ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapSystemRedundancyAlarm.setStatus(
        "current"
    )

vpwrTrapIShareAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 12)
)
vpwrTrapIShareAlarm.setObjects(
    ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapIShareAlarm.setStatus(
        "current"
    )

vpwrTrapModuleFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 13)
)
vpwrTrapModuleFailAlarm.setObjects(
    ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapModuleFailAlarm.setStatus(
        "current"
    )

vpwrTrapMultipleModuleFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 14)
)
vpwrTrapMultipleModuleFailAlarm.setObjects(
    ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapMultipleModuleFailAlarm.setStatus(
        "current"
    )

vpwrTrapModuleCommAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 15)
)
vpwrTrapModuleCommAlarm.setObjects(
    ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapModuleCommAlarm.setStatus(
        "current"
    )

vpwrTrapSystemOverTemperatureAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 16)
)
vpwrTrapSystemOverTemperatureAlarm.setObjects(
    ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapSystemOverTemperatureAlarm.setStatus(
        "current"
    )

vpwrTrapSystemOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 17)
)
vpwrTrapSystemOK.setObjects(
    ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapSystemOK.setStatus(
        "current"
    )

vpwrTrapModuleInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 18)
)
vpwrTrapModuleInserted.setObjects(
      *(("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString"),
        ("ELTEK-BC2000-DC-POWER-MIB", "vpwrBayIndex"),
        ("ELTEK-BC2000-DC-POWER-MIB", "vpwrModuleIndex"))
)
if mibBuilder.loadTexts:
    vpwrTrapModuleInserted.setStatus(
        "current"
    )

vpwrTrapModuleRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 19)
)
vpwrTrapModuleRemoved.setObjects(
      *(("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString"),
        ("ELTEK-BC2000-DC-POWER-MIB", "vpwrBayIndex"),
        ("ELTEK-BC2000-DC-POWER-MIB", "vpwrModuleIndex"))
)
if mibBuilder.loadTexts:
    vpwrTrapModuleRemoved.setStatus(
        "current"
    )

vpwrTrapThermalCompActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 20)
)
vpwrTrapThermalCompActive.setObjects(
    ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapThermalCompActive.setStatus(
        "current"
    )

vpwrTrapThermalCompInactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 21)
)
vpwrTrapThermalCompInactive.setObjects(
    ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapThermalCompInactive.setStatus(
        "current"
    )

vpwrTrapInternalTempAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 22)
)
vpwrTrapInternalTempAlarmSet.setObjects(
    ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapInternalTempAlarmSet.setStatus(
        "current"
    )

vpwrTrapInternalTempAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 23)
)
vpwrTrapInternalTempAlarmCleared.setObjects(
    ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapInternalTempAlarmCleared.setStatus(
        "current"
    )

vpwrTrapBatteryTempAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 24)
)
vpwrTrapBatteryTempAlarmSet.setObjects(
    ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapBatteryTempAlarmSet.setStatus(
        "current"
    )

vpwrTrapBatteryTempAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 25)
)
vpwrTrapBatteryTempAlarmCleared.setObjects(
    ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapBatteryTempAlarmCleared.setStatus(
        "current"
    )

vpwrTrapLoginFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 26)
)
vpwrTrapLoginFail.setObjects(
    ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapLoginFail.setStatus(
        "current"
    )

vpwrTrapLoginSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 27)
)
vpwrTrapLoginSuccess.setObjects(
    ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapLoginSuccess.setStatus(
        "current"
    )

vpwrTrapLogout = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 28)
)
vpwrTrapLogout.setObjects(
    ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapLogout.setStatus(
        "current"
    )

vpwrTrapAdminPwdChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 29)
)
vpwrTrapAdminPwdChange.setObjects(
    ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapAdminPwdChange.setStatus(
        "current"
    )

vpwrTrapIllegalConfigSubmit = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 30)
)
vpwrTrapIllegalConfigSubmit.setObjects(
    ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapIllegalConfigSubmit.setStatus(
        "current"
    )

vpwrTrapCfgChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 31)
)
vpwrTrapCfgChange.setObjects(
    ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapCfgChange.setStatus(
        "current"
    )

vpwrTrapClearEventHistory = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 32)
)
vpwrTrapClearEventHistory.setObjects(
    ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapClearEventHistory.setStatus(
        "current"
    )

vpwrTrapSwDownloadNoReboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 33)
)
vpwrTrapSwDownloadNoReboot.setObjects(
    ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapSwDownloadNoReboot.setStatus(
        "current"
    )

vpwrTrapSwDownloadAndReboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 34)
)
vpwrTrapSwDownloadAndReboot.setObjects(
    ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapSwDownloadAndReboot.setStatus(
        "current"
    )

vpwrTrapSystemClockChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 35)
)
vpwrTrapSystemClockChange.setObjects(
    ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapSystemClockChange.setStatus(
        "current"
    )

vpwrTrapModuleAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 36)
)
vpwrTrapModuleAlarm.setObjects(
    ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapModuleAlarm.setStatus(
        "current"
    )

vpwrTrapOIDChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 37)
)
vpwrTrapOIDChange.setObjects(
    ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapOIDChange.setStatus(
        "current"
    )

vpwrTrapThermalRunaway = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 38)
)
vpwrTrapThermalRunaway.setObjects(
    ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapThermalRunaway.setStatus(
        "current"
    )

vpwrTrapBatteryDischargeTestAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 39)
)
vpwrTrapBatteryDischargeTestAlarm.setObjects(
    ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapBatteryDischargeTestAlarm.setStatus(
        "current"
    )

vpwrTrapBayUnnameAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 40)
)
vpwrTrapBayUnnameAlarm.setObjects(
    ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapBayUnnameAlarm.setStatus(
        "current"
    )

vpwrTrapPMComFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 41)
)
vpwrTrapPMComFailAlarm.setObjects(
    ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapPMComFailAlarm.setStatus(
        "current"
    )

vpwrTrapFuseOverloadAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 42)
)
vpwrTrapFuseOverloadAlarm.setObjects(
    ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapFuseOverloadAlarm.setStatus(
        "current"
    )

vpwrTrapPeripheralAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 43)
)
vpwrTrapPeripheralAlarm.setObjects(
    ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapPeripheralAlarm.setStatus(
        "current"
    )

vpwrTrapThermalProbeAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 44)
)
vpwrTrapThermalProbeAlarm.setObjects(
    ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapThermalProbeAlarm.setStatus(
        "current"
    )

vpwrTrapBayCommAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 45)
)
vpwrTrapBayCommAlarm.setObjects(
    ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapBayCommAlarm.setStatus(
        "current"
    )

vpwrTrapDistributionCommAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 46)
)
vpwrTrapDistributionCommAlarm.setObjects(
    ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapDistributionCommAlarm.setStatus(
        "current"
    )

vpwrTrapConverterAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 47)
)
vpwrTrapConverterAlarm.setObjects(
    ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapConverterAlarm.setStatus(
        "current"
    )

vpwrTrapMultipleConvFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 48)
)
vpwrTrapMultipleConvFailAlarm.setObjects(
    ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapMultipleConvFailAlarm.setStatus(
        "current"
    )

vpwrTrapDGUAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 49)
)
vpwrTrapDGUAlarm.setObjects(
    ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapDGUAlarm.setStatus(
        "current"
    )

vpwrTrapConfigErrorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 50)
)
vpwrTrapConfigErrorAlarm.setObjects(
    ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapConfigErrorAlarm.setStatus(
        "current"
    )

vpwrTrapDisplayFirmwareMismatchAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 51)
)
vpwrTrapDisplayFirmwareMismatchAlarm.setObjects(
    ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapDisplayFirmwareMismatchAlarm.setStatus(
        "current"
    )

vpwrTrapConverterInputFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 52)
)
vpwrTrapConverterInputFailAlarm.setObjects(
    ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapConverterInputFailAlarm.setStatus(
        "current"
    )

vpwrTrapBatteryRechgIlimitFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 53)
)
vpwrTrapBatteryRechgIlimitFailAlarm.setObjects(
    ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapBatteryRechgIlimitFailAlarm.setStatus(
        "current"
    )

vpwrTrapSystemAlive = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 54)
)
vpwrTrapSystemAlive.setObjects(
    ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapSystemAlive.setStatus(
        "current"
    )

vpwrTrapSystemAuxAlmSource = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 55)
)
vpwrTrapSystemAuxAlmSource.setObjects(
      *(("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString"),
        ("ELTEK-BC2000-DC-POWER-MIB", "vpwrAlarmingModuleOID"),
        ("ELTEK-BC2000-DC-POWER-MIB", "vpwrAlarmingModuleIndex"),
        ("ELTEK-BC2000-DC-POWER-MIB", "vpwrAlarmingSubModuleBitMap"))
)
if mibBuilder.loadTexts:
    vpwrTrapSystemAuxAlmSource.setStatus(
        "current"
    )

vpwrTrapSystemDistAlmSource = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 56)
)
vpwrTrapSystemDistAlmSource.setObjects(
      *(("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString"),
        ("ELTEK-BC2000-DC-POWER-MIB", "vpwrAlarmingModuleOID"),
        ("ELTEK-BC2000-DC-POWER-MIB", "vpwrAlarmingModuleIndex"),
        ("ELTEK-BC2000-DC-POWER-MIB", "vpwrAlarmingSubModuleBitMap"))
)
if mibBuilder.loadTexts:
    vpwrTrapSystemDistAlmSource.setStatus(
        "current"
    )

vpwrTrapSystemBatCapacityAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 58)
)
vpwrTrapSystemBatCapacityAlarm.setObjects(
      *(("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString"),
        ("ELTEK-BC2000-DC-POWER-MIB", "vpwrSystemCurrent"),
        ("ELTEK-BC2000-DC-POWER-MIB", "vpwrBatteryCurrentCapacity"))
)
if mibBuilder.loadTexts:
    vpwrTrapSystemBatCapacityAlarm.setStatus(
        "current"
    )

vpwrTrapSystemACFClearAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 61)
)
vpwrTrapSystemACFClearAlarm.setObjects(
      *(("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString"),
        ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapAcfDuration"))
)
if mibBuilder.loadTexts:
    vpwrTrapSystemACFClearAlarm.setStatus(
        "current"
    )

vpwrTrapSystemACFSetAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 62)
)
vpwrTrapSystemACFSetAlarm.setObjects(
      *(("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString"),
        ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapAcfDuration"))
)
if mibBuilder.loadTexts:
    vpwrTrapSystemACFSetAlarm.setStatus(
        "current"
    )

vpwrTrapSystemBatCapacityLeft = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 64)
)
vpwrTrapSystemBatCapacityLeft.setObjects(
      *(("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString"),
        ("ELTEK-BC2000-DC-POWER-MIB", "vpwrBatteryRemainingTime"))
)
if mibBuilder.loadTexts:
    vpwrTrapSystemBatCapacityLeft.setStatus(
        "current"
    )

vpwrTrapRectifierUVAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 65)
)
vpwrTrapRectifierUVAlarm.setObjects(
      *(("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString"),
        ("ELTEK-BC2000-DC-POWER-MIB", "vpwrBayIndex"),
        ("ELTEK-BC2000-DC-POWER-MIB", "vpwrModuleIndex"))
)
if mibBuilder.loadTexts:
    vpwrTrapRectifierUVAlarm.setStatus(
        "current"
    )

vpwrTrapMultRectifierUVAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 66)
)
vpwrTrapMultRectifierUVAlarm.setObjects(
    ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapMultRectifierUVAlarm.setStatus(
        "current"
    )

vpwrTrapRingerAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 67)
)
vpwrTrapRingerAlarm.setObjects(
    ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapRingerAlarm.setStatus(
        "current"
    )

vpwrTrapMultRingerAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 68)
)
vpwrTrapMultRingerAlarm.setObjects(
    ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapMultRingerAlarm.setStatus(
        "current"
    )

vpwrTrapI2CCANAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 69)
)
vpwrTrapI2CCANAlarm.setObjects(
    ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapI2CCANAlarm.setStatus(
        "current"
    )

vpwrTrapRectifierIlimitAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 70)
)
vpwrTrapRectifierIlimitAlarm.setObjects(
      *(("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString"),
        ("ELTEK-BC2000-DC-POWER-MIB", "vpwrBayIndex"),
        ("ELTEK-BC2000-DC-POWER-MIB", "vpwrModuleIndex"))
)
if mibBuilder.loadTexts:
    vpwrTrapRectifierIlimitAlarm.setStatus(
        "current"
    )

vpwrTrapMultRectifierIlimitAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 71)
)
vpwrTrapMultRectifierIlimitAlarm.setObjects(
    ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapMultRectifierIlimitAlarm.setStatus(
        "current"
    )

vpwrTrapRingerCommAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 72)
)
vpwrTrapRingerCommAlarm.setObjects(
    ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapRingerCommAlarm.setStatus(
        "current"
    )

vpwrTrapUnassignedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 99)
)
vpwrTrapUnassignedAlarm.setObjects(
    ("ELTEK-BC2000-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapUnassignedAlarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEK-BC2000-DC-POWER-MIB",
    **{"PositiveInteger": PositiveInteger,
       "NonNegativeInteger": NonNegativeInteger,
       "GenericEnableDisableTC": GenericEnableDisableTC,
       "SysInputValue": SysInputValue,
       "VpwrPMCnfgValue": VpwrPMCnfgValue,
       "BDTStartSourceTC": BDTStartSourceTC,
       "BDTResultTC": BDTResultTC,
       "eltek": eltek,
       "vpwrDcPowerSystem": vpwrDcPowerSystem,
       "vpwrSystemIdentGroup": vpwrSystemIdentGroup,
       "vpwrIdentManufacturer": vpwrIdentManufacturer,
       "vpwrIdentModel": vpwrIdentModel,
       "vpwrIdentControllerVersion": vpwrIdentControllerVersion,
       "vpwrIdentAgentSoftwareVersion": vpwrIdentAgentSoftwareVersion,
       "vpwrIdentName": vpwrIdentName,
       "vpwrSystemIdentTable": vpwrSystemIdentTable,
       "vpwrSystemIdentEntry": vpwrSystemIdentEntry,
       "vpwrBayIndex": vpwrBayIndex,
       "vpwrModuleIndex": vpwrModuleIndex,
       "vpwrModuleOID": vpwrModuleOID,
       "vpwrModuleCurrent": vpwrModuleCurrent,
       "vpwrModuleOperStatus": vpwrModuleOperStatus,
       "vpwrModuleCapacity": vpwrModuleCapacity,
       "vpwrSystemConfigGroup": vpwrSystemConfigGroup,
       "vpwrSystemTempCompensation": vpwrSystemTempCompensation,
       "vpwrSystemTempCompStartTemperature": vpwrSystemTempCompStartTemperature,
       "vpwrSystemTempCompStopVoltage": vpwrSystemTempCompStopVoltage,
       "vpwrSystemTempCompensationSlope": vpwrSystemTempCompensationSlope,
       "vpwrSystemThermalSenseType": vpwrSystemThermalSenseType,
       "vpwrSystemHVAlarmSetpoint": vpwrSystemHVAlarmSetpoint,
       "vpwrSystemBDAlarmSetpoint": vpwrSystemBDAlarmSetpoint,
       "vpwrSystemInternalTempLThreshold": vpwrSystemInternalTempLThreshold,
       "vpwrSystemInternalTempUThreshold": vpwrSystemInternalTempUThreshold,
       "vpwrSystemParameterGroup": vpwrSystemParameterGroup,
       "vpwrSystemShelfCapacity": vpwrSystemShelfCapacity,
       "vpwrSystemVoltage": vpwrSystemVoltage,
       "vpwrSystemCurrent": vpwrSystemCurrent,
       "vpwrSystemControllerState": vpwrSystemControllerState,
       "vpwrSystemInternalTemperature": vpwrSystemInternalTemperature,
       "vpwrSystemTempCompensationState": vpwrSystemTempCompensationState,
       "vpwrSystemType": vpwrSystemType,
       "vpwrSystemCumulativeUpTime": vpwrSystemCumulativeUpTime,
       "vpwrSystemBatteryRemainingTime": vpwrSystemBatteryRemainingTime,
       "vpwrSystemPanelIdentGroup": vpwrSystemPanelIdentGroup,
       "vpwrPanelStatusTable": vpwrPanelStatusTable,
       "vpwrPanelStatus": vpwrPanelStatus,
       "vpwrPanelStatusIndex": vpwrPanelStatusIndex,
       "vpwrPanelStatusModuleIndex": vpwrPanelStatusModuleIndex,
       "vpwrPanelStatusModuleOID": vpwrPanelStatusModuleOID,
       "vpwrPanelStatusModuleCurrent": vpwrPanelStatusModuleCurrent,
       "vpwrpanelStatusModuleOperStatus": vpwrpanelStatusModuleOperStatus,
       "vpwrPanelStatusModuleCapacity": vpwrPanelStatusModuleCapacity,
       "vpwrPanelIdentTable": vpwrPanelIdentTable,
       "vpwrPanelIdentEntry": vpwrPanelIdentEntry,
       "vpwrPanelIndex": vpwrPanelIndex,
       "vpwrPanelModuleIndex": vpwrPanelModuleIndex,
       "vpwrPanelModuleSerNum": vpwrPanelModuleSerNum,
       "vpwrPanelModuleModelName": vpwrPanelModuleModelName,
       "vpwrPanelModuleFWVer": vpwrPanelModuleFWVer,
       "vpwrPanelModuleTestDate": vpwrPanelModuleTestDate,
       "vpwrSystemHistoryGroup": vpwrSystemHistoryGroup,
       "vpwrSysHistAlarmTable": vpwrSysHistAlarmTable,
       "vpwrSysHistAlarmEntry": vpwrSysHistAlarmEntry,
       "vpwrSysHistAlarmIndex": vpwrSysHistAlarmIndex,
       "vpwrSysHistAlarmDescription": vpwrSysHistAlarmDescription,
       "vpwrSystemAlarmGroup": vpwrSystemAlarmGroup,
       "vpwrSystemAlarmMajor": vpwrSystemAlarmMajor,
       "vpwrSystemAlarmMinor": vpwrSystemAlarmMinor,
       "vpwrSystemACFailAlarm": vpwrSystemACFailAlarm,
       "vpwrSystemHighVoltageWarningAlarm": vpwrSystemHighVoltageWarningAlarm,
       "vpwrSystemHighVoltageShutdownAlarm": vpwrSystemHighVoltageShutdownAlarm,
       "vpwrSystemBatteryonDischargeAlarm": vpwrSystemBatteryonDischargeAlarm,
       "vpwrSystemLowVoltageWarningAlarm": vpwrSystemLowVoltageWarningAlarm,
       "vpwrSystemLVDOpenAlarm": vpwrSystemLVDOpenAlarm,
       "vpwrSystemDistributionAlarm": vpwrSystemDistributionAlarm,
       "vpwrSystemAuxiliaryAlarm": vpwrSystemAuxiliaryAlarm,
       "vpwrSystemRedundantCapAlarm": vpwrSystemRedundantCapAlarm,
       "vpwrSystemRectIShareAlarm": vpwrSystemRectIShareAlarm,
       "vpwrSystemSnglRectAlarm": vpwrSystemSnglRectAlarm,
       "vpwrSystemMultRectAlarm": vpwrSystemMultRectAlarm,
       "vpwrSystemModlCommAlarm": vpwrSystemModlCommAlarm,
       "vpwrSystemOverTempAlarm": vpwrSystemOverTempAlarm,
       "vpwrSystemThermRAAlarm": vpwrSystemThermRAAlarm,
       "vpwrSystemBDTAlarm": vpwrSystemBDTAlarm,
       "vpwrSystemRectUVAlarm": vpwrSystemRectUVAlarm,
       "vpwrSystemMultRectUVAlarm": vpwrSystemMultRectUVAlarm,
       "vpwrSystemSnglRngrAlarm": vpwrSystemSnglRngrAlarm,
       "vpwrSystemMultRngrAlarm": vpwrSystemMultRngrAlarm,
       "vpwrSystemTempProbeAlarm": vpwrSystemTempProbeAlarm,
       "vpwrSystemRngrCommAlarm": vpwrSystemRngrCommAlarm,
       "vpwrSystemDistPMCommAlarm": vpwrSystemDistPMCommAlarm,
       "vpwrSystemRectILimitAlarm": vpwrSystemRectILimitAlarm,
       "vpwrSystemMultRectILimitAlarm": vpwrSystemMultRectILimitAlarm,
       "vpwrSystemUnmappedI2CCANAlarm": vpwrSystemUnmappedI2CCANAlarm,
       "vpwrSystemConfigErrAlarm": vpwrSystemConfigErrAlarm,
       "vpwrSystemDispFWAlarm": vpwrSystemDispFWAlarm,
       "vpwrSystemUndefinedAlarm": vpwrSystemUndefinedAlarm,
       "vpwrDcPowerRectifier": vpwrDcPowerRectifier,
       "vpwrRectifierConfigGroup": vpwrRectifierConfigGroup,
       "vpwrRectifierFVSetpoint": vpwrRectifierFVSetpoint,
       "vpwrRectifierHVSDSetpoint": vpwrRectifierHVSDSetpoint,
       "vpwrRectifierCurrentLimitAdminState": vpwrRectifierCurrentLimitAdminState,
       "vpwrRectifierCurrentLimit": vpwrRectifierCurrentLimit,
       "vpwrRectifierFallbackAdminState": vpwrRectifierFallbackAdminState,
       "vpwrRectifierFallbackVoltage": vpwrRectifierFallbackVoltage,
       "vpwrRectifierAlarmGroup": vpwrRectifierAlarmGroup,
       "vpwrRectAlarmDCFail": vpwrRectAlarmDCFail,
       "vpwrRectAlarmBoostFail": vpwrRectAlarmBoostFail,
       "vpwrRectAlarmACFail": vpwrRectAlarmACFail,
       "vpwrRectAlarmHVSD": vpwrRectAlarmHVSD,
       "vpwrRectAlarmFanFail": vpwrRectAlarmFanFail,
       "vpwrRectAlarmAmbTemp": vpwrRectAlarmAmbTemp,
       "vpwrRectAlarmIntTemp": vpwrRectAlarmIntTemp,
       "vpwrRectAlarmIShare": vpwrRectAlarmIShare,
       "vpwrRectAlarmUV": vpwrRectAlarmUV,
       "vpwrRectAlarmLowVoltage": vpwrRectAlarmLowVoltage,
       "vpwrRectAlarmReserved": vpwrRectAlarmReserved,
       "vpwrRectAlarmDCEnable": vpwrRectAlarmDCEnable,
       "vpwrRectAlarmRemoteShutdown": vpwrRectAlarmRemoteShutdown,
       "vpwrRectAlarmModDisableShutdown": vpwrRectAlarmModDisableShutdown,
       "vpwrRectAlarmShortPinShutdown": vpwrRectAlarmShortPinShutdown,
       "vpwrRectAlarmBoostComm": vpwrRectAlarmBoostComm,
       "vpwrDcPowerLvd": vpwrDcPowerLvd,
       "vpwrLvdConfigGroup": vpwrLvdConfigGroup,
       "vpwrLvdWarningSetpoint": vpwrLvdWarningSetpoint,
       "vpwrLvdDisconnectSetpoint": vpwrLvdDisconnectSetpoint,
       "vpwrLvdReconnectSetpoint": vpwrLvdReconnectSetpoint,
       "vpwrLvdReconnectDelayTimer": vpwrLvdReconnectDelayTimer,
       "vpwrLvd2DisconnectSetpoint": vpwrLvd2DisconnectSetpoint,
       "vpwrLvd2ReconnectSetpoint": vpwrLvd2ReconnectSetpoint,
       "vpwrLvd2ReconnectDelayTimer": vpwrLvd2ReconnectDelayTimer,
       "vpwrLvd3DisconnectSetpoint": vpwrLvd3DisconnectSetpoint,
       "vpwrLvd3ReconnectSetpoint": vpwrLvd3ReconnectSetpoint,
       "vpwrLvd3ReconnectDelayTimer": vpwrLvd3ReconnectDelayTimer,
       "vpwrLvd4DisconnectSetpoint": vpwrLvd4DisconnectSetpoint,
       "vpwrLvd4ReconnectSetpoint": vpwrLvd4ReconnectSetpoint,
       "vpwrLvd4ReconnectDelayTimer": vpwrLvd4ReconnectDelayTimer,
       "vpwrDCPowerLampTest": vpwrDCPowerLampTest,
       "vpwrDcPowerModuleIdent": vpwrDcPowerModuleIdent,
       "vpwrDcPowerModuleIdentTable": vpwrDcPowerModuleIdentTable,
       "vpwrDcPowerModuleIdentEntry": vpwrDcPowerModuleIdentEntry,
       "vpwrBayIndex1": vpwrBayIndex1,
       "vpwrDCModuleIndex": vpwrDCModuleIndex,
       "vpwrModuleSerialNumber": vpwrModuleSerialNumber,
       "vpwrModuleModelNumber": vpwrModuleModelNumber,
       "vpwrModuleFwVersion": vpwrModuleFwVersion,
       "vpwrModuleTestDate": vpwrModuleTestDate,
       "vpwrModuleOperHours": vpwrModuleOperHours,
       "vpwrDcPowerBatteryGroup": vpwrDcPowerBatteryGroup,
       "vpwrBatteryTempGroup": vpwrBatteryTempGroup,
       "vpwrBatteryTempTable": vpwrBatteryTempTable,
       "vpwrBatteryTempEntry": vpwrBatteryTempEntry,
       "vpwrBatteryTempIndex": vpwrBatteryTempIndex,
       "vpwrBatteryTempName": vpwrBatteryTempName,
       "vpwrBatteryTemp": vpwrBatteryTemp,
       "vpwrBatteryTempLThreshold": vpwrBatteryTempLThreshold,
       "vpwrBatteryTempUThreshold": vpwrBatteryTempUThreshold,
       "batteryTempCompensation": batteryTempCompensation,
       "batteryTempCompHighStartTemperature": batteryTempCompHighStartTemperature,
       "batteryTempCompHighStopVoltage": batteryTempCompHighStopVoltage,
       "batteryTempCompHighSlope": batteryTempCompHighSlope,
       "batteryTempCompLowStartTemperature": batteryTempCompLowStartTemperature,
       "batteryTempCompLowStopVoltage": batteryTempCompLowStopVoltage,
       "batteryTempCompLowSlope": batteryTempCompLowSlope,
       "batteryTempCompRunawayTemperature": batteryTempCompRunawayTemperature,
       "batteryTempCompRunawayStopVoltage": batteryTempCompRunawayStopVoltage,
       "batteryTempCompSenseSource": batteryTempCompSenseSource,
       "batteryTempCompRunawayState": batteryTempCompRunawayState,
       "vpwrBatteryCurrentGroup": vpwrBatteryCurrentGroup,
       "vpwrBatteryCurrentLimitAdminState": vpwrBatteryCurrentLimitAdminState,
       "vpwrBatteryCurrentLimit": vpwrBatteryCurrentLimit,
       "vpwrBatteryCurrent": vpwrBatteryCurrent,
       "vpwrBatteryBoostGroup": vpwrBatteryBoostGroup,
       "vpwrBoostAdminState": vpwrBoostAdminState,
       "vpwrBoostVoltage": vpwrBoostVoltage,
       "vpwrBoostDuration": vpwrBoostDuration,
       "vpwrBoostOperState": vpwrBoostOperState,
       "vpwrBatteryDischargeTestGroup": vpwrBatteryDischargeTestGroup,
       "vpwrBDTAdminState": vpwrBDTAdminState,
       "vpwrBDTDuration": vpwrBDTDuration,
       "vpwrBDTAlarmVoltage": vpwrBDTAlarmVoltage,
       "vpwrBDTAbortVoltage": vpwrBDTAbortVoltage,
       "vpwrBDTAlarmCoefficient": vpwrBDTAlarmCoefficient,
       "vpwrBDTOperState": vpwrBDTOperState,
       "vpwrBDTClearAlarm": vpwrBDTClearAlarm,
       "vpwrBDTActualTime": vpwrBDTActualTime,
       "vpwrBDTAlarmDelay": vpwrBDTAlarmDelay,
       "vpwrBDTResult": vpwrBDTResult,
       "vpwrBDTAutoAdminState": vpwrBDTAutoAdminState,
       "vpwrBDTHistTable": vpwrBDTHistTable,
       "vpwrBDTHistEntry": vpwrBDTHistEntry,
       "vpwrBDTHistIndex": vpwrBDTHistIndex,
       "vpwrBDTHistDateTime": vpwrBDTHistDateTime,
       "vpwrBDTHistDuration": vpwrBDTHistDuration,
       "vpwrBDTHistAlarmVoltage": vpwrBDTHistAlarmVoltage,
       "vpwrBDTHistAbortVoltage": vpwrBDTHistAbortVoltage,
       "vpwrBDTHistStartMethod": vpwrBDTHistStartMethod,
       "vpwrBDTHistResult": vpwrBDTHistResult,
       "vpwrBDTHistActualTime": vpwrBDTHistActualTime,
       "vpwrBDTHistStartVoltage": vpwrBDTHistStartVoltage,
       "vpwrBDTHistEndVoltage": vpwrBDTHistEndVoltage,
       "vpwrBDTSchedTable": vpwrBDTSchedTable,
       "vpwrBDTSchedEntry": vpwrBDTSchedEntry,
       "vpwrBDTSchedIndex": vpwrBDTSchedIndex,
       "vpwrBDTSchedDay": vpwrBDTSchedDay,
       "vpwrBDTSchedMonth": vpwrBDTSchedMonth,
       "vpwrBDTSchedHour": vpwrBDTSchedHour,
       "vpwrBDTSchedMinute": vpwrBDTSchedMinute,
       "vpwrDcPowerAlarmGroup": vpwrDcPowerAlarmGroup,
       "vpwrAlarmsPresent": vpwrAlarmsPresent,
       "vpwrAlarmTable": vpwrAlarmTable,
       "vpwrAlarmEntry": vpwrAlarmEntry,
       "vpwrAlarmIndex": vpwrAlarmIndex,
       "vpwrAlarmDescr": vpwrAlarmDescr,
       "vpwrAlarmTime": vpwrAlarmTime,
       "sysAlarmConfigTable": sysAlarmConfigTable,
       "sysAlarmConfigEntry": sysAlarmConfigEntry,
       "sysAlarmIndex": sysAlarmIndex,
       "sysAlarmDefaultName": sysAlarmDefaultName,
       "sysAlarmCustomName": sysAlarmCustomName,
       "sysAlarmSeverity": sysAlarmSeverity,
       "sysAlarmToRelayMapping": sysAlarmToRelayMapping,
       "sysAlarmOperStatus": sysAlarmOperStatus,
       "sysAlarmComFailState": sysAlarmComFailState,
       "sysAlarmIShareState": sysAlarmIShareState,
       "sysAlarmRedundancyState": sysAlarmRedundancyState,
       "sysAlarmComFailToACFailState": sysAlarmComFailToACFailState,
       "vpwrDcPowerSnmpConfig": vpwrDcPowerSnmpConfig,
       "vpwrTrapTable": vpwrTrapTable,
       "vpwrTrapEntry": vpwrTrapEntry,
       "vpwrTrapIpIndex": vpwrTrapIpIndex,
       "vpwrTrapIpAddress": vpwrTrapIpAddress,
       "vpwrTrapCriticality": vpwrTrapCriticality,
       "vpwrReadCommunityString": vpwrReadCommunityString,
       "vpwrWriteCommunityString": vpwrWriteCommunityString,
       "vpwrTrapCommunityString": vpwrTrapCommunityString,
       "vpwrTrapVersion": vpwrTrapVersion,
       "vpwrDcPowerTraps": vpwrDcPowerTraps,
       "vpwrTrapPowerMajorAlarm": vpwrTrapPowerMajorAlarm,
       "vpwrTrapPowerMinorAlarm": vpwrTrapPowerMinorAlarm,
       "vpwrTrapACFAlarm": vpwrTrapACFAlarm,
       "vpwrTrapHVAlarm": vpwrTrapHVAlarm,
       "vpwrTrapHVSDAlarm": vpwrTrapHVSDAlarm,
       "vpwrTrapBDAlarm": vpwrTrapBDAlarm,
       "vpwrTrapLVDWarningAlarm": vpwrTrapLVDWarningAlarm,
       "vpwrTrapLVDOpenAlarm": vpwrTrapLVDOpenAlarm,
       "vpwrTrapDistAlarm": vpwrTrapDistAlarm,
       "vpwrTrapAuxAlarm": vpwrTrapAuxAlarm,
       "vpwrTrapSystemRedundancyAlarm": vpwrTrapSystemRedundancyAlarm,
       "vpwrTrapIShareAlarm": vpwrTrapIShareAlarm,
       "vpwrTrapModuleFailAlarm": vpwrTrapModuleFailAlarm,
       "vpwrTrapMultipleModuleFailAlarm": vpwrTrapMultipleModuleFailAlarm,
       "vpwrTrapModuleCommAlarm": vpwrTrapModuleCommAlarm,
       "vpwrTrapSystemOverTemperatureAlarm": vpwrTrapSystemOverTemperatureAlarm,
       "vpwrTrapSystemOK": vpwrTrapSystemOK,
       "vpwrTrapModuleInserted": vpwrTrapModuleInserted,
       "vpwrTrapModuleRemoved": vpwrTrapModuleRemoved,
       "vpwrTrapThermalCompActive": vpwrTrapThermalCompActive,
       "vpwrTrapThermalCompInactive": vpwrTrapThermalCompInactive,
       "vpwrTrapInternalTempAlarmSet": vpwrTrapInternalTempAlarmSet,
       "vpwrTrapInternalTempAlarmCleared": vpwrTrapInternalTempAlarmCleared,
       "vpwrTrapBatteryTempAlarmSet": vpwrTrapBatteryTempAlarmSet,
       "vpwrTrapBatteryTempAlarmCleared": vpwrTrapBatteryTempAlarmCleared,
       "vpwrTrapLoginFail": vpwrTrapLoginFail,
       "vpwrTrapLoginSuccess": vpwrTrapLoginSuccess,
       "vpwrTrapLogout": vpwrTrapLogout,
       "vpwrTrapAdminPwdChange": vpwrTrapAdminPwdChange,
       "vpwrTrapIllegalConfigSubmit": vpwrTrapIllegalConfigSubmit,
       "vpwrTrapCfgChange": vpwrTrapCfgChange,
       "vpwrTrapClearEventHistory": vpwrTrapClearEventHistory,
       "vpwrTrapSwDownloadNoReboot": vpwrTrapSwDownloadNoReboot,
       "vpwrTrapSwDownloadAndReboot": vpwrTrapSwDownloadAndReboot,
       "vpwrTrapSystemClockChange": vpwrTrapSystemClockChange,
       "vpwrTrapModuleAlarm": vpwrTrapModuleAlarm,
       "vpwrTrapOIDChange": vpwrTrapOIDChange,
       "vpwrTrapThermalRunaway": vpwrTrapThermalRunaway,
       "vpwrTrapBatteryDischargeTestAlarm": vpwrTrapBatteryDischargeTestAlarm,
       "vpwrTrapBayUnnameAlarm": vpwrTrapBayUnnameAlarm,
       "vpwrTrapPMComFailAlarm": vpwrTrapPMComFailAlarm,
       "vpwrTrapFuseOverloadAlarm": vpwrTrapFuseOverloadAlarm,
       "vpwrTrapPeripheralAlarm": vpwrTrapPeripheralAlarm,
       "vpwrTrapThermalProbeAlarm": vpwrTrapThermalProbeAlarm,
       "vpwrTrapBayCommAlarm": vpwrTrapBayCommAlarm,
       "vpwrTrapDistributionCommAlarm": vpwrTrapDistributionCommAlarm,
       "vpwrTrapConverterAlarm": vpwrTrapConverterAlarm,
       "vpwrTrapMultipleConvFailAlarm": vpwrTrapMultipleConvFailAlarm,
       "vpwrTrapDGUAlarm": vpwrTrapDGUAlarm,
       "vpwrTrapConfigErrorAlarm": vpwrTrapConfigErrorAlarm,
       "vpwrTrapDisplayFirmwareMismatchAlarm": vpwrTrapDisplayFirmwareMismatchAlarm,
       "vpwrTrapConverterInputFailAlarm": vpwrTrapConverterInputFailAlarm,
       "vpwrTrapBatteryRechgIlimitFailAlarm": vpwrTrapBatteryRechgIlimitFailAlarm,
       "vpwrTrapSystemAlive": vpwrTrapSystemAlive,
       "vpwrTrapSystemAuxAlmSource": vpwrTrapSystemAuxAlmSource,
       "vpwrTrapSystemDistAlmSource": vpwrTrapSystemDistAlmSource,
       "vpwrTrapSystemBatCapacityAlarm": vpwrTrapSystemBatCapacityAlarm,
       "vpwrTrapSystemACFClearAlarm": vpwrTrapSystemACFClearAlarm,
       "vpwrTrapSystemACFSetAlarm": vpwrTrapSystemACFSetAlarm,
       "vpwrTrapSystemBatCapacityLeft": vpwrTrapSystemBatCapacityLeft,
       "vpwrTrapRectifierUVAlarm": vpwrTrapRectifierUVAlarm,
       "vpwrTrapMultRectifierUVAlarm": vpwrTrapMultRectifierUVAlarm,
       "vpwrTrapRingerAlarm": vpwrTrapRingerAlarm,
       "vpwrTrapMultRingerAlarm": vpwrTrapMultRingerAlarm,
       "vpwrTrapI2CCANAlarm": vpwrTrapI2CCANAlarm,
       "vpwrTrapRectifierIlimitAlarm": vpwrTrapRectifierIlimitAlarm,
       "vpwrTrapMultRectifierIlimitAlarm": vpwrTrapMultRectifierIlimitAlarm,
       "vpwrTrapRingerCommAlarm": vpwrTrapRingerCommAlarm,
       "vpwrTrapUnassignedAlarm": vpwrTrapUnassignedAlarm,
       "vpwrDcPowerTrapVars": vpwrDcPowerTrapVars,
       "vpwrTrapsMsgString": vpwrTrapsMsgString,
       "vpwrTrapUserIpAddress": vpwrTrapUserIpAddress,
       "vpwrTrapAcfDuration": vpwrTrapAcfDuration,
       "vpwrAlarmingSubModuleBitMap": vpwrAlarmingSubModuleBitMap,
       "vpwrBatteryCurrentCapacity": vpwrBatteryCurrentCapacity,
       "vpwrAlarmingModuleIndex": vpwrAlarmingModuleIndex,
       "vpwrAlarmingModuleOID": vpwrAlarmingModuleOID,
       "vpwrAlarmingModuleBitMap": vpwrAlarmingModuleBitMap,
       "vpwrBatteryRemainingTime": vpwrBatteryRemainingTime,
       "vpwrDcPowerRinger": vpwrDcPowerRinger,
       "vpwrRingerConfigGroup": vpwrRingerConfigGroup,
       "vpwrRingerIndex": vpwrRingerIndex,
       "vpwrRingerParameterAdminState": vpwrRingerParameterAdminState,
       "vpwrRingerParameterAcVoltage": vpwrRingerParameterAcVoltage,
       "vpwrRingerParameterDcVoltage": vpwrRingerParameterDcVoltage,
       "vpwrRingerParameterFrequency": vpwrRingerParameterFrequency,
       "vpwrRingerNumberPresent": vpwrRingerNumberPresent,
       "vpwrRingerAlarmGroup": vpwrRingerAlarmGroup,
       "vpwrRingerAlarmAFailed": vpwrRingerAlarmAFailed,
       "vpwrRingerAlarmAOverTemp": vpwrRingerAlarmAOverTemp,
       "vpwrRingerAlarmAOverCurrent": vpwrRingerAlarmAOverCurrent,
       "vpwrRingerAlarmBFailed": vpwrRingerAlarmBFailed,
       "vpwrRingerAlarmBOverTemp": vpwrRingerAlarmBOverTemp,
       "vpwrRingerAlarmBOverCurrent": vpwrRingerAlarmBOverCurrent,
       "vpwrRingerTestGroup": vpwrRingerTestGroup,
       "vpwrDcPowerDcDcConverter": vpwrDcPowerDcDcConverter,
       "vpwrDcDcConverterConfigGroup": vpwrDcDcConverterConfigGroup,
       "vpwrDcDcConverterAlarmGroup": vpwrDcDcConverterAlarmGroup,
       "vpwrDcDcConverterTestGroup": vpwrDcDcConverterTestGroup,
       "vpwrDcPowerDcAcInverter": vpwrDcPowerDcAcInverter,
       "vpwrDcAcInverterConfigGroup": vpwrDcAcInverterConfigGroup,
       "vpwrDcAcInverterAlarmGroup": vpwrDcAcInverterAlarmGroup,
       "vpwrDcAcInverterTestGroup": vpwrDcAcInverterTestGroup,
       "vpwrDcPowerAcLineModule": vpwrDcPowerAcLineModule,
       "vpwrAcLineModuleConfigGroup": vpwrAcLineModuleConfigGroup,
       "vpwrAcLineModuleAlarmGroup": vpwrAcLineModuleAlarmGroup,
       "vpwrAcLineModuleTestGroup": vpwrAcLineModuleTestGroup,
       "vpwrDcPowerIoModule": vpwrDcPowerIoModule,
       "vpwrIoModuleConfigGroup": vpwrIoModuleConfigGroup,
       "vpwrIoModuleAlarmGroup": vpwrIoModuleAlarmGroup,
       "vpwrIoModuleTestGroup": vpwrIoModuleTestGroup,
       "vpwrDcPowerPMModule": vpwrDcPowerPMModule,
       "vpwrPMCnfgTable": vpwrPMCnfgTable,
       "vpwrPMCnfgEntry": vpwrPMCnfgEntry,
       "vpwrPMIndex": vpwrPMIndex,
       "vpwrPMDescription": vpwrPMDescription,
       "vpwrPMCnfg1": vpwrPMCnfg1,
       "vpwrPMCnfg2": vpwrPMCnfg2,
       "vpwrPMCnfg3": vpwrPMCnfg3,
       "vpwrPMCnfg4": vpwrPMCnfg4,
       "vpwrPMCnfg5": vpwrPMCnfg5,
       "vpwrPMCnfg6": vpwrPMCnfg6,
       "vpwrPMCnfg7": vpwrPMCnfg7,
       "vpwrPMCnfg8": vpwrPMCnfg8,
       "vpwrPMInputStatusTable": vpwrPMInputStatusTable,
       "vpwrPMInputStatusEntry": vpwrPMInputStatusEntry,
       "vpwrPMIndex1": vpwrPMIndex1,
       "vpwrPMDescription1": vpwrPMDescription1,
       "vpwrPMInput1State": vpwrPMInput1State,
       "vpwrPMInput2State": vpwrPMInput2State,
       "vpwrPMInput3State": vpwrPMInput3State,
       "vpwrPMInput4State": vpwrPMInput4State,
       "vpwrPMInput5State": vpwrPMInput5State,
       "vpwrPMInput6State": vpwrPMInput6State,
       "vpwrPMInput7State": vpwrPMInput7State,
       "vpwrPMInput8State": vpwrPMInput8State,
       "vpwrPMRelayCtrlTable": vpwrPMRelayCtrlTable,
       "vpwrPMRelayCtrlEntry": vpwrPMRelayCtrlEntry,
       "vpwrPMIndex2": vpwrPMIndex2,
       "vpwrPMDescription2": vpwrPMDescription2,
       "vpwrPMRelay1State": vpwrPMRelay1State,
       "vpwrPMRelay2State": vpwrPMRelay2State,
       "vpwrPMRelay3State": vpwrPMRelay3State,
       "vpwrPMRelay4State": vpwrPMRelay4State,
       "vpwrPMRelay5State": vpwrPMRelay5State,
       "vpwrPMRelay6State": vpwrPMRelay6State,
       "vpwrPMModuleAlarmGroup": vpwrPMModuleAlarmGroup,
       "vpwrPMModuleTestGroup": vpwrPMModuleTestGroup,
       "vpwrDcPowerDistModule": vpwrDcPowerDistModule,
       "vpwrDcPowerBattery": vpwrDcPowerBattery,
       "vpwrDcPowerController": vpwrDcPowerController,
       "vpwrDcPowerUnkModule": vpwrDcPowerUnkModule,
       "thirdPartyProduct": thirdPartyProduct}
)
