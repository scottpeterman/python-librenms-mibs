# SNMP MIB module (ICT-PDU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ict\ICT-PDU-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:01:23 2025
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
_DistPanel_ObjectIdentity = ObjectIdentity
distPanel = _DistPanel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39145, 10)
)
_DeviceModel_Type = DisplayString
_DeviceModel_Object = MibScalar
deviceModel = _DeviceModel_Object(
    (1, 3, 6, 1, 4, 1, 39145, 10, 1),
    _DeviceModel_Type()
)
deviceModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceModel.setStatus("mandatory")
_DeviceName_Type = DisplayString
_DeviceName_Object = MibScalar
deviceName = _DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 39145, 10, 2),
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
    (1, 3, 6, 1, 4, 1, 39145, 10, 3),
    _DeviceHardware_Type()
)
deviceHardware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceHardware.setStatus("mandatory")
_DeviceFirmware_Type = DisplayString
_DeviceFirmware_Object = MibScalar
deviceFirmware = _DeviceFirmware_Object(
    (1, 3, 6, 1, 4, 1, 39145, 10, 4),
    _DeviceFirmware_Type()
)
deviceFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceFirmware.setStatus("mandatory")
_DeviceMacAddress_Type = DisplayString
_DeviceMacAddress_Object = MibScalar
deviceMacAddress = _DeviceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 39145, 10, 5),
    _DeviceMacAddress_Type()
)
deviceMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceMacAddress.setStatus("mandatory")
_SystemVoltage_Type = DisplayString
_SystemVoltage_Object = MibScalar
systemVoltage = _SystemVoltage_Object(
    (1, 3, 6, 1, 4, 1, 39145, 10, 6),
    _SystemVoltage_Type()
)
systemVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemVoltage.setStatus("mandatory")
_SystemCurrent_Type = DisplayString
_SystemCurrent_Object = MibScalar
systemCurrent = _SystemCurrent_Object(
    (1, 3, 6, 1, 4, 1, 39145, 10, 7),
    _SystemCurrent_Type()
)
systemCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemCurrent.setStatus("mandatory")
_OutputTable_Object = MibTable
outputTable = _OutputTable_Object(
    (1, 3, 6, 1, 4, 1, 39145, 10, 8)
)
if mibBuilder.loadTexts:
    outputTable.setStatus("mandatory")
_OutputEntry_Object = MibTableRow
outputEntry = _OutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 39145, 10, 8, 1)
)
outputEntry.setIndexNames(
    (0, "ICT-PDU-MIB", "outputNumber"),
)
if mibBuilder.loadTexts:
    outputEntry.setStatus("mandatory")
_OutputNumber_Type = Integer32
_OutputNumber_Object = MibTableColumn
outputNumber = _OutputNumber_Object(
    (1, 3, 6, 1, 4, 1, 39145, 10, 8, 1, 1),
    _OutputNumber_Type()
)
outputNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputNumber.setStatus("mandatory")
_OutputName_Type = DisplayString
_OutputName_Object = MibTableColumn
outputName = _OutputName_Object(
    (1, 3, 6, 1, 4, 1, 39145, 10, 8, 1, 2),
    _OutputName_Type()
)
outputName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputName.setStatus("mandatory")
_OutputCurrent_Type = DisplayString
_OutputCurrent_Object = MibTableColumn
outputCurrent = _OutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 39145, 10, 8, 1, 3),
    _OutputCurrent_Type()
)
outputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputCurrent.setStatus("mandatory")


