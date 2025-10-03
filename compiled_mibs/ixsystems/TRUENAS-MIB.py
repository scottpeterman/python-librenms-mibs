# SNMP MIB module (TRUENAS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ixsystems\TRUENAS-MIB
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

trueNas = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 50536)
)
if mibBuilder.loadTexts:
    trueNas.setRevisions(
        ("2022-12-21 18:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AlertLevelType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("info", 1),
          ("notice", 2),
          ("warning", 3),
          ("error", 4),
          ("critical", 5),
          ("alert", 6),
          ("emergency", 7))
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
    (0, "TRUENAS-MIB", "zpoolIndex"),
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
_ZpoolName_Type = DisplayString
_ZpoolName_Object = MibTableColumn
zpoolName = _ZpoolName_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 1, 1, 1, 2),
    _ZpoolName_Type()
)
zpoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zpoolName.setStatus("current")
_ZpoolHealth_Type = DisplayString
_ZpoolHealth_Object = MibTableColumn
zpoolHealth = _ZpoolHealth_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 1, 1, 1, 3),
    _ZpoolHealth_Type()
)
zpoolHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zpoolHealth.setStatus("current")
_ZpoolReadOps_Type = Counter64
_ZpoolReadOps_Object = MibTableColumn
zpoolReadOps = _ZpoolReadOps_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 1, 1, 1, 4),
    _ZpoolReadOps_Type()
)
zpoolReadOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zpoolReadOps.setStatus("current")
_ZpoolWriteOps_Type = Counter64
_ZpoolWriteOps_Object = MibTableColumn
zpoolWriteOps = _ZpoolWriteOps_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 1, 1, 1, 5),
    _ZpoolWriteOps_Type()
)
zpoolWriteOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zpoolWriteOps.setStatus("current")
_ZpoolReadBytes_Type = Counter64
_ZpoolReadBytes_Object = MibTableColumn
zpoolReadBytes = _ZpoolReadBytes_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 1, 1, 1, 6),
    _ZpoolReadBytes_Type()
)
zpoolReadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zpoolReadBytes.setStatus("current")
_ZpoolWriteBytes_Type = Counter64
_ZpoolWriteBytes_Object = MibTableColumn
zpoolWriteBytes = _ZpoolWriteBytes_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 1, 1, 1, 7),
    _ZpoolWriteBytes_Type()
)
zpoolWriteBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zpoolWriteBytes.setStatus("current")
_ZpoolReadOps1sec_Type = Counter64
_ZpoolReadOps1sec_Object = MibTableColumn
zpoolReadOps1sec = _ZpoolReadOps1sec_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 1, 1, 1, 8),
    _ZpoolReadOps1sec_Type()
)
zpoolReadOps1sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zpoolReadOps1sec.setStatus("current")
_ZpoolWriteOps1sec_Type = Counter64
_ZpoolWriteOps1sec_Object = MibTableColumn
zpoolWriteOps1sec = _ZpoolWriteOps1sec_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 1, 1, 1, 9),
    _ZpoolWriteOps1sec_Type()
)
zpoolWriteOps1sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zpoolWriteOps1sec.setStatus("current")
_ZpoolReadBytes1sec_Type = Counter64
_ZpoolReadBytes1sec_Object = MibTableColumn
zpoolReadBytes1sec = _ZpoolReadBytes1sec_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 1, 1, 1, 10),
    _ZpoolReadBytes1sec_Type()
)
zpoolReadBytes1sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zpoolReadBytes1sec.setStatus("current")
_ZpoolWriteBytes1sec_Type = Counter64
_ZpoolWriteBytes1sec_Object = MibTableColumn
zpoolWriteBytes1sec = _ZpoolWriteBytes1sec_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 1, 1, 1, 11),
    _ZpoolWriteBytes1sec_Type()
)
zpoolWriteBytes1sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zpoolWriteBytes1sec.setStatus("current")
_Zvol_ObjectIdentity = ObjectIdentity
zvol = _Zvol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50536, 1, 2)
)
_ZvolTable_Object = MibTable
zvolTable = _ZvolTable_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 2, 1)
)
if mibBuilder.loadTexts:
    zvolTable.setStatus("current")
