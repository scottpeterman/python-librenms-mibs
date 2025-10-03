# SNMP MIB module (DANTHERM-COOLING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dantherm\DANTHERM-COOLING-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:33:51 2025
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

_DanthermCooling_ObjectIdentity = ObjectIdentity
danthermCooling = _DanthermCooling_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46651)
)
_ControllerCC3000_ObjectIdentity = ObjectIdentity
controllerCC3000 = _ControllerCC3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46651, 1)
)
_SystemStatus_ObjectIdentity = ObjectIdentity
systemStatus = _SystemStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46651, 1, 1)
)


class _OnBoardTempr_Type(Integer32):
    """Custom type onBoardTempr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-41, 101),
    )


_OnBoardTempr_Type.__name__ = "Integer32"
_OnBoardTempr_Object = MibScalar
onBoardTempr = _OnBoardTempr_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 1, 1),
    _OnBoardTempr_Type()
)
onBoardTempr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onBoardTempr.setStatus("mandatory")


class _RoomTempr_Type(Integer32):
    """Custom type roomTempr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-41, 101),
    )


_RoomTempr_Type.__name__ = "Integer32"
_RoomTempr_Object = MibScalar
roomTempr = _RoomTempr_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 1, 2),
    _RoomTempr_Type()
)
roomTempr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roomTempr.setStatus("mandatory")


class _HotSpotTempr_Type(Integer32):
    """Custom type hotSpotTempr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-41, 101),
    )


_HotSpotTempr_Type.__name__ = "Integer32"
_HotSpotTempr_Object = MibScalar
hotSpotTempr = _HotSpotTempr_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 1, 3),
    _HotSpotTempr_Type()
)
hotSpotTempr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hotSpotTempr.setStatus("mandatory")


class _Outdoor1Tempr_Type(Integer32):
    """Custom type outdoor1Tempr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-41, 101),
    )


_Outdoor1Tempr_Type.__name__ = "Integer32"
_Outdoor1Tempr_Object = MibScalar
outdoor1Tempr = _Outdoor1Tempr_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 1, 4),
    _Outdoor1Tempr_Type()
)
outdoor1Tempr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outdoor1Tempr.setStatus("mandatory")


class _Outdoor2Tempr_Type(Integer32):
    """Custom type outdoor2Tempr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-41, 101),
    )


_Outdoor2Tempr_Type.__name__ = "Integer32"
_Outdoor2Tempr_Object = MibScalar
outdoor2Tempr = _Outdoor2Tempr_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 1, 5),
    _Outdoor2Tempr_Type()
)
outdoor2Tempr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outdoor2Tempr.setStatus("mandatory")


class _ShelterTempr_Type(Integer32):
    """Custom type shelterTempr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-41, 101),
    )


_ShelterTempr_Type.__name__ = "Integer32"
_ShelterTempr_Object = MibScalar
shelterTempr = _ShelterTempr_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 1, 6),
    _ShelterTempr_Type()
)
shelterTempr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelterTempr.setStatus("mandatory")


class _OutdoorCombinedTempr_Type(Integer32):
    """Custom type outdoorCombinedTempr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-41, 101),
    )


_OutdoorCombinedTempr_Type.__name__ = "Integer32"
_OutdoorCombinedTempr_Object = MibScalar
outdoorCombinedTempr = _OutdoorCombinedTempr_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 1, 7),
    _OutdoorCombinedTempr_Type()
)
outdoorCombinedTempr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outdoorCombinedTempr.setStatus("mandatory")


class _Fan1RPM_Type(Integer32):
    """Custom type fan1RPM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_Fan1RPM_Type.__name__ = "Integer32"
_Fan1RPM_Object = MibScalar
fan1RPM = _Fan1RPM_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 1, 8),
    _Fan1RPM_Type()
)
fan1RPM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan1RPM.setStatus("mandatory")


class _Fan2RPM_Type(Integer32):
    """Custom type fan2RPM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_Fan2RPM_Type.__name__ = "Integer32"
_Fan2RPM_Object = MibScalar
fan2RPM = _Fan2RPM_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 1, 9),
    _Fan2RPM_Type()
)
fan2RPM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan2RPM.setStatus("mandatory")


class _Fan1SpeedPercentage_Type(Integer32):
    """Custom type fan1SpeedPercentage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Fan1SpeedPercentage_Type.__name__ = "Integer32"
_Fan1SpeedPercentage_Object = MibScalar
fan1SpeedPercentage = _Fan1SpeedPercentage_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 1, 10),
    _Fan1SpeedPercentage_Type()
)
fan1SpeedPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan1SpeedPercentage.setStatus("mandatory")


class _Fan2SpeedPercentage_Type(Integer32):
    """Custom type fan2SpeedPercentage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Fan2SpeedPercentage_Type.__name__ = "Integer32"
_Fan2SpeedPercentage_Object = MibScalar
fan2SpeedPercentage = _Fan2SpeedPercentage_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 1, 11),
    _Fan2SpeedPercentage_Type()
)
fan2SpeedPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan2SpeedPercentage.setStatus("mandatory")


class _Damper1Position_Type(Integer32):
    """Custom type damper1Position based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Damper1Position_Type.__name__ = "Integer32"
_Damper1Position_Object = MibScalar
damper1Position = _Damper1Position_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 1, 12),
    _Damper1Position_Type()
)
damper1Position.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    damper1Position.setStatus("mandatory")


class _Damper2Position_Type(Integer32):
    """Custom type damper2Position based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Damper2Position_Type.__name__ = "Integer32"
_Damper2Position_Object = MibScalar
damper2Position = _Damper2Position_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 1, 13),
    _Damper2Position_Type()
)
damper2Position.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    damper2Position.setStatus("mandatory")


class _Humidity_Type(Integer32):
    """Custom type humidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Humidity_Type.__name__ = "Integer32"
_Humidity_Object = MibScalar
humidity = _Humidity_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 1, 14),
    _Humidity_Type()
)
humidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity.setStatus("mandatory")


class _Dewpoint_Type(Integer32):
    """Custom type dewpoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-41, 101),
    )


_Dewpoint_Type.__name__ = "Integer32"
_Dewpoint_Object = MibScalar
dewpoint = _Dewpoint_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 1, 15),
    _Dewpoint_Type()
)
dewpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint.setStatus("mandatory")


class _AtmosphericPressure_Type(Integer32):
    """Custom type atmosphericPressure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_AtmosphericPressure_Type.__name__ = "Integer32"
_AtmosphericPressure_Object = MibScalar
atmosphericPressure = _AtmosphericPressure_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 1, 16),
    _AtmosphericPressure_Type()
)
atmosphericPressure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmosphericPressure.setStatus("mandatory")


class _FlowPressure_Type(Integer32):
    """Custom type flowPressure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
    )


_FlowPressure_Type.__name__ = "Integer32"
_FlowPressure_Object = MibScalar
flowPressure = _FlowPressure_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 1, 17),
    _FlowPressure_Type()
)
flowPressure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowPressure.setStatus("mandatory")


class _Fan1Status_Type(Integer32):
    """Custom type fan1Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Fan1Status_Type.__name__ = "Integer32"
_Fan1Status_Object = MibScalar
fan1Status = _Fan1Status_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 1, 18),
    _Fan1Status_Type()
)
fan1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan1Status.setStatus("mandatory")


class _Fan2Status_Type(Integer32):
    """Custom type fan2Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Fan2Status_Type.__name__ = "Integer32"
_Fan2Status_Object = MibScalar
fan2Status = _Fan2Status_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 1, 19),
    _Fan2Status_Type()
)
fan2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan2Status.setStatus("mandatory")


class _Damper1Status_Type(Integer32):
    """Custom type damper1Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Damper1Status_Type.__name__ = "Integer32"
_Damper1Status_Object = MibScalar
damper1Status = _Damper1Status_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 1, 20),
    _Damper1Status_Type()
)
damper1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    damper1Status.setStatus("mandatory")


class _Damper2Status_Type(Integer32):
    """Custom type damper2Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Damper2Status_Type.__name__ = "Integer32"
_Damper2Status_Object = MibScalar
damper2Status = _Damper2Status_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 1, 21),
    _Damper2Status_Type()
)
damper2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    damper2Status.setStatus("mandatory")


class _Aircond1Status_Type(Integer32):
    """Custom type aircond1Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Aircond1Status_Type.__name__ = "Integer32"
_Aircond1Status_Object = MibScalar
aircond1Status = _Aircond1Status_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 1, 22),
    _Aircond1Status_Type()
)
aircond1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aircond1Status.setStatus("mandatory")


class _Aircond2Status_Type(Integer32):
    """Custom type aircond2Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Aircond2Status_Type.__name__ = "Integer32"
_Aircond2Status_Object = MibScalar
aircond2Status = _Aircond2Status_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 1, 23),
    _Aircond2Status_Type()
)
aircond2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aircond2Status.setStatus("mandatory")


class _HeaterStatus_Type(Integer32):
    """Custom type heaterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HeaterStatus_Type.__name__ = "Integer32"
_HeaterStatus_Object = MibScalar
heaterStatus = _HeaterStatus_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 1, 24),
    _HeaterStatus_Type()
)
heaterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heaterStatus.setStatus("mandatory")


class _Shelter1Status_Type(Integer32):
    """Custom type shelter1Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_Shelter1Status_Type.__name__ = "Integer32"
_Shelter1Status_Object = MibScalar
shelter1Status = _Shelter1Status_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 1, 25),
    _Shelter1Status_Type()
)
shelter1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelter1Status.setStatus("mandatory")


class _Shelter2Status_Type(Integer32):
    """Custom type shelter2Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_Shelter2Status_Type.__name__ = "Integer32"
_Shelter2Status_Object = MibScalar
shelter2Status = _Shelter2Status_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 1, 26),
    _Shelter2Status_Type()
)
shelter2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelter2Status.setStatus("mandatory")


class _Shelter1Mode_Type(Integer32):
    """Custom type shelter1Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Shelter1Mode_Type.__name__ = "Integer32"
_Shelter1Mode_Object = MibScalar
shelter1Mode = _Shelter1Mode_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 1, 27),
    _Shelter1Mode_Type()
)
shelter1Mode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelter1Mode.setStatus("mandatory")


class _Shelter2Mode_Type(Integer32):
    """Custom type shelter2Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Shelter2Mode_Type.__name__ = "Integer32"
_Shelter2Mode_Object = MibScalar
shelter2Mode = _Shelter2Mode_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 1, 28),
    _Shelter2Mode_Type()
)
shelter2Mode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelter2Mode.setStatus("mandatory")


class _Shelter1Setpoint_Type(Integer32):
    """Custom type shelter1Setpoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-41, 80),
    )


_Shelter1Setpoint_Type.__name__ = "Integer32"
_Shelter1Setpoint_Object = MibScalar
shelter1Setpoint = _Shelter1Setpoint_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 1, 29),
    _Shelter1Setpoint_Type()
)
shelter1Setpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelter1Setpoint.setStatus("mandatory")


class _Shelter2Setpoint_Type(Integer32):
    """Custom type shelter2Setpoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-41, 80),
    )


_Shelter2Setpoint_Type.__name__ = "Integer32"
_Shelter2Setpoint_Object = MibScalar
shelter2Setpoint = _Shelter2Setpoint_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 1, 30),
    _Shelter2Setpoint_Type()
)
shelter2Setpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelter2Setpoint.setStatus("mandatory")


class _ErrorStatus_Type(Integer32):
    """Custom type errorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 33554432),
    )


_ErrorStatus_Type.__name__ = "Integer32"
_ErrorStatus_Object = MibScalar
errorStatus = _ErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 1, 31),
    _ErrorStatus_Type()
)
errorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorStatus.setStatus("mandatory")


class _MaskedErrorStatus_Type(Integer32):
    """Custom type maskedErrorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 33554432),
    )


_MaskedErrorStatus_Type.__name__ = "Integer32"
_MaskedErrorStatus_Object = MibScalar
maskedErrorStatus = _MaskedErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 1, 32),
    _MaskedErrorStatus_Type()
)
maskedErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maskedErrorStatus.setStatus("mandatory")


class _Voltage_Type(Integer32):
    """Custom type voltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 80),
    )


_Voltage_Type.__name__ = "Integer32"
_Voltage_Object = MibScalar
voltage = _Voltage_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 1, 33),
    _Voltage_Type()
)
voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltage.setStatus("mandatory")


class _DigitalInputStatus_Type(Integer32):
    """Custom type digitalInputStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_DigitalInputStatus_Type.__name__ = "Integer32"
_DigitalInputStatus_Object = MibScalar
digitalInputStatus = _DigitalInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 1, 34),
    _DigitalInputStatus_Type()
)
digitalInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalInputStatus.setStatus("mandatory")


class _AlarmDriveStatus_Type(Integer32):
    """Custom type alarmDriveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_AlarmDriveStatus_Type.__name__ = "Integer32"
_AlarmDriveStatus_Object = MibScalar
alarmDriveStatus = _AlarmDriveStatus_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 1, 35),
    _AlarmDriveStatus_Type()
)
alarmDriveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmDriveStatus.setStatus("mandatory")


class _Fan1OpertdurHour_Type(Integer32):
    """Custom type fan1OpertdurHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fan1OpertdurHour_Type.__name__ = "Integer32"
_Fan1OpertdurHour_Object = MibScalar
fan1OpertdurHour = _Fan1OpertdurHour_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 1, 36),
    _Fan1OpertdurHour_Type()
)
fan1OpertdurHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fan1OpertdurHour.setStatus("mandatory")


class _Fan1OpertdurMin_Type(Integer32):
    """Custom type fan1OpertdurMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_Fan1OpertdurMin_Type.__name__ = "Integer32"
_Fan1OpertdurMin_Object = MibScalar
fan1OpertdurMin = _Fan1OpertdurMin_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 1, 37),
    _Fan1OpertdurMin_Type()
)
fan1OpertdurMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fan1OpertdurMin.setStatus("mandatory")


class _Fan2OpertdurHour_Type(Integer32):
    """Custom type fan2OpertdurHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fan2OpertdurHour_Type.__name__ = "Integer32"
_Fan2OpertdurHour_Object = MibScalar
fan2OpertdurHour = _Fan2OpertdurHour_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 1, 38),
    _Fan2OpertdurHour_Type()
)
fan2OpertdurHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fan2OpertdurHour.setStatus("mandatory")


class _Fan2OpertdurMin_Type(Integer32):
    """Custom type fan2OpertdurMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_Fan2OpertdurMin_Type.__name__ = "Integer32"
_Fan2OpertdurMin_Object = MibScalar
fan2OpertdurMin = _Fan2OpertdurMin_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 1, 39),
    _Fan2OpertdurMin_Type()
)
fan2OpertdurMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fan2OpertdurMin.setStatus("mandatory")


class _Aircon1OpertdurHour_Type(Integer32):
    """Custom type aircon1OpertdurHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Aircon1OpertdurHour_Type.__name__ = "Integer32"
_Aircon1OpertdurHour_Object = MibScalar
aircon1OpertdurHour = _Aircon1OpertdurHour_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 1, 40),
    _Aircon1OpertdurHour_Type()
)
aircon1OpertdurHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aircon1OpertdurHour.setStatus("mandatory")


class _Aircon1OpertdurMin_Type(Integer32):
    """Custom type aircon1OpertdurMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_Aircon1OpertdurMin_Type.__name__ = "Integer32"
_Aircon1OpertdurMin_Object = MibScalar
aircon1OpertdurMin = _Aircon1OpertdurMin_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 1, 41),
    _Aircon1OpertdurMin_Type()
)
aircon1OpertdurMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aircon1OpertdurMin.setStatus("mandatory")


class _Aircon2OpertdurHour_Type(Integer32):
    """Custom type aircon2OpertdurHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Aircon2OpertdurHour_Type.__name__ = "Integer32"
_Aircon2OpertdurHour_Object = MibScalar
aircon2OpertdurHour = _Aircon2OpertdurHour_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 1, 42),
    _Aircon2OpertdurHour_Type()
)
aircon2OpertdurHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aircon2OpertdurHour.setStatus("mandatory")


class _Aircon2OpertdurMin_Type(Integer32):
    """Custom type aircon2OpertdurMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_Aircon2OpertdurMin_Type.__name__ = "Integer32"
_Aircon2OpertdurMin_Object = MibScalar
aircon2OpertdurMin = _Aircon2OpertdurMin_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 1, 43),
    _Aircon2OpertdurMin_Type()
)
aircon2OpertdurMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aircon2OpertdurMin.setStatus("mandatory")


class _HeaterOpertdurHour_Type(Integer32):
    """Custom type heaterOpertdurHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HeaterOpertdurHour_Type.__name__ = "Integer32"
_HeaterOpertdurHour_Object = MibScalar
heaterOpertdurHour = _HeaterOpertdurHour_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 1, 44),
    _HeaterOpertdurHour_Type()
)
heaterOpertdurHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    heaterOpertdurHour.setStatus("mandatory")