class _OutputFuseStatus_Type(Integer32):
    """Custom type outputFuseStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("open", 2))
    )


_OutputFuseStatus_Type.__name__ = "Integer32"
_OutputFuseStatus_Object = MibTableColumn
outputFuseStatus = _OutputFuseStatus_Object(
    (1, 3, 6, 1, 4, 1, 39145, 10, 8, 1, 4),
    _OutputFuseStatus_Type()
)
outputFuseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputFuseStatus.setStatus("mandatory")


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
_OutputEnable_Object = MibTableColumn
outputEnable = _OutputEnable_Object(
    (1, 3, 6, 1, 4, 1, 39145, 10, 8, 1, 5),
    _OutputEnable_Type()
)
outputEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputEnable.setStatus("mandatory")
_OutputCurrentX100_Type = Integer32
_OutputCurrentX100_Object = MibTableColumn
outputCurrentX100 = _OutputCurrentX100_Object(
    (1, 3, 6, 1, 4, 1, 39145, 10, 8, 1, 6),
    _OutputCurrentX100_Type()
)
outputCurrentX100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputCurrentX100.setStatus("mandatory")
_AlarmTable_Object = MibTable
alarmTable = _AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 39145, 10, 9)
)
if mibBuilder.loadTexts:
    alarmTable.setStatus("mandatory")
_AlarmEntry_Object = MibTableRow
alarmEntry = _AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 39145, 10, 9, 1)
)
alarmEntry.setIndexNames(
    (0, "ICT-PDU-MIB", "alarmNumber"),
)
if mibBuilder.loadTexts:
    alarmEntry.setStatus("mandatory")
_AlarmNumber_Type = Integer32
_AlarmNumber_Object = MibTableColumn
alarmNumber = _AlarmNumber_Object(
    (1, 3, 6, 1, 4, 1, 39145, 10, 9, 1, 1),
    _AlarmNumber_Type()
)
alarmNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmNumber.setStatus("mandatory")
_AlarmName_Type = DisplayString
_AlarmName_Object = MibTableColumn
alarmName = _AlarmName_Object(
    (1, 3, 6, 1, 4, 1, 39145, 10, 9, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 39145, 10, 9, 1, 3),
    _AlarmStatus_Type()
)
alarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmStatus.setStatus("mandatory")
_BusTable_Object = MibTable
busTable = _BusTable_Object(
    (1, 3, 6, 1, 4, 1, 39145, 10, 10)
)
if mibBuilder.loadTexts:
    busTable.setStatus("mandatory")
_BusEntry_Object = MibTableRow
busEntry = _BusEntry_Object(
    (1, 3, 6, 1, 4, 1, 39145, 10, 10, 1)
)
busEntry.setIndexNames(
    (0, "ICT-PDU-MIB", "busNumber"),
)
if mibBuilder.loadTexts:
    busEntry.setStatus("mandatory")
_BusNumber_Type = Integer32
_BusNumber_Object = MibTableColumn
busNumber = _BusNumber_Object(
    (1, 3, 6, 1, 4, 1, 39145, 10, 10, 1, 1),
    _BusNumber_Type()
)
busNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busNumber.setStatus("mandatory")
_BusName_Type = DisplayString
_BusName_Object = MibTableColumn
busName = _BusName_Object(
    (1, 3, 6, 1, 4, 1, 39145, 10, 10, 1, 2),
    _BusName_Type()
)
busName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busName.setStatus("mandatory")
_BusVoltage_Type = DisplayString
_BusVoltage_Object = MibTableColumn
busVoltage = _BusVoltage_Object(
    (1, 3, 6, 1, 4, 1, 39145, 10, 10, 1, 3),
    _BusVoltage_Type()
)
busVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busVoltage.setStatus("mandatory")
_BusCurrent_Type = DisplayString
_BusCurrent_Object = MibTableColumn
busCurrent = _BusCurrent_Object(
    (1, 3, 6, 1, 4, 1, 39145, 10, 10, 1, 4),
    _BusCurrent_Type()
)
busCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busCurrent.setStatus("mandatory")
_BusVoltageX100_Type = Integer32
_BusVoltageX100_Object = MibTableColumn
busVoltageX100 = _BusVoltageX100_Object(
    (1, 3, 6, 1, 4, 1, 39145, 10, 10, 1, 5),
    _BusVoltageX100_Type()
)
busVoltageX100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busVoltageX100.setStatus("mandatory")
_BusCurrentX100_Type = Integer32
_BusCurrentX100_Object = MibTableColumn
busCurrentX100 = _BusCurrentX100_Object(
    (1, 3, 6, 1, 4, 1, 39145, 10, 10, 1, 6),
    _BusCurrentX100_Type()
)
busCurrentX100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busCurrentX100.setStatus("mandatory")

# Managed Objects groups


# Notification objects

sysUndervoltageAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 10, 0, 101)
)
sysUndervoltageAlarmTrap.setObjects(
    ("ICT-PDU-MIB", "busNumber")
)
if mibBuilder.loadTexts:
    sysUndervoltageAlarmTrap.setStatus(
        ""
    )

sysOvervoltageAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 10, 0, 102)
)
sysOvervoltageAlarmTrap.setObjects(
    ("ICT-PDU-MIB", "busNumber")
)
if mibBuilder.loadTexts:
    sysOvervoltageAlarmTrap.setStatus(
        ""
    )

sysOvercurrentAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 10, 0, 103)
)
sysOvercurrentAlarmTrap.setObjects(
    ("ICT-PDU-MIB", "busNumber")
)
if mibBuilder.loadTexts:
    sysOvercurrentAlarmTrap.setStatus(
        ""
    )

fuseAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 10, 0, 104)
)
fuseAlarmTrap.setObjects(
    ("ICT-PDU-MIB", "outputNumber")
)
if mibBuilder.loadTexts:
    fuseAlarmTrap.setStatus(
        ""
    )

undercurrentAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 10, 0, 105)
)
undercurrentAlarmTrap.setObjects(
    ("ICT-PDU-MIB", "outputNumber")
)
if mibBuilder.loadTexts:
    undercurrentAlarmTrap.setStatus(
        ""
    )

overcurrentAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 10, 0, 106)
)
overcurrentAlarmTrap.setObjects(
    ("ICT-PDU-MIB", "outputNumber")
)
if mibBuilder.loadTexts:
    overcurrentAlarmTrap.setStatus(
        ""
    )

loadshedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 10, 0, 107)
)
loadshedTrap.setObjects(
    ("ICT-PDU-MIB", "outputNumber")
)
if mibBuilder.loadTexts:
    loadshedTrap.setStatus(
        ""
    )

alarmInputTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 10, 0, 108)
)
alarmInputTrap.setObjects(
    ("ICT-PDU-MIB", "alarmNumber")
)
if mibBuilder.loadTexts:
    alarmInputTrap.setStatus(
        ""
    )

sysUndervoltageAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 10, 0, 111)
)
sysUndervoltageAlarmClear.setObjects(
    ("ICT-PDU-MIB", "busNumber")
)
if mibBuilder.loadTexts:
    sysUndervoltageAlarmClear.setStatus(
        ""
    )

sysOvervoltageAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 10, 0, 112)
)
sysOvervoltageAlarmClear.setObjects(
    ("ICT-PDU-MIB", "busNumber")
)
if mibBuilder.loadTexts:
    sysOvervoltageAlarmClear.setStatus(
        ""
    )

sysOvercurrentAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 10, 0, 113)
)
sysOvercurrentAlarmClear.setObjects(
    ("ICT-PDU-MIB", "busNumber")
)
if mibBuilder.loadTexts:
    sysOvercurrentAlarmClear.setStatus(
        ""
    )

fuseAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 10, 0, 114)
)
fuseAlarmClear.setObjects(
    ("ICT-PDU-MIB", "outputNumber")
)
if mibBuilder.loadTexts:
    fuseAlarmClear.setStatus(
        ""
    )

undercurrentAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 10, 0, 115)
)
undercurrentAlarmClear.setObjects(
    ("ICT-PDU-MIB", "outputNumber")
)
if mibBuilder.loadTexts:
    undercurrentAlarmClear.setStatus(
        ""
    )

overcurrentAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 10, 0, 116)
)
overcurrentAlarmClear.setObjects(
    ("ICT-PDU-MIB", "outputNumber")
)
if mibBuilder.loadTexts:
    overcurrentAlarmClear.setStatus(
        ""
    )

loadshedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 10, 0, 117)
)
loadshedClear.setObjects(
    ("ICT-PDU-MIB", "outputNumber")
)
if mibBuilder.loadTexts:
    loadshedClear.setStatus(
        ""
    )

alarmInputClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 10, 0, 118)
)
alarmInputClear.setObjects(
    ("ICT-PDU-MIB", "alarmNumber")
)
if mibBuilder.loadTexts:
    alarmInputClear.setStatus(
        ""
    )

scheduledPowerCycle = NotificationType(
    (1, 3, 6, 1, 4, 1, 39145, 10, 0, 126)
)
scheduledPowerCycle.setObjects(
    ("ICT-PDU-MIB", "outputNumber")
)
if mibBuilder.loadTexts:
    scheduledPowerCycle.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ICT-PDU-MIB",
    **{"ictPower": ictPower,
       "distPanel": distPanel,
       "sysUndervoltageAlarmTrap": sysUndervoltageAlarmTrap,
       "sysOvervoltageAlarmTrap": sysOvervoltageAlarmTrap,
       "sysOvercurrentAlarmTrap": sysOvercurrentAlarmTrap,
       "fuseAlarmTrap": fuseAlarmTrap,
       "undercurrentAlarmTrap": undercurrentAlarmTrap,
       "overcurrentAlarmTrap": overcurrentAlarmTrap,
       "loadshedTrap": loadshedTrap,
       "alarmInputTrap": alarmInputTrap,
       "sysUndervoltageAlarmClear": sysUndervoltageAlarmClear,
       "sysOvervoltageAlarmClear": sysOvervoltageAlarmClear,
       "sysOvercurrentAlarmClear": sysOvercurrentAlarmClear,
       "fuseAlarmClear": fuseAlarmClear,
       "undercurrentAlarmClear": undercurrentAlarmClear,
       "overcurrentAlarmClear": overcurrentAlarmClear,
       "loadshedClear": loadshedClear,
       "alarmInputClear": alarmInputClear,
       "scheduledPowerCycle": scheduledPowerCycle,
       "deviceModel": deviceModel,
       "deviceName": deviceName,
       "deviceHardware": deviceHardware,
       "deviceFirmware": deviceFirmware,
       "deviceMacAddress": deviceMacAddress,
       "systemVoltage": systemVoltage,
       "systemCurrent": systemCurrent,
       "outputTable": outputTable,
       "outputEntry": outputEntry,
       "outputNumber": outputNumber,
       "outputName": outputName,
       "outputCurrent": outputCurrent,
       "outputFuseStatus": outputFuseStatus,
       "outputEnable": outputEnable,
       "outputCurrentX100": outputCurrentX100,
       "alarmTable": alarmTable,
       "alarmEntry": alarmEntry,
       "alarmNumber": alarmNumber,
       "alarmName": alarmName,
       "alarmStatus": alarmStatus,
       "busTable": busTable,
       "busEntry": busEntry,
       "busNumber": busNumber,
       "busName": busName,
       "busVoltage": busVoltage,
       "busCurrent": busCurrent,
       "busVoltageX100": busVoltageX100,
       "busCurrentX100": busCurrentX100}
)
