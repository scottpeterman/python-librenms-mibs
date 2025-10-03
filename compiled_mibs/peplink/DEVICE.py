# SNMP MIB module (DEVICE) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\peplink\DEVICE
# Produced by pysmi-1.6.2 at Thu Oct  2 12:20:40 2025
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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

deviceInfo = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Peplink_ObjectIdentity = ObjectIdentity
peplink = _Peplink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23695)
)
_ProductMib_ObjectIdentity = ObjectIdentity
productMib = _ProductMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23695, 200)
)
_GeneralMib_ObjectIdentity = ObjectIdentity
generalMib = _GeneralMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1)
)
_DeviceMib_ObjectIdentity = ObjectIdentity
deviceMib = _DeviceMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 1)
)
_DeviceInfoSystem_ObjectIdentity = ObjectIdentity
deviceInfoSystem = _DeviceInfoSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 1, 1, 1)
)
_DeviceModel_Type = OctetString
_DeviceModel_Object = MibScalar
deviceModel = _DeviceModel_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 1, 1, 1, 1),
    _DeviceModel_Type()
)
deviceModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceModel.setStatus("current")
_DeviceSerialNumber_Type = OctetString
_DeviceSerialNumber_Object = MibScalar
deviceSerialNumber = _DeviceSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 1, 1, 1, 2),
    _DeviceSerialNumber_Type()
)
deviceSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceSerialNumber.setStatus("current")
_DeviceFirmwareVersion_Type = OctetString
_DeviceFirmwareVersion_Object = MibScalar
deviceFirmwareVersion = _DeviceFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 1, 1, 1, 3),
    _DeviceFirmwareVersion_Type()
)
deviceFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceFirmwareVersion.setStatus("current")
_DeviceInfoTime_ObjectIdentity = ObjectIdentity
deviceInfoTime = _DeviceInfoTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 1, 1, 2)
)
_DeviceSystemTime_Type = OctetString
_DeviceSystemTime_Object = MibScalar
deviceSystemTime = _DeviceSystemTime_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 1, 1, 2, 1),
    _DeviceSystemTime_Type()
)
deviceSystemTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceSystemTime.setStatus("current")
_DeviceSystemUpTime_Type = OctetString
_DeviceSystemUpTime_Object = MibScalar
deviceSystemUpTime = _DeviceSystemUpTime_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 1, 1, 2, 2),
    _DeviceSystemUpTime_Type()
)
deviceSystemUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceSystemUpTime.setStatus("current")
_DeviceInfoUsage_ObjectIdentity = ObjectIdentity
deviceInfoUsage = _DeviceInfoUsage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 1, 1, 3)
)


class _DeviceCpuLoad_Type(Integer32):
    """Custom type deviceCpuLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DeviceCpuLoad_Type.__name__ = "Integer32"
_DeviceCpuLoad_Object = MibScalar
deviceCpuLoad = _DeviceCpuLoad_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 1, 1, 3, 1),
    _DeviceCpuLoad_Type()
)
deviceCpuLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceCpuLoad.setStatus("current")
_DeviceTotalMemory_Type = Integer32
_DeviceTotalMemory_Object = MibScalar
deviceTotalMemory = _DeviceTotalMemory_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 1, 1, 3, 2),
    _DeviceTotalMemory_Type()
)
deviceTotalMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceTotalMemory.setStatus("current")
_DeviceMemoryUsage_Type = Integer32
_DeviceMemoryUsage_Object = MibScalar
deviceMemoryUsage = _DeviceMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 1, 1, 3, 3),
    _DeviceMemoryUsage_Type()
)
deviceMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceMemoryUsage.setStatus("current")
_DeviceInfoHardware_ObjectIdentity = ObjectIdentity
deviceInfoHardware = _DeviceInfoHardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 1, 1, 4)
)
_DevicePSUTable_Object = MibTable
devicePSUTable = _DevicePSUTable_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    devicePSUTable.setStatus("current")
_DevicePSUEntry_Object = MibTableRow
devicePSUEntry = _DevicePSUEntry_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 1, 1, 4, 1, 1)
)
devicePSUEntry.setIndexNames(
    (0, "DEVICE", "devicePSUId"),
)
if mibBuilder.loadTexts:
    devicePSUEntry.setStatus("current")
_DevicePSUId_Type = Integer32
_DevicePSUId_Object = MibTableColumn
devicePSUId = _DevicePSUId_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 1, 1, 4, 1, 1, 1),
    _DevicePSUId_Type()
)
devicePSUId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devicePSUId.setStatus("current")


class _DevicePSUStatus_Type(Integer32):
    """Custom type devicePSUStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("on", 1))
    )