class _HeaterOpertdurMin_Type(Integer32):
    """Custom type heaterOpertdurMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_HeaterOpertdurMin_Type.__name__ = "Integer32"
_HeaterOpertdurMin_Object = MibScalar
heaterOpertdurMin = _HeaterOpertdurMin_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 1, 45),
    _HeaterOpertdurMin_Type()
)
heaterOpertdurMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    heaterOpertdurMin.setStatus("mandatory")
_CcSN_Type = OctetString
_CcSN_Object = MibScalar
ccSN = _CcSN_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 1, 46),
    _CcSN_Type()
)
ccSN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSN.setStatus("mandatory")
_Fanbox1SN_Type = OctetString
_Fanbox1SN_Object = MibScalar
fanbox1SN = _Fanbox1SN_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 1, 47),
    _Fanbox1SN_Type()
)
fanbox1SN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fanbox1SN.setStatus("mandatory")
_Fanbox2SN_Type = OctetString
_Fanbox2SN_Object = MibScalar
fanbox2SN = _Fanbox2SN_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 1, 48),
    _Fanbox2SN_Type()
)
fanbox2SN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fanbox2SN.setStatus("mandatory")
_Aircond1SN_Type = OctetString
_Aircond1SN_Object = MibScalar
aircond1SN = _Aircond1SN_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 1, 49),
    _Aircond1SN_Type()
)
aircond1SN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aircond1SN.setStatus("mandatory")
_Aircond2SN_Type = OctetString
_Aircond2SN_Object = MibScalar
aircond2SN = _Aircond2SN_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 1, 50),
    _Aircond2SN_Type()
)
aircond2SN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aircond2SN.setStatus("mandatory")
_FwVersion_Type = OctetString
_FwVersion_Object = MibScalar
fwVersion = _FwVersion_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 1, 51),
    _FwVersion_Type()
)
fwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwVersion.setStatus("mandatory")
_HighlevelControl_ObjectIdentity = ObjectIdentity
highlevelControl = _HighlevelControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46651, 1, 2)
)


class _CoolSetpointZone1_Type(Integer32):
    """Custom type coolSetpointZone1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-41, 101),
    )


_CoolSetpointZone1_Type.__name__ = "Integer32"
_CoolSetpointZone1_Object = MibScalar
coolSetpointZone1 = _CoolSetpointZone1_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 2, 1),
    _CoolSetpointZone1_Type()
)
coolSetpointZone1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coolSetpointZone1.setStatus("mandatory")


class _CoolSetpointZone2_Type(Integer32):
    """Custom type coolSetpointZone2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-41, 101),
    )


_CoolSetpointZone2_Type.__name__ = "Integer32"
_CoolSetpointZone2_Object = MibScalar
coolSetpointZone2 = _CoolSetpointZone2_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 2, 2),
    _CoolSetpointZone2_Type()
)
coolSetpointZone2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coolSetpointZone2.setStatus("mandatory")


class _HeaterSetpoint_Type(Integer32):
    """Custom type heaterSetpoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-41, 101),
    )


_HeaterSetpoint_Type.__name__ = "Integer32"
_HeaterSetpoint_Object = MibScalar
heaterSetpoint = _HeaterSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 2, 3),
    _HeaterSetpoint_Type()
)
heaterSetpoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    heaterSetpoint.setStatus("mandatory")


class _BackupConfig_Type(Integer32):
    """Custom type backupConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BackupConfig_Type.__name__ = "Integer32"
_BackupConfig_Object = MibScalar
backupConfig = _BackupConfig_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 2, 4),
    _BackupConfig_Type()
)
backupConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupConfig.setStatus("mandatory")


class _RestoreConfig_Type(Integer32):
    """Custom type restoreConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RestoreConfig_Type.__name__ = "Integer32"
_RestoreConfig_Object = MibScalar
restoreConfig = _RestoreConfig_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 2, 5),
    _RestoreConfig_Type()
)
restoreConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restoreConfig.setStatus("mandatory")


class _SystemReset_Type(Integer32):
    """Custom type systemReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_SystemReset_Type.__name__ = "Integer32"
_SystemReset_Object = MibScalar
systemReset = _SystemReset_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 2, 6),
    _SystemReset_Type()
)
systemReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemReset.setStatus("mandatory")


class _Year_Type(Integer32):
    """Custom type year based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2015, 2099),
    )


_Year_Type.__name__ = "Integer32"
_Year_Object = MibScalar
year = _Year_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 2, 7),
    _Year_Type()
)
year.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    year.setStatus("mandatory")


class _Month_Type(Integer32):
    """Custom type month based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Month_Type.__name__ = "Integer32"
_Month_Object = MibScalar
month = _Month_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 2, 8),
    _Month_Type()
)
month.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    month.setStatus("mandatory")


class _Date_Type(Integer32):
    """Custom type date based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_Date_Type.__name__ = "Integer32"
_Date_Object = MibScalar
date = _Date_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 2, 9),
    _Date_Type()
)
date.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    date.setStatus("mandatory")


class _Hour_Type(Integer32):
    """Custom type hour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_Hour_Type.__name__ = "Integer32"
_Hour_Object = MibScalar
hour = _Hour_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 2, 10),
    _Hour_Type()
)
hour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hour.setStatus("mandatory")


class _Minute_Type(Integer32):
    """Custom type minute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_Minute_Type.__name__ = "Integer32"
_Minute_Object = MibScalar
minute = _Minute_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 2, 11),
    _Minute_Type()
)
minute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minute.setStatus("mandatory")
_Fan1Config_ObjectIdentity = ObjectIdentity
fan1Config = _Fan1Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46651, 1, 3)
)


class _SaveReloadConff1_Type(Integer32):
    """Custom type saveReloadConff1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_SaveReloadConff1_Type.__name__ = "Integer32"
_SaveReloadConff1_Object = MibScalar
saveReloadConff1 = _SaveReloadConff1_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 3, 1),
    _SaveReloadConff1_Type()
)
saveReloadConff1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saveReloadConff1.setStatus("mandatory")


class _OffTemprf1_Type(Integer32):
    """Custom type offTemprf1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-41, 101),
    )


_OffTemprf1_Type.__name__ = "Integer32"
_OffTemprf1_Object = MibScalar
offTemprf1 = _OffTemprf1_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 3, 2),
    _OffTemprf1_Type()
)
offTemprf1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    offTemprf1.setStatus("mandatory")


class _IdleOnTemprf1_Type(Integer32):
    """Custom type idleOnTemprf1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-41, 101),
    )


_IdleOnTemprf1_Type.__name__ = "Integer32"
_IdleOnTemprf1_Object = MibScalar
idleOnTemprf1 = _IdleOnTemprf1_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 3, 3),
    _IdleOnTemprf1_Type()
)
idleOnTemprf1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    idleOnTemprf1.setStatus("mandatory")


class _IdleEntryTemprf1_Type(Integer32):
    """Custom type idleEntryTemprf1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-41, 101),
    )


_IdleEntryTemprf1_Type.__name__ = "Integer32"
_IdleEntryTemprf1_Object = MibScalar
idleEntryTemprf1 = _IdleEntryTemprf1_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 3, 4),
    _IdleEntryTemprf1_Type()
)
idleEntryTemprf1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    idleEntryTemprf1.setStatus("mandatory")


class _MidPoint1Temprf1_Type(Integer32):
    """Custom type midPoint1Temprf1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-41, 101),
    )


_MidPoint1Temprf1_Type.__name__ = "Integer32"
_MidPoint1Temprf1_Object = MibScalar
midPoint1Temprf1 = _MidPoint1Temprf1_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 3, 5),
    _MidPoint1Temprf1_Type()
)
midPoint1Temprf1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midPoint1Temprf1.setStatus("mandatory")


class _SetPointTemprf1_Type(Integer32):
    """Custom type setPointTemprf1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-41, 101),
    )


_SetPointTemprf1_Type.__name__ = "Integer32"
_SetPointTemprf1_Object = MibScalar
setPointTemprf1 = _SetPointTemprf1_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 3, 6),
    _SetPointTemprf1_Type()
)
setPointTemprf1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPointTemprf1.setStatus("mandatory")


class _MidPoint2Temprf1_Type(Integer32):
    """Custom type midPoint2Temprf1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-41, 101),
    )


_MidPoint2Temprf1_Type.__name__ = "Integer32"
_MidPoint2Temprf1_Object = MibScalar
midPoint2Temprf1 = _MidPoint2Temprf1_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 3, 7),
    _MidPoint2Temprf1_Type()
)
midPoint2Temprf1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midPoint2Temprf1.setStatus("mandatory")


class _HighSpeedTemprf1_Type(Integer32):
    """Custom type highSpeedTemprf1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-41, 101),
    )


_HighSpeedTemprf1_Type.__name__ = "Integer32"
_HighSpeedTemprf1_Object = MibScalar
highSpeedTemprf1 = _HighSpeedTemprf1_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 3, 8),
    _HighSpeedTemprf1_Type()
)
highSpeedTemprf1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highSpeedTemprf1.setStatus("mandatory")


class _ExtendHighSpeedEntryTemprf1_Type(Integer32):
    """Custom type extendHighSpeedEntryTemprf1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-41, 101),
    )


_ExtendHighSpeedEntryTemprf1_Type.__name__ = "Integer32"
_ExtendHighSpeedEntryTemprf1_Object = MibScalar
extendHighSpeedEntryTemprf1 = _ExtendHighSpeedEntryTemprf1_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 3, 9),
    _ExtendHighSpeedEntryTemprf1_Type()
)
extendHighSpeedEntryTemprf1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extendHighSpeedEntryTemprf1.setStatus("mandatory")


class _ExtendHighSpeedExitTemprf1_Type(Integer32):
    """Custom type extendHighSpeedExitTemprf1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-41, 101),
    )


_ExtendHighSpeedExitTemprf1_Type.__name__ = "Integer32"
_ExtendHighSpeedExitTemprf1_Object = MibScalar
extendHighSpeedExitTemprf1 = _ExtendHighSpeedExitTemprf1_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 3, 10),
    _ExtendHighSpeedExitTemprf1_Type()
)
extendHighSpeedExitTemprf1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extendHighSpeedExitTemprf1.setStatus("mandatory")


class _BoostEntryTemprf1_Type(Integer32):
    """Custom type boostEntryTemprf1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-41, 101),
    )


_BoostEntryTemprf1_Type.__name__ = "Integer32"
_BoostEntryTemprf1_Object = MibScalar
boostEntryTemprf1 = _BoostEntryTemprf1_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 3, 11),
    _BoostEntryTemprf1_Type()
)
boostEntryTemprf1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boostEntryTemprf1.setStatus("mandatory")


class _BoostExitTemprf1_Type(Integer32):
    """Custom type boostExitTemprf1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-41, 101),
    )


_BoostExitTemprf1_Type.__name__ = "Integer32"
_BoostExitTemprf1_Object = MibScalar
boostExitTemprf1 = _BoostExitTemprf1_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 3, 12),
    _BoostExitTemprf1_Type()
)
boostExitTemprf1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boostExitTemprf1.setStatus("mandatory")


class _IdleRPMf1_Type(Integer32):
    """Custom type idleRPMf1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_IdleRPMf1_Type.__name__ = "Integer32"
_IdleRPMf1_Object = MibScalar
idleRPMf1 = _IdleRPMf1_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 3, 13),
    _IdleRPMf1_Type()
)
idleRPMf1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    idleRPMf1.setStatus("mandatory")


class _MidPointRPMf1_Type(Integer32):
    """Custom type midPointRPMf1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_MidPointRPMf1_Type.__name__ = "Integer32"
_MidPointRPMf1_Object = MibScalar
midPointRPMf1 = _MidPointRPMf1_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 3, 14),
    _MidPointRPMf1_Type()
)
midPointRPMf1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midPointRPMf1.setStatus("mandatory")


class _HighSpeedRPMf1_Type(Integer32):
    """Custom type highSpeedRPMf1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_HighSpeedRPMf1_Type.__name__ = "Integer32"
_HighSpeedRPMf1_Object = MibScalar
highSpeedRPMf1 = _HighSpeedRPMf1_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 3, 15),
    _HighSpeedRPMf1_Type()
)
highSpeedRPMf1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highSpeedRPMf1.setStatus("mandatory")


class _ExtendHighSpeedRPMf1_Type(Integer32):
    """Custom type extendHighSpeedRPMf1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_ExtendHighSpeedRPMf1_Type.__name__ = "Integer32"
_ExtendHighSpeedRPMf1_Object = MibScalar
extendHighSpeedRPMf1 = _ExtendHighSpeedRPMf1_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 3, 16),
    _ExtendHighSpeedRPMf1_Type()
)
extendHighSpeedRPMf1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extendHighSpeedRPMf1.setStatus("mandatory")


class _IdleDutyCyclef1_Type(Integer32):
    """Custom type idleDutyCyclef1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IdleDutyCyclef1_Type.__name__ = "Integer32"
_IdleDutyCyclef1_Object = MibScalar
idleDutyCyclef1 = _IdleDutyCyclef1_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 3, 17),
    _IdleDutyCyclef1_Type()
)
idleDutyCyclef1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    idleDutyCyclef1.setStatus("mandatory")


class _MidDutyCyclef1_Type(Integer32):
    """Custom type midDutyCyclef1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MidDutyCyclef1_Type.__name__ = "Integer32"
_MidDutyCyclef1_Object = MibScalar
midDutyCyclef1 = _MidDutyCyclef1_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 3, 18),
    _MidDutyCyclef1_Type()
)
midDutyCyclef1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midDutyCyclef1.setStatus("mandatory")


class _HighSpeedDutyCyclef1_Type(Integer32):
    """Custom type highSpeedDutyCyclef1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HighSpeedDutyCyclef1_Type.__name__ = "Integer32"
_HighSpeedDutyCyclef1_Object = MibScalar
highSpeedDutyCyclef1 = _HighSpeedDutyCyclef1_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 3, 19),
    _HighSpeedDutyCyclef1_Type()
)
highSpeedDutyCyclef1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highSpeedDutyCyclef1.setStatus("mandatory")


class _ExtendHighSpeedDutyCyclef1_Type(Integer32):
    """Custom type extendHighSpeedDutyCyclef1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ExtendHighSpeedDutyCyclef1_Type.__name__ = "Integer32"
_ExtendHighSpeedDutyCyclef1_Object = MibScalar
extendHighSpeedDutyCyclef1 = _ExtendHighSpeedDutyCyclef1_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 3, 20),
    _ExtendHighSpeedDutyCyclef1_Type()
)
extendHighSpeedDutyCyclef1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extendHighSpeedDutyCyclef1.setStatus("mandatory")


class _BoostDutyCyclef1_Type(Integer32):
    """Custom type boostDutyCyclef1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BoostDutyCyclef1_Type.__name__ = "Integer32"
_BoostDutyCyclef1_Object = MibScalar
boostDutyCyclef1 = _BoostDutyCyclef1_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 3, 21),
    _BoostDutyCyclef1_Type()
)
boostDutyCyclef1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boostDutyCyclef1.setStatus("mandatory")


class _DeadBandRPMf1_Type(Integer32):
    """Custom type deadBandRPMf1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_DeadBandRPMf1_Type.__name__ = "Integer32"
_DeadBandRPMf1_Object = MibScalar
deadBandRPMf1 = _DeadBandRPMf1_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 3, 22),
    _DeadBandRPMf1_Type()
)
deadBandRPMf1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deadBandRPMf1.setStatus("mandatory")


class _OverrideDigi1f1_Type(Integer32):
    """Custom type overrideDigi1f1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_OverrideDigi1f1_Type.__name__ = "Integer32"
_OverrideDigi1f1_Object = MibScalar
overrideDigi1f1 = _OverrideDigi1f1_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 3, 23),
    _OverrideDigi1f1_Type()
)
overrideDigi1f1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overrideDigi1f1.setStatus("mandatory")


class _OverrideDigi2f1_Type(Integer32):
    """Custom type overrideDigi2f1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_OverrideDigi2f1_Type.__name__ = "Integer32"
_OverrideDigi2f1_Object = MibScalar
overrideDigi2f1 = _OverrideDigi2f1_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 3, 24),
    _OverrideDigi2f1_Type()
)
overrideDigi2f1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overrideDigi2f1.setStatus("mandatory")


class _OverrideDigi3f1_Type(Integer32):
    """Custom type overrideDigi3f1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_OverrideDigi3f1_Type.__name__ = "Integer32"
_OverrideDigi3f1_Object = MibScalar
overrideDigi3f1 = _OverrideDigi3f1_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 3, 25),
    _OverrideDigi3f1_Type()
)
overrideDigi3f1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overrideDigi3f1.setStatus("mandatory")


class _OverrideSensorfailf1_Type(Integer32):
    """Custom type overrideSensorfailf1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_OverrideSensorfailf1_Type.__name__ = "Integer32"
_OverrideSensorfailf1_Object = MibScalar
overrideSensorfailf1 = _OverrideSensorfailf1_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 3, 26),
    _OverrideSensorfailf1_Type()
)
overrideSensorfailf1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overrideSensorfailf1.setStatus("mandatory")


