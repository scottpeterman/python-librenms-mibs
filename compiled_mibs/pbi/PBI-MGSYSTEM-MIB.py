# SNMP MIB module (PBI-MGSYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\pbi\PBI-MGSYSTEM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:20:30 2025
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

(mg,) = mibBuilder.importSymbols(
    "PBI-MAIN-MIB",
    "mg")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

mgSystem = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1)
)
if mibBuilder.loadTexts:
    mgSystem.setRevisions(
        ("2006-09-13 10:23",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BasicInfo_ObjectIdentity = ObjectIdentity
basicInfo = _BasicInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1)
)


class _UnitName_Type(DisplayString):
    """Custom type unitName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UnitName_Type.__name__ = "DisplayString"
_UnitName_Object = MibScalar
unitName = _UnitName_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 1),
    _UnitName_Type()
)
unitName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitName.setStatus("current")
_SerialNumber_Type = DisplayString
_SerialNumber_Object = MibScalar
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 2),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("current")
_FpgaVersion_Type = DisplayString
_FpgaVersion_Object = MibScalar
fpgaVersion = _FpgaVersion_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 3),
    _FpgaVersion_Type()
)
fpgaVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpgaVersion.setStatus("current")
_McuVersion_Type = DisplayString
_McuVersion_Object = MibScalar
mcuVersion = _McuVersion_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 4),
    _McuVersion_Type()
)
mcuVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcuVersion.setStatus("current")


class _MacAddress_Type(DisplayString):
    """Custom type macAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MacAddress_Type.__name__ = "DisplayString"
_MacAddress_Object = MibScalar
macAddress = _MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 5),
    _MacAddress_Type()
)
macAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macAddress.setStatus("current")
_Gateway_Type = IpAddress
_Gateway_Object = MibScalar
gateway = _Gateway_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 6),
    _Gateway_Type()
)
gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gateway.setStatus("current")
_DeviceIP_Type = IpAddress
_DeviceIP_Object = MibScalar
deviceIP = _DeviceIP_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 7),
    _DeviceIP_Type()
)
deviceIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceIP.setStatus("current")
_SubnetMask_Type = IpAddress
_SubnetMask_Object = MibScalar
subnetMask = _SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 8),
    _SubnetMask_Type()
)
subnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetMask.setStatus("current")
_TrapIpAddress_Type = IpAddress
_TrapIpAddress_Object = MibScalar
trapIpAddress = _TrapIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 9),
    _TrapIpAddress_Type()
)
trapIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapIpAddress.setStatus("current")


class _Upgrade_Type(Integer32):
    """Custom type upgrade based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_Upgrade_Type.__name__ = "Integer32"
_Upgrade_Object = MibScalar
upgrade = _Upgrade_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 10),
    _Upgrade_Type()
)
upgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upgrade.setStatus("current")
_UpgradeIP_Type = IpAddress
_UpgradeIP_Object = MibScalar
upgradeIP = _UpgradeIP_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 11),
    _UpgradeIP_Type()
)
upgradeIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upgradeIP.setStatus("current")


class _Default_Type(Integer32):
    """Custom type default based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_Default_Type.__name__ = "Integer32"
_Default_Object = MibScalar
default = _Default_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 12),
    _Default_Type()
)
default.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default.setStatus("current")
_DeviceType_Type = Integer32
_DeviceType_Object = MibScalar
deviceType = _DeviceType_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 13),
    _DeviceType_Type()
)
deviceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceType.setStatus("current")
_HardwareVersion_Type = DisplayString
_HardwareVersion_Object = MibScalar
hardwareVersion = _HardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 14),
    _HardwareVersion_Type()
)
hardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareVersion.setStatus("current")
_ExterndBoard_Type = TruthValue
_ExterndBoard_Object = MibScalar
externdBoard = _ExterndBoard_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 15),
    _ExterndBoard_Type()
)
externdBoard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externdBoard.setStatus("current")
_TrapDeviceOffTable_Object = MibTable
trapDeviceOffTable = _TrapDeviceOffTable_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 16)
)
if mibBuilder.loadTexts:
    trapDeviceOffTable.setStatus("current")
_TrapDeviceOffEntry_Object = MibTableRow
trapDeviceOffEntry = _TrapDeviceOffEntry_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 16, 1)
)
trapDeviceOffEntry.setIndexNames(
    (0, "PBI-MGSYSTEM-MIB", "deviceOffDeviceName"),
)
if mibBuilder.loadTexts:
    trapDeviceOffEntry.setStatus("current")
