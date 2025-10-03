# SNMP MIB module (CISCOSB-SYSMNG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cisco\CISCOSB-SYSMNG-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:29:58 2025
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

(Percents,
 switch001) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "Percents",
    "switch001")

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
 RowPointer,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlSysmngMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204)
)
if mibBuilder.loadTexts:
    rlSysmngMib.setRevisions(
        ("1970-01-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class SysmngResourceRouteType(TextualConvention, Integer32):
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
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2),
          ("ipmv4", 3),
          ("ipmv6", 4),
          ("nonIp", 5),
          ("ipv4Policy", 6),
          ("ipv6Policy", 7),
          ("vlanMapping", 8),
          ("totalCount", 9))
    )



class SysmngResourceRouteUsageType(TextualConvention, Integer32):
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
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("ipv4Neighbor", 1),
          ("ipv4Address", 2),
          ("ipv4Route", 3),
          ("ipv6Neighbor", 4),
          ("ipv6Address", 5),
          ("ipv6OnlinkPrefix", 6),
          ("ipv6Route", 7),
          ("ipmv4Route", 8),
          ("ipmv4RouteStarG", 9),
          ("ipmv6Route", 10),
          ("ipmv6RouteStarG", 11),
          ("ipv4PolicyRoute", 12),
          ("ipv6PolicyRoute", 13),
          ("vlanMapping", 14))
    )



class SysmngPoolType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("router", 1),
          ("iscsi", 2),
          ("voip", 3),
          ("misc", 4))
    )



# MIB Managed Objects in the order of their OIDs

_RlSysmngTcamAllocations_ObjectIdentity = ObjectIdentity
rlSysmngTcamAllocations = _RlSysmngTcamAllocations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 1)
)
_RlSysmngTcamAllocationsTable_Object = MibTable
rlSysmngTcamAllocationsTable = _RlSysmngTcamAllocationsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 1, 1)
)
if mibBuilder.loadTexts:
    rlSysmngTcamAllocationsTable.setStatus("current")
_RlSysmngTcamAllocationsEntry_Object = MibTableRow
rlSysmngTcamAllocationsEntry = _RlSysmngTcamAllocationsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 1, 1, 1)
)
rlSysmngTcamAllocationsEntry.setIndexNames(
    (0, "CISCOSB-SYSMNG-MIB", "rlSysmngTcamAllocProfileName"),
    (0, "CISCOSB-SYSMNG-MIB", "rlSysmngTcamAllocPoolType"),
)
if mibBuilder.loadTexts:
    rlSysmngTcamAllocationsEntry.setStatus("current")
_RlSysmngTcamAllocProfileName_Type = DisplayString
_RlSysmngTcamAllocProfileName_Object = MibTableColumn
rlSysmngTcamAllocProfileName = _RlSysmngTcamAllocProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 1, 1, 1, 1),
    _RlSysmngTcamAllocProfileName_Type()
)
rlSysmngTcamAllocProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlSysmngTcamAllocProfileName.setStatus("current")
_RlSysmngTcamAllocPoolType_Type = SysmngPoolType
_RlSysmngTcamAllocPoolType_Object = MibTableColumn
rlSysmngTcamAllocPoolType = _RlSysmngTcamAllocPoolType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 1, 1, 1, 2),
    _RlSysmngTcamAllocPoolType_Type()
)
rlSysmngTcamAllocPoolType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlSysmngTcamAllocPoolType.setStatus("current")


class _RlSysmngTcamAllocMinRequiredEntries_Type(Unsigned32):
    """Custom type rlSysmngTcamAllocMinRequiredEntries based on Unsigned32"""
    defaultValue = 0


_RlSysmngTcamAllocMinRequiredEntries_Type.__name__ = "Unsigned32"
_RlSysmngTcamAllocMinRequiredEntries_Object = MibTableColumn
rlSysmngTcamAllocMinRequiredEntries = _RlSysmngTcamAllocMinRequiredEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 1, 1, 1, 3),
    _RlSysmngTcamAllocMinRequiredEntries_Type()
)
rlSysmngTcamAllocMinRequiredEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSysmngTcamAllocMinRequiredEntries.setStatus("current")