class _SensorSelectf1_Type(Integer32):
    """Custom type sensorSelectf1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_SensorSelectf1_Type.__name__ = "Integer32"
_SensorSelectf1_Object = MibScalar
sensorSelectf1 = _SensorSelectf1_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 3, 27),
    _SensorSelectf1_Type()
)
sensorSelectf1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorSelectf1.setStatus("mandatory")


class _TachoPulseperrotationf1_Type(Integer32):
    """Custom type tachoPulseperrotationf1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TachoPulseperrotationf1_Type.__name__ = "Integer32"
_TachoPulseperrotationf1_Object = MibScalar
tachoPulseperrotationf1 = _TachoPulseperrotationf1_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 3, 28),
    _TachoPulseperrotationf1_Type()
)
tachoPulseperrotationf1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tachoPulseperrotationf1.setStatus("mandatory")


class _ClosedLoopenablef1_Type(Integer32):
    """Custom type closedLoopenablef1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ClosedLoopenablef1_Type.__name__ = "Integer32"
_ClosedLoopenablef1_Object = MibScalar
closedLoopenablef1 = _ClosedLoopenablef1_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 3, 29),
    _ClosedLoopenablef1_Type()
)
closedLoopenablef1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    closedLoopenablef1.setStatus("mandatory")


class _ControlTypef1_Type(Integer32):
    """Custom type controlTypef1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ControlTypef1_Type.__name__ = "Integer32"
_ControlTypef1_Object = MibScalar
controlTypef1 = _ControlTypef1_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 3, 30),
    _ControlTypef1_Type()
)
controlTypef1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlTypef1.setStatus("mandatory")


class _Enablef1_Type(Integer32):
    """Custom type enablef1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Enablef1_Type.__name__ = "Integer32"
_Enablef1_Object = MibScalar
enablef1 = _Enablef1_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 3, 31),
    _Enablef1_Type()
)
enablef1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enablef1.setStatus("mandatory")
_Fan2Config_ObjectIdentity = ObjectIdentity
fan2Config = _Fan2Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46651, 1, 4)
)


class _SaveReloadConff2_Type(Integer32):
    """Custom type saveReloadConff2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_SaveReloadConff2_Type.__name__ = "Integer32"
_SaveReloadConff2_Object = MibScalar
saveReloadConff2 = _SaveReloadConff2_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 4, 1),
    _SaveReloadConff2_Type()
)
saveReloadConff2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saveReloadConff2.setStatus("mandatory")


class _OffTemprf2_Type(Integer32):
    """Custom type offTemprf2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-41, 101),
    )


_OffTemprf2_Type.__name__ = "Integer32"
_OffTemprf2_Object = MibScalar
offTemprf2 = _OffTemprf2_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 4, 2),
    _OffTemprf2_Type()
)
offTemprf2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    offTemprf2.setStatus("mandatory")


class _IdleOnTemprf2_Type(Integer32):
    """Custom type idleOnTemprf2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-41, 101),
    )


_IdleOnTemprf2_Type.__name__ = "Integer32"
_IdleOnTemprf2_Object = MibScalar
idleOnTemprf2 = _IdleOnTemprf2_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 4, 3),
    _IdleOnTemprf2_Type()
)
idleOnTemprf2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    idleOnTemprf2.setStatus("mandatory")


class _IdleEntryTemprf2_Type(Integer32):
    """Custom type idleEntryTemprf2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-41, 101),
    )


_IdleEntryTemprf2_Type.__name__ = "Integer32"
_IdleEntryTemprf2_Object = MibScalar
idleEntryTemprf2 = _IdleEntryTemprf2_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 4, 4),
    _IdleEntryTemprf2_Type()
)
idleEntryTemprf2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    idleEntryTemprf2.setStatus("mandatory")


class _MidPoint1Temprf2_Type(Integer32):
    """Custom type midPoint1Temprf2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-41, 101),
    )


_MidPoint1Temprf2_Type.__name__ = "Integer32"
_MidPoint1Temprf2_Object = MibScalar
midPoint1Temprf2 = _MidPoint1Temprf2_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 4, 5),
    _MidPoint1Temprf2_Type()
)
midPoint1Temprf2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midPoint1Temprf2.setStatus("mandatory")


class _SetPointTemprf2_Type(Integer32):
    """Custom type setPointTemprf2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-41, 101),
    )


_SetPointTemprf2_Type.__name__ = "Integer32"
_SetPointTemprf2_Object = MibScalar
setPointTemprf2 = _SetPointTemprf2_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 4, 6),
    _SetPointTemprf2_Type()
)
setPointTemprf2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPointTemprf2.setStatus("mandatory")


class _MidPoint2Temprf2_Type(Integer32):
    """Custom type midPoint2Temprf2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-41, 101),
    )


_MidPoint2Temprf2_Type.__name__ = "Integer32"
_MidPoint2Temprf2_Object = MibScalar
midPoint2Temprf2 = _MidPoint2Temprf2_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 4, 7),
    _MidPoint2Temprf2_Type()
)
midPoint2Temprf2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midPoint2Temprf2.setStatus("mandatory")


class _HighSpeedTemprf2_Type(Integer32):
    """Custom type highSpeedTemprf2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-41, 101),
    )


_HighSpeedTemprf2_Type.__name__ = "Integer32"
_HighSpeedTemprf2_Object = MibScalar
highSpeedTemprf2 = _HighSpeedTemprf2_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 4, 8),
    _HighSpeedTemprf2_Type()
)
highSpeedTemprf2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highSpeedTemprf2.setStatus("mandatory")


class _ExtendHighSpeedEntryTemprf2_Type(Integer32):
    """Custom type extendHighSpeedEntryTemprf2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-41, 101),
    )


_ExtendHighSpeedEntryTemprf2_Type.__name__ = "Integer32"
_ExtendHighSpeedEntryTemprf2_Object = MibScalar
extendHighSpeedEntryTemprf2 = _ExtendHighSpeedEntryTemprf2_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 4, 9),
    _ExtendHighSpeedEntryTemprf2_Type()
)
extendHighSpeedEntryTemprf2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extendHighSpeedEntryTemprf2.setStatus("mandatory")


class _ExtendHighSpeedExitTemprf2_Type(Integer32):
    """Custom type extendHighSpeedExitTemprf2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-41, 101),
    )


_ExtendHighSpeedExitTemprf2_Type.__name__ = "Integer32"
_ExtendHighSpeedExitTemprf2_Object = MibScalar
extendHighSpeedExitTemprf2 = _ExtendHighSpeedExitTemprf2_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 4, 10),
    _ExtendHighSpeedExitTemprf2_Type()
)
extendHighSpeedExitTemprf2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extendHighSpeedExitTemprf2.setStatus("mandatory")


class _BoostEntryTemprf2_Type(Integer32):
    """Custom type boostEntryTemprf2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-41, 101),
    )


_BoostEntryTemprf2_Type.__name__ = "Integer32"
_BoostEntryTemprf2_Object = MibScalar
boostEntryTemprf2 = _BoostEntryTemprf2_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 4, 11),
    _BoostEntryTemprf2_Type()
)
boostEntryTemprf2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boostEntryTemprf2.setStatus("mandatory")


class _BoostExitTemprf2_Type(Integer32):
    """Custom type boostExitTemprf2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-41, 101),
    )


_BoostExitTemprf2_Type.__name__ = "Integer32"
_BoostExitTemprf2_Object = MibScalar
boostExitTemprf2 = _BoostExitTemprf2_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 4, 12),
    _BoostExitTemprf2_Type()
)
boostExitTemprf2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boostExitTemprf2.setStatus("mandatory")


class _IdleRPMf2_Type(Integer32):
    """Custom type idleRPMf2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_IdleRPMf2_Type.__name__ = "Integer32"
_IdleRPMf2_Object = MibScalar
idleRPMf2 = _IdleRPMf2_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 4, 13),
    _IdleRPMf2_Type()
)
idleRPMf2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    idleRPMf2.setStatus("mandatory")


class _MidPointRPMf2_Type(Integer32):
    """Custom type midPointRPMf2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_MidPointRPMf2_Type.__name__ = "Integer32"
_MidPointRPMf2_Object = MibScalar
midPointRPMf2 = _MidPointRPMf2_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 4, 14),
    _MidPointRPMf2_Type()
)
midPointRPMf2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midPointRPMf2.setStatus("mandatory")


class _HighSpeedRPMf2_Type(Integer32):
    """Custom type highSpeedRPMf2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_HighSpeedRPMf2_Type.__name__ = "Integer32"
_HighSpeedRPMf2_Object = MibScalar
highSpeedRPMf2 = _HighSpeedRPMf2_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 4, 15),
    _HighSpeedRPMf2_Type()
)
highSpeedRPMf2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highSpeedRPMf2.setStatus("mandatory")


class _ExtendHighSpeedRPMf2_Type(Integer32):
    """Custom type extendHighSpeedRPMf2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_ExtendHighSpeedRPMf2_Type.__name__ = "Integer32"
_ExtendHighSpeedRPMf2_Object = MibScalar
extendHighSpeedRPMf2 = _ExtendHighSpeedRPMf2_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 4, 16),
    _ExtendHighSpeedRPMf2_Type()
)
extendHighSpeedRPMf2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extendHighSpeedRPMf2.setStatus("mandatory")


class _IdleDutyCyclef2_Type(Integer32):
    """Custom type idleDutyCyclef2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IdleDutyCyclef2_Type.__name__ = "Integer32"
_IdleDutyCyclef2_Object = MibScalar
idleDutyCyclef2 = _IdleDutyCyclef2_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 4, 17),
    _IdleDutyCyclef2_Type()
)
idleDutyCyclef2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    idleDutyCyclef2.setStatus("mandatory")


class _MidDutyCyclef2_Type(Integer32):
    """Custom type midDutyCyclef2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MidDutyCyclef2_Type.__name__ = "Integer32"
_MidDutyCyclef2_Object = MibScalar
midDutyCyclef2 = _MidDutyCyclef2_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 4, 18),
    _MidDutyCyclef2_Type()
)
midDutyCyclef2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midDutyCyclef2.setStatus("mandatory")


class _HighSpeedDutyCyclef2_Type(Integer32):
    """Custom type highSpeedDutyCyclef2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HighSpeedDutyCyclef2_Type.__name__ = "Integer32"
_HighSpeedDutyCyclef2_Object = MibScalar
highSpeedDutyCyclef2 = _HighSpeedDutyCyclef2_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 4, 19),
    _HighSpeedDutyCyclef2_Type()
)
highSpeedDutyCyclef2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highSpeedDutyCyclef2.setStatus("mandatory")


class _ExtendHighSpeedDutyCyclef2_Type(Integer32):
    """Custom type extendHighSpeedDutyCyclef2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ExtendHighSpeedDutyCyclef2_Type.__name__ = "Integer32"
_ExtendHighSpeedDutyCyclef2_Object = MibScalar
extendHighSpeedDutyCyclef2 = _ExtendHighSpeedDutyCyclef2_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 4, 20),
    _ExtendHighSpeedDutyCyclef2_Type()
)
extendHighSpeedDutyCyclef2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extendHighSpeedDutyCyclef2.setStatus("mandatory")


class _BoostDutyCyclef2_Type(Integer32):
    """Custom type boostDutyCyclef2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BoostDutyCyclef2_Type.__name__ = "Integer32"
_BoostDutyCyclef2_Object = MibScalar
boostDutyCyclef2 = _BoostDutyCyclef2_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 4, 21),
    _BoostDutyCyclef2_Type()
)
boostDutyCyclef2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boostDutyCyclef2.setStatus("mandatory")


class _DeadBandRPMf2_Type(Integer32):
    """Custom type deadBandRPMf2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_DeadBandRPMf2_Type.__name__ = "Integer32"
_DeadBandRPMf2_Object = MibScalar
deadBandRPMf2 = _DeadBandRPMf2_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 4, 22),
    _DeadBandRPMf2_Type()
)
deadBandRPMf2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deadBandRPMf2.setStatus("mandatory")


class _OverrideDigi1f2_Type(Integer32):
    """Custom type overrideDigi1f2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_OverrideDigi1f2_Type.__name__ = "Integer32"
_OverrideDigi1f2_Object = MibScalar
overrideDigi1f2 = _OverrideDigi1f2_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 4, 23),
    _OverrideDigi1f2_Type()
)
overrideDigi1f2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overrideDigi1f2.setStatus("mandatory")


class _OverrideDigi2f2_Type(Integer32):
    """Custom type overrideDigi2f2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_OverrideDigi2f2_Type.__name__ = "Integer32"
_OverrideDigi2f2_Object = MibScalar
overrideDigi2f2 = _OverrideDigi2f2_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 4, 24),
    _OverrideDigi2f2_Type()
)
overrideDigi2f2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overrideDigi2f2.setStatus("mandatory")


class _OverrideDigi3f2_Type(Integer32):
    """Custom type overrideDigi3f2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_OverrideDigi3f2_Type.__name__ = "Integer32"
_OverrideDigi3f2_Object = MibScalar
overrideDigi3f2 = _OverrideDigi3f2_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 4, 25),
    _OverrideDigi3f2_Type()
)
overrideDigi3f2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overrideDigi3f2.setStatus("mandatory")


class _OverrideSensorfailf2_Type(Integer32):
    """Custom type overrideSensorfailf2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_OverrideSensorfailf2_Type.__name__ = "Integer32"
_OverrideSensorfailf2_Object = MibScalar
overrideSensorfailf2 = _OverrideSensorfailf2_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 4, 26),
    _OverrideSensorfailf2_Type()
)
overrideSensorfailf2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overrideSensorfailf2.setStatus("mandatory")


class _SensorSelectf2_Type(Integer32):
    """Custom type sensorSelectf2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_SensorSelectf2_Type.__name__ = "Integer32"
_SensorSelectf2_Object = MibScalar
sensorSelectf2 = _SensorSelectf2_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 4, 27),
    _SensorSelectf2_Type()
)
sensorSelectf2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorSelectf2.setStatus("mandatory")


class _TachoPulseperrotationf2_Type(Integer32):
    """Custom type tachoPulseperrotationf2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TachoPulseperrotationf2_Type.__name__ = "Integer32"
_TachoPulseperrotationf2_Object = MibScalar
tachoPulseperrotationf2 = _TachoPulseperrotationf2_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 4, 28),
    _TachoPulseperrotationf2_Type()
)
tachoPulseperrotationf2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tachoPulseperrotationf2.setStatus("mandatory")


class _ClosedLoopenablef2_Type(Integer32):
    """Custom type closedLoopenablef2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ClosedLoopenablef2_Type.__name__ = "Integer32"
_ClosedLoopenablef2_Object = MibScalar
closedLoopenablef2 = _ClosedLoopenablef2_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 4, 29),
    _ClosedLoopenablef2_Type()
)
closedLoopenablef2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    closedLoopenablef2.setStatus("mandatory")


class _ControlTypef2_Type(Integer32):
    """Custom type controlTypef2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ControlTypef2_Type.__name__ = "Integer32"
_ControlTypef2_Object = MibScalar
controlTypef2 = _ControlTypef2_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 4, 30),
    _ControlTypef2_Type()
)
controlTypef2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlTypef2.setStatus("mandatory")


class _Enablef2_Type(Integer32):
    """Custom type enablef2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Enablef2_Type.__name__ = "Integer32"
_Enablef2_Object = MibScalar
enablef2 = _Enablef2_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 4, 31),
    _Enablef2_Type()
)
enablef2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enablef2.setStatus("mandatory")
_Damper1Config_ObjectIdentity = ObjectIdentity
damper1Config = _Damper1Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46651, 1, 5)
)


class _SaveReloadConfd1_Type(Integer32):
    """Custom type saveReloadConfd1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_SaveReloadConfd1_Type.__name__ = "Integer32"
_SaveReloadConfd1_Object = MibScalar
saveReloadConfd1 = _SaveReloadConfd1_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 5, 1),
    _SaveReloadConfd1_Type()
)
saveReloadConfd1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saveReloadConfd1.setStatus("mandatory")


class _LowercloseTemprd1_Type(Integer32):
    """Custom type lowercloseTemprd1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-41, 101),
    )


_LowercloseTemprd1_Type.__name__ = "Integer32"
_LowercloseTemprd1_Object = MibScalar
lowercloseTemprd1 = _LowercloseTemprd1_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 5, 2),
    _LowercloseTemprd1_Type()
)
lowercloseTemprd1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowercloseTemprd1.setStatus("mandatory")


class _SetPointd1_Type(Integer32):
    """Custom type setPointd1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-41, 101),
    )


_SetPointd1_Type.__name__ = "Integer32"
_SetPointd1_Object = MibScalar
setPointd1 = _SetPointd1_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 5, 3),
    _SetPointd1_Type()
)
setPointd1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPointd1.setStatus("mandatory")


class _UpperOpentempd1_Type(Integer32):
    """Custom type upperOpentempd1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-41, 101),
    )


