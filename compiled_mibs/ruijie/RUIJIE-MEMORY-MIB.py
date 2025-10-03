# SNMP MIB module (RUIJIE-MEMORY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ruijie\RUIJIE-MEMORY-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:24:26 2025
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

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

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

ruijieMemoryMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 35)
)
if mibBuilder.loadTexts:
    ruijieMemoryMIB.setRevisions(
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

_RuijieMemoryPoolMIBObjects_ObjectIdentity = ObjectIdentity
ruijieMemoryPoolMIBObjects = _RuijieMemoryPoolMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 35, 1)
)
_RuijieMemoryPoolUtilizationTable_Object = MibTable
ruijieMemoryPoolUtilizationTable = _RuijieMemoryPoolUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 35, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieMemoryPoolUtilizationTable.setStatus("current")
_RuijieMemoryPoolUtilizationEntry_Object = MibTableRow
ruijieMemoryPoolUtilizationEntry = _RuijieMemoryPoolUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 35, 1, 1, 1)
)
ruijieMemoryPoolUtilizationEntry.setIndexNames(
    (0, "RUIJIE-MEMORY-MIB", "ruijieMemoryPoolIndex"),
)
if mibBuilder.loadTexts:
    ruijieMemoryPoolUtilizationEntry.setStatus("current")