class _RlSysmngTcamAllocStaticConfigEntries_Type(Unsigned32):
    """Custom type rlSysmngTcamAllocStaticConfigEntries based on Unsigned32"""
    defaultValue = 0


_RlSysmngTcamAllocStaticConfigEntries_Type.__name__ = "Unsigned32"
_RlSysmngTcamAllocStaticConfigEntries_Object = MibTableColumn
rlSysmngTcamAllocStaticConfigEntries = _RlSysmngTcamAllocStaticConfigEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 1, 1, 1, 4),
    _RlSysmngTcamAllocStaticConfigEntries_Type()
)
rlSysmngTcamAllocStaticConfigEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSysmngTcamAllocStaticConfigEntries.setStatus("current")


class _RlSysmngTcamAllocInUseEntries_Type(Unsigned32):
    """Custom type rlSysmngTcamAllocInUseEntries based on Unsigned32"""
    defaultValue = 0


_RlSysmngTcamAllocInUseEntries_Type.__name__ = "Unsigned32"
_RlSysmngTcamAllocInUseEntries_Object = MibTableColumn
rlSysmngTcamAllocInUseEntries = _RlSysmngTcamAllocInUseEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 1, 1, 1, 5),
    _RlSysmngTcamAllocInUseEntries_Type()
)
rlSysmngTcamAllocInUseEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSysmngTcamAllocInUseEntries.setStatus("current")


class _RlSysmngTcamAllocPoolSize_Type(Unsigned32):
    """Custom type rlSysmngTcamAllocPoolSize based on Unsigned32"""
    defaultValue = 0


_RlSysmngTcamAllocPoolSize_Type.__name__ = "Unsigned32"
_RlSysmngTcamAllocPoolSize_Object = MibTableColumn
rlSysmngTcamAllocPoolSize = _RlSysmngTcamAllocPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 1, 1, 1, 6),
    _RlSysmngTcamAllocPoolSize_Type()
)
rlSysmngTcamAllocPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSysmngTcamAllocPoolSize.setStatus("current")
_RlSysmngResource_ObjectIdentity = ObjectIdentity
rlSysmngResource = _RlSysmngResource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 2)
)
_RlSysmngResourceTable_Object = MibTable
rlSysmngResourceTable = _RlSysmngResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 2, 1)
)
if mibBuilder.loadTexts:
    rlSysmngResourceTable.setStatus("current")
_RlSysmngResourceEntry_Object = MibTableRow
rlSysmngResourceEntry = _RlSysmngResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 2, 1, 1)
)
rlSysmngResourceEntry.setIndexNames(
    (0, "CISCOSB-SYSMNG-MIB", "rlSysmngResourceRouteType"),
)
if mibBuilder.loadTexts:
    rlSysmngResourceEntry.setStatus("current")
_RlSysmngResourceRouteType_Type = SysmngResourceRouteType
_RlSysmngResourceRouteType_Object = MibTableColumn
rlSysmngResourceRouteType = _RlSysmngResourceRouteType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 2, 1, 1, 1),
    _RlSysmngResourceRouteType_Type()
)
rlSysmngResourceRouteType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlSysmngResourceRouteType.setStatus("current")


class _RlSysmngResourceCurrentUse_Type(Unsigned32):
    """Custom type rlSysmngResourceCurrentUse based on Unsigned32"""
    defaultValue = 0


_RlSysmngResourceCurrentUse_Type.__name__ = "Unsigned32"
_RlSysmngResourceCurrentUse_Object = MibTableColumn
rlSysmngResourceCurrentUse = _RlSysmngResourceCurrentUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 2, 1, 1, 2),
    _RlSysmngResourceCurrentUse_Type()
)
rlSysmngResourceCurrentUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSysmngResourceCurrentUse.setStatus("current")


