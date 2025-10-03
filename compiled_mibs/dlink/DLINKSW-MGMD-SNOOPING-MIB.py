# SNMP MIB module (DLINKSW-MGMD-SNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-MGMD-SNOOPING-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:37:35 2025
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

(dlinkIndustrialCommon,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlinkIndustrialCommon")

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

(VlanId,
 VlanIdOrNone) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId",
    "VlanIdOrNone")

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
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dlinkSwMgmdSnoopingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 6)
)
if mibBuilder.loadTexts:
    dlinkSwMgmdSnoopingMIB.setRevisions(
        ("2013-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class SnoopingType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("igmpSnooping", 1),
          ("mldSnooping", 2))
    )



# MIB Managed Objects in the order of their OIDs

_DMgmdSnpMIBNotifications_ObjectIdentity = ObjectIdentity
dMgmdSnpMIBNotifications = _DMgmdSnpMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 0)
)
_DMgmdSnpMIBObjects_ObjectIdentity = ObjectIdentity
dMgmdSnpMIBObjects = _DMgmdSnpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1)
)
_DMgmdSnpGlobalCtrl_ObjectIdentity = ObjectIdentity
dMgmdSnpGlobalCtrl = _DMgmdSnpGlobalCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 1)
)


class _DMgmdSnpStateGblEnabled_Type(Bits):
    """Custom type dMgmdSnpStateGblEnabled based on Bits"""
    namedValues = NamedValues(
        *(("ipv4", 0),
          ("ipv6", 1))
    )

_DMgmdSnpStateGblEnabled_Type.__name__ = "Bits"
_DMgmdSnpStateGblEnabled_Object = MibScalar
dMgmdSnpStateGblEnabled = _DMgmdSnpStateGblEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 1, 1),
    _DMgmdSnpStateGblEnabled_Type()
)
dMgmdSnpStateGblEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dMgmdSnpStateGblEnabled.setStatus("current")


class _DMgmdSnpClearAllState_Type(Integer32):
    """Custom type dMgmdSnpClearAllState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notClear", 0),
          ("igmpClear", 1),
          ("mldClear", 2))
    )


_DMgmdSnpClearAllState_Type.__name__ = "Integer32"
_DMgmdSnpClearAllState_Object = MibScalar
dMgmdSnpClearAllState = _DMgmdSnpClearAllState_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 1, 2),
    _DMgmdSnpClearAllState_Type()
)
dMgmdSnpClearAllState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dMgmdSnpClearAllState.setStatus("current")
_DMgmdSnpClearIgmpSnoopByPortIf_Type = InterfaceIndexOrZero
_DMgmdSnpClearIgmpSnoopByPortIf_Object = MibScalar
dMgmdSnpClearIgmpSnoopByPortIf = _DMgmdSnpClearIgmpSnoopByPortIf_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 1, 3),
    _DMgmdSnpClearIgmpSnoopByPortIf_Type()
)
dMgmdSnpClearIgmpSnoopByPortIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dMgmdSnpClearIgmpSnoopByPortIf.setStatus("current")
_DMgmdSnpClearMldSnoopByPortIf_Type = InterfaceIndexOrZero
_DMgmdSnpClearMldSnoopByPortIf_Object = MibScalar
dMgmdSnpClearMldSnoopByPortIf = _DMgmdSnpClearMldSnoopByPortIf_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 1, 4),
    _DMgmdSnpClearMldSnoopByPortIf_Type()
)
dMgmdSnpClearMldSnoopByPortIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dMgmdSnpClearMldSnoopByPortIf.setStatus("current")
_DMgmdSnpClearIgmpSnoopByVlanId_Type = VlanIdOrNone
_DMgmdSnpClearIgmpSnoopByVlanId_Object = MibScalar
dMgmdSnpClearIgmpSnoopByVlanId = _DMgmdSnpClearIgmpSnoopByVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 1, 5),
    _DMgmdSnpClearIgmpSnoopByVlanId_Type()
)
dMgmdSnpClearIgmpSnoopByVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dMgmdSnpClearIgmpSnoopByVlanId.setStatus("current")
_DMgmdSnpClearMldSnoopByVlanId_Type = VlanIdOrNone
_DMgmdSnpClearMldSnoopByVlanId_Object = MibScalar
dMgmdSnpClearMldSnoopByVlanId = _DMgmdSnpClearMldSnoopByVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 1, 6),
    _DMgmdSnpClearMldSnoopByVlanId_Type()
)
dMgmdSnpClearMldSnoopByVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dMgmdSnpClearMldSnoopByVlanId.setStatus("current")
_DMgmdSnpVlanIfCtrl_ObjectIdentity = ObjectIdentity
dMgmdSnpVlanIfCtrl = _DMgmdSnpVlanIfCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 2)
)
_DMgmdSnpIfTable_Object = MibTable
dMgmdSnpIfTable = _DMgmdSnpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dMgmdSnpIfTable.setStatus("current")
_DMgmdSnpIfEntry_Object = MibTableRow
dMgmdSnpIfEntry = _DMgmdSnpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 2, 1, 1)
)
dMgmdSnpIfEntry.setIndexNames(
    (0, "DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpIfVlanIfIndex"),
    (0, "DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpIfSnoopingType"),
)
if mibBuilder.loadTexts:
    dMgmdSnpIfEntry.setStatus("current")
_DMgmdSnpIfVlanIfIndex_Type = InterfaceIndex
_DMgmdSnpIfVlanIfIndex_Object = MibTableColumn
dMgmdSnpIfVlanIfIndex = _DMgmdSnpIfVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 2, 1, 1, 1),
    _DMgmdSnpIfVlanIfIndex_Type()
)
dMgmdSnpIfVlanIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dMgmdSnpIfVlanIfIndex.setStatus("current")
_DMgmdSnpIfSnoopingType_Type = SnoopingType
_DMgmdSnpIfSnoopingType_Object = MibTableColumn
dMgmdSnpIfSnoopingType = _DMgmdSnpIfSnoopingType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 2, 1, 1, 2),
    _DMgmdSnpIfSnoopingType_Type()
)
dMgmdSnpIfSnoopingType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dMgmdSnpIfSnoopingType.setStatus("current")
_DMgmdSnpIfRowStatus_Type = RowStatus
_DMgmdSnpIfRowStatus_Object = MibTableColumn
dMgmdSnpIfRowStatus = _DMgmdSnpIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 2, 1, 1, 3),
    _DMgmdSnpIfRowStatus_Type()
)
dMgmdSnpIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dMgmdSnpIfRowStatus.setStatus("current")


class _DMgmdSnpIfStateEnabled_Type(TruthValue):
    """Custom type dMgmdSnpIfStateEnabled based on TruthValue"""
    defaultValue = 2


_DMgmdSnpIfStateEnabled_Type.__name__ = "TruthValue"
_DMgmdSnpIfStateEnabled_Object = MibTableColumn
dMgmdSnpIfStateEnabled = _DMgmdSnpIfStateEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 2, 1, 1, 4),
    _DMgmdSnpIfStateEnabled_Type()
)
dMgmdSnpIfStateEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dMgmdSnpIfStateEnabled.setStatus("current")


class _DMgmdSnpIfQuerierStateEnabled_Type(TruthValue):
    """Custom type dMgmdSnpIfQuerierStateEnabled based on TruthValue"""
    defaultValue = 2


_DMgmdSnpIfQuerierStateEnabled_Type.__name__ = "TruthValue"
_DMgmdSnpIfQuerierStateEnabled_Object = MibTableColumn
dMgmdSnpIfQuerierStateEnabled = _DMgmdSnpIfQuerierStateEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 2, 1, 1, 5),
    _DMgmdSnpIfQuerierStateEnabled_Type()
)
dMgmdSnpIfQuerierStateEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dMgmdSnpIfQuerierStateEnabled.setStatus("current")


class _DMgmdSnpIfQuerierRouter_Type(Integer32):
    """Custom type dMgmdSnpIfQuerierRouter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("absence", 1),
          ("active", 2),
          ("nonActive", 3))
    )


_DMgmdSnpIfQuerierRouter_Type.__name__ = "Integer32"
_DMgmdSnpIfQuerierRouter_Object = MibTableColumn
dMgmdSnpIfQuerierRouter = _DMgmdSnpIfQuerierRouter_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 2, 1, 1, 6),
    _DMgmdSnpIfQuerierRouter_Type()
)
dMgmdSnpIfQuerierRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dMgmdSnpIfQuerierRouter.setStatus("current")


class _DMgmdSnpIfFastLeaveEnabled_Type(TruthValue):
    """Custom type dMgmdSnpIfFastLeaveEnabled based on TruthValue"""
    defaultValue = 2


_DMgmdSnpIfFastLeaveEnabled_Type.__name__ = "TruthValue"
_DMgmdSnpIfFastLeaveEnabled_Object = MibTableColumn
dMgmdSnpIfFastLeaveEnabled = _DMgmdSnpIfFastLeaveEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 2, 1, 1, 7),
    _DMgmdSnpIfFastLeaveEnabled_Type()
)
dMgmdSnpIfFastLeaveEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dMgmdSnpIfFastLeaveEnabled.setStatus("current")


class _DMgmdSnpIfFastLeaveHostBased_Type(TruthValue):
    """Custom type dMgmdSnpIfFastLeaveHostBased based on TruthValue"""
    defaultValue = 2


_DMgmdSnpIfFastLeaveHostBased_Type.__name__ = "TruthValue"
_DMgmdSnpIfFastLeaveHostBased_Object = MibTableColumn
dMgmdSnpIfFastLeaveHostBased = _DMgmdSnpIfFastLeaveHostBased_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 2, 1, 1, 8),
    _DMgmdSnpIfFastLeaveHostBased_Type()
)
dMgmdSnpIfFastLeaveHostBased.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dMgmdSnpIfFastLeaveHostBased.setStatus("current")


