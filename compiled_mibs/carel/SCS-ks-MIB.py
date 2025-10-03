# SNMP MIB module (SCS-ks-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\carel\SCS-ks-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:23:45 2025
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

(ifEntry,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifEntry",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysContact,
 sysLocation,
 sysName) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysContact",
    "sysLocation",
    "sysName")

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

scs_ks = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 1, 1)
)
if mibBuilder.loadTexts:
    scs_ks.setRevisions(
        ("2020-11-05 18:05",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Carel_ObjectIdentity = ObjectIdentity
carel = _Carel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839)
)
_Systm_ObjectIdentity = ObjectIdentity
systm = _Systm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 1)
)
_Scs_ObjectIdentity = ObjectIdentity
scs = _Scs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 1, 2)
)


class _Status_evaporator_fan_Type(Integer32):
    """Custom type status_evaporator_fan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Status_evaporator_fan_Type.__name__ = "Integer32"
_Status_evaporator_fan_Object = MibScalar
status_evaporator_fan = _Status_evaporator_fan_Object(
    (1, 3, 6, 1, 4, 1, 9839, 1, 2, 1),
    _Status_evaporator_fan_Type()
)
status_evaporator_fan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_evaporator_fan.setStatus("current")
if mibBuilder.loadTexts:
    status_evaporator_fan.setUnits("N/A")


class _Status_condenser_fan_Type(Integer32):
    """Custom type status_condenser_fan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Status_condenser_fan_Type.__name__ = "Integer32"
_Status_condenser_fan_Object = MibScalar
status_condenser_fan = _Status_condenser_fan_Object(
    (1, 3, 6, 1, 4, 1, 9839, 1, 2, 2),
    _Status_condenser_fan_Type()
)
status_condenser_fan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_condenser_fan.setStatus("current")
if mibBuilder.loadTexts:
    status_condenser_fan.setUnits("N/A")


class _Status_compressor_Type(Integer32):
    """Custom type status_compressor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Status_compressor_Type.__name__ = "Integer32"
_Status_compressor_Object = MibScalar
status_compressor = _Status_compressor_Object(
    (1, 3, 6, 1, 4, 1, 9839, 1, 2, 3),
    _Status_compressor_Type()
)
status_compressor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_compressor.setStatus("current")
if mibBuilder.loadTexts:
    status_compressor.setUnits("N/A")


class _Status_heater_thermal_protection_Type(Integer32):
    """Custom type status_heater_thermal_protection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Status_heater_thermal_protection_Type.__name__ = "Integer32"
_Status_heater_thermal_protection_Object = MibScalar
status_heater_thermal_protection = _Status_heater_thermal_protection_Object(
    (1, 3, 6, 1, 4, 1, 9839, 1, 2, 4),
    _Status_heater_thermal_protection_Type()
)
status_heater_thermal_protection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_heater_thermal_protection.setStatus("current")
if mibBuilder.loadTexts:
    status_heater_thermal_protection.setUnits("N/A")


class _Status_exhaust_air_sensor_Type(Integer32):
    """Custom type status_exhaust_air_sensor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Status_exhaust_air_sensor_Type.__name__ = "Integer32"
_Status_exhaust_air_sensor_Object = MibScalar
status_exhaust_air_sensor = _Status_exhaust_air_sensor_Object(
    (1, 3, 6, 1, 4, 1, 9839, 1, 2, 5),
    _Status_exhaust_air_sensor_Type()
)
status_exhaust_air_sensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_exhaust_air_sensor.setStatus("current")
if mibBuilder.loadTexts:
    status_exhaust_air_sensor.setUnits("N/A")


class _Status_supply_air_sensor_Type(Integer32):
    """Custom type status_supply_air_sensor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Status_supply_air_sensor_Type.__name__ = "Integer32"
_Status_supply_air_sensor_Object = MibScalar
status_supply_air_sensor = _Status_supply_air_sensor_Object(
    (1, 3, 6, 1, 4, 1, 9839, 1, 2, 6),
    _Status_supply_air_sensor_Type()
)
status_supply_air_sensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_supply_air_sensor.setStatus("current")
if mibBuilder.loadTexts:
    status_supply_air_sensor.setUnits("N/A")


class _Status_outside_sensor_Type(Integer32):
    """Custom type status_outside_sensor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Status_outside_sensor_Type.__name__ = "Integer32"
_Status_outside_sensor_Object = MibScalar
status_outside_sensor = _Status_outside_sensor_Object(
    (1, 3, 6, 1, 4, 1, 9839, 1, 2, 7),
    _Status_outside_sensor_Type()
)
status_outside_sensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_outside_sensor.setStatus("current")
if mibBuilder.loadTexts:
    status_outside_sensor.setUnits("N/A")


class _Status_room_temperature_sensor_Type(Integer32):
    """Custom type status_room_temperature_sensor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Status_room_temperature_sensor_Type.__name__ = "Integer32"
