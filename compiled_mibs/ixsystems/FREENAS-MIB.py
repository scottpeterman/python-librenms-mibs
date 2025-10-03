# SNMP MIB module (FREENAS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ixsystems\FREENAS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:02:10 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

freeNas = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 50536)
)
if mibBuilder.loadTexts:
    freeNas.setRevisions(
        ("2017-10-27 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ZPoolHealthType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("online", 0),
          ("degraded", 1),
          ("faulted", 2),
          ("offline", 3),
          ("unavail", 4),
          ("removed", 5))
    )



class AlertLevelType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(20,
              30,
              50)
        )
    )
    namedValues = NamedValues(
        *(("info", 20),
          ("warning", 30),
          ("critical", 50))
    )



# MIB Managed Objects in the order of their OIDs

_Zfs_ObjectIdentity = ObjectIdentity
zfs = _Zfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50536, 1)
)
_Zpool_ObjectIdentity = ObjectIdentity
zpool = _Zpool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50536, 1, 1)
)
_ZpoolTable_Object = MibTable
zpoolTable = _ZpoolTable_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 1, 1)
)
if mibBuilder.loadTexts:
    zpoolTable.setStatus("current")
_ZpoolEntry_Object = MibTableRow
zpoolEntry = _ZpoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 1, 1, 1)
)
zpoolEntry.setIndexNames(
    (0, "FREENAS-MIB", "zpoolIndex"),
)
if mibBuilder.loadTexts:
    zpoolEntry.setStatus("current")


class _ZpoolIndex_Type(Integer32):
    """Custom type zpoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ZpoolIndex_Type.__name__ = "Integer32"
_ZpoolIndex_Object = MibTableColumn
zpoolIndex = _ZpoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 1, 1, 1, 1),
    _ZpoolIndex_Type()
)
zpoolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zpoolIndex.setStatus("current")
_ZpoolDescr_Type = DisplayString
_ZpoolDescr_Object = MibTableColumn
zpoolDescr = _ZpoolDescr_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 1, 1, 1, 2),
    _ZpoolDescr_Type()
)
zpoolDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zpoolDescr.setStatus("current")


class _ZpoolAllocationUnits_Type(Integer32):
    """Custom type zpoolAllocationUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ZpoolAllocationUnits_Type.__name__ = "Integer32"
_ZpoolAllocationUnits_Object = MibTableColumn
zpoolAllocationUnits = _ZpoolAllocationUnits_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 1, 1, 1, 3),
    _ZpoolAllocationUnits_Type()
)
zpoolAllocationUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zpoolAllocationUnits.setStatus("current")
if mibBuilder.loadTexts:
    zpoolAllocationUnits.setUnits("Bytes")


class _ZpoolSize_Type(Integer32):
    """Custom type zpoolSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZpoolSize_Type.__name__ = "Integer32"
_ZpoolSize_Object = MibTableColumn
zpoolSize = _ZpoolSize_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 1, 1, 1, 4),
    _ZpoolSize_Type()
)
zpoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zpoolSize.setStatus("current")


class _ZpoolUsed_Type(Integer32):
    """Custom type zpoolUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZpoolUsed_Type.__name__ = "Integer32"
_ZpoolUsed_Object = MibTableColumn
zpoolUsed = _ZpoolUsed_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 1, 1, 1, 5),
    _ZpoolUsed_Type()
)
zpoolUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zpoolUsed.setStatus("current")