_DeviceOffDeviceName_Type = DisplayString
_DeviceOffDeviceName_Object = MibTableColumn
deviceOffDeviceName = _DeviceOffDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 16, 1, 1),
    _DeviceOffDeviceName_Type()
)
deviceOffDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceOffDeviceName.setStatus("current")
_DeviceOffDeviceIP_Type = DisplayString
_DeviceOffDeviceIP_Object = MibTableColumn
deviceOffDeviceIP = _DeviceOffDeviceIP_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 16, 1, 2),
    _DeviceOffDeviceIP_Type()
)
deviceOffDeviceIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceOffDeviceIP.setStatus("current")
_DeviceOffReserve_Type = DisplayString
_DeviceOffReserve_Object = MibTableColumn
deviceOffReserve = _DeviceOffReserve_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 16, 1, 3),
    _DeviceOffReserve_Type()
)
deviceOffReserve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceOffReserve.setStatus("current")
_DeviceOffLevel_Type = DisplayString
_DeviceOffLevel_Object = MibTableColumn
deviceOffLevel = _DeviceOffLevel_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 16, 1, 4),
    _DeviceOffLevel_Type()
)
deviceOffLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceOffLevel.setStatus("current")
_DeviceOffTriggerTime_Type = DisplayString
_DeviceOffTriggerTime_Object = MibTableColumn
deviceOffTriggerTime = _DeviceOffTriggerTime_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 16, 1, 5),
    _DeviceOffTriggerTime_Type()
)
deviceOffTriggerTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceOffTriggerTime.setStatus("current")
_DeviceOffDescription_Type = DisplayString
_DeviceOffDescription_Object = MibTableColumn
deviceOffDescription = _DeviceOffDescription_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 16, 1, 6),
    _DeviceOffDescription_Type()
)
deviceOffDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceOffDescription.setStatus("current")
_TrapDeviceOnTable_Object = MibTable
trapDeviceOnTable = _TrapDeviceOnTable_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 17)
)
if mibBuilder.loadTexts:
    trapDeviceOnTable.setStatus("current")
_TrapDeviceOnEntry_Object = MibTableRow
trapDeviceOnEntry = _TrapDeviceOnEntry_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 17, 1)
)
trapDeviceOnEntry.setIndexNames(
    (0, "PBI-MGSYSTEM-MIB", "deviceOnDeviceName"),
)
if mibBuilder.loadTexts:
    trapDeviceOnEntry.setStatus("current")
_DeviceOnDeviceName_Type = DisplayString
_DeviceOnDeviceName_Object = MibTableColumn
deviceOnDeviceName = _DeviceOnDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 17, 1, 1),
    _DeviceOnDeviceName_Type()
)
deviceOnDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceOnDeviceName.setStatus("current")
_DeviceOnDeviceIP_Type = DisplayString
_DeviceOnDeviceIP_Object = MibTableColumn
deviceOnDeviceIP = _DeviceOnDeviceIP_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 17, 1, 2),
    _DeviceOnDeviceIP_Type()
)
deviceOnDeviceIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceOnDeviceIP.setStatus("current")
_DeviceOnReserve_Type = DisplayString
_DeviceOnReserve_Object = MibTableColumn
deviceOnReserve = _DeviceOnReserve_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 17, 1, 3),
    _DeviceOnReserve_Type()
)
deviceOnReserve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceOnReserve.setStatus("current")
_DeviceOnLevel_Type = DisplayString
_DeviceOnLevel_Object = MibTableColumn
deviceOnLevel = _DeviceOnLevel_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 17, 1, 4),
    _DeviceOnLevel_Type()
)
deviceOnLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceOnLevel.setStatus("current")
_DeviceOnTriggerTime_Type = DisplayString
_DeviceOnTriggerTime_Object = MibTableColumn
deviceOnTriggerTime = _DeviceOnTriggerTime_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 17, 1, 5),
    _DeviceOnTriggerTime_Type()
)
deviceOnTriggerTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceOnTriggerTime.setStatus("current")
_DeviceOnDescription_Type = DisplayString
_DeviceOnDescription_Object = MibTableColumn
deviceOnDescription = _DeviceOnDescription_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 17, 1, 6),
    _DeviceOnDescription_Type()
)
deviceOnDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceOnDescription.setStatus("current")
_TrapFanFailedTable_Object = MibTable
trapFanFailedTable = _TrapFanFailedTable_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 18)
)
if mibBuilder.loadTexts:
    trapFanFailedTable.setStatus("current")
_TrapFanFailedEntry_Object = MibTableRow
trapFanFailedEntry = _TrapFanFailedEntry_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 18, 1)
)
trapFanFailedEntry.setIndexNames(
    (0, "PBI-MGSYSTEM-MIB", "fanFailedDeviceName"),
)
if mibBuilder.loadTexts:
    trapFanFailedEntry.setStatus("current")
