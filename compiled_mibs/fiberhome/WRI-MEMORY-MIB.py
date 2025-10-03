# SNMP MIB module (WRI-MEMORY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fiberhome\WRI-MEMORY-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:44:13 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(wri,
 wriProducts) = mibBuilder.importSymbols(
    "WRI-SMI",
    "wri",
    "wriProducts")


# MODULE-IDENTITY

msppMemory = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 5)
)
if mibBuilder.loadTexts:
    msppMemory.setRevisions(
        ("2010-01-11 00:00",
         "2009-01-11 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Mspp_ObjectIdentity = ObjectIdentity
mspp = _Mspp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012)
)
_MsppChassis_ObjectIdentity = ObjectIdentity
msppChassis = _MsppChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1)
)
_MemoryTable_Object = MibTable
memoryTable = _MemoryTable_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 5, 1)
)
if mibBuilder.loadTexts:
    memoryTable.setStatus("current")
_MemoryEntry_Object = MibTableRow
memoryEntry = _MemoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 5, 1, 1)
)
memoryEntry.setIndexNames(
    (0, "WRI-MEMORY-MIB", "memoryIndex"),
)
if mibBuilder.loadTexts:
    memoryEntry.setStatus("current")
_MemoryIndex_Type = Integer32
_MemoryIndex_Object = MibTableColumn
memoryIndex = _MemoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 5, 1, 1, 1),
    _MemoryIndex_Type()
)
memoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryIndex.setStatus("current")
_MemorySdramSize_Type = Counter32
_MemorySdramSize_Object = MibTableColumn
memorySdramSize = _MemorySdramSize_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 5, 1, 1, 2),
    _MemorySdramSize_Type()
)
memorySdramSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memorySdramSize.setStatus("current")
_MemorySdramUsed_Type = Counter32
_MemorySdramUsed_Object = MibTableColumn
memorySdramUsed = _MemorySdramUsed_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 5, 1, 1, 3),
    _MemorySdramUsed_Type()
)
memorySdramUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memorySdramUsed.setStatus("current")
_MemoryFlashSize_Type = Counter32
_MemoryFlashSize_Object = MibTableColumn
memoryFlashSize = _MemoryFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 5, 1, 1, 4),
    _MemoryFlashSize_Type()
)
memoryFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryFlashSize.setStatus("current")
_MemoryFlashUsed_Type = Counter32
_MemoryFlashUsed_Object = MibTableColumn
memoryFlashUsed = _MemoryFlashUsed_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 5, 1, 1, 5),
    _MemoryFlashUsed_Type()
)
memoryFlashUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryFlashUsed.setStatus("current")
_MemorySdramHThreshold_Type = Counter32
_MemorySdramHThreshold_Object = MibTableColumn
memorySdramHThreshold = _MemorySdramHThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 5, 1, 1, 6),
    _MemorySdramHThreshold_Type()
)
memorySdramHThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    memorySdramHThreshold.setStatus("current")
_MemoryGeneral_ObjectIdentity = ObjectIdentity
memoryGeneral = _MemoryGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 5, 2)
)
_MemoryTrapEnable_Type = Integer32
_MemoryTrapEnable_Object = MibScalar
memoryTrapEnable = _MemoryTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 5, 2, 1),
    _MemoryTrapEnable_Type()
)
memoryTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    memoryTrapEnable.setStatus("current")
_MemoryMonitorEnable_Type = Integer32
_MemoryMonitorEnable_Object = MibScalar
memoryMonitorEnable = _MemoryMonitorEnable_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 5, 2, 2),
    _MemoryMonitorEnable_Type()
)
memoryMonitorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    memoryMonitorEnable.setStatus("current")
_MemoryTrap_ObjectIdentity = ObjectIdentity
memoryTrap = _MemoryTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 5, 3)
)
_MemoryPoolTable_Object = MibTable
memoryPoolTable = _MemoryPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 5, 4)
)
if mibBuilder.loadTexts:
    memoryPoolTable.setStatus("current")
