# SNMP MIB module (DLINKSW-IP-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-IP-EXT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:37:14 2025
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
 InetAddressIPv4,
 InetAddressIPv6,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv4",
    "InetAddressIPv6",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dlinkSwIpExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 75)
)
if mibBuilder.loadTexts:
    dlinkSwIpExtMIB.setRevisions(
        ("2013-08-06 00:00",
         "2013-08-29 00:00",
         "2013-09-18 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DIpExtMIBNotifications_ObjectIdentity = ObjectIdentity
dIpExtMIBNotifications = _DIpExtMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 0)
)
_DIpExtMIBObjects_ObjectIdentity = ObjectIdentity
dIpExtMIBObjects = _DIpExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1)
)
_DIpExtGenArpMgmt_ObjectIdentity = ObjectIdentity
dIpExtGenArpMgmt = _DIpExtGenArpMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 1)
)


class _DIpExtClearArpCacheAll_Type(Integer32):
    """Custom type dIpExtClearArpCacheAll based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("noOp", 2))
    )


_DIpExtClearArpCacheAll_Type.__name__ = "Integer32"
_DIpExtClearArpCacheAll_Object = MibScalar
dIpExtClearArpCacheAll = _DIpExtClearArpCacheAll_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 1, 1),
    _DIpExtClearArpCacheAll_Type()
)
dIpExtClearArpCacheAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dIpExtClearArpCacheAll.setStatus("current")
_DIpExtClearArpCacheByIf_Type = InterfaceIndexOrZero
_DIpExtClearArpCacheByIf_Object = MibScalar
dIpExtClearArpCacheByIf = _DIpExtClearArpCacheByIf_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 1, 2),
    _DIpExtClearArpCacheByIf_Type()
)
dIpExtClearArpCacheByIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dIpExtClearArpCacheByIf.setStatus("current")
_DIpExtTotalArpEntries_Type = Unsigned32
_DIpExtTotalArpEntries_Object = MibScalar
dIpExtTotalArpEntries = _DIpExtTotalArpEntries_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 1, 3),
    _DIpExtTotalArpEntries_Type()
)
dIpExtTotalArpEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpExtTotalArpEntries.setStatus("current")
_DIpExtGratuitousArpMgmt_ObjectIdentity = ObjectIdentity
dIpExtGratuitousArpMgmt = _DIpExtGratuitousArpMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 2)
)


class _DIpExtGratuitousARPSendRequestEnabled_Type(TruthValue):
    """Custom type dIpExtGratuitousARPSendRequestEnabled based on TruthValue"""
    defaultValue = 2


_DIpExtGratuitousARPSendRequestEnabled_Type.__name__ = "TruthValue"
_DIpExtGratuitousARPSendRequestEnabled_Object = MibScalar
dIpExtGratuitousARPSendRequestEnabled = _DIpExtGratuitousARPSendRequestEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 2, 1),
    _DIpExtGratuitousARPSendRequestEnabled_Type()
)
dIpExtGratuitousARPSendRequestEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dIpExtGratuitousARPSendRequestEnabled.setStatus("current")


class _DIpExtGratuitousARPLearningEnabled_Type(TruthValue):
    """Custom type dIpExtGratuitousARPLearningEnabled based on TruthValue"""
    defaultValue = 1


_DIpExtGratuitousARPLearningEnabled_Type.__name__ = "TruthValue"
_DIpExtGratuitousARPLearningEnabled_Object = MibScalar
dIpExtGratuitousARPLearningEnabled = _DIpExtGratuitousARPLearningEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 2, 2),
    _DIpExtGratuitousARPLearningEnabled_Type()
)
dIpExtGratuitousARPLearningEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dIpExtGratuitousARPLearningEnabled.setStatus("current")


class _DIpExtGratuitousARPDadReplyEnabled_Type(TruthValue):
    """Custom type dIpExtGratuitousARPDadReplyEnabled based on TruthValue"""
    defaultValue = 2


_DIpExtGratuitousARPDadReplyEnabled_Type.__name__ = "TruthValue"
_DIpExtGratuitousARPDadReplyEnabled_Object = MibScalar
dIpExtGratuitousARPDadReplyEnabled = _DIpExtGratuitousARPDadReplyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 2, 3),
    _DIpExtGratuitousARPDadReplyEnabled_Type()
)
dIpExtGratuitousARPDadReplyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dIpExtGratuitousARPDadReplyEnabled.setStatus("current")


class _DIpExtGratuitousARPTrapEnabled_Type(TruthValue):
    """Custom type dIpExtGratuitousARPTrapEnabled based on TruthValue"""
    defaultValue = 2


_DIpExtGratuitousARPTrapEnabled_Type.__name__ = "TruthValue"
_DIpExtGratuitousARPTrapEnabled_Object = MibScalar
dIpExtGratuitousARPTrapEnabled = _DIpExtGratuitousARPTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 2, 4),
    _DIpExtGratuitousARPTrapEnabled_Type()
)
dIpExtGratuitousARPTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dIpExtGratuitousARPTrapEnabled.setStatus("current")
_DIpExtGratuitousARPNotifyInfo_ObjectIdentity = ObjectIdentity
dIpExtGratuitousARPNotifyInfo = _DIpExtGratuitousARPNotifyInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 2, 5)
)
_DIpExtGratuitousARPIpAddr_Type = IpAddress
_DIpExtGratuitousARPIpAddr_Object = MibScalar
dIpExtGratuitousARPIpAddr = _DIpExtGratuitousARPIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 2, 5, 1),
    _DIpExtGratuitousARPIpAddr_Type()
)
dIpExtGratuitousARPIpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dIpExtGratuitousARPIpAddr.setStatus("current")
_DIpExtGratuitousARPMacAddr_Type = MacAddress
_DIpExtGratuitousARPMacAddr_Object = MibScalar
dIpExtGratuitousARPMacAddr = _DIpExtGratuitousARPMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 2, 5, 2),
    _DIpExtGratuitousARPMacAddr_Type()
)
dIpExtGratuitousARPMacAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dIpExtGratuitousARPMacAddr.setStatus("current")
_DIpExtGratuitousARPPortNumber_Type = DisplayString
_DIpExtGratuitousARPPortNumber_Object = MibScalar
dIpExtGratuitousARPPortNumber = _DIpExtGratuitousARPPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 2, 5, 3),
    _DIpExtGratuitousARPPortNumber_Type()
)
dIpExtGratuitousARPPortNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dIpExtGratuitousARPPortNumber.setStatus("current")
_DIpExtIpv6NeighborDiscoverMgmt_ObjectIdentity = ObjectIdentity
dIpExtIpv6NeighborDiscoverMgmt = _DIpExtIpv6NeighborDiscoverMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 3)
)


class _DIpExtClearAllIpv6Neighbors_Type(Integer32):
    """Custom type dIpExtClearAllIpv6Neighbors based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("noOp", 2))
    )


_DIpExtClearAllIpv6Neighbors_Type.__name__ = "Integer32"
_DIpExtClearAllIpv6Neighbors_Object = MibScalar
dIpExtClearAllIpv6Neighbors = _DIpExtClearAllIpv6Neighbors_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 3, 1),
    _DIpExtClearAllIpv6Neighbors_Type()
)
dIpExtClearAllIpv6Neighbors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dIpExtClearAllIpv6Neighbors.setStatus("current")
_DIpExtClearIpv6NeighborsByIf_Type = InterfaceIndexOrZero
_DIpExtClearIpv6NeighborsByIf_Object = MibScalar
dIpExtClearIpv6NeighborsByIf = _DIpExtClearIpv6NeighborsByIf_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 3, 2),
    _DIpExtClearIpv6NeighborsByIf_Type()
)
dIpExtClearIpv6NeighborsByIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dIpExtClearIpv6NeighborsByIf.setStatus("current")
_DIpExtTotalIpv6Neighbors_Type = Unsigned32
_DIpExtTotalIpv6Neighbors_Object = MibScalar
dIpExtTotalIpv6Neighbors = _DIpExtTotalIpv6Neighbors_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 3, 3),
    _DIpExtTotalIpv6Neighbors_Type()
)
dIpExtTotalIpv6Neighbors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpExtTotalIpv6Neighbors.setStatus("current")
_DIpExtInterfaceMgmt_ObjectIdentity = ObjectIdentity
dIpExtInterfaceMgmt = _DIpExtInterfaceMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 4)
)
_DIpExtIpIfTable_Object = MibTable
dIpExtIpIfTable = _DIpExtIpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 4, 1)
)
if mibBuilder.loadTexts:
    dIpExtIpIfTable.setStatus("current")
