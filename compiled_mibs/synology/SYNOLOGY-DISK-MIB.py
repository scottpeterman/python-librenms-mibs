# SNMP MIB module (SYNOLOGY-DISK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\synology\SYNOLOGY-DISK-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:29:26 2025
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

synoDisk = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 2)
)
if mibBuilder.loadTexts:
    synoDisk.setRevisions(
        ("2013-09-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Synology_ObjectIdentity = ObjectIdentity
synology = _Synology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574)
)
_DiskTable_Object = MibTable
diskTable = _DiskTable_Object(
    (1, 3, 6, 1, 4, 1, 6574, 2, 1)
)
if mibBuilder.loadTexts:
    diskTable.setStatus("current")
_DiskEntry_Object = MibTableRow
diskEntry = _DiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 6574, 2, 1, 1)
)
diskEntry.setIndexNames(
    (0, "SYNOLOGY-DISK-MIB", "diskIndex"),
)
if mibBuilder.loadTexts:
    diskEntry.setStatus("current")


class _DiskIndex_Type(Integer32):
    """Custom type diskIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DiskIndex_Type.__name__ = "Integer32"
_DiskIndex_Object = MibTableColumn
diskIndex = _DiskIndex_Object(
    (1, 3, 6, 1, 4, 1, 6574, 2, 1, 1, 1),
    _DiskIndex_Type()
)
diskIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskIndex.setStatus("current")
_DiskID_Type = OctetString
_DiskID_Object = MibTableColumn
diskID = _DiskID_Object(
    (1, 3, 6, 1, 4, 1, 6574, 2, 1, 1, 2),
    _DiskID_Type()
)
diskID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskID.setStatus("current")
_DiskModel_Type = OctetString
_DiskModel_Object = MibTableColumn
diskModel = _DiskModel_Object(
    (1, 3, 6, 1, 4, 1, 6574, 2, 1, 1, 3),
    _DiskModel_Type()
)
diskModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskModel.setStatus("current")
_DiskType_Type = OctetString
_DiskType_Object = MibTableColumn
diskType = _DiskType_Object(
    (1, 3, 6, 1, 4, 1, 6574, 2, 1, 1, 4),
    _DiskType_Type()
)
diskType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskType.setStatus("current")


class _DiskStatus_Type(Integer32):
    """Custom type diskStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_DiskStatus_Type.__name__ = "Integer32"
_DiskStatus_Object = MibTableColumn
diskStatus = _DiskStatus_Object(
    (1, 3, 6, 1, 4, 1, 6574, 2, 1, 1, 5),
    _DiskStatus_Type()
)
diskStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskStatus.setStatus("current")
_DiskTemperature_Type = Integer32
_DiskTemperature_Object = MibTableColumn
diskTemperature = _DiskTemperature_Object(
    (1, 3, 6, 1, 4, 1, 6574, 2, 1, 1, 6),
    _DiskTemperature_Type()
)
diskTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskTemperature.setStatus("current")
_DiskRole_Type = OctetString
_DiskRole_Object = MibTableColumn
diskRole = _DiskRole_Object(
    (1, 3, 6, 1, 4, 1, 6574, 2, 1, 1, 7),
    _DiskRole_Type()
)
diskRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskRole.setStatus("current")
_DiskRetry_Type = Integer32
_DiskRetry_Object = MibTableColumn
diskRetry = _DiskRetry_Object(
    (1, 3, 6, 1, 4, 1, 6574, 2, 1, 1, 8),
    _DiskRetry_Type()
)
diskRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskRetry.setStatus("current")
_DiskBadSector_Type = Integer32
_DiskBadSector_Object = MibTableColumn
diskBadSector = _DiskBadSector_Object(
    (1, 3, 6, 1, 4, 1, 6574, 2, 1, 1, 9),
    _DiskBadSector_Type()
)
diskBadSector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskBadSector.setStatus("current")
_DiskIdentifyFail_Type = Integer32
_DiskIdentifyFail_Object = MibTableColumn
diskIdentifyFail = _DiskIdentifyFail_Object(
    (1, 3, 6, 1, 4, 1, 6574, 2, 1, 1, 10),
    _DiskIdentifyFail_Type()
)
diskIdentifyFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskIdentifyFail.setStatus("current")
_DiskRemainLife_Type = Integer32
_DiskRemainLife_Object = MibTableColumn
diskRemainLife = _DiskRemainLife_Object(
    (1, 3, 6, 1, 4, 1, 6574, 2, 1, 1, 11),
    _DiskRemainLife_Type()
)
diskRemainLife.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskRemainLife.setStatus("current")
_DiskName_Type = OctetString
_DiskName_Object = MibTableColumn
diskName = _DiskName_Object(
    (1, 3, 6, 1, 4, 1, 6574, 2, 1, 1, 12),
    _DiskName_Type()
)
diskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskName.setStatus("current")


