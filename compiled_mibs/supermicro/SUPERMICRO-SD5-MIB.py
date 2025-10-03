# SNMP MIB module (SUPERMICRO-SD5-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\supermicro\SUPERMICRO-SD5-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:29:24 2025
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

(smSSMInfo,) = mibBuilder.importSymbols(
    "SUPERMICRO-SMI",
    "smSSMInfo")


# MODULE-IDENTITY

smSuperDoctor5MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Sd5Table_Object = MibTable
sd5Table = _Sd5Table_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 1)
)
if mibBuilder.loadTexts:
    sd5Table.setStatus("current")
_Sd5Entry_Object = MibTableRow
sd5Entry = _Sd5Entry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 1, 1)
)
sd5Entry.setIndexNames(
    (0, "SUPERMICRO-SD5-MIB", "sd5Idx"),
)
if mibBuilder.loadTexts:
    sd5Entry.setStatus("current")


class _Sd5Idx_Type(Integer32):
    """Custom type sd5Idx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Sd5Idx_Type.__name__ = "Integer32"
_Sd5Idx_Object = MibTableColumn
sd5Idx = _Sd5Idx_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 1, 1, 1),
    _Sd5Idx_Type()
)
sd5Idx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sd5Idx.setStatus("current")
_Sd5Version_Type = DisplayString
_Sd5Version_Object = MibTableColumn
sd5Version = _Sd5Version_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 1, 1, 2),
    _Sd5Version_Type()
)
sd5Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sd5Version.setStatus("current")
_Sd5MIBVersion_Type = DisplayString
_Sd5MIBVersion_Object = MibTableColumn
sd5MIBVersion = _Sd5MIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 1, 1, 3),
    _Sd5MIBVersion_Type()
)
sd5MIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sd5MIBVersion.setStatus("current")
_CpuTable_Object = MibTable
cpuTable = _CpuTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 2)
)
if mibBuilder.loadTexts:
    cpuTable.setStatus("current")
_CpuEntry_Object = MibTableRow
cpuEntry = _CpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 2, 1)
)
cpuEntry.setIndexNames(
    (0, "SUPERMICRO-SD5-MIB", "cpuIndex"),
)
if mibBuilder.loadTexts:
    cpuEntry.setStatus("current")
_CpuIndex_Type = DisplayString
_CpuIndex_Object = MibTableColumn
cpuIndex = _CpuIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 2, 1, 1),
    _CpuIndex_Type()
)
cpuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuIndex.setStatus("current")
_CpuName_Type = DisplayString
_CpuName_Object = MibTableColumn
cpuName = _CpuName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 2, 1, 2),
    _CpuName_Type()
)
cpuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuName.setStatus("current")
_CpuDescription_Type = DisplayString
_CpuDescription_Object = MibTableColumn
cpuDescription = _CpuDescription_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 2, 1, 3),
    _CpuDescription_Type()
)
cpuDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuDescription.setStatus("current")
_CpuManufacturer_Type = DisplayString
_CpuManufacturer_Object = MibTableColumn
cpuManufacturer = _CpuManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 2, 1, 4),
    _CpuManufacturer_Type()
)
cpuManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuManufacturer.setStatus("current")


class _CpuDeviceStatus_Type(Integer32):
    """Custom type cpuDeviceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpuDeviceStatus_Type.__name__ = "Integer32"
_CpuDeviceStatus_Object = MibTableColumn
cpuDeviceStatus = _CpuDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 2, 1, 5),
    _CpuDeviceStatus_Type()
)
cpuDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuDeviceStatus.setStatus("current")
_CpuMaxSpeed_Type = DisplayString
_CpuMaxSpeed_Object = MibTableColumn
cpuMaxSpeed = _CpuMaxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 2, 1, 6),
    _CpuMaxSpeed_Type()
)
cpuMaxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuMaxSpeed.setStatus("current")
_CpuCurrentSpeed_Type = DisplayString
_CpuCurrentSpeed_Object = MibTableColumn
cpuCurrentSpeed = _CpuCurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 2, 1, 7),
    _CpuCurrentSpeed_Type()
)
cpuCurrentSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuCurrentSpeed.setStatus("current")
_CpuLoadingPercentage_Type = DisplayString
_CpuLoadingPercentage_Object = MibTableColumn
cpuLoadingPercentage = _CpuLoadingPercentage_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 2, 1, 9),
    _CpuLoadingPercentage_Type()
)
cpuLoadingPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuLoadingPercentage.setStatus("current")


class _CpuCoreEnabled_Type(Integer32):
    """Custom type cpuCoreEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpuCoreEnabled_Type.__name__ = "Integer32"
_CpuCoreEnabled_Object = MibTableColumn
cpuCoreEnabled = _CpuCoreEnabled_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 2, 1, 10),
    _CpuCoreEnabled_Type()
)
cpuCoreEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuCoreEnabled.setStatus("current")


class _CpuCoreCount_Type(Integer32):
    """Custom type cpuCoreCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpuCoreCount_Type.__name__ = "Integer32"
_CpuCoreCount_Object = MibTableColumn
cpuCoreCount = _CpuCoreCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 2, 1, 11),
    _CpuCoreCount_Type()
)
cpuCoreCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuCoreCount.setStatus("current")


class _CpuThreadCount_Type(Integer32):
    """Custom type cpuThreadCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpuThreadCount_Type.__name__ = "Integer32"
_CpuThreadCount_Object = MibTableColumn
cpuThreadCount = _CpuThreadCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 2, 1, 12),
    _CpuThreadCount_Type()
)
cpuThreadCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuThreadCount.setStatus("current")
_CpuSocketDesignation_Type = DisplayString
_CpuSocketDesignation_Object = MibTableColumn
cpuSocketDesignation = _CpuSocketDesignation_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 2, 1, 14),
    _CpuSocketDesignation_Type()
)
cpuSocketDesignation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuSocketDesignation.setStatus("current")
_CpuDeviceVersion_Type = DisplayString
_CpuDeviceVersion_Object = MibTableColumn
cpuDeviceVersion = _CpuDeviceVersion_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 2, 1, 18),
    _CpuDeviceVersion_Type()
)
cpuDeviceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuDeviceVersion.setStatus("current")
_CpuDeviceID_Type = DisplayString
_CpuDeviceID_Object = MibTableColumn
cpuDeviceID = _CpuDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 2, 1, 20),
    _CpuDeviceID_Type()
)
cpuDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuDeviceID.setStatus("current")
_CpuID_Type = DisplayString
_CpuID_Object = MibTableColumn
cpuID = _CpuID_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 2, 1, 21),
    _CpuID_Type()
)
cpuID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuID.setStatus("current")
_MemTable_Object = MibTable
memTable = _MemTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 3)
)
if mibBuilder.loadTexts:
    memTable.setStatus("current")
_MemEntry_Object = MibTableRow
memEntry = _MemEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 3, 1)
)
memEntry.setIndexNames(
    (0, "SUPERMICRO-SD5-MIB", "memTag"),
)
if mibBuilder.loadTexts:
    memEntry.setStatus("current")
_MemTag_Type = DisplayString
_MemTag_Object = MibTableColumn
memTag = _MemTag_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 3, 1, 1),
    _MemTag_Type()
)
memTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memTag.setStatus("current")
_MemDescription_Type = DisplayString
_MemDescription_Object = MibTableColumn
memDescription = _MemDescription_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 3, 1, 2),
    _MemDescription_Type()
)
memDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memDescription.setStatus("current")


class _MemDeviceStatus_Type(Integer32):
    """Custom type memDeviceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MemDeviceStatus_Type.__name__ = "Integer32"
_MemDeviceStatus_Object = MibTableColumn
memDeviceStatus = _MemDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 3, 1, 3),
    _MemDeviceStatus_Type()
)
memDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memDeviceStatus.setStatus("current")
_MemLabeledBank_Type = DisplayString
_MemLabeledBank_Object = MibTableColumn
memLabeledBank = _MemLabeledBank_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 3, 1, 4),
    _MemLabeledBank_Type()
)
memLabeledBank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memLabeledBank.setStatus("current")
_MemDeviceLocator_Type = DisplayString
_MemDeviceLocator_Object = MibTableColumn
memDeviceLocator = _MemDeviceLocator_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 3, 1, 5),
    _MemDeviceLocator_Type()
)
memDeviceLocator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memDeviceLocator.setStatus("current")
_MemModel_Type = DisplayString
_MemModel_Object = MibTableColumn
memModel = _MemModel_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 3, 1, 7),
    _MemModel_Type()
)
memModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memModel.setStatus("current")
_MemManufacturer_Type = DisplayString
_MemManufacturer_Object = MibTableColumn
memManufacturer = _MemManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 3, 1, 8),
    _MemManufacturer_Type()
)
memManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memManufacturer.setStatus("current")
_MemPartNumber_Type = DisplayString
_MemPartNumber_Object = MibTableColumn
memPartNumber = _MemPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 3, 1, 9),
    _MemPartNumber_Type()
)
memPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memPartNumber.setStatus("current")
_MemSerialNumber_Type = DisplayString
_MemSerialNumber_Object = MibTableColumn
memSerialNumber = _MemSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 3, 1, 10),
    _MemSerialNumber_Type()
)
memSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memSerialNumber.setStatus("current")