_DIpExtIpIfEntry_Object = MibTableRow
dIpExtIpIfEntry = _DIpExtIpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 4, 1, 1)
)
dIpExtIpIfEntry.setIndexNames(
    (0, "DLINKSW-IP-EXT-MIB", "dIpExtIpIfType"),
    (0, "DLINKSW-IP-EXT-MIB", "dIpExtIpIfNumber"),
)
if mibBuilder.loadTexts:
    dIpExtIpIfEntry.setStatus("current")


class _DIpExtIpIfType_Type(Integer32):
    """Custom type dIpExtIpIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loopback", 1),
          ("vlan", 2))
    )


_DIpExtIpIfType_Type.__name__ = "Integer32"
_DIpExtIpIfType_Object = MibTableColumn
dIpExtIpIfType = _DIpExtIpIfType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 4, 1, 1, 1),
    _DIpExtIpIfType_Type()
)
dIpExtIpIfType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dIpExtIpIfType.setStatus("current")


class _DIpExtIpIfNumber_Type(Unsigned32):
    """Custom type dIpExtIpIfNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DIpExtIpIfNumber_Type.__name__ = "Unsigned32"
_DIpExtIpIfNumber_Object = MibTableColumn
dIpExtIpIfNumber = _DIpExtIpIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 4, 1, 1, 2),
    _DIpExtIpIfNumber_Type()
)
dIpExtIpIfNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dIpExtIpIfNumber.setStatus("current")
_DIpExtIpIfIndex_Type = InterfaceIndex
_DIpExtIpIfIndex_Object = MibTableColumn
dIpExtIpIfIndex = _DIpExtIpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 4, 1, 1, 3),
    _DIpExtIpIfIndex_Type()
)
dIpExtIpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpExtIpIfIndex.setStatus("current")
_DIpExtIpIfRowStatus_Type = RowStatus
_DIpExtIpIfRowStatus_Object = MibTableColumn
dIpExtIpIfRowStatus = _DIpExtIpIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 4, 1, 1, 4),
    _DIpExtIpIfRowStatus_Type()
)
dIpExtIpIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dIpExtIpIfRowStatus.setStatus("current")
_DIpExtIfCfgTableNumber_Type = Unsigned32
_DIpExtIfCfgTableNumber_Object = MibScalar
dIpExtIfCfgTableNumber = _DIpExtIfCfgTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 4, 2),
    _DIpExtIfCfgTableNumber_Type()
)
dIpExtIfCfgTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpExtIfCfgTableNumber.setStatus("current")
_DIpExtIfCfgTable_Object = MibTable
dIpExtIfCfgTable = _DIpExtIfCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 4, 3)
)
if mibBuilder.loadTexts:
    dIpExtIfCfgTable.setStatus("current")
_DIpExtIfCfgEntry_Object = MibTableRow
dIpExtIfCfgEntry = _DIpExtIfCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 4, 3, 1)
)
dIpExtIfCfgEntry.setIndexNames(
    (0, "DLINKSW-IP-EXT-MIB", "dIpExtIfCfgIfIndex"),
)
if mibBuilder.loadTexts:
    dIpExtIfCfgEntry.setStatus("current")
_DIpExtIfCfgIfIndex_Type = InterfaceIndex
_DIpExtIfCfgIfIndex_Object = MibTableColumn
dIpExtIfCfgIfIndex = _DIpExtIfCfgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 4, 3, 1, 1),
    _DIpExtIfCfgIfIndex_Type()
)
dIpExtIfCfgIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dIpExtIfCfgIfIndex.setStatus("current")


class _DIpExtIfCfgDhcpEnabled_Type(TruthValue):
    """Custom type dIpExtIfCfgDhcpEnabled based on TruthValue"""
    defaultValue = 2


_DIpExtIfCfgDhcpEnabled_Type.__name__ = "TruthValue"
_DIpExtIfCfgDhcpEnabled_Object = MibTableColumn
dIpExtIfCfgDhcpEnabled = _DIpExtIfCfgDhcpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 4, 3, 1, 2),
    _DIpExtIfCfgDhcpEnabled_Type()
)
dIpExtIfCfgDhcpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dIpExtIfCfgDhcpEnabled.setStatus("current")


class _DIpExtIfCfgArpTimeout_Type(Unsigned32):
    """Custom type dIpExtIfCfgArpTimeout based on Unsigned32"""
    defaultValue = 240

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_DIpExtIfCfgArpTimeout_Type.__name__ = "Unsigned32"
_DIpExtIfCfgArpTimeout_Object = MibTableColumn
dIpExtIfCfgArpTimeout = _DIpExtIfCfgArpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 4, 3, 1, 3),
    _DIpExtIfCfgArpTimeout_Type()
)
dIpExtIfCfgArpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dIpExtIfCfgArpTimeout.setStatus("current")
if mibBuilder.loadTexts:
    dIpExtIfCfgArpTimeout.setUnits("minutes")


class _DIpExtIfCfgProxyArpEnabled_Type(TruthValue):
    """Custom type dIpExtIfCfgProxyArpEnabled based on TruthValue"""
    defaultValue = 2


_DIpExtIfCfgProxyArpEnabled_Type.__name__ = "TruthValue"
_DIpExtIfCfgProxyArpEnabled_Object = MibTableColumn
dIpExtIfCfgProxyArpEnabled = _DIpExtIfCfgProxyArpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 4, 3, 1, 4),
    _DIpExtIfCfgProxyArpEnabled_Type()
)
dIpExtIfCfgProxyArpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dIpExtIfCfgProxyArpEnabled.setStatus("current")


class _DIpExtIfCfgLocalProxyArpEnabled_Type(TruthValue):
    """Custom type dIpExtIfCfgLocalProxyArpEnabled based on TruthValue"""
    defaultValue = 2


_DIpExtIfCfgLocalProxyArpEnabled_Type.__name__ = "TruthValue"
_DIpExtIfCfgLocalProxyArpEnabled_Object = MibTableColumn
dIpExtIfCfgLocalProxyArpEnabled = _DIpExtIfCfgLocalProxyArpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 4, 3, 1, 5),
    _DIpExtIfCfgLocalProxyArpEnabled_Type()
)
dIpExtIfCfgLocalProxyArpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dIpExtIfCfgLocalProxyArpEnabled.setStatus("current")


class _DIpExtIfCfgDirectedBcastEnabled_Type(TruthValue):
    """Custom type dIpExtIfCfgDirectedBcastEnabled based on TruthValue"""
    defaultValue = 2


_DIpExtIfCfgDirectedBcastEnabled_Type.__name__ = "TruthValue"
_DIpExtIfCfgDirectedBcastEnabled_Object = MibTableColumn
dIpExtIfCfgDirectedBcastEnabled = _DIpExtIfCfgDirectedBcastEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 4, 3, 1, 6),
    _DIpExtIfCfgDirectedBcastEnabled_Type()
)
dIpExtIfCfgDirectedBcastEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dIpExtIfCfgDirectedBcastEnabled.setStatus("current")


class _DIpExtIfCfgDirectedBcastAcl_Type(DisplayString):
    """Custom type dIpExtIfCfgDirectedBcastAcl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DIpExtIfCfgDirectedBcastAcl_Type.__name__ = "DisplayString"
_DIpExtIfCfgDirectedBcastAcl_Object = MibTableColumn
dIpExtIfCfgDirectedBcastAcl = _DIpExtIfCfgDirectedBcastAcl_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 4, 3, 1, 7),
    _DIpExtIfCfgDirectedBcastAcl_Type()
)
dIpExtIfCfgDirectedBcastAcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dIpExtIfCfgDirectedBcastAcl.setStatus("current")


class _DIpExtIfCfgGratuitousARPSendInterval_Type(Unsigned32):
    """Custom type dIpExtIfCfgGratuitousARPSendInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 3600),
    )


