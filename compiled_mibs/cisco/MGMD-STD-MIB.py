# SNMP MIB module (MGMD-STD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\MGMD-STD-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:29:04 2025
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

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

mgmdStdMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 185)
)
if mibBuilder.loadTexts:
    mgmdStdMIB.setRevisions(
        ("2009-03-30 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MgmdMIBObjects_ObjectIdentity = ObjectIdentity
mgmdMIBObjects = _MgmdMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 185, 1)
)
_MgmdHostInterfaceTable_Object = MibTable
mgmdHostInterfaceTable = _MgmdHostInterfaceTable_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 1)
)
if mibBuilder.loadTexts:
    mgmdHostInterfaceTable.setStatus("current")
_MgmdHostInterfaceEntry_Object = MibTableRow
mgmdHostInterfaceEntry = _MgmdHostInterfaceEntry_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 1, 1)
)
mgmdHostInterfaceEntry.setIndexNames(
    (0, "MGMD-STD-MIB", "mgmdHostInterfaceIfIndex"),
    (0, "MGMD-STD-MIB", "mgmdHostInterfaceQuerierType"),
)
if mibBuilder.loadTexts:
    mgmdHostInterfaceEntry.setStatus("current")
_MgmdHostInterfaceIfIndex_Type = InterfaceIndex
_MgmdHostInterfaceIfIndex_Object = MibTableColumn
mgmdHostInterfaceIfIndex = _MgmdHostInterfaceIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 1, 1, 1),
    _MgmdHostInterfaceIfIndex_Type()
)
mgmdHostInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgmdHostInterfaceIfIndex.setStatus("current")


class _MgmdHostInterfaceQuerierType_Type(InetAddressType):
    """Custom type mgmdHostInterfaceQuerierType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_MgmdHostInterfaceQuerierType_Type.__name__ = "InetAddressType"
_MgmdHostInterfaceQuerierType_Object = MibTableColumn
mgmdHostInterfaceQuerierType = _MgmdHostInterfaceQuerierType_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 1, 1, 2),
    _MgmdHostInterfaceQuerierType_Type()
)
mgmdHostInterfaceQuerierType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgmdHostInterfaceQuerierType.setStatus("current")


class _MgmdHostInterfaceQuerier_Type(InetAddress):
    """Custom type mgmdHostInterfaceQuerier based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_MgmdHostInterfaceQuerier_Type.__name__ = "InetAddress"
_MgmdHostInterfaceQuerier_Object = MibTableColumn
mgmdHostInterfaceQuerier = _MgmdHostInterfaceQuerier_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 1, 1, 3),
    _MgmdHostInterfaceQuerier_Type()
)
mgmdHostInterfaceQuerier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdHostInterfaceQuerier.setStatus("current")
_MgmdHostInterfaceStatus_Type = RowStatus
_MgmdHostInterfaceStatus_Object = MibTableColumn
mgmdHostInterfaceStatus = _MgmdHostInterfaceStatus_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 1, 1, 4),
    _MgmdHostInterfaceStatus_Type()
)
mgmdHostInterfaceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgmdHostInterfaceStatus.setStatus("current")


class _MgmdHostInterfaceVersion_Type(Unsigned32):
    """Custom type mgmdHostInterfaceVersion based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_MgmdHostInterfaceVersion_Type.__name__ = "Unsigned32"
_MgmdHostInterfaceVersion_Object = MibTableColumn
mgmdHostInterfaceVersion = _MgmdHostInterfaceVersion_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 1, 1, 5),
    _MgmdHostInterfaceVersion_Type()
)
mgmdHostInterfaceVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgmdHostInterfaceVersion.setStatus("current")


class _MgmdHostInterfaceVersion1QuerierTimer_Type(TimeTicks):
    """Custom type mgmdHostInterfaceVersion1QuerierTimer based on TimeTicks"""
    defaultValue = 0


_MgmdHostInterfaceVersion1QuerierTimer_Type.__name__ = "TimeTicks"
_MgmdHostInterfaceVersion1QuerierTimer_Object = MibTableColumn
mgmdHostInterfaceVersion1QuerierTimer = _MgmdHostInterfaceVersion1QuerierTimer_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 1, 1, 6),
    _MgmdHostInterfaceVersion1QuerierTimer_Type()
)
mgmdHostInterfaceVersion1QuerierTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdHostInterfaceVersion1QuerierTimer.setStatus("current")


class _MgmdHostInterfaceVersion2QuerierTimer_Type(TimeTicks):
    """Custom type mgmdHostInterfaceVersion2QuerierTimer based on TimeTicks"""
    defaultValue = 0


_MgmdHostInterfaceVersion2QuerierTimer_Type.__name__ = "TimeTicks"
_MgmdHostInterfaceVersion2QuerierTimer_Object = MibTableColumn
mgmdHostInterfaceVersion2QuerierTimer = _MgmdHostInterfaceVersion2QuerierTimer_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 1, 1, 7),
    _MgmdHostInterfaceVersion2QuerierTimer_Type()
)
mgmdHostInterfaceVersion2QuerierTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdHostInterfaceVersion2QuerierTimer.setStatus("current")


class _MgmdHostInterfaceVersion3Robustness_Type(Unsigned32):
    """Custom type mgmdHostInterfaceVersion3Robustness based on Unsigned32"""
    defaultValue = 2


_MgmdHostInterfaceVersion3Robustness_Type.__name__ = "Unsigned32"
_MgmdHostInterfaceVersion3Robustness_Object = MibTableColumn
mgmdHostInterfaceVersion3Robustness = _MgmdHostInterfaceVersion3Robustness_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 1, 1, 8),
    _MgmdHostInterfaceVersion3Robustness_Type()
)
mgmdHostInterfaceVersion3Robustness.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgmdHostInterfaceVersion3Robustness.setStatus("current")
_MgmdRouterInterfaceTable_Object = MibTable
mgmdRouterInterfaceTable = _MgmdRouterInterfaceTable_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 2)
)
if mibBuilder.loadTexts:
    mgmdRouterInterfaceTable.setStatus("current")
_MgmdRouterInterfaceEntry_Object = MibTableRow
mgmdRouterInterfaceEntry = _MgmdRouterInterfaceEntry_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 2, 1)
)
mgmdRouterInterfaceEntry.setIndexNames(
    (0, "MGMD-STD-MIB", "mgmdRouterInterfaceIfIndex"),
    (0, "MGMD-STD-MIB", "mgmdRouterInterfaceQuerierType"),
)
if mibBuilder.loadTexts:
    mgmdRouterInterfaceEntry.setStatus("current")
_MgmdRouterInterfaceIfIndex_Type = InterfaceIndex
_MgmdRouterInterfaceIfIndex_Object = MibTableColumn
mgmdRouterInterfaceIfIndex = _MgmdRouterInterfaceIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 2, 1, 1),
    _MgmdRouterInterfaceIfIndex_Type()
)
mgmdRouterInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgmdRouterInterfaceIfIndex.setStatus("current")


class _MgmdRouterInterfaceQuerierType_Type(InetAddressType):
    """Custom type mgmdRouterInterfaceQuerierType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_MgmdRouterInterfaceQuerierType_Type.__name__ = "InetAddressType"
