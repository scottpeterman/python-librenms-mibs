# SNMP MIB module (NPT-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ribbon\NPT-SYSTEM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:23:19 2025
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

(nptSystem,) = mibBuilder.importSymbols(
    "NPT-ROOT-MIB",
    "nptSystem")

(NPTSNMPEnable,
 NPTSNMPYesOrNo,
 NPTSfpFiberType,
 NPTSfpLOSStatus,
 NPTSfpLaserTrStatus,
 NPTSfpLineCode,
 NPTSfpOperStatus) = mibBuilder.importSymbols(
    "NPT-TC-MIB",
    "NPTSNMPEnable",
    "NPTSNMPYesOrNo",
    "NPTSfpFiberType",
    "NPTSfpLOSStatus",
    "NPTSfpLaserTrStatus",
    "NPTSfpLineCode",
    "NPTSfpOperStatus")

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

nptSystemModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    nptSystemModule.setRevisions(
        ("2011-05-24 09:45",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NptMibVersion_Type = DisplayString
_NptMibVersion_Object = MibScalar
nptMibVersion = _NptMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 1),
    _NptMibVersion_Type()
)
nptMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptMibVersion.setStatus("current")
_NptNESoftwareVersion_Type = DisplayString
_NptNESoftwareVersion_Object = MibScalar
nptNESoftwareVersion = _NptNESoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 2),
    _NptNESoftwareVersion_Type()
)
nptNESoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptNESoftwareVersion.setStatus("current")
_NptBoardInfoTable_Object = MibTable
nptBoardInfoTable = _NptBoardInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    nptBoardInfoTable.setStatus("current")
_NptBoardInfoEntry_Object = MibTableRow
nptBoardInfoEntry = _NptBoardInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 3, 1)
)
nptBoardInfoEntry.setIndexNames(
    (0, "NPT-SYSTEM-MIB", "nptSlotId"),
)
if mibBuilder.loadTexts:
    nptBoardInfoEntry.setStatus("current")


class _NptSlotId_Type(Integer32):
    """Custom type nptSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NptSlotId_Type.__name__ = "Integer32"
_NptSlotId_Object = MibTableColumn
nptSlotId = _NptSlotId_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 3, 1, 1),
    _NptSlotId_Type()
)
nptSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptSlotId.setStatus("current")
_NptPhysicalBoardType_Type = DisplayString
_NptPhysicalBoardType_Object = MibTableColumn
nptPhysicalBoardType = _NptPhysicalBoardType_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 3, 1, 2),
    _NptPhysicalBoardType_Type()
)
nptPhysicalBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptPhysicalBoardType.setStatus("current")
_NptLogicalBoardType_Type = DisplayString
_NptLogicalBoardType_Object = MibTableColumn
nptLogicalBoardType = _NptLogicalBoardType_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 3, 1, 3),
    _NptLogicalBoardType_Type()
)
nptLogicalBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptLogicalBoardType.setStatus("current")
_NptCardDescription_Type = DisplayString
_NptCardDescription_Object = MibTableColumn
nptCardDescription = _NptCardDescription_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 3, 1, 4),
    _NptCardDescription_Type()
)
nptCardDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptCardDescription.setStatus("current")
_NptCardSerialNumber_Type = DisplayString
_NptCardSerialNumber_Object = MibTableColumn
nptCardSerialNumber = _NptCardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 3, 1, 5),
    _NptCardSerialNumber_Type()
)
nptCardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptCardSerialNumber.setStatus("current")
_NptHwRevision_Type = DisplayString
_NptHwRevision_Object = MibTableColumn
nptHwRevision = _NptHwRevision_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 3, 1, 6),
    _NptHwRevision_Type()
)
nptHwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptHwRevision.setStatus("current")
_NptHwOption_Type = DisplayString
_NptHwOption_Object = MibTableColumn
nptHwOption = _NptHwOption_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 3, 1, 7),
    _NptHwOption_Type()
)
nptHwOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptHwOption.setStatus("current")
_NptEPLDRevision_Type = DisplayString
_NptEPLDRevision_Object = MibTableColumn
nptEPLDRevision = _NptEPLDRevision_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 3, 1, 8),
    _NptEPLDRevision_Type()
)
nptEPLDRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptEPLDRevision.setStatus("current")
_NptBootVersion_Type = DisplayString
_NptBootVersion_Object = MibTableColumn
nptBootVersion = _NptBootVersion_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 3, 1, 9),
    _NptBootVersion_Type()
)
nptBootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptBootVersion.setStatus("current")
_NptFPGAVersion_Type = DisplayString
_NptFPGAVersion_Object = MibTableColumn
nptFPGAVersion = _NptFPGAVersion_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 3, 1, 10),
    _NptFPGAVersion_Type()
)
nptFPGAVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptFPGAVersion.setStatus("current")
_NptSWRevision_Type = DisplayString
_NptSWRevision_Object = MibTableColumn
nptSWRevision = _NptSWRevision_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 3, 1, 11),
    _NptSWRevision_Type()
)
nptSWRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptSWRevision.setStatus("current")
_NptVendor_Type = DisplayString
_NptVendor_Object = MibTableColumn
nptVendor = _NptVendor_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 3, 1, 12),
    _NptVendor_Type()
)
nptVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptVendor.setStatus("current")
_NptMacAddress_Type = DisplayString
_NptMacAddress_Object = MibTableColumn
nptMacAddress = _NptMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 3, 1, 13),
    _NptMacAddress_Type()
)
nptMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptMacAddress.setStatus("current")
_NptSysTrapConfig_ObjectIdentity = ObjectIdentity
nptSysTrapConfig = _NptSysTrapConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 4)
)
if mibBuilder.loadTexts:
    nptSysTrapConfig.setStatus("current")
_NptManagerTable_Object = MibTable
nptManagerTable = _NptManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 4, 4)
)
if mibBuilder.loadTexts:
    nptManagerTable.setStatus("current")
_NptManagerEntry_Object = MibTableRow
nptManagerEntry = _NptManagerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 4, 4, 1)
)
nptManagerEntry.setIndexNames(
    (0, "NPT-SYSTEM-MIB", "nptTrapIpAddress"),
    (0, "NPT-SYSTEM-MIB", "nptTrapPortNumber"),
    (0, "NPT-SYSTEM-MIB", "nptTrapVersion"),
)
if mibBuilder.loadTexts:
    nptManagerEntry.setStatus("current")
_NptTrapIpAddress_Type = DisplayString
_NptTrapIpAddress_Object = MibTableColumn
nptTrapIpAddress = _NptTrapIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 4, 4, 1, 1),
    _NptTrapIpAddress_Type()
)
nptTrapIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptTrapIpAddress.setStatus("current")


class _NptTrapPortNumber_Type(Unsigned32):
    """Custom type nptTrapPortNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NptTrapPortNumber_Type.__name__ = "Unsigned32"
_NptTrapPortNumber_Object = MibTableColumn
nptTrapPortNumber = _NptTrapPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 4, 4, 1, 2),
    _NptTrapPortNumber_Type()
)
nptTrapPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptTrapPortNumber.setStatus("current")


class _NptTrapVersion_Type(Unsigned32):
    """Custom type nptTrapVersion based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NptTrapVersion_Type.__name__ = "Unsigned32"
_NptTrapVersion_Object = MibTableColumn
nptTrapVersion = _NptTrapVersion_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 4, 4, 1, 3),
    _NptTrapVersion_Type()
)
nptTrapVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptTrapVersion.setStatus("current")


class _NptIsAdministrator_Type(Unsigned32):
    """Custom type nptIsAdministrator based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NptIsAdministrator_Type.__name__ = "Unsigned32"
_NptIsAdministrator_Object = MibTableColumn
nptIsAdministrator = _NptIsAdministrator_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 4, 4, 1, 4),
    _NptIsAdministrator_Type()
)
nptIsAdministrator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptIsAdministrator.setStatus("current")
_NptCpuInfoTable_Object = MibTable
nptCpuInfoTable = _NptCpuInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 5)
)
if mibBuilder.loadTexts:
    nptCpuInfoTable.setStatus("current")
_NptCpuInfoEntry_Object = MibTableRow
nptCpuInfoEntry = _NptCpuInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 5, 1)
)
nptCpuInfoEntry.setIndexNames(
    (0, "NPT-SYSTEM-MIB", "nptCpuSlotId"),
)
if mibBuilder.loadTexts:
    nptCpuInfoEntry.setStatus("current")


class _NptCpuSlotId_Type(Integer32):
    """Custom type nptCpuSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NptCpuSlotId_Type.__name__ = "Integer32"
_NptCpuSlotId_Object = MibTableColumn
nptCpuSlotId = _NptCpuSlotId_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 5, 1, 1),
    _NptCpuSlotId_Type()
)
nptCpuSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptCpuSlotId.setStatus("current")
_NptCpuSlotType_Type = DisplayString
_NptCpuSlotType_Object = MibTableColumn
nptCpuSlotType = _NptCpuSlotType_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 5, 1, 2),
    _NptCpuSlotType_Type()
)
nptCpuSlotType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptCpuSlotType.setStatus("current")
_NptCpuPhysicalBoardType_Type = DisplayString
_NptCpuPhysicalBoardType_Object = MibTableColumn
nptCpuPhysicalBoardType = _NptCpuPhysicalBoardType_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 5, 1, 3),
    _NptCpuPhysicalBoardType_Type()
)
nptCpuPhysicalBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptCpuPhysicalBoardType.setStatus("current")
_NptCpuType_Type = DisplayString
_NptCpuType_Object = MibTableColumn
nptCpuType = _NptCpuType_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 5, 1, 4),
    _NptCpuType_Type()
)
nptCpuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptCpuType.setStatus("current")
_NptCpuRevision_Type = DisplayString
_NptCpuRevision_Object = MibTableColumn
nptCpuRevision = _NptCpuRevision_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 5, 1, 5),
    _NptCpuRevision_Type()
)
nptCpuRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptCpuRevision.setStatus("current")
_NptCpuSpeed_Type = DisplayString
_NptCpuSpeed_Object = MibTableColumn
nptCpuSpeed = _NptCpuSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 5, 1, 6),
    _NptCpuSpeed_Type()
)
nptCpuSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptCpuSpeed.setStatus("current")
_NptCpuCacheSize_Type = DisplayString
_NptCpuCacheSize_Object = MibTableColumn
nptCpuCacheSize = _NptCpuCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 5, 1, 7),
    _NptCpuCacheSize_Type()
)
nptCpuCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptCpuCacheSize.setStatus("current")
_NptTotalProcesses_Type = Integer32
_NptTotalProcesses_Object = MibTableColumn
nptTotalProcesses = _NptTotalProcesses_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 5, 1, 8),
    _NptTotalProcesses_Type()
)
nptTotalProcesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptTotalProcesses.setStatus("current")
_NptProcessesStatus_Type = DisplayString
_NptProcessesStatus_Object = MibTableColumn
nptProcessesStatus = _NptProcessesStatus_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 5, 1, 9),
    _NptProcessesStatus_Type()
)
nptProcessesStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptProcessesStatus.setStatus("current")
_NptUptime_Type = DisplayString
_NptUptime_Object = MibTableColumn
nptUptime = _NptUptime_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 5, 1, 10),
    _NptUptime_Type()
)
nptUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptUptime.setStatus("current")
_NptLoadAverage_Type = DisplayString
_NptLoadAverage_Object = MibTableColumn
nptLoadAverage = _NptLoadAverage_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 5, 1, 11),
    _NptLoadAverage_Type()
)
nptLoadAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptLoadAverage.setStatus("current")
_NptUserUtilization_Type = Integer32
_NptUserUtilization_Object = MibTableColumn
nptUserUtilization = _NptUserUtilization_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 5, 1, 12),
    _NptUserUtilization_Type()
)
nptUserUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptUserUtilization.setStatus("current")
_NptNiceUtilization_Type = Integer32
_NptNiceUtilization_Object = MibTableColumn
nptNiceUtilization = _NptNiceUtilization_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 5, 1, 13),
    _NptNiceUtilization_Type()
)
nptNiceUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptNiceUtilization.setStatus("current")
_NptSystemUtilization_Type = Integer32
_NptSystemUtilization_Object = MibTableColumn
nptSystemUtilization = _NptSystemUtilization_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 5, 1, 14),
    _NptSystemUtilization_Type()
)
nptSystemUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptSystemUtilization.setStatus("current")
_NptWaitingUtilization_Type = Integer32
_NptWaitingUtilization_Object = MibTableColumn
nptWaitingUtilization = _NptWaitingUtilization_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 5, 1, 15),
    _NptWaitingUtilization_Type()
)
nptWaitingUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptWaitingUtilization.setStatus("current")
_NptHwInterupUtilization_Type = Integer32
_NptHwInterupUtilization_Object = MibTableColumn
nptHwInterupUtilization = _NptHwInterupUtilization_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 5, 1, 16),
    _NptHwInterupUtilization_Type()
)
nptHwInterupUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptHwInterupUtilization.setStatus("current")
_NptSoftInterupUtilization_Type = Integer32
_NptSoftInterupUtilization_Object = MibTableColumn
nptSoftInterupUtilization = _NptSoftInterupUtilization_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 5, 1, 17),
    _NptSoftInterupUtilization_Type()
)
nptSoftInterupUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptSoftInterupUtilization.setStatus("current")
_NptIdle_Type = Integer32
_NptIdle_Object = MibTableColumn
nptIdle = _NptIdle_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 5, 1, 18),
    _NptIdle_Type()
)
nptIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptIdle.setStatus("current")
_NptMemoryInfoTable_Object = MibTable
nptMemoryInfoTable = _NptMemoryInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 6)
)
if mibBuilder.loadTexts:
    nptMemoryInfoTable.setStatus("current")
_NptMemoryInfoEntry_Object = MibTableRow
nptMemoryInfoEntry = _NptMemoryInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 6, 1)
)
nptMemoryInfoEntry.setIndexNames(
    (0, "NPT-SYSTEM-MIB", "nptMemorySlotId"),
)
if mibBuilder.loadTexts:
    nptMemoryInfoEntry.setStatus("current")


class _NptMemorySlotId_Type(Integer32):
    """Custom type nptMemorySlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NptMemorySlotId_Type.__name__ = "Integer32"