_DIpExtIfCfgGratuitousARPSendInterval_Type.__name__ = "Unsigned32"
_DIpExtIfCfgGratuitousARPSendInterval_Object = MibTableColumn
dIpExtIfCfgGratuitousARPSendInterval = _DIpExtIfCfgGratuitousARPSendInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 4, 3, 1, 8),
    _DIpExtIfCfgGratuitousARPSendInterval_Type()
)
dIpExtIfCfgGratuitousARPSendInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dIpExtIfCfgGratuitousARPSendInterval.setStatus("current")
if mibBuilder.loadTexts:
    dIpExtIfCfgGratuitousARPSendInterval.setUnits("seconds")


class _DIpExtIfCfgIpMtu_Type(Unsigned32):
    """Custom type dIpExtIfCfgIpMtu based on Unsigned32"""
    defaultValue = 1500


_DIpExtIfCfgIpMtu_Type.__name__ = "Unsigned32"
_DIpExtIfCfgIpMtu_Object = MibTableColumn
dIpExtIfCfgIpMtu = _DIpExtIfCfgIpMtu_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 4, 3, 1, 9),
    _DIpExtIfCfgIpMtu_Type()
)
dIpExtIfCfgIpMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dIpExtIfCfgIpMtu.setStatus("current")


class _DIpExtIfCfgDADTransmits_Type(Unsigned32):
    """Custom type dIpExtIfCfgDADTransmits based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DIpExtIfCfgDADTransmits_Type.__name__ = "Unsigned32"
_DIpExtIfCfgDADTransmits_Object = MibTableColumn
dIpExtIfCfgDADTransmits = _DIpExtIfCfgDADTransmits_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 4, 3, 1, 10),
    _DIpExtIfCfgDADTransmits_Type()
)
dIpExtIfCfgDADTransmits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dIpExtIfCfgDADTransmits.setStatus("current")
_DIpExtIpAddressTable_Object = MibTable
dIpExtIpAddressTable = _DIpExtIpAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 4, 4)
)
if mibBuilder.loadTexts:
    dIpExtIpAddressTable.setStatus("current")
_DIpExtIpAddressEntry_Object = MibTableRow
dIpExtIpAddressEntry = _DIpExtIpAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 4, 4, 1)
)
dIpExtIpAddressEntry.setIndexNames(
    (0, "DLINKSW-IP-EXT-MIB", "dIpExtIpAddressType"),
    (0, "DLINKSW-IP-EXT-MIB", "dIpExtIpAddress"),
    (0, "DLINKSW-IP-EXT-MIB", "dIpExtIpAddressIfIndex"),
)
if mibBuilder.loadTexts:
    dIpExtIpAddressEntry.setStatus("current")
_DIpExtIpAddressType_Type = InetAddressType
_DIpExtIpAddressType_Object = MibTableColumn
dIpExtIpAddressType = _DIpExtIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 4, 4, 1, 1),
    _DIpExtIpAddressType_Type()
)
dIpExtIpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dIpExtIpAddressType.setStatus("current")


class _DIpExtIpAddress_Type(InetAddress):
    """Custom type dIpExtIpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_DIpExtIpAddress_Type.__name__ = "InetAddress"
_DIpExtIpAddress_Object = MibTableColumn
dIpExtIpAddress = _DIpExtIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 4, 4, 1, 2),
    _DIpExtIpAddress_Type()
)
dIpExtIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dIpExtIpAddress.setStatus("current")
_DIpExtIpAddressIfIndex_Type = InterfaceIndex
_DIpExtIpAddressIfIndex_Object = MibTableColumn
dIpExtIpAddressIfIndex = _DIpExtIpAddressIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 4, 4, 1, 3),
    _DIpExtIpAddressIfIndex_Type()
)
dIpExtIpAddressIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dIpExtIpAddressIfIndex.setStatus("current")
_DIpExtIpAddressPrefixLength_Type = InetAddressPrefixLength
_DIpExtIpAddressPrefixLength_Object = MibTableColumn
dIpExtIpAddressPrefixLength = _DIpExtIpAddressPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 4, 4, 1, 4),
    _DIpExtIpAddressPrefixLength_Type()
)
dIpExtIpAddressPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dIpExtIpAddressPrefixLength.setStatus("current")


class _DIpExtIpAddressCategory_Type(Integer32):
    """Custom type dIpExtIpAddressCategory based on Integer32"""
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
        *(("primary", 1),
          ("secondary", 2),
          ("linkLocal", 3),
          ("eui64", 4))
    )


_DIpExtIpAddressCategory_Type.__name__ = "Integer32"
_DIpExtIpAddressCategory_Object = MibTableColumn
dIpExtIpAddressCategory = _DIpExtIpAddressCategory_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 4, 4, 1, 5),
    _DIpExtIpAddressCategory_Type()
)
dIpExtIpAddressCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dIpExtIpAddressCategory.setStatus("current")
_DIpExtIpAddressRowStatus_Type = RowStatus
_DIpExtIpAddressRowStatus_Object = MibTableColumn
dIpExtIpAddressRowStatus = _DIpExtIpAddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 4, 4, 1, 6),
    _DIpExtIpAddressRowStatus_Type()
)
dIpExtIpAddressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dIpExtIpAddressRowStatus.setStatus("current")
_DIpExtIpAddrBaseGenPrefixTable_Object = MibTable
dIpExtIpAddrBaseGenPrefixTable = _DIpExtIpAddrBaseGenPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 4, 5)
)
if mibBuilder.loadTexts:
    dIpExtIpAddrBaseGenPrefixTable.setStatus("current")
_DIpExtIpAddrBaseGenPrefixEntry_Object = MibTableRow
dIpExtIpAddrBaseGenPrefixEntry = _DIpExtIpAddrBaseGenPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 4, 5, 1)
)
dIpExtIpAddrBaseGenPrefixEntry.setIndexNames(
    (0, "DLINKSW-IP-EXT-MIB", "dIpExtIpAddrBasePrefixIfIndex"),
    (0, "DLINKSW-IP-EXT-MIB", "dIpExtIpAddrBasePrefixName"),
)
if mibBuilder.loadTexts:
    dIpExtIpAddrBaseGenPrefixEntry.setStatus("current")
_DIpExtIpAddrBasePrefixIfIndex_Type = InterfaceIndex
_DIpExtIpAddrBasePrefixIfIndex_Object = MibTableColumn
dIpExtIpAddrBasePrefixIfIndex = _DIpExtIpAddrBasePrefixIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 4, 5, 1, 1),
    _DIpExtIpAddrBasePrefixIfIndex_Type()
)
dIpExtIpAddrBasePrefixIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dIpExtIpAddrBasePrefixIfIndex.setStatus("current")