_UpperOpentempd1_Type.__name__ = "Integer32"
_UpperOpentempd1_Object = MibScalar
upperOpentempd1 = _UpperOpentempd1_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 5, 4),
    _UpperOpentempd1_Type()
)
upperOpentempd1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upperOpentempd1.setStatus("mandatory")


class _UpperClosetempd1_Type(Integer32):
    """Custom type upperClosetempd1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-41, 101),
    )


_UpperClosetempd1_Type.__name__ = "Integer32"
_UpperClosetempd1_Object = MibScalar
upperClosetempd1 = _UpperClosetempd1_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 5, 5),
    _UpperClosetempd1_Type()
)
upperClosetempd1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upperClosetempd1.setStatus("mandatory")


class _EmgncyClosetempd1_Type(Integer32):
    """Custom type emgncyClosetempd1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-41, 101),
    )


_EmgncyClosetempd1_Type.__name__ = "Integer32"
_EmgncyClosetempd1_Object = MibScalar
emgncyClosetempd1 = _EmgncyClosetempd1_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 5, 6),
    _EmgncyClosetempd1_Type()
)
emgncyClosetempd1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emgncyClosetempd1.setStatus("mandatory")


class _Emgncyopentempd1_Type(Integer32):
    """Custom type emgncyopentempd1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-41, 101),
    )


_Emgncyopentempd1_Type.__name__ = "Integer32"
_Emgncyopentempd1_Object = MibScalar
emgncyopentempd1 = _Emgncyopentempd1_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 5, 7),
    _Emgncyopentempd1_Type()
)
emgncyopentempd1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emgncyopentempd1.setStatus("mandatory")


class _OverrideDigi1d1_Type(Integer32):
    """Custom type overrideDigi1d1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_OverrideDigi1d1_Type.__name__ = "Integer32"
_OverrideDigi1d1_Object = MibScalar
overrideDigi1d1 = _OverrideDigi1d1_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 5, 8),
    _OverrideDigi1d1_Type()
)
overrideDigi1d1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overrideDigi1d1.setStatus("mandatory")


class _OverrideDigi2d1_Type(Integer32):
    """Custom type overrideDigi2d1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_OverrideDigi2d1_Type.__name__ = "Integer32"
_OverrideDigi2d1_Object = MibScalar
overrideDigi2d1 = _OverrideDigi2d1_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 5, 9),
    _OverrideDigi2d1_Type()
)
overrideDigi2d1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overrideDigi2d1.setStatus("mandatory")


class _OverrideDigi3d1_Type(Integer32):
    """Custom type overrideDigi3d1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_OverrideDigi3d1_Type.__name__ = "Integer32"
_OverrideDigi3d1_Object = MibScalar
overrideDigi3d1 = _OverrideDigi3d1_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 5, 10),
    _OverrideDigi3d1_Type()
)
overrideDigi3d1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overrideDigi3d1.setStatus("mandatory")


class _OverrideSensorFaild1_Type(Integer32):
    """Custom type overrideSensorFaild1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_OverrideSensorFaild1_Type.__name__ = "Integer32"
_OverrideSensorFaild1_Object = MibScalar
overrideSensorFaild1 = _OverrideSensorFaild1_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 5, 11),
    _OverrideSensorFaild1_Type()
)
overrideSensorFaild1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overrideSensorFaild1.setStatus("mandatory")


class _SensSelectd1_Type(Integer32):
    """Custom type sensSelectd1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_SensSelectd1_Type.__name__ = "Integer32"
_SensSelectd1_Object = MibScalar
sensSelectd1 = _SensSelectd1_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 5, 12),
    _SensSelectd1_Type()
)
sensSelectd1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensSelectd1.setStatus("mandatory")


class _RunDurationd1_Type(Integer32):
    """Custom type runDurationd1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 300),
    )


_RunDurationd1_Type.__name__ = "Integer32"
_RunDurationd1_Object = MibScalar
runDurationd1 = _RunDurationd1_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 5, 13),
    _RunDurationd1_Type()
)
runDurationd1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    runDurationd1.setStatus("mandatory")


class _Enabled1_Type(Integer32):
    """Custom type enabled1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Enabled1_Type.__name__ = "Integer32"
_Enabled1_Object = MibScalar
enabled1 = _Enabled1_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 5, 14),
    _Enabled1_Type()
)
enabled1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enabled1.setStatus("mandatory")
_Damper2Config_ObjectIdentity = ObjectIdentity
damper2Config = _Damper2Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46651, 1, 6)
)


class _SaveReloadConfd2_Type(Integer32):
    """Custom type saveReloadConfd2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_SaveReloadConfd2_Type.__name__ = "Integer32"
_SaveReloadConfd2_Object = MibScalar
saveReloadConfd2 = _SaveReloadConfd2_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 6, 1),
    _SaveReloadConfd2_Type()
)
saveReloadConfd2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saveReloadConfd2.setStatus("mandatory")


class _LowercloseTemprd2_Type(Integer32):
    """Custom type lowercloseTemprd2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-41, 101),
    )


_LowercloseTemprd2_Type.__name__ = "Integer32"
_LowercloseTemprd2_Object = MibScalar
lowercloseTemprd2 = _LowercloseTemprd2_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 6, 2),
    _LowercloseTemprd2_Type()
)
lowercloseTemprd2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowercloseTemprd2.setStatus("mandatory")


class _SetPointd2_Type(Integer32):
    """Custom type setPointd2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-41, 101),
    )


_SetPointd2_Type.__name__ = "Integer32"
_SetPointd2_Object = MibScalar
setPointd2 = _SetPointd2_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 6, 3),
    _SetPointd2_Type()
)
setPointd2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPointd2.setStatus("mandatory")


class _UpperOpentempd2_Type(Integer32):
    """Custom type upperOpentempd2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-41, 101),
    )


_UpperOpentempd2_Type.__name__ = "Integer32"
_UpperOpentempd2_Object = MibScalar
upperOpentempd2 = _UpperOpentempd2_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 6, 4),
    _UpperOpentempd2_Type()
)
upperOpentempd2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upperOpentempd2.setStatus("mandatory")


class _UpperClosetempd2_Type(Integer32):
    """Custom type upperClosetempd2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-41, 101),
    )


_UpperClosetempd2_Type.__name__ = "Integer32"
_UpperClosetempd2_Object = MibScalar
upperClosetempd2 = _UpperClosetempd2_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 6, 5),
    _UpperClosetempd2_Type()
)
upperClosetempd2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upperClosetempd2.setStatus("mandatory")


class _EmgncyClosetempd2_Type(Integer32):
    """Custom type emgncyClosetempd2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-41, 101),
    )


_EmgncyClosetempd2_Type.__name__ = "Integer32"
_EmgncyClosetempd2_Object = MibScalar
emgncyClosetempd2 = _EmgncyClosetempd2_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 6, 6),
    _EmgncyClosetempd2_Type()
)
emgncyClosetempd2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emgncyClosetempd2.setStatus("mandatory")


class _Emgncyopentempd2_Type(Integer32):
    """Custom type emgncyopentempd2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-41, 101),
    )


_Emgncyopentempd2_Type.__name__ = "Integer32"
_Emgncyopentempd2_Object = MibScalar
emgncyopentempd2 = _Emgncyopentempd2_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 6, 7),
    _Emgncyopentempd2_Type()
)
emgncyopentempd2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emgncyopentempd2.setStatus("mandatory")


class _OverrideDigi1d2_Type(Integer32):
    """Custom type overrideDigi1d2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_OverrideDigi1d2_Type.__name__ = "Integer32"
_OverrideDigi1d2_Object = MibScalar
overrideDigi1d2 = _OverrideDigi1d2_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 6, 8),
    _OverrideDigi1d2_Type()
)
overrideDigi1d2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overrideDigi1d2.setStatus("mandatory")


class _OverrideDigi2d2_Type(Integer32):
    """Custom type overrideDigi2d2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_OverrideDigi2d2_Type.__name__ = "Integer32"
_OverrideDigi2d2_Object = MibScalar
overrideDigi2d2 = _OverrideDigi2d2_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 6, 9),
    _OverrideDigi2d2_Type()
)
overrideDigi2d2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overrideDigi2d2.setStatus("mandatory")


class _OverrideDigi3d2_Type(Integer32):
    """Custom type overrideDigi3d2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_OverrideDigi3d2_Type.__name__ = "Integer32"
_OverrideDigi3d2_Object = MibScalar
overrideDigi3d2 = _OverrideDigi3d2_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 6, 10),
    _OverrideDigi3d2_Type()
)
overrideDigi3d2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overrideDigi3d2.setStatus("mandatory")


class _OverrideSensorFaild2_Type(Integer32):
    """Custom type overrideSensorFaild2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_OverrideSensorFaild2_Type.__name__ = "Integer32"
_OverrideSensorFaild2_Object = MibScalar
overrideSensorFaild2 = _OverrideSensorFaild2_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 6, 11),
    _OverrideSensorFaild2_Type()
)
overrideSensorFaild2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overrideSensorFaild2.setStatus("mandatory")


class _SensSelectd2_Type(Integer32):
    """Custom type sensSelectd2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_SensSelectd2_Type.__name__ = "Integer32"
_SensSelectd2_Object = MibScalar
sensSelectd2 = _SensSelectd2_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 6, 12),
    _SensSelectd2_Type()
)
sensSelectd2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensSelectd2.setStatus("mandatory")


class _RunDurationd2_Type(Integer32):
    """Custom type runDurationd2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 300),
    )


_RunDurationd2_Type.__name__ = "Integer32"
_RunDurationd2_Object = MibScalar
runDurationd2 = _RunDurationd2_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 6, 13),
    _RunDurationd2_Type()
)
runDurationd2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    runDurationd2.setStatus("mandatory")


class _Enabled2_Type(Integer32):
    """Custom type enabled2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Enabled2_Type.__name__ = "Integer32"
_Enabled2_Object = MibScalar
enabled2 = _Enabled2_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 6, 14),
    _Enabled2_Type()
)
enabled2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enabled2.setStatus("mandatory")
_Aircon1Config_ObjectIdentity = ObjectIdentity
aircon1Config = _Aircon1Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46651, 1, 7)
)


class _SaveReloadConfac1_Type(Integer32):
    """Custom type saveReloadConfac1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_SaveReloadConfac1_Type.__name__ = "Integer32"
_SaveReloadConfac1_Object = MibScalar
saveReloadConfac1 = _SaveReloadConfac1_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 7, 1),
    _SaveReloadConfac1_Type()
)
saveReloadConfac1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saveReloadConfac1.setStatus("mandatory")


class _ONTemprac1_Type(Integer32):
    """Custom type oNTemprac1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-41, 101),
    )


_ONTemprac1_Type.__name__ = "Integer32"
_ONTemprac1_Object = MibScalar
oNTemprac1 = _ONTemprac1_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 7, 2),
    _ONTemprac1_Type()
)
oNTemprac1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oNTemprac1.setStatus("mandatory")


class _OFFTemprac1_Type(Integer32):
    """Custom type oFFTemprac1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-41, 101),
    )


_OFFTemprac1_Type.__name__ = "Integer32"
_OFFTemprac1_Object = MibScalar
oFFTemprac1 = _OFFTemprac1_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 7, 3),
    _OFFTemprac1_Type()
)
oFFTemprac1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oFFTemprac1.setStatus("mandatory")


class _OverrideDigi1ac1_Type(Integer32):
    """Custom type overrideDigi1ac1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_OverrideDigi1ac1_Type.__name__ = "Integer32"
_OverrideDigi1ac1_Object = MibScalar
overrideDigi1ac1 = _OverrideDigi1ac1_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 7, 4),
    _OverrideDigi1ac1_Type()
)
overrideDigi1ac1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overrideDigi1ac1.setStatus("mandatory")


class _OverrideDigi2ac1_Type(Integer32):
    """Custom type overrideDigi2ac1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_OverrideDigi2ac1_Type.__name__ = "Integer32"
_OverrideDigi2ac1_Object = MibScalar
overrideDigi2ac1 = _OverrideDigi2ac1_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 7, 5),
    _OverrideDigi2ac1_Type()
)
overrideDigi2ac1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overrideDigi2ac1.setStatus("mandatory")


class _OverrideDigi3ac1_Type(Integer32):
    """Custom type overrideDigi3ac1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_OverrideDigi3ac1_Type.__name__ = "Integer32"
_OverrideDigi3ac1_Object = MibScalar
overrideDigi3ac1 = _OverrideDigi3ac1_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 7, 6),
    _OverrideDigi3ac1_Type()
)
overrideDigi3ac1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overrideDigi3ac1.setStatus("mandatory")


class _OverrideSensorFailac1_Type(Integer32):
    """Custom type overrideSensorFailac1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_OverrideSensorFailac1_Type.__name__ = "Integer32"
_OverrideSensorFailac1_Object = MibScalar
overrideSensorFailac1 = _OverrideSensorFailac1_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 7, 7),
    _OverrideSensorFailac1_Type()
)
overrideSensorFailac1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overrideSensorFailac1.setStatus("mandatory")


class _SensSelectac1_Type(Integer32):
    """Custom type sensSelectac1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_SensSelectac1_Type.__name__ = "Integer32"
_SensSelectac1_Object = MibScalar
sensSelectac1 = _SensSelectac1_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 7, 8),
    _SensSelectac1_Type()
)
sensSelectac1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensSelectac1.setStatus("mandatory")


class _MinimumRunDurationac1_Type(Integer32):
    """Custom type minimumRunDurationac1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_MinimumRunDurationac1_Type.__name__ = "Integer32"
_MinimumRunDurationac1_Object = MibScalar
minimumRunDurationac1 = _MinimumRunDurationac1_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 7, 9),
    _MinimumRunDurationac1_Type()
)
minimumRunDurationac1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minimumRunDurationac1.setStatus("mandatory")


class _RestartTimeoutac1_Type(Integer32):
    """Custom type restartTimeoutac1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_RestartTimeoutac1_Type.__name__ = "Integer32"
_RestartTimeoutac1_Object = MibScalar
restartTimeoutac1 = _RestartTimeoutac1_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 7, 10),
    _RestartTimeoutac1_Type()
)
restartTimeoutac1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restartTimeoutac1.setStatus("mandatory")


class _Enableac1_Type(Integer32):
    """Custom type enableac1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Enableac1_Type.__name__ = "Integer32"
_Enableac1_Object = MibScalar
enableac1 = _Enableac1_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 7, 11),
    _Enableac1_Type()
)
enableac1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableac1.setStatus("mandatory")
_Aircon2Config_ObjectIdentity = ObjectIdentity
aircon2Config = _Aircon2Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46651, 1, 8)
)


class _SaveReloadConfac2_Type(Integer32):
    """Custom type saveReloadConfac2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_SaveReloadConfac2_Type.__name__ = "Integer32"
_SaveReloadConfac2_Object = MibScalar
saveReloadConfac2 = _SaveReloadConfac2_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 8, 1),
    _SaveReloadConfac2_Type()
)
saveReloadConfac2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saveReloadConfac2.setStatus("mandatory")


class _OnTemprac2_Type(Integer32):
    """Custom type onTemprac2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-41, 101),
    )


_OnTemprac2_Type.__name__ = "Integer32"
_OnTemprac2_Object = MibScalar
onTemprac2 = _OnTemprac2_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 8, 2),
    _OnTemprac2_Type()
)
onTemprac2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onTemprac2.setStatus("mandatory")


class _OffTemprac2_Type(Integer32):
    """Custom type offTemprac2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-41, 101),
    )


_OffTemprac2_Type.__name__ = "Integer32"
_OffTemprac2_Object = MibScalar
offTemprac2 = _OffTemprac2_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 8, 3),
    _OffTemprac2_Type()
)
offTemprac2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    offTemprac2.setStatus("mandatory")


class _OverrideDigi1ac2_Type(Integer32):
    """Custom type overrideDigi1ac2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_OverrideDigi1ac2_Type.__name__ = "Integer32"
_OverrideDigi1ac2_Object = MibScalar
overrideDigi1ac2 = _OverrideDigi1ac2_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 8, 4),
    _OverrideDigi1ac2_Type()
)
overrideDigi1ac2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overrideDigi1ac2.setStatus("mandatory")


class _OverrideDigi2ac2_Type(Integer32):
    """Custom type overrideDigi2ac2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_OverrideDigi2ac2_Type.__name__ = "Integer32"
_OverrideDigi2ac2_Object = MibScalar
overrideDigi2ac2 = _OverrideDigi2ac2_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 8, 5),
    _OverrideDigi2ac2_Type()
)
overrideDigi2ac2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overrideDigi2ac2.setStatus("mandatory")


