# SNMP MIB module (CONTROLBOX-TH332-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\controlbox\CONTROLBOX-TH332-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:33:30 2025
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

th332 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 2)
)
if mibBuilder.loadTexts:
    th332.setRevisions(
        ("2015-03-23 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Controlbox_ObjectIdentity = ObjectIdentity
controlbox = _Controlbox_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095)
)
_TrapNotifications_ObjectIdentity = ObjectIdentity
trapNotifications = _TrapNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 2, 0)
)
_Control_ObjectIdentity = ObjectIdentity
control = _Control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 2, 1)
)
_DeviceID_Type = Integer32
_DeviceID_Object = MibScalar
deviceID = _DeviceID_Object(
    (1, 3, 6, 1, 4, 1, 17095, 2, 1, 1),
    _DeviceID_Type()
)
deviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceID.setStatus("current")
_DeviceName_Type = DisplayString
_DeviceName_Object = MibScalar
deviceName = _DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 17095, 2, 1, 2),
    _DeviceName_Type()
)
deviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceName.setStatus("current")
_Temperature_Type = DisplayString
_Temperature_Object = MibScalar
temperature = _Temperature_Object(
    (1, 3, 6, 1, 4, 1, 17095, 2, 1, 3),
    _Temperature_Type()
)
temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature.setStatus("current")
_Humidity_Type = DisplayString
_Humidity_Object = MibScalar
humidity = _Humidity_Object(
    (1, 3, 6, 1, 4, 1, 17095, 2, 1, 4),
    _Humidity_Type()
)
humidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity.setStatus("current")
_Dewpoint_Type = DisplayString
_Dewpoint_Object = MibScalar
dewpoint = _Dewpoint_Object(
    (1, 3, 6, 1, 4, 1, 17095, 2, 1, 5),
    _Dewpoint_Type()
)
dewpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint.setStatus("current")


class _TemperatureState_Type(Integer32):
    """Custom type temperatureState based on Integer32"""
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
        *(("normal", 0),
          ("alert", 1),
          ("warning", 2),
          ("critical", 3))
    )


_TemperatureState_Type.__name__ = "Integer32"
_TemperatureState_Object = MibScalar
temperatureState = _TemperatureState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 2, 1, 6),
    _TemperatureState_Type()
)
temperatureState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureState.setStatus("current")


class _HumidityState_Type(Integer32):
    """Custom type humidityState based on Integer32"""
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
        *(("normal", 0),
          ("alert", 1),
          ("warning", 2),
          ("critical", 3))
    )


_HumidityState_Type.__name__ = "Integer32"
_HumidityState_Object = MibScalar
humidityState = _HumidityState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 2, 1, 7),
    _HumidityState_Type()
)
humidityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidityState.setStatus("current")


class _DewpointState_Type(Integer32):
    """Custom type dewpointState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("alert", 1))
    )


_DewpointState_Type.__name__ = "Integer32"
_DewpointState_Object = MibScalar
dewpointState = _DewpointState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 2, 1, 8),
    _DewpointState_Type()
)
dewpointState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpointState.setStatus("current")

# Managed Objects groups


# Notification objects

temperatureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17095, 2, 0, 1)
)
temperatureTrap.setObjects(
      *(("CONTROLBOX-TH332-MIB", "deviceName"),
        ("CONTROLBOX-TH332-MIB", "temperature"),
        ("CONTROLBOX-TH332-MIB", "temperatureState"))
)
if mibBuilder.loadTexts:
    temperatureTrap.setStatus(
        "current"
    )

humidityTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17095, 2, 0, 2)
)
humidityTrap.setObjects(
      *(("CONTROLBOX-TH332-MIB", "deviceName"),
        ("CONTROLBOX-TH332-MIB", "humidity"),
        ("CONTROLBOX-TH332-MIB", "humidityState"))
)
if mibBuilder.loadTexts:
    humidityTrap.setStatus(
        "current"
    )

dewpointTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17095, 2, 0, 3)
)
dewpointTrap.setObjects(
      *(("CONTROLBOX-TH332-MIB", "deviceName"),
        ("CONTROLBOX-TH332-MIB", "dewpoint"),
        ("CONTROLBOX-TH332-MIB", "dewpointState"))
)
if mibBuilder.loadTexts:
    dewpointTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CONTROLBOX-TH332-MIB",
    **{"controlbox": controlbox,
       "th332": th332,
       "trapNotifications": trapNotifications,
       "temperatureTrap": temperatureTrap,
       "humidityTrap": humidityTrap,
       "dewpointTrap": dewpointTrap,
       "control": control,
       "deviceID": deviceID,
       "deviceName": deviceName,
       "temperature": temperature,
       "humidity": humidity,
       "dewpoint": dewpoint,
       "temperatureState": temperatureState,
       "humidityState": humidityState,
       "dewpointState": dewpointState}
)