class _DMgmdSnpIfMinimumVersion_Type(Integer32):
    """Custom type dMgmdSnpIfMinimumVersion based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("version2", 2),
          ("version3", 3))
    )


_DMgmdSnpIfMinimumVersion_Type.__name__ = "Integer32"
_DMgmdSnpIfMinimumVersion_Object = MibTableColumn
dMgmdSnpIfMinimumVersion = _DMgmdSnpIfMinimumVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 2, 1, 1, 9),
    _DMgmdSnpIfMinimumVersion_Type()
)
dMgmdSnpIfMinimumVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dMgmdSnpIfMinimumVersion.setStatus("current")


class _DMgmdSnpIfExplicitTrackEnabled_Type(TruthValue):
    """Custom type dMgmdSnpIfExplicitTrackEnabled based on TruthValue"""
    defaultValue = 2


_DMgmdSnpIfExplicitTrackEnabled_Type.__name__ = "TruthValue"
_DMgmdSnpIfExplicitTrackEnabled_Object = MibTableColumn
dMgmdSnpIfExplicitTrackEnabled = _DMgmdSnpIfExplicitTrackEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 2, 1, 1, 10),
    _DMgmdSnpIfExplicitTrackEnabled_Type()
)
dMgmdSnpIfExplicitTrackEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dMgmdSnpIfExplicitTrackEnabled.setStatus("current")


class _DMgmdSnpIfReportSuppresEnabled_Type(TruthValue):
    """Custom type dMgmdSnpIfReportSuppresEnabled based on TruthValue"""
    defaultValue = 2


_DMgmdSnpIfReportSuppresEnabled_Type.__name__ = "TruthValue"
_DMgmdSnpIfReportSuppresEnabled_Object = MibTableColumn
dMgmdSnpIfReportSuppresEnabled = _DMgmdSnpIfReportSuppresEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 2, 1, 1, 11),
    _DMgmdSnpIfReportSuppresEnabled_Type()
)
dMgmdSnpIfReportSuppresEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dMgmdSnpIfReportSuppresEnabled.setStatus("current")


class _DMgmdSnpIfProxyReportingEnabled_Type(TruthValue):
    """Custom type dMgmdSnpIfProxyReportingEnabled based on TruthValue"""
    defaultValue = 2


_DMgmdSnpIfProxyReportingEnabled_Type.__name__ = "TruthValue"
_DMgmdSnpIfProxyReportingEnabled_Object = MibTableColumn
dMgmdSnpIfProxyReportingEnabled = _DMgmdSnpIfProxyReportingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 2, 1, 1, 12),
    _DMgmdSnpIfProxyReportingEnabled_Type()
)
dMgmdSnpIfProxyReportingEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dMgmdSnpIfProxyReportingEnabled.setStatus("current")


class _DMgmdSnpIfAutoLearnMrouter_Type(TruthValue):
    """Custom type dMgmdSnpIfAutoLearnMrouter based on TruthValue"""
    defaultValue = 2


_DMgmdSnpIfAutoLearnMrouter_Type.__name__ = "TruthValue"
_DMgmdSnpIfAutoLearnMrouter_Object = MibTableColumn
dMgmdSnpIfAutoLearnMrouter = _DMgmdSnpIfAutoLearnMrouter_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 2, 1, 1, 13),
    _DMgmdSnpIfAutoLearnMrouter_Type()
)
dMgmdSnpIfAutoLearnMrouter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dMgmdSnpIfAutoLearnMrouter.setStatus("current")


class _DMgmdSnpIfProxyReportSrcAddrType_Type(InetAddressType):
    """Custom type dMgmdSnpIfProxyReportSrcAddrType based on InetAddressType"""
    defaultValue = 1


_DMgmdSnpIfProxyReportSrcAddrType_Type.__name__ = "InetAddressType"
_DMgmdSnpIfProxyReportSrcAddrType_Object = MibTableColumn
dMgmdSnpIfProxyReportSrcAddrType = _DMgmdSnpIfProxyReportSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 2, 1, 1, 14),
    _DMgmdSnpIfProxyReportSrcAddrType_Type()
)
dMgmdSnpIfProxyReportSrcAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dMgmdSnpIfProxyReportSrcAddrType.setStatus("current")


class _DMgmdSnpIfProxyReportSrcAddr_Type(InetAddress):
    """Custom type dMgmdSnpIfProxyReportSrcAddr based on InetAddress"""
    defaultHexValue = "00000000"


_DMgmdSnpIfProxyReportSrcAddr_Type.__name__ = "InetAddress"
_DMgmdSnpIfProxyReportSrcAddr_Object = MibTableColumn
dMgmdSnpIfProxyReportSrcAddr = _DMgmdSnpIfProxyReportSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 2, 1, 1, 15),
    _DMgmdSnpIfProxyReportSrcAddr_Type()
)
dMgmdSnpIfProxyReportSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dMgmdSnpIfProxyReportSrcAddr.setStatus("current")


class _DMgmdSnpIfQueryInterval_Type(Unsigned32):
    """Custom type dMgmdSnpIfQueryInterval based on Unsigned32"""
    defaultValue = 125

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31744),
    )


_DMgmdSnpIfQueryInterval_Type.__name__ = "Unsigned32"
_DMgmdSnpIfQueryInterval_Object = MibTableColumn
dMgmdSnpIfQueryInterval = _DMgmdSnpIfQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 2, 1, 1, 16),
    _DMgmdSnpIfQueryInterval_Type()
)
dMgmdSnpIfQueryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dMgmdSnpIfQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    dMgmdSnpIfQueryInterval.setUnits("seconds")
_DMgmdSnpIfQueryMaxResponseTime_Type = Unsigned32
_DMgmdSnpIfQueryMaxResponseTime_Object = MibTableColumn
dMgmdSnpIfQueryMaxResponseTime = _DMgmdSnpIfQueryMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 2, 1, 1, 17),
    _DMgmdSnpIfQueryMaxResponseTime_Type()
)
dMgmdSnpIfQueryMaxResponseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dMgmdSnpIfQueryMaxResponseTime.setStatus("current")
if mibBuilder.loadTexts:
    dMgmdSnpIfQueryMaxResponseTime.setUnits("seconds")


class _DMgmdSnpIfQueryVersion_Type(Unsigned32):
    """Custom type dMgmdSnpIfQueryVersion based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_DMgmdSnpIfQueryVersion_Type.__name__ = "Unsigned32"
_DMgmdSnpIfQueryVersion_Object = MibTableColumn
dMgmdSnpIfQueryVersion = _DMgmdSnpIfQueryVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 2, 1, 1, 18),
    _DMgmdSnpIfQueryVersion_Type()
)
dMgmdSnpIfQueryVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dMgmdSnpIfQueryVersion.setStatus("current")


class _DMgmdSnpIfRobustness_Type(Unsigned32):
    """Custom type dMgmdSnpIfRobustness based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_DMgmdSnpIfRobustness_Type.__name__ = "Unsigned32"
_DMgmdSnpIfRobustness_Object = MibTableColumn
dMgmdSnpIfRobustness = _DMgmdSnpIfRobustness_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 2, 1, 1, 19),
    _DMgmdSnpIfRobustness_Type()
)
dMgmdSnpIfRobustness.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dMgmdSnpIfRobustness.setStatus("current")


class _DMgmdSnpIfLastMemberQueryInterval_Type(Unsigned32):
    """Custom type dMgmdSnpIfLastMemberQueryInterval based on Unsigned32"""
    defaultValue = 1


_DMgmdSnpIfLastMemberQueryInterval_Type.__name__ = "Unsigned32"
_DMgmdSnpIfLastMemberQueryInterval_Object = MibTableColumn
dMgmdSnpIfLastMemberQueryInterval = _DMgmdSnpIfLastMemberQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 2, 1, 1, 20),
    _DMgmdSnpIfLastMemberQueryInterval_Type()
)
dMgmdSnpIfLastMemberQueryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dMgmdSnpIfLastMemberQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    dMgmdSnpIfLastMemberQueryInterval.setUnits("seconds")
_DMgmdSnpIfSuppressionTime_Type = Unsigned32
_DMgmdSnpIfSuppressionTime_Object = MibTableColumn
dMgmdSnpIfSuppressionTime = _DMgmdSnpIfSuppressionTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 2, 1, 1, 21),
    _DMgmdSnpIfSuppressionTime_Type()
)
dMgmdSnpIfSuppressionTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dMgmdSnpIfSuppressionTime.setStatus("current")
if mibBuilder.loadTexts:
    dMgmdSnpIfSuppressionTime.setUnits("seconds")
_DMgmdSnpPortIfCtrl_ObjectIdentity = ObjectIdentity
dMgmdSnpPortIfCtrl = _DMgmdSnpPortIfCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 3)
)
_DMgmdSnpMrouterTable_Object = MibTable
dMgmdSnpMrouterTable = _DMgmdSnpMrouterTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dMgmdSnpMrouterTable.setStatus("current")
_DMgmdSnpMrouterEntry_Object = MibTableRow
dMgmdSnpMrouterEntry = _DMgmdSnpMrouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 3, 1, 1)
)
dMgmdSnpMrouterEntry.setIndexNames(
    (0, "DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpMrouterIfIndex"),
    (0, "DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpMrouterVlanIfIndex"),
    (0, "DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpMrouterQuerierType"),
)
if mibBuilder.loadTexts:
    dMgmdSnpMrouterEntry.setStatus("current")
_DMgmdSnpMrouterIfIndex_Type = InterfaceIndex
_DMgmdSnpMrouterIfIndex_Object = MibTableColumn
dMgmdSnpMrouterIfIndex = _DMgmdSnpMrouterIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 3, 1, 1, 1),
    _DMgmdSnpMrouterIfIndex_Type()
)
dMgmdSnpMrouterIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dMgmdSnpMrouterIfIndex.setStatus("current")
_DMgmdSnpMrouterVlanIfIndex_Type = InterfaceIndex
_DMgmdSnpMrouterVlanIfIndex_Object = MibTableColumn
dMgmdSnpMrouterVlanIfIndex = _DMgmdSnpMrouterVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 3, 1, 1, 2),
    _DMgmdSnpMrouterVlanIfIndex_Type()
)
dMgmdSnpMrouterVlanIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dMgmdSnpMrouterVlanIfIndex.setStatus("current")
_DMgmdSnpMrouterQuerierType_Type = SnoopingType
_DMgmdSnpMrouterQuerierType_Object = MibTableColumn
dMgmdSnpMrouterQuerierType = _DMgmdSnpMrouterQuerierType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 3, 1, 1, 3),
    _DMgmdSnpMrouterQuerierType_Type()
)
dMgmdSnpMrouterQuerierType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dMgmdSnpMrouterQuerierType.setStatus("current")
_DMgmdSnpMrouterStatus_Type = RowStatus
_DMgmdSnpMrouterStatus_Object = MibTableColumn
dMgmdSnpMrouterStatus = _DMgmdSnpMrouterStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 3, 1, 1, 4),
    _DMgmdSnpMrouterStatus_Type()
)
dMgmdSnpMrouterStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dMgmdSnpMrouterStatus.setStatus("current")


class _DMgmdSnpMrouterAdminState_Type(Integer32):
    """Custom type dMgmdSnpMrouterAdminState based on Integer32"""
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
        *(("none", 1),
          ("designated", 2),
          ("forbidden", 3))
    )


_DMgmdSnpMrouterAdminState_Type.__name__ = "Integer32"
_DMgmdSnpMrouterAdminState_Object = MibTableColumn
dMgmdSnpMrouterAdminState = _DMgmdSnpMrouterAdminState_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 3, 1, 1, 5),
    _DMgmdSnpMrouterAdminState_Type()
)
dMgmdSnpMrouterAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dMgmdSnpMrouterAdminState.setStatus("current")
_DMgmdSnpMrouterDynamicMrouter_Type = TruthValue
_DMgmdSnpMrouterDynamicMrouter_Object = MibTableColumn
dMgmdSnpMrouterDynamicMrouter = _DMgmdSnpMrouterDynamicMrouter_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 3, 1, 1, 6),
    _DMgmdSnpMrouterDynamicMrouter_Type()
)
dMgmdSnpMrouterDynamicMrouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dMgmdSnpMrouterDynamicMrouter.setStatus("current")
_DMgmdSnpIfLimitTable_Object = MibTable
dMgmdSnpIfLimitTable = _DMgmdSnpIfLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 3, 2)
)
if mibBuilder.loadTexts:
    dMgmdSnpIfLimitTable.setStatus("current")
_DMgmdSnpIfLimitEntry_Object = MibTableRow
dMgmdSnpIfLimitEntry = _DMgmdSnpIfLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 3, 2, 1)
)
dMgmdSnpIfLimitEntry.setIndexNames(
    (0, "DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpIfLimitIfIndex"),
    (0, "DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpIfLimitVlanId"),
    (0, "DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpIfLimitSnoopingType"),
)
if mibBuilder.loadTexts:
    dMgmdSnpIfLimitEntry.setStatus("current")
_DMgmdSnpIfLimitIfIndex_Type = InterfaceIndex
_DMgmdSnpIfLimitIfIndex_Object = MibTableColumn
dMgmdSnpIfLimitIfIndex = _DMgmdSnpIfLimitIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 3, 2, 1, 1),
    _DMgmdSnpIfLimitIfIndex_Type()
)
dMgmdSnpIfLimitIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dMgmdSnpIfLimitIfIndex.setStatus("current")
_DMgmdSnpIfLimitVlanId_Type = VlanIdOrNone
_DMgmdSnpIfLimitVlanId_Object = MibTableColumn
dMgmdSnpIfLimitVlanId = _DMgmdSnpIfLimitVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 3, 2, 1, 2),
    _DMgmdSnpIfLimitVlanId_Type()
)
dMgmdSnpIfLimitVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dMgmdSnpIfLimitVlanId.setStatus("current")
_DMgmdSnpIfLimitSnoopingType_Type = SnoopingType
_DMgmdSnpIfLimitSnoopingType_Object = MibTableColumn
dMgmdSnpIfLimitSnoopingType = _DMgmdSnpIfLimitSnoopingType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 3, 2, 1, 3),
    _DMgmdSnpIfLimitSnoopingType_Type()
)
dMgmdSnpIfLimitSnoopingType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dMgmdSnpIfLimitSnoopingType.setStatus("current")
_DMgmdSnpIfLimitRowStatus_Type = RowStatus
_DMgmdSnpIfLimitRowStatus_Object = MibTableColumn
dMgmdSnpIfLimitRowStatus = _DMgmdSnpIfLimitRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 3, 2, 1, 4),
    _DMgmdSnpIfLimitRowStatus_Type()
)
dMgmdSnpIfLimitRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dMgmdSnpIfLimitRowStatus.setStatus("current")


class _DMgmdSnpIfLimitExceptAccLstName_Type(DisplayString):
    """Custom type dMgmdSnpIfLimitExceptAccLstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DMgmdSnpIfLimitExceptAccLstName_Type.__name__ = "DisplayString"