class _MemCapacity_Type(Integer32):
    """Custom type memCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MemCapacity_Type.__name__ = "Integer32"
_MemCapacity_Object = MibTableColumn
memCapacity = _MemCapacity_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 3, 1, 11),
    _MemCapacity_Type()
)
memCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memCapacity.setStatus("current")
_MemDataWidth_Type = DisplayString
_MemDataWidth_Object = MibTableColumn
memDataWidth = _MemDataWidth_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 3, 1, 12),
    _MemDataWidth_Type()
)
memDataWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memDataWidth.setStatus("current")
_MemTotalWidth_Type = DisplayString
_MemTotalWidth_Object = MibTableColumn
memTotalWidth = _MemTotalWidth_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 3, 1, 13),
    _MemTotalWidth_Type()
)
memTotalWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memTotalWidth.setStatus("current")


class _MemErrorCount_Type(Integer32):
    """Custom type memErrorCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MemErrorCount_Type.__name__ = "Integer32"
_MemErrorCount_Object = MibTableColumn
memErrorCount = _MemErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 3, 1, 15),
    _MemErrorCount_Type()
)
memErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memErrorCount.setStatus("current")


class _MemECCErrorCount_Type(Integer32):
    """Custom type memECCErrorCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MemECCErrorCount_Type.__name__ = "Integer32"
_MemECCErrorCount_Object = MibTableColumn
memECCErrorCount = _MemECCErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 3, 1, 16),
    _MemECCErrorCount_Type()
)
memECCErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memECCErrorCount.setStatus("current")


class _MemUECCErrorCount_Type(Integer32):
    """Custom type memUECCErrorCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MemUECCErrorCount_Type.__name__ = "Integer32"
_MemUECCErrorCount_Object = MibTableColumn
memUECCErrorCount = _MemUECCErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 3, 1, 17),
    _MemUECCErrorCount_Type()
)
memUECCErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memUECCErrorCount.setStatus("current")
_DiskTable_Object = MibTable
diskTable = _DiskTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 4)
)
if mibBuilder.loadTexts:
    diskTable.setStatus("current")
_DiskEntry_Object = MibTableRow
diskEntry = _DiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 4, 1)
)
diskEntry.setIndexNames(
    (0, "SUPERMICRO-SD5-MIB", "diskName"),
)
if mibBuilder.loadTexts:
    diskEntry.setStatus("current")
_DiskSerialNumber_Type = DisplayString
_DiskSerialNumber_Object = MibTableColumn
diskSerialNumber = _DiskSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 4, 1, 1),
    _DiskSerialNumber_Type()
)
diskSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskSerialNumber.setStatus("current")
_DiskName_Type = DisplayString
_DiskName_Object = MibTableColumn
diskName = _DiskName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 4, 1, 2),
    _DiskName_Type()
)
diskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskName.setStatus("current")
_DiskVendor_Type = DisplayString
_DiskVendor_Object = MibTableColumn
diskVendor = _DiskVendor_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 4, 1, 3),
    _DiskVendor_Type()
)
diskVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskVendor.setStatus("current")


class _DiskSmartStatus_Type(Integer32):
    """Custom type diskSmartStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DiskSmartStatus_Type.__name__ = "Integer32"
_DiskSmartStatus_Object = MibTableColumn
diskSmartStatus = _DiskSmartStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 4, 1, 4),
    _DiskSmartStatus_Type()
)
diskSmartStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskSmartStatus.setStatus("current")
_DiskModel_Type = DisplayString
_DiskModel_Object = MibTableColumn
diskModel = _DiskModel_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 4, 1, 5),
    _DiskModel_Type()
)
diskModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskModel.setStatus("current")


class _DiskSize_Type(Integer32):
    """Custom type diskSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DiskSize_Type.__name__ = "Integer32"
_DiskSize_Object = MibTableColumn
diskSize = _DiskSize_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 4, 1, 6),
    _DiskSize_Type()
)
diskSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskSize.setStatus("current")
_DiskMediaType_Type = DisplayString
_DiskMediaType_Object = MibTableColumn
diskMediaType = _DiskMediaType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 4, 1, 8),
    _DiskMediaType_Type()
)
diskMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskMediaType.setStatus("current")
_DiskInterfaceType_Type = DisplayString
_DiskInterfaceType_Object = MibTableColumn
diskInterfaceType = _DiskInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 4, 1, 9),
    _DiskInterfaceType_Type()
)
diskInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskInterfaceType.setStatus("current")
_DiskController_Type = DisplayString
_DiskController_Object = MibTableColumn
diskController = _DiskController_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 4, 1, 10),
    _DiskController_Type()
)
diskController.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskController.setStatus("current")
_DiskSlotID_Type = DisplayString
_DiskSlotID_Object = MibTableColumn
diskSlotID = _DiskSlotID_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 4, 1, 11),
    _DiskSlotID_Type()
)
diskSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskSlotID.setStatus("current")
_SysBIOSTable_Object = MibTable
sysBIOSTable = _SysBIOSTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 5)
)
if mibBuilder.loadTexts:
    sysBIOSTable.setStatus("current")
_SysBIOSEntry_Object = MibTableRow
sysBIOSEntry = _SysBIOSEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 5, 1)
)
sysBIOSEntry.setIndexNames(
    (0, "SUPERMICRO-SD5-MIB", "sysBIOSIndex"),
)
if mibBuilder.loadTexts:
    sysBIOSEntry.setStatus("current")


class _SysBIOSIndex_Type(Integer32):
    """Custom type sysBIOSIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SysBIOSIndex_Type.__name__ = "Integer32"
_SysBIOSIndex_Object = MibTableColumn
sysBIOSIndex = _SysBIOSIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 5, 1, 1),
    _SysBIOSIndex_Type()
)
sysBIOSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBIOSIndex.setStatus("current")
_SysBIOSReleaseDate_Type = DisplayString
_SysBIOSReleaseDate_Object = MibTableColumn
sysBIOSReleaseDate = _SysBIOSReleaseDate_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 5, 1, 7),
    _SysBIOSReleaseDate_Type()
)
sysBIOSReleaseDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBIOSReleaseDate.setStatus("current")
_SysBIOSVersion_Type = DisplayString
_SysBIOSVersion_Object = MibTableColumn
sysBIOSVersion = _SysBIOSVersion_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 5, 1, 8),
    _SysBIOSVersion_Type()
)
sysBIOSVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBIOSVersion.setStatus("current")
_SysBIOSManufacturer_Type = DisplayString
_SysBIOSManufacturer_Object = MibTableColumn
sysBIOSManufacturer = _SysBIOSManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 5, 1, 11),
    _SysBIOSManufacturer_Type()
)
sysBIOSManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBIOSManufacturer.setStatus("current")
_MbTable_Object = MibTable
mbTable = _MbTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 6)
)
if mibBuilder.loadTexts:
    mbTable.setStatus("current")
_MbEntry_Object = MibTableRow
mbEntry = _MbEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 6, 1)
)
mbEntry.setIndexNames(
    (0, "SUPERMICRO-SD5-MIB", "mbIndex"),
)
if mibBuilder.loadTexts:
    mbEntry.setStatus("current")


class _MbIndex_Type(Integer32):
    """Custom type mbIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MbIndex_Type.__name__ = "Integer32"
_MbIndex_Object = MibTableColumn
mbIndex = _MbIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 6, 1, 1),
    _MbIndex_Type()
)
mbIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbIndex.setStatus("current")
_MbManufacturer_Type = DisplayString
_MbManufacturer_Object = MibTableColumn
mbManufacturer = _MbManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 6, 1, 10),
    _MbManufacturer_Type()
)
mbManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbManufacturer.setStatus("current")
_MbProductName_Type = DisplayString
_MbProductName_Object = MibTableColumn
mbProductName = _MbProductName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 6, 1, 11),
    _MbProductName_Type()
)
mbProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbProductName.setStatus("current")
_MbVersionName_Type = DisplayString
_MbVersionName_Object = MibTableColumn
mbVersionName = _MbVersionName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 6, 1, 12),
    _MbVersionName_Type()
)
mbVersionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbVersionName.setStatus("current")
_MbAssetTag_Type = DisplayString
_MbAssetTag_Object = MibTableColumn
mbAssetTag = _MbAssetTag_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 6, 1, 15),
    _MbAssetTag_Type()
)
mbAssetTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbAssetTag.setStatus("current")
_MbSerialNumber_Type = DisplayString
_MbSerialNumber_Object = MibTableColumn
mbSerialNumber = _MbSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 6, 1, 16),
    _MbSerialNumber_Type()
)
mbSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbSerialNumber.setStatus("current")
_OsTable_Object = MibTable
osTable = _OsTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 7)
)
if mibBuilder.loadTexts:
    osTable.setStatus("current")
_OsEntry_Object = MibTableRow
osEntry = _OsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 7, 1)
)
osEntry.setIndexNames(
    (0, "SUPERMICRO-SD5-MIB", "osIndex"),
)
if mibBuilder.loadTexts:
    osEntry.setStatus("current")


