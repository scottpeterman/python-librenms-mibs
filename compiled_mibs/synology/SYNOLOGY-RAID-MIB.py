# SNMP MIB module (SYNOLOGY-RAID-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\synology\SYNOLOGY-RAID-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:29:27 2025
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

synoRaid = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 3)
)
if mibBuilder.loadTexts:
    synoRaid.setRevisions(
        ("2013-09-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Synology_ObjectIdentity = ObjectIdentity
synology = _Synology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574)
)
_RaidTable_Object = MibTable
raidTable = _RaidTable_Object(
    (1, 3, 6, 1, 4, 1, 6574, 3, 1)
)
if mibBuilder.loadTexts:
    raidTable.setStatus("current")
_RaidEntry_Object = MibTableRow
raidEntry = _RaidEntry_Object(
    (1, 3, 6, 1, 4, 1, 6574, 3, 1, 1)
)
raidEntry.setIndexNames(
    (0, "SYNOLOGY-RAID-MIB", "raidIndex"),
)
if mibBuilder.loadTexts:
    raidEntry.setStatus("current")


class _RaidIndex_Type(Integer32):
    """Custom type raidIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RaidIndex_Type.__name__ = "Integer32"
_RaidIndex_Object = MibTableColumn
raidIndex = _RaidIndex_Object(
    (1, 3, 6, 1, 4, 1, 6574, 3, 1, 1, 1),
    _RaidIndex_Type()
)
raidIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidIndex.setStatus("current")
_RaidName_Type = OctetString
_RaidName_Object = MibTableColumn
raidName = _RaidName_Object(
    (1, 3, 6, 1, 4, 1, 6574, 3, 1, 1, 2),
    _RaidName_Type()
)
raidName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidName.setStatus("current")


class _RaidStatus_Type(Integer32):
    """Custom type raidStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_RaidStatus_Type.__name__ = "Integer32"
_RaidStatus_Object = MibTableColumn
raidStatus = _RaidStatus_Object(
    (1, 3, 6, 1, 4, 1, 6574, 3, 1, 1, 3),
    _RaidStatus_Type()
)
raidStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidStatus.setStatus("current")
_RaidFreeSize_Type = Counter64
_RaidFreeSize_Object = MibTableColumn
raidFreeSize = _RaidFreeSize_Object(
    (1, 3, 6, 1, 4, 1, 6574, 3, 1, 1, 4),
    _RaidFreeSize_Type()
)
raidFreeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidFreeSize.setStatus("current")
_RaidTotalSize_Type = Counter64
_RaidTotalSize_Object = MibTableColumn
raidTotalSize = _RaidTotalSize_Object(
    (1, 3, 6, 1, 4, 1, 6574, 3, 1, 1, 5),
    _RaidTotalSize_Type()
)
raidTotalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidTotalSize.setStatus("current")
_RaidHotspareCnt_Type = Integer32
_RaidHotspareCnt_Object = MibTableColumn
raidHotspareCnt = _RaidHotspareCnt_Object(
    (1, 3, 6, 1, 4, 1, 6574, 3, 1, 1, 6),
    _RaidHotspareCnt_Type()
)
raidHotspareCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidHotspareCnt.setStatus("current")
_RaidConformance_ObjectIdentity = ObjectIdentity
raidConformance = _RaidConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 3, 2)
)
_RaidCompliances_ObjectIdentity = ObjectIdentity
raidCompliances = _RaidCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 3, 2, 1)
)
_RaidGroups_ObjectIdentity = ObjectIdentity
raidGroups = _RaidGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 3, 2, 2)
)

# Managed Objects groups

raidGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6574, 3, 2, 2, 1)
)
raidGroup.setObjects(
      *(("SYNOLOGY-RAID-MIB", "raidIndex"),
        ("SYNOLOGY-RAID-MIB", "raidName"),
        ("SYNOLOGY-RAID-MIB", "raidStatus"),
        ("SYNOLOGY-RAID-MIB", "raidFreeSize"),
        ("SYNOLOGY-RAID-MIB", "raidTotalSize"),
        ("SYNOLOGY-RAID-MIB", "raidHotspareCnt"))
)
if mibBuilder.loadTexts:
    raidGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

raidCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6574, 3, 2, 1, 1)
)
raidCompliance.setObjects(
    ("SYNOLOGY-RAID-MIB", "raidGroup")
)
if mibBuilder.loadTexts:
    raidCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYNOLOGY-RAID-MIB",
    **{"synology": synology,
       "synoRaid": synoRaid,
       "raidTable": raidTable,
       "raidEntry": raidEntry,
       "raidIndex": raidIndex,
       "raidName": raidName,
       "raidStatus": raidStatus,
       "raidFreeSize": raidFreeSize,
       "raidTotalSize": raidTotalSize,
       "raidHotspareCnt": raidHotspareCnt,
       "raidConformance": raidConformance,
       "raidCompliances": raidCompliances,
       "raidCompliance": raidCompliance,
       "raidGroups": raidGroups,
       "raidGroup": raidGroup}
)
