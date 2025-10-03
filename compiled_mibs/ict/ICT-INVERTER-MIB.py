# SNMP MIB module (ICT-INVERTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ict\ICT-INVERTER-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:01:22 2025
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

_IctPower_ObjectIdentity = ObjectIdentity
ictPower = _IctPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39145)
)
_Inverter_ObjectIdentity = ObjectIdentity
inverter = _Inverter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39145, 12)
)
_DeviceModel_Type = DisplayString
_DeviceModel_Object = MibScalar
deviceModel = _DeviceModel_Object(
    (1, 3, 6, 1, 4, 1, 39145, 12, 1),
    _DeviceModel_Type()
)
deviceModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceModel.setStatus("mandatory")
_DeviceName_Type = DisplayString
_DeviceName_Object = MibScalar
deviceName = _DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 39145, 12, 2),
    _DeviceName_Type()
)
deviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceName.setStatus("mandatory")


class _DeviceHardware_Type(Integer32):
    """Custom type deviceHardware based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_DeviceHardware_Type.__name__ = "Integer32"
_DeviceHardware_Object = MibScalar
deviceHardware = _DeviceHardware_Object(
    (1, 3, 6, 1, 4, 1, 39145, 12, 3),
    _DeviceHardware_Type()
)
deviceHardware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceHardware.setStatus("mandatory")
_DeviceFirmware_Type = DisplayString
_DeviceFirmware_Object = MibScalar
deviceFirmware = _DeviceFirmware_Object(
    (1, 3, 6, 1, 4, 1, 39145, 12, 4),
    _DeviceFirmware_Type()
)
deviceFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceFirmware.setStatus("mandatory")
_DeviceMacAddress_Type = DisplayString
_DeviceMacAddress_Object = MibScalar
deviceMacAddress = _DeviceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 39145, 12, 5),
    _DeviceMacAddress_Type()
)
deviceMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceMacAddress.setStatus("mandatory")
_BatteryVoltage_Type = DisplayString
_BatteryVoltage_Object = MibScalar
batteryVoltage = _BatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 39145, 12, 6),
    _BatteryVoltage_Type()
)
batteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryVoltage.setStatus("mandatory")
_InverterVoltage_Type = DisplayString
_InverterVoltage_Object = MibScalar
inverterVoltage = _InverterVoltage_Object(
    (1, 3, 6, 1, 4, 1, 39145, 12, 7),
    _InverterVoltage_Type()
)
inverterVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inverterVoltage.setStatus("mandatory")
_InverterPower_Type = DisplayString
_InverterPower_Object = MibScalar
inverterPower = _InverterPower_Object(
    (1, 3, 6, 1, 4, 1, 39145, 12, 8),
    _InverterPower_Type()
)
inverterPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inverterPower.setStatus("mandatory")


class _InverterStatus_Type(Integer32):
    """Custom type inverterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_InverterStatus_Type.__name__ = "Integer32"
_InverterStatus_Object = MibScalar
inverterStatus = _InverterStatus_Object(
    (1, 3, 6, 1, 4, 1, 39145, 12, 9),
    _InverterStatus_Type()
)
inverterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inverterStatus.setStatus("mandatory")


class _InverterControl_Type(Integer32):
    """Custom type inverterControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_InverterControl_Type.__name__ = "Integer32"
_InverterControl_Object = MibScalar
inverterControl = _InverterControl_Object(
    (1, 3, 6, 1, 4, 1, 39145, 12, 10),
    _InverterControl_Type()
)
inverterControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inverterControl.setStatus("mandatory")


class _TransferRelayStatus_Type(Integer32):
    """Custom type transferRelayStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inverter", 1),
          ("grid", 2))
    )


_TransferRelayStatus_Type.__name__ = "Integer32"
_TransferRelayStatus_Object = MibScalar
transferRelayStatus = _TransferRelayStatus_Object(
    (1, 3, 6, 1, 4, 1, 39145, 12, 11),
    _TransferRelayStatus_Type()
)
transferRelayStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transferRelayStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects

undervoltageAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 12, 0, 101)
)
if mibBuilder.loadTexts:
    undervoltageAlarmTrap.setStatus(
        ""
    )

overvoltageAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 12, 0, 102)
)
if mibBuilder.loadTexts:
    overvoltageAlarmTrap.setStatus(
        ""
    )

overtemperatureAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 12, 0, 103)
)
if mibBuilder.loadTexts:
    overtemperatureAlarmTrap.setStatus(
        ""
    )

outputFaultAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 12, 0, 104)
)
if mibBuilder.loadTexts:
    outputFaultAlarmTrap.setStatus(
        ""
    )

systemFaultAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 12, 0, 105)
)
if mibBuilder.loadTexts:
    systemFaultAlarmTrap.setStatus(
        ""
    )

remoteSwitchAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 12, 0, 106)
)
if mibBuilder.loadTexts:
    remoteSwitchAlarmTrap.setStatus(
        ""
    )

undervoltageAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 12, 0, 111)
)
if mibBuilder.loadTexts:
    undervoltageAlarmClear.setStatus(
        ""
    )

overvoltageAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 12, 0, 112)
)
if mibBuilder.loadTexts:
    overvoltageAlarmClear.setStatus(
        ""
    )

overtemperatureAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 12, 0, 113)
)
if mibBuilder.loadTexts:
    overtemperatureAlarmClear.setStatus(
        ""
    )

outputFaultAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 12, 0, 114)
)
if mibBuilder.loadTexts:
    outputFaultAlarmClear.setStatus(
        ""
    )

systemFaultAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 12, 0, 115)
)
if mibBuilder.loadTexts:
    systemFaultAlarmClear.setStatus(
        ""
    )

remoteSwitchAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 12, 0, 116)
)
if mibBuilder.loadTexts:
    remoteSwitchAlarmClear.setStatus(
        ""
    )

inverterPowerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 12, 0, 121)
)
if mibBuilder.loadTexts:
    inverterPowerTrap.setStatus(
        ""
    )

gridPowerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 12, 0, 122)
)
if mibBuilder.loadTexts:
    gridPowerTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ICT-INVERTER-MIB",
    **{"ictPower": ictPower,
       "inverter": inverter,
       "undervoltageAlarmTrap": undervoltageAlarmTrap,
       "overvoltageAlarmTrap": overvoltageAlarmTrap,
       "overtemperatureAlarmTrap": overtemperatureAlarmTrap,
       "outputFaultAlarmTrap": outputFaultAlarmTrap,
       "systemFaultAlarmTrap": systemFaultAlarmTrap,
       "remoteSwitchAlarmTrap": remoteSwitchAlarmTrap,
       "undervoltageAlarmClear": undervoltageAlarmClear,
       "overvoltageAlarmClear": overvoltageAlarmClear,
       "overtemperatureAlarmClear": overtemperatureAlarmClear,
       "outputFaultAlarmClear": outputFaultAlarmClear,
       "systemFaultAlarmClear": systemFaultAlarmClear,
       "remoteSwitchAlarmClear": remoteSwitchAlarmClear,
       "inverterPowerTrap": inverterPowerTrap,
       "gridPowerTrap": gridPowerTrap,
       "deviceModel": deviceModel,
       "deviceName": deviceName,
       "deviceHardware": deviceHardware,
       "deviceFirmware": deviceFirmware,
       "deviceMacAddress": deviceMacAddress,
       "batteryVoltage": batteryVoltage,
       "inverterVoltage": inverterVoltage,
       "inverterPower": inverterPower,
       "inverterStatus": inverterStatus,
       "inverterControl": inverterControl,
       "transferRelayStatus": transferRelayStatus}
)
