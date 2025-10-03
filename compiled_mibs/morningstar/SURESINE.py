# SNMP MIB module (SURESINE) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\morningstar\SURESINE
# Produced by pysmi-1.6.2 at Thu Oct  2 12:10:55 2025
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

suresine = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 33333, 9)
)
if mibBuilder.loadTexts:
    suresine.setRevisions(
        ("2019-12-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



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
          ("loadOn", 1),
          ("lvdWarning", 2),
          ("lowVoltageDisconnect", 3),
          ("fault", 4),
          ("disconnect", 5),
          ("loadOff", 6),
          ("unknownState", 7),
          ("standby", 8))
    )



class AlarmsBitfield(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("heatsinkTempSensorOpen", 0),
          ("heatsinkTempSensorShort", 1),
          ("unknownAlarm", 2),
          ("suresineHot", 3))
    )


class FaultsBitfield(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("reset", 0),
          ("overcurrent", 1),
          ("unknownFault", 2),
          ("software", 3),
          ("highVoltageDisconnect", 4),
          ("suresineHot", 5),
          ("dipSwitchChanged", 6),
          ("customSettingsEdit", 7))
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
    (1, 3, 6, 1, 4, 1, 33333, 9, 1),
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
    (1, 3, 6, 1, 4, 1, 33333, 9, 2),
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
    (1, 3, 6, 1, 4, 1, 33333, 9, 3),
    _DeviceVersion_Type()
)
deviceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceVersion.setStatus("current")
_BatteryVoltageSlow_Type = Unsigned32
_BatteryVoltageSlow_Object = MibScalar
batteryVoltageSlow = _BatteryVoltageSlow_Object(
    (1, 3, 6, 1, 4, 1, 33333, 9, 30),
    _BatteryVoltageSlow_Type()
)
batteryVoltageSlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryVoltageSlow.setStatus("current")
_AcCurrent_Type = Unsigned32
_AcCurrent_Object = MibScalar
acCurrent = _AcCurrent_Object(
    (1, 3, 6, 1, 4, 1, 33333, 9, 31),
    _AcCurrent_Type()
)
acCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acCurrent.setStatus("current")
_HeatsinkTemperature_Type = Integer32
_HeatsinkTemperature_Object = MibScalar
heatsinkTemperature = _HeatsinkTemperature_Object(
    (1, 3, 6, 1, 4, 1, 33333, 9, 32),
    _HeatsinkTemperature_Type()
)
heatsinkTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heatsinkTemperature.setStatus("current")
_LoadState_Type = LoadStateEnum
_LoadState_Object = MibScalar
loadState = _LoadState_Object(
    (1, 3, 6, 1, 4, 1, 33333, 9, 33),
    _LoadState_Type()
)
loadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadState.setStatus("current")
_Alarms_Type = AlarmsBitfield
_Alarms_Object = MibScalar
alarms = _Alarms_Object(
    (1, 3, 6, 1, 4, 1, 33333, 9, 34),
    _Alarms_Type()
)
alarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarms.setStatus("current")
_Faults_Type = FaultsBitfield
_Faults_Object = MibScalar
faults = _Faults_Object(
    (1, 3, 6, 1, 4, 1, 33333, 9, 35),
    _Faults_Type()
)
faults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faults.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SURESINE",
    **{"LoadStateEnum": LoadStateEnum,
       "AlarmsBitfield": AlarmsBitfield,
       "FaultsBitfield": FaultsBitfield,
       "suresine": suresine,
       "subModel": subModel,
       "serialNumber": serialNumber,
       "deviceVersion": deviceVersion,
       "batteryVoltageSlow": batteryVoltageSlow,
       "acCurrent": acCurrent,
       "heatsinkTemperature": heatsinkTemperature,
       "loadState": loadState,
       "alarms": alarms,
       "faults": faults}
)