_Status_room_temperature_sensor_Object = MibScalar
status_room_temperature_sensor = _Status_room_temperature_sensor_Object(
    (1, 3, 6, 1, 4, 1, 9839, 1, 2, 8),
    _Status_room_temperature_sensor_Type()
)
status_room_temperature_sensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_room_temperature_sensor.setStatus("current")
if mibBuilder.loadTexts:
    status_room_temperature_sensor.setUnits("N/A")


class _Status_room_humidity_sensor_Type(Integer32):
    """Custom type status_room_humidity_sensor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Status_room_humidity_sensor_Type.__name__ = "Integer32"
_Status_room_humidity_sensor_Object = MibScalar
status_room_humidity_sensor = _Status_room_humidity_sensor_Object(
    (1, 3, 6, 1, 4, 1, 9839, 1, 2, 9),
    _Status_room_humidity_sensor_Type()
)
status_room_humidity_sensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_room_humidity_sensor.setStatus("current")
if mibBuilder.loadTexts:
    status_room_humidity_sensor.setUnits("N/A")


class _Status_min_exhaust_air_temperature_Type(Integer32):
    """Custom type status_min_exhaust_air_temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Status_min_exhaust_air_temperature_Type.__name__ = "Integer32"
_Status_min_exhaust_air_temperature_Object = MibScalar
status_min_exhaust_air_temperature = _Status_min_exhaust_air_temperature_Object(
    (1, 3, 6, 1, 4, 1, 9839, 1, 2, 10),
    _Status_min_exhaust_air_temperature_Type()
)
status_min_exhaust_air_temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_min_exhaust_air_temperature.setStatus("current")
if mibBuilder.loadTexts:
    status_min_exhaust_air_temperature.setUnits("N/A")


class _Status_max_exhaust_air_temperature_Type(Integer32):
    """Custom type status_max_exhaust_air_temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Status_max_exhaust_air_temperature_Type.__name__ = "Integer32"
_Status_max_exhaust_air_temperature_Object = MibScalar
status_max_exhaust_air_temperature = _Status_max_exhaust_air_temperature_Object(
    (1, 3, 6, 1, 4, 1, 9839, 1, 2, 11),
    _Status_max_exhaust_air_temperature_Type()
)
status_max_exhaust_air_temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_max_exhaust_air_temperature.setStatus("current")
if mibBuilder.loadTexts:
    status_max_exhaust_air_temperature.setUnits("N/A")


class _Status_min_supply_air_temperature_Type(Integer32):
    """Custom type status_min_supply_air_temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Status_min_supply_air_temperature_Type.__name__ = "Integer32"
_Status_min_supply_air_temperature_Object = MibScalar
status_min_supply_air_temperature = _Status_min_supply_air_temperature_Object(
    (1, 3, 6, 1, 4, 1, 9839, 1, 2, 12),
    _Status_min_supply_air_temperature_Type()
)
status_min_supply_air_temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_min_supply_air_temperature.setStatus("current")
if mibBuilder.loadTexts:
    status_min_supply_air_temperature.setUnits("N/A")


class _Status_water_sensor_Type(Integer32):
    """Custom type status_water_sensor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Status_water_sensor_Type.__name__ = "Integer32"
_Status_water_sensor_Object = MibScalar
status_water_sensor = _Status_water_sensor_Object(
    (1, 3, 6, 1, 4, 1, 9839, 1, 2, 13),
    _Status_water_sensor_Type()
)
status_water_sensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_water_sensor.setStatus("current")
if mibBuilder.loadTexts:
    status_water_sensor.setUnits("N/A")


class _Status_filter_monitoring_Type(Integer32):
    """Custom type status_filter_monitoring based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Status_filter_monitoring_Type.__name__ = "Integer32"
_Status_filter_monitoring_Object = MibScalar
status_filter_monitoring = _Status_filter_monitoring_Object(
    (1, 3, 6, 1, 4, 1, 9839, 1, 2, 14),
    _Status_filter_monitoring_Type()
)
status_filter_monitoring.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_filter_monitoring.setStatus("current")
if mibBuilder.loadTexts:
    status_filter_monitoring.setUnits("N/A")