class _DIpExtIpAddrBasePrefixName_Type(DisplayString):
    """Custom type dIpExtIpAddrBasePrefixName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DIpExtIpAddrBasePrefixName_Type.__name__ = "DisplayString"
_DIpExtIpAddrBasePrefixName_Object = MibTableColumn
dIpExtIpAddrBasePrefixName = _DIpExtIpAddrBasePrefixName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 4, 5, 1, 2),
    _DIpExtIpAddrBasePrefixName_Type()
)
dIpExtIpAddrBasePrefixName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dIpExtIpAddrBasePrefixName.setStatus("current")
_DIpExtIpAddrBasePrefixSubBits_Type = InetAddressIPv6
_DIpExtIpAddrBasePrefixSubBits_Object = MibTableColumn
dIpExtIpAddrBasePrefixSubBits = _DIpExtIpAddrBasePrefixSubBits_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 4, 5, 1, 3),
    _DIpExtIpAddrBasePrefixSubBits_Type()
)
dIpExtIpAddrBasePrefixSubBits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dIpExtIpAddrBasePrefixSubBits.setStatus("current")
_DIpExtIpAddrBasePrefixLength_Type = InetAddressPrefixLength
_DIpExtIpAddrBasePrefixLength_Object = MibTableColumn
dIpExtIpAddrBasePrefixLength = _DIpExtIpAddrBasePrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 4, 5, 1, 4),
    _DIpExtIpAddrBasePrefixLength_Type()
)
dIpExtIpAddrBasePrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dIpExtIpAddrBasePrefixLength.setStatus("current")
_DIpExtIpAddrBasePrefixRowStatus_Type = RowStatus
_DIpExtIpAddrBasePrefixRowStatus_Object = MibTableColumn
dIpExtIpAddrBasePrefixRowStatus = _DIpExtIpAddrBasePrefixRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 4, 5, 1, 5),
    _DIpExtIpAddrBasePrefixRowStatus_Type()
)
dIpExtIpAddrBasePrefixRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dIpExtIpAddrBasePrefixRowStatus.setStatus("current")
_DIpExtPrefixMgmt_ObjectIdentity = ObjectIdentity
dIpExtPrefixMgmt = _DIpExtPrefixMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 5)
)
_DIpExtIpv6GneralPrefixTable_Object = MibTable
dIpExtIpv6GneralPrefixTable = _DIpExtIpv6GneralPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 5, 1)
)
if mibBuilder.loadTexts:
    dIpExtIpv6GneralPrefixTable.setStatus("current")
_DIpExtIpv6GneralPrefixEntry_Object = MibTableRow
dIpExtIpv6GneralPrefixEntry = _DIpExtIpv6GneralPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 5, 1, 1)
)
dIpExtIpv6GneralPrefixEntry.setIndexNames(
    (0, "DLINKSW-IP-EXT-MIB", "dIpExtGneralPrefixName"),
)
if mibBuilder.loadTexts:
    dIpExtIpv6GneralPrefixEntry.setStatus("current")
_DIpExtGneralPrefixName_Type = DisplayString
_DIpExtGneralPrefixName_Object = MibTableColumn
dIpExtGneralPrefixName = _DIpExtGneralPrefixName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 5, 1, 1, 1),
    _DIpExtGneralPrefixName_Type()
)
dIpExtGneralPrefixName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dIpExtGneralPrefixName.setStatus("current")


class _DIpExtGneralPrefixType_Type(Integer32):
    """Custom type dIpExtGneralPrefixType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("ipv6ToIpv4", 2))
    )


_DIpExtGneralPrefixType_Type.__name__ = "Integer32"
_DIpExtGneralPrefixType_Object = MibTableColumn
dIpExtGneralPrefixType = _DIpExtGneralPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 5, 1, 1, 2),
    _DIpExtGneralPrefixType_Type()
)
dIpExtGneralPrefixType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dIpExtGneralPrefixType.setStatus("current")
_DIpExtGneralPrefix_Type = InetAddressIPv6
_DIpExtGneralPrefix_Object = MibTableColumn
dIpExtGneralPrefix = _DIpExtGneralPrefix_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 5, 1, 1, 3),
    _DIpExtGneralPrefix_Type()
)
dIpExtGneralPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dIpExtGneralPrefix.setStatus("current")
_DIpExtGneralPrefixLength_Type = InetAddressPrefixLength
_DIpExtGneralPrefixLength_Object = MibTableColumn
dIpExtGneralPrefixLength = _DIpExtGneralPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 5, 1, 1, 4),
    _DIpExtGneralPrefixLength_Type()
)
dIpExtGneralPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dIpExtGneralPrefixLength.setStatus("current")
_DIpExtGeneralPrefix6to4IfIndex_Type = InterfaceIndex
_DIpExtGeneralPrefix6to4IfIndex_Object = MibTableColumn
dIpExtGeneralPrefix6to4IfIndex = _DIpExtGeneralPrefix6to4IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 5, 1, 1, 5),
    _DIpExtGeneralPrefix6to4IfIndex_Type()
)
dIpExtGeneralPrefix6to4IfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dIpExtGeneralPrefix6to4IfIndex.setStatus("current")
_DIpExtGeneralPrefixRowStatus_Type = RowStatus
_DIpExtGeneralPrefixRowStatus_Object = MibTableColumn
dIpExtGeneralPrefixRowStatus = _DIpExtGeneralPrefixRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 5, 1, 1, 6),
    _DIpExtGeneralPrefixRowStatus_Type()
)
dIpExtGeneralPrefixRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dIpExtGeneralPrefixRowStatus.setStatus("current")
_DIpExtIpv6PrefixTable_Object = MibTable
dIpExtIpv6PrefixTable = _DIpExtIpv6PrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 5, 2)
)
if mibBuilder.loadTexts:
    dIpExtIpv6PrefixTable.setStatus("current")
_DIpExtIpv6PrefixEntry_Object = MibTableRow
dIpExtIpv6PrefixEntry = _DIpExtIpv6PrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 5, 2, 1)
)
dIpExtIpv6PrefixEntry.setIndexNames(
    (0, "DLINKSW-IP-EXT-MIB", "dIpExtIpv6PrefixIfIndex"),
    (0, "DLINKSW-IP-EXT-MIB", "dIpExtIpv6Prefix"),
    (0, "DLINKSW-IP-EXT-MIB", "dIpExtIpv6PrefixLength"),
)
if mibBuilder.loadTexts:
    dIpExtIpv6PrefixEntry.setStatus("current")
_DIpExtIpv6PrefixIfIndex_Type = InterfaceIndex
_DIpExtIpv6PrefixIfIndex_Object = MibTableColumn
dIpExtIpv6PrefixIfIndex = _DIpExtIpv6PrefixIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 5, 2, 1, 1),
    _DIpExtIpv6PrefixIfIndex_Type()
)
dIpExtIpv6PrefixIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dIpExtIpv6PrefixIfIndex.setStatus("current")
_DIpExtIpv6Prefix_Type = InetAddressIPv6
_DIpExtIpv6Prefix_Object = MibTableColumn
dIpExtIpv6Prefix = _DIpExtIpv6Prefix_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 5, 2, 1, 2),
    _DIpExtIpv6Prefix_Type()
)
dIpExtIpv6Prefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dIpExtIpv6Prefix.setStatus("current")
_DIpExtIpv6PrefixLength_Type = InetAddressPrefixLength
_DIpExtIpv6PrefixLength_Object = MibTableColumn
dIpExtIpv6PrefixLength = _DIpExtIpv6PrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 5, 2, 1, 3),
    _DIpExtIpv6PrefixLength_Type()
)
dIpExtIpv6PrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dIpExtIpv6PrefixLength.setStatus("current")


class _DIpExtIpv6PrefixValidLifetime_Type(Unsigned32):
    """Custom type dIpExtIpv6PrefixValidLifetime based on Unsigned32"""
    defaultValue = 2592000


_DIpExtIpv6PrefixValidLifetime_Type.__name__ = "Unsigned32"
_DIpExtIpv6PrefixValidLifetime_Object = MibTableColumn
dIpExtIpv6PrefixValidLifetime = _DIpExtIpv6PrefixValidLifetime_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 5, 2, 1, 4),
    _DIpExtIpv6PrefixValidLifetime_Type()
)
dIpExtIpv6PrefixValidLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dIpExtIpv6PrefixValidLifetime.setStatus("current")
if mibBuilder.loadTexts:
    dIpExtIpv6PrefixValidLifetime.setUnits("seconds")


class _DIpExtIpv6PrefixPreferLifetime_Type(Unsigned32):
    """Custom type dIpExtIpv6PrefixPreferLifetime based on Unsigned32"""
    defaultValue = 604800


