# SNMP MIB module (DLINKSW-IPMCAST-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-IPMCAST-EXT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:37:18 2025
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
 InetAddressPrefixLength,
 InetAddressType,
 InetVersion) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetVersion")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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

dlinkSwIpMcastExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 55)
)
if mibBuilder.loadTexts:
    dlinkSwIpMcastExtMIB.setRevisions(
        ("2013-05-02 00:00",
         "2014-06-16 00:00",
         "2014-07-18 00:00",
         "2014-08-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DIpmcExtNotifications_ObjectIdentity = ObjectIdentity
dIpmcExtNotifications = _DIpmcExtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 0)
)
_DIpmcExtObjects_ObjectIdentity = ObjectIdentity
dIpmcExtObjects = _DIpmcExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1)
)


class _DIpmcExtMcastRouteEnabled_Type(Bits):
    """Custom type dIpmcExtMcastRouteEnabled based on Bits"""
    namedValues = NamedValues(
        *(("ipv4", 0),
          ("ipv6", 1))
    )

_DIpmcExtMcastRouteEnabled_Type.__name__ = "Bits"
_DIpmcExtMcastRouteEnabled_Object = MibScalar
dIpmcExtMcastRouteEnabled = _DIpmcExtMcastRouteEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 1),
    _DIpmcExtMcastRouteEnabled_Type()
)
dIpmcExtMcastRouteEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dIpmcExtMcastRouteEnabled.setStatus("current")


class _DIpmcExtIpv4McastTableLookupMode_Type(Integer32):
    """Custom type dIpmcExtIpv4McastTableLookupMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("mac", 2))
    )


_DIpmcExtIpv4McastTableLookupMode_Type.__name__ = "Integer32"
_DIpmcExtIpv4McastTableLookupMode_Object = MibScalar
dIpmcExtIpv4McastTableLookupMode = _DIpmcExtIpv4McastTableLookupMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 2),
    _DIpmcExtIpv4McastTableLookupMode_Type()
)
dIpmcExtIpv4McastTableLookupMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dIpmcExtIpv4McastTableLookupMode.setStatus("current")
_DIpmcExtClearStatisticsObjects_ObjectIdentity = ObjectIdentity
dIpmcExtClearStatisticsObjects = _DIpmcExtClearStatisticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 3)
)


class _DIpmcExtClearStatistics_Type(Bits):
    """Custom type dIpmcExtClearStatistics based on Bits"""
    namedValues = NamedValues(
        *(("igmp", 0),
          ("pim", 1),
          ("dvmrp", 2))
    )

_DIpmcExtClearStatistics_Type.__name__ = "Bits"
_DIpmcExtClearStatistics_Object = MibScalar
dIpmcExtClearStatistics = _DIpmcExtClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 3, 1),
    _DIpmcExtClearStatistics_Type()
)
dIpmcExtClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dIpmcExtClearStatistics.setStatus("current")
_DIpmcExtBoundaryTable_Object = MibTable
dIpmcExtBoundaryTable = _DIpmcExtBoundaryTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 4)
)
if mibBuilder.loadTexts:
    dIpmcExtBoundaryTable.setStatus("current")
_DIpmcExtBoundaryEntry_Object = MibTableRow
dIpmcExtBoundaryEntry = _DIpmcExtBoundaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 4, 1)
)
dIpmcExtBoundaryEntry.setIndexNames(
    (0, "DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtBoundaryVersion"),
    (0, "DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtBoundaryIfIdx"),
    (0, "DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtBoundaryAccessList"),
    (0, "DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtBoundaryApplyDirection"),
)
if mibBuilder.loadTexts:
    dIpmcExtBoundaryEntry.setStatus("current")
_DIpmcExtBoundaryVersion_Type = InetVersion
_DIpmcExtBoundaryVersion_Object = MibTableColumn
dIpmcExtBoundaryVersion = _DIpmcExtBoundaryVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 4, 1, 1),
    _DIpmcExtBoundaryVersion_Type()
)
dIpmcExtBoundaryVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dIpmcExtBoundaryVersion.setStatus("current")
_DIpmcExtBoundaryIfIdx_Type = InterfaceIndex
_DIpmcExtBoundaryIfIdx_Object = MibTableColumn
dIpmcExtBoundaryIfIdx = _DIpmcExtBoundaryIfIdx_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 4, 1, 2),
    _DIpmcExtBoundaryIfIdx_Type()
)
dIpmcExtBoundaryIfIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dIpmcExtBoundaryIfIdx.setStatus("current")


class _DIpmcExtBoundaryAccessList_Type(DisplayString):
    """Custom type dIpmcExtBoundaryAccessList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DIpmcExtBoundaryAccessList_Type.__name__ = "DisplayString"
_DIpmcExtBoundaryAccessList_Object = MibTableColumn
dIpmcExtBoundaryAccessList = _DIpmcExtBoundaryAccessList_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 4, 1, 3),
    _DIpmcExtBoundaryAccessList_Type()
)
dIpmcExtBoundaryAccessList.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dIpmcExtBoundaryAccessList.setStatus("current")


class _DIpmcExtBoundaryApplyDirection_Type(Integer32):
    """Custom type dIpmcExtBoundaryApplyDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_DIpmcExtBoundaryApplyDirection_Type.__name__ = "Integer32"
_DIpmcExtBoundaryApplyDirection_Object = MibTableColumn
dIpmcExtBoundaryApplyDirection = _DIpmcExtBoundaryApplyDirection_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 4, 1, 4),
    _DIpmcExtBoundaryApplyDirection_Type()
)
dIpmcExtBoundaryApplyDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dIpmcExtBoundaryApplyDirection.setStatus("current")
_DIpmcExtBoundaryRowStatus_Type = RowStatus
_DIpmcExtBoundaryRowStatus_Object = MibTableColumn
dIpmcExtBoundaryRowStatus = _DIpmcExtBoundaryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 4, 1, 99),
    _DIpmcExtBoundaryRowStatus_Type()
)
dIpmcExtBoundaryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dIpmcExtBoundaryRowStatus.setStatus("current")
_DIpmcExtStaticMrouteTable_Object = MibTable
dIpmcExtStaticMrouteTable = _DIpmcExtStaticMrouteTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 5)
)
if mibBuilder.loadTexts:
    dIpmcExtStaticMrouteTable.setStatus("current")
_DIpmcExtStaticMrouteEntry_Object = MibTableRow
dIpmcExtStaticMrouteEntry = _DIpmcExtStaticMrouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 5, 1)
)
dIpmcExtStaticMrouteEntry.setIndexNames(
    (0, "DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtStaticMrouteSrcNetType"),
    (0, "DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtStaticMrouteSrcNetAddr"),
    (0, "DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtStaticMrouteSrcNetPreLen"),
)
if mibBuilder.loadTexts:
    dIpmcExtStaticMrouteEntry.setStatus("current")
_DIpmcExtStaticMrouteSrcNetType_Type = InetAddressType
_DIpmcExtStaticMrouteSrcNetType_Object = MibTableColumn
dIpmcExtStaticMrouteSrcNetType = _DIpmcExtStaticMrouteSrcNetType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 5, 1, 1),
    _DIpmcExtStaticMrouteSrcNetType_Type()
)
dIpmcExtStaticMrouteSrcNetType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dIpmcExtStaticMrouteSrcNetType.setStatus("current")
_DIpmcExtStaticMrouteSrcNetAddr_Type = InetAddress
_DIpmcExtStaticMrouteSrcNetAddr_Object = MibTableColumn
dIpmcExtStaticMrouteSrcNetAddr = _DIpmcExtStaticMrouteSrcNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 5, 1, 2),
    _DIpmcExtStaticMrouteSrcNetAddr_Type()
)
dIpmcExtStaticMrouteSrcNetAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dIpmcExtStaticMrouteSrcNetAddr.setStatus("current")
_DIpmcExtStaticMrouteSrcNetPreLen_Type = InetAddressPrefixLength
_DIpmcExtStaticMrouteSrcNetPreLen_Object = MibTableColumn
dIpmcExtStaticMrouteSrcNetPreLen = _DIpmcExtStaticMrouteSrcNetPreLen_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 5, 1, 3),
    _DIpmcExtStaticMrouteSrcNetPreLen_Type()
)
dIpmcExtStaticMrouteSrcNetPreLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dIpmcExtStaticMrouteSrcNetPreLen.setStatus("current")


class _DIpmcExtStaticMrouteRpfType_Type(Integer32):
    """Custom type dIpmcExtStaticMrouteRpfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("neighborAddr", 1),
          ("interfaceId", 2))
    )


