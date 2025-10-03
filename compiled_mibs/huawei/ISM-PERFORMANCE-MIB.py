# SNMP MIB module (ISM-PERFORMANCE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\huawei\ISM-PERFORMANCE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:59:55 2025
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
        ("2013-04-07 17:16",)
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
_HwPerformance_ObjectIdentity = ObjectIdentity
hwPerformance = _HwPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21)
)


class _HwPerformanceSwitch_Type(Integer32):
    """Custom type hwPerformanceSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwPerformanceSwitch_Type.__name__ = "Integer32"
_HwPerformanceSwitch_Object = MibScalar
hwPerformanceSwitch = _HwPerformanceSwitch_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 1),
    _HwPerformanceSwitch_Type()
)
hwPerformanceSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPerformanceSwitch.setStatus("current")
_HwPerfNodeTable_Object = MibTable
hwPerfNodeTable = _HwPerfNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 3)
)
if mibBuilder.loadTexts:
    hwPerfNodeTable.setStatus("current")
_HwPerfNodeEntry_Object = MibTableRow
hwPerfNodeEntry = _HwPerfNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 3, 1)
)
hwPerfNodeEntry.setIndexNames(
    (0, "ISM-PERFORMANCE-MIB", "hwPerfNodeIfIndex"),
)
if mibBuilder.loadTexts:
    hwPerfNodeEntry.setStatus("current")
_HwPerfNodeIfIndex_Type = Unsigned32
_HwPerfNodeIfIndex_Object = MibTableColumn
hwPerfNodeIfIndex = _HwPerfNodeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 3, 1, 1),
    _HwPerfNodeIfIndex_Type()
)
hwPerfNodeIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfNodeIfIndex.setStatus("current")
_HwPerfNodeCPUUsage_Type = Unsigned32
_HwPerfNodeCPUUsage_Object = MibTableColumn
hwPerfNodeCPUUsage = _HwPerfNodeCPUUsage_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 3, 1, 2),
    _HwPerfNodeCPUUsage_Type()
)
hwPerfNodeCPUUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfNodeCPUUsage.setStatus("current")
_HwPerfNodeAvgCacheUsage_Type = Unsigned32
_HwPerfNodeAvgCacheUsage_Object = MibTableColumn
hwPerfNodeAvgCacheUsage = _HwPerfNodeAvgCacheUsage_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 3, 1, 3),
    _HwPerfNodeAvgCacheUsage_Type()
)
hwPerfNodeAvgCacheUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfNodeAvgCacheUsage.setStatus("current")
_HwPerfNodeDelay_Type = Unsigned32
_HwPerfNodeDelay_Object = MibTableColumn
hwPerfNodeDelay = _HwPerfNodeDelay_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 3, 1, 4),
    _HwPerfNodeDelay_Type()
)
hwPerfNodeDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfNodeDelay.setStatus("current")
_HwPerfNodeTotalIOPS_Type = Unsigned32
_HwPerfNodeTotalIOPS_Object = MibTableColumn
hwPerfNodeTotalIOPS = _HwPerfNodeTotalIOPS_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 3, 1, 5),
    _HwPerfNodeTotalIOPS_Type()
)
hwPerfNodeTotalIOPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfNodeTotalIOPS.setStatus("current")
_HwPerfNodeReadIOPS_Type = Unsigned32
_HwPerfNodeReadIOPS_Object = MibTableColumn
hwPerfNodeReadIOPS = _HwPerfNodeReadIOPS_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 3, 1, 6),
    _HwPerfNodeReadIOPS_Type()
)
hwPerfNodeReadIOPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfNodeReadIOPS.setStatus("current")
_HwPerfNodeWriteIOPS_Type = Unsigned32
_HwPerfNodeWriteIOPS_Object = MibTableColumn
hwPerfNodeWriteIOPS = _HwPerfNodeWriteIOPS_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 3, 1, 7),
    _HwPerfNodeWriteIOPS_Type()
)
hwPerfNodeWriteIOPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfNodeWriteIOPS.setStatus("current")
_HwPerfNodeTotalTraffic_Type = Unsigned32
_HwPerfNodeTotalTraffic_Object = MibTableColumn
hwPerfNodeTotalTraffic = _HwPerfNodeTotalTraffic_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 3, 1, 8),
    _HwPerfNodeTotalTraffic_Type()
)
hwPerfNodeTotalTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfNodeTotalTraffic.setStatus("current")
_HwPerfNodeReadTraffic_Type = Unsigned32
_HwPerfNodeReadTraffic_Object = MibTableColumn
hwPerfNodeReadTraffic = _HwPerfNodeReadTraffic_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 3, 1, 9),
    _HwPerfNodeReadTraffic_Type()
)
hwPerfNodeReadTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfNodeReadTraffic.setStatus("current")
_HwPerfNodeWriteTraffic_Type = Unsigned32
_HwPerfNodeWriteTraffic_Object = MibTableColumn
hwPerfNodeWriteTraffic = _HwPerfNodeWriteTraffic_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 3, 1, 10),
    _HwPerfNodeWriteTraffic_Type()
)
hwPerfNodeWriteTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfNodeWriteTraffic.setStatus("current")
_HwPerfNodeFileBandwidth_Type = Counter64
_HwPerfNodeFileBandwidth_Object = MibTableColumn
hwPerfNodeFileBandwidth = _HwPerfNodeFileBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 3, 1, 11),
    _HwPerfNodeFileBandwidth_Type()
)
hwPerfNodeFileBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfNodeFileBandwidth.setStatus("current")
_HwPerfNodeFileOPS_Type = Counter64
_HwPerfNodeFileOPS_Object = MibTableColumn
hwPerfNodeFileOPS = _HwPerfNodeFileOPS_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 3, 1, 12),
    _HwPerfNodeFileOPS_Type()
)
hwPerfNodeFileOPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfNodeFileOPS.setStatus("current")
_HwPerfLunTable_Object = MibTable
hwPerfLunTable = _HwPerfLunTable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 4)
)
if mibBuilder.loadTexts:
    hwPerfLunTable.setStatus("current")
_HwPerfLunEntry_Object = MibTableRow
hwPerfLunEntry = _HwPerfLunEntry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 4, 1)
)
hwPerfLunEntry.setIndexNames(
    (0, "ISM-PERFORMANCE-MIB", "hwPerfLunID"),
)
if mibBuilder.loadTexts:
    hwPerfLunEntry.setStatus("current")
_HwPerfLunID_Type = Unsigned32
_HwPerfLunID_Object = MibTableColumn
hwPerfLunID = _HwPerfLunID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 4, 1, 1),
    _HwPerfLunID_Type()
)
hwPerfLunID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfLunID.setStatus("current")
_HwPerfLunHitRate_Type = Unsigned32
_HwPerfLunHitRate_Object = MibTableColumn
hwPerfLunHitRate = _HwPerfLunHitRate_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 4, 1, 2),
    _HwPerfLunHitRate_Type()
)
hwPerfLunHitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfLunHitRate.setStatus("current")
_HwPerfLunTotalIOPS_Type = Unsigned32
_HwPerfLunTotalIOPS_Object = MibTableColumn
hwPerfLunTotalIOPS = _HwPerfLunTotalIOPS_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 4, 1, 3),
    _HwPerfLunTotalIOPS_Type()
)
hwPerfLunTotalIOPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfLunTotalIOPS.setStatus("current")
_HwPerfLunReadIOPS_Type = Unsigned32
_HwPerfLunReadIOPS_Object = MibTableColumn
hwPerfLunReadIOPS = _HwPerfLunReadIOPS_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 4, 1, 4),
    _HwPerfLunReadIOPS_Type()
)
hwPerfLunReadIOPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfLunReadIOPS.setStatus("current")
_HwPerfLunWriteIOPS_Type = Unsigned32
_HwPerfLunWriteIOPS_Object = MibTableColumn
hwPerfLunWriteIOPS = _HwPerfLunWriteIOPS_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 4, 1, 5),
    _HwPerfLunWriteIOPS_Type()
)
hwPerfLunWriteIOPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfLunWriteIOPS.setStatus("current")
_HwPerfLunTotalTraffic_Type = Unsigned32
_HwPerfLunTotalTraffic_Object = MibTableColumn
hwPerfLunTotalTraffic = _HwPerfLunTotalTraffic_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 4, 1, 6),
    _HwPerfLunTotalTraffic_Type()
)
hwPerfLunTotalTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfLunTotalTraffic.setStatus("current")
_HwPerfLunReadTraffic_Type = Unsigned32
_HwPerfLunReadTraffic_Object = MibTableColumn
hwPerfLunReadTraffic = _HwPerfLunReadTraffic_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 4, 1, 7),
    _HwPerfLunReadTraffic_Type()
)
hwPerfLunReadTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfLunReadTraffic.setStatus("current")
_HwPerfLunWriteTraffic_Type = Unsigned32
_HwPerfLunWriteTraffic_Object = MibTableColumn
hwPerfLunWriteTraffic = _HwPerfLunWriteTraffic_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 4, 1, 8),
    _HwPerfLunWriteTraffic_Type()
)
hwPerfLunWriteTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfLunWriteTraffic.setStatus("current")
_HwPerfLunReadIORate_Type = Unsigned32
_HwPerfLunReadIORate_Object = MibTableColumn
hwPerfLunReadIORate = _HwPerfLunReadIORate_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 4, 1, 9),
    _HwPerfLunReadIORate_Type()
)
hwPerfLunReadIORate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfLunReadIORate.setStatus("current")
_HwPerfLunWriteIORate_Type = Unsigned32
_HwPerfLunWriteIORate_Object = MibTableColumn
hwPerfLunWriteIORate = _HwPerfLunWriteIORate_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 4, 1, 10),
    _HwPerfLunWriteIORate_Type()
)
hwPerfLunWriteIORate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfLunWriteIORate.setStatus("current")
_HwPerfLunMaxTraffic_Type = Unsigned32
_HwPerfLunMaxTraffic_Object = MibTableColumn
hwPerfLunMaxTraffic = _HwPerfLunMaxTraffic_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 4, 1, 11),
    _HwPerfLunMaxTraffic_Type()
)
hwPerfLunMaxTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfLunMaxTraffic.setStatus("current")
_HwPerfLunMaxIOPS_Type = Unsigned32
_HwPerfLunMaxIOPS_Object = MibTableColumn
hwPerfLunMaxIOPS = _HwPerfLunMaxIOPS_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 4, 1, 12),
    _HwPerfLunMaxIOPS_Type()
)
hwPerfLunMaxIOPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfLunMaxIOPS.setStatus("current")
_HwPerfPortTable_Object = MibTable
hwPerfPortTable = _HwPerfPortTable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 5)
)
if mibBuilder.loadTexts:
    hwPerfPortTable.setStatus("current")
_HwPerfPortEntry_Object = MibTableRow
hwPerfPortEntry = _HwPerfPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 5, 1)
)
hwPerfPortEntry.setIndexNames(
    (0, "ISM-PERFORMANCE-MIB", "hwPerfPortIfIndex"),
)
if mibBuilder.loadTexts:
    hwPerfPortEntry.setStatus("current")
_HwPerfPortIfIndex_Type = Unsigned32
_HwPerfPortIfIndex_Object = MibTableColumn
hwPerfPortIfIndex = _HwPerfPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 5, 1, 1),
    _HwPerfPortIfIndex_Type()
)
hwPerfPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfPortIfIndex.setStatus("current")
_HwPerfPortDelay_Type = Unsigned32
_HwPerfPortDelay_Object = MibTableColumn
hwPerfPortDelay = _HwPerfPortDelay_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 5, 1, 2),
    _HwPerfPortDelay_Type()
)
hwPerfPortDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfPortDelay.setStatus("current")
_HwPerfPortTotalIOPS_Type = Unsigned32
_HwPerfPortTotalIOPS_Object = MibTableColumn
hwPerfPortTotalIOPS = _HwPerfPortTotalIOPS_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 5, 1, 3),
    _HwPerfPortTotalIOPS_Type()
)
hwPerfPortTotalIOPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfPortTotalIOPS.setStatus("current")
_HwPerfPortReadIOPS_Type = Unsigned32
_HwPerfPortReadIOPS_Object = MibTableColumn
hwPerfPortReadIOPS = _HwPerfPortReadIOPS_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 5, 1, 4),
    _HwPerfPortReadIOPS_Type()
)
hwPerfPortReadIOPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfPortReadIOPS.setStatus("current")
_HwPerfPortWriteIOPS_Type = Unsigned32
_HwPerfPortWriteIOPS_Object = MibTableColumn
hwPerfPortWriteIOPS = _HwPerfPortWriteIOPS_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 5, 1, 5),
    _HwPerfPortWriteIOPS_Type()
)
hwPerfPortWriteIOPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfPortWriteIOPS.setStatus("current")
_HwPerfPortTotalTraffic_Type = Unsigned32
_HwPerfPortTotalTraffic_Object = MibTableColumn
hwPerfPortTotalTraffic = _HwPerfPortTotalTraffic_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 5, 1, 6),
    _HwPerfPortTotalTraffic_Type()
)
hwPerfPortTotalTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfPortTotalTraffic.setStatus("current")
_HwPerfPortReadTraffic_Type = Unsigned32
_HwPerfPortReadTraffic_Object = MibTableColumn
hwPerfPortReadTraffic = _HwPerfPortReadTraffic_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 5, 1, 7),
    _HwPerfPortReadTraffic_Type()
)
hwPerfPortReadTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfPortReadTraffic.setStatus("current")
_HwPerfPortWriteTraffic_Type = Unsigned32
_HwPerfPortWriteTraffic_Object = MibTableColumn
hwPerfPortWriteTraffic = _HwPerfPortWriteTraffic_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 5, 1, 8),
    _HwPerfPortWriteTraffic_Type()
)
hwPerfPortWriteTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfPortWriteTraffic.setStatus("current")
_HwPerfPortMaxTraffic_Type = Unsigned32
_HwPerfPortMaxTraffic_Object = MibTableColumn
hwPerfPortMaxTraffic = _HwPerfPortMaxTraffic_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 5, 1, 9),
    _HwPerfPortMaxTraffic_Type()
)
hwPerfPortMaxTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfPortMaxTraffic.setStatus("current")
_HwPerfPortMaxIOPS_Type = Unsigned32
_HwPerfPortMaxIOPS_Object = MibTableColumn
hwPerfPortMaxIOPS = _HwPerfPortMaxIOPS_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 5, 1, 10),
    _HwPerfPortMaxIOPS_Type()
)
hwPerfPortMaxIOPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfPortMaxIOPS.setStatus("current")
_HwPerfPortLocation_Type = OctetString
_HwPerfPortLocation_Object = MibTableColumn
hwPerfPortLocation = _HwPerfPortLocation_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 5, 1, 11),
    _HwPerfPortLocation_Type()
)
hwPerfPortLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfPortLocation.setStatus("current")
_HwPerfCacheTable_Object = MibTable
hwPerfCacheTable = _HwPerfCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 7)
)
if mibBuilder.loadTexts:
    hwPerfCacheTable.setStatus("current")
_HwPerfCacheEntry_Object = MibTableRow
hwPerfCacheEntry = _HwPerfCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 7, 1)
)
hwPerfCacheEntry.setIndexNames(
    (0, "ISM-PERFORMANCE-MIB", "hwPerfCacheID"),
)
if mibBuilder.loadTexts:
    hwPerfCacheEntry.setStatus("current")
_HwPerfCacheID_Type = Unsigned32
_HwPerfCacheID_Object = MibTableColumn
hwPerfCacheID = _HwPerfCacheID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 7, 1, 1),
    _HwPerfCacheID_Type()
)
hwPerfCacheID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfCacheID.setStatus("current")
_HwPerfCacheReadUtilization_Type = Integer32
_HwPerfCacheReadUtilization_Object = MibTableColumn
hwPerfCacheReadUtilization = _HwPerfCacheReadUtilization_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 7, 1, 2),
    _HwPerfCacheReadUtilization_Type()
)
hwPerfCacheReadUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfCacheReadUtilization.setStatus("current")
_HwPerfCacheWriteUtilization_Type = Integer32
_HwPerfCacheWriteUtilization_Object = MibTableColumn
hwPerfCacheWriteUtilization = _HwPerfCacheWriteUtilization_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 7, 1, 3),
    _HwPerfCacheWriteUtilization_Type()
)
hwPerfCacheWriteUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfCacheWriteUtilization.setStatus("current")
_HwPerfCacheMirrorWriteUtilization_Type = Integer32
_HwPerfCacheMirrorWriteUtilization_Object = MibTableColumn
hwPerfCacheMirrorWriteUtilization = _HwPerfCacheMirrorWriteUtilization_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 7, 1, 4),
    _HwPerfCacheMirrorWriteUtilization_Type()
)
hwPerfCacheMirrorWriteUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfCacheMirrorWriteUtilization.setStatus("current")
_HwPerfCacheHitRatio_Type = Integer32
_HwPerfCacheHitRatio_Object = MibTableColumn
hwPerfCacheHitRatio = _HwPerfCacheHitRatio_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 7, 1, 5),
    _HwPerfCacheHitRatio_Type()
)
hwPerfCacheHitRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfCacheHitRatio.setStatus("current")
_HwPerfControllerNFSV3Table_Object = MibTable
hwPerfControllerNFSV3Table = _HwPerfControllerNFSV3Table_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 10)
)
if mibBuilder.loadTexts:
    hwPerfControllerNFSV3Table.setStatus("current")
_HwPerfControllerNFSV3Entry_Object = MibTableRow
hwPerfControllerNFSV3Entry = _HwPerfControllerNFSV3Entry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 10, 1)
)
hwPerfControllerNFSV3Entry.setIndexNames(
    (0, "ISM-PERFORMANCE-MIB", "hwPerfControllerNFSV3ID"),
)
if mibBuilder.loadTexts:
    hwPerfControllerNFSV3Entry.setStatus("current")
_HwPerfControllerNFSV3ID_Type = OctetString
_HwPerfControllerNFSV3ID_Object = MibTableColumn
hwPerfControllerNFSV3ID = _HwPerfControllerNFSV3ID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 10, 1, 1),
    _HwPerfControllerNFSV3ID_Type()
)
hwPerfControllerNFSV3ID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfControllerNFSV3ID.setStatus("current")
_HwPerfControllerNFSV3OPS_Type = Counter64
_HwPerfControllerNFSV3OPS_Object = MibTableColumn
hwPerfControllerNFSV3OPS = _HwPerfControllerNFSV3OPS_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 10, 1, 2),
    _HwPerfControllerNFSV3OPS_Type()
)
hwPerfControllerNFSV3OPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfControllerNFSV3OPS.setStatus("current")
_HwPerfControllerNFSV3Bps_Type = Counter64
_HwPerfControllerNFSV3Bps_Object = MibTableColumn
hwPerfControllerNFSV3Bps = _HwPerfControllerNFSV3Bps_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 10, 1, 3),
    _HwPerfControllerNFSV3Bps_Type()
)
hwPerfControllerNFSV3Bps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfControllerNFSV3Bps.setStatus("current")
_HwPerfControllerNFSV4Table_Object = MibTable
hwPerfControllerNFSV4Table = _HwPerfControllerNFSV4Table_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 11)
)
if mibBuilder.loadTexts:
    hwPerfControllerNFSV4Table.setStatus("current")
_HwPerfControllerNFSV4Entry_Object = MibTableRow
hwPerfControllerNFSV4Entry = _HwPerfControllerNFSV4Entry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 11, 1)
)
hwPerfControllerNFSV4Entry.setIndexNames(
    (0, "ISM-PERFORMANCE-MIB", "hwPerfControllerNFSV4ID"),
)
if mibBuilder.loadTexts:
    hwPerfControllerNFSV4Entry.setStatus("current")
_HwPerfControllerNFSV4ID_Type = OctetString
_HwPerfControllerNFSV4ID_Object = MibTableColumn
hwPerfControllerNFSV4ID = _HwPerfControllerNFSV4ID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 11, 1, 1),
    _HwPerfControllerNFSV4ID_Type()
)
hwPerfControllerNFSV4ID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfControllerNFSV4ID.setStatus("current")
_HwPerfControllerNFSV4OPS_Type = Counter64
_HwPerfControllerNFSV4OPS_Object = MibTableColumn
hwPerfControllerNFSV4OPS = _HwPerfControllerNFSV4OPS_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 11, 1, 2),
    _HwPerfControllerNFSV4OPS_Type()
)
hwPerfControllerNFSV4OPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfControllerNFSV4OPS.setStatus("current")
_HwPerfControllerNFSV4Bps_Type = Counter64
_HwPerfControllerNFSV4Bps_Object = MibTableColumn
hwPerfControllerNFSV4Bps = _HwPerfControllerNFSV4Bps_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 11, 1, 3),
    _HwPerfControllerNFSV4Bps_Type()
)
hwPerfControllerNFSV4Bps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfControllerNFSV4Bps.setStatus("current")
_HwPerfControllerSMBV1Table_Object = MibTable
hwPerfControllerSMBV1Table = _HwPerfControllerSMBV1Table_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 12)
)
if mibBuilder.loadTexts:
    hwPerfControllerSMBV1Table.setStatus("current")
_HwPerfControllerSMBV1Entry_Object = MibTableRow
hwPerfControllerSMBV1Entry = _HwPerfControllerSMBV1Entry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 12, 1)
)
hwPerfControllerSMBV1Entry.setIndexNames(
    (0, "ISM-PERFORMANCE-MIB", "hwPerfControllerSMBV1ID"),
)
if mibBuilder.loadTexts:
    hwPerfControllerSMBV1Entry.setStatus("current")
_HwPerfControllerSMBV1ID_Type = OctetString
_HwPerfControllerSMBV1ID_Object = MibTableColumn
hwPerfControllerSMBV1ID = _HwPerfControllerSMBV1ID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 12, 1, 1),
    _HwPerfControllerSMBV1ID_Type()
)
hwPerfControllerSMBV1ID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfControllerSMBV1ID.setStatus("current")
_HwPerfControllerSMBV1OPS_Type = Counter64
_HwPerfControllerSMBV1OPS_Object = MibTableColumn
hwPerfControllerSMBV1OPS = _HwPerfControllerSMBV1OPS_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 12, 1, 2),
    _HwPerfControllerSMBV1OPS_Type()
)
hwPerfControllerSMBV1OPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfControllerSMBV1OPS.setStatus("current")
_HwPerfControllerSMBV1Bps_Type = Counter64
_HwPerfControllerSMBV1Bps_Object = MibTableColumn
hwPerfControllerSMBV1Bps = _HwPerfControllerSMBV1Bps_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 12, 1, 3),
    _HwPerfControllerSMBV1Bps_Type()
)
hwPerfControllerSMBV1Bps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfControllerSMBV1Bps.setStatus("current")
_HwPerfControllerSMBV2Table_Object = MibTable
hwPerfControllerSMBV2Table = _HwPerfControllerSMBV2Table_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 13)
)
if mibBuilder.loadTexts:
    hwPerfControllerSMBV2Table.setStatus("current")
_HwPerfControllerSMBV2Entry_Object = MibTableRow
hwPerfControllerSMBV2Entry = _HwPerfControllerSMBV2Entry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 13, 1)
)
hwPerfControllerSMBV2Entry.setIndexNames(
    (0, "ISM-PERFORMANCE-MIB", "hwPerfControllerSMBV2ID"),
)
if mibBuilder.loadTexts:
    hwPerfControllerSMBV2Entry.setStatus("current")
_HwPerfControllerSMBV2ID_Type = OctetString
_HwPerfControllerSMBV2ID_Object = MibTableColumn
hwPerfControllerSMBV2ID = _HwPerfControllerSMBV2ID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 13, 1, 1),
    _HwPerfControllerSMBV2ID_Type()
)
hwPerfControllerSMBV2ID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfControllerSMBV2ID.setStatus("current")
_HwPerfControllerSMBV2OPS_Type = Counter64
_HwPerfControllerSMBV2OPS_Object = MibTableColumn
hwPerfControllerSMBV2OPS = _HwPerfControllerSMBV2OPS_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 13, 1, 2),
    _HwPerfControllerSMBV2OPS_Type()
)
hwPerfControllerSMBV2OPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfControllerSMBV2OPS.setStatus("current")
_HwPerfControllerSMBV2Bps_Type = Counter64
_HwPerfControllerSMBV2Bps_Object = MibTableColumn
hwPerfControllerSMBV2Bps = _HwPerfControllerSMBV2Bps_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 13, 1, 3),
    _HwPerfControllerSMBV2Bps_Type()
)
hwPerfControllerSMBV2Bps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfControllerSMBV2Bps.setStatus("current")
_HwPerfFileSystemTable_Object = MibTable
hwPerfFileSystemTable = _HwPerfFileSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 14)
)
if mibBuilder.loadTexts:
    hwPerfFileSystemTable.setStatus("current")
_HwPerfFileSystemEntry_Object = MibTableRow
hwPerfFileSystemEntry = _HwPerfFileSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 14, 1)
)
hwPerfFileSystemEntry.setIndexNames(
    (0, "ISM-PERFORMANCE-MIB", "hwPerfFileSystemID"),
)
if mibBuilder.loadTexts:
    hwPerfFileSystemEntry.setStatus("current")
_HwPerfFileSystemID_Type = OctetString
_HwPerfFileSystemID_Object = MibTableColumn
hwPerfFileSystemID = _HwPerfFileSystemID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 14, 1, 1),
    _HwPerfFileSystemID_Type()
)
hwPerfFileSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfFileSystemID.setStatus("current")
_HwPerfFileSystemOPS_Type = Counter64
_HwPerfFileSystemOPS_Object = MibTableColumn
hwPerfFileSystemOPS = _HwPerfFileSystemOPS_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 14, 1, 2),
    _HwPerfFileSystemOPS_Type()
)
hwPerfFileSystemOPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfFileSystemOPS.setStatus("current")
_HwPerfFileSystemServiceTime_Type = Counter64
_HwPerfFileSystemServiceTime_Object = MibTableColumn
hwPerfFileSystemServiceTime = _HwPerfFileSystemServiceTime_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 14, 1, 3),
    _HwPerfFileSystemServiceTime_Type()
)
hwPerfFileSystemServiceTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfFileSystemServiceTime.setStatus("current")
_HwPerfFileSystemReadOPS_Type = Counter64
_HwPerfFileSystemReadOPS_Object = MibTableColumn
hwPerfFileSystemReadOPS = _HwPerfFileSystemReadOPS_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 14, 1, 4),
    _HwPerfFileSystemReadOPS_Type()
)
hwPerfFileSystemReadOPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfFileSystemReadOPS.setStatus("current")
_HwPerfFileSystemReadBandwidth_Type = Counter64
_HwPerfFileSystemReadBandwidth_Object = MibTableColumn
hwPerfFileSystemReadBandwidth = _HwPerfFileSystemReadBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 14, 1, 5),
    _HwPerfFileSystemReadBandwidth_Type()
)
hwPerfFileSystemReadBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfFileSystemReadBandwidth.setStatus("current")
_HwPerfFileSystemAvRdOPSRspTime_Type = Counter64
_HwPerfFileSystemAvRdOPSRspTime_Object = MibTableColumn
hwPerfFileSystemAvRdOPSRspTime = _HwPerfFileSystemAvRdOPSRspTime_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 14, 1, 6),
    _HwPerfFileSystemAvRdOPSRspTime_Type()
)
hwPerfFileSystemAvRdOPSRspTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfFileSystemAvRdOPSRspTime.setStatus("current")
_HwPerfFileSystemAvWrOPSRspTime_Type = Counter64
_HwPerfFileSystemAvWrOPSRspTime_Object = MibTableColumn
hwPerfFileSystemAvWrOPSRspTime = _HwPerfFileSystemAvWrOPSRspTime_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 14, 1, 7),
    _HwPerfFileSystemAvWrOPSRspTime_Type()
)
hwPerfFileSystemAvWrOPSRspTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfFileSystemAvWrOPSRspTime.setStatus("current")
_HwPerfFileSystemWriteOPS_Type = Counter64
_HwPerfFileSystemWriteOPS_Object = MibTableColumn
hwPerfFileSystemWriteOPS = _HwPerfFileSystemWriteOPS_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 14, 1, 8),
    _HwPerfFileSystemWriteOPS_Type()
)
hwPerfFileSystemWriteOPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfFileSystemWriteOPS.setStatus("current")
_HwPerfFileSystemWriteBandwidth_Type = Counter64
_HwPerfFileSystemWriteBandwidth_Object = MibTableColumn
hwPerfFileSystemWriteBandwidth = _HwPerfFileSystemWriteBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 21, 14, 1, 9),
    _HwPerfFileSystemWriteBandwidth_Type()
)
hwPerfFileSystemWriteBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfFileSystemWriteBandwidth.setStatus("current")
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
      *(("ISM-PERFORMANCE-MIB", "hwPerfControllerNFSV3ID"),
        ("ISM-PERFORMANCE-MIB", "hwPerfControllerNFSV4ID"),
        ("ISM-PERFORMANCE-MIB", "hwPerfControllerSMBV1ID"),
        ("ISM-PERFORMANCE-MIB", "hwPerfControllerSMBV2ID"),
        ("ISM-PERFORMANCE-MIB", "hwPerfFileSystemID"),
        ("ISM-PERFORMANCE-MIB", "hwPerfNodeCPUUsage"),
        ("ISM-PERFORMANCE-MIB", "hwPerfNodeAvgCacheUsage"),
        ("ISM-PERFORMANCE-MIB", "hwPerfLunTotalIOPS"),
        ("ISM-PERFORMANCE-MIB", "hwPerfLunHitRate"),
        ("ISM-PERFORMANCE-MIB", "hwPerfLunReadIOPS"),
        ("ISM-PERFORMANCE-MIB", "hwPerfLunWriteIOPS"),
        ("ISM-PERFORMANCE-MIB", "hwPerfLunTotalTraffic"),
        ("ISM-PERFORMANCE-MIB", "hwPerfLunReadTraffic"),
        ("ISM-PERFORMANCE-MIB", "hwPerfLunWriteTraffic"),
        ("ISM-PERFORMANCE-MIB", "hwPerfPortDelay"),
        ("ISM-PERFORMANCE-MIB", "hwPerfPortTotalIOPS"),
        ("ISM-PERFORMANCE-MIB", "hwPerfPortReadIOPS"),
        ("ISM-PERFORMANCE-MIB", "hwPerfPortWriteIOPS"),
        ("ISM-PERFORMANCE-MIB", "hwPerfPortTotalTraffic"),
        ("ISM-PERFORMANCE-MIB", "hwPerfPortReadTraffic"),
        ("ISM-PERFORMANCE-MIB", "hwPerfPortWriteTraffic"),
        ("ISM-PERFORMANCE-MIB", "hwPerfNodeDelay"),
        ("ISM-PERFORMANCE-MIB", "hwPerfNodeTotalIOPS"),
        ("ISM-PERFORMANCE-MIB", "hwPerfNodeReadIOPS"),
        ("ISM-PERFORMANCE-MIB", "hwPerfNodeWriteIOPS"),
        ("ISM-PERFORMANCE-MIB", "hwPerfNodeTotalTraffic"),
        ("ISM-PERFORMANCE-MIB", "hwPerfNodeReadTraffic"),
        ("ISM-PERFORMANCE-MIB", "hwPerfNodeWriteTraffic"),
        ("ISM-PERFORMANCE-MIB", "hwPerfLunID"),
        ("ISM-PERFORMANCE-MIB", "hwPerfPortIfIndex"),
        ("ISM-PERFORMANCE-MIB", "hwPerfLunWriteIORate"),
        ("ISM-PERFORMANCE-MIB", "hwPerfLunReadIORate"),
        ("ISM-PERFORMANCE-MIB", "hwPerfCacheID"),
        ("ISM-PERFORMANCE-MIB", "hwPerfCacheReadUtilization"),
        ("ISM-PERFORMANCE-MIB", "hwPerfCacheWriteUtilization"),
        ("ISM-PERFORMANCE-MIB", "hwPerfCacheMirrorWriteUtilization"),
        ("ISM-PERFORMANCE-MIB", "hwPerfCacheHitRatio"),
        ("ISM-PERFORMANCE-MIB", "hwPerfLunMaxTraffic"),
        ("ISM-PERFORMANCE-MIB", "hwPerfLunMaxIOPS"),
        ("ISM-PERFORMANCE-MIB", "hwPerfPortMaxTraffic"),
        ("ISM-PERFORMANCE-MIB", "hwPerfPortMaxIOPS"),
        ("ISM-PERFORMANCE-MIB", "hwPerfNodeFileBandwidth"),
        ("ISM-PERFORMANCE-MIB", "hwPerfNodeFileOPS"),
        ("ISM-PERFORMANCE-MIB", "hwPerfControllerNFSV3Bps"),
        ("ISM-PERFORMANCE-MIB", "hwPerfControllerNFSV3OPS"),
        ("ISM-PERFORMANCE-MIB", "hwPerfControllerNFSV4OPS"),
        ("ISM-PERFORMANCE-MIB", "hwPerfControllerNFSV4Bps"),
        ("ISM-PERFORMANCE-MIB", "hwPerfControllerSMBV1OPS"),
        ("ISM-PERFORMANCE-MIB", "hwPerfControllerSMBV2OPS"),
        ("ISM-PERFORMANCE-MIB", "hwPerfControllerSMBV2Bps"),
        ("ISM-PERFORMANCE-MIB", "hwPerfFileSystemOPS"),
        ("ISM-PERFORMANCE-MIB", "hwPerfFileSystemServiceTime"),
        ("ISM-PERFORMANCE-MIB", "hwPerfFileSystemReadOPS"),
        ("ISM-PERFORMANCE-MIB", "hwPerfFileSystemReadBandwidth"),
        ("ISM-PERFORMANCE-MIB", "hwPerfFileSystemWriteOPS"),
        ("ISM-PERFORMANCE-MIB", "hwPerfFileSystemWriteBandwidth"),
        ("ISM-PERFORMANCE-MIB", "hwPerformanceSwitch"),
        ("ISM-PERFORMANCE-MIB", "hwPerfFileSystemAvRdOPSRspTime"),
        ("ISM-PERFORMANCE-MIB", "hwPerfFileSystemAvWrOPSRspTime"),
        ("ISM-PERFORMANCE-MIB", "hwPerfPortLocation"),
        ("ISM-PERFORMANCE-MIB", "hwPerfControllerSMBV1Bps"),
        ("ISM-PERFORMANCE-MIB", "hwPerfNodeIfIndex"))
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
    ("ISM-PERFORMANCE-MIB", "currentObjectGroup")
)
if mibBuilder.loadTexts:
    basicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ISM-PERFORMANCE-MIB",
    **{"NodeCodeString": NodeCodeString,
       "huaweistorage": huaweistorage,
       "hwStorage": hwStorage,
       "hwISM": hwISM,
       "hwPerformance": hwPerformance,
       "hwPerformanceSwitch": hwPerformanceSwitch,
       "hwPerfNodeTable": hwPerfNodeTable,
       "hwPerfNodeEntry": hwPerfNodeEntry,
       "hwPerfNodeIfIndex": hwPerfNodeIfIndex,
       "hwPerfNodeCPUUsage": hwPerfNodeCPUUsage,
       "hwPerfNodeAvgCacheUsage": hwPerfNodeAvgCacheUsage,
       "hwPerfNodeDelay": hwPerfNodeDelay,
       "hwPerfNodeTotalIOPS": hwPerfNodeTotalIOPS,
       "hwPerfNodeReadIOPS": hwPerfNodeReadIOPS,
       "hwPerfNodeWriteIOPS": hwPerfNodeWriteIOPS,
       "hwPerfNodeTotalTraffic": hwPerfNodeTotalTraffic,
       "hwPerfNodeReadTraffic": hwPerfNodeReadTraffic,
       "hwPerfNodeWriteTraffic": hwPerfNodeWriteTraffic,
       "hwPerfNodeFileBandwidth": hwPerfNodeFileBandwidth,
       "hwPerfNodeFileOPS": hwPerfNodeFileOPS,
       "hwPerfLunTable": hwPerfLunTable,
       "hwPerfLunEntry": hwPerfLunEntry,
       "hwPerfLunID": hwPerfLunID,
       "hwPerfLunHitRate": hwPerfLunHitRate,
       "hwPerfLunTotalIOPS": hwPerfLunTotalIOPS,
       "hwPerfLunReadIOPS": hwPerfLunReadIOPS,
       "hwPerfLunWriteIOPS": hwPerfLunWriteIOPS,
       "hwPerfLunTotalTraffic": hwPerfLunTotalTraffic,
       "hwPerfLunReadTraffic": hwPerfLunReadTraffic,
       "hwPerfLunWriteTraffic": hwPerfLunWriteTraffic,
       "hwPerfLunReadIORate": hwPerfLunReadIORate,
       "hwPerfLunWriteIORate": hwPerfLunWriteIORate,
       "hwPerfLunMaxTraffic": hwPerfLunMaxTraffic,
       "hwPerfLunMaxIOPS": hwPerfLunMaxIOPS,
       "hwPerfPortTable": hwPerfPortTable,
       "hwPerfPortEntry": hwPerfPortEntry,
       "hwPerfPortIfIndex": hwPerfPortIfIndex,
       "hwPerfPortDelay": hwPerfPortDelay,
       "hwPerfPortTotalIOPS": hwPerfPortTotalIOPS,
       "hwPerfPortReadIOPS": hwPerfPortReadIOPS,
       "hwPerfPortWriteIOPS": hwPerfPortWriteIOPS,
       "hwPerfPortTotalTraffic": hwPerfPortTotalTraffic,
       "hwPerfPortReadTraffic": hwPerfPortReadTraffic,
       "hwPerfPortWriteTraffic": hwPerfPortWriteTraffic,
       "hwPerfPortMaxTraffic": hwPerfPortMaxTraffic,
       "hwPerfPortMaxIOPS": hwPerfPortMaxIOPS,
       "hwPerfPortLocation": hwPerfPortLocation,
       "hwPerfCacheTable": hwPerfCacheTable,
       "hwPerfCacheEntry": hwPerfCacheEntry,
       "hwPerfCacheID": hwPerfCacheID,
       "hwPerfCacheReadUtilization": hwPerfCacheReadUtilization,
       "hwPerfCacheWriteUtilization": hwPerfCacheWriteUtilization,
       "hwPerfCacheMirrorWriteUtilization": hwPerfCacheMirrorWriteUtilization,
       "hwPerfCacheHitRatio": hwPerfCacheHitRatio,
       "hwPerfControllerNFSV3Table": hwPerfControllerNFSV3Table,
       "hwPerfControllerNFSV3Entry": hwPerfControllerNFSV3Entry,
       "hwPerfControllerNFSV3ID": hwPerfControllerNFSV3ID,
       "hwPerfControllerNFSV3OPS": hwPerfControllerNFSV3OPS,
       "hwPerfControllerNFSV3Bps": hwPerfControllerNFSV3Bps,
       "hwPerfControllerNFSV4Table": hwPerfControllerNFSV4Table,
       "hwPerfControllerNFSV4Entry": hwPerfControllerNFSV4Entry,
       "hwPerfControllerNFSV4ID": hwPerfControllerNFSV4ID,
       "hwPerfControllerNFSV4OPS": hwPerfControllerNFSV4OPS,
       "hwPerfControllerNFSV4Bps": hwPerfControllerNFSV4Bps,
       "hwPerfControllerSMBV1Table": hwPerfControllerSMBV1Table,
       "hwPerfControllerSMBV1Entry": hwPerfControllerSMBV1Entry,
       "hwPerfControllerSMBV1ID": hwPerfControllerSMBV1ID,
       "hwPerfControllerSMBV1OPS": hwPerfControllerSMBV1OPS,
       "hwPerfControllerSMBV1Bps": hwPerfControllerSMBV1Bps,
       "hwPerfControllerSMBV2Table": hwPerfControllerSMBV2Table,
       "hwPerfControllerSMBV2Entry": hwPerfControllerSMBV2Entry,
       "hwPerfControllerSMBV2ID": hwPerfControllerSMBV2ID,
       "hwPerfControllerSMBV2OPS": hwPerfControllerSMBV2OPS,
       "hwPerfControllerSMBV2Bps": hwPerfControllerSMBV2Bps,
       "hwPerfFileSystemTable": hwPerfFileSystemTable,
       "hwPerfFileSystemEntry": hwPerfFileSystemEntry,
       "hwPerfFileSystemID": hwPerfFileSystemID,
       "hwPerfFileSystemOPS": hwPerfFileSystemOPS,
       "hwPerfFileSystemServiceTime": hwPerfFileSystemServiceTime,
       "hwPerfFileSystemReadOPS": hwPerfFileSystemReadOPS,
       "hwPerfFileSystemReadBandwidth": hwPerfFileSystemReadBandwidth,
       "hwPerfFileSystemAvRdOPSRspTime": hwPerfFileSystemAvRdOPSRspTime,
       "hwPerfFileSystemAvWrOPSRspTime": hwPerfFileSystemAvWrOPSRspTime,
       "hwPerfFileSystemWriteOPS": hwPerfFileSystemWriteOPS,
       "hwPerfFileSystemWriteBandwidth": hwPerfFileSystemWriteBandwidth,
       "isoConformance": isoConformance,
       "isoGroups": isoGroups,
       "currentObjectGroup": currentObjectGroup,
       "isoCompliances": isoCompliances,
       "basicCompliance": basicCompliance}
)