class _OsIndex_Type(Integer32):
    """Custom type osIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OsIndex_Type.__name__ = "Integer32"
_OsIndex_Object = MibTableColumn
osIndex = _OsIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 7, 1, 1),
    _OsIndex_Type()
)
osIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osIndex.setStatus("current")
_OsName_Type = DisplayString
_OsName_Object = MibTableColumn
osName = _OsName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 7, 1, 6),
    _OsName_Type()
)
osName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osName.setStatus("current")
_OsVersion_Type = DisplayString
_OsVersion_Object = MibTableColumn
osVersion = _OsVersion_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 7, 1, 7),
    _OsVersion_Type()
)
osVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osVersion.setStatus("current")
_OsManufacturer_Type = DisplayString
_OsManufacturer_Object = MibTableColumn
osManufacturer = _OsManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 7, 1, 8),
    _OsManufacturer_Type()
)
osManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osManufacturer.setStatus("current")
_OsSerialNumber_Type = DisplayString
_OsSerialNumber_Object = MibTableColumn
osSerialNumber = _OsSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 7, 1, 9),
    _OsSerialNumber_Type()
)
osSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osSerialNumber.setStatus("current")
_OsCSDVersion_Type = DisplayString
_OsCSDVersion_Object = MibTableColumn
osCSDVersion = _OsCSDVersion_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 7, 1, 10),
    _OsCSDVersion_Type()
)
osCSDVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osCSDVersion.setStatus("current")
_DmiLogTable_ObjectIdentity = ObjectIdentity
dmiLogTable = _DmiLogTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 8)
)
_CeccLogTable_Object = MibTable
ceccLogTable = _CeccLogTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 8, 1)
)
if mibBuilder.loadTexts:
    ceccLogTable.setStatus("current")
_CeccLogEntry_Object = MibTableRow
ceccLogEntry = _CeccLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 8, 1, 1)
)
ceccLogEntry.setIndexNames(
    (0, "SUPERMICRO-SD5-MIB", "ceccLogIndex"),
)
if mibBuilder.loadTexts:
    ceccLogEntry.setStatus("current")
_CeccLogDatetime_Type = DisplayString
_CeccLogDatetime_Object = MibTableColumn
ceccLogDatetime = _CeccLogDatetime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 8, 1, 1, 1),
    _CeccLogDatetime_Type()
)
ceccLogDatetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceccLogDatetime.setStatus("current")
_CeccLogInfo_Type = DisplayString
_CeccLogInfo_Object = MibTableColumn
ceccLogInfo = _CeccLogInfo_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 8, 1, 1, 2),
    _CeccLogInfo_Type()
)
ceccLogInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceccLogInfo.setStatus("current")


class _CeccLogIndex_Type(Integer32):
    """Custom type ceccLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CeccLogIndex_Type.__name__ = "Integer32"
_CeccLogIndex_Object = MibTableColumn
ceccLogIndex = _CeccLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 8, 1, 1, 10),
    _CeccLogIndex_Type()
)
ceccLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceccLogIndex.setStatus("current")
_UeccLogTable_Object = MibTable
ueccLogTable = _UeccLogTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 8, 2)
)
if mibBuilder.loadTexts:
    ueccLogTable.setStatus("current")
_UeccLogEntry_Object = MibTableRow
ueccLogEntry = _UeccLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 8, 2, 1)
)
ueccLogEntry.setIndexNames(
    (0, "SUPERMICRO-SD5-MIB", "ceccLogIndex"),
)
if mibBuilder.loadTexts:
    ueccLogEntry.setStatus("current")
_UeccLogDatetime_Type = DisplayString
_UeccLogDatetime_Object = MibTableColumn
ueccLogDatetime = _UeccLogDatetime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 8, 2, 1, 1),
    _UeccLogDatetime_Type()
)
ueccLogDatetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ueccLogDatetime.setStatus("current")
_UeccLogInfo_Type = DisplayString
_UeccLogInfo_Object = MibTableColumn
ueccLogInfo = _UeccLogInfo_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 8, 2, 1, 2),
    _UeccLogInfo_Type()
)
ueccLogInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ueccLogInfo.setStatus("current")


class _UeccLogIndex_Type(Integer32):
    """Custom type ueccLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UeccLogIndex_Type.__name__ = "Integer32"
_UeccLogIndex_Object = MibTableColumn
ueccLogIndex = _UeccLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 8, 2, 1, 10),
    _UeccLogIndex_Type()
)
ueccLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ueccLogIndex.setStatus("current")
_PostLogTable_Object = MibTable
postLogTable = _PostLogTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 8, 8)
)
if mibBuilder.loadTexts:
    postLogTable.setStatus("current")
_PostLogEntry_Object = MibTableRow
postLogEntry = _PostLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 8, 8, 1)
)
postLogEntry.setIndexNames(
    (0, "SUPERMICRO-SD5-MIB", "postLogIndex"),
)
if mibBuilder.loadTexts:
    postLogEntry.setStatus("current")
_PostLogDatetime_Type = DisplayString
_PostLogDatetime_Object = MibTableColumn
postLogDatetime = _PostLogDatetime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 8, 8, 1, 1),
    _PostLogDatetime_Type()
)
postLogDatetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    postLogDatetime.setStatus("current")
_PostLogInfo_Type = DisplayString
_PostLogInfo_Object = MibTableColumn
postLogInfo = _PostLogInfo_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 8, 8, 1, 2),
    _PostLogInfo_Type()
)
postLogInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    postLogInfo.setStatus("current")


class _PostLogIndex_Type(Integer32):
    """Custom type postLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PostLogIndex_Type.__name__ = "Integer32"
_PostLogIndex_Object = MibTableColumn
postLogIndex = _PostLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 8, 8, 1, 10),
    _PostLogIndex_Type()
)
postLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    postLogIndex.setStatus("current")
_CpuLogTable_Object = MibTable
cpuLogTable = _CpuLogTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 8, 11)
)
if mibBuilder.loadTexts:
    cpuLogTable.setStatus("current")
_CpuLogEntry_Object = MibTableRow
cpuLogEntry = _CpuLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 8, 11, 1)
)
cpuLogEntry.setIndexNames(
    (0, "SUPERMICRO-SD5-MIB", "cpuLogIndex"),
)
if mibBuilder.loadTexts:
    cpuLogEntry.setStatus("current")
_CpuLogDatetime_Type = DisplayString
_CpuLogDatetime_Object = MibTableColumn
cpuLogDatetime = _CpuLogDatetime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 8, 11, 1, 1),
    _CpuLogDatetime_Type()
)
cpuLogDatetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuLogDatetime.setStatus("current")
_CpuLogInfo_Type = DisplayString
_CpuLogInfo_Object = MibTableColumn
cpuLogInfo = _CpuLogInfo_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 8, 11, 1, 2),
    _CpuLogInfo_Type()
)
cpuLogInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuLogInfo.setStatus("current")


class _CpuLogIndex_Type(Integer32):
    """Custom type cpuLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CpuLogIndex_Type.__name__ = "Integer32"
_CpuLogIndex_Object = MibTableColumn
cpuLogIndex = _CpuLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 8, 11, 1, 10),
    _CpuLogIndex_Type()
)
cpuLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuLogIndex.setStatus("current")
_RaidAdapterTable_Object = MibTable
raidAdapterTable = _RaidAdapterTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 9)
)
if mibBuilder.loadTexts:
    raidAdapterTable.setStatus("current")
_RaidAdapterEntry_Object = MibTableRow
raidAdapterEntry = _RaidAdapterEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 9, 1)
)
raidAdapterEntry.setIndexNames(
    (0, "SUPERMICRO-SD5-MIB", "raidAdapterIndex"),
)
if mibBuilder.loadTexts:
    raidAdapterEntry.setStatus("current")


class _RaidAdapterIndex_Type(Integer32):
    """Custom type raidAdapterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RaidAdapterIndex_Type.__name__ = "Integer32"