_ZvolEntry_Object = MibTableRow
zvolEntry = _ZvolEntry_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 2, 1, 1)
)
zvolEntry.setIndexNames(
    (0, "TRUENAS-MIB", "zvolIndex"),
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
    (1, 3, 6, 1, 4, 1, 50536, 1, 2, 1, 1, 1),
    _ZvolIndex_Type()
)
zvolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zvolIndex.setStatus("current")
_ZvolDescr_Type = DisplayString
_ZvolDescr_Object = MibTableColumn
zvolDescr = _ZvolDescr_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 2, 1, 1, 2),
    _ZvolDescr_Type()
)
zvolDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zvolDescr.setStatus("current")
_ZvolUsedBytes_Type = Counter64
_ZvolUsedBytes_Object = MibTableColumn
zvolUsedBytes = _ZvolUsedBytes_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 2, 1, 1, 3),
    _ZvolUsedBytes_Type()
)
zvolUsedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zvolUsedBytes.setStatus("current")
_ZvolAvailableBytes_Type = Counter64
_ZvolAvailableBytes_Object = MibTableColumn
zvolAvailableBytes = _ZvolAvailableBytes_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 2, 1, 1, 4),
    _ZvolAvailableBytes_Type()
)
zvolAvailableBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zvolAvailableBytes.setStatus("current")
_ZvolReferencedBytes_Type = Counter64
_ZvolReferencedBytes_Object = MibTableColumn
zvolReferencedBytes = _ZvolReferencedBytes_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 2, 1, 1, 5),
    _ZvolReferencedBytes_Type()
)
zvolReferencedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zvolReferencedBytes.setStatus("current")
_Arc_ObjectIdentity = ObjectIdentity
arc = _Arc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50536, 1, 3)
)
_ZfsArcSize_Type = Gauge32
_ZfsArcSize_Object = MibScalar
zfsArcSize = _ZfsArcSize_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 3, 1),
    _ZfsArcSize_Type()
)
zfsArcSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zfsArcSize.setStatus("current")
_ZfsArcMeta_Type = Gauge32
_ZfsArcMeta_Object = MibScalar
zfsArcMeta = _ZfsArcMeta_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 3, 2),
    _ZfsArcMeta_Type()
)
zfsArcMeta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zfsArcMeta.setStatus("current")
_ZfsArcData_Type = Gauge32
_ZfsArcData_Object = MibScalar
zfsArcData = _ZfsArcData_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 3, 3),
    _ZfsArcData_Type()
)
zfsArcData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zfsArcData.setStatus("current")
_ZfsArcHits_Type = Gauge32
_ZfsArcHits_Object = MibScalar
zfsArcHits = _ZfsArcHits_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 3, 4),
    _ZfsArcHits_Type()
)
zfsArcHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zfsArcHits.setStatus("current")
_ZfsArcMisses_Type = Gauge32
_ZfsArcMisses_Object = MibScalar
zfsArcMisses = _ZfsArcMisses_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 3, 5),
    _ZfsArcMisses_Type()
)
zfsArcMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zfsArcMisses.setStatus("current")
_ZfsArcC_Type = Gauge32
_ZfsArcC_Object = MibScalar
zfsArcC = _ZfsArcC_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 3, 6),
    _ZfsArcC_Type()
)
zfsArcC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zfsArcC.setStatus("current")
_ZfsArcMissPercent_Type = DisplayString
_ZfsArcMissPercent_Object = MibScalar
zfsArcMissPercent = _ZfsArcMissPercent_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 3, 8),
    _ZfsArcMissPercent_Type()
)
zfsArcMissPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zfsArcMissPercent.setStatus("current")
_ZfsArcCacheHitRatio_Type = DisplayString
_ZfsArcCacheHitRatio_Object = MibScalar
zfsArcCacheHitRatio = _ZfsArcCacheHitRatio_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 3, 9),
    _ZfsArcCacheHitRatio_Type()
)
zfsArcCacheHitRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zfsArcCacheHitRatio.setStatus("current")
_ZfsArcCacheMissRatio_Type = DisplayString
_ZfsArcCacheMissRatio_Object = MibScalar
zfsArcCacheMissRatio = _ZfsArcCacheMissRatio_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 3, 10),
    _ZfsArcCacheMissRatio_Type()
)
zfsArcCacheMissRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zfsArcCacheMissRatio.setStatus("current")
_L2arc_ObjectIdentity = ObjectIdentity
l2arc = _L2arc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50536, 1, 4)
)
_ZfsL2ArcHits_Type = Counter32
_ZfsL2ArcHits_Object = MibScalar
zfsL2ArcHits = _ZfsL2ArcHits_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 4, 1),
    _ZfsL2ArcHits_Type()
)
zfsL2ArcHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zfsL2ArcHits.setStatus("current")
_ZfsL2ArcMisses_Type = Counter32
_ZfsL2ArcMisses_Object = MibScalar
zfsL2ArcMisses = _ZfsL2ArcMisses_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 4, 2),
    _ZfsL2ArcMisses_Type()
)
zfsL2ArcMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zfsL2ArcMisses.setStatus("current")
_ZfsL2ArcRead_Type = Counter32
_ZfsL2ArcRead_Object = MibScalar
zfsL2ArcRead = _ZfsL2ArcRead_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 4, 3),
    _ZfsL2ArcRead_Type()
)
zfsL2ArcRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zfsL2ArcRead.setStatus("current")
_ZfsL2ArcWrite_Type = Counter32
_ZfsL2ArcWrite_Object = MibScalar
zfsL2ArcWrite = _ZfsL2ArcWrite_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 4, 4),
    _ZfsL2ArcWrite_Type()
)
zfsL2ArcWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zfsL2ArcWrite.setStatus("current")
_ZfsL2ArcSize_Type = Gauge32
_ZfsL2ArcSize_Object = MibScalar
zfsL2ArcSize = _ZfsL2ArcSize_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 4, 5),
    _ZfsL2ArcSize_Type()
)
zfsL2ArcSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zfsL2ArcSize.setStatus("current")
_Zil_ObjectIdentity = ObjectIdentity
zil = _Zil_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50536, 1, 5)
)
_ZfsZilstatOps1sec_Type = Counter64
_ZfsZilstatOps1sec_Object = MibScalar
zfsZilstatOps1sec = _ZfsZilstatOps1sec_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 5, 1),
    _ZfsZilstatOps1sec_Type()
)
zfsZilstatOps1sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zfsZilstatOps1sec.setStatus("current")
_ZfsZilstatOps5sec_Type = Counter64
_ZfsZilstatOps5sec_Object = MibScalar
zfsZilstatOps5sec = _ZfsZilstatOps5sec_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 5, 2),
    _ZfsZilstatOps5sec_Type()
)
zfsZilstatOps5sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zfsZilstatOps5sec.setStatus("current")
_ZfsZilstatOps10sec_Type = Counter64
_ZfsZilstatOps10sec_Object = MibScalar
zfsZilstatOps10sec = _ZfsZilstatOps10sec_Object(
    (1, 3, 6, 1, 4, 1, 50536, 1, 5, 3),
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
_HddTempTable_Object = MibTable
hddTempTable = _HddTempTable_Object(
    (1, 3, 6, 1, 4, 1, 50536, 3)
)
if mibBuilder.loadTexts:
    hddTempTable.setStatus("current")
_HddTempEntry_Object = MibTableRow
hddTempEntry = _HddTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 50536, 3, 1)
)
hddTempEntry.setIndexNames(
    (0, "TRUENAS-MIB", "hddTempIndex"),
)
if mibBuilder.loadTexts:
    hddTempEntry.setStatus("current")


