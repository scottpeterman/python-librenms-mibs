# SNMP MIB module (FS-MEMORY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fs\FS-MEMORY-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:45:49 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

fsMemoryMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 35)
)
if mibBuilder.loadTexts:
    fsMemoryMIB.setRevisions(
        ("2003-10-14 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Percent(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



# MIB Managed Objects in the order of their OIDs

_FsMemoryPoolMIBObjects_ObjectIdentity = ObjectIdentity
fsMemoryPoolMIBObjects = _FsMemoryPoolMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 35, 1)
)
_FsMemoryPoolUtilizationTable_Object = MibTable
fsMemoryPoolUtilizationTable = _FsMemoryPoolUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 35, 1, 1)
)
if mibBuilder.loadTexts:
    fsMemoryPoolUtilizationTable.setStatus("current")
_FsMemoryPoolUtilizationEntry_Object = MibTableRow
fsMemoryPoolUtilizationEntry = _FsMemoryPoolUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 35, 1, 1, 1)
)
fsMemoryPoolUtilizationEntry.setIndexNames(
    (0, "FS-MEMORY-MIB", "fsMemoryPoolIndex"),
)
if mibBuilder.loadTexts:
    fsMemoryPoolUtilizationEntry.setStatus("current")
_FsMemoryPoolIndex_Type = Integer32
_FsMemoryPoolIndex_Object = MibTableColumn
fsMemoryPoolIndex = _FsMemoryPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 35, 1, 1, 1, 1),
    _FsMemoryPoolIndex_Type()
)
fsMemoryPoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMemoryPoolIndex.setStatus("current")
_FsMemoryPoolName_Type = DisplayString
_FsMemoryPoolName_Object = MibTableColumn
fsMemoryPoolName = _FsMemoryPoolName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 35, 1, 1, 1, 2),
    _FsMemoryPoolName_Type()
)
fsMemoryPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMemoryPoolName.setStatus("current")
_FsMemoryPoolCurrentUtilization_Type = Percent
_FsMemoryPoolCurrentUtilization_Object = MibTableColumn
fsMemoryPoolCurrentUtilization = _FsMemoryPoolCurrentUtilization_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 35, 1, 1, 1, 3),
    _FsMemoryPoolCurrentUtilization_Type()
)
fsMemoryPoolCurrentUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMemoryPoolCurrentUtilization.setStatus("current")
_FsMemoryPoolLowestUtilization_Type = Percent
_FsMemoryPoolLowestUtilization_Object = MibTableColumn
fsMemoryPoolLowestUtilization = _FsMemoryPoolLowestUtilization_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 35, 1, 1, 1, 4),
    _FsMemoryPoolLowestUtilization_Type()
)
fsMemoryPoolLowestUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMemoryPoolLowestUtilization.setStatus("current")
_FsMemoryPoolLargestUtilization_Type = Percent
_FsMemoryPoolLargestUtilization_Object = MibTableColumn
fsMemoryPoolLargestUtilization = _FsMemoryPoolLargestUtilization_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 35, 1, 1, 1, 5),
    _FsMemoryPoolLargestUtilization_Type()
)
fsMemoryPoolLargestUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMemoryPoolLargestUtilization.setStatus("current")
_FsMemoryPoolSize_Type = Integer32
_FsMemoryPoolSize_Object = MibTableColumn
fsMemoryPoolSize = _FsMemoryPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 35, 1, 1, 1, 6),
    _FsMemoryPoolSize_Type()
)
fsMemoryPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMemoryPoolSize.setStatus("current")
_FsMemoryPoolUsed_Type = Integer32
_FsMemoryPoolUsed_Object = MibTableColumn
fsMemoryPoolUsed = _FsMemoryPoolUsed_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 35, 1, 1, 1, 7),
    _FsMemoryPoolUsed_Type()
)
fsMemoryPoolUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMemoryPoolUsed.setStatus("current")
_FsMemoryPoolFree_Type = Integer32
_FsMemoryPoolFree_Object = MibTableColumn
fsMemoryPoolFree = _FsMemoryPoolFree_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 35, 1, 1, 1, 8),
    _FsMemoryPoolFree_Type()
)
fsMemoryPoolFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMemoryPoolFree.setStatus("current")
_FsMemoryPoolWarning_Type = Percent
_FsMemoryPoolWarning_Object = MibTableColumn
fsMemoryPoolWarning = _FsMemoryPoolWarning_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 35, 1, 1, 1, 9),
    _FsMemoryPoolWarning_Type()
)
fsMemoryPoolWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMemoryPoolWarning.setStatus("current")
_FsMemoryPoolCritical_Type = Percent
_FsMemoryPoolCritical_Object = MibTableColumn
fsMemoryPoolCritical = _FsMemoryPoolCritical_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 35, 1, 1, 1, 10),
    _FsMemoryPoolCritical_Type()
)
fsMemoryPoolCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMemoryPoolCritical.setStatus("current")
_FsMemoryPoolAverageUtilization_Type = Percent
_FsMemoryPoolAverageUtilization_Object = MibTableColumn
fsMemoryPoolAverageUtilization = _FsMemoryPoolAverageUtilization_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 35, 1, 1, 1, 11),
    _FsMemoryPoolAverageUtilization_Type()
)
fsMemoryPoolAverageUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMemoryPoolAverageUtilization.setStatus("current")
_FsMemoryPoolTotalSize_Type = Gauge32
_FsMemoryPoolTotalSize_Object = MibTableColumn
fsMemoryPoolTotalSize = _FsMemoryPoolTotalSize_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 35, 1, 1, 1, 12),
    _FsMemoryPoolTotalSize_Type()
)
fsMemoryPoolTotalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMemoryPoolTotalSize.setStatus("current")
_FsMemoryPoolUsedSize_Type = Gauge32
_FsMemoryPoolUsedSize_Object = MibTableColumn
fsMemoryPoolUsedSize = _FsMemoryPoolUsedSize_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 35, 1, 1, 1, 13),
    _FsMemoryPoolUsedSize_Type()
)
fsMemoryPoolUsedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMemoryPoolUsedSize.setStatus("current")
_FsMemoryPoolFreeSize_Type = Gauge32
_FsMemoryPoolFreeSize_Object = MibTableColumn
fsMemoryPoolFreeSize = _FsMemoryPoolFreeSize_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 35, 1, 1, 1, 14),
    _FsMemoryPoolFreeSize_Type()
)
fsMemoryPoolFreeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMemoryPoolFreeSize.setStatus("current")
_FsNodeMemoryPoolTable_Object = MibTable
fsNodeMemoryPoolTable = _FsNodeMemoryPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 35, 1, 2)
)
if mibBuilder.loadTexts:
    fsNodeMemoryPoolTable.setStatus("current")