_RaidAdapterIndex_Object = MibTableColumn
raidAdapterIndex = _RaidAdapterIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 9, 1, 1),
    _RaidAdapterIndex_Type()
)
raidAdapterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidAdapterIndex.setStatus("current")
_RaidAdapterGroup_Type = DisplayString
_RaidAdapterGroup_Object = MibTableColumn
raidAdapterGroup = _RaidAdapterGroup_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 9, 1, 2),
    _RaidAdapterGroup_Type()
)
raidAdapterGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidAdapterGroup.setStatus("current")
_RaidAdapterId_Type = DisplayString
_RaidAdapterId_Object = MibTableColumn
raidAdapterId = _RaidAdapterId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 9, 1, 3),
    _RaidAdapterId_Type()
)
raidAdapterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidAdapterId.setStatus("current")
_RaidAdapterProductName_Type = DisplayString
_RaidAdapterProductName_Object = MibTableColumn
raidAdapterProductName = _RaidAdapterProductName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 9, 1, 4),
    _RaidAdapterProductName_Type()
)
raidAdapterProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidAdapterProductName.setStatus("current")
_RaidAdapterSerialNumber_Type = DisplayString
_RaidAdapterSerialNumber_Object = MibTableColumn
raidAdapterSerialNumber = _RaidAdapterSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 9, 1, 5),
    _RaidAdapterSerialNumber_Type()
)
raidAdapterSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidAdapterSerialNumber.setStatus("current")
_RaidAdapterFWPackageBuild_Type = DisplayString
_RaidAdapterFWPackageBuild_Object = MibTableColumn
raidAdapterFWPackageBuild = _RaidAdapterFWPackageBuild_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 9, 1, 6),
    _RaidAdapterFWPackageBuild_Type()
)
raidAdapterFWPackageBuild.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidAdapterFWPackageBuild.setStatus("current")
_RaidAdapterFWVersion_Type = DisplayString
_RaidAdapterFWVersion_Object = MibTableColumn
raidAdapterFWVersion = _RaidAdapterFWVersion_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 9, 1, 7),
    _RaidAdapterFWVersion_Type()
)
raidAdapterFWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidAdapterFWVersion.setStatus("current")
_RaidAdapterBIOSVersion_Type = DisplayString
_RaidAdapterBIOSVersion_Object = MibTableColumn
raidAdapterBIOSVersion = _RaidAdapterBIOSVersion_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 9, 1, 8),
    _RaidAdapterBIOSVersion_Type()
)
raidAdapterBIOSVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidAdapterBIOSVersion.setStatus("current")
_RaidAdapterVendorId_Type = DisplayString
_RaidAdapterVendorId_Object = MibTableColumn
raidAdapterVendorId = _RaidAdapterVendorId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 9, 1, 9),
    _RaidAdapterVendorId_Type()
)
raidAdapterVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidAdapterVendorId.setStatus("current")
_RaidAdapterDeviceId_Type = DisplayString
_RaidAdapterDeviceId_Object = MibTableColumn
raidAdapterDeviceId = _RaidAdapterDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 9, 1, 10),
    _RaidAdapterDeviceId_Type()
)
raidAdapterDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidAdapterDeviceId.setStatus("current")
_RaidAdapterSubVendorId_Type = DisplayString
_RaidAdapterSubVendorId_Object = MibTableColumn
raidAdapterSubVendorId = _RaidAdapterSubVendorId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 9, 1, 11),
    _RaidAdapterSubVendorId_Type()
)
raidAdapterSubVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidAdapterSubVendorId.setStatus("current")
_RaidAdapterSubDeviceId_Type = DisplayString
_RaidAdapterSubDeviceId_Object = MibTableColumn
raidAdapterSubDeviceId = _RaidAdapterSubDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 9, 1, 12),
    _RaidAdapterSubDeviceId_Type()
)
raidAdapterSubDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidAdapterSubDeviceId.setStatus("current")
_RaidIsBBUAbsent_Type = DisplayString
_RaidIsBBUAbsent_Object = MibTableColumn
raidIsBBUAbsent = _RaidIsBBUAbsent_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 9, 1, 13),
    _RaidIsBBUAbsent_Type()
)
raidIsBBUAbsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidIsBBUAbsent.setStatus("current")
_RaidIsBBUAbsentIgnored_Type = DisplayString
_RaidIsBBUAbsentIgnored_Object = MibTableColumn
raidIsBBUAbsentIgnored = _RaidIsBBUAbsentIgnored_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 9, 1, 14),
    _RaidIsBBUAbsentIgnored_Type()
)
raidIsBBUAbsentIgnored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidIsBBUAbsentIgnored.setStatus("current")


class _RaidAdapterAllinoneStatus_Type(Integer32):
    """Custom type raidAdapterAllinoneStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RaidAdapterAllinoneStatus_Type.__name__ = "Integer32"
_RaidAdapterAllinoneStatus_Object = MibTableColumn
raidAdapterAllinoneStatus = _RaidAdapterAllinoneStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 9, 1, 15),
    _RaidAdapterAllinoneStatus_Type()
)
raidAdapterAllinoneStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidAdapterAllinoneStatus.setStatus("current")
_RaidAdapterAllinoneMsg_Type = DisplayString
_RaidAdapterAllinoneMsg_Object = MibTableColumn
raidAdapterAllinoneMsg = _RaidAdapterAllinoneMsg_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 9, 1, 16),
    _RaidAdapterAllinoneMsg_Type()
)
raidAdapterAllinoneMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidAdapterAllinoneMsg.setStatus("current")
_RaidBBUTable_Object = MibTable
raidBBUTable = _RaidBBUTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 10)
)
if mibBuilder.loadTexts:
    raidBBUTable.setStatus("current")
_RaidBBUEntry_Object = MibTableRow
raidBBUEntry = _RaidBBUEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 10, 1)
)
raidBBUEntry.setIndexNames(
    (0, "SUPERMICRO-SD5-MIB", "raidBBUIndex"),
)
if mibBuilder.loadTexts:
    raidBBUEntry.setStatus("current")


class _RaidBBUIndex_Type(Integer32):
    """Custom type raidBBUIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RaidBBUIndex_Type.__name__ = "Integer32"
_RaidBBUIndex_Object = MibTableColumn
raidBBUIndex = _RaidBBUIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 10, 1, 1),
    _RaidBBUIndex_Type()
)
raidBBUIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidBBUIndex.setStatus("current")
_RaidAdapterGroup_BBU_Type = DisplayString
_RaidAdapterGroup_BBU_Object = MibTableColumn
raidAdapterGroup_BBU = _RaidAdapterGroup_BBU_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 10, 1, 2),
    _RaidAdapterGroup_BBU_Type()
)
raidAdapterGroup_BBU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidAdapterGroup_BBU.setStatus("current")
_RaidAdapterId_BBU_Type = DisplayString
_RaidAdapterId_BBU_Object = MibTableColumn
raidAdapterId_BBU = _RaidAdapterId_BBU_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 10, 1, 3),
    _RaidAdapterId_BBU_Type()
)
raidAdapterId_BBU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidAdapterId_BBU.setStatus("current")
_RaidBBUStatus_Type = DisplayString
_RaidBBUStatus_Object = MibTableColumn
raidBBUStatus = _RaidBBUStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 10, 1, 8),
    _RaidBBUStatus_Type()
)
raidBBUStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidBBUStatus.setStatus("current")


class _RaidBBUAllinoneStatus_Type(Integer32):
    """Custom type raidBBUAllinoneStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RaidBBUAllinoneStatus_Type.__name__ = "Integer32"
_RaidBBUAllinoneStatus_Object = MibTableColumn
raidBBUAllinoneStatus = _RaidBBUAllinoneStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 10, 1, 9),
    _RaidBBUAllinoneStatus_Type()
)
raidBBUAllinoneStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidBBUAllinoneStatus.setStatus("current")
_RaidBBUAllinoneMsg_Type = DisplayString
_RaidBBUAllinoneMsg_Object = MibTableColumn
raidBBUAllinoneMsg = _RaidBBUAllinoneMsg_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 10, 1, 10),
    _RaidBBUAllinoneMsg_Type()
)
raidBBUAllinoneMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidBBUAllinoneMsg.setStatus("current")
_RaidVDTable_Object = MibTable
raidVDTable = _RaidVDTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 11)
)
if mibBuilder.loadTexts:
    raidVDTable.setStatus("current")
_RaidVDEntry_Object = MibTableRow
raidVDEntry = _RaidVDEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 11, 1)
)
raidVDEntry.setIndexNames(
    (0, "SUPERMICRO-SD5-MIB", "raidVDIndex"),
)
if mibBuilder.loadTexts:
    raidVDEntry.setStatus("current")


class _RaidVDIndex_Type(Integer32):
    """Custom type raidVDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RaidVDIndex_Type.__name__ = "Integer32"