_DIpmcExtStaticMrouteRpfType_Type.__name__ = "Integer32"
_DIpmcExtStaticMrouteRpfType_Object = MibTableColumn
dIpmcExtStaticMrouteRpfType = _DIpmcExtStaticMrouteRpfType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 5, 1, 4),
    _DIpmcExtStaticMrouteRpfType_Type()
)
dIpmcExtStaticMrouteRpfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dIpmcExtStaticMrouteRpfType.setStatus("current")
_DIpmcExtStaticMrouteRpfAddr_Type = InetAddress
_DIpmcExtStaticMrouteRpfAddr_Object = MibTableColumn
dIpmcExtStaticMrouteRpfAddr = _DIpmcExtStaticMrouteRpfAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 5, 1, 5),
    _DIpmcExtStaticMrouteRpfAddr_Type()
)
dIpmcExtStaticMrouteRpfAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dIpmcExtStaticMrouteRpfAddr.setStatus("current")
_DIpmcExtStaticMrouteRpfIfIndex_Type = InterfaceIndexOrZero
_DIpmcExtStaticMrouteRpfIfIndex_Object = MibTableColumn
dIpmcExtStaticMrouteRpfIfIndex = _DIpmcExtStaticMrouteRpfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 5, 1, 6),
    _DIpmcExtStaticMrouteRpfIfIndex_Type()
)
dIpmcExtStaticMrouteRpfIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dIpmcExtStaticMrouteRpfIfIndex.setStatus("current")
_DIpmcExtStaticMrouteRowStatus_Type = RowStatus
_DIpmcExtStaticMrouteRowStatus_Object = MibTableColumn
dIpmcExtStaticMrouteRowStatus = _DIpmcExtStaticMrouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 5, 1, 99),
    _DIpmcExtStaticMrouteRowStatus_Type()
)
dIpmcExtStaticMrouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dIpmcExtStaticMrouteRowStatus.setStatus("current")
_DIpmcExtCtrlPktCpuFilterTable_Object = MibTable
dIpmcExtCtrlPktCpuFilterTable = _DIpmcExtCtrlPktCpuFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 6)
)
if mibBuilder.loadTexts:
    dIpmcExtCtrlPktCpuFilterTable.setStatus("current")
_DIpmcExtCtrlPktCpuFilterEntry_Object = MibTableRow
dIpmcExtCtrlPktCpuFilterEntry = _DIpmcExtCtrlPktCpuFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 6, 1)
)
dIpmcExtCtrlPktCpuFilterEntry.setIndexNames(
    (0, "DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtCtrlPktCpuFilterIfIdx"),
)
if mibBuilder.loadTexts:
    dIpmcExtCtrlPktCpuFilterEntry.setStatus("current")
_DIpmcExtCtrlPktCpuFilterIfIdx_Type = InterfaceIndex
_DIpmcExtCtrlPktCpuFilterIfIdx_Object = MibTableColumn
dIpmcExtCtrlPktCpuFilterIfIdx = _DIpmcExtCtrlPktCpuFilterIfIdx_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 6, 1, 1),
    _DIpmcExtCtrlPktCpuFilterIfIdx_Type()
)
dIpmcExtCtrlPktCpuFilterIfIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dIpmcExtCtrlPktCpuFilterIfIdx.setStatus("current")


class _DIpmcExtCtrlPktCpuFilterV4Proto_Type(Bits):
    """Custom type dIpmcExtCtrlPktCpuFilterV4Proto based on Bits"""
    namedValues = NamedValues(
        *(("dvmrp", 0),
          ("pim", 1),
          ("igmpQuery", 2),
          ("ospf", 3),
          ("rip", 4),
          ("vrrp", 5))
    )

_DIpmcExtCtrlPktCpuFilterV4Proto_Type.__name__ = "Bits"
_DIpmcExtCtrlPktCpuFilterV4Proto_Object = MibTableColumn
dIpmcExtCtrlPktCpuFilterV4Proto = _DIpmcExtCtrlPktCpuFilterV4Proto_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 6, 1, 2),
    _DIpmcExtCtrlPktCpuFilterV4Proto_Type()
)
dIpmcExtCtrlPktCpuFilterV4Proto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dIpmcExtCtrlPktCpuFilterV4Proto.setStatus("current")


class _DIpmcExtCtrlPktCpuFilterV6Proto_Type(Bits):
    """Custom type dIpmcExtCtrlPktCpuFilterV6Proto based on Bits"""
    namedValues = NamedValues(
        *(("pim", 0),
          ("mldQuery", 1),
          ("ospf", 2),
          ("ripng", 3),
          ("nd", 4))
    )

_DIpmcExtCtrlPktCpuFilterV6Proto_Type.__name__ = "Bits"
_DIpmcExtCtrlPktCpuFilterV6Proto_Object = MibTableColumn
dIpmcExtCtrlPktCpuFilterV6Proto = _DIpmcExtCtrlPktCpuFilterV6Proto_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 6, 1, 3),
    _DIpmcExtCtrlPktCpuFilterV6Proto_Type()
)
dIpmcExtCtrlPktCpuFilterV6Proto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dIpmcExtCtrlPktCpuFilterV6Proto.setStatus("current")
_DIpmcExtCtrlPktReplacePriTable_Object = MibTable
dIpmcExtCtrlPktReplacePriTable = _DIpmcExtCtrlPktReplacePriTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 7)
)
if mibBuilder.loadTexts:
    dIpmcExtCtrlPktReplacePriTable.setStatus("current")
_DIpmcExtCtrlPktReplacePriEntry_Object = MibTableRow
dIpmcExtCtrlPktReplacePriEntry = _DIpmcExtCtrlPktReplacePriEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 7, 1)
)
dIpmcExtCtrlPktReplacePriEntry.setIndexNames(
    (0, "DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtCtrlPktRepPriPotocol"),
)
if mibBuilder.loadTexts:
    dIpmcExtCtrlPktReplacePriEntry.setStatus("current")


class _DIpmcExtCtrlPktRepPriPotocol_Type(Integer32):
    """Custom type dIpmcExtCtrlPktRepPriPotocol based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("v4dvmrp", 1),
          ("v4pim", 2),
          ("igmpQuery", 3),
          ("v4ospf", 4),
          ("rip", 5),
          ("v4vrrp", 6),
          ("v6pim", 7),
          ("mld", 8),
          ("v6ospf", 9),
          ("ripng", 10),
          ("nd", 11))
    )


_DIpmcExtCtrlPktRepPriPotocol_Type.__name__ = "Integer32"
_DIpmcExtCtrlPktRepPriPotocol_Object = MibTableColumn
dIpmcExtCtrlPktRepPriPotocol = _DIpmcExtCtrlPktRepPriPotocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 7, 1, 1),
    _DIpmcExtCtrlPktRepPriPotocol_Type()
)
dIpmcExtCtrlPktRepPriPotocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dIpmcExtCtrlPktRepPriPotocol.setStatus("current")


class _DIpmcExtCtrlPktRepDscp_Type(Integer32):
    """Custom type dIpmcExtCtrlPktRepDscp based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 63),
    )


_DIpmcExtCtrlPktRepDscp_Type.__name__ = "Integer32"
_DIpmcExtCtrlPktRepDscp_Object = MibTableColumn
dIpmcExtCtrlPktRepDscp = _DIpmcExtCtrlPktRepDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 7, 1, 2),
    _DIpmcExtCtrlPktRepDscp_Type()
)
dIpmcExtCtrlPktRepDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dIpmcExtCtrlPktRepDscp.setStatus("current")


class _DIpmcExtCtrlPktRepPriority_Type(Integer32):
    """Custom type dIpmcExtCtrlPktRepPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )


_DIpmcExtCtrlPktRepPriority_Type.__name__ = "Integer32"
_DIpmcExtCtrlPktRepPriority_Object = MibTableColumn
dIpmcExtCtrlPktRepPriority = _DIpmcExtCtrlPktRepPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 7, 1, 3),
    _DIpmcExtCtrlPktRepPriority_Type()
)
dIpmcExtCtrlPktRepPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dIpmcExtCtrlPktRepPriority.setStatus("current")
_DIpmcExtCtrlPktRepPriRowStatus_Type = RowStatus
_DIpmcExtCtrlPktRepPriRowStatus_Object = MibTableColumn
dIpmcExtCtrlPktRepPriRowStatus = _DIpmcExtCtrlPktRepPriRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 7, 1, 99),
    _DIpmcExtCtrlPktRepPriRowStatus_Type()
)
dIpmcExtCtrlPktRepPriRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dIpmcExtCtrlPktRepPriRowStatus.setStatus("current")
_DIpmcExtRpfTable_Object = MibTable
dIpmcExtRpfTable = _DIpmcExtRpfTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 8)
)
if mibBuilder.loadTexts:
    dIpmcExtRpfTable.setStatus("current")
_DIpmcExtRpfEntry_Object = MibTableRow
dIpmcExtRpfEntry = _DIpmcExtRpfEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 8, 1)
)
dIpmcExtRpfEntry.setIndexNames(
    (0, "DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtRpfAddrType"),
    (0, "DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtRpfAddr"),
    (0, "DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtRpfRouteAddr"),
    (0, "DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtRpfRoutePrefixLen"),
)
if mibBuilder.loadTexts:
    dIpmcExtRpfEntry.setStatus("current")
_DIpmcExtRpfAddrType_Type = InetAddressType
_DIpmcExtRpfAddrType_Object = MibTableColumn
dIpmcExtRpfAddrType = _DIpmcExtRpfAddrType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 8, 1, 1),
    _DIpmcExtRpfAddrType_Type()
)
dIpmcExtRpfAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dIpmcExtRpfAddrType.setStatus("current")
_DIpmcExtRpfAddr_Type = InetAddress
_DIpmcExtRpfAddr_Object = MibTableColumn
dIpmcExtRpfAddr = _DIpmcExtRpfAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 8, 1, 2),
    _DIpmcExtRpfAddr_Type()
)
dIpmcExtRpfAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dIpmcExtRpfAddr.setStatus("current")
_DIpmcExtRpfRouteAddr_Type = InetAddress
_DIpmcExtRpfRouteAddr_Object = MibTableColumn
dIpmcExtRpfRouteAddr = _DIpmcExtRpfRouteAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 8, 1, 3),
    _DIpmcExtRpfRouteAddr_Type()
)
dIpmcExtRpfRouteAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dIpmcExtRpfRouteAddr.setStatus("current")
_DIpmcExtRpfRoutePrefixLen_Type = InetAddressPrefixLength
_DIpmcExtRpfRoutePrefixLen_Object = MibTableColumn
dIpmcExtRpfRoutePrefixLen = _DIpmcExtRpfRoutePrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 8, 1, 4),
    _DIpmcExtRpfRoutePrefixLen_Type()
)
dIpmcExtRpfRoutePrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dIpmcExtRpfRoutePrefixLen.setStatus("current")
_DIpmcExtRpfIfIndex_Type = InterfaceIndexOrZero
_DIpmcExtRpfIfIndex_Object = MibTableColumn
dIpmcExtRpfIfIndex = _DIpmcExtRpfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 8, 1, 5),
    _DIpmcExtRpfIfIndex_Type()
)
dIpmcExtRpfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpmcExtRpfIfIndex.setStatus("current")
_DIpmcExtRpfNeighborAddr_Type = InetAddress
_DIpmcExtRpfNeighborAddr_Object = MibTableColumn
dIpmcExtRpfNeighborAddr = _DIpmcExtRpfNeighborAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 8, 1, 6),
    _DIpmcExtRpfNeighborAddr_Type()
)
dIpmcExtRpfNeighborAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpmcExtRpfNeighborAddr.setStatus("current")


class _DIpmcExtRpfType_Type(Integer32):
    """Custom type dIpmcExtRpfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unicast", 1),
          ("static", 2))
    )