_FanFailedDeviceName_Type = DisplayString
_FanFailedDeviceName_Object = MibTableColumn
fanFailedDeviceName = _FanFailedDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 18, 1, 1),
    _FanFailedDeviceName_Type()
)
fanFailedDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanFailedDeviceName.setStatus("current")
_FanFailedDeviceIP_Type = DisplayString
_FanFailedDeviceIP_Object = MibTableColumn
fanFailedDeviceIP = _FanFailedDeviceIP_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 18, 1, 2),
    _FanFailedDeviceIP_Type()
)
fanFailedDeviceIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanFailedDeviceIP.setStatus("current")
_FanFailedReserve_Type = DisplayString
_FanFailedReserve_Object = MibTableColumn
fanFailedReserve = _FanFailedReserve_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 18, 1, 3),
    _FanFailedReserve_Type()
)
fanFailedReserve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanFailedReserve.setStatus("current")
_FanFailedLevel_Type = DisplayString
_FanFailedLevel_Object = MibTableColumn
fanFailedLevel = _FanFailedLevel_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 18, 1, 4),
    _FanFailedLevel_Type()
)
fanFailedLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanFailedLevel.setStatus("current")
_FanFailedTriggerTime_Type = DisplayString
_FanFailedTriggerTime_Object = MibTableColumn
fanFailedTriggerTime = _FanFailedTriggerTime_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 18, 1, 5),
    _FanFailedTriggerTime_Type()
)
fanFailedTriggerTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanFailedTriggerTime.setStatus("current")
_FanFailedDescription_Type = DisplayString
_FanFailedDescription_Object = MibTableColumn
fanFailedDescription = _FanFailedDescription_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 18, 1, 6),
    _FanFailedDescription_Type()
)
fanFailedDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanFailedDescription.setStatus("current")
_TrapSignalOffTable_Object = MibTable
trapSignalOffTable = _TrapSignalOffTable_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 19)
)
if mibBuilder.loadTexts:
    trapSignalOffTable.setStatus("current")
_TrapSignalOffEntry_Object = MibTableRow
trapSignalOffEntry = _TrapSignalOffEntry_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 19, 1)
)
trapSignalOffEntry.setIndexNames(
    (0, "PBI-MGSYSTEM-MIB", "signalOffDeviceName"),
)
if mibBuilder.loadTexts:
    trapSignalOffEntry.setStatus("current")
_SignalOffDeviceName_Type = DisplayString
_SignalOffDeviceName_Object = MibTableColumn
signalOffDeviceName = _SignalOffDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 19, 1, 1),
    _SignalOffDeviceName_Type()
)
signalOffDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalOffDeviceName.setStatus("current")
_SignalOffDeviceIP_Type = DisplayString
_SignalOffDeviceIP_Object = MibTableColumn
signalOffDeviceIP = _SignalOffDeviceIP_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 19, 1, 2),
    _SignalOffDeviceIP_Type()
)
signalOffDeviceIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalOffDeviceIP.setStatus("current")
_SignalOffChannel_Type = DisplayString
_SignalOffChannel_Object = MibTableColumn
signalOffChannel = _SignalOffChannel_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 19, 1, 3),
    _SignalOffChannel_Type()
)
signalOffChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalOffChannel.setStatus("current")
_SignalOffLevel_Type = DisplayString
_SignalOffLevel_Object = MibTableColumn
signalOffLevel = _SignalOffLevel_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 19, 1, 4),
    _SignalOffLevel_Type()
)
signalOffLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalOffLevel.setStatus("current")
_SignalOffTriggerTime_Type = DisplayString
_SignalOffTriggerTime_Object = MibTableColumn
signalOffTriggerTime = _SignalOffTriggerTime_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 19, 1, 5),
    _SignalOffTriggerTime_Type()
)
signalOffTriggerTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalOffTriggerTime.setStatus("current")
_SignalOffDescription_Type = DisplayString
_SignalOffDescription_Object = MibTableColumn
signalOffDescription = _SignalOffDescription_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 19, 1, 6),
    _SignalOffDescription_Type()
)
signalOffDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalOffDescription.setStatus("current")
_SignalOffSlot_Type = DisplayString
_SignalOffSlot_Object = MibTableColumn
signalOffSlot = _SignalOffSlot_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 19, 1, 7),
    _SignalOffSlot_Type()
)
signalOffSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalOffSlot.setStatus("current")
_TrapSignalOnTable_Object = MibTable
trapSignalOnTable = _TrapSignalOnTable_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 20)
)
if mibBuilder.loadTexts:
    trapSignalOnTable.setStatus("current")
_TrapSignalOnEntry_Object = MibTableRow
trapSignalOnEntry = _TrapSignalOnEntry_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 20, 1)
)
trapSignalOnEntry.setIndexNames(
    (0, "PBI-MGSYSTEM-MIB", "signalOnDeviceName"),
)
if mibBuilder.loadTexts:
    trapSignalOnEntry.setStatus("current")