class _RuijieMemoryPoolIndex_Type(Integer32):
    """Custom type ruijieMemoryPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RuijieMemoryPoolIndex_Type.__name__ = "Integer32"
_RuijieMemoryPoolIndex_Object = MibTableColumn
ruijieMemoryPoolIndex = _RuijieMemoryPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 35, 1, 1, 1, 1),
    _RuijieMemoryPoolIndex_Type()
)
ruijieMemoryPoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMemoryPoolIndex.setStatus("current")
_RuijieMemoryPoolName_Type = DisplayString
_RuijieMemoryPoolName_Object = MibTableColumn
ruijieMemoryPoolName = _RuijieMemoryPoolName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 35, 1, 1, 1, 2),
    _RuijieMemoryPoolName_Type()
)
ruijieMemoryPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMemoryPoolName.setStatus("current")
_RuijieMemoryPoolCurrentUtilization_Type = Percent
_RuijieMemoryPoolCurrentUtilization_Object = MibTableColumn
ruijieMemoryPoolCurrentUtilization = _RuijieMemoryPoolCurrentUtilization_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 35, 1, 1, 1, 3),
    _RuijieMemoryPoolCurrentUtilization_Type()
)
ruijieMemoryPoolCurrentUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMemoryPoolCurrentUtilization.setStatus("current")
_RuijieMemoryPoolLowestUtilization_Type = Percent
_RuijieMemoryPoolLowestUtilization_Object = MibTableColumn
ruijieMemoryPoolLowestUtilization = _RuijieMemoryPoolLowestUtilization_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 35, 1, 1, 1, 4),
    _RuijieMemoryPoolLowestUtilization_Type()
)
ruijieMemoryPoolLowestUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMemoryPoolLowestUtilization.setStatus("current")
_RuijieMemoryPoolLargestUtilization_Type = Percent
_RuijieMemoryPoolLargestUtilization_Object = MibTableColumn
ruijieMemoryPoolLargestUtilization = _RuijieMemoryPoolLargestUtilization_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 35, 1, 1, 1, 5),
    _RuijieMemoryPoolLargestUtilization_Type()
)
ruijieMemoryPoolLargestUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMemoryPoolLargestUtilization.setStatus("current")
_RuijieMemoryPoolSize_Type = Integer32
_RuijieMemoryPoolSize_Object = MibTableColumn
ruijieMemoryPoolSize = _RuijieMemoryPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 35, 1, 1, 1, 6),
    _RuijieMemoryPoolSize_Type()
)
ruijieMemoryPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMemoryPoolSize.setStatus("current")
_RuijieMemoryPoolUsed_Type = Integer32
_RuijieMemoryPoolUsed_Object = MibTableColumn
ruijieMemoryPoolUsed = _RuijieMemoryPoolUsed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 35, 1, 1, 1, 7),
    _RuijieMemoryPoolUsed_Type()
)
ruijieMemoryPoolUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMemoryPoolUsed.setStatus("current")
_RuijieMemoryPoolFree_Type = Integer32
_RuijieMemoryPoolFree_Object = MibTableColumn
ruijieMemoryPoolFree = _RuijieMemoryPoolFree_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 35, 1, 1, 1, 8),
    _RuijieMemoryPoolFree_Type()
)
ruijieMemoryPoolFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMemoryPoolFree.setStatus("current")
_RuijieMemoryPoolWarning_Type = Percent
_RuijieMemoryPoolWarning_Object = MibTableColumn
ruijieMemoryPoolWarning = _RuijieMemoryPoolWarning_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 35, 1, 1, 1, 9),
    _RuijieMemoryPoolWarning_Type()
)
ruijieMemoryPoolWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieMemoryPoolWarning.setStatus("current")
_RuijieMemoryPoolCritical_Type = Percent
_RuijieMemoryPoolCritical_Object = MibTableColumn
ruijieMemoryPoolCritical = _RuijieMemoryPoolCritical_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 35, 1, 1, 1, 10),
    _RuijieMemoryPoolCritical_Type()
)
ruijieMemoryPoolCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieMemoryPoolCritical.setStatus("current")
_RuijieMemoryPoolAverageUtilization_Type = Percent
_RuijieMemoryPoolAverageUtilization_Object = MibTableColumn
ruijieMemoryPoolAverageUtilization = _RuijieMemoryPoolAverageUtilization_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 35, 1, 1, 1, 11),
    _RuijieMemoryPoolAverageUtilization_Type()
)
ruijieMemoryPoolAverageUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMemoryPoolAverageUtilization.setStatus("current")
_RuijieMemoryPoolTotalSize_Type = Gauge32
_RuijieMemoryPoolTotalSize_Object = MibTableColumn
ruijieMemoryPoolTotalSize = _RuijieMemoryPoolTotalSize_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 35, 1, 1, 1, 12),
    _RuijieMemoryPoolTotalSize_Type()
)
ruijieMemoryPoolTotalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMemoryPoolTotalSize.setStatus("current")
_RuijieMemoryPoolUsedSize_Type = Gauge32
_RuijieMemoryPoolUsedSize_Object = MibTableColumn
ruijieMemoryPoolUsedSize = _RuijieMemoryPoolUsedSize_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 35, 1, 1, 1, 13),
    _RuijieMemoryPoolUsedSize_Type()
)
ruijieMemoryPoolUsedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMemoryPoolUsedSize.setStatus("current")
_RuijieMemoryPoolFreeSize_Type = Gauge32
_RuijieMemoryPoolFreeSize_Object = MibTableColumn
ruijieMemoryPoolFreeSize = _RuijieMemoryPoolFreeSize_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 35, 1, 1, 1, 14),
    _RuijieMemoryPoolFreeSize_Type()
)
ruijieMemoryPoolFreeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMemoryPoolFreeSize.setStatus("current")
_RuijieNodeMemoryPoolTable_Object = MibTable
ruijieNodeMemoryPoolTable = _RuijieNodeMemoryPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 35, 1, 2)
)
if mibBuilder.loadTexts:
    ruijieNodeMemoryPoolTable.setStatus("current")
_RuijieNodeMemoryPoolEntry_Object = MibTableRow
ruijieNodeMemoryPoolEntry = _RuijieNodeMemoryPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 35, 1, 2, 1)
)
ruijieNodeMemoryPoolEntry.setIndexNames(
    (0, "RUIJIE-MEMORY-MIB", "ruijieNodeMemoryPoolIndex"),
)
if mibBuilder.loadTexts:
    ruijieNodeMemoryPoolEntry.setStatus("current")


class _RuijieNodeMemoryPoolIndex_Type(Integer32):
    """Custom type ruijieNodeMemoryPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RuijieNodeMemoryPoolIndex_Type.__name__ = "Integer32"
