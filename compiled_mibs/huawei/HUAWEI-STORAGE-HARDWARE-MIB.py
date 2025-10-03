# SNMP MIB module (HUAWEI-STORAGE-HARDWARE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\huawei\HUAWEI-STORAGE-HARDWARE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:58:43 2025
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

hwStorage = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 34774, 4)
)
if mibBuilder.loadTexts:
    hwStorage.setRevisions(
        ("2014-04-06 13:54",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class NodeCodeString(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 17),
    )



# MIB Managed Objects in the order of their OIDs

_Huaweistorage_ObjectIdentity = ObjectIdentity
huaweistorage = _Huaweistorage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34774)
)
_HwISM_ObjectIdentity = ObjectIdentity
hwISM = _HwISM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1)
)
_HwStorageDevice_ObjectIdentity = ObjectIdentity
hwStorageDevice = _HwStorageDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23)
)
_HwHardwareInfo_ObjectIdentity = ObjectIdentity
hwHardwareInfo = _HwHardwareInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5)
)
_HwInfoDiskTable_Object = MibTable
hwInfoDiskTable = _HwInfoDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 1)
)
if mibBuilder.loadTexts:
    hwInfoDiskTable.setStatus("current")
_HwInfoDiskEntry_Object = MibTableRow
hwInfoDiskEntry = _HwInfoDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 1, 1)
)
hwInfoDiskEntry.setIndexNames(
    (0, "HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoDiskID"),
)
if mibBuilder.loadTexts:
    hwInfoDiskEntry.setStatus("current")
_HwInfoDiskID_Type = OctetString
_HwInfoDiskID_Object = MibTableColumn
hwInfoDiskID = _HwInfoDiskID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 1, 1, 1),
    _HwInfoDiskID_Type()
)
hwInfoDiskID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoDiskID.setStatus("current")
_HwInfoDiskHealthStatus_Type = Unsigned32
_HwInfoDiskHealthStatus_Object = MibTableColumn
hwInfoDiskHealthStatus = _HwInfoDiskHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 1, 1, 2),
    _HwInfoDiskHealthStatus_Type()
)
hwInfoDiskHealthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoDiskHealthStatus.setStatus("current")
_HwInfoDiskRunningStatus_Type = Unsigned32
_HwInfoDiskRunningStatus_Object = MibTableColumn
hwInfoDiskRunningStatus = _HwInfoDiskRunningStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 1, 1, 3),
    _HwInfoDiskRunningStatus_Type()
)
hwInfoDiskRunningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoDiskRunningStatus.setStatus("current")
_HwInfoDiskLocation_Type = OctetString
_HwInfoDiskLocation_Object = MibTableColumn
hwInfoDiskLocation = _HwInfoDiskLocation_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 1, 1, 4),
    _HwInfoDiskLocation_Type()
)
hwInfoDiskLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoDiskLocation.setStatus("current")
_HwInfoDiskType_Type = Unsigned32
_HwInfoDiskType_Object = MibTableColumn
hwInfoDiskType = _HwInfoDiskType_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 1, 1, 5),
    _HwInfoDiskType_Type()
)
hwInfoDiskType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoDiskType.setStatus("current")
_HwInfoDiskCapacity_Type = Counter64
_HwInfoDiskCapacity_Object = MibTableColumn
hwInfoDiskCapacity = _HwInfoDiskCapacity_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 1, 1, 6),
    _HwInfoDiskCapacity_Type()
)
hwInfoDiskCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoDiskCapacity.setStatus("current")
_HwInfoDiskRole_Type = Unsigned32
_HwInfoDiskRole_Object = MibTableColumn
hwInfoDiskRole = _HwInfoDiskRole_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 1, 1, 7),
    _HwInfoDiskRole_Type()
)
hwInfoDiskRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoDiskRole.setStatus("current")
_HwInfoDiskSpeed_Type = Unsigned32
_HwInfoDiskSpeed_Object = MibTableColumn
hwInfoDiskSpeed = _HwInfoDiskSpeed_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 1, 1, 8),
    _HwInfoDiskSpeed_Type()
)
hwInfoDiskSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoDiskSpeed.setStatus("current")
_HwInfoDiskInterfaceBandwidth_Type = Unsigned32
_HwInfoDiskInterfaceBandwidth_Object = MibTableColumn
hwInfoDiskInterfaceBandwidth = _HwInfoDiskInterfaceBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 1, 1, 9),
    _HwInfoDiskInterfaceBandwidth_Type()
)
hwInfoDiskInterfaceBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoDiskInterfaceBandwidth.setStatus("current")
_HwInfoDiskSectorSize_Type = Unsigned32
_HwInfoDiskSectorSize_Object = MibTableColumn
hwInfoDiskSectorSize = _HwInfoDiskSectorSize_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 1, 1, 10),
    _HwInfoDiskSectorSize_Type()
)
hwInfoDiskSectorSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoDiskSectorSize.setStatus("current")
_HwInfoDiskTemperature_Type = Integer32
_HwInfoDiskTemperature_Object = MibTableColumn
hwInfoDiskTemperature = _HwInfoDiskTemperature_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 1, 1, 11),
    _HwInfoDiskTemperature_Type()
)
hwInfoDiskTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoDiskTemperature.setStatus("current")
_HwInfoDiskModel_Type = OctetString
_HwInfoDiskModel_Object = MibTableColumn
hwInfoDiskModel = _HwInfoDiskModel_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 1, 1, 12),
    _HwInfoDiskModel_Type()
)
hwInfoDiskModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoDiskModel.setStatus("current")
_HwInfoDiskFirmwareVersion_Type = OctetString
_HwInfoDiskFirmwareVersion_Object = MibTableColumn
hwInfoDiskFirmwareVersion = _HwInfoDiskFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 1, 1, 13),
    _HwInfoDiskFirmwareVersion_Type()
)
hwInfoDiskFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoDiskFirmwareVersion.setStatus("current")
_HwInfoDiskManufacturer_Type = OctetString
_HwInfoDiskManufacturer_Object = MibTableColumn
hwInfoDiskManufacturer = _HwInfoDiskManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 1, 1, 14),
    _HwInfoDiskManufacturer_Type()
)
hwInfoDiskManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoDiskManufacturer.setStatus("current")
_HwInfoDiskSerialNumber_Type = OctetString
_HwInfoDiskSerialNumber_Object = MibTableColumn
hwInfoDiskSerialNumber = _HwInfoDiskSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 1, 1, 15),
    _HwInfoDiskSerialNumber_Type()
)
hwInfoDiskSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoDiskSerialNumber.setStatus("current")
_HwInfoDiskLightStatus_Type = Unsigned32
_HwInfoDiskLightStatus_Object = MibTableColumn
hwInfoDiskLightStatus = _HwInfoDiskLightStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 1, 1, 16),
    _HwInfoDiskLightStatus_Type()
)
hwInfoDiskLightStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoDiskLightStatus.setStatus("current")
_HwInfoDiskDiskDomainID_Type = OctetString
_HwInfoDiskDiskDomainID_Object = MibTableColumn
hwInfoDiskDiskDomainID = _HwInfoDiskDiskDomainID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 1, 1, 17),
    _HwInfoDiskDiskDomainID_Type()
)
hwInfoDiskDiskDomainID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoDiskDiskDomainID.setStatus("current")
_HwInfoDiskDiskDomainName_Type = OctetString
_HwInfoDiskDiskDomainName_Object = MibTableColumn
hwInfoDiskDiskDomainName = _HwInfoDiskDiskDomainName_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 1, 1, 18),
    _HwInfoDiskDiskDomainName_Type()
)
hwInfoDiskDiskDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoDiskDiskDomainName.setStatus("current")
_HwInfoDiskDiskDomainTierID_Type = OctetString
_HwInfoDiskDiskDomainTierID_Object = MibTableColumn
hwInfoDiskDiskDomainTierID = _HwInfoDiskDiskDomainTierID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 1, 1, 19),
    _HwInfoDiskDiskDomainTierID_Type()
)
hwInfoDiskDiskDomainTierID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoDiskDiskDomainTierID.setStatus("current")
_HwInfoDiskCofferDisk_Type = Unsigned32
_HwInfoDiskCofferDisk_Object = MibTableColumn
hwInfoDiskCofferDisk = _HwInfoDiskCofferDisk_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 1, 1, 20),
    _HwInfoDiskCofferDisk_Type()
)
hwInfoDiskCofferDisk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoDiskCofferDisk.setStatus("current")
_HwInfoDiskRunTime_Type = Unsigned32
_HwInfoDiskRunTime_Object = MibTableColumn
hwInfoDiskRunTime = _HwInfoDiskRunTime_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 1, 1, 21),
    _HwInfoDiskRunTime_Type()
)
hwInfoDiskRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoDiskRunTime.setStatus("current")
_HwInfoDiskProgress_Type = Unsigned32
_HwInfoDiskProgress_Object = MibTableColumn
hwInfoDiskProgress = _HwInfoDiskProgress_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 1, 1, 22),
    _HwInfoDiskProgress_Type()
)
hwInfoDiskProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoDiskProgress.setStatus("current")
_HwInfoDiskBarCode_Type = OctetString
_HwInfoDiskBarCode_Object = MibTableColumn
hwInfoDiskBarCode = _HwInfoDiskBarCode_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 1, 1, 23),
    _HwInfoDiskBarCode_Type()
)
hwInfoDiskBarCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoDiskBarCode.setStatus("current")
_HwInfoDiskCapacityUsage_Type = Unsigned32
_HwInfoDiskCapacityUsage_Object = MibTableColumn
hwInfoDiskCapacityUsage = _HwInfoDiskCapacityUsage_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 1, 1, 24),
    _HwInfoDiskCapacityUsage_Type()
)
hwInfoDiskCapacityUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoDiskCapacityUsage.setStatus("current")
_HwInfoDiskHealthMark_Type = Unsigned32
_HwInfoDiskHealthMark_Object = MibTableColumn
hwInfoDiskHealthMark = _HwInfoDiskHealthMark_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 1, 1, 25),
    _HwInfoDiskHealthMark_Type()
)
hwInfoDiskHealthMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoDiskHealthMark.setStatus("current")
_HwInfoControllerTable_Object = MibTable
hwInfoControllerTable = _HwInfoControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 2)
)
if mibBuilder.loadTexts:
    hwInfoControllerTable.setStatus("current")
_HwInfoControllerEntry_Object = MibTableRow
hwInfoControllerEntry = _HwInfoControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 2, 1)
)
hwInfoControllerEntry.setIndexNames(
    (0, "HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoControllerID"),
)
if mibBuilder.loadTexts:
    hwInfoControllerEntry.setStatus("current")