class _ZpoolAvailable_Type(Integer32):
    """Custom type zpoolAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZpoolAvailable_Type.__name__ = "Integer32"
_ZpoolAvailable_Object = MibTableColumn
zpoolAvailable = _ZpoolAvailable_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 1, 1, 1, 6),
    _ZpoolAvailable_Type()
)
zpoolAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zpoolAvailable.setStatus("current")
_ZpoolHealth_Type = ZPoolHealthType
_ZpoolHealth_Object = MibTableColumn
zpoolHealth = _ZpoolHealth_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 1, 1, 1, 7),
    _ZpoolHealth_Type()
)
zpoolHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zpoolHealth.setStatus("current")
_ZpoolReadOps_Type = Counter64
_ZpoolReadOps_Object = MibTableColumn
zpoolReadOps = _ZpoolReadOps_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 1, 1, 1, 8),
    _ZpoolReadOps_Type()
)
zpoolReadOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zpoolReadOps.setStatus("current")
_ZpoolWriteOps_Type = Counter64
_ZpoolWriteOps_Object = MibTableColumn
zpoolWriteOps = _ZpoolWriteOps_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 1, 1, 1, 9),
    _ZpoolWriteOps_Type()
)
zpoolWriteOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zpoolWriteOps.setStatus("current")
_ZpoolReadBytes_Type = Counter64
_ZpoolReadBytes_Object = MibTableColumn
zpoolReadBytes = _ZpoolReadBytes_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 1, 1, 1, 10),
    _ZpoolReadBytes_Type()
)
zpoolReadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zpoolReadBytes.setStatus("current")
_ZpoolWriteBytes_Type = Counter64
_ZpoolWriteBytes_Object = MibTableColumn
zpoolWriteBytes = _ZpoolWriteBytes_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 1, 1, 1, 11),
    _ZpoolWriteBytes_Type()
)
zpoolWriteBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zpoolWriteBytes.setStatus("current")
_ZpoolReadOps1sec_Type = Counter64
_ZpoolReadOps1sec_Object = MibTableColumn
zpoolReadOps1sec = _ZpoolReadOps1sec_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 1, 1, 1, 12),
    _ZpoolReadOps1sec_Type()
)
zpoolReadOps1sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zpoolReadOps1sec.setStatus("current")
_ZpoolWriteOps1sec_Type = Counter64
_ZpoolWriteOps1sec_Object = MibTableColumn
zpoolWriteOps1sec = _ZpoolWriteOps1sec_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 1, 1, 1, 13),
    _ZpoolWriteOps1sec_Type()
)
zpoolWriteOps1sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zpoolWriteOps1sec.setStatus("current")
_ZpoolReadBytes1sec_Type = Counter64
_ZpoolReadBytes1sec_Object = MibTableColumn
zpoolReadBytes1sec = _ZpoolReadBytes1sec_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 1, 1, 1, 14),
    _ZpoolReadBytes1sec_Type()
)
zpoolReadBytes1sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zpoolReadBytes1sec.setStatus("current")
_ZpoolWriteBytes1sec_Type = Counter64
_ZpoolWriteBytes1sec_Object = MibTableColumn
zpoolWriteBytes1sec = _ZpoolWriteBytes1sec_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 1, 1, 1, 15),
    _ZpoolWriteBytes1sec_Type()
)
zpoolWriteBytes1sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zpoolWriteBytes1sec.setStatus("current")
_Dataset_ObjectIdentity = ObjectIdentity
dataset = _Dataset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50536, 1, 2)
)
_DatasetTable_Object = MibTable
datasetTable = _DatasetTable_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 2, 1)
)
if mibBuilder.loadTexts:
    datasetTable.setStatus("current")
_DatasetEntry_Object = MibTableRow
datasetEntry = _DatasetEntry_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 2, 1, 1)
)
datasetEntry.setIndexNames(
    (0, "FREENAS-MIB", "datasetIndex"),
)
if mibBuilder.loadTexts:
    datasetEntry.setStatus("current")


class _DatasetIndex_Type(Integer32):
    """Custom type datasetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DatasetIndex_Type.__name__ = "Integer32"
_DatasetIndex_Object = MibTableColumn
datasetIndex = _DatasetIndex_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 2, 1, 1, 1),
    _DatasetIndex_Type()
)
datasetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    datasetIndex.setStatus("current")
_DatasetDescr_Type = DisplayString
_DatasetDescr_Object = MibTableColumn
datasetDescr = _DatasetDescr_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 2, 1, 1, 2),
    _DatasetDescr_Type()
)
datasetDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    datasetDescr.setStatus("current")


