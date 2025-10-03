# SNMP MIB module (F5-PLATFORM-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\f5\F5-PLATFORM-STATS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:44:10 2025
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

(f5Compliance,
 platform) = mibBuilder.importSymbols(
    "F5-COMMON-SMI-MIB",
    "f5Compliance",
    "platform")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

f5PlatformStats = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PlatformStatsIndex(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )



class String(DisplayString):
    status = "current"
    displayHint = "1t"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )



# MIB Managed Objects in the order of their OIDs

_F5PlatformStatsObjects_ObjectIdentity = ObjectIdentity
f5PlatformStatsObjects = _F5PlatformStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1)
)
_PlatformCpuStatsTable_ObjectIdentity = ObjectIdentity
platformCpuStatsTable = _PlatformCpuStatsTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 1)
)
_CpuProcessorStatsTable_Object = MibTable
cpuProcessorStatsTable = _CpuProcessorStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cpuProcessorStatsTable.setStatus("current")
_CpuProcessorStatsEntry_Object = MibTableRow
cpuProcessorStatsEntry = _CpuProcessorStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 1, 1, 1)
)
cpuProcessorStatsEntry.setIndexNames(
    (0, "F5-PLATFORM-STATS-MIB", "index"),
    (0, "F5-PLATFORM-STATS-MIB", "cpuIndex"),
)
if mibBuilder.loadTexts:
    cpuProcessorStatsEntry.setStatus("current")
_Index_Type = PlatformStatsIndex
_Index_Object = MibTableColumn
index = _Index_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 1, 1, 1, 1),
    _Index_Type()
)
index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    index.setStatus("current")


class _CpuIndex_Type(Integer32):
    """Custom type cpuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpuIndex_Type.__name__ = "Integer32"
_CpuIndex_Object = MibTableColumn
cpuIndex = _CpuIndex_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 1, 1, 1, 2),
    _CpuIndex_Type()
)
cpuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuIndex.setStatus("current")
_CpuCacheSize_Type = String
_CpuCacheSize_Object = MibTableColumn
cpuCacheSize = _CpuCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 1, 1, 1, 3),
    _CpuCacheSize_Type()
)
cpuCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuCacheSize.setStatus("current")
_CpuCoreCnt_Type = String
_CpuCoreCnt_Object = MibTableColumn
cpuCoreCnt = _CpuCoreCnt_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 1, 1, 1, 4),
    _CpuCoreCnt_Type()
)
cpuCoreCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuCoreCnt.setStatus("current")
_CpuFreq_Type = String
_CpuFreq_Object = MibTableColumn
cpuFreq = _CpuFreq_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 1, 1, 1, 5),
    _CpuFreq_Type()
)
cpuFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuFreq.setStatus("current")
_CpuStepping_Type = String
_CpuStepping_Object = MibTableColumn
cpuStepping = _CpuStepping_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 1, 1, 1, 6),
    _CpuStepping_Type()
)
cpuStepping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuStepping.setStatus("current")
_CpuThreadCnt_Type = String
_CpuThreadCnt_Object = MibTableColumn
cpuThreadCnt = _CpuThreadCnt_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 1, 1, 1, 7),
    _CpuThreadCnt_Type()
)
cpuThreadCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuThreadCnt.setStatus("current")
_CpuModelName_Type = String
_CpuModelName_Object = MibTableColumn
cpuModelName = _CpuModelName_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 1, 1, 1, 8),
    _CpuModelName_Type()
)
cpuModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuModelName.setStatus("current")
_CpuUtilizationStatsTable_Object = MibTable
cpuUtilizationStatsTable = _CpuUtilizationStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cpuUtilizationStatsTable.setStatus("current")
_CpuUtilizationStatsEntry_Object = MibTableRow
cpuUtilizationStatsEntry = _CpuUtilizationStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 1, 2, 1)
)
cpuUtilizationStatsEntry.setIndexNames(
    (0, "F5-PLATFORM-STATS-MIB", "index"),
)
if mibBuilder.loadTexts:
    cpuUtilizationStatsEntry.setStatus("current")


class _CpuCore_Type(DisplayString):
    """Custom type cpuCore based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CpuCore_Type.__name__ = "DisplayString"
_CpuCore_Object = MibTableColumn
cpuCore = _CpuCore_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 1, 2, 1, 1),
    _CpuCore_Type()
)
cpuCore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuCore.setStatus("current")
_CpuCurrent_Type = Integer32
_CpuCurrent_Object = MibTableColumn
cpuCurrent = _CpuCurrent_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 1, 2, 1, 2),
    _CpuCurrent_Type()
)
cpuCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuCurrent.setStatus("current")
if mibBuilder.loadTexts:
    cpuCurrent.setUnits("percentage")
_CpuTotal5secAvg_Type = Integer32
_CpuTotal5secAvg_Object = MibTableColumn
cpuTotal5secAvg = _CpuTotal5secAvg_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 1, 2, 1, 3),
    _CpuTotal5secAvg_Type()
)
cpuTotal5secAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTotal5secAvg.setStatus("current")
if mibBuilder.loadTexts:
    cpuTotal5secAvg.setUnits("percentage")