class _RlSysmngResourceCurrentUseHw_Type(Unsigned32):
    """Custom type rlSysmngResourceCurrentUseHw based on Unsigned32"""
    defaultValue = 0


_RlSysmngResourceCurrentUseHw_Type.__name__ = "Unsigned32"
_RlSysmngResourceCurrentUseHw_Object = MibTableColumn
rlSysmngResourceCurrentUseHw = _RlSysmngResourceCurrentUseHw_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 2, 1, 1, 3),
    _RlSysmngResourceCurrentUseHw_Type()
)
rlSysmngResourceCurrentUseHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSysmngResourceCurrentUseHw.setStatus("current")


class _RlSysmngResourceCurrentMax_Type(Unsigned32):
    """Custom type rlSysmngResourceCurrentMax based on Unsigned32"""
    defaultValue = 0


_RlSysmngResourceCurrentMax_Type.__name__ = "Unsigned32"
_RlSysmngResourceCurrentMax_Object = MibTableColumn
rlSysmngResourceCurrentMax = _RlSysmngResourceCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 2, 1, 1, 4),
    _RlSysmngResourceCurrentMax_Type()
)
rlSysmngResourceCurrentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSysmngResourceCurrentMax.setStatus("current")


class _RlSysmngResourceCurrentMaxHw_Type(Unsigned32):
    """Custom type rlSysmngResourceCurrentMaxHw based on Unsigned32"""
    defaultValue = 0


_RlSysmngResourceCurrentMaxHw_Type.__name__ = "Unsigned32"
_RlSysmngResourceCurrentMaxHw_Object = MibTableColumn
rlSysmngResourceCurrentMaxHw = _RlSysmngResourceCurrentMaxHw_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 2, 1, 1, 5),
    _RlSysmngResourceCurrentMaxHw_Type()
)
rlSysmngResourceCurrentMaxHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSysmngResourceCurrentMaxHw.setStatus("current")


class _RlSysmngResourceTemporaryMax_Type(Unsigned32):
    """Custom type rlSysmngResourceTemporaryMax based on Unsigned32"""
    defaultValue = 0


_RlSysmngResourceTemporaryMax_Type.__name__ = "Unsigned32"
_RlSysmngResourceTemporaryMax_Object = MibTableColumn
rlSysmngResourceTemporaryMax = _RlSysmngResourceTemporaryMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 2, 1, 1, 6),
    _RlSysmngResourceTemporaryMax_Type()
)
rlSysmngResourceTemporaryMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSysmngResourceTemporaryMax.setStatus("current")


class _RlSysmngResourceTemporaryMaxHw_Type(Unsigned32):
    """Custom type rlSysmngResourceTemporaryMaxHw based on Unsigned32"""
    defaultValue = 0


_RlSysmngResourceTemporaryMaxHw_Type.__name__ = "Unsigned32"
_RlSysmngResourceTemporaryMaxHw_Object = MibTableColumn
rlSysmngResourceTemporaryMaxHw = _RlSysmngResourceTemporaryMaxHw_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 2, 1, 1, 7),
    _RlSysmngResourceTemporaryMaxHw_Type()
)
rlSysmngResourceTemporaryMaxHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSysmngResourceTemporaryMaxHw.setStatus("current")


class _RlSysmngResourceCurrentNexthopMax_Type(Unsigned32):
    """Custom type rlSysmngResourceCurrentNexthopMax based on Unsigned32"""
    defaultValue = 0


_RlSysmngResourceCurrentNexthopMax_Type.__name__ = "Unsigned32"
_RlSysmngResourceCurrentNexthopMax_Object = MibTableColumn
rlSysmngResourceCurrentNexthopMax = _RlSysmngResourceCurrentNexthopMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 2, 1, 1, 8),
    _RlSysmngResourceCurrentNexthopMax_Type()
)
rlSysmngResourceCurrentNexthopMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSysmngResourceCurrentNexthopMax.setStatus("current")