_RaidVDIndex_Object = MibTableColumn
raidVDIndex = _RaidVDIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 11, 1, 1),
    _RaidVDIndex_Type()
)
raidVDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVDIndex.setStatus("current")
_RaidAdapterGroup_VD_Type = DisplayString
_RaidAdapterGroup_VD_Object = MibTableColumn
raidAdapterGroup_VD = _RaidAdapterGroup_VD_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 11, 1, 2),
    _RaidAdapterGroup_VD_Type()
)
raidAdapterGroup_VD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidAdapterGroup_VD.setStatus("current")
_RaidAdapterId_VD_Type = DisplayString
_RaidAdapterId_VD_Object = MibTableColumn
raidAdapterId_VD = _RaidAdapterId_VD_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 11, 1, 3),
    _RaidAdapterId_VD_Type()
)
raidAdapterId_VD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidAdapterId_VD.setStatus("current")
_RaidDiskGroupId_Type = DisplayString
_RaidDiskGroupId_Object = MibTableColumn
raidDiskGroupId = _RaidDiskGroupId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 11, 1, 4),
    _RaidDiskGroupId_Type()
)
raidDiskGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDiskGroupId.setStatus("current")
_RaidVDId_Type = DisplayString
_RaidVDId_Object = MibTableColumn
raidVDId = _RaidVDId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 11, 1, 5),
    _RaidVDId_Type()
)
raidVDId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVDId.setStatus("current")
_RaidVDTargetId_Type = DisplayString
_RaidVDTargetId_Object = MibTableColumn
raidVDTargetId = _RaidVDTargetId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 11, 1, 6),
    _RaidVDTargetId_Type()
)
raidVDTargetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVDTargetId.setStatus("current")
_RaidVDName_Type = DisplayString
_RaidVDName_Object = MibTableColumn
raidVDName = _RaidVDName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 11, 1, 7),
    _RaidVDName_Type()
)
raidVDName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVDName.setStatus("current")
_RaidVDRaidLevel_Type = DisplayString
_RaidVDRaidLevel_Object = MibTableColumn
raidVDRaidLevel = _RaidVDRaidLevel_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 11, 1, 8),
    _RaidVDRaidLevel_Type()
)
raidVDRaidLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVDRaidLevel.setStatus("current")
_RaidVDSize_Type = DisplayString
_RaidVDSize_Object = MibTableColumn
raidVDSize = _RaidVDSize_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 11, 1, 9),
    _RaidVDSize_Type()
)
raidVDSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVDSize.setStatus("current")
_RaidVDMirrorDataSize_Type = DisplayString
_RaidVDMirrorDataSize_Object = MibTableColumn
raidVDMirrorDataSize = _RaidVDMirrorDataSize_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 11, 1, 10),
    _RaidVDMirrorDataSize_Type()
)
raidVDMirrorDataSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVDMirrorDataSize.setStatus("current")
_RaidVDStripSize_Type = DisplayString
_RaidVDStripSize_Object = MibTableColumn
raidVDStripSize = _RaidVDStripSize_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 11, 1, 11),
    _RaidVDStripSize_Type()
)
raidVDStripSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVDStripSize.setStatus("current")
_RaidVDNumDrives_Type = DisplayString
_RaidVDNumDrives_Object = MibTableColumn
raidVDNumDrives = _RaidVDNumDrives_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 11, 1, 12),
    _RaidVDNumDrives_Type()
)
raidVDNumDrives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVDNumDrives.setStatus("current")
_RaidVDSpanDepth_Type = DisplayString
_RaidVDSpanDepth_Object = MibTableColumn
raidVDSpanDepth = _RaidVDSpanDepth_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 11, 1, 13),
    _RaidVDSpanDepth_Type()
)
raidVDSpanDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVDSpanDepth.setStatus("current")
_RaidVDDefaultCachePolicy_Type = DisplayString
_RaidVDDefaultCachePolicy_Object = MibTableColumn
raidVDDefaultCachePolicy = _RaidVDDefaultCachePolicy_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 11, 1, 14),
    _RaidVDDefaultCachePolicy_Type()
)
raidVDDefaultCachePolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVDDefaultCachePolicy.setStatus("current")
_RaidVDCurrentCachePolicy_Type = DisplayString
_RaidVDCurrentCachePolicy_Object = MibTableColumn
raidVDCurrentCachePolicy = _RaidVDCurrentCachePolicy_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 11, 1, 15),
    _RaidVDCurrentCachePolicy_Type()
)
raidVDCurrentCachePolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVDCurrentCachePolicy.setStatus("current")
_RaidVDDefaultAccessPolicy_Type = DisplayString
_RaidVDDefaultAccessPolicy_Object = MibTableColumn
raidVDDefaultAccessPolicy = _RaidVDDefaultAccessPolicy_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 11, 1, 16),
    _RaidVDDefaultAccessPolicy_Type()
)
raidVDDefaultAccessPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVDDefaultAccessPolicy.setStatus("current")
_RaidVDCurrentAccessPolicy_Type = DisplayString
_RaidVDCurrentAccessPolicy_Object = MibTableColumn
raidVDCurrentAccessPolicy = _RaidVDCurrentAccessPolicy_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 11, 1, 17),
    _RaidVDCurrentAccessPolicy_Type()
)
raidVDCurrentAccessPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVDCurrentAccessPolicy.setStatus("current")
_RaidVDDiskCachePolicy_Type = DisplayString
_RaidVDDiskCachePolicy_Object = MibTableColumn
raidVDDiskCachePolicy = _RaidVDDiskCachePolicy_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 11, 1, 18),
    _RaidVDDiskCachePolicy_Type()
)
raidVDDiskCachePolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVDDiskCachePolicy.setStatus("current")
_RaidVDEncryptionType_Type = DisplayString
_RaidVDEncryptionType_Object = MibTableColumn
raidVDEncryptionType = _RaidVDEncryptionType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 11, 1, 19),
    _RaidVDEncryptionType_Type()
)
raidVDEncryptionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVDEncryptionType.setStatus("current")
_RaidVDDefaultPSPolicy_Type = DisplayString
_RaidVDDefaultPSPolicy_Object = MibTableColumn
raidVDDefaultPSPolicy = _RaidVDDefaultPSPolicy_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 11, 1, 20),
    _RaidVDDefaultPSPolicy_Type()
)
raidVDDefaultPSPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVDDefaultPSPolicy.setStatus("current")
_RaidVDCurrentPSPolicy_Type = DisplayString
_RaidVDCurrentPSPolicy_Object = MibTableColumn
raidVDCurrentPSPolicy = _RaidVDCurrentPSPolicy_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 11, 1, 21),
    _RaidVDCurrentPSPolicy_Type()
)
raidVDCurrentPSPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVDCurrentPSPolicy.setStatus("current")
_RaidVDCanSpinUpIn1Min_Type = DisplayString
_RaidVDCanSpinUpIn1Min_Object = MibTableColumn
raidVDCanSpinUpIn1Min = _RaidVDCanSpinUpIn1Min_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 11, 1, 22),
    _RaidVDCanSpinUpIn1Min_Type()
)
raidVDCanSpinUpIn1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVDCanSpinUpIn1Min.setStatus("current")
_RaidVDSupportT10Power_Type = DisplayString
_RaidVDSupportT10Power_Object = MibTableColumn
raidVDSupportT10Power = _RaidVDSupportT10Power_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 11, 1, 23),
    _RaidVDSupportT10Power_Type()
)
raidVDSupportT10Power.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVDSupportT10Power.setStatus("current")
_RaidVDSupportsMaxPS_Type = DisplayString
_RaidVDSupportsMaxPS_Object = MibTableColumn
raidVDSupportsMaxPS = _RaidVDSupportsMaxPS_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 11, 1, 24),
    _RaidVDSupportsMaxPS_Type()
)
raidVDSupportsMaxPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVDSupportsMaxPS.setStatus("current")
_RaidVDBadBlocksExist_Type = DisplayString
_RaidVDBadBlocksExist_Object = MibTableColumn
raidVDBadBlocksExist = _RaidVDBadBlocksExist_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 11, 1, 25),
    _RaidVDBadBlocksExist_Type()
)
raidVDBadBlocksExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVDBadBlocksExist.setStatus("current")
_RaidVDCached_Type = DisplayString
_RaidVDCached_Object = MibTableColumn
raidVDCached = _RaidVDCached_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 11, 1, 26),
    _RaidVDCached_Type()
)
raidVDCached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVDCached.setStatus("current")
_RaidVDState_Type = DisplayString
_RaidVDState_Object = MibTableColumn
raidVDState = _RaidVDState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 11, 1, 27),
    _RaidVDState_Type()
)
raidVDState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVDState.setStatus("current")


class _RaidVDAllinoneStatus_Type(Integer32):
    """Custom type raidVDAllinoneStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RaidVDAllinoneStatus_Type.__name__ = "Integer32"
_RaidVDAllinoneStatus_Object = MibTableColumn
raidVDAllinoneStatus = _RaidVDAllinoneStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 11, 1, 28),
    _RaidVDAllinoneStatus_Type()
)
raidVDAllinoneStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVDAllinoneStatus.setStatus("current")
_RaidVDAllinoneMsg_Type = DisplayString
_RaidVDAllinoneMsg_Object = MibTableColumn
raidVDAllinoneMsg = _RaidVDAllinoneMsg_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 11, 1, 29),
    _RaidVDAllinoneMsg_Type()
)
raidVDAllinoneMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVDAllinoneMsg.setStatus("current")
_RaidPDTable_Object = MibTable
raidPDTable = _RaidPDTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 12)
)
if mibBuilder.loadTexts:
    raidPDTable.setStatus("current")
_RaidPDEntry_Object = MibTableRow
raidPDEntry = _RaidPDEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 12, 1)
)
raidPDEntry.setIndexNames(
    (0, "SUPERMICRO-SD5-MIB", "raidPDIndex"),
)
if mibBuilder.loadTexts:
    raidPDEntry.setStatus("current")


class _RaidPDIndex_Type(Integer32):
    """Custom type raidPDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RaidPDIndex_Type.__name__ = "Integer32"