_CpuTotal1minAvg_Type = Integer32
_CpuTotal1minAvg_Object = MibTableColumn
cpuTotal1minAvg = _CpuTotal1minAvg_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 1, 2, 1, 4),
    _CpuTotal1minAvg_Type()
)
cpuTotal1minAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTotal1minAvg.setStatus("current")
if mibBuilder.loadTexts:
    cpuTotal1minAvg.setUnits("percentage")
_CpuTotal5minAvg_Type = Integer32
_CpuTotal5minAvg_Object = MibTableColumn
cpuTotal5minAvg = _CpuTotal5minAvg_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 1, 2, 1, 5),
    _CpuTotal5minAvg_Type()
)
cpuTotal5minAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTotal5minAvg.setStatus("current")
if mibBuilder.loadTexts:
    cpuTotal5minAvg.setUnits("percentage")
_CpuCoreStatsTable_Object = MibTable
cpuCoreStatsTable = _CpuCoreStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cpuCoreStatsTable.setStatus("current")
_CpuCoreStatsEntry_Object = MibTableRow
cpuCoreStatsEntry = _CpuCoreStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 1, 3, 1)
)
cpuCoreStatsEntry.setIndexNames(
    (0, "F5-PLATFORM-STATS-MIB", "index"),
    (0, "F5-PLATFORM-STATS-MIB", "coreIndex"),
)
if mibBuilder.loadTexts:
    cpuCoreStatsEntry.setStatus("current")


class _CoreIndex_Type(Integer32):
    """Custom type coreIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CoreIndex_Type.__name__ = "Integer32"
_CoreIndex_Object = MibTableColumn
coreIndex = _CoreIndex_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 1, 3, 1, 1),
    _CoreIndex_Type()
)
coreIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coreIndex.setStatus("current")


class _CoreName_Type(DisplayString):
    """Custom type coreName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CoreName_Type.__name__ = "DisplayString"
_CoreName_Object = MibTableColumn
coreName = _CoreName_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 1, 3, 1, 2),
    _CoreName_Type()
)
coreName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coreName.setStatus("current")
_CoreCurrent_Type = Integer32
_CoreCurrent_Object = MibTableColumn
coreCurrent = _CoreCurrent_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 1, 3, 1, 3),
    _CoreCurrent_Type()
)
coreCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coreCurrent.setStatus("current")
if mibBuilder.loadTexts:
    coreCurrent.setUnits("percentage")
_CoreTotal5secAvg_Type = Integer32
_CoreTotal5secAvg_Object = MibTableColumn
coreTotal5secAvg = _CoreTotal5secAvg_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 1, 3, 1, 4),
    _CoreTotal5secAvg_Type()
)
coreTotal5secAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coreTotal5secAvg.setStatus("current")
if mibBuilder.loadTexts:
    coreTotal5secAvg.setUnits("percentage")
_CoreTotal1minAvg_Type = Integer32
_CoreTotal1minAvg_Object = MibTableColumn
coreTotal1minAvg = _CoreTotal1minAvg_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 1, 3, 1, 5),
    _CoreTotal1minAvg_Type()
)
coreTotal1minAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coreTotal1minAvg.setStatus("current")
if mibBuilder.loadTexts:
    coreTotal1minAvg.setUnits("percentage")
_CoreTotal5minAvg_Type = Integer32
_CoreTotal5minAvg_Object = MibTableColumn
coreTotal5minAvg = _CoreTotal5minAvg_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 1, 3, 1, 6),
    _CoreTotal5minAvg_Type()
)
coreTotal5minAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coreTotal5minAvg.setStatus("current")
if mibBuilder.loadTexts:
    coreTotal5minAvg.setUnits("percentage")
_PlatformDiskStatsTable_ObjectIdentity = ObjectIdentity
platformDiskStatsTable = _PlatformDiskStatsTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 2)
)
_DiskInfoTable_Object = MibTable
diskInfoTable = _DiskInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    diskInfoTable.setStatus("current")
_DiskInfoEntry_Object = MibTableRow
diskInfoEntry = _DiskInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 2, 1, 1)
)
diskInfoEntry.setIndexNames(
    (0, "F5-PLATFORM-STATS-MIB", "index"),
    (0, "F5-PLATFORM-STATS-MIB", "diskName"),
)
if mibBuilder.loadTexts:
    diskInfoEntry.setStatus("current")


class _DiskName_Type(DisplayString):
    """Custom type diskName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_DiskName_Type.__name__ = "DisplayString"
_DiskName_Object = MibTableColumn
diskName = _DiskName_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 2, 1, 1, 2),
    _DiskName_Type()
)
diskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskName.setStatus("current")


class _DiskModel_Type(DisplayString):
    """Custom type diskModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_DiskModel_Type.__name__ = "DisplayString"
_DiskModel_Object = MibTableColumn
diskModel = _DiskModel_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 2, 1, 1, 3),
    _DiskModel_Type()
)
diskModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskModel.setStatus("current")


class _DiskVendor_Type(DisplayString):
    """Custom type diskVendor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_DiskVendor_Type.__name__ = "DisplayString"
_DiskVendor_Object = MibTableColumn
diskVendor = _DiskVendor_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 2, 1, 1, 4),
    _DiskVendor_Type()
)
diskVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskVendor.setStatus("current")


class _DiskVersion_Type(DisplayString):
    """Custom type diskVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_DiskVersion_Type.__name__ = "DisplayString"