class _RlSysmngResourceCurrentNexthopMaxHw_Type(Unsigned32):
    """Custom type rlSysmngResourceCurrentNexthopMaxHw based on Unsigned32"""
    defaultValue = 0


_RlSysmngResourceCurrentNexthopMaxHw_Type.__name__ = "Unsigned32"
_RlSysmngResourceCurrentNexthopMaxHw_Object = MibTableColumn
rlSysmngResourceCurrentNexthopMaxHw = _RlSysmngResourceCurrentNexthopMaxHw_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 2, 1, 1, 9),
    _RlSysmngResourceCurrentNexthopMaxHw_Type()
)
rlSysmngResourceCurrentNexthopMaxHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSysmngResourceCurrentNexthopMaxHw.setStatus("current")


class _RlSysmngResourceCurrentNexthopUse_Type(Unsigned32):
    """Custom type rlSysmngResourceCurrentNexthopUse based on Unsigned32"""
    defaultValue = 0


_RlSysmngResourceCurrentNexthopUse_Type.__name__ = "Unsigned32"
_RlSysmngResourceCurrentNexthopUse_Object = MibTableColumn
rlSysmngResourceCurrentNexthopUse = _RlSysmngResourceCurrentNexthopUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 2, 1, 1, 10),
    _RlSysmngResourceCurrentNexthopUse_Type()
)
rlSysmngResourceCurrentNexthopUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSysmngResourceCurrentNexthopUse.setStatus("current")


class _RlSysmngResourceCurrentNexthopUseHw_Type(Unsigned32):
    """Custom type rlSysmngResourceCurrentNexthopUseHw based on Unsigned32"""
    defaultValue = 0


_RlSysmngResourceCurrentNexthopUseHw_Type.__name__ = "Unsigned32"
_RlSysmngResourceCurrentNexthopUseHw_Object = MibTableColumn
rlSysmngResourceCurrentNexthopUseHw = _RlSysmngResourceCurrentNexthopUseHw_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 2, 1, 1, 11),
    _RlSysmngResourceCurrentNexthopUseHw_Type()
)
rlSysmngResourceCurrentNexthopUseHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSysmngResourceCurrentNexthopUseHw.setStatus("current")
_RlSysmngRouterResourceAction_Type = Integer32
_RlSysmngRouterResourceAction_Object = MibScalar
rlSysmngRouterResourceAction = _RlSysmngRouterResourceAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 3),
    _RlSysmngRouterResourceAction_Type()
)
rlSysmngRouterResourceAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSysmngRouterResourceAction.setStatus("current")
_RlSysmngResourceUsage_ObjectIdentity = ObjectIdentity
rlSysmngResourceUsage = _RlSysmngResourceUsage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 4)
)
_RlSysmngResourceUsageTable_Object = MibTable
rlSysmngResourceUsageTable = _RlSysmngResourceUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 4, 1)
)
if mibBuilder.loadTexts:
    rlSysmngResourceUsageTable.setStatus("current")
_RlSysmngResourceUsageEntry_Object = MibTableRow
rlSysmngResourceUsageEntry = _RlSysmngResourceUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 4, 1, 1)
)
rlSysmngResourceUsageEntry.setIndexNames(
    (0, "CISCOSB-SYSMNG-MIB", "rlSysmngResourceUsageType"),
)
if mibBuilder.loadTexts:
    rlSysmngResourceUsageEntry.setStatus("current")
_RlSysmngResourceUsageType_Type = SysmngResourceRouteUsageType
_RlSysmngResourceUsageType_Object = MibTableColumn
rlSysmngResourceUsageType = _RlSysmngResourceUsageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 4, 1, 1, 1),
    _RlSysmngResourceUsageType_Type()
)
rlSysmngResourceUsageType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlSysmngResourceUsageType.setStatus("current")


class _RlSysmngResourceUsageNum_Type(Unsigned32):
    """Custom type rlSysmngResourceUsageNum based on Unsigned32"""
    defaultValue = 0