_FsNodeMemoryPoolEntry_Object = MibTableRow
fsNodeMemoryPoolEntry = _FsNodeMemoryPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 35, 1, 2, 1)
)
fsNodeMemoryPoolEntry.setIndexNames(
    (0, "FS-MEMORY-MIB", "fsNodeMemoryPoolIndex"),
)
if mibBuilder.loadTexts:
    fsNodeMemoryPoolEntry.setStatus("current")
_FsNodeMemoryPoolIndex_Type = Integer32
_FsNodeMemoryPoolIndex_Object = MibTableColumn
fsNodeMemoryPoolIndex = _FsNodeMemoryPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 35, 1, 2, 1, 1),
    _FsNodeMemoryPoolIndex_Type()
)
fsNodeMemoryPoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsNodeMemoryPoolIndex.setStatus("current")
_FsNodeMemoryPoolName_Type = DisplayString
_FsNodeMemoryPoolName_Object = MibTableColumn
fsNodeMemoryPoolName = _FsNodeMemoryPoolName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 35, 1, 2, 1, 2),
    _FsNodeMemoryPoolName_Type()
)
fsNodeMemoryPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsNodeMemoryPoolName.setStatus("current")
_FsNodeMemoryPoolCurrentUtilization_Type = Percent
_FsNodeMemoryPoolCurrentUtilization_Object = MibTableColumn
fsNodeMemoryPoolCurrentUtilization = _FsNodeMemoryPoolCurrentUtilization_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 35, 1, 2, 1, 3),
    _FsNodeMemoryPoolCurrentUtilization_Type()
)
fsNodeMemoryPoolCurrentUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsNodeMemoryPoolCurrentUtilization.setStatus("current")
_FsNodeMemoryPoolLowestUtilization_Type = Percent
_FsNodeMemoryPoolLowestUtilization_Object = MibTableColumn
fsNodeMemoryPoolLowestUtilization = _FsNodeMemoryPoolLowestUtilization_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 35, 1, 2, 1, 4),
    _FsNodeMemoryPoolLowestUtilization_Type()
)
fsNodeMemoryPoolLowestUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsNodeMemoryPoolLowestUtilization.setStatus("current")
_FsNodeMemoryPoolLargestUtilization_Type = Percent
_FsNodeMemoryPoolLargestUtilization_Object = MibTableColumn
fsNodeMemoryPoolLargestUtilization = _FsNodeMemoryPoolLargestUtilization_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 35, 1, 2, 1, 5),
    _FsNodeMemoryPoolLargestUtilization_Type()
)
fsNodeMemoryPoolLargestUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsNodeMemoryPoolLargestUtilization.setStatus("current")
_FsNodeMemoryPoolSize_Type = Integer32
_FsNodeMemoryPoolSize_Object = MibTableColumn
fsNodeMemoryPoolSize = _FsNodeMemoryPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 35, 1, 2, 1, 6),
    _FsNodeMemoryPoolSize_Type()
)
fsNodeMemoryPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsNodeMemoryPoolSize.setStatus("current")
_FsNodeMemoryPoolUsed_Type = Integer32
_FsNodeMemoryPoolUsed_Object = MibTableColumn
fsNodeMemoryPoolUsed = _FsNodeMemoryPoolUsed_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 35, 1, 2, 1, 7),
    _FsNodeMemoryPoolUsed_Type()
)
fsNodeMemoryPoolUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsNodeMemoryPoolUsed.setStatus("current")
_FsNodeMemoryPoolFree_Type = Integer32
_FsNodeMemoryPoolFree_Object = MibTableColumn
fsNodeMemoryPoolFree = _FsNodeMemoryPoolFree_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 35, 1, 2, 1, 8),
    _FsNodeMemoryPoolFree_Type()
)
fsNodeMemoryPoolFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsNodeMemoryPoolFree.setStatus("current")
_FsNodeMemoryPoolWarning_Type = Percent
_FsNodeMemoryPoolWarning_Object = MibTableColumn
fsNodeMemoryPoolWarning = _FsNodeMemoryPoolWarning_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 35, 1, 2, 1, 9),
    _FsNodeMemoryPoolWarning_Type()
)
fsNodeMemoryPoolWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNodeMemoryPoolWarning.setStatus("current")
_FsNodeMemoryPoolCritical_Type = Percent
_FsNodeMemoryPoolCritical_Object = MibTableColumn
fsNodeMemoryPoolCritical = _FsNodeMemoryPoolCritical_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 35, 1, 2, 1, 10),
    _FsNodeMemoryPoolCritical_Type()
)
fsNodeMemoryPoolCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNodeMemoryPoolCritical.setStatus("current")
_FsNodeMemoryPoolTotalSize_Type = Gauge32
_FsNodeMemoryPoolTotalSize_Object = MibTableColumn
fsNodeMemoryPoolTotalSize = _FsNodeMemoryPoolTotalSize_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 35, 1, 2, 1, 11),
    _FsNodeMemoryPoolTotalSize_Type()
)
fsNodeMemoryPoolTotalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsNodeMemoryPoolTotalSize.setStatus("current")
_FsNodeMemoryPoolUsedSize_Type = Gauge32
_FsNodeMemoryPoolUsedSize_Object = MibTableColumn
fsNodeMemoryPoolUsedSize = _FsNodeMemoryPoolUsedSize_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 35, 1, 2, 1, 12),
    _FsNodeMemoryPoolUsedSize_Type()
)
fsNodeMemoryPoolUsedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsNodeMemoryPoolUsedSize.setStatus("current")
_FsNodeMemoryPoolFreeSize_Type = Gauge32
_FsNodeMemoryPoolFreeSize_Object = MibTableColumn
fsNodeMemoryPoolFreeSize = _FsNodeMemoryPoolFreeSize_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 35, 1, 2, 1, 13),
    _FsNodeMemoryPoolFreeSize_Type()
)
fsNodeMemoryPoolFreeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsNodeMemoryPoolFreeSize.setStatus("current")
_FsLankApMemoryPoolTable_Object = MibTable
fsLankApMemoryPoolTable = _FsLankApMemoryPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 35, 1, 3)
)
if mibBuilder.loadTexts:
    fsLankApMemoryPoolTable.setStatus("current")