_DiskVersion_Object = MibTableColumn
diskVersion = _DiskVersion_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 2, 1, 1, 5),
    _DiskVersion_Type()
)
diskVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskVersion.setStatus("current")


class _DiskSerialNo_Type(DisplayString):
    """Custom type diskSerialNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_DiskSerialNo_Type.__name__ = "DisplayString"
_DiskSerialNo_Object = MibTableColumn
diskSerialNo = _DiskSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 2, 1, 1, 6),
    _DiskSerialNo_Type()
)
diskSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskSerialNo.setStatus("current")


class _DiskSize_Type(DisplayString):
    """Custom type diskSize based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_DiskSize_Type.__name__ = "DisplayString"
_DiskSize_Object = MibTableColumn
diskSize = _DiskSize_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 2, 1, 1, 7),
    _DiskSize_Type()
)
diskSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskSize.setStatus("current")


class _DiskType_Type(DisplayString):
    """Custom type diskType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_DiskType_Type.__name__ = "DisplayString"
_DiskType_Object = MibTableColumn
diskType = _DiskType_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 2, 1, 1, 8),
    _DiskType_Type()
)
diskType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskType.setStatus("current")
_DiskUtilizationStatsTable_Object = MibTable
diskUtilizationStatsTable = _DiskUtilizationStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    diskUtilizationStatsTable.setStatus("current")
_DiskUtilizationStatsEntry_Object = MibTableRow
diskUtilizationStatsEntry = _DiskUtilizationStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 2, 2, 1)
)
diskUtilizationStatsEntry.setIndexNames(
    (0, "F5-PLATFORM-STATS-MIB", "index"),
    (0, "F5-PLATFORM-STATS-MIB", "diskName"),
)
if mibBuilder.loadTexts:
    diskUtilizationStatsEntry.setStatus("current")


class _DiskPercentageUsed_Type(Integer32):
    """Custom type diskPercentageUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DiskPercentageUsed_Type.__name__ = "Integer32"
_DiskPercentageUsed_Object = MibTableColumn
diskPercentageUsed = _DiskPercentageUsed_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 2, 2, 1, 3),
    _DiskPercentageUsed_Type()
)
diskPercentageUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskPercentageUsed.setStatus("current")
if mibBuilder.loadTexts:
    diskPercentageUsed.setUnits("percentage")
_DiskTotalIops_Type = Counter64
_DiskTotalIops_Object = MibTableColumn
diskTotalIops = _DiskTotalIops_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 2, 2, 1, 4),
    _DiskTotalIops_Type()
)
diskTotalIops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskTotalIops.setStatus("current")
if mibBuilder.loadTexts:
    diskTotalIops.setUnits("IOPs")
_DiskReadIops_Type = Counter64
_DiskReadIops_Object = MibTableColumn
diskReadIops = _DiskReadIops_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 2, 2, 1, 5),
    _DiskReadIops_Type()
)
diskReadIops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskReadIops.setStatus("current")
if mibBuilder.loadTexts:
    diskReadIops.setUnits("IOPs")
_DiskReadMerged_Type = Counter64
_DiskReadMerged_Object = MibTableColumn
diskReadMerged = _DiskReadMerged_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 2, 2, 1, 6),
    _DiskReadMerged_Type()
)
diskReadMerged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskReadMerged.setStatus("current")
_DiskReadBytes_Type = Counter64
_DiskReadBytes_Object = MibTableColumn
diskReadBytes = _DiskReadBytes_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 2, 2, 1, 7),
    _DiskReadBytes_Type()
)
diskReadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskReadBytes.setStatus("current")
if mibBuilder.loadTexts:
    diskReadBytes.setUnits("bytes")
_DiskReadLatencyMs_Type = Counter64
_DiskReadLatencyMs_Object = MibTableColumn
diskReadLatencyMs = _DiskReadLatencyMs_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 2, 2, 1, 8),
    _DiskReadLatencyMs_Type()
)
diskReadLatencyMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskReadLatencyMs.setStatus("current")
if mibBuilder.loadTexts:
    diskReadLatencyMs.setUnits("ms")
_DiskWriteIops_Type = Counter64
_DiskWriteIops_Object = MibTableColumn
diskWriteIops = _DiskWriteIops_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 2, 2, 1, 9),
    _DiskWriteIops_Type()
)
diskWriteIops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskWriteIops.setStatus("current")
if mibBuilder.loadTexts:
    diskWriteIops.setUnits("IOPs")
_DiskWriteMerged_Type = Counter64
_DiskWriteMerged_Object = MibTableColumn
diskWriteMerged = _DiskWriteMerged_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 2, 2, 1, 10),
    _DiskWriteMerged_Type()
)
diskWriteMerged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskWriteMerged.setStatus("current")
_DiskWriteBytes_Type = Counter64
_DiskWriteBytes_Object = MibTableColumn
diskWriteBytes = _DiskWriteBytes_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 2, 2, 1, 11),
    _DiskWriteBytes_Type()
)
diskWriteBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskWriteBytes.setStatus("current")
if mibBuilder.loadTexts:
    diskWriteBytes.setUnits("bytes")