_RlSysmngResourceUsageNum_Type.__name__ = "Unsigned32"
_RlSysmngResourceUsageNum_Object = MibTableColumn
rlSysmngResourceUsageNum = _RlSysmngResourceUsageNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 4, 1, 1, 2),
    _RlSysmngResourceUsageNum_Type()
)
rlSysmngResourceUsageNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSysmngResourceUsageNum.setStatus("current")
_RlSysmngResourcePerUnit_ObjectIdentity = ObjectIdentity
rlSysmngResourcePerUnit = _RlSysmngResourcePerUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 5)
)
_RlSysmngResourcePerUnitTable_Object = MibTable
rlSysmngResourcePerUnitTable = _RlSysmngResourcePerUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 5, 1)
)
if mibBuilder.loadTexts:
    rlSysmngResourcePerUnitTable.setStatus("current")
_RlSysmngResourcePerUnitEntry_Object = MibTableRow
rlSysmngResourcePerUnitEntry = _RlSysmngResourcePerUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 5, 1, 1)
)
rlSysmngResourcePerUnitEntry.setIndexNames(
    (0, "CISCOSB-SYSMNG-MIB", "rlSysmngResourcePerUnitRouteType"),
    (0, "CISCOSB-SYSMNG-MIB", "rlSysmngResourcePerUnitUnitId"),
)
if mibBuilder.loadTexts:
    rlSysmngResourcePerUnitEntry.setStatus("current")
_RlSysmngResourcePerUnitRouteType_Type = SysmngResourceRouteType
_RlSysmngResourcePerUnitRouteType_Object = MibTableColumn
rlSysmngResourcePerUnitRouteType = _RlSysmngResourcePerUnitRouteType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 5, 1, 1, 1),
    _RlSysmngResourcePerUnitRouteType_Type()
)
rlSysmngResourcePerUnitRouteType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlSysmngResourcePerUnitRouteType.setStatus("current")
_RlSysmngResourcePerUnitUnitId_Type = Unsigned32
_RlSysmngResourcePerUnitUnitId_Object = MibTableColumn
rlSysmngResourcePerUnitUnitId = _RlSysmngResourcePerUnitUnitId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 5, 1, 1, 2),
    _RlSysmngResourcePerUnitUnitId_Type()
)
rlSysmngResourcePerUnitUnitId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlSysmngResourcePerUnitUnitId.setStatus("current")


class _RlSysmngResourcePerUnitCurrentUse_Type(Unsigned32):
    """Custom type rlSysmngResourcePerUnitCurrentUse based on Unsigned32"""
    defaultValue = 0


_RlSysmngResourcePerUnitCurrentUse_Type.__name__ = "Unsigned32"
_RlSysmngResourcePerUnitCurrentUse_Object = MibTableColumn
rlSysmngResourcePerUnitCurrentUse = _RlSysmngResourcePerUnitCurrentUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 5, 1, 1, 3),
    _RlSysmngResourcePerUnitCurrentUse_Type()
)
rlSysmngResourcePerUnitCurrentUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSysmngResourcePerUnitCurrentUse.setStatus("current")


class _RlSysmngResourcePerUnitCurrentUseHw_Type(Unsigned32):
    """Custom type rlSysmngResourcePerUnitCurrentUseHw based on Unsigned32"""
    defaultValue = 0


_RlSysmngResourcePerUnitCurrentUseHw_Type.__name__ = "Unsigned32"
_RlSysmngResourcePerUnitCurrentUseHw_Object = MibTableColumn
rlSysmngResourcePerUnitCurrentUseHw = _RlSysmngResourcePerUnitCurrentUseHw_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 5, 1, 1, 4),
    _RlSysmngResourcePerUnitCurrentUseHw_Type()
)
rlSysmngResourcePerUnitCurrentUseHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSysmngResourcePerUnitCurrentUseHw.setStatus("current")


class _RlSysmngResourcePerUnitCurrentMax_Type(Unsigned32):
    """Custom type rlSysmngResourcePerUnitCurrentMax based on Unsigned32"""
    defaultValue = 0