_SignalOnDeviceName_Type = DisplayString
_SignalOnDeviceName_Object = MibTableColumn
signalOnDeviceName = _SignalOnDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 20, 1, 1),
    _SignalOnDeviceName_Type()
)
signalOnDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalOnDeviceName.setStatus("current")
_SignalOnDeviceIP_Type = DisplayString
_SignalOnDeviceIP_Object = MibTableColumn
signalOnDeviceIP = _SignalOnDeviceIP_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 20, 1, 2),
    _SignalOnDeviceIP_Type()
)
signalOnDeviceIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalOnDeviceIP.setStatus("current")
_SignalOnChannel_Type = DisplayString
_SignalOnChannel_Object = MibTableColumn
signalOnChannel = _SignalOnChannel_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 20, 1, 3),
    _SignalOnChannel_Type()
)
signalOnChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalOnChannel.setStatus("current")
_SignalOnLevel_Type = DisplayString
_SignalOnLevel_Object = MibTableColumn
signalOnLevel = _SignalOnLevel_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 20, 1, 4),
    _SignalOnLevel_Type()
)
signalOnLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalOnLevel.setStatus("current")
_SignalOnTriggerTime_Type = DisplayString
_SignalOnTriggerTime_Object = MibTableColumn
signalOnTriggerTime = _SignalOnTriggerTime_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 20, 1, 5),
    _SignalOnTriggerTime_Type()
)
signalOnTriggerTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalOnTriggerTime.setStatus("current")
_SignalOnDescription_Type = DisplayString
_SignalOnDescription_Object = MibTableColumn
signalOnDescription = _SignalOnDescription_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 20, 1, 6),
    _SignalOnDescription_Type()
)
signalOnDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalOnDescription.setStatus("current")
_SignalOnSlot_Type = DisplayString
_SignalOnSlot_Object = MibTableColumn
signalOnSlot = _SignalOnSlot_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 20, 1, 7),
    _SignalOnSlot_Type()
)
signalOnSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalOnSlot.setStatus("current")
_TrapSignalChangeTable_Object = MibTable
trapSignalChangeTable = _TrapSignalChangeTable_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 21)
)
if mibBuilder.loadTexts:
    trapSignalChangeTable.setStatus("current")
_TrapSignalChangeEntry_Object = MibTableRow
trapSignalChangeEntry = _TrapSignalChangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 21, 1)
)
trapSignalChangeEntry.setIndexNames(
    (0, "PBI-MGSYSTEM-MIB", "signalChangeDeviceName"),
)
if mibBuilder.loadTexts:
    trapSignalChangeEntry.setStatus("current")
_SignalChangeDeviceName_Type = DisplayString
_SignalChangeDeviceName_Object = MibTableColumn
signalChangeDeviceName = _SignalChangeDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 21, 1, 1),
    _SignalChangeDeviceName_Type()
)
signalChangeDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalChangeDeviceName.setStatus("current")
_SignalChangeDeviceIP_Type = DisplayString
_SignalChangeDeviceIP_Object = MibTableColumn
signalChangeDeviceIP = _SignalChangeDeviceIP_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 21, 1, 2),
    _SignalChangeDeviceIP_Type()
)
signalChangeDeviceIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalChangeDeviceIP.setStatus("current")
_SignalChangeChannel_Type = DisplayString
_SignalChangeChannel_Object = MibTableColumn
signalChangeChannel = _SignalChangeChannel_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 21, 1, 3),
    _SignalChangeChannel_Type()
)
signalChangeChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalChangeChannel.setStatus("current")
_SignalChangeLevel_Type = DisplayString
_SignalChangeLevel_Object = MibTableColumn
signalChangeLevel = _SignalChangeLevel_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 21, 1, 4),
    _SignalChangeLevel_Type()
)
signalChangeLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalChangeLevel.setStatus("current")
_SignalChangeTriggerTime_Type = DisplayString
_SignalChangeTriggerTime_Object = MibTableColumn
signalChangeTriggerTime = _SignalChangeTriggerTime_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 21, 1, 5),
    _SignalChangeTriggerTime_Type()
)
signalChangeTriggerTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalChangeTriggerTime.setStatus("current")
_SignalChangeDescription_Type = DisplayString
_SignalChangeDescription_Object = MibTableColumn
signalChangeDescription = _SignalChangeDescription_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 21, 1, 6),
    _SignalChangeDescription_Type()
)
signalChangeDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalChangeDescription.setStatus("current")
_SignalChangeSlot_Type = DisplayString
_SignalChangeSlot_Object = MibTableColumn
signalChangeSlot = _SignalChangeSlot_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 21, 1, 7),
    _SignalChangeSlot_Type()
)
signalChangeSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalChangeSlot.setStatus("current")
_TrapTSOverflowTable_Object = MibTable
trapTSOverflowTable = _TrapTSOverflowTable_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 22)
)
if mibBuilder.loadTexts:
    trapTSOverflowTable.setStatus("current")