_NptMemorySlotId_Object = MibTableColumn
nptMemorySlotId = _NptMemorySlotId_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 6, 1, 1),
    _NptMemorySlotId_Type()
)
nptMemorySlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptMemorySlotId.setStatus("current")
_NptMemorySlotType_Type = DisplayString
_NptMemorySlotType_Object = MibTableColumn
nptMemorySlotType = _NptMemorySlotType_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 6, 1, 2),
    _NptMemorySlotType_Type()
)
nptMemorySlotType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptMemorySlotType.setStatus("current")
_NptMemoryPhysicalBoardType_Type = DisplayString
_NptMemoryPhysicalBoardType_Object = MibTableColumn
nptMemoryPhysicalBoardType = _NptMemoryPhysicalBoardType_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 6, 1, 3),
    _NptMemoryPhysicalBoardType_Type()
)
nptMemoryPhysicalBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptMemoryPhysicalBoardType.setStatus("current")
_NptMemoryFree_Type = Integer32
_NptMemoryFree_Object = MibTableColumn
nptMemoryFree = _NptMemoryFree_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 6, 1, 4),
    _NptMemoryFree_Type()
)
nptMemoryFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptMemoryFree.setStatus("current")
_NptMemoryUsed_Type = Integer32
_NptMemoryUsed_Object = MibTableColumn
nptMemoryUsed = _NptMemoryUsed_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 6, 1, 5),
    _NptMemoryUsed_Type()
)
nptMemoryUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptMemoryUsed.setStatus("current")
_NptMemoryBuffers_Type = Integer32
_NptMemoryBuffers_Object = MibTableColumn
nptMemoryBuffers = _NptMemoryBuffers_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 6, 1, 6),
    _NptMemoryBuffers_Type()
)
nptMemoryBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptMemoryBuffers.setStatus("current")
_NptMemoryTotal_Type = Integer32
_NptMemoryTotal_Object = MibTableColumn
nptMemoryTotal = _NptMemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 6, 1, 7),
    _NptMemoryTotal_Type()
)
nptMemoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptMemoryTotal.setStatus("current")
_NptMemoryFreeSwap_Type = Integer32
_NptMemoryFreeSwap_Object = MibTableColumn
nptMemoryFreeSwap = _NptMemoryFreeSwap_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 6, 1, 8),
    _NptMemoryFreeSwap_Type()
)
nptMemoryFreeSwap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptMemoryFreeSwap.setStatus("current")
_NptMemoryUsedSwap_Type = Integer32
_NptMemoryUsedSwap_Object = MibTableColumn
nptMemoryUsedSwap = _NptMemoryUsedSwap_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 6, 1, 9),
    _NptMemoryUsedSwap_Type()
)
nptMemoryUsedSwap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptMemoryUsedSwap.setStatus("current")
_NptMemoryCachedSwap_Type = Integer32
_NptMemoryCachedSwap_Object = MibTableColumn
nptMemoryCachedSwap = _NptMemoryCachedSwap_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 6, 1, 10),
    _NptMemoryCachedSwap_Type()
)
nptMemoryCachedSwap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptMemoryCachedSwap.setStatus("current")
_NptMemoryTotalSwap_Type = Integer32
_NptMemoryTotalSwap_Object = MibTableColumn
nptMemoryTotalSwap = _NptMemoryTotalSwap_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 6, 1, 11),
    _NptMemoryTotalSwap_Type()
)
nptMemoryTotalSwap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptMemoryTotalSwap.setStatus("current")
_NptSysStartTime_Type = DisplayString
_NptSysStartTime_Object = MibScalar
nptSysStartTime = _NptSysStartTime_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 7),
    _NptSysStartTime_Type()
)
nptSysStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptSysStartTime.setStatus("current")
_NptTransceiverInformation_ObjectIdentity = ObjectIdentity
nptTransceiverInformation = _NptTransceiverInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8)
)
if mibBuilder.loadTexts:
    nptTransceiverInformation.setStatus("current")
_NptTransceiverConfigurationTable_Object = MibTable
nptTransceiverConfigurationTable = _NptTransceiverConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 1)
)
if mibBuilder.loadTexts:
    nptTransceiverConfigurationTable.setStatus("current")
_NptTransceiverConfigurationEntry_Object = MibTableRow
nptTransceiverConfigurationEntry = _NptTransceiverConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 1, 1)
)
nptTransceiverConfigurationEntry.setIndexNames(
    (0, "NPT-SYSTEM-MIB", "nptTransceiverConfigurationIndex"),
)
if mibBuilder.loadTexts:
    nptTransceiverConfigurationEntry.setStatus("current")


class _NptTransceiverConfigurationIndex_Type(Unsigned32):
    """Custom type nptTransceiverConfigurationIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NptTransceiverConfigurationIndex_Type.__name__ = "Unsigned32"
_NptTransceiverConfigurationIndex_Object = MibTableColumn
nptTransceiverConfigurationIndex = _NptTransceiverConfigurationIndex_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 1, 1, 1),
    _NptTransceiverConfigurationIndex_Type()
)
nptTransceiverConfigurationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptTransceiverConfigurationIndex.setStatus("current")
_NptTransceiverConfigurationName_Type = DisplayString
_NptTransceiverConfigurationName_Object = MibTableColumn
nptTransceiverConfigurationName = _NptTransceiverConfigurationName_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 1, 1, 2),
    _NptTransceiverConfigurationName_Type()
)
nptTransceiverConfigurationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptTransceiverConfigurationName.setStatus("current")
_NptExpectedTransceiverType_Type = DisplayString
_NptExpectedTransceiverType_Object = MibTableColumn
nptExpectedTransceiverType = _NptExpectedTransceiverType_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 1, 1, 3),
    _NptExpectedTransceiverType_Type()
)
nptExpectedTransceiverType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptExpectedTransceiverType.setStatus("current")
_NptExpectedApplicationCode_Type = DisplayString
_NptExpectedApplicationCode_Object = MibTableColumn
nptExpectedApplicationCode = _NptExpectedApplicationCode_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 1, 1, 4),
    _NptExpectedApplicationCode_Type()
)
nptExpectedApplicationCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptExpectedApplicationCode.setStatus("current")
_NptRate_Type = DisplayString
_NptRate_Object = MibTableColumn
nptRate = _NptRate_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 1, 1, 5),
    _NptRate_Type()
)
nptRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptRate.setStatus("current")
_NptConnectorType_Type = DisplayString
_NptConnectorType_Object = MibTableColumn
nptConnectorType = _NptConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 1, 1, 6),
    _NptConnectorType_Type()
)
nptConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptConnectorType.setStatus("current")
_NptNominalBitrate_Type = DisplayString
_NptNominalBitrate_Object = MibTableColumn
nptNominalBitrate = _NptNominalBitrate_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 1, 1, 7),
    _NptNominalBitrate_Type()
)
nptNominalBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptNominalBitrate.setStatus("current")
_NptSupportedLinkLength_Type = DisplayString
_NptSupportedLinkLength_Object = MibTableColumn
nptSupportedLinkLength = _NptSupportedLinkLength_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 1, 1, 8),
    _NptSupportedLinkLength_Type()
)
nptSupportedLinkLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptSupportedLinkLength.setStatus("current")
_NptTransmitedWavelength_Type = DisplayString
_NptTransmitedWavelength_Object = MibTableColumn
nptTransmitedWavelength = _NptTransmitedWavelength_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 1, 1, 9),
    _NptTransmitedWavelength_Type()
)
nptTransmitedWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptTransmitedWavelength.setStatus("current")
_NptChannelColor_Type = DisplayString
_NptChannelColor_Object = MibTableColumn
nptChannelColor = _NptChannelColor_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 1, 1, 10),
    _NptChannelColor_Type()
)
nptChannelColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptChannelColor.setStatus("current")
_NptSupportedFiberType_Type = DisplayString
_NptSupportedFiberType_Object = MibTableColumn
nptSupportedFiberType = _NptSupportedFiberType_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 1, 1, 11),
    _NptSupportedFiberType_Type()
)
nptSupportedFiberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptSupportedFiberType.setStatus("current")
_NptTransceiverStatusTable_Object = MibTable
nptTransceiverStatusTable = _NptTransceiverStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 2)
)
if mibBuilder.loadTexts:
    nptTransceiverStatusTable.setStatus("current")
_NptTransceiverStatusEntry_Object = MibTableRow
nptTransceiverStatusEntry = _NptTransceiverStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 2, 1)
)
nptTransceiverStatusEntry.setIndexNames(
    (0, "NPT-SYSTEM-MIB", "nptTransceiverStatusIndex"),
)
if mibBuilder.loadTexts:
    nptTransceiverStatusEntry.setStatus("current")


class _NptTransceiverStatusIndex_Type(Unsigned32):
    """Custom type nptTransceiverStatusIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NptTransceiverStatusIndex_Type.__name__ = "Unsigned32"