_RuijieNodeMemoryPoolIndex_Object = MibTableColumn
ruijieNodeMemoryPoolIndex = _RuijieNodeMemoryPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 35, 1, 2, 1, 1),
    _RuijieNodeMemoryPoolIndex_Type()
)
ruijieNodeMemoryPoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieNodeMemoryPoolIndex.setStatus("current")
_RuijieNodeMemoryPoolName_Type = DisplayString
_RuijieNodeMemoryPoolName_Object = MibTableColumn
ruijieNodeMemoryPoolName = _RuijieNodeMemoryPoolName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 35, 1, 2, 1, 2),
    _RuijieNodeMemoryPoolName_Type()
)
ruijieNodeMemoryPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieNodeMemoryPoolName.setStatus("current")
_RuijieNodeMemoryPoolCurrentUtilization_Type = Percent
_RuijieNodeMemoryPoolCurrentUtilization_Object = MibTableColumn
ruijieNodeMemoryPoolCurrentUtilization = _RuijieNodeMemoryPoolCurrentUtilization_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 35, 1, 2, 1, 3),
    _RuijieNodeMemoryPoolCurrentUtilization_Type()
)
ruijieNodeMemoryPoolCurrentUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieNodeMemoryPoolCurrentUtilization.setStatus("current")
_RuijieNodeMemoryPoolLowestUtilization_Type = Percent
_RuijieNodeMemoryPoolLowestUtilization_Object = MibTableColumn
ruijieNodeMemoryPoolLowestUtilization = _RuijieNodeMemoryPoolLowestUtilization_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 35, 1, 2, 1, 4),
    _RuijieNodeMemoryPoolLowestUtilization_Type()
)
ruijieNodeMemoryPoolLowestUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieNodeMemoryPoolLowestUtilization.setStatus("current")
_RuijieNodeMemoryPoolLargestUtilization_Type = Percent
_RuijieNodeMemoryPoolLargestUtilization_Object = MibTableColumn
ruijieNodeMemoryPoolLargestUtilization = _RuijieNodeMemoryPoolLargestUtilization_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 35, 1, 2, 1, 5),
    _RuijieNodeMemoryPoolLargestUtilization_Type()
)
ruijieNodeMemoryPoolLargestUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieNodeMemoryPoolLargestUtilization.setStatus("current")
_RuijieNodeMemoryPoolSize_Type = Integer32
_RuijieNodeMemoryPoolSize_Object = MibTableColumn
ruijieNodeMemoryPoolSize = _RuijieNodeMemoryPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 35, 1, 2, 1, 6),
    _RuijieNodeMemoryPoolSize_Type()
)
ruijieNodeMemoryPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieNodeMemoryPoolSize.setStatus("current")
_RuijieNodeMemoryPoolUsed_Type = Integer32
_RuijieNodeMemoryPoolUsed_Object = MibTableColumn
ruijieNodeMemoryPoolUsed = _RuijieNodeMemoryPoolUsed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 35, 1, 2, 1, 7),
    _RuijieNodeMemoryPoolUsed_Type()
)
ruijieNodeMemoryPoolUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieNodeMemoryPoolUsed.setStatus("current")
_RuijieNodeMemoryPoolFree_Type = Integer32
_RuijieNodeMemoryPoolFree_Object = MibTableColumn
ruijieNodeMemoryPoolFree = _RuijieNodeMemoryPoolFree_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 35, 1, 2, 1, 8),
    _RuijieNodeMemoryPoolFree_Type()
)
ruijieNodeMemoryPoolFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieNodeMemoryPoolFree.setStatus("current")
_RuijieNodeMemoryPoolWarning_Type = Percent
_RuijieNodeMemoryPoolWarning_Object = MibTableColumn
ruijieNodeMemoryPoolWarning = _RuijieNodeMemoryPoolWarning_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 35, 1, 2, 1, 9),
    _RuijieNodeMemoryPoolWarning_Type()
)
ruijieNodeMemoryPoolWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNodeMemoryPoolWarning.setStatus("current")
_RuijieNodeMemoryPoolCritical_Type = Percent
_RuijieNodeMemoryPoolCritical_Object = MibTableColumn
ruijieNodeMemoryPoolCritical = _RuijieNodeMemoryPoolCritical_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 35, 1, 2, 1, 10),
    _RuijieNodeMemoryPoolCritical_Type()
)
ruijieNodeMemoryPoolCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNodeMemoryPoolCritical.setStatus("current")
_RuijieNodeMemoryPoolTotalSize_Type = Gauge32
_RuijieNodeMemoryPoolTotalSize_Object = MibTableColumn
ruijieNodeMemoryPoolTotalSize = _RuijieNodeMemoryPoolTotalSize_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 35, 1, 2, 1, 11),
    _RuijieNodeMemoryPoolTotalSize_Type()
)
ruijieNodeMemoryPoolTotalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieNodeMemoryPoolTotalSize.setStatus("current")
_RuijieNodeMemoryPoolUsedSize_Type = Gauge32
_RuijieNodeMemoryPoolUsedSize_Object = MibTableColumn
ruijieNodeMemoryPoolUsedSize = _RuijieNodeMemoryPoolUsedSize_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 35, 1, 2, 1, 12),
    _RuijieNodeMemoryPoolUsedSize_Type()
)
ruijieNodeMemoryPoolUsedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieNodeMemoryPoolUsedSize.setStatus("current")
_RuijieNodeMemoryPoolFreeSize_Type = Gauge32
_RuijieNodeMemoryPoolFreeSize_Object = MibTableColumn
ruijieNodeMemoryPoolFreeSize = _RuijieNodeMemoryPoolFreeSize_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 35, 1, 2, 1, 13),
    _RuijieNodeMemoryPoolFreeSize_Type()
)
ruijieNodeMemoryPoolFreeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieNodeMemoryPoolFreeSize.setStatus("current")
_RuijieLankApMemoryPoolTable_Object = MibTable
ruijieLankApMemoryPoolTable = _RuijieLankApMemoryPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 35, 1, 3)
)
if mibBuilder.loadTexts:
    ruijieLankApMemoryPoolTable.setStatus("current")