_TrapTSOverflowEntry_Object = MibTableRow
trapTSOverflowEntry = _TrapTSOverflowEntry_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 22, 1)
)
trapTSOverflowEntry.setIndexNames(
    (0, "PBI-MGSYSTEM-MIB", "tsOverflowDeviceName"),
)
if mibBuilder.loadTexts:
    trapTSOverflowEntry.setStatus("current")
_TsOverflowDeviceName_Type = DisplayString
_TsOverflowDeviceName_Object = MibTableColumn
tsOverflowDeviceName = _TsOverflowDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 22, 1, 1),
    _TsOverflowDeviceName_Type()
)
tsOverflowDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsOverflowDeviceName.setStatus("current")
_TsOverflowDeviceIP_Type = DisplayString
_TsOverflowDeviceIP_Object = MibTableColumn
tsOverflowDeviceIP = _TsOverflowDeviceIP_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 22, 1, 2),
    _TsOverflowDeviceIP_Type()
)
tsOverflowDeviceIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsOverflowDeviceIP.setStatus("current")
_TsOverflowChannel_Type = DisplayString
_TsOverflowChannel_Object = MibTableColumn
tsOverflowChannel = _TsOverflowChannel_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 22, 1, 3),
    _TsOverflowChannel_Type()
)
tsOverflowChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsOverflowChannel.setStatus("current")
_TsOverflowLevel_Type = DisplayString
_TsOverflowLevel_Object = MibTableColumn
tsOverflowLevel = _TsOverflowLevel_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 22, 1, 4),
    _TsOverflowLevel_Type()
)
tsOverflowLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsOverflowLevel.setStatus("current")
_TsOverflowTriggerTime_Type = DisplayString
_TsOverflowTriggerTime_Object = MibTableColumn
tsOverflowTriggerTime = _TsOverflowTriggerTime_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 22, 1, 5),
    _TsOverflowTriggerTime_Type()
)
tsOverflowTriggerTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsOverflowTriggerTime.setStatus("current")
_TsOverflowDescription_Type = DisplayString
_TsOverflowDescription_Object = MibTableColumn
tsOverflowDescription = _TsOverflowDescription_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 22, 1, 6),
    _TsOverflowDescription_Type()
)
tsOverflowDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsOverflowDescription.setStatus("current")
_TsOverflowSlot_Type = DisplayString
_TsOverflowSlot_Object = MibTableColumn
tsOverflowSlot = _TsOverflowSlot_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 22, 1, 7),
    _TsOverflowSlot_Type()
)
tsOverflowSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsOverflowSlot.setStatus("current")
_RebootCommand_Type = Integer32
_RebootCommand_Object = MibScalar
rebootCommand = _RebootCommand_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 23),
    _RebootCommand_Type()
)
rebootCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rebootCommand.setStatus("current")
_TrapTSIDErrorTable_Object = MibTable
trapTSIDErrorTable = _TrapTSIDErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 24)
)
if mibBuilder.loadTexts:
    trapTSIDErrorTable.setStatus("current")
_TrapTSIDErrorEntry_Object = MibTableRow
trapTSIDErrorEntry = _TrapTSIDErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 24, 1)
)
trapTSIDErrorEntry.setIndexNames(
    (0, "PBI-MGSYSTEM-MIB", "tsIDErrorDeviceName"),
)
if mibBuilder.loadTexts:
    trapTSIDErrorEntry.setStatus("current")
_TsIDErrorDeviceName_Type = DisplayString
_TsIDErrorDeviceName_Object = MibTableColumn
tsIDErrorDeviceName = _TsIDErrorDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 24, 1, 1),
    _TsIDErrorDeviceName_Type()
)
tsIDErrorDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsIDErrorDeviceName.setStatus("current")
_TsIDErrorDeviceIP_Type = DisplayString
_TsIDErrorDeviceIP_Object = MibTableColumn
tsIDErrorDeviceIP = _TsIDErrorDeviceIP_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 24, 1, 2),
    _TsIDErrorDeviceIP_Type()
)
tsIDErrorDeviceIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsIDErrorDeviceIP.setStatus("current")
_TsIDErrorTsID_Type = DisplayString
_TsIDErrorTsID_Object = MibTableColumn
tsIDErrorTsID = _TsIDErrorTsID_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 24, 1, 3),
    _TsIDErrorTsID_Type()
)
tsIDErrorTsID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsIDErrorTsID.setStatus("current")
_TsIDErrorLevel_Type = DisplayString
_TsIDErrorLevel_Object = MibTableColumn
tsIDErrorLevel = _TsIDErrorLevel_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 24, 1, 4),
    _TsIDErrorLevel_Type()
)
tsIDErrorLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsIDErrorLevel.setStatus("current")
_TsIDErrorTriggerTime_Type = DisplayString
_TsIDErrorTriggerTime_Object = MibTableColumn
tsIDErrorTriggerTime = _TsIDErrorTriggerTime_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 24, 1, 5),
    _TsIDErrorTriggerTime_Type()
)
tsIDErrorTriggerTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsIDErrorTriggerTime.setStatus("current")
_TsIDErrorDescription_Type = DisplayString
_TsIDErrorDescription_Object = MibTableColumn
tsIDErrorDescription = _TsIDErrorDescription_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 24, 1, 6),
    _TsIDErrorDescription_Type()
)
tsIDErrorDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsIDErrorDescription.setStatus("current")
_TsIDErrorSlot_Type = DisplayString
_TsIDErrorSlot_Object = MibTableColumn
tsIDErrorSlot = _TsIDErrorSlot_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 24, 1, 7),
    _TsIDErrorSlot_Type()
)
tsIDErrorSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsIDErrorSlot.setStatus("current")
_TrapTSIDRightTable_Object = MibTable
trapTSIDRightTable = _TrapTSIDRightTable_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 25)
)
if mibBuilder.loadTexts:
    trapTSIDRightTable.setStatus("current")