_DMgmdSnpIfLimitExceptAccLstName_Object = MibTableColumn
dMgmdSnpIfLimitExceptAccLstName = _DMgmdSnpIfLimitExceptAccLstName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 3, 2, 1, 5),
    _DMgmdSnpIfLimitExceptAccLstName_Type()
)
dMgmdSnpIfLimitExceptAccLstName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dMgmdSnpIfLimitExceptAccLstName.setStatus("current")


class _DMgmdSnpIfLimitValue_Type(Unsigned32):
    """Custom type dMgmdSnpIfLimitValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_DMgmdSnpIfLimitValue_Type.__name__ = "Unsigned32"
_DMgmdSnpIfLimitValue_Object = MibTableColumn
dMgmdSnpIfLimitValue = _DMgmdSnpIfLimitValue_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 3, 2, 1, 6),
    _DMgmdSnpIfLimitValue_Type()
)
dMgmdSnpIfLimitValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dMgmdSnpIfLimitValue.setStatus("current")
_DMgmdSnpAccGrpTable_Object = MibTable
dMgmdSnpAccGrpTable = _DMgmdSnpAccGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 3, 3)
)
if mibBuilder.loadTexts:
    dMgmdSnpAccGrpTable.setStatus("current")
_DMgmdSnpAccGrpEntry_Object = MibTableRow
dMgmdSnpAccGrpEntry = _DMgmdSnpAccGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 3, 3, 1)
)
dMgmdSnpAccGrpEntry.setIndexNames(
    (0, "DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpAccGrpIfIndex"),
    (0, "DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpAccGrpVlanId"),
    (0, "DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpAccGrpSnoopingType"),
)
if mibBuilder.loadTexts:
    dMgmdSnpAccGrpEntry.setStatus("current")
_DMgmdSnpAccGrpIfIndex_Type = InterfaceIndex
_DMgmdSnpAccGrpIfIndex_Object = MibTableColumn
dMgmdSnpAccGrpIfIndex = _DMgmdSnpAccGrpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 3, 3, 1, 1),
    _DMgmdSnpAccGrpIfIndex_Type()
)
dMgmdSnpAccGrpIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dMgmdSnpAccGrpIfIndex.setStatus("current")
_DMgmdSnpAccGrpVlanId_Type = VlanIdOrNone
_DMgmdSnpAccGrpVlanId_Object = MibTableColumn
dMgmdSnpAccGrpVlanId = _DMgmdSnpAccGrpVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 3, 3, 1, 2),
    _DMgmdSnpAccGrpVlanId_Type()
)
dMgmdSnpAccGrpVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dMgmdSnpAccGrpVlanId.setStatus("current")
_DMgmdSnpAccGrpSnoopingType_Type = SnoopingType
_DMgmdSnpAccGrpSnoopingType_Object = MibTableColumn
dMgmdSnpAccGrpSnoopingType = _DMgmdSnpAccGrpSnoopingType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 3, 3, 1, 3),
    _DMgmdSnpAccGrpSnoopingType_Type()
)
dMgmdSnpAccGrpSnoopingType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dMgmdSnpAccGrpSnoopingType.setStatus("current")
_DMgmdSnpAccGrpStatus_Type = RowStatus
_DMgmdSnpAccGrpStatus_Object = MibTableColumn
dMgmdSnpAccGrpStatus = _DMgmdSnpAccGrpStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 3, 3, 1, 4),
    _DMgmdSnpAccGrpStatus_Type()
)
dMgmdSnpAccGrpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dMgmdSnpAccGrpStatus.setStatus("current")


class _DMgmdSnpAccessGroupName_Type(DisplayString):
    """Custom type dMgmdSnpAccessGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DMgmdSnpAccessGroupName_Type.__name__ = "DisplayString"
_DMgmdSnpAccessGroupName_Object = MibTableColumn
dMgmdSnpAccessGroupName = _DMgmdSnpAccessGroupName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 3, 3, 1, 5),
    _DMgmdSnpAccessGroupName_Type()
)
dMgmdSnpAccessGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dMgmdSnpAccessGroupName.setStatus("current")
_DMgmdSnpGroupCtrl_ObjectIdentity = ObjectIdentity
dMgmdSnpGroupCtrl = _DMgmdSnpGroupCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 4)
)
_DMgmdSnpGroupTable_Object = MibTable
dMgmdSnpGroupTable = _DMgmdSnpGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 4, 1)
)
if mibBuilder.loadTexts:
    dMgmdSnpGroupTable.setStatus("current")
_DMgmdSnpGroupEntry_Object = MibTableRow
dMgmdSnpGroupEntry = _DMgmdSnpGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 4, 1, 1)
)
dMgmdSnpGroupEntry.setIndexNames(
    (0, "DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpGroupVlanIfIndex"),
    (0, "DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpGroupAddressType"),
    (0, "DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpGroupAddress"),
    (0, "DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpGroupIfIndex"),
)
if mibBuilder.loadTexts:
    dMgmdSnpGroupEntry.setStatus("current")
_DMgmdSnpGroupVlanIfIndex_Type = InterfaceIndex
_DMgmdSnpGroupVlanIfIndex_Object = MibTableColumn
dMgmdSnpGroupVlanIfIndex = _DMgmdSnpGroupVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 4, 1, 1, 1),
    _DMgmdSnpGroupVlanIfIndex_Type()
)
dMgmdSnpGroupVlanIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dMgmdSnpGroupVlanIfIndex.setStatus("current")
_DMgmdSnpGroupAddressType_Type = InetAddressType
_DMgmdSnpGroupAddressType_Object = MibTableColumn
dMgmdSnpGroupAddressType = _DMgmdSnpGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 4, 1, 1, 2),
    _DMgmdSnpGroupAddressType_Type()
)
dMgmdSnpGroupAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dMgmdSnpGroupAddressType.setStatus("current")
_DMgmdSnpGroupAddress_Type = InetAddress
_DMgmdSnpGroupAddress_Object = MibTableColumn
dMgmdSnpGroupAddress = _DMgmdSnpGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 4, 1, 1, 3),
    _DMgmdSnpGroupAddress_Type()
)
dMgmdSnpGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dMgmdSnpGroupAddress.setStatus("current")
_DMgmdSnpGroupIfIndex_Type = InterfaceIndex
_DMgmdSnpGroupIfIndex_Object = MibTableColumn
dMgmdSnpGroupIfIndex = _DMgmdSnpGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 4, 1, 1, 4),
    _DMgmdSnpGroupIfIndex_Type()
)
dMgmdSnpGroupIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dMgmdSnpGroupIfIndex.setStatus("current")