_DIpExtIpv6PrefixPreferLifetime_Type.__name__ = "Unsigned32"
_DIpExtIpv6PrefixPreferLifetime_Object = MibTableColumn
dIpExtIpv6PrefixPreferLifetime = _DIpExtIpv6PrefixPreferLifetime_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 5, 2, 1, 5),
    _DIpExtIpv6PrefixPreferLifetime_Type()
)
dIpExtIpv6PrefixPreferLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dIpExtIpv6PrefixPreferLifetime.setStatus("current")
if mibBuilder.loadTexts:
    dIpExtIpv6PrefixPreferLifetime.setUnits("seconds")


class _DIpExtIpv6PrefixOnLinkFlag_Type(TruthValue):
    """Custom type dIpExtIpv6PrefixOnLinkFlag based on TruthValue"""
    defaultValue = 2


_DIpExtIpv6PrefixOnLinkFlag_Type.__name__ = "TruthValue"
_DIpExtIpv6PrefixOnLinkFlag_Object = MibTableColumn
dIpExtIpv6PrefixOnLinkFlag = _DIpExtIpv6PrefixOnLinkFlag_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 5, 2, 1, 6),
    _DIpExtIpv6PrefixOnLinkFlag_Type()
)
dIpExtIpv6PrefixOnLinkFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dIpExtIpv6PrefixOnLinkFlag.setStatus("current")


class _DIpExtIpv6PrefixAutonomousFlag_Type(TruthValue):
    """Custom type dIpExtIpv6PrefixAutonomousFlag based on TruthValue"""
    defaultValue = 1


_DIpExtIpv6PrefixAutonomousFlag_Type.__name__ = "TruthValue"
_DIpExtIpv6PrefixAutonomousFlag_Object = MibTableColumn
dIpExtIpv6PrefixAutonomousFlag = _DIpExtIpv6PrefixAutonomousFlag_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 5, 2, 1, 7),
    _DIpExtIpv6PrefixAutonomousFlag_Type()
)
dIpExtIpv6PrefixAutonomousFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dIpExtIpv6PrefixAutonomousFlag.setStatus("current")
_DIpExtIpv6PrefixRowStatus_Type = RowStatus
_DIpExtIpv6PrefixRowStatus_Object = MibTableColumn
dIpExtIpv6PrefixRowStatus = _DIpExtIpv6PrefixRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 5, 2, 1, 8),
    _DIpExtIpv6PrefixRowStatus_Type()
)
dIpExtIpv6PrefixRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dIpExtIpv6PrefixRowStatus.setStatus("current")
_DIpExtDhcpClientMgmt_ObjectIdentity = ObjectIdentity
dIpExtDhcpClientMgmt = _DIpExtDhcpClientMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 6)
)
_DIpExtDhcpClientIfTable_Object = MibTable
dIpExtDhcpClientIfTable = _DIpExtDhcpClientIfTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 6, 1)
)
if mibBuilder.loadTexts:
    dIpExtDhcpClientIfTable.setStatus("current")
_DIpExtDhcpClientIfEntry_Object = MibTableRow
dIpExtDhcpClientIfEntry = _DIpExtDhcpClientIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 6, 1, 1)
)
dIpExtDhcpClientIfEntry.setIndexNames(
    (0, "DLINKSW-IP-EXT-MIB", "dIpExtDhcpClientIfIndex"),
)
if mibBuilder.loadTexts:
    dIpExtDhcpClientIfEntry.setStatus("current")
_DIpExtDhcpClientIfIndex_Type = InterfaceIndex
_DIpExtDhcpClientIfIndex_Object = MibTableColumn
dIpExtDhcpClientIfIndex = _DIpExtDhcpClientIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 6, 1, 1, 1),
    _DIpExtDhcpClientIfIndex_Type()
)
dIpExtDhcpClientIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dIpExtDhcpClientIfIndex.setStatus("current")


class _DIpExtDhcpClientIfClassIdType_Type(Integer32):
    """Custom type dIpExtDhcpClientIfClassIdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 1),
          ("hex", 2))
    )


_DIpExtDhcpClientIfClassIdType_Type.__name__ = "Integer32"
_DIpExtDhcpClientIfClassIdType_Object = MibTableColumn
dIpExtDhcpClientIfClassIdType = _DIpExtDhcpClientIfClassIdType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 6, 1, 1, 2),
    _DIpExtDhcpClientIfClassIdType_Type()
)
dIpExtDhcpClientIfClassIdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dIpExtDhcpClientIfClassIdType.setStatus("current")


class _DIpExtDhcpClientIfClassIdValue_Type(DisplayString):
    """Custom type dIpExtDhcpClientIfClassIdValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_DIpExtDhcpClientIfClassIdValue_Type.__name__ = "DisplayString"
_DIpExtDhcpClientIfClassIdValue_Object = MibTableColumn
dIpExtDhcpClientIfClassIdValue = _DIpExtDhcpClientIfClassIdValue_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 6, 1, 1, 3),
    _DIpExtDhcpClientIfClassIdValue_Type()
)
dIpExtDhcpClientIfClassIdValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dIpExtDhcpClientIfClassIdValue.setStatus("current")
_DIpExtDhcpClientIfClientIdIfIdx_Type = InterfaceIndex
_DIpExtDhcpClientIfClientIdIfIdx_Object = MibTableColumn
dIpExtDhcpClientIfClientIdIfIdx = _DIpExtDhcpClientIfClientIdIfIdx_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 6, 1, 1, 4),
    _DIpExtDhcpClientIfClientIdIfIdx_Type()
)
dIpExtDhcpClientIfClientIdIfIdx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dIpExtDhcpClientIfClientIdIfIdx.setStatus("current")


class _DIpExtDhcpClientIfHostName_Type(DisplayString):
    """Custom type dIpExtDhcpClientIfHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_DIpExtDhcpClientIfHostName_Type.__name__ = "DisplayString"
_DIpExtDhcpClientIfHostName_Object = MibTableColumn
dIpExtDhcpClientIfHostName = _DIpExtDhcpClientIfHostName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 6, 1, 1, 5),
    _DIpExtDhcpClientIfHostName_Type()
)
dIpExtDhcpClientIfHostName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dIpExtDhcpClientIfHostName.setStatus("current")


class _DIpExtDhcpClientIfLeaseDay_Type(Integer32):
    """Custom type dIpExtDhcpClientIfLeaseDay based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 10000),
    )


_DIpExtDhcpClientIfLeaseDay_Type.__name__ = "Integer32"
_DIpExtDhcpClientIfLeaseDay_Object = MibTableColumn
dIpExtDhcpClientIfLeaseDay = _DIpExtDhcpClientIfLeaseDay_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 6, 1, 1, 6),
    _DIpExtDhcpClientIfLeaseDay_Type()
)
dIpExtDhcpClientIfLeaseDay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dIpExtDhcpClientIfLeaseDay.setStatus("current")


class _DIpExtDhcpClientIfLeaseHour_Type(Unsigned32):
    """Custom type dIpExtDhcpClientIfLeaseHour based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_DIpExtDhcpClientIfLeaseHour_Type.__name__ = "Unsigned32"
_DIpExtDhcpClientIfLeaseHour_Object = MibTableColumn
dIpExtDhcpClientIfLeaseHour = _DIpExtDhcpClientIfLeaseHour_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 6, 1, 1, 7),
    _DIpExtDhcpClientIfLeaseHour_Type()
)
dIpExtDhcpClientIfLeaseHour.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dIpExtDhcpClientIfLeaseHour.setStatus("current")


class _DIpExtDhcpClientIfLeaseMinute_Type(Unsigned32):
    """Custom type dIpExtDhcpClientIfLeaseMinute based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_DIpExtDhcpClientIfLeaseMinute_Type.__name__ = "Unsigned32"
_DIpExtDhcpClientIfLeaseMinute_Object = MibTableColumn
dIpExtDhcpClientIfLeaseMinute = _DIpExtDhcpClientIfLeaseMinute_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 6, 1, 1, 8),
    _DIpExtDhcpClientIfLeaseMinute_Type()
)
dIpExtDhcpClientIfLeaseMinute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dIpExtDhcpClientIfLeaseMinute.setStatus("current")