_NptTransceiverStatusIndex_Object = MibTableColumn
nptTransceiverStatusIndex = _NptTransceiverStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 2, 1, 1),
    _NptTransceiverStatusIndex_Type()
)
nptTransceiverStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptTransceiverStatusIndex.setStatus("current")
_NptTransceiverStatusName_Type = DisplayString
_NptTransceiverStatusName_Object = MibTableColumn
nptTransceiverStatusName = _NptTransceiverStatusName_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 2, 1, 2),
    _NptTransceiverStatusName_Type()
)
nptTransceiverStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptTransceiverStatusName.setStatus("current")
_NptOperationalState_Type = NPTSfpOperStatus
_NptOperationalState_Object = MibTableColumn
nptOperationalState = _NptOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 2, 1, 3),
    _NptOperationalState_Type()
)
nptOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptOperationalState.setStatus("current")
_NptActualLaserTransmitStatus_Type = NPTSfpLaserTrStatus
_NptActualLaserTransmitStatus_Object = MibTableColumn
nptActualLaserTransmitStatus = _NptActualLaserTransmitStatus_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 2, 1, 4),
    _NptActualLaserTransmitStatus_Type()
)
nptActualLaserTransmitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptActualLaserTransmitStatus.setStatus("current")
_NptReceivedLOSStatus_Type = NPTSfpLOSStatus
_NptReceivedLOSStatus_Object = MibTableColumn
nptReceivedLOSStatus = _NptReceivedLOSStatus_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 2, 1, 5),
    _NptReceivedLOSStatus_Type()
)
nptReceivedLOSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptReceivedLOSStatus.setStatus("current")
_NptActualNominalBitrate_Type = Integer32
_NptActualNominalBitrate_Object = MibTableColumn
nptActualNominalBitrate = _NptActualNominalBitrate_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 2, 1, 6),
    _NptActualNominalBitrate_Type()
)
nptActualNominalBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptActualNominalBitrate.setStatus("current")
_NptActualSupportedLinkLength_Type = Integer32
_NptActualSupportedLinkLength_Object = MibTableColumn
nptActualSupportedLinkLength = _NptActualSupportedLinkLength_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 2, 1, 7),
    _NptActualSupportedLinkLength_Type()
)
nptActualSupportedLinkLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptActualSupportedLinkLength.setStatus("current")
_NptActualTransmitedWavelength_Type = Integer32
_NptActualTransmitedWavelength_Object = MibTableColumn
nptActualTransmitedWavelength = _NptActualTransmitedWavelength_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 2, 1, 8),
    _NptActualTransmitedWavelength_Type()
)
nptActualTransmitedWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptActualTransmitedWavelength.setStatus("current")
_NptActualSupportedFiberType_Type = NPTSfpFiberType
_NptActualSupportedFiberType_Object = MibTableColumn
nptActualSupportedFiberType = _NptActualSupportedFiberType_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 2, 1, 9),
    _NptActualSupportedFiberType_Type()
)
nptActualSupportedFiberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptActualSupportedFiberType.setStatus("current")
_NptLineCode_Type = NPTSfpLineCode
_NptLineCode_Object = MibTableColumn
nptLineCode = _NptLineCode_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 2, 1, 10),
    _NptLineCode_Type()
)
nptLineCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptLineCode.setStatus("current")
_NptCoherent_Type = TruthValue
_NptCoherent_Object = MibTableColumn
nptCoherent = _NptCoherent_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 2, 1, 11),
    _NptCoherent_Type()
)
nptCoherent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptCoherent.setStatus("current")
_NptSubBand_Type = Integer32
_NptSubBand_Object = MibTableColumn
nptSubBand = _NptSubBand_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 2, 1, 12),
    _NptSubBand_Type()
)
nptSubBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptSubBand.setStatus("current")
_NptMeasuredRxOSNR_Type = DisplayString
_NptMeasuredRxOSNR_Object = MibTableColumn
nptMeasuredRxOSNR = _NptMeasuredRxOSNR_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 2, 1, 13),
    _NptMeasuredRxOSNR_Type()
)
nptMeasuredRxOSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptMeasuredRxOSNR.setStatus("current")
_NptTxOSNR_Type = DisplayString
_NptTxOSNR_Object = MibTableColumn
nptTxOSNR = _NptTxOSNR_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 2, 1, 14),
    _NptTxOSNR_Type()
)
nptTxOSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptTxOSNR.setStatus("current")
_NptTransceiverInventoryTable_Object = MibTable
nptTransceiverInventoryTable = _NptTransceiverInventoryTable_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 3)
)
if mibBuilder.loadTexts:
    nptTransceiverInventoryTable.setStatus("current")
_NptTransceiverInventoryEntry_Object = MibTableRow
nptTransceiverInventoryEntry = _NptTransceiverInventoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 3, 1)
)
nptTransceiverInventoryEntry.setIndexNames(
    (0, "NPT-SYSTEM-MIB", "nptTransceiverInventoryIndex"),
)
if mibBuilder.loadTexts:
    nptTransceiverInventoryEntry.setStatus("current")


class _NptTransceiverInventoryIndex_Type(Unsigned32):
    """Custom type nptTransceiverInventoryIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NptTransceiverInventoryIndex_Type.__name__ = "Unsigned32"
_NptTransceiverInventoryIndex_Object = MibTableColumn
nptTransceiverInventoryIndex = _NptTransceiverInventoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 3, 1, 1),
    _NptTransceiverInventoryIndex_Type()
)
nptTransceiverInventoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptTransceiverInventoryIndex.setStatus("current")
_NptTransceiverInventoryName_Type = DisplayString
_NptTransceiverInventoryName_Object = MibTableColumn
nptTransceiverInventoryName = _NptTransceiverInventoryName_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 3, 1, 2),
    _NptTransceiverInventoryName_Type()
)
nptTransceiverInventoryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptTransceiverInventoryName.setStatus("current")
_NptActualTransceiverType_Type = DisplayString
_NptActualTransceiverType_Object = MibTableColumn
nptActualTransceiverType = _NptActualTransceiverType_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 3, 1, 3),
    _NptActualTransceiverType_Type()
)
nptActualTransceiverType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptActualTransceiverType.setStatus("current")
_NptTransceiverInventoryVendor_Type = DisplayString
_NptTransceiverInventoryVendor_Object = MibTableColumn
nptTransceiverInventoryVendor = _NptTransceiverInventoryVendor_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 3, 1, 4),
    _NptTransceiverInventoryVendor_Type()
)
nptTransceiverInventoryVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptTransceiverInventoryVendor.setStatus("current")
_NptSerialNumber_Type = DisplayString
_NptSerialNumber_Object = MibTableColumn
nptSerialNumber = _NptSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 3, 1, 5),
    _NptSerialNumber_Type()
)
nptSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptSerialNumber.setStatus("current")
_NptHWRevision_Type = DisplayString
_NptHWRevision_Object = MibTableColumn
nptHWRevision = _NptHWRevision_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 3, 1, 6),
    _NptHWRevision_Type()
)
nptHWRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptHWRevision.setStatus("current")
_NptHWOption_Type = DisplayString
_NptHWOption_Object = MibTableColumn
nptHWOption = _NptHWOption_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 3, 1, 7),
    _NptHWOption_Type()
)
nptHWOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptHWOption.setStatus("current")
_NptGeneralDescription_Type = DisplayString
_NptGeneralDescription_Object = MibTableColumn
nptGeneralDescription = _NptGeneralDescription_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 3, 1, 8),
    _NptGeneralDescription_Type()
)
nptGeneralDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptGeneralDescription.setStatus("current")
_NptModuleSubType_Type = DisplayString
_NptModuleSubType_Object = MibTableColumn
nptModuleSubType = _NptModuleSubType_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 3, 1, 9),
    _NptModuleSubType_Type()
)
nptModuleSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptModuleSubType.setStatus("current")
_NptActualApplicationCode_Type = DisplayString
_NptActualApplicationCode_Object = MibTableColumn
nptActualApplicationCode = _NptActualApplicationCode_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 3, 1, 10),
    _NptActualApplicationCode_Type()
)
nptActualApplicationCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptActualApplicationCode.setStatus("current")
_NptSupportChannelNumber_Type = DisplayString
_NptSupportChannelNumber_Object = MibTableColumn
nptSupportChannelNumber = _NptSupportChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 3, 1, 11),
    _NptSupportChannelNumber_Type()
)
nptSupportChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptSupportChannelNumber.setStatus("current")
_NptWDMFirstChannelnumber_Type = DisplayString
_NptWDMFirstChannelnumber_Object = MibTableColumn
nptWDMFirstChannelnumber = _NptWDMFirstChannelnumber_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 3, 1, 12),
    _NptWDMFirstChannelnumber_Type()
)
nptWDMFirstChannelnumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptWDMFirstChannelnumber.setStatus("current")
_NptChannelSpacing_Type = DisplayString
_NptChannelSpacing_Object = MibTableColumn
nptChannelSpacing = _NptChannelSpacing_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 3, 1, 13),
    _NptChannelSpacing_Type()
)
nptChannelSpacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptChannelSpacing.setStatus("current")
_NptTransceiverPower_ObjectIdentity = ObjectIdentity
nptTransceiverPower = _NptTransceiverPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 4)
)
if mibBuilder.loadTexts:
    nptTransceiverPower.setStatus("current")
_NptTransceiverPowerTable_Object = MibTable
nptTransceiverPowerTable = _NptTransceiverPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 4, 1)
)
if mibBuilder.loadTexts:
    nptTransceiverPowerTable.setStatus("current")
_NptTransceiverPowerEntry_Object = MibTableRow
nptTransceiverPowerEntry = _NptTransceiverPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 4, 1, 1)
)
nptTransceiverPowerEntry.setIndexNames(
    (0, "NPT-SYSTEM-MIB", "nptTransceiverPowerIndex"),
)
if mibBuilder.loadTexts:
    nptTransceiverPowerEntry.setStatus("current")


class _NptTransceiverPowerIndex_Type(Unsigned32):
    """Custom type nptTransceiverPowerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NptTransceiverPowerIndex_Type.__name__ = "Unsigned32"