_MgmdRouterInterfaceQuerierType_Object = MibTableColumn
mgmdRouterInterfaceQuerierType = _MgmdRouterInterfaceQuerierType_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 2, 1, 2),
    _MgmdRouterInterfaceQuerierType_Type()
)
mgmdRouterInterfaceQuerierType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgmdRouterInterfaceQuerierType.setStatus("current")


class _MgmdRouterInterfaceQuerier_Type(InetAddress):
    """Custom type mgmdRouterInterfaceQuerier based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_MgmdRouterInterfaceQuerier_Type.__name__ = "InetAddress"
_MgmdRouterInterfaceQuerier_Object = MibTableColumn
mgmdRouterInterfaceQuerier = _MgmdRouterInterfaceQuerier_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 2, 1, 3),
    _MgmdRouterInterfaceQuerier_Type()
)
mgmdRouterInterfaceQuerier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdRouterInterfaceQuerier.setStatus("current")


class _MgmdRouterInterfaceQueryInterval_Type(Unsigned32):
    """Custom type mgmdRouterInterfaceQueryInterval based on Unsigned32"""
    defaultValue = 125

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31744),
    )


_MgmdRouterInterfaceQueryInterval_Type.__name__ = "Unsigned32"
_MgmdRouterInterfaceQueryInterval_Object = MibTableColumn
mgmdRouterInterfaceQueryInterval = _MgmdRouterInterfaceQueryInterval_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 2, 1, 4),
    _MgmdRouterInterfaceQueryInterval_Type()
)
mgmdRouterInterfaceQueryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgmdRouterInterfaceQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    mgmdRouterInterfaceQueryInterval.setUnits("seconds")
_MgmdRouterInterfaceStatus_Type = RowStatus
_MgmdRouterInterfaceStatus_Object = MibTableColumn
mgmdRouterInterfaceStatus = _MgmdRouterInterfaceStatus_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 2, 1, 5),
    _MgmdRouterInterfaceStatus_Type()
)
mgmdRouterInterfaceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgmdRouterInterfaceStatus.setStatus("current")


class _MgmdRouterInterfaceVersion_Type(Unsigned32):
    """Custom type mgmdRouterInterfaceVersion based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_MgmdRouterInterfaceVersion_Type.__name__ = "Unsigned32"
_MgmdRouterInterfaceVersion_Object = MibTableColumn
mgmdRouterInterfaceVersion = _MgmdRouterInterfaceVersion_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 2, 1, 6),
    _MgmdRouterInterfaceVersion_Type()
)
mgmdRouterInterfaceVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgmdRouterInterfaceVersion.setStatus("current")


class _MgmdRouterInterfaceQueryMaxResponseTime_Type(Unsigned32):
    """Custom type mgmdRouterInterfaceQueryMaxResponseTime based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31744),
    )


_MgmdRouterInterfaceQueryMaxResponseTime_Type.__name__ = "Unsigned32"
_MgmdRouterInterfaceQueryMaxResponseTime_Object = MibTableColumn
mgmdRouterInterfaceQueryMaxResponseTime = _MgmdRouterInterfaceQueryMaxResponseTime_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 2, 1, 7),
    _MgmdRouterInterfaceQueryMaxResponseTime_Type()
)
mgmdRouterInterfaceQueryMaxResponseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgmdRouterInterfaceQueryMaxResponseTime.setStatus("current")
if mibBuilder.loadTexts:
    mgmdRouterInterfaceQueryMaxResponseTime.setUnits("tenths of seconds")
_MgmdRouterInterfaceQuerierUpTime_Type = TimeTicks
_MgmdRouterInterfaceQuerierUpTime_Object = MibTableColumn
mgmdRouterInterfaceQuerierUpTime = _MgmdRouterInterfaceQuerierUpTime_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 2, 1, 8),
    _MgmdRouterInterfaceQuerierUpTime_Type()
)
mgmdRouterInterfaceQuerierUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdRouterInterfaceQuerierUpTime.setStatus("current")
_MgmdRouterInterfaceQuerierExpiryTime_Type = TimeTicks
_MgmdRouterInterfaceQuerierExpiryTime_Object = MibTableColumn
mgmdRouterInterfaceQuerierExpiryTime = _MgmdRouterInterfaceQuerierExpiryTime_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 2, 1, 9),
    _MgmdRouterInterfaceQuerierExpiryTime_Type()
)
mgmdRouterInterfaceQuerierExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdRouterInterfaceQuerierExpiryTime.setStatus("current")
_MgmdRouterInterfaceWrongVersionQueries_Type = Counter32
_MgmdRouterInterfaceWrongVersionQueries_Object = MibTableColumn
mgmdRouterInterfaceWrongVersionQueries = _MgmdRouterInterfaceWrongVersionQueries_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 2, 1, 10),
    _MgmdRouterInterfaceWrongVersionQueries_Type()
)
mgmdRouterInterfaceWrongVersionQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdRouterInterfaceWrongVersionQueries.setStatus("current")
_MgmdRouterInterfaceJoins_Type = Counter32
_MgmdRouterInterfaceJoins_Object = MibTableColumn
mgmdRouterInterfaceJoins = _MgmdRouterInterfaceJoins_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 2, 1, 11),
    _MgmdRouterInterfaceJoins_Type()
)
mgmdRouterInterfaceJoins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdRouterInterfaceJoins.setStatus("current")


class _MgmdRouterInterfaceProxyIfIndex_Type(InterfaceIndexOrZero):
    """Custom type mgmdRouterInterfaceProxyIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_MgmdRouterInterfaceProxyIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_MgmdRouterInterfaceProxyIfIndex_Object = MibTableColumn
mgmdRouterInterfaceProxyIfIndex = _MgmdRouterInterfaceProxyIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 2, 1, 12),
    _MgmdRouterInterfaceProxyIfIndex_Type()
)
mgmdRouterInterfaceProxyIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgmdRouterInterfaceProxyIfIndex.setStatus("current")
_MgmdRouterInterfaceGroups_Type = Gauge32
_MgmdRouterInterfaceGroups_Object = MibTableColumn
mgmdRouterInterfaceGroups = _MgmdRouterInterfaceGroups_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 2, 1, 13),
    _MgmdRouterInterfaceGroups_Type()
)
mgmdRouterInterfaceGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdRouterInterfaceGroups.setStatus("current")


class _MgmdRouterInterfaceRobustness_Type(Unsigned32):
    """Custom type mgmdRouterInterfaceRobustness based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MgmdRouterInterfaceRobustness_Type.__name__ = "Unsigned32"
_MgmdRouterInterfaceRobustness_Object = MibTableColumn
mgmdRouterInterfaceRobustness = _MgmdRouterInterfaceRobustness_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 2, 1, 14),
    _MgmdRouterInterfaceRobustness_Type()
)
mgmdRouterInterfaceRobustness.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgmdRouterInterfaceRobustness.setStatus("current")


class _MgmdRouterInterfaceLastMemberQueryInterval_Type(Unsigned32):
    """Custom type mgmdRouterInterfaceLastMemberQueryInterval based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31744),
    )