_DIpmcExtRpfType_Type.__name__ = "Integer32"
_DIpmcExtRpfType_Object = MibTableColumn
dIpmcExtRpfType = _DIpmcExtRpfType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 8, 1, 7),
    _DIpmcExtRpfType_Type()
)
dIpmcExtRpfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpmcExtRpfType.setStatus("current")
_DIpmcExtRpfMetricValid_Type = TruthValue
_DIpmcExtRpfMetricValid_Object = MibTableColumn
dIpmcExtRpfMetricValid = _DIpmcExtRpfMetricValid_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 8, 1, 9),
    _DIpmcExtRpfMetricValid_Type()
)
dIpmcExtRpfMetricValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpmcExtRpfMetricValid.setStatus("current")
_DIpmcExtRpfMetric_Type = Unsigned32
_DIpmcExtRpfMetric_Object = MibTableColumn
dIpmcExtRpfMetric = _DIpmcExtRpfMetric_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 8, 1, 10),
    _DIpmcExtRpfMetric_Type()
)
dIpmcExtRpfMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpmcExtRpfMetric.setStatus("current")
_DIpmcExtGrpOutgoingPortTable_Object = MibTable
dIpmcExtGrpOutgoingPortTable = _DIpmcExtGrpOutgoingPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 9)
)
if mibBuilder.loadTexts:
    dIpmcExtGrpOutgoingPortTable.setStatus("current")
_DIpmcExtGrpOutgoingPortEntry_Object = MibTableRow
dIpmcExtGrpOutgoingPortEntry = _DIpmcExtGrpOutgoingPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 9, 1)
)
dIpmcExtGrpOutgoingPortEntry.setIndexNames(
    (0, "DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtGrpOutgoingAddrType"),
    (0, "DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtGrpOutgoingVlanIndex"),
    (0, "DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtGrpOutgoingGroupAddr"),
    (0, "DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtGrpOutgoingPfxLen"),
    (0, "DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtGrpOutgoingSrcAddr"),
    (0, "DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtGrpOutgoingSrcPfxLen"),
    (0, "DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtGrpOutgoingPort"),
)
if mibBuilder.loadTexts:
    dIpmcExtGrpOutgoingPortEntry.setStatus("current")
_DIpmcExtGrpOutgoingAddrType_Type = InetAddressType
_DIpmcExtGrpOutgoingAddrType_Object = MibTableColumn
dIpmcExtGrpOutgoingAddrType = _DIpmcExtGrpOutgoingAddrType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 9, 1, 1),
    _DIpmcExtGrpOutgoingAddrType_Type()
)
dIpmcExtGrpOutgoingAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dIpmcExtGrpOutgoingAddrType.setStatus("current")
_DIpmcExtGrpOutgoingVlanIndex_Type = VlanId
_DIpmcExtGrpOutgoingVlanIndex_Object = MibTableColumn
dIpmcExtGrpOutgoingVlanIndex = _DIpmcExtGrpOutgoingVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 9, 1, 2),
    _DIpmcExtGrpOutgoingVlanIndex_Type()
)
dIpmcExtGrpOutgoingVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dIpmcExtGrpOutgoingVlanIndex.setStatus("current")
_DIpmcExtGrpOutgoingGroupAddr_Type = InetAddress
_DIpmcExtGrpOutgoingGroupAddr_Object = MibTableColumn
dIpmcExtGrpOutgoingGroupAddr = _DIpmcExtGrpOutgoingGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 9, 1, 3),
    _DIpmcExtGrpOutgoingGroupAddr_Type()
)
dIpmcExtGrpOutgoingGroupAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dIpmcExtGrpOutgoingGroupAddr.setStatus("current")
_DIpmcExtGrpOutgoingPfxLen_Type = InetAddressPrefixLength
_DIpmcExtGrpOutgoingPfxLen_Object = MibTableColumn
dIpmcExtGrpOutgoingPfxLen = _DIpmcExtGrpOutgoingPfxLen_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 9, 1, 4),
    _DIpmcExtGrpOutgoingPfxLen_Type()
)
dIpmcExtGrpOutgoingPfxLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dIpmcExtGrpOutgoingPfxLen.setStatus("current")
_DIpmcExtGrpOutgoingSrcAddr_Type = InetAddress
_DIpmcExtGrpOutgoingSrcAddr_Object = MibTableColumn
dIpmcExtGrpOutgoingSrcAddr = _DIpmcExtGrpOutgoingSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 9, 1, 5),
    _DIpmcExtGrpOutgoingSrcAddr_Type()
)
dIpmcExtGrpOutgoingSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dIpmcExtGrpOutgoingSrcAddr.setStatus("current")
_DIpmcExtGrpOutgoingSrcPfxLen_Type = InetAddressPrefixLength
_DIpmcExtGrpOutgoingSrcPfxLen_Object = MibTableColumn
dIpmcExtGrpOutgoingSrcPfxLen = _DIpmcExtGrpOutgoingSrcPfxLen_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 9, 1, 6),
    _DIpmcExtGrpOutgoingSrcPfxLen_Type()
)
dIpmcExtGrpOutgoingSrcPfxLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dIpmcExtGrpOutgoingSrcPfxLen.setStatus("current")
_DIpmcExtGrpOutgoingPort_Type = InterfaceIndex
_DIpmcExtGrpOutgoingPort_Object = MibTableColumn
dIpmcExtGrpOutgoingPort = _DIpmcExtGrpOutgoingPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 9, 1, 7),
    _DIpmcExtGrpOutgoingPort_Type()
)
dIpmcExtGrpOutgoingPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpmcExtGrpOutgoingPort.setStatus("current")
_DIpmcExtStatisticsObjects_ObjectIdentity = ObjectIdentity
dIpmcExtStatisticsObjects = _DIpmcExtStatisticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10)
)
_DIpmcExtIgmpPortIfStatTable_Object = MibTable
dIpmcExtIgmpPortIfStatTable = _DIpmcExtIgmpPortIfStatTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 1)
)
if mibBuilder.loadTexts:
    dIpmcExtIgmpPortIfStatTable.setStatus("current")
_DIpmcExtIgmpPortIfStatEntry_Object = MibTableRow
dIpmcExtIgmpPortIfStatEntry = _DIpmcExtIgmpPortIfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 1, 1)
)
dIpmcExtIgmpPortIfStatEntry.setIndexNames(
    (0, "DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtIgmpPortIfIndex"),
)
if mibBuilder.loadTexts:
    dIpmcExtIgmpPortIfStatEntry.setStatus("current")