_HwInfoControllerID_Type = OctetString
_HwInfoControllerID_Object = MibTableColumn
hwInfoControllerID = _HwInfoControllerID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 2, 1, 1),
    _HwInfoControllerID_Type()
)
hwInfoControllerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoControllerID.setStatus("current")
_HwInfoControllerHealthStatus_Type = Unsigned32
_HwInfoControllerHealthStatus_Object = MibTableColumn
hwInfoControllerHealthStatus = _HwInfoControllerHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 2, 1, 2),
    _HwInfoControllerHealthStatus_Type()
)
hwInfoControllerHealthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoControllerHealthStatus.setStatus("current")
_HwInfoControllerRunningStatus_Type = Unsigned32
_HwInfoControllerRunningStatus_Object = MibTableColumn
hwInfoControllerRunningStatus = _HwInfoControllerRunningStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 2, 1, 3),
    _HwInfoControllerRunningStatus_Type()
)
hwInfoControllerRunningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoControllerRunningStatus.setStatus("current")
_HwInfoControllerCPU_Type = OctetString
_HwInfoControllerCPU_Object = MibTableColumn
hwInfoControllerCPU = _HwInfoControllerCPU_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 2, 1, 4),
    _HwInfoControllerCPU_Type()
)
hwInfoControllerCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoControllerCPU.setStatus("current")
_HwInfoControllerLocation_Type = OctetString
_HwInfoControllerLocation_Object = MibTableColumn
hwInfoControllerLocation = _HwInfoControllerLocation_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 2, 1, 5),
    _HwInfoControllerLocation_Type()
)
hwInfoControllerLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoControllerLocation.setStatus("current")
_HwInfoControllerRole_Type = Unsigned32
_HwInfoControllerRole_Object = MibTableColumn
hwInfoControllerRole = _HwInfoControllerRole_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 2, 1, 6),
    _HwInfoControllerRole_Type()
)
hwInfoControllerRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoControllerRole.setStatus("current")
_HwInfoControllerCacheCapacity_Type = Unsigned32
_HwInfoControllerCacheCapacity_Object = MibTableColumn
hwInfoControllerCacheCapacity = _HwInfoControllerCacheCapacity_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 2, 1, 7),
    _HwInfoControllerCacheCapacity_Type()
)
hwInfoControllerCacheCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoControllerCacheCapacity.setStatus("current")
_HwInfoControllerCPUUsage_Type = Unsigned32
_HwInfoControllerCPUUsage_Object = MibTableColumn
hwInfoControllerCPUUsage = _HwInfoControllerCPUUsage_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 2, 1, 8),
    _HwInfoControllerCPUUsage_Type()
)
hwInfoControllerCPUUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoControllerCPUUsage.setStatus("current")
_HwInfoControllerMemoryUsage_Type = Unsigned32
_HwInfoControllerMemoryUsage_Object = MibTableColumn
hwInfoControllerMemoryUsage = _HwInfoControllerMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 2, 1, 9),
    _HwInfoControllerMemoryUsage_Type()
)
hwInfoControllerMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoControllerMemoryUsage.setStatus("current")
_HwInfoControllerVoltage_Type = Unsigned32
_HwInfoControllerVoltage_Object = MibTableColumn
hwInfoControllerVoltage = _HwInfoControllerVoltage_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 2, 1, 10),
    _HwInfoControllerVoltage_Type()
)
hwInfoControllerVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoControllerVoltage.setStatus("current")
_HwInfoControllerSoftwareVersion_Type = OctetString
_HwInfoControllerSoftwareVersion_Object = MibTableColumn
hwInfoControllerSoftwareVersion = _HwInfoControllerSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 2, 1, 11),
    _HwInfoControllerSoftwareVersion_Type()
)
hwInfoControllerSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoControllerSoftwareVersion.setStatus("current")
_HwInfoControllerPCBVersion_Type = OctetString
_HwInfoControllerPCBVersion_Object = MibTableColumn
hwInfoControllerPCBVersion = _HwInfoControllerPCBVersion_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 2, 1, 12),
    _HwInfoControllerPCBVersion_Type()
)
hwInfoControllerPCBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoControllerPCBVersion.setStatus("current")
_HwInfoControllerSESVersion_Type = OctetString
_HwInfoControllerSESVersion_Object = MibTableColumn
hwInfoControllerSESVersion = _HwInfoControllerSESVersion_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 2, 1, 13),
    _HwInfoControllerSESVersion_Type()
)
hwInfoControllerSESVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoControllerSESVersion.setStatus("current")
_HwInfoControllerBMCVersion_Type = OctetString
_HwInfoControllerBMCVersion_Object = MibTableColumn
hwInfoControllerBMCVersion = _HwInfoControllerBMCVersion_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 2, 1, 14),
    _HwInfoControllerBMCVersion_Type()
)
hwInfoControllerBMCVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoControllerBMCVersion.setStatus("current")
_HwInfoControllerLogicVersion_Type = OctetString
_HwInfoControllerLogicVersion_Object = MibTableColumn
hwInfoControllerLogicVersion = _HwInfoControllerLogicVersion_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 2, 1, 15),
    _HwInfoControllerLogicVersion_Type()
)
hwInfoControllerLogicVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoControllerLogicVersion.setStatus("current")
_HwInfoControllerBIOSVersion_Type = OctetString
_HwInfoControllerBIOSVersion_Object = MibTableColumn
hwInfoControllerBIOSVersion = _HwInfoControllerBIOSVersion_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 2, 1, 16),
    _HwInfoControllerBIOSVersion_Type()
)
hwInfoControllerBIOSVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoControllerBIOSVersion.setStatus("current")
_HwInfoControllerElectronicLabel_Type = OctetString
_HwInfoControllerElectronicLabel_Object = MibTableColumn
hwInfoControllerElectronicLabel = _HwInfoControllerElectronicLabel_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 2, 1, 17),
    _HwInfoControllerElectronicLabel_Type()
)
hwInfoControllerElectronicLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoControllerElectronicLabel.setStatus("current")
_HwInfoPowerTable_Object = MibTable
hwInfoPowerTable = _HwInfoPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 3)
)
if mibBuilder.loadTexts:
    hwInfoPowerTable.setStatus("current")
_HwInfoPowerEntry_Object = MibTableRow
hwInfoPowerEntry = _HwInfoPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 3, 1)
)
hwInfoPowerEntry.setIndexNames(
    (0, "HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPowerID"),
)
if mibBuilder.loadTexts:
    hwInfoPowerEntry.setStatus("current")
_HwInfoPowerID_Type = OctetString
_HwInfoPowerID_Object = MibTableColumn
hwInfoPowerID = _HwInfoPowerID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 3, 1, 1),
    _HwInfoPowerID_Type()
)
hwInfoPowerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPowerID.setStatus("current")
_HwInfoPowerLocation_Type = OctetString
_HwInfoPowerLocation_Object = MibTableColumn
hwInfoPowerLocation = _HwInfoPowerLocation_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 3, 1, 2),
    _HwInfoPowerLocation_Type()
)
hwInfoPowerLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPowerLocation.setStatus("current")
_HwInfoPowerHealthStatus_Type = Unsigned32
_HwInfoPowerHealthStatus_Object = MibTableColumn
hwInfoPowerHealthStatus = _HwInfoPowerHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 3, 1, 3),
    _HwInfoPowerHealthStatus_Type()
)
hwInfoPowerHealthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPowerHealthStatus.setStatus("current")
_HwInfoPowerRunningStatus_Type = Unsigned32
_HwInfoPowerRunningStatus_Object = MibTableColumn
hwInfoPowerRunningStatus = _HwInfoPowerRunningStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 3, 1, 4),
    _HwInfoPowerRunningStatus_Type()
)
hwInfoPowerRunningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPowerRunningStatus.setStatus("current")
_HwInfoPowerType_Type = Unsigned32
_HwInfoPowerType_Object = MibTableColumn
hwInfoPowerType = _HwInfoPowerType_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 3, 1, 5),
    _HwInfoPowerType_Type()
)
hwInfoPowerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPowerType.setStatus("current")
_HwInfoPowerManufacturer_Type = OctetString
_HwInfoPowerManufacturer_Object = MibTableColumn
hwInfoPowerManufacturer = _HwInfoPowerManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 3, 1, 6),
    _HwInfoPowerManufacturer_Type()
)
hwInfoPowerManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPowerManufacturer.setStatus("current")
_HwInfoPowerModle_Type = OctetString
_HwInfoPowerModle_Object = MibTableColumn
hwInfoPowerModle = _HwInfoPowerModle_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 3, 1, 7),
    _HwInfoPowerModle_Type()
)
hwInfoPowerModle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPowerModle.setStatus("current")
_HwInfoPowerVersion_Type = OctetString
_HwInfoPowerVersion_Object = MibTableColumn
hwInfoPowerVersion = _HwInfoPowerVersion_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 3, 1, 8),
    _HwInfoPowerVersion_Type()
)
hwInfoPowerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPowerVersion.setStatus("current")
_HwInfoPowerProduceDate_Type = OctetString
_HwInfoPowerProduceDate_Object = MibTableColumn
hwInfoPowerProduceDate = _HwInfoPowerProduceDate_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 3, 1, 9),
    _HwInfoPowerProduceDate_Type()
)
hwInfoPowerProduceDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPowerProduceDate.setStatus("current")
_HwInfoPowerSerialNumber_Type = OctetString
_HwInfoPowerSerialNumber_Object = MibTableColumn
hwInfoPowerSerialNumber = _HwInfoPowerSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 3, 1, 10),
    _HwInfoPowerSerialNumber_Type()
)
hwInfoPowerSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPowerSerialNumber.setStatus("current")
_HwInfoFanTable_Object = MibTable
hwInfoFanTable = _HwInfoFanTable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 4)
)
if mibBuilder.loadTexts:
    hwInfoFanTable.setStatus("current")
_HwInfoFanEntry_Object = MibTableRow
hwInfoFanEntry = _HwInfoFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 4, 1)
)
hwInfoFanEntry.setIndexNames(
    (0, "HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoFanID"),
)
if mibBuilder.loadTexts:
    hwInfoFanEntry.setStatus("current")
_HwInfoFanID_Type = OctetString
_HwInfoFanID_Object = MibTableColumn
hwInfoFanID = _HwInfoFanID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 4, 1, 1),
    _HwInfoFanID_Type()
)
hwInfoFanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoFanID.setStatus("current")
_HwInfoFanLocation_Type = OctetString
_HwInfoFanLocation_Object = MibTableColumn
hwInfoFanLocation = _HwInfoFanLocation_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 4, 1, 2),
    _HwInfoFanLocation_Type()
)
hwInfoFanLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoFanLocation.setStatus("current")
_HwInfoFanHealthStatus_Type = Unsigned32
_HwInfoFanHealthStatus_Object = MibTableColumn
hwInfoFanHealthStatus = _HwInfoFanHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 4, 1, 3),
    _HwInfoFanHealthStatus_Type()
)
hwInfoFanHealthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoFanHealthStatus.setStatus("current")
_HwInfoFanRunningStatus_Type = Unsigned32
_HwInfoFanRunningStatus_Object = MibTableColumn
hwInfoFanRunningStatus = _HwInfoFanRunningStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 4, 1, 4),
    _HwInfoFanRunningStatus_Type()
)
hwInfoFanRunningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoFanRunningStatus.setStatus("current")
_HwInfoFanRunningLevel_Type = Unsigned32
_HwInfoFanRunningLevel_Object = MibTableColumn
hwInfoFanRunningLevel = _HwInfoFanRunningLevel_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 4, 1, 5),
    _HwInfoFanRunningLevel_Type()
)
hwInfoFanRunningLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoFanRunningLevel.setStatus("current")
_HwInfoFanElectronicLabel_Type = OctetString
_HwInfoFanElectronicLabel_Object = MibTableColumn
hwInfoFanElectronicLabel = _HwInfoFanElectronicLabel_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 4, 1, 6),
    _HwInfoFanElectronicLabel_Type()
)
hwInfoFanElectronicLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoFanElectronicLabel.setStatus("current")
_HwInfoBBUTable_Object = MibTable
hwInfoBBUTable = _HwInfoBBUTable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 5)
)
if mibBuilder.loadTexts:
    hwInfoBBUTable.setStatus("current")
_HwInfoBBUEntry_Object = MibTableRow
hwInfoBBUEntry = _HwInfoBBUEntry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 5, 1)
)
hwInfoBBUEntry.setIndexNames(
    (0, "HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoBBUID"),
)
if mibBuilder.loadTexts:
    hwInfoBBUEntry.setStatus("current")