_MemoryPoolEntry_Object = MibTableRow
memoryPoolEntry = _MemoryPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 5, 4, 1)
)
memoryPoolEntry.setIndexNames(
    (0, "WRI-MEMORY-MIB", "memoryPoolIndex"),
)
if mibBuilder.loadTexts:
    memoryPoolEntry.setStatus("current")
_MemoryPoolIndex_Type = Unsigned32
_MemoryPoolIndex_Object = MibTableColumn
memoryPoolIndex = _MemoryPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 5, 4, 1, 1),
    _MemoryPoolIndex_Type()
)
memoryPoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryPoolIndex.setStatus("current")
_MemoryPoolDescr_Type = OctetString
_MemoryPoolDescr_Object = MibTableColumn
memoryPoolDescr = _MemoryPoolDescr_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 5, 4, 1, 2),
    _MemoryPoolDescr_Type()
)
memoryPoolDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryPoolDescr.setStatus("current")
_MemoryPoolFreeBytesNum_Type = Counter32
_MemoryPoolFreeBytesNum_Object = MibTableColumn
memoryPoolFreeBytesNum = _MemoryPoolFreeBytesNum_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 5, 4, 1, 3),
    _MemoryPoolFreeBytesNum_Type()
)
memoryPoolFreeBytesNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryPoolFreeBytesNum.setStatus("current")
_MemoryPoolFreeBlocksNum_Type = Counter32
_MemoryPoolFreeBlocksNum_Object = MibTableColumn
memoryPoolFreeBlocksNum = _MemoryPoolFreeBlocksNum_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 5, 4, 1, 4),
    _MemoryPoolFreeBlocksNum_Type()
)
memoryPoolFreeBlocksNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryPoolFreeBlocksNum.setStatus("current")
_MemoryPoolFreeMaxBlockSize_Type = Counter32
_MemoryPoolFreeMaxBlockSize_Object = MibTableColumn
memoryPoolFreeMaxBlockSize = _MemoryPoolFreeMaxBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 5, 4, 1, 5),
    _MemoryPoolFreeMaxBlockSize_Type()
)
memoryPoolFreeMaxBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryPoolFreeMaxBlockSize.setStatus("current")
_MemoryPoolMinBlockWords_Type = Counter32
_MemoryPoolMinBlockWords_Object = MibTableColumn
memoryPoolMinBlockWords = _MemoryPoolMinBlockWords_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 5, 4, 1, 6),
    _MemoryPoolMinBlockWords_Type()
)
memoryPoolMinBlockWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryPoolMinBlockWords.setStatus("current")
_MemoryPoolAllocBytesNum_Type = Counter32
_MemoryPoolAllocBytesNum_Object = MibTableColumn
memoryPoolAllocBytesNum = _MemoryPoolAllocBytesNum_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 5, 4, 1, 7),
    _MemoryPoolAllocBytesNum_Type()
)
memoryPoolAllocBytesNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryPoolAllocBytesNum.setStatus("current")
_MemoryPoolAllocBlocksNum_Type = Counter32
_MemoryPoolAllocBlocksNum_Object = MibTableColumn
memoryPoolAllocBlocksNum = _MemoryPoolAllocBlocksNum_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 5, 4, 1, 8),
    _MemoryPoolAllocBlocksNum_Type()
)
memoryPoolAllocBlocksNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryPoolAllocBlocksNum.setStatus("current")
_MemoryPoolAllocBytesCumulate_Type = Counter32
_MemoryPoolAllocBytesCumulate_Object = MibTableColumn
memoryPoolAllocBytesCumulate = _MemoryPoolAllocBytesCumulate_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 5, 4, 1, 9),
    _MemoryPoolAllocBytesCumulate_Type()
)
memoryPoolAllocBytesCumulate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryPoolAllocBytesCumulate.setStatus("current")
_MemoryPoolAllocBlocksCumulate_Type = Counter32
_MemoryPoolAllocBlocksCumulate_Object = MibTableColumn
memoryPoolAllocBlocksCumulate = _MemoryPoolAllocBlocksCumulate_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 5, 4, 1, 10),
    _MemoryPoolAllocBlocksCumulate_Type()
)
memoryPoolAllocBlocksCumulate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryPoolAllocBlocksCumulate.setStatus("current")
_MemoryPoolTotalBytes_Type = Counter32
_MemoryPoolTotalBytes_Object = MibTableColumn
memoryPoolTotalBytes = _MemoryPoolTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 5, 4, 1, 11),
    _MemoryPoolTotalBytes_Type()
)
memoryPoolTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryPoolTotalBytes.setStatus("current")
_MemoryPoolHighThreshold_Type = Integer32
_MemoryPoolHighThreshold_Object = MibTableColumn
memoryPoolHighThreshold = _MemoryPoolHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 5, 4, 1, 12),
    _MemoryPoolHighThreshold_Type()
)
memoryPoolHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    memoryPoolHighThreshold.setStatus("current")