_FsLankApMemoryPoolEntry_Object = MibTableRow
fsLankApMemoryPoolEntry = _FsLankApMemoryPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 35, 1, 3, 1)
)
fsLankApMemoryPoolEntry.setIndexNames(
    (0, "FS-MEMORY-MIB", "fsLankApMemoryPoolMacAddr"),
)
if mibBuilder.loadTexts:
    fsLankApMemoryPoolEntry.setStatus("current")
_FsLankApMemoryPoolMacAddr_Type = MacAddress
_FsLankApMemoryPoolMacAddr_Object = MibTableColumn
fsLankApMemoryPoolMacAddr = _FsLankApMemoryPoolMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 35, 1, 3, 1, 1),
    _FsLankApMemoryPoolMacAddr_Type()
)
fsLankApMemoryPoolMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLankApMemoryPoolMacAddr.setStatus("current")
_FsLankApMemoryPoolWarning_Type = Percent
_FsLankApMemoryPoolWarning_Object = MibTableColumn
fsLankApMemoryPoolWarning = _FsLankApMemoryPoolWarning_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 35, 1, 3, 1, 2),
    _FsLankApMemoryPoolWarning_Type()
)
fsLankApMemoryPoolWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLankApMemoryPoolWarning.setStatus("current")
_FsLankApMemoryPoolCritical_Type = Percent
_FsLankApMemoryPoolCritical_Object = MibTableColumn
fsLankApMemoryPoolCritical = _FsLankApMemoryPoolCritical_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 35, 1, 3, 1, 3),
    _FsLankApMemoryPoolCritical_Type()
)
fsLankApMemoryPoolCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLankApMemoryPoolCritical.setStatus("current")
_FsLankApMemoryPoolCurrentUtilization_Type = Percent
_FsLankApMemoryPoolCurrentUtilization_Object = MibTableColumn
fsLankApMemoryPoolCurrentUtilization = _FsLankApMemoryPoolCurrentUtilization_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 35, 1, 3, 1, 4),
    _FsLankApMemoryPoolCurrentUtilization_Type()
)
fsLankApMemoryPoolCurrentUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLankApMemoryPoolCurrentUtilization.setStatus("current")
_FsLankApMemoryPoolAverageUtilization_Type = Percent
_FsLankApMemoryPoolAverageUtilization_Object = MibTableColumn
fsLankApMemoryPoolAverageUtilization = _FsLankApMemoryPoolAverageUtilization_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 35, 1, 3, 1, 5),
    _FsLankApMemoryPoolAverageUtilization_Type()
)
fsLankApMemoryPoolAverageUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLankApMemoryPoolAverageUtilization.setStatus("current")
_FsMemoryMIBConformance_ObjectIdentity = ObjectIdentity
fsMemoryMIBConformance = _FsMemoryMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 35, 2)
)
_FsMemoryMIBCompliances_ObjectIdentity = ObjectIdentity
fsMemoryMIBCompliances = _FsMemoryMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 35, 2, 1)
)
_FsMemoryMIBGroups_ObjectIdentity = ObjectIdentity
fsMemoryMIBGroups = _FsMemoryMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 35, 2, 2)
)