_HwInfoBBUID_Type = OctetString
_HwInfoBBUID_Object = MibTableColumn
hwInfoBBUID = _HwInfoBBUID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 5, 1, 1),
    _HwInfoBBUID_Type()
)
hwInfoBBUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoBBUID.setStatus("current")
_HwInfoBBULocation_Type = OctetString
_HwInfoBBULocation_Object = MibTableColumn
hwInfoBBULocation = _HwInfoBBULocation_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 5, 1, 2),
    _HwInfoBBULocation_Type()
)
hwInfoBBULocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoBBULocation.setStatus("current")
_HwInfoBBUHealthStatus_Type = Unsigned32
_HwInfoBBUHealthStatus_Object = MibTableColumn
hwInfoBBUHealthStatus = _HwInfoBBUHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 5, 1, 3),
    _HwInfoBBUHealthStatus_Type()
)
hwInfoBBUHealthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoBBUHealthStatus.setStatus("current")
_HwInfoBBURunningStatus_Type = Unsigned32
_HwInfoBBURunningStatus_Object = MibTableColumn
hwInfoBBURunningStatus = _HwInfoBBURunningStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 5, 1, 4),
    _HwInfoBBURunningStatus_Type()
)
hwInfoBBURunningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoBBURunningStatus.setStatus("current")
_HwInfoBBUType_Type = Unsigned32
_HwInfoBBUType_Object = MibTableColumn
hwInfoBBUType = _HwInfoBBUType_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 5, 1, 5),
    _HwInfoBBUType_Type()
)
hwInfoBBUType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoBBUType.setStatus("current")
_HwInfoBBUCurrentVoltage_Type = Unsigned32
_HwInfoBBUCurrentVoltage_Object = MibTableColumn
hwInfoBBUCurrentVoltage = _HwInfoBBUCurrentVoltage_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 5, 1, 6),
    _HwInfoBBUCurrentVoltage_Type()
)
hwInfoBBUCurrentVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoBBUCurrentVoltage.setStatus("current")
_HwInfoBBUNumberOfDischarges_Type = Unsigned32
_HwInfoBBUNumberOfDischarges_Object = MibTableColumn
hwInfoBBUNumberOfDischarges = _HwInfoBBUNumberOfDischarges_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 5, 1, 7),
    _HwInfoBBUNumberOfDischarges_Type()
)
hwInfoBBUNumberOfDischarges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoBBUNumberOfDischarges.setStatus("current")
_HwInfoBBUFirmwareVersion_Type = OctetString
_HwInfoBBUFirmwareVersion_Object = MibTableColumn
hwInfoBBUFirmwareVersion = _HwInfoBBUFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 5, 1, 8),
    _HwInfoBBUFirmwareVersion_Type()
)
hwInfoBBUFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoBBUFirmwareVersion.setStatus("current")
_HwInfoBBUDeliveredOn_Type = OctetString
_HwInfoBBUDeliveredOn_Object = MibTableColumn
hwInfoBBUDeliveredOn = _HwInfoBBUDeliveredOn_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 5, 1, 9),
    _HwInfoBBUDeliveredOn_Type()
)
hwInfoBBUDeliveredOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoBBUDeliveredOn.setStatus("current")
_HwInfoBBUOwningController_Type = OctetString
_HwInfoBBUOwningController_Object = MibTableColumn
hwInfoBBUOwningController = _HwInfoBBUOwningController_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 5, 1, 10),
    _HwInfoBBUOwningController_Type()
)
hwInfoBBUOwningController.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoBBUOwningController.setStatus("current")
_HwInfoBBUElectronicLabel_Type = OctetString
_HwInfoBBUElectronicLabel_Object = MibTableColumn
hwInfoBBUElectronicLabel = _HwInfoBBUElectronicLabel_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 5, 1, 11),
    _HwInfoBBUElectronicLabel_Type()
)
hwInfoBBUElectronicLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoBBUElectronicLabel.setStatus("current")
_HwInfoEnclosureTable_Object = MibTable
hwInfoEnclosureTable = _HwInfoEnclosureTable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 6)
)
if mibBuilder.loadTexts:
    hwInfoEnclosureTable.setStatus("current")
_HwInfoEnclosureEntry_Object = MibTableRow
hwInfoEnclosureEntry = _HwInfoEnclosureEntry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 6, 1)
)
hwInfoEnclosureEntry.setIndexNames(
    (0, "HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoEnclosureID"),
)
if mibBuilder.loadTexts:
    hwInfoEnclosureEntry.setStatus("current")
_HwInfoEnclosureID_Type = OctetString
_HwInfoEnclosureID_Object = MibTableColumn
hwInfoEnclosureID = _HwInfoEnclosureID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 6, 1, 1),
    _HwInfoEnclosureID_Type()
)
hwInfoEnclosureID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoEnclosureID.setStatus("current")
_HwInfoEnclosureName_Type = OctetString
_HwInfoEnclosureName_Object = MibTableColumn
hwInfoEnclosureName = _HwInfoEnclosureName_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 6, 1, 2),
    _HwInfoEnclosureName_Type()
)
hwInfoEnclosureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoEnclosureName.setStatus("current")
_HwInfoEnclosureLogicType_Type = Unsigned32
_HwInfoEnclosureLogicType_Object = MibTableColumn
hwInfoEnclosureLogicType = _HwInfoEnclosureLogicType_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 6, 1, 3),
    _HwInfoEnclosureLogicType_Type()
)
hwInfoEnclosureLogicType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoEnclosureLogicType.setStatus("current")
_HwInfoEnclosureHealthStatus_Type = Unsigned32
_HwInfoEnclosureHealthStatus_Object = MibTableColumn
hwInfoEnclosureHealthStatus = _HwInfoEnclosureHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 6, 1, 4),
    _HwInfoEnclosureHealthStatus_Type()
)
hwInfoEnclosureHealthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoEnclosureHealthStatus.setStatus("current")
_HwInfoEnclosureRunningStatus_Type = Unsigned32
_HwInfoEnclosureRunningStatus_Object = MibTableColumn
hwInfoEnclosureRunningStatus = _HwInfoEnclosureRunningStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 6, 1, 5),
    _HwInfoEnclosureRunningStatus_Type()
)
hwInfoEnclosureRunningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoEnclosureRunningStatus.setStatus("current")
_HwInfoEnclosureLocation_Type = OctetString
_HwInfoEnclosureLocation_Object = MibTableColumn
hwInfoEnclosureLocation = _HwInfoEnclosureLocation_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 6, 1, 6),
    _HwInfoEnclosureLocation_Type()
)
hwInfoEnclosureLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoEnclosureLocation.setStatus("current")
_HwInfoEnclosureType_Type = Unsigned32
_HwInfoEnclosureType_Object = MibTableColumn
hwInfoEnclosureType = _HwInfoEnclosureType_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 6, 1, 7),
    _HwInfoEnclosureType_Type()
)
hwInfoEnclosureType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoEnclosureType.setStatus("current")
_HwInfoEnclosureTemperature_Type = Integer32
_HwInfoEnclosureTemperature_Object = MibTableColumn
hwInfoEnclosureTemperature = _HwInfoEnclosureTemperature_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 6, 1, 8),
    _HwInfoEnclosureTemperature_Type()
)
hwInfoEnclosureTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoEnclosureTemperature.setStatus("current")
_HwInfoEnclosureSN_Type = OctetString
_HwInfoEnclosureSN_Object = MibTableColumn
hwInfoEnclosureSN = _HwInfoEnclosureSN_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 6, 1, 9),
    _HwInfoEnclosureSN_Type()
)
hwInfoEnclosureSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoEnclosureSN.setStatus("current")
_HwInfoEnclosureMAC_Type = OctetString
_HwInfoEnclosureMAC_Object = MibTableColumn
hwInfoEnclosureMAC = _HwInfoEnclosureMAC_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 6, 1, 10),
    _HwInfoEnclosureMAC_Type()
)
hwInfoEnclosureMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoEnclosureMAC.setStatus("current")
_HwInfoEnclosureHeight_Type = Unsigned32
_HwInfoEnclosureHeight_Object = MibTableColumn
hwInfoEnclosureHeight = _HwInfoEnclosureHeight_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 6, 1, 11),
    _HwInfoEnclosureHeight_Type()
)
hwInfoEnclosureHeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoEnclosureHeight.setStatus("current")
_HwInfoEnclosureExpansionDepth_Type = Unsigned32
_HwInfoEnclosureExpansionDepth_Object = MibTableColumn
hwInfoEnclosureExpansionDepth = _HwInfoEnclosureExpansionDepth_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 6, 1, 12),
    _HwInfoEnclosureExpansionDepth_Type()
)
hwInfoEnclosureExpansionDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoEnclosureExpansionDepth.setStatus("current")
_HwInfoEnclosureElectronicLabel_Type = OctetString
_HwInfoEnclosureElectronicLabel_Object = MibTableColumn
hwInfoEnclosureElectronicLabel = _HwInfoEnclosureElectronicLabel_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 6, 1, 13),
    _HwInfoEnclosureElectronicLabel_Type()
)
hwInfoEnclosureElectronicLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoEnclosureElectronicLabel.setStatus("current")
_HwInfoPortComTable_Object = MibTable
hwInfoPortComTable = _HwInfoPortComTable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 7)
)
if mibBuilder.loadTexts:
    hwInfoPortComTable.setStatus("current")
_HwInfoPortComEntry_Object = MibTableRow
hwInfoPortComEntry = _HwInfoPortComEntry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 7, 1)
)
hwInfoPortComEntry.setIndexNames(
    (0, "HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortComID"),
)
if mibBuilder.loadTexts:
    hwInfoPortComEntry.setStatus("current")
_HwInfoPortComID_Type = OctetString
_HwInfoPortComID_Object = MibTableColumn
hwInfoPortComID = _HwInfoPortComID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 7, 1, 1),
    _HwInfoPortComID_Type()
)
hwInfoPortComID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortComID.setStatus("current")
_HwInfoPortComLocation_Type = OctetString
_HwInfoPortComLocation_Object = MibTableColumn
hwInfoPortComLocation = _HwInfoPortComLocation_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 7, 1, 2),
    _HwInfoPortComLocation_Type()
)
hwInfoPortComLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortComLocation.setStatus("current")
_HwInfoPortComHealthStatus_Type = Unsigned32
_HwInfoPortComHealthStatus_Object = MibTableColumn
hwInfoPortComHealthStatus = _HwInfoPortComHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 7, 1, 3),
    _HwInfoPortComHealthStatus_Type()
)
hwInfoPortComHealthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortComHealthStatus.setStatus("current")
_HwInfoPortComRunningStatus_Type = Unsigned32
_HwInfoPortComRunningStatus_Object = MibTableColumn
hwInfoPortComRunningStatus = _HwInfoPortComRunningStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 7, 1, 4),
    _HwInfoPortComRunningStatus_Type()
)
hwInfoPortComRunningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortComRunningStatus.setStatus("current")
_HwInfoPortComType_Type = Unsigned32
_HwInfoPortComType_Object = MibTableColumn
hwInfoPortComType = _HwInfoPortComType_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 7, 1, 5),
    _HwInfoPortComType_Type()
)
hwInfoPortComType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortComType.setStatus("current")
_HwInfoPortEthTable_Object = MibTable
hwInfoPortEthTable = _HwInfoPortEthTable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 8)
)
if mibBuilder.loadTexts:
    hwInfoPortEthTable.setStatus("current")
_HwInfoPortEthEntry_Object = MibTableRow
hwInfoPortEthEntry = _HwInfoPortEthEntry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 8, 1)
)
hwInfoPortEthEntry.setIndexNames(
    (0, "HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortEthID"),
)
if mibBuilder.loadTexts:
    hwInfoPortEthEntry.setStatus("current")