_DiskWriteLatencyMs_Type = Counter64
_DiskWriteLatencyMs_Object = MibTableColumn
diskWriteLatencyMs = _DiskWriteLatencyMs_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 2, 2, 1, 12),
    _DiskWriteLatencyMs_Type()
)
diskWriteLatencyMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskWriteLatencyMs.setStatus("current")
if mibBuilder.loadTexts:
    diskWriteLatencyMs.setUnits("ms")
_PlatformTemperatureTable_ObjectIdentity = ObjectIdentity
platformTemperatureTable = _PlatformTemperatureTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 3)
)
_TemperatureStatsTable_Object = MibTable
temperatureStatsTable = _TemperatureStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    temperatureStatsTable.setStatus("current")
_TemperatureStatsEntry_Object = MibTableRow
temperatureStatsEntry = _TemperatureStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 3, 1, 1)
)
temperatureStatsEntry.setIndexNames(
    (0, "F5-PLATFORM-STATS-MIB", "index"),
)
if mibBuilder.loadTexts:
    temperatureStatsEntry.setStatus("current")


class _TempCurrent_Type(DisplayString):
    """Custom type tempCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_TempCurrent_Type.__name__ = "DisplayString"
_TempCurrent_Object = MibTableColumn
tempCurrent = _TempCurrent_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 3, 1, 1, 2),
    _TempCurrent_Type()
)
tempCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempCurrent.setStatus("current")
if mibBuilder.loadTexts:
    tempCurrent.setUnits("centigrade")


class _TempAverage_Type(DisplayString):
    """Custom type tempAverage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_TempAverage_Type.__name__ = "DisplayString"
_TempAverage_Object = MibTableColumn
tempAverage = _TempAverage_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 3, 1, 1, 3),
    _TempAverage_Type()
)
tempAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempAverage.setStatus("current")
if mibBuilder.loadTexts:
    tempAverage.setUnits("centigrade")


class _TempMinimum_Type(DisplayString):
    """Custom type tempMinimum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_TempMinimum_Type.__name__ = "DisplayString"
_TempMinimum_Object = MibTableColumn
tempMinimum = _TempMinimum_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 3, 1, 1, 4),
    _TempMinimum_Type()
)
tempMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempMinimum.setStatus("current")
if mibBuilder.loadTexts:
    tempMinimum.setUnits("centigrade")


class _TempMaximum_Type(DisplayString):
    """Custom type tempMaximum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_TempMaximum_Type.__name__ = "DisplayString"
_TempMaximum_Object = MibTableColumn
tempMaximum = _TempMaximum_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 3, 1, 1, 5),
    _TempMaximum_Type()
)
tempMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempMaximum.setStatus("current")
if mibBuilder.loadTexts:
    tempMaximum.setUnits("centigrade")
_PlatformMemoryStatsTable_ObjectIdentity = ObjectIdentity
platformMemoryStatsTable = _PlatformMemoryStatsTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 4)
)
_MemoryStatsTable_Object = MibTable
memoryStatsTable = _MemoryStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    memoryStatsTable.setStatus("current")
_MemoryStatsEntry_Object = MibTableRow
memoryStatsEntry = _MemoryStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 4, 1, 1)
)
memoryStatsEntry.setIndexNames(
    (0, "F5-PLATFORM-STATS-MIB", "index"),
)
if mibBuilder.loadTexts:
    memoryStatsEntry.setStatus("current")
_MemAvailable_Type = Counter64
_MemAvailable_Object = MibTableColumn
memAvailable = _MemAvailable_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 4, 1, 1, 2),
    _MemAvailable_Type()
)
memAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memAvailable.setStatus("current")
if mibBuilder.loadTexts:
    memAvailable.setUnits("bytes")
_MemFree_Type = Counter64
_MemFree_Object = MibTableColumn
memFree = _MemFree_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 4, 1, 1, 3),
    _MemFree_Type()
)
memFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memFree.setStatus("current")
if mibBuilder.loadTexts:
    memFree.setUnits("bytes")


class _MemPercentageUsed_Type(Integer32):
    """Custom type memPercentageUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MemPercentageUsed_Type.__name__ = "Integer32"
_MemPercentageUsed_Object = MibTableColumn
memPercentageUsed = _MemPercentageUsed_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 4, 1, 1, 4),
    _MemPercentageUsed_Type()
)
memPercentageUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memPercentageUsed.setStatus("current")
if mibBuilder.loadTexts:
    memPercentageUsed.setUnits("percentage")
_MemPlatformTotal_Type = Counter64
_MemPlatformTotal_Object = MibTableColumn
memPlatformTotal = _MemPlatformTotal_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 4, 1, 1, 5),
    _MemPlatformTotal_Type()
)
memPlatformTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memPlatformTotal.setStatus("current")
if mibBuilder.loadTexts:
    memPlatformTotal.setUnits("bytes")
_MemPlatformUsed_Type = Counter64
_MemPlatformUsed_Object = MibTableColumn
memPlatformUsed = _MemPlatformUsed_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 4, 1, 1, 6),
    _MemPlatformUsed_Type()
)
memPlatformUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memPlatformUsed.setStatus("current")
if mibBuilder.loadTexts:
    memPlatformUsed.setUnits("bytes")
_PlatformFpgaTable_ObjectIdentity = ObjectIdentity
platformFpgaTable = _PlatformFpgaTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 5)
)
_FpgaTable_Object = MibTable
fpgaTable = _FpgaTable_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    fpgaTable.setStatus("current")
_FpgaEntry_Object = MibTableRow
fpgaEntry = _FpgaEntry_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 5, 1, 1)
)
fpgaEntry.setIndexNames(
    (0, "F5-PLATFORM-STATS-MIB", "index"),
    (0, "F5-PLATFORM-STATS-MIB", "fpgaIndex"),
)
if mibBuilder.loadTexts:
    fpgaEntry.setStatus("current")


class _FpgaIndex_Type(DisplayString):
    """Custom type fpgaIndex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_FpgaIndex_Type.__name__ = "DisplayString"