_NptTransceiverPowerIndex_Object = MibTableColumn
nptTransceiverPowerIndex = _NptTransceiverPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 4, 1, 1, 1),
    _NptTransceiverPowerIndex_Type()
)
nptTransceiverPowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptTransceiverPowerIndex.setStatus("current")
_NptTransceiverPowerName_Type = DisplayString
_NptTransceiverPowerName_Object = MibTableColumn
nptTransceiverPowerName = _NptTransceiverPowerName_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 4, 1, 1, 2),
    _NptTransceiverPowerName_Type()
)
nptTransceiverPowerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptTransceiverPowerName.setStatus("current")
_NptLaservoltage_Type = Integer32
_NptLaservoltage_Object = MibTableColumn
nptLaservoltage = _NptLaservoltage_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 4, 1, 1, 3),
    _NptLaservoltage_Type()
)
nptLaservoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptLaservoltage.setStatus("current")
_NptLaserbiascurrent_Type = Integer32
_NptLaserbiascurrent_Object = MibTableColumn
nptLaserbiascurrent = _NptLaserbiascurrent_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 4, 1, 1, 4),
    _NptLaserbiascurrent_Type()
)
nptLaserbiascurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptLaserbiascurrent.setStatus("current")
_NptLasertemperature_Type = Integer32
_NptLasertemperature_Object = MibTableColumn
nptLasertemperature = _NptLasertemperature_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 4, 1, 1, 5),
    _NptLasertemperature_Type()
)
nptLasertemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptLasertemperature.setStatus("current")
_NptTxlaserpower_Type = Integer32
_NptTxlaserpower_Object = MibTableColumn
nptTxlaserpower = _NptTxlaserpower_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 4, 1, 1, 6),
    _NptTxlaserpower_Type()
)
nptTxlaserpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptTxlaserpower.setStatus("current")
_NptRxlaserpower_Type = Integer32
_NptRxlaserpower_Object = MibTableColumn
nptRxlaserpower = _NptRxlaserpower_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 4, 1, 1, 7),
    _NptRxlaserpower_Type()
)
nptRxlaserpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptRxlaserpower.setStatus("current")
_NptMaxrxpowerlane_Type = Integer32
_NptMaxrxpowerlane_Object = MibTableColumn
nptMaxrxpowerlane = _NptMaxrxpowerlane_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 4, 1, 1, 8),
    _NptMaxrxpowerlane_Type()
)
nptMaxrxpowerlane.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptMaxrxpowerlane.setStatus("current")
_NptMinrxpowerlane_Type = Integer32
_NptMinrxpowerlane_Object = MibTableColumn
nptMinrxpowerlane = _NptMinrxpowerlane_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 4, 1, 1, 9),
    _NptMinrxpowerlane_Type()
)
nptMinrxpowerlane.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptMinrxpowerlane.setStatus("current")
_NptMaxtxpowerlane_Type = Integer32
_NptMaxtxpowerlane_Object = MibTableColumn
nptMaxtxpowerlane = _NptMaxtxpowerlane_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 4, 1, 1, 10),
    _NptMaxtxpowerlane_Type()
)
nptMaxtxpowerlane.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptMaxtxpowerlane.setStatus("current")
_NptMintxpowerlane_Type = Integer32
_NptMintxpowerlane_Object = MibTableColumn
nptMintxpowerlane = _NptMintxpowerlane_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 4, 1, 1, 11),
    _NptMintxpowerlane_Type()
)
nptMintxpowerlane.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptMintxpowerlane.setStatus("current")
_NptMaxLaserBiasCur_Type = Integer32
_NptMaxLaserBiasCur_Object = MibTableColumn
nptMaxLaserBiasCur = _NptMaxLaserBiasCur_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 4, 1, 1, 12),
    _NptMaxLaserBiasCur_Type()
)
nptMaxLaserBiasCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptMaxLaserBiasCur.setStatus("current")
_NptTransceiverPowerMultilaneTable_Object = MibTable
nptTransceiverPowerMultilaneTable = _NptTransceiverPowerMultilaneTable_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 4, 2)
)
if mibBuilder.loadTexts:
    nptTransceiverPowerMultilaneTable.setStatus("current")
_NptTransceiverPowerMultilaneEntry_Object = MibTableRow
nptTransceiverPowerMultilaneEntry = _NptTransceiverPowerMultilaneEntry_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 4, 2, 1)
)
nptTransceiverPowerMultilaneEntry.setIndexNames(
    (0, "NPT-SYSTEM-MIB", "nptTransceiverPowerMultilaneIndex"),
    (0, "NPT-SYSTEM-MIB", "nptLaneNum"),
)
if mibBuilder.loadTexts:
    nptTransceiverPowerMultilaneEntry.setStatus("current")


class _NptTransceiverPowerMultilaneIndex_Type(Unsigned32):
    """Custom type nptTransceiverPowerMultilaneIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NptTransceiverPowerMultilaneIndex_Type.__name__ = "Unsigned32"
_NptTransceiverPowerMultilaneIndex_Object = MibTableColumn
nptTransceiverPowerMultilaneIndex = _NptTransceiverPowerMultilaneIndex_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 4, 2, 1, 1),
    _NptTransceiverPowerMultilaneIndex_Type()
)
nptTransceiverPowerMultilaneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptTransceiverPowerMultilaneIndex.setStatus("current")
_NptLaneNum_Type = Unsigned32
_NptLaneNum_Object = MibTableColumn
nptLaneNum = _NptLaneNum_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 4, 2, 1, 2),
    _NptLaneNum_Type()
)
nptLaneNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptLaneNum.setStatus("current")
_NptTransceiverPowerMultilaneName_Type = DisplayString
_NptTransceiverPowerMultilaneName_Object = MibTableColumn
nptTransceiverPowerMultilaneName = _NptTransceiverPowerMultilaneName_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 4, 2, 1, 3),
    _NptTransceiverPowerMultilaneName_Type()
)
nptTransceiverPowerMultilaneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptTransceiverPowerMultilaneName.setStatus("current")
_NptLaneTxLaserPower_Type = Integer32
_NptLaneTxLaserPower_Object = MibTableColumn
nptLaneTxLaserPower = _NptLaneTxLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 4, 2, 1, 4),
    _NptLaneTxLaserPower_Type()
)
nptLaneTxLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptLaneTxLaserPower.setStatus("current")
_NptLaneRxLaserPower_Type = Integer32
_NptLaneRxLaserPower_Object = MibTableColumn
nptLaneRxLaserPower = _NptLaneRxLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 4, 2, 1, 5),
    _NptLaneRxLaserPower_Type()
)
nptLaneRxLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptLaneRxLaserPower.setStatus("current")
_NptLaneLaserBiasCur_Type = Integer32
_NptLaneLaserBiasCur_Object = MibTableColumn
nptLaneLaserBiasCur = _NptLaneLaserBiasCur_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 4, 2, 1, 6),
    _NptLaneLaserBiasCur_Type()
)
nptLaneLaserBiasCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptLaneLaserBiasCur.setStatus("current")
_NptTunnableTransceiverConfigurationTable_Object = MibTable
nptTunnableTransceiverConfigurationTable = _NptTunnableTransceiverConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 5)
)
if mibBuilder.loadTexts:
    nptTunnableTransceiverConfigurationTable.setStatus("current")
_NptTunnableTransceiverConfigurationEntry_Object = MibTableRow
nptTunnableTransceiverConfigurationEntry = _NptTunnableTransceiverConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 5, 1)
)
nptTunnableTransceiverConfigurationEntry.setIndexNames(
    (0, "NPT-SYSTEM-MIB", "nptTunnableTransceiverConfigurationIndex"),
)
if mibBuilder.loadTexts:
    nptTunnableTransceiverConfigurationEntry.setStatus("current")


class _NptTunnableTransceiverConfigurationIndex_Type(Unsigned32):
    """Custom type nptTunnableTransceiverConfigurationIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NptTunnableTransceiverConfigurationIndex_Type.__name__ = "Unsigned32"
_NptTunnableTransceiverConfigurationIndex_Object = MibTableColumn
nptTunnableTransceiverConfigurationIndex = _NptTunnableTransceiverConfigurationIndex_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 5, 1, 1),
    _NptTunnableTransceiverConfigurationIndex_Type()
)
nptTunnableTransceiverConfigurationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptTunnableTransceiverConfigurationIndex.setStatus("current")
_NptTunnableTransceiverConfigurationName_Type = DisplayString
_NptTunnableTransceiverConfigurationName_Object = MibTableColumn
nptTunnableTransceiverConfigurationName = _NptTunnableTransceiverConfigurationName_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 5, 1, 2),
    _NptTunnableTransceiverConfigurationName_Type()
)
nptTunnableTransceiverConfigurationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptTunnableTransceiverConfigurationName.setStatus("current")
_NptChannelFrequency_Type = Integer32
_NptChannelFrequency_Object = MibTableColumn
nptChannelFrequency = _NptChannelFrequency_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 5, 1, 3),
    _NptChannelFrequency_Type()
)
nptChannelFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptChannelFrequency.setStatus("current")
_NptWavelength_Type = DisplayString
_NptWavelength_Object = MibTableColumn
nptWavelength = _NptWavelength_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 5, 1, 4),
    _NptWavelength_Type()
)
nptWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptWavelength.setStatus("current")
_NptTxDither_Type = NPTSNMPEnable
_NptTxDither_Object = MibTableColumn
nptTxDither = _NptTxDither_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 5, 1, 5),
    _NptTxDither_Type()
)
nptTxDither.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptTxDither.setStatus("current")
_NptFrequencyTuning_Type = NPTSNMPYesOrNo
_NptFrequencyTuning_Object = MibTableColumn
nptFrequencyTuning = _NptFrequencyTuning_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 5, 1, 6),
    _NptFrequencyTuning_Type()
)
nptFrequencyTuning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptFrequencyTuning.setStatus("current")
_NptWavelengthTuning_Type = NPTSNMPYesOrNo
_NptWavelengthTuning_Object = MibTableColumn
nptWavelengthTuning = _NptWavelengthTuning_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 5, 1, 7),
    _NptWavelengthTuning_Type()
)
nptWavelengthTuning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptWavelengthTuning.setStatus("current")
_NptTxDitherSupport_Type = NPTSNMPYesOrNo
_NptTxDitherSupport_Object = MibTableColumn
nptTxDitherSupport = _NptTxDitherSupport_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 5, 1, 8),
    _NptTxDitherSupport_Type()
)
nptTxDitherSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptTxDitherSupport.setStatus("current")
_NptFirstFrequency_Type = DisplayString
_NptFirstFrequency_Object = MibTableColumn
nptFirstFrequency = _NptFirstFrequency_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 5, 1, 9),
    _NptFirstFrequency_Type()
)
nptFirstFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptFirstFrequency.setStatus("current")
_NptLastFrequency_Type = DisplayString
_NptLastFrequency_Object = MibTableColumn
nptLastFrequency = _NptLastFrequency_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 5, 1, 10),
    _NptLastFrequency_Type()
)
nptLastFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptLastFrequency.setStatus("current")
_NptMinimumSupportedGridSpacing_Type = DisplayString
_NptMinimumSupportedGridSpacing_Object = MibTableColumn
nptMinimumSupportedGridSpacing = _NptMinimumSupportedGridSpacing_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 5, 1, 11),
    _NptMinimumSupportedGridSpacing_Type()
)
nptMinimumSupportedGridSpacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptMinimumSupportedGridSpacing.setStatus("current")
_NptTransceiverThresholdTable_Object = MibTable
nptTransceiverThresholdTable = _NptTransceiverThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 6)
)
if mibBuilder.loadTexts:
    nptTransceiverThresholdTable.setStatus("current")
_NptTransceiverThresholdEntry_Object = MibTableRow
nptTransceiverThresholdEntry = _NptTransceiverThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 6, 1)
)
nptTransceiverThresholdEntry.setIndexNames(
    (0, "NPT-SYSTEM-MIB", "nptTransceiverThresholdIfIndex"),
)
if mibBuilder.loadTexts:
    nptTransceiverThresholdEntry.setStatus("current")