_DIpmcExtIgmpPortIfIndex_Type = InterfaceIndex
_DIpmcExtIgmpPortIfIndex_Object = MibTableColumn
dIpmcExtIgmpPortIfIndex = _DIpmcExtIgmpPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 1, 1, 1),
    _DIpmcExtIgmpPortIfIndex_Type()
)
dIpmcExtIgmpPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dIpmcExtIgmpPortIfIndex.setStatus("current")
_DIpmcExtIgmpPortIfV1RxReport_Type = Counter32
_DIpmcExtIgmpPortIfV1RxReport_Object = MibTableColumn
dIpmcExtIgmpPortIfV1RxReport = _DIpmcExtIgmpPortIfV1RxReport_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 1, 1, 2),
    _DIpmcExtIgmpPortIfV1RxReport_Type()
)
dIpmcExtIgmpPortIfV1RxReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpmcExtIgmpPortIfV1RxReport.setStatus("current")
_DIpmcExtIgmpPortIfV1RxQuery_Type = Counter32
_DIpmcExtIgmpPortIfV1RxQuery_Object = MibTableColumn
dIpmcExtIgmpPortIfV1RxQuery = _DIpmcExtIgmpPortIfV1RxQuery_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 1, 1, 3),
    _DIpmcExtIgmpPortIfV1RxQuery_Type()
)
dIpmcExtIgmpPortIfV1RxQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpmcExtIgmpPortIfV1RxQuery.setStatus("current")
_DIpmcExtIgmpPortIfV1TxReport_Type = Counter32
_DIpmcExtIgmpPortIfV1TxReport_Object = MibTableColumn
dIpmcExtIgmpPortIfV1TxReport = _DIpmcExtIgmpPortIfV1TxReport_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 1, 1, 4),
    _DIpmcExtIgmpPortIfV1TxReport_Type()
)
dIpmcExtIgmpPortIfV1TxReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpmcExtIgmpPortIfV1TxReport.setStatus("current")
_DIpmcExtIgmpPortIfV1TxQuery_Type = Counter32
_DIpmcExtIgmpPortIfV1TxQuery_Object = MibTableColumn
dIpmcExtIgmpPortIfV1TxQuery = _DIpmcExtIgmpPortIfV1TxQuery_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 1, 1, 5),
    _DIpmcExtIgmpPortIfV1TxQuery_Type()
)
dIpmcExtIgmpPortIfV1TxQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpmcExtIgmpPortIfV1TxQuery.setStatus("current")
_DIpmcExtIgmpPortIfV2RxReport_Type = Counter32
_DIpmcExtIgmpPortIfV2RxReport_Object = MibTableColumn
dIpmcExtIgmpPortIfV2RxReport = _DIpmcExtIgmpPortIfV2RxReport_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 1, 1, 6),
    _DIpmcExtIgmpPortIfV2RxReport_Type()
)
dIpmcExtIgmpPortIfV2RxReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpmcExtIgmpPortIfV2RxReport.setStatus("current")
_DIpmcExtIgmpPortIfV2RxQuery_Type = Counter32
_DIpmcExtIgmpPortIfV2RxQuery_Object = MibTableColumn
dIpmcExtIgmpPortIfV2RxQuery = _DIpmcExtIgmpPortIfV2RxQuery_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 1, 1, 7),
    _DIpmcExtIgmpPortIfV2RxQuery_Type()
)
dIpmcExtIgmpPortIfV2RxQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpmcExtIgmpPortIfV2RxQuery.setStatus("current")
_DIpmcExtIgmpPortIfV2RxLeave_Type = Counter32
_DIpmcExtIgmpPortIfV2RxLeave_Object = MibTableColumn
dIpmcExtIgmpPortIfV2RxLeave = _DIpmcExtIgmpPortIfV2RxLeave_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 1, 1, 8),
    _DIpmcExtIgmpPortIfV2RxLeave_Type()
)
dIpmcExtIgmpPortIfV2RxLeave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpmcExtIgmpPortIfV2RxLeave.setStatus("current")
_DIpmcExtIgmpPortIfV2TxReport_Type = Counter32
_DIpmcExtIgmpPortIfV2TxReport_Object = MibTableColumn
dIpmcExtIgmpPortIfV2TxReport = _DIpmcExtIgmpPortIfV2TxReport_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 1, 1, 9),
    _DIpmcExtIgmpPortIfV2TxReport_Type()
)
dIpmcExtIgmpPortIfV2TxReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpmcExtIgmpPortIfV2TxReport.setStatus("current")
_DIpmcExtIgmpPortIfV2TxQuery_Type = Counter32
_DIpmcExtIgmpPortIfV2TxQuery_Object = MibTableColumn
dIpmcExtIgmpPortIfV2TxQuery = _DIpmcExtIgmpPortIfV2TxQuery_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 1, 1, 10),
    _DIpmcExtIgmpPortIfV2TxQuery_Type()
)
dIpmcExtIgmpPortIfV2TxQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpmcExtIgmpPortIfV2TxQuery.setStatus("current")
_DIpmcExtIgmpPortIfV2TxLeave_Type = Counter32
_DIpmcExtIgmpPortIfV2TxLeave_Object = MibTableColumn
dIpmcExtIgmpPortIfV2TxLeave = _DIpmcExtIgmpPortIfV2TxLeave_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 1, 1, 11),
    _DIpmcExtIgmpPortIfV2TxLeave_Type()
)
dIpmcExtIgmpPortIfV2TxLeave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpmcExtIgmpPortIfV2TxLeave.setStatus("current")
_DIpmcExtIgmpPortIfV3RxReport_Type = Counter32
_DIpmcExtIgmpPortIfV3RxReport_Object = MibTableColumn
dIpmcExtIgmpPortIfV3RxReport = _DIpmcExtIgmpPortIfV3RxReport_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 1, 1, 12),
    _DIpmcExtIgmpPortIfV3RxReport_Type()
)
dIpmcExtIgmpPortIfV3RxReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpmcExtIgmpPortIfV3RxReport.setStatus("current")
_DIpmcExtIgmpPortIfV3RxQuery_Type = Counter32
_DIpmcExtIgmpPortIfV3RxQuery_Object = MibTableColumn
dIpmcExtIgmpPortIfV3RxQuery = _DIpmcExtIgmpPortIfV3RxQuery_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 1, 1, 13),
    _DIpmcExtIgmpPortIfV3RxQuery_Type()
)
dIpmcExtIgmpPortIfV3RxQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpmcExtIgmpPortIfV3RxQuery.setStatus("current")
_DIpmcExtIgmpPortIfV3TxReport_Type = Counter32
_DIpmcExtIgmpPortIfV3TxReport_Object = MibTableColumn
dIpmcExtIgmpPortIfV3TxReport = _DIpmcExtIgmpPortIfV3TxReport_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 1, 1, 14),
    _DIpmcExtIgmpPortIfV3TxReport_Type()
)
dIpmcExtIgmpPortIfV3TxReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpmcExtIgmpPortIfV3TxReport.setStatus("current")
_DIpmcExtIgmpPortIfV3TxQuery_Type = Counter32
_DIpmcExtIgmpPortIfV3TxQuery_Object = MibTableColumn
dIpmcExtIgmpPortIfV3TxQuery = _DIpmcExtIgmpPortIfV3TxQuery_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 1, 1, 15),
    _DIpmcExtIgmpPortIfV3TxQuery_Type()
)
dIpmcExtIgmpPortIfV3TxQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpmcExtIgmpPortIfV3TxQuery.setStatus("current")
_DIpmcExtIgmpPortIfRxUnknown_Type = Counter32
_DIpmcExtIgmpPortIfRxUnknown_Object = MibTableColumn
dIpmcExtIgmpPortIfRxUnknown = _DIpmcExtIgmpPortIfRxUnknown_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 1, 1, 16),
    _DIpmcExtIgmpPortIfRxUnknown_Type()
)
dIpmcExtIgmpPortIfRxUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpmcExtIgmpPortIfRxUnknown.setStatus("current")
_DIpmcExtIgmpPortIfTxUnknown_Type = Counter32
_DIpmcExtIgmpPortIfTxUnknown_Object = MibTableColumn
dIpmcExtIgmpPortIfTxUnknown = _DIpmcExtIgmpPortIfTxUnknown_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 1, 1, 17),
    _DIpmcExtIgmpPortIfTxUnknown_Type()
)
dIpmcExtIgmpPortIfTxUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpmcExtIgmpPortIfTxUnknown.setStatus("current")
_DIpmcExtPimPortIfStatTable_Object = MibTable
dIpmcExtPimPortIfStatTable = _DIpmcExtPimPortIfStatTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 2)
)
if mibBuilder.loadTexts:
    dIpmcExtPimPortIfStatTable.setStatus("current")
_DIpmcExtPimPortIfStatEntry_Object = MibTableRow
dIpmcExtPimPortIfStatEntry = _DIpmcExtPimPortIfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 2, 1)
)
dIpmcExtPimPortIfStatEntry.setIndexNames(
    (0, "DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtPimPortIfIndex"),
    (0, "DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtPimPortIfVersion"),
)
if mibBuilder.loadTexts:
    dIpmcExtPimPortIfStatEntry.setStatus("current")