_HwInfoPortEthID_Type = OctetString
_HwInfoPortEthID_Object = MibTableColumn
hwInfoPortEthID = _HwInfoPortEthID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 8, 1, 1),
    _HwInfoPortEthID_Type()
)
hwInfoPortEthID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortEthID.setStatus("current")
_HwInfoPortEthLocation_Type = OctetString
_HwInfoPortEthLocation_Object = MibTableColumn
hwInfoPortEthLocation = _HwInfoPortEthLocation_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 8, 1, 2),
    _HwInfoPortEthLocation_Type()
)
hwInfoPortEthLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortEthLocation.setStatus("current")
_HwInfoPortEthHealthStatus_Type = Unsigned32
_HwInfoPortEthHealthStatus_Object = MibTableColumn
hwInfoPortEthHealthStatus = _HwInfoPortEthHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 8, 1, 3),
    _HwInfoPortEthHealthStatus_Type()
)
hwInfoPortEthHealthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortEthHealthStatus.setStatus("current")
_HwInfoPortEthRunningStatus_Type = Unsigned32
_HwInfoPortEthRunningStatus_Object = MibTableColumn
hwInfoPortEthRunningStatus = _HwInfoPortEthRunningStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 8, 1, 4),
    _HwInfoPortEthRunningStatus_Type()
)
hwInfoPortEthRunningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortEthRunningStatus.setStatus("current")
_HwInfoPortEthType_Type = Unsigned32
_HwInfoPortEthType_Object = MibTableColumn
hwInfoPortEthType = _HwInfoPortEthType_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 8, 1, 5),
    _HwInfoPortEthType_Type()
)
hwInfoPortEthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortEthType.setStatus("current")
_HwInfoPortEthIPv4Address_Type = OctetString
_HwInfoPortEthIPv4Address_Object = MibTableColumn
hwInfoPortEthIPv4Address = _HwInfoPortEthIPv4Address_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 8, 1, 6),
    _HwInfoPortEthIPv4Address_Type()
)
hwInfoPortEthIPv4Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortEthIPv4Address.setStatus("current")
_HwInfoPortEthSubnetMask_Type = OctetString
_HwInfoPortEthSubnetMask_Object = MibTableColumn
hwInfoPortEthSubnetMask = _HwInfoPortEthSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 8, 1, 7),
    _HwInfoPortEthSubnetMask_Type()
)
hwInfoPortEthSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortEthSubnetMask.setStatus("current")
_HwInfoPortEthIPv4Gateway_Type = OctetString
_HwInfoPortEthIPv4Gateway_Object = MibTableColumn
hwInfoPortEthIPv4Gateway = _HwInfoPortEthIPv4Gateway_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 8, 1, 8),
    _HwInfoPortEthIPv4Gateway_Type()
)
hwInfoPortEthIPv4Gateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortEthIPv4Gateway.setStatus("current")
_HwInfoPortEthIPv6Address_Type = OctetString
_HwInfoPortEthIPv6Address_Object = MibTableColumn
hwInfoPortEthIPv6Address = _HwInfoPortEthIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 8, 1, 9),
    _HwInfoPortEthIPv6Address_Type()
)
hwInfoPortEthIPv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortEthIPv6Address.setStatus("current")
_HwInfoPortEthIPv6PrefixLength_Type = OctetString
_HwInfoPortEthIPv6PrefixLength_Object = MibTableColumn
hwInfoPortEthIPv6PrefixLength = _HwInfoPortEthIPv6PrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 8, 1, 10),
    _HwInfoPortEthIPv6PrefixLength_Type()
)
hwInfoPortEthIPv6PrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortEthIPv6PrefixLength.setStatus("current")
_HwInfoPortEthIPv6Gateway_Type = OctetString
_HwInfoPortEthIPv6Gateway_Object = MibTableColumn
hwInfoPortEthIPv6Gateway = _HwInfoPortEthIPv6Gateway_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 8, 1, 11),
    _HwInfoPortEthIPv6Gateway_Type()
)
hwInfoPortEthIPv6Gateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortEthIPv6Gateway.setStatus("current")
_HwInfoPortEthMAC_Type = OctetString
_HwInfoPortEthMAC_Object = MibTableColumn
hwInfoPortEthMAC = _HwInfoPortEthMAC_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 8, 1, 12),
    _HwInfoPortEthMAC_Type()
)
hwInfoPortEthMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortEthMAC.setStatus("current")
_HwInfoPortEthRole_Type = Unsigned32
_HwInfoPortEthRole_Object = MibTableColumn
hwInfoPortEthRole = _HwInfoPortEthRole_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 8, 1, 13),
    _HwInfoPortEthRole_Type()
)
hwInfoPortEthRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortEthRole.setStatus("current")
_HwInfoPortEthMode_Type = Unsigned32
_HwInfoPortEthMode_Object = MibTableColumn
hwInfoPortEthMode = _HwInfoPortEthMode_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 8, 1, 14),
    _HwInfoPortEthMode_Type()
)
hwInfoPortEthMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortEthMode.setStatus("current")
_HwInfoPortEthMTU_Type = Unsigned32
_HwInfoPortEthMTU_Object = MibTableColumn
hwInfoPortEthMTU = _HwInfoPortEthMTU_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 8, 1, 15),
    _HwInfoPortEthMTU_Type()
)
hwInfoPortEthMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortEthMTU.setStatus("current")
_HwInfoPortEthWorkingRate_Type = Unsigned32
_HwInfoPortEthWorkingRate_Object = MibTableColumn
hwInfoPortEthWorkingRate = _HwInfoPortEthWorkingRate_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 8, 1, 16),
    _HwInfoPortEthWorkingRate_Type()
)
hwInfoPortEthWorkingRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortEthWorkingRate.setStatus("current")
_HwInfoPortEthBondName_Type = OctetString
_HwInfoPortEthBondName_Object = MibTableColumn
hwInfoPortEthBondName = _HwInfoPortEthBondName_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 8, 1, 17),
    _HwInfoPortEthBondName_Type()
)
hwInfoPortEthBondName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortEthBondName.setStatus("current")
_HwInfoPortEthiSCSIPort_Type = OctetString
_HwInfoPortEthiSCSIPort_Object = MibTableColumn
hwInfoPortEthiSCSIPort = _HwInfoPortEthiSCSIPort_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 8, 1, 18),
    _HwInfoPortEthiSCSIPort_Type()
)
hwInfoPortEthiSCSIPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortEthiSCSIPort.setStatus("current")
_HwInfoPortEthiSCSIName_Type = OctetString
_HwInfoPortEthiSCSIName_Object = MibTableColumn
hwInfoPortEthiSCSIName = _HwInfoPortEthiSCSIName_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 8, 1, 19),
    _HwInfoPortEthiSCSIName_Type()
)
hwInfoPortEthiSCSIName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortEthiSCSIName.setStatus("current")
_HwInfoPortEthErrorPackets_Type = Unsigned32
_HwInfoPortEthErrorPackets_Object = MibTableColumn
hwInfoPortEthErrorPackets = _HwInfoPortEthErrorPackets_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 8, 1, 20),
    _HwInfoPortEthErrorPackets_Type()
)
hwInfoPortEthErrorPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortEthErrorPackets.setStatus("current")
_HwInfoPortEthLostPackages_Type = Unsigned32
_HwInfoPortEthLostPackages_Object = MibTableColumn
hwInfoPortEthLostPackages = _HwInfoPortEthLostPackages_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 8, 1, 21),
    _HwInfoPortEthLostPackages_Type()
)
hwInfoPortEthLostPackages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortEthLostPackages.setStatus("current")
_HwInfoPortEthStartTime_Type = OctetString
_HwInfoPortEthStartTime_Object = MibTableColumn
hwInfoPortEthStartTime = _HwInfoPortEthStartTime_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 8, 1, 22),
    _HwInfoPortEthStartTime_Type()
)
hwInfoPortEthStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortEthStartTime.setStatus("current")
_HwInfoPortFCTable_Object = MibTable
hwInfoPortFCTable = _HwInfoPortFCTable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 9)
)
if mibBuilder.loadTexts:
    hwInfoPortFCTable.setStatus("current")
_HwInfoPortFCEntry_Object = MibTableRow
hwInfoPortFCEntry = _HwInfoPortFCEntry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 9, 1)
)
hwInfoPortFCEntry.setIndexNames(
    (0, "HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortFCID"),
)
if mibBuilder.loadTexts:
    hwInfoPortFCEntry.setStatus("current")
_HwInfoPortFCID_Type = OctetString
_HwInfoPortFCID_Object = MibTableColumn
hwInfoPortFCID = _HwInfoPortFCID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 9, 1, 1),
    _HwInfoPortFCID_Type()
)
hwInfoPortFCID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortFCID.setStatus("current")
_HwInfoPortFCLocation_Type = OctetString
_HwInfoPortFCLocation_Object = MibTableColumn
hwInfoPortFCLocation = _HwInfoPortFCLocation_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 9, 1, 2),
    _HwInfoPortFCLocation_Type()
)
hwInfoPortFCLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortFCLocation.setStatus("current")
_HwInfoPortFCHealthStatus_Type = Unsigned32
_HwInfoPortFCHealthStatus_Object = MibTableColumn
hwInfoPortFCHealthStatus = _HwInfoPortFCHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 9, 1, 3),
    _HwInfoPortFCHealthStatus_Type()
)
hwInfoPortFCHealthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortFCHealthStatus.setStatus("current")
_HwInfoPortFCRunningStatus_Type = Unsigned32
_HwInfoPortFCRunningStatus_Object = MibTableColumn
hwInfoPortFCRunningStatus = _HwInfoPortFCRunningStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 9, 1, 4),
    _HwInfoPortFCRunningStatus_Type()
)
hwInfoPortFCRunningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortFCRunningStatus.setStatus("current")
_HwInfoPortFCType_Type = Unsigned32
_HwInfoPortFCType_Object = MibTableColumn
hwInfoPortFCType = _HwInfoPortFCType_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 9, 1, 5),
    _HwInfoPortFCType_Type()
)
hwInfoPortFCType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortFCType.setStatus("current")
_HwInfoPortFCWorkingRate_Type = Unsigned32
_HwInfoPortFCWorkingRate_Object = MibTableColumn
hwInfoPortFCWorkingRate = _HwInfoPortFCWorkingRate_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 9, 1, 6),
    _HwInfoPortFCWorkingRate_Type()
)
hwInfoPortFCWorkingRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortFCWorkingRate.setStatus("current")
_HwInfoPortFCConfiguredSpeed_Type = Unsigned32
_HwInfoPortFCConfiguredSpeed_Object = MibTableColumn
hwInfoPortFCConfiguredSpeed = _HwInfoPortFCConfiguredSpeed_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 9, 1, 7),
    _HwInfoPortFCConfiguredSpeed_Type()
)
hwInfoPortFCConfiguredSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortFCConfiguredSpeed.setStatus("current")
_HwInfoPortFCWWN_Type = OctetString
_HwInfoPortFCWWN_Object = MibTableColumn
hwInfoPortFCWWN = _HwInfoPortFCWWN_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 9, 1, 8),
    _HwInfoPortFCWWN_Type()
)
hwInfoPortFCWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortFCWWN.setStatus("current")
_HwInfoPortFCRole_Type = Unsigned32
_HwInfoPortFCRole_Object = MibTableColumn
hwInfoPortFCRole = _HwInfoPortFCRole_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 9, 1, 9),
    _HwInfoPortFCRole_Type()
)
hwInfoPortFCRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortFCRole.setStatus("current")
_HwInfoPortFCSFPStatus_Type = Unsigned32
_HwInfoPortFCSFPStatus_Object = MibTableColumn
hwInfoPortFCSFPStatus = _HwInfoPortFCSFPStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 9, 1, 10),
    _HwInfoPortFCSFPStatus_Type()
)
hwInfoPortFCSFPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortFCSFPStatus.setStatus("current")
_HwInfoPortFCWorkingMode_Type = Unsigned32
_HwInfoPortFCWorkingMode_Object = MibTableColumn
hwInfoPortFCWorkingMode = _HwInfoPortFCWorkingMode_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 9, 1, 11),
    _HwInfoPortFCWorkingMode_Type()
)
hwInfoPortFCWorkingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortFCWorkingMode.setStatus("current")
_HwInfoPortFCConfiguredMode_Type = Unsigned32
_HwInfoPortFCConfiguredMode_Object = MibTableColumn
hwInfoPortFCConfiguredMode = _HwInfoPortFCConfiguredMode_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 9, 1, 12),
    _HwInfoPortFCConfiguredMode_Type()
)
hwInfoPortFCConfiguredMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortFCConfiguredMode.setStatus("current")
_HwInfoPortFCFloginDelayTimes_Type = Unsigned32
_HwInfoPortFCFloginDelayTimes_Object = MibTableColumn
hwInfoPortFCFloginDelayTimes = _HwInfoPortFCFloginDelayTimes_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 9, 1, 13),
    _HwInfoPortFCFloginDelayTimes_Type()
)
hwInfoPortFCFloginDelayTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortFCFloginDelayTimes.setStatus("current")
_HwInfoPortFCLostSignals_Type = Unsigned32
_HwInfoPortFCLostSignals_Object = MibTableColumn
hwInfoPortFCLostSignals = _HwInfoPortFCLostSignals_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 9, 1, 14),
    _HwInfoPortFCLostSignals_Type()
)
hwInfoPortFCLostSignals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortFCLostSignals.setStatus("current")
_HwInfoPortFCLinkErrorsCodes_Type = Unsigned32
_HwInfoPortFCLinkErrorsCodes_Object = MibTableColumn
hwInfoPortFCLinkErrorsCodes = _HwInfoPortFCLinkErrorsCodes_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 9, 1, 15),
    _HwInfoPortFCLinkErrorsCodes_Type()
)
hwInfoPortFCLinkErrorsCodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortFCLinkErrorsCodes.setStatus("current")
_HwInfoPortFCLostSynchronizations_Type = Unsigned32
_HwInfoPortFCLostSynchronizations_Object = MibTableColumn
hwInfoPortFCLostSynchronizations = _HwInfoPortFCLostSynchronizations_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 9, 1, 16),
    _HwInfoPortFCLostSynchronizations_Type()
)
hwInfoPortFCLostSynchronizations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortFCLostSynchronizations.setStatus("current")
_HwInfoPortFCFailedConnections_Type = Unsigned32
_HwInfoPortFCFailedConnections_Object = MibTableColumn
hwInfoPortFCFailedConnections = _HwInfoPortFCFailedConnections_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 9, 1, 17),
    _HwInfoPortFCFailedConnections_Type()
)
hwInfoPortFCFailedConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortFCFailedConnections.setStatus("current")
_HwInfoPortFCStartTime_Type = OctetString
_HwInfoPortFCStartTime_Object = MibTableColumn
hwInfoPortFCStartTime = _HwInfoPortFCStartTime_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 9, 1, 18),
    _HwInfoPortFCStartTime_Type()
)
hwInfoPortFCStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortFCStartTime.setStatus("current")
_HwInfoPortFCoETable_Object = MibTable
hwInfoPortFCoETable = _HwInfoPortFCoETable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 10)
)
if mibBuilder.loadTexts:
    hwInfoPortFCoETable.setStatus("current")