class _NptTransceiverThresholdIfIndex_Type(Unsigned32):
    """Custom type nptTransceiverThresholdIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NptTransceiverThresholdIfIndex_Type.__name__ = "Unsigned32"
_NptTransceiverThresholdIfIndex_Object = MibTableColumn
nptTransceiverThresholdIfIndex = _NptTransceiverThresholdIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 6, 1, 1),
    _NptTransceiverThresholdIfIndex_Type()
)
nptTransceiverThresholdIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptTransceiverThresholdIfIndex.setStatus("current")
_NptTransceiverThresholdPortName_Type = DisplayString
_NptTransceiverThresholdPortName_Object = MibTableColumn
nptTransceiverThresholdPortName = _NptTransceiverThresholdPortName_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 6, 1, 2),
    _NptTransceiverThresholdPortName_Type()
)
nptTransceiverThresholdPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptTransceiverThresholdPortName.setStatus("current")
_NptTxOpticalPowerWarningLowTotal_Type = Integer32
_NptTxOpticalPowerWarningLowTotal_Object = MibTableColumn
nptTxOpticalPowerWarningLowTotal = _NptTxOpticalPowerWarningLowTotal_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 6, 1, 3),
    _NptTxOpticalPowerWarningLowTotal_Type()
)
nptTxOpticalPowerWarningLowTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptTxOpticalPowerWarningLowTotal.setStatus("current")
_NptTxOpticalPowerWarningHighTotal_Type = Integer32
_NptTxOpticalPowerWarningHighTotal_Object = MibTableColumn
nptTxOpticalPowerWarningHighTotal = _NptTxOpticalPowerWarningHighTotal_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 6, 1, 4),
    _NptTxOpticalPowerWarningHighTotal_Type()
)
nptTxOpticalPowerWarningHighTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptTxOpticalPowerWarningHighTotal.setStatus("current")
_NptTxOpticalPowerAlarmLowTotal_Type = Integer32
_NptTxOpticalPowerAlarmLowTotal_Object = MibTableColumn
nptTxOpticalPowerAlarmLowTotal = _NptTxOpticalPowerAlarmLowTotal_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 6, 1, 5),
    _NptTxOpticalPowerAlarmLowTotal_Type()
)
nptTxOpticalPowerAlarmLowTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptTxOpticalPowerAlarmLowTotal.setStatus("current")
_NptTxOpticalPowerAlarmHighTotal_Type = Integer32
_NptTxOpticalPowerAlarmHighTotal_Object = MibTableColumn
nptTxOpticalPowerAlarmHighTotal = _NptTxOpticalPowerAlarmHighTotal_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 6, 1, 6),
    _NptTxOpticalPowerAlarmHighTotal_Type()
)
nptTxOpticalPowerAlarmHighTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptTxOpticalPowerAlarmHighTotal.setStatus("current")
_NptRxOpticalPowerWarningLowTotal_Type = Integer32
_NptRxOpticalPowerWarningLowTotal_Object = MibTableColumn
nptRxOpticalPowerWarningLowTotal = _NptRxOpticalPowerWarningLowTotal_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 6, 1, 7),
    _NptRxOpticalPowerWarningLowTotal_Type()
)
nptRxOpticalPowerWarningLowTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptRxOpticalPowerWarningLowTotal.setStatus("current")
_NptRxOpticalPowerWarningHighTotal_Type = Integer32
_NptRxOpticalPowerWarningHighTotal_Object = MibTableColumn
nptRxOpticalPowerWarningHighTotal = _NptRxOpticalPowerWarningHighTotal_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 6, 1, 8),
    _NptRxOpticalPowerWarningHighTotal_Type()
)
nptRxOpticalPowerWarningHighTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptRxOpticalPowerWarningHighTotal.setStatus("current")
_NptRxOpticalPowerAlarmLowTotal_Type = Integer32
_NptRxOpticalPowerAlarmLowTotal_Object = MibTableColumn
nptRxOpticalPowerAlarmLowTotal = _NptRxOpticalPowerAlarmLowTotal_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 6, 1, 9),
    _NptRxOpticalPowerAlarmLowTotal_Type()
)
nptRxOpticalPowerAlarmLowTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptRxOpticalPowerAlarmLowTotal.setStatus("current")
_NptRxOpticalPowerAlarmHighTotal_Type = Integer32
_NptRxOpticalPowerAlarmHighTotal_Object = MibTableColumn
nptRxOpticalPowerAlarmHighTotal = _NptRxOpticalPowerAlarmHighTotal_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 6, 1, 10),
    _NptRxOpticalPowerAlarmHighTotal_Type()
)
nptRxOpticalPowerAlarmHighTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptRxOpticalPowerAlarmHighTotal.setStatus("current")
_NptTxOpticalPowerWarningLowPerLane_Type = Integer32
_NptTxOpticalPowerWarningLowPerLane_Object = MibTableColumn
nptTxOpticalPowerWarningLowPerLane = _NptTxOpticalPowerWarningLowPerLane_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 6, 1, 11),
    _NptTxOpticalPowerWarningLowPerLane_Type()
)
nptTxOpticalPowerWarningLowPerLane.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptTxOpticalPowerWarningLowPerLane.setStatus("current")
_NptTxOpticalPowerWarningHighPerLane_Type = Integer32
_NptTxOpticalPowerWarningHighPerLane_Object = MibTableColumn
nptTxOpticalPowerWarningHighPerLane = _NptTxOpticalPowerWarningHighPerLane_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 6, 1, 12),
    _NptTxOpticalPowerWarningHighPerLane_Type()
)
nptTxOpticalPowerWarningHighPerLane.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptTxOpticalPowerWarningHighPerLane.setStatus("current")
_NptTxOpticalPowerAlarmLowPerLane_Type = Integer32
_NptTxOpticalPowerAlarmLowPerLane_Object = MibTableColumn
nptTxOpticalPowerAlarmLowPerLane = _NptTxOpticalPowerAlarmLowPerLane_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 6, 1, 13),
    _NptTxOpticalPowerAlarmLowPerLane_Type()
)
nptTxOpticalPowerAlarmLowPerLane.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptTxOpticalPowerAlarmLowPerLane.setStatus("current")
_NptTxOpticalPowerAlarmHighPerLane_Type = Integer32
_NptTxOpticalPowerAlarmHighPerLane_Object = MibTableColumn
nptTxOpticalPowerAlarmHighPerLane = _NptTxOpticalPowerAlarmHighPerLane_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 6, 1, 14),
    _NptTxOpticalPowerAlarmHighPerLane_Type()
)
nptTxOpticalPowerAlarmHighPerLane.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptTxOpticalPowerAlarmHighPerLane.setStatus("current")
_NptRxOpticalPowerWarningLowPerLane_Type = Integer32
_NptRxOpticalPowerWarningLowPerLane_Object = MibTableColumn
nptRxOpticalPowerWarningLowPerLane = _NptRxOpticalPowerWarningLowPerLane_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 6, 1, 15),
    _NptRxOpticalPowerWarningLowPerLane_Type()
)
nptRxOpticalPowerWarningLowPerLane.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptRxOpticalPowerWarningLowPerLane.setStatus("current")
_NptRxOpticalPowerWarningHighPerLane_Type = Integer32
_NptRxOpticalPowerWarningHighPerLane_Object = MibTableColumn
nptRxOpticalPowerWarningHighPerLane = _NptRxOpticalPowerWarningHighPerLane_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 6, 1, 16),
    _NptRxOpticalPowerWarningHighPerLane_Type()
)
nptRxOpticalPowerWarningHighPerLane.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptRxOpticalPowerWarningHighPerLane.setStatus("current")
_NptRxOpticalPowerAlarmLowPerLane_Type = Integer32
_NptRxOpticalPowerAlarmLowPerLane_Object = MibTableColumn
nptRxOpticalPowerAlarmLowPerLane = _NptRxOpticalPowerAlarmLowPerLane_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 6, 1, 17),
    _NptRxOpticalPowerAlarmLowPerLane_Type()
)
nptRxOpticalPowerAlarmLowPerLane.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptRxOpticalPowerAlarmLowPerLane.setStatus("current")
_NptRxOpticalPowerAlarmHighPerLane_Type = Integer32
_NptRxOpticalPowerAlarmHighPerLane_Object = MibTableColumn
nptRxOpticalPowerAlarmHighPerLane = _NptRxOpticalPowerAlarmHighPerLane_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 6, 1, 18),
    _NptRxOpticalPowerAlarmHighPerLane_Type()
)
nptRxOpticalPowerAlarmHighPerLane.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptRxOpticalPowerAlarmHighPerLane.setStatus("current")
_NptTxLaserBiasCurrentWarningLow_Type = Integer32
_NptTxLaserBiasCurrentWarningLow_Object = MibTableColumn
nptTxLaserBiasCurrentWarningLow = _NptTxLaserBiasCurrentWarningLow_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 6, 1, 19),
    _NptTxLaserBiasCurrentWarningLow_Type()
)
nptTxLaserBiasCurrentWarningLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptTxLaserBiasCurrentWarningLow.setStatus("current")
_NptTxLaserBiasCurrentWarningHigh_Type = Integer32
_NptTxLaserBiasCurrentWarningHigh_Object = MibTableColumn
nptTxLaserBiasCurrentWarningHigh = _NptTxLaserBiasCurrentWarningHigh_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 6, 1, 20),
    _NptTxLaserBiasCurrentWarningHigh_Type()
)
nptTxLaserBiasCurrentWarningHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptTxLaserBiasCurrentWarningHigh.setStatus("current")
_NptTxLaserBiasCurrentAlarmLow_Type = Integer32
_NptTxLaserBiasCurrentAlarmLow_Object = MibTableColumn
nptTxLaserBiasCurrentAlarmLow = _NptTxLaserBiasCurrentAlarmLow_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 6, 1, 21),
    _NptTxLaserBiasCurrentAlarmLow_Type()
)
nptTxLaserBiasCurrentAlarmLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptTxLaserBiasCurrentAlarmLow.setStatus("current")
_NptTxLaserBiasCurrentAlarmHigh_Type = Integer32
_NptTxLaserBiasCurrentAlarmHigh_Object = MibTableColumn
nptTxLaserBiasCurrentAlarmHigh = _NptTxLaserBiasCurrentAlarmHigh_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 6, 1, 22),
    _NptTxLaserBiasCurrentAlarmHigh_Type()
)
nptTxLaserBiasCurrentAlarmHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptTxLaserBiasCurrentAlarmHigh.setStatus("current")
_NptTransceiverTemperatureWarningLow_Type = Integer32
_NptTransceiverTemperatureWarningLow_Object = MibTableColumn
nptTransceiverTemperatureWarningLow = _NptTransceiverTemperatureWarningLow_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 6, 1, 23),
    _NptTransceiverTemperatureWarningLow_Type()
)
nptTransceiverTemperatureWarningLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptTransceiverTemperatureWarningLow.setStatus("current")
_NptTransceiverTemperatureWarningHigh_Type = Integer32
_NptTransceiverTemperatureWarningHigh_Object = MibTableColumn
nptTransceiverTemperatureWarningHigh = _NptTransceiverTemperatureWarningHigh_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 6, 1, 24),
    _NptTransceiverTemperatureWarningHigh_Type()
)
nptTransceiverTemperatureWarningHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptTransceiverTemperatureWarningHigh.setStatus("current")
_NptTransceiverTemperatureAlarmLow_Type = Integer32
_NptTransceiverTemperatureAlarmLow_Object = MibTableColumn
nptTransceiverTemperatureAlarmLow = _NptTransceiverTemperatureAlarmLow_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 6, 1, 25),
    _NptTransceiverTemperatureAlarmLow_Type()
)
nptTransceiverTemperatureAlarmLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptTransceiverTemperatureAlarmLow.setStatus("current")
_NptTransceiverTemperatureAlarmHigh_Type = Integer32
_NptTransceiverTemperatureAlarmHigh_Object = MibTableColumn
nptTransceiverTemperatureAlarmHigh = _NptTransceiverTemperatureAlarmHigh_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 6, 1, 26),
    _NptTransceiverTemperatureAlarmHigh_Type()
)
nptTransceiverTemperatureAlarmHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptTransceiverTemperatureAlarmHigh.setStatus("current")
_NptThreeDotThreeVoltageSupplyWarningLow_Type = Integer32
_NptThreeDotThreeVoltageSupplyWarningLow_Object = MibTableColumn
nptThreeDotThreeVoltageSupplyWarningLow = _NptThreeDotThreeVoltageSupplyWarningLow_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 6, 1, 27),
    _NptThreeDotThreeVoltageSupplyWarningLow_Type()
)
nptThreeDotThreeVoltageSupplyWarningLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptThreeDotThreeVoltageSupplyWarningLow.setStatus("current")
_NptThreeDotThreeVoltageSupplyWarningHigh_Type = Integer32
_NptThreeDotThreeVoltageSupplyWarningHigh_Object = MibTableColumn
nptThreeDotThreeVoltageSupplyWarningHigh = _NptThreeDotThreeVoltageSupplyWarningHigh_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 6, 1, 28),
    _NptThreeDotThreeVoltageSupplyWarningHigh_Type()
)
nptThreeDotThreeVoltageSupplyWarningHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptThreeDotThreeVoltageSupplyWarningHigh.setStatus("current")
_NptThreeDotThreeVoltageSupplyAlarmLow_Type = Integer32
_NptThreeDotThreeVoltageSupplyAlarmLow_Object = MibTableColumn
nptThreeDotThreeVoltageSupplyAlarmLow = _NptThreeDotThreeVoltageSupplyAlarmLow_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 6, 1, 29),
    _NptThreeDotThreeVoltageSupplyAlarmLow_Type()
)
nptThreeDotThreeVoltageSupplyAlarmLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptThreeDotThreeVoltageSupplyAlarmLow.setStatus("current")
_NptThreeDotThreeVoltageSupplyAlarmHigh_Type = Integer32
_NptThreeDotThreeVoltageSupplyAlarmHigh_Object = MibTableColumn
nptThreeDotThreeVoltageSupplyAlarmHigh = _NptThreeDotThreeVoltageSupplyAlarmHigh_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 8, 6, 1, 30),
    _NptThreeDotThreeVoltageSupplyAlarmHigh_Type()
)
nptThreeDotThreeVoltageSupplyAlarmHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptThreeDotThreeVoltageSupplyAlarmHigh.setStatus("current")
_NptPowerConsumption_ObjectIdentity = ObjectIdentity
nptPowerConsumption = _NptPowerConsumption_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 9)
)
if mibBuilder.loadTexts:
    nptPowerConsumption.setStatus("current")
_NptChassisPowerTable_Object = MibTable
nptChassisPowerTable = _NptChassisPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 9, 1)
)
if mibBuilder.loadTexts:
    nptChassisPowerTable.setStatus("current")
_NptChassisPowerEntry_Object = MibTableRow
nptChassisPowerEntry = _NptChassisPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 9, 1, 1)
)
nptChassisPowerEntry.setIndexNames(
    (0, "NPT-SYSTEM-MIB", "nptChassisPowerObjectIndex"),
)
if mibBuilder.loadTexts:
    nptChassisPowerEntry.setStatus("current")


class _NptChassisPowerObjectIndex_Type(Integer32):
    """Custom type nptChassisPowerObjectIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NptChassisPowerObjectIndex_Type.__name__ = "Integer32"