class _OverrideDigi3ac2_Type(Integer32):
    """Custom type overrideDigi3ac2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_OverrideDigi3ac2_Type.__name__ = "Integer32"
_OverrideDigi3ac2_Object = MibScalar
overrideDigi3ac2 = _OverrideDigi3ac2_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 8, 6),
    _OverrideDigi3ac2_Type()
)
overrideDigi3ac2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overrideDigi3ac2.setStatus("mandatory")


class _OverrideSensorFailac2_Type(Integer32):
    """Custom type overrideSensorFailac2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_OverrideSensorFailac2_Type.__name__ = "Integer32"
_OverrideSensorFailac2_Object = MibScalar
overrideSensorFailac2 = _OverrideSensorFailac2_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 8, 7),
    _OverrideSensorFailac2_Type()
)
overrideSensorFailac2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overrideSensorFailac2.setStatus("mandatory")


class _SensSelectac2_Type(Integer32):
    """Custom type sensSelectac2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_SensSelectac2_Type.__name__ = "Integer32"
_SensSelectac2_Object = MibScalar
sensSelectac2 = _SensSelectac2_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 8, 8),
    _SensSelectac2_Type()
)
sensSelectac2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensSelectac2.setStatus("mandatory")


class _MinimumRunDurationac2_Type(Integer32):
    """Custom type minimumRunDurationac2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_MinimumRunDurationac2_Type.__name__ = "Integer32"
_MinimumRunDurationac2_Object = MibScalar
minimumRunDurationac2 = _MinimumRunDurationac2_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 8, 9),
    _MinimumRunDurationac2_Type()
)
minimumRunDurationac2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minimumRunDurationac2.setStatus("mandatory")


class _RestartTimeoutac2_Type(Integer32):
    """Custom type restartTimeoutac2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_RestartTimeoutac2_Type.__name__ = "Integer32"
_RestartTimeoutac2_Object = MibScalar
restartTimeoutac2 = _RestartTimeoutac2_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 8, 10),
    _RestartTimeoutac2_Type()
)
restartTimeoutac2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restartTimeoutac2.setStatus("mandatory")


class _Enableac2_Type(Integer32):
    """Custom type enableac2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Enableac2_Type.__name__ = "Integer32"
_Enableac2_Object = MibScalar
enableac2 = _Enableac2_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 8, 11),
    _Enableac2_Type()
)
enableac2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableac2.setStatus("mandatory")
_HeaterConfig_ObjectIdentity = ObjectIdentity
heaterConfig = _HeaterConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46651, 1, 9)
)


class _SaveReloadConfhtr_Type(Integer32):
    """Custom type saveReloadConfhtr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_SaveReloadConfhtr_Type.__name__ = "Integer32"
_SaveReloadConfhtr_Object = MibScalar
saveReloadConfhtr = _SaveReloadConfhtr_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 9, 1),
    _SaveReloadConfhtr_Type()
)
saveReloadConfhtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saveReloadConfhtr.setStatus("mandatory")


class _OnTemprhtr_Type(Integer32):
    """Custom type onTemprhtr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-41, 101),
    )


_OnTemprhtr_Type.__name__ = "Integer32"
_OnTemprhtr_Object = MibScalar
onTemprhtr = _OnTemprhtr_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 9, 2),
    _OnTemprhtr_Type()
)
onTemprhtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onTemprhtr.setStatus("mandatory")


class _OffTemprhtr_Type(Integer32):
    """Custom type offTemprhtr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-41, 101),
    )


_OffTemprhtr_Type.__name__ = "Integer32"
_OffTemprhtr_Object = MibScalar
offTemprhtr = _OffTemprhtr_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 9, 3),
    _OffTemprhtr_Type()
)
offTemprhtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    offTemprhtr.setStatus("mandatory")


class _OverrideDigi1htr_Type(Integer32):
    """Custom type overrideDigi1htr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_OverrideDigi1htr_Type.__name__ = "Integer32"
_OverrideDigi1htr_Object = MibScalar
overrideDigi1htr = _OverrideDigi1htr_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 9, 4),
    _OverrideDigi1htr_Type()
)
overrideDigi1htr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overrideDigi1htr.setStatus("mandatory")


class _OverrideDigi2htr_Type(Integer32):
    """Custom type overrideDigi2htr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_OverrideDigi2htr_Type.__name__ = "Integer32"
_OverrideDigi2htr_Object = MibScalar
overrideDigi2htr = _OverrideDigi2htr_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 9, 5),
    _OverrideDigi2htr_Type()
)
overrideDigi2htr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overrideDigi2htr.setStatus("mandatory")


class _OverrideDigi3htr_Type(Integer32):
    """Custom type overrideDigi3htr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_OverrideDigi3htr_Type.__name__ = "Integer32"
_OverrideDigi3htr_Object = MibScalar
overrideDigi3htr = _OverrideDigi3htr_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 9, 6),
    _OverrideDigi3htr_Type()
)
overrideDigi3htr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overrideDigi3htr.setStatus("mandatory")


class _OverrideSensorFailhtr_Type(Integer32):
    """Custom type overrideSensorFailhtr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_OverrideSensorFailhtr_Type.__name__ = "Integer32"
_OverrideSensorFailhtr_Object = MibScalar
overrideSensorFailhtr = _OverrideSensorFailhtr_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 9, 7),
    _OverrideSensorFailhtr_Type()
)
overrideSensorFailhtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overrideSensorFailhtr.setStatus("mandatory")


class _SensSelecthtr_Type(Integer32):
    """Custom type sensSelecthtr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_SensSelecthtr_Type.__name__ = "Integer32"
_SensSelecthtr_Object = MibScalar
sensSelecthtr = _SensSelecthtr_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 9, 8),
    _SensSelecthtr_Type()
)
sensSelecthtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensSelecthtr.setStatus("mandatory")


class _Enablehtr_Type(Integer32):
    """Custom type enablehtr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Enablehtr_Type.__name__ = "Integer32"
_Enablehtr_Object = MibScalar
enablehtr = _Enablehtr_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 9, 9),
    _Enablehtr_Type()
)
enablehtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enablehtr.setStatus("mandatory")
_HumidityConfig_ObjectIdentity = ObjectIdentity
humidityConfig = _HumidityConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46651, 1, 10)
)


class _SaveReloadConfhum_Type(Integer32):
    """Custom type saveReloadConfhum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_SaveReloadConfhum_Type.__name__ = "Integer32"
_SaveReloadConfhum_Object = MibScalar
saveReloadConfhum = _SaveReloadConfhum_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 10, 1),
    _SaveReloadConfhum_Type()
)
saveReloadConfhum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saveReloadConfhum.setStatus("mandatory")


class _RhEntryhum_Type(Integer32):
    """Custom type rhEntryhum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(40, 100),
    )


_RhEntryhum_Type.__name__ = "Integer32"
_RhEntryhum_Object = MibScalar
rhEntryhum = _RhEntryhum_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 10, 2),
    _RhEntryhum_Type()
)
rhEntryhum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rhEntryhum.setStatus("mandatory")


class _RhExithum_Type(Integer32):
    """Custom type rhExithum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(40, 100),
    )


_RhExithum_Type.__name__ = "Integer32"
_RhExithum_Object = MibScalar
rhExithum = _RhExithum_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 10, 3),
    _RhExithum_Type()
)
rhExithum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rhExithum.setStatus("mandatory")


class _Coolingmodehum_Type(Integer32):
    """Custom type coolingmodehum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Coolingmodehum_Type.__name__ = "Integer32"
_Coolingmodehum_Object = MibScalar
coolingmodehum = _Coolingmodehum_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 10, 4),
    _Coolingmodehum_Type()
)
coolingmodehum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coolingmodehum.setStatus("mandatory")


class _Temprsetpoffsethum_Type(Integer32):
    """Custom type temprsetpoffsethum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 10),
    )


_Temprsetpoffsethum_Type.__name__ = "Integer32"
_Temprsetpoffsethum_Object = MibScalar
temprsetpoffsethum = _Temprsetpoffsethum_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 10, 5),
    _Temprsetpoffsethum_Type()
)
temprsetpoffsethum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temprsetpoffsethum.setStatus("mandatory")


class _RhSensPositionhum_Type(Integer32):
    """Custom type rhSensPositionhum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RhSensPositionhum_Type.__name__ = "Integer32"
_RhSensPositionhum_Object = MibScalar
rhSensPositionhum = _RhSensPositionhum_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 10, 6),
    _RhSensPositionhum_Type()
)
rhSensPositionhum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rhSensPositionhum.setStatus("mandatory")


class _Enablehum_Type(Integer32):
    """Custom type enablehum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Enablehum_Type.__name__ = "Integer32"
_Enablehum_Object = MibScalar
enablehum = _Enablehum_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 10, 7),
    _Enablehum_Type()
)
enablehum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enablehum.setStatus("mandatory")
_SystemConfig_ObjectIdentity = ObjectIdentity
systemConfig = _SystemConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11)
)


class _SaveReloadConfsysc_Type(Integer32):
    """Custom type saveReloadConfsysc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_SaveReloadConfsysc_Type.__name__ = "Integer32"
_SaveReloadConfsysc_Object = MibScalar
saveReloadConfsysc = _SaveReloadConfsysc_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 1),
    _SaveReloadConfsysc_Type()
)
saveReloadConfsysc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saveReloadConfsysc.setStatus("mandatory")


class _VdcLowEntrysys_Type(Integer32):
    """Custom type vdcLowEntrysys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(18, 60),
    )


_VdcLowEntrysys_Type.__name__ = "Integer32"
_VdcLowEntrysys_Object = MibScalar
vdcLowEntrysys = _VdcLowEntrysys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 2),
    _VdcLowEntrysys_Type()
)
vdcLowEntrysys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdcLowEntrysys.setStatus("mandatory")


class _VdcLowExitsys_Type(Integer32):
    """Custom type vdcLowExitsys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(18, 60),
    )


_VdcLowExitsys_Type.__name__ = "Integer32"
_VdcLowExitsys_Object = MibScalar
vdcLowExitsys = _VdcLowExitsys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 3),
    _VdcLowExitsys_Type()
)
vdcLowExitsys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdcLowExitsys.setStatus("mandatory")


class _VdcHighEntrysys_Type(Integer32):
    """Custom type vdcHighEntrysys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(18, 60),
    )


_VdcHighEntrysys_Type.__name__ = "Integer32"
_VdcHighEntrysys_Object = MibScalar
vdcHighEntrysys = _VdcHighEntrysys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 4),
    _VdcHighEntrysys_Type()
)
vdcHighEntrysys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdcHighEntrysys.setStatus("mandatory")


class _VdcHighExitsys_Type(Integer32):
    """Custom type vdcHighExitsys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(18, 60),
    )


_VdcHighExitsys_Type.__name__ = "Integer32"
_VdcHighExitsys_Object = MibScalar
vdcHighExitsys = _VdcHighExitsys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 5),
    _VdcHighExitsys_Type()
)
vdcHighExitsys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdcHighExitsys.setStatus("mandatory")


class _TemprLowlimitsys_Type(Integer32):
    """Custom type temprLowlimitsys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 80),
    )


_TemprLowlimitsys_Type.__name__ = "Integer32"
_TemprLowlimitsys_Object = MibScalar
temprLowlimitsys = _TemprLowlimitsys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 6),
    _TemprLowlimitsys_Type()
)
temprLowlimitsys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temprLowlimitsys.setStatus("mandatory")


class _TemprHighlimit1sys_Type(Integer32):
    """Custom type temprHighlimit1sys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 80),
    )


_TemprHighlimit1sys_Type.__name__ = "Integer32"
_TemprHighlimit1sys_Object = MibScalar
temprHighlimit1sys = _TemprHighlimit1sys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 7),
    _TemprHighlimit1sys_Type()
)
temprHighlimit1sys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temprHighlimit1sys.setStatus("mandatory")


class _TemprHighlimit2sys_Type(Integer32):
    """Custom type temprHighlimit2sys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 80),
    )


_TemprHighlimit2sys_Type.__name__ = "Integer32"
_TemprHighlimit2sys_Object = MibScalar
temprHighlimit2sys = _TemprHighlimit2sys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 8),
    _TemprHighlimit2sys_Type()
)
temprHighlimit2sys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temprHighlimit2sys.setStatus("mandatory")


class _TemprHighlimit3sys_Type(Integer32):
    """Custom type temprHighlimit3sys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 80),
    )


_TemprHighlimit3sys_Type.__name__ = "Integer32"
_TemprHighlimit3sys_Object = MibScalar
temprHighlimit3sys = _TemprHighlimit3sys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 9),
    _TemprHighlimit3sys_Type()
)
temprHighlimit3sys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temprHighlimit3sys.setStatus("mandatory")


class _Temprlimithyssys_Type(Integer32):
    """Custom type temprlimithyssys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, 20),
    )


_Temprlimithyssys_Type.__name__ = "Integer32"
_Temprlimithyssys_Object = MibScalar
temprlimithyssys = _Temprlimithyssys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 10),
    _Temprlimithyssys_Type()
)
temprlimithyssys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temprlimithyssys.setStatus("mandatory")


class _RhLowlimitsys_Type(Integer32):
    """Custom type rhLowlimitsys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RhLowlimitsys_Type.__name__ = "Integer32"
_RhLowlimitsys_Object = MibScalar
rhLowlimitsys = _RhLowlimitsys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 11),
    _RhLowlimitsys_Type()
)
rhLowlimitsys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rhLowlimitsys.setStatus("mandatory")


class _RhHighlimitsys_Type(Integer32):
    """Custom type rhHighlimitsys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RhHighlimitsys_Type.__name__ = "Integer32"
_RhHighlimitsys_Object = MibScalar
rhHighlimitsys = _RhHighlimitsys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 12),
    _RhHighlimitsys_Type()
)
rhHighlimitsys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rhHighlimitsys.setStatus("mandatory")


class _Flowpresslimit1sys_Type(Integer32):
    """Custom type flowpresslimit1sys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 400),
    )


_Flowpresslimit1sys_Type.__name__ = "Integer32"
_Flowpresslimit1sys_Object = MibScalar
flowpresslimit1sys = _Flowpresslimit1sys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 13),
    _Flowpresslimit1sys_Type()
)
flowpresslimit1sys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowpresslimit1sys.setStatus("mandatory")


class _Flowpresslimit2sys_Type(Integer32):
    """Custom type flowpresslimit2sys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 400),
    )


_Flowpresslimit2sys_Type.__name__ = "Integer32"
_Flowpresslimit2sys_Object = MibScalar
flowpresslimit2sys = _Flowpresslimit2sys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 14),
    _Flowpresslimit2sys_Type()
)
flowpresslimit2sys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowpresslimit2sys.setStatus("mandatory")


class _Flowpresshyssys_Type(Integer32):
    """Custom type flowpresshyssys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 400),
    )


_Flowpresshyssys_Type.__name__ = "Integer32"
_Flowpresshyssys_Object = MibScalar
flowpresshyssys = _Flowpresshyssys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 15),
    _Flowpresshyssys_Type()
)
flowpresshyssys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowpresshyssys.setStatus("mandatory")


class _Coolingzonessys_Type(Integer32):
    """Custom type coolingzonessys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Coolingzonessys_Type.__name__ = "Integer32"
_Coolingzonessys_Object = MibScalar
coolingzonessys = _Coolingzonessys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 16),
    _Coolingzonessys_Type()
)
coolingzonessys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coolingzonessys.setStatus("mandatory")


class _CoolingModesys_Type(Integer32):
    """Custom type coolingModesys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_CoolingModesys_Type.__name__ = "Integer32"
_CoolingModesys_Object = MibScalar
coolingModesys = _CoolingModesys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 17),
    _CoolingModesys_Type()
)
coolingModesys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coolingModesys.setStatus("mandatory")


class _NegCoolingDeltaOverridesys_Type(Integer32):
    """Custom type negCoolingDeltaOverridesys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NegCoolingDeltaOverridesys_Type.__name__ = "Integer32"
_NegCoolingDeltaOverridesys_Object = MibScalar
negCoolingDeltaOverridesys = _NegCoolingDeltaOverridesys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 18),
    _NegCoolingDeltaOverridesys_Type()
)
negCoolingDeltaOverridesys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    negCoolingDeltaOverridesys.setStatus("mandatory")


class _NegCoolingDeltaHyssys_Type(Integer32):
    """Custom type negCoolingDeltaHyssys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 10),
    )


_NegCoolingDeltaHyssys_Type.__name__ = "Integer32"
_NegCoolingDeltaHyssys_Object = MibScalar
negCoolingDeltaHyssys = _NegCoolingDeltaHyssys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 19),
    _NegCoolingDeltaHyssys_Type()
)
negCoolingDeltaHyssys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    negCoolingDeltaHyssys.setStatus("mandatory")


class _CoolingDeltatempsys_Type(Integer32):
    """Custom type coolingDeltatempsys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 10),
    )


_CoolingDeltatempsys_Type.__name__ = "Integer32"
_CoolingDeltatempsys_Object = MibScalar
coolingDeltatempsys = _CoolingDeltatempsys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 20),
    _CoolingDeltatempsys_Type()
)
coolingDeltatempsys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coolingDeltatempsys.setStatus("mandatory")