_HwInfoPortFCoEEntry_Object = MibTableRow
hwInfoPortFCoEEntry = _HwInfoPortFCoEEntry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 10, 1)
)
hwInfoPortFCoEEntry.setIndexNames(
    (0, "HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortFCoEID"),
)
if mibBuilder.loadTexts:
    hwInfoPortFCoEEntry.setStatus("current")
_HwInfoPortFCoEID_Type = OctetString
_HwInfoPortFCoEID_Object = MibTableColumn
hwInfoPortFCoEID = _HwInfoPortFCoEID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 10, 1, 1),
    _HwInfoPortFCoEID_Type()
)
hwInfoPortFCoEID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortFCoEID.setStatus("current")
_HwInfoPortFCoELocation_Type = OctetString
_HwInfoPortFCoELocation_Object = MibTableColumn
hwInfoPortFCoELocation = _HwInfoPortFCoELocation_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 10, 1, 2),
    _HwInfoPortFCoELocation_Type()
)
hwInfoPortFCoELocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortFCoELocation.setStatus("current")
_HwInfoPortFCoEHealthStatus_Type = Unsigned32
_HwInfoPortFCoEHealthStatus_Object = MibTableColumn
hwInfoPortFCoEHealthStatus = _HwInfoPortFCoEHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 10, 1, 3),
    _HwInfoPortFCoEHealthStatus_Type()
)
hwInfoPortFCoEHealthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortFCoEHealthStatus.setStatus("current")
_HwInfoPortFCoERunningStatus_Type = Unsigned32
_HwInfoPortFCoERunningStatus_Object = MibTableColumn
hwInfoPortFCoERunningStatus = _HwInfoPortFCoERunningStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 10, 1, 4),
    _HwInfoPortFCoERunningStatus_Type()
)
hwInfoPortFCoERunningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortFCoERunningStatus.setStatus("current")
_HwInfoPortFCoEType_Type = Unsigned32
_HwInfoPortFCoEType_Object = MibTableColumn
hwInfoPortFCoEType = _HwInfoPortFCoEType_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 10, 1, 5),
    _HwInfoPortFCoEType_Type()
)
hwInfoPortFCoEType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortFCoEType.setStatus("current")
_HwInfoPortFCoEWorkingRate_Type = Unsigned32
_HwInfoPortFCoEWorkingRate_Object = MibTableColumn
hwInfoPortFCoEWorkingRate = _HwInfoPortFCoEWorkingRate_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 10, 1, 6),
    _HwInfoPortFCoEWorkingRate_Type()
)
hwInfoPortFCoEWorkingRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortFCoEWorkingRate.setStatus("current")
_HwInfoPortFCoEWWN_Type = OctetString
_HwInfoPortFCoEWWN_Object = MibTableColumn
hwInfoPortFCoEWWN = _HwInfoPortFCoEWWN_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 10, 1, 7),
    _HwInfoPortFCoEWWN_Type()
)
hwInfoPortFCoEWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortFCoEWWN.setStatus("current")
_HwInfoPortFCoERole_Type = Unsigned32
_HwInfoPortFCoERole_Object = MibTableColumn
hwInfoPortFCoERole = _HwInfoPortFCoERole_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 10, 1, 8),
    _HwInfoPortFCoERole_Type()
)
hwInfoPortFCoERole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortFCoERole.setStatus("current")
_HwInfoPortFCoESFPStatus_Type = Unsigned32
_HwInfoPortFCoESFPStatus_Object = MibTableColumn
hwInfoPortFCoESFPStatus = _HwInfoPortFCoESFPStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 10, 1, 9),
    _HwInfoPortFCoESFPStatus_Type()
)
hwInfoPortFCoESFPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortFCoESFPStatus.setStatus("current")
_HwInfoPortFCoEErrorPackets_Type = Unsigned32
_HwInfoPortFCoEErrorPackets_Object = MibTableColumn
hwInfoPortFCoEErrorPackets = _HwInfoPortFCoEErrorPackets_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 10, 1, 10),
    _HwInfoPortFCoEErrorPackets_Type()
)
hwInfoPortFCoEErrorPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortFCoEErrorPackets.setStatus("current")
_HwInfoPortFCoELostPackets_Type = Unsigned32
_HwInfoPortFCoELostPackets_Object = MibTableColumn
hwInfoPortFCoELostPackets = _HwInfoPortFCoELostPackets_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 10, 1, 11),
    _HwInfoPortFCoELostPackets_Type()
)
hwInfoPortFCoELostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortFCoELostPackets.setStatus("current")
_HwInfoPortFCoEOverFlowedPackets_Type = Unsigned32
_HwInfoPortFCoEOverFlowedPackets_Object = MibTableColumn
hwInfoPortFCoEOverFlowedPackets = _HwInfoPortFCoEOverFlowedPackets_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 10, 1, 12),
    _HwInfoPortFCoEOverFlowedPackets_Type()
)
hwInfoPortFCoEOverFlowedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortFCoEOverFlowedPackets.setStatus("current")
_HwInfoPortFCoEStartTime_Type = OctetString
_HwInfoPortFCoEStartTime_Object = MibTableColumn
hwInfoPortFCoEStartTime = _HwInfoPortFCoEStartTime_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 10, 1, 13),
    _HwInfoPortFCoEStartTime_Type()
)
hwInfoPortFCoEStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortFCoEStartTime.setStatus("current")
_HwInfoPortPCIETable_Object = MibTable
hwInfoPortPCIETable = _HwInfoPortPCIETable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 11)
)
if mibBuilder.loadTexts:
    hwInfoPortPCIETable.setStatus("current")
_HwInfoPortPCIEEntry_Object = MibTableRow
hwInfoPortPCIEEntry = _HwInfoPortPCIEEntry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 11, 1)
)
hwInfoPortPCIEEntry.setIndexNames(
    (0, "HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortPCIEID"),
)
if mibBuilder.loadTexts:
    hwInfoPortPCIEEntry.setStatus("current")
_HwInfoPortPCIEID_Type = OctetString
_HwInfoPortPCIEID_Object = MibTableColumn
hwInfoPortPCIEID = _HwInfoPortPCIEID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 11, 1, 1),
    _HwInfoPortPCIEID_Type()
)
hwInfoPortPCIEID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortPCIEID.setStatus("current")
_HwInfoPortPCIELocation_Type = OctetString
_HwInfoPortPCIELocation_Object = MibTableColumn
hwInfoPortPCIELocation = _HwInfoPortPCIELocation_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 11, 1, 2),
    _HwInfoPortPCIELocation_Type()
)
hwInfoPortPCIELocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortPCIELocation.setStatus("current")
_HwInfoPortPCIEHealthStatus_Type = Unsigned32
_HwInfoPortPCIEHealthStatus_Object = MibTableColumn
hwInfoPortPCIEHealthStatus = _HwInfoPortPCIEHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 11, 1, 3),
    _HwInfoPortPCIEHealthStatus_Type()
)
hwInfoPortPCIEHealthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortPCIEHealthStatus.setStatus("current")
_HwInfoPortPCIERunningStatus_Type = Unsigned32
_HwInfoPortPCIERunningStatus_Object = MibTableColumn
hwInfoPortPCIERunningStatus = _HwInfoPortPCIERunningStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 11, 1, 4),
    _HwInfoPortPCIERunningStatus_Type()
)
hwInfoPortPCIERunningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortPCIERunningStatus.setStatus("current")
_HwInfoPortPCIESpeed_Type = Unsigned32
_HwInfoPortPCIESpeed_Object = MibTableColumn
hwInfoPortPCIESpeed = _HwInfoPortPCIESpeed_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 11, 1, 5),
    _HwInfoPortPCIESpeed_Type()
)
hwInfoPortPCIESpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortPCIESpeed.setStatus("current")
_HwInfoPortPCIECurrentPeerPortID_Type = OctetString
_HwInfoPortPCIECurrentPeerPortID_Object = MibTableColumn
hwInfoPortPCIECurrentPeerPortID = _HwInfoPortPCIECurrentPeerPortID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 11, 1, 6),
    _HwInfoPortPCIECurrentPeerPortID_Type()
)
hwInfoPortPCIECurrentPeerPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortPCIECurrentPeerPortID.setStatus("current")
_HwInfoPortPCIESuggestPeerPortID_Type = OctetString
_HwInfoPortPCIESuggestPeerPortID_Object = MibTableColumn
hwInfoPortPCIESuggestPeerPortID = _HwInfoPortPCIESuggestPeerPortID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 11, 1, 7),
    _HwInfoPortPCIESuggestPeerPortID_Type()
)
hwInfoPortPCIESuggestPeerPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortPCIESuggestPeerPortID.setStatus("current")
_HwInfoPortPCIELostSignals_Type = Unsigned32
_HwInfoPortPCIELostSignals_Object = MibTableColumn
hwInfoPortPCIELostSignals = _HwInfoPortPCIELostSignals_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 11, 1, 8),
    _HwInfoPortPCIELostSignals_Type()
)
hwInfoPortPCIELostSignals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortPCIELostSignals.setStatus("current")
_HwInfoPortPCIEECRCError_Type = Unsigned32
_HwInfoPortPCIEECRCError_Object = MibTableColumn
hwInfoPortPCIEECRCError = _HwInfoPortPCIEECRCError_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 11, 1, 9),
    _HwInfoPortPCIEECRCError_Type()
)
hwInfoPortPCIEECRCError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortPCIEECRCError.setStatus("current")
_HwInfoPortPCIEBadTlp_Type = Unsigned32
_HwInfoPortPCIEBadTlp_Object = MibTableColumn
hwInfoPortPCIEBadTlp = _HwInfoPortPCIEBadTlp_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 11, 1, 10),
    _HwInfoPortPCIEBadTlp_Type()
)
hwInfoPortPCIEBadTlp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortPCIEBadTlp.setStatus("current")
_HwInfoPortPCIEBalDllp_Type = Unsigned32
_HwInfoPortPCIEBalDllp_Object = MibTableColumn
hwInfoPortPCIEBalDllp = _HwInfoPortPCIEBalDllp_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 11, 1, 11),
    _HwInfoPortPCIEBalDllp_Type()
)
hwInfoPortPCIEBalDllp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortPCIEBalDllp.setStatus("current")
_HwInfoPortPCIERecvError_Type = Unsigned32
_HwInfoPortPCIERecvError_Object = MibTableColumn
hwInfoPortPCIERecvError = _HwInfoPortPCIERecvError_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 11, 1, 12),
    _HwInfoPortPCIERecvError_Type()
)
hwInfoPortPCIERecvError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortPCIERecvError.setStatus("current")
_HwInfoPortPCIEChipEccError_Type = Unsigned32
_HwInfoPortPCIEChipEccError_Object = MibTableColumn
hwInfoPortPCIEChipEccError = _HwInfoPortPCIEChipEccError_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 11, 1, 13),
    _HwInfoPortPCIEChipEccError_Type()
)
hwInfoPortPCIEChipEccError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortPCIEChipEccError.setStatus("current")
_HwInfoPortPCIEStartTime_Type = OctetString
_HwInfoPortPCIEStartTime_Object = MibTableColumn
hwInfoPortPCIEStartTime = _HwInfoPortPCIEStartTime_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 11, 1, 14),
    _HwInfoPortPCIEStartTime_Type()
)
hwInfoPortPCIEStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortPCIEStartTime.setStatus("current")
_HwInfoPortSASTable_Object = MibTable
hwInfoPortSASTable = _HwInfoPortSASTable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 12)
)
if mibBuilder.loadTexts:
    hwInfoPortSASTable.setStatus("current")