_DevicePSUStatus_Type.__name__ = "Integer32"
_DevicePSUStatus_Object = MibTableColumn
devicePSUStatus = _DevicePSUStatus_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 1, 1, 4, 1, 1, 2),
    _DevicePSUStatus_Type()
)
devicePSUStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devicePSUStatus.setStatus("current")
_DeviceCurrentPower_Type = Integer32
_DeviceCurrentPower_Object = MibTableColumn
deviceCurrentPower = _DeviceCurrentPower_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 1, 1, 4, 1, 1, 3),
    _DeviceCurrentPower_Type()
)
deviceCurrentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceCurrentPower.setStatus("current")
_DeviceMaxPower_Type = Integer32
_DeviceMaxPower_Object = MibTableColumn
deviceMaxPower = _DeviceMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 1, 1, 4, 1, 1, 4),
    _DeviceMaxPower_Type()
)
deviceMaxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceMaxPower.setStatus("current")
_DevicePSUPercentage_Type = Integer32
_DevicePSUPercentage_Object = MibTableColumn
devicePSUPercentage = _DevicePSUPercentage_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 1, 1, 4, 1, 1, 5),
    _DevicePSUPercentage_Type()
)
devicePSUPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devicePSUPercentage.setStatus("current")
_DeviceFanTable_Object = MibTable
deviceFanTable = _DeviceFanTable_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    deviceFanTable.setStatus("current")
_DeviceFanEntry_Object = MibTableRow
deviceFanEntry = _DeviceFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 1, 1, 4, 2, 1)
)
deviceFanEntry.setIndexNames(
    (0, "DEVICE", "deviceFanId"),
)
if mibBuilder.loadTexts:
    deviceFanEntry.setStatus("current")
_DeviceFanId_Type = Integer32
_DeviceFanId_Object = MibTableColumn
deviceFanId = _DeviceFanId_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 1, 1, 4, 2, 1, 1),
    _DeviceFanId_Type()
)
deviceFanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceFanId.setStatus("current")


class _DeviceFanStatus_Type(Integer32):
    """Custom type deviceFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("on", 1))
    )


_DeviceFanStatus_Type.__name__ = "Integer32"
_DeviceFanStatus_Object = MibTableColumn
deviceFanStatus = _DeviceFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 1, 1, 4, 2, 1, 2),
    _DeviceFanStatus_Type()
)
deviceFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceFanStatus.setStatus("current")
_DeviceFanSpeed_Type = Integer32
_DeviceFanSpeed_Object = MibTableColumn
deviceFanSpeed = _DeviceFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 1, 1, 4, 2, 1, 3),
    _DeviceFanSpeed_Type()
)
deviceFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceFanSpeed.setStatus("current")
_DevicePowerSourceTable_Object = MibTable
devicePowerSourceTable = _DevicePowerSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 1, 1, 4, 3)
)
if mibBuilder.loadTexts:
    devicePowerSourceTable.setStatus("current")
_DevicePowerSourceEntry_Object = MibTableRow
devicePowerSourceEntry = _DevicePowerSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 1, 1, 4, 3, 1)
)
devicePowerSourceEntry.setIndexNames(
    (0, "DEVICE", "devicePowerSourceId"),
)
if mibBuilder.loadTexts:
    devicePowerSourceEntry.setStatus("current")
_DevicePowerSourceId_Type = Integer32
_DevicePowerSourceId_Object = MibTableColumn
devicePowerSourceId = _DevicePowerSourceId_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 1, 1, 4, 3, 1, 1),
    _DevicePowerSourceId_Type()
)
devicePowerSourceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devicePowerSourceId.setStatus("current")
_DevicePowerSourceName_Type = OctetString
_DevicePowerSourceName_Object = MibTableColumn
devicePowerSourceName = _DevicePowerSourceName_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 1, 1, 4, 3, 1, 2),
    _DevicePowerSourceName_Type()
)
devicePowerSourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devicePowerSourceName.setStatus("current")


class _DevicePowerSourceStatus_Type(Integer32):
    """Custom type devicePowerSourceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noCableDetected", 0),
          ("connected", 1))
    )


