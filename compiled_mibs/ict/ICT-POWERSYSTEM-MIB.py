# SNMP MIB module (ICT-POWERSYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ict\ICT-POWERSYSTEM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:01:25 2025
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
_PowerSystem_ObjectIdentity = ObjectIdentity
powerSystem = _PowerSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39145, 13)
)
_DeviceModel_Type = DisplayString
_DeviceModel_Object = MibScalar
deviceModel = _DeviceModel_Object(
    (1, 3, 6, 1, 4, 1, 39145, 13, 1),
    _DeviceModel_Type()
)
deviceModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceModel.setStatus("mandatory")
_DeviceName_Type = DisplayString
_DeviceName_Object = MibScalar
deviceName = _DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 39145, 13, 2),
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
    (1, 3, 6, 1, 4, 1, 39145, 13, 3),
    _DeviceHardware_Type()
)
deviceHardware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceHardware.setStatus("mandatory")
_DeviceFirmware_Type = DisplayString
_DeviceFirmware_Object = MibScalar
deviceFirmware = _DeviceFirmware_Object(
    (1, 3, 6, 1, 4, 1, 39145, 13, 4),
    _DeviceFirmware_Type()
)
deviceFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceFirmware.setStatus("mandatory")
_DeviceMacAddress_Type = DisplayString
_DeviceMacAddress_Object = MibScalar
deviceMacAddress = _DeviceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 39145, 13, 5),
    _DeviceMacAddress_Type()
)
deviceMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceMacAddress.setStatus("mandatory")
_InputVoltage_Type = DisplayString
_InputVoltage_Object = MibScalar
inputVoltage = _InputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 39145, 13, 6),
    _InputVoltage_Type()
)
inputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputVoltage.setStatus("mandatory")
_OutputVoltage_Type = DisplayString
_OutputVoltage_Object = MibScalar
outputVoltage = _OutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 39145, 13, 7),
    _OutputVoltage_Type()
)
outputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputVoltage.setStatus("mandatory")
_OutputCurrent_Type = DisplayString
_OutputCurrent_Object = MibScalar
outputCurrent = _OutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 39145, 13, 8),
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
    (1, 3, 6, 1, 4, 1, 39145, 13, 9),
    _OutputEnable_Type()
)
outputEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputEnable.setStatus("mandatory")
_ModuleTable_Object = MibTable
moduleTable = _ModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 39145, 13, 10)
)
if mibBuilder.loadTexts:
    moduleTable.setStatus("mandatory")
_ModuleEntry_Object = MibTableRow
moduleEntry = _ModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 39145, 13, 10, 1)
)
moduleEntry.setIndexNames(
    (0, "ICT-POWERSYSTEM-MIB", "moduleNumber"),
)
if mibBuilder.loadTexts:
    moduleEntry.setStatus("mandatory")


class _ModuleNumber_Type(Integer32):
    """Custom type moduleNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ModuleNumber_Type.__name__ = "Integer32"
_ModuleNumber_Object = MibTableColumn
moduleNumber = _ModuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 39145, 13, 10, 1, 1),
    _ModuleNumber_Type()
)
moduleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleNumber.setStatus("mandatory")


class _ModuleStatus_Type(Integer32):
    """Custom type moduleStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notInstalled", 1),
          ("ok", 2),
          ("alarm", 3))
    )


_ModuleStatus_Type.__name__ = "Integer32"
_ModuleStatus_Object = MibTableColumn
moduleStatus = _ModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 39145, 13, 10, 1, 2),
    _ModuleStatus_Type()
)
moduleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleStatus.setStatus("mandatory")


class _ModuleType_Type(Integer32):
    """Custom type moduleType based on Integer32"""
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
        *(("notInstalled", 1),
          ("power", 2),
          ("battery", 3),
          ("distribution", 4),
          ("converter", 5))
    )