_HwInfoPortSASEntry_Object = MibTableRow
hwInfoPortSASEntry = _HwInfoPortSASEntry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 12, 1)
)
hwInfoPortSASEntry.setIndexNames(
    (0, "HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortSASID"),
)
if mibBuilder.loadTexts:
    hwInfoPortSASEntry.setStatus("current")
_HwInfoPortSASID_Type = OctetString
_HwInfoPortSASID_Object = MibTableColumn
hwInfoPortSASID = _HwInfoPortSASID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 12, 1, 1),
    _HwInfoPortSASID_Type()
)
hwInfoPortSASID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortSASID.setStatus("current")
_HwInfoPortSASLocation_Type = OctetString
_HwInfoPortSASLocation_Object = MibTableColumn
hwInfoPortSASLocation = _HwInfoPortSASLocation_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 12, 1, 2),
    _HwInfoPortSASLocation_Type()
)
hwInfoPortSASLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortSASLocation.setStatus("current")
_HwInfoPortSASHealthStatus_Type = Unsigned32
_HwInfoPortSASHealthStatus_Object = MibTableColumn
hwInfoPortSASHealthStatus = _HwInfoPortSASHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 12, 1, 3),
    _HwInfoPortSASHealthStatus_Type()
)
hwInfoPortSASHealthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortSASHealthStatus.setStatus("current")
_HwInfoPortSASRunningStatus_Type = Unsigned32
_HwInfoPortSASRunningStatus_Object = MibTableColumn
hwInfoPortSASRunningStatus = _HwInfoPortSASRunningStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 12, 1, 4),
    _HwInfoPortSASRunningStatus_Type()
)
hwInfoPortSASRunningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortSASRunningStatus.setStatus("current")
_HwInfoPortSASType_Type = Unsigned32
_HwInfoPortSASType_Object = MibTableColumn
hwInfoPortSASType = _HwInfoPortSASType_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 12, 1, 5),
    _HwInfoPortSASType_Type()
)
hwInfoPortSASType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortSASType.setStatus("current")
_HwInfoPortSASWorkingRate_Type = Unsigned32
_HwInfoPortSASWorkingRate_Object = MibTableColumn
hwInfoPortSASWorkingRate = _HwInfoPortSASWorkingRate_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 12, 1, 6),
    _HwInfoPortSASWorkingRate_Type()
)
hwInfoPortSASWorkingRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortSASWorkingRate.setStatus("current")
_HwInfoPortSASWWN_Type = OctetString
_HwInfoPortSASWWN_Object = MibTableColumn
hwInfoPortSASWWN = _HwInfoPortSASWWN_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 12, 1, 7),
    _HwInfoPortSASWWN_Type()
)
hwInfoPortSASWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortSASWWN.setStatus("current")
_HwInfoPortSASRole_Type = Unsigned32
_HwInfoPortSASRole_Object = MibTableColumn
hwInfoPortSASRole = _HwInfoPortSASRole_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 12, 1, 8),
    _HwInfoPortSASRole_Type()
)
hwInfoPortSASRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortSASRole.setStatus("current")
_HwInfoPortSASInvalidDword_Type = Unsigned32
_HwInfoPortSASInvalidDword_Object = MibTableColumn
hwInfoPortSASInvalidDword = _HwInfoPortSASInvalidDword_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 12, 1, 9),
    _HwInfoPortSASInvalidDword_Type()
)
hwInfoPortSASInvalidDword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortSASInvalidDword.setStatus("current")
_HwInfoPortSASConsistErrors_Type = Unsigned32
_HwInfoPortSASConsistErrors_Object = MibTableColumn
hwInfoPortSASConsistErrors = _HwInfoPortSASConsistErrors_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 12, 1, 10),
    _HwInfoPortSASConsistErrors_Type()
)
hwInfoPortSASConsistErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortSASConsistErrors.setStatus("current")
_HwInfoPortSASLossOfDword_Type = Unsigned32
_HwInfoPortSASLossOfDword_Object = MibTableColumn
hwInfoPortSASLossOfDword = _HwInfoPortSASLossOfDword_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 12, 1, 11),
    _HwInfoPortSASLossOfDword_Type()
)
hwInfoPortSASLossOfDword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortSASLossOfDword.setStatus("current")
_HwInfoPortSASPHYResetErrors_Type = Unsigned32
_HwInfoPortSASPHYResetErrors_Object = MibTableColumn
hwInfoPortSASPHYResetErrors = _HwInfoPortSASPHYResetErrors_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 12, 1, 12),
    _HwInfoPortSASPHYResetErrors_Type()
)
hwInfoPortSASPHYResetErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortSASPHYResetErrors.setStatus("current")
_HwInfoPortSASStartTime_Type = OctetString
_HwInfoPortSASStartTime_Object = MibTableColumn
hwInfoPortSASStartTime = _HwInfoPortSASStartTime_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 12, 1, 13),
    _HwInfoPortSASStartTime_Type()
)
hwInfoPortSASStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortSASStartTime.setStatus("current")
_HwInfoPortSASEnabled_Type = Unsigned32
_HwInfoPortSASEnabled_Object = MibTableColumn
hwInfoPortSASEnabled = _HwInfoPortSASEnabled_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 12, 1, 14),
    _HwInfoPortSASEnabled_Type()
)
hwInfoPortSASEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortSASEnabled.setStatus("current")
_HwInfoInterfaceModuleTable_Object = MibTable
hwInfoInterfaceModuleTable = _HwInfoInterfaceModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 13)
)
if mibBuilder.loadTexts:
    hwInfoInterfaceModuleTable.setStatus("current")
_HwInfoInterfaceModuleEntry_Object = MibTableRow
hwInfoInterfaceModuleEntry = _HwInfoInterfaceModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 13, 1)
)
hwInfoInterfaceModuleEntry.setIndexNames(
    (0, "HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoInterfaceModuleID"),
)
if mibBuilder.loadTexts:
    hwInfoInterfaceModuleEntry.setStatus("current")
_HwInfoInterfaceModuleID_Type = OctetString
_HwInfoInterfaceModuleID_Object = MibTableColumn
hwInfoInterfaceModuleID = _HwInfoInterfaceModuleID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 13, 1, 1),
    _HwInfoInterfaceModuleID_Type()
)
hwInfoInterfaceModuleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoInterfaceModuleID.setStatus("current")
_HwInfoInterfaceModuleLocation_Type = OctetString
_HwInfoInterfaceModuleLocation_Object = MibTableColumn
hwInfoInterfaceModuleLocation = _HwInfoInterfaceModuleLocation_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 13, 1, 2),
    _HwInfoInterfaceModuleLocation_Type()
)
hwInfoInterfaceModuleLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoInterfaceModuleLocation.setStatus("current")
_HwInfoInterfaceModuleHealthStatus_Type = Unsigned32
_HwInfoInterfaceModuleHealthStatus_Object = MibTableColumn
hwInfoInterfaceModuleHealthStatus = _HwInfoInterfaceModuleHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 13, 1, 3),
    _HwInfoInterfaceModuleHealthStatus_Type()
)
hwInfoInterfaceModuleHealthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoInterfaceModuleHealthStatus.setStatus("current")
_HwInfoInterfaceModuleRunningStatus_Type = Unsigned32
_HwInfoInterfaceModuleRunningStatus_Object = MibTableColumn
hwInfoInterfaceModuleRunningStatus = _HwInfoInterfaceModuleRunningStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 13, 1, 4),
    _HwInfoInterfaceModuleRunningStatus_Type()
)
hwInfoInterfaceModuleRunningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoInterfaceModuleRunningStatus.setStatus("current")
_HwInfoInterfaceModuleModel_Type = Unsigned32
_HwInfoInterfaceModuleModel_Object = MibTableColumn
hwInfoInterfaceModuleModel = _HwInfoInterfaceModuleModel_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 13, 1, 5),
    _HwInfoInterfaceModuleModel_Type()
)
hwInfoInterfaceModuleModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoInterfaceModuleModel.setStatus("current")
_HwInfoInterfaceModuleLogicVersion_Type = OctetString
_HwInfoInterfaceModuleLogicVersion_Object = MibTableColumn
hwInfoInterfaceModuleLogicVersion = _HwInfoInterfaceModuleLogicVersion_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 13, 1, 6),
    _HwInfoInterfaceModuleLogicVersion_Type()
)
hwInfoInterfaceModuleLogicVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoInterfaceModuleLogicVersion.setStatus("current")
_HwInfoInterfaceModulePCBVersion_Type = OctetString
_HwInfoInterfaceModulePCBVersion_Object = MibTableColumn
hwInfoInterfaceModulePCBVersion = _HwInfoInterfaceModulePCBVersion_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 13, 1, 7),
    _HwInfoInterfaceModulePCBVersion_Type()
)
hwInfoInterfaceModulePCBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoInterfaceModulePCBVersion.setStatus("current")
_HwInfoInterfaceModuleElectronicLabel_Type = OctetString
_HwInfoInterfaceModuleElectronicLabel_Object = MibTableColumn
hwInfoInterfaceModuleElectronicLabel = _HwInfoInterfaceModuleElectronicLabel_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 13, 1, 8),
    _HwInfoInterfaceModuleElectronicLabel_Type()
)
hwInfoInterfaceModuleElectronicLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoInterfaceModuleElectronicLabel.setStatus("current")
_HwInfoExpBoardTable_Object = MibTable
hwInfoExpBoardTable = _HwInfoExpBoardTable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 14)
)
if mibBuilder.loadTexts:
    hwInfoExpBoardTable.setStatus("current")
_HwInfoExpBoardEntry_Object = MibTableRow
hwInfoExpBoardEntry = _HwInfoExpBoardEntry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 14, 1)
)
hwInfoExpBoardEntry.setIndexNames(
    (0, "HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoExpBoardID"),
)
if mibBuilder.loadTexts:
    hwInfoExpBoardEntry.setStatus("current")
_HwInfoExpBoardID_Type = OctetString
_HwInfoExpBoardID_Object = MibTableColumn
hwInfoExpBoardID = _HwInfoExpBoardID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 14, 1, 1),
    _HwInfoExpBoardID_Type()
)
hwInfoExpBoardID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoExpBoardID.setStatus("current")
_HwInfoExpBoardLocation_Type = OctetString
_HwInfoExpBoardLocation_Object = MibTableColumn
hwInfoExpBoardLocation = _HwInfoExpBoardLocation_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 14, 1, 2),
    _HwInfoExpBoardLocation_Type()
)
hwInfoExpBoardLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoExpBoardLocation.setStatus("current")
_HwInfoExpBoardHealthStatus_Type = Unsigned32
_HwInfoExpBoardHealthStatus_Object = MibTableColumn
hwInfoExpBoardHealthStatus = _HwInfoExpBoardHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 14, 1, 3),
    _HwInfoExpBoardHealthStatus_Type()
)
hwInfoExpBoardHealthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoExpBoardHealthStatus.setStatus("current")
_HwInfoExpBoardRunningStatus_Type = Unsigned32
_HwInfoExpBoardRunningStatus_Object = MibTableColumn
hwInfoExpBoardRunningStatus = _HwInfoExpBoardRunningStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 14, 1, 4),
    _HwInfoExpBoardRunningStatus_Type()
)
hwInfoExpBoardRunningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoExpBoardRunningStatus.setStatus("current")
_HwInfoExpBoardModel_Type = Unsigned32
_HwInfoExpBoardModel_Object = MibTableColumn
hwInfoExpBoardModel = _HwInfoExpBoardModel_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 14, 1, 5),
    _HwInfoExpBoardModel_Type()
)
hwInfoExpBoardModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoExpBoardModel.setStatus("current")
_HwInfoExpBoardLogicVersion_Type = OctetString
_HwInfoExpBoardLogicVersion_Object = MibTableColumn
hwInfoExpBoardLogicVersion = _HwInfoExpBoardLogicVersion_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 14, 1, 6),
    _HwInfoExpBoardLogicVersion_Type()
)
hwInfoExpBoardLogicVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoExpBoardLogicVersion.setStatus("current")
_HwInfoExpBoardPCBVersion_Type = OctetString
_HwInfoExpBoardPCBVersion_Object = MibTableColumn
hwInfoExpBoardPCBVersion = _HwInfoExpBoardPCBVersion_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 14, 1, 7),
    _HwInfoExpBoardPCBVersion_Type()
)
hwInfoExpBoardPCBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoExpBoardPCBVersion.setStatus("current")
_HwInfoExpBoardSESVersion_Type = OctetString
_HwInfoExpBoardSESVersion_Object = MibTableColumn
hwInfoExpBoardSESVersion = _HwInfoExpBoardSESVersion_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 14, 1, 8),
    _HwInfoExpBoardSESVersion_Type()
)
hwInfoExpBoardSESVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoExpBoardSESVersion.setStatus("current")
_HwInfoExpBoardELabel_Type = OctetString
_HwInfoExpBoardELabel_Object = MibTableColumn
hwInfoExpBoardELabel = _HwInfoExpBoardELabel_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 23, 5, 14, 1, 9),
    _HwInfoExpBoardELabel_Type()
)
hwInfoExpBoardELabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoExpBoardELabel.setStatus("current")
_IsoConformance_ObjectIdentity = ObjectIdentity
isoConformance = _IsoConformance_ObjectIdentity(
    (1, 6)
)
_IsoGroups_ObjectIdentity = ObjectIdentity
isoGroups = _IsoGroups_ObjectIdentity(
    (1, 6, 1)
)
_IsoCompliances_ObjectIdentity = ObjectIdentity
isoCompliances = _IsoCompliances_ObjectIdentity(
    (1, 6, 2)
)