_RuijieLankApMemoryPoolEntry_Object = MibTableRow
ruijieLankApMemoryPoolEntry = _RuijieLankApMemoryPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 35, 1, 3, 1)
)
ruijieLankApMemoryPoolEntry.setIndexNames(
    (0, "RUIJIE-MEMORY-MIB", "ruijieLankApMemoryPoolMacAddr"),
)
if mibBuilder.loadTexts:
    ruijieLankApMemoryPoolEntry.setStatus("current")
_RuijieLankApMemoryPoolMacAddr_Type = MacAddress
_RuijieLankApMemoryPoolMacAddr_Object = MibTableColumn
ruijieLankApMemoryPoolMacAddr = _RuijieLankApMemoryPoolMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 35, 1, 3, 1, 1),
    _RuijieLankApMemoryPoolMacAddr_Type()
)
ruijieLankApMemoryPoolMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieLankApMemoryPoolMacAddr.setStatus("current")
_RuijieLankApMemoryPoolWarning_Type = Percent
_RuijieLankApMemoryPoolWarning_Object = MibTableColumn
ruijieLankApMemoryPoolWarning = _RuijieLankApMemoryPoolWarning_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 35, 1, 3, 1, 2),
    _RuijieLankApMemoryPoolWarning_Type()
)
ruijieLankApMemoryPoolWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieLankApMemoryPoolWarning.setStatus("current")
_RuijieLankApMemoryPoolCritical_Type = Percent
_RuijieLankApMemoryPoolCritical_Object = MibTableColumn
ruijieLankApMemoryPoolCritical = _RuijieLankApMemoryPoolCritical_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 35, 1, 3, 1, 3),
    _RuijieLankApMemoryPoolCritical_Type()
)
ruijieLankApMemoryPoolCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieLankApMemoryPoolCritical.setStatus("current")
_RuijieLankApMemoryPoolCurrentUtilization_Type = Percent
_RuijieLankApMemoryPoolCurrentUtilization_Object = MibTableColumn
ruijieLankApMemoryPoolCurrentUtilization = _RuijieLankApMemoryPoolCurrentUtilization_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 35, 1, 3, 1, 4),
    _RuijieLankApMemoryPoolCurrentUtilization_Type()
)
ruijieLankApMemoryPoolCurrentUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieLankApMemoryPoolCurrentUtilization.setStatus("current")
_RuijieLankApMemoryPoolAverageUtilization_Type = Percent
_RuijieLankApMemoryPoolAverageUtilization_Object = MibTableColumn
ruijieLankApMemoryPoolAverageUtilization = _RuijieLankApMemoryPoolAverageUtilization_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 35, 1, 3, 1, 5),
    _RuijieLankApMemoryPoolAverageUtilization_Type()
)
ruijieLankApMemoryPoolAverageUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieLankApMemoryPoolAverageUtilization.setStatus("current")
_RuijieMemoryMIBConformance_ObjectIdentity = ObjectIdentity
ruijieMemoryMIBConformance = _RuijieMemoryMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 35, 2)
)
_RuijieMemoryMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieMemoryMIBCompliances = _RuijieMemoryMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 35, 2, 1)
)
_RuijieMemoryMIBGroups_ObjectIdentity = ObjectIdentity
ruijieMemoryMIBGroups = _RuijieMemoryMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 35, 2, 2)
)