_MgmdRouterInterfaceLastMemberQueryInterval_Type.__name__ = "Unsigned32"
_MgmdRouterInterfaceLastMemberQueryInterval_Object = MibTableColumn
mgmdRouterInterfaceLastMemberQueryInterval = _MgmdRouterInterfaceLastMemberQueryInterval_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 2, 1, 15),
    _MgmdRouterInterfaceLastMemberQueryInterval_Type()
)
mgmdRouterInterfaceLastMemberQueryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgmdRouterInterfaceLastMemberQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    mgmdRouterInterfaceLastMemberQueryInterval.setUnits("tenths of seconds")


class _MgmdRouterInterfaceLastMemberQueryCount_Type(Unsigned32):
    """Custom type mgmdRouterInterfaceLastMemberQueryCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MgmdRouterInterfaceLastMemberQueryCount_Type.__name__ = "Unsigned32"
_MgmdRouterInterfaceLastMemberQueryCount_Object = MibTableColumn
mgmdRouterInterfaceLastMemberQueryCount = _MgmdRouterInterfaceLastMemberQueryCount_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 2, 1, 16),
    _MgmdRouterInterfaceLastMemberQueryCount_Type()
)
mgmdRouterInterfaceLastMemberQueryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdRouterInterfaceLastMemberQueryCount.setStatus("current")


class _MgmdRouterInterfaceStartupQueryCount_Type(Unsigned32):
    """Custom type mgmdRouterInterfaceStartupQueryCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MgmdRouterInterfaceStartupQueryCount_Type.__name__ = "Unsigned32"
_MgmdRouterInterfaceStartupQueryCount_Object = MibTableColumn
mgmdRouterInterfaceStartupQueryCount = _MgmdRouterInterfaceStartupQueryCount_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 2, 1, 17),
    _MgmdRouterInterfaceStartupQueryCount_Type()
)
mgmdRouterInterfaceStartupQueryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdRouterInterfaceStartupQueryCount.setStatus("current")


class _MgmdRouterInterfaceStartupQueryInterval_Type(Unsigned32):
    """Custom type mgmdRouterInterfaceStartupQueryInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31744),
    )


_MgmdRouterInterfaceStartupQueryInterval_Type.__name__ = "Unsigned32"
_MgmdRouterInterfaceStartupQueryInterval_Object = MibTableColumn
mgmdRouterInterfaceStartupQueryInterval = _MgmdRouterInterfaceStartupQueryInterval_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 2, 1, 18),
    _MgmdRouterInterfaceStartupQueryInterval_Type()
)
mgmdRouterInterfaceStartupQueryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdRouterInterfaceStartupQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    mgmdRouterInterfaceStartupQueryInterval.setUnits("seconds")
_MgmdHostCacheTable_Object = MibTable
mgmdHostCacheTable = _MgmdHostCacheTable_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 3)
)
if mibBuilder.loadTexts:
    mgmdHostCacheTable.setStatus("current")
_MgmdHostCacheEntry_Object = MibTableRow
mgmdHostCacheEntry = _MgmdHostCacheEntry_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 3, 1)
)
mgmdHostCacheEntry.setIndexNames(
    (0, "MGMD-STD-MIB", "mgmdHostCacheAddressType"),
    (0, "MGMD-STD-MIB", "mgmdHostCacheAddress"),
    (0, "MGMD-STD-MIB", "mgmdHostCacheIfIndex"),
)
if mibBuilder.loadTexts:
    mgmdHostCacheEntry.setStatus("current")


class _MgmdHostCacheAddressType_Type(InetAddressType):
    """Custom type mgmdHostCacheAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_MgmdHostCacheAddressType_Type.__name__ = "InetAddressType"
_MgmdHostCacheAddressType_Object = MibTableColumn
mgmdHostCacheAddressType = _MgmdHostCacheAddressType_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 3, 1, 1),
    _MgmdHostCacheAddressType_Type()
)
mgmdHostCacheAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgmdHostCacheAddressType.setStatus("current")


class _MgmdHostCacheAddress_Type(InetAddress):
    """Custom type mgmdHostCacheAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_MgmdHostCacheAddress_Type.__name__ = "InetAddress"
_MgmdHostCacheAddress_Object = MibTableColumn
mgmdHostCacheAddress = _MgmdHostCacheAddress_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 3, 1, 2),
    _MgmdHostCacheAddress_Type()
)
mgmdHostCacheAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgmdHostCacheAddress.setStatus("current")
_MgmdHostCacheIfIndex_Type = InterfaceIndex
_MgmdHostCacheIfIndex_Object = MibTableColumn
mgmdHostCacheIfIndex = _MgmdHostCacheIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 3, 1, 3),
    _MgmdHostCacheIfIndex_Type()
)
mgmdHostCacheIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgmdHostCacheIfIndex.setStatus("current")
_MgmdHostCacheUpTime_Type = TimeTicks
_MgmdHostCacheUpTime_Object = MibTableColumn
mgmdHostCacheUpTime = _MgmdHostCacheUpTime_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 3, 1, 4),
    _MgmdHostCacheUpTime_Type()
)
mgmdHostCacheUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdHostCacheUpTime.setStatus("current")


class _MgmdHostCacheLastReporter_Type(InetAddress):
    """Custom type mgmdHostCacheLastReporter based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_MgmdHostCacheLastReporter_Type.__name__ = "InetAddress"
_MgmdHostCacheLastReporter_Object = MibTableColumn
mgmdHostCacheLastReporter = _MgmdHostCacheLastReporter_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 3, 1, 5),
    _MgmdHostCacheLastReporter_Type()
)
mgmdHostCacheLastReporter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdHostCacheLastReporter.setStatus("current")


class _MgmdHostCacheSourceFilterMode_Type(Integer32):
    """Custom type mgmdHostCacheSourceFilterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("include", 1),
          ("exclude", 2))
    )


_MgmdHostCacheSourceFilterMode_Type.__name__ = "Integer32"
_MgmdHostCacheSourceFilterMode_Object = MibTableColumn
mgmdHostCacheSourceFilterMode = _MgmdHostCacheSourceFilterMode_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 3, 1, 6),
    _MgmdHostCacheSourceFilterMode_Type()
)
mgmdHostCacheSourceFilterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdHostCacheSourceFilterMode.setStatus("current")
_MgmdRouterCacheTable_Object = MibTable
mgmdRouterCacheTable = _MgmdRouterCacheTable_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 4)
)
if mibBuilder.loadTexts:
    mgmdRouterCacheTable.setStatus("current")
_MgmdRouterCacheEntry_Object = MibTableRow
mgmdRouterCacheEntry = _MgmdRouterCacheEntry_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 4, 1)
)
mgmdRouterCacheEntry.setIndexNames(
    (0, "MGMD-STD-MIB", "mgmdRouterCacheAddressType"),
    (0, "MGMD-STD-MIB", "mgmdRouterCacheAddress"),
    (0, "MGMD-STD-MIB", "mgmdRouterCacheIfIndex"),
)
if mibBuilder.loadTexts:
    mgmdRouterCacheEntry.setStatus("current")


class _MgmdRouterCacheAddressType_Type(InetAddressType):
    """Custom type mgmdRouterCacheAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_MgmdRouterCacheAddressType_Type.__name__ = "InetAddressType"