# Managed Objects groups

currentObjectGroup = ObjectGroup(
    (1, 6, 1, 1)
)
currentObjectGroup.setObjects(
      *(("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortComID"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortComLocation"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortComHealthStatus"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortComRunningStatus"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortComType"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortEthID"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortEthLocation"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortEthHealthStatus"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortEthRunningStatus"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortEthType"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortEthIPv4Address"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortEthSubnetMask"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortEthIPv4Gateway"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortEthIPv6Address"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortEthIPv6PrefixLength"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortEthIPv6Gateway"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortEthMAC"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortEthRole"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortEthMode"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortEthMTU"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortEthWorkingRate"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortEthBondName"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortEthiSCSIPort"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortEthiSCSIName"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortEthErrorPackets"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortEthLostPackages"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortFCID"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortFCLocation"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortFCHealthStatus"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortFCRunningStatus"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortFCType"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortFCWorkingRate"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortFCConfiguredSpeed"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortFCWWN"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortFCRole"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortFCSFPStatus"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortFCWorkingMode"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortFCConfiguredMode"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortFCFloginDelayTimes"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortFCLostSignals"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortFCLinkErrorsCodes"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortFCLostSynchronizations"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortFCFailedConnections"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortFCoEID"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortFCoELocation"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortFCoEHealthStatus"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortFCoERunningStatus"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortFCoEType"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortFCoEWorkingRate"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortFCoEWWN"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortFCoERole"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortFCoESFPStatus"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortFCoEErrorPackets"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortFCoELostPackets"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortFCoEOverFlowedPackets"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortFCoEStartTime"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortPCIEID"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortPCIELocation"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortPCIEHealthStatus"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortPCIERunningStatus"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortPCIESpeed"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortPCIECurrentPeerPortID"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortPCIESuggestPeerPortID"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortPCIELostSignals"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortPCIEECRCError"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortPCIEBadTlp"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortPCIEBalDllp"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortPCIERecvError"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortPCIEChipEccError"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortSASID"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortSASLocation"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortSASHealthStatus"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortSASRunningStatus"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortSASType"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortSASWorkingRate"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortSASWWN"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortSASRole"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortSASInvalidDword"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortSASConsistErrors"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortSASLossOfDword"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortSASPHYResetErrors"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortSASStartTime"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortSASEnabled"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoInterfaceModuleID"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoInterfaceModuleLocation"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoInterfaceModuleHealthStatus"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoInterfaceModuleRunningStatus"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoInterfaceModuleModel"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoInterfaceModuleLogicVersion"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoInterfaceModulePCBVersion"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoInterfaceModuleElectronicLabel"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoDiskID"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoDiskHealthStatus"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoDiskRunningStatus"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoDiskType"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoDiskCapacity"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoDiskRole"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoDiskSpeed"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoDiskInterfaceBandwidth"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoDiskSectorSize"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoDiskTemperature"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoDiskModel"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoDiskFirmwareVersion"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoDiskManufacturer"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoDiskSerialNumber"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoDiskLightStatus"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoDiskDiskDomainID"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoDiskDiskDomainName"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoDiskDiskDomainTierID"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoDiskCofferDisk"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoDiskRunTime"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoDiskProgress"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoDiskBarCode"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoDiskCapacityUsage"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoDiskHealthMark"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoControllerHealthStatus"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoControllerRunningStatus"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoControllerCPU"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoControllerRole"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoControllerCacheCapacity"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoControllerCPUUsage"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoControllerMemoryUsage"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoControllerVoltage"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoControllerSoftwareVersion"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoControllerPCBVersion"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoControllerSESVersion"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoControllerBMCVersion"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoControllerLogicVersion"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoControllerBIOSVersion"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoControllerElectronicLabel"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPowerHealthStatus"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPowerRunningStatus"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPowerManufacturer"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPowerProduceDate"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPowerSerialNumber"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoFanHealthStatus"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoFanElectronicLabel"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoBBUHealthStatus"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoBBURunningStatus"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoBBUType"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoBBUNumberOfDischarges"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoBBUFirmwareVersion"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoBBUDeliveredOn"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoBBUOwningController"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoBBUElectronicLabel"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoEnclosureID"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoEnclosureLogicType"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoEnclosureHealthStatus"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoEnclosureRunningStatus"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoEnclosureLocation"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoEnclosureType"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoEnclosureTemperature"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoEnclosureSN"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoEnclosureMAC"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoEnclosureHeight"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoEnclosureExpansionDepth"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoFanRunningStatus"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoFanRunningLevel"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPowerModle"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPowerVersion"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoControllerID"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPowerID"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPowerType"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoBBUID"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoControllerLocation"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoDiskLocation"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoEnclosureName"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoEnclosureElectronicLabel"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPowerLocation"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoFanLocation"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoBBULocation"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortFCStartTime"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortEthStartTime"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoPortPCIEStartTime"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoExpBoardID"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoExpBoardLocation"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoExpBoardHealthStatus"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoExpBoardRunningStatus"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoExpBoardModel"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoExpBoardLogicVersion"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoExpBoardPCBVersion"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoExpBoardSESVersion"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoExpBoardELabel"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoBBUCurrentVoltage"),
        ("HUAWEI-STORAGE-HARDWARE-MIB", "hwInfoFanID"))
)
if mibBuilder.loadTexts:
    currentObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

basicCompliance = ModuleCompliance(
    (1, 6, 2, 1)
)
basicCompliance.setObjects(
    ("HUAWEI-STORAGE-HARDWARE-MIB", "currentObjectGroup")
)
if mibBuilder.loadTexts:
    basicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-STORAGE-HARDWARE-MIB",
    **{"NodeCodeString": NodeCodeString,
       "huaweistorage": huaweistorage,
       "hwStorage": hwStorage,
       "hwISM": hwISM,
       "hwStorageDevice": hwStorageDevice,
       "hwHardwareInfo": hwHardwareInfo,
       "hwInfoDiskTable": hwInfoDiskTable,
       "hwInfoDiskEntry": hwInfoDiskEntry,
       "hwInfoDiskID": hwInfoDiskID,
       "hwInfoDiskHealthStatus": hwInfoDiskHealthStatus,
       "hwInfoDiskRunningStatus": hwInfoDiskRunningStatus,
       "hwInfoDiskLocation": hwInfoDiskLocation,
       "hwInfoDiskType": hwInfoDiskType,
       "hwInfoDiskCapacity": hwInfoDiskCapacity,
       "hwInfoDiskRole": hwInfoDiskRole,
       "hwInfoDiskSpeed": hwInfoDiskSpeed,
       "hwInfoDiskInterfaceBandwidth": hwInfoDiskInterfaceBandwidth,
       "hwInfoDiskSectorSize": hwInfoDiskSectorSize,
       "hwInfoDiskTemperature": hwInfoDiskTemperature,
       "hwInfoDiskModel": hwInfoDiskModel,
       "hwInfoDiskFirmwareVersion": hwInfoDiskFirmwareVersion,
       "hwInfoDiskManufacturer": hwInfoDiskManufacturer,
       "hwInfoDiskSerialNumber": hwInfoDiskSerialNumber,
       "hwInfoDiskLightStatus": hwInfoDiskLightStatus,
       "hwInfoDiskDiskDomainID": hwInfoDiskDiskDomainID,
       "hwInfoDiskDiskDomainName": hwInfoDiskDiskDomainName,
       "hwInfoDiskDiskDomainTierID": hwInfoDiskDiskDomainTierID,
       "hwInfoDiskCofferDisk": hwInfoDiskCofferDisk,
       "hwInfoDiskRunTime": hwInfoDiskRunTime,
       "hwInfoDiskProgress": hwInfoDiskProgress,
       "hwInfoDiskBarCode": hwInfoDiskBarCode,
       "hwInfoDiskCapacityUsage": hwInfoDiskCapacityUsage,
       "hwInfoDiskHealthMark": hwInfoDiskHealthMark,
       "hwInfoControllerTable": hwInfoControllerTable,
       "hwInfoControllerEntry": hwInfoControllerEntry,
       "hwInfoControllerID": hwInfoControllerID,
       "hwInfoControllerHealthStatus": hwInfoControllerHealthStatus,
       "hwInfoControllerRunningStatus": hwInfoControllerRunningStatus,
       "hwInfoControllerCPU": hwInfoControllerCPU,
       "hwInfoControllerLocation": hwInfoControllerLocation,
       "hwInfoControllerRole": hwInfoControllerRole,
       "hwInfoControllerCacheCapacity": hwInfoControllerCacheCapacity,
       "hwInfoControllerCPUUsage": hwInfoControllerCPUUsage,
       "hwInfoControllerMemoryUsage": hwInfoControllerMemoryUsage,
       "hwInfoControllerVoltage": hwInfoControllerVoltage,
       "hwInfoControllerSoftwareVersion": hwInfoControllerSoftwareVersion,
       "hwInfoControllerPCBVersion": hwInfoControllerPCBVersion,
       "hwInfoControllerSESVersion": hwInfoControllerSESVersion,
       "hwInfoControllerBMCVersion": hwInfoControllerBMCVersion,
       "hwInfoControllerLogicVersion": hwInfoControllerLogicVersion,
       "hwInfoControllerBIOSVersion": hwInfoControllerBIOSVersion,
       "hwInfoControllerElectronicLabel": hwInfoControllerElectronicLabel,
       "hwInfoPowerTable": hwInfoPowerTable,
       "hwInfoPowerEntry": hwInfoPowerEntry,
       "hwInfoPowerID": hwInfoPowerID,
       "hwInfoPowerLocation": hwInfoPowerLocation,
       "hwInfoPowerHealthStatus": hwInfoPowerHealthStatus,
       "hwInfoPowerRunningStatus": hwInfoPowerRunningStatus,
       "hwInfoPowerType": hwInfoPowerType,
       "hwInfoPowerManufacturer": hwInfoPowerManufacturer,
       "hwInfoPowerModle": hwInfoPowerModle,
       "hwInfoPowerVersion": hwInfoPowerVersion,
       "hwInfoPowerProduceDate": hwInfoPowerProduceDate,
       "hwInfoPowerSerialNumber": hwInfoPowerSerialNumber,
       "hwInfoFanTable": hwInfoFanTable,
       "hwInfoFanEntry": hwInfoFanEntry,
       "hwInfoFanID": hwInfoFanID,
       "hwInfoFanLocation": hwInfoFanLocation,
       "hwInfoFanHealthStatus": hwInfoFanHealthStatus,
       "hwInfoFanRunningStatus": hwInfoFanRunningStatus,
       "hwInfoFanRunningLevel": hwInfoFanRunningLevel,
       "hwInfoFanElectronicLabel": hwInfoFanElectronicLabel,
       "hwInfoBBUTable": hwInfoBBUTable,
       "hwInfoBBUEntry": hwInfoBBUEntry,
       "hwInfoBBUID": hwInfoBBUID,
       "hwInfoBBULocation": hwInfoBBULocation,
       "hwInfoBBUHealthStatus": hwInfoBBUHealthStatus,
       "hwInfoBBURunningStatus": hwInfoBBURunningStatus,
       "hwInfoBBUType": hwInfoBBUType,
       "hwInfoBBUCurrentVoltage": hwInfoBBUCurrentVoltage,
       "hwInfoBBUNumberOfDischarges": hwInfoBBUNumberOfDischarges,
       "hwInfoBBUFirmwareVersion": hwInfoBBUFirmwareVersion,
       "hwInfoBBUDeliveredOn": hwInfoBBUDeliveredOn,
       "hwInfoBBUOwningController": hwInfoBBUOwningController,
       "hwInfoBBUElectronicLabel": hwInfoBBUElectronicLabel,
       "hwInfoEnclosureTable": hwInfoEnclosureTable,
       "hwInfoEnclosureEntry": hwInfoEnclosureEntry,
       "hwInfoEnclosureID": hwInfoEnclosureID,
       "hwInfoEnclosureName": hwInfoEnclosureName,
       "hwInfoEnclosureLogicType": hwInfoEnclosureLogicType,
       "hwInfoEnclosureHealthStatus": hwInfoEnclosureHealthStatus,
       "hwInfoEnclosureRunningStatus": hwInfoEnclosureRunningStatus,
       "hwInfoEnclosureLocation": hwInfoEnclosureLocation,
       "hwInfoEnclosureType": hwInfoEnclosureType,
       "hwInfoEnclosureTemperature": hwInfoEnclosureTemperature,
       "hwInfoEnclosureSN": hwInfoEnclosureSN,
       "hwInfoEnclosureMAC": hwInfoEnclosureMAC,
       "hwInfoEnclosureHeight": hwInfoEnclosureHeight,
       "hwInfoEnclosureExpansionDepth": hwInfoEnclosureExpansionDepth,
       "hwInfoEnclosureElectronicLabel": hwInfoEnclosureElectronicLabel,
       "hwInfoPortComTable": hwInfoPortComTable,
       "hwInfoPortComEntry": hwInfoPortComEntry,
       "hwInfoPortComID": hwInfoPortComID,
       "hwInfoPortComLocation": hwInfoPortComLocation,
       "hwInfoPortComHealthStatus": hwInfoPortComHealthStatus,
       "hwInfoPortComRunningStatus": hwInfoPortComRunningStatus,
       "hwInfoPortComType": hwInfoPortComType,
       "hwInfoPortEthTable": hwInfoPortEthTable,
       "hwInfoPortEthEntry": hwInfoPortEthEntry,
       "hwInfoPortEthID": hwInfoPortEthID,
       "hwInfoPortEthLocation": hwInfoPortEthLocation,
       "hwInfoPortEthHealthStatus": hwInfoPortEthHealthStatus,
       "hwInfoPortEthRunningStatus": hwInfoPortEthRunningStatus,
       "hwInfoPortEthType": hwInfoPortEthType,
       "hwInfoPortEthIPv4Address": hwInfoPortEthIPv4Address,
       "hwInfoPortEthSubnetMask": hwInfoPortEthSubnetMask,
       "hwInfoPortEthIPv4Gateway": hwInfoPortEthIPv4Gateway,
       "hwInfoPortEthIPv6Address": hwInfoPortEthIPv6Address,
       "hwInfoPortEthIPv6PrefixLength": hwInfoPortEthIPv6PrefixLength,
       "hwInfoPortEthIPv6Gateway": hwInfoPortEthIPv6Gateway,
       "hwInfoPortEthMAC": hwInfoPortEthMAC,
       "hwInfoPortEthRole": hwInfoPortEthRole,
       "hwInfoPortEthMode": hwInfoPortEthMode,
       "hwInfoPortEthMTU": hwInfoPortEthMTU,
       "hwInfoPortEthWorkingRate": hwInfoPortEthWorkingRate,
       "hwInfoPortEthBondName": hwInfoPortEthBondName,
       "hwInfoPortEthiSCSIPort": hwInfoPortEthiSCSIPort,
       "hwInfoPortEthiSCSIName": hwInfoPortEthiSCSIName,
       "hwInfoPortEthErrorPackets": hwInfoPortEthErrorPackets,
       "hwInfoPortEthLostPackages": hwInfoPortEthLostPackages,
       "hwInfoPortEthStartTime": hwInfoPortEthStartTime,
       "hwInfoPortFCTable": hwInfoPortFCTable,
       "hwInfoPortFCEntry": hwInfoPortFCEntry,
       "hwInfoPortFCID": hwInfoPortFCID,
       "hwInfoPortFCLocation": hwInfoPortFCLocation,
       "hwInfoPortFCHealthStatus": hwInfoPortFCHealthStatus,
       "hwInfoPortFCRunningStatus": hwInfoPortFCRunningStatus,
       "hwInfoPortFCType": hwInfoPortFCType,
       "hwInfoPortFCWorkingRate": hwInfoPortFCWorkingRate,
       "hwInfoPortFCConfiguredSpeed": hwInfoPortFCConfiguredSpeed,
       "hwInfoPortFCWWN": hwInfoPortFCWWN,
       "hwInfoPortFCRole": hwInfoPortFCRole,
       "hwInfoPortFCSFPStatus": hwInfoPortFCSFPStatus,
       "hwInfoPortFCWorkingMode": hwInfoPortFCWorkingMode,
       "hwInfoPortFCConfiguredMode": hwInfoPortFCConfiguredMode,
       "hwInfoPortFCFloginDelayTimes": hwInfoPortFCFloginDelayTimes,
       "hwInfoPortFCLostSignals": hwInfoPortFCLostSignals,
       "hwInfoPortFCLinkErrorsCodes": hwInfoPortFCLinkErrorsCodes,
       "hwInfoPortFCLostSynchronizations": hwInfoPortFCLostSynchronizations,
       "hwInfoPortFCFailedConnections": hwInfoPortFCFailedConnections,
       "hwInfoPortFCStartTime": hwInfoPortFCStartTime,
       "hwInfoPortFCoETable": hwInfoPortFCoETable,
       "hwInfoPortFCoEEntry": hwInfoPortFCoEEntry,
       "hwInfoPortFCoEID": hwInfoPortFCoEID,
       "hwInfoPortFCoELocation": hwInfoPortFCoELocation,
       "hwInfoPortFCoEHealthStatus": hwInfoPortFCoEHealthStatus,
       "hwInfoPortFCoERunningStatus": hwInfoPortFCoERunningStatus,
       "hwInfoPortFCoEType": hwInfoPortFCoEType,
       "hwInfoPortFCoEWorkingRate": hwInfoPortFCoEWorkingRate,
       "hwInfoPortFCoEWWN": hwInfoPortFCoEWWN,
       "hwInfoPortFCoERole": hwInfoPortFCoERole,
       "hwInfoPortFCoESFPStatus": hwInfoPortFCoESFPStatus,
       "hwInfoPortFCoEErrorPackets": hwInfoPortFCoEErrorPackets,
       "hwInfoPortFCoELostPackets": hwInfoPortFCoELostPackets,
       "hwInfoPortFCoEOverFlowedPackets": hwInfoPortFCoEOverFlowedPackets,
       "hwInfoPortFCoEStartTime": hwInfoPortFCoEStartTime,
       "hwInfoPortPCIETable": hwInfoPortPCIETable,
       "hwInfoPortPCIEEntry": hwInfoPortPCIEEntry,
       "hwInfoPortPCIEID": hwInfoPortPCIEID,
       "hwInfoPortPCIELocation": hwInfoPortPCIELocation,
       "hwInfoPortPCIEHealthStatus": hwInfoPortPCIEHealthStatus,
       "hwInfoPortPCIERunningStatus": hwInfoPortPCIERunningStatus,
       "hwInfoPortPCIESpeed": hwInfoPortPCIESpeed,
       "hwInfoPortPCIECurrentPeerPortID": hwInfoPortPCIECurrentPeerPortID,
       "hwInfoPortPCIESuggestPeerPortID": hwInfoPortPCIESuggestPeerPortID,
       "hwInfoPortPCIELostSignals": hwInfoPortPCIELostSignals,
       "hwInfoPortPCIEECRCError": hwInfoPortPCIEECRCError,
       "hwInfoPortPCIEBadTlp": hwInfoPortPCIEBadTlp,
       "hwInfoPortPCIEBalDllp": hwInfoPortPCIEBalDllp,
       "hwInfoPortPCIERecvError": hwInfoPortPCIERecvError,
       "hwInfoPortPCIEChipEccError": hwInfoPortPCIEChipEccError,
       "hwInfoPortPCIEStartTime": hwInfoPortPCIEStartTime,
       "hwInfoPortSASTable": hwInfoPortSASTable,
       "hwInfoPortSASEntry": hwInfoPortSASEntry,
       "hwInfoPortSASID": hwInfoPortSASID,
       "hwInfoPortSASLocation": hwInfoPortSASLocation,
       "hwInfoPortSASHealthStatus": hwInfoPortSASHealthStatus,
       "hwInfoPortSASRunningStatus": hwInfoPortSASRunningStatus,
       "hwInfoPortSASType": hwInfoPortSASType,
       "hwInfoPortSASWorkingRate": hwInfoPortSASWorkingRate,
       "hwInfoPortSASWWN": hwInfoPortSASWWN,
       "hwInfoPortSASRole": hwInfoPortSASRole,
       "hwInfoPortSASInvalidDword": hwInfoPortSASInvalidDword,
       "hwInfoPortSASConsistErrors": hwInfoPortSASConsistErrors,
       "hwInfoPortSASLossOfDword": hwInfoPortSASLossOfDword,
       "hwInfoPortSASPHYResetErrors": hwInfoPortSASPHYResetErrors,
       "hwInfoPortSASStartTime": hwInfoPortSASStartTime,
       "hwInfoPortSASEnabled": hwInfoPortSASEnabled,
       "hwInfoInterfaceModuleTable": hwInfoInterfaceModuleTable,
       "hwInfoInterfaceModuleEntry": hwInfoInterfaceModuleEntry,
       "hwInfoInterfaceModuleID": hwInfoInterfaceModuleID,
       "hwInfoInterfaceModuleLocation": hwInfoInterfaceModuleLocation,
       "hwInfoInterfaceModuleHealthStatus": hwInfoInterfaceModuleHealthStatus,
       "hwInfoInterfaceModuleRunningStatus": hwInfoInterfaceModuleRunningStatus,
       "hwInfoInterfaceModuleModel": hwInfoInterfaceModuleModel,
       "hwInfoInterfaceModuleLogicVersion": hwInfoInterfaceModuleLogicVersion,
       "hwInfoInterfaceModulePCBVersion": hwInfoInterfaceModulePCBVersion,
       "hwInfoInterfaceModuleElectronicLabel": hwInfoInterfaceModuleElectronicLabel,
       "hwInfoExpBoardTable": hwInfoExpBoardTable,
       "hwInfoExpBoardEntry": hwInfoExpBoardEntry,
       "hwInfoExpBoardID": hwInfoExpBoardID,
       "hwInfoExpBoardLocation": hwInfoExpBoardLocation,
       "hwInfoExpBoardHealthStatus": hwInfoExpBoardHealthStatus,
       "hwInfoExpBoardRunningStatus": hwInfoExpBoardRunningStatus,
       "hwInfoExpBoardModel": hwInfoExpBoardModel,
       "hwInfoExpBoardLogicVersion": hwInfoExpBoardLogicVersion,
       "hwInfoExpBoardPCBVersion": hwInfoExpBoardPCBVersion,
       "hwInfoExpBoardSESVersion": hwInfoExpBoardSESVersion,
       "hwInfoExpBoardELabel": hwInfoExpBoardELabel,
       "isoConformance": isoConformance,
       "isoGroups": isoGroups,
       "currentObjectGroup": currentObjectGroup,
       "isoCompliances": isoCompliances,
       "basicCompliance": basicCompliance}
)