class _DatasetAllocationUnits_Type(Integer32):
    """Custom type datasetAllocationUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DatasetAllocationUnits_Type.__name__ = "Integer32"
_DatasetAllocationUnits_Object = MibTableColumn
datasetAllocationUnits = _DatasetAllocationUnits_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 2, 1, 1, 3),
    _DatasetAllocationUnits_Type()
)
datasetAllocationUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    datasetAllocationUnits.setStatus("current")
if mibBuilder.loadTexts:
    datasetAllocationUnits.setUnits("Bytes")


class _DatasetSize_Type(Integer32):
    """Custom type datasetSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DatasetSize_Type.__name__ = "Integer32"
_DatasetSize_Object = MibTableColumn
datasetSize = _DatasetSize_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 2, 1, 1, 4),
    _DatasetSize_Type()
)
datasetSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    datasetSize.setStatus("current")


class _DatasetUsed_Type(Integer32):
    """Custom type datasetUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DatasetUsed_Type.__name__ = "Integer32"
_DatasetUsed_Object = MibTableColumn
datasetUsed = _DatasetUsed_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 2, 1, 1, 5),
    _DatasetUsed_Type()
)
datasetUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    datasetUsed.setStatus("current")


class _DatasetAvailable_Type(Integer32):
    """Custom type datasetAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DatasetAvailable_Type.__name__ = "Integer32"
_DatasetAvailable_Object = MibTableColumn
datasetAvailable = _DatasetAvailable_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 2, 1, 1, 6),
    _DatasetAvailable_Type()
)
datasetAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    datasetAvailable.setStatus("current")
_Zvol_ObjectIdentity = ObjectIdentity
zvol = _Zvol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50536, 1, 3)
)
_ZvolTable_Object = MibTable
zvolTable = _ZvolTable_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 3, 1)
)
if mibBuilder.loadTexts:
    zvolTable.setStatus("current")
_ZvolEntry_Object = MibTableRow
zvolEntry = _ZvolEntry_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 3, 1, 1)
)
zvolEntry.setIndexNames(
    (0, "FREENAS-MIB", "zvolIndex"),
)
if mibBuilder.loadTexts:
    zvolEntry.setStatus("current")


class _ZvolIndex_Type(Integer32):
    """Custom type zvolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ZvolIndex_Type.__name__ = "Integer32"
_ZvolIndex_Object = MibTableColumn
zvolIndex = _ZvolIndex_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 3, 1, 1, 1),
    _ZvolIndex_Type()
)
zvolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zvolIndex.setStatus("current")
_ZvolDescr_Type = DisplayString
_ZvolDescr_Object = MibTableColumn
zvolDescr = _ZvolDescr_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 3, 1, 1, 2),
    _ZvolDescr_Type()
)
zvolDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zvolDescr.setStatus("current")


class _ZvolAllocationUnits_Type(Integer32):
    """Custom type zvolAllocationUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ZvolAllocationUnits_Type.__name__ = "Integer32"
_ZvolAllocationUnits_Object = MibTableColumn
zvolAllocationUnits = _ZvolAllocationUnits_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 3, 1, 1, 3),
    _ZvolAllocationUnits_Type()
)
zvolAllocationUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zvolAllocationUnits.setStatus("current")
if mibBuilder.loadTexts:
    zvolAllocationUnits.setUnits("Bytes")


class _ZvolSize_Type(Integer32):
    """Custom type zvolSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZvolSize_Type.__name__ = "Integer32"
_ZvolSize_Object = MibTableColumn
zvolSize = _ZvolSize_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 3, 1, 1, 4),
    _ZvolSize_Type()
)
zvolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zvolSize.setStatus("current")


class _ZvolUsed_Type(Integer32):
    """Custom type zvolUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZvolUsed_Type.__name__ = "Integer32"