class _DMgmdSnpGroupVersion_Type(Integer32):
    """Custom type dMgmdSnpGroupVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("version1", 1),
          ("version2", 2),
          ("version3", 3))
    )


_DMgmdSnpGroupVersion_Type.__name__ = "Integer32"
_DMgmdSnpGroupVersion_Object = MibTableColumn
dMgmdSnpGroupVersion = _DMgmdSnpGroupVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 4, 1, 1, 5),
    _DMgmdSnpGroupVersion_Type()
)
dMgmdSnpGroupVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dMgmdSnpGroupVersion.setStatus("current")
_DMgmdSnpGroupUpTime_Type = TimeTicks
_DMgmdSnpGroupUpTime_Object = MibTableColumn
dMgmdSnpGroupUpTime = _DMgmdSnpGroupUpTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 4, 1, 1, 6),
    _DMgmdSnpGroupUpTime_Type()
)
dMgmdSnpGroupUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dMgmdSnpGroupUpTime.setStatus("current")
_DMgmdSnpGroupExpire_Type = TimeTicks
_DMgmdSnpGroupExpire_Object = MibTableColumn
dMgmdSnpGroupExpire = _DMgmdSnpGroupExpire_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 4, 1, 1, 7),
    _DMgmdSnpGroupExpire_Type()
)
dMgmdSnpGroupExpire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dMgmdSnpGroupExpire.setStatus("current")


class _DMgmdSnpGroupMode_Type(Integer32):
    """Custom type dMgmdSnpGroupMode based on Integer32"""
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


_DMgmdSnpGroupMode_Type.__name__ = "Integer32"
_DMgmdSnpGroupMode_Object = MibTableColumn
dMgmdSnpGroupMode = _DMgmdSnpGroupMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 4, 1, 1, 8),
    _DMgmdSnpGroupMode_Type()
)
dMgmdSnpGroupMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dMgmdSnpGroupMode.setStatus("current")


class _DMgmdSnpGroupLastReportAddrType_Type(InetAddressType):
    """Custom type dMgmdSnpGroupLastReportAddrType based on InetAddressType"""
    defaultValue = 1


_DMgmdSnpGroupLastReportAddrType_Type.__name__ = "InetAddressType"
_DMgmdSnpGroupLastReportAddrType_Object = MibTableColumn
dMgmdSnpGroupLastReportAddrType = _DMgmdSnpGroupLastReportAddrType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 4, 1, 1, 9),
    _DMgmdSnpGroupLastReportAddrType_Type()
)
dMgmdSnpGroupLastReportAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dMgmdSnpGroupLastReportAddrType.setStatus("current")
_DMgmdSnpGroupLastReportAddr_Type = InetAddress
_DMgmdSnpGroupLastReportAddr_Object = MibTableColumn
dMgmdSnpGroupLastReportAddr = _DMgmdSnpGroupLastReportAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 4, 1, 1, 10),
    _DMgmdSnpGroupLastReportAddr_Type()
)
dMgmdSnpGroupLastReportAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dMgmdSnpGroupLastReportAddr.setStatus("current")
_DMgmdSnpGroupSrcTable_Object = MibTable
dMgmdSnpGroupSrcTable = _DMgmdSnpGroupSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 4, 2)
)
if mibBuilder.loadTexts:
    dMgmdSnpGroupSrcTable.setStatus("current")
_DMgmdSnpGroupSrcEntry_Object = MibTableRow
dMgmdSnpGroupSrcEntry = _DMgmdSnpGroupSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 4, 2, 1)
)
dMgmdSnpGroupSrcEntry.setIndexNames(
    (0, "DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpGroupVlanIfIndex"),
    (0, "DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpGroupAddressType"),
    (0, "DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpGroupAddress"),
    (0, "DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpGroupSrcAddrType"),
    (0, "DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpGroupSrcAddress"),
    (0, "DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpGroupSrcIfIndex"),
)
if mibBuilder.loadTexts:
    dMgmdSnpGroupSrcEntry.setStatus("current")
_DMgmdSnpGroupSrcAddrType_Type = InetAddressType
_DMgmdSnpGroupSrcAddrType_Object = MibTableColumn
dMgmdSnpGroupSrcAddrType = _DMgmdSnpGroupSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 4, 2, 1, 1),
    _DMgmdSnpGroupSrcAddrType_Type()
)
dMgmdSnpGroupSrcAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dMgmdSnpGroupSrcAddrType.setStatus("current")
_DMgmdSnpGroupSrcAddress_Type = InetAddress
_DMgmdSnpGroupSrcAddress_Object = MibTableColumn
dMgmdSnpGroupSrcAddress = _DMgmdSnpGroupSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 4, 2, 1, 2),
    _DMgmdSnpGroupSrcAddress_Type()
)
dMgmdSnpGroupSrcAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dMgmdSnpGroupSrcAddress.setStatus("current")
_DMgmdSnpGroupSrcIfIndex_Type = InterfaceIndex
_DMgmdSnpGroupSrcIfIndex_Object = MibTableColumn
dMgmdSnpGroupSrcIfIndex = _DMgmdSnpGroupSrcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 4, 2, 1, 3),
    _DMgmdSnpGroupSrcIfIndex_Type()
)
dMgmdSnpGroupSrcIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dMgmdSnpGroupSrcIfIndex.setStatus("current")
_DMgmdSnpGroupSrcUpTime_Type = TimeTicks
_DMgmdSnpGroupSrcUpTime_Object = MibTableColumn
dMgmdSnpGroupSrcUpTime = _DMgmdSnpGroupSrcUpTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 4, 2, 1, 4),
    _DMgmdSnpGroupSrcUpTime_Type()
)
dMgmdSnpGroupSrcUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dMgmdSnpGroupSrcUpTime.setStatus("current")
_DMgmdSnpGroupSrcExpire_Type = TimeTicks
_DMgmdSnpGroupSrcExpire_Object = MibTableColumn
dMgmdSnpGroupSrcExpire = _DMgmdSnpGroupSrcExpire_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 4, 2, 1, 5),
    _DMgmdSnpGroupSrcExpire_Type()
)
dMgmdSnpGroupSrcExpire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dMgmdSnpGroupSrcExpire.setStatus("current")


class _DMgmdSnpGroupSrcForward_Type(Integer32):
    """Custom type dMgmdSnpGroupSrcForward based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_DMgmdSnpGroupSrcForward_Type.__name__ = "Integer32"
_DMgmdSnpGroupSrcForward_Object = MibTableColumn
dMgmdSnpGroupSrcForward = _DMgmdSnpGroupSrcForward_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 4, 2, 1, 6),
    _DMgmdSnpGroupSrcForward_Type()
)
dMgmdSnpGroupSrcForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dMgmdSnpGroupSrcForward.setStatus("current")
_DMgmdSnpStaticGrpTable_Object = MibTable
dMgmdSnpStaticGrpTable = _DMgmdSnpStaticGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 4, 3)
)
if mibBuilder.loadTexts:
    dMgmdSnpStaticGrpTable.setStatus("current")
_DMgmdSnpStaticGrpEntry_Object = MibTableRow
dMgmdSnpStaticGrpEntry = _DMgmdSnpStaticGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 4, 3, 1)
)
dMgmdSnpStaticGrpEntry.setIndexNames(
    (0, "DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpStaticGrpVlanIfIndex"),
    (0, "DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpStaticGrpAddressType"),
    (0, "DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpStaticGrpAddress"),
    (0, "DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpStaticGrpIfIndex"),
)
if mibBuilder.loadTexts:
    dMgmdSnpStaticGrpEntry.setStatus("current")
_DMgmdSnpStaticGrpVlanIfIndex_Type = InterfaceIndex
_DMgmdSnpStaticGrpVlanIfIndex_Object = MibTableColumn
dMgmdSnpStaticGrpVlanIfIndex = _DMgmdSnpStaticGrpVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 4, 3, 1, 1),
    _DMgmdSnpStaticGrpVlanIfIndex_Type()
)
dMgmdSnpStaticGrpVlanIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dMgmdSnpStaticGrpVlanIfIndex.setStatus("current")
_DMgmdSnpStaticGrpAddressType_Type = InetAddressType
_DMgmdSnpStaticGrpAddressType_Object = MibTableColumn
dMgmdSnpStaticGrpAddressType = _DMgmdSnpStaticGrpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 4, 3, 1, 2),
    _DMgmdSnpStaticGrpAddressType_Type()
)
dMgmdSnpStaticGrpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dMgmdSnpStaticGrpAddressType.setStatus("current")
_DMgmdSnpStaticGrpAddress_Type = InetAddress
_DMgmdSnpStaticGrpAddress_Object = MibTableColumn
dMgmdSnpStaticGrpAddress = _DMgmdSnpStaticGrpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 4, 3, 1, 3),
    _DMgmdSnpStaticGrpAddress_Type()
)
dMgmdSnpStaticGrpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dMgmdSnpStaticGrpAddress.setStatus("current")
_DMgmdSnpStaticGrpIfIndex_Type = InterfaceIndex
_DMgmdSnpStaticGrpIfIndex_Object = MibTableColumn
dMgmdSnpStaticGrpIfIndex = _DMgmdSnpStaticGrpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 4, 3, 1, 4),
    _DMgmdSnpStaticGrpIfIndex_Type()
)
dMgmdSnpStaticGrpIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dMgmdSnpStaticGrpIfIndex.setStatus("current")
_DMgmdSnpStaticGrpStatus_Type = RowStatus
_DMgmdSnpStaticGrpStatus_Object = MibTableColumn
dMgmdSnpStaticGrpStatus = _DMgmdSnpStaticGrpStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 4, 3, 1, 5),
    _DMgmdSnpStaticGrpStatus_Type()
)
dMgmdSnpStaticGrpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dMgmdSnpStaticGrpStatus.setStatus("current")
_DMgmdSnpStaticGrpSrcTable_Object = MibTable
dMgmdSnpStaticGrpSrcTable = _DMgmdSnpStaticGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 4, 4)
)
if mibBuilder.loadTexts:
    dMgmdSnpStaticGrpSrcTable.setStatus("current")
_DMgmdSnpStaticGrpSrcEntry_Object = MibTableRow
dMgmdSnpStaticGrpSrcEntry = _DMgmdSnpStaticGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 4, 4, 1)
)
dMgmdSnpStaticGrpSrcEntry.setIndexNames(
    (0, "DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpStaticGrpVlanIfIndex"),
    (0, "DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpStaticGrpAddressType"),
    (0, "DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpStaticGrpAddress"),
    (0, "DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpStaticGrpSrcAddrType"),
    (0, "DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpStaticGrpSrcAddress"),
    (0, "DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpStaticGrpSrcIfIndex"),
)
if mibBuilder.loadTexts:
    dMgmdSnpStaticGrpSrcEntry.setStatus("current")
_DMgmdSnpStaticGrpSrcAddrType_Type = InetAddressType
_DMgmdSnpStaticGrpSrcAddrType_Object = MibTableColumn
dMgmdSnpStaticGrpSrcAddrType = _DMgmdSnpStaticGrpSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 4, 4, 1, 1),
    _DMgmdSnpStaticGrpSrcAddrType_Type()
)
dMgmdSnpStaticGrpSrcAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dMgmdSnpStaticGrpSrcAddrType.setStatus("current")
_DMgmdSnpStaticGrpSrcAddress_Type = InetAddress
_DMgmdSnpStaticGrpSrcAddress_Object = MibTableColumn
dMgmdSnpStaticGrpSrcAddress = _DMgmdSnpStaticGrpSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 4, 4, 1, 2),
    _DMgmdSnpStaticGrpSrcAddress_Type()
)
dMgmdSnpStaticGrpSrcAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dMgmdSnpStaticGrpSrcAddress.setStatus("current")
_DMgmdSnpStaticGrpSrcIfIndex_Type = InterfaceIndex
_DMgmdSnpStaticGrpSrcIfIndex_Object = MibTableColumn
dMgmdSnpStaticGrpSrcIfIndex = _DMgmdSnpStaticGrpSrcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 4, 4, 1, 3),
    _DMgmdSnpStaticGrpSrcIfIndex_Type()
)
dMgmdSnpStaticGrpSrcIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dMgmdSnpStaticGrpSrcIfIndex.setStatus("current")
_DMgmdSnpStaticGrpSrcStatus_Type = RowStatus
_DMgmdSnpStaticGrpSrcStatus_Object = MibTableColumn
dMgmdSnpStaticGrpSrcStatus = _DMgmdSnpStaticGrpSrcStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 4, 4, 1, 4),
    _DMgmdSnpStaticGrpSrcStatus_Type()
)
dMgmdSnpStaticGrpSrcStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dMgmdSnpStaticGrpSrcStatus.setStatus("current")
_DMgmdSnpHostTable_Object = MibTable
dMgmdSnpHostTable = _DMgmdSnpHostTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 5)
)
if mibBuilder.loadTexts:
    dMgmdSnpHostTable.setStatus("current")