_RlSysmngResourcePerUnitCurrentMax_Type.__name__ = "Unsigned32"
_RlSysmngResourcePerUnitCurrentMax_Object = MibTableColumn
rlSysmngResourcePerUnitCurrentMax = _RlSysmngResourcePerUnitCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 5, 1, 1, 5),
    _RlSysmngResourcePerUnitCurrentMax_Type()
)
rlSysmngResourcePerUnitCurrentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSysmngResourcePerUnitCurrentMax.setStatus("current")


class _RlSysmngResourcePerUnitCurrentMaxHw_Type(Unsigned32):
    """Custom type rlSysmngResourcePerUnitCurrentMaxHw based on Unsigned32"""
    defaultValue = 0


_RlSysmngResourcePerUnitCurrentMaxHw_Type.__name__ = "Unsigned32"
_RlSysmngResourcePerUnitCurrentMaxHw_Object = MibTableColumn
rlSysmngResourcePerUnitCurrentMaxHw = _RlSysmngResourcePerUnitCurrentMaxHw_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 5, 1, 1, 6),
    _RlSysmngResourcePerUnitCurrentMaxHw_Type()
)
rlSysmngResourcePerUnitCurrentMaxHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSysmngResourcePerUnitCurrentMaxHw.setStatus("current")


class _RlSysmngResourcePerUnitTemporaryMax_Type(Unsigned32):
    """Custom type rlSysmngResourcePerUnitTemporaryMax based on Unsigned32"""
    defaultValue = 0


_RlSysmngResourcePerUnitTemporaryMax_Type.__name__ = "Unsigned32"
_RlSysmngResourcePerUnitTemporaryMax_Object = MibTableColumn
rlSysmngResourcePerUnitTemporaryMax = _RlSysmngResourcePerUnitTemporaryMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 5, 1, 1, 7),
    _RlSysmngResourcePerUnitTemporaryMax_Type()
)
rlSysmngResourcePerUnitTemporaryMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSysmngResourcePerUnitTemporaryMax.setStatus("current")


class _RlSysmngResourcePerUnitTemporaryMaxHw_Type(Unsigned32):
    """Custom type rlSysmngResourcePerUnitTemporaryMaxHw based on Unsigned32"""
    defaultValue = 0


_RlSysmngResourcePerUnitTemporaryMaxHw_Type.__name__ = "Unsigned32"
_RlSysmngResourcePerUnitTemporaryMaxHw_Object = MibTableColumn
rlSysmngResourcePerUnitTemporaryMaxHw = _RlSysmngResourcePerUnitTemporaryMaxHw_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 5, 1, 1, 8),
    _RlSysmngResourcePerUnitTemporaryMaxHw_Type()
)
rlSysmngResourcePerUnitTemporaryMaxHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSysmngResourcePerUnitTemporaryMaxHw.setStatus("current")


class _RlSysmngResourcePerUnitCurrentNexthopMax_Type(Unsigned32):
    """Custom type rlSysmngResourcePerUnitCurrentNexthopMax based on Unsigned32"""
    defaultValue = 0


_RlSysmngResourcePerUnitCurrentNexthopMax_Type.__name__ = "Unsigned32"
_RlSysmngResourcePerUnitCurrentNexthopMax_Object = MibTableColumn
rlSysmngResourcePerUnitCurrentNexthopMax = _RlSysmngResourcePerUnitCurrentNexthopMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 5, 1, 1, 9),
    _RlSysmngResourcePerUnitCurrentNexthopMax_Type()
)
rlSysmngResourcePerUnitCurrentNexthopMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSysmngResourcePerUnitCurrentNexthopMax.setStatus("current")


class _RlSysmngResourcePerUnitCurrentNexthopMaxHw_Type(Unsigned32):
    """Custom type rlSysmngResourcePerUnitCurrentNexthopMaxHw based on Unsigned32"""
    defaultValue = 0