_TrapTSIDRightEntry_Object = MibTableRow
trapTSIDRightEntry = _TrapTSIDRightEntry_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 25, 1)
)
trapTSIDRightEntry.setIndexNames(
    (0, "PBI-MGSYSTEM-MIB", "tsIDRightDeviceName"),
)
if mibBuilder.loadTexts:
    trapTSIDRightEntry.setStatus("current")
_TsIDRightDeviceName_Type = DisplayString
_TsIDRightDeviceName_Object = MibTableColumn
tsIDRightDeviceName = _TsIDRightDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 25, 1, 1),
    _TsIDRightDeviceName_Type()
)
tsIDRightDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsIDRightDeviceName.setStatus("current")
_TsIDRightDeviceIP_Type = DisplayString
_TsIDRightDeviceIP_Object = MibTableColumn
tsIDRightDeviceIP = _TsIDRightDeviceIP_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 25, 1, 2),
    _TsIDRightDeviceIP_Type()
)
tsIDRightDeviceIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsIDRightDeviceIP.setStatus("current")
_TsIDRightTSID_Type = DisplayString
_TsIDRightTSID_Object = MibTableColumn
tsIDRightTSID = _TsIDRightTSID_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 25, 1, 3),
    _TsIDRightTSID_Type()
)
tsIDRightTSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsIDRightTSID.setStatus("current")
_TsIDRightLevel_Type = DisplayString
_TsIDRightLevel_Object = MibTableColumn
tsIDRightLevel = _TsIDRightLevel_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 25, 1, 4),
    _TsIDRightLevel_Type()
)
tsIDRightLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsIDRightLevel.setStatus("current")
_TsIDRightTriggerTime_Type = DisplayString
_TsIDRightTriggerTime_Object = MibTableColumn
tsIDRightTriggerTime = _TsIDRightTriggerTime_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 25, 1, 5),
    _TsIDRightTriggerTime_Type()
)
tsIDRightTriggerTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsIDRightTriggerTime.setStatus("current")
_TsIDRightDescription_Type = DisplayString
_TsIDRightDescription_Object = MibTableColumn
tsIDRightDescription = _TsIDRightDescription_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 25, 1, 6),
    _TsIDRightDescription_Type()
)
tsIDRightDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsIDRightDescription.setStatus("current")
_TsIDRightSlot_Type = DisplayString
_TsIDRightSlot_Object = MibTableColumn
tsIDRightSlot = _TsIDRightSlot_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 25, 1, 7),
    _TsIDRightSlot_Type()
)
tsIDRightSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsIDRightSlot.setStatus("current")
_TrapTSBitRateNormalTable_Object = MibTable
trapTSBitRateNormalTable = _TrapTSBitRateNormalTable_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 26)
)
if mibBuilder.loadTexts:
    trapTSBitRateNormalTable.setStatus("current")
_TrapTSBitRateNormalEntry_Object = MibTableRow
trapTSBitRateNormalEntry = _TrapTSBitRateNormalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 26, 1)
)
trapTSBitRateNormalEntry.setIndexNames(
    (0, "PBI-MGSYSTEM-MIB", "tsBitRateNormalDeviceName"),
)
if mibBuilder.loadTexts:
    trapTSBitRateNormalEntry.setStatus("current")
