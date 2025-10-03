# SNMP MIB module (ICT-PLATINUM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ict\ICT-PLATINUM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:01:24 2025
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
_PlatinumSeries_ObjectIdentity = ObjectIdentity
platinumSeries = _PlatinumSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39145, 11)
)
_DeviceModel_Type = DisplayString
_DeviceModel_Object = MibScalar
deviceModel = _DeviceModel_Object(
    (1, 3, 6, 1, 4, 1, 39145, 11, 1),
    _DeviceModel_Type()
)
deviceModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceModel.setStatus("mandatory")
_DeviceName_Type = DisplayString
_DeviceName_Object = MibScalar
deviceName = _DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 39145, 11, 2),
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
    (1, 3, 6, 1, 4, 1, 39145, 11, 3),
    _DeviceHardware_Type()
)
deviceHardware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceHardware.setStatus("mandatory")
_DeviceFirmware_Type = DisplayString
_DeviceFirmware_Object = MibScalar
deviceFirmware = _DeviceFirmware_Object(
    (1, 3, 6, 1, 4, 1, 39145, 11, 4),
    _DeviceFirmware_Type()
)
deviceFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceFirmware.setStatus("mandatory")
_DeviceMacAddress_Type = DisplayString
_DeviceMacAddress_Object = MibScalar
deviceMacAddress = _DeviceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 39145, 11, 5),
    _DeviceMacAddress_Type()
)
deviceMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceMacAddress.setStatus("mandatory")
_InputVoltage_Type = DisplayString
_InputVoltage_Object = MibScalar
inputVoltage = _InputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 39145, 11, 6),
    _InputVoltage_Type()
)
inputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputVoltage.setStatus("mandatory")
_OutputVoltage_Type = DisplayString
_OutputVoltage_Object = MibScalar
outputVoltage = _OutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 39145, 11, 7),
    _OutputVoltage_Type()
)
outputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputVoltage.setStatus("mandatory")
_OutputCurrent_Type = DisplayString
_OutputCurrent_Object = MibScalar
outputCurrent = _OutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 39145, 11, 8),
    _OutputCurrent_Type()
)
outputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputCurrent.setStatus("mandatory")


class _OutputEnable_Type(Integer32):
    """Custom type outputEnable based on Integer32"""
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


_OutputEnable_Type.__name__ = "Integer32"
_OutputEnable_Object = MibScalar
outputEnable = _OutputEnable_Object(
    (1, 3, 6, 1, 4, 1, 39145, 11, 9),
    _OutputEnable_Type()
)
outputEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputEnable.setStatus("mandatory")
_BatteryVoltage_Type = DisplayString
_BatteryVoltage_Object = MibScalar
batteryVoltage = _BatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 39145, 11, 10),
    _BatteryVoltage_Type()
)
batteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryVoltage.setStatus("mandatory")
_BatteryCurrent_Type = DisplayString
_BatteryCurrent_Object = MibScalar
batteryCurrent = _BatteryCurrent_Object(
    (1, 3, 6, 1, 4, 1, 39145, 11, 11),
    _BatteryCurrent_Type()
)
batteryCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryCurrent.setStatus("mandatory")
_BatteryTemperature_Type = Integer32
_BatteryTemperature_Object = MibScalar
batteryTemperature = _BatteryTemperature_Object(
    (1, 3, 6, 1, 4, 1, 39145, 11, 12),
    _BatteryTemperature_Type()
)
batteryTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTemperature.setStatus("mandatory")