_DIpmcExtPimPortIfIndex_Type = InterfaceIndex
_DIpmcExtPimPortIfIndex_Object = MibTableColumn
dIpmcExtPimPortIfIndex = _DIpmcExtPimPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 2, 1, 1),
    _DIpmcExtPimPortIfIndex_Type()
)
dIpmcExtPimPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dIpmcExtPimPortIfIndex.setStatus("current")
_DIpmcExtPimPortIfVersion_Type = InetVersion
_DIpmcExtPimPortIfVersion_Object = MibTableColumn
dIpmcExtPimPortIfVersion = _DIpmcExtPimPortIfVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 2, 1, 2),
    _DIpmcExtPimPortIfVersion_Type()
)
dIpmcExtPimPortIfVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dIpmcExtPimPortIfVersion.setStatus("current")
_DIpmcExtPimPortIfRxHello_Type = Counter32
_DIpmcExtPimPortIfRxHello_Object = MibTableColumn
dIpmcExtPimPortIfRxHello = _DIpmcExtPimPortIfRxHello_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 2, 1, 3),
    _DIpmcExtPimPortIfRxHello_Type()
)
dIpmcExtPimPortIfRxHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpmcExtPimPortIfRxHello.setStatus("current")
_DIpmcExtPimPortIfTxHello_Type = Counter32
_DIpmcExtPimPortIfTxHello_Object = MibTableColumn
dIpmcExtPimPortIfTxHello = _DIpmcExtPimPortIfTxHello_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 2, 1, 4),
    _DIpmcExtPimPortIfTxHello_Type()
)
dIpmcExtPimPortIfTxHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpmcExtPimPortIfTxHello.setStatus("current")
_DIpmcExtPimPortIfRxRegister_Type = Counter32
_DIpmcExtPimPortIfRxRegister_Object = MibTableColumn
dIpmcExtPimPortIfRxRegister = _DIpmcExtPimPortIfRxRegister_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 2, 1, 5),
    _DIpmcExtPimPortIfRxRegister_Type()
)
dIpmcExtPimPortIfRxRegister.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpmcExtPimPortIfRxRegister.setStatus("current")
_DIpmcExtPimPortIfTxRegister_Type = Counter32
_DIpmcExtPimPortIfTxRegister_Object = MibTableColumn
dIpmcExtPimPortIfTxRegister = _DIpmcExtPimPortIfTxRegister_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 2, 1, 6),
    _DIpmcExtPimPortIfTxRegister_Type()
)
dIpmcExtPimPortIfTxRegister.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpmcExtPimPortIfTxRegister.setStatus("current")
_DIpmcExtPimPortIfRxRegisterStop_Type = Counter32
_DIpmcExtPimPortIfRxRegisterStop_Object = MibTableColumn
dIpmcExtPimPortIfRxRegisterStop = _DIpmcExtPimPortIfRxRegisterStop_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 2, 1, 7),
    _DIpmcExtPimPortIfRxRegisterStop_Type()
)
dIpmcExtPimPortIfRxRegisterStop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpmcExtPimPortIfRxRegisterStop.setStatus("current")
_DIpmcExtPimPortIfTxRegisterStop_Type = Counter32
_DIpmcExtPimPortIfTxRegisterStop_Object = MibTableColumn
dIpmcExtPimPortIfTxRegisterStop = _DIpmcExtPimPortIfTxRegisterStop_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 2, 1, 8),
    _DIpmcExtPimPortIfTxRegisterStop_Type()
)
dIpmcExtPimPortIfTxRegisterStop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpmcExtPimPortIfTxRegisterStop.setStatus("current")
_DIpmcExtPimPortIfRxJoinPrune_Type = Counter32
_DIpmcExtPimPortIfRxJoinPrune_Object = MibTableColumn
dIpmcExtPimPortIfRxJoinPrune = _DIpmcExtPimPortIfRxJoinPrune_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 2, 1, 9),
    _DIpmcExtPimPortIfRxJoinPrune_Type()
)
dIpmcExtPimPortIfRxJoinPrune.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpmcExtPimPortIfRxJoinPrune.setStatus("current")
_DIpmcExtPimPortIfTxJoinPrune_Type = Counter32
_DIpmcExtPimPortIfTxJoinPrune_Object = MibTableColumn
dIpmcExtPimPortIfTxJoinPrune = _DIpmcExtPimPortIfTxJoinPrune_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 2, 1, 10),
    _DIpmcExtPimPortIfTxJoinPrune_Type()
)
dIpmcExtPimPortIfTxJoinPrune.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpmcExtPimPortIfTxJoinPrune.setStatus("current")
_DIpmcExtPimPortIfRxBootstrap_Type = Counter32
_DIpmcExtPimPortIfRxBootstrap_Object = MibTableColumn
dIpmcExtPimPortIfRxBootstrap = _DIpmcExtPimPortIfRxBootstrap_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 2, 1, 11),
    _DIpmcExtPimPortIfRxBootstrap_Type()
)
dIpmcExtPimPortIfRxBootstrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpmcExtPimPortIfRxBootstrap.setStatus("current")
_DIpmcExtPimPortIfTxBootstrap_Type = Counter32
_DIpmcExtPimPortIfTxBootstrap_Object = MibTableColumn
dIpmcExtPimPortIfTxBootstrap = _DIpmcExtPimPortIfTxBootstrap_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 2, 1, 12),
    _DIpmcExtPimPortIfTxBootstrap_Type()
)
dIpmcExtPimPortIfTxBootstrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpmcExtPimPortIfTxBootstrap.setStatus("current")
_DIpmcExtPimPortIfRxAssert_Type = Counter32
_DIpmcExtPimPortIfRxAssert_Object = MibTableColumn
dIpmcExtPimPortIfRxAssert = _DIpmcExtPimPortIfRxAssert_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 2, 1, 13),
    _DIpmcExtPimPortIfRxAssert_Type()
)
dIpmcExtPimPortIfRxAssert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpmcExtPimPortIfRxAssert.setStatus("current")
_DIpmcExtPimPortIfTxAssert_Type = Counter32
_DIpmcExtPimPortIfTxAssert_Object = MibTableColumn
dIpmcExtPimPortIfTxAssert = _DIpmcExtPimPortIfTxAssert_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 2, 1, 14),
    _DIpmcExtPimPortIfTxAssert_Type()
)
dIpmcExtPimPortIfTxAssert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpmcExtPimPortIfTxAssert.setStatus("current")
_DIpmcExtPimPortIfRxGraft_Type = Counter32
_DIpmcExtPimPortIfRxGraft_Object = MibTableColumn
dIpmcExtPimPortIfRxGraft = _DIpmcExtPimPortIfRxGraft_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 2, 1, 15),
    _DIpmcExtPimPortIfRxGraft_Type()
)
dIpmcExtPimPortIfRxGraft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpmcExtPimPortIfRxGraft.setStatus("current")
_DIpmcExtPimPortIfTxGraft_Type = Counter32
_DIpmcExtPimPortIfTxGraft_Object = MibTableColumn
dIpmcExtPimPortIfTxGraft = _DIpmcExtPimPortIfTxGraft_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 2, 1, 16),
    _DIpmcExtPimPortIfTxGraft_Type()
)
dIpmcExtPimPortIfTxGraft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpmcExtPimPortIfTxGraft.setStatus("current")
_DIpmcExtPimPortIfRxGraftAck_Type = Counter32
_DIpmcExtPimPortIfRxGraftAck_Object = MibTableColumn
dIpmcExtPimPortIfRxGraftAck = _DIpmcExtPimPortIfRxGraftAck_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 2, 1, 17),
    _DIpmcExtPimPortIfRxGraftAck_Type()
)
dIpmcExtPimPortIfRxGraftAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpmcExtPimPortIfRxGraftAck.setStatus("current")
_DIpmcExtPimPortIfTxGraftAck_Type = Counter32
_DIpmcExtPimPortIfTxGraftAck_Object = MibTableColumn
dIpmcExtPimPortIfTxGraftAck = _DIpmcExtPimPortIfTxGraftAck_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 2, 1, 18),
    _DIpmcExtPimPortIfTxGraftAck_Type()
)
dIpmcExtPimPortIfTxGraftAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpmcExtPimPortIfTxGraftAck.setStatus("current")
_DIpmcExtPimPortIfRxCRpAdv_Type = Counter32
_DIpmcExtPimPortIfRxCRpAdv_Object = MibTableColumn
dIpmcExtPimPortIfRxCRpAdv = _DIpmcExtPimPortIfRxCRpAdv_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 2, 1, 19),
    _DIpmcExtPimPortIfRxCRpAdv_Type()
)
dIpmcExtPimPortIfRxCRpAdv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpmcExtPimPortIfRxCRpAdv.setStatus("current")
_DIpmcExtPimPortIfTxCRpAdv_Type = Counter32
_DIpmcExtPimPortIfTxCRpAdv_Object = MibTableColumn
dIpmcExtPimPortIfTxCRpAdv = _DIpmcExtPimPortIfTxCRpAdv_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 2, 1, 20),
    _DIpmcExtPimPortIfTxCRpAdv_Type()
)
dIpmcExtPimPortIfTxCRpAdv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpmcExtPimPortIfTxCRpAdv.setStatus("current")
_DIpmcExtPimPortIfRxStateRefresh_Type = Counter32
_DIpmcExtPimPortIfRxStateRefresh_Object = MibTableColumn
dIpmcExtPimPortIfRxStateRefresh = _DIpmcExtPimPortIfRxStateRefresh_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 2, 1, 21),
    _DIpmcExtPimPortIfRxStateRefresh_Type()
)
dIpmcExtPimPortIfRxStateRefresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpmcExtPimPortIfRxStateRefresh.setStatus("current")
_DIpmcExtPimPortIfTxStateRefresh_Type = Counter32
_DIpmcExtPimPortIfTxStateRefresh_Object = MibTableColumn
dIpmcExtPimPortIfTxStateRefresh = _DIpmcExtPimPortIfTxStateRefresh_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 2, 1, 22),
    _DIpmcExtPimPortIfTxStateRefresh_Type()
)
dIpmcExtPimPortIfTxStateRefresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpmcExtPimPortIfTxStateRefresh.setStatus("current")
_DIpmcExtPimPortIfRxUnknown_Type = Counter32
_DIpmcExtPimPortIfRxUnknown_Object = MibTableColumn
dIpmcExtPimPortIfRxUnknown = _DIpmcExtPimPortIfRxUnknown_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 2, 1, 23),
    _DIpmcExtPimPortIfRxUnknown_Type()
)
dIpmcExtPimPortIfRxUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpmcExtPimPortIfRxUnknown.setStatus("current")
_DIpmcExtPimPortIfTxUnknown_Type = Counter32
_DIpmcExtPimPortIfTxUnknown_Object = MibTableColumn
dIpmcExtPimPortIfTxUnknown = _DIpmcExtPimPortIfTxUnknown_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 2, 1, 24),
    _DIpmcExtPimPortIfTxUnknown_Type()
)
dIpmcExtPimPortIfTxUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpmcExtPimPortIfTxUnknown.setStatus("current")
_DIpmcExtDvmrpPortIfStatTable_Object = MibTable
dIpmcExtDvmrpPortIfStatTable = _DIpmcExtDvmrpPortIfStatTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 3)
)
if mibBuilder.loadTexts:
    dIpmcExtDvmrpPortIfStatTable.setStatus("current")