class _DIpExtDhcpClientAutoconfig_Type(Integer32):
    """Custom type dIpExtDhcpClientAutoconfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_DIpExtDhcpClientAutoconfig_Type.__name__ = "Integer32"
_DIpExtDhcpClientAutoconfig_Object = MibScalar
dIpExtDhcpClientAutoconfig = _DIpExtDhcpClientAutoconfig_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 6, 2),
    _DIpExtDhcpClientAutoconfig_Type()
)
dIpExtDhcpClientAutoconfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dIpExtDhcpClientAutoconfig.setStatus("current")
_DIpExtUdpForwardMgmt_ObjectIdentity = ObjectIdentity
dIpExtUdpForwardMgmt = _DIpExtUdpForwardMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 7)
)
_DIpExtUdpFwdPortTable_Object = MibTable
dIpExtUdpFwdPortTable = _DIpExtUdpFwdPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 7, 1)
)
if mibBuilder.loadTexts:
    dIpExtUdpFwdPortTable.setStatus("current")
_DIpExtUdpFwdPortEntry_Object = MibTableRow
dIpExtUdpFwdPortEntry = _DIpExtUdpFwdPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 7, 1, 1)
)
dIpExtUdpFwdPortEntry.setIndexNames(
    (0, "DLINKSW-IP-EXT-MIB", "dIpExtUdpFwdPortNumber"),
)
if mibBuilder.loadTexts:
    dIpExtUdpFwdPortEntry.setStatus("current")
_DIpExtUdpFwdPortNumber_Type = InetPortNumber
_DIpExtUdpFwdPortNumber_Object = MibTableColumn
dIpExtUdpFwdPortNumber = _DIpExtUdpFwdPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 7, 1, 1, 1),
    _DIpExtUdpFwdPortNumber_Type()
)
dIpExtUdpFwdPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dIpExtUdpFwdPortNumber.setStatus("current")
_DIpExtUdpFwdPortRowStatus_Type = RowStatus
_DIpExtUdpFwdPortRowStatus_Object = MibTableColumn
dIpExtUdpFwdPortRowStatus = _DIpExtUdpFwdPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 7, 1, 1, 2),
    _DIpExtUdpFwdPortRowStatus_Type()
)
dIpExtUdpFwdPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dIpExtUdpFwdPortRowStatus.setStatus("current")
_DIpExtUdpHelperAddrTable_Object = MibTable
dIpExtUdpHelperAddrTable = _DIpExtUdpHelperAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 7, 2)
)
if mibBuilder.loadTexts:
    dIpExtUdpHelperAddrTable.setStatus("current")
_DIpExtUdpHelperAddrEntry_Object = MibTableRow
dIpExtUdpHelperAddrEntry = _DIpExtUdpHelperAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 7, 2, 1)
)
dIpExtUdpHelperAddrEntry.setIndexNames(
    (0, "DLINKSW-IP-EXT-MIB", "dIpExtUdpHelperIfIndex"),
    (0, "DLINKSW-IP-EXT-MIB", "dIpExtUdpHelperAddrType"),
    (0, "DLINKSW-IP-EXT-MIB", "dIpExtUdpHelperAddr"),
)
if mibBuilder.loadTexts:
    dIpExtUdpHelperAddrEntry.setStatus("current")
_DIpExtUdpHelperIfIndex_Type = InterfaceIndex
_DIpExtUdpHelperIfIndex_Object = MibTableColumn
dIpExtUdpHelperIfIndex = _DIpExtUdpHelperIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 7, 2, 1, 1),
    _DIpExtUdpHelperIfIndex_Type()
)
dIpExtUdpHelperIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dIpExtUdpHelperIfIndex.setStatus("current")
_DIpExtUdpHelperAddrType_Type = InetAddressType
_DIpExtUdpHelperAddrType_Object = MibTableColumn
dIpExtUdpHelperAddrType = _DIpExtUdpHelperAddrType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 7, 2, 1, 2),
    _DIpExtUdpHelperAddrType_Type()
)
dIpExtUdpHelperAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dIpExtUdpHelperAddrType.setStatus("current")
_DIpExtUdpHelperAddr_Type = InetAddress
_DIpExtUdpHelperAddr_Object = MibTableColumn
dIpExtUdpHelperAddr = _DIpExtUdpHelperAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 7, 2, 1, 3),
    _DIpExtUdpHelperAddr_Type()
)
dIpExtUdpHelperAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dIpExtUdpHelperAddr.setStatus("current")
_DIpExtUdpHelperAddrRowStatus_Type = RowStatus
_DIpExtUdpHelperAddrRowStatus_Object = MibTableColumn
dIpExtUdpHelperAddrRowStatus = _DIpExtUdpHelperAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 1, 7, 2, 1, 4),
    _DIpExtUdpHelperAddrRowStatus_Type()
)
dIpExtUdpHelperAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dIpExtUdpHelperAddrRowStatus.setStatus("current")
_DIpExtMIBConformance_ObjectIdentity = ObjectIdentity
dIpExtMIBConformance = _DIpExtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 2)
)
_DIpExtCompliances_ObjectIdentity = ObjectIdentity
dIpExtCompliances = _DIpExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 2, 1)
)
_DIpExtGroups_ObjectIdentity = ObjectIdentity
dIpExtGroups = _DIpExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 2, 2)
)

# Managed Objects groups

dIpExtBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 2, 2, 1)
)
dIpExtBasicGroup.setObjects(
      *(("DLINKSW-IP-EXT-MIB", "dIpExtClearArpCacheAll"),
        ("DLINKSW-IP-EXT-MIB", "dIpExtClearArpCacheByIf"),
        ("DLINKSW-IP-EXT-MIB", "dIpExtTotalArpEntries"),
        ("DLINKSW-IP-EXT-MIB", "dIpExtIpIfIndex"),
        ("DLINKSW-IP-EXT-MIB", "dIpExtIpIfRowStatus"),
        ("DLINKSW-IP-EXT-MIB", "dIpExtIfCfgTableNumber"),
        ("DLINKSW-IP-EXT-MIB", "dIpExtIfCfgDhcpEnabled"),
        ("DLINKSW-IP-EXT-MIB", "dIpExtIfCfgArpTimeout"),
        ("DLINKSW-IP-EXT-MIB", "dIpExtIfCfgIpMtu"),
        ("DLINKSW-IP-EXT-MIB", "dIpExtIpAddressPrefixLength"),
        ("DLINKSW-IP-EXT-MIB", "dIpExtIpAddressCategory"),
        ("DLINKSW-IP-EXT-MIB", "dIpExtIpAddressRowStatus"))
)
if mibBuilder.loadTexts:
    dIpExtBasicGroup.setStatus("current")

dIpExtBasicIpv6OnlyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 2, 2, 2)
)
dIpExtBasicIpv6OnlyGroup.setObjects(
      *(("DLINKSW-IP-EXT-MIB", "dIpExtClearAllIpv6Neighbors"),
        ("DLINKSW-IP-EXT-MIB", "dIpExtClearIpv6NeighborsByIf"),
        ("DLINKSW-IP-EXT-MIB", "dIpExtTotalIpv6Neighbors"),
        ("DLINKSW-IP-EXT-MIB", "dIpExtIfCfgDADTransmits"))
)
if mibBuilder.loadTexts:
    dIpExtBasicIpv6OnlyGroup.setStatus("current")

dIpExtGeneralPrefixGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 2, 2, 3)
)
dIpExtGeneralPrefixGroup.setObjects(
      *(("DLINKSW-IP-EXT-MIB", "dIpExtIpAddrBasePrefixSubBits"),
        ("DLINKSW-IP-EXT-MIB", "dIpExtIpAddrBasePrefixLength"),
        ("DLINKSW-IP-EXT-MIB", "dIpExtIpAddrBasePrefixRowStatus"),
        ("DLINKSW-IP-EXT-MIB", "dIpExtGneralPrefixType"),
        ("DLINKSW-IP-EXT-MIB", "dIpExtGneralPrefix"),
        ("DLINKSW-IP-EXT-MIB", "dIpExtGneralPrefixLength"),
        ("DLINKSW-IP-EXT-MIB", "dIpExtGeneralPrefix6to4IfIndex"),
        ("DLINKSW-IP-EXT-MIB", "dIpExtGeneralPrefixRowStatus"))
)
if mibBuilder.loadTexts:
    dIpExtGeneralPrefixGroup.setStatus("current")

dIpExtRaPrefixGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 2, 2, 4)
)
dIpExtRaPrefixGroup.setObjects(
      *(("DLINKSW-IP-EXT-MIB", "dIpExtIpv6Prefix"),
        ("DLINKSW-IP-EXT-MIB", "dIpExtIpv6PrefixLength"),
        ("DLINKSW-IP-EXT-MIB", "dIpExtIpv6PrefixValidLifetime"),
        ("DLINKSW-IP-EXT-MIB", "dIpExtIpv6PrefixPreferLifetime"),
        ("DLINKSW-IP-EXT-MIB", "dIpExtIpv6PrefixOnLinkFlag"),
        ("DLINKSW-IP-EXT-MIB", "dIpExtIpv6PrefixAutonomousFlag"),
        ("DLINKSW-IP-EXT-MIB", "dIpExtIpv6PrefixRowStatus"))
)
if mibBuilder.loadTexts:
    dIpExtRaPrefixGroup.setStatus("current")

dIpExtGratuitousArpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 2, 2, 5)
)
dIpExtGratuitousArpGroup.setObjects(
      *(("DLINKSW-IP-EXT-MIB", "dIpExtIfCfgGratuitousARPSendInterval"),
        ("DLINKSW-IP-EXT-MIB", "dIpExtGratuitousARPSendRequestEnabled"),
        ("DLINKSW-IP-EXT-MIB", "dIpExtGratuitousARPLearningEnabled"))
)
if mibBuilder.loadTexts:
    dIpExtGratuitousArpGroup.setStatus("current")

dIpExtProxyArpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 2, 2, 6)
)
dIpExtProxyArpGroup.setObjects(
      *(("DLINKSW-IP-EXT-MIB", "dIpExtIfCfgProxyArpEnabled"),
        ("DLINKSW-IP-EXT-MIB", "dIpExtIfCfgLocalProxyArpEnabled"))
)
if mibBuilder.loadTexts:
    dIpExtProxyArpGroup.setStatus("current")

dIpExtDirectedBroadcastGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 2, 2, 7)
)
dIpExtDirectedBroadcastGroup.setObjects(
      *(("DLINKSW-IP-EXT-MIB", "dIpExtIfCfgDirectedBcastEnabled"),
        ("DLINKSW-IP-EXT-MIB", "dIpExtIfCfgDirectedBcastAcl"))
)
if mibBuilder.loadTexts:
    dIpExtDirectedBroadcastGroup.setStatus("current")

dIpExtDhcpClientGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 2, 2, 8)
)
dIpExtDhcpClientGroup.setObjects(
      *(("DLINKSW-IP-EXT-MIB", "dIpExtDhcpClientIfClassIdType"),
        ("DLINKSW-IP-EXT-MIB", "dIpExtDhcpClientIfClassIdValue"),
        ("DLINKSW-IP-EXT-MIB", "dIpExtDhcpClientIfClientIdIfIdx"),
        ("DLINKSW-IP-EXT-MIB", "dIpExtDhcpClientIfHostName"),
        ("DLINKSW-IP-EXT-MIB", "dIpExtDhcpClientIfLeaseDay"),
        ("DLINKSW-IP-EXT-MIB", "dIpExtDhcpClientIfLeaseHour"),
        ("DLINKSW-IP-EXT-MIB", "dIpExtDhcpClientIfLeaseMinute"))
)
if mibBuilder.loadTexts:
    dIpExtDhcpClientGroup.setStatus("current")

dIpExtUdpForwardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 2, 2, 9)
)
dIpExtUdpForwardGroup.setObjects(
      *(("DLINKSW-IP-EXT-MIB", "dIpExtUdpFwdPortRowStatus"),
        ("DLINKSW-IP-EXT-MIB", "dIpExtUdpHelperAddrRowStatus"))
)
if mibBuilder.loadTexts:
    dIpExtUdpForwardGroup.setStatus("current")


# Notification objects

dIpExtGratuitousARPTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 0, 1)
)
dIpExtGratuitousARPTrap.setObjects(
      *(("DLINKSW-IP-EXT-MIB", "dIpExtGratuitousARPIpAddr"),
        ("DLINKSW-IP-EXT-MIB", "dIpExtGratuitousARPMacAddr"),
        ("DLINKSW-IP-EXT-MIB", "dIpExtGratuitousARPPortNumber"),
        ("DLINKSW-IP-EXT-MIB", "dIpExtIfCfgIfIndex"))
)
if mibBuilder.loadTexts:
    dIpExtGratuitousARPTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

dIpExtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 75, 2, 1, 1)
)
dIpExtCompliance.setObjects(
      *(("DLINKSW-IP-EXT-MIB", "dIpExtBasicGroup"),
        ("DLINKSW-IP-EXT-MIB", "dIpExtBasicIpv6OnlyGroup"),
        ("DLINKSW-IP-EXT-MIB", "dIpExtGeneralPrefixGroup"),
        ("DLINKSW-IP-EXT-MIB", "dIpExtGratuitousArpGroup"),
        ("DLINKSW-IP-EXT-MIB", "dIpExtProxyArpGroup"),
        ("DLINKSW-IP-EXT-MIB", "dIpExtDirectedBroadcastGroup"),
        ("DLINKSW-IP-EXT-MIB", "dIpExtDhcpClientGroup"),
        ("DLINKSW-IP-EXT-MIB", "dIpExtUdpForwardGroup"))
)
if mibBuilder.loadTexts:
    dIpExtCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-IP-EXT-MIB",
    **{"dlinkSwIpExtMIB": dlinkSwIpExtMIB,
       "dIpExtMIBNotifications": dIpExtMIBNotifications,
       "dIpExtGratuitousARPTrap": dIpExtGratuitousARPTrap,
       "dIpExtMIBObjects": dIpExtMIBObjects,
       "dIpExtGenArpMgmt": dIpExtGenArpMgmt,
       "dIpExtClearArpCacheAll": dIpExtClearArpCacheAll,
       "dIpExtClearArpCacheByIf": dIpExtClearArpCacheByIf,
       "dIpExtTotalArpEntries": dIpExtTotalArpEntries,
       "dIpExtGratuitousArpMgmt": dIpExtGratuitousArpMgmt,
       "dIpExtGratuitousARPSendRequestEnabled": dIpExtGratuitousARPSendRequestEnabled,
       "dIpExtGratuitousARPLearningEnabled": dIpExtGratuitousARPLearningEnabled,
       "dIpExtGratuitousARPDadReplyEnabled": dIpExtGratuitousARPDadReplyEnabled,
       "dIpExtGratuitousARPTrapEnabled": dIpExtGratuitousARPTrapEnabled,
       "dIpExtGratuitousARPNotifyInfo": dIpExtGratuitousARPNotifyInfo,
       "dIpExtGratuitousARPIpAddr": dIpExtGratuitousARPIpAddr,
       "dIpExtGratuitousARPMacAddr": dIpExtGratuitousARPMacAddr,
       "dIpExtGratuitousARPPortNumber": dIpExtGratuitousARPPortNumber,
       "dIpExtIpv6NeighborDiscoverMgmt": dIpExtIpv6NeighborDiscoverMgmt,
       "dIpExtClearAllIpv6Neighbors": dIpExtClearAllIpv6Neighbors,
       "dIpExtClearIpv6NeighborsByIf": dIpExtClearIpv6NeighborsByIf,
       "dIpExtTotalIpv6Neighbors": dIpExtTotalIpv6Neighbors,
       "dIpExtInterfaceMgmt": dIpExtInterfaceMgmt,
       "dIpExtIpIfTable": dIpExtIpIfTable,
       "dIpExtIpIfEntry": dIpExtIpIfEntry,
       "dIpExtIpIfType": dIpExtIpIfType,
       "dIpExtIpIfNumber": dIpExtIpIfNumber,
       "dIpExtIpIfIndex": dIpExtIpIfIndex,
       "dIpExtIpIfRowStatus": dIpExtIpIfRowStatus,
       "dIpExtIfCfgTableNumber": dIpExtIfCfgTableNumber,
       "dIpExtIfCfgTable": dIpExtIfCfgTable,
       "dIpExtIfCfgEntry": dIpExtIfCfgEntry,
       "dIpExtIfCfgIfIndex": dIpExtIfCfgIfIndex,
       "dIpExtIfCfgDhcpEnabled": dIpExtIfCfgDhcpEnabled,
       "dIpExtIfCfgArpTimeout": dIpExtIfCfgArpTimeout,
       "dIpExtIfCfgProxyArpEnabled": dIpExtIfCfgProxyArpEnabled,
       "dIpExtIfCfgLocalProxyArpEnabled": dIpExtIfCfgLocalProxyArpEnabled,
       "dIpExtIfCfgDirectedBcastEnabled": dIpExtIfCfgDirectedBcastEnabled,
       "dIpExtIfCfgDirectedBcastAcl": dIpExtIfCfgDirectedBcastAcl,
       "dIpExtIfCfgGratuitousARPSendInterval": dIpExtIfCfgGratuitousARPSendInterval,
       "dIpExtIfCfgIpMtu": dIpExtIfCfgIpMtu,
       "dIpExtIfCfgDADTransmits": dIpExtIfCfgDADTransmits,
       "dIpExtIpAddressTable": dIpExtIpAddressTable,
       "dIpExtIpAddressEntry": dIpExtIpAddressEntry,
       "dIpExtIpAddressType": dIpExtIpAddressType,
       "dIpExtIpAddress": dIpExtIpAddress,
       "dIpExtIpAddressIfIndex": dIpExtIpAddressIfIndex,
       "dIpExtIpAddressPrefixLength": dIpExtIpAddressPrefixLength,
       "dIpExtIpAddressCategory": dIpExtIpAddressCategory,
       "dIpExtIpAddressRowStatus": dIpExtIpAddressRowStatus,
       "dIpExtIpAddrBaseGenPrefixTable": dIpExtIpAddrBaseGenPrefixTable,
       "dIpExtIpAddrBaseGenPrefixEntry": dIpExtIpAddrBaseGenPrefixEntry,
       "dIpExtIpAddrBasePrefixIfIndex": dIpExtIpAddrBasePrefixIfIndex,
       "dIpExtIpAddrBasePrefixName": dIpExtIpAddrBasePrefixName,
       "dIpExtIpAddrBasePrefixSubBits": dIpExtIpAddrBasePrefixSubBits,
       "dIpExtIpAddrBasePrefixLength": dIpExtIpAddrBasePrefixLength,
       "dIpExtIpAddrBasePrefixRowStatus": dIpExtIpAddrBasePrefixRowStatus,
       "dIpExtPrefixMgmt": dIpExtPrefixMgmt,
       "dIpExtIpv6GneralPrefixTable": dIpExtIpv6GneralPrefixTable,
       "dIpExtIpv6GneralPrefixEntry": dIpExtIpv6GneralPrefixEntry,
       "dIpExtGneralPrefixName": dIpExtGneralPrefixName,
       "dIpExtGneralPrefixType": dIpExtGneralPrefixType,
       "dIpExtGneralPrefix": dIpExtGneralPrefix,
       "dIpExtGneralPrefixLength": dIpExtGneralPrefixLength,
       "dIpExtGeneralPrefix6to4IfIndex": dIpExtGeneralPrefix6to4IfIndex,
       "dIpExtGeneralPrefixRowStatus": dIpExtGeneralPrefixRowStatus,
       "dIpExtIpv6PrefixTable": dIpExtIpv6PrefixTable,
       "dIpExtIpv6PrefixEntry": dIpExtIpv6PrefixEntry,
       "dIpExtIpv6PrefixIfIndex": dIpExtIpv6PrefixIfIndex,
       "dIpExtIpv6Prefix": dIpExtIpv6Prefix,
       "dIpExtIpv6PrefixLength": dIpExtIpv6PrefixLength,
       "dIpExtIpv6PrefixValidLifetime": dIpExtIpv6PrefixValidLifetime,
       "dIpExtIpv6PrefixPreferLifetime": dIpExtIpv6PrefixPreferLifetime,
       "dIpExtIpv6PrefixOnLinkFlag": dIpExtIpv6PrefixOnLinkFlag,
       "dIpExtIpv6PrefixAutonomousFlag": dIpExtIpv6PrefixAutonomousFlag,
       "dIpExtIpv6PrefixRowStatus": dIpExtIpv6PrefixRowStatus,
       "dIpExtDhcpClientMgmt": dIpExtDhcpClientMgmt,
       "dIpExtDhcpClientIfTable": dIpExtDhcpClientIfTable,
       "dIpExtDhcpClientIfEntry": dIpExtDhcpClientIfEntry,
       "dIpExtDhcpClientIfIndex": dIpExtDhcpClientIfIndex,
       "dIpExtDhcpClientIfClassIdType": dIpExtDhcpClientIfClassIdType,
       "dIpExtDhcpClientIfClassIdValue": dIpExtDhcpClientIfClassIdValue,
       "dIpExtDhcpClientIfClientIdIfIdx": dIpExtDhcpClientIfClientIdIfIdx,
       "dIpExtDhcpClientIfHostName": dIpExtDhcpClientIfHostName,
       "dIpExtDhcpClientIfLeaseDay": dIpExtDhcpClientIfLeaseDay,
       "dIpExtDhcpClientIfLeaseHour": dIpExtDhcpClientIfLeaseHour,
       "dIpExtDhcpClientIfLeaseMinute": dIpExtDhcpClientIfLeaseMinute,
       "dIpExtDhcpClientAutoconfig": dIpExtDhcpClientAutoconfig,
       "dIpExtUdpForwardMgmt": dIpExtUdpForwardMgmt,
       "dIpExtUdpFwdPortTable": dIpExtUdpFwdPortTable,
       "dIpExtUdpFwdPortEntry": dIpExtUdpFwdPortEntry,
       "dIpExtUdpFwdPortNumber": dIpExtUdpFwdPortNumber,
       "dIpExtUdpFwdPortRowStatus": dIpExtUdpFwdPortRowStatus,
       "dIpExtUdpHelperAddrTable": dIpExtUdpHelperAddrTable,
       "dIpExtUdpHelperAddrEntry": dIpExtUdpHelperAddrEntry,
       "dIpExtUdpHelperIfIndex": dIpExtUdpHelperIfIndex,
       "dIpExtUdpHelperAddrType": dIpExtUdpHelperAddrType,
       "dIpExtUdpHelperAddr": dIpExtUdpHelperAddr,
       "dIpExtUdpHelperAddrRowStatus": dIpExtUdpHelperAddrRowStatus,
       "dIpExtMIBConformance": dIpExtMIBConformance,
       "dIpExtCompliances": dIpExtCompliances,
       "dIpExtCompliance": dIpExtCompliance,
       "dIpExtGroups": dIpExtGroups,
       "dIpExtBasicGroup": dIpExtBasicGroup,
       "dIpExtBasicIpv6OnlyGroup": dIpExtBasicIpv6OnlyGroup,
       "dIpExtGeneralPrefixGroup": dIpExtGeneralPrefixGroup,
       "dIpExtRaPrefixGroup": dIpExtRaPrefixGroup,
       "dIpExtGratuitousArpGroup": dIpExtGratuitousArpGroup,
       "dIpExtProxyArpGroup": dIpExtProxyArpGroup,
       "dIpExtDirectedBroadcastGroup": dIpExtDirectedBroadcastGroup,
       "dIpExtDhcpClientGroup": dIpExtDhcpClientGroup,
       "dIpExtUdpForwardGroup": dIpExtUdpForwardGroup}
)