_NptChassisPowerObjectIndex_Object = MibTableColumn
nptChassisPowerObjectIndex = _NptChassisPowerObjectIndex_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 9, 1, 1, 1),
    _NptChassisPowerObjectIndex_Type()
)
nptChassisPowerObjectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptChassisPowerObjectIndex.setStatus("current")
_NptChassisPowerObjectName_Type = DisplayString
_NptChassisPowerObjectName_Object = MibTableColumn
nptChassisPowerObjectName = _NptChassisPowerObjectName_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 9, 1, 1, 2),
    _NptChassisPowerObjectName_Type()
)
nptChassisPowerObjectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptChassisPowerObjectName.setStatus("current")
_NptChassisPowerCurrentInputDCVoltage_Type = Integer32
_NptChassisPowerCurrentInputDCVoltage_Object = MibTableColumn
nptChassisPowerCurrentInputDCVoltage = _NptChassisPowerCurrentInputDCVoltage_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 9, 1, 1, 3),
    _NptChassisPowerCurrentInputDCVoltage_Type()
)
nptChassisPowerCurrentInputDCVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptChassisPowerCurrentInputDCVoltage.setStatus("current")
_NptChassisPowerCurrentInputDCCurrent_Type = Integer32
_NptChassisPowerCurrentInputDCCurrent_Object = MibTableColumn
nptChassisPowerCurrentInputDCCurrent = _NptChassisPowerCurrentInputDCCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 9, 1, 1, 4),
    _NptChassisPowerCurrentInputDCCurrent_Type()
)
nptChassisPowerCurrentInputDCCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptChassisPowerCurrentInputDCCurrent.setStatus("current")
_NptChassisPowerMaxInputDCVoltage_Type = Integer32
_NptChassisPowerMaxInputDCVoltage_Object = MibTableColumn
nptChassisPowerMaxInputDCVoltage = _NptChassisPowerMaxInputDCVoltage_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 9, 1, 1, 5),
    _NptChassisPowerMaxInputDCVoltage_Type()
)
nptChassisPowerMaxInputDCVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptChassisPowerMaxInputDCVoltage.setStatus("current")
_NptChassisPowerMinInputDCVoltage_Type = Integer32
_NptChassisPowerMinInputDCVoltage_Object = MibTableColumn
nptChassisPowerMinInputDCVoltage = _NptChassisPowerMinInputDCVoltage_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 9, 1, 1, 6),
    _NptChassisPowerMinInputDCVoltage_Type()
)
nptChassisPowerMinInputDCVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptChassisPowerMinInputDCVoltage.setStatus("current")
_NptChassisPowerMaxInputDCCurrent_Type = Integer32
_NptChassisPowerMaxInputDCCurrent_Object = MibTableColumn
nptChassisPowerMaxInputDCCurrent = _NptChassisPowerMaxInputDCCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 9, 1, 1, 7),
    _NptChassisPowerMaxInputDCCurrent_Type()
)
nptChassisPowerMaxInputDCCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptChassisPowerMaxInputDCCurrent.setStatus("current")
_NptChassisPowerMinInputDCCurrent_Type = Integer32
_NptChassisPowerMinInputDCCurrent_Object = MibTableColumn
nptChassisPowerMinInputDCCurrent = _NptChassisPowerMinInputDCCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 9, 1, 1, 8),
    _NptChassisPowerMinInputDCCurrent_Type()
)
nptChassisPowerMinInputDCCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptChassisPowerMinInputDCCurrent.setStatus("current")
_NptChassisPowerCurrentPowerConsumption_Type = Integer32
_NptChassisPowerCurrentPowerConsumption_Object = MibTableColumn
nptChassisPowerCurrentPowerConsumption = _NptChassisPowerCurrentPowerConsumption_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 9, 1, 1, 9),
    _NptChassisPowerCurrentPowerConsumption_Type()
)
nptChassisPowerCurrentPowerConsumption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptChassisPowerCurrentPowerConsumption.setStatus("current")
_NptChassisPowerShelfPowerConsumption_Type = Integer32
_NptChassisPowerShelfPowerConsumption_Object = MibTableColumn
nptChassisPowerShelfPowerConsumption = _NptChassisPowerShelfPowerConsumption_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 9, 1, 1, 10),
    _NptChassisPowerShelfPowerConsumption_Type()
)
nptChassisPowerShelfPowerConsumption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptChassisPowerShelfPowerConsumption.setStatus("current")
_NptChassisPowerMaxOutputPower_Type = Integer32
_NptChassisPowerMaxOutputPower_Object = MibTableColumn
nptChassisPowerMaxOutputPower = _NptChassisPowerMaxOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 9, 1, 1, 11),
    _NptChassisPowerMaxOutputPower_Type()
)
nptChassisPowerMaxOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptChassisPowerMaxOutputPower.setStatus("current")
_NptShelfPowerTable_Object = MibTable
nptShelfPowerTable = _NptShelfPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 9, 2)
)
if mibBuilder.loadTexts:
    nptShelfPowerTable.setStatus("current")
_NptShelfPowerEntry_Object = MibTableRow
nptShelfPowerEntry = _NptShelfPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 9, 2, 1)
)
nptShelfPowerEntry.setIndexNames(
    (0, "NPT-SYSTEM-MIB", "nptShelfPowerObjectIndex"),
)
if mibBuilder.loadTexts:
    nptShelfPowerEntry.setStatus("current")


class _NptShelfPowerObjectIndex_Type(Integer32):
    """Custom type nptShelfPowerObjectIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NptShelfPowerObjectIndex_Type.__name__ = "Integer32"
_NptShelfPowerObjectIndex_Object = MibTableColumn
nptShelfPowerObjectIndex = _NptShelfPowerObjectIndex_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 9, 2, 1, 1),
    _NptShelfPowerObjectIndex_Type()
)
nptShelfPowerObjectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptShelfPowerObjectIndex.setStatus("current")
_NptShelfPowerObjectName_Type = DisplayString
_NptShelfPowerObjectName_Object = MibTableColumn
nptShelfPowerObjectName = _NptShelfPowerObjectName_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 9, 2, 1, 2),
    _NptShelfPowerObjectName_Type()
)
nptShelfPowerObjectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptShelfPowerObjectName.setStatus("current")
_NptShelfPowerTotalPowerBudget_Type = Integer32
_NptShelfPowerTotalPowerBudget_Object = MibTableColumn
nptShelfPowerTotalPowerBudget = _NptShelfPowerTotalPowerBudget_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 9, 2, 1, 3),
    _NptShelfPowerTotalPowerBudget_Type()
)
nptShelfPowerTotalPowerBudget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptShelfPowerTotalPowerBudget.setStatus("current")
_NptShelfPowerAssignedBudget_Type = Integer32
_NptShelfPowerAssignedBudget_Object = MibTableColumn
nptShelfPowerAssignedBudget = _NptShelfPowerAssignedBudget_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 9, 2, 1, 4),
    _NptShelfPowerAssignedBudget_Type()
)
nptShelfPowerAssignedBudget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptShelfPowerAssignedBudget.setStatus("current")
_NptShelfPowerRemainingBudget_Type = Integer32
_NptShelfPowerRemainingBudget_Object = MibTableColumn
nptShelfPowerRemainingBudget = _NptShelfPowerRemainingBudget_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 9, 2, 1, 5),
    _NptShelfPowerRemainingBudget_Type()
)
nptShelfPowerRemainingBudget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptShelfPowerRemainingBudget.setStatus("current")
_NptShelfPowerStatus_Type = DisplayString
_NptShelfPowerStatus_Object = MibTableColumn
nptShelfPowerStatus = _NptShelfPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 9, 2, 1, 6),
    _NptShelfPowerStatus_Type()
)
nptShelfPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptShelfPowerStatus.setStatus("current")
_NptShelfPowerActualPowerConsumption_Type = Integer32
_NptShelfPowerActualPowerConsumption_Object = MibTableColumn
nptShelfPowerActualPowerConsumption = _NptShelfPowerActualPowerConsumption_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 9, 2, 1, 7),
    _NptShelfPowerActualPowerConsumption_Type()
)
nptShelfPowerActualPowerConsumption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptShelfPowerActualPowerConsumption.setStatus("current")
_NptChassisEnvironment_ObjectIdentity = ObjectIdentity
nptChassisEnvironment = _NptChassisEnvironment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 10)
)
if mibBuilder.loadTexts:
    nptChassisEnvironment.setStatus("current")
_NptFanStateTable_Object = MibTable
nptFanStateTable = _NptFanStateTable_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 10, 1)
)
if mibBuilder.loadTexts:
    nptFanStateTable.setStatus("current")
_NptFanStateEntry_Object = MibTableRow
nptFanStateEntry = _NptFanStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 10, 1, 1)
)
nptFanStateEntry.setIndexNames(
    (0, "NPT-SYSTEM-MIB", "nptFanStateIndex"),
)
if mibBuilder.loadTexts:
    nptFanStateEntry.setStatus("current")


class _NptFanStateIndex_Type(Integer32):
    """Custom type nptFanStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NptFanStateIndex_Type.__name__ = "Integer32"