_RaidPDIndex_Object = MibTableColumn
raidPDIndex = _RaidPDIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 12, 1, 1),
    _RaidPDIndex_Type()
)
raidPDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPDIndex.setStatus("current")
_RaidAdapterGroup_PD_Type = DisplayString
_RaidAdapterGroup_PD_Object = MibTableColumn
raidAdapterGroup_PD = _RaidAdapterGroup_PD_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 12, 1, 2),
    _RaidAdapterGroup_PD_Type()
)
raidAdapterGroup_PD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidAdapterGroup_PD.setStatus("current")
_RaidAdapterId_PD_Type = DisplayString
_RaidAdapterId_PD_Object = MibTableColumn
raidAdapterId_PD = _RaidAdapterId_PD_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 12, 1, 3),
    _RaidAdapterId_PD_Type()
)
raidAdapterId_PD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidAdapterId_PD.setStatus("current")
_RaidDiskGroupId_PD_Type = DisplayString
_RaidDiskGroupId_PD_Object = MibTableColumn
raidDiskGroupId_PD = _RaidDiskGroupId_PD_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 12, 1, 4),
    _RaidDiskGroupId_PD_Type()
)
raidDiskGroupId_PD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDiskGroupId_PD.setStatus("current")
_RaidPDSlotNumber_Type = DisplayString
_RaidPDSlotNumber_Object = MibTableColumn
raidPDSlotNumber = _RaidPDSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 12, 1, 5),
    _RaidPDSlotNumber_Type()
)
raidPDSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPDSlotNumber.setStatus("current")
_RaidPDFirmwareState_Type = DisplayString
_RaidPDFirmwareState_Object = MibTableColumn
raidPDFirmwareState = _RaidPDFirmwareState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 12, 1, 6),
    _RaidPDFirmwareState_Type()
)
raidPDFirmwareState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPDFirmwareState.setStatus("current")
_RaidPDMediaErrorCount_Type = DisplayString
_RaidPDMediaErrorCount_Object = MibTableColumn
raidPDMediaErrorCount = _RaidPDMediaErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 12, 1, 7),
    _RaidPDMediaErrorCount_Type()
)
raidPDMediaErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPDMediaErrorCount.setStatus("current")
_RaidPDOtherErrorCount_Type = DisplayString
_RaidPDOtherErrorCount_Object = MibTableColumn
raidPDOtherErrorCount = _RaidPDOtherErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 12, 1, 8),
    _RaidPDOtherErrorCount_Type()
)
raidPDOtherErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPDOtherErrorCount.setStatus("current")
_RaidPDPredFailCount_Type = DisplayString
_RaidPDPredFailCount_Object = MibTableColumn
raidPDPredFailCount = _RaidPDPredFailCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 12, 1, 9),
    _RaidPDPredFailCount_Type()
)
raidPDPredFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPDPredFailCount.setStatus("current")
_RaidPDLastPredFailEventSeqNo_Type = DisplayString
_RaidPDLastPredFailEventSeqNo_Object = MibTableColumn
raidPDLastPredFailEventSeqNo = _RaidPDLastPredFailEventSeqNo_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 12, 1, 10),
    _RaidPDLastPredFailEventSeqNo_Type()
)
raidPDLastPredFailEventSeqNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPDLastPredFailEventSeqNo.setStatus("current")
_RaidPDRawSize_Type = DisplayString
_RaidPDRawSize_Object = MibTableColumn
raidPDRawSize = _RaidPDRawSize_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 12, 1, 11),
    _RaidPDRawSize_Type()
)
raidPDRawSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPDRawSize.setStatus("current")
_RaidPDDeviceFwLevel_Type = DisplayString
_RaidPDDeviceFwLevel_Object = MibTableColumn
raidPDDeviceFwLevel = _RaidPDDeviceFwLevel_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 12, 1, 12),
    _RaidPDDeviceFwLevel_Type()
)
raidPDDeviceFwLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPDDeviceFwLevel.setStatus("current")
_RaidPDInquiryData_Type = DisplayString
_RaidPDInquiryData_Object = MibTableColumn
raidPDInquiryData = _RaidPDInquiryData_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 12, 1, 13),
    _RaidPDInquiryData_Type()
)
raidPDInquiryData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPDInquiryData.setStatus("current")
_RaidPDDeviceSpeed_Type = DisplayString
_RaidPDDeviceSpeed_Object = MibTableColumn
raidPDDeviceSpeed = _RaidPDDeviceSpeed_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 12, 1, 14),
    _RaidPDDeviceSpeed_Type()
)
raidPDDeviceSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPDDeviceSpeed.setStatus("current")
_RaidPDLinkSpeed_Type = DisplayString
_RaidPDLinkSpeed_Object = MibTableColumn
raidPDLinkSpeed = _RaidPDLinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 12, 1, 15),
    _RaidPDLinkSpeed_Type()
)
raidPDLinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPDLinkSpeed.setStatus("current")
_RaidPDMediaType_Type = DisplayString
_RaidPDMediaType_Object = MibTableColumn
raidPDMediaType = _RaidPDMediaType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 12, 1, 16),
    _RaidPDMediaType_Type()
)
raidPDMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPDMediaType.setStatus("current")
_RaidPDWriteCache_Type = DisplayString
_RaidPDWriteCache_Object = MibTableColumn
raidPDWriteCache = _RaidPDWriteCache_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 12, 1, 17),
    _RaidPDWriteCache_Type()
)
raidPDWriteCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPDWriteCache.setStatus("current")
_RaidPDNCQSetting_Type = DisplayString
_RaidPDNCQSetting_Object = MibTableColumn
raidPDNCQSetting = _RaidPDNCQSetting_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 12, 1, 18),
    _RaidPDNCQSetting_Type()
)
raidPDNCQSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPDNCQSetting.setStatus("current")
_RaidPDPort0Linkspeed_Type = DisplayString
_RaidPDPort0Linkspeed_Object = MibTableColumn
raidPDPort0Linkspeed = _RaidPDPort0Linkspeed_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 12, 1, 19),
    _RaidPDPort0Linkspeed_Type()
)
raidPDPort0Linkspeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPDPort0Linkspeed.setStatus("current")
_RaidPDPort0Status_Type = DisplayString
_RaidPDPort0Status_Object = MibTableColumn
raidPDPort0Status = _RaidPDPort0Status_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 12, 1, 20),
    _RaidPDPort0Status_Type()
)
raidPDPort0Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPDPort0Status.setStatus("current")
_RaidPDPort1Linkspeed_Type = DisplayString
_RaidPDPort1Linkspeed_Object = MibTableColumn
raidPDPort1Linkspeed = _RaidPDPort1Linkspeed_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 12, 1, 21),
    _RaidPDPort1Linkspeed_Type()
)
raidPDPort1Linkspeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPDPort1Linkspeed.setStatus("current")
_RaidPDPort1Status_Type = DisplayString
_RaidPDPort1Status_Object = MibTableColumn
raidPDPort1Status = _RaidPDPort1Status_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 12, 1, 22),
    _RaidPDPort1Status_Type()
)
raidPDPort1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPDPort1Status.setStatus("current")
_RaidPDEnclosureDeviceID_Type = DisplayString
_RaidPDEnclosureDeviceID_Object = MibTableColumn
raidPDEnclosureDeviceID = _RaidPDEnclosureDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 12, 1, 23),
    _RaidPDEnclosureDeviceID_Type()
)
raidPDEnclosureDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPDEnclosureDeviceID.setStatus("current")
_RaidPDOpProgress_Type = DisplayString
_RaidPDOpProgress_Object = MibTableColumn
raidPDOpProgress = _RaidPDOpProgress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 12, 1, 24),
    _RaidPDOpProgress_Type()
)
raidPDOpProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPDOpProgress.setStatus("current")
_RaidPDSpan_Type = DisplayString
_RaidPDSpan_Object = MibTableColumn
raidPDSpan = _RaidPDSpan_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 12, 1, 25),
    _RaidPDSpan_Type()
)
raidPDSpan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPDSpan.setStatus("current")