class _ShelterTemprsys_Type(Integer32):
    """Custom type shelterTemprsys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_ShelterTemprsys_Type.__name__ = "Integer32"
_ShelterTemprsys_Object = MibScalar
shelterTemprsys = _ShelterTemprsys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 21),
    _ShelterTemprsys_Type()
)
shelterTemprsys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shelterTemprsys.setStatus("mandatory")


class _Acleadlagsys_Type(Integer32):
    """Custom type acleadlagsys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Acleadlagsys_Type.__name__ = "Integer32"
_Acleadlagsys_Object = MibScalar
acleadlagsys = _Acleadlagsys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 22),
    _Acleadlagsys_Type()
)
acleadlagsys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acleadlagsys.setStatus("mandatory")


class _CoolingModeXzonesys_Type(Integer32):
    """Custom type coolingModeXzonesys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_CoolingModeXzonesys_Type.__name__ = "Integer32"
_CoolingModeXzonesys_Object = MibScalar
coolingModeXzonesys = _CoolingModeXzonesys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 23),
    _CoolingModeXzonesys_Type()
)
coolingModeXzonesys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coolingModeXzonesys.setStatus("mandatory")


class _NegCoolingDeltaOverrideXzonesys_Type(Integer32):
    """Custom type negCoolingDeltaOverrideXzonesys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NegCoolingDeltaOverrideXzonesys_Type.__name__ = "Integer32"
_NegCoolingDeltaOverrideXzonesys_Object = MibScalar
negCoolingDeltaOverrideXzonesys = _NegCoolingDeltaOverrideXzonesys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 24),
    _NegCoolingDeltaOverrideXzonesys_Type()
)
negCoolingDeltaOverrideXzonesys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    negCoolingDeltaOverrideXzonesys.setStatus("mandatory")


class _NegCoolingDeltaHysXzonesys_Type(Integer32):
    """Custom type negCoolingDeltaHysXzonesys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 10),
    )


_NegCoolingDeltaHysXzonesys_Type.__name__ = "Integer32"
_NegCoolingDeltaHysXzonesys_Object = MibScalar
negCoolingDeltaHysXzonesys = _NegCoolingDeltaHysXzonesys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 25),
    _NegCoolingDeltaHysXzonesys_Type()
)
negCoolingDeltaHysXzonesys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    negCoolingDeltaHysXzonesys.setStatus("mandatory")


class _CoolingDeltatempXzonesys_Type(Integer32):
    """Custom type coolingDeltatempXzonesys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 10),
    )


_CoolingDeltatempXzonesys_Type.__name__ = "Integer32"
_CoolingDeltatempXzonesys_Object = MibScalar
coolingDeltatempXzonesys = _CoolingDeltatempXzonesys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 26),
    _CoolingDeltatempXzonesys_Type()
)
coolingDeltatempXzonesys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coolingDeltatempXzonesys.setStatus("mandatory")


class _Fan1Zonesys_Type(Integer32):
    """Custom type fan1Zonesys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Fan1Zonesys_Type.__name__ = "Integer32"
_Fan1Zonesys_Object = MibScalar
fan1Zonesys = _Fan1Zonesys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 27),
    _Fan1Zonesys_Type()
)
fan1Zonesys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fan1Zonesys.setStatus("mandatory")


class _Fan2Zonesys_Type(Integer32):
    """Custom type fan2Zonesys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Fan2Zonesys_Type.__name__ = "Integer32"
_Fan2Zonesys_Object = MibScalar
fan2Zonesys = _Fan2Zonesys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 28),
    _Fan2Zonesys_Type()
)
fan2Zonesys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fan2Zonesys.setStatus("mandatory")


class _Ac1Zonesys_Type(Integer32):
    """Custom type ac1Zonesys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Ac1Zonesys_Type.__name__ = "Integer32"
_Ac1Zonesys_Object = MibScalar
ac1Zonesys = _Ac1Zonesys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 29),
    _Ac1Zonesys_Type()
)
ac1Zonesys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ac1Zonesys.setStatus("mandatory")


class _Ac2Zonesys_Type(Integer32):
    """Custom type ac2Zonesys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Ac2Zonesys_Type.__name__ = "Integer32"
_Ac2Zonesys_Object = MibScalar
ac2Zonesys = _Ac2Zonesys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 30),
    _Ac2Zonesys_Type()
)
ac2Zonesys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ac2Zonesys.setStatus("mandatory")


class _Damper1Zonesys_Type(Integer32):
    """Custom type damper1Zonesys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Damper1Zonesys_Type.__name__ = "Integer32"
_Damper1Zonesys_Object = MibScalar
damper1Zonesys = _Damper1Zonesys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 31),
    _Damper1Zonesys_Type()
)
damper1Zonesys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    damper1Zonesys.setStatus("mandatory")


class _Damper2Zonesys_Type(Integer32):
    """Custom type damper2Zonesys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Damper2Zonesys_Type.__name__ = "Integer32"
_Damper2Zonesys_Object = MibScalar
damper2Zonesys = _Damper2Zonesys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 32),
    _Damper2Zonesys_Type()
)
damper2Zonesys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    damper2Zonesys.setStatus("mandatory")


class _HeaterZonesys_Type(Integer32):
    """Custom type heaterZonesys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_HeaterZonesys_Type.__name__ = "Integer32"
_HeaterZonesys_Object = MibScalar
heaterZonesys = _HeaterZonesys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 33),
    _HeaterZonesys_Type()
)
heaterZonesys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    heaterZonesys.setStatus("mandatory")


class _StatusLogsys_Type(Integer32):
    """Custom type statusLogsys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_StatusLogsys_Type.__name__ = "Integer32"
_StatusLogsys_Object = MibScalar
statusLogsys = _StatusLogsys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 34),
    _StatusLogsys_Type()
)
statusLogsys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statusLogsys.setStatus("mandatory")


class _Logintervalsys_Type(Integer32):
    """Custom type logintervalsys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_Logintervalsys_Type.__name__ = "Integer32"
_Logintervalsys_Object = MibScalar
logintervalsys = _Logintervalsys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 35),
    _Logintervalsys_Type()
)
logintervalsys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logintervalsys.setStatus("mandatory")


class _Alarm1NONCsys_Type(Integer32):
    """Custom type alarm1NONCsys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarm1NONCsys_Type.__name__ = "Integer32"
_Alarm1NONCsys_Object = MibScalar
alarm1NONCsys = _Alarm1NONCsys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 36),
    _Alarm1NONCsys_Type()
)
alarm1NONCsys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm1NONCsys.setStatus("mandatory")


class _Alarm2NONCsys_Type(Integer32):
    """Custom type alarm2NONCsys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarm2NONCsys_Type.__name__ = "Integer32"
_Alarm2NONCsys_Object = MibScalar
alarm2NONCsys = _Alarm2NONCsys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 37),
    _Alarm2NONCsys_Type()
)
alarm2NONCsys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm2NONCsys.setStatus("mandatory")


class _Alarm3NONCsys_Type(Integer32):
    """Custom type alarm3NONCsys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarm3NONCsys_Type.__name__ = "Integer32"
_Alarm3NONCsys_Object = MibScalar
alarm3NONCsys = _Alarm3NONCsys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 38),
    _Alarm3NONCsys_Type()
)
alarm3NONCsys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm3NONCsys.setStatus("mandatory")


class _Alarm4NONCsys_Type(Integer32):
    """Custom type alarm4NONCsys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarm4NONCsys_Type.__name__ = "Integer32"
_Alarm4NONCsys_Object = MibScalar
alarm4NONCsys = _Alarm4NONCsys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 39),
    _Alarm4NONCsys_Type()
)
alarm4NONCsys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm4NONCsys.setStatus("mandatory")


class _Alarm5NONCsys_Type(Integer32):
    """Custom type alarm5NONCsys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarm5NONCsys_Type.__name__ = "Integer32"
_Alarm5NONCsys_Object = MibScalar
alarm5NONCsys = _Alarm5NONCsys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 40),
    _Alarm5NONCsys_Type()
)
alarm5NONCsys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm5NONCsys.setStatus("mandatory")


class _Alarm6NONCsys_Type(Integer32):
    """Custom type alarm6NONCsys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarm6NONCsys_Type.__name__ = "Integer32"
_Alarm6NONCsys_Object = MibScalar
alarm6NONCsys = _Alarm6NONCsys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 41),
    _Alarm6NONCsys_Type()
)
alarm6NONCsys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm6NONCsys.setStatus("mandatory")


class _Alarm7NONCsys_Type(Integer32):
    """Custom type alarm7NONCsys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarm7NONCsys_Type.__name__ = "Integer32"
_Alarm7NONCsys_Object = MibScalar
alarm7NONCsys = _Alarm7NONCsys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 42),
    _Alarm7NONCsys_Type()
)
alarm7NONCsys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm7NONCsys.setStatus("mandatory")


class _Alarm8NONCsys_Type(Integer32):
    """Custom type alarm8NONCsys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarm8NONCsys_Type.__name__ = "Integer32"
_Alarm8NONCsys_Object = MibScalar
alarm8NONCsys = _Alarm8NONCsys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 43),
    _Alarm8NONCsys_Type()
)
alarm8NONCsys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm8NONCsys.setStatus("mandatory")


class _Alarm9NONCsys_Type(Integer32):
    """Custom type alarm9NONCsys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarm9NONCsys_Type.__name__ = "Integer32"
_Alarm9NONCsys_Object = MibScalar
alarm9NONCsys = _Alarm9NONCsys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 44),
    _Alarm9NONCsys_Type()
)
alarm9NONCsys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm9NONCsys.setStatus("mandatory")


class _Alarm10NONCsys_Type(Integer32):
    """Custom type alarm10NONCsys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarm10NONCsys_Type.__name__ = "Integer32"
_Alarm10NONCsys_Object = MibScalar
alarm10NONCsys = _Alarm10NONCsys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 45),
    _Alarm10NONCsys_Type()
)
alarm10NONCsys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm10NONCsys.setStatus("mandatory")


class _Alarm1Delaysys_Type(Integer32):
    """Custom type alarm1Delaysys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Alarm1Delaysys_Type.__name__ = "Integer32"
_Alarm1Delaysys_Object = MibScalar
alarm1Delaysys = _Alarm1Delaysys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 46),
    _Alarm1Delaysys_Type()
)
alarm1Delaysys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm1Delaysys.setStatus("mandatory")


class _Alarm2Delaysys_Type(Integer32):
    """Custom type alarm2Delaysys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Alarm2Delaysys_Type.__name__ = "Integer32"
_Alarm2Delaysys_Object = MibScalar
alarm2Delaysys = _Alarm2Delaysys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 47),
    _Alarm2Delaysys_Type()
)
alarm2Delaysys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm2Delaysys.setStatus("mandatory")


class _Alarm3Delaysys_Type(Integer32):
    """Custom type alarm3Delaysys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Alarm3Delaysys_Type.__name__ = "Integer32"
_Alarm3Delaysys_Object = MibScalar
alarm3Delaysys = _Alarm3Delaysys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 48),
    _Alarm3Delaysys_Type()
)
alarm3Delaysys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm3Delaysys.setStatus("mandatory")


class _Alarm4Delaysys_Type(Integer32):
    """Custom type alarm4Delaysys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Alarm4Delaysys_Type.__name__ = "Integer32"
_Alarm4Delaysys_Object = MibScalar
alarm4Delaysys = _Alarm4Delaysys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 49),
    _Alarm4Delaysys_Type()
)
alarm4Delaysys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm4Delaysys.setStatus("mandatory")


class _Alarm5Delaysys_Type(Integer32):
    """Custom type alarm5Delaysys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Alarm5Delaysys_Type.__name__ = "Integer32"
_Alarm5Delaysys_Object = MibScalar
alarm5Delaysys = _Alarm5Delaysys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 50),
    _Alarm5Delaysys_Type()
)
alarm5Delaysys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm5Delaysys.setStatus("mandatory")


class _Alarm6Delaysys_Type(Integer32):
    """Custom type alarm6Delaysys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Alarm6Delaysys_Type.__name__ = "Integer32"
_Alarm6Delaysys_Object = MibScalar
alarm6Delaysys = _Alarm6Delaysys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 51),
    _Alarm6Delaysys_Type()
)
alarm6Delaysys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm6Delaysys.setStatus("mandatory")


class _Alarm7Delaysys_Type(Integer32):
    """Custom type alarm7Delaysys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Alarm7Delaysys_Type.__name__ = "Integer32"
_Alarm7Delaysys_Object = MibScalar
alarm7Delaysys = _Alarm7Delaysys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 52),
    _Alarm7Delaysys_Type()
)
alarm7Delaysys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm7Delaysys.setStatus("mandatory")


class _Alarm8Delaysys_Type(Integer32):
    """Custom type alarm8Delaysys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Alarm8Delaysys_Type.__name__ = "Integer32"
_Alarm8Delaysys_Object = MibScalar
alarm8Delaysys = _Alarm8Delaysys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 53),
    _Alarm8Delaysys_Type()
)
alarm8Delaysys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm8Delaysys.setStatus("mandatory")


class _Alarm9Delaysys_Type(Integer32):
    """Custom type alarm9Delaysys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Alarm9Delaysys_Type.__name__ = "Integer32"
_Alarm9Delaysys_Object = MibScalar
alarm9Delaysys = _Alarm9Delaysys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 54),
    _Alarm9Delaysys_Type()
)
alarm9Delaysys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm9Delaysys.setStatus("mandatory")


class _Alarm10Delaysys_Type(Integer32):
    """Custom type alarm10Delaysys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Alarm10Delaysys_Type.__name__ = "Integer32"
_Alarm10Delaysys_Object = MibScalar
alarm10Delaysys = _Alarm10Delaysys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 55),
    _Alarm10Delaysys_Type()
)
alarm10Delaysys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm10Delaysys.setStatus("mandatory")


class _Ac1NONCsys_Type(Integer32):
    """Custom type ac1NONCsys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Ac1NONCsys_Type.__name__ = "Integer32"
_Ac1NONCsys_Object = MibScalar
ac1NONCsys = _Ac1NONCsys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 56),
    _Ac1NONCsys_Type()
)
ac1NONCsys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ac1NONCsys.setStatus("mandatory")


class _Ac2NONCsys_Type(Integer32):
    """Custom type ac2NONCsys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Ac2NONCsys_Type.__name__ = "Integer32"
_Ac2NONCsys_Object = MibScalar
ac2NONCsys = _Ac2NONCsys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 57),
    _Ac2NONCsys_Type()
)
ac2NONCsys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ac2NONCsys.setStatus("mandatory")


class _Dig1NONCsys_Type(Integer32):
    """Custom type dig1NONCsys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Dig1NONCsys_Type.__name__ = "Integer32"
_Dig1NONCsys_Object = MibScalar
dig1NONCsys = _Dig1NONCsys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 58),
    _Dig1NONCsys_Type()
)
dig1NONCsys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dig1NONCsys.setStatus("mandatory")


class _Dig2NONCsys_Type(Integer32):
    """Custom type dig2NONCsys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Dig2NONCsys_Type.__name__ = "Integer32"
_Dig2NONCsys_Object = MibScalar
dig2NONCsys = _Dig2NONCsys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 59),
    _Dig2NONCsys_Type()
)
dig2NONCsys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dig2NONCsys.setStatus("mandatory")


class _Dig3NONCsys_Type(Integer32):
    """Custom type dig3NONCsys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Dig3NONCsys_Type.__name__ = "Integer32"
_Dig3NONCsys_Object = MibScalar
dig3NONCsys = _Dig3NONCsys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 60),
    _Dig3NONCsys_Type()
)
dig3NONCsys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dig3NONCsys.setStatus("mandatory")


class _Dig2funcoverridesys_Type(Integer32):
    """Custom type dig2funcoverridesys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Dig2funcoverridesys_Type.__name__ = "Integer32"
_Dig2funcoverridesys_Object = MibScalar
dig2funcoverridesys = _Dig2funcoverridesys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 61),
    _Dig2funcoverridesys_Type()
)
dig2funcoverridesys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dig2funcoverridesys.setStatus("mandatory")


class _Dig3funcoverridesys_Type(Integer32):
    """Custom type dig3funcoverridesys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Dig3funcoverridesys_Type.__name__ = "Integer32"
_Dig3funcoverridesys_Object = MibScalar
dig3funcoverridesys = _Dig3funcoverridesys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 62),
    _Dig3funcoverridesys_Type()
)
dig3funcoverridesys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dig3funcoverridesys.setStatus("mandatory")


class _Dig2offsetsys_Type(Integer32):
    """Custom type dig2offsetsys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 10),
    )


_Dig2offsetsys_Type.__name__ = "Integer32"
_Dig2offsetsys_Object = MibScalar
dig2offsetsys = _Dig2offsetsys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 63),
    _Dig2offsetsys_Type()
)
dig2offsetsys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dig2offsetsys.setStatus("mandatory")


class _Dig3offsetsys_Type(Integer32):
    """Custom type dig3offsetsys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 10),
    )