_DMgmdSnpHostEntry_Object = MibTableRow
dMgmdSnpHostEntry = _DMgmdSnpHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 5, 1)
)
dMgmdSnpHostEntry.setIndexNames(
    (0, "DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpHostVlanIfIndex"),
    (0, "DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpHostGrpAddressType"),
    (0, "DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpHostGrpAddress"),
    (0, "DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpHostIfIndex"),
    (0, "DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpHostAddrType"),
    (0, "DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpHostAddress"),
)
if mibBuilder.loadTexts:
    dMgmdSnpHostEntry.setStatus("current")
_DMgmdSnpHostVlanIfIndex_Type = InterfaceIndex
_DMgmdSnpHostVlanIfIndex_Object = MibTableColumn
dMgmdSnpHostVlanIfIndex = _DMgmdSnpHostVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 5, 1, 1),
    _DMgmdSnpHostVlanIfIndex_Type()
)
dMgmdSnpHostVlanIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dMgmdSnpHostVlanIfIndex.setStatus("current")
_DMgmdSnpHostGrpAddressType_Type = InetAddressType
_DMgmdSnpHostGrpAddressType_Object = MibTableColumn
dMgmdSnpHostGrpAddressType = _DMgmdSnpHostGrpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 5, 1, 2),
    _DMgmdSnpHostGrpAddressType_Type()
)
dMgmdSnpHostGrpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dMgmdSnpHostGrpAddressType.setStatus("current")
_DMgmdSnpHostGrpAddress_Type = InetAddress
_DMgmdSnpHostGrpAddress_Object = MibTableColumn
dMgmdSnpHostGrpAddress = _DMgmdSnpHostGrpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 5, 1, 3),
    _DMgmdSnpHostGrpAddress_Type()
)
dMgmdSnpHostGrpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dMgmdSnpHostGrpAddress.setStatus("current")
_DMgmdSnpHostIfIndex_Type = InterfaceIndex
_DMgmdSnpHostIfIndex_Object = MibTableColumn
dMgmdSnpHostIfIndex = _DMgmdSnpHostIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 5, 1, 4),
    _DMgmdSnpHostIfIndex_Type()
)
dMgmdSnpHostIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dMgmdSnpHostIfIndex.setStatus("current")
_DMgmdSnpHostAddrType_Type = InetAddressType
_DMgmdSnpHostAddrType_Object = MibTableColumn
dMgmdSnpHostAddrType = _DMgmdSnpHostAddrType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 5, 1, 5),
    _DMgmdSnpHostAddrType_Type()
)
dMgmdSnpHostAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dMgmdSnpHostAddrType.setStatus("current")
_DMgmdSnpHostAddress_Type = InetAddress
_DMgmdSnpHostAddress_Object = MibTableColumn
dMgmdSnpHostAddress = _DMgmdSnpHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 5, 1, 6),
    _DMgmdSnpHostAddress_Type()
)
dMgmdSnpHostAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dMgmdSnpHostAddress.setStatus("current")
_DMgmdSnpStatistics_ObjectIdentity = ObjectIdentity
dMgmdSnpStatistics = _DMgmdSnpStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 6)
)
_DMgmdSnpStatPortIfTable_Object = MibTable
dMgmdSnpStatPortIfTable = _DMgmdSnpStatPortIfTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 6, 1)
)
if mibBuilder.loadTexts:
    dMgmdSnpStatPortIfTable.setStatus("current")
_DMgmdSnpStatPortIfEntry_Object = MibTableRow
dMgmdSnpStatPortIfEntry = _DMgmdSnpStatPortIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 6, 1, 1)
)
dMgmdSnpStatPortIfEntry.setIndexNames(
    (0, "DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpStatPortIfIndex"),
    (0, "DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpStatPortIfType"),
)
if mibBuilder.loadTexts:
    dMgmdSnpStatPortIfEntry.setStatus("current")
_DMgmdSnpStatPortIfIndex_Type = InterfaceIndex
_DMgmdSnpStatPortIfIndex_Object = MibTableColumn
dMgmdSnpStatPortIfIndex = _DMgmdSnpStatPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 6, 1, 1, 1),
    _DMgmdSnpStatPortIfIndex_Type()
)
dMgmdSnpStatPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dMgmdSnpStatPortIfIndex.setStatus("current")
_DMgmdSnpStatPortIfType_Type = SnoopingType
_DMgmdSnpStatPortIfType_Object = MibTableColumn
dMgmdSnpStatPortIfType = _DMgmdSnpStatPortIfType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 6, 1, 1, 2),
    _DMgmdSnpStatPortIfType_Type()
)
dMgmdSnpStatPortIfType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dMgmdSnpStatPortIfType.setStatus("current")
_DMgmdSnpStatPortIfV1RxReport_Type = Counter64
_DMgmdSnpStatPortIfV1RxReport_Object = MibTableColumn
dMgmdSnpStatPortIfV1RxReport = _DMgmdSnpStatPortIfV1RxReport_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 6, 1, 1, 3),
    _DMgmdSnpStatPortIfV1RxReport_Type()
)
dMgmdSnpStatPortIfV1RxReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dMgmdSnpStatPortIfV1RxReport.setStatus("current")
_DMgmdSnpStatPortIfV1RxQuery_Type = Counter64
_DMgmdSnpStatPortIfV1RxQuery_Object = MibTableColumn
dMgmdSnpStatPortIfV1RxQuery = _DMgmdSnpStatPortIfV1RxQuery_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 6, 1, 1, 4),
    _DMgmdSnpStatPortIfV1RxQuery_Type()
)
dMgmdSnpStatPortIfV1RxQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dMgmdSnpStatPortIfV1RxQuery.setStatus("current")
_DMgmdSnpStatPortIfV1TxReport_Type = Counter64
_DMgmdSnpStatPortIfV1TxReport_Object = MibTableColumn
dMgmdSnpStatPortIfV1TxReport = _DMgmdSnpStatPortIfV1TxReport_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 6, 1, 1, 5),
    _DMgmdSnpStatPortIfV1TxReport_Type()
)
dMgmdSnpStatPortIfV1TxReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dMgmdSnpStatPortIfV1TxReport.setStatus("current")
_DMgmdSnpStatPortIfV1TxQuery_Type = Counter64
_DMgmdSnpStatPortIfV1TxQuery_Object = MibTableColumn
dMgmdSnpStatPortIfV1TxQuery = _DMgmdSnpStatPortIfV1TxQuery_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 6, 1, 1, 6),
    _DMgmdSnpStatPortIfV1TxQuery_Type()
)
dMgmdSnpStatPortIfV1TxQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dMgmdSnpStatPortIfV1TxQuery.setStatus("current")
_DMgmdSnpStatPortIfV2RxReport_Type = Counter64
_DMgmdSnpStatPortIfV2RxReport_Object = MibTableColumn
dMgmdSnpStatPortIfV2RxReport = _DMgmdSnpStatPortIfV2RxReport_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 6, 1, 1, 7),
    _DMgmdSnpStatPortIfV2RxReport_Type()
)
dMgmdSnpStatPortIfV2RxReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dMgmdSnpStatPortIfV2RxReport.setStatus("current")
_DMgmdSnpStatPortIfV2RxQuery_Type = Counter64
_DMgmdSnpStatPortIfV2RxQuery_Object = MibTableColumn
dMgmdSnpStatPortIfV2RxQuery = _DMgmdSnpStatPortIfV2RxQuery_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 6, 1, 1, 8),
    _DMgmdSnpStatPortIfV2RxQuery_Type()
)
dMgmdSnpStatPortIfV2RxQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dMgmdSnpStatPortIfV2RxQuery.setStatus("current")
_DMgmdSnpStatPortIfV2RxLeave_Type = Counter64
_DMgmdSnpStatPortIfV2RxLeave_Object = MibTableColumn
dMgmdSnpStatPortIfV2RxLeave = _DMgmdSnpStatPortIfV2RxLeave_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 6, 1, 1, 9),
    _DMgmdSnpStatPortIfV2RxLeave_Type()
)
dMgmdSnpStatPortIfV2RxLeave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dMgmdSnpStatPortIfV2RxLeave.setStatus("current")
_DMgmdSnpStatPortIfV2TxReport_Type = Counter64
_DMgmdSnpStatPortIfV2TxReport_Object = MibTableColumn
dMgmdSnpStatPortIfV2TxReport = _DMgmdSnpStatPortIfV2TxReport_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 6, 1, 1, 10),
    _DMgmdSnpStatPortIfV2TxReport_Type()
)
dMgmdSnpStatPortIfV2TxReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dMgmdSnpStatPortIfV2TxReport.setStatus("current")
_DMgmdSnpStatPortIfV2TxQuery_Type = Counter64
_DMgmdSnpStatPortIfV2TxQuery_Object = MibTableColumn
dMgmdSnpStatPortIfV2TxQuery = _DMgmdSnpStatPortIfV2TxQuery_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 6, 1, 1, 11),
    _DMgmdSnpStatPortIfV2TxQuery_Type()
)
dMgmdSnpStatPortIfV2TxQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dMgmdSnpStatPortIfV2TxQuery.setStatus("current")
_DMgmdSnpStatPortIfV2TxLeave_Type = Counter64
_DMgmdSnpStatPortIfV2TxLeave_Object = MibTableColumn
dMgmdSnpStatPortIfV2TxLeave = _DMgmdSnpStatPortIfV2TxLeave_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 6, 1, 1, 12),
    _DMgmdSnpStatPortIfV2TxLeave_Type()
)
dMgmdSnpStatPortIfV2TxLeave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dMgmdSnpStatPortIfV2TxLeave.setStatus("current")
_DMgmdSnpStatPortIfV3RxReport_Type = Counter64
_DMgmdSnpStatPortIfV3RxReport_Object = MibTableColumn
dMgmdSnpStatPortIfV3RxReport = _DMgmdSnpStatPortIfV3RxReport_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 6, 1, 1, 13),
    _DMgmdSnpStatPortIfV3RxReport_Type()
)
dMgmdSnpStatPortIfV3RxReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dMgmdSnpStatPortIfV3RxReport.setStatus("current")
_DMgmdSnpStatPortIfV3RxQuery_Type = Counter64
_DMgmdSnpStatPortIfV3RxQuery_Object = MibTableColumn
dMgmdSnpStatPortIfV3RxQuery = _DMgmdSnpStatPortIfV3RxQuery_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 6, 1, 1, 14),
    _DMgmdSnpStatPortIfV3RxQuery_Type()
)
dMgmdSnpStatPortIfV3RxQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dMgmdSnpStatPortIfV3RxQuery.setStatus("current")
_DMgmdSnpStatPortIfV3TxReport_Type = Counter64
_DMgmdSnpStatPortIfV3TxReport_Object = MibTableColumn
dMgmdSnpStatPortIfV3TxReport = _DMgmdSnpStatPortIfV3TxReport_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 6, 1, 1, 15),
    _DMgmdSnpStatPortIfV3TxReport_Type()
)
dMgmdSnpStatPortIfV3TxReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dMgmdSnpStatPortIfV3TxReport.setStatus("current")
_DMgmdSnpStatPortIfV3TxQuery_Type = Counter64
_DMgmdSnpStatPortIfV3TxQuery_Object = MibTableColumn
dMgmdSnpStatPortIfV3TxQuery = _DMgmdSnpStatPortIfV3TxQuery_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 6, 1, 1, 16),
    _DMgmdSnpStatPortIfV3TxQuery_Type()
)
dMgmdSnpStatPortIfV3TxQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dMgmdSnpStatPortIfV3TxQuery.setStatus("current")
_DMgmdSnpStatPortIfDropByAccGroup_Type = Counter64
_DMgmdSnpStatPortIfDropByAccGroup_Object = MibTableColumn
dMgmdSnpStatPortIfDropByAccGroup = _DMgmdSnpStatPortIfDropByAccGroup_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 6, 1, 1, 17),
    _DMgmdSnpStatPortIfDropByAccGroup_Type()
)
dMgmdSnpStatPortIfDropByAccGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dMgmdSnpStatPortIfDropByAccGroup.setStatus("current")
_DMgmdSnpStatPortIfDropByGrpLimit_Type = Counter64
_DMgmdSnpStatPortIfDropByGrpLimit_Object = MibTableColumn
dMgmdSnpStatPortIfDropByGrpLimit = _DMgmdSnpStatPortIfDropByGrpLimit_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 6, 1, 1, 18),
    _DMgmdSnpStatPortIfDropByGrpLimit_Type()
)
dMgmdSnpStatPortIfDropByGrpLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dMgmdSnpStatPortIfDropByGrpLimit.setStatus("current")
_DMgmdSnpStatVlanIfTable_Object = MibTable
dMgmdSnpStatVlanIfTable = _DMgmdSnpStatVlanIfTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 6, 2)
)
if mibBuilder.loadTexts:
    dMgmdSnpStatVlanIfTable.setStatus("current")