_TsBitRateNormalDeviceName_Type = DisplayString
_TsBitRateNormalDeviceName_Object = MibTableColumn
tsBitRateNormalDeviceName = _TsBitRateNormalDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 26, 1, 1),
    _TsBitRateNormalDeviceName_Type()
)
tsBitRateNormalDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsBitRateNormalDeviceName.setStatus("current")
_TsBitRateNormalDeviceIP_Type = DisplayString
_TsBitRateNormalDeviceIP_Object = MibTableColumn
tsBitRateNormalDeviceIP = _TsBitRateNormalDeviceIP_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 26, 1, 2),
    _TsBitRateNormalDeviceIP_Type()
)
tsBitRateNormalDeviceIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsBitRateNormalDeviceIP.setStatus("current")
_TsBitRateNormalChannel_Type = DisplayString
_TsBitRateNormalChannel_Object = MibTableColumn
tsBitRateNormalChannel = _TsBitRateNormalChannel_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 26, 1, 3),
    _TsBitRateNormalChannel_Type()
)
tsBitRateNormalChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsBitRateNormalChannel.setStatus("current")
_TsBitRateNormalLevel_Type = DisplayString
_TsBitRateNormalLevel_Object = MibTableColumn
tsBitRateNormalLevel = _TsBitRateNormalLevel_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 26, 1, 4),
    _TsBitRateNormalLevel_Type()
)
tsBitRateNormalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsBitRateNormalLevel.setStatus("current")
_TsBitRateNormalTriggerTime_Type = DisplayString
_TsBitRateNormalTriggerTime_Object = MibTableColumn
tsBitRateNormalTriggerTime = _TsBitRateNormalTriggerTime_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 26, 1, 5),
    _TsBitRateNormalTriggerTime_Type()
)
tsBitRateNormalTriggerTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsBitRateNormalTriggerTime.setStatus("current")
_TsBitRateNormalDescription_Type = DisplayString
_TsBitRateNormalDescription_Object = MibTableColumn
tsBitRateNormalDescription = _TsBitRateNormalDescription_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 26, 1, 6),
    _TsBitRateNormalDescription_Type()
)
tsBitRateNormalDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsBitRateNormalDescription.setStatus("current")
_TsBitRateNormalSlot_Type = DisplayString
_TsBitRateNormalSlot_Object = MibTableColumn
tsBitRateNormalSlot = _TsBitRateNormalSlot_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 26, 1, 7),
    _TsBitRateNormalSlot_Type()
)
tsBitRateNormalSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsBitRateNormalSlot.setStatus("current")
_VirtualGroupInfo_Type = DisplayString
_VirtualGroupInfo_Object = MibScalar
virtualGroupInfo = _VirtualGroupInfo_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 27),
    _VirtualGroupInfo_Type()
)
virtualGroupInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    virtualGroupInfo.setStatus("current")
_ModuleNumber_Type = Integer32
_ModuleNumber_Object = MibScalar
moduleNumber = _ModuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 28),
    _ModuleNumber_Type()
)
moduleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleNumber.setStatus("current")
_ChestTemp_Type = Integer32
_ChestTemp_Object = MibScalar
chestTemp = _ChestTemp_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 29),
    _ChestTemp_Type()
)
chestTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chestTemp.setStatus("current")