_Dig3offsetsys_Type.__name__ = "Integer32"
_Dig3offsetsys_Object = MibScalar
dig3offsetsys = _Dig3offsetsys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 64),
    _Dig3offsetsys_Type()
)
dig3offsetsys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dig3offsetsys.setStatus("mandatory")


class _Dig2trigModesys_Type(Integer32):
    """Custom type dig2trigModesys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Dig2trigModesys_Type.__name__ = "Integer32"
_Dig2trigModesys_Object = MibScalar
dig2trigModesys = _Dig2trigModesys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 65),
    _Dig2trigModesys_Type()
)
dig2trigModesys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dig2trigModesys.setStatus("mandatory")


class _Dig3TrigModesys_Type(Integer32):
    """Custom type dig3TrigModesys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Dig3TrigModesys_Type.__name__ = "Integer32"
_Dig3TrigModesys_Object = MibScalar
dig3TrigModesys = _Dig3TrigModesys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 66),
    _Dig3TrigModesys_Type()
)
dig3TrigModesys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dig3TrigModesys.setStatus("mandatory")


class _FilterGuard1NONCsys_Type(Integer32):
    """Custom type filterGuard1NONCsys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FilterGuard1NONCsys_Type.__name__ = "Integer32"
_FilterGuard1NONCsys_Object = MibScalar
filterGuard1NONCsys = _FilterGuard1NONCsys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 67),
    _FilterGuard1NONCsys_Type()
)
filterGuard1NONCsys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterGuard1NONCsys.setStatus("mandatory")


class _FilterGuard2NONCsys_Type(Integer32):
    """Custom type filterGuard2NONCsys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FilterGuard2NONCsys_Type.__name__ = "Integer32"
_FilterGuard2NONCsys_Object = MibScalar
filterGuard2NONCsys = _FilterGuard2NONCsys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 68),
    _FilterGuard2NONCsys_Type()
)
filterGuard2NONCsys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterGuard2NONCsys.setStatus("mandatory")


class _TemprUnitsCFsys_Type(Integer32):
    """Custom type temprUnitsCFsys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_TemprUnitsCFsys_Type.__name__ = "Integer32"
_TemprUnitsCFsys_Object = MibScalar
temprUnitsCFsys = _TemprUnitsCFsys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 69),
    _TemprUnitsCFsys_Type()
)
temprUnitsCFsys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temprUnitsCFsys.setStatus("mandatory")


class _LanguageEnglishsys_Type(Integer32):
    """Custom type languageEnglishsys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_LanguageEnglishsys_Type.__name__ = "Integer32"
_LanguageEnglishsys_Object = MibScalar
languageEnglishsys = _LanguageEnglishsys_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 11, 70),
    _LanguageEnglishsys_Type()
)
languageEnglishsys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    languageEnglishsys.setStatus("mandatory")
_AlarmConfig_ObjectIdentity = ObjectIdentity
alarmConfig = _AlarmConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46651, 1, 12)
)


class _SaveReloadConfAlm_Type(Integer32):
    """Custom type saveReloadConfAlm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_SaveReloadConfAlm_Type.__name__ = "Integer32"
_SaveReloadConfAlm_Object = MibScalar
saveReloadConfAlm = _SaveReloadConfAlm_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 12, 1),
    _SaveReloadConfAlm_Type()
)
saveReloadConfAlm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saveReloadConfAlm.setStatus("mandatory")


class _Alarm1mask_Type(Integer32):
    """Custom type alarm1mask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 33554432),
    )


_Alarm1mask_Type.__name__ = "Integer32"
_Alarm1mask_Object = MibScalar
alarm1mask = _Alarm1mask_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 12, 2),
    _Alarm1mask_Type()
)
alarm1mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm1mask.setStatus("mandatory")


class _Alarm2mask_Type(Integer32):
    """Custom type alarm2mask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 33554432),
    )


_Alarm2mask_Type.__name__ = "Integer32"
_Alarm2mask_Object = MibScalar
alarm2mask = _Alarm2mask_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 12, 3),
    _Alarm2mask_Type()
)
alarm2mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm2mask.setStatus("mandatory")


class _Alarm3mask_Type(Integer32):
    """Custom type alarm3mask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25),
    )


_Alarm3mask_Type.__name__ = "Integer32"
_Alarm3mask_Object = MibScalar
alarm3mask = _Alarm3mask_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 12, 4),
    _Alarm3mask_Type()
)
alarm3mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm3mask.setStatus("mandatory")


class _Alarm4mask_Type(Integer32):
    """Custom type alarm4mask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25),
    )


_Alarm4mask_Type.__name__ = "Integer32"
_Alarm4mask_Object = MibScalar
alarm4mask = _Alarm4mask_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 12, 5),
    _Alarm4mask_Type()
)
alarm4mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm4mask.setStatus("mandatory")


class _Alarm5mask_Type(Integer32):
    """Custom type alarm5mask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25),
    )


_Alarm5mask_Type.__name__ = "Integer32"
_Alarm5mask_Object = MibScalar
alarm5mask = _Alarm5mask_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 12, 6),
    _Alarm5mask_Type()
)
alarm5mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm5mask.setStatus("mandatory")


class _Alarm6mask_Type(Integer32):
    """Custom type alarm6mask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25),
    )


_Alarm6mask_Type.__name__ = "Integer32"
_Alarm6mask_Object = MibScalar
alarm6mask = _Alarm6mask_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 12, 7),
    _Alarm6mask_Type()
)
alarm6mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm6mask.setStatus("mandatory")


class _Alarm7mask_Type(Integer32):
    """Custom type alarm7mask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25),
    )


_Alarm7mask_Type.__name__ = "Integer32"
_Alarm7mask_Object = MibScalar
alarm7mask = _Alarm7mask_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 12, 8),
    _Alarm7mask_Type()
)
alarm7mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm7mask.setStatus("mandatory")


class _Alarm8mask_Type(Integer32):
    """Custom type alarm8mask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25),
    )


_Alarm8mask_Type.__name__ = "Integer32"
_Alarm8mask_Object = MibScalar
alarm8mask = _Alarm8mask_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 12, 9),
    _Alarm8mask_Type()
)
alarm8mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm8mask.setStatus("mandatory")


class _Alarm9mask_Type(Integer32):
    """Custom type alarm9mask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25),
    )


_Alarm9mask_Type.__name__ = "Integer32"
_Alarm9mask_Object = MibScalar
alarm9mask = _Alarm9mask_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 12, 10),
    _Alarm9mask_Type()
)
alarm9mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm9mask.setStatus("mandatory")


class _Alarm10mask_Type(Integer32):
    """Custom type alarm10mask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25),
    )


_Alarm10mask_Type.__name__ = "Integer32"
_Alarm10mask_Object = MibScalar
alarm10mask = _Alarm10mask_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 12, 11),
    _Alarm10mask_Type()
)
alarm10mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm10mask.setStatus("mandatory")
_NightModeConfig_ObjectIdentity = ObjectIdentity
nightModeConfig = _NightModeConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46651, 1, 13)
)


class _SaveReloadConfNm_Type(Integer32):
    """Custom type saveReloadConfNm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_SaveReloadConfNm_Type.__name__ = "Integer32"
_SaveReloadConfNm_Object = MibScalar
saveReloadConfNm = _SaveReloadConfNm_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 13, 1),
    _SaveReloadConfNm_Type()
)
saveReloadConfNm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saveReloadConfNm.setStatus("mandatory")


class _StarttimeHournm_Type(Integer32):
    """Custom type starttimeHournm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_StarttimeHournm_Type.__name__ = "Integer32"
_StarttimeHournm_Object = MibScalar
starttimeHournm = _StarttimeHournm_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 13, 2),
    _StarttimeHournm_Type()
)
starttimeHournm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starttimeHournm.setStatus("mandatory")


class _StartTimeMinutesnm_Type(Integer32):
    """Custom type startTimeMinutesnm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_StartTimeMinutesnm_Type.__name__ = "Integer32"
_StartTimeMinutesnm_Object = MibScalar
startTimeMinutesnm = _StartTimeMinutesnm_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 13, 3),
    _StartTimeMinutesnm_Type()
)
startTimeMinutesnm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    startTimeMinutesnm.setStatus("mandatory")


class _EndTimeHournm_Type(Integer32):
    """Custom type endTimeHournm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_EndTimeHournm_Type.__name__ = "Integer32"
_EndTimeHournm_Object = MibScalar
endTimeHournm = _EndTimeHournm_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 13, 4),
    _EndTimeHournm_Type()
)
endTimeHournm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    endTimeHournm.setStatus("mandatory")


class _EndTimeMinutesnm_Type(Integer32):
    """Custom type endTimeMinutesnm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_EndTimeMinutesnm_Type.__name__ = "Integer32"
_EndTimeMinutesnm_Object = MibScalar
endTimeMinutesnm = _EndTimeMinutesnm_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 13, 5),
    _EndTimeMinutesnm_Type()
)
endTimeMinutesnm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    endTimeMinutesnm.setStatus("mandatory")


class _FanMaxRPMnm_Type(Integer32):
    """Custom type fanMaxRPMnm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FanMaxRPMnm_Type.__name__ = "Integer32"
_FanMaxRPMnm_Object = MibScalar
fanMaxRPMnm = _FanMaxRPMnm_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 13, 6),
    _FanMaxRPMnm_Type()
)
fanMaxRPMnm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fanMaxRPMnm.setStatus("mandatory")


class _SetPointOffsetnm_Type(Integer32):
    """Custom type setPointOffsetnm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 10),
    )


_SetPointOffsetnm_Type.__name__ = "Integer32"
_SetPointOffsetnm_Object = MibScalar
setPointOffsetnm = _SetPointOffsetnm_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 13, 7),
    _SetPointOffsetnm_Type()
)
setPointOffsetnm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPointOffsetnm.setStatus("mandatory")


class _CoolingModenm_Type(Integer32):
    """Custom type coolingModenm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_CoolingModenm_Type.__name__ = "Integer32"
_CoolingModenm_Object = MibScalar
coolingModenm = _CoolingModenm_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 13, 8),
    _CoolingModenm_Type()
)
coolingModenm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coolingModenm.setStatus("mandatory")


class _Enablenm_Type(Integer32):
    """Custom type enablenm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Enablenm_Type.__name__ = "Integer32"
_Enablenm_Object = MibScalar
enablenm = _Enablenm_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 13, 9),
    _Enablenm_Type()
)
enablenm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enablenm.setStatus("mandatory")
_NetworkConfig_ObjectIdentity = ObjectIdentity
networkConfig = _NetworkConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46651, 1, 14)
)


class _SaveReloadConfNW_Type(Integer32):
    """Custom type saveReloadConfNW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_SaveReloadConfNW_Type.__name__ = "Integer32"
_SaveReloadConfNW_Object = MibScalar
saveReloadConfNW = _SaveReloadConfNW_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 14, 1),
    _SaveReloadConfNW_Type()
)
saveReloadConfNW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saveReloadConfNW.setStatus("mandatory")


class _Dhcpenable_Type(Integer32):
    """Custom type dhcpenable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Dhcpenable_Type.__name__ = "Integer32"
_Dhcpenable_Object = MibScalar
dhcpenable = _Dhcpenable_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 14, 2),
    _Dhcpenable_Type()
)
dhcpenable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpenable.setStatus("mandatory")
_Ipaddr_Type = OctetString
_Ipaddr_Object = MibScalar
ipaddr = _Ipaddr_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 14, 3),
    _Ipaddr_Type()
)
ipaddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipaddr.setStatus("mandatory")
_Subnetmask_Type = OctetString
_Subnetmask_Object = MibScalar
subnetmask = _Subnetmask_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 14, 4),
    _Subnetmask_Type()
)
subnetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetmask.setStatus("mandatory")
_GatewayIPaddr_Type = OctetString
_GatewayIPaddr_Object = MibScalar
gatewayIPaddr = _GatewayIPaddr_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 14, 5),
    _GatewayIPaddr_Type()
)
gatewayIPaddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gatewayIPaddr.setStatus("mandatory")
_NtpIPaddr_Type = OctetString
_NtpIPaddr_Object = MibScalar
ntpIPaddr = _NtpIPaddr_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 14, 6),
    _NtpIPaddr_Type()
)
ntpIPaddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpIPaddr.setStatus("mandatory")


class _SnmpPort_Type(Integer32):
    """Custom type snmpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnmpPort_Type.__name__ = "Integer32"
_SnmpPort_Object = MibScalar
snmpPort = _SnmpPort_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 14, 7),
    _SnmpPort_Type()
)
snmpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpPort.setStatus("mandatory")
_TrapServer1IPaddr_Type = OctetString
_TrapServer1IPaddr_Object = MibScalar
trapServer1IPaddr = _TrapServer1IPaddr_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 14, 8),
    _TrapServer1IPaddr_Type()
)
trapServer1IPaddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapServer1IPaddr.setStatus("mandatory")


class _TrapServer1port_Type(Integer32):
    """Custom type trapServer1port based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TrapServer1port_Type.__name__ = "Integer32"
_TrapServer1port_Object = MibScalar
trapServer1port = _TrapServer1port_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 14, 9),
    _TrapServer1port_Type()
)
trapServer1port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapServer1port.setStatus("mandatory")
_TrapServer2IPaddr_Type = OctetString
_TrapServer2IPaddr_Object = MibScalar
trapServer2IPaddr = _TrapServer2IPaddr_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 14, 10),
    _TrapServer2IPaddr_Type()
)
trapServer2IPaddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapServer2IPaddr.setStatus("mandatory")


class _TrapServer2port_Type(Integer32):
    """Custom type trapServer2port based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TrapServer2port_Type.__name__ = "Integer32"
_TrapServer2port_Object = MibScalar
trapServer2port = _TrapServer2port_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 14, 11),
    _TrapServer2port_Type()
)
trapServer2port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapServer2port.setStatus("mandatory")
_TrapServer3IPaddr_Type = OctetString
_TrapServer3IPaddr_Object = MibScalar
trapServer3IPaddr = _TrapServer3IPaddr_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 14, 12),
    _TrapServer3IPaddr_Type()
)
trapServer3IPaddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapServer3IPaddr.setStatus("mandatory")


class _TrapServer3port_Type(Integer32):
    """Custom type trapServer3port based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TrapServer3port_Type.__name__ = "Integer32"
_TrapServer3port_Object = MibScalar
trapServer3port = _TrapServer3port_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 14, 13),
    _TrapServer3port_Type()
)
trapServer3port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapServer3port.setStatus("mandatory")
_SnmpCommunity_Type = OctetString
_SnmpCommunity_Object = MibScalar
snmpCommunity = _SnmpCommunity_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 14, 14),
    _SnmpCommunity_Type()
)
snmpCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpCommunity.setStatus("mandatory")
_HostName_Type = OctetString
_HostName_Object = MibScalar
hostName = _HostName_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 14, 15),
    _HostName_Type()
)
hostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostName.setStatus("mandatory")
_TrapError_ObjectIdentity = ObjectIdentity
trapError = _TrapError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46651, 1, 15)
)


class _ErrorNumber_Type(Integer32):
    """Custom type errorNumber based on Integer32"""
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
        *(("VoltageLow", 1),
          ("VoltageHigh", 2),
          ("TemprLow", 3),
          ("TemprLimit1", 4),
          ("TemprLimit2", 5),
          ("TemprLimit3", 6),
          ("HumidLow", 7),
          ("HumidHigh", 8),
          ("FltrPressure1", 9),
          ("FltPressure2", 10),
          ("Fan1", 11),
          ("Fan2", 12),
          ("OnboardSens", 13),
          ("RoomSens", 14),
          ("HotspotSens", 15),
          ("Ambient1Sens", 16),
          ("Ambient2Sens", 17),
          ("Dig1IP", 18),
          ("Dig2IP", 19),
          ("Dig3IP", 20),
          ("FilterIP1", 21),
          ("FilterIP2", 22),
          ("Network", 23),
          ("Intstorage", 24),
          ("SDCard", 25))
    )


_ErrorNumber_Type.__name__ = "Integer32"
_ErrorNumber_Object = MibScalar
errorNumber = _ErrorNumber_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 15, 1),
    _ErrorNumber_Type()
)
errorNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    errorNumber.setStatus("mandatory")