_DMgmdSnpStatVlanIfEntry_Object = MibTableRow
dMgmdSnpStatVlanIfEntry = _DMgmdSnpStatVlanIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 6, 2, 1)
)
dMgmdSnpStatVlanIfEntry.setIndexNames(
    (0, "DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpStatVlanIfIndex"),
    (0, "DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpStatVlanIfType"),
)
if mibBuilder.loadTexts:
    dMgmdSnpStatVlanIfEntry.setStatus("current")
_DMgmdSnpStatVlanIfIndex_Type = VlanId
_DMgmdSnpStatVlanIfIndex_Object = MibTableColumn
dMgmdSnpStatVlanIfIndex = _DMgmdSnpStatVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 6, 2, 1, 1),
    _DMgmdSnpStatVlanIfIndex_Type()
)
dMgmdSnpStatVlanIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dMgmdSnpStatVlanIfIndex.setStatus("current")
_DMgmdSnpStatVlanIfType_Type = SnoopingType
_DMgmdSnpStatVlanIfType_Object = MibTableColumn
dMgmdSnpStatVlanIfType = _DMgmdSnpStatVlanIfType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 6, 2, 1, 2),
    _DMgmdSnpStatVlanIfType_Type()
)
dMgmdSnpStatVlanIfType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dMgmdSnpStatVlanIfType.setStatus("current")
_DMgmdSnpStatVlanIfV1RxReport_Type = Counter64
_DMgmdSnpStatVlanIfV1RxReport_Object = MibTableColumn
dMgmdSnpStatVlanIfV1RxReport = _DMgmdSnpStatVlanIfV1RxReport_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 6, 2, 1, 3),
    _DMgmdSnpStatVlanIfV1RxReport_Type()
)
dMgmdSnpStatVlanIfV1RxReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dMgmdSnpStatVlanIfV1RxReport.setStatus("current")
_DMgmdSnpStatVlanIfV1RxQuery_Type = Counter64
_DMgmdSnpStatVlanIfV1RxQuery_Object = MibTableColumn
dMgmdSnpStatVlanIfV1RxQuery = _DMgmdSnpStatVlanIfV1RxQuery_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 6, 2, 1, 4),
    _DMgmdSnpStatVlanIfV1RxQuery_Type()
)
dMgmdSnpStatVlanIfV1RxQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dMgmdSnpStatVlanIfV1RxQuery.setStatus("current")
_DMgmdSnpStatVlanIfV1TxReport_Type = Counter64
_DMgmdSnpStatVlanIfV1TxReport_Object = MibTableColumn
dMgmdSnpStatVlanIfV1TxReport = _DMgmdSnpStatVlanIfV1TxReport_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 6, 2, 1, 5),
    _DMgmdSnpStatVlanIfV1TxReport_Type()
)
dMgmdSnpStatVlanIfV1TxReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dMgmdSnpStatVlanIfV1TxReport.setStatus("current")
_DMgmdSnpStatVlanIfV1TxQuery_Type = Counter64
_DMgmdSnpStatVlanIfV1TxQuery_Object = MibTableColumn
dMgmdSnpStatVlanIfV1TxQuery = _DMgmdSnpStatVlanIfV1TxQuery_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 6, 2, 1, 6),
    _DMgmdSnpStatVlanIfV1TxQuery_Type()
)
dMgmdSnpStatVlanIfV1TxQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dMgmdSnpStatVlanIfV1TxQuery.setStatus("current")
_DMgmdSnpStatVlanIfV2RxReport_Type = Counter64
_DMgmdSnpStatVlanIfV2RxReport_Object = MibTableColumn
dMgmdSnpStatVlanIfV2RxReport = _DMgmdSnpStatVlanIfV2RxReport_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 6, 2, 1, 7),
    _DMgmdSnpStatVlanIfV2RxReport_Type()
)
dMgmdSnpStatVlanIfV2RxReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dMgmdSnpStatVlanIfV2RxReport.setStatus("current")
_DMgmdSnpStatVlanIfV2RxQuery_Type = Counter64
_DMgmdSnpStatVlanIfV2RxQuery_Object = MibTableColumn
dMgmdSnpStatVlanIfV2RxQuery = _DMgmdSnpStatVlanIfV2RxQuery_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 6, 2, 1, 8),
    _DMgmdSnpStatVlanIfV2RxQuery_Type()
)
dMgmdSnpStatVlanIfV2RxQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dMgmdSnpStatVlanIfV2RxQuery.setStatus("current")
_DMgmdSnpStatVlanIfV2RxLeave_Type = Counter64
_DMgmdSnpStatVlanIfV2RxLeave_Object = MibTableColumn
dMgmdSnpStatVlanIfV2RxLeave = _DMgmdSnpStatVlanIfV2RxLeave_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 6, 2, 1, 9),
    _DMgmdSnpStatVlanIfV2RxLeave_Type()
)
dMgmdSnpStatVlanIfV2RxLeave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dMgmdSnpStatVlanIfV2RxLeave.setStatus("current")
_DMgmdSnpStatVlanIfV2TxReport_Type = Counter64
_DMgmdSnpStatVlanIfV2TxReport_Object = MibTableColumn
dMgmdSnpStatVlanIfV2TxReport = _DMgmdSnpStatVlanIfV2TxReport_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 6, 2, 1, 10),
    _DMgmdSnpStatVlanIfV2TxReport_Type()
)
dMgmdSnpStatVlanIfV2TxReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dMgmdSnpStatVlanIfV2TxReport.setStatus("current")
_DMgmdSnpStatVlanIfV2TxQuery_Type = Counter64
_DMgmdSnpStatVlanIfV2TxQuery_Object = MibTableColumn
dMgmdSnpStatVlanIfV2TxQuery = _DMgmdSnpStatVlanIfV2TxQuery_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 6, 2, 1, 11),
    _DMgmdSnpStatVlanIfV2TxQuery_Type()
)
dMgmdSnpStatVlanIfV2TxQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dMgmdSnpStatVlanIfV2TxQuery.setStatus("current")
_DMgmdSnpStatVlanIfV2TxLeave_Type = Counter64
_DMgmdSnpStatVlanIfV2TxLeave_Object = MibTableColumn
dMgmdSnpStatVlanIfV2TxLeave = _DMgmdSnpStatVlanIfV2TxLeave_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 6, 2, 1, 12),
    _DMgmdSnpStatVlanIfV2TxLeave_Type()
)
dMgmdSnpStatVlanIfV2TxLeave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dMgmdSnpStatVlanIfV2TxLeave.setStatus("current")
_DMgmdSnpStatVlanIfV3RxReport_Type = Counter64
_DMgmdSnpStatVlanIfV3RxReport_Object = MibTableColumn
dMgmdSnpStatVlanIfV3RxReport = _DMgmdSnpStatVlanIfV3RxReport_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 6, 2, 1, 13),
    _DMgmdSnpStatVlanIfV3RxReport_Type()
)
dMgmdSnpStatVlanIfV3RxReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dMgmdSnpStatVlanIfV3RxReport.setStatus("current")
_DMgmdSnpStatVlanIfV3RxQuery_Type = Counter64
_DMgmdSnpStatVlanIfV3RxQuery_Object = MibTableColumn
dMgmdSnpStatVlanIfV3RxQuery = _DMgmdSnpStatVlanIfV3RxQuery_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 6, 2, 1, 14),
    _DMgmdSnpStatVlanIfV3RxQuery_Type()
)
dMgmdSnpStatVlanIfV3RxQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dMgmdSnpStatVlanIfV3RxQuery.setStatus("current")
_DMgmdSnpStatVlanIfV3TxReport_Type = Counter64
_DMgmdSnpStatVlanIfV3TxReport_Object = MibTableColumn
dMgmdSnpStatVlanIfV3TxReport = _DMgmdSnpStatVlanIfV3TxReport_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 6, 2, 1, 15),
    _DMgmdSnpStatVlanIfV3TxReport_Type()
)
dMgmdSnpStatVlanIfV3TxReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dMgmdSnpStatVlanIfV3TxReport.setStatus("current")
_DMgmdSnpStatVlanIfV3TxQuery_Type = Counter64
_DMgmdSnpStatVlanIfV3TxQuery_Object = MibTableColumn
dMgmdSnpStatVlanIfV3TxQuery = _DMgmdSnpStatVlanIfV3TxQuery_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 6, 2, 1, 16),
    _DMgmdSnpStatVlanIfV3TxQuery_Type()
)
dMgmdSnpStatVlanIfV3TxQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dMgmdSnpStatVlanIfV3TxQuery.setStatus("current")
_DMgmdSnpStatVlanIfDropByAccGroup_Type = Counter64
_DMgmdSnpStatVlanIfDropByAccGroup_Object = MibTableColumn
dMgmdSnpStatVlanIfDropByAccGroup = _DMgmdSnpStatVlanIfDropByAccGroup_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 6, 2, 1, 17),
    _DMgmdSnpStatVlanIfDropByAccGroup_Type()
)
dMgmdSnpStatVlanIfDropByAccGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dMgmdSnpStatVlanIfDropByAccGroup.setStatus("current")
_DMgmdSnpStatVlanIfDropByGrpLimit_Type = Counter64
_DMgmdSnpStatVlanIfDropByGrpLimit_Object = MibTableColumn
dMgmdSnpStatVlanIfDropByGrpLimit = _DMgmdSnpStatVlanIfDropByGrpLimit_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 1, 6, 2, 1, 18),
    _DMgmdSnpStatVlanIfDropByGrpLimit_Type()
)
dMgmdSnpStatVlanIfDropByGrpLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dMgmdSnpStatVlanIfDropByGrpLimit.setStatus("current")
_DMgmdSnpMIBConformance_ObjectIdentity = ObjectIdentity
dMgmdSnpMIBConformance = _DMgmdSnpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 2)
)
_DMgmdSnpCompliances_ObjectIdentity = ObjectIdentity
dMgmdSnpCompliances = _DMgmdSnpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 2, 1)
)
_DMgmdSnpGroups_ObjectIdentity = ObjectIdentity
dMgmdSnpGroups = _DMgmdSnpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 2, 2)
)