_MgmdRouterCacheAddressType_Object = MibTableColumn
mgmdRouterCacheAddressType = _MgmdRouterCacheAddressType_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 4, 1, 1),
    _MgmdRouterCacheAddressType_Type()
)
mgmdRouterCacheAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgmdRouterCacheAddressType.setStatus("current")


class _MgmdRouterCacheAddress_Type(InetAddress):
    """Custom type mgmdRouterCacheAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_MgmdRouterCacheAddress_Type.__name__ = "InetAddress"
_MgmdRouterCacheAddress_Object = MibTableColumn
mgmdRouterCacheAddress = _MgmdRouterCacheAddress_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 4, 1, 2),
    _MgmdRouterCacheAddress_Type()
)
mgmdRouterCacheAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgmdRouterCacheAddress.setStatus("current")
_MgmdRouterCacheIfIndex_Type = InterfaceIndex
_MgmdRouterCacheIfIndex_Object = MibTableColumn
mgmdRouterCacheIfIndex = _MgmdRouterCacheIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 4, 1, 3),
    _MgmdRouterCacheIfIndex_Type()
)
mgmdRouterCacheIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgmdRouterCacheIfIndex.setStatus("current")


class _MgmdRouterCacheLastReporter_Type(InetAddress):
    """Custom type mgmdRouterCacheLastReporter based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_MgmdRouterCacheLastReporter_Type.__name__ = "InetAddress"
_MgmdRouterCacheLastReporter_Object = MibTableColumn
mgmdRouterCacheLastReporter = _MgmdRouterCacheLastReporter_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 4, 1, 4),
    _MgmdRouterCacheLastReporter_Type()
)
mgmdRouterCacheLastReporter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdRouterCacheLastReporter.setStatus("current")
_MgmdRouterCacheUpTime_Type = TimeTicks
_MgmdRouterCacheUpTime_Object = MibTableColumn
mgmdRouterCacheUpTime = _MgmdRouterCacheUpTime_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 4, 1, 5),
    _MgmdRouterCacheUpTime_Type()
)
mgmdRouterCacheUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdRouterCacheUpTime.setStatus("current")
_MgmdRouterCacheExpiryTime_Type = TimeTicks
_MgmdRouterCacheExpiryTime_Object = MibTableColumn
mgmdRouterCacheExpiryTime = _MgmdRouterCacheExpiryTime_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 4, 1, 6),
    _MgmdRouterCacheExpiryTime_Type()
)
mgmdRouterCacheExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdRouterCacheExpiryTime.setStatus("current")
_MgmdRouterCacheExcludeModeExpiryTimer_Type = TimeTicks
_MgmdRouterCacheExcludeModeExpiryTimer_Object = MibTableColumn
mgmdRouterCacheExcludeModeExpiryTimer = _MgmdRouterCacheExcludeModeExpiryTimer_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 4, 1, 7),
    _MgmdRouterCacheExcludeModeExpiryTimer_Type()
)
mgmdRouterCacheExcludeModeExpiryTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdRouterCacheExcludeModeExpiryTimer.setStatus("current")
_MgmdRouterCacheVersion1HostTimer_Type = TimeTicks
_MgmdRouterCacheVersion1HostTimer_Object = MibTableColumn
mgmdRouterCacheVersion1HostTimer = _MgmdRouterCacheVersion1HostTimer_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 4, 1, 8),
    _MgmdRouterCacheVersion1HostTimer_Type()
)
mgmdRouterCacheVersion1HostTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdRouterCacheVersion1HostTimer.setStatus("current")
_MgmdRouterCacheVersion2HostTimer_Type = TimeTicks
_MgmdRouterCacheVersion2HostTimer_Object = MibTableColumn
mgmdRouterCacheVersion2HostTimer = _MgmdRouterCacheVersion2HostTimer_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 4, 1, 9),
    _MgmdRouterCacheVersion2HostTimer_Type()
)
mgmdRouterCacheVersion2HostTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdRouterCacheVersion2HostTimer.setStatus("current")


class _MgmdRouterCacheSourceFilterMode_Type(Integer32):
    """Custom type mgmdRouterCacheSourceFilterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("include", 1),
          ("exclude", 2))
    )


_MgmdRouterCacheSourceFilterMode_Type.__name__ = "Integer32"
_MgmdRouterCacheSourceFilterMode_Object = MibTableColumn
mgmdRouterCacheSourceFilterMode = _MgmdRouterCacheSourceFilterMode_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 4, 1, 10),
    _MgmdRouterCacheSourceFilterMode_Type()
)
mgmdRouterCacheSourceFilterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdRouterCacheSourceFilterMode.setStatus("current")
_MgmdInverseHostCacheTable_Object = MibTable
mgmdInverseHostCacheTable = _MgmdInverseHostCacheTable_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 5)
)
if mibBuilder.loadTexts:
    mgmdInverseHostCacheTable.setStatus("current")
_MgmdInverseHostCacheEntry_Object = MibTableRow
mgmdInverseHostCacheEntry = _MgmdInverseHostCacheEntry_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 5, 1)
)
mgmdInverseHostCacheEntry.setIndexNames(
    (0, "MGMD-STD-MIB", "mgmdInverseHostCacheIfIndex"),
    (0, "MGMD-STD-MIB", "mgmdInverseHostCacheAddressType"),
    (0, "MGMD-STD-MIB", "mgmdInverseHostCacheAddress"),
)
if mibBuilder.loadTexts:
    mgmdInverseHostCacheEntry.setStatus("current")
_MgmdInverseHostCacheIfIndex_Type = InterfaceIndex
_MgmdInverseHostCacheIfIndex_Object = MibTableColumn
mgmdInverseHostCacheIfIndex = _MgmdInverseHostCacheIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 5, 1, 1),
    _MgmdInverseHostCacheIfIndex_Type()
)
mgmdInverseHostCacheIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgmdInverseHostCacheIfIndex.setStatus("current")


class _MgmdInverseHostCacheAddressType_Type(InetAddressType):
    """Custom type mgmdInverseHostCacheAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_MgmdInverseHostCacheAddressType_Type.__name__ = "InetAddressType"
_MgmdInverseHostCacheAddressType_Object = MibTableColumn
mgmdInverseHostCacheAddressType = _MgmdInverseHostCacheAddressType_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 5, 1, 2),
    _MgmdInverseHostCacheAddressType_Type()
)
mgmdInverseHostCacheAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgmdInverseHostCacheAddressType.setStatus("current")