_RlSysmngResourcePerUnitCurrentNexthopMaxHw_Type.__name__ = "Unsigned32"
_RlSysmngResourcePerUnitCurrentNexthopMaxHw_Object = MibTableColumn
rlSysmngResourcePerUnitCurrentNexthopMaxHw = _RlSysmngResourcePerUnitCurrentNexthopMaxHw_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 5, 1, 1, 10),
    _RlSysmngResourcePerUnitCurrentNexthopMaxHw_Type()
)
rlSysmngResourcePerUnitCurrentNexthopMaxHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSysmngResourcePerUnitCurrentNexthopMaxHw.setStatus("current")


class _RlSysmngResourcePerUnitCurrentNexthopUse_Type(Unsigned32):
    """Custom type rlSysmngResourcePerUnitCurrentNexthopUse based on Unsigned32"""
    defaultValue = 0


_RlSysmngResourcePerUnitCurrentNexthopUse_Type.__name__ = "Unsigned32"
_RlSysmngResourcePerUnitCurrentNexthopUse_Object = MibTableColumn
rlSysmngResourcePerUnitCurrentNexthopUse = _RlSysmngResourcePerUnitCurrentNexthopUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 5, 1, 1, 11),
    _RlSysmngResourcePerUnitCurrentNexthopUse_Type()
)
rlSysmngResourcePerUnitCurrentNexthopUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSysmngResourcePerUnitCurrentNexthopUse.setStatus("current")


class _RlSysmngResourcePerUnitCurrentNexthopUseHw_Type(Unsigned32):
    """Custom type rlSysmngResourcePerUnitCurrentNexthopUseHw based on Unsigned32"""
    defaultValue = 0


_RlSysmngResourcePerUnitCurrentNexthopUseHw_Type.__name__ = "Unsigned32"
_RlSysmngResourcePerUnitCurrentNexthopUseHw_Object = MibTableColumn
rlSysmngResourcePerUnitCurrentNexthopUseHw = _RlSysmngResourcePerUnitCurrentNexthopUseHw_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 5, 1, 1, 12),
    _RlSysmngResourcePerUnitCurrentNexthopUseHw_Type()
)
rlSysmngResourcePerUnitCurrentNexthopUseHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSysmngResourcePerUnitCurrentNexthopUseHw.setStatus("current")


class _RlRouterHwReactivate_Type(Integer32):
    """Custom type rlRouterHwReactivate based on Integer32"""
    defaultValue = 0


_RlRouterHwReactivate_Type.__name__ = "Integer32"
_RlRouterHwReactivate_Object = MibScalar
rlRouterHwReactivate = _RlRouterHwReactivate_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 6),
    _RlRouterHwReactivate_Type()
)
rlRouterHwReactivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRouterHwReactivate.setStatus("current")