_FpgaIndex_Object = MibTableColumn
fpgaIndex = _FpgaIndex_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 5, 1, 1, 1),
    _FpgaIndex_Type()
)
fpgaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpgaIndex.setStatus("current")


class _FpgaVersion_Type(DisplayString):
    """Custom type fpgaVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_FpgaVersion_Type.__name__ = "DisplayString"
_FpgaVersion_Object = MibTableColumn
fpgaVersion = _FpgaVersion_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 5, 1, 1, 2),
    _FpgaVersion_Type()
)
fpgaVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpgaVersion.setStatus("current")
_PlatformFwTable_ObjectIdentity = ObjectIdentity
platformFwTable = _PlatformFwTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 6)
)
_FwTable_Object = MibTable
fwTable = _FwTable_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 6, 1)
)
if mibBuilder.loadTexts:
    fwTable.setStatus("current")
_FwEntry_Object = MibTableRow
fwEntry = _FwEntry_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 6, 1, 1)
)
fwEntry.setIndexNames(
    (0, "F5-PLATFORM-STATS-MIB", "index"),
    (0, "F5-PLATFORM-STATS-MIB", "fwName"),
)
if mibBuilder.loadTexts:
    fwEntry.setStatus("current")


class _FwName_Type(DisplayString):
    """Custom type fwName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_FwName_Type.__name__ = "DisplayString"
_FwName_Object = MibTableColumn
fwName = _FwName_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 6, 1, 1, 1),
    _FwName_Type()
)
fwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwName.setStatus("current")


class _FwVersion_Type(DisplayString):
    """Custom type fwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_FwVersion_Type.__name__ = "DisplayString"
_FwVersion_Object = MibTableColumn
fwVersion = _FwVersion_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 6, 1, 1, 2),
    _FwVersion_Type()
)
fwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwVersion.setStatus("current")
_Configurable_Type = TruthValue
_Configurable_Object = MibTableColumn
configurable = _Configurable_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 6, 1, 1, 3),
    _Configurable_Type()
)
configurable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configurable.setStatus("current")


class _FwUpdateStatus_Type(DisplayString):
    """Custom type fwUpdateStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_FwUpdateStatus_Type.__name__ = "DisplayString"
_FwUpdateStatus_Object = MibTableColumn
fwUpdateStatus = _FwUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 6, 1, 1, 4),
    _FwUpdateStatus_Type()
)
fwUpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwUpdateStatus.setStatus("current")
_PlatformFantrayTable_ObjectIdentity = ObjectIdentity
platformFantrayTable = _PlatformFantrayTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 7)
)
_FantrayStatsTable_Object = MibTable
fantrayStatsTable = _FantrayStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 7, 1)
)
if mibBuilder.loadTexts:
    fantrayStatsTable.setStatus("current")
_FantrayStatsEntry_Object = MibTableRow
fantrayStatsEntry = _FantrayStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 7, 1, 1)
)
fantrayStatsEntry.setIndexNames(
    (0, "F5-PLATFORM-STATS-MIB", "index"),
)
if mibBuilder.loadTexts:
    fantrayStatsEntry.setStatus("current")
_Fan_1_speed_Type = Integer32
_Fan_1_speed_Object = MibTableColumn
fan_1_speed = _Fan_1_speed_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 7, 1, 1, 1),
    _Fan_1_speed_Type()
)
fan_1_speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan_1_speed.setStatus("current")
if mibBuilder.loadTexts:
    fan_1_speed.setUnits("RPM")
_Fan_2_speed_Type = Integer32
_Fan_2_speed_Object = MibTableColumn
fan_2_speed = _Fan_2_speed_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 7, 1, 1, 2),
    _Fan_2_speed_Type()
)
fan_2_speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan_2_speed.setStatus("current")
if mibBuilder.loadTexts:
    fan_2_speed.setUnits("RPM")
_Fan_3_speed_Type = Integer32
_Fan_3_speed_Object = MibTableColumn
fan_3_speed = _Fan_3_speed_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 7, 1, 1, 3),
    _Fan_3_speed_Type()
)
fan_3_speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan_3_speed.setStatus("current")
if mibBuilder.loadTexts:
    fan_3_speed.setUnits("RPM")
_Fan_4_speed_Type = Integer32
_Fan_4_speed_Object = MibTableColumn
fan_4_speed = _Fan_4_speed_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 7, 1, 1, 4),
    _Fan_4_speed_Type()
)
fan_4_speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan_4_speed.setStatus("current")
if mibBuilder.loadTexts:
    fan_4_speed.setUnits("RPM")