class _Status_Type(Integer32):
    """Custom type status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ALARMclear", 0),
          ("ALARMset", 1))
    )


_Status_Type.__name__ = "Integer32"
_Status_Object = MibScalar
status = _Status_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 15, 2),
    _Status_Type()
)
status.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    status.setStatus("mandatory")
_Value_Type = OctetString
_Value_Object = MibScalar
value = _Value_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 15, 3),
    _Value_Type()
)
value.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    value.setStatus("mandatory")
_Info_Type = OctetString
_Info_Object = MibScalar
info = _Info_Object(
    (1, 3, 6, 1, 4, 1, 46651, 1, 15, 4),
    _Info_Type()
)
info.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    info.setStatus("mandatory")

# Managed Objects groups


# Notification objects

cc3000Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 46651, 0, 1)
)
cc3000Trap.setObjects(
      *(("DANTHERM-COOLING-MIB", "hostName"),
        ("DANTHERM-COOLING-MIB", "errorNumber"),
        ("DANTHERM-COOLING-MIB", "status"),
        ("DANTHERM-COOLING-MIB", "value"),
        ("DANTHERM-COOLING-MIB", "info"))
)
if mibBuilder.loadTexts:
    cc3000Trap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DANTHERM-COOLING-MIB",
    **{"danthermCooling": danthermCooling,
       "cc3000Trap": cc3000Trap,
       "controllerCC3000": controllerCC3000,
       "systemStatus": systemStatus,
       "onBoardTempr": onBoardTempr,
       "roomTempr": roomTempr,
       "hotSpotTempr": hotSpotTempr,
       "outdoor1Tempr": outdoor1Tempr,
       "outdoor2Tempr": outdoor2Tempr,
       "shelterTempr": shelterTempr,
       "outdoorCombinedTempr": outdoorCombinedTempr,
       "fan1RPM": fan1RPM,
       "fan2RPM": fan2RPM,
       "fan1SpeedPercentage": fan1SpeedPercentage,
       "fan2SpeedPercentage": fan2SpeedPercentage,
       "damper1Position": damper1Position,
       "damper2Position": damper2Position,
       "humidity": humidity,
       "dewpoint": dewpoint,
       "atmosphericPressure": atmosphericPressure,
       "flowPressure": flowPressure,
       "fan1Status": fan1Status,
       "fan2Status": fan2Status,
       "damper1Status": damper1Status,
       "damper2Status": damper2Status,
       "aircond1Status": aircond1Status,
       "aircond2Status": aircond2Status,
       "heaterStatus": heaterStatus,
       "shelter1Status": shelter1Status,
       "shelter2Status": shelter2Status,
       "shelter1Mode": shelter1Mode,
       "shelter2Mode": shelter2Mode,
       "shelter1Setpoint": shelter1Setpoint,
       "shelter2Setpoint": shelter2Setpoint,
       "errorStatus": errorStatus,
       "maskedErrorStatus": maskedErrorStatus,
       "voltage": voltage,
       "digitalInputStatus": digitalInputStatus,
       "alarmDriveStatus": alarmDriveStatus,
       "fan1OpertdurHour": fan1OpertdurHour,
       "fan1OpertdurMin": fan1OpertdurMin,
       "fan2OpertdurHour": fan2OpertdurHour,
       "fan2OpertdurMin": fan2OpertdurMin,
       "aircon1OpertdurHour": aircon1OpertdurHour,
       "aircon1OpertdurMin": aircon1OpertdurMin,
       "aircon2OpertdurHour": aircon2OpertdurHour,
       "aircon2OpertdurMin": aircon2OpertdurMin,
       "heaterOpertdurHour": heaterOpertdurHour,
       "heaterOpertdurMin": heaterOpertdurMin,
       "ccSN": ccSN,
       "fanbox1SN": fanbox1SN,
       "fanbox2SN": fanbox2SN,
       "aircond1SN": aircond1SN,
       "aircond2SN": aircond2SN,
       "fwVersion": fwVersion,
       "highlevelControl": highlevelControl,
       "coolSetpointZone1": coolSetpointZone1,
       "coolSetpointZone2": coolSetpointZone2,
       "heaterSetpoint": heaterSetpoint,
       "backupConfig": backupConfig,
       "restoreConfig": restoreConfig,
       "systemReset": systemReset,
       "year": year,
       "month": month,
       "date": date,
       "hour": hour,
       "minute": minute,
       "fan1Config": fan1Config,
       "saveReloadConff1": saveReloadConff1,
       "offTemprf1": offTemprf1,
       "idleOnTemprf1": idleOnTemprf1,
       "idleEntryTemprf1": idleEntryTemprf1,
       "midPoint1Temprf1": midPoint1Temprf1,
       "setPointTemprf1": setPointTemprf1,
       "midPoint2Temprf1": midPoint2Temprf1,
       "highSpeedTemprf1": highSpeedTemprf1,
       "extendHighSpeedEntryTemprf1": extendHighSpeedEntryTemprf1,
       "extendHighSpeedExitTemprf1": extendHighSpeedExitTemprf1,
       "boostEntryTemprf1": boostEntryTemprf1,
       "boostExitTemprf1": boostExitTemprf1,
       "idleRPMf1": idleRPMf1,
       "midPointRPMf1": midPointRPMf1,
       "highSpeedRPMf1": highSpeedRPMf1,
       "extendHighSpeedRPMf1": extendHighSpeedRPMf1,
       "idleDutyCyclef1": idleDutyCyclef1,
       "midDutyCyclef1": midDutyCyclef1,
       "highSpeedDutyCyclef1": highSpeedDutyCyclef1,
       "extendHighSpeedDutyCyclef1": extendHighSpeedDutyCyclef1,
       "boostDutyCyclef1": boostDutyCyclef1,
       "deadBandRPMf1": deadBandRPMf1,
       "overrideDigi1f1": overrideDigi1f1,
       "overrideDigi2f1": overrideDigi2f1,
       "overrideDigi3f1": overrideDigi3f1,
       "overrideSensorfailf1": overrideSensorfailf1,
       "sensorSelectf1": sensorSelectf1,
       "tachoPulseperrotationf1": tachoPulseperrotationf1,
       "closedLoopenablef1": closedLoopenablef1,
       "controlTypef1": controlTypef1,
       "enablef1": enablef1,
       "fan2Config": fan2Config,
       "saveReloadConff2": saveReloadConff2,
       "offTemprf2": offTemprf2,
       "idleOnTemprf2": idleOnTemprf2,
       "idleEntryTemprf2": idleEntryTemprf2,
       "midPoint1Temprf2": midPoint1Temprf2,
       "setPointTemprf2": setPointTemprf2,
       "midPoint2Temprf2": midPoint2Temprf2,
       "highSpeedTemprf2": highSpeedTemprf2,
       "extendHighSpeedEntryTemprf2": extendHighSpeedEntryTemprf2,
       "extendHighSpeedExitTemprf2": extendHighSpeedExitTemprf2,
       "boostEntryTemprf2": boostEntryTemprf2,
       "boostExitTemprf2": boostExitTemprf2,
       "idleRPMf2": idleRPMf2,
       "midPointRPMf2": midPointRPMf2,
       "highSpeedRPMf2": highSpeedRPMf2,
       "extendHighSpeedRPMf2": extendHighSpeedRPMf2,
       "idleDutyCyclef2": idleDutyCyclef2,
       "midDutyCyclef2": midDutyCyclef2,
       "highSpeedDutyCyclef2": highSpeedDutyCyclef2,
       "extendHighSpeedDutyCyclef2": extendHighSpeedDutyCyclef2,
       "boostDutyCyclef2": boostDutyCyclef2,
       "deadBandRPMf2": deadBandRPMf2,
       "overrideDigi1f2": overrideDigi1f2,
       "overrideDigi2f2": overrideDigi2f2,
       "overrideDigi3f2": overrideDigi3f2,
       "overrideSensorfailf2": overrideSensorfailf2,
       "sensorSelectf2": sensorSelectf2,
       "tachoPulseperrotationf2": tachoPulseperrotationf2,
       "closedLoopenablef2": closedLoopenablef2,
       "controlTypef2": controlTypef2,
       "enablef2": enablef2,
       "damper1Config": damper1Config,
       "saveReloadConfd1": saveReloadConfd1,
       "lowercloseTemprd1": lowercloseTemprd1,
       "setPointd1": setPointd1,
       "upperOpentempd1": upperOpentempd1,
       "upperClosetempd1": upperClosetempd1,
       "emgncyClosetempd1": emgncyClosetempd1,
       "emgncyopentempd1": emgncyopentempd1,
       "overrideDigi1d1": overrideDigi1d1,
       "overrideDigi2d1": overrideDigi2d1,
       "overrideDigi3d1": overrideDigi3d1,
       "overrideSensorFaild1": overrideSensorFaild1,
       "sensSelectd1": sensSelectd1,
       "runDurationd1": runDurationd1,
       "enabled1": enabled1,
       "damper2Config": damper2Config,
       "saveReloadConfd2": saveReloadConfd2,
       "lowercloseTemprd2": lowercloseTemprd2,
       "setPointd2": setPointd2,
       "upperOpentempd2": upperOpentempd2,
       "upperClosetempd2": upperClosetempd2,
       "emgncyClosetempd2": emgncyClosetempd2,
       "emgncyopentempd2": emgncyopentempd2,
       "overrideDigi1d2": overrideDigi1d2,
       "overrideDigi2d2": overrideDigi2d2,
       "overrideDigi3d2": overrideDigi3d2,
       "overrideSensorFaild2": overrideSensorFaild2,
       "sensSelectd2": sensSelectd2,
       "runDurationd2": runDurationd2,
       "enabled2": enabled2,
       "aircon1Config": aircon1Config,
       "saveReloadConfac1": saveReloadConfac1,
       "oNTemprac1": oNTemprac1,
       "oFFTemprac1": oFFTemprac1,
       "overrideDigi1ac1": overrideDigi1ac1,
       "overrideDigi2ac1": overrideDigi2ac1,
       "overrideDigi3ac1": overrideDigi3ac1,
       "overrideSensorFailac1": overrideSensorFailac1,
       "sensSelectac1": sensSelectac1,
       "minimumRunDurationac1": minimumRunDurationac1,
       "restartTimeoutac1": restartTimeoutac1,
       "enableac1": enableac1,
       "aircon2Config": aircon2Config,
       "saveReloadConfac2": saveReloadConfac2,
       "onTemprac2": onTemprac2,
       "offTemprac2": offTemprac2,
       "overrideDigi1ac2": overrideDigi1ac2,
       "overrideDigi2ac2": overrideDigi2ac2,
       "overrideDigi3ac2": overrideDigi3ac2,
       "overrideSensorFailac2": overrideSensorFailac2,
       "sensSelectac2": sensSelectac2,
       "minimumRunDurationac2": minimumRunDurationac2,
       "restartTimeoutac2": restartTimeoutac2,
       "enableac2": enableac2,
       "heaterConfig": heaterConfig,
       "saveReloadConfhtr": saveReloadConfhtr,
       "onTemprhtr": onTemprhtr,
       "offTemprhtr": offTemprhtr,
       "overrideDigi1htr": overrideDigi1htr,
       "overrideDigi2htr": overrideDigi2htr,
       "overrideDigi3htr": overrideDigi3htr,
       "overrideSensorFailhtr": overrideSensorFailhtr,
       "sensSelecthtr": sensSelecthtr,
       "enablehtr": enablehtr,
       "humidityConfig": humidityConfig,
       "saveReloadConfhum": saveReloadConfhum,
       "rhEntryhum": rhEntryhum,
       "rhExithum": rhExithum,
       "coolingmodehum": coolingmodehum,
       "temprsetpoffsethum": temprsetpoffsethum,
       "rhSensPositionhum": rhSensPositionhum,
       "enablehum": enablehum,
       "systemConfig": systemConfig,
       "saveReloadConfsysc": saveReloadConfsysc,
       "vdcLowEntrysys": vdcLowEntrysys,
       "vdcLowExitsys": vdcLowExitsys,
       "vdcHighEntrysys": vdcHighEntrysys,
       "vdcHighExitsys": vdcHighExitsys,
       "temprLowlimitsys": temprLowlimitsys,
       "temprHighlimit1sys": temprHighlimit1sys,
       "temprHighlimit2sys": temprHighlimit2sys,
       "temprHighlimit3sys": temprHighlimit3sys,
       "temprlimithyssys": temprlimithyssys,
       "rhLowlimitsys": rhLowlimitsys,
       "rhHighlimitsys": rhHighlimitsys,
       "flowpresslimit1sys": flowpresslimit1sys,
       "flowpresslimit2sys": flowpresslimit2sys,
       "flowpresshyssys": flowpresshyssys,
       "coolingzonessys": coolingzonessys,
       "coolingModesys": coolingModesys,
       "negCoolingDeltaOverridesys": negCoolingDeltaOverridesys,
       "negCoolingDeltaHyssys": negCoolingDeltaHyssys,
       "coolingDeltatempsys": coolingDeltatempsys,
       "shelterTemprsys": shelterTemprsys,
       "acleadlagsys": acleadlagsys,
       "coolingModeXzonesys": coolingModeXzonesys,
       "negCoolingDeltaOverrideXzonesys": negCoolingDeltaOverrideXzonesys,
       "negCoolingDeltaHysXzonesys": negCoolingDeltaHysXzonesys,
       "coolingDeltatempXzonesys": coolingDeltatempXzonesys,
       "fan1Zonesys": fan1Zonesys,
       "fan2Zonesys": fan2Zonesys,
       "ac1Zonesys": ac1Zonesys,
       "ac2Zonesys": ac2Zonesys,
       "damper1Zonesys": damper1Zonesys,
       "damper2Zonesys": damper2Zonesys,
       "heaterZonesys": heaterZonesys,
       "statusLogsys": statusLogsys,
       "logintervalsys": logintervalsys,
       "alarm1NONCsys": alarm1NONCsys,
       "alarm2NONCsys": alarm2NONCsys,
       "alarm3NONCsys": alarm3NONCsys,
       "alarm4NONCsys": alarm4NONCsys,
       "alarm5NONCsys": alarm5NONCsys,
       "alarm6NONCsys": alarm6NONCsys,
       "alarm7NONCsys": alarm7NONCsys,
       "alarm8NONCsys": alarm8NONCsys,
       "alarm9NONCsys": alarm9NONCsys,
       "alarm10NONCsys": alarm10NONCsys,
       "alarm1Delaysys": alarm1Delaysys,
       "alarm2Delaysys": alarm2Delaysys,
       "alarm3Delaysys": alarm3Delaysys,
       "alarm4Delaysys": alarm4Delaysys,
       "alarm5Delaysys": alarm5Delaysys,
       "alarm6Delaysys": alarm6Delaysys,
       "alarm7Delaysys": alarm7Delaysys,
       "alarm8Delaysys": alarm8Delaysys,
       "alarm9Delaysys": alarm9Delaysys,
       "alarm10Delaysys": alarm10Delaysys,
       "ac1NONCsys": ac1NONCsys,
       "ac2NONCsys": ac2NONCsys,
       "dig1NONCsys": dig1NONCsys,
       "dig2NONCsys": dig2NONCsys,
       "dig3NONCsys": dig3NONCsys,
       "dig2funcoverridesys": dig2funcoverridesys,
       "dig3funcoverridesys": dig3funcoverridesys,
       "dig2offsetsys": dig2offsetsys,
       "dig3offsetsys": dig3offsetsys,
       "dig2trigModesys": dig2trigModesys,
       "dig3TrigModesys": dig3TrigModesys,
       "filterGuard1NONCsys": filterGuard1NONCsys,
       "filterGuard2NONCsys": filterGuard2NONCsys,
       "temprUnitsCFsys": temprUnitsCFsys,
       "languageEnglishsys": languageEnglishsys,
       "alarmConfig": alarmConfig,
       "saveReloadConfAlm": saveReloadConfAlm,
       "alarm1mask": alarm1mask,
       "alarm2mask": alarm2mask,
       "alarm3mask": alarm3mask,
       "alarm4mask": alarm4mask,
       "alarm5mask": alarm5mask,
       "alarm6mask": alarm6mask,
       "alarm7mask": alarm7mask,
       "alarm8mask": alarm8mask,
       "alarm9mask": alarm9mask,
       "alarm10mask": alarm10mask,
       "nightModeConfig": nightModeConfig,
       "saveReloadConfNm": saveReloadConfNm,
       "starttimeHournm": starttimeHournm,
       "startTimeMinutesnm": startTimeMinutesnm,
       "endTimeHournm": endTimeHournm,
       "endTimeMinutesnm": endTimeMinutesnm,
       "fanMaxRPMnm": fanMaxRPMnm,
       "setPointOffsetnm": setPointOffsetnm,
       "coolingModenm": coolingModenm,
       "enablenm": enablenm,
       "networkConfig": networkConfig,
       "saveReloadConfNW": saveReloadConfNW,
       "dhcpenable": dhcpenable,
       "ipaddr": ipaddr,
       "subnetmask": subnetmask,
       "gatewayIPaddr": gatewayIPaddr,
       "ntpIPaddr": ntpIPaddr,
       "snmpPort": snmpPort,
       "trapServer1IPaddr": trapServer1IPaddr,
       "trapServer1port": trapServer1port,
       "trapServer2IPaddr": trapServer2IPaddr,
       "trapServer2port": trapServer2port,
       "trapServer3IPaddr": trapServer3IPaddr,
       "trapServer3port": trapServer3port,
       "snmpCommunity": snmpCommunity,
       "hostName": hostName,
       "trapError": trapError,
       "errorNumber": errorNumber,
       "status": status,
       "value": value,
       "info": info}
)