class _RlRouterHwStatus_Type(Integer32):
    """Custom type rlRouterHwStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("inRecovery", 2),
          ("suspended", 3))
    )


_RlRouterHwStatus_Type.__name__ = "Integer32"
_RlRouterHwStatus_Object = MibScalar
rlRouterHwStatus = _RlRouterHwStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 7),
    _RlRouterHwStatus_Type()
)
rlRouterHwStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRouterHwStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-SYSMNG-MIB",
    **{"SysmngResourceRouteType": SysmngResourceRouteType,
       "SysmngResourceRouteUsageType": SysmngResourceRouteUsageType,
       "SysmngPoolType": SysmngPoolType,
       "rlSysmngMib": rlSysmngMib,
       "rlSysmngTcamAllocations": rlSysmngTcamAllocations,
       "rlSysmngTcamAllocationsTable": rlSysmngTcamAllocationsTable,
       "rlSysmngTcamAllocationsEntry": rlSysmngTcamAllocationsEntry,
       "rlSysmngTcamAllocProfileName": rlSysmngTcamAllocProfileName,
       "rlSysmngTcamAllocPoolType": rlSysmngTcamAllocPoolType,
       "rlSysmngTcamAllocMinRequiredEntries": rlSysmngTcamAllocMinRequiredEntries,
       "rlSysmngTcamAllocStaticConfigEntries": rlSysmngTcamAllocStaticConfigEntries,
       "rlSysmngTcamAllocInUseEntries": rlSysmngTcamAllocInUseEntries,
       "rlSysmngTcamAllocPoolSize": rlSysmngTcamAllocPoolSize,
       "rlSysmngResource": rlSysmngResource,
       "rlSysmngResourceTable": rlSysmngResourceTable,
       "rlSysmngResourceEntry": rlSysmngResourceEntry,
       "rlSysmngResourceRouteType": rlSysmngResourceRouteType,
       "rlSysmngResourceCurrentUse": rlSysmngResourceCurrentUse,
       "rlSysmngResourceCurrentUseHw": rlSysmngResourceCurrentUseHw,
       "rlSysmngResourceCurrentMax": rlSysmngResourceCurrentMax,
       "rlSysmngResourceCurrentMaxHw": rlSysmngResourceCurrentMaxHw,
       "rlSysmngResourceTemporaryMax": rlSysmngResourceTemporaryMax,
       "rlSysmngResourceTemporaryMaxHw": rlSysmngResourceTemporaryMaxHw,
       "rlSysmngResourceCurrentNexthopMax": rlSysmngResourceCurrentNexthopMax,
       "rlSysmngResourceCurrentNexthopMaxHw": rlSysmngResourceCurrentNexthopMaxHw,
       "rlSysmngResourceCurrentNexthopUse": rlSysmngResourceCurrentNexthopUse,
       "rlSysmngResourceCurrentNexthopUseHw": rlSysmngResourceCurrentNexthopUseHw,
       "rlSysmngRouterResourceAction": rlSysmngRouterResourceAction,
       "rlSysmngResourceUsage": rlSysmngResourceUsage,
       "rlSysmngResourceUsageTable": rlSysmngResourceUsageTable,
       "rlSysmngResourceUsageEntry": rlSysmngResourceUsageEntry,
       "rlSysmngResourceUsageType": rlSysmngResourceUsageType,
       "rlSysmngResourceUsageNum": rlSysmngResourceUsageNum,
       "rlSysmngResourcePerUnit": rlSysmngResourcePerUnit,
       "rlSysmngResourcePerUnitTable": rlSysmngResourcePerUnitTable,
       "rlSysmngResourcePerUnitEntry": rlSysmngResourcePerUnitEntry,
       "rlSysmngResourcePerUnitRouteType": rlSysmngResourcePerUnitRouteType,
       "rlSysmngResourcePerUnitUnitId": rlSysmngResourcePerUnitUnitId,
       "rlSysmngResourcePerUnitCurrentUse": rlSysmngResourcePerUnitCurrentUse,
       "rlSysmngResourcePerUnitCurrentUseHw": rlSysmngResourcePerUnitCurrentUseHw,
       "rlSysmngResourcePerUnitCurrentMax": rlSysmngResourcePerUnitCurrentMax,
       "rlSysmngResourcePerUnitCurrentMaxHw": rlSysmngResourcePerUnitCurrentMaxHw,
       "rlSysmngResourcePerUnitTemporaryMax": rlSysmngResourcePerUnitTemporaryMax,
       "rlSysmngResourcePerUnitTemporaryMaxHw": rlSysmngResourcePerUnitTemporaryMaxHw,
       "rlSysmngResourcePerUnitCurrentNexthopMax": rlSysmngResourcePerUnitCurrentNexthopMax,
       "rlSysmngResourcePerUnitCurrentNexthopMaxHw": rlSysmngResourcePerUnitCurrentNexthopMaxHw,
       "rlSysmngResourcePerUnitCurrentNexthopUse": rlSysmngResourcePerUnitCurrentNexthopUse,
       "rlSysmngResourcePerUnitCurrentNexthopUseHw": rlSysmngResourcePerUnitCurrentNexthopUseHw,
       "rlRouterHwReactivate": rlRouterHwReactivate,
       "rlRouterHwStatus": rlRouterHwStatus}
)
