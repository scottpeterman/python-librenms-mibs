# SNMP MIB module (F3-L3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\adva\F3-L3-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:16:19 2025
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

(fsp150cm,) = mibBuilder.importSymbols(
    "ADVA-MIB",
    "fsp150cm")

(AdminState,
 CmPmBinAction,
 CmPmIntervalType,
 F3DisplayString,
 FlowSecState,
 IpVersion,
 OperationalState,
 PerfCounter64,
 SecondaryState,
 TrafficDirection,
 VlanId,
 VlanPriority) = mibBuilder.importSymbols(
    "CM-COMMON-MIB",
    "AdminState",
    "CmPmBinAction",
    "CmPmIntervalType",
    "F3DisplayString",
    "FlowSecState",
    "IpVersion",
    "OperationalState",
    "PerfCounter64",
    "SecondaryState",
    "TrafficDirection",
    "VlanId",
    "VlanPriority")

(neIndex,
 shelfIndex,
 slotIndex) = mibBuilder.importSymbols(
    "CM-ENTITY-MIB",
    "neIndex",
    "shelfIndex",
    "slotIndex")

(AclNoMatchDispositionType,
 PolicerAlgorithmType,
 PolicerColorMode,
 ShapingType) = mibBuilder.importSymbols(
    "CM-FACILITY-MIB",
    "AclNoMatchDispositionType",
    "PolicerAlgorithmType",
    "PolicerColorMode",
    "ShapingType")

(CmDhcpRole,
 DHCPCIDType,
 DHCPHostNameType,
 IpEntryType,
 IpMode) = mibBuilder.importSymbols(
    "CM-IP-MIB",
    "CmDhcpRole",
    "DHCPCIDType",
    "DHCPHostNameType",
    "IpEntryType",
    "IpMode")

(PhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue",
    "VariablePointer")


# MODULE-IDENTITY

f3L3MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37)
)
if mibBuilder.loadTexts:
    f3L3MIB.setRevisions(
        ("2018-10-25 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class BgpGracefulRestartControlType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("enable", 1),
          ("disable", 2),
          ("helperOnly", 3))
    )



class EcmpDistributionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("l3", 1),
          ("l4", 2))
    )



class BgpUpdateSourceType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("none", 1),
          ("ipv4Address", 2),
          ("ipv6Address", 3),
          ("interfaceName", 4))
    )



class BgpRouteFilterDirection(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("in", 1),
          ("out", 2))
    )



class IpPrefixDispositionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("permit", 1),
          ("deny", 2))
    )



class BgpRouterActionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("optimizeBgpRouteRetrieve", 1),
          ("optimizeBgpInRouteRetrieve", 2))
    )



class OspfRouterActionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("optimizeOspfAsLsDbRetrieve", 1),
          ("optimizeOspfLsDbRetrieve", 2),
          ("optimizeOspfNeighborRetrieve", 3),
          ("optimizeOspfLinkLsDbRetrieve", 4))
    )



class Ipv6AddressAssignMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("manual", 1),
          ("automatic", 2),
          ("external", 3))
    )



class TrafficIpRouteOriginType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("notApplicable", 0),
          ("bgp", 1),
          ("ospf", 2),
          ("connected", 3),
          ("static", 4),
          ("dhcp", 5),
          ("slaac", 6),
          ("dhcp-relay", 7),
          ("isis", 8),
          ("ti-lfa", 9))
    )



class NdpNeighborReachabilityState(TextualConvention, Integer32):
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
        *(("notApplicable", 0),
          ("incomplete", 1),
          ("reachable", 2),
          ("stale", 3),
          ("delay", 4),
          ("probe", 5))
    )



class NdpRaDefaultRouterPreference(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("none", 1),
          ("high", 2),
          ("medium", 3),
          ("low", 4))
    )



class Ipv6LinkLocalAddressMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("automatic", 1),
          ("manual", 2))
    )



class IpInterfaceType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("host", 1),
          ("router", 2))
    )



class OspfAuthType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("none", 1),
          ("simple", 2),
          ("cryptoGraphic", 3))
    )



class OspfInterfaceState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("down", 1),
          ("loopback", 2),
          ("waiting", 3),
          ("pointToPoint", 4),
          ("drOther", 5),
          ("dr", 6),
          ("backup", 7))
    )



class OspfIfType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("broadcast", 1),
          ("pointToPoint", 2),
          ("loopback", 3))
    )



class TrafficOspfRole(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("dr", 1),
          ("bdr", 2),
          ("drother", 3),
          ("pointToPoint", 4))
    )



class OspfAdjacencyState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("down", 1),
          ("attempt", 2),
          ("init", 3),
          ("twoWay", 4),
          ("exStart", 5),
          ("exchange", 6),
          ("loading", 7),
          ("full", 8))
    )



class OspfAsLsaType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("asExternal", 1),
          ("asOpaque", 2))
    )



class OspfLsaType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("router", 1),
          ("network", 2),
          ("summary", 3),
          ("asExternal", 4),
          ("areaOpaque", 5),
          ("summaryNet", 6),
          ("summaryAsbr", 7),
          ("multicast", 8),
          ("nssaExternal", 9),
          ("interAreaPrefix", 10),
          ("interAreaRouter", 11),
          ("link", 12),
          ("intraAreaPrefix", 13))
    )



class RoutesMetricType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("e1", 1),
          ("e2", 2))
    )



class TrafficOspfAreaType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("stub", 1),
          ("normal", 2))
    )



class BgpSessionStateType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("idle", 1),
          ("connect", 2),
          ("active", 3),
          ("openSent", 4),
          ("openConfirm", 5),
          ("established", 6))
    )



class BgpNextHopUpdateType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("default", 1),
          ("self", 2),
          ("ipv4", 3),
          ("ipv6", 4))
    )



class BgpPeerAddressFamilyNameType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("ipv4-unicast", 1),
          ("ipv6-unicast", 2))
    )



class OspfVersion(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("ospfv2", 1),
          ("ospfv3", 2))
    )



class VrfAction(TextualConvention, Integer32):
    status = "deprecated"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("ping", 1),
          ("fluchARPCache", 2),
          ("traceRoute", 3),
          ("retrieveEffectiveRoutes", 4))
    )



class VrfActionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("notApplicable", 0),
          ("ping", 1),
          ("traceRoute", 2),
          ("optimizeRouteRetrieve", 3),
          ("flushArpCache", 4),
          ("pingV6", 5),
          ("traceRouteV6", 6),
          ("optimizeIpv6RouteRetrieve", 7),
          ("flushNDP", 8),
          ("optimizeBfdSessionRetrieve", 9))
    )



class IfIpAddressSourceType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 1),
          ("static", 2))
    )



class DhcpRelayInterfaceSide(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("client", 1),
          ("server", 2))
    )



class L3AclRuleOperation(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("accept", 1),
          ("deny", 2))
    )



class AclRuleL2Side(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("access", 1),
          ("network", 2))
    )



class TrafficIpRouteStatus(TextualConvention, Integer32):
    status = "deprecated"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("nexthopUnresovled", 2),
          ("interfaceOutage", 3),
          ("noResources", 4),
          ("standby", 5),
          ("bfdSessDown", 6))
    )



class RouteFlags(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("dDynamic", 0),
          ("gUseGW", 1),
          ("hFullMask", 2),
          ("mModifiedByIcmp", 3),
          ("oOutage", 4),
          ("uNormal", 5))
    )


class TrafficIpRouteStatusType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("nexthopUnresolved", 2),
          ("interfaceOutage", 3),
          ("noResources", 4),
          ("standby", 5),
          ("bfdSessDown", 6))
    )



class AffectiveArpActionType(TextualConvention, Integer32):
    status = "deprecated"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("retrieveAffectiveArp", 1))
    )



class TrafficIpInterfaceActionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("optimizeArpRetrieve", 1),
          ("optimizeNdpRetrieve", 2),
          ("optimizeIPv6AddressEntryRetrieve", 3))
    )



class TrafficIpv6InterfaceActionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("optimizeNdpRetrieve", 1),
          ("optimizeIPv6AddressEntryRetrieve", 2))
    )



class SrSidType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("index", 1),
          ("label", 2),
          ("sid", 3))
    )



class VrfTransportType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("sr", 2))
    )



class TilfaProtectionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("link-protection", 1),
          ("node-protection", 2))
    )



# MIB Managed Objects in the order of their OIDs

_F3L3Objects_ObjectIdentity = ObjectIdentity
f3L3Objects = _F3L3Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1)
)
_F3DhcpRelayAgentTable_Object = MibTable
f3DhcpRelayAgentTable = _F3DhcpRelayAgentTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 1)
)
if mibBuilder.loadTexts:
    f3DhcpRelayAgentTable.setStatus("current")
_F3DhcpRelayAgentEntry_Object = MibTableRow
f3DhcpRelayAgentEntry = _F3DhcpRelayAgentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 1, 1)
)
f3DhcpRelayAgentEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-L3-MIB", "f3DhcpRelayAgentIndex"),
)
if mibBuilder.loadTexts:
    f3DhcpRelayAgentEntry.setStatus("current")
_F3DhcpRelayAgentIndex_Type = Integer32
_F3DhcpRelayAgentIndex_Object = MibTableColumn
f3DhcpRelayAgentIndex = _F3DhcpRelayAgentIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 1, 1, 1),
    _F3DhcpRelayAgentIndex_Type()
)
f3DhcpRelayAgentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3DhcpRelayAgentIndex.setStatus("current")


class _F3DhcpRelayAgentAlias_Type(F3DisplayString):
    """Custom type f3DhcpRelayAgentAlias based on F3DisplayString"""
    subtypeSpec = F3DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_F3DhcpRelayAgentAlias_Type.__name__ = "F3DisplayString"
_F3DhcpRelayAgentAlias_Object = MibTableColumn
f3DhcpRelayAgentAlias = _F3DhcpRelayAgentAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 1, 1, 2),
    _F3DhcpRelayAgentAlias_Type()
)
f3DhcpRelayAgentAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3DhcpRelayAgentAlias.setStatus("current")
_F3DhcpRelayAgentAdminState_Type = AdminState
_F3DhcpRelayAgentAdminState_Object = MibTableColumn
f3DhcpRelayAgentAdminState = _F3DhcpRelayAgentAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 1, 1, 3),
    _F3DhcpRelayAgentAdminState_Type()
)
f3DhcpRelayAgentAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3DhcpRelayAgentAdminState.setStatus("current")
_F3DhcpRelayAgentSecondaryState_Type = SecondaryState
_F3DhcpRelayAgentSecondaryState_Object = MibTableColumn
f3DhcpRelayAgentSecondaryState = _F3DhcpRelayAgentSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 1, 1, 4),
    _F3DhcpRelayAgentSecondaryState_Type()
)
f3DhcpRelayAgentSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3DhcpRelayAgentSecondaryState.setStatus("current")
_F3DhcpRelayAgentOperationalState_Type = OperationalState
_F3DhcpRelayAgentOperationalState_Object = MibTableColumn
f3DhcpRelayAgentOperationalState = _F3DhcpRelayAgentOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 1, 1, 5),
    _F3DhcpRelayAgentOperationalState_Type()
)
f3DhcpRelayAgentOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3DhcpRelayAgentOperationalState.setStatus("current")
_F3DhcpRelayAgentIpVersion_Type = IpVersion
_F3DhcpRelayAgentIpVersion_Object = MibTableColumn
f3DhcpRelayAgentIpVersion = _F3DhcpRelayAgentIpVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 1, 1, 6),
    _F3DhcpRelayAgentIpVersion_Type()
)
f3DhcpRelayAgentIpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3DhcpRelayAgentIpVersion.setStatus("current")
_F3DhcpRelayAgentServerIpAddress_Type = IpAddress
_F3DhcpRelayAgentServerIpAddress_Object = MibTableColumn
f3DhcpRelayAgentServerIpAddress = _F3DhcpRelayAgentServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 1, 1, 7),
    _F3DhcpRelayAgentServerIpAddress_Type()
)
f3DhcpRelayAgentServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3DhcpRelayAgentServerIpAddress.setStatus("current")
_F3DhcpRelayAgentOp82SubOp9ControlEnabled_Type = TruthValue
_F3DhcpRelayAgentOp82SubOp9ControlEnabled_Object = MibTableColumn
f3DhcpRelayAgentOp82SubOp9ControlEnabled = _F3DhcpRelayAgentOp82SubOp9ControlEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 1, 1, 8),
    _F3DhcpRelayAgentOp82SubOp9ControlEnabled_Type()
)
f3DhcpRelayAgentOp82SubOp9ControlEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3DhcpRelayAgentOp82SubOp9ControlEnabled.setStatus("current")


class _F3DhcpRelayAgentOp82SubOp9Value_Type(DisplayString):
    """Custom type f3DhcpRelayAgentOp82SubOp9Value based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_F3DhcpRelayAgentOp82SubOp9Value_Type.__name__ = "DisplayString"
_F3DhcpRelayAgentOp82SubOp9Value_Object = MibTableColumn
f3DhcpRelayAgentOp82SubOp9Value = _F3DhcpRelayAgentOp82SubOp9Value_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 1, 1, 9),
    _F3DhcpRelayAgentOp82SubOp9Value_Type()
)
f3DhcpRelayAgentOp82SubOp9Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3DhcpRelayAgentOp82SubOp9Value.setStatus("current")
_F3DhcpRelayAgentStorageType_Type = StorageType
_F3DhcpRelayAgentStorageType_Object = MibTableColumn
f3DhcpRelayAgentStorageType = _F3DhcpRelayAgentStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 1, 1, 10),
    _F3DhcpRelayAgentStorageType_Type()
)
f3DhcpRelayAgentStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3DhcpRelayAgentStorageType.setStatus("current")
_F3DhcpRelayAgentRowStatus_Type = RowStatus
_F3DhcpRelayAgentRowStatus_Object = MibTableColumn
f3DhcpRelayAgentRowStatus = _F3DhcpRelayAgentRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 1, 1, 11),
    _F3DhcpRelayAgentRowStatus_Type()
)
f3DhcpRelayAgentRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3DhcpRelayAgentRowStatus.setStatus("current")
_F3VrfTable_Object = MibTable
f3VrfTable = _F3VrfTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 2)
)
if mibBuilder.loadTexts:
    f3VrfTable.setStatus("current")
_F3VrfEntry_Object = MibTableRow
f3VrfEntry = _F3VrfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 2, 1)
)
f3VrfEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-L3-MIB", "f3VrfIndex"),
)
if mibBuilder.loadTexts:
    f3VrfEntry.setStatus("current")
_F3VrfIndex_Type = Integer32
_F3VrfIndex_Object = MibTableColumn
f3VrfIndex = _F3VrfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 2, 1, 1),
    _F3VrfIndex_Type()
)
f3VrfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3VrfIndex.setStatus("current")


class _F3VrfAlias_Type(F3DisplayString):
    """Custom type f3VrfAlias based on F3DisplayString"""
    subtypeSpec = F3DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_F3VrfAlias_Type.__name__ = "F3DisplayString"
_F3VrfAlias_Object = MibTableColumn
f3VrfAlias = _F3VrfAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 2, 1, 2),
    _F3VrfAlias_Type()
)
f3VrfAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3VrfAlias.setStatus("current")
_F3VrfAdminState_Type = AdminState
_F3VrfAdminState_Object = MibTableColumn
f3VrfAdminState = _F3VrfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 2, 1, 3),
    _F3VrfAdminState_Type()
)
f3VrfAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3VrfAdminState.setStatus("current")
_F3VrfSecondaryState_Type = SecondaryState
_F3VrfSecondaryState_Object = MibTableColumn
f3VrfSecondaryState = _F3VrfSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 2, 1, 4),
    _F3VrfSecondaryState_Type()
)
f3VrfSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3VrfSecondaryState.setStatus("current")
_F3VrfOperationalState_Type = OperationalState
_F3VrfOperationalState_Object = MibTableColumn
f3VrfOperationalState = _F3VrfOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 2, 1, 5),
    _F3VrfOperationalState_Type()
)
f3VrfOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3VrfOperationalState.setStatus("current")
_F3VrfAccIsolationControlEnabled_Type = OperationalState
_F3VrfAccIsolationControlEnabled_Object = MibTableColumn
f3VrfAccIsolationControlEnabled = _F3VrfAccIsolationControlEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 2, 1, 6),
    _F3VrfAccIsolationControlEnabled_Type()
)
f3VrfAccIsolationControlEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3VrfAccIsolationControlEnabled.setStatus("obsolete")
_F3VrfPingIpv4Destination_Type = IpAddress
_F3VrfPingIpv4Destination_Object = MibTableColumn
f3VrfPingIpv4Destination = _F3VrfPingIpv4Destination_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 2, 1, 7),
    _F3VrfPingIpv4Destination_Type()
)
f3VrfPingIpv4Destination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3VrfPingIpv4Destination.setStatus("current")
_F3VrfTraceRouteIpv4Destination_Type = IpAddress
_F3VrfTraceRouteIpv4Destination_Object = MibTableColumn
f3VrfTraceRouteIpv4Destination = _F3VrfTraceRouteIpv4Destination_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 2, 1, 8),
    _F3VrfTraceRouteIpv4Destination_Type()
)
f3VrfTraceRouteIpv4Destination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3VrfTraceRouteIpv4Destination.setStatus("current")
_F3VrfAction_Type = VrfAction
_F3VrfAction_Object = MibTableColumn
f3VrfAction = _F3VrfAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 2, 1, 9),
    _F3VrfAction_Type()
)
f3VrfAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3VrfAction.setStatus("deprecated")
_F3VrfPingResult_Type = F3DisplayString
_F3VrfPingResult_Object = MibTableColumn
f3VrfPingResult = _F3VrfPingResult_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 2, 1, 10),
    _F3VrfPingResult_Type()
)
f3VrfPingResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3VrfPingResult.setStatus("current")
_F3VrfTraceRouteResult_Type = F3DisplayString
_F3VrfTraceRouteResult_Object = MibTableColumn
f3VrfTraceRouteResult = _F3VrfTraceRouteResult_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 2, 1, 11),
    _F3VrfTraceRouteResult_Type()
)
f3VrfTraceRouteResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3VrfTraceRouteResult.setStatus("current")
_F3VrfStorageType_Type = StorageType
_F3VrfStorageType_Object = MibTableColumn
f3VrfStorageType = _F3VrfStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 2, 1, 12),
    _F3VrfStorageType_Type()
)
f3VrfStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3VrfStorageType.setStatus("current")
_F3VrfRowStatus_Type = RowStatus
_F3VrfRowStatus_Object = MibTableColumn
f3VrfRowStatus = _F3VrfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 2, 1, 13),
    _F3VrfRowStatus_Type()
)
f3VrfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3VrfRowStatus.setStatus("current")
_F3VrfDhcpRoutesControl_Type = TruthValue
_F3VrfDhcpRoutesControl_Object = MibTableColumn
f3VrfDhcpRoutesControl = _F3VrfDhcpRoutesControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 2, 1, 14),
    _F3VrfDhcpRoutesControl_Type()
)
f3VrfDhcpRoutesControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3VrfDhcpRoutesControl.setStatus("current")
_F3VrfActionX_Type = VrfActionType
_F3VrfActionX_Object = MibTableColumn
f3VrfActionX = _F3VrfActionX_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 2, 1, 15),
    _F3VrfActionX_Type()
)
f3VrfActionX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3VrfActionX.setStatus("current")
_F3VrfActionIfName_Type = DisplayString
_F3VrfActionIfName_Object = MibTableColumn
f3VrfActionIfName = _F3VrfActionIfName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 2, 1, 16),
    _F3VrfActionIfName_Type()
)
f3VrfActionIfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3VrfActionIfName.setStatus("current")
_F3VrfIpVersion_Type = IpVersion
_F3VrfIpVersion_Object = MibTableColumn
f3VrfIpVersion = _F3VrfIpVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 2, 1, 17),
    _F3VrfIpVersion_Type()
)
f3VrfIpVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3VrfIpVersion.setStatus("current")
_F3VrfPingIpv6Destination_Type = Ipv6Address
_F3VrfPingIpv6Destination_Object = MibTableColumn
f3VrfPingIpv6Destination = _F3VrfPingIpv6Destination_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 2, 1, 18),
    _F3VrfPingIpv6Destination_Type()
)
f3VrfPingIpv6Destination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3VrfPingIpv6Destination.setStatus("current")
_F3VrfTraceRouteIpv6Destination_Type = Ipv6Address
_F3VrfTraceRouteIpv6Destination_Object = MibTableColumn
f3VrfTraceRouteIpv6Destination = _F3VrfTraceRouteIpv6Destination_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 2, 1, 19),
    _F3VrfTraceRouteIpv6Destination_Type()
)
f3VrfTraceRouteIpv6Destination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3VrfTraceRouteIpv6Destination.setStatus("current")
_F3VrfMaxFwdTableEntries_Type = Integer32
_F3VrfMaxFwdTableEntries_Object = MibTableColumn
f3VrfMaxFwdTableEntries = _F3VrfMaxFwdTableEntries_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 2, 1, 20),
    _F3VrfMaxFwdTableEntries_Type()
)
f3VrfMaxFwdTableEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3VrfMaxFwdTableEntries.setStatus("current")
_F3VrfFwdTableFull_Type = TruthValue
_F3VrfFwdTableFull_Object = MibTableColumn
f3VrfFwdTableFull = _F3VrfFwdTableFull_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 2, 1, 21),
    _F3VrfFwdTableFull_Type()
)
f3VrfFwdTableFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3VrfFwdTableFull.setStatus("current")
_F3VrfEcmpDistribution_Type = EcmpDistributionType
_F3VrfEcmpDistribution_Object = MibTableColumn
f3VrfEcmpDistribution = _F3VrfEcmpDistribution_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 2, 1, 22),
    _F3VrfEcmpDistribution_Type()
)
f3VrfEcmpDistribution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3VrfEcmpDistribution.setStatus("current")
_F3VrfEcmpStaticRoutesMaximumPaths_Type = Unsigned32
_F3VrfEcmpStaticRoutesMaximumPaths_Object = MibTableColumn
f3VrfEcmpStaticRoutesMaximumPaths = _F3VrfEcmpStaticRoutesMaximumPaths_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 2, 1, 23),
    _F3VrfEcmpStaticRoutesMaximumPaths_Type()
)
f3VrfEcmpStaticRoutesMaximumPaths.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3VrfEcmpStaticRoutesMaximumPaths.setStatus("current")
_F3VrfTransportType_Type = VrfTransportType
_F3VrfTransportType_Object = MibTableColumn
f3VrfTransportType = _F3VrfTransportType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 2, 1, 24),
    _F3VrfTransportType_Type()
)
f3VrfTransportType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3VrfTransportType.setStatus("current")
_F3L3FlowPointTable_Object = MibTable
f3L3FlowPointTable = _F3L3FlowPointTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3)
)
if mibBuilder.loadTexts:
    f3L3FlowPointTable.setStatus("current")
_F3L3FlowPointEntry_Object = MibTableRow
f3L3FlowPointEntry = _F3L3FlowPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1)
)
f3L3FlowPointEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortTypeIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointIndex"),
)
if mibBuilder.loadTexts:
    f3L3FlowPointEntry.setStatus("current")
_F3L3FlowPointPortTypeIndex_Type = Integer32
_F3L3FlowPointPortTypeIndex_Object = MibTableColumn
f3L3FlowPointPortTypeIndex = _F3L3FlowPointPortTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1, 1),
    _F3L3FlowPointPortTypeIndex_Type()
)
f3L3FlowPointPortTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3FlowPointPortTypeIndex.setStatus("current")
_F3L3FlowPointPortIndex_Type = Integer32
_F3L3FlowPointPortIndex_Object = MibTableColumn
f3L3FlowPointPortIndex = _F3L3FlowPointPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1, 2),
    _F3L3FlowPointPortIndex_Type()
)
f3L3FlowPointPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3FlowPointPortIndex.setStatus("current")
_F3L3FlowPointIndex_Type = Integer32
_F3L3FlowPointIndex_Object = MibTableColumn
f3L3FlowPointIndex = _F3L3FlowPointIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1, 3),
    _F3L3FlowPointIndex_Type()
)
f3L3FlowPointIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3FlowPointIndex.setStatus("current")


class _F3L3FlowPointAlias_Type(F3DisplayString):
    """Custom type f3L3FlowPointAlias based on F3DisplayString"""
    subtypeSpec = F3DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_F3L3FlowPointAlias_Type.__name__ = "F3DisplayString"
_F3L3FlowPointAlias_Object = MibTableColumn
f3L3FlowPointAlias = _F3L3FlowPointAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1, 4),
    _F3L3FlowPointAlias_Type()
)
f3L3FlowPointAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3FlowPointAlias.setStatus("current")
_F3L3FlowPointAdminState_Type = AdminState
_F3L3FlowPointAdminState_Object = MibTableColumn
f3L3FlowPointAdminState = _F3L3FlowPointAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1, 5),
    _F3L3FlowPointAdminState_Type()
)
f3L3FlowPointAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3FlowPointAdminState.setStatus("current")
_F3L3FlowPointSecondaryState_Type = SecondaryState
_F3L3FlowPointSecondaryState_Object = MibTableColumn
f3L3FlowPointSecondaryState = _F3L3FlowPointSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1, 6),
    _F3L3FlowPointSecondaryState_Type()
)
f3L3FlowPointSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointSecondaryState.setStatus("current")
_F3L3FlowPointOperationalState_Type = OperationalState
_F3L3FlowPointOperationalState_Object = MibTableColumn
f3L3FlowPointOperationalState = _F3L3FlowPointOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1, 7),
    _F3L3FlowPointOperationalState_Type()
)
f3L3FlowPointOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointOperationalState.setStatus("current")
_F3L3FlowPointMultiCOSEnabled_Type = TruthValue
_F3L3FlowPointMultiCOSEnabled_Object = MibTableColumn
f3L3FlowPointMultiCOSEnabled = _F3L3FlowPointMultiCOSEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1, 8),
    _F3L3FlowPointMultiCOSEnabled_Type()
)
f3L3FlowPointMultiCOSEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3FlowPointMultiCOSEnabled.setStatus("current")
_F3L3FlowPointCOS_Type = Integer32
_F3L3FlowPointCOS_Object = MibTableColumn
f3L3FlowPointCOS = _F3L3FlowPointCOS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1, 9),
    _F3L3FlowPointCOS_Type()
)
f3L3FlowPointCOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3FlowPointCOS.setStatus("current")
_F3L3FlowPointUntaggedMemberShipEnabled_Type = TruthValue
_F3L3FlowPointUntaggedMemberShipEnabled_Object = MibTableColumn
f3L3FlowPointUntaggedMemberShipEnabled = _F3L3FlowPointUntaggedMemberShipEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1, 10),
    _F3L3FlowPointUntaggedMemberShipEnabled_Type()
)
f3L3FlowPointUntaggedMemberShipEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3FlowPointUntaggedMemberShipEnabled.setStatus("current")
_F3L3FlowPointOuterTagMemberShipEnabled_Type = TruthValue
_F3L3FlowPointOuterTagMemberShipEnabled_Object = MibTableColumn
f3L3FlowPointOuterTagMemberShipEnabled = _F3L3FlowPointOuterTagMemberShipEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1, 11),
    _F3L3FlowPointOuterTagMemberShipEnabled_Type()
)
f3L3FlowPointOuterTagMemberShipEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3FlowPointOuterTagMemberShipEnabled.setStatus("current")
_F3L3FlowPointOuterTagMemberShipVlanId_Type = VlanId
_F3L3FlowPointOuterTagMemberShipVlanId_Object = MibTableColumn
f3L3FlowPointOuterTagMemberShipVlanId = _F3L3FlowPointOuterTagMemberShipVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1, 12),
    _F3L3FlowPointOuterTagMemberShipVlanId_Type()
)
f3L3FlowPointOuterTagMemberShipVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3FlowPointOuterTagMemberShipVlanId.setStatus("current")
_F3L3FlowPointInnerTagMemberShipEnabled_Type = TruthValue
_F3L3FlowPointInnerTagMemberShipEnabled_Object = MibTableColumn
f3L3FlowPointInnerTagMemberShipEnabled = _F3L3FlowPointInnerTagMemberShipEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1, 13),
    _F3L3FlowPointInnerTagMemberShipEnabled_Type()
)
f3L3FlowPointInnerTagMemberShipEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3FlowPointInnerTagMemberShipEnabled.setStatus("current")
_F3L3FlowPointInnerTagMemberShipVlanId_Type = VlanId
_F3L3FlowPointInnerTagMemberShipVlanId_Object = MibTableColumn
f3L3FlowPointInnerTagMemberShipVlanId = _F3L3FlowPointInnerTagMemberShipVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1, 14),
    _F3L3FlowPointInnerTagMemberShipVlanId_Type()
)
f3L3FlowPointInnerTagMemberShipVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3FlowPointInnerTagMemberShipVlanId.setStatus("current")
_F3L3FlowPointFragmentedPktsFwdEnabled_Type = TruthValue
_F3L3FlowPointFragmentedPktsFwdEnabled_Object = MibTableColumn
f3L3FlowPointFragmentedPktsFwdEnabled = _F3L3FlowPointFragmentedPktsFwdEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1, 15),
    _F3L3FlowPointFragmentedPktsFwdEnabled_Type()
)
f3L3FlowPointFragmentedPktsFwdEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3FlowPointFragmentedPktsFwdEnabled.setStatus("current")
_F3L3FlowPointHCosMgmtEnabled_Type = TruthValue
_F3L3FlowPointHCosMgmtEnabled_Object = MibTableColumn
f3L3FlowPointHCosMgmtEnabled = _F3L3FlowPointHCosMgmtEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1, 16),
    _F3L3FlowPointHCosMgmtEnabled_Type()
)
f3L3FlowPointHCosMgmtEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3FlowPointHCosMgmtEnabled.setStatus("current")
_F3L3FlowPointHCosGuaranteedBwHi_Type = Unsigned32
_F3L3FlowPointHCosGuaranteedBwHi_Object = MibTableColumn
f3L3FlowPointHCosGuaranteedBwHi = _F3L3FlowPointHCosGuaranteedBwHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1, 17),
    _F3L3FlowPointHCosGuaranteedBwHi_Type()
)
f3L3FlowPointHCosGuaranteedBwHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3FlowPointHCosGuaranteedBwHi.setStatus("current")
_F3L3FlowPointHCosGuaranteedBwLo_Type = Unsigned32
_F3L3FlowPointHCosGuaranteedBwLo_Object = MibTableColumn
f3L3FlowPointHCosGuaranteedBwLo = _F3L3FlowPointHCosGuaranteedBwLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1, 18),
    _F3L3FlowPointHCosGuaranteedBwLo_Type()
)
f3L3FlowPointHCosGuaranteedBwLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3FlowPointHCosGuaranteedBwLo.setStatus("current")
_F3L3FlowPointHCosMaximumBwHi_Type = Unsigned32
_F3L3FlowPointHCosMaximumBwHi_Object = MibTableColumn
f3L3FlowPointHCosMaximumBwHi = _F3L3FlowPointHCosMaximumBwHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1, 19),
    _F3L3FlowPointHCosMaximumBwHi_Type()
)
f3L3FlowPointHCosMaximumBwHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3FlowPointHCosMaximumBwHi.setStatus("current")
_F3L3FlowPointHCosMaximumBwLo_Type = Unsigned32
_F3L3FlowPointHCosMaximumBwLo_Object = MibTableColumn
f3L3FlowPointHCosMaximumBwLo = _F3L3FlowPointHCosMaximumBwLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1, 20),
    _F3L3FlowPointHCosMaximumBwLo_Type()
)
f3L3FlowPointHCosMaximumBwLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3FlowPointHCosMaximumBwLo.setStatus("current")
_F3L3FlowPointPolicingEnabled_Type = TruthValue
_F3L3FlowPointPolicingEnabled_Object = MibTableColumn
f3L3FlowPointPolicingEnabled = _F3L3FlowPointPolicingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1, 21),
    _F3L3FlowPointPolicingEnabled_Type()
)
f3L3FlowPointPolicingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3FlowPointPolicingEnabled.setStatus("current")
_F3L3FlowPointStorageType_Type = StorageType
_F3L3FlowPointStorageType_Object = MibTableColumn
f3L3FlowPointStorageType = _F3L3FlowPointStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1, 22),
    _F3L3FlowPointStorageType_Type()
)
f3L3FlowPointStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3FlowPointStorageType.setStatus("current")
_F3L3FlowPointRowStatus_Type = RowStatus
_F3L3FlowPointRowStatus_Object = MibTableColumn
f3L3FlowPointRowStatus = _F3L3FlowPointRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1, 23),
    _F3L3FlowPointRowStatus_Type()
)
f3L3FlowPointRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3FlowPointRowStatus.setStatus("current")
_F3L3FlowPointDscpOverwriteControl_Type = TruthValue
_F3L3FlowPointDscpOverwriteControl_Object = MibTableColumn
f3L3FlowPointDscpOverwriteControl = _F3L3FlowPointDscpOverwriteControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1, 24),
    _F3L3FlowPointDscpOverwriteControl_Type()
)
f3L3FlowPointDscpOverwriteControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3FlowPointDscpOverwriteControl.setStatus("current")
_F3L3FlowPointPriMapProfile_Type = VariablePointer
_F3L3FlowPointPriMapProfile_Object = MibTableColumn
f3L3FlowPointPriMapProfile = _F3L3FlowPointPriMapProfile_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1, 25),
    _F3L3FlowPointPriMapProfile_Type()
)
f3L3FlowPointPriMapProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3FlowPointPriMapProfile.setStatus("current")
_F3L3FlowPointRefConnectGuardFlow_Type = VariablePointer
_F3L3FlowPointRefConnectGuardFlow_Object = MibTableColumn
f3L3FlowPointRefConnectGuardFlow = _F3L3FlowPointRefConnectGuardFlow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1, 26),
    _F3L3FlowPointRefConnectGuardFlow_Type()
)
f3L3FlowPointRefConnectGuardFlow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3FlowPointRefConnectGuardFlow.setStatus("current")
_F3L3FlowPointSecureState_Type = FlowSecState
_F3L3FlowPointSecureState_Object = MibTableColumn
f3L3FlowPointSecureState = _F3L3FlowPointSecureState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1, 27),
    _F3L3FlowPointSecureState_Type()
)
f3L3FlowPointSecureState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointSecureState.setStatus("current")
_F3L3FlowPointSecureBlockingEnabled_Type = TruthValue
_F3L3FlowPointSecureBlockingEnabled_Object = MibTableColumn
f3L3FlowPointSecureBlockingEnabled = _F3L3FlowPointSecureBlockingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1, 28),
    _F3L3FlowPointSecureBlockingEnabled_Type()
)
f3L3FlowPointSecureBlockingEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3FlowPointSecureBlockingEnabled.setStatus("current")
_F3L3FlowPointWfqSegmentationCOS_Type = Integer32
_F3L3FlowPointWfqSegmentationCOS_Object = MibTableColumn
f3L3FlowPointWfqSegmentationCOS = _F3L3FlowPointWfqSegmentationCOS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1, 29),
    _F3L3FlowPointWfqSegmentationCOS_Type()
)
f3L3FlowPointWfqSegmentationCOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3FlowPointWfqSegmentationCOS.setStatus("current")
_F3L3FlowPointWfqGroupCOS_Type = Integer32
_F3L3FlowPointWfqGroupCOS_Object = MibTableColumn
f3L3FlowPointWfqGroupCOS = _F3L3FlowPointWfqGroupCOS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1, 30),
    _F3L3FlowPointWfqGroupCOS_Type()
)
f3L3FlowPointWfqGroupCOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3FlowPointWfqGroupCOS.setStatus("current")
_F3L3FlowPointWfqGroupEirLo_Type = Unsigned32
_F3L3FlowPointWfqGroupEirLo_Object = MibTableColumn
f3L3FlowPointWfqGroupEirLo = _F3L3FlowPointWfqGroupEirLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1, 31),
    _F3L3FlowPointWfqGroupEirLo_Type()
)
f3L3FlowPointWfqGroupEirLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3FlowPointWfqGroupEirLo.setStatus("current")
_F3L3FlowPointWfqGroupEirHi_Type = Unsigned32
_F3L3FlowPointWfqGroupEirHi_Object = MibTableColumn
f3L3FlowPointWfqGroupEirHi = _F3L3FlowPointWfqGroupEirHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1, 32),
    _F3L3FlowPointWfqGroupEirHi_Type()
)
f3L3FlowPointWfqGroupEirHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3FlowPointWfqGroupEirHi.setStatus("current")


class _F3L3FlowPointOuterVlanEthertype_Type(Integer32):
    """Custom type f3L3FlowPointOuterVlanEthertype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_F3L3FlowPointOuterVlanEthertype_Type.__name__ = "Integer32"
_F3L3FlowPointOuterVlanEthertype_Object = MibTableColumn
f3L3FlowPointOuterVlanEthertype = _F3L3FlowPointOuterVlanEthertype_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1, 33),
    _F3L3FlowPointOuterVlanEthertype_Type()
)
f3L3FlowPointOuterVlanEthertype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3FlowPointOuterVlanEthertype.setStatus("current")


class _F3L3FlowPointInnerVlanEthertype_Type(Integer32):
    """Custom type f3L3FlowPointInnerVlanEthertype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_F3L3FlowPointInnerVlanEthertype_Type.__name__ = "Integer32"
_F3L3FlowPointInnerVlanEthertype_Object = MibTableColumn
f3L3FlowPointInnerVlanEthertype = _F3L3FlowPointInnerVlanEthertype_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1, 34),
    _F3L3FlowPointInnerVlanEthertype_Type()
)
f3L3FlowPointInnerVlanEthertype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3FlowPointInnerVlanEthertype.setStatus("current")
_F3L3FlowPointIpVersion_Type = IpVersion
_F3L3FlowPointIpVersion_Object = MibTableColumn
f3L3FlowPointIpVersion = _F3L3FlowPointIpVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 3, 1, 35),
    _F3L3FlowPointIpVersion_Type()
)
f3L3FlowPointIpVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3FlowPointIpVersion.setStatus("current")
_F3L3AclRuleTable_Object = MibTable
f3L3AclRuleTable = _F3L3AclRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4)
)
if mibBuilder.loadTexts:
    f3L3AclRuleTable.setStatus("current")
_F3L3AclRuleEntry_Object = MibTableRow
f3L3AclRuleEntry = _F3L3AclRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1)
)
f3L3AclRuleEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L3AclRuleParentIndex"),
    (0, "F3-L3-MIB", "f3L3AclRuleIndex"),
)
if mibBuilder.loadTexts:
    f3L3AclRuleEntry.setStatus("current")
_F3L3AclRuleParentIndex_Type = Integer32
_F3L3AclRuleParentIndex_Object = MibTableColumn
f3L3AclRuleParentIndex = _F3L3AclRuleParentIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 1),
    _F3L3AclRuleParentIndex_Type()
)
f3L3AclRuleParentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3AclRuleParentIndex.setStatus("current")
_F3L3AclRuleIndex_Type = Integer32
_F3L3AclRuleIndex_Object = MibTableColumn
f3L3AclRuleIndex = _F3L3AclRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 2),
    _F3L3AclRuleIndex_Type()
)
f3L3AclRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3AclRuleIndex.setStatus("current")


class _F3L3AclRuleAlias_Type(F3DisplayString):
    """Custom type f3L3AclRuleAlias based on F3DisplayString"""
    subtypeSpec = F3DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_F3L3AclRuleAlias_Type.__name__ = "F3DisplayString"
_F3L3AclRuleAlias_Object = MibTableColumn
f3L3AclRuleAlias = _F3L3AclRuleAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 3),
    _F3L3AclRuleAlias_Type()
)
f3L3AclRuleAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleAlias.setStatus("current")
_F3L3AclRuleSrcIpv4AddressControl_Type = TruthValue
_F3L3AclRuleSrcIpv4AddressControl_Object = MibTableColumn
f3L3AclRuleSrcIpv4AddressControl = _F3L3AclRuleSrcIpv4AddressControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 4),
    _F3L3AclRuleSrcIpv4AddressControl_Type()
)
f3L3AclRuleSrcIpv4AddressControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleSrcIpv4AddressControl.setStatus("current")
_F3L3AclRuleDynamicSrcIpControl_Type = TruthValue
_F3L3AclRuleDynamicSrcIpControl_Object = MibTableColumn
f3L3AclRuleDynamicSrcIpControl = _F3L3AclRuleDynamicSrcIpControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 5),
    _F3L3AclRuleDynamicSrcIpControl_Type()
)
f3L3AclRuleDynamicSrcIpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleDynamicSrcIpControl.setStatus("current")
_F3L3AclRuleSrcIpv4AddressLowLimit_Type = IpAddress
_F3L3AclRuleSrcIpv4AddressLowLimit_Object = MibTableColumn
f3L3AclRuleSrcIpv4AddressLowLimit = _F3L3AclRuleSrcIpv4AddressLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 6),
    _F3L3AclRuleSrcIpv4AddressLowLimit_Type()
)
f3L3AclRuleSrcIpv4AddressLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleSrcIpv4AddressLowLimit.setStatus("current")
_F3L3AclRuleDstIpv4AddressControl_Type = TruthValue
_F3L3AclRuleDstIpv4AddressControl_Object = MibTableColumn
f3L3AclRuleDstIpv4AddressControl = _F3L3AclRuleDstIpv4AddressControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 7),
    _F3L3AclRuleDstIpv4AddressControl_Type()
)
f3L3AclRuleDstIpv4AddressControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleDstIpv4AddressControl.setStatus("current")
_F3L3AclRuleDstIpv4AddressLowLimit_Type = IpAddress
_F3L3AclRuleDstIpv4AddressLowLimit_Object = MibTableColumn
f3L3AclRuleDstIpv4AddressLowLimit = _F3L3AclRuleDstIpv4AddressLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 8),
    _F3L3AclRuleDstIpv4AddressLowLimit_Type()
)
f3L3AclRuleDstIpv4AddressLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleDstIpv4AddressLowLimit.setStatus("current")
_F3L3AclRuleIpv4PriorityControl_Type = TruthValue
_F3L3AclRuleIpv4PriorityControl_Object = MibTableColumn
f3L3AclRuleIpv4PriorityControl = _F3L3AclRuleIpv4PriorityControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 9),
    _F3L3AclRuleIpv4PriorityControl_Type()
)
f3L3AclRuleIpv4PriorityControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleIpv4PriorityControl.setStatus("deprecated")
_F3L3AclRuleIpv4PriorityLowLimit_Type = Integer32
_F3L3AclRuleIpv4PriorityLowLimit_Object = MibTableColumn
f3L3AclRuleIpv4PriorityLowLimit = _F3L3AclRuleIpv4PriorityLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 10),
    _F3L3AclRuleIpv4PriorityLowLimit_Type()
)
f3L3AclRuleIpv4PriorityLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleIpv4PriorityLowLimit.setStatus("deprecated")
_F3L3AclRuleProtocolControl_Type = TruthValue
_F3L3AclRuleProtocolControl_Object = MibTableColumn
f3L3AclRuleProtocolControl = _F3L3AclRuleProtocolControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 11),
    _F3L3AclRuleProtocolControl_Type()
)
f3L3AclRuleProtocolControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleProtocolControl.setStatus("current")
_F3L3AclRuleProtocolNumber_Type = Integer32
_F3L3AclRuleProtocolNumber_Object = MibTableColumn
f3L3AclRuleProtocolNumber = _F3L3AclRuleProtocolNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 12),
    _F3L3AclRuleProtocolNumber_Type()
)
f3L3AclRuleProtocolNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleProtocolNumber.setStatus("current")
_F3L3AclRuleSrcPortControl_Type = TruthValue
_F3L3AclRuleSrcPortControl_Object = MibTableColumn
f3L3AclRuleSrcPortControl = _F3L3AclRuleSrcPortControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 13),
    _F3L3AclRuleSrcPortControl_Type()
)
f3L3AclRuleSrcPortControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleSrcPortControl.setStatus("current")
_F3L3AclRuleSrcPortLowLimit_Type = Integer32
_F3L3AclRuleSrcPortLowLimit_Object = MibTableColumn
f3L3AclRuleSrcPortLowLimit = _F3L3AclRuleSrcPortLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 14),
    _F3L3AclRuleSrcPortLowLimit_Type()
)
f3L3AclRuleSrcPortLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleSrcPortLowLimit.setStatus("current")
_F3L3AclRuleSrcPortHighLimit_Type = Integer32
_F3L3AclRuleSrcPortHighLimit_Object = MibTableColumn
f3L3AclRuleSrcPortHighLimit = _F3L3AclRuleSrcPortHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 15),
    _F3L3AclRuleSrcPortHighLimit_Type()
)
f3L3AclRuleSrcPortHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleSrcPortHighLimit.setStatus("current")
_F3L3AclRuleDstPortControl_Type = TruthValue
_F3L3AclRuleDstPortControl_Object = MibTableColumn
f3L3AclRuleDstPortControl = _F3L3AclRuleDstPortControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 16),
    _F3L3AclRuleDstPortControl_Type()
)
f3L3AclRuleDstPortControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleDstPortControl.setStatus("current")
_F3L3AclRuleDstPortLowLimit_Type = Integer32
_F3L3AclRuleDstPortLowLimit_Object = MibTableColumn
f3L3AclRuleDstPortLowLimit = _F3L3AclRuleDstPortLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 17),
    _F3L3AclRuleDstPortLowLimit_Type()
)
f3L3AclRuleDstPortLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleDstPortLowLimit.setStatus("current")
_F3L3AclRuleDstPortHighLimit_Type = Integer32
_F3L3AclRuleDstPortHighLimit_Object = MibTableColumn
f3L3AclRuleDstPortHighLimit = _F3L3AclRuleDstPortHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 18),
    _F3L3AclRuleDstPortHighLimit_Type()
)
f3L3AclRuleDstPortHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleDstPortHighLimit.setStatus("current")
_F3L3AclRulePriority_Type = Integer32
_F3L3AclRulePriority_Object = MibTableColumn
f3L3AclRulePriority = _F3L3AclRulePriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 19),
    _F3L3AclRulePriority_Type()
)
f3L3AclRulePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRulePriority.setStatus("current")
_F3L3AclRuleCOS_Type = Integer32
_F3L3AclRuleCOS_Object = MibTableColumn
f3L3AclRuleCOS = _F3L3AclRuleCOS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 20),
    _F3L3AclRuleCOS_Type()
)
f3L3AclRuleCOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleCOS.setStatus("current")
_F3L3AclRuleOperation_Type = L3AclRuleOperation
_F3L3AclRuleOperation_Object = MibTableColumn
f3L3AclRuleOperation = _F3L3AclRuleOperation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 21),
    _F3L3AclRuleOperation_Type()
)
f3L3AclRuleOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleOperation.setStatus("current")
_F3L3AclRuleSummary_Type = F3DisplayString
_F3L3AclRuleSummary_Object = MibTableColumn
f3L3AclRuleSummary = _F3L3AclRuleSummary_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 22),
    _F3L3AclRuleSummary_Type()
)
f3L3AclRuleSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3AclRuleSummary.setStatus("current")
_F3L3AclRuleCosOverrideControl_Type = TruthValue
_F3L3AclRuleCosOverrideControl_Object = MibTableColumn
f3L3AclRuleCosOverrideControl = _F3L3AclRuleCosOverrideControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 23),
    _F3L3AclRuleCosOverrideControl_Type()
)
f3L3AclRuleCosOverrideControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleCosOverrideControl.setStatus("current")
_F3L3AclRuleSrcMacAddressControl_Type = TruthValue
_F3L3AclRuleSrcMacAddressControl_Object = MibTableColumn
f3L3AclRuleSrcMacAddressControl = _F3L3AclRuleSrcMacAddressControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 24),
    _F3L3AclRuleSrcMacAddressControl_Type()
)
f3L3AclRuleSrcMacAddressControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleSrcMacAddressControl.setStatus("current")
_F3L3AclRuleDynamicSrcMacAddressControl_Type = TruthValue
_F3L3AclRuleDynamicSrcMacAddressControl_Object = MibTableColumn
f3L3AclRuleDynamicSrcMacAddressControl = _F3L3AclRuleDynamicSrcMacAddressControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 25),
    _F3L3AclRuleDynamicSrcMacAddressControl_Type()
)
f3L3AclRuleDynamicSrcMacAddressControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleDynamicSrcMacAddressControl.setStatus("current")
_F3L3AclRuleSrcMacAddress_Type = MacAddress
_F3L3AclRuleSrcMacAddress_Object = MibTableColumn
f3L3AclRuleSrcMacAddress = _F3L3AclRuleSrcMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 26),
    _F3L3AclRuleSrcMacAddress_Type()
)
f3L3AclRuleSrcMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleSrcMacAddress.setStatus("current")
_F3L3AclRuleSrcMacAddressMask_Type = MacAddress
_F3L3AclRuleSrcMacAddressMask_Object = MibTableColumn
f3L3AclRuleSrcMacAddressMask = _F3L3AclRuleSrcMacAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 27),
    _F3L3AclRuleSrcMacAddressMask_Type()
)
f3L3AclRuleSrcMacAddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleSrcMacAddressMask.setStatus("current")
_F3L3AclRuleDstMacAddressControl_Type = TruthValue
_F3L3AclRuleDstMacAddressControl_Object = MibTableColumn
f3L3AclRuleDstMacAddressControl = _F3L3AclRuleDstMacAddressControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 28),
    _F3L3AclRuleDstMacAddressControl_Type()
)
f3L3AclRuleDstMacAddressControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleDstMacAddressControl.setStatus("current")
_F3L3AclRuleDstMacAddress_Type = MacAddress
_F3L3AclRuleDstMacAddress_Object = MibTableColumn
f3L3AclRuleDstMacAddress = _F3L3AclRuleDstMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 29),
    _F3L3AclRuleDstMacAddress_Type()
)
f3L3AclRuleDstMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleDstMacAddress.setStatus("current")
_F3L3AclRuleDstMacAddressMask_Type = MacAddress
_F3L3AclRuleDstMacAddressMask_Object = MibTableColumn
f3L3AclRuleDstMacAddressMask = _F3L3AclRuleDstMacAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 30),
    _F3L3AclRuleDstMacAddressMask_Type()
)
f3L3AclRuleDstMacAddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleDstMacAddressMask.setStatus("current")
_F3L3AclRuleOuterVlanVIDControl_Type = TruthValue
_F3L3AclRuleOuterVlanVIDControl_Object = MibTableColumn
f3L3AclRuleOuterVlanVIDControl = _F3L3AclRuleOuterVlanVIDControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 31),
    _F3L3AclRuleOuterVlanVIDControl_Type()
)
f3L3AclRuleOuterVlanVIDControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleOuterVlanVIDControl.setStatus("current")
_F3L3AclRuleOuterVlanVIDLowLimit_Type = VlanId
_F3L3AclRuleOuterVlanVIDLowLimit_Object = MibTableColumn
f3L3AclRuleOuterVlanVIDLowLimit = _F3L3AclRuleOuterVlanVIDLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 32),
    _F3L3AclRuleOuterVlanVIDLowLimit_Type()
)
f3L3AclRuleOuterVlanVIDLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleOuterVlanVIDLowLimit.setStatus("current")
_F3L3AclRuleOuterVlanVIDHighLimit_Type = VlanId
_F3L3AclRuleOuterVlanVIDHighLimit_Object = MibTableColumn
f3L3AclRuleOuterVlanVIDHighLimit = _F3L3AclRuleOuterVlanVIDHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 33),
    _F3L3AclRuleOuterVlanVIDHighLimit_Type()
)
f3L3AclRuleOuterVlanVIDHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleOuterVlanVIDHighLimit.setStatus("current")
_F3L3AclRuleInnerVlanVIDControl_Type = TruthValue
_F3L3AclRuleInnerVlanVIDControl_Object = MibTableColumn
f3L3AclRuleInnerVlanVIDControl = _F3L3AclRuleInnerVlanVIDControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 34),
    _F3L3AclRuleInnerVlanVIDControl_Type()
)
f3L3AclRuleInnerVlanVIDControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleInnerVlanVIDControl.setStatus("current")
_F3L3AclRuleInnerVlanVIDLowLimit_Type = VlanId
_F3L3AclRuleInnerVlanVIDLowLimit_Object = MibTableColumn
f3L3AclRuleInnerVlanVIDLowLimit = _F3L3AclRuleInnerVlanVIDLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 35),
    _F3L3AclRuleInnerVlanVIDLowLimit_Type()
)
f3L3AclRuleInnerVlanVIDLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleInnerVlanVIDLowLimit.setStatus("current")
_F3L3AclRuleInnerVlanVIDHighLimit_Type = VlanId
_F3L3AclRuleInnerVlanVIDHighLimit_Object = MibTableColumn
f3L3AclRuleInnerVlanVIDHighLimit = _F3L3AclRuleInnerVlanVIDHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 36),
    _F3L3AclRuleInnerVlanVIDHighLimit_Type()
)
f3L3AclRuleInnerVlanVIDHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleInnerVlanVIDHighLimit.setStatus("current")
_F3L3AclRuleOuterVlanPcpControl_Type = TruthValue
_F3L3AclRuleOuterVlanPcpControl_Object = MibTableColumn
f3L3AclRuleOuterVlanPcpControl = _F3L3AclRuleOuterVlanPcpControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 37),
    _F3L3AclRuleOuterVlanPcpControl_Type()
)
f3L3AclRuleOuterVlanPcpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleOuterVlanPcpControl.setStatus("current")
_F3L3AclRuleOuterVlanPcpLowLimit_Type = VlanPriority
_F3L3AclRuleOuterVlanPcpLowLimit_Object = MibTableColumn
f3L3AclRuleOuterVlanPcpLowLimit = _F3L3AclRuleOuterVlanPcpLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 38),
    _F3L3AclRuleOuterVlanPcpLowLimit_Type()
)
f3L3AclRuleOuterVlanPcpLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleOuterVlanPcpLowLimit.setStatus("current")
_F3L3AclRuleOuterVlanPcpHighLimit_Type = VlanPriority
_F3L3AclRuleOuterVlanPcpHighLimit_Object = MibTableColumn
f3L3AclRuleOuterVlanPcpHighLimit = _F3L3AclRuleOuterVlanPcpHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 39),
    _F3L3AclRuleOuterVlanPcpHighLimit_Type()
)
f3L3AclRuleOuterVlanPcpHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleOuterVlanPcpHighLimit.setStatus("current")
_F3L3AclRuleInnerVlanPcpControl_Type = TruthValue
_F3L3AclRuleInnerVlanPcpControl_Object = MibTableColumn
f3L3AclRuleInnerVlanPcpControl = _F3L3AclRuleInnerVlanPcpControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 40),
    _F3L3AclRuleInnerVlanPcpControl_Type()
)
f3L3AclRuleInnerVlanPcpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleInnerVlanPcpControl.setStatus("current")
_F3L3AclRuleInnerVlanPcpLowLimit_Type = VlanPriority
_F3L3AclRuleInnerVlanPcpLowLimit_Object = MibTableColumn
f3L3AclRuleInnerVlanPcpLowLimit = _F3L3AclRuleInnerVlanPcpLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 41),
    _F3L3AclRuleInnerVlanPcpLowLimit_Type()
)
f3L3AclRuleInnerVlanPcpLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleInnerVlanPcpLowLimit.setStatus("current")
_F3L3AclRuleInnerVlanPcpHighLimit_Type = VlanPriority
_F3L3AclRuleInnerVlanPcpHighLimit_Object = MibTableColumn
f3L3AclRuleInnerVlanPcpHighLimit = _F3L3AclRuleInnerVlanPcpHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 42),
    _F3L3AclRuleInnerVlanPcpHighLimit_Type()
)
f3L3AclRuleInnerVlanPcpHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleInnerVlanPcpHighLimit.setStatus("current")
_F3L3AclRuleOuterVlanDeiControl_Type = TruthValue
_F3L3AclRuleOuterVlanDeiControl_Object = MibTableColumn
f3L3AclRuleOuterVlanDeiControl = _F3L3AclRuleOuterVlanDeiControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 43),
    _F3L3AclRuleOuterVlanDeiControl_Type()
)
f3L3AclRuleOuterVlanDeiControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleOuterVlanDeiControl.setStatus("current")


class _F3L3AclRuleOuterVlanDei_Type(Unsigned32):
    """Custom type f3L3AclRuleOuterVlanDei based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_F3L3AclRuleOuterVlanDei_Type.__name__ = "Unsigned32"
_F3L3AclRuleOuterVlanDei_Object = MibTableColumn
f3L3AclRuleOuterVlanDei = _F3L3AclRuleOuterVlanDei_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 44),
    _F3L3AclRuleOuterVlanDei_Type()
)
f3L3AclRuleOuterVlanDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleOuterVlanDei.setStatus("current")
_F3L3AclRuleEtherTypeControl_Type = TruthValue
_F3L3AclRuleEtherTypeControl_Object = MibTableColumn
f3L3AclRuleEtherTypeControl = _F3L3AclRuleEtherTypeControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 45),
    _F3L3AclRuleEtherTypeControl_Type()
)
f3L3AclRuleEtherTypeControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleEtherTypeControl.setStatus("current")
_F3L3AclRuleEtherType_Type = Integer32
_F3L3AclRuleEtherType_Object = MibTableColumn
f3L3AclRuleEtherType = _F3L3AclRuleEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 46),
    _F3L3AclRuleEtherType_Type()
)
f3L3AclRuleEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleEtherType.setStatus("current")
_F3L3AclRuleTcpFlagsControl_Type = TruthValue
_F3L3AclRuleTcpFlagsControl_Object = MibTableColumn
f3L3AclRuleTcpFlagsControl = _F3L3AclRuleTcpFlagsControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 47),
    _F3L3AclRuleTcpFlagsControl_Type()
)
f3L3AclRuleTcpFlagsControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleTcpFlagsControl.setStatus("current")
_F3L3AclRuleTcpFlags_Type = Integer32
_F3L3AclRuleTcpFlags_Object = MibTableColumn
f3L3AclRuleTcpFlags = _F3L3AclRuleTcpFlags_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 48),
    _F3L3AclRuleTcpFlags_Type()
)
f3L3AclRuleTcpFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleTcpFlags.setStatus("current")
_F3L3AclRuleSrcIpv4AddressHighLimit_Type = IpAddress
_F3L3AclRuleSrcIpv4AddressHighLimit_Object = MibTableColumn
f3L3AclRuleSrcIpv4AddressHighLimit = _F3L3AclRuleSrcIpv4AddressHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 49),
    _F3L3AclRuleSrcIpv4AddressHighLimit_Type()
)
f3L3AclRuleSrcIpv4AddressHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleSrcIpv4AddressHighLimit.setStatus("current")
_F3L3AclRuleDstIpv4AddressHighLimit_Type = IpAddress
_F3L3AclRuleDstIpv4AddressHighLimit_Object = MibTableColumn
f3L3AclRuleDstIpv4AddressHighLimit = _F3L3AclRuleDstIpv4AddressHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 50),
    _F3L3AclRuleDstIpv4AddressHighLimit_Type()
)
f3L3AclRuleDstIpv4AddressHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleDstIpv4AddressHighLimit.setStatus("current")
_F3L3AclRuleIpv4PriorityHighLimit_Type = Integer32
_F3L3AclRuleIpv4PriorityHighLimit_Object = MibTableColumn
f3L3AclRuleIpv4PriorityHighLimit = _F3L3AclRuleIpv4PriorityHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 51),
    _F3L3AclRuleIpv4PriorityHighLimit_Type()
)
f3L3AclRuleIpv4PriorityHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleIpv4PriorityHighLimit.setStatus("deprecated")
_F3L3AclRuleStorageType_Type = StorageType
_F3L3AclRuleStorageType_Object = MibTableColumn
f3L3AclRuleStorageType = _F3L3AclRuleStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 52),
    _F3L3AclRuleStorageType_Type()
)
f3L3AclRuleStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3AclRuleStorageType.setStatus("current")
_F3L3AclRuleRowStatus_Type = RowStatus
_F3L3AclRuleRowStatus_Object = MibTableColumn
f3L3AclRuleRowStatus = _F3L3AclRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 53),
    _F3L3AclRuleRowStatus_Type()
)
f3L3AclRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3AclRuleRowStatus.setStatus("current")
_F3L3AclRuleAdminState_Type = AdminState
_F3L3AclRuleAdminState_Object = MibTableColumn
f3L3AclRuleAdminState = _F3L3AclRuleAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 54),
    _F3L3AclRuleAdminState_Type()
)
f3L3AclRuleAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleAdminState.setStatus("current")
_F3L3AclRuleActive_Type = TruthValue
_F3L3AclRuleActive_Object = MibTableColumn
f3L3AclRuleActive = _F3L3AclRuleActive_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 55),
    _F3L3AclRuleActive_Type()
)
f3L3AclRuleActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleActive.setStatus("current")
_F3L3AclRuleSrcIpV6AddressControl_Type = TruthValue
_F3L3AclRuleSrcIpV6AddressControl_Object = MibTableColumn
f3L3AclRuleSrcIpV6AddressControl = _F3L3AclRuleSrcIpV6AddressControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 56),
    _F3L3AclRuleSrcIpV6AddressControl_Type()
)
f3L3AclRuleSrcIpV6AddressControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleSrcIpV6AddressControl.setStatus("current")
_F3L3AclRuleSrcIpV6Address_Type = Ipv6Address
_F3L3AclRuleSrcIpV6Address_Object = MibTableColumn
f3L3AclRuleSrcIpV6Address = _F3L3AclRuleSrcIpV6Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 57),
    _F3L3AclRuleSrcIpV6Address_Type()
)
f3L3AclRuleSrcIpV6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleSrcIpV6Address.setStatus("current")


class _F3L3AclRuleSrcIpV6AddressPrefixLen_Type(Integer32):
    """Custom type f3L3AclRuleSrcIpV6AddressPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_F3L3AclRuleSrcIpV6AddressPrefixLen_Type.__name__ = "Integer32"
_F3L3AclRuleSrcIpV6AddressPrefixLen_Object = MibTableColumn
f3L3AclRuleSrcIpV6AddressPrefixLen = _F3L3AclRuleSrcIpV6AddressPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 58),
    _F3L3AclRuleSrcIpV6AddressPrefixLen_Type()
)
f3L3AclRuleSrcIpV6AddressPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleSrcIpV6AddressPrefixLen.setStatus("current")
_F3L3AclRuleDstIpV6AddressControl_Type = TruthValue
_F3L3AclRuleDstIpV6AddressControl_Object = MibTableColumn
f3L3AclRuleDstIpV6AddressControl = _F3L3AclRuleDstIpV6AddressControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 59),
    _F3L3AclRuleDstIpV6AddressControl_Type()
)
f3L3AclRuleDstIpV6AddressControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleDstIpV6AddressControl.setStatus("current")
_F3L3AclRuleDstIpV6Address_Type = Ipv6Address
_F3L3AclRuleDstIpV6Address_Object = MibTableColumn
f3L3AclRuleDstIpV6Address = _F3L3AclRuleDstIpV6Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 60),
    _F3L3AclRuleDstIpV6Address_Type()
)
f3L3AclRuleDstIpV6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleDstIpV6Address.setStatus("current")


class _F3L3AclRuleDstIpV6AddressPrefixLen_Type(Integer32):
    """Custom type f3L3AclRuleDstIpV6AddressPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_F3L3AclRuleDstIpV6AddressPrefixLen_Type.__name__ = "Integer32"
_F3L3AclRuleDstIpV6AddressPrefixLen_Object = MibTableColumn
f3L3AclRuleDstIpV6AddressPrefixLen = _F3L3AclRuleDstIpV6AddressPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 61),
    _F3L3AclRuleDstIpV6AddressPrefixLen_Type()
)
f3L3AclRuleDstIpV6AddressPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleDstIpV6AddressPrefixLen.setStatus("current")
_F3L3AclRuleIpV6FlowLabelControl_Type = TruthValue
_F3L3AclRuleIpV6FlowLabelControl_Object = MibTableColumn
f3L3AclRuleIpV6FlowLabelControl = _F3L3AclRuleIpV6FlowLabelControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 62),
    _F3L3AclRuleIpV6FlowLabelControl_Type()
)
f3L3AclRuleIpV6FlowLabelControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleIpV6FlowLabelControl.setStatus("current")


class _F3L3AclRuleIpV6FlowLabel_Type(Integer32):
    """Custom type f3L3AclRuleIpV6FlowLabel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_F3L3AclRuleIpV6FlowLabel_Type.__name__ = "Integer32"
_F3L3AclRuleIpV6FlowLabel_Object = MibTableColumn
f3L3AclRuleIpV6FlowLabel = _F3L3AclRuleIpV6FlowLabel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 63),
    _F3L3AclRuleIpV6FlowLabel_Type()
)
f3L3AclRuleIpV6FlowLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleIpV6FlowLabel.setStatus("current")
_F3L3AclRulePriorityControl_Type = TruthValue
_F3L3AclRulePriorityControl_Object = MibTableColumn
f3L3AclRulePriorityControl = _F3L3AclRulePriorityControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 64),
    _F3L3AclRulePriorityControl_Type()
)
f3L3AclRulePriorityControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRulePriorityControl.setStatus("current")
_F3L3AclRulePriorityLowLimit_Type = Integer32
_F3L3AclRulePriorityLowLimit_Object = MibTableColumn
f3L3AclRulePriorityLowLimit = _F3L3AclRulePriorityLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 65),
    _F3L3AclRulePriorityLowLimit_Type()
)
f3L3AclRulePriorityLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRulePriorityLowLimit.setStatus("current")
_F3L3AclRulePriorityHighLimit_Type = Integer32
_F3L3AclRulePriorityHighLimit_Object = MibTableColumn
f3L3AclRulePriorityHighLimit = _F3L3AclRulePriorityHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 4, 1, 66),
    _F3L3AclRulePriorityHighLimit_Type()
)
f3L3AclRulePriorityHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRulePriorityHighLimit.setStatus("current")
_F3L2A2NAclRuleTable_Object = MibTable
f3L2A2NAclRuleTable = _F3L2A2NAclRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5)
)
if mibBuilder.loadTexts:
    f3L2A2NAclRuleTable.setStatus("current")
_F3L2A2NAclRuleEntry_Object = MibTableRow
f3L2A2NAclRuleEntry = _F3L2A2NAclRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1)
)
f3L2A2NAclRuleEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L2A2NAclRuleParentIndex"),
    (0, "F3-L3-MIB", "f3L2A2NAclRuleIndex"),
)
if mibBuilder.loadTexts:
    f3L2A2NAclRuleEntry.setStatus("current")
_F3L2A2NAclRuleParentIndex_Type = Integer32
_F3L2A2NAclRuleParentIndex_Object = MibTableColumn
f3L2A2NAclRuleParentIndex = _F3L2A2NAclRuleParentIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 1),
    _F3L2A2NAclRuleParentIndex_Type()
)
f3L2A2NAclRuleParentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleParentIndex.setStatus("current")
_F3L2A2NAclRuleIndex_Type = Integer32
_F3L2A2NAclRuleIndex_Object = MibTableColumn
f3L2A2NAclRuleIndex = _F3L2A2NAclRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 2),
    _F3L2A2NAclRuleIndex_Type()
)
f3L2A2NAclRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleIndex.setStatus("current")


class _F3L2A2NAclRuleAlias_Type(F3DisplayString):
    """Custom type f3L2A2NAclRuleAlias based on F3DisplayString"""
    subtypeSpec = F3DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_F3L2A2NAclRuleAlias_Type.__name__ = "F3DisplayString"
_F3L2A2NAclRuleAlias_Object = MibTableColumn
f3L2A2NAclRuleAlias = _F3L2A2NAclRuleAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 3),
    _F3L2A2NAclRuleAlias_Type()
)
f3L2A2NAclRuleAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleAlias.setStatus("current")
_F3L2A2NAclRuleSrcIpv4AddressControl_Type = TruthValue
_F3L2A2NAclRuleSrcIpv4AddressControl_Object = MibTableColumn
f3L2A2NAclRuleSrcIpv4AddressControl = _F3L2A2NAclRuleSrcIpv4AddressControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 4),
    _F3L2A2NAclRuleSrcIpv4AddressControl_Type()
)
f3L2A2NAclRuleSrcIpv4AddressControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleSrcIpv4AddressControl.setStatus("current")
_F3L2A2NAclRuleDynamicSrcIpControl_Type = TruthValue
_F3L2A2NAclRuleDynamicSrcIpControl_Object = MibTableColumn
f3L2A2NAclRuleDynamicSrcIpControl = _F3L2A2NAclRuleDynamicSrcIpControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 5),
    _F3L2A2NAclRuleDynamicSrcIpControl_Type()
)
f3L2A2NAclRuleDynamicSrcIpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleDynamicSrcIpControl.setStatus("current")
_F3L2A2NAclRuleSrcIpv4AddressLowLimit_Type = IpAddress
_F3L2A2NAclRuleSrcIpv4AddressLowLimit_Object = MibTableColumn
f3L2A2NAclRuleSrcIpv4AddressLowLimit = _F3L2A2NAclRuleSrcIpv4AddressLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 6),
    _F3L2A2NAclRuleSrcIpv4AddressLowLimit_Type()
)
f3L2A2NAclRuleSrcIpv4AddressLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleSrcIpv4AddressLowLimit.setStatus("current")
_F3L2A2NAclRuleDstIpv4AddressControl_Type = TruthValue
_F3L2A2NAclRuleDstIpv4AddressControl_Object = MibTableColumn
f3L2A2NAclRuleDstIpv4AddressControl = _F3L2A2NAclRuleDstIpv4AddressControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 7),
    _F3L2A2NAclRuleDstIpv4AddressControl_Type()
)
f3L2A2NAclRuleDstIpv4AddressControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleDstIpv4AddressControl.setStatus("current")
_F3L2A2NAclRuleDstIpv4AddressLowLimit_Type = IpAddress
_F3L2A2NAclRuleDstIpv4AddressLowLimit_Object = MibTableColumn
f3L2A2NAclRuleDstIpv4AddressLowLimit = _F3L2A2NAclRuleDstIpv4AddressLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 8),
    _F3L2A2NAclRuleDstIpv4AddressLowLimit_Type()
)
f3L2A2NAclRuleDstIpv4AddressLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleDstIpv4AddressLowLimit.setStatus("current")
_F3L2A2NAclRuleIpv4PriorityControl_Type = TruthValue
_F3L2A2NAclRuleIpv4PriorityControl_Object = MibTableColumn
f3L2A2NAclRuleIpv4PriorityControl = _F3L2A2NAclRuleIpv4PriorityControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 9),
    _F3L2A2NAclRuleIpv4PriorityControl_Type()
)
f3L2A2NAclRuleIpv4PriorityControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleIpv4PriorityControl.setStatus("current")
_F3L2A2NAclRuleIpv4PriorityLowLimit_Type = Integer32
_F3L2A2NAclRuleIpv4PriorityLowLimit_Object = MibTableColumn
f3L2A2NAclRuleIpv4PriorityLowLimit = _F3L2A2NAclRuleIpv4PriorityLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 10),
    _F3L2A2NAclRuleIpv4PriorityLowLimit_Type()
)
f3L2A2NAclRuleIpv4PriorityLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleIpv4PriorityLowLimit.setStatus("current")
_F3L2A2NAclRuleProtocolControl_Type = TruthValue
_F3L2A2NAclRuleProtocolControl_Object = MibTableColumn
f3L2A2NAclRuleProtocolControl = _F3L2A2NAclRuleProtocolControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 11),
    _F3L2A2NAclRuleProtocolControl_Type()
)
f3L2A2NAclRuleProtocolControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleProtocolControl.setStatus("current")
_F3L2A2NAclRuleProtocolNumber_Type = Integer32
_F3L2A2NAclRuleProtocolNumber_Object = MibTableColumn
f3L2A2NAclRuleProtocolNumber = _F3L2A2NAclRuleProtocolNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 12),
    _F3L2A2NAclRuleProtocolNumber_Type()
)
f3L2A2NAclRuleProtocolNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleProtocolNumber.setStatus("current")
_F3L2A2NAclRuleSrcPortControl_Type = TruthValue
_F3L2A2NAclRuleSrcPortControl_Object = MibTableColumn
f3L2A2NAclRuleSrcPortControl = _F3L2A2NAclRuleSrcPortControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 13),
    _F3L2A2NAclRuleSrcPortControl_Type()
)
f3L2A2NAclRuleSrcPortControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleSrcPortControl.setStatus("current")
_F3L2A2NAclRuleSrcPortLowLimit_Type = Integer32
_F3L2A2NAclRuleSrcPortLowLimit_Object = MibTableColumn
f3L2A2NAclRuleSrcPortLowLimit = _F3L2A2NAclRuleSrcPortLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 14),
    _F3L2A2NAclRuleSrcPortLowLimit_Type()
)
f3L2A2NAclRuleSrcPortLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleSrcPortLowLimit.setStatus("current")
_F3L2A2NAclRuleSrcPortHighLimit_Type = Integer32
_F3L2A2NAclRuleSrcPortHighLimit_Object = MibTableColumn
f3L2A2NAclRuleSrcPortHighLimit = _F3L2A2NAclRuleSrcPortHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 15),
    _F3L2A2NAclRuleSrcPortHighLimit_Type()
)
f3L2A2NAclRuleSrcPortHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleSrcPortHighLimit.setStatus("current")
_F3L2A2NAclRuleDstPortControl_Type = TruthValue
_F3L2A2NAclRuleDstPortControl_Object = MibTableColumn
f3L2A2NAclRuleDstPortControl = _F3L2A2NAclRuleDstPortControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 16),
    _F3L2A2NAclRuleDstPortControl_Type()
)
f3L2A2NAclRuleDstPortControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleDstPortControl.setStatus("current")
_F3L2A2NAclRuleDstPortLowLimit_Type = Integer32
_F3L2A2NAclRuleDstPortLowLimit_Object = MibTableColumn
f3L2A2NAclRuleDstPortLowLimit = _F3L2A2NAclRuleDstPortLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 17),
    _F3L2A2NAclRuleDstPortLowLimit_Type()
)
f3L2A2NAclRuleDstPortLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleDstPortLowLimit.setStatus("current")
_F3L2A2NAclRuleDstPortHighLimit_Type = Integer32
_F3L2A2NAclRuleDstPortHighLimit_Object = MibTableColumn
f3L2A2NAclRuleDstPortHighLimit = _F3L2A2NAclRuleDstPortHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 18),
    _F3L2A2NAclRuleDstPortHighLimit_Type()
)
f3L2A2NAclRuleDstPortHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleDstPortHighLimit.setStatus("current")
_F3L2A2NAclRulePriority_Type = Integer32
_F3L2A2NAclRulePriority_Object = MibTableColumn
f3L2A2NAclRulePriority = _F3L2A2NAclRulePriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 19),
    _F3L2A2NAclRulePriority_Type()
)
f3L2A2NAclRulePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRulePriority.setStatus("current")
_F3L2A2NAclRuleCOS_Type = Integer32
_F3L2A2NAclRuleCOS_Object = MibTableColumn
f3L2A2NAclRuleCOS = _F3L2A2NAclRuleCOS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 20),
    _F3L2A2NAclRuleCOS_Type()
)
f3L2A2NAclRuleCOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleCOS.setStatus("current")
_F3L2A2NAclRuleOperation_Type = L3AclRuleOperation
_F3L2A2NAclRuleOperation_Object = MibTableColumn
f3L2A2NAclRuleOperation = _F3L2A2NAclRuleOperation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 21),
    _F3L2A2NAclRuleOperation_Type()
)
f3L2A2NAclRuleOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleOperation.setStatus("current")
_F3L2A2NAclRuleSummary_Type = F3DisplayString
_F3L2A2NAclRuleSummary_Object = MibTableColumn
f3L2A2NAclRuleSummary = _F3L2A2NAclRuleSummary_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 22),
    _F3L2A2NAclRuleSummary_Type()
)
f3L2A2NAclRuleSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleSummary.setStatus("current")
_F3L2A2NAclRuleCosOverrideControl_Type = TruthValue
_F3L2A2NAclRuleCosOverrideControl_Object = MibTableColumn
f3L2A2NAclRuleCosOverrideControl = _F3L2A2NAclRuleCosOverrideControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 23),
    _F3L2A2NAclRuleCosOverrideControl_Type()
)
f3L2A2NAclRuleCosOverrideControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleCosOverrideControl.setStatus("current")
_F3L2A2NAclRuleSrcMacAddressControl_Type = TruthValue
_F3L2A2NAclRuleSrcMacAddressControl_Object = MibTableColumn
f3L2A2NAclRuleSrcMacAddressControl = _F3L2A2NAclRuleSrcMacAddressControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 24),
    _F3L2A2NAclRuleSrcMacAddressControl_Type()
)
f3L2A2NAclRuleSrcMacAddressControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleSrcMacAddressControl.setStatus("current")
_F3L2A2NAclRuleDynamicSrcMacAddressControl_Type = TruthValue
_F3L2A2NAclRuleDynamicSrcMacAddressControl_Object = MibTableColumn
f3L2A2NAclRuleDynamicSrcMacAddressControl = _F3L2A2NAclRuleDynamicSrcMacAddressControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 25),
    _F3L2A2NAclRuleDynamicSrcMacAddressControl_Type()
)
f3L2A2NAclRuleDynamicSrcMacAddressControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleDynamicSrcMacAddressControl.setStatus("current")
_F3L2A2NAclRuleSrcMacAddress_Type = MacAddress
_F3L2A2NAclRuleSrcMacAddress_Object = MibTableColumn
f3L2A2NAclRuleSrcMacAddress = _F3L2A2NAclRuleSrcMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 26),
    _F3L2A2NAclRuleSrcMacAddress_Type()
)
f3L2A2NAclRuleSrcMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleSrcMacAddress.setStatus("current")
_F3L2A2NAclRuleSrcMacAddressMask_Type = MacAddress
_F3L2A2NAclRuleSrcMacAddressMask_Object = MibTableColumn
f3L2A2NAclRuleSrcMacAddressMask = _F3L2A2NAclRuleSrcMacAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 27),
    _F3L2A2NAclRuleSrcMacAddressMask_Type()
)
f3L2A2NAclRuleSrcMacAddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleSrcMacAddressMask.setStatus("current")
_F3L2A2NAclRuleDstMacAddressControl_Type = TruthValue
_F3L2A2NAclRuleDstMacAddressControl_Object = MibTableColumn
f3L2A2NAclRuleDstMacAddressControl = _F3L2A2NAclRuleDstMacAddressControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 28),
    _F3L2A2NAclRuleDstMacAddressControl_Type()
)
f3L2A2NAclRuleDstMacAddressControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleDstMacAddressControl.setStatus("current")
_F3L2A2NAclRuleDstMacAddress_Type = MacAddress
_F3L2A2NAclRuleDstMacAddress_Object = MibTableColumn
f3L2A2NAclRuleDstMacAddress = _F3L2A2NAclRuleDstMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 29),
    _F3L2A2NAclRuleDstMacAddress_Type()
)
f3L2A2NAclRuleDstMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleDstMacAddress.setStatus("current")
_F3L2A2NAclRuleDstMacAddressMask_Type = MacAddress
_F3L2A2NAclRuleDstMacAddressMask_Object = MibTableColumn
f3L2A2NAclRuleDstMacAddressMask = _F3L2A2NAclRuleDstMacAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 30),
    _F3L2A2NAclRuleDstMacAddressMask_Type()
)
f3L2A2NAclRuleDstMacAddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleDstMacAddressMask.setStatus("current")
_F3L2A2NAclRuleOuterVlanVIDControl_Type = TruthValue
_F3L2A2NAclRuleOuterVlanVIDControl_Object = MibTableColumn
f3L2A2NAclRuleOuterVlanVIDControl = _F3L2A2NAclRuleOuterVlanVIDControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 31),
    _F3L2A2NAclRuleOuterVlanVIDControl_Type()
)
f3L2A2NAclRuleOuterVlanVIDControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleOuterVlanVIDControl.setStatus("current")
_F3L2A2NAclRuleOuterVlanVIDLowLimit_Type = VlanId
_F3L2A2NAclRuleOuterVlanVIDLowLimit_Object = MibTableColumn
f3L2A2NAclRuleOuterVlanVIDLowLimit = _F3L2A2NAclRuleOuterVlanVIDLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 32),
    _F3L2A2NAclRuleOuterVlanVIDLowLimit_Type()
)
f3L2A2NAclRuleOuterVlanVIDLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleOuterVlanVIDLowLimit.setStatus("current")
_F3L2A2NAclRuleOuterVlanVIDHighLimit_Type = VlanId
_F3L2A2NAclRuleOuterVlanVIDHighLimit_Object = MibTableColumn
f3L2A2NAclRuleOuterVlanVIDHighLimit = _F3L2A2NAclRuleOuterVlanVIDHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 33),
    _F3L2A2NAclRuleOuterVlanVIDHighLimit_Type()
)
f3L2A2NAclRuleOuterVlanVIDHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleOuterVlanVIDHighLimit.setStatus("current")
_F3L2A2NAclRuleInnerVlanVIDControl_Type = TruthValue
_F3L2A2NAclRuleInnerVlanVIDControl_Object = MibTableColumn
f3L2A2NAclRuleInnerVlanVIDControl = _F3L2A2NAclRuleInnerVlanVIDControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 34),
    _F3L2A2NAclRuleInnerVlanVIDControl_Type()
)
f3L2A2NAclRuleInnerVlanVIDControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleInnerVlanVIDControl.setStatus("current")
_F3L2A2NAclRuleInnerVlanVIDLowLimit_Type = VlanId
_F3L2A2NAclRuleInnerVlanVIDLowLimit_Object = MibTableColumn
f3L2A2NAclRuleInnerVlanVIDLowLimit = _F3L2A2NAclRuleInnerVlanVIDLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 35),
    _F3L2A2NAclRuleInnerVlanVIDLowLimit_Type()
)
f3L2A2NAclRuleInnerVlanVIDLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleInnerVlanVIDLowLimit.setStatus("current")
_F3L2A2NAclRuleInnerVlanVIDHighLimit_Type = VlanId
_F3L2A2NAclRuleInnerVlanVIDHighLimit_Object = MibTableColumn
f3L2A2NAclRuleInnerVlanVIDHighLimit = _F3L2A2NAclRuleInnerVlanVIDHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 36),
    _F3L2A2NAclRuleInnerVlanVIDHighLimit_Type()
)
f3L2A2NAclRuleInnerVlanVIDHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleInnerVlanVIDHighLimit.setStatus("current")
_F3L2A2NAclRuleOuterVlanPcpControl_Type = TruthValue
_F3L2A2NAclRuleOuterVlanPcpControl_Object = MibTableColumn
f3L2A2NAclRuleOuterVlanPcpControl = _F3L2A2NAclRuleOuterVlanPcpControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 37),
    _F3L2A2NAclRuleOuterVlanPcpControl_Type()
)
f3L2A2NAclRuleOuterVlanPcpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleOuterVlanPcpControl.setStatus("current")
_F3L2A2NAclRuleOuterVlanPcpLowLimit_Type = VlanPriority
_F3L2A2NAclRuleOuterVlanPcpLowLimit_Object = MibTableColumn
f3L2A2NAclRuleOuterVlanPcpLowLimit = _F3L2A2NAclRuleOuterVlanPcpLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 38),
    _F3L2A2NAclRuleOuterVlanPcpLowLimit_Type()
)
f3L2A2NAclRuleOuterVlanPcpLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleOuterVlanPcpLowLimit.setStatus("current")
_F3L2A2NAclRuleOuterVlanPcpHighLimit_Type = VlanPriority
_F3L2A2NAclRuleOuterVlanPcpHighLimit_Object = MibTableColumn
f3L2A2NAclRuleOuterVlanPcpHighLimit = _F3L2A2NAclRuleOuterVlanPcpHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 39),
    _F3L2A2NAclRuleOuterVlanPcpHighLimit_Type()
)
f3L2A2NAclRuleOuterVlanPcpHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleOuterVlanPcpHighLimit.setStatus("current")
_F3L2A2NAclRuleInnerVlanPcpControl_Type = TruthValue
_F3L2A2NAclRuleInnerVlanPcpControl_Object = MibTableColumn
f3L2A2NAclRuleInnerVlanPcpControl = _F3L2A2NAclRuleInnerVlanPcpControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 40),
    _F3L2A2NAclRuleInnerVlanPcpControl_Type()
)
f3L2A2NAclRuleInnerVlanPcpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleInnerVlanPcpControl.setStatus("current")
_F3L2A2NAclRuleInnerVlanPcpLowLimit_Type = VlanPriority
_F3L2A2NAclRuleInnerVlanPcpLowLimit_Object = MibTableColumn
f3L2A2NAclRuleInnerVlanPcpLowLimit = _F3L2A2NAclRuleInnerVlanPcpLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 41),
    _F3L2A2NAclRuleInnerVlanPcpLowLimit_Type()
)
f3L2A2NAclRuleInnerVlanPcpLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleInnerVlanPcpLowLimit.setStatus("current")
_F3L2A2NAclRuleInnerVlanPcpHighLimit_Type = VlanPriority
_F3L2A2NAclRuleInnerVlanPcpHighLimit_Object = MibTableColumn
f3L2A2NAclRuleInnerVlanPcpHighLimit = _F3L2A2NAclRuleInnerVlanPcpHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 42),
    _F3L2A2NAclRuleInnerVlanPcpHighLimit_Type()
)
f3L2A2NAclRuleInnerVlanPcpHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleInnerVlanPcpHighLimit.setStatus("current")
_F3L2A2NAclRuleOuterVlanDeiControl_Type = TruthValue
_F3L2A2NAclRuleOuterVlanDeiControl_Object = MibTableColumn
f3L2A2NAclRuleOuterVlanDeiControl = _F3L2A2NAclRuleOuterVlanDeiControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 43),
    _F3L2A2NAclRuleOuterVlanDeiControl_Type()
)
f3L2A2NAclRuleOuterVlanDeiControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleOuterVlanDeiControl.setStatus("current")


class _F3L2A2NAclRuleOuterVlanDei_Type(Unsigned32):
    """Custom type f3L2A2NAclRuleOuterVlanDei based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_F3L2A2NAclRuleOuterVlanDei_Type.__name__ = "Unsigned32"
_F3L2A2NAclRuleOuterVlanDei_Object = MibTableColumn
f3L2A2NAclRuleOuterVlanDei = _F3L2A2NAclRuleOuterVlanDei_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 44),
    _F3L2A2NAclRuleOuterVlanDei_Type()
)
f3L2A2NAclRuleOuterVlanDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleOuterVlanDei.setStatus("current")
_F3L2A2NAclRuleEtherTypeControl_Type = TruthValue
_F3L2A2NAclRuleEtherTypeControl_Object = MibTableColumn
f3L2A2NAclRuleEtherTypeControl = _F3L2A2NAclRuleEtherTypeControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 45),
    _F3L2A2NAclRuleEtherTypeControl_Type()
)
f3L2A2NAclRuleEtherTypeControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleEtherTypeControl.setStatus("current")
_F3L2A2NAclRuleEtherType_Type = Integer32
_F3L2A2NAclRuleEtherType_Object = MibTableColumn
f3L2A2NAclRuleEtherType = _F3L2A2NAclRuleEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 46),
    _F3L2A2NAclRuleEtherType_Type()
)
f3L2A2NAclRuleEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleEtherType.setStatus("current")
_F3L2A2NAclRuleTcpFlagsControl_Type = TruthValue
_F3L2A2NAclRuleTcpFlagsControl_Object = MibTableColumn
f3L2A2NAclRuleTcpFlagsControl = _F3L2A2NAclRuleTcpFlagsControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 47),
    _F3L2A2NAclRuleTcpFlagsControl_Type()
)
f3L2A2NAclRuleTcpFlagsControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleTcpFlagsControl.setStatus("current")
_F3L2A2NAclRuleTcpFlags_Type = Integer32
_F3L2A2NAclRuleTcpFlags_Object = MibTableColumn
f3L2A2NAclRuleTcpFlags = _F3L2A2NAclRuleTcpFlags_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 48),
    _F3L2A2NAclRuleTcpFlags_Type()
)
f3L2A2NAclRuleTcpFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleTcpFlags.setStatus("current")
_F3L2A2NAclRuleSrcIpv4AddressHighLimit_Type = IpAddress
_F3L2A2NAclRuleSrcIpv4AddressHighLimit_Object = MibTableColumn
f3L2A2NAclRuleSrcIpv4AddressHighLimit = _F3L2A2NAclRuleSrcIpv4AddressHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 49),
    _F3L2A2NAclRuleSrcIpv4AddressHighLimit_Type()
)
f3L2A2NAclRuleSrcIpv4AddressHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleSrcIpv4AddressHighLimit.setStatus("current")
_F3L2A2NAclRuleDstIpv4AddressHighLimit_Type = IpAddress
_F3L2A2NAclRuleDstIpv4AddressHighLimit_Object = MibTableColumn
f3L2A2NAclRuleDstIpv4AddressHighLimit = _F3L2A2NAclRuleDstIpv4AddressHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 50),
    _F3L2A2NAclRuleDstIpv4AddressHighLimit_Type()
)
f3L2A2NAclRuleDstIpv4AddressHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleDstIpv4AddressHighLimit.setStatus("current")
_F3L2A2NAclRuleIpv4PriorityHighLimit_Type = Integer32
_F3L2A2NAclRuleIpv4PriorityHighLimit_Object = MibTableColumn
f3L2A2NAclRuleIpv4PriorityHighLimit = _F3L2A2NAclRuleIpv4PriorityHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 51),
    _F3L2A2NAclRuleIpv4PriorityHighLimit_Type()
)
f3L2A2NAclRuleIpv4PriorityHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleIpv4PriorityHighLimit.setStatus("current")
_F3L2A2NAclRuleStorageType_Type = StorageType
_F3L2A2NAclRuleStorageType_Object = MibTableColumn
f3L2A2NAclRuleStorageType = _F3L2A2NAclRuleStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 52),
    _F3L2A2NAclRuleStorageType_Type()
)
f3L2A2NAclRuleStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleStorageType.setStatus("current")
_F3L2A2NAclRuleRowStatus_Type = RowStatus
_F3L2A2NAclRuleRowStatus_Object = MibTableColumn
f3L2A2NAclRuleRowStatus = _F3L2A2NAclRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 53),
    _F3L2A2NAclRuleRowStatus_Type()
)
f3L2A2NAclRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleRowStatus.setStatus("current")
_F3L2A2NAclRuleAdminState_Type = AdminState
_F3L2A2NAclRuleAdminState_Object = MibTableColumn
f3L2A2NAclRuleAdminState = _F3L2A2NAclRuleAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 54),
    _F3L2A2NAclRuleAdminState_Type()
)
f3L2A2NAclRuleAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleAdminState.setStatus("current")
_F3L2A2NAclRuleActive_Type = TruthValue
_F3L2A2NAclRuleActive_Object = MibTableColumn
f3L2A2NAclRuleActive = _F3L2A2NAclRuleActive_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 55),
    _F3L2A2NAclRuleActive_Type()
)
f3L2A2NAclRuleActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleActive.setStatus("current")
_F3L2A2NAclRuleSrcIpV6AddressControl_Type = TruthValue
_F3L2A2NAclRuleSrcIpV6AddressControl_Object = MibTableColumn
f3L2A2NAclRuleSrcIpV6AddressControl = _F3L2A2NAclRuleSrcIpV6AddressControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 56),
    _F3L2A2NAclRuleSrcIpV6AddressControl_Type()
)
f3L2A2NAclRuleSrcIpV6AddressControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleSrcIpV6AddressControl.setStatus("current")
_F3L2A2NAclRuleSrcIpV6Address_Type = Ipv6Address
_F3L2A2NAclRuleSrcIpV6Address_Object = MibTableColumn
f3L2A2NAclRuleSrcIpV6Address = _F3L2A2NAclRuleSrcIpV6Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 57),
    _F3L2A2NAclRuleSrcIpV6Address_Type()
)
f3L2A2NAclRuleSrcIpV6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleSrcIpV6Address.setStatus("current")
_F3L2A2NAclRuleSrcIpV6AddressPrefixLen_Type = Integer32
_F3L2A2NAclRuleSrcIpV6AddressPrefixLen_Object = MibTableColumn
f3L2A2NAclRuleSrcIpV6AddressPrefixLen = _F3L2A2NAclRuleSrcIpV6AddressPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 58),
    _F3L2A2NAclRuleSrcIpV6AddressPrefixLen_Type()
)
f3L2A2NAclRuleSrcIpV6AddressPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleSrcIpV6AddressPrefixLen.setStatus("current")
_F3L2A2NAclRuleDstIpV6AddressControl_Type = TruthValue
_F3L2A2NAclRuleDstIpV6AddressControl_Object = MibTableColumn
f3L2A2NAclRuleDstIpV6AddressControl = _F3L2A2NAclRuleDstIpV6AddressControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 59),
    _F3L2A2NAclRuleDstIpV6AddressControl_Type()
)
f3L2A2NAclRuleDstIpV6AddressControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleDstIpV6AddressControl.setStatus("current")
_F3L2A2NAclRuleDstIpV6Address_Type = Ipv6Address
_F3L2A2NAclRuleDstIpV6Address_Object = MibTableColumn
f3L2A2NAclRuleDstIpV6Address = _F3L2A2NAclRuleDstIpV6Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 60),
    _F3L2A2NAclRuleDstIpV6Address_Type()
)
f3L2A2NAclRuleDstIpV6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleDstIpV6Address.setStatus("current")
_F3L2A2NAclRuleDstIpV6AddressPrefixLen_Type = Integer32
_F3L2A2NAclRuleDstIpV6AddressPrefixLen_Object = MibTableColumn
f3L2A2NAclRuleDstIpV6AddressPrefixLen = _F3L2A2NAclRuleDstIpV6AddressPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 61),
    _F3L2A2NAclRuleDstIpV6AddressPrefixLen_Type()
)
f3L2A2NAclRuleDstIpV6AddressPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleDstIpV6AddressPrefixLen.setStatus("current")
_F3L2A2NAclRuleIpV6FlowLabelControl_Type = TruthValue
_F3L2A2NAclRuleIpV6FlowLabelControl_Object = MibTableColumn
f3L2A2NAclRuleIpV6FlowLabelControl = _F3L2A2NAclRuleIpV6FlowLabelControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 62),
    _F3L2A2NAclRuleIpV6FlowLabelControl_Type()
)
f3L2A2NAclRuleIpV6FlowLabelControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleIpV6FlowLabelControl.setStatus("current")
_F3L2A2NAclRuleIpV6FlowLabel_Type = Integer32
_F3L2A2NAclRuleIpV6FlowLabel_Object = MibTableColumn
f3L2A2NAclRuleIpV6FlowLabel = _F3L2A2NAclRuleIpV6FlowLabel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 5, 1, 63),
    _F3L2A2NAclRuleIpV6FlowLabel_Type()
)
f3L2A2NAclRuleIpV6FlowLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleIpV6FlowLabel.setStatus("current")
_F3L2N2AAclRuleTable_Object = MibTable
f3L2N2AAclRuleTable = _F3L2N2AAclRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6)
)
if mibBuilder.loadTexts:
    f3L2N2AAclRuleTable.setStatus("current")
_F3L2N2AAclRuleEntry_Object = MibTableRow
f3L2N2AAclRuleEntry = _F3L2N2AAclRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1)
)
f3L2N2AAclRuleEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L2N2AAclRuleParentIndex"),
    (0, "F3-L3-MIB", "f3L2N2AAclRuleIndex"),
)
if mibBuilder.loadTexts:
    f3L2N2AAclRuleEntry.setStatus("current")
_F3L2N2AAclRuleParentIndex_Type = Integer32
_F3L2N2AAclRuleParentIndex_Object = MibTableColumn
f3L2N2AAclRuleParentIndex = _F3L2N2AAclRuleParentIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 1),
    _F3L2N2AAclRuleParentIndex_Type()
)
f3L2N2AAclRuleParentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleParentIndex.setStatus("current")
_F3L2N2AAclRuleIndex_Type = Integer32
_F3L2N2AAclRuleIndex_Object = MibTableColumn
f3L2N2AAclRuleIndex = _F3L2N2AAclRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 2),
    _F3L2N2AAclRuleIndex_Type()
)
f3L2N2AAclRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleIndex.setStatus("current")


class _F3L2N2AAclRuleAlias_Type(F3DisplayString):
    """Custom type f3L2N2AAclRuleAlias based on F3DisplayString"""
    subtypeSpec = F3DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_F3L2N2AAclRuleAlias_Type.__name__ = "F3DisplayString"
_F3L2N2AAclRuleAlias_Object = MibTableColumn
f3L2N2AAclRuleAlias = _F3L2N2AAclRuleAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 3),
    _F3L2N2AAclRuleAlias_Type()
)
f3L2N2AAclRuleAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleAlias.setStatus("current")
_F3L2N2AAclRuleSrcIpv4AddressControl_Type = TruthValue
_F3L2N2AAclRuleSrcIpv4AddressControl_Object = MibTableColumn
f3L2N2AAclRuleSrcIpv4AddressControl = _F3L2N2AAclRuleSrcIpv4AddressControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 4),
    _F3L2N2AAclRuleSrcIpv4AddressControl_Type()
)
f3L2N2AAclRuleSrcIpv4AddressControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleSrcIpv4AddressControl.setStatus("current")
_F3L2N2AAclRuleDynamicSrcIpControl_Type = TruthValue
_F3L2N2AAclRuleDynamicSrcIpControl_Object = MibTableColumn
f3L2N2AAclRuleDynamicSrcIpControl = _F3L2N2AAclRuleDynamicSrcIpControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 5),
    _F3L2N2AAclRuleDynamicSrcIpControl_Type()
)
f3L2N2AAclRuleDynamicSrcIpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleDynamicSrcIpControl.setStatus("current")
_F3L2N2AAclRuleSrcIpv4AddressLowLimit_Type = IpAddress
_F3L2N2AAclRuleSrcIpv4AddressLowLimit_Object = MibTableColumn
f3L2N2AAclRuleSrcIpv4AddressLowLimit = _F3L2N2AAclRuleSrcIpv4AddressLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 6),
    _F3L2N2AAclRuleSrcIpv4AddressLowLimit_Type()
)
f3L2N2AAclRuleSrcIpv4AddressLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleSrcIpv4AddressLowLimit.setStatus("current")
_F3L2N2AAclRuleDstIpv4AddressControl_Type = TruthValue
_F3L2N2AAclRuleDstIpv4AddressControl_Object = MibTableColumn
f3L2N2AAclRuleDstIpv4AddressControl = _F3L2N2AAclRuleDstIpv4AddressControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 7),
    _F3L2N2AAclRuleDstIpv4AddressControl_Type()
)
f3L2N2AAclRuleDstIpv4AddressControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleDstIpv4AddressControl.setStatus("current")
_F3L2N2AAclRuleDstIpv4AddressLowLimit_Type = IpAddress
_F3L2N2AAclRuleDstIpv4AddressLowLimit_Object = MibTableColumn
f3L2N2AAclRuleDstIpv4AddressLowLimit = _F3L2N2AAclRuleDstIpv4AddressLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 8),
    _F3L2N2AAclRuleDstIpv4AddressLowLimit_Type()
)
f3L2N2AAclRuleDstIpv4AddressLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleDstIpv4AddressLowLimit.setStatus("current")
_F3L2N2AAclRuleIpv4PriorityControl_Type = TruthValue
_F3L2N2AAclRuleIpv4PriorityControl_Object = MibTableColumn
f3L2N2AAclRuleIpv4PriorityControl = _F3L2N2AAclRuleIpv4PriorityControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 9),
    _F3L2N2AAclRuleIpv4PriorityControl_Type()
)
f3L2N2AAclRuleIpv4PriorityControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleIpv4PriorityControl.setStatus("current")
_F3L2N2AAclRuleIpv4PriorityLowLimit_Type = Integer32
_F3L2N2AAclRuleIpv4PriorityLowLimit_Object = MibTableColumn
f3L2N2AAclRuleIpv4PriorityLowLimit = _F3L2N2AAclRuleIpv4PriorityLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 10),
    _F3L2N2AAclRuleIpv4PriorityLowLimit_Type()
)
f3L2N2AAclRuleIpv4PriorityLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleIpv4PriorityLowLimit.setStatus("current")
_F3L2N2AAclRuleProtocolControl_Type = TruthValue
_F3L2N2AAclRuleProtocolControl_Object = MibTableColumn
f3L2N2AAclRuleProtocolControl = _F3L2N2AAclRuleProtocolControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 11),
    _F3L2N2AAclRuleProtocolControl_Type()
)
f3L2N2AAclRuleProtocolControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleProtocolControl.setStatus("current")
_F3L2N2AAclRuleProtocolNumber_Type = Integer32
_F3L2N2AAclRuleProtocolNumber_Object = MibTableColumn
f3L2N2AAclRuleProtocolNumber = _F3L2N2AAclRuleProtocolNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 12),
    _F3L2N2AAclRuleProtocolNumber_Type()
)
f3L2N2AAclRuleProtocolNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleProtocolNumber.setStatus("current")
_F3L2N2AAclRuleSrcPortControl_Type = TruthValue
_F3L2N2AAclRuleSrcPortControl_Object = MibTableColumn
f3L2N2AAclRuleSrcPortControl = _F3L2N2AAclRuleSrcPortControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 13),
    _F3L2N2AAclRuleSrcPortControl_Type()
)
f3L2N2AAclRuleSrcPortControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleSrcPortControl.setStatus("current")
_F3L2N2AAclRuleSrcPortLowLimit_Type = Integer32
_F3L2N2AAclRuleSrcPortLowLimit_Object = MibTableColumn
f3L2N2AAclRuleSrcPortLowLimit = _F3L2N2AAclRuleSrcPortLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 14),
    _F3L2N2AAclRuleSrcPortLowLimit_Type()
)
f3L2N2AAclRuleSrcPortLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleSrcPortLowLimit.setStatus("current")
_F3L2N2AAclRuleSrcPortHighLimit_Type = Integer32
_F3L2N2AAclRuleSrcPortHighLimit_Object = MibTableColumn
f3L2N2AAclRuleSrcPortHighLimit = _F3L2N2AAclRuleSrcPortHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 15),
    _F3L2N2AAclRuleSrcPortHighLimit_Type()
)
f3L2N2AAclRuleSrcPortHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleSrcPortHighLimit.setStatus("current")
_F3L2N2AAclRuleDstPortControl_Type = TruthValue
_F3L2N2AAclRuleDstPortControl_Object = MibTableColumn
f3L2N2AAclRuleDstPortControl = _F3L2N2AAclRuleDstPortControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 16),
    _F3L2N2AAclRuleDstPortControl_Type()
)
f3L2N2AAclRuleDstPortControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleDstPortControl.setStatus("current")
_F3L2N2AAclRuleDstPortLowLimit_Type = Integer32
_F3L2N2AAclRuleDstPortLowLimit_Object = MibTableColumn
f3L2N2AAclRuleDstPortLowLimit = _F3L2N2AAclRuleDstPortLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 17),
    _F3L2N2AAclRuleDstPortLowLimit_Type()
)
f3L2N2AAclRuleDstPortLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleDstPortLowLimit.setStatus("current")
_F3L2N2AAclRuleDstPortHighLimit_Type = Integer32
_F3L2N2AAclRuleDstPortHighLimit_Object = MibTableColumn
f3L2N2AAclRuleDstPortHighLimit = _F3L2N2AAclRuleDstPortHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 18),
    _F3L2N2AAclRuleDstPortHighLimit_Type()
)
f3L2N2AAclRuleDstPortHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleDstPortHighLimit.setStatus("current")
_F3L2N2AAclRulePriority_Type = Integer32
_F3L2N2AAclRulePriority_Object = MibTableColumn
f3L2N2AAclRulePriority = _F3L2N2AAclRulePriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 19),
    _F3L2N2AAclRulePriority_Type()
)
f3L2N2AAclRulePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRulePriority.setStatus("current")
_F3L2N2AAclRuleCOS_Type = Integer32
_F3L2N2AAclRuleCOS_Object = MibTableColumn
f3L2N2AAclRuleCOS = _F3L2N2AAclRuleCOS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 20),
    _F3L2N2AAclRuleCOS_Type()
)
f3L2N2AAclRuleCOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleCOS.setStatus("current")
_F3L2N2AAclRuleOperation_Type = L3AclRuleOperation
_F3L2N2AAclRuleOperation_Object = MibTableColumn
f3L2N2AAclRuleOperation = _F3L2N2AAclRuleOperation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 21),
    _F3L2N2AAclRuleOperation_Type()
)
f3L2N2AAclRuleOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleOperation.setStatus("current")
_F3L2N2AAclRuleSummary_Type = F3DisplayString
_F3L2N2AAclRuleSummary_Object = MibTableColumn
f3L2N2AAclRuleSummary = _F3L2N2AAclRuleSummary_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 22),
    _F3L2N2AAclRuleSummary_Type()
)
f3L2N2AAclRuleSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleSummary.setStatus("current")
_F3L2N2AAclRuleCosOverrideControl_Type = TruthValue
_F3L2N2AAclRuleCosOverrideControl_Object = MibTableColumn
f3L2N2AAclRuleCosOverrideControl = _F3L2N2AAclRuleCosOverrideControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 23),
    _F3L2N2AAclRuleCosOverrideControl_Type()
)
f3L2N2AAclRuleCosOverrideControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleCosOverrideControl.setStatus("current")
_F3L2N2AAclRuleSrcMacAddressControl_Type = TruthValue
_F3L2N2AAclRuleSrcMacAddressControl_Object = MibTableColumn
f3L2N2AAclRuleSrcMacAddressControl = _F3L2N2AAclRuleSrcMacAddressControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 24),
    _F3L2N2AAclRuleSrcMacAddressControl_Type()
)
f3L2N2AAclRuleSrcMacAddressControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleSrcMacAddressControl.setStatus("current")
_F3L2N2AAclRuleDynamicSrcMacAddressControl_Type = TruthValue
_F3L2N2AAclRuleDynamicSrcMacAddressControl_Object = MibTableColumn
f3L2N2AAclRuleDynamicSrcMacAddressControl = _F3L2N2AAclRuleDynamicSrcMacAddressControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 25),
    _F3L2N2AAclRuleDynamicSrcMacAddressControl_Type()
)
f3L2N2AAclRuleDynamicSrcMacAddressControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleDynamicSrcMacAddressControl.setStatus("current")
_F3L2N2AAclRuleSrcMacAddress_Type = MacAddress
_F3L2N2AAclRuleSrcMacAddress_Object = MibTableColumn
f3L2N2AAclRuleSrcMacAddress = _F3L2N2AAclRuleSrcMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 26),
    _F3L2N2AAclRuleSrcMacAddress_Type()
)
f3L2N2AAclRuleSrcMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleSrcMacAddress.setStatus("current")
_F3L2N2AAclRuleSrcMacAddressMask_Type = MacAddress
_F3L2N2AAclRuleSrcMacAddressMask_Object = MibTableColumn
f3L2N2AAclRuleSrcMacAddressMask = _F3L2N2AAclRuleSrcMacAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 27),
    _F3L2N2AAclRuleSrcMacAddressMask_Type()
)
f3L2N2AAclRuleSrcMacAddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleSrcMacAddressMask.setStatus("current")
_F3L2N2AAclRuleDstMacAddressControl_Type = TruthValue
_F3L2N2AAclRuleDstMacAddressControl_Object = MibTableColumn
f3L2N2AAclRuleDstMacAddressControl = _F3L2N2AAclRuleDstMacAddressControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 28),
    _F3L2N2AAclRuleDstMacAddressControl_Type()
)
f3L2N2AAclRuleDstMacAddressControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleDstMacAddressControl.setStatus("current")
_F3L2N2AAclRuleDstMacAddress_Type = MacAddress
_F3L2N2AAclRuleDstMacAddress_Object = MibTableColumn
f3L2N2AAclRuleDstMacAddress = _F3L2N2AAclRuleDstMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 29),
    _F3L2N2AAclRuleDstMacAddress_Type()
)
f3L2N2AAclRuleDstMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleDstMacAddress.setStatus("current")
_F3L2N2AAclRuleDstMacAddressMask_Type = MacAddress
_F3L2N2AAclRuleDstMacAddressMask_Object = MibTableColumn
f3L2N2AAclRuleDstMacAddressMask = _F3L2N2AAclRuleDstMacAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 30),
    _F3L2N2AAclRuleDstMacAddressMask_Type()
)
f3L2N2AAclRuleDstMacAddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleDstMacAddressMask.setStatus("current")
_F3L2N2AAclRuleOuterVlanVIDControl_Type = TruthValue
_F3L2N2AAclRuleOuterVlanVIDControl_Object = MibTableColumn
f3L2N2AAclRuleOuterVlanVIDControl = _F3L2N2AAclRuleOuterVlanVIDControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 31),
    _F3L2N2AAclRuleOuterVlanVIDControl_Type()
)
f3L2N2AAclRuleOuterVlanVIDControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleOuterVlanVIDControl.setStatus("current")
_F3L2N2AAclRuleOuterVlanVIDLowLimit_Type = VlanId
_F3L2N2AAclRuleOuterVlanVIDLowLimit_Object = MibTableColumn
f3L2N2AAclRuleOuterVlanVIDLowLimit = _F3L2N2AAclRuleOuterVlanVIDLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 32),
    _F3L2N2AAclRuleOuterVlanVIDLowLimit_Type()
)
f3L2N2AAclRuleOuterVlanVIDLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleOuterVlanVIDLowLimit.setStatus("current")
_F3L2N2AAclRuleOuterVlanVIDHighLimit_Type = VlanId
_F3L2N2AAclRuleOuterVlanVIDHighLimit_Object = MibTableColumn
f3L2N2AAclRuleOuterVlanVIDHighLimit = _F3L2N2AAclRuleOuterVlanVIDHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 33),
    _F3L2N2AAclRuleOuterVlanVIDHighLimit_Type()
)
f3L2N2AAclRuleOuterVlanVIDHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleOuterVlanVIDHighLimit.setStatus("current")
_F3L2N2AAclRuleInnerVlanVIDControl_Type = TruthValue
_F3L2N2AAclRuleInnerVlanVIDControl_Object = MibTableColumn
f3L2N2AAclRuleInnerVlanVIDControl = _F3L2N2AAclRuleInnerVlanVIDControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 34),
    _F3L2N2AAclRuleInnerVlanVIDControl_Type()
)
f3L2N2AAclRuleInnerVlanVIDControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleInnerVlanVIDControl.setStatus("current")
_F3L2N2AAclRuleInnerVlanVIDLowLimit_Type = VlanId
_F3L2N2AAclRuleInnerVlanVIDLowLimit_Object = MibTableColumn
f3L2N2AAclRuleInnerVlanVIDLowLimit = _F3L2N2AAclRuleInnerVlanVIDLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 35),
    _F3L2N2AAclRuleInnerVlanVIDLowLimit_Type()
)
f3L2N2AAclRuleInnerVlanVIDLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleInnerVlanVIDLowLimit.setStatus("current")
_F3L2N2AAclRuleInnerVlanVIDHighLimit_Type = VlanId
_F3L2N2AAclRuleInnerVlanVIDHighLimit_Object = MibTableColumn
f3L2N2AAclRuleInnerVlanVIDHighLimit = _F3L2N2AAclRuleInnerVlanVIDHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 36),
    _F3L2N2AAclRuleInnerVlanVIDHighLimit_Type()
)
f3L2N2AAclRuleInnerVlanVIDHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleInnerVlanVIDHighLimit.setStatus("current")
_F3L2N2AAclRuleOuterVlanPcpControl_Type = TruthValue
_F3L2N2AAclRuleOuterVlanPcpControl_Object = MibTableColumn
f3L2N2AAclRuleOuterVlanPcpControl = _F3L2N2AAclRuleOuterVlanPcpControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 37),
    _F3L2N2AAclRuleOuterVlanPcpControl_Type()
)
f3L2N2AAclRuleOuterVlanPcpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleOuterVlanPcpControl.setStatus("current")
_F3L2N2AAclRuleOuterVlanPcpLowLimit_Type = VlanPriority
_F3L2N2AAclRuleOuterVlanPcpLowLimit_Object = MibTableColumn
f3L2N2AAclRuleOuterVlanPcpLowLimit = _F3L2N2AAclRuleOuterVlanPcpLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 38),
    _F3L2N2AAclRuleOuterVlanPcpLowLimit_Type()
)
f3L2N2AAclRuleOuterVlanPcpLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleOuterVlanPcpLowLimit.setStatus("current")
_F3L2N2AAclRuleOuterVlanPcpHighLimit_Type = VlanPriority
_F3L2N2AAclRuleOuterVlanPcpHighLimit_Object = MibTableColumn
f3L2N2AAclRuleOuterVlanPcpHighLimit = _F3L2N2AAclRuleOuterVlanPcpHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 39),
    _F3L2N2AAclRuleOuterVlanPcpHighLimit_Type()
)
f3L2N2AAclRuleOuterVlanPcpHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleOuterVlanPcpHighLimit.setStatus("current")
_F3L2N2AAclRuleInnerVlanPcpControl_Type = TruthValue
_F3L2N2AAclRuleInnerVlanPcpControl_Object = MibTableColumn
f3L2N2AAclRuleInnerVlanPcpControl = _F3L2N2AAclRuleInnerVlanPcpControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 40),
    _F3L2N2AAclRuleInnerVlanPcpControl_Type()
)
f3L2N2AAclRuleInnerVlanPcpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleInnerVlanPcpControl.setStatus("current")
_F3L2N2AAclRuleInnerVlanPcpLowLimit_Type = VlanPriority
_F3L2N2AAclRuleInnerVlanPcpLowLimit_Object = MibTableColumn
f3L2N2AAclRuleInnerVlanPcpLowLimit = _F3L2N2AAclRuleInnerVlanPcpLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 41),
    _F3L2N2AAclRuleInnerVlanPcpLowLimit_Type()
)
f3L2N2AAclRuleInnerVlanPcpLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleInnerVlanPcpLowLimit.setStatus("current")
_F3L2N2AAclRuleInnerVlanPcpHighLimit_Type = VlanPriority
_F3L2N2AAclRuleInnerVlanPcpHighLimit_Object = MibTableColumn
f3L2N2AAclRuleInnerVlanPcpHighLimit = _F3L2N2AAclRuleInnerVlanPcpHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 42),
    _F3L2N2AAclRuleInnerVlanPcpHighLimit_Type()
)
f3L2N2AAclRuleInnerVlanPcpHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleInnerVlanPcpHighLimit.setStatus("current")
_F3L2N2AAclRuleOuterVlanDeiControl_Type = TruthValue
_F3L2N2AAclRuleOuterVlanDeiControl_Object = MibTableColumn
f3L2N2AAclRuleOuterVlanDeiControl = _F3L2N2AAclRuleOuterVlanDeiControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 43),
    _F3L2N2AAclRuleOuterVlanDeiControl_Type()
)
f3L2N2AAclRuleOuterVlanDeiControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleOuterVlanDeiControl.setStatus("current")


class _F3L2N2AAclRuleOuterVlanDei_Type(Unsigned32):
    """Custom type f3L2N2AAclRuleOuterVlanDei based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_F3L2N2AAclRuleOuterVlanDei_Type.__name__ = "Unsigned32"
_F3L2N2AAclRuleOuterVlanDei_Object = MibTableColumn
f3L2N2AAclRuleOuterVlanDei = _F3L2N2AAclRuleOuterVlanDei_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 44),
    _F3L2N2AAclRuleOuterVlanDei_Type()
)
f3L2N2AAclRuleOuterVlanDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleOuterVlanDei.setStatus("current")
_F3L2N2AAclRuleEtherTypeControl_Type = TruthValue
_F3L2N2AAclRuleEtherTypeControl_Object = MibTableColumn
f3L2N2AAclRuleEtherTypeControl = _F3L2N2AAclRuleEtherTypeControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 45),
    _F3L2N2AAclRuleEtherTypeControl_Type()
)
f3L2N2AAclRuleEtherTypeControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleEtherTypeControl.setStatus("current")
_F3L2N2AAclRuleEtherType_Type = Integer32
_F3L2N2AAclRuleEtherType_Object = MibTableColumn
f3L2N2AAclRuleEtherType = _F3L2N2AAclRuleEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 46),
    _F3L2N2AAclRuleEtherType_Type()
)
f3L2N2AAclRuleEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleEtherType.setStatus("current")
_F3L2N2AAclRuleTcpFlagsControl_Type = TruthValue
_F3L2N2AAclRuleTcpFlagsControl_Object = MibTableColumn
f3L2N2AAclRuleTcpFlagsControl = _F3L2N2AAclRuleTcpFlagsControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 47),
    _F3L2N2AAclRuleTcpFlagsControl_Type()
)
f3L2N2AAclRuleTcpFlagsControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleTcpFlagsControl.setStatus("current")
_F3L2N2AAclRuleTcpFlags_Type = Integer32
_F3L2N2AAclRuleTcpFlags_Object = MibTableColumn
f3L2N2AAclRuleTcpFlags = _F3L2N2AAclRuleTcpFlags_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 48),
    _F3L2N2AAclRuleTcpFlags_Type()
)
f3L2N2AAclRuleTcpFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleTcpFlags.setStatus("current")
_F3L2N2AAclRuleSrcIpv4AddressHighLimit_Type = IpAddress
_F3L2N2AAclRuleSrcIpv4AddressHighLimit_Object = MibTableColumn
f3L2N2AAclRuleSrcIpv4AddressHighLimit = _F3L2N2AAclRuleSrcIpv4AddressHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 49),
    _F3L2N2AAclRuleSrcIpv4AddressHighLimit_Type()
)
f3L2N2AAclRuleSrcIpv4AddressHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleSrcIpv4AddressHighLimit.setStatus("current")
_F3L2N2AAclRuleDstIpv4AddressHighLimit_Type = IpAddress
_F3L2N2AAclRuleDstIpv4AddressHighLimit_Object = MibTableColumn
f3L2N2AAclRuleDstIpv4AddressHighLimit = _F3L2N2AAclRuleDstIpv4AddressHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 50),
    _F3L2N2AAclRuleDstIpv4AddressHighLimit_Type()
)
f3L2N2AAclRuleDstIpv4AddressHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleDstIpv4AddressHighLimit.setStatus("current")
_F3L2N2AAclRuleIpv4PriorityHighLimit_Type = Integer32
_F3L2N2AAclRuleIpv4PriorityHighLimit_Object = MibTableColumn
f3L2N2AAclRuleIpv4PriorityHighLimit = _F3L2N2AAclRuleIpv4PriorityHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 51),
    _F3L2N2AAclRuleIpv4PriorityHighLimit_Type()
)
f3L2N2AAclRuleIpv4PriorityHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleIpv4PriorityHighLimit.setStatus("current")
_F3L2N2AAclRuleStorageType_Type = StorageType
_F3L2N2AAclRuleStorageType_Object = MibTableColumn
f3L2N2AAclRuleStorageType = _F3L2N2AAclRuleStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 52),
    _F3L2N2AAclRuleStorageType_Type()
)
f3L2N2AAclRuleStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleStorageType.setStatus("current")
_F3L2N2AAclRuleRowStatus_Type = RowStatus
_F3L2N2AAclRuleRowStatus_Object = MibTableColumn
f3L2N2AAclRuleRowStatus = _F3L2N2AAclRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 53),
    _F3L2N2AAclRuleRowStatus_Type()
)
f3L2N2AAclRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleRowStatus.setStatus("current")
_F3L2N2AAclRuleAdminState_Type = AdminState
_F3L2N2AAclRuleAdminState_Object = MibTableColumn
f3L2N2AAclRuleAdminState = _F3L2N2AAclRuleAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 54),
    _F3L2N2AAclRuleAdminState_Type()
)
f3L2N2AAclRuleAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleAdminState.setStatus("current")
_F3L2N2AAclRuleActive_Type = TruthValue
_F3L2N2AAclRuleActive_Object = MibTableColumn
f3L2N2AAclRuleActive = _F3L2N2AAclRuleActive_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 55),
    _F3L2N2AAclRuleActive_Type()
)
f3L2N2AAclRuleActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleActive.setStatus("current")
_F3L2N2AAclRuleSrcIpV6AddressControl_Type = TruthValue
_F3L2N2AAclRuleSrcIpV6AddressControl_Object = MibTableColumn
f3L2N2AAclRuleSrcIpV6AddressControl = _F3L2N2AAclRuleSrcIpV6AddressControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 56),
    _F3L2N2AAclRuleSrcIpV6AddressControl_Type()
)
f3L2N2AAclRuleSrcIpV6AddressControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleSrcIpV6AddressControl.setStatus("current")
_F3L2N2AAclRuleSrcIpV6Address_Type = Ipv6Address
_F3L2N2AAclRuleSrcIpV6Address_Object = MibTableColumn
f3L2N2AAclRuleSrcIpV6Address = _F3L2N2AAclRuleSrcIpV6Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 57),
    _F3L2N2AAclRuleSrcIpV6Address_Type()
)
f3L2N2AAclRuleSrcIpV6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleSrcIpV6Address.setStatus("current")
_F3L2N2AAclRuleSrcIpV6AddressPrefixLen_Type = Integer32
_F3L2N2AAclRuleSrcIpV6AddressPrefixLen_Object = MibTableColumn
f3L2N2AAclRuleSrcIpV6AddressPrefixLen = _F3L2N2AAclRuleSrcIpV6AddressPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 58),
    _F3L2N2AAclRuleSrcIpV6AddressPrefixLen_Type()
)
f3L2N2AAclRuleSrcIpV6AddressPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleSrcIpV6AddressPrefixLen.setStatus("current")
_F3L2N2AAclRuleDstIpV6AddressControl_Type = TruthValue
_F3L2N2AAclRuleDstIpV6AddressControl_Object = MibTableColumn
f3L2N2AAclRuleDstIpV6AddressControl = _F3L2N2AAclRuleDstIpV6AddressControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 59),
    _F3L2N2AAclRuleDstIpV6AddressControl_Type()
)
f3L2N2AAclRuleDstIpV6AddressControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleDstIpV6AddressControl.setStatus("current")
_F3L2N2AAclRuleDstIpV6Address_Type = Ipv6Address
_F3L2N2AAclRuleDstIpV6Address_Object = MibTableColumn
f3L2N2AAclRuleDstIpV6Address = _F3L2N2AAclRuleDstIpV6Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 60),
    _F3L2N2AAclRuleDstIpV6Address_Type()
)
f3L2N2AAclRuleDstIpV6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleDstIpV6Address.setStatus("current")
_F3L2N2AAclRuleDstIpV6AddressPrefixLen_Type = Integer32
_F3L2N2AAclRuleDstIpV6AddressPrefixLen_Object = MibTableColumn
f3L2N2AAclRuleDstIpV6AddressPrefixLen = _F3L2N2AAclRuleDstIpV6AddressPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 61),
    _F3L2N2AAclRuleDstIpV6AddressPrefixLen_Type()
)
f3L2N2AAclRuleDstIpV6AddressPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleDstIpV6AddressPrefixLen.setStatus("current")
_F3L2N2AAclRuleIpV6FlowLabelControl_Type = TruthValue
_F3L2N2AAclRuleIpV6FlowLabelControl_Object = MibTableColumn
f3L2N2AAclRuleIpV6FlowLabelControl = _F3L2N2AAclRuleIpV6FlowLabelControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 62),
    _F3L2N2AAclRuleIpV6FlowLabelControl_Type()
)
f3L2N2AAclRuleIpV6FlowLabelControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleIpV6FlowLabelControl.setStatus("current")
_F3L2N2AAclRuleIpV6FlowLabel_Type = Integer32
_F3L2N2AAclRuleIpV6FlowLabel_Object = MibTableColumn
f3L2N2AAclRuleIpV6FlowLabel = _F3L2N2AAclRuleIpV6FlowLabel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 6, 1, 63),
    _F3L2N2AAclRuleIpV6FlowLabel_Type()
)
f3L2N2AAclRuleIpV6FlowLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleIpV6FlowLabel.setStatus("current")
_F3L3QosPolicerTable_Object = MibTable
f3L3QosPolicerTable = _F3L3QosPolicerTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 7)
)
if mibBuilder.loadTexts:
    f3L3QosPolicerTable.setStatus("current")
_F3L3QosPolicerEntry_Object = MibTableRow
f3L3QosPolicerEntry = _F3L3QosPolicerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 7, 1)
)
f3L3QosPolicerEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortTypeIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointIndex"),
    (0, "F3-L3-MIB", "f3L3QosPolicerIndex"),
)
if mibBuilder.loadTexts:
    f3L3QosPolicerEntry.setStatus("current")


class _F3L3QosPolicerIndex_Type(Integer32):
    """Custom type f3L3QosPolicerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_F3L3QosPolicerIndex_Type.__name__ = "Integer32"
_F3L3QosPolicerIndex_Object = MibTableColumn
f3L3QosPolicerIndex = _F3L3QosPolicerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 7, 1, 1),
    _F3L3QosPolicerIndex_Type()
)
f3L3QosPolicerIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3QosPolicerIndex.setStatus("current")
_F3L3QosPolicerAdminState_Type = AdminState
_F3L3QosPolicerAdminState_Object = MibTableColumn
f3L3QosPolicerAdminState = _F3L3QosPolicerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 7, 1, 2),
    _F3L3QosPolicerAdminState_Type()
)
f3L3QosPolicerAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3QosPolicerAdminState.setStatus("current")
_F3L3QosPolicerOperationalState_Type = OperationalState
_F3L3QosPolicerOperationalState_Object = MibTableColumn
f3L3QosPolicerOperationalState = _F3L3QosPolicerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 7, 1, 3),
    _F3L3QosPolicerOperationalState_Type()
)
f3L3QosPolicerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosPolicerOperationalState.setStatus("current")
_F3L3QosPolicerSecondaryState_Type = SecondaryState
_F3L3QosPolicerSecondaryState_Object = MibTableColumn
f3L3QosPolicerSecondaryState = _F3L3QosPolicerSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 7, 1, 4),
    _F3L3QosPolicerSecondaryState_Type()
)
f3L3QosPolicerSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosPolicerSecondaryState.setStatus("current")
_F3L3QosPolicerCIRLo_Type = Unsigned32
_F3L3QosPolicerCIRLo_Object = MibTableColumn
f3L3QosPolicerCIRLo = _F3L3QosPolicerCIRLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 7, 1, 5),
    _F3L3QosPolicerCIRLo_Type()
)
f3L3QosPolicerCIRLo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3QosPolicerCIRLo.setStatus("current")
_F3L3QosPolicerCIRHi_Type = Unsigned32
_F3L3QosPolicerCIRHi_Object = MibTableColumn
f3L3QosPolicerCIRHi = _F3L3QosPolicerCIRHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 7, 1, 6),
    _F3L3QosPolicerCIRHi_Type()
)
f3L3QosPolicerCIRHi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3QosPolicerCIRHi.setStatus("current")
_F3L3QosPolicerEIRLo_Type = Unsigned32
_F3L3QosPolicerEIRLo_Object = MibTableColumn
f3L3QosPolicerEIRLo = _F3L3QosPolicerEIRLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 7, 1, 7),
    _F3L3QosPolicerEIRLo_Type()
)
f3L3QosPolicerEIRLo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3QosPolicerEIRLo.setStatus("current")
_F3L3QosPolicerEIRHi_Type = Unsigned32
_F3L3QosPolicerEIRHi_Object = MibTableColumn
f3L3QosPolicerEIRHi = _F3L3QosPolicerEIRHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 7, 1, 8),
    _F3L3QosPolicerEIRHi_Type()
)
f3L3QosPolicerEIRHi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3QosPolicerEIRHi.setStatus("current")
_F3L3QosPolicerCBS_Type = Integer32
_F3L3QosPolicerCBS_Object = MibTableColumn
f3L3QosPolicerCBS = _F3L3QosPolicerCBS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 7, 1, 9),
    _F3L3QosPolicerCBS_Type()
)
f3L3QosPolicerCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3QosPolicerCBS.setStatus("current")
_F3L3QosPolicerEBS_Type = Integer32
_F3L3QosPolicerEBS_Object = MibTableColumn
f3L3QosPolicerEBS = _F3L3QosPolicerEBS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 7, 1, 10),
    _F3L3QosPolicerEBS_Type()
)
f3L3QosPolicerEBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3QosPolicerEBS.setStatus("current")
_F3L3QosPolicerAlgorithm_Type = PolicerAlgorithmType
_F3L3QosPolicerAlgorithm_Object = MibTableColumn
f3L3QosPolicerAlgorithm = _F3L3QosPolicerAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 7, 1, 11),
    _F3L3QosPolicerAlgorithm_Type()
)
f3L3QosPolicerAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosPolicerAlgorithm.setStatus("current")
_F3L3QosPolicerColorMode_Type = PolicerColorMode
_F3L3QosPolicerColorMode_Object = MibTableColumn
f3L3QosPolicerColorMode = _F3L3QosPolicerColorMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 7, 1, 12),
    _F3L3QosPolicerColorMode_Type()
)
f3L3QosPolicerColorMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3QosPolicerColorMode.setStatus("current")
_F3L3QosPolicerCouplingFlag_Type = TruthValue
_F3L3QosPolicerCouplingFlag_Object = MibTableColumn
f3L3QosPolicerCouplingFlag = _F3L3QosPolicerCouplingFlag_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 7, 1, 13),
    _F3L3QosPolicerCouplingFlag_Type()
)
f3L3QosPolicerCouplingFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3QosPolicerCouplingFlag.setStatus("current")
_F3L3QosPolicerStorageType_Type = StorageType
_F3L3QosPolicerStorageType_Object = MibTableColumn
f3L3QosPolicerStorageType = _F3L3QosPolicerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 7, 1, 14),
    _F3L3QosPolicerStorageType_Type()
)
f3L3QosPolicerStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3QosPolicerStorageType.setStatus("current")
_F3L3QosPolicerRowStatus_Type = RowStatus
_F3L3QosPolicerRowStatus_Object = MibTableColumn
f3L3QosPolicerRowStatus = _F3L3QosPolicerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 7, 1, 15),
    _F3L3QosPolicerRowStatus_Type()
)
f3L3QosPolicerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3QosPolicerRowStatus.setStatus("current")
_F3L3QosPolicerCIRMaxHi_Type = Unsigned32
_F3L3QosPolicerCIRMaxHi_Object = MibTableColumn
f3L3QosPolicerCIRMaxHi = _F3L3QosPolicerCIRMaxHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 7, 1, 16),
    _F3L3QosPolicerCIRMaxHi_Type()
)
f3L3QosPolicerCIRMaxHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3QosPolicerCIRMaxHi.setStatus("current")
_F3L3QosPolicerCIRMaxLo_Type = Unsigned32
_F3L3QosPolicerCIRMaxLo_Object = MibTableColumn
f3L3QosPolicerCIRMaxLo = _F3L3QosPolicerCIRMaxLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 7, 1, 17),
    _F3L3QosPolicerCIRMaxLo_Type()
)
f3L3QosPolicerCIRMaxLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3QosPolicerCIRMaxLo.setStatus("current")
_F3L3QosPolicerEIRMaxHi_Type = Unsigned32
_F3L3QosPolicerEIRMaxHi_Object = MibTableColumn
f3L3QosPolicerEIRMaxHi = _F3L3QosPolicerEIRMaxHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 7, 1, 18),
    _F3L3QosPolicerEIRMaxHi_Type()
)
f3L3QosPolicerEIRMaxHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3QosPolicerEIRMaxHi.setStatus("current")
_F3L3QosPolicerEIRMaxLo_Type = Unsigned32
_F3L3QosPolicerEIRMaxLo_Object = MibTableColumn
f3L3QosPolicerEIRMaxLo = _F3L3QosPolicerEIRMaxLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 7, 1, 19),
    _F3L3QosPolicerEIRMaxLo_Type()
)
f3L3QosPolicerEIRMaxLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3QosPolicerEIRMaxLo.setStatus("current")
_F3L3QosPolicerEnvelopeObject_Type = VariablePointer
_F3L3QosPolicerEnvelopeObject_Object = MibTableColumn
f3L3QosPolicerEnvelopeObject = _F3L3QosPolicerEnvelopeObject_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 7, 1, 20),
    _F3L3QosPolicerEnvelopeObject_Type()
)
f3L3QosPolicerEnvelopeObject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3QosPolicerEnvelopeObject.setStatus("current")
_F3L3QosPolicerRank_Type = Integer32
_F3L3QosPolicerRank_Object = MibTableColumn
f3L3QosPolicerRank = _F3L3QosPolicerRank_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 7, 1, 21),
    _F3L3QosPolicerRank_Type()
)
f3L3QosPolicerRank.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3QosPolicerRank.setStatus("current")
_F3L3QosPolicerPolicingEnabled_Type = TruthValue
_F3L3QosPolicerPolicingEnabled_Object = MibTableColumn
f3L3QosPolicerPolicingEnabled = _F3L3QosPolicerPolicingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 7, 1, 22),
    _F3L3QosPolicerPolicingEnabled_Type()
)
f3L3QosPolicerPolicingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3QosPolicerPolicingEnabled.setStatus("current")
_F3L3QosShaperTable_Object = MibTable
f3L3QosShaperTable = _F3L3QosShaperTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 8)
)
if mibBuilder.loadTexts:
    f3L3QosShaperTable.setStatus("current")
_F3L3QosShaperEntry_Object = MibTableRow
f3L3QosShaperEntry = _F3L3QosShaperEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 8, 1)
)
f3L3QosShaperEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortTypeIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointIndex"),
    (0, "F3-L3-MIB", "f3L3QosShaperIndex"),
)
if mibBuilder.loadTexts:
    f3L3QosShaperEntry.setStatus("current")


class _F3L3QosShaperIndex_Type(Integer32):
    """Custom type f3L3QosShaperIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_F3L3QosShaperIndex_Type.__name__ = "Integer32"
_F3L3QosShaperIndex_Object = MibTableColumn
f3L3QosShaperIndex = _F3L3QosShaperIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 8, 1, 1),
    _F3L3QosShaperIndex_Type()
)
f3L3QosShaperIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3QosShaperIndex.setStatus("current")
_F3L3QosShaperAdminState_Type = AdminState
_F3L3QosShaperAdminState_Object = MibTableColumn
f3L3QosShaperAdminState = _F3L3QosShaperAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 8, 1, 2),
    _F3L3QosShaperAdminState_Type()
)
f3L3QosShaperAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3QosShaperAdminState.setStatus("current")
_F3L3QosShaperOperationalState_Type = OperationalState
_F3L3QosShaperOperationalState_Object = MibTableColumn
f3L3QosShaperOperationalState = _F3L3QosShaperOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 8, 1, 3),
    _F3L3QosShaperOperationalState_Type()
)
f3L3QosShaperOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperOperationalState.setStatus("current")
_F3L3QosShaperSecondaryState_Type = SecondaryState
_F3L3QosShaperSecondaryState_Object = MibTableColumn
f3L3QosShaperSecondaryState = _F3L3QosShaperSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 8, 1, 4),
    _F3L3QosShaperSecondaryState_Type()
)
f3L3QosShaperSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperSecondaryState.setStatus("current")
_F3L3QosShaperCIRLo_Type = Unsigned32
_F3L3QosShaperCIRLo_Object = MibTableColumn
f3L3QosShaperCIRLo = _F3L3QosShaperCIRLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 8, 1, 5),
    _F3L3QosShaperCIRLo_Type()
)
f3L3QosShaperCIRLo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3QosShaperCIRLo.setStatus("current")
_F3L3QosShaperCIRHi_Type = Unsigned32
_F3L3QosShaperCIRHi_Object = MibTableColumn
f3L3QosShaperCIRHi = _F3L3QosShaperCIRHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 8, 1, 6),
    _F3L3QosShaperCIRHi_Type()
)
f3L3QosShaperCIRHi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3QosShaperCIRHi.setStatus("current")
_F3L3QosShaperEIRLo_Type = Unsigned32
_F3L3QosShaperEIRLo_Object = MibTableColumn
f3L3QosShaperEIRLo = _F3L3QosShaperEIRLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 8, 1, 7),
    _F3L3QosShaperEIRLo_Type()
)
f3L3QosShaperEIRLo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3QosShaperEIRLo.setStatus("current")
_F3L3QosShaperEIRHi_Type = Unsigned32
_F3L3QosShaperEIRHi_Object = MibTableColumn
f3L3QosShaperEIRHi = _F3L3QosShaperEIRHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 8, 1, 8),
    _F3L3QosShaperEIRHi_Type()
)
f3L3QosShaperEIRHi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3QosShaperEIRHi.setStatus("current")
_F3L3QosShaperBufferSize_Type = Unsigned32
_F3L3QosShaperBufferSize_Object = MibTableColumn
f3L3QosShaperBufferSize = _F3L3QosShaperBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 8, 1, 9),
    _F3L3QosShaperBufferSize_Type()
)
f3L3QosShaperBufferSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3QosShaperBufferSize.setStatus("current")


class _F3L3QosShaperCOS_Type(Integer32):
    """Custom type f3L3QosShaperCOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_F3L3QosShaperCOS_Type.__name__ = "Integer32"
_F3L3QosShaperCOS_Object = MibTableColumn
f3L3QosShaperCOS = _F3L3QosShaperCOS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 8, 1, 10),
    _F3L3QosShaperCOS_Type()
)
f3L3QosShaperCOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperCOS.setStatus("current")
_F3L3QosShaperWredGreenMinQueueThreshold_Type = Unsigned32
_F3L3QosShaperWredGreenMinQueueThreshold_Object = MibTableColumn
f3L3QosShaperWredGreenMinQueueThreshold = _F3L3QosShaperWredGreenMinQueueThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 8, 1, 11),
    _F3L3QosShaperWredGreenMinQueueThreshold_Type()
)
f3L3QosShaperWredGreenMinQueueThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3QosShaperWredGreenMinQueueThreshold.setStatus("current")
_F3L3QosShaperWredGreenMaxQueueThreshold_Type = Unsigned32
_F3L3QosShaperWredGreenMaxQueueThreshold_Object = MibTableColumn
f3L3QosShaperWredGreenMaxQueueThreshold = _F3L3QosShaperWredGreenMaxQueueThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 8, 1, 12),
    _F3L3QosShaperWredGreenMaxQueueThreshold_Type()
)
f3L3QosShaperWredGreenMaxQueueThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3QosShaperWredGreenMaxQueueThreshold.setStatus("current")
_F3L3QosShaperWredGreenDropProbability_Type = Unsigned32
_F3L3QosShaperWredGreenDropProbability_Object = MibTableColumn
f3L3QosShaperWredGreenDropProbability = _F3L3QosShaperWredGreenDropProbability_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 8, 1, 13),
    _F3L3QosShaperWredGreenDropProbability_Type()
)
f3L3QosShaperWredGreenDropProbability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3QosShaperWredGreenDropProbability.setStatus("current")
_F3L3QosShaperWredYellowMinQueueThreshold_Type = Unsigned32
_F3L3QosShaperWredYellowMinQueueThreshold_Object = MibTableColumn
f3L3QosShaperWredYellowMinQueueThreshold = _F3L3QosShaperWredYellowMinQueueThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 8, 1, 14),
    _F3L3QosShaperWredYellowMinQueueThreshold_Type()
)
f3L3QosShaperWredYellowMinQueueThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3QosShaperWredYellowMinQueueThreshold.setStatus("current")
_F3L3QosShaperWredYellowMaxQueueThreshold_Type = Unsigned32
_F3L3QosShaperWredYellowMaxQueueThreshold_Object = MibTableColumn
f3L3QosShaperWredYellowMaxQueueThreshold = _F3L3QosShaperWredYellowMaxQueueThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 8, 1, 15),
    _F3L3QosShaperWredYellowMaxQueueThreshold_Type()
)
f3L3QosShaperWredYellowMaxQueueThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3QosShaperWredYellowMaxQueueThreshold.setStatus("current")
_F3L3QosShaperWredYellowDropProbability_Type = Unsigned32
_F3L3QosShaperWredYellowDropProbability_Object = MibTableColumn
f3L3QosShaperWredYellowDropProbability = _F3L3QosShaperWredYellowDropProbability_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 8, 1, 16),
    _F3L3QosShaperWredYellowDropProbability_Type()
)
f3L3QosShaperWredYellowDropProbability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3QosShaperWredYellowDropProbability.setStatus("current")
_F3L3QosShaperStorageType_Type = StorageType
_F3L3QosShaperStorageType_Object = MibTableColumn
f3L3QosShaperStorageType = _F3L3QosShaperStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 8, 1, 17),
    _F3L3QosShaperStorageType_Type()
)
f3L3QosShaperStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3QosShaperStorageType.setStatus("current")
_F3L3QosShaperRowStatus_Type = RowStatus
_F3L3QosShaperRowStatus_Object = MibTableColumn
f3L3QosShaperRowStatus = _F3L3QosShaperRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 8, 1, 18),
    _F3L3QosShaperRowStatus_Type()
)
f3L3QosShaperRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3QosShaperRowStatus.setStatus("current")
_F3L3QosShaperWfqWeight_Type = Integer32
_F3L3QosShaperWfqWeight_Object = MibTableColumn
f3L3QosShaperWfqWeight = _F3L3QosShaperWfqWeight_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 8, 1, 19),
    _F3L3QosShaperWfqWeight_Type()
)
f3L3QosShaperWfqWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3QosShaperWfqWeight.setStatus("current")
_F3L3TrafficIPInterfaceTable_Object = MibTable
f3L3TrafficIPInterfaceTable = _F3L3TrafficIPInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9)
)
if mibBuilder.loadTexts:
    f3L3TrafficIPInterfaceTable.setStatus("current")
_F3L3TrafficIPInterfaceEntry_Object = MibTableRow
f3L3TrafficIPInterfaceEntry = _F3L3TrafficIPInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1)
)
f3L3TrafficIPInterfaceEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficIPIfIndex"),
)
if mibBuilder.loadTexts:
    f3L3TrafficIPInterfaceEntry.setStatus("current")
_F3L3TrafficIPIfIndex_Type = Integer32
_F3L3TrafficIPIfIndex_Object = MibTableColumn
f3L3TrafficIPIfIndex = _F3L3TrafficIPIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 1),
    _F3L3TrafficIPIfIndex_Type()
)
f3L3TrafficIPIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfIndex.setStatus("current")


class _F3L3TrafficIPIfName_Type(DisplayString):
    """Custom type f3L3TrafficIPIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_F3L3TrafficIPIfName_Type.__name__ = "DisplayString"
_F3L3TrafficIPIfName_Object = MibTableColumn
f3L3TrafficIPIfName = _F3L3TrafficIPIfName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 2),
    _F3L3TrafficIPIfName_Type()
)
f3L3TrafficIPIfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfName.setStatus("current")
_F3L3TrafficIPIfAdminState_Type = AdminState
_F3L3TrafficIPIfAdminState_Object = MibTableColumn
f3L3TrafficIPIfAdminState = _F3L3TrafficIPIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 3),
    _F3L3TrafficIPIfAdminState_Type()
)
f3L3TrafficIPIfAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfAdminState.setStatus("current")
_F3L3TrafficIPIfSecondaryState_Type = SecondaryState
_F3L3TrafficIPIfSecondaryState_Object = MibTableColumn
f3L3TrafficIPIfSecondaryState = _F3L3TrafficIPIfSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 4),
    _F3L3TrafficIPIfSecondaryState_Type()
)
f3L3TrafficIPIfSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfSecondaryState.setStatus("current")
_F3L3TrafficIPIfOperationalState_Type = OperationalState
_F3L3TrafficIPIfOperationalState_Object = MibTableColumn
f3L3TrafficIPIfOperationalState = _F3L3TrafficIPIfOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 5),
    _F3L3TrafficIPIfOperationalState_Type()
)
f3L3TrafficIPIfOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfOperationalState.setStatus("current")
_F3L3TrafficIPIfProxyArpEnabled_Type = TruthValue
_F3L3TrafficIPIfProxyArpEnabled_Object = MibTableColumn
f3L3TrafficIPIfProxyArpEnabled = _F3L3TrafficIPIfProxyArpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 6),
    _F3L3TrafficIPIfProxyArpEnabled_Type()
)
f3L3TrafficIPIfProxyArpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfProxyArpEnabled.setStatus("current")
_F3L3TrafficIPIfIpAddressSourceType_Type = IfIpAddressSourceType
_F3L3TrafficIPIfIpAddressSourceType_Object = MibTableColumn
f3L3TrafficIPIfIpAddressSourceType = _F3L3TrafficIPIfIpAddressSourceType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 7),
    _F3L3TrafficIPIfIpAddressSourceType_Type()
)
f3L3TrafficIPIfIpAddressSourceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfIpAddressSourceType.setStatus("current")
_F3L3TrafficIPIfMgmtUseEnable_Type = TruthValue
_F3L3TrafficIPIfMgmtUseEnable_Object = MibTableColumn
f3L3TrafficIPIfMgmtUseEnable = _F3L3TrafficIPIfMgmtUseEnable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 8),
    _F3L3TrafficIPIfMgmtUseEnable_Type()
)
f3L3TrafficIPIfMgmtUseEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfMgmtUseEnable.setStatus("current")
_F3L3TrafficIPIfIpAddress_Type = IpAddress
_F3L3TrafficIPIfIpAddress_Object = MibTableColumn
f3L3TrafficIPIfIpAddress = _F3L3TrafficIPIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 9),
    _F3L3TrafficIPIfIpAddress_Type()
)
f3L3TrafficIPIfIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfIpAddress.setStatus("current")
_F3L3TrafficIPIfMask_Type = IpAddress
_F3L3TrafficIPIfMask_Object = MibTableColumn
f3L3TrafficIPIfMask = _F3L3TrafficIPIfMask_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 10),
    _F3L3TrafficIPIfMask_Type()
)
f3L3TrafficIPIfMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfMask.setStatus("current")
_F3L3TrafficIPIfDhcpRelayInterfaceSide_Type = DhcpRelayInterfaceSide
_F3L3TrafficIPIfDhcpRelayInterfaceSide_Object = MibTableColumn
f3L3TrafficIPIfDhcpRelayInterfaceSide = _F3L3TrafficIPIfDhcpRelayInterfaceSide_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 11),
    _F3L3TrafficIPIfDhcpRelayInterfaceSide_Type()
)
f3L3TrafficIPIfDhcpRelayInterfaceSide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfDhcpRelayInterfaceSide.setStatus("current")


class _F3L3TrafficIPIfDhcpRelayVendorClassiDOpt60_Type(DisplayString):
    """Custom type f3L3TrafficIPIfDhcpRelayVendorClassiDOpt60 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_F3L3TrafficIPIfDhcpRelayVendorClassiDOpt60_Type.__name__ = "DisplayString"
_F3L3TrafficIPIfDhcpRelayVendorClassiDOpt60_Object = MibTableColumn
f3L3TrafficIPIfDhcpRelayVendorClassiDOpt60 = _F3L3TrafficIPIfDhcpRelayVendorClassiDOpt60_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 12),
    _F3L3TrafficIPIfDhcpRelayVendorClassiDOpt60_Type()
)
f3L3TrafficIPIfDhcpRelayVendorClassiDOpt60.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfDhcpRelayVendorClassiDOpt60.setStatus("current")
_F3L3TrafficIPIfDhcpRelayVendorClassiDOpt60Control_Type = TruthValue
_F3L3TrafficIPIfDhcpRelayVendorClassiDOpt60Control_Object = MibTableColumn
f3L3TrafficIPIfDhcpRelayVendorClassiDOpt60Control = _F3L3TrafficIPIfDhcpRelayVendorClassiDOpt60Control_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 13),
    _F3L3TrafficIPIfDhcpRelayVendorClassiDOpt60Control_Type()
)
f3L3TrafficIPIfDhcpRelayVendorClassiDOpt60Control.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfDhcpRelayVendorClassiDOpt60Control.setStatus("current")


class _F3L3TrafficIPIfDhcpRelayUserClassOpt77_Type(DisplayString):
    """Custom type f3L3TrafficIPIfDhcpRelayUserClassOpt77 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_F3L3TrafficIPIfDhcpRelayUserClassOpt77_Type.__name__ = "DisplayString"
_F3L3TrafficIPIfDhcpRelayUserClassOpt77_Object = MibTableColumn
f3L3TrafficIPIfDhcpRelayUserClassOpt77 = _F3L3TrafficIPIfDhcpRelayUserClassOpt77_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 14),
    _F3L3TrafficIPIfDhcpRelayUserClassOpt77_Type()
)
f3L3TrafficIPIfDhcpRelayUserClassOpt77.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfDhcpRelayUserClassOpt77.setStatus("current")
_F3L3TrafficIPIfDhcpRelayUserClassOpt77Control_Type = TruthValue
_F3L3TrafficIPIfDhcpRelayUserClassOpt77Control_Object = MibTableColumn
f3L3TrafficIPIfDhcpRelayUserClassOpt77Control = _F3L3TrafficIPIfDhcpRelayUserClassOpt77Control_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 15),
    _F3L3TrafficIPIfDhcpRelayUserClassOpt77Control_Type()
)
f3L3TrafficIPIfDhcpRelayUserClassOpt77Control.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfDhcpRelayUserClassOpt77Control.setStatus("current")


class _F3L3TrafficIPIfDhcpRelayInfoOpt82Sub1_Type(DisplayString):
    """Custom type f3L3TrafficIPIfDhcpRelayInfoOpt82Sub1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_F3L3TrafficIPIfDhcpRelayInfoOpt82Sub1_Type.__name__ = "DisplayString"
_F3L3TrafficIPIfDhcpRelayInfoOpt82Sub1_Object = MibTableColumn
f3L3TrafficIPIfDhcpRelayInfoOpt82Sub1 = _F3L3TrafficIPIfDhcpRelayInfoOpt82Sub1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 16),
    _F3L3TrafficIPIfDhcpRelayInfoOpt82Sub1_Type()
)
f3L3TrafficIPIfDhcpRelayInfoOpt82Sub1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfDhcpRelayInfoOpt82Sub1.setStatus("current")
_F3L3TrafficIPIfDhcpRelayInfoOpt82Sub1Enabled_Type = TruthValue
_F3L3TrafficIPIfDhcpRelayInfoOpt82Sub1Enabled_Object = MibTableColumn
f3L3TrafficIPIfDhcpRelayInfoOpt82Sub1Enabled = _F3L3TrafficIPIfDhcpRelayInfoOpt82Sub1Enabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 17),
    _F3L3TrafficIPIfDhcpRelayInfoOpt82Sub1Enabled_Type()
)
f3L3TrafficIPIfDhcpRelayInfoOpt82Sub1Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfDhcpRelayInfoOpt82Sub1Enabled.setStatus("current")


class _F3L3TrafficIPIfDhcpRelayInfoOpt82Sub2_Type(DisplayString):
    """Custom type f3L3TrafficIPIfDhcpRelayInfoOpt82Sub2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_F3L3TrafficIPIfDhcpRelayInfoOpt82Sub2_Type.__name__ = "DisplayString"
_F3L3TrafficIPIfDhcpRelayInfoOpt82Sub2_Object = MibTableColumn
f3L3TrafficIPIfDhcpRelayInfoOpt82Sub2 = _F3L3TrafficIPIfDhcpRelayInfoOpt82Sub2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 18),
    _F3L3TrafficIPIfDhcpRelayInfoOpt82Sub2_Type()
)
f3L3TrafficIPIfDhcpRelayInfoOpt82Sub2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfDhcpRelayInfoOpt82Sub2.setStatus("current")
_F3L3TrafficIPIfDhcpRelayInfoOpt82Sub2Enabled_Type = TruthValue
_F3L3TrafficIPIfDhcpRelayInfoOpt82Sub2Enabled_Object = MibTableColumn
f3L3TrafficIPIfDhcpRelayInfoOpt82Sub2Enabled = _F3L3TrafficIPIfDhcpRelayInfoOpt82Sub2Enabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 19),
    _F3L3TrafficIPIfDhcpRelayInfoOpt82Sub2Enabled_Type()
)
f3L3TrafficIPIfDhcpRelayInfoOpt82Sub2Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfDhcpRelayInfoOpt82Sub2Enabled.setStatus("current")
_F3L3TrafficIPIfDhcpEnabled_Type = TruthValue
_F3L3TrafficIPIfDhcpEnabled_Object = MibTableColumn
f3L3TrafficIPIfDhcpEnabled = _F3L3TrafficIPIfDhcpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 20),
    _F3L3TrafficIPIfDhcpEnabled_Type()
)
f3L3TrafficIPIfDhcpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfDhcpEnabled.setStatus("current")
_F3L3TrafficIPIfDhcpRole_Type = CmDhcpRole
_F3L3TrafficIPIfDhcpRole_Object = MibTableColumn
f3L3TrafficIPIfDhcpRole = _F3L3TrafficIPIfDhcpRole_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 21),
    _F3L3TrafficIPIfDhcpRole_Type()
)
f3L3TrafficIPIfDhcpRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfDhcpRole.setStatus("current")
_F3L3TrafficIPIfDhcpClientIdEnabled_Type = TruthValue
_F3L3TrafficIPIfDhcpClientIdEnabled_Object = MibTableColumn
f3L3TrafficIPIfDhcpClientIdEnabled = _F3L3TrafficIPIfDhcpClientIdEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 22),
    _F3L3TrafficIPIfDhcpClientIdEnabled_Type()
)
f3L3TrafficIPIfDhcpClientIdEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfDhcpClientIdEnabled.setStatus("current")
_F3L3TrafficIPIfDhcpClientId_Type = DisplayString
_F3L3TrafficIPIfDhcpClientId_Object = MibTableColumn
f3L3TrafficIPIfDhcpClientId = _F3L3TrafficIPIfDhcpClientId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 23),
    _F3L3TrafficIPIfDhcpClientId_Type()
)
f3L3TrafficIPIfDhcpClientId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfDhcpClientId.setStatus("current")
_F3L3TrafficIPIfDhcpClassIdEnabled_Type = TruthValue
_F3L3TrafficIPIfDhcpClassIdEnabled_Object = MibTableColumn
f3L3TrafficIPIfDhcpClassIdEnabled = _F3L3TrafficIPIfDhcpClassIdEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 24),
    _F3L3TrafficIPIfDhcpClassIdEnabled_Type()
)
f3L3TrafficIPIfDhcpClassIdEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfDhcpClassIdEnabled.setStatus("current")
_F3L3TrafficIPIfDhcpHostNameEnabled_Type = TruthValue
_F3L3TrafficIPIfDhcpHostNameEnabled_Object = MibTableColumn
f3L3TrafficIPIfDhcpHostNameEnabled = _F3L3TrafficIPIfDhcpHostNameEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 25),
    _F3L3TrafficIPIfDhcpHostNameEnabled_Type()
)
f3L3TrafficIPIfDhcpHostNameEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfDhcpHostNameEnabled.setStatus("current")
_F3L3TrafficIPIfDhcpHostName_Type = DisplayString
_F3L3TrafficIPIfDhcpHostName_Object = MibTableColumn
f3L3TrafficIPIfDhcpHostName = _F3L3TrafficIPIfDhcpHostName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 26),
    _F3L3TrafficIPIfDhcpHostName_Type()
)
f3L3TrafficIPIfDhcpHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfDhcpHostName.setStatus("current")
_F3L3TrafficIPIfDhcpClientIdType_Type = DHCPCIDType
_F3L3TrafficIPIfDhcpClientIdType_Object = MibTableColumn
f3L3TrafficIPIfDhcpClientIdType = _F3L3TrafficIPIfDhcpClientIdType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 27),
    _F3L3TrafficIPIfDhcpClientIdType_Type()
)
f3L3TrafficIPIfDhcpClientIdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfDhcpClientIdType.setStatus("current")
_F3L3TrafficIPIfDhcpHostNameType_Type = DHCPHostNameType
_F3L3TrafficIPIfDhcpHostNameType_Object = MibTableColumn
f3L3TrafficIPIfDhcpHostNameType = _F3L3TrafficIPIfDhcpHostNameType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 28),
    _F3L3TrafficIPIfDhcpHostNameType_Type()
)
f3L3TrafficIPIfDhcpHostNameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfDhcpHostNameType.setStatus("current")
_F3L3TrafficIPIfStorageType_Type = StorageType
_F3L3TrafficIPIfStorageType_Object = MibTableColumn
f3L3TrafficIPIfStorageType = _F3L3TrafficIPIfStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 29),
    _F3L3TrafficIPIfStorageType_Type()
)
f3L3TrafficIPIfStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfStorageType.setStatus("current")
_F3L3TrafficIPIfRowStatus_Type = RowStatus
_F3L3TrafficIPIfRowStatus_Object = MibTableColumn
f3L3TrafficIPIfRowStatus = _F3L3TrafficIPIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 30),
    _F3L3TrafficIPIfRowStatus_Type()
)
f3L3TrafficIPIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfRowStatus.setStatus("current")
_F3L3TrafficIPIfAction_Type = AffectiveArpActionType
_F3L3TrafficIPIfAction_Object = MibTableColumn
f3L3TrafficIPIfAction = _F3L3TrafficIPIfAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 31),
    _F3L3TrafficIPIfAction_Type()
)
f3L3TrafficIPIfAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfAction.setStatus("deprecated")
_F3L3TrafficIPIfActionX_Type = TrafficIpInterfaceActionType
_F3L3TrafficIPIfActionX_Object = MibTableColumn
f3L3TrafficIPIfActionX = _F3L3TrafficIPIfActionX_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 32),
    _F3L3TrafficIPIfActionX_Type()
)
f3L3TrafficIPIfActionX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfActionX.setStatus("current")
_F3L3TrafficIPIfUnnumberedControl_Type = TruthValue
_F3L3TrafficIPIfUnnumberedControl_Object = MibTableColumn
f3L3TrafficIPIfUnnumberedControl = _F3L3TrafficIPIfUnnumberedControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 33),
    _F3L3TrafficIPIfUnnumberedControl_Type()
)
f3L3TrafficIPIfUnnumberedControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfUnnumberedControl.setStatus("current")
_F3L3TrafficIPIfBorrowedIntf_Type = DisplayString
_F3L3TrafficIPIfBorrowedIntf_Object = MibTableColumn
f3L3TrafficIPIfBorrowedIntf = _F3L3TrafficIPIfBorrowedIntf_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 34),
    _F3L3TrafficIPIfBorrowedIntf_Type()
)
f3L3TrafficIPIfBorrowedIntf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfBorrowedIntf.setStatus("current")
_F3L3TrafficIPIfIpMode_Type = IpMode
_F3L3TrafficIPIfIpMode_Object = MibTableColumn
f3L3TrafficIPIfIpMode = _F3L3TrafficIPIfIpMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 35),
    _F3L3TrafficIPIfIpMode_Type()
)
f3L3TrafficIPIfIpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfIpMode.setStatus("current")
_F3L3TrafficIPIfType_Type = IpInterfaceType
_F3L3TrafficIPIfType_Object = MibTableColumn
f3L3TrafficIPIfType = _F3L3TrafficIPIfType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 36),
    _F3L3TrafficIPIfType_Type()
)
f3L3TrafficIPIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfType.setStatus("current")
_F3L3TrafficIPIfIpv6LinkLocalAddr_Type = Ipv6Address
_F3L3TrafficIPIfIpv6LinkLocalAddr_Object = MibTableColumn
f3L3TrafficIPIfIpv6LinkLocalAddr = _F3L3TrafficIPIfIpv6LinkLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 37),
    _F3L3TrafficIPIfIpv6LinkLocalAddr_Type()
)
f3L3TrafficIPIfIpv6LinkLocalAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfIpv6LinkLocalAddr.setStatus("current")
_F3L3TrafficIPIfIpv6LinkLocalAddrMode_Type = Ipv6LinkLocalAddressMode
_F3L3TrafficIPIfIpv6LinkLocalAddrMode_Object = MibTableColumn
f3L3TrafficIPIfIpv6LinkLocalAddrMode = _F3L3TrafficIPIfIpv6LinkLocalAddrMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 38),
    _F3L3TrafficIPIfIpv6LinkLocalAddrMode_Type()
)
f3L3TrafficIPIfIpv6LinkLocalAddrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfIpv6LinkLocalAddrMode.setStatus("current")
_F3L3TrafficIPIfIpv6StatelessAddrAutoconfigEnabled_Type = TruthValue
_F3L3TrafficIPIfIpv6StatelessAddrAutoconfigEnabled_Object = MibTableColumn
f3L3TrafficIPIfIpv6StatelessAddrAutoconfigEnabled = _F3L3TrafficIPIfIpv6StatelessAddrAutoconfigEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 39),
    _F3L3TrafficIPIfIpv6StatelessAddrAutoconfigEnabled_Type()
)
f3L3TrafficIPIfIpv6StatelessAddrAutoconfigEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfIpv6StatelessAddrAutoconfigEnabled.setStatus("current")
_F3L3TrafficIPIfDefaultGateway_Type = Ipv6Address
_F3L3TrafficIPIfDefaultGateway_Object = MibTableColumn
f3L3TrafficIPIfDefaultGateway = _F3L3TrafficIPIfDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 40),
    _F3L3TrafficIPIfDefaultGateway_Type()
)
f3L3TrafficIPIfDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfDefaultGateway.setStatus("current")
_F3L3TrafficIPIfIcmpErrorMsgRateLimit_Type = Integer32
_F3L3TrafficIPIfIcmpErrorMsgRateLimit_Object = MibTableColumn
f3L3TrafficIPIfIcmpErrorMsgRateLimit = _F3L3TrafficIPIfIcmpErrorMsgRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 41),
    _F3L3TrafficIPIfIcmpErrorMsgRateLimit_Type()
)
f3L3TrafficIPIfIcmpErrorMsgRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfIcmpErrorMsgRateLimit.setStatus("current")
_F3L3TrafficIPIfDhcpv6Role_Type = CmDhcpRole
_F3L3TrafficIPIfDhcpv6Role_Object = MibTableColumn
f3L3TrafficIPIfDhcpv6Role = _F3L3TrafficIPIfDhcpv6Role_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 42),
    _F3L3TrafficIPIfDhcpv6Role_Type()
)
f3L3TrafficIPIfDhcpv6Role.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfDhcpv6Role.setStatus("current")
_F3L3TrafficIPIfDhcpv6Enabled_Type = TruthValue
_F3L3TrafficIPIfDhcpv6Enabled_Object = MibTableColumn
f3L3TrafficIPIfDhcpv6Enabled = _F3L3TrafficIPIfDhcpv6Enabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 43),
    _F3L3TrafficIPIfDhcpv6Enabled_Type()
)
f3L3TrafficIPIfDhcpv6Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfDhcpv6Enabled.setStatus("current")
_F3L3TrafficIPIfDhcpRapidCommitControlEnabled_Type = TruthValue
_F3L3TrafficIPIfDhcpRapidCommitControlEnabled_Object = MibTableColumn
f3L3TrafficIPIfDhcpRapidCommitControlEnabled = _F3L3TrafficIPIfDhcpRapidCommitControlEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 44),
    _F3L3TrafficIPIfDhcpRapidCommitControlEnabled_Type()
)
f3L3TrafficIPIfDhcpRapidCommitControlEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfDhcpRapidCommitControlEnabled.setStatus("current")
_F3L3TrafficIPIfMaxRAInterval_Type = Unsigned32
_F3L3TrafficIPIfMaxRAInterval_Object = MibTableColumn
f3L3TrafficIPIfMaxRAInterval = _F3L3TrafficIPIfMaxRAInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 45),
    _F3L3TrafficIPIfMaxRAInterval_Type()
)
f3L3TrafficIPIfMaxRAInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfMaxRAInterval.setStatus("current")
_F3L3TrafficIPIfMinRAInterval_Type = Unsigned32
_F3L3TrafficIPIfMinRAInterval_Object = MibTableColumn
f3L3TrafficIPIfMinRAInterval = _F3L3TrafficIPIfMinRAInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 46),
    _F3L3TrafficIPIfMinRAInterval_Type()
)
f3L3TrafficIPIfMinRAInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfMinRAInterval.setStatus("current")
_F3L3TrafficIPIfRouterLifeTime_Type = Unsigned32
_F3L3TrafficIPIfRouterLifeTime_Object = MibTableColumn
f3L3TrafficIPIfRouterLifeTime = _F3L3TrafficIPIfRouterLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 47),
    _F3L3TrafficIPIfRouterLifeTime_Type()
)
f3L3TrafficIPIfRouterLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfRouterLifeTime.setStatus("current")
_F3L3TrafficIPIfReachableTime_Type = Unsigned32
_F3L3TrafficIPIfReachableTime_Object = MibTableColumn
f3L3TrafficIPIfReachableTime = _F3L3TrafficIPIfReachableTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 48),
    _F3L3TrafficIPIfReachableTime_Type()
)
f3L3TrafficIPIfReachableTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfReachableTime.setStatus("current")
_F3L3TrafficIPIfRaDhcpMoreConfigEnabled_Type = TruthValue
_F3L3TrafficIPIfRaDhcpMoreConfigEnabled_Object = MibTableColumn
f3L3TrafficIPIfRaDhcpMoreConfigEnabled = _F3L3TrafficIPIfRaDhcpMoreConfigEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 49),
    _F3L3TrafficIPIfRaDhcpMoreConfigEnabled_Type()
)
f3L3TrafficIPIfRaDhcpMoreConfigEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfRaDhcpMoreConfigEnabled.setStatus("current")
_F3L3TrafficIPIfRaManagedAddressConfigEnabled_Type = TruthValue
_F3L3TrafficIPIfRaManagedAddressConfigEnabled_Object = MibTableColumn
f3L3TrafficIPIfRaManagedAddressConfigEnabled = _F3L3TrafficIPIfRaManagedAddressConfigEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 50),
    _F3L3TrafficIPIfRaManagedAddressConfigEnabled_Type()
)
f3L3TrafficIPIfRaManagedAddressConfigEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfRaManagedAddressConfigEnabled.setStatus("current")
_F3L3TrafficIPIfRaRDNSSOptionEnabled_Type = TruthValue
_F3L3TrafficIPIfRaRDNSSOptionEnabled_Object = MibTableColumn
f3L3TrafficIPIfRaRDNSSOptionEnabled = _F3L3TrafficIPIfRaRDNSSOptionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 51),
    _F3L3TrafficIPIfRaRDNSSOptionEnabled_Type()
)
f3L3TrafficIPIfRaRDNSSOptionEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfRaRDNSSOptionEnabled.setStatus("current")
_F3L3TrafficIPIfRaRDNSSLifeTime_Type = Unsigned32
_F3L3TrafficIPIfRaRDNSSLifeTime_Object = MibTableColumn
f3L3TrafficIPIfRaRDNSSLifeTime = _F3L3TrafficIPIfRaRDNSSLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 52),
    _F3L3TrafficIPIfRaRDNSSLifeTime_Type()
)
f3L3TrafficIPIfRaRDNSSLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfRaRDNSSLifeTime.setStatus("current")
_F3L3TrafficIPIfRaDNSSList_Type = DisplayString
_F3L3TrafficIPIfRaDNSSList_Object = MibTableColumn
f3L3TrafficIPIfRaDNSSList = _F3L3TrafficIPIfRaDNSSList_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 53),
    _F3L3TrafficIPIfRaDNSSList_Type()
)
f3L3TrafficIPIfRaDNSSList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfRaDNSSList.setStatus("current")
_F3L3TrafficIPIfRaDefaultRouterPreference_Type = NdpRaDefaultRouterPreference
_F3L3TrafficIPIfRaDefaultRouterPreference_Object = MibTableColumn
f3L3TrafficIPIfRaDefaultRouterPreference = _F3L3TrafficIPIfRaDefaultRouterPreference_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 54),
    _F3L3TrafficIPIfRaDefaultRouterPreference_Type()
)
f3L3TrafficIPIfRaDefaultRouterPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfRaDefaultRouterPreference.setStatus("current")
_F3L3TrafficIPIfDupAddrDetectControl_Type = TruthValue
_F3L3TrafficIPIfDupAddrDetectControl_Object = MibTableColumn
f3L3TrafficIPIfDupAddrDetectControl = _F3L3TrafficIPIfDupAddrDetectControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 55),
    _F3L3TrafficIPIfDupAddrDetectControl_Type()
)
f3L3TrafficIPIfDupAddrDetectControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfDupAddrDetectControl.setStatus("current")
_F3L3TrafficIPIfDupAddrDetectTransmits_Type = Unsigned32
_F3L3TrafficIPIfDupAddrDetectTransmits_Object = MibTableColumn
f3L3TrafficIPIfDupAddrDetectTransmits = _F3L3TrafficIPIfDupAddrDetectTransmits_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 56),
    _F3L3TrafficIPIfDupAddrDetectTransmits_Type()
)
f3L3TrafficIPIfDupAddrDetectTransmits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfDupAddrDetectTransmits.setStatus("current")
_F3L3TrafficIPIfDupAddrDetectRetransTimer_Type = Unsigned32
_F3L3TrafficIPIfDupAddrDetectRetransTimer_Object = MibTableColumn
f3L3TrafficIPIfDupAddrDetectRetransTimer = _F3L3TrafficIPIfDupAddrDetectRetransTimer_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 57),
    _F3L3TrafficIPIfDupAddrDetectRetransTimer_Type()
)
f3L3TrafficIPIfDupAddrDetectRetransTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfDupAddrDetectRetransTimer.setStatus("current")
_F3L3TrafficIPIfMTU_Type = Integer32
_F3L3TrafficIPIfMTU_Object = MibTableColumn
f3L3TrafficIPIfMTU = _F3L3TrafficIPIfMTU_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 9, 1, 58),
    _F3L3TrafficIPIfMTU_Type()
)
f3L3TrafficIPIfMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfMTU.setStatus("current")
_F3DhcpRelayAgentTrafficIpIfMemberTable_Object = MibTable
f3DhcpRelayAgentTrafficIpIfMemberTable = _F3DhcpRelayAgentTrafficIpIfMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 10)
)
if mibBuilder.loadTexts:
    f3DhcpRelayAgentTrafficIpIfMemberTable.setStatus("current")
_F3DhcpRelayAgentTrafficIpIfMemberEntry_Object = MibTableRow
f3DhcpRelayAgentTrafficIpIfMemberEntry = _F3DhcpRelayAgentTrafficIpIfMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 10, 1)
)
f3DhcpRelayAgentTrafficIpIfMemberEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-L3-MIB", "f3DhcpRelayAgentIndex"),
    (0, "F3-L3-MIB", "f3DhcpRelayAgentTrafficIpIfMemberObject"),
)
if mibBuilder.loadTexts:
    f3DhcpRelayAgentTrafficIpIfMemberEntry.setStatus("current")
_F3DhcpRelayAgentTrafficIpIfMemberObject_Type = VariablePointer
_F3DhcpRelayAgentTrafficIpIfMemberObject_Object = MibTableColumn
f3DhcpRelayAgentTrafficIpIfMemberObject = _F3DhcpRelayAgentTrafficIpIfMemberObject_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 10, 1, 1),
    _F3DhcpRelayAgentTrafficIpIfMemberObject_Type()
)
f3DhcpRelayAgentTrafficIpIfMemberObject.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3DhcpRelayAgentTrafficIpIfMemberObject.setStatus("current")
_F3DhcpRelayAgentTrafficIpIfMemberStorageType_Type = StorageType
_F3DhcpRelayAgentTrafficIpIfMemberStorageType_Object = MibTableColumn
f3DhcpRelayAgentTrafficIpIfMemberStorageType = _F3DhcpRelayAgentTrafficIpIfMemberStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 10, 1, 2),
    _F3DhcpRelayAgentTrafficIpIfMemberStorageType_Type()
)
f3DhcpRelayAgentTrafficIpIfMemberStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3DhcpRelayAgentTrafficIpIfMemberStorageType.setStatus("current")
_F3DhcpRelayAgentTrafficIpIfMemberRowStatus_Type = RowStatus
_F3DhcpRelayAgentTrafficIpIfMemberRowStatus_Object = MibTableColumn
f3DhcpRelayAgentTrafficIpIfMemberRowStatus = _F3DhcpRelayAgentTrafficIpIfMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 10, 1, 3),
    _F3DhcpRelayAgentTrafficIpIfMemberRowStatus_Type()
)
f3DhcpRelayAgentTrafficIpIfMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3DhcpRelayAgentTrafficIpIfMemberRowStatus.setStatus("current")
_F3VrfTrafficIpIfMemberTable_Object = MibTable
f3VrfTrafficIpIfMemberTable = _F3VrfTrafficIpIfMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 11)
)
if mibBuilder.loadTexts:
    f3VrfTrafficIpIfMemberTable.setStatus("current")
_F3VrfTrafficIpIfMemberEntry_Object = MibTableRow
f3VrfTrafficIpIfMemberEntry = _F3VrfTrafficIpIfMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 11, 1)
)
f3VrfTrafficIpIfMemberEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-L3-MIB", "f3VrfIndex"),
    (0, "F3-L3-MIB", "f3VrfTrafficIpIfMemberObject"),
)
if mibBuilder.loadTexts:
    f3VrfTrafficIpIfMemberEntry.setStatus("current")
_F3VrfTrafficIpIfMemberObject_Type = VariablePointer
_F3VrfTrafficIpIfMemberObject_Object = MibTableColumn
f3VrfTrafficIpIfMemberObject = _F3VrfTrafficIpIfMemberObject_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 11, 1, 1),
    _F3VrfTrafficIpIfMemberObject_Type()
)
f3VrfTrafficIpIfMemberObject.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3VrfTrafficIpIfMemberObject.setStatus("current")
_F3VrfTrafficIpIfMemberStorageType_Type = StorageType
_F3VrfTrafficIpIfMemberStorageType_Object = MibTableColumn
f3VrfTrafficIpIfMemberStorageType = _F3VrfTrafficIpIfMemberStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 11, 1, 2),
    _F3VrfTrafficIpIfMemberStorageType_Type()
)
f3VrfTrafficIpIfMemberStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3VrfTrafficIpIfMemberStorageType.setStatus("current")
_F3VrfTrafficIpIfMemberRowStatus_Type = RowStatus
_F3VrfTrafficIpIfMemberRowStatus_Object = MibTableColumn
f3VrfTrafficIpIfMemberRowStatus = _F3VrfTrafficIpIfMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 11, 1, 3),
    _F3VrfTrafficIpIfMemberRowStatus_Type()
)
f3VrfTrafficIpIfMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3VrfTrafficIpIfMemberRowStatus.setStatus("current")
_F3L3TrafficIpv4RouteTable_Object = MibTable
f3L3TrafficIpv4RouteTable = _F3L3TrafficIpv4RouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 12)
)
if mibBuilder.loadTexts:
    f3L3TrafficIpv4RouteTable.setStatus("deprecated")
_F3L3TrafficIpv4RouteEntry_Object = MibTableRow
f3L3TrafficIpv4RouteEntry = _F3L3TrafficIpv4RouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 12, 1)
)
f3L3TrafficIpv4RouteEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-L3-MIB", "f3VrfIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficIpv4RouteDest"),
    (0, "F3-L3-MIB", "f3L3TrafficIpv4RouteMask"),
    (0, "F3-L3-MIB", "f3L3TrafficIpv4RouteNextHop"),
    (0, "F3-L3-MIB", "f3L3TrafficIpv4RouteInterface"),
)
if mibBuilder.loadTexts:
    f3L3TrafficIpv4RouteEntry.setStatus("deprecated")
_F3L3TrafficIpv4RouteDest_Type = IpAddress
_F3L3TrafficIpv4RouteDest_Object = MibTableColumn
f3L3TrafficIpv4RouteDest = _F3L3TrafficIpv4RouteDest_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 12, 1, 1),
    _F3L3TrafficIpv4RouteDest_Type()
)
f3L3TrafficIpv4RouteDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIpv4RouteDest.setStatus("deprecated")
_F3L3TrafficIpv4RouteMask_Type = IpAddress
_F3L3TrafficIpv4RouteMask_Object = MibTableColumn
f3L3TrafficIpv4RouteMask = _F3L3TrafficIpv4RouteMask_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 12, 1, 2),
    _F3L3TrafficIpv4RouteMask_Type()
)
f3L3TrafficIpv4RouteMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIpv4RouteMask.setStatus("deprecated")
_F3L3TrafficIpv4RouteNextHop_Type = IpAddress
_F3L3TrafficIpv4RouteNextHop_Object = MibTableColumn
f3L3TrafficIpv4RouteNextHop = _F3L3TrafficIpv4RouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 12, 1, 3),
    _F3L3TrafficIpv4RouteNextHop_Type()
)
f3L3TrafficIpv4RouteNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIpv4RouteNextHop.setStatus("deprecated")
_F3L3TrafficIpv4RouteMetric_Type = Integer32
_F3L3TrafficIpv4RouteMetric_Object = MibTableColumn
f3L3TrafficIpv4RouteMetric = _F3L3TrafficIpv4RouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 12, 1, 4),
    _F3L3TrafficIpv4RouteMetric_Type()
)
f3L3TrafficIpv4RouteMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIpv4RouteMetric.setStatus("deprecated")
_F3L3TrafficIpv4RouteInterface_Type = DisplayString
_F3L3TrafficIpv4RouteInterface_Object = MibTableColumn
f3L3TrafficIpv4RouteInterface = _F3L3TrafficIpv4RouteInterface_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 12, 1, 5),
    _F3L3TrafficIpv4RouteInterface_Type()
)
f3L3TrafficIpv4RouteInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIpv4RouteInterface.setStatus("deprecated")
_F3L3TrafficIpv4RouteAdvertise_Type = TruthValue
_F3L3TrafficIpv4RouteAdvertise_Object = MibTableColumn
f3L3TrafficIpv4RouteAdvertise = _F3L3TrafficIpv4RouteAdvertise_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 12, 1, 6),
    _F3L3TrafficIpv4RouteAdvertise_Type()
)
f3L3TrafficIpv4RouteAdvertise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIpv4RouteAdvertise.setStatus("deprecated")
_F3L3TrafficIpv4RouteStatus_Type = TrafficIpRouteStatus
_F3L3TrafficIpv4RouteStatus_Object = MibTableColumn
f3L3TrafficIpv4RouteStatus = _F3L3TrafficIpv4RouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 12, 1, 7),
    _F3L3TrafficIpv4RouteStatus_Type()
)
f3L3TrafficIpv4RouteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpv4RouteStatus.setStatus("deprecated")
_F3L3TrafficIpv4RouteSourceForwardingEnable_Type = TruthValue
_F3L3TrafficIpv4RouteSourceForwardingEnable_Object = MibTableColumn
f3L3TrafficIpv4RouteSourceForwardingEnable = _F3L3TrafficIpv4RouteSourceForwardingEnable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 12, 1, 8),
    _F3L3TrafficIpv4RouteSourceForwardingEnable_Type()
)
f3L3TrafficIpv4RouteSourceForwardingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIpv4RouteSourceForwardingEnable.setStatus("deprecated")
_F3L3TrafficIpv4RouteFlags_Type = RouteFlags
_F3L3TrafficIpv4RouteFlags_Object = MibTableColumn
f3L3TrafficIpv4RouteFlags = _F3L3TrafficIpv4RouteFlags_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 12, 1, 9),
    _F3L3TrafficIpv4RouteFlags_Type()
)
f3L3TrafficIpv4RouteFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpv4RouteFlags.setStatus("obsolete")
_F3L3TrafficIpv4RouteStorageType_Type = StorageType
_F3L3TrafficIpv4RouteStorageType_Object = MibTableColumn
f3L3TrafficIpv4RouteStorageType = _F3L3TrafficIpv4RouteStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 12, 1, 10),
    _F3L3TrafficIpv4RouteStorageType_Type()
)
f3L3TrafficIpv4RouteStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficIpv4RouteStorageType.setStatus("deprecated")
_F3L3TrafficIpv4RouteRowStatus_Type = RowStatus
_F3L3TrafficIpv4RouteRowStatus_Object = MibTableColumn
f3L3TrafficIpv4RouteRowStatus = _F3L3TrafficIpv4RouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 12, 1, 11),
    _F3L3TrafficIpv4RouteRowStatus_Type()
)
f3L3TrafficIpv4RouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficIpv4RouteRowStatus.setStatus("deprecated")
_F3L3TrafficIpv4RouteType_Type = IpEntryType
_F3L3TrafficIpv4RouteType_Object = MibTableColumn
f3L3TrafficIpv4RouteType = _F3L3TrafficIpv4RouteType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 12, 1, 12),
    _F3L3TrafficIpv4RouteType_Type()
)
f3L3TrafficIpv4RouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpv4RouteType.setStatus("deprecated")
_F3L3TrafficIpv4RouteStatusX_Type = TrafficIpRouteStatusType
_F3L3TrafficIpv4RouteStatusX_Object = MibTableColumn
f3L3TrafficIpv4RouteStatusX = _F3L3TrafficIpv4RouteStatusX_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 12, 1, 13),
    _F3L3TrafficIpv4RouteStatusX_Type()
)
f3L3TrafficIpv4RouteStatusX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpv4RouteStatusX.setStatus("deprecated")
_F3L3TrafficIpv4RouteOrigin_Type = TrafficIpRouteOriginType
_F3L3TrafficIpv4RouteOrigin_Object = MibTableColumn
f3L3TrafficIpv4RouteOrigin = _F3L3TrafficIpv4RouteOrigin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 12, 1, 14),
    _F3L3TrafficIpv4RouteOrigin_Type()
)
f3L3TrafficIpv4RouteOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpv4RouteOrigin.setStatus("deprecated")
_F3L3TrafficArpTable_Object = MibTable
f3L3TrafficArpTable = _F3L3TrafficArpTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 13)
)
if mibBuilder.loadTexts:
    f3L3TrafficArpTable.setStatus("current")
_F3L3TrafficArpEntry_Object = MibTableRow
f3L3TrafficArpEntry = _F3L3TrafficArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 13, 1)
)
f3L3TrafficArpEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficIPIfIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficArpIPAddress"),
)
if mibBuilder.loadTexts:
    f3L3TrafficArpEntry.setStatus("current")
_F3L3TrafficArpIPAddress_Type = IpAddress
_F3L3TrafficArpIPAddress_Object = MibTableColumn
f3L3TrafficArpIPAddress = _F3L3TrafficArpIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 13, 1, 1),
    _F3L3TrafficArpIPAddress_Type()
)
f3L3TrafficArpIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3TrafficArpIPAddress.setStatus("current")
_F3L3TrafficArpMacAddress_Type = MacAddress
_F3L3TrafficArpMacAddress_Object = MibTableColumn
f3L3TrafficArpMacAddress = _F3L3TrafficArpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 13, 1, 2),
    _F3L3TrafficArpMacAddress_Type()
)
f3L3TrafficArpMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficArpMacAddress.setStatus("current")
_F3L3TrafficArpInterface_Type = DisplayString
_F3L3TrafficArpInterface_Object = MibTableColumn
f3L3TrafficArpInterface = _F3L3TrafficArpInterface_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 13, 1, 3),
    _F3L3TrafficArpInterface_Type()
)
f3L3TrafficArpInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficArpInterface.setStatus("current")
_F3L3TrafficArpEntryType_Type = IpEntryType
_F3L3TrafficArpEntryType_Object = MibTableColumn
f3L3TrafficArpEntryType = _F3L3TrafficArpEntryType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 13, 1, 4),
    _F3L3TrafficArpEntryType_Type()
)
f3L3TrafficArpEntryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficArpEntryType.setStatus("current")
_F3L3TrafficArpStorageType_Type = StorageType
_F3L3TrafficArpStorageType_Object = MibTableColumn
f3L3TrafficArpStorageType = _F3L3TrafficArpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 13, 1, 5),
    _F3L3TrafficArpStorageType_Type()
)
f3L3TrafficArpStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficArpStorageType.setStatus("current")
_F3L3TrafficArpRowStatus_Type = RowStatus
_F3L3TrafficArpRowStatus_Object = MibTableColumn
f3L3TrafficArpRowStatus = _F3L3TrafficArpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 13, 1, 6),
    _F3L3TrafficArpRowStatus_Type()
)
f3L3TrafficArpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficArpRowStatus.setStatus("current")
_F3L3TrafficBgpRouterTable_Object = MibTable
f3L3TrafficBgpRouterTable = _F3L3TrafficBgpRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 14)
)
if mibBuilder.loadTexts:
    f3L3TrafficBgpRouterTable.setStatus("current")
_F3L3TrafficBgpRouterEntry_Object = MibTableRow
f3L3TrafficBgpRouterEntry = _F3L3TrafficBgpRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 14, 1)
)
f3L3TrafficBgpRouterEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-L3-MIB", "f3VrfIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficBgpRouterIndex"),
)
if mibBuilder.loadTexts:
    f3L3TrafficBgpRouterEntry.setStatus("current")
_F3L3TrafficBgpRouterIndex_Type = Unsigned32
_F3L3TrafficBgpRouterIndex_Object = MibTableColumn
f3L3TrafficBgpRouterIndex = _F3L3TrafficBgpRouterIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 14, 1, 1),
    _F3L3TrafficBgpRouterIndex_Type()
)
f3L3TrafficBgpRouterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3TrafficBgpRouterIndex.setStatus("current")
_F3L3TrafficBgpRouterAdminState_Type = AdminState
_F3L3TrafficBgpRouterAdminState_Object = MibTableColumn
f3L3TrafficBgpRouterAdminState = _F3L3TrafficBgpRouterAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 14, 1, 2),
    _F3L3TrafficBgpRouterAdminState_Type()
)
f3L3TrafficBgpRouterAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficBgpRouterAdminState.setStatus("current")
_F3L3TrafficBgpRouterSecondaryState_Type = SecondaryState
_F3L3TrafficBgpRouterSecondaryState_Object = MibTableColumn
f3L3TrafficBgpRouterSecondaryState = _F3L3TrafficBgpRouterSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 14, 1, 3),
    _F3L3TrafficBgpRouterSecondaryState_Type()
)
f3L3TrafficBgpRouterSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficBgpRouterSecondaryState.setStatus("current")
_F3L3TrafficBgpRouterOperationalState_Type = OperationalState
_F3L3TrafficBgpRouterOperationalState_Object = MibTableColumn
f3L3TrafficBgpRouterOperationalState = _F3L3TrafficBgpRouterOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 14, 1, 4),
    _F3L3TrafficBgpRouterOperationalState_Type()
)
f3L3TrafficBgpRouterOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficBgpRouterOperationalState.setStatus("current")
_F3L3TrafficBgpRouterId_Type = IpAddress
_F3L3TrafficBgpRouterId_Object = MibTableColumn
f3L3TrafficBgpRouterId = _F3L3TrafficBgpRouterId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 14, 1, 5),
    _F3L3TrafficBgpRouterId_Type()
)
f3L3TrafficBgpRouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficBgpRouterId.setStatus("current")
_F3L3TrafficBgpRouterAsNumber_Type = Unsigned32
_F3L3TrafficBgpRouterAsNumber_Object = MibTableColumn
f3L3TrafficBgpRouterAsNumber = _F3L3TrafficBgpRouterAsNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 14, 1, 6),
    _F3L3TrafficBgpRouterAsNumber_Type()
)
f3L3TrafficBgpRouterAsNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficBgpRouterAsNumber.setStatus("current")
_F3L3TrafficBgpRouterConnectedRoutesRedistControl_Type = TruthValue
_F3L3TrafficBgpRouterConnectedRoutesRedistControl_Object = MibTableColumn
f3L3TrafficBgpRouterConnectedRoutesRedistControl = _F3L3TrafficBgpRouterConnectedRoutesRedistControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 14, 1, 7),
    _F3L3TrafficBgpRouterConnectedRoutesRedistControl_Type()
)
f3L3TrafficBgpRouterConnectedRoutesRedistControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficBgpRouterConnectedRoutesRedistControl.setStatus("deprecated")
_F3L3TrafficBgpRouterOspfRoutesRedistControl_Type = TruthValue
_F3L3TrafficBgpRouterOspfRoutesRedistControl_Object = MibTableColumn
f3L3TrafficBgpRouterOspfRoutesRedistControl = _F3L3TrafficBgpRouterOspfRoutesRedistControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 14, 1, 8),
    _F3L3TrafficBgpRouterOspfRoutesRedistControl_Type()
)
f3L3TrafficBgpRouterOspfRoutesRedistControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficBgpRouterOspfRoutesRedistControl.setStatus("deprecated")
_F3L3TrafficBgpRouterStaticRoutesRedistControl_Type = TruthValue
_F3L3TrafficBgpRouterStaticRoutesRedistControl_Object = MibTableColumn
f3L3TrafficBgpRouterStaticRoutesRedistControl = _F3L3TrafficBgpRouterStaticRoutesRedistControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 14, 1, 9),
    _F3L3TrafficBgpRouterStaticRoutesRedistControl_Type()
)
f3L3TrafficBgpRouterStaticRoutesRedistControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficBgpRouterStaticRoutesRedistControl.setStatus("deprecated")
_F3L3TrafficBgpRouterDhcpRoutesRedistControl_Type = TruthValue
_F3L3TrafficBgpRouterDhcpRoutesRedistControl_Object = MibTableColumn
f3L3TrafficBgpRouterDhcpRoutesRedistControl = _F3L3TrafficBgpRouterDhcpRoutesRedistControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 14, 1, 10),
    _F3L3TrafficBgpRouterDhcpRoutesRedistControl_Type()
)
f3L3TrafficBgpRouterDhcpRoutesRedistControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficBgpRouterDhcpRoutesRedistControl.setStatus("deprecated")
_F3L3TrafficBgpRouterStorageType_Type = StorageType
_F3L3TrafficBgpRouterStorageType_Object = MibTableColumn
f3L3TrafficBgpRouterStorageType = _F3L3TrafficBgpRouterStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 14, 1, 11),
    _F3L3TrafficBgpRouterStorageType_Type()
)
f3L3TrafficBgpRouterStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficBgpRouterStorageType.setStatus("current")
_F3L3TrafficBgpRouterRowStatus_Type = RowStatus
_F3L3TrafficBgpRouterRowStatus_Object = MibTableColumn
f3L3TrafficBgpRouterRowStatus = _F3L3TrafficBgpRouterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 14, 1, 12),
    _F3L3TrafficBgpRouterRowStatus_Type()
)
f3L3TrafficBgpRouterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficBgpRouterRowStatus.setStatus("current")
_F3L3TrafficBgpRouterAction_Type = BgpRouterActionType
_F3L3TrafficBgpRouterAction_Object = MibTableColumn
f3L3TrafficBgpRouterAction = _F3L3TrafficBgpRouterAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 14, 1, 13),
    _F3L3TrafficBgpRouterAction_Type()
)
f3L3TrafficBgpRouterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficBgpRouterAction.setStatus("current")
_F3L3TrafficBgpRouterIBgpAdminDistance_Type = Unsigned32
_F3L3TrafficBgpRouterIBgpAdminDistance_Object = MibTableColumn
f3L3TrafficBgpRouterIBgpAdminDistance = _F3L3TrafficBgpRouterIBgpAdminDistance_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 14, 1, 14),
    _F3L3TrafficBgpRouterIBgpAdminDistance_Type()
)
f3L3TrafficBgpRouterIBgpAdminDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficBgpRouterIBgpAdminDistance.setStatus("current")
_F3L3TrafficBgpRouterEBgpAdminDistance_Type = Unsigned32
_F3L3TrafficBgpRouterEBgpAdminDistance_Object = MibTableColumn
f3L3TrafficBgpRouterEBgpAdminDistance = _F3L3TrafficBgpRouterEBgpAdminDistance_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 14, 1, 15),
    _F3L3TrafficBgpRouterEBgpAdminDistance_Type()
)
f3L3TrafficBgpRouterEBgpAdminDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficBgpRouterEBgpAdminDistance.setStatus("current")
_F3L3TrafficBgpRouterEcmpMaximumPaths_Type = Unsigned32
_F3L3TrafficBgpRouterEcmpMaximumPaths_Object = MibTableColumn
f3L3TrafficBgpRouterEcmpMaximumPaths = _F3L3TrafficBgpRouterEcmpMaximumPaths_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 14, 1, 16),
    _F3L3TrafficBgpRouterEcmpMaximumPaths_Type()
)
f3L3TrafficBgpRouterEcmpMaximumPaths.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficBgpRouterEcmpMaximumPaths.setStatus("current")
_F3L3TrafficBgpRouterRestartTime_Type = Unsigned32
_F3L3TrafficBgpRouterRestartTime_Object = MibTableColumn
f3L3TrafficBgpRouterRestartTime = _F3L3TrafficBgpRouterRestartTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 14, 1, 17),
    _F3L3TrafficBgpRouterRestartTime_Type()
)
f3L3TrafficBgpRouterRestartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficBgpRouterRestartTime.setStatus("current")
_F3L3TrafficBgpRouterStaleRoutesTime_Type = Unsigned32
_F3L3TrafficBgpRouterStaleRoutesTime_Object = MibTableColumn
f3L3TrafficBgpRouterStaleRoutesTime = _F3L3TrafficBgpRouterStaleRoutesTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 14, 1, 18),
    _F3L3TrafficBgpRouterStaleRoutesTime_Type()
)
f3L3TrafficBgpRouterStaleRoutesTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficBgpRouterStaleRoutesTime.setStatus("current")
_F3L3TrafficBgpRouteTable_Object = MibTable
f3L3TrafficBgpRouteTable = _F3L3TrafficBgpRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 15)
)
if mibBuilder.loadTexts:
    f3L3TrafficBgpRouteTable.setStatus("current")
_F3L3TrafficBgpRouteEntry_Object = MibTableRow
f3L3TrafficBgpRouteEntry = _F3L3TrafficBgpRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 15, 1)
)
f3L3TrafficBgpRouteEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-L3-MIB", "f3VrfIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficBgpRouterIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficBgpRouteNetwork"),
    (0, "F3-L3-MIB", "f3L3TrafficBgpRouteMetric"),
    (0, "F3-L3-MIB", "f3L3TrafficBgpRouteNextHop"),
)
if mibBuilder.loadTexts:
    f3L3TrafficBgpRouteEntry.setStatus("current")
_F3L3TrafficBgpRouteNetwork_Type = IpAddress
_F3L3TrafficBgpRouteNetwork_Object = MibTableColumn
f3L3TrafficBgpRouteNetwork = _F3L3TrafficBgpRouteNetwork_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 15, 1, 1),
    _F3L3TrafficBgpRouteNetwork_Type()
)
f3L3TrafficBgpRouteNetwork.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3TrafficBgpRouteNetwork.setStatus("current")
_F3L3TrafficBgpRouteMetric_Type = Unsigned32
_F3L3TrafficBgpRouteMetric_Object = MibTableColumn
f3L3TrafficBgpRouteMetric = _F3L3TrafficBgpRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 15, 1, 2),
    _F3L3TrafficBgpRouteMetric_Type()
)
f3L3TrafficBgpRouteMetric.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3TrafficBgpRouteMetric.setStatus("current")
_F3L3TrafficBgpRouteNextHop_Type = IpAddress
_F3L3TrafficBgpRouteNextHop_Object = MibTableColumn
f3L3TrafficBgpRouteNextHop = _F3L3TrafficBgpRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 15, 1, 3),
    _F3L3TrafficBgpRouteNextHop_Type()
)
f3L3TrafficBgpRouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3TrafficBgpRouteNextHop.setStatus("current")


class _F3L3TrafficBgpRoutePath_Type(DisplayString):
    """Custom type f3L3TrafficBgpRoutePath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_F3L3TrafficBgpRoutePath_Type.__name__ = "DisplayString"
_F3L3TrafficBgpRoutePath_Object = MibTableColumn
f3L3TrafficBgpRoutePath = _F3L3TrafficBgpRoutePath_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 15, 1, 4),
    _F3L3TrafficBgpRoutePath_Type()
)
f3L3TrafficBgpRoutePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficBgpRoutePath.setStatus("current")
_F3L3TrafficBgpPeerTable_Object = MibTable
f3L3TrafficBgpPeerTable = _F3L3TrafficBgpPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 16)
)
if mibBuilder.loadTexts:
    f3L3TrafficBgpPeerTable.setStatus("current")
_F3L3TrafficBgpPeerEntry_Object = MibTableRow
f3L3TrafficBgpPeerEntry = _F3L3TrafficBgpPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 16, 1)
)
f3L3TrafficBgpPeerEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-L3-MIB", "f3VrfIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficBgpRouterIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficBgpPeerIndex"),
)
if mibBuilder.loadTexts:
    f3L3TrafficBgpPeerEntry.setStatus("current")
_F3L3TrafficBgpPeerIndex_Type = Unsigned32
_F3L3TrafficBgpPeerIndex_Object = MibTableColumn
f3L3TrafficBgpPeerIndex = _F3L3TrafficBgpPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 16, 1, 1),
    _F3L3TrafficBgpPeerIndex_Type()
)
f3L3TrafficBgpPeerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3TrafficBgpPeerIndex.setStatus("current")
_F3L3TrafficBgpPeerAdminState_Type = AdminState
_F3L3TrafficBgpPeerAdminState_Object = MibTableColumn
f3L3TrafficBgpPeerAdminState = _F3L3TrafficBgpPeerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 16, 1, 2),
    _F3L3TrafficBgpPeerAdminState_Type()
)
f3L3TrafficBgpPeerAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficBgpPeerAdminState.setStatus("current")
_F3L3TrafficBgpPeerSecondaryState_Type = SecondaryState
_F3L3TrafficBgpPeerSecondaryState_Object = MibTableColumn
f3L3TrafficBgpPeerSecondaryState = _F3L3TrafficBgpPeerSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 16, 1, 3),
    _F3L3TrafficBgpPeerSecondaryState_Type()
)
f3L3TrafficBgpPeerSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficBgpPeerSecondaryState.setStatus("current")
_F3L3TrafficBgpPeerOperationalState_Type = OperationalState
_F3L3TrafficBgpPeerOperationalState_Object = MibTableColumn
f3L3TrafficBgpPeerOperationalState = _F3L3TrafficBgpPeerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 16, 1, 4),
    _F3L3TrafficBgpPeerOperationalState_Type()
)
f3L3TrafficBgpPeerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficBgpPeerOperationalState.setStatus("current")
_F3L3TrafficBgpPeerIpv4Addr_Type = IpAddress
_F3L3TrafficBgpPeerIpv4Addr_Object = MibTableColumn
f3L3TrafficBgpPeerIpv4Addr = _F3L3TrafficBgpPeerIpv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 16, 1, 5),
    _F3L3TrafficBgpPeerIpv4Addr_Type()
)
f3L3TrafficBgpPeerIpv4Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficBgpPeerIpv4Addr.setStatus("current")
_F3L3TrafficBgpPeerAsNumber_Type = Unsigned32
_F3L3TrafficBgpPeerAsNumber_Object = MibTableColumn
f3L3TrafficBgpPeerAsNumber = _F3L3TrafficBgpPeerAsNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 16, 1, 6),
    _F3L3TrafficBgpPeerAsNumber_Type()
)
f3L3TrafficBgpPeerAsNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficBgpPeerAsNumber.setStatus("current")


class _F3L3TrafficBgpPeerDescription_Type(DisplayString):
    """Custom type f3L3TrafficBgpPeerDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_F3L3TrafficBgpPeerDescription_Type.__name__ = "DisplayString"
_F3L3TrafficBgpPeerDescription_Object = MibTableColumn
f3L3TrafficBgpPeerDescription = _F3L3TrafficBgpPeerDescription_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 16, 1, 7),
    _F3L3TrafficBgpPeerDescription_Type()
)
f3L3TrafficBgpPeerDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficBgpPeerDescription.setStatus("current")
_F3L3TrafficBgpPeerBgpSessionState_Type = BgpSessionStateType
_F3L3TrafficBgpPeerBgpSessionState_Object = MibTableColumn
f3L3TrafficBgpPeerBgpSessionState = _F3L3TrafficBgpPeerBgpSessionState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 16, 1, 8),
    _F3L3TrafficBgpPeerBgpSessionState_Type()
)
f3L3TrafficBgpPeerBgpSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficBgpPeerBgpSessionState.setStatus("current")
_F3L3TrafficBgpPeerHoldTime_Type = Unsigned32
_F3L3TrafficBgpPeerHoldTime_Object = MibTableColumn
f3L3TrafficBgpPeerHoldTime = _F3L3TrafficBgpPeerHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 16, 1, 9),
    _F3L3TrafficBgpPeerHoldTime_Type()
)
f3L3TrafficBgpPeerHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficBgpPeerHoldTime.setStatus("current")
_F3L3TrafficBgpPeerStartupHoldTime_Type = Unsigned32
_F3L3TrafficBgpPeerStartupHoldTime_Object = MibTableColumn
f3L3TrafficBgpPeerStartupHoldTime = _F3L3TrafficBgpPeerStartupHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 16, 1, 10),
    _F3L3TrafficBgpPeerStartupHoldTime_Type()
)
f3L3TrafficBgpPeerStartupHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficBgpPeerStartupHoldTime.setStatus("current")
_F3L3TrafficBgpPeerKeepAliveTime_Type = Unsigned32
_F3L3TrafficBgpPeerKeepAliveTime_Object = MibTableColumn
f3L3TrafficBgpPeerKeepAliveTime = _F3L3TrafficBgpPeerKeepAliveTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 16, 1, 11),
    _F3L3TrafficBgpPeerKeepAliveTime_Type()
)
f3L3TrafficBgpPeerKeepAliveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficBgpPeerKeepAliveTime.setStatus("current")
_F3L3TrafficBgpPeerConnectRetryTime_Type = Unsigned32
_F3L3TrafficBgpPeerConnectRetryTime_Object = MibTableColumn
f3L3TrafficBgpPeerConnectRetryTime = _F3L3TrafficBgpPeerConnectRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 16, 1, 12),
    _F3L3TrafficBgpPeerConnectRetryTime_Type()
)
f3L3TrafficBgpPeerConnectRetryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficBgpPeerConnectRetryTime.setStatus("current")
_F3L3TrafficBgpPeerUpdateSourceIp_Type = IpAddress
_F3L3TrafficBgpPeerUpdateSourceIp_Object = MibTableColumn
f3L3TrafficBgpPeerUpdateSourceIp = _F3L3TrafficBgpPeerUpdateSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 16, 1, 13),
    _F3L3TrafficBgpPeerUpdateSourceIp_Type()
)
f3L3TrafficBgpPeerUpdateSourceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficBgpPeerUpdateSourceIp.setStatus("current")
_F3L3TrafficBgpPeerAuthenticationKey_Type = VariablePointer
_F3L3TrafficBgpPeerAuthenticationKey_Object = MibTableColumn
f3L3TrafficBgpPeerAuthenticationKey = _F3L3TrafficBgpPeerAuthenticationKey_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 16, 1, 14),
    _F3L3TrafficBgpPeerAuthenticationKey_Type()
)
f3L3TrafficBgpPeerAuthenticationKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficBgpPeerAuthenticationKey.setStatus("current")
_F3L3TrafficBgpPeerTimeSinceUpTransition_Type = Unsigned32
_F3L3TrafficBgpPeerTimeSinceUpTransition_Object = MibTableColumn
f3L3TrafficBgpPeerTimeSinceUpTransition = _F3L3TrafficBgpPeerTimeSinceUpTransition_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 16, 1, 15),
    _F3L3TrafficBgpPeerTimeSinceUpTransition_Type()
)
f3L3TrafficBgpPeerTimeSinceUpTransition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficBgpPeerTimeSinceUpTransition.setStatus("current")
_F3L3TrafficBgpPeerTimeSinceDownTransition_Type = Unsigned32
_F3L3TrafficBgpPeerTimeSinceDownTransition_Object = MibTableColumn
f3L3TrafficBgpPeerTimeSinceDownTransition = _F3L3TrafficBgpPeerTimeSinceDownTransition_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 16, 1, 16),
    _F3L3TrafficBgpPeerTimeSinceDownTransition_Type()
)
f3L3TrafficBgpPeerTimeSinceDownTransition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficBgpPeerTimeSinceDownTransition.setStatus("current")
_F3L3TrafficBgpPeerStorageType_Type = StorageType
_F3L3TrafficBgpPeerStorageType_Object = MibTableColumn
f3L3TrafficBgpPeerStorageType = _F3L3TrafficBgpPeerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 16, 1, 17),
    _F3L3TrafficBgpPeerStorageType_Type()
)
f3L3TrafficBgpPeerStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficBgpPeerStorageType.setStatus("current")
_F3L3TrafficBgpPeerRowStatus_Type = RowStatus
_F3L3TrafficBgpPeerRowStatus_Object = MibTableColumn
f3L3TrafficBgpPeerRowStatus = _F3L3TrafficBgpPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 16, 1, 18),
    _F3L3TrafficBgpPeerRowStatus_Type()
)
f3L3TrafficBgpPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficBgpPeerRowStatus.setStatus("current")
_F3L3TrafficBgpPeerIpVersion_Type = IpVersion
_F3L3TrafficBgpPeerIpVersion_Object = MibTableColumn
f3L3TrafficBgpPeerIpVersion = _F3L3TrafficBgpPeerIpVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 16, 1, 19),
    _F3L3TrafficBgpPeerIpVersion_Type()
)
f3L3TrafficBgpPeerIpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficBgpPeerIpVersion.setStatus("current")
_F3L3TrafficBgpPeerIpv6Address_Type = Ipv6Address
_F3L3TrafficBgpPeerIpv6Address_Object = MibTableColumn
f3L3TrafficBgpPeerIpv6Address = _F3L3TrafficBgpPeerIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 16, 1, 20),
    _F3L3TrafficBgpPeerIpv6Address_Type()
)
f3L3TrafficBgpPeerIpv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficBgpPeerIpv6Address.setStatus("current")
_F3L3TrafficBgpPeerUpdateSourceIpv6_Type = Ipv6Address
_F3L3TrafficBgpPeerUpdateSourceIpv6_Object = MibTableColumn
f3L3TrafficBgpPeerUpdateSourceIpv6 = _F3L3TrafficBgpPeerUpdateSourceIpv6_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 16, 1, 21),
    _F3L3TrafficBgpPeerUpdateSourceIpv6_Type()
)
f3L3TrafficBgpPeerUpdateSourceIpv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficBgpPeerUpdateSourceIpv6.setStatus("current")
_F3L3TrafficBgpPeerMultihopControl_Type = TruthValue
_F3L3TrafficBgpPeerMultihopControl_Object = MibTableColumn
f3L3TrafficBgpPeerMultihopControl = _F3L3TrafficBgpPeerMultihopControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 16, 1, 22),
    _F3L3TrafficBgpPeerMultihopControl_Type()
)
f3L3TrafficBgpPeerMultihopControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficBgpPeerMultihopControl.setStatus("current")
_F3L3TrafficBgpPeerMultihopTtl_Type = Unsigned32
_F3L3TrafficBgpPeerMultihopTtl_Object = MibTableColumn
f3L3TrafficBgpPeerMultihopTtl = _F3L3TrafficBgpPeerMultihopTtl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 16, 1, 23),
    _F3L3TrafficBgpPeerMultihopTtl_Type()
)
f3L3TrafficBgpPeerMultihopTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficBgpPeerMultihopTtl.setStatus("current")
_F3L3TrafficBgpPeerUpdateSourceInterface_Type = DisplayString
_F3L3TrafficBgpPeerUpdateSourceInterface_Object = MibTableColumn
f3L3TrafficBgpPeerUpdateSourceInterface = _F3L3TrafficBgpPeerUpdateSourceInterface_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 16, 1, 24),
    _F3L3TrafficBgpPeerUpdateSourceInterface_Type()
)
f3L3TrafficBgpPeerUpdateSourceInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficBgpPeerUpdateSourceInterface.setStatus("current")
_F3L3TrafficBgpPeerUpdateSourceType_Type = BgpUpdateSourceType
_F3L3TrafficBgpPeerUpdateSourceType_Object = MibTableColumn
f3L3TrafficBgpPeerUpdateSourceType = _F3L3TrafficBgpPeerUpdateSourceType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 16, 1, 25),
    _F3L3TrafficBgpPeerUpdateSourceType_Type()
)
f3L3TrafficBgpPeerUpdateSourceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficBgpPeerUpdateSourceType.setStatus("current")
_F3L3TrafficBgpPeerLocalPreference_Type = Unsigned32
_F3L3TrafficBgpPeerLocalPreference_Object = MibTableColumn
f3L3TrafficBgpPeerLocalPreference = _F3L3TrafficBgpPeerLocalPreference_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 16, 1, 26),
    _F3L3TrafficBgpPeerLocalPreference_Type()
)
f3L3TrafficBgpPeerLocalPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficBgpPeerLocalPreference.setStatus("current")
_F3L3TrafficBgpPeerRouteReflectorClient_Type = TruthValue
_F3L3TrafficBgpPeerRouteReflectorClient_Object = MibTableColumn
f3L3TrafficBgpPeerRouteReflectorClient = _F3L3TrafficBgpPeerRouteReflectorClient_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 16, 1, 27),
    _F3L3TrafficBgpPeerRouteReflectorClient_Type()
)
f3L3TrafficBgpPeerRouteReflectorClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficBgpPeerRouteReflectorClient.setStatus("current")
_F3L3TrafficBgpPeerRouteReflectorClusterId_Type = IpAddress
_F3L3TrafficBgpPeerRouteReflectorClusterId_Object = MibTableColumn
f3L3TrafficBgpPeerRouteReflectorClusterId = _F3L3TrafficBgpPeerRouteReflectorClusterId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 16, 1, 28),
    _F3L3TrafficBgpPeerRouteReflectorClusterId_Type()
)
f3L3TrafficBgpPeerRouteReflectorClusterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficBgpPeerRouteReflectorClusterId.setStatus("current")
_F3L3TrafficBgpPeerBgpRouteInboundFilter_Type = DisplayString
_F3L3TrafficBgpPeerBgpRouteInboundFilter_Object = MibTableColumn
f3L3TrafficBgpPeerBgpRouteInboundFilter = _F3L3TrafficBgpPeerBgpRouteInboundFilter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 16, 1, 29),
    _F3L3TrafficBgpPeerBgpRouteInboundFilter_Type()
)
f3L3TrafficBgpPeerBgpRouteInboundFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficBgpPeerBgpRouteInboundFilter.setStatus("current")
_F3L3TrafficBgpPeerBgpRouteOutboundFilter_Type = DisplayString
_F3L3TrafficBgpPeerBgpRouteOutboundFilter_Object = MibTableColumn
f3L3TrafficBgpPeerBgpRouteOutboundFilter = _F3L3TrafficBgpPeerBgpRouteOutboundFilter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 16, 1, 30),
    _F3L3TrafficBgpPeerBgpRouteOutboundFilter_Type()
)
f3L3TrafficBgpPeerBgpRouteOutboundFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficBgpPeerBgpRouteOutboundFilter.setStatus("current")
_F3L3TrafficBgpPeerBgpGracefulRestart_Type = BgpGracefulRestartControlType
_F3L3TrafficBgpPeerBgpGracefulRestart_Object = MibTableColumn
f3L3TrafficBgpPeerBgpGracefulRestart = _F3L3TrafficBgpPeerBgpGracefulRestart_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 16, 1, 31),
    _F3L3TrafficBgpPeerBgpGracefulRestart_Type()
)
f3L3TrafficBgpPeerBgpGracefulRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficBgpPeerBgpGracefulRestart.setStatus("current")
_F3L3TrafficBgpPeerPeerRestartTime_Type = Unsigned32
_F3L3TrafficBgpPeerPeerRestartTime_Object = MibTableColumn
f3L3TrafficBgpPeerPeerRestartTime = _F3L3TrafficBgpPeerPeerRestartTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 16, 1, 32),
    _F3L3TrafficBgpPeerPeerRestartTime_Type()
)
f3L3TrafficBgpPeerPeerRestartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficBgpPeerPeerRestartTime.setStatus("current")
_F3L3TrafficBgpPeerPeerRestarting_Type = TruthValue
_F3L3TrafficBgpPeerPeerRestarting_Object = MibTableColumn
f3L3TrafficBgpPeerPeerRestarting = _F3L3TrafficBgpPeerPeerRestarting_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 16, 1, 33),
    _F3L3TrafficBgpPeerPeerRestarting_Type()
)
f3L3TrafficBgpPeerPeerRestarting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficBgpPeerPeerRestarting.setStatus("current")
_F3VrfOspfRouterTable_Object = MibTable
f3VrfOspfRouterTable = _F3VrfOspfRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 17)
)
if mibBuilder.loadTexts:
    f3VrfOspfRouterTable.setStatus("current")
_F3VrfOspfRouterEntry_Object = MibTableRow
f3VrfOspfRouterEntry = _F3VrfOspfRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 17, 1)
)
f3VrfOspfRouterEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-L3-MIB", "f3VrfIndex"),
    (0, "F3-L3-MIB", "f3VrfOspfRouterIndex"),
)
if mibBuilder.loadTexts:
    f3VrfOspfRouterEntry.setStatus("current")
_F3VrfOspfRouterIndex_Type = Unsigned32
_F3VrfOspfRouterIndex_Object = MibTableColumn
f3VrfOspfRouterIndex = _F3VrfOspfRouterIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 17, 1, 1),
    _F3VrfOspfRouterIndex_Type()
)
f3VrfOspfRouterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3VrfOspfRouterIndex.setStatus("current")
_F3VrfOspfRouterAdminState_Type = AdminState
_F3VrfOspfRouterAdminState_Object = MibTableColumn
f3VrfOspfRouterAdminState = _F3VrfOspfRouterAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 17, 1, 2),
    _F3VrfOspfRouterAdminState_Type()
)
f3VrfOspfRouterAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3VrfOspfRouterAdminState.setStatus("current")
_F3VrfOspfRouterSecondaryState_Type = SecondaryState
_F3VrfOspfRouterSecondaryState_Object = MibTableColumn
f3VrfOspfRouterSecondaryState = _F3VrfOspfRouterSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 17, 1, 3),
    _F3VrfOspfRouterSecondaryState_Type()
)
f3VrfOspfRouterSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3VrfOspfRouterSecondaryState.setStatus("current")
_F3VrfOspfRouterOperationalState_Type = OperationalState
_F3VrfOspfRouterOperationalState_Object = MibTableColumn
f3VrfOspfRouterOperationalState = _F3VrfOspfRouterOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 17, 1, 4),
    _F3VrfOspfRouterOperationalState_Type()
)
f3VrfOspfRouterOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3VrfOspfRouterOperationalState.setStatus("current")
_F3VrfOspfRouterId_Type = IpAddress
_F3VrfOspfRouterId_Object = MibTableColumn
f3VrfOspfRouterId = _F3VrfOspfRouterId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 17, 1, 5),
    _F3VrfOspfRouterId_Type()
)
f3VrfOspfRouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3VrfOspfRouterId.setStatus("current")


class _F3VrfOspfRouterDescription_Type(DisplayString):
    """Custom type f3VrfOspfRouterDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_F3VrfOspfRouterDescription_Type.__name__ = "DisplayString"
_F3VrfOspfRouterDescription_Object = MibTableColumn
f3VrfOspfRouterDescription = _F3VrfOspfRouterDescription_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 17, 1, 6),
    _F3VrfOspfRouterDescription_Type()
)
f3VrfOspfRouterDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3VrfOspfRouterDescription.setStatus("current")
_F3VrfOspfRouterBgpRoutesRedistributeToOspf_Type = TruthValue
_F3VrfOspfRouterBgpRoutesRedistributeToOspf_Object = MibTableColumn
f3VrfOspfRouterBgpRoutesRedistributeToOspf = _F3VrfOspfRouterBgpRoutesRedistributeToOspf_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 17, 1, 7),
    _F3VrfOspfRouterBgpRoutesRedistributeToOspf_Type()
)
f3VrfOspfRouterBgpRoutesRedistributeToOspf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3VrfOspfRouterBgpRoutesRedistributeToOspf.setStatus("current")
_F3VrfOspfRouterBgpRoutesMetricType_Type = RoutesMetricType
_F3VrfOspfRouterBgpRoutesMetricType_Object = MibTableColumn
f3VrfOspfRouterBgpRoutesMetricType = _F3VrfOspfRouterBgpRoutesMetricType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 17, 1, 8),
    _F3VrfOspfRouterBgpRoutesMetricType_Type()
)
f3VrfOspfRouterBgpRoutesMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3VrfOspfRouterBgpRoutesMetricType.setStatus("current")
_F3VrfOspfRouterBgpRoutesMetric_Type = Unsigned32
_F3VrfOspfRouterBgpRoutesMetric_Object = MibTableColumn
f3VrfOspfRouterBgpRoutesMetric = _F3VrfOspfRouterBgpRoutesMetric_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 17, 1, 9),
    _F3VrfOspfRouterBgpRoutesMetric_Type()
)
f3VrfOspfRouterBgpRoutesMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3VrfOspfRouterBgpRoutesMetric.setStatus("current")
_F3VrfOspfRouterStaticRoutesRedistributeToOspf_Type = TruthValue
_F3VrfOspfRouterStaticRoutesRedistributeToOspf_Object = MibTableColumn
f3VrfOspfRouterStaticRoutesRedistributeToOspf = _F3VrfOspfRouterStaticRoutesRedistributeToOspf_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 17, 1, 10),
    _F3VrfOspfRouterStaticRoutesRedistributeToOspf_Type()
)
f3VrfOspfRouterStaticRoutesRedistributeToOspf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3VrfOspfRouterStaticRoutesRedistributeToOspf.setStatus("current")
_F3VrfOspfRouterStaticRoutesMetricType_Type = RoutesMetricType
_F3VrfOspfRouterStaticRoutesMetricType_Object = MibTableColumn
f3VrfOspfRouterStaticRoutesMetricType = _F3VrfOspfRouterStaticRoutesMetricType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 17, 1, 11),
    _F3VrfOspfRouterStaticRoutesMetricType_Type()
)
f3VrfOspfRouterStaticRoutesMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3VrfOspfRouterStaticRoutesMetricType.setStatus("current")
_F3VrfOspfRouterStaticRoutesMetric_Type = Unsigned32
_F3VrfOspfRouterStaticRoutesMetric_Object = MibTableColumn
f3VrfOspfRouterStaticRoutesMetric = _F3VrfOspfRouterStaticRoutesMetric_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 17, 1, 12),
    _F3VrfOspfRouterStaticRoutesMetric_Type()
)
f3VrfOspfRouterStaticRoutesMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3VrfOspfRouterStaticRoutesMetric.setStatus("current")
_F3VrfOspfRouterConnectedRoutesRedistributeToOspf_Type = TruthValue
_F3VrfOspfRouterConnectedRoutesRedistributeToOspf_Object = MibTableColumn
f3VrfOspfRouterConnectedRoutesRedistributeToOspf = _F3VrfOspfRouterConnectedRoutesRedistributeToOspf_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 17, 1, 13),
    _F3VrfOspfRouterConnectedRoutesRedistributeToOspf_Type()
)
f3VrfOspfRouterConnectedRoutesRedistributeToOspf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3VrfOspfRouterConnectedRoutesRedistributeToOspf.setStatus("current")
_F3VrfOspfRouterConnectedRoutesMetricType_Type = RoutesMetricType
_F3VrfOspfRouterConnectedRoutesMetricType_Object = MibTableColumn
f3VrfOspfRouterConnectedRoutesMetricType = _F3VrfOspfRouterConnectedRoutesMetricType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 17, 1, 14),
    _F3VrfOspfRouterConnectedRoutesMetricType_Type()
)
f3VrfOspfRouterConnectedRoutesMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3VrfOspfRouterConnectedRoutesMetricType.setStatus("current")
_F3VrfOspfRouterConnectedRoutesMetric_Type = Unsigned32
_F3VrfOspfRouterConnectedRoutesMetric_Object = MibTableColumn
f3VrfOspfRouterConnectedRoutesMetric = _F3VrfOspfRouterConnectedRoutesMetric_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 17, 1, 15),
    _F3VrfOspfRouterConnectedRoutesMetric_Type()
)
f3VrfOspfRouterConnectedRoutesMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3VrfOspfRouterConnectedRoutesMetric.setStatus("current")
_F3VrfOspfRouterDhcpRoutesRedistributeToOspf_Type = TruthValue
_F3VrfOspfRouterDhcpRoutesRedistributeToOspf_Object = MibTableColumn
f3VrfOspfRouterDhcpRoutesRedistributeToOspf = _F3VrfOspfRouterDhcpRoutesRedistributeToOspf_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 17, 1, 16),
    _F3VrfOspfRouterDhcpRoutesRedistributeToOspf_Type()
)
f3VrfOspfRouterDhcpRoutesRedistributeToOspf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3VrfOspfRouterDhcpRoutesRedistributeToOspf.setStatus("current")
_F3VrfOspfRouterDhcpRoutesMetricType_Type = RoutesMetricType
_F3VrfOspfRouterDhcpRoutesMetricType_Object = MibTableColumn
f3VrfOspfRouterDhcpRoutesMetricType = _F3VrfOspfRouterDhcpRoutesMetricType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 17, 1, 17),
    _F3VrfOspfRouterDhcpRoutesMetricType_Type()
)
f3VrfOspfRouterDhcpRoutesMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3VrfOspfRouterDhcpRoutesMetricType.setStatus("current")
_F3VrfOspfRouterDhcpRoutesMetric_Type = Unsigned32
_F3VrfOspfRouterDhcpRoutesMetric_Object = MibTableColumn
f3VrfOspfRouterDhcpRoutesMetric = _F3VrfOspfRouterDhcpRoutesMetric_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 17, 1, 18),
    _F3VrfOspfRouterDhcpRoutesMetric_Type()
)
f3VrfOspfRouterDhcpRoutesMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3VrfOspfRouterDhcpRoutesMetric.setStatus("current")
_F3VrfOspfRouterIsAbr_Type = TruthValue
_F3VrfOspfRouterIsAbr_Object = MibTableColumn
f3VrfOspfRouterIsAbr = _F3VrfOspfRouterIsAbr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 17, 1, 19),
    _F3VrfOspfRouterIsAbr_Type()
)
f3VrfOspfRouterIsAbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3VrfOspfRouterIsAbr.setStatus("current")
_F3VrfOspfRouterIsAsbr_Type = TruthValue
_F3VrfOspfRouterIsAsbr_Object = MibTableColumn
f3VrfOspfRouterIsAsbr = _F3VrfOspfRouterIsAsbr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 17, 1, 20),
    _F3VrfOspfRouterIsAsbr_Type()
)
f3VrfOspfRouterIsAsbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3VrfOspfRouterIsAsbr.setStatus("current")
_F3VrfOspfRouterStorageType_Type = StorageType
_F3VrfOspfRouterStorageType_Object = MibTableColumn
f3VrfOspfRouterStorageType = _F3VrfOspfRouterStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 17, 1, 21),
    _F3VrfOspfRouterStorageType_Type()
)
f3VrfOspfRouterStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3VrfOspfRouterStorageType.setStatus("current")
_F3VrfOspfRouterRowStatus_Type = RowStatus
_F3VrfOspfRouterRowStatus_Object = MibTableColumn
f3VrfOspfRouterRowStatus = _F3VrfOspfRouterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 17, 1, 22),
    _F3VrfOspfRouterRowStatus_Type()
)
f3VrfOspfRouterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3VrfOspfRouterRowStatus.setStatus("current")
_F3VrfOspfRouterAction_Type = OspfRouterActionType
_F3VrfOspfRouterAction_Object = MibTableColumn
f3VrfOspfRouterAction = _F3VrfOspfRouterAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 17, 1, 23),
    _F3VrfOspfRouterAction_Type()
)
f3VrfOspfRouterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3VrfOspfRouterAction.setStatus("current")
_F3VrfOspfRouterVersion_Type = OspfVersion
_F3VrfOspfRouterVersion_Object = MibTableColumn
f3VrfOspfRouterVersion = _F3VrfOspfRouterVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 17, 1, 24),
    _F3VrfOspfRouterVersion_Type()
)
f3VrfOspfRouterVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3VrfOspfRouterVersion.setStatus("current")
_F3VrfOspfRouterAdministrativeDistance_Type = Unsigned32
_F3VrfOspfRouterAdministrativeDistance_Object = MibTableColumn
f3VrfOspfRouterAdministrativeDistance = _F3VrfOspfRouterAdministrativeDistance_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 17, 1, 25),
    _F3VrfOspfRouterAdministrativeDistance_Type()
)
f3VrfOspfRouterAdministrativeDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3VrfOspfRouterAdministrativeDistance.setStatus("current")
_F3VrfOspfRouterSlaacRoutesRedistributeToOspf_Type = TruthValue
_F3VrfOspfRouterSlaacRoutesRedistributeToOspf_Object = MibTableColumn
f3VrfOspfRouterSlaacRoutesRedistributeToOspf = _F3VrfOspfRouterSlaacRoutesRedistributeToOspf_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 17, 1, 26),
    _F3VrfOspfRouterSlaacRoutesRedistributeToOspf_Type()
)
f3VrfOspfRouterSlaacRoutesRedistributeToOspf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3VrfOspfRouterSlaacRoutesRedistributeToOspf.setStatus("current")
_F3VrfOspfRouterSlaacRoutesMetricType_Type = RoutesMetricType
_F3VrfOspfRouterSlaacRoutesMetricType_Object = MibTableColumn
f3VrfOspfRouterSlaacRoutesMetricType = _F3VrfOspfRouterSlaacRoutesMetricType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 17, 1, 27),
    _F3VrfOspfRouterSlaacRoutesMetricType_Type()
)
f3VrfOspfRouterSlaacRoutesMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3VrfOspfRouterSlaacRoutesMetricType.setStatus("current")
_F3VrfOspfRouterSlaacRoutesMetric_Type = Unsigned32
_F3VrfOspfRouterSlaacRoutesMetric_Object = MibTableColumn
f3VrfOspfRouterSlaacRoutesMetric = _F3VrfOspfRouterSlaacRoutesMetric_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 17, 1, 28),
    _F3VrfOspfRouterSlaacRoutesMetric_Type()
)
f3VrfOspfRouterSlaacRoutesMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3VrfOspfRouterSlaacRoutesMetric.setStatus("current")
_F3VrfOspfRouterEcmpMaximumPaths_Type = Unsigned32
_F3VrfOspfRouterEcmpMaximumPaths_Object = MibTableColumn
f3VrfOspfRouterEcmpMaximumPaths = _F3VrfOspfRouterEcmpMaximumPaths_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 17, 1, 29),
    _F3VrfOspfRouterEcmpMaximumPaths_Type()
)
f3VrfOspfRouterEcmpMaximumPaths.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3VrfOspfRouterEcmpMaximumPaths.setStatus("current")
_F3VrfOspfRouterSrControl_Type = TruthValue
_F3VrfOspfRouterSrControl_Object = MibTableColumn
f3VrfOspfRouterSrControl = _F3VrfOspfRouterSrControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 17, 1, 30),
    _F3VrfOspfRouterSrControl_Type()
)
f3VrfOspfRouterSrControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3VrfOspfRouterSrControl.setStatus("current")
_F3VrfOspfRouterConvergenceTime_Type = Unsigned32
_F3VrfOspfRouterConvergenceTime_Object = MibTableColumn
f3VrfOspfRouterConvergenceTime = _F3VrfOspfRouterConvergenceTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 17, 1, 31),
    _F3VrfOspfRouterConvergenceTime_Type()
)
f3VrfOspfRouterConvergenceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3VrfOspfRouterConvergenceTime.setStatus("current")
_F3L3TrafficOspfAreaTable_Object = MibTable
f3L3TrafficOspfAreaTable = _F3L3TrafficOspfAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 18)
)
if mibBuilder.loadTexts:
    f3L3TrafficOspfAreaTable.setStatus("current")
_F3L3TrafficOspfAreaEntry_Object = MibTableRow
f3L3TrafficOspfAreaEntry = _F3L3TrafficOspfAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 18, 1)
)
f3L3TrafficOspfAreaEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-L3-MIB", "f3VrfIndex"),
    (0, "F3-L3-MIB", "f3VrfOspfRouterIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficOspfAreaIndex"),
)
if mibBuilder.loadTexts:
    f3L3TrafficOspfAreaEntry.setStatus("current")
_F3L3TrafficOspfAreaIndex_Type = Unsigned32
_F3L3TrafficOspfAreaIndex_Object = MibTableColumn
f3L3TrafficOspfAreaIndex = _F3L3TrafficOspfAreaIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 18, 1, 1),
    _F3L3TrafficOspfAreaIndex_Type()
)
f3L3TrafficOspfAreaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3TrafficOspfAreaIndex.setStatus("current")
_F3L3TrafficOspfAreaType_Type = TrafficOspfAreaType
_F3L3TrafficOspfAreaType_Object = MibTableColumn
f3L3TrafficOspfAreaType = _F3L3TrafficOspfAreaType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 18, 1, 2),
    _F3L3TrafficOspfAreaType_Type()
)
f3L3TrafficOspfAreaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficOspfAreaType.setStatus("current")
_F3L3TrafficOspfAreaDefaultCost_Type = Unsigned32
_F3L3TrafficOspfAreaDefaultCost_Object = MibTableColumn
f3L3TrafficOspfAreaDefaultCost = _F3L3TrafficOspfAreaDefaultCost_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 18, 1, 3),
    _F3L3TrafficOspfAreaDefaultCost_Type()
)
f3L3TrafficOspfAreaDefaultCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficOspfAreaDefaultCost.setStatus("current")
_F3L3TrafficOspfAreaId_Type = IpAddress
_F3L3TrafficOspfAreaId_Object = MibTableColumn
f3L3TrafficOspfAreaId = _F3L3TrafficOspfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 18, 1, 4),
    _F3L3TrafficOspfAreaId_Type()
)
f3L3TrafficOspfAreaId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficOspfAreaId.setStatus("current")
_F3L3TrafficOspfAreaStorageType_Type = StorageType
_F3L3TrafficOspfAreaStorageType_Object = MibTableColumn
f3L3TrafficOspfAreaStorageType = _F3L3TrafficOspfAreaStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 18, 1, 5),
    _F3L3TrafficOspfAreaStorageType_Type()
)
f3L3TrafficOspfAreaStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficOspfAreaStorageType.setStatus("current")
_F3L3TrafficOspfAreaRowStatus_Type = RowStatus
_F3L3TrafficOspfAreaRowStatus_Object = MibTableColumn
f3L3TrafficOspfAreaRowStatus = _F3L3TrafficOspfAreaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 18, 1, 6),
    _F3L3TrafficOspfAreaRowStatus_Type()
)
f3L3TrafficOspfAreaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficOspfAreaRowStatus.setStatus("current")
_F3L3TrafficOspfAreaAuthType_Type = OspfAuthType
_F3L3TrafficOspfAreaAuthType_Object = MibTableColumn
f3L3TrafficOspfAreaAuthType = _F3L3TrafficOspfAreaAuthType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 18, 1, 7),
    _F3L3TrafficOspfAreaAuthType_Type()
)
f3L3TrafficOspfAreaAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficOspfAreaAuthType.setStatus("current")
_F3L3TrafficOspfAreaSimpleAuthKey_Type = DisplayString
_F3L3TrafficOspfAreaSimpleAuthKey_Object = MibTableColumn
f3L3TrafficOspfAreaSimpleAuthKey = _F3L3TrafficOspfAreaSimpleAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 18, 1, 8),
    _F3L3TrafficOspfAreaSimpleAuthKey_Type()
)
f3L3TrafficOspfAreaSimpleAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficOspfAreaSimpleAuthKey.setStatus("current")
_F3L3TrafficOspfAreaCryptoKeyId_Type = VariablePointer
_F3L3TrafficOspfAreaCryptoKeyId_Object = MibTableColumn
f3L3TrafficOspfAreaCryptoKeyId = _F3L3TrafficOspfAreaCryptoKeyId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 18, 1, 9),
    _F3L3TrafficOspfAreaCryptoKeyId_Type()
)
f3L3TrafficOspfAreaCryptoKeyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficOspfAreaCryptoKeyId.setStatus("current")
_F3L3TrafficOspfAreaIfMemberTable_Object = MibTable
f3L3TrafficOspfAreaIfMemberTable = _F3L3TrafficOspfAreaIfMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 19)
)
if mibBuilder.loadTexts:
    f3L3TrafficOspfAreaIfMemberTable.setStatus("current")
_F3L3TrafficOspfAreaIfMemberEntry_Object = MibTableRow
f3L3TrafficOspfAreaIfMemberEntry = _F3L3TrafficOspfAreaIfMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 19, 1)
)
f3L3TrafficOspfAreaIfMemberEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-L3-MIB", "f3VrfIndex"),
    (0, "F3-L3-MIB", "f3VrfOspfRouterIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficOspfAreaIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficOspfAreaIfMemberObject"),
)
if mibBuilder.loadTexts:
    f3L3TrafficOspfAreaIfMemberEntry.setStatus("current")
_F3L3TrafficOspfAreaIfMemberObject_Type = VariablePointer
_F3L3TrafficOspfAreaIfMemberObject_Object = MibTableColumn
f3L3TrafficOspfAreaIfMemberObject = _F3L3TrafficOspfAreaIfMemberObject_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 19, 1, 1),
    _F3L3TrafficOspfAreaIfMemberObject_Type()
)
f3L3TrafficOspfAreaIfMemberObject.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3TrafficOspfAreaIfMemberObject.setStatus("current")
_F3L3TrafficOspfAreaIfMemberStorageType_Type = StorageType
_F3L3TrafficOspfAreaIfMemberStorageType_Object = MibTableColumn
f3L3TrafficOspfAreaIfMemberStorageType = _F3L3TrafficOspfAreaIfMemberStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 19, 1, 2),
    _F3L3TrafficOspfAreaIfMemberStorageType_Type()
)
f3L3TrafficOspfAreaIfMemberStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficOspfAreaIfMemberStorageType.setStatus("current")
_F3L3TrafficOspfAreaIfMemberRowStatus_Type = RowStatus
_F3L3TrafficOspfAreaIfMemberRowStatus_Object = MibTableColumn
f3L3TrafficOspfAreaIfMemberRowStatus = _F3L3TrafficOspfAreaIfMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 19, 1, 3),
    _F3L3TrafficOspfAreaIfMemberRowStatus_Type()
)
f3L3TrafficOspfAreaIfMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficOspfAreaIfMemberRowStatus.setStatus("current")
_F3VrfLoopbackInterfaceTable_Object = MibTable
f3VrfLoopbackInterfaceTable = _F3VrfLoopbackInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 20)
)
if mibBuilder.loadTexts:
    f3VrfLoopbackInterfaceTable.setStatus("current")
_F3VrfLoopbackInterfaceEntry_Object = MibTableRow
f3VrfLoopbackInterfaceEntry = _F3VrfLoopbackInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 20, 1)
)
f3VrfLoopbackInterfaceEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-L3-MIB", "f3VrfIndex"),
    (0, "F3-L3-MIB", "f3VrfLoopbackInterfaceIndex"),
)
if mibBuilder.loadTexts:
    f3VrfLoopbackInterfaceEntry.setStatus("current")
_F3VrfLoopbackInterfaceIndex_Type = Unsigned32
_F3VrfLoopbackInterfaceIndex_Object = MibTableColumn
f3VrfLoopbackInterfaceIndex = _F3VrfLoopbackInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 20, 1, 1),
    _F3VrfLoopbackInterfaceIndex_Type()
)
f3VrfLoopbackInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3VrfLoopbackInterfaceIndex.setStatus("current")


class _F3VrfLoopbackInterfaceName_Type(DisplayString):
    """Custom type f3VrfLoopbackInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_F3VrfLoopbackInterfaceName_Type.__name__ = "DisplayString"
_F3VrfLoopbackInterfaceName_Object = MibTableColumn
f3VrfLoopbackInterfaceName = _F3VrfLoopbackInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 20, 1, 2),
    _F3VrfLoopbackInterfaceName_Type()
)
f3VrfLoopbackInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3VrfLoopbackInterfaceName.setStatus("current")
_F3VrfLoopbackInterfaceIpAddress_Type = IpAddress
_F3VrfLoopbackInterfaceIpAddress_Object = MibTableColumn
f3VrfLoopbackInterfaceIpAddress = _F3VrfLoopbackInterfaceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 20, 1, 3),
    _F3VrfLoopbackInterfaceIpAddress_Type()
)
f3VrfLoopbackInterfaceIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3VrfLoopbackInterfaceIpAddress.setStatus("current")
_F3VrfLoopbackInterfaceNetMask_Type = IpAddress
_F3VrfLoopbackInterfaceNetMask_Object = MibTableColumn
f3VrfLoopbackInterfaceNetMask = _F3VrfLoopbackInterfaceNetMask_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 20, 1, 4),
    _F3VrfLoopbackInterfaceNetMask_Type()
)
f3VrfLoopbackInterfaceNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3VrfLoopbackInterfaceNetMask.setStatus("current")
_F3VrfLoopbackInterfaceCIRLo_Type = Unsigned32
_F3VrfLoopbackInterfaceCIRLo_Object = MibTableColumn
f3VrfLoopbackInterfaceCIRLo = _F3VrfLoopbackInterfaceCIRLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 20, 1, 5),
    _F3VrfLoopbackInterfaceCIRLo_Type()
)
f3VrfLoopbackInterfaceCIRLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3VrfLoopbackInterfaceCIRLo.setStatus("current")
_F3VrfLoopbackInterfaceCIRHi_Type = Unsigned32
_F3VrfLoopbackInterfaceCIRHi_Object = MibTableColumn
f3VrfLoopbackInterfaceCIRHi = _F3VrfLoopbackInterfaceCIRHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 20, 1, 6),
    _F3VrfLoopbackInterfaceCIRHi_Type()
)
f3VrfLoopbackInterfaceCIRHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3VrfLoopbackInterfaceCIRHi.setStatus("current")
_F3VrfLoopbackInterfaceStorageType_Type = StorageType
_F3VrfLoopbackInterfaceStorageType_Object = MibTableColumn
f3VrfLoopbackInterfaceStorageType = _F3VrfLoopbackInterfaceStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 20, 1, 7),
    _F3VrfLoopbackInterfaceStorageType_Type()
)
f3VrfLoopbackInterfaceStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3VrfLoopbackInterfaceStorageType.setStatus("current")
_F3VrfLoopbackInterfaceRowStatus_Type = RowStatus
_F3VrfLoopbackInterfaceRowStatus_Object = MibTableColumn
f3VrfLoopbackInterfaceRowStatus = _F3VrfLoopbackInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 20, 1, 8),
    _F3VrfLoopbackInterfaceRowStatus_Type()
)
f3VrfLoopbackInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3VrfLoopbackInterfaceRowStatus.setStatus("current")
_F3VrfLoopbackInterfaceIpMode_Type = IpMode
_F3VrfLoopbackInterfaceIpMode_Object = MibTableColumn
f3VrfLoopbackInterfaceIpMode = _F3VrfLoopbackInterfaceIpMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 20, 1, 9),
    _F3VrfLoopbackInterfaceIpMode_Type()
)
f3VrfLoopbackInterfaceIpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3VrfLoopbackInterfaceIpMode.setStatus("current")
_F3VrfLoopbackInterfaceIpv6Address_Type = Ipv6Address
_F3VrfLoopbackInterfaceIpv6Address_Object = MibTableColumn
f3VrfLoopbackInterfaceIpv6Address = _F3VrfLoopbackInterfaceIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 20, 1, 10),
    _F3VrfLoopbackInterfaceIpv6Address_Type()
)
f3VrfLoopbackInterfaceIpv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3VrfLoopbackInterfaceIpv6Address.setStatus("current")
_F3VrfLoopbackInterfaceIpv6AddrPrefixLen_Type = Integer32
_F3VrfLoopbackInterfaceIpv6AddrPrefixLen_Object = MibTableColumn
f3VrfLoopbackInterfaceIpv6AddrPrefixLen = _F3VrfLoopbackInterfaceIpv6AddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 20, 1, 11),
    _F3VrfLoopbackInterfaceIpv6AddrPrefixLen_Type()
)
f3VrfLoopbackInterfaceIpv6AddrPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3VrfLoopbackInterfaceIpv6AddrPrefixLen.setStatus("current")
_F3L3TrafficOspfAsLsDbTable_Object = MibTable
f3L3TrafficOspfAsLsDbTable = _F3L3TrafficOspfAsLsDbTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 21)
)
if mibBuilder.loadTexts:
    f3L3TrafficOspfAsLsDbTable.setStatus("current")
_F3L3TrafficOspfAsLsDbEntry_Object = MibTableRow
f3L3TrafficOspfAsLsDbEntry = _F3L3TrafficOspfAsLsDbEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 21, 1)
)
f3L3TrafficOspfAsLsDbEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-L3-MIB", "f3VrfIndex"),
    (0, "F3-L3-MIB", "f3VrfOspfRouterIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficOspfAsLsDbType"),
    (0, "F3-L3-MIB", "f3L3TrafficOspfAsLsDbId"),
    (0, "F3-L3-MIB", "f3L3TrafficOspfAsLsDbRouterId"),
)
if mibBuilder.loadTexts:
    f3L3TrafficOspfAsLsDbEntry.setStatus("current")
_F3L3TrafficOspfAsLsDbType_Type = OspfAsLsaType
_F3L3TrafficOspfAsLsDbType_Object = MibTableColumn
f3L3TrafficOspfAsLsDbType = _F3L3TrafficOspfAsLsDbType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 21, 1, 1),
    _F3L3TrafficOspfAsLsDbType_Type()
)
f3L3TrafficOspfAsLsDbType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3TrafficOspfAsLsDbType.setStatus("current")
_F3L3TrafficOspfAsLsDbId_Type = IpAddress
_F3L3TrafficOspfAsLsDbId_Object = MibTableColumn
f3L3TrafficOspfAsLsDbId = _F3L3TrafficOspfAsLsDbId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 21, 1, 2),
    _F3L3TrafficOspfAsLsDbId_Type()
)
f3L3TrafficOspfAsLsDbId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3TrafficOspfAsLsDbId.setStatus("current")
_F3L3TrafficOspfAsLsDbRouterId_Type = IpAddress
_F3L3TrafficOspfAsLsDbRouterId_Object = MibTableColumn
f3L3TrafficOspfAsLsDbRouterId = _F3L3TrafficOspfAsLsDbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 21, 1, 3),
    _F3L3TrafficOspfAsLsDbRouterId_Type()
)
f3L3TrafficOspfAsLsDbRouterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3TrafficOspfAsLsDbRouterId.setStatus("current")
_F3L3TrafficOspfAsLsDbChecksum_Type = Unsigned32
_F3L3TrafficOspfAsLsDbChecksum_Object = MibTableColumn
f3L3TrafficOspfAsLsDbChecksum = _F3L3TrafficOspfAsLsDbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 21, 1, 4),
    _F3L3TrafficOspfAsLsDbChecksum_Type()
)
f3L3TrafficOspfAsLsDbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficOspfAsLsDbChecksum.setStatus("current")
_F3L3TrafficOspfAsLsDbSeqNum_Type = Unsigned32
_F3L3TrafficOspfAsLsDbSeqNum_Object = MibTableColumn
f3L3TrafficOspfAsLsDbSeqNum = _F3L3TrafficOspfAsLsDbSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 21, 1, 5),
    _F3L3TrafficOspfAsLsDbSeqNum_Type()
)
f3L3TrafficOspfAsLsDbSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficOspfAsLsDbSeqNum.setStatus("current")
_F3L3TrafficOspfAsLsDbAge_Type = Unsigned32
_F3L3TrafficOspfAsLsDbAge_Object = MibTableColumn
f3L3TrafficOspfAsLsDbAge = _F3L3TrafficOspfAsLsDbAge_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 21, 1, 6),
    _F3L3TrafficOspfAsLsDbAge_Type()
)
f3L3TrafficOspfAsLsDbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficOspfAsLsDbAge.setStatus("current")
_F3L3TrafficOspfLsDbTable_Object = MibTable
f3L3TrafficOspfLsDbTable = _F3L3TrafficOspfLsDbTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 22)
)
if mibBuilder.loadTexts:
    f3L3TrafficOspfLsDbTable.setStatus("current")
_F3L3TrafficOspfLsDbEntry_Object = MibTableRow
f3L3TrafficOspfLsDbEntry = _F3L3TrafficOspfLsDbEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 22, 1)
)
f3L3TrafficOspfLsDbEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-L3-MIB", "f3VrfIndex"),
    (0, "F3-L3-MIB", "f3VrfOspfRouterIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficOspfLsDbType"),
    (0, "F3-L3-MIB", "f3L3TrafficOspfLsDbId"),
    (0, "F3-L3-MIB", "f3L3TrafficOspfLsDbRouterId"),
    (0, "F3-L3-MIB", "f3L3TrafficOspfLsDbAreaId"),
)
if mibBuilder.loadTexts:
    f3L3TrafficOspfLsDbEntry.setStatus("current")
_F3L3TrafficOspfLsDbType_Type = OspfLsaType
_F3L3TrafficOspfLsDbType_Object = MibTableColumn
f3L3TrafficOspfLsDbType = _F3L3TrafficOspfLsDbType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 22, 1, 1),
    _F3L3TrafficOspfLsDbType_Type()
)
f3L3TrafficOspfLsDbType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3TrafficOspfLsDbType.setStatus("current")
_F3L3TrafficOspfLsDbId_Type = IpAddress
_F3L3TrafficOspfLsDbId_Object = MibTableColumn
f3L3TrafficOspfLsDbId = _F3L3TrafficOspfLsDbId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 22, 1, 2),
    _F3L3TrafficOspfLsDbId_Type()
)
f3L3TrafficOspfLsDbId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3TrafficOspfLsDbId.setStatus("current")
_F3L3TrafficOspfLsDbRouterId_Type = IpAddress
_F3L3TrafficOspfLsDbRouterId_Object = MibTableColumn
f3L3TrafficOspfLsDbRouterId = _F3L3TrafficOspfLsDbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 22, 1, 3),
    _F3L3TrafficOspfLsDbRouterId_Type()
)
f3L3TrafficOspfLsDbRouterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3TrafficOspfLsDbRouterId.setStatus("current")
_F3L3TrafficOspfLsDbAreaId_Type = IpAddress
_F3L3TrafficOspfLsDbAreaId_Object = MibTableColumn
f3L3TrafficOspfLsDbAreaId = _F3L3TrafficOspfLsDbAreaId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 22, 1, 4),
    _F3L3TrafficOspfLsDbAreaId_Type()
)
f3L3TrafficOspfLsDbAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3TrafficOspfLsDbAreaId.setStatus("current")
_F3L3TrafficOspfLsDbChecksum_Type = Unsigned32
_F3L3TrafficOspfLsDbChecksum_Object = MibTableColumn
f3L3TrafficOspfLsDbChecksum = _F3L3TrafficOspfLsDbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 22, 1, 5),
    _F3L3TrafficOspfLsDbChecksum_Type()
)
f3L3TrafficOspfLsDbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficOspfLsDbChecksum.setStatus("current")
_F3L3TrafficOspfLsDbSeqNum_Type = Unsigned32
_F3L3TrafficOspfLsDbSeqNum_Object = MibTableColumn
f3L3TrafficOspfLsDbSeqNum = _F3L3TrafficOspfLsDbSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 22, 1, 6),
    _F3L3TrafficOspfLsDbSeqNum_Type()
)
f3L3TrafficOspfLsDbSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficOspfLsDbSeqNum.setStatus("current")
_F3L3TrafficOspfLsDbAge_Type = Unsigned32
_F3L3TrafficOspfLsDbAge_Object = MibTableColumn
f3L3TrafficOspfLsDbAge = _F3L3TrafficOspfLsDbAge_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 22, 1, 7),
    _F3L3TrafficOspfLsDbAge_Type()
)
f3L3TrafficOspfLsDbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficOspfLsDbAge.setStatus("current")
_F3L3TrafficOspfNeighborTable_Object = MibTable
f3L3TrafficOspfNeighborTable = _F3L3TrafficOspfNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 23)
)
if mibBuilder.loadTexts:
    f3L3TrafficOspfNeighborTable.setStatus("current")
_F3L3TrafficOspfNeighborEntry_Object = MibTableRow
f3L3TrafficOspfNeighborEntry = _F3L3TrafficOspfNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 23, 1)
)
f3L3TrafficOspfNeighborEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-L3-MIB", "f3VrfIndex"),
    (0, "F3-L3-MIB", "f3VrfOspfRouterIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficOspfNeighborIpAddress"),
)
if mibBuilder.loadTexts:
    f3L3TrafficOspfNeighborEntry.setStatus("current")
_F3L3TrafficOspfNeighborIpAddress_Type = IpAddress
_F3L3TrafficOspfNeighborIpAddress_Object = MibTableColumn
f3L3TrafficOspfNeighborIpAddress = _F3L3TrafficOspfNeighborIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 23, 1, 1),
    _F3L3TrafficOspfNeighborIpAddress_Type()
)
f3L3TrafficOspfNeighborIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3TrafficOspfNeighborIpAddress.setStatus("current")
_F3L3TrafficOspfNeighborInterface_Type = VariablePointer
_F3L3TrafficOspfNeighborInterface_Object = MibTableColumn
f3L3TrafficOspfNeighborInterface = _F3L3TrafficOspfNeighborInterface_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 23, 1, 2),
    _F3L3TrafficOspfNeighborInterface_Type()
)
f3L3TrafficOspfNeighborInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficOspfNeighborInterface.setStatus("deprecated")
_F3L3TrafficOspfNeighborRouterId_Type = IpAddress
_F3L3TrafficOspfNeighborRouterId_Object = MibTableColumn
f3L3TrafficOspfNeighborRouterId = _F3L3TrafficOspfNeighborRouterId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 23, 1, 3),
    _F3L3TrafficOspfNeighborRouterId_Type()
)
f3L3TrafficOspfNeighborRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficOspfNeighborRouterId.setStatus("current")
_F3L3TrafficOspfNeighborState_Type = OspfAdjacencyState
_F3L3TrafficOspfNeighborState_Object = MibTableColumn
f3L3TrafficOspfNeighborState = _F3L3TrafficOspfNeighborState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 23, 1, 4),
    _F3L3TrafficOspfNeighborState_Type()
)
f3L3TrafficOspfNeighborState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficOspfNeighborState.setStatus("current")
_F3L3TrafficOspfNeighborRole_Type = TrafficOspfRole
_F3L3TrafficOspfNeighborRole_Object = MibTableColumn
f3L3TrafficOspfNeighborRole = _F3L3TrafficOspfNeighborRole_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 23, 1, 5),
    _F3L3TrafficOspfNeighborRole_Type()
)
f3L3TrafficOspfNeighborRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficOspfNeighborRole.setStatus("current")
_F3L3TrafficOspfNeighborPriority_Type = Unsigned32
_F3L3TrafficOspfNeighborPriority_Object = MibTableColumn
f3L3TrafficOspfNeighborPriority = _F3L3TrafficOspfNeighborPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 23, 1, 6),
    _F3L3TrafficOspfNeighborPriority_Type()
)
f3L3TrafficOspfNeighborPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficOspfNeighborPriority.setStatus("current")
_F3L3TrafficOspfNeighborDeadTime_Type = Unsigned32
_F3L3TrafficOspfNeighborDeadTime_Object = MibTableColumn
f3L3TrafficOspfNeighborDeadTime = _F3L3TrafficOspfNeighborDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 23, 1, 7),
    _F3L3TrafficOspfNeighborDeadTime_Type()
)
f3L3TrafficOspfNeighborDeadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficOspfNeighborDeadTime.setStatus("current")
_F3L3TrafficOspfNeighborLocalInterfaceName_Type = DisplayString
_F3L3TrafficOspfNeighborLocalInterfaceName_Object = MibTableColumn
f3L3TrafficOspfNeighborLocalInterfaceName = _F3L3TrafficOspfNeighborLocalInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 23, 1, 8),
    _F3L3TrafficOspfNeighborLocalInterfaceName_Type()
)
f3L3TrafficOspfNeighborLocalInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficOspfNeighborLocalInterfaceName.setStatus("current")
_F3L3TrafficIPInterfaceOspfTable_Object = MibTable
f3L3TrafficIPInterfaceOspfTable = _F3L3TrafficIPInterfaceOspfTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 25)
)
if mibBuilder.loadTexts:
    f3L3TrafficIPInterfaceOspfTable.setStatus("current")
_F3L3TrafficIPInterfaceOspfEntry_Object = MibTableRow
f3L3TrafficIPInterfaceOspfEntry = _F3L3TrafficIPInterfaceOspfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 25, 1)
)
if mibBuilder.loadTexts:
    f3L3TrafficIPInterfaceOspfEntry.setStatus("current")
_F3L3TrafficIPIfOspfAreaId_Type = IpAddress
_F3L3TrafficIPIfOspfAreaId_Object = MibTableColumn
f3L3TrafficIPIfOspfAreaId = _F3L3TrafficIPIfOspfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 25, 1, 1),
    _F3L3TrafficIPIfOspfAreaId_Type()
)
f3L3TrafficIPIfOspfAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfOspfAreaId.setStatus("current")
_F3L3TrafficIPIfOspfCost_Type = Unsigned32
_F3L3TrafficIPIfOspfCost_Object = MibTableColumn
f3L3TrafficIPIfOspfCost = _F3L3TrafficIPIfOspfCost_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 25, 1, 2),
    _F3L3TrafficIPIfOspfCost_Type()
)
f3L3TrafficIPIfOspfCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfOspfCost.setStatus("current")
_F3L3TrafficIPIfOspfIfType_Type = OspfIfType
_F3L3TrafficIPIfOspfIfType_Object = MibTableColumn
f3L3TrafficIPIfOspfIfType = _F3L3TrafficIPIfOspfIfType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 25, 1, 3),
    _F3L3TrafficIPIfOspfIfType_Type()
)
f3L3TrafficIPIfOspfIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfOspfIfType.setStatus("current")
_F3L3TrafficIPIfOspfRtrPriority_Type = Unsigned32
_F3L3TrafficIPIfOspfRtrPriority_Object = MibTableColumn
f3L3TrafficIPIfOspfRtrPriority = _F3L3TrafficIPIfOspfRtrPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 25, 1, 4),
    _F3L3TrafficIPIfOspfRtrPriority_Type()
)
f3L3TrafficIPIfOspfRtrPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfOspfRtrPriority.setStatus("current")
_F3L3TrafficIPIfOspfHelloInterval_Type = Unsigned32
_F3L3TrafficIPIfOspfHelloInterval_Object = MibTableColumn
f3L3TrafficIPIfOspfHelloInterval = _F3L3TrafficIPIfOspfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 25, 1, 5),
    _F3L3TrafficIPIfOspfHelloInterval_Type()
)
f3L3TrafficIPIfOspfHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfOspfHelloInterval.setStatus("current")
_F3L3TrafficIPIfOspfDeadInterval_Type = Unsigned32
_F3L3TrafficIPIfOspfDeadInterval_Object = MibTableColumn
f3L3TrafficIPIfOspfDeadInterval = _F3L3TrafficIPIfOspfDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 25, 1, 6),
    _F3L3TrafficIPIfOspfDeadInterval_Type()
)
f3L3TrafficIPIfOspfDeadInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfOspfDeadInterval.setStatus("current")
_F3L3TrafficIPIfOspfTransmitDelay_Type = Unsigned32
_F3L3TrafficIPIfOspfTransmitDelay_Object = MibTableColumn
f3L3TrafficIPIfOspfTransmitDelay = _F3L3TrafficIPIfOspfTransmitDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 25, 1, 7),
    _F3L3TrafficIPIfOspfTransmitDelay_Type()
)
f3L3TrafficIPIfOspfTransmitDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfOspfTransmitDelay.setStatus("current")
_F3L3TrafficIPIfOspfRetransmitInterval_Type = Unsigned32
_F3L3TrafficIPIfOspfRetransmitInterval_Object = MibTableColumn
f3L3TrafficIPIfOspfRetransmitInterval = _F3L3TrafficIPIfOspfRetransmitInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 25, 1, 8),
    _F3L3TrafficIPIfOspfRetransmitInterval_Type()
)
f3L3TrafficIPIfOspfRetransmitInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfOspfRetransmitInterval.setStatus("current")
_F3L3TrafficIPIfOspfState_Type = OspfInterfaceState
_F3L3TrafficIPIfOspfState_Object = MibTableColumn
f3L3TrafficIPIfOspfState = _F3L3TrafficIPIfOspfState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 25, 1, 9),
    _F3L3TrafficIPIfOspfState_Type()
)
f3L3TrafficIPIfOspfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfOspfState.setStatus("current")
_F3L3TrafficIPIfOspfDesignatedRouterId_Type = IpAddress
_F3L3TrafficIPIfOspfDesignatedRouterId_Object = MibTableColumn
f3L3TrafficIPIfOspfDesignatedRouterId = _F3L3TrafficIPIfOspfDesignatedRouterId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 25, 1, 10),
    _F3L3TrafficIPIfOspfDesignatedRouterId_Type()
)
f3L3TrafficIPIfOspfDesignatedRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfOspfDesignatedRouterId.setStatus("current")
_F3L3TrafficIPIfOspfBackupDesignatedRouterId_Type = IpAddress
_F3L3TrafficIPIfOspfBackupDesignatedRouterId_Object = MibTableColumn
f3L3TrafficIPIfOspfBackupDesignatedRouterId = _F3L3TrafficIPIfOspfBackupDesignatedRouterId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 25, 1, 11),
    _F3L3TrafficIPIfOspfBackupDesignatedRouterId_Type()
)
f3L3TrafficIPIfOspfBackupDesignatedRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfOspfBackupDesignatedRouterId.setStatus("current")
_F3L3TrafficIPIfOspfAuthType_Type = OspfAuthType
_F3L3TrafficIPIfOspfAuthType_Object = MibTableColumn
f3L3TrafficIPIfOspfAuthType = _F3L3TrafficIPIfOspfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 25, 1, 12),
    _F3L3TrafficIPIfOspfAuthType_Type()
)
f3L3TrafficIPIfOspfAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfOspfAuthType.setStatus("current")
_F3L3TrafficIPIfOspfSimpleAuthKey_Type = DisplayString
_F3L3TrafficIPIfOspfSimpleAuthKey_Object = MibTableColumn
f3L3TrafficIPIfOspfSimpleAuthKey = _F3L3TrafficIPIfOspfSimpleAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 25, 1, 13),
    _F3L3TrafficIPIfOspfSimpleAuthKey_Type()
)
f3L3TrafficIPIfOspfSimpleAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfOspfSimpleAuthKey.setStatus("current")
_F3L3TrafficIPIfospfCryptoKeyId_Type = VariablePointer
_F3L3TrafficIPIfospfCryptoKeyId_Object = MibTableColumn
f3L3TrafficIPIfospfCryptoKeyId = _F3L3TrafficIPIfospfCryptoKeyId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 25, 1, 14),
    _F3L3TrafficIPIfospfCryptoKeyId_Type()
)
f3L3TrafficIPIfospfCryptoKeyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPIfospfCryptoKeyId.setStatus("current")
_F3L3TrafficIPv6InterfaceTable_Object = MibTable
f3L3TrafficIPv6InterfaceTable = _F3L3TrafficIPv6InterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 26)
)
if mibBuilder.loadTexts:
    f3L3TrafficIPv6InterfaceTable.setStatus("current")
_F3L3TrafficIPv6InterfaceEntry_Object = MibTableRow
f3L3TrafficIPv6InterfaceEntry = _F3L3TrafficIPv6InterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 26, 1)
)
f3L3TrafficIPv6InterfaceEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficIPv6IfIndex"),
)
if mibBuilder.loadTexts:
    f3L3TrafficIPv6InterfaceEntry.setStatus("current")
_F3L3TrafficIPv6IfIndex_Type = Integer32
_F3L3TrafficIPv6IfIndex_Object = MibTableColumn
f3L3TrafficIPv6IfIndex = _F3L3TrafficIPv6IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 26, 1, 1),
    _F3L3TrafficIPv6IfIndex_Type()
)
f3L3TrafficIPv6IfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6IfIndex.setStatus("current")


class _F3L3TrafficIPv6IfName_Type(DisplayString):
    """Custom type f3L3TrafficIPv6IfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_F3L3TrafficIPv6IfName_Type.__name__ = "DisplayString"
_F3L3TrafficIPv6IfName_Object = MibTableColumn
f3L3TrafficIPv6IfName = _F3L3TrafficIPv6IfName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 26, 1, 2),
    _F3L3TrafficIPv6IfName_Type()
)
f3L3TrafficIPv6IfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6IfName.setStatus("current")
_F3L3TrafficIPv6IfAdminState_Type = AdminState
_F3L3TrafficIPv6IfAdminState_Object = MibTableColumn
f3L3TrafficIPv6IfAdminState = _F3L3TrafficIPv6IfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 26, 1, 3),
    _F3L3TrafficIPv6IfAdminState_Type()
)
f3L3TrafficIPv6IfAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6IfAdminState.setStatus("current")
_F3L3TrafficIPv6IfSecondaryState_Type = SecondaryState
_F3L3TrafficIPv6IfSecondaryState_Object = MibTableColumn
f3L3TrafficIPv6IfSecondaryState = _F3L3TrafficIPv6IfSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 26, 1, 4),
    _F3L3TrafficIPv6IfSecondaryState_Type()
)
f3L3TrafficIPv6IfSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6IfSecondaryState.setStatus("current")
_F3L3TrafficIPv6IfOperationalState_Type = OperationalState
_F3L3TrafficIPv6IfOperationalState_Object = MibTableColumn
f3L3TrafficIPv6IfOperationalState = _F3L3TrafficIPv6IfOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 26, 1, 5),
    _F3L3TrafficIPv6IfOperationalState_Type()
)
f3L3TrafficIPv6IfOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6IfOperationalState.setStatus("current")
_F3L3TrafficIPv6IfType_Type = IpInterfaceType
_F3L3TrafficIPv6IfType_Object = MibTableColumn
f3L3TrafficIPv6IfType = _F3L3TrafficIPv6IfType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 26, 1, 6),
    _F3L3TrafficIPv6IfType_Type()
)
f3L3TrafficIPv6IfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6IfType.setStatus("current")
_F3L3TrafficIPv6IfLinkLocalAddr_Type = Ipv6Address
_F3L3TrafficIPv6IfLinkLocalAddr_Object = MibTableColumn
f3L3TrafficIPv6IfLinkLocalAddr = _F3L3TrafficIPv6IfLinkLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 26, 1, 7),
    _F3L3TrafficIPv6IfLinkLocalAddr_Type()
)
f3L3TrafficIPv6IfLinkLocalAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6IfLinkLocalAddr.setStatus("current")
_F3L3TrafficIPv6IfLinkLocalAddrMode_Type = Ipv6LinkLocalAddressMode
_F3L3TrafficIPv6IfLinkLocalAddrMode_Object = MibTableColumn
f3L3TrafficIPv6IfLinkLocalAddrMode = _F3L3TrafficIPv6IfLinkLocalAddrMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 26, 1, 8),
    _F3L3TrafficIPv6IfLinkLocalAddrMode_Type()
)
f3L3TrafficIPv6IfLinkLocalAddrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6IfLinkLocalAddrMode.setStatus("current")
_F3L3TrafficIPv6IfMtu_Type = Integer32
_F3L3TrafficIPv6IfMtu_Object = MibTableColumn
f3L3TrafficIPv6IfMtu = _F3L3TrafficIPv6IfMtu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 26, 1, 9),
    _F3L3TrafficIPv6IfMtu_Type()
)
f3L3TrafficIPv6IfMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6IfMtu.setStatus("current")
_F3L3TrafficIPv6IfStatelessAddrAutoconfigEnabled_Type = TruthValue
_F3L3TrafficIPv6IfStatelessAddrAutoconfigEnabled_Object = MibTableColumn
f3L3TrafficIPv6IfStatelessAddrAutoconfigEnabled = _F3L3TrafficIPv6IfStatelessAddrAutoconfigEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 26, 1, 10),
    _F3L3TrafficIPv6IfStatelessAddrAutoconfigEnabled_Type()
)
f3L3TrafficIPv6IfStatelessAddrAutoconfigEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6IfStatelessAddrAutoconfigEnabled.setStatus("current")
_F3L3TrafficIPv6IfDefaultGateway_Type = Ipv6Address
_F3L3TrafficIPv6IfDefaultGateway_Object = MibTableColumn
f3L3TrafficIPv6IfDefaultGateway = _F3L3TrafficIPv6IfDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 26, 1, 11),
    _F3L3TrafficIPv6IfDefaultGateway_Type()
)
f3L3TrafficIPv6IfDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6IfDefaultGateway.setStatus("current")
_F3L3TrafficIPv6IfIcmpErrorMsgRateLimit_Type = Integer32
_F3L3TrafficIPv6IfIcmpErrorMsgRateLimit_Object = MibTableColumn
f3L3TrafficIPv6IfIcmpErrorMsgRateLimit = _F3L3TrafficIPv6IfIcmpErrorMsgRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 26, 1, 12),
    _F3L3TrafficIPv6IfIcmpErrorMsgRateLimit_Type()
)
f3L3TrafficIPv6IfIcmpErrorMsgRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6IfIcmpErrorMsgRateLimit.setStatus("current")
_F3L3TrafficIPv6IfDhcpRole_Type = CmDhcpRole
_F3L3TrafficIPv6IfDhcpRole_Object = MibTableColumn
f3L3TrafficIPv6IfDhcpRole = _F3L3TrafficIPv6IfDhcpRole_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 26, 1, 13),
    _F3L3TrafficIPv6IfDhcpRole_Type()
)
f3L3TrafficIPv6IfDhcpRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6IfDhcpRole.setStatus("current")
_F3L3TrafficIPv6IfDhcpEnabled_Type = TruthValue
_F3L3TrafficIPv6IfDhcpEnabled_Object = MibTableColumn
f3L3TrafficIPv6IfDhcpEnabled = _F3L3TrafficIPv6IfDhcpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 26, 1, 14),
    _F3L3TrafficIPv6IfDhcpEnabled_Type()
)
f3L3TrafficIPv6IfDhcpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6IfDhcpEnabled.setStatus("current")
_F3L3TrafficIPv6IfDhcpRapidCommitControlEnabled_Type = TruthValue
_F3L3TrafficIPv6IfDhcpRapidCommitControlEnabled_Object = MibTableColumn
f3L3TrafficIPv6IfDhcpRapidCommitControlEnabled = _F3L3TrafficIPv6IfDhcpRapidCommitControlEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 26, 1, 15),
    _F3L3TrafficIPv6IfDhcpRapidCommitControlEnabled_Type()
)
f3L3TrafficIPv6IfDhcpRapidCommitControlEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6IfDhcpRapidCommitControlEnabled.setStatus("current")
_F3L3TrafficIPv6IfMaxRAInterval_Type = Unsigned32
_F3L3TrafficIPv6IfMaxRAInterval_Object = MibTableColumn
f3L3TrafficIPv6IfMaxRAInterval = _F3L3TrafficIPv6IfMaxRAInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 26, 1, 16),
    _F3L3TrafficIPv6IfMaxRAInterval_Type()
)
f3L3TrafficIPv6IfMaxRAInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6IfMaxRAInterval.setStatus("current")
_F3L3TrafficIPv6IfMinRAInterval_Type = Unsigned32
_F3L3TrafficIPv6IfMinRAInterval_Object = MibTableColumn
f3L3TrafficIPv6IfMinRAInterval = _F3L3TrafficIPv6IfMinRAInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 26, 1, 17),
    _F3L3TrafficIPv6IfMinRAInterval_Type()
)
f3L3TrafficIPv6IfMinRAInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6IfMinRAInterval.setStatus("current")
_F3L3TrafficIPv6IfRouterLifeTime_Type = Unsigned32
_F3L3TrafficIPv6IfRouterLifeTime_Object = MibTableColumn
f3L3TrafficIPv6IfRouterLifeTime = _F3L3TrafficIPv6IfRouterLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 26, 1, 18),
    _F3L3TrafficIPv6IfRouterLifeTime_Type()
)
f3L3TrafficIPv6IfRouterLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6IfRouterLifeTime.setStatus("current")
_F3L3TrafficIPv6IfReachableTime_Type = Unsigned32
_F3L3TrafficIPv6IfReachableTime_Object = MibTableColumn
f3L3TrafficIPv6IfReachableTime = _F3L3TrafficIPv6IfReachableTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 26, 1, 19),
    _F3L3TrafficIPv6IfReachableTime_Type()
)
f3L3TrafficIPv6IfReachableTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6IfReachableTime.setStatus("current")
_F3L3TrafficIPv6IfRaDhcpMoreConfigEnabled_Type = TruthValue
_F3L3TrafficIPv6IfRaDhcpMoreConfigEnabled_Object = MibTableColumn
f3L3TrafficIPv6IfRaDhcpMoreConfigEnabled = _F3L3TrafficIPv6IfRaDhcpMoreConfigEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 26, 1, 20),
    _F3L3TrafficIPv6IfRaDhcpMoreConfigEnabled_Type()
)
f3L3TrafficIPv6IfRaDhcpMoreConfigEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6IfRaDhcpMoreConfigEnabled.setStatus("current")
_F3L3TrafficIPv6IfRaManagedAddressConfigEnabled_Type = TruthValue
_F3L3TrafficIPv6IfRaManagedAddressConfigEnabled_Object = MibTableColumn
f3L3TrafficIPv6IfRaManagedAddressConfigEnabled = _F3L3TrafficIPv6IfRaManagedAddressConfigEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 26, 1, 21),
    _F3L3TrafficIPv6IfRaManagedAddressConfigEnabled_Type()
)
f3L3TrafficIPv6IfRaManagedAddressConfigEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6IfRaManagedAddressConfigEnabled.setStatus("current")
_F3L3TrafficIPv6IfRaRDNSSOptionEnabled_Type = TruthValue
_F3L3TrafficIPv6IfRaRDNSSOptionEnabled_Object = MibTableColumn
f3L3TrafficIPv6IfRaRDNSSOptionEnabled = _F3L3TrafficIPv6IfRaRDNSSOptionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 26, 1, 22),
    _F3L3TrafficIPv6IfRaRDNSSOptionEnabled_Type()
)
f3L3TrafficIPv6IfRaRDNSSOptionEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6IfRaRDNSSOptionEnabled.setStatus("current")
_F3L3TrafficIPv6IfRaRDNSSLifeTime_Type = Unsigned32
_F3L3TrafficIPv6IfRaRDNSSLifeTime_Object = MibTableColumn
f3L3TrafficIPv6IfRaRDNSSLifeTime = _F3L3TrafficIPv6IfRaRDNSSLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 26, 1, 23),
    _F3L3TrafficIPv6IfRaRDNSSLifeTime_Type()
)
f3L3TrafficIPv6IfRaRDNSSLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6IfRaRDNSSLifeTime.setStatus("current")
_F3L3TrafficIPv6IfRaDNSSList_Type = DisplayString
_F3L3TrafficIPv6IfRaDNSSList_Object = MibTableColumn
f3L3TrafficIPv6IfRaDNSSList = _F3L3TrafficIPv6IfRaDNSSList_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 26, 1, 24),
    _F3L3TrafficIPv6IfRaDNSSList_Type()
)
f3L3TrafficIPv6IfRaDNSSList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6IfRaDNSSList.setStatus("current")
_F3L3TrafficIPv6IfRaDefaultRouterPreference_Type = NdpRaDefaultRouterPreference
_F3L3TrafficIPv6IfRaDefaultRouterPreference_Object = MibTableColumn
f3L3TrafficIPv6IfRaDefaultRouterPreference = _F3L3TrafficIPv6IfRaDefaultRouterPreference_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 26, 1, 25),
    _F3L3TrafficIPv6IfRaDefaultRouterPreference_Type()
)
f3L3TrafficIPv6IfRaDefaultRouterPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6IfRaDefaultRouterPreference.setStatus("current")
_F3L3TrafficIPv6IfDupAddrDetectControl_Type = TruthValue
_F3L3TrafficIPv6IfDupAddrDetectControl_Object = MibTableColumn
f3L3TrafficIPv6IfDupAddrDetectControl = _F3L3TrafficIPv6IfDupAddrDetectControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 26, 1, 26),
    _F3L3TrafficIPv6IfDupAddrDetectControl_Type()
)
f3L3TrafficIPv6IfDupAddrDetectControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6IfDupAddrDetectControl.setStatus("current")
_F3L3TrafficIPv6IfDupAddrDetectTransmits_Type = Unsigned32
_F3L3TrafficIPv6IfDupAddrDetectTransmits_Object = MibTableColumn
f3L3TrafficIPv6IfDupAddrDetectTransmits = _F3L3TrafficIPv6IfDupAddrDetectTransmits_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 26, 1, 27),
    _F3L3TrafficIPv6IfDupAddrDetectTransmits_Type()
)
f3L3TrafficIPv6IfDupAddrDetectTransmits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6IfDupAddrDetectTransmits.setStatus("current")
_F3L3TrafficIPv6IfDupAddrDetectRetransTimer_Type = Unsigned32
_F3L3TrafficIPv6IfDupAddrDetectRetransTimer_Object = MibTableColumn
f3L3TrafficIPv6IfDupAddrDetectRetransTimer = _F3L3TrafficIPv6IfDupAddrDetectRetransTimer_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 26, 1, 28),
    _F3L3TrafficIPv6IfDupAddrDetectRetransTimer_Type()
)
f3L3TrafficIPv6IfDupAddrDetectRetransTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6IfDupAddrDetectRetransTimer.setStatus("current")
_F3L3TrafficIPv6IfStorageType_Type = StorageType
_F3L3TrafficIPv6IfStorageType_Object = MibTableColumn
f3L3TrafficIPv6IfStorageType = _F3L3TrafficIPv6IfStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 26, 1, 29),
    _F3L3TrafficIPv6IfStorageType_Type()
)
f3L3TrafficIPv6IfStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6IfStorageType.setStatus("current")
_F3L3TrafficIPv6IfRowStatus_Type = RowStatus
_F3L3TrafficIPv6IfRowStatus_Object = MibTableColumn
f3L3TrafficIPv6IfRowStatus = _F3L3TrafficIPv6IfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 26, 1, 30),
    _F3L3TrafficIPv6IfRowStatus_Type()
)
f3L3TrafficIPv6IfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6IfRowStatus.setStatus("current")
_F3L3TrafficIPv6IfAction_Type = TrafficIpv6InterfaceActionType
_F3L3TrafficIPv6IfAction_Object = MibTableColumn
f3L3TrafficIPv6IfAction = _F3L3TrafficIPv6IfAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 26, 1, 31),
    _F3L3TrafficIPv6IfAction_Type()
)
f3L3TrafficIPv6IfAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6IfAction.setStatus("current")
_F3L3TrafficIPv6AddressTable_Object = MibTable
f3L3TrafficIPv6AddressTable = _F3L3TrafficIPv6AddressTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 27)
)
if mibBuilder.loadTexts:
    f3L3TrafficIPv6AddressTable.setStatus("current")
_F3L3TrafficIPv6AddressEntry_Object = MibTableRow
f3L3TrafficIPv6AddressEntry = _F3L3TrafficIPv6AddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 27, 1)
)
f3L3TrafficIPv6AddressEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficIPv6IfIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficIPv6AddrIndex"),
)
if mibBuilder.loadTexts:
    f3L3TrafficIPv6AddressEntry.setStatus("current")
_F3L3TrafficIPv6AddrIndex_Type = Integer32
_F3L3TrafficIPv6AddrIndex_Object = MibTableColumn
f3L3TrafficIPv6AddrIndex = _F3L3TrafficIPv6AddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 27, 1, 1),
    _F3L3TrafficIPv6AddrIndex_Type()
)
f3L3TrafficIPv6AddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6AddrIndex.setStatus("current")
_F3L3TrafficIPv6AddrAssignMode_Type = Ipv6AddressAssignMode
_F3L3TrafficIPv6AddrAssignMode_Object = MibTableColumn
f3L3TrafficIPv6AddrAssignMode = _F3L3TrafficIPv6AddrAssignMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 27, 1, 2),
    _F3L3TrafficIPv6AddrAssignMode_Type()
)
f3L3TrafficIPv6AddrAssignMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6AddrAssignMode.setStatus("current")
_F3L3TrafficIPv6AddrUnicastAddr_Type = Ipv6Address
_F3L3TrafficIPv6AddrUnicastAddr_Object = MibTableColumn
f3L3TrafficIPv6AddrUnicastAddr = _F3L3TrafficIPv6AddrUnicastAddr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 27, 1, 3),
    _F3L3TrafficIPv6AddrUnicastAddr_Type()
)
f3L3TrafficIPv6AddrUnicastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6AddrUnicastAddr.setStatus("current")
_F3L3TrafficIPv6AddrUnicastAddrPrefixLength_Type = Integer32
_F3L3TrafficIPv6AddrUnicastAddrPrefixLength_Object = MibTableColumn
f3L3TrafficIPv6AddrUnicastAddrPrefixLength = _F3L3TrafficIPv6AddrUnicastAddrPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 27, 1, 4),
    _F3L3TrafficIPv6AddrUnicastAddrPrefixLength_Type()
)
f3L3TrafficIPv6AddrUnicastAddrPrefixLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6AddrUnicastAddrPrefixLength.setStatus("current")
_F3L3TrafficIPv6AddrUnicastAddrAutoGenPrefix_Type = DisplayString
_F3L3TrafficIPv6AddrUnicastAddrAutoGenPrefix_Object = MibTableColumn
f3L3TrafficIPv6AddrUnicastAddrAutoGenPrefix = _F3L3TrafficIPv6AddrUnicastAddrAutoGenPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 27, 1, 5),
    _F3L3TrafficIPv6AddrUnicastAddrAutoGenPrefix_Type()
)
f3L3TrafficIPv6AddrUnicastAddrAutoGenPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6AddrUnicastAddrAutoGenPrefix.setStatus("current")
_F3L3TrafficIPv6AddrStorageType_Type = StorageType
_F3L3TrafficIPv6AddrStorageType_Object = MibTableColumn
f3L3TrafficIPv6AddrStorageType = _F3L3TrafficIPv6AddrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 27, 1, 6),
    _F3L3TrafficIPv6AddrStorageType_Type()
)
f3L3TrafficIPv6AddrStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6AddrStorageType.setStatus("current")
_F3L3TrafficIPv6AddrRowStatus_Type = RowStatus
_F3L3TrafficIPv6AddrRowStatus_Object = MibTableColumn
f3L3TrafficIPv6AddrRowStatus = _F3L3TrafficIPv6AddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 27, 1, 7),
    _F3L3TrafficIPv6AddrRowStatus_Type()
)
f3L3TrafficIPv6AddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6AddrRowStatus.setStatus("current")
_F3L3TrafficIPv6PrefixTable_Object = MibTable
f3L3TrafficIPv6PrefixTable = _F3L3TrafficIPv6PrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 28)
)
if mibBuilder.loadTexts:
    f3L3TrafficIPv6PrefixTable.setStatus("current")
_F3L3TrafficIPv6PrefixEntry_Object = MibTableRow
f3L3TrafficIPv6PrefixEntry = _F3L3TrafficIPv6PrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 28, 1)
)
f3L3TrafficIPv6PrefixEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficIPv6IfIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficIPv6PrefixIndex"),
)
if mibBuilder.loadTexts:
    f3L3TrafficIPv6PrefixEntry.setStatus("current")
_F3L3TrafficIPv6PrefixIndex_Type = Integer32
_F3L3TrafficIPv6PrefixIndex_Object = MibTableColumn
f3L3TrafficIPv6PrefixIndex = _F3L3TrafficIPv6PrefixIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 28, 1, 1),
    _F3L3TrafficIPv6PrefixIndex_Type()
)
f3L3TrafficIPv6PrefixIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6PrefixIndex.setStatus("current")
_F3L3TrafficIPv6PrefixRaPrefixAdvEnabled_Type = TruthValue
_F3L3TrafficIPv6PrefixRaPrefixAdvEnabled_Object = MibTableColumn
f3L3TrafficIPv6PrefixRaPrefixAdvEnabled = _F3L3TrafficIPv6PrefixRaPrefixAdvEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 28, 1, 2),
    _F3L3TrafficIPv6PrefixRaPrefixAdvEnabled_Type()
)
f3L3TrafficIPv6PrefixRaPrefixAdvEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6PrefixRaPrefixAdvEnabled.setStatus("current")
_F3L3TrafficIPv6PrefixRaPrefix_Type = Ipv6Address
_F3L3TrafficIPv6PrefixRaPrefix_Object = MibTableColumn
f3L3TrafficIPv6PrefixRaPrefix = _F3L3TrafficIPv6PrefixRaPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 28, 1, 3),
    _F3L3TrafficIPv6PrefixRaPrefix_Type()
)
f3L3TrafficIPv6PrefixRaPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6PrefixRaPrefix.setStatus("current")
_F3L3TrafficIPv6PrefixRaPrefixLength_Type = Integer32
_F3L3TrafficIPv6PrefixRaPrefixLength_Object = MibTableColumn
f3L3TrafficIPv6PrefixRaPrefixLength = _F3L3TrafficIPv6PrefixRaPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 28, 1, 4),
    _F3L3TrafficIPv6PrefixRaPrefixLength_Type()
)
f3L3TrafficIPv6PrefixRaPrefixLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6PrefixRaPrefixLength.setStatus("current")
_F3L3TrafficIPv6PrefixValidLifeTime_Type = Unsigned32
_F3L3TrafficIPv6PrefixValidLifeTime_Object = MibTableColumn
f3L3TrafficIPv6PrefixValidLifeTime = _F3L3TrafficIPv6PrefixValidLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 28, 1, 5),
    _F3L3TrafficIPv6PrefixValidLifeTime_Type()
)
f3L3TrafficIPv6PrefixValidLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6PrefixValidLifeTime.setStatus("current")
_F3L3TrafficIPv6PrefixPreferredLifeTime_Type = Unsigned32
_F3L3TrafficIPv6PrefixPreferredLifeTime_Object = MibTableColumn
f3L3TrafficIPv6PrefixPreferredLifeTime = _F3L3TrafficIPv6PrefixPreferredLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 28, 1, 6),
    _F3L3TrafficIPv6PrefixPreferredLifeTime_Type()
)
f3L3TrafficIPv6PrefixPreferredLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6PrefixPreferredLifeTime.setStatus("current")
_F3L3TrafficIPv6PrefixStorageType_Type = StorageType
_F3L3TrafficIPv6PrefixStorageType_Object = MibTableColumn
f3L3TrafficIPv6PrefixStorageType = _F3L3TrafficIPv6PrefixStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 28, 1, 7),
    _F3L3TrafficIPv6PrefixStorageType_Type()
)
f3L3TrafficIPv6PrefixStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6PrefixStorageType.setStatus("current")
_F3L3TrafficIPv6PrefixRowStatus_Type = RowStatus
_F3L3TrafficIPv6PrefixRowStatus_Object = MibTableColumn
f3L3TrafficIPv6PrefixRowStatus = _F3L3TrafficIPv6PrefixRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 28, 1, 8),
    _F3L3TrafficIPv6PrefixRowStatus_Type()
)
f3L3TrafficIPv6PrefixRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6PrefixRowStatus.setStatus("current")
_F3L3TrafficIPv6NdpTable_Object = MibTable
f3L3TrafficIPv6NdpTable = _F3L3TrafficIPv6NdpTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 29)
)
if mibBuilder.loadTexts:
    f3L3TrafficIPv6NdpTable.setStatus("current")
_F3L3TrafficIPv6NdpEntry_Object = MibTableRow
f3L3TrafficIPv6NdpEntry = _F3L3TrafficIPv6NdpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 29, 1)
)
f3L3TrafficIPv6NdpEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficIPv6IfIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficIPv6NdpIPv6Addr"),
)
if mibBuilder.loadTexts:
    f3L3TrafficIPv6NdpEntry.setStatus("current")
_F3L3TrafficIPv6NdpIPv6Addr_Type = Ipv6Address
_F3L3TrafficIPv6NdpIPv6Addr_Object = MibTableColumn
f3L3TrafficIPv6NdpIPv6Addr = _F3L3TrafficIPv6NdpIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 29, 1, 1),
    _F3L3TrafficIPv6NdpIPv6Addr_Type()
)
f3L3TrafficIPv6NdpIPv6Addr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6NdpIPv6Addr.setStatus("current")


class _F3L3TrafficIPv6NdpInterface_Type(DisplayString):
    """Custom type f3L3TrafficIPv6NdpInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_F3L3TrafficIPv6NdpInterface_Type.__name__ = "DisplayString"
_F3L3TrafficIPv6NdpInterface_Object = MibTableColumn
f3L3TrafficIPv6NdpInterface = _F3L3TrafficIPv6NdpInterface_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 29, 1, 2),
    _F3L3TrafficIPv6NdpInterface_Type()
)
f3L3TrafficIPv6NdpInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6NdpInterface.setStatus("current")
_F3L3TrafficIPv6NdpMacAddress_Type = MacAddress
_F3L3TrafficIPv6NdpMacAddress_Object = MibTableColumn
f3L3TrafficIPv6NdpMacAddress = _F3L3TrafficIPv6NdpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 29, 1, 3),
    _F3L3TrafficIPv6NdpMacAddress_Type()
)
f3L3TrafficIPv6NdpMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6NdpMacAddress.setStatus("current")
_F3L3TrafficIPv6NdpType_Type = IpEntryType
_F3L3TrafficIPv6NdpType_Object = MibTableColumn
f3L3TrafficIPv6NdpType = _F3L3TrafficIPv6NdpType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 29, 1, 4),
    _F3L3TrafficIPv6NdpType_Type()
)
f3L3TrafficIPv6NdpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6NdpType.setStatus("current")
_F3L3TrafficIPv6NdpReachabilityState_Type = NdpNeighborReachabilityState
_F3L3TrafficIPv6NdpReachabilityState_Object = MibTableColumn
f3L3TrafficIPv6NdpReachabilityState = _F3L3TrafficIPv6NdpReachabilityState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 29, 1, 5),
    _F3L3TrafficIPv6NdpReachabilityState_Type()
)
f3L3TrafficIPv6NdpReachabilityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6NdpReachabilityState.setStatus("current")
_F3L3TrafficIPv6NdpAge_Type = Integer32
_F3L3TrafficIPv6NdpAge_Object = MibTableColumn
f3L3TrafficIPv6NdpAge = _F3L3TrafficIPv6NdpAge_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 29, 1, 6),
    _F3L3TrafficIPv6NdpAge_Type()
)
f3L3TrafficIPv6NdpAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6NdpAge.setStatus("current")
_F3L3TrafficIPv6NdpStorageType_Type = StorageType
_F3L3TrafficIPv6NdpStorageType_Object = MibTableColumn
f3L3TrafficIPv6NdpStorageType = _F3L3TrafficIPv6NdpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 29, 1, 7),
    _F3L3TrafficIPv6NdpStorageType_Type()
)
f3L3TrafficIPv6NdpStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6NdpStorageType.setStatus("current")
_F3L3TrafficIPv6NdpRowStatus_Type = RowStatus
_F3L3TrafficIPv6NdpRowStatus_Object = MibTableColumn
f3L3TrafficIPv6NdpRowStatus = _F3L3TrafficIPv6NdpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 29, 1, 8),
    _F3L3TrafficIPv6NdpRowStatus_Type()
)
f3L3TrafficIPv6NdpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6NdpRowStatus.setStatus("current")
_F3L3TrafficIpv6RouteTable_Object = MibTable
f3L3TrafficIpv6RouteTable = _F3L3TrafficIpv6RouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 30)
)
if mibBuilder.loadTexts:
    f3L3TrafficIpv6RouteTable.setStatus("current")
_F3L3TrafficIpv6RouteEntry_Object = MibTableRow
f3L3TrafficIpv6RouteEntry = _F3L3TrafficIpv6RouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 30, 1)
)
f3L3TrafficIpv6RouteEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-L3-MIB", "f3VrfIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficIpv6RouteDest"),
    (0, "F3-L3-MIB", "f3L3TrafficIpv6RoutePrefixLength"),
    (0, "F3-L3-MIB", "f3L3TrafficIpv6RouteGateway"),
    (0, "F3-L3-MIB", "f3L3TrafficIpv6RouteInterface"),
)
if mibBuilder.loadTexts:
    f3L3TrafficIpv6RouteEntry.setStatus("current")
_F3L3TrafficIpv6RouteDest_Type = Ipv6Address
_F3L3TrafficIpv6RouteDest_Object = MibTableColumn
f3L3TrafficIpv6RouteDest = _F3L3TrafficIpv6RouteDest_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 30, 1, 1),
    _F3L3TrafficIpv6RouteDest_Type()
)
f3L3TrafficIpv6RouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3TrafficIpv6RouteDest.setStatus("current")
_F3L3TrafficIpv6RoutePrefixLength_Type = Integer32
_F3L3TrafficIpv6RoutePrefixLength_Object = MibTableColumn
f3L3TrafficIpv6RoutePrefixLength = _F3L3TrafficIpv6RoutePrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 30, 1, 2),
    _F3L3TrafficIpv6RoutePrefixLength_Type()
)
f3L3TrafficIpv6RoutePrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3TrafficIpv6RoutePrefixLength.setStatus("current")
_F3L3TrafficIpv6RouteGateway_Type = Ipv6Address
_F3L3TrafficIpv6RouteGateway_Object = MibTableColumn
f3L3TrafficIpv6RouteGateway = _F3L3TrafficIpv6RouteGateway_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 30, 1, 3),
    _F3L3TrafficIpv6RouteGateway_Type()
)
f3L3TrafficIpv6RouteGateway.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3TrafficIpv6RouteGateway.setStatus("current")


class _F3L3TrafficIpv6RouteInterface_Type(DisplayString):
    """Custom type f3L3TrafficIpv6RouteInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_F3L3TrafficIpv6RouteInterface_Type.__name__ = "DisplayString"
_F3L3TrafficIpv6RouteInterface_Object = MibTableColumn
f3L3TrafficIpv6RouteInterface = _F3L3TrafficIpv6RouteInterface_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 30, 1, 4),
    _F3L3TrafficIpv6RouteInterface_Type()
)
f3L3TrafficIpv6RouteInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3TrafficIpv6RouteInterface.setStatus("current")
_F3L3TrafficIpv6RouteMetric_Type = Integer32
_F3L3TrafficIpv6RouteMetric_Object = MibTableColumn
f3L3TrafficIpv6RouteMetric = _F3L3TrafficIpv6RouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 30, 1, 5),
    _F3L3TrafficIpv6RouteMetric_Type()
)
f3L3TrafficIpv6RouteMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIpv6RouteMetric.setStatus("current")
_F3L3TrafficIpv6RouteType_Type = IpEntryType
_F3L3TrafficIpv6RouteType_Object = MibTableColumn
f3L3TrafficIpv6RouteType = _F3L3TrafficIpv6RouteType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 30, 1, 6),
    _F3L3TrafficIpv6RouteType_Type()
)
f3L3TrafficIpv6RouteType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficIpv6RouteType.setStatus("current")
_F3L3TrafficIpv6RouteAdvertise_Type = TruthValue
_F3L3TrafficIpv6RouteAdvertise_Object = MibTableColumn
f3L3TrafficIpv6RouteAdvertise = _F3L3TrafficIpv6RouteAdvertise_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 30, 1, 7),
    _F3L3TrafficIpv6RouteAdvertise_Type()
)
f3L3TrafficIpv6RouteAdvertise.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficIpv6RouteAdvertise.setStatus("current")
_F3L3TrafficIpv6RouteStatus_Type = TrafficIpRouteStatus
_F3L3TrafficIpv6RouteStatus_Object = MibTableColumn
f3L3TrafficIpv6RouteStatus = _F3L3TrafficIpv6RouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 30, 1, 8),
    _F3L3TrafficIpv6RouteStatus_Type()
)
f3L3TrafficIpv6RouteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpv6RouteStatus.setStatus("current")
_F3L3TrafficIpv6RouteFlags_Type = RouteFlags
_F3L3TrafficIpv6RouteFlags_Object = MibTableColumn
f3L3TrafficIpv6RouteFlags = _F3L3TrafficIpv6RouteFlags_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 30, 1, 9),
    _F3L3TrafficIpv6RouteFlags_Type()
)
f3L3TrafficIpv6RouteFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpv6RouteFlags.setStatus("current")
_F3L3TrafficIpv6RouteOrigin_Type = TrafficIpRouteOriginType
_F3L3TrafficIpv6RouteOrigin_Object = MibTableColumn
f3L3TrafficIpv6RouteOrigin = _F3L3TrafficIpv6RouteOrigin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 30, 1, 10),
    _F3L3TrafficIpv6RouteOrigin_Type()
)
f3L3TrafficIpv6RouteOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpv6RouteOrigin.setStatus("current")
_F3L3TrafficIpv6RouteStorageType_Type = StorageType
_F3L3TrafficIpv6RouteStorageType_Object = MibTableColumn
f3L3TrafficIpv6RouteStorageType = _F3L3TrafficIpv6RouteStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 30, 1, 11),
    _F3L3TrafficIpv6RouteStorageType_Type()
)
f3L3TrafficIpv6RouteStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficIpv6RouteStorageType.setStatus("current")
_F3L3TrafficIpv6RouteRowStatus_Type = RowStatus
_F3L3TrafficIpv6RouteRowStatus_Object = MibTableColumn
f3L3TrafficIpv6RouteRowStatus = _F3L3TrafficIpv6RouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 30, 1, 12),
    _F3L3TrafficIpv6RouteRowStatus_Type()
)
f3L3TrafficIpv6RouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficIpv6RouteRowStatus.setStatus("current")
_F3DhcpV6RelayAgentTable_Object = MibTable
f3DhcpV6RelayAgentTable = _F3DhcpV6RelayAgentTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 31)
)
if mibBuilder.loadTexts:
    f3DhcpV6RelayAgentTable.setStatus("current")
_F3DhcpV6RelayAgentEntry_Object = MibTableRow
f3DhcpV6RelayAgentEntry = _F3DhcpV6RelayAgentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 31, 1)
)
f3DhcpV6RelayAgentEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-L3-MIB", "f3DhcpV6RelayAgentIndex"),
)
if mibBuilder.loadTexts:
    f3DhcpV6RelayAgentEntry.setStatus("current")
_F3DhcpV6RelayAgentIndex_Type = Integer32
_F3DhcpV6RelayAgentIndex_Object = MibTableColumn
f3DhcpV6RelayAgentIndex = _F3DhcpV6RelayAgentIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 31, 1, 1),
    _F3DhcpV6RelayAgentIndex_Type()
)
f3DhcpV6RelayAgentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3DhcpV6RelayAgentIndex.setStatus("current")


class _F3DhcpV6RelayAgentAlias_Type(F3DisplayString):
    """Custom type f3DhcpV6RelayAgentAlias based on F3DisplayString"""
    subtypeSpec = F3DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_F3DhcpV6RelayAgentAlias_Type.__name__ = "F3DisplayString"
_F3DhcpV6RelayAgentAlias_Object = MibTableColumn
f3DhcpV6RelayAgentAlias = _F3DhcpV6RelayAgentAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 31, 1, 2),
    _F3DhcpV6RelayAgentAlias_Type()
)
f3DhcpV6RelayAgentAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3DhcpV6RelayAgentAlias.setStatus("current")
_F3DhcpV6RelayAgentAdminState_Type = AdminState
_F3DhcpV6RelayAgentAdminState_Object = MibTableColumn
f3DhcpV6RelayAgentAdminState = _F3DhcpV6RelayAgentAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 31, 1, 3),
    _F3DhcpV6RelayAgentAdminState_Type()
)
f3DhcpV6RelayAgentAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3DhcpV6RelayAgentAdminState.setStatus("current")
_F3DhcpV6RelayAgentSecondaryState_Type = SecondaryState
_F3DhcpV6RelayAgentSecondaryState_Object = MibTableColumn
f3DhcpV6RelayAgentSecondaryState = _F3DhcpV6RelayAgentSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 31, 1, 4),
    _F3DhcpV6RelayAgentSecondaryState_Type()
)
f3DhcpV6RelayAgentSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3DhcpV6RelayAgentSecondaryState.setStatus("current")
_F3DhcpV6RelayAgentOperationalState_Type = OperationalState
_F3DhcpV6RelayAgentOperationalState_Object = MibTableColumn
f3DhcpV6RelayAgentOperationalState = _F3DhcpV6RelayAgentOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 31, 1, 5),
    _F3DhcpV6RelayAgentOperationalState_Type()
)
f3DhcpV6RelayAgentOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3DhcpV6RelayAgentOperationalState.setStatus("current")
_F3DhcpV6RelayAgentServerIpAddress_Type = Ipv6Address
_F3DhcpV6RelayAgentServerIpAddress_Object = MibTableColumn
f3DhcpV6RelayAgentServerIpAddress = _F3DhcpV6RelayAgentServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 31, 1, 6),
    _F3DhcpV6RelayAgentServerIpAddress_Type()
)
f3DhcpV6RelayAgentServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3DhcpV6RelayAgentServerIpAddress.setStatus("current")
_F3DhcpV6RelayAgentServerIpInteface_Type = VariablePointer
_F3DhcpV6RelayAgentServerIpInteface_Object = MibTableColumn
f3DhcpV6RelayAgentServerIpInteface = _F3DhcpV6RelayAgentServerIpInteface_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 31, 1, 7),
    _F3DhcpV6RelayAgentServerIpInteface_Type()
)
f3DhcpV6RelayAgentServerIpInteface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3DhcpV6RelayAgentServerIpInteface.setStatus("current")
_F3DhcpV6RelayAgentStorageType_Type = StorageType
_F3DhcpV6RelayAgentStorageType_Object = MibTableColumn
f3DhcpV6RelayAgentStorageType = _F3DhcpV6RelayAgentStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 31, 1, 8),
    _F3DhcpV6RelayAgentStorageType_Type()
)
f3DhcpV6RelayAgentStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3DhcpV6RelayAgentStorageType.setStatus("current")
_F3DhcpV6RelayAgentRowStatus_Type = RowStatus
_F3DhcpV6RelayAgentRowStatus_Object = MibTableColumn
f3DhcpV6RelayAgentRowStatus = _F3DhcpV6RelayAgentRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 31, 1, 9),
    _F3DhcpV6RelayAgentRowStatus_Type()
)
f3DhcpV6RelayAgentRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3DhcpV6RelayAgentRowStatus.setStatus("current")
_F3DhcpV6RelayAgentClientTrafficIpIfMemberTable_Object = MibTable
f3DhcpV6RelayAgentClientTrafficIpIfMemberTable = _F3DhcpV6RelayAgentClientTrafficIpIfMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 32)
)
if mibBuilder.loadTexts:
    f3DhcpV6RelayAgentClientTrafficIpIfMemberTable.setStatus("current")
_F3DhcpV6RelayAgentClientTrafficIpIfMemberEntry_Object = MibTableRow
f3DhcpV6RelayAgentClientTrafficIpIfMemberEntry = _F3DhcpV6RelayAgentClientTrafficIpIfMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 32, 1)
)
f3DhcpV6RelayAgentClientTrafficIpIfMemberEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-L3-MIB", "f3DhcpV6RelayAgentIndex"),
    (0, "F3-L3-MIB", "f3DhcpV6RelayAgentClientTrafficIpIfMemberObject"),
)
if mibBuilder.loadTexts:
    f3DhcpV6RelayAgentClientTrafficIpIfMemberEntry.setStatus("current")
_F3DhcpV6RelayAgentClientTrafficIpIfMemberObject_Type = VariablePointer
_F3DhcpV6RelayAgentClientTrafficIpIfMemberObject_Object = MibTableColumn
f3DhcpV6RelayAgentClientTrafficIpIfMemberObject = _F3DhcpV6RelayAgentClientTrafficIpIfMemberObject_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 32, 1, 1),
    _F3DhcpV6RelayAgentClientTrafficIpIfMemberObject_Type()
)
f3DhcpV6RelayAgentClientTrafficIpIfMemberObject.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3DhcpV6RelayAgentClientTrafficIpIfMemberObject.setStatus("current")
_F3DhcpV6RelayAgentClientTrafficIpIfMemberStorageType_Type = StorageType
_F3DhcpV6RelayAgentClientTrafficIpIfMemberStorageType_Object = MibTableColumn
f3DhcpV6RelayAgentClientTrafficIpIfMemberStorageType = _F3DhcpV6RelayAgentClientTrafficIpIfMemberStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 32, 1, 2),
    _F3DhcpV6RelayAgentClientTrafficIpIfMemberStorageType_Type()
)
f3DhcpV6RelayAgentClientTrafficIpIfMemberStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3DhcpV6RelayAgentClientTrafficIpIfMemberStorageType.setStatus("current")
_F3DhcpV6RelayAgentClientTrafficIpIfMemberRowStatus_Type = RowStatus
_F3DhcpV6RelayAgentClientTrafficIpIfMemberRowStatus_Object = MibTableColumn
f3DhcpV6RelayAgentClientTrafficIpIfMemberRowStatus = _F3DhcpV6RelayAgentClientTrafficIpIfMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 32, 1, 3),
    _F3DhcpV6RelayAgentClientTrafficIpIfMemberRowStatus_Type()
)
f3DhcpV6RelayAgentClientTrafficIpIfMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3DhcpV6RelayAgentClientTrafficIpIfMemberRowStatus.setStatus("current")
_CmL3FlowPointTable_Object = MibTable
cmL3FlowPointTable = _CmL3FlowPointTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 33)
)
if mibBuilder.loadTexts:
    cmL3FlowPointTable.setStatus("current")
_CmL3FlowPointEntry_Object = MibTableRow
cmL3FlowPointEntry = _CmL3FlowPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 33, 1)
)
cmL3FlowPointEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "cmL3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "cmL3FlowPointIndex"),
)
if mibBuilder.loadTexts:
    cmL3FlowPointEntry.setStatus("current")
_CmL3FlowPointPortIndex_Type = Integer32
_CmL3FlowPointPortIndex_Object = MibTableColumn
cmL3FlowPointPortIndex = _CmL3FlowPointPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 33, 1, 1),
    _CmL3FlowPointPortIndex_Type()
)
cmL3FlowPointPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmL3FlowPointPortIndex.setStatus("current")
_CmL3FlowPointIndex_Type = Integer32
_CmL3FlowPointIndex_Object = MibTableColumn
cmL3FlowPointIndex = _CmL3FlowPointIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 33, 1, 2),
    _CmL3FlowPointIndex_Type()
)
cmL3FlowPointIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmL3FlowPointIndex.setStatus("current")


class _CmL3FlowPointAlias_Type(F3DisplayString):
    """Custom type cmL3FlowPointAlias based on F3DisplayString"""
    subtypeSpec = F3DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CmL3FlowPointAlias_Type.__name__ = "F3DisplayString"
_CmL3FlowPointAlias_Object = MibTableColumn
cmL3FlowPointAlias = _CmL3FlowPointAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 33, 1, 3),
    _CmL3FlowPointAlias_Type()
)
cmL3FlowPointAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmL3FlowPointAlias.setStatus("current")
_CmL3FlowPointAdminState_Type = AdminState
_CmL3FlowPointAdminState_Object = MibTableColumn
cmL3FlowPointAdminState = _CmL3FlowPointAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 33, 1, 4),
    _CmL3FlowPointAdminState_Type()
)
cmL3FlowPointAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmL3FlowPointAdminState.setStatus("current")
_CmL3FlowPointSecondaryState_Type = SecondaryState
_CmL3FlowPointSecondaryState_Object = MibTableColumn
cmL3FlowPointSecondaryState = _CmL3FlowPointSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 33, 1, 5),
    _CmL3FlowPointSecondaryState_Type()
)
cmL3FlowPointSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3FlowPointSecondaryState.setStatus("current")
_CmL3FlowPointOperationalState_Type = OperationalState
_CmL3FlowPointOperationalState_Object = MibTableColumn
cmL3FlowPointOperationalState = _CmL3FlowPointOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 33, 1, 6),
    _CmL3FlowPointOperationalState_Type()
)
cmL3FlowPointOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3FlowPointOperationalState.setStatus("current")
_CmL3FlowPointMultiCOSEnabled_Type = TruthValue
_CmL3FlowPointMultiCOSEnabled_Object = MibTableColumn
cmL3FlowPointMultiCOSEnabled = _CmL3FlowPointMultiCOSEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 33, 1, 7),
    _CmL3FlowPointMultiCOSEnabled_Type()
)
cmL3FlowPointMultiCOSEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmL3FlowPointMultiCOSEnabled.setStatus("current")
_CmL3FlowPointCOS_Type = Integer32
_CmL3FlowPointCOS_Object = MibTableColumn
cmL3FlowPointCOS = _CmL3FlowPointCOS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 33, 1, 8),
    _CmL3FlowPointCOS_Type()
)
cmL3FlowPointCOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmL3FlowPointCOS.setStatus("current")
_CmL3FlowPointUntaggedMemberShipEnabled_Type = TruthValue
_CmL3FlowPointUntaggedMemberShipEnabled_Object = MibTableColumn
cmL3FlowPointUntaggedMemberShipEnabled = _CmL3FlowPointUntaggedMemberShipEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 33, 1, 9),
    _CmL3FlowPointUntaggedMemberShipEnabled_Type()
)
cmL3FlowPointUntaggedMemberShipEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmL3FlowPointUntaggedMemberShipEnabled.setStatus("current")
_CmL3FlowPointOuterTagMemberShipEnabled_Type = TruthValue
_CmL3FlowPointOuterTagMemberShipEnabled_Object = MibTableColumn
cmL3FlowPointOuterTagMemberShipEnabled = _CmL3FlowPointOuterTagMemberShipEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 33, 1, 10),
    _CmL3FlowPointOuterTagMemberShipEnabled_Type()
)
cmL3FlowPointOuterTagMemberShipEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmL3FlowPointOuterTagMemberShipEnabled.setStatus("current")
_CmL3FlowPointOuterTagMemberShipVlanId_Type = VlanId
_CmL3FlowPointOuterTagMemberShipVlanId_Object = MibTableColumn
cmL3FlowPointOuterTagMemberShipVlanId = _CmL3FlowPointOuterTagMemberShipVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 33, 1, 11),
    _CmL3FlowPointOuterTagMemberShipVlanId_Type()
)
cmL3FlowPointOuterTagMemberShipVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmL3FlowPointOuterTagMemberShipVlanId.setStatus("current")
_CmL3FlowPointInnerTagMemberShipEnabled_Type = TruthValue
_CmL3FlowPointInnerTagMemberShipEnabled_Object = MibTableColumn
cmL3FlowPointInnerTagMemberShipEnabled = _CmL3FlowPointInnerTagMemberShipEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 33, 1, 12),
    _CmL3FlowPointInnerTagMemberShipEnabled_Type()
)
cmL3FlowPointInnerTagMemberShipEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmL3FlowPointInnerTagMemberShipEnabled.setStatus("current")
_CmL3FlowPointInnerTagMemberShipVlanId_Type = VlanId
_CmL3FlowPointInnerTagMemberShipVlanId_Object = MibTableColumn
cmL3FlowPointInnerTagMemberShipVlanId = _CmL3FlowPointInnerTagMemberShipVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 33, 1, 13),
    _CmL3FlowPointInnerTagMemberShipVlanId_Type()
)
cmL3FlowPointInnerTagMemberShipVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmL3FlowPointInnerTagMemberShipVlanId.setStatus("current")
_CmL3FlowPointFragmentedPktsFwdEnabled_Type = TruthValue
_CmL3FlowPointFragmentedPktsFwdEnabled_Object = MibTableColumn
cmL3FlowPointFragmentedPktsFwdEnabled = _CmL3FlowPointFragmentedPktsFwdEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 33, 1, 14),
    _CmL3FlowPointFragmentedPktsFwdEnabled_Type()
)
cmL3FlowPointFragmentedPktsFwdEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmL3FlowPointFragmentedPktsFwdEnabled.setStatus("current")
_CmL3FlowPointHCosMgmtEnabled_Type = TruthValue
_CmL3FlowPointHCosMgmtEnabled_Object = MibTableColumn
cmL3FlowPointHCosMgmtEnabled = _CmL3FlowPointHCosMgmtEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 33, 1, 15),
    _CmL3FlowPointHCosMgmtEnabled_Type()
)
cmL3FlowPointHCosMgmtEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmL3FlowPointHCosMgmtEnabled.setStatus("current")
_CmL3FlowPointHCosGuaranteedBwHi_Type = Unsigned32
_CmL3FlowPointHCosGuaranteedBwHi_Object = MibTableColumn
cmL3FlowPointHCosGuaranteedBwHi = _CmL3FlowPointHCosGuaranteedBwHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 33, 1, 16),
    _CmL3FlowPointHCosGuaranteedBwHi_Type()
)
cmL3FlowPointHCosGuaranteedBwHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmL3FlowPointHCosGuaranteedBwHi.setStatus("current")
_CmL3FlowPointHCosGuaranteedBwLo_Type = Unsigned32
_CmL3FlowPointHCosGuaranteedBwLo_Object = MibTableColumn
cmL3FlowPointHCosGuaranteedBwLo = _CmL3FlowPointHCosGuaranteedBwLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 33, 1, 17),
    _CmL3FlowPointHCosGuaranteedBwLo_Type()
)
cmL3FlowPointHCosGuaranteedBwLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmL3FlowPointHCosGuaranteedBwLo.setStatus("current")
_CmL3FlowPointHCosMaximumBwHi_Type = Unsigned32
_CmL3FlowPointHCosMaximumBwHi_Object = MibTableColumn
cmL3FlowPointHCosMaximumBwHi = _CmL3FlowPointHCosMaximumBwHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 33, 1, 18),
    _CmL3FlowPointHCosMaximumBwHi_Type()
)
cmL3FlowPointHCosMaximumBwHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmL3FlowPointHCosMaximumBwHi.setStatus("current")
_CmL3FlowPointHCosMaximumBwLo_Type = Unsigned32
_CmL3FlowPointHCosMaximumBwLo_Object = MibTableColumn
cmL3FlowPointHCosMaximumBwLo = _CmL3FlowPointHCosMaximumBwLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 33, 1, 19),
    _CmL3FlowPointHCosMaximumBwLo_Type()
)
cmL3FlowPointHCosMaximumBwLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmL3FlowPointHCosMaximumBwLo.setStatus("current")
_CmL3FlowPointDscpOverwriteControl_Type = TruthValue
_CmL3FlowPointDscpOverwriteControl_Object = MibTableColumn
cmL3FlowPointDscpOverwriteControl = _CmL3FlowPointDscpOverwriteControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 33, 1, 20),
    _CmL3FlowPointDscpOverwriteControl_Type()
)
cmL3FlowPointDscpOverwriteControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmL3FlowPointDscpOverwriteControl.setStatus("current")
_CmL3FlowPointPriMapProfile_Type = VariablePointer
_CmL3FlowPointPriMapProfile_Object = MibTableColumn
cmL3FlowPointPriMapProfile = _CmL3FlowPointPriMapProfile_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 33, 1, 21),
    _CmL3FlowPointPriMapProfile_Type()
)
cmL3FlowPointPriMapProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmL3FlowPointPriMapProfile.setStatus("current")
_CmL3FlowPointStorageType_Type = StorageType
_CmL3FlowPointStorageType_Object = MibTableColumn
cmL3FlowPointStorageType = _CmL3FlowPointStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 33, 1, 22),
    _CmL3FlowPointStorageType_Type()
)
cmL3FlowPointStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmL3FlowPointStorageType.setStatus("current")
_CmL3FlowPointRowStatus_Type = RowStatus
_CmL3FlowPointRowStatus_Object = MibTableColumn
cmL3FlowPointRowStatus = _CmL3FlowPointRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 33, 1, 23),
    _CmL3FlowPointRowStatus_Type()
)
cmL3FlowPointRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmL3FlowPointRowStatus.setStatus("current")
_CmL3FlowPointAclNoMatchDisposition_Type = AclNoMatchDispositionType
_CmL3FlowPointAclNoMatchDisposition_Object = MibTableColumn
cmL3FlowPointAclNoMatchDisposition = _CmL3FlowPointAclNoMatchDisposition_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 33, 1, 24),
    _CmL3FlowPointAclNoMatchDisposition_Type()
)
cmL3FlowPointAclNoMatchDisposition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmL3FlowPointAclNoMatchDisposition.setStatus("current")
_CmL3FlowPointWfqSegmentationCOS_Type = Integer32
_CmL3FlowPointWfqSegmentationCOS_Object = MibTableColumn
cmL3FlowPointWfqSegmentationCOS = _CmL3FlowPointWfqSegmentationCOS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 33, 1, 25),
    _CmL3FlowPointWfqSegmentationCOS_Type()
)
cmL3FlowPointWfqSegmentationCOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmL3FlowPointWfqSegmentationCOS.setStatus("current")
_CmL3FlowPointWfqGroupCOS_Type = Integer32
_CmL3FlowPointWfqGroupCOS_Object = MibTableColumn
cmL3FlowPointWfqGroupCOS = _CmL3FlowPointWfqGroupCOS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 33, 1, 26),
    _CmL3FlowPointWfqGroupCOS_Type()
)
cmL3FlowPointWfqGroupCOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmL3FlowPointWfqGroupCOS.setStatus("current")
_CmL3FlowPointWfqGroupEirLo_Type = Unsigned32
_CmL3FlowPointWfqGroupEirLo_Object = MibTableColumn
cmL3FlowPointWfqGroupEirLo = _CmL3FlowPointWfqGroupEirLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 33, 1, 27),
    _CmL3FlowPointWfqGroupEirLo_Type()
)
cmL3FlowPointWfqGroupEirLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmL3FlowPointWfqGroupEirLo.setStatus("current")
_CmL3FlowPointWfqGroupEirHi_Type = Unsigned32
_CmL3FlowPointWfqGroupEirHi_Object = MibTableColumn
cmL3FlowPointWfqGroupEirHi = _CmL3FlowPointWfqGroupEirHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 33, 1, 28),
    _CmL3FlowPointWfqGroupEirHi_Type()
)
cmL3FlowPointWfqGroupEirHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmL3FlowPointWfqGroupEirHi.setStatus("current")
_CmL3FlowPointEgressShapingType_Type = ShapingType
_CmL3FlowPointEgressShapingType_Object = MibTableColumn
cmL3FlowPointEgressShapingType = _CmL3FlowPointEgressShapingType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 33, 1, 29),
    _CmL3FlowPointEgressShapingType_Type()
)
cmL3FlowPointEgressShapingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmL3FlowPointEgressShapingType.setStatus("current")
_CmL3QosPolicerTable_Object = MibTable
cmL3QosPolicerTable = _CmL3QosPolicerTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 34)
)
if mibBuilder.loadTexts:
    cmL3QosPolicerTable.setStatus("current")
_CmL3QosPolicerEntry_Object = MibTableRow
cmL3QosPolicerEntry = _CmL3QosPolicerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 34, 1)
)
cmL3QosPolicerEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "cmL3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "cmL3FlowPointIndex"),
    (0, "F3-L3-MIB", "cmL3QosPolicerIndex"),
)
if mibBuilder.loadTexts:
    cmL3QosPolicerEntry.setStatus("current")


class _CmL3QosPolicerIndex_Type(Integer32):
    """Custom type cmL3QosPolicerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CmL3QosPolicerIndex_Type.__name__ = "Integer32"
_CmL3QosPolicerIndex_Object = MibTableColumn
cmL3QosPolicerIndex = _CmL3QosPolicerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 34, 1, 1),
    _CmL3QosPolicerIndex_Type()
)
cmL3QosPolicerIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmL3QosPolicerIndex.setStatus("current")
_CmL3QosPolicerAdminState_Type = AdminState
_CmL3QosPolicerAdminState_Object = MibTableColumn
cmL3QosPolicerAdminState = _CmL3QosPolicerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 34, 1, 2),
    _CmL3QosPolicerAdminState_Type()
)
cmL3QosPolicerAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmL3QosPolicerAdminState.setStatus("current")
_CmL3QosPolicerOperationalState_Type = OperationalState
_CmL3QosPolicerOperationalState_Object = MibTableColumn
cmL3QosPolicerOperationalState = _CmL3QosPolicerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 34, 1, 3),
    _CmL3QosPolicerOperationalState_Type()
)
cmL3QosPolicerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosPolicerOperationalState.setStatus("current")
_CmL3QosPolicerSecondaryState_Type = SecondaryState
_CmL3QosPolicerSecondaryState_Object = MibTableColumn
cmL3QosPolicerSecondaryState = _CmL3QosPolicerSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 34, 1, 4),
    _CmL3QosPolicerSecondaryState_Type()
)
cmL3QosPolicerSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosPolicerSecondaryState.setStatus("current")
_CmL3QosPolicerCIRLo_Type = Unsigned32
_CmL3QosPolicerCIRLo_Object = MibTableColumn
cmL3QosPolicerCIRLo = _CmL3QosPolicerCIRLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 34, 1, 5),
    _CmL3QosPolicerCIRLo_Type()
)
cmL3QosPolicerCIRLo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmL3QosPolicerCIRLo.setStatus("current")
_CmL3QosPolicerCIRHi_Type = Unsigned32
_CmL3QosPolicerCIRHi_Object = MibTableColumn
cmL3QosPolicerCIRHi = _CmL3QosPolicerCIRHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 34, 1, 6),
    _CmL3QosPolicerCIRHi_Type()
)
cmL3QosPolicerCIRHi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmL3QosPolicerCIRHi.setStatus("current")
_CmL3QosPolicerEIRLo_Type = Unsigned32
_CmL3QosPolicerEIRLo_Object = MibTableColumn
cmL3QosPolicerEIRLo = _CmL3QosPolicerEIRLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 34, 1, 7),
    _CmL3QosPolicerEIRLo_Type()
)
cmL3QosPolicerEIRLo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmL3QosPolicerEIRLo.setStatus("current")
_CmL3QosPolicerEIRHi_Type = Unsigned32
_CmL3QosPolicerEIRHi_Object = MibTableColumn
cmL3QosPolicerEIRHi = _CmL3QosPolicerEIRHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 34, 1, 8),
    _CmL3QosPolicerEIRHi_Type()
)
cmL3QosPolicerEIRHi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmL3QosPolicerEIRHi.setStatus("current")
_CmL3QosPolicerCBS_Type = Integer32
_CmL3QosPolicerCBS_Object = MibTableColumn
cmL3QosPolicerCBS = _CmL3QosPolicerCBS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 34, 1, 9),
    _CmL3QosPolicerCBS_Type()
)
cmL3QosPolicerCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmL3QosPolicerCBS.setStatus("current")
_CmL3QosPolicerEBS_Type = Integer32
_CmL3QosPolicerEBS_Object = MibTableColumn
cmL3QosPolicerEBS = _CmL3QosPolicerEBS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 34, 1, 10),
    _CmL3QosPolicerEBS_Type()
)
cmL3QosPolicerEBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmL3QosPolicerEBS.setStatus("current")
_CmL3QosPolicerAlgorithm_Type = PolicerAlgorithmType
_CmL3QosPolicerAlgorithm_Object = MibTableColumn
cmL3QosPolicerAlgorithm = _CmL3QosPolicerAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 34, 1, 11),
    _CmL3QosPolicerAlgorithm_Type()
)
cmL3QosPolicerAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosPolicerAlgorithm.setStatus("current")
_CmL3QosPolicerColorMode_Type = PolicerColorMode
_CmL3QosPolicerColorMode_Object = MibTableColumn
cmL3QosPolicerColorMode = _CmL3QosPolicerColorMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 34, 1, 12),
    _CmL3QosPolicerColorMode_Type()
)
cmL3QosPolicerColorMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmL3QosPolicerColorMode.setStatus("current")
_CmL3QosPolicerCouplingFlag_Type = TruthValue
_CmL3QosPolicerCouplingFlag_Object = MibTableColumn
cmL3QosPolicerCouplingFlag = _CmL3QosPolicerCouplingFlag_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 34, 1, 13),
    _CmL3QosPolicerCouplingFlag_Type()
)
cmL3QosPolicerCouplingFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmL3QosPolicerCouplingFlag.setStatus("current")
_CmL3QosPolicerCIRMaxHi_Type = Unsigned32
_CmL3QosPolicerCIRMaxHi_Object = MibTableColumn
cmL3QosPolicerCIRMaxHi = _CmL3QosPolicerCIRMaxHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 34, 1, 14),
    _CmL3QosPolicerCIRMaxHi_Type()
)
cmL3QosPolicerCIRMaxHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmL3QosPolicerCIRMaxHi.setStatus("current")
_CmL3QosPolicerCIRMaxLo_Type = Unsigned32
_CmL3QosPolicerCIRMaxLo_Object = MibTableColumn
cmL3QosPolicerCIRMaxLo = _CmL3QosPolicerCIRMaxLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 34, 1, 15),
    _CmL3QosPolicerCIRMaxLo_Type()
)
cmL3QosPolicerCIRMaxLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmL3QosPolicerCIRMaxLo.setStatus("current")
_CmL3QosPolicerEIRMaxHi_Type = Unsigned32
_CmL3QosPolicerEIRMaxHi_Object = MibTableColumn
cmL3QosPolicerEIRMaxHi = _CmL3QosPolicerEIRMaxHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 34, 1, 16),
    _CmL3QosPolicerEIRMaxHi_Type()
)
cmL3QosPolicerEIRMaxHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmL3QosPolicerEIRMaxHi.setStatus("current")
_CmL3QosPolicerEIRMaxLo_Type = Unsigned32
_CmL3QosPolicerEIRMaxLo_Object = MibTableColumn
cmL3QosPolicerEIRMaxLo = _CmL3QosPolicerEIRMaxLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 34, 1, 17),
    _CmL3QosPolicerEIRMaxLo_Type()
)
cmL3QosPolicerEIRMaxLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmL3QosPolicerEIRMaxLo.setStatus("current")
_CmL3QosPolicerEnvelopeObject_Type = VariablePointer
_CmL3QosPolicerEnvelopeObject_Object = MibTableColumn
cmL3QosPolicerEnvelopeObject = _CmL3QosPolicerEnvelopeObject_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 34, 1, 18),
    _CmL3QosPolicerEnvelopeObject_Type()
)
cmL3QosPolicerEnvelopeObject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmL3QosPolicerEnvelopeObject.setStatus("current")
_CmL3QosPolicerRank_Type = Integer32
_CmL3QosPolicerRank_Object = MibTableColumn
cmL3QosPolicerRank = _CmL3QosPolicerRank_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 34, 1, 19),
    _CmL3QosPolicerRank_Type()
)
cmL3QosPolicerRank.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmL3QosPolicerRank.setStatus("current")
_CmL3QosPolicerPolicingEnabled_Type = TruthValue
_CmL3QosPolicerPolicingEnabled_Object = MibTableColumn
cmL3QosPolicerPolicingEnabled = _CmL3QosPolicerPolicingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 34, 1, 20),
    _CmL3QosPolicerPolicingEnabled_Type()
)
cmL3QosPolicerPolicingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmL3QosPolicerPolicingEnabled.setStatus("current")
_CmL3QosPolicerStorageType_Type = StorageType
_CmL3QosPolicerStorageType_Object = MibTableColumn
cmL3QosPolicerStorageType = _CmL3QosPolicerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 34, 1, 21),
    _CmL3QosPolicerStorageType_Type()
)
cmL3QosPolicerStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmL3QosPolicerStorageType.setStatus("current")
_CmL3QosPolicerRowStatus_Type = RowStatus
_CmL3QosPolicerRowStatus_Object = MibTableColumn
cmL3QosPolicerRowStatus = _CmL3QosPolicerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 34, 1, 22),
    _CmL3QosPolicerRowStatus_Type()
)
cmL3QosPolicerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmL3QosPolicerRowStatus.setStatus("current")
_CmL3QosShaperTable_Object = MibTable
cmL3QosShaperTable = _CmL3QosShaperTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 35)
)
if mibBuilder.loadTexts:
    cmL3QosShaperTable.setStatus("current")
_CmL3QosShaperEntry_Object = MibTableRow
cmL3QosShaperEntry = _CmL3QosShaperEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 35, 1)
)
cmL3QosShaperEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "cmL3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "cmL3FlowPointIndex"),
    (0, "F3-L3-MIB", "cmL3QosShaperIndex"),
)
if mibBuilder.loadTexts:
    cmL3QosShaperEntry.setStatus("current")


class _CmL3QosShaperIndex_Type(Integer32):
    """Custom type cmL3QosShaperIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CmL3QosShaperIndex_Type.__name__ = "Integer32"
_CmL3QosShaperIndex_Object = MibTableColumn
cmL3QosShaperIndex = _CmL3QosShaperIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 35, 1, 1),
    _CmL3QosShaperIndex_Type()
)
cmL3QosShaperIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmL3QosShaperIndex.setStatus("current")
_CmL3QosShaperAdminState_Type = AdminState
_CmL3QosShaperAdminState_Object = MibTableColumn
cmL3QosShaperAdminState = _CmL3QosShaperAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 35, 1, 2),
    _CmL3QosShaperAdminState_Type()
)
cmL3QosShaperAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmL3QosShaperAdminState.setStatus("current")
_CmL3QosShaperOperationalState_Type = OperationalState
_CmL3QosShaperOperationalState_Object = MibTableColumn
cmL3QosShaperOperationalState = _CmL3QosShaperOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 35, 1, 3),
    _CmL3QosShaperOperationalState_Type()
)
cmL3QosShaperOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosShaperOperationalState.setStatus("current")
_CmL3QosShaperSecondaryState_Type = SecondaryState
_CmL3QosShaperSecondaryState_Object = MibTableColumn
cmL3QosShaperSecondaryState = _CmL3QosShaperSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 35, 1, 4),
    _CmL3QosShaperSecondaryState_Type()
)
cmL3QosShaperSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosShaperSecondaryState.setStatus("current")
_CmL3QosShaperCIRLo_Type = Unsigned32
_CmL3QosShaperCIRLo_Object = MibTableColumn
cmL3QosShaperCIRLo = _CmL3QosShaperCIRLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 35, 1, 5),
    _CmL3QosShaperCIRLo_Type()
)
cmL3QosShaperCIRLo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmL3QosShaperCIRLo.setStatus("current")
_CmL3QosShaperCIRHi_Type = Unsigned32
_CmL3QosShaperCIRHi_Object = MibTableColumn
cmL3QosShaperCIRHi = _CmL3QosShaperCIRHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 35, 1, 6),
    _CmL3QosShaperCIRHi_Type()
)
cmL3QosShaperCIRHi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmL3QosShaperCIRHi.setStatus("current")
_CmL3QosShaperEIRLo_Type = Unsigned32
_CmL3QosShaperEIRLo_Object = MibTableColumn
cmL3QosShaperEIRLo = _CmL3QosShaperEIRLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 35, 1, 7),
    _CmL3QosShaperEIRLo_Type()
)
cmL3QosShaperEIRLo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmL3QosShaperEIRLo.setStatus("current")
_CmL3QosShaperEIRHi_Type = Unsigned32
_CmL3QosShaperEIRHi_Object = MibTableColumn
cmL3QosShaperEIRHi = _CmL3QosShaperEIRHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 35, 1, 8),
    _CmL3QosShaperEIRHi_Type()
)
cmL3QosShaperEIRHi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmL3QosShaperEIRHi.setStatus("current")
_CmL3QosShaperBufferSize_Type = Unsigned32
_CmL3QosShaperBufferSize_Object = MibTableColumn
cmL3QosShaperBufferSize = _CmL3QosShaperBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 35, 1, 9),
    _CmL3QosShaperBufferSize_Type()
)
cmL3QosShaperBufferSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmL3QosShaperBufferSize.setStatus("current")


class _CmL3QosShaperCOS_Type(Integer32):
    """Custom type cmL3QosShaperCOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CmL3QosShaperCOS_Type.__name__ = "Integer32"
_CmL3QosShaperCOS_Object = MibTableColumn
cmL3QosShaperCOS = _CmL3QosShaperCOS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 35, 1, 10),
    _CmL3QosShaperCOS_Type()
)
cmL3QosShaperCOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosShaperCOS.setStatus("current")
_CmL3QosShaperStorageType_Type = StorageType
_CmL3QosShaperStorageType_Object = MibTableColumn
cmL3QosShaperStorageType = _CmL3QosShaperStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 35, 1, 11),
    _CmL3QosShaperStorageType_Type()
)
cmL3QosShaperStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmL3QosShaperStorageType.setStatus("current")
_CmL3QosShaperRowStatus_Type = RowStatus
_CmL3QosShaperRowStatus_Object = MibTableColumn
cmL3QosShaperRowStatus = _CmL3QosShaperRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 35, 1, 12),
    _CmL3QosShaperRowStatus_Type()
)
cmL3QosShaperRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmL3QosShaperRowStatus.setStatus("current")
_CmL3QosShaperWfqWeight_Type = Integer32
_CmL3QosShaperWfqWeight_Object = MibTableColumn
cmL3QosShaperWfqWeight = _CmL3QosShaperWfqWeight_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 35, 1, 13),
    _CmL3QosShaperWfqWeight_Type()
)
cmL3QosShaperWfqWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmL3QosShaperWfqWeight.setStatus("current")
_F3L3TrafficOspfInterfaceTable_Object = MibTable
f3L3TrafficOspfInterfaceTable = _F3L3TrafficOspfInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 36)
)
if mibBuilder.loadTexts:
    f3L3TrafficOspfInterfaceTable.setStatus("current")
_F3L3TrafficOspfInterfaceEntry_Object = MibTableRow
f3L3TrafficOspfInterfaceEntry = _F3L3TrafficOspfInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 36, 1)
)
f3L3TrafficOspfInterfaceEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-L3-MIB", "f3VrfIndex"),
    (0, "F3-L3-MIB", "f3VrfOspfRouterIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficOspfAreaIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficOspfInterfaceIndex"),
)
if mibBuilder.loadTexts:
    f3L3TrafficOspfInterfaceEntry.setStatus("current")
_F3L3TrafficOspfInterfaceIndex_Type = Integer32
_F3L3TrafficOspfInterfaceIndex_Object = MibTableColumn
f3L3TrafficOspfInterfaceIndex = _F3L3TrafficOspfInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 36, 1, 1),
    _F3L3TrafficOspfInterfaceIndex_Type()
)
f3L3TrafficOspfInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3TrafficOspfInterfaceIndex.setStatus("current")
_F3L3TrafficOspfInterfaceOspfCost_Type = Unsigned32
_F3L3TrafficOspfInterfaceOspfCost_Object = MibTableColumn
f3L3TrafficOspfInterfaceOspfCost = _F3L3TrafficOspfInterfaceOspfCost_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 36, 1, 2),
    _F3L3TrafficOspfInterfaceOspfCost_Type()
)
f3L3TrafficOspfInterfaceOspfCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficOspfInterfaceOspfCost.setStatus("current")
_F3L3TrafficOspfInterfaceType_Type = OspfIfType
_F3L3TrafficOspfInterfaceType_Object = MibTableColumn
f3L3TrafficOspfInterfaceType = _F3L3TrafficOspfInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 36, 1, 3),
    _F3L3TrafficOspfInterfaceType_Type()
)
f3L3TrafficOspfInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficOspfInterfaceType.setStatus("current")
_F3L3TrafficOspfInterfaceOspfRtrPriority_Type = Integer32
_F3L3TrafficOspfInterfaceOspfRtrPriority_Object = MibTableColumn
f3L3TrafficOspfInterfaceOspfRtrPriority = _F3L3TrafficOspfInterfaceOspfRtrPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 36, 1, 4),
    _F3L3TrafficOspfInterfaceOspfRtrPriority_Type()
)
f3L3TrafficOspfInterfaceOspfRtrPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficOspfInterfaceOspfRtrPriority.setStatus("current")
_F3L3TrafficOspfInterfaceOspfHelloInterval_Type = Integer32
_F3L3TrafficOspfInterfaceOspfHelloInterval_Object = MibTableColumn
f3L3TrafficOspfInterfaceOspfHelloInterval = _F3L3TrafficOspfInterfaceOspfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 36, 1, 5),
    _F3L3TrafficOspfInterfaceOspfHelloInterval_Type()
)
f3L3TrafficOspfInterfaceOspfHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficOspfInterfaceOspfHelloInterval.setStatus("current")
_F3L3TrafficOspfInterfaceOspfDeadInterval_Type = Integer32
_F3L3TrafficOspfInterfaceOspfDeadInterval_Object = MibTableColumn
f3L3TrafficOspfInterfaceOspfDeadInterval = _F3L3TrafficOspfInterfaceOspfDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 36, 1, 6),
    _F3L3TrafficOspfInterfaceOspfDeadInterval_Type()
)
f3L3TrafficOspfInterfaceOspfDeadInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficOspfInterfaceOspfDeadInterval.setStatus("current")
_F3L3TrafficOspfInterfaceOspfTransmitDelay_Type = Integer32
_F3L3TrafficOspfInterfaceOspfTransmitDelay_Object = MibTableColumn
f3L3TrafficOspfInterfaceOspfTransmitDelay = _F3L3TrafficOspfInterfaceOspfTransmitDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 36, 1, 7),
    _F3L3TrafficOspfInterfaceOspfTransmitDelay_Type()
)
f3L3TrafficOspfInterfaceOspfTransmitDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficOspfInterfaceOspfTransmitDelay.setStatus("current")
_F3L3TrafficOspfInterfaceOspfRetransmitInterval_Type = Integer32
_F3L3TrafficOspfInterfaceOspfRetransmitInterval_Object = MibTableColumn
f3L3TrafficOspfInterfaceOspfRetransmitInterval = _F3L3TrafficOspfInterfaceOspfRetransmitInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 36, 1, 8),
    _F3L3TrafficOspfInterfaceOspfRetransmitInterval_Type()
)
f3L3TrafficOspfInterfaceOspfRetransmitInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficOspfInterfaceOspfRetransmitInterval.setStatus("current")
_F3L3TrafficOspfInterfaceState_Type = OspfInterfaceState
_F3L3TrafficOspfInterfaceState_Object = MibTableColumn
f3L3TrafficOspfInterfaceState = _F3L3TrafficOspfInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 36, 1, 9),
    _F3L3TrafficOspfInterfaceState_Type()
)
f3L3TrafficOspfInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficOspfInterfaceState.setStatus("current")
_F3L3TrafficOspfInterfaceOspfDesignatedRouterId_Type = IpAddress
_F3L3TrafficOspfInterfaceOspfDesignatedRouterId_Object = MibTableColumn
f3L3TrafficOspfInterfaceOspfDesignatedRouterId = _F3L3TrafficOspfInterfaceOspfDesignatedRouterId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 36, 1, 10),
    _F3L3TrafficOspfInterfaceOspfDesignatedRouterId_Type()
)
f3L3TrafficOspfInterfaceOspfDesignatedRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficOspfInterfaceOspfDesignatedRouterId.setStatus("current")
_F3L3TrafficOspfInterfaceOspfBackupDesignatedRouterId_Type = IpAddress
_F3L3TrafficOspfInterfaceOspfBackupDesignatedRouterId_Object = MibTableColumn
f3L3TrafficOspfInterfaceOspfBackupDesignatedRouterId = _F3L3TrafficOspfInterfaceOspfBackupDesignatedRouterId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 36, 1, 11),
    _F3L3TrafficOspfInterfaceOspfBackupDesignatedRouterId_Type()
)
f3L3TrafficOspfInterfaceOspfBackupDesignatedRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficOspfInterfaceOspfBackupDesignatedRouterId.setStatus("current")
_F3L3TrafficOspfInterfaceOspfAuthType_Type = OspfAuthType
_F3L3TrafficOspfInterfaceOspfAuthType_Object = MibTableColumn
f3L3TrafficOspfInterfaceOspfAuthType = _F3L3TrafficOspfInterfaceOspfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 36, 1, 12),
    _F3L3TrafficOspfInterfaceOspfAuthType_Type()
)
f3L3TrafficOspfInterfaceOspfAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficOspfInterfaceOspfAuthType.setStatus("current")
_F3L3TrafficOspfInterfaceOspfSimpleAuthKey_Type = DisplayString
_F3L3TrafficOspfInterfaceOspfSimpleAuthKey_Object = MibTableColumn
f3L3TrafficOspfInterfaceOspfSimpleAuthKey = _F3L3TrafficOspfInterfaceOspfSimpleAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 36, 1, 13),
    _F3L3TrafficOspfInterfaceOspfSimpleAuthKey_Type()
)
f3L3TrafficOspfInterfaceOspfSimpleAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficOspfInterfaceOspfSimpleAuthKey.setStatus("current")
_F3L3TrafficOspfInterfaceOspfCryptoKeyId_Type = VariablePointer
_F3L3TrafficOspfInterfaceOspfCryptoKeyId_Object = MibTableColumn
f3L3TrafficOspfInterfaceOspfCryptoKeyId = _F3L3TrafficOspfInterfaceOspfCryptoKeyId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 36, 1, 14),
    _F3L3TrafficOspfInterfaceOspfCryptoKeyId_Type()
)
f3L3TrafficOspfInterfaceOspfCryptoKeyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficOspfInterfaceOspfCryptoKeyId.setStatus("current")
_F3L3TrafficOspfInterfaceOspfInstanceId_Type = Unsigned32
_F3L3TrafficOspfInterfaceOspfInstanceId_Object = MibTableColumn
f3L3TrafficOspfInterfaceOspfInstanceId = _F3L3TrafficOspfInterfaceOspfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 36, 1, 15),
    _F3L3TrafficOspfInterfaceOspfInstanceId_Type()
)
f3L3TrafficOspfInterfaceOspfInstanceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficOspfInterfaceOspfInstanceId.setStatus("current")
_F3L3TrafficOspfInterfaceId_Type = Unsigned32
_F3L3TrafficOspfInterfaceId_Object = MibTableColumn
f3L3TrafficOspfInterfaceId = _F3L3TrafficOspfInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 36, 1, 16),
    _F3L3TrafficOspfInterfaceId_Type()
)
f3L3TrafficOspfInterfaceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficOspfInterfaceId.setStatus("current")
_F3L3TrafficOspfInterfaceLinkLsaSuppression_Type = TruthValue
_F3L3TrafficOspfInterfaceLinkLsaSuppression_Object = MibTableColumn
f3L3TrafficOspfInterfaceLinkLsaSuppression = _F3L3TrafficOspfInterfaceLinkLsaSuppression_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 36, 1, 17),
    _F3L3TrafficOspfInterfaceLinkLsaSuppression_Type()
)
f3L3TrafficOspfInterfaceLinkLsaSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficOspfInterfaceLinkLsaSuppression.setStatus("current")
_F3L3TrafficOspfInterfacePassiveControl_Type = TruthValue
_F3L3TrafficOspfInterfacePassiveControl_Object = MibTableColumn
f3L3TrafficOspfInterfacePassiveControl = _F3L3TrafficOspfInterfacePassiveControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 36, 1, 18),
    _F3L3TrafficOspfInterfacePassiveControl_Type()
)
f3L3TrafficOspfInterfacePassiveControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficOspfInterfacePassiveControl.setStatus("current")
_F3L3TrafficOspfInterfaceAssociatedIpInterface_Type = DisplayString
_F3L3TrafficOspfInterfaceAssociatedIpInterface_Object = MibTableColumn
f3L3TrafficOspfInterfaceAssociatedIpInterface = _F3L3TrafficOspfInterfaceAssociatedIpInterface_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 36, 1, 19),
    _F3L3TrafficOspfInterfaceAssociatedIpInterface_Type()
)
f3L3TrafficOspfInterfaceAssociatedIpInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficOspfInterfaceAssociatedIpInterface.setStatus("current")
_F3L3TrafficOspfInterfaceStorageType_Type = StorageType
_F3L3TrafficOspfInterfaceStorageType_Object = MibTableColumn
f3L3TrafficOspfInterfaceStorageType = _F3L3TrafficOspfInterfaceStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 36, 1, 20),
    _F3L3TrafficOspfInterfaceStorageType_Type()
)
f3L3TrafficOspfInterfaceStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficOspfInterfaceStorageType.setStatus("current")
_F3L3TrafficOspfInterfaceRowStatus_Type = RowStatus
_F3L3TrafficOspfInterfaceRowStatus_Object = MibTableColumn
f3L3TrafficOspfInterfaceRowStatus = _F3L3TrafficOspfInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 36, 1, 21),
    _F3L3TrafficOspfInterfaceRowStatus_Type()
)
f3L3TrafficOspfInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficOspfInterfaceRowStatus.setStatus("current")
_F3L3TrafficOspfInterfaceTilfaControl_Type = TruthValue
_F3L3TrafficOspfInterfaceTilfaControl_Object = MibTableColumn
f3L3TrafficOspfInterfaceTilfaControl = _F3L3TrafficOspfInterfaceTilfaControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 36, 1, 22),
    _F3L3TrafficOspfInterfaceTilfaControl_Type()
)
f3L3TrafficOspfInterfaceTilfaControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficOspfInterfaceTilfaControl.setStatus("current")
_F3L3TrafficOspfInterfaceTilfaProtectionType_Type = TilfaProtectionType
_F3L3TrafficOspfInterfaceTilfaProtectionType_Object = MibTableColumn
f3L3TrafficOspfInterfaceTilfaProtectionType = _F3L3TrafficOspfInterfaceTilfaProtectionType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 36, 1, 23),
    _F3L3TrafficOspfInterfaceTilfaProtectionType_Type()
)
f3L3TrafficOspfInterfaceTilfaProtectionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficOspfInterfaceTilfaProtectionType.setStatus("current")
_F3L3TrafficBgpPeerAddressFamilyTable_Object = MibTable
f3L3TrafficBgpPeerAddressFamilyTable = _F3L3TrafficBgpPeerAddressFamilyTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 37)
)
if mibBuilder.loadTexts:
    f3L3TrafficBgpPeerAddressFamilyTable.setStatus("current")
_F3L3TrafficBgpPeerAddressFamilyEntry_Object = MibTableRow
f3L3TrafficBgpPeerAddressFamilyEntry = _F3L3TrafficBgpPeerAddressFamilyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 37, 1)
)
f3L3TrafficBgpPeerAddressFamilyEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-L3-MIB", "f3VrfIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficBgpRouterIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficBgpPeerIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficBgpPeerAddressFamilyIndex"),
)
if mibBuilder.loadTexts:
    f3L3TrafficBgpPeerAddressFamilyEntry.setStatus("current")
_F3L3TrafficBgpPeerAddressFamilyIndex_Type = Integer32
_F3L3TrafficBgpPeerAddressFamilyIndex_Object = MibTableColumn
f3L3TrafficBgpPeerAddressFamilyIndex = _F3L3TrafficBgpPeerAddressFamilyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 37, 1, 1),
    _F3L3TrafficBgpPeerAddressFamilyIndex_Type()
)
f3L3TrafficBgpPeerAddressFamilyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3TrafficBgpPeerAddressFamilyIndex.setStatus("current")
_F3L3TrafficBgpPeerAddressFamilyName_Type = BgpPeerAddressFamilyNameType
_F3L3TrafficBgpPeerAddressFamilyName_Object = MibTableColumn
f3L3TrafficBgpPeerAddressFamilyName = _F3L3TrafficBgpPeerAddressFamilyName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 37, 1, 2),
    _F3L3TrafficBgpPeerAddressFamilyName_Type()
)
f3L3TrafficBgpPeerAddressFamilyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficBgpPeerAddressFamilyName.setStatus("current")
_F3L3TrafficBgpPeerAddressFamilyRedistOspfRoute_Type = TruthValue
_F3L3TrafficBgpPeerAddressFamilyRedistOspfRoute_Object = MibTableColumn
f3L3TrafficBgpPeerAddressFamilyRedistOspfRoute = _F3L3TrafficBgpPeerAddressFamilyRedistOspfRoute_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 37, 1, 3),
    _F3L3TrafficBgpPeerAddressFamilyRedistOspfRoute_Type()
)
f3L3TrafficBgpPeerAddressFamilyRedistOspfRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficBgpPeerAddressFamilyRedistOspfRoute.setStatus("current")
_F3L3TrafficBgpPeerAddressFamilyRedistConnectedRoute_Type = TruthValue
_F3L3TrafficBgpPeerAddressFamilyRedistConnectedRoute_Object = MibTableColumn
f3L3TrafficBgpPeerAddressFamilyRedistConnectedRoute = _F3L3TrafficBgpPeerAddressFamilyRedistConnectedRoute_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 37, 1, 4),
    _F3L3TrafficBgpPeerAddressFamilyRedistConnectedRoute_Type()
)
f3L3TrafficBgpPeerAddressFamilyRedistConnectedRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficBgpPeerAddressFamilyRedistConnectedRoute.setStatus("current")
_F3L3TrafficBgpPeerAddressFamilyRedistStaticRoute_Type = TruthValue
_F3L3TrafficBgpPeerAddressFamilyRedistStaticRoute_Object = MibTableColumn
f3L3TrafficBgpPeerAddressFamilyRedistStaticRoute = _F3L3TrafficBgpPeerAddressFamilyRedistStaticRoute_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 37, 1, 5),
    _F3L3TrafficBgpPeerAddressFamilyRedistStaticRoute_Type()
)
f3L3TrafficBgpPeerAddressFamilyRedistStaticRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficBgpPeerAddressFamilyRedistStaticRoute.setStatus("current")
_F3L3TrafficBgpPeerAddressFamilyRedistDhcpRoute_Type = TruthValue
_F3L3TrafficBgpPeerAddressFamilyRedistDhcpRoute_Object = MibTableColumn
f3L3TrafficBgpPeerAddressFamilyRedistDhcpRoute = _F3L3TrafficBgpPeerAddressFamilyRedistDhcpRoute_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 37, 1, 6),
    _F3L3TrafficBgpPeerAddressFamilyRedistDhcpRoute_Type()
)
f3L3TrafficBgpPeerAddressFamilyRedistDhcpRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficBgpPeerAddressFamilyRedistDhcpRoute.setStatus("current")
_F3L3TrafficBgpPeerAddressFamilyRedistSlaacRoute_Type = TruthValue
_F3L3TrafficBgpPeerAddressFamilyRedistSlaacRoute_Object = MibTableColumn
f3L3TrafficBgpPeerAddressFamilyRedistSlaacRoute = _F3L3TrafficBgpPeerAddressFamilyRedistSlaacRoute_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 37, 1, 7),
    _F3L3TrafficBgpPeerAddressFamilyRedistSlaacRoute_Type()
)
f3L3TrafficBgpPeerAddressFamilyRedistSlaacRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficBgpPeerAddressFamilyRedistSlaacRoute.setStatus("current")
_F3L3TrafficBgpPeerAddressFamilySendDefaultRoute_Type = TruthValue
_F3L3TrafficBgpPeerAddressFamilySendDefaultRoute_Object = MibTableColumn
f3L3TrafficBgpPeerAddressFamilySendDefaultRoute = _F3L3TrafficBgpPeerAddressFamilySendDefaultRoute_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 37, 1, 8),
    _F3L3TrafficBgpPeerAddressFamilySendDefaultRoute_Type()
)
f3L3TrafficBgpPeerAddressFamilySendDefaultRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficBgpPeerAddressFamilySendDefaultRoute.setStatus("current")
_F3L3TrafficBgpPeerAddressFamilyNextHopType_Type = BgpNextHopUpdateType
_F3L3TrafficBgpPeerAddressFamilyNextHopType_Object = MibTableColumn
f3L3TrafficBgpPeerAddressFamilyNextHopType = _F3L3TrafficBgpPeerAddressFamilyNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 37, 1, 9),
    _F3L3TrafficBgpPeerAddressFamilyNextHopType_Type()
)
f3L3TrafficBgpPeerAddressFamilyNextHopType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficBgpPeerAddressFamilyNextHopType.setStatus("current")
_F3L3TrafficBgpPeerAddressFamilyNextHopIpv4_Type = IpAddress
_F3L3TrafficBgpPeerAddressFamilyNextHopIpv4_Object = MibTableColumn
f3L3TrafficBgpPeerAddressFamilyNextHopIpv4 = _F3L3TrafficBgpPeerAddressFamilyNextHopIpv4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 37, 1, 10),
    _F3L3TrafficBgpPeerAddressFamilyNextHopIpv4_Type()
)
f3L3TrafficBgpPeerAddressFamilyNextHopIpv4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficBgpPeerAddressFamilyNextHopIpv4.setStatus("current")
_F3L3TrafficBgpPeerAddressFamilyNextHopIpv6_Type = Ipv6Address
_F3L3TrafficBgpPeerAddressFamilyNextHopIpv6_Object = MibTableColumn
f3L3TrafficBgpPeerAddressFamilyNextHopIpv6 = _F3L3TrafficBgpPeerAddressFamilyNextHopIpv6_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 37, 1, 11),
    _F3L3TrafficBgpPeerAddressFamilyNextHopIpv6_Type()
)
f3L3TrafficBgpPeerAddressFamilyNextHopIpv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficBgpPeerAddressFamilyNextHopIpv6.setStatus("current")
_F3L3TrafficBgpPeerAddressFamilyExtNextHopControl_Type = TruthValue
_F3L3TrafficBgpPeerAddressFamilyExtNextHopControl_Object = MibTableColumn
f3L3TrafficBgpPeerAddressFamilyExtNextHopControl = _F3L3TrafficBgpPeerAddressFamilyExtNextHopControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 37, 1, 12),
    _F3L3TrafficBgpPeerAddressFamilyExtNextHopControl_Type()
)
f3L3TrafficBgpPeerAddressFamilyExtNextHopControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficBgpPeerAddressFamilyExtNextHopControl.setStatus("current")
_F3L3TrafficBgpPeerAddressFamilyStorageType_Type = StorageType
_F3L3TrafficBgpPeerAddressFamilyStorageType_Object = MibTableColumn
f3L3TrafficBgpPeerAddressFamilyStorageType = _F3L3TrafficBgpPeerAddressFamilyStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 37, 1, 13),
    _F3L3TrafficBgpPeerAddressFamilyStorageType_Type()
)
f3L3TrafficBgpPeerAddressFamilyStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficBgpPeerAddressFamilyStorageType.setStatus("current")
_F3L3TrafficBgpPeerAddressFamilyRowStatus_Type = RowStatus
_F3L3TrafficBgpPeerAddressFamilyRowStatus_Object = MibTableColumn
f3L3TrafficBgpPeerAddressFamilyRowStatus = _F3L3TrafficBgpPeerAddressFamilyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 37, 1, 14),
    _F3L3TrafficBgpPeerAddressFamilyRowStatus_Type()
)
f3L3TrafficBgpPeerAddressFamilyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficBgpPeerAddressFamilyRowStatus.setStatus("current")
_F3L3TrafficBgpRIBRouteTable_Object = MibTable
f3L3TrafficBgpRIBRouteTable = _F3L3TrafficBgpRIBRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 38)
)
if mibBuilder.loadTexts:
    f3L3TrafficBgpRIBRouteTable.setStatus("current")
_F3L3TrafficBgpRIBRouteEntry_Object = MibTableRow
f3L3TrafficBgpRIBRouteEntry = _F3L3TrafficBgpRIBRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 38, 1)
)
f3L3TrafficBgpRIBRouteEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-L3-MIB", "f3VrfIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficBgpRouterIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficBgpRIBRouteIndex"),
)
if mibBuilder.loadTexts:
    f3L3TrafficBgpRIBRouteEntry.setStatus("current")
_F3L3TrafficBgpRIBRouteIndex_Type = Integer32
_F3L3TrafficBgpRIBRouteIndex_Object = MibTableColumn
f3L3TrafficBgpRIBRouteIndex = _F3L3TrafficBgpRIBRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 38, 1, 1),
    _F3L3TrafficBgpRIBRouteIndex_Type()
)
f3L3TrafficBgpRIBRouteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3TrafficBgpRIBRouteIndex.setStatus("current")
_F3L3TrafficBgpRIBRouteNetwork_Type = DisplayString
_F3L3TrafficBgpRIBRouteNetwork_Object = MibTableColumn
f3L3TrafficBgpRIBRouteNetwork = _F3L3TrafficBgpRIBRouteNetwork_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 38, 1, 2),
    _F3L3TrafficBgpRIBRouteNetwork_Type()
)
f3L3TrafficBgpRIBRouteNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficBgpRIBRouteNetwork.setStatus("current")
_F3L3TrafficBgpRIBRouteNextHop_Type = DisplayString
_F3L3TrafficBgpRIBRouteNextHop_Object = MibTableColumn
f3L3TrafficBgpRIBRouteNextHop = _F3L3TrafficBgpRIBRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 38, 1, 3),
    _F3L3TrafficBgpRIBRouteNextHop_Type()
)
f3L3TrafficBgpRIBRouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficBgpRIBRouteNextHop.setStatus("current")
_F3L3TrafficBgpRIBRouteMetric_Type = Integer32
_F3L3TrafficBgpRIBRouteMetric_Object = MibTableColumn
f3L3TrafficBgpRIBRouteMetric = _F3L3TrafficBgpRIBRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 38, 1, 4),
    _F3L3TrafficBgpRIBRouteMetric_Type()
)
f3L3TrafficBgpRIBRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficBgpRIBRouteMetric.setStatus("current")
_F3L3TrafficBgpRIBRoutePath_Type = DisplayString
_F3L3TrafficBgpRIBRoutePath_Object = MibTableColumn
f3L3TrafficBgpRIBRoutePath = _F3L3TrafficBgpRIBRoutePath_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 38, 1, 5),
    _F3L3TrafficBgpRIBRoutePath_Type()
)
f3L3TrafficBgpRIBRoutePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficBgpRIBRoutePath.setStatus("current")
_F3L3TrafficBgpInRouteTable_Object = MibTable
f3L3TrafficBgpInRouteTable = _F3L3TrafficBgpInRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 39)
)
if mibBuilder.loadTexts:
    f3L3TrafficBgpInRouteTable.setStatus("current")
_F3L3TrafficBgpInRouteEntry_Object = MibTableRow
f3L3TrafficBgpInRouteEntry = _F3L3TrafficBgpInRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 39, 1)
)
f3L3TrafficBgpInRouteEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-L3-MIB", "f3VrfIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficBgpRouterIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficBgpInRouteIndex"),
)
if mibBuilder.loadTexts:
    f3L3TrafficBgpInRouteEntry.setStatus("current")
_F3L3TrafficBgpInRouteIndex_Type = Unsigned32
_F3L3TrafficBgpInRouteIndex_Object = MibTableColumn
f3L3TrafficBgpInRouteIndex = _F3L3TrafficBgpInRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 39, 1, 1),
    _F3L3TrafficBgpInRouteIndex_Type()
)
f3L3TrafficBgpInRouteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3TrafficBgpInRouteIndex.setStatus("current")


class _F3L3TrafficBgpInRouteNetwork_Type(DisplayString):
    """Custom type f3L3TrafficBgpInRouteNetwork based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_F3L3TrafficBgpInRouteNetwork_Type.__name__ = "DisplayString"
_F3L3TrafficBgpInRouteNetwork_Object = MibTableColumn
f3L3TrafficBgpInRouteNetwork = _F3L3TrafficBgpInRouteNetwork_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 39, 1, 2),
    _F3L3TrafficBgpInRouteNetwork_Type()
)
f3L3TrafficBgpInRouteNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficBgpInRouteNetwork.setStatus("current")


class _F3L3TrafficBgpInRouteNextHop_Type(DisplayString):
    """Custom type f3L3TrafficBgpInRouteNextHop based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_F3L3TrafficBgpInRouteNextHop_Type.__name__ = "DisplayString"
_F3L3TrafficBgpInRouteNextHop_Object = MibTableColumn
f3L3TrafficBgpInRouteNextHop = _F3L3TrafficBgpInRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 39, 1, 3),
    _F3L3TrafficBgpInRouteNextHop_Type()
)
f3L3TrafficBgpInRouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficBgpInRouteNextHop.setStatus("current")
_F3L3TrafficBgpInRouteMetric_Type = Unsigned32
_F3L3TrafficBgpInRouteMetric_Object = MibTableColumn
f3L3TrafficBgpInRouteMetric = _F3L3TrafficBgpInRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 39, 1, 4),
    _F3L3TrafficBgpInRouteMetric_Type()
)
f3L3TrafficBgpInRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficBgpInRouteMetric.setStatus("current")


class _F3L3TrafficBgpInRoutePath_Type(DisplayString):
    """Custom type f3L3TrafficBgpInRoutePath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_F3L3TrafficBgpInRoutePath_Type.__name__ = "DisplayString"
_F3L3TrafficBgpInRoutePath_Object = MibTableColumn
f3L3TrafficBgpInRoutePath = _F3L3TrafficBgpInRoutePath_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 39, 1, 5),
    _F3L3TrafficBgpInRoutePath_Type()
)
f3L3TrafficBgpInRoutePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficBgpInRoutePath.setStatus("current")
_F3L3TrafficBgpInRouteLocalPreference_Type = Unsigned32
_F3L3TrafficBgpInRouteLocalPreference_Object = MibTableColumn
f3L3TrafficBgpInRouteLocalPreference = _F3L3TrafficBgpInRouteLocalPreference_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 39, 1, 6),
    _F3L3TrafficBgpInRouteLocalPreference_Type()
)
f3L3TrafficBgpInRouteLocalPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficBgpInRouteLocalPreference.setStatus("current")
_F3L3TrafficBgpRouteV2Table_Object = MibTable
f3L3TrafficBgpRouteV2Table = _F3L3TrafficBgpRouteV2Table_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 40)
)
if mibBuilder.loadTexts:
    f3L3TrafficBgpRouteV2Table.setStatus("current")
_F3L3TrafficBgpRouteV2Entry_Object = MibTableRow
f3L3TrafficBgpRouteV2Entry = _F3L3TrafficBgpRouteV2Entry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 40, 1)
)
f3L3TrafficBgpRouteV2Entry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-L3-MIB", "f3VrfIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficBgpRouterIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficBgpRouteV2Index"),
)
if mibBuilder.loadTexts:
    f3L3TrafficBgpRouteV2Entry.setStatus("current")
_F3L3TrafficBgpRouteV2Index_Type = Unsigned32
_F3L3TrafficBgpRouteV2Index_Object = MibTableColumn
f3L3TrafficBgpRouteV2Index = _F3L3TrafficBgpRouteV2Index_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 40, 1, 1),
    _F3L3TrafficBgpRouteV2Index_Type()
)
f3L3TrafficBgpRouteV2Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3TrafficBgpRouteV2Index.setStatus("current")


class _F3L3TrafficBgpRouteV2Network_Type(DisplayString):
    """Custom type f3L3TrafficBgpRouteV2Network based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_F3L3TrafficBgpRouteV2Network_Type.__name__ = "DisplayString"
_F3L3TrafficBgpRouteV2Network_Object = MibTableColumn
f3L3TrafficBgpRouteV2Network = _F3L3TrafficBgpRouteV2Network_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 40, 1, 2),
    _F3L3TrafficBgpRouteV2Network_Type()
)
f3L3TrafficBgpRouteV2Network.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficBgpRouteV2Network.setStatus("current")


class _F3L3TrafficBgpRouteV2NextHop_Type(DisplayString):
    """Custom type f3L3TrafficBgpRouteV2NextHop based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_F3L3TrafficBgpRouteV2NextHop_Type.__name__ = "DisplayString"
_F3L3TrafficBgpRouteV2NextHop_Object = MibTableColumn
f3L3TrafficBgpRouteV2NextHop = _F3L3TrafficBgpRouteV2NextHop_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 40, 1, 3),
    _F3L3TrafficBgpRouteV2NextHop_Type()
)
f3L3TrafficBgpRouteV2NextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficBgpRouteV2NextHop.setStatus("current")
_F3L3TrafficBgpRouteV2Metric_Type = Unsigned32
_F3L3TrafficBgpRouteV2Metric_Object = MibTableColumn
f3L3TrafficBgpRouteV2Metric = _F3L3TrafficBgpRouteV2Metric_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 40, 1, 4),
    _F3L3TrafficBgpRouteV2Metric_Type()
)
f3L3TrafficBgpRouteV2Metric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficBgpRouteV2Metric.setStatus("current")


class _F3L3TrafficBgpRouteV2Path_Type(DisplayString):
    """Custom type f3L3TrafficBgpRouteV2Path based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_F3L3TrafficBgpRouteV2Path_Type.__name__ = "DisplayString"
_F3L3TrafficBgpRouteV2Path_Object = MibTableColumn
f3L3TrafficBgpRouteV2Path = _F3L3TrafficBgpRouteV2Path_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 40, 1, 5),
    _F3L3TrafficBgpRouteV2Path_Type()
)
f3L3TrafficBgpRouteV2Path.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficBgpRouteV2Path.setStatus("current")
_F3L3TrafficBgpRouteV2LocalPreference_Type = Unsigned32
_F3L3TrafficBgpRouteV2LocalPreference_Object = MibTableColumn
f3L3TrafficBgpRouteV2LocalPreference = _F3L3TrafficBgpRouteV2LocalPreference_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 40, 1, 6),
    _F3L3TrafficBgpRouteV2LocalPreference_Type()
)
f3L3TrafficBgpRouteV2LocalPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficBgpRouteV2LocalPreference.setStatus("current")
_F3L3TrafficBgpPeerAddressFamilyAdvPrefixTable_Object = MibTable
f3L3TrafficBgpPeerAddressFamilyAdvPrefixTable = _F3L3TrafficBgpPeerAddressFamilyAdvPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 41)
)
if mibBuilder.loadTexts:
    f3L3TrafficBgpPeerAddressFamilyAdvPrefixTable.setStatus("current")
_F3L3TrafficBgpPeerAddressFamilyAdvPrefixEntry_Object = MibTableRow
f3L3TrafficBgpPeerAddressFamilyAdvPrefixEntry = _F3L3TrafficBgpPeerAddressFamilyAdvPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 41, 1)
)
f3L3TrafficBgpPeerAddressFamilyAdvPrefixEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-L3-MIB", "f3VrfIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficBgpRouterIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficBgpPeerIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficBgpPeerAddressFamilyIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficBgpPeerAddressFamilyAdvPrefix"),
)
if mibBuilder.loadTexts:
    f3L3TrafficBgpPeerAddressFamilyAdvPrefixEntry.setStatus("current")
_F3L3TrafficBgpPeerAddressFamilyAdvPrefix_Type = DisplayString
_F3L3TrafficBgpPeerAddressFamilyAdvPrefix_Object = MibTableColumn
f3L3TrafficBgpPeerAddressFamilyAdvPrefix = _F3L3TrafficBgpPeerAddressFamilyAdvPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 41, 1, 1),
    _F3L3TrafficBgpPeerAddressFamilyAdvPrefix_Type()
)
f3L3TrafficBgpPeerAddressFamilyAdvPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3TrafficBgpPeerAddressFamilyAdvPrefix.setStatus("current")
_F3L3TrafficBgpPeerAddressFamilyAdvPrefixStorageType_Type = StorageType
_F3L3TrafficBgpPeerAddressFamilyAdvPrefixStorageType_Object = MibTableColumn
f3L3TrafficBgpPeerAddressFamilyAdvPrefixStorageType = _F3L3TrafficBgpPeerAddressFamilyAdvPrefixStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 41, 1, 2),
    _F3L3TrafficBgpPeerAddressFamilyAdvPrefixStorageType_Type()
)
f3L3TrafficBgpPeerAddressFamilyAdvPrefixStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficBgpPeerAddressFamilyAdvPrefixStorageType.setStatus("current")
_F3L3TrafficBgpPeerAddressFamilyAdvPrefixRowStatus_Type = RowStatus
_F3L3TrafficBgpPeerAddressFamilyAdvPrefixRowStatus_Object = MibTableColumn
f3L3TrafficBgpPeerAddressFamilyAdvPrefixRowStatus = _F3L3TrafficBgpPeerAddressFamilyAdvPrefixRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 41, 1, 3),
    _F3L3TrafficBgpPeerAddressFamilyAdvPrefixRowStatus_Type()
)
f3L3TrafficBgpPeerAddressFamilyAdvPrefixRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficBgpPeerAddressFamilyAdvPrefixRowStatus.setStatus("current")
_F3L3TrafficOspfV3NeighborTable_Object = MibTable
f3L3TrafficOspfV3NeighborTable = _F3L3TrafficOspfV3NeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 42)
)
if mibBuilder.loadTexts:
    f3L3TrafficOspfV3NeighborTable.setStatus("current")
_F3L3TrafficOspfV3NeighborEntry_Object = MibTableRow
f3L3TrafficOspfV3NeighborEntry = _F3L3TrafficOspfV3NeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 42, 1)
)
f3L3TrafficOspfV3NeighborEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-L3-MIB", "f3VrfIndex"),
    (0, "F3-L3-MIB", "f3VrfOspfRouterIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficOspfV3NeighborRouterId"),
    (0, "F3-L3-MIB", "f3L3TrafficOspfV3NeighborInterfaceId"),
)
if mibBuilder.loadTexts:
    f3L3TrafficOspfV3NeighborEntry.setStatus("current")
_F3L3TrafficOspfV3NeighborRouterId_Type = IpAddress
_F3L3TrafficOspfV3NeighborRouterId_Object = MibTableColumn
f3L3TrafficOspfV3NeighborRouterId = _F3L3TrafficOspfV3NeighborRouterId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 42, 1, 1),
    _F3L3TrafficOspfV3NeighborRouterId_Type()
)
f3L3TrafficOspfV3NeighborRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficOspfV3NeighborRouterId.setStatus("current")
_F3L3TrafficOspfV3NeighborInterfaceId_Type = Unsigned32
_F3L3TrafficOspfV3NeighborInterfaceId_Object = MibTableColumn
f3L3TrafficOspfV3NeighborInterfaceId = _F3L3TrafficOspfV3NeighborInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 42, 1, 2),
    _F3L3TrafficOspfV3NeighborInterfaceId_Type()
)
f3L3TrafficOspfV3NeighborInterfaceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficOspfV3NeighborInterfaceId.setStatus("current")
_F3L3TrafficOspfV3NeighborPriority_Type = Unsigned32
_F3L3TrafficOspfV3NeighborPriority_Object = MibTableColumn
f3L3TrafficOspfV3NeighborPriority = _F3L3TrafficOspfV3NeighborPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 42, 1, 3),
    _F3L3TrafficOspfV3NeighborPriority_Type()
)
f3L3TrafficOspfV3NeighborPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficOspfV3NeighborPriority.setStatus("current")
_F3L3TrafficOspfV3NeighborDeadTime_Type = Unsigned32
_F3L3TrafficOspfV3NeighborDeadTime_Object = MibTableColumn
f3L3TrafficOspfV3NeighborDeadTime = _F3L3TrafficOspfV3NeighborDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 42, 1, 4),
    _F3L3TrafficOspfV3NeighborDeadTime_Type()
)
f3L3TrafficOspfV3NeighborDeadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficOspfV3NeighborDeadTime.setStatus("current")
_F3L3TrafficOspfV3NeighborLocalInterfaceName_Type = DisplayString
_F3L3TrafficOspfV3NeighborLocalInterfaceName_Object = MibTableColumn
f3L3TrafficOspfV3NeighborLocalInterfaceName = _F3L3TrafficOspfV3NeighborLocalInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 42, 1, 5),
    _F3L3TrafficOspfV3NeighborLocalInterfaceName_Type()
)
f3L3TrafficOspfV3NeighborLocalInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficOspfV3NeighborLocalInterfaceName.setStatus("current")
_F3L3TrafficOspfV3NeighborState_Type = OspfAdjacencyState
_F3L3TrafficOspfV3NeighborState_Object = MibTableColumn
f3L3TrafficOspfV3NeighborState = _F3L3TrafficOspfV3NeighborState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 42, 1, 6),
    _F3L3TrafficOspfV3NeighborState_Type()
)
f3L3TrafficOspfV3NeighborState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficOspfV3NeighborState.setStatus("current")
_F3L3TrafficOspfV3NeighborRole_Type = TrafficOspfRole
_F3L3TrafficOspfV3NeighborRole_Object = MibTableColumn
f3L3TrafficOspfV3NeighborRole = _F3L3TrafficOspfV3NeighborRole_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 42, 1, 7),
    _F3L3TrafficOspfV3NeighborRole_Type()
)
f3L3TrafficOspfV3NeighborRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficOspfV3NeighborRole.setStatus("current")
_F3L3TrafficOspfV3NeighborIpAddress_Type = DisplayString
_F3L3TrafficOspfV3NeighborIpAddress_Object = MibTableColumn
f3L3TrafficOspfV3NeighborIpAddress = _F3L3TrafficOspfV3NeighborIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 42, 1, 8),
    _F3L3TrafficOspfV3NeighborIpAddress_Type()
)
f3L3TrafficOspfV3NeighborIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficOspfV3NeighborIpAddress.setStatus("current")
_F3L3TrafficOspfLinkLsDbTable_Object = MibTable
f3L3TrafficOspfLinkLsDbTable = _F3L3TrafficOspfLinkLsDbTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 43)
)
if mibBuilder.loadTexts:
    f3L3TrafficOspfLinkLsDbTable.setStatus("current")
_F3L3TrafficOspfLinkLsDbEntry_Object = MibTableRow
f3L3TrafficOspfLinkLsDbEntry = _F3L3TrafficOspfLinkLsDbEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 43, 1)
)
f3L3TrafficOspfLinkLsDbEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-L3-MIB", "f3VrfIndex"),
    (0, "F3-L3-MIB", "f3VrfOspfRouterIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficOspfLinkLsDbType"),
    (0, "F3-L3-MIB", "f3L3TrafficOspfLinkLsDbId"),
    (0, "F3-L3-MIB", "f3L3TrafficOspfLinkLsDbAdvRouterId"),
    (0, "F3-L3-MIB", "f3L3TrafficOspfLinkLsDbInterfaceId"),
    (0, "F3-L3-MIB", "f3L3TrafficOspfLinkLsDbInterface"),
)
if mibBuilder.loadTexts:
    f3L3TrafficOspfLinkLsDbEntry.setStatus("current")
_F3L3TrafficOspfLinkLsDbType_Type = OspfLsaType
_F3L3TrafficOspfLinkLsDbType_Object = MibTableColumn
f3L3TrafficOspfLinkLsDbType = _F3L3TrafficOspfLinkLsDbType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 43, 1, 1),
    _F3L3TrafficOspfLinkLsDbType_Type()
)
f3L3TrafficOspfLinkLsDbType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3TrafficOspfLinkLsDbType.setStatus("current")
_F3L3TrafficOspfLinkLsDbId_Type = IpAddress
_F3L3TrafficOspfLinkLsDbId_Object = MibTableColumn
f3L3TrafficOspfLinkLsDbId = _F3L3TrafficOspfLinkLsDbId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 43, 1, 2),
    _F3L3TrafficOspfLinkLsDbId_Type()
)
f3L3TrafficOspfLinkLsDbId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3TrafficOspfLinkLsDbId.setStatus("current")
_F3L3TrafficOspfLinkLsDbAdvRouterId_Type = IpAddress
_F3L3TrafficOspfLinkLsDbAdvRouterId_Object = MibTableColumn
f3L3TrafficOspfLinkLsDbAdvRouterId = _F3L3TrafficOspfLinkLsDbAdvRouterId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 43, 1, 3),
    _F3L3TrafficOspfLinkLsDbAdvRouterId_Type()
)
f3L3TrafficOspfLinkLsDbAdvRouterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3TrafficOspfLinkLsDbAdvRouterId.setStatus("current")
_F3L3TrafficOspfLinkLsDbInterfaceId_Type = Unsigned32
_F3L3TrafficOspfLinkLsDbInterfaceId_Object = MibTableColumn
f3L3TrafficOspfLinkLsDbInterfaceId = _F3L3TrafficOspfLinkLsDbInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 43, 1, 4),
    _F3L3TrafficOspfLinkLsDbInterfaceId_Type()
)
f3L3TrafficOspfLinkLsDbInterfaceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3TrafficOspfLinkLsDbInterfaceId.setStatus("current")
_F3L3TrafficOspfLinkLsDbInterface_Type = DisplayString
_F3L3TrafficOspfLinkLsDbInterface_Object = MibTableColumn
f3L3TrafficOspfLinkLsDbInterface = _F3L3TrafficOspfLinkLsDbInterface_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 43, 1, 5),
    _F3L3TrafficOspfLinkLsDbInterface_Type()
)
f3L3TrafficOspfLinkLsDbInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3TrafficOspfLinkLsDbInterface.setStatus("current")
_F3L3TrafficOspfLinkLsDbAreaId_Type = IpAddress
_F3L3TrafficOspfLinkLsDbAreaId_Object = MibTableColumn
f3L3TrafficOspfLinkLsDbAreaId = _F3L3TrafficOspfLinkLsDbAreaId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 43, 1, 6),
    _F3L3TrafficOspfLinkLsDbAreaId_Type()
)
f3L3TrafficOspfLinkLsDbAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficOspfLinkLsDbAreaId.setStatus("current")
_F3L3TrafficOspfLinkLsDbChecksum_Type = Unsigned32
_F3L3TrafficOspfLinkLsDbChecksum_Object = MibTableColumn
f3L3TrafficOspfLinkLsDbChecksum = _F3L3TrafficOspfLinkLsDbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 43, 1, 7),
    _F3L3TrafficOspfLinkLsDbChecksum_Type()
)
f3L3TrafficOspfLinkLsDbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficOspfLinkLsDbChecksum.setStatus("current")
_F3L3TrafficOspfLinkLsDbSeqNum_Type = Unsigned32
_F3L3TrafficOspfLinkLsDbSeqNum_Object = MibTableColumn
f3L3TrafficOspfLinkLsDbSeqNum = _F3L3TrafficOspfLinkLsDbSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 43, 1, 8),
    _F3L3TrafficOspfLinkLsDbSeqNum_Type()
)
f3L3TrafficOspfLinkLsDbSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficOspfLinkLsDbSeqNum.setStatus("current")
_F3L3TrafficOspfLinkLsDbAge_Type = Unsigned32
_F3L3TrafficOspfLinkLsDbAge_Object = MibTableColumn
f3L3TrafficOspfLinkLsDbAge = _F3L3TrafficOspfLinkLsDbAge_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 43, 1, 9),
    _F3L3TrafficOspfLinkLsDbAge_Type()
)
f3L3TrafficOspfLinkLsDbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficOspfLinkLsDbAge.setStatus("current")
_F3L3TrafficOspfLinkLsDbRtrPriority_Type = Unsigned32
_F3L3TrafficOspfLinkLsDbRtrPriority_Object = MibTableColumn
f3L3TrafficOspfLinkLsDbRtrPriority = _F3L3TrafficOspfLinkLsDbRtrPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 43, 1, 10),
    _F3L3TrafficOspfLinkLsDbRtrPriority_Type()
)
f3L3TrafficOspfLinkLsDbRtrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficOspfLinkLsDbRtrPriority.setStatus("current")
_F3L3TrafficOspfLinkLsDbLinkLocalAddress_Type = DisplayString
_F3L3TrafficOspfLinkLsDbLinkLocalAddress_Object = MibTableColumn
f3L3TrafficOspfLinkLsDbLinkLocalAddress = _F3L3TrafficOspfLinkLsDbLinkLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 43, 1, 11),
    _F3L3TrafficOspfLinkLsDbLinkLocalAddress_Type()
)
f3L3TrafficOspfLinkLsDbLinkLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficOspfLinkLsDbLinkLocalAddress.setStatus("current")
_F3L3TrafficOspfLinkLsDbPrefixList_Type = DisplayString
_F3L3TrafficOspfLinkLsDbPrefixList_Object = MibTableColumn
f3L3TrafficOspfLinkLsDbPrefixList = _F3L3TrafficOspfLinkLsDbPrefixList_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 43, 1, 12),
    _F3L3TrafficOspfLinkLsDbPrefixList_Type()
)
f3L3TrafficOspfLinkLsDbPrefixList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficOspfLinkLsDbPrefixList.setStatus("current")
_F3L3TrafficIpv4StaticRouteTable_Object = MibTable
f3L3TrafficIpv4StaticRouteTable = _F3L3TrafficIpv4StaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 44)
)
if mibBuilder.loadTexts:
    f3L3TrafficIpv4StaticRouteTable.setStatus("current")
_F3L3TrafficIpv4StaticRouteEntry_Object = MibTableRow
f3L3TrafficIpv4StaticRouteEntry = _F3L3TrafficIpv4StaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 44, 1)
)
f3L3TrafficIpv4StaticRouteEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-L3-MIB", "f3VrfIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficIpv4StaticRouteDest"),
    (0, "F3-L3-MIB", "f3L3TrafficIpv4StaticRouteMask"),
    (0, "F3-L3-MIB", "f3L3TrafficIpv4StaticRouteNextHop"),
    (0, "F3-L3-MIB", "f3L3TrafficIpv4StaticRouteInterface"),
)
if mibBuilder.loadTexts:
    f3L3TrafficIpv4StaticRouteEntry.setStatus("current")
_F3L3TrafficIpv4StaticRouteDest_Type = IpAddress
_F3L3TrafficIpv4StaticRouteDest_Object = MibTableColumn
f3L3TrafficIpv4StaticRouteDest = _F3L3TrafficIpv4StaticRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 44, 1, 1),
    _F3L3TrafficIpv4StaticRouteDest_Type()
)
f3L3TrafficIpv4StaticRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3TrafficIpv4StaticRouteDest.setStatus("current")
_F3L3TrafficIpv4StaticRouteMask_Type = IpAddress
_F3L3TrafficIpv4StaticRouteMask_Object = MibTableColumn
f3L3TrafficIpv4StaticRouteMask = _F3L3TrafficIpv4StaticRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 44, 1, 2),
    _F3L3TrafficIpv4StaticRouteMask_Type()
)
f3L3TrafficIpv4StaticRouteMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3TrafficIpv4StaticRouteMask.setStatus("current")
_F3L3TrafficIpv4StaticRouteNextHop_Type = DisplayString
_F3L3TrafficIpv4StaticRouteNextHop_Object = MibTableColumn
f3L3TrafficIpv4StaticRouteNextHop = _F3L3TrafficIpv4StaticRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 44, 1, 3),
    _F3L3TrafficIpv4StaticRouteNextHop_Type()
)
f3L3TrafficIpv4StaticRouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3TrafficIpv4StaticRouteNextHop.setStatus("current")
_F3L3TrafficIpv4StaticRouteInterface_Type = DisplayString
_F3L3TrafficIpv4StaticRouteInterface_Object = MibTableColumn
f3L3TrafficIpv4StaticRouteInterface = _F3L3TrafficIpv4StaticRouteInterface_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 44, 1, 4),
    _F3L3TrafficIpv4StaticRouteInterface_Type()
)
f3L3TrafficIpv4StaticRouteInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3TrafficIpv4StaticRouteInterface.setStatus("current")
_F3L3TrafficIpv4StaticRouteMetric_Type = Integer32
_F3L3TrafficIpv4StaticRouteMetric_Object = MibTableColumn
f3L3TrafficIpv4StaticRouteMetric = _F3L3TrafficIpv4StaticRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 44, 1, 5),
    _F3L3TrafficIpv4StaticRouteMetric_Type()
)
f3L3TrafficIpv4StaticRouteMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIpv4StaticRouteMetric.setStatus("current")
_F3L3TrafficIpv4StaticRouteSourceForwardingEnable_Type = TruthValue
_F3L3TrafficIpv4StaticRouteSourceForwardingEnable_Object = MibTableColumn
f3L3TrafficIpv4StaticRouteSourceForwardingEnable = _F3L3TrafficIpv4StaticRouteSourceForwardingEnable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 44, 1, 6),
    _F3L3TrafficIpv4StaticRouteSourceForwardingEnable_Type()
)
f3L3TrafficIpv4StaticRouteSourceForwardingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIpv4StaticRouteSourceForwardingEnable.setStatus("current")
_F3L3TrafficIpv4StaticRouteStorageType_Type = StorageType
_F3L3TrafficIpv4StaticRouteStorageType_Object = MibTableColumn
f3L3TrafficIpv4StaticRouteStorageType = _F3L3TrafficIpv4StaticRouteStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 44, 1, 7),
    _F3L3TrafficIpv4StaticRouteStorageType_Type()
)
f3L3TrafficIpv4StaticRouteStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficIpv4StaticRouteStorageType.setStatus("current")
_F3L3TrafficIpv4StaticRouteRowStatus_Type = RowStatus
_F3L3TrafficIpv4StaticRouteRowStatus_Object = MibTableColumn
f3L3TrafficIpv4StaticRouteRowStatus = _F3L3TrafficIpv4StaticRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 44, 1, 8),
    _F3L3TrafficIpv4StaticRouteRowStatus_Type()
)
f3L3TrafficIpv4StaticRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficIpv4StaticRouteRowStatus.setStatus("current")
_F3L3TrafficIpv4AllRouteTable_Object = MibTable
f3L3TrafficIpv4AllRouteTable = _F3L3TrafficIpv4AllRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 45)
)
if mibBuilder.loadTexts:
    f3L3TrafficIpv4AllRouteTable.setStatus("current")
_F3L3TrafficIpv4AllRouteEntry_Object = MibTableRow
f3L3TrafficIpv4AllRouteEntry = _F3L3TrafficIpv4AllRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 45, 1)
)
f3L3TrafficIpv4AllRouteEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-L3-MIB", "f3VrfIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficIpv4AllRouteDest"),
    (0, "F3-L3-MIB", "f3L3TrafficIpv4AllRouteMask"),
    (0, "F3-L3-MIB", "f3L3TrafficIpv4AllRouteNextHop"),
    (0, "F3-L3-MIB", "f3L3TrafficIpv4AllRouteInterface"),
    (0, "F3-L3-MIB", "f3L3TrafficIpv4AllRouteOrigin"),
)
if mibBuilder.loadTexts:
    f3L3TrafficIpv4AllRouteEntry.setStatus("current")
_F3L3TrafficIpv4AllRouteDest_Type = IpAddress
_F3L3TrafficIpv4AllRouteDest_Object = MibTableColumn
f3L3TrafficIpv4AllRouteDest = _F3L3TrafficIpv4AllRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 45, 1, 1),
    _F3L3TrafficIpv4AllRouteDest_Type()
)
f3L3TrafficIpv4AllRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3TrafficIpv4AllRouteDest.setStatus("current")
_F3L3TrafficIpv4AllRouteMask_Type = IpAddress
_F3L3TrafficIpv4AllRouteMask_Object = MibTableColumn
f3L3TrafficIpv4AllRouteMask = _F3L3TrafficIpv4AllRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 45, 1, 2),
    _F3L3TrafficIpv4AllRouteMask_Type()
)
f3L3TrafficIpv4AllRouteMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3TrafficIpv4AllRouteMask.setStatus("current")
_F3L3TrafficIpv4AllRouteNextHop_Type = DisplayString
_F3L3TrafficIpv4AllRouteNextHop_Object = MibTableColumn
f3L3TrafficIpv4AllRouteNextHop = _F3L3TrafficIpv4AllRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 45, 1, 3),
    _F3L3TrafficIpv4AllRouteNextHop_Type()
)
f3L3TrafficIpv4AllRouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3TrafficIpv4AllRouteNextHop.setStatus("current")
_F3L3TrafficIpv4AllRouteInterface_Type = DisplayString
_F3L3TrafficIpv4AllRouteInterface_Object = MibTableColumn
f3L3TrafficIpv4AllRouteInterface = _F3L3TrafficIpv4AllRouteInterface_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 45, 1, 4),
    _F3L3TrafficIpv4AllRouteInterface_Type()
)
f3L3TrafficIpv4AllRouteInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3TrafficIpv4AllRouteInterface.setStatus("current")
_F3L3TrafficIpv4AllRouteOrigin_Type = TrafficIpRouteOriginType
_F3L3TrafficIpv4AllRouteOrigin_Object = MibTableColumn
f3L3TrafficIpv4AllRouteOrigin = _F3L3TrafficIpv4AllRouteOrigin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 45, 1, 5),
    _F3L3TrafficIpv4AllRouteOrigin_Type()
)
f3L3TrafficIpv4AllRouteOrigin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3TrafficIpv4AllRouteOrigin.setStatus("current")
_F3L3TrafficIpv4AllRouteMetric_Type = Integer32
_F3L3TrafficIpv4AllRouteMetric_Object = MibTableColumn
f3L3TrafficIpv4AllRouteMetric = _F3L3TrafficIpv4AllRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 45, 1, 6),
    _F3L3TrafficIpv4AllRouteMetric_Type()
)
f3L3TrafficIpv4AllRouteMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIpv4AllRouteMetric.setStatus("current")
_F3L3TrafficIpv4AllRouteSourceForwardingEnable_Type = TruthValue
_F3L3TrafficIpv4AllRouteSourceForwardingEnable_Object = MibTableColumn
f3L3TrafficIpv4AllRouteSourceForwardingEnable = _F3L3TrafficIpv4AllRouteSourceForwardingEnable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 45, 1, 7),
    _F3L3TrafficIpv4AllRouteSourceForwardingEnable_Type()
)
f3L3TrafficIpv4AllRouteSourceForwardingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIpv4AllRouteSourceForwardingEnable.setStatus("current")
_F3L3TrafficIpv4AllRouteAdminDistance_Type = Unsigned32
_F3L3TrafficIpv4AllRouteAdminDistance_Object = MibTableColumn
f3L3TrafficIpv4AllRouteAdminDistance = _F3L3TrafficIpv4AllRouteAdminDistance_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 45, 1, 8),
    _F3L3TrafficIpv4AllRouteAdminDistance_Type()
)
f3L3TrafficIpv4AllRouteAdminDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpv4AllRouteAdminDistance.setStatus("current")
_F3L3TrafficIpv4AllRouteStatus_Type = TrafficIpRouteStatusType
_F3L3TrafficIpv4AllRouteStatus_Object = MibTableColumn
f3L3TrafficIpv4AllRouteStatus = _F3L3TrafficIpv4AllRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 45, 1, 9),
    _F3L3TrafficIpv4AllRouteStatus_Type()
)
f3L3TrafficIpv4AllRouteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpv4AllRouteStatus.setStatus("current")
_F3L3TrafficIpv4AllRouteStorageType_Type = StorageType
_F3L3TrafficIpv4AllRouteStorageType_Object = MibTableColumn
f3L3TrafficIpv4AllRouteStorageType = _F3L3TrafficIpv4AllRouteStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 45, 1, 10),
    _F3L3TrafficIpv4AllRouteStorageType_Type()
)
f3L3TrafficIpv4AllRouteStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficIpv4AllRouteStorageType.setStatus("current")
_F3L3TrafficIpv4AllRouteRowStatus_Type = RowStatus
_F3L3TrafficIpv4AllRouteRowStatus_Object = MibTableColumn
f3L3TrafficIpv4AllRouteRowStatus = _F3L3TrafficIpv4AllRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 45, 1, 11),
    _F3L3TrafficIpv4AllRouteRowStatus_Type()
)
f3L3TrafficIpv4AllRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficIpv4AllRouteRowStatus.setStatus("current")
_F3L3TrafficIpv6StaticRouteTable_Object = MibTable
f3L3TrafficIpv6StaticRouteTable = _F3L3TrafficIpv6StaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 46)
)
if mibBuilder.loadTexts:
    f3L3TrafficIpv6StaticRouteTable.setStatus("current")
_F3L3TrafficIpv6StaticRouteEntry_Object = MibTableRow
f3L3TrafficIpv6StaticRouteEntry = _F3L3TrafficIpv6StaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 46, 1)
)
f3L3TrafficIpv6StaticRouteEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-L3-MIB", "f3VrfIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficIpv6StaticRouteDest"),
    (0, "F3-L3-MIB", "f3L3TrafficIpv6StaticRoutePrefixLength"),
    (0, "F3-L3-MIB", "f3L3TrafficIpv6StaticRouteNextHop"),
    (0, "F3-L3-MIB", "f3L3TrafficIpv6StaticRouteInterface"),
)
if mibBuilder.loadTexts:
    f3L3TrafficIpv6StaticRouteEntry.setStatus("current")
_F3L3TrafficIpv6StaticRouteDest_Type = Ipv6Address
_F3L3TrafficIpv6StaticRouteDest_Object = MibTableColumn
f3L3TrafficIpv6StaticRouteDest = _F3L3TrafficIpv6StaticRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 46, 1, 1),
    _F3L3TrafficIpv6StaticRouteDest_Type()
)
f3L3TrafficIpv6StaticRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3TrafficIpv6StaticRouteDest.setStatus("current")
_F3L3TrafficIpv6StaticRoutePrefixLength_Type = Integer32
_F3L3TrafficIpv6StaticRoutePrefixLength_Object = MibTableColumn
f3L3TrafficIpv6StaticRoutePrefixLength = _F3L3TrafficIpv6StaticRoutePrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 46, 1, 2),
    _F3L3TrafficIpv6StaticRoutePrefixLength_Type()
)
f3L3TrafficIpv6StaticRoutePrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3TrafficIpv6StaticRoutePrefixLength.setStatus("current")
_F3L3TrafficIpv6StaticRouteNextHop_Type = DisplayString
_F3L3TrafficIpv6StaticRouteNextHop_Object = MibTableColumn
f3L3TrafficIpv6StaticRouteNextHop = _F3L3TrafficIpv6StaticRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 46, 1, 3),
    _F3L3TrafficIpv6StaticRouteNextHop_Type()
)
f3L3TrafficIpv6StaticRouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3TrafficIpv6StaticRouteNextHop.setStatus("current")


class _F3L3TrafficIpv6StaticRouteInterface_Type(DisplayString):
    """Custom type f3L3TrafficIpv6StaticRouteInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_F3L3TrafficIpv6StaticRouteInterface_Type.__name__ = "DisplayString"
_F3L3TrafficIpv6StaticRouteInterface_Object = MibTableColumn
f3L3TrafficIpv6StaticRouteInterface = _F3L3TrafficIpv6StaticRouteInterface_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 46, 1, 4),
    _F3L3TrafficIpv6StaticRouteInterface_Type()
)
f3L3TrafficIpv6StaticRouteInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3TrafficIpv6StaticRouteInterface.setStatus("current")
_F3L3TrafficIpv6StaticRouteMetric_Type = Integer32
_F3L3TrafficIpv6StaticRouteMetric_Object = MibTableColumn
f3L3TrafficIpv6StaticRouteMetric = _F3L3TrafficIpv6StaticRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 46, 1, 5),
    _F3L3TrafficIpv6StaticRouteMetric_Type()
)
f3L3TrafficIpv6StaticRouteMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIpv6StaticRouteMetric.setStatus("current")
_F3L3TrafficIpv6StaticRouteStorageType_Type = StorageType
_F3L3TrafficIpv6StaticRouteStorageType_Object = MibTableColumn
f3L3TrafficIpv6StaticRouteStorageType = _F3L3TrafficIpv6StaticRouteStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 46, 1, 6),
    _F3L3TrafficIpv6StaticRouteStorageType_Type()
)
f3L3TrafficIpv6StaticRouteStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficIpv6StaticRouteStorageType.setStatus("current")
_F3L3TrafficIpv6StaticRouteRowStatus_Type = RowStatus
_F3L3TrafficIpv6StaticRouteRowStatus_Object = MibTableColumn
f3L3TrafficIpv6StaticRouteRowStatus = _F3L3TrafficIpv6StaticRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 46, 1, 7),
    _F3L3TrafficIpv6StaticRouteRowStatus_Type()
)
f3L3TrafficIpv6StaticRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficIpv6StaticRouteRowStatus.setStatus("current")
_F3L3TrafficIpv6AllRouteTable_Object = MibTable
f3L3TrafficIpv6AllRouteTable = _F3L3TrafficIpv6AllRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 47)
)
if mibBuilder.loadTexts:
    f3L3TrafficIpv6AllRouteTable.setStatus("current")
_F3L3TrafficIpv6AllRouteEntry_Object = MibTableRow
f3L3TrafficIpv6AllRouteEntry = _F3L3TrafficIpv6AllRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 47, 1)
)
f3L3TrafficIpv6AllRouteEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-L3-MIB", "f3VrfIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficIpv6AllRouteDest"),
    (0, "F3-L3-MIB", "f3L3TrafficIpv6AllRoutePrefixLength"),
    (0, "F3-L3-MIB", "f3L3TrafficIpv6AllRouteNextHop"),
    (0, "F3-L3-MIB", "f3L3TrafficIpv6AllRouteInterface"),
    (0, "F3-L3-MIB", "f3L3TrafficIpv6AllRouteOrigin"),
)
if mibBuilder.loadTexts:
    f3L3TrafficIpv6AllRouteEntry.setStatus("current")
_F3L3TrafficIpv6AllRouteDest_Type = Ipv6Address
_F3L3TrafficIpv6AllRouteDest_Object = MibTableColumn
f3L3TrafficIpv6AllRouteDest = _F3L3TrafficIpv6AllRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 47, 1, 1),
    _F3L3TrafficIpv6AllRouteDest_Type()
)
f3L3TrafficIpv6AllRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3TrafficIpv6AllRouteDest.setStatus("current")
_F3L3TrafficIpv6AllRoutePrefixLength_Type = Integer32
_F3L3TrafficIpv6AllRoutePrefixLength_Object = MibTableColumn
f3L3TrafficIpv6AllRoutePrefixLength = _F3L3TrafficIpv6AllRoutePrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 47, 1, 2),
    _F3L3TrafficIpv6AllRoutePrefixLength_Type()
)
f3L3TrafficIpv6AllRoutePrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3TrafficIpv6AllRoutePrefixLength.setStatus("current")
_F3L3TrafficIpv6AllRouteNextHop_Type = DisplayString
_F3L3TrafficIpv6AllRouteNextHop_Object = MibTableColumn
f3L3TrafficIpv6AllRouteNextHop = _F3L3TrafficIpv6AllRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 47, 1, 3),
    _F3L3TrafficIpv6AllRouteNextHop_Type()
)
f3L3TrafficIpv6AllRouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3TrafficIpv6AllRouteNextHop.setStatus("current")


class _F3L3TrafficIpv6AllRouteInterface_Type(DisplayString):
    """Custom type f3L3TrafficIpv6AllRouteInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_F3L3TrafficIpv6AllRouteInterface_Type.__name__ = "DisplayString"
_F3L3TrafficIpv6AllRouteInterface_Object = MibTableColumn
f3L3TrafficIpv6AllRouteInterface = _F3L3TrafficIpv6AllRouteInterface_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 47, 1, 4),
    _F3L3TrafficIpv6AllRouteInterface_Type()
)
f3L3TrafficIpv6AllRouteInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3TrafficIpv6AllRouteInterface.setStatus("current")
_F3L3TrafficIpv6AllRouteOrigin_Type = TrafficIpRouteOriginType
_F3L3TrafficIpv6AllRouteOrigin_Object = MibTableColumn
f3L3TrafficIpv6AllRouteOrigin = _F3L3TrafficIpv6AllRouteOrigin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 47, 1, 5),
    _F3L3TrafficIpv6AllRouteOrigin_Type()
)
f3L3TrafficIpv6AllRouteOrigin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3TrafficIpv6AllRouteOrigin.setStatus("current")
_F3L3TrafficIpv6AllRouteMetric_Type = Integer32
_F3L3TrafficIpv6AllRouteMetric_Object = MibTableColumn
f3L3TrafficIpv6AllRouteMetric = _F3L3TrafficIpv6AllRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 47, 1, 6),
    _F3L3TrafficIpv6AllRouteMetric_Type()
)
f3L3TrafficIpv6AllRouteMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIpv6AllRouteMetric.setStatus("current")
_F3L3TrafficIpv6AllRouteAdminDistance_Type = Unsigned32
_F3L3TrafficIpv6AllRouteAdminDistance_Object = MibTableColumn
f3L3TrafficIpv6AllRouteAdminDistance = _F3L3TrafficIpv6AllRouteAdminDistance_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 47, 1, 7),
    _F3L3TrafficIpv6AllRouteAdminDistance_Type()
)
f3L3TrafficIpv6AllRouteAdminDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpv6AllRouteAdminDistance.setStatus("current")
_F3L3TrafficIpv6AllRouteStatus_Type = TrafficIpRouteStatus
_F3L3TrafficIpv6AllRouteStatus_Object = MibTableColumn
f3L3TrafficIpv6AllRouteStatus = _F3L3TrafficIpv6AllRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 47, 1, 8),
    _F3L3TrafficIpv6AllRouteStatus_Type()
)
f3L3TrafficIpv6AllRouteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpv6AllRouteStatus.setStatus("current")
_F3L3TrafficIpv6AllRouteStorageType_Type = StorageType
_F3L3TrafficIpv6AllRouteStorageType_Object = MibTableColumn
f3L3TrafficIpv6AllRouteStorageType = _F3L3TrafficIpv6AllRouteStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 47, 1, 9),
    _F3L3TrafficIpv6AllRouteStorageType_Type()
)
f3L3TrafficIpv6AllRouteStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficIpv6AllRouteStorageType.setStatus("current")
_F3L3TrafficIpv6AllRouteRowStatus_Type = RowStatus
_F3L3TrafficIpv6AllRouteRowStatus_Object = MibTableColumn
f3L3TrafficIpv6AllRouteRowStatus = _F3L3TrafficIpv6AllRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 47, 1, 10),
    _F3L3TrafficIpv6AllRouteRowStatus_Type()
)
f3L3TrafficIpv6AllRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficIpv6AllRouteRowStatus.setStatus("current")
_F3IpPrefixListTable_Object = MibTable
f3IpPrefixListTable = _F3IpPrefixListTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 48)
)
if mibBuilder.loadTexts:
    f3IpPrefixListTable.setStatus("current")
_F3IpPrefixListEntry_Object = MibTableRow
f3IpPrefixListEntry = _F3IpPrefixListEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 48, 1)
)
f3IpPrefixListEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-L3-MIB", "f3VrfIndex"),
    (0, "F3-L3-MIB", "f3IpPrefixListIndex"),
)
if mibBuilder.loadTexts:
    f3IpPrefixListEntry.setStatus("current")
_F3IpPrefixListIndex_Type = Integer32
_F3IpPrefixListIndex_Object = MibTableColumn
f3IpPrefixListIndex = _F3IpPrefixListIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 48, 1, 1),
    _F3IpPrefixListIndex_Type()
)
f3IpPrefixListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3IpPrefixListIndex.setStatus("current")
_F3IpPrefixListName_Type = DisplayString
_F3IpPrefixListName_Object = MibTableColumn
f3IpPrefixListName = _F3IpPrefixListName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 48, 1, 2),
    _F3IpPrefixListName_Type()
)
f3IpPrefixListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3IpPrefixListName.setStatus("current")
_F3IpPrefixListDefaultDisposition_Type = IpPrefixDispositionType
_F3IpPrefixListDefaultDisposition_Object = MibTableColumn
f3IpPrefixListDefaultDisposition = _F3IpPrefixListDefaultDisposition_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 48, 1, 3),
    _F3IpPrefixListDefaultDisposition_Type()
)
f3IpPrefixListDefaultDisposition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3IpPrefixListDefaultDisposition.setStatus("current")
_F3IpPrefixListStorageType_Type = StorageType
_F3IpPrefixListStorageType_Object = MibTableColumn
f3IpPrefixListStorageType = _F3IpPrefixListStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 48, 1, 4),
    _F3IpPrefixListStorageType_Type()
)
f3IpPrefixListStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3IpPrefixListStorageType.setStatus("current")
_F3IpPrefixListRowStatus_Type = RowStatus
_F3IpPrefixListRowStatus_Object = MibTableColumn
f3IpPrefixListRowStatus = _F3IpPrefixListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 48, 1, 5),
    _F3IpPrefixListRowStatus_Type()
)
f3IpPrefixListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3IpPrefixListRowStatus.setStatus("current")
_F3IpPrefixTable_Object = MibTable
f3IpPrefixTable = _F3IpPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 49)
)
if mibBuilder.loadTexts:
    f3IpPrefixTable.setStatus("current")
_F3IpPrefixEntry_Object = MibTableRow
f3IpPrefixEntry = _F3IpPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 49, 1)
)
f3IpPrefixEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-L3-MIB", "f3VrfIndex"),
    (0, "F3-L3-MIB", "f3IpPrefixListIndex"),
    (0, "F3-L3-MIB", "f3IpPrefixIndex"),
)
if mibBuilder.loadTexts:
    f3IpPrefixEntry.setStatus("current")
_F3IpPrefixIndex_Type = Integer32
_F3IpPrefixIndex_Object = MibTableColumn
f3IpPrefixIndex = _F3IpPrefixIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 49, 1, 1),
    _F3IpPrefixIndex_Type()
)
f3IpPrefixIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3IpPrefixIndex.setStatus("current")
_F3IpPrefix_Type = DisplayString
_F3IpPrefix_Object = MibTableColumn
f3IpPrefix = _F3IpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 49, 1, 2),
    _F3IpPrefix_Type()
)
f3IpPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3IpPrefix.setStatus("current")
_F3IpPrefixPriority_Type = Unsigned32
_F3IpPrefixPriority_Object = MibTableColumn
f3IpPrefixPriority = _F3IpPrefixPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 49, 1, 3),
    _F3IpPrefixPriority_Type()
)
f3IpPrefixPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3IpPrefixPriority.setStatus("current")
_F3IpPrefixDisposition_Type = IpPrefixDispositionType
_F3IpPrefixDisposition_Object = MibTableColumn
f3IpPrefixDisposition = _F3IpPrefixDisposition_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 49, 1, 4),
    _F3IpPrefixDisposition_Type()
)
f3IpPrefixDisposition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3IpPrefixDisposition.setStatus("current")
_F3IpPrefixLessOrEqualPrefixLen_Type = Integer32
_F3IpPrefixLessOrEqualPrefixLen_Object = MibTableColumn
f3IpPrefixLessOrEqualPrefixLen = _F3IpPrefixLessOrEqualPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 49, 1, 5),
    _F3IpPrefixLessOrEqualPrefixLen_Type()
)
f3IpPrefixLessOrEqualPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3IpPrefixLessOrEqualPrefixLen.setStatus("current")
_F3IpPrefixGreaterOrEqualPrefixLen_Type = Integer32
_F3IpPrefixGreaterOrEqualPrefixLen_Object = MibTableColumn
f3IpPrefixGreaterOrEqualPrefixLen = _F3IpPrefixGreaterOrEqualPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 49, 1, 6),
    _F3IpPrefixGreaterOrEqualPrefixLen_Type()
)
f3IpPrefixGreaterOrEqualPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3IpPrefixGreaterOrEqualPrefixLen.setStatus("current")
_F3IpPrefixStorageType_Type = StorageType
_F3IpPrefixStorageType_Object = MibTableColumn
f3IpPrefixStorageType = _F3IpPrefixStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 49, 1, 7),
    _F3IpPrefixStorageType_Type()
)
f3IpPrefixStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3IpPrefixStorageType.setStatus("current")
_F3IpPrefixRowStatus_Type = RowStatus
_F3IpPrefixRowStatus_Object = MibTableColumn
f3IpPrefixRowStatus = _F3IpPrefixRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 49, 1, 8),
    _F3IpPrefixRowStatus_Type()
)
f3IpPrefixRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3IpPrefixRowStatus.setStatus("current")
_F3L3TrafficIPInterfaceRAPrefixTable_Object = MibTable
f3L3TrafficIPInterfaceRAPrefixTable = _F3L3TrafficIPInterfaceRAPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 50)
)
if mibBuilder.loadTexts:
    f3L3TrafficIPInterfaceRAPrefixTable.setStatus("current")
_F3L3TrafficIPInterfaceRAPrefixEntry_Object = MibTableRow
f3L3TrafficIPInterfaceRAPrefixEntry = _F3L3TrafficIPInterfaceRAPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 50, 1)
)
f3L3TrafficIPInterfaceRAPrefixEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficIPIfIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficIPInterfaceRAPrefixIndex"),
)
if mibBuilder.loadTexts:
    f3L3TrafficIPInterfaceRAPrefixEntry.setStatus("current")
_F3L3TrafficIPInterfaceRAPrefixIndex_Type = Integer32
_F3L3TrafficIPInterfaceRAPrefixIndex_Object = MibTableColumn
f3L3TrafficIPInterfaceRAPrefixIndex = _F3L3TrafficIPInterfaceRAPrefixIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 50, 1, 1),
    _F3L3TrafficIPInterfaceRAPrefixIndex_Type()
)
f3L3TrafficIPInterfaceRAPrefixIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3TrafficIPInterfaceRAPrefixIndex.setStatus("current")
_F3L3TrafficIPInterfaceRAPrefixAdvertiseEnabled_Type = TruthValue
_F3L3TrafficIPInterfaceRAPrefixAdvertiseEnabled_Object = MibTableColumn
f3L3TrafficIPInterfaceRAPrefixAdvertiseEnabled = _F3L3TrafficIPInterfaceRAPrefixAdvertiseEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 50, 1, 2),
    _F3L3TrafficIPInterfaceRAPrefixAdvertiseEnabled_Type()
)
f3L3TrafficIPInterfaceRAPrefixAdvertiseEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPInterfaceRAPrefixAdvertiseEnabled.setStatus("current")
_F3L3TrafficIPInterfaceRAPrefix_Type = Ipv6Address
_F3L3TrafficIPInterfaceRAPrefix_Object = MibTableColumn
f3L3TrafficIPInterfaceRAPrefix = _F3L3TrafficIPInterfaceRAPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 50, 1, 3),
    _F3L3TrafficIPInterfaceRAPrefix_Type()
)
f3L3TrafficIPInterfaceRAPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPInterfaceRAPrefix.setStatus("current")
_F3L3TrafficIPInterfaceRAPrefixLength_Type = Integer32
_F3L3TrafficIPInterfaceRAPrefixLength_Object = MibTableColumn
f3L3TrafficIPInterfaceRAPrefixLength = _F3L3TrafficIPInterfaceRAPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 50, 1, 4),
    _F3L3TrafficIPInterfaceRAPrefixLength_Type()
)
f3L3TrafficIPInterfaceRAPrefixLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPInterfaceRAPrefixLength.setStatus("current")
_F3L3TrafficIPInterfaceRAPrefixValidLifeTime_Type = Unsigned32
_F3L3TrafficIPInterfaceRAPrefixValidLifeTime_Object = MibTableColumn
f3L3TrafficIPInterfaceRAPrefixValidLifeTime = _F3L3TrafficIPInterfaceRAPrefixValidLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 50, 1, 5),
    _F3L3TrafficIPInterfaceRAPrefixValidLifeTime_Type()
)
f3L3TrafficIPInterfaceRAPrefixValidLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPInterfaceRAPrefixValidLifeTime.setStatus("current")
_F3L3TrafficIPInterfaceRAPrefixPreferredLifeTime_Type = Unsigned32
_F3L3TrafficIPInterfaceRAPrefixPreferredLifeTime_Object = MibTableColumn
f3L3TrafficIPInterfaceRAPrefixPreferredLifeTime = _F3L3TrafficIPInterfaceRAPrefixPreferredLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 50, 1, 6),
    _F3L3TrafficIPInterfaceRAPrefixPreferredLifeTime_Type()
)
f3L3TrafficIPInterfaceRAPrefixPreferredLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPInterfaceRAPrefixPreferredLifeTime.setStatus("current")
_F3L3TrafficIPInterfaceRAPrefixStorageType_Type = StorageType
_F3L3TrafficIPInterfaceRAPrefixStorageType_Object = MibTableColumn
f3L3TrafficIPInterfaceRAPrefixStorageType = _F3L3TrafficIPInterfaceRAPrefixStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 50, 1, 7),
    _F3L3TrafficIPInterfaceRAPrefixStorageType_Type()
)
f3L3TrafficIPInterfaceRAPrefixStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficIPInterfaceRAPrefixStorageType.setStatus("current")
_F3L3TrafficIPInterfaceRAPrefixRowStatus_Type = RowStatus
_F3L3TrafficIPInterfaceRAPrefixRowStatus_Object = MibTableColumn
f3L3TrafficIPInterfaceRAPrefixRowStatus = _F3L3TrafficIPInterfaceRAPrefixRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 50, 1, 8),
    _F3L3TrafficIPInterfaceRAPrefixRowStatus_Type()
)
f3L3TrafficIPInterfaceRAPrefixRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficIPInterfaceRAPrefixRowStatus.setStatus("current")
_F3L3TrafficIPInterfaceNdpTable_Object = MibTable
f3L3TrafficIPInterfaceNdpTable = _F3L3TrafficIPInterfaceNdpTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 51)
)
if mibBuilder.loadTexts:
    f3L3TrafficIPInterfaceNdpTable.setStatus("current")
_F3L3TrafficIPInterfaceNdpEntry_Object = MibTableRow
f3L3TrafficIPInterfaceNdpEntry = _F3L3TrafficIPInterfaceNdpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 51, 1)
)
f3L3TrafficIPInterfaceNdpEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficIPv6IfIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficIPv6NdpIPv6Addr"),
)
if mibBuilder.loadTexts:
    f3L3TrafficIPInterfaceNdpEntry.setStatus("current")
_F3L3TrafficIPInterfaceNdpIPv6Addr_Type = Ipv6Address
_F3L3TrafficIPInterfaceNdpIPv6Addr_Object = MibTableColumn
f3L3TrafficIPInterfaceNdpIPv6Addr = _F3L3TrafficIPInterfaceNdpIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 51, 1, 1),
    _F3L3TrafficIPInterfaceNdpIPv6Addr_Type()
)
f3L3TrafficIPInterfaceNdpIPv6Addr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3TrafficIPInterfaceNdpIPv6Addr.setStatus("current")


class _F3L3TrafficIPInterfaceNdpInterface_Type(DisplayString):
    """Custom type f3L3TrafficIPInterfaceNdpInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_F3L3TrafficIPInterfaceNdpInterface_Type.__name__ = "DisplayString"
_F3L3TrafficIPInterfaceNdpInterface_Object = MibTableColumn
f3L3TrafficIPInterfaceNdpInterface = _F3L3TrafficIPInterfaceNdpInterface_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 51, 1, 2),
    _F3L3TrafficIPInterfaceNdpInterface_Type()
)
f3L3TrafficIPInterfaceNdpInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficIPInterfaceNdpInterface.setStatus("current")
_F3L3TrafficIPInterfaceNdpMacAddress_Type = MacAddress
_F3L3TrafficIPInterfaceNdpMacAddress_Object = MibTableColumn
f3L3TrafficIPInterfaceNdpMacAddress = _F3L3TrafficIPInterfaceNdpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 51, 1, 3),
    _F3L3TrafficIPInterfaceNdpMacAddress_Type()
)
f3L3TrafficIPInterfaceNdpMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficIPInterfaceNdpMacAddress.setStatus("current")
_F3L3TrafficIPInterfaceNdpType_Type = IpEntryType
_F3L3TrafficIPInterfaceNdpType_Object = MibTableColumn
f3L3TrafficIPInterfaceNdpType = _F3L3TrafficIPInterfaceNdpType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 51, 1, 4),
    _F3L3TrafficIPInterfaceNdpType_Type()
)
f3L3TrafficIPInterfaceNdpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficIPInterfaceNdpType.setStatus("current")
_F3L3TrafficIPInterfaceNdpReachabilityState_Type = NdpNeighborReachabilityState
_F3L3TrafficIPInterfaceNdpReachabilityState_Object = MibTableColumn
f3L3TrafficIPInterfaceNdpReachabilityState = _F3L3TrafficIPInterfaceNdpReachabilityState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 51, 1, 5),
    _F3L3TrafficIPInterfaceNdpReachabilityState_Type()
)
f3L3TrafficIPInterfaceNdpReachabilityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIPInterfaceNdpReachabilityState.setStatus("current")
_F3L3TrafficIPInterfaceNdpAge_Type = Integer32
_F3L3TrafficIPInterfaceNdpAge_Object = MibTableColumn
f3L3TrafficIPInterfaceNdpAge = _F3L3TrafficIPInterfaceNdpAge_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 51, 1, 6),
    _F3L3TrafficIPInterfaceNdpAge_Type()
)
f3L3TrafficIPInterfaceNdpAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIPInterfaceNdpAge.setStatus("current")
_F3L3TrafficIPInterfaceNdpStorageType_Type = StorageType
_F3L3TrafficIPInterfaceNdpStorageType_Object = MibTableColumn
f3L3TrafficIPInterfaceNdpStorageType = _F3L3TrafficIPInterfaceNdpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 51, 1, 7),
    _F3L3TrafficIPInterfaceNdpStorageType_Type()
)
f3L3TrafficIPInterfaceNdpStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficIPInterfaceNdpStorageType.setStatus("current")
_F3L3TrafficIPInterfaceNdpRowStatus_Type = RowStatus
_F3L3TrafficIPInterfaceNdpRowStatus_Object = MibTableColumn
f3L3TrafficIPInterfaceNdpRowStatus = _F3L3TrafficIPInterfaceNdpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 51, 1, 8),
    _F3L3TrafficIPInterfaceNdpRowStatus_Type()
)
f3L3TrafficIPInterfaceNdpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficIPInterfaceNdpRowStatus.setStatus("current")
_F3L3TrafficIPInterfaceIPv6AddressTable_Object = MibTable
f3L3TrafficIPInterfaceIPv6AddressTable = _F3L3TrafficIPInterfaceIPv6AddressTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 52)
)
if mibBuilder.loadTexts:
    f3L3TrafficIPInterfaceIPv6AddressTable.setStatus("current")
_F3L3TrafficIPInterfaceIPv6AddressEntry_Object = MibTableRow
f3L3TrafficIPInterfaceIPv6AddressEntry = _F3L3TrafficIPInterfaceIPv6AddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 52, 1)
)
f3L3TrafficIPInterfaceIPv6AddressEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficIPIfIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficIPInterfaceIPv6AddressIndex"),
)
if mibBuilder.loadTexts:
    f3L3TrafficIPInterfaceIPv6AddressEntry.setStatus("current")
_F3L3TrafficIPInterfaceIPv6AddressIndex_Type = Integer32
_F3L3TrafficIPInterfaceIPv6AddressIndex_Object = MibTableColumn
f3L3TrafficIPInterfaceIPv6AddressIndex = _F3L3TrafficIPInterfaceIPv6AddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 52, 1, 1),
    _F3L3TrafficIPInterfaceIPv6AddressIndex_Type()
)
f3L3TrafficIPInterfaceIPv6AddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3L3TrafficIPInterfaceIPv6AddressIndex.setStatus("current")
_F3L3TrafficIPInterfaceIPv6AddressAssignMode_Type = Ipv6AddressAssignMode
_F3L3TrafficIPInterfaceIPv6AddressAssignMode_Object = MibTableColumn
f3L3TrafficIPInterfaceIPv6AddressAssignMode = _F3L3TrafficIPInterfaceIPv6AddressAssignMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 52, 1, 2),
    _F3L3TrafficIPInterfaceIPv6AddressAssignMode_Type()
)
f3L3TrafficIPInterfaceIPv6AddressAssignMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPInterfaceIPv6AddressAssignMode.setStatus("current")
_F3L3TrafficIPInterfaceIPv6AddressUnicastAddr_Type = Ipv6Address
_F3L3TrafficIPInterfaceIPv6AddressUnicastAddr_Object = MibTableColumn
f3L3TrafficIPInterfaceIPv6AddressUnicastAddr = _F3L3TrafficIPInterfaceIPv6AddressUnicastAddr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 52, 1, 3),
    _F3L3TrafficIPInterfaceIPv6AddressUnicastAddr_Type()
)
f3L3TrafficIPInterfaceIPv6AddressUnicastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPInterfaceIPv6AddressUnicastAddr.setStatus("current")
_F3L3TrafficIPInterfaceIPv6AddressUnicastAddrPrefixLength_Type = Integer32
_F3L3TrafficIPInterfaceIPv6AddressUnicastAddrPrefixLength_Object = MibTableColumn
f3L3TrafficIPInterfaceIPv6AddressUnicastAddrPrefixLength = _F3L3TrafficIPInterfaceIPv6AddressUnicastAddrPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 52, 1, 4),
    _F3L3TrafficIPInterfaceIPv6AddressUnicastAddrPrefixLength_Type()
)
f3L3TrafficIPInterfaceIPv6AddressUnicastAddrPrefixLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPInterfaceIPv6AddressUnicastAddrPrefixLength.setStatus("current")
_F3L3TrafficIPInterfaceIPv6AddressUnicastAddrAutoGenPrefix_Type = DisplayString
_F3L3TrafficIPInterfaceIPv6AddressUnicastAddrAutoGenPrefix_Object = MibTableColumn
f3L3TrafficIPInterfaceIPv6AddressUnicastAddrAutoGenPrefix = _F3L3TrafficIPInterfaceIPv6AddressUnicastAddrAutoGenPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 52, 1, 5),
    _F3L3TrafficIPInterfaceIPv6AddressUnicastAddrAutoGenPrefix_Type()
)
f3L3TrafficIPInterfaceIPv6AddressUnicastAddrAutoGenPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPInterfaceIPv6AddressUnicastAddrAutoGenPrefix.setStatus("current")
_F3L3TrafficIPInterfaceIPv6AddressStorageType_Type = StorageType
_F3L3TrafficIPInterfaceIPv6AddressStorageType_Object = MibTableColumn
f3L3TrafficIPInterfaceIPv6AddressStorageType = _F3L3TrafficIPInterfaceIPv6AddressStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 52, 1, 6),
    _F3L3TrafficIPInterfaceIPv6AddressStorageType_Type()
)
f3L3TrafficIPInterfaceIPv6AddressStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficIPInterfaceIPv6AddressStorageType.setStatus("current")
_F3L3TrafficIPInterfaceIPv6AddressRowStatus_Type = RowStatus
_F3L3TrafficIPInterfaceIPv6AddressRowStatus_Object = MibTableColumn
f3L3TrafficIPInterfaceIPv6AddressRowStatus = _F3L3TrafficIPInterfaceIPv6AddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 1, 52, 1, 7),
    _F3L3TrafficIPInterfaceIPv6AddressRowStatus_Type()
)
f3L3TrafficIPInterfaceIPv6AddressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3L3TrafficIPInterfaceIPv6AddressRowStatus.setStatus("current")
_F3L3Performance_ObjectIdentity = ObjectIdentity
f3L3Performance = _F3L3Performance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2)
)
_F3L3FlowPointStatsTable_Object = MibTable
f3L3FlowPointStatsTable = _F3L3FlowPointStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 1)
)
if mibBuilder.loadTexts:
    f3L3FlowPointStatsTable.setStatus("current")
_F3L3FlowPointStatsEntry_Object = MibTableRow
f3L3FlowPointStatsEntry = _F3L3FlowPointStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 1, 1)
)
f3L3FlowPointStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortTypeIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointStatsIndex"),
)
if mibBuilder.loadTexts:
    f3L3FlowPointStatsEntry.setStatus("current")


class _F3L3FlowPointStatsIndex_Type(Integer32):
    """Custom type f3L3FlowPointStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_F3L3FlowPointStatsIndex_Type.__name__ = "Integer32"
_F3L3FlowPointStatsIndex_Object = MibTableColumn
f3L3FlowPointStatsIndex = _F3L3FlowPointStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 1, 1, 1),
    _F3L3FlowPointStatsIndex_Type()
)
f3L3FlowPointStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointStatsIndex.setStatus("current")
_F3L3FlowPointStatsIntervalType_Type = CmPmIntervalType
_F3L3FlowPointStatsIntervalType_Object = MibTableColumn
f3L3FlowPointStatsIntervalType = _F3L3FlowPointStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 1, 1, 2),
    _F3L3FlowPointStatsIntervalType_Type()
)
f3L3FlowPointStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointStatsIntervalType.setStatus("current")
_F3L3FlowPointStatsValid_Type = TruthValue
_F3L3FlowPointStatsValid_Object = MibTableColumn
f3L3FlowPointStatsValid = _F3L3FlowPointStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 1, 1, 3),
    _F3L3FlowPointStatsValid_Type()
)
f3L3FlowPointStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointStatsValid.setStatus("current")
_F3L3FlowPointStatsAction_Type = CmPmBinAction
_F3L3FlowPointStatsAction_Object = MibTableColumn
f3L3FlowPointStatsAction = _F3L3FlowPointStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 1, 1, 4),
    _F3L3FlowPointStatsAction_Type()
)
f3L3FlowPointStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3FlowPointStatsAction.setStatus("current")
_F3L3FlowPointStatsFMG_Type = PerfCounter64
_F3L3FlowPointStatsFMG_Object = MibTableColumn
f3L3FlowPointStatsFMG = _F3L3FlowPointStatsFMG_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 1, 1, 5),
    _F3L3FlowPointStatsFMG_Type()
)
f3L3FlowPointStatsFMG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointStatsFMG.setStatus("current")
_F3L3FlowPointStatsFMY_Type = PerfCounter64
_F3L3FlowPointStatsFMY_Object = MibTableColumn
f3L3FlowPointStatsFMY = _F3L3FlowPointStatsFMY_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 1, 1, 6),
    _F3L3FlowPointStatsFMY_Type()
)
f3L3FlowPointStatsFMY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointStatsFMY.setStatus("current")
_F3L3FlowPointStatsFMRD_Type = PerfCounter64
_F3L3FlowPointStatsFMRD_Object = MibTableColumn
f3L3FlowPointStatsFMRD = _F3L3FlowPointStatsFMRD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 1, 1, 7),
    _F3L3FlowPointStatsFMRD_Type()
)
f3L3FlowPointStatsFMRD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointStatsFMRD.setStatus("current")
_F3L3FlowPointStatsFTD_Type = PerfCounter64
_F3L3FlowPointStatsFTD_Object = MibTableColumn
f3L3FlowPointStatsFTD = _F3L3FlowPointStatsFTD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 1, 1, 8),
    _F3L3FlowPointStatsFTD_Type()
)
f3L3FlowPointStatsFTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointStatsFTD.setStatus("current")
_F3L3FlowPointStatsFragmentedDropAcl_Type = PerfCounter64
_F3L3FlowPointStatsFragmentedDropAcl_Object = MibTableColumn
f3L3FlowPointStatsFragmentedDropAcl = _F3L3FlowPointStatsFragmentedDropAcl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 1, 1, 9),
    _F3L3FlowPointStatsFragmentedDropAcl_Type()
)
f3L3FlowPointStatsFragmentedDropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointStatsFragmentedDropAcl.setStatus("current")
_F3L3FlowPointStatsAclRuleDrop_Type = PerfCounter64
_F3L3FlowPointStatsAclRuleDrop_Object = MibTableColumn
f3L3FlowPointStatsAclRuleDrop = _F3L3FlowPointStatsAclRuleDrop_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 1, 1, 10),
    _F3L3FlowPointStatsAclRuleDrop_Type()
)
f3L3FlowPointStatsAclRuleDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointStatsAclRuleDrop.setStatus("current")
_F3L3FlowPointStatsTtlEqual1Drop_Type = PerfCounter64
_F3L3FlowPointStatsTtlEqual1Drop_Object = MibTableColumn
f3L3FlowPointStatsTtlEqual1Drop = _F3L3FlowPointStatsTtlEqual1Drop_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 1, 1, 11),
    _F3L3FlowPointStatsTtlEqual1Drop_Type()
)
f3L3FlowPointStatsTtlEqual1Drop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointStatsTtlEqual1Drop.setStatus("current")
_F3L3FlowPointStatsFrameTx_Type = PerfCounter64
_F3L3FlowPointStatsFrameTx_Object = MibTableColumn
f3L3FlowPointStatsFrameTx = _F3L3FlowPointStatsFrameTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 1, 1, 12),
    _F3L3FlowPointStatsFrameTx_Type()
)
f3L3FlowPointStatsFrameTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointStatsFrameTx.setStatus("current")
_F3L3FlowPointStatsFrameRx_Type = PerfCounter64
_F3L3FlowPointStatsFrameRx_Object = MibTableColumn
f3L3FlowPointStatsFrameRx = _F3L3FlowPointStatsFrameRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 1, 1, 13),
    _F3L3FlowPointStatsFrameRx_Type()
)
f3L3FlowPointStatsFrameRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointStatsFrameRx.setStatus("current")
_F3L3FlowPointStatsNoRouteDrop_Type = PerfCounter64
_F3L3FlowPointStatsNoRouteDrop_Object = MibTableColumn
f3L3FlowPointStatsNoRouteDrop = _F3L3FlowPointStatsNoRouteDrop_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 1, 1, 14),
    _F3L3FlowPointStatsNoRouteDrop_Type()
)
f3L3FlowPointStatsNoRouteDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointStatsNoRouteDrop.setStatus("current")
_F3L3FlowPointStatsHopLimitDrop_Type = PerfCounter64
_F3L3FlowPointStatsHopLimitDrop_Object = MibTableColumn
f3L3FlowPointStatsHopLimitDrop = _F3L3FlowPointStatsHopLimitDrop_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 1, 1, 15),
    _F3L3FlowPointStatsHopLimitDrop_Type()
)
f3L3FlowPointStatsHopLimitDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointStatsHopLimitDrop.setStatus("current")
_F3L3FlowPointHistoryTable_Object = MibTable
f3L3FlowPointHistoryTable = _F3L3FlowPointHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 2)
)
if mibBuilder.loadTexts:
    f3L3FlowPointHistoryTable.setStatus("current")
_F3L3FlowPointHistoryEntry_Object = MibTableRow
f3L3FlowPointHistoryEntry = _F3L3FlowPointHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 2, 1)
)
f3L3FlowPointHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortTypeIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointStatsIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointHistoryIndex"),
)
if mibBuilder.loadTexts:
    f3L3FlowPointHistoryEntry.setStatus("current")


class _F3L3FlowPointHistoryIndex_Type(Integer32):
    """Custom type f3L3FlowPointHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3L3FlowPointHistoryIndex_Type.__name__ = "Integer32"
_F3L3FlowPointHistoryIndex_Object = MibTableColumn
f3L3FlowPointHistoryIndex = _F3L3FlowPointHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 2, 1, 1),
    _F3L3FlowPointHistoryIndex_Type()
)
f3L3FlowPointHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointHistoryIndex.setStatus("current")
_F3L3FlowPointHistoryTime_Type = DateAndTime
_F3L3FlowPointHistoryTime_Object = MibTableColumn
f3L3FlowPointHistoryTime = _F3L3FlowPointHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 2, 1, 2),
    _F3L3FlowPointHistoryTime_Type()
)
f3L3FlowPointHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointHistoryTime.setStatus("current")
_F3L3FlowPointHistoryValid_Type = TruthValue
_F3L3FlowPointHistoryValid_Object = MibTableColumn
f3L3FlowPointHistoryValid = _F3L3FlowPointHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 2, 1, 3),
    _F3L3FlowPointHistoryValid_Type()
)
f3L3FlowPointHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointHistoryValid.setStatus("current")
_F3L3FlowPointHistoryAction_Type = CmPmBinAction
_F3L3FlowPointHistoryAction_Object = MibTableColumn
f3L3FlowPointHistoryAction = _F3L3FlowPointHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 2, 1, 4),
    _F3L3FlowPointHistoryAction_Type()
)
f3L3FlowPointHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3FlowPointHistoryAction.setStatus("current")
_F3L3FlowPointHistoryFMG_Type = PerfCounter64
_F3L3FlowPointHistoryFMG_Object = MibTableColumn
f3L3FlowPointHistoryFMG = _F3L3FlowPointHistoryFMG_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 2, 1, 5),
    _F3L3FlowPointHistoryFMG_Type()
)
f3L3FlowPointHistoryFMG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointHistoryFMG.setStatus("current")
_F3L3FlowPointHistoryFMY_Type = PerfCounter64
_F3L3FlowPointHistoryFMY_Object = MibTableColumn
f3L3FlowPointHistoryFMY = _F3L3FlowPointHistoryFMY_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 2, 1, 6),
    _F3L3FlowPointHistoryFMY_Type()
)
f3L3FlowPointHistoryFMY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointHistoryFMY.setStatus("current")
_F3L3FlowPointHistoryFMRD_Type = PerfCounter64
_F3L3FlowPointHistoryFMRD_Object = MibTableColumn
f3L3FlowPointHistoryFMRD = _F3L3FlowPointHistoryFMRD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 2, 1, 7),
    _F3L3FlowPointHistoryFMRD_Type()
)
f3L3FlowPointHistoryFMRD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointHistoryFMRD.setStatus("current")
_F3L3FlowPointHistoryFTD_Type = PerfCounter64
_F3L3FlowPointHistoryFTD_Object = MibTableColumn
f3L3FlowPointHistoryFTD = _F3L3FlowPointHistoryFTD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 2, 1, 8),
    _F3L3FlowPointHistoryFTD_Type()
)
f3L3FlowPointHistoryFTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointHistoryFTD.setStatus("current")
_F3L3FlowPointHistoryFragmentedDropAcl_Type = PerfCounter64
_F3L3FlowPointHistoryFragmentedDropAcl_Object = MibTableColumn
f3L3FlowPointHistoryFragmentedDropAcl = _F3L3FlowPointHistoryFragmentedDropAcl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 2, 1, 9),
    _F3L3FlowPointHistoryFragmentedDropAcl_Type()
)
f3L3FlowPointHistoryFragmentedDropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointHistoryFragmentedDropAcl.setStatus("current")
_F3L3FlowPointHistoryAclRuleDrop_Type = PerfCounter64
_F3L3FlowPointHistoryAclRuleDrop_Object = MibTableColumn
f3L3FlowPointHistoryAclRuleDrop = _F3L3FlowPointHistoryAclRuleDrop_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 2, 1, 10),
    _F3L3FlowPointHistoryAclRuleDrop_Type()
)
f3L3FlowPointHistoryAclRuleDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointHistoryAclRuleDrop.setStatus("current")
_F3L3FlowPointHistoryTtlEqual1Drop_Type = PerfCounter64
_F3L3FlowPointHistoryTtlEqual1Drop_Object = MibTableColumn
f3L3FlowPointHistoryTtlEqual1Drop = _F3L3FlowPointHistoryTtlEqual1Drop_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 2, 1, 11),
    _F3L3FlowPointHistoryTtlEqual1Drop_Type()
)
f3L3FlowPointHistoryTtlEqual1Drop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointHistoryTtlEqual1Drop.setStatus("current")
_F3L3FlowPointHistoryFrameTx_Type = PerfCounter64
_F3L3FlowPointHistoryFrameTx_Object = MibTableColumn
f3L3FlowPointHistoryFrameTx = _F3L3FlowPointHistoryFrameTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 2, 1, 12),
    _F3L3FlowPointHistoryFrameTx_Type()
)
f3L3FlowPointHistoryFrameTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointHistoryFrameTx.setStatus("current")
_F3L3FlowPointHistoryFrameRx_Type = PerfCounter64
_F3L3FlowPointHistoryFrameRx_Object = MibTableColumn
f3L3FlowPointHistoryFrameRx = _F3L3FlowPointHistoryFrameRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 2, 1, 13),
    _F3L3FlowPointHistoryFrameRx_Type()
)
f3L3FlowPointHistoryFrameRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointHistoryFrameRx.setStatus("current")
_F3L3FlowPointHistoryNoRouteDrop_Type = PerfCounter64
_F3L3FlowPointHistoryNoRouteDrop_Object = MibTableColumn
f3L3FlowPointHistoryNoRouteDrop = _F3L3FlowPointHistoryNoRouteDrop_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 2, 1, 14),
    _F3L3FlowPointHistoryNoRouteDrop_Type()
)
f3L3FlowPointHistoryNoRouteDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointHistoryNoRouteDrop.setStatus("current")
_F3L3FlowPointHistoryHopLimitDrop_Type = PerfCounter64
_F3L3FlowPointHistoryHopLimitDrop_Object = MibTableColumn
f3L3FlowPointHistoryHopLimitDrop = _F3L3FlowPointHistoryHopLimitDrop_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 2, 1, 15),
    _F3L3FlowPointHistoryHopLimitDrop_Type()
)
f3L3FlowPointHistoryHopLimitDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointHistoryHopLimitDrop.setStatus("current")
_F3L3FlowPointThresholdTable_Object = MibTable
f3L3FlowPointThresholdTable = _F3L3FlowPointThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 3)
)
if mibBuilder.loadTexts:
    f3L3FlowPointThresholdTable.setStatus("current")
_F3L3FlowPointThresholdEntry_Object = MibTableRow
f3L3FlowPointThresholdEntry = _F3L3FlowPointThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 3, 1)
)
f3L3FlowPointThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortTypeIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointStatsIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointThresholdIndex"),
)
if mibBuilder.loadTexts:
    f3L3FlowPointThresholdEntry.setStatus("current")


class _F3L3FlowPointThresholdIndex_Type(Integer32):
    """Custom type f3L3FlowPointThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3L3FlowPointThresholdIndex_Type.__name__ = "Integer32"
_F3L3FlowPointThresholdIndex_Object = MibTableColumn
f3L3FlowPointThresholdIndex = _F3L3FlowPointThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 3, 1, 1),
    _F3L3FlowPointThresholdIndex_Type()
)
f3L3FlowPointThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointThresholdIndex.setStatus("current")
_F3L3FlowPointThresholdInterval_Type = CmPmIntervalType
_F3L3FlowPointThresholdInterval_Object = MibTableColumn
f3L3FlowPointThresholdInterval = _F3L3FlowPointThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 3, 1, 2),
    _F3L3FlowPointThresholdInterval_Type()
)
f3L3FlowPointThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointThresholdInterval.setStatus("current")
_F3L3FlowPointThresholdVariable_Type = VariablePointer
_F3L3FlowPointThresholdVariable_Object = MibTableColumn
f3L3FlowPointThresholdVariable = _F3L3FlowPointThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 3, 1, 3),
    _F3L3FlowPointThresholdVariable_Type()
)
f3L3FlowPointThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointThresholdVariable.setStatus("current")
_F3L3FlowPointThresholdValueLo_Type = Unsigned32
_F3L3FlowPointThresholdValueLo_Object = MibTableColumn
f3L3FlowPointThresholdValueLo = _F3L3FlowPointThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 3, 1, 4),
    _F3L3FlowPointThresholdValueLo_Type()
)
f3L3FlowPointThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3FlowPointThresholdValueLo.setStatus("current")
_F3L3FlowPointThresholdValueHi_Type = Unsigned32
_F3L3FlowPointThresholdValueHi_Object = MibTableColumn
f3L3FlowPointThresholdValueHi = _F3L3FlowPointThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 3, 1, 5),
    _F3L3FlowPointThresholdValueHi_Type()
)
f3L3FlowPointThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3FlowPointThresholdValueHi.setStatus("current")
_F3L3FlowPointThresholdMonValue_Type = Counter64
_F3L3FlowPointThresholdMonValue_Object = MibTableColumn
f3L3FlowPointThresholdMonValue = _F3L3FlowPointThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 3, 1, 6),
    _F3L3FlowPointThresholdMonValue_Type()
)
f3L3FlowPointThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3FlowPointThresholdMonValue.setStatus("current")
_F3L3TrafficIpInterfaceStatsTable_Object = MibTable
f3L3TrafficIpInterfaceStatsTable = _F3L3TrafficIpInterfaceStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 4)
)
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceStatsTable.setStatus("current")
_F3L3TrafficIpInterfaceStatsEntry_Object = MibTableRow
f3L3TrafficIpInterfaceStatsEntry = _F3L3TrafficIpInterfaceStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 4, 1)
)
f3L3TrafficIpInterfaceStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficIPIfIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficIpInterfaceStatsIndex"),
)
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceStatsEntry.setStatus("current")


class _F3L3TrafficIpInterfaceStatsIndex_Type(Integer32):
    """Custom type f3L3TrafficIpInterfaceStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_F3L3TrafficIpInterfaceStatsIndex_Type.__name__ = "Integer32"
_F3L3TrafficIpInterfaceStatsIndex_Object = MibTableColumn
f3L3TrafficIpInterfaceStatsIndex = _F3L3TrafficIpInterfaceStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 4, 1, 1),
    _F3L3TrafficIpInterfaceStatsIndex_Type()
)
f3L3TrafficIpInterfaceStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceStatsIndex.setStatus("current")
_F3L3TrafficIpInterfaceStatsIntervalType_Type = CmPmIntervalType
_F3L3TrafficIpInterfaceStatsIntervalType_Object = MibTableColumn
f3L3TrafficIpInterfaceStatsIntervalType = _F3L3TrafficIpInterfaceStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 4, 1, 2),
    _F3L3TrafficIpInterfaceStatsIntervalType_Type()
)
f3L3TrafficIpInterfaceStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceStatsIntervalType.setStatus("current")
_F3L3TrafficIpInterfaceStatsValid_Type = TruthValue
_F3L3TrafficIpInterfaceStatsValid_Object = MibTableColumn
f3L3TrafficIpInterfaceStatsValid = _F3L3TrafficIpInterfaceStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 4, 1, 3),
    _F3L3TrafficIpInterfaceStatsValid_Type()
)
f3L3TrafficIpInterfaceStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceStatsValid.setStatus("current")
_F3L3TrafficIpInterfaceStatsAction_Type = CmPmBinAction
_F3L3TrafficIpInterfaceStatsAction_Object = MibTableColumn
f3L3TrafficIpInterfaceStatsAction = _F3L3TrafficIpInterfaceStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 4, 1, 4),
    _F3L3TrafficIpInterfaceStatsAction_Type()
)
f3L3TrafficIpInterfaceStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceStatsAction.setStatus("current")
_F3L3TrafficIpInterfaceStatsDhcpTx_Type = PerfCounter64
_F3L3TrafficIpInterfaceStatsDhcpTx_Object = MibTableColumn
f3L3TrafficIpInterfaceStatsDhcpTx = _F3L3TrafficIpInterfaceStatsDhcpTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 4, 1, 5),
    _F3L3TrafficIpInterfaceStatsDhcpTx_Type()
)
f3L3TrafficIpInterfaceStatsDhcpTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceStatsDhcpTx.setStatus("current")
_F3L3TrafficIpInterfaceStatsDhcpRx_Type = PerfCounter64
_F3L3TrafficIpInterfaceStatsDhcpRx_Object = MibTableColumn
f3L3TrafficIpInterfaceStatsDhcpRx = _F3L3TrafficIpInterfaceStatsDhcpRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 4, 1, 6),
    _F3L3TrafficIpInterfaceStatsDhcpRx_Type()
)
f3L3TrafficIpInterfaceStatsDhcpRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceStatsDhcpRx.setStatus("current")
_F3L3TrafficIpInterfaceStatsIcmpTx_Type = PerfCounter64
_F3L3TrafficIpInterfaceStatsIcmpTx_Object = MibTableColumn
f3L3TrafficIpInterfaceStatsIcmpTx = _F3L3TrafficIpInterfaceStatsIcmpTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 4, 1, 7),
    _F3L3TrafficIpInterfaceStatsIcmpTx_Type()
)
f3L3TrafficIpInterfaceStatsIcmpTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceStatsIcmpTx.setStatus("current")
_F3L3TrafficIpInterfaceStatsIcmpRx_Type = PerfCounter64
_F3L3TrafficIpInterfaceStatsIcmpRx_Object = MibTableColumn
f3L3TrafficIpInterfaceStatsIcmpRx = _F3L3TrafficIpInterfaceStatsIcmpRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 4, 1, 8),
    _F3L3TrafficIpInterfaceStatsIcmpRx_Type()
)
f3L3TrafficIpInterfaceStatsIcmpRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceStatsIcmpRx.setStatus("current")
_F3L3TrafficIpInterfaceStatsArpReqTx_Type = PerfCounter64
_F3L3TrafficIpInterfaceStatsArpReqTx_Object = MibTableColumn
f3L3TrafficIpInterfaceStatsArpReqTx = _F3L3TrafficIpInterfaceStatsArpReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 4, 1, 9),
    _F3L3TrafficIpInterfaceStatsArpReqTx_Type()
)
f3L3TrafficIpInterfaceStatsArpReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceStatsArpReqTx.setStatus("current")
_F3L3TrafficIpInterfaceStatsArpReqRx_Type = PerfCounter64
_F3L3TrafficIpInterfaceStatsArpReqRx_Object = MibTableColumn
f3L3TrafficIpInterfaceStatsArpReqRx = _F3L3TrafficIpInterfaceStatsArpReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 4, 1, 10),
    _F3L3TrafficIpInterfaceStatsArpReqRx_Type()
)
f3L3TrafficIpInterfaceStatsArpReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceStatsArpReqRx.setStatus("current")
_F3L3TrafficIpInterfaceStatsArpReplyTx_Type = PerfCounter64
_F3L3TrafficIpInterfaceStatsArpReplyTx_Object = MibTableColumn
f3L3TrafficIpInterfaceStatsArpReplyTx = _F3L3TrafficIpInterfaceStatsArpReplyTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 4, 1, 11),
    _F3L3TrafficIpInterfaceStatsArpReplyTx_Type()
)
f3L3TrafficIpInterfaceStatsArpReplyTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceStatsArpReplyTx.setStatus("current")
_F3L3TrafficIpInterfaceStatsArpReplyRx_Type = PerfCounter64
_F3L3TrafficIpInterfaceStatsArpReplyRx_Object = MibTableColumn
f3L3TrafficIpInterfaceStatsArpReplyRx = _F3L3TrafficIpInterfaceStatsArpReplyRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 4, 1, 12),
    _F3L3TrafficIpInterfaceStatsArpReplyRx_Type()
)
f3L3TrafficIpInterfaceStatsArpReplyRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceStatsArpReplyRx.setStatus("current")
_F3L3TrafficIpInterfaceStatsDhcpV6Tx_Type = PerfCounter64
_F3L3TrafficIpInterfaceStatsDhcpV6Tx_Object = MibTableColumn
f3L3TrafficIpInterfaceStatsDhcpV6Tx = _F3L3TrafficIpInterfaceStatsDhcpV6Tx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 4, 1, 13),
    _F3L3TrafficIpInterfaceStatsDhcpV6Tx_Type()
)
f3L3TrafficIpInterfaceStatsDhcpV6Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceStatsDhcpV6Tx.setStatus("current")
_F3L3TrafficIpInterfaceStatsDhcpV6Rx_Type = PerfCounter64
_F3L3TrafficIpInterfaceStatsDhcpV6Rx_Object = MibTableColumn
f3L3TrafficIpInterfaceStatsDhcpV6Rx = _F3L3TrafficIpInterfaceStatsDhcpV6Rx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 4, 1, 14),
    _F3L3TrafficIpInterfaceStatsDhcpV6Rx_Type()
)
f3L3TrafficIpInterfaceStatsDhcpV6Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceStatsDhcpV6Rx.setStatus("current")
_F3L3TrafficIpInterfaceStatsIcmpV6WONdpTx_Type = PerfCounter64
_F3L3TrafficIpInterfaceStatsIcmpV6WONdpTx_Object = MibTableColumn
f3L3TrafficIpInterfaceStatsIcmpV6WONdpTx = _F3L3TrafficIpInterfaceStatsIcmpV6WONdpTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 4, 1, 15),
    _F3L3TrafficIpInterfaceStatsIcmpV6WONdpTx_Type()
)
f3L3TrafficIpInterfaceStatsIcmpV6WONdpTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceStatsIcmpV6WONdpTx.setStatus("current")
_F3L3TrafficIpInterfaceStatsIcmpV6WONdpRx_Type = PerfCounter64
_F3L3TrafficIpInterfaceStatsIcmpV6WONdpRx_Object = MibTableColumn
f3L3TrafficIpInterfaceStatsIcmpV6WONdpRx = _F3L3TrafficIpInterfaceStatsIcmpV6WONdpRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 4, 1, 16),
    _F3L3TrafficIpInterfaceStatsIcmpV6WONdpRx_Type()
)
f3L3TrafficIpInterfaceStatsIcmpV6WONdpRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceStatsIcmpV6WONdpRx.setStatus("current")
_F3L3TrafficIpInterfaceStatsNdpNSTx_Type = PerfCounter64
_F3L3TrafficIpInterfaceStatsNdpNSTx_Object = MibTableColumn
f3L3TrafficIpInterfaceStatsNdpNSTx = _F3L3TrafficIpInterfaceStatsNdpNSTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 4, 1, 17),
    _F3L3TrafficIpInterfaceStatsNdpNSTx_Type()
)
f3L3TrafficIpInterfaceStatsNdpNSTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceStatsNdpNSTx.setStatus("current")
_F3L3TrafficIpInterfaceStatsNdpNSRx_Type = PerfCounter64
_F3L3TrafficIpInterfaceStatsNdpNSRx_Object = MibTableColumn
f3L3TrafficIpInterfaceStatsNdpNSRx = _F3L3TrafficIpInterfaceStatsNdpNSRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 4, 1, 18),
    _F3L3TrafficIpInterfaceStatsNdpNSRx_Type()
)
f3L3TrafficIpInterfaceStatsNdpNSRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceStatsNdpNSRx.setStatus("current")
_F3L3TrafficIpInterfaceStatsNdpNATx_Type = PerfCounter64
_F3L3TrafficIpInterfaceStatsNdpNATx_Object = MibTableColumn
f3L3TrafficIpInterfaceStatsNdpNATx = _F3L3TrafficIpInterfaceStatsNdpNATx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 4, 1, 19),
    _F3L3TrafficIpInterfaceStatsNdpNATx_Type()
)
f3L3TrafficIpInterfaceStatsNdpNATx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceStatsNdpNATx.setStatus("current")
_F3L3TrafficIpInterfaceStatsNdpNARx_Type = PerfCounter64
_F3L3TrafficIpInterfaceStatsNdpNARx_Object = MibTableColumn
f3L3TrafficIpInterfaceStatsNdpNARx = _F3L3TrafficIpInterfaceStatsNdpNARx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 4, 1, 20),
    _F3L3TrafficIpInterfaceStatsNdpNARx_Type()
)
f3L3TrafficIpInterfaceStatsNdpNARx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceStatsNdpNARx.setStatus("current")
_F3L3TrafficIpInterfaceStatsNdpRATx_Type = PerfCounter64
_F3L3TrafficIpInterfaceStatsNdpRATx_Object = MibTableColumn
f3L3TrafficIpInterfaceStatsNdpRATx = _F3L3TrafficIpInterfaceStatsNdpRATx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 4, 1, 21),
    _F3L3TrafficIpInterfaceStatsNdpRATx_Type()
)
f3L3TrafficIpInterfaceStatsNdpRATx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceStatsNdpRATx.setStatus("current")
_F3L3TrafficIpInterfaceStatsNdpRARx_Type = PerfCounter64
_F3L3TrafficIpInterfaceStatsNdpRARx_Object = MibTableColumn
f3L3TrafficIpInterfaceStatsNdpRARx = _F3L3TrafficIpInterfaceStatsNdpRARx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 4, 1, 22),
    _F3L3TrafficIpInterfaceStatsNdpRARx_Type()
)
f3L3TrafficIpInterfaceStatsNdpRARx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceStatsNdpRARx.setStatus("current")
_F3L3TrafficIpInterfaceStatsNdpRSTx_Type = PerfCounter64
_F3L3TrafficIpInterfaceStatsNdpRSTx_Object = MibTableColumn
f3L3TrafficIpInterfaceStatsNdpRSTx = _F3L3TrafficIpInterfaceStatsNdpRSTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 4, 1, 23),
    _F3L3TrafficIpInterfaceStatsNdpRSTx_Type()
)
f3L3TrafficIpInterfaceStatsNdpRSTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceStatsNdpRSTx.setStatus("current")
_F3L3TrafficIpInterfaceStatsNdpRSRx_Type = PerfCounter64
_F3L3TrafficIpInterfaceStatsNdpRSRx_Object = MibTableColumn
f3L3TrafficIpInterfaceStatsNdpRSRx = _F3L3TrafficIpInterfaceStatsNdpRSRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 4, 1, 24),
    _F3L3TrafficIpInterfaceStatsNdpRSRx_Type()
)
f3L3TrafficIpInterfaceStatsNdpRSRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceStatsNdpRSRx.setStatus("current")
_F3L3TrafficIpInterfaceHistoryTable_Object = MibTable
f3L3TrafficIpInterfaceHistoryTable = _F3L3TrafficIpInterfaceHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 5)
)
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceHistoryTable.setStatus("current")
_F3L3TrafficIpInterfaceHistoryEntry_Object = MibTableRow
f3L3TrafficIpInterfaceHistoryEntry = _F3L3TrafficIpInterfaceHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 5, 1)
)
f3L3TrafficIpInterfaceHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficIPIfIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficIpInterfaceStatsIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficIpInterfaceHistoryIndex"),
)
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceHistoryEntry.setStatus("current")


class _F3L3TrafficIpInterfaceHistoryIndex_Type(Integer32):
    """Custom type f3L3TrafficIpInterfaceHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3L3TrafficIpInterfaceHistoryIndex_Type.__name__ = "Integer32"
_F3L3TrafficIpInterfaceHistoryIndex_Object = MibTableColumn
f3L3TrafficIpInterfaceHistoryIndex = _F3L3TrafficIpInterfaceHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 5, 1, 1),
    _F3L3TrafficIpInterfaceHistoryIndex_Type()
)
f3L3TrafficIpInterfaceHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceHistoryIndex.setStatus("current")
_F3L3TrafficIpInterfaceHistoryTime_Type = DateAndTime
_F3L3TrafficIpInterfaceHistoryTime_Object = MibTableColumn
f3L3TrafficIpInterfaceHistoryTime = _F3L3TrafficIpInterfaceHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 5, 1, 2),
    _F3L3TrafficIpInterfaceHistoryTime_Type()
)
f3L3TrafficIpInterfaceHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceHistoryTime.setStatus("current")
_F3L3TrafficIpInterfaceHistoryValid_Type = TruthValue
_F3L3TrafficIpInterfaceHistoryValid_Object = MibTableColumn
f3L3TrafficIpInterfaceHistoryValid = _F3L3TrafficIpInterfaceHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 5, 1, 3),
    _F3L3TrafficIpInterfaceHistoryValid_Type()
)
f3L3TrafficIpInterfaceHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceHistoryValid.setStatus("current")
_F3L3TrafficIpInterfaceHistoryAction_Type = CmPmBinAction
_F3L3TrafficIpInterfaceHistoryAction_Object = MibTableColumn
f3L3TrafficIpInterfaceHistoryAction = _F3L3TrafficIpInterfaceHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 5, 1, 4),
    _F3L3TrafficIpInterfaceHistoryAction_Type()
)
f3L3TrafficIpInterfaceHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceHistoryAction.setStatus("current")
_F3L3TrafficIpInterfaceHistoryDhcpTx_Type = PerfCounter64
_F3L3TrafficIpInterfaceHistoryDhcpTx_Object = MibTableColumn
f3L3TrafficIpInterfaceHistoryDhcpTx = _F3L3TrafficIpInterfaceHistoryDhcpTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 5, 1, 5),
    _F3L3TrafficIpInterfaceHistoryDhcpTx_Type()
)
f3L3TrafficIpInterfaceHistoryDhcpTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceHistoryDhcpTx.setStatus("current")
_F3L3TrafficIpInterfaceHistoryDhcpRx_Type = PerfCounter64
_F3L3TrafficIpInterfaceHistoryDhcpRx_Object = MibTableColumn
f3L3TrafficIpInterfaceHistoryDhcpRx = _F3L3TrafficIpInterfaceHistoryDhcpRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 5, 1, 6),
    _F3L3TrafficIpInterfaceHistoryDhcpRx_Type()
)
f3L3TrafficIpInterfaceHistoryDhcpRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceHistoryDhcpRx.setStatus("current")
_F3L3TrafficIpInterfaceHistoryIcmpTx_Type = PerfCounter64
_F3L3TrafficIpInterfaceHistoryIcmpTx_Object = MibTableColumn
f3L3TrafficIpInterfaceHistoryIcmpTx = _F3L3TrafficIpInterfaceHistoryIcmpTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 5, 1, 7),
    _F3L3TrafficIpInterfaceHistoryIcmpTx_Type()
)
f3L3TrafficIpInterfaceHistoryIcmpTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceHistoryIcmpTx.setStatus("current")
_F3L3TrafficIpInterfaceHistoryIcmpRx_Type = PerfCounter64
_F3L3TrafficIpInterfaceHistoryIcmpRx_Object = MibTableColumn
f3L3TrafficIpInterfaceHistoryIcmpRx = _F3L3TrafficIpInterfaceHistoryIcmpRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 5, 1, 8),
    _F3L3TrafficIpInterfaceHistoryIcmpRx_Type()
)
f3L3TrafficIpInterfaceHistoryIcmpRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceHistoryIcmpRx.setStatus("current")
_F3L3TrafficIpInterfaceHistoryArpReqTx_Type = PerfCounter64
_F3L3TrafficIpInterfaceHistoryArpReqTx_Object = MibTableColumn
f3L3TrafficIpInterfaceHistoryArpReqTx = _F3L3TrafficIpInterfaceHistoryArpReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 5, 1, 9),
    _F3L3TrafficIpInterfaceHistoryArpReqTx_Type()
)
f3L3TrafficIpInterfaceHistoryArpReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceHistoryArpReqTx.setStatus("current")
_F3L3TrafficIpInterfaceHistoryArpReqRx_Type = PerfCounter64
_F3L3TrafficIpInterfaceHistoryArpReqRx_Object = MibTableColumn
f3L3TrafficIpInterfaceHistoryArpReqRx = _F3L3TrafficIpInterfaceHistoryArpReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 5, 1, 10),
    _F3L3TrafficIpInterfaceHistoryArpReqRx_Type()
)
f3L3TrafficIpInterfaceHistoryArpReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceHistoryArpReqRx.setStatus("current")
_F3L3TrafficIpInterfaceHistoryArpReplyTx_Type = PerfCounter64
_F3L3TrafficIpInterfaceHistoryArpReplyTx_Object = MibTableColumn
f3L3TrafficIpInterfaceHistoryArpReplyTx = _F3L3TrafficIpInterfaceHistoryArpReplyTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 5, 1, 11),
    _F3L3TrafficIpInterfaceHistoryArpReplyTx_Type()
)
f3L3TrafficIpInterfaceHistoryArpReplyTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceHistoryArpReplyTx.setStatus("current")
_F3L3TrafficIpInterfaceHistoryArpReplyRx_Type = PerfCounter64
_F3L3TrafficIpInterfaceHistoryArpReplyRx_Object = MibTableColumn
f3L3TrafficIpInterfaceHistoryArpReplyRx = _F3L3TrafficIpInterfaceHistoryArpReplyRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 5, 1, 12),
    _F3L3TrafficIpInterfaceHistoryArpReplyRx_Type()
)
f3L3TrafficIpInterfaceHistoryArpReplyRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceHistoryArpReplyRx.setStatus("current")
_F3L3TrafficIpInterfaceHistoryDhcpV6Tx_Type = PerfCounter64
_F3L3TrafficIpInterfaceHistoryDhcpV6Tx_Object = MibTableColumn
f3L3TrafficIpInterfaceHistoryDhcpV6Tx = _F3L3TrafficIpInterfaceHistoryDhcpV6Tx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 5, 1, 13),
    _F3L3TrafficIpInterfaceHistoryDhcpV6Tx_Type()
)
f3L3TrafficIpInterfaceHistoryDhcpV6Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceHistoryDhcpV6Tx.setStatus("current")
_F3L3TrafficIpInterfaceHistoryDhcpV6Rx_Type = PerfCounter64
_F3L3TrafficIpInterfaceHistoryDhcpV6Rx_Object = MibTableColumn
f3L3TrafficIpInterfaceHistoryDhcpV6Rx = _F3L3TrafficIpInterfaceHistoryDhcpV6Rx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 5, 1, 14),
    _F3L3TrafficIpInterfaceHistoryDhcpV6Rx_Type()
)
f3L3TrafficIpInterfaceHistoryDhcpV6Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceHistoryDhcpV6Rx.setStatus("current")
_F3L3TrafficIpInterfaceHistoryIcmpV6WONdpTx_Type = PerfCounter64
_F3L3TrafficIpInterfaceHistoryIcmpV6WONdpTx_Object = MibTableColumn
f3L3TrafficIpInterfaceHistoryIcmpV6WONdpTx = _F3L3TrafficIpInterfaceHistoryIcmpV6WONdpTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 5, 1, 15),
    _F3L3TrafficIpInterfaceHistoryIcmpV6WONdpTx_Type()
)
f3L3TrafficIpInterfaceHistoryIcmpV6WONdpTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceHistoryIcmpV6WONdpTx.setStatus("current")
_F3L3TrafficIpInterfaceHistoryIcmpV6WONdpRx_Type = PerfCounter64
_F3L3TrafficIpInterfaceHistoryIcmpV6WONdpRx_Object = MibTableColumn
f3L3TrafficIpInterfaceHistoryIcmpV6WONdpRx = _F3L3TrafficIpInterfaceHistoryIcmpV6WONdpRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 5, 1, 16),
    _F3L3TrafficIpInterfaceHistoryIcmpV6WONdpRx_Type()
)
f3L3TrafficIpInterfaceHistoryIcmpV6WONdpRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceHistoryIcmpV6WONdpRx.setStatus("current")
_F3L3TrafficIpInterfaceHistoryNdpNSTx_Type = PerfCounter64
_F3L3TrafficIpInterfaceHistoryNdpNSTx_Object = MibTableColumn
f3L3TrafficIpInterfaceHistoryNdpNSTx = _F3L3TrafficIpInterfaceHistoryNdpNSTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 5, 1, 17),
    _F3L3TrafficIpInterfaceHistoryNdpNSTx_Type()
)
f3L3TrafficIpInterfaceHistoryNdpNSTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceHistoryNdpNSTx.setStatus("current")
_F3L3TrafficIpInterfaceHistoryNdpNSRx_Type = PerfCounter64
_F3L3TrafficIpInterfaceHistoryNdpNSRx_Object = MibTableColumn
f3L3TrafficIpInterfaceHistoryNdpNSRx = _F3L3TrafficIpInterfaceHistoryNdpNSRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 5, 1, 18),
    _F3L3TrafficIpInterfaceHistoryNdpNSRx_Type()
)
f3L3TrafficIpInterfaceHistoryNdpNSRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceHistoryNdpNSRx.setStatus("current")
_F3L3TrafficIpInterfaceHistoryNdpNATx_Type = PerfCounter64
_F3L3TrafficIpInterfaceHistoryNdpNATx_Object = MibTableColumn
f3L3TrafficIpInterfaceHistoryNdpNATx = _F3L3TrafficIpInterfaceHistoryNdpNATx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 5, 1, 19),
    _F3L3TrafficIpInterfaceHistoryNdpNATx_Type()
)
f3L3TrafficIpInterfaceHistoryNdpNATx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceHistoryNdpNATx.setStatus("current")
_F3L3TrafficIpInterfaceHistoryNdpNARx_Type = PerfCounter64
_F3L3TrafficIpInterfaceHistoryNdpNARx_Object = MibTableColumn
f3L3TrafficIpInterfaceHistoryNdpNARx = _F3L3TrafficIpInterfaceHistoryNdpNARx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 5, 1, 20),
    _F3L3TrafficIpInterfaceHistoryNdpNARx_Type()
)
f3L3TrafficIpInterfaceHistoryNdpNARx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceHistoryNdpNARx.setStatus("current")
_F3L3TrafficIpInterfaceHistoryNdpRATx_Type = PerfCounter64
_F3L3TrafficIpInterfaceHistoryNdpRATx_Object = MibTableColumn
f3L3TrafficIpInterfaceHistoryNdpRATx = _F3L3TrafficIpInterfaceHistoryNdpRATx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 5, 1, 21),
    _F3L3TrafficIpInterfaceHistoryNdpRATx_Type()
)
f3L3TrafficIpInterfaceHistoryNdpRATx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceHistoryNdpRATx.setStatus("current")
_F3L3TrafficIpInterfaceHistoryNdpRARx_Type = PerfCounter64
_F3L3TrafficIpInterfaceHistoryNdpRARx_Object = MibTableColumn
f3L3TrafficIpInterfaceHistoryNdpRARx = _F3L3TrafficIpInterfaceHistoryNdpRARx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 5, 1, 22),
    _F3L3TrafficIpInterfaceHistoryNdpRARx_Type()
)
f3L3TrafficIpInterfaceHistoryNdpRARx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceHistoryNdpRARx.setStatus("current")
_F3L3TrafficIpInterfaceHistoryNdpRSTx_Type = PerfCounter64
_F3L3TrafficIpInterfaceHistoryNdpRSTx_Object = MibTableColumn
f3L3TrafficIpInterfaceHistoryNdpRSTx = _F3L3TrafficIpInterfaceHistoryNdpRSTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 5, 1, 23),
    _F3L3TrafficIpInterfaceHistoryNdpRSTx_Type()
)
f3L3TrafficIpInterfaceHistoryNdpRSTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceHistoryNdpRSTx.setStatus("current")
_F3L3TrafficIpInterfaceHistoryNdpRSRx_Type = PerfCounter64
_F3L3TrafficIpInterfaceHistoryNdpRSRx_Object = MibTableColumn
f3L3TrafficIpInterfaceHistoryNdpRSRx = _F3L3TrafficIpInterfaceHistoryNdpRSRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 5, 1, 24),
    _F3L3TrafficIpInterfaceHistoryNdpRSRx_Type()
)
f3L3TrafficIpInterfaceHistoryNdpRSRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceHistoryNdpRSRx.setStatus("current")
_F3L3TrafficIpInterfaceThresholdTable_Object = MibTable
f3L3TrafficIpInterfaceThresholdTable = _F3L3TrafficIpInterfaceThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 6)
)
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceThresholdTable.setStatus("current")
_F3L3TrafficIpInterfaceThresholdEntry_Object = MibTableRow
f3L3TrafficIpInterfaceThresholdEntry = _F3L3TrafficIpInterfaceThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 6, 1)
)
f3L3TrafficIpInterfaceThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficIPIfIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficIpInterfaceStatsIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficIpInterfaceThresholdIndex"),
)
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceThresholdEntry.setStatus("current")


class _F3L3TrafficIpInterfaceThresholdIndex_Type(Integer32):
    """Custom type f3L3TrafficIpInterfaceThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3L3TrafficIpInterfaceThresholdIndex_Type.__name__ = "Integer32"
_F3L3TrafficIpInterfaceThresholdIndex_Object = MibTableColumn
f3L3TrafficIpInterfaceThresholdIndex = _F3L3TrafficIpInterfaceThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 6, 1, 1),
    _F3L3TrafficIpInterfaceThresholdIndex_Type()
)
f3L3TrafficIpInterfaceThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceThresholdIndex.setStatus("current")
_F3L3TrafficIpInterfaceThresholdInterval_Type = CmPmIntervalType
_F3L3TrafficIpInterfaceThresholdInterval_Object = MibTableColumn
f3L3TrafficIpInterfaceThresholdInterval = _F3L3TrafficIpInterfaceThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 6, 1, 2),
    _F3L3TrafficIpInterfaceThresholdInterval_Type()
)
f3L3TrafficIpInterfaceThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceThresholdInterval.setStatus("current")
_F3L3TrafficIpInterfaceThresholdVariable_Type = VariablePointer
_F3L3TrafficIpInterfaceThresholdVariable_Object = MibTableColumn
f3L3TrafficIpInterfaceThresholdVariable = _F3L3TrafficIpInterfaceThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 6, 1, 3),
    _F3L3TrafficIpInterfaceThresholdVariable_Type()
)
f3L3TrafficIpInterfaceThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceThresholdVariable.setStatus("current")
_F3L3TrafficIpInterfaceThresholdValueLo_Type = Unsigned32
_F3L3TrafficIpInterfaceThresholdValueLo_Object = MibTableColumn
f3L3TrafficIpInterfaceThresholdValueLo = _F3L3TrafficIpInterfaceThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 6, 1, 4),
    _F3L3TrafficIpInterfaceThresholdValueLo_Type()
)
f3L3TrafficIpInterfaceThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceThresholdValueLo.setStatus("current")
_F3L3TrafficIpInterfaceThresholdValueHi_Type = Unsigned32
_F3L3TrafficIpInterfaceThresholdValueHi_Object = MibTableColumn
f3L3TrafficIpInterfaceThresholdValueHi = _F3L3TrafficIpInterfaceThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 6, 1, 5),
    _F3L3TrafficIpInterfaceThresholdValueHi_Type()
)
f3L3TrafficIpInterfaceThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceThresholdValueHi.setStatus("current")
_F3L3TrafficIpInterfaceThresholdMonValue_Type = Counter64
_F3L3TrafficIpInterfaceThresholdMonValue_Object = MibTableColumn
f3L3TrafficIpInterfaceThresholdMonValue = _F3L3TrafficIpInterfaceThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 6, 1, 6),
    _F3L3TrafficIpInterfaceThresholdMonValue_Type()
)
f3L3TrafficIpInterfaceThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceThresholdMonValue.setStatus("current")
_F3L3AclRuleStatsTable_Object = MibTable
f3L3AclRuleStatsTable = _F3L3AclRuleStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 7)
)
if mibBuilder.loadTexts:
    f3L3AclRuleStatsTable.setStatus("current")
_F3L3AclRuleStatsEntry_Object = MibTableRow
f3L3AclRuleStatsEntry = _F3L3AclRuleStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 7, 1)
)
f3L3AclRuleStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L3AclRuleParentIndex"),
    (0, "F3-L3-MIB", "f3L3AclRuleIndex"),
    (0, "F3-L3-MIB", "f3L3AclRuleStatsIndex"),
)
if mibBuilder.loadTexts:
    f3L3AclRuleStatsEntry.setStatus("current")


class _F3L3AclRuleStatsIndex_Type(Integer32):
    """Custom type f3L3AclRuleStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_F3L3AclRuleStatsIndex_Type.__name__ = "Integer32"
_F3L3AclRuleStatsIndex_Object = MibTableColumn
f3L3AclRuleStatsIndex = _F3L3AclRuleStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 7, 1, 1),
    _F3L3AclRuleStatsIndex_Type()
)
f3L3AclRuleStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3AclRuleStatsIndex.setStatus("current")
_F3L3AclRuleStatsIntervalType_Type = CmPmIntervalType
_F3L3AclRuleStatsIntervalType_Object = MibTableColumn
f3L3AclRuleStatsIntervalType = _F3L3AclRuleStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 7, 1, 2),
    _F3L3AclRuleStatsIntervalType_Type()
)
f3L3AclRuleStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3AclRuleStatsIntervalType.setStatus("current")
_F3L3AclRuleStatsValid_Type = TruthValue
_F3L3AclRuleStatsValid_Object = MibTableColumn
f3L3AclRuleStatsValid = _F3L3AclRuleStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 7, 1, 3),
    _F3L3AclRuleStatsValid_Type()
)
f3L3AclRuleStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3AclRuleStatsValid.setStatus("current")
_F3L3AclRuleStatsAction_Type = CmPmBinAction
_F3L3AclRuleStatsAction_Object = MibTableColumn
f3L3AclRuleStatsAction = _F3L3AclRuleStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 7, 1, 4),
    _F3L3AclRuleStatsAction_Type()
)
f3L3AclRuleStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleStatsAction.setStatus("current")
_F3L3AclRuleStatsRuleMatch_Type = PerfCounter64
_F3L3AclRuleStatsRuleMatch_Object = MibTableColumn
f3L3AclRuleStatsRuleMatch = _F3L3AclRuleStatsRuleMatch_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 7, 1, 5),
    _F3L3AclRuleStatsRuleMatch_Type()
)
f3L3AclRuleStatsRuleMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3AclRuleStatsRuleMatch.setStatus("current")
_F3L3AclRuleHistoryTable_Object = MibTable
f3L3AclRuleHistoryTable = _F3L3AclRuleHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 8)
)
if mibBuilder.loadTexts:
    f3L3AclRuleHistoryTable.setStatus("current")
_F3L3AclRuleHistoryEntry_Object = MibTableRow
f3L3AclRuleHistoryEntry = _F3L3AclRuleHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 8, 1)
)
f3L3AclRuleHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L3AclRuleParentIndex"),
    (0, "F3-L3-MIB", "f3L3AclRuleIndex"),
    (0, "F3-L3-MIB", "f3L3AclRuleStatsIndex"),
    (0, "F3-L3-MIB", "f3L3AclRuleHistoryIndex"),
)
if mibBuilder.loadTexts:
    f3L3AclRuleHistoryEntry.setStatus("current")


class _F3L3AclRuleHistoryIndex_Type(Integer32):
    """Custom type f3L3AclRuleHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3L3AclRuleHistoryIndex_Type.__name__ = "Integer32"
_F3L3AclRuleHistoryIndex_Object = MibTableColumn
f3L3AclRuleHistoryIndex = _F3L3AclRuleHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 8, 1, 1),
    _F3L3AclRuleHistoryIndex_Type()
)
f3L3AclRuleHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3AclRuleHistoryIndex.setStatus("current")
_F3L3AclRuleHistoryTime_Type = DateAndTime
_F3L3AclRuleHistoryTime_Object = MibTableColumn
f3L3AclRuleHistoryTime = _F3L3AclRuleHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 8, 1, 2),
    _F3L3AclRuleHistoryTime_Type()
)
f3L3AclRuleHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3AclRuleHistoryTime.setStatus("current")
_F3L3AclRuleHistoryValid_Type = TruthValue
_F3L3AclRuleHistoryValid_Object = MibTableColumn
f3L3AclRuleHistoryValid = _F3L3AclRuleHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 8, 1, 3),
    _F3L3AclRuleHistoryValid_Type()
)
f3L3AclRuleHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3AclRuleHistoryValid.setStatus("current")
_F3L3AclRuleHistoryAction_Type = CmPmBinAction
_F3L3AclRuleHistoryAction_Object = MibTableColumn
f3L3AclRuleHistoryAction = _F3L3AclRuleHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 8, 1, 4),
    _F3L3AclRuleHistoryAction_Type()
)
f3L3AclRuleHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleHistoryAction.setStatus("current")
_F3L3AclRuleHistoryRuleMatch_Type = PerfCounter64
_F3L3AclRuleHistoryRuleMatch_Object = MibTableColumn
f3L3AclRuleHistoryRuleMatch = _F3L3AclRuleHistoryRuleMatch_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 8, 1, 5),
    _F3L3AclRuleHistoryRuleMatch_Type()
)
f3L3AclRuleHistoryRuleMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3AclRuleHistoryRuleMatch.setStatus("current")
_F3L3AclRuleThresholdTable_Object = MibTable
f3L3AclRuleThresholdTable = _F3L3AclRuleThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 9)
)
if mibBuilder.loadTexts:
    f3L3AclRuleThresholdTable.setStatus("current")
_F3L3AclRuleThresholdEntry_Object = MibTableRow
f3L3AclRuleThresholdEntry = _F3L3AclRuleThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 9, 1)
)
f3L3AclRuleThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L3AclRuleParentIndex"),
    (0, "F3-L3-MIB", "f3L3AclRuleIndex"),
    (0, "F3-L3-MIB", "f3L3AclRuleStatsIndex"),
    (0, "F3-L3-MIB", "f3L3AclRuleThresholdIndex"),
)
if mibBuilder.loadTexts:
    f3L3AclRuleThresholdEntry.setStatus("current")


class _F3L3AclRuleThresholdIndex_Type(Integer32):
    """Custom type f3L3AclRuleThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3L3AclRuleThresholdIndex_Type.__name__ = "Integer32"
_F3L3AclRuleThresholdIndex_Object = MibTableColumn
f3L3AclRuleThresholdIndex = _F3L3AclRuleThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 9, 1, 1),
    _F3L3AclRuleThresholdIndex_Type()
)
f3L3AclRuleThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3AclRuleThresholdIndex.setStatus("current")
_F3L3AclRuleThresholdInterval_Type = CmPmIntervalType
_F3L3AclRuleThresholdInterval_Object = MibTableColumn
f3L3AclRuleThresholdInterval = _F3L3AclRuleThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 9, 1, 2),
    _F3L3AclRuleThresholdInterval_Type()
)
f3L3AclRuleThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3AclRuleThresholdInterval.setStatus("current")
_F3L3AclRuleThresholdVariable_Type = VariablePointer
_F3L3AclRuleThresholdVariable_Object = MibTableColumn
f3L3AclRuleThresholdVariable = _F3L3AclRuleThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 9, 1, 3),
    _F3L3AclRuleThresholdVariable_Type()
)
f3L3AclRuleThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3AclRuleThresholdVariable.setStatus("current")
_F3L3AclRuleThresholdValueLo_Type = Unsigned32
_F3L3AclRuleThresholdValueLo_Object = MibTableColumn
f3L3AclRuleThresholdValueLo = _F3L3AclRuleThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 9, 1, 4),
    _F3L3AclRuleThresholdValueLo_Type()
)
f3L3AclRuleThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleThresholdValueLo.setStatus("current")
_F3L3AclRuleThresholdValueHi_Type = Unsigned32
_F3L3AclRuleThresholdValueHi_Object = MibTableColumn
f3L3AclRuleThresholdValueHi = _F3L3AclRuleThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 9, 1, 5),
    _F3L3AclRuleThresholdValueHi_Type()
)
f3L3AclRuleThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3AclRuleThresholdValueHi.setStatus("current")
_F3L3AclRuleThresholdMonValue_Type = Counter64
_F3L3AclRuleThresholdMonValue_Object = MibTableColumn
f3L3AclRuleThresholdMonValue = _F3L3AclRuleThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 9, 1, 6),
    _F3L3AclRuleThresholdMonValue_Type()
)
f3L3AclRuleThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3AclRuleThresholdMonValue.setStatus("current")
_F3L3QosPolicerStatsTable_Object = MibTable
f3L3QosPolicerStatsTable = _F3L3QosPolicerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 10)
)
if mibBuilder.loadTexts:
    f3L3QosPolicerStatsTable.setStatus("current")
_F3L3QosPolicerStatsEntry_Object = MibTableRow
f3L3QosPolicerStatsEntry = _F3L3QosPolicerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 10, 1)
)
f3L3QosPolicerStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortTypeIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointIndex"),
    (0, "F3-L3-MIB", "f3L3QosPolicerIndex"),
    (0, "F3-L3-MIB", "f3L3QosPolicerStatsIndex"),
)
if mibBuilder.loadTexts:
    f3L3QosPolicerStatsEntry.setStatus("current")


class _F3L3QosPolicerStatsIndex_Type(Integer32):
    """Custom type f3L3QosPolicerStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3L3QosPolicerStatsIndex_Type.__name__ = "Integer32"
_F3L3QosPolicerStatsIndex_Object = MibTableColumn
f3L3QosPolicerStatsIndex = _F3L3QosPolicerStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 10, 1, 1),
    _F3L3QosPolicerStatsIndex_Type()
)
f3L3QosPolicerStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosPolicerStatsIndex.setStatus("current")
_F3L3QosPolicerStatsIntervalType_Type = CmPmIntervalType
_F3L3QosPolicerStatsIntervalType_Object = MibTableColumn
f3L3QosPolicerStatsIntervalType = _F3L3QosPolicerStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 10, 1, 2),
    _F3L3QosPolicerStatsIntervalType_Type()
)
f3L3QosPolicerStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosPolicerStatsIntervalType.setStatus("current")
_F3L3QosPolicerStatsValid_Type = TruthValue
_F3L3QosPolicerStatsValid_Object = MibTableColumn
f3L3QosPolicerStatsValid = _F3L3QosPolicerStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 10, 1, 3),
    _F3L3QosPolicerStatsValid_Type()
)
f3L3QosPolicerStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosPolicerStatsValid.setStatus("current")
_F3L3QosPolicerStatsAction_Type = CmPmBinAction
_F3L3QosPolicerStatsAction_Object = MibTableColumn
f3L3QosPolicerStatsAction = _F3L3QosPolicerStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 10, 1, 4),
    _F3L3QosPolicerStatsAction_Type()
)
f3L3QosPolicerStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3QosPolicerStatsAction.setStatus("current")
_F3L3QosPolicerStatsFMG_Type = PerfCounter64
_F3L3QosPolicerStatsFMG_Object = MibTableColumn
f3L3QosPolicerStatsFMG = _F3L3QosPolicerStatsFMG_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 10, 1, 5),
    _F3L3QosPolicerStatsFMG_Type()
)
f3L3QosPolicerStatsFMG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosPolicerStatsFMG.setStatus("current")
_F3L3QosPolicerStatsFMY_Type = PerfCounter64
_F3L3QosPolicerStatsFMY_Object = MibTableColumn
f3L3QosPolicerStatsFMY = _F3L3QosPolicerStatsFMY_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 10, 1, 6),
    _F3L3QosPolicerStatsFMY_Type()
)
f3L3QosPolicerStatsFMY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosPolicerStatsFMY.setStatus("current")
_F3L3QosPolicerStatsFMYD_Type = PerfCounter64
_F3L3QosPolicerStatsFMYD_Object = MibTableColumn
f3L3QosPolicerStatsFMYD = _F3L3QosPolicerStatsFMYD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 10, 1, 7),
    _F3L3QosPolicerStatsFMYD_Type()
)
f3L3QosPolicerStatsFMYD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosPolicerStatsFMYD.setStatus("deprecated")
_F3L3QosPolicerStatsFMRD_Type = PerfCounter64
_F3L3QosPolicerStatsFMRD_Object = MibTableColumn
f3L3QosPolicerStatsFMRD = _F3L3QosPolicerStatsFMRD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 10, 1, 8),
    _F3L3QosPolicerStatsFMRD_Type()
)
f3L3QosPolicerStatsFMRD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosPolicerStatsFMRD.setStatus("current")
_F3L3QosPolicerStatsBytesIn_Type = PerfCounter64
_F3L3QosPolicerStatsBytesIn_Object = MibTableColumn
f3L3QosPolicerStatsBytesIn = _F3L3QosPolicerStatsBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 10, 1, 9),
    _F3L3QosPolicerStatsBytesIn_Type()
)
f3L3QosPolicerStatsBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosPolicerStatsBytesIn.setStatus("current")
_F3L3QosPolicerStatsBytesOut_Type = PerfCounter64
_F3L3QosPolicerStatsBytesOut_Object = MibTableColumn
f3L3QosPolicerStatsBytesOut = _F3L3QosPolicerStatsBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 10, 1, 10),
    _F3L3QosPolicerStatsBytesOut_Type()
)
f3L3QosPolicerStatsBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosPolicerStatsBytesOut.setStatus("current")
_F3L3QosPolicerStatsABR_Type = PerfCounter64
_F3L3QosPolicerStatsABR_Object = MibTableColumn
f3L3QosPolicerStatsABR = _F3L3QosPolicerStatsABR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 10, 1, 11),
    _F3L3QosPolicerStatsABR_Type()
)
f3L3QosPolicerStatsABR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosPolicerStatsABR.setStatus("current")
_F3L3QosPolicerHistoryTable_Object = MibTable
f3L3QosPolicerHistoryTable = _F3L3QosPolicerHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 11)
)
if mibBuilder.loadTexts:
    f3L3QosPolicerHistoryTable.setStatus("current")
_F3L3QosPolicerHistoryEntry_Object = MibTableRow
f3L3QosPolicerHistoryEntry = _F3L3QosPolicerHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 11, 1)
)
f3L3QosPolicerHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortTypeIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointIndex"),
    (0, "F3-L3-MIB", "f3L3QosPolicerIndex"),
    (0, "F3-L3-MIB", "f3L3QosPolicerStatsIndex"),
    (0, "F3-L3-MIB", "f3L3QosPolicerHistoryIndex"),
)
if mibBuilder.loadTexts:
    f3L3QosPolicerHistoryEntry.setStatus("current")


class _F3L3QosPolicerHistoryIndex_Type(Integer32):
    """Custom type f3L3QosPolicerHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3L3QosPolicerHistoryIndex_Type.__name__ = "Integer32"
_F3L3QosPolicerHistoryIndex_Object = MibTableColumn
f3L3QosPolicerHistoryIndex = _F3L3QosPolicerHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 11, 1, 1),
    _F3L3QosPolicerHistoryIndex_Type()
)
f3L3QosPolicerHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosPolicerHistoryIndex.setStatus("current")
_F3L3QosPolicerHistoryTime_Type = DateAndTime
_F3L3QosPolicerHistoryTime_Object = MibTableColumn
f3L3QosPolicerHistoryTime = _F3L3QosPolicerHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 11, 1, 2),
    _F3L3QosPolicerHistoryTime_Type()
)
f3L3QosPolicerHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosPolicerHistoryTime.setStatus("current")
_F3L3QosPolicerHistoryValid_Type = TruthValue
_F3L3QosPolicerHistoryValid_Object = MibTableColumn
f3L3QosPolicerHistoryValid = _F3L3QosPolicerHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 11, 1, 3),
    _F3L3QosPolicerHistoryValid_Type()
)
f3L3QosPolicerHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosPolicerHistoryValid.setStatus("current")
_F3L3QosPolicerHistoryAction_Type = CmPmBinAction
_F3L3QosPolicerHistoryAction_Object = MibTableColumn
f3L3QosPolicerHistoryAction = _F3L3QosPolicerHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 11, 1, 4),
    _F3L3QosPolicerHistoryAction_Type()
)
f3L3QosPolicerHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3QosPolicerHistoryAction.setStatus("current")
_F3L3QosPolicerHistoryFMG_Type = PerfCounter64
_F3L3QosPolicerHistoryFMG_Object = MibTableColumn
f3L3QosPolicerHistoryFMG = _F3L3QosPolicerHistoryFMG_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 11, 1, 5),
    _F3L3QosPolicerHistoryFMG_Type()
)
f3L3QosPolicerHistoryFMG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosPolicerHistoryFMG.setStatus("current")
_F3L3QosPolicerHistoryFMY_Type = PerfCounter64
_F3L3QosPolicerHistoryFMY_Object = MibTableColumn
f3L3QosPolicerHistoryFMY = _F3L3QosPolicerHistoryFMY_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 11, 1, 6),
    _F3L3QosPolicerHistoryFMY_Type()
)
f3L3QosPolicerHistoryFMY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosPolicerHistoryFMY.setStatus("current")
_F3L3QosPolicerHistoryFMYD_Type = PerfCounter64
_F3L3QosPolicerHistoryFMYD_Object = MibTableColumn
f3L3QosPolicerHistoryFMYD = _F3L3QosPolicerHistoryFMYD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 11, 1, 7),
    _F3L3QosPolicerHistoryFMYD_Type()
)
f3L3QosPolicerHistoryFMYD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosPolicerHistoryFMYD.setStatus("deprecated")
_F3L3QosPolicerHistoryFMRD_Type = PerfCounter64
_F3L3QosPolicerHistoryFMRD_Object = MibTableColumn
f3L3QosPolicerHistoryFMRD = _F3L3QosPolicerHistoryFMRD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 11, 1, 8),
    _F3L3QosPolicerHistoryFMRD_Type()
)
f3L3QosPolicerHistoryFMRD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosPolicerHistoryFMRD.setStatus("current")
_F3L3QosPolicerHistoryBytesIn_Type = PerfCounter64
_F3L3QosPolicerHistoryBytesIn_Object = MibTableColumn
f3L3QosPolicerHistoryBytesIn = _F3L3QosPolicerHistoryBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 11, 1, 9),
    _F3L3QosPolicerHistoryBytesIn_Type()
)
f3L3QosPolicerHistoryBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosPolicerHistoryBytesIn.setStatus("current")
_F3L3QosPolicerHistoryBytesOut_Type = PerfCounter64
_F3L3QosPolicerHistoryBytesOut_Object = MibTableColumn
f3L3QosPolicerHistoryBytesOut = _F3L3QosPolicerHistoryBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 11, 1, 10),
    _F3L3QosPolicerHistoryBytesOut_Type()
)
f3L3QosPolicerHistoryBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosPolicerHistoryBytesOut.setStatus("current")
_F3L3QosPolicerHistoryABR_Type = PerfCounter64
_F3L3QosPolicerHistoryABR_Object = MibTableColumn
f3L3QosPolicerHistoryABR = _F3L3QosPolicerHistoryABR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 11, 1, 11),
    _F3L3QosPolicerHistoryABR_Type()
)
f3L3QosPolicerHistoryABR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosPolicerHistoryABR.setStatus("current")
_F3L3QosPolicerThresholdTable_Object = MibTable
f3L3QosPolicerThresholdTable = _F3L3QosPolicerThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 12)
)
if mibBuilder.loadTexts:
    f3L3QosPolicerThresholdTable.setStatus("current")
_F3L3QosPolicerThresholdEntry_Object = MibTableRow
f3L3QosPolicerThresholdEntry = _F3L3QosPolicerThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 12, 1)
)
f3L3QosPolicerThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortTypeIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointIndex"),
    (0, "F3-L3-MIB", "f3L3QosPolicerIndex"),
    (0, "F3-L3-MIB", "f3L3QosPolicerStatsIndex"),
    (0, "F3-L3-MIB", "f3L3QosPolicerThresholdIndex"),
)
if mibBuilder.loadTexts:
    f3L3QosPolicerThresholdEntry.setStatus("current")


class _F3L3QosPolicerThresholdIndex_Type(Integer32):
    """Custom type f3L3QosPolicerThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3L3QosPolicerThresholdIndex_Type.__name__ = "Integer32"
_F3L3QosPolicerThresholdIndex_Object = MibTableColumn
f3L3QosPolicerThresholdIndex = _F3L3QosPolicerThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 12, 1, 1),
    _F3L3QosPolicerThresholdIndex_Type()
)
f3L3QosPolicerThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosPolicerThresholdIndex.setStatus("current")
_F3L3QosPolicerThresholdInterval_Type = CmPmIntervalType
_F3L3QosPolicerThresholdInterval_Object = MibTableColumn
f3L3QosPolicerThresholdInterval = _F3L3QosPolicerThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 12, 1, 2),
    _F3L3QosPolicerThresholdInterval_Type()
)
f3L3QosPolicerThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosPolicerThresholdInterval.setStatus("current")
_F3L3QosPolicerThresholdVariable_Type = VariablePointer
_F3L3QosPolicerThresholdVariable_Object = MibTableColumn
f3L3QosPolicerThresholdVariable = _F3L3QosPolicerThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 12, 1, 3),
    _F3L3QosPolicerThresholdVariable_Type()
)
f3L3QosPolicerThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosPolicerThresholdVariable.setStatus("current")
_F3L3QosPolicerThresholdValueLo_Type = Unsigned32
_F3L3QosPolicerThresholdValueLo_Object = MibTableColumn
f3L3QosPolicerThresholdValueLo = _F3L3QosPolicerThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 12, 1, 4),
    _F3L3QosPolicerThresholdValueLo_Type()
)
f3L3QosPolicerThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3QosPolicerThresholdValueLo.setStatus("current")
_F3L3QosPolicerThresholdValueHi_Type = Unsigned32
_F3L3QosPolicerThresholdValueHi_Object = MibTableColumn
f3L3QosPolicerThresholdValueHi = _F3L3QosPolicerThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 12, 1, 5),
    _F3L3QosPolicerThresholdValueHi_Type()
)
f3L3QosPolicerThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3QosPolicerThresholdValueHi.setStatus("current")
_F3L3QosPolicerThresholdMonValue_Type = Counter64
_F3L3QosPolicerThresholdMonValue_Object = MibTableColumn
f3L3QosPolicerThresholdMonValue = _F3L3QosPolicerThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 12, 1, 6),
    _F3L3QosPolicerThresholdMonValue_Type()
)
f3L3QosPolicerThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosPolicerThresholdMonValue.setStatus("current")
_F3L3QosShaperStatsTable_Object = MibTable
f3L3QosShaperStatsTable = _F3L3QosShaperStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 13)
)
if mibBuilder.loadTexts:
    f3L3QosShaperStatsTable.setStatus("current")
_F3L3QosShaperStatsEntry_Object = MibTableRow
f3L3QosShaperStatsEntry = _F3L3QosShaperStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 13, 1)
)
f3L3QosShaperStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortTypeIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointIndex"),
    (0, "F3-L3-MIB", "f3L3QosShaperIndex"),
    (0, "F3-L3-MIB", "f3L3QosShaperStatsIndex"),
)
if mibBuilder.loadTexts:
    f3L3QosShaperStatsEntry.setStatus("current")


class _F3L3QosShaperStatsIndex_Type(Integer32):
    """Custom type f3L3QosShaperStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3L3QosShaperStatsIndex_Type.__name__ = "Integer32"
_F3L3QosShaperStatsIndex_Object = MibTableColumn
f3L3QosShaperStatsIndex = _F3L3QosShaperStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 13, 1, 1),
    _F3L3QosShaperStatsIndex_Type()
)
f3L3QosShaperStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperStatsIndex.setStatus("current")
_F3L3QosShaperStatsIntervalType_Type = CmPmIntervalType
_F3L3QosShaperStatsIntervalType_Object = MibTableColumn
f3L3QosShaperStatsIntervalType = _F3L3QosShaperStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 13, 1, 2),
    _F3L3QosShaperStatsIntervalType_Type()
)
f3L3QosShaperStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperStatsIntervalType.setStatus("current")
_F3L3QosShaperStatsValid_Type = TruthValue
_F3L3QosShaperStatsValid_Object = MibTableColumn
f3L3QosShaperStatsValid = _F3L3QosShaperStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 13, 1, 3),
    _F3L3QosShaperStatsValid_Type()
)
f3L3QosShaperStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperStatsValid.setStatus("current")
_F3L3QosShaperStatsAction_Type = CmPmBinAction
_F3L3QosShaperStatsAction_Object = MibTableColumn
f3L3QosShaperStatsAction = _F3L3QosShaperStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 13, 1, 4),
    _F3L3QosShaperStatsAction_Type()
)
f3L3QosShaperStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3QosShaperStatsAction.setStatus("current")
_F3L3QosShaperStatsBT_Type = PerfCounter64
_F3L3QosShaperStatsBT_Object = MibTableColumn
f3L3QosShaperStatsBT = _F3L3QosShaperStatsBT_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 13, 1, 5),
    _F3L3QosShaperStatsBT_Type()
)
f3L3QosShaperStatsBT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperStatsBT.setStatus("current")
_F3L3QosShaperStatsBTD_Type = PerfCounter64
_F3L3QosShaperStatsBTD_Object = MibTableColumn
f3L3QosShaperStatsBTD = _F3L3QosShaperStatsBTD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 13, 1, 6),
    _F3L3QosShaperStatsBTD_Type()
)
f3L3QosShaperStatsBTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperStatsBTD.setStatus("current")
_F3L3QosShaperStatsFD_Type = PerfCounter64
_F3L3QosShaperStatsFD_Object = MibTableColumn
f3L3QosShaperStatsFD = _F3L3QosShaperStatsFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 13, 1, 7),
    _F3L3QosShaperStatsFD_Type()
)
f3L3QosShaperStatsFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperStatsFD.setStatus("current")
_F3L3QosShaperStatsFTD_Type = PerfCounter64
_F3L3QosShaperStatsFTD_Object = MibTableColumn
f3L3QosShaperStatsFTD = _F3L3QosShaperStatsFTD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 13, 1, 8),
    _F3L3QosShaperStatsFTD_Type()
)
f3L3QosShaperStatsFTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperStatsFTD.setStatus("current")
_F3L3QosShaperStatsBR_Type = PerfCounter64
_F3L3QosShaperStatsBR_Object = MibTableColumn
f3L3QosShaperStatsBR = _F3L3QosShaperStatsBR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 13, 1, 9),
    _F3L3QosShaperStatsBR_Type()
)
f3L3QosShaperStatsBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperStatsBR.setStatus("current")
_F3L3QosShaperStatsFR_Type = PerfCounter64
_F3L3QosShaperStatsFR_Object = MibTableColumn
f3L3QosShaperStatsFR = _F3L3QosShaperStatsFR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 13, 1, 10),
    _F3L3QosShaperStatsFR_Type()
)
f3L3QosShaperStatsFR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperStatsFR.setStatus("current")
_F3L3QosShaperStatsABRRL_Type = PerfCounter64
_F3L3QosShaperStatsABRRL_Object = MibTableColumn
f3L3QosShaperStatsABRRL = _F3L3QosShaperStatsABRRL_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 13, 1, 11),
    _F3L3QosShaperStatsABRRL_Type()
)
f3L3QosShaperStatsABRRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperStatsABRRL.setStatus("current")
_F3L3QosShaperStatsABRRLR_Type = PerfCounter64
_F3L3QosShaperStatsABRRLR_Object = MibTableColumn
f3L3QosShaperStatsABRRLR = _F3L3QosShaperStatsABRRLR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 13, 1, 12),
    _F3L3QosShaperStatsABRRLR_Type()
)
f3L3QosShaperStatsABRRLR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperStatsABRRLR.setStatus("current")
_F3L3QosShaperStatsBREDD_Type = PerfCounter64
_F3L3QosShaperStatsBREDD_Object = MibTableColumn
f3L3QosShaperStatsBREDD = _F3L3QosShaperStatsBREDD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 13, 1, 13),
    _F3L3QosShaperStatsBREDD_Type()
)
f3L3QosShaperStatsBREDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperStatsBREDD.setStatus("current")
_F3L3QosShaperStatsFREDD_Type = PerfCounter64
_F3L3QosShaperStatsFREDD_Object = MibTableColumn
f3L3QosShaperStatsFREDD = _F3L3QosShaperStatsFREDD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 13, 1, 14),
    _F3L3QosShaperStatsFREDD_Type()
)
f3L3QosShaperStatsFREDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperStatsFREDD.setStatus("current")
_F3L3QosShaperHistoryTable_Object = MibTable
f3L3QosShaperHistoryTable = _F3L3QosShaperHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 14)
)
if mibBuilder.loadTexts:
    f3L3QosShaperHistoryTable.setStatus("current")
_F3L3QosShaperHistoryEntry_Object = MibTableRow
f3L3QosShaperHistoryEntry = _F3L3QosShaperHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 14, 1)
)
f3L3QosShaperHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortTypeIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointIndex"),
    (0, "F3-L3-MIB", "f3L3QosShaperIndex"),
    (0, "F3-L3-MIB", "f3L3QosShaperStatsIndex"),
    (0, "F3-L3-MIB", "f3L3QosShaperHistoryIndex"),
)
if mibBuilder.loadTexts:
    f3L3QosShaperHistoryEntry.setStatus("current")


class _F3L3QosShaperHistoryIndex_Type(Integer32):
    """Custom type f3L3QosShaperHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3L3QosShaperHistoryIndex_Type.__name__ = "Integer32"
_F3L3QosShaperHistoryIndex_Object = MibTableColumn
f3L3QosShaperHistoryIndex = _F3L3QosShaperHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 14, 1, 1),
    _F3L3QosShaperHistoryIndex_Type()
)
f3L3QosShaperHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperHistoryIndex.setStatus("current")
_F3L3QosShaperHistoryTime_Type = DateAndTime
_F3L3QosShaperHistoryTime_Object = MibTableColumn
f3L3QosShaperHistoryTime = _F3L3QosShaperHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 14, 1, 2),
    _F3L3QosShaperHistoryTime_Type()
)
f3L3QosShaperHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperHistoryTime.setStatus("current")
_F3L3QosShaperHistoryValid_Type = TruthValue
_F3L3QosShaperHistoryValid_Object = MibTableColumn
f3L3QosShaperHistoryValid = _F3L3QosShaperHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 14, 1, 3),
    _F3L3QosShaperHistoryValid_Type()
)
f3L3QosShaperHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperHistoryValid.setStatus("current")
_F3L3QosShaperHistoryAction_Type = CmPmBinAction
_F3L3QosShaperHistoryAction_Object = MibTableColumn
f3L3QosShaperHistoryAction = _F3L3QosShaperHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 14, 1, 4),
    _F3L3QosShaperHistoryAction_Type()
)
f3L3QosShaperHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3QosShaperHistoryAction.setStatus("current")
_F3L3QosShaperHistoryBT_Type = PerfCounter64
_F3L3QosShaperHistoryBT_Object = MibTableColumn
f3L3QosShaperHistoryBT = _F3L3QosShaperHistoryBT_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 14, 1, 5),
    _F3L3QosShaperHistoryBT_Type()
)
f3L3QosShaperHistoryBT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperHistoryBT.setStatus("current")
_F3L3QosShaperHistoryBTD_Type = PerfCounter64
_F3L3QosShaperHistoryBTD_Object = MibTableColumn
f3L3QosShaperHistoryBTD = _F3L3QosShaperHistoryBTD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 14, 1, 6),
    _F3L3QosShaperHistoryBTD_Type()
)
f3L3QosShaperHistoryBTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperHistoryBTD.setStatus("current")
_F3L3QosShaperHistoryFD_Type = PerfCounter64
_F3L3QosShaperHistoryFD_Object = MibTableColumn
f3L3QosShaperHistoryFD = _F3L3QosShaperHistoryFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 14, 1, 7),
    _F3L3QosShaperHistoryFD_Type()
)
f3L3QosShaperHistoryFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperHistoryFD.setStatus("current")
_F3L3QosShaperHistoryFTD_Type = PerfCounter64
_F3L3QosShaperHistoryFTD_Object = MibTableColumn
f3L3QosShaperHistoryFTD = _F3L3QosShaperHistoryFTD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 14, 1, 8),
    _F3L3QosShaperHistoryFTD_Type()
)
f3L3QosShaperHistoryFTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperHistoryFTD.setStatus("current")
_F3L3QosShaperHistoryBR_Type = PerfCounter64
_F3L3QosShaperHistoryBR_Object = MibTableColumn
f3L3QosShaperHistoryBR = _F3L3QosShaperHistoryBR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 14, 1, 9),
    _F3L3QosShaperHistoryBR_Type()
)
f3L3QosShaperHistoryBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperHistoryBR.setStatus("current")
_F3L3QosShaperHistoryFR_Type = PerfCounter64
_F3L3QosShaperHistoryFR_Object = MibTableColumn
f3L3QosShaperHistoryFR = _F3L3QosShaperHistoryFR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 14, 1, 10),
    _F3L3QosShaperHistoryFR_Type()
)
f3L3QosShaperHistoryFR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperHistoryFR.setStatus("current")
_F3L3QosShaperHistoryABRRL_Type = PerfCounter64
_F3L3QosShaperHistoryABRRL_Object = MibTableColumn
f3L3QosShaperHistoryABRRL = _F3L3QosShaperHistoryABRRL_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 14, 1, 11),
    _F3L3QosShaperHistoryABRRL_Type()
)
f3L3QosShaperHistoryABRRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperHistoryABRRL.setStatus("current")
_F3L3QosShaperHistoryABRRLR_Type = PerfCounter64
_F3L3QosShaperHistoryABRRLR_Object = MibTableColumn
f3L3QosShaperHistoryABRRLR = _F3L3QosShaperHistoryABRRLR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 14, 1, 12),
    _F3L3QosShaperHistoryABRRLR_Type()
)
f3L3QosShaperHistoryABRRLR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperHistoryABRRLR.setStatus("current")
_F3L3QosShaperHistoryBREDD_Type = PerfCounter64
_F3L3QosShaperHistoryBREDD_Object = MibTableColumn
f3L3QosShaperHistoryBREDD = _F3L3QosShaperHistoryBREDD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 14, 1, 13),
    _F3L3QosShaperHistoryBREDD_Type()
)
f3L3QosShaperHistoryBREDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperHistoryBREDD.setStatus("current")
_F3L3QosShaperHistoryFREDD_Type = PerfCounter64
_F3L3QosShaperHistoryFREDD_Object = MibTableColumn
f3L3QosShaperHistoryFREDD = _F3L3QosShaperHistoryFREDD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 14, 1, 14),
    _F3L3QosShaperHistoryFREDD_Type()
)
f3L3QosShaperHistoryFREDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperHistoryFREDD.setStatus("current")
_F3L3QosShaperThresholdTable_Object = MibTable
f3L3QosShaperThresholdTable = _F3L3QosShaperThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 15)
)
if mibBuilder.loadTexts:
    f3L3QosShaperThresholdTable.setStatus("current")
_F3L3QosShaperThresholdEntry_Object = MibTableRow
f3L3QosShaperThresholdEntry = _F3L3QosShaperThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 15, 1)
)
f3L3QosShaperThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortTypeIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointIndex"),
    (0, "F3-L3-MIB", "f3L3QosShaperIndex"),
    (0, "F3-L3-MIB", "f3L3QosShaperStatsIndex"),
    (0, "F3-L3-MIB", "f3L3QosShaperThresholdIndex"),
)
if mibBuilder.loadTexts:
    f3L3QosShaperThresholdEntry.setStatus("current")


class _F3L3QosShaperThresholdIndex_Type(Integer32):
    """Custom type f3L3QosShaperThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3L3QosShaperThresholdIndex_Type.__name__ = "Integer32"
_F3L3QosShaperThresholdIndex_Object = MibTableColumn
f3L3QosShaperThresholdIndex = _F3L3QosShaperThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 15, 1, 1),
    _F3L3QosShaperThresholdIndex_Type()
)
f3L3QosShaperThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperThresholdIndex.setStatus("current")
_F3L3QosShaperThresholdInterval_Type = CmPmIntervalType
_F3L3QosShaperThresholdInterval_Object = MibTableColumn
f3L3QosShaperThresholdInterval = _F3L3QosShaperThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 15, 1, 2),
    _F3L3QosShaperThresholdInterval_Type()
)
f3L3QosShaperThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperThresholdInterval.setStatus("current")
_F3L3QosShaperThresholdVariable_Type = VariablePointer
_F3L3QosShaperThresholdVariable_Object = MibTableColumn
f3L3QosShaperThresholdVariable = _F3L3QosShaperThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 15, 1, 3),
    _F3L3QosShaperThresholdVariable_Type()
)
f3L3QosShaperThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperThresholdVariable.setStatus("current")
_F3L3QosShaperThresholdValueLo_Type = Unsigned32
_F3L3QosShaperThresholdValueLo_Object = MibTableColumn
f3L3QosShaperThresholdValueLo = _F3L3QosShaperThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 15, 1, 4),
    _F3L3QosShaperThresholdValueLo_Type()
)
f3L3QosShaperThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3QosShaperThresholdValueLo.setStatus("current")
_F3L3QosShaperThresholdValueHi_Type = Unsigned32
_F3L3QosShaperThresholdValueHi_Object = MibTableColumn
f3L3QosShaperThresholdValueHi = _F3L3QosShaperThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 15, 1, 5),
    _F3L3QosShaperThresholdValueHi_Type()
)
f3L3QosShaperThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3QosShaperThresholdValueHi.setStatus("current")
_F3L3QosShaperThresholdMonValue_Type = Counter64
_F3L3QosShaperThresholdMonValue_Object = MibTableColumn
f3L3QosShaperThresholdMonValue = _F3L3QosShaperThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 15, 1, 6),
    _F3L3QosShaperThresholdMonValue_Type()
)
f3L3QosShaperThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3QosShaperThresholdMonValue.setStatus("current")
_F3L2A2NAclRuleStatsTable_Object = MibTable
f3L2A2NAclRuleStatsTable = _F3L2A2NAclRuleStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 16)
)
if mibBuilder.loadTexts:
    f3L2A2NAclRuleStatsTable.setStatus("current")
_F3L2A2NAclRuleStatsEntry_Object = MibTableRow
f3L2A2NAclRuleStatsEntry = _F3L2A2NAclRuleStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 16, 1)
)
f3L2A2NAclRuleStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L2A2NAclRuleParentIndex"),
    (0, "F3-L3-MIB", "f3L2A2NAclRuleIndex"),
    (0, "F3-L3-MIB", "f3L2A2NAclRuleStatsIndex"),
)
if mibBuilder.loadTexts:
    f3L2A2NAclRuleStatsEntry.setStatus("current")


class _F3L2A2NAclRuleStatsIndex_Type(Integer32):
    """Custom type f3L2A2NAclRuleStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_F3L2A2NAclRuleStatsIndex_Type.__name__ = "Integer32"
_F3L2A2NAclRuleStatsIndex_Object = MibTableColumn
f3L2A2NAclRuleStatsIndex = _F3L2A2NAclRuleStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 16, 1, 1),
    _F3L2A2NAclRuleStatsIndex_Type()
)
f3L2A2NAclRuleStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleStatsIndex.setStatus("current")
_F3L2A2NAclRuleStatsIntervalType_Type = CmPmIntervalType
_F3L2A2NAclRuleStatsIntervalType_Object = MibTableColumn
f3L2A2NAclRuleStatsIntervalType = _F3L2A2NAclRuleStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 16, 1, 2),
    _F3L2A2NAclRuleStatsIntervalType_Type()
)
f3L2A2NAclRuleStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleStatsIntervalType.setStatus("current")
_F3L2A2NAclRuleStatsValid_Type = TruthValue
_F3L2A2NAclRuleStatsValid_Object = MibTableColumn
f3L2A2NAclRuleStatsValid = _F3L2A2NAclRuleStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 16, 1, 3),
    _F3L2A2NAclRuleStatsValid_Type()
)
f3L2A2NAclRuleStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleStatsValid.setStatus("current")
_F3L2A2NAclRuleStatsAction_Type = CmPmBinAction
_F3L2A2NAclRuleStatsAction_Object = MibTableColumn
f3L2A2NAclRuleStatsAction = _F3L2A2NAclRuleStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 16, 1, 4),
    _F3L2A2NAclRuleStatsAction_Type()
)
f3L2A2NAclRuleStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleStatsAction.setStatus("current")
_F3L2A2NAclRuleStatsRuleMatch_Type = PerfCounter64
_F3L2A2NAclRuleStatsRuleMatch_Object = MibTableColumn
f3L2A2NAclRuleStatsRuleMatch = _F3L2A2NAclRuleStatsRuleMatch_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 16, 1, 5),
    _F3L2A2NAclRuleStatsRuleMatch_Type()
)
f3L2A2NAclRuleStatsRuleMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleStatsRuleMatch.setStatus("current")
_F3L2A2NAclRuleHistoryTable_Object = MibTable
f3L2A2NAclRuleHistoryTable = _F3L2A2NAclRuleHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 17)
)
if mibBuilder.loadTexts:
    f3L2A2NAclRuleHistoryTable.setStatus("current")
_F3L2A2NAclRuleHistoryEntry_Object = MibTableRow
f3L2A2NAclRuleHistoryEntry = _F3L2A2NAclRuleHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 17, 1)
)
f3L2A2NAclRuleHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L2A2NAclRuleParentIndex"),
    (0, "F3-L3-MIB", "f3L2A2NAclRuleIndex"),
    (0, "F3-L3-MIB", "f3L2A2NAclRuleStatsIndex"),
    (0, "F3-L3-MIB", "f3L2A2NAclRuleHistoryIndex"),
)
if mibBuilder.loadTexts:
    f3L2A2NAclRuleHistoryEntry.setStatus("current")


class _F3L2A2NAclRuleHistoryIndex_Type(Integer32):
    """Custom type f3L2A2NAclRuleHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3L2A2NAclRuleHistoryIndex_Type.__name__ = "Integer32"
_F3L2A2NAclRuleHistoryIndex_Object = MibTableColumn
f3L2A2NAclRuleHistoryIndex = _F3L2A2NAclRuleHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 17, 1, 1),
    _F3L2A2NAclRuleHistoryIndex_Type()
)
f3L2A2NAclRuleHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleHistoryIndex.setStatus("current")
_F3L2A2NAclRuleHistoryTime_Type = DateAndTime
_F3L2A2NAclRuleHistoryTime_Object = MibTableColumn
f3L2A2NAclRuleHistoryTime = _F3L2A2NAclRuleHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 17, 1, 2),
    _F3L2A2NAclRuleHistoryTime_Type()
)
f3L2A2NAclRuleHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleHistoryTime.setStatus("current")
_F3L2A2NAclRuleHistoryValid_Type = TruthValue
_F3L2A2NAclRuleHistoryValid_Object = MibTableColumn
f3L2A2NAclRuleHistoryValid = _F3L2A2NAclRuleHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 17, 1, 3),
    _F3L2A2NAclRuleHistoryValid_Type()
)
f3L2A2NAclRuleHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleHistoryValid.setStatus("current")
_F3L2A2NAclRuleHistoryAction_Type = CmPmBinAction
_F3L2A2NAclRuleHistoryAction_Object = MibTableColumn
f3L2A2NAclRuleHistoryAction = _F3L2A2NAclRuleHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 17, 1, 4),
    _F3L2A2NAclRuleHistoryAction_Type()
)
f3L2A2NAclRuleHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleHistoryAction.setStatus("current")
_F3L2A2NAclRuleHistoryRuleMatch_Type = PerfCounter64
_F3L2A2NAclRuleHistoryRuleMatch_Object = MibTableColumn
f3L2A2NAclRuleHistoryRuleMatch = _F3L2A2NAclRuleHistoryRuleMatch_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 17, 1, 5),
    _F3L2A2NAclRuleHistoryRuleMatch_Type()
)
f3L2A2NAclRuleHistoryRuleMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleHistoryRuleMatch.setStatus("current")
_F3L2A2NAclRuleThresholdTable_Object = MibTable
f3L2A2NAclRuleThresholdTable = _F3L2A2NAclRuleThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 18)
)
if mibBuilder.loadTexts:
    f3L2A2NAclRuleThresholdTable.setStatus("current")
_F3L2A2NAclRuleThresholdEntry_Object = MibTableRow
f3L2A2NAclRuleThresholdEntry = _F3L2A2NAclRuleThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 18, 1)
)
f3L2A2NAclRuleThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L2A2NAclRuleParentIndex"),
    (0, "F3-L3-MIB", "f3L2A2NAclRuleIndex"),
    (0, "F3-L3-MIB", "f3L2A2NAclRuleStatsIndex"),
    (0, "F3-L3-MIB", "f3L2A2NAclRuleThresholdIndex"),
)
if mibBuilder.loadTexts:
    f3L2A2NAclRuleThresholdEntry.setStatus("current")


class _F3L2A2NAclRuleThresholdIndex_Type(Integer32):
    """Custom type f3L2A2NAclRuleThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3L2A2NAclRuleThresholdIndex_Type.__name__ = "Integer32"
_F3L2A2NAclRuleThresholdIndex_Object = MibTableColumn
f3L2A2NAclRuleThresholdIndex = _F3L2A2NAclRuleThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 18, 1, 1),
    _F3L2A2NAclRuleThresholdIndex_Type()
)
f3L2A2NAclRuleThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleThresholdIndex.setStatus("current")
_F3L2A2NAclRuleThresholdInterval_Type = CmPmIntervalType
_F3L2A2NAclRuleThresholdInterval_Object = MibTableColumn
f3L2A2NAclRuleThresholdInterval = _F3L2A2NAclRuleThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 18, 1, 2),
    _F3L2A2NAclRuleThresholdInterval_Type()
)
f3L2A2NAclRuleThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleThresholdInterval.setStatus("current")
_F3L2A2NAclRuleThresholdVariable_Type = VariablePointer
_F3L2A2NAclRuleThresholdVariable_Object = MibTableColumn
f3L2A2NAclRuleThresholdVariable = _F3L2A2NAclRuleThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 18, 1, 3),
    _F3L2A2NAclRuleThresholdVariable_Type()
)
f3L2A2NAclRuleThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleThresholdVariable.setStatus("current")
_F3L2A2NAclRuleThresholdValueLo_Type = Unsigned32
_F3L2A2NAclRuleThresholdValueLo_Object = MibTableColumn
f3L2A2NAclRuleThresholdValueLo = _F3L2A2NAclRuleThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 18, 1, 4),
    _F3L2A2NAclRuleThresholdValueLo_Type()
)
f3L2A2NAclRuleThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleThresholdValueLo.setStatus("current")
_F3L2A2NAclRuleThresholdValueHi_Type = Unsigned32
_F3L2A2NAclRuleThresholdValueHi_Object = MibTableColumn
f3L2A2NAclRuleThresholdValueHi = _F3L2A2NAclRuleThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 18, 1, 5),
    _F3L2A2NAclRuleThresholdValueHi_Type()
)
f3L2A2NAclRuleThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleThresholdValueHi.setStatus("current")
_F3L2A2NAclRuleThresholdMonValue_Type = Counter64
_F3L2A2NAclRuleThresholdMonValue_Object = MibTableColumn
f3L2A2NAclRuleThresholdMonValue = _F3L2A2NAclRuleThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 18, 1, 6),
    _F3L2A2NAclRuleThresholdMonValue_Type()
)
f3L2A2NAclRuleThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L2A2NAclRuleThresholdMonValue.setStatus("current")
_F3L2N2AAclRuleStatsTable_Object = MibTable
f3L2N2AAclRuleStatsTable = _F3L2N2AAclRuleStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 19)
)
if mibBuilder.loadTexts:
    f3L2N2AAclRuleStatsTable.setStatus("current")
_F3L2N2AAclRuleStatsEntry_Object = MibTableRow
f3L2N2AAclRuleStatsEntry = _F3L2N2AAclRuleStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 19, 1)
)
f3L2N2AAclRuleStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L2N2AAclRuleParentIndex"),
    (0, "F3-L3-MIB", "f3L2N2AAclRuleIndex"),
    (0, "F3-L3-MIB", "f3L2N2AAclRuleStatsIndex"),
)
if mibBuilder.loadTexts:
    f3L2N2AAclRuleStatsEntry.setStatus("current")


class _F3L2N2AAclRuleStatsIndex_Type(Integer32):
    """Custom type f3L2N2AAclRuleStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_F3L2N2AAclRuleStatsIndex_Type.__name__ = "Integer32"
_F3L2N2AAclRuleStatsIndex_Object = MibTableColumn
f3L2N2AAclRuleStatsIndex = _F3L2N2AAclRuleStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 19, 1, 1),
    _F3L2N2AAclRuleStatsIndex_Type()
)
f3L2N2AAclRuleStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleStatsIndex.setStatus("current")
_F3L2N2AAclRuleStatsIntervalType_Type = CmPmIntervalType
_F3L2N2AAclRuleStatsIntervalType_Object = MibTableColumn
f3L2N2AAclRuleStatsIntervalType = _F3L2N2AAclRuleStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 19, 1, 2),
    _F3L2N2AAclRuleStatsIntervalType_Type()
)
f3L2N2AAclRuleStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleStatsIntervalType.setStatus("current")
_F3L2N2AAclRuleStatsValid_Type = TruthValue
_F3L2N2AAclRuleStatsValid_Object = MibTableColumn
f3L2N2AAclRuleStatsValid = _F3L2N2AAclRuleStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 19, 1, 3),
    _F3L2N2AAclRuleStatsValid_Type()
)
f3L2N2AAclRuleStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleStatsValid.setStatus("current")
_F3L2N2AAclRuleStatsAction_Type = CmPmBinAction
_F3L2N2AAclRuleStatsAction_Object = MibTableColumn
f3L2N2AAclRuleStatsAction = _F3L2N2AAclRuleStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 19, 1, 4),
    _F3L2N2AAclRuleStatsAction_Type()
)
f3L2N2AAclRuleStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleStatsAction.setStatus("current")
_F3L2N2AAclRuleStatsRuleMatch_Type = PerfCounter64
_F3L2N2AAclRuleStatsRuleMatch_Object = MibTableColumn
f3L2N2AAclRuleStatsRuleMatch = _F3L2N2AAclRuleStatsRuleMatch_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 19, 1, 5),
    _F3L2N2AAclRuleStatsRuleMatch_Type()
)
f3L2N2AAclRuleStatsRuleMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleStatsRuleMatch.setStatus("current")
_F3L2N2AAclRuleHistoryTable_Object = MibTable
f3L2N2AAclRuleHistoryTable = _F3L2N2AAclRuleHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 20)
)
if mibBuilder.loadTexts:
    f3L2N2AAclRuleHistoryTable.setStatus("current")
_F3L2N2AAclRuleHistoryEntry_Object = MibTableRow
f3L2N2AAclRuleHistoryEntry = _F3L2N2AAclRuleHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 20, 1)
)
f3L2N2AAclRuleHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L2N2AAclRuleParentIndex"),
    (0, "F3-L3-MIB", "f3L2N2AAclRuleIndex"),
    (0, "F3-L3-MIB", "f3L2N2AAclRuleStatsIndex"),
    (0, "F3-L3-MIB", "f3L2N2AAclRuleHistoryIndex"),
)
if mibBuilder.loadTexts:
    f3L2N2AAclRuleHistoryEntry.setStatus("current")


class _F3L2N2AAclRuleHistoryIndex_Type(Integer32):
    """Custom type f3L2N2AAclRuleHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3L2N2AAclRuleHistoryIndex_Type.__name__ = "Integer32"
_F3L2N2AAclRuleHistoryIndex_Object = MibTableColumn
f3L2N2AAclRuleHistoryIndex = _F3L2N2AAclRuleHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 20, 1, 1),
    _F3L2N2AAclRuleHistoryIndex_Type()
)
f3L2N2AAclRuleHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleHistoryIndex.setStatus("current")
_F3L2N2AAclRuleHistoryTime_Type = DateAndTime
_F3L2N2AAclRuleHistoryTime_Object = MibTableColumn
f3L2N2AAclRuleHistoryTime = _F3L2N2AAclRuleHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 20, 1, 2),
    _F3L2N2AAclRuleHistoryTime_Type()
)
f3L2N2AAclRuleHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleHistoryTime.setStatus("current")
_F3L2N2AAclRuleHistoryValid_Type = TruthValue
_F3L2N2AAclRuleHistoryValid_Object = MibTableColumn
f3L2N2AAclRuleHistoryValid = _F3L2N2AAclRuleHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 20, 1, 3),
    _F3L2N2AAclRuleHistoryValid_Type()
)
f3L2N2AAclRuleHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleHistoryValid.setStatus("current")
_F3L2N2AAclRuleHistoryAction_Type = CmPmBinAction
_F3L2N2AAclRuleHistoryAction_Object = MibTableColumn
f3L2N2AAclRuleHistoryAction = _F3L2N2AAclRuleHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 20, 1, 4),
    _F3L2N2AAclRuleHistoryAction_Type()
)
f3L2N2AAclRuleHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleHistoryAction.setStatus("current")
_F3L2N2AAclRuleHistoryRuleMatch_Type = PerfCounter64
_F3L2N2AAclRuleHistoryRuleMatch_Object = MibTableColumn
f3L2N2AAclRuleHistoryRuleMatch = _F3L2N2AAclRuleHistoryRuleMatch_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 20, 1, 5),
    _F3L2N2AAclRuleHistoryRuleMatch_Type()
)
f3L2N2AAclRuleHistoryRuleMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleHistoryRuleMatch.setStatus("current")
_F3L2N2AAclRuleThresholdTable_Object = MibTable
f3L2N2AAclRuleThresholdTable = _F3L2N2AAclRuleThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 21)
)
if mibBuilder.loadTexts:
    f3L2N2AAclRuleThresholdTable.setStatus("current")
_F3L2N2AAclRuleThresholdEntry_Object = MibTableRow
f3L2N2AAclRuleThresholdEntry = _F3L2N2AAclRuleThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 21, 1)
)
f3L2N2AAclRuleThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L2N2AAclRuleParentIndex"),
    (0, "F3-L3-MIB", "f3L2N2AAclRuleIndex"),
    (0, "F3-L3-MIB", "f3L2N2AAclRuleStatsIndex"),
    (0, "F3-L3-MIB", "f3L2N2AAclRuleThresholdIndex"),
)
if mibBuilder.loadTexts:
    f3L2N2AAclRuleThresholdEntry.setStatus("current")


class _F3L2N2AAclRuleThresholdIndex_Type(Integer32):
    """Custom type f3L2N2AAclRuleThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3L2N2AAclRuleThresholdIndex_Type.__name__ = "Integer32"
_F3L2N2AAclRuleThresholdIndex_Object = MibTableColumn
f3L2N2AAclRuleThresholdIndex = _F3L2N2AAclRuleThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 21, 1, 1),
    _F3L2N2AAclRuleThresholdIndex_Type()
)
f3L2N2AAclRuleThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleThresholdIndex.setStatus("current")
_F3L2N2AAclRuleThresholdInterval_Type = CmPmIntervalType
_F3L2N2AAclRuleThresholdInterval_Object = MibTableColumn
f3L2N2AAclRuleThresholdInterval = _F3L2N2AAclRuleThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 21, 1, 2),
    _F3L2N2AAclRuleThresholdInterval_Type()
)
f3L2N2AAclRuleThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleThresholdInterval.setStatus("current")
_F3L2N2AAclRuleThresholdVariable_Type = VariablePointer
_F3L2N2AAclRuleThresholdVariable_Object = MibTableColumn
f3L2N2AAclRuleThresholdVariable = _F3L2N2AAclRuleThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 21, 1, 3),
    _F3L2N2AAclRuleThresholdVariable_Type()
)
f3L2N2AAclRuleThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleThresholdVariable.setStatus("current")
_F3L2N2AAclRuleThresholdValueLo_Type = Unsigned32
_F3L2N2AAclRuleThresholdValueLo_Object = MibTableColumn
f3L2N2AAclRuleThresholdValueLo = _F3L2N2AAclRuleThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 21, 1, 4),
    _F3L2N2AAclRuleThresholdValueLo_Type()
)
f3L2N2AAclRuleThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleThresholdValueLo.setStatus("current")
_F3L2N2AAclRuleThresholdValueHi_Type = Unsigned32
_F3L2N2AAclRuleThresholdValueHi_Object = MibTableColumn
f3L2N2AAclRuleThresholdValueHi = _F3L2N2AAclRuleThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 21, 1, 5),
    _F3L2N2AAclRuleThresholdValueHi_Type()
)
f3L2N2AAclRuleThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleThresholdValueHi.setStatus("current")
_F3L2N2AAclRuleThresholdMonValue_Type = Counter64
_F3L2N2AAclRuleThresholdMonValue_Object = MibTableColumn
f3L2N2AAclRuleThresholdMonValue = _F3L2N2AAclRuleThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 21, 1, 6),
    _F3L2N2AAclRuleThresholdMonValue_Type()
)
f3L2N2AAclRuleThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L2N2AAclRuleThresholdMonValue.setStatus("current")
_F3L3TrafficIPv6InterfaceStatsTable_Object = MibTable
f3L3TrafficIPv6InterfaceStatsTable = _F3L3TrafficIPv6InterfaceStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 22)
)
if mibBuilder.loadTexts:
    f3L3TrafficIPv6InterfaceStatsTable.setStatus("current")
_F3L3TrafficIPv6InterfaceStatsEntry_Object = MibTableRow
f3L3TrafficIPv6InterfaceStatsEntry = _F3L3TrafficIPv6InterfaceStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 22, 1)
)
f3L3TrafficIPv6InterfaceStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficIPv6IfIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficIPv6InterfaceStatsIndex"),
)
if mibBuilder.loadTexts:
    f3L3TrafficIPv6InterfaceStatsEntry.setStatus("current")


class _F3L3TrafficIPv6InterfaceStatsIndex_Type(Integer32):
    """Custom type f3L3TrafficIPv6InterfaceStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_F3L3TrafficIPv6InterfaceStatsIndex_Type.__name__ = "Integer32"
_F3L3TrafficIPv6InterfaceStatsIndex_Object = MibTableColumn
f3L3TrafficIPv6InterfaceStatsIndex = _F3L3TrafficIPv6InterfaceStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 22, 1, 1),
    _F3L3TrafficIPv6InterfaceStatsIndex_Type()
)
f3L3TrafficIPv6InterfaceStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6InterfaceStatsIndex.setStatus("current")
_F3L3TrafficIPv6InterfaceStatsIntervalType_Type = CmPmIntervalType
_F3L3TrafficIPv6InterfaceStatsIntervalType_Object = MibTableColumn
f3L3TrafficIPv6InterfaceStatsIntervalType = _F3L3TrafficIPv6InterfaceStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 22, 1, 2),
    _F3L3TrafficIPv6InterfaceStatsIntervalType_Type()
)
f3L3TrafficIPv6InterfaceStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6InterfaceStatsIntervalType.setStatus("current")
_F3L3TrafficIPv6InterfaceStatsValid_Type = TruthValue
_F3L3TrafficIPv6InterfaceStatsValid_Object = MibTableColumn
f3L3TrafficIPv6InterfaceStatsValid = _F3L3TrafficIPv6InterfaceStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 22, 1, 3),
    _F3L3TrafficIPv6InterfaceStatsValid_Type()
)
f3L3TrafficIPv6InterfaceStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6InterfaceStatsValid.setStatus("current")
_F3L3TrafficIPv6InterfaceStatsAction_Type = CmPmBinAction
_F3L3TrafficIPv6InterfaceStatsAction_Object = MibTableColumn
f3L3TrafficIPv6InterfaceStatsAction = _F3L3TrafficIPv6InterfaceStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 22, 1, 4),
    _F3L3TrafficIPv6InterfaceStatsAction_Type()
)
f3L3TrafficIPv6InterfaceStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6InterfaceStatsAction.setStatus("current")
_F3L3TrafficIPv6InterfaceStatsDhcpV6Tx_Type = PerfCounter64
_F3L3TrafficIPv6InterfaceStatsDhcpV6Tx_Object = MibTableColumn
f3L3TrafficIPv6InterfaceStatsDhcpV6Tx = _F3L3TrafficIPv6InterfaceStatsDhcpV6Tx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 22, 1, 5),
    _F3L3TrafficIPv6InterfaceStatsDhcpV6Tx_Type()
)
f3L3TrafficIPv6InterfaceStatsDhcpV6Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6InterfaceStatsDhcpV6Tx.setStatus("current")
_F3L3TrafficIPv6InterfaceStatsDhcpV6Rx_Type = PerfCounter64
_F3L3TrafficIPv6InterfaceStatsDhcpV6Rx_Object = MibTableColumn
f3L3TrafficIPv6InterfaceStatsDhcpV6Rx = _F3L3TrafficIPv6InterfaceStatsDhcpV6Rx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 22, 1, 6),
    _F3L3TrafficIPv6InterfaceStatsDhcpV6Rx_Type()
)
f3L3TrafficIPv6InterfaceStatsDhcpV6Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6InterfaceStatsDhcpV6Rx.setStatus("current")
_F3L3TrafficIPv6InterfaceStatsIcmpV6WONdpTx_Type = PerfCounter64
_F3L3TrafficIPv6InterfaceStatsIcmpV6WONdpTx_Object = MibTableColumn
f3L3TrafficIPv6InterfaceStatsIcmpV6WONdpTx = _F3L3TrafficIPv6InterfaceStatsIcmpV6WONdpTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 22, 1, 7),
    _F3L3TrafficIPv6InterfaceStatsIcmpV6WONdpTx_Type()
)
f3L3TrafficIPv6InterfaceStatsIcmpV6WONdpTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6InterfaceStatsIcmpV6WONdpTx.setStatus("current")
_F3L3TrafficIPv6InterfaceStatsIcmpV6WONdpRx_Type = PerfCounter64
_F3L3TrafficIPv6InterfaceStatsIcmpV6WONdpRx_Object = MibTableColumn
f3L3TrafficIPv6InterfaceStatsIcmpV6WONdpRx = _F3L3TrafficIPv6InterfaceStatsIcmpV6WONdpRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 22, 1, 8),
    _F3L3TrafficIPv6InterfaceStatsIcmpV6WONdpRx_Type()
)
f3L3TrafficIPv6InterfaceStatsIcmpV6WONdpRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6InterfaceStatsIcmpV6WONdpRx.setStatus("current")
_F3L3TrafficIPv6InterfaceStatsNdpNSTx_Type = PerfCounter64
_F3L3TrafficIPv6InterfaceStatsNdpNSTx_Object = MibTableColumn
f3L3TrafficIPv6InterfaceStatsNdpNSTx = _F3L3TrafficIPv6InterfaceStatsNdpNSTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 22, 1, 9),
    _F3L3TrafficIPv6InterfaceStatsNdpNSTx_Type()
)
f3L3TrafficIPv6InterfaceStatsNdpNSTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6InterfaceStatsNdpNSTx.setStatus("current")
_F3L3TrafficIPv6InterfaceStatsNdpNSRx_Type = PerfCounter64
_F3L3TrafficIPv6InterfaceStatsNdpNSRx_Object = MibTableColumn
f3L3TrafficIPv6InterfaceStatsNdpNSRx = _F3L3TrafficIPv6InterfaceStatsNdpNSRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 22, 1, 10),
    _F3L3TrafficIPv6InterfaceStatsNdpNSRx_Type()
)
f3L3TrafficIPv6InterfaceStatsNdpNSRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6InterfaceStatsNdpNSRx.setStatus("current")
_F3L3TrafficIPv6InterfaceStatsNdpNATx_Type = PerfCounter64
_F3L3TrafficIPv6InterfaceStatsNdpNATx_Object = MibTableColumn
f3L3TrafficIPv6InterfaceStatsNdpNATx = _F3L3TrafficIPv6InterfaceStatsNdpNATx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 22, 1, 11),
    _F3L3TrafficIPv6InterfaceStatsNdpNATx_Type()
)
f3L3TrafficIPv6InterfaceStatsNdpNATx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6InterfaceStatsNdpNATx.setStatus("current")
_F3L3TrafficIPv6InterfaceStatsNdpNARx_Type = PerfCounter64
_F3L3TrafficIPv6InterfaceStatsNdpNARx_Object = MibTableColumn
f3L3TrafficIPv6InterfaceStatsNdpNARx = _F3L3TrafficIPv6InterfaceStatsNdpNARx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 22, 1, 12),
    _F3L3TrafficIPv6InterfaceStatsNdpNARx_Type()
)
f3L3TrafficIPv6InterfaceStatsNdpNARx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6InterfaceStatsNdpNARx.setStatus("current")
_F3L3TrafficIPv6InterfaceStatsNdpRATx_Type = PerfCounter64
_F3L3TrafficIPv6InterfaceStatsNdpRATx_Object = MibTableColumn
f3L3TrafficIPv6InterfaceStatsNdpRATx = _F3L3TrafficIPv6InterfaceStatsNdpRATx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 22, 1, 13),
    _F3L3TrafficIPv6InterfaceStatsNdpRATx_Type()
)
f3L3TrafficIPv6InterfaceStatsNdpRATx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6InterfaceStatsNdpRATx.setStatus("current")
_F3L3TrafficIPv6InterfaceStatsNdpRARx_Type = PerfCounter64
_F3L3TrafficIPv6InterfaceStatsNdpRARx_Object = MibTableColumn
f3L3TrafficIPv6InterfaceStatsNdpRARx = _F3L3TrafficIPv6InterfaceStatsNdpRARx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 22, 1, 14),
    _F3L3TrafficIPv6InterfaceStatsNdpRARx_Type()
)
f3L3TrafficIPv6InterfaceStatsNdpRARx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6InterfaceStatsNdpRARx.setStatus("current")
_F3L3TrafficIPv6InterfaceStatsNdpRSTx_Type = PerfCounter64
_F3L3TrafficIPv6InterfaceStatsNdpRSTx_Object = MibTableColumn
f3L3TrafficIPv6InterfaceStatsNdpRSTx = _F3L3TrafficIPv6InterfaceStatsNdpRSTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 22, 1, 15),
    _F3L3TrafficIPv6InterfaceStatsNdpRSTx_Type()
)
f3L3TrafficIPv6InterfaceStatsNdpRSTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6InterfaceStatsNdpRSTx.setStatus("current")
_F3L3TrafficIPv6InterfaceStatsNdpRSRx_Type = PerfCounter64
_F3L3TrafficIPv6InterfaceStatsNdpRSRx_Object = MibTableColumn
f3L3TrafficIPv6InterfaceStatsNdpRSRx = _F3L3TrafficIPv6InterfaceStatsNdpRSRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 22, 1, 16),
    _F3L3TrafficIPv6InterfaceStatsNdpRSRx_Type()
)
f3L3TrafficIPv6InterfaceStatsNdpRSRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6InterfaceStatsNdpRSRx.setStatus("current")
_F3L3TrafficIPv6InterfaceHistoryTable_Object = MibTable
f3L3TrafficIPv6InterfaceHistoryTable = _F3L3TrafficIPv6InterfaceHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 23)
)
if mibBuilder.loadTexts:
    f3L3TrafficIPv6InterfaceHistoryTable.setStatus("current")
_F3L3TrafficIPv6InterfaceHistoryEntry_Object = MibTableRow
f3L3TrafficIPv6InterfaceHistoryEntry = _F3L3TrafficIPv6InterfaceHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 23, 1)
)
f3L3TrafficIPv6InterfaceHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficIPv6IfIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficIPv6InterfaceStatsIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficIPv6InterfaceHistoryIndex"),
)
if mibBuilder.loadTexts:
    f3L3TrafficIPv6InterfaceHistoryEntry.setStatus("current")


class _F3L3TrafficIPv6InterfaceHistoryIndex_Type(Integer32):
    """Custom type f3L3TrafficIPv6InterfaceHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_F3L3TrafficIPv6InterfaceHistoryIndex_Type.__name__ = "Integer32"
_F3L3TrafficIPv6InterfaceHistoryIndex_Object = MibTableColumn
f3L3TrafficIPv6InterfaceHistoryIndex = _F3L3TrafficIPv6InterfaceHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 23, 1, 1),
    _F3L3TrafficIPv6InterfaceHistoryIndex_Type()
)
f3L3TrafficIPv6InterfaceHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6InterfaceHistoryIndex.setStatus("current")
_F3L3TrafficIPv6InterfaceHistoryTime_Type = DateAndTime
_F3L3TrafficIPv6InterfaceHistoryTime_Object = MibTableColumn
f3L3TrafficIPv6InterfaceHistoryTime = _F3L3TrafficIPv6InterfaceHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 23, 1, 2),
    _F3L3TrafficIPv6InterfaceHistoryTime_Type()
)
f3L3TrafficIPv6InterfaceHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6InterfaceHistoryTime.setStatus("current")
_F3L3TrafficIPv6InterfaceHistoryValid_Type = TruthValue
_F3L3TrafficIPv6InterfaceHistoryValid_Object = MibTableColumn
f3L3TrafficIPv6InterfaceHistoryValid = _F3L3TrafficIPv6InterfaceHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 23, 1, 3),
    _F3L3TrafficIPv6InterfaceHistoryValid_Type()
)
f3L3TrafficIPv6InterfaceHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6InterfaceHistoryValid.setStatus("current")
_F3L3TrafficIPv6InterfaceHistoryAction_Type = CmPmBinAction
_F3L3TrafficIPv6InterfaceHistoryAction_Object = MibTableColumn
f3L3TrafficIPv6InterfaceHistoryAction = _F3L3TrafficIPv6InterfaceHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 23, 1, 4),
    _F3L3TrafficIPv6InterfaceHistoryAction_Type()
)
f3L3TrafficIPv6InterfaceHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6InterfaceHistoryAction.setStatus("current")
_F3L3TrafficIPv6InterfaceHistoryDhcpV6Tx_Type = PerfCounter64
_F3L3TrafficIPv6InterfaceHistoryDhcpV6Tx_Object = MibTableColumn
f3L3TrafficIPv6InterfaceHistoryDhcpV6Tx = _F3L3TrafficIPv6InterfaceHistoryDhcpV6Tx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 23, 1, 5),
    _F3L3TrafficIPv6InterfaceHistoryDhcpV6Tx_Type()
)
f3L3TrafficIPv6InterfaceHistoryDhcpV6Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6InterfaceHistoryDhcpV6Tx.setStatus("current")
_F3L3TrafficIPv6InterfaceHistoryDhcpV6Rx_Type = PerfCounter64
_F3L3TrafficIPv6InterfaceHistoryDhcpV6Rx_Object = MibTableColumn
f3L3TrafficIPv6InterfaceHistoryDhcpV6Rx = _F3L3TrafficIPv6InterfaceHistoryDhcpV6Rx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 23, 1, 6),
    _F3L3TrafficIPv6InterfaceHistoryDhcpV6Rx_Type()
)
f3L3TrafficIPv6InterfaceHistoryDhcpV6Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6InterfaceHistoryDhcpV6Rx.setStatus("current")
_F3L3TrafficIPv6InterfaceHistoryIcmpV6WONdpTx_Type = PerfCounter64
_F3L3TrafficIPv6InterfaceHistoryIcmpV6WONdpTx_Object = MibTableColumn
f3L3TrafficIPv6InterfaceHistoryIcmpV6WONdpTx = _F3L3TrafficIPv6InterfaceHistoryIcmpV6WONdpTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 23, 1, 7),
    _F3L3TrafficIPv6InterfaceHistoryIcmpV6WONdpTx_Type()
)
f3L3TrafficIPv6InterfaceHistoryIcmpV6WONdpTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6InterfaceHistoryIcmpV6WONdpTx.setStatus("current")
_F3L3TrafficIPv6InterfaceHistoryIcmpV6WONdpRx_Type = PerfCounter64
_F3L3TrafficIPv6InterfaceHistoryIcmpV6WONdpRx_Object = MibTableColumn
f3L3TrafficIPv6InterfaceHistoryIcmpV6WONdpRx = _F3L3TrafficIPv6InterfaceHistoryIcmpV6WONdpRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 23, 1, 8),
    _F3L3TrafficIPv6InterfaceHistoryIcmpV6WONdpRx_Type()
)
f3L3TrafficIPv6InterfaceHistoryIcmpV6WONdpRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6InterfaceHistoryIcmpV6WONdpRx.setStatus("current")
_F3L3TrafficIPv6InterfaceHistoryNdpNSTx_Type = PerfCounter64
_F3L3TrafficIPv6InterfaceHistoryNdpNSTx_Object = MibTableColumn
f3L3TrafficIPv6InterfaceHistoryNdpNSTx = _F3L3TrafficIPv6InterfaceHistoryNdpNSTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 23, 1, 9),
    _F3L3TrafficIPv6InterfaceHistoryNdpNSTx_Type()
)
f3L3TrafficIPv6InterfaceHistoryNdpNSTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6InterfaceHistoryNdpNSTx.setStatus("current")
_F3L3TrafficIPv6InterfaceHistoryNdpNSRx_Type = PerfCounter64
_F3L3TrafficIPv6InterfaceHistoryNdpNSRx_Object = MibTableColumn
f3L3TrafficIPv6InterfaceHistoryNdpNSRx = _F3L3TrafficIPv6InterfaceHistoryNdpNSRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 23, 1, 10),
    _F3L3TrafficIPv6InterfaceHistoryNdpNSRx_Type()
)
f3L3TrafficIPv6InterfaceHistoryNdpNSRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6InterfaceHistoryNdpNSRx.setStatus("current")
_F3L3TrafficIPv6InterfaceHistoryNdpNATx_Type = PerfCounter64
_F3L3TrafficIPv6InterfaceHistoryNdpNATx_Object = MibTableColumn
f3L3TrafficIPv6InterfaceHistoryNdpNATx = _F3L3TrafficIPv6InterfaceHistoryNdpNATx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 23, 1, 11),
    _F3L3TrafficIPv6InterfaceHistoryNdpNATx_Type()
)
f3L3TrafficIPv6InterfaceHistoryNdpNATx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6InterfaceHistoryNdpNATx.setStatus("current")
_F3L3TrafficIPv6InterfaceHistoryNdpNARx_Type = PerfCounter64
_F3L3TrafficIPv6InterfaceHistoryNdpNARx_Object = MibTableColumn
f3L3TrafficIPv6InterfaceHistoryNdpNARx = _F3L3TrafficIPv6InterfaceHistoryNdpNARx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 23, 1, 12),
    _F3L3TrafficIPv6InterfaceHistoryNdpNARx_Type()
)
f3L3TrafficIPv6InterfaceHistoryNdpNARx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6InterfaceHistoryNdpNARx.setStatus("current")
_F3L3TrafficIPv6InterfaceHistoryNdpRATx_Type = PerfCounter64
_F3L3TrafficIPv6InterfaceHistoryNdpRATx_Object = MibTableColumn
f3L3TrafficIPv6InterfaceHistoryNdpRATx = _F3L3TrafficIPv6InterfaceHistoryNdpRATx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 23, 1, 13),
    _F3L3TrafficIPv6InterfaceHistoryNdpRATx_Type()
)
f3L3TrafficIPv6InterfaceHistoryNdpRATx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6InterfaceHistoryNdpRATx.setStatus("current")
_F3L3TrafficIPv6InterfaceHistoryNdpRARx_Type = PerfCounter64
_F3L3TrafficIPv6InterfaceHistoryNdpRARx_Object = MibTableColumn
f3L3TrafficIPv6InterfaceHistoryNdpRARx = _F3L3TrafficIPv6InterfaceHistoryNdpRARx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 23, 1, 14),
    _F3L3TrafficIPv6InterfaceHistoryNdpRARx_Type()
)
f3L3TrafficIPv6InterfaceHistoryNdpRARx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6InterfaceHistoryNdpRARx.setStatus("current")
_F3L3TrafficIPv6InterfaceHistoryNdpRSTx_Type = PerfCounter64
_F3L3TrafficIPv6InterfaceHistoryNdpRSTx_Object = MibTableColumn
f3L3TrafficIPv6InterfaceHistoryNdpRSTx = _F3L3TrafficIPv6InterfaceHistoryNdpRSTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 23, 1, 15),
    _F3L3TrafficIPv6InterfaceHistoryNdpRSTx_Type()
)
f3L3TrafficIPv6InterfaceHistoryNdpRSTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6InterfaceHistoryNdpRSTx.setStatus("current")
_F3L3TrafficIPv6InterfaceHistoryNdpRSRx_Type = PerfCounter64
_F3L3TrafficIPv6InterfaceHistoryNdpRSRx_Object = MibTableColumn
f3L3TrafficIPv6InterfaceHistoryNdpRSRx = _F3L3TrafficIPv6InterfaceHistoryNdpRSRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 23, 1, 16),
    _F3L3TrafficIPv6InterfaceHistoryNdpRSRx_Type()
)
f3L3TrafficIPv6InterfaceHistoryNdpRSRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6InterfaceHistoryNdpRSRx.setStatus("current")
_F3L3TrafficIPv6InterfaceThresholdTable_Object = MibTable
f3L3TrafficIPv6InterfaceThresholdTable = _F3L3TrafficIPv6InterfaceThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 24)
)
if mibBuilder.loadTexts:
    f3L3TrafficIPv6InterfaceThresholdTable.setStatus("current")
_F3L3TrafficIPv6InterfaceThresholdEntry_Object = MibTableRow
f3L3TrafficIPv6InterfaceThresholdEntry = _F3L3TrafficIPv6InterfaceThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 24, 1)
)
f3L3TrafficIPv6InterfaceThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "f3L3FlowPointIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficIPv6IfIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficIPv6InterfaceStatsIndex"),
    (0, "F3-L3-MIB", "f3L3TrafficIPv6InterfaceThresholdIndex"),
)
if mibBuilder.loadTexts:
    f3L3TrafficIPv6InterfaceThresholdEntry.setStatus("current")


class _F3L3TrafficIPv6InterfaceThresholdIndex_Type(Integer32):
    """Custom type f3L3TrafficIPv6InterfaceThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3L3TrafficIPv6InterfaceThresholdIndex_Type.__name__ = "Integer32"
_F3L3TrafficIPv6InterfaceThresholdIndex_Object = MibTableColumn
f3L3TrafficIPv6InterfaceThresholdIndex = _F3L3TrafficIPv6InterfaceThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 24, 1, 1),
    _F3L3TrafficIPv6InterfaceThresholdIndex_Type()
)
f3L3TrafficIPv6InterfaceThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6InterfaceThresholdIndex.setStatus("current")
_F3L3TrafficIPv6InterfaceThresholdInterval_Type = CmPmIntervalType
_F3L3TrafficIPv6InterfaceThresholdInterval_Object = MibTableColumn
f3L3TrafficIPv6InterfaceThresholdInterval = _F3L3TrafficIPv6InterfaceThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 24, 1, 2),
    _F3L3TrafficIPv6InterfaceThresholdInterval_Type()
)
f3L3TrafficIPv6InterfaceThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6InterfaceThresholdInterval.setStatus("current")
_F3L3TrafficIPv6InterfaceThresholdVariable_Type = VariablePointer
_F3L3TrafficIPv6InterfaceThresholdVariable_Object = MibTableColumn
f3L3TrafficIPv6InterfaceThresholdVariable = _F3L3TrafficIPv6InterfaceThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 24, 1, 3),
    _F3L3TrafficIPv6InterfaceThresholdVariable_Type()
)
f3L3TrafficIPv6InterfaceThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6InterfaceThresholdVariable.setStatus("current")
_F3L3TrafficIPv6InterfaceThresholdValueLo_Type = Unsigned32
_F3L3TrafficIPv6InterfaceThresholdValueLo_Object = MibTableColumn
f3L3TrafficIPv6InterfaceThresholdValueLo = _F3L3TrafficIPv6InterfaceThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 24, 1, 4),
    _F3L3TrafficIPv6InterfaceThresholdValueLo_Type()
)
f3L3TrafficIPv6InterfaceThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6InterfaceThresholdValueLo.setStatus("current")
_F3L3TrafficIPv6InterfaceThresholdValueHi_Type = Unsigned32
_F3L3TrafficIPv6InterfaceThresholdValueHi_Object = MibTableColumn
f3L3TrafficIPv6InterfaceThresholdValueHi = _F3L3TrafficIPv6InterfaceThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 24, 1, 5),
    _F3L3TrafficIPv6InterfaceThresholdValueHi_Type()
)
f3L3TrafficIPv6InterfaceThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6InterfaceThresholdValueHi.setStatus("current")
_F3L3TrafficIPv6InterfaceThresholdMonValue_Type = Counter64
_F3L3TrafficIPv6InterfaceThresholdMonValue_Object = MibTableColumn
f3L3TrafficIPv6InterfaceThresholdMonValue = _F3L3TrafficIPv6InterfaceThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 24, 1, 6),
    _F3L3TrafficIPv6InterfaceThresholdMonValue_Type()
)
f3L3TrafficIPv6InterfaceThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6InterfaceThresholdMonValue.setStatus("current")
_CmL3FlowPointStatsTable_Object = MibTable
cmL3FlowPointStatsTable = _CmL3FlowPointStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 25)
)
if mibBuilder.loadTexts:
    cmL3FlowPointStatsTable.setStatus("current")
_CmL3FlowPointStatsEntry_Object = MibTableRow
cmL3FlowPointStatsEntry = _CmL3FlowPointStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 25, 1)
)
cmL3FlowPointStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "cmL3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "cmL3FlowPointIndex"),
    (0, "F3-L3-MIB", "cmL3FlowPointStatsIndex"),
)
if mibBuilder.loadTexts:
    cmL3FlowPointStatsEntry.setStatus("current")


class _CmL3FlowPointStatsIndex_Type(Integer32):
    """Custom type cmL3FlowPointStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CmL3FlowPointStatsIndex_Type.__name__ = "Integer32"
_CmL3FlowPointStatsIndex_Object = MibTableColumn
cmL3FlowPointStatsIndex = _CmL3FlowPointStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 25, 1, 1),
    _CmL3FlowPointStatsIndex_Type()
)
cmL3FlowPointStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3FlowPointStatsIndex.setStatus("current")
_CmL3FlowPointStatsIntervalType_Type = CmPmIntervalType
_CmL3FlowPointStatsIntervalType_Object = MibTableColumn
cmL3FlowPointStatsIntervalType = _CmL3FlowPointStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 25, 1, 2),
    _CmL3FlowPointStatsIntervalType_Type()
)
cmL3FlowPointStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3FlowPointStatsIntervalType.setStatus("current")
_CmL3FlowPointStatsValid_Type = TruthValue
_CmL3FlowPointStatsValid_Object = MibTableColumn
cmL3FlowPointStatsValid = _CmL3FlowPointStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 25, 1, 3),
    _CmL3FlowPointStatsValid_Type()
)
cmL3FlowPointStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3FlowPointStatsValid.setStatus("current")
_CmL3FlowPointStatsAction_Type = CmPmBinAction
_CmL3FlowPointStatsAction_Object = MibTableColumn
cmL3FlowPointStatsAction = _CmL3FlowPointStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 25, 1, 4),
    _CmL3FlowPointStatsAction_Type()
)
cmL3FlowPointStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmL3FlowPointStatsAction.setStatus("current")
_CmL3FlowPointStatsFMG_Type = PerfCounter64
_CmL3FlowPointStatsFMG_Object = MibTableColumn
cmL3FlowPointStatsFMG = _CmL3FlowPointStatsFMG_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 25, 1, 5),
    _CmL3FlowPointStatsFMG_Type()
)
cmL3FlowPointStatsFMG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3FlowPointStatsFMG.setStatus("current")
_CmL3FlowPointStatsFMY_Type = PerfCounter64
_CmL3FlowPointStatsFMY_Object = MibTableColumn
cmL3FlowPointStatsFMY = _CmL3FlowPointStatsFMY_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 25, 1, 6),
    _CmL3FlowPointStatsFMY_Type()
)
cmL3FlowPointStatsFMY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3FlowPointStatsFMY.setStatus("current")
_CmL3FlowPointStatsFMRD_Type = PerfCounter64
_CmL3FlowPointStatsFMRD_Object = MibTableColumn
cmL3FlowPointStatsFMRD = _CmL3FlowPointStatsFMRD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 25, 1, 7),
    _CmL3FlowPointStatsFMRD_Type()
)
cmL3FlowPointStatsFMRD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3FlowPointStatsFMRD.setStatus("current")
_CmL3FlowPointStatsFTD_Type = PerfCounter64
_CmL3FlowPointStatsFTD_Object = MibTableColumn
cmL3FlowPointStatsFTD = _CmL3FlowPointStatsFTD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 25, 1, 8),
    _CmL3FlowPointStatsFTD_Type()
)
cmL3FlowPointStatsFTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3FlowPointStatsFTD.setStatus("current")
_CmL3FlowPointStatsFragmentedDropAcl_Type = PerfCounter64
_CmL3FlowPointStatsFragmentedDropAcl_Object = MibTableColumn
cmL3FlowPointStatsFragmentedDropAcl = _CmL3FlowPointStatsFragmentedDropAcl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 25, 1, 9),
    _CmL3FlowPointStatsFragmentedDropAcl_Type()
)
cmL3FlowPointStatsFragmentedDropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3FlowPointStatsFragmentedDropAcl.setStatus("current")
_CmL3FlowPointStatsAclRuleDrop_Type = PerfCounter64
_CmL3FlowPointStatsAclRuleDrop_Object = MibTableColumn
cmL3FlowPointStatsAclRuleDrop = _CmL3FlowPointStatsAclRuleDrop_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 25, 1, 10),
    _CmL3FlowPointStatsAclRuleDrop_Type()
)
cmL3FlowPointStatsAclRuleDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3FlowPointStatsAclRuleDrop.setStatus("current")
_CmL3FlowPointStatsTtlEqual1Drop_Type = PerfCounter64
_CmL3FlowPointStatsTtlEqual1Drop_Object = MibTableColumn
cmL3FlowPointStatsTtlEqual1Drop = _CmL3FlowPointStatsTtlEqual1Drop_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 25, 1, 11),
    _CmL3FlowPointStatsTtlEqual1Drop_Type()
)
cmL3FlowPointStatsTtlEqual1Drop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3FlowPointStatsTtlEqual1Drop.setStatus("current")
_CmL3FlowPointStatsFrameTx_Type = PerfCounter64
_CmL3FlowPointStatsFrameTx_Object = MibTableColumn
cmL3FlowPointStatsFrameTx = _CmL3FlowPointStatsFrameTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 25, 1, 12),
    _CmL3FlowPointStatsFrameTx_Type()
)
cmL3FlowPointStatsFrameTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3FlowPointStatsFrameTx.setStatus("current")
_CmL3FlowPointStatsFrameRx_Type = PerfCounter64
_CmL3FlowPointStatsFrameRx_Object = MibTableColumn
cmL3FlowPointStatsFrameRx = _CmL3FlowPointStatsFrameRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 25, 1, 13),
    _CmL3FlowPointStatsFrameRx_Type()
)
cmL3FlowPointStatsFrameRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3FlowPointStatsFrameRx.setStatus("current")
_CmL3FlowPointStatsNoRouteDrop_Type = PerfCounter64
_CmL3FlowPointStatsNoRouteDrop_Object = MibTableColumn
cmL3FlowPointStatsNoRouteDrop = _CmL3FlowPointStatsNoRouteDrop_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 25, 1, 14),
    _CmL3FlowPointStatsNoRouteDrop_Type()
)
cmL3FlowPointStatsNoRouteDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3FlowPointStatsNoRouteDrop.setStatus("current")
_CmL3FlowPointStatsAclDropNoMatch_Type = PerfCounter64
_CmL3FlowPointStatsAclDropNoMatch_Object = MibTableColumn
cmL3FlowPointStatsAclDropNoMatch = _CmL3FlowPointStatsAclDropNoMatch_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 25, 1, 15),
    _CmL3FlowPointStatsAclDropNoMatch_Type()
)
cmL3FlowPointStatsAclDropNoMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3FlowPointStatsAclDropNoMatch.setStatus("current")
_CmL3FlowPointHistoryTable_Object = MibTable
cmL3FlowPointHistoryTable = _CmL3FlowPointHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 26)
)
if mibBuilder.loadTexts:
    cmL3FlowPointHistoryTable.setStatus("current")
_CmL3FlowPointHistoryEntry_Object = MibTableRow
cmL3FlowPointHistoryEntry = _CmL3FlowPointHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 26, 1)
)
cmL3FlowPointHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "cmL3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "cmL3FlowPointIndex"),
    (0, "F3-L3-MIB", "cmL3FlowPointStatsIndex"),
    (0, "F3-L3-MIB", "cmL3FlowPointHistoryIndex"),
)
if mibBuilder.loadTexts:
    cmL3FlowPointHistoryEntry.setStatus("current")


class _CmL3FlowPointHistoryIndex_Type(Integer32):
    """Custom type cmL3FlowPointHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmL3FlowPointHistoryIndex_Type.__name__ = "Integer32"
_CmL3FlowPointHistoryIndex_Object = MibTableColumn
cmL3FlowPointHistoryIndex = _CmL3FlowPointHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 26, 1, 1),
    _CmL3FlowPointHistoryIndex_Type()
)
cmL3FlowPointHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3FlowPointHistoryIndex.setStatus("current")
_CmL3FlowPointHistoryTime_Type = DateAndTime
_CmL3FlowPointHistoryTime_Object = MibTableColumn
cmL3FlowPointHistoryTime = _CmL3FlowPointHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 26, 1, 2),
    _CmL3FlowPointHistoryTime_Type()
)
cmL3FlowPointHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3FlowPointHistoryTime.setStatus("current")
_CmL3FlowPointHistoryValid_Type = TruthValue
_CmL3FlowPointHistoryValid_Object = MibTableColumn
cmL3FlowPointHistoryValid = _CmL3FlowPointHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 26, 1, 3),
    _CmL3FlowPointHistoryValid_Type()
)
cmL3FlowPointHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3FlowPointHistoryValid.setStatus("current")
_CmL3FlowPointHistoryAction_Type = CmPmBinAction
_CmL3FlowPointHistoryAction_Object = MibTableColumn
cmL3FlowPointHistoryAction = _CmL3FlowPointHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 26, 1, 4),
    _CmL3FlowPointHistoryAction_Type()
)
cmL3FlowPointHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmL3FlowPointHistoryAction.setStatus("current")
_CmL3FlowPointHistoryFMG_Type = PerfCounter64
_CmL3FlowPointHistoryFMG_Object = MibTableColumn
cmL3FlowPointHistoryFMG = _CmL3FlowPointHistoryFMG_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 26, 1, 5),
    _CmL3FlowPointHistoryFMG_Type()
)
cmL3FlowPointHistoryFMG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3FlowPointHistoryFMG.setStatus("current")
_CmL3FlowPointHistoryFMY_Type = PerfCounter64
_CmL3FlowPointHistoryFMY_Object = MibTableColumn
cmL3FlowPointHistoryFMY = _CmL3FlowPointHistoryFMY_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 26, 1, 6),
    _CmL3FlowPointHistoryFMY_Type()
)
cmL3FlowPointHistoryFMY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3FlowPointHistoryFMY.setStatus("current")
_CmL3FlowPointHistoryFMRD_Type = PerfCounter64
_CmL3FlowPointHistoryFMRD_Object = MibTableColumn
cmL3FlowPointHistoryFMRD = _CmL3FlowPointHistoryFMRD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 26, 1, 7),
    _CmL3FlowPointHistoryFMRD_Type()
)
cmL3FlowPointHistoryFMRD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3FlowPointHistoryFMRD.setStatus("current")
_CmL3FlowPointHistoryFTD_Type = PerfCounter64
_CmL3FlowPointHistoryFTD_Object = MibTableColumn
cmL3FlowPointHistoryFTD = _CmL3FlowPointHistoryFTD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 26, 1, 8),
    _CmL3FlowPointHistoryFTD_Type()
)
cmL3FlowPointHistoryFTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3FlowPointHistoryFTD.setStatus("current")
_CmL3FlowPointHistoryFragmentedDropAcl_Type = PerfCounter64
_CmL3FlowPointHistoryFragmentedDropAcl_Object = MibTableColumn
cmL3FlowPointHistoryFragmentedDropAcl = _CmL3FlowPointHistoryFragmentedDropAcl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 26, 1, 9),
    _CmL3FlowPointHistoryFragmentedDropAcl_Type()
)
cmL3FlowPointHistoryFragmentedDropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3FlowPointHistoryFragmentedDropAcl.setStatus("current")
_CmL3FlowPointHistoryAclRuleDrop_Type = PerfCounter64
_CmL3FlowPointHistoryAclRuleDrop_Object = MibTableColumn
cmL3FlowPointHistoryAclRuleDrop = _CmL3FlowPointHistoryAclRuleDrop_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 26, 1, 10),
    _CmL3FlowPointHistoryAclRuleDrop_Type()
)
cmL3FlowPointHistoryAclRuleDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3FlowPointHistoryAclRuleDrop.setStatus("current")
_CmL3FlowPointHistoryTtlEqual1Drop_Type = PerfCounter64
_CmL3FlowPointHistoryTtlEqual1Drop_Object = MibTableColumn
cmL3FlowPointHistoryTtlEqual1Drop = _CmL3FlowPointHistoryTtlEqual1Drop_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 26, 1, 11),
    _CmL3FlowPointHistoryTtlEqual1Drop_Type()
)
cmL3FlowPointHistoryTtlEqual1Drop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3FlowPointHistoryTtlEqual1Drop.setStatus("current")
_CmL3FlowPointHistoryFrameTx_Type = PerfCounter64
_CmL3FlowPointHistoryFrameTx_Object = MibTableColumn
cmL3FlowPointHistoryFrameTx = _CmL3FlowPointHistoryFrameTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 26, 1, 12),
    _CmL3FlowPointHistoryFrameTx_Type()
)
cmL3FlowPointHistoryFrameTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3FlowPointHistoryFrameTx.setStatus("current")
_CmL3FlowPointHistoryFrameRx_Type = PerfCounter64
_CmL3FlowPointHistoryFrameRx_Object = MibTableColumn
cmL3FlowPointHistoryFrameRx = _CmL3FlowPointHistoryFrameRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 26, 1, 13),
    _CmL3FlowPointHistoryFrameRx_Type()
)
cmL3FlowPointHistoryFrameRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3FlowPointHistoryFrameRx.setStatus("current")
_CmL3FlowPointHistoryNoRouteDrop_Type = PerfCounter64
_CmL3FlowPointHistoryNoRouteDrop_Object = MibTableColumn
cmL3FlowPointHistoryNoRouteDrop = _CmL3FlowPointHistoryNoRouteDrop_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 26, 1, 14),
    _CmL3FlowPointHistoryNoRouteDrop_Type()
)
cmL3FlowPointHistoryNoRouteDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3FlowPointHistoryNoRouteDrop.setStatus("current")
_CmL3FlowPointHistoryAclDropNoMatch_Type = PerfCounter64
_CmL3FlowPointHistoryAclDropNoMatch_Object = MibTableColumn
cmL3FlowPointHistoryAclDropNoMatch = _CmL3FlowPointHistoryAclDropNoMatch_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 26, 1, 15),
    _CmL3FlowPointHistoryAclDropNoMatch_Type()
)
cmL3FlowPointHistoryAclDropNoMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3FlowPointHistoryAclDropNoMatch.setStatus("current")
_CmL3FlowPointThresholdTable_Object = MibTable
cmL3FlowPointThresholdTable = _CmL3FlowPointThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 27)
)
if mibBuilder.loadTexts:
    cmL3FlowPointThresholdTable.setStatus("current")
_CmL3FlowPointThresholdEntry_Object = MibTableRow
cmL3FlowPointThresholdEntry = _CmL3FlowPointThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 27, 1)
)
cmL3FlowPointThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "cmL3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "cmL3FlowPointIndex"),
    (0, "F3-L3-MIB", "cmL3FlowPointStatsIndex"),
    (0, "F3-L3-MIB", "cmL3FlowPointThresholdIndex"),
)
if mibBuilder.loadTexts:
    cmL3FlowPointThresholdEntry.setStatus("current")


class _CmL3FlowPointThresholdIndex_Type(Integer32):
    """Custom type cmL3FlowPointThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmL3FlowPointThresholdIndex_Type.__name__ = "Integer32"
_CmL3FlowPointThresholdIndex_Object = MibTableColumn
cmL3FlowPointThresholdIndex = _CmL3FlowPointThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 27, 1, 1),
    _CmL3FlowPointThresholdIndex_Type()
)
cmL3FlowPointThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3FlowPointThresholdIndex.setStatus("current")
_CmL3FlowPointThresholdInterval_Type = CmPmIntervalType
_CmL3FlowPointThresholdInterval_Object = MibTableColumn
cmL3FlowPointThresholdInterval = _CmL3FlowPointThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 27, 1, 2),
    _CmL3FlowPointThresholdInterval_Type()
)
cmL3FlowPointThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3FlowPointThresholdInterval.setStatus("current")
_CmL3FlowPointThresholdVariable_Type = VariablePointer
_CmL3FlowPointThresholdVariable_Object = MibTableColumn
cmL3FlowPointThresholdVariable = _CmL3FlowPointThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 27, 1, 3),
    _CmL3FlowPointThresholdVariable_Type()
)
cmL3FlowPointThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3FlowPointThresholdVariable.setStatus("current")
_CmL3FlowPointThresholdValueLo_Type = Unsigned32
_CmL3FlowPointThresholdValueLo_Object = MibTableColumn
cmL3FlowPointThresholdValueLo = _CmL3FlowPointThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 27, 1, 4),
    _CmL3FlowPointThresholdValueLo_Type()
)
cmL3FlowPointThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmL3FlowPointThresholdValueLo.setStatus("current")
_CmL3FlowPointThresholdValueHi_Type = Unsigned32
_CmL3FlowPointThresholdValueHi_Object = MibTableColumn
cmL3FlowPointThresholdValueHi = _CmL3FlowPointThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 27, 1, 5),
    _CmL3FlowPointThresholdValueHi_Type()
)
cmL3FlowPointThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmL3FlowPointThresholdValueHi.setStatus("current")
_CmL3FlowPointThresholdMonValue_Type = Counter64
_CmL3FlowPointThresholdMonValue_Object = MibTableColumn
cmL3FlowPointThresholdMonValue = _CmL3FlowPointThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 27, 1, 6),
    _CmL3FlowPointThresholdMonValue_Type()
)
cmL3FlowPointThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3FlowPointThresholdMonValue.setStatus("current")
_CmL3QosPolicerStatsTable_Object = MibTable
cmL3QosPolicerStatsTable = _CmL3QosPolicerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 28)
)
if mibBuilder.loadTexts:
    cmL3QosPolicerStatsTable.setStatus("current")
_CmL3QosPolicerStatsEntry_Object = MibTableRow
cmL3QosPolicerStatsEntry = _CmL3QosPolicerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 28, 1)
)
cmL3QosPolicerStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "cmL3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "cmL3FlowPointIndex"),
    (0, "F3-L3-MIB", "cmL3QosPolicerIndex"),
    (0, "F3-L3-MIB", "cmL3QosPolicerStatsIndex"),
)
if mibBuilder.loadTexts:
    cmL3QosPolicerStatsEntry.setStatus("current")


class _CmL3QosPolicerStatsIndex_Type(Integer32):
    """Custom type cmL3QosPolicerStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmL3QosPolicerStatsIndex_Type.__name__ = "Integer32"
_CmL3QosPolicerStatsIndex_Object = MibTableColumn
cmL3QosPolicerStatsIndex = _CmL3QosPolicerStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 28, 1, 1),
    _CmL3QosPolicerStatsIndex_Type()
)
cmL3QosPolicerStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosPolicerStatsIndex.setStatus("current")
_CmL3QosPolicerStatsIntervalType_Type = CmPmIntervalType
_CmL3QosPolicerStatsIntervalType_Object = MibTableColumn
cmL3QosPolicerStatsIntervalType = _CmL3QosPolicerStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 28, 1, 2),
    _CmL3QosPolicerStatsIntervalType_Type()
)
cmL3QosPolicerStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosPolicerStatsIntervalType.setStatus("current")
_CmL3QosPolicerStatsValid_Type = TruthValue
_CmL3QosPolicerStatsValid_Object = MibTableColumn
cmL3QosPolicerStatsValid = _CmL3QosPolicerStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 28, 1, 3),
    _CmL3QosPolicerStatsValid_Type()
)
cmL3QosPolicerStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosPolicerStatsValid.setStatus("current")
_CmL3QosPolicerStatsAction_Type = CmPmBinAction
_CmL3QosPolicerStatsAction_Object = MibTableColumn
cmL3QosPolicerStatsAction = _CmL3QosPolicerStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 28, 1, 4),
    _CmL3QosPolicerStatsAction_Type()
)
cmL3QosPolicerStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmL3QosPolicerStatsAction.setStatus("current")
_CmL3QosPolicerStatsFMG_Type = PerfCounter64
_CmL3QosPolicerStatsFMG_Object = MibTableColumn
cmL3QosPolicerStatsFMG = _CmL3QosPolicerStatsFMG_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 28, 1, 5),
    _CmL3QosPolicerStatsFMG_Type()
)
cmL3QosPolicerStatsFMG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosPolicerStatsFMG.setStatus("current")
_CmL3QosPolicerStatsFMY_Type = PerfCounter64
_CmL3QosPolicerStatsFMY_Object = MibTableColumn
cmL3QosPolicerStatsFMY = _CmL3QosPolicerStatsFMY_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 28, 1, 6),
    _CmL3QosPolicerStatsFMY_Type()
)
cmL3QosPolicerStatsFMY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosPolicerStatsFMY.setStatus("current")
_CmL3QosPolicerStatsFMYD_Type = PerfCounter64
_CmL3QosPolicerStatsFMYD_Object = MibTableColumn
cmL3QosPolicerStatsFMYD = _CmL3QosPolicerStatsFMYD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 28, 1, 7),
    _CmL3QosPolicerStatsFMYD_Type()
)
cmL3QosPolicerStatsFMYD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosPolicerStatsFMYD.setStatus("deprecated")
_CmL3QosPolicerStatsFMRD_Type = PerfCounter64
_CmL3QosPolicerStatsFMRD_Object = MibTableColumn
cmL3QosPolicerStatsFMRD = _CmL3QosPolicerStatsFMRD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 28, 1, 8),
    _CmL3QosPolicerStatsFMRD_Type()
)
cmL3QosPolicerStatsFMRD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosPolicerStatsFMRD.setStatus("current")
_CmL3QosPolicerStatsBytesIn_Type = PerfCounter64
_CmL3QosPolicerStatsBytesIn_Object = MibTableColumn
cmL3QosPolicerStatsBytesIn = _CmL3QosPolicerStatsBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 28, 1, 9),
    _CmL3QosPolicerStatsBytesIn_Type()
)
cmL3QosPolicerStatsBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosPolicerStatsBytesIn.setStatus("current")
_CmL3QosPolicerStatsBytesOut_Type = PerfCounter64
_CmL3QosPolicerStatsBytesOut_Object = MibTableColumn
cmL3QosPolicerStatsBytesOut = _CmL3QosPolicerStatsBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 28, 1, 10),
    _CmL3QosPolicerStatsBytesOut_Type()
)
cmL3QosPolicerStatsBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosPolicerStatsBytesOut.setStatus("current")
_CmL3QosPolicerStatsABR_Type = PerfCounter64
_CmL3QosPolicerStatsABR_Object = MibTableColumn
cmL3QosPolicerStatsABR = _CmL3QosPolicerStatsABR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 28, 1, 11),
    _CmL3QosPolicerStatsABR_Type()
)
cmL3QosPolicerStatsABR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosPolicerStatsABR.setStatus("current")
_CmL3QosPolicerHistoryTable_Object = MibTable
cmL3QosPolicerHistoryTable = _CmL3QosPolicerHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 29)
)
if mibBuilder.loadTexts:
    cmL3QosPolicerHistoryTable.setStatus("current")
_CmL3QosPolicerHistoryEntry_Object = MibTableRow
cmL3QosPolicerHistoryEntry = _CmL3QosPolicerHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 29, 1)
)
cmL3QosPolicerHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "cmL3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "cmL3FlowPointIndex"),
    (0, "F3-L3-MIB", "cmL3QosPolicerIndex"),
    (0, "F3-L3-MIB", "cmL3QosPolicerStatsIndex"),
    (0, "F3-L3-MIB", "cmL3QosPolicerHistoryIndex"),
)
if mibBuilder.loadTexts:
    cmL3QosPolicerHistoryEntry.setStatus("current")


class _CmL3QosPolicerHistoryIndex_Type(Integer32):
    """Custom type cmL3QosPolicerHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmL3QosPolicerHistoryIndex_Type.__name__ = "Integer32"
_CmL3QosPolicerHistoryIndex_Object = MibTableColumn
cmL3QosPolicerHistoryIndex = _CmL3QosPolicerHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 29, 1, 1),
    _CmL3QosPolicerHistoryIndex_Type()
)
cmL3QosPolicerHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosPolicerHistoryIndex.setStatus("current")
_CmL3QosPolicerHistoryTime_Type = DateAndTime
_CmL3QosPolicerHistoryTime_Object = MibTableColumn
cmL3QosPolicerHistoryTime = _CmL3QosPolicerHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 29, 1, 2),
    _CmL3QosPolicerHistoryTime_Type()
)
cmL3QosPolicerHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosPolicerHistoryTime.setStatus("current")
_CmL3QosPolicerHistoryValid_Type = TruthValue
_CmL3QosPolicerHistoryValid_Object = MibTableColumn
cmL3QosPolicerHistoryValid = _CmL3QosPolicerHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 29, 1, 3),
    _CmL3QosPolicerHistoryValid_Type()
)
cmL3QosPolicerHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosPolicerHistoryValid.setStatus("current")
_CmL3QosPolicerHistoryAction_Type = CmPmBinAction
_CmL3QosPolicerHistoryAction_Object = MibTableColumn
cmL3QosPolicerHistoryAction = _CmL3QosPolicerHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 29, 1, 4),
    _CmL3QosPolicerHistoryAction_Type()
)
cmL3QosPolicerHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmL3QosPolicerHistoryAction.setStatus("current")
_CmL3QosPolicerHistoryFMG_Type = PerfCounter64
_CmL3QosPolicerHistoryFMG_Object = MibTableColumn
cmL3QosPolicerHistoryFMG = _CmL3QosPolicerHistoryFMG_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 29, 1, 5),
    _CmL3QosPolicerHistoryFMG_Type()
)
cmL3QosPolicerHistoryFMG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosPolicerHistoryFMG.setStatus("current")
_CmL3QosPolicerHistoryFMY_Type = PerfCounter64
_CmL3QosPolicerHistoryFMY_Object = MibTableColumn
cmL3QosPolicerHistoryFMY = _CmL3QosPolicerHistoryFMY_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 29, 1, 6),
    _CmL3QosPolicerHistoryFMY_Type()
)
cmL3QosPolicerHistoryFMY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosPolicerHistoryFMY.setStatus("current")
_CmL3QosPolicerHistoryFMYD_Type = PerfCounter64
_CmL3QosPolicerHistoryFMYD_Object = MibTableColumn
cmL3QosPolicerHistoryFMYD = _CmL3QosPolicerHistoryFMYD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 29, 1, 7),
    _CmL3QosPolicerHistoryFMYD_Type()
)
cmL3QosPolicerHistoryFMYD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosPolicerHistoryFMYD.setStatus("deprecated")
_CmL3QosPolicerHistoryFMRD_Type = PerfCounter64
_CmL3QosPolicerHistoryFMRD_Object = MibTableColumn
cmL3QosPolicerHistoryFMRD = _CmL3QosPolicerHistoryFMRD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 29, 1, 8),
    _CmL3QosPolicerHistoryFMRD_Type()
)
cmL3QosPolicerHistoryFMRD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosPolicerHistoryFMRD.setStatus("current")
_CmL3QosPolicerHistoryBytesIn_Type = PerfCounter64
_CmL3QosPolicerHistoryBytesIn_Object = MibTableColumn
cmL3QosPolicerHistoryBytesIn = _CmL3QosPolicerHistoryBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 29, 1, 9),
    _CmL3QosPolicerHistoryBytesIn_Type()
)
cmL3QosPolicerHistoryBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosPolicerHistoryBytesIn.setStatus("current")
_CmL3QosPolicerHistoryBytesOut_Type = PerfCounter64
_CmL3QosPolicerHistoryBytesOut_Object = MibTableColumn
cmL3QosPolicerHistoryBytesOut = _CmL3QosPolicerHistoryBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 29, 1, 10),
    _CmL3QosPolicerHistoryBytesOut_Type()
)
cmL3QosPolicerHistoryBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosPolicerHistoryBytesOut.setStatus("current")
_CmL3QosPolicerHistoryABR_Type = PerfCounter64
_CmL3QosPolicerHistoryABR_Object = MibTableColumn
cmL3QosPolicerHistoryABR = _CmL3QosPolicerHistoryABR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 29, 1, 11),
    _CmL3QosPolicerHistoryABR_Type()
)
cmL3QosPolicerHistoryABR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosPolicerHistoryABR.setStatus("current")
_CmL3QosPolicerThresholdTable_Object = MibTable
cmL3QosPolicerThresholdTable = _CmL3QosPolicerThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 30)
)
if mibBuilder.loadTexts:
    cmL3QosPolicerThresholdTable.setStatus("current")
_CmL3QosPolicerThresholdEntry_Object = MibTableRow
cmL3QosPolicerThresholdEntry = _CmL3QosPolicerThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 30, 1)
)
cmL3QosPolicerThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "cmL3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "cmL3FlowPointIndex"),
    (0, "F3-L3-MIB", "cmL3QosPolicerIndex"),
    (0, "F3-L3-MIB", "cmL3QosPolicerStatsIndex"),
    (0, "F3-L3-MIB", "cmL3QosPolicerThresholdIndex"),
)
if mibBuilder.loadTexts:
    cmL3QosPolicerThresholdEntry.setStatus("current")


class _CmL3QosPolicerThresholdIndex_Type(Integer32):
    """Custom type cmL3QosPolicerThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmL3QosPolicerThresholdIndex_Type.__name__ = "Integer32"
_CmL3QosPolicerThresholdIndex_Object = MibTableColumn
cmL3QosPolicerThresholdIndex = _CmL3QosPolicerThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 30, 1, 1),
    _CmL3QosPolicerThresholdIndex_Type()
)
cmL3QosPolicerThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosPolicerThresholdIndex.setStatus("current")
_CmL3QosPolicerThresholdInterval_Type = CmPmIntervalType
_CmL3QosPolicerThresholdInterval_Object = MibTableColumn
cmL3QosPolicerThresholdInterval = _CmL3QosPolicerThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 30, 1, 2),
    _CmL3QosPolicerThresholdInterval_Type()
)
cmL3QosPolicerThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosPolicerThresholdInterval.setStatus("current")
_CmL3QosPolicerThresholdVariable_Type = VariablePointer
_CmL3QosPolicerThresholdVariable_Object = MibTableColumn
cmL3QosPolicerThresholdVariable = _CmL3QosPolicerThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 30, 1, 3),
    _CmL3QosPolicerThresholdVariable_Type()
)
cmL3QosPolicerThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosPolicerThresholdVariable.setStatus("current")
_CmL3QosPolicerThresholdValueLo_Type = Unsigned32
_CmL3QosPolicerThresholdValueLo_Object = MibTableColumn
cmL3QosPolicerThresholdValueLo = _CmL3QosPolicerThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 30, 1, 4),
    _CmL3QosPolicerThresholdValueLo_Type()
)
cmL3QosPolicerThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmL3QosPolicerThresholdValueLo.setStatus("current")
_CmL3QosPolicerThresholdValueHi_Type = Unsigned32
_CmL3QosPolicerThresholdValueHi_Object = MibTableColumn
cmL3QosPolicerThresholdValueHi = _CmL3QosPolicerThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 30, 1, 5),
    _CmL3QosPolicerThresholdValueHi_Type()
)
cmL3QosPolicerThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmL3QosPolicerThresholdValueHi.setStatus("current")
_CmL3QosPolicerThresholdMonValue_Type = Counter64
_CmL3QosPolicerThresholdMonValue_Object = MibTableColumn
cmL3QosPolicerThresholdMonValue = _CmL3QosPolicerThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 30, 1, 6),
    _CmL3QosPolicerThresholdMonValue_Type()
)
cmL3QosPolicerThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosPolicerThresholdMonValue.setStatus("current")
_CmL3QosShaperStatsTable_Object = MibTable
cmL3QosShaperStatsTable = _CmL3QosShaperStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 31)
)
if mibBuilder.loadTexts:
    cmL3QosShaperStatsTable.setStatus("current")
_CmL3QosShaperStatsEntry_Object = MibTableRow
cmL3QosShaperStatsEntry = _CmL3QosShaperStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 31, 1)
)
cmL3QosShaperStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "cmL3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "cmL3FlowPointIndex"),
    (0, "F3-L3-MIB", "cmL3QosShaperIndex"),
    (0, "F3-L3-MIB", "cmL3QosShaperStatsIndex"),
)
if mibBuilder.loadTexts:
    cmL3QosShaperStatsEntry.setStatus("current")


class _CmL3QosShaperStatsIndex_Type(Integer32):
    """Custom type cmL3QosShaperStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmL3QosShaperStatsIndex_Type.__name__ = "Integer32"
_CmL3QosShaperStatsIndex_Object = MibTableColumn
cmL3QosShaperStatsIndex = _CmL3QosShaperStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 31, 1, 1),
    _CmL3QosShaperStatsIndex_Type()
)
cmL3QosShaperStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosShaperStatsIndex.setStatus("current")
_CmL3QosShaperStatsIntervalType_Type = CmPmIntervalType
_CmL3QosShaperStatsIntervalType_Object = MibTableColumn
cmL3QosShaperStatsIntervalType = _CmL3QosShaperStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 31, 1, 2),
    _CmL3QosShaperStatsIntervalType_Type()
)
cmL3QosShaperStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosShaperStatsIntervalType.setStatus("current")
_CmL3QosShaperStatsValid_Type = TruthValue
_CmL3QosShaperStatsValid_Object = MibTableColumn
cmL3QosShaperStatsValid = _CmL3QosShaperStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 31, 1, 3),
    _CmL3QosShaperStatsValid_Type()
)
cmL3QosShaperStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosShaperStatsValid.setStatus("current")
_CmL3QosShaperStatsAction_Type = CmPmBinAction
_CmL3QosShaperStatsAction_Object = MibTableColumn
cmL3QosShaperStatsAction = _CmL3QosShaperStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 31, 1, 4),
    _CmL3QosShaperStatsAction_Type()
)
cmL3QosShaperStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmL3QosShaperStatsAction.setStatus("current")
_CmL3QosShaperStatsBT_Type = PerfCounter64
_CmL3QosShaperStatsBT_Object = MibTableColumn
cmL3QosShaperStatsBT = _CmL3QosShaperStatsBT_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 31, 1, 5),
    _CmL3QosShaperStatsBT_Type()
)
cmL3QosShaperStatsBT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosShaperStatsBT.setStatus("current")
_CmL3QosShaperStatsBTD_Type = PerfCounter64
_CmL3QosShaperStatsBTD_Object = MibTableColumn
cmL3QosShaperStatsBTD = _CmL3QosShaperStatsBTD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 31, 1, 6),
    _CmL3QosShaperStatsBTD_Type()
)
cmL3QosShaperStatsBTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosShaperStatsBTD.setStatus("current")
_CmL3QosShaperStatsFD_Type = PerfCounter64
_CmL3QosShaperStatsFD_Object = MibTableColumn
cmL3QosShaperStatsFD = _CmL3QosShaperStatsFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 31, 1, 7),
    _CmL3QosShaperStatsFD_Type()
)
cmL3QosShaperStatsFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosShaperStatsFD.setStatus("current")
_CmL3QosShaperStatsFTD_Type = PerfCounter64
_CmL3QosShaperStatsFTD_Object = MibTableColumn
cmL3QosShaperStatsFTD = _CmL3QosShaperStatsFTD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 31, 1, 8),
    _CmL3QosShaperStatsFTD_Type()
)
cmL3QosShaperStatsFTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosShaperStatsFTD.setStatus("current")
_CmL3QosShaperStatsBR_Type = PerfCounter64
_CmL3QosShaperStatsBR_Object = MibTableColumn
cmL3QosShaperStatsBR = _CmL3QosShaperStatsBR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 31, 1, 9),
    _CmL3QosShaperStatsBR_Type()
)
cmL3QosShaperStatsBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosShaperStatsBR.setStatus("current")
_CmL3QosShaperStatsFR_Type = PerfCounter64
_CmL3QosShaperStatsFR_Object = MibTableColumn
cmL3QosShaperStatsFR = _CmL3QosShaperStatsFR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 31, 1, 10),
    _CmL3QosShaperStatsFR_Type()
)
cmL3QosShaperStatsFR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosShaperStatsFR.setStatus("current")
_CmL3QosShaperStatsABRRL_Type = PerfCounter64
_CmL3QosShaperStatsABRRL_Object = MibTableColumn
cmL3QosShaperStatsABRRL = _CmL3QosShaperStatsABRRL_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 31, 1, 11),
    _CmL3QosShaperStatsABRRL_Type()
)
cmL3QosShaperStatsABRRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosShaperStatsABRRL.setStatus("current")
_CmL3QosShaperStatsABRRLR_Type = PerfCounter64
_CmL3QosShaperStatsABRRLR_Object = MibTableColumn
cmL3QosShaperStatsABRRLR = _CmL3QosShaperStatsABRRLR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 31, 1, 12),
    _CmL3QosShaperStatsABRRLR_Type()
)
cmL3QosShaperStatsABRRLR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosShaperStatsABRRLR.setStatus("current")
_CmL3QosShaperStatsBREDD_Type = PerfCounter64
_CmL3QosShaperStatsBREDD_Object = MibTableColumn
cmL3QosShaperStatsBREDD = _CmL3QosShaperStatsBREDD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 31, 1, 13),
    _CmL3QosShaperStatsBREDD_Type()
)
cmL3QosShaperStatsBREDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosShaperStatsBREDD.setStatus("current")
_CmL3QosShaperStatsFREDD_Type = PerfCounter64
_CmL3QosShaperStatsFREDD_Object = MibTableColumn
cmL3QosShaperStatsFREDD = _CmL3QosShaperStatsFREDD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 31, 1, 14),
    _CmL3QosShaperStatsFREDD_Type()
)
cmL3QosShaperStatsFREDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosShaperStatsFREDD.setStatus("current")
_CmL3QosShaperHistoryTable_Object = MibTable
cmL3QosShaperHistoryTable = _CmL3QosShaperHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 32)
)
if mibBuilder.loadTexts:
    cmL3QosShaperHistoryTable.setStatus("current")
_CmL3QosShaperHistoryEntry_Object = MibTableRow
cmL3QosShaperHistoryEntry = _CmL3QosShaperHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 32, 1)
)
cmL3QosShaperHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "cmL3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "cmL3FlowPointIndex"),
    (0, "F3-L3-MIB", "cmL3QosShaperIndex"),
    (0, "F3-L3-MIB", "cmL3QosShaperStatsIndex"),
    (0, "F3-L3-MIB", "cmL3QosShaperHistoryIndex"),
)
if mibBuilder.loadTexts:
    cmL3QosShaperHistoryEntry.setStatus("current")


class _CmL3QosShaperHistoryIndex_Type(Integer32):
    """Custom type cmL3QosShaperHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmL3QosShaperHistoryIndex_Type.__name__ = "Integer32"
_CmL3QosShaperHistoryIndex_Object = MibTableColumn
cmL3QosShaperHistoryIndex = _CmL3QosShaperHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 32, 1, 1),
    _CmL3QosShaperHistoryIndex_Type()
)
cmL3QosShaperHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosShaperHistoryIndex.setStatus("current")
_CmL3QosShaperHistoryTime_Type = DateAndTime
_CmL3QosShaperHistoryTime_Object = MibTableColumn
cmL3QosShaperHistoryTime = _CmL3QosShaperHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 32, 1, 2),
    _CmL3QosShaperHistoryTime_Type()
)
cmL3QosShaperHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosShaperHistoryTime.setStatus("current")
_CmL3QosShaperHistoryValid_Type = TruthValue
_CmL3QosShaperHistoryValid_Object = MibTableColumn
cmL3QosShaperHistoryValid = _CmL3QosShaperHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 32, 1, 3),
    _CmL3QosShaperHistoryValid_Type()
)
cmL3QosShaperHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosShaperHistoryValid.setStatus("current")
_CmL3QosShaperHistoryAction_Type = CmPmBinAction
_CmL3QosShaperHistoryAction_Object = MibTableColumn
cmL3QosShaperHistoryAction = _CmL3QosShaperHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 32, 1, 4),
    _CmL3QosShaperHistoryAction_Type()
)
cmL3QosShaperHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmL3QosShaperHistoryAction.setStatus("current")
_CmL3QosShaperHistoryBT_Type = PerfCounter64
_CmL3QosShaperHistoryBT_Object = MibTableColumn
cmL3QosShaperHistoryBT = _CmL3QosShaperHistoryBT_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 32, 1, 5),
    _CmL3QosShaperHistoryBT_Type()
)
cmL3QosShaperHistoryBT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosShaperHistoryBT.setStatus("current")
_CmL3QosShaperHistoryBTD_Type = PerfCounter64
_CmL3QosShaperHistoryBTD_Object = MibTableColumn
cmL3QosShaperHistoryBTD = _CmL3QosShaperHistoryBTD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 32, 1, 6),
    _CmL3QosShaperHistoryBTD_Type()
)
cmL3QosShaperHistoryBTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosShaperHistoryBTD.setStatus("current")
_CmL3QosShaperHistoryFD_Type = PerfCounter64
_CmL3QosShaperHistoryFD_Object = MibTableColumn
cmL3QosShaperHistoryFD = _CmL3QosShaperHistoryFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 32, 1, 7),
    _CmL3QosShaperHistoryFD_Type()
)
cmL3QosShaperHistoryFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosShaperHistoryFD.setStatus("current")
_CmL3QosShaperHistoryFTD_Type = PerfCounter64
_CmL3QosShaperHistoryFTD_Object = MibTableColumn
cmL3QosShaperHistoryFTD = _CmL3QosShaperHistoryFTD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 32, 1, 8),
    _CmL3QosShaperHistoryFTD_Type()
)
cmL3QosShaperHistoryFTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosShaperHistoryFTD.setStatus("current")
_CmL3QosShaperHistoryBR_Type = PerfCounter64
_CmL3QosShaperHistoryBR_Object = MibTableColumn
cmL3QosShaperHistoryBR = _CmL3QosShaperHistoryBR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 32, 1, 9),
    _CmL3QosShaperHistoryBR_Type()
)
cmL3QosShaperHistoryBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosShaperHistoryBR.setStatus("current")
_CmL3QosShaperHistoryFR_Type = PerfCounter64
_CmL3QosShaperHistoryFR_Object = MibTableColumn
cmL3QosShaperHistoryFR = _CmL3QosShaperHistoryFR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 32, 1, 10),
    _CmL3QosShaperHistoryFR_Type()
)
cmL3QosShaperHistoryFR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosShaperHistoryFR.setStatus("current")
_CmL3QosShaperHistoryABRRL_Type = PerfCounter64
_CmL3QosShaperHistoryABRRL_Object = MibTableColumn
cmL3QosShaperHistoryABRRL = _CmL3QosShaperHistoryABRRL_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 32, 1, 11),
    _CmL3QosShaperHistoryABRRL_Type()
)
cmL3QosShaperHistoryABRRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosShaperHistoryABRRL.setStatus("current")
_CmL3QosShaperHistoryABRRLR_Type = PerfCounter64
_CmL3QosShaperHistoryABRRLR_Object = MibTableColumn
cmL3QosShaperHistoryABRRLR = _CmL3QosShaperHistoryABRRLR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 32, 1, 12),
    _CmL3QosShaperHistoryABRRLR_Type()
)
cmL3QosShaperHistoryABRRLR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosShaperHistoryABRRLR.setStatus("current")
_CmL3QosShaperHistoryBREDD_Type = PerfCounter64
_CmL3QosShaperHistoryBREDD_Object = MibTableColumn
cmL3QosShaperHistoryBREDD = _CmL3QosShaperHistoryBREDD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 32, 1, 13),
    _CmL3QosShaperHistoryBREDD_Type()
)
cmL3QosShaperHistoryBREDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosShaperHistoryBREDD.setStatus("current")
_CmL3QosShaperHistoryFREDD_Type = PerfCounter64
_CmL3QosShaperHistoryFREDD_Object = MibTableColumn
cmL3QosShaperHistoryFREDD = _CmL3QosShaperHistoryFREDD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 32, 1, 14),
    _CmL3QosShaperHistoryFREDD_Type()
)
cmL3QosShaperHistoryFREDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosShaperHistoryFREDD.setStatus("current")
_CmL3QosShaperThresholdTable_Object = MibTable
cmL3QosShaperThresholdTable = _CmL3QosShaperThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 33)
)
if mibBuilder.loadTexts:
    cmL3QosShaperThresholdTable.setStatus("current")
_CmL3QosShaperThresholdEntry_Object = MibTableRow
cmL3QosShaperThresholdEntry = _CmL3QosShaperThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 33, 1)
)
cmL3QosShaperThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-L3-MIB", "cmL3FlowPointPortIndex"),
    (0, "F3-L3-MIB", "cmL3FlowPointIndex"),
    (0, "F3-L3-MIB", "cmL3QosShaperIndex"),
    (0, "F3-L3-MIB", "cmL3QosShaperStatsIndex"),
    (0, "F3-L3-MIB", "cmL3QosShaperThresholdIndex"),
)
if mibBuilder.loadTexts:
    cmL3QosShaperThresholdEntry.setStatus("current")


class _CmL3QosShaperThresholdIndex_Type(Integer32):
    """Custom type cmL3QosShaperThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmL3QosShaperThresholdIndex_Type.__name__ = "Integer32"
_CmL3QosShaperThresholdIndex_Object = MibTableColumn
cmL3QosShaperThresholdIndex = _CmL3QosShaperThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 33, 1, 1),
    _CmL3QosShaperThresholdIndex_Type()
)
cmL3QosShaperThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosShaperThresholdIndex.setStatus("current")
_CmL3QosShaperThresholdInterval_Type = CmPmIntervalType
_CmL3QosShaperThresholdInterval_Object = MibTableColumn
cmL3QosShaperThresholdInterval = _CmL3QosShaperThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 33, 1, 2),
    _CmL3QosShaperThresholdInterval_Type()
)
cmL3QosShaperThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosShaperThresholdInterval.setStatus("current")
_CmL3QosShaperThresholdVariable_Type = VariablePointer
_CmL3QosShaperThresholdVariable_Object = MibTableColumn
cmL3QosShaperThresholdVariable = _CmL3QosShaperThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 33, 1, 3),
    _CmL3QosShaperThresholdVariable_Type()
)
cmL3QosShaperThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosShaperThresholdVariable.setStatus("current")
_CmL3QosShaperThresholdValueLo_Type = Unsigned32
_CmL3QosShaperThresholdValueLo_Object = MibTableColumn
cmL3QosShaperThresholdValueLo = _CmL3QosShaperThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 33, 1, 4),
    _CmL3QosShaperThresholdValueLo_Type()
)
cmL3QosShaperThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmL3QosShaperThresholdValueLo.setStatus("current")
_CmL3QosShaperThresholdValueHi_Type = Unsigned32
_CmL3QosShaperThresholdValueHi_Object = MibTableColumn
cmL3QosShaperThresholdValueHi = _CmL3QosShaperThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 33, 1, 5),
    _CmL3QosShaperThresholdValueHi_Type()
)
cmL3QosShaperThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmL3QosShaperThresholdValueHi.setStatus("current")
_CmL3QosShaperThresholdMonValue_Type = Counter64
_CmL3QosShaperThresholdMonValue_Object = MibTableColumn
cmL3QosShaperThresholdMonValue = _CmL3QosShaperThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 2, 33, 1, 6),
    _CmL3QosShaperThresholdMonValue_Type()
)
cmL3QosShaperThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmL3QosShaperThresholdMonValue.setStatus("current")
_F3L3Notifications_ObjectIdentity = ObjectIdentity
f3L3Notifications = _F3L3Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 3)
)
_F3L3Conformance_ObjectIdentity = ObjectIdentity
f3L3Conformance = _F3L3Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 4)
)
_F3L3Compliances_ObjectIdentity = ObjectIdentity
f3L3Compliances = _F3L3Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 4, 1)
)
_F3L3Groups_ObjectIdentity = ObjectIdentity
f3L3Groups = _F3L3Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 4, 2)
)
_CmL3Notifications_ObjectIdentity = ObjectIdentity
cmL3Notifications = _CmL3Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 5)
)
f3L3TrafficIPInterfaceEntry.registerAugmentions(
    ("F3-L3-MIB",
     "f3L3TrafficIPInterfaceOspfEntry")
)
f3L3TrafficIPInterfaceOspfEntry.setIndexNames(*f3L3TrafficIPInterfaceEntry.getIndexNames())

# Managed Objects groups

f3L3ObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 4, 2, 1)
)
f3L3ObjectsGroup.setObjects(
      *(("F3-L3-MIB", "f3DhcpRelayAgentIndex"),
        ("F3-L3-MIB", "f3DhcpRelayAgentAlias"),
        ("F3-L3-MIB", "f3DhcpRelayAgentAdminState"),
        ("F3-L3-MIB", "f3DhcpRelayAgentSecondaryState"),
        ("F3-L3-MIB", "f3DhcpRelayAgentOperationalState"),
        ("F3-L3-MIB", "f3DhcpRelayAgentIpVersion"),
        ("F3-L3-MIB", "f3DhcpRelayAgentServerIpAddress"),
        ("F3-L3-MIB", "f3DhcpRelayAgentOp82SubOp9ControlEnabled"),
        ("F3-L3-MIB", "f3DhcpRelayAgentOp82SubOp9Value"),
        ("F3-L3-MIB", "f3DhcpRelayAgentStorageType"),
        ("F3-L3-MIB", "f3DhcpRelayAgentRowStatus"),
        ("F3-L3-MIB", "f3VrfIndex"),
        ("F3-L3-MIB", "f3VrfAlias"),
        ("F3-L3-MIB", "f3VrfAdminState"),
        ("F3-L3-MIB", "f3VrfSecondaryState"),
        ("F3-L3-MIB", "f3VrfTraceRouteIpv4Destination"),
        ("F3-L3-MIB", "f3VrfOperationalState"),
        ("F3-L3-MIB", "f3VrfAccIsolationControlEnabled"),
        ("F3-L3-MIB", "f3VrfPingResult"),
        ("F3-L3-MIB", "f3VrfPingIpv4Destination"),
        ("F3-L3-MIB", "f3VrfTraceRouteResult"),
        ("F3-L3-MIB", "f3VrfAction"),
        ("F3-L3-MIB", "f3VrfStorageType"),
        ("F3-L3-MIB", "f3VrfTransportType"),
        ("F3-L3-MIB", "f3VrfRowStatus"),
        ("F3-L3-MIB", "f3VrfDhcpRoutesControl"),
        ("F3-L3-MIB", "f3VrfActionX"),
        ("F3-L3-MIB", "f3VrfActionIfName"),
        ("F3-L3-MIB", "f3VrfIpVersion"),
        ("F3-L3-MIB", "f3VrfPingIpv6Destination"),
        ("F3-L3-MIB", "f3VrfTraceRouteIpv6Destination"),
        ("F3-L3-MIB", "f3L3FlowPointPortTypeIndex"),
        ("F3-L3-MIB", "f3L3FlowPointPortIndex"),
        ("F3-L3-MIB", "f3L3FlowPointIndex"),
        ("F3-L3-MIB", "f3L3FlowPointAlias"),
        ("F3-L3-MIB", "f3L3FlowPointAdminState"),
        ("F3-L3-MIB", "f3L3FlowPointSecondaryState"),
        ("F3-L3-MIB", "f3L3FlowPointOperationalState"),
        ("F3-L3-MIB", "f3L3FlowPointMultiCOSEnabled"),
        ("F3-L3-MIB", "f3L3FlowPointCOS"),
        ("F3-L3-MIB", "f3L3FlowPointUntaggedMemberShipEnabled"),
        ("F3-L3-MIB", "f3L3FlowPointOuterTagMemberShipEnabled"),
        ("F3-L3-MIB", "f3L3FlowPointOuterTagMemberShipVlanId"),
        ("F3-L3-MIB", "f3L3FlowPointInnerTagMemberShipEnabled"),
        ("F3-L3-MIB", "f3L3FlowPointInnerTagMemberShipVlanId"),
        ("F3-L3-MIB", "f3L3FlowPointFragmentedPktsFwdEnabled"),
        ("F3-L3-MIB", "f3L3FlowPointHCosMgmtEnabled"),
        ("F3-L3-MIB", "f3L3FlowPointHCosGuaranteedBwHi"),
        ("F3-L3-MIB", "f3L3FlowPointHCosGuaranteedBwLo"),
        ("F3-L3-MIB", "f3L3FlowPointHCosMaximumBwHi"),
        ("F3-L3-MIB", "f3L3FlowPointHCosMaximumBwLo"),
        ("F3-L3-MIB", "f3L3FlowPointPolicingEnabled"),
        ("F3-L3-MIB", "f3L3FlowPointStorageType"),
        ("F3-L3-MIB", "f3L3FlowPointRowStatus"),
        ("F3-L3-MIB", "f3L3FlowPointDscpOverwriteControl"),
        ("F3-L3-MIB", "f3L3FlowPointPriMapProfile"),
        ("F3-L3-MIB", "f3L3FlowPointRefConnectGuardFlow"),
        ("F3-L3-MIB", "f3L3FlowPointSecureState"),
        ("F3-L3-MIB", "f3L3FlowPointSecureBlockingEnabled"),
        ("F3-L3-MIB", "f3L3FlowPointWfqSegmentationCOS"),
        ("F3-L3-MIB", "f3L3FlowPointWfqGroupCOS"),
        ("F3-L3-MIB", "f3L3FlowPointWfqGroupEirLo"),
        ("F3-L3-MIB", "f3L3FlowPointWfqGroupEirHi"),
        ("F3-L3-MIB", "f3L3FlowPointOuterVlanEthertype"),
        ("F3-L3-MIB", "f3L3FlowPointInnerVlanEthertype"),
        ("F3-L3-MIB", "f3L3FlowPointIpVersion"),
        ("F3-L3-MIB", "f3L3AclRuleParentIndex"),
        ("F3-L3-MIB", "f3L3AclRuleIndex"),
        ("F3-L3-MIB", "f3L3AclRuleAlias"),
        ("F3-L3-MIB", "f3L3AclRuleSrcIpv4AddressControl"),
        ("F3-L3-MIB", "f3L3AclRuleDynamicSrcIpControl"),
        ("F3-L3-MIB", "f3L3AclRuleSrcIpv4AddressLowLimit"),
        ("F3-L3-MIB", "f3L3AclRuleDstIpv4AddressControl"),
        ("F3-L3-MIB", "f3L3AclRuleDstIpv4AddressLowLimit"),
        ("F3-L3-MIB", "f3L3AclRuleIpv4PriorityControl"),
        ("F3-L3-MIB", "f3L3AclRuleIpv4PriorityLowLimit"),
        ("F3-L3-MIB", "f3L3AclRuleProtocolControl"),
        ("F3-L3-MIB", "f3L3AclRuleProtocolNumber"),
        ("F3-L3-MIB", "f3L3AclRuleSrcPortControl"),
        ("F3-L3-MIB", "f3L3AclRuleSrcPortLowLimit"),
        ("F3-L3-MIB", "f3L3AclRuleSrcPortHighLimit"),
        ("F3-L3-MIB", "f3L3AclRuleDstPortControl"),
        ("F3-L3-MIB", "f3L3AclRuleDstPortLowLimit"),
        ("F3-L3-MIB", "f3L3AclRuleDstPortHighLimit"),
        ("F3-L3-MIB", "f3L3AclRulePriority"),
        ("F3-L3-MIB", "f3L3AclRuleCOS"),
        ("F3-L3-MIB", "f3L3AclRuleOperation"),
        ("F3-L3-MIB", "f3L3AclRuleSummary"),
        ("F3-L3-MIB", "f3L3AclRuleCosOverrideControl"),
        ("F3-L3-MIB", "f3L3AclRuleSrcMacAddressControl"),
        ("F3-L3-MIB", "f3L3AclRuleDynamicSrcMacAddressControl"),
        ("F3-L3-MIB", "f3L3AclRuleSrcMacAddress"),
        ("F3-L3-MIB", "f3L3AclRuleSrcMacAddressMask"),
        ("F3-L3-MIB", "f3L3AclRuleDstMacAddressControl"),
        ("F3-L3-MIB", "f3L3AclRuleDstMacAddress"),
        ("F3-L3-MIB", "f3L3AclRuleDstMacAddressMask"),
        ("F3-L3-MIB", "f3L3AclRuleOuterVlanVIDControl"),
        ("F3-L3-MIB", "f3L3AclRuleOuterVlanVIDLowLimit"),
        ("F3-L3-MIB", "f3L3AclRuleOuterVlanVIDHighLimit"),
        ("F3-L3-MIB", "f3L3AclRuleInnerVlanVIDControl"),
        ("F3-L3-MIB", "f3L3AclRuleInnerVlanVIDLowLimit"),
        ("F3-L3-MIB", "f3L3AclRuleInnerVlanVIDHighLimit"),
        ("F3-L3-MIB", "f3L3AclRuleOuterVlanPcpControl"),
        ("F3-L3-MIB", "f3L3AclRuleOuterVlanPcpLowLimit"),
        ("F3-L3-MIB", "f3L3AclRuleOuterVlanPcpHighLimit"),
        ("F3-L3-MIB", "f3L3AclRuleInnerVlanPcpControl"),
        ("F3-L3-MIB", "f3L3AclRuleInnerVlanPcpLowLimit"),
        ("F3-L3-MIB", "f3L3AclRuleInnerVlanPcpHighLimit"),
        ("F3-L3-MIB", "f3L3AclRuleOuterVlanDeiControl"),
        ("F3-L3-MIB", "f3L3AclRuleOuterVlanDei"),
        ("F3-L3-MIB", "f3L3AclRuleEtherTypeControl"),
        ("F3-L3-MIB", "f3L3AclRuleEtherType"),
        ("F3-L3-MIB", "f3L3AclRuleTcpFlagsControl"),
        ("F3-L3-MIB", "f3L3AclRuleTcpFlags"),
        ("F3-L3-MIB", "f3L3AclRuleSrcIpv4AddressHighLimit"),
        ("F3-L3-MIB", "f3L3AclRuleDstIpv4AddressHighLimit"),
        ("F3-L3-MIB", "f3L3AclRuleIpv4PriorityHighLimit"),
        ("F3-L3-MIB", "f3L3AclRuleStorageType"),
        ("F3-L3-MIB", "f3L3AclRuleRowStatus"),
        ("F3-L3-MIB", "f3L3AclRuleAdminState"),
        ("F3-L3-MIB", "f3L3AclRuleActive"),
        ("F3-L3-MIB", "f3L3AclRuleSrcIpV6AddressControl"),
        ("F3-L3-MIB", "f3L3AclRuleSrcIpV6Address"),
        ("F3-L3-MIB", "f3L3AclRuleSrcIpV6AddressPrefixLen"),
        ("F3-L3-MIB", "f3L3AclRuleDstIpV6AddressControl"),
        ("F3-L3-MIB", "f3L3AclRuleDstIpV6Address"),
        ("F3-L3-MIB", "f3L3AclRuleDstIpV6AddressPrefixLen"),
        ("F3-L3-MIB", "f3L3AclRuleIpV6FlowLabelControl"),
        ("F3-L3-MIB", "f3L3AclRuleIpV6FlowLabel"),
        ("F3-L3-MIB", "f3L3AclRuleIpV6FlowLabel"),
        ("F3-L3-MIB", "f3L3AclRulePriorityControl"),
        ("F3-L3-MIB", "f3L3AclRulePriorityLowLimit"),
        ("F3-L3-MIB", "f3L3AclRulePriorityHighLimit"),
        ("F3-L3-MIB", "f3L2A2NAclRuleParentIndex"),
        ("F3-L3-MIB", "f3L2A2NAclRuleIndex"),
        ("F3-L3-MIB", "f3L2A2NAclRuleAlias"),
        ("F3-L3-MIB", "f3L2A2NAclRuleSrcIpv4AddressControl"),
        ("F3-L3-MIB", "f3L2A2NAclRuleDynamicSrcIpControl"),
        ("F3-L3-MIB", "f3L2A2NAclRuleSrcIpv4AddressLowLimit"),
        ("F3-L3-MIB", "f3L2A2NAclRuleDstIpv4AddressControl"),
        ("F3-L3-MIB", "f3L2A2NAclRuleDstIpv4AddressLowLimit"),
        ("F3-L3-MIB", "f3L2A2NAclRuleIpv4PriorityControl"),
        ("F3-L3-MIB", "f3L2A2NAclRuleIpv4PriorityLowLimit"),
        ("F3-L3-MIB", "f3L2A2NAclRuleProtocolControl"),
        ("F3-L3-MIB", "f3L2A2NAclRuleProtocolNumber"),
        ("F3-L3-MIB", "f3L2A2NAclRuleSrcPortControl"),
        ("F3-L3-MIB", "f3L2A2NAclRuleSrcPortLowLimit"),
        ("F3-L3-MIB", "f3L2A2NAclRuleSrcPortHighLimit"),
        ("F3-L3-MIB", "f3L2A2NAclRuleDstPortControl"),
        ("F3-L3-MIB", "f3L2A2NAclRuleDstPortLowLimit"),
        ("F3-L3-MIB", "f3L2A2NAclRuleDstPortHighLimit"),
        ("F3-L3-MIB", "f3L2A2NAclRulePriority"),
        ("F3-L3-MIB", "f3L2A2NAclRuleCOS"),
        ("F3-L3-MIB", "f3L2A2NAclRuleOperation"),
        ("F3-L3-MIB", "f3L2A2NAclRuleSummary"),
        ("F3-L3-MIB", "f3L2A2NAclRuleCosOverrideControl"),
        ("F3-L3-MIB", "f3L2A2NAclRuleSrcMacAddressControl"),
        ("F3-L3-MIB", "f3L2A2NAclRuleDynamicSrcMacAddressControl"),
        ("F3-L3-MIB", "f3L2A2NAclRuleSrcMacAddress"),
        ("F3-L3-MIB", "f3L2A2NAclRuleSrcMacAddressMask"),
        ("F3-L3-MIB", "f3L2A2NAclRuleDstMacAddressControl"),
        ("F3-L3-MIB", "f3L2A2NAclRuleDstMacAddress"),
        ("F3-L3-MIB", "f3L2A2NAclRuleDstMacAddressMask"),
        ("F3-L3-MIB", "f3L2A2NAclRuleOuterVlanVIDControl"),
        ("F3-L3-MIB", "f3L2A2NAclRuleOuterVlanVIDLowLimit"),
        ("F3-L3-MIB", "f3L2A2NAclRuleOuterVlanVIDHighLimit"),
        ("F3-L3-MIB", "f3L2A2NAclRuleInnerVlanVIDControl"),
        ("F3-L3-MIB", "f3L2A2NAclRuleInnerVlanVIDLowLimit"),
        ("F3-L3-MIB", "f3L2A2NAclRuleInnerVlanVIDHighLimit"),
        ("F3-L3-MIB", "f3L2A2NAclRuleOuterVlanPcpControl"),
        ("F3-L3-MIB", "f3L2A2NAclRuleOuterVlanPcpLowLimit"),
        ("F3-L3-MIB", "f3L2A2NAclRuleOuterVlanPcpHighLimit"),
        ("F3-L3-MIB", "f3L2A2NAclRuleInnerVlanPcpControl"),
        ("F3-L3-MIB", "f3L2A2NAclRuleInnerVlanPcpLowLimit"),
        ("F3-L3-MIB", "f3L2A2NAclRuleInnerVlanPcpHighLimit"),
        ("F3-L3-MIB", "f3L2A2NAclRuleOuterVlanDeiControl"),
        ("F3-L3-MIB", "f3L2A2NAclRuleOuterVlanDei"),
        ("F3-L3-MIB", "f3L2A2NAclRuleEtherTypeControl"),
        ("F3-L3-MIB", "f3L2A2NAclRuleEtherType"),
        ("F3-L3-MIB", "f3L2A2NAclRuleTcpFlagsControl"),
        ("F3-L3-MIB", "f3L2A2NAclRuleTcpFlags"),
        ("F3-L3-MIB", "f3L2A2NAclRuleSrcIpv4AddressHighLimit"),
        ("F3-L3-MIB", "f3L2A2NAclRuleDstIpv4AddressHighLimit"),
        ("F3-L3-MIB", "f3L2A2NAclRuleIpv4PriorityHighLimit"),
        ("F3-L3-MIB", "f3L2A2NAclRuleStorageType"),
        ("F3-L3-MIB", "f3L2A2NAclRuleRowStatus"),
        ("F3-L3-MIB", "f3L2A2NAclRuleAdminState"),
        ("F3-L3-MIB", "f3L2A2NAclRuleActive"),
        ("F3-L3-MIB", "f3L2A2NAclRuleSrcIpV6AddressControl"),
        ("F3-L3-MIB", "f3L2A2NAclRuleSrcIpV6Address"),
        ("F3-L3-MIB", "f3L2A2NAclRuleSrcIpV6AddressPrefixLen"),
        ("F3-L3-MIB", "f3L2A2NAclRuleDstIpV6AddressControl"),
        ("F3-L3-MIB", "f3L2A2NAclRuleDstIpV6Address"),
        ("F3-L3-MIB", "f3L2A2NAclRuleDstIpV6AddressPrefixLen"),
        ("F3-L3-MIB", "f3L2A2NAclRuleIpV6FlowLabelControl"),
        ("F3-L3-MIB", "f3L2A2NAclRuleIpV6FlowLabel"),
        ("F3-L3-MIB", "f3L2N2AAclRuleParentIndex"),
        ("F3-L3-MIB", "f3L2N2AAclRuleIndex"),
        ("F3-L3-MIB", "f3L2N2AAclRuleAlias"),
        ("F3-L3-MIB", "f3L2N2AAclRuleSrcIpv4AddressControl"),
        ("F3-L3-MIB", "f3L2N2AAclRuleDynamicSrcIpControl"),
        ("F3-L3-MIB", "f3L2N2AAclRuleSrcIpv4AddressLowLimit"),
        ("F3-L3-MIB", "f3L2N2AAclRuleDstIpv4AddressControl"),
        ("F3-L3-MIB", "f3L2N2AAclRuleDstIpv4AddressLowLimit"),
        ("F3-L3-MIB", "f3L2N2AAclRuleIpv4PriorityControl"),
        ("F3-L3-MIB", "f3L2N2AAclRuleIpv4PriorityLowLimit"),
        ("F3-L3-MIB", "f3L2N2AAclRuleProtocolControl"),
        ("F3-L3-MIB", "f3L2N2AAclRuleProtocolNumber"),
        ("F3-L3-MIB", "f3L2N2AAclRuleSrcPortControl"),
        ("F3-L3-MIB", "f3L2N2AAclRuleSrcPortLowLimit"),
        ("F3-L3-MIB", "f3L2N2AAclRuleSrcPortHighLimit"),
        ("F3-L3-MIB", "f3L2N2AAclRuleDstPortControl"),
        ("F3-L3-MIB", "f3L2N2AAclRuleDstPortLowLimit"),
        ("F3-L3-MIB", "f3L2N2AAclRuleDstPortHighLimit"),
        ("F3-L3-MIB", "f3L2N2AAclRulePriority"),
        ("F3-L3-MIB", "f3L2N2AAclRuleCOS"),
        ("F3-L3-MIB", "f3L2N2AAclRuleOperation"),
        ("F3-L3-MIB", "f3L2N2AAclRuleSummary"),
        ("F3-L3-MIB", "f3L2N2AAclRuleCosOverrideControl"),
        ("F3-L3-MIB", "f3L2N2AAclRuleSrcMacAddressControl"),
        ("F3-L3-MIB", "f3L2N2AAclRuleDynamicSrcMacAddressControl"),
        ("F3-L3-MIB", "f3L2N2AAclRuleSrcMacAddress"),
        ("F3-L3-MIB", "f3L2N2AAclRuleSrcMacAddressMask"),
        ("F3-L3-MIB", "f3L2N2AAclRuleDstMacAddressControl"),
        ("F3-L3-MIB", "f3L2N2AAclRuleDstMacAddress"),
        ("F3-L3-MIB", "f3L2N2AAclRuleDstMacAddressMask"),
        ("F3-L3-MIB", "f3L2N2AAclRuleOuterVlanVIDControl"),
        ("F3-L3-MIB", "f3L2N2AAclRuleOuterVlanVIDLowLimit"),
        ("F3-L3-MIB", "f3L2N2AAclRuleOuterVlanVIDHighLimit"),
        ("F3-L3-MIB", "f3L2N2AAclRuleInnerVlanVIDControl"),
        ("F3-L3-MIB", "f3L2N2AAclRuleInnerVlanVIDLowLimit"),
        ("F3-L3-MIB", "f3L2N2AAclRuleInnerVlanVIDHighLimit"),
        ("F3-L3-MIB", "f3L2N2AAclRuleOuterVlanPcpControl"),
        ("F3-L3-MIB", "f3L2N2AAclRuleOuterVlanPcpLowLimit"),
        ("F3-L3-MIB", "f3L2N2AAclRuleOuterVlanPcpHighLimit"),
        ("F3-L3-MIB", "f3L2N2AAclRuleInnerVlanPcpControl"),
        ("F3-L3-MIB", "f3L2N2AAclRuleInnerVlanPcpLowLimit"),
        ("F3-L3-MIB", "f3L2N2AAclRuleInnerVlanPcpHighLimit"),
        ("F3-L3-MIB", "f3L2N2AAclRuleOuterVlanDeiControl"),
        ("F3-L3-MIB", "f3L2N2AAclRuleOuterVlanDei"),
        ("F3-L3-MIB", "f3L2N2AAclRuleEtherTypeControl"),
        ("F3-L3-MIB", "f3L2N2AAclRuleEtherType"),
        ("F3-L3-MIB", "f3L2N2AAclRuleTcpFlagsControl"),
        ("F3-L3-MIB", "f3L2N2AAclRuleTcpFlags"),
        ("F3-L3-MIB", "f3L2N2AAclRuleSrcIpv4AddressHighLimit"),
        ("F3-L3-MIB", "f3L2N2AAclRuleDstIpv4AddressHighLimit"),
        ("F3-L3-MIB", "f3L2N2AAclRuleIpv4PriorityHighLimit"),
        ("F3-L3-MIB", "f3L2N2AAclRuleStorageType"),
        ("F3-L3-MIB", "f3L2N2AAclRuleRowStatus"),
        ("F3-L3-MIB", "f3L2N2AAclRuleAdminState"),
        ("F3-L3-MIB", "f3L2N2AAclRuleActive"),
        ("F3-L3-MIB", "f3L2N2AAclRuleSrcIpV6AddressControl"),
        ("F3-L3-MIB", "f3L2N2AAclRuleSrcIpV6Address"),
        ("F3-L3-MIB", "f3L2N2AAclRuleSrcIpV6AddressPrefixLen"),
        ("F3-L3-MIB", "f3L2N2AAclRuleDstIpV6AddressControl"),
        ("F3-L3-MIB", "f3L2N2AAclRuleDstIpV6Address"),
        ("F3-L3-MIB", "f3L2N2AAclRuleDstIpV6AddressPrefixLen"),
        ("F3-L3-MIB", "f3L3AclRuleIpV6FlowLabelControl"),
        ("F3-L3-MIB", "f3L3AclRuleIpV6FlowLabel"),
        ("F3-L3-MIB", "f3L3QosPolicerIndex"),
        ("F3-L3-MIB", "f3L3QosPolicerAdminState"),
        ("F3-L3-MIB", "f3L3QosPolicerOperationalState"),
        ("F3-L3-MIB", "f3L3QosPolicerSecondaryState"),
        ("F3-L3-MIB", "f3L3QosPolicerCIRLo"),
        ("F3-L3-MIB", "f3L3QosPolicerCIRHi"),
        ("F3-L3-MIB", "f3L3QosPolicerEIRLo"),
        ("F3-L3-MIB", "f3L3QosPolicerEIRHi"),
        ("F3-L3-MIB", "f3L3QosPolicerCBS"),
        ("F3-L3-MIB", "f3L3QosPolicerEBS"),
        ("F3-L3-MIB", "f3L3QosPolicerAlgorithm"),
        ("F3-L3-MIB", "f3L3QosPolicerColorMode"),
        ("F3-L3-MIB", "f3L3QosPolicerCouplingFlag"),
        ("F3-L3-MIB", "f3L3QosPolicerStorageType"),
        ("F3-L3-MIB", "f3L3QosPolicerRowStatus"),
        ("F3-L3-MIB", "f3L3QosPolicerCIRMaxHi"),
        ("F3-L3-MIB", "f3L3QosPolicerCIRMaxLo"),
        ("F3-L3-MIB", "f3L3QosPolicerEIRMaxHi"),
        ("F3-L3-MIB", "f3L3QosPolicerEIRMaxLo"),
        ("F3-L3-MIB", "f3L3QosPolicerEnvelopeObject"),
        ("F3-L3-MIB", "f3L3QosPolicerRank"),
        ("F3-L3-MIB", "f3L3QosPolicerPolicingEnabled"),
        ("F3-L3-MIB", "f3L3QosShaperIndex"),
        ("F3-L3-MIB", "f3L3QosShaperAdminState"),
        ("F3-L3-MIB", "f3L3QosShaperOperationalState"),
        ("F3-L3-MIB", "f3L3QosShaperSecondaryState"),
        ("F3-L3-MIB", "f3L3QosShaperCIRLo"),
        ("F3-L3-MIB", "f3L3QosShaperCIRHi"),
        ("F3-L3-MIB", "f3L3QosShaperEIRLo"),
        ("F3-L3-MIB", "f3L3QosShaperEIRHi"),
        ("F3-L3-MIB", "f3L3QosShaperBufferSize"),
        ("F3-L3-MIB", "f3L3QosShaperCOS"),
        ("F3-L3-MIB", "f3L3QosShaperWredGreenMinQueueThreshold"),
        ("F3-L3-MIB", "f3L3QosShaperWredGreenMaxQueueThreshold"),
        ("F3-L3-MIB", "f3L3QosShaperWredGreenDropProbability"),
        ("F3-L3-MIB", "f3L3QosShaperWredYellowMinQueueThreshold"),
        ("F3-L3-MIB", "f3L3QosShaperWredYellowMaxQueueThreshold"),
        ("F3-L3-MIB", "f3L3QosShaperWredYellowDropProbability"),
        ("F3-L3-MIB", "f3L3QosShaperStorageType"),
        ("F3-L3-MIB", "f3L3QosShaperRowStatus"),
        ("F3-L3-MIB", "f3L3QosShaperWfqWeight"),
        ("F3-L3-MIB", "f3L3TrafficIPIfIndex"),
        ("F3-L3-MIB", "f3L3TrafficIPIfName"),
        ("F3-L3-MIB", "f3L3TrafficIPIfAdminState"),
        ("F3-L3-MIB", "f3L3TrafficIPIfSecondaryState"),
        ("F3-L3-MIB", "f3L3TrafficIPIfOperationalState"),
        ("F3-L3-MIB", "f3L3TrafficIPIfProxyArpEnabled"),
        ("F3-L3-MIB", "f3L3TrafficIPIfIpAddressSourceType"),
        ("F3-L3-MIB", "f3L3TrafficIPIfMgmtUseEnable"),
        ("F3-L3-MIB", "f3L3TrafficIPIfIpAddress"),
        ("F3-L3-MIB", "f3L3TrafficIPIfMask"),
        ("F3-L3-MIB", "f3L3TrafficIPIfDhcpRelayInterfaceSide"),
        ("F3-L3-MIB", "f3L3TrafficIPIfDhcpRelayVendorClassiDOpt60"),
        ("F3-L3-MIB", "f3L3TrafficIPIfDhcpRelayVendorClassiDOpt60Control"),
        ("F3-L3-MIB", "f3L3TrafficIPIfDhcpRelayUserClassOpt77"),
        ("F3-L3-MIB", "f3L3TrafficIPIfDhcpRelayInfoOpt82Sub1"),
        ("F3-L3-MIB", "f3L3TrafficIPIfDhcpRelayUserClassOpt77Control"),
        ("F3-L3-MIB", "f3L3TrafficIPIfDhcpRelayInfoOpt82Sub1Enabled"),
        ("F3-L3-MIB", "f3L3TrafficIPIfDhcpRelayInfoOpt82Sub2"),
        ("F3-L3-MIB", "f3L3TrafficIPIfDhcpRelayInfoOpt82Sub2Enabled"),
        ("F3-L3-MIB", "f3L3TrafficIPIfDhcpEnabled"),
        ("F3-L3-MIB", "f3L3TrafficIPIfDhcpRole"),
        ("F3-L3-MIB", "f3L3TrafficIPIfDhcpClientIdEnabled"),
        ("F3-L3-MIB", "f3L3TrafficIPIfDhcpClientId"),
        ("F3-L3-MIB", "f3L3TrafficIPIfDhcpClassIdEnabled"),
        ("F3-L3-MIB", "f3L3TrafficIPIfDhcpHostNameEnabled"),
        ("F3-L3-MIB", "f3L3TrafficIPIfDhcpHostName"),
        ("F3-L3-MIB", "f3L3TrafficIPIfDhcpClientIdType"),
        ("F3-L3-MIB", "f3L3TrafficIPIfDhcpHostNameType"),
        ("F3-L3-MIB", "f3L3TrafficIPIfStorageType"),
        ("F3-L3-MIB", "f3L3TrafficIPIfRowStatus"),
        ("F3-L3-MIB", "f3L3TrafficIPIfAction"),
        ("F3-L3-MIB", "f3L3TrafficIPIfActionX"),
        ("F3-L3-MIB", "f3L3TrafficIPIfUnnumberedControl"),
        ("F3-L3-MIB", "f3L3TrafficIPIfBorrowedIntf"),
        ("F3-L3-MIB", "f3L3TrafficIPIfIpMode"),
        ("F3-L3-MIB", "f3L3TrafficIPIfType"),
        ("F3-L3-MIB", "f3L3TrafficIPIfIpv6LinkLocalAddr"),
        ("F3-L3-MIB", "f3L3TrafficIPIfIpv6LinkLocalAddrMode"),
        ("F3-L3-MIB", "f3L3TrafficIPIfIpv6StatelessAddrAutoconfigEnabled"),
        ("F3-L3-MIB", "f3L3TrafficIPIfDefaultGateway"),
        ("F3-L3-MIB", "f3L3TrafficIPIfIcmpErrorMsgRateLimit"),
        ("F3-L3-MIB", "f3L3TrafficIPIfDhcpv6Role"),
        ("F3-L3-MIB", "f3L3TrafficIPIfDhcpv6Enabled"),
        ("F3-L3-MIB", "f3L3TrafficIPIfDhcpRapidCommitControlEnabled"),
        ("F3-L3-MIB", "f3L3TrafficIPIfMaxRAInterval"),
        ("F3-L3-MIB", "f3L3TrafficIPIfMinRAInterval"),
        ("F3-L3-MIB", "f3L3TrafficIPIfRouterLifeTime"),
        ("F3-L3-MIB", "f3L3TrafficIPIfReachableTime"),
        ("F3-L3-MIB", "f3L3TrafficIPIfRaDhcpMoreConfigEnabled"),
        ("F3-L3-MIB", "f3L3TrafficIPIfRaManagedAddressConfigEnabled"),
        ("F3-L3-MIB", "f3L3TrafficIPIfRaRDNSSOptionEnabled"),
        ("F3-L3-MIB", "f3L3TrafficIPIfRaRDNSSLifeTime"),
        ("F3-L3-MIB", "f3L3TrafficIPIfRaDNSSList"),
        ("F3-L3-MIB", "f3L3TrafficIPIfRaDefaultRouterPreference"),
        ("F3-L3-MIB", "f3L3TrafficIPIfDupAddrDetectControl"),
        ("F3-L3-MIB", "f3L3TrafficIPIfDupAddrDetectTransmits"),
        ("F3-L3-MIB", "f3L3TrafficIPIfDupAddrDetectRetransTimer"),
        ("F3-L3-MIB", "f3L3TrafficIPIfMTU"),
        ("F3-L3-MIB", "f3VrfActionIfName"),
        ("F3-L3-MIB", "f3VrfIpVersion"),
        ("F3-L3-MIB", "f3VrfPingIpv6Destination"),
        ("F3-L3-MIB", "f3VrfTraceRouteIpv6Destination"),
        ("F3-L3-MIB", "f3VrfMaxFwdTableEntries"),
        ("F3-L3-MIB", "f3VrfFwdTableFull"),
        ("F3-L3-MIB", "f3VrfEcmpDistribution"),
        ("F3-L3-MIB", "f3VrfEcmpStaticRoutesMaximumPaths"),
        ("F3-L3-MIB", "f3DhcpRelayAgentTrafficIpIfMemberObject"),
        ("F3-L3-MIB", "f3DhcpRelayAgentTrafficIpIfMemberStorageType"),
        ("F3-L3-MIB", "f3DhcpRelayAgentTrafficIpIfMemberRowStatus"),
        ("F3-L3-MIB", "f3VrfTrafficIpIfMemberObject"),
        ("F3-L3-MIB", "f3VrfTrafficIpIfMemberStorageType"),
        ("F3-L3-MIB", "f3VrfTrafficIpIfMemberRowStatus"),
        ("F3-L3-MIB", "f3L3TrafficIpv4RouteDest"),
        ("F3-L3-MIB", "f3L3TrafficIpv4RouteMask"),
        ("F3-L3-MIB", "f3L3TrafficIpv4RouteNextHop"),
        ("F3-L3-MIB", "f3L3TrafficIpv4RouteMetric"),
        ("F3-L3-MIB", "f3L3TrafficIpv4RouteInterface"),
        ("F3-L3-MIB", "f3L3TrafficIpv4RouteAdvertise"),
        ("F3-L3-MIB", "f3L3TrafficIpv4RouteStatus"),
        ("F3-L3-MIB", "f3L3TrafficIpv4RouteStatusX"),
        ("F3-L3-MIB", "f3L3TrafficIpv4RouteSourceForwardingEnable"),
        ("F3-L3-MIB", "f3L3TrafficIpv4RouteFlags"),
        ("F3-L3-MIB", "f3L3TrafficIpv4RouteStorageType"),
        ("F3-L3-MIB", "f3L3TrafficIpv4RouteRowStatus"),
        ("F3-L3-MIB", "f3L3TrafficIpv4RouteType"),
        ("F3-L3-MIB", "f3L3TrafficIpv4RouteStatusX"),
        ("F3-L3-MIB", "f3L3TrafficIpv4RouteOrigin"),
        ("F3-L3-MIB", "f3L3TrafficArpIPAddress"),
        ("F3-L3-MIB", "f3L3TrafficArpMacAddress"),
        ("F3-L3-MIB", "f3L3TrafficArpInterface"),
        ("F3-L3-MIB", "f3L3TrafficArpEntryType"),
        ("F3-L3-MIB", "f3L3TrafficArpStorageType"),
        ("F3-L3-MIB", "f3L3TrafficArpRowStatus"),
        ("F3-L3-MIB", "cmL3FlowPointPortIndex"),
        ("F3-L3-MIB", "cmL3FlowPointIndex"),
        ("F3-L3-MIB", "cmL3FlowPointAlias"),
        ("F3-L3-MIB", "cmL3FlowPointAdminState"),
        ("F3-L3-MIB", "cmL3FlowPointSecondaryState"),
        ("F3-L3-MIB", "cmL3FlowPointOperationalState"),
        ("F3-L3-MIB", "cmL3FlowPointMultiCOSEnabled"),
        ("F3-L3-MIB", "cmL3FlowPointCOS"),
        ("F3-L3-MIB", "cmL3FlowPointUntaggedMemberShipEnabled"),
        ("F3-L3-MIB", "cmL3FlowPointOuterTagMemberShipEnabled"),
        ("F3-L3-MIB", "cmL3FlowPointOuterTagMemberShipVlanId"),
        ("F3-L3-MIB", "cmL3FlowPointInnerTagMemberShipEnabled"),
        ("F3-L3-MIB", "cmL3FlowPointInnerTagMemberShipVlanId"),
        ("F3-L3-MIB", "cmL3FlowPointFragmentedPktsFwdEnabled"),
        ("F3-L3-MIB", "cmL3FlowPointHCosMgmtEnabled"),
        ("F3-L3-MIB", "cmL3FlowPointHCosGuaranteedBwHi"),
        ("F3-L3-MIB", "cmL3FlowPointHCosGuaranteedBwLo"),
        ("F3-L3-MIB", "cmL3FlowPointHCosMaximumBwHi"),
        ("F3-L3-MIB", "cmL3FlowPointHCosMaximumBwLo"),
        ("F3-L3-MIB", "cmL3FlowPointDscpOverwriteControl"),
        ("F3-L3-MIB", "cmL3FlowPointPriMapProfile"),
        ("F3-L3-MIB", "cmL3FlowPointStorageType"),
        ("F3-L3-MIB", "cmL3FlowPointRowStatus"),
        ("F3-L3-MIB", "cmL3FlowPointAclNoMatchDisposition"),
        ("F3-L3-MIB", "cmL3FlowPointWfqSegmentationCOS"),
        ("F3-L3-MIB", "cmL3FlowPointWfqGroupCOS"),
        ("F3-L3-MIB", "cmL3FlowPointWfqGroupEirLo"),
        ("F3-L3-MIB", "cmL3FlowPointWfqGroupEirHi"),
        ("F3-L3-MIB", "cmL3FlowPointEgressShapingType"),
        ("F3-L3-MIB", "cmL3QosPolicerIndex"),
        ("F3-L3-MIB", "cmL3QosPolicerAdminState"),
        ("F3-L3-MIB", "cmL3QosPolicerOperationalState"),
        ("F3-L3-MIB", "cmL3QosPolicerSecondaryState"),
        ("F3-L3-MIB", "cmL3QosPolicerCIRLo"),
        ("F3-L3-MIB", "cmL3QosPolicerCIRHi"),
        ("F3-L3-MIB", "cmL3QosPolicerEIRLo"),
        ("F3-L3-MIB", "cmL3QosPolicerEIRHi"),
        ("F3-L3-MIB", "cmL3QosPolicerCBS"),
        ("F3-L3-MIB", "cmL3QosPolicerEBS"),
        ("F3-L3-MIB", "cmL3QosPolicerAlgorithm"),
        ("F3-L3-MIB", "cmL3QosPolicerColorMode"),
        ("F3-L3-MIB", "cmL3QosPolicerCouplingFlag"),
        ("F3-L3-MIB", "cmL3QosPolicerCIRMaxHi"),
        ("F3-L3-MIB", "cmL3QosPolicerCIRMaxLo"),
        ("F3-L3-MIB", "cmL3QosPolicerEIRMaxHi"),
        ("F3-L3-MIB", "cmL3QosPolicerEIRMaxLo"),
        ("F3-L3-MIB", "cmL3QosPolicerEnvelopeObject"),
        ("F3-L3-MIB", "cmL3QosPolicerRank"),
        ("F3-L3-MIB", "cmL3QosPolicerPolicingEnabled"),
        ("F3-L3-MIB", "cmL3QosPolicerStorageType"),
        ("F3-L3-MIB", "cmL3QosPolicerRowStatus"),
        ("F3-L3-MIB", "cmL3QosShaperIndex"),
        ("F3-L3-MIB", "cmL3QosShaperAdminState"),
        ("F3-L3-MIB", "cmL3QosShaperOperationalState"),
        ("F3-L3-MIB", "cmL3QosShaperSecondaryState"),
        ("F3-L3-MIB", "cmL3QosShaperCIRLo"),
        ("F3-L3-MIB", "cmL3QosShaperCIRHi"),
        ("F3-L3-MIB", "cmL3QosShaperEIRLo"),
        ("F3-L3-MIB", "cmL3QosShaperEIRHi"),
        ("F3-L3-MIB", "cmL3QosShaperBufferSize"),
        ("F3-L3-MIB", "cmL3QosShaperCOS"),
        ("F3-L3-MIB", "cmL3QosShaperStorageType"),
        ("F3-L3-MIB", "cmL3QosShaperRowStatus"),
        ("F3-L3-MIB", "cmL3QosShaperWfqWeight"),
        ("F3-L3-MIB", "f3L3TrafficIpv4StaticRouteDest"),
        ("F3-L3-MIB", "f3L3TrafficIpv4StaticRouteMask"),
        ("F3-L3-MIB", "f3L3TrafficIpv4StaticRouteNextHop"),
        ("F3-L3-MIB", "f3L3TrafficIpv4StaticRouteInterface"),
        ("F3-L3-MIB", "f3L3TrafficIpv4StaticRouteMetric"),
        ("F3-L3-MIB", "f3L3TrafficIpv4StaticRouteSourceForwardingEnable"),
        ("F3-L3-MIB", "f3L3TrafficIpv4StaticRouteStorageType"),
        ("F3-L3-MIB", "f3L3TrafficIpv4StaticRouteRowStatus"),
        ("F3-L3-MIB", "f3L3TrafficIpv4AllRouteDest"),
        ("F3-L3-MIB", "f3L3TrafficIpv4AllRouteMask"),
        ("F3-L3-MIB", "f3L3TrafficIpv4AllRouteNextHop"),
        ("F3-L3-MIB", "f3L3TrafficIpv4AllRouteInterface"),
        ("F3-L3-MIB", "f3L3TrafficIpv4AllRouteOrigin"),
        ("F3-L3-MIB", "f3L3TrafficIpv4AllRouteMetric"),
        ("F3-L3-MIB", "f3L3TrafficIpv4AllRouteSourceForwardingEnable"),
        ("F3-L3-MIB", "f3L3TrafficIpv4AllRouteAdminDistance"),
        ("F3-L3-MIB", "f3L3TrafficIpv4AllRouteStatus"),
        ("F3-L3-MIB", "f3L3TrafficIpv4AllRouteStorageType"),
        ("F3-L3-MIB", "f3L3TrafficIpv4AllRouteRowStatus"),
        ("F3-L3-MIB", "f3L3TrafficIpv6StaticRouteDest"),
        ("F3-L3-MIB", "f3L3TrafficIpv6StaticRoutePrefixLength"),
        ("F3-L3-MIB", "f3L3TrafficIpv6StaticRouteNextHop"),
        ("F3-L3-MIB", "f3L3TrafficIpv6StaticRouteInterface"),
        ("F3-L3-MIB", "f3L3TrafficIpv6StaticRouteMetric"),
        ("F3-L3-MIB", "f3L3TrafficIpv6StaticRouteStorageType"),
        ("F3-L3-MIB", "f3L3TrafficIpv6StaticRouteRowStatus"),
        ("F3-L3-MIB", "f3L3TrafficIpv6AllRouteDest"),
        ("F3-L3-MIB", "f3L3TrafficIpv6AllRoutePrefixLength"),
        ("F3-L3-MIB", "f3L3TrafficIpv6AllRouteNextHop"),
        ("F3-L3-MIB", "f3L3TrafficIpv6AllRouteInterface"),
        ("F3-L3-MIB", "f3L3TrafficIpv6AllRouteOrigin"),
        ("F3-L3-MIB", "f3L3TrafficIpv6AllRouteMetric"),
        ("F3-L3-MIB", "f3L3TrafficIpv6AllRouteAdminDistance"),
        ("F3-L3-MIB", "f3L3TrafficIpv6AllRouteStatus"),
        ("F3-L3-MIB", "f3L3TrafficIpv6AllRouteStorageType"),
        ("F3-L3-MIB", "f3L3TrafficIpv6AllRouteRowStatus"),
        ("F3-L3-MIB", "f3IpPrefixListIndex"),
        ("F3-L3-MIB", "f3IpPrefixListName"),
        ("F3-L3-MIB", "f3IpPrefixListDefaultDisposition"),
        ("F3-L3-MIB", "f3IpPrefixListStorageType"),
        ("F3-L3-MIB", "f3IpPrefixListRowStatus"),
        ("F3-L3-MIB", "f3IpPrefixIndex"),
        ("F3-L3-MIB", "f3IpPrefix"),
        ("F3-L3-MIB", "f3IpPrefixPriority"),
        ("F3-L3-MIB", "f3IpPrefixDisposition"),
        ("F3-L3-MIB", "f3IpPrefixLessOrEqualPrefixLen"),
        ("F3-L3-MIB", "f3IpPrefixGreaterOrEqualPrefixLen"),
        ("F3-L3-MIB", "f3IpPrefixStorageType"),
        ("F3-L3-MIB", "f3IpPrefixRowStatus"))
)
if mibBuilder.loadTexts:
    f3L3ObjectsGroup.setStatus("current")

f3L3PerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 4, 2, 2)
)
f3L3PerfGroup.setObjects(
      *(("F3-L3-MIB", "f3L3FlowPointStatsIndex"),
        ("F3-L3-MIB", "f3L3FlowPointStatsIntervalType"),
        ("F3-L3-MIB", "f3L3FlowPointStatsValid"),
        ("F3-L3-MIB", "f3L3FlowPointStatsAction"),
        ("F3-L3-MIB", "f3L3FlowPointStatsFMG"),
        ("F3-L3-MIB", "f3L3FlowPointStatsFMY"),
        ("F3-L3-MIB", "f3L3FlowPointStatsFMRD"),
        ("F3-L3-MIB", "f3L3FlowPointStatsFTD"),
        ("F3-L3-MIB", "f3L3FlowPointStatsFragmentedDropAcl"),
        ("F3-L3-MIB", "f3L3FlowPointStatsAclRuleDrop"),
        ("F3-L3-MIB", "f3L3FlowPointStatsTtlEqual1Drop"),
        ("F3-L3-MIB", "f3L3FlowPointStatsFrameTx"),
        ("F3-L3-MIB", "f3L3FlowPointStatsFrameRx"),
        ("F3-L3-MIB", "f3L3FlowPointStatsNoRouteDrop"),
        ("F3-L3-MIB", "f3L3FlowPointStatsHopLimitDrop"),
        ("F3-L3-MIB", "f3L3FlowPointHistoryIndex"),
        ("F3-L3-MIB", "f3L3FlowPointHistoryTime"),
        ("F3-L3-MIB", "f3L3FlowPointHistoryValid"),
        ("F3-L3-MIB", "f3L3FlowPointHistoryAction"),
        ("F3-L3-MIB", "f3L3FlowPointHistoryFMG"),
        ("F3-L3-MIB", "f3L3FlowPointHistoryFMY"),
        ("F3-L3-MIB", "f3L3FlowPointHistoryFMRD"),
        ("F3-L3-MIB", "f3L3FlowPointHistoryFTD"),
        ("F3-L3-MIB", "f3L3FlowPointHistoryFragmentedDropAcl"),
        ("F3-L3-MIB", "f3L3FlowPointHistoryAclRuleDrop"),
        ("F3-L3-MIB", "f3L3FlowPointHistoryTtlEqual1Drop"),
        ("F3-L3-MIB", "f3L3FlowPointHistoryFrameTx"),
        ("F3-L3-MIB", "f3L3FlowPointHistoryFrameRx"),
        ("F3-L3-MIB", "f3L3FlowPointHistoryNoRouteDrop"),
        ("F3-L3-MIB", "f3L3FlowPointHistoryHopLimitDrop"),
        ("F3-L3-MIB", "f3L3FlowPointThresholdIndex"),
        ("F3-L3-MIB", "f3L3FlowPointThresholdInterval"),
        ("F3-L3-MIB", "f3L3FlowPointThresholdVariable"),
        ("F3-L3-MIB", "f3L3FlowPointThresholdValueLo"),
        ("F3-L3-MIB", "f3L3FlowPointThresholdValueHi"),
        ("F3-L3-MIB", "f3L3FlowPointThresholdMonValue"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceStatsIndex"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceStatsIntervalType"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceStatsValid"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceStatsAction"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceStatsDhcpTx"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceStatsDhcpRx"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceStatsIcmpTx"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceStatsIcmpRx"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceStatsArpReqTx"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceStatsArpReqRx"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceStatsArpReplyTx"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceStatsArpReplyRx"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceStatsDhcpV6Tx"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceStatsDhcpV6Rx"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceStatsIcmpV6WONdpTx"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceStatsIcmpV6WONdpRx"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceStatsNdpNSTx"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceStatsNdpNSRx"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceStatsNdpNATx"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceStatsNdpNARx"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceStatsNdpRATx"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceStatsNdpRARx"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceStatsNdpRSTx"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceStatsNdpRSRx"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceHistoryIndex"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceHistoryTime"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceHistoryValid"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceHistoryAction"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceHistoryDhcpTx"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceHistoryDhcpRx"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceHistoryIcmpTx"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceHistoryIcmpRx"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceHistoryArpReqTx"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceHistoryArpReqRx"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceHistoryArpReplyTx"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceHistoryArpReplyRx"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceHistoryDhcpV6Tx"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceHistoryDhcpV6Rx"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceHistoryIcmpV6WONdpTx"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceHistoryIcmpV6WONdpRx"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceHistoryNdpNSTx"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceHistoryNdpNSRx"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceHistoryNdpNATx"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceHistoryNdpNARx"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceHistoryNdpRATx"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceHistoryNdpRARx"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceHistoryNdpRSTx"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceHistoryNdpRSRx"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceThresholdIndex"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceThresholdInterval"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceThresholdVariable"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceThresholdValueLo"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceThresholdValueHi"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceThresholdMonValue"),
        ("F3-L3-MIB", "f3L3AclRuleStatsIndex"),
        ("F3-L3-MIB", "f3L3AclRuleStatsIntervalType"),
        ("F3-L3-MIB", "f3L3AclRuleStatsValid"),
        ("F3-L3-MIB", "f3L3AclRuleStatsAction"),
        ("F3-L3-MIB", "f3L3AclRuleStatsRuleMatch"),
        ("F3-L3-MIB", "f3L3AclRuleHistoryIndex"),
        ("F3-L3-MIB", "f3L3AclRuleHistoryTime"),
        ("F3-L3-MIB", "f3L3AclRuleHistoryValid"),
        ("F3-L3-MIB", "f3L3AclRuleHistoryAction"),
        ("F3-L3-MIB", "f3L3AclRuleHistoryRuleMatch"),
        ("F3-L3-MIB", "f3L3AclRuleThresholdIndex"),
        ("F3-L3-MIB", "f3L3AclRuleThresholdInterval"),
        ("F3-L3-MIB", "f3L3AclRuleThresholdVariable"),
        ("F3-L3-MIB", "f3L3AclRuleThresholdValueLo"),
        ("F3-L3-MIB", "f3L3AclRuleThresholdValueHi"),
        ("F3-L3-MIB", "f3L3AclRuleThresholdMonValue"),
        ("F3-L3-MIB", "f3L2A2NAclRuleStatsIndex"),
        ("F3-L3-MIB", "f3L2A2NAclRuleStatsIntervalType"),
        ("F3-L3-MIB", "f3L2A2NAclRuleStatsValid"),
        ("F3-L3-MIB", "f3L2A2NAclRuleStatsAction"),
        ("F3-L3-MIB", "f3L2A2NAclRuleStatsRuleMatch"),
        ("F3-L3-MIB", "f3L2A2NAclRuleHistoryIndex"),
        ("F3-L3-MIB", "f3L2A2NAclRuleHistoryTime"),
        ("F3-L3-MIB", "f3L2A2NAclRuleHistoryValid"),
        ("F3-L3-MIB", "f3L2A2NAclRuleHistoryAction"),
        ("F3-L3-MIB", "f3L2A2NAclRuleHistoryRuleMatch"),
        ("F3-L3-MIB", "f3L2A2NAclRuleThresholdIndex"),
        ("F3-L3-MIB", "f3L2A2NAclRuleThresholdInterval"),
        ("F3-L3-MIB", "f3L2A2NAclRuleThresholdVariable"),
        ("F3-L3-MIB", "f3L2A2NAclRuleThresholdValueLo"),
        ("F3-L3-MIB", "f3L2A2NAclRuleThresholdValueHi"),
        ("F3-L3-MIB", "f3L2A2NAclRuleThresholdMonValue"),
        ("F3-L3-MIB", "f3L2N2AAclRuleStatsIndex"),
        ("F3-L3-MIB", "f3L2N2AAclRuleStatsIntervalType"),
        ("F3-L3-MIB", "f3L2N2AAclRuleStatsValid"),
        ("F3-L3-MIB", "f3L2N2AAclRuleStatsAction"),
        ("F3-L3-MIB", "f3L2N2AAclRuleStatsRuleMatch"),
        ("F3-L3-MIB", "f3L2N2AAclRuleHistoryIndex"),
        ("F3-L3-MIB", "f3L2N2AAclRuleHistoryTime"),
        ("F3-L3-MIB", "f3L2N2AAclRuleHistoryValid"),
        ("F3-L3-MIB", "f3L2N2AAclRuleHistoryAction"),
        ("F3-L3-MIB", "f3L2N2AAclRuleHistoryRuleMatch"),
        ("F3-L3-MIB", "f3L2N2AAclRuleThresholdIndex"),
        ("F3-L3-MIB", "f3L2N2AAclRuleThresholdInterval"),
        ("F3-L3-MIB", "f3L2N2AAclRuleThresholdVariable"),
        ("F3-L3-MIB", "f3L2N2AAclRuleThresholdValueLo"),
        ("F3-L3-MIB", "f3L2N2AAclRuleThresholdValueHi"),
        ("F3-L3-MIB", "f3L2N2AAclRuleThresholdMonValue"),
        ("F3-L3-MIB", "f3L3QosPolicerStatsIndex"),
        ("F3-L3-MIB", "f3L3QosPolicerStatsIntervalType"),
        ("F3-L3-MIB", "f3L3QosPolicerStatsValid"),
        ("F3-L3-MIB", "f3L3QosPolicerStatsAction"),
        ("F3-L3-MIB", "f3L3QosPolicerStatsFMG"),
        ("F3-L3-MIB", "f3L3QosPolicerStatsFMY"),
        ("F3-L3-MIB", "f3L3QosPolicerStatsFMYD"),
        ("F3-L3-MIB", "f3L3QosPolicerStatsFMRD"),
        ("F3-L3-MIB", "f3L3QosPolicerStatsBytesIn"),
        ("F3-L3-MIB", "f3L3QosPolicerStatsBytesOut"),
        ("F3-L3-MIB", "f3L3QosPolicerStatsABR"),
        ("F3-L3-MIB", "f3L3QosPolicerHistoryIndex"),
        ("F3-L3-MIB", "f3L3QosPolicerHistoryTime"),
        ("F3-L3-MIB", "f3L3QosPolicerHistoryValid"),
        ("F3-L3-MIB", "f3L3QosPolicerHistoryAction"),
        ("F3-L3-MIB", "f3L3QosPolicerHistoryFMG"),
        ("F3-L3-MIB", "f3L3QosPolicerHistoryFMY"),
        ("F3-L3-MIB", "f3L3QosPolicerHistoryFMYD"),
        ("F3-L3-MIB", "f3L3QosPolicerHistoryFMRD"),
        ("F3-L3-MIB", "f3L3QosPolicerHistoryBytesIn"),
        ("F3-L3-MIB", "f3L3QosPolicerHistoryBytesOut"),
        ("F3-L3-MIB", "f3L3QosPolicerHistoryABR"),
        ("F3-L3-MIB", "f3L3QosPolicerThresholdIndex"),
        ("F3-L3-MIB", "f3L3QosPolicerThresholdInterval"),
        ("F3-L3-MIB", "f3L3QosPolicerThresholdVariable"),
        ("F3-L3-MIB", "f3L3QosPolicerThresholdValueLo"),
        ("F3-L3-MIB", "f3L3QosPolicerThresholdValueHi"),
        ("F3-L3-MIB", "f3L3QosPolicerThresholdMonValue"),
        ("F3-L3-MIB", "f3L3QosShaperStatsIndex"),
        ("F3-L3-MIB", "f3L3QosShaperStatsIntervalType"),
        ("F3-L3-MIB", "f3L3QosShaperStatsValid"),
        ("F3-L3-MIB", "f3L3QosShaperStatsAction"),
        ("F3-L3-MIB", "f3L3QosShaperStatsBT"),
        ("F3-L3-MIB", "f3L3QosShaperStatsBTD"),
        ("F3-L3-MIB", "f3L3QosShaperStatsFD"),
        ("F3-L3-MIB", "f3L3QosShaperStatsFTD"),
        ("F3-L3-MIB", "f3L3QosShaperStatsBR"),
        ("F3-L3-MIB", "f3L3QosShaperStatsFR"),
        ("F3-L3-MIB", "f3L3QosShaperStatsABRRL"),
        ("F3-L3-MIB", "f3L3QosShaperStatsBREDD"),
        ("F3-L3-MIB", "f3L3QosShaperStatsFREDD"),
        ("F3-L3-MIB", "f3L3QosShaperHistoryIndex"),
        ("F3-L3-MIB", "f3L3QosShaperHistoryTime"),
        ("F3-L3-MIB", "f3L3QosShaperHistoryValid"),
        ("F3-L3-MIB", "f3L3QosShaperHistoryAction"),
        ("F3-L3-MIB", "f3L3QosShaperHistoryBT"),
        ("F3-L3-MIB", "f3L3QosShaperHistoryBTD"),
        ("F3-L3-MIB", "f3L3QosShaperHistoryFD"),
        ("F3-L3-MIB", "f3L3QosShaperHistoryFTD"),
        ("F3-L3-MIB", "f3L3QosShaperHistoryBR"),
        ("F3-L3-MIB", "f3L3QosShaperHistoryFR"),
        ("F3-L3-MIB", "f3L3QosShaperHistoryABRRL"),
        ("F3-L3-MIB", "f3L3QosShaperHistoryBREDD"),
        ("F3-L3-MIB", "f3L3QosShaperHistoryFREDD"),
        ("F3-L3-MIB", "f3L3QosShaperThresholdIndex"),
        ("F3-L3-MIB", "f3L3QosShaperThresholdInterval"),
        ("F3-L3-MIB", "f3L3QosShaperThresholdVariable"),
        ("F3-L3-MIB", "f3L3QosShaperThresholdValueLo"),
        ("F3-L3-MIB", "f3L3QosShaperThresholdValueHi"),
        ("F3-L3-MIB", "f3L3QosShaperThresholdMonValue"),
        ("F3-L3-MIB", "cmL3FlowPointStatsIndex"),
        ("F3-L3-MIB", "cmL3FlowPointStatsIntervalType"),
        ("F3-L3-MIB", "cmL3FlowPointStatsValid"),
        ("F3-L3-MIB", "cmL3FlowPointStatsAction"),
        ("F3-L3-MIB", "cmL3FlowPointStatsFMG"),
        ("F3-L3-MIB", "cmL3FlowPointStatsFMY"),
        ("F3-L3-MIB", "cmL3FlowPointStatsFMRD"),
        ("F3-L3-MIB", "cmL3FlowPointStatsFTD"),
        ("F3-L3-MIB", "cmL3FlowPointStatsFragmentedDropAcl"),
        ("F3-L3-MIB", "cmL3FlowPointStatsAclRuleDrop"),
        ("F3-L3-MIB", "cmL3FlowPointStatsTtlEqual1Drop"),
        ("F3-L3-MIB", "cmL3FlowPointStatsFrameTx"),
        ("F3-L3-MIB", "cmL3FlowPointStatsFrameRx"),
        ("F3-L3-MIB", "cmL3FlowPointStatsNoRouteDrop"),
        ("F3-L3-MIB", "cmL3FlowPointStatsAclDropNoMatch"),
        ("F3-L3-MIB", "cmL3FlowPointHistoryIndex"),
        ("F3-L3-MIB", "cmL3FlowPointHistoryTime"),
        ("F3-L3-MIB", "cmL3FlowPointHistoryValid"),
        ("F3-L3-MIB", "cmL3FlowPointHistoryAction"),
        ("F3-L3-MIB", "cmL3FlowPointHistoryFMG"),
        ("F3-L3-MIB", "cmL3FlowPointHistoryFMY"),
        ("F3-L3-MIB", "cmL3FlowPointHistoryFMRD"),
        ("F3-L3-MIB", "cmL3FlowPointHistoryFTD"),
        ("F3-L3-MIB", "cmL3FlowPointHistoryFragmentedDropAcl"),
        ("F3-L3-MIB", "cmL3FlowPointHistoryAclRuleDrop"),
        ("F3-L3-MIB", "cmL3FlowPointHistoryTtlEqual1Drop"),
        ("F3-L3-MIB", "cmL3FlowPointHistoryFrameTx"),
        ("F3-L3-MIB", "cmL3FlowPointHistoryFrameRx"),
        ("F3-L3-MIB", "cmL3FlowPointHistoryNoRouteDrop"),
        ("F3-L3-MIB", "cmL3FlowPointHistoryAclDropNoMatch"),
        ("F3-L3-MIB", "cmL3FlowPointThresholdIndex"),
        ("F3-L3-MIB", "cmL3FlowPointThresholdInterval"),
        ("F3-L3-MIB", "cmL3FlowPointThresholdVariable"),
        ("F3-L3-MIB", "cmL3FlowPointThresholdValueLo"),
        ("F3-L3-MIB", "cmL3FlowPointThresholdValueHi"),
        ("F3-L3-MIB", "cmL3FlowPointThresholdMonValue"),
        ("F3-L3-MIB", "cmL3QosPolicerStatsIndex"),
        ("F3-L3-MIB", "cmL3QosPolicerStatsIntervalType"),
        ("F3-L3-MIB", "cmL3QosPolicerStatsValid"),
        ("F3-L3-MIB", "cmL3QosPolicerStatsAction"),
        ("F3-L3-MIB", "cmL3QosPolicerStatsFMG"),
        ("F3-L3-MIB", "cmL3QosPolicerStatsFMY"),
        ("F3-L3-MIB", "cmL3QosPolicerStatsFMYD"),
        ("F3-L3-MIB", "cmL3QosPolicerStatsFMRD"),
        ("F3-L3-MIB", "cmL3QosPolicerStatsBytesIn"),
        ("F3-L3-MIB", "cmL3QosPolicerStatsBytesOut"),
        ("F3-L3-MIB", "cmL3QosPolicerStatsABR"),
        ("F3-L3-MIB", "cmL3QosPolicerHistoryIndex"),
        ("F3-L3-MIB", "cmL3QosPolicerHistoryTime"),
        ("F3-L3-MIB", "cmL3QosPolicerHistoryValid"),
        ("F3-L3-MIB", "cmL3QosPolicerHistoryAction"),
        ("F3-L3-MIB", "cmL3QosPolicerHistoryFMG"),
        ("F3-L3-MIB", "cmL3QosPolicerHistoryFMY"),
        ("F3-L3-MIB", "cmL3QosPolicerHistoryFMYD"),
        ("F3-L3-MIB", "cmL3QosPolicerHistoryFMRD"),
        ("F3-L3-MIB", "cmL3QosPolicerHistoryBytesIn"),
        ("F3-L3-MIB", "cmL3QosPolicerHistoryBytesOut"),
        ("F3-L3-MIB", "cmL3QosPolicerHistoryABR"),
        ("F3-L3-MIB", "cmL3QosPolicerThresholdIndex"),
        ("F3-L3-MIB", "cmL3QosPolicerThresholdInterval"),
        ("F3-L3-MIB", "cmL3QosPolicerThresholdVariable"),
        ("F3-L3-MIB", "cmL3QosPolicerThresholdValueLo"),
        ("F3-L3-MIB", "cmL3QosPolicerThresholdValueHi"),
        ("F3-L3-MIB", "cmL3QosPolicerThresholdMonValue"),
        ("F3-L3-MIB", "cmL3QosShaperStatsIndex"),
        ("F3-L3-MIB", "cmL3QosShaperStatsIntervalType"),
        ("F3-L3-MIB", "cmL3QosShaperStatsValid"),
        ("F3-L3-MIB", "cmL3QosShaperStatsAction"),
        ("F3-L3-MIB", "cmL3QosShaperStatsBT"),
        ("F3-L3-MIB", "cmL3QosShaperStatsBTD"),
        ("F3-L3-MIB", "cmL3QosShaperStatsFD"),
        ("F3-L3-MIB", "cmL3QosShaperStatsFTD"),
        ("F3-L3-MIB", "cmL3QosShaperStatsBR"),
        ("F3-L3-MIB", "cmL3QosShaperStatsFR"),
        ("F3-L3-MIB", "cmL3QosShaperStatsABRRL"),
        ("F3-L3-MIB", "cmL3QosShaperStatsABRRLR"),
        ("F3-L3-MIB", "cmL3QosShaperStatsBREDD"),
        ("F3-L3-MIB", "cmL3QosShaperStatsFREDD"),
        ("F3-L3-MIB", "cmL3QosShaperHistoryFTD"),
        ("F3-L3-MIB", "cmL3QosShaperHistoryBR"),
        ("F3-L3-MIB", "cmL3QosShaperHistoryFR"),
        ("F3-L3-MIB", "cmL3QosShaperHistoryABRRL"),
        ("F3-L3-MIB", "cmL3QosShaperHistoryABRRLR"),
        ("F3-L3-MIB", "cmL3QosShaperHistoryBREDD"),
        ("F3-L3-MIB", "cmL3QosShaperHistoryFREDD"),
        ("F3-L3-MIB", "cmL3QosShaperThresholdIndex"),
        ("F3-L3-MIB", "cmL3QosShaperThresholdInterval"),
        ("F3-L3-MIB", "cmL3QosShaperThresholdVariable"),
        ("F3-L3-MIB", "cmL3QosShaperThresholdValueLo"),
        ("F3-L3-MIB", "cmL3QosShaperThresholdValueHi"),
        ("F3-L3-MIB", "cmL3QosShaperThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3L3PerfGroup.setStatus("current")

f3L3TrafficOspfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 4, 2, 3)
)
f3L3TrafficOspfGroup.setObjects(
      *(("F3-L3-MIB", "f3VrfOspfRouterIndex"),
        ("F3-L3-MIB", "f3VrfOspfRouterAdminState"),
        ("F3-L3-MIB", "f3VrfOspfRouterSecondaryState"),
        ("F3-L3-MIB", "f3VrfOspfRouterOperationalState"),
        ("F3-L3-MIB", "f3VrfOspfRouterId"),
        ("F3-L3-MIB", "f3VrfOspfRouterDescription"),
        ("F3-L3-MIB", "f3VrfOspfRouterBgpRoutesRedistributeToOspf"),
        ("F3-L3-MIB", "f3VrfOspfRouterBgpRoutesMetricType"),
        ("F3-L3-MIB", "f3VrfOspfRouterBgpRoutesMetric"),
        ("F3-L3-MIB", "f3VrfOspfRouterStaticRoutesRedistributeToOspf"),
        ("F3-L3-MIB", "f3VrfOspfRouterStaticRoutesMetricType"),
        ("F3-L3-MIB", "f3VrfOspfRouterStaticRoutesMetric"),
        ("F3-L3-MIB", "f3VrfOspfRouterConnectedRoutesRedistributeToOspf"),
        ("F3-L3-MIB", "f3VrfOspfRouterConnectedRoutesMetricType"),
        ("F3-L3-MIB", "f3VrfOspfRouterConnectedRoutesMetric"),
        ("F3-L3-MIB", "f3VrfOspfRouterDhcpRoutesRedistributeToOspf"),
        ("F3-L3-MIB", "f3VrfOspfRouterDhcpRoutesMetricType"),
        ("F3-L3-MIB", "f3VrfOspfRouterDhcpRoutesMetric"),
        ("F3-L3-MIB", "f3VrfOspfRouterStorageType"),
        ("F3-L3-MIB", "f3VrfOspfRouterRowStatus"),
        ("F3-L3-MIB", "f3VrfOspfRouterAction"),
        ("F3-L3-MIB", "f3VrfOspfRouterVersion"),
        ("F3-L3-MIB", "f3VrfOspfRouterAdministrativeDistance"),
        ("F3-L3-MIB", "f3VrfOspfRouterSlaacRoutesRedistributeToOspf"),
        ("F3-L3-MIB", "f3VrfOspfRouterSlaacRoutesMetricType"),
        ("F3-L3-MIB", "f3VrfOspfRouterSlaacRoutesMetric"),
        ("F3-L3-MIB", "f3VrfOspfRouterEcmpMaximumPaths"),
        ("F3-L3-MIB", "f3VrfOspfRouterSrControl"),
        ("F3-L3-MIB", "f3VrfOspfRouterConvergenceTime"),
        ("F3-L3-MIB", "f3L3TrafficOspfAreaIndex"),
        ("F3-L3-MIB", "f3L3TrafficOspfAreaType"),
        ("F3-L3-MIB", "f3L3TrafficOspfAreaDefaultCost"),
        ("F3-L3-MIB", "f3L3TrafficOspfAreaId"),
        ("F3-L3-MIB", "f3L3TrafficOspfAreaStorageType"),
        ("F3-L3-MIB", "f3L3TrafficOspfAreaRowStatus"),
        ("F3-L3-MIB", "f3L3TrafficOspfAreaAuthType"),
        ("F3-L3-MIB", "f3L3TrafficOspfAreaSimpleAuthKey"),
        ("F3-L3-MIB", "f3L3TrafficOspfAreaCryptoKeyId"),
        ("F3-L3-MIB", "f3L3TrafficOspfAreaIfMemberObject"),
        ("F3-L3-MIB", "f3L3TrafficOspfAreaIfMemberStorageType"),
        ("F3-L3-MIB", "f3L3TrafficOspfAreaIfMemberRowStatus"),
        ("F3-L3-MIB", "f3VrfLoopbackInterfaceIndex"),
        ("F3-L3-MIB", "f3VrfLoopbackInterfaceName"),
        ("F3-L3-MIB", "f3VrfLoopbackInterfaceIpAddress"),
        ("F3-L3-MIB", "f3VrfLoopbackInterfaceNetMask"),
        ("F3-L3-MIB", "f3VrfLoopbackInterfaceCIRLo"),
        ("F3-L3-MIB", "f3VrfLoopbackInterfaceCIRHi"),
        ("F3-L3-MIB", "f3VrfLoopbackInterfaceStorageType"),
        ("F3-L3-MIB", "f3VrfLoopbackInterfaceRowStatus"),
        ("F3-L3-MIB", "f3VrfLoopbackInterfaceIpMode"),
        ("F3-L3-MIB", "f3VrfLoopbackInterfaceIpv6Address"),
        ("F3-L3-MIB", "f3VrfLoopbackInterfaceIpv6AddrPrefixLen"),
        ("F3-L3-MIB", "f3L3TrafficOspfAsLsDbType"),
        ("F3-L3-MIB", "f3L3TrafficOspfAsLsDbId"),
        ("F3-L3-MIB", "f3L3TrafficOspfAsLsDbRouterId"),
        ("F3-L3-MIB", "f3L3TrafficOspfAsLsDbChecksum"),
        ("F3-L3-MIB", "f3L3TrafficOspfAsLsDbSeqNum"),
        ("F3-L3-MIB", "f3L3TrafficOspfAsLsDbAge"),
        ("F3-L3-MIB", "f3L3TrafficOspfLsDbType"),
        ("F3-L3-MIB", "f3L3TrafficOspfLsDbId"),
        ("F3-L3-MIB", "f3L3TrafficOspfLsDbRouterId"),
        ("F3-L3-MIB", "f3L3TrafficOspfLsDbAreaId"),
        ("F3-L3-MIB", "f3L3TrafficOspfLsDbChecksum"),
        ("F3-L3-MIB", "f3L3TrafficOspfLsDbSeqNum"),
        ("F3-L3-MIB", "f3L3TrafficOspfLsDbAge"),
        ("F3-L3-MIB", "f3L3TrafficOspfNeighborIpAddress"),
        ("F3-L3-MIB", "f3L3TrafficOspfNeighborInterface"),
        ("F3-L3-MIB", "f3L3TrafficOspfNeighborRouterId"),
        ("F3-L3-MIB", "f3L3TrafficOspfNeighborState"),
        ("F3-L3-MIB", "f3L3TrafficOspfNeighborRole"),
        ("F3-L3-MIB", "f3L3TrafficOspfNeighborPriority"),
        ("F3-L3-MIB", "f3L3TrafficOspfNeighborDeadTime"),
        ("F3-L3-MIB", "f3L3TrafficOspfNeighborLocalInterfaceName"),
        ("F3-L3-MIB", "f3L3TrafficIPIfOspfAreaId"),
        ("F3-L3-MIB", "f3L3TrafficIPIfOspfCost"),
        ("F3-L3-MIB", "f3L3TrafficIPIfOspfIfType"),
        ("F3-L3-MIB", "f3L3TrafficIPIfOspfRtrPriority"),
        ("F3-L3-MIB", "f3L3TrafficIPIfOspfHelloInterval"),
        ("F3-L3-MIB", "f3L3TrafficIPIfOspfDeadInterval"),
        ("F3-L3-MIB", "f3L3TrafficIPIfOspfTransmitDelay"),
        ("F3-L3-MIB", "f3L3TrafficIPIfOspfRetransmitInterval"),
        ("F3-L3-MIB", "f3L3TrafficIPIfOspfState"),
        ("F3-L3-MIB", "f3L3TrafficIPIfOspfDesignatedRouterId"),
        ("F3-L3-MIB", "f3L3TrafficIPIfOspfBackupDesignatedRouterId"),
        ("F3-L3-MIB", "f3L3TrafficIPIfOspfAuthType"),
        ("F3-L3-MIB", "f3L3TrafficIPIfOspfSimpleAuthKey"),
        ("F3-L3-MIB", "f3L3TrafficIPIfospfCryptoKeyId"),
        ("F3-L3-MIB", "f3L3TrafficOspfInterfaceIndex"),
        ("F3-L3-MIB", "f3L3TrafficOspfInterfaceOspfCost"),
        ("F3-L3-MIB", "f3L3TrafficOspfInterfaceType"),
        ("F3-L3-MIB", "f3L3TrafficOspfInterfaceOspfRtrPriority"),
        ("F3-L3-MIB", "f3L3TrafficOspfInterfaceOspfHelloInterval"),
        ("F3-L3-MIB", "f3L3TrafficOspfInterfaceOspfDeadInterval"),
        ("F3-L3-MIB", "f3L3TrafficOspfInterfaceOspfTransmitDelay"),
        ("F3-L3-MIB", "f3L3TrafficOspfInterfaceOspfRetransmitInterval"),
        ("F3-L3-MIB", "f3L3TrafficOspfInterfaceState"),
        ("F3-L3-MIB", "f3L3TrafficOspfInterfaceOspfDesignatedRouterId"),
        ("F3-L3-MIB", "f3L3TrafficOspfInterfaceOspfBackupDesignatedRouterId"),
        ("F3-L3-MIB", "f3L3TrafficOspfInterfaceOspfAuthType"),
        ("F3-L3-MIB", "f3L3TrafficOspfInterfaceOspfSimpleAuthKey"),
        ("F3-L3-MIB", "f3L3TrafficOspfInterfaceOspfCryptoKeyId"),
        ("F3-L3-MIB", "f3L3TrafficOspfInterfaceOspfInstanceId"),
        ("F3-L3-MIB", "f3L3TrafficOspfInterfaceId"),
        ("F3-L3-MIB", "f3L3TrafficOspfInterfaceLinkLsaSuppression"),
        ("F3-L3-MIB", "f3L3TrafficOspfInterfacePassiveControl"),
        ("F3-L3-MIB", "f3L3TrafficOspfInterfaceAssociatedIpInterface"),
        ("F3-L3-MIB", "f3L3TrafficOspfInterfaceStorageType"),
        ("F3-L3-MIB", "f3L3TrafficOspfInterfaceRowStatus"),
        ("F3-L3-MIB", "f3L3TrafficOspfInterfaceTilfaControl"),
        ("F3-L3-MIB", "f3L3TrafficOspfInterfaceTilfaProtectionType"),
        ("F3-L3-MIB", "f3L3TrafficOspfV3NeighborRouterId"),
        ("F3-L3-MIB", "f3L3TrafficOspfV3NeighborInterfaceId"),
        ("F3-L3-MIB", "f3L3TrafficOspfV3NeighborPriority"),
        ("F3-L3-MIB", "f3L3TrafficOspfV3NeighborDeadTime"),
        ("F3-L3-MIB", "f3L3TrafficOspfV3NeighborLocalInterfaceName"),
        ("F3-L3-MIB", "f3L3TrafficOspfV3NeighborState"),
        ("F3-L3-MIB", "f3L3TrafficOspfV3NeighborRole"),
        ("F3-L3-MIB", "f3L3TrafficOspfV3NeighborIpAddress"),
        ("F3-L3-MIB", "f3L3TrafficOspfLinkLsDbInterfaceId"),
        ("F3-L3-MIB", "f3L3TrafficOspfLinkLsDbInterface"),
        ("F3-L3-MIB", "f3L3TrafficOspfLinkLsDbType"),
        ("F3-L3-MIB", "f3L3TrafficOspfLinkLsDbId"),
        ("F3-L3-MIB", "f3L3TrafficOspfLinkLsDbAdvRouterId"),
        ("F3-L3-MIB", "f3L3TrafficOspfLinkLsDbAreaId"),
        ("F3-L3-MIB", "f3L3TrafficOspfLinkLsDbChecksum"),
        ("F3-L3-MIB", "f3L3TrafficOspfLinkLsDbSeqNum"),
        ("F3-L3-MIB", "f3L3TrafficOspfLinkLsDbAge"),
        ("F3-L3-MIB", "f3L3TrafficOspfLinkLsDbRtrPriority"),
        ("F3-L3-MIB", "f3L3TrafficOspfLinkLsDbLinkLocalAddress"),
        ("F3-L3-MIB", "f3L3TrafficOspfLinkLsDbPrefixList"))
)
if mibBuilder.loadTexts:
    f3L3TrafficOspfGroup.setStatus("current")

f3L3TrafficIPv6Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 4, 2, 4)
)
f3L3TrafficIPv6Group.setObjects(
      *(("F3-L3-MIB", "f3L3TrafficIPv6IfIndex"),
        ("F3-L3-MIB", "f3L3TrafficIPv6IfName"),
        ("F3-L3-MIB", "f3L3TrafficIPv6IfAdminState"),
        ("F3-L3-MIB", "f3L3TrafficIPv6IfSecondaryState"),
        ("F3-L3-MIB", "f3L3TrafficIPv6IfOperationalState"),
        ("F3-L3-MIB", "f3L3TrafficIPv6IfType"),
        ("F3-L3-MIB", "f3L3TrafficIPv6IfLinkLocalAddr"),
        ("F3-L3-MIB", "f3L3TrafficIPv6IfLinkLocalAddrMode"),
        ("F3-L3-MIB", "f3L3TrafficIPv6IfMtu"),
        ("F3-L3-MIB", "f3L3TrafficIPv6IfStatelessAddrAutoconfigEnabled"),
        ("F3-L3-MIB", "f3L3TrafficIPv6IfDefaultGateway"),
        ("F3-L3-MIB", "f3L3TrafficIPv6IfIcmpErrorMsgRateLimit"),
        ("F3-L3-MIB", "f3L3TrafficIPv6IfDhcpRole"),
        ("F3-L3-MIB", "f3L3TrafficIPv6IfDhcpEnabled"),
        ("F3-L3-MIB", "f3L3TrafficIPv6IfDhcpRapidCommitControlEnabled"),
        ("F3-L3-MIB", "f3L3TrafficIPv6IfMaxRAInterval"),
        ("F3-L3-MIB", "f3L3TrafficIPv6IfMinRAInterval"),
        ("F3-L3-MIB", "f3L3TrafficIPv6IfRouterLifeTime"),
        ("F3-L3-MIB", "f3L3TrafficIPv6IfReachableTime"),
        ("F3-L3-MIB", "f3L3TrafficIPv6IfRaDhcpMoreConfigEnabled"),
        ("F3-L3-MIB", "f3L3TrafficIPv6IfRaManagedAddressConfigEnabled"),
        ("F3-L3-MIB", "f3L3TrafficIPv6IfRaRDNSSOptionEnabled"),
        ("F3-L3-MIB", "f3L3TrafficIPv6IfRaRDNSSLifeTime"),
        ("F3-L3-MIB", "f3L3TrafficIPv6IfRaDNSSList"),
        ("F3-L3-MIB", "f3L3TrafficIPv6IfRaDefaultRouterPreference"),
        ("F3-L3-MIB", "f3L3TrafficIPv6IfDupAddrDetectControl"),
        ("F3-L3-MIB", "f3L3TrafficIPv6IfDupAddrDetectTransmits"),
        ("F3-L3-MIB", "f3L3TrafficIPv6IfDupAddrDetectRetransTimer"),
        ("F3-L3-MIB", "f3L3TrafficIPv6IfStorageType"),
        ("F3-L3-MIB", "f3L3TrafficIPv6IfRowStatus"),
        ("F3-L3-MIB", "f3L3TrafficIPv6IfAction"),
        ("F3-L3-MIB", "f3L3TrafficIPv6AddrIndex"),
        ("F3-L3-MIB", "f3L3TrafficIPv6AddrAssignMode"),
        ("F3-L3-MIB", "f3L3TrafficIPv6AddrUnicastAddr"),
        ("F3-L3-MIB", "f3L3TrafficIPv6AddrUnicastAddrPrefixLength"),
        ("F3-L3-MIB", "f3L3TrafficIPv6AddrUnicastAddrAutoGenPrefix"),
        ("F3-L3-MIB", "f3L3TrafficIPv6AddrStorageType"),
        ("F3-L3-MIB", "f3L3TrafficIPv6AddrRowStatus"),
        ("F3-L3-MIB", "f3L3TrafficIPv6PrefixIndex"),
        ("F3-L3-MIB", "f3L3TrafficIPv6PrefixRaPrefixAdvEnabled"),
        ("F3-L3-MIB", "f3L3TrafficIPv6PrefixRaPrefix"),
        ("F3-L3-MIB", "f3L3TrafficIPv6PrefixRaPrefixLength"),
        ("F3-L3-MIB", "f3L3TrafficIPv6PrefixValidLifeTime"),
        ("F3-L3-MIB", "f3L3TrafficIPv6PrefixPreferredLifeTime"),
        ("F3-L3-MIB", "f3L3TrafficIPv6PrefixStorageType"),
        ("F3-L3-MIB", "f3L3TrafficIPv6PrefixRowStatus"),
        ("F3-L3-MIB", "f3L3TrafficIPv6NdpIPv6Addr"),
        ("F3-L3-MIB", "f3L3TrafficIPv6NdpInterface"),
        ("F3-L3-MIB", "f3L3TrafficIPv6NdpMacAddress"),
        ("F3-L3-MIB", "f3L3TrafficIPv6NdpType"),
        ("F3-L3-MIB", "f3L3TrafficIPv6NdpReachabilityState"),
        ("F3-L3-MIB", "f3L3TrafficIPv6NdpAge"),
        ("F3-L3-MIB", "f3L3TrafficIPv6NdpStorageType"),
        ("F3-L3-MIB", "f3L3TrafficIPv6NdpRowStatus"),
        ("F3-L3-MIB", "f3L3TrafficIpv6RouteDest"),
        ("F3-L3-MIB", "f3L3TrafficIpv6RoutePrefixLength"),
        ("F3-L3-MIB", "f3L3TrafficIpv6RouteGateway"),
        ("F3-L3-MIB", "f3L3TrafficIpv6RouteInterface"),
        ("F3-L3-MIB", "f3L3TrafficIpv6RouteMetric"),
        ("F3-L3-MIB", "f3L3TrafficIpv6RouteType"),
        ("F3-L3-MIB", "f3L3TrafficIpv6RouteAdvertise"),
        ("F3-L3-MIB", "f3L3TrafficIpv6RouteStatus"),
        ("F3-L3-MIB", "f3L3TrafficIpv6RouteFlags"),
        ("F3-L3-MIB", "f3L3TrafficIpv6RouteOrigin"),
        ("F3-L3-MIB", "f3L3TrafficIpv6RouteStorageType"),
        ("F3-L3-MIB", "f3L3TrafficIpv6RouteRowStatus"),
        ("F3-L3-MIB", "f3DhcpV6RelayAgentIndex"),
        ("F3-L3-MIB", "f3DhcpV6RelayAgentAlias"),
        ("F3-L3-MIB", "f3DhcpV6RelayAgentAdminState"),
        ("F3-L3-MIB", "f3DhcpV6RelayAgentSecondaryState"),
        ("F3-L3-MIB", "f3DhcpV6RelayAgentOperationalState"),
        ("F3-L3-MIB", "f3DhcpV6RelayAgentServerIpAddress"),
        ("F3-L3-MIB", "f3DhcpV6RelayAgentServerIpInteface"),
        ("F3-L3-MIB", "f3DhcpV6RelayAgentStorageType"),
        ("F3-L3-MIB", "f3DhcpV6RelayAgentRowStatus"),
        ("F3-L3-MIB", "f3DhcpV6RelayAgentClientTrafficIpIfMemberObject"),
        ("F3-L3-MIB", "f3DhcpV6RelayAgentClientTrafficIpIfMemberStorageType"),
        ("F3-L3-MIB", "f3DhcpV6RelayAgentClientTrafficIpIfMemberRowStatus"),
        ("F3-L3-MIB", "f3L3TrafficIPInterfaceIPv6AddressIndex"),
        ("F3-L3-MIB", "f3L3TrafficIPInterfaceIPv6AddressAssignMode"),
        ("F3-L3-MIB", "f3L3TrafficIPInterfaceIPv6AddressUnicastAddr"),
        ("F3-L3-MIB", "f3L3TrafficIPInterfaceIPv6AddressUnicastAddrPrefixLength"),
        ("F3-L3-MIB", "f3L3TrafficIPInterfaceIPv6AddressUnicastAddrAutoGenPrefix"),
        ("F3-L3-MIB", "f3L3TrafficIPInterfaceIPv6AddressStorageType"),
        ("F3-L3-MIB", "f3L3TrafficIPInterfaceIPv6AddressRowStatus"),
        ("F3-L3-MIB", "f3L3TrafficIPInterfaceRAPrefixIndex"),
        ("F3-L3-MIB", "f3L3TrafficIPInterfaceRAPrefixAdvertiseEnabled"),
        ("F3-L3-MIB", "f3L3TrafficIPInterfaceRAPrefix"),
        ("F3-L3-MIB", "f3L3TrafficIPInterfaceRAPrefixLength"),
        ("F3-L3-MIB", "f3L3TrafficIPInterfaceRAPrefixValidLifeTime"),
        ("F3-L3-MIB", "f3L3TrafficIPInterfaceRAPrefixPreferredLifeTime"),
        ("F3-L3-MIB", "f3L3TrafficIPInterfaceRAPrefixStorageType"),
        ("F3-L3-MIB", "f3L3TrafficIPInterfaceRAPrefixRowStatus"),
        ("F3-L3-MIB", "f3L3TrafficIPInterfaceNdpIPv6Addr"),
        ("F3-L3-MIB", "f3L3TrafficIPInterfaceNdpInterface"),
        ("F3-L3-MIB", "f3L3TrafficIPInterfaceNdpMacAddress"),
        ("F3-L3-MIB", "f3L3TrafficIPInterfaceNdpType"),
        ("F3-L3-MIB", "f3L3TrafficIPInterfaceNdpReachabilityState"),
        ("F3-L3-MIB", "f3L3TrafficIPInterfaceNdpAge"),
        ("F3-L3-MIB", "f3L3TrafficIPInterfaceNdpStorageType"),
        ("F3-L3-MIB", "f3L3TrafficIPInterfaceNdpRowStatus"))
)
if mibBuilder.loadTexts:
    f3L3TrafficIPv6Group.setStatus("current")

f3L3TrafficBgpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 4, 2, 5)
)
f3L3TrafficBgpGroup.setObjects(
      *(("F3-L3-MIB", "f3L3TrafficBgpRouterIndex"),
        ("F3-L3-MIB", "f3L3TrafficBgpRouterAdminState"),
        ("F3-L3-MIB", "f3L3TrafficBgpRouterSecondaryState"),
        ("F3-L3-MIB", "f3L3TrafficBgpRouterOperationalState"),
        ("F3-L3-MIB", "f3L3TrafficBgpRouterId"),
        ("F3-L3-MIB", "f3L3TrafficBgpRouterAsNumber"),
        ("F3-L3-MIB", "f3L3TrafficBgpRouterConnectedRoutesRedistControl"),
        ("F3-L3-MIB", "f3L3TrafficBgpRouterOspfRoutesRedistControl"),
        ("F3-L3-MIB", "f3L3TrafficBgpRouterStaticRoutesRedistControl"),
        ("F3-L3-MIB", "f3L3TrafficBgpRouterDhcpRoutesRedistControl"),
        ("F3-L3-MIB", "f3L3TrafficBgpRouterStorageType"),
        ("F3-L3-MIB", "f3L3TrafficBgpRouterRowStatus"),
        ("F3-L3-MIB", "f3L3TrafficBgpRouterAction"),
        ("F3-L3-MIB", "f3L3TrafficBgpRouterIBgpAdminDistance"),
        ("F3-L3-MIB", "f3L3TrafficBgpRouterEBgpAdminDistance"),
        ("F3-L3-MIB", "f3L3TrafficBgpRouterEcmpMaximumPaths"),
        ("F3-L3-MIB", "f3L3TrafficBgpRouterRestartTime"),
        ("F3-L3-MIB", "f3L3TrafficBgpRouterStaleRoutesTime"),
        ("F3-L3-MIB", "f3L3TrafficBgpRouteNetwork"),
        ("F3-L3-MIB", "f3L3TrafficBgpRouteMetric"),
        ("F3-L3-MIB", "f3L3TrafficBgpRouteNextHop"),
        ("F3-L3-MIB", "f3L3TrafficBgpRoutePath"),
        ("F3-L3-MIB", "f3L3TrafficBgpPeerIndex"),
        ("F3-L3-MIB", "f3L3TrafficBgpPeerAdminState"),
        ("F3-L3-MIB", "f3L3TrafficBgpPeerSecondaryState"),
        ("F3-L3-MIB", "f3L3TrafficBgpPeerOperationalState"),
        ("F3-L3-MIB", "f3L3TrafficBgpPeerIpv4Addr"),
        ("F3-L3-MIB", "f3L3TrafficBgpPeerAsNumber"),
        ("F3-L3-MIB", "f3L3TrafficBgpPeerDescription"),
        ("F3-L3-MIB", "f3L3TrafficBgpPeerBgpSessionState"),
        ("F3-L3-MIB", "f3L3TrafficBgpPeerHoldTime"),
        ("F3-L3-MIB", "f3L3TrafficBgpPeerStartupHoldTime"),
        ("F3-L3-MIB", "f3L3TrafficBgpPeerKeepAliveTime"),
        ("F3-L3-MIB", "f3L3TrafficBgpPeerConnectRetryTime"),
        ("F3-L3-MIB", "f3L3TrafficBgpPeerUpdateSourceIp"),
        ("F3-L3-MIB", "f3L3TrafficBgpPeerAuthenticationKey"),
        ("F3-L3-MIB", "f3L3TrafficBgpPeerTimeSinceUpTransition"),
        ("F3-L3-MIB", "f3L3TrafficBgpPeerTimeSinceDownTransition"),
        ("F3-L3-MIB", "f3L3TrafficBgpPeerStorageType"),
        ("F3-L3-MIB", "f3L3TrafficBgpPeerRowStatus"),
        ("F3-L3-MIB", "f3L3TrafficBgpPeerIpVersion"),
        ("F3-L3-MIB", "f3L3TrafficBgpPeerIpv6Address"),
        ("F3-L3-MIB", "f3L3TrafficBgpPeerUpdateSourceIpv6"),
        ("F3-L3-MIB", "f3L3TrafficBgpPeerMultihopControl"),
        ("F3-L3-MIB", "f3L3TrafficBgpPeerMultihopTtl"),
        ("F3-L3-MIB", "f3L3TrafficBgpPeerUpdateSourceInterface"),
        ("F3-L3-MIB", "f3L3TrafficBgpPeerUpdateSourceType"),
        ("F3-L3-MIB", "f3L3TrafficBgpPeerLocalPreference"),
        ("F3-L3-MIB", "f3L3TrafficBgpPeerRouteReflectorClient"),
        ("F3-L3-MIB", "f3L3TrafficBgpPeerRouteReflectorClusterId"),
        ("F3-L3-MIB", "f3L3TrafficBgpPeerBgpRouteInboundFilter"),
        ("F3-L3-MIB", "f3L3TrafficBgpPeerBgpRouteOutboundFilter"),
        ("F3-L3-MIB", "f3L3TrafficBgpPeerBgpGracefulRestart"),
        ("F3-L3-MIB", "f3L3TrafficBgpPeerPeerRestartTime"),
        ("F3-L3-MIB", "f3L3TrafficBgpPeerPeerRestarting"),
        ("F3-L3-MIB", "f3L3TrafficBgpPeerAddressFamilyIndex"),
        ("F3-L3-MIB", "f3L3TrafficBgpPeerAddressFamilyName"),
        ("F3-L3-MIB", "f3L3TrafficBgpPeerAddressFamilyRedistOspfRoute"),
        ("F3-L3-MIB", "f3L3TrafficBgpPeerAddressFamilyRedistConnectedRoute"),
        ("F3-L3-MIB", "f3L3TrafficBgpPeerAddressFamilyRedistStaticRoute"),
        ("F3-L3-MIB", "f3L3TrafficBgpPeerAddressFamilyRedistDhcpRoute"),
        ("F3-L3-MIB", "f3L3TrafficBgpPeerAddressFamilyRedistSlaacRoute"),
        ("F3-L3-MIB", "f3L3TrafficBgpPeerAddressFamilySendDefaultRoute"),
        ("F3-L3-MIB", "f3L3TrafficBgpPeerAddressFamilyNextHopType"),
        ("F3-L3-MIB", "f3L3TrafficBgpPeerAddressFamilyNextHopIpv4"),
        ("F3-L3-MIB", "f3L3TrafficBgpPeerAddressFamilyNextHopIpv6"),
        ("F3-L3-MIB", "f3L3TrafficBgpPeerAddressFamilyExtNextHopControl"),
        ("F3-L3-MIB", "f3L3TrafficBgpPeerAddressFamilyStorageType"),
        ("F3-L3-MIB", "f3L3TrafficBgpPeerAddressFamilyRowStatus"),
        ("F3-L3-MIB", "f3L3TrafficBgpRIBRouteIndex"),
        ("F3-L3-MIB", "f3L3TrafficBgpRIBRouteNetwork"),
        ("F3-L3-MIB", "f3L3TrafficBgpRIBRouteNextHop"),
        ("F3-L3-MIB", "f3L3TrafficBgpRIBRouteMetric"),
        ("F3-L3-MIB", "f3L3TrafficBgpRIBRoutePath"),
        ("F3-L3-MIB", "f3L3TrafficBgpRouteV2Network"),
        ("F3-L3-MIB", "f3L3TrafficBgpRouteV2NextHop"),
        ("F3-L3-MIB", "f3L3TrafficBgpRouteV2Metric"),
        ("F3-L3-MIB", "f3L3TrafficBgpRouteV2Path"),
        ("F3-L3-MIB", "f3L3TrafficBgpRouteV2LocalPreference"),
        ("F3-L3-MIB", "f3L3TrafficBgpPeerAddressFamilyAdvPrefix"),
        ("F3-L3-MIB", "f3L3TrafficBgpPeerAddressFamilyAdvPrefixStorageType"),
        ("F3-L3-MIB", "f3L3TrafficBgpPeerAddressFamilyAdvPrefixRowStatus"),
        ("F3-L3-MIB", "f3L3TrafficBgpInRouteIndex"),
        ("F3-L3-MIB", "f3L3TrafficBgpInRouteNetwork"),
        ("F3-L3-MIB", "f3L3TrafficBgpInRouteNextHop"),
        ("F3-L3-MIB", "f3L3TrafficBgpInRouteMetric"),
        ("F3-L3-MIB", "f3L3TrafficBgpInRoutePath"),
        ("F3-L3-MIB", "f3L3TrafficBgpInRouteLocalPreference"))
)
if mibBuilder.loadTexts:
    f3L3TrafficBgpGroup.setStatus("current")


# Notification objects

f3L3FlowPointThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 3, 1)
)
f3L3FlowPointThresholdCrossingAlert.setObjects(
      *(("F3-L3-MIB", "f3L3FlowPointThresholdIndex"),
        ("F3-L3-MIB", "f3L3FlowPointThresholdInterval"),
        ("F3-L3-MIB", "f3L3FlowPointThresholdVariable"),
        ("F3-L3-MIB", "f3L3FlowPointThresholdValueLo"),
        ("F3-L3-MIB", "f3L3FlowPointThresholdValueHi"),
        ("F3-L3-MIB", "f3L3FlowPointThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3L3FlowPointThresholdCrossingAlert.setStatus(
        "current"
    )

f3L3QosPolicerThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 3, 2)
)
f3L3QosPolicerThresholdCrossingAlert.setObjects(
      *(("F3-L3-MIB", "f3L3QosPolicerThresholdIndex"),
        ("F3-L3-MIB", "f3L3QosPolicerThresholdInterval"),
        ("F3-L3-MIB", "f3L3QosPolicerThresholdVariable"),
        ("F3-L3-MIB", "f3L3QosPolicerThresholdValueLo"),
        ("F3-L3-MIB", "f3L3QosPolicerThresholdValueHi"),
        ("F3-L3-MIB", "f3L3QosPolicerThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3L3QosPolicerThresholdCrossingAlert.setStatus(
        "current"
    )

f3L3QosShaperThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 3, 3)
)
f3L3QosShaperThresholdCrossingAlert.setObjects(
      *(("F3-L3-MIB", "f3L3QosShaperThresholdIndex"),
        ("F3-L3-MIB", "f3L3QosShaperThresholdInterval"),
        ("F3-L3-MIB", "f3L3QosShaperThresholdVariable"),
        ("F3-L3-MIB", "f3L3QosShaperThresholdValueLo"),
        ("F3-L3-MIB", "f3L3QosShaperThresholdValueHi"),
        ("F3-L3-MIB", "f3L3QosShaperThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3L3QosShaperThresholdCrossingAlert.setStatus(
        "current"
    )

f3L3TrafficIpInterfaceThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 3, 4)
)
f3L3TrafficIpInterfaceThresholdCrossingAlert.setObjects(
      *(("F3-L3-MIB", "f3L3TrafficIpInterfaceThresholdIndex"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceThresholdInterval"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceThresholdVariable"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceThresholdValueLo"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceThresholdValueHi"),
        ("F3-L3-MIB", "f3L3TrafficIpInterfaceThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3L3TrafficIpInterfaceThresholdCrossingAlert.setStatus(
        "current"
    )

f3L3AclRuleThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 3, 5)
)
f3L3AclRuleThresholdCrossingAlert.setObjects(
      *(("F3-L3-MIB", "f3L3AclRuleThresholdIndex"),
        ("F3-L3-MIB", "f3L3AclRuleThresholdInterval"),
        ("F3-L3-MIB", "f3L3AclRuleThresholdVariable"),
        ("F3-L3-MIB", "f3L3AclRuleThresholdValueLo"),
        ("F3-L3-MIB", "f3L3AclRuleThresholdValueHi"),
        ("F3-L3-MIB", "f3L3AclRuleThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3L3AclRuleThresholdCrossingAlert.setStatus(
        "current"
    )

f3L2A2NAclRuleThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 3, 6)
)
f3L2A2NAclRuleThresholdCrossingAlert.setObjects(
      *(("F3-L3-MIB", "f3L2A2NAclRuleThresholdIndex"),
        ("F3-L3-MIB", "f3L2A2NAclRuleThresholdInterval"),
        ("F3-L3-MIB", "f3L2A2NAclRuleThresholdVariable"),
        ("F3-L3-MIB", "f3L2A2NAclRuleThresholdValueLo"),
        ("F3-L3-MIB", "f3L2A2NAclRuleThresholdValueHi"),
        ("F3-L3-MIB", "f3L2A2NAclRuleThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3L2A2NAclRuleThresholdCrossingAlert.setStatus(
        "current"
    )

f3L2N2AAclRuleThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 3, 7)
)
f3L2N2AAclRuleThresholdCrossingAlert.setObjects(
      *(("F3-L3-MIB", "f3L2N2AAclRuleThresholdIndex"),
        ("F3-L3-MIB", "f3L2N2AAclRuleThresholdInterval"),
        ("F3-L3-MIB", "f3L2N2AAclRuleThresholdVariable"),
        ("F3-L3-MIB", "f3L2N2AAclRuleThresholdValueLo"),
        ("F3-L3-MIB", "f3L2N2AAclRuleThresholdValueHi"),
        ("F3-L3-MIB", "f3L2N2AAclRuleThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3L2N2AAclRuleThresholdCrossingAlert.setStatus(
        "current"
    )

f3L3TrafficIPv6InterfaceThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 3, 8)
)
f3L3TrafficIPv6InterfaceThresholdCrossingAlert.setObjects(
      *(("F3-L3-MIB", "f3L3TrafficIPv6InterfaceThresholdIndex"),
        ("F3-L3-MIB", "f3L3TrafficIPv6InterfaceThresholdInterval"),
        ("F3-L3-MIB", "f3L3TrafficIPv6InterfaceThresholdVariable"),
        ("F3-L3-MIB", "f3L3TrafficIPv6InterfaceThresholdValueLo"),
        ("F3-L3-MIB", "f3L3TrafficIPv6InterfaceThresholdValueHi"),
        ("F3-L3-MIB", "f3L3TrafficIPv6InterfaceThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3L3TrafficIPv6InterfaceThresholdCrossingAlert.setStatus(
        "current"
    )

cmL3FlowPointThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 5, 9)
)
cmL3FlowPointThresholdCrossingAlert.setObjects(
      *(("F3-L3-MIB", "cmL3FlowPointThresholdIndex"),
        ("F3-L3-MIB", "cmL3FlowPointThresholdInterval"),
        ("F3-L3-MIB", "cmL3FlowPointThresholdVariable"),
        ("F3-L3-MIB", "cmL3FlowPointThresholdValueLo"),
        ("F3-L3-MIB", "cmL3FlowPointThresholdValueHi"),
        ("F3-L3-MIB", "cmL3FlowPointThresholdMonValue"))
)
if mibBuilder.loadTexts:
    cmL3FlowPointThresholdCrossingAlert.setStatus(
        "current"
    )

cmL3QosPolicerThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 5, 10)
)
cmL3QosPolicerThresholdCrossingAlert.setObjects(
      *(("F3-L3-MIB", "cmL3QosPolicerThresholdIndex"),
        ("F3-L3-MIB", "cmL3QosPolicerThresholdInterval"),
        ("F3-L3-MIB", "cmL3QosPolicerThresholdVariable"),
        ("F3-L3-MIB", "cmL3QosPolicerThresholdValueLo"),
        ("F3-L3-MIB", "cmL3QosPolicerThresholdValueHi"),
        ("F3-L3-MIB", "cmL3QosPolicerThresholdMonValue"))
)
if mibBuilder.loadTexts:
    cmL3QosPolicerThresholdCrossingAlert.setStatus(
        "current"
    )

cmL3QosShaperThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 5, 11)
)
cmL3QosShaperThresholdCrossingAlert.setObjects(
      *(("F3-L3-MIB", "cmL3QosShaperThresholdIndex"),
        ("F3-L3-MIB", "cmL3QosShaperThresholdInterval"),
        ("F3-L3-MIB", "cmL3QosShaperThresholdVariable"),
        ("F3-L3-MIB", "cmL3QosShaperThresholdValueLo"),
        ("F3-L3-MIB", "cmL3QosShaperThresholdValueHi"),
        ("F3-L3-MIB", "cmL3QosShaperThresholdMonValue"))
)
if mibBuilder.loadTexts:
    cmL3QosShaperThresholdCrossingAlert.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

f3L3Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 37, 4, 1, 1)
)
f3L3Compliance.setObjects(
      *(("F3-L3-MIB", "f3L3ObjectsGroup"),
        ("F3-L3-MIB", "f3L3PerfGroup"),
        ("F3-L3-MIB", "f3L3TrafficOspfGroup"),
        ("F3-L3-MIB", "f3L3TrafficIPv6Group"),
        ("F3-L3-MIB", "f3L3TrafficBgpGroup"))
)
if mibBuilder.loadTexts:
    f3L3Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F3-L3-MIB",
    **{"BgpGracefulRestartControlType": BgpGracefulRestartControlType,
       "EcmpDistributionType": EcmpDistributionType,
       "BgpUpdateSourceType": BgpUpdateSourceType,
       "BgpRouteFilterDirection": BgpRouteFilterDirection,
       "IpPrefixDispositionType": IpPrefixDispositionType,
       "BgpRouterActionType": BgpRouterActionType,
       "OspfRouterActionType": OspfRouterActionType,
       "Ipv6AddressAssignMode": Ipv6AddressAssignMode,
       "TrafficIpRouteOriginType": TrafficIpRouteOriginType,
       "NdpNeighborReachabilityState": NdpNeighborReachabilityState,
       "NdpRaDefaultRouterPreference": NdpRaDefaultRouterPreference,
       "Ipv6LinkLocalAddressMode": Ipv6LinkLocalAddressMode,
       "IpInterfaceType": IpInterfaceType,
       "OspfAuthType": OspfAuthType,
       "OspfInterfaceState": OspfInterfaceState,
       "OspfIfType": OspfIfType,
       "TrafficOspfRole": TrafficOspfRole,
       "OspfAdjacencyState": OspfAdjacencyState,
       "OspfAsLsaType": OspfAsLsaType,
       "OspfLsaType": OspfLsaType,
       "RoutesMetricType": RoutesMetricType,
       "TrafficOspfAreaType": TrafficOspfAreaType,
       "BgpSessionStateType": BgpSessionStateType,
       "BgpNextHopUpdateType": BgpNextHopUpdateType,
       "BgpPeerAddressFamilyNameType": BgpPeerAddressFamilyNameType,
       "OspfVersion": OspfVersion,
       "VrfAction": VrfAction,
       "VrfActionType": VrfActionType,
       "IfIpAddressSourceType": IfIpAddressSourceType,
       "DhcpRelayInterfaceSide": DhcpRelayInterfaceSide,
       "L3AclRuleOperation": L3AclRuleOperation,
       "AclRuleL2Side": AclRuleL2Side,
       "TrafficIpRouteStatus": TrafficIpRouteStatus,
       "RouteFlags": RouteFlags,
       "TrafficIpRouteStatusType": TrafficIpRouteStatusType,
       "AffectiveArpActionType": AffectiveArpActionType,
       "TrafficIpInterfaceActionType": TrafficIpInterfaceActionType,
       "TrafficIpv6InterfaceActionType": TrafficIpv6InterfaceActionType,
       "SrSidType": SrSidType,
       "VrfTransportType": VrfTransportType,
       "TilfaProtectionType": TilfaProtectionType,
       "f3L3MIB": f3L3MIB,
       "f3L3Objects": f3L3Objects,
       "f3DhcpRelayAgentTable": f3DhcpRelayAgentTable,
       "f3DhcpRelayAgentEntry": f3DhcpRelayAgentEntry,
       "f3DhcpRelayAgentIndex": f3DhcpRelayAgentIndex,
       "f3DhcpRelayAgentAlias": f3DhcpRelayAgentAlias,
       "f3DhcpRelayAgentAdminState": f3DhcpRelayAgentAdminState,
       "f3DhcpRelayAgentSecondaryState": f3DhcpRelayAgentSecondaryState,
       "f3DhcpRelayAgentOperationalState": f3DhcpRelayAgentOperationalState,
       "f3DhcpRelayAgentIpVersion": f3DhcpRelayAgentIpVersion,
       "f3DhcpRelayAgentServerIpAddress": f3DhcpRelayAgentServerIpAddress,
       "f3DhcpRelayAgentOp82SubOp9ControlEnabled": f3DhcpRelayAgentOp82SubOp9ControlEnabled,
       "f3DhcpRelayAgentOp82SubOp9Value": f3DhcpRelayAgentOp82SubOp9Value,
       "f3DhcpRelayAgentStorageType": f3DhcpRelayAgentStorageType,
       "f3DhcpRelayAgentRowStatus": f3DhcpRelayAgentRowStatus,
       "f3VrfTable": f3VrfTable,
       "f3VrfEntry": f3VrfEntry,
       "f3VrfIndex": f3VrfIndex,
       "f3VrfAlias": f3VrfAlias,
       "f3VrfAdminState": f3VrfAdminState,
       "f3VrfSecondaryState": f3VrfSecondaryState,
       "f3VrfOperationalState": f3VrfOperationalState,
       "f3VrfAccIsolationControlEnabled": f3VrfAccIsolationControlEnabled,
       "f3VrfPingIpv4Destination": f3VrfPingIpv4Destination,
       "f3VrfTraceRouteIpv4Destination": f3VrfTraceRouteIpv4Destination,
       "f3VrfAction": f3VrfAction,
       "f3VrfPingResult": f3VrfPingResult,
       "f3VrfTraceRouteResult": f3VrfTraceRouteResult,
       "f3VrfStorageType": f3VrfStorageType,
       "f3VrfRowStatus": f3VrfRowStatus,
       "f3VrfDhcpRoutesControl": f3VrfDhcpRoutesControl,
       "f3VrfActionX": f3VrfActionX,
       "f3VrfActionIfName": f3VrfActionIfName,
       "f3VrfIpVersion": f3VrfIpVersion,
       "f3VrfPingIpv6Destination": f3VrfPingIpv6Destination,
       "f3VrfTraceRouteIpv6Destination": f3VrfTraceRouteIpv6Destination,
       "f3VrfMaxFwdTableEntries": f3VrfMaxFwdTableEntries,
       "f3VrfFwdTableFull": f3VrfFwdTableFull,
       "f3VrfEcmpDistribution": f3VrfEcmpDistribution,
       "f3VrfEcmpStaticRoutesMaximumPaths": f3VrfEcmpStaticRoutesMaximumPaths,
       "f3VrfTransportType": f3VrfTransportType,
       "f3L3FlowPointTable": f3L3FlowPointTable,
       "f3L3FlowPointEntry": f3L3FlowPointEntry,
       "f3L3FlowPointPortTypeIndex": f3L3FlowPointPortTypeIndex,
       "f3L3FlowPointPortIndex": f3L3FlowPointPortIndex,
       "f3L3FlowPointIndex": f3L3FlowPointIndex,
       "f3L3FlowPointAlias": f3L3FlowPointAlias,
       "f3L3FlowPointAdminState": f3L3FlowPointAdminState,
       "f3L3FlowPointSecondaryState": f3L3FlowPointSecondaryState,
       "f3L3FlowPointOperationalState": f3L3FlowPointOperationalState,
       "f3L3FlowPointMultiCOSEnabled": f3L3FlowPointMultiCOSEnabled,
       "f3L3FlowPointCOS": f3L3FlowPointCOS,
       "f3L3FlowPointUntaggedMemberShipEnabled": f3L3FlowPointUntaggedMemberShipEnabled,
       "f3L3FlowPointOuterTagMemberShipEnabled": f3L3FlowPointOuterTagMemberShipEnabled,
       "f3L3FlowPointOuterTagMemberShipVlanId": f3L3FlowPointOuterTagMemberShipVlanId,
       "f3L3FlowPointInnerTagMemberShipEnabled": f3L3FlowPointInnerTagMemberShipEnabled,
       "f3L3FlowPointInnerTagMemberShipVlanId": f3L3FlowPointInnerTagMemberShipVlanId,
       "f3L3FlowPointFragmentedPktsFwdEnabled": f3L3FlowPointFragmentedPktsFwdEnabled,
       "f3L3FlowPointHCosMgmtEnabled": f3L3FlowPointHCosMgmtEnabled,
       "f3L3FlowPointHCosGuaranteedBwHi": f3L3FlowPointHCosGuaranteedBwHi,
       "f3L3FlowPointHCosGuaranteedBwLo": f3L3FlowPointHCosGuaranteedBwLo,
       "f3L3FlowPointHCosMaximumBwHi": f3L3FlowPointHCosMaximumBwHi,
       "f3L3FlowPointHCosMaximumBwLo": f3L3FlowPointHCosMaximumBwLo,
       "f3L3FlowPointPolicingEnabled": f3L3FlowPointPolicingEnabled,
       "f3L3FlowPointStorageType": f3L3FlowPointStorageType,
       "f3L3FlowPointRowStatus": f3L3FlowPointRowStatus,
       "f3L3FlowPointDscpOverwriteControl": f3L3FlowPointDscpOverwriteControl,
       "f3L3FlowPointPriMapProfile": f3L3FlowPointPriMapProfile,
       "f3L3FlowPointRefConnectGuardFlow": f3L3FlowPointRefConnectGuardFlow,
       "f3L3FlowPointSecureState": f3L3FlowPointSecureState,
       "f3L3FlowPointSecureBlockingEnabled": f3L3FlowPointSecureBlockingEnabled,
       "f3L3FlowPointWfqSegmentationCOS": f3L3FlowPointWfqSegmentationCOS,
       "f3L3FlowPointWfqGroupCOS": f3L3FlowPointWfqGroupCOS,
       "f3L3FlowPointWfqGroupEirLo": f3L3FlowPointWfqGroupEirLo,
       "f3L3FlowPointWfqGroupEirHi": f3L3FlowPointWfqGroupEirHi,
       "f3L3FlowPointOuterVlanEthertype": f3L3FlowPointOuterVlanEthertype,
       "f3L3FlowPointInnerVlanEthertype": f3L3FlowPointInnerVlanEthertype,
       "f3L3FlowPointIpVersion": f3L3FlowPointIpVersion,
       "f3L3AclRuleTable": f3L3AclRuleTable,
       "f3L3AclRuleEntry": f3L3AclRuleEntry,
       "f3L3AclRuleParentIndex": f3L3AclRuleParentIndex,
       "f3L3AclRuleIndex": f3L3AclRuleIndex,
       "f3L3AclRuleAlias": f3L3AclRuleAlias,
       "f3L3AclRuleSrcIpv4AddressControl": f3L3AclRuleSrcIpv4AddressControl,
       "f3L3AclRuleDynamicSrcIpControl": f3L3AclRuleDynamicSrcIpControl,
       "f3L3AclRuleSrcIpv4AddressLowLimit": f3L3AclRuleSrcIpv4AddressLowLimit,
       "f3L3AclRuleDstIpv4AddressControl": f3L3AclRuleDstIpv4AddressControl,
       "f3L3AclRuleDstIpv4AddressLowLimit": f3L3AclRuleDstIpv4AddressLowLimit,
       "f3L3AclRuleIpv4PriorityControl": f3L3AclRuleIpv4PriorityControl,
       "f3L3AclRuleIpv4PriorityLowLimit": f3L3AclRuleIpv4PriorityLowLimit,
       "f3L3AclRuleProtocolControl": f3L3AclRuleProtocolControl,
       "f3L3AclRuleProtocolNumber": f3L3AclRuleProtocolNumber,
       "f3L3AclRuleSrcPortControl": f3L3AclRuleSrcPortControl,
       "f3L3AclRuleSrcPortLowLimit": f3L3AclRuleSrcPortLowLimit,
       "f3L3AclRuleSrcPortHighLimit": f3L3AclRuleSrcPortHighLimit,
       "f3L3AclRuleDstPortControl": f3L3AclRuleDstPortControl,
       "f3L3AclRuleDstPortLowLimit": f3L3AclRuleDstPortLowLimit,
       "f3L3AclRuleDstPortHighLimit": f3L3AclRuleDstPortHighLimit,
       "f3L3AclRulePriority": f3L3AclRulePriority,
       "f3L3AclRuleCOS": f3L3AclRuleCOS,
       "f3L3AclRuleOperation": f3L3AclRuleOperation,
       "f3L3AclRuleSummary": f3L3AclRuleSummary,
       "f3L3AclRuleCosOverrideControl": f3L3AclRuleCosOverrideControl,
       "f3L3AclRuleSrcMacAddressControl": f3L3AclRuleSrcMacAddressControl,
       "f3L3AclRuleDynamicSrcMacAddressControl": f3L3AclRuleDynamicSrcMacAddressControl,
       "f3L3AclRuleSrcMacAddress": f3L3AclRuleSrcMacAddress,
       "f3L3AclRuleSrcMacAddressMask": f3L3AclRuleSrcMacAddressMask,
       "f3L3AclRuleDstMacAddressControl": f3L3AclRuleDstMacAddressControl,
       "f3L3AclRuleDstMacAddress": f3L3AclRuleDstMacAddress,
       "f3L3AclRuleDstMacAddressMask": f3L3AclRuleDstMacAddressMask,
       "f3L3AclRuleOuterVlanVIDControl": f3L3AclRuleOuterVlanVIDControl,
       "f3L3AclRuleOuterVlanVIDLowLimit": f3L3AclRuleOuterVlanVIDLowLimit,
       "f3L3AclRuleOuterVlanVIDHighLimit": f3L3AclRuleOuterVlanVIDHighLimit,
       "f3L3AclRuleInnerVlanVIDControl": f3L3AclRuleInnerVlanVIDControl,
       "f3L3AclRuleInnerVlanVIDLowLimit": f3L3AclRuleInnerVlanVIDLowLimit,
       "f3L3AclRuleInnerVlanVIDHighLimit": f3L3AclRuleInnerVlanVIDHighLimit,
       "f3L3AclRuleOuterVlanPcpControl": f3L3AclRuleOuterVlanPcpControl,
       "f3L3AclRuleOuterVlanPcpLowLimit": f3L3AclRuleOuterVlanPcpLowLimit,
       "f3L3AclRuleOuterVlanPcpHighLimit": f3L3AclRuleOuterVlanPcpHighLimit,
       "f3L3AclRuleInnerVlanPcpControl": f3L3AclRuleInnerVlanPcpControl,
       "f3L3AclRuleInnerVlanPcpLowLimit": f3L3AclRuleInnerVlanPcpLowLimit,
       "f3L3AclRuleInnerVlanPcpHighLimit": f3L3AclRuleInnerVlanPcpHighLimit,
       "f3L3AclRuleOuterVlanDeiControl": f3L3AclRuleOuterVlanDeiControl,
       "f3L3AclRuleOuterVlanDei": f3L3AclRuleOuterVlanDei,
       "f3L3AclRuleEtherTypeControl": f3L3AclRuleEtherTypeControl,
       "f3L3AclRuleEtherType": f3L3AclRuleEtherType,
       "f3L3AclRuleTcpFlagsControl": f3L3AclRuleTcpFlagsControl,
       "f3L3AclRuleTcpFlags": f3L3AclRuleTcpFlags,
       "f3L3AclRuleSrcIpv4AddressHighLimit": f3L3AclRuleSrcIpv4AddressHighLimit,
       "f3L3AclRuleDstIpv4AddressHighLimit": f3L3AclRuleDstIpv4AddressHighLimit,
       "f3L3AclRuleIpv4PriorityHighLimit": f3L3AclRuleIpv4PriorityHighLimit,
       "f3L3AclRuleStorageType": f3L3AclRuleStorageType,
       "f3L3AclRuleRowStatus": f3L3AclRuleRowStatus,
       "f3L3AclRuleAdminState": f3L3AclRuleAdminState,
       "f3L3AclRuleActive": f3L3AclRuleActive,
       "f3L3AclRuleSrcIpV6AddressControl": f3L3AclRuleSrcIpV6AddressControl,
       "f3L3AclRuleSrcIpV6Address": f3L3AclRuleSrcIpV6Address,
       "f3L3AclRuleSrcIpV6AddressPrefixLen": f3L3AclRuleSrcIpV6AddressPrefixLen,
       "f3L3AclRuleDstIpV6AddressControl": f3L3AclRuleDstIpV6AddressControl,
       "f3L3AclRuleDstIpV6Address": f3L3AclRuleDstIpV6Address,
       "f3L3AclRuleDstIpV6AddressPrefixLen": f3L3AclRuleDstIpV6AddressPrefixLen,
       "f3L3AclRuleIpV6FlowLabelControl": f3L3AclRuleIpV6FlowLabelControl,
       "f3L3AclRuleIpV6FlowLabel": f3L3AclRuleIpV6FlowLabel,
       "f3L3AclRulePriorityControl": f3L3AclRulePriorityControl,
       "f3L3AclRulePriorityLowLimit": f3L3AclRulePriorityLowLimit,
       "f3L3AclRulePriorityHighLimit": f3L3AclRulePriorityHighLimit,
       "f3L2A2NAclRuleTable": f3L2A2NAclRuleTable,
       "f3L2A2NAclRuleEntry": f3L2A2NAclRuleEntry,
       "f3L2A2NAclRuleParentIndex": f3L2A2NAclRuleParentIndex,
       "f3L2A2NAclRuleIndex": f3L2A2NAclRuleIndex,
       "f3L2A2NAclRuleAlias": f3L2A2NAclRuleAlias,
       "f3L2A2NAclRuleSrcIpv4AddressControl": f3L2A2NAclRuleSrcIpv4AddressControl,
       "f3L2A2NAclRuleDynamicSrcIpControl": f3L2A2NAclRuleDynamicSrcIpControl,
       "f3L2A2NAclRuleSrcIpv4AddressLowLimit": f3L2A2NAclRuleSrcIpv4AddressLowLimit,
       "f3L2A2NAclRuleDstIpv4AddressControl": f3L2A2NAclRuleDstIpv4AddressControl,
       "f3L2A2NAclRuleDstIpv4AddressLowLimit": f3L2A2NAclRuleDstIpv4AddressLowLimit,
       "f3L2A2NAclRuleIpv4PriorityControl": f3L2A2NAclRuleIpv4PriorityControl,
       "f3L2A2NAclRuleIpv4PriorityLowLimit": f3L2A2NAclRuleIpv4PriorityLowLimit,
       "f3L2A2NAclRuleProtocolControl": f3L2A2NAclRuleProtocolControl,
       "f3L2A2NAclRuleProtocolNumber": f3L2A2NAclRuleProtocolNumber,
       "f3L2A2NAclRuleSrcPortControl": f3L2A2NAclRuleSrcPortControl,
       "f3L2A2NAclRuleSrcPortLowLimit": f3L2A2NAclRuleSrcPortLowLimit,
       "f3L2A2NAclRuleSrcPortHighLimit": f3L2A2NAclRuleSrcPortHighLimit,
       "f3L2A2NAclRuleDstPortControl": f3L2A2NAclRuleDstPortControl,
       "f3L2A2NAclRuleDstPortLowLimit": f3L2A2NAclRuleDstPortLowLimit,
       "f3L2A2NAclRuleDstPortHighLimit": f3L2A2NAclRuleDstPortHighLimit,
       "f3L2A2NAclRulePriority": f3L2A2NAclRulePriority,
       "f3L2A2NAclRuleCOS": f3L2A2NAclRuleCOS,
       "f3L2A2NAclRuleOperation": f3L2A2NAclRuleOperation,
       "f3L2A2NAclRuleSummary": f3L2A2NAclRuleSummary,
       "f3L2A2NAclRuleCosOverrideControl": f3L2A2NAclRuleCosOverrideControl,
       "f3L2A2NAclRuleSrcMacAddressControl": f3L2A2NAclRuleSrcMacAddressControl,
       "f3L2A2NAclRuleDynamicSrcMacAddressControl": f3L2A2NAclRuleDynamicSrcMacAddressControl,
       "f3L2A2NAclRuleSrcMacAddress": f3L2A2NAclRuleSrcMacAddress,
       "f3L2A2NAclRuleSrcMacAddressMask": f3L2A2NAclRuleSrcMacAddressMask,
       "f3L2A2NAclRuleDstMacAddressControl": f3L2A2NAclRuleDstMacAddressControl,
       "f3L2A2NAclRuleDstMacAddress": f3L2A2NAclRuleDstMacAddress,
       "f3L2A2NAclRuleDstMacAddressMask": f3L2A2NAclRuleDstMacAddressMask,
       "f3L2A2NAclRuleOuterVlanVIDControl": f3L2A2NAclRuleOuterVlanVIDControl,
       "f3L2A2NAclRuleOuterVlanVIDLowLimit": f3L2A2NAclRuleOuterVlanVIDLowLimit,
       "f3L2A2NAclRuleOuterVlanVIDHighLimit": f3L2A2NAclRuleOuterVlanVIDHighLimit,
       "f3L2A2NAclRuleInnerVlanVIDControl": f3L2A2NAclRuleInnerVlanVIDControl,
       "f3L2A2NAclRuleInnerVlanVIDLowLimit": f3L2A2NAclRuleInnerVlanVIDLowLimit,
       "f3L2A2NAclRuleInnerVlanVIDHighLimit": f3L2A2NAclRuleInnerVlanVIDHighLimit,
       "f3L2A2NAclRuleOuterVlanPcpControl": f3L2A2NAclRuleOuterVlanPcpControl,
       "f3L2A2NAclRuleOuterVlanPcpLowLimit": f3L2A2NAclRuleOuterVlanPcpLowLimit,
       "f3L2A2NAclRuleOuterVlanPcpHighLimit": f3L2A2NAclRuleOuterVlanPcpHighLimit,
       "f3L2A2NAclRuleInnerVlanPcpControl": f3L2A2NAclRuleInnerVlanPcpControl,
       "f3L2A2NAclRuleInnerVlanPcpLowLimit": f3L2A2NAclRuleInnerVlanPcpLowLimit,
       "f3L2A2NAclRuleInnerVlanPcpHighLimit": f3L2A2NAclRuleInnerVlanPcpHighLimit,
       "f3L2A2NAclRuleOuterVlanDeiControl": f3L2A2NAclRuleOuterVlanDeiControl,
       "f3L2A2NAclRuleOuterVlanDei": f3L2A2NAclRuleOuterVlanDei,
       "f3L2A2NAclRuleEtherTypeControl": f3L2A2NAclRuleEtherTypeControl,
       "f3L2A2NAclRuleEtherType": f3L2A2NAclRuleEtherType,
       "f3L2A2NAclRuleTcpFlagsControl": f3L2A2NAclRuleTcpFlagsControl,
       "f3L2A2NAclRuleTcpFlags": f3L2A2NAclRuleTcpFlags,
       "f3L2A2NAclRuleSrcIpv4AddressHighLimit": f3L2A2NAclRuleSrcIpv4AddressHighLimit,
       "f3L2A2NAclRuleDstIpv4AddressHighLimit": f3L2A2NAclRuleDstIpv4AddressHighLimit,
       "f3L2A2NAclRuleIpv4PriorityHighLimit": f3L2A2NAclRuleIpv4PriorityHighLimit,
       "f3L2A2NAclRuleStorageType": f3L2A2NAclRuleStorageType,
       "f3L2A2NAclRuleRowStatus": f3L2A2NAclRuleRowStatus,
       "f3L2A2NAclRuleAdminState": f3L2A2NAclRuleAdminState,
       "f3L2A2NAclRuleActive": f3L2A2NAclRuleActive,
       "f3L2A2NAclRuleSrcIpV6AddressControl": f3L2A2NAclRuleSrcIpV6AddressControl,
       "f3L2A2NAclRuleSrcIpV6Address": f3L2A2NAclRuleSrcIpV6Address,
       "f3L2A2NAclRuleSrcIpV6AddressPrefixLen": f3L2A2NAclRuleSrcIpV6AddressPrefixLen,
       "f3L2A2NAclRuleDstIpV6AddressControl": f3L2A2NAclRuleDstIpV6AddressControl,
       "f3L2A2NAclRuleDstIpV6Address": f3L2A2NAclRuleDstIpV6Address,
       "f3L2A2NAclRuleDstIpV6AddressPrefixLen": f3L2A2NAclRuleDstIpV6AddressPrefixLen,
       "f3L2A2NAclRuleIpV6FlowLabelControl": f3L2A2NAclRuleIpV6FlowLabelControl,
       "f3L2A2NAclRuleIpV6FlowLabel": f3L2A2NAclRuleIpV6FlowLabel,
       "f3L2N2AAclRuleTable": f3L2N2AAclRuleTable,
       "f3L2N2AAclRuleEntry": f3L2N2AAclRuleEntry,
       "f3L2N2AAclRuleParentIndex": f3L2N2AAclRuleParentIndex,
       "f3L2N2AAclRuleIndex": f3L2N2AAclRuleIndex,
       "f3L2N2AAclRuleAlias": f3L2N2AAclRuleAlias,
       "f3L2N2AAclRuleSrcIpv4AddressControl": f3L2N2AAclRuleSrcIpv4AddressControl,
       "f3L2N2AAclRuleDynamicSrcIpControl": f3L2N2AAclRuleDynamicSrcIpControl,
       "f3L2N2AAclRuleSrcIpv4AddressLowLimit": f3L2N2AAclRuleSrcIpv4AddressLowLimit,
       "f3L2N2AAclRuleDstIpv4AddressControl": f3L2N2AAclRuleDstIpv4AddressControl,
       "f3L2N2AAclRuleDstIpv4AddressLowLimit": f3L2N2AAclRuleDstIpv4AddressLowLimit,
       "f3L2N2AAclRuleIpv4PriorityControl": f3L2N2AAclRuleIpv4PriorityControl,
       "f3L2N2AAclRuleIpv4PriorityLowLimit": f3L2N2AAclRuleIpv4PriorityLowLimit,
       "f3L2N2AAclRuleProtocolControl": f3L2N2AAclRuleProtocolControl,
       "f3L2N2AAclRuleProtocolNumber": f3L2N2AAclRuleProtocolNumber,
       "f3L2N2AAclRuleSrcPortControl": f3L2N2AAclRuleSrcPortControl,
       "f3L2N2AAclRuleSrcPortLowLimit": f3L2N2AAclRuleSrcPortLowLimit,
       "f3L2N2AAclRuleSrcPortHighLimit": f3L2N2AAclRuleSrcPortHighLimit,
       "f3L2N2AAclRuleDstPortControl": f3L2N2AAclRuleDstPortControl,
       "f3L2N2AAclRuleDstPortLowLimit": f3L2N2AAclRuleDstPortLowLimit,
       "f3L2N2AAclRuleDstPortHighLimit": f3L2N2AAclRuleDstPortHighLimit,
       "f3L2N2AAclRulePriority": f3L2N2AAclRulePriority,
       "f3L2N2AAclRuleCOS": f3L2N2AAclRuleCOS,
       "f3L2N2AAclRuleOperation": f3L2N2AAclRuleOperation,
       "f3L2N2AAclRuleSummary": f3L2N2AAclRuleSummary,
       "f3L2N2AAclRuleCosOverrideControl": f3L2N2AAclRuleCosOverrideControl,
       "f3L2N2AAclRuleSrcMacAddressControl": f3L2N2AAclRuleSrcMacAddressControl,
       "f3L2N2AAclRuleDynamicSrcMacAddressControl": f3L2N2AAclRuleDynamicSrcMacAddressControl,
       "f3L2N2AAclRuleSrcMacAddress": f3L2N2AAclRuleSrcMacAddress,
       "f3L2N2AAclRuleSrcMacAddressMask": f3L2N2AAclRuleSrcMacAddressMask,
       "f3L2N2AAclRuleDstMacAddressControl": f3L2N2AAclRuleDstMacAddressControl,
       "f3L2N2AAclRuleDstMacAddress": f3L2N2AAclRuleDstMacAddress,
       "f3L2N2AAclRuleDstMacAddressMask": f3L2N2AAclRuleDstMacAddressMask,
       "f3L2N2AAclRuleOuterVlanVIDControl": f3L2N2AAclRuleOuterVlanVIDControl,
       "f3L2N2AAclRuleOuterVlanVIDLowLimit": f3L2N2AAclRuleOuterVlanVIDLowLimit,
       "f3L2N2AAclRuleOuterVlanVIDHighLimit": f3L2N2AAclRuleOuterVlanVIDHighLimit,
       "f3L2N2AAclRuleInnerVlanVIDControl": f3L2N2AAclRuleInnerVlanVIDControl,
       "f3L2N2AAclRuleInnerVlanVIDLowLimit": f3L2N2AAclRuleInnerVlanVIDLowLimit,
       "f3L2N2AAclRuleInnerVlanVIDHighLimit": f3L2N2AAclRuleInnerVlanVIDHighLimit,
       "f3L2N2AAclRuleOuterVlanPcpControl": f3L2N2AAclRuleOuterVlanPcpControl,
       "f3L2N2AAclRuleOuterVlanPcpLowLimit": f3L2N2AAclRuleOuterVlanPcpLowLimit,
       "f3L2N2AAclRuleOuterVlanPcpHighLimit": f3L2N2AAclRuleOuterVlanPcpHighLimit,
       "f3L2N2AAclRuleInnerVlanPcpControl": f3L2N2AAclRuleInnerVlanPcpControl,
       "f3L2N2AAclRuleInnerVlanPcpLowLimit": f3L2N2AAclRuleInnerVlanPcpLowLimit,
       "f3L2N2AAclRuleInnerVlanPcpHighLimit": f3L2N2AAclRuleInnerVlanPcpHighLimit,
       "f3L2N2AAclRuleOuterVlanDeiControl": f3L2N2AAclRuleOuterVlanDeiControl,
       "f3L2N2AAclRuleOuterVlanDei": f3L2N2AAclRuleOuterVlanDei,
       "f3L2N2AAclRuleEtherTypeControl": f3L2N2AAclRuleEtherTypeControl,
       "f3L2N2AAclRuleEtherType": f3L2N2AAclRuleEtherType,
       "f3L2N2AAclRuleTcpFlagsControl": f3L2N2AAclRuleTcpFlagsControl,
       "f3L2N2AAclRuleTcpFlags": f3L2N2AAclRuleTcpFlags,
       "f3L2N2AAclRuleSrcIpv4AddressHighLimit": f3L2N2AAclRuleSrcIpv4AddressHighLimit,
       "f3L2N2AAclRuleDstIpv4AddressHighLimit": f3L2N2AAclRuleDstIpv4AddressHighLimit,
       "f3L2N2AAclRuleIpv4PriorityHighLimit": f3L2N2AAclRuleIpv4PriorityHighLimit,
       "f3L2N2AAclRuleStorageType": f3L2N2AAclRuleStorageType,
       "f3L2N2AAclRuleRowStatus": f3L2N2AAclRuleRowStatus,
       "f3L2N2AAclRuleAdminState": f3L2N2AAclRuleAdminState,
       "f3L2N2AAclRuleActive": f3L2N2AAclRuleActive,
       "f3L2N2AAclRuleSrcIpV6AddressControl": f3L2N2AAclRuleSrcIpV6AddressControl,
       "f3L2N2AAclRuleSrcIpV6Address": f3L2N2AAclRuleSrcIpV6Address,
       "f3L2N2AAclRuleSrcIpV6AddressPrefixLen": f3L2N2AAclRuleSrcIpV6AddressPrefixLen,
       "f3L2N2AAclRuleDstIpV6AddressControl": f3L2N2AAclRuleDstIpV6AddressControl,
       "f3L2N2AAclRuleDstIpV6Address": f3L2N2AAclRuleDstIpV6Address,
       "f3L2N2AAclRuleDstIpV6AddressPrefixLen": f3L2N2AAclRuleDstIpV6AddressPrefixLen,
       "f3L2N2AAclRuleIpV6FlowLabelControl": f3L2N2AAclRuleIpV6FlowLabelControl,
       "f3L2N2AAclRuleIpV6FlowLabel": f3L2N2AAclRuleIpV6FlowLabel,
       "f3L3QosPolicerTable": f3L3QosPolicerTable,
       "f3L3QosPolicerEntry": f3L3QosPolicerEntry,
       "f3L3QosPolicerIndex": f3L3QosPolicerIndex,
       "f3L3QosPolicerAdminState": f3L3QosPolicerAdminState,
       "f3L3QosPolicerOperationalState": f3L3QosPolicerOperationalState,
       "f3L3QosPolicerSecondaryState": f3L3QosPolicerSecondaryState,
       "f3L3QosPolicerCIRLo": f3L3QosPolicerCIRLo,
       "f3L3QosPolicerCIRHi": f3L3QosPolicerCIRHi,
       "f3L3QosPolicerEIRLo": f3L3QosPolicerEIRLo,
       "f3L3QosPolicerEIRHi": f3L3QosPolicerEIRHi,
       "f3L3QosPolicerCBS": f3L3QosPolicerCBS,
       "f3L3QosPolicerEBS": f3L3QosPolicerEBS,
       "f3L3QosPolicerAlgorithm": f3L3QosPolicerAlgorithm,
       "f3L3QosPolicerColorMode": f3L3QosPolicerColorMode,
       "f3L3QosPolicerCouplingFlag": f3L3QosPolicerCouplingFlag,
       "f3L3QosPolicerStorageType": f3L3QosPolicerStorageType,
       "f3L3QosPolicerRowStatus": f3L3QosPolicerRowStatus,
       "f3L3QosPolicerCIRMaxHi": f3L3QosPolicerCIRMaxHi,
       "f3L3QosPolicerCIRMaxLo": f3L3QosPolicerCIRMaxLo,
       "f3L3QosPolicerEIRMaxHi": f3L3QosPolicerEIRMaxHi,
       "f3L3QosPolicerEIRMaxLo": f3L3QosPolicerEIRMaxLo,
       "f3L3QosPolicerEnvelopeObject": f3L3QosPolicerEnvelopeObject,
       "f3L3QosPolicerRank": f3L3QosPolicerRank,
       "f3L3QosPolicerPolicingEnabled": f3L3QosPolicerPolicingEnabled,
       "f3L3QosShaperTable": f3L3QosShaperTable,
       "f3L3QosShaperEntry": f3L3QosShaperEntry,
       "f3L3QosShaperIndex": f3L3QosShaperIndex,
       "f3L3QosShaperAdminState": f3L3QosShaperAdminState,
       "f3L3QosShaperOperationalState": f3L3QosShaperOperationalState,
       "f3L3QosShaperSecondaryState": f3L3QosShaperSecondaryState,
       "f3L3QosShaperCIRLo": f3L3QosShaperCIRLo,
       "f3L3QosShaperCIRHi": f3L3QosShaperCIRHi,
       "f3L3QosShaperEIRLo": f3L3QosShaperEIRLo,
       "f3L3QosShaperEIRHi": f3L3QosShaperEIRHi,
       "f3L3QosShaperBufferSize": f3L3QosShaperBufferSize,
       "f3L3QosShaperCOS": f3L3QosShaperCOS,
       "f3L3QosShaperWredGreenMinQueueThreshold": f3L3QosShaperWredGreenMinQueueThreshold,
       "f3L3QosShaperWredGreenMaxQueueThreshold": f3L3QosShaperWredGreenMaxQueueThreshold,
       "f3L3QosShaperWredGreenDropProbability": f3L3QosShaperWredGreenDropProbability,
       "f3L3QosShaperWredYellowMinQueueThreshold": f3L3QosShaperWredYellowMinQueueThreshold,
       "f3L3QosShaperWredYellowMaxQueueThreshold": f3L3QosShaperWredYellowMaxQueueThreshold,
       "f3L3QosShaperWredYellowDropProbability": f3L3QosShaperWredYellowDropProbability,
       "f3L3QosShaperStorageType": f3L3QosShaperStorageType,
       "f3L3QosShaperRowStatus": f3L3QosShaperRowStatus,
       "f3L3QosShaperWfqWeight": f3L3QosShaperWfqWeight,
       "f3L3TrafficIPInterfaceTable": f3L3TrafficIPInterfaceTable,
       "f3L3TrafficIPInterfaceEntry": f3L3TrafficIPInterfaceEntry,
       "f3L3TrafficIPIfIndex": f3L3TrafficIPIfIndex,
       "f3L3TrafficIPIfName": f3L3TrafficIPIfName,
       "f3L3TrafficIPIfAdminState": f3L3TrafficIPIfAdminState,
       "f3L3TrafficIPIfSecondaryState": f3L3TrafficIPIfSecondaryState,
       "f3L3TrafficIPIfOperationalState": f3L3TrafficIPIfOperationalState,
       "f3L3TrafficIPIfProxyArpEnabled": f3L3TrafficIPIfProxyArpEnabled,
       "f3L3TrafficIPIfIpAddressSourceType": f3L3TrafficIPIfIpAddressSourceType,
       "f3L3TrafficIPIfMgmtUseEnable": f3L3TrafficIPIfMgmtUseEnable,
       "f3L3TrafficIPIfIpAddress": f3L3TrafficIPIfIpAddress,
       "f3L3TrafficIPIfMask": f3L3TrafficIPIfMask,
       "f3L3TrafficIPIfDhcpRelayInterfaceSide": f3L3TrafficIPIfDhcpRelayInterfaceSide,
       "f3L3TrafficIPIfDhcpRelayVendorClassiDOpt60": f3L3TrafficIPIfDhcpRelayVendorClassiDOpt60,
       "f3L3TrafficIPIfDhcpRelayVendorClassiDOpt60Control": f3L3TrafficIPIfDhcpRelayVendorClassiDOpt60Control,
       "f3L3TrafficIPIfDhcpRelayUserClassOpt77": f3L3TrafficIPIfDhcpRelayUserClassOpt77,
       "f3L3TrafficIPIfDhcpRelayUserClassOpt77Control": f3L3TrafficIPIfDhcpRelayUserClassOpt77Control,
       "f3L3TrafficIPIfDhcpRelayInfoOpt82Sub1": f3L3TrafficIPIfDhcpRelayInfoOpt82Sub1,
       "f3L3TrafficIPIfDhcpRelayInfoOpt82Sub1Enabled": f3L3TrafficIPIfDhcpRelayInfoOpt82Sub1Enabled,
       "f3L3TrafficIPIfDhcpRelayInfoOpt82Sub2": f3L3TrafficIPIfDhcpRelayInfoOpt82Sub2,
       "f3L3TrafficIPIfDhcpRelayInfoOpt82Sub2Enabled": f3L3TrafficIPIfDhcpRelayInfoOpt82Sub2Enabled,
       "f3L3TrafficIPIfDhcpEnabled": f3L3TrafficIPIfDhcpEnabled,
       "f3L3TrafficIPIfDhcpRole": f3L3TrafficIPIfDhcpRole,
       "f3L3TrafficIPIfDhcpClientIdEnabled": f3L3TrafficIPIfDhcpClientIdEnabled,
       "f3L3TrafficIPIfDhcpClientId": f3L3TrafficIPIfDhcpClientId,
       "f3L3TrafficIPIfDhcpClassIdEnabled": f3L3TrafficIPIfDhcpClassIdEnabled,
       "f3L3TrafficIPIfDhcpHostNameEnabled": f3L3TrafficIPIfDhcpHostNameEnabled,
       "f3L3TrafficIPIfDhcpHostName": f3L3TrafficIPIfDhcpHostName,
       "f3L3TrafficIPIfDhcpClientIdType": f3L3TrafficIPIfDhcpClientIdType,
       "f3L3TrafficIPIfDhcpHostNameType": f3L3TrafficIPIfDhcpHostNameType,
       "f3L3TrafficIPIfStorageType": f3L3TrafficIPIfStorageType,
       "f3L3TrafficIPIfRowStatus": f3L3TrafficIPIfRowStatus,
       "f3L3TrafficIPIfAction": f3L3TrafficIPIfAction,
       "f3L3TrafficIPIfActionX": f3L3TrafficIPIfActionX,
       "f3L3TrafficIPIfUnnumberedControl": f3L3TrafficIPIfUnnumberedControl,
       "f3L3TrafficIPIfBorrowedIntf": f3L3TrafficIPIfBorrowedIntf,
       "f3L3TrafficIPIfIpMode": f3L3TrafficIPIfIpMode,
       "f3L3TrafficIPIfType": f3L3TrafficIPIfType,
       "f3L3TrafficIPIfIpv6LinkLocalAddr": f3L3TrafficIPIfIpv6LinkLocalAddr,
       "f3L3TrafficIPIfIpv6LinkLocalAddrMode": f3L3TrafficIPIfIpv6LinkLocalAddrMode,
       "f3L3TrafficIPIfIpv6StatelessAddrAutoconfigEnabled": f3L3TrafficIPIfIpv6StatelessAddrAutoconfigEnabled,
       "f3L3TrafficIPIfDefaultGateway": f3L3TrafficIPIfDefaultGateway,
       "f3L3TrafficIPIfIcmpErrorMsgRateLimit": f3L3TrafficIPIfIcmpErrorMsgRateLimit,
       "f3L3TrafficIPIfDhcpv6Role": f3L3TrafficIPIfDhcpv6Role,
       "f3L3TrafficIPIfDhcpv6Enabled": f3L3TrafficIPIfDhcpv6Enabled,
       "f3L3TrafficIPIfDhcpRapidCommitControlEnabled": f3L3TrafficIPIfDhcpRapidCommitControlEnabled,
       "f3L3TrafficIPIfMaxRAInterval": f3L3TrafficIPIfMaxRAInterval,
       "f3L3TrafficIPIfMinRAInterval": f3L3TrafficIPIfMinRAInterval,
       "f3L3TrafficIPIfRouterLifeTime": f3L3TrafficIPIfRouterLifeTime,
       "f3L3TrafficIPIfReachableTime": f3L3TrafficIPIfReachableTime,
       "f3L3TrafficIPIfRaDhcpMoreConfigEnabled": f3L3TrafficIPIfRaDhcpMoreConfigEnabled,
       "f3L3TrafficIPIfRaManagedAddressConfigEnabled": f3L3TrafficIPIfRaManagedAddressConfigEnabled,
       "f3L3TrafficIPIfRaRDNSSOptionEnabled": f3L3TrafficIPIfRaRDNSSOptionEnabled,
       "f3L3TrafficIPIfRaRDNSSLifeTime": f3L3TrafficIPIfRaRDNSSLifeTime,
       "f3L3TrafficIPIfRaDNSSList": f3L3TrafficIPIfRaDNSSList,
       "f3L3TrafficIPIfRaDefaultRouterPreference": f3L3TrafficIPIfRaDefaultRouterPreference,
       "f3L3TrafficIPIfDupAddrDetectControl": f3L3TrafficIPIfDupAddrDetectControl,
       "f3L3TrafficIPIfDupAddrDetectTransmits": f3L3TrafficIPIfDupAddrDetectTransmits,
       "f3L3TrafficIPIfDupAddrDetectRetransTimer": f3L3TrafficIPIfDupAddrDetectRetransTimer,
       "f3L3TrafficIPIfMTU": f3L3TrafficIPIfMTU,
       "f3DhcpRelayAgentTrafficIpIfMemberTable": f3DhcpRelayAgentTrafficIpIfMemberTable,
       "f3DhcpRelayAgentTrafficIpIfMemberEntry": f3DhcpRelayAgentTrafficIpIfMemberEntry,
       "f3DhcpRelayAgentTrafficIpIfMemberObject": f3DhcpRelayAgentTrafficIpIfMemberObject,
       "f3DhcpRelayAgentTrafficIpIfMemberStorageType": f3DhcpRelayAgentTrafficIpIfMemberStorageType,
       "f3DhcpRelayAgentTrafficIpIfMemberRowStatus": f3DhcpRelayAgentTrafficIpIfMemberRowStatus,
       "f3VrfTrafficIpIfMemberTable": f3VrfTrafficIpIfMemberTable,
       "f3VrfTrafficIpIfMemberEntry": f3VrfTrafficIpIfMemberEntry,
       "f3VrfTrafficIpIfMemberObject": f3VrfTrafficIpIfMemberObject,
       "f3VrfTrafficIpIfMemberStorageType": f3VrfTrafficIpIfMemberStorageType,
       "f3VrfTrafficIpIfMemberRowStatus": f3VrfTrafficIpIfMemberRowStatus,
       "f3L3TrafficIpv4RouteTable": f3L3TrafficIpv4RouteTable,
       "f3L3TrafficIpv4RouteEntry": f3L3TrafficIpv4RouteEntry,
       "f3L3TrafficIpv4RouteDest": f3L3TrafficIpv4RouteDest,
       "f3L3TrafficIpv4RouteMask": f3L3TrafficIpv4RouteMask,
       "f3L3TrafficIpv4RouteNextHop": f3L3TrafficIpv4RouteNextHop,
       "f3L3TrafficIpv4RouteMetric": f3L3TrafficIpv4RouteMetric,
       "f3L3TrafficIpv4RouteInterface": f3L3TrafficIpv4RouteInterface,
       "f3L3TrafficIpv4RouteAdvertise": f3L3TrafficIpv4RouteAdvertise,
       "f3L3TrafficIpv4RouteStatus": f3L3TrafficIpv4RouteStatus,
       "f3L3TrafficIpv4RouteSourceForwardingEnable": f3L3TrafficIpv4RouteSourceForwardingEnable,
       "f3L3TrafficIpv4RouteFlags": f3L3TrafficIpv4RouteFlags,
       "f3L3TrafficIpv4RouteStorageType": f3L3TrafficIpv4RouteStorageType,
       "f3L3TrafficIpv4RouteRowStatus": f3L3TrafficIpv4RouteRowStatus,
       "f3L3TrafficIpv4RouteType": f3L3TrafficIpv4RouteType,
       "f3L3TrafficIpv4RouteStatusX": f3L3TrafficIpv4RouteStatusX,
       "f3L3TrafficIpv4RouteOrigin": f3L3TrafficIpv4RouteOrigin,
       "f3L3TrafficArpTable": f3L3TrafficArpTable,
       "f3L3TrafficArpEntry": f3L3TrafficArpEntry,
       "f3L3TrafficArpIPAddress": f3L3TrafficArpIPAddress,
       "f3L3TrafficArpMacAddress": f3L3TrafficArpMacAddress,
       "f3L3TrafficArpInterface": f3L3TrafficArpInterface,
       "f3L3TrafficArpEntryType": f3L3TrafficArpEntryType,
       "f3L3TrafficArpStorageType": f3L3TrafficArpStorageType,
       "f3L3TrafficArpRowStatus": f3L3TrafficArpRowStatus,
       "f3L3TrafficBgpRouterTable": f3L3TrafficBgpRouterTable,
       "f3L3TrafficBgpRouterEntry": f3L3TrafficBgpRouterEntry,
       "f3L3TrafficBgpRouterIndex": f3L3TrafficBgpRouterIndex,
       "f3L3TrafficBgpRouterAdminState": f3L3TrafficBgpRouterAdminState,
       "f3L3TrafficBgpRouterSecondaryState": f3L3TrafficBgpRouterSecondaryState,
       "f3L3TrafficBgpRouterOperationalState": f3L3TrafficBgpRouterOperationalState,
       "f3L3TrafficBgpRouterId": f3L3TrafficBgpRouterId,
       "f3L3TrafficBgpRouterAsNumber": f3L3TrafficBgpRouterAsNumber,
       "f3L3TrafficBgpRouterConnectedRoutesRedistControl": f3L3TrafficBgpRouterConnectedRoutesRedistControl,
       "f3L3TrafficBgpRouterOspfRoutesRedistControl": f3L3TrafficBgpRouterOspfRoutesRedistControl,
       "f3L3TrafficBgpRouterStaticRoutesRedistControl": f3L3TrafficBgpRouterStaticRoutesRedistControl,
       "f3L3TrafficBgpRouterDhcpRoutesRedistControl": f3L3TrafficBgpRouterDhcpRoutesRedistControl,
       "f3L3TrafficBgpRouterStorageType": f3L3TrafficBgpRouterStorageType,
       "f3L3TrafficBgpRouterRowStatus": f3L3TrafficBgpRouterRowStatus,
       "f3L3TrafficBgpRouterAction": f3L3TrafficBgpRouterAction,
       "f3L3TrafficBgpRouterIBgpAdminDistance": f3L3TrafficBgpRouterIBgpAdminDistance,
       "f3L3TrafficBgpRouterEBgpAdminDistance": f3L3TrafficBgpRouterEBgpAdminDistance,
       "f3L3TrafficBgpRouterEcmpMaximumPaths": f3L3TrafficBgpRouterEcmpMaximumPaths,
       "f3L3TrafficBgpRouterRestartTime": f3L3TrafficBgpRouterRestartTime,
       "f3L3TrafficBgpRouterStaleRoutesTime": f3L3TrafficBgpRouterStaleRoutesTime,
       "f3L3TrafficBgpRouteTable": f3L3TrafficBgpRouteTable,
       "f3L3TrafficBgpRouteEntry": f3L3TrafficBgpRouteEntry,
       "f3L3TrafficBgpRouteNetwork": f3L3TrafficBgpRouteNetwork,
       "f3L3TrafficBgpRouteMetric": f3L3TrafficBgpRouteMetric,
       "f3L3TrafficBgpRouteNextHop": f3L3TrafficBgpRouteNextHop,
       "f3L3TrafficBgpRoutePath": f3L3TrafficBgpRoutePath,
       "f3L3TrafficBgpPeerTable": f3L3TrafficBgpPeerTable,
       "f3L3TrafficBgpPeerEntry": f3L3TrafficBgpPeerEntry,
       "f3L3TrafficBgpPeerIndex": f3L3TrafficBgpPeerIndex,
       "f3L3TrafficBgpPeerAdminState": f3L3TrafficBgpPeerAdminState,
       "f3L3TrafficBgpPeerSecondaryState": f3L3TrafficBgpPeerSecondaryState,
       "f3L3TrafficBgpPeerOperationalState": f3L3TrafficBgpPeerOperationalState,
       "f3L3TrafficBgpPeerIpv4Addr": f3L3TrafficBgpPeerIpv4Addr,
       "f3L3TrafficBgpPeerAsNumber": f3L3TrafficBgpPeerAsNumber,
       "f3L3TrafficBgpPeerDescription": f3L3TrafficBgpPeerDescription,
       "f3L3TrafficBgpPeerBgpSessionState": f3L3TrafficBgpPeerBgpSessionState,
       "f3L3TrafficBgpPeerHoldTime": f3L3TrafficBgpPeerHoldTime,
       "f3L3TrafficBgpPeerStartupHoldTime": f3L3TrafficBgpPeerStartupHoldTime,
       "f3L3TrafficBgpPeerKeepAliveTime": f3L3TrafficBgpPeerKeepAliveTime,
       "f3L3TrafficBgpPeerConnectRetryTime": f3L3TrafficBgpPeerConnectRetryTime,
       "f3L3TrafficBgpPeerUpdateSourceIp": f3L3TrafficBgpPeerUpdateSourceIp,
       "f3L3TrafficBgpPeerAuthenticationKey": f3L3TrafficBgpPeerAuthenticationKey,
       "f3L3TrafficBgpPeerTimeSinceUpTransition": f3L3TrafficBgpPeerTimeSinceUpTransition,
       "f3L3TrafficBgpPeerTimeSinceDownTransition": f3L3TrafficBgpPeerTimeSinceDownTransition,
       "f3L3TrafficBgpPeerStorageType": f3L3TrafficBgpPeerStorageType,
       "f3L3TrafficBgpPeerRowStatus": f3L3TrafficBgpPeerRowStatus,
       "f3L3TrafficBgpPeerIpVersion": f3L3TrafficBgpPeerIpVersion,
       "f3L3TrafficBgpPeerIpv6Address": f3L3TrafficBgpPeerIpv6Address,
       "f3L3TrafficBgpPeerUpdateSourceIpv6": f3L3TrafficBgpPeerUpdateSourceIpv6,
       "f3L3TrafficBgpPeerMultihopControl": f3L3TrafficBgpPeerMultihopControl,
       "f3L3TrafficBgpPeerMultihopTtl": f3L3TrafficBgpPeerMultihopTtl,
       "f3L3TrafficBgpPeerUpdateSourceInterface": f3L3TrafficBgpPeerUpdateSourceInterface,
       "f3L3TrafficBgpPeerUpdateSourceType": f3L3TrafficBgpPeerUpdateSourceType,
       "f3L3TrafficBgpPeerLocalPreference": f3L3TrafficBgpPeerLocalPreference,
       "f3L3TrafficBgpPeerRouteReflectorClient": f3L3TrafficBgpPeerRouteReflectorClient,
       "f3L3TrafficBgpPeerRouteReflectorClusterId": f3L3TrafficBgpPeerRouteReflectorClusterId,
       "f3L3TrafficBgpPeerBgpRouteInboundFilter": f3L3TrafficBgpPeerBgpRouteInboundFilter,
       "f3L3TrafficBgpPeerBgpRouteOutboundFilter": f3L3TrafficBgpPeerBgpRouteOutboundFilter,
       "f3L3TrafficBgpPeerBgpGracefulRestart": f3L3TrafficBgpPeerBgpGracefulRestart,
       "f3L3TrafficBgpPeerPeerRestartTime": f3L3TrafficBgpPeerPeerRestartTime,
       "f3L3TrafficBgpPeerPeerRestarting": f3L3TrafficBgpPeerPeerRestarting,
       "f3VrfOspfRouterTable": f3VrfOspfRouterTable,
       "f3VrfOspfRouterEntry": f3VrfOspfRouterEntry,
       "f3VrfOspfRouterIndex": f3VrfOspfRouterIndex,
       "f3VrfOspfRouterAdminState": f3VrfOspfRouterAdminState,
       "f3VrfOspfRouterSecondaryState": f3VrfOspfRouterSecondaryState,
       "f3VrfOspfRouterOperationalState": f3VrfOspfRouterOperationalState,
       "f3VrfOspfRouterId": f3VrfOspfRouterId,
       "f3VrfOspfRouterDescription": f3VrfOspfRouterDescription,
       "f3VrfOspfRouterBgpRoutesRedistributeToOspf": f3VrfOspfRouterBgpRoutesRedistributeToOspf,
       "f3VrfOspfRouterBgpRoutesMetricType": f3VrfOspfRouterBgpRoutesMetricType,
       "f3VrfOspfRouterBgpRoutesMetric": f3VrfOspfRouterBgpRoutesMetric,
       "f3VrfOspfRouterStaticRoutesRedistributeToOspf": f3VrfOspfRouterStaticRoutesRedistributeToOspf,
       "f3VrfOspfRouterStaticRoutesMetricType": f3VrfOspfRouterStaticRoutesMetricType,
       "f3VrfOspfRouterStaticRoutesMetric": f3VrfOspfRouterStaticRoutesMetric,
       "f3VrfOspfRouterConnectedRoutesRedistributeToOspf": f3VrfOspfRouterConnectedRoutesRedistributeToOspf,
       "f3VrfOspfRouterConnectedRoutesMetricType": f3VrfOspfRouterConnectedRoutesMetricType,
       "f3VrfOspfRouterConnectedRoutesMetric": f3VrfOspfRouterConnectedRoutesMetric,
       "f3VrfOspfRouterDhcpRoutesRedistributeToOspf": f3VrfOspfRouterDhcpRoutesRedistributeToOspf,
       "f3VrfOspfRouterDhcpRoutesMetricType": f3VrfOspfRouterDhcpRoutesMetricType,
       "f3VrfOspfRouterDhcpRoutesMetric": f3VrfOspfRouterDhcpRoutesMetric,
       "f3VrfOspfRouterIsAbr": f3VrfOspfRouterIsAbr,
       "f3VrfOspfRouterIsAsbr": f3VrfOspfRouterIsAsbr,
       "f3VrfOspfRouterStorageType": f3VrfOspfRouterStorageType,
       "f3VrfOspfRouterRowStatus": f3VrfOspfRouterRowStatus,
       "f3VrfOspfRouterAction": f3VrfOspfRouterAction,
       "f3VrfOspfRouterVersion": f3VrfOspfRouterVersion,
       "f3VrfOspfRouterAdministrativeDistance": f3VrfOspfRouterAdministrativeDistance,
       "f3VrfOspfRouterSlaacRoutesRedistributeToOspf": f3VrfOspfRouterSlaacRoutesRedistributeToOspf,
       "f3VrfOspfRouterSlaacRoutesMetricType": f3VrfOspfRouterSlaacRoutesMetricType,
       "f3VrfOspfRouterSlaacRoutesMetric": f3VrfOspfRouterSlaacRoutesMetric,
       "f3VrfOspfRouterEcmpMaximumPaths": f3VrfOspfRouterEcmpMaximumPaths,
       "f3VrfOspfRouterSrControl": f3VrfOspfRouterSrControl,
       "f3VrfOspfRouterConvergenceTime": f3VrfOspfRouterConvergenceTime,
       "f3L3TrafficOspfAreaTable": f3L3TrafficOspfAreaTable,
       "f3L3TrafficOspfAreaEntry": f3L3TrafficOspfAreaEntry,
       "f3L3TrafficOspfAreaIndex": f3L3TrafficOspfAreaIndex,
       "f3L3TrafficOspfAreaType": f3L3TrafficOspfAreaType,
       "f3L3TrafficOspfAreaDefaultCost": f3L3TrafficOspfAreaDefaultCost,
       "f3L3TrafficOspfAreaId": f3L3TrafficOspfAreaId,
       "f3L3TrafficOspfAreaStorageType": f3L3TrafficOspfAreaStorageType,
       "f3L3TrafficOspfAreaRowStatus": f3L3TrafficOspfAreaRowStatus,
       "f3L3TrafficOspfAreaAuthType": f3L3TrafficOspfAreaAuthType,
       "f3L3TrafficOspfAreaSimpleAuthKey": f3L3TrafficOspfAreaSimpleAuthKey,
       "f3L3TrafficOspfAreaCryptoKeyId": f3L3TrafficOspfAreaCryptoKeyId,
       "f3L3TrafficOspfAreaIfMemberTable": f3L3TrafficOspfAreaIfMemberTable,
       "f3L3TrafficOspfAreaIfMemberEntry": f3L3TrafficOspfAreaIfMemberEntry,
       "f3L3TrafficOspfAreaIfMemberObject": f3L3TrafficOspfAreaIfMemberObject,
       "f3L3TrafficOspfAreaIfMemberStorageType": f3L3TrafficOspfAreaIfMemberStorageType,
       "f3L3TrafficOspfAreaIfMemberRowStatus": f3L3TrafficOspfAreaIfMemberRowStatus,
       "f3VrfLoopbackInterfaceTable": f3VrfLoopbackInterfaceTable,
       "f3VrfLoopbackInterfaceEntry": f3VrfLoopbackInterfaceEntry,
       "f3VrfLoopbackInterfaceIndex": f3VrfLoopbackInterfaceIndex,
       "f3VrfLoopbackInterfaceName": f3VrfLoopbackInterfaceName,
       "f3VrfLoopbackInterfaceIpAddress": f3VrfLoopbackInterfaceIpAddress,
       "f3VrfLoopbackInterfaceNetMask": f3VrfLoopbackInterfaceNetMask,
       "f3VrfLoopbackInterfaceCIRLo": f3VrfLoopbackInterfaceCIRLo,
       "f3VrfLoopbackInterfaceCIRHi": f3VrfLoopbackInterfaceCIRHi,
       "f3VrfLoopbackInterfaceStorageType": f3VrfLoopbackInterfaceStorageType,
       "f3VrfLoopbackInterfaceRowStatus": f3VrfLoopbackInterfaceRowStatus,
       "f3VrfLoopbackInterfaceIpMode": f3VrfLoopbackInterfaceIpMode,
       "f3VrfLoopbackInterfaceIpv6Address": f3VrfLoopbackInterfaceIpv6Address,
       "f3VrfLoopbackInterfaceIpv6AddrPrefixLen": f3VrfLoopbackInterfaceIpv6AddrPrefixLen,
       "f3L3TrafficOspfAsLsDbTable": f3L3TrafficOspfAsLsDbTable,
       "f3L3TrafficOspfAsLsDbEntry": f3L3TrafficOspfAsLsDbEntry,
       "f3L3TrafficOspfAsLsDbType": f3L3TrafficOspfAsLsDbType,
       "f3L3TrafficOspfAsLsDbId": f3L3TrafficOspfAsLsDbId,
       "f3L3TrafficOspfAsLsDbRouterId": f3L3TrafficOspfAsLsDbRouterId,
       "f3L3TrafficOspfAsLsDbChecksum": f3L3TrafficOspfAsLsDbChecksum,
       "f3L3TrafficOspfAsLsDbSeqNum": f3L3TrafficOspfAsLsDbSeqNum,
       "f3L3TrafficOspfAsLsDbAge": f3L3TrafficOspfAsLsDbAge,
       "f3L3TrafficOspfLsDbTable": f3L3TrafficOspfLsDbTable,
       "f3L3TrafficOspfLsDbEntry": f3L3TrafficOspfLsDbEntry,
       "f3L3TrafficOspfLsDbType": f3L3TrafficOspfLsDbType,
       "f3L3TrafficOspfLsDbId": f3L3TrafficOspfLsDbId,
       "f3L3TrafficOspfLsDbRouterId": f3L3TrafficOspfLsDbRouterId,
       "f3L3TrafficOspfLsDbAreaId": f3L3TrafficOspfLsDbAreaId,
       "f3L3TrafficOspfLsDbChecksum": f3L3TrafficOspfLsDbChecksum,
       "f3L3TrafficOspfLsDbSeqNum": f3L3TrafficOspfLsDbSeqNum,
       "f3L3TrafficOspfLsDbAge": f3L3TrafficOspfLsDbAge,
       "f3L3TrafficOspfNeighborTable": f3L3TrafficOspfNeighborTable,
       "f3L3TrafficOspfNeighborEntry": f3L3TrafficOspfNeighborEntry,
       "f3L3TrafficOspfNeighborIpAddress": f3L3TrafficOspfNeighborIpAddress,
       "f3L3TrafficOspfNeighborInterface": f3L3TrafficOspfNeighborInterface,
       "f3L3TrafficOspfNeighborRouterId": f3L3TrafficOspfNeighborRouterId,
       "f3L3TrafficOspfNeighborState": f3L3TrafficOspfNeighborState,
       "f3L3TrafficOspfNeighborRole": f3L3TrafficOspfNeighborRole,
       "f3L3TrafficOspfNeighborPriority": f3L3TrafficOspfNeighborPriority,
       "f3L3TrafficOspfNeighborDeadTime": f3L3TrafficOspfNeighborDeadTime,
       "f3L3TrafficOspfNeighborLocalInterfaceName": f3L3TrafficOspfNeighborLocalInterfaceName,
       "f3L3TrafficIPInterfaceOspfTable": f3L3TrafficIPInterfaceOspfTable,
       "f3L3TrafficIPInterfaceOspfEntry": f3L3TrafficIPInterfaceOspfEntry,
       "f3L3TrafficIPIfOspfAreaId": f3L3TrafficIPIfOspfAreaId,
       "f3L3TrafficIPIfOspfCost": f3L3TrafficIPIfOspfCost,
       "f3L3TrafficIPIfOspfIfType": f3L3TrafficIPIfOspfIfType,
       "f3L3TrafficIPIfOspfRtrPriority": f3L3TrafficIPIfOspfRtrPriority,
       "f3L3TrafficIPIfOspfHelloInterval": f3L3TrafficIPIfOspfHelloInterval,
       "f3L3TrafficIPIfOspfDeadInterval": f3L3TrafficIPIfOspfDeadInterval,
       "f3L3TrafficIPIfOspfTransmitDelay": f3L3TrafficIPIfOspfTransmitDelay,
       "f3L3TrafficIPIfOspfRetransmitInterval": f3L3TrafficIPIfOspfRetransmitInterval,
       "f3L3TrafficIPIfOspfState": f3L3TrafficIPIfOspfState,
       "f3L3TrafficIPIfOspfDesignatedRouterId": f3L3TrafficIPIfOspfDesignatedRouterId,
       "f3L3TrafficIPIfOspfBackupDesignatedRouterId": f3L3TrafficIPIfOspfBackupDesignatedRouterId,
       "f3L3TrafficIPIfOspfAuthType": f3L3TrafficIPIfOspfAuthType,
       "f3L3TrafficIPIfOspfSimpleAuthKey": f3L3TrafficIPIfOspfSimpleAuthKey,
       "f3L3TrafficIPIfospfCryptoKeyId": f3L3TrafficIPIfospfCryptoKeyId,
       "f3L3TrafficIPv6InterfaceTable": f3L3TrafficIPv6InterfaceTable,
       "f3L3TrafficIPv6InterfaceEntry": f3L3TrafficIPv6InterfaceEntry,
       "f3L3TrafficIPv6IfIndex": f3L3TrafficIPv6IfIndex,
       "f3L3TrafficIPv6IfName": f3L3TrafficIPv6IfName,
       "f3L3TrafficIPv6IfAdminState": f3L3TrafficIPv6IfAdminState,
       "f3L3TrafficIPv6IfSecondaryState": f3L3TrafficIPv6IfSecondaryState,
       "f3L3TrafficIPv6IfOperationalState": f3L3TrafficIPv6IfOperationalState,
       "f3L3TrafficIPv6IfType": f3L3TrafficIPv6IfType,
       "f3L3TrafficIPv6IfLinkLocalAddr": f3L3TrafficIPv6IfLinkLocalAddr,
       "f3L3TrafficIPv6IfLinkLocalAddrMode": f3L3TrafficIPv6IfLinkLocalAddrMode,
       "f3L3TrafficIPv6IfMtu": f3L3TrafficIPv6IfMtu,
       "f3L3TrafficIPv6IfStatelessAddrAutoconfigEnabled": f3L3TrafficIPv6IfStatelessAddrAutoconfigEnabled,
       "f3L3TrafficIPv6IfDefaultGateway": f3L3TrafficIPv6IfDefaultGateway,
       "f3L3TrafficIPv6IfIcmpErrorMsgRateLimit": f3L3TrafficIPv6IfIcmpErrorMsgRateLimit,
       "f3L3TrafficIPv6IfDhcpRole": f3L3TrafficIPv6IfDhcpRole,
       "f3L3TrafficIPv6IfDhcpEnabled": f3L3TrafficIPv6IfDhcpEnabled,
       "f3L3TrafficIPv6IfDhcpRapidCommitControlEnabled": f3L3TrafficIPv6IfDhcpRapidCommitControlEnabled,
       "f3L3TrafficIPv6IfMaxRAInterval": f3L3TrafficIPv6IfMaxRAInterval,
       "f3L3TrafficIPv6IfMinRAInterval": f3L3TrafficIPv6IfMinRAInterval,
       "f3L3TrafficIPv6IfRouterLifeTime": f3L3TrafficIPv6IfRouterLifeTime,
       "f3L3TrafficIPv6IfReachableTime": f3L3TrafficIPv6IfReachableTime,
       "f3L3TrafficIPv6IfRaDhcpMoreConfigEnabled": f3L3TrafficIPv6IfRaDhcpMoreConfigEnabled,
       "f3L3TrafficIPv6IfRaManagedAddressConfigEnabled": f3L3TrafficIPv6IfRaManagedAddressConfigEnabled,
       "f3L3TrafficIPv6IfRaRDNSSOptionEnabled": f3L3TrafficIPv6IfRaRDNSSOptionEnabled,
       "f3L3TrafficIPv6IfRaRDNSSLifeTime": f3L3TrafficIPv6IfRaRDNSSLifeTime,
       "f3L3TrafficIPv6IfRaDNSSList": f3L3TrafficIPv6IfRaDNSSList,
       "f3L3TrafficIPv6IfRaDefaultRouterPreference": f3L3TrafficIPv6IfRaDefaultRouterPreference,
       "f3L3TrafficIPv6IfDupAddrDetectControl": f3L3TrafficIPv6IfDupAddrDetectControl,
       "f3L3TrafficIPv6IfDupAddrDetectTransmits": f3L3TrafficIPv6IfDupAddrDetectTransmits,
       "f3L3TrafficIPv6IfDupAddrDetectRetransTimer": f3L3TrafficIPv6IfDupAddrDetectRetransTimer,
       "f3L3TrafficIPv6IfStorageType": f3L3TrafficIPv6IfStorageType,
       "f3L3TrafficIPv6IfRowStatus": f3L3TrafficIPv6IfRowStatus,
       "f3L3TrafficIPv6IfAction": f3L3TrafficIPv6IfAction,
       "f3L3TrafficIPv6AddressTable": f3L3TrafficIPv6AddressTable,
       "f3L3TrafficIPv6AddressEntry": f3L3TrafficIPv6AddressEntry,
       "f3L3TrafficIPv6AddrIndex": f3L3TrafficIPv6AddrIndex,
       "f3L3TrafficIPv6AddrAssignMode": f3L3TrafficIPv6AddrAssignMode,
       "f3L3TrafficIPv6AddrUnicastAddr": f3L3TrafficIPv6AddrUnicastAddr,
       "f3L3TrafficIPv6AddrUnicastAddrPrefixLength": f3L3TrafficIPv6AddrUnicastAddrPrefixLength,
       "f3L3TrafficIPv6AddrUnicastAddrAutoGenPrefix": f3L3TrafficIPv6AddrUnicastAddrAutoGenPrefix,
       "f3L3TrafficIPv6AddrStorageType": f3L3TrafficIPv6AddrStorageType,
       "f3L3TrafficIPv6AddrRowStatus": f3L3TrafficIPv6AddrRowStatus,
       "f3L3TrafficIPv6PrefixTable": f3L3TrafficIPv6PrefixTable,
       "f3L3TrafficIPv6PrefixEntry": f3L3TrafficIPv6PrefixEntry,
       "f3L3TrafficIPv6PrefixIndex": f3L3TrafficIPv6PrefixIndex,
       "f3L3TrafficIPv6PrefixRaPrefixAdvEnabled": f3L3TrafficIPv6PrefixRaPrefixAdvEnabled,
       "f3L3TrafficIPv6PrefixRaPrefix": f3L3TrafficIPv6PrefixRaPrefix,
       "f3L3TrafficIPv6PrefixRaPrefixLength": f3L3TrafficIPv6PrefixRaPrefixLength,
       "f3L3TrafficIPv6PrefixValidLifeTime": f3L3TrafficIPv6PrefixValidLifeTime,
       "f3L3TrafficIPv6PrefixPreferredLifeTime": f3L3TrafficIPv6PrefixPreferredLifeTime,
       "f3L3TrafficIPv6PrefixStorageType": f3L3TrafficIPv6PrefixStorageType,
       "f3L3TrafficIPv6PrefixRowStatus": f3L3TrafficIPv6PrefixRowStatus,
       "f3L3TrafficIPv6NdpTable": f3L3TrafficIPv6NdpTable,
       "f3L3TrafficIPv6NdpEntry": f3L3TrafficIPv6NdpEntry,
       "f3L3TrafficIPv6NdpIPv6Addr": f3L3TrafficIPv6NdpIPv6Addr,
       "f3L3TrafficIPv6NdpInterface": f3L3TrafficIPv6NdpInterface,
       "f3L3TrafficIPv6NdpMacAddress": f3L3TrafficIPv6NdpMacAddress,
       "f3L3TrafficIPv6NdpType": f3L3TrafficIPv6NdpType,
       "f3L3TrafficIPv6NdpReachabilityState": f3L3TrafficIPv6NdpReachabilityState,
       "f3L3TrafficIPv6NdpAge": f3L3TrafficIPv6NdpAge,
       "f3L3TrafficIPv6NdpStorageType": f3L3TrafficIPv6NdpStorageType,
       "f3L3TrafficIPv6NdpRowStatus": f3L3TrafficIPv6NdpRowStatus,
       "f3L3TrafficIpv6RouteTable": f3L3TrafficIpv6RouteTable,
       "f3L3TrafficIpv6RouteEntry": f3L3TrafficIpv6RouteEntry,
       "f3L3TrafficIpv6RouteDest": f3L3TrafficIpv6RouteDest,
       "f3L3TrafficIpv6RoutePrefixLength": f3L3TrafficIpv6RoutePrefixLength,
       "f3L3TrafficIpv6RouteGateway": f3L3TrafficIpv6RouteGateway,
       "f3L3TrafficIpv6RouteInterface": f3L3TrafficIpv6RouteInterface,
       "f3L3TrafficIpv6RouteMetric": f3L3TrafficIpv6RouteMetric,
       "f3L3TrafficIpv6RouteType": f3L3TrafficIpv6RouteType,
       "f3L3TrafficIpv6RouteAdvertise": f3L3TrafficIpv6RouteAdvertise,
       "f3L3TrafficIpv6RouteStatus": f3L3TrafficIpv6RouteStatus,
       "f3L3TrafficIpv6RouteFlags": f3L3TrafficIpv6RouteFlags,
       "f3L3TrafficIpv6RouteOrigin": f3L3TrafficIpv6RouteOrigin,
       "f3L3TrafficIpv6RouteStorageType": f3L3TrafficIpv6RouteStorageType,
       "f3L3TrafficIpv6RouteRowStatus": f3L3TrafficIpv6RouteRowStatus,
       "f3DhcpV6RelayAgentTable": f3DhcpV6RelayAgentTable,
       "f3DhcpV6RelayAgentEntry": f3DhcpV6RelayAgentEntry,
       "f3DhcpV6RelayAgentIndex": f3DhcpV6RelayAgentIndex,
       "f3DhcpV6RelayAgentAlias": f3DhcpV6RelayAgentAlias,
       "f3DhcpV6RelayAgentAdminState": f3DhcpV6RelayAgentAdminState,
       "f3DhcpV6RelayAgentSecondaryState": f3DhcpV6RelayAgentSecondaryState,
       "f3DhcpV6RelayAgentOperationalState": f3DhcpV6RelayAgentOperationalState,
       "f3DhcpV6RelayAgentServerIpAddress": f3DhcpV6RelayAgentServerIpAddress,
       "f3DhcpV6RelayAgentServerIpInteface": f3DhcpV6RelayAgentServerIpInteface,
       "f3DhcpV6RelayAgentStorageType": f3DhcpV6RelayAgentStorageType,
       "f3DhcpV6RelayAgentRowStatus": f3DhcpV6RelayAgentRowStatus,
       "f3DhcpV6RelayAgentClientTrafficIpIfMemberTable": f3DhcpV6RelayAgentClientTrafficIpIfMemberTable,
       "f3DhcpV6RelayAgentClientTrafficIpIfMemberEntry": f3DhcpV6RelayAgentClientTrafficIpIfMemberEntry,
       "f3DhcpV6RelayAgentClientTrafficIpIfMemberObject": f3DhcpV6RelayAgentClientTrafficIpIfMemberObject,
       "f3DhcpV6RelayAgentClientTrafficIpIfMemberStorageType": f3DhcpV6RelayAgentClientTrafficIpIfMemberStorageType,
       "f3DhcpV6RelayAgentClientTrafficIpIfMemberRowStatus": f3DhcpV6RelayAgentClientTrafficIpIfMemberRowStatus,
       "cmL3FlowPointTable": cmL3FlowPointTable,
       "cmL3FlowPointEntry": cmL3FlowPointEntry,
       "cmL3FlowPointPortIndex": cmL3FlowPointPortIndex,
       "cmL3FlowPointIndex": cmL3FlowPointIndex,
       "cmL3FlowPointAlias": cmL3FlowPointAlias,
       "cmL3FlowPointAdminState": cmL3FlowPointAdminState,
       "cmL3FlowPointSecondaryState": cmL3FlowPointSecondaryState,
       "cmL3FlowPointOperationalState": cmL3FlowPointOperationalState,
       "cmL3FlowPointMultiCOSEnabled": cmL3FlowPointMultiCOSEnabled,
       "cmL3FlowPointCOS": cmL3FlowPointCOS,
       "cmL3FlowPointUntaggedMemberShipEnabled": cmL3FlowPointUntaggedMemberShipEnabled,
       "cmL3FlowPointOuterTagMemberShipEnabled": cmL3FlowPointOuterTagMemberShipEnabled,
       "cmL3FlowPointOuterTagMemberShipVlanId": cmL3FlowPointOuterTagMemberShipVlanId,
       "cmL3FlowPointInnerTagMemberShipEnabled": cmL3FlowPointInnerTagMemberShipEnabled,
       "cmL3FlowPointInnerTagMemberShipVlanId": cmL3FlowPointInnerTagMemberShipVlanId,
       "cmL3FlowPointFragmentedPktsFwdEnabled": cmL3FlowPointFragmentedPktsFwdEnabled,
       "cmL3FlowPointHCosMgmtEnabled": cmL3FlowPointHCosMgmtEnabled,
       "cmL3FlowPointHCosGuaranteedBwHi": cmL3FlowPointHCosGuaranteedBwHi,
       "cmL3FlowPointHCosGuaranteedBwLo": cmL3FlowPointHCosGuaranteedBwLo,
       "cmL3FlowPointHCosMaximumBwHi": cmL3FlowPointHCosMaximumBwHi,
       "cmL3FlowPointHCosMaximumBwLo": cmL3FlowPointHCosMaximumBwLo,
       "cmL3FlowPointDscpOverwriteControl": cmL3FlowPointDscpOverwriteControl,
       "cmL3FlowPointPriMapProfile": cmL3FlowPointPriMapProfile,
       "cmL3FlowPointStorageType": cmL3FlowPointStorageType,
       "cmL3FlowPointRowStatus": cmL3FlowPointRowStatus,
       "cmL3FlowPointAclNoMatchDisposition": cmL3FlowPointAclNoMatchDisposition,
       "cmL3FlowPointWfqSegmentationCOS": cmL3FlowPointWfqSegmentationCOS,
       "cmL3FlowPointWfqGroupCOS": cmL3FlowPointWfqGroupCOS,
       "cmL3FlowPointWfqGroupEirLo": cmL3FlowPointWfqGroupEirLo,
       "cmL3FlowPointWfqGroupEirHi": cmL3FlowPointWfqGroupEirHi,
       "cmL3FlowPointEgressShapingType": cmL3FlowPointEgressShapingType,
       "cmL3QosPolicerTable": cmL3QosPolicerTable,
       "cmL3QosPolicerEntry": cmL3QosPolicerEntry,
       "cmL3QosPolicerIndex": cmL3QosPolicerIndex,
       "cmL3QosPolicerAdminState": cmL3QosPolicerAdminState,
       "cmL3QosPolicerOperationalState": cmL3QosPolicerOperationalState,
       "cmL3QosPolicerSecondaryState": cmL3QosPolicerSecondaryState,
       "cmL3QosPolicerCIRLo": cmL3QosPolicerCIRLo,
       "cmL3QosPolicerCIRHi": cmL3QosPolicerCIRHi,
       "cmL3QosPolicerEIRLo": cmL3QosPolicerEIRLo,
       "cmL3QosPolicerEIRHi": cmL3QosPolicerEIRHi,
       "cmL3QosPolicerCBS": cmL3QosPolicerCBS,
       "cmL3QosPolicerEBS": cmL3QosPolicerEBS,
       "cmL3QosPolicerAlgorithm": cmL3QosPolicerAlgorithm,
       "cmL3QosPolicerColorMode": cmL3QosPolicerColorMode,
       "cmL3QosPolicerCouplingFlag": cmL3QosPolicerCouplingFlag,
       "cmL3QosPolicerCIRMaxHi": cmL3QosPolicerCIRMaxHi,
       "cmL3QosPolicerCIRMaxLo": cmL3QosPolicerCIRMaxLo,
       "cmL3QosPolicerEIRMaxHi": cmL3QosPolicerEIRMaxHi,
       "cmL3QosPolicerEIRMaxLo": cmL3QosPolicerEIRMaxLo,
       "cmL3QosPolicerEnvelopeObject": cmL3QosPolicerEnvelopeObject,
       "cmL3QosPolicerRank": cmL3QosPolicerRank,
       "cmL3QosPolicerPolicingEnabled": cmL3QosPolicerPolicingEnabled,
       "cmL3QosPolicerStorageType": cmL3QosPolicerStorageType,
       "cmL3QosPolicerRowStatus": cmL3QosPolicerRowStatus,
       "cmL3QosShaperTable": cmL3QosShaperTable,
       "cmL3QosShaperEntry": cmL3QosShaperEntry,
       "cmL3QosShaperIndex": cmL3QosShaperIndex,
       "cmL3QosShaperAdminState": cmL3QosShaperAdminState,
       "cmL3QosShaperOperationalState": cmL3QosShaperOperationalState,
       "cmL3QosShaperSecondaryState": cmL3QosShaperSecondaryState,
       "cmL3QosShaperCIRLo": cmL3QosShaperCIRLo,
       "cmL3QosShaperCIRHi": cmL3QosShaperCIRHi,
       "cmL3QosShaperEIRLo": cmL3QosShaperEIRLo,
       "cmL3QosShaperEIRHi": cmL3QosShaperEIRHi,
       "cmL3QosShaperBufferSize": cmL3QosShaperBufferSize,
       "cmL3QosShaperCOS": cmL3QosShaperCOS,
       "cmL3QosShaperStorageType": cmL3QosShaperStorageType,
       "cmL3QosShaperRowStatus": cmL3QosShaperRowStatus,
       "cmL3QosShaperWfqWeight": cmL3QosShaperWfqWeight,
       "f3L3TrafficOspfInterfaceTable": f3L3TrafficOspfInterfaceTable,
       "f3L3TrafficOspfInterfaceEntry": f3L3TrafficOspfInterfaceEntry,
       "f3L3TrafficOspfInterfaceIndex": f3L3TrafficOspfInterfaceIndex,
       "f3L3TrafficOspfInterfaceOspfCost": f3L3TrafficOspfInterfaceOspfCost,
       "f3L3TrafficOspfInterfaceType": f3L3TrafficOspfInterfaceType,
       "f3L3TrafficOspfInterfaceOspfRtrPriority": f3L3TrafficOspfInterfaceOspfRtrPriority,
       "f3L3TrafficOspfInterfaceOspfHelloInterval": f3L3TrafficOspfInterfaceOspfHelloInterval,
       "f3L3TrafficOspfInterfaceOspfDeadInterval": f3L3TrafficOspfInterfaceOspfDeadInterval,
       "f3L3TrafficOspfInterfaceOspfTransmitDelay": f3L3TrafficOspfInterfaceOspfTransmitDelay,
       "f3L3TrafficOspfInterfaceOspfRetransmitInterval": f3L3TrafficOspfInterfaceOspfRetransmitInterval,
       "f3L3TrafficOspfInterfaceState": f3L3TrafficOspfInterfaceState,
       "f3L3TrafficOspfInterfaceOspfDesignatedRouterId": f3L3TrafficOspfInterfaceOspfDesignatedRouterId,
       "f3L3TrafficOspfInterfaceOspfBackupDesignatedRouterId": f3L3TrafficOspfInterfaceOspfBackupDesignatedRouterId,
       "f3L3TrafficOspfInterfaceOspfAuthType": f3L3TrafficOspfInterfaceOspfAuthType,
       "f3L3TrafficOspfInterfaceOspfSimpleAuthKey": f3L3TrafficOspfInterfaceOspfSimpleAuthKey,
       "f3L3TrafficOspfInterfaceOspfCryptoKeyId": f3L3TrafficOspfInterfaceOspfCryptoKeyId,
       "f3L3TrafficOspfInterfaceOspfInstanceId": f3L3TrafficOspfInterfaceOspfInstanceId,
       "f3L3TrafficOspfInterfaceId": f3L3TrafficOspfInterfaceId,
       "f3L3TrafficOspfInterfaceLinkLsaSuppression": f3L3TrafficOspfInterfaceLinkLsaSuppression,
       "f3L3TrafficOspfInterfacePassiveControl": f3L3TrafficOspfInterfacePassiveControl,
       "f3L3TrafficOspfInterfaceAssociatedIpInterface": f3L3TrafficOspfInterfaceAssociatedIpInterface,
       "f3L3TrafficOspfInterfaceStorageType": f3L3TrafficOspfInterfaceStorageType,
       "f3L3TrafficOspfInterfaceRowStatus": f3L3TrafficOspfInterfaceRowStatus,
       "f3L3TrafficOspfInterfaceTilfaControl": f3L3TrafficOspfInterfaceTilfaControl,
       "f3L3TrafficOspfInterfaceTilfaProtectionType": f3L3TrafficOspfInterfaceTilfaProtectionType,
       "f3L3TrafficBgpPeerAddressFamilyTable": f3L3TrafficBgpPeerAddressFamilyTable,
       "f3L3TrafficBgpPeerAddressFamilyEntry": f3L3TrafficBgpPeerAddressFamilyEntry,
       "f3L3TrafficBgpPeerAddressFamilyIndex": f3L3TrafficBgpPeerAddressFamilyIndex,
       "f3L3TrafficBgpPeerAddressFamilyName": f3L3TrafficBgpPeerAddressFamilyName,
       "f3L3TrafficBgpPeerAddressFamilyRedistOspfRoute": f3L3TrafficBgpPeerAddressFamilyRedistOspfRoute,
       "f3L3TrafficBgpPeerAddressFamilyRedistConnectedRoute": f3L3TrafficBgpPeerAddressFamilyRedistConnectedRoute,
       "f3L3TrafficBgpPeerAddressFamilyRedistStaticRoute": f3L3TrafficBgpPeerAddressFamilyRedistStaticRoute,
       "f3L3TrafficBgpPeerAddressFamilyRedistDhcpRoute": f3L3TrafficBgpPeerAddressFamilyRedistDhcpRoute,
       "f3L3TrafficBgpPeerAddressFamilyRedistSlaacRoute": f3L3TrafficBgpPeerAddressFamilyRedistSlaacRoute,
       "f3L3TrafficBgpPeerAddressFamilySendDefaultRoute": f3L3TrafficBgpPeerAddressFamilySendDefaultRoute,
       "f3L3TrafficBgpPeerAddressFamilyNextHopType": f3L3TrafficBgpPeerAddressFamilyNextHopType,
       "f3L3TrafficBgpPeerAddressFamilyNextHopIpv4": f3L3TrafficBgpPeerAddressFamilyNextHopIpv4,
       "f3L3TrafficBgpPeerAddressFamilyNextHopIpv6": f3L3TrafficBgpPeerAddressFamilyNextHopIpv6,
       "f3L3TrafficBgpPeerAddressFamilyExtNextHopControl": f3L3TrafficBgpPeerAddressFamilyExtNextHopControl,
       "f3L3TrafficBgpPeerAddressFamilyStorageType": f3L3TrafficBgpPeerAddressFamilyStorageType,
       "f3L3TrafficBgpPeerAddressFamilyRowStatus": f3L3TrafficBgpPeerAddressFamilyRowStatus,
       "f3L3TrafficBgpRIBRouteTable": f3L3TrafficBgpRIBRouteTable,
       "f3L3TrafficBgpRIBRouteEntry": f3L3TrafficBgpRIBRouteEntry,
       "f3L3TrafficBgpRIBRouteIndex": f3L3TrafficBgpRIBRouteIndex,
       "f3L3TrafficBgpRIBRouteNetwork": f3L3TrafficBgpRIBRouteNetwork,
       "f3L3TrafficBgpRIBRouteNextHop": f3L3TrafficBgpRIBRouteNextHop,
       "f3L3TrafficBgpRIBRouteMetric": f3L3TrafficBgpRIBRouteMetric,
       "f3L3TrafficBgpRIBRoutePath": f3L3TrafficBgpRIBRoutePath,
       "f3L3TrafficBgpInRouteTable": f3L3TrafficBgpInRouteTable,
       "f3L3TrafficBgpInRouteEntry": f3L3TrafficBgpInRouteEntry,
       "f3L3TrafficBgpInRouteIndex": f3L3TrafficBgpInRouteIndex,
       "f3L3TrafficBgpInRouteNetwork": f3L3TrafficBgpInRouteNetwork,
       "f3L3TrafficBgpInRouteNextHop": f3L3TrafficBgpInRouteNextHop,
       "f3L3TrafficBgpInRouteMetric": f3L3TrafficBgpInRouteMetric,
       "f3L3TrafficBgpInRoutePath": f3L3TrafficBgpInRoutePath,
       "f3L3TrafficBgpInRouteLocalPreference": f3L3TrafficBgpInRouteLocalPreference,
       "f3L3TrafficBgpRouteV2Table": f3L3TrafficBgpRouteV2Table,
       "f3L3TrafficBgpRouteV2Entry": f3L3TrafficBgpRouteV2Entry,
       "f3L3TrafficBgpRouteV2Index": f3L3TrafficBgpRouteV2Index,
       "f3L3TrafficBgpRouteV2Network": f3L3TrafficBgpRouteV2Network,
       "f3L3TrafficBgpRouteV2NextHop": f3L3TrafficBgpRouteV2NextHop,
       "f3L3TrafficBgpRouteV2Metric": f3L3TrafficBgpRouteV2Metric,
       "f3L3TrafficBgpRouteV2Path": f3L3TrafficBgpRouteV2Path,
       "f3L3TrafficBgpRouteV2LocalPreference": f3L3TrafficBgpRouteV2LocalPreference,
       "f3L3TrafficBgpPeerAddressFamilyAdvPrefixTable": f3L3TrafficBgpPeerAddressFamilyAdvPrefixTable,
       "f3L3TrafficBgpPeerAddressFamilyAdvPrefixEntry": f3L3TrafficBgpPeerAddressFamilyAdvPrefixEntry,
       "f3L3TrafficBgpPeerAddressFamilyAdvPrefix": f3L3TrafficBgpPeerAddressFamilyAdvPrefix,
       "f3L3TrafficBgpPeerAddressFamilyAdvPrefixStorageType": f3L3TrafficBgpPeerAddressFamilyAdvPrefixStorageType,
       "f3L3TrafficBgpPeerAddressFamilyAdvPrefixRowStatus": f3L3TrafficBgpPeerAddressFamilyAdvPrefixRowStatus,
       "f3L3TrafficOspfV3NeighborTable": f3L3TrafficOspfV3NeighborTable,
       "f3L3TrafficOspfV3NeighborEntry": f3L3TrafficOspfV3NeighborEntry,
       "f3L3TrafficOspfV3NeighborRouterId": f3L3TrafficOspfV3NeighborRouterId,
       "f3L3TrafficOspfV3NeighborInterfaceId": f3L3TrafficOspfV3NeighborInterfaceId,
       "f3L3TrafficOspfV3NeighborPriority": f3L3TrafficOspfV3NeighborPriority,
       "f3L3TrafficOspfV3NeighborDeadTime": f3L3TrafficOspfV3NeighborDeadTime,
       "f3L3TrafficOspfV3NeighborLocalInterfaceName": f3L3TrafficOspfV3NeighborLocalInterfaceName,
       "f3L3TrafficOspfV3NeighborState": f3L3TrafficOspfV3NeighborState,
       "f3L3TrafficOspfV3NeighborRole": f3L3TrafficOspfV3NeighborRole,
       "f3L3TrafficOspfV3NeighborIpAddress": f3L3TrafficOspfV3NeighborIpAddress,
       "f3L3TrafficOspfLinkLsDbTable": f3L3TrafficOspfLinkLsDbTable,
       "f3L3TrafficOspfLinkLsDbEntry": f3L3TrafficOspfLinkLsDbEntry,
       "f3L3TrafficOspfLinkLsDbType": f3L3TrafficOspfLinkLsDbType,
       "f3L3TrafficOspfLinkLsDbId": f3L3TrafficOspfLinkLsDbId,
       "f3L3TrafficOspfLinkLsDbAdvRouterId": f3L3TrafficOspfLinkLsDbAdvRouterId,
       "f3L3TrafficOspfLinkLsDbInterfaceId": f3L3TrafficOspfLinkLsDbInterfaceId,
       "f3L3TrafficOspfLinkLsDbInterface": f3L3TrafficOspfLinkLsDbInterface,
       "f3L3TrafficOspfLinkLsDbAreaId": f3L3TrafficOspfLinkLsDbAreaId,
       "f3L3TrafficOspfLinkLsDbChecksum": f3L3TrafficOspfLinkLsDbChecksum,
       "f3L3TrafficOspfLinkLsDbSeqNum": f3L3TrafficOspfLinkLsDbSeqNum,
       "f3L3TrafficOspfLinkLsDbAge": f3L3TrafficOspfLinkLsDbAge,
       "f3L3TrafficOspfLinkLsDbRtrPriority": f3L3TrafficOspfLinkLsDbRtrPriority,
       "f3L3TrafficOspfLinkLsDbLinkLocalAddress": f3L3TrafficOspfLinkLsDbLinkLocalAddress,
       "f3L3TrafficOspfLinkLsDbPrefixList": f3L3TrafficOspfLinkLsDbPrefixList,
       "f3L3TrafficIpv4StaticRouteTable": f3L3TrafficIpv4StaticRouteTable,
       "f3L3TrafficIpv4StaticRouteEntry": f3L3TrafficIpv4StaticRouteEntry,
       "f3L3TrafficIpv4StaticRouteDest": f3L3TrafficIpv4StaticRouteDest,
       "f3L3TrafficIpv4StaticRouteMask": f3L3TrafficIpv4StaticRouteMask,
       "f3L3TrafficIpv4StaticRouteNextHop": f3L3TrafficIpv4StaticRouteNextHop,
       "f3L3TrafficIpv4StaticRouteInterface": f3L3TrafficIpv4StaticRouteInterface,
       "f3L3TrafficIpv4StaticRouteMetric": f3L3TrafficIpv4StaticRouteMetric,
       "f3L3TrafficIpv4StaticRouteSourceForwardingEnable": f3L3TrafficIpv4StaticRouteSourceForwardingEnable,
       "f3L3TrafficIpv4StaticRouteStorageType": f3L3TrafficIpv4StaticRouteStorageType,
       "f3L3TrafficIpv4StaticRouteRowStatus": f3L3TrafficIpv4StaticRouteRowStatus,
       "f3L3TrafficIpv4AllRouteTable": f3L3TrafficIpv4AllRouteTable,
       "f3L3TrafficIpv4AllRouteEntry": f3L3TrafficIpv4AllRouteEntry,
       "f3L3TrafficIpv4AllRouteDest": f3L3TrafficIpv4AllRouteDest,
       "f3L3TrafficIpv4AllRouteMask": f3L3TrafficIpv4AllRouteMask,
       "f3L3TrafficIpv4AllRouteNextHop": f3L3TrafficIpv4AllRouteNextHop,
       "f3L3TrafficIpv4AllRouteInterface": f3L3TrafficIpv4AllRouteInterface,
       "f3L3TrafficIpv4AllRouteOrigin": f3L3TrafficIpv4AllRouteOrigin,
       "f3L3TrafficIpv4AllRouteMetric": f3L3TrafficIpv4AllRouteMetric,
       "f3L3TrafficIpv4AllRouteSourceForwardingEnable": f3L3TrafficIpv4AllRouteSourceForwardingEnable,
       "f3L3TrafficIpv4AllRouteAdminDistance": f3L3TrafficIpv4AllRouteAdminDistance,
       "f3L3TrafficIpv4AllRouteStatus": f3L3TrafficIpv4AllRouteStatus,
       "f3L3TrafficIpv4AllRouteStorageType": f3L3TrafficIpv4AllRouteStorageType,
       "f3L3TrafficIpv4AllRouteRowStatus": f3L3TrafficIpv4AllRouteRowStatus,
       "f3L3TrafficIpv6StaticRouteTable": f3L3TrafficIpv6StaticRouteTable,
       "f3L3TrafficIpv6StaticRouteEntry": f3L3TrafficIpv6StaticRouteEntry,
       "f3L3TrafficIpv6StaticRouteDest": f3L3TrafficIpv6StaticRouteDest,
       "f3L3TrafficIpv6StaticRoutePrefixLength": f3L3TrafficIpv6StaticRoutePrefixLength,
       "f3L3TrafficIpv6StaticRouteNextHop": f3L3TrafficIpv6StaticRouteNextHop,
       "f3L3TrafficIpv6StaticRouteInterface": f3L3TrafficIpv6StaticRouteInterface,
       "f3L3TrafficIpv6StaticRouteMetric": f3L3TrafficIpv6StaticRouteMetric,
       "f3L3TrafficIpv6StaticRouteStorageType": f3L3TrafficIpv6StaticRouteStorageType,
       "f3L3TrafficIpv6StaticRouteRowStatus": f3L3TrafficIpv6StaticRouteRowStatus,
       "f3L3TrafficIpv6AllRouteTable": f3L3TrafficIpv6AllRouteTable,
       "f3L3TrafficIpv6AllRouteEntry": f3L3TrafficIpv6AllRouteEntry,
       "f3L3TrafficIpv6AllRouteDest": f3L3TrafficIpv6AllRouteDest,
       "f3L3TrafficIpv6AllRoutePrefixLength": f3L3TrafficIpv6AllRoutePrefixLength,
       "f3L3TrafficIpv6AllRouteNextHop": f3L3TrafficIpv6AllRouteNextHop,
       "f3L3TrafficIpv6AllRouteInterface": f3L3TrafficIpv6AllRouteInterface,
       "f3L3TrafficIpv6AllRouteOrigin": f3L3TrafficIpv6AllRouteOrigin,
       "f3L3TrafficIpv6AllRouteMetric": f3L3TrafficIpv6AllRouteMetric,
       "f3L3TrafficIpv6AllRouteAdminDistance": f3L3TrafficIpv6AllRouteAdminDistance,
       "f3L3TrafficIpv6AllRouteStatus": f3L3TrafficIpv6AllRouteStatus,
       "f3L3TrafficIpv6AllRouteStorageType": f3L3TrafficIpv6AllRouteStorageType,
       "f3L3TrafficIpv6AllRouteRowStatus": f3L3TrafficIpv6AllRouteRowStatus,
       "f3IpPrefixListTable": f3IpPrefixListTable,
       "f3IpPrefixListEntry": f3IpPrefixListEntry,
       "f3IpPrefixListIndex": f3IpPrefixListIndex,
       "f3IpPrefixListName": f3IpPrefixListName,
       "f3IpPrefixListDefaultDisposition": f3IpPrefixListDefaultDisposition,
       "f3IpPrefixListStorageType": f3IpPrefixListStorageType,
       "f3IpPrefixListRowStatus": f3IpPrefixListRowStatus,
       "f3IpPrefixTable": f3IpPrefixTable,
       "f3IpPrefixEntry": f3IpPrefixEntry,
       "f3IpPrefixIndex": f3IpPrefixIndex,
       "f3IpPrefix": f3IpPrefix,
       "f3IpPrefixPriority": f3IpPrefixPriority,
       "f3IpPrefixDisposition": f3IpPrefixDisposition,
       "f3IpPrefixLessOrEqualPrefixLen": f3IpPrefixLessOrEqualPrefixLen,
       "f3IpPrefixGreaterOrEqualPrefixLen": f3IpPrefixGreaterOrEqualPrefixLen,
       "f3IpPrefixStorageType": f3IpPrefixStorageType,
       "f3IpPrefixRowStatus": f3IpPrefixRowStatus,
       "f3L3TrafficIPInterfaceRAPrefixTable": f3L3TrafficIPInterfaceRAPrefixTable,
       "f3L3TrafficIPInterfaceRAPrefixEntry": f3L3TrafficIPInterfaceRAPrefixEntry,
       "f3L3TrafficIPInterfaceRAPrefixIndex": f3L3TrafficIPInterfaceRAPrefixIndex,
       "f3L3TrafficIPInterfaceRAPrefixAdvertiseEnabled": f3L3TrafficIPInterfaceRAPrefixAdvertiseEnabled,
       "f3L3TrafficIPInterfaceRAPrefix": f3L3TrafficIPInterfaceRAPrefix,
       "f3L3TrafficIPInterfaceRAPrefixLength": f3L3TrafficIPInterfaceRAPrefixLength,
       "f3L3TrafficIPInterfaceRAPrefixValidLifeTime": f3L3TrafficIPInterfaceRAPrefixValidLifeTime,
       "f3L3TrafficIPInterfaceRAPrefixPreferredLifeTime": f3L3TrafficIPInterfaceRAPrefixPreferredLifeTime,
       "f3L3TrafficIPInterfaceRAPrefixStorageType": f3L3TrafficIPInterfaceRAPrefixStorageType,
       "f3L3TrafficIPInterfaceRAPrefixRowStatus": f3L3TrafficIPInterfaceRAPrefixRowStatus,
       "f3L3TrafficIPInterfaceNdpTable": f3L3TrafficIPInterfaceNdpTable,
       "f3L3TrafficIPInterfaceNdpEntry": f3L3TrafficIPInterfaceNdpEntry,
       "f3L3TrafficIPInterfaceNdpIPv6Addr": f3L3TrafficIPInterfaceNdpIPv6Addr,
       "f3L3TrafficIPInterfaceNdpInterface": f3L3TrafficIPInterfaceNdpInterface,
       "f3L3TrafficIPInterfaceNdpMacAddress": f3L3TrafficIPInterfaceNdpMacAddress,
       "f3L3TrafficIPInterfaceNdpType": f3L3TrafficIPInterfaceNdpType,
       "f3L3TrafficIPInterfaceNdpReachabilityState": f3L3TrafficIPInterfaceNdpReachabilityState,
       "f3L3TrafficIPInterfaceNdpAge": f3L3TrafficIPInterfaceNdpAge,
       "f3L3TrafficIPInterfaceNdpStorageType": f3L3TrafficIPInterfaceNdpStorageType,
       "f3L3TrafficIPInterfaceNdpRowStatus": f3L3TrafficIPInterfaceNdpRowStatus,
       "f3L3TrafficIPInterfaceIPv6AddressTable": f3L3TrafficIPInterfaceIPv6AddressTable,
       "f3L3TrafficIPInterfaceIPv6AddressEntry": f3L3TrafficIPInterfaceIPv6AddressEntry,
       "f3L3TrafficIPInterfaceIPv6AddressIndex": f3L3TrafficIPInterfaceIPv6AddressIndex,
       "f3L3TrafficIPInterfaceIPv6AddressAssignMode": f3L3TrafficIPInterfaceIPv6AddressAssignMode,
       "f3L3TrafficIPInterfaceIPv6AddressUnicastAddr": f3L3TrafficIPInterfaceIPv6AddressUnicastAddr,
       "f3L3TrafficIPInterfaceIPv6AddressUnicastAddrPrefixLength": f3L3TrafficIPInterfaceIPv6AddressUnicastAddrPrefixLength,
       "f3L3TrafficIPInterfaceIPv6AddressUnicastAddrAutoGenPrefix": f3L3TrafficIPInterfaceIPv6AddressUnicastAddrAutoGenPrefix,
       "f3L3TrafficIPInterfaceIPv6AddressStorageType": f3L3TrafficIPInterfaceIPv6AddressStorageType,
       "f3L3TrafficIPInterfaceIPv6AddressRowStatus": f3L3TrafficIPInterfaceIPv6AddressRowStatus,
       "f3L3Performance": f3L3Performance,
       "f3L3FlowPointStatsTable": f3L3FlowPointStatsTable,
       "f3L3FlowPointStatsEntry": f3L3FlowPointStatsEntry,
       "f3L3FlowPointStatsIndex": f3L3FlowPointStatsIndex,
       "f3L3FlowPointStatsIntervalType": f3L3FlowPointStatsIntervalType,
       "f3L3FlowPointStatsValid": f3L3FlowPointStatsValid,
       "f3L3FlowPointStatsAction": f3L3FlowPointStatsAction,
       "f3L3FlowPointStatsFMG": f3L3FlowPointStatsFMG,
       "f3L3FlowPointStatsFMY": f3L3FlowPointStatsFMY,
       "f3L3FlowPointStatsFMRD": f3L3FlowPointStatsFMRD,
       "f3L3FlowPointStatsFTD": f3L3FlowPointStatsFTD,
       "f3L3FlowPointStatsFragmentedDropAcl": f3L3FlowPointStatsFragmentedDropAcl,
       "f3L3FlowPointStatsAclRuleDrop": f3L3FlowPointStatsAclRuleDrop,
       "f3L3FlowPointStatsTtlEqual1Drop": f3L3FlowPointStatsTtlEqual1Drop,
       "f3L3FlowPointStatsFrameTx": f3L3FlowPointStatsFrameTx,
       "f3L3FlowPointStatsFrameRx": f3L3FlowPointStatsFrameRx,
       "f3L3FlowPointStatsNoRouteDrop": f3L3FlowPointStatsNoRouteDrop,
       "f3L3FlowPointStatsHopLimitDrop": f3L3FlowPointStatsHopLimitDrop,
       "f3L3FlowPointHistoryTable": f3L3FlowPointHistoryTable,
       "f3L3FlowPointHistoryEntry": f3L3FlowPointHistoryEntry,
       "f3L3FlowPointHistoryIndex": f3L3FlowPointHistoryIndex,
       "f3L3FlowPointHistoryTime": f3L3FlowPointHistoryTime,
       "f3L3FlowPointHistoryValid": f3L3FlowPointHistoryValid,
       "f3L3FlowPointHistoryAction": f3L3FlowPointHistoryAction,
       "f3L3FlowPointHistoryFMG": f3L3FlowPointHistoryFMG,
       "f3L3FlowPointHistoryFMY": f3L3FlowPointHistoryFMY,
       "f3L3FlowPointHistoryFMRD": f3L3FlowPointHistoryFMRD,
       "f3L3FlowPointHistoryFTD": f3L3FlowPointHistoryFTD,
       "f3L3FlowPointHistoryFragmentedDropAcl": f3L3FlowPointHistoryFragmentedDropAcl,
       "f3L3FlowPointHistoryAclRuleDrop": f3L3FlowPointHistoryAclRuleDrop,
       "f3L3FlowPointHistoryTtlEqual1Drop": f3L3FlowPointHistoryTtlEqual1Drop,
       "f3L3FlowPointHistoryFrameTx": f3L3FlowPointHistoryFrameTx,
       "f3L3FlowPointHistoryFrameRx": f3L3FlowPointHistoryFrameRx,
       "f3L3FlowPointHistoryNoRouteDrop": f3L3FlowPointHistoryNoRouteDrop,
       "f3L3FlowPointHistoryHopLimitDrop": f3L3FlowPointHistoryHopLimitDrop,
       "f3L3FlowPointThresholdTable": f3L3FlowPointThresholdTable,
       "f3L3FlowPointThresholdEntry": f3L3FlowPointThresholdEntry,
       "f3L3FlowPointThresholdIndex": f3L3FlowPointThresholdIndex,
       "f3L3FlowPointThresholdInterval": f3L3FlowPointThresholdInterval,
       "f3L3FlowPointThresholdVariable": f3L3FlowPointThresholdVariable,
       "f3L3FlowPointThresholdValueLo": f3L3FlowPointThresholdValueLo,
       "f3L3FlowPointThresholdValueHi": f3L3FlowPointThresholdValueHi,
       "f3L3FlowPointThresholdMonValue": f3L3FlowPointThresholdMonValue,
       "f3L3TrafficIpInterfaceStatsTable": f3L3TrafficIpInterfaceStatsTable,
       "f3L3TrafficIpInterfaceStatsEntry": f3L3TrafficIpInterfaceStatsEntry,
       "f3L3TrafficIpInterfaceStatsIndex": f3L3TrafficIpInterfaceStatsIndex,
       "f3L3TrafficIpInterfaceStatsIntervalType": f3L3TrafficIpInterfaceStatsIntervalType,
       "f3L3TrafficIpInterfaceStatsValid": f3L3TrafficIpInterfaceStatsValid,
       "f3L3TrafficIpInterfaceStatsAction": f3L3TrafficIpInterfaceStatsAction,
       "f3L3TrafficIpInterfaceStatsDhcpTx": f3L3TrafficIpInterfaceStatsDhcpTx,
       "f3L3TrafficIpInterfaceStatsDhcpRx": f3L3TrafficIpInterfaceStatsDhcpRx,
       "f3L3TrafficIpInterfaceStatsIcmpTx": f3L3TrafficIpInterfaceStatsIcmpTx,
       "f3L3TrafficIpInterfaceStatsIcmpRx": f3L3TrafficIpInterfaceStatsIcmpRx,
       "f3L3TrafficIpInterfaceStatsArpReqTx": f3L3TrafficIpInterfaceStatsArpReqTx,
       "f3L3TrafficIpInterfaceStatsArpReqRx": f3L3TrafficIpInterfaceStatsArpReqRx,
       "f3L3TrafficIpInterfaceStatsArpReplyTx": f3L3TrafficIpInterfaceStatsArpReplyTx,
       "f3L3TrafficIpInterfaceStatsArpReplyRx": f3L3TrafficIpInterfaceStatsArpReplyRx,
       "f3L3TrafficIpInterfaceStatsDhcpV6Tx": f3L3TrafficIpInterfaceStatsDhcpV6Tx,
       "f3L3TrafficIpInterfaceStatsDhcpV6Rx": f3L3TrafficIpInterfaceStatsDhcpV6Rx,
       "f3L3TrafficIpInterfaceStatsIcmpV6WONdpTx": f3L3TrafficIpInterfaceStatsIcmpV6WONdpTx,
       "f3L3TrafficIpInterfaceStatsIcmpV6WONdpRx": f3L3TrafficIpInterfaceStatsIcmpV6WONdpRx,
       "f3L3TrafficIpInterfaceStatsNdpNSTx": f3L3TrafficIpInterfaceStatsNdpNSTx,
       "f3L3TrafficIpInterfaceStatsNdpNSRx": f3L3TrafficIpInterfaceStatsNdpNSRx,
       "f3L3TrafficIpInterfaceStatsNdpNATx": f3L3TrafficIpInterfaceStatsNdpNATx,
       "f3L3TrafficIpInterfaceStatsNdpNARx": f3L3TrafficIpInterfaceStatsNdpNARx,
       "f3L3TrafficIpInterfaceStatsNdpRATx": f3L3TrafficIpInterfaceStatsNdpRATx,
       "f3L3TrafficIpInterfaceStatsNdpRARx": f3L3TrafficIpInterfaceStatsNdpRARx,
       "f3L3TrafficIpInterfaceStatsNdpRSTx": f3L3TrafficIpInterfaceStatsNdpRSTx,
       "f3L3TrafficIpInterfaceStatsNdpRSRx": f3L3TrafficIpInterfaceStatsNdpRSRx,
       "f3L3TrafficIpInterfaceHistoryTable": f3L3TrafficIpInterfaceHistoryTable,
       "f3L3TrafficIpInterfaceHistoryEntry": f3L3TrafficIpInterfaceHistoryEntry,
       "f3L3TrafficIpInterfaceHistoryIndex": f3L3TrafficIpInterfaceHistoryIndex,
       "f3L3TrafficIpInterfaceHistoryTime": f3L3TrafficIpInterfaceHistoryTime,
       "f3L3TrafficIpInterfaceHistoryValid": f3L3TrafficIpInterfaceHistoryValid,
       "f3L3TrafficIpInterfaceHistoryAction": f3L3TrafficIpInterfaceHistoryAction,
       "f3L3TrafficIpInterfaceHistoryDhcpTx": f3L3TrafficIpInterfaceHistoryDhcpTx,
       "f3L3TrafficIpInterfaceHistoryDhcpRx": f3L3TrafficIpInterfaceHistoryDhcpRx,
       "f3L3TrafficIpInterfaceHistoryIcmpTx": f3L3TrafficIpInterfaceHistoryIcmpTx,
       "f3L3TrafficIpInterfaceHistoryIcmpRx": f3L3TrafficIpInterfaceHistoryIcmpRx,
       "f3L3TrafficIpInterfaceHistoryArpReqTx": f3L3TrafficIpInterfaceHistoryArpReqTx,
       "f3L3TrafficIpInterfaceHistoryArpReqRx": f3L3TrafficIpInterfaceHistoryArpReqRx,
       "f3L3TrafficIpInterfaceHistoryArpReplyTx": f3L3TrafficIpInterfaceHistoryArpReplyTx,
       "f3L3TrafficIpInterfaceHistoryArpReplyRx": f3L3TrafficIpInterfaceHistoryArpReplyRx,
       "f3L3TrafficIpInterfaceHistoryDhcpV6Tx": f3L3TrafficIpInterfaceHistoryDhcpV6Tx,
       "f3L3TrafficIpInterfaceHistoryDhcpV6Rx": f3L3TrafficIpInterfaceHistoryDhcpV6Rx,
       "f3L3TrafficIpInterfaceHistoryIcmpV6WONdpTx": f3L3TrafficIpInterfaceHistoryIcmpV6WONdpTx,
       "f3L3TrafficIpInterfaceHistoryIcmpV6WONdpRx": f3L3TrafficIpInterfaceHistoryIcmpV6WONdpRx,
       "f3L3TrafficIpInterfaceHistoryNdpNSTx": f3L3TrafficIpInterfaceHistoryNdpNSTx,
       "f3L3TrafficIpInterfaceHistoryNdpNSRx": f3L3TrafficIpInterfaceHistoryNdpNSRx,
       "f3L3TrafficIpInterfaceHistoryNdpNATx": f3L3TrafficIpInterfaceHistoryNdpNATx,
       "f3L3TrafficIpInterfaceHistoryNdpNARx": f3L3TrafficIpInterfaceHistoryNdpNARx,
       "f3L3TrafficIpInterfaceHistoryNdpRATx": f3L3TrafficIpInterfaceHistoryNdpRATx,
       "f3L3TrafficIpInterfaceHistoryNdpRARx": f3L3TrafficIpInterfaceHistoryNdpRARx,
       "f3L3TrafficIpInterfaceHistoryNdpRSTx": f3L3TrafficIpInterfaceHistoryNdpRSTx,
       "f3L3TrafficIpInterfaceHistoryNdpRSRx": f3L3TrafficIpInterfaceHistoryNdpRSRx,
       "f3L3TrafficIpInterfaceThresholdTable": f3L3TrafficIpInterfaceThresholdTable,
       "f3L3TrafficIpInterfaceThresholdEntry": f3L3TrafficIpInterfaceThresholdEntry,
       "f3L3TrafficIpInterfaceThresholdIndex": f3L3TrafficIpInterfaceThresholdIndex,
       "f3L3TrafficIpInterfaceThresholdInterval": f3L3TrafficIpInterfaceThresholdInterval,
       "f3L3TrafficIpInterfaceThresholdVariable": f3L3TrafficIpInterfaceThresholdVariable,
       "f3L3TrafficIpInterfaceThresholdValueLo": f3L3TrafficIpInterfaceThresholdValueLo,
       "f3L3TrafficIpInterfaceThresholdValueHi": f3L3TrafficIpInterfaceThresholdValueHi,
       "f3L3TrafficIpInterfaceThresholdMonValue": f3L3TrafficIpInterfaceThresholdMonValue,
       "f3L3AclRuleStatsTable": f3L3AclRuleStatsTable,
       "f3L3AclRuleStatsEntry": f3L3AclRuleStatsEntry,
       "f3L3AclRuleStatsIndex": f3L3AclRuleStatsIndex,
       "f3L3AclRuleStatsIntervalType": f3L3AclRuleStatsIntervalType,
       "f3L3AclRuleStatsValid": f3L3AclRuleStatsValid,
       "f3L3AclRuleStatsAction": f3L3AclRuleStatsAction,
       "f3L3AclRuleStatsRuleMatch": f3L3AclRuleStatsRuleMatch,
       "f3L3AclRuleHistoryTable": f3L3AclRuleHistoryTable,
       "f3L3AclRuleHistoryEntry": f3L3AclRuleHistoryEntry,
       "f3L3AclRuleHistoryIndex": f3L3AclRuleHistoryIndex,
       "f3L3AclRuleHistoryTime": f3L3AclRuleHistoryTime,
       "f3L3AclRuleHistoryValid": f3L3AclRuleHistoryValid,
       "f3L3AclRuleHistoryAction": f3L3AclRuleHistoryAction,
       "f3L3AclRuleHistoryRuleMatch": f3L3AclRuleHistoryRuleMatch,
       "f3L3AclRuleThresholdTable": f3L3AclRuleThresholdTable,
       "f3L3AclRuleThresholdEntry": f3L3AclRuleThresholdEntry,
       "f3L3AclRuleThresholdIndex": f3L3AclRuleThresholdIndex,
       "f3L3AclRuleThresholdInterval": f3L3AclRuleThresholdInterval,
       "f3L3AclRuleThresholdVariable": f3L3AclRuleThresholdVariable,
       "f3L3AclRuleThresholdValueLo": f3L3AclRuleThresholdValueLo,
       "f3L3AclRuleThresholdValueHi": f3L3AclRuleThresholdValueHi,
       "f3L3AclRuleThresholdMonValue": f3L3AclRuleThresholdMonValue,
       "f3L3QosPolicerStatsTable": f3L3QosPolicerStatsTable,
       "f3L3QosPolicerStatsEntry": f3L3QosPolicerStatsEntry,
       "f3L3QosPolicerStatsIndex": f3L3QosPolicerStatsIndex,
       "f3L3QosPolicerStatsIntervalType": f3L3QosPolicerStatsIntervalType,
       "f3L3QosPolicerStatsValid": f3L3QosPolicerStatsValid,
       "f3L3QosPolicerStatsAction": f3L3QosPolicerStatsAction,
       "f3L3QosPolicerStatsFMG": f3L3QosPolicerStatsFMG,
       "f3L3QosPolicerStatsFMY": f3L3QosPolicerStatsFMY,
       "f3L3QosPolicerStatsFMYD": f3L3QosPolicerStatsFMYD,
       "f3L3QosPolicerStatsFMRD": f3L3QosPolicerStatsFMRD,
       "f3L3QosPolicerStatsBytesIn": f3L3QosPolicerStatsBytesIn,
       "f3L3QosPolicerStatsBytesOut": f3L3QosPolicerStatsBytesOut,
       "f3L3QosPolicerStatsABR": f3L3QosPolicerStatsABR,
       "f3L3QosPolicerHistoryTable": f3L3QosPolicerHistoryTable,
       "f3L3QosPolicerHistoryEntry": f3L3QosPolicerHistoryEntry,
       "f3L3QosPolicerHistoryIndex": f3L3QosPolicerHistoryIndex,
       "f3L3QosPolicerHistoryTime": f3L3QosPolicerHistoryTime,
       "f3L3QosPolicerHistoryValid": f3L3QosPolicerHistoryValid,
       "f3L3QosPolicerHistoryAction": f3L3QosPolicerHistoryAction,
       "f3L3QosPolicerHistoryFMG": f3L3QosPolicerHistoryFMG,
       "f3L3QosPolicerHistoryFMY": f3L3QosPolicerHistoryFMY,
       "f3L3QosPolicerHistoryFMYD": f3L3QosPolicerHistoryFMYD,
       "f3L3QosPolicerHistoryFMRD": f3L3QosPolicerHistoryFMRD,
       "f3L3QosPolicerHistoryBytesIn": f3L3QosPolicerHistoryBytesIn,
       "f3L3QosPolicerHistoryBytesOut": f3L3QosPolicerHistoryBytesOut,
       "f3L3QosPolicerHistoryABR": f3L3QosPolicerHistoryABR,
       "f3L3QosPolicerThresholdTable": f3L3QosPolicerThresholdTable,
       "f3L3QosPolicerThresholdEntry": f3L3QosPolicerThresholdEntry,
       "f3L3QosPolicerThresholdIndex": f3L3QosPolicerThresholdIndex,
       "f3L3QosPolicerThresholdInterval": f3L3QosPolicerThresholdInterval,
       "f3L3QosPolicerThresholdVariable": f3L3QosPolicerThresholdVariable,
       "f3L3QosPolicerThresholdValueLo": f3L3QosPolicerThresholdValueLo,
       "f3L3QosPolicerThresholdValueHi": f3L3QosPolicerThresholdValueHi,
       "f3L3QosPolicerThresholdMonValue": f3L3QosPolicerThresholdMonValue,
       "f3L3QosShaperStatsTable": f3L3QosShaperStatsTable,
       "f3L3QosShaperStatsEntry": f3L3QosShaperStatsEntry,
       "f3L3QosShaperStatsIndex": f3L3QosShaperStatsIndex,
       "f3L3QosShaperStatsIntervalType": f3L3QosShaperStatsIntervalType,
       "f3L3QosShaperStatsValid": f3L3QosShaperStatsValid,
       "f3L3QosShaperStatsAction": f3L3QosShaperStatsAction,
       "f3L3QosShaperStatsBT": f3L3QosShaperStatsBT,
       "f3L3QosShaperStatsBTD": f3L3QosShaperStatsBTD,
       "f3L3QosShaperStatsFD": f3L3QosShaperStatsFD,
       "f3L3QosShaperStatsFTD": f3L3QosShaperStatsFTD,
       "f3L3QosShaperStatsBR": f3L3QosShaperStatsBR,
       "f3L3QosShaperStatsFR": f3L3QosShaperStatsFR,
       "f3L3QosShaperStatsABRRL": f3L3QosShaperStatsABRRL,
       "f3L3QosShaperStatsABRRLR": f3L3QosShaperStatsABRRLR,
       "f3L3QosShaperStatsBREDD": f3L3QosShaperStatsBREDD,
       "f3L3QosShaperStatsFREDD": f3L3QosShaperStatsFREDD,
       "f3L3QosShaperHistoryTable": f3L3QosShaperHistoryTable,
       "f3L3QosShaperHistoryEntry": f3L3QosShaperHistoryEntry,
       "f3L3QosShaperHistoryIndex": f3L3QosShaperHistoryIndex,
       "f3L3QosShaperHistoryTime": f3L3QosShaperHistoryTime,
       "f3L3QosShaperHistoryValid": f3L3QosShaperHistoryValid,
       "f3L3QosShaperHistoryAction": f3L3QosShaperHistoryAction,
       "f3L3QosShaperHistoryBT": f3L3QosShaperHistoryBT,
       "f3L3QosShaperHistoryBTD": f3L3QosShaperHistoryBTD,
       "f3L3QosShaperHistoryFD": f3L3QosShaperHistoryFD,
       "f3L3QosShaperHistoryFTD": f3L3QosShaperHistoryFTD,
       "f3L3QosShaperHistoryBR": f3L3QosShaperHistoryBR,
       "f3L3QosShaperHistoryFR": f3L3QosShaperHistoryFR,
       "f3L3QosShaperHistoryABRRL": f3L3QosShaperHistoryABRRL,
       "f3L3QosShaperHistoryABRRLR": f3L3QosShaperHistoryABRRLR,
       "f3L3QosShaperHistoryBREDD": f3L3QosShaperHistoryBREDD,
       "f3L3QosShaperHistoryFREDD": f3L3QosShaperHistoryFREDD,
       "f3L3QosShaperThresholdTable": f3L3QosShaperThresholdTable,
       "f3L3QosShaperThresholdEntry": f3L3QosShaperThresholdEntry,
       "f3L3QosShaperThresholdIndex": f3L3QosShaperThresholdIndex,
       "f3L3QosShaperThresholdInterval": f3L3QosShaperThresholdInterval,
       "f3L3QosShaperThresholdVariable": f3L3QosShaperThresholdVariable,
       "f3L3QosShaperThresholdValueLo": f3L3QosShaperThresholdValueLo,
       "f3L3QosShaperThresholdValueHi": f3L3QosShaperThresholdValueHi,
       "f3L3QosShaperThresholdMonValue": f3L3QosShaperThresholdMonValue,
       "f3L2A2NAclRuleStatsTable": f3L2A2NAclRuleStatsTable,
       "f3L2A2NAclRuleStatsEntry": f3L2A2NAclRuleStatsEntry,
       "f3L2A2NAclRuleStatsIndex": f3L2A2NAclRuleStatsIndex,
       "f3L2A2NAclRuleStatsIntervalType": f3L2A2NAclRuleStatsIntervalType,
       "f3L2A2NAclRuleStatsValid": f3L2A2NAclRuleStatsValid,
       "f3L2A2NAclRuleStatsAction": f3L2A2NAclRuleStatsAction,
       "f3L2A2NAclRuleStatsRuleMatch": f3L2A2NAclRuleStatsRuleMatch,
       "f3L2A2NAclRuleHistoryTable": f3L2A2NAclRuleHistoryTable,
       "f3L2A2NAclRuleHistoryEntry": f3L2A2NAclRuleHistoryEntry,
       "f3L2A2NAclRuleHistoryIndex": f3L2A2NAclRuleHistoryIndex,
       "f3L2A2NAclRuleHistoryTime": f3L2A2NAclRuleHistoryTime,
       "f3L2A2NAclRuleHistoryValid": f3L2A2NAclRuleHistoryValid,
       "f3L2A2NAclRuleHistoryAction": f3L2A2NAclRuleHistoryAction,
       "f3L2A2NAclRuleHistoryRuleMatch": f3L2A2NAclRuleHistoryRuleMatch,
       "f3L2A2NAclRuleThresholdTable": f3L2A2NAclRuleThresholdTable,
       "f3L2A2NAclRuleThresholdEntry": f3L2A2NAclRuleThresholdEntry,
       "f3L2A2NAclRuleThresholdIndex": f3L2A2NAclRuleThresholdIndex,
       "f3L2A2NAclRuleThresholdInterval": f3L2A2NAclRuleThresholdInterval,
       "f3L2A2NAclRuleThresholdVariable": f3L2A2NAclRuleThresholdVariable,
       "f3L2A2NAclRuleThresholdValueLo": f3L2A2NAclRuleThresholdValueLo,
       "f3L2A2NAclRuleThresholdValueHi": f3L2A2NAclRuleThresholdValueHi,
       "f3L2A2NAclRuleThresholdMonValue": f3L2A2NAclRuleThresholdMonValue,
       "f3L2N2AAclRuleStatsTable": f3L2N2AAclRuleStatsTable,
       "f3L2N2AAclRuleStatsEntry": f3L2N2AAclRuleStatsEntry,
       "f3L2N2AAclRuleStatsIndex": f3L2N2AAclRuleStatsIndex,
       "f3L2N2AAclRuleStatsIntervalType": f3L2N2AAclRuleStatsIntervalType,
       "f3L2N2AAclRuleStatsValid": f3L2N2AAclRuleStatsValid,
       "f3L2N2AAclRuleStatsAction": f3L2N2AAclRuleStatsAction,
       "f3L2N2AAclRuleStatsRuleMatch": f3L2N2AAclRuleStatsRuleMatch,
       "f3L2N2AAclRuleHistoryTable": f3L2N2AAclRuleHistoryTable,
       "f3L2N2AAclRuleHistoryEntry": f3L2N2AAclRuleHistoryEntry,
       "f3L2N2AAclRuleHistoryIndex": f3L2N2AAclRuleHistoryIndex,
       "f3L2N2AAclRuleHistoryTime": f3L2N2AAclRuleHistoryTime,
       "f3L2N2AAclRuleHistoryValid": f3L2N2AAclRuleHistoryValid,
       "f3L2N2AAclRuleHistoryAction": f3L2N2AAclRuleHistoryAction,
       "f3L2N2AAclRuleHistoryRuleMatch": f3L2N2AAclRuleHistoryRuleMatch,
       "f3L2N2AAclRuleThresholdTable": f3L2N2AAclRuleThresholdTable,
       "f3L2N2AAclRuleThresholdEntry": f3L2N2AAclRuleThresholdEntry,
       "f3L2N2AAclRuleThresholdIndex": f3L2N2AAclRuleThresholdIndex,
       "f3L2N2AAclRuleThresholdInterval": f3L2N2AAclRuleThresholdInterval,
       "f3L2N2AAclRuleThresholdVariable": f3L2N2AAclRuleThresholdVariable,
       "f3L2N2AAclRuleThresholdValueLo": f3L2N2AAclRuleThresholdValueLo,
       "f3L2N2AAclRuleThresholdValueHi": f3L2N2AAclRuleThresholdValueHi,
       "f3L2N2AAclRuleThresholdMonValue": f3L2N2AAclRuleThresholdMonValue,
       "f3L3TrafficIPv6InterfaceStatsTable": f3L3TrafficIPv6InterfaceStatsTable,
       "f3L3TrafficIPv6InterfaceStatsEntry": f3L3TrafficIPv6InterfaceStatsEntry,
       "f3L3TrafficIPv6InterfaceStatsIndex": f3L3TrafficIPv6InterfaceStatsIndex,
       "f3L3TrafficIPv6InterfaceStatsIntervalType": f3L3TrafficIPv6InterfaceStatsIntervalType,
       "f3L3TrafficIPv6InterfaceStatsValid": f3L3TrafficIPv6InterfaceStatsValid,
       "f3L3TrafficIPv6InterfaceStatsAction": f3L3TrafficIPv6InterfaceStatsAction,
       "f3L3TrafficIPv6InterfaceStatsDhcpV6Tx": f3L3TrafficIPv6InterfaceStatsDhcpV6Tx,
       "f3L3TrafficIPv6InterfaceStatsDhcpV6Rx": f3L3TrafficIPv6InterfaceStatsDhcpV6Rx,
       "f3L3TrafficIPv6InterfaceStatsIcmpV6WONdpTx": f3L3TrafficIPv6InterfaceStatsIcmpV6WONdpTx,
       "f3L3TrafficIPv6InterfaceStatsIcmpV6WONdpRx": f3L3TrafficIPv6InterfaceStatsIcmpV6WONdpRx,
       "f3L3TrafficIPv6InterfaceStatsNdpNSTx": f3L3TrafficIPv6InterfaceStatsNdpNSTx,
       "f3L3TrafficIPv6InterfaceStatsNdpNSRx": f3L3TrafficIPv6InterfaceStatsNdpNSRx,
       "f3L3TrafficIPv6InterfaceStatsNdpNATx": f3L3TrafficIPv6InterfaceStatsNdpNATx,
       "f3L3TrafficIPv6InterfaceStatsNdpNARx": f3L3TrafficIPv6InterfaceStatsNdpNARx,
       "f3L3TrafficIPv6InterfaceStatsNdpRATx": f3L3TrafficIPv6InterfaceStatsNdpRATx,
       "f3L3TrafficIPv6InterfaceStatsNdpRARx": f3L3TrafficIPv6InterfaceStatsNdpRARx,
       "f3L3TrafficIPv6InterfaceStatsNdpRSTx": f3L3TrafficIPv6InterfaceStatsNdpRSTx,
       "f3L3TrafficIPv6InterfaceStatsNdpRSRx": f3L3TrafficIPv6InterfaceStatsNdpRSRx,
       "f3L3TrafficIPv6InterfaceHistoryTable": f3L3TrafficIPv6InterfaceHistoryTable,
       "f3L3TrafficIPv6InterfaceHistoryEntry": f3L3TrafficIPv6InterfaceHistoryEntry,
       "f3L3TrafficIPv6InterfaceHistoryIndex": f3L3TrafficIPv6InterfaceHistoryIndex,
       "f3L3TrafficIPv6InterfaceHistoryTime": f3L3TrafficIPv6InterfaceHistoryTime,
       "f3L3TrafficIPv6InterfaceHistoryValid": f3L3TrafficIPv6InterfaceHistoryValid,
       "f3L3TrafficIPv6InterfaceHistoryAction": f3L3TrafficIPv6InterfaceHistoryAction,
       "f3L3TrafficIPv6InterfaceHistoryDhcpV6Tx": f3L3TrafficIPv6InterfaceHistoryDhcpV6Tx,
       "f3L3TrafficIPv6InterfaceHistoryDhcpV6Rx": f3L3TrafficIPv6InterfaceHistoryDhcpV6Rx,
       "f3L3TrafficIPv6InterfaceHistoryIcmpV6WONdpTx": f3L3TrafficIPv6InterfaceHistoryIcmpV6WONdpTx,
       "f3L3TrafficIPv6InterfaceHistoryIcmpV6WONdpRx": f3L3TrafficIPv6InterfaceHistoryIcmpV6WONdpRx,
       "f3L3TrafficIPv6InterfaceHistoryNdpNSTx": f3L3TrafficIPv6InterfaceHistoryNdpNSTx,
       "f3L3TrafficIPv6InterfaceHistoryNdpNSRx": f3L3TrafficIPv6InterfaceHistoryNdpNSRx,
       "f3L3TrafficIPv6InterfaceHistoryNdpNATx": f3L3TrafficIPv6InterfaceHistoryNdpNATx,
       "f3L3TrafficIPv6InterfaceHistoryNdpNARx": f3L3TrafficIPv6InterfaceHistoryNdpNARx,
       "f3L3TrafficIPv6InterfaceHistoryNdpRATx": f3L3TrafficIPv6InterfaceHistoryNdpRATx,
       "f3L3TrafficIPv6InterfaceHistoryNdpRARx": f3L3TrafficIPv6InterfaceHistoryNdpRARx,
       "f3L3TrafficIPv6InterfaceHistoryNdpRSTx": f3L3TrafficIPv6InterfaceHistoryNdpRSTx,
       "f3L3TrafficIPv6InterfaceHistoryNdpRSRx": f3L3TrafficIPv6InterfaceHistoryNdpRSRx,
       "f3L3TrafficIPv6InterfaceThresholdTable": f3L3TrafficIPv6InterfaceThresholdTable,
       "f3L3TrafficIPv6InterfaceThresholdEntry": f3L3TrafficIPv6InterfaceThresholdEntry,
       "f3L3TrafficIPv6InterfaceThresholdIndex": f3L3TrafficIPv6InterfaceThresholdIndex,
       "f3L3TrafficIPv6InterfaceThresholdInterval": f3L3TrafficIPv6InterfaceThresholdInterval,
       "f3L3TrafficIPv6InterfaceThresholdVariable": f3L3TrafficIPv6InterfaceThresholdVariable,
       "f3L3TrafficIPv6InterfaceThresholdValueLo": f3L3TrafficIPv6InterfaceThresholdValueLo,
       "f3L3TrafficIPv6InterfaceThresholdValueHi": f3L3TrafficIPv6InterfaceThresholdValueHi,
       "f3L3TrafficIPv6InterfaceThresholdMonValue": f3L3TrafficIPv6InterfaceThresholdMonValue,
       "cmL3FlowPointStatsTable": cmL3FlowPointStatsTable,
       "cmL3FlowPointStatsEntry": cmL3FlowPointStatsEntry,
       "cmL3FlowPointStatsIndex": cmL3FlowPointStatsIndex,
       "cmL3FlowPointStatsIntervalType": cmL3FlowPointStatsIntervalType,
       "cmL3FlowPointStatsValid": cmL3FlowPointStatsValid,
       "cmL3FlowPointStatsAction": cmL3FlowPointStatsAction,
       "cmL3FlowPointStatsFMG": cmL3FlowPointStatsFMG,
       "cmL3FlowPointStatsFMY": cmL3FlowPointStatsFMY,
       "cmL3FlowPointStatsFMRD": cmL3FlowPointStatsFMRD,
       "cmL3FlowPointStatsFTD": cmL3FlowPointStatsFTD,
       "cmL3FlowPointStatsFragmentedDropAcl": cmL3FlowPointStatsFragmentedDropAcl,
       "cmL3FlowPointStatsAclRuleDrop": cmL3FlowPointStatsAclRuleDrop,
       "cmL3FlowPointStatsTtlEqual1Drop": cmL3FlowPointStatsTtlEqual1Drop,
       "cmL3FlowPointStatsFrameTx": cmL3FlowPointStatsFrameTx,
       "cmL3FlowPointStatsFrameRx": cmL3FlowPointStatsFrameRx,
       "cmL3FlowPointStatsNoRouteDrop": cmL3FlowPointStatsNoRouteDrop,
       "cmL3FlowPointStatsAclDropNoMatch": cmL3FlowPointStatsAclDropNoMatch,
       "cmL3FlowPointHistoryTable": cmL3FlowPointHistoryTable,
       "cmL3FlowPointHistoryEntry": cmL3FlowPointHistoryEntry,
       "cmL3FlowPointHistoryIndex": cmL3FlowPointHistoryIndex,
       "cmL3FlowPointHistoryTime": cmL3FlowPointHistoryTime,
       "cmL3FlowPointHistoryValid": cmL3FlowPointHistoryValid,
       "cmL3FlowPointHistoryAction": cmL3FlowPointHistoryAction,
       "cmL3FlowPointHistoryFMG": cmL3FlowPointHistoryFMG,
       "cmL3FlowPointHistoryFMY": cmL3FlowPointHistoryFMY,
       "cmL3FlowPointHistoryFMRD": cmL3FlowPointHistoryFMRD,
       "cmL3FlowPointHistoryFTD": cmL3FlowPointHistoryFTD,
       "cmL3FlowPointHistoryFragmentedDropAcl": cmL3FlowPointHistoryFragmentedDropAcl,
       "cmL3FlowPointHistoryAclRuleDrop": cmL3FlowPointHistoryAclRuleDrop,
       "cmL3FlowPointHistoryTtlEqual1Drop": cmL3FlowPointHistoryTtlEqual1Drop,
       "cmL3FlowPointHistoryFrameTx": cmL3FlowPointHistoryFrameTx,
       "cmL3FlowPointHistoryFrameRx": cmL3FlowPointHistoryFrameRx,
       "cmL3FlowPointHistoryNoRouteDrop": cmL3FlowPointHistoryNoRouteDrop,
       "cmL3FlowPointHistoryAclDropNoMatch": cmL3FlowPointHistoryAclDropNoMatch,
       "cmL3FlowPointThresholdTable": cmL3FlowPointThresholdTable,
       "cmL3FlowPointThresholdEntry": cmL3FlowPointThresholdEntry,
       "cmL3FlowPointThresholdIndex": cmL3FlowPointThresholdIndex,
       "cmL3FlowPointThresholdInterval": cmL3FlowPointThresholdInterval,
       "cmL3FlowPointThresholdVariable": cmL3FlowPointThresholdVariable,
       "cmL3FlowPointThresholdValueLo": cmL3FlowPointThresholdValueLo,
       "cmL3FlowPointThresholdValueHi": cmL3FlowPointThresholdValueHi,
       "cmL3FlowPointThresholdMonValue": cmL3FlowPointThresholdMonValue,
       "cmL3QosPolicerStatsTable": cmL3QosPolicerStatsTable,
       "cmL3QosPolicerStatsEntry": cmL3QosPolicerStatsEntry,
       "cmL3QosPolicerStatsIndex": cmL3QosPolicerStatsIndex,
       "cmL3QosPolicerStatsIntervalType": cmL3QosPolicerStatsIntervalType,
       "cmL3QosPolicerStatsValid": cmL3QosPolicerStatsValid,
       "cmL3QosPolicerStatsAction": cmL3QosPolicerStatsAction,
       "cmL3QosPolicerStatsFMG": cmL3QosPolicerStatsFMG,
       "cmL3QosPolicerStatsFMY": cmL3QosPolicerStatsFMY,
       "cmL3QosPolicerStatsFMYD": cmL3QosPolicerStatsFMYD,
       "cmL3QosPolicerStatsFMRD": cmL3QosPolicerStatsFMRD,
       "cmL3QosPolicerStatsBytesIn": cmL3QosPolicerStatsBytesIn,
       "cmL3QosPolicerStatsBytesOut": cmL3QosPolicerStatsBytesOut,
       "cmL3QosPolicerStatsABR": cmL3QosPolicerStatsABR,
       "cmL3QosPolicerHistoryTable": cmL3QosPolicerHistoryTable,
       "cmL3QosPolicerHistoryEntry": cmL3QosPolicerHistoryEntry,
       "cmL3QosPolicerHistoryIndex": cmL3QosPolicerHistoryIndex,
       "cmL3QosPolicerHistoryTime": cmL3QosPolicerHistoryTime,
       "cmL3QosPolicerHistoryValid": cmL3QosPolicerHistoryValid,
       "cmL3QosPolicerHistoryAction": cmL3QosPolicerHistoryAction,
       "cmL3QosPolicerHistoryFMG": cmL3QosPolicerHistoryFMG,
       "cmL3QosPolicerHistoryFMY": cmL3QosPolicerHistoryFMY,
       "cmL3QosPolicerHistoryFMYD": cmL3QosPolicerHistoryFMYD,
       "cmL3QosPolicerHistoryFMRD": cmL3QosPolicerHistoryFMRD,
       "cmL3QosPolicerHistoryBytesIn": cmL3QosPolicerHistoryBytesIn,
       "cmL3QosPolicerHistoryBytesOut": cmL3QosPolicerHistoryBytesOut,
       "cmL3QosPolicerHistoryABR": cmL3QosPolicerHistoryABR,
       "cmL3QosPolicerThresholdTable": cmL3QosPolicerThresholdTable,
       "cmL3QosPolicerThresholdEntry": cmL3QosPolicerThresholdEntry,
       "cmL3QosPolicerThresholdIndex": cmL3QosPolicerThresholdIndex,
       "cmL3QosPolicerThresholdInterval": cmL3QosPolicerThresholdInterval,
       "cmL3QosPolicerThresholdVariable": cmL3QosPolicerThresholdVariable,
       "cmL3QosPolicerThresholdValueLo": cmL3QosPolicerThresholdValueLo,
       "cmL3QosPolicerThresholdValueHi": cmL3QosPolicerThresholdValueHi,
       "cmL3QosPolicerThresholdMonValue": cmL3QosPolicerThresholdMonValue,
       "cmL3QosShaperStatsTable": cmL3QosShaperStatsTable,
       "cmL3QosShaperStatsEntry": cmL3QosShaperStatsEntry,
       "cmL3QosShaperStatsIndex": cmL3QosShaperStatsIndex,
       "cmL3QosShaperStatsIntervalType": cmL3QosShaperStatsIntervalType,
       "cmL3QosShaperStatsValid": cmL3QosShaperStatsValid,
       "cmL3QosShaperStatsAction": cmL3QosShaperStatsAction,
       "cmL3QosShaperStatsBT": cmL3QosShaperStatsBT,
       "cmL3QosShaperStatsBTD": cmL3QosShaperStatsBTD,
       "cmL3QosShaperStatsFD": cmL3QosShaperStatsFD,
       "cmL3QosShaperStatsFTD": cmL3QosShaperStatsFTD,
       "cmL3QosShaperStatsBR": cmL3QosShaperStatsBR,
       "cmL3QosShaperStatsFR": cmL3QosShaperStatsFR,
       "cmL3QosShaperStatsABRRL": cmL3QosShaperStatsABRRL,
       "cmL3QosShaperStatsABRRLR": cmL3QosShaperStatsABRRLR,
       "cmL3QosShaperStatsBREDD": cmL3QosShaperStatsBREDD,
       "cmL3QosShaperStatsFREDD": cmL3QosShaperStatsFREDD,
       "cmL3QosShaperHistoryTable": cmL3QosShaperHistoryTable,
       "cmL3QosShaperHistoryEntry": cmL3QosShaperHistoryEntry,
       "cmL3QosShaperHistoryIndex": cmL3QosShaperHistoryIndex,
       "cmL3QosShaperHistoryTime": cmL3QosShaperHistoryTime,
       "cmL3QosShaperHistoryValid": cmL3QosShaperHistoryValid,
       "cmL3QosShaperHistoryAction": cmL3QosShaperHistoryAction,
       "cmL3QosShaperHistoryBT": cmL3QosShaperHistoryBT,
       "cmL3QosShaperHistoryBTD": cmL3QosShaperHistoryBTD,
       "cmL3QosShaperHistoryFD": cmL3QosShaperHistoryFD,
       "cmL3QosShaperHistoryFTD": cmL3QosShaperHistoryFTD,
       "cmL3QosShaperHistoryBR": cmL3QosShaperHistoryBR,
       "cmL3QosShaperHistoryFR": cmL3QosShaperHistoryFR,
       "cmL3QosShaperHistoryABRRL": cmL3QosShaperHistoryABRRL,
       "cmL3QosShaperHistoryABRRLR": cmL3QosShaperHistoryABRRLR,
       "cmL3QosShaperHistoryBREDD": cmL3QosShaperHistoryBREDD,
       "cmL3QosShaperHistoryFREDD": cmL3QosShaperHistoryFREDD,
       "cmL3QosShaperThresholdTable": cmL3QosShaperThresholdTable,
       "cmL3QosShaperThresholdEntry": cmL3QosShaperThresholdEntry,
       "cmL3QosShaperThresholdIndex": cmL3QosShaperThresholdIndex,
       "cmL3QosShaperThresholdInterval": cmL3QosShaperThresholdInterval,
       "cmL3QosShaperThresholdVariable": cmL3QosShaperThresholdVariable,
       "cmL3QosShaperThresholdValueLo": cmL3QosShaperThresholdValueLo,
       "cmL3QosShaperThresholdValueHi": cmL3QosShaperThresholdValueHi,
       "cmL3QosShaperThresholdMonValue": cmL3QosShaperThresholdMonValue,
       "f3L3Notifications": f3L3Notifications,
       "f3L3FlowPointThresholdCrossingAlert": f3L3FlowPointThresholdCrossingAlert,
       "f3L3QosPolicerThresholdCrossingAlert": f3L3QosPolicerThresholdCrossingAlert,
       "f3L3QosShaperThresholdCrossingAlert": f3L3QosShaperThresholdCrossingAlert,
       "f3L3TrafficIpInterfaceThresholdCrossingAlert": f3L3TrafficIpInterfaceThresholdCrossingAlert,
       "f3L3AclRuleThresholdCrossingAlert": f3L3AclRuleThresholdCrossingAlert,
       "f3L2A2NAclRuleThresholdCrossingAlert": f3L2A2NAclRuleThresholdCrossingAlert,
       "f3L2N2AAclRuleThresholdCrossingAlert": f3L2N2AAclRuleThresholdCrossingAlert,
       "f3L3TrafficIPv6InterfaceThresholdCrossingAlert": f3L3TrafficIPv6InterfaceThresholdCrossingAlert,
       "f3L3Conformance": f3L3Conformance,
       "f3L3Compliances": f3L3Compliances,
       "f3L3Compliance": f3L3Compliance,
       "f3L3Groups": f3L3Groups,
       "f3L3ObjectsGroup": f3L3ObjectsGroup,
       "f3L3PerfGroup": f3L3PerfGroup,
       "f3L3TrafficOspfGroup": f3L3TrafficOspfGroup,
       "f3L3TrafficIPv6Group": f3L3TrafficIPv6Group,
       "f3L3TrafficBgpGroup": f3L3TrafficBgpGroup,
       "cmL3Notifications": cmL3Notifications,
       "cmL3FlowPointThresholdCrossingAlert": cmL3FlowPointThresholdCrossingAlert,
       "cmL3QosPolicerThresholdCrossingAlert": cmL3QosPolicerThresholdCrossingAlert,
       "cmL3QosShaperThresholdCrossingAlert": cmL3QosShaperThresholdCrossingAlert}
)