_DIpmcExtDvmrpPortIfStatEntry_Object = MibTableRow
dIpmcExtDvmrpPortIfStatEntry = _DIpmcExtDvmrpPortIfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 3, 1)
)
dIpmcExtDvmrpPortIfStatEntry.setIndexNames(
    (0, "DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtDvmrpPortIfIndex"),
)
if mibBuilder.loadTexts:
    dIpmcExtDvmrpPortIfStatEntry.setStatus("current")
_DIpmcExtDvmrpPortIfIndex_Type = InterfaceIndex
_DIpmcExtDvmrpPortIfIndex_Object = MibTableColumn
dIpmcExtDvmrpPortIfIndex = _DIpmcExtDvmrpPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 3, 1, 1),
    _DIpmcExtDvmrpPortIfIndex_Type()
)
dIpmcExtDvmrpPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dIpmcExtDvmrpPortIfIndex.setStatus("current")
_DIpmcExtDvmrpPortIfRxProbe_Type = Counter32
_DIpmcExtDvmrpPortIfRxProbe_Object = MibTableColumn
dIpmcExtDvmrpPortIfRxProbe = _DIpmcExtDvmrpPortIfRxProbe_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 3, 1, 2),
    _DIpmcExtDvmrpPortIfRxProbe_Type()
)
dIpmcExtDvmrpPortIfRxProbe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpmcExtDvmrpPortIfRxProbe.setStatus("current")
_DIpmcExtDvmrpPortIfTxProbe_Type = Counter32
_DIpmcExtDvmrpPortIfTxProbe_Object = MibTableColumn
dIpmcExtDvmrpPortIfTxProbe = _DIpmcExtDvmrpPortIfTxProbe_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 3, 1, 3),
    _DIpmcExtDvmrpPortIfTxProbe_Type()
)
dIpmcExtDvmrpPortIfTxProbe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpmcExtDvmrpPortIfTxProbe.setStatus("current")
_DIpmcExtDvmrpPortIfRxReport_Type = Counter32
_DIpmcExtDvmrpPortIfRxReport_Object = MibTableColumn
dIpmcExtDvmrpPortIfRxReport = _DIpmcExtDvmrpPortIfRxReport_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 3, 1, 4),
    _DIpmcExtDvmrpPortIfRxReport_Type()
)
dIpmcExtDvmrpPortIfRxReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpmcExtDvmrpPortIfRxReport.setStatus("current")
_DIpmcExtDvmrpPortIfTxReport_Type = Counter32
_DIpmcExtDvmrpPortIfTxReport_Object = MibTableColumn
dIpmcExtDvmrpPortIfTxReport = _DIpmcExtDvmrpPortIfTxReport_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 3, 1, 5),
    _DIpmcExtDvmrpPortIfTxReport_Type()
)
dIpmcExtDvmrpPortIfTxReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpmcExtDvmrpPortIfTxReport.setStatus("current")
_DIpmcExtDvmrpPortIfRxPrune_Type = Counter32
_DIpmcExtDvmrpPortIfRxPrune_Object = MibTableColumn
dIpmcExtDvmrpPortIfRxPrune = _DIpmcExtDvmrpPortIfRxPrune_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 3, 1, 6),
    _DIpmcExtDvmrpPortIfRxPrune_Type()
)
dIpmcExtDvmrpPortIfRxPrune.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpmcExtDvmrpPortIfRxPrune.setStatus("current")
_DIpmcExtDvmrpPortIfTxPrune_Type = Counter32
_DIpmcExtDvmrpPortIfTxPrune_Object = MibTableColumn
dIpmcExtDvmrpPortIfTxPrune = _DIpmcExtDvmrpPortIfTxPrune_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 3, 1, 7),
    _DIpmcExtDvmrpPortIfTxPrune_Type()
)
dIpmcExtDvmrpPortIfTxPrune.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpmcExtDvmrpPortIfTxPrune.setStatus("current")
_DIpmcExtDvmrpPortIfRxGraft_Type = Counter32
_DIpmcExtDvmrpPortIfRxGraft_Object = MibTableColumn
dIpmcExtDvmrpPortIfRxGraft = _DIpmcExtDvmrpPortIfRxGraft_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 3, 1, 8),
    _DIpmcExtDvmrpPortIfRxGraft_Type()
)
dIpmcExtDvmrpPortIfRxGraft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpmcExtDvmrpPortIfRxGraft.setStatus("current")
_DIpmcExtDvmrpPortIfTxGraft_Type = Counter32
_DIpmcExtDvmrpPortIfTxGraft_Object = MibTableColumn
dIpmcExtDvmrpPortIfTxGraft = _DIpmcExtDvmrpPortIfTxGraft_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 3, 1, 9),
    _DIpmcExtDvmrpPortIfTxGraft_Type()
)
dIpmcExtDvmrpPortIfTxGraft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpmcExtDvmrpPortIfTxGraft.setStatus("current")
_DIpmcExtDvmrpPortIfRxGraftAck_Type = Counter32
_DIpmcExtDvmrpPortIfRxGraftAck_Object = MibTableColumn
dIpmcExtDvmrpPortIfRxGraftAck = _DIpmcExtDvmrpPortIfRxGraftAck_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 3, 1, 10),
    _DIpmcExtDvmrpPortIfRxGraftAck_Type()
)
dIpmcExtDvmrpPortIfRxGraftAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpmcExtDvmrpPortIfRxGraftAck.setStatus("current")
_DIpmcExtDvmrpPortIfTxGraftAck_Type = Counter32
_DIpmcExtDvmrpPortIfTxGraftAck_Object = MibTableColumn
dIpmcExtDvmrpPortIfTxGraftAck = _DIpmcExtDvmrpPortIfTxGraftAck_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 3, 1, 11),
    _DIpmcExtDvmrpPortIfTxGraftAck_Type()
)
dIpmcExtDvmrpPortIfTxGraftAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpmcExtDvmrpPortIfTxGraftAck.setStatus("current")
_DIpmcExtDvmrpPortIfRxUnknown_Type = Counter32
_DIpmcExtDvmrpPortIfRxUnknown_Object = MibTableColumn
dIpmcExtDvmrpPortIfRxUnknown = _DIpmcExtDvmrpPortIfRxUnknown_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 3, 1, 12),
    _DIpmcExtDvmrpPortIfRxUnknown_Type()
)
dIpmcExtDvmrpPortIfRxUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpmcExtDvmrpPortIfRxUnknown.setStatus("current")
_DIpmcExtDvmrpPortIfTxUnknown_Type = Counter32
_DIpmcExtDvmrpPortIfTxUnknown_Object = MibTableColumn
dIpmcExtDvmrpPortIfTxUnknown = _DIpmcExtDvmrpPortIfTxUnknown_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 1, 10, 3, 1, 13),
    _DIpmcExtDvmrpPortIfTxUnknown_Type()
)
dIpmcExtDvmrpPortIfTxUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpmcExtDvmrpPortIfTxUnknown.setStatus("current")
_DIpmcExtConformance_ObjectIdentity = ObjectIdentity
dIpmcExtConformance = _DIpmcExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 2)
)
_DIpmcExtCompliances_ObjectIdentity = ObjectIdentity
dIpmcExtCompliances = _DIpmcExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 2, 1)
)
_DIpmcExtGroups_ObjectIdentity = ObjectIdentity
dIpmcExtGroups = _DIpmcExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 2, 2)
)

# Managed Objects groups

dIpmcExtClearStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 2, 2, 1)
)
dIpmcExtClearStatisticsGroup.setObjects(
    ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtClearStatistics")
)
if mibBuilder.loadTexts:
    dIpmcExtClearStatisticsGroup.setStatus("current")

dIpmcExtGeneralCtrlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 2, 2, 2)
)
dIpmcExtGeneralCtrlGroup.setObjects(
      *(("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtMcastRouteEnabled"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtIpv4McastTableLookupMode"))
)
if mibBuilder.loadTexts:
    dIpmcExtGeneralCtrlGroup.setStatus("current")

dIpmcExtBoundaryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 2, 2, 3)
)
dIpmcExtBoundaryGroup.setObjects(
    ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtBoundaryRowStatus")
)
if mibBuilder.loadTexts:
    dIpmcExtBoundaryGroup.setStatus("current")

dIpmcExtMrouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 2, 2, 4)
)
dIpmcExtMrouteGroup.setObjects(
      *(("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtStaticMrouteRpfType"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtStaticMrouteRpfAddr"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtStaticMrouteRpfIfIndex"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtStaticMrouteRowStatus"))
)
if mibBuilder.loadTexts:
    dIpmcExtMrouteGroup.setStatus("current")

dIpmcExtCtrlPktCpuFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 2, 2, 5)
)
dIpmcExtCtrlPktCpuFilterGroup.setObjects(
      *(("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtCtrlPktCpuFilterV4Proto"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtCtrlPktCpuFilterV6Proto"))
)
if mibBuilder.loadTexts:
    dIpmcExtCtrlPktCpuFilterGroup.setStatus("current")

dIpmcExtCtrlPktReplacePriGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 2, 2, 6)
)
dIpmcExtCtrlPktReplacePriGroup.setObjects(
      *(("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtCtrlPktRepDscp"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtCtrlPktRepPriority"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtCtrlPktRepPriRowStatus"))
)
if mibBuilder.loadTexts:
    dIpmcExtCtrlPktReplacePriGroup.setStatus("current")

dIpmcExtRpfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 2, 2, 7)
)
dIpmcExtRpfGroup.setObjects(
      *(("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtRpfIfIndex"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtRpfNeighborAddr"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtRpfType"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtRpfMetricValid"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtRpfMetric"))
)
if mibBuilder.loadTexts:
    dIpmcExtRpfGroup.setStatus("current")

dIpmcExtOutgoingPortsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 2, 2, 8)
)
dIpmcExtOutgoingPortsInfoGroup.setObjects(
    ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtGrpOutgoingPort")
)
if mibBuilder.loadTexts:
    dIpmcExtOutgoingPortsInfoGroup.setStatus("current")

dIpmcExtIgmpStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 2, 2, 9)
)
dIpmcExtIgmpStatisticsGroup.setObjects(
      *(("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtIgmpPortIfV1RxReport"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtIgmpPortIfV1RxQuery"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtIgmpPortIfV1TxReport"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtIgmpPortIfV1TxQuery"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtIgmpPortIfV2RxReport"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtIgmpPortIfV2RxQuery"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtIgmpPortIfV2RxLeave"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtIgmpPortIfV2TxReport"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtIgmpPortIfV2TxQuery"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtIgmpPortIfV2TxLeave"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtIgmpPortIfV3RxReport"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtIgmpPortIfV3RxQuery"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtIgmpPortIfV3TxReport"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtIgmpPortIfV3TxQuery"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtIgmpPortIfRxUnknown"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtIgmpPortIfTxUnknown"))
)
if mibBuilder.loadTexts:
    dIpmcExtIgmpStatisticsGroup.setStatus("current")

dIpmcExtPimStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 2, 2, 10)
)
dIpmcExtPimStatisticsGroup.setObjects(
      *(("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtPimPortIfRxHello"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtPimPortIfTxHello"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtPimPortIfRxRegister"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtPimPortIfTxRegister"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtPimPortIfRxRegisterStop"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtPimPortIfTxRegisterStop"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtPimPortIfRxJoinPrune"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtPimPortIfTxJoinPrune"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtPimPortIfRxBootstrap"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtPimPortIfTxBootstrap"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtPimPortIfRxAssert"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtPimPortIfTxAssert"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtPimPortIfRxGraft"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtPimPortIfTxGraft"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtPimPortIfRxGraftAck"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtPimPortIfTxGraftAck"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtPimPortIfRxCRpAdv"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtPimPortIfTxCRpAdv"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtPimPortIfRxStateRefresh"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtPimPortIfTxStateRefresh"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtPimPortIfRxUnknown"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtPimPortIfTxUnknown"))
)
if mibBuilder.loadTexts:
    dIpmcExtPimStatisticsGroup.setStatus("current")

dIpmcExtDvmrpStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 2, 2, 11)
)
dIpmcExtDvmrpStatisticsGroup.setObjects(
      *(("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtDvmrpPortIfRxProbe"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtDvmrpPortIfTxProbe"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtDvmrpPortIfRxReport"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtDvmrpPortIfTxReport"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtDvmrpPortIfRxPrune"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtDvmrpPortIfTxPrune"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtDvmrpPortIfRxGraft"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtDvmrpPortIfTxGraft"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtDvmrpPortIfRxGraftAck"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtDvmrpPortIfTxGraftAck"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtDvmrpPortIfRxUnknown"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtDvmrpPortIfTxUnknown"))
)
if mibBuilder.loadTexts:
    dIpmcExtDvmrpStatisticsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dIpmcExtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 55, 2, 1, 1)
)
dIpmcExtCompliance.setObjects(
      *(("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtGeneralCtrlGroup"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtBoundaryGroup"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtMrouteGroup"),
        ("DLINKSW-IPMCAST-EXT-MIB", "dIpmcExtRpfGroup"))
)
if mibBuilder.loadTexts:
    dIpmcExtCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-IPMCAST-EXT-MIB",
    **{"dlinkSwIpMcastExtMIB": dlinkSwIpMcastExtMIB,
       "dIpmcExtNotifications": dIpmcExtNotifications,
       "dIpmcExtObjects": dIpmcExtObjects,
       "dIpmcExtMcastRouteEnabled": dIpmcExtMcastRouteEnabled,
       "dIpmcExtIpv4McastTableLookupMode": dIpmcExtIpv4McastTableLookupMode,
       "dIpmcExtClearStatisticsObjects": dIpmcExtClearStatisticsObjects,
       "dIpmcExtClearStatistics": dIpmcExtClearStatistics,
       "dIpmcExtBoundaryTable": dIpmcExtBoundaryTable,
       "dIpmcExtBoundaryEntry": dIpmcExtBoundaryEntry,
       "dIpmcExtBoundaryVersion": dIpmcExtBoundaryVersion,
       "dIpmcExtBoundaryIfIdx": dIpmcExtBoundaryIfIdx,
       "dIpmcExtBoundaryAccessList": dIpmcExtBoundaryAccessList,
       "dIpmcExtBoundaryApplyDirection": dIpmcExtBoundaryApplyDirection,
       "dIpmcExtBoundaryRowStatus": dIpmcExtBoundaryRowStatus,
       "dIpmcExtStaticMrouteTable": dIpmcExtStaticMrouteTable,
       "dIpmcExtStaticMrouteEntry": dIpmcExtStaticMrouteEntry,
       "dIpmcExtStaticMrouteSrcNetType": dIpmcExtStaticMrouteSrcNetType,
       "dIpmcExtStaticMrouteSrcNetAddr": dIpmcExtStaticMrouteSrcNetAddr,
       "dIpmcExtStaticMrouteSrcNetPreLen": dIpmcExtStaticMrouteSrcNetPreLen,
       "dIpmcExtStaticMrouteRpfType": dIpmcExtStaticMrouteRpfType,
       "dIpmcExtStaticMrouteRpfAddr": dIpmcExtStaticMrouteRpfAddr,
       "dIpmcExtStaticMrouteRpfIfIndex": dIpmcExtStaticMrouteRpfIfIndex,
       "dIpmcExtStaticMrouteRowStatus": dIpmcExtStaticMrouteRowStatus,
       "dIpmcExtCtrlPktCpuFilterTable": dIpmcExtCtrlPktCpuFilterTable,
       "dIpmcExtCtrlPktCpuFilterEntry": dIpmcExtCtrlPktCpuFilterEntry,
       "dIpmcExtCtrlPktCpuFilterIfIdx": dIpmcExtCtrlPktCpuFilterIfIdx,
       "dIpmcExtCtrlPktCpuFilterV4Proto": dIpmcExtCtrlPktCpuFilterV4Proto,
       "dIpmcExtCtrlPktCpuFilterV6Proto": dIpmcExtCtrlPktCpuFilterV6Proto,
       "dIpmcExtCtrlPktReplacePriTable": dIpmcExtCtrlPktReplacePriTable,
       "dIpmcExtCtrlPktReplacePriEntry": dIpmcExtCtrlPktReplacePriEntry,
       "dIpmcExtCtrlPktRepPriPotocol": dIpmcExtCtrlPktRepPriPotocol,
       "dIpmcExtCtrlPktRepDscp": dIpmcExtCtrlPktRepDscp,
       "dIpmcExtCtrlPktRepPriority": dIpmcExtCtrlPktRepPriority,
       "dIpmcExtCtrlPktRepPriRowStatus": dIpmcExtCtrlPktRepPriRowStatus,
       "dIpmcExtRpfTable": dIpmcExtRpfTable,
       "dIpmcExtRpfEntry": dIpmcExtRpfEntry,
       "dIpmcExtRpfAddrType": dIpmcExtRpfAddrType,
       "dIpmcExtRpfAddr": dIpmcExtRpfAddr,
       "dIpmcExtRpfRouteAddr": dIpmcExtRpfRouteAddr,
       "dIpmcExtRpfRoutePrefixLen": dIpmcExtRpfRoutePrefixLen,
       "dIpmcExtRpfIfIndex": dIpmcExtRpfIfIndex,
       "dIpmcExtRpfNeighborAddr": dIpmcExtRpfNeighborAddr,
       "dIpmcExtRpfType": dIpmcExtRpfType,
       "dIpmcExtRpfMetricValid": dIpmcExtRpfMetricValid,
       "dIpmcExtRpfMetric": dIpmcExtRpfMetric,
       "dIpmcExtGrpOutgoingPortTable": dIpmcExtGrpOutgoingPortTable,
       "dIpmcExtGrpOutgoingPortEntry": dIpmcExtGrpOutgoingPortEntry,
       "dIpmcExtGrpOutgoingAddrType": dIpmcExtGrpOutgoingAddrType,
       "dIpmcExtGrpOutgoingVlanIndex": dIpmcExtGrpOutgoingVlanIndex,
       "dIpmcExtGrpOutgoingGroupAddr": dIpmcExtGrpOutgoingGroupAddr,
       "dIpmcExtGrpOutgoingPfxLen": dIpmcExtGrpOutgoingPfxLen,
       "dIpmcExtGrpOutgoingSrcAddr": dIpmcExtGrpOutgoingSrcAddr,
       "dIpmcExtGrpOutgoingSrcPfxLen": dIpmcExtGrpOutgoingSrcPfxLen,
       "dIpmcExtGrpOutgoingPort": dIpmcExtGrpOutgoingPort,
       "dIpmcExtStatisticsObjects": dIpmcExtStatisticsObjects,
       "dIpmcExtIgmpPortIfStatTable": dIpmcExtIgmpPortIfStatTable,
       "dIpmcExtIgmpPortIfStatEntry": dIpmcExtIgmpPortIfStatEntry,
       "dIpmcExtIgmpPortIfIndex": dIpmcExtIgmpPortIfIndex,
       "dIpmcExtIgmpPortIfV1RxReport": dIpmcExtIgmpPortIfV1RxReport,
       "dIpmcExtIgmpPortIfV1RxQuery": dIpmcExtIgmpPortIfV1RxQuery,
       "dIpmcExtIgmpPortIfV1TxReport": dIpmcExtIgmpPortIfV1TxReport,
       "dIpmcExtIgmpPortIfV1TxQuery": dIpmcExtIgmpPortIfV1TxQuery,
       "dIpmcExtIgmpPortIfV2RxReport": dIpmcExtIgmpPortIfV2RxReport,
       "dIpmcExtIgmpPortIfV2RxQuery": dIpmcExtIgmpPortIfV2RxQuery,
       "dIpmcExtIgmpPortIfV2RxLeave": dIpmcExtIgmpPortIfV2RxLeave,
       "dIpmcExtIgmpPortIfV2TxReport": dIpmcExtIgmpPortIfV2TxReport,
       "dIpmcExtIgmpPortIfV2TxQuery": dIpmcExtIgmpPortIfV2TxQuery,
       "dIpmcExtIgmpPortIfV2TxLeave": dIpmcExtIgmpPortIfV2TxLeave,
       "dIpmcExtIgmpPortIfV3RxReport": dIpmcExtIgmpPortIfV3RxReport,
       "dIpmcExtIgmpPortIfV3RxQuery": dIpmcExtIgmpPortIfV3RxQuery,
       "dIpmcExtIgmpPortIfV3TxReport": dIpmcExtIgmpPortIfV3TxReport,
       "dIpmcExtIgmpPortIfV3TxQuery": dIpmcExtIgmpPortIfV3TxQuery,
       "dIpmcExtIgmpPortIfRxUnknown": dIpmcExtIgmpPortIfRxUnknown,
       "dIpmcExtIgmpPortIfTxUnknown": dIpmcExtIgmpPortIfTxUnknown,
       "dIpmcExtPimPortIfStatTable": dIpmcExtPimPortIfStatTable,
       "dIpmcExtPimPortIfStatEntry": dIpmcExtPimPortIfStatEntry,
       "dIpmcExtPimPortIfIndex": dIpmcExtPimPortIfIndex,
       "dIpmcExtPimPortIfVersion": dIpmcExtPimPortIfVersion,
       "dIpmcExtPimPortIfRxHello": dIpmcExtPimPortIfRxHello,
       "dIpmcExtPimPortIfTxHello": dIpmcExtPimPortIfTxHello,
       "dIpmcExtPimPortIfRxRegister": dIpmcExtPimPortIfRxRegister,
       "dIpmcExtPimPortIfTxRegister": dIpmcExtPimPortIfTxRegister,
       "dIpmcExtPimPortIfRxRegisterStop": dIpmcExtPimPortIfRxRegisterStop,
       "dIpmcExtPimPortIfTxRegisterStop": dIpmcExtPimPortIfTxRegisterStop,
       "dIpmcExtPimPortIfRxJoinPrune": dIpmcExtPimPortIfRxJoinPrune,
       "dIpmcExtPimPortIfTxJoinPrune": dIpmcExtPimPortIfTxJoinPrune,
       "dIpmcExtPimPortIfRxBootstrap": dIpmcExtPimPortIfRxBootstrap,
       "dIpmcExtPimPortIfTxBootstrap": dIpmcExtPimPortIfTxBootstrap,
       "dIpmcExtPimPortIfRxAssert": dIpmcExtPimPortIfRxAssert,
       "dIpmcExtPimPortIfTxAssert": dIpmcExtPimPortIfTxAssert,
       "dIpmcExtPimPortIfRxGraft": dIpmcExtPimPortIfRxGraft,
       "dIpmcExtPimPortIfTxGraft": dIpmcExtPimPortIfTxGraft,
       "dIpmcExtPimPortIfRxGraftAck": dIpmcExtPimPortIfRxGraftAck,
       "dIpmcExtPimPortIfTxGraftAck": dIpmcExtPimPortIfTxGraftAck,
       "dIpmcExtPimPortIfRxCRpAdv": dIpmcExtPimPortIfRxCRpAdv,
       "dIpmcExtPimPortIfTxCRpAdv": dIpmcExtPimPortIfTxCRpAdv,
       "dIpmcExtPimPortIfRxStateRefresh": dIpmcExtPimPortIfRxStateRefresh,
       "dIpmcExtPimPortIfTxStateRefresh": dIpmcExtPimPortIfTxStateRefresh,
       "dIpmcExtPimPortIfRxUnknown": dIpmcExtPimPortIfRxUnknown,
       "dIpmcExtPimPortIfTxUnknown": dIpmcExtPimPortIfTxUnknown,
       "dIpmcExtDvmrpPortIfStatTable": dIpmcExtDvmrpPortIfStatTable,
       "dIpmcExtDvmrpPortIfStatEntry": dIpmcExtDvmrpPortIfStatEntry,
       "dIpmcExtDvmrpPortIfIndex": dIpmcExtDvmrpPortIfIndex,
       "dIpmcExtDvmrpPortIfRxProbe": dIpmcExtDvmrpPortIfRxProbe,
       "dIpmcExtDvmrpPortIfTxProbe": dIpmcExtDvmrpPortIfTxProbe,
       "dIpmcExtDvmrpPortIfRxReport": dIpmcExtDvmrpPortIfRxReport,
       "dIpmcExtDvmrpPortIfTxReport": dIpmcExtDvmrpPortIfTxReport,
       "dIpmcExtDvmrpPortIfRxPrune": dIpmcExtDvmrpPortIfRxPrune,
       "dIpmcExtDvmrpPortIfTxPrune": dIpmcExtDvmrpPortIfTxPrune,
       "dIpmcExtDvmrpPortIfRxGraft": dIpmcExtDvmrpPortIfRxGraft,
       "dIpmcExtDvmrpPortIfTxGraft": dIpmcExtDvmrpPortIfTxGraft,
       "dIpmcExtDvmrpPortIfRxGraftAck": dIpmcExtDvmrpPortIfRxGraftAck,
       "dIpmcExtDvmrpPortIfTxGraftAck": dIpmcExtDvmrpPortIfTxGraftAck,
       "dIpmcExtDvmrpPortIfRxUnknown": dIpmcExtDvmrpPortIfRxUnknown,
       "dIpmcExtDvmrpPortIfTxUnknown": dIpmcExtDvmrpPortIfTxUnknown,
       "dIpmcExtConformance": dIpmcExtConformance,
       "dIpmcExtCompliances": dIpmcExtCompliances,
       "dIpmcExtCompliance": dIpmcExtCompliance,
       "dIpmcExtGroups": dIpmcExtGroups,
       "dIpmcExtClearStatisticsGroup": dIpmcExtClearStatisticsGroup,
       "dIpmcExtGeneralCtrlGroup": dIpmcExtGeneralCtrlGroup,
       "dIpmcExtBoundaryGroup": dIpmcExtBoundaryGroup,
       "dIpmcExtMrouteGroup": dIpmcExtMrouteGroup,
       "dIpmcExtCtrlPktCpuFilterGroup": dIpmcExtCtrlPktCpuFilterGroup,
       "dIpmcExtCtrlPktReplacePriGroup": dIpmcExtCtrlPktReplacePriGroup,
       "dIpmcExtRpfGroup": dIpmcExtRpfGroup,
       "dIpmcExtOutgoingPortsInfoGroup": dIpmcExtOutgoingPortsInfoGroup,
       "dIpmcExtIgmpStatisticsGroup": dIpmcExtIgmpStatisticsGroup,
       "dIpmcExtPimStatisticsGroup": dIpmcExtPimStatisticsGroup,
       "dIpmcExtDvmrpStatisticsGroup": dIpmcExtDvmrpStatisticsGroup}
)