# Managed Objects groups

dMgmdSnpGblCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 2, 2, 1)
)
dMgmdSnpGblCfgGroup.setObjects(
      *(("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpStateGblEnabled"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpClearAllState"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpClearIgmpSnoopByPortIf"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpClearMldSnoopByPortIf"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpClearIgmpSnoopByVlanId"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpClearMldSnoopByVlanId"))
)
if mibBuilder.loadTexts:
    dMgmdSnpGblCfgGroup.setStatus("current")

dMgmdSnpVlanIfCfgGoup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 2, 2, 2)
)
dMgmdSnpVlanIfCfgGoup.setObjects(
      *(("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpIfRowStatus"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpIfStateEnabled"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpIfQuerierStateEnabled"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpIfQuerierRouter"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpIfFastLeaveEnabled"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpIfFastLeaveHostBased"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpIfExplicitTrackEnabled"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpIfReportSuppresEnabled"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpIfMinimumVersion"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpIfProxyReportingEnabled"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpIfAutoLearnMrouter"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpIfProxyReportSrcAddrType"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpIfProxyReportSrcAddr"))
)
if mibBuilder.loadTexts:
    dMgmdSnpVlanIfCfgGoup.setStatus("current")

dMgmdSnpPortIfCfgGoup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 2, 2, 3)
)
dMgmdSnpPortIfCfgGoup.setObjects(
      *(("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpMrouterStatus"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpMrouterAdminState"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpIfLimitRowStatus"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpIfLimitExceptAccLstName"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpIfLimitValue"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpAccGrpStatus"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpAccessGroupName"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpStaticGrpStatus"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpStaticGrpSrcStatus"))
)
if mibBuilder.loadTexts:
    dMgmdSnpPortIfCfgGoup.setStatus("current")

dMgmdSnpDynamicInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 2, 2, 4)
)
dMgmdSnpDynamicInfoGroup.setObjects(
      *(("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpMrouterDynamicMrouter"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpHostAddress"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpGroupVersion"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpGroupUpTime"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpGroupExpire"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpGroupMode"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpGroupLastReportAddrType"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpGroupLastReportAddr"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpGroupSrcUpTime"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpGroupSrcExpire"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpGroupSrcForward"))
)
if mibBuilder.loadTexts:
    dMgmdSnpDynamicInfoGroup.setStatus("current")