class _Exhaust_air_temperature_Type(Integer32):
    """Custom type exhaust_air_temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Exhaust_air_temperature_Type.__name__ = "Integer32"
_Exhaust_air_temperature_Object = MibScalar
exhaust_air_temperature = _Exhaust_air_temperature_Object(
    (1, 3, 6, 1, 4, 1, 9839, 1, 2, 15),
    _Exhaust_air_temperature_Type()
)
exhaust_air_temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exhaust_air_temperature.setStatus("current")
if mibBuilder.loadTexts:
    exhaust_air_temperature.setUnits("N/A")


class _Supply_air_temperature_Type(Integer32):
    """Custom type supply_air_temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Supply_air_temperature_Type.__name__ = "Integer32"
_Supply_air_temperature_Object = MibScalar
supply_air_temperature = _Supply_air_temperature_Object(
    (1, 3, 6, 1, 4, 1, 9839, 1, 2, 16),
    _Supply_air_temperature_Type()
)
supply_air_temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supply_air_temperature.setStatus("current")
if mibBuilder.loadTexts:
    supply_air_temperature.setUnits("N/A")


class _Outside_air_temperature_Type(Integer32):
    """Custom type outside_air_temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Outside_air_temperature_Type.__name__ = "Integer32"
_Outside_air_temperature_Object = MibScalar
outside_air_temperature = _Outside_air_temperature_Object(
    (1, 3, 6, 1, 4, 1, 9839, 1, 2, 17),
    _Outside_air_temperature_Type()
)
outside_air_temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outside_air_temperature.setStatus("current")
if mibBuilder.loadTexts:
    outside_air_temperature.setUnits("N/A")


class _Room_temperature_Type(Integer32):
    """Custom type room_temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Room_temperature_Type.__name__ = "Integer32"
_Room_temperature_Object = MibScalar
room_temperature = _Room_temperature_Object(
    (1, 3, 6, 1, 4, 1, 9839, 1, 2, 18),
    _Room_temperature_Type()
)
room_temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    room_temperature.setStatus("current")
if mibBuilder.loadTexts:
    room_temperature.setUnits("N/A")


class _Room_humidity_Type(Integer32):
    """Custom type room_humidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Room_humidity_Type.__name__ = "Integer32"
_Room_humidity_Object = MibScalar
room_humidity = _Room_humidity_Object(
    (1, 3, 6, 1, 4, 1, 9839, 1, 2, 19),
    _Room_humidity_Type()
)
room_humidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    room_humidity.setStatus("current")
if mibBuilder.loadTexts:
    room_humidity.setUnits("N/A")


class _Status_operational_status_Type(Integer32):
    """Custom type status_operational_status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Status_operational_status_Type.__name__ = "Integer32"
_Status_operational_status_Object = MibScalar
status_operational_status = _Status_operational_status_Object(
    (1, 3, 6, 1, 4, 1, 9839, 1, 2, 20),
    _Status_operational_status_Type()
)
status_operational_status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_operational_status.setStatus("current")
if mibBuilder.loadTexts:
    status_operational_status.setUnits("N/A")


class _Status_collective_fault_Type(Integer32):
    """Custom type status_collective_fault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Status_collective_fault_Type.__name__ = "Integer32"
_Status_collective_fault_Object = MibScalar
status_collective_fault = _Status_collective_fault_Object(
    (1, 3, 6, 1, 4, 1, 9839, 1, 2, 21),
    _Status_collective_fault_Type()
)
status_collective_fault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_collective_fault.setStatus("current")
if mibBuilder.loadTexts:
    status_collective_fault.setUnits("N/A")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SCS-ks-MIB",
    **{"carel": carel,
       "systm": systm,
       "scs-ks": scs_ks,
       "scs": scs,
       "status-evaporator-fan": status_evaporator_fan,
       "status-condenser-fan": status_condenser_fan,
       "status-compressor": status_compressor,
       "status-heater-thermal-protection": status_heater_thermal_protection,
       "status-exhaust-air-sensor": status_exhaust_air_sensor,
       "status-supply-air-sensor": status_supply_air_sensor,
       "status-outside-sensor": status_outside_sensor,
       "status-room-temperature-sensor": status_room_temperature_sensor,
       "status-room-humidity-sensor": status_room_humidity_sensor,
       "status-min-exhaust-air-temperature": status_min_exhaust_air_temperature,
       "status-max-exhaust-air-temperature": status_max_exhaust_air_temperature,
       "status-min-supply-air-temperature": status_min_supply_air_temperature,
       "status-water-sensor": status_water_sensor,
       "status-filter-monitoring": status_filter_monitoring,
       "exhaust-air-temperature": exhaust_air_temperature,
       "supply-air-temperature": supply_air_temperature,
       "outside-air-temperature": outside_air_temperature,
       "room-temperature": room_temperature,
       "room-humidity": room_humidity,
       "status-operational-status": status_operational_status,
       "status-collective-fault": status_collective_fault}
)