_NptFanStateIndex_Object = MibTableColumn
nptFanStateIndex = _NptFanStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 10, 1, 1, 1),
    _NptFanStateIndex_Type()
)
nptFanStateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptFanStateIndex.setStatus("current")
_NptFanStateObjectName_Type = DisplayString
_NptFanStateObjectName_Object = MibTableColumn
nptFanStateObjectName = _NptFanStateObjectName_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 10, 1, 1, 2),
    _NptFanStateObjectName_Type()
)
nptFanStateObjectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptFanStateObjectName.setStatus("current")
_NptFanStateTurboMode_Type = DisplayString
_NptFanStateTurboMode_Object = MibTableColumn
nptFanStateTurboMode = _NptFanStateTurboMode_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 10, 1, 1, 3),
    _NptFanStateTurboMode_Type()
)
nptFanStateTurboMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptFanStateTurboMode.setStatus("current")
_NptFanStateSpeed_Type = DisplayString
_NptFanStateSpeed_Object = MibTableColumn
nptFanStateSpeed = _NptFanStateSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 10, 1, 1, 4),
    _NptFanStateSpeed_Type()
)
nptFanStateSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptFanStateSpeed.setStatus("current")
_NptFanStateLevel_Type = DisplayString
_NptFanStateLevel_Object = MibTableColumn
nptFanStateLevel = _NptFanStateLevel_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 10, 1, 1, 5),
    _NptFanStateLevel_Type()
)
nptFanStateLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptFanStateLevel.setStatus("current")
_NptFanStatePowerVoltage_Type = DisplayString
_NptFanStatePowerVoltage_Object = MibTableColumn
nptFanStatePowerVoltage = _NptFanStatePowerVoltage_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 10, 1, 1, 6),
    _NptFanStatePowerVoltage_Type()
)
nptFanStatePowerVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptFanStatePowerVoltage.setStatus("current")
_NptFanUnitStateTable_Object = MibTable
nptFanUnitStateTable = _NptFanUnitStateTable_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 10, 2)
)
if mibBuilder.loadTexts:
    nptFanUnitStateTable.setStatus("current")
_NptFanUnitStateEntry_Object = MibTableRow
nptFanUnitStateEntry = _NptFanUnitStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 10, 2, 1)
)
nptFanUnitStateEntry.setIndexNames(
    (0, "NPT-SYSTEM-MIB", "nptFanUnitSlot"),
    (0, "NPT-SYSTEM-MIB", "nptFanUnitStateID"),
    (0, "NPT-SYSTEM-MIB", "nptFanUnitStateObjectName"),
)
if mibBuilder.loadTexts:
    nptFanUnitStateEntry.setStatus("current")


class _NptFanUnitSlot_Type(Integer32):
    """Custom type nptFanUnitSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NptFanUnitSlot_Type.__name__ = "Integer32"
_NptFanUnitSlot_Object = MibTableColumn
nptFanUnitSlot = _NptFanUnitSlot_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 10, 2, 1, 1),
    _NptFanUnitSlot_Type()
)
nptFanUnitSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptFanUnitSlot.setStatus("current")


class _NptFanUnitStateID_Type(Integer32):
    """Custom type nptFanUnitStateID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NptFanUnitStateID_Type.__name__ = "Integer32"
_NptFanUnitStateID_Object = MibTableColumn
nptFanUnitStateID = _NptFanUnitStateID_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 10, 2, 1, 2),
    _NptFanUnitStateID_Type()
)
nptFanUnitStateID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptFanUnitStateID.setStatus("current")
_NptFanUnitStateObjectName_Type = DisplayString
_NptFanUnitStateObjectName_Object = MibTableColumn
nptFanUnitStateObjectName = _NptFanUnitStateObjectName_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 10, 2, 1, 3),
    _NptFanUnitStateObjectName_Type()
)
nptFanUnitStateObjectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptFanUnitStateObjectName.setStatus("current")
_NptFanUnitStateRPM_Type = Integer32
_NptFanUnitStateRPM_Object = MibTableColumn
nptFanUnitStateRPM = _NptFanUnitStateRPM_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 10, 2, 1, 4),
    _NptFanUnitStateRPM_Type()
)
nptFanUnitStateRPM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptFanUnitStateRPM.setStatus("current")
_NptFanUnitStateLevel_Type = DisplayString
_NptFanUnitStateLevel_Object = MibTableColumn
nptFanUnitStateLevel = _NptFanUnitStateLevel_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 10, 2, 1, 5),
    _NptFanUnitStateLevel_Type()
)
nptFanUnitStateLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptFanUnitStateLevel.setStatus("current")
_NptFanUnitStateStatus_Type = DisplayString
_NptFanUnitStateStatus_Object = MibTableColumn
nptFanUnitStateStatus = _NptFanUnitStateStatus_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 10, 2, 1, 6),
    _NptFanUnitStateStatus_Type()
)
nptFanUnitStateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptFanUnitStateStatus.setStatus("current")
_NptCardTemperatureTable_Object = MibTable
nptCardTemperatureTable = _NptCardTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 10, 3)
)
if mibBuilder.loadTexts:
    nptCardTemperatureTable.setStatus("current")
_NptCardTemperatureEntry_Object = MibTableRow
nptCardTemperatureEntry = _NptCardTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 10, 3, 1)
)
nptCardTemperatureEntry.setIndexNames(
    (0, "NPT-SYSTEM-MIB", "nptSlotIndex"),
)
if mibBuilder.loadTexts:
    nptCardTemperatureEntry.setStatus("current")