class _MgmdInverseHostCacheAddress_Type(InetAddress):
    """Custom type mgmdInverseHostCacheAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_MgmdInverseHostCacheAddress_Type.__name__ = "InetAddress"
_MgmdInverseHostCacheAddress_Object = MibTableColumn
mgmdInverseHostCacheAddress = _MgmdInverseHostCacheAddress_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 5, 1, 3),
    _MgmdInverseHostCacheAddress_Type()
)
mgmdInverseHostCacheAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdInverseHostCacheAddress.setStatus("current")
_MgmdInverseRouterCacheTable_Object = MibTable
mgmdInverseRouterCacheTable = _MgmdInverseRouterCacheTable_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 6)
)
if mibBuilder.loadTexts:
    mgmdInverseRouterCacheTable.setStatus("current")
_MgmdInverseRouterCacheEntry_Object = MibTableRow
mgmdInverseRouterCacheEntry = _MgmdInverseRouterCacheEntry_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 6, 1)
)
mgmdInverseRouterCacheEntry.setIndexNames(
    (0, "MGMD-STD-MIB", "mgmdInverseRouterCacheIfIndex"),
    (0, "MGMD-STD-MIB", "mgmdInverseRouterCacheAddressType"),
    (0, "MGMD-STD-MIB", "mgmdInverseRouterCacheAddress"),
)
if mibBuilder.loadTexts:
    mgmdInverseRouterCacheEntry.setStatus("current")
_MgmdInverseRouterCacheIfIndex_Type = InterfaceIndex
_MgmdInverseRouterCacheIfIndex_Object = MibTableColumn
mgmdInverseRouterCacheIfIndex = _MgmdInverseRouterCacheIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 6, 1, 1),
    _MgmdInverseRouterCacheIfIndex_Type()
)
mgmdInverseRouterCacheIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgmdInverseRouterCacheIfIndex.setStatus("current")


class _MgmdInverseRouterCacheAddressType_Type(InetAddressType):
    """Custom type mgmdInverseRouterCacheAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_MgmdInverseRouterCacheAddressType_Type.__name__ = "InetAddressType"
_MgmdInverseRouterCacheAddressType_Object = MibTableColumn
mgmdInverseRouterCacheAddressType = _MgmdInverseRouterCacheAddressType_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 6, 1, 2),
    _MgmdInverseRouterCacheAddressType_Type()
)
mgmdInverseRouterCacheAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgmdInverseRouterCacheAddressType.setStatus("current")


class _MgmdInverseRouterCacheAddress_Type(InetAddress):
    """Custom type mgmdInverseRouterCacheAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_MgmdInverseRouterCacheAddress_Type.__name__ = "InetAddress"
_MgmdInverseRouterCacheAddress_Object = MibTableColumn
mgmdInverseRouterCacheAddress = _MgmdInverseRouterCacheAddress_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 6, 1, 3),
    _MgmdInverseRouterCacheAddress_Type()
)
mgmdInverseRouterCacheAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdInverseRouterCacheAddress.setStatus("current")
_MgmdHostSrcListTable_Object = MibTable
mgmdHostSrcListTable = _MgmdHostSrcListTable_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 7)
)
if mibBuilder.loadTexts:
    mgmdHostSrcListTable.setStatus("current")
_MgmdHostSrcListEntry_Object = MibTableRow
mgmdHostSrcListEntry = _MgmdHostSrcListEntry_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 7, 1)
)
mgmdHostSrcListEntry.setIndexNames(
    (0, "MGMD-STD-MIB", "mgmdHostSrcListAddressType"),
    (0, "MGMD-STD-MIB", "mgmdHostSrcListAddress"),
    (0, "MGMD-STD-MIB", "mgmdHostSrcListIfIndex"),
    (0, "MGMD-STD-MIB", "mgmdHostSrcListHostAddress"),
)
if mibBuilder.loadTexts:
    mgmdHostSrcListEntry.setStatus("current")


class _MgmdHostSrcListAddressType_Type(InetAddressType):
    """Custom type mgmdHostSrcListAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_MgmdHostSrcListAddressType_Type.__name__ = "InetAddressType"
_MgmdHostSrcListAddressType_Object = MibTableColumn
mgmdHostSrcListAddressType = _MgmdHostSrcListAddressType_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 7, 1, 1),
    _MgmdHostSrcListAddressType_Type()
)
mgmdHostSrcListAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgmdHostSrcListAddressType.setStatus("current")


class _MgmdHostSrcListAddress_Type(InetAddress):
    """Custom type mgmdHostSrcListAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_MgmdHostSrcListAddress_Type.__name__ = "InetAddress"
_MgmdHostSrcListAddress_Object = MibTableColumn
mgmdHostSrcListAddress = _MgmdHostSrcListAddress_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 7, 1, 2),
    _MgmdHostSrcListAddress_Type()
)
mgmdHostSrcListAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgmdHostSrcListAddress.setStatus("current")
_MgmdHostSrcListIfIndex_Type = InterfaceIndex
_MgmdHostSrcListIfIndex_Object = MibTableColumn
mgmdHostSrcListIfIndex = _MgmdHostSrcListIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 7, 1, 3),
    _MgmdHostSrcListIfIndex_Type()
)
mgmdHostSrcListIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgmdHostSrcListIfIndex.setStatus("current")


class _MgmdHostSrcListHostAddress_Type(InetAddress):
    """Custom type mgmdHostSrcListHostAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_MgmdHostSrcListHostAddress_Type.__name__ = "InetAddress"
_MgmdHostSrcListHostAddress_Object = MibTableColumn
mgmdHostSrcListHostAddress = _MgmdHostSrcListHostAddress_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 7, 1, 4),
    _MgmdHostSrcListHostAddress_Type()
)
mgmdHostSrcListHostAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgmdHostSrcListHostAddress.setStatus("current")
_MgmdHostSrcListExpire_Type = TimeTicks
_MgmdHostSrcListExpire_Object = MibTableColumn
mgmdHostSrcListExpire = _MgmdHostSrcListExpire_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 7, 1, 5),
    _MgmdHostSrcListExpire_Type()
)
mgmdHostSrcListExpire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdHostSrcListExpire.setStatus("current")
_MgmdRouterSrcListTable_Object = MibTable
mgmdRouterSrcListTable = _MgmdRouterSrcListTable_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 8)
)
if mibBuilder.loadTexts:
    mgmdRouterSrcListTable.setStatus("current")
_MgmdRouterSrcListEntry_Object = MibTableRow
mgmdRouterSrcListEntry = _MgmdRouterSrcListEntry_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 8, 1)
)
mgmdRouterSrcListEntry.setIndexNames(
    (0, "MGMD-STD-MIB", "mgmdRouterSrcListAddressType"),
    (0, "MGMD-STD-MIB", "mgmdRouterSrcListAddress"),
    (0, "MGMD-STD-MIB", "mgmdRouterSrcListIfIndex"),
    (0, "MGMD-STD-MIB", "mgmdRouterSrcListHostAddress"),
)
if mibBuilder.loadTexts:
    mgmdRouterSrcListEntry.setStatus("current")


class _MgmdRouterSrcListAddressType_Type(InetAddressType):
    """Custom type mgmdRouterSrcListAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_MgmdRouterSrcListAddressType_Type.__name__ = "InetAddressType"
_MgmdRouterSrcListAddressType_Object = MibTableColumn
mgmdRouterSrcListAddressType = _MgmdRouterSrcListAddressType_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 8, 1, 1),
    _MgmdRouterSrcListAddressType_Type()
)
mgmdRouterSrcListAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgmdRouterSrcListAddressType.setStatus("current")


class _MgmdRouterSrcListAddress_Type(InetAddress):
    """Custom type mgmdRouterSrcListAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_MgmdRouterSrcListAddress_Type.__name__ = "InetAddress"