class _MemoryPoolTrapEnable_Type(Integer32):
    """Custom type memoryPoolTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_MemoryPoolTrapEnable_Type.__name__ = "Integer32"
_MemoryPoolTrapEnable_Object = MibTableColumn
memoryPoolTrapEnable = _MemoryPoolTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 5, 4, 1, 13),
    _MemoryPoolTrapEnable_Type()
)
memoryPoolTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    memoryPoolTrapEnable.setStatus("current")


class _MemoryPoolStatus_Type(Integer32):
    """Custom type memoryPoolStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("highoverflow", 1))
    )


_MemoryPoolStatus_Type.__name__ = "Integer32"
_MemoryPoolStatus_Object = MibTableColumn
memoryPoolStatus = _MemoryPoolStatus_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 5, 4, 1, 14),
    _MemoryPoolStatus_Type()
)
memoryPoolStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryPoolStatus.setStatus("current")
_MemoryPoolAllSetting_Type = OctetString
_MemoryPoolAllSetting_Object = MibTableColumn
memoryPoolAllSetting = _MemoryPoolAllSetting_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 5, 4, 1, 15),
    _MemoryPoolAllSetting_Type()
)
memoryPoolAllSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    memoryPoolAllSetting.setStatus("current")
_MemoryPoolAllocMaxBytesNum_Type = Integer32
_MemoryPoolAllocMaxBytesNum_Object = MibTableColumn
memoryPoolAllocMaxBytesNum = _MemoryPoolAllocMaxBytesNum_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 5, 4, 1, 16),
    _MemoryPoolAllocMaxBytesNum_Type()
)
memoryPoolAllocMaxBytesNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryPoolAllocMaxBytesNum.setStatus("current")
_MemoryPoolLowThreshold_Type = Integer32
_MemoryPoolLowThreshold_Object = MibTableColumn
memoryPoolLowThreshold = _MemoryPoolLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 5, 4, 1, 17),
    _MemoryPoolLowThreshold_Type()
)
memoryPoolLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    memoryPoolLowThreshold.setStatus("current")
_MemoryPoolCurrUsage_Type = Counter32
_MemoryPoolCurrUsage_Object = MibTableColumn
memoryPoolCurrUsage = _MemoryPoolCurrUsage_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 5, 4, 1, 18),
    _MemoryPoolCurrUsage_Type()
)
memoryPoolCurrUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryPoolCurrUsage.setStatus("current")
_MemoryPoolIndexDescr_Type = OctetString
_MemoryPoolIndexDescr_Object = MibTableColumn
memoryPoolIndexDescr = _MemoryPoolIndexDescr_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 5, 4, 1, 19),
    _MemoryPoolIndexDescr_Type()
)
memoryPoolIndexDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryPoolIndexDescr.setStatus("current")