_ZvolUsed_Object = MibTableColumn
zvolUsed = _ZvolUsed_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 3, 1, 1, 5),
    _ZvolUsed_Type()
)
zvolUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zvolUsed.setStatus("current")


class _ZvolAvailable_Type(Integer32):
    """Custom type zvolAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZvolAvailable_Type.__name__ = "Integer32"
_ZvolAvailable_Object = MibTableColumn
zvolAvailable = _ZvolAvailable_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 3, 1, 1, 6),
    _ZvolAvailable_Type()
)
zvolAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zvolAvailable.setStatus("current")
_Arc_ObjectIdentity = ObjectIdentity
arc = _Arc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50536, 1, 4)
)
_ZfsArcSize_Type = Gauge32
_ZfsArcSize_Object = MibScalar
zfsArcSize = _ZfsArcSize_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 4, 1),
    _ZfsArcSize_Type()
)
zfsArcSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zfsArcSize.setStatus("current")
_ZfsArcMeta_Type = Gauge32
_ZfsArcMeta_Object = MibScalar
zfsArcMeta = _ZfsArcMeta_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 4, 2),
    _ZfsArcMeta_Type()
)
zfsArcMeta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zfsArcMeta.setStatus("current")
_ZfsArcData_Type = Gauge32
_ZfsArcData_Object = MibScalar
zfsArcData = _ZfsArcData_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 4, 3),
    _ZfsArcData_Type()
)
zfsArcData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zfsArcData.setStatus("current")
_ZfsArcHits_Type = Gauge32
_ZfsArcHits_Object = MibScalar
zfsArcHits = _ZfsArcHits_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 4, 4),
    _ZfsArcHits_Type()
)
zfsArcHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zfsArcHits.setStatus("current")
_ZfsArcMisses_Type = Gauge32
_ZfsArcMisses_Object = MibScalar
zfsArcMisses = _ZfsArcMisses_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 4, 5),
    _ZfsArcMisses_Type()
)
zfsArcMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zfsArcMisses.setStatus("current")
_ZfsArcC_Type = Gauge32
_ZfsArcC_Object = MibScalar
zfsArcC = _ZfsArcC_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 4, 6),
    _ZfsArcC_Type()
)
zfsArcC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zfsArcC.setStatus("current")
_ZfsArcP_Type = Gauge32
_ZfsArcP_Object = MibScalar
zfsArcP = _ZfsArcP_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 4, 7),
    _ZfsArcP_Type()
)
zfsArcP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zfsArcP.setStatus("current")
_ZfsArcMissPercent_Type = DisplayString
_ZfsArcMissPercent_Object = MibScalar
zfsArcMissPercent = _ZfsArcMissPercent_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 4, 8),
    _ZfsArcMissPercent_Type()
)
zfsArcMissPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zfsArcMissPercent.setStatus("current")
_ZfsArcCacheHitRatio_Type = DisplayString
_ZfsArcCacheHitRatio_Object = MibScalar
zfsArcCacheHitRatio = _ZfsArcCacheHitRatio_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 4, 9),
    _ZfsArcCacheHitRatio_Type()
)
zfsArcCacheHitRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zfsArcCacheHitRatio.setStatus("current")
_ZfsArcCacheMissRatio_Type = DisplayString
_ZfsArcCacheMissRatio_Object = MibScalar
zfsArcCacheMissRatio = _ZfsArcCacheMissRatio_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 4, 10),
    _ZfsArcCacheMissRatio_Type()
)
zfsArcCacheMissRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zfsArcCacheMissRatio.setStatus("current")
_L2arc_ObjectIdentity = ObjectIdentity
l2arc = _L2arc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50536, 1, 5)
)
_ZfsL2ArcHits_Type = Counter32
_ZfsL2ArcHits_Object = MibScalar
zfsL2ArcHits = _ZfsL2ArcHits_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 5, 1),
    _ZfsL2ArcHits_Type()
)
zfsL2ArcHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zfsL2ArcHits.setStatus("current")
_ZfsL2ArcMisses_Type = Counter32
_ZfsL2ArcMisses_Object = MibScalar
zfsL2ArcMisses = _ZfsL2ArcMisses_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 5, 2),
    _ZfsL2ArcMisses_Type()
)
zfsL2ArcMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zfsL2ArcMisses.setStatus("current")
_ZfsL2ArcRead_Type = Counter32
_ZfsL2ArcRead_Object = MibScalar
zfsL2ArcRead = _ZfsL2ArcRead_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 5, 3),
    _ZfsL2ArcRead_Type()
)
zfsL2ArcRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zfsL2ArcRead.setStatus("current")
_ZfsL2ArcWrite_Type = Counter32
_ZfsL2ArcWrite_Object = MibScalar
zfsL2ArcWrite = _ZfsL2ArcWrite_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 5, 4),
    _ZfsL2ArcWrite_Type()
)
zfsL2ArcWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zfsL2ArcWrite.setStatus("current")
_ZfsL2ArcSize_Type = Gauge32
_ZfsL2ArcSize_Object = MibScalar
zfsL2ArcSize = _ZfsL2ArcSize_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 5, 5),
    _ZfsL2ArcSize_Type()
)
zfsL2ArcSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zfsL2ArcSize.setStatus("current")
_Zil_ObjectIdentity = ObjectIdentity
zil = _Zil_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50536, 1, 6)
)
_ZfsZilstatOps1sec_Type = Counter64
_ZfsZilstatOps1sec_Object = MibScalar
zfsZilstatOps1sec = _ZfsZilstatOps1sec_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 6, 1),
    _ZfsZilstatOps1sec_Type()
)
zfsZilstatOps1sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zfsZilstatOps1sec.setStatus("current")
_ZfsZilstatOps5sec_Type = Counter64
_ZfsZilstatOps5sec_Object = MibScalar
zfsZilstatOps5sec = _ZfsZilstatOps5sec_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 6, 2),
    _ZfsZilstatOps5sec_Type()
)
zfsZilstatOps5sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zfsZilstatOps5sec.setStatus("current")
_ZfsZilstatOps10sec_Type = Counter64
_ZfsZilstatOps10sec_Object = MibScalar
zfsZilstatOps10sec = _ZfsZilstatOps10sec_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 6, 3),
    _ZfsZilstatOps10sec_Type()
)
zfsZilstatOps10sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zfsZilstatOps10sec.setStatus("current")
_Notifications_ObjectIdentity = ObjectIdentity
notifications = _Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50536, 2)
)
_NotificationPrefix_ObjectIdentity = ObjectIdentity
notificationPrefix = _NotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50536, 2, 1)
)
_NotificationObjects_ObjectIdentity = ObjectIdentity
notificationObjects = _NotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50536, 2, 2)
)
_AlertId_Type = DisplayString
_AlertId_Object = MibScalar
alertId = _AlertId_Object(
    (1, 3, 6, 1, 4, 1, 50536, 2, 2, 1),
    _AlertId_Type()
)
alertId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertId.setStatus("current")
_AlertLevel_Type = AlertLevelType
_AlertLevel_Object = MibScalar
alertLevel = _AlertLevel_Object(
    (1, 3, 6, 1, 4, 1, 50536, 2, 2, 2),
    _AlertLevel_Type()
)
alertLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertLevel.setStatus("current")
_AlertMessage_Type = DisplayString
_AlertMessage_Object = MibScalar
alertMessage = _AlertMessage_Object(
    (1, 3, 6, 1, 4, 1, 50536, 2, 2, 3),
    _AlertMessage_Type()
)
alertMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertMessage.setStatus("current")

# Managed Objects groups


# Notification objects

alert = NotificationType(
    (1, 3, 6, 1, 4, 1, 50536, 2, 1, 1)
)
alert.setObjects(
      *(("FREENAS-MIB", "alertId"),
        ("FREENAS-MIB", "alertLevel"),
        ("FREENAS-MIB", "alertMessage"))
)
if mibBuilder.loadTexts:
    alert.setStatus(
        "current"
    )

alertCancellation = NotificationType(
    (1, 3, 6, 1, 4, 1, 50536, 2, 1, 2)
)
alertCancellation.setObjects(
    ("FREENAS-MIB", "alertId")
)
if mibBuilder.loadTexts:
    alertCancellation.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FREENAS-MIB",
    **{"ZPoolHealthType": ZPoolHealthType,
       "AlertLevelType": AlertLevelType,
       "freeNas": freeNas,
       "zfs": zfs,
       "zpool": zpool,
       "zpoolTable": zpoolTable,
       "zpoolEntry": zpoolEntry,
       "zpoolIndex": zpoolIndex,
       "zpoolDescr": zpoolDescr,
       "zpoolAllocationUnits": zpoolAllocationUnits,
       "zpoolSize": zpoolSize,
       "zpoolUsed": zpoolUsed,
       "zpoolAvailable": zpoolAvailable,
       "zpoolHealth": zpoolHealth,
       "zpoolReadOps": zpoolReadOps,
       "zpoolWriteOps": zpoolWriteOps,
       "zpoolReadBytes": zpoolReadBytes,
       "zpoolWriteBytes": zpoolWriteBytes,
       "zpoolReadOps1sec": zpoolReadOps1sec,
       "zpoolWriteOps1sec": zpoolWriteOps1sec,
       "zpoolReadBytes1sec": zpoolReadBytes1sec,
       "zpoolWriteBytes1sec": zpoolWriteBytes1sec,
       "dataset": dataset,
       "datasetTable": datasetTable,
       "datasetEntry": datasetEntry,
       "datasetIndex": datasetIndex,
       "datasetDescr": datasetDescr,
       "datasetAllocationUnits": datasetAllocationUnits,
       "datasetSize": datasetSize,
       "datasetUsed": datasetUsed,
       "datasetAvailable": datasetAvailable,
       "zvol": zvol,
       "zvolTable": zvolTable,
       "zvolEntry": zvolEntry,
       "zvolIndex": zvolIndex,
       "zvolDescr": zvolDescr,
       "zvolAllocationUnits": zvolAllocationUnits,
       "zvolSize": zvolSize,
       "zvolUsed": zvolUsed,
       "zvolAvailable": zvolAvailable,
       "arc": arc,
       "zfsArcSize": zfsArcSize,
       "zfsArcMeta": zfsArcMeta,
       "zfsArcData": zfsArcData,
       "zfsArcHits": zfsArcHits,
       "zfsArcMisses": zfsArcMisses,
       "zfsArcC": zfsArcC,
       "zfsArcP": zfsArcP,
       "zfsArcMissPercent": zfsArcMissPercent,
       "zfsArcCacheHitRatio": zfsArcCacheHitRatio,
       "zfsArcCacheMissRatio": zfsArcCacheMissRatio,
       "l2arc": l2arc,
       "zfsL2ArcHits": zfsL2ArcHits,
       "zfsL2ArcMisses": zfsL2ArcMisses,
       "zfsL2ArcRead": zfsL2ArcRead,
       "zfsL2ArcWrite": zfsL2ArcWrite,
       "zfsL2ArcSize": zfsL2ArcSize,
       "zil": zil,
       "zfsZilstatOps1sec": zfsZilstatOps1sec,
       "zfsZilstatOps5sec": zfsZilstatOps5sec,
       "zfsZilstatOps10sec": zfsZilstatOps10sec,
       "notifications": notifications,
       "notificationPrefix": notificationPrefix,
       "alert": alert,
       "alertCancellation": alertCancellation,
       "notificationObjects": notificationObjects,
       "alertId": alertId,
       "alertLevel": alertLevel,
       "alertMessage": alertMessage}
)