class _NptSlotIndex_Type(Unsigned32):
    """Custom type nptSlotIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NptSlotIndex_Type.__name__ = "Unsigned32"
_NptSlotIndex_Object = MibTableColumn
nptSlotIndex = _NptSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 10, 3, 1, 1),
    _NptSlotIndex_Type()
)
nptSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptSlotIndex.setStatus("current")
_NptCardName_Type = DisplayString
_NptCardName_Object = MibTableColumn
nptCardName = _NptCardName_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 10, 3, 1, 2),
    _NptCardName_Type()
)
nptCardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptCardName.setStatus("current")
_NptStatus_Type = DisplayString
_NptStatus_Object = MibTableColumn
nptStatus = _NptStatus_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 10, 3, 1, 3),
    _NptStatus_Type()
)
nptStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptStatus.setStatus("current")
_NptTemperature_Type = Integer32
_NptTemperature_Object = MibTableColumn
nptTemperature = _NptTemperature_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 10, 3, 1, 4),
    _NptTemperature_Type()
)
nptTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptTemperature.setStatus("current")
_NptHighAlarmThreshold_Type = Integer32
_NptHighAlarmThreshold_Object = MibTableColumn
nptHighAlarmThreshold = _NptHighAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 10, 3, 1, 5),
    _NptHighAlarmThreshold_Type()
)
nptHighAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptHighAlarmThreshold.setStatus("current")
_NptHighWarnThreshold_Type = Integer32
_NptHighWarnThreshold_Object = MibTableColumn
nptHighWarnThreshold = _NptHighWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 10, 3, 1, 6),
    _NptHighWarnThreshold_Type()
)
nptHighWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptHighWarnThreshold.setStatus("current")
_NptLowAlarmThreshold_Type = Integer32
_NptLowAlarmThreshold_Object = MibTableColumn
nptLowAlarmThreshold = _NptLowAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 10, 3, 1, 7),
    _NptLowAlarmThreshold_Type()
)
nptLowAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptLowAlarmThreshold.setStatus("current")
_NptLowWarnThreshold_Type = Integer32
_NptLowWarnThreshold_Object = MibTableColumn
nptLowWarnThreshold = _NptLowWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2, 1, 10, 3, 1, 8),
    _NptLowWarnThreshold_Type()
)
nptLowWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nptLowWarnThreshold.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NPT-SYSTEM-MIB",
    **{"nptSystemModule": nptSystemModule,
       "nptMibVersion": nptMibVersion,
       "nptNESoftwareVersion": nptNESoftwareVersion,
       "nptBoardInfoTable": nptBoardInfoTable,
       "nptBoardInfoEntry": nptBoardInfoEntry,
       "nptSlotId": nptSlotId,
       "nptPhysicalBoardType": nptPhysicalBoardType,
       "nptLogicalBoardType": nptLogicalBoardType,
       "nptCardDescription": nptCardDescription,
       "nptCardSerialNumber": nptCardSerialNumber,
       "nptHwRevision": nptHwRevision,
       "nptHwOption": nptHwOption,
       "nptEPLDRevision": nptEPLDRevision,
       "nptBootVersion": nptBootVersion,
       "nptFPGAVersion": nptFPGAVersion,
       "nptSWRevision": nptSWRevision,
       "nptVendor": nptVendor,
       "nptMacAddress": nptMacAddress,
       "nptSysTrapConfig": nptSysTrapConfig,
       "nptManagerTable": nptManagerTable,
       "nptManagerEntry": nptManagerEntry,
       "nptTrapIpAddress": nptTrapIpAddress,
       "nptTrapPortNumber": nptTrapPortNumber,
       "nptTrapVersion": nptTrapVersion,
       "nptIsAdministrator": nptIsAdministrator,
       "nptCpuInfoTable": nptCpuInfoTable,
       "nptCpuInfoEntry": nptCpuInfoEntry,
       "nptCpuSlotId": nptCpuSlotId,
       "nptCpuSlotType": nptCpuSlotType,
       "nptCpuPhysicalBoardType": nptCpuPhysicalBoardType,
       "nptCpuType": nptCpuType,
       "nptCpuRevision": nptCpuRevision,
       "nptCpuSpeed": nptCpuSpeed,
       "nptCpuCacheSize": nptCpuCacheSize,
       "nptTotalProcesses": nptTotalProcesses,
       "nptProcessesStatus": nptProcessesStatus,
       "nptUptime": nptUptime,
       "nptLoadAverage": nptLoadAverage,
       "nptUserUtilization": nptUserUtilization,
       "nptNiceUtilization": nptNiceUtilization,
       "nptSystemUtilization": nptSystemUtilization,
       "nptWaitingUtilization": nptWaitingUtilization,
       "nptHwInterupUtilization": nptHwInterupUtilization,
       "nptSoftInterupUtilization": nptSoftInterupUtilization,
       "nptIdle": nptIdle,
       "nptMemoryInfoTable": nptMemoryInfoTable,
       "nptMemoryInfoEntry": nptMemoryInfoEntry,
       "nptMemorySlotId": nptMemorySlotId,
       "nptMemorySlotType": nptMemorySlotType,
       "nptMemoryPhysicalBoardType": nptMemoryPhysicalBoardType,
       "nptMemoryFree": nptMemoryFree,
       "nptMemoryUsed": nptMemoryUsed,
       "nptMemoryBuffers": nptMemoryBuffers,
       "nptMemoryTotal": nptMemoryTotal,
       "nptMemoryFreeSwap": nptMemoryFreeSwap,
       "nptMemoryUsedSwap": nptMemoryUsedSwap,
       "nptMemoryCachedSwap": nptMemoryCachedSwap,
       "nptMemoryTotalSwap": nptMemoryTotalSwap,
       "nptSysStartTime": nptSysStartTime,
       "nptTransceiverInformation": nptTransceiverInformation,
       "nptTransceiverConfigurationTable": nptTransceiverConfigurationTable,
       "nptTransceiverConfigurationEntry": nptTransceiverConfigurationEntry,
       "nptTransceiverConfigurationIndex": nptTransceiverConfigurationIndex,
       "nptTransceiverConfigurationName": nptTransceiverConfigurationName,
       "nptExpectedTransceiverType": nptExpectedTransceiverType,
       "nptExpectedApplicationCode": nptExpectedApplicationCode,
       "nptRate": nptRate,
       "nptConnectorType": nptConnectorType,
       "nptNominalBitrate": nptNominalBitrate,
       "nptSupportedLinkLength": nptSupportedLinkLength,
       "nptTransmitedWavelength": nptTransmitedWavelength,
       "nptChannelColor": nptChannelColor,
       "nptSupportedFiberType": nptSupportedFiberType,
       "nptTransceiverStatusTable": nptTransceiverStatusTable,
       "nptTransceiverStatusEntry": nptTransceiverStatusEntry,
       "nptTransceiverStatusIndex": nptTransceiverStatusIndex,
       "nptTransceiverStatusName": nptTransceiverStatusName,
       "nptOperationalState": nptOperationalState,
       "nptActualLaserTransmitStatus": nptActualLaserTransmitStatus,
       "nptReceivedLOSStatus": nptReceivedLOSStatus,
       "nptActualNominalBitrate": nptActualNominalBitrate,
       "nptActualSupportedLinkLength": nptActualSupportedLinkLength,
       "nptActualTransmitedWavelength": nptActualTransmitedWavelength,
       "nptActualSupportedFiberType": nptActualSupportedFiberType,
       "nptLineCode": nptLineCode,
       "nptCoherent": nptCoherent,
       "nptSubBand": nptSubBand,
       "nptMeasuredRxOSNR": nptMeasuredRxOSNR,
       "nptTxOSNR": nptTxOSNR,
       "nptTransceiverInventoryTable": nptTransceiverInventoryTable,
       "nptTransceiverInventoryEntry": nptTransceiverInventoryEntry,
       "nptTransceiverInventoryIndex": nptTransceiverInventoryIndex,
       "nptTransceiverInventoryName": nptTransceiverInventoryName,
       "nptActualTransceiverType": nptActualTransceiverType,
       "nptTransceiverInventoryVendor": nptTransceiverInventoryVendor,
       "nptSerialNumber": nptSerialNumber,
       "nptHWRevision": nptHWRevision,
       "nptHWOption": nptHWOption,
       "nptGeneralDescription": nptGeneralDescription,
       "nptModuleSubType": nptModuleSubType,
       "nptActualApplicationCode": nptActualApplicationCode,
       "nptSupportChannelNumber": nptSupportChannelNumber,
       "nptWDMFirstChannelnumber": nptWDMFirstChannelnumber,
       "nptChannelSpacing": nptChannelSpacing,
       "nptTransceiverPower": nptTransceiverPower,
       "nptTransceiverPowerTable": nptTransceiverPowerTable,
       "nptTransceiverPowerEntry": nptTransceiverPowerEntry,
       "nptTransceiverPowerIndex": nptTransceiverPowerIndex,
       "nptTransceiverPowerName": nptTransceiverPowerName,
       "nptLaservoltage": nptLaservoltage,
       "nptLaserbiascurrent": nptLaserbiascurrent,
       "nptLasertemperature": nptLasertemperature,
       "nptTxlaserpower": nptTxlaserpower,
       "nptRxlaserpower": nptRxlaserpower,
       "nptMaxrxpowerlane": nptMaxrxpowerlane,
       "nptMinrxpowerlane": nptMinrxpowerlane,
       "nptMaxtxpowerlane": nptMaxtxpowerlane,
       "nptMintxpowerlane": nptMintxpowerlane,
       "nptMaxLaserBiasCur": nptMaxLaserBiasCur,
       "nptTransceiverPowerMultilaneTable": nptTransceiverPowerMultilaneTable,
       "nptTransceiverPowerMultilaneEntry": nptTransceiverPowerMultilaneEntry,
       "nptTransceiverPowerMultilaneIndex": nptTransceiverPowerMultilaneIndex,
       "nptLaneNum": nptLaneNum,
       "nptTransceiverPowerMultilaneName": nptTransceiverPowerMultilaneName,
       "nptLaneTxLaserPower": nptLaneTxLaserPower,
       "nptLaneRxLaserPower": nptLaneRxLaserPower,
       "nptLaneLaserBiasCur": nptLaneLaserBiasCur,
       "nptTunnableTransceiverConfigurationTable": nptTunnableTransceiverConfigurationTable,
       "nptTunnableTransceiverConfigurationEntry": nptTunnableTransceiverConfigurationEntry,
       "nptTunnableTransceiverConfigurationIndex": nptTunnableTransceiverConfigurationIndex,
       "nptTunnableTransceiverConfigurationName": nptTunnableTransceiverConfigurationName,
       "nptChannelFrequency": nptChannelFrequency,
       "nptWavelength": nptWavelength,
       "nptTxDither": nptTxDither,
       "nptFrequencyTuning": nptFrequencyTuning,
       "nptWavelengthTuning": nptWavelengthTuning,
       "nptTxDitherSupport": nptTxDitherSupport,
       "nptFirstFrequency": nptFirstFrequency,
       "nptLastFrequency": nptLastFrequency,
       "nptMinimumSupportedGridSpacing": nptMinimumSupportedGridSpacing,
       "nptTransceiverThresholdTable": nptTransceiverThresholdTable,
       "nptTransceiverThresholdEntry": nptTransceiverThresholdEntry,
       "nptTransceiverThresholdIfIndex": nptTransceiverThresholdIfIndex,
       "nptTransceiverThresholdPortName": nptTransceiverThresholdPortName,
       "nptTxOpticalPowerWarningLowTotal": nptTxOpticalPowerWarningLowTotal,
       "nptTxOpticalPowerWarningHighTotal": nptTxOpticalPowerWarningHighTotal,
       "nptTxOpticalPowerAlarmLowTotal": nptTxOpticalPowerAlarmLowTotal,
       "nptTxOpticalPowerAlarmHighTotal": nptTxOpticalPowerAlarmHighTotal,
       "nptRxOpticalPowerWarningLowTotal": nptRxOpticalPowerWarningLowTotal,
       "nptRxOpticalPowerWarningHighTotal": nptRxOpticalPowerWarningHighTotal,
       "nptRxOpticalPowerAlarmLowTotal": nptRxOpticalPowerAlarmLowTotal,
       "nptRxOpticalPowerAlarmHighTotal": nptRxOpticalPowerAlarmHighTotal,
       "nptTxOpticalPowerWarningLowPerLane": nptTxOpticalPowerWarningLowPerLane,
       "nptTxOpticalPowerWarningHighPerLane": nptTxOpticalPowerWarningHighPerLane,
       "nptTxOpticalPowerAlarmLowPerLane": nptTxOpticalPowerAlarmLowPerLane,
       "nptTxOpticalPowerAlarmHighPerLane": nptTxOpticalPowerAlarmHighPerLane,
       "nptRxOpticalPowerWarningLowPerLane": nptRxOpticalPowerWarningLowPerLane,
       "nptRxOpticalPowerWarningHighPerLane": nptRxOpticalPowerWarningHighPerLane,
       "nptRxOpticalPowerAlarmLowPerLane": nptRxOpticalPowerAlarmLowPerLane,
       "nptRxOpticalPowerAlarmHighPerLane": nptRxOpticalPowerAlarmHighPerLane,
       "nptTxLaserBiasCurrentWarningLow": nptTxLaserBiasCurrentWarningLow,
       "nptTxLaserBiasCurrentWarningHigh": nptTxLaserBiasCurrentWarningHigh,
       "nptTxLaserBiasCurrentAlarmLow": nptTxLaserBiasCurrentAlarmLow,
       "nptTxLaserBiasCurrentAlarmHigh": nptTxLaserBiasCurrentAlarmHigh,
       "nptTransceiverTemperatureWarningLow": nptTransceiverTemperatureWarningLow,
       "nptTransceiverTemperatureWarningHigh": nptTransceiverTemperatureWarningHigh,
       "nptTransceiverTemperatureAlarmLow": nptTransceiverTemperatureAlarmLow,
       "nptTransceiverTemperatureAlarmHigh": nptTransceiverTemperatureAlarmHigh,
       "nptThreeDotThreeVoltageSupplyWarningLow": nptThreeDotThreeVoltageSupplyWarningLow,
       "nptThreeDotThreeVoltageSupplyWarningHigh": nptThreeDotThreeVoltageSupplyWarningHigh,
       "nptThreeDotThreeVoltageSupplyAlarmLow": nptThreeDotThreeVoltageSupplyAlarmLow,
       "nptThreeDotThreeVoltageSupplyAlarmHigh": nptThreeDotThreeVoltageSupplyAlarmHigh,
       "nptPowerConsumption": nptPowerConsumption,
       "nptChassisPowerTable": nptChassisPowerTable,
       "nptChassisPowerEntry": nptChassisPowerEntry,
       "nptChassisPowerObjectIndex": nptChassisPowerObjectIndex,
       "nptChassisPowerObjectName": nptChassisPowerObjectName,
       "nptChassisPowerCurrentInputDCVoltage": nptChassisPowerCurrentInputDCVoltage,
       "nptChassisPowerCurrentInputDCCurrent": nptChassisPowerCurrentInputDCCurrent,
       "nptChassisPowerMaxInputDCVoltage": nptChassisPowerMaxInputDCVoltage,
       "nptChassisPowerMinInputDCVoltage": nptChassisPowerMinInputDCVoltage,
       "nptChassisPowerMaxInputDCCurrent": nptChassisPowerMaxInputDCCurrent,
       "nptChassisPowerMinInputDCCurrent": nptChassisPowerMinInputDCCurrent,
       "nptChassisPowerCurrentPowerConsumption": nptChassisPowerCurrentPowerConsumption,
       "nptChassisPowerShelfPowerConsumption": nptChassisPowerShelfPowerConsumption,
       "nptChassisPowerMaxOutputPower": nptChassisPowerMaxOutputPower,
       "nptShelfPowerTable": nptShelfPowerTable,
       "nptShelfPowerEntry": nptShelfPowerEntry,
       "nptShelfPowerObjectIndex": nptShelfPowerObjectIndex,
       "nptShelfPowerObjectName": nptShelfPowerObjectName,
       "nptShelfPowerTotalPowerBudget": nptShelfPowerTotalPowerBudget,
       "nptShelfPowerAssignedBudget": nptShelfPowerAssignedBudget,
       "nptShelfPowerRemainingBudget": nptShelfPowerRemainingBudget,
       "nptShelfPowerStatus": nptShelfPowerStatus,
       "nptShelfPowerActualPowerConsumption": nptShelfPowerActualPowerConsumption,
       "nptChassisEnvironment": nptChassisEnvironment,
       "nptFanStateTable": nptFanStateTable,
       "nptFanStateEntry": nptFanStateEntry,
       "nptFanStateIndex": nptFanStateIndex,
       "nptFanStateObjectName": nptFanStateObjectName,
       "nptFanStateTurboMode": nptFanStateTurboMode,
       "nptFanStateSpeed": nptFanStateSpeed,
       "nptFanStateLevel": nptFanStateLevel,
       "nptFanStatePowerVoltage": nptFanStatePowerVoltage,
       "nptFanUnitStateTable": nptFanUnitStateTable,
       "nptFanUnitStateEntry": nptFanUnitStateEntry,
       "nptFanUnitSlot": nptFanUnitSlot,
       "nptFanUnitStateID": nptFanUnitStateID,
       "nptFanUnitStateObjectName": nptFanUnitStateObjectName,
       "nptFanUnitStateRPM": nptFanUnitStateRPM,
       "nptFanUnitStateLevel": nptFanUnitStateLevel,
       "nptFanUnitStateStatus": nptFanUnitStateStatus,
       "nptCardTemperatureTable": nptCardTemperatureTable,
       "nptCardTemperatureEntry": nptCardTemperatureEntry,
       "nptSlotIndex": nptSlotIndex,
       "nptCardName": nptCardName,
       "nptStatus": nptStatus,
       "nptTemperature": nptTemperature,
       "nptHighAlarmThreshold": nptHighAlarmThreshold,
       "nptHighWarnThreshold": nptHighWarnThreshold,
       "nptLowAlarmThreshold": nptLowAlarmThreshold,
       "nptLowWarnThreshold": nptLowWarnThreshold}
)