_ModuleType_Type.__name__ = "Integer32"
_ModuleType_Object = MibTableColumn
moduleType = _ModuleType_Object(
    (1, 3, 6, 1, 4, 1, 39145, 13, 10, 1, 3),
    _ModuleType_Type()
)
moduleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleType.setStatus("mandatory")
_ModuleVoltage_Type = DisplayString
_ModuleVoltage_Object = MibTableColumn
moduleVoltage = _ModuleVoltage_Object(
    (1, 3, 6, 1, 4, 1, 39145, 13, 10, 1, 4),
    _ModuleVoltage_Type()
)
moduleVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleVoltage.setStatus("mandatory")
_ModuleCurrentA_Type = DisplayString
_ModuleCurrentA_Object = MibTableColumn
moduleCurrentA = _ModuleCurrentA_Object(
    (1, 3, 6, 1, 4, 1, 39145, 13, 10, 1, 5),
    _ModuleCurrentA_Type()
)
moduleCurrentA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCurrentA.setStatus("mandatory")
_ModuleCurrentB_Type = DisplayString
_ModuleCurrentB_Object = MibTableColumn
moduleCurrentB = _ModuleCurrentB_Object(
    (1, 3, 6, 1, 4, 1, 39145, 13, 10, 1, 6),
    _ModuleCurrentB_Type()
)
moduleCurrentB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCurrentB.setStatus("mandatory")
_ModuleCurrentC_Type = DisplayString
_ModuleCurrentC_Object = MibTableColumn
moduleCurrentC = _ModuleCurrentC_Object(
    (1, 3, 6, 1, 4, 1, 39145, 13, 10, 1, 7),
    _ModuleCurrentC_Type()
)
moduleCurrentC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCurrentC.setStatus("mandatory")
_ModuleCurrentD_Type = DisplayString
_ModuleCurrentD_Object = MibTableColumn
moduleCurrentD = _ModuleCurrentD_Object(
    (1, 3, 6, 1, 4, 1, 39145, 13, 10, 1, 8),
    _ModuleCurrentD_Type()
)
moduleCurrentD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCurrentD.setStatus("mandatory")


class _ModuleControlA_Type(Integer32):
    """Custom type moduleControlA based on Integer32"""
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


_ModuleControlA_Type.__name__ = "Integer32"
_ModuleControlA_Object = MibTableColumn
moduleControlA = _ModuleControlA_Object(
    (1, 3, 6, 1, 4, 1, 39145, 13, 10, 1, 9),
    _ModuleControlA_Type()
)
moduleControlA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleControlA.setStatus("mandatory")


class _ModuleControlB_Type(Integer32):
    """Custom type moduleControlB based on Integer32"""
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


_ModuleControlB_Type.__name__ = "Integer32"
_ModuleControlB_Object = MibTableColumn
moduleControlB = _ModuleControlB_Object(
    (1, 3, 6, 1, 4, 1, 39145, 13, 10, 1, 10),
    _ModuleControlB_Type()
)
moduleControlB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleControlB.setStatus("mandatory")


class _ModuleControlC_Type(Integer32):
    """Custom type moduleControlC based on Integer32"""
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


_ModuleControlC_Type.__name__ = "Integer32"
_ModuleControlC_Object = MibTableColumn
moduleControlC = _ModuleControlC_Object(
    (1, 3, 6, 1, 4, 1, 39145, 13, 10, 1, 11),
    _ModuleControlC_Type()
)
moduleControlC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleControlC.setStatus("mandatory")


class _ModuleControlD_Type(Integer32):
    """Custom type moduleControlD based on Integer32"""
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


_ModuleControlD_Type.__name__ = "Integer32"
_ModuleControlD_Object = MibTableColumn
moduleControlD = _ModuleControlD_Object(
    (1, 3, 6, 1, 4, 1, 39145, 13, 10, 1, 12),
    _ModuleControlD_Type()
)
moduleControlD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleControlD.setStatus("mandatory")
_ModuleVoltageX100_Type = Integer32
_ModuleVoltageX100_Object = MibTableColumn
moduleVoltageX100 = _ModuleVoltageX100_Object(
    (1, 3, 6, 1, 4, 1, 39145, 13, 10, 1, 13),
    _ModuleVoltageX100_Type()
)
moduleVoltageX100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleVoltageX100.setStatus("mandatory")
_ModuleCurrentAX100_Type = Integer32
_ModuleCurrentAX100_Object = MibTableColumn
moduleCurrentAX100 = _ModuleCurrentAX100_Object(
    (1, 3, 6, 1, 4, 1, 39145, 13, 10, 1, 14),
    _ModuleCurrentAX100_Type()
)
moduleCurrentAX100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCurrentAX100.setStatus("mandatory")
_ModuleCurrentBX100_Type = Integer32
_ModuleCurrentBX100_Object = MibTableColumn
moduleCurrentBX100 = _ModuleCurrentBX100_Object(
    (1, 3, 6, 1, 4, 1, 39145, 13, 10, 1, 15),
    _ModuleCurrentBX100_Type()
)
moduleCurrentBX100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCurrentBX100.setStatus("mandatory")
_ModuleCurrentCX100_Type = Integer32
_ModuleCurrentCX100_Object = MibTableColumn
moduleCurrentCX100 = _ModuleCurrentCX100_Object(
    (1, 3, 6, 1, 4, 1, 39145, 13, 10, 1, 16),
    _ModuleCurrentCX100_Type()
)
moduleCurrentCX100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCurrentCX100.setStatus("mandatory")
_ModuleCurrentDX100_Type = Integer32
_ModuleCurrentDX100_Object = MibTableColumn
moduleCurrentDX100 = _ModuleCurrentDX100_Object(
    (1, 3, 6, 1, 4, 1, 39145, 13, 10, 1, 17),
    _ModuleCurrentDX100_Type()
)
moduleCurrentDX100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCurrentDX100.setStatus("mandatory")
_ModuleAlarms_Type = Integer32
_ModuleAlarms_Object = MibTableColumn
moduleAlarms = _ModuleAlarms_Object(
    (1, 3, 6, 1, 4, 1, 39145, 13, 10, 1, 18),
    _ModuleAlarms_Type()
)
moduleAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleAlarms.setStatus("mandatory")
_AlarmTable_Object = MibTable
alarmTable = _AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 39145, 13, 11)
)
if mibBuilder.loadTexts:
    alarmTable.setStatus("mandatory")