class _DiskHealthStatus_Type(Integer32):
    """Custom type diskHealthStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_DiskHealthStatus_Type.__name__ = "Integer32"
_DiskHealthStatus_Object = MibTableColumn
diskHealthStatus = _DiskHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 6574, 2, 1, 1, 13),
    _DiskHealthStatus_Type()
)
diskHealthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskHealthStatus.setStatus("current")
_DiskConformance_ObjectIdentity = ObjectIdentity
diskConformance = _DiskConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 2, 2)
)
_DiskCompliances_ObjectIdentity = ObjectIdentity
diskCompliances = _DiskCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 2, 2, 1)
)
_DiskGroups_ObjectIdentity = ObjectIdentity
diskGroups = _DiskGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 2, 2, 2)
)

# Managed Objects groups

diskGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6574, 2, 2, 2, 1)
)
diskGroup.setObjects(
      *(("SYNOLOGY-DISK-MIB", "diskIndex"),
        ("SYNOLOGY-DISK-MIB", "diskID"),
        ("SYNOLOGY-DISK-MIB", "diskModel"),
        ("SYNOLOGY-DISK-MIB", "diskType"),
        ("SYNOLOGY-DISK-MIB", "diskStatus"),
        ("SYNOLOGY-DISK-MIB", "diskTemperature"),
        ("SYNOLOGY-DISK-MIB", "diskRole"),
        ("SYNOLOGY-DISK-MIB", "diskRetry"),
        ("SYNOLOGY-DISK-MIB", "diskBadSector"),
        ("SYNOLOGY-DISK-MIB", "diskIdentifyFail"),
        ("SYNOLOGY-DISK-MIB", "diskRemainLife"),
        ("SYNOLOGY-DISK-MIB", "diskName"),
        ("SYNOLOGY-DISK-MIB", "diskHealthStatus"))
)
if mibBuilder.loadTexts:
    diskGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

diskCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6574, 2, 2, 1, 1)
)
diskCompliance.setObjects(
    ("SYNOLOGY-DISK-MIB", "diskGroup")
)
if mibBuilder.loadTexts:
    diskCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYNOLOGY-DISK-MIB",
    **{"synology": synology,
       "synoDisk": synoDisk,
       "diskTable": diskTable,
       "diskEntry": diskEntry,
       "diskIndex": diskIndex,
       "diskID": diskID,
       "diskModel": diskModel,
       "diskType": diskType,
       "diskStatus": diskStatus,
       "diskTemperature": diskTemperature,
       "diskRole": diskRole,
       "diskRetry": diskRetry,
       "diskBadSector": diskBadSector,
       "diskIdentifyFail": diskIdentifyFail,
       "diskRemainLife": diskRemainLife,
       "diskName": diskName,
       "diskHealthStatus": diskHealthStatus,
       "diskConformance": diskConformance,
       "diskCompliances": diskCompliances,
       "diskCompliance": diskCompliance,
       "diskGroups": diskGroups,
       "diskGroup": diskGroup}
)