# Managed Objects groups

ruijieMemoryPoolUtilizationMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 35, 2, 2, 1)
)
ruijieMemoryPoolUtilizationMIBGroup.setObjects(
      *(("RUIJIE-MEMORY-MIB", "ruijieMemoryPoolIndex"),
        ("RUIJIE-MEMORY-MIB", "ruijieMemoryPoolName"),
        ("RUIJIE-MEMORY-MIB", "ruijieMemoryPoolCurrentUtilization"),
        ("RUIJIE-MEMORY-MIB", "ruijieMemoryPoolLowestUtilization"),
        ("RUIJIE-MEMORY-MIB", "ruijieMemoryPoolLargestUtilization"),
        ("RUIJIE-MEMORY-MIB", "ruijieMemoryPoolSize"),
        ("RUIJIE-MEMORY-MIB", "ruijieMemoryPoolUsed"),
        ("RUIJIE-MEMORY-MIB", "ruijieMemoryPoolFree"),
        ("RUIJIE-MEMORY-MIB", "ruijieMemoryPoolWarning"),
        ("RUIJIE-MEMORY-MIB", "ruijieMemoryPoolCritical"),
        ("RUIJIE-MEMORY-MIB", "ruijieMemoryPoolAverageUtilization"),
        ("RUIJIE-MEMORY-MIB", "ruijieMemoryPoolTotalSize"),
        ("RUIJIE-MEMORY-MIB", "ruijieMemoryPoolUsedSize"),
        ("RUIJIE-MEMORY-MIB", "ruijieMemoryPoolFreeSize"))
)
if mibBuilder.loadTexts:
    ruijieMemoryPoolUtilizationMIBGroup.setStatus("current")

ruijieNodeMemoryPoolMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 35, 2, 2, 2)
)
ruijieNodeMemoryPoolMIBGroup.setObjects(
      *(("RUIJIE-MEMORY-MIB", "ruijieNodeMemoryPoolIndex"),
        ("RUIJIE-MEMORY-MIB", "ruijieNodeMemoryPoolName"),
        ("RUIJIE-MEMORY-MIB", "ruijieNodeMemoryPoolCurrentUtilization"),
        ("RUIJIE-MEMORY-MIB", "ruijieNodeMemoryPoolLowestUtilization"),
        ("RUIJIE-MEMORY-MIB", "ruijieNodeMemoryPoolLargestUtilization"),
        ("RUIJIE-MEMORY-MIB", "ruijieNodeMemoryPoolSize"),
        ("RUIJIE-MEMORY-MIB", "ruijieNodeMemoryPoolUsed"),
        ("RUIJIE-MEMORY-MIB", "ruijieNodeMemoryPoolFree"),
        ("RUIJIE-MEMORY-MIB", "ruijieNodeMemoryPoolWarning"),
        ("RUIJIE-MEMORY-MIB", "ruijieNodeMemoryPoolCritical"),
        ("RUIJIE-MEMORY-MIB", "ruijieNodeMemoryPoolTotalSize"),
        ("RUIJIE-MEMORY-MIB", "ruijieNodeMemoryPoolUsedSize"),
        ("RUIJIE-MEMORY-MIB", "ruijieNodeMemoryPoolFreeSize"))
)
if mibBuilder.loadTexts:
    ruijieNodeMemoryPoolMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ruijieMemoryMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 35, 2, 1, 1)
)
ruijieMemoryMIBCompliance.setObjects(
    ("RUIJIE-MEMORY-MIB", "ruijieMemoryPoolUtilizationMIBGroup")
)
if mibBuilder.loadTexts:
    ruijieMemoryMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-MEMORY-MIB",
    **{"Percent": Percent,
       "ruijieMemoryMIB": ruijieMemoryMIB,
       "ruijieMemoryPoolMIBObjects": ruijieMemoryPoolMIBObjects,
       "ruijieMemoryPoolUtilizationTable": ruijieMemoryPoolUtilizationTable,
       "ruijieMemoryPoolUtilizationEntry": ruijieMemoryPoolUtilizationEntry,
       "ruijieMemoryPoolIndex": ruijieMemoryPoolIndex,
       "ruijieMemoryPoolName": ruijieMemoryPoolName,
       "ruijieMemoryPoolCurrentUtilization": ruijieMemoryPoolCurrentUtilization,
       "ruijieMemoryPoolLowestUtilization": ruijieMemoryPoolLowestUtilization,
       "ruijieMemoryPoolLargestUtilization": ruijieMemoryPoolLargestUtilization,
       "ruijieMemoryPoolSize": ruijieMemoryPoolSize,
       "ruijieMemoryPoolUsed": ruijieMemoryPoolUsed,
       "ruijieMemoryPoolFree": ruijieMemoryPoolFree,
       "ruijieMemoryPoolWarning": ruijieMemoryPoolWarning,
       "ruijieMemoryPoolCritical": ruijieMemoryPoolCritical,
       "ruijieMemoryPoolAverageUtilization": ruijieMemoryPoolAverageUtilization,
       "ruijieMemoryPoolTotalSize": ruijieMemoryPoolTotalSize,
       "ruijieMemoryPoolUsedSize": ruijieMemoryPoolUsedSize,
       "ruijieMemoryPoolFreeSize": ruijieMemoryPoolFreeSize,
       "ruijieNodeMemoryPoolTable": ruijieNodeMemoryPoolTable,
       "ruijieNodeMemoryPoolEntry": ruijieNodeMemoryPoolEntry,
       "ruijieNodeMemoryPoolIndex": ruijieNodeMemoryPoolIndex,
       "ruijieNodeMemoryPoolName": ruijieNodeMemoryPoolName,
       "ruijieNodeMemoryPoolCurrentUtilization": ruijieNodeMemoryPoolCurrentUtilization,
       "ruijieNodeMemoryPoolLowestUtilization": ruijieNodeMemoryPoolLowestUtilization,
       "ruijieNodeMemoryPoolLargestUtilization": ruijieNodeMemoryPoolLargestUtilization,
       "ruijieNodeMemoryPoolSize": ruijieNodeMemoryPoolSize,
       "ruijieNodeMemoryPoolUsed": ruijieNodeMemoryPoolUsed,
       "ruijieNodeMemoryPoolFree": ruijieNodeMemoryPoolFree,
       "ruijieNodeMemoryPoolWarning": ruijieNodeMemoryPoolWarning,
       "ruijieNodeMemoryPoolCritical": ruijieNodeMemoryPoolCritical,
       "ruijieNodeMemoryPoolTotalSize": ruijieNodeMemoryPoolTotalSize,
       "ruijieNodeMemoryPoolUsedSize": ruijieNodeMemoryPoolUsedSize,
       "ruijieNodeMemoryPoolFreeSize": ruijieNodeMemoryPoolFreeSize,
       "ruijieLankApMemoryPoolTable": ruijieLankApMemoryPoolTable,
       "ruijieLankApMemoryPoolEntry": ruijieLankApMemoryPoolEntry,
       "ruijieLankApMemoryPoolMacAddr": ruijieLankApMemoryPoolMacAddr,
       "ruijieLankApMemoryPoolWarning": ruijieLankApMemoryPoolWarning,
       "ruijieLankApMemoryPoolCritical": ruijieLankApMemoryPoolCritical,
       "ruijieLankApMemoryPoolCurrentUtilization": ruijieLankApMemoryPoolCurrentUtilization,
       "ruijieLankApMemoryPoolAverageUtilization": ruijieLankApMemoryPoolAverageUtilization,
       "ruijieMemoryMIBConformance": ruijieMemoryMIBConformance,
       "ruijieMemoryMIBCompliances": ruijieMemoryMIBCompliances,
       "ruijieMemoryMIBCompliance": ruijieMemoryMIBCompliance,
       "ruijieMemoryMIBGroups": ruijieMemoryMIBGroups,
       "ruijieMemoryPoolUtilizationMIBGroup": ruijieMemoryPoolUtilizationMIBGroup,
       "ruijieNodeMemoryPoolMIBGroup": ruijieNodeMemoryPoolMIBGroup}
)