# Managed Objects groups

fsMemoryPoolUtilizationMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 35, 2, 2, 1)
)
fsMemoryPoolUtilizationMIBGroup.setObjects(
      *(("FS-MEMORY-MIB", "fsMemoryPoolIndex"),
        ("FS-MEMORY-MIB", "fsMemoryPoolName"),
        ("FS-MEMORY-MIB", "fsMemoryPoolCurrentUtilization"),
        ("FS-MEMORY-MIB", "fsMemoryPoolLowestUtilization"),
        ("FS-MEMORY-MIB", "fsMemoryPoolLargestUtilization"),
        ("FS-MEMORY-MIB", "fsMemoryPoolSize"),
        ("FS-MEMORY-MIB", "fsMemoryPoolUsed"),
        ("FS-MEMORY-MIB", "fsMemoryPoolFree"),
        ("FS-MEMORY-MIB", "fsMemoryPoolWarning"),
        ("FS-MEMORY-MIB", "fsMemoryPoolCritical"),
        ("FS-MEMORY-MIB", "fsMemoryPoolAverageUtilization"),
        ("FS-MEMORY-MIB", "fsMemoryPoolTotalSize"),
        ("FS-MEMORY-MIB", "fsMemoryPoolUsedSize"),
        ("FS-MEMORY-MIB", "fsMemoryPoolFreeSize"))
)
if mibBuilder.loadTexts:
    fsMemoryPoolUtilizationMIBGroup.setStatus("current")

fsNodeMemoryPoolMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 35, 2, 2, 2)
)
fsNodeMemoryPoolMIBGroup.setObjects(
      *(("FS-MEMORY-MIB", "fsNodeMemoryPoolIndex"),
        ("FS-MEMORY-MIB", "fsNodeMemoryPoolName"),
        ("FS-MEMORY-MIB", "fsNodeMemoryPoolCurrentUtilization"),
        ("FS-MEMORY-MIB", "fsNodeMemoryPoolLowestUtilization"),
        ("FS-MEMORY-MIB", "fsNodeMemoryPoolLargestUtilization"),
        ("FS-MEMORY-MIB", "fsNodeMemoryPoolSize"),
        ("FS-MEMORY-MIB", "fsNodeMemoryPoolUsed"),
        ("FS-MEMORY-MIB", "fsNodeMemoryPoolFree"),
        ("FS-MEMORY-MIB", "fsNodeMemoryPoolWarning"),
        ("FS-MEMORY-MIB", "fsNodeMemoryPoolCritical"),
        ("FS-MEMORY-MIB", "fsNodeMemoryPoolTotalSize"),
        ("FS-MEMORY-MIB", "fsNodeMemoryPoolUsedSize"),
        ("FS-MEMORY-MIB", "fsNodeMemoryPoolFreeSize"))
)
if mibBuilder.loadTexts:
    fsNodeMemoryPoolMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fsMemoryMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 35, 2, 1, 1)
)
fsMemoryMIBCompliance.setObjects(
    ("FS-MEMORY-MIB", "fsMemoryPoolUtilizationMIBGroup")
)
if mibBuilder.loadTexts:
    fsMemoryMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-MEMORY-MIB",
    **{"Percent": Percent,
       "fsMemoryMIB": fsMemoryMIB,
       "fsMemoryPoolMIBObjects": fsMemoryPoolMIBObjects,
       "fsMemoryPoolUtilizationTable": fsMemoryPoolUtilizationTable,
       "fsMemoryPoolUtilizationEntry": fsMemoryPoolUtilizationEntry,
       "fsMemoryPoolIndex": fsMemoryPoolIndex,
       "fsMemoryPoolName": fsMemoryPoolName,
       "fsMemoryPoolCurrentUtilization": fsMemoryPoolCurrentUtilization,
       "fsMemoryPoolLowestUtilization": fsMemoryPoolLowestUtilization,
       "fsMemoryPoolLargestUtilization": fsMemoryPoolLargestUtilization,
       "fsMemoryPoolSize": fsMemoryPoolSize,
       "fsMemoryPoolUsed": fsMemoryPoolUsed,
       "fsMemoryPoolFree": fsMemoryPoolFree,
       "fsMemoryPoolWarning": fsMemoryPoolWarning,
       "fsMemoryPoolCritical": fsMemoryPoolCritical,
       "fsMemoryPoolAverageUtilization": fsMemoryPoolAverageUtilization,
       "fsMemoryPoolTotalSize": fsMemoryPoolTotalSize,
       "fsMemoryPoolUsedSize": fsMemoryPoolUsedSize,
       "fsMemoryPoolFreeSize": fsMemoryPoolFreeSize,
       "fsNodeMemoryPoolTable": fsNodeMemoryPoolTable,
       "fsNodeMemoryPoolEntry": fsNodeMemoryPoolEntry,
       "fsNodeMemoryPoolIndex": fsNodeMemoryPoolIndex,
       "fsNodeMemoryPoolName": fsNodeMemoryPoolName,
       "fsNodeMemoryPoolCurrentUtilization": fsNodeMemoryPoolCurrentUtilization,
       "fsNodeMemoryPoolLowestUtilization": fsNodeMemoryPoolLowestUtilization,
       "fsNodeMemoryPoolLargestUtilization": fsNodeMemoryPoolLargestUtilization,
       "fsNodeMemoryPoolSize": fsNodeMemoryPoolSize,
       "fsNodeMemoryPoolUsed": fsNodeMemoryPoolUsed,
       "fsNodeMemoryPoolFree": fsNodeMemoryPoolFree,
       "fsNodeMemoryPoolWarning": fsNodeMemoryPoolWarning,
       "fsNodeMemoryPoolCritical": fsNodeMemoryPoolCritical,
       "fsNodeMemoryPoolTotalSize": fsNodeMemoryPoolTotalSize,
       "fsNodeMemoryPoolUsedSize": fsNodeMemoryPoolUsedSize,
       "fsNodeMemoryPoolFreeSize": fsNodeMemoryPoolFreeSize,
       "fsLankApMemoryPoolTable": fsLankApMemoryPoolTable,
       "fsLankApMemoryPoolEntry": fsLankApMemoryPoolEntry,
       "fsLankApMemoryPoolMacAddr": fsLankApMemoryPoolMacAddr,
       "fsLankApMemoryPoolWarning": fsLankApMemoryPoolWarning,
       "fsLankApMemoryPoolCritical": fsLankApMemoryPoolCritical,
       "fsLankApMemoryPoolCurrentUtilization": fsLankApMemoryPoolCurrentUtilization,
       "fsLankApMemoryPoolAverageUtilization": fsLankApMemoryPoolAverageUtilization,
       "fsMemoryMIBConformance": fsMemoryMIBConformance,
       "fsMemoryMIBCompliances": fsMemoryMIBCompliances,
       "fsMemoryMIBCompliance": fsMemoryMIBCompliance,
       "fsMemoryMIBGroups": fsMemoryMIBGroups,
       "fsMemoryPoolUtilizationMIBGroup": fsMemoryPoolUtilizationMIBGroup,
       "fsNodeMemoryPoolMIBGroup": fsNodeMemoryPoolMIBGroup}
)