class _RaidPDAllinoneStatus_Type(Integer32):
    """Custom type raidPDAllinoneStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RaidPDAllinoneStatus_Type.__name__ = "Integer32"
_RaidPDAllinoneStatus_Object = MibTableColumn
raidPDAllinoneStatus = _RaidPDAllinoneStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 12, 1, 26),
    _RaidPDAllinoneStatus_Type()
)
raidPDAllinoneStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPDAllinoneStatus.setStatus("current")
_RaidPDAllinoneMsg_Type = DisplayString
_RaidPDAllinoneMsg_Object = MibTableColumn
raidPDAllinoneMsg = _RaidPDAllinoneMsg_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 12, 1, 27),
    _RaidPDAllinoneMsg_Type()
)
raidPDAllinoneMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPDAllinoneMsg.setStatus("current")
_RaidPDModel_Type = DisplayString
_RaidPDModel_Object = MibTableColumn
raidPDModel = _RaidPDModel_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 12, 1, 28),
    _RaidPDModel_Type()
)
raidPDModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPDModel.setStatus("current")
_RaidPDSerialNumber_Type = DisplayString
_RaidPDSerialNumber_Object = MibTableColumn
raidPDSerialNumber = _RaidPDSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 12, 1, 29),
    _RaidPDSerialNumber_Type()
)
raidPDSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPDSerialNumber.setStatus("current")
_RaidPDFirmwareRevision_Type = DisplayString
_RaidPDFirmwareRevision_Object = MibTableColumn
raidPDFirmwareRevision = _RaidPDFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 10876, 100, 1, 12, 1, 30),
    _RaidPDFirmwareRevision_Type()
)
raidPDFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPDFirmwareRevision.setStatus("current")
_SmSD5TrapMIB_ObjectIdentity = ObjectIdentity
smSD5TrapMIB = _SmSD5TrapMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 100, 3)
)

# Managed Objects groups


# Notification objects

trapFanNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 100, 3, 0, 101)
)
if mibBuilder.loadTexts:
    trapFanNormal.setStatus(
        ""
    )

trapFanWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 100, 3, 0, 102)
)
if mibBuilder.loadTexts:
    trapFanWarning.setStatus(
        ""
    )

trapFanCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 100, 3, 0, 103)
)
if mibBuilder.loadTexts:
    trapFanCritical.setStatus(
        ""
    )

trapVoltageNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 100, 3, 0, 201)
)
if mibBuilder.loadTexts:
    trapVoltageNormal.setStatus(
        ""
    )

trapVoltageWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 100, 3, 0, 202)
)
if mibBuilder.loadTexts:
    trapVoltageWarning.setStatus(
        ""
    )

trapVoltageCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 100, 3, 0, 203)
)
if mibBuilder.loadTexts:
    trapVoltageCritical.setStatus(
        ""
    )

trapTemperatureNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 100, 3, 0, 301)
)
if mibBuilder.loadTexts:
    trapTemperatureNormal.setStatus(
        ""
    )

trapTemperatureWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 100, 3, 0, 302)
)
if mibBuilder.loadTexts:
    trapTemperatureWarning.setStatus(
        ""
    )

trapTemperatureCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 100, 3, 0, 303)
)
if mibBuilder.loadTexts:
    trapTemperatureCritical.setStatus(
        ""
    )

trapChassisIntrusionCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 100, 3, 0, 401)
)
if mibBuilder.loadTexts:
    trapChassisIntrusionCleared.setStatus(
        ""
    )

trapChassisIntrusion = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 100, 3, 0, 403)
)
if mibBuilder.loadTexts:
    trapChassisIntrusion.setStatus(
        ""
    )

trapStorageSMARTCheckNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 100, 3, 0, 601)
)
if mibBuilder.loadTexts:
    trapStorageSMARTCheckNormal.setStatus(
        ""
    )

trapStorageSMARTCheckWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 100, 3, 0, 602)
)
if mibBuilder.loadTexts:
    trapStorageSMARTCheckWarning.setStatus(
        ""
    )

trapStorageSMARTCheckCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 100, 3, 0, 603)
)
if mibBuilder.loadTexts:
    trapStorageSMARTCheckCritical.setStatus(
        ""
    )

trapPowerSupplyNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 100, 3, 0, 701)
)
if mibBuilder.loadTexts:
    trapPowerSupplyNormal.setStatus(
        ""
    )

trapPowerSupplyWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 100, 3, 0, 702)
)
if mibBuilder.loadTexts:
    trapPowerSupplyWarning.setStatus(
        ""
    )

trapPowerSupplyCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 100, 3, 0, 703)
)
if mibBuilder.loadTexts:
    trapPowerSupplyCritical.setStatus(
        ""
    )

trapMemoryCeccNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 100, 3, 0, 801)
)
if mibBuilder.loadTexts:
    trapMemoryCeccNormal.setStatus(
        ""
    )

trapMemoryCeccWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 100, 3, 0, 802)
)
if mibBuilder.loadTexts:
    trapMemoryCeccWarning.setStatus(
        ""
    )

trapMemoryCeccCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 100, 3, 0, 803)
)
if mibBuilder.loadTexts:
    trapMemoryCeccCritical.setStatus(
        ""
    )

trapMemoryUeccNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 100, 3, 0, 901)
)
if mibBuilder.loadTexts:
    trapMemoryUeccNormal.setStatus(
        ""
    )

trapMemoryUeccWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 100, 3, 0, 902)
)
if mibBuilder.loadTexts:
    trapMemoryUeccWarning.setStatus(
        ""
    )

trapMemoryUeccCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 100, 3, 0, 903)
)
if mibBuilder.loadTexts:
    trapMemoryUeccCritical.setStatus(
        ""
    )

trapGenericNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 100, 3, 0, 1001)
)
if mibBuilder.loadTexts:
    trapGenericNormal.setStatus(
        ""
    )

trapGenericWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 100, 3, 0, 1002)
)
if mibBuilder.loadTexts:
    trapGenericWarning.setStatus(
        ""
    )

trapGenericCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 100, 3, 0, 1003)
)
if mibBuilder.loadTexts:
    trapGenericCritical.setStatus(
        ""
    )

trapBbpStatusNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 100, 3, 0, 1101)
)
if mibBuilder.loadTexts:
    trapBbpStatusNormal.setStatus(
        ""
    )

trapBbpStatusWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 100, 3, 0, 1102)
)
if mibBuilder.loadTexts:
    trapBbpStatusWarning.setStatus(
        ""
    )

trapBbpStatusCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 100, 3, 0, 1103)
)
if mibBuilder.loadTexts:
    trapBbpStatusCritical.setStatus(
        ""
    )

trapCpuFaultNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 100, 3, 0, 1201)
)
if mibBuilder.loadTexts:
    trapCpuFaultNormal.setStatus(
        ""
    )

trapCpuFaultWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 100, 3, 0, 1202)
)
if mibBuilder.loadTexts:
    trapCpuFaultWarning.setStatus(
        ""
    )

trapCpuFaultCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 100, 3, 0, 1203)
)
if mibBuilder.loadTexts:
    trapCpuFaultCritical.setStatus(
        ""
    )

trapStorageAdapterStatusNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 100, 3, 0, 1301)
)
if mibBuilder.loadTexts:
    trapStorageAdapterStatusNormal.setStatus(
        ""
    )

trapStorageAdapterStatusWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 100, 3, 0, 1302)
)
if mibBuilder.loadTexts:
    trapStorageAdapterStatusWarning.setStatus(
        ""
    )

trapStorageAdapterStatusCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 100, 3, 0, 1303)
)
if mibBuilder.loadTexts:
    trapStorageAdapterStatusCritical.setStatus(
        ""
    )

trapBatteryStatusNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 100, 3, 0, 1401)
)
if mibBuilder.loadTexts:
    trapBatteryStatusNormal.setStatus(
        ""
    )

trapBatteryStatusWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 100, 3, 0, 1402)
)
if mibBuilder.loadTexts:
    trapBatteryStatusWarning.setStatus(
        ""
    )

trapBatteryStatusCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 100, 3, 0, 1403)
)
if mibBuilder.loadTexts:
    trapBatteryStatusCritical.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-SD5-MIB",
    **{"smSuperDoctor5MIB": smSuperDoctor5MIB,
       "sd5Table": sd5Table,
       "sd5Entry": sd5Entry,
       "sd5Idx": sd5Idx,
       "sd5Version": sd5Version,
       "sd5MIBVersion": sd5MIBVersion,
       "cpuTable": cpuTable,
       "cpuEntry": cpuEntry,
       "cpuIndex": cpuIndex,
       "cpuName": cpuName,
       "cpuDescription": cpuDescription,
       "cpuManufacturer": cpuManufacturer,
       "cpuDeviceStatus": cpuDeviceStatus,
       "cpuMaxSpeed": cpuMaxSpeed,
       "cpuCurrentSpeed": cpuCurrentSpeed,
       "cpuLoadingPercentage": cpuLoadingPercentage,
       "cpuCoreEnabled": cpuCoreEnabled,
       "cpuCoreCount": cpuCoreCount,
       "cpuThreadCount": cpuThreadCount,
       "cpuSocketDesignation": cpuSocketDesignation,
       "cpuDeviceVersion": cpuDeviceVersion,
       "cpuDeviceID": cpuDeviceID,
       "cpuID": cpuID,
       "memTable": memTable,
       "memEntry": memEntry,
       "memTag": memTag,
       "memDescription": memDescription,
       "memDeviceStatus": memDeviceStatus,
       "memLabeledBank": memLabeledBank,
       "memDeviceLocator": memDeviceLocator,
       "memModel": memModel,
       "memManufacturer": memManufacturer,
       "memPartNumber": memPartNumber,
       "memSerialNumber": memSerialNumber,
       "memCapacity": memCapacity,
       "memDataWidth": memDataWidth,
       "memTotalWidth": memTotalWidth,
       "memErrorCount": memErrorCount,
       "memECCErrorCount": memECCErrorCount,
       "memUECCErrorCount": memUECCErrorCount,
       "diskTable": diskTable,
       "diskEntry": diskEntry,
       "diskSerialNumber": diskSerialNumber,
       "diskName": diskName,
       "diskVendor": diskVendor,
       "diskSmartStatus": diskSmartStatus,
       "diskModel": diskModel,
       "diskSize": diskSize,
       "diskMediaType": diskMediaType,
       "diskInterfaceType": diskInterfaceType,
       "diskController": diskController,
       "diskSlotID": diskSlotID,
       "sysBIOSTable": sysBIOSTable,
       "sysBIOSEntry": sysBIOSEntry,
       "sysBIOSIndex": sysBIOSIndex,
       "sysBIOSReleaseDate": sysBIOSReleaseDate,
       "sysBIOSVersion": sysBIOSVersion,
       "sysBIOSManufacturer": sysBIOSManufacturer,
       "mbTable": mbTable,
       "mbEntry": mbEntry,
       "mbIndex": mbIndex,
       "mbManufacturer": mbManufacturer,
       "mbProductName": mbProductName,
       "mbVersionName": mbVersionName,
       "mbAssetTag": mbAssetTag,
       "mbSerialNumber": mbSerialNumber,
       "osTable": osTable,
       "osEntry": osEntry,
       "osIndex": osIndex,
       "osName": osName,
       "osVersion": osVersion,
       "osManufacturer": osManufacturer,
       "osSerialNumber": osSerialNumber,
       "osCSDVersion": osCSDVersion,
       "dmiLogTable": dmiLogTable,
       "ceccLogTable": ceccLogTable,
       "ceccLogEntry": ceccLogEntry,
       "ceccLogDatetime": ceccLogDatetime,
       "ceccLogInfo": ceccLogInfo,
       "ceccLogIndex": ceccLogIndex,
       "ueccLogTable": ueccLogTable,
       "ueccLogEntry": ueccLogEntry,
       "ueccLogDatetime": ueccLogDatetime,
       "ueccLogInfo": ueccLogInfo,
       "ueccLogIndex": ueccLogIndex,
       "postLogTable": postLogTable,
       "postLogEntry": postLogEntry,
       "postLogDatetime": postLogDatetime,
       "postLogInfo": postLogInfo,
       "postLogIndex": postLogIndex,
       "cpuLogTable": cpuLogTable,
       "cpuLogEntry": cpuLogEntry,
       "cpuLogDatetime": cpuLogDatetime,
       "cpuLogInfo": cpuLogInfo,
       "cpuLogIndex": cpuLogIndex,
       "raidAdapterTable": raidAdapterTable,
       "raidAdapterEntry": raidAdapterEntry,
       "raidAdapterIndex": raidAdapterIndex,
       "raidAdapterGroup": raidAdapterGroup,
       "raidAdapterId": raidAdapterId,
       "raidAdapterProductName": raidAdapterProductName,
       "raidAdapterSerialNumber": raidAdapterSerialNumber,
       "raidAdapterFWPackageBuild": raidAdapterFWPackageBuild,
       "raidAdapterFWVersion": raidAdapterFWVersion,
       "raidAdapterBIOSVersion": raidAdapterBIOSVersion,
       "raidAdapterVendorId": raidAdapterVendorId,
       "raidAdapterDeviceId": raidAdapterDeviceId,
       "raidAdapterSubVendorId": raidAdapterSubVendorId,
       "raidAdapterSubDeviceId": raidAdapterSubDeviceId,
       "raidIsBBUAbsent": raidIsBBUAbsent,
       "raidIsBBUAbsentIgnored": raidIsBBUAbsentIgnored,
       "raidAdapterAllinoneStatus": raidAdapterAllinoneStatus,
       "raidAdapterAllinoneMsg": raidAdapterAllinoneMsg,
       "raidBBUTable": raidBBUTable,
       "raidBBUEntry": raidBBUEntry,
       "raidBBUIndex": raidBBUIndex,
       "raidAdapterGroup-BBU": raidAdapterGroup_BBU,
       "raidAdapterId-BBU": raidAdapterId_BBU,
       "raidBBUStatus": raidBBUStatus,
       "raidBBUAllinoneStatus": raidBBUAllinoneStatus,
       "raidBBUAllinoneMsg": raidBBUAllinoneMsg,
       "raidVDTable": raidVDTable,
       "raidVDEntry": raidVDEntry,
       "raidVDIndex": raidVDIndex,
       "raidAdapterGroup-VD": raidAdapterGroup_VD,
       "raidAdapterId-VD": raidAdapterId_VD,
       "raidDiskGroupId": raidDiskGroupId,
       "raidVDId": raidVDId,
       "raidVDTargetId": raidVDTargetId,
       "raidVDName": raidVDName,
       "raidVDRaidLevel": raidVDRaidLevel,
       "raidVDSize": raidVDSize,
       "raidVDMirrorDataSize": raidVDMirrorDataSize,
       "raidVDStripSize": raidVDStripSize,
       "raidVDNumDrives": raidVDNumDrives,
       "raidVDSpanDepth": raidVDSpanDepth,
       "raidVDDefaultCachePolicy": raidVDDefaultCachePolicy,
       "raidVDCurrentCachePolicy": raidVDCurrentCachePolicy,
       "raidVDDefaultAccessPolicy": raidVDDefaultAccessPolicy,
       "raidVDCurrentAccessPolicy": raidVDCurrentAccessPolicy,
       "raidVDDiskCachePolicy": raidVDDiskCachePolicy,
       "raidVDEncryptionType": raidVDEncryptionType,
       "raidVDDefaultPSPolicy": raidVDDefaultPSPolicy,
       "raidVDCurrentPSPolicy": raidVDCurrentPSPolicy,
       "raidVDCanSpinUpIn1Min": raidVDCanSpinUpIn1Min,
       "raidVDSupportT10Power": raidVDSupportT10Power,
       "raidVDSupportsMaxPS": raidVDSupportsMaxPS,
       "raidVDBadBlocksExist": raidVDBadBlocksExist,
       "raidVDCached": raidVDCached,
       "raidVDState": raidVDState,
       "raidVDAllinoneStatus": raidVDAllinoneStatus,
       "raidVDAllinoneMsg": raidVDAllinoneMsg,
       "raidPDTable": raidPDTable,
       "raidPDEntry": raidPDEntry,
       "raidPDIndex": raidPDIndex,
       "raidAdapterGroup-PD": raidAdapterGroup_PD,
       "raidAdapterId-PD": raidAdapterId_PD,
       "raidDiskGroupId-PD": raidDiskGroupId_PD,
       "raidPDSlotNumber": raidPDSlotNumber,
       "raidPDFirmwareState": raidPDFirmwareState,
       "raidPDMediaErrorCount": raidPDMediaErrorCount,
       "raidPDOtherErrorCount": raidPDOtherErrorCount,
       "raidPDPredFailCount": raidPDPredFailCount,
       "raidPDLastPredFailEventSeqNo": raidPDLastPredFailEventSeqNo,
       "raidPDRawSize": raidPDRawSize,
       "raidPDDeviceFwLevel": raidPDDeviceFwLevel,
       "raidPDInquiryData": raidPDInquiryData,
       "raidPDDeviceSpeed": raidPDDeviceSpeed,
       "raidPDLinkSpeed": raidPDLinkSpeed,
       "raidPDMediaType": raidPDMediaType,
       "raidPDWriteCache": raidPDWriteCache,
       "raidPDNCQSetting": raidPDNCQSetting,
       "raidPDPort0Linkspeed": raidPDPort0Linkspeed,
       "raidPDPort0Status": raidPDPort0Status,
       "raidPDPort1Linkspeed": raidPDPort1Linkspeed,
       "raidPDPort1Status": raidPDPort1Status,
       "raidPDEnclosureDeviceID": raidPDEnclosureDeviceID,
       "raidPDOpProgress": raidPDOpProgress,
       "raidPDSpan": raidPDSpan,
       "raidPDAllinoneStatus": raidPDAllinoneStatus,
       "raidPDAllinoneMsg": raidPDAllinoneMsg,
       "raidPDModel": raidPDModel,
       "raidPDSerialNumber": raidPDSerialNumber,
       "raidPDFirmwareRevision": raidPDFirmwareRevision,
       "smSD5TrapMIB": smSD5TrapMIB,
       "trapFanNormal": trapFanNormal,
       "trapFanWarning": trapFanWarning,
       "trapFanCritical": trapFanCritical,
       "trapVoltageNormal": trapVoltageNormal,
       "trapVoltageWarning": trapVoltageWarning,
       "trapVoltageCritical": trapVoltageCritical,
       "trapTemperatureNormal": trapTemperatureNormal,
       "trapTemperatureWarning": trapTemperatureWarning,
       "trapTemperatureCritical": trapTemperatureCritical,
       "trapChassisIntrusionCleared": trapChassisIntrusionCleared,
       "trapChassisIntrusion": trapChassisIntrusion,
       "trapStorageSMARTCheckNormal": trapStorageSMARTCheckNormal,
       "trapStorageSMARTCheckWarning": trapStorageSMARTCheckWarning,
       "trapStorageSMARTCheckCritical": trapStorageSMARTCheckCritical,
       "trapPowerSupplyNormal": trapPowerSupplyNormal,
       "trapPowerSupplyWarning": trapPowerSupplyWarning,
       "trapPowerSupplyCritical": trapPowerSupplyCritical,
       "trapMemoryCeccNormal": trapMemoryCeccNormal,
       "trapMemoryCeccWarning": trapMemoryCeccWarning,
       "trapMemoryCeccCritical": trapMemoryCeccCritical,
       "trapMemoryUeccNormal": trapMemoryUeccNormal,
       "trapMemoryUeccWarning": trapMemoryUeccWarning,
       "trapMemoryUeccCritical": trapMemoryUeccCritical,
       "trapGenericNormal": trapGenericNormal,
       "trapGenericWarning": trapGenericWarning,
       "trapGenericCritical": trapGenericCritical,
       "trapBbpStatusNormal": trapBbpStatusNormal,
       "trapBbpStatusWarning": trapBbpStatusWarning,
       "trapBbpStatusCritical": trapBbpStatusCritical,
       "trapCpuFaultNormal": trapCpuFaultNormal,
       "trapCpuFaultWarning": trapCpuFaultWarning,
       "trapCpuFaultCritical": trapCpuFaultCritical,
       "trapStorageAdapterStatusNormal": trapStorageAdapterStatusNormal,
       "trapStorageAdapterStatusWarning": trapStorageAdapterStatusWarning,
       "trapStorageAdapterStatusCritical": trapStorageAdapterStatusCritical,
       "trapBatteryStatusNormal": trapBatteryStatusNormal,
       "trapBatteryStatusWarning": trapBatteryStatusWarning,
       "trapBatteryStatusCritical": trapBatteryStatusCritical}
)