_DevicePowerSourceStatus_Type.__name__ = "Integer32"
_DevicePowerSourceStatus_Object = MibTableColumn
devicePowerSourceStatus = _DevicePowerSourceStatus_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 1, 1, 4, 3, 1, 3),
    _DevicePowerSourceStatus_Type()
)
devicePowerSourceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devicePowerSourceStatus.setStatus("current")
_DeviceInfoTemperature_ObjectIdentity = ObjectIdentity
deviceInfoTemperature = _DeviceInfoTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 1, 1, 4, 4)
)
_DeviceTemperatureCelsius_Type = Gauge32
_DeviceTemperatureCelsius_Object = MibScalar
deviceTemperatureCelsius = _DeviceTemperatureCelsius_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 1, 1, 4, 4, 1),
    _DeviceTemperatureCelsius_Type()
)
deviceTemperatureCelsius.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceTemperatureCelsius.setStatus("current")
if mibBuilder.loadTexts:
    deviceTemperatureCelsius.setUnits("mC")
_DeviceTemperatureFahrenheit_Type = Gauge32
_DeviceTemperatureFahrenheit_Object = MibScalar
deviceTemperatureFahrenheit = _DeviceTemperatureFahrenheit_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 1, 1, 4, 4, 2),
    _DeviceTemperatureFahrenheit_Type()
)
deviceTemperatureFahrenheit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceTemperatureFahrenheit.setStatus("current")
if mibBuilder.loadTexts:
    deviceTemperatureFahrenheit.setUnits("mF")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DEVICE",
    **{"peplink": peplink,
       "productMib": productMib,
       "generalMib": generalMib,
       "deviceMib": deviceMib,
       "deviceInfo": deviceInfo,
       "deviceInfoSystem": deviceInfoSystem,
       "deviceModel": deviceModel,
       "deviceSerialNumber": deviceSerialNumber,
       "deviceFirmwareVersion": deviceFirmwareVersion,
       "deviceInfoTime": deviceInfoTime,
       "deviceSystemTime": deviceSystemTime,
       "deviceSystemUpTime": deviceSystemUpTime,
       "deviceInfoUsage": deviceInfoUsage,
       "deviceCpuLoad": deviceCpuLoad,
       "deviceTotalMemory": deviceTotalMemory,
       "deviceMemoryUsage": deviceMemoryUsage,
       "deviceInfoHardware": deviceInfoHardware,
       "devicePSUTable": devicePSUTable,
       "devicePSUEntry": devicePSUEntry,
       "devicePSUId": devicePSUId,
       "devicePSUStatus": devicePSUStatus,
       "deviceCurrentPower": deviceCurrentPower,
       "deviceMaxPower": deviceMaxPower,
       "devicePSUPercentage": devicePSUPercentage,
       "deviceFanTable": deviceFanTable,
       "deviceFanEntry": deviceFanEntry,
       "deviceFanId": deviceFanId,
       "deviceFanStatus": deviceFanStatus,
       "deviceFanSpeed": deviceFanSpeed,
       "devicePowerSourceTable": devicePowerSourceTable,
       "devicePowerSourceEntry": devicePowerSourceEntry,
       "devicePowerSourceId": devicePowerSourceId,
       "devicePowerSourceName": devicePowerSourceName,
       "devicePowerSourceStatus": devicePowerSourceStatus,
       "deviceInfoTemperature": deviceInfoTemperature,
       "deviceTemperatureCelsius": deviceTemperatureCelsius,
       "deviceTemperatureFahrenheit": deviceTemperatureFahrenheit}
)