class _BatterySoc_Type(Integer32):
    """Custom type batterySoc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BatterySoc_Type.__name__ = "Integer32"
_BatterySoc_Object = MibScalar
batterySoc = _BatterySoc_Object(
    (1, 3, 6, 1, 4, 1, 39145, 11, 13),
    _BatterySoc_Type()
)
batterySoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batterySoc.setStatus("mandatory")
_BatteryNetAh_Type = Integer32
_BatteryNetAh_Object = MibScalar
batteryNetAh = _BatteryNetAh_Object(
    (1, 3, 6, 1, 4, 1, 39145, 11, 14),
    _BatteryNetAh_Type()
)
batteryNetAh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryNetAh.setStatus("mandatory")
_BatteryRunTime_Type = Integer32
_BatteryRunTime_Object = MibScalar
batteryRunTime = _BatteryRunTime_Object(
    (1, 3, 6, 1, 4, 1, 39145, 11, 15),
    _BatteryRunTime_Type()
)
batteryRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryRunTime.setStatus("mandatory")
_InputVoltageX1_Type = Integer32
_InputVoltageX1_Object = MibScalar
inputVoltageX1 = _InputVoltageX1_Object(
    (1, 3, 6, 1, 4, 1, 39145, 11, 16),
    _InputVoltageX1_Type()
)
inputVoltageX1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputVoltageX1.setStatus("mandatory")
_OutputVoltageX100_Type = Integer32
_OutputVoltageX100_Object = MibScalar
outputVoltageX100 = _OutputVoltageX100_Object(
    (1, 3, 6, 1, 4, 1, 39145, 11, 17),
    _OutputVoltageX100_Type()
)
outputVoltageX100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputVoltageX100.setStatus("mandatory")
_OutputCurrentX100_Type = Integer32
_OutputCurrentX100_Object = MibScalar
outputCurrentX100 = _OutputCurrentX100_Object(
    (1, 3, 6, 1, 4, 1, 39145, 11, 18),
    _OutputCurrentX100_Type()
)
outputCurrentX100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputCurrentX100.setStatus("mandatory")
_BatteryVoltageX100_Type = Integer32
_BatteryVoltageX100_Object = MibScalar
batteryVoltageX100 = _BatteryVoltageX100_Object(
    (1, 3, 6, 1, 4, 1, 39145, 11, 19),
    _BatteryVoltageX100_Type()
)
batteryVoltageX100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryVoltageX100.setStatus("mandatory")
_BatteryCurrentX100_Type = Integer32
_BatteryCurrentX100_Object = MibScalar
batteryCurrentX100 = _BatteryCurrentX100_Object(
    (1, 3, 6, 1, 4, 1, 39145, 11, 20),
    _BatteryCurrentX100_Type()
)
batteryCurrentX100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryCurrentX100.setStatus("mandatory")


class _BatteryTestResult_Type(Integer32):
    """Custom type batteryTestResult based on Integer32"""
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
          ("inProgress", 2),
          ("pass", 3),
          ("fail", 4))
    )


_BatteryTestResult_Type.__name__ = "Integer32"
_BatteryTestResult_Object = MibScalar
batteryTestResult = _BatteryTestResult_Object(
    (1, 3, 6, 1, 4, 1, 39145, 11, 21),
    _BatteryTestResult_Type()
)
batteryTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTestResult.setStatus("mandatory")

# Managed Objects groups


# Notification objects

acFailAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 11, 0, 101)
)
if mibBuilder.loadTexts:
    acFailAlarmTrap.setStatus(
        ""
    )

dcFailAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 11, 0, 102)
)
if mibBuilder.loadTexts:
    dcFailAlarmTrap.setStatus(
        ""
    )

sysFailAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 11, 0, 103)
)
if mibBuilder.loadTexts:
    sysFailAlarmTrap.setStatus(
        ""
    )

overtemperatureAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 11, 0, 104)
)
if mibBuilder.loadTexts:
    overtemperatureAlarmTrap.setStatus(
        ""
    )

commFailAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 11, 0, 105)
)
if mibBuilder.loadTexts:
    commFailAlarmTrap.setStatus(
        ""
    )

fanFailAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 11, 0, 106)
)
if mibBuilder.loadTexts:
    fanFailAlarmTrap.setStatus(
        ""
    )

batteryAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 11, 0, 107)
)
if mibBuilder.loadTexts:
    batteryAlarmTrap.setStatus(
        ""
    )

acFailAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 11, 0, 111)
)
if mibBuilder.loadTexts:
    acFailAlarmClear.setStatus(
        ""
    )

dcFailAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 11, 0, 112)
)
if mibBuilder.loadTexts:
    dcFailAlarmClear.setStatus(
        ""
    )

sysFailAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 11, 0, 113)
)
if mibBuilder.loadTexts:
    sysFailAlarmClear.setStatus(
        ""
    )

overtemperatureAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 11, 0, 114)
)
if mibBuilder.loadTexts:
    overtemperatureAlarmClear.setStatus(
        ""
    )

commFailAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 11, 0, 115)
)
if mibBuilder.loadTexts:
    commFailAlarmClear.setStatus(
        ""
    )

fanFailAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 11, 0, 116)
)
if mibBuilder.loadTexts:
    fanFailAlarmClear.setStatus(
        ""
    )

batteryAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 11, 0, 117)
)
if mibBuilder.loadTexts:
    batteryAlarmClear.setStatus(
        ""
    )

batteryTestStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 11, 0, 121)
)
if mibBuilder.loadTexts:
    batteryTestStart.setStatus(
        ""
    )

batteryTestComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 11, 0, 122)
)
if mibBuilder.loadTexts:
    batteryTestComplete.setStatus(
        ""
    )

batteryTestFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 11, 0, 123)
)
if mibBuilder.loadTexts:
    batteryTestFail.setStatus(
        ""
    )

batteryEqualizeStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 11, 0, 124)
)
if mibBuilder.loadTexts:
    batteryEqualizeStart.setStatus(
        ""
    )

batteryEqualizeComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 11, 0, 125)
)
if mibBuilder.loadTexts:
    batteryEqualizeComplete.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ICT-PLATINUM-MIB",
    **{"ictPower": ictPower,
       "platinumSeries": platinumSeries,
       "acFailAlarmTrap": acFailAlarmTrap,
       "dcFailAlarmTrap": dcFailAlarmTrap,
       "sysFailAlarmTrap": sysFailAlarmTrap,
       "overtemperatureAlarmTrap": overtemperatureAlarmTrap,
       "commFailAlarmTrap": commFailAlarmTrap,
       "fanFailAlarmTrap": fanFailAlarmTrap,
       "batteryAlarmTrap": batteryAlarmTrap,
       "acFailAlarmClear": acFailAlarmClear,
       "dcFailAlarmClear": dcFailAlarmClear,
       "sysFailAlarmClear": sysFailAlarmClear,
       "overtemperatureAlarmClear": overtemperatureAlarmClear,
       "commFailAlarmClear": commFailAlarmClear,
       "fanFailAlarmClear": fanFailAlarmClear,
       "batteryAlarmClear": batteryAlarmClear,
       "batteryTestStart": batteryTestStart,
       "batteryTestComplete": batteryTestComplete,
       "batteryTestFail": batteryTestFail,
       "batteryEqualizeStart": batteryEqualizeStart,
       "batteryEqualizeComplete": batteryEqualizeComplete,
       "deviceModel": deviceModel,
       "deviceName": deviceName,
       "deviceHardware": deviceHardware,
       "deviceFirmware": deviceFirmware,
       "deviceMacAddress": deviceMacAddress,
       "inputVoltage": inputVoltage,
       "outputVoltage": outputVoltage,
       "outputCurrent": outputCurrent,
       "outputEnable": outputEnable,
       "batteryVoltage": batteryVoltage,
       "batteryCurrent": batteryCurrent,
       "batteryTemperature": batteryTemperature,
       "batterySoc": batterySoc,
       "batteryNetAh": batteryNetAh,
       "batteryRunTime": batteryRunTime,
       "inputVoltageX1": inputVoltageX1,
       "outputVoltageX100": outputVoltageX100,
       "outputCurrentX100": outputCurrentX100,
       "batteryVoltageX100": batteryVoltageX100,
       "batteryCurrentX100": batteryCurrentX100,
       "batteryTestResult": batteryTestResult}
)