_Fan_5_speed_Type = Integer32
_Fan_5_speed_Object = MibTableColumn
fan_5_speed = _Fan_5_speed_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 7, 1, 1, 5),
    _Fan_5_speed_Type()
)
fan_5_speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan_5_speed.setStatus("current")
if mibBuilder.loadTexts:
    fan_5_speed.setUnits("RPM")
_Fan_6_speed_Type = Integer32
_Fan_6_speed_Object = MibTableColumn
fan_6_speed = _Fan_6_speed_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 7, 1, 1, 6),
    _Fan_6_speed_Type()
)
fan_6_speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan_6_speed.setStatus("current")
if mibBuilder.loadTexts:
    fan_6_speed.setUnits("RPM")
_Fan_7_speed_Type = Integer32
_Fan_7_speed_Object = MibTableColumn
fan_7_speed = _Fan_7_speed_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 7, 1, 1, 7),
    _Fan_7_speed_Type()
)
fan_7_speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan_7_speed.setStatus("current")
if mibBuilder.loadTexts:
    fan_7_speed.setUnits("RPM")
_Fan_8_speed_Type = Integer32
_Fan_8_speed_Object = MibTableColumn
fan_8_speed = _Fan_8_speed_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 7, 1, 1, 8),
    _Fan_8_speed_Type()
)
fan_8_speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan_8_speed.setStatus("current")
if mibBuilder.loadTexts:
    fan_8_speed.setUnits("RPM")
_Fan_9_speed_Type = Integer32
_Fan_9_speed_Object = MibTableColumn
fan_9_speed = _Fan_9_speed_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 7, 1, 1, 9),
    _Fan_9_speed_Type()
)
fan_9_speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan_9_speed.setStatus("current")
if mibBuilder.loadTexts:
    fan_9_speed.setUnits("RPM")
_Fan_10_speed_Type = Integer32
_Fan_10_speed_Object = MibTableColumn
fan_10_speed = _Fan_10_speed_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 7, 1, 1, 10),
    _Fan_10_speed_Type()
)
fan_10_speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan_10_speed.setStatus("current")
if mibBuilder.loadTexts:
    fan_10_speed.setUnits("RPM")
_Fan_11_speed_Type = Integer32
_Fan_11_speed_Object = MibTableColumn
fan_11_speed = _Fan_11_speed_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 7, 1, 1, 11),
    _Fan_11_speed_Type()
)
fan_11_speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan_11_speed.setStatus("current")
if mibBuilder.loadTexts:
    fan_11_speed.setUnits("RPM")
_Fan_12_speed_Type = Integer32
_Fan_12_speed_Object = MibTableColumn
fan_12_speed = _Fan_12_speed_Object(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 1, 7, 1, 1, 12),
    _Fan_12_speed_Type()
)
fan_12_speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan_12_speed.setStatus("current")
if mibBuilder.loadTexts:
    fan_12_speed.setUnits("RPM")
_PlatformConformance_ObjectIdentity = ObjectIdentity
platformConformance = _PlatformConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 2)
)
_PlatformGroups_ObjectIdentity = ObjectIdentity
platformGroups = _PlatformGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 2, 1)
)
_PlatformCompliances_ObjectIdentity = ObjectIdentity
platformCompliances = _PlatformCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 2, 2)
)

# Managed Objects groups

platformCPUGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 2, 1, 1)
)
platformCPUGroup.setObjects(
      *(("F5-PLATFORM-STATS-MIB", "index"),
        ("F5-PLATFORM-STATS-MIB", "cpuIndex"),
        ("F5-PLATFORM-STATS-MIB", "cpuCacheSize"),
        ("F5-PLATFORM-STATS-MIB", "cpuCoreCnt"),
        ("F5-PLATFORM-STATS-MIB", "cpuFreq"),
        ("F5-PLATFORM-STATS-MIB", "cpuStepping"),
        ("F5-PLATFORM-STATS-MIB", "cpuThreadCnt"),
        ("F5-PLATFORM-STATS-MIB", "cpuModelName"),
        ("F5-PLATFORM-STATS-MIB", "cpuCore"),
        ("F5-PLATFORM-STATS-MIB", "cpuCurrent"),
        ("F5-PLATFORM-STATS-MIB", "cpuTotal5secAvg"),
        ("F5-PLATFORM-STATS-MIB", "cpuTotal1minAvg"),
        ("F5-PLATFORM-STATS-MIB", "cpuTotal5minAvg"),
        ("F5-PLATFORM-STATS-MIB", "coreIndex"),
        ("F5-PLATFORM-STATS-MIB", "coreCurrent"),
        ("F5-PLATFORM-STATS-MIB", "coreTotal5secAvg"),
        ("F5-PLATFORM-STATS-MIB", "coreTotal1minAvg"),
        ("F5-PLATFORM-STATS-MIB", "coreTotal5minAvg"))
)
if mibBuilder.loadTexts:
    platformCPUGroup.setStatus("current")

platformDiskGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 2, 1, 2)
)
platformDiskGroup.setObjects(
      *(("F5-PLATFORM-STATS-MIB", "diskName"),
        ("F5-PLATFORM-STATS-MIB", "diskModel"),
        ("F5-PLATFORM-STATS-MIB", "diskVendor"),
        ("F5-PLATFORM-STATS-MIB", "diskVersion"),
        ("F5-PLATFORM-STATS-MIB", "diskSerialNo"),
        ("F5-PLATFORM-STATS-MIB", "diskSize"),
        ("F5-PLATFORM-STATS-MIB", "diskType"),
        ("F5-PLATFORM-STATS-MIB", "diskPercentageUsed"),
        ("F5-PLATFORM-STATS-MIB", "diskTotalIops"),
        ("F5-PLATFORM-STATS-MIB", "diskReadIops"),
        ("F5-PLATFORM-STATS-MIB", "diskReadMerged"),
        ("F5-PLATFORM-STATS-MIB", "diskReadBytes"),
        ("F5-PLATFORM-STATS-MIB", "diskReadLatencyMs"),
        ("F5-PLATFORM-STATS-MIB", "diskWriteIops"),
        ("F5-PLATFORM-STATS-MIB", "diskWriteMerged"),
        ("F5-PLATFORM-STATS-MIB", "diskWriteBytes"),
        ("F5-PLATFORM-STATS-MIB", "diskWriteLatencyMs"))
)
if mibBuilder.loadTexts:
    platformDiskGroup.setStatus("current")

platformTempGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 2, 1, 3)
)
platformTempGroup.setObjects(
      *(("F5-PLATFORM-STATS-MIB", "tempCurrent"),
        ("F5-PLATFORM-STATS-MIB", "tempAverage"),
        ("F5-PLATFORM-STATS-MIB", "tempMinimum"),
        ("F5-PLATFORM-STATS-MIB", "tempMaximum"))
)
if mibBuilder.loadTexts:
    platformTempGroup.setStatus("current")

platformMemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 2, 1, 4)
)
platformMemGroup.setObjects(
      *(("F5-PLATFORM-STATS-MIB", "memAvailable"),
        ("F5-PLATFORM-STATS-MIB", "memFree"),
        ("F5-PLATFORM-STATS-MIB", "memPercentageUsed"),
        ("F5-PLATFORM-STATS-MIB", "memPlatformTotal"),
        ("F5-PLATFORM-STATS-MIB", "memPlatformUsed"))
)
if mibBuilder.loadTexts:
    platformMemGroup.setStatus("current")

platformFpgaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 2, 1, 5)
)
platformFpgaGroup.setObjects(
      *(("F5-PLATFORM-STATS-MIB", "fpgaIndex"),
        ("F5-PLATFORM-STATS-MIB", "fpgaVersion"))
)
if mibBuilder.loadTexts:
    platformFpgaGroup.setStatus("current")

platformFwVersionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 2, 1, 6)
)
platformFwVersionGroup.setObjects(
      *(("F5-PLATFORM-STATS-MIB", "fwName"),
        ("F5-PLATFORM-STATS-MIB", "fwVersion"),
        ("F5-PLATFORM-STATS-MIB", "configurable"),
        ("F5-PLATFORM-STATS-MIB", "fwUpdateStatus"))
)
if mibBuilder.loadTexts:
    platformFwVersionGroup.setStatus("current")

platformFantrayGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 2, 1, 7)
)
platformFantrayGroup.setObjects(
      *(("F5-PLATFORM-STATS-MIB", "fan-1-speed"),
        ("F5-PLATFORM-STATS-MIB", "fan-2-speed"),
        ("F5-PLATFORM-STATS-MIB", "fan-3-speed"),
        ("F5-PLATFORM-STATS-MIB", "fan-4-speed"),
        ("F5-PLATFORM-STATS-MIB", "fan-5-speed"),
        ("F5-PLATFORM-STATS-MIB", "fan-6-speed"),
        ("F5-PLATFORM-STATS-MIB", "fan-7-speed"),
        ("F5-PLATFORM-STATS-MIB", "fan-8-speed"),
        ("F5-PLATFORM-STATS-MIB", "fan-9-speed"),
        ("F5-PLATFORM-STATS-MIB", "fan-10-speed"),
        ("F5-PLATFORM-STATS-MIB", "fan-11-speed"),
        ("F5-PLATFORM-STATS-MIB", "fan-12-speed"))
)
if mibBuilder.loadTexts:
    platformFantrayGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

platformCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 12276, 1, 2, 2, 2, 1)
)
platformCompliance.setObjects(
      *(("F5-PLATFORM-STATS-MIB", "platformCPUGroup"),
        ("F5-PLATFORM-STATS-MIB", "platformDiskGroup"),
        ("F5-PLATFORM-STATS-MIB", "platformTempGroup"),
        ("F5-PLATFORM-STATS-MIB", "platformMemGroup"),
        ("F5-PLATFORM-STATS-MIB", "platformFpgaGroup"),
        ("F5-PLATFORM-STATS-MIB", "platformFwVersionGroup"),
        ("F5-PLATFORM-STATS-MIB", "platformFantrayGroup"))
)
if mibBuilder.loadTexts:
    platformCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F5-PLATFORM-STATS-MIB",
    **{"PlatformStatsIndex": PlatformStatsIndex,
       "String": String,
       "f5PlatformStats": f5PlatformStats,
       "f5PlatformStatsObjects": f5PlatformStatsObjects,
       "platformCpuStatsTable": platformCpuStatsTable,
       "cpuProcessorStatsTable": cpuProcessorStatsTable,
       "cpuProcessorStatsEntry": cpuProcessorStatsEntry,
       "index": index,
       "cpuIndex": cpuIndex,
       "cpuCacheSize": cpuCacheSize,
       "cpuCoreCnt": cpuCoreCnt,
       "cpuFreq": cpuFreq,
       "cpuStepping": cpuStepping,
       "cpuThreadCnt": cpuThreadCnt,
       "cpuModelName": cpuModelName,
       "cpuUtilizationStatsTable": cpuUtilizationStatsTable,
       "cpuUtilizationStatsEntry": cpuUtilizationStatsEntry,
       "cpuCore": cpuCore,
       "cpuCurrent": cpuCurrent,
       "cpuTotal5secAvg": cpuTotal5secAvg,
       "cpuTotal1minAvg": cpuTotal1minAvg,
       "cpuTotal5minAvg": cpuTotal5minAvg,
       "cpuCoreStatsTable": cpuCoreStatsTable,
       "cpuCoreStatsEntry": cpuCoreStatsEntry,
       "coreIndex": coreIndex,
       "coreName": coreName,
       "coreCurrent": coreCurrent,
       "coreTotal5secAvg": coreTotal5secAvg,
       "coreTotal1minAvg": coreTotal1minAvg,
       "coreTotal5minAvg": coreTotal5minAvg,
       "platformDiskStatsTable": platformDiskStatsTable,
       "diskInfoTable": diskInfoTable,
       "diskInfoEntry": diskInfoEntry,
       "diskName": diskName,
       "diskModel": diskModel,
       "diskVendor": diskVendor,
       "diskVersion": diskVersion,
       "diskSerialNo": diskSerialNo,
       "diskSize": diskSize,
       "diskType": diskType,
       "diskUtilizationStatsTable": diskUtilizationStatsTable,
       "diskUtilizationStatsEntry": diskUtilizationStatsEntry,
       "diskPercentageUsed": diskPercentageUsed,
       "diskTotalIops": diskTotalIops,
       "diskReadIops": diskReadIops,
       "diskReadMerged": diskReadMerged,
       "diskReadBytes": diskReadBytes,
       "diskReadLatencyMs": diskReadLatencyMs,
       "diskWriteIops": diskWriteIops,
       "diskWriteMerged": diskWriteMerged,
       "diskWriteBytes": diskWriteBytes,
       "diskWriteLatencyMs": diskWriteLatencyMs,
       "platformTemperatureTable": platformTemperatureTable,
       "temperatureStatsTable": temperatureStatsTable,
       "temperatureStatsEntry": temperatureStatsEntry,
       "tempCurrent": tempCurrent,
       "tempAverage": tempAverage,
       "tempMinimum": tempMinimum,
       "tempMaximum": tempMaximum,
       "platformMemoryStatsTable": platformMemoryStatsTable,
       "memoryStatsTable": memoryStatsTable,
       "memoryStatsEntry": memoryStatsEntry,
       "memAvailable": memAvailable,
       "memFree": memFree,
       "memPercentageUsed": memPercentageUsed,
       "memPlatformTotal": memPlatformTotal,
       "memPlatformUsed": memPlatformUsed,
       "platformFpgaTable": platformFpgaTable,
       "fpgaTable": fpgaTable,
       "fpgaEntry": fpgaEntry,
       "fpgaIndex": fpgaIndex,
       "fpgaVersion": fpgaVersion,
       "platformFwTable": platformFwTable,
       "fwTable": fwTable,
       "fwEntry": fwEntry,
       "fwName": fwName,
       "fwVersion": fwVersion,
       "configurable": configurable,
       "fwUpdateStatus": fwUpdateStatus,
       "platformFantrayTable": platformFantrayTable,
       "fantrayStatsTable": fantrayStatsTable,
       "fantrayStatsEntry": fantrayStatsEntry,
       "fan-1-speed": fan_1_speed,
       "fan-2-speed": fan_2_speed,
       "fan-3-speed": fan_3_speed,
       "fan-4-speed": fan_4_speed,
       "fan-5-speed": fan_5_speed,
       "fan-6-speed": fan_6_speed,
       "fan-7-speed": fan_7_speed,
       "fan-8-speed": fan_8_speed,
       "fan-9-speed": fan_9_speed,
       "fan-10-speed": fan_10_speed,
       "fan-11-speed": fan_11_speed,
       "fan-12-speed": fan_12_speed,
       "platformConformance": platformConformance,
       "platformGroups": platformGroups,
       "platformCPUGroup": platformCPUGroup,
       "platformDiskGroup": platformDiskGroup,
       "platformTempGroup": platformTempGroup,
       "platformMemGroup": platformMemGroup,
       "platformFpgaGroup": platformFpgaGroup,
       "platformFwVersionGroup": platformFwVersionGroup,
       "platformFantrayGroup": platformFantrayGroup,
       "platformCompliances": platformCompliances,
       "platformCompliance": platformCompliance}
)