_AlarmEntry_Object = MibTableRow
alarmEntry = _AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 39145, 13, 11, 1)
)
alarmEntry.setIndexNames(
    (0, "ICT-POWERSYSTEM-MIB", "alarmNumber"),
)
if mibBuilder.loadTexts:
    alarmEntry.setStatus("mandatory")


class _AlarmNumber_Type(Integer32):
    """Custom type alarmNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AlarmNumber_Type.__name__ = "Integer32"
_AlarmNumber_Object = MibTableColumn
alarmNumber = _AlarmNumber_Object(
    (1, 3, 6, 1, 4, 1, 39145, 13, 11, 1, 1),
    _AlarmNumber_Type()
)
alarmNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmNumber.setStatus("mandatory")
_AlarmName_Type = DisplayString
_AlarmName_Object = MibTableColumn
alarmName = _AlarmName_Object(
    (1, 3, 6, 1, 4, 1, 39145, 13, 11, 1, 2),
    _AlarmName_Type()
)
alarmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmName.setStatus("mandatory")


class _AlarmStatus_Type(Integer32):
    """Custom type alarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("ready", 2),
          ("alarm", 3))
    )


_AlarmStatus_Type.__name__ = "Integer32"
_AlarmStatus_Object = MibTableColumn
alarmStatus = _AlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 39145, 13, 11, 1, 3),
    _AlarmStatus_Type()
)
alarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmStatus.setStatus("mandatory")
_ProbeTemperature_Type = Integer32
_ProbeTemperature_Object = MibScalar
probeTemperature = _ProbeTemperature_Object(
    (1, 3, 6, 1, 4, 1, 39145, 13, 12),
    _ProbeTemperature_Type()
)
probeTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probeTemperature.setStatus("mandatory")