_MgmdRouterSrcListAddress_Object = MibTableColumn
mgmdRouterSrcListAddress = _MgmdRouterSrcListAddress_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 8, 1, 2),
    _MgmdRouterSrcListAddress_Type()
)
mgmdRouterSrcListAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgmdRouterSrcListAddress.setStatus("current")
_MgmdRouterSrcListIfIndex_Type = InterfaceIndex
_MgmdRouterSrcListIfIndex_Object = MibTableColumn
mgmdRouterSrcListIfIndex = _MgmdRouterSrcListIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 8, 1, 3),
    _MgmdRouterSrcListIfIndex_Type()
)
mgmdRouterSrcListIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgmdRouterSrcListIfIndex.setStatus("current")


class _MgmdRouterSrcListHostAddress_Type(InetAddress):
    """Custom type mgmdRouterSrcListHostAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_MgmdRouterSrcListHostAddress_Type.__name__ = "InetAddress"
_MgmdRouterSrcListHostAddress_Object = MibTableColumn
mgmdRouterSrcListHostAddress = _MgmdRouterSrcListHostAddress_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 8, 1, 4),
    _MgmdRouterSrcListHostAddress_Type()
)
mgmdRouterSrcListHostAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgmdRouterSrcListHostAddress.setStatus("current")
_MgmdRouterSrcListExpire_Type = TimeTicks
_MgmdRouterSrcListExpire_Object = MibTableColumn
mgmdRouterSrcListExpire = _MgmdRouterSrcListExpire_Object(
    (1, 3, 6, 1, 2, 1, 185, 1, 8, 1, 5),
    _MgmdRouterSrcListExpire_Type()
)
mgmdRouterSrcListExpire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdRouterSrcListExpire.setStatus("current")
_MgmdMIBConformance_ObjectIdentity = ObjectIdentity
mgmdMIBConformance = _MgmdMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 185, 2)
)
_MgmdMIBCompliance_ObjectIdentity = ObjectIdentity
mgmdMIBCompliance = _MgmdMIBCompliance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 185, 2, 1)
)
_MgmdMIBGroups_ObjectIdentity = ObjectIdentity
mgmdMIBGroups = _MgmdMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 185, 2, 2)
)

# Managed Objects groups

mgmdHostBaseMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 185, 2, 2, 1)
)
mgmdHostBaseMIBGroup.setObjects(
      *(("MGMD-STD-MIB", "mgmdHostInterfaceStatus"),
        ("MGMD-STD-MIB", "mgmdHostInterfaceVersion"))
)
if mibBuilder.loadTexts:
    mgmdHostBaseMIBGroup.setStatus("current")

mgmdRouterBaseMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 185, 2, 2, 2)
)
mgmdRouterBaseMIBGroup.setObjects(
      *(("MGMD-STD-MIB", "mgmdRouterInterfaceStatus"),
        ("MGMD-STD-MIB", "mgmdRouterInterfaceQueryInterval"),
        ("MGMD-STD-MIB", "mgmdRouterCacheUpTime"),
        ("MGMD-STD-MIB", "mgmdRouterCacheExpiryTime"),
        ("MGMD-STD-MIB", "mgmdRouterInterfaceVersion"),
        ("MGMD-STD-MIB", "mgmdRouterInterfaceJoins"),
        ("MGMD-STD-MIB", "mgmdRouterInterfaceGroups"),
        ("MGMD-STD-MIB", "mgmdRouterCacheLastReporter"),
        ("MGMD-STD-MIB", "mgmdRouterInterfaceQuerierUpTime"),
        ("MGMD-STD-MIB", "mgmdRouterInterfaceQuerierExpiryTime"),
        ("MGMD-STD-MIB", "mgmdRouterInterfaceQuerier"),
        ("MGMD-STD-MIB", "mgmdInverseRouterCacheAddress"))
)
if mibBuilder.loadTexts:
    mgmdRouterBaseMIBGroup.setStatus("current")

mgmdV2HostMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 185, 2, 2, 3)
)
mgmdV2HostMIBGroup.setObjects(
    ("MGMD-STD-MIB", "mgmdHostInterfaceVersion1QuerierTimer")
)
if mibBuilder.loadTexts:
    mgmdV2HostMIBGroup.setStatus("current")

mgmdHostExtendedMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 185, 2, 2, 4)
)
mgmdHostExtendedMIBGroup.setObjects(
      *(("MGMD-STD-MIB", "mgmdHostCacheLastReporter"),
        ("MGMD-STD-MIB", "mgmdHostCacheUpTime"),
        ("MGMD-STD-MIB", "mgmdHostInterfaceQuerier"),
        ("MGMD-STD-MIB", "mgmdInverseHostCacheAddress"))
)
if mibBuilder.loadTexts:
    mgmdHostExtendedMIBGroup.setStatus("current")

mgmdV2RouterBaseMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 185, 2, 2, 5)
)
mgmdV2RouterBaseMIBGroup.setObjects(
      *(("MGMD-STD-MIB", "mgmdRouterInterfaceWrongVersionQueries"),
        ("MGMD-STD-MIB", "mgmdRouterInterfaceLastMemberQueryCount"),
        ("MGMD-STD-MIB", "mgmdRouterInterfaceStartupQueryCount"),
        ("MGMD-STD-MIB", "mgmdRouterInterfaceStartupQueryInterval"),
        ("MGMD-STD-MIB", "mgmdRouterCacheVersion1HostTimer"),
        ("MGMD-STD-MIB", "mgmdRouterInterfaceQueryMaxResponseTime"),
        ("MGMD-STD-MIB", "mgmdRouterInterfaceRobustness"),
        ("MGMD-STD-MIB", "mgmdRouterInterfaceLastMemberQueryInterval"))
)
if mibBuilder.loadTexts:
    mgmdV2RouterBaseMIBGroup.setStatus("current")

mgmdV2ProxyMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 185, 2, 2, 6)
)
mgmdV2ProxyMIBGroup.setObjects(
    ("MGMD-STD-MIB", "mgmdRouterInterfaceProxyIfIndex")
)
if mibBuilder.loadTexts:
    mgmdV2ProxyMIBGroup.setStatus("current")

mgmdV3HostMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 185, 2, 2, 7)
)
mgmdV3HostMIBGroup.setObjects(
      *(("MGMD-STD-MIB", "mgmdHostInterfaceVersion2QuerierTimer"),
        ("MGMD-STD-MIB", "mgmdHostCacheSourceFilterMode"),
        ("MGMD-STD-MIB", "mgmdHostInterfaceVersion3Robustness"),
        ("MGMD-STD-MIB", "mgmdHostSrcListExpire"))
)
if mibBuilder.loadTexts:
    mgmdV3HostMIBGroup.setStatus("current")

mgmdV3RouterMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 185, 2, 2, 8)
)
mgmdV3RouterMIBGroup.setObjects(
      *(("MGMD-STD-MIB", "mgmdRouterCacheSourceFilterMode"),
        ("MGMD-STD-MIB", "mgmdRouterCacheVersion2HostTimer"),
        ("MGMD-STD-MIB", "mgmdRouterCacheExcludeModeExpiryTimer"),
        ("MGMD-STD-MIB", "mgmdRouterSrcListExpire"))
)
if mibBuilder.loadTexts:
    mgmdV3RouterMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mgmdIgmpV1HostReadMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 185, 2, 1, 1)
)
mgmdIgmpV1HostReadMIBCompliance.setObjects(
    ("MGMD-STD-MIB", "mgmdHostBaseMIBGroup")
)
if mibBuilder.loadTexts:
    mgmdIgmpV1HostReadMIBCompliance.setStatus(
        "current"
    )

mgmdIgmpV1RouterReadMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 185, 2, 1, 2)
)
mgmdIgmpV1RouterReadMIBCompliance.setObjects(
    ("MGMD-STD-MIB", "mgmdRouterBaseMIBGroup")
)
if mibBuilder.loadTexts:
    mgmdIgmpV1RouterReadMIBCompliance.setStatus(
        "current"
    )

mgmdIgmpV1RouterWriteMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 185, 2, 1, 3)
)
mgmdIgmpV1RouterWriteMIBCompliance.setObjects(
    ("MGMD-STD-MIB", "mgmdRouterBaseMIBGroup")
)
if mibBuilder.loadTexts:
    mgmdIgmpV1RouterWriteMIBCompliance.setStatus(
        "current"
    )

mgmdIgmpV2MldV1HostReadMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 185, 2, 1, 4)
)
mgmdIgmpV2MldV1HostReadMIBCompliance.setObjects(
      *(("MGMD-STD-MIB", "mgmdHostBaseMIBGroup"),
        ("MGMD-STD-MIB", "mgmdV2HostMIBGroup"))
)
if mibBuilder.loadTexts:
    mgmdIgmpV2MldV1HostReadMIBCompliance.setStatus(
        "current"
    )

mgmdIgmpV2MldV1HostWriteMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 185, 2, 1, 5)
)
mgmdIgmpV2MldV1HostWriteMIBCompliance.setObjects(
      *(("MGMD-STD-MIB", "mgmdHostBaseMIBGroup"),
        ("MGMD-STD-MIB", "mgmdV2HostMIBGroup"))
)
if mibBuilder.loadTexts:
    mgmdIgmpV2MldV1HostWriteMIBCompliance.setStatus(
        "current"
    )

mgmdIgmpV2MldV1RouterReadMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 185, 2, 1, 6)
)
mgmdIgmpV2MldV1RouterReadMIBCompliance.setObjects(
      *(("MGMD-STD-MIB", "mgmdRouterBaseMIBGroup"),
        ("MGMD-STD-MIB", "mgmdV2RouterBaseMIBGroup"))
)
if mibBuilder.loadTexts:
    mgmdIgmpV2MldV1RouterReadMIBCompliance.setStatus(
        "current"
    )

mgmdIgmpV2V3MldV1V2RouterWriteMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 185, 2, 1, 7)
)
mgmdIgmpV2V3MldV1V2RouterWriteMIBCompliance.setObjects(
      *(("MGMD-STD-MIB", "mgmdRouterBaseMIBGroup"),
        ("MGMD-STD-MIB", "mgmdV2RouterBaseMIBGroup"),
        ("MGMD-STD-MIB", "mgmdV2ProxyMIBGroup"))
)
if mibBuilder.loadTexts:
    mgmdIgmpV2V3MldV1V2RouterWriteMIBCompliance.setStatus(
        "current"
    )

mgmdIgmpV3MldV2HostReadMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 185, 2, 1, 8)
)
mgmdIgmpV3MldV2HostReadMIBCompliance.setObjects(
      *(("MGMD-STD-MIB", "mgmdHostBaseMIBGroup"),
        ("MGMD-STD-MIB", "mgmdV2HostMIBGroup"),
        ("MGMD-STD-MIB", "mgmdV3HostMIBGroup"))
)
if mibBuilder.loadTexts:
    mgmdIgmpV3MldV2HostReadMIBCompliance.setStatus(
        "current"
    )

mgmdIgmpV3MldV2HostWriteMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 185, 2, 1, 9)
)
mgmdIgmpV3MldV2HostWriteMIBCompliance.setObjects(
      *(("MGMD-STD-MIB", "mgmdHostBaseMIBGroup"),
        ("MGMD-STD-MIB", "mgmdV2HostMIBGroup"),
        ("MGMD-STD-MIB", "mgmdV3HostMIBGroup"),
        ("MGMD-STD-MIB", "mgmdHostExtendedMIBGroup"))
)
if mibBuilder.loadTexts:
    mgmdIgmpV3MldV2HostWriteMIBCompliance.setStatus(
        "current"
    )

mgmdIgmpV3MldV2RouterReadMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 185, 2, 1, 10)
)
mgmdIgmpV3MldV2RouterReadMIBCompliance.setObjects(
      *(("MGMD-STD-MIB", "mgmdRouterBaseMIBGroup"),
        ("MGMD-STD-MIB", "mgmdV2RouterBaseMIBGroup"),
        ("MGMD-STD-MIB", "mgmdV3RouterMIBGroup"))
)
if mibBuilder.loadTexts:
    mgmdIgmpV3MldV2RouterReadMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MGMD-STD-MIB",
    **{"mgmdStdMIB": mgmdStdMIB,
       "mgmdMIBObjects": mgmdMIBObjects,
       "mgmdHostInterfaceTable": mgmdHostInterfaceTable,
       "mgmdHostInterfaceEntry": mgmdHostInterfaceEntry,
       "mgmdHostInterfaceIfIndex": mgmdHostInterfaceIfIndex,
       "mgmdHostInterfaceQuerierType": mgmdHostInterfaceQuerierType,
       "mgmdHostInterfaceQuerier": mgmdHostInterfaceQuerier,
       "mgmdHostInterfaceStatus": mgmdHostInterfaceStatus,
       "mgmdHostInterfaceVersion": mgmdHostInterfaceVersion,
       "mgmdHostInterfaceVersion1QuerierTimer": mgmdHostInterfaceVersion1QuerierTimer,
       "mgmdHostInterfaceVersion2QuerierTimer": mgmdHostInterfaceVersion2QuerierTimer,
       "mgmdHostInterfaceVersion3Robustness": mgmdHostInterfaceVersion3Robustness,
       "mgmdRouterInterfaceTable": mgmdRouterInterfaceTable,
       "mgmdRouterInterfaceEntry": mgmdRouterInterfaceEntry,
       "mgmdRouterInterfaceIfIndex": mgmdRouterInterfaceIfIndex,
       "mgmdRouterInterfaceQuerierType": mgmdRouterInterfaceQuerierType,
       "mgmdRouterInterfaceQuerier": mgmdRouterInterfaceQuerier,
       "mgmdRouterInterfaceQueryInterval": mgmdRouterInterfaceQueryInterval,
       "mgmdRouterInterfaceStatus": mgmdRouterInterfaceStatus,
       "mgmdRouterInterfaceVersion": mgmdRouterInterfaceVersion,
       "mgmdRouterInterfaceQueryMaxResponseTime": mgmdRouterInterfaceQueryMaxResponseTime,
       "mgmdRouterInterfaceQuerierUpTime": mgmdRouterInterfaceQuerierUpTime,
       "mgmdRouterInterfaceQuerierExpiryTime": mgmdRouterInterfaceQuerierExpiryTime,
       "mgmdRouterInterfaceWrongVersionQueries": mgmdRouterInterfaceWrongVersionQueries,
       "mgmdRouterInterfaceJoins": mgmdRouterInterfaceJoins,
       "mgmdRouterInterfaceProxyIfIndex": mgmdRouterInterfaceProxyIfIndex,
       "mgmdRouterInterfaceGroups": mgmdRouterInterfaceGroups,
       "mgmdRouterInterfaceRobustness": mgmdRouterInterfaceRobustness,
       "mgmdRouterInterfaceLastMemberQueryInterval": mgmdRouterInterfaceLastMemberQueryInterval,
       "mgmdRouterInterfaceLastMemberQueryCount": mgmdRouterInterfaceLastMemberQueryCount,
       "mgmdRouterInterfaceStartupQueryCount": mgmdRouterInterfaceStartupQueryCount,
       "mgmdRouterInterfaceStartupQueryInterval": mgmdRouterInterfaceStartupQueryInterval,
       "mgmdHostCacheTable": mgmdHostCacheTable,
       "mgmdHostCacheEntry": mgmdHostCacheEntry,
       "mgmdHostCacheAddressType": mgmdHostCacheAddressType,
       "mgmdHostCacheAddress": mgmdHostCacheAddress,
       "mgmdHostCacheIfIndex": mgmdHostCacheIfIndex,
       "mgmdHostCacheUpTime": mgmdHostCacheUpTime,
       "mgmdHostCacheLastReporter": mgmdHostCacheLastReporter,
       "mgmdHostCacheSourceFilterMode": mgmdHostCacheSourceFilterMode,
       "mgmdRouterCacheTable": mgmdRouterCacheTable,
       "mgmdRouterCacheEntry": mgmdRouterCacheEntry,
       "mgmdRouterCacheAddressType": mgmdRouterCacheAddressType,
       "mgmdRouterCacheAddress": mgmdRouterCacheAddress,
       "mgmdRouterCacheIfIndex": mgmdRouterCacheIfIndex,
       "mgmdRouterCacheLastReporter": mgmdRouterCacheLastReporter,
       "mgmdRouterCacheUpTime": mgmdRouterCacheUpTime,
       "mgmdRouterCacheExpiryTime": mgmdRouterCacheExpiryTime,
       "mgmdRouterCacheExcludeModeExpiryTimer": mgmdRouterCacheExcludeModeExpiryTimer,
       "mgmdRouterCacheVersion1HostTimer": mgmdRouterCacheVersion1HostTimer,
       "mgmdRouterCacheVersion2HostTimer": mgmdRouterCacheVersion2HostTimer,
       "mgmdRouterCacheSourceFilterMode": mgmdRouterCacheSourceFilterMode,
       "mgmdInverseHostCacheTable": mgmdInverseHostCacheTable,
       "mgmdInverseHostCacheEntry": mgmdInverseHostCacheEntry,
       "mgmdInverseHostCacheIfIndex": mgmdInverseHostCacheIfIndex,
       "mgmdInverseHostCacheAddressType": mgmdInverseHostCacheAddressType,
       "mgmdInverseHostCacheAddress": mgmdInverseHostCacheAddress,
       "mgmdInverseRouterCacheTable": mgmdInverseRouterCacheTable,
       "mgmdInverseRouterCacheEntry": mgmdInverseRouterCacheEntry,
       "mgmdInverseRouterCacheIfIndex": mgmdInverseRouterCacheIfIndex,
       "mgmdInverseRouterCacheAddressType": mgmdInverseRouterCacheAddressType,
       "mgmdInverseRouterCacheAddress": mgmdInverseRouterCacheAddress,
       "mgmdHostSrcListTable": mgmdHostSrcListTable,
       "mgmdHostSrcListEntry": mgmdHostSrcListEntry,
       "mgmdHostSrcListAddressType": mgmdHostSrcListAddressType,
       "mgmdHostSrcListAddress": mgmdHostSrcListAddress,
       "mgmdHostSrcListIfIndex": mgmdHostSrcListIfIndex,
       "mgmdHostSrcListHostAddress": mgmdHostSrcListHostAddress,
       "mgmdHostSrcListExpire": mgmdHostSrcListExpire,
       "mgmdRouterSrcListTable": mgmdRouterSrcListTable,
       "mgmdRouterSrcListEntry": mgmdRouterSrcListEntry,
       "mgmdRouterSrcListAddressType": mgmdRouterSrcListAddressType,
       "mgmdRouterSrcListAddress": mgmdRouterSrcListAddress,
       "mgmdRouterSrcListIfIndex": mgmdRouterSrcListIfIndex,
       "mgmdRouterSrcListHostAddress": mgmdRouterSrcListHostAddress,
       "mgmdRouterSrcListExpire": mgmdRouterSrcListExpire,
       "mgmdMIBConformance": mgmdMIBConformance,
       "mgmdMIBCompliance": mgmdMIBCompliance,
       "mgmdIgmpV1HostReadMIBCompliance": mgmdIgmpV1HostReadMIBCompliance,
       "mgmdIgmpV1RouterReadMIBCompliance": mgmdIgmpV1RouterReadMIBCompliance,
       "mgmdIgmpV1RouterWriteMIBCompliance": mgmdIgmpV1RouterWriteMIBCompliance,
       "mgmdIgmpV2MldV1HostReadMIBCompliance": mgmdIgmpV2MldV1HostReadMIBCompliance,
       "mgmdIgmpV2MldV1HostWriteMIBCompliance": mgmdIgmpV2MldV1HostWriteMIBCompliance,
       "mgmdIgmpV2MldV1RouterReadMIBCompliance": mgmdIgmpV2MldV1RouterReadMIBCompliance,
       "mgmdIgmpV2V3MldV1V2RouterWriteMIBCompliance": mgmdIgmpV2V3MldV1V2RouterWriteMIBCompliance,
       "mgmdIgmpV3MldV2HostReadMIBCompliance": mgmdIgmpV3MldV2HostReadMIBCompliance,
       "mgmdIgmpV3MldV2HostWriteMIBCompliance": mgmdIgmpV3MldV2HostWriteMIBCompliance,
       "mgmdIgmpV3MldV2RouterReadMIBCompliance": mgmdIgmpV3MldV2RouterReadMIBCompliance,
       "mgmdMIBGroups": mgmdMIBGroups,
       "mgmdHostBaseMIBGroup": mgmdHostBaseMIBGroup,
       "mgmdRouterBaseMIBGroup": mgmdRouterBaseMIBGroup,
       "mgmdV2HostMIBGroup": mgmdV2HostMIBGroup,
       "mgmdHostExtendedMIBGroup": mgmdHostExtendedMIBGroup,
       "mgmdV2RouterBaseMIBGroup": mgmdV2RouterBaseMIBGroup,
       "mgmdV2ProxyMIBGroup": mgmdV2ProxyMIBGroup,
       "mgmdV3HostMIBGroup": mgmdV3HostMIBGroup,
       "mgmdV3RouterMIBGroup": mgmdV3RouterMIBGroup}
)