dMgmdSnpStatisticsInfoGoup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 2, 2, 5)
)
dMgmdSnpStatisticsInfoGoup.setObjects(
      *(("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpStatPortIfV1RxReport"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpStatPortIfV1RxQuery"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpStatPortIfV1TxReport"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpStatPortIfV1TxQuery"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpStatPortIfV2RxReport"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpStatPortIfV2RxQuery"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpStatPortIfV2RxLeave"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpStatPortIfV2TxReport"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpStatPortIfV2TxQuery"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpStatPortIfV2TxLeave"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpStatPortIfV3RxReport"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpStatPortIfV3RxQuery"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpStatPortIfV3TxReport"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpStatPortIfV3TxQuery"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpStatPortIfDropByAccGroup"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpStatPortIfDropByGrpLimit"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpStatVlanIfV1RxReport"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpStatVlanIfV1RxQuery"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpStatVlanIfV1TxReport"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpStatVlanIfV1TxQuery"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpStatVlanIfV2RxReport"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpStatVlanIfV2RxQuery"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpStatVlanIfV2RxLeave"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpStatVlanIfV2TxReport"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpStatVlanIfV2TxQuery"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpStatVlanIfV2TxLeave"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpStatVlanIfV3RxReport"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpStatVlanIfV3RxQuery"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpStatVlanIfV3TxReport"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpStatVlanIfV3TxQuery"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpStatVlanIfDropByAccGroup"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpStatVlanIfDropByGrpLimit"))
)
if mibBuilder.loadTexts:
    dMgmdSnpStatisticsInfoGoup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dMgmdSnpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 6, 2, 1, 1)
)
dMgmdSnpCompliance.setObjects(
      *(("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpGblCfgGroup"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpVlanIfCfgGoup"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpPortIfCfgGoup"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpDynamicInfoGroup"),
        ("DLINKSW-MGMD-SNOOPING-MIB", "dMgmdSnpStatisticsInfoGoup"))
)
if mibBuilder.loadTexts:
    dMgmdSnpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-MGMD-SNOOPING-MIB",
    **{"SnoopingType": SnoopingType,
       "dlinkSwMgmdSnoopingMIB": dlinkSwMgmdSnoopingMIB,
       "dMgmdSnpMIBNotifications": dMgmdSnpMIBNotifications,
       "dMgmdSnpMIBObjects": dMgmdSnpMIBObjects,
       "dMgmdSnpGlobalCtrl": dMgmdSnpGlobalCtrl,
       "dMgmdSnpStateGblEnabled": dMgmdSnpStateGblEnabled,
       "dMgmdSnpClearAllState": dMgmdSnpClearAllState,
       "dMgmdSnpClearIgmpSnoopByPortIf": dMgmdSnpClearIgmpSnoopByPortIf,
       "dMgmdSnpClearMldSnoopByPortIf": dMgmdSnpClearMldSnoopByPortIf,
       "dMgmdSnpClearIgmpSnoopByVlanId": dMgmdSnpClearIgmpSnoopByVlanId,
       "dMgmdSnpClearMldSnoopByVlanId": dMgmdSnpClearMldSnoopByVlanId,
       "dMgmdSnpVlanIfCtrl": dMgmdSnpVlanIfCtrl,
       "dMgmdSnpIfTable": dMgmdSnpIfTable,
       "dMgmdSnpIfEntry": dMgmdSnpIfEntry,
       "dMgmdSnpIfVlanIfIndex": dMgmdSnpIfVlanIfIndex,
       "dMgmdSnpIfSnoopingType": dMgmdSnpIfSnoopingType,
       "dMgmdSnpIfRowStatus": dMgmdSnpIfRowStatus,
       "dMgmdSnpIfStateEnabled": dMgmdSnpIfStateEnabled,
       "dMgmdSnpIfQuerierStateEnabled": dMgmdSnpIfQuerierStateEnabled,
       "dMgmdSnpIfQuerierRouter": dMgmdSnpIfQuerierRouter,
       "dMgmdSnpIfFastLeaveEnabled": dMgmdSnpIfFastLeaveEnabled,
       "dMgmdSnpIfFastLeaveHostBased": dMgmdSnpIfFastLeaveHostBased,
       "dMgmdSnpIfMinimumVersion": dMgmdSnpIfMinimumVersion,
       "dMgmdSnpIfExplicitTrackEnabled": dMgmdSnpIfExplicitTrackEnabled,
       "dMgmdSnpIfReportSuppresEnabled": dMgmdSnpIfReportSuppresEnabled,
       "dMgmdSnpIfProxyReportingEnabled": dMgmdSnpIfProxyReportingEnabled,
       "dMgmdSnpIfAutoLearnMrouter": dMgmdSnpIfAutoLearnMrouter,
       "dMgmdSnpIfProxyReportSrcAddrType": dMgmdSnpIfProxyReportSrcAddrType,
       "dMgmdSnpIfProxyReportSrcAddr": dMgmdSnpIfProxyReportSrcAddr,
       "dMgmdSnpIfQueryInterval": dMgmdSnpIfQueryInterval,
       "dMgmdSnpIfQueryMaxResponseTime": dMgmdSnpIfQueryMaxResponseTime,
       "dMgmdSnpIfQueryVersion": dMgmdSnpIfQueryVersion,
       "dMgmdSnpIfRobustness": dMgmdSnpIfRobustness,
       "dMgmdSnpIfLastMemberQueryInterval": dMgmdSnpIfLastMemberQueryInterval,
       "dMgmdSnpIfSuppressionTime": dMgmdSnpIfSuppressionTime,
       "dMgmdSnpPortIfCtrl": dMgmdSnpPortIfCtrl,
       "dMgmdSnpMrouterTable": dMgmdSnpMrouterTable,
       "dMgmdSnpMrouterEntry": dMgmdSnpMrouterEntry,
       "dMgmdSnpMrouterIfIndex": dMgmdSnpMrouterIfIndex,
       "dMgmdSnpMrouterVlanIfIndex": dMgmdSnpMrouterVlanIfIndex,
       "dMgmdSnpMrouterQuerierType": dMgmdSnpMrouterQuerierType,
       "dMgmdSnpMrouterStatus": dMgmdSnpMrouterStatus,
       "dMgmdSnpMrouterAdminState": dMgmdSnpMrouterAdminState,
       "dMgmdSnpMrouterDynamicMrouter": dMgmdSnpMrouterDynamicMrouter,
       "dMgmdSnpIfLimitTable": dMgmdSnpIfLimitTable,
       "dMgmdSnpIfLimitEntry": dMgmdSnpIfLimitEntry,
       "dMgmdSnpIfLimitIfIndex": dMgmdSnpIfLimitIfIndex,
       "dMgmdSnpIfLimitVlanId": dMgmdSnpIfLimitVlanId,
       "dMgmdSnpIfLimitSnoopingType": dMgmdSnpIfLimitSnoopingType,
       "dMgmdSnpIfLimitRowStatus": dMgmdSnpIfLimitRowStatus,
       "dMgmdSnpIfLimitExceptAccLstName": dMgmdSnpIfLimitExceptAccLstName,
       "dMgmdSnpIfLimitValue": dMgmdSnpIfLimitValue,
       "dMgmdSnpAccGrpTable": dMgmdSnpAccGrpTable,
       "dMgmdSnpAccGrpEntry": dMgmdSnpAccGrpEntry,
       "dMgmdSnpAccGrpIfIndex": dMgmdSnpAccGrpIfIndex,
       "dMgmdSnpAccGrpVlanId": dMgmdSnpAccGrpVlanId,
       "dMgmdSnpAccGrpSnoopingType": dMgmdSnpAccGrpSnoopingType,
       "dMgmdSnpAccGrpStatus": dMgmdSnpAccGrpStatus,
       "dMgmdSnpAccessGroupName": dMgmdSnpAccessGroupName,
       "dMgmdSnpGroupCtrl": dMgmdSnpGroupCtrl,
       "dMgmdSnpGroupTable": dMgmdSnpGroupTable,
       "dMgmdSnpGroupEntry": dMgmdSnpGroupEntry,
       "dMgmdSnpGroupVlanIfIndex": dMgmdSnpGroupVlanIfIndex,
       "dMgmdSnpGroupAddressType": dMgmdSnpGroupAddressType,
       "dMgmdSnpGroupAddress": dMgmdSnpGroupAddress,
       "dMgmdSnpGroupIfIndex": dMgmdSnpGroupIfIndex,
       "dMgmdSnpGroupVersion": dMgmdSnpGroupVersion,
       "dMgmdSnpGroupUpTime": dMgmdSnpGroupUpTime,
       "dMgmdSnpGroupExpire": dMgmdSnpGroupExpire,
       "dMgmdSnpGroupMode": dMgmdSnpGroupMode,
       "dMgmdSnpGroupLastReportAddrType": dMgmdSnpGroupLastReportAddrType,
       "dMgmdSnpGroupLastReportAddr": dMgmdSnpGroupLastReportAddr,
       "dMgmdSnpGroupSrcTable": dMgmdSnpGroupSrcTable,
       "dMgmdSnpGroupSrcEntry": dMgmdSnpGroupSrcEntry,
       "dMgmdSnpGroupSrcAddrType": dMgmdSnpGroupSrcAddrType,
       "dMgmdSnpGroupSrcAddress": dMgmdSnpGroupSrcAddress,
       "dMgmdSnpGroupSrcIfIndex": dMgmdSnpGroupSrcIfIndex,
       "dMgmdSnpGroupSrcUpTime": dMgmdSnpGroupSrcUpTime,
       "dMgmdSnpGroupSrcExpire": dMgmdSnpGroupSrcExpire,
       "dMgmdSnpGroupSrcForward": dMgmdSnpGroupSrcForward,
       "dMgmdSnpStaticGrpTable": dMgmdSnpStaticGrpTable,
       "dMgmdSnpStaticGrpEntry": dMgmdSnpStaticGrpEntry,
       "dMgmdSnpStaticGrpVlanIfIndex": dMgmdSnpStaticGrpVlanIfIndex,
       "dMgmdSnpStaticGrpAddressType": dMgmdSnpStaticGrpAddressType,
       "dMgmdSnpStaticGrpAddress": dMgmdSnpStaticGrpAddress,
       "dMgmdSnpStaticGrpIfIndex": dMgmdSnpStaticGrpIfIndex,
       "dMgmdSnpStaticGrpStatus": dMgmdSnpStaticGrpStatus,
       "dMgmdSnpStaticGrpSrcTable": dMgmdSnpStaticGrpSrcTable,
       "dMgmdSnpStaticGrpSrcEntry": dMgmdSnpStaticGrpSrcEntry,
       "dMgmdSnpStaticGrpSrcAddrType": dMgmdSnpStaticGrpSrcAddrType,
       "dMgmdSnpStaticGrpSrcAddress": dMgmdSnpStaticGrpSrcAddress,
       "dMgmdSnpStaticGrpSrcIfIndex": dMgmdSnpStaticGrpSrcIfIndex,
       "dMgmdSnpStaticGrpSrcStatus": dMgmdSnpStaticGrpSrcStatus,
       "dMgmdSnpHostTable": dMgmdSnpHostTable,
       "dMgmdSnpHostEntry": dMgmdSnpHostEntry,
       "dMgmdSnpHostVlanIfIndex": dMgmdSnpHostVlanIfIndex,
       "dMgmdSnpHostGrpAddressType": dMgmdSnpHostGrpAddressType,
       "dMgmdSnpHostGrpAddress": dMgmdSnpHostGrpAddress,
       "dMgmdSnpHostIfIndex": dMgmdSnpHostIfIndex,
       "dMgmdSnpHostAddrType": dMgmdSnpHostAddrType,
       "dMgmdSnpHostAddress": dMgmdSnpHostAddress,
       "dMgmdSnpStatistics": dMgmdSnpStatistics,
       "dMgmdSnpStatPortIfTable": dMgmdSnpStatPortIfTable,
       "dMgmdSnpStatPortIfEntry": dMgmdSnpStatPortIfEntry,
       "dMgmdSnpStatPortIfIndex": dMgmdSnpStatPortIfIndex,
       "dMgmdSnpStatPortIfType": dMgmdSnpStatPortIfType,
       "dMgmdSnpStatPortIfV1RxReport": dMgmdSnpStatPortIfV1RxReport,
       "dMgmdSnpStatPortIfV1RxQuery": dMgmdSnpStatPortIfV1RxQuery,
       "dMgmdSnpStatPortIfV1TxReport": dMgmdSnpStatPortIfV1TxReport,
       "dMgmdSnpStatPortIfV1TxQuery": dMgmdSnpStatPortIfV1TxQuery,
       "dMgmdSnpStatPortIfV2RxReport": dMgmdSnpStatPortIfV2RxReport,
       "dMgmdSnpStatPortIfV2RxQuery": dMgmdSnpStatPortIfV2RxQuery,
       "dMgmdSnpStatPortIfV2RxLeave": dMgmdSnpStatPortIfV2RxLeave,
       "dMgmdSnpStatPortIfV2TxReport": dMgmdSnpStatPortIfV2TxReport,
       "dMgmdSnpStatPortIfV2TxQuery": dMgmdSnpStatPortIfV2TxQuery,
       "dMgmdSnpStatPortIfV2TxLeave": dMgmdSnpStatPortIfV2TxLeave,
       "dMgmdSnpStatPortIfV3RxReport": dMgmdSnpStatPortIfV3RxReport,
       "dMgmdSnpStatPortIfV3RxQuery": dMgmdSnpStatPortIfV3RxQuery,
       "dMgmdSnpStatPortIfV3TxReport": dMgmdSnpStatPortIfV3TxReport,
       "dMgmdSnpStatPortIfV3TxQuery": dMgmdSnpStatPortIfV3TxQuery,
       "dMgmdSnpStatPortIfDropByAccGroup": dMgmdSnpStatPortIfDropByAccGroup,
       "dMgmdSnpStatPortIfDropByGrpLimit": dMgmdSnpStatPortIfDropByGrpLimit,
       "dMgmdSnpStatVlanIfTable": dMgmdSnpStatVlanIfTable,
       "dMgmdSnpStatVlanIfEntry": dMgmdSnpStatVlanIfEntry,
       "dMgmdSnpStatVlanIfIndex": dMgmdSnpStatVlanIfIndex,
       "dMgmdSnpStatVlanIfType": dMgmdSnpStatVlanIfType,
       "dMgmdSnpStatVlanIfV1RxReport": dMgmdSnpStatVlanIfV1RxReport,
       "dMgmdSnpStatVlanIfV1RxQuery": dMgmdSnpStatVlanIfV1RxQuery,
       "dMgmdSnpStatVlanIfV1TxReport": dMgmdSnpStatVlanIfV1TxReport,
       "dMgmdSnpStatVlanIfV1TxQuery": dMgmdSnpStatVlanIfV1TxQuery,
       "dMgmdSnpStatVlanIfV2RxReport": dMgmdSnpStatVlanIfV2RxReport,
       "dMgmdSnpStatVlanIfV2RxQuery": dMgmdSnpStatVlanIfV2RxQuery,
       "dMgmdSnpStatVlanIfV2RxLeave": dMgmdSnpStatVlanIfV2RxLeave,
       "dMgmdSnpStatVlanIfV2TxReport": dMgmdSnpStatVlanIfV2TxReport,
       "dMgmdSnpStatVlanIfV2TxQuery": dMgmdSnpStatVlanIfV2TxQuery,
       "dMgmdSnpStatVlanIfV2TxLeave": dMgmdSnpStatVlanIfV2TxLeave,
       "dMgmdSnpStatVlanIfV3RxReport": dMgmdSnpStatVlanIfV3RxReport,
       "dMgmdSnpStatVlanIfV3RxQuery": dMgmdSnpStatVlanIfV3RxQuery,
       "dMgmdSnpStatVlanIfV3TxReport": dMgmdSnpStatVlanIfV3TxReport,
       "dMgmdSnpStatVlanIfV3TxQuery": dMgmdSnpStatVlanIfV3TxQuery,
       "dMgmdSnpStatVlanIfDropByAccGroup": dMgmdSnpStatVlanIfDropByAccGroup,
       "dMgmdSnpStatVlanIfDropByGrpLimit": dMgmdSnpStatVlanIfDropByGrpLimit,
       "dMgmdSnpMIBConformance": dMgmdSnpMIBConformance,
       "dMgmdSnpCompliances": dMgmdSnpCompliances,
       "dMgmdSnpCompliance": dMgmdSnpCompliance,
       "dMgmdSnpGroups": dMgmdSnpGroups,
       "dMgmdSnpGblCfgGroup": dMgmdSnpGblCfgGroup,
       "dMgmdSnpVlanIfCfgGoup": dMgmdSnpVlanIfCfgGoup,
       "dMgmdSnpPortIfCfgGoup": dMgmdSnpPortIfCfgGoup,
       "dMgmdSnpDynamicInfoGroup": dMgmdSnpDynamicInfoGroup,
       "dMgmdSnpStatisticsInfoGoup": dMgmdSnpStatisticsInfoGoup}
)