class _LcdSwitch_Type(Integer32):
    """Custom type lcdSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alwaysOn", 0),
          ("time", 1))
    )


_LcdSwitch_Type.__name__ = "Integer32"
_LcdSwitch_Object = MibScalar
lcdSwitch = _LcdSwitch_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 1, 1, 35),
    _LcdSwitch_Type()
)
lcdSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcdSwitch.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PBI-MGSYSTEM-MIB",
    **{"mgSystem": mgSystem,
       "basicInfo": basicInfo,
       "unitName": unitName,
       "serialNumber": serialNumber,
       "fpgaVersion": fpgaVersion,
       "mcuVersion": mcuVersion,
       "macAddress": macAddress,
       "gateway": gateway,
       "deviceIP": deviceIP,
       "subnetMask": subnetMask,
       "trapIpAddress": trapIpAddress,
       "upgrade": upgrade,
       "upgradeIP": upgradeIP,
       "default": default,
       "deviceType": deviceType,
       "hardwareVersion": hardwareVersion,
       "externdBoard": externdBoard,
       "trapDeviceOffTable": trapDeviceOffTable,
       "trapDeviceOffEntry": trapDeviceOffEntry,
       "deviceOffDeviceName": deviceOffDeviceName,
       "deviceOffDeviceIP": deviceOffDeviceIP,
       "deviceOffReserve": deviceOffReserve,
       "deviceOffLevel": deviceOffLevel,
       "deviceOffTriggerTime": deviceOffTriggerTime,
       "deviceOffDescription": deviceOffDescription,
       "trapDeviceOnTable": trapDeviceOnTable,
       "trapDeviceOnEntry": trapDeviceOnEntry,
       "deviceOnDeviceName": deviceOnDeviceName,
       "deviceOnDeviceIP": deviceOnDeviceIP,
       "deviceOnReserve": deviceOnReserve,
       "deviceOnLevel": deviceOnLevel,
       "deviceOnTriggerTime": deviceOnTriggerTime,
       "deviceOnDescription": deviceOnDescription,
       "trapFanFailedTable": trapFanFailedTable,
       "trapFanFailedEntry": trapFanFailedEntry,
       "fanFailedDeviceName": fanFailedDeviceName,
       "fanFailedDeviceIP": fanFailedDeviceIP,
       "fanFailedReserve": fanFailedReserve,
       "fanFailedLevel": fanFailedLevel,
       "fanFailedTriggerTime": fanFailedTriggerTime,
       "fanFailedDescription": fanFailedDescription,
       "trapSignalOffTable": trapSignalOffTable,
       "trapSignalOffEntry": trapSignalOffEntry,
       "signalOffDeviceName": signalOffDeviceName,
       "signalOffDeviceIP": signalOffDeviceIP,
       "signalOffChannel": signalOffChannel,
       "signalOffLevel": signalOffLevel,
       "signalOffTriggerTime": signalOffTriggerTime,
       "signalOffDescription": signalOffDescription,
       "signalOffSlot": signalOffSlot,
       "trapSignalOnTable": trapSignalOnTable,
       "trapSignalOnEntry": trapSignalOnEntry,
       "signalOnDeviceName": signalOnDeviceName,
       "signalOnDeviceIP": signalOnDeviceIP,
       "signalOnChannel": signalOnChannel,
       "signalOnLevel": signalOnLevel,
       "signalOnTriggerTime": signalOnTriggerTime,
       "signalOnDescription": signalOnDescription,
       "signalOnSlot": signalOnSlot,
       "trapSignalChangeTable": trapSignalChangeTable,
       "trapSignalChangeEntry": trapSignalChangeEntry,
       "signalChangeDeviceName": signalChangeDeviceName,
       "signalChangeDeviceIP": signalChangeDeviceIP,
       "signalChangeChannel": signalChangeChannel,
       "signalChangeLevel": signalChangeLevel,
       "signalChangeTriggerTime": signalChangeTriggerTime,
       "signalChangeDescription": signalChangeDescription,
       "signalChangeSlot": signalChangeSlot,
       "trapTSOverflowTable": trapTSOverflowTable,
       "trapTSOverflowEntry": trapTSOverflowEntry,
       "tsOverflowDeviceName": tsOverflowDeviceName,
       "tsOverflowDeviceIP": tsOverflowDeviceIP,
       "tsOverflowChannel": tsOverflowChannel,
       "tsOverflowLevel": tsOverflowLevel,
       "tsOverflowTriggerTime": tsOverflowTriggerTime,
       "tsOverflowDescription": tsOverflowDescription,
       "tsOverflowSlot": tsOverflowSlot,
       "rebootCommand": rebootCommand,
       "trapTSIDErrorTable": trapTSIDErrorTable,
       "trapTSIDErrorEntry": trapTSIDErrorEntry,
       "tsIDErrorDeviceName": tsIDErrorDeviceName,
       "tsIDErrorDeviceIP": tsIDErrorDeviceIP,
       "tsIDErrorTsID": tsIDErrorTsID,
       "tsIDErrorLevel": tsIDErrorLevel,
       "tsIDErrorTriggerTime": tsIDErrorTriggerTime,
       "tsIDErrorDescription": tsIDErrorDescription,
       "tsIDErrorSlot": tsIDErrorSlot,
       "trapTSIDRightTable": trapTSIDRightTable,
       "trapTSIDRightEntry": trapTSIDRightEntry,
       "tsIDRightDeviceName": tsIDRightDeviceName,
       "tsIDRightDeviceIP": tsIDRightDeviceIP,
       "tsIDRightTSID": tsIDRightTSID,
       "tsIDRightLevel": tsIDRightLevel,
       "tsIDRightTriggerTime": tsIDRightTriggerTime,
       "tsIDRightDescription": tsIDRightDescription,
       "tsIDRightSlot": tsIDRightSlot,
       "trapTSBitRateNormalTable": trapTSBitRateNormalTable,
       "trapTSBitRateNormalEntry": trapTSBitRateNormalEntry,
       "tsBitRateNormalDeviceName": tsBitRateNormalDeviceName,
       "tsBitRateNormalDeviceIP": tsBitRateNormalDeviceIP,
       "tsBitRateNormalChannel": tsBitRateNormalChannel,
       "tsBitRateNormalLevel": tsBitRateNormalLevel,
       "tsBitRateNormalTriggerTime": tsBitRateNormalTriggerTime,
       "tsBitRateNormalDescription": tsBitRateNormalDescription,
       "tsBitRateNormalSlot": tsBitRateNormalSlot,
       "virtualGroupInfo": virtualGroupInfo,
       "moduleNumber": moduleNumber,
       "chestTemp": chestTemp,
       "lcdSwitch": lcdSwitch}
)