class _BatterySoc_Type(Integer32):
    """Custom type batterySoc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BatterySoc_Type.__name__ = "Integer32"
_BatterySoc_Object = MibScalar
batterySoc = _BatterySoc_Object(
    (1, 3, 6, 1, 4, 1, 39145, 13, 13),
    _BatterySoc_Type()
)
batterySoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batterySoc.setStatus("mandatory")
_BatteryNetAh_Type = Integer32
_BatteryNetAh_Object = MibScalar
batteryNetAh = _BatteryNetAh_Object(
    (1, 3, 6, 1, 4, 1, 39145, 13, 14),
    _BatteryNetAh_Type()
)
batteryNetAh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryNetAh.setStatus("mandatory")
_BatteryRunTime_Type = Integer32
_BatteryRunTime_Object = MibScalar
batteryRunTime = _BatteryRunTime_Object(
    (1, 3, 6, 1, 4, 1, 39145, 13, 15),
    _BatteryRunTime_Type()
)
batteryRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryRunTime.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 39145, 13, 16),
    _BatteryTestResult_Type()
)
batteryTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTestResult.setStatus("mandatory")
_InputVoltageX1_Type = Integer32
_InputVoltageX1_Object = MibScalar
inputVoltageX1 = _InputVoltageX1_Object(
    (1, 3, 6, 1, 4, 1, 39145, 13, 17),
    _InputVoltageX1_Type()
)
inputVoltageX1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputVoltageX1.setStatus("mandatory")
_OutputVoltageX100_Type = Integer32
_OutputVoltageX100_Object = MibScalar
outputVoltageX100 = _OutputVoltageX100_Object(
    (1, 3, 6, 1, 4, 1, 39145, 13, 18),
    _OutputVoltageX100_Type()
)
outputVoltageX100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputVoltageX100.setStatus("mandatory")
_OutputCurrentX100_Type = Integer32
_OutputCurrentX100_Object = MibScalar
outputCurrentX100 = _OutputCurrentX100_Object(
    (1, 3, 6, 1, 4, 1, 39145, 13, 19),
    _OutputCurrentX100_Type()
)
outputCurrentX100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputCurrentX100.setStatus("mandatory")
_DeviceAlarms_Type = Integer32
_DeviceAlarms_Object = MibScalar
deviceAlarms = _DeviceAlarms_Object(
    (1, 3, 6, 1, 4, 1, 39145, 13, 20),
    _DeviceAlarms_Type()
)
deviceAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceAlarms.setStatus("mandatory")

# Managed Objects groups


# Notification objects

moduleAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 13, 0, 101)
)
moduleAlarmTrap.setObjects(
    ("ICT-POWERSYSTEM-MIB", "moduleNumber")
)
if mibBuilder.loadTexts:
    moduleAlarmTrap.setStatus(
        ""
    )

alarmInputTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 13, 0, 102)
)
alarmInputTrap.setObjects(
    ("ICT-POWERSYSTEM-MIB", "alarmNumber")
)
if mibBuilder.loadTexts:
    alarmInputTrap.setStatus(
        ""
    )

acFailAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 13, 0, 103)
)
if mibBuilder.loadTexts:
    acFailAlarmTrap.setStatus(
        ""
    )

sysCurrentLimitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 13, 0, 104)
)
if mibBuilder.loadTexts:
    sysCurrentLimitTrap.setStatus(
        ""
    )

moduleAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 13, 0, 111)
)
moduleAlarmClear.setObjects(
    ("ICT-POWERSYSTEM-MIB", "moduleNumber")
)
if mibBuilder.loadTexts:
    moduleAlarmClear.setStatus(
        ""
    )

alarmInputClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 13, 0, 112)
)
alarmInputClear.setObjects(
    ("ICT-POWERSYSTEM-MIB", "alarmNumber")
)
if mibBuilder.loadTexts:
    alarmInputClear.setStatus(
        ""
    )

acFailAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 13, 0, 113)
)
if mibBuilder.loadTexts:
    acFailAlarmClear.setStatus(
        ""
    )

sysCurrentLimitClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 13, 0, 114)
)
if mibBuilder.loadTexts:
    sysCurrentLimitClear.setStatus(
        ""
    )

batteryTestStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 13, 0, 121)
)
if mibBuilder.loadTexts:
    batteryTestStart.setStatus(
        ""
    )

batteryTestComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 13, 0, 122)
)
if mibBuilder.loadTexts:
    batteryTestComplete.setStatus(
        ""
    )

batteryTestFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 13, 0, 123)
)
if mibBuilder.loadTexts:
    batteryTestFail.setStatus(
        ""
    )

batteryEqualizeStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 13, 0, 124)
)
if mibBuilder.loadTexts:
    batteryEqualizeStart.setStatus(
        ""
    )

batteryEqualizeComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 13, 0, 125)
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
    "ICT-POWERSYSTEM-MIB",
    **{"ictPower": ictPower,
       "powerSystem": powerSystem,
       "moduleAlarmTrap": moduleAlarmTrap,
       "alarmInputTrap": alarmInputTrap,
       "acFailAlarmTrap": acFailAlarmTrap,
       "sysCurrentLimitTrap": sysCurrentLimitTrap,
       "moduleAlarmClear": moduleAlarmClear,
       "alarmInputClear": alarmInputClear,
       "acFailAlarmClear": acFailAlarmClear,
       "sysCurrentLimitClear": sysCurrentLimitClear,
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
       "moduleTable": moduleTable,
       "moduleEntry": moduleEntry,
       "moduleNumber": moduleNumber,
       "moduleStatus": moduleStatus,
       "moduleType": moduleType,
       "moduleVoltage": moduleVoltage,
       "moduleCurrentA": moduleCurrentA,
       "moduleCurrentB": moduleCurrentB,
       "moduleCurrentC": moduleCurrentC,
       "moduleCurrentD": moduleCurrentD,
       "moduleControlA": moduleControlA,
       "moduleControlB": moduleControlB,
       "moduleControlC": moduleControlC,
       "moduleControlD": moduleControlD,
       "moduleVoltageX100": moduleVoltageX100,
       "moduleCurrentAX100": moduleCurrentAX100,
       "moduleCurrentBX100": moduleCurrentBX100,
       "moduleCurrentCX100": moduleCurrentCX100,
       "moduleCurrentDX100": moduleCurrentDX100,
       "moduleAlarms": moduleAlarms,
       "alarmTable": alarmTable,
       "alarmEntry": alarmEntry,
       "alarmNumber": alarmNumber,
       "alarmName": alarmName,
       "alarmStatus": alarmStatus,
       "probeTemperature": probeTemperature,
       "batterySoc": batterySoc,
       "batteryNetAh": batteryNetAh,
       "batteryRunTime": batteryRunTime,
       "batteryTestResult": batteryTestResult,
       "inputVoltageX1": inputVoltageX1,
       "outputVoltageX100": outputVoltageX100,
       "outputCurrentX100": outputCurrentX100,
       "deviceAlarms": deviceAlarms}
)