# Managed Objects groups


# Notification objects

memoryOverThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 5, 3, 1)
)
memoryOverThreshold.setObjects(
      *(("WRI-MEMORY-MIB", "memoryPoolCurrUsage"),
        ("WRI-MEMORY-MIB", "memoryPoolHighThreshold"),
        ("WRI-MEMORY-MIB", "memoryPoolLowThreshold"))
)
if mibBuilder.loadTexts:
    memoryOverThreshold.setStatus(
        "current"
    )

memoryUnderThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 5, 3, 2)
)
memoryUnderThreshold.setObjects(
      *(("WRI-MEMORY-MIB", "memoryPoolCurrUsage"),
        ("WRI-MEMORY-MIB", "memoryPoolHighThreshold"),
        ("WRI-MEMORY-MIB", "memoryPoolLowThreshold"))
)
if mibBuilder.loadTexts:
    memoryUnderThreshold.setStatus(
        "current"
    )

memoryRecoverThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 5, 3, 3)
)
memoryRecoverThreshold.setObjects(
      *(("WRI-MEMORY-MIB", "memoryPoolCurrUsage"),
        ("WRI-MEMORY-MIB", "memoryPoolHighThreshold"),
        ("WRI-MEMORY-MIB", "memoryPoolLowThreshold"))
)
if mibBuilder.loadTexts:
    memoryRecoverThreshold.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WRI-MEMORY-MIB",
    **{"mspp": mspp,
       "msppChassis": msppChassis,
       "msppMemory": msppMemory,
       "memoryTable": memoryTable,
       "memoryEntry": memoryEntry,
       "memoryIndex": memoryIndex,
       "memorySdramSize": memorySdramSize,
       "memorySdramUsed": memorySdramUsed,
       "memoryFlashSize": memoryFlashSize,
       "memoryFlashUsed": memoryFlashUsed,
       "memorySdramHThreshold": memorySdramHThreshold,
       "memoryGeneral": memoryGeneral,
       "memoryTrapEnable": memoryTrapEnable,
       "memoryMonitorEnable": memoryMonitorEnable,
       "memoryTrap": memoryTrap,
       "memoryOverThreshold": memoryOverThreshold,
       "memoryUnderThreshold": memoryUnderThreshold,
       "memoryRecoverThreshold": memoryRecoverThreshold,
       "memoryPoolTable": memoryPoolTable,
       "memoryPoolEntry": memoryPoolEntry,
       "memoryPoolIndex": memoryPoolIndex,
       "memoryPoolDescr": memoryPoolDescr,
       "memoryPoolFreeBytesNum": memoryPoolFreeBytesNum,
       "memoryPoolFreeBlocksNum": memoryPoolFreeBlocksNum,
       "memoryPoolFreeMaxBlockSize": memoryPoolFreeMaxBlockSize,
       "memoryPoolMinBlockWords": memoryPoolMinBlockWords,
       "memoryPoolAllocBytesNum": memoryPoolAllocBytesNum,
       "memoryPoolAllocBlocksNum": memoryPoolAllocBlocksNum,
       "memoryPoolAllocBytesCumulate": memoryPoolAllocBytesCumulate,
       "memoryPoolAllocBlocksCumulate": memoryPoolAllocBlocksCumulate,
       "memoryPoolTotalBytes": memoryPoolTotalBytes,
       "memoryPoolHighThreshold": memoryPoolHighThreshold,
       "memoryPoolTrapEnable": memoryPoolTrapEnable,
       "memoryPoolStatus": memoryPoolStatus,
       "memoryPoolAllSetting": memoryPoolAllSetting,
       "memoryPoolAllocMaxBytesNum": memoryPoolAllocMaxBytesNum,
       "memoryPoolLowThreshold": memoryPoolLowThreshold,
       "memoryPoolCurrUsage": memoryPoolCurrUsage,
       "memoryPoolIndexDescr": memoryPoolIndexDescr}
)