class _HddTempIndex_Type(Integer32):
    """Custom type hddTempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HddTempIndex_Type.__name__ = "Integer32"
_HddTempIndex_Object = MibTableColumn
hddTempIndex = _HddTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 50536, 3, 1, 1),
    _HddTempIndex_Type()
)
hddTempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddTempIndex.setStatus("current")
_HddTempDevice_Type = DisplayString
_HddTempDevice_Object = MibTableColumn
hddTempDevice = _HddTempDevice_Object(
    (1, 3, 6, 1, 4, 1, 50536, 3, 1, 2),
    _HddTempDevice_Type()
)
hddTempDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddTempDevice.setStatus("current")
_HddTempValue_Type = Gauge32
_HddTempValue_Object = MibTableColumn
hddTempValue = _HddTempValue_Object(
    (1, 3, 6, 1, 4, 1, 50536, 3, 1, 3),
    _HddTempValue_Type()
)
hddTempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddTempValue.setStatus("current")

# Managed Objects groups


# Notification objects

alert = NotificationType(
    (1, 3, 6, 1, 4, 1, 50536, 2, 1, 1)
)
alert.setObjects(
      *(("TRUENAS-MIB", "alertId"),
        ("TRUENAS-MIB", "alertLevel"),
        ("TRUENAS-MIB", "alertMessage"))
)
if mibBuilder.loadTexts:
    alert.setStatus(
        "current"
    )

alertCancellation = NotificationType(
    (1, 3, 6, 1, 4, 1, 50536, 2, 1, 2)
)
alertCancellation.setObjects(
    ("TRUENAS-MIB", "alertId")
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
    "TRUENAS-MIB",
    **{"AlertLevelType": AlertLevelType,
       "trueNas": trueNas,
       "zfs": zfs,
       "zpool": zpool,
       "zpoolTable": zpoolTable,
       "zpoolEntry": zpoolEntry,
       "zpoolIndex": zpoolIndex,
       "zpoolName": zpoolName,
       "zpoolHealth": zpoolHealth,
       "zpoolReadOps": zpoolReadOps,
       "zpoolWriteOps": zpoolWriteOps,
       "zpoolReadBytes": zpoolReadBytes,
       "zpoolWriteBytes": zpoolWriteBytes,
       "zpoolReadOps1sec": zpoolReadOps1sec,
       "zpoolWriteOps1sec": zpoolWriteOps1sec,
       "zpoolReadBytes1sec": zpoolReadBytes1sec,
       "zpoolWriteBytes1sec": zpoolWriteBytes1sec,
       "zvol": zvol,
       "zvolTable": zvolTable,
       "zvolEntry": zvolEntry,
       "zvolIndex": zvolIndex,
       "zvolDescr": zvolDescr,
       "zvolUsedBytes": zvolUsedBytes,
       "zvolAvailableBytes": zvolAvailableBytes,
       "zvolReferencedBytes": zvolReferencedBytes,
       "arc": arc,
       "zfsArcSize": zfsArcSize,
       "zfsArcMeta": zfsArcMeta,
       "zfsArcData": zfsArcData,
       "zfsArcHits": zfsArcHits,
       "zfsArcMisses": zfsArcMisses,
       "zfsArcC": zfsArcC,
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
       "alertMessage": alertMessage,
       "hddTempTable": hddTempTable,
       "hddTempEntry": hddTempEntry,
       "hddTempIndex": hddTempIndex,
       "hddTempDevice": hddTempDevice,
       "hddTempValue": hddTempValue}
)
