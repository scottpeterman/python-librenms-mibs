# SNMP MIB module (TIMETRA-OAM-TEST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\TIMETRA-OAM-TEST-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:17:30 2025
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

(AtmVcIdentifier,
 AtmVpIdentifier) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmVcIdentifier",
    "AtmVpIdentifier")

(Dot1agCfmMepIdOrZero,) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "Dot1agCfmMepIdOrZero")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber")

(MplsLabel,) = mibBuilder.importSymbols(
    "MPLS-LDP-MIB",
    "MplsLabel")

(RouterID,) = mibBuilder.importSymbols(
    "OSPF-MIB",
    "RouterID")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(SdpBindVcType,
 SdpId) = mibBuilder.importSymbols(
    "TIMETRA-SERV-MIB",
    "SdpBindVcType",
    "SdpId")

(TmnxMobGwId,) = mibBuilder.importSymbols(
    "TIMETRA-TC-MG-MIB",
    "TmnxMobGwId")

(Dot1PPriority,
 IpAddressPrefixLength,
 SdpBindId,
 ServiceOperStatus,
 TDSCPName,
 TDSCPNameOrEmpty,
 TFCName,
 TItemDescription,
 TLNamedItem,
 TLNamedItemOrEmpty,
 TNamedItem,
 TNamedItemOrEmpty,
 TPolicyStatementNameOrEmpty,
 TProfile,
 TmnxActionType,
 TmnxAdminState,
 TmnxBfdOnLspSessFecType,
 TmnxBgpRouteTarget,
 TmnxEnabledDisabled,
 TmnxEnabledDisabledAdminState,
 TmnxEncapVal,
 TmnxHigh32,
 TmnxIgpInstance,
 TmnxLow32,
 TmnxMplsTpGlobalID,
 TmnxMplsTpNodeID,
 TmnxPortID,
 TmnxPwGlobalIdOrZero,
 TmnxServId,
 TmnxSpokeSdpIdOrZero,
 TmnxStrSapId,
 TmnxTunnelID,
 TmnxTunnelType,
 TmnxVPNRouteDistinguisher,
 TmnxVRtrID,
 TmnxVRtrIDOrZero,
 TmnxVcId,
 TmnxVcIdOrNone) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "Dot1PPriority",
    "IpAddressPrefixLength",
    "SdpBindId",
    "ServiceOperStatus",
    "TDSCPName",
    "TDSCPNameOrEmpty",
    "TFCName",
    "TItemDescription",
    "TLNamedItem",
    "TLNamedItemOrEmpty",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TPolicyStatementNameOrEmpty",
    "TProfile",
    "TmnxActionType",
    "TmnxAdminState",
    "TmnxBfdOnLspSessFecType",
    "TmnxBgpRouteTarget",
    "TmnxEnabledDisabled",
    "TmnxEnabledDisabledAdminState",
    "TmnxEncapVal",
    "TmnxHigh32",
    "TmnxIgpInstance",
    "TmnxLow32",
    "TmnxMplsTpGlobalID",
    "TmnxMplsTpNodeID",
    "TmnxPortID",
    "TmnxPwGlobalIdOrZero",
    "TmnxServId",
    "TmnxSpokeSdpIdOrZero",
    "TmnxStrSapId",
    "TmnxTunnelID",
    "TmnxTunnelType",
    "TmnxVPNRouteDistinguisher",
    "TmnxVRtrID",
    "TmnxVRtrIDOrZero",
    "TmnxVcId",
    "TmnxVcIdOrNone")

(vRtrID,
 vRtrIfIndex) = mibBuilder.importSymbols(
    "TIMETRA-VRTR-MIB",
    "vRtrID",
    "vRtrIfIndex")


# MODULE-IDENTITY

timetraOamTestMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 11)
)
if mibBuilder.loadTexts:
    timetraOamTestMIBModule.setRevisions(
        ("2017-01-01 00:00",
         "2016-01-01 00:00",
         "2015-01-01 00:00",
         "2014-01-01 00:00",
         "2011-02-01 00:00",
         "2009-02-28 00:00",
         "2008-01-01 00:00",
         "2007-01-01 00:00",
         "2006-03-09 00:00",
         "2005-08-31 00:00",
         "2005-01-24 00:00",
         "2004-01-15 00:00",
         "2003-08-15 00:00",
         "2003-01-20 00:00",
         "2001-11-15 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxOamBierHistoryReturnCode(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class TmnxOamBuildPktHeaderType(TextualConvention, Integer32):
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
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("controlWord", 1),
          ("dot1q", 2),
          ("ethernet", 3),
          ("gre", 4),
          ("gtpUser", 5),
          ("ipsecAuth", 6),
          ("ipv4", 7),
          ("ipv6", 8),
          ("ipv6Fragment", 9),
          ("l2tp", 10),
          ("mpls", 11),
          ("pbb", 12),
          ("tcp", 13),
          ("udp", 14))
    )



class TmnxOamLspAssocChannel(TextualConvention, Integer32):
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
        *(("notApplicable", 1),
          ("nonIp", 2),
          ("none", 3),
          ("ipv4", 4))
    )



class TmnxOamLspTestSubMode(TextualConvention, Integer32):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("unspecified", 1),
          ("static", 2),
          ("bgpLabeledPrefix", 3),
          ("srIsis", 4),
          ("srOspf", 5),
          ("srTe", 6),
          ("srPolicy", 7),
          ("srOspf3", 8))
    )



class TmnxOamMplsEchoDownMapTlv(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dsmap", 1),
          ("ddmap", 2))
    )



class TmnxOamMplsEchoDownMapTlvOrNone(TextualConvention, Integer32):
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
        *(("dsmap", 1),
          ("ddmap", 2),
          ("none", 3))
    )



class TmnxOamMplsTpPathType(TextualConvention, Integer32):
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
        *(("working", 1),
          ("protect", 2),
          ("active", 3))
    )



class TmnxOamTestMode(TextualConvention, Integer32):
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
        *(("notConfigured", 0),
          ("ping", 1),
          ("traceroute", 2))
    )



class TmnxOamPingRtnCode(TextualConvention, Integer32):
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
              13,
              14,
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("fecEgress", 1),
          ("fecNoMap", 2),
          ("notDownstream", 3),
          ("downstream", 4),
          ("downstreamNotLabel", 5),
          ("downstreamNotMac", 6),
          ("downstreamNotMacFlood", 7),
          ("malformedEchoRequest", 8),
          ("tlvNotUnderstood", 9),
          ("downstreamNotInMfib", 10),
          ("downstreamMismatched", 11),
          ("upstreamIfIdUnkn", 12),
          ("noMplsFwd", 13),
          ("noLabelAtStackDepth", 14),
          ("protoIntfMismatched", 15),
          ("terminatedByOneLabel", 16),
          ("seeDDMapForRetCodeSubCode", 17),
          ("fecStackChange", 18))
    )



class TmnxOamAddressType(TextualConvention, Integer32):
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("ipv4Address", 1),
          ("ipv6Address", 2),
          ("macAddress", 3),
          ("sapId", 4),
          ("sdpId", 5),
          ("localCpu", 6),
          ("ipv4Unnumbered", 7),
          ("ipv6Unnumbered", 8),
          ("sdpBindId", 9),
          ("nonIp", 10),
          ("networkInterface", 11))
    )



class TmnxOamResponseStatus(TextualConvention, Integer32):
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
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              167,
              168,
              169,
              170,
              171,
              172,
              173,
              174,
              175,
              176,
              177,
              178,
              179,
              180,
              181,
              182,
              183,
              184,
              185,
              186,
              187,
              188,
              189,
              190,
              191,
              192,
              193,
              194)
        )
    )
    namedValues = NamedValues(
        *(("responseReceived", 1),
          ("unknown", 2),
          ("internalError", 3),
          ("maxConcurrentLimitReached", 4),
          ("requestTimedOut", 5),
          ("unknownOrigSdpId", 6),
          ("downOrigSdpId", 7),
          ("requestTerminated", 8),
          ("invalidOriginatorId", 9),
          ("invalidResponderId", 10),
          ("unknownRespSdpId", 11),
          ("downRespSdpId", 12),
          ("invalidServiceId", 13),
          ("invalidSdp", 14),
          ("downServiceSdp", 15),
          ("noServiceEgressLabel", 16),
          ("invalidHostAddress", 17),
          ("invalidMacAddress", 18),
          ("invalidLspName", 19),
          ("macIsLocal", 20),
          ("farEndUnreachable", 21),
          ("downOriginatorId", 22),
          ("downResponderId", 23),
          ("changedResponderId", 24),
          ("downOrigSvcId", 25),
          ("downRespSvcId", 26),
          ("noServiceIngressLabel", 27),
          ("mismatchCustId", 28),
          ("mismatchSvcType", 29),
          ("mismatchSvcMtu", 30),
          ("mismatchSvcLabel", 31),
          ("noSdpBoundToSvc", 32),
          ("downOrigSdpBinding", 33),
          ("invalidLspPathName", 34),
          ("noLspEndpointAddr", 35),
          ("invalidLspId", 36),
          ("downLspPath", 37),
          ("invalidLspProtocol", 38),
          ("invalidLspLabel", 39),
          ("routeIsLocal", 40),
          ("noRouteToDest", 41),
          ("localExtranetRoute", 42),
          ("srcIpInBgpVpnRoute", 43),
          ("srcIpInvalid", 44),
          ("bgpDaemonBusy", 45),
          ("mcastNotEnabled", 46),
          ("mTraceNoSGFlow", 47),
          ("mTraceSysIpNotCfg", 48),
          ("noFwdEntryInMfib", 49),
          ("dnsNameNotFound", 50),
          ("noSocket", 51),
          ("socketOptVprnIdFail", 52),
          ("socketOptIfInexFail", 53),
          ("socketOptNextHopFail", 54),
          ("socketOptMtuDiscFail", 55),
          ("socketOptSndbufFail", 56),
          ("socketOptHdrincFail", 57),
          ("socketOptTosFail", 58),
          ("socketOptTtlFail", 59),
          ("bindSocketFail", 60),
          ("noRouteByIntf", 61),
          ("noIntf", 62),
          ("noLocalIp", 63),
          ("sendtoFail", 64),
          ("rcvdWrongType", 65),
          ("noDirectInterface", 66),
          ("nexthopUnreachable", 67),
          ("socketOptHwTimeStampFail", 68),
          ("noSpokeSdpInVll", 69),
          ("farEndVccvNotSupported", 70),
          ("noVcEgressLabel", 71),
          ("socketOptIpSessionFail", 72),
          ("rcvdWrongSize", 73),
          ("dnsLookupFail", 74),
          ("noIpv6SrcAddrOnIntf", 75),
          ("multipathNotSupported", 76),
          ("nhIntfNameNotFound", 77),
          ("msPwInvalidReplyMode", 78),
          ("ancpNoAncpString", 79),
          ("ancpNoSubscriber", 80),
          ("ancpNoAncpStringForSubscriber", 81),
          ("ancpNoAccessNodeforAncpString", 82),
          ("ancpNoAncpCapabilityNegotiated", 83),
          ("ancpOtherTestInProgress", 84),
          ("ancpMaxNbrAncpTestsInProgress", 85),
          ("spokeSdpOperDown", 86),
          ("noMsPwVccvInReplyDir", 87),
          ("p2mpLspNameOrInstInvalid", 88),
          ("p2mpLspS2LPathDown", 89),
          ("p2mpLspS2LAddressInvalid", 90),
          ("p2mpLspNotOperational", 91),
          ("p2mpLspTrMultipleReplies", 92),
          ("invalidMepId", 93),
          ("multipleReplies", 94),
          ("packetSizeTooBig", 95),
          ("gtpPingError", 96),
          ("gtpPingRsrcUnavailable", 97),
          ("gtpPingDupRequest", 98),
          ("gtpPingCleanUpInProg", 99),
          ("invalidInterface", 100),
          ("p2mpLspNotFound", 101),
          ("ethCfmSlmInLoss", 102),
          ("ethCfmSlmOutLoss", 103),
          ("ethCfmSlmUnacknowledged", 104),
          ("spokeSdpFecNoBndFound", 105),
          ("mtraceNotSupportedP2mp", 106),
          ("useFec129Parameters", 107),
          ("dnsServerUnexpectedResponse", 108),
          ("dnsServerResponseFormErr", 109),
          ("dnsServerResponseServFail", 110),
          ("dnsServerResponseNotImp", 111),
          ("dnsServerResponseRefused", 112),
          ("sendFailUndefinedServiceId", 113),
          ("sendFailWrongServiceType", 114),
          ("sendFailSubnettedService", 115),
          ("invalidRespServiceId", 116),
          ("adminDownOrigSdpBind", 117),
          ("operDownRespSdpBind", 118),
          ("adminDownRespSdpBind", 119),
          ("sdpBindVcidMismatch", 120),
          ("sdpBindTypeMismatch", 121),
          ("sdpBindVcTypeMismatch", 122),
          ("sdpBindVlanVcTagMismatch", 123),
          ("adminDownOrigSvc", 124),
          ("adminDownRespSvc", 125),
          ("adminDownOrigSdpId", 126),
          ("adminDownRespSdpId", 127),
          ("mTraceSourceIsNotRemote", 128),
          ("invalidVirtualRouterId", 129),
          ("ldpPrefixIsLocal", 130),
          ("sourceIpIsNotLocal", 131),
          ("nextHopIpIsLocal", 132),
          ("targetIpIsLocal", 133),
          ("invalidControlPlaneOption", 134),
          ("iomRevisionNotSupported", 135),
          ("invalidSourceMacOption", 136),
          ("sendFailSpbMgdService", 137),
          ("useStaticPwParameters", 138),
          ("type1Fec129PwNotSupported", 139),
          ("mplsTpLspPathNotOperational", 140),
          ("invalidStaticMplsTpLsp", 141),
          ("controlWordNotValid", 142),
          ("pwPathIdNotConfigured", 143),
          ("notSupportedOnVcSwitchService", 144),
          ("sdpFarEndNotSupported", 145),
          ("mplsTpLspPathShutdown", 146),
          ("forceOptionIsBlocked", 147),
          ("intfForLspPathIsNotOperational", 148),
          ("ttlExpired", 149),
          ("networkUnreachable", 150),
          ("hostUnreachable", 151),
          ("bgpLabelPrefixIsLocal", 152),
          ("bgpLabelPrefixUnknown", 153),
          ("ldpPrefixUnknown", 154),
          ("l2tpv3DeliveryTypeUnsupported", 155),
          ("vPingPeerCvNoLspPing", 156),
          ("vPingPeerCcNoCtrlWord", 157),
          ("sendFailEvpnCfgdService", 158),
          ("sendFailed", 159),
          ("minimumPacketSizeNotMet", 160),
          ("invalidTargetFecType", 161),
          ("p2mpLspPingNotSupportedOnMgmtRtr", 162),
          ("ipv4SdpFarEndsOnly", 163),
          ("vxlanEgrBndSvcMismatch", 164),
          ("vxlanNoMatchingTep", 165),
          ("vxlanEvpnUnconfigured", 166),
          ("ipv6SdpFarEndsNotSupported", 167),
          ("oamTestOverSRTunNotSupported", 168),
          ("sendFailEvpnCfgdPbbService", 169),
          ("txPortDown", 170),
          ("noTxPort", 171),
          ("parentAdminDown", 172),
          ("destMacResolveFail", 173),
          ("vxlanIpV6TermUnsupported", 174),
          ("ipPrefixIsLocal", 175),
          ("ipPrefixUnknown", 176),
          ("greEthBrdgdDelvryTypeUnsupported", 177),
          ("mtrace2Disabled", 178),
          ("ipv6TunneledNextHopUnsupported", 179),
          ("srTunneledNextHopUnsupported", 180),
          ("srTeTunneledNextHopUnsupported", 181),
          ("nextHopIpIsSubnet", 182),
          ("ipDestAndNextHopComboUnsupported", 183),
          ("resolvedIpDstSrcComboUnsupported", 184),
          ("srPolicyNotFound", 185),
          ("srPolicySegmentListNotFound", 186),
          ("ethCfmUnsupportedTestType", 187),
          ("ipPrefixInvalid", 188),
          ("bierError", 189),
          ("pathDestAddrTypeMismatch", 190),
          ("srcAddrTypeMismatch", 191),
          ("nhAddrTypeMismatch", 192),
          ("invalidRouterInstance", 193),
          ("mtrace2OperDown", 194))
    )



class TmnxOamSignalProtocol(TextualConvention, Integer32):
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
        *(("unknown", 0),
          ("static", 1),
          ("bgp", 2),
          ("ldp", 3),
          ("rsvpTe", 4),
          ("ospf", 5),
          ("isis", 6),
          ("ospf3", 7))
    )



class TmnxOamTestResponsePlane(TextualConvention, Integer32):
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
        *(("controlPlane", 1),
          ("dataPlane", 2),
          ("none", 3))
    )



class TmnxOamSaaThreshold(TextualConvention, Integer32):
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
        *(("noThreshold", 0),
          ("inJitter", 1),
          ("outJitter", 2),
          ("rtJitter", 3),
          ("inLoss", 4),
          ("outLoss", 5),
          ("rtLoss", 6),
          ("inLatency", 7),
          ("outLatency", 8),
          ("rtLatency", 9))
    )



class TmnxOamVccvAssocChannel(TextualConvention, Integer32):
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
        *(("notApplicable", 1),
          ("nonIp", 2),
          ("ipv4", 3))
    )



class TmnxOamVccvTestSubMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unspecified", 1),
          ("static", 2))
    )



class TmnxOamVccvSwitTgtFecType(TextualConvention, Integer32):
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
        *(("none", 1),
          ("fec128", 2),
          ("static", 3))
    )



class TmnxOamVcType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              11)
        )
    )
    namedValues = NamedValues(
        *(("meshSdp", 5),
          ("spokeSdp", 11))
    )



class TmnxOamLTtraceDisStatusBits(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("timeout", 0),
          ("maxPath", 1),
          ("maxHop", 2),
          ("unexploredPath", 3),
          ("noResource", 4))
    )


class TmnxOamTestResult(TextualConvention, Integer32):
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
        *(("undetermined", 0),
          ("success", 1),
          ("failed", 2),
          ("aborted", 3),
          ("txResourcesUnavail", 4))
    )



# MIB Managed Objects in the order of their OIDs

_TmnxOamTestConformance_ObjectIdentity = ObjectIdentity
tmnxOamTestConformance = _TmnxOamTestConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11)
)
_TmnxOamPingConformance_ObjectIdentity = ObjectIdentity
tmnxOamPingConformance = _TmnxOamPingConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1)
)
_TmnxOamPingCompliances_ObjectIdentity = ObjectIdentity
tmnxOamPingCompliances = _TmnxOamPingCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 1)
)
_TmnxOamPingGroups_ObjectIdentity = ObjectIdentity
tmnxOamPingGroups = _TmnxOamPingGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2)
)
_TmnxOamPingV19v0ObjGroups_ObjectIdentity = ObjectIdentity
tmnxOamPingV19v0ObjGroups = _TmnxOamPingV19v0ObjGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 63)
)
_TmnxOamPingV20v0ObjGroups_ObjectIdentity = ObjectIdentity
tmnxOamPingV20v0ObjGroups = _TmnxOamPingV20v0ObjGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 64)
)
_TmnxOamIfPingObjGroups_ObjectIdentity = ObjectIdentity
tmnxOamIfPingObjGroups = _TmnxOamIfPingObjGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 3)
)
_TmnxOamLnkMeasObjsGroups_ObjectIdentity = ObjectIdentity
tmnxOamLnkMeasObjsGroups = _TmnxOamLnkMeasObjsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 4)
)
_TmnxOamTraceRouteConformance_ObjectIdentity = ObjectIdentity
tmnxOamTraceRouteConformance = _TmnxOamTraceRouteConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2)
)
_TmnxOamTrCompliances_ObjectIdentity = ObjectIdentity
tmnxOamTrCompliances = _TmnxOamTrCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 1)
)
_TmnxOamTrGroups_ObjectIdentity = ObjectIdentity
tmnxOamTrGroups = _TmnxOamTrGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 2)
)
_TmnxOamTrV19v0ObjGroups_ObjectIdentity = ObjectIdentity
tmnxOamTrV19v0ObjGroups = _TmnxOamTrV19v0ObjGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 2, 46)
)
_TmnxOamTrV20v0ObjGroups_ObjectIdentity = ObjectIdentity
tmnxOamTrV20v0ObjGroups = _TmnxOamTrV20v0ObjGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 2, 47)
)
_TmnxOamTrV21v0ObjGroups_ObjectIdentity = ObjectIdentity
tmnxOamTrV21v0ObjGroups = _TmnxOamTrV21v0ObjGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 2, 48)
)
_TmnxOamSaaConformance_ObjectIdentity = ObjectIdentity
tmnxOamSaaConformance = _TmnxOamSaaConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 3)
)
_TmnxOamSaaCompliances_ObjectIdentity = ObjectIdentity
tmnxOamSaaCompliances = _TmnxOamSaaCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 3, 1)
)
_TmnxOamSaaGroups_ObjectIdentity = ObjectIdentity
tmnxOamSaaGroups = _TmnxOamSaaGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 3, 2)
)
_TmnxOamMobGatewayConformance_ObjectIdentity = ObjectIdentity
tmnxOamMobGatewayConformance = _TmnxOamMobGatewayConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 4)
)
_TmnxOamGeneralConformance_ObjectIdentity = ObjectIdentity
tmnxOamGeneralConformance = _TmnxOamGeneralConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 5)
)
_TmnxOamGeneralCompliances_ObjectIdentity = ObjectIdentity
tmnxOamGeneralCompliances = _TmnxOamGeneralCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 5, 1)
)
_TmnxOamGeneralGroups_ObjectIdentity = ObjectIdentity
tmnxOamGeneralGroups = _TmnxOamGeneralGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 5, 2)
)
_TmnxOamDiagConformance_ObjectIdentity = ObjectIdentity
tmnxOamDiagConformance = _TmnxOamDiagConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 6)
)
_TmnxOamDiagCompliances_ObjectIdentity = ObjectIdentity
tmnxOamDiagCompliances = _TmnxOamDiagCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 6, 1)
)
_TmnxOamDiagGroups_ObjectIdentity = ObjectIdentity
tmnxOamDiagGroups = _TmnxOamDiagGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 6, 2)
)
_TmnxOamIfPingConformance_ObjectIdentity = ObjectIdentity
tmnxOamIfPingConformance = _TmnxOamIfPingConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 7)
)
_TmnxOamIfPingCompliances_ObjectIdentity = ObjectIdentity
tmnxOamIfPingCompliances = _TmnxOamIfPingCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 7, 1)
)
_TmnxOamLnkMeasConformance_ObjectIdentity = ObjectIdentity
tmnxOamLnkMeasConformance = _TmnxOamLnkMeasConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 8)
)
_TmnxOamLnkMeasCompliances_ObjectIdentity = ObjectIdentity
tmnxOamLnkMeasCompliances = _TmnxOamLnkMeasCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 8, 1)
)
_TmnxOamTestObjs_ObjectIdentity = ObjectIdentity
tmnxOamTestObjs = _TmnxOamTestObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11)
)
_TmnxOamPingObjs_ObjectIdentity = ObjectIdentity
tmnxOamPingObjs = _TmnxOamPingObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1)
)
_TmnxOamPingNotificationObjects_ObjectIdentity = ObjectIdentity
tmnxOamPingNotificationObjects = _TmnxOamPingNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 1)
)


class _TmnxOamPingMaxConcurrentTests_Type(Unsigned32):
    """Custom type tmnxOamPingMaxConcurrentTests based on Unsigned32"""
    defaultValue = 0


_TmnxOamPingMaxConcurrentTests_Type.__name__ = "Unsigned32"
_TmnxOamPingMaxConcurrentTests_Object = MibScalar
tmnxOamPingMaxConcurrentTests = _TmnxOamPingMaxConcurrentTests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 2),
    _TmnxOamPingMaxConcurrentTests_Type()
)
tmnxOamPingMaxConcurrentTests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPingMaxConcurrentTests.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingMaxConcurrentTests.setUnits("tests")
_TmnxOamPingCtlTable_Object = MibTable
tmnxOamPingCtlTable = _TmnxOamPingCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3)
)
if mibBuilder.loadTexts:
    tmnxOamPingCtlTable.setStatus("current")
_TmnxOamPingCtlEntry_Object = MibTableRow
tmnxOamPingCtlEntry = _TmnxOamPingCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1)
)
tmnxOamPingCtlEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamPingCtlEntry.setStatus("current")


class _TmnxOamPingCtlOwnerIndex_Type(SnmpAdminString):
    """Custom type tmnxOamPingCtlOwnerIndex based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TmnxOamPingCtlOwnerIndex_Type.__name__ = "SnmpAdminString"
_TmnxOamPingCtlOwnerIndex_Object = MibTableColumn
tmnxOamPingCtlOwnerIndex = _TmnxOamPingCtlOwnerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 1),
    _TmnxOamPingCtlOwnerIndex_Type()
)
tmnxOamPingCtlOwnerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamPingCtlOwnerIndex.setStatus("current")


class _TmnxOamPingCtlTestIndex_Type(SnmpAdminString):
    """Custom type tmnxOamPingCtlTestIndex based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TmnxOamPingCtlTestIndex_Type.__name__ = "SnmpAdminString"
_TmnxOamPingCtlTestIndex_Object = MibTableColumn
tmnxOamPingCtlTestIndex = _TmnxOamPingCtlTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 2),
    _TmnxOamPingCtlTestIndex_Type()
)
tmnxOamPingCtlTestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamPingCtlTestIndex.setStatus("current")
_TmnxOamPingCtlRowStatus_Type = RowStatus
_TmnxOamPingCtlRowStatus_Object = MibTableColumn
tmnxOamPingCtlRowStatus = _TmnxOamPingCtlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 3),
    _TmnxOamPingCtlRowStatus_Type()
)
tmnxOamPingCtlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlRowStatus.setStatus("current")


class _TmnxOamPingCtlStorageType_Type(StorageType):
    """Custom type tmnxOamPingCtlStorageType based on StorageType"""
    defaultValue = 2


_TmnxOamPingCtlStorageType_Type.__name__ = "StorageType"
_TmnxOamPingCtlStorageType_Object = MibTableColumn
tmnxOamPingCtlStorageType = _TmnxOamPingCtlStorageType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 4),
    _TmnxOamPingCtlStorageType_Type()
)
tmnxOamPingCtlStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlStorageType.setStatus("obsolete")


class _TmnxOamPingCtlDescr_Type(SnmpAdminString):
    """Custom type tmnxOamPingCtlDescr based on SnmpAdminString"""
    defaultHexValue = ""


_TmnxOamPingCtlDescr_Type.__name__ = "SnmpAdminString"
_TmnxOamPingCtlDescr_Object = MibTableColumn
tmnxOamPingCtlDescr = _TmnxOamPingCtlDescr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 5),
    _TmnxOamPingCtlDescr_Type()
)
tmnxOamPingCtlDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlDescr.setStatus("obsolete")


class _TmnxOamPingCtlTestMode_Type(Integer32):
    """Custom type tmnxOamPingCtlTestMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              25)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("sdpPing", 1),
          ("mtuPing", 2),
          ("svcPing", 3),
          ("macPing", 5),
          ("macPopulate", 6),
          ("macPurge", 7),
          ("lspPing", 8),
          ("vprnPing", 9),
          ("atmPing", 10),
          ("mfibPing", 11),
          ("cpePing", 12),
          ("mrInfo", 13),
          ("vccvPing", 14),
          ("icmpPing", 15),
          ("dnsPing", 16),
          ("ancpLoopback", 17),
          ("p2mpLspPing", 18),
          ("ethCfmLoopback", 19),
          ("ethCfmTwoWayDelay", 20),
          ("gtpPing", 21),
          ("ethCfmTwoWaySlm", 22),
          ("vxlanPing", 23),
          ("bierPing", 25))
    )


_TmnxOamPingCtlTestMode_Type.__name__ = "Integer32"
_TmnxOamPingCtlTestMode_Object = MibTableColumn
tmnxOamPingCtlTestMode = _TmnxOamPingCtlTestMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 6),
    _TmnxOamPingCtlTestMode_Type()
)
tmnxOamPingCtlTestMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlTestMode.setStatus("current")
_TmnxOamPingCtlAdminStatus_Type = TmnxEnabledDisabledAdminState
_TmnxOamPingCtlAdminStatus_Object = MibTableColumn
tmnxOamPingCtlAdminStatus = _TmnxOamPingCtlAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 7),
    _TmnxOamPingCtlAdminStatus_Type()
)
tmnxOamPingCtlAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlAdminStatus.setStatus("current")


class _TmnxOamPingCtlOrigSdpId_Type(SdpId):
    """Custom type tmnxOamPingCtlOrigSdpId based on SdpId"""
    defaultValue = 0


_TmnxOamPingCtlOrigSdpId_Type.__name__ = "SdpId"
_TmnxOamPingCtlOrigSdpId_Object = MibTableColumn
tmnxOamPingCtlOrigSdpId = _TmnxOamPingCtlOrigSdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 8),
    _TmnxOamPingCtlOrigSdpId_Type()
)
tmnxOamPingCtlOrigSdpId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlOrigSdpId.setStatus("current")


class _TmnxOamPingCtlRespSdpId_Type(SdpId):
    """Custom type tmnxOamPingCtlRespSdpId based on SdpId"""
    defaultValue = 0


_TmnxOamPingCtlRespSdpId_Type.__name__ = "SdpId"
_TmnxOamPingCtlRespSdpId_Object = MibTableColumn
tmnxOamPingCtlRespSdpId = _TmnxOamPingCtlRespSdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 9),
    _TmnxOamPingCtlRespSdpId_Type()
)
tmnxOamPingCtlRespSdpId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlRespSdpId.setStatus("current")


class _TmnxOamPingCtlFcName_Type(TFCName):
    """Custom type tmnxOamPingCtlFcName based on TFCName"""
    defaultValue = OctetString("be")


_TmnxOamPingCtlFcName_Type.__name__ = "TFCName"
_TmnxOamPingCtlFcName_Object = MibTableColumn
tmnxOamPingCtlFcName = _TmnxOamPingCtlFcName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 10),
    _TmnxOamPingCtlFcName_Type()
)
tmnxOamPingCtlFcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlFcName.setStatus("current")


class _TmnxOamPingCtlProfile_Type(TProfile):
    """Custom type tmnxOamPingCtlProfile based on TProfile"""
    defaultValue = 2


_TmnxOamPingCtlProfile_Type.__name__ = "TProfile"
_TmnxOamPingCtlProfile_Object = MibTableColumn
tmnxOamPingCtlProfile = _TmnxOamPingCtlProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 11),
    _TmnxOamPingCtlProfile_Type()
)
tmnxOamPingCtlProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlProfile.setStatus("current")


class _TmnxOamPingCtlMtuStartSize_Type(Unsigned32):
    """Custom type tmnxOamPingCtlMtuStartSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(40, 9786),
    )


_TmnxOamPingCtlMtuStartSize_Type.__name__ = "Unsigned32"
_TmnxOamPingCtlMtuStartSize_Object = MibTableColumn
tmnxOamPingCtlMtuStartSize = _TmnxOamPingCtlMtuStartSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 12),
    _TmnxOamPingCtlMtuStartSize_Type()
)
tmnxOamPingCtlMtuStartSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlMtuStartSize.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingCtlMtuStartSize.setUnits("octets")


class _TmnxOamPingCtlMtuEndSize_Type(Unsigned32):
    """Custom type tmnxOamPingCtlMtuEndSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(40, 9786),
    )


_TmnxOamPingCtlMtuEndSize_Type.__name__ = "Unsigned32"
_TmnxOamPingCtlMtuEndSize_Object = MibTableColumn
tmnxOamPingCtlMtuEndSize = _TmnxOamPingCtlMtuEndSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 13),
    _TmnxOamPingCtlMtuEndSize_Type()
)
tmnxOamPingCtlMtuEndSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlMtuEndSize.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingCtlMtuEndSize.setUnits("octets")


class _TmnxOamPingCtlMtuStepSize_Type(Unsigned32):
    """Custom type tmnxOamPingCtlMtuStepSize based on Unsigned32"""
    defaultValue = 32

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_TmnxOamPingCtlMtuStepSize_Type.__name__ = "Unsigned32"
_TmnxOamPingCtlMtuStepSize_Object = MibTableColumn
tmnxOamPingCtlMtuStepSize = _TmnxOamPingCtlMtuStepSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 14),
    _TmnxOamPingCtlMtuStepSize_Type()
)
tmnxOamPingCtlMtuStepSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlMtuStepSize.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingCtlMtuStepSize.setUnits("octets")


class _TmnxOamPingCtlTargetIpAddress_Type(IpAddress):
    """Custom type tmnxOamPingCtlTargetIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_TmnxOamPingCtlTargetIpAddress_Type.__name__ = "IpAddress"
_TmnxOamPingCtlTargetIpAddress_Object = MibTableColumn
tmnxOamPingCtlTargetIpAddress = _TmnxOamPingCtlTargetIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 16),
    _TmnxOamPingCtlTargetIpAddress_Type()
)
tmnxOamPingCtlTargetIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlTargetIpAddress.setStatus("obsolete")


class _TmnxOamPingCtlServiceId_Type(TmnxServId):
    """Custom type tmnxOamPingCtlServiceId based on TmnxServId"""
    defaultValue = 0

    subtypeSpec = TmnxServId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TmnxOamPingCtlServiceId_Type.__name__ = "TmnxServId"
_TmnxOamPingCtlServiceId_Object = MibTableColumn
tmnxOamPingCtlServiceId = _TmnxOamPingCtlServiceId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 17),
    _TmnxOamPingCtlServiceId_Type()
)
tmnxOamPingCtlServiceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlServiceId.setStatus("current")


class _TmnxOamPingCtlLocalSdp_Type(TruthValue):
    """Custom type tmnxOamPingCtlLocalSdp based on TruthValue"""
    defaultValue = 2


_TmnxOamPingCtlLocalSdp_Type.__name__ = "TruthValue"
_TmnxOamPingCtlLocalSdp_Object = MibTableColumn
tmnxOamPingCtlLocalSdp = _TmnxOamPingCtlLocalSdp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 18),
    _TmnxOamPingCtlLocalSdp_Type()
)
tmnxOamPingCtlLocalSdp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlLocalSdp.setStatus("current")


class _TmnxOamPingCtlRemoteSdp_Type(TruthValue):
    """Custom type tmnxOamPingCtlRemoteSdp based on TruthValue"""
    defaultValue = 2


_TmnxOamPingCtlRemoteSdp_Type.__name__ = "TruthValue"
_TmnxOamPingCtlRemoteSdp_Object = MibTableColumn
tmnxOamPingCtlRemoteSdp = _TmnxOamPingCtlRemoteSdp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 19),
    _TmnxOamPingCtlRemoteSdp_Type()
)
tmnxOamPingCtlRemoteSdp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlRemoteSdp.setStatus("current")


class _TmnxOamPingCtlSize_Type(Unsigned32):
    """Custom type tmnxOamPingCtlSize based on Unsigned32"""
    defaultValue = 72

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16384),
    )


_TmnxOamPingCtlSize_Type.__name__ = "Unsigned32"
_TmnxOamPingCtlSize_Object = MibTableColumn
tmnxOamPingCtlSize = _TmnxOamPingCtlSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 20),
    _TmnxOamPingCtlSize_Type()
)
tmnxOamPingCtlSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlSize.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingCtlSize.setUnits("octets")


class _TmnxOamPingCtlTimeOut_Type(Unsigned32):
    """Custom type tmnxOamPingCtlTimeOut based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_TmnxOamPingCtlTimeOut_Type.__name__ = "Unsigned32"
_TmnxOamPingCtlTimeOut_Object = MibTableColumn
tmnxOamPingCtlTimeOut = _TmnxOamPingCtlTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 21),
    _TmnxOamPingCtlTimeOut_Type()
)
tmnxOamPingCtlTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingCtlTimeOut.setUnits("seconds")


class _TmnxOamPingCtlProbeCount_Type(Unsigned32):
    """Custom type tmnxOamPingCtlProbeCount based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_TmnxOamPingCtlProbeCount_Type.__name__ = "Unsigned32"
_TmnxOamPingCtlProbeCount_Object = MibTableColumn
tmnxOamPingCtlProbeCount = _TmnxOamPingCtlProbeCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 22),
    _TmnxOamPingCtlProbeCount_Type()
)
tmnxOamPingCtlProbeCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlProbeCount.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingCtlProbeCount.setUnits("probes")


class _TmnxOamPingCtlInterval_Type(Unsigned32):
    """Custom type tmnxOamPingCtlInterval based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_TmnxOamPingCtlInterval_Type.__name__ = "Unsigned32"
_TmnxOamPingCtlInterval_Object = MibTableColumn
tmnxOamPingCtlInterval = _TmnxOamPingCtlInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 23),
    _TmnxOamPingCtlInterval_Type()
)
tmnxOamPingCtlInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlInterval.setStatus("current")


class _TmnxOamPingCtlMaxRows_Type(Unsigned32):
    """Custom type tmnxOamPingCtlMaxRows based on Unsigned32"""
    defaultValue = 300


_TmnxOamPingCtlMaxRows_Type.__name__ = "Unsigned32"
_TmnxOamPingCtlMaxRows_Object = MibTableColumn
tmnxOamPingCtlMaxRows = _TmnxOamPingCtlMaxRows_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 24),
    _TmnxOamPingCtlMaxRows_Type()
)
tmnxOamPingCtlMaxRows.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlMaxRows.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxOamPingCtlMaxRows.setUnits("rows")


class _TmnxOamPingCtlTrapGeneration_Type(Bits):
    """Custom type tmnxOamPingCtlTrapGeneration based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("probeFailure", 0),
          ("testFailure", 1),
          ("testCompletion", 2))
    )

_TmnxOamPingCtlTrapGeneration_Type.__name__ = "Bits"
_TmnxOamPingCtlTrapGeneration_Object = MibTableColumn
tmnxOamPingCtlTrapGeneration = _TmnxOamPingCtlTrapGeneration_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 25),
    _TmnxOamPingCtlTrapGeneration_Type()
)
tmnxOamPingCtlTrapGeneration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlTrapGeneration.setStatus("current")


class _TmnxOamPingCtlTrapProbeFailureFilter_Type(Unsigned32):
    """Custom type tmnxOamPingCtlTrapProbeFailureFilter based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_TmnxOamPingCtlTrapProbeFailureFilter_Type.__name__ = "Unsigned32"
_TmnxOamPingCtlTrapProbeFailureFilter_Object = MibTableColumn
tmnxOamPingCtlTrapProbeFailureFilter = _TmnxOamPingCtlTrapProbeFailureFilter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 26),
    _TmnxOamPingCtlTrapProbeFailureFilter_Type()
)
tmnxOamPingCtlTrapProbeFailureFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlTrapProbeFailureFilter.setStatus("current")


class _TmnxOamPingCtlTrapTestFailureFilter_Type(Unsigned32):
    """Custom type tmnxOamPingCtlTrapTestFailureFilter based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_TmnxOamPingCtlTrapTestFailureFilter_Type.__name__ = "Unsigned32"
_TmnxOamPingCtlTrapTestFailureFilter_Object = MibTableColumn
tmnxOamPingCtlTrapTestFailureFilter = _TmnxOamPingCtlTrapTestFailureFilter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 27),
    _TmnxOamPingCtlTrapTestFailureFilter_Type()
)
tmnxOamPingCtlTrapTestFailureFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlTrapTestFailureFilter.setStatus("current")


class _TmnxOamPingCtlSAA_Type(TruthValue):
    """Custom type tmnxOamPingCtlSAA based on TruthValue"""
    defaultValue = 2


_TmnxOamPingCtlSAA_Type.__name__ = "TruthValue"
_TmnxOamPingCtlSAA_Object = MibTableColumn
tmnxOamPingCtlSAA = _TmnxOamPingCtlSAA_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 28),
    _TmnxOamPingCtlSAA_Type()
)
tmnxOamPingCtlSAA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlSAA.setStatus("current")
_TmnxOamPingCtlRuns_Type = Counter32
_TmnxOamPingCtlRuns_Object = MibTableColumn
tmnxOamPingCtlRuns = _TmnxOamPingCtlRuns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 29),
    _TmnxOamPingCtlRuns_Type()
)
tmnxOamPingCtlRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingCtlRuns.setStatus("current")
_TmnxOamPingCtlFailures_Type = Counter32
_TmnxOamPingCtlFailures_Object = MibTableColumn
tmnxOamPingCtlFailures = _TmnxOamPingCtlFailures_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 30),
    _TmnxOamPingCtlFailures_Type()
)
tmnxOamPingCtlFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingCtlFailures.setStatus("current")
_TmnxOamPingCtlLastRunResult_Type = TmnxOamTestResult
_TmnxOamPingCtlLastRunResult_Object = MibTableColumn
tmnxOamPingCtlLastRunResult = _TmnxOamPingCtlLastRunResult_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 31),
    _TmnxOamPingCtlLastRunResult_Type()
)
tmnxOamPingCtlLastRunResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingCtlLastRunResult.setStatus("current")
_TmnxOamPingCtlLastChanged_Type = TimeStamp
_TmnxOamPingCtlLastChanged_Object = MibTableColumn
tmnxOamPingCtlLastChanged = _TmnxOamPingCtlLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 32),
    _TmnxOamPingCtlLastChanged_Type()
)
tmnxOamPingCtlLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingCtlLastChanged.setStatus("current")


class _TmnxOamPingCtlVRtrID_Type(TmnxVRtrIDOrZero):
    """Custom type tmnxOamPingCtlVRtrID based on TmnxVRtrIDOrZero"""
    defaultValue = 1


_TmnxOamPingCtlVRtrID_Type.__name__ = "TmnxVRtrIDOrZero"
_TmnxOamPingCtlVRtrID_Object = MibTableColumn
tmnxOamPingCtlVRtrID = _TmnxOamPingCtlVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 33),
    _TmnxOamPingCtlVRtrID_Type()
)
tmnxOamPingCtlVRtrID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlVRtrID.setStatus("current")


class _TmnxOamPingCtlTgtAddrType_Type(InetAddressType):
    """Custom type tmnxOamPingCtlTgtAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxOamPingCtlTgtAddrType_Type.__name__ = "InetAddressType"
_TmnxOamPingCtlTgtAddrType_Object = MibTableColumn
tmnxOamPingCtlTgtAddrType = _TmnxOamPingCtlTgtAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 34),
    _TmnxOamPingCtlTgtAddrType_Type()
)
tmnxOamPingCtlTgtAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlTgtAddrType.setStatus("current")


class _TmnxOamPingCtlTgtAddress_Type(InetAddress):
    """Custom type tmnxOamPingCtlTgtAddress based on InetAddress"""
    defaultHexValue = ""


_TmnxOamPingCtlTgtAddress_Type.__name__ = "InetAddress"
_TmnxOamPingCtlTgtAddress_Object = MibTableColumn
tmnxOamPingCtlTgtAddress = _TmnxOamPingCtlTgtAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 35),
    _TmnxOamPingCtlTgtAddress_Type()
)
tmnxOamPingCtlTgtAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlTgtAddress.setStatus("current")


class _TmnxOamPingCtlSrcAddrType_Type(InetAddressType):
    """Custom type tmnxOamPingCtlSrcAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxOamPingCtlSrcAddrType_Type.__name__ = "InetAddressType"
_TmnxOamPingCtlSrcAddrType_Object = MibTableColumn
tmnxOamPingCtlSrcAddrType = _TmnxOamPingCtlSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 36),
    _TmnxOamPingCtlSrcAddrType_Type()
)
tmnxOamPingCtlSrcAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlSrcAddrType.setStatus("current")


class _TmnxOamPingCtlSrcAddress_Type(InetAddress):
    """Custom type tmnxOamPingCtlSrcAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamPingCtlSrcAddress_Type.__name__ = "InetAddress"
_TmnxOamPingCtlSrcAddress_Object = MibTableColumn
tmnxOamPingCtlSrcAddress = _TmnxOamPingCtlSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 37),
    _TmnxOamPingCtlSrcAddress_Type()
)
tmnxOamPingCtlSrcAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlSrcAddress.setStatus("current")


class _TmnxOamPingCtlDnsName_Type(OctetString):
    """Custom type tmnxOamPingCtlDnsName based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxOamPingCtlDnsName_Type.__name__ = "OctetString"
_TmnxOamPingCtlDnsName_Object = MibTableColumn
tmnxOamPingCtlDnsName = _TmnxOamPingCtlDnsName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 38),
    _TmnxOamPingCtlDnsName_Type()
)
tmnxOamPingCtlDnsName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlDnsName.setStatus("current")


class _TmnxOamPingCtlDNSRecord_Type(Integer32):
    """Custom type tmnxOamPingCtlDNSRecord based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4Arecord", 1),
          ("ipv6AAAArecord", 2))
    )


_TmnxOamPingCtlDNSRecord_Type.__name__ = "Integer32"
_TmnxOamPingCtlDNSRecord_Object = MibTableColumn
tmnxOamPingCtlDNSRecord = _TmnxOamPingCtlDNSRecord_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 39),
    _TmnxOamPingCtlDNSRecord_Type()
)
tmnxOamPingCtlDNSRecord.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlDNSRecord.setStatus("current")


class _TmnxOamPingCtlIntervalUnits_Type(Integer32):
    """Custom type tmnxOamPingCtlIntervalUnits based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("seconds", 1),
          ("centiseconds", 2))
    )


_TmnxOamPingCtlIntervalUnits_Type.__name__ = "Integer32"
_TmnxOamPingCtlIntervalUnits_Object = MibTableColumn
tmnxOamPingCtlIntervalUnits = _TmnxOamPingCtlIntervalUnits_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 40),
    _TmnxOamPingCtlIntervalUnits_Type()
)
tmnxOamPingCtlIntervalUnits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlIntervalUnits.setStatus("current")


class _TmnxOamPingCtlSubscriberName_Type(TLNamedItemOrEmpty):
    """Custom type tmnxOamPingCtlSubscriberName based on TLNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOamPingCtlSubscriberName_Type.__name__ = "TLNamedItemOrEmpty"
_TmnxOamPingCtlSubscriberName_Object = MibTableColumn
tmnxOamPingCtlSubscriberName = _TmnxOamPingCtlSubscriberName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 41),
    _TmnxOamPingCtlSubscriberName_Type()
)
tmnxOamPingCtlSubscriberName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlSubscriberName.setStatus("current")


class _TmnxOamPingCtlRouterInstanceName_Type(TLNamedItemOrEmpty):
    """Custom type tmnxOamPingCtlRouterInstanceName based on TLNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOamPingCtlRouterInstanceName_Type.__name__ = "TLNamedItemOrEmpty"
_TmnxOamPingCtlRouterInstanceName_Object = MibTableColumn
tmnxOamPingCtlRouterInstanceName = _TmnxOamPingCtlRouterInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 42),
    _TmnxOamPingCtlRouterInstanceName_Type()
)
tmnxOamPingCtlRouterInstanceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlRouterInstanceName.setStatus("current")
_TmnxOamPingResultsTable_Object = MibTable
tmnxOamPingResultsTable = _TmnxOamPingResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4)
)
if mibBuilder.loadTexts:
    tmnxOamPingResultsTable.setStatus("current")
_TmnxOamPingResultsEntry_Object = MibTableRow
tmnxOamPingResultsEntry = _TmnxOamPingResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1)
)
tmnxOamPingResultsEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTestIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsTestRunIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamPingResultsEntry.setStatus("current")


class _TmnxOamPingResultsOperStatus_Type(Integer32):
    """Custom type tmnxOamPingResultsOperStatus based on Integer32"""
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


_TmnxOamPingResultsOperStatus_Type.__name__ = "Integer32"
_TmnxOamPingResultsOperStatus_Object = MibTableColumn
tmnxOamPingResultsOperStatus = _TmnxOamPingResultsOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1, 1),
    _TmnxOamPingResultsOperStatus_Type()
)
tmnxOamPingResultsOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingResultsOperStatus.setStatus("current")
_TmnxOamPingResultsMinRtt_Type = Unsigned32
_TmnxOamPingResultsMinRtt_Object = MibTableColumn
tmnxOamPingResultsMinRtt = _TmnxOamPingResultsMinRtt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1, 4),
    _TmnxOamPingResultsMinRtt_Type()
)
tmnxOamPingResultsMinRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingResultsMinRtt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingResultsMinRtt.setUnits("microseconds")
_TmnxOamPingResultsMaxRtt_Type = Unsigned32
_TmnxOamPingResultsMaxRtt_Object = MibTableColumn
tmnxOamPingResultsMaxRtt = _TmnxOamPingResultsMaxRtt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1, 5),
    _TmnxOamPingResultsMaxRtt_Type()
)
tmnxOamPingResultsMaxRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingResultsMaxRtt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingResultsMaxRtt.setUnits("microseconds")
_TmnxOamPingResultsAverageRtt_Type = Unsigned32
_TmnxOamPingResultsAverageRtt_Object = MibTableColumn
tmnxOamPingResultsAverageRtt = _TmnxOamPingResultsAverageRtt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1, 6),
    _TmnxOamPingResultsAverageRtt_Type()
)
tmnxOamPingResultsAverageRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingResultsAverageRtt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingResultsAverageRtt.setUnits("microseconds")
_TmnxOamPingResultsRttSumOfSquares_Type = Unsigned32
_TmnxOamPingResultsRttSumOfSquares_Object = MibTableColumn
tmnxOamPingResultsRttSumOfSquares = _TmnxOamPingResultsRttSumOfSquares_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1, 7),
    _TmnxOamPingResultsRttSumOfSquares_Type()
)
tmnxOamPingResultsRttSumOfSquares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingResultsRttSumOfSquares.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingResultsRttSumOfSquares.setUnits("microseconds squared")
_TmnxOamPingResultsMtuResponseSize_Type = Unsigned32
_TmnxOamPingResultsMtuResponseSize_Object = MibTableColumn
tmnxOamPingResultsMtuResponseSize = _TmnxOamPingResultsMtuResponseSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1, 8),
    _TmnxOamPingResultsMtuResponseSize_Type()
)
tmnxOamPingResultsMtuResponseSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingResultsMtuResponseSize.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingResultsMtuResponseSize.setUnits("octets")


class _TmnxOamPingResultsSvcPing_Type(Integer32):
    """Custom type tmnxOamPingResultsSvcPing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undetermined", 0),
          ("failed", 1),
          ("success", 2))
    )


_TmnxOamPingResultsSvcPing_Type.__name__ = "Integer32"
_TmnxOamPingResultsSvcPing_Object = MibTableColumn
tmnxOamPingResultsSvcPing = _TmnxOamPingResultsSvcPing_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1, 9),
    _TmnxOamPingResultsSvcPing_Type()
)
tmnxOamPingResultsSvcPing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingResultsSvcPing.setStatus("current")
_TmnxOamPingResultsProbeResponses_Type = Unsigned32
_TmnxOamPingResultsProbeResponses_Object = MibTableColumn
tmnxOamPingResultsProbeResponses = _TmnxOamPingResultsProbeResponses_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1, 10),
    _TmnxOamPingResultsProbeResponses_Type()
)
tmnxOamPingResultsProbeResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingResultsProbeResponses.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingResultsProbeResponses.setUnits("responses")
_TmnxOamPingResultsSentProbes_Type = Unsigned32
_TmnxOamPingResultsSentProbes_Object = MibTableColumn
tmnxOamPingResultsSentProbes = _TmnxOamPingResultsSentProbes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1, 11),
    _TmnxOamPingResultsSentProbes_Type()
)
tmnxOamPingResultsSentProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingResultsSentProbes.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingResultsSentProbes.setUnits("probes")
_TmnxOamPingResultsLastGoodProbe_Type = DateAndTime
_TmnxOamPingResultsLastGoodProbe_Object = MibTableColumn
tmnxOamPingResultsLastGoodProbe = _TmnxOamPingResultsLastGoodProbe_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1, 12),
    _TmnxOamPingResultsLastGoodProbe_Type()
)
tmnxOamPingResultsLastGoodProbe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingResultsLastGoodProbe.setStatus("current")


class _TmnxOamPingResultsLastRespHeader_Type(OctetString):
    """Custom type tmnxOamPingResultsLastRespHeader based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(100, 100),
    )
    fixed_length = 100


_TmnxOamPingResultsLastRespHeader_Type.__name__ = "OctetString"
_TmnxOamPingResultsLastRespHeader_Object = MibTableColumn
tmnxOamPingResultsLastRespHeader = _TmnxOamPingResultsLastRespHeader_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1, 13),
    _TmnxOamPingResultsLastRespHeader_Type()
)
tmnxOamPingResultsLastRespHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingResultsLastRespHeader.setStatus("obsolete")
_TmnxOamPingResultsMinTt_Type = Integer32
_TmnxOamPingResultsMinTt_Object = MibTableColumn
tmnxOamPingResultsMinTt = _TmnxOamPingResultsMinTt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1, 14),
    _TmnxOamPingResultsMinTt_Type()
)
tmnxOamPingResultsMinTt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingResultsMinTt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingResultsMinTt.setUnits("microseconds")
_TmnxOamPingResultsMaxTt_Type = Integer32
_TmnxOamPingResultsMaxTt_Object = MibTableColumn
tmnxOamPingResultsMaxTt = _TmnxOamPingResultsMaxTt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1, 15),
    _TmnxOamPingResultsMaxTt_Type()
)
tmnxOamPingResultsMaxTt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingResultsMaxTt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingResultsMaxTt.setUnits("microseconds")
_TmnxOamPingResultsAverageTt_Type = Integer32
_TmnxOamPingResultsAverageTt_Object = MibTableColumn
tmnxOamPingResultsAverageTt = _TmnxOamPingResultsAverageTt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1, 16),
    _TmnxOamPingResultsAverageTt_Type()
)
tmnxOamPingResultsAverageTt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingResultsAverageTt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingResultsAverageTt.setUnits("microseconds")
_TmnxOamPingResultsTtSumOfSquares_Type = Unsigned32
_TmnxOamPingResultsTtSumOfSquares_Object = MibTableColumn
tmnxOamPingResultsTtSumOfSquares = _TmnxOamPingResultsTtSumOfSquares_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1, 17),
    _TmnxOamPingResultsTtSumOfSquares_Type()
)
tmnxOamPingResultsTtSumOfSquares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingResultsTtSumOfSquares.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingResultsTtSumOfSquares.setUnits("microseconds squared")
_TmnxOamPingResultsMinInTt_Type = Integer32
_TmnxOamPingResultsMinInTt_Object = MibTableColumn
tmnxOamPingResultsMinInTt = _TmnxOamPingResultsMinInTt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1, 18),
    _TmnxOamPingResultsMinInTt_Type()
)
tmnxOamPingResultsMinInTt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingResultsMinInTt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingResultsMinInTt.setUnits("microseconds")
_TmnxOamPingResultsMaxInTt_Type = Integer32
_TmnxOamPingResultsMaxInTt_Object = MibTableColumn
tmnxOamPingResultsMaxInTt = _TmnxOamPingResultsMaxInTt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1, 19),
    _TmnxOamPingResultsMaxInTt_Type()
)
tmnxOamPingResultsMaxInTt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingResultsMaxInTt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingResultsMaxInTt.setUnits("microseconds")
_TmnxOamPingResultsAverageInTt_Type = Integer32
_TmnxOamPingResultsAverageInTt_Object = MibTableColumn
tmnxOamPingResultsAverageInTt = _TmnxOamPingResultsAverageInTt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1, 20),
    _TmnxOamPingResultsAverageInTt_Type()
)
tmnxOamPingResultsAverageInTt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingResultsAverageInTt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingResultsAverageInTt.setUnits("microseconds")
_TmnxOamPingResultsInTtSumOfSqrs_Type = Unsigned32
_TmnxOamPingResultsInTtSumOfSqrs_Object = MibTableColumn
tmnxOamPingResultsInTtSumOfSqrs = _TmnxOamPingResultsInTtSumOfSqrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1, 21),
    _TmnxOamPingResultsInTtSumOfSqrs_Type()
)
tmnxOamPingResultsInTtSumOfSqrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingResultsInTtSumOfSqrs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingResultsInTtSumOfSqrs.setUnits("microseconds squared")
_TmnxOamPingResultsOutJitter_Type = Integer32
_TmnxOamPingResultsOutJitter_Object = MibTableColumn
tmnxOamPingResultsOutJitter = _TmnxOamPingResultsOutJitter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1, 22),
    _TmnxOamPingResultsOutJitter_Type()
)
tmnxOamPingResultsOutJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingResultsOutJitter.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingResultsOutJitter.setUnits("microseconds")
_TmnxOamPingResultsInJitter_Type = Integer32
_TmnxOamPingResultsInJitter_Object = MibTableColumn
tmnxOamPingResultsInJitter = _TmnxOamPingResultsInJitter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1, 23),
    _TmnxOamPingResultsInJitter_Type()
)
tmnxOamPingResultsInJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingResultsInJitter.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingResultsInJitter.setUnits("microseconds")
_TmnxOamPingResultsRtJitter_Type = Integer32
_TmnxOamPingResultsRtJitter_Object = MibTableColumn
tmnxOamPingResultsRtJitter = _TmnxOamPingResultsRtJitter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1, 24),
    _TmnxOamPingResultsRtJitter_Type()
)
tmnxOamPingResultsRtJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingResultsRtJitter.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingResultsRtJitter.setUnits("microseconds")
_TmnxOamPingResultsProbeTimeouts_Type = Unsigned32
_TmnxOamPingResultsProbeTimeouts_Object = MibTableColumn
tmnxOamPingResultsProbeTimeouts = _TmnxOamPingResultsProbeTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1, 25),
    _TmnxOamPingResultsProbeTimeouts_Type()
)
tmnxOamPingResultsProbeTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingResultsProbeTimeouts.setStatus("current")
_TmnxOamPingResultsProbeFailures_Type = Unsigned32
_TmnxOamPingResultsProbeFailures_Object = MibTableColumn
tmnxOamPingResultsProbeFailures = _TmnxOamPingResultsProbeFailures_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1, 26),
    _TmnxOamPingResultsProbeFailures_Type()
)
tmnxOamPingResultsProbeFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingResultsProbeFailures.setStatus("current")


class _TmnxOamPingResultsTestRunIndex_Type(Unsigned32):
    """Custom type tmnxOamPingResultsTestRunIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxOamPingResultsTestRunIndex_Type.__name__ = "Unsigned32"
_TmnxOamPingResultsTestRunIndex_Object = MibTableColumn
tmnxOamPingResultsTestRunIndex = _TmnxOamPingResultsTestRunIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1, 27),
    _TmnxOamPingResultsTestRunIndex_Type()
)
tmnxOamPingResultsTestRunIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamPingResultsTestRunIndex.setStatus("current")
_TmnxOamPingResultsRttOFSumSquares_Type = Counter32
_TmnxOamPingResultsRttOFSumSquares_Object = MibTableColumn
tmnxOamPingResultsRttOFSumSquares = _TmnxOamPingResultsRttOFSumSquares_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1, 28),
    _TmnxOamPingResultsRttOFSumSquares_Type()
)
tmnxOamPingResultsRttOFSumSquares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingResultsRttOFSumSquares.setStatus("current")
_TmnxOamPingResultsRttHCSumSquares_Type = Counter64
_TmnxOamPingResultsRttHCSumSquares_Object = MibTableColumn
tmnxOamPingResultsRttHCSumSquares = _TmnxOamPingResultsRttHCSumSquares_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1, 29),
    _TmnxOamPingResultsRttHCSumSquares_Type()
)
tmnxOamPingResultsRttHCSumSquares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingResultsRttHCSumSquares.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingResultsRttHCSumSquares.setUnits("microseconds squared")
_TmnxOamPingResultsTtOFSumSquares_Type = Counter32
_TmnxOamPingResultsTtOFSumSquares_Object = MibTableColumn
tmnxOamPingResultsTtOFSumSquares = _TmnxOamPingResultsTtOFSumSquares_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1, 30),
    _TmnxOamPingResultsTtOFSumSquares_Type()
)
tmnxOamPingResultsTtOFSumSquares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingResultsTtOFSumSquares.setStatus("current")
_TmnxOamPingResultsTtHCSumSquares_Type = Counter64
_TmnxOamPingResultsTtHCSumSquares_Object = MibTableColumn
tmnxOamPingResultsTtHCSumSquares = _TmnxOamPingResultsTtHCSumSquares_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1, 31),
    _TmnxOamPingResultsTtHCSumSquares_Type()
)
tmnxOamPingResultsTtHCSumSquares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingResultsTtHCSumSquares.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingResultsTtHCSumSquares.setUnits("microseconds squared")
_TmnxOamPingResultsInTtOFSumSqrs_Type = Counter32
_TmnxOamPingResultsInTtOFSumSqrs_Object = MibTableColumn
tmnxOamPingResultsInTtOFSumSqrs = _TmnxOamPingResultsInTtOFSumSqrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1, 32),
    _TmnxOamPingResultsInTtOFSumSqrs_Type()
)
tmnxOamPingResultsInTtOFSumSqrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingResultsInTtOFSumSqrs.setStatus("current")
_TmnxOamPingResultsInTtHCSumSqrs_Type = Counter64
_TmnxOamPingResultsInTtHCSumSqrs_Object = MibTableColumn
tmnxOamPingResultsInTtHCSumSqrs = _TmnxOamPingResultsInTtHCSumSqrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1, 33),
    _TmnxOamPingResultsInTtHCSumSqrs_Type()
)
tmnxOamPingResultsInTtHCSumSqrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingResultsInTtHCSumSqrs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingResultsInTtHCSumSqrs.setUnits("microseconds squared")
_TmnxOamPingResultsTestRunResult_Type = TmnxOamTestResult
_TmnxOamPingResultsTestRunResult_Object = MibTableColumn
tmnxOamPingResultsTestRunResult = _TmnxOamPingResultsTestRunResult_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1, 34),
    _TmnxOamPingResultsTestRunResult_Type()
)
tmnxOamPingResultsTestRunResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingResultsTestRunResult.setStatus("current")
_TmnxOamPingResultsOutOfOrder_Type = Counter32
_TmnxOamPingResultsOutOfOrder_Object = MibTableColumn
tmnxOamPingResultsOutOfOrder = _TmnxOamPingResultsOutOfOrder_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1, 35),
    _TmnxOamPingResultsOutOfOrder_Type()
)
tmnxOamPingResultsOutOfOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingResultsOutOfOrder.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingResultsOutOfOrder.setUnits("reply PDUs")
_TmnxOamPingHistoryTable_Object = MibTable
tmnxOamPingHistoryTable = _TmnxOamPingHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5)
)
if mibBuilder.loadTexts:
    tmnxOamPingHistoryTable.setStatus("current")
_TmnxOamPingHistoryEntry_Object = MibTableRow
tmnxOamPingHistoryEntry = _TmnxOamPingHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5, 1)
)
tmnxOamPingHistoryEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTestIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsTestRunIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamPingHistoryEntry.setStatus("current")


class _TmnxOamPingHistoryIndex_Type(Unsigned32):
    """Custom type tmnxOamPingHistoryIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxOamPingHistoryIndex_Type.__name__ = "Unsigned32"
_TmnxOamPingHistoryIndex_Object = MibTableColumn
tmnxOamPingHistoryIndex = _TmnxOamPingHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5, 1, 1),
    _TmnxOamPingHistoryIndex_Type()
)
tmnxOamPingHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamPingHistoryIndex.setStatus("current")
_TmnxOamPingHistoryResponse_Type = Unsigned32
_TmnxOamPingHistoryResponse_Object = MibTableColumn
tmnxOamPingHistoryResponse = _TmnxOamPingHistoryResponse_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5, 1, 2),
    _TmnxOamPingHistoryResponse_Type()
)
tmnxOamPingHistoryResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingHistoryResponse.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingHistoryResponse.setUnits("microseconds")
_TmnxOamPingHistoryOneWayTime_Type = Integer32
_TmnxOamPingHistoryOneWayTime_Object = MibTableColumn
tmnxOamPingHistoryOneWayTime = _TmnxOamPingHistoryOneWayTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5, 1, 3),
    _TmnxOamPingHistoryOneWayTime_Type()
)
tmnxOamPingHistoryOneWayTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingHistoryOneWayTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingHistoryOneWayTime.setUnits("microseconds")
_TmnxOamPingHistorySize_Type = Unsigned32
_TmnxOamPingHistorySize_Object = MibTableColumn
tmnxOamPingHistorySize = _TmnxOamPingHistorySize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5, 1, 4),
    _TmnxOamPingHistorySize_Type()
)
tmnxOamPingHistorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingHistorySize.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingHistorySize.setUnits("octets")
_TmnxOamPingHistoryStatus_Type = TmnxOamResponseStatus
_TmnxOamPingHistoryStatus_Object = MibTableColumn
tmnxOamPingHistoryStatus = _TmnxOamPingHistoryStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5, 1, 5),
    _TmnxOamPingHistoryStatus_Type()
)
tmnxOamPingHistoryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingHistoryStatus.setStatus("current")
_TmnxOamPingHistoryTime_Type = DateAndTime
_TmnxOamPingHistoryTime_Object = MibTableColumn
tmnxOamPingHistoryTime = _TmnxOamPingHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5, 1, 6),
    _TmnxOamPingHistoryTime_Type()
)
tmnxOamPingHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingHistoryTime.setStatus("current")
_TmnxOamPingHistoryReturnCode_Type = TmnxOamPingRtnCode
_TmnxOamPingHistoryReturnCode_Object = MibTableColumn
tmnxOamPingHistoryReturnCode = _TmnxOamPingHistoryReturnCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5, 1, 7),
    _TmnxOamPingHistoryReturnCode_Type()
)
tmnxOamPingHistoryReturnCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingHistoryReturnCode.setStatus("current")
_TmnxOamPingHistorySrcIpAddress_Type = IpAddress
_TmnxOamPingHistorySrcIpAddress_Object = MibTableColumn
tmnxOamPingHistorySrcIpAddress = _TmnxOamPingHistorySrcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5, 1, 8),
    _TmnxOamPingHistorySrcIpAddress_Type()
)
tmnxOamPingHistorySrcIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingHistorySrcIpAddress.setStatus("obsolete")
_TmnxOamPingHistAddressType_Type = TmnxOamAddressType
_TmnxOamPingHistAddressType_Object = MibTableColumn
tmnxOamPingHistAddressType = _TmnxOamPingHistAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5, 1, 9),
    _TmnxOamPingHistAddressType_Type()
)
tmnxOamPingHistAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingHistAddressType.setStatus("current")
_TmnxOamPingHistSapId_Type = TmnxStrSapId
_TmnxOamPingHistSapId_Object = MibTableColumn
tmnxOamPingHistSapId = _TmnxOamPingHistSapId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5, 1, 10),
    _TmnxOamPingHistSapId_Type()
)
tmnxOamPingHistSapId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingHistSapId.setStatus("current")
_TmnxOamPingHistoryVersion_Type = Unsigned32
_TmnxOamPingHistoryVersion_Object = MibTableColumn
tmnxOamPingHistoryVersion = _TmnxOamPingHistoryVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5, 1, 12),
    _TmnxOamPingHistoryVersion_Type()
)
tmnxOamPingHistoryVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingHistoryVersion.setStatus("current")
_TmnxOamPingHistoryCpeMacAddr_Type = MacAddress
_TmnxOamPingHistoryCpeMacAddr_Object = MibTableColumn
tmnxOamPingHistoryCpeMacAddr = _TmnxOamPingHistoryCpeMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5, 1, 13),
    _TmnxOamPingHistoryCpeMacAddr_Type()
)
tmnxOamPingHistoryCpeMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingHistoryCpeMacAddr.setStatus("current")
_TmnxOamPingHistoryRespSvcId_Type = TmnxServId
_TmnxOamPingHistoryRespSvcId_Object = MibTableColumn
tmnxOamPingHistoryRespSvcId = _TmnxOamPingHistoryRespSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5, 1, 14),
    _TmnxOamPingHistoryRespSvcId_Type()
)
tmnxOamPingHistoryRespSvcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingHistoryRespSvcId.setStatus("current")
_TmnxOamPingHistorySequence_Type = Unsigned32
_TmnxOamPingHistorySequence_Object = MibTableColumn
tmnxOamPingHistorySequence = _TmnxOamPingHistorySequence_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5, 1, 15),
    _TmnxOamPingHistorySequence_Type()
)
tmnxOamPingHistorySequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingHistorySequence.setStatus("current")
_TmnxOamPingHistoryIfIndex_Type = InterfaceIndexOrZero
_TmnxOamPingHistoryIfIndex_Object = MibTableColumn
tmnxOamPingHistoryIfIndex = _TmnxOamPingHistoryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5, 1, 16),
    _TmnxOamPingHistoryIfIndex_Type()
)
tmnxOamPingHistoryIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingHistoryIfIndex.setStatus("current")
_TmnxOamPingHistoryDataLen_Type = Unsigned32
_TmnxOamPingHistoryDataLen_Object = MibTableColumn
tmnxOamPingHistoryDataLen = _TmnxOamPingHistoryDataLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5, 1, 17),
    _TmnxOamPingHistoryDataLen_Type()
)
tmnxOamPingHistoryDataLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingHistoryDataLen.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingHistoryDataLen.setUnits("octets")
_TmnxOamPingHistoryRespPlane_Type = TmnxOamTestResponsePlane
_TmnxOamPingHistoryRespPlane_Object = MibTableColumn
tmnxOamPingHistoryRespPlane = _TmnxOamPingHistoryRespPlane_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5, 1, 18),
    _TmnxOamPingHistoryRespPlane_Type()
)
tmnxOamPingHistoryRespPlane.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingHistoryRespPlane.setStatus("current")


class _TmnxOamPingHistoryReqHdr_Type(OctetString):
    """Custom type tmnxOamPingHistoryReqHdr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 150),
    )


_TmnxOamPingHistoryReqHdr_Type.__name__ = "OctetString"
_TmnxOamPingHistoryReqHdr_Object = MibTableColumn
tmnxOamPingHistoryReqHdr = _TmnxOamPingHistoryReqHdr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5, 1, 19),
    _TmnxOamPingHistoryReqHdr_Type()
)
tmnxOamPingHistoryReqHdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingHistoryReqHdr.setStatus("obsolete")


class _TmnxOamPingHistoryRespHdr_Type(OctetString):
    """Custom type tmnxOamPingHistoryRespHdr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 150),
    )


_TmnxOamPingHistoryRespHdr_Type.__name__ = "OctetString"
_TmnxOamPingHistoryRespHdr_Object = MibTableColumn
tmnxOamPingHistoryRespHdr = _TmnxOamPingHistoryRespHdr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5, 1, 20),
    _TmnxOamPingHistoryRespHdr_Type()
)
tmnxOamPingHistoryRespHdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingHistoryRespHdr.setStatus("current")
_TmnxOamPingHistoryDnsAddrType_Type = InetAddressType
_TmnxOamPingHistoryDnsAddrType_Object = MibTableColumn
tmnxOamPingHistoryDnsAddrType = _TmnxOamPingHistoryDnsAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5, 1, 21),
    _TmnxOamPingHistoryDnsAddrType_Type()
)
tmnxOamPingHistoryDnsAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingHistoryDnsAddrType.setStatus("current")


class _TmnxOamPingHistoryDnsAddress_Type(InetAddress):
    """Custom type tmnxOamPingHistoryDnsAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamPingHistoryDnsAddress_Type.__name__ = "InetAddress"
_TmnxOamPingHistoryDnsAddress_Object = MibTableColumn
tmnxOamPingHistoryDnsAddress = _TmnxOamPingHistoryDnsAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5, 1, 22),
    _TmnxOamPingHistoryDnsAddress_Type()
)
tmnxOamPingHistoryDnsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingHistoryDnsAddress.setStatus("current")
_TmnxOamPingHistorySrcAddrType_Type = InetAddressType
_TmnxOamPingHistorySrcAddrType_Object = MibTableColumn
tmnxOamPingHistorySrcAddrType = _TmnxOamPingHistorySrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5, 1, 23),
    _TmnxOamPingHistorySrcAddrType_Type()
)
tmnxOamPingHistorySrcAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingHistorySrcAddrType.setStatus("current")


class _TmnxOamPingHistorySrcAddress_Type(InetAddress):
    """Custom type tmnxOamPingHistorySrcAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxOamPingHistorySrcAddress_Type.__name__ = "InetAddress"
_TmnxOamPingHistorySrcAddress_Object = MibTableColumn
tmnxOamPingHistorySrcAddress = _TmnxOamPingHistorySrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5, 1, 24),
    _TmnxOamPingHistorySrcAddress_Type()
)
tmnxOamPingHistorySrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingHistorySrcAddress.setStatus("current")
_TmnxOamPingHistoryInOneWayTime_Type = Integer32
_TmnxOamPingHistoryInOneWayTime_Object = MibTableColumn
tmnxOamPingHistoryInOneWayTime = _TmnxOamPingHistoryInOneWayTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5, 1, 25),
    _TmnxOamPingHistoryInOneWayTime_Type()
)
tmnxOamPingHistoryInOneWayTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingHistoryInOneWayTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingHistoryInOneWayTime.setUnits("microseconds")
_TmnxOamPingHistoryLspName_Type = TLNamedItemOrEmpty
_TmnxOamPingHistoryLspName_Object = MibTableColumn
tmnxOamPingHistoryLspName = _TmnxOamPingHistoryLspName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5, 1, 26),
    _TmnxOamPingHistoryLspName_Type()
)
tmnxOamPingHistoryLspName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingHistoryLspName.setStatus("current")
_TmnxOamPingHistNextHopAddrType_Type = InetAddressType
_TmnxOamPingHistNextHopAddrType_Object = MibTableColumn
tmnxOamPingHistNextHopAddrType = _TmnxOamPingHistNextHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5, 1, 27),
    _TmnxOamPingHistNextHopAddrType_Type()
)
tmnxOamPingHistNextHopAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingHistNextHopAddrType.setStatus("current")


class _TmnxOamPingHistNextHopAddress_Type(InetAddress):
    """Custom type tmnxOamPingHistNextHopAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxOamPingHistNextHopAddress_Type.__name__ = "InetAddress"
_TmnxOamPingHistNextHopAddress_Object = MibTableColumn
tmnxOamPingHistNextHopAddress = _TmnxOamPingHistNextHopAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5, 1, 28),
    _TmnxOamPingHistNextHopAddress_Type()
)
tmnxOamPingHistNextHopAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingHistNextHopAddress.setStatus("current")
_TmnxOamPingHistorySrcGlobalId_Type = TmnxMplsTpGlobalID
_TmnxOamPingHistorySrcGlobalId_Object = MibTableColumn
tmnxOamPingHistorySrcGlobalId = _TmnxOamPingHistorySrcGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5, 1, 29),
    _TmnxOamPingHistorySrcGlobalId_Type()
)
tmnxOamPingHistorySrcGlobalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingHistorySrcGlobalId.setStatus("current")
_TmnxOamPingHistorySrcNodeId_Type = TmnxMplsTpNodeID
_TmnxOamPingHistorySrcNodeId_Object = MibTableColumn
tmnxOamPingHistorySrcNodeId = _TmnxOamPingHistorySrcNodeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5, 1, 30),
    _TmnxOamPingHistorySrcNodeId_Type()
)
tmnxOamPingHistorySrcNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingHistorySrcNodeId.setStatus("current")
_TmnxOamPingHistorySdpBindId_Type = TNamedItemOrEmpty
_TmnxOamPingHistorySdpBindId_Object = MibTableColumn
tmnxOamPingHistorySdpBindId = _TmnxOamPingHistorySdpBindId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5, 1, 31),
    _TmnxOamPingHistorySdpBindId_Type()
)
tmnxOamPingHistorySdpBindId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingHistorySdpBindId.setStatus("current")
_TmnxOamPingHistoryRtrnSubcode_Type = Unsigned32
_TmnxOamPingHistoryRtrnSubcode_Object = MibTableColumn
tmnxOamPingHistoryRtrnSubcode = _TmnxOamPingHistoryRtrnSubcode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5, 1, 32),
    _TmnxOamPingHistoryRtrnSubcode_Type()
)
tmnxOamPingHistoryRtrnSubcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingHistoryRtrnSubcode.setStatus("current")
_TmnxOamPingHistoryNetworkIfName_Type = TNamedItemOrEmpty
_TmnxOamPingHistoryNetworkIfName_Object = MibTableColumn
tmnxOamPingHistoryNetworkIfName = _TmnxOamPingHistoryNetworkIfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5, 1, 33),
    _TmnxOamPingHistoryNetworkIfName_Type()
)
tmnxOamPingHistoryNetworkIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingHistoryNetworkIfName.setStatus("current")
_TmnxOamMacPingCtlTable_Object = MibTable
tmnxOamMacPingCtlTable = _TmnxOamMacPingCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 6)
)
if mibBuilder.loadTexts:
    tmnxOamMacPingCtlTable.setStatus("current")
_TmnxOamMacPingCtlEntry_Object = MibTableRow
tmnxOamMacPingCtlEntry = _TmnxOamMacPingCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 6, 1)
)
tmnxOamMacPingCtlEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamMacPingCtlEntry.setStatus("current")


class _TmnxOamMacPingCtlTargetMacAddr_Type(MacAddress):
    """Custom type tmnxOamMacPingCtlTargetMacAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_TmnxOamMacPingCtlTargetMacAddr_Type.__name__ = "MacAddress"
_TmnxOamMacPingCtlTargetMacAddr_Object = MibTableColumn
tmnxOamMacPingCtlTargetMacAddr = _TmnxOamMacPingCtlTargetMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 6, 1, 1),
    _TmnxOamMacPingCtlTargetMacAddr_Type()
)
tmnxOamMacPingCtlTargetMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMacPingCtlTargetMacAddr.setStatus("current")


class _TmnxOamMacPingCtlSourceMacAddr_Type(MacAddress):
    """Custom type tmnxOamMacPingCtlSourceMacAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_TmnxOamMacPingCtlSourceMacAddr_Type.__name__ = "MacAddress"
_TmnxOamMacPingCtlSourceMacAddr_Object = MibTableColumn
tmnxOamMacPingCtlSourceMacAddr = _TmnxOamMacPingCtlSourceMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 6, 1, 2),
    _TmnxOamMacPingCtlSourceMacAddr_Type()
)
tmnxOamMacPingCtlSourceMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMacPingCtlSourceMacAddr.setStatus("current")


class _TmnxOamMacPingCtlSendControl_Type(TruthValue):
    """Custom type tmnxOamMacPingCtlSendControl based on TruthValue"""
    defaultValue = 2


_TmnxOamMacPingCtlSendControl_Type.__name__ = "TruthValue"
_TmnxOamMacPingCtlSendControl_Object = MibTableColumn
tmnxOamMacPingCtlSendControl = _TmnxOamMacPingCtlSendControl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 6, 1, 3),
    _TmnxOamMacPingCtlSendControl_Type()
)
tmnxOamMacPingCtlSendControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMacPingCtlSendControl.setStatus("current")


class _TmnxOamMacPingCtlReplyControl_Type(TruthValue):
    """Custom type tmnxOamMacPingCtlReplyControl based on TruthValue"""
    defaultValue = 2


_TmnxOamMacPingCtlReplyControl_Type.__name__ = "TruthValue"
_TmnxOamMacPingCtlReplyControl_Object = MibTableColumn
tmnxOamMacPingCtlReplyControl = _TmnxOamMacPingCtlReplyControl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 6, 1, 4),
    _TmnxOamMacPingCtlReplyControl_Type()
)
tmnxOamMacPingCtlReplyControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMacPingCtlReplyControl.setStatus("current")


class _TmnxOamMacPingCtlTtl_Type(Unsigned32):
    """Custom type tmnxOamMacPingCtlTtl based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TmnxOamMacPingCtlTtl_Type.__name__ = "Unsigned32"
_TmnxOamMacPingCtlTtl_Object = MibTableColumn
tmnxOamMacPingCtlTtl = _TmnxOamMacPingCtlTtl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 6, 1, 5),
    _TmnxOamMacPingCtlTtl_Type()
)
tmnxOamMacPingCtlTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMacPingCtlTtl.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamMacPingCtlTtl.setUnits("time-to-live value")


class _TmnxOamMacPingCtlRegister_Type(TruthValue):
    """Custom type tmnxOamMacPingCtlRegister based on TruthValue"""
    defaultValue = 2


_TmnxOamMacPingCtlRegister_Type.__name__ = "TruthValue"
_TmnxOamMacPingCtlRegister_Object = MibTableColumn
tmnxOamMacPingCtlRegister = _TmnxOamMacPingCtlRegister_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 6, 1, 6),
    _TmnxOamMacPingCtlRegister_Type()
)
tmnxOamMacPingCtlRegister.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMacPingCtlRegister.setStatus("current")


class _TmnxOamMacPingCtlFlood_Type(TruthValue):
    """Custom type tmnxOamMacPingCtlFlood based on TruthValue"""
    defaultValue = 2


_TmnxOamMacPingCtlFlood_Type.__name__ = "TruthValue"
_TmnxOamMacPingCtlFlood_Object = MibTableColumn
tmnxOamMacPingCtlFlood = _TmnxOamMacPingCtlFlood_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 6, 1, 7),
    _TmnxOamMacPingCtlFlood_Type()
)
tmnxOamMacPingCtlFlood.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMacPingCtlFlood.setStatus("current")


class _TmnxOamMacPingCtlForce_Type(TruthValue):
    """Custom type tmnxOamMacPingCtlForce based on TruthValue"""
    defaultValue = 2


_TmnxOamMacPingCtlForce_Type.__name__ = "TruthValue"
_TmnxOamMacPingCtlForce_Object = MibTableColumn
tmnxOamMacPingCtlForce = _TmnxOamMacPingCtlForce_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 6, 1, 8),
    _TmnxOamMacPingCtlForce_Type()
)
tmnxOamMacPingCtlForce.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMacPingCtlForce.setStatus("current")


class _TmnxOamMacPingCtlAge_Type(Unsigned32):
    """Custom type tmnxOamMacPingCtlAge based on Unsigned32"""
    defaultValue = 3600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmnxOamMacPingCtlAge_Type.__name__ = "Unsigned32"
_TmnxOamMacPingCtlAge_Object = MibTableColumn
tmnxOamMacPingCtlAge = _TmnxOamMacPingCtlAge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 6, 1, 9),
    _TmnxOamMacPingCtlAge_Type()
)
tmnxOamMacPingCtlAge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMacPingCtlAge.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamMacPingCtlAge.setUnits("seconds")


class _TmnxOamMacPingCtlSapPortId_Type(TmnxPortID):
    """Custom type tmnxOamMacPingCtlSapPortId based on TmnxPortID"""
    defaultValue = 0


_TmnxOamMacPingCtlSapPortId_Type.__name__ = "TmnxPortID"
_TmnxOamMacPingCtlSapPortId_Object = MibTableColumn
tmnxOamMacPingCtlSapPortId = _TmnxOamMacPingCtlSapPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 6, 1, 10),
    _TmnxOamMacPingCtlSapPortId_Type()
)
tmnxOamMacPingCtlSapPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMacPingCtlSapPortId.setStatus("current")


class _TmnxOamMacPingCtlSapEncapValue_Type(TmnxEncapVal):
    """Custom type tmnxOamMacPingCtlSapEncapValue based on TmnxEncapVal"""
    defaultValue = 0


_TmnxOamMacPingCtlSapEncapValue_Type.__name__ = "TmnxEncapVal"
_TmnxOamMacPingCtlSapEncapValue_Object = MibTableColumn
tmnxOamMacPingCtlSapEncapValue = _TmnxOamMacPingCtlSapEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 6, 1, 11),
    _TmnxOamMacPingCtlSapEncapValue_Type()
)
tmnxOamMacPingCtlSapEncapValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMacPingCtlSapEncapValue.setStatus("current")


class _TmnxOamMacPingCtlFibEntryName_Type(TNamedItemOrEmpty):
    """Custom type tmnxOamMacPingCtlFibEntryName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOamMacPingCtlFibEntryName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOamMacPingCtlFibEntryName_Object = MibTableColumn
tmnxOamMacPingCtlFibEntryName = _TmnxOamMacPingCtlFibEntryName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 6, 1, 12),
    _TmnxOamMacPingCtlFibEntryName_Type()
)
tmnxOamMacPingCtlFibEntryName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMacPingCtlFibEntryName.setStatus("obsolete")
_TmnxOamMacPingHistoryTable_Object = MibTable
tmnxOamMacPingHistoryTable = _TmnxOamMacPingHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 7)
)
if mibBuilder.loadTexts:
    tmnxOamMacPingHistoryTable.setStatus("current")
_TmnxOamMacPingHistoryEntry_Object = MibTableRow
tmnxOamMacPingHistoryEntry = _TmnxOamMacPingHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 7, 1)
)
tmnxOamMacPingHistoryEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTestIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsTestRunIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingHistoryIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingReplyIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamMacPingHistoryEntry.setStatus("current")


class _TmnxOamMacPingHistoryIndex_Type(Unsigned32):
    """Custom type tmnxOamMacPingHistoryIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxOamMacPingHistoryIndex_Type.__name__ = "Unsigned32"
_TmnxOamMacPingHistoryIndex_Object = MibTableColumn
tmnxOamMacPingHistoryIndex = _TmnxOamMacPingHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 7, 1, 1),
    _TmnxOamMacPingHistoryIndex_Type()
)
tmnxOamMacPingHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamMacPingHistoryIndex.setStatus("current")


class _TmnxOamMacPingReplyIndex_Type(Unsigned32):
    """Custom type tmnxOamMacPingReplyIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxOamMacPingReplyIndex_Type.__name__ = "Unsigned32"
_TmnxOamMacPingReplyIndex_Object = MibTableColumn
tmnxOamMacPingReplyIndex = _TmnxOamMacPingReplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 7, 1, 2),
    _TmnxOamMacPingReplyIndex_Type()
)
tmnxOamMacPingReplyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamMacPingReplyIndex.setStatus("current")
_TmnxOamMacPingHistoryResponse_Type = Unsigned32
_TmnxOamMacPingHistoryResponse_Object = MibTableColumn
tmnxOamMacPingHistoryResponse = _TmnxOamMacPingHistoryResponse_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 7, 1, 3),
    _TmnxOamMacPingHistoryResponse_Type()
)
tmnxOamMacPingHistoryResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacPingHistoryResponse.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamMacPingHistoryResponse.setUnits("microseconds")
_TmnxOamMacPingHistoryOneWayTime_Type = Integer32
_TmnxOamMacPingHistoryOneWayTime_Object = MibTableColumn
tmnxOamMacPingHistoryOneWayTime = _TmnxOamMacPingHistoryOneWayTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 7, 1, 4),
    _TmnxOamMacPingHistoryOneWayTime_Type()
)
tmnxOamMacPingHistoryOneWayTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacPingHistoryOneWayTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamMacPingHistoryOneWayTime.setUnits("microseconds")
_TmnxOamMacPingHistoryStatus_Type = TmnxOamResponseStatus
_TmnxOamMacPingHistoryStatus_Object = MibTableColumn
tmnxOamMacPingHistoryStatus = _TmnxOamMacPingHistoryStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 7, 1, 5),
    _TmnxOamMacPingHistoryStatus_Type()
)
tmnxOamMacPingHistoryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacPingHistoryStatus.setStatus("current")
_TmnxOamMacPingHistoryTime_Type = DateAndTime
_TmnxOamMacPingHistoryTime_Object = MibTableColumn
tmnxOamMacPingHistoryTime = _TmnxOamMacPingHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 7, 1, 6),
    _TmnxOamMacPingHistoryTime_Type()
)
tmnxOamMacPingHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacPingHistoryTime.setStatus("current")
_TmnxOamMacPingHistoryReturnCode_Type = TmnxOamPingRtnCode
_TmnxOamMacPingHistoryReturnCode_Object = MibTableColumn
tmnxOamMacPingHistoryReturnCode = _TmnxOamMacPingHistoryReturnCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 7, 1, 7),
    _TmnxOamMacPingHistoryReturnCode_Type()
)
tmnxOamMacPingHistoryReturnCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacPingHistoryReturnCode.setStatus("current")
_TmnxOamMacPingHistorySrcIpAddress_Type = IpAddress
_TmnxOamMacPingHistorySrcIpAddress_Object = MibTableColumn
tmnxOamMacPingHistorySrcIpAddress = _TmnxOamMacPingHistorySrcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 7, 1, 8),
    _TmnxOamMacPingHistorySrcIpAddress_Type()
)
tmnxOamMacPingHistorySrcIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacPingHistorySrcIpAddress.setStatus("obsolete")
_TmnxOamMacPingHistoryAddressType_Type = TmnxOamAddressType
_TmnxOamMacPingHistoryAddressType_Object = MibTableColumn
tmnxOamMacPingHistoryAddressType = _TmnxOamMacPingHistoryAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 7, 1, 9),
    _TmnxOamMacPingHistoryAddressType_Type()
)
tmnxOamMacPingHistoryAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacPingHistoryAddressType.setStatus("current")
_TmnxOamMacPingHistorySapId_Type = TmnxStrSapId
_TmnxOamMacPingHistorySapId_Object = MibTableColumn
tmnxOamMacPingHistorySapId = _TmnxOamMacPingHistorySapId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 7, 1, 10),
    _TmnxOamMacPingHistorySapId_Type()
)
tmnxOamMacPingHistorySapId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacPingHistorySapId.setStatus("current")
_TmnxOamMacPingHistorySdpId_Type = SdpId
_TmnxOamMacPingHistorySdpId_Object = MibTableColumn
tmnxOamMacPingHistorySdpId = _TmnxOamMacPingHistorySdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 7, 1, 12),
    _TmnxOamMacPingHistorySdpId_Type()
)
tmnxOamMacPingHistorySdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacPingHistorySdpId.setStatus("current")
_TmnxOamMacPingHistoryAdminStatus_Type = TruthValue
_TmnxOamMacPingHistoryAdminStatus_Object = MibTableColumn
tmnxOamMacPingHistoryAdminStatus = _TmnxOamMacPingHistoryAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 7, 1, 13),
    _TmnxOamMacPingHistoryAdminStatus_Type()
)
tmnxOamMacPingHistoryAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacPingHistoryAdminStatus.setStatus("current")
_TmnxOamMacPingHistoryOperStatus_Type = TruthValue
_TmnxOamMacPingHistoryOperStatus_Object = MibTableColumn
tmnxOamMacPingHistoryOperStatus = _TmnxOamMacPingHistoryOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 7, 1, 14),
    _TmnxOamMacPingHistoryOperStatus_Type()
)
tmnxOamMacPingHistoryOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacPingHistoryOperStatus.setStatus("current")
_TmnxOamMacPingHistoryResponsePlane_Type = TmnxOamTestResponsePlane
_TmnxOamMacPingHistoryResponsePlane_Object = MibTableColumn
tmnxOamMacPingHistoryResponsePlane = _TmnxOamMacPingHistoryResponsePlane_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 7, 1, 15),
    _TmnxOamMacPingHistoryResponsePlane_Type()
)
tmnxOamMacPingHistoryResponsePlane.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacPingHistoryResponsePlane.setStatus("current")
_TmnxOamMacPingHistorySize_Type = Unsigned32
_TmnxOamMacPingHistorySize_Object = MibTableColumn
tmnxOamMacPingHistorySize = _TmnxOamMacPingHistorySize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 7, 1, 16),
    _TmnxOamMacPingHistorySize_Type()
)
tmnxOamMacPingHistorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacPingHistorySize.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamMacPingHistorySize.setUnits("octets")
_TmnxOamMacPingHistoryInOneWayTime_Type = Integer32
_TmnxOamMacPingHistoryInOneWayTime_Object = MibTableColumn
tmnxOamMacPingHistoryInOneWayTime = _TmnxOamMacPingHistoryInOneWayTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 7, 1, 17),
    _TmnxOamMacPingHistoryInOneWayTime_Type()
)
tmnxOamMacPingHistoryInOneWayTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacPingHistoryInOneWayTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamMacPingHistoryInOneWayTime.setUnits("microseconds")
_TmnxOamMacPingHistorySrcAddrType_Type = InetAddressType
_TmnxOamMacPingHistorySrcAddrType_Object = MibTableColumn
tmnxOamMacPingHistorySrcAddrType = _TmnxOamMacPingHistorySrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 7, 1, 18),
    _TmnxOamMacPingHistorySrcAddrType_Type()
)
tmnxOamMacPingHistorySrcAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacPingHistorySrcAddrType.setStatus("current")


class _TmnxOamMacPingHistorySrcAddress_Type(InetAddress):
    """Custom type tmnxOamMacPingHistorySrcAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamMacPingHistorySrcAddress_Type.__name__ = "InetAddress"
_TmnxOamMacPingHistorySrcAddress_Object = MibTableColumn
tmnxOamMacPingHistorySrcAddress = _TmnxOamMacPingHistorySrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 7, 1, 19),
    _TmnxOamMacPingHistorySrcAddress_Type()
)
tmnxOamMacPingHistorySrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacPingHistorySrcAddress.setStatus("current")
_TmnxOamMacPingL2MapTable_Object = MibTable
tmnxOamMacPingL2MapTable = _TmnxOamMacPingL2MapTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 8)
)
if mibBuilder.loadTexts:
    tmnxOamMacPingL2MapTable.setStatus("obsolete")
_TmnxOamMacPingL2MapEntry_Object = MibTableRow
tmnxOamMacPingL2MapEntry = _TmnxOamMacPingL2MapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 8, 1)
)
tmnxOamMacPingL2MapEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTestIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsTestRunIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingHistoryIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingReplyIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingL2MapIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamMacPingL2MapEntry.setStatus("obsolete")


class _TmnxOamMacPingL2MapIndex_Type(Unsigned32):
    """Custom type tmnxOamMacPingL2MapIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxOamMacPingL2MapIndex_Type.__name__ = "Unsigned32"
_TmnxOamMacPingL2MapIndex_Object = MibTableColumn
tmnxOamMacPingL2MapIndex = _TmnxOamMacPingL2MapIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 8, 1, 1),
    _TmnxOamMacPingL2MapIndex_Type()
)
tmnxOamMacPingL2MapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamMacPingL2MapIndex.setStatus("obsolete")
_TmnxOamMacPingL2MapRouterID_Type = IpAddress
_TmnxOamMacPingL2MapRouterID_Object = MibTableColumn
tmnxOamMacPingL2MapRouterID = _TmnxOamMacPingL2MapRouterID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 8, 1, 2),
    _TmnxOamMacPingL2MapRouterID_Type()
)
tmnxOamMacPingL2MapRouterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacPingL2MapRouterID.setStatus("obsolete")
_TmnxOamMacPingL2MapLabel_Type = MplsLabel
_TmnxOamMacPingL2MapLabel_Object = MibTableColumn
tmnxOamMacPingL2MapLabel = _TmnxOamMacPingL2MapLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 8, 1, 3),
    _TmnxOamMacPingL2MapLabel_Type()
)
tmnxOamMacPingL2MapLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacPingL2MapLabel.setStatus("obsolete")
_TmnxOamMacPingL2MapProtocol_Type = TmnxOamSignalProtocol
_TmnxOamMacPingL2MapProtocol_Object = MibTableColumn
tmnxOamMacPingL2MapProtocol = _TmnxOamMacPingL2MapProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 8, 1, 4),
    _TmnxOamMacPingL2MapProtocol_Type()
)
tmnxOamMacPingL2MapProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacPingL2MapProtocol.setStatus("obsolete")
_TmnxOamMacPingL2MapVCType_Type = TmnxOamVcType
_TmnxOamMacPingL2MapVCType_Object = MibTableColumn
tmnxOamMacPingL2MapVCType = _TmnxOamMacPingL2MapVCType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 8, 1, 5),
    _TmnxOamMacPingL2MapVCType_Type()
)
tmnxOamMacPingL2MapVCType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacPingL2MapVCType.setStatus("obsolete")
_TmnxOamMacPingL2MapVCID_Type = TmnxVcId
_TmnxOamMacPingL2MapVCID_Object = MibTableColumn
tmnxOamMacPingL2MapVCID = _TmnxOamMacPingL2MapVCID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 8, 1, 6),
    _TmnxOamMacPingL2MapVCID_Type()
)
tmnxOamMacPingL2MapVCID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacPingL2MapVCID.setStatus("obsolete")


class _TmnxOamMacPingL2MapDirection_Type(Integer32):
    """Custom type tmnxOamMacPingL2MapDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("upstream", 1),
          ("downstream", 2))
    )


_TmnxOamMacPingL2MapDirection_Type.__name__ = "Integer32"
_TmnxOamMacPingL2MapDirection_Object = MibTableColumn
tmnxOamMacPingL2MapDirection = _TmnxOamMacPingL2MapDirection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 8, 1, 7),
    _TmnxOamMacPingL2MapDirection_Type()
)
tmnxOamMacPingL2MapDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacPingL2MapDirection.setStatus("obsolete")
_TmnxOamLspPingCtlTable_Object = MibTable
tmnxOamLspPingCtlTable = _TmnxOamLspPingCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 9)
)
if mibBuilder.loadTexts:
    tmnxOamLspPingCtlTable.setStatus("current")
_TmnxOamLspPingCtlEntry_Object = MibTableRow
tmnxOamLspPingCtlEntry = _TmnxOamLspPingCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 9, 1)
)
tmnxOamLspPingCtlEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamLspPingCtlEntry.setStatus("current")


class _TmnxOamLspPingCtlVRtrID_Type(TmnxVRtrID):
    """Custom type tmnxOamLspPingCtlVRtrID based on TmnxVRtrID"""
    defaultValue = 1


_TmnxOamLspPingCtlVRtrID_Type.__name__ = "TmnxVRtrID"
_TmnxOamLspPingCtlVRtrID_Object = MibTableColumn
tmnxOamLspPingCtlVRtrID = _TmnxOamLspPingCtlVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 9, 1, 1),
    _TmnxOamLspPingCtlVRtrID_Type()
)
tmnxOamLspPingCtlVRtrID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspPingCtlVRtrID.setStatus("obsolete")


class _TmnxOamLspPingCtlLspName_Type(TLNamedItemOrEmpty):
    """Custom type tmnxOamLspPingCtlLspName based on TLNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOamLspPingCtlLspName_Type.__name__ = "TLNamedItemOrEmpty"
_TmnxOamLspPingCtlLspName_Object = MibTableColumn
tmnxOamLspPingCtlLspName = _TmnxOamLspPingCtlLspName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 9, 1, 2),
    _TmnxOamLspPingCtlLspName_Type()
)
tmnxOamLspPingCtlLspName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspPingCtlLspName.setStatus("current")


class _TmnxOamLspPingCtlReturnLsp_Type(TNamedItemOrEmpty):
    """Custom type tmnxOamLspPingCtlReturnLsp based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOamLspPingCtlReturnLsp_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOamLspPingCtlReturnLsp_Object = MibTableColumn
tmnxOamLspPingCtlReturnLsp = _TmnxOamLspPingCtlReturnLsp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 9, 1, 3),
    _TmnxOamLspPingCtlReturnLsp_Type()
)
tmnxOamLspPingCtlReturnLsp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspPingCtlReturnLsp.setStatus("obsolete")


class _TmnxOamLspPingCtlTtl_Type(Unsigned32):
    """Custom type tmnxOamLspPingCtlTtl based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TmnxOamLspPingCtlTtl_Type.__name__ = "Unsigned32"
_TmnxOamLspPingCtlTtl_Object = MibTableColumn
tmnxOamLspPingCtlTtl = _TmnxOamLspPingCtlTtl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 9, 1, 4),
    _TmnxOamLspPingCtlTtl_Type()
)
tmnxOamLspPingCtlTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspPingCtlTtl.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamLspPingCtlTtl.setUnits("time-to-live value")


class _TmnxOamLspPingCtlPathName_Type(TLNamedItemOrEmpty):
    """Custom type tmnxOamLspPingCtlPathName based on TLNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOamLspPingCtlPathName_Type.__name__ = "TLNamedItemOrEmpty"
_TmnxOamLspPingCtlPathName_Object = MibTableColumn
tmnxOamLspPingCtlPathName = _TmnxOamLspPingCtlPathName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 9, 1, 5),
    _TmnxOamLspPingCtlPathName_Type()
)
tmnxOamLspPingCtlPathName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspPingCtlPathName.setStatus("current")


class _TmnxOamLspPingCtlLdpIpPrefix_Type(IpAddress):
    """Custom type tmnxOamLspPingCtlLdpIpPrefix based on IpAddress"""
    defaultHexValue = "00000000"


_TmnxOamLspPingCtlLdpIpPrefix_Type.__name__ = "IpAddress"
_TmnxOamLspPingCtlLdpIpPrefix_Object = MibTableColumn
tmnxOamLspPingCtlLdpIpPrefix = _TmnxOamLspPingCtlLdpIpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 9, 1, 6),
    _TmnxOamLspPingCtlLdpIpPrefix_Type()
)
tmnxOamLspPingCtlLdpIpPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspPingCtlLdpIpPrefix.setStatus("obsolete")


class _TmnxOamLspPingCtlLdpIpPrefixLen_Type(IpAddressPrefixLength):
    """Custom type tmnxOamLspPingCtlLdpIpPrefixLen based on IpAddressPrefixLength"""
    defaultValue = 32


_TmnxOamLspPingCtlLdpIpPrefixLen_Type.__name__ = "IpAddressPrefixLength"
_TmnxOamLspPingCtlLdpIpPrefixLen_Object = MibTableColumn
tmnxOamLspPingCtlLdpIpPrefixLen = _TmnxOamLspPingCtlLdpIpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 9, 1, 7),
    _TmnxOamLspPingCtlLdpIpPrefixLen_Type()
)
tmnxOamLspPingCtlLdpIpPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspPingCtlLdpIpPrefixLen.setStatus("obsolete")


class _TmnxOamLspPingCtlLdpPrefixType_Type(InetAddressType):
    """Custom type tmnxOamLspPingCtlLdpPrefixType based on InetAddressType"""
    defaultValue = 0


_TmnxOamLspPingCtlLdpPrefixType_Type.__name__ = "InetAddressType"
_TmnxOamLspPingCtlLdpPrefixType_Object = MibTableColumn
tmnxOamLspPingCtlLdpPrefixType = _TmnxOamLspPingCtlLdpPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 9, 1, 8),
    _TmnxOamLspPingCtlLdpPrefixType_Type()
)
tmnxOamLspPingCtlLdpPrefixType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspPingCtlLdpPrefixType.setStatus("current")


class _TmnxOamLspPingCtlLdpPrefix_Type(InetAddress):
    """Custom type tmnxOamLspPingCtlLdpPrefix based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamLspPingCtlLdpPrefix_Type.__name__ = "InetAddress"
_TmnxOamLspPingCtlLdpPrefix_Object = MibTableColumn
tmnxOamLspPingCtlLdpPrefix = _TmnxOamLspPingCtlLdpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 9, 1, 9),
    _TmnxOamLspPingCtlLdpPrefix_Type()
)
tmnxOamLspPingCtlLdpPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspPingCtlLdpPrefix.setStatus("current")


class _TmnxOamLspPingCtlLdpPrefixLen_Type(InetAddressPrefixLength):
    """Custom type tmnxOamLspPingCtlLdpPrefixLen based on InetAddressPrefixLength"""
    defaultValue = 32


_TmnxOamLspPingCtlLdpPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxOamLspPingCtlLdpPrefixLen_Object = MibTableColumn
tmnxOamLspPingCtlLdpPrefixLen = _TmnxOamLspPingCtlLdpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 9, 1, 10),
    _TmnxOamLspPingCtlLdpPrefixLen_Type()
)
tmnxOamLspPingCtlLdpPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspPingCtlLdpPrefixLen.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamLspPingCtlLdpPrefixLen.setUnits("bits")


class _TmnxOamLspPingCtlPathDestType_Type(InetAddressType):
    """Custom type tmnxOamLspPingCtlPathDestType based on InetAddressType"""
    defaultValue = 0


_TmnxOamLspPingCtlPathDestType_Type.__name__ = "InetAddressType"
_TmnxOamLspPingCtlPathDestType_Object = MibTableColumn
tmnxOamLspPingCtlPathDestType = _TmnxOamLspPingCtlPathDestType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 9, 1, 11),
    _TmnxOamLspPingCtlPathDestType_Type()
)
tmnxOamLspPingCtlPathDestType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspPingCtlPathDestType.setStatus("current")


class _TmnxOamLspPingCtlPathDest_Type(InetAddress):
    """Custom type tmnxOamLspPingCtlPathDest based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamLspPingCtlPathDest_Type.__name__ = "InetAddress"
_TmnxOamLspPingCtlPathDest_Object = MibTableColumn
tmnxOamLspPingCtlPathDest = _TmnxOamLspPingCtlPathDest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 9, 1, 12),
    _TmnxOamLspPingCtlPathDest_Type()
)
tmnxOamLspPingCtlPathDest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspPingCtlPathDest.setStatus("current")


class _TmnxOamLspPingCtlNhIntfName_Type(TNamedItemOrEmpty):
    """Custom type tmnxOamLspPingCtlNhIntfName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOamLspPingCtlNhIntfName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOamLspPingCtlNhIntfName_Object = MibTableColumn
tmnxOamLspPingCtlNhIntfName = _TmnxOamLspPingCtlNhIntfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 9, 1, 13),
    _TmnxOamLspPingCtlNhIntfName_Type()
)
tmnxOamLspPingCtlNhIntfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspPingCtlNhIntfName.setStatus("current")


class _TmnxOamLspPingCtlNhAddressType_Type(InetAddressType):
    """Custom type tmnxOamLspPingCtlNhAddressType based on InetAddressType"""
    defaultValue = 0


_TmnxOamLspPingCtlNhAddressType_Type.__name__ = "InetAddressType"
_TmnxOamLspPingCtlNhAddressType_Object = MibTableColumn
tmnxOamLspPingCtlNhAddressType = _TmnxOamLspPingCtlNhAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 9, 1, 14),
    _TmnxOamLspPingCtlNhAddressType_Type()
)
tmnxOamLspPingCtlNhAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspPingCtlNhAddressType.setStatus("current")


class _TmnxOamLspPingCtlNhAddress_Type(InetAddress):
    """Custom type tmnxOamLspPingCtlNhAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamLspPingCtlNhAddress_Type.__name__ = "InetAddress"
_TmnxOamLspPingCtlNhAddress_Object = MibTableColumn
tmnxOamLspPingCtlNhAddress = _TmnxOamLspPingCtlNhAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 9, 1, 15),
    _TmnxOamLspPingCtlNhAddress_Type()
)
tmnxOamLspPingCtlNhAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspPingCtlNhAddress.setStatus("current")


class _TmnxOamLspPingCtlTestSubMode_Type(TmnxOamLspTestSubMode):
    """Custom type tmnxOamLspPingCtlTestSubMode based on TmnxOamLspTestSubMode"""
    defaultValue = 1


_TmnxOamLspPingCtlTestSubMode_Type.__name__ = "TmnxOamLspTestSubMode"
_TmnxOamLspPingCtlTestSubMode_Object = MibTableColumn
tmnxOamLspPingCtlTestSubMode = _TmnxOamLspPingCtlTestSubMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 9, 1, 16),
    _TmnxOamLspPingCtlTestSubMode_Type()
)
tmnxOamLspPingCtlTestSubMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspPingCtlTestSubMode.setStatus("current")


class _TmnxOamLspPingCtlMplsTpPathType_Type(TmnxOamMplsTpPathType):
    """Custom type tmnxOamLspPingCtlMplsTpPathType based on TmnxOamMplsTpPathType"""
    defaultValue = 3


_TmnxOamLspPingCtlMplsTpPathType_Type.__name__ = "TmnxOamMplsTpPathType"
_TmnxOamLspPingCtlMplsTpPathType_Object = MibTableColumn
tmnxOamLspPingCtlMplsTpPathType = _TmnxOamLspPingCtlMplsTpPathType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 9, 1, 17),
    _TmnxOamLspPingCtlMplsTpPathType_Type()
)
tmnxOamLspPingCtlMplsTpPathType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspPingCtlMplsTpPathType.setStatus("current")


class _TmnxOamLspPingCtlMplsTpGlobalId_Type(TmnxMplsTpGlobalID):
    """Custom type tmnxOamLspPingCtlMplsTpGlobalId based on TmnxMplsTpGlobalID"""
    defaultValue = 0


_TmnxOamLspPingCtlMplsTpGlobalId_Type.__name__ = "TmnxMplsTpGlobalID"
_TmnxOamLspPingCtlMplsTpGlobalId_Object = MibTableColumn
tmnxOamLspPingCtlMplsTpGlobalId = _TmnxOamLspPingCtlMplsTpGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 9, 1, 18),
    _TmnxOamLspPingCtlMplsTpGlobalId_Type()
)
tmnxOamLspPingCtlMplsTpGlobalId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspPingCtlMplsTpGlobalId.setStatus("current")


class _TmnxOamLspPingCtlMplsTpNodeId_Type(TmnxMplsTpNodeID):
    """Custom type tmnxOamLspPingCtlMplsTpNodeId based on TmnxMplsTpNodeID"""
    defaultValue = 0


_TmnxOamLspPingCtlMplsTpNodeId_Type.__name__ = "TmnxMplsTpNodeID"
_TmnxOamLspPingCtlMplsTpNodeId_Object = MibTableColumn
tmnxOamLspPingCtlMplsTpNodeId = _TmnxOamLspPingCtlMplsTpNodeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 9, 1, 19),
    _TmnxOamLspPingCtlMplsTpNodeId_Type()
)
tmnxOamLspPingCtlMplsTpNodeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspPingCtlMplsTpNodeId.setStatus("current")


class _TmnxOamLspPingCtlAssocChannel_Type(TmnxOamLspAssocChannel):
    """Custom type tmnxOamLspPingCtlAssocChannel based on TmnxOamLspAssocChannel"""
    defaultValue = 1


_TmnxOamLspPingCtlAssocChannel_Type.__name__ = "TmnxOamLspAssocChannel"
_TmnxOamLspPingCtlAssocChannel_Object = MibTableColumn
tmnxOamLspPingCtlAssocChannel = _TmnxOamLspPingCtlAssocChannel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 9, 1, 20),
    _TmnxOamLspPingCtlAssocChannel_Type()
)
tmnxOamLspPingCtlAssocChannel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspPingCtlAssocChannel.setStatus("current")


class _TmnxOamLspPingCtlForce_Type(TruthValue):
    """Custom type tmnxOamLspPingCtlForce based on TruthValue"""
    defaultValue = 2


_TmnxOamLspPingCtlForce_Type.__name__ = "TruthValue"
_TmnxOamLspPingCtlForce_Object = MibTableColumn
tmnxOamLspPingCtlForce = _TmnxOamLspPingCtlForce_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 9, 1, 21),
    _TmnxOamLspPingCtlForce_Type()
)
tmnxOamLspPingCtlForce.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspPingCtlForce.setStatus("current")


class _TmnxOamLspPingCtlIgpInstance_Type(TmnxIgpInstance):
    """Custom type tmnxOamLspPingCtlIgpInstance based on TmnxIgpInstance"""
    defaultValue = 0


_TmnxOamLspPingCtlIgpInstance_Type.__name__ = "TmnxIgpInstance"
_TmnxOamLspPingCtlIgpInstance_Object = MibTableColumn
tmnxOamLspPingCtlIgpInstance = _TmnxOamLspPingCtlIgpInstance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 9, 1, 22),
    _TmnxOamLspPingCtlIgpInstance_Type()
)
tmnxOamLspPingCtlIgpInstance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspPingCtlIgpInstance.setStatus("current")


class _TmnxOamLspPingCtlSrPlcyColor_Type(Unsigned32):
    """Custom type tmnxOamLspPingCtlSrPlcyColor based on Unsigned32"""
    defaultValue = 0


_TmnxOamLspPingCtlSrPlcyColor_Type.__name__ = "Unsigned32"
_TmnxOamLspPingCtlSrPlcyColor_Object = MibTableColumn
tmnxOamLspPingCtlSrPlcyColor = _TmnxOamLspPingCtlSrPlcyColor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 9, 1, 23),
    _TmnxOamLspPingCtlSrPlcyColor_Type()
)
tmnxOamLspPingCtlSrPlcyColor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspPingCtlSrPlcyColor.setStatus("current")


class _TmnxOamLspPingCtlSrPlcyEndPtAddT_Type(InetAddressType):
    """Custom type tmnxOamLspPingCtlSrPlcyEndPtAddT based on InetAddressType"""
    defaultValue = 0


_TmnxOamLspPingCtlSrPlcyEndPtAddT_Type.__name__ = "InetAddressType"
_TmnxOamLspPingCtlSrPlcyEndPtAddT_Object = MibTableColumn
tmnxOamLspPingCtlSrPlcyEndPtAddT = _TmnxOamLspPingCtlSrPlcyEndPtAddT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 9, 1, 24),
    _TmnxOamLspPingCtlSrPlcyEndPtAddT_Type()
)
tmnxOamLspPingCtlSrPlcyEndPtAddT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspPingCtlSrPlcyEndPtAddT.setStatus("current")


class _TmnxOamLspPingCtlSrPlcyEndPtAddr_Type(InetAddress):
    """Custom type tmnxOamLspPingCtlSrPlcyEndPtAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamLspPingCtlSrPlcyEndPtAddr_Type.__name__ = "InetAddress"
_TmnxOamLspPingCtlSrPlcyEndPtAddr_Object = MibTableColumn
tmnxOamLspPingCtlSrPlcyEndPtAddr = _TmnxOamLspPingCtlSrPlcyEndPtAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 9, 1, 25),
    _TmnxOamLspPingCtlSrPlcyEndPtAddr_Type()
)
tmnxOamLspPingCtlSrPlcyEndPtAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspPingCtlSrPlcyEndPtAddr.setStatus("current")


class _TmnxOamLspPingCtlSrPlcySegList_Type(Unsigned32):
    """Custom type tmnxOamLspPingCtlSrPlcySegList based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_TmnxOamLspPingCtlSrPlcySegList_Type.__name__ = "Unsigned32"
_TmnxOamLspPingCtlSrPlcySegList_Object = MibTableColumn
tmnxOamLspPingCtlSrPlcySegList = _TmnxOamLspPingCtlSrPlcySegList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 9, 1, 26),
    _TmnxOamLspPingCtlSrPlcySegList_Type()
)
tmnxOamLspPingCtlSrPlcySegList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspPingCtlSrPlcySegList.setStatus("current")
_TmnxOamVprnPingCtlTable_Object = MibTable
tmnxOamVprnPingCtlTable = _TmnxOamVprnPingCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 10)
)
if mibBuilder.loadTexts:
    tmnxOamVprnPingCtlTable.setStatus("current")
_TmnxOamVprnPingCtlEntry_Object = MibTableRow
tmnxOamVprnPingCtlEntry = _TmnxOamVprnPingCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 10, 1)
)
tmnxOamVprnPingCtlEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamVprnPingCtlEntry.setStatus("current")


class _TmnxOamVprnPingCtlSourceIpAddr_Type(IpAddress):
    """Custom type tmnxOamVprnPingCtlSourceIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_TmnxOamVprnPingCtlSourceIpAddr_Type.__name__ = "IpAddress"
_TmnxOamVprnPingCtlSourceIpAddr_Object = MibTableColumn
tmnxOamVprnPingCtlSourceIpAddr = _TmnxOamVprnPingCtlSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 10, 1, 1),
    _TmnxOamVprnPingCtlSourceIpAddr_Type()
)
tmnxOamVprnPingCtlSourceIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamVprnPingCtlSourceIpAddr.setStatus("obsolete")


class _TmnxOamVprnPingCtlReplyControl_Type(TruthValue):
    """Custom type tmnxOamVprnPingCtlReplyControl based on TruthValue"""
    defaultValue = 2


_TmnxOamVprnPingCtlReplyControl_Type.__name__ = "TruthValue"
_TmnxOamVprnPingCtlReplyControl_Object = MibTableColumn
tmnxOamVprnPingCtlReplyControl = _TmnxOamVprnPingCtlReplyControl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 10, 1, 2),
    _TmnxOamVprnPingCtlReplyControl_Type()
)
tmnxOamVprnPingCtlReplyControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamVprnPingCtlReplyControl.setStatus("current")


class _TmnxOamVprnPingCtlTtl_Type(Unsigned32):
    """Custom type tmnxOamVprnPingCtlTtl based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TmnxOamVprnPingCtlTtl_Type.__name__ = "Unsigned32"
_TmnxOamVprnPingCtlTtl_Object = MibTableColumn
tmnxOamVprnPingCtlTtl = _TmnxOamVprnPingCtlTtl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 10, 1, 3),
    _TmnxOamVprnPingCtlTtl_Type()
)
tmnxOamVprnPingCtlTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamVprnPingCtlTtl.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamVprnPingCtlTtl.setUnits("time-to-live value")


class _TmnxOamVprnPingCtlSrcAddrType_Type(InetAddressType):
    """Custom type tmnxOamVprnPingCtlSrcAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxOamVprnPingCtlSrcAddrType_Type.__name__ = "InetAddressType"
_TmnxOamVprnPingCtlSrcAddrType_Object = MibTableColumn
tmnxOamVprnPingCtlSrcAddrType = _TmnxOamVprnPingCtlSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 10, 1, 4),
    _TmnxOamVprnPingCtlSrcAddrType_Type()
)
tmnxOamVprnPingCtlSrcAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamVprnPingCtlSrcAddrType.setStatus("current")


class _TmnxOamVprnPingCtlSrcAddress_Type(InetAddress):
    """Custom type tmnxOamVprnPingCtlSrcAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamVprnPingCtlSrcAddress_Type.__name__ = "InetAddress"
_TmnxOamVprnPingCtlSrcAddress_Object = MibTableColumn
tmnxOamVprnPingCtlSrcAddress = _TmnxOamVprnPingCtlSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 10, 1, 5),
    _TmnxOamVprnPingCtlSrcAddress_Type()
)
tmnxOamVprnPingCtlSrcAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamVprnPingCtlSrcAddress.setStatus("current")
_TmnxOamAtmPingCtlTable_Object = MibTable
tmnxOamAtmPingCtlTable = _TmnxOamAtmPingCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 11)
)
if mibBuilder.loadTexts:
    tmnxOamAtmPingCtlTable.setStatus("current")
_TmnxOamAtmPingCtlEntry_Object = MibTableRow
tmnxOamAtmPingCtlEntry = _TmnxOamAtmPingCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 11, 1)
)
tmnxOamAtmPingCtlEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamAtmPingCtlEntry.setStatus("current")


class _TmnxOamAtmPingCtlPortId_Type(TmnxPortID):
    """Custom type tmnxOamAtmPingCtlPortId based on TmnxPortID"""
    defaultValue = 0


_TmnxOamAtmPingCtlPortId_Type.__name__ = "TmnxPortID"
_TmnxOamAtmPingCtlPortId_Object = MibTableColumn
tmnxOamAtmPingCtlPortId = _TmnxOamAtmPingCtlPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 11, 1, 1),
    _TmnxOamAtmPingCtlPortId_Type()
)
tmnxOamAtmPingCtlPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamAtmPingCtlPortId.setStatus("current")


class _TmnxOamAtmPingCtlVpi_Type(AtmVpIdentifier):
    """Custom type tmnxOamAtmPingCtlVpi based on AtmVpIdentifier"""
    defaultValue = 0


_TmnxOamAtmPingCtlVpi_Type.__name__ = "AtmVpIdentifier"
_TmnxOamAtmPingCtlVpi_Object = MibTableColumn
tmnxOamAtmPingCtlVpi = _TmnxOamAtmPingCtlVpi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 11, 1, 2),
    _TmnxOamAtmPingCtlVpi_Type()
)
tmnxOamAtmPingCtlVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamAtmPingCtlVpi.setStatus("current")


class _TmnxOamAtmPingCtlVci_Type(AtmVcIdentifier):
    """Custom type tmnxOamAtmPingCtlVci based on AtmVcIdentifier"""
    defaultValue = 0


_TmnxOamAtmPingCtlVci_Type.__name__ = "AtmVcIdentifier"
_TmnxOamAtmPingCtlVci_Object = MibTableColumn
tmnxOamAtmPingCtlVci = _TmnxOamAtmPingCtlVci_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 11, 1, 3),
    _TmnxOamAtmPingCtlVci_Type()
)
tmnxOamAtmPingCtlVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamAtmPingCtlVci.setStatus("current")


class _TmnxOamAtmPingCtlLpbkLocation_Type(OctetString):
    """Custom type tmnxOamAtmPingCtlLpbkLocation based on OctetString"""
    defaultHexValue = "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_TmnxOamAtmPingCtlLpbkLocation_Type.__name__ = "OctetString"
_TmnxOamAtmPingCtlLpbkLocation_Object = MibTableColumn
tmnxOamAtmPingCtlLpbkLocation = _TmnxOamAtmPingCtlLpbkLocation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 11, 1, 4),
    _TmnxOamAtmPingCtlLpbkLocation_Type()
)
tmnxOamAtmPingCtlLpbkLocation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamAtmPingCtlLpbkLocation.setStatus("current")


class _TmnxOamAtmPingCtlSegment_Type(Integer32):
    """Custom type tmnxOamAtmPingCtlSegment based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("endToEnd", 1),
          ("segment", 2))
    )


_TmnxOamAtmPingCtlSegment_Type.__name__ = "Integer32"
_TmnxOamAtmPingCtlSegment_Object = MibTableColumn
tmnxOamAtmPingCtlSegment = _TmnxOamAtmPingCtlSegment_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 11, 1, 5),
    _TmnxOamAtmPingCtlSegment_Type()
)
tmnxOamAtmPingCtlSegment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamAtmPingCtlSegment.setStatus("current")
_TmnxOamMfibPingCtlTable_Object = MibTable
tmnxOamMfibPingCtlTable = _TmnxOamMfibPingCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 12)
)
if mibBuilder.loadTexts:
    tmnxOamMfibPingCtlTable.setStatus("current")
_TmnxOamMfibPingCtlEntry_Object = MibTableRow
tmnxOamMfibPingCtlEntry = _TmnxOamMfibPingCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 12, 1)
)
tmnxOamMfibPingCtlEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamMfibPingCtlEntry.setStatus("current")


class _TmnxOamMfibPingCtlSourceIpAddr_Type(IpAddress):
    """Custom type tmnxOamMfibPingCtlSourceIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_TmnxOamMfibPingCtlSourceIpAddr_Type.__name__ = "IpAddress"
_TmnxOamMfibPingCtlSourceIpAddr_Object = MibTableColumn
tmnxOamMfibPingCtlSourceIpAddr = _TmnxOamMfibPingCtlSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 12, 1, 1),
    _TmnxOamMfibPingCtlSourceIpAddr_Type()
)
tmnxOamMfibPingCtlSourceIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamMfibPingCtlSourceIpAddr.setStatus("obsolete")


class _TmnxOamMfibPingCtlDestIpAddr_Type(IpAddress):
    """Custom type tmnxOamMfibPingCtlDestIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_TmnxOamMfibPingCtlDestIpAddr_Type.__name__ = "IpAddress"
_TmnxOamMfibPingCtlDestIpAddr_Object = MibTableColumn
tmnxOamMfibPingCtlDestIpAddr = _TmnxOamMfibPingCtlDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 12, 1, 2),
    _TmnxOamMfibPingCtlDestIpAddr_Type()
)
tmnxOamMfibPingCtlDestIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamMfibPingCtlDestIpAddr.setStatus("obsolete")


class _TmnxOamMfibPingCtlReplyControl_Type(TruthValue):
    """Custom type tmnxOamMfibPingCtlReplyControl based on TruthValue"""
    defaultValue = 2


_TmnxOamMfibPingCtlReplyControl_Type.__name__ = "TruthValue"
_TmnxOamMfibPingCtlReplyControl_Object = MibTableColumn
tmnxOamMfibPingCtlReplyControl = _TmnxOamMfibPingCtlReplyControl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 12, 1, 3),
    _TmnxOamMfibPingCtlReplyControl_Type()
)
tmnxOamMfibPingCtlReplyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamMfibPingCtlReplyControl.setStatus("current")


class _TmnxOamMfibPingCtlTtl_Type(Unsigned32):
    """Custom type tmnxOamMfibPingCtlTtl based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TmnxOamMfibPingCtlTtl_Type.__name__ = "Unsigned32"
_TmnxOamMfibPingCtlTtl_Object = MibTableColumn
tmnxOamMfibPingCtlTtl = _TmnxOamMfibPingCtlTtl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 12, 1, 4),
    _TmnxOamMfibPingCtlTtl_Type()
)
tmnxOamMfibPingCtlTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamMfibPingCtlTtl.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamMfibPingCtlTtl.setUnits("time-to-live value")


class _TmnxOamMfibPingCtlSrcAddrType_Type(InetAddressType):
    """Custom type tmnxOamMfibPingCtlSrcAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxOamMfibPingCtlSrcAddrType_Type.__name__ = "InetAddressType"
_TmnxOamMfibPingCtlSrcAddrType_Object = MibTableColumn
tmnxOamMfibPingCtlSrcAddrType = _TmnxOamMfibPingCtlSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 12, 1, 5),
    _TmnxOamMfibPingCtlSrcAddrType_Type()
)
tmnxOamMfibPingCtlSrcAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamMfibPingCtlSrcAddrType.setStatus("current")


class _TmnxOamMfibPingCtlSrcAddress_Type(InetAddress):
    """Custom type tmnxOamMfibPingCtlSrcAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamMfibPingCtlSrcAddress_Type.__name__ = "InetAddress"
_TmnxOamMfibPingCtlSrcAddress_Object = MibTableColumn
tmnxOamMfibPingCtlSrcAddress = _TmnxOamMfibPingCtlSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 12, 1, 6),
    _TmnxOamMfibPingCtlSrcAddress_Type()
)
tmnxOamMfibPingCtlSrcAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamMfibPingCtlSrcAddress.setStatus("current")


class _TmnxOamMfibPingCtlDestAddrType_Type(InetAddressType):
    """Custom type tmnxOamMfibPingCtlDestAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxOamMfibPingCtlDestAddrType_Type.__name__ = "InetAddressType"
_TmnxOamMfibPingCtlDestAddrType_Object = MibTableColumn
tmnxOamMfibPingCtlDestAddrType = _TmnxOamMfibPingCtlDestAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 12, 1, 7),
    _TmnxOamMfibPingCtlDestAddrType_Type()
)
tmnxOamMfibPingCtlDestAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamMfibPingCtlDestAddrType.setStatus("current")


class _TmnxOamMfibPingCtlDestAddress_Type(InetAddress):
    """Custom type tmnxOamMfibPingCtlDestAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamMfibPingCtlDestAddress_Type.__name__ = "InetAddress"
_TmnxOamMfibPingCtlDestAddress_Object = MibTableColumn
tmnxOamMfibPingCtlDestAddress = _TmnxOamMfibPingCtlDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 12, 1, 8),
    _TmnxOamMfibPingCtlDestAddress_Type()
)
tmnxOamMfibPingCtlDestAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamMfibPingCtlDestAddress.setStatus("current")


class _TmnxOamMfibPingCtlDestMacAddr_Type(MacAddress):
    """Custom type tmnxOamMfibPingCtlDestMacAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_TmnxOamMfibPingCtlDestMacAddr_Type.__name__ = "MacAddress"
_TmnxOamMfibPingCtlDestMacAddr_Object = MibTableColumn
tmnxOamMfibPingCtlDestMacAddr = _TmnxOamMfibPingCtlDestMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 12, 1, 9),
    _TmnxOamMfibPingCtlDestMacAddr_Type()
)
tmnxOamMfibPingCtlDestMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamMfibPingCtlDestMacAddr.setStatus("current")
_TmnxOamCpePingCtlTable_Object = MibTable
tmnxOamCpePingCtlTable = _TmnxOamCpePingCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 13)
)
if mibBuilder.loadTexts:
    tmnxOamCpePingCtlTable.setStatus("current")
_TmnxOamCpePingCtlEntry_Object = MibTableRow
tmnxOamCpePingCtlEntry = _TmnxOamCpePingCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 13, 1)
)
tmnxOamCpePingCtlEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamCpePingCtlEntry.setStatus("current")


class _TmnxOamCpePingCtlSourceIpAddr_Type(IpAddress):
    """Custom type tmnxOamCpePingCtlSourceIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_TmnxOamCpePingCtlSourceIpAddr_Type.__name__ = "IpAddress"
_TmnxOamCpePingCtlSourceIpAddr_Object = MibTableColumn
tmnxOamCpePingCtlSourceIpAddr = _TmnxOamCpePingCtlSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 13, 1, 1),
    _TmnxOamCpePingCtlSourceIpAddr_Type()
)
tmnxOamCpePingCtlSourceIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamCpePingCtlSourceIpAddr.setStatus("obsolete")


class _TmnxOamCpePingCtlSendControl_Type(TruthValue):
    """Custom type tmnxOamCpePingCtlSendControl based on TruthValue"""
    defaultValue = 2


_TmnxOamCpePingCtlSendControl_Type.__name__ = "TruthValue"
_TmnxOamCpePingCtlSendControl_Object = MibTableColumn
tmnxOamCpePingCtlSendControl = _TmnxOamCpePingCtlSendControl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 13, 1, 2),
    _TmnxOamCpePingCtlSendControl_Type()
)
tmnxOamCpePingCtlSendControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamCpePingCtlSendControl.setStatus("current")


class _TmnxOamCpePingCtlReplyControl_Type(TruthValue):
    """Custom type tmnxOamCpePingCtlReplyControl based on TruthValue"""
    defaultValue = 2


_TmnxOamCpePingCtlReplyControl_Type.__name__ = "TruthValue"
_TmnxOamCpePingCtlReplyControl_Object = MibTableColumn
tmnxOamCpePingCtlReplyControl = _TmnxOamCpePingCtlReplyControl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 13, 1, 3),
    _TmnxOamCpePingCtlReplyControl_Type()
)
tmnxOamCpePingCtlReplyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamCpePingCtlReplyControl.setStatus("current")


class _TmnxOamCpePingCtlTtl_Type(Unsigned32):
    """Custom type tmnxOamCpePingCtlTtl based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TmnxOamCpePingCtlTtl_Type.__name__ = "Unsigned32"
_TmnxOamCpePingCtlTtl_Object = MibTableColumn
tmnxOamCpePingCtlTtl = _TmnxOamCpePingCtlTtl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 13, 1, 4),
    _TmnxOamCpePingCtlTtl_Type()
)
tmnxOamCpePingCtlTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamCpePingCtlTtl.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamCpePingCtlTtl.setUnits("time-to-live value")


class _TmnxOamCpePingCtlSrceMacAddr_Type(MacAddress):
    """Custom type tmnxOamCpePingCtlSrceMacAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_TmnxOamCpePingCtlSrceMacAddr_Type.__name__ = "MacAddress"
_TmnxOamCpePingCtlSrceMacAddr_Object = MibTableColumn
tmnxOamCpePingCtlSrceMacAddr = _TmnxOamCpePingCtlSrceMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 13, 1, 5),
    _TmnxOamCpePingCtlSrceMacAddr_Type()
)
tmnxOamCpePingCtlSrceMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamCpePingCtlSrceMacAddr.setStatus("current")


class _TmnxOamCpePingCtlSrcAddrType_Type(InetAddressType):
    """Custom type tmnxOamCpePingCtlSrcAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxOamCpePingCtlSrcAddrType_Type.__name__ = "InetAddressType"
_TmnxOamCpePingCtlSrcAddrType_Object = MibTableColumn
tmnxOamCpePingCtlSrcAddrType = _TmnxOamCpePingCtlSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 13, 1, 6),
    _TmnxOamCpePingCtlSrcAddrType_Type()
)
tmnxOamCpePingCtlSrcAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamCpePingCtlSrcAddrType.setStatus("current")


class _TmnxOamCpePingCtlSrcAddress_Type(InetAddress):
    """Custom type tmnxOamCpePingCtlSrcAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamCpePingCtlSrcAddress_Type.__name__ = "InetAddress"
_TmnxOamCpePingCtlSrcAddress_Object = MibTableColumn
tmnxOamCpePingCtlSrcAddress = _TmnxOamCpePingCtlSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 13, 1, 7),
    _TmnxOamCpePingCtlSrcAddress_Type()
)
tmnxOamCpePingCtlSrcAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamCpePingCtlSrcAddress.setStatus("current")
_TmnxOamMRInfoRespTable_Object = MibTable
tmnxOamMRInfoRespTable = _TmnxOamMRInfoRespTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 14)
)
if mibBuilder.loadTexts:
    tmnxOamMRInfoRespTable.setStatus("current")
_TmnxOamMRInfoRespEntry_Object = MibTableRow
tmnxOamMRInfoRespEntry = _TmnxOamMRInfoRespEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 14, 1)
)
tmnxOamMRInfoRespEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTestIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsTestRunIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamMRInfoRespEntry.setStatus("current")


class _TmnxOamMRInfoRespCapabilities_Type(Bits):
    """Custom type tmnxOamMRInfoRespCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("leaf", 0),
          ("prune", 1),
          ("genid", 2),
          ("mtrace", 3),
          ("snmp", 4))
    )

_TmnxOamMRInfoRespCapabilities_Type.__name__ = "Bits"
_TmnxOamMRInfoRespCapabilities_Object = MibTableColumn
tmnxOamMRInfoRespCapabilities = _TmnxOamMRInfoRespCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 14, 1, 1),
    _TmnxOamMRInfoRespCapabilities_Type()
)
tmnxOamMRInfoRespCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMRInfoRespCapabilities.setStatus("current")
_TmnxOamMRInfoRespMinorVersion_Type = Unsigned32
_TmnxOamMRInfoRespMinorVersion_Object = MibTableColumn
tmnxOamMRInfoRespMinorVersion = _TmnxOamMRInfoRespMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 14, 1, 2),
    _TmnxOamMRInfoRespMinorVersion_Type()
)
tmnxOamMRInfoRespMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMRInfoRespMinorVersion.setStatus("current")
_TmnxOamMRInfoRespMajorVersion_Type = Unsigned32
_TmnxOamMRInfoRespMajorVersion_Object = MibTableColumn
tmnxOamMRInfoRespMajorVersion = _TmnxOamMRInfoRespMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 14, 1, 3),
    _TmnxOamMRInfoRespMajorVersion_Type()
)
tmnxOamMRInfoRespMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMRInfoRespMajorVersion.setStatus("current")
_TmnxOamMRInfoRespNumInterfaces_Type = Unsigned32
_TmnxOamMRInfoRespNumInterfaces_Object = MibTableColumn
tmnxOamMRInfoRespNumInterfaces = _TmnxOamMRInfoRespNumInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 14, 1, 4),
    _TmnxOamMRInfoRespNumInterfaces_Type()
)
tmnxOamMRInfoRespNumInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMRInfoRespNumInterfaces.setStatus("current")
_TmnxOamMRInfoRespIfTable_Object = MibTable
tmnxOamMRInfoRespIfTable = _TmnxOamMRInfoRespIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 15)
)
if mibBuilder.loadTexts:
    tmnxOamMRInfoRespIfTable.setStatus("current")
_TmnxOamMRInfoRespIfEntry_Object = MibTableRow
tmnxOamMRInfoRespIfEntry = _TmnxOamMRInfoRespIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 15, 1)
)
tmnxOamMRInfoRespIfEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTestIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsTestRunIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamMRInfoRespIfIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamMRInfoRespIfEntry.setStatus("current")
_TmnxOamMRInfoRespIfIndex_Type = Unsigned32
_TmnxOamMRInfoRespIfIndex_Object = MibTableColumn
tmnxOamMRInfoRespIfIndex = _TmnxOamMRInfoRespIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 15, 1, 1),
    _TmnxOamMRInfoRespIfIndex_Type()
)
tmnxOamMRInfoRespIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamMRInfoRespIfIndex.setStatus("current")
_TmnxOamMRInfoRespIfAddress_Type = IpAddress
_TmnxOamMRInfoRespIfAddress_Object = MibTableColumn
tmnxOamMRInfoRespIfAddress = _TmnxOamMRInfoRespIfAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 15, 1, 2),
    _TmnxOamMRInfoRespIfAddress_Type()
)
tmnxOamMRInfoRespIfAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMRInfoRespIfAddress.setStatus("obsolete")
_TmnxOamMRInfoRespIfMetric_Type = Unsigned32
_TmnxOamMRInfoRespIfMetric_Object = MibTableColumn
tmnxOamMRInfoRespIfMetric = _TmnxOamMRInfoRespIfMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 15, 1, 3),
    _TmnxOamMRInfoRespIfMetric_Type()
)
tmnxOamMRInfoRespIfMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMRInfoRespIfMetric.setStatus("current")
_TmnxOamMRInfoRespIfThreshold_Type = Unsigned32
_TmnxOamMRInfoRespIfThreshold_Object = MibTableColumn
tmnxOamMRInfoRespIfThreshold = _TmnxOamMRInfoRespIfThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 15, 1, 4),
    _TmnxOamMRInfoRespIfThreshold_Type()
)
tmnxOamMRInfoRespIfThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMRInfoRespIfThreshold.setStatus("current")


class _TmnxOamMRInfoRespIfFlags_Type(Bits):
    """Custom type tmnxOamMRInfoRespIfFlags based on Bits"""
    namedValues = NamedValues(
        *(("tunnel", 0),
          ("srcrt", 1),
          ("reserved1", 2),
          ("reserved2", 3),
          ("down", 4),
          ("disabled", 5),
          ("querier", 6),
          ("leaf", 7))
    )

_TmnxOamMRInfoRespIfFlags_Type.__name__ = "Bits"
_TmnxOamMRInfoRespIfFlags_Object = MibTableColumn
tmnxOamMRInfoRespIfFlags = _TmnxOamMRInfoRespIfFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 15, 1, 5),
    _TmnxOamMRInfoRespIfFlags_Type()
)
tmnxOamMRInfoRespIfFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMRInfoRespIfFlags.setStatus("current")
_TmnxOamMRInfoRespIfNbrCount_Type = Unsigned32
_TmnxOamMRInfoRespIfNbrCount_Object = MibTableColumn
tmnxOamMRInfoRespIfNbrCount = _TmnxOamMRInfoRespIfNbrCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 15, 1, 6),
    _TmnxOamMRInfoRespIfNbrCount_Type()
)
tmnxOamMRInfoRespIfNbrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMRInfoRespIfNbrCount.setStatus("current")
_TmnxOamMRInfoRespIfAddrType_Type = InetAddressType
_TmnxOamMRInfoRespIfAddrType_Object = MibTableColumn
tmnxOamMRInfoRespIfAddrType = _TmnxOamMRInfoRespIfAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 15, 1, 7),
    _TmnxOamMRInfoRespIfAddrType_Type()
)
tmnxOamMRInfoRespIfAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMRInfoRespIfAddrType.setStatus("current")


class _TmnxOamMRInfoRespIfAddr_Type(InetAddress):
    """Custom type tmnxOamMRInfoRespIfAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamMRInfoRespIfAddr_Type.__name__ = "InetAddress"
_TmnxOamMRInfoRespIfAddr_Object = MibTableColumn
tmnxOamMRInfoRespIfAddr = _TmnxOamMRInfoRespIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 15, 1, 8),
    _TmnxOamMRInfoRespIfAddr_Type()
)
tmnxOamMRInfoRespIfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMRInfoRespIfAddr.setStatus("current")
_TmnxOamMRInfoRespIfNbrTable_Object = MibTable
tmnxOamMRInfoRespIfNbrTable = _TmnxOamMRInfoRespIfNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 16)
)
if mibBuilder.loadTexts:
    tmnxOamMRInfoRespIfNbrTable.setStatus("current")
_TmnxOamMRInfoRespIfNbrEntry_Object = MibTableRow
tmnxOamMRInfoRespIfNbrEntry = _TmnxOamMRInfoRespIfNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 16, 1)
)
tmnxOamMRInfoRespIfNbrEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTestIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsTestRunIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamMRInfoRespIfIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamMRInfoRespIfNbrIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamMRInfoRespIfNbrEntry.setStatus("current")
_TmnxOamMRInfoRespIfNbrIndex_Type = Unsigned32
_TmnxOamMRInfoRespIfNbrIndex_Object = MibTableColumn
tmnxOamMRInfoRespIfNbrIndex = _TmnxOamMRInfoRespIfNbrIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 16, 1, 1),
    _TmnxOamMRInfoRespIfNbrIndex_Type()
)
tmnxOamMRInfoRespIfNbrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamMRInfoRespIfNbrIndex.setStatus("current")
_TmnxOamMRInfoRespIfNbrAddress_Type = IpAddress
_TmnxOamMRInfoRespIfNbrAddress_Object = MibTableColumn
tmnxOamMRInfoRespIfNbrAddress = _TmnxOamMRInfoRespIfNbrAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 16, 1, 2),
    _TmnxOamMRInfoRespIfNbrAddress_Type()
)
tmnxOamMRInfoRespIfNbrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMRInfoRespIfNbrAddress.setStatus("obsolete")
_TmnxOamMRInfoRespIfNbrAddrType_Type = InetAddressType
_TmnxOamMRInfoRespIfNbrAddrType_Object = MibTableColumn
tmnxOamMRInfoRespIfNbrAddrType = _TmnxOamMRInfoRespIfNbrAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 16, 1, 3),
    _TmnxOamMRInfoRespIfNbrAddrType_Type()
)
tmnxOamMRInfoRespIfNbrAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMRInfoRespIfNbrAddrType.setStatus("current")


class _TmnxOamMRInfoRespIfNbrAddr_Type(InetAddress):
    """Custom type tmnxOamMRInfoRespIfNbrAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamMRInfoRespIfNbrAddr_Type.__name__ = "InetAddress"
_TmnxOamMRInfoRespIfNbrAddr_Object = MibTableColumn
tmnxOamMRInfoRespIfNbrAddr = _TmnxOamMRInfoRespIfNbrAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 16, 1, 4),
    _TmnxOamMRInfoRespIfNbrAddr_Type()
)
tmnxOamMRInfoRespIfNbrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMRInfoRespIfNbrAddr.setStatus("current")
_TmnxOamVccvPingCtlTable_Object = MibTable
tmnxOamVccvPingCtlTable = _TmnxOamVccvPingCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 17)
)
if mibBuilder.loadTexts:
    tmnxOamVccvPingCtlTable.setStatus("current")
_TmnxOamVccvPingCtlEntry_Object = MibTableRow
tmnxOamVccvPingCtlEntry = _TmnxOamVccvPingCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 17, 1)
)
tmnxOamVccvPingCtlEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamVccvPingCtlEntry.setStatus("current")


class _TmnxOamVccvPingCtlSdpIdVcId_Type(SdpBindId):
    """Custom type tmnxOamVccvPingCtlSdpIdVcId based on SdpBindId"""
    defaultHexValue = "0000000000000000"


_TmnxOamVccvPingCtlSdpIdVcId_Type.__name__ = "SdpBindId"
_TmnxOamVccvPingCtlSdpIdVcId_Object = MibTableColumn
tmnxOamVccvPingCtlSdpIdVcId = _TmnxOamVccvPingCtlSdpIdVcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 17, 1, 1),
    _TmnxOamVccvPingCtlSdpIdVcId_Type()
)
tmnxOamVccvPingCtlSdpIdVcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamVccvPingCtlSdpIdVcId.setStatus("current")


class _TmnxOamVccvPingCtlReplyMode_Type(Integer32):
    """Custom type tmnxOamVccvPingCtlReplyMode based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ip", 2),
          ("controlChannel", 4))
    )


_TmnxOamVccvPingCtlReplyMode_Type.__name__ = "Integer32"
_TmnxOamVccvPingCtlReplyMode_Object = MibTableColumn
tmnxOamVccvPingCtlReplyMode = _TmnxOamVccvPingCtlReplyMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 17, 1, 2),
    _TmnxOamVccvPingCtlReplyMode_Type()
)
tmnxOamVccvPingCtlReplyMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamVccvPingCtlReplyMode.setStatus("current")


class _TmnxOamVccvPingCtlPwId_Type(TmnxVcIdOrNone):
    """Custom type tmnxOamVccvPingCtlPwId based on TmnxVcIdOrNone"""
    defaultValue = 0


_TmnxOamVccvPingCtlPwId_Type.__name__ = "TmnxVcIdOrNone"
_TmnxOamVccvPingCtlPwId_Object = MibTableColumn
tmnxOamVccvPingCtlPwId = _TmnxOamVccvPingCtlPwId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 17, 1, 3),
    _TmnxOamVccvPingCtlPwId_Type()
)
tmnxOamVccvPingCtlPwId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamVccvPingCtlPwId.setStatus("current")


class _TmnxOamVccvPingCtlTtl_Type(Unsigned32):
    """Custom type tmnxOamVccvPingCtlTtl based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TmnxOamVccvPingCtlTtl_Type.__name__ = "Unsigned32"
_TmnxOamVccvPingCtlTtl_Object = MibTableColumn
tmnxOamVccvPingCtlTtl = _TmnxOamVccvPingCtlTtl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 17, 1, 4),
    _TmnxOamVccvPingCtlTtl_Type()
)
tmnxOamVccvPingCtlTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamVccvPingCtlTtl.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamVccvPingCtlTtl.setUnits("time-to-live value")


class _TmnxOamVccvPingCtlSpokeSdpId_Type(TmnxSpokeSdpIdOrZero):
    """Custom type tmnxOamVccvPingCtlSpokeSdpId based on TmnxSpokeSdpIdOrZero"""
    defaultValue = 0


_TmnxOamVccvPingCtlSpokeSdpId_Type.__name__ = "TmnxSpokeSdpIdOrZero"
_TmnxOamVccvPingCtlSpokeSdpId_Object = MibTableColumn
tmnxOamVccvPingCtlSpokeSdpId = _TmnxOamVccvPingCtlSpokeSdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 17, 1, 5),
    _TmnxOamVccvPingCtlSpokeSdpId_Type()
)
tmnxOamVccvPingCtlSpokeSdpId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamVccvPingCtlSpokeSdpId.setStatus("current")


class _TmnxOamVccvPingCtlSaiiGlobalId_Type(TmnxPwGlobalIdOrZero):
    """Custom type tmnxOamVccvPingCtlSaiiGlobalId based on TmnxPwGlobalIdOrZero"""
    defaultValue = 0


_TmnxOamVccvPingCtlSaiiGlobalId_Type.__name__ = "TmnxPwGlobalIdOrZero"
_TmnxOamVccvPingCtlSaiiGlobalId_Object = MibTableColumn
tmnxOamVccvPingCtlSaiiGlobalId = _TmnxOamVccvPingCtlSaiiGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 17, 1, 6),
    _TmnxOamVccvPingCtlSaiiGlobalId_Type()
)
tmnxOamVccvPingCtlSaiiGlobalId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamVccvPingCtlSaiiGlobalId.setStatus("current")


class _TmnxOamVccvPingCtlSaiiPrefix_Type(Unsigned32):
    """Custom type tmnxOamVccvPingCtlSaiiPrefix based on Unsigned32"""
    defaultValue = 0


_TmnxOamVccvPingCtlSaiiPrefix_Type.__name__ = "Unsigned32"
_TmnxOamVccvPingCtlSaiiPrefix_Object = MibTableColumn
tmnxOamVccvPingCtlSaiiPrefix = _TmnxOamVccvPingCtlSaiiPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 17, 1, 7),
    _TmnxOamVccvPingCtlSaiiPrefix_Type()
)
tmnxOamVccvPingCtlSaiiPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamVccvPingCtlSaiiPrefix.setStatus("current")


class _TmnxOamVccvPingCtlSaiiAcId_Type(Unsigned32):
    """Custom type tmnxOamVccvPingCtlSaiiAcId based on Unsigned32"""
    defaultValue = 0


_TmnxOamVccvPingCtlSaiiAcId_Type.__name__ = "Unsigned32"
_TmnxOamVccvPingCtlSaiiAcId_Object = MibTableColumn
tmnxOamVccvPingCtlSaiiAcId = _TmnxOamVccvPingCtlSaiiAcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 17, 1, 8),
    _TmnxOamVccvPingCtlSaiiAcId_Type()
)
tmnxOamVccvPingCtlSaiiAcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamVccvPingCtlSaiiAcId.setStatus("current")


class _TmnxOamVccvPingCtlTaiiGlobalId_Type(TmnxPwGlobalIdOrZero):
    """Custom type tmnxOamVccvPingCtlTaiiGlobalId based on TmnxPwGlobalIdOrZero"""
    defaultValue = 0


_TmnxOamVccvPingCtlTaiiGlobalId_Type.__name__ = "TmnxPwGlobalIdOrZero"
_TmnxOamVccvPingCtlTaiiGlobalId_Object = MibTableColumn
tmnxOamVccvPingCtlTaiiGlobalId = _TmnxOamVccvPingCtlTaiiGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 17, 1, 9),
    _TmnxOamVccvPingCtlTaiiGlobalId_Type()
)
tmnxOamVccvPingCtlTaiiGlobalId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamVccvPingCtlTaiiGlobalId.setStatus("current")


class _TmnxOamVccvPingCtlTaiiPrefix_Type(Unsigned32):
    """Custom type tmnxOamVccvPingCtlTaiiPrefix based on Unsigned32"""
    defaultValue = 0


_TmnxOamVccvPingCtlTaiiPrefix_Type.__name__ = "Unsigned32"
_TmnxOamVccvPingCtlTaiiPrefix_Object = MibTableColumn
tmnxOamVccvPingCtlTaiiPrefix = _TmnxOamVccvPingCtlTaiiPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 17, 1, 10),
    _TmnxOamVccvPingCtlTaiiPrefix_Type()
)
tmnxOamVccvPingCtlTaiiPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamVccvPingCtlTaiiPrefix.setStatus("current")


class _TmnxOamVccvPingCtlTaiiAcId_Type(Unsigned32):
    """Custom type tmnxOamVccvPingCtlTaiiAcId based on Unsigned32"""
    defaultValue = 0


_TmnxOamVccvPingCtlTaiiAcId_Type.__name__ = "Unsigned32"
_TmnxOamVccvPingCtlTaiiAcId_Object = MibTableColumn
tmnxOamVccvPingCtlTaiiAcId = _TmnxOamVccvPingCtlTaiiAcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 17, 1, 11),
    _TmnxOamVccvPingCtlTaiiAcId_Type()
)
tmnxOamVccvPingCtlTaiiAcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamVccvPingCtlTaiiAcId.setStatus("current")


class _TmnxOamVccvPingCtlMplsTpGlobalId_Type(TmnxMplsTpGlobalID):
    """Custom type tmnxOamVccvPingCtlMplsTpGlobalId based on TmnxMplsTpGlobalID"""
    defaultValue = 0


_TmnxOamVccvPingCtlMplsTpGlobalId_Type.__name__ = "TmnxMplsTpGlobalID"
_TmnxOamVccvPingCtlMplsTpGlobalId_Object = MibTableColumn
tmnxOamVccvPingCtlMplsTpGlobalId = _TmnxOamVccvPingCtlMplsTpGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 17, 1, 12),
    _TmnxOamVccvPingCtlMplsTpGlobalId_Type()
)
tmnxOamVccvPingCtlMplsTpGlobalId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamVccvPingCtlMplsTpGlobalId.setStatus("current")


class _TmnxOamVccvPingCtlMplsTpNodeId_Type(TmnxMplsTpNodeID):
    """Custom type tmnxOamVccvPingCtlMplsTpNodeId based on TmnxMplsTpNodeID"""
    defaultValue = 0


_TmnxOamVccvPingCtlMplsTpNodeId_Type.__name__ = "TmnxMplsTpNodeID"
_TmnxOamVccvPingCtlMplsTpNodeId_Object = MibTableColumn
tmnxOamVccvPingCtlMplsTpNodeId = _TmnxOamVccvPingCtlMplsTpNodeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 17, 1, 13),
    _TmnxOamVccvPingCtlMplsTpNodeId_Type()
)
tmnxOamVccvPingCtlMplsTpNodeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamVccvPingCtlMplsTpNodeId.setStatus("current")


class _TmnxOamVccvPingCtlTestSubMode_Type(TmnxOamVccvTestSubMode):
    """Custom type tmnxOamVccvPingCtlTestSubMode based on TmnxOamVccvTestSubMode"""
    defaultValue = 1


_TmnxOamVccvPingCtlTestSubMode_Type.__name__ = "TmnxOamVccvTestSubMode"
_TmnxOamVccvPingCtlTestSubMode_Object = MibTableColumn
tmnxOamVccvPingCtlTestSubMode = _TmnxOamVccvPingCtlTestSubMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 17, 1, 14),
    _TmnxOamVccvPingCtlTestSubMode_Type()
)
tmnxOamVccvPingCtlTestSubMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamVccvPingCtlTestSubMode.setStatus("current")


class _TmnxOamVccvPingCtlAssocChannel_Type(TmnxOamVccvAssocChannel):
    """Custom type tmnxOamVccvPingCtlAssocChannel based on TmnxOamVccvAssocChannel"""
    defaultValue = 1


_TmnxOamVccvPingCtlAssocChannel_Type.__name__ = "TmnxOamVccvAssocChannel"
_TmnxOamVccvPingCtlAssocChannel_Object = MibTableColumn
tmnxOamVccvPingCtlAssocChannel = _TmnxOamVccvPingCtlAssocChannel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 17, 1, 15),
    _TmnxOamVccvPingCtlAssocChannel_Type()
)
tmnxOamVccvPingCtlAssocChannel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamVccvPingCtlAssocChannel.setStatus("current")


class _TmnxOamVccvPingCtlSwitTgtFecType_Type(TmnxOamVccvSwitTgtFecType):
    """Custom type tmnxOamVccvPingCtlSwitTgtFecType based on TmnxOamVccvSwitTgtFecType"""
    defaultValue = 1


_TmnxOamVccvPingCtlSwitTgtFecType_Type.__name__ = "TmnxOamVccvSwitTgtFecType"
_TmnxOamVccvPingCtlSwitTgtFecType_Object = MibTableColumn
tmnxOamVccvPingCtlSwitTgtFecType = _TmnxOamVccvPingCtlSwitTgtFecType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 17, 1, 16),
    _TmnxOamVccvPingCtlSwitTgtFecType_Type()
)
tmnxOamVccvPingCtlSwitTgtFecType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamVccvPingCtlSwitTgtFecType.setStatus("current")
_TmnxOamIcmpPingCtlTable_Object = MibTable
tmnxOamIcmpPingCtlTable = _TmnxOamIcmpPingCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 18)
)
if mibBuilder.loadTexts:
    tmnxOamIcmpPingCtlTable.setStatus("current")
_TmnxOamIcmpPingCtlEntry_Object = MibTableRow
tmnxOamIcmpPingCtlEntry = _TmnxOamIcmpPingCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 18, 1)
)
tmnxOamIcmpPingCtlEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamIcmpPingCtlEntry.setStatus("current")


class _TmnxOamIcmpPingCtlRapid_Type(TruthValue):
    """Custom type tmnxOamIcmpPingCtlRapid based on TruthValue"""
    defaultValue = 2


_TmnxOamIcmpPingCtlRapid_Type.__name__ = "TruthValue"
_TmnxOamIcmpPingCtlRapid_Object = MibTableColumn
tmnxOamIcmpPingCtlRapid = _TmnxOamIcmpPingCtlRapid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 18, 1, 1),
    _TmnxOamIcmpPingCtlRapid_Type()
)
tmnxOamIcmpPingCtlRapid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamIcmpPingCtlRapid.setStatus("current")


class _TmnxOamIcmpPingCtlTtl_Type(Unsigned32):
    """Custom type tmnxOamIcmpPingCtlTtl based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_TmnxOamIcmpPingCtlTtl_Type.__name__ = "Unsigned32"
_TmnxOamIcmpPingCtlTtl_Object = MibTableColumn
tmnxOamIcmpPingCtlTtl = _TmnxOamIcmpPingCtlTtl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 18, 1, 2),
    _TmnxOamIcmpPingCtlTtl_Type()
)
tmnxOamIcmpPingCtlTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamIcmpPingCtlTtl.setStatus("current")


class _TmnxOamIcmpPingCtlDSField_Type(Unsigned32):
    """Custom type tmnxOamIcmpPingCtlDSField based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxOamIcmpPingCtlDSField_Type.__name__ = "Unsigned32"
_TmnxOamIcmpPingCtlDSField_Object = MibTableColumn
tmnxOamIcmpPingCtlDSField = _TmnxOamIcmpPingCtlDSField_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 18, 1, 3),
    _TmnxOamIcmpPingCtlDSField_Type()
)
tmnxOamIcmpPingCtlDSField.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamIcmpPingCtlDSField.setStatus("current")


class _TmnxOamIcmpPingCtlPattern_Type(Integer32):
    """Custom type tmnxOamIcmpPingCtlPattern based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )


_TmnxOamIcmpPingCtlPattern_Type.__name__ = "Integer32"
_TmnxOamIcmpPingCtlPattern_Object = MibTableColumn
tmnxOamIcmpPingCtlPattern = _TmnxOamIcmpPingCtlPattern_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 18, 1, 4),
    _TmnxOamIcmpPingCtlPattern_Type()
)
tmnxOamIcmpPingCtlPattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamIcmpPingCtlPattern.setStatus("current")


class _TmnxOamIcmpPingCtlNhAddrType_Type(InetAddressType):
    """Custom type tmnxOamIcmpPingCtlNhAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxOamIcmpPingCtlNhAddrType_Type.__name__ = "InetAddressType"
_TmnxOamIcmpPingCtlNhAddrType_Object = MibTableColumn
tmnxOamIcmpPingCtlNhAddrType = _TmnxOamIcmpPingCtlNhAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 18, 1, 5),
    _TmnxOamIcmpPingCtlNhAddrType_Type()
)
tmnxOamIcmpPingCtlNhAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamIcmpPingCtlNhAddrType.setStatus("current")


class _TmnxOamIcmpPingCtlNhAddress_Type(InetAddress):
    """Custom type tmnxOamIcmpPingCtlNhAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamIcmpPingCtlNhAddress_Type.__name__ = "InetAddress"
_TmnxOamIcmpPingCtlNhAddress_Object = MibTableColumn
tmnxOamIcmpPingCtlNhAddress = _TmnxOamIcmpPingCtlNhAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 18, 1, 6),
    _TmnxOamIcmpPingCtlNhAddress_Type()
)
tmnxOamIcmpPingCtlNhAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamIcmpPingCtlNhAddress.setStatus("current")


class _TmnxOamIcmpPingCtlEgrIfIndex_Type(InterfaceIndexOrZero):
    """Custom type tmnxOamIcmpPingCtlEgrIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_TmnxOamIcmpPingCtlEgrIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_TmnxOamIcmpPingCtlEgrIfIndex_Object = MibTableColumn
tmnxOamIcmpPingCtlEgrIfIndex = _TmnxOamIcmpPingCtlEgrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 18, 1, 7),
    _TmnxOamIcmpPingCtlEgrIfIndex_Type()
)
tmnxOamIcmpPingCtlEgrIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamIcmpPingCtlEgrIfIndex.setStatus("obsolete")


class _TmnxOamIcmpPingCtlBypassRouting_Type(TruthValue):
    """Custom type tmnxOamIcmpPingCtlBypassRouting based on TruthValue"""
    defaultValue = 2


_TmnxOamIcmpPingCtlBypassRouting_Type.__name__ = "TruthValue"
_TmnxOamIcmpPingCtlBypassRouting_Object = MibTableColumn
tmnxOamIcmpPingCtlBypassRouting = _TmnxOamIcmpPingCtlBypassRouting_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 18, 1, 8),
    _TmnxOamIcmpPingCtlBypassRouting_Type()
)
tmnxOamIcmpPingCtlBypassRouting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamIcmpPingCtlBypassRouting.setStatus("current")


class _TmnxOamIcmpPingCtlDoNotFragment_Type(TruthValue):
    """Custom type tmnxOamIcmpPingCtlDoNotFragment based on TruthValue"""
    defaultValue = 2


_TmnxOamIcmpPingCtlDoNotFragment_Type.__name__ = "TruthValue"
_TmnxOamIcmpPingCtlDoNotFragment_Object = MibTableColumn
tmnxOamIcmpPingCtlDoNotFragment = _TmnxOamIcmpPingCtlDoNotFragment_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 18, 1, 9),
    _TmnxOamIcmpPingCtlDoNotFragment_Type()
)
tmnxOamIcmpPingCtlDoNotFragment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamIcmpPingCtlDoNotFragment.setStatus("current")


class _TmnxOamIcmpPingCtlEgrIfName_Type(TNamedItemOrEmpty):
    """Custom type tmnxOamIcmpPingCtlEgrIfName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOamIcmpPingCtlEgrIfName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOamIcmpPingCtlEgrIfName_Object = MibTableColumn
tmnxOamIcmpPingCtlEgrIfName = _TmnxOamIcmpPingCtlEgrIfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 18, 1, 10),
    _TmnxOamIcmpPingCtlEgrIfName_Type()
)
tmnxOamIcmpPingCtlEgrIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamIcmpPingCtlEgrIfName.setStatus("current")
_TmnxOamAncpTestCtlTable_Object = MibTable
tmnxOamAncpTestCtlTable = _TmnxOamAncpTestCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 19)
)
if mibBuilder.loadTexts:
    tmnxOamAncpTestCtlTable.setStatus("current")
_TmnxOamAncpTestCtlEntry_Object = MibTableRow
tmnxOamAncpTestCtlEntry = _TmnxOamAncpTestCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 19, 1)
)
tmnxOamAncpTestCtlEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamAncpTestCtlEntry.setStatus("current")


class _TmnxOamAncpTestTarget_Type(Integer32):
    """Custom type tmnxOamAncpTestTarget based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("subscriberId", 1),
          ("ancpString", 2))
    )


_TmnxOamAncpTestTarget_Type.__name__ = "Integer32"
_TmnxOamAncpTestTarget_Object = MibTableColumn
tmnxOamAncpTestTarget = _TmnxOamAncpTestTarget_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 19, 1, 1),
    _TmnxOamAncpTestTarget_Type()
)
tmnxOamAncpTestTarget.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamAncpTestTarget.setStatus("current")


class _TmnxOamAncpTestTargetId_Type(DisplayString):
    """Custom type tmnxOamAncpTestTargetId based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_TmnxOamAncpTestTargetId_Type.__name__ = "DisplayString"
_TmnxOamAncpTestTargetId_Object = MibTableColumn
tmnxOamAncpTestTargetId = _TmnxOamAncpTestTargetId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 19, 1, 2),
    _TmnxOamAncpTestTargetId_Type()
)
tmnxOamAncpTestTargetId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamAncpTestTargetId.setStatus("current")


class _TmnxOamAncpTestcount_Type(Integer32):
    """Custom type tmnxOamAncpTestcount based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_TmnxOamAncpTestcount_Type.__name__ = "Integer32"
_TmnxOamAncpTestcount_Object = MibTableColumn
tmnxOamAncpTestcount = _TmnxOamAncpTestcount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 19, 1, 3),
    _TmnxOamAncpTestcount_Type()
)
tmnxOamAncpTestcount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamAncpTestcount.setStatus("current")


class _TmnxOamAncpTestTimeout_Type(Integer32):
    """Custom type tmnxOamAncpTestTimeout based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxOamAncpTestTimeout_Type.__name__ = "Integer32"
_TmnxOamAncpTestTimeout_Object = MibTableColumn
tmnxOamAncpTestTimeout = _TmnxOamAncpTestTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 19, 1, 4),
    _TmnxOamAncpTestTimeout_Type()
)
tmnxOamAncpTestTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamAncpTestTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamAncpTestTimeout.setUnits("seconds")
_TmnxOamAncpTestHistoryTable_Object = MibTable
tmnxOamAncpTestHistoryTable = _TmnxOamAncpTestHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 20)
)
if mibBuilder.loadTexts:
    tmnxOamAncpTestHistoryTable.setStatus("current")
_TmnxOamAncpTestHistoryEntry_Object = MibTableRow
tmnxOamAncpTestHistoryEntry = _TmnxOamAncpTestHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 20, 1)
)
tmnxOamAncpTestHistoryEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTestIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsTestRunIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamAncpHistoryIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamAncpTestHistoryEntry.setStatus("current")


class _TmnxOamAncpHistoryIndex_Type(Unsigned32):
    """Custom type tmnxOamAncpHistoryIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxOamAncpHistoryIndex_Type.__name__ = "Unsigned32"
_TmnxOamAncpHistoryIndex_Object = MibTableColumn
tmnxOamAncpHistoryIndex = _TmnxOamAncpHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 20, 1, 1),
    _TmnxOamAncpHistoryIndex_Type()
)
tmnxOamAncpHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamAncpHistoryIndex.setStatus("current")


class _TmnxOamAncpHistoryAncpString_Type(DisplayString):
    """Custom type tmnxOamAncpHistoryAncpString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_TmnxOamAncpHistoryAncpString_Type.__name__ = "DisplayString"
_TmnxOamAncpHistoryAncpString_Object = MibTableColumn
tmnxOamAncpHistoryAncpString = _TmnxOamAncpHistoryAncpString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 20, 1, 2),
    _TmnxOamAncpHistoryAncpString_Type()
)
tmnxOamAncpHistoryAncpString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamAncpHistoryAncpString.setStatus("current")
_TmnxOamAncpHistoryAccNodeCode_Type = Unsigned32
_TmnxOamAncpHistoryAccNodeCode_Object = MibTableColumn
tmnxOamAncpHistoryAccNodeCode = _TmnxOamAncpHistoryAccNodeCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 20, 1, 3),
    _TmnxOamAncpHistoryAccNodeCode_Type()
)
tmnxOamAncpHistoryAccNodeCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamAncpHistoryAccNodeCode.setStatus("current")
_TmnxOamAncpHistoryAccNodeResult_Type = Unsigned32
_TmnxOamAncpHistoryAccNodeResult_Object = MibTableColumn
tmnxOamAncpHistoryAccNodeResult = _TmnxOamAncpHistoryAccNodeResult_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 20, 1, 4),
    _TmnxOamAncpHistoryAccNodeResult_Type()
)
tmnxOamAncpHistoryAccNodeResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamAncpHistoryAccNodeResult.setStatus("current")
_TmnxOamAncpHistoryAccNodeRspStr_Type = DisplayString
_TmnxOamAncpHistoryAccNodeRspStr_Object = MibTableColumn
tmnxOamAncpHistoryAccNodeRspStr = _TmnxOamAncpHistoryAccNodeRspStr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 20, 1, 5),
    _TmnxOamAncpHistoryAccNodeRspStr_Type()
)
tmnxOamAncpHistoryAccNodeRspStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamAncpHistoryAccNodeRspStr.setStatus("current")
_TmnxOamP2mpLspPingCtlTable_Object = MibTable
tmnxOamP2mpLspPingCtlTable = _TmnxOamP2mpLspPingCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 21)
)
if mibBuilder.loadTexts:
    tmnxOamP2mpLspPingCtlTable.setStatus("current")
_TmnxOamP2mpLspPingCtlEntry_Object = MibTableRow
tmnxOamP2mpLspPingCtlEntry = _TmnxOamP2mpLspPingCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 21, 1)
)
tmnxOamP2mpLspPingCtlEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamP2mpLspPingCtlEntry.setStatus("current")


class _TmnxOamP2mpLspPingCtlLspName_Type(TLNamedItemOrEmpty):
    """Custom type tmnxOamP2mpLspPingCtlLspName based on TLNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOamP2mpLspPingCtlLspName_Type.__name__ = "TLNamedItemOrEmpty"
_TmnxOamP2mpLspPingCtlLspName_Object = MibTableColumn
tmnxOamP2mpLspPingCtlLspName = _TmnxOamP2mpLspPingCtlLspName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 21, 1, 1),
    _TmnxOamP2mpLspPingCtlLspName_Type()
)
tmnxOamP2mpLspPingCtlLspName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamP2mpLspPingCtlLspName.setStatus("current")


class _TmnxOamP2mpLspPingCtlInstName_Type(TNamedItemOrEmpty):
    """Custom type tmnxOamP2mpLspPingCtlInstName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOamP2mpLspPingCtlInstName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOamP2mpLspPingCtlInstName_Object = MibTableColumn
tmnxOamP2mpLspPingCtlInstName = _TmnxOamP2mpLspPingCtlInstName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 21, 1, 2),
    _TmnxOamP2mpLspPingCtlInstName_Type()
)
tmnxOamP2mpLspPingCtlInstName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamP2mpLspPingCtlInstName.setStatus("current")


class _TmnxOamP2mpLspPingCtlTtl_Type(Unsigned32):
    """Custom type tmnxOamP2mpLspPingCtlTtl based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TmnxOamP2mpLspPingCtlTtl_Type.__name__ = "Unsigned32"
_TmnxOamP2mpLspPingCtlTtl_Object = MibTableColumn
tmnxOamP2mpLspPingCtlTtl = _TmnxOamP2mpLspPingCtlTtl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 21, 1, 3),
    _TmnxOamP2mpLspPingCtlTtl_Type()
)
tmnxOamP2mpLspPingCtlTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamP2mpLspPingCtlTtl.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamP2mpLspPingCtlTtl.setUnits("time-to-live value")


class _TmnxOamP2mpLspPingCtlP2MPId_Type(Unsigned32):
    """Custom type tmnxOamP2mpLspPingCtlP2MPId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxOamP2mpLspPingCtlP2MPId_Type.__name__ = "Unsigned32"
_TmnxOamP2mpLspPingCtlP2MPId_Object = MibTableColumn
tmnxOamP2mpLspPingCtlP2MPId = _TmnxOamP2mpLspPingCtlP2MPId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 21, 1, 4),
    _TmnxOamP2mpLspPingCtlP2MPId_Type()
)
tmnxOamP2mpLspPingCtlP2MPId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamP2mpLspPingCtlP2MPId.setStatus("current")


class _TmnxOamP2mpLspPingCtlSrcAddrType_Type(InetAddressType):
    """Custom type tmnxOamP2mpLspPingCtlSrcAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxOamP2mpLspPingCtlSrcAddrType_Type.__name__ = "InetAddressType"
_TmnxOamP2mpLspPingCtlSrcAddrType_Object = MibTableColumn
tmnxOamP2mpLspPingCtlSrcAddrType = _TmnxOamP2mpLspPingCtlSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 21, 1, 5),
    _TmnxOamP2mpLspPingCtlSrcAddrType_Type()
)
tmnxOamP2mpLspPingCtlSrcAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamP2mpLspPingCtlSrcAddrType.setStatus("current")


class _TmnxOamP2mpLspPingCtlSrcAddr_Type(InetAddress):
    """Custom type tmnxOamP2mpLspPingCtlSrcAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamP2mpLspPingCtlSrcAddr_Type.__name__ = "InetAddress"
_TmnxOamP2mpLspPingCtlSrcAddr_Object = MibTableColumn
tmnxOamP2mpLspPingCtlSrcAddr = _TmnxOamP2mpLspPingCtlSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 21, 1, 6),
    _TmnxOamP2mpLspPingCtlSrcAddr_Type()
)
tmnxOamP2mpLspPingCtlSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamP2mpLspPingCtlSrcAddr.setStatus("current")


class _TmnxOamP2mpLspPingCtlGrpAddrType_Type(InetAddressType):
    """Custom type tmnxOamP2mpLspPingCtlGrpAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxOamP2mpLspPingCtlGrpAddrType_Type.__name__ = "InetAddressType"
_TmnxOamP2mpLspPingCtlGrpAddrType_Object = MibTableColumn
tmnxOamP2mpLspPingCtlGrpAddrType = _TmnxOamP2mpLspPingCtlGrpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 21, 1, 7),
    _TmnxOamP2mpLspPingCtlGrpAddrType_Type()
)
tmnxOamP2mpLspPingCtlGrpAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamP2mpLspPingCtlGrpAddrType.setStatus("current")


class _TmnxOamP2mpLspPingCtlGrpAddr_Type(InetAddress):
    """Custom type tmnxOamP2mpLspPingCtlGrpAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamP2mpLspPingCtlGrpAddr_Type.__name__ = "InetAddress"
_TmnxOamP2mpLspPingCtlGrpAddr_Object = MibTableColumn
tmnxOamP2mpLspPingCtlGrpAddr = _TmnxOamP2mpLspPingCtlGrpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 21, 1, 8),
    _TmnxOamP2mpLspPingCtlGrpAddr_Type()
)
tmnxOamP2mpLspPingCtlGrpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamP2mpLspPingCtlGrpAddr.setStatus("current")


class _TmnxOamP2mpLspPingCtlOptionalTLV_Type(Integer32):
    """Custom type tmnxOamP2mpLspPingCtlOptionalTLV based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("vpnRecursiveFec", 2))
    )


_TmnxOamP2mpLspPingCtlOptionalTLV_Type.__name__ = "Integer32"
_TmnxOamP2mpLspPingCtlOptionalTLV_Object = MibTableColumn
tmnxOamP2mpLspPingCtlOptionalTLV = _TmnxOamP2mpLspPingCtlOptionalTLV_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 21, 1, 9),
    _TmnxOamP2mpLspPingCtlOptionalTLV_Type()
)
tmnxOamP2mpLspPingCtlOptionalTLV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamP2mpLspPingCtlOptionalTLV.setStatus("current")
_TmnxOamP2mpLspPingIPAddressTable_Object = MibTable
tmnxOamP2mpLspPingIPAddressTable = _TmnxOamP2mpLspPingIPAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 22)
)
if mibBuilder.loadTexts:
    tmnxOamP2mpLspPingIPAddressTable.setStatus("current")
_TmnxOamP2mpLspPingIPAddressEntry_Object = MibTableRow
tmnxOamP2mpLspPingIPAddressEntry = _TmnxOamP2mpLspPingIPAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 22, 1)
)
tmnxOamP2mpLspPingIPAddressEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTestIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamP2mpLspPingCtlIpAddrIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamP2mpLspPingIPAddressEntry.setStatus("current")


class _TmnxOamP2mpLspPingCtlIpAddrIndex_Type(Unsigned32):
    """Custom type tmnxOamP2mpLspPingCtlIpAddrIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_TmnxOamP2mpLspPingCtlIpAddrIndex_Type.__name__ = "Unsigned32"
_TmnxOamP2mpLspPingCtlIpAddrIndex_Object = MibTableColumn
tmnxOamP2mpLspPingCtlIpAddrIndex = _TmnxOamP2mpLspPingCtlIpAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 22, 1, 1),
    _TmnxOamP2mpLspPingCtlIpAddrIndex_Type()
)
tmnxOamP2mpLspPingCtlIpAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamP2mpLspPingCtlIpAddrIndex.setStatus("current")
_TmnxOamP2mpLspPingCtlIpRowStatus_Type = RowStatus
_TmnxOamP2mpLspPingCtlIpRowStatus_Object = MibTableColumn
tmnxOamP2mpLspPingCtlIpRowStatus = _TmnxOamP2mpLspPingCtlIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 22, 1, 2),
    _TmnxOamP2mpLspPingCtlIpRowStatus_Type()
)
tmnxOamP2mpLspPingCtlIpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamP2mpLspPingCtlIpRowStatus.setStatus("current")
_TmnxOamP2mpLspPingCtlIpAddrType_Type = InetAddressType
_TmnxOamP2mpLspPingCtlIpAddrType_Object = MibTableColumn
tmnxOamP2mpLspPingCtlIpAddrType = _TmnxOamP2mpLspPingCtlIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 22, 1, 3),
    _TmnxOamP2mpLspPingCtlIpAddrType_Type()
)
tmnxOamP2mpLspPingCtlIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamP2mpLspPingCtlIpAddrType.setStatus("current")


class _TmnxOamP2mpLspPingCtlIpAddr_Type(InetAddress):
    """Custom type tmnxOamP2mpLspPingCtlIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamP2mpLspPingCtlIpAddr_Type.__name__ = "InetAddress"
_TmnxOamP2mpLspPingCtlIpAddr_Object = MibTableColumn
tmnxOamP2mpLspPingCtlIpAddr = _TmnxOamP2mpLspPingCtlIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 22, 1, 4),
    _TmnxOamP2mpLspPingCtlIpAddr_Type()
)
tmnxOamP2mpLspPingCtlIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamP2mpLspPingCtlIpAddr.setStatus("current")
_TmnxOamEthCfmPingCtlTable_Object = MibTable
tmnxOamEthCfmPingCtlTable = _TmnxOamEthCfmPingCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 23)
)
if mibBuilder.loadTexts:
    tmnxOamEthCfmPingCtlTable.setStatus("current")
_TmnxOamEthCfmPingCtlEntry_Object = MibTableRow
tmnxOamEthCfmPingCtlEntry = _TmnxOamEthCfmPingCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 23, 1)
)
tmnxOamEthCfmPingCtlEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamEthCfmPingCtlEntry.setStatus("current")


class _TmnxOamEthCfmPingCtlTgtMacAddr_Type(MacAddress):
    """Custom type tmnxOamEthCfmPingCtlTgtMacAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_TmnxOamEthCfmPingCtlTgtMacAddr_Type.__name__ = "MacAddress"
_TmnxOamEthCfmPingCtlTgtMacAddr_Object = MibTableColumn
tmnxOamEthCfmPingCtlTgtMacAddr = _TmnxOamEthCfmPingCtlTgtMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 23, 1, 1),
    _TmnxOamEthCfmPingCtlTgtMacAddr_Type()
)
tmnxOamEthCfmPingCtlTgtMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamEthCfmPingCtlTgtMacAddr.setStatus("current")


class _TmnxOamEthCfmPingCtlSrcMdIndex_Type(Unsigned32):
    """Custom type tmnxOamEthCfmPingCtlSrcMdIndex based on Unsigned32"""
    defaultValue = 0


_TmnxOamEthCfmPingCtlSrcMdIndex_Type.__name__ = "Unsigned32"
_TmnxOamEthCfmPingCtlSrcMdIndex_Object = MibTableColumn
tmnxOamEthCfmPingCtlSrcMdIndex = _TmnxOamEthCfmPingCtlSrcMdIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 23, 1, 2),
    _TmnxOamEthCfmPingCtlSrcMdIndex_Type()
)
tmnxOamEthCfmPingCtlSrcMdIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamEthCfmPingCtlSrcMdIndex.setStatus("current")


class _TmnxOamEthCfmPingCtlSrcMaIndex_Type(Unsigned32):
    """Custom type tmnxOamEthCfmPingCtlSrcMaIndex based on Unsigned32"""
    defaultValue = 0


_TmnxOamEthCfmPingCtlSrcMaIndex_Type.__name__ = "Unsigned32"
_TmnxOamEthCfmPingCtlSrcMaIndex_Object = MibTableColumn
tmnxOamEthCfmPingCtlSrcMaIndex = _TmnxOamEthCfmPingCtlSrcMaIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 23, 1, 3),
    _TmnxOamEthCfmPingCtlSrcMaIndex_Type()
)
tmnxOamEthCfmPingCtlSrcMaIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamEthCfmPingCtlSrcMaIndex.setStatus("current")


class _TmnxOamEthCfmPingCtlSrcMepId_Type(Dot1agCfmMepIdOrZero):
    """Custom type tmnxOamEthCfmPingCtlSrcMepId based on Dot1agCfmMepIdOrZero"""
    defaultValue = 0


_TmnxOamEthCfmPingCtlSrcMepId_Type.__name__ = "Dot1agCfmMepIdOrZero"
_TmnxOamEthCfmPingCtlSrcMepId_Object = MibTableColumn
tmnxOamEthCfmPingCtlSrcMepId = _TmnxOamEthCfmPingCtlSrcMepId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 23, 1, 4),
    _TmnxOamEthCfmPingCtlSrcMepId_Type()
)
tmnxOamEthCfmPingCtlSrcMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamEthCfmPingCtlSrcMepId.setStatus("current")


class _TmnxOamEthCfmPingCtlRemoteMepId_Type(Dot1agCfmMepIdOrZero):
    """Custom type tmnxOamEthCfmPingCtlRemoteMepId based on Dot1agCfmMepIdOrZero"""
    defaultValue = 0


_TmnxOamEthCfmPingCtlRemoteMepId_Type.__name__ = "Dot1agCfmMepIdOrZero"
_TmnxOamEthCfmPingCtlRemoteMepId_Object = MibTableColumn
tmnxOamEthCfmPingCtlRemoteMepId = _TmnxOamEthCfmPingCtlRemoteMepId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 23, 1, 5),
    _TmnxOamEthCfmPingCtlRemoteMepId_Type()
)
tmnxOamEthCfmPingCtlRemoteMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamEthCfmPingCtlRemoteMepId.setStatus("current")
_TmnxOamVccvPgTgFec128CtlTable_Object = MibTable
tmnxOamVccvPgTgFec128CtlTable = _TmnxOamVccvPgTgFec128CtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 24)
)
if mibBuilder.loadTexts:
    tmnxOamVccvPgTgFec128CtlTable.setStatus("current")
_TmnxOamVccvPgTgFec128CtlEntry_Object = MibTableRow
tmnxOamVccvPgTgFec128CtlEntry = _TmnxOamVccvPgTgFec128CtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 24, 1)
)
tmnxOamVccvPgTgFec128CtlEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamVccvPgTgFec128CtlEntry.setStatus("current")


class _TmnxOamVccvPgTgFec128CtlSrcAddrT_Type(InetAddressType):
    """Custom type tmnxOamVccvPgTgFec128CtlSrcAddrT based on InetAddressType"""
    defaultValue = 0


_TmnxOamVccvPgTgFec128CtlSrcAddrT_Type.__name__ = "InetAddressType"
_TmnxOamVccvPgTgFec128CtlSrcAddrT_Object = MibTableColumn
tmnxOamVccvPgTgFec128CtlSrcAddrT = _TmnxOamVccvPgTgFec128CtlSrcAddrT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 24, 1, 1),
    _TmnxOamVccvPgTgFec128CtlSrcAddrT_Type()
)
tmnxOamVccvPgTgFec128CtlSrcAddrT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamVccvPgTgFec128CtlSrcAddrT.setStatus("current")


class _TmnxOamVccvPgTgFec128CtlSrcAddr_Type(InetAddress):
    """Custom type tmnxOamVccvPgTgFec128CtlSrcAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamVccvPgTgFec128CtlSrcAddr_Type.__name__ = "InetAddress"
_TmnxOamVccvPgTgFec128CtlSrcAddr_Object = MibTableColumn
tmnxOamVccvPgTgFec128CtlSrcAddr = _TmnxOamVccvPgTgFec128CtlSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 24, 1, 2),
    _TmnxOamVccvPgTgFec128CtlSrcAddr_Type()
)
tmnxOamVccvPgTgFec128CtlSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamVccvPgTgFec128CtlSrcAddr.setStatus("current")


class _TmnxOamVccvPgTgFec128CtlDstAddrT_Type(InetAddressType):
    """Custom type tmnxOamVccvPgTgFec128CtlDstAddrT based on InetAddressType"""
    defaultValue = 0


_TmnxOamVccvPgTgFec128CtlDstAddrT_Type.__name__ = "InetAddressType"
_TmnxOamVccvPgTgFec128CtlDstAddrT_Object = MibTableColumn
tmnxOamVccvPgTgFec128CtlDstAddrT = _TmnxOamVccvPgTgFec128CtlDstAddrT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 24, 1, 3),
    _TmnxOamVccvPgTgFec128CtlDstAddrT_Type()
)
tmnxOamVccvPgTgFec128CtlDstAddrT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamVccvPgTgFec128CtlDstAddrT.setStatus("current")


class _TmnxOamVccvPgTgFec128CtlDstAddr_Type(InetAddress):
    """Custom type tmnxOamVccvPgTgFec128CtlDstAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamVccvPgTgFec128CtlDstAddr_Type.__name__ = "InetAddress"
_TmnxOamVccvPgTgFec128CtlDstAddr_Object = MibTableColumn
tmnxOamVccvPgTgFec128CtlDstAddr = _TmnxOamVccvPgTgFec128CtlDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 24, 1, 4),
    _TmnxOamVccvPgTgFec128CtlDstAddr_Type()
)
tmnxOamVccvPgTgFec128CtlDstAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamVccvPgTgFec128CtlDstAddr.setStatus("current")


class _TmnxOamVccvPgTgFec128CtlPwId_Type(Unsigned32):
    """Custom type tmnxOamVccvPgTgFec128CtlPwId based on Unsigned32"""
    defaultValue = 0


_TmnxOamVccvPgTgFec128CtlPwId_Type.__name__ = "Unsigned32"
_TmnxOamVccvPgTgFec128CtlPwId_Object = MibTableColumn
tmnxOamVccvPgTgFec128CtlPwId = _TmnxOamVccvPgTgFec128CtlPwId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 24, 1, 5),
    _TmnxOamVccvPgTgFec128CtlPwId_Type()
)
tmnxOamVccvPgTgFec128CtlPwId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamVccvPgTgFec128CtlPwId.setStatus("current")


class _TmnxOamVccvPgTgFec128CtlPwType_Type(Unsigned32):
    """Custom type tmnxOamVccvPgTgFec128CtlPwType based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TmnxOamVccvPgTgFec128CtlPwType_Type.__name__ = "Unsigned32"
_TmnxOamVccvPgTgFec128CtlPwType_Object = MibTableColumn
tmnxOamVccvPgTgFec128CtlPwType = _TmnxOamVccvPgTgFec128CtlPwType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 24, 1, 6),
    _TmnxOamVccvPgTgFec128CtlPwType_Type()
)
tmnxOamVccvPgTgFec128CtlPwType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamVccvPgTgFec128CtlPwType.setStatus("current")
_TmnxOamVccvPgTgStaticCtlTable_Object = MibTable
tmnxOamVccvPgTgStaticCtlTable = _TmnxOamVccvPgTgStaticCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 25)
)
if mibBuilder.loadTexts:
    tmnxOamVccvPgTgStaticCtlTable.setStatus("current")
_TmnxOamVccvPgTgStaticCtlEntry_Object = MibTableRow
tmnxOamVccvPgTgStaticCtlEntry = _TmnxOamVccvPgTgStaticCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 25, 1)
)
tmnxOamVccvPgTgStaticCtlEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamVccvPgTgStaticCtlEntry.setStatus("current")


class _TmnxOamVccvPgTgStaticCtlAgi_Type(TmnxVPNRouteDistinguisher):
    """Custom type tmnxOamVccvPgTgStaticCtlAgi based on TmnxVPNRouteDistinguisher"""
    defaultHexValue = "0000000000000000"


_TmnxOamVccvPgTgStaticCtlAgi_Type.__name__ = "TmnxVPNRouteDistinguisher"
_TmnxOamVccvPgTgStaticCtlAgi_Object = MibTableColumn
tmnxOamVccvPgTgStaticCtlAgi = _TmnxOamVccvPgTgStaticCtlAgi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 25, 1, 1),
    _TmnxOamVccvPgTgStaticCtlAgi_Type()
)
tmnxOamVccvPgTgStaticCtlAgi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamVccvPgTgStaticCtlAgi.setStatus("current")


class _TmnxOamVccvPgTgStaticCtlSaiiGlbl_Type(TmnxPwGlobalIdOrZero):
    """Custom type tmnxOamVccvPgTgStaticCtlSaiiGlbl based on TmnxPwGlobalIdOrZero"""
    defaultValue = 0


_TmnxOamVccvPgTgStaticCtlSaiiGlbl_Type.__name__ = "TmnxPwGlobalIdOrZero"
_TmnxOamVccvPgTgStaticCtlSaiiGlbl_Object = MibTableColumn
tmnxOamVccvPgTgStaticCtlSaiiGlbl = _TmnxOamVccvPgTgStaticCtlSaiiGlbl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 25, 1, 2),
    _TmnxOamVccvPgTgStaticCtlSaiiGlbl_Type()
)
tmnxOamVccvPgTgStaticCtlSaiiGlbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamVccvPgTgStaticCtlSaiiGlbl.setStatus("current")


class _TmnxOamVccvPgTgStaticCtlSaiiNode_Type(TmnxMplsTpNodeID):
    """Custom type tmnxOamVccvPgTgStaticCtlSaiiNode based on TmnxMplsTpNodeID"""
    defaultValue = 0


_TmnxOamVccvPgTgStaticCtlSaiiNode_Type.__name__ = "TmnxMplsTpNodeID"
_TmnxOamVccvPgTgStaticCtlSaiiNode_Object = MibTableColumn
tmnxOamVccvPgTgStaticCtlSaiiNode = _TmnxOamVccvPgTgStaticCtlSaiiNode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 25, 1, 3),
    _TmnxOamVccvPgTgStaticCtlSaiiNode_Type()
)
tmnxOamVccvPgTgStaticCtlSaiiNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamVccvPgTgStaticCtlSaiiNode.setStatus("current")


class _TmnxOamVccvPgTgStaticCtlSaiiAcId_Type(Unsigned32):
    """Custom type tmnxOamVccvPgTgStaticCtlSaiiAcId based on Unsigned32"""
    defaultValue = 0


_TmnxOamVccvPgTgStaticCtlSaiiAcId_Type.__name__ = "Unsigned32"
_TmnxOamVccvPgTgStaticCtlSaiiAcId_Object = MibTableColumn
tmnxOamVccvPgTgStaticCtlSaiiAcId = _TmnxOamVccvPgTgStaticCtlSaiiAcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 25, 1, 4),
    _TmnxOamVccvPgTgStaticCtlSaiiAcId_Type()
)
tmnxOamVccvPgTgStaticCtlSaiiAcId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamVccvPgTgStaticCtlSaiiAcId.setStatus("current")


class _TmnxOamVccvPgTgStaticCtlTaiiGlbl_Type(TmnxPwGlobalIdOrZero):
    """Custom type tmnxOamVccvPgTgStaticCtlTaiiGlbl based on TmnxPwGlobalIdOrZero"""
    defaultValue = 0


_TmnxOamVccvPgTgStaticCtlTaiiGlbl_Type.__name__ = "TmnxPwGlobalIdOrZero"
_TmnxOamVccvPgTgStaticCtlTaiiGlbl_Object = MibTableColumn
tmnxOamVccvPgTgStaticCtlTaiiGlbl = _TmnxOamVccvPgTgStaticCtlTaiiGlbl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 25, 1, 5),
    _TmnxOamVccvPgTgStaticCtlTaiiGlbl_Type()
)
tmnxOamVccvPgTgStaticCtlTaiiGlbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamVccvPgTgStaticCtlTaiiGlbl.setStatus("current")


class _TmnxOamVccvPgTgStaticCtlTaiiNode_Type(TmnxMplsTpNodeID):
    """Custom type tmnxOamVccvPgTgStaticCtlTaiiNode based on TmnxMplsTpNodeID"""
    defaultValue = 0


_TmnxOamVccvPgTgStaticCtlTaiiNode_Type.__name__ = "TmnxMplsTpNodeID"
_TmnxOamVccvPgTgStaticCtlTaiiNode_Object = MibTableColumn
tmnxOamVccvPgTgStaticCtlTaiiNode = _TmnxOamVccvPgTgStaticCtlTaiiNode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 25, 1, 6),
    _TmnxOamVccvPgTgStaticCtlTaiiNode_Type()
)
tmnxOamVccvPgTgStaticCtlTaiiNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamVccvPgTgStaticCtlTaiiNode.setStatus("current")


class _TmnxOamVccvPgTgStaticCtlTaiiAcId_Type(Unsigned32):
    """Custom type tmnxOamVccvPgTgStaticCtlTaiiAcId based on Unsigned32"""
    defaultValue = 0


_TmnxOamVccvPgTgStaticCtlTaiiAcId_Type.__name__ = "Unsigned32"
_TmnxOamVccvPgTgStaticCtlTaiiAcId_Object = MibTableColumn
tmnxOamVccvPgTgStaticCtlTaiiAcId = _TmnxOamVccvPgTgStaticCtlTaiiAcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 25, 1, 7),
    _TmnxOamVccvPgTgStaticCtlTaiiAcId_Type()
)
tmnxOamVccvPgTgStaticCtlTaiiAcId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamVccvPgTgStaticCtlTaiiAcId.setStatus("current")
_TmnxOamVxlanPingCtlTable_Object = MibTable
tmnxOamVxlanPingCtlTable = _TmnxOamVxlanPingCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 26)
)
if mibBuilder.loadTexts:
    tmnxOamVxlanPingCtlTable.setStatus("current")
_TmnxOamVxlanPingCtlEntry_Object = MibTableRow
tmnxOamVxlanPingCtlEntry = _TmnxOamVxlanPingCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 26, 1)
)
tmnxOamVxlanPingCtlEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamVxlanPingCtlEntry.setStatus("current")


class _TmnxOamVxlanPingCtlNetworkId_Type(Unsigned32):
    """Custom type tmnxOamVxlanPingCtlNetworkId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 16777215),
    )


_TmnxOamVxlanPingCtlNetworkId_Type.__name__ = "Unsigned32"
_TmnxOamVxlanPingCtlNetworkId_Object = MibTableColumn
tmnxOamVxlanPingCtlNetworkId = _TmnxOamVxlanPingCtlNetworkId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 26, 1, 1),
    _TmnxOamVxlanPingCtlNetworkId_Type()
)
tmnxOamVxlanPingCtlNetworkId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamVxlanPingCtlNetworkId.setStatus("current")


class _TmnxOamVxlanPingCtlReplyMode_Type(Integer32):
    """Custom type tmnxOamVxlanPingCtlReplyMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("udp", 2),
          ("overlay", 3))
    )


_TmnxOamVxlanPingCtlReplyMode_Type.__name__ = "Integer32"
_TmnxOamVxlanPingCtlReplyMode_Object = MibTableColumn
tmnxOamVxlanPingCtlReplyMode = _TmnxOamVxlanPingCtlReplyMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 26, 1, 2),
    _TmnxOamVxlanPingCtlReplyMode_Type()
)
tmnxOamVxlanPingCtlReplyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamVxlanPingCtlReplyMode.setStatus("current")


class _TmnxOamVxlanPingCtlIFlag_Type(Unsigned32):
    """Custom type tmnxOamVxlanPingCtlIFlag based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_TmnxOamVxlanPingCtlIFlag_Type.__name__ = "Unsigned32"
_TmnxOamVxlanPingCtlIFlag_Object = MibTableColumn
tmnxOamVxlanPingCtlIFlag = _TmnxOamVxlanPingCtlIFlag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 26, 1, 3),
    _TmnxOamVxlanPingCtlIFlag_Type()
)
tmnxOamVxlanPingCtlIFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamVxlanPingCtlIFlag.setStatus("current")


class _TmnxOamVxlanPingCtlTestId_Type(Unsigned32):
    """Custom type tmnxOamVxlanPingCtlTestId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TmnxOamVxlanPingCtlTestId_Type.__name__ = "Unsigned32"
_TmnxOamVxlanPingCtlTestId_Object = MibTableColumn
tmnxOamVxlanPingCtlTestId = _TmnxOamVxlanPingCtlTestId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 26, 1, 4),
    _TmnxOamVxlanPingCtlTestId_Type()
)
tmnxOamVxlanPingCtlTestId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamVxlanPingCtlTestId.setStatus("current")


class _TmnxOamVxlanPingCtlOutSrcUdpPt_Type(Unsigned32):
    """Custom type tmnxOamVxlanPingCtlOutSrcUdpPt based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_TmnxOamVxlanPingCtlOutSrcUdpPt_Type.__name__ = "Unsigned32"
_TmnxOamVxlanPingCtlOutSrcUdpPt_Object = MibTableColumn
tmnxOamVxlanPingCtlOutSrcUdpPt = _TmnxOamVxlanPingCtlOutSrcUdpPt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 26, 1, 5),
    _TmnxOamVxlanPingCtlOutSrcUdpPt_Type()
)
tmnxOamVxlanPingCtlOutSrcUdpPt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamVxlanPingCtlOutSrcUdpPt.setStatus("current")


class _TmnxOamVxlanPingCtlOutIpTtl_Type(Unsigned32):
    """Custom type tmnxOamVxlanPingCtlOutIpTtl based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TmnxOamVxlanPingCtlOutIpTtl_Type.__name__ = "Unsigned32"
_TmnxOamVxlanPingCtlOutIpTtl_Object = MibTableColumn
tmnxOamVxlanPingCtlOutIpTtl = _TmnxOamVxlanPingCtlOutIpTtl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 26, 1, 6),
    _TmnxOamVxlanPingCtlOutIpTtl_Type()
)
tmnxOamVxlanPingCtlOutIpTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamVxlanPingCtlOutIpTtl.setStatus("current")


class _TmnxOamVxlanPingCtlInL2DestMac_Type(MacAddress):
    """Custom type tmnxOamVxlanPingCtlInL2DestMac based on MacAddress"""
    defaultHexValue = "000000000000"


_TmnxOamVxlanPingCtlInL2DestMac_Type.__name__ = "MacAddress"
_TmnxOamVxlanPingCtlInL2DestMac_Object = MibTableColumn
tmnxOamVxlanPingCtlInL2DestMac = _TmnxOamVxlanPingCtlInL2DestMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 26, 1, 7),
    _TmnxOamVxlanPingCtlInL2DestMac_Type()
)
tmnxOamVxlanPingCtlInL2DestMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamVxlanPingCtlInL2DestMac.setStatus("current")


class _TmnxOamVxlanPingCtlInIpSrcAddrT_Type(InetAddressType):
    """Custom type tmnxOamVxlanPingCtlInIpSrcAddrT based on InetAddressType"""
    defaultValue = 1


_TmnxOamVxlanPingCtlInIpSrcAddrT_Type.__name__ = "InetAddressType"
_TmnxOamVxlanPingCtlInIpSrcAddrT_Object = MibTableColumn
tmnxOamVxlanPingCtlInIpSrcAddrT = _TmnxOamVxlanPingCtlInIpSrcAddrT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 26, 1, 8),
    _TmnxOamVxlanPingCtlInIpSrcAddrT_Type()
)
tmnxOamVxlanPingCtlInIpSrcAddrT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamVxlanPingCtlInIpSrcAddrT.setStatus("current")


class _TmnxOamVxlanPingCtlInIpSrcAddr_Type(InetAddress):
    """Custom type tmnxOamVxlanPingCtlInIpSrcAddr based on InetAddress"""
    defaultHexValue = "00000000"

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamVxlanPingCtlInIpSrcAddr_Type.__name__ = "InetAddress"
_TmnxOamVxlanPingCtlInIpSrcAddr_Object = MibTableColumn
tmnxOamVxlanPingCtlInIpSrcAddr = _TmnxOamVxlanPingCtlInIpSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 26, 1, 9),
    _TmnxOamVxlanPingCtlInIpSrcAddr_Type()
)
tmnxOamVxlanPingCtlInIpSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamVxlanPingCtlInIpSrcAddr.setStatus("current")


class _TmnxOamVxlanPingCtlInIpDstAddrT_Type(InetAddressType):
    """Custom type tmnxOamVxlanPingCtlInIpDstAddrT based on InetAddressType"""
    defaultValue = 1


_TmnxOamVxlanPingCtlInIpDstAddrT_Type.__name__ = "InetAddressType"
_TmnxOamVxlanPingCtlInIpDstAddrT_Object = MibTableColumn
tmnxOamVxlanPingCtlInIpDstAddrT = _TmnxOamVxlanPingCtlInIpDstAddrT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 26, 1, 10),
    _TmnxOamVxlanPingCtlInIpDstAddrT_Type()
)
tmnxOamVxlanPingCtlInIpDstAddrT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamVxlanPingCtlInIpDstAddrT.setStatus("current")


class _TmnxOamVxlanPingCtlInIpDstAddr_Type(InetAddress):
    """Custom type tmnxOamVxlanPingCtlInIpDstAddr based on InetAddress"""
    defaultHexValue = "7f000001"

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamVxlanPingCtlInIpDstAddr_Type.__name__ = "InetAddress"
_TmnxOamVxlanPingCtlInIpDstAddr_Object = MibTableColumn
tmnxOamVxlanPingCtlInIpDstAddr = _TmnxOamVxlanPingCtlInIpDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 26, 1, 11),
    _TmnxOamVxlanPingCtlInIpDstAddr_Type()
)
tmnxOamVxlanPingCtlInIpDstAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamVxlanPingCtlInIpDstAddr.setStatus("current")


class _TmnxOamVxlanPingCtlEndSysMacAddr_Type(MacAddress):
    """Custom type tmnxOamVxlanPingCtlEndSysMacAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_TmnxOamVxlanPingCtlEndSysMacAddr_Type.__name__ = "MacAddress"
_TmnxOamVxlanPingCtlEndSysMacAddr_Object = MibTableColumn
tmnxOamVxlanPingCtlEndSysMacAddr = _TmnxOamVxlanPingCtlEndSysMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 26, 1, 12),
    _TmnxOamVxlanPingCtlEndSysMacAddr_Type()
)
tmnxOamVxlanPingCtlEndSysMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamVxlanPingCtlEndSysMacAddr.setStatus("current")


class _TmnxOamVxlanPingCtlReflectPad_Type(TruthValue):
    """Custom type tmnxOamVxlanPingCtlReflectPad based on TruthValue"""
    defaultValue = 2


_TmnxOamVxlanPingCtlReflectPad_Type.__name__ = "TruthValue"
_TmnxOamVxlanPingCtlReflectPad_Object = MibTableColumn
tmnxOamVxlanPingCtlReflectPad = _TmnxOamVxlanPingCtlReflectPad_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 26, 1, 13),
    _TmnxOamVxlanPingCtlReflectPad_Type()
)
tmnxOamVxlanPingCtlReflectPad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamVxlanPingCtlReflectPad.setStatus("current")
_TmnxOamVxlanPingHistoryTable_Object = MibTable
tmnxOamVxlanPingHistoryTable = _TmnxOamVxlanPingHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 27)
)
if mibBuilder.loadTexts:
    tmnxOamVxlanPingHistoryTable.setStatus("current")
_TmnxOamVxlanPingHistoryEntry_Object = MibTableRow
tmnxOamVxlanPingHistoryEntry = _TmnxOamVxlanPingHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 27, 1)
)
tmnxOamVxlanPingHistoryEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTestIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsTestRunIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamVxlanPingHistoryEntry.setStatus("current")


class _TmnxOamVxlanPingHistReturnCode_Type(Unsigned32):
    """Custom type tmnxOamVxlanPingHistReturnCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxOamVxlanPingHistReturnCode_Type.__name__ = "Unsigned32"
_TmnxOamVxlanPingHistReturnCode_Object = MibTableColumn
tmnxOamVxlanPingHistReturnCode = _TmnxOamVxlanPingHistReturnCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 27, 1, 1),
    _TmnxOamVxlanPingHistReturnCode_Type()
)
tmnxOamVxlanPingHistReturnCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVxlanPingHistReturnCode.setStatus("current")


class _TmnxOamVxlanPingHistRtrnSubCode_Type(Unsigned32):
    """Custom type tmnxOamVxlanPingHistRtrnSubCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxOamVxlanPingHistRtrnSubCode_Type.__name__ = "Unsigned32"
_TmnxOamVxlanPingHistRtrnSubCode_Object = MibTableColumn
tmnxOamVxlanPingHistRtrnSubCode = _TmnxOamVxlanPingHistRtrnSubCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 27, 1, 2),
    _TmnxOamVxlanPingHistRtrnSubCode_Type()
)
tmnxOamVxlanPingHistRtrnSubCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVxlanPingHistRtrnSubCode.setStatus("current")


class _TmnxOamVxlanPingHistValidationRC_Type(Unsigned32):
    """Custom type tmnxOamVxlanPingHistValidationRC based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TmnxOamVxlanPingHistValidationRC_Type.__name__ = "Unsigned32"
_TmnxOamVxlanPingHistValidationRC_Object = MibTableColumn
tmnxOamVxlanPingHistValidationRC = _TmnxOamVxlanPingHistValidationRC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 27, 1, 3),
    _TmnxOamVxlanPingHistValidationRC_Type()
)
tmnxOamVxlanPingHistValidationRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVxlanPingHistValidationRC.setStatus("current")


class _TmnxOamVxlanPingHistNetworkId_Type(Unsigned32):
    """Custom type tmnxOamVxlanPingHistNetworkId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_TmnxOamVxlanPingHistNetworkId_Type.__name__ = "Unsigned32"
_TmnxOamVxlanPingHistNetworkId_Object = MibTableColumn
tmnxOamVxlanPingHistNetworkId = _TmnxOamVxlanPingHistNetworkId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 27, 1, 4),
    _TmnxOamVxlanPingHistNetworkId_Type()
)
tmnxOamVxlanPingHistNetworkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVxlanPingHistNetworkId.setStatus("current")


class _TmnxOamVxlanPingHistOutIpTtl_Type(Unsigned32):
    """Custom type tmnxOamVxlanPingHistOutIpTtl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxOamVxlanPingHistOutIpTtl_Type.__name__ = "Unsigned32"
_TmnxOamVxlanPingHistOutIpTtl_Object = MibTableColumn
tmnxOamVxlanPingHistOutIpTtl = _TmnxOamVxlanPingHistOutIpTtl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 27, 1, 5),
    _TmnxOamVxlanPingHistOutIpTtl_Type()
)
tmnxOamVxlanPingHistOutIpTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVxlanPingHistOutIpTtl.setStatus("current")
_TmnxOamBfdOnLspPingResultsTable_Object = MibTable
tmnxOamBfdOnLspPingResultsTable = _TmnxOamBfdOnLspPingResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 28)
)
if mibBuilder.loadTexts:
    tmnxOamBfdOnLspPingResultsTable.setStatus("current")
_TmnxOamBfdOnLspPingResultsEntry_Object = MibTableRow
tmnxOamBfdOnLspPingResultsEntry = _TmnxOamBfdOnLspPingResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 28, 1)
)
tmnxOamBfdOnLspPingResultsEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamBfdOnLspLocalBfdDiscrim"),
)
if mibBuilder.loadTexts:
    tmnxOamBfdOnLspPingResultsEntry.setStatus("current")


class _TmnxOamBfdOnLspLocalBfdDiscrim_Type(Unsigned32):
    """Custom type tmnxOamBfdOnLspLocalBfdDiscrim based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxOamBfdOnLspLocalBfdDiscrim_Type.__name__ = "Unsigned32"
_TmnxOamBfdOnLspLocalBfdDiscrim_Object = MibTableColumn
tmnxOamBfdOnLspLocalBfdDiscrim = _TmnxOamBfdOnLspLocalBfdDiscrim_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 28, 1, 1),
    _TmnxOamBfdOnLspLocalBfdDiscrim_Type()
)
tmnxOamBfdOnLspLocalBfdDiscrim.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamBfdOnLspLocalBfdDiscrim.setStatus("current")
_TmnxOamBfdOnLspRemoteBfdDiscrim_Type = Unsigned32
_TmnxOamBfdOnLspRemoteBfdDiscrim_Object = MibTableColumn
tmnxOamBfdOnLspRemoteBfdDiscrim = _TmnxOamBfdOnLspRemoteBfdDiscrim_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 28, 1, 2),
    _TmnxOamBfdOnLspRemoteBfdDiscrim_Type()
)
tmnxOamBfdOnLspRemoteBfdDiscrim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamBfdOnLspRemoteBfdDiscrim.setStatus("current")
_TmnxOamBfdOnLspRemoteAddressType_Type = InetAddressType
_TmnxOamBfdOnLspRemoteAddressType_Object = MibTableColumn
tmnxOamBfdOnLspRemoteAddressType = _TmnxOamBfdOnLspRemoteAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 28, 1, 3),
    _TmnxOamBfdOnLspRemoteAddressType_Type()
)
tmnxOamBfdOnLspRemoteAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamBfdOnLspRemoteAddressType.setStatus("current")


class _TmnxOamBfdOnLspRemoteAddress_Type(InetAddress):
    """Custom type tmnxOamBfdOnLspRemoteAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamBfdOnLspRemoteAddress_Type.__name__ = "InetAddress"
_TmnxOamBfdOnLspRemoteAddress_Object = MibTableColumn
tmnxOamBfdOnLspRemoteAddress = _TmnxOamBfdOnLspRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 28, 1, 4),
    _TmnxOamBfdOnLspRemoteAddress_Type()
)
tmnxOamBfdOnLspRemoteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamBfdOnLspRemoteAddress.setStatus("current")
_TmnxOamBfdOnLspLspName_Type = TLNamedItemOrEmpty
_TmnxOamBfdOnLspLspName_Object = MibTableColumn
tmnxOamBfdOnLspLspName = _TmnxOamBfdOnLspLspName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 28, 1, 5),
    _TmnxOamBfdOnLspLspName_Type()
)
tmnxOamBfdOnLspLspName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamBfdOnLspLspName.setStatus("current")
_TmnxOamBfdOnLspPingReturnCode_Type = TmnxOamPingRtnCode
_TmnxOamBfdOnLspPingReturnCode_Object = MibTableColumn
tmnxOamBfdOnLspPingReturnCode = _TmnxOamBfdOnLspPingReturnCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 28, 1, 6),
    _TmnxOamBfdOnLspPingReturnCode_Type()
)
tmnxOamBfdOnLspPingReturnCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamBfdOnLspPingReturnCode.setStatus("current")
_TmnxOamBfdOnLspPingReturnSubcode_Type = Unsigned32
_TmnxOamBfdOnLspPingReturnSubcode_Object = MibTableColumn
tmnxOamBfdOnLspPingReturnSubcode = _TmnxOamBfdOnLspPingReturnSubcode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 28, 1, 7),
    _TmnxOamBfdOnLspPingReturnSubcode_Type()
)
tmnxOamBfdOnLspPingReturnSubcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamBfdOnLspPingReturnSubcode.setStatus("current")
_TmnxOamBfdOnLspPingTxCount_Type = Unsigned32
_TmnxOamBfdOnLspPingTxCount_Object = MibTableColumn
tmnxOamBfdOnLspPingTxCount = _TmnxOamBfdOnLspPingTxCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 28, 1, 8),
    _TmnxOamBfdOnLspPingTxCount_Type()
)
tmnxOamBfdOnLspPingTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamBfdOnLspPingTxCount.setStatus("current")
_TmnxOamBfdOnLspPingRxCount_Type = Unsigned32
_TmnxOamBfdOnLspPingRxCount_Object = MibTableColumn
tmnxOamBfdOnLspPingRxCount = _TmnxOamBfdOnLspPingRxCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 28, 1, 9),
    _TmnxOamBfdOnLspPingRxCount_Type()
)
tmnxOamBfdOnLspPingRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamBfdOnLspPingRxCount.setStatus("current")


class _TmnxOamBfdOnLspPathState_Type(Integer32):
    """Custom type tmnxOamBfdOnLspPathState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("active", 2),
          ("inactive", 3))
    )


_TmnxOamBfdOnLspPathState_Type.__name__ = "Integer32"
_TmnxOamBfdOnLspPathState_Object = MibTableColumn
tmnxOamBfdOnLspPathState = _TmnxOamBfdOnLspPathState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 28, 1, 10),
    _TmnxOamBfdOnLspPathState_Type()
)
tmnxOamBfdOnLspPathState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamBfdOnLspPathState.setStatus("current")
_TmnxOamBfdOnLspPingTxInterval_Type = Unsigned32
_TmnxOamBfdOnLspPingTxInterval_Object = MibTableColumn
tmnxOamBfdOnLspPingTxInterval = _TmnxOamBfdOnLspPingTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 28, 1, 11),
    _TmnxOamBfdOnLspPingTxInterval_Type()
)
tmnxOamBfdOnLspPingTxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamBfdOnLspPingTxInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamBfdOnLspPingTxInterval.setUnits("seconds")
_TmnxOamBfdOnLspBootStrRetryCount_Type = Unsigned32
_TmnxOamBfdOnLspBootStrRetryCount_Object = MibTableColumn
tmnxOamBfdOnLspBootStrRetryCount = _TmnxOamBfdOnLspBootStrRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 28, 1, 12),
    _TmnxOamBfdOnLspBootStrRetryCount_Type()
)
tmnxOamBfdOnLspBootStrRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamBfdOnLspBootStrRetryCount.setStatus("current")
_TmnxOamBfdOnLspFecType_Type = TmnxBfdOnLspSessFecType
_TmnxOamBfdOnLspFecType_Object = MibTableColumn
tmnxOamBfdOnLspFecType = _TmnxOamBfdOnLspFecType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 28, 1, 13),
    _TmnxOamBfdOnLspFecType_Type()
)
tmnxOamBfdOnLspFecType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamBfdOnLspFecType.setStatus("current")
_TmnxOamBfdOnLspPrefixType_Type = InetAddressType
_TmnxOamBfdOnLspPrefixType_Object = MibTableColumn
tmnxOamBfdOnLspPrefixType = _TmnxOamBfdOnLspPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 28, 1, 14),
    _TmnxOamBfdOnLspPrefixType_Type()
)
tmnxOamBfdOnLspPrefixType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamBfdOnLspPrefixType.setStatus("current")


class _TmnxOamBfdOnLspPrefix_Type(InetAddress):
    """Custom type tmnxOamBfdOnLspPrefix based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamBfdOnLspPrefix_Type.__name__ = "InetAddress"
_TmnxOamBfdOnLspPrefix_Object = MibTableColumn
tmnxOamBfdOnLspPrefix = _TmnxOamBfdOnLspPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 28, 1, 15),
    _TmnxOamBfdOnLspPrefix_Type()
)
tmnxOamBfdOnLspPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamBfdOnLspPrefix.setStatus("current")


class _TmnxOamBfdOnLspPrefixLen_Type(InetAddressPrefixLength):
    """Custom type tmnxOamBfdOnLspPrefixLen based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_TmnxOamBfdOnLspPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxOamBfdOnLspPrefixLen_Object = MibTableColumn
tmnxOamBfdOnLspPrefixLen = _TmnxOamBfdOnLspPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 28, 1, 16),
    _TmnxOamBfdOnLspPrefixLen_Type()
)
tmnxOamBfdOnLspPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamBfdOnLspPrefixLen.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamBfdOnLspPrefixLen.setUnits("bits")
_TmnxOamBfdOnLspSourceAddressType_Type = InetAddressType
_TmnxOamBfdOnLspSourceAddressType_Object = MibTableColumn
tmnxOamBfdOnLspSourceAddressType = _TmnxOamBfdOnLspSourceAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 28, 1, 17),
    _TmnxOamBfdOnLspSourceAddressType_Type()
)
tmnxOamBfdOnLspSourceAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamBfdOnLspSourceAddressType.setStatus("current")


class _TmnxOamBfdOnLspSourceAddress_Type(InetAddress):
    """Custom type tmnxOamBfdOnLspSourceAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamBfdOnLspSourceAddress_Type.__name__ = "InetAddress"
_TmnxOamBfdOnLspSourceAddress_Object = MibTableColumn
tmnxOamBfdOnLspSourceAddress = _TmnxOamBfdOnLspSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 28, 1, 18),
    _TmnxOamBfdOnLspSourceAddress_Type()
)
tmnxOamBfdOnLspSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamBfdOnLspSourceAddress.setStatus("current")


class _TmnxOamBfdOnLspOperState_Type(Integer32):
    """Custom type tmnxOamBfdOnLspOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bootstrapInProg", 1),
          ("bootstrappedNoPeriodicVerif", 2),
          ("bootstrappedSendingPeriodicVerif", 3))
    )


_TmnxOamBfdOnLspOperState_Type.__name__ = "Integer32"
_TmnxOamBfdOnLspOperState_Object = MibTableColumn
tmnxOamBfdOnLspOperState = _TmnxOamBfdOnLspOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 28, 1, 19),
    _TmnxOamBfdOnLspOperState_Type()
)
tmnxOamBfdOnLspOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamBfdOnLspOperState.setStatus("current")
_TmnxOamVxlanPingResultsTable_Object = MibTable
tmnxOamVxlanPingResultsTable = _TmnxOamVxlanPingResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 29)
)
if mibBuilder.loadTexts:
    tmnxOamVxlanPingResultsTable.setStatus("current")
_TmnxOamVxlanPingResultsEntry_Object = MibTableRow
tmnxOamVxlanPingResultsEntry = _TmnxOamVxlanPingResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 29, 1)
)
tmnxOamVxlanPingResultsEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTestIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsTestRunIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamVxlanPingResultsEntry.setStatus("current")
_TmnxOamVxlanPingResOutSrcAddrTyp_Type = InetAddressType
_TmnxOamVxlanPingResOutSrcAddrTyp_Object = MibTableColumn
tmnxOamVxlanPingResOutSrcAddrTyp = _TmnxOamVxlanPingResOutSrcAddrTyp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 29, 1, 1),
    _TmnxOamVxlanPingResOutSrcAddrTyp_Type()
)
tmnxOamVxlanPingResOutSrcAddrTyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVxlanPingResOutSrcAddrTyp.setStatus("current")


class _TmnxOamVxlanPingResOutSrcAddress_Type(InetAddress):
    """Custom type tmnxOamVxlanPingResOutSrcAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamVxlanPingResOutSrcAddress_Type.__name__ = "InetAddress"
_TmnxOamVxlanPingResOutSrcAddress_Object = MibTableColumn
tmnxOamVxlanPingResOutSrcAddress = _TmnxOamVxlanPingResOutSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 29, 1, 2),
    _TmnxOamVxlanPingResOutSrcAddress_Type()
)
tmnxOamVxlanPingResOutSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVxlanPingResOutSrcAddress.setStatus("current")
_TmnxOamPingReadOnlyScalars_ObjectIdentity = ObjectIdentity
tmnxOamPingReadOnlyScalars = _TmnxOamPingReadOnlyScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 30)
)
_TmnxOamBfdOnLspSessBootstrInProg_Type = Gauge32
_TmnxOamBfdOnLspSessBootstrInProg_Object = MibScalar
tmnxOamBfdOnLspSessBootstrInProg = _TmnxOamBfdOnLspSessBootstrInProg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 30, 1),
    _TmnxOamBfdOnLspSessBootstrInProg_Type()
)
tmnxOamBfdOnLspSessBootstrInProg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamBfdOnLspSessBootstrInProg.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamBfdOnLspSessBootstrInProg.setUnits("sessions")
_TmnxOamBfdOnLspSessBootstrNoPV_Type = Gauge32
_TmnxOamBfdOnLspSessBootstrNoPV_Object = MibScalar
tmnxOamBfdOnLspSessBootstrNoPV = _TmnxOamBfdOnLspSessBootstrNoPV_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 30, 2),
    _TmnxOamBfdOnLspSessBootstrNoPV_Type()
)
tmnxOamBfdOnLspSessBootstrNoPV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamBfdOnLspSessBootstrNoPV.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamBfdOnLspSessBootstrNoPV.setUnits("sessions")
_TmnxOamBfdOnLspSessBootstrSendPV_Type = Gauge32
_TmnxOamBfdOnLspSessBootstrSendPV_Object = MibScalar
tmnxOamBfdOnLspSessBootstrSendPV = _TmnxOamBfdOnLspSessBootstrSendPV_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 30, 3),
    _TmnxOamBfdOnLspSessBootstrSendPV_Type()
)
tmnxOamBfdOnLspSessBootstrSendPV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamBfdOnLspSessBootstrSendPV.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamBfdOnLspSessBootstrSendPV.setUnits("sessions")
_TmnxOamBierPingCtlTable_Object = MibTable
tmnxOamBierPingCtlTable = _TmnxOamBierPingCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 31)
)
if mibBuilder.loadTexts:
    tmnxOamBierPingCtlTable.setStatus("current")
_TmnxOamBierPingCtlEntry_Object = MibTableRow
tmnxOamBierPingCtlEntry = _TmnxOamBierPingCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 31, 1)
)
tmnxOamBierPingCtlEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamBierPingCtlEntry.setStatus("current")


class _TmnxOamBierPingCtlSubDomain_Type(Unsigned32):
    """Custom type tmnxOamBierPingCtlSubDomain based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxOamBierPingCtlSubDomain_Type.__name__ = "Unsigned32"
_TmnxOamBierPingCtlSubDomain_Object = MibTableColumn
tmnxOamBierPingCtlSubDomain = _TmnxOamBierPingCtlSubDomain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 31, 1, 1),
    _TmnxOamBierPingCtlSubDomain_Type()
)
tmnxOamBierPingCtlSubDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamBierPingCtlSubDomain.setStatus("current")


class _TmnxOamBierPingCtlBfrId_Type(Unsigned32):
    """Custom type tmnxOamBierPingCtlBfrId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_TmnxOamBierPingCtlBfrId_Type.__name__ = "Unsigned32"
_TmnxOamBierPingCtlBfrId_Object = MibTableColumn
tmnxOamBierPingCtlBfrId = _TmnxOamBierPingCtlBfrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 31, 1, 2),
    _TmnxOamBierPingCtlBfrId_Type()
)
tmnxOamBierPingCtlBfrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamBierPingCtlBfrId.setStatus("current")


class _TmnxOamBierPingCtlBfrIdStart_Type(Unsigned32):
    """Custom type tmnxOamBierPingCtlBfrIdStart based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_TmnxOamBierPingCtlBfrIdStart_Type.__name__ = "Unsigned32"
_TmnxOamBierPingCtlBfrIdStart_Object = MibTableColumn
tmnxOamBierPingCtlBfrIdStart = _TmnxOamBierPingCtlBfrIdStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 31, 1, 3),
    _TmnxOamBierPingCtlBfrIdStart_Type()
)
tmnxOamBierPingCtlBfrIdStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamBierPingCtlBfrIdStart.setStatus("current")


class _TmnxOamBierPingCtlBfrIdEnd_Type(Unsigned32):
    """Custom type tmnxOamBierPingCtlBfrIdEnd based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_TmnxOamBierPingCtlBfrIdEnd_Type.__name__ = "Unsigned32"
_TmnxOamBierPingCtlBfrIdEnd_Object = MibTableColumn
tmnxOamBierPingCtlBfrIdEnd = _TmnxOamBierPingCtlBfrIdEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 31, 1, 4),
    _TmnxOamBierPingCtlBfrIdEnd_Type()
)
tmnxOamBierPingCtlBfrIdEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamBierPingCtlBfrIdEnd.setStatus("current")


class _TmnxOamBierPingCtlTtl_Type(Unsigned32):
    """Custom type tmnxOamBierPingCtlTtl based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TmnxOamBierPingCtlTtl_Type.__name__ = "Unsigned32"
_TmnxOamBierPingCtlTtl_Object = MibTableColumn
tmnxOamBierPingCtlTtl = _TmnxOamBierPingCtlTtl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 31, 1, 5),
    _TmnxOamBierPingCtlTtl_Type()
)
tmnxOamBierPingCtlTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamBierPingCtlTtl.setStatus("current")
_TmnxOamBierPingBfrPfxCtlTable_Object = MibTable
tmnxOamBierPingBfrPfxCtlTable = _TmnxOamBierPingBfrPfxCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 32)
)
if mibBuilder.loadTexts:
    tmnxOamBierPingBfrPfxCtlTable.setStatus("current")
_TmnxOamBierPingBfrPfxCtlEntry_Object = MibTableRow
tmnxOamBierPingBfrPfxCtlEntry = _TmnxOamBierPingBfrPfxCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 32, 1)
)
tmnxOamBierPingBfrPfxCtlEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTestIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamBierPingPfxIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamBierPingBfrPfxCtlEntry.setStatus("current")


class _TmnxOamBierPingPfxIndex_Type(Unsigned32):
    """Custom type tmnxOamBierPingPfxIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_TmnxOamBierPingPfxIndex_Type.__name__ = "Unsigned32"
_TmnxOamBierPingPfxIndex_Object = MibTableColumn
tmnxOamBierPingPfxIndex = _TmnxOamBierPingPfxIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 32, 1, 1),
    _TmnxOamBierPingPfxIndex_Type()
)
tmnxOamBierPingPfxIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamBierPingPfxIndex.setStatus("current")
_TmnxOamBierPingBfrPfxCtlRowState_Type = RowStatus
_TmnxOamBierPingBfrPfxCtlRowState_Object = MibTableColumn
tmnxOamBierPingBfrPfxCtlRowState = _TmnxOamBierPingBfrPfxCtlRowState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 32, 1, 2),
    _TmnxOamBierPingBfrPfxCtlRowState_Type()
)
tmnxOamBierPingBfrPfxCtlRowState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamBierPingBfrPfxCtlRowState.setStatus("current")


class _TmnxOamBierPingBfrPfxCtlAddrType_Type(InetAddressType):
    """Custom type tmnxOamBierPingBfrPfxCtlAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxOamBierPingBfrPfxCtlAddrType_Type.__name__ = "InetAddressType"
_TmnxOamBierPingBfrPfxCtlAddrType_Object = MibTableColumn
tmnxOamBierPingBfrPfxCtlAddrType = _TmnxOamBierPingBfrPfxCtlAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 32, 1, 3),
    _TmnxOamBierPingBfrPfxCtlAddrType_Type()
)
tmnxOamBierPingBfrPfxCtlAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamBierPingBfrPfxCtlAddrType.setStatus("current")


class _TmnxOamBierPingBfrPfxCtlAddress_Type(InetAddress):
    """Custom type tmnxOamBierPingBfrPfxCtlAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamBierPingBfrPfxCtlAddress_Type.__name__ = "InetAddress"
_TmnxOamBierPingBfrPfxCtlAddress_Object = MibTableColumn
tmnxOamBierPingBfrPfxCtlAddress = _TmnxOamBierPingBfrPfxCtlAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 32, 1, 4),
    _TmnxOamBierPingBfrPfxCtlAddress_Type()
)
tmnxOamBierPingBfrPfxCtlAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamBierPingBfrPfxCtlAddress.setStatus("current")
_TmnxOamBierPingHistoryTable_Object = MibTable
tmnxOamBierPingHistoryTable = _TmnxOamBierPingHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 33)
)
if mibBuilder.loadTexts:
    tmnxOamBierPingHistoryTable.setStatus("current")
_TmnxOamBierPingHistoryEntry_Object = MibTableRow
tmnxOamBierPingHistoryEntry = _TmnxOamBierPingHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 33, 1)
)
tmnxOamBierPingHistoryEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTestIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsTestRunIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamBierPingHistoryEntry.setStatus("current")


class _TmnxOamBierPingHistoryBfrId_Type(Unsigned32):
    """Custom type tmnxOamBierPingHistoryBfrId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_TmnxOamBierPingHistoryBfrId_Type.__name__ = "Unsigned32"
_TmnxOamBierPingHistoryBfrId_Object = MibTableColumn
tmnxOamBierPingHistoryBfrId = _TmnxOamBierPingHistoryBfrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 33, 1, 1),
    _TmnxOamBierPingHistoryBfrId_Type()
)
tmnxOamBierPingHistoryBfrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamBierPingHistoryBfrId.setStatus("current")
_TmnxOamBierPingHistoryBfrPfxType_Type = InetAddressType
_TmnxOamBierPingHistoryBfrPfxType_Object = MibTableColumn
tmnxOamBierPingHistoryBfrPfxType = _TmnxOamBierPingHistoryBfrPfxType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 33, 1, 2),
    _TmnxOamBierPingHistoryBfrPfxType_Type()
)
tmnxOamBierPingHistoryBfrPfxType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamBierPingHistoryBfrPfxType.setStatus("current")


class _TmnxOamBierPingHistoryBfrPfx_Type(InetAddress):
    """Custom type tmnxOamBierPingHistoryBfrPfx based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamBierPingHistoryBfrPfx_Type.__name__ = "InetAddress"
_TmnxOamBierPingHistoryBfrPfx_Object = MibTableColumn
tmnxOamBierPingHistoryBfrPfx = _TmnxOamBierPingHistoryBfrPfx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 33, 1, 3),
    _TmnxOamBierPingHistoryBfrPfx_Type()
)
tmnxOamBierPingHistoryBfrPfx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamBierPingHistoryBfrPfx.setStatus("current")
_TmnxOamBierPingHistoryReturnCode_Type = TmnxOamBierHistoryReturnCode
_TmnxOamBierPingHistoryReturnCode_Object = MibTableColumn
tmnxOamBierPingHistoryReturnCode = _TmnxOamBierPingHistoryReturnCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 33, 1, 4),
    _TmnxOamBierPingHistoryReturnCode_Type()
)
tmnxOamBierPingHistoryReturnCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamBierPingHistoryReturnCode.setStatus("current")
_TmnxOamTraceRouteObjs_ObjectIdentity = ObjectIdentity
tmnxOamTraceRouteObjs = _TmnxOamTraceRouteObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2)
)
_TmnxOamTraceRouteNotifyObjects_ObjectIdentity = ObjectIdentity
tmnxOamTraceRouteNotifyObjects = _TmnxOamTraceRouteNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 1)
)


class _TmnxOamTrMaxConcurrentRequests_Type(Unsigned32):
    """Custom type tmnxOamTrMaxConcurrentRequests based on Unsigned32"""
    defaultValue = 0


_TmnxOamTrMaxConcurrentRequests_Type.__name__ = "Unsigned32"
_TmnxOamTrMaxConcurrentRequests_Object = MibScalar
tmnxOamTrMaxConcurrentRequests = _TmnxOamTrMaxConcurrentRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 2),
    _TmnxOamTrMaxConcurrentRequests_Type()
)
tmnxOamTrMaxConcurrentRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamTrMaxConcurrentRequests.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamTrMaxConcurrentRequests.setUnits("requests")
_TmnxOamTrCtlTable_Object = MibTable
tmnxOamTrCtlTable = _TmnxOamTrCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3)
)
if mibBuilder.loadTexts:
    tmnxOamTrCtlTable.setStatus("current")
_TmnxOamTrCtlEntry_Object = MibTableRow
tmnxOamTrCtlEntry = _TmnxOamTrCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1)
)
tmnxOamTrCtlEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamTrCtlEntry.setStatus("current")


class _TmnxOamTrCtlOwnerIndex_Type(SnmpAdminString):
    """Custom type tmnxOamTrCtlOwnerIndex based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TmnxOamTrCtlOwnerIndex_Type.__name__ = "SnmpAdminString"
_TmnxOamTrCtlOwnerIndex_Object = MibTableColumn
tmnxOamTrCtlOwnerIndex = _TmnxOamTrCtlOwnerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 1),
    _TmnxOamTrCtlOwnerIndex_Type()
)
tmnxOamTrCtlOwnerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamTrCtlOwnerIndex.setStatus("current")


class _TmnxOamTrCtlTestIndex_Type(SnmpAdminString):
    """Custom type tmnxOamTrCtlTestIndex based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TmnxOamTrCtlTestIndex_Type.__name__ = "SnmpAdminString"
_TmnxOamTrCtlTestIndex_Object = MibTableColumn
tmnxOamTrCtlTestIndex = _TmnxOamTrCtlTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 2),
    _TmnxOamTrCtlTestIndex_Type()
)
tmnxOamTrCtlTestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamTrCtlTestIndex.setStatus("current")
_TmnxOamTrCtlRowStatus_Type = RowStatus
_TmnxOamTrCtlRowStatus_Object = MibTableColumn
tmnxOamTrCtlRowStatus = _TmnxOamTrCtlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 3),
    _TmnxOamTrCtlRowStatus_Type()
)
tmnxOamTrCtlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamTrCtlRowStatus.setStatus("current")


class _TmnxOamTrCtlStorageType_Type(StorageType):
    """Custom type tmnxOamTrCtlStorageType based on StorageType"""
    defaultValue = 2


_TmnxOamTrCtlStorageType_Type.__name__ = "StorageType"
_TmnxOamTrCtlStorageType_Object = MibTableColumn
tmnxOamTrCtlStorageType = _TmnxOamTrCtlStorageType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 4),
    _TmnxOamTrCtlStorageType_Type()
)
tmnxOamTrCtlStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamTrCtlStorageType.setStatus("obsolete")


class _TmnxOamTrCtlDescr_Type(SnmpAdminString):
    """Custom type tmnxOamTrCtlDescr based on SnmpAdminString"""
    defaultHexValue = "00"


_TmnxOamTrCtlDescr_Type.__name__ = "SnmpAdminString"
_TmnxOamTrCtlDescr_Object = MibTableColumn
tmnxOamTrCtlDescr = _TmnxOamTrCtlDescr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 5),
    _TmnxOamTrCtlDescr_Type()
)
tmnxOamTrCtlDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamTrCtlDescr.setStatus("obsolete")


class _TmnxOamTrCtlTestMode_Type(Integer32):
    """Custom type tmnxOamTrCtlTestMode based on Integer32"""
    defaultValue = 0

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
              10)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("macTraceRoute", 1),
          ("lspTraceRoute", 2),
          ("vprnTraceRoute", 3),
          ("mcastTraceRoute", 4),
          ("icmpTraceRoute", 5),
          ("ldpTreeTrace", 6),
          ("vccvTraceRoute", 7),
          ("p2mpLspTrace", 8),
          ("ethCfmLinkTrace", 9),
          ("bierTrace", 10))
    )


_TmnxOamTrCtlTestMode_Type.__name__ = "Integer32"
_TmnxOamTrCtlTestMode_Object = MibTableColumn
tmnxOamTrCtlTestMode = _TmnxOamTrCtlTestMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 6),
    _TmnxOamTrCtlTestMode_Type()
)
tmnxOamTrCtlTestMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamTrCtlTestMode.setStatus("current")


class _TmnxOamTrCtlAdminStatus_Type(TmnxEnabledDisabledAdminState):
    """Custom type tmnxOamTrCtlAdminStatus based on TmnxEnabledDisabledAdminState"""
    defaultValue = 2


_TmnxOamTrCtlAdminStatus_Type.__name__ = "TmnxEnabledDisabledAdminState"
_TmnxOamTrCtlAdminStatus_Object = MibTableColumn
tmnxOamTrCtlAdminStatus = _TmnxOamTrCtlAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 7),
    _TmnxOamTrCtlAdminStatus_Type()
)
tmnxOamTrCtlAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamTrCtlAdminStatus.setStatus("current")


class _TmnxOamTrCtlFcName_Type(TFCName):
    """Custom type tmnxOamTrCtlFcName based on TFCName"""
    defaultValue = OctetString("be")


_TmnxOamTrCtlFcName_Type.__name__ = "TFCName"
_TmnxOamTrCtlFcName_Object = MibTableColumn
tmnxOamTrCtlFcName = _TmnxOamTrCtlFcName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 8),
    _TmnxOamTrCtlFcName_Type()
)
tmnxOamTrCtlFcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamTrCtlFcName.setStatus("current")


class _TmnxOamTrCtlProfile_Type(TProfile):
    """Custom type tmnxOamTrCtlProfile based on TProfile"""
    defaultValue = 2


_TmnxOamTrCtlProfile_Type.__name__ = "TProfile"
_TmnxOamTrCtlProfile_Object = MibTableColumn
tmnxOamTrCtlProfile = _TmnxOamTrCtlProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 9),
    _TmnxOamTrCtlProfile_Type()
)
tmnxOamTrCtlProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamTrCtlProfile.setStatus("current")


class _TmnxOamTrCtlTargetIpAddress_Type(IpAddress):
    """Custom type tmnxOamTrCtlTargetIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_TmnxOamTrCtlTargetIpAddress_Type.__name__ = "IpAddress"
_TmnxOamTrCtlTargetIpAddress_Object = MibTableColumn
tmnxOamTrCtlTargetIpAddress = _TmnxOamTrCtlTargetIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 10),
    _TmnxOamTrCtlTargetIpAddress_Type()
)
tmnxOamTrCtlTargetIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamTrCtlTargetIpAddress.setStatus("obsolete")


class _TmnxOamTrCtlServiceId_Type(TmnxServId):
    """Custom type tmnxOamTrCtlServiceId based on TmnxServId"""
    defaultValue = 0

    subtypeSpec = TmnxServId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TmnxOamTrCtlServiceId_Type.__name__ = "TmnxServId"
_TmnxOamTrCtlServiceId_Object = MibTableColumn
tmnxOamTrCtlServiceId = _TmnxOamTrCtlServiceId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 11),
    _TmnxOamTrCtlServiceId_Type()
)
tmnxOamTrCtlServiceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamTrCtlServiceId.setStatus("current")


class _TmnxOamTrCtlDataSize_Type(Unsigned32):
    """Custom type tmnxOamTrCtlDataSize based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9786),
    )


_TmnxOamTrCtlDataSize_Type.__name__ = "Unsigned32"
_TmnxOamTrCtlDataSize_Object = MibTableColumn
tmnxOamTrCtlDataSize = _TmnxOamTrCtlDataSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 12),
    _TmnxOamTrCtlDataSize_Type()
)
tmnxOamTrCtlDataSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamTrCtlDataSize.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamTrCtlDataSize.setUnits("octets")


class _TmnxOamTrCtlTimeOut_Type(Unsigned32):
    """Custom type tmnxOamTrCtlTimeOut based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TmnxOamTrCtlTimeOut_Type.__name__ = "Unsigned32"
_TmnxOamTrCtlTimeOut_Object = MibTableColumn
tmnxOamTrCtlTimeOut = _TmnxOamTrCtlTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 13),
    _TmnxOamTrCtlTimeOut_Type()
)
tmnxOamTrCtlTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamTrCtlTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamTrCtlTimeOut.setUnits("seconds")


class _TmnxOamTrCtlProbesPerHop_Type(Unsigned32):
    """Custom type tmnxOamTrCtlProbesPerHop based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TmnxOamTrCtlProbesPerHop_Type.__name__ = "Unsigned32"
_TmnxOamTrCtlProbesPerHop_Object = MibTableColumn
tmnxOamTrCtlProbesPerHop = _TmnxOamTrCtlProbesPerHop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 14),
    _TmnxOamTrCtlProbesPerHop_Type()
)
tmnxOamTrCtlProbesPerHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamTrCtlProbesPerHop.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamTrCtlProbesPerHop.setUnits("probes")


class _TmnxOamTrCtlMaxTtl_Type(Unsigned32):
    """Custom type tmnxOamTrCtlMaxTtl based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TmnxOamTrCtlMaxTtl_Type.__name__ = "Unsigned32"
_TmnxOamTrCtlMaxTtl_Object = MibTableColumn
tmnxOamTrCtlMaxTtl = _TmnxOamTrCtlMaxTtl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 15),
    _TmnxOamTrCtlMaxTtl_Type()
)
tmnxOamTrCtlMaxTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamTrCtlMaxTtl.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamTrCtlMaxTtl.setUnits("time-to-live value")


class _TmnxOamTrCtlInitialTtl_Type(Unsigned32):
    """Custom type tmnxOamTrCtlInitialTtl based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TmnxOamTrCtlInitialTtl_Type.__name__ = "Unsigned32"
_TmnxOamTrCtlInitialTtl_Object = MibTableColumn
tmnxOamTrCtlInitialTtl = _TmnxOamTrCtlInitialTtl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 16),
    _TmnxOamTrCtlInitialTtl_Type()
)
tmnxOamTrCtlInitialTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamTrCtlInitialTtl.setStatus("current")


class _TmnxOamTrCtlDSField_Type(Unsigned32):
    """Custom type tmnxOamTrCtlDSField based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxOamTrCtlDSField_Type.__name__ = "Unsigned32"
_TmnxOamTrCtlDSField_Object = MibTableColumn
tmnxOamTrCtlDSField = _TmnxOamTrCtlDSField_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 17),
    _TmnxOamTrCtlDSField_Type()
)
tmnxOamTrCtlDSField.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamTrCtlDSField.setStatus("current")


class _TmnxOamTrCtlMaxFailures_Type(Unsigned32):
    """Custom type tmnxOamTrCtlMaxFailures based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TmnxOamTrCtlMaxFailures_Type.__name__ = "Unsigned32"
_TmnxOamTrCtlMaxFailures_Object = MibTableColumn
tmnxOamTrCtlMaxFailures = _TmnxOamTrCtlMaxFailures_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 18),
    _TmnxOamTrCtlMaxFailures_Type()
)
tmnxOamTrCtlMaxFailures.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamTrCtlMaxFailures.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamTrCtlMaxFailures.setUnits("timeouts")


class _TmnxOamTrCtlInterval_Type(Unsigned32):
    """Custom type tmnxOamTrCtlInterval based on Unsigned32"""
    defaultValue = 1


_TmnxOamTrCtlInterval_Type.__name__ = "Unsigned32"
_TmnxOamTrCtlInterval_Object = MibTableColumn
tmnxOamTrCtlInterval = _TmnxOamTrCtlInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 19),
    _TmnxOamTrCtlInterval_Type()
)
tmnxOamTrCtlInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamTrCtlInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamTrCtlInterval.setUnits("seconds")


class _TmnxOamTrCtlMaxRows_Type(Unsigned32):
    """Custom type tmnxOamTrCtlMaxRows based on Unsigned32"""
    defaultValue = 300


_TmnxOamTrCtlMaxRows_Type.__name__ = "Unsigned32"
_TmnxOamTrCtlMaxRows_Object = MibTableColumn
tmnxOamTrCtlMaxRows = _TmnxOamTrCtlMaxRows_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 20),
    _TmnxOamTrCtlMaxRows_Type()
)
tmnxOamTrCtlMaxRows.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamTrCtlMaxRows.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxOamTrCtlMaxRows.setUnits("rows")


class _TmnxOamTrCtlTrapGeneration_Type(Bits):
    """Custom type tmnxOamTrCtlTrapGeneration based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("pathChange", 0),
          ("testFailure", 1),
          ("testCompletion", 2))
    )

_TmnxOamTrCtlTrapGeneration_Type.__name__ = "Bits"
_TmnxOamTrCtlTrapGeneration_Object = MibTableColumn
tmnxOamTrCtlTrapGeneration = _TmnxOamTrCtlTrapGeneration_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 21),
    _TmnxOamTrCtlTrapGeneration_Type()
)
tmnxOamTrCtlTrapGeneration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamTrCtlTrapGeneration.setStatus("current")


class _TmnxOamTrCtlCreateHopsEntries_Type(TruthValue):
    """Custom type tmnxOamTrCtlCreateHopsEntries based on TruthValue"""
    defaultValue = 2


_TmnxOamTrCtlCreateHopsEntries_Type.__name__ = "TruthValue"
_TmnxOamTrCtlCreateHopsEntries_Object = MibTableColumn
tmnxOamTrCtlCreateHopsEntries = _TmnxOamTrCtlCreateHopsEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 22),
    _TmnxOamTrCtlCreateHopsEntries_Type()
)
tmnxOamTrCtlCreateHopsEntries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamTrCtlCreateHopsEntries.setStatus("obsolete")


class _TmnxOamTrCtlSAA_Type(TruthValue):
    """Custom type tmnxOamTrCtlSAA based on TruthValue"""
    defaultValue = 2


_TmnxOamTrCtlSAA_Type.__name__ = "TruthValue"
_TmnxOamTrCtlSAA_Object = MibTableColumn
tmnxOamTrCtlSAA = _TmnxOamTrCtlSAA_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 23),
    _TmnxOamTrCtlSAA_Type()
)
tmnxOamTrCtlSAA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamTrCtlSAA.setStatus("current")
_TmnxOamTrCtlRuns_Type = Counter32
_TmnxOamTrCtlRuns_Object = MibTableColumn
tmnxOamTrCtlRuns = _TmnxOamTrCtlRuns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 24),
    _TmnxOamTrCtlRuns_Type()
)
tmnxOamTrCtlRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrCtlRuns.setStatus("current")
_TmnxOamTrCtlFailures_Type = Counter32
_TmnxOamTrCtlFailures_Object = MibTableColumn
tmnxOamTrCtlFailures = _TmnxOamTrCtlFailures_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 25),
    _TmnxOamTrCtlFailures_Type()
)
tmnxOamTrCtlFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrCtlFailures.setStatus("current")
_TmnxOamTrCtlLastRunResult_Type = TmnxOamTestResult
_TmnxOamTrCtlLastRunResult_Object = MibTableColumn
tmnxOamTrCtlLastRunResult = _TmnxOamTrCtlLastRunResult_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 26),
    _TmnxOamTrCtlLastRunResult_Type()
)
tmnxOamTrCtlLastRunResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrCtlLastRunResult.setStatus("current")
_TmnxOamTrCtlLastChanged_Type = TimeStamp
_TmnxOamTrCtlLastChanged_Object = MibTableColumn
tmnxOamTrCtlLastChanged = _TmnxOamTrCtlLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 27),
    _TmnxOamTrCtlLastChanged_Type()
)
tmnxOamTrCtlLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrCtlLastChanged.setStatus("current")


class _TmnxOamTrCtlVRtrID_Type(TmnxVRtrIDOrZero):
    """Custom type tmnxOamTrCtlVRtrID based on TmnxVRtrIDOrZero"""
    defaultValue = 1


_TmnxOamTrCtlVRtrID_Type.__name__ = "TmnxVRtrIDOrZero"
_TmnxOamTrCtlVRtrID_Object = MibTableColumn
tmnxOamTrCtlVRtrID = _TmnxOamTrCtlVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 28),
    _TmnxOamTrCtlVRtrID_Type()
)
tmnxOamTrCtlVRtrID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamTrCtlVRtrID.setStatus("current")


class _TmnxOamTrCtlTgtAddrType_Type(InetAddressType):
    """Custom type tmnxOamTrCtlTgtAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxOamTrCtlTgtAddrType_Type.__name__ = "InetAddressType"
_TmnxOamTrCtlTgtAddrType_Object = MibTableColumn
tmnxOamTrCtlTgtAddrType = _TmnxOamTrCtlTgtAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 29),
    _TmnxOamTrCtlTgtAddrType_Type()
)
tmnxOamTrCtlTgtAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamTrCtlTgtAddrType.setStatus("current")


class _TmnxOamTrCtlTgtAddress_Type(InetAddress):
    """Custom type tmnxOamTrCtlTgtAddress based on InetAddress"""
    defaultHexValue = ""


_TmnxOamTrCtlTgtAddress_Type.__name__ = "InetAddress"
_TmnxOamTrCtlTgtAddress_Object = MibTableColumn
tmnxOamTrCtlTgtAddress = _TmnxOamTrCtlTgtAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 30),
    _TmnxOamTrCtlTgtAddress_Type()
)
tmnxOamTrCtlTgtAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamTrCtlTgtAddress.setStatus("current")


class _TmnxOamTrCtlSrcAddrType_Type(InetAddressType):
    """Custom type tmnxOamTrCtlSrcAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxOamTrCtlSrcAddrType_Type.__name__ = "InetAddressType"
_TmnxOamTrCtlSrcAddrType_Object = MibTableColumn
tmnxOamTrCtlSrcAddrType = _TmnxOamTrCtlSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 31),
    _TmnxOamTrCtlSrcAddrType_Type()
)
tmnxOamTrCtlSrcAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamTrCtlSrcAddrType.setStatus("current")


class _TmnxOamTrCtlSrcAddress_Type(InetAddress):
    """Custom type tmnxOamTrCtlSrcAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamTrCtlSrcAddress_Type.__name__ = "InetAddress"
_TmnxOamTrCtlSrcAddress_Object = MibTableColumn
tmnxOamTrCtlSrcAddress = _TmnxOamTrCtlSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 32),
    _TmnxOamTrCtlSrcAddress_Type()
)
tmnxOamTrCtlSrcAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamTrCtlSrcAddress.setStatus("current")


class _TmnxOamTrCtlWaitMilliSec_Type(Unsigned32):
    """Custom type tmnxOamTrCtlWaitMilliSec based on Unsigned32"""
    defaultValue = 5000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 60000),
    )


_TmnxOamTrCtlWaitMilliSec_Type.__name__ = "Unsigned32"
_TmnxOamTrCtlWaitMilliSec_Object = MibTableColumn
tmnxOamTrCtlWaitMilliSec = _TmnxOamTrCtlWaitMilliSec_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 33),
    _TmnxOamTrCtlWaitMilliSec_Type()
)
tmnxOamTrCtlWaitMilliSec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamTrCtlWaitMilliSec.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamTrCtlWaitMilliSec.setUnits("milliseconds")


class _TmnxOamTrCtlRouterInstanceName_Type(TLNamedItemOrEmpty):
    """Custom type tmnxOamTrCtlRouterInstanceName based on TLNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOamTrCtlRouterInstanceName_Type.__name__ = "TLNamedItemOrEmpty"
_TmnxOamTrCtlRouterInstanceName_Object = MibTableColumn
tmnxOamTrCtlRouterInstanceName = _TmnxOamTrCtlRouterInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 34),
    _TmnxOamTrCtlRouterInstanceName_Type()
)
tmnxOamTrCtlRouterInstanceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamTrCtlRouterInstanceName.setStatus("current")
_TmnxOamTrResultsTable_Object = MibTable
tmnxOamTrResultsTable = _TmnxOamTrResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 4)
)
if mibBuilder.loadTexts:
    tmnxOamTrResultsTable.setStatus("current")
_TmnxOamTrResultsEntry_Object = MibTableRow
tmnxOamTrResultsEntry = _TmnxOamTrResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 4, 1)
)
tmnxOamTrResultsEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsTestRunIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamTrResultsEntry.setStatus("current")


class _TmnxOamTrResultsOperStatus_Type(Integer32):
    """Custom type tmnxOamTrResultsOperStatus based on Integer32"""
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


_TmnxOamTrResultsOperStatus_Type.__name__ = "Integer32"
_TmnxOamTrResultsOperStatus_Object = MibTableColumn
tmnxOamTrResultsOperStatus = _TmnxOamTrResultsOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 4, 1, 1),
    _TmnxOamTrResultsOperStatus_Type()
)
tmnxOamTrResultsOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrResultsOperStatus.setStatus("current")
_TmnxOamTrResultsCurHopCount_Type = Gauge32
_TmnxOamTrResultsCurHopCount_Object = MibTableColumn
tmnxOamTrResultsCurHopCount = _TmnxOamTrResultsCurHopCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 4, 1, 2),
    _TmnxOamTrResultsCurHopCount_Type()
)
tmnxOamTrResultsCurHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrResultsCurHopCount.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamTrResultsCurHopCount.setUnits("hops")
_TmnxOamTrResultsCurProbeCount_Type = Gauge32
_TmnxOamTrResultsCurProbeCount_Object = MibTableColumn
tmnxOamTrResultsCurProbeCount = _TmnxOamTrResultsCurProbeCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 4, 1, 3),
    _TmnxOamTrResultsCurProbeCount_Type()
)
tmnxOamTrResultsCurProbeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrResultsCurProbeCount.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamTrResultsCurProbeCount.setUnits("probes")
_TmnxOamTrResultsIpTgtAddr_Type = IpAddress
_TmnxOamTrResultsIpTgtAddr_Object = MibTableColumn
tmnxOamTrResultsIpTgtAddr = _TmnxOamTrResultsIpTgtAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 4, 1, 4),
    _TmnxOamTrResultsIpTgtAddr_Type()
)
tmnxOamTrResultsIpTgtAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrResultsIpTgtAddr.setStatus("obsolete")
_TmnxOamTrResultsTestAttempts_Type = Unsigned32
_TmnxOamTrResultsTestAttempts_Object = MibTableColumn
tmnxOamTrResultsTestAttempts = _TmnxOamTrResultsTestAttempts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 4, 1, 5),
    _TmnxOamTrResultsTestAttempts_Type()
)
tmnxOamTrResultsTestAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrResultsTestAttempts.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxOamTrResultsTestAttempts.setUnits("tests")
_TmnxOamTrResultsTestSuccesses_Type = Unsigned32
_TmnxOamTrResultsTestSuccesses_Object = MibTableColumn
tmnxOamTrResultsTestSuccesses = _TmnxOamTrResultsTestSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 4, 1, 6),
    _TmnxOamTrResultsTestSuccesses_Type()
)
tmnxOamTrResultsTestSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrResultsTestSuccesses.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxOamTrResultsTestSuccesses.setUnits("tests")
_TmnxOamTrResultsLastGoodPath_Type = DateAndTime
_TmnxOamTrResultsLastGoodPath_Object = MibTableColumn
tmnxOamTrResultsLastGoodPath = _TmnxOamTrResultsLastGoodPath_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 4, 1, 7),
    _TmnxOamTrResultsLastGoodPath_Type()
)
tmnxOamTrResultsLastGoodPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrResultsLastGoodPath.setStatus("current")


class _TmnxOamTrResultsTestRunIndex_Type(Unsigned32):
    """Custom type tmnxOamTrResultsTestRunIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxOamTrResultsTestRunIndex_Type.__name__ = "Unsigned32"
_TmnxOamTrResultsTestRunIndex_Object = MibTableColumn
tmnxOamTrResultsTestRunIndex = _TmnxOamTrResultsTestRunIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 4, 1, 8),
    _TmnxOamTrResultsTestRunIndex_Type()
)
tmnxOamTrResultsTestRunIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamTrResultsTestRunIndex.setStatus("current")
_TmnxOamTrResultsTgtAddrType_Type = InetAddressType
_TmnxOamTrResultsTgtAddrType_Object = MibTableColumn
tmnxOamTrResultsTgtAddrType = _TmnxOamTrResultsTgtAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 4, 1, 9),
    _TmnxOamTrResultsTgtAddrType_Type()
)
tmnxOamTrResultsTgtAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrResultsTgtAddrType.setStatus("current")


class _TmnxOamTrResultsTgtAddress_Type(InetAddress):
    """Custom type tmnxOamTrResultsTgtAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamTrResultsTgtAddress_Type.__name__ = "InetAddress"
_TmnxOamTrResultsTgtAddress_Object = MibTableColumn
tmnxOamTrResultsTgtAddress = _TmnxOamTrResultsTgtAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 4, 1, 10),
    _TmnxOamTrResultsTgtAddress_Type()
)
tmnxOamTrResultsTgtAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrResultsTgtAddress.setStatus("current")
_TmnxOamTrResultsTestRunResult_Type = TmnxOamTestResult
_TmnxOamTrResultsTestRunResult_Object = MibTableColumn
tmnxOamTrResultsTestRunResult = _TmnxOamTrResultsTestRunResult_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 4, 1, 11),
    _TmnxOamTrResultsTestRunResult_Type()
)
tmnxOamTrResultsTestRunResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrResultsTestRunResult.setStatus("current")
_TmnxOamTrProbeHistoryTable_Object = MibTable
tmnxOamTrProbeHistoryTable = _TmnxOamTrProbeHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 5)
)
if mibBuilder.loadTexts:
    tmnxOamTrProbeHistoryTable.setStatus("current")
_TmnxOamTrProbeHistoryEntry_Object = MibTableRow
tmnxOamTrProbeHistoryEntry = _TmnxOamTrProbeHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 5, 1)
)
tmnxOamTrProbeHistoryEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsTestRunIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryHopIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryProbeIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamTrProbeHistoryEntry.setStatus("current")


class _TmnxOamTrProbeHistoryIndex_Type(Unsigned32):
    """Custom type tmnxOamTrProbeHistoryIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxOamTrProbeHistoryIndex_Type.__name__ = "Unsigned32"
_TmnxOamTrProbeHistoryIndex_Object = MibTableColumn
tmnxOamTrProbeHistoryIndex = _TmnxOamTrProbeHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 5, 1, 1),
    _TmnxOamTrProbeHistoryIndex_Type()
)
tmnxOamTrProbeHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamTrProbeHistoryIndex.setStatus("current")


class _TmnxOamTrProbeHistoryHopIndex_Type(Unsigned32):
    """Custom type tmnxOamTrProbeHistoryHopIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TmnxOamTrProbeHistoryHopIndex_Type.__name__ = "Unsigned32"
_TmnxOamTrProbeHistoryHopIndex_Object = MibTableColumn
tmnxOamTrProbeHistoryHopIndex = _TmnxOamTrProbeHistoryHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 5, 1, 2),
    _TmnxOamTrProbeHistoryHopIndex_Type()
)
tmnxOamTrProbeHistoryHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamTrProbeHistoryHopIndex.setStatus("current")


class _TmnxOamTrProbeHistoryProbeIndex_Type(Unsigned32):
    """Custom type tmnxOamTrProbeHistoryProbeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TmnxOamTrProbeHistoryProbeIndex_Type.__name__ = "Unsigned32"
_TmnxOamTrProbeHistoryProbeIndex_Object = MibTableColumn
tmnxOamTrProbeHistoryProbeIndex = _TmnxOamTrProbeHistoryProbeIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 5, 1, 3),
    _TmnxOamTrProbeHistoryProbeIndex_Type()
)
tmnxOamTrProbeHistoryProbeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamTrProbeHistoryProbeIndex.setStatus("current")
_TmnxOamTrProbeHistoryIpAddr_Type = IpAddress
_TmnxOamTrProbeHistoryIpAddr_Object = MibTableColumn
tmnxOamTrProbeHistoryIpAddr = _TmnxOamTrProbeHistoryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 5, 1, 4),
    _TmnxOamTrProbeHistoryIpAddr_Type()
)
tmnxOamTrProbeHistoryIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrProbeHistoryIpAddr.setStatus("obsolete")
_TmnxOamTrProbeHistoryResponse_Type = Unsigned32
_TmnxOamTrProbeHistoryResponse_Object = MibTableColumn
tmnxOamTrProbeHistoryResponse = _TmnxOamTrProbeHistoryResponse_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 5, 1, 5),
    _TmnxOamTrProbeHistoryResponse_Type()
)
tmnxOamTrProbeHistoryResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrProbeHistoryResponse.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamTrProbeHistoryResponse.setUnits("microseconds")
_TmnxOamTrProbeHistoryOneWayTime_Type = Integer32
_TmnxOamTrProbeHistoryOneWayTime_Object = MibTableColumn
tmnxOamTrProbeHistoryOneWayTime = _TmnxOamTrProbeHistoryOneWayTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 5, 1, 6),
    _TmnxOamTrProbeHistoryOneWayTime_Type()
)
tmnxOamTrProbeHistoryOneWayTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrProbeHistoryOneWayTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamTrProbeHistoryOneWayTime.setUnits("microseconds")
_TmnxOamTrProbeHistoryStatus_Type = TmnxOamResponseStatus
_TmnxOamTrProbeHistoryStatus_Object = MibTableColumn
tmnxOamTrProbeHistoryStatus = _TmnxOamTrProbeHistoryStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 5, 1, 7),
    _TmnxOamTrProbeHistoryStatus_Type()
)
tmnxOamTrProbeHistoryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrProbeHistoryStatus.setStatus("current")
_TmnxOamTrProbeHistoryLastRC_Type = Integer32
_TmnxOamTrProbeHistoryLastRC_Object = MibTableColumn
tmnxOamTrProbeHistoryLastRC = _TmnxOamTrProbeHistoryLastRC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 5, 1, 8),
    _TmnxOamTrProbeHistoryLastRC_Type()
)
tmnxOamTrProbeHistoryLastRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrProbeHistoryLastRC.setStatus("current")
_TmnxOamTrProbeHistoryTime_Type = DateAndTime
_TmnxOamTrProbeHistoryTime_Object = MibTableColumn
tmnxOamTrProbeHistoryTime = _TmnxOamTrProbeHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 5, 1, 9),
    _TmnxOamTrProbeHistoryTime_Type()
)
tmnxOamTrProbeHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrProbeHistoryTime.setStatus("current")
_TmnxOamTrProbeHistoryResponsePlane_Type = TmnxOamTestResponsePlane
_TmnxOamTrProbeHistoryResponsePlane_Object = MibTableColumn
tmnxOamTrProbeHistoryResponsePlane = _TmnxOamTrProbeHistoryResponsePlane_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 5, 1, 10),
    _TmnxOamTrProbeHistoryResponsePlane_Type()
)
tmnxOamTrProbeHistoryResponsePlane.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrProbeHistoryResponsePlane.setStatus("current")
_TmnxOamTrProbeHistoryAddressType_Type = TmnxOamAddressType
_TmnxOamTrProbeHistoryAddressType_Object = MibTableColumn
tmnxOamTrProbeHistoryAddressType = _TmnxOamTrProbeHistoryAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 5, 1, 11),
    _TmnxOamTrProbeHistoryAddressType_Type()
)
tmnxOamTrProbeHistoryAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrProbeHistoryAddressType.setStatus("current")
_TmnxOamTrProbeHistorySapId_Type = TmnxStrSapId
_TmnxOamTrProbeHistorySapId_Object = MibTableColumn
tmnxOamTrProbeHistorySapId = _TmnxOamTrProbeHistorySapId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 5, 1, 12),
    _TmnxOamTrProbeHistorySapId_Type()
)
tmnxOamTrProbeHistorySapId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrProbeHistorySapId.setStatus("current")
_TmnxOamTrProbeHistoryVersion_Type = Unsigned32
_TmnxOamTrProbeHistoryVersion_Object = MibTableColumn
tmnxOamTrProbeHistoryVersion = _TmnxOamTrProbeHistoryVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 5, 1, 14),
    _TmnxOamTrProbeHistoryVersion_Type()
)
tmnxOamTrProbeHistoryVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrProbeHistoryVersion.setStatus("current")
_TmnxOamTrProbeHistoryRouterID_Type = RouterID
_TmnxOamTrProbeHistoryRouterID_Object = MibTableColumn
tmnxOamTrProbeHistoryRouterID = _TmnxOamTrProbeHistoryRouterID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 5, 1, 15),
    _TmnxOamTrProbeHistoryRouterID_Type()
)
tmnxOamTrProbeHistoryRouterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrProbeHistoryRouterID.setStatus("obsolete")
_TmnxOamTrProbeHistoryIfIndex_Type = InterfaceIndexOrZero
_TmnxOamTrProbeHistoryIfIndex_Object = MibTableColumn
tmnxOamTrProbeHistoryIfIndex = _TmnxOamTrProbeHistoryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 5, 1, 16),
    _TmnxOamTrProbeHistoryIfIndex_Type()
)
tmnxOamTrProbeHistoryIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrProbeHistoryIfIndex.setStatus("current")
_TmnxOamTrProbeHistoryDataLen_Type = Unsigned32
_TmnxOamTrProbeHistoryDataLen_Object = MibTableColumn
tmnxOamTrProbeHistoryDataLen = _TmnxOamTrProbeHistoryDataLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 5, 1, 17),
    _TmnxOamTrProbeHistoryDataLen_Type()
)
tmnxOamTrProbeHistoryDataLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrProbeHistoryDataLen.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamTrProbeHistoryDataLen.setUnits("octets")
_TmnxOamTrProbeHistorySize_Type = Unsigned32
_TmnxOamTrProbeHistorySize_Object = MibTableColumn
tmnxOamTrProbeHistorySize = _TmnxOamTrProbeHistorySize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 5, 1, 18),
    _TmnxOamTrProbeHistorySize_Type()
)
tmnxOamTrProbeHistorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrProbeHistorySize.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamTrProbeHistorySize.setUnits("octets")
_TmnxOamTrProbeHistoryInOneWayTime_Type = Integer32
_TmnxOamTrProbeHistoryInOneWayTime_Object = MibTableColumn
tmnxOamTrProbeHistoryInOneWayTime = _TmnxOamTrProbeHistoryInOneWayTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 5, 1, 19),
    _TmnxOamTrProbeHistoryInOneWayTime_Type()
)
tmnxOamTrProbeHistoryInOneWayTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrProbeHistoryInOneWayTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamTrProbeHistoryInOneWayTime.setUnits("microseconds")
_TmnxOamTrProbeHistoryAddrType_Type = InetAddressType
_TmnxOamTrProbeHistoryAddrType_Object = MibTableColumn
tmnxOamTrProbeHistoryAddrType = _TmnxOamTrProbeHistoryAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 5, 1, 20),
    _TmnxOamTrProbeHistoryAddrType_Type()
)
tmnxOamTrProbeHistoryAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrProbeHistoryAddrType.setStatus("current")


class _TmnxOamTrProbeHistoryAddress_Type(InetAddress):
    """Custom type tmnxOamTrProbeHistoryAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamTrProbeHistoryAddress_Type.__name__ = "InetAddress"
_TmnxOamTrProbeHistoryAddress_Object = MibTableColumn
tmnxOamTrProbeHistoryAddress = _TmnxOamTrProbeHistoryAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 5, 1, 21),
    _TmnxOamTrProbeHistoryAddress_Type()
)
tmnxOamTrProbeHistoryAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrProbeHistoryAddress.setStatus("current")
_TmnxOamTrProbeHistorySrcGlobalId_Type = TmnxMplsTpGlobalID
_TmnxOamTrProbeHistorySrcGlobalId_Object = MibTableColumn
tmnxOamTrProbeHistorySrcGlobalId = _TmnxOamTrProbeHistorySrcGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 5, 1, 22),
    _TmnxOamTrProbeHistorySrcGlobalId_Type()
)
tmnxOamTrProbeHistorySrcGlobalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrProbeHistorySrcGlobalId.setStatus("current")
_TmnxOamTrProbeHistorySrcNodeId_Type = TmnxMplsTpNodeID
_TmnxOamTrProbeHistorySrcNodeId_Object = MibTableColumn
tmnxOamTrProbeHistorySrcNodeId = _TmnxOamTrProbeHistorySrcNodeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 5, 1, 23),
    _TmnxOamTrProbeHistorySrcNodeId_Type()
)
tmnxOamTrProbeHistorySrcNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrProbeHistorySrcNodeId.setStatus("current")
_TmnxOamTrProbeHistorySdpBindId_Type = TNamedItemOrEmpty
_TmnxOamTrProbeHistorySdpBindId_Object = MibTableColumn
tmnxOamTrProbeHistorySdpBindId = _TmnxOamTrProbeHistorySdpBindId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 5, 1, 24),
    _TmnxOamTrProbeHistorySdpBindId_Type()
)
tmnxOamTrProbeHistorySdpBindId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrProbeHistorySdpBindId.setStatus("current")
_TmnxOamTrProbeHistoryRtrnSubcode_Type = Unsigned32
_TmnxOamTrProbeHistoryRtrnSubcode_Object = MibTableColumn
tmnxOamTrProbeHistoryRtrnSubcode = _TmnxOamTrProbeHistoryRtrnSubcode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 5, 1, 25),
    _TmnxOamTrProbeHistoryRtrnSubcode_Type()
)
tmnxOamTrProbeHistoryRtrnSubcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrProbeHistoryRtrnSubcode.setStatus("current")
_TmnxOamTrProbeHistoryNtwrkIfName_Type = TNamedItemOrEmpty
_TmnxOamTrProbeHistoryNtwrkIfName_Object = MibTableColumn
tmnxOamTrProbeHistoryNtwrkIfName = _TmnxOamTrProbeHistoryNtwrkIfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 5, 1, 26),
    _TmnxOamTrProbeHistoryNtwrkIfName_Type()
)
tmnxOamTrProbeHistoryNtwrkIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrProbeHistoryNtwrkIfName.setStatus("current")
_TmnxOamTrHopsTable_Object = MibTable
tmnxOamTrHopsTable = _TmnxOamTrHopsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 6)
)
if mibBuilder.loadTexts:
    tmnxOamTrHopsTable.setStatus("current")
_TmnxOamTrHopsEntry_Object = MibTableRow
tmnxOamTrHopsEntry = _TmnxOamTrHopsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 6, 1)
)
tmnxOamTrHopsEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsTestRunIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsHopIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamTrHopsEntry.setStatus("current")
_TmnxOamTrHopsHopIndex_Type = Unsigned32
_TmnxOamTrHopsHopIndex_Object = MibTableColumn
tmnxOamTrHopsHopIndex = _TmnxOamTrHopsHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 6, 1, 1),
    _TmnxOamTrHopsHopIndex_Type()
)
tmnxOamTrHopsHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamTrHopsHopIndex.setStatus("current")
_TmnxOamTrHopsIpTgtAddress_Type = IpAddress
_TmnxOamTrHopsIpTgtAddress_Object = MibTableColumn
tmnxOamTrHopsIpTgtAddress = _TmnxOamTrHopsIpTgtAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 6, 1, 2),
    _TmnxOamTrHopsIpTgtAddress_Type()
)
tmnxOamTrHopsIpTgtAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrHopsIpTgtAddress.setStatus("obsolete")
_TmnxOamTrHopsMinRtt_Type = Unsigned32
_TmnxOamTrHopsMinRtt_Object = MibTableColumn
tmnxOamTrHopsMinRtt = _TmnxOamTrHopsMinRtt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 6, 1, 3),
    _TmnxOamTrHopsMinRtt_Type()
)
tmnxOamTrHopsMinRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrHopsMinRtt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamTrHopsMinRtt.setUnits("microseconds")
_TmnxOamTrHopsMaxRtt_Type = Unsigned32
_TmnxOamTrHopsMaxRtt_Object = MibTableColumn
tmnxOamTrHopsMaxRtt = _TmnxOamTrHopsMaxRtt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 6, 1, 4),
    _TmnxOamTrHopsMaxRtt_Type()
)
tmnxOamTrHopsMaxRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrHopsMaxRtt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamTrHopsMaxRtt.setUnits("microseconds")
_TmnxOamTrHopsAverageRtt_Type = Unsigned32
_TmnxOamTrHopsAverageRtt_Object = MibTableColumn
tmnxOamTrHopsAverageRtt = _TmnxOamTrHopsAverageRtt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 6, 1, 5),
    _TmnxOamTrHopsAverageRtt_Type()
)
tmnxOamTrHopsAverageRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrHopsAverageRtt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamTrHopsAverageRtt.setUnits("microseconds")
_TmnxOamTrHopsRttSumOfSquares_Type = Unsigned32
_TmnxOamTrHopsRttSumOfSquares_Object = MibTableColumn
tmnxOamTrHopsRttSumOfSquares = _TmnxOamTrHopsRttSumOfSquares_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 6, 1, 6),
    _TmnxOamTrHopsRttSumOfSquares_Type()
)
tmnxOamTrHopsRttSumOfSquares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrHopsRttSumOfSquares.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamTrHopsRttSumOfSquares.setUnits("microseconds squared")
_TmnxOamTrHopsMinTt_Type = Integer32
_TmnxOamTrHopsMinTt_Object = MibTableColumn
tmnxOamTrHopsMinTt = _TmnxOamTrHopsMinTt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 6, 1, 7),
    _TmnxOamTrHopsMinTt_Type()
)
tmnxOamTrHopsMinTt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrHopsMinTt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamTrHopsMinTt.setUnits("microseconds")
_TmnxOamTrHopsMaxTt_Type = Integer32
_TmnxOamTrHopsMaxTt_Object = MibTableColumn
tmnxOamTrHopsMaxTt = _TmnxOamTrHopsMaxTt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 6, 1, 8),
    _TmnxOamTrHopsMaxTt_Type()
)
tmnxOamTrHopsMaxTt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrHopsMaxTt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamTrHopsMaxTt.setUnits("microseconds")
_TmnxOamTrHopsAverageTt_Type = Integer32
_TmnxOamTrHopsAverageTt_Object = MibTableColumn
tmnxOamTrHopsAverageTt = _TmnxOamTrHopsAverageTt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 6, 1, 9),
    _TmnxOamTrHopsAverageTt_Type()
)
tmnxOamTrHopsAverageTt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrHopsAverageTt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamTrHopsAverageTt.setUnits("microseconds")
_TmnxOamTrHopsTtSumOfSquares_Type = Unsigned32
_TmnxOamTrHopsTtSumOfSquares_Object = MibTableColumn
tmnxOamTrHopsTtSumOfSquares = _TmnxOamTrHopsTtSumOfSquares_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 6, 1, 10),
    _TmnxOamTrHopsTtSumOfSquares_Type()
)
tmnxOamTrHopsTtSumOfSquares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrHopsTtSumOfSquares.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamTrHopsTtSumOfSquares.setUnits("microseconds squared")
_TmnxOamTrHopsSentProbes_Type = Unsigned32
_TmnxOamTrHopsSentProbes_Object = MibTableColumn
tmnxOamTrHopsSentProbes = _TmnxOamTrHopsSentProbes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 6, 1, 11),
    _TmnxOamTrHopsSentProbes_Type()
)
tmnxOamTrHopsSentProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrHopsSentProbes.setStatus("current")
_TmnxOamTrHopsProbeResponses_Type = Unsigned32
_TmnxOamTrHopsProbeResponses_Object = MibTableColumn
tmnxOamTrHopsProbeResponses = _TmnxOamTrHopsProbeResponses_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 6, 1, 12),
    _TmnxOamTrHopsProbeResponses_Type()
)
tmnxOamTrHopsProbeResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrHopsProbeResponses.setStatus("current")
_TmnxOamTrHopsLastGoodProbe_Type = DateAndTime
_TmnxOamTrHopsLastGoodProbe_Object = MibTableColumn
tmnxOamTrHopsLastGoodProbe = _TmnxOamTrHopsLastGoodProbe_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 6, 1, 13),
    _TmnxOamTrHopsLastGoodProbe_Type()
)
tmnxOamTrHopsLastGoodProbe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrHopsLastGoodProbe.setStatus("current")
_TmnxOamTrHopsMinInTt_Type = Integer32
_TmnxOamTrHopsMinInTt_Object = MibTableColumn
tmnxOamTrHopsMinInTt = _TmnxOamTrHopsMinInTt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 6, 1, 18),
    _TmnxOamTrHopsMinInTt_Type()
)
tmnxOamTrHopsMinInTt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrHopsMinInTt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamTrHopsMinInTt.setUnits("microseconds")
_TmnxOamTrHopsMaxInTt_Type = Integer32
_TmnxOamTrHopsMaxInTt_Object = MibTableColumn
tmnxOamTrHopsMaxInTt = _TmnxOamTrHopsMaxInTt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 6, 1, 19),
    _TmnxOamTrHopsMaxInTt_Type()
)
tmnxOamTrHopsMaxInTt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrHopsMaxInTt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamTrHopsMaxInTt.setUnits("microseconds")
_TmnxOamTrHopsAverageInTt_Type = Integer32
_TmnxOamTrHopsAverageInTt_Object = MibTableColumn
tmnxOamTrHopsAverageInTt = _TmnxOamTrHopsAverageInTt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 6, 1, 20),
    _TmnxOamTrHopsAverageInTt_Type()
)
tmnxOamTrHopsAverageInTt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrHopsAverageInTt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamTrHopsAverageInTt.setUnits("microseconds")
_TmnxOamTrHopsInTtSumOfSqrs_Type = Unsigned32
_TmnxOamTrHopsInTtSumOfSqrs_Object = MibTableColumn
tmnxOamTrHopsInTtSumOfSqrs = _TmnxOamTrHopsInTtSumOfSqrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 6, 1, 21),
    _TmnxOamTrHopsInTtSumOfSqrs_Type()
)
tmnxOamTrHopsInTtSumOfSqrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrHopsInTtSumOfSqrs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamTrHopsInTtSumOfSqrs.setUnits("microseconds squared")
_TmnxOamTrHopsOutJitter_Type = Integer32
_TmnxOamTrHopsOutJitter_Object = MibTableColumn
tmnxOamTrHopsOutJitter = _TmnxOamTrHopsOutJitter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 6, 1, 22),
    _TmnxOamTrHopsOutJitter_Type()
)
tmnxOamTrHopsOutJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrHopsOutJitter.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamTrHopsOutJitter.setUnits("microseconds")
_TmnxOamTrHopsInJitter_Type = Integer32
_TmnxOamTrHopsInJitter_Object = MibTableColumn
tmnxOamTrHopsInJitter = _TmnxOamTrHopsInJitter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 6, 1, 23),
    _TmnxOamTrHopsInJitter_Type()
)
tmnxOamTrHopsInJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrHopsInJitter.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamTrHopsInJitter.setUnits("microseconds")
_TmnxOamTrHopsRtJitter_Type = Integer32
_TmnxOamTrHopsRtJitter_Object = MibTableColumn
tmnxOamTrHopsRtJitter = _TmnxOamTrHopsRtJitter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 6, 1, 24),
    _TmnxOamTrHopsRtJitter_Type()
)
tmnxOamTrHopsRtJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrHopsRtJitter.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamTrHopsRtJitter.setUnits("microseconds")
_TmnxOamTrHopsProbeTimeouts_Type = Unsigned32
_TmnxOamTrHopsProbeTimeouts_Object = MibTableColumn
tmnxOamTrHopsProbeTimeouts = _TmnxOamTrHopsProbeTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 6, 1, 25),
    _TmnxOamTrHopsProbeTimeouts_Type()
)
tmnxOamTrHopsProbeTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrHopsProbeTimeouts.setStatus("current")
_TmnxOamTrHopsProbeFailures_Type = Unsigned32
_TmnxOamTrHopsProbeFailures_Object = MibTableColumn
tmnxOamTrHopsProbeFailures = _TmnxOamTrHopsProbeFailures_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 6, 1, 26),
    _TmnxOamTrHopsProbeFailures_Type()
)
tmnxOamTrHopsProbeFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrHopsProbeFailures.setStatus("current")
_TmnxOamTrHopsTgtAddrType_Type = InetAddressType
_TmnxOamTrHopsTgtAddrType_Object = MibTableColumn
tmnxOamTrHopsTgtAddrType = _TmnxOamTrHopsTgtAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 6, 1, 27),
    _TmnxOamTrHopsTgtAddrType_Type()
)
tmnxOamTrHopsTgtAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrHopsTgtAddrType.setStatus("current")


class _TmnxOamTrHopsTgtAddress_Type(InetAddress):
    """Custom type tmnxOamTrHopsTgtAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamTrHopsTgtAddress_Type.__name__ = "InetAddress"
_TmnxOamTrHopsTgtAddress_Object = MibTableColumn
tmnxOamTrHopsTgtAddress = _TmnxOamTrHopsTgtAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 6, 1, 28),
    _TmnxOamTrHopsTgtAddress_Type()
)
tmnxOamTrHopsTgtAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrHopsTgtAddress.setStatus("current")
_TmnxOamTrHopsRttOFSumSquares_Type = Counter32
_TmnxOamTrHopsRttOFSumSquares_Object = MibTableColumn
tmnxOamTrHopsRttOFSumSquares = _TmnxOamTrHopsRttOFSumSquares_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 6, 1, 29),
    _TmnxOamTrHopsRttOFSumSquares_Type()
)
tmnxOamTrHopsRttOFSumSquares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrHopsRttOFSumSquares.setStatus("current")
_TmnxOamTrHopsRttHCSumSquares_Type = Counter64
_TmnxOamTrHopsRttHCSumSquares_Object = MibTableColumn
tmnxOamTrHopsRttHCSumSquares = _TmnxOamTrHopsRttHCSumSquares_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 6, 1, 30),
    _TmnxOamTrHopsRttHCSumSquares_Type()
)
tmnxOamTrHopsRttHCSumSquares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrHopsRttHCSumSquares.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamTrHopsRttHCSumSquares.setUnits("microseconds squared")
_TmnxOamTrHopsTtOFSumSquares_Type = Counter32
_TmnxOamTrHopsTtOFSumSquares_Object = MibTableColumn
tmnxOamTrHopsTtOFSumSquares = _TmnxOamTrHopsTtOFSumSquares_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 6, 1, 31),
    _TmnxOamTrHopsTtOFSumSquares_Type()
)
tmnxOamTrHopsTtOFSumSquares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrHopsTtOFSumSquares.setStatus("current")
_TmnxOamTrHopsTtHCSumSquares_Type = Counter64
_TmnxOamTrHopsTtHCSumSquares_Object = MibTableColumn
tmnxOamTrHopsTtHCSumSquares = _TmnxOamTrHopsTtHCSumSquares_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 6, 1, 32),
    _TmnxOamTrHopsTtHCSumSquares_Type()
)
tmnxOamTrHopsTtHCSumSquares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrHopsTtHCSumSquares.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamTrHopsTtHCSumSquares.setUnits("microseconds squared")
_TmnxOamTrHopsInTtOFSumSqrs_Type = Counter32
_TmnxOamTrHopsInTtOFSumSqrs_Object = MibTableColumn
tmnxOamTrHopsInTtOFSumSqrs = _TmnxOamTrHopsInTtOFSumSqrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 6, 1, 33),
    _TmnxOamTrHopsInTtOFSumSqrs_Type()
)
tmnxOamTrHopsInTtOFSumSqrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrHopsInTtOFSumSqrs.setStatus("current")
_TmnxOamTrHopsInTtHCSumSqrs_Type = Counter64
_TmnxOamTrHopsInTtHCSumSqrs_Object = MibTableColumn
tmnxOamTrHopsInTtHCSumSqrs = _TmnxOamTrHopsInTtHCSumSqrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 6, 1, 34),
    _TmnxOamTrHopsInTtHCSumSqrs_Type()
)
tmnxOamTrHopsInTtHCSumSqrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrHopsInTtHCSumSqrs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamTrHopsInTtHCSumSqrs.setUnits("microseconds squared")
_TmnxOamMacTrCtlTable_Object = MibTable
tmnxOamMacTrCtlTable = _TmnxOamMacTrCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 7)
)
if mibBuilder.loadTexts:
    tmnxOamMacTrCtlTable.setStatus("current")
_TmnxOamMacTrCtlEntry_Object = MibTableRow
tmnxOamMacTrCtlEntry = _TmnxOamMacTrCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 7, 1)
)
tmnxOamMacTrCtlEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamMacTrCtlEntry.setStatus("current")


class _TmnxOamMacTrCtlTargetMacAddr_Type(MacAddress):
    """Custom type tmnxOamMacTrCtlTargetMacAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_TmnxOamMacTrCtlTargetMacAddr_Type.__name__ = "MacAddress"
_TmnxOamMacTrCtlTargetMacAddr_Object = MibTableColumn
tmnxOamMacTrCtlTargetMacAddr = _TmnxOamMacTrCtlTargetMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 7, 1, 1),
    _TmnxOamMacTrCtlTargetMacAddr_Type()
)
tmnxOamMacTrCtlTargetMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMacTrCtlTargetMacAddr.setStatus("current")


class _TmnxOamMacTrCtlSourceMacAddr_Type(MacAddress):
    """Custom type tmnxOamMacTrCtlSourceMacAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_TmnxOamMacTrCtlSourceMacAddr_Type.__name__ = "MacAddress"
_TmnxOamMacTrCtlSourceMacAddr_Object = MibTableColumn
tmnxOamMacTrCtlSourceMacAddr = _TmnxOamMacTrCtlSourceMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 7, 1, 2),
    _TmnxOamMacTrCtlSourceMacAddr_Type()
)
tmnxOamMacTrCtlSourceMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMacTrCtlSourceMacAddr.setStatus("current")


class _TmnxOamMacTrCtlSendControl_Type(TruthValue):
    """Custom type tmnxOamMacTrCtlSendControl based on TruthValue"""
    defaultValue = 2


_TmnxOamMacTrCtlSendControl_Type.__name__ = "TruthValue"
_TmnxOamMacTrCtlSendControl_Object = MibTableColumn
tmnxOamMacTrCtlSendControl = _TmnxOamMacTrCtlSendControl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 7, 1, 3),
    _TmnxOamMacTrCtlSendControl_Type()
)
tmnxOamMacTrCtlSendControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMacTrCtlSendControl.setStatus("current")


class _TmnxOamMacTrCtlReplyControl_Type(TruthValue):
    """Custom type tmnxOamMacTrCtlReplyControl based on TruthValue"""
    defaultValue = 2


_TmnxOamMacTrCtlReplyControl_Type.__name__ = "TruthValue"
_TmnxOamMacTrCtlReplyControl_Object = MibTableColumn
tmnxOamMacTrCtlReplyControl = _TmnxOamMacTrCtlReplyControl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 7, 1, 4),
    _TmnxOamMacTrCtlReplyControl_Type()
)
tmnxOamMacTrCtlReplyControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMacTrCtlReplyControl.setStatus("current")
_TmnxOamMacTrL2MapTable_Object = MibTable
tmnxOamMacTrL2MapTable = _TmnxOamMacTrL2MapTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 8)
)
if mibBuilder.loadTexts:
    tmnxOamMacTrL2MapTable.setStatus("current")
_TmnxOamMacTrL2MapEntry_Object = MibTableRow
tmnxOamMacTrL2MapEntry = _TmnxOamMacTrL2MapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 8, 1)
)
tmnxOamMacTrL2MapEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsTestRunIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryHopIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryProbeIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamMacTrL2MapIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamMacTrL2MapEntry.setStatus("current")


class _TmnxOamMacTrL2MapIndex_Type(Unsigned32):
    """Custom type tmnxOamMacTrL2MapIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxOamMacTrL2MapIndex_Type.__name__ = "Unsigned32"
_TmnxOamMacTrL2MapIndex_Object = MibTableColumn
tmnxOamMacTrL2MapIndex = _TmnxOamMacTrL2MapIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 8, 1, 1),
    _TmnxOamMacTrL2MapIndex_Type()
)
tmnxOamMacTrL2MapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamMacTrL2MapIndex.setStatus("current")
_TmnxOamMacTrL2MapRouterID_Type = IpAddress
_TmnxOamMacTrL2MapRouterID_Object = MibTableColumn
tmnxOamMacTrL2MapRouterID = _TmnxOamMacTrL2MapRouterID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 8, 1, 2),
    _TmnxOamMacTrL2MapRouterID_Type()
)
tmnxOamMacTrL2MapRouterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacTrL2MapRouterID.setStatus("current")
_TmnxOamMacTrL2MapLabel_Type = MplsLabel
_TmnxOamMacTrL2MapLabel_Object = MibTableColumn
tmnxOamMacTrL2MapLabel = _TmnxOamMacTrL2MapLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 8, 1, 3),
    _TmnxOamMacTrL2MapLabel_Type()
)
tmnxOamMacTrL2MapLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacTrL2MapLabel.setStatus("current")
_TmnxOamMacTrL2MapProtocol_Type = TmnxOamSignalProtocol
_TmnxOamMacTrL2MapProtocol_Object = MibTableColumn
tmnxOamMacTrL2MapProtocol = _TmnxOamMacTrL2MapProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 8, 1, 4),
    _TmnxOamMacTrL2MapProtocol_Type()
)
tmnxOamMacTrL2MapProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacTrL2MapProtocol.setStatus("current")
_TmnxOamMacTrL2MapVCType_Type = TmnxOamVcType
_TmnxOamMacTrL2MapVCType_Object = MibTableColumn
tmnxOamMacTrL2MapVCType = _TmnxOamMacTrL2MapVCType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 8, 1, 5),
    _TmnxOamMacTrL2MapVCType_Type()
)
tmnxOamMacTrL2MapVCType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacTrL2MapVCType.setStatus("current")
_TmnxOamMacTrL2MapVCID_Type = TmnxVcId
_TmnxOamMacTrL2MapVCID_Object = MibTableColumn
tmnxOamMacTrL2MapVCID = _TmnxOamMacTrL2MapVCID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 8, 1, 6),
    _TmnxOamMacTrL2MapVCID_Type()
)
tmnxOamMacTrL2MapVCID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacTrL2MapVCID.setStatus("current")


class _TmnxOamMacTrL2MapDirection_Type(Integer32):
    """Custom type tmnxOamMacTrL2MapDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("upstream", 1),
          ("downstream", 2))
    )


_TmnxOamMacTrL2MapDirection_Type.__name__ = "Integer32"
_TmnxOamMacTrL2MapDirection_Object = MibTableColumn
tmnxOamMacTrL2MapDirection = _TmnxOamMacTrL2MapDirection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 8, 1, 7),
    _TmnxOamMacTrL2MapDirection_Type()
)
tmnxOamMacTrL2MapDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacTrL2MapDirection.setStatus("current")
_TmnxOamMacTrL2MapSdpId_Type = SdpId
_TmnxOamMacTrL2MapSdpId_Object = MibTableColumn
tmnxOamMacTrL2MapSdpId = _TmnxOamMacTrL2MapSdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 8, 1, 8),
    _TmnxOamMacTrL2MapSdpId_Type()
)
tmnxOamMacTrL2MapSdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacTrL2MapSdpId.setStatus("current")
_TmnxOamMacTrL2MapSapName_Type = TNamedItemOrEmpty
_TmnxOamMacTrL2MapSapName_Object = MibTableColumn
tmnxOamMacTrL2MapSapName = _TmnxOamMacTrL2MapSapName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 8, 1, 9),
    _TmnxOamMacTrL2MapSapName_Type()
)
tmnxOamMacTrL2MapSapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacTrL2MapSapName.setStatus("current")
_TmnxOamLspTrCtlTable_Object = MibTable
tmnxOamLspTrCtlTable = _TmnxOamLspTrCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 9)
)
if mibBuilder.loadTexts:
    tmnxOamLspTrCtlTable.setStatus("current")
_TmnxOamLspTrCtlEntry_Object = MibTableRow
tmnxOamLspTrCtlEntry = _TmnxOamLspTrCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 9, 1)
)
tmnxOamLspTrCtlEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamLspTrCtlEntry.setStatus("current")


class _TmnxOamLspTrCtlVRtrID_Type(TmnxVRtrID):
    """Custom type tmnxOamLspTrCtlVRtrID based on TmnxVRtrID"""
    defaultValue = 1


_TmnxOamLspTrCtlVRtrID_Type.__name__ = "TmnxVRtrID"
_TmnxOamLspTrCtlVRtrID_Object = MibTableColumn
tmnxOamLspTrCtlVRtrID = _TmnxOamLspTrCtlVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 9, 1, 1),
    _TmnxOamLspTrCtlVRtrID_Type()
)
tmnxOamLspTrCtlVRtrID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspTrCtlVRtrID.setStatus("obsolete")


class _TmnxOamLspTrCtlLspName_Type(TLNamedItemOrEmpty):
    """Custom type tmnxOamLspTrCtlLspName based on TLNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOamLspTrCtlLspName_Type.__name__ = "TLNamedItemOrEmpty"
_TmnxOamLspTrCtlLspName_Object = MibTableColumn
tmnxOamLspTrCtlLspName = _TmnxOamLspTrCtlLspName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 9, 1, 2),
    _TmnxOamLspTrCtlLspName_Type()
)
tmnxOamLspTrCtlLspName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspTrCtlLspName.setStatus("current")


class _TmnxOamLspTrCtlPathName_Type(TLNamedItemOrEmpty):
    """Custom type tmnxOamLspTrCtlPathName based on TLNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOamLspTrCtlPathName_Type.__name__ = "TLNamedItemOrEmpty"
_TmnxOamLspTrCtlPathName_Object = MibTableColumn
tmnxOamLspTrCtlPathName = _TmnxOamLspTrCtlPathName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 9, 1, 3),
    _TmnxOamLspTrCtlPathName_Type()
)
tmnxOamLspTrCtlPathName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspTrCtlPathName.setStatus("current")


class _TmnxOamLspTrCtlLdpIpPrefix_Type(IpAddress):
    """Custom type tmnxOamLspTrCtlLdpIpPrefix based on IpAddress"""
    defaultHexValue = "00000000"


_TmnxOamLspTrCtlLdpIpPrefix_Type.__name__ = "IpAddress"
_TmnxOamLspTrCtlLdpIpPrefix_Object = MibTableColumn
tmnxOamLspTrCtlLdpIpPrefix = _TmnxOamLspTrCtlLdpIpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 9, 1, 4),
    _TmnxOamLspTrCtlLdpIpPrefix_Type()
)
tmnxOamLspTrCtlLdpIpPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspTrCtlLdpIpPrefix.setStatus("obsolete")


class _TmnxOamLspTrCtlLdpIpPrefixLen_Type(IpAddressPrefixLength):
    """Custom type tmnxOamLspTrCtlLdpIpPrefixLen based on IpAddressPrefixLength"""
    defaultValue = 32


_TmnxOamLspTrCtlLdpIpPrefixLen_Type.__name__ = "IpAddressPrefixLength"
_TmnxOamLspTrCtlLdpIpPrefixLen_Object = MibTableColumn
tmnxOamLspTrCtlLdpIpPrefixLen = _TmnxOamLspTrCtlLdpIpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 9, 1, 5),
    _TmnxOamLspTrCtlLdpIpPrefixLen_Type()
)
tmnxOamLspTrCtlLdpIpPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspTrCtlLdpIpPrefixLen.setStatus("obsolete")


class _TmnxOamLspTrCtlLdpPrefixType_Type(InetAddressType):
    """Custom type tmnxOamLspTrCtlLdpPrefixType based on InetAddressType"""
    defaultValue = 0


_TmnxOamLspTrCtlLdpPrefixType_Type.__name__ = "InetAddressType"
_TmnxOamLspTrCtlLdpPrefixType_Object = MibTableColumn
tmnxOamLspTrCtlLdpPrefixType = _TmnxOamLspTrCtlLdpPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 9, 1, 6),
    _TmnxOamLspTrCtlLdpPrefixType_Type()
)
tmnxOamLspTrCtlLdpPrefixType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspTrCtlLdpPrefixType.setStatus("current")


class _TmnxOamLspTrCtlLdpPrefix_Type(InetAddress):
    """Custom type tmnxOamLspTrCtlLdpPrefix based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamLspTrCtlLdpPrefix_Type.__name__ = "InetAddress"
_TmnxOamLspTrCtlLdpPrefix_Object = MibTableColumn
tmnxOamLspTrCtlLdpPrefix = _TmnxOamLspTrCtlLdpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 9, 1, 7),
    _TmnxOamLspTrCtlLdpPrefix_Type()
)
tmnxOamLspTrCtlLdpPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspTrCtlLdpPrefix.setStatus("current")


class _TmnxOamLspTrCtlLdpPrefixLen_Type(InetAddressPrefixLength):
    """Custom type tmnxOamLspTrCtlLdpPrefixLen based on InetAddressPrefixLength"""
    defaultValue = 32


_TmnxOamLspTrCtlLdpPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxOamLspTrCtlLdpPrefixLen_Object = MibTableColumn
tmnxOamLspTrCtlLdpPrefixLen = _TmnxOamLspTrCtlLdpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 9, 1, 8),
    _TmnxOamLspTrCtlLdpPrefixLen_Type()
)
tmnxOamLspTrCtlLdpPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspTrCtlLdpPrefixLen.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamLspTrCtlLdpPrefixLen.setUnits("bits")


class _TmnxOamLspTrCtlPathDestType_Type(InetAddressType):
    """Custom type tmnxOamLspTrCtlPathDestType based on InetAddressType"""
    defaultValue = 0


_TmnxOamLspTrCtlPathDestType_Type.__name__ = "InetAddressType"
_TmnxOamLspTrCtlPathDestType_Object = MibTableColumn
tmnxOamLspTrCtlPathDestType = _TmnxOamLspTrCtlPathDestType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 9, 1, 9),
    _TmnxOamLspTrCtlPathDestType_Type()
)
tmnxOamLspTrCtlPathDestType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspTrCtlPathDestType.setStatus("current")


class _TmnxOamLspTrCtlPathDest_Type(InetAddress):
    """Custom type tmnxOamLspTrCtlPathDest based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamLspTrCtlPathDest_Type.__name__ = "InetAddress"
_TmnxOamLspTrCtlPathDest_Object = MibTableColumn
tmnxOamLspTrCtlPathDest = _TmnxOamLspTrCtlPathDest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 9, 1, 10),
    _TmnxOamLspTrCtlPathDest_Type()
)
tmnxOamLspTrCtlPathDest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspTrCtlPathDest.setStatus("current")


class _TmnxOamLspTrCtlNhIntfName_Type(TNamedItemOrEmpty):
    """Custom type tmnxOamLspTrCtlNhIntfName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOamLspTrCtlNhIntfName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOamLspTrCtlNhIntfName_Object = MibTableColumn
tmnxOamLspTrCtlNhIntfName = _TmnxOamLspTrCtlNhIntfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 9, 1, 11),
    _TmnxOamLspTrCtlNhIntfName_Type()
)
tmnxOamLspTrCtlNhIntfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspTrCtlNhIntfName.setStatus("current")


class _TmnxOamLspTrCtlNhAddressType_Type(InetAddressType):
    """Custom type tmnxOamLspTrCtlNhAddressType based on InetAddressType"""
    defaultValue = 0


_TmnxOamLspTrCtlNhAddressType_Type.__name__ = "InetAddressType"
_TmnxOamLspTrCtlNhAddressType_Object = MibTableColumn
tmnxOamLspTrCtlNhAddressType = _TmnxOamLspTrCtlNhAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 9, 1, 12),
    _TmnxOamLspTrCtlNhAddressType_Type()
)
tmnxOamLspTrCtlNhAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspTrCtlNhAddressType.setStatus("current")


class _TmnxOamLspTrCtlNhAddress_Type(InetAddress):
    """Custom type tmnxOamLspTrCtlNhAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamLspTrCtlNhAddress_Type.__name__ = "InetAddress"
_TmnxOamLspTrCtlNhAddress_Object = MibTableColumn
tmnxOamLspTrCtlNhAddress = _TmnxOamLspTrCtlNhAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 9, 1, 13),
    _TmnxOamLspTrCtlNhAddress_Type()
)
tmnxOamLspTrCtlNhAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspTrCtlNhAddress.setStatus("current")
_TmnxOamLspTrCtlDownstreamMapTlv_Type = TmnxOamMplsEchoDownMapTlvOrNone
_TmnxOamLspTrCtlDownstreamMapTlv_Object = MibTableColumn
tmnxOamLspTrCtlDownstreamMapTlv = _TmnxOamLspTrCtlDownstreamMapTlv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 9, 1, 14),
    _TmnxOamLspTrCtlDownstreamMapTlv_Type()
)
tmnxOamLspTrCtlDownstreamMapTlv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspTrCtlDownstreamMapTlv.setStatus("current")


class _TmnxOamLspTrCtlTestSubMode_Type(TmnxOamLspTestSubMode):
    """Custom type tmnxOamLspTrCtlTestSubMode based on TmnxOamLspTestSubMode"""
    defaultValue = 1


_TmnxOamLspTrCtlTestSubMode_Type.__name__ = "TmnxOamLspTestSubMode"
_TmnxOamLspTrCtlTestSubMode_Object = MibTableColumn
tmnxOamLspTrCtlTestSubMode = _TmnxOamLspTrCtlTestSubMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 9, 1, 15),
    _TmnxOamLspTrCtlTestSubMode_Type()
)
tmnxOamLspTrCtlTestSubMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspTrCtlTestSubMode.setStatus("current")


class _TmnxOamLspTrCtlMplsTpPathType_Type(TmnxOamMplsTpPathType):
    """Custom type tmnxOamLspTrCtlMplsTpPathType based on TmnxOamMplsTpPathType"""
    defaultValue = 3


_TmnxOamLspTrCtlMplsTpPathType_Type.__name__ = "TmnxOamMplsTpPathType"
_TmnxOamLspTrCtlMplsTpPathType_Object = MibTableColumn
tmnxOamLspTrCtlMplsTpPathType = _TmnxOamLspTrCtlMplsTpPathType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 9, 1, 16),
    _TmnxOamLspTrCtlMplsTpPathType_Type()
)
tmnxOamLspTrCtlMplsTpPathType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspTrCtlMplsTpPathType.setStatus("current")


class _TmnxOamLspTrCtlAssocChannel_Type(TmnxOamLspAssocChannel):
    """Custom type tmnxOamLspTrCtlAssocChannel based on TmnxOamLspAssocChannel"""
    defaultValue = 1


_TmnxOamLspTrCtlAssocChannel_Type.__name__ = "TmnxOamLspAssocChannel"
_TmnxOamLspTrCtlAssocChannel_Object = MibTableColumn
tmnxOamLspTrCtlAssocChannel = _TmnxOamLspTrCtlAssocChannel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 9, 1, 17),
    _TmnxOamLspTrCtlAssocChannel_Type()
)
tmnxOamLspTrCtlAssocChannel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspTrCtlAssocChannel.setStatus("current")


class _TmnxOamLspTrCtlForce_Type(TruthValue):
    """Custom type tmnxOamLspTrCtlForce based on TruthValue"""
    defaultValue = 2


_TmnxOamLspTrCtlForce_Type.__name__ = "TruthValue"
_TmnxOamLspTrCtlForce_Object = MibTableColumn
tmnxOamLspTrCtlForce = _TmnxOamLspTrCtlForce_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 9, 1, 18),
    _TmnxOamLspTrCtlForce_Type()
)
tmnxOamLspTrCtlForce.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspTrCtlForce.setStatus("current")


class _TmnxOamLspTrCtlIgpInstance_Type(TmnxIgpInstance):
    """Custom type tmnxOamLspTrCtlIgpInstance based on TmnxIgpInstance"""
    defaultValue = 0


_TmnxOamLspTrCtlIgpInstance_Type.__name__ = "TmnxIgpInstance"
_TmnxOamLspTrCtlIgpInstance_Object = MibTableColumn
tmnxOamLspTrCtlIgpInstance = _TmnxOamLspTrCtlIgpInstance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 9, 1, 19),
    _TmnxOamLspTrCtlIgpInstance_Type()
)
tmnxOamLspTrCtlIgpInstance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspTrCtlIgpInstance.setStatus("current")


class _TmnxOamLspTrCtlSrPlcyColor_Type(Unsigned32):
    """Custom type tmnxOamLspTrCtlSrPlcyColor based on Unsigned32"""
    defaultValue = 0


_TmnxOamLspTrCtlSrPlcyColor_Type.__name__ = "Unsigned32"
_TmnxOamLspTrCtlSrPlcyColor_Object = MibTableColumn
tmnxOamLspTrCtlSrPlcyColor = _TmnxOamLspTrCtlSrPlcyColor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 9, 1, 20),
    _TmnxOamLspTrCtlSrPlcyColor_Type()
)
tmnxOamLspTrCtlSrPlcyColor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspTrCtlSrPlcyColor.setStatus("current")


class _TmnxOamLspTrCtlSrPlcyEndPtAddT_Type(InetAddressType):
    """Custom type tmnxOamLspTrCtlSrPlcyEndPtAddT based on InetAddressType"""
    defaultValue = 0


_TmnxOamLspTrCtlSrPlcyEndPtAddT_Type.__name__ = "InetAddressType"
_TmnxOamLspTrCtlSrPlcyEndPtAddT_Object = MibTableColumn
tmnxOamLspTrCtlSrPlcyEndPtAddT = _TmnxOamLspTrCtlSrPlcyEndPtAddT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 9, 1, 21),
    _TmnxOamLspTrCtlSrPlcyEndPtAddT_Type()
)
tmnxOamLspTrCtlSrPlcyEndPtAddT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspTrCtlSrPlcyEndPtAddT.setStatus("current")


class _TmnxOamLspTrCtlSrPlcyEndPtAddr_Type(InetAddress):
    """Custom type tmnxOamLspTrCtlSrPlcyEndPtAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamLspTrCtlSrPlcyEndPtAddr_Type.__name__ = "InetAddress"
_TmnxOamLspTrCtlSrPlcyEndPtAddr_Object = MibTableColumn
tmnxOamLspTrCtlSrPlcyEndPtAddr = _TmnxOamLspTrCtlSrPlcyEndPtAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 9, 1, 22),
    _TmnxOamLspTrCtlSrPlcyEndPtAddr_Type()
)
tmnxOamLspTrCtlSrPlcyEndPtAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspTrCtlSrPlcyEndPtAddr.setStatus("current")


class _TmnxOamLspTrCtlSrPlcySegList_Type(Unsigned32):
    """Custom type tmnxOamLspTrCtlSrPlcySegList based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_TmnxOamLspTrCtlSrPlcySegList_Type.__name__ = "Unsigned32"
_TmnxOamLspTrCtlSrPlcySegList_Object = MibTableColumn
tmnxOamLspTrCtlSrPlcySegList = _TmnxOamLspTrCtlSrPlcySegList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 9, 1, 23),
    _TmnxOamLspTrCtlSrPlcySegList_Type()
)
tmnxOamLspTrCtlSrPlcySegList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspTrCtlSrPlcySegList.setStatus("current")
_TmnxOamLspTrMapTable_Object = MibTable
tmnxOamLspTrMapTable = _TmnxOamLspTrMapTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 10)
)
if mibBuilder.loadTexts:
    tmnxOamLspTrMapTable.setStatus("current")
_TmnxOamLspTrMapEntry_Object = MibTableRow
tmnxOamLspTrMapEntry = _TmnxOamLspTrMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 10, 1)
)
tmnxOamLspTrMapEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsTestRunIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryHopIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryProbeIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrMapIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamLspTrMapEntry.setStatus("current")


class _TmnxOamLspTrMapIndex_Type(Unsigned32):
    """Custom type tmnxOamLspTrMapIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxOamLspTrMapIndex_Type.__name__ = "Unsigned32"
_TmnxOamLspTrMapIndex_Object = MibTableColumn
tmnxOamLspTrMapIndex = _TmnxOamLspTrMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 10, 1, 1),
    _TmnxOamLspTrMapIndex_Type()
)
tmnxOamLspTrMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamLspTrMapIndex.setStatus("current")
_TmnxOamLspTrMapDSIPv4Addr_Type = IpAddress
_TmnxOamLspTrMapDSIPv4Addr_Object = MibTableColumn
tmnxOamLspTrMapDSIPv4Addr = _TmnxOamLspTrMapDSIPv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 10, 1, 2),
    _TmnxOamLspTrMapDSIPv4Addr_Type()
)
tmnxOamLspTrMapDSIPv4Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLspTrMapDSIPv4Addr.setStatus("obsolete")
_TmnxOamLspTrMapAddrType_Type = TmnxOamAddressType
_TmnxOamLspTrMapAddrType_Object = MibTableColumn
tmnxOamLspTrMapAddrType = _TmnxOamLspTrMapAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 10, 1, 3),
    _TmnxOamLspTrMapAddrType_Type()
)
tmnxOamLspTrMapAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLspTrMapAddrType.setStatus("current")
_TmnxOamLspTrMapDSIfAddr_Type = Unsigned32
_TmnxOamLspTrMapDSIfAddr_Object = MibTableColumn
tmnxOamLspTrMapDSIfAddr = _TmnxOamLspTrMapDSIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 10, 1, 4),
    _TmnxOamLspTrMapDSIfAddr_Type()
)
tmnxOamLspTrMapDSIfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLspTrMapDSIfAddr.setStatus("obsolete")


class _TmnxOamLspTrMapMTU_Type(Unsigned32):
    """Custom type tmnxOamLspTrMapMTU based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TmnxOamLspTrMapMTU_Type.__name__ = "Unsigned32"
_TmnxOamLspTrMapMTU_Object = MibTableColumn
tmnxOamLspTrMapMTU = _TmnxOamLspTrMapMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 10, 1, 5),
    _TmnxOamLspTrMapMTU_Type()
)
tmnxOamLspTrMapMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLspTrMapMTU.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamLspTrMapMTU.setUnits("octets")


class _TmnxOamLspTrMapDSIndex_Type(Unsigned32):
    """Custom type tmnxOamLspTrMapDSIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxOamLspTrMapDSIndex_Type.__name__ = "Unsigned32"
_TmnxOamLspTrMapDSIndex_Object = MibTableColumn
tmnxOamLspTrMapDSIndex = _TmnxOamLspTrMapDSIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 10, 1, 6),
    _TmnxOamLspTrMapDSIndex_Type()
)
tmnxOamLspTrMapDSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLspTrMapDSIndex.setStatus("obsolete")
_TmnxOamLspTrMapDsEgrIfNum_Type = Unsigned32
_TmnxOamLspTrMapDsEgrIfNum_Object = MibTableColumn
tmnxOamLspTrMapDsEgrIfNum = _TmnxOamLspTrMapDsEgrIfNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 10, 1, 7),
    _TmnxOamLspTrMapDsEgrIfNum_Type()
)
tmnxOamLspTrMapDsEgrIfNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLspTrMapDsEgrIfNum.setStatus("current")
_TmnxOamLspTrMapDsIngIfNum_Type = Unsigned32
_TmnxOamLspTrMapDsIngIfNum_Object = MibTableColumn
tmnxOamLspTrMapDsIngIfNum = _TmnxOamLspTrMapDsIngIfNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 10, 1, 8),
    _TmnxOamLspTrMapDsIngIfNum_Type()
)
tmnxOamLspTrMapDsIngIfNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLspTrMapDsIngIfNum.setStatus("current")
_TmnxOamLspTrMapDsIpAddressType_Type = InetAddressType
_TmnxOamLspTrMapDsIpAddressType_Object = MibTableColumn
tmnxOamLspTrMapDsIpAddressType = _TmnxOamLspTrMapDsIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 10, 1, 9),
    _TmnxOamLspTrMapDsIpAddressType_Type()
)
tmnxOamLspTrMapDsIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLspTrMapDsIpAddressType.setStatus("current")


class _TmnxOamLspTrMapDsIpAddress_Type(InetAddress):
    """Custom type tmnxOamLspTrMapDsIpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamLspTrMapDsIpAddress_Type.__name__ = "InetAddress"
_TmnxOamLspTrMapDsIpAddress_Object = MibTableColumn
tmnxOamLspTrMapDsIpAddress = _TmnxOamLspTrMapDsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 10, 1, 10),
    _TmnxOamLspTrMapDsIpAddress_Type()
)
tmnxOamLspTrMapDsIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLspTrMapDsIpAddress.setStatus("current")
_TmnxOamLspTrMapDsIfAddressType_Type = InetAddressType
_TmnxOamLspTrMapDsIfAddressType_Object = MibTableColumn
tmnxOamLspTrMapDsIfAddressType = _TmnxOamLspTrMapDsIfAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 10, 1, 11),
    _TmnxOamLspTrMapDsIfAddressType_Type()
)
tmnxOamLspTrMapDsIfAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLspTrMapDsIfAddressType.setStatus("current")


class _TmnxOamLspTrMapDsIfAddress_Type(InetAddress):
    """Custom type tmnxOamLspTrMapDsIfAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamLspTrMapDsIfAddress_Type.__name__ = "InetAddress"
_TmnxOamLspTrMapDsIfAddress_Object = MibTableColumn
tmnxOamLspTrMapDsIfAddress = _TmnxOamLspTrMapDsIfAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 10, 1, 12),
    _TmnxOamLspTrMapDsIfAddress_Type()
)
tmnxOamLspTrMapDsIfAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLspTrMapDsIfAddress.setStatus("current")
_TmnxOamVprnTrCtlTable_Object = MibTable
tmnxOamVprnTrCtlTable = _TmnxOamVprnTrCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 11)
)
if mibBuilder.loadTexts:
    tmnxOamVprnTrCtlTable.setStatus("current")
_TmnxOamVprnTrCtlEntry_Object = MibTableRow
tmnxOamVprnTrCtlEntry = _TmnxOamVprnTrCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 11, 1)
)
tmnxOamVprnTrCtlEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamVprnTrCtlEntry.setStatus("current")


class _TmnxOamVprnTrCtlSourceIpAddr_Type(IpAddress):
    """Custom type tmnxOamVprnTrCtlSourceIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_TmnxOamVprnTrCtlSourceIpAddr_Type.__name__ = "IpAddress"
_TmnxOamVprnTrCtlSourceIpAddr_Object = MibTableColumn
tmnxOamVprnTrCtlSourceIpAddr = _TmnxOamVprnTrCtlSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 11, 1, 1),
    _TmnxOamVprnTrCtlSourceIpAddr_Type()
)
tmnxOamVprnTrCtlSourceIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamVprnTrCtlSourceIpAddr.setStatus("obsolete")


class _TmnxOamVprnTrCtlReplyControl_Type(TruthValue):
    """Custom type tmnxOamVprnTrCtlReplyControl based on TruthValue"""
    defaultValue = 2


_TmnxOamVprnTrCtlReplyControl_Type.__name__ = "TruthValue"
_TmnxOamVprnTrCtlReplyControl_Object = MibTableColumn
tmnxOamVprnTrCtlReplyControl = _TmnxOamVprnTrCtlReplyControl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 11, 1, 2),
    _TmnxOamVprnTrCtlReplyControl_Type()
)
tmnxOamVprnTrCtlReplyControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamVprnTrCtlReplyControl.setStatus("current")


class _TmnxOamVprnTrCtlSrcAddrType_Type(InetAddressType):
    """Custom type tmnxOamVprnTrCtlSrcAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxOamVprnTrCtlSrcAddrType_Type.__name__ = "InetAddressType"
_TmnxOamVprnTrCtlSrcAddrType_Object = MibTableColumn
tmnxOamVprnTrCtlSrcAddrType = _TmnxOamVprnTrCtlSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 11, 1, 3),
    _TmnxOamVprnTrCtlSrcAddrType_Type()
)
tmnxOamVprnTrCtlSrcAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamVprnTrCtlSrcAddrType.setStatus("current")


class _TmnxOamVprnTrCtlSrcAddress_Type(InetAddress):
    """Custom type tmnxOamVprnTrCtlSrcAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamVprnTrCtlSrcAddress_Type.__name__ = "InetAddress"
_TmnxOamVprnTrCtlSrcAddress_Object = MibTableColumn
tmnxOamVprnTrCtlSrcAddress = _TmnxOamVprnTrCtlSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 11, 1, 4),
    _TmnxOamVprnTrCtlSrcAddress_Type()
)
tmnxOamVprnTrCtlSrcAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamVprnTrCtlSrcAddress.setStatus("current")
_TmnxOamVprnTrL3MapTable_Object = MibTable
tmnxOamVprnTrL3MapTable = _TmnxOamVprnTrL3MapTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 12)
)
if mibBuilder.loadTexts:
    tmnxOamVprnTrL3MapTable.setStatus("current")
_TmnxOamVprnTrL3MapEntry_Object = MibTableRow
tmnxOamVprnTrL3MapEntry = _TmnxOamVprnTrL3MapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 12, 1)
)
tmnxOamVprnTrL3MapEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsTestRunIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryHopIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryProbeIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrL3MapReporter"),
)
if mibBuilder.loadTexts:
    tmnxOamVprnTrL3MapEntry.setStatus("current")


class _TmnxOamVprnTrL3MapReporter_Type(Integer32):
    """Custom type tmnxOamVprnTrL3MapReporter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("requestor", 1),
          ("responder", 2))
    )


_TmnxOamVprnTrL3MapReporter_Type.__name__ = "Integer32"
_TmnxOamVprnTrL3MapReporter_Object = MibTableColumn
tmnxOamVprnTrL3MapReporter = _TmnxOamVprnTrL3MapReporter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 12, 1, 1),
    _TmnxOamVprnTrL3MapReporter_Type()
)
tmnxOamVprnTrL3MapReporter.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamVprnTrL3MapReporter.setStatus("current")
_TmnxOamVprnTrL3MapRouterID_Type = RouterID
_TmnxOamVprnTrL3MapRouterID_Object = MibTableColumn
tmnxOamVprnTrL3MapRouterID = _TmnxOamVprnTrL3MapRouterID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 12, 1, 2),
    _TmnxOamVprnTrL3MapRouterID_Type()
)
tmnxOamVprnTrL3MapRouterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVprnTrL3MapRouterID.setStatus("current")
_TmnxOamVprnTrL3MapRteDestAddr_Type = IpAddress
_TmnxOamVprnTrL3MapRteDestAddr_Object = MibTableColumn
tmnxOamVprnTrL3MapRteDestAddr = _TmnxOamVprnTrL3MapRteDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 12, 1, 3),
    _TmnxOamVprnTrL3MapRteDestAddr_Type()
)
tmnxOamVprnTrL3MapRteDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVprnTrL3MapRteDestAddr.setStatus("obsolete")
_TmnxOamVprnTrL3MapRteDestMask_Type = Unsigned32
_TmnxOamVprnTrL3MapRteDestMask_Object = MibTableColumn
tmnxOamVprnTrL3MapRteDestMask = _TmnxOamVprnTrL3MapRteDestMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 12, 1, 4),
    _TmnxOamVprnTrL3MapRteDestMask_Type()
)
tmnxOamVprnTrL3MapRteDestMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVprnTrL3MapRteDestMask.setStatus("obsolete")
_TmnxOamVprnTrL3MapRteVprnLabel_Type = MplsLabel
_TmnxOamVprnTrL3MapRteVprnLabel_Object = MibTableColumn
tmnxOamVprnTrL3MapRteVprnLabel = _TmnxOamVprnTrL3MapRteVprnLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 12, 1, 5),
    _TmnxOamVprnTrL3MapRteVprnLabel_Type()
)
tmnxOamVprnTrL3MapRteVprnLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVprnTrL3MapRteVprnLabel.setStatus("current")
_TmnxOamVprnTrL3MapRteMetrics_Type = Unsigned32
_TmnxOamVprnTrL3MapRteMetrics_Object = MibTableColumn
tmnxOamVprnTrL3MapRteMetrics = _TmnxOamVprnTrL3MapRteMetrics_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 12, 1, 6),
    _TmnxOamVprnTrL3MapRteMetrics_Type()
)
tmnxOamVprnTrL3MapRteMetrics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVprnTrL3MapRteMetrics.setStatus("current")
_TmnxOamVprnTrL3MapRteLastUp_Type = DateAndTime
_TmnxOamVprnTrL3MapRteLastUp_Object = MibTableColumn
tmnxOamVprnTrL3MapRteLastUp = _TmnxOamVprnTrL3MapRteLastUp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 12, 1, 7),
    _TmnxOamVprnTrL3MapRteLastUp_Type()
)
tmnxOamVprnTrL3MapRteLastUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVprnTrL3MapRteLastUp.setStatus("current")


class _TmnxOamVprnTrL3MapRteOwner_Type(Integer32):
    """Custom type tmnxOamVprnTrL3MapRteOwner based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("local", 1),
          ("static", 2),
          ("rip", 3),
          ("ospf", 4),
          ("isis", 5),
          ("bgp", 6),
          ("bgpVpn", 7),
          ("ldp", 8),
          ("aggregate", 9),
          ("any", 10))
    )


_TmnxOamVprnTrL3MapRteOwner_Type.__name__ = "Integer32"
_TmnxOamVprnTrL3MapRteOwner_Object = MibTableColumn
tmnxOamVprnTrL3MapRteOwner = _TmnxOamVprnTrL3MapRteOwner_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 12, 1, 8),
    _TmnxOamVprnTrL3MapRteOwner_Type()
)
tmnxOamVprnTrL3MapRteOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVprnTrL3MapRteOwner.setStatus("current")
_TmnxOamVprnTrL3MapRtePref_Type = Unsigned32
_TmnxOamVprnTrL3MapRtePref_Object = MibTableColumn
tmnxOamVprnTrL3MapRtePref = _TmnxOamVprnTrL3MapRtePref_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 12, 1, 9),
    _TmnxOamVprnTrL3MapRtePref_Type()
)
tmnxOamVprnTrL3MapRtePref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVprnTrL3MapRtePref.setStatus("current")
_TmnxOamVprnTrL3MapRteDist_Type = TmnxVPNRouteDistinguisher
_TmnxOamVprnTrL3MapRteDist_Object = MibTableColumn
tmnxOamVprnTrL3MapRteDist = _TmnxOamVprnTrL3MapRteDist_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 12, 1, 10),
    _TmnxOamVprnTrL3MapRteDist_Type()
)
tmnxOamVprnTrL3MapRteDist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVprnTrL3MapRteDist.setStatus("current")
_TmnxOamVprnTrL3MapNumNextHops_Type = Unsigned32
_TmnxOamVprnTrL3MapNumNextHops_Object = MibTableColumn
tmnxOamVprnTrL3MapNumNextHops = _TmnxOamVprnTrL3MapNumNextHops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 12, 1, 11),
    _TmnxOamVprnTrL3MapNumNextHops_Type()
)
tmnxOamVprnTrL3MapNumNextHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVprnTrL3MapNumNextHops.setStatus("current")
_TmnxOamVprnTrL3MapNumRteTargets_Type = Unsigned32
_TmnxOamVprnTrL3MapNumRteTargets_Object = MibTableColumn
tmnxOamVprnTrL3MapNumRteTargets = _TmnxOamVprnTrL3MapNumRteTargets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 12, 1, 12),
    _TmnxOamVprnTrL3MapNumRteTargets_Type()
)
tmnxOamVprnTrL3MapNumRteTargets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVprnTrL3MapNumRteTargets.setStatus("current")
_TmnxOamVprnTrL3MapDestAddrType_Type = InetAddressType
_TmnxOamVprnTrL3MapDestAddrType_Object = MibTableColumn
tmnxOamVprnTrL3MapDestAddrType = _TmnxOamVprnTrL3MapDestAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 12, 1, 13),
    _TmnxOamVprnTrL3MapDestAddrType_Type()
)
tmnxOamVprnTrL3MapDestAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVprnTrL3MapDestAddrType.setStatus("current")


class _TmnxOamVprnTrL3MapDestAddress_Type(InetAddress):
    """Custom type tmnxOamVprnTrL3MapDestAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamVprnTrL3MapDestAddress_Type.__name__ = "InetAddress"
_TmnxOamVprnTrL3MapDestAddress_Object = MibTableColumn
tmnxOamVprnTrL3MapDestAddress = _TmnxOamVprnTrL3MapDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 12, 1, 14),
    _TmnxOamVprnTrL3MapDestAddress_Type()
)
tmnxOamVprnTrL3MapDestAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVprnTrL3MapDestAddress.setStatus("current")
_TmnxOamVprnTrL3MapDestMaskLen_Type = InetAddressPrefixLength
_TmnxOamVprnTrL3MapDestMaskLen_Object = MibTableColumn
tmnxOamVprnTrL3MapDestMaskLen = _TmnxOamVprnTrL3MapDestMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 12, 1, 15),
    _TmnxOamVprnTrL3MapDestMaskLen_Type()
)
tmnxOamVprnTrL3MapDestMaskLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVprnTrL3MapDestMaskLen.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamVprnTrL3MapDestMaskLen.setUnits("bits")
_TmnxOamVprnTrNextHopTable_Object = MibTable
tmnxOamVprnTrNextHopTable = _TmnxOamVprnTrNextHopTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 13)
)
if mibBuilder.loadTexts:
    tmnxOamVprnTrNextHopTable.setStatus("current")
_TmnxOamVprnTrNextHopEntry_Object = MibTableRow
tmnxOamVprnTrNextHopEntry = _TmnxOamVprnTrNextHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 13, 1)
)
tmnxOamVprnTrNextHopEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsTestRunIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryHopIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryProbeIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrL3MapReporter"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrNextHopIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamVprnTrNextHopEntry.setStatus("current")


class _TmnxOamVprnTrNextHopIndex_Type(Unsigned32):
    """Custom type tmnxOamVprnTrNextHopIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxOamVprnTrNextHopIndex_Type.__name__ = "Unsigned32"
_TmnxOamVprnTrNextHopIndex_Object = MibTableColumn
tmnxOamVprnTrNextHopIndex = _TmnxOamVprnTrNextHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 13, 1, 1),
    _TmnxOamVprnTrNextHopIndex_Type()
)
tmnxOamVprnTrNextHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamVprnTrNextHopIndex.setStatus("current")
_TmnxOamVprnTrNextHopRtrID_Type = RouterID
_TmnxOamVprnTrNextHopRtrID_Object = MibTableColumn
tmnxOamVprnTrNextHopRtrID = _TmnxOamVprnTrNextHopRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 13, 1, 2),
    _TmnxOamVprnTrNextHopRtrID_Type()
)
tmnxOamVprnTrNextHopRtrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVprnTrNextHopRtrID.setStatus("obsolete")


class _TmnxOamVprnTrNextHopType_Type(Integer32):
    """Custom type tmnxOamVprnTrNextHopType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_TmnxOamVprnTrNextHopType_Type.__name__ = "Integer32"
_TmnxOamVprnTrNextHopType_Object = MibTableColumn
tmnxOamVprnTrNextHopType = _TmnxOamVprnTrNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 13, 1, 3),
    _TmnxOamVprnTrNextHopType_Type()
)
tmnxOamVprnTrNextHopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVprnTrNextHopType.setStatus("current")
_TmnxOamVprnTrNextHopTunnelID_Type = TmnxTunnelID
_TmnxOamVprnTrNextHopTunnelID_Object = MibTableColumn
tmnxOamVprnTrNextHopTunnelID = _TmnxOamVprnTrNextHopTunnelID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 13, 1, 4),
    _TmnxOamVprnTrNextHopTunnelID_Type()
)
tmnxOamVprnTrNextHopTunnelID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVprnTrNextHopTunnelID.setStatus("current")
_TmnxOamVprnTrNextHopTunnelType_Type = TmnxTunnelType
_TmnxOamVprnTrNextHopTunnelType_Object = MibTableColumn
tmnxOamVprnTrNextHopTunnelType = _TmnxOamVprnTrNextHopTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 13, 1, 5),
    _TmnxOamVprnTrNextHopTunnelType_Type()
)
tmnxOamVprnTrNextHopTunnelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVprnTrNextHopTunnelType.setStatus("current")
_TmnxOamVprnTrNextHopIfIndex_Type = InterfaceIndex
_TmnxOamVprnTrNextHopIfIndex_Object = MibTableColumn
tmnxOamVprnTrNextHopIfIndex = _TmnxOamVprnTrNextHopIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 13, 1, 6),
    _TmnxOamVprnTrNextHopIfIndex_Type()
)
tmnxOamVprnTrNextHopIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVprnTrNextHopIfIndex.setStatus("current")
_TmnxOamVprnTrNextHopAddrType_Type = InetAddressType
_TmnxOamVprnTrNextHopAddrType_Object = MibTableColumn
tmnxOamVprnTrNextHopAddrType = _TmnxOamVprnTrNextHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 13, 1, 7),
    _TmnxOamVprnTrNextHopAddrType_Type()
)
tmnxOamVprnTrNextHopAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVprnTrNextHopAddrType.setStatus("current")


class _TmnxOamVprnTrNextHopAddress_Type(InetAddress):
    """Custom type tmnxOamVprnTrNextHopAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxOamVprnTrNextHopAddress_Type.__name__ = "InetAddress"
_TmnxOamVprnTrNextHopAddress_Object = MibTableColumn
tmnxOamVprnTrNextHopAddress = _TmnxOamVprnTrNextHopAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 13, 1, 8),
    _TmnxOamVprnTrNextHopAddress_Type()
)
tmnxOamVprnTrNextHopAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVprnTrNextHopAddress.setStatus("current")
_TmnxOamVprnTrRTTable_Object = MibTable
tmnxOamVprnTrRTTable = _TmnxOamVprnTrRTTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 14)
)
if mibBuilder.loadTexts:
    tmnxOamVprnTrRTTable.setStatus("current")
_TmnxOamVprnTrRTEntry_Object = MibTableRow
tmnxOamVprnTrRTEntry = _TmnxOamVprnTrRTEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 14, 1)
)
tmnxOamVprnTrRTEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsTestRunIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryHopIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryProbeIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrL3MapReporter"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrRTIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamVprnTrRTEntry.setStatus("current")


class _TmnxOamVprnTrRTIndex_Type(Unsigned32):
    """Custom type tmnxOamVprnTrRTIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxOamVprnTrRTIndex_Type.__name__ = "Unsigned32"
_TmnxOamVprnTrRTIndex_Object = MibTableColumn
tmnxOamVprnTrRTIndex = _TmnxOamVprnTrRTIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 14, 1, 1),
    _TmnxOamVprnTrRTIndex_Type()
)
tmnxOamVprnTrRTIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamVprnTrRTIndex.setStatus("current")
_TmnxOamVprnTrRouteTarget_Type = TmnxBgpRouteTarget
_TmnxOamVprnTrRouteTarget_Object = MibTableColumn
tmnxOamVprnTrRouteTarget = _TmnxOamVprnTrRouteTarget_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 14, 1, 2),
    _TmnxOamVprnTrRouteTarget_Type()
)
tmnxOamVprnTrRouteTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVprnTrRouteTarget.setStatus("current")
_TmnxOamLspTrDSLabelTable_Object = MibTable
tmnxOamLspTrDSLabelTable = _TmnxOamLspTrDSLabelTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 15)
)
if mibBuilder.loadTexts:
    tmnxOamLspTrDSLabelTable.setStatus("current")
_TmnxOamLspTrDSLabelEntry_Object = MibTableRow
tmnxOamLspTrDSLabelEntry = _TmnxOamLspTrDSLabelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 15, 1)
)
tmnxOamLspTrDSLabelEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsTestRunIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryHopIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryProbeIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrMapIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrDSLabelIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamLspTrDSLabelEntry.setStatus("current")


class _TmnxOamLspTrDSLabelIndex_Type(Unsigned32):
    """Custom type tmnxOamLspTrDSLabelIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxOamLspTrDSLabelIndex_Type.__name__ = "Unsigned32"
_TmnxOamLspTrDSLabelIndex_Object = MibTableColumn
tmnxOamLspTrDSLabelIndex = _TmnxOamLspTrDSLabelIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 15, 1, 1),
    _TmnxOamLspTrDSLabelIndex_Type()
)
tmnxOamLspTrDSLabelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamLspTrDSLabelIndex.setStatus("current")
_TmnxOamLspTrDSLabelLabel_Type = MplsLabel
_TmnxOamLspTrDSLabelLabel_Object = MibTableColumn
tmnxOamLspTrDSLabelLabel = _TmnxOamLspTrDSLabelLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 15, 1, 2),
    _TmnxOamLspTrDSLabelLabel_Type()
)
tmnxOamLspTrDSLabelLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLspTrDSLabelLabel.setStatus("current")
_TmnxOamLspTrDSLabelProtocol_Type = TmnxOamSignalProtocol
_TmnxOamLspTrDSLabelProtocol_Object = MibTableColumn
tmnxOamLspTrDSLabelProtocol = _TmnxOamLspTrDSLabelProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 15, 1, 3),
    _TmnxOamLspTrDSLabelProtocol_Type()
)
tmnxOamLspTrDSLabelProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLspTrDSLabelProtocol.setStatus("current")
_TmnxOamMcastTrCtlTable_Object = MibTable
tmnxOamMcastTrCtlTable = _TmnxOamMcastTrCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 16)
)
if mibBuilder.loadTexts:
    tmnxOamMcastTrCtlTable.setStatus("current")
_TmnxOamMcastTrCtlEntry_Object = MibTableRow
tmnxOamMcastTrCtlEntry = _TmnxOamMcastTrCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 16, 1)
)
tmnxOamMcastTrCtlEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamMcastTrCtlEntry.setStatus("current")


class _TmnxOamMcastTrCtlVRtrID_Type(TmnxVRtrID):
    """Custom type tmnxOamMcastTrCtlVRtrID based on TmnxVRtrID"""
    defaultValue = 1


_TmnxOamMcastTrCtlVRtrID_Type.__name__ = "TmnxVRtrID"
_TmnxOamMcastTrCtlVRtrID_Object = MibTableColumn
tmnxOamMcastTrCtlVRtrID = _TmnxOamMcastTrCtlVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 16, 1, 1),
    _TmnxOamMcastTrCtlVRtrID_Type()
)
tmnxOamMcastTrCtlVRtrID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMcastTrCtlVRtrID.setStatus("current")
_TmnxOamMcastTrCtlSrcIpAddr_Type = IpAddress
_TmnxOamMcastTrCtlSrcIpAddr_Object = MibTableColumn
tmnxOamMcastTrCtlSrcIpAddr = _TmnxOamMcastTrCtlSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 16, 1, 2),
    _TmnxOamMcastTrCtlSrcIpAddr_Type()
)
tmnxOamMcastTrCtlSrcIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMcastTrCtlSrcIpAddr.setStatus("obsolete")


class _TmnxOamMcastTrCtlDestIpAddr_Type(IpAddress):
    """Custom type tmnxOamMcastTrCtlDestIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_TmnxOamMcastTrCtlDestIpAddr_Type.__name__ = "IpAddress"
_TmnxOamMcastTrCtlDestIpAddr_Object = MibTableColumn
tmnxOamMcastTrCtlDestIpAddr = _TmnxOamMcastTrCtlDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 16, 1, 3),
    _TmnxOamMcastTrCtlDestIpAddr_Type()
)
tmnxOamMcastTrCtlDestIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMcastTrCtlDestIpAddr.setStatus("obsolete")
_TmnxOamMcastTrCtlRespIpAddr_Type = IpAddress
_TmnxOamMcastTrCtlRespIpAddr_Object = MibTableColumn
tmnxOamMcastTrCtlRespIpAddr = _TmnxOamMcastTrCtlRespIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 16, 1, 4),
    _TmnxOamMcastTrCtlRespIpAddr_Type()
)
tmnxOamMcastTrCtlRespIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMcastTrCtlRespIpAddr.setStatus("obsolete")
_TmnxOamMcastTrCtlGrpIpAddr_Type = IpAddress
_TmnxOamMcastTrCtlGrpIpAddr_Object = MibTableColumn
tmnxOamMcastTrCtlGrpIpAddr = _TmnxOamMcastTrCtlGrpIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 16, 1, 5),
    _TmnxOamMcastTrCtlGrpIpAddr_Type()
)
tmnxOamMcastTrCtlGrpIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMcastTrCtlGrpIpAddr.setStatus("obsolete")


class _TmnxOamMcastTrCtlHops_Type(Unsigned32):
    """Custom type tmnxOamMcastTrCtlHops based on Unsigned32"""
    defaultValue = 32

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TmnxOamMcastTrCtlHops_Type.__name__ = "Unsigned32"
_TmnxOamMcastTrCtlHops_Object = MibTableColumn
tmnxOamMcastTrCtlHops = _TmnxOamMcastTrCtlHops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 16, 1, 6),
    _TmnxOamMcastTrCtlHops_Type()
)
tmnxOamMcastTrCtlHops.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMcastTrCtlHops.setStatus("current")
_TmnxOamMcastTrQueryId_Type = Unsigned32
_TmnxOamMcastTrQueryId_Object = MibTableColumn
tmnxOamMcastTrQueryId = _TmnxOamMcastTrQueryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 16, 1, 7),
    _TmnxOamMcastTrQueryId_Type()
)
tmnxOamMcastTrQueryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMcastTrQueryId.setStatus("current")


class _TmnxOamMcastTrCtlSrcAddrType_Type(InetAddressType):
    """Custom type tmnxOamMcastTrCtlSrcAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxOamMcastTrCtlSrcAddrType_Type.__name__ = "InetAddressType"
_TmnxOamMcastTrCtlSrcAddrType_Object = MibTableColumn
tmnxOamMcastTrCtlSrcAddrType = _TmnxOamMcastTrCtlSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 16, 1, 8),
    _TmnxOamMcastTrCtlSrcAddrType_Type()
)
tmnxOamMcastTrCtlSrcAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMcastTrCtlSrcAddrType.setStatus("current")


class _TmnxOamMcastTrCtlSrcAddress_Type(InetAddress):
    """Custom type tmnxOamMcastTrCtlSrcAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamMcastTrCtlSrcAddress_Type.__name__ = "InetAddress"
_TmnxOamMcastTrCtlSrcAddress_Object = MibTableColumn
tmnxOamMcastTrCtlSrcAddress = _TmnxOamMcastTrCtlSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 16, 1, 9),
    _TmnxOamMcastTrCtlSrcAddress_Type()
)
tmnxOamMcastTrCtlSrcAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMcastTrCtlSrcAddress.setStatus("current")


class _TmnxOamMcastTrCtlDestAddrType_Type(InetAddressType):
    """Custom type tmnxOamMcastTrCtlDestAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxOamMcastTrCtlDestAddrType_Type.__name__ = "InetAddressType"
_TmnxOamMcastTrCtlDestAddrType_Object = MibTableColumn
tmnxOamMcastTrCtlDestAddrType = _TmnxOamMcastTrCtlDestAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 16, 1, 10),
    _TmnxOamMcastTrCtlDestAddrType_Type()
)
tmnxOamMcastTrCtlDestAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMcastTrCtlDestAddrType.setStatus("current")


class _TmnxOamMcastTrCtlDestAddress_Type(InetAddress):
    """Custom type tmnxOamMcastTrCtlDestAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamMcastTrCtlDestAddress_Type.__name__ = "InetAddress"
_TmnxOamMcastTrCtlDestAddress_Object = MibTableColumn
tmnxOamMcastTrCtlDestAddress = _TmnxOamMcastTrCtlDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 16, 1, 11),
    _TmnxOamMcastTrCtlDestAddress_Type()
)
tmnxOamMcastTrCtlDestAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMcastTrCtlDestAddress.setStatus("current")
_TmnxOamMcastTrCtlRespAddrType_Type = InetAddressType
_TmnxOamMcastTrCtlRespAddrType_Object = MibTableColumn
tmnxOamMcastTrCtlRespAddrType = _TmnxOamMcastTrCtlRespAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 16, 1, 12),
    _TmnxOamMcastTrCtlRespAddrType_Type()
)
tmnxOamMcastTrCtlRespAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMcastTrCtlRespAddrType.setStatus("current")


class _TmnxOamMcastTrCtlRespAddress_Type(InetAddress):
    """Custom type tmnxOamMcastTrCtlRespAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamMcastTrCtlRespAddress_Type.__name__ = "InetAddress"
_TmnxOamMcastTrCtlRespAddress_Object = MibTableColumn
tmnxOamMcastTrCtlRespAddress = _TmnxOamMcastTrCtlRespAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 16, 1, 13),
    _TmnxOamMcastTrCtlRespAddress_Type()
)
tmnxOamMcastTrCtlRespAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMcastTrCtlRespAddress.setStatus("current")


class _TmnxOamMcastTrCtlGrpAddrType_Type(InetAddressType):
    """Custom type tmnxOamMcastTrCtlGrpAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxOamMcastTrCtlGrpAddrType_Type.__name__ = "InetAddressType"
_TmnxOamMcastTrCtlGrpAddrType_Object = MibTableColumn
tmnxOamMcastTrCtlGrpAddrType = _TmnxOamMcastTrCtlGrpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 16, 1, 14),
    _TmnxOamMcastTrCtlGrpAddrType_Type()
)
tmnxOamMcastTrCtlGrpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMcastTrCtlGrpAddrType.setStatus("current")


class _TmnxOamMcastTrCtlGrpAddress_Type(InetAddress):
    """Custom type tmnxOamMcastTrCtlGrpAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamMcastTrCtlGrpAddress_Type.__name__ = "InetAddress"
_TmnxOamMcastTrCtlGrpAddress_Object = MibTableColumn
tmnxOamMcastTrCtlGrpAddress = _TmnxOamMcastTrCtlGrpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 16, 1, 15),
    _TmnxOamMcastTrCtlGrpAddress_Type()
)
tmnxOamMcastTrCtlGrpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMcastTrCtlGrpAddress.setStatus("current")


class _TmnxOamMcastTrCtlTestSubMode_Type(Integer32):
    """Custom type tmnxOamMcastTrCtlTestSubMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mcastTraceRouteV1", 1),
          ("mcastTraceRouteV2", 2))
    )


_TmnxOamMcastTrCtlTestSubMode_Type.__name__ = "Integer32"
_TmnxOamMcastTrCtlTestSubMode_Object = MibTableColumn
tmnxOamMcastTrCtlTestSubMode = _TmnxOamMcastTrCtlTestSubMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 16, 1, 16),
    _TmnxOamMcastTrCtlTestSubMode_Type()
)
tmnxOamMcastTrCtlTestSubMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMcastTrCtlTestSubMode.setStatus("current")
_TmnxOamMcastTrRespTable_Object = MibTable
tmnxOamMcastTrRespTable = _TmnxOamMcastTrRespTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 17)
)
if mibBuilder.loadTexts:
    tmnxOamMcastTrRespTable.setStatus("current")
_TmnxOamMcastTrRespEntry_Object = MibTableRow
tmnxOamMcastTrRespEntry = _TmnxOamMcastTrRespEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 17, 1)
)
tmnxOamMcastTrRespEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsTestRunIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryHopIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryProbeIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamMcastTrRespEntry.setStatus("current")
_TmnxOamMcastTrRespQueryArrivalTime_Type = Unsigned32
_TmnxOamMcastTrRespQueryArrivalTime_Object = MibTableColumn
tmnxOamMcastTrRespQueryArrivalTime = _TmnxOamMcastTrRespQueryArrivalTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 17, 1, 1),
    _TmnxOamMcastTrRespQueryArrivalTime_Type()
)
tmnxOamMcastTrRespQueryArrivalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMcastTrRespQueryArrivalTime.setStatus("current")
_TmnxOamMcastTrRespInIfAddr_Type = IpAddress
_TmnxOamMcastTrRespInIfAddr_Object = MibTableColumn
tmnxOamMcastTrRespInIfAddr = _TmnxOamMcastTrRespInIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 17, 1, 2),
    _TmnxOamMcastTrRespInIfAddr_Type()
)
tmnxOamMcastTrRespInIfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMcastTrRespInIfAddr.setStatus("obsolete")
_TmnxOamMcastTrRespOutIfAddr_Type = IpAddress
_TmnxOamMcastTrRespOutIfAddr_Object = MibTableColumn
tmnxOamMcastTrRespOutIfAddr = _TmnxOamMcastTrRespOutIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 17, 1, 3),
    _TmnxOamMcastTrRespOutIfAddr_Type()
)
tmnxOamMcastTrRespOutIfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMcastTrRespOutIfAddr.setStatus("obsolete")
_TmnxOamMcastTrRespPrevHopRtrAddr_Type = IpAddress
_TmnxOamMcastTrRespPrevHopRtrAddr_Object = MibTableColumn
tmnxOamMcastTrRespPrevHopRtrAddr = _TmnxOamMcastTrRespPrevHopRtrAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 17, 1, 4),
    _TmnxOamMcastTrRespPrevHopRtrAddr_Type()
)
tmnxOamMcastTrRespPrevHopRtrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMcastTrRespPrevHopRtrAddr.setStatus("obsolete")
_TmnxOamMcastTrRespInPktCount_Type = Counter32
_TmnxOamMcastTrRespInPktCount_Object = MibTableColumn
tmnxOamMcastTrRespInPktCount = _TmnxOamMcastTrRespInPktCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 17, 1, 5),
    _TmnxOamMcastTrRespInPktCount_Type()
)
tmnxOamMcastTrRespInPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMcastTrRespInPktCount.setStatus("current")
_TmnxOamMcastTrRespOutPktCount_Type = Counter32
_TmnxOamMcastTrRespOutPktCount_Object = MibTableColumn
tmnxOamMcastTrRespOutPktCount = _TmnxOamMcastTrRespOutPktCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 17, 1, 6),
    _TmnxOamMcastTrRespOutPktCount_Type()
)
tmnxOamMcastTrRespOutPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMcastTrRespOutPktCount.setStatus("current")
_TmnxOamMcastTrRespSGPktCount_Type = Counter32
_TmnxOamMcastTrRespSGPktCount_Object = MibTableColumn
tmnxOamMcastTrRespSGPktCount = _TmnxOamMcastTrRespSGPktCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 17, 1, 7),
    _TmnxOamMcastTrRespSGPktCount_Type()
)
tmnxOamMcastTrRespSGPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMcastTrRespSGPktCount.setStatus("current")


class _TmnxOamMcastTrRespRtgProtocol_Type(Integer32):
    """Custom type tmnxOamMcastTrRespRtgProtocol based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("dvmrp", 1),
          ("mospf", 2),
          ("pim", 3),
          ("cbt", 4),
          ("pimSpecial", 5),
          ("pimStatic", 6),
          ("dvmrpStatic", 7),
          ("bgp4Plus", 8),
          ("cbtSpecial", 9),
          ("cbtStatic", 10),
          ("pimAssert", 11))
    )


_TmnxOamMcastTrRespRtgProtocol_Type.__name__ = "Integer32"
_TmnxOamMcastTrRespRtgProtocol_Object = MibTableColumn
tmnxOamMcastTrRespRtgProtocol = _TmnxOamMcastTrRespRtgProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 17, 1, 8),
    _TmnxOamMcastTrRespRtgProtocol_Type()
)
tmnxOamMcastTrRespRtgProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMcastTrRespRtgProtocol.setStatus("current")
_TmnxOamMcastTrRespFwdTtl_Type = Unsigned32
_TmnxOamMcastTrRespFwdTtl_Object = MibTableColumn
tmnxOamMcastTrRespFwdTtl = _TmnxOamMcastTrRespFwdTtl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 17, 1, 9),
    _TmnxOamMcastTrRespFwdTtl_Type()
)
tmnxOamMcastTrRespFwdTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMcastTrRespFwdTtl.setStatus("current")
_TmnxOamMcastTrRespMBZBit_Type = Unsigned32
_TmnxOamMcastTrRespMBZBit_Object = MibTableColumn
tmnxOamMcastTrRespMBZBit = _TmnxOamMcastTrRespMBZBit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 17, 1, 10),
    _TmnxOamMcastTrRespMBZBit_Type()
)
tmnxOamMcastTrRespMBZBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMcastTrRespMBZBit.setStatus("current")
_TmnxOamMcastTrRespSrcBit_Type = Unsigned32
_TmnxOamMcastTrRespSrcBit_Object = MibTableColumn
tmnxOamMcastTrRespSrcBit = _TmnxOamMcastTrRespSrcBit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 17, 1, 11),
    _TmnxOamMcastTrRespSrcBit_Type()
)
tmnxOamMcastTrRespSrcBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMcastTrRespSrcBit.setStatus("current")
_TmnxOamMcastTrRespSrcMask_Type = Unsigned32
_TmnxOamMcastTrRespSrcMask_Object = MibTableColumn
tmnxOamMcastTrRespSrcMask = _TmnxOamMcastTrRespSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 17, 1, 12),
    _TmnxOamMcastTrRespSrcMask_Type()
)
tmnxOamMcastTrRespSrcMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMcastTrRespSrcMask.setStatus("current")


class _TmnxOamMcastTrRespFwdCode_Type(Integer32):
    """Custom type tmnxOamMcastTrRespFwdCode based on Integer32"""
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
              13,
              128,
              129,
              130,
              131,
              132)
        )
    )
    namedValues = NamedValues(
        *(("noError", 0),
          ("wrongIf", 1),
          ("pruneSent", 2),
          ("pruneRecvd", 3),
          ("scoped", 4),
          ("noRoute", 5),
          ("wrongLastHop", 6),
          ("notForwarding", 7),
          ("reachedRP", 8),
          ("rpfIf", 9),
          ("noMulticast", 10),
          ("infoHidden", 11),
          ("reachedGW", 12),
          ("unknownQuery", 13),
          ("fatalError", 128),
          ("noSpace", 129),
          ("oldRouter", 130),
          ("adminProhib", 131),
          ("unknown", 132))
    )


_TmnxOamMcastTrRespFwdCode_Type.__name__ = "Integer32"
_TmnxOamMcastTrRespFwdCode_Object = MibTableColumn
tmnxOamMcastTrRespFwdCode = _TmnxOamMcastTrRespFwdCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 17, 1, 13),
    _TmnxOamMcastTrRespFwdCode_Type()
)
tmnxOamMcastTrRespFwdCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMcastTrRespFwdCode.setStatus("current")
_TmnxOamMcastTrRespInIfAddrType_Type = InetAddressType
_TmnxOamMcastTrRespInIfAddrType_Object = MibTableColumn
tmnxOamMcastTrRespInIfAddrType = _TmnxOamMcastTrRespInIfAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 17, 1, 14),
    _TmnxOamMcastTrRespInIfAddrType_Type()
)
tmnxOamMcastTrRespInIfAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMcastTrRespInIfAddrType.setStatus("current")


class _TmnxOamMcastTrRespInIfAddress_Type(InetAddress):
    """Custom type tmnxOamMcastTrRespInIfAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamMcastTrRespInIfAddress_Type.__name__ = "InetAddress"
_TmnxOamMcastTrRespInIfAddress_Object = MibTableColumn
tmnxOamMcastTrRespInIfAddress = _TmnxOamMcastTrRespInIfAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 17, 1, 15),
    _TmnxOamMcastTrRespInIfAddress_Type()
)
tmnxOamMcastTrRespInIfAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMcastTrRespInIfAddress.setStatus("current")
_TmnxOamMcastTrRespOutIfAddrType_Type = InetAddressType
_TmnxOamMcastTrRespOutIfAddrType_Object = MibTableColumn
tmnxOamMcastTrRespOutIfAddrType = _TmnxOamMcastTrRespOutIfAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 17, 1, 16),
    _TmnxOamMcastTrRespOutIfAddrType_Type()
)
tmnxOamMcastTrRespOutIfAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMcastTrRespOutIfAddrType.setStatus("current")


class _TmnxOamMcastTrRespOutIfAddress_Type(InetAddress):
    """Custom type tmnxOamMcastTrRespOutIfAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamMcastTrRespOutIfAddress_Type.__name__ = "InetAddress"
_TmnxOamMcastTrRespOutIfAddress_Object = MibTableColumn
tmnxOamMcastTrRespOutIfAddress = _TmnxOamMcastTrRespOutIfAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 17, 1, 17),
    _TmnxOamMcastTrRespOutIfAddress_Type()
)
tmnxOamMcastTrRespOutIfAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMcastTrRespOutIfAddress.setStatus("current")
_TmnxOamMcastTrRespPhRtrAddrType_Type = InetAddressType
_TmnxOamMcastTrRespPhRtrAddrType_Object = MibTableColumn
tmnxOamMcastTrRespPhRtrAddrType = _TmnxOamMcastTrRespPhRtrAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 17, 1, 18),
    _TmnxOamMcastTrRespPhRtrAddrType_Type()
)
tmnxOamMcastTrRespPhRtrAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMcastTrRespPhRtrAddrType.setStatus("current")


class _TmnxOamMcastTrRespPhRtrAddress_Type(InetAddress):
    """Custom type tmnxOamMcastTrRespPhRtrAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamMcastTrRespPhRtrAddress_Type.__name__ = "InetAddress"
_TmnxOamMcastTrRespPhRtrAddress_Object = MibTableColumn
tmnxOamMcastTrRespPhRtrAddress = _TmnxOamMcastTrRespPhRtrAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 17, 1, 19),
    _TmnxOamMcastTrRespPhRtrAddress_Type()
)
tmnxOamMcastTrRespPhRtrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMcastTrRespPhRtrAddress.setStatus("current")
_TmnxOamMcastTrRespInPktCountHC_Type = Counter64
_TmnxOamMcastTrRespInPktCountHC_Object = MibTableColumn
tmnxOamMcastTrRespInPktCountHC = _TmnxOamMcastTrRespInPktCountHC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 17, 1, 20),
    _TmnxOamMcastTrRespInPktCountHC_Type()
)
tmnxOamMcastTrRespInPktCountHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMcastTrRespInPktCountHC.setStatus("current")
_TmnxOamMcastTrRespOutPktCountHC_Type = Counter64
_TmnxOamMcastTrRespOutPktCountHC_Object = MibTableColumn
tmnxOamMcastTrRespOutPktCountHC = _TmnxOamMcastTrRespOutPktCountHC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 17, 1, 21),
    _TmnxOamMcastTrRespOutPktCountHC_Type()
)
tmnxOamMcastTrRespOutPktCountHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMcastTrRespOutPktCountHC.setStatus("current")
_TmnxOamMcastTrRespSGPktCountHC_Type = Counter64
_TmnxOamMcastTrRespSGPktCountHC_Object = MibTableColumn
tmnxOamMcastTrRespSGPktCountHC = _TmnxOamMcastTrRespSGPktCountHC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 17, 1, 22),
    _TmnxOamMcastTrRespSGPktCountHC_Type()
)
tmnxOamMcastTrRespSGPktCountHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMcastTrRespSGPktCountHC.setStatus("current")


class _TmnxOamMcastTrRespRtgProtocol2_Type(Integer32):
    """Custom type tmnxOamMcastTrRespRtgProtocol2 based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("other", 1),
          ("local", 2),
          ("netmgmt", 3),
          ("icmp", 4),
          ("egp", 5),
          ("ggp", 6),
          ("hello", 7),
          ("rip", 8),
          ("isIs", 9),
          ("esIs", 10),
          ("ciscoIgrp", 11),
          ("bbnSpfIgp", 12),
          ("ospf", 13),
          ("bgp", 14),
          ("idpr", 15),
          ("ciscoEigrp", 16),
          ("dvmrp", 17),
          ("rpl", 18),
          ("dhcp", 19),
          ("ttdp", 20))
    )


_TmnxOamMcastTrRespRtgProtocol2_Type.__name__ = "Integer32"
_TmnxOamMcastTrRespRtgProtocol2_Object = MibTableColumn
tmnxOamMcastTrRespRtgProtocol2 = _TmnxOamMcastTrRespRtgProtocol2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 17, 1, 23),
    _TmnxOamMcastTrRespRtgProtocol2_Type()
)
tmnxOamMcastTrRespRtgProtocol2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMcastTrRespRtgProtocol2.setStatus("current")


class _TmnxOamMcastTrRespMcastRtgProto_Type(Integer32):
    """Custom type tmnxOamMcastTrRespMcastRtgProto based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("other", 1),
          ("local", 2),
          ("netmgmt", 3),
          ("dvmrp", 4),
          ("mospf", 5),
          ("pimSparseDense", 6),
          ("cbt", 7),
          ("pimSparseMode", 8),
          ("pimDenseMode", 9),
          ("igmpOnly", 10),
          ("bgmp", 11),
          ("msdp", 12))
    )


_TmnxOamMcastTrRespMcastRtgProto_Type.__name__ = "Integer32"
_TmnxOamMcastTrRespMcastRtgProto_Object = MibTableColumn
tmnxOamMcastTrRespMcastRtgProto = _TmnxOamMcastTrRespMcastRtgProto_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 17, 1, 24),
    _TmnxOamMcastTrRespMcastRtgProto_Type()
)
tmnxOamMcastTrRespMcastRtgProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMcastTrRespMcastRtgProto.setStatus("current")
_TmnxOamMcastTrRespInIfIndex_Type = Unsigned32
_TmnxOamMcastTrRespInIfIndex_Object = MibTableColumn
tmnxOamMcastTrRespInIfIndex = _TmnxOamMcastTrRespInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 17, 1, 25),
    _TmnxOamMcastTrRespInIfIndex_Type()
)
tmnxOamMcastTrRespInIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMcastTrRespInIfIndex.setStatus("current")
_TmnxOamMcastTrRespOutIfIndex_Type = Unsigned32
_TmnxOamMcastTrRespOutIfIndex_Object = MibTableColumn
tmnxOamMcastTrRespOutIfIndex = _TmnxOamMcastTrRespOutIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 17, 1, 26),
    _TmnxOamMcastTrRespOutIfIndex_Type()
)
tmnxOamMcastTrRespOutIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMcastTrRespOutIfIndex.setStatus("current")
_TmnxOamMcastTrRespLocalAddrType_Type = InetAddressType
_TmnxOamMcastTrRespLocalAddrType_Object = MibTableColumn
tmnxOamMcastTrRespLocalAddrType = _TmnxOamMcastTrRespLocalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 17, 1, 27),
    _TmnxOamMcastTrRespLocalAddrType_Type()
)
tmnxOamMcastTrRespLocalAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMcastTrRespLocalAddrType.setStatus("current")


class _TmnxOamMcastTrRespLocalAddress_Type(InetAddress):
    """Custom type tmnxOamMcastTrRespLocalAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamMcastTrRespLocalAddress_Type.__name__ = "InetAddress"
_TmnxOamMcastTrRespLocalAddress_Object = MibTableColumn
tmnxOamMcastTrRespLocalAddress = _TmnxOamMcastTrRespLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 17, 1, 28),
    _TmnxOamMcastTrRespLocalAddress_Type()
)
tmnxOamMcastTrRespLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMcastTrRespLocalAddress.setStatus("current")
_TmnxOamLTtraceCtlTable_Object = MibTable
tmnxOamLTtraceCtlTable = _TmnxOamLTtraceCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 18)
)
if mibBuilder.loadTexts:
    tmnxOamLTtraceCtlTable.setStatus("current")
_TmnxOamLTtraceCtlEntry_Object = MibTableRow
tmnxOamLTtraceCtlEntry = _TmnxOamLTtraceCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 18, 1)
)
tmnxOamLTtraceCtlEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamLTtraceCtlEntry.setStatus("current")


class _TmnxOamLTtraceCtlLdpPrefixType_Type(InetAddressType):
    """Custom type tmnxOamLTtraceCtlLdpPrefixType based on InetAddressType"""
    defaultValue = 0


_TmnxOamLTtraceCtlLdpPrefixType_Type.__name__ = "InetAddressType"
_TmnxOamLTtraceCtlLdpPrefixType_Object = MibTableColumn
tmnxOamLTtraceCtlLdpPrefixType = _TmnxOamLTtraceCtlLdpPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 18, 1, 2),
    _TmnxOamLTtraceCtlLdpPrefixType_Type()
)
tmnxOamLTtraceCtlLdpPrefixType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLTtraceCtlLdpPrefixType.setStatus("current")


class _TmnxOamLTtraceCtlLdpPrefix_Type(InetAddress):
    """Custom type tmnxOamLTtraceCtlLdpPrefix based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamLTtraceCtlLdpPrefix_Type.__name__ = "InetAddress"
_TmnxOamLTtraceCtlLdpPrefix_Object = MibTableColumn
tmnxOamLTtraceCtlLdpPrefix = _TmnxOamLTtraceCtlLdpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 18, 1, 3),
    _TmnxOamLTtraceCtlLdpPrefix_Type()
)
tmnxOamLTtraceCtlLdpPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLTtraceCtlLdpPrefix.setStatus("current")


class _TmnxOamLTtraceCtlLdpPrefixLen_Type(InetAddressPrefixLength):
    """Custom type tmnxOamLTtraceCtlLdpPrefixLen based on InetAddressPrefixLength"""
    defaultValue = 32


_TmnxOamLTtraceCtlLdpPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxOamLTtraceCtlLdpPrefixLen_Object = MibTableColumn
tmnxOamLTtraceCtlLdpPrefixLen = _TmnxOamLTtraceCtlLdpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 18, 1, 4),
    _TmnxOamLTtraceCtlLdpPrefixLen_Type()
)
tmnxOamLTtraceCtlLdpPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLTtraceCtlLdpPrefixLen.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamLTtraceCtlLdpPrefixLen.setUnits("bits")


class _TmnxOamLTtraceCtlMaxPath_Type(Unsigned32):
    """Custom type tmnxOamLTtraceCtlMaxPath based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TmnxOamLTtraceCtlMaxPath_Type.__name__ = "Unsigned32"
_TmnxOamLTtraceCtlMaxPath_Object = MibTableColumn
tmnxOamLTtraceCtlMaxPath = _TmnxOamLTtraceCtlMaxPath_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 18, 1, 5),
    _TmnxOamLTtraceCtlMaxPath_Type()
)
tmnxOamLTtraceCtlMaxPath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLTtraceCtlMaxPath.setStatus("current")
_TmnxOamLTtraceCtlDownstreamMpTlv_Type = TmnxOamMplsEchoDownMapTlv
_TmnxOamLTtraceCtlDownstreamMpTlv_Object = MibTableColumn
tmnxOamLTtraceCtlDownstreamMpTlv = _TmnxOamLTtraceCtlDownstreamMpTlv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 18, 1, 6),
    _TmnxOamLTtraceCtlDownstreamMpTlv_Type()
)
tmnxOamLTtraceCtlDownstreamMpTlv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLTtraceCtlDownstreamMpTlv.setStatus("current")
_TmnxOamLTtraceMaxConRequests_Type = Unsigned32
_TmnxOamLTtraceMaxConRequests_Object = MibScalar
tmnxOamLTtraceMaxConRequests = _TmnxOamLTtraceMaxConRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 19),
    _TmnxOamLTtraceMaxConRequests_Type()
)
tmnxOamLTtraceMaxConRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceMaxConRequests.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamLTtraceMaxConRequests.setUnits("requests")
_TmnxOamLTtraceResultsTable_Object = MibTable
tmnxOamLTtraceResultsTable = _TmnxOamLTtraceResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 20)
)
if mibBuilder.loadTexts:
    tmnxOamLTtraceResultsTable.setStatus("current")
_TmnxOamLTtraceResultsEntry_Object = MibTableRow
tmnxOamLTtraceResultsEntry = _TmnxOamLTtraceResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 20, 1)
)
tmnxOamLTtraceResultsEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamLTtraceResultsEntry.setStatus("current")
_TmnxOamLTtraceResultsDisPaths_Type = Unsigned32
_TmnxOamLTtraceResultsDisPaths_Object = MibTableColumn
tmnxOamLTtraceResultsDisPaths = _TmnxOamLTtraceResultsDisPaths_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 20, 1, 2),
    _TmnxOamLTtraceResultsDisPaths_Type()
)
tmnxOamLTtraceResultsDisPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceResultsDisPaths.setStatus("current")
_TmnxOamLTtraceResultsFailedHops_Type = Unsigned32
_TmnxOamLTtraceResultsFailedHops_Object = MibTableColumn
tmnxOamLTtraceResultsFailedHops = _TmnxOamLTtraceResultsFailedHops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 20, 1, 3),
    _TmnxOamLTtraceResultsFailedHops_Type()
)
tmnxOamLTtraceResultsFailedHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceResultsFailedHops.setStatus("current")


class _TmnxOamLTtraceResultsDisState_Type(Integer32):
    """Custom type tmnxOamLTtraceResultsDisState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("initial", 0),
          ("inProgress", 1),
          ("done", 2))
    )


_TmnxOamLTtraceResultsDisState_Type.__name__ = "Integer32"
_TmnxOamLTtraceResultsDisState_Object = MibTableColumn
tmnxOamLTtraceResultsDisState = _TmnxOamLTtraceResultsDisState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 20, 1, 4),
    _TmnxOamLTtraceResultsDisState_Type()
)
tmnxOamLTtraceResultsDisState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceResultsDisState.setStatus("current")
_TmnxOamLTtraceResultsDisStatus_Type = TmnxOamLTtraceDisStatusBits
_TmnxOamLTtraceResultsDisStatus_Object = MibTableColumn
tmnxOamLTtraceResultsDisStatus = _TmnxOamLTtraceResultsDisStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 20, 1, 5),
    _TmnxOamLTtraceResultsDisStatus_Type()
)
tmnxOamLTtraceResultsDisStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceResultsDisStatus.setStatus("current")
_TmnxOamLTtraceHopInfoTable_Object = MibTable
tmnxOamLTtraceHopInfoTable = _TmnxOamLTtraceHopInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 21)
)
if mibBuilder.loadTexts:
    tmnxOamLTtraceHopInfoTable.setStatus("current")
_TmnxOamLTtraceHopInfoEntry_Object = MibTableRow
tmnxOamLTtraceHopInfoEntry = _TmnxOamLTtraceHopInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 21, 1)
)
tmnxOamLTtraceHopInfoEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceHopIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamLTtraceHopInfoEntry.setStatus("current")
_TmnxOamLTtraceHopIndex_Type = Unsigned32
_TmnxOamLTtraceHopIndex_Object = MibTableColumn
tmnxOamLTtraceHopIndex = _TmnxOamLTtraceHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 21, 1, 1),
    _TmnxOamLTtraceHopIndex_Type()
)
tmnxOamLTtraceHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamLTtraceHopIndex.setStatus("current")
_TmnxOamLTtraceUpStreamHopIndex_Type = Unsigned32
_TmnxOamLTtraceUpStreamHopIndex_Object = MibTableColumn
tmnxOamLTtraceUpStreamHopIndex = _TmnxOamLTtraceUpStreamHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 21, 1, 2),
    _TmnxOamLTtraceUpStreamHopIndex_Type()
)
tmnxOamLTtraceUpStreamHopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceUpStreamHopIndex.setStatus("current")
_TmnxOamLTtraceHopAddrType_Type = InetAddressType
_TmnxOamLTtraceHopAddrType_Object = MibTableColumn
tmnxOamLTtraceHopAddrType = _TmnxOamLTtraceHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 21, 1, 3),
    _TmnxOamLTtraceHopAddrType_Type()
)
tmnxOamLTtraceHopAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceHopAddrType.setStatus("current")


class _TmnxOamLTtraceHopAddr_Type(InetAddress):
    """Custom type tmnxOamLTtraceHopAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamLTtraceHopAddr_Type.__name__ = "InetAddress"
_TmnxOamLTtraceHopAddr_Object = MibTableColumn
tmnxOamLTtraceHopAddr = _TmnxOamLTtraceHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 21, 1, 4),
    _TmnxOamLTtraceHopAddr_Type()
)
tmnxOamLTtraceHopAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceHopAddr.setStatus("current")
_TmnxOamLTtraceHopDstAddrType_Type = InetAddressType
_TmnxOamLTtraceHopDstAddrType_Object = MibTableColumn
tmnxOamLTtraceHopDstAddrType = _TmnxOamLTtraceHopDstAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 21, 1, 5),
    _TmnxOamLTtraceHopDstAddrType_Type()
)
tmnxOamLTtraceHopDstAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceHopDstAddrType.setStatus("current")


class _TmnxOamLTtraceHopDstAddr_Type(InetAddress):
    """Custom type tmnxOamLTtraceHopDstAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamLTtraceHopDstAddr_Type.__name__ = "InetAddress"
_TmnxOamLTtraceHopDstAddr_Object = MibTableColumn
tmnxOamLTtraceHopDstAddr = _TmnxOamLTtraceHopDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 21, 1, 6),
    _TmnxOamLTtraceHopDstAddr_Type()
)
tmnxOamLTtraceHopDstAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceHopDstAddr.setStatus("current")
_TmnxOamLTtraceHopEgrNhAddrType_Type = InetAddressType
_TmnxOamLTtraceHopEgrNhAddrType_Object = MibTableColumn
tmnxOamLTtraceHopEgrNhAddrType = _TmnxOamLTtraceHopEgrNhAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 21, 1, 7),
    _TmnxOamLTtraceHopEgrNhAddrType_Type()
)
tmnxOamLTtraceHopEgrNhAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceHopEgrNhAddrType.setStatus("current")


class _TmnxOamLTtraceHopEgrNhAddr_Type(InetAddress):
    """Custom type tmnxOamLTtraceHopEgrNhAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamLTtraceHopEgrNhAddr_Type.__name__ = "InetAddress"
_TmnxOamLTtraceHopEgrNhAddr_Object = MibTableColumn
tmnxOamLTtraceHopEgrNhAddr = _TmnxOamLTtraceHopEgrNhAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 21, 1, 8),
    _TmnxOamLTtraceHopEgrNhAddr_Type()
)
tmnxOamLTtraceHopEgrNhAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceHopEgrNhAddr.setStatus("current")
_TmnxOamLTtraceHopDisTtl_Type = Unsigned32
_TmnxOamLTtraceHopDisTtl_Object = MibTableColumn
tmnxOamLTtraceHopDisTtl = _TmnxOamLTtraceHopDisTtl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 21, 1, 9),
    _TmnxOamLTtraceHopDisTtl_Type()
)
tmnxOamLTtraceHopDisTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceHopDisTtl.setStatus("current")
_TmnxOamLTtraceHopLastRc_Type = TmnxOamPingRtnCode
_TmnxOamLTtraceHopLastRc_Object = MibTableColumn
tmnxOamLTtraceHopLastRc = _TmnxOamLTtraceHopLastRc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 21, 1, 10),
    _TmnxOamLTtraceHopLastRc_Type()
)
tmnxOamLTtraceHopLastRc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceHopLastRc.setStatus("current")


class _TmnxOamLTtraceHopDiscoveryState_Type(Integer32):
    """Custom type tmnxOamLTtraceHopDiscoveryState based on Integer32"""
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
        *(("inProgress", 0),
          ("doneOk", 1),
          ("doneTimeout", 2),
          ("doneLoopDetected", 3),
          ("doneExpiredTtl", 4))
    )


_TmnxOamLTtraceHopDiscoveryState_Type.__name__ = "Integer32"
_TmnxOamLTtraceHopDiscoveryState_Object = MibTableColumn
tmnxOamLTtraceHopDiscoveryState = _TmnxOamLTtraceHopDiscoveryState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 21, 1, 11),
    _TmnxOamLTtraceHopDiscoveryState_Type()
)
tmnxOamLTtraceHopDiscoveryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceHopDiscoveryState.setStatus("current")
_TmnxOamLTtraceHopDiscoveryTime_Type = TimeStamp
_TmnxOamLTtraceHopDiscoveryTime_Object = MibTableColumn
tmnxOamLTtraceHopDiscoveryTime = _TmnxOamLTtraceHopDiscoveryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 21, 1, 12),
    _TmnxOamLTtraceHopDiscoveryTime_Type()
)
tmnxOamLTtraceHopDiscoveryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceHopDiscoveryTime.setStatus("current")
_TmnxOamLTtraceHopLabel1_Type = MplsLabel
_TmnxOamLTtraceHopLabel1_Object = MibTableColumn
tmnxOamLTtraceHopLabel1 = _TmnxOamLTtraceHopLabel1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 21, 1, 13),
    _TmnxOamLTtraceHopLabel1_Type()
)
tmnxOamLTtraceHopLabel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceHopLabel1.setStatus("current")
_TmnxOamLTtraceHopLabel2_Type = MplsLabel
_TmnxOamLTtraceHopLabel2_Object = MibTableColumn
tmnxOamLTtraceHopLabel2 = _TmnxOamLTtraceHopLabel2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 21, 1, 14),
    _TmnxOamLTtraceHopLabel2_Type()
)
tmnxOamLTtraceHopLabel2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceHopLabel2.setStatus("current")
_TmnxOamLTtraceHopLabel3_Type = MplsLabel
_TmnxOamLTtraceHopLabel3_Object = MibTableColumn
tmnxOamLTtraceHopLabel3 = _TmnxOamLTtraceHopLabel3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 21, 1, 15),
    _TmnxOamLTtraceHopLabel3_Type()
)
tmnxOamLTtraceHopLabel3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceHopLabel3.setStatus("current")
_TmnxOamLTtraceHopLabel4_Type = MplsLabel
_TmnxOamLTtraceHopLabel4_Object = MibTableColumn
tmnxOamLTtraceHopLabel4 = _TmnxOamLTtraceHopLabel4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 21, 1, 16),
    _TmnxOamLTtraceHopLabel4_Type()
)
tmnxOamLTtraceHopLabel4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceHopLabel4.setStatus("current")
_TmnxOamLTtraceHopLabel5_Type = MplsLabel
_TmnxOamLTtraceHopLabel5_Object = MibTableColumn
tmnxOamLTtraceHopLabel5 = _TmnxOamLTtraceHopLabel5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 21, 1, 17),
    _TmnxOamLTtraceHopLabel5_Type()
)
tmnxOamLTtraceHopLabel5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceHopLabel5.setStatus("current")
_TmnxOamLTtraceHopLabel6_Type = MplsLabel
_TmnxOamLTtraceHopLabel6_Object = MibTableColumn
tmnxOamLTtraceHopLabel6 = _TmnxOamLTtraceHopLabel6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 21, 1, 18),
    _TmnxOamLTtraceHopLabel6_Type()
)
tmnxOamLTtraceHopLabel6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceHopLabel6.setStatus("current")
_TmnxOamLTtraceHopIfAddrType_Type = InetAddressType
_TmnxOamLTtraceHopIfAddrType_Object = MibTableColumn
tmnxOamLTtraceHopIfAddrType = _TmnxOamLTtraceHopIfAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 21, 1, 19),
    _TmnxOamLTtraceHopIfAddrType_Type()
)
tmnxOamLTtraceHopIfAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceHopIfAddrType.setStatus("current")


class _TmnxOamLTtraceHopIfAddress_Type(InetAddress):
    """Custom type tmnxOamLTtraceHopIfAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamLTtraceHopIfAddress_Type.__name__ = "InetAddress"
_TmnxOamLTtraceHopIfAddress_Object = MibTableColumn
tmnxOamLTtraceHopIfAddress = _TmnxOamLTtraceHopIfAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 21, 1, 20),
    _TmnxOamLTtraceHopIfAddress_Type()
)
tmnxOamLTtraceHopIfAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceHopIfAddress.setStatus("current")
_TmnxOamLTtraceHopRouterIdType_Type = InetAddressType
_TmnxOamLTtraceHopRouterIdType_Object = MibTableColumn
tmnxOamLTtraceHopRouterIdType = _TmnxOamLTtraceHopRouterIdType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 21, 1, 21),
    _TmnxOamLTtraceHopRouterIdType_Type()
)
tmnxOamLTtraceHopRouterIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceHopRouterIdType.setStatus("current")


class _TmnxOamLTtraceHopRouterId_Type(InetAddress):
    """Custom type tmnxOamLTtraceHopRouterId based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamLTtraceHopRouterId_Type.__name__ = "InetAddress"
_TmnxOamLTtraceHopRouterId_Object = MibTableColumn
tmnxOamLTtraceHopRouterId = _TmnxOamLTtraceHopRouterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 21, 1, 22),
    _TmnxOamLTtraceHopRouterId_Type()
)
tmnxOamLTtraceHopRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceHopRouterId.setStatus("current")
_TmnxOamLTtraceAutoConfigTable_Object = MibTable
tmnxOamLTtraceAutoConfigTable = _TmnxOamLTtraceAutoConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 22)
)
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoConfigTable.setStatus("current")
_TmnxOamLTtraceAutoConfigEntry_Object = MibTableRow
tmnxOamLTtraceAutoConfigEntry = _TmnxOamLTtraceAutoConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 22, 1)
)
tmnxOamLTtraceAutoConfigEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
)
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoConfigEntry.setStatus("current")
_TmnxOamLTtraceAutoRowStatus_Type = RowStatus
_TmnxOamLTtraceAutoRowStatus_Object = MibTableColumn
tmnxOamLTtraceAutoRowStatus = _TmnxOamLTtraceAutoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 22, 1, 1),
    _TmnxOamLTtraceAutoRowStatus_Type()
)
tmnxOamLTtraceAutoRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoRowStatus.setStatus("current")
_TmnxOamLTtraceAutoLastChanged_Type = TimeStamp
_TmnxOamLTtraceAutoLastChanged_Object = MibTableColumn
tmnxOamLTtraceAutoLastChanged = _TmnxOamLTtraceAutoLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 22, 1, 2),
    _TmnxOamLTtraceAutoLastChanged_Type()
)
tmnxOamLTtraceAutoLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoLastChanged.setStatus("current")


class _TmnxOamLTtraceAutoStorageType_Type(StorageType):
    """Custom type tmnxOamLTtraceAutoStorageType based on StorageType"""
    defaultValue = 2


_TmnxOamLTtraceAutoStorageType_Type.__name__ = "StorageType"
_TmnxOamLTtraceAutoStorageType_Object = MibTableColumn
tmnxOamLTtraceAutoStorageType = _TmnxOamLTtraceAutoStorageType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 22, 1, 3),
    _TmnxOamLTtraceAutoStorageType_Type()
)
tmnxOamLTtraceAutoStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoStorageType.setStatus("obsolete")


class _TmnxOamLTtraceAutoAdminState_Type(TmnxAdminState):
    """Custom type tmnxOamLTtraceAutoAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxOamLTtraceAutoAdminState_Type.__name__ = "TmnxAdminState"
_TmnxOamLTtraceAutoAdminState_Object = MibTableColumn
tmnxOamLTtraceAutoAdminState = _TmnxOamLTtraceAutoAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 22, 1, 4),
    _TmnxOamLTtraceAutoAdminState_Type()
)
tmnxOamLTtraceAutoAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoAdminState.setStatus("current")


class _TmnxOamLTtraceAutoFcName_Type(TFCName):
    """Custom type tmnxOamLTtraceAutoFcName based on TFCName"""
    defaultValue = OctetString("be")


_TmnxOamLTtraceAutoFcName_Type.__name__ = "TFCName"
_TmnxOamLTtraceAutoFcName_Object = MibTableColumn
tmnxOamLTtraceAutoFcName = _TmnxOamLTtraceAutoFcName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 22, 1, 5),
    _TmnxOamLTtraceAutoFcName_Type()
)
tmnxOamLTtraceAutoFcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoFcName.setStatus("current")


class _TmnxOamLTtraceAutoProfile_Type(TProfile):
    """Custom type tmnxOamLTtraceAutoProfile based on TProfile"""
    defaultValue = 2


_TmnxOamLTtraceAutoProfile_Type.__name__ = "TProfile"
_TmnxOamLTtraceAutoProfile_Object = MibTableColumn
tmnxOamLTtraceAutoProfile = _TmnxOamLTtraceAutoProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 22, 1, 6),
    _TmnxOamLTtraceAutoProfile_Type()
)
tmnxOamLTtraceAutoProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoProfile.setStatus("current")


class _TmnxOamLTtraceAutoDiscIntvl_Type(Unsigned32):
    """Custom type tmnxOamLTtraceAutoDiscIntvl based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 1440),
    )


_TmnxOamLTtraceAutoDiscIntvl_Type.__name__ = "Unsigned32"
_TmnxOamLTtraceAutoDiscIntvl_Object = MibTableColumn
tmnxOamLTtraceAutoDiscIntvl = _TmnxOamLTtraceAutoDiscIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 22, 1, 7),
    _TmnxOamLTtraceAutoDiscIntvl_Type()
)
tmnxOamLTtraceAutoDiscIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoDiscIntvl.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoDiscIntvl.setUnits("minutes")


class _TmnxOamLTtraceAutoMaxPath_Type(Unsigned32):
    """Custom type tmnxOamLTtraceAutoMaxPath based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_TmnxOamLTtraceAutoMaxPath_Type.__name__ = "Unsigned32"
_TmnxOamLTtraceAutoMaxPath_Object = MibTableColumn
tmnxOamLTtraceAutoMaxPath = _TmnxOamLTtraceAutoMaxPath_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 22, 1, 8),
    _TmnxOamLTtraceAutoMaxPath_Type()
)
tmnxOamLTtraceAutoMaxPath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoMaxPath.setStatus("current")


class _TmnxOamLTtraceAutoTrMaxTtl_Type(Unsigned32):
    """Custom type tmnxOamLTtraceAutoTrMaxTtl based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TmnxOamLTtraceAutoTrMaxTtl_Type.__name__ = "Unsigned32"
_TmnxOamLTtraceAutoTrMaxTtl_Object = MibTableColumn
tmnxOamLTtraceAutoTrMaxTtl = _TmnxOamLTtraceAutoTrMaxTtl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 22, 1, 9),
    _TmnxOamLTtraceAutoTrMaxTtl_Type()
)
tmnxOamLTtraceAutoTrMaxTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoTrMaxTtl.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoTrMaxTtl.setUnits("time-to-live value")


class _TmnxOamLTtraceAutoTrTimeOut_Type(Unsigned32):
    """Custom type tmnxOamLTtraceAutoTrTimeOut based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TmnxOamLTtraceAutoTrTimeOut_Type.__name__ = "Unsigned32"
_TmnxOamLTtraceAutoTrTimeOut_Object = MibTableColumn
tmnxOamLTtraceAutoTrTimeOut = _TmnxOamLTtraceAutoTrTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 22, 1, 10),
    _TmnxOamLTtraceAutoTrTimeOut_Type()
)
tmnxOamLTtraceAutoTrTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoTrTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoTrTimeOut.setUnits("seconds")


class _TmnxOamLTtraceAutoTrMaxFailures_Type(Unsigned32):
    """Custom type tmnxOamLTtraceAutoTrMaxFailures based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TmnxOamLTtraceAutoTrMaxFailures_Type.__name__ = "Unsigned32"
_TmnxOamLTtraceAutoTrMaxFailures_Object = MibTableColumn
tmnxOamLTtraceAutoTrMaxFailures = _TmnxOamLTtraceAutoTrMaxFailures_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 22, 1, 11),
    _TmnxOamLTtraceAutoTrMaxFailures_Type()
)
tmnxOamLTtraceAutoTrMaxFailures.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoTrMaxFailures.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoTrMaxFailures.setUnits("timeouts")


class _TmnxOamLTtraceAutoPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxOamLTtraceAutoPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxOamLTtraceAutoPolicy1_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxOamLTtraceAutoPolicy1_Object = MibTableColumn
tmnxOamLTtraceAutoPolicy1 = _TmnxOamLTtraceAutoPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 22, 1, 12),
    _TmnxOamLTtraceAutoPolicy1_Type()
)
tmnxOamLTtraceAutoPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoPolicy1.setStatus("current")


class _TmnxOamLTtraceAutoPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxOamLTtraceAutoPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxOamLTtraceAutoPolicy2_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxOamLTtraceAutoPolicy2_Object = MibTableColumn
tmnxOamLTtraceAutoPolicy2 = _TmnxOamLTtraceAutoPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 22, 1, 13),
    _TmnxOamLTtraceAutoPolicy2_Type()
)
tmnxOamLTtraceAutoPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoPolicy2.setStatus("current")


class _TmnxOamLTtraceAutoPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxOamLTtraceAutoPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxOamLTtraceAutoPolicy3_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxOamLTtraceAutoPolicy3_Object = MibTableColumn
tmnxOamLTtraceAutoPolicy3 = _TmnxOamLTtraceAutoPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 22, 1, 14),
    _TmnxOamLTtraceAutoPolicy3_Type()
)
tmnxOamLTtraceAutoPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoPolicy3.setStatus("current")


class _TmnxOamLTtraceAutoPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxOamLTtraceAutoPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxOamLTtraceAutoPolicy4_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxOamLTtraceAutoPolicy4_Object = MibTableColumn
tmnxOamLTtraceAutoPolicy4 = _TmnxOamLTtraceAutoPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 22, 1, 15),
    _TmnxOamLTtraceAutoPolicy4_Type()
)
tmnxOamLTtraceAutoPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoPolicy4.setStatus("current")


class _TmnxOamLTtraceAutoPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxOamLTtraceAutoPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxOamLTtraceAutoPolicy5_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxOamLTtraceAutoPolicy5_Object = MibTableColumn
tmnxOamLTtraceAutoPolicy5 = _TmnxOamLTtraceAutoPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 22, 1, 16),
    _TmnxOamLTtraceAutoPolicy5_Type()
)
tmnxOamLTtraceAutoPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoPolicy5.setStatus("current")


class _TmnxOamLTtraceAutoProbeIntvl_Type(Unsigned32):
    """Custom type tmnxOamLTtraceAutoProbeIntvl based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TmnxOamLTtraceAutoProbeIntvl_Type.__name__ = "Unsigned32"
_TmnxOamLTtraceAutoProbeIntvl_Object = MibTableColumn
tmnxOamLTtraceAutoProbeIntvl = _TmnxOamLTtraceAutoProbeIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 22, 1, 17),
    _TmnxOamLTtraceAutoProbeIntvl_Type()
)
tmnxOamLTtraceAutoProbeIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoProbeIntvl.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoProbeIntvl.setUnits("minutes")


class _TmnxOamLTtraceAutoPrTimeOut_Type(Unsigned32):
    """Custom type tmnxOamLTtraceAutoPrTimeOut based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_TmnxOamLTtraceAutoPrTimeOut_Type.__name__ = "Unsigned32"
_TmnxOamLTtraceAutoPrTimeOut_Object = MibTableColumn
tmnxOamLTtraceAutoPrTimeOut = _TmnxOamLTtraceAutoPrTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 22, 1, 18),
    _TmnxOamLTtraceAutoPrTimeOut_Type()
)
tmnxOamLTtraceAutoPrTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoPrTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoPrTimeOut.setUnits("minutes")


class _TmnxOamLTtraceAutoPrMaxFailures_Type(Unsigned32):
    """Custom type tmnxOamLTtraceAutoPrMaxFailures based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TmnxOamLTtraceAutoPrMaxFailures_Type.__name__ = "Unsigned32"
_TmnxOamLTtraceAutoPrMaxFailures_Object = MibTableColumn
tmnxOamLTtraceAutoPrMaxFailures = _TmnxOamLTtraceAutoPrMaxFailures_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 22, 1, 19),
    _TmnxOamLTtraceAutoPrMaxFailures_Type()
)
tmnxOamLTtraceAutoPrMaxFailures.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoPrMaxFailures.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoPrMaxFailures.setUnits("timeouts")
_TmnxOamLTtraceAutoStatusTable_Object = MibTable
tmnxOamLTtraceAutoStatusTable = _TmnxOamLTtraceAutoStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 23)
)
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoStatusTable.setStatus("current")
_TmnxOamLTtraceAutoStatusEntry_Object = MibTableRow
tmnxOamLTtraceAutoStatusEntry = _TmnxOamLTtraceAutoStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 23, 1)
)
tmnxOamLTtraceAutoStatusEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
)
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoStatusEntry.setStatus("current")


class _TmnxOamLTtraceAutoDiscoveryState_Type(Integer32):
    """Custom type tmnxOamLTtraceAutoDiscoveryState based on Integer32"""
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
        *(("initial", 0),
          ("inProgress", 1),
          ("done", 2),
          ("halt", 3))
    )


_TmnxOamLTtraceAutoDiscoveryState_Type.__name__ = "Integer32"
_TmnxOamLTtraceAutoDiscoveryState_Object = MibTableColumn
tmnxOamLTtraceAutoDiscoveryState = _TmnxOamLTtraceAutoDiscoveryState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 23, 1, 1),
    _TmnxOamLTtraceAutoDiscoveryState_Type()
)
tmnxOamLTtraceAutoDiscoveryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoDiscoveryState.setStatus("current")
_TmnxOamLTtraceAutoTotalFecs_Type = Unsigned32
_TmnxOamLTtraceAutoTotalFecs_Object = MibTableColumn
tmnxOamLTtraceAutoTotalFecs = _TmnxOamLTtraceAutoTotalFecs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 23, 1, 2),
    _TmnxOamLTtraceAutoTotalFecs_Type()
)
tmnxOamLTtraceAutoTotalFecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoTotalFecs.setStatus("current")
_TmnxOamLTtraceAutoDisFecs_Type = Unsigned32
_TmnxOamLTtraceAutoDisFecs_Object = MibTableColumn
tmnxOamLTtraceAutoDisFecs = _TmnxOamLTtraceAutoDisFecs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 23, 1, 3),
    _TmnxOamLTtraceAutoDisFecs_Type()
)
tmnxOamLTtraceAutoDisFecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoDisFecs.setStatus("current")
_TmnxOamLTtraceAutoLastDisStart_Type = TimeStamp
_TmnxOamLTtraceAutoLastDisStart_Object = MibTableColumn
tmnxOamLTtraceAutoLastDisStart = _TmnxOamLTtraceAutoLastDisStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 23, 1, 4),
    _TmnxOamLTtraceAutoLastDisStart_Type()
)
tmnxOamLTtraceAutoLastDisStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoLastDisStart.setStatus("current")
_TmnxOamLTtraceAutoLastDisEnd_Type = TimeStamp
_TmnxOamLTtraceAutoLastDisEnd_Object = MibTableColumn
tmnxOamLTtraceAutoLastDisEnd = _TmnxOamLTtraceAutoLastDisEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 23, 1, 5),
    _TmnxOamLTtraceAutoLastDisEnd_Type()
)
tmnxOamLTtraceAutoLastDisEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoLastDisEnd.setStatus("current")
_TmnxOamLTtraceAutoLastDisDur_Type = Unsigned32
_TmnxOamLTtraceAutoLastDisDur_Object = MibTableColumn
tmnxOamLTtraceAutoLastDisDur = _TmnxOamLTtraceAutoLastDisDur_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 23, 1, 6),
    _TmnxOamLTtraceAutoLastDisDur_Type()
)
tmnxOamLTtraceAutoLastDisDur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoLastDisDur.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoLastDisDur.setUnits("seconds")
_TmnxOamLTtraceFecInfoTable_Object = MibTable
tmnxOamLTtraceFecInfoTable = _TmnxOamLTtraceFecInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 24)
)
if mibBuilder.loadTexts:
    tmnxOamLTtraceFecInfoTable.setStatus("current")
_TmnxOamLTtraceFecInfoEntry_Object = MibTableRow
tmnxOamLTtraceFecInfoEntry = _TmnxOamLTtraceFecInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 24, 1)
)
tmnxOamLTtraceFecInfoEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceFecPrefixType"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceFecPrefix"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceFecPrefLen"),
)
if mibBuilder.loadTexts:
    tmnxOamLTtraceFecInfoEntry.setStatus("current")
_TmnxOamLTtraceFecPrefixType_Type = InetAddressType
_TmnxOamLTtraceFecPrefixType_Object = MibTableColumn
tmnxOamLTtraceFecPrefixType = _TmnxOamLTtraceFecPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 24, 1, 1),
    _TmnxOamLTtraceFecPrefixType_Type()
)
tmnxOamLTtraceFecPrefixType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamLTtraceFecPrefixType.setStatus("current")


class _TmnxOamLTtraceFecPrefix_Type(InetAddress):
    """Custom type tmnxOamLTtraceFecPrefix based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamLTtraceFecPrefix_Type.__name__ = "InetAddress"
_TmnxOamLTtraceFecPrefix_Object = MibTableColumn
tmnxOamLTtraceFecPrefix = _TmnxOamLTtraceFecPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 24, 1, 2),
    _TmnxOamLTtraceFecPrefix_Type()
)
tmnxOamLTtraceFecPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamLTtraceFecPrefix.setStatus("current")
_TmnxOamLTtraceFecPrefLen_Type = InetAddressPrefixLength
_TmnxOamLTtraceFecPrefLen_Object = MibTableColumn
tmnxOamLTtraceFecPrefLen = _TmnxOamLTtraceFecPrefLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 24, 1, 3),
    _TmnxOamLTtraceFecPrefLen_Type()
)
tmnxOamLTtraceFecPrefLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamLTtraceFecPrefLen.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamLTtraceFecPrefLen.setUnits("bits")


class _TmnxOamLTtraceFecDiscoveryState_Type(Integer32):
    """Custom type tmnxOamLTtraceFecDiscoveryState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("initial", 0),
          ("inProgress", 1),
          ("done", 2))
    )


_TmnxOamLTtraceFecDiscoveryState_Type.__name__ = "Integer32"
_TmnxOamLTtraceFecDiscoveryState_Object = MibTableColumn
tmnxOamLTtraceFecDiscoveryState = _TmnxOamLTtraceFecDiscoveryState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 24, 1, 4),
    _TmnxOamLTtraceFecDiscoveryState_Type()
)
tmnxOamLTtraceFecDiscoveryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceFecDiscoveryState.setStatus("current")
_TmnxOamLTtraceFecDisStatusBits_Type = TmnxOamLTtraceDisStatusBits
_TmnxOamLTtraceFecDisStatusBits_Object = MibTableColumn
tmnxOamLTtraceFecDisStatusBits = _TmnxOamLTtraceFecDisStatusBits_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 24, 1, 5),
    _TmnxOamLTtraceFecDisStatusBits_Type()
)
tmnxOamLTtraceFecDisStatusBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceFecDisStatusBits.setStatus("current")
_TmnxOamLTtraceFecDisPaths_Type = Unsigned32
_TmnxOamLTtraceFecDisPaths_Object = MibTableColumn
tmnxOamLTtraceFecDisPaths = _TmnxOamLTtraceFecDisPaths_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 24, 1, 6),
    _TmnxOamLTtraceFecDisPaths_Type()
)
tmnxOamLTtraceFecDisPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceFecDisPaths.setStatus("current")
_TmnxOamLTtraceFecFailedHops_Type = Unsigned32
_TmnxOamLTtraceFecFailedHops_Object = MibTableColumn
tmnxOamLTtraceFecFailedHops = _TmnxOamLTtraceFecFailedHops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 24, 1, 7),
    _TmnxOamLTtraceFecFailedHops_Type()
)
tmnxOamLTtraceFecFailedHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceFecFailedHops.setStatus("current")
_TmnxOamLTtraceFecLastDisEnd_Type = TimeStamp
_TmnxOamLTtraceFecLastDisEnd_Object = MibTableColumn
tmnxOamLTtraceFecLastDisEnd = _TmnxOamLTtraceFecLastDisEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 24, 1, 8),
    _TmnxOamLTtraceFecLastDisEnd_Type()
)
tmnxOamLTtraceFecLastDisEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceFecLastDisEnd.setStatus("current")
_TmnxOamLTtraceFecFailedProbes_Type = Unsigned32
_TmnxOamLTtraceFecFailedProbes_Object = MibTableColumn
tmnxOamLTtraceFecFailedProbes = _TmnxOamLTtraceFecFailedProbes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 24, 1, 9),
    _TmnxOamLTtraceFecFailedProbes_Type()
)
tmnxOamLTtraceFecFailedProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceFecFailedProbes.setStatus("current")


class _TmnxOamLTtraceFecProbeState_Type(Integer32):
    """Custom type tmnxOamLTtraceFecProbeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oK", 0),
          ("partiallyFailed", 1),
          ("failed", 2))
    )


_TmnxOamLTtraceFecProbeState_Type.__name__ = "Integer32"
_TmnxOamLTtraceFecProbeState_Object = MibTableColumn
tmnxOamLTtraceFecProbeState = _TmnxOamLTtraceFecProbeState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 24, 1, 10),
    _TmnxOamLTtraceFecProbeState_Type()
)
tmnxOamLTtraceFecProbeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceFecProbeState.setStatus("current")
_TmnxOamLTtraceFecSendErrProbes_Type = Unsigned32
_TmnxOamLTtraceFecSendErrProbes_Object = MibTableColumn
tmnxOamLTtraceFecSendErrProbes = _TmnxOamLTtraceFecSendErrProbes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 24, 1, 11),
    _TmnxOamLTtraceFecSendErrProbes_Type()
)
tmnxOamLTtraceFecSendErrProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceFecSendErrProbes.setStatus("current")
_TmnxOamLTtracePathInfoTable_Object = MibTable
tmnxOamLTtracePathInfoTable = _TmnxOamLTtracePathInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 25)
)
if mibBuilder.loadTexts:
    tmnxOamLTtracePathInfoTable.setStatus("current")
_TmnxOamLTtracePathInfoEntry_Object = MibTableRow
tmnxOamLTtracePathInfoEntry = _TmnxOamLTtracePathInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 25, 1)
)
tmnxOamLTtracePathInfoEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceFecPrefixType"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceFecPrefix"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceFecPrefLen"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamLTtracePathDstAddrType"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamLTtracePathDstAddr"),
)
if mibBuilder.loadTexts:
    tmnxOamLTtracePathInfoEntry.setStatus("current")
_TmnxOamLTtracePathDstAddrType_Type = InetAddressType
_TmnxOamLTtracePathDstAddrType_Object = MibTableColumn
tmnxOamLTtracePathDstAddrType = _TmnxOamLTtracePathDstAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 25, 1, 1),
    _TmnxOamLTtracePathDstAddrType_Type()
)
tmnxOamLTtracePathDstAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamLTtracePathDstAddrType.setStatus("current")


class _TmnxOamLTtracePathDstAddr_Type(InetAddress):
    """Custom type tmnxOamLTtracePathDstAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamLTtracePathDstAddr_Type.__name__ = "InetAddress"
_TmnxOamLTtracePathDstAddr_Object = MibTableColumn
tmnxOamLTtracePathDstAddr = _TmnxOamLTtracePathDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 25, 1, 2),
    _TmnxOamLTtracePathDstAddr_Type()
)
tmnxOamLTtracePathDstAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamLTtracePathDstAddr.setStatus("current")
_TmnxOamLTtracePathRemAddrType_Type = InetAddressType
_TmnxOamLTtracePathRemAddrType_Object = MibTableColumn
tmnxOamLTtracePathRemAddrType = _TmnxOamLTtracePathRemAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 25, 1, 3),
    _TmnxOamLTtracePathRemAddrType_Type()
)
tmnxOamLTtracePathRemAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtracePathRemAddrType.setStatus("current")


class _TmnxOamLTtracePathRemoteAddr_Type(InetAddress):
    """Custom type tmnxOamLTtracePathRemoteAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamLTtracePathRemoteAddr_Type.__name__ = "InetAddress"
_TmnxOamLTtracePathRemoteAddr_Object = MibTableColumn
tmnxOamLTtracePathRemoteAddr = _TmnxOamLTtracePathRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 25, 1, 4),
    _TmnxOamLTtracePathRemoteAddr_Type()
)
tmnxOamLTtracePathRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtracePathRemoteAddr.setStatus("current")
_TmnxOamLTtracePathEgrNhAddrType_Type = InetAddressType
_TmnxOamLTtracePathEgrNhAddrType_Object = MibTableColumn
tmnxOamLTtracePathEgrNhAddrType = _TmnxOamLTtracePathEgrNhAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 25, 1, 5),
    _TmnxOamLTtracePathEgrNhAddrType_Type()
)
tmnxOamLTtracePathEgrNhAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtracePathEgrNhAddrType.setStatus("current")


class _TmnxOamLTtracePathEgrNhAddr_Type(InetAddress):
    """Custom type tmnxOamLTtracePathEgrNhAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamLTtracePathEgrNhAddr_Type.__name__ = "InetAddress"
_TmnxOamLTtracePathEgrNhAddr_Object = MibTableColumn
tmnxOamLTtracePathEgrNhAddr = _TmnxOamLTtracePathEgrNhAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 25, 1, 6),
    _TmnxOamLTtracePathEgrNhAddr_Type()
)
tmnxOamLTtracePathEgrNhAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtracePathEgrNhAddr.setStatus("current")
_TmnxOamLTtracePathDisTtl_Type = Unsigned32
_TmnxOamLTtracePathDisTtl_Object = MibTableColumn
tmnxOamLTtracePathDisTtl = _TmnxOamLTtracePathDisTtl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 25, 1, 7),
    _TmnxOamLTtracePathDisTtl_Type()
)
tmnxOamLTtracePathDisTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtracePathDisTtl.setStatus("current")
_TmnxOamLTtracePathLastDisTime_Type = TimeStamp
_TmnxOamLTtracePathLastDisTime_Object = MibTableColumn
tmnxOamLTtracePathLastDisTime = _TmnxOamLTtracePathLastDisTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 25, 1, 8),
    _TmnxOamLTtracePathLastDisTime_Type()
)
tmnxOamLTtracePathLastDisTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtracePathLastDisTime.setStatus("current")
_TmnxOamLTtracePathLastRc_Type = TmnxOamPingRtnCode
_TmnxOamLTtracePathLastRc_Object = MibTableColumn
tmnxOamLTtracePathLastRc = _TmnxOamLTtracePathLastRc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 25, 1, 9),
    _TmnxOamLTtracePathLastRc_Type()
)
tmnxOamLTtracePathLastRc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtracePathLastRc.setStatus("current")


class _TmnxOamLTtracePathProbeState_Type(Integer32):
    """Custom type tmnxOamLTtracePathProbeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("oK", 0),
          ("failed", 1))
    )


_TmnxOamLTtracePathProbeState_Type.__name__ = "Integer32"
_TmnxOamLTtracePathProbeState_Object = MibTableColumn
tmnxOamLTtracePathProbeState = _TmnxOamLTtracePathProbeState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 25, 1, 10),
    _TmnxOamLTtracePathProbeState_Type()
)
tmnxOamLTtracePathProbeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtracePathProbeState.setStatus("current")
_TmnxOamLTtracePathProbeTmOutCnt_Type = Unsigned32
_TmnxOamLTtracePathProbeTmOutCnt_Object = MibTableColumn
tmnxOamLTtracePathProbeTmOutCnt = _TmnxOamLTtracePathProbeTmOutCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 25, 1, 11),
    _TmnxOamLTtracePathProbeTmOutCnt_Type()
)
tmnxOamLTtracePathProbeTmOutCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtracePathProbeTmOutCnt.setStatus("current")


class _TmnxOamLTtracePathProbeSendErr_Type(Integer32):
    """Custom type tmnxOamLTtracePathProbeSendErr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("oK", 0),
          ("failed", 1))
    )


_TmnxOamLTtracePathProbeSendErr_Type.__name__ = "Integer32"
_TmnxOamLTtracePathProbeSendErr_Object = MibTableColumn
tmnxOamLTtracePathProbeSendErr = _TmnxOamLTtracePathProbeSendErr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 25, 1, 12),
    _TmnxOamLTtracePathProbeSendErr_Type()
)
tmnxOamLTtracePathProbeSendErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtracePathProbeSendErr.setStatus("current")
_TmnxOamVccvTrCtlTable_Object = MibTable
tmnxOamVccvTrCtlTable = _TmnxOamVccvTrCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 26)
)
if mibBuilder.loadTexts:
    tmnxOamVccvTrCtlTable.setStatus("current")
_TmnxOamVccvTrCtlEntry_Object = MibTableRow
tmnxOamVccvTrCtlEntry = _TmnxOamVccvTrCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 26, 1)
)
tmnxOamVccvTrCtlEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamVccvTrCtlEntry.setStatus("current")


class _TmnxOamVccvTrCtlSdpIdVcId_Type(SdpBindId):
    """Custom type tmnxOamVccvTrCtlSdpIdVcId based on SdpBindId"""
    defaultHexValue = "0000000000000000"


_TmnxOamVccvTrCtlSdpIdVcId_Type.__name__ = "SdpBindId"
_TmnxOamVccvTrCtlSdpIdVcId_Object = MibTableColumn
tmnxOamVccvTrCtlSdpIdVcId = _TmnxOamVccvTrCtlSdpIdVcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 26, 1, 1),
    _TmnxOamVccvTrCtlSdpIdVcId_Type()
)
tmnxOamVccvTrCtlSdpIdVcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamVccvTrCtlSdpIdVcId.setStatus("current")


class _TmnxOamVccvTrCtlReplyMode_Type(Integer32):
    """Custom type tmnxOamVccvTrCtlReplyMode based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ip", 2),
          ("controlChannel", 4))
    )


_TmnxOamVccvTrCtlReplyMode_Type.__name__ = "Integer32"
_TmnxOamVccvTrCtlReplyMode_Object = MibTableColumn
tmnxOamVccvTrCtlReplyMode = _TmnxOamVccvTrCtlReplyMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 26, 1, 2),
    _TmnxOamVccvTrCtlReplyMode_Type()
)
tmnxOamVccvTrCtlReplyMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamVccvTrCtlReplyMode.setStatus("current")


class _TmnxOamVccvTrCtlSpokeSdpId_Type(TmnxSpokeSdpIdOrZero):
    """Custom type tmnxOamVccvTrCtlSpokeSdpId based on TmnxSpokeSdpIdOrZero"""
    defaultValue = 0


_TmnxOamVccvTrCtlSpokeSdpId_Type.__name__ = "TmnxSpokeSdpIdOrZero"
_TmnxOamVccvTrCtlSpokeSdpId_Object = MibTableColumn
tmnxOamVccvTrCtlSpokeSdpId = _TmnxOamVccvTrCtlSpokeSdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 26, 1, 3),
    _TmnxOamVccvTrCtlSpokeSdpId_Type()
)
tmnxOamVccvTrCtlSpokeSdpId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamVccvTrCtlSpokeSdpId.setStatus("current")


class _TmnxOamVccvTrCtlSaiiGlobalId_Type(TmnxPwGlobalIdOrZero):
    """Custom type tmnxOamVccvTrCtlSaiiGlobalId based on TmnxPwGlobalIdOrZero"""
    defaultValue = 0


_TmnxOamVccvTrCtlSaiiGlobalId_Type.__name__ = "TmnxPwGlobalIdOrZero"
_TmnxOamVccvTrCtlSaiiGlobalId_Object = MibTableColumn
tmnxOamVccvTrCtlSaiiGlobalId = _TmnxOamVccvTrCtlSaiiGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 26, 1, 4),
    _TmnxOamVccvTrCtlSaiiGlobalId_Type()
)
tmnxOamVccvTrCtlSaiiGlobalId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamVccvTrCtlSaiiGlobalId.setStatus("current")


class _TmnxOamVccvTrCtlSaiiPrefix_Type(Unsigned32):
    """Custom type tmnxOamVccvTrCtlSaiiPrefix based on Unsigned32"""
    defaultValue = 0


_TmnxOamVccvTrCtlSaiiPrefix_Type.__name__ = "Unsigned32"
_TmnxOamVccvTrCtlSaiiPrefix_Object = MibTableColumn
tmnxOamVccvTrCtlSaiiPrefix = _TmnxOamVccvTrCtlSaiiPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 26, 1, 5),
    _TmnxOamVccvTrCtlSaiiPrefix_Type()
)
tmnxOamVccvTrCtlSaiiPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamVccvTrCtlSaiiPrefix.setStatus("current")


class _TmnxOamVccvTrCtlSaiiAcId_Type(Unsigned32):
    """Custom type tmnxOamVccvTrCtlSaiiAcId based on Unsigned32"""
    defaultValue = 0


_TmnxOamVccvTrCtlSaiiAcId_Type.__name__ = "Unsigned32"
_TmnxOamVccvTrCtlSaiiAcId_Object = MibTableColumn
tmnxOamVccvTrCtlSaiiAcId = _TmnxOamVccvTrCtlSaiiAcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 26, 1, 6),
    _TmnxOamVccvTrCtlSaiiAcId_Type()
)
tmnxOamVccvTrCtlSaiiAcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamVccvTrCtlSaiiAcId.setStatus("current")


class _TmnxOamVccvTrCtlTaiiGlobalId_Type(TmnxPwGlobalIdOrZero):
    """Custom type tmnxOamVccvTrCtlTaiiGlobalId based on TmnxPwGlobalIdOrZero"""
    defaultValue = 0


_TmnxOamVccvTrCtlTaiiGlobalId_Type.__name__ = "TmnxPwGlobalIdOrZero"
_TmnxOamVccvTrCtlTaiiGlobalId_Object = MibTableColumn
tmnxOamVccvTrCtlTaiiGlobalId = _TmnxOamVccvTrCtlTaiiGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 26, 1, 7),
    _TmnxOamVccvTrCtlTaiiGlobalId_Type()
)
tmnxOamVccvTrCtlTaiiGlobalId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamVccvTrCtlTaiiGlobalId.setStatus("current")


class _TmnxOamVccvTrCtlTaiiPrefix_Type(Unsigned32):
    """Custom type tmnxOamVccvTrCtlTaiiPrefix based on Unsigned32"""
    defaultValue = 0


_TmnxOamVccvTrCtlTaiiPrefix_Type.__name__ = "Unsigned32"
_TmnxOamVccvTrCtlTaiiPrefix_Object = MibTableColumn
tmnxOamVccvTrCtlTaiiPrefix = _TmnxOamVccvTrCtlTaiiPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 26, 1, 8),
    _TmnxOamVccvTrCtlTaiiPrefix_Type()
)
tmnxOamVccvTrCtlTaiiPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamVccvTrCtlTaiiPrefix.setStatus("current")


class _TmnxOamVccvTrCtlTaiiAcId_Type(Unsigned32):
    """Custom type tmnxOamVccvTrCtlTaiiAcId based on Unsigned32"""
    defaultValue = 0


_TmnxOamVccvTrCtlTaiiAcId_Type.__name__ = "Unsigned32"
_TmnxOamVccvTrCtlTaiiAcId_Object = MibTableColumn
tmnxOamVccvTrCtlTaiiAcId = _TmnxOamVccvTrCtlTaiiAcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 26, 1, 9),
    _TmnxOamVccvTrCtlTaiiAcId_Type()
)
tmnxOamVccvTrCtlTaiiAcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamVccvTrCtlTaiiAcId.setStatus("current")


class _TmnxOamVccvTrCtlTestSubMode_Type(TmnxOamVccvTestSubMode):
    """Custom type tmnxOamVccvTrCtlTestSubMode based on TmnxOamVccvTestSubMode"""
    defaultValue = 1


_TmnxOamVccvTrCtlTestSubMode_Type.__name__ = "TmnxOamVccvTestSubMode"
_TmnxOamVccvTrCtlTestSubMode_Object = MibTableColumn
tmnxOamVccvTrCtlTestSubMode = _TmnxOamVccvTrCtlTestSubMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 26, 1, 10),
    _TmnxOamVccvTrCtlTestSubMode_Type()
)
tmnxOamVccvTrCtlTestSubMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamVccvTrCtlTestSubMode.setStatus("current")


class _TmnxOamVccvTrCtlAssocChannel_Type(TmnxOamVccvAssocChannel):
    """Custom type tmnxOamVccvTrCtlAssocChannel based on TmnxOamVccvAssocChannel"""
    defaultValue = 1


_TmnxOamVccvTrCtlAssocChannel_Type.__name__ = "TmnxOamVccvAssocChannel"
_TmnxOamVccvTrCtlAssocChannel_Object = MibTableColumn
tmnxOamVccvTrCtlAssocChannel = _TmnxOamVccvTrCtlAssocChannel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 26, 1, 11),
    _TmnxOamVccvTrCtlAssocChannel_Type()
)
tmnxOamVccvTrCtlAssocChannel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamVccvTrCtlAssocChannel.setStatus("current")


class _TmnxOamVccvTrCtlSwitTgtFecType_Type(TmnxOamVccvSwitTgtFecType):
    """Custom type tmnxOamVccvTrCtlSwitTgtFecType based on TmnxOamVccvSwitTgtFecType"""
    defaultValue = 1


_TmnxOamVccvTrCtlSwitTgtFecType_Type.__name__ = "TmnxOamVccvSwitTgtFecType"
_TmnxOamVccvTrCtlSwitTgtFecType_Object = MibTableColumn
tmnxOamVccvTrCtlSwitTgtFecType = _TmnxOamVccvTrCtlSwitTgtFecType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 26, 1, 12),
    _TmnxOamVccvTrCtlSwitTgtFecType_Type()
)
tmnxOamVccvTrCtlSwitTgtFecType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamVccvTrCtlSwitTgtFecType.setStatus("current")
_TmnxOamVccvTrNextPwSegmentTable_Object = MibTable
tmnxOamVccvTrNextPwSegmentTable = _TmnxOamVccvTrNextPwSegmentTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 27)
)
if mibBuilder.loadTexts:
    tmnxOamVccvTrNextPwSegmentTable.setStatus("current")
_TmnxOamVccvTrNextPwSegmentEntry_Object = MibTableRow
tmnxOamVccvTrNextPwSegmentEntry = _TmnxOamVccvTrNextPwSegmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 27, 1)
)
tmnxOamVccvTrNextPwSegmentEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsTestRunIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryHopIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryProbeIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamVccvTrNextPwSegmentEntry.setStatus("current")
_TmnxOamVccvTrNextPwID_Type = TmnxVcIdOrNone
_TmnxOamVccvTrNextPwID_Object = MibTableColumn
tmnxOamVccvTrNextPwID = _TmnxOamVccvTrNextPwID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 27, 1, 1),
    _TmnxOamVccvTrNextPwID_Type()
)
tmnxOamVccvTrNextPwID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVccvTrNextPwID.setStatus("current")
_TmnxOamVccvTrNextPwType_Type = SdpBindVcType
_TmnxOamVccvTrNextPwType_Object = MibTableColumn
tmnxOamVccvTrNextPwType = _TmnxOamVccvTrNextPwType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 27, 1, 2),
    _TmnxOamVccvTrNextPwType_Type()
)
tmnxOamVccvTrNextPwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVccvTrNextPwType.setStatus("current")
_TmnxOamVccvTrNextSenderAddrType_Type = InetAddressType
_TmnxOamVccvTrNextSenderAddrType_Object = MibTableColumn
tmnxOamVccvTrNextSenderAddrType = _TmnxOamVccvTrNextSenderAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 27, 1, 3),
    _TmnxOamVccvTrNextSenderAddrType_Type()
)
tmnxOamVccvTrNextSenderAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVccvTrNextSenderAddrType.setStatus("current")


class _TmnxOamVccvTrNextSenderAddr_Type(InetAddress):
    """Custom type tmnxOamVccvTrNextSenderAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamVccvTrNextSenderAddr_Type.__name__ = "InetAddress"
_TmnxOamVccvTrNextSenderAddr_Object = MibTableColumn
tmnxOamVccvTrNextSenderAddr = _TmnxOamVccvTrNextSenderAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 27, 1, 4),
    _TmnxOamVccvTrNextSenderAddr_Type()
)
tmnxOamVccvTrNextSenderAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVccvTrNextSenderAddr.setStatus("current")
_TmnxOamVccvTrNextRemoteAddrType_Type = InetAddressType
_TmnxOamVccvTrNextRemoteAddrType_Object = MibTableColumn
tmnxOamVccvTrNextRemoteAddrType = _TmnxOamVccvTrNextRemoteAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 27, 1, 5),
    _TmnxOamVccvTrNextRemoteAddrType_Type()
)
tmnxOamVccvTrNextRemoteAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVccvTrNextRemoteAddrType.setStatus("current")


class _TmnxOamVccvTrNextRemoteAddr_Type(InetAddress):
    """Custom type tmnxOamVccvTrNextRemoteAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamVccvTrNextRemoteAddr_Type.__name__ = "InetAddress"
_TmnxOamVccvTrNextRemoteAddr_Object = MibTableColumn
tmnxOamVccvTrNextRemoteAddr = _TmnxOamVccvTrNextRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 27, 1, 6),
    _TmnxOamVccvTrNextRemoteAddr_Type()
)
tmnxOamVccvTrNextRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVccvTrNextRemoteAddr.setStatus("current")
_TmnxOamVccvTrNextSaiiGlobalId_Type = TmnxPwGlobalIdOrZero
_TmnxOamVccvTrNextSaiiGlobalId_Object = MibTableColumn
tmnxOamVccvTrNextSaiiGlobalId = _TmnxOamVccvTrNextSaiiGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 27, 1, 7),
    _TmnxOamVccvTrNextSaiiGlobalId_Type()
)
tmnxOamVccvTrNextSaiiGlobalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVccvTrNextSaiiGlobalId.setStatus("current")
_TmnxOamVccvTrNextSaiiPrefix_Type = Unsigned32
_TmnxOamVccvTrNextSaiiPrefix_Object = MibTableColumn
tmnxOamVccvTrNextSaiiPrefix = _TmnxOamVccvTrNextSaiiPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 27, 1, 8),
    _TmnxOamVccvTrNextSaiiPrefix_Type()
)
tmnxOamVccvTrNextSaiiPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVccvTrNextSaiiPrefix.setStatus("current")
_TmnxOamVccvTrNextSaiiAcId_Type = Unsigned32
_TmnxOamVccvTrNextSaiiAcId_Object = MibTableColumn
tmnxOamVccvTrNextSaiiAcId = _TmnxOamVccvTrNextSaiiAcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 27, 1, 9),
    _TmnxOamVccvTrNextSaiiAcId_Type()
)
tmnxOamVccvTrNextSaiiAcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVccvTrNextSaiiAcId.setStatus("current")
_TmnxOamVccvTrNextTaiiGlobalId_Type = TmnxPwGlobalIdOrZero
_TmnxOamVccvTrNextTaiiGlobalId_Object = MibTableColumn
tmnxOamVccvTrNextTaiiGlobalId = _TmnxOamVccvTrNextTaiiGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 27, 1, 10),
    _TmnxOamVccvTrNextTaiiGlobalId_Type()
)
tmnxOamVccvTrNextTaiiGlobalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVccvTrNextTaiiGlobalId.setStatus("current")
_TmnxOamVccvTrNextTaiiPrefix_Type = Unsigned32
_TmnxOamVccvTrNextTaiiPrefix_Object = MibTableColumn
tmnxOamVccvTrNextTaiiPrefix = _TmnxOamVccvTrNextTaiiPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 27, 1, 11),
    _TmnxOamVccvTrNextTaiiPrefix_Type()
)
tmnxOamVccvTrNextTaiiPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVccvTrNextTaiiPrefix.setStatus("current")
_TmnxOamVccvTrNextTaiiAcId_Type = Unsigned32
_TmnxOamVccvTrNextTaiiAcId_Object = MibTableColumn
tmnxOamVccvTrNextTaiiAcId = _TmnxOamVccvTrNextTaiiAcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 27, 1, 12),
    _TmnxOamVccvTrNextTaiiAcId_Type()
)
tmnxOamVccvTrNextTaiiAcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVccvTrNextTaiiAcId.setStatus("current")


class _TmnxOamVccvTrNextTpAgi_Type(OctetString):
    """Custom type tmnxOamVccvTrNextTpAgi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_TmnxOamVccvTrNextTpAgi_Type.__name__ = "OctetString"
_TmnxOamVccvTrNextTpAgi_Object = MibTableColumn
tmnxOamVccvTrNextTpAgi = _TmnxOamVccvTrNextTpAgi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 27, 1, 13),
    _TmnxOamVccvTrNextTpAgi_Type()
)
tmnxOamVccvTrNextTpAgi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVccvTrNextTpAgi.setStatus("current")
_TmnxOamVccvTrNextTpSaiiGlobalId_Type = TmnxMplsTpGlobalID
_TmnxOamVccvTrNextTpSaiiGlobalId_Object = MibTableColumn
tmnxOamVccvTrNextTpSaiiGlobalId = _TmnxOamVccvTrNextTpSaiiGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 27, 1, 14),
    _TmnxOamVccvTrNextTpSaiiGlobalId_Type()
)
tmnxOamVccvTrNextTpSaiiGlobalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVccvTrNextTpSaiiGlobalId.setStatus("current")
_TmnxOamVccvTrNextTpSaiiNodeId_Type = TmnxMplsTpNodeID
_TmnxOamVccvTrNextTpSaiiNodeId_Object = MibTableColumn
tmnxOamVccvTrNextTpSaiiNodeId = _TmnxOamVccvTrNextTpSaiiNodeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 27, 1, 15),
    _TmnxOamVccvTrNextTpSaiiNodeId_Type()
)
tmnxOamVccvTrNextTpSaiiNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVccvTrNextTpSaiiNodeId.setStatus("current")
_TmnxOamVccvTrNextTpSaiiAcId_Type = Unsigned32
_TmnxOamVccvTrNextTpSaiiAcId_Object = MibTableColumn
tmnxOamVccvTrNextTpSaiiAcId = _TmnxOamVccvTrNextTpSaiiAcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 27, 1, 16),
    _TmnxOamVccvTrNextTpSaiiAcId_Type()
)
tmnxOamVccvTrNextTpSaiiAcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVccvTrNextTpSaiiAcId.setStatus("current")
_TmnxOamVccvTrNextTpTaiiGlobalId_Type = TmnxMplsTpGlobalID
_TmnxOamVccvTrNextTpTaiiGlobalId_Object = MibTableColumn
tmnxOamVccvTrNextTpTaiiGlobalId = _TmnxOamVccvTrNextTpTaiiGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 27, 1, 17),
    _TmnxOamVccvTrNextTpTaiiGlobalId_Type()
)
tmnxOamVccvTrNextTpTaiiGlobalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVccvTrNextTpTaiiGlobalId.setStatus("current")
_TmnxOamVccvTrNextTpTaiiNodeId_Type = TmnxMplsTpNodeID
_TmnxOamVccvTrNextTpTaiiNodeId_Object = MibTableColumn
tmnxOamVccvTrNextTpTaiiNodeId = _TmnxOamVccvTrNextTpTaiiNodeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 27, 1, 18),
    _TmnxOamVccvTrNextTpTaiiNodeId_Type()
)
tmnxOamVccvTrNextTpTaiiNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVccvTrNextTpTaiiNodeId.setStatus("current")
_TmnxOamVccvTrNextTpTaiiAcId_Type = Unsigned32
_TmnxOamVccvTrNextTpTaiiAcId_Object = MibTableColumn
tmnxOamVccvTrNextTpTaiiAcId = _TmnxOamVccvTrNextTpTaiiAcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 27, 1, 19),
    _TmnxOamVccvTrNextTpTaiiAcId_Type()
)
tmnxOamVccvTrNextTpTaiiAcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVccvTrNextTpTaiiAcId.setStatus("current")
_TmnxOamP2mpLspTrCtlTable_Object = MibTable
tmnxOamP2mpLspTrCtlTable = _TmnxOamP2mpLspTrCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 28)
)
if mibBuilder.loadTexts:
    tmnxOamP2mpLspTrCtlTable.setStatus("current")
_TmnxOamP2mpLspTrCtlEntry_Object = MibTableRow
tmnxOamP2mpLspTrCtlEntry = _TmnxOamP2mpLspTrCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 28, 1)
)
tmnxOamP2mpLspTrCtlEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamP2mpLspTrCtlEntry.setStatus("current")


class _TmnxOamP2mpLspTrCtlLspName_Type(TLNamedItemOrEmpty):
    """Custom type tmnxOamP2mpLspTrCtlLspName based on TLNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOamP2mpLspTrCtlLspName_Type.__name__ = "TLNamedItemOrEmpty"
_TmnxOamP2mpLspTrCtlLspName_Object = MibTableColumn
tmnxOamP2mpLspTrCtlLspName = _TmnxOamP2mpLspTrCtlLspName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 28, 1, 1),
    _TmnxOamP2mpLspTrCtlLspName_Type()
)
tmnxOamP2mpLspTrCtlLspName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamP2mpLspTrCtlLspName.setStatus("current")


class _TmnxOamP2mpLspTrCtlInstName_Type(TNamedItemOrEmpty):
    """Custom type tmnxOamP2mpLspTrCtlInstName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOamP2mpLspTrCtlInstName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOamP2mpLspTrCtlInstName_Object = MibTableColumn
tmnxOamP2mpLspTrCtlInstName = _TmnxOamP2mpLspTrCtlInstName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 28, 1, 2),
    _TmnxOamP2mpLspTrCtlInstName_Type()
)
tmnxOamP2mpLspTrCtlInstName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamP2mpLspTrCtlInstName.setStatus("current")


class _TmnxOamP2mpLspTrCtlLeafIpAddr_Type(InetAddress):
    """Custom type tmnxOamP2mpLspTrCtlLeafIpAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamP2mpLspTrCtlLeafIpAddr_Type.__name__ = "InetAddress"
_TmnxOamP2mpLspTrCtlLeafIpAddr_Object = MibTableColumn
tmnxOamP2mpLspTrCtlLeafIpAddr = _TmnxOamP2mpLspTrCtlLeafIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 28, 1, 3),
    _TmnxOamP2mpLspTrCtlLeafIpAddr_Type()
)
tmnxOamP2mpLspTrCtlLeafIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamP2mpLspTrCtlLeafIpAddr.setStatus("current")


class _TmnxOamP2mpLspTrCtlLeafIpAddrType_Type(InetAddressType):
    """Custom type tmnxOamP2mpLspTrCtlLeafIpAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxOamP2mpLspTrCtlLeafIpAddrType_Type.__name__ = "InetAddressType"
_TmnxOamP2mpLspTrCtlLeafIpAddrType_Object = MibTableColumn
tmnxOamP2mpLspTrCtlLeafIpAddrType = _TmnxOamP2mpLspTrCtlLeafIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 28, 1, 4),
    _TmnxOamP2mpLspTrCtlLeafIpAddrType_Type()
)
tmnxOamP2mpLspTrCtlLeafIpAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamP2mpLspTrCtlLeafIpAddrType.setStatus("current")
_TmnxOamP2mpLspTrMapTable_Object = MibTable
tmnxOamP2mpLspTrMapTable = _TmnxOamP2mpLspTrMapTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 29)
)
if mibBuilder.loadTexts:
    tmnxOamP2mpLspTrMapTable.setStatus("current")
_TmnxOamP2mpLspTrMapEntry_Object = MibTableRow
tmnxOamP2mpLspTrMapEntry = _TmnxOamP2mpLspTrMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 29, 1)
)
tmnxOamP2mpLspTrMapEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsTestRunIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryHopIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryProbeIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamP2mpLspTrMapIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamP2mpLspTrMapEntry.setStatus("current")


class _TmnxOamP2mpLspTrMapIndex_Type(Unsigned32):
    """Custom type tmnxOamP2mpLspTrMapIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxOamP2mpLspTrMapIndex_Type.__name__ = "Unsigned32"
_TmnxOamP2mpLspTrMapIndex_Object = MibTableColumn
tmnxOamP2mpLspTrMapIndex = _TmnxOamP2mpLspTrMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 29, 1, 1),
    _TmnxOamP2mpLspTrMapIndex_Type()
)
tmnxOamP2mpLspTrMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamP2mpLspTrMapIndex.setStatus("current")
_TmnxOamP2mpLspTrMapDSIPv4Addr_Type = IpAddress
_TmnxOamP2mpLspTrMapDSIPv4Addr_Object = MibTableColumn
tmnxOamP2mpLspTrMapDSIPv4Addr = _TmnxOamP2mpLspTrMapDSIPv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 29, 1, 2),
    _TmnxOamP2mpLspTrMapDSIPv4Addr_Type()
)
tmnxOamP2mpLspTrMapDSIPv4Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamP2mpLspTrMapDSIPv4Addr.setStatus("current")
_TmnxOamP2mpLspTrMapAddrType_Type = TmnxOamAddressType
_TmnxOamP2mpLspTrMapAddrType_Object = MibTableColumn
tmnxOamP2mpLspTrMapAddrType = _TmnxOamP2mpLspTrMapAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 29, 1, 3),
    _TmnxOamP2mpLspTrMapAddrType_Type()
)
tmnxOamP2mpLspTrMapAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamP2mpLspTrMapAddrType.setStatus("current")
_TmnxOamP2mpLspTrMapDSIfAddr_Type = Unsigned32
_TmnxOamP2mpLspTrMapDSIfAddr_Object = MibTableColumn
tmnxOamP2mpLspTrMapDSIfAddr = _TmnxOamP2mpLspTrMapDSIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 29, 1, 4),
    _TmnxOamP2mpLspTrMapDSIfAddr_Type()
)
tmnxOamP2mpLspTrMapDSIfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamP2mpLspTrMapDSIfAddr.setStatus("current")


class _TmnxOamP2mpLspTrMapMTU_Type(Unsigned32):
    """Custom type tmnxOamP2mpLspTrMapMTU based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TmnxOamP2mpLspTrMapMTU_Type.__name__ = "Unsigned32"
_TmnxOamP2mpLspTrMapMTU_Object = MibTableColumn
tmnxOamP2mpLspTrMapMTU = _TmnxOamP2mpLspTrMapMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 29, 1, 5),
    _TmnxOamP2mpLspTrMapMTU_Type()
)
tmnxOamP2mpLspTrMapMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamP2mpLspTrMapMTU.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamP2mpLspTrMapMTU.setUnits("octets")
_TmnxOamP2mpLspTrMapP2mpBranch_Type = TruthValue
_TmnxOamP2mpLspTrMapP2mpBranch_Object = MibTableColumn
tmnxOamP2mpLspTrMapP2mpBranch = _TmnxOamP2mpLspTrMapP2mpBranch_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 29, 1, 6),
    _TmnxOamP2mpLspTrMapP2mpBranch_Type()
)
tmnxOamP2mpLspTrMapP2mpBranch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamP2mpLspTrMapP2mpBranch.setStatus("current")
_TmnxOamP2mpLspTrMapP2mpBud_Type = TruthValue
_TmnxOamP2mpLspTrMapP2mpBud_Object = MibTableColumn
tmnxOamP2mpLspTrMapP2mpBud = _TmnxOamP2mpLspTrMapP2mpBud_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 29, 1, 7),
    _TmnxOamP2mpLspTrMapP2mpBud_Type()
)
tmnxOamP2mpLspTrMapP2mpBud.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamP2mpLspTrMapP2mpBud.setStatus("current")
_TmnxOamP2mpLspTrDSLabelTable_Object = MibTable
tmnxOamP2mpLspTrDSLabelTable = _TmnxOamP2mpLspTrDSLabelTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 30)
)
if mibBuilder.loadTexts:
    tmnxOamP2mpLspTrDSLabelTable.setStatus("current")
_TmnxOamP2mpLspTrDSLabelEntry_Object = MibTableRow
tmnxOamP2mpLspTrDSLabelEntry = _TmnxOamP2mpLspTrDSLabelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 30, 1)
)
tmnxOamP2mpLspTrDSLabelEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsTestRunIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryHopIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryProbeIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrMapIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamP2mpLspTrDSLabelIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamP2mpLspTrDSLabelEntry.setStatus("current")


class _TmnxOamP2mpLspTrDSLabelIndex_Type(Unsigned32):
    """Custom type tmnxOamP2mpLspTrDSLabelIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxOamP2mpLspTrDSLabelIndex_Type.__name__ = "Unsigned32"
_TmnxOamP2mpLspTrDSLabelIndex_Object = MibTableColumn
tmnxOamP2mpLspTrDSLabelIndex = _TmnxOamP2mpLspTrDSLabelIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 30, 1, 1),
    _TmnxOamP2mpLspTrDSLabelIndex_Type()
)
tmnxOamP2mpLspTrDSLabelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamP2mpLspTrDSLabelIndex.setStatus("current")
_TmnxOamP2mpLspTrDSLabelLabel_Type = MplsLabel
_TmnxOamP2mpLspTrDSLabelLabel_Object = MibTableColumn
tmnxOamP2mpLspTrDSLabelLabel = _TmnxOamP2mpLspTrDSLabelLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 30, 1, 2),
    _TmnxOamP2mpLspTrDSLabelLabel_Type()
)
tmnxOamP2mpLspTrDSLabelLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamP2mpLspTrDSLabelLabel.setStatus("current")
_TmnxOamP2mpLspTrDSLabelProtocol_Type = TmnxOamSignalProtocol
_TmnxOamP2mpLspTrDSLabelProtocol_Object = MibTableColumn
tmnxOamP2mpLspTrDSLabelProtocol = _TmnxOamP2mpLspTrDSLabelProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 30, 1, 3),
    _TmnxOamP2mpLspTrDSLabelProtocol_Type()
)
tmnxOamP2mpLspTrDSLabelProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamP2mpLspTrDSLabelProtocol.setStatus("current")
_TmnxOamEthCfmTrCtlTable_Object = MibTable
tmnxOamEthCfmTrCtlTable = _TmnxOamEthCfmTrCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 31)
)
if mibBuilder.loadTexts:
    tmnxOamEthCfmTrCtlTable.setStatus("current")
_TmnxOamEthCfmTrCtlEntry_Object = MibTableRow
tmnxOamEthCfmTrCtlEntry = _TmnxOamEthCfmTrCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 31, 1)
)
tmnxOamEthCfmTrCtlEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamEthCfmTrCtlEntry.setStatus("current")


class _TmnxOamEthCfmTrCtlTgtMacAddr_Type(MacAddress):
    """Custom type tmnxOamEthCfmTrCtlTgtMacAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_TmnxOamEthCfmTrCtlTgtMacAddr_Type.__name__ = "MacAddress"
_TmnxOamEthCfmTrCtlTgtMacAddr_Object = MibTableColumn
tmnxOamEthCfmTrCtlTgtMacAddr = _TmnxOamEthCfmTrCtlTgtMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 31, 1, 1),
    _TmnxOamEthCfmTrCtlTgtMacAddr_Type()
)
tmnxOamEthCfmTrCtlTgtMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamEthCfmTrCtlTgtMacAddr.setStatus("current")


class _TmnxOamEthCfmTrCtlSrcMdIndex_Type(Unsigned32):
    """Custom type tmnxOamEthCfmTrCtlSrcMdIndex based on Unsigned32"""
    defaultValue = 0


_TmnxOamEthCfmTrCtlSrcMdIndex_Type.__name__ = "Unsigned32"
_TmnxOamEthCfmTrCtlSrcMdIndex_Object = MibTableColumn
tmnxOamEthCfmTrCtlSrcMdIndex = _TmnxOamEthCfmTrCtlSrcMdIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 31, 1, 2),
    _TmnxOamEthCfmTrCtlSrcMdIndex_Type()
)
tmnxOamEthCfmTrCtlSrcMdIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamEthCfmTrCtlSrcMdIndex.setStatus("current")


class _TmnxOamEthCfmTrCtlSrcMaIndex_Type(Unsigned32):
    """Custom type tmnxOamEthCfmTrCtlSrcMaIndex based on Unsigned32"""
    defaultValue = 0


_TmnxOamEthCfmTrCtlSrcMaIndex_Type.__name__ = "Unsigned32"
_TmnxOamEthCfmTrCtlSrcMaIndex_Object = MibTableColumn
tmnxOamEthCfmTrCtlSrcMaIndex = _TmnxOamEthCfmTrCtlSrcMaIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 31, 1, 3),
    _TmnxOamEthCfmTrCtlSrcMaIndex_Type()
)
tmnxOamEthCfmTrCtlSrcMaIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamEthCfmTrCtlSrcMaIndex.setStatus("current")


class _TmnxOamEthCfmTrCtlSrcMepId_Type(Dot1agCfmMepIdOrZero):
    """Custom type tmnxOamEthCfmTrCtlSrcMepId based on Dot1agCfmMepIdOrZero"""
    defaultValue = 0


_TmnxOamEthCfmTrCtlSrcMepId_Type.__name__ = "Dot1agCfmMepIdOrZero"
_TmnxOamEthCfmTrCtlSrcMepId_Object = MibTableColumn
tmnxOamEthCfmTrCtlSrcMepId = _TmnxOamEthCfmTrCtlSrcMepId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 31, 1, 4),
    _TmnxOamEthCfmTrCtlSrcMepId_Type()
)
tmnxOamEthCfmTrCtlSrcMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamEthCfmTrCtlSrcMepId.setStatus("current")


class _TmnxOamEthCfmTrCtlRemoteMepId_Type(Dot1agCfmMepIdOrZero):
    """Custom type tmnxOamEthCfmTrCtlRemoteMepId based on Dot1agCfmMepIdOrZero"""
    defaultValue = 0


_TmnxOamEthCfmTrCtlRemoteMepId_Type.__name__ = "Dot1agCfmMepIdOrZero"
_TmnxOamEthCfmTrCtlRemoteMepId_Object = MibTableColumn
tmnxOamEthCfmTrCtlRemoteMepId = _TmnxOamEthCfmTrCtlRemoteMepId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 31, 1, 5),
    _TmnxOamEthCfmTrCtlRemoteMepId_Type()
)
tmnxOamEthCfmTrCtlRemoteMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamEthCfmTrCtlRemoteMepId.setStatus("current")
_TmnxOamEthCfmTrPrHistTable_Object = MibTable
tmnxOamEthCfmTrPrHistTable = _TmnxOamEthCfmTrPrHistTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 32)
)
if mibBuilder.loadTexts:
    tmnxOamEthCfmTrPrHistTable.setStatus("current")
_TmnxOamEthCfmTrPrHistEntry_Object = MibTableRow
tmnxOamEthCfmTrPrHistEntry = _TmnxOamEthCfmTrPrHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 32, 1)
)
tmnxOamEthCfmTrPrHistEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsTestRunIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryHopIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryProbeIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamEthCfmTrPrHistEntry.setStatus("current")
_TmnxOamEthCfmTrPrHistIngressMac_Type = MacAddress
_TmnxOamEthCfmTrPrHistIngressMac_Object = MibTableColumn
tmnxOamEthCfmTrPrHistIngressMac = _TmnxOamEthCfmTrPrHistIngressMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 32, 1, 1),
    _TmnxOamEthCfmTrPrHistIngressMac_Type()
)
tmnxOamEthCfmTrPrHistIngressMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamEthCfmTrPrHistIngressMac.setStatus("current")
_TmnxOamEthCfmTrPrHistEgressMac_Type = MacAddress
_TmnxOamEthCfmTrPrHistEgressMac_Object = MibTableColumn
tmnxOamEthCfmTrPrHistEgressMac = _TmnxOamEthCfmTrPrHistEgressMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 32, 1, 2),
    _TmnxOamEthCfmTrPrHistEgressMac_Type()
)
tmnxOamEthCfmTrPrHistEgressMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamEthCfmTrPrHistEgressMac.setStatus("current")


class _TmnxOamEthCfmTrPrHistRelayAction_Type(Integer32):
    """Custom type tmnxOamEthCfmTrPrHistRelayAction based on Integer32"""
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
        *(("unknown", 0),
          ("rlyHit", 1),
          ("rlyFdb", 2),
          ("rlyMpdb", 3))
    )


_TmnxOamEthCfmTrPrHistRelayAction_Type.__name__ = "Integer32"
_TmnxOamEthCfmTrPrHistRelayAction_Object = MibTableColumn
tmnxOamEthCfmTrPrHistRelayAction = _TmnxOamEthCfmTrPrHistRelayAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 32, 1, 3),
    _TmnxOamEthCfmTrPrHistRelayAction_Type()
)
tmnxOamEthCfmTrPrHistRelayAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamEthCfmTrPrHistRelayAction.setStatus("current")
_TmnxOamEthCfmTrPrHistForwarded_Type = TruthValue
_TmnxOamEthCfmTrPrHistForwarded_Object = MibTableColumn
tmnxOamEthCfmTrPrHistForwarded = _TmnxOamEthCfmTrPrHistForwarded_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 32, 1, 4),
    _TmnxOamEthCfmTrPrHistForwarded_Type()
)
tmnxOamEthCfmTrPrHistForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamEthCfmTrPrHistForwarded.setStatus("current")
_TmnxOamEthCfmTrPrHistTerminalMep_Type = TruthValue
_TmnxOamEthCfmTrPrHistTerminalMep_Object = MibTableColumn
tmnxOamEthCfmTrPrHistTerminalMep = _TmnxOamEthCfmTrPrHistTerminalMep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 32, 1, 5),
    _TmnxOamEthCfmTrPrHistTerminalMep_Type()
)
tmnxOamEthCfmTrPrHistTerminalMep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamEthCfmTrPrHistTerminalMep.setStatus("current")
_TmnxOamLspTrFecStackTable_Object = MibTable
tmnxOamLspTrFecStackTable = _TmnxOamLspTrFecStackTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 33)
)
if mibBuilder.loadTexts:
    tmnxOamLspTrFecStackTable.setStatus("current")
_TmnxOamLspTrFecStackEntry_Object = MibTableRow
tmnxOamLspTrFecStackEntry = _TmnxOamLspTrFecStackEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 33, 1)
)
tmnxOamLspTrFecStackEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsTestRunIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryHopIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryProbeIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrMapIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrFecStackFecIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamLspTrFecStackEntry.setStatus("current")


class _TmnxOamLspTrFecStackFecIndex_Type(Unsigned32):
    """Custom type tmnxOamLspTrFecStackFecIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TmnxOamLspTrFecStackFecIndex_Type.__name__ = "Unsigned32"
_TmnxOamLspTrFecStackFecIndex_Object = MibTableColumn
tmnxOamLspTrFecStackFecIndex = _TmnxOamLspTrFecStackFecIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 33, 1, 1),
    _TmnxOamLspTrFecStackFecIndex_Type()
)
tmnxOamLspTrFecStackFecIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamLspTrFecStackFecIndex.setStatus("current")


class _TmnxOamLspTrFecStackOperType_Type(Integer32):
    """Custom type tmnxOamLspTrFecStackOperType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("push", 1),
          ("pop", 2))
    )


_TmnxOamLspTrFecStackOperType_Type.__name__ = "Integer32"
_TmnxOamLspTrFecStackOperType_Object = MibTableColumn
tmnxOamLspTrFecStackOperType = _TmnxOamLspTrFecStackOperType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 33, 1, 2),
    _TmnxOamLspTrFecStackOperType_Type()
)
tmnxOamLspTrFecStackOperType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLspTrFecStackOperType.setStatus("current")
_TmnxOamLspTrFecStackFecSubType_Type = TNamedItemOrEmpty
_TmnxOamLspTrFecStackFecSubType_Object = MibTableColumn
tmnxOamLspTrFecStackFecSubType = _TmnxOamLspTrFecStackFecSubType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 33, 1, 3),
    _TmnxOamLspTrFecStackFecSubType_Type()
)
tmnxOamLspTrFecStackFecSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLspTrFecStackFecSubType.setStatus("current")
_TmnxOamLspTrFecStackPrefixType_Type = InetAddressType
_TmnxOamLspTrFecStackPrefixType_Object = MibTableColumn
tmnxOamLspTrFecStackPrefixType = _TmnxOamLspTrFecStackPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 33, 1, 4),
    _TmnxOamLspTrFecStackPrefixType_Type()
)
tmnxOamLspTrFecStackPrefixType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLspTrFecStackPrefixType.setStatus("current")


class _TmnxOamLspTrFecStackPrefix_Type(InetAddress):
    """Custom type tmnxOamLspTrFecStackPrefix based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamLspTrFecStackPrefix_Type.__name__ = "InetAddress"
_TmnxOamLspTrFecStackPrefix_Object = MibTableColumn
tmnxOamLspTrFecStackPrefix = _TmnxOamLspTrFecStackPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 33, 1, 5),
    _TmnxOamLspTrFecStackPrefix_Type()
)
tmnxOamLspTrFecStackPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLspTrFecStackPrefix.setStatus("current")
_TmnxOamLspTrFecStackPrefixLen_Type = InetAddressPrefixLength
_TmnxOamLspTrFecStackPrefixLen_Object = MibTableColumn
tmnxOamLspTrFecStackPrefixLen = _TmnxOamLspTrFecStackPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 33, 1, 6),
    _TmnxOamLspTrFecStackPrefixLen_Type()
)
tmnxOamLspTrFecStackPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLspTrFecStackPrefixLen.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamLspTrFecStackPrefixLen.setUnits("bits")
_TmnxOamLspTrFecStackRemPeerAddrT_Type = InetAddressType
_TmnxOamLspTrFecStackRemPeerAddrT_Object = MibTableColumn
tmnxOamLspTrFecStackRemPeerAddrT = _TmnxOamLspTrFecStackRemPeerAddrT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 33, 1, 7),
    _TmnxOamLspTrFecStackRemPeerAddrT_Type()
)
tmnxOamLspTrFecStackRemPeerAddrT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLspTrFecStackRemPeerAddrT.setStatus("current")


class _TmnxOamLspTrFecStackRemPeerAddr_Type(InetAddress):
    """Custom type tmnxOamLspTrFecStackRemPeerAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamLspTrFecStackRemPeerAddr_Type.__name__ = "InetAddress"
_TmnxOamLspTrFecStackRemPeerAddr_Object = MibTableColumn
tmnxOamLspTrFecStackRemPeerAddr = _TmnxOamLspTrFecStackRemPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 33, 1, 8),
    _TmnxOamLspTrFecStackRemPeerAddr_Type()
)
tmnxOamLspTrFecStackRemPeerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLspTrFecStackRemPeerAddr.setStatus("current")
_TmnxOamVccvTrTgFec128CtlTable_Object = MibTable
tmnxOamVccvTrTgFec128CtlTable = _TmnxOamVccvTrTgFec128CtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 34)
)
if mibBuilder.loadTexts:
    tmnxOamVccvTrTgFec128CtlTable.setStatus("current")
_TmnxOamVccvTrTgFec128CtlEntry_Object = MibTableRow
tmnxOamVccvTrTgFec128CtlEntry = _TmnxOamVccvTrTgFec128CtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 34, 1)
)
tmnxOamVccvTrTgFec128CtlEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamVccvTrTgFec128CtlEntry.setStatus("current")


class _TmnxOamVccvTrTgFec128CtlSrcAddrT_Type(InetAddressType):
    """Custom type tmnxOamVccvTrTgFec128CtlSrcAddrT based on InetAddressType"""
    defaultValue = 0


_TmnxOamVccvTrTgFec128CtlSrcAddrT_Type.__name__ = "InetAddressType"
_TmnxOamVccvTrTgFec128CtlSrcAddrT_Object = MibTableColumn
tmnxOamVccvTrTgFec128CtlSrcAddrT = _TmnxOamVccvTrTgFec128CtlSrcAddrT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 34, 1, 1),
    _TmnxOamVccvTrTgFec128CtlSrcAddrT_Type()
)
tmnxOamVccvTrTgFec128CtlSrcAddrT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamVccvTrTgFec128CtlSrcAddrT.setStatus("current")


class _TmnxOamVccvTrTgFec128CtlSrcAddr_Type(InetAddress):
    """Custom type tmnxOamVccvTrTgFec128CtlSrcAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamVccvTrTgFec128CtlSrcAddr_Type.__name__ = "InetAddress"
_TmnxOamVccvTrTgFec128CtlSrcAddr_Object = MibTableColumn
tmnxOamVccvTrTgFec128CtlSrcAddr = _TmnxOamVccvTrTgFec128CtlSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 34, 1, 2),
    _TmnxOamVccvTrTgFec128CtlSrcAddr_Type()
)
tmnxOamVccvTrTgFec128CtlSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamVccvTrTgFec128CtlSrcAddr.setStatus("current")


class _TmnxOamVccvTrTgFec128CtlDstAddrT_Type(InetAddressType):
    """Custom type tmnxOamVccvTrTgFec128CtlDstAddrT based on InetAddressType"""
    defaultValue = 0


_TmnxOamVccvTrTgFec128CtlDstAddrT_Type.__name__ = "InetAddressType"
_TmnxOamVccvTrTgFec128CtlDstAddrT_Object = MibTableColumn
tmnxOamVccvTrTgFec128CtlDstAddrT = _TmnxOamVccvTrTgFec128CtlDstAddrT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 34, 1, 3),
    _TmnxOamVccvTrTgFec128CtlDstAddrT_Type()
)
tmnxOamVccvTrTgFec128CtlDstAddrT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamVccvTrTgFec128CtlDstAddrT.setStatus("current")


class _TmnxOamVccvTrTgFec128CtlDstAddr_Type(InetAddress):
    """Custom type tmnxOamVccvTrTgFec128CtlDstAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamVccvTrTgFec128CtlDstAddr_Type.__name__ = "InetAddress"
_TmnxOamVccvTrTgFec128CtlDstAddr_Object = MibTableColumn
tmnxOamVccvTrTgFec128CtlDstAddr = _TmnxOamVccvTrTgFec128CtlDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 34, 1, 4),
    _TmnxOamVccvTrTgFec128CtlDstAddr_Type()
)
tmnxOamVccvTrTgFec128CtlDstAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamVccvTrTgFec128CtlDstAddr.setStatus("current")


class _TmnxOamVccvTrTgFec128CtlPwId_Type(Unsigned32):
    """Custom type tmnxOamVccvTrTgFec128CtlPwId based on Unsigned32"""
    defaultValue = 0


_TmnxOamVccvTrTgFec128CtlPwId_Type.__name__ = "Unsigned32"
_TmnxOamVccvTrTgFec128CtlPwId_Object = MibTableColumn
tmnxOamVccvTrTgFec128CtlPwId = _TmnxOamVccvTrTgFec128CtlPwId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 34, 1, 5),
    _TmnxOamVccvTrTgFec128CtlPwId_Type()
)
tmnxOamVccvTrTgFec128CtlPwId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamVccvTrTgFec128CtlPwId.setStatus("current")


class _TmnxOamVccvTrTgFec128CtlPwType_Type(Unsigned32):
    """Custom type tmnxOamVccvTrTgFec128CtlPwType based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TmnxOamVccvTrTgFec128CtlPwType_Type.__name__ = "Unsigned32"
_TmnxOamVccvTrTgFec128CtlPwType_Object = MibTableColumn
tmnxOamVccvTrTgFec128CtlPwType = _TmnxOamVccvTrTgFec128CtlPwType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 34, 1, 6),
    _TmnxOamVccvTrTgFec128CtlPwType_Type()
)
tmnxOamVccvTrTgFec128CtlPwType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamVccvTrTgFec128CtlPwType.setStatus("current")
_TmnxOamVccvTrTgStaticCtlTable_Object = MibTable
tmnxOamVccvTrTgStaticCtlTable = _TmnxOamVccvTrTgStaticCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 35)
)
if mibBuilder.loadTexts:
    tmnxOamVccvTrTgStaticCtlTable.setStatus("current")
_TmnxOamVccvTrTgStaticCtlEntry_Object = MibTableRow
tmnxOamVccvTrTgStaticCtlEntry = _TmnxOamVccvTrTgStaticCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 35, 1)
)
tmnxOamVccvTrTgStaticCtlEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamVccvTrTgStaticCtlEntry.setStatus("current")


class _TmnxOamVccvTrTgStaticCtlAgi_Type(TmnxVPNRouteDistinguisher):
    """Custom type tmnxOamVccvTrTgStaticCtlAgi based on TmnxVPNRouteDistinguisher"""
    defaultHexValue = "0000000000000000"


_TmnxOamVccvTrTgStaticCtlAgi_Type.__name__ = "TmnxVPNRouteDistinguisher"
_TmnxOamVccvTrTgStaticCtlAgi_Object = MibTableColumn
tmnxOamVccvTrTgStaticCtlAgi = _TmnxOamVccvTrTgStaticCtlAgi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 35, 1, 1),
    _TmnxOamVccvTrTgStaticCtlAgi_Type()
)
tmnxOamVccvTrTgStaticCtlAgi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamVccvTrTgStaticCtlAgi.setStatus("current")


class _TmnxOamVccvTrTgStaticCtlSaiiGlbl_Type(TmnxPwGlobalIdOrZero):
    """Custom type tmnxOamVccvTrTgStaticCtlSaiiGlbl based on TmnxPwGlobalIdOrZero"""
    defaultValue = 0


_TmnxOamVccvTrTgStaticCtlSaiiGlbl_Type.__name__ = "TmnxPwGlobalIdOrZero"
_TmnxOamVccvTrTgStaticCtlSaiiGlbl_Object = MibTableColumn
tmnxOamVccvTrTgStaticCtlSaiiGlbl = _TmnxOamVccvTrTgStaticCtlSaiiGlbl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 35, 1, 2),
    _TmnxOamVccvTrTgStaticCtlSaiiGlbl_Type()
)
tmnxOamVccvTrTgStaticCtlSaiiGlbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamVccvTrTgStaticCtlSaiiGlbl.setStatus("current")


class _TmnxOamVccvTrTgStaticCtlSaiiNode_Type(TmnxMplsTpNodeID):
    """Custom type tmnxOamVccvTrTgStaticCtlSaiiNode based on TmnxMplsTpNodeID"""
    defaultValue = 0


_TmnxOamVccvTrTgStaticCtlSaiiNode_Type.__name__ = "TmnxMplsTpNodeID"
_TmnxOamVccvTrTgStaticCtlSaiiNode_Object = MibTableColumn
tmnxOamVccvTrTgStaticCtlSaiiNode = _TmnxOamVccvTrTgStaticCtlSaiiNode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 35, 1, 3),
    _TmnxOamVccvTrTgStaticCtlSaiiNode_Type()
)
tmnxOamVccvTrTgStaticCtlSaiiNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamVccvTrTgStaticCtlSaiiNode.setStatus("current")


class _TmnxOamVccvTrTgStaticCtlSaiiAcId_Type(Unsigned32):
    """Custom type tmnxOamVccvTrTgStaticCtlSaiiAcId based on Unsigned32"""
    defaultValue = 0


_TmnxOamVccvTrTgStaticCtlSaiiAcId_Type.__name__ = "Unsigned32"
_TmnxOamVccvTrTgStaticCtlSaiiAcId_Object = MibTableColumn
tmnxOamVccvTrTgStaticCtlSaiiAcId = _TmnxOamVccvTrTgStaticCtlSaiiAcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 35, 1, 4),
    _TmnxOamVccvTrTgStaticCtlSaiiAcId_Type()
)
tmnxOamVccvTrTgStaticCtlSaiiAcId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamVccvTrTgStaticCtlSaiiAcId.setStatus("current")


class _TmnxOamVccvTrTgStaticCtlTaiiGlbl_Type(TmnxPwGlobalIdOrZero):
    """Custom type tmnxOamVccvTrTgStaticCtlTaiiGlbl based on TmnxPwGlobalIdOrZero"""
    defaultValue = 0


_TmnxOamVccvTrTgStaticCtlTaiiGlbl_Type.__name__ = "TmnxPwGlobalIdOrZero"
_TmnxOamVccvTrTgStaticCtlTaiiGlbl_Object = MibTableColumn
tmnxOamVccvTrTgStaticCtlTaiiGlbl = _TmnxOamVccvTrTgStaticCtlTaiiGlbl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 35, 1, 5),
    _TmnxOamVccvTrTgStaticCtlTaiiGlbl_Type()
)
tmnxOamVccvTrTgStaticCtlTaiiGlbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamVccvTrTgStaticCtlTaiiGlbl.setStatus("current")


class _TmnxOamVccvTrTgStaticCtlTaiiNode_Type(TmnxMplsTpNodeID):
    """Custom type tmnxOamVccvTrTgStaticCtlTaiiNode based on TmnxMplsTpNodeID"""
    defaultValue = 0


_TmnxOamVccvTrTgStaticCtlTaiiNode_Type.__name__ = "TmnxMplsTpNodeID"
_TmnxOamVccvTrTgStaticCtlTaiiNode_Object = MibTableColumn
tmnxOamVccvTrTgStaticCtlTaiiNode = _TmnxOamVccvTrTgStaticCtlTaiiNode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 35, 1, 6),
    _TmnxOamVccvTrTgStaticCtlTaiiNode_Type()
)
tmnxOamVccvTrTgStaticCtlTaiiNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamVccvTrTgStaticCtlTaiiNode.setStatus("current")


class _TmnxOamVccvTrTgStaticCtlTaiiAcId_Type(Unsigned32):
    """Custom type tmnxOamVccvTrTgStaticCtlTaiiAcId based on Unsigned32"""
    defaultValue = 0


_TmnxOamVccvTrTgStaticCtlTaiiAcId_Type.__name__ = "Unsigned32"
_TmnxOamVccvTrTgStaticCtlTaiiAcId_Object = MibTableColumn
tmnxOamVccvTrTgStaticCtlTaiiAcId = _TmnxOamVccvTrTgStaticCtlTaiiAcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 35, 1, 7),
    _TmnxOamVccvTrTgStaticCtlTaiiAcId_Type()
)
tmnxOamVccvTrTgStaticCtlTaiiAcId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamVccvTrTgStaticCtlTaiiAcId.setStatus("current")
_TmnxOamIcmpTrLabelStackTable_Object = MibTable
tmnxOamIcmpTrLabelStackTable = _TmnxOamIcmpTrLabelStackTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 36)
)
if mibBuilder.loadTexts:
    tmnxOamIcmpTrLabelStackTable.setStatus("current")
_TmnxOamIcmpTrLabelStackEntry_Object = MibTableRow
tmnxOamIcmpTrLabelStackEntry = _TmnxOamIcmpTrLabelStackEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 36, 1)
)
tmnxOamIcmpTrLabelStackEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsTestRunIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryHopIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryProbeIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamIcmpTrLabelStackMemberNum"),
)
if mibBuilder.loadTexts:
    tmnxOamIcmpTrLabelStackEntry.setStatus("current")


class _TmnxOamIcmpTrLabelStackMemberNum_Type(Unsigned32):
    """Custom type tmnxOamIcmpTrLabelStackMemberNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxOamIcmpTrLabelStackMemberNum_Type.__name__ = "Unsigned32"
_TmnxOamIcmpTrLabelStackMemberNum_Object = MibTableColumn
tmnxOamIcmpTrLabelStackMemberNum = _TmnxOamIcmpTrLabelStackMemberNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 36, 1, 1),
    _TmnxOamIcmpTrLabelStackMemberNum_Type()
)
tmnxOamIcmpTrLabelStackMemberNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamIcmpTrLabelStackMemberNum.setStatus("current")


class _TmnxOamIcmpTrLabelStackLabel_Type(Unsigned32):
    """Custom type tmnxOamIcmpTrLabelStackLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_TmnxOamIcmpTrLabelStackLabel_Type.__name__ = "Unsigned32"
_TmnxOamIcmpTrLabelStackLabel_Object = MibTableColumn
tmnxOamIcmpTrLabelStackLabel = _TmnxOamIcmpTrLabelStackLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 36, 1, 2),
    _TmnxOamIcmpTrLabelStackLabel_Type()
)
tmnxOamIcmpTrLabelStackLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamIcmpTrLabelStackLabel.setStatus("current")


class _TmnxOamIcmpTrLabelStackExperimnt_Type(Unsigned32):
    """Custom type tmnxOamIcmpTrLabelStackExperimnt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TmnxOamIcmpTrLabelStackExperimnt_Type.__name__ = "Unsigned32"
_TmnxOamIcmpTrLabelStackExperimnt_Object = MibTableColumn
tmnxOamIcmpTrLabelStackExperimnt = _TmnxOamIcmpTrLabelStackExperimnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 36, 1, 3),
    _TmnxOamIcmpTrLabelStackExperimnt_Type()
)
tmnxOamIcmpTrLabelStackExperimnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamIcmpTrLabelStackExperimnt.setStatus("current")


class _TmnxOamIcmpTrLabelStackBottom_Type(Unsigned32):
    """Custom type tmnxOamIcmpTrLabelStackBottom based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_TmnxOamIcmpTrLabelStackBottom_Type.__name__ = "Unsigned32"
_TmnxOamIcmpTrLabelStackBottom_Object = MibTableColumn
tmnxOamIcmpTrLabelStackBottom = _TmnxOamIcmpTrLabelStackBottom_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 36, 1, 4),
    _TmnxOamIcmpTrLabelStackBottom_Type()
)
tmnxOamIcmpTrLabelStackBottom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamIcmpTrLabelStackBottom.setStatus("current")


class _TmnxOamIcmpTrLabelStackTtl_Type(Unsigned32):
    """Custom type tmnxOamIcmpTrLabelStackTtl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxOamIcmpTrLabelStackTtl_Type.__name__ = "Unsigned32"
_TmnxOamIcmpTrLabelStackTtl_Object = MibTableColumn
tmnxOamIcmpTrLabelStackTtl = _TmnxOamIcmpTrLabelStackTtl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 36, 1, 5),
    _TmnxOamIcmpTrLabelStackTtl_Type()
)
tmnxOamIcmpTrLabelStackTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamIcmpTrLabelStackTtl.setStatus("current")
_TmnxOamBierTrCtlTable_Object = MibTable
tmnxOamBierTrCtlTable = _TmnxOamBierTrCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 37)
)
if mibBuilder.loadTexts:
    tmnxOamBierTrCtlTable.setStatus("current")
_TmnxOamBierTrCtlEntry_Object = MibTableRow
tmnxOamBierTrCtlEntry = _TmnxOamBierTrCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 37, 1)
)
tmnxOamBierTrCtlEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamBierTrCtlEntry.setStatus("current")


class _TmnxOamBierTrCtlSubDomain_Type(Unsigned32):
    """Custom type tmnxOamBierTrCtlSubDomain based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxOamBierTrCtlSubDomain_Type.__name__ = "Unsigned32"
_TmnxOamBierTrCtlSubDomain_Object = MibTableColumn
tmnxOamBierTrCtlSubDomain = _TmnxOamBierTrCtlSubDomain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 37, 1, 1),
    _TmnxOamBierTrCtlSubDomain_Type()
)
tmnxOamBierTrCtlSubDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamBierTrCtlSubDomain.setStatus("current")


class _TmnxOamBierTrCtlBfrId_Type(Unsigned32):
    """Custom type tmnxOamBierTrCtlBfrId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_TmnxOamBierTrCtlBfrId_Type.__name__ = "Unsigned32"
_TmnxOamBierTrCtlBfrId_Object = MibTableColumn
tmnxOamBierTrCtlBfrId = _TmnxOamBierTrCtlBfrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 37, 1, 2),
    _TmnxOamBierTrCtlBfrId_Type()
)
tmnxOamBierTrCtlBfrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamBierTrCtlBfrId.setStatus("current")


class _TmnxOamBierTrCtlBfrPfxAddrType_Type(InetAddressType):
    """Custom type tmnxOamBierTrCtlBfrPfxAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxOamBierTrCtlBfrPfxAddrType_Type.__name__ = "InetAddressType"
_TmnxOamBierTrCtlBfrPfxAddrType_Object = MibTableColumn
tmnxOamBierTrCtlBfrPfxAddrType = _TmnxOamBierTrCtlBfrPfxAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 37, 1, 3),
    _TmnxOamBierTrCtlBfrPfxAddrType_Type()
)
tmnxOamBierTrCtlBfrPfxAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamBierTrCtlBfrPfxAddrType.setStatus("current")


class _TmnxOamBierTrCtlBfrPfxAddress_Type(InetAddress):
    """Custom type tmnxOamBierTrCtlBfrPfxAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamBierTrCtlBfrPfxAddress_Type.__name__ = "InetAddress"
_TmnxOamBierTrCtlBfrPfxAddress_Object = MibTableColumn
tmnxOamBierTrCtlBfrPfxAddress = _TmnxOamBierTrCtlBfrPfxAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 37, 1, 4),
    _TmnxOamBierTrCtlBfrPfxAddress_Type()
)
tmnxOamBierTrCtlBfrPfxAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamBierTrCtlBfrPfxAddress.setStatus("current")
_TmnxOamBierTrProbeHistoryTable_Object = MibTable
tmnxOamBierTrProbeHistoryTable = _TmnxOamBierTrProbeHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 38)
)
if mibBuilder.loadTexts:
    tmnxOamBierTrProbeHistoryTable.setStatus("current")
_TmnxOamBierTrProbeHistoryEntry_Object = MibTableRow
tmnxOamBierTrProbeHistoryEntry = _TmnxOamBierTrProbeHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 38, 1)
)
tmnxOamBierTrProbeHistoryEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsTestRunIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryHopIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryProbeIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamBierTrProbeHistoryEntry.setStatus("current")


class _TmnxOamBierTrHistoryBfrId_Type(Unsigned32):
    """Custom type tmnxOamBierTrHistoryBfrId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_TmnxOamBierTrHistoryBfrId_Type.__name__ = "Unsigned32"
_TmnxOamBierTrHistoryBfrId_Object = MibTableColumn
tmnxOamBierTrHistoryBfrId = _TmnxOamBierTrHistoryBfrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 38, 1, 1),
    _TmnxOamBierTrHistoryBfrId_Type()
)
tmnxOamBierTrHistoryBfrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamBierTrHistoryBfrId.setStatus("current")
_TmnxOamBierTrHistoryReturnCode_Type = TmnxOamBierHistoryReturnCode
_TmnxOamBierTrHistoryReturnCode_Object = MibTableColumn
tmnxOamBierTrHistoryReturnCode = _TmnxOamBierTrHistoryReturnCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 38, 1, 2),
    _TmnxOamBierTrHistoryReturnCode_Type()
)
tmnxOamBierTrHistoryReturnCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamBierTrHistoryReturnCode.setStatus("current")
_TmnxOamBierTrHistoryUpStrIfAddrT_Type = InetAddressType
_TmnxOamBierTrHistoryUpStrIfAddrT_Object = MibTableColumn
tmnxOamBierTrHistoryUpStrIfAddrT = _TmnxOamBierTrHistoryUpStrIfAddrT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 38, 1, 3),
    _TmnxOamBierTrHistoryUpStrIfAddrT_Type()
)
tmnxOamBierTrHistoryUpStrIfAddrT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamBierTrHistoryUpStrIfAddrT.setStatus("current")


class _TmnxOamBierTrHistoryUpStrIfAddr_Type(InetAddress):
    """Custom type tmnxOamBierTrHistoryUpStrIfAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamBierTrHistoryUpStrIfAddr_Type.__name__ = "InetAddress"
_TmnxOamBierTrHistoryUpStrIfAddr_Object = MibTableColumn
tmnxOamBierTrHistoryUpStrIfAddr = _TmnxOamBierTrHistoryUpStrIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 38, 1, 4),
    _TmnxOamBierTrHistoryUpStrIfAddr_Type()
)
tmnxOamBierTrHistoryUpStrIfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamBierTrHistoryUpStrIfAddr.setStatus("current")
_TmnxOamBierTrHistoryUpStrIfNum_Type = Unsigned32
_TmnxOamBierTrHistoryUpStrIfNum_Object = MibTableColumn
tmnxOamBierTrHistoryUpStrIfNum = _TmnxOamBierTrHistoryUpStrIfNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 38, 1, 5),
    _TmnxOamBierTrHistoryUpStrIfNum_Type()
)
tmnxOamBierTrHistoryUpStrIfNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamBierTrHistoryUpStrIfNum.setStatus("current")
_TmnxOamBierTrHistoryDnStrAddrTyp_Type = InetAddressType
_TmnxOamBierTrHistoryDnStrAddrTyp_Object = MibTableColumn
tmnxOamBierTrHistoryDnStrAddrTyp = _TmnxOamBierTrHistoryDnStrAddrTyp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 38, 1, 6),
    _TmnxOamBierTrHistoryDnStrAddrTyp_Type()
)
tmnxOamBierTrHistoryDnStrAddrTyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamBierTrHistoryDnStrAddrTyp.setStatus("current")


class _TmnxOamBierTrHistoryDnStrAddr_Type(InetAddress):
    """Custom type tmnxOamBierTrHistoryDnStrAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamBierTrHistoryDnStrAddr_Type.__name__ = "InetAddress"
_TmnxOamBierTrHistoryDnStrAddr_Object = MibTableColumn
tmnxOamBierTrHistoryDnStrAddr = _TmnxOamBierTrHistoryDnStrAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 38, 1, 7),
    _TmnxOamBierTrHistoryDnStrAddr_Type()
)
tmnxOamBierTrHistoryDnStrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamBierTrHistoryDnStrAddr.setStatus("current")
_TmnxOamBierTrHistoryDnStrIfAddrT_Type = InetAddressType
_TmnxOamBierTrHistoryDnStrIfAddrT_Object = MibTableColumn
tmnxOamBierTrHistoryDnStrIfAddrT = _TmnxOamBierTrHistoryDnStrIfAddrT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 38, 1, 8),
    _TmnxOamBierTrHistoryDnStrIfAddrT_Type()
)
tmnxOamBierTrHistoryDnStrIfAddrT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamBierTrHistoryDnStrIfAddrT.setStatus("current")


class _TmnxOamBierTrHistoryDnStrIfAddr_Type(InetAddress):
    """Custom type tmnxOamBierTrHistoryDnStrIfAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamBierTrHistoryDnStrIfAddr_Type.__name__ = "InetAddress"
_TmnxOamBierTrHistoryDnStrIfAddr_Object = MibTableColumn
tmnxOamBierTrHistoryDnStrIfAddr = _TmnxOamBierTrHistoryDnStrIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 38, 1, 9),
    _TmnxOamBierTrHistoryDnStrIfAddr_Type()
)
tmnxOamBierTrHistoryDnStrIfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamBierTrHistoryDnStrIfAddr.setStatus("current")
_TmnxOamBierTrHistoryDnStrIfNum_Type = Unsigned32
_TmnxOamBierTrHistoryDnStrIfNum_Object = MibTableColumn
tmnxOamBierTrHistoryDnStrIfNum = _TmnxOamBierTrHistoryDnStrIfNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 38, 1, 10),
    _TmnxOamBierTrHistoryDnStrIfNum_Type()
)
tmnxOamBierTrHistoryDnStrIfNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamBierTrHistoryDnStrIfNum.setStatus("current")
_TmnxOamIcmpTrCtlTable_Object = MibTable
tmnxOamIcmpTrCtlTable = _TmnxOamIcmpTrCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 39)
)
if mibBuilder.loadTexts:
    tmnxOamIcmpTrCtlTable.setStatus("current")
_TmnxOamIcmpTrCtlEntry_Object = MibTableRow
tmnxOamIcmpTrCtlEntry = _TmnxOamIcmpTrCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 39, 1)
)
tmnxOamIcmpTrCtlEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamIcmpTrCtlEntry.setStatus("current")


class _TmnxOamIcmpTrCtlProtocol_Type(Integer32):
    """Custom type tmnxOamIcmpTrCtlProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("udp", 1),
          ("tcp", 2))
    )


_TmnxOamIcmpTrCtlProtocol_Type.__name__ = "Integer32"
_TmnxOamIcmpTrCtlProtocol_Object = MibTableColumn
tmnxOamIcmpTrCtlProtocol = _TmnxOamIcmpTrCtlProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 39, 1, 1),
    _TmnxOamIcmpTrCtlProtocol_Type()
)
tmnxOamIcmpTrCtlProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamIcmpTrCtlProtocol.setStatus("current")


class _TmnxOamIcmpTrCtlDestTcpUdpPort_Type(Unsigned32):
    """Custom type tmnxOamIcmpTrCtlDestTcpUdpPort based on Unsigned32"""
    defaultValue = 33434

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmnxOamIcmpTrCtlDestTcpUdpPort_Type.__name__ = "Unsigned32"
_TmnxOamIcmpTrCtlDestTcpUdpPort_Object = MibTableColumn
tmnxOamIcmpTrCtlDestTcpUdpPort = _TmnxOamIcmpTrCtlDestTcpUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 39, 1, 2),
    _TmnxOamIcmpTrCtlDestTcpUdpPort_Type()
)
tmnxOamIcmpTrCtlDestTcpUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamIcmpTrCtlDestTcpUdpPort.setStatus("current")


class _TmnxOamIcmpTrCtlDestUdpPortFixed_Type(TruthValue):
    """Custom type tmnxOamIcmpTrCtlDestUdpPortFixed based on TruthValue"""
    defaultValue = 2


_TmnxOamIcmpTrCtlDestUdpPortFixed_Type.__name__ = "TruthValue"
_TmnxOamIcmpTrCtlDestUdpPortFixed_Object = MibTableColumn
tmnxOamIcmpTrCtlDestUdpPortFixed = _TmnxOamIcmpTrCtlDestUdpPortFixed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 39, 1, 3),
    _TmnxOamIcmpTrCtlDestUdpPortFixed_Type()
)
tmnxOamIcmpTrCtlDestUdpPortFixed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamIcmpTrCtlDestUdpPortFixed.setStatus("current")


class _TmnxOamIcmpTrCtlPadSize_Type(Unsigned32):
    """Custom type tmnxOamIcmpTrCtlPadSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9786),
    )


_TmnxOamIcmpTrCtlPadSize_Type.__name__ = "Unsigned32"
_TmnxOamIcmpTrCtlPadSize_Object = MibTableColumn
tmnxOamIcmpTrCtlPadSize = _TmnxOamIcmpTrCtlPadSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 39, 1, 4),
    _TmnxOamIcmpTrCtlPadSize_Type()
)
tmnxOamIcmpTrCtlPadSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamIcmpTrCtlPadSize.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamIcmpTrCtlPadSize.setUnits("octets")
_TmnxOamSaaObjs_ObjectIdentity = ObjectIdentity
tmnxOamSaaObjs = _TmnxOamSaaObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 3)
)
_TmnxOamSaaNotifyObjects_ObjectIdentity = ObjectIdentity
tmnxOamSaaNotifyObjects = _TmnxOamSaaNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 3, 1)
)
_TmnxOamSaaCtlTable_Object = MibTable
tmnxOamSaaCtlTable = _TmnxOamSaaCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 3, 2)
)
if mibBuilder.loadTexts:
    tmnxOamSaaCtlTable.setStatus("current")
_TmnxOamSaaCtlEntry_Object = MibTableRow
tmnxOamSaaCtlEntry = _TmnxOamSaaCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 3, 2, 1)
)
tmnxOamSaaCtlEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamSaaCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamSaaCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamSaaCtlEntry.setStatus("current")


class _TmnxOamSaaCtlOwnerIndex_Type(SnmpAdminString):
    """Custom type tmnxOamSaaCtlOwnerIndex based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TmnxOamSaaCtlOwnerIndex_Type.__name__ = "SnmpAdminString"
_TmnxOamSaaCtlOwnerIndex_Object = MibTableColumn
tmnxOamSaaCtlOwnerIndex = _TmnxOamSaaCtlOwnerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 3, 2, 1, 1),
    _TmnxOamSaaCtlOwnerIndex_Type()
)
tmnxOamSaaCtlOwnerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamSaaCtlOwnerIndex.setStatus("current")


class _TmnxOamSaaCtlTestIndex_Type(SnmpAdminString):
    """Custom type tmnxOamSaaCtlTestIndex based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TmnxOamSaaCtlTestIndex_Type.__name__ = "SnmpAdminString"
_TmnxOamSaaCtlTestIndex_Object = MibTableColumn
tmnxOamSaaCtlTestIndex = _TmnxOamSaaCtlTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 3, 2, 1, 2),
    _TmnxOamSaaCtlTestIndex_Type()
)
tmnxOamSaaCtlTestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamSaaCtlTestIndex.setStatus("current")
_TmnxOamSaaCtlRowStatus_Type = RowStatus
_TmnxOamSaaCtlRowStatus_Object = MibTableColumn
tmnxOamSaaCtlRowStatus = _TmnxOamSaaCtlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 3, 2, 1, 3),
    _TmnxOamSaaCtlRowStatus_Type()
)
tmnxOamSaaCtlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamSaaCtlRowStatus.setStatus("current")


class _TmnxOamSaaCtlStorageType_Type(StorageType):
    """Custom type tmnxOamSaaCtlStorageType based on StorageType"""
    defaultValue = 3


_TmnxOamSaaCtlStorageType_Type.__name__ = "StorageType"
_TmnxOamSaaCtlStorageType_Object = MibTableColumn
tmnxOamSaaCtlStorageType = _TmnxOamSaaCtlStorageType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 3, 2, 1, 4),
    _TmnxOamSaaCtlStorageType_Type()
)
tmnxOamSaaCtlStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamSaaCtlStorageType.setStatus("obsolete")
_TmnxOamSaaCtlLastChanged_Type = TimeStamp
_TmnxOamSaaCtlLastChanged_Object = MibTableColumn
tmnxOamSaaCtlLastChanged = _TmnxOamSaaCtlLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 3, 2, 1, 5),
    _TmnxOamSaaCtlLastChanged_Type()
)
tmnxOamSaaCtlLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamSaaCtlLastChanged.setStatus("current")


class _TmnxOamSaaCtlAdminStatus_Type(TmnxAdminState):
    """Custom type tmnxOamSaaCtlAdminStatus based on TmnxAdminState"""
    defaultValue = 3


_TmnxOamSaaCtlAdminStatus_Type.__name__ = "TmnxAdminState"
_TmnxOamSaaCtlAdminStatus_Object = MibTableColumn
tmnxOamSaaCtlAdminStatus = _TmnxOamSaaCtlAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 3, 2, 1, 6),
    _TmnxOamSaaCtlAdminStatus_Type()
)
tmnxOamSaaCtlAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamSaaCtlAdminStatus.setStatus("current")


class _TmnxOamSaaCtlDescr_Type(TItemDescription):
    """Custom type tmnxOamSaaCtlDescr based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxOamSaaCtlDescr_Type.__name__ = "TItemDescription"
_TmnxOamSaaCtlDescr_Object = MibTableColumn
tmnxOamSaaCtlDescr = _TmnxOamSaaCtlDescr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 3, 2, 1, 7),
    _TmnxOamSaaCtlDescr_Type()
)
tmnxOamSaaCtlDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamSaaCtlDescr.setStatus("current")


class _TmnxOamSaaCtlTestMode_Type(TmnxOamTestMode):
    """Custom type tmnxOamSaaCtlTestMode based on TmnxOamTestMode"""
    defaultValue = 0


_TmnxOamSaaCtlTestMode_Type.__name__ = "TmnxOamTestMode"
_TmnxOamSaaCtlTestMode_Object = MibTableColumn
tmnxOamSaaCtlTestMode = _TmnxOamSaaCtlTestMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 3, 2, 1, 8),
    _TmnxOamSaaCtlTestMode_Type()
)
tmnxOamSaaCtlTestMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamSaaCtlTestMode.setStatus("current")
_TmnxOamSaaCtlRuns_Type = Counter32
_TmnxOamSaaCtlRuns_Object = MibTableColumn
tmnxOamSaaCtlRuns = _TmnxOamSaaCtlRuns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 3, 2, 1, 9),
    _TmnxOamSaaCtlRuns_Type()
)
tmnxOamSaaCtlRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamSaaCtlRuns.setStatus("current")
_TmnxOamSaaCtlFailures_Type = Counter32
_TmnxOamSaaCtlFailures_Object = MibTableColumn
tmnxOamSaaCtlFailures = _TmnxOamSaaCtlFailures_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 3, 2, 1, 10),
    _TmnxOamSaaCtlFailures_Type()
)
tmnxOamSaaCtlFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamSaaCtlFailures.setStatus("current")
_TmnxOamSaaCtlLastRunResult_Type = TmnxOamTestResult
_TmnxOamSaaCtlLastRunResult_Object = MibTableColumn
tmnxOamSaaCtlLastRunResult = _TmnxOamSaaCtlLastRunResult_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 3, 2, 1, 11),
    _TmnxOamSaaCtlLastRunResult_Type()
)
tmnxOamSaaCtlLastRunResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamSaaCtlLastRunResult.setStatus("current")


class _TmnxOamSaaCtlAcctPolicyId_Type(Integer32):
    """Custom type tmnxOamSaaCtlAcctPolicyId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_TmnxOamSaaCtlAcctPolicyId_Type.__name__ = "Integer32"
_TmnxOamSaaCtlAcctPolicyId_Object = MibTableColumn
tmnxOamSaaCtlAcctPolicyId = _TmnxOamSaaCtlAcctPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 3, 2, 1, 12),
    _TmnxOamSaaCtlAcctPolicyId_Type()
)
tmnxOamSaaCtlAcctPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamSaaCtlAcctPolicyId.setStatus("current")


class _TmnxOamSaaCtlSuppressAccounting_Type(TruthValue):
    """Custom type tmnxOamSaaCtlSuppressAccounting based on TruthValue"""
    defaultValue = 2


_TmnxOamSaaCtlSuppressAccounting_Type.__name__ = "TruthValue"
_TmnxOamSaaCtlSuppressAccounting_Object = MibTableColumn
tmnxOamSaaCtlSuppressAccounting = _TmnxOamSaaCtlSuppressAccounting_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 3, 2, 1, 13),
    _TmnxOamSaaCtlSuppressAccounting_Type()
)
tmnxOamSaaCtlSuppressAccounting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamSaaCtlSuppressAccounting.setStatus("current")


class _TmnxOamSaaCtlContinuous_Type(TruthValue):
    """Custom type tmnxOamSaaCtlContinuous based on TruthValue"""
    defaultValue = 2


_TmnxOamSaaCtlContinuous_Type.__name__ = "TruthValue"
_TmnxOamSaaCtlContinuous_Object = MibTableColumn
tmnxOamSaaCtlContinuous = _TmnxOamSaaCtlContinuous_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 3, 2, 1, 14),
    _TmnxOamSaaCtlContinuous_Type()
)
tmnxOamSaaCtlContinuous.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamSaaCtlContinuous.setStatus("current")


class _TmnxOamSaaCtlKeepProbeHistoryAdm_Type(Integer32):
    """Custom type tmnxOamSaaCtlKeepProbeHistoryAdm based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("keep", 1),
          ("drop", 2),
          ("auto", 3))
    )


_TmnxOamSaaCtlKeepProbeHistoryAdm_Type.__name__ = "Integer32"
_TmnxOamSaaCtlKeepProbeHistoryAdm_Object = MibTableColumn
tmnxOamSaaCtlKeepProbeHistoryAdm = _TmnxOamSaaCtlKeepProbeHistoryAdm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 3, 2, 1, 15),
    _TmnxOamSaaCtlKeepProbeHistoryAdm_Type()
)
tmnxOamSaaCtlKeepProbeHistoryAdm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamSaaCtlKeepProbeHistoryAdm.setStatus("current")


class _TmnxOamSaaCtlKeepProbeHistoryOpr_Type(Integer32):
    """Custom type tmnxOamSaaCtlKeepProbeHistoryOpr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("keep", 1),
          ("drop", 2))
    )


_TmnxOamSaaCtlKeepProbeHistoryOpr_Type.__name__ = "Integer32"
_TmnxOamSaaCtlKeepProbeHistoryOpr_Object = MibTableColumn
tmnxOamSaaCtlKeepProbeHistoryOpr = _TmnxOamSaaCtlKeepProbeHistoryOpr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 3, 2, 1, 16),
    _TmnxOamSaaCtlKeepProbeHistoryOpr_Type()
)
tmnxOamSaaCtlKeepProbeHistoryOpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamSaaCtlKeepProbeHistoryOpr.setStatus("current")
_TmnxOamSaaThresholdTable_Object = MibTable
tmnxOamSaaThresholdTable = _TmnxOamSaaThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 3, 3)
)
if mibBuilder.loadTexts:
    tmnxOamSaaThresholdTable.setStatus("current")
_TmnxOamSaaThresholdEntry_Object = MibTableRow
tmnxOamSaaThresholdEntry = _TmnxOamSaaThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 3, 3, 1)
)
tmnxOamSaaThresholdEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamSaaCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamSaaCtlTestIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamSaaTType"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamSaaTDirection"),
)
if mibBuilder.loadTexts:
    tmnxOamSaaThresholdEntry.setStatus("current")
_TmnxOamSaaTType_Type = TmnxOamSaaThreshold
_TmnxOamSaaTType_Object = MibTableColumn
tmnxOamSaaTType = _TmnxOamSaaTType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 3, 3, 1, 1),
    _TmnxOamSaaTType_Type()
)
tmnxOamSaaTType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamSaaTType.setStatus("current")


class _TmnxOamSaaTDirection_Type(Integer32):
    """Custom type tmnxOamSaaTDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rising", 1),
          ("falling", 2))
    )


_TmnxOamSaaTDirection_Type.__name__ = "Integer32"
_TmnxOamSaaTDirection_Object = MibTableColumn
tmnxOamSaaTDirection = _TmnxOamSaaTDirection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 3, 3, 1, 2),
    _TmnxOamSaaTDirection_Type()
)
tmnxOamSaaTDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamSaaTDirection.setStatus("current")
_TmnxOamSaaTRowStatus_Type = RowStatus
_TmnxOamSaaTRowStatus_Object = MibTableColumn
tmnxOamSaaTRowStatus = _TmnxOamSaaTRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 3, 3, 1, 3),
    _TmnxOamSaaTRowStatus_Type()
)
tmnxOamSaaTRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamSaaTRowStatus.setStatus("current")
_TmnxOamSaaTLastChanged_Type = TimeStamp
_TmnxOamSaaTLastChanged_Object = MibTableColumn
tmnxOamSaaTLastChanged = _TmnxOamSaaTLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 3, 3, 1, 4),
    _TmnxOamSaaTLastChanged_Type()
)
tmnxOamSaaTLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamSaaTLastChanged.setStatus("current")


class _TmnxOamSaaTThreshold_Type(Unsigned32):
    """Custom type tmnxOamSaaTThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TmnxOamSaaTThreshold_Type.__name__ = "Unsigned32"
_TmnxOamSaaTThreshold_Object = MibTableColumn
tmnxOamSaaTThreshold = _TmnxOamSaaTThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 3, 3, 1, 5),
    _TmnxOamSaaTThreshold_Type()
)
tmnxOamSaaTThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamSaaTThreshold.setStatus("current")
_TmnxOamSaaTValue_Type = Integer32
_TmnxOamSaaTValue_Object = MibTableColumn
tmnxOamSaaTValue = _TmnxOamSaaTValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 3, 3, 1, 6),
    _TmnxOamSaaTValue_Type()
)
tmnxOamSaaTValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamSaaTValue.setStatus("current")
_TmnxOamSaaTLastSent_Type = TimeStamp
_TmnxOamSaaTLastSent_Object = MibTableColumn
tmnxOamSaaTLastSent = _TmnxOamSaaTLastSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 3, 3, 1, 7),
    _TmnxOamSaaTLastSent_Type()
)
tmnxOamSaaTLastSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamSaaTLastSent.setStatus("current")
_TmnxOamSaaTTestMode_Type = TmnxOamTestMode
_TmnxOamSaaTTestMode_Object = MibTableColumn
tmnxOamSaaTTestMode = _TmnxOamSaaTTestMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 3, 3, 1, 8),
    _TmnxOamSaaTTestMode_Type()
)
tmnxOamSaaTTestMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamSaaTTestMode.setStatus("current")
_TmnxOamSaaTTestRunIndex_Type = Unsigned32
_TmnxOamSaaTTestRunIndex_Object = MibTableColumn
tmnxOamSaaTTestRunIndex = _TmnxOamSaaTTestRunIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 3, 3, 1, 9),
    _TmnxOamSaaTTestRunIndex_Type()
)
tmnxOamSaaTTestRunIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamSaaTTestRunIndex.setStatus("current")
_TmnxOamMobGatewayObjs_ObjectIdentity = ObjectIdentity
tmnxOamMobGatewayObjs = _TmnxOamMobGatewayObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 4)
)
_TmnxOamMobGtpPingCtlTable_Object = MibTable
tmnxOamMobGtpPingCtlTable = _TmnxOamMobGtpPingCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 4, 1)
)
if mibBuilder.loadTexts:
    tmnxOamMobGtpPingCtlTable.setStatus("current")
_TmnxOamMobGtpPingCtlEntry_Object = MibTableRow
tmnxOamMobGtpPingCtlEntry = _TmnxOamMobGtpPingCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 4, 1, 1)
)
tmnxOamMobGtpPingCtlEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamMobGtpPingCtlEntry.setStatus("current")


class _TmnxOamMobGtpPingRefPointType_Type(Integer32):
    """Custom type tmnxOamMobGtpPingRefPointType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5,
              9,
              10,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("s11", 1),
          ("s1u", 3),
          ("gnc", 5),
          ("s2bc", 9),
          ("s2bu", 10),
          ("s2ac", 14),
          ("s2au", 15),
          ("gnu", 16))
    )


_TmnxOamMobGtpPingRefPointType_Type.__name__ = "Integer32"
_TmnxOamMobGtpPingRefPointType_Object = MibTableColumn
tmnxOamMobGtpPingRefPointType = _TmnxOamMobGtpPingRefPointType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 4, 1, 1, 1),
    _TmnxOamMobGtpPingRefPointType_Type()
)
tmnxOamMobGtpPingRefPointType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMobGtpPingRefPointType.setStatus("current")
_TmnxOamMobGtpPingVRtrId_Type = TmnxVRtrID
_TmnxOamMobGtpPingVRtrId_Object = MibTableColumn
tmnxOamMobGtpPingVRtrId = _TmnxOamMobGtpPingVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 4, 1, 1, 2),
    _TmnxOamMobGtpPingVRtrId_Type()
)
tmnxOamMobGtpPingVRtrId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMobGtpPingVRtrId.setStatus("obsolete")
_TmnxOamMobGtpPingPort_Type = InetPortNumber
_TmnxOamMobGtpPingPort_Object = MibTableColumn
tmnxOamMobGtpPingPort = _TmnxOamMobGtpPingPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 4, 1, 1, 3),
    _TmnxOamMobGtpPingPort_Type()
)
tmnxOamMobGtpPingPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMobGtpPingPort.setStatus("current")
_TmnxOamMobGtpPingGateway_Type = TmnxMobGwId
_TmnxOamMobGtpPingGateway_Object = MibTableColumn
tmnxOamMobGtpPingGateway = _TmnxOamMobGtpPingGateway_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 4, 1, 1, 4),
    _TmnxOamMobGtpPingGateway_Type()
)
tmnxOamMobGtpPingGateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMobGtpPingGateway.setStatus("current")
_TmnxOamDnsPingCtlTable_ObjectIdentity = ObjectIdentity
tmnxOamDnsPingCtlTable = _TmnxOamDnsPingCtlTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 4, 3)
)
_TmnxOamGeneralObjs_ObjectIdentity = ObjectIdentity
tmnxOamGeneralObjs = _TmnxOamGeneralObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 5)
)


class _TmnxOamMplsPduTimeStampFormat_Type(Integer32):
    """Custom type tmnxOamMplsPduTimeStampFormat based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("rfc4379", 0),
          ("unix", 1))
    )


_TmnxOamMplsPduTimeStampFormat_Type.__name__ = "Integer32"
_TmnxOamMplsPduTimeStampFormat_Object = MibScalar
tmnxOamMplsPduTimeStampFormat = _TmnxOamMplsPduTimeStampFormat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 5, 1),
    _TmnxOamMplsPduTimeStampFormat_Type()
)
tmnxOamMplsPduTimeStampFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamMplsPduTimeStampFormat.setStatus("current")
_TmnxOamGeneralStats_ObjectIdentity = ObjectIdentity
tmnxOamGeneralStats = _TmnxOamGeneralStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 5, 2)
)
_TmnxOamSysPerfOprLimitTx_Type = Gauge32
_TmnxOamSysPerfOprLimitTx_Object = MibScalar
tmnxOamSysPerfOprLimitTx = _TmnxOamSysPerfOprLimitTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 5, 2, 1),
    _TmnxOamSysPerfOprLimitTx_Type()
)
tmnxOamSysPerfOprLimitTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamSysPerfOprLimitTx.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxOamSysPerfOprLimitTx.setUnits("echo request packets per second")
_TmnxOamSysPerfCfgLimitTx_Type = Gauge32
_TmnxOamSysPerfCfgLimitTx_Object = MibScalar
tmnxOamSysPerfCfgLimitTx = _TmnxOamSysPerfCfgLimitTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 5, 2, 2),
    _TmnxOamSysPerfCfgLimitTx_Type()
)
tmnxOamSysPerfCfgLimitTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamSysPerfCfgLimitTx.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxOamSysPerfCfgLimitTx.setUnits("echo request packets per second")
_TmnxOamSysPerfCfgTotalTx_Type = Gauge32
_TmnxOamSysPerfCfgTotalTx_Object = MibScalar
tmnxOamSysPerfCfgTotalTx = _TmnxOamSysPerfCfgTotalTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 5, 2, 3),
    _TmnxOamSysPerfCfgTotalTx_Type()
)
tmnxOamSysPerfCfgTotalTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamSysPerfCfgTotalTx.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxOamSysPerfCfgTotalTx.setUnits("echo request packets per second")
_TmnxOamSysPerfLastClearedTime_Type = TimeStamp
_TmnxOamSysPerfLastClearedTime_Object = MibScalar
tmnxOamSysPerfLastClearedTime = _TmnxOamSysPerfLastClearedTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 5, 2, 4),
    _TmnxOamSysPerfLastClearedTime_Type()
)
tmnxOamSysPerfLastClearedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamSysPerfLastClearedTime.setStatus("current")
_TmnxOamSysPerfLocalTestTx_Type = Counter32
_TmnxOamSysPerfLocalTestTx_Object = MibScalar
tmnxOamSysPerfLocalTestTx = _TmnxOamSysPerfLocalTestTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 5, 2, 5),
    _TmnxOamSysPerfLocalTestTx_Type()
)
tmnxOamSysPerfLocalTestTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamSysPerfLocalTestTx.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamSysPerfLocalTestTx.setUnits("echo request packets")
_TmnxOamSysPerfRemoteTestRx_Type = Counter32
_TmnxOamSysPerfRemoteTestRx_Object = MibScalar
tmnxOamSysPerfRemoteTestRx = _TmnxOamSysPerfRemoteTestRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 5, 2, 6),
    _TmnxOamSysPerfRemoteTestRx_Type()
)
tmnxOamSysPerfRemoteTestRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamSysPerfRemoteTestRx.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamSysPerfRemoteTestRx.setUnits("echo request packets")
_TmnxOamSysPerfReqTypeTable_Object = MibTable
tmnxOamSysPerfReqTypeTable = _TmnxOamSysPerfReqTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 5, 2, 7)
)
if mibBuilder.loadTexts:
    tmnxOamSysPerfReqTypeTable.setStatus("current")
_TmnxOamSysPerfReqTypeEntry_Object = MibTableRow
tmnxOamSysPerfReqTypeEntry = _TmnxOamSysPerfReqTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 5, 2, 7, 1)
)
tmnxOamSysPerfReqTypeEntry.setIndexNames(
    (1, "TIMETRA-OAM-TEST-MIB", "tmnxOamSysPerfReqTypeName"),
)
if mibBuilder.loadTexts:
    tmnxOamSysPerfReqTypeEntry.setStatus("current")
_TmnxOamSysPerfReqTypeName_Type = TNamedItem
_TmnxOamSysPerfReqTypeName_Object = MibTableColumn
tmnxOamSysPerfReqTypeName = _TmnxOamSysPerfReqTypeName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 5, 2, 7, 1, 1),
    _TmnxOamSysPerfReqTypeName_Type()
)
tmnxOamSysPerfReqTypeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamSysPerfReqTypeName.setStatus("current")
_TmnxOamSysPerfReqTypeLocalTestTx_Type = Counter32
_TmnxOamSysPerfReqTypeLocalTestTx_Object = MibTableColumn
tmnxOamSysPerfReqTypeLocalTestTx = _TmnxOamSysPerfReqTypeLocalTestTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 5, 2, 7, 1, 2),
    _TmnxOamSysPerfReqTypeLocalTestTx_Type()
)
tmnxOamSysPerfReqTypeLocalTestTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamSysPerfReqTypeLocalTestTx.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamSysPerfReqTypeLocalTestTx.setUnits("echo request packets")
_TmnxOamSysPerfReqTypeRemoteTstRx_Type = Counter32
_TmnxOamSysPerfReqTypeRemoteTstRx_Object = MibTableColumn
tmnxOamSysPerfReqTypeRemoteTstRx = _TmnxOamSysPerfReqTypeRemoteTstRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 5, 2, 7, 1, 3),
    _TmnxOamSysPerfReqTypeRemoteTstRx_Type()
)
tmnxOamSysPerfReqTypeRemoteTstRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamSysPerfReqTypeRemoteTstRx.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamSysPerfReqTypeRemoteTstRx.setUnits("echo request packets")
_TmnxOamSysSessionLimit_Type = Gauge32
_TmnxOamSysSessionLimit_Object = MibScalar
tmnxOamSysSessionLimit = _TmnxOamSysSessionLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 5, 2, 8),
    _TmnxOamSysSessionLimit_Type()
)
tmnxOamSysSessionLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamSysSessionLimit.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxOamSysSessionLimit.setUnits("sessions")
_TmnxOamSysSessionCount_Type = Gauge32
_TmnxOamSysSessionCount_Object = MibScalar
tmnxOamSysSessionCount = _TmnxOamSysSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 5, 2, 9),
    _TmnxOamSysSessionCount_Type()
)
tmnxOamSysSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamSysSessionCount.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxOamSysSessionCount.setUnits("sessions")
_TmnxOamSysBgIcmpBrgSessionLimit_Type = Gauge32
_TmnxOamSysBgIcmpBrgSessionLimit_Object = MibScalar
tmnxOamSysBgIcmpBrgSessionLimit = _TmnxOamSysBgIcmpBrgSessionLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 5, 2, 10),
    _TmnxOamSysBgIcmpBrgSessionLimit_Type()
)
tmnxOamSysBgIcmpBrgSessionLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamSysBgIcmpBrgSessionLimit.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamSysBgIcmpBrgSessionLimit.setUnits("sessions")
_TmnxOamSysBgIcmpBrgSessionCount_Type = Gauge32
_TmnxOamSysBgIcmpBrgSessionCount_Object = MibScalar
tmnxOamSysBgIcmpBrgSessionCount = _TmnxOamSysBgIcmpBrgSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 5, 2, 11),
    _TmnxOamSysBgIcmpBrgSessionCount_Type()
)
tmnxOamSysBgIcmpBrgSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamSysBgIcmpBrgSessionCount.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamSysBgIcmpBrgSessionCount.setUnits("sessions")
_TmnxOamSysLspSelfPingSessLimit_Type = Gauge32
_TmnxOamSysLspSelfPingSessLimit_Object = MibScalar
tmnxOamSysLspSelfPingSessLimit = _TmnxOamSysLspSelfPingSessLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 5, 2, 12),
    _TmnxOamSysLspSelfPingSessLimit_Type()
)
tmnxOamSysLspSelfPingSessLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamSysLspSelfPingSessLimit.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamSysLspSelfPingSessLimit.setUnits("sessions")
_TmnxOamSysLspSelfPingSessCount_Type = Gauge32
_TmnxOamSysLspSelfPingSessCount_Object = MibScalar
tmnxOamSysLspSelfPingSessCount = _TmnxOamSysLspSelfPingSessCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 5, 2, 13),
    _TmnxOamSysLspSelfPingSessCount_Type()
)
tmnxOamSysLspSelfPingSessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamSysLspSelfPingSessCount.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamSysLspSelfPingSessCount.setUnits("sessions")
_TmnxOamSysPerfCfgLspSelfTxLimit_Type = Gauge32
_TmnxOamSysPerfCfgLspSelfTxLimit_Object = MibScalar
tmnxOamSysPerfCfgLspSelfTxLimit = _TmnxOamSysPerfCfgLspSelfTxLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 5, 2, 14),
    _TmnxOamSysPerfCfgLspSelfTxLimit_Type()
)
tmnxOamSysPerfCfgLspSelfTxLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamSysPerfCfgLspSelfTxLimit.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamSysPerfCfgLspSelfTxLimit.setUnits("echo request packets per second")
_TmnxOamSysPerfCfgLspSelfTxTotal_Type = Gauge32
_TmnxOamSysPerfCfgLspSelfTxTotal_Object = MibScalar
tmnxOamSysPerfCfgLspSelfTxTotal = _TmnxOamSysPerfCfgLspSelfTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 5, 2, 15),
    _TmnxOamSysPerfCfgLspSelfTxTotal_Type()
)
tmnxOamSysPerfCfgLspSelfTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamSysPerfCfgLspSelfTxTotal.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamSysPerfCfgLspSelfTxTotal.setUnits("echo request packets per second")
_TmnxOamSysBgIcmpIfCtlSessLimit_Type = Gauge32
_TmnxOamSysBgIcmpIfCtlSessLimit_Object = MibScalar
tmnxOamSysBgIcmpIfCtlSessLimit = _TmnxOamSysBgIcmpIfCtlSessLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 5, 2, 16),
    _TmnxOamSysBgIcmpIfCtlSessLimit_Type()
)
tmnxOamSysBgIcmpIfCtlSessLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamSysBgIcmpIfCtlSessLimit.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamSysBgIcmpIfCtlSessLimit.setUnits("sessions")
_TmnxOamSysBgIcmpIfCtlSessCount_Type = Gauge32
_TmnxOamSysBgIcmpIfCtlSessCount_Object = MibScalar
tmnxOamSysBgIcmpIfCtlSessCount = _TmnxOamSysBgIcmpIfCtlSessCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 5, 2, 17),
    _TmnxOamSysBgIcmpIfCtlSessCount_Type()
)
tmnxOamSysBgIcmpIfCtlSessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamSysBgIcmpIfCtlSessCount.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamSysBgIcmpIfCtlSessCount.setUnits("sessions")
_TmnxOamSysTestLimit_Type = Gauge32
_TmnxOamSysTestLimit_Object = MibScalar
tmnxOamSysTestLimit = _TmnxOamSysTestLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 5, 2, 18),
    _TmnxOamSysTestLimit_Type()
)
tmnxOamSysTestLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamSysTestLimit.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamSysTestLimit.setUnits("tests")
_TmnxOamSysTestCount_Type = Gauge32
_TmnxOamSysTestCount_Object = MibScalar
tmnxOamSysTestCount = _TmnxOamSysTestCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 5, 2, 19),
    _TmnxOamSysTestCount_Type()
)
tmnxOamSysTestCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamSysTestCount.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamSysTestCount.setUnits("tests")
_TmnxOamSysTxLimit_Type = Gauge32
_TmnxOamSysTxLimit_Object = MibScalar
tmnxOamSysTxLimit = _TmnxOamSysTxLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 5, 2, 20),
    _TmnxOamSysTxLimit_Type()
)
tmnxOamSysTxLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamSysTxLimit.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamSysTxLimit.setUnits("echo request packets per second")
_TmnxOamSysTxTotal_Type = Gauge32
_TmnxOamSysTxTotal_Object = MibScalar
tmnxOamSysTxTotal = _TmnxOamSysTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 5, 2, 21),
    _TmnxOamSysTxTotal_Type()
)
tmnxOamSysTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamSysTxTotal.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamSysTxTotal.setUnits("echo request packets per second")
_TmnxOamSysShareTestLimit_Type = Gauge32
_TmnxOamSysShareTestLimit_Object = MibScalar
tmnxOamSysShareTestLimit = _TmnxOamSysShareTestLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 5, 2, 22),
    _TmnxOamSysShareTestLimit_Type()
)
tmnxOamSysShareTestLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamSysShareTestLimit.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamSysShareTestLimit.setUnits("tests")
_TmnxOamSysShareTestCount_Type = Gauge32
_TmnxOamSysShareTestCount_Object = MibScalar
tmnxOamSysShareTestCount = _TmnxOamSysShareTestCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 5, 2, 23),
    _TmnxOamSysShareTestCount_Type()
)
tmnxOamSysShareTestCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamSysShareTestCount.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamSysShareTestCount.setUnits("tests")
_TmnxOamSysShareTxLimit_Type = Gauge32
_TmnxOamSysShareTxLimit_Object = MibScalar
tmnxOamSysShareTxLimit = _TmnxOamSysShareTxLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 5, 2, 24),
    _TmnxOamSysShareTxLimit_Type()
)
tmnxOamSysShareTxLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamSysShareTxLimit.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamSysShareTxLimit.setUnits("echo request packets per second")
_TmnxOamSysShareTxTotal_Type = Gauge32
_TmnxOamSysShareTxTotal_Object = MibScalar
tmnxOamSysShareTxTotal = _TmnxOamSysShareTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 5, 2, 25),
    _TmnxOamSysShareTxTotal_Type()
)
tmnxOamSysShareTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamSysShareTxTotal.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamSysShareTxTotal.setUnits("echo request packets per second")


class _TmnxOamMplsEchoDownstreamMapTlv_Type(TmnxOamMplsEchoDownMapTlv):
    """Custom type tmnxOamMplsEchoDownstreamMapTlv based on TmnxOamMplsEchoDownMapTlv"""
    defaultValue = 1


_TmnxOamMplsEchoDownstreamMapTlv_Type.__name__ = "TmnxOamMplsEchoDownMapTlv"
_TmnxOamMplsEchoDownstreamMapTlv_Object = MibScalar
tmnxOamMplsEchoDownstreamMapTlv = _TmnxOamMplsEchoDownstreamMapTlv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 5, 3),
    _TmnxOamMplsEchoDownstreamMapTlv_Type()
)
tmnxOamMplsEchoDownstreamMapTlv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamMplsEchoDownstreamMapTlv.setStatus("current")
_TmnxOamDiagObjs_ObjectIdentity = ObjectIdentity
tmnxOamDiagObjs = _TmnxOamDiagObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6)
)
_TmnxOamDiagCtlTable_Object = MibTable
tmnxOamDiagCtlTable = _TmnxOamDiagCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 1)
)
if mibBuilder.loadTexts:
    tmnxOamDiagCtlTable.setStatus("current")
_TmnxOamDiagCtlEntry_Object = MibTableRow
tmnxOamDiagCtlEntry = _TmnxOamDiagCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 1, 1)
)
tmnxOamDiagCtlEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamDiagCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamDiagCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamDiagCtlEntry.setStatus("current")


class _TmnxOamDiagCtlOwnerIndex_Type(SnmpAdminString):
    """Custom type tmnxOamDiagCtlOwnerIndex based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TmnxOamDiagCtlOwnerIndex_Type.__name__ = "SnmpAdminString"
_TmnxOamDiagCtlOwnerIndex_Object = MibTableColumn
tmnxOamDiagCtlOwnerIndex = _TmnxOamDiagCtlOwnerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 1, 1, 1),
    _TmnxOamDiagCtlOwnerIndex_Type()
)
tmnxOamDiagCtlOwnerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamDiagCtlOwnerIndex.setStatus("current")


class _TmnxOamDiagCtlTestIndex_Type(SnmpAdminString):
    """Custom type tmnxOamDiagCtlTestIndex based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TmnxOamDiagCtlTestIndex_Type.__name__ = "SnmpAdminString"
_TmnxOamDiagCtlTestIndex_Object = MibTableColumn
tmnxOamDiagCtlTestIndex = _TmnxOamDiagCtlTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 1, 1, 2),
    _TmnxOamDiagCtlTestIndex_Type()
)
tmnxOamDiagCtlTestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamDiagCtlTestIndex.setStatus("current")
_TmnxOamDiagCtlRowStatus_Type = RowStatus
_TmnxOamDiagCtlRowStatus_Object = MibTableColumn
tmnxOamDiagCtlRowStatus = _TmnxOamDiagCtlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 1, 1, 3),
    _TmnxOamDiagCtlRowStatus_Type()
)
tmnxOamDiagCtlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamDiagCtlRowStatus.setStatus("current")
_TmnxOamDiagCtlLastChanged_Type = TimeStamp
_TmnxOamDiagCtlLastChanged_Object = MibTableColumn
tmnxOamDiagCtlLastChanged = _TmnxOamDiagCtlLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 1, 1, 4),
    _TmnxOamDiagCtlLastChanged_Type()
)
tmnxOamDiagCtlLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamDiagCtlLastChanged.setStatus("current")


class _TmnxOamDiagCtlTestMode_Type(Integer32):
    """Custom type tmnxOamDiagCtlTestMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("findEgressDiag", 1))
    )


_TmnxOamDiagCtlTestMode_Type.__name__ = "Integer32"
_TmnxOamDiagCtlTestMode_Object = MibTableColumn
tmnxOamDiagCtlTestMode = _TmnxOamDiagCtlTestMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 1, 1, 5),
    _TmnxOamDiagCtlTestMode_Type()
)
tmnxOamDiagCtlTestMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamDiagCtlTestMode.setStatus("current")


class _TmnxOamDiagCtlAdminState_Type(TmnxEnabledDisabled):
    """Custom type tmnxOamDiagCtlAdminState based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxOamDiagCtlAdminState_Type.__name__ = "TmnxEnabledDisabled"
_TmnxOamDiagCtlAdminState_Object = MibTableColumn
tmnxOamDiagCtlAdminState = _TmnxOamDiagCtlAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 1, 1, 6),
    _TmnxOamDiagCtlAdminState_Type()
)
tmnxOamDiagCtlAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamDiagCtlAdminState.setStatus("current")
_TmnxOamFindEgrDiagCtlTable_Object = MibTable
tmnxOamFindEgrDiagCtlTable = _TmnxOamFindEgrDiagCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 2)
)
if mibBuilder.loadTexts:
    tmnxOamFindEgrDiagCtlTable.setStatus("current")
_TmnxOamFindEgrDiagCtlEntry_Object = MibTableRow
tmnxOamFindEgrDiagCtlEntry = _TmnxOamFindEgrDiagCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 2, 1)
)
tmnxOamFindEgrDiagCtlEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamDiagCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamDiagCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamFindEgrDiagCtlEntry.setStatus("current")
_TmnxOamFindEgrDiagCtlLastChanged_Type = TimeStamp
_TmnxOamFindEgrDiagCtlLastChanged_Object = MibTableColumn
tmnxOamFindEgrDiagCtlLastChanged = _TmnxOamFindEgrDiagCtlLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 2, 1, 1),
    _TmnxOamFindEgrDiagCtlLastChanged_Type()
)
tmnxOamFindEgrDiagCtlLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamFindEgrDiagCtlLastChanged.setStatus("current")


class _TmnxOamFindEgrDiagCtlPacketNum_Type(Unsigned32):
    """Custom type tmnxOamFindEgrDiagCtlPacketNum based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TmnxOamFindEgrDiagCtlPacketNum_Type.__name__ = "Unsigned32"
_TmnxOamFindEgrDiagCtlPacketNum_Object = MibTableColumn
tmnxOamFindEgrDiagCtlPacketNum = _TmnxOamFindEgrDiagCtlPacketNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 2, 1, 2),
    _TmnxOamFindEgrDiagCtlPacketNum_Type()
)
tmnxOamFindEgrDiagCtlPacketNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamFindEgrDiagCtlPacketNum.setStatus("current")


class _TmnxOamFindEgrDiagCtlIngPortId_Type(TmnxPortID):
    """Custom type tmnxOamFindEgrDiagCtlIngPortId based on TmnxPortID"""
    defaultValue = 503316480


_TmnxOamFindEgrDiagCtlIngPortId_Type.__name__ = "TmnxPortID"
_TmnxOamFindEgrDiagCtlIngPortId_Object = MibTableColumn
tmnxOamFindEgrDiagCtlIngPortId = _TmnxOamFindEgrDiagCtlIngPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 2, 1, 3),
    _TmnxOamFindEgrDiagCtlIngPortId_Type()
)
tmnxOamFindEgrDiagCtlIngPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamFindEgrDiagCtlIngPortId.setStatus("current")
_TmnxOamFindEgrDiagResultsTable_Object = MibTable
tmnxOamFindEgrDiagResultsTable = _TmnxOamFindEgrDiagResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 3)
)
if mibBuilder.loadTexts:
    tmnxOamFindEgrDiagResultsTable.setStatus("current")
_TmnxOamFindEgrDiagResultsEntry_Object = MibTableRow
tmnxOamFindEgrDiagResultsEntry = _TmnxOamFindEgrDiagResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 3, 1)
)
tmnxOamFindEgrDiagResultsEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamDiagCtlOwnerIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamDiagCtlTestIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamDiagResultsTestRunIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamFindEgrDiagResultsEntry.setStatus("current")


class _TmnxOamDiagResultsTestRunIndex_Type(Unsigned32):
    """Custom type tmnxOamDiagResultsTestRunIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxOamDiagResultsTestRunIndex_Type.__name__ = "Unsigned32"
_TmnxOamDiagResultsTestRunIndex_Object = MibTableColumn
tmnxOamDiagResultsTestRunIndex = _TmnxOamDiagResultsTestRunIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 3, 1, 1),
    _TmnxOamDiagResultsTestRunIndex_Type()
)
tmnxOamDiagResultsTestRunIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamDiagResultsTestRunIndex.setStatus("current")
_TmnxOamFindEgrDiagOperState_Type = TmnxEnabledDisabled
_TmnxOamFindEgrDiagOperState_Object = MibTableColumn
tmnxOamFindEgrDiagOperState = _TmnxOamFindEgrDiagOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 3, 1, 2),
    _TmnxOamFindEgrDiagOperState_Type()
)
tmnxOamFindEgrDiagOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamFindEgrDiagOperState.setStatus("current")
_TmnxOamFindEgrDiagEgressPort_Type = TmnxPortID
_TmnxOamFindEgrDiagEgressPort_Object = MibTableColumn
tmnxOamFindEgrDiagEgressPort = _TmnxOamFindEgrDiagEgressPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 3, 1, 3),
    _TmnxOamFindEgrDiagEgressPort_Type()
)
tmnxOamFindEgrDiagEgressPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamFindEgrDiagEgressPort.setStatus("current")
_TmnxOamFindEgrDiagEgrRtrInstName_Type = TLNamedItemOrEmpty
_TmnxOamFindEgrDiagEgrRtrInstName_Object = MibTableColumn
tmnxOamFindEgrDiagEgrRtrInstName = _TmnxOamFindEgrDiagEgrRtrInstName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 3, 1, 4),
    _TmnxOamFindEgrDiagEgrRtrInstName_Type()
)
tmnxOamFindEgrDiagEgrRtrInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamFindEgrDiagEgrRtrInstName.setStatus("current")
_TmnxOamFindEgrDiagEgressIfName_Type = TNamedItemOrEmpty
_TmnxOamFindEgrDiagEgressIfName_Object = MibTableColumn
tmnxOamFindEgrDiagEgressIfName = _TmnxOamFindEgrDiagEgressIfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 3, 1, 5),
    _TmnxOamFindEgrDiagEgressIfName_Type()
)
tmnxOamFindEgrDiagEgressIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamFindEgrDiagEgressIfName.setStatus("current")
_TmnxOamFindEgrDiagNextHopAddrTyp_Type = InetAddressType
_TmnxOamFindEgrDiagNextHopAddrTyp_Object = MibTableColumn
tmnxOamFindEgrDiagNextHopAddrTyp = _TmnxOamFindEgrDiagNextHopAddrTyp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 3, 1, 6),
    _TmnxOamFindEgrDiagNextHopAddrTyp_Type()
)
tmnxOamFindEgrDiagNextHopAddrTyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamFindEgrDiagNextHopAddrTyp.setStatus("current")


class _TmnxOamFindEgrDiagNextHopAddress_Type(InetAddress):
    """Custom type tmnxOamFindEgrDiagNextHopAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamFindEgrDiagNextHopAddress_Type.__name__ = "InetAddress"
_TmnxOamFindEgrDiagNextHopAddress_Object = MibTableColumn
tmnxOamFindEgrDiagNextHopAddress = _TmnxOamFindEgrDiagNextHopAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 3, 1, 7),
    _TmnxOamFindEgrDiagNextHopAddress_Type()
)
tmnxOamFindEgrDiagNextHopAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamFindEgrDiagNextHopAddress.setStatus("current")
_TmnxOamBuildPktCtlTable_Object = MibTable
tmnxOamBuildPktCtlTable = _TmnxOamBuildPktCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 4)
)
if mibBuilder.loadTexts:
    tmnxOamBuildPktCtlTable.setStatus("current")
_TmnxOamBuildPktCtlEntry_Object = MibTableRow
tmnxOamBuildPktCtlEntry = _TmnxOamBuildPktCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 4, 1)
)
tmnxOamBuildPktCtlEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktNum"),
)
if mibBuilder.loadTexts:
    tmnxOamBuildPktCtlEntry.setStatus("current")


class _TmnxOamBuildPktNum_Type(Unsigned32):
    """Custom type tmnxOamBuildPktNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmnxOamBuildPktNum_Type.__name__ = "Unsigned32"
_TmnxOamBuildPktNum_Object = MibTableColumn
tmnxOamBuildPktNum = _TmnxOamBuildPktNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 4, 1, 1),
    _TmnxOamBuildPktNum_Type()
)
tmnxOamBuildPktNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamBuildPktNum.setStatus("current")
_TmnxOamBuildPktRowStatus_Type = RowStatus
_TmnxOamBuildPktRowStatus_Object = MibTableColumn
tmnxOamBuildPktRowStatus = _TmnxOamBuildPktRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 4, 1, 2),
    _TmnxOamBuildPktRowStatus_Type()
)
tmnxOamBuildPktRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamBuildPktRowStatus.setStatus("current")
_TmnxOamBuildPktLastChanged_Type = TimeStamp
_TmnxOamBuildPktLastChanged_Object = MibTableColumn
tmnxOamBuildPktLastChanged = _TmnxOamBuildPktLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 4, 1, 3),
    _TmnxOamBuildPktLastChanged_Type()
)
tmnxOamBuildPktLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamBuildPktLastChanged.setStatus("current")


class _TmnxOamBuildPktHeaderSeq_Type(DisplayString):
    """Custom type tmnxOamBuildPktHeaderSeq based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 153),
    )


_TmnxOamBuildPktHeaderSeq_Type.__name__ = "DisplayString"
_TmnxOamBuildPktHeaderSeq_Object = MibTableColumn
tmnxOamBuildPktHeaderSeq = _TmnxOamBuildPktHeaderSeq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 4, 1, 4),
    _TmnxOamBuildPktHeaderSeq_Type()
)
tmnxOamBuildPktHeaderSeq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamBuildPktHeaderSeq.setStatus("current")
_TmnxOamBuildPktHdrCtlTable_Object = MibTable
tmnxOamBuildPktHdrCtlTable = _TmnxOamBuildPktHdrCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 5)
)
if mibBuilder.loadTexts:
    tmnxOamBuildPktHdrCtlTable.setStatus("current")
_TmnxOamBuildPktHdrCtlEntry_Object = MibTableRow
tmnxOamBuildPktHdrCtlEntry = _TmnxOamBuildPktHdrCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 5, 1)
)
tmnxOamBuildPktHdrCtlEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktHeaderNum"),
)
if mibBuilder.loadTexts:
    tmnxOamBuildPktHdrCtlEntry.setStatus("current")


class _TmnxOamBuildPktHeaderNum_Type(Unsigned32):
    """Custom type tmnxOamBuildPktHeaderNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmnxOamBuildPktHeaderNum_Type.__name__ = "Unsigned32"
_TmnxOamBuildPktHeaderNum_Object = MibTableColumn
tmnxOamBuildPktHeaderNum = _TmnxOamBuildPktHeaderNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 5, 1, 1),
    _TmnxOamBuildPktHeaderNum_Type()
)
tmnxOamBuildPktHeaderNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamBuildPktHeaderNum.setStatus("current")
_TmnxOamBuildPktHdrRowStatus_Type = RowStatus
_TmnxOamBuildPktHdrRowStatus_Object = MibTableColumn
tmnxOamBuildPktHdrRowStatus = _TmnxOamBuildPktHdrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 5, 1, 2),
    _TmnxOamBuildPktHdrRowStatus_Type()
)
tmnxOamBuildPktHdrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamBuildPktHdrRowStatus.setStatus("current")
_TmnxOamBuildPktHdrLastChanged_Type = TimeStamp
_TmnxOamBuildPktHdrLastChanged_Object = MibTableColumn
tmnxOamBuildPktHdrLastChanged = _TmnxOamBuildPktHdrLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 5, 1, 3),
    _TmnxOamBuildPktHdrLastChanged_Type()
)
tmnxOamBuildPktHdrLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamBuildPktHdrLastChanged.setStatus("current")


class _TmnxOamBuildPktHdrType_Type(TmnxOamBuildPktHeaderType):
    """Custom type tmnxOamBuildPktHdrType based on TmnxOamBuildPktHeaderType"""
    defaultValue = 0


_TmnxOamBuildPktHdrType_Type.__name__ = "TmnxOamBuildPktHeaderType"
_TmnxOamBuildPktHdrType_Object = MibTableColumn
tmnxOamBuildPktHdrType = _TmnxOamBuildPktHdrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 5, 1, 4),
    _TmnxOamBuildPktHdrType_Type()
)
tmnxOamBuildPktHdrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamBuildPktHdrType.setStatus("current")
_TmnxOamBuildPktHdrOvrCtlTable_Object = MibTable
tmnxOamBuildPktHdrOvrCtlTable = _TmnxOamBuildPktHdrOvrCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 6)
)
if mibBuilder.loadTexts:
    tmnxOamBuildPktHdrOvrCtlTable.setStatus("current")
_TmnxOamBuildPktHdrOvrCtlEntry_Object = MibTableRow
tmnxOamBuildPktHdrOvrCtlEntry = _TmnxOamBuildPktHdrOvrCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 6, 1)
)
tmnxOamBuildPktHdrOvrCtlEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktNum"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktHeaderNum"),
)
if mibBuilder.loadTexts:
    tmnxOamBuildPktHdrOvrCtlEntry.setStatus("current")
_TmnxOamBuildPktHdrOvrRowStatus_Type = RowStatus
_TmnxOamBuildPktHdrOvrRowStatus_Object = MibTableColumn
tmnxOamBuildPktHdrOvrRowStatus = _TmnxOamBuildPktHdrOvrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 6, 1, 1),
    _TmnxOamBuildPktHdrOvrRowStatus_Type()
)
tmnxOamBuildPktHdrOvrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamBuildPktHdrOvrRowStatus.setStatus("current")
_TmnxOamBuildPktHdrOvrLastChanged_Type = TimeStamp
_TmnxOamBuildPktHdrOvrLastChanged_Object = MibTableColumn
tmnxOamBuildPktHdrOvrLastChanged = _TmnxOamBuildPktHdrOvrLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 6, 1, 2),
    _TmnxOamBuildPktHdrOvrLastChanged_Type()
)
tmnxOamBuildPktHdrOvrLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamBuildPktHdrOvrLastChanged.setStatus("current")
_TmnxOamBuildPktEthCtlTable_Object = MibTable
tmnxOamBuildPktEthCtlTable = _TmnxOamBuildPktEthCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 7)
)
if mibBuilder.loadTexts:
    tmnxOamBuildPktEthCtlTable.setStatus("current")
_TmnxOamBuildPktEthCtlEntry_Object = MibTableRow
tmnxOamBuildPktEthCtlEntry = _TmnxOamBuildPktEthCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 7, 1)
)
tmnxOamBuildPktEthCtlEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktNumOrZero"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktHeaderNum"),
)
if mibBuilder.loadTexts:
    tmnxOamBuildPktEthCtlEntry.setStatus("current")


class _TmnxOamBuildPktNumOrZero_Type(Unsigned32):
    """Custom type tmnxOamBuildPktNumOrZero based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TmnxOamBuildPktNumOrZero_Type.__name__ = "Unsigned32"
_TmnxOamBuildPktNumOrZero_Object = MibTableColumn
tmnxOamBuildPktNumOrZero = _TmnxOamBuildPktNumOrZero_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 7, 1, 1),
    _TmnxOamBuildPktNumOrZero_Type()
)
tmnxOamBuildPktNumOrZero.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamBuildPktNumOrZero.setStatus("current")
_TmnxOamBuildPktEthLastChanged_Type = TimeStamp
_TmnxOamBuildPktEthLastChanged_Object = MibTableColumn
tmnxOamBuildPktEthLastChanged = _TmnxOamBuildPktEthLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 7, 1, 2),
    _TmnxOamBuildPktEthLastChanged_Type()
)
tmnxOamBuildPktEthLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamBuildPktEthLastChanged.setStatus("current")
_TmnxOamBuildPktEthDstMacAddr_Type = MacAddress
_TmnxOamBuildPktEthDstMacAddr_Object = MibTableColumn
tmnxOamBuildPktEthDstMacAddr = _TmnxOamBuildPktEthDstMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 7, 1, 3),
    _TmnxOamBuildPktEthDstMacAddr_Type()
)
tmnxOamBuildPktEthDstMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamBuildPktEthDstMacAddr.setStatus("current")
_TmnxOamBuildPktEthSrcMacAddr_Type = MacAddress
_TmnxOamBuildPktEthSrcMacAddr_Object = MibTableColumn
tmnxOamBuildPktEthSrcMacAddr = _TmnxOamBuildPktEthSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 7, 1, 4),
    _TmnxOamBuildPktEthSrcMacAddr_Type()
)
tmnxOamBuildPktEthSrcMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamBuildPktEthSrcMacAddr.setStatus("current")
_TmnxOamBuildPktIpCtlTable_Object = MibTable
tmnxOamBuildPktIpCtlTable = _TmnxOamBuildPktIpCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 8)
)
if mibBuilder.loadTexts:
    tmnxOamBuildPktIpCtlTable.setStatus("current")
_TmnxOamBuildPktIpCtlEntry_Object = MibTableRow
tmnxOamBuildPktIpCtlEntry = _TmnxOamBuildPktIpCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 8, 1)
)
tmnxOamBuildPktIpCtlEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktNumOrZero"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktHeaderNum"),
)
if mibBuilder.loadTexts:
    tmnxOamBuildPktIpCtlEntry.setStatus("current")
_TmnxOamBuildPktIpLastChanged_Type = TimeStamp
_TmnxOamBuildPktIpLastChanged_Object = MibTableColumn
tmnxOamBuildPktIpLastChanged = _TmnxOamBuildPktIpLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 8, 1, 1),
    _TmnxOamBuildPktIpLastChanged_Type()
)
tmnxOamBuildPktIpLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamBuildPktIpLastChanged.setStatus("current")
_TmnxOamBuildPktIpDstIpAddrType_Type = InetAddressType
_TmnxOamBuildPktIpDstIpAddrType_Object = MibTableColumn
tmnxOamBuildPktIpDstIpAddrType = _TmnxOamBuildPktIpDstIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 8, 1, 2),
    _TmnxOamBuildPktIpDstIpAddrType_Type()
)
tmnxOamBuildPktIpDstIpAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamBuildPktIpDstIpAddrType.setStatus("current")


class _TmnxOamBuildPktIpDstIpAddress_Type(InetAddress):
    """Custom type tmnxOamBuildPktIpDstIpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamBuildPktIpDstIpAddress_Type.__name__ = "InetAddress"
_TmnxOamBuildPktIpDstIpAddress_Object = MibTableColumn
tmnxOamBuildPktIpDstIpAddress = _TmnxOamBuildPktIpDstIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 8, 1, 3),
    _TmnxOamBuildPktIpDstIpAddress_Type()
)
tmnxOamBuildPktIpDstIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamBuildPktIpDstIpAddress.setStatus("current")
_TmnxOamBuildPktIpSrcIpAddrType_Type = InetAddressType
_TmnxOamBuildPktIpSrcIpAddrType_Object = MibTableColumn
tmnxOamBuildPktIpSrcIpAddrType = _TmnxOamBuildPktIpSrcIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 8, 1, 4),
    _TmnxOamBuildPktIpSrcIpAddrType_Type()
)
tmnxOamBuildPktIpSrcIpAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamBuildPktIpSrcIpAddrType.setStatus("current")


class _TmnxOamBuildPktIpSrcIpAddress_Type(InetAddress):
    """Custom type tmnxOamBuildPktIpSrcIpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamBuildPktIpSrcIpAddress_Type.__name__ = "InetAddress"
_TmnxOamBuildPktIpSrcIpAddress_Object = MibTableColumn
tmnxOamBuildPktIpSrcIpAddress = _TmnxOamBuildPktIpSrcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 8, 1, 5),
    _TmnxOamBuildPktIpSrcIpAddress_Type()
)
tmnxOamBuildPktIpSrcIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamBuildPktIpSrcIpAddress.setStatus("current")
_TmnxOamBuildPktIpDscp_Type = TDSCPNameOrEmpty
_TmnxOamBuildPktIpDscp_Object = MibTableColumn
tmnxOamBuildPktIpDscp = _TmnxOamBuildPktIpDscp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 8, 1, 6),
    _TmnxOamBuildPktIpDscp_Type()
)
tmnxOamBuildPktIpDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamBuildPktIpDscp.setStatus("current")


class _TmnxOamBuildPktIPv4MoreFragments_Type(Integer32):
    """Custom type tmnxOamBuildPktIPv4MoreFragments based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 1),
    )


_TmnxOamBuildPktIPv4MoreFragments_Type.__name__ = "Integer32"
_TmnxOamBuildPktIPv4MoreFragments_Object = MibTableColumn
tmnxOamBuildPktIPv4MoreFragments = _TmnxOamBuildPktIPv4MoreFragments_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 8, 1, 7),
    _TmnxOamBuildPktIPv4MoreFragments_Type()
)
tmnxOamBuildPktIPv4MoreFragments.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamBuildPktIPv4MoreFragments.setStatus("current")
_TmnxOamBuildPktTcpUdpCtlTable_Object = MibTable
tmnxOamBuildPktTcpUdpCtlTable = _TmnxOamBuildPktTcpUdpCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 9)
)
if mibBuilder.loadTexts:
    tmnxOamBuildPktTcpUdpCtlTable.setStatus("current")
_TmnxOamBuildPktTcpUdpCtlEntry_Object = MibTableRow
tmnxOamBuildPktTcpUdpCtlEntry = _TmnxOamBuildPktTcpUdpCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 9, 1)
)
tmnxOamBuildPktTcpUdpCtlEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktNumOrZero"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktHeaderNum"),
)
if mibBuilder.loadTexts:
    tmnxOamBuildPktTcpUdpCtlEntry.setStatus("current")
_TmnxOamBuildPktTcpUdpLastChanged_Type = TimeStamp
_TmnxOamBuildPktTcpUdpLastChanged_Object = MibTableColumn
tmnxOamBuildPktTcpUdpLastChanged = _TmnxOamBuildPktTcpUdpLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 9, 1, 1),
    _TmnxOamBuildPktTcpUdpLastChanged_Type()
)
tmnxOamBuildPktTcpUdpLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamBuildPktTcpUdpLastChanged.setStatus("current")


class _TmnxOamBuildPktTcpUdpDstPort_Type(Integer32):
    """Custom type tmnxOamBuildPktTcpUdpDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )


_TmnxOamBuildPktTcpUdpDstPort_Type.__name__ = "Integer32"
_TmnxOamBuildPktTcpUdpDstPort_Object = MibTableColumn
tmnxOamBuildPktTcpUdpDstPort = _TmnxOamBuildPktTcpUdpDstPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 9, 1, 2),
    _TmnxOamBuildPktTcpUdpDstPort_Type()
)
tmnxOamBuildPktTcpUdpDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamBuildPktTcpUdpDstPort.setStatus("current")


class _TmnxOamBuildPktTcpUdpSrcPort_Type(Integer32):
    """Custom type tmnxOamBuildPktTcpUdpSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )


_TmnxOamBuildPktTcpUdpSrcPort_Type.__name__ = "Integer32"
_TmnxOamBuildPktTcpUdpSrcPort_Object = MibTableColumn
tmnxOamBuildPktTcpUdpSrcPort = _TmnxOamBuildPktTcpUdpSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 9, 1, 3),
    _TmnxOamBuildPktTcpUdpSrcPort_Type()
)
tmnxOamBuildPktTcpUdpSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamBuildPktTcpUdpSrcPort.setStatus("current")
_TmnxOamBuildPktDot1qCtlTable_Object = MibTable
tmnxOamBuildPktDot1qCtlTable = _TmnxOamBuildPktDot1qCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 10)
)
if mibBuilder.loadTexts:
    tmnxOamBuildPktDot1qCtlTable.setStatus("current")
_TmnxOamBuildPktDot1qCtlEntry_Object = MibTableRow
tmnxOamBuildPktDot1qCtlEntry = _TmnxOamBuildPktDot1qCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 10, 1)
)
tmnxOamBuildPktDot1qCtlEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktNumOrZero"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktHeaderNum"),
)
if mibBuilder.loadTexts:
    tmnxOamBuildPktDot1qCtlEntry.setStatus("current")
_TmnxOamBuildPktDot1qLastChanged_Type = TimeStamp
_TmnxOamBuildPktDot1qLastChanged_Object = MibTableColumn
tmnxOamBuildPktDot1qLastChanged = _TmnxOamBuildPktDot1qLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 10, 1, 1),
    _TmnxOamBuildPktDot1qLastChanged_Type()
)
tmnxOamBuildPktDot1qLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamBuildPktDot1qLastChanged.setStatus("current")


class _TmnxOamBuildPktDot1qPrioCodePt_Type(Integer32):
    """Custom type tmnxOamBuildPktDot1qPrioCodePt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )


_TmnxOamBuildPktDot1qPrioCodePt_Type.__name__ = "Integer32"
_TmnxOamBuildPktDot1qPrioCodePt_Object = MibTableColumn
tmnxOamBuildPktDot1qPrioCodePt = _TmnxOamBuildPktDot1qPrioCodePt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 10, 1, 2),
    _TmnxOamBuildPktDot1qPrioCodePt_Type()
)
tmnxOamBuildPktDot1qPrioCodePt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamBuildPktDot1qPrioCodePt.setStatus("current")


class _TmnxOamBuildPktDot1qTagProtoId_Type(Integer32):
    """Custom type tmnxOamBuildPktDot1qTagProtoId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1536, 65535),
    )


_TmnxOamBuildPktDot1qTagProtoId_Type.__name__ = "Integer32"
_TmnxOamBuildPktDot1qTagProtoId_Object = MibTableColumn
tmnxOamBuildPktDot1qTagProtoId = _TmnxOamBuildPktDot1qTagProtoId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 10, 1, 3),
    _TmnxOamBuildPktDot1qTagProtoId_Type()
)
tmnxOamBuildPktDot1qTagProtoId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamBuildPktDot1qTagProtoId.setStatus("current")


class _TmnxOamBuildPktDot1qVlanId_Type(Integer32):
    """Custom type tmnxOamBuildPktDot1qVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 4095),
    )


_TmnxOamBuildPktDot1qVlanId_Type.__name__ = "Integer32"
_TmnxOamBuildPktDot1qVlanId_Object = MibTableColumn
tmnxOamBuildPktDot1qVlanId = _TmnxOamBuildPktDot1qVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 10, 1, 4),
    _TmnxOamBuildPktDot1qVlanId_Type()
)
tmnxOamBuildPktDot1qVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamBuildPktDot1qVlanId.setStatus("current")
_TmnxOamBuildPktIPsecAuthCtlTable_Object = MibTable
tmnxOamBuildPktIPsecAuthCtlTable = _TmnxOamBuildPktIPsecAuthCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 11)
)
if mibBuilder.loadTexts:
    tmnxOamBuildPktIPsecAuthCtlTable.setStatus("current")
_TmnxOamBuildPktIPsecAuthCtlEntry_Object = MibTableRow
tmnxOamBuildPktIPsecAuthCtlEntry = _TmnxOamBuildPktIPsecAuthCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 11, 1)
)
tmnxOamBuildPktIPsecAuthCtlEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktNumOrZero"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktHeaderNum"),
)
if mibBuilder.loadTexts:
    tmnxOamBuildPktIPsecAuthCtlEntry.setStatus("current")
_TmnxOamBuildPktIPsecAuthLastChgd_Type = TimeStamp
_TmnxOamBuildPktIPsecAuthLastChgd_Object = MibTableColumn
tmnxOamBuildPktIPsecAuthLastChgd = _TmnxOamBuildPktIPsecAuthLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 11, 1, 1),
    _TmnxOamBuildPktIPsecAuthLastChgd_Type()
)
tmnxOamBuildPktIPsecAuthLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamBuildPktIPsecAuthLastChgd.setStatus("current")


class _TmnxOamBuildPktIPsecAuthSecPrIdx_Type(Unsigned32):
    """Custom type tmnxOamBuildPktIPsecAuthSecPrIdx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxOamBuildPktIPsecAuthSecPrIdx_Type.__name__ = "Unsigned32"
_TmnxOamBuildPktIPsecAuthSecPrIdx_Object = MibTableColumn
tmnxOamBuildPktIPsecAuthSecPrIdx = _TmnxOamBuildPktIPsecAuthSecPrIdx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 11, 1, 2),
    _TmnxOamBuildPktIPsecAuthSecPrIdx_Type()
)
tmnxOamBuildPktIPsecAuthSecPrIdx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamBuildPktIPsecAuthSecPrIdx.setStatus("current")
_TmnxOamBuildPktPbbCtlTable_Object = MibTable
tmnxOamBuildPktPbbCtlTable = _TmnxOamBuildPktPbbCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 12)
)
if mibBuilder.loadTexts:
    tmnxOamBuildPktPbbCtlTable.setStatus("current")
_TmnxOamBuildPktPbbCtlEntry_Object = MibTableRow
tmnxOamBuildPktPbbCtlEntry = _TmnxOamBuildPktPbbCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 12, 1)
)
tmnxOamBuildPktPbbCtlEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktNumOrZero"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktHeaderNum"),
)
if mibBuilder.loadTexts:
    tmnxOamBuildPktPbbCtlEntry.setStatus("current")
_TmnxOamBuildPktPbbLastChanged_Type = TimeStamp
_TmnxOamBuildPktPbbLastChanged_Object = MibTableColumn
tmnxOamBuildPktPbbLastChanged = _TmnxOamBuildPktPbbLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 12, 1, 1),
    _TmnxOamBuildPktPbbLastChanged_Type()
)
tmnxOamBuildPktPbbLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamBuildPktPbbLastChanged.setStatus("current")


class _TmnxOamBuildPktPbbIsid_Type(Integer32):
    """Custom type tmnxOamBuildPktPbbIsid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 16777215),
    )


_TmnxOamBuildPktPbbIsid_Type.__name__ = "Integer32"
_TmnxOamBuildPktPbbIsid_Object = MibTableColumn
tmnxOamBuildPktPbbIsid = _TmnxOamBuildPktPbbIsid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 12, 1, 2),
    _TmnxOamBuildPktPbbIsid_Type()
)
tmnxOamBuildPktPbbIsid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamBuildPktPbbIsid.setStatus("current")


class _TmnxOamBuildPktPbbTagProtocolId_Type(Integer32):
    """Custom type tmnxOamBuildPktPbbTagProtocolId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1536, 65535),
    )


_TmnxOamBuildPktPbbTagProtocolId_Type.__name__ = "Integer32"
_TmnxOamBuildPktPbbTagProtocolId_Object = MibTableColumn
tmnxOamBuildPktPbbTagProtocolId = _TmnxOamBuildPktPbbTagProtocolId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 12, 1, 3),
    _TmnxOamBuildPktPbbTagProtocolId_Type()
)
tmnxOamBuildPktPbbTagProtocolId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamBuildPktPbbTagProtocolId.setStatus("current")
_TmnxOamBuildPktL2tpCtlTable_Object = MibTable
tmnxOamBuildPktL2tpCtlTable = _TmnxOamBuildPktL2tpCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 13)
)
if mibBuilder.loadTexts:
    tmnxOamBuildPktL2tpCtlTable.setStatus("current")
_TmnxOamBuildPktL2tpCtlEntry_Object = MibTableRow
tmnxOamBuildPktL2tpCtlEntry = _TmnxOamBuildPktL2tpCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 13, 1)
)
tmnxOamBuildPktL2tpCtlEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktNumOrZero"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktHeaderNum"),
)
if mibBuilder.loadTexts:
    tmnxOamBuildPktL2tpCtlEntry.setStatus("current")
_TmnxOamBuildPktL2tpLastChanged_Type = TimeStamp
_TmnxOamBuildPktL2tpLastChanged_Object = MibTableColumn
tmnxOamBuildPktL2tpLastChanged = _TmnxOamBuildPktL2tpLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 13, 1, 1),
    _TmnxOamBuildPktL2tpLastChanged_Type()
)
tmnxOamBuildPktL2tpLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamBuildPktL2tpLastChanged.setStatus("current")


class _TmnxOamBuildPktL2tpSessionId_Type(Integer32):
    """Custom type tmnxOamBuildPktL2tpSessionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )


_TmnxOamBuildPktL2tpSessionId_Type.__name__ = "Integer32"
_TmnxOamBuildPktL2tpSessionId_Object = MibTableColumn
tmnxOamBuildPktL2tpSessionId = _TmnxOamBuildPktL2tpSessionId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 13, 1, 2),
    _TmnxOamBuildPktL2tpSessionId_Type()
)
tmnxOamBuildPktL2tpSessionId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamBuildPktL2tpSessionId.setStatus("current")


class _TmnxOamBuildPktL2tpTunnelId_Type(Integer32):
    """Custom type tmnxOamBuildPktL2tpTunnelId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )


_TmnxOamBuildPktL2tpTunnelId_Type.__name__ = "Integer32"
_TmnxOamBuildPktL2tpTunnelId_Object = MibTableColumn
tmnxOamBuildPktL2tpTunnelId = _TmnxOamBuildPktL2tpTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 13, 1, 3),
    _TmnxOamBuildPktL2tpTunnelId_Type()
)
tmnxOamBuildPktL2tpTunnelId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamBuildPktL2tpTunnelId.setStatus("current")
_TmnxOamBuildPktMplsCtlTable_Object = MibTable
tmnxOamBuildPktMplsCtlTable = _TmnxOamBuildPktMplsCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 14)
)
if mibBuilder.loadTexts:
    tmnxOamBuildPktMplsCtlTable.setStatus("current")
_TmnxOamBuildPktMplsCtlEntry_Object = MibTableRow
tmnxOamBuildPktMplsCtlEntry = _TmnxOamBuildPktMplsCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 14, 1)
)
tmnxOamBuildPktMplsCtlEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktNumOrZero"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktHeaderNum"),
)
if mibBuilder.loadTexts:
    tmnxOamBuildPktMplsCtlEntry.setStatus("current")
_TmnxOamBuildPktMplsLastChanged_Type = TimeStamp
_TmnxOamBuildPktMplsLastChanged_Object = MibTableColumn
tmnxOamBuildPktMplsLastChanged = _TmnxOamBuildPktMplsLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 14, 1, 1),
    _TmnxOamBuildPktMplsLastChanged_Type()
)
tmnxOamBuildPktMplsLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamBuildPktMplsLastChanged.setStatus("current")


class _TmnxOamBuildPktMplsLabel_Type(Integer32):
    """Custom type tmnxOamBuildPktMplsLabel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 1048575),
    )


_TmnxOamBuildPktMplsLabel_Type.__name__ = "Integer32"
_TmnxOamBuildPktMplsLabel_Object = MibTableColumn
tmnxOamBuildPktMplsLabel = _TmnxOamBuildPktMplsLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 14, 1, 2),
    _TmnxOamBuildPktMplsLabel_Type()
)
tmnxOamBuildPktMplsLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamBuildPktMplsLabel.setStatus("current")


class _TmnxOamBuildPktMplsTrafficClass_Type(Integer32):
    """Custom type tmnxOamBuildPktMplsTrafficClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )


_TmnxOamBuildPktMplsTrafficClass_Type.__name__ = "Integer32"
_TmnxOamBuildPktMplsTrafficClass_Object = MibTableColumn
tmnxOamBuildPktMplsTrafficClass = _TmnxOamBuildPktMplsTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 14, 1, 3),
    _TmnxOamBuildPktMplsTrafficClass_Type()
)
tmnxOamBuildPktMplsTrafficClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamBuildPktMplsTrafficClass.setStatus("current")
_TmnxOamBuildPktGtpUserCtlTable_Object = MibTable
tmnxOamBuildPktGtpUserCtlTable = _TmnxOamBuildPktGtpUserCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 15)
)
if mibBuilder.loadTexts:
    tmnxOamBuildPktGtpUserCtlTable.setStatus("current")
_TmnxOamBuildPktGtpUserCtlEntry_Object = MibTableRow
tmnxOamBuildPktGtpUserCtlEntry = _TmnxOamBuildPktGtpUserCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 15, 1)
)
tmnxOamBuildPktGtpUserCtlEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktNumOrZero"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktHeaderNum"),
)
if mibBuilder.loadTexts:
    tmnxOamBuildPktGtpUserCtlEntry.setStatus("current")
_TmnxOamBuildPktGtpUserLastChgd_Type = TimeStamp
_TmnxOamBuildPktGtpUserLastChgd_Object = MibTableColumn
tmnxOamBuildPktGtpUserLastChgd = _TmnxOamBuildPktGtpUserLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 15, 1, 1),
    _TmnxOamBuildPktGtpUserLastChgd_Type()
)
tmnxOamBuildPktGtpUserLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamBuildPktGtpUserLastChgd.setStatus("current")


class _TmnxOamBuildPktGtpUserTunnEpIdHi_Type(TmnxHigh32):
    """Custom type tmnxOamBuildPktGtpUserTunnEpIdHi based on TmnxHigh32"""
    subtypeSpec = TmnxHigh32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_TmnxOamBuildPktGtpUserTunnEpIdHi_Type.__name__ = "TmnxHigh32"
_TmnxOamBuildPktGtpUserTunnEpIdHi_Object = MibTableColumn
tmnxOamBuildPktGtpUserTunnEpIdHi = _TmnxOamBuildPktGtpUserTunnEpIdHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 15, 1, 2),
    _TmnxOamBuildPktGtpUserTunnEpIdHi_Type()
)
tmnxOamBuildPktGtpUserTunnEpIdHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamBuildPktGtpUserTunnEpIdHi.setStatus("current")
_TmnxOamBuildPktGtpUserTunnEpIdLo_Type = TmnxLow32
_TmnxOamBuildPktGtpUserTunnEpIdLo_Object = MibTableColumn
tmnxOamBuildPktGtpUserTunnEpIdLo = _TmnxOamBuildPktGtpUserTunnEpIdLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 6, 15, 1, 3),
    _TmnxOamBuildPktGtpUserTunnEpIdLo_Type()
)
tmnxOamBuildPktGtpUserTunnEpIdLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamBuildPktGtpUserTunnEpIdLo.setStatus("current")
_TmnxOamNotificationObjs_ObjectIdentity = ObjectIdentity
tmnxOamNotificationObjs = _TmnxOamNotificationObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 7)
)


class _TmnxOamTestRunIndex_Type(Unsigned32):
    """Custom type tmnxOamTestRunIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxOamTestRunIndex_Type.__name__ = "Unsigned32"
_TmnxOamTestRunIndex_Object = MibScalar
tmnxOamTestRunIndex = _TmnxOamTestRunIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 7, 1),
    _TmnxOamTestRunIndex_Type()
)
tmnxOamTestRunIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxOamTestRunIndex.setStatus("current")
_TmnxOamIfPingObjs_ObjectIdentity = ObjectIdentity
tmnxOamIfPingObjs = _TmnxOamIfPingObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 8)
)
_TmnxOamIfPingTmplCtlTable_Object = MibTable
tmnxOamIfPingTmplCtlTable = _TmnxOamIfPingTmplCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 8, 1)
)
if mibBuilder.loadTexts:
    tmnxOamIfPingTmplCtlTable.setStatus("current")
_TmnxOamIfPingTmplCtlEntry_Object = MibTableRow
tmnxOamIfPingTmplCtlEntry = _TmnxOamIfPingTmplCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 8, 1, 1)
)
tmnxOamIfPingTmplCtlEntry.setIndexNames(
    (1, "TIMETRA-OAM-TEST-MIB", "tmnxOamIfPingTmplCtlName"),
)
if mibBuilder.loadTexts:
    tmnxOamIfPingTmplCtlEntry.setStatus("current")
_TmnxOamIfPingTmplCtlName_Type = TLNamedItem
_TmnxOamIfPingTmplCtlName_Object = MibTableColumn
tmnxOamIfPingTmplCtlName = _TmnxOamIfPingTmplCtlName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 8, 1, 1, 1),
    _TmnxOamIfPingTmplCtlName_Type()
)
tmnxOamIfPingTmplCtlName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamIfPingTmplCtlName.setStatus("current")
_TmnxOamIfPingTmplCtlRowStatus_Type = RowStatus
_TmnxOamIfPingTmplCtlRowStatus_Object = MibTableColumn
tmnxOamIfPingTmplCtlRowStatus = _TmnxOamIfPingTmplCtlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 8, 1, 1, 2),
    _TmnxOamIfPingTmplCtlRowStatus_Type()
)
tmnxOamIfPingTmplCtlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamIfPingTmplCtlRowStatus.setStatus("current")
_TmnxOamIfPingTmplCtlLastMgmtChg_Type = TimeStamp
_TmnxOamIfPingTmplCtlLastMgmtChg_Object = MibTableColumn
tmnxOamIfPingTmplCtlLastMgmtChg = _TmnxOamIfPingTmplCtlLastMgmtChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 8, 1, 1, 3),
    _TmnxOamIfPingTmplCtlLastMgmtChg_Type()
)
tmnxOamIfPingTmplCtlLastMgmtChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamIfPingTmplCtlLastMgmtChg.setStatus("current")


class _TmnxOamIfPingTmplCtlDescription_Type(TItemDescription):
    """Custom type tmnxOamIfPingTmplCtlDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxOamIfPingTmplCtlDescription_Type.__name__ = "TItemDescription"
_TmnxOamIfPingTmplCtlDescription_Object = MibTableColumn
tmnxOamIfPingTmplCtlDescription = _TmnxOamIfPingTmplCtlDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 8, 1, 1, 4),
    _TmnxOamIfPingTmplCtlDescription_Type()
)
tmnxOamIfPingTmplCtlDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamIfPingTmplCtlDescription.setStatus("current")


class _TmnxOamIfPingTmplCtlDscp_Type(TDSCPName):
    """Custom type tmnxOamIfPingTmplCtlDscp based on TDSCPName"""
    defaultValue = OctetString("nc1")


_TmnxOamIfPingTmplCtlDscp_Type.__name__ = "TDSCPName"
_TmnxOamIfPingTmplCtlDscp_Object = MibTableColumn
tmnxOamIfPingTmplCtlDscp = _TmnxOamIfPingTmplCtlDscp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 8, 1, 1, 5),
    _TmnxOamIfPingTmplCtlDscp_Type()
)
tmnxOamIfPingTmplCtlDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamIfPingTmplCtlDscp.setStatus("current")


class _TmnxOamIfPingTmplCtlDot1p_Type(Dot1PPriority):
    """Custom type tmnxOamIfPingTmplCtlDot1p based on Dot1PPriority"""
    defaultValue = 7

    subtypeSpec = Dot1PPriority.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TmnxOamIfPingTmplCtlDot1p_Type.__name__ = "Dot1PPriority"
_TmnxOamIfPingTmplCtlDot1p_Object = MibTableColumn
tmnxOamIfPingTmplCtlDot1p = _TmnxOamIfPingTmplCtlDot1p_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 8, 1, 1, 6),
    _TmnxOamIfPingTmplCtlDot1p_Type()
)
tmnxOamIfPingTmplCtlDot1p.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamIfPingTmplCtlDot1p.setStatus("current")


class _TmnxOamIfPingTmplCtlInterval_Type(Unsigned32):
    """Custom type tmnxOamIfPingTmplCtlInterval based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TmnxOamIfPingTmplCtlInterval_Type.__name__ = "Unsigned32"
_TmnxOamIfPingTmplCtlInterval_Object = MibTableColumn
tmnxOamIfPingTmplCtlInterval = _TmnxOamIfPingTmplCtlInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 8, 1, 1, 7),
    _TmnxOamIfPingTmplCtlInterval_Type()
)
tmnxOamIfPingTmplCtlInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamIfPingTmplCtlInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamIfPingTmplCtlInterval.setUnits("seconds")


class _TmnxOamIfPingTmplCtlTimeout_Type(Unsigned32):
    """Custom type tmnxOamIfPingTmplCtlTimeout based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TmnxOamIfPingTmplCtlTimeout_Type.__name__ = "Unsigned32"
_TmnxOamIfPingTmplCtlTimeout_Object = MibTableColumn
tmnxOamIfPingTmplCtlTimeout = _TmnxOamIfPingTmplCtlTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 8, 1, 1, 8),
    _TmnxOamIfPingTmplCtlTimeout_Type()
)
tmnxOamIfPingTmplCtlTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamIfPingTmplCtlTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamIfPingTmplCtlTimeout.setUnits("seconds")


class _TmnxOamIfPingTmplCtlFailThrld_Type(Unsigned32):
    """Custom type tmnxOamIfPingTmplCtlFailThrld based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_TmnxOamIfPingTmplCtlFailThrld_Type.__name__ = "Unsigned32"
_TmnxOamIfPingTmplCtlFailThrld_Object = MibTableColumn
tmnxOamIfPingTmplCtlFailThrld = _TmnxOamIfPingTmplCtlFailThrld_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 8, 1, 1, 9),
    _TmnxOamIfPingTmplCtlFailThrld_Type()
)
tmnxOamIfPingTmplCtlFailThrld.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamIfPingTmplCtlFailThrld.setStatus("current")


class _TmnxOamIfPingTmplCtlReactInt_Type(Unsigned32):
    """Custom type tmnxOamIfPingTmplCtlReactInt based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TmnxOamIfPingTmplCtlReactInt_Type.__name__ = "Unsigned32"
_TmnxOamIfPingTmplCtlReactInt_Object = MibTableColumn
tmnxOamIfPingTmplCtlReactInt = _TmnxOamIfPingTmplCtlReactInt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 8, 1, 1, 10),
    _TmnxOamIfPingTmplCtlReactInt_Type()
)
tmnxOamIfPingTmplCtlReactInt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamIfPingTmplCtlReactInt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamIfPingTmplCtlReactInt.setUnits("seconds")


class _TmnxOamIfPingTmplCtlReactFailThr_Type(Unsigned32):
    """Custom type tmnxOamIfPingTmplCtlReactFailThr based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TmnxOamIfPingTmplCtlReactFailThr_Type.__name__ = "Unsigned32"
_TmnxOamIfPingTmplCtlReactFailThr_Object = MibTableColumn
tmnxOamIfPingTmplCtlReactFailThr = _TmnxOamIfPingTmplCtlReactFailThr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 8, 1, 1, 11),
    _TmnxOamIfPingTmplCtlReactFailThr_Type()
)
tmnxOamIfPingTmplCtlReactFailThr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamIfPingTmplCtlReactFailThr.setStatus("current")


class _TmnxOamIfPingTmplCtlReactTimeout_Type(Unsigned32):
    """Custom type tmnxOamIfPingTmplCtlReactTimeout based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TmnxOamIfPingTmplCtlReactTimeout_Type.__name__ = "Unsigned32"
_TmnxOamIfPingTmplCtlReactTimeout_Object = MibTableColumn
tmnxOamIfPingTmplCtlReactTimeout = _TmnxOamIfPingTmplCtlReactTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 8, 1, 1, 12),
    _TmnxOamIfPingTmplCtlReactTimeout_Type()
)
tmnxOamIfPingTmplCtlReactTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamIfPingTmplCtlReactTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamIfPingTmplCtlReactTimeout.setUnits("seconds")


class _TmnxOamIfPingTmplCtlReactThrld_Type(Unsigned32):
    """Custom type tmnxOamIfPingTmplCtlReactThrld based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TmnxOamIfPingTmplCtlReactThrld_Type.__name__ = "Unsigned32"
_TmnxOamIfPingTmplCtlReactThrld_Object = MibTableColumn
tmnxOamIfPingTmplCtlReactThrld = _TmnxOamIfPingTmplCtlReactThrld_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 8, 1, 1, 13),
    _TmnxOamIfPingTmplCtlReactThrld_Type()
)
tmnxOamIfPingTmplCtlReactThrld.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamIfPingTmplCtlReactThrld.setStatus("current")


class _TmnxOamIfPingTmplCtlSize_Type(Unsigned32):
    """Custom type tmnxOamIfPingTmplCtlSize based on Unsigned32"""
    defaultValue = 56

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(12, 9786),
    )


_TmnxOamIfPingTmplCtlSize_Type.__name__ = "Unsigned32"
_TmnxOamIfPingTmplCtlSize_Object = MibTableColumn
tmnxOamIfPingTmplCtlSize = _TmnxOamIfPingTmplCtlSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 8, 1, 1, 14),
    _TmnxOamIfPingTmplCtlSize_Type()
)
tmnxOamIfPingTmplCtlSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamIfPingTmplCtlSize.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamIfPingTmplCtlSize.setUnits("octets")


class _TmnxOamIfPingTmplCtlTtl_Type(Unsigned32):
    """Custom type tmnxOamIfPingTmplCtlTtl based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TmnxOamIfPingTmplCtlTtl_Type.__name__ = "Unsigned32"
_TmnxOamIfPingTmplCtlTtl_Object = MibTableColumn
tmnxOamIfPingTmplCtlTtl = _TmnxOamIfPingTmplCtlTtl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 8, 1, 1, 15),
    _TmnxOamIfPingTmplCtlTtl_Type()
)
tmnxOamIfPingTmplCtlTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamIfPingTmplCtlTtl.setStatus("current")


class _TmnxOamIfPingTmplCtlSync_Type(TmnxActionType):
    """Custom type tmnxOamIfPingTmplCtlSync based on TmnxActionType"""
    defaultValue = 2


_TmnxOamIfPingTmplCtlSync_Type.__name__ = "TmnxActionType"
_TmnxOamIfPingTmplCtlSync_Object = MibTableColumn
tmnxOamIfPingTmplCtlSync = _TmnxOamIfPingTmplCtlSync_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 8, 1, 1, 16),
    _TmnxOamIfPingTmplCtlSync_Type()
)
tmnxOamIfPingTmplCtlSync.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamIfPingTmplCtlSync.setStatus("current")
_TmnxOamIfPingIfTable_Object = MibTable
tmnxOamIfPingIfTable = _TmnxOamIfPingIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 8, 2)
)
if mibBuilder.loadTexts:
    tmnxOamIfPingIfTable.setStatus("current")
_TmnxOamIfPingIfEntry_Object = MibTableRow
tmnxOamIfPingIfEntry = _TmnxOamIfPingIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 8, 2, 1)
)
tmnxOamIfPingIfEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamIfPingIfEntry.setStatus("current")
_TmnxOamIfPingIfRowStatus_Type = RowStatus
_TmnxOamIfPingIfRowStatus_Object = MibTableColumn
tmnxOamIfPingIfRowStatus = _TmnxOamIfPingIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 8, 2, 1, 1),
    _TmnxOamIfPingIfRowStatus_Type()
)
tmnxOamIfPingIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamIfPingIfRowStatus.setStatus("current")
_TmnxOamIfPingIfTemplate_Type = TLNamedItem
_TmnxOamIfPingIfTemplate_Object = MibTableColumn
tmnxOamIfPingIfTemplate = _TmnxOamIfPingIfTemplate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 8, 2, 1, 2),
    _TmnxOamIfPingIfTemplate_Type()
)
tmnxOamIfPingIfTemplate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamIfPingIfTemplate.setStatus("current")
_TmnxOamIfPingIfLastChanged_Type = TimeStamp
_TmnxOamIfPingIfLastChanged_Object = MibTableColumn
tmnxOamIfPingIfLastChanged = _TmnxOamIfPingIfLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 8, 2, 1, 3),
    _TmnxOamIfPingIfLastChanged_Type()
)
tmnxOamIfPingIfLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamIfPingIfLastChanged.setStatus("current")


class _TmnxOamIfPingIfAdminState_Type(TmnxAdminState):
    """Custom type tmnxOamIfPingIfAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxOamIfPingIfAdminState_Type.__name__ = "TmnxAdminState"
_TmnxOamIfPingIfAdminState_Object = MibTableColumn
tmnxOamIfPingIfAdminState = _TmnxOamIfPingIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 8, 2, 1, 4),
    _TmnxOamIfPingIfAdminState_Type()
)
tmnxOamIfPingIfAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamIfPingIfAdminState.setStatus("current")


class _TmnxOamIfPingIfDestAddrType_Type(InetAddressType):
    """Custom type tmnxOamIfPingIfDestAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxOamIfPingIfDestAddrType_Type.__name__ = "InetAddressType"
_TmnxOamIfPingIfDestAddrType_Object = MibTableColumn
tmnxOamIfPingIfDestAddrType = _TmnxOamIfPingIfDestAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 8, 2, 1, 5),
    _TmnxOamIfPingIfDestAddrType_Type()
)
tmnxOamIfPingIfDestAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamIfPingIfDestAddrType.setStatus("current")


class _TmnxOamIfPingIfDestAddr_Type(InetAddress):
    """Custom type tmnxOamIfPingIfDestAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamIfPingIfDestAddr_Type.__name__ = "InetAddress"
_TmnxOamIfPingIfDestAddr_Object = MibTableColumn
tmnxOamIfPingIfDestAddr = _TmnxOamIfPingIfDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 8, 2, 1, 6),
    _TmnxOamIfPingIfDestAddr_Type()
)
tmnxOamIfPingIfDestAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamIfPingIfDestAddr.setStatus("current")
_TmnxOamIfPingIfFailThrldCnt_Type = Counter32
_TmnxOamIfPingIfFailThrldCnt_Object = MibTableColumn
tmnxOamIfPingIfFailThrldCnt = _TmnxOamIfPingIfFailThrldCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 8, 2, 1, 7),
    _TmnxOamIfPingIfFailThrldCnt_Type()
)
tmnxOamIfPingIfFailThrldCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamIfPingIfFailThrldCnt.setStatus("current")
_TmnxOamIfPingIfPassThrldCnt_Type = Counter32
_TmnxOamIfPingIfPassThrldCnt_Object = MibTableColumn
tmnxOamIfPingIfPassThrldCnt = _TmnxOamIfPingIfPassThrldCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 8, 2, 1, 8),
    _TmnxOamIfPingIfPassThrldCnt_Type()
)
tmnxOamIfPingIfPassThrldCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamIfPingIfPassThrldCnt.setStatus("current")
_TmnxOamIfPingIfCtlDscp_Type = TDSCPName
_TmnxOamIfPingIfCtlDscp_Object = MibTableColumn
tmnxOamIfPingIfCtlDscp = _TmnxOamIfPingIfCtlDscp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 8, 2, 1, 9),
    _TmnxOamIfPingIfCtlDscp_Type()
)
tmnxOamIfPingIfCtlDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamIfPingIfCtlDscp.setStatus("current")


class _TmnxOamIfPingIfCtlDot1p_Type(Dot1PPriority):
    """Custom type tmnxOamIfPingIfCtlDot1p based on Dot1PPriority"""
    subtypeSpec = Dot1PPriority.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TmnxOamIfPingIfCtlDot1p_Type.__name__ = "Dot1PPriority"
_TmnxOamIfPingIfCtlDot1p_Object = MibTableColumn
tmnxOamIfPingIfCtlDot1p = _TmnxOamIfPingIfCtlDot1p_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 8, 2, 1, 10),
    _TmnxOamIfPingIfCtlDot1p_Type()
)
tmnxOamIfPingIfCtlDot1p.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamIfPingIfCtlDot1p.setStatus("current")


class _TmnxOamIfPingIfCtlInterval_Type(Unsigned32):
    """Custom type tmnxOamIfPingIfCtlInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TmnxOamIfPingIfCtlInterval_Type.__name__ = "Unsigned32"
_TmnxOamIfPingIfCtlInterval_Object = MibTableColumn
tmnxOamIfPingIfCtlInterval = _TmnxOamIfPingIfCtlInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 8, 2, 1, 11),
    _TmnxOamIfPingIfCtlInterval_Type()
)
tmnxOamIfPingIfCtlInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamIfPingIfCtlInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamIfPingIfCtlInterval.setUnits("seconds")


class _TmnxOamIfPingIfCtlTimeout_Type(Unsigned32):
    """Custom type tmnxOamIfPingIfCtlTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TmnxOamIfPingIfCtlTimeout_Type.__name__ = "Unsigned32"
_TmnxOamIfPingIfCtlTimeout_Object = MibTableColumn
tmnxOamIfPingIfCtlTimeout = _TmnxOamIfPingIfCtlTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 8, 2, 1, 12),
    _TmnxOamIfPingIfCtlTimeout_Type()
)
tmnxOamIfPingIfCtlTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamIfPingIfCtlTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamIfPingIfCtlTimeout.setUnits("seconds")


class _TmnxOamIfPingIfCtlFailThrld_Type(Unsigned32):
    """Custom type tmnxOamIfPingIfCtlFailThrld based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TmnxOamIfPingIfCtlFailThrld_Type.__name__ = "Unsigned32"
_TmnxOamIfPingIfCtlFailThrld_Object = MibTableColumn
tmnxOamIfPingIfCtlFailThrld = _TmnxOamIfPingIfCtlFailThrld_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 8, 2, 1, 13),
    _TmnxOamIfPingIfCtlFailThrld_Type()
)
tmnxOamIfPingIfCtlFailThrld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamIfPingIfCtlFailThrld.setStatus("current")


class _TmnxOamIfPingIfCtlReactInt_Type(Unsigned32):
    """Custom type tmnxOamIfPingIfCtlReactInt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TmnxOamIfPingIfCtlReactInt_Type.__name__ = "Unsigned32"
_TmnxOamIfPingIfCtlReactInt_Object = MibTableColumn
tmnxOamIfPingIfCtlReactInt = _TmnxOamIfPingIfCtlReactInt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 8, 2, 1, 14),
    _TmnxOamIfPingIfCtlReactInt_Type()
)
tmnxOamIfPingIfCtlReactInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamIfPingIfCtlReactInt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamIfPingIfCtlReactInt.setUnits("seconds")


class _TmnxOamIfPingIfCtlReactFailThr_Type(Unsigned32):
    """Custom type tmnxOamIfPingIfCtlReactFailThr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_TmnxOamIfPingIfCtlReactFailThr_Type.__name__ = "Unsigned32"
_TmnxOamIfPingIfCtlReactFailThr_Object = MibTableColumn
tmnxOamIfPingIfCtlReactFailThr = _TmnxOamIfPingIfCtlReactFailThr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 8, 2, 1, 15),
    _TmnxOamIfPingIfCtlReactFailThr_Type()
)
tmnxOamIfPingIfCtlReactFailThr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamIfPingIfCtlReactFailThr.setStatus("current")


class _TmnxOamIfPingIfCtlReactTimeout_Type(Unsigned32):
    """Custom type tmnxOamIfPingIfCtlReactTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TmnxOamIfPingIfCtlReactTimeout_Type.__name__ = "Unsigned32"
_TmnxOamIfPingIfCtlReactTimeout_Object = MibTableColumn
tmnxOamIfPingIfCtlReactTimeout = _TmnxOamIfPingIfCtlReactTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 8, 2, 1, 16),
    _TmnxOamIfPingIfCtlReactTimeout_Type()
)
tmnxOamIfPingIfCtlReactTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamIfPingIfCtlReactTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamIfPingIfCtlReactTimeout.setUnits("seconds")


class _TmnxOamIfPingIfCtlReactThrld_Type(Unsigned32):
    """Custom type tmnxOamIfPingIfCtlReactThrld based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TmnxOamIfPingIfCtlReactThrld_Type.__name__ = "Unsigned32"
_TmnxOamIfPingIfCtlReactThrld_Object = MibTableColumn
tmnxOamIfPingIfCtlReactThrld = _TmnxOamIfPingIfCtlReactThrld_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 8, 2, 1, 17),
    _TmnxOamIfPingIfCtlReactThrld_Type()
)
tmnxOamIfPingIfCtlReactThrld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamIfPingIfCtlReactThrld.setStatus("current")


class _TmnxOamIfPingIfCtlSize_Type(Unsigned32):
    """Custom type tmnxOamIfPingIfCtlSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(56, 9786),
    )


_TmnxOamIfPingIfCtlSize_Type.__name__ = "Unsigned32"
_TmnxOamIfPingIfCtlSize_Object = MibTableColumn
tmnxOamIfPingIfCtlSize = _TmnxOamIfPingIfCtlSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 8, 2, 1, 18),
    _TmnxOamIfPingIfCtlSize_Type()
)
tmnxOamIfPingIfCtlSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamIfPingIfCtlSize.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamIfPingIfCtlSize.setUnits("octets")


class _TmnxOamIfPingIfCtlTtl_Type(Unsigned32):
    """Custom type tmnxOamIfPingIfCtlTtl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TmnxOamIfPingIfCtlTtl_Type.__name__ = "Unsigned32"
_TmnxOamIfPingIfCtlTtl_Object = MibTableColumn
tmnxOamIfPingIfCtlTtl = _TmnxOamIfPingIfCtlTtl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 8, 2, 1, 19),
    _TmnxOamIfPingIfCtlTtl_Type()
)
tmnxOamIfPingIfCtlTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamIfPingIfCtlTtl.setStatus("current")


class _TmnxOamIfPingIfCurrentInterval_Type(Integer32):
    """Custom type tmnxOamIfPingIfCurrentInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("interval", 0),
          ("reactivation", 1))
    )


_TmnxOamIfPingIfCurrentInterval_Type.__name__ = "Integer32"
_TmnxOamIfPingIfCurrentInterval_Object = MibTableColumn
tmnxOamIfPingIfCurrentInterval = _TmnxOamIfPingIfCurrentInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 8, 2, 1, 20),
    _TmnxOamIfPingIfCurrentInterval_Type()
)
tmnxOamIfPingIfCurrentInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamIfPingIfCurrentInterval.setStatus("current")


class _TmnxOamIfPingIfCurrentState_Type(Integer32):
    """Custom type tmnxOamIfPingIfCurrentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("operational", 0),
          ("recovering", 1),
          ("failed", 2))
    )


_TmnxOamIfPingIfCurrentState_Type.__name__ = "Integer32"
_TmnxOamIfPingIfCurrentState_Object = MibTableColumn
tmnxOamIfPingIfCurrentState = _TmnxOamIfPingIfCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 8, 2, 1, 21),
    _TmnxOamIfPingIfCurrentState_Type()
)
tmnxOamIfPingIfCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamIfPingIfCurrentState.setStatus("current")
_TmnxOamLnkMeasObjs_ObjectIdentity = ObjectIdentity
tmnxOamLnkMeasObjs = _TmnxOamLnkMeasObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9)
)
_TmnxOamLnkMeasTmplCtlTable_Object = MibTable
tmnxOamLnkMeasTmplCtlTable = _TmnxOamLnkMeasTmplCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 1)
)
if mibBuilder.loadTexts:
    tmnxOamLnkMeasTmplCtlTable.setStatus("current")
_TmnxOamLnkMeasTmplCtlEntry_Object = MibTableRow
tmnxOamLnkMeasTmplCtlEntry = _TmnxOamLnkMeasTmplCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 1, 1)
)
tmnxOamLnkMeasTmplCtlEntry.setIndexNames(
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasTmplCtlName"),
)
if mibBuilder.loadTexts:
    tmnxOamLnkMeasTmplCtlEntry.setStatus("current")
_TmnxOamLnkMeasTmplCtlName_Type = TLNamedItem
_TmnxOamLnkMeasTmplCtlName_Object = MibTableColumn
tmnxOamLnkMeasTmplCtlName = _TmnxOamLnkMeasTmplCtlName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 1, 1, 1),
    _TmnxOamLnkMeasTmplCtlName_Type()
)
tmnxOamLnkMeasTmplCtlName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasTmplCtlName.setStatus("current")
_TmnxOamLnkMeasTmplCtlRowStatus_Type = RowStatus
_TmnxOamLnkMeasTmplCtlRowStatus_Object = MibTableColumn
tmnxOamLnkMeasTmplCtlRowStatus = _TmnxOamLnkMeasTmplCtlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 1, 1, 2),
    _TmnxOamLnkMeasTmplCtlRowStatus_Type()
)
tmnxOamLnkMeasTmplCtlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasTmplCtlRowStatus.setStatus("current")
_TmnxOamLnkMeasTmplCtlLastMgmtChg_Type = TimeStamp
_TmnxOamLnkMeasTmplCtlLastMgmtChg_Object = MibTableColumn
tmnxOamLnkMeasTmplCtlLastMgmtChg = _TmnxOamLnkMeasTmplCtlLastMgmtChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 1, 1, 3),
    _TmnxOamLnkMeasTmplCtlLastMgmtChg_Type()
)
tmnxOamLnkMeasTmplCtlLastMgmtChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasTmplCtlLastMgmtChg.setStatus("current")


class _TmnxOamLnkMeasTmplCtlDescription_Type(TItemDescription):
    """Custom type tmnxOamLnkMeasTmplCtlDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxOamLnkMeasTmplCtlDescription_Type.__name__ = "TItemDescription"
_TmnxOamLnkMeasTmplCtlDescription_Object = MibTableColumn
tmnxOamLnkMeasTmplCtlDescription = _TmnxOamLnkMeasTmplCtlDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 1, 1, 4),
    _TmnxOamLnkMeasTmplCtlDescription_Type()
)
tmnxOamLnkMeasTmplCtlDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasTmplCtlDescription.setStatus("current")


class _TmnxOamLnkMeasTmplCtlUnidirMeasT_Type(Integer32):
    """Custom type tmnxOamLnkMeasTmplCtlUnidirMeasT based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("derived", 1),
          ("actual", 2))
    )


_TmnxOamLnkMeasTmplCtlUnidirMeasT_Type.__name__ = "Integer32"
_TmnxOamLnkMeasTmplCtlUnidirMeasT_Object = MibTableColumn
tmnxOamLnkMeasTmplCtlUnidirMeasT = _TmnxOamLnkMeasTmplCtlUnidirMeasT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 1, 1, 5),
    _TmnxOamLnkMeasTmplCtlUnidirMeasT_Type()
)
tmnxOamLnkMeasTmplCtlUnidirMeasT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasTmplCtlUnidirMeasT.setStatus("current")


class _TmnxOamLnkMeasTmplCtlDelayMeasTy_Type(Integer32):
    """Custom type tmnxOamLnkMeasTmplCtlDelayMeasTy based on Integer32"""
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
        *(("min", 1),
          ("max", 2),
          ("avg", 3))
    )


_TmnxOamLnkMeasTmplCtlDelayMeasTy_Type.__name__ = "Integer32"
_TmnxOamLnkMeasTmplCtlDelayMeasTy_Object = MibTableColumn
tmnxOamLnkMeasTmplCtlDelayMeasTy = _TmnxOamLnkMeasTmplCtlDelayMeasTy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 1, 1, 6),
    _TmnxOamLnkMeasTmplCtlDelayMeasTy_Type()
)
tmnxOamLnkMeasTmplCtlDelayMeasTy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasTmplCtlDelayMeasTy.setStatus("current")


class _TmnxOamLnkMeasTmplCtlInterval_Type(Unsigned32):
    """Custom type tmnxOamLnkMeasTmplCtlInterval based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TmnxOamLnkMeasTmplCtlInterval_Type.__name__ = "Unsigned32"
_TmnxOamLnkMeasTmplCtlInterval_Object = MibTableColumn
tmnxOamLnkMeasTmplCtlInterval = _TmnxOamLnkMeasTmplCtlInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 1, 1, 7),
    _TmnxOamLnkMeasTmplCtlInterval_Type()
)
tmnxOamLnkMeasTmplCtlInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasTmplCtlInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasTmplCtlInterval.setUnits("seconds")


class _TmnxOamLnkMeasTmplCtlLastRepHold_Type(Unsigned32):
    """Custom type tmnxOamLnkMeasTmplCtlLastRepHold based on Unsigned32"""
    defaultValue = 86400

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 86400),
    )


_TmnxOamLnkMeasTmplCtlLastRepHold_Type.__name__ = "Unsigned32"
_TmnxOamLnkMeasTmplCtlLastRepHold_Object = MibTableColumn
tmnxOamLnkMeasTmplCtlLastRepHold = _TmnxOamLnkMeasTmplCtlLastRepHold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 1, 1, 8),
    _TmnxOamLnkMeasTmplCtlLastRepHold_Type()
)
tmnxOamLnkMeasTmplCtlLastRepHold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasTmplCtlLastRepHold.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasTmplCtlLastRepHold.setUnits("seconds")


class _TmnxOamLnkMeasTmplCtlDscpEgrRmrk_Type(TruthValue):
    """Custom type tmnxOamLnkMeasTmplCtlDscpEgrRmrk based on TruthValue"""
    defaultValue = 2


_TmnxOamLnkMeasTmplCtlDscpEgrRmrk_Type.__name__ = "TruthValue"
_TmnxOamLnkMeasTmplCtlDscpEgrRmrk_Object = MibTableColumn
tmnxOamLnkMeasTmplCtlDscpEgrRmrk = _TmnxOamLnkMeasTmplCtlDscpEgrRmrk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 1, 1, 9),
    _TmnxOamLnkMeasTmplCtlDscpEgrRmrk_Type()
)
tmnxOamLnkMeasTmplCtlDscpEgrRmrk.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasTmplCtlDscpEgrRmrk.setStatus("current")


class _TmnxOamLnkMeasTmplCtlIpv6UdpZero_Type(TruthValue):
    """Custom type tmnxOamLnkMeasTmplCtlIpv6UdpZero based on TruthValue"""
    defaultValue = 2


_TmnxOamLnkMeasTmplCtlIpv6UdpZero_Type.__name__ = "TruthValue"
_TmnxOamLnkMeasTmplCtlIpv6UdpZero_Object = MibTableColumn
tmnxOamLnkMeasTmplCtlIpv6UdpZero = _TmnxOamLnkMeasTmplCtlIpv6UdpZero_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 1, 1, 10),
    _TmnxOamLnkMeasTmplCtlIpv6UdpZero_Type()
)
tmnxOamLnkMeasTmplCtlIpv6UdpZero.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasTmplCtlIpv6UdpZero.setStatus("current")


class _TmnxOamLnkMeasTmplCtlDscpName_Type(TDSCPName):
    """Custom type tmnxOamLnkMeasTmplCtlDscpName based on TDSCPName"""
    defaultValue = OctetString("nc1")


_TmnxOamLnkMeasTmplCtlDscpName_Type.__name__ = "TDSCPName"
_TmnxOamLnkMeasTmplCtlDscpName_Object = MibTableColumn
tmnxOamLnkMeasTmplCtlDscpName = _TmnxOamLnkMeasTmplCtlDscpName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 1, 1, 11),
    _TmnxOamLnkMeasTmplCtlDscpName_Type()
)
tmnxOamLnkMeasTmplCtlDscpName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasTmplCtlDscpName.setStatus("current")


class _TmnxOamLnkMeasTmplCtlDstUdpPort_Type(InetPortNumber):
    """Custom type tmnxOamLnkMeasTmplCtlDstUdpPort based on InetPortNumber"""
    defaultValue = 862

    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmnxOamLnkMeasTmplCtlDstUdpPort_Type.__name__ = "InetPortNumber"
_TmnxOamLnkMeasTmplCtlDstUdpPort_Object = MibTableColumn
tmnxOamLnkMeasTmplCtlDstUdpPort = _TmnxOamLnkMeasTmplCtlDstUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 1, 1, 12),
    _TmnxOamLnkMeasTmplCtlDstUdpPort_Type()
)
tmnxOamLnkMeasTmplCtlDstUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasTmplCtlDstUdpPort.setStatus("current")


class _TmnxOamLnkMeasTmplCtlFC_Type(TFCName):
    """Custom type tmnxOamLnkMeasTmplCtlFC based on TFCName"""
    defaultValue = OctetString("h1")


_TmnxOamLnkMeasTmplCtlFC_Type.__name__ = "TFCName"
_TmnxOamLnkMeasTmplCtlFC_Object = MibTableColumn
tmnxOamLnkMeasTmplCtlFC = _TmnxOamLnkMeasTmplCtlFC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 1, 1, 13),
    _TmnxOamLnkMeasTmplCtlFC_Type()
)
tmnxOamLnkMeasTmplCtlFC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasTmplCtlFC.setStatus("current")


class _TmnxOamLnkMeasTmplCtlProfile_Type(TProfile):
    """Custom type tmnxOamLnkMeasTmplCtlProfile based on TProfile"""
    defaultValue = 1


_TmnxOamLnkMeasTmplCtlProfile_Type.__name__ = "TProfile"
_TmnxOamLnkMeasTmplCtlProfile_Object = MibTableColumn
tmnxOamLnkMeasTmplCtlProfile = _TmnxOamLnkMeasTmplCtlProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 1, 1, 14),
    _TmnxOamLnkMeasTmplCtlProfile_Type()
)
tmnxOamLnkMeasTmplCtlProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasTmplCtlProfile.setStatus("current")


class _TmnxOamLnkMeasTmplCtlTwlTmStpFmt_Type(Integer32):
    """Custom type tmnxOamLnkMeasTmplCtlTwlTmStpFmt based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ntp", 1),
          ("ptp", 2))
    )


_TmnxOamLnkMeasTmplCtlTwlTmStpFmt_Type.__name__ = "Integer32"
_TmnxOamLnkMeasTmplCtlTwlTmStpFmt_Object = MibTableColumn
tmnxOamLnkMeasTmplCtlTwlTmStpFmt = _TmnxOamLnkMeasTmplCtlTwlTmStpFmt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 1, 1, 15),
    _TmnxOamLnkMeasTmplCtlTwlTmStpFmt_Type()
)
tmnxOamLnkMeasTmplCtlTwlTmStpFmt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasTmplCtlTwlTmStpFmt.setStatus("current")


class _TmnxOamLnkMeasTmplCtlTwlTimeLive_Type(Unsigned32):
    """Custom type tmnxOamLnkMeasTmplCtlTwlTimeLive based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TmnxOamLnkMeasTmplCtlTwlTimeLive_Type.__name__ = "Unsigned32"
_TmnxOamLnkMeasTmplCtlTwlTimeLive_Object = MibTableColumn
tmnxOamLnkMeasTmplCtlTwlTimeLive = _TmnxOamLnkMeasTmplCtlTwlTimeLive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 1, 1, 16),
    _TmnxOamLnkMeasTmplCtlTwlTimeLive_Type()
)
tmnxOamLnkMeasTmplCtlTwlTimeLive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasTmplCtlTwlTimeLive.setStatus("current")


class _TmnxOamLnkMeasTmplCtlSWMultplir_Type(Unsigned32):
    """Custom type tmnxOamLnkMeasTmplCtlSWMultplir based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_TmnxOamLnkMeasTmplCtlSWMultplir_Type.__name__ = "Unsigned32"
_TmnxOamLnkMeasTmplCtlSWMultplir_Object = MibTableColumn
tmnxOamLnkMeasTmplCtlSWMultplir = _TmnxOamLnkMeasTmplCtlSWMultplir_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 1, 1, 17),
    _TmnxOamLnkMeasTmplCtlSWMultplir_Type()
)
tmnxOamLnkMeasTmplCtlSWMultplir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasTmplCtlSWMultplir.setStatus("current")


class _TmnxOamLnkMeasTmplCtlSWIntegrity_Type(Unsigned32):
    """Custom type tmnxOamLnkMeasTmplCtlSWIntegrity based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 100),
    )


_TmnxOamLnkMeasTmplCtlSWIntegrity_Type.__name__ = "Unsigned32"
_TmnxOamLnkMeasTmplCtlSWIntegrity_Object = MibTableColumn
tmnxOamLnkMeasTmplCtlSWIntegrity = _TmnxOamLnkMeasTmplCtlSWIntegrity_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 1, 1, 18),
    _TmnxOamLnkMeasTmplCtlSWIntegrity_Type()
)
tmnxOamLnkMeasTmplCtlSWIntegrity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasTmplCtlSWIntegrity.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasTmplCtlSWIntegrity.setUnits("percent")


class _TmnxOamLnkMeasTmplCtlSWThrldRel_Type(Unsigned32):
    """Custom type tmnxOamLnkMeasTmplCtlSWThrldRel based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 500),
    )


_TmnxOamLnkMeasTmplCtlSWThrldRel_Type.__name__ = "Unsigned32"
_TmnxOamLnkMeasTmplCtlSWThrldRel_Object = MibTableColumn
tmnxOamLnkMeasTmplCtlSWThrldRel = _TmnxOamLnkMeasTmplCtlSWThrldRel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 1, 1, 19),
    _TmnxOamLnkMeasTmplCtlSWThrldRel_Type()
)
tmnxOamLnkMeasTmplCtlSWThrldRel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasTmplCtlSWThrldRel.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasTmplCtlSWThrldRel.setUnits("percent")


class _TmnxOamLnkMeasTmplCtlSWThrldAbs_Type(Unsigned32):
    """Custom type tmnxOamLnkMeasTmplCtlSWThrldAbs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 100000),
    )


_TmnxOamLnkMeasTmplCtlSWThrldAbs_Type.__name__ = "Unsigned32"
_TmnxOamLnkMeasTmplCtlSWThrldAbs_Object = MibTableColumn
tmnxOamLnkMeasTmplCtlSWThrldAbs = _TmnxOamLnkMeasTmplCtlSWThrldAbs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 1, 1, 20),
    _TmnxOamLnkMeasTmplCtlSWThrldAbs_Type()
)
tmnxOamLnkMeasTmplCtlSWThrldAbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasTmplCtlSWThrldAbs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasTmplCtlSWThrldAbs.setUnits("microseconds")


class _TmnxOamLnkMeasTmplCtlASWMultplir_Type(Unsigned32):
    """Custom type tmnxOamLnkMeasTmplCtlASWMultplir based on Unsigned32"""
    defaultValue = 12

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_TmnxOamLnkMeasTmplCtlASWMultplir_Type.__name__ = "Unsigned32"
_TmnxOamLnkMeasTmplCtlASWMultplir_Object = MibTableColumn
tmnxOamLnkMeasTmplCtlASWMultplir = _TmnxOamLnkMeasTmplCtlASWMultplir_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 1, 1, 21),
    _TmnxOamLnkMeasTmplCtlASWMultplir_Type()
)
tmnxOamLnkMeasTmplCtlASWMultplir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasTmplCtlASWMultplir.setStatus("current")


class _TmnxOamLnkMeasTmplCtlASWIntgrity_Type(Unsigned32):
    """Custom type tmnxOamLnkMeasTmplCtlASWIntgrity based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 100),
    )


_TmnxOamLnkMeasTmplCtlASWIntgrity_Type.__name__ = "Unsigned32"
_TmnxOamLnkMeasTmplCtlASWIntgrity_Object = MibTableColumn
tmnxOamLnkMeasTmplCtlASWIntgrity = _TmnxOamLnkMeasTmplCtlASWIntgrity_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 1, 1, 22),
    _TmnxOamLnkMeasTmplCtlASWIntgrity_Type()
)
tmnxOamLnkMeasTmplCtlASWIntgrity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasTmplCtlASWIntgrity.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasTmplCtlASWIntgrity.setUnits("percent")


class _TmnxOamLnkMeasTmplCtlASWThrldRel_Type(Unsigned32):
    """Custom type tmnxOamLnkMeasTmplCtlASWThrldRel based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 100),
    )


_TmnxOamLnkMeasTmplCtlASWThrldRel_Type.__name__ = "Unsigned32"
_TmnxOamLnkMeasTmplCtlASWThrldRel_Object = MibTableColumn
tmnxOamLnkMeasTmplCtlASWThrldRel = _TmnxOamLnkMeasTmplCtlASWThrldRel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 1, 1, 23),
    _TmnxOamLnkMeasTmplCtlASWThrldRel_Type()
)
tmnxOamLnkMeasTmplCtlASWThrldRel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasTmplCtlASWThrldRel.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasTmplCtlASWThrldRel.setUnits("percent")


class _TmnxOamLnkMeasTmplCtlASWThrldAbs_Type(Unsigned32):
    """Custom type tmnxOamLnkMeasTmplCtlASWThrldAbs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 100000),
    )


_TmnxOamLnkMeasTmplCtlASWThrldAbs_Type.__name__ = "Unsigned32"
_TmnxOamLnkMeasTmplCtlASWThrldAbs_Object = MibTableColumn
tmnxOamLnkMeasTmplCtlASWThrldAbs = _TmnxOamLnkMeasTmplCtlASWThrldAbs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 1, 1, 24),
    _TmnxOamLnkMeasTmplCtlASWThrldAbs_Type()
)
tmnxOamLnkMeasTmplCtlASWThrldAbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasTmplCtlASWThrldAbs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasTmplCtlASWThrldAbs.setUnits("microseconds")


class _TmnxOamLnkMeasTmplCtlAdminState_Type(TmnxEnabledDisabledAdminState):
    """Custom type tmnxOamLnkMeasTmplCtlAdminState based on TmnxEnabledDisabledAdminState"""
    defaultValue = 2


_TmnxOamLnkMeasTmplCtlAdminState_Type.__name__ = "TmnxEnabledDisabledAdminState"
_TmnxOamLnkMeasTmplCtlAdminState_Object = MibTableColumn
tmnxOamLnkMeasTmplCtlAdminState = _TmnxOamLnkMeasTmplCtlAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 1, 1, 25),
    _TmnxOamLnkMeasTmplCtlAdminState_Type()
)
tmnxOamLnkMeasTmplCtlAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasTmplCtlAdminState.setStatus("current")
_TmnxOamLnkMeasIfResTable_Object = MibTable
tmnxOamLnkMeasIfResTable = _TmnxOamLnkMeasIfResTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 2)
)
if mibBuilder.loadTexts:
    tmnxOamLnkMeasIfResTable.setStatus("current")
_TmnxOamLnkMeasIfResEntry_Object = MibTableRow
tmnxOamLnkMeasIfResEntry = _TmnxOamLnkMeasIfResEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 2, 1)
)
tmnxOamLnkMeasIfResEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamLnkMeasIfResEntry.setStatus("current")
_TmnxOamLnkMeasIfResSrcIpAddrTy_Type = InetAddressType
_TmnxOamLnkMeasIfResSrcIpAddrTy_Object = MibTableColumn
tmnxOamLnkMeasIfResSrcIpAddrTy = _TmnxOamLnkMeasIfResSrcIpAddrTy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 2, 1, 1),
    _TmnxOamLnkMeasIfResSrcIpAddrTy_Type()
)
tmnxOamLnkMeasIfResSrcIpAddrTy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasIfResSrcIpAddrTy.setStatus("current")


class _TmnxOamLnkMeasIfResSrcIpAddr_Type(InetAddress):
    """Custom type tmnxOamLnkMeasIfResSrcIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxOamLnkMeasIfResSrcIpAddr_Type.__name__ = "InetAddress"
_TmnxOamLnkMeasIfResSrcIpAddr_Object = MibTableColumn
tmnxOamLnkMeasIfResSrcIpAddr = _TmnxOamLnkMeasIfResSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 2, 1, 2),
    _TmnxOamLnkMeasIfResSrcIpAddr_Type()
)
tmnxOamLnkMeasIfResSrcIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasIfResSrcIpAddr.setStatus("current")
_TmnxOamLnkMeasIfResSrcIpAssigned_Type = TruthValue
_TmnxOamLnkMeasIfResSrcIpAssigned_Object = MibTableColumn
tmnxOamLnkMeasIfResSrcIpAssigned = _TmnxOamLnkMeasIfResSrcIpAssigned_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 2, 1, 3),
    _TmnxOamLnkMeasIfResSrcIpAssigned_Type()
)
tmnxOamLnkMeasIfResSrcIpAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasIfResSrcIpAssigned.setStatus("current")
_TmnxOamLnkMeasIfResDstIpAddrTy_Type = InetAddressType
_TmnxOamLnkMeasIfResDstIpAddrTy_Object = MibTableColumn
tmnxOamLnkMeasIfResDstIpAddrTy = _TmnxOamLnkMeasIfResDstIpAddrTy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 2, 1, 4),
    _TmnxOamLnkMeasIfResDstIpAddrTy_Type()
)
tmnxOamLnkMeasIfResDstIpAddrTy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasIfResDstIpAddrTy.setStatus("current")


class _TmnxOamLnkMeasIfResDstIpAddr_Type(InetAddress):
    """Custom type tmnxOamLnkMeasIfResDstIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxOamLnkMeasIfResDstIpAddr_Type.__name__ = "InetAddress"
_TmnxOamLnkMeasIfResDstIpAddr_Object = MibTableColumn
tmnxOamLnkMeasIfResDstIpAddr = _TmnxOamLnkMeasIfResDstIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 2, 1, 5),
    _TmnxOamLnkMeasIfResDstIpAddr_Type()
)
tmnxOamLnkMeasIfResDstIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasIfResDstIpAddr.setStatus("current")
_TmnxOamLnkMeasIfResDstIpAssigned_Type = TruthValue
_TmnxOamLnkMeasIfResDstIpAssigned_Object = MibTableColumn
tmnxOamLnkMeasIfResDstIpAssigned = _TmnxOamLnkMeasIfResDstIpAssigned_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 2, 1, 6),
    _TmnxOamLnkMeasIfResDstIpAssigned_Type()
)
tmnxOamLnkMeasIfResDstIpAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasIfResDstIpAssigned.setStatus("current")
_TmnxOamLnkMeasIfResOperState_Type = ServiceOperStatus
_TmnxOamLnkMeasIfResOperState_Object = MibTableColumn
tmnxOamLnkMeasIfResOperState = _TmnxOamLnkMeasIfResOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 2, 1, 7),
    _TmnxOamLnkMeasIfResOperState_Type()
)
tmnxOamLnkMeasIfResOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasIfResOperState.setStatus("current")


class _TmnxOamLnkMeasIfResFailureCond_Type(Bits):
    """Custom type tmnxOamLnkMeasIfResFailureCond based on Bits"""
    namedValues = NamedValues(
        *(("noProtocol", 0),
          ("templateAdminDown", 1),
          ("udpPortUnavailable", 2),
          ("internalError", 3))
    )

_TmnxOamLnkMeasIfResFailureCond_Type.__name__ = "Bits"
_TmnxOamLnkMeasIfResFailureCond_Object = MibTableColumn
tmnxOamLnkMeasIfResFailureCond = _TmnxOamLnkMeasIfResFailureCond_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 2, 1, 8),
    _TmnxOamLnkMeasIfResFailureCond_Type()
)
tmnxOamLnkMeasIfResFailureCond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasIfResFailureCond.setStatus("current")


class _TmnxOamLnkMeasIfResDetctbleTxErr_Type(Integer32):
    """Custom type tmnxOamLnkMeasIfResDetctbleTxErr based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("interfaceDown", 2),
          ("unexpectedError", 3),
          ("noRoute", 4),
          ("sourceIpNotLocal", 5),
          ("invalidDestIp", 6),
          ("invalidInterfaceType", 7),
          ("sameSourceIpDestIp", 8))
    )


_TmnxOamLnkMeasIfResDetctbleTxErr_Type.__name__ = "Integer32"
_TmnxOamLnkMeasIfResDetctbleTxErr_Object = MibTableColumn
tmnxOamLnkMeasIfResDetctbleTxErr = _TmnxOamLnkMeasIfResDetctbleTxErr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 2, 1, 9),
    _TmnxOamLnkMeasIfResDetctbleTxErr_Type()
)
tmnxOamLnkMeasIfResDetctbleTxErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasIfResDetctbleTxErr.setStatus("current")
_TmnxOamLnkMeasIfResReporting_Type = TruthValue
_TmnxOamLnkMeasIfResReporting_Object = MibTableColumn
tmnxOamLnkMeasIfResReporting = _TmnxOamLnkMeasIfResReporting_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 2, 1, 10),
    _TmnxOamLnkMeasIfResReporting_Type()
)
tmnxOamLnkMeasIfResReporting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasIfResReporting.setStatus("current")


class _TmnxOamLnkMeasIfResDelayReported_Type(Integer32):
    """Custom type tmnxOamLnkMeasIfResDelayReported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )


_TmnxOamLnkMeasIfResDelayReported_Type.__name__ = "Integer32"
_TmnxOamLnkMeasIfResDelayReported_Object = MibTableColumn
tmnxOamLnkMeasIfResDelayReported = _TmnxOamLnkMeasIfResDelayReported_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 2, 1, 11),
    _TmnxOamLnkMeasIfResDelayReported_Type()
)
tmnxOamLnkMeasIfResDelayReported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasIfResDelayReported.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasIfResDelayReported.setUnits("microseconds")


class _TmnxOamLnkMeasIfResTimestampUTC_Type(DateAndTime):
    """Custom type tmnxOamLnkMeasIfResTimestampUTC based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_TmnxOamLnkMeasIfResTimestampUTC_Type.__name__ = "DateAndTime"
_TmnxOamLnkMeasIfResTimestampUTC_Object = MibTableColumn
tmnxOamLnkMeasIfResTimestampUTC = _TmnxOamLnkMeasIfResTimestampUTC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 2, 1, 12),
    _TmnxOamLnkMeasIfResTimestampUTC_Type()
)
tmnxOamLnkMeasIfResTimestampUTC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasIfResTimestampUTC.setStatus("current")


class _TmnxOamLnkMeasIfResTriggeredBy_Type(Integer32):
    """Custom type tmnxOamLnkMeasIfResTriggeredBy based on Integer32"""
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
        *(("none", 1),
          ("sampleThresholdAbsolute", 2),
          ("sampleThresholdRelative", 3),
          ("aggregateThresholdAbsolute", 4),
          ("aggregateThresholdRelative", 5),
          ("expired", 6))
    )


_TmnxOamLnkMeasIfResTriggeredBy_Type.__name__ = "Integer32"
_TmnxOamLnkMeasIfResTriggeredBy_Object = MibTableColumn
tmnxOamLnkMeasIfResTriggeredBy = _TmnxOamLnkMeasIfResTriggeredBy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 2, 1, 13),
    _TmnxOamLnkMeasIfResTriggeredBy_Type()
)
tmnxOamLnkMeasIfResTriggeredBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasIfResTriggeredBy.setStatus("current")
_TmnxOamLnkMeasIfResNewestASWIdx_Type = Unsigned32
_TmnxOamLnkMeasIfResNewestASWIdx_Object = MibTableColumn
tmnxOamLnkMeasIfResNewestASWIdx = _TmnxOamLnkMeasIfResNewestASWIdx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 2, 1, 14),
    _TmnxOamLnkMeasIfResNewestASWIdx_Type()
)
tmnxOamLnkMeasIfResNewestASWIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasIfResNewestASWIdx.setStatus("current")
_TmnxOamLnkMeasIfResNewestSWIdx_Type = Unsigned32
_TmnxOamLnkMeasIfResNewestSWIdx_Object = MibTableColumn
tmnxOamLnkMeasIfResNewestSWIdx = _TmnxOamLnkMeasIfResNewestSWIdx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 2, 1, 15),
    _TmnxOamLnkMeasIfResNewestSWIdx_Type()
)
tmnxOamLnkMeasIfResNewestSWIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasIfResNewestSWIdx.setStatus("current")
_TmnxOamLnkMeasIfResASWTable_Object = MibTable
tmnxOamLnkMeasIfResASWTable = _TmnxOamLnkMeasIfResASWTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 3)
)
if mibBuilder.loadTexts:
    tmnxOamLnkMeasIfResASWTable.setStatus("current")
_TmnxOamLnkMeasIfResASWEntry_Object = MibTableRow
tmnxOamLnkMeasIfResASWEntry = _TmnxOamLnkMeasIfResASWEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 3, 1)
)
tmnxOamLnkMeasIfResASWEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasIfResASWIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamLnkMeasIfResASWEntry.setStatus("current")


class _TmnxOamLnkMeasIfResASWIndex_Type(Unsigned32):
    """Custom type tmnxOamLnkMeasIfResASWIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxOamLnkMeasIfResASWIndex_Type.__name__ = "Unsigned32"
_TmnxOamLnkMeasIfResASWIndex_Object = MibTableColumn
tmnxOamLnkMeasIfResASWIndex = _TmnxOamLnkMeasIfResASWIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 3, 1, 1),
    _TmnxOamLnkMeasIfResASWIndex_Type()
)
tmnxOamLnkMeasIfResASWIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasIfResASWIndex.setStatus("current")


class _TmnxOamLnkMeasIfResASWEndUTC_Type(DateAndTime):
    """Custom type tmnxOamLnkMeasIfResASWEndUTC based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_TmnxOamLnkMeasIfResASWEndUTC_Type.__name__ = "DateAndTime"
_TmnxOamLnkMeasIfResASWEndUTC_Object = MibTableColumn
tmnxOamLnkMeasIfResASWEndUTC = _TmnxOamLnkMeasIfResASWEndUTC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 3, 1, 2),
    _TmnxOamLnkMeasIfResASWEndUTC_Type()
)
tmnxOamLnkMeasIfResASWEndUTC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasIfResASWEndUTC.setStatus("current")


class _TmnxOamLnkMeasIfResASWState_Type(Integer32):
    """Custom type tmnxOamLnkMeasIfResASWState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("completed", 1),
          ("inProgress", 2),
          ("swReported", 3),
          ("aswReported", 4),
          ("terminated", 5))
    )


_TmnxOamLnkMeasIfResASWState_Type.__name__ = "Integer32"
_TmnxOamLnkMeasIfResASWState_Object = MibTableColumn
tmnxOamLnkMeasIfResASWState = _TmnxOamLnkMeasIfResASWState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 3, 1, 3),
    _TmnxOamLnkMeasIfResASWState_Type()
)
tmnxOamLnkMeasIfResASWState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasIfResASWState.setStatus("current")
_TmnxOamLnkMeasIfResASWWindCount_Type = Unsigned32
_TmnxOamLnkMeasIfResASWWindCount_Object = MibTableColumn
tmnxOamLnkMeasIfResASWWindCount = _TmnxOamLnkMeasIfResASWWindCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 3, 1, 4),
    _TmnxOamLnkMeasIfResASWWindCount_Type()
)
tmnxOamLnkMeasIfResASWWindCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasIfResASWWindCount.setStatus("current")
_TmnxOamLnkMeasIfResASWReportMin_Type = Unsigned32
_TmnxOamLnkMeasIfResASWReportMin_Object = MibTableColumn
tmnxOamLnkMeasIfResASWReportMin = _TmnxOamLnkMeasIfResASWReportMin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 3, 1, 5),
    _TmnxOamLnkMeasIfResASWReportMin_Type()
)
tmnxOamLnkMeasIfResASWReportMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasIfResASWReportMin.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasIfResASWReportMin.setUnits("microseconds")
_TmnxOamLnkMeasIfResASWReportMax_Type = Unsigned32
_TmnxOamLnkMeasIfResASWReportMax_Object = MibTableColumn
tmnxOamLnkMeasIfResASWReportMax = _TmnxOamLnkMeasIfResASWReportMax_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 3, 1, 6),
    _TmnxOamLnkMeasIfResASWReportMax_Type()
)
tmnxOamLnkMeasIfResASWReportMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasIfResASWReportMax.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasIfResASWReportMax.setUnits("microseconds")
_TmnxOamLnkMeasIfResASWReportAvg_Type = Unsigned32
_TmnxOamLnkMeasIfResASWReportAvg_Object = MibTableColumn
tmnxOamLnkMeasIfResASWReportAvg = _TmnxOamLnkMeasIfResASWReportAvg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 3, 1, 7),
    _TmnxOamLnkMeasIfResASWReportAvg_Type()
)
tmnxOamLnkMeasIfResASWReportAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasIfResASWReportAvg.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasIfResASWReportAvg.setUnits("microseconds")
_TmnxOamLnkMeasIfResASWIntegrity_Type = TruthValue
_TmnxOamLnkMeasIfResASWIntegrity_Object = MibTableColumn
tmnxOamLnkMeasIfResASWIntegrity = _TmnxOamLnkMeasIfResASWIntegrity_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 3, 1, 8),
    _TmnxOamLnkMeasIfResASWIntegrity_Type()
)
tmnxOamLnkMeasIfResASWIntegrity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasIfResASWIntegrity.setStatus("current")
_TmnxOamLnkMeasIfResASWResult_Type = Unsigned32
_TmnxOamLnkMeasIfResASWResult_Object = MibTableColumn
tmnxOamLnkMeasIfResASWResult = _TmnxOamLnkMeasIfResASWResult_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 3, 1, 9),
    _TmnxOamLnkMeasIfResASWResult_Type()
)
tmnxOamLnkMeasIfResASWResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasIfResASWResult.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasIfResASWResult.setUnits("microseconds")
_TmnxOamLnkMeasIfResSWTable_Object = MibTable
tmnxOamLnkMeasIfResSWTable = _TmnxOamLnkMeasIfResSWTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 4)
)
if mibBuilder.loadTexts:
    tmnxOamLnkMeasIfResSWTable.setStatus("current")
_TmnxOamLnkMeasIfResSWEntry_Object = MibTableRow
tmnxOamLnkMeasIfResSWEntry = _TmnxOamLnkMeasIfResSWEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 4, 1)
)
tmnxOamLnkMeasIfResSWEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
    (0, "TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasIfResSWIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamLnkMeasIfResSWEntry.setStatus("current")


class _TmnxOamLnkMeasIfResSWIndex_Type(Unsigned32):
    """Custom type tmnxOamLnkMeasIfResSWIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxOamLnkMeasIfResSWIndex_Type.__name__ = "Unsigned32"
_TmnxOamLnkMeasIfResSWIndex_Object = MibTableColumn
tmnxOamLnkMeasIfResSWIndex = _TmnxOamLnkMeasIfResSWIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 4, 1, 1),
    _TmnxOamLnkMeasIfResSWIndex_Type()
)
tmnxOamLnkMeasIfResSWIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasIfResSWIndex.setStatus("current")


class _TmnxOamLnkMeasIfResSWEndUTC_Type(DateAndTime):
    """Custom type tmnxOamLnkMeasIfResSWEndUTC based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_TmnxOamLnkMeasIfResSWEndUTC_Type.__name__ = "DateAndTime"
_TmnxOamLnkMeasIfResSWEndUTC_Object = MibTableColumn
tmnxOamLnkMeasIfResSWEndUTC = _TmnxOamLnkMeasIfResSWEndUTC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 4, 1, 2),
    _TmnxOamLnkMeasIfResSWEndUTC_Type()
)
tmnxOamLnkMeasIfResSWEndUTC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasIfResSWEndUTC.setStatus("current")


class _TmnxOamLnkMeasIfResSWState_Type(Integer32):
    """Custom type tmnxOamLnkMeasIfResSWState based on Integer32"""
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
        *(("completed", 1),
          ("inProgress", 2),
          ("swReported", 3),
          ("terminated", 4))
    )


_TmnxOamLnkMeasIfResSWState_Type.__name__ = "Integer32"
_TmnxOamLnkMeasIfResSWState_Object = MibTableColumn
tmnxOamLnkMeasIfResSWState = _TmnxOamLnkMeasIfResSWState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 4, 1, 3),
    _TmnxOamLnkMeasIfResSWState_Type()
)
tmnxOamLnkMeasIfResSWState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasIfResSWState.setStatus("current")
_TmnxOamLnkMeasIfResSWSent_Type = Unsigned32
_TmnxOamLnkMeasIfResSWSent_Object = MibTableColumn
tmnxOamLnkMeasIfResSWSent = _TmnxOamLnkMeasIfResSWSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 4, 1, 4),
    _TmnxOamLnkMeasIfResSWSent_Type()
)
tmnxOamLnkMeasIfResSWSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasIfResSWSent.setStatus("current")
_TmnxOamLnkMeasIfResSWReceived_Type = Unsigned32
_TmnxOamLnkMeasIfResSWReceived_Object = MibTableColumn
tmnxOamLnkMeasIfResSWReceived = _TmnxOamLnkMeasIfResSWReceived_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 4, 1, 5),
    _TmnxOamLnkMeasIfResSWReceived_Type()
)
tmnxOamLnkMeasIfResSWReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasIfResSWReceived.setStatus("current")
_TmnxOamLnkMeasIfResSWMin_Type = Unsigned32
_TmnxOamLnkMeasIfResSWMin_Object = MibTableColumn
tmnxOamLnkMeasIfResSWMin = _TmnxOamLnkMeasIfResSWMin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 4, 1, 6),
    _TmnxOamLnkMeasIfResSWMin_Type()
)
tmnxOamLnkMeasIfResSWMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasIfResSWMin.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasIfResSWMin.setUnits("microseconds")
_TmnxOamLnkMeasIfResSWMax_Type = Unsigned32
_TmnxOamLnkMeasIfResSWMax_Object = MibTableColumn
tmnxOamLnkMeasIfResSWMax = _TmnxOamLnkMeasIfResSWMax_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 4, 1, 7),
    _TmnxOamLnkMeasIfResSWMax_Type()
)
tmnxOamLnkMeasIfResSWMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasIfResSWMax.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasIfResSWMax.setUnits("microseconds")
_TmnxOamLnkMeasIfResSWAvg_Type = Unsigned32
_TmnxOamLnkMeasIfResSWAvg_Object = MibTableColumn
tmnxOamLnkMeasIfResSWAvg = _TmnxOamLnkMeasIfResSWAvg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 4, 1, 8),
    _TmnxOamLnkMeasIfResSWAvg_Type()
)
tmnxOamLnkMeasIfResSWAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasIfResSWAvg.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasIfResSWAvg.setUnits("microseconds")
_TmnxOamLnkMeasIfResSWErrors_Type = Unsigned32
_TmnxOamLnkMeasIfResSWErrors_Object = MibTableColumn
tmnxOamLnkMeasIfResSWErrors = _TmnxOamLnkMeasIfResSWErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 4, 1, 9),
    _TmnxOamLnkMeasIfResSWErrors_Type()
)
tmnxOamLnkMeasIfResSWErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasIfResSWErrors.setStatus("current")
_TmnxOamLnkMeasIfResSWIntegrity_Type = TruthValue
_TmnxOamLnkMeasIfResSWIntegrity_Object = MibTableColumn
tmnxOamLnkMeasIfResSWIntegrity = _TmnxOamLnkMeasIfResSWIntegrity_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 4, 1, 10),
    _TmnxOamLnkMeasIfResSWIntegrity_Type()
)
tmnxOamLnkMeasIfResSWIntegrity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasIfResSWIntegrity.setStatus("current")
_TmnxOamLnkMeasIfResSWResult_Type = Unsigned32
_TmnxOamLnkMeasIfResSWResult_Object = MibTableColumn
tmnxOamLnkMeasIfResSWResult = _TmnxOamLnkMeasIfResSWResult_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 9, 4, 1, 11),
    _TmnxOamLnkMeasIfResSWResult_Type()
)
tmnxOamLnkMeasIfResSWResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasIfResSWResult.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamLnkMeasIfResSWResult.setUnits("microseconds")
_TmnxOamTestNotifications_ObjectIdentity = ObjectIdentity
tmnxOamTestNotifications = _TmnxOamTestNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 11)
)
_TmnxOamPingNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxOamPingNotifyPrefix = _TmnxOamPingNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 11, 1)
)
_TmnxOamPingNotifications_ObjectIdentity = ObjectIdentity
tmnxOamPingNotifications = _TmnxOamPingNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 11, 1, 0)
)
_TmnxOamTraceRouteNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxOamTraceRouteNotifyPrefix = _TmnxOamTraceRouteNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 11, 2)
)
_TmnxOamTraceRouteNotifications_ObjectIdentity = ObjectIdentity
tmnxOamTraceRouteNotifications = _TmnxOamTraceRouteNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 11, 2, 0)
)
_TmnxOamSaaNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxOamSaaNotifyPrefix = _TmnxOamSaaNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 11, 3)
)
_TmnxOamSaaNotifications_ObjectIdentity = ObjectIdentity
tmnxOamSaaNotifications = _TmnxOamSaaNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 11, 3, 0)
)
_TmnxOamDiagNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxOamDiagNotifyPrefix = _TmnxOamDiagNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 11, 6)
)
_TmnxOamDiagNotifications_ObjectIdentity = ObjectIdentity
tmnxOamDiagNotifications = _TmnxOamDiagNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 11, 6, 0)
)

# Managed Objects groups

tmnxOamMacPingL2MapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 3)
)
tmnxOamMacPingL2MapGroup.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingL2MapRouterID"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingL2MapLabel"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingL2MapProtocol"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingL2MapVCType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingL2MapVCID"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingL2MapDirection"))
)
if mibBuilder.loadTexts:
    tmnxOamMacPingL2MapGroup.setStatus("obsolete")

tmnxOamAtmPingR2r1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 8)
)
tmnxOamAtmPingR2r1Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamAtmPingCtlPortId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamAtmPingCtlVpi"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamAtmPingCtlVci"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamAtmPingCtlLpbkLocation"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamAtmPingCtlSegment"))
)
if mibBuilder.loadTexts:
    tmnxOamAtmPingR2r1Group.setStatus("current")

tmnxOamMacPingV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 14)
)
tmnxOamMacPingV4v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingCtlTargetMacAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingCtlSourceMacAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingCtlSendControl"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingCtlReplyControl"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingCtlTtl"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingCtlRegister"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingCtlFlood"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingCtlForce"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingCtlAge"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingCtlSapPortId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingCtlSapEncapValue"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingCtlFibEntryName"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingHistoryResponse"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingHistoryOneWayTime"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingHistoryStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingHistoryTime"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingHistoryReturnCode"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingHistoryAddressType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingHistorySapId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingHistorySdpId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingHistoryAdminStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingHistoryOperStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingHistoryResponsePlane"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingHistorySize"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingHistoryInOneWayTime"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingHistorySrcAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingHistorySrcAddress"))
)
if mibBuilder.loadTexts:
    tmnxOamMacPingV4v0Group.setStatus("obsolete")

tmnxOamVccvPingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 15)
)
tmnxOamVccvPingGroup.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPingCtlSdpIdVcId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPingCtlReplyMode"))
)
if mibBuilder.loadTexts:
    tmnxOamVccvPingGroup.setStatus("obsolete")

tmnxOamPingGeneralV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 16)
)
tmnxOamPingGeneralV4v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamPingMaxConcurrentTests"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlRowStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlStorageType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlDescr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTestMode"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlAdminStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlOrigSdpId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlRespSdpId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlFcName"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlProfile"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlMtuStartSize"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlMtuEndSize"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlMtuStepSize"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlServiceId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlLocalSdp"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlRemoteSdp"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlSize"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTimeOut"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlProbeCount"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlInterval"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlMaxRows"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTrapGeneration"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTrapProbeFailureFilter"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTrapTestFailureFilter"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlSAA"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlRuns"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlFailures"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlLastRunResult"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlLastChanged"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlVRtrID"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTgtAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTgtAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlSrcAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlSrcAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlDnsName"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsOperStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMinRtt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMaxRtt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsAverageRtt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsRttSumOfSquares"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMtuResponseSize"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsSvcPing"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsProbeResponses"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsSentProbes"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsLastGoodProbe"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsLastRespHeader"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMinTt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMaxTt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsAverageTt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsTtSumOfSquares"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMinInTt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMaxInTt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsAverageInTt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsInTtSumOfSqrs"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsOutJitter"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsInJitter"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsRtJitter"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsProbeTimeouts"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsProbeFailures"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryResponse"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryOneWayTime"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistorySize"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryTime"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryReturnCode"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistAddressType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryVersion"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistSapId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryCpeMacAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryRespSvcId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistorySequence"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryIfIndex"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryDataLen"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryRespPlane"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryReqHdr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryRespHdr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryDnsAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryDnsAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistorySrcAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistorySrcAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryInOneWayTime"))
)
if mibBuilder.loadTexts:
    tmnxOamPingGeneralV4v0Group.setStatus("obsolete")

tmnxOamLspPingV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 17)
)
tmnxOamLspPingV4v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlVRtrID"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlLspName"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlReturnLsp"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlTtl"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlPathName"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlLdpPrefixType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlLdpPrefix"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlLdpPrefixLen"))
)
if mibBuilder.loadTexts:
    tmnxOamLspPingV4v0Group.setStatus("obsolete")

tmnxOamVprnPingV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 19)
)
tmnxOamVprnPingV4v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnPingCtlReplyControl"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnPingCtlTtl"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnPingCtlSrcAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnPingCtlSrcAddress"))
)
if mibBuilder.loadTexts:
    tmnxOamVprnPingV4v0Group.setStatus("current")

tmnxOamMfibPingV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 20)
)
tmnxOamMfibPingV4v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamMfibPingCtlReplyControl"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMfibPingCtlTtl"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMfibPingCtlSrcAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMfibPingCtlSrcAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMfibPingCtlDestAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMfibPingCtlDestAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryRespSvcId"))
)
if mibBuilder.loadTexts:
    tmnxOamMfibPingV4v0Group.setStatus("obsolete")

tmnxOamCpePingV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 21)
)
tmnxOamCpePingV4v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamCpePingCtlSendControl"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamCpePingCtlReplyControl"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamCpePingCtlTtl"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamCpePingCtlSrceMacAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamCpePingCtlSrcAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamCpePingCtlSrcAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryCpeMacAddr"))
)
if mibBuilder.loadTexts:
    tmnxOamCpePingV4v0Group.setStatus("current")

tmnxOamMRInfoV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 22)
)
tmnxOamMRInfoV4v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamMRInfoRespCapabilities"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMRInfoRespMinorVersion"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMRInfoRespMajorVersion"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMRInfoRespNumInterfaces"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMRInfoRespIfMetric"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMRInfoRespIfThreshold"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMRInfoRespIfFlags"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMRInfoRespIfNbrCount"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMRInfoRespIfAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMRInfoRespIfAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMRInfoRespIfNbrAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMRInfoRespIfNbrAddr"))
)
if mibBuilder.loadTexts:
    tmnxOamMRInfoV4v0Group.setStatus("current")

tmnxOamIcmpPingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 23)
)
tmnxOamIcmpPingGroup.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamIcmpPingCtlRapid"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIcmpPingCtlTtl"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIcmpPingCtlDSField"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIcmpPingCtlPattern"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIcmpPingCtlNhAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIcmpPingCtlNhAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIcmpPingCtlEgrIfIndex"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIcmpPingCtlEgrIfName"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIcmpPingCtlBypassRouting"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIcmpPingCtlDoNotFragment"))
)
if mibBuilder.loadTexts:
    tmnxOamIcmpPingGroup.setStatus("current")

tmnxOamPingObsoleteV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 24)
)
tmnxOamPingObsoleteV4v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTargetIpAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistorySrcIpAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingHistorySrcIpAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlLdpIpPrefix"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlLdpIpPrefixLen"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnPingCtlSourceIpAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMfibPingCtlSourceIpAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMfibPingCtlDestIpAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamCpePingCtlSourceIpAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMRInfoRespIfAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMRInfoRespIfNbrAddress"))
)
if mibBuilder.loadTexts:
    tmnxOamPingObsoleteV4v0Group.setStatus("current")

tmnxOamLspPingV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 27)
)
tmnxOamLspPingV5v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlVRtrID"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlLspName"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlReturnLsp"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlTtl"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlPathName"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlLdpPrefixType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlLdpPrefix"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlLdpPrefixLen"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlPathDestType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlPathDest"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlNhIntfName"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlNhAddressType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlNhAddress"))
)
if mibBuilder.loadTexts:
    tmnxOamLspPingV5v0Group.setStatus("obsolete")

tmnxOamVccvPingV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 28)
)
tmnxOamVccvPingV5v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPingCtlSdpIdVcId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPingCtlReplyMode"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPingCtlPwId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPingCtlTtl"))
)
if mibBuilder.loadTexts:
    tmnxOamVccvPingV5v0Group.setStatus("current")

tmnxOamAncpTestV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 29)
)
tmnxOamAncpTestV5v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamAncpTestTarget"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamAncpTestTargetId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamAncpTestcount"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamAncpTestTimeout"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamAncpHistoryAncpString"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamAncpHistoryAccNodeResult"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamAncpHistoryAccNodeCode"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamAncpHistoryAccNodeRspStr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPingCtlTtl"))
)
if mibBuilder.loadTexts:
    tmnxOamAncpTestV5v0Group.setStatus("current")

tmnxOamMfibPingV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 31)
)
tmnxOamMfibPingV6v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamMfibPingCtlReplyControl"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMfibPingCtlTtl"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMfibPingCtlSrcAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMfibPingCtlSrcAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMfibPingCtlDestAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMfibPingCtlDestAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryRespSvcId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMfibPingCtlDestMacAddr"))
)
if mibBuilder.loadTexts:
    tmnxOamMfibPingV6v0Group.setStatus("current")

tmnxOamPingGeneralV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 32)
)
tmnxOamPingGeneralV6v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamPingMaxConcurrentTests"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlRowStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlStorageType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlDescr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTestMode"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlAdminStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlOrigSdpId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlRespSdpId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlFcName"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlProfile"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlMtuStartSize"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlMtuEndSize"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlMtuStepSize"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlServiceId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlLocalSdp"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlRemoteSdp"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlSize"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTimeOut"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlProbeCount"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlInterval"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTrapGeneration"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTrapProbeFailureFilter"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTrapTestFailureFilter"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlSAA"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlRuns"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlFailures"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlLastRunResult"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlLastChanged"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlVRtrID"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTgtAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTgtAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlSrcAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlSrcAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlDnsName"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsOperStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMinRtt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMaxRtt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsAverageRtt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsRttSumOfSquares"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMtuResponseSize"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsSvcPing"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsProbeResponses"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsSentProbes"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsLastGoodProbe"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsLastRespHeader"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMinTt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMaxTt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsAverageTt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsTtSumOfSquares"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMinInTt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMaxInTt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsAverageInTt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsInTtSumOfSqrs"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsOutJitter"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsInJitter"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsRtJitter"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsProbeTimeouts"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsProbeFailures"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryResponse"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryOneWayTime"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistorySize"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryTime"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryReturnCode"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistAddressType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryVersion"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistSapId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryCpeMacAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryRespSvcId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistorySequence"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryIfIndex"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryDataLen"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryRespPlane"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryReqHdr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryRespHdr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryDnsAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryDnsAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistorySrcAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistorySrcAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryInOneWayTime"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlDNSRecord"))
)
if mibBuilder.loadTexts:
    tmnxOamPingGeneralV6v0Group.setStatus("obsolete")

tmnxOamP2mpLspPingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 33)
)
tmnxOamP2mpLspPingGroup.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamP2mpLspPingCtlLspName"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamP2mpLspPingCtlInstName"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamP2mpLspPingCtlTtl"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamP2mpLspPingCtlIpRowStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamP2mpLspPingCtlIpAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamP2mpLspPingCtlIpAddr"))
)
if mibBuilder.loadTexts:
    tmnxOamP2mpLspPingGroup.setStatus("current")

tmnxOamLspPingV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 34)
)
tmnxOamLspPingV6v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlLspName"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlTtl"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlPathName"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlLdpPrefixType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlLdpPrefix"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlLdpPrefixLen"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlPathDestType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlPathDest"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlNhIntfName"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlNhAddressType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlNhAddress"))
)
if mibBuilder.loadTexts:
    tmnxOamLspPingV6v0Group.setStatus("obsolete")

tmnxOamPingGeneralV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 35)
)
tmnxOamPingGeneralV7v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamPingMaxConcurrentTests"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlRowStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlStorageType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlDescr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTestMode"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlAdminStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlOrigSdpId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlRespSdpId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlFcName"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlProfile"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlMtuStartSize"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlMtuEndSize"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlMtuStepSize"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlServiceId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlLocalSdp"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlRemoteSdp"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlSize"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTimeOut"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlProbeCount"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlInterval"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTrapGeneration"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTrapProbeFailureFilter"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTrapTestFailureFilter"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlSAA"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlRuns"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlFailures"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlLastRunResult"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlLastChanged"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlVRtrID"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTgtAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTgtAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlSrcAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlSrcAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlDnsName"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsOperStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMinRtt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMaxRtt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsAverageRtt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsRttSumOfSquares"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMtuResponseSize"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsSvcPing"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsProbeResponses"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsSentProbes"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsLastGoodProbe"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsLastRespHeader"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMinTt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMaxTt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsAverageTt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsTtSumOfSquares"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMinInTt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMaxInTt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsAverageInTt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsInTtSumOfSqrs"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsOutJitter"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsInJitter"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsRtJitter"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsProbeTimeouts"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsProbeFailures"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryResponse"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryOneWayTime"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistorySize"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryTime"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryReturnCode"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistAddressType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryVersion"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistSapId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryCpeMacAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryRespSvcId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistorySequence"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryIfIndex"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryDataLen"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryRespPlane"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryReqHdr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryRespHdr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryDnsAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryDnsAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistorySrcAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistorySrcAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryInOneWayTime"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlDNSRecord"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsRttOFSumSquares"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsRttHCSumSquares"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsTtOFSumSquares"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsTtHCSumSquares"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsInTtOFSumSqrs"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsInTtHCSumSqrs"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsTestRunResult"))
)
if mibBuilder.loadTexts:
    tmnxOamPingGeneralV7v0Group.setStatus("obsolete")

tmnxOamPingObsoleteV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 37)
)
tmnxOamPingObsoleteV6v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlReturnLsp"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlVRtrID"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlMaxRows"))
)
if mibBuilder.loadTexts:
    tmnxOamPingObsoleteV6v0Group.setStatus("current")

tmnxOamPingObsoleteV6v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 38)
)
tmnxOamPingObsoleteV6v1Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingL2MapRouterID"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingL2MapLabel"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingL2MapProtocol"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingL2MapVCType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingL2MapVCID"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingL2MapDirection"))
)
if mibBuilder.loadTexts:
    tmnxOamPingObsoleteV6v1Group.setStatus("current")

tmnxOamEthCfmPingV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 39)
)
tmnxOamEthCfmPingV8v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamEthCfmPingCtlTgtMacAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamEthCfmPingCtlSrcMdIndex"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamEthCfmPingCtlSrcMaIndex"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamEthCfmPingCtlSrcMepId"))
)
if mibBuilder.loadTexts:
    tmnxOamEthCfmPingV8v0Group.setStatus("current")

tmnxOamP2mpLspPingV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 40)
)
tmnxOamP2mpLspPingV8v0Group.setObjects(
    ("TIMETRA-OAM-TEST-MIB", "tmnxOamP2mpLspPingCtlP2MPId")
)
if mibBuilder.loadTexts:
    tmnxOamP2mpLspPingV8v0Group.setStatus("current")

tmnxOamPingGeneralV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 41)
)
tmnxOamPingGeneralV8v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamPingMaxConcurrentTests"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlRowStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlStorageType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlDescr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTestMode"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlAdminStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlOrigSdpId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlRespSdpId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlFcName"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlProfile"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlMtuStartSize"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlMtuEndSize"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlMtuStepSize"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlServiceId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlLocalSdp"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlRemoteSdp"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlSize"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTimeOut"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlProbeCount"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlInterval"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTrapGeneration"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTrapProbeFailureFilter"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTrapTestFailureFilter"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlSAA"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlRuns"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlFailures"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlLastRunResult"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlLastChanged"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlVRtrID"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTgtAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTgtAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlSrcAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlSrcAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlDnsName"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsOperStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMinRtt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMaxRtt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsAverageRtt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsRttSumOfSquares"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMtuResponseSize"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsSvcPing"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsProbeResponses"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsSentProbes"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsLastGoodProbe"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMinTt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMaxTt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsAverageTt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsTtSumOfSquares"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMinInTt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMaxInTt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsAverageInTt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsInTtSumOfSqrs"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsOutJitter"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsInJitter"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsRtJitter"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsProbeTimeouts"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsProbeFailures"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryResponse"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryOneWayTime"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistorySize"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryTime"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryReturnCode"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistAddressType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryVersion"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistSapId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryCpeMacAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryRespSvcId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistorySequence"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryIfIndex"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryDataLen"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryRespPlane"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryReqHdr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryRespHdr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryDnsAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryDnsAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistorySrcAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistorySrcAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryInOneWayTime"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryLspName"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistNextHopAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistNextHopAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlDNSRecord"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsRttOFSumSquares"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsRttHCSumSquares"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsTtOFSumSquares"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsTtHCSumSquares"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsInTtOFSumSqrs"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsInTtHCSumSqrs"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsTestRunResult"))
)
if mibBuilder.loadTexts:
    tmnxOamPingGeneralV8v0Group.setStatus("obsolete")

tmnxOamPingObsoleteV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 42)
)
tmnxOamPingObsoleteV8v0Group.setObjects(
    ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsLastRespHeader")
)
if mibBuilder.loadTexts:
    tmnxOamPingObsoleteV8v0Group.setStatus("current")

tmnxOamVccvPingV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 43)
)
tmnxOamVccvPingV9v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPingCtlSpokeSdpId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPingCtlSaiiGlobalId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPingCtlSaiiPrefix"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPingCtlSaiiAcId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPingCtlTaiiGlobalId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPingCtlTaiiPrefix"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPingCtlTaiiAcId"))
)
if mibBuilder.loadTexts:
    tmnxOamVccvPingV9v0Group.setStatus("current")

tmnxOamPingCtlV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 44)
)
tmnxOamPingCtlV10v0Group.setObjects(
    ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlIntervalUnits")
)
if mibBuilder.loadTexts:
    tmnxOamPingCtlV10v0Group.setStatus("current")

tmnxOamMobilePingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 45)
)
tmnxOamMobilePingGroup.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamMobGtpPingRefPointType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMobGtpPingVRtrId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMobGtpPingPort"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMobGtpPingGateway"))
)
if mibBuilder.loadTexts:
    tmnxOamMobilePingGroup.setStatus("obsolete")

tmnxOamPingObsoleteV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 46)
)
tmnxOamPingObsoleteV10v0Group.setObjects(
    ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryReqHdr")
)
if mibBuilder.loadTexts:
    tmnxOamPingObsoleteV10v0Group.setStatus("current")

tmnxOamPingGeneralV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 47)
)
tmnxOamPingGeneralV10v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamPingMaxConcurrentTests"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlRowStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTestMode"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlAdminStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlOrigSdpId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlRespSdpId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlFcName"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlProfile"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlMtuStartSize"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlMtuEndSize"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlMtuStepSize"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlServiceId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlLocalSdp"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlRemoteSdp"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlSize"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTimeOut"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlProbeCount"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlInterval"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTrapGeneration"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTrapProbeFailureFilter"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTrapTestFailureFilter"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlSAA"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlRuns"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlFailures"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlLastRunResult"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlLastChanged"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlVRtrID"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTgtAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTgtAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlSrcAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlSrcAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlDnsName"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsOperStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMinRtt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMaxRtt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsAverageRtt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsRttSumOfSquares"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMtuResponseSize"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsSvcPing"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsProbeResponses"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsSentProbes"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsLastGoodProbe"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMinTt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMaxTt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsAverageTt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsTtSumOfSquares"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMinInTt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMaxInTt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsAverageInTt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsInTtSumOfSqrs"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsOutJitter"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsInJitter"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsRtJitter"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsProbeTimeouts"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsProbeFailures"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryResponse"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryOneWayTime"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistorySize"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryTime"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryReturnCode"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistAddressType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryVersion"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistSapId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryCpeMacAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryRespSvcId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistorySequence"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryIfIndex"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryDataLen"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryRespPlane"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryRespHdr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryDnsAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryDnsAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistorySrcAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistorySrcAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryInOneWayTime"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryLspName"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistNextHopAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistNextHopAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlDNSRecord"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsRttOFSumSquares"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsRttHCSumSquares"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsTtOFSumSquares"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsTtHCSumSquares"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsInTtOFSumSqrs"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsInTtHCSumSqrs"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsTestRunResult"))
)
if mibBuilder.loadTexts:
    tmnxOamPingGeneralV10v0Group.setStatus("current")

tmnxOamP2mpLspPingV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 48)
)
tmnxOamP2mpLspPingV10v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamP2mpLspPingCtlSrcAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamP2mpLspPingCtlSrcAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamP2mpLspPingCtlGrpAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamP2mpLspPingCtlGrpAddr"))
)
if mibBuilder.loadTexts:
    tmnxOamP2mpLspPingV10v0Group.setStatus("current")

tmnxOamPingObsoleteV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 49)
)
tmnxOamPingObsoleteV11v0Group.setObjects(
    ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingCtlFibEntryName")
)
if mibBuilder.loadTexts:
    tmnxOamPingObsoleteV11v0Group.setStatus("current")

tmnxOamMacPingCtlV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 50)
)
tmnxOamMacPingCtlV11v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingCtlTargetMacAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingCtlSourceMacAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingCtlSendControl"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingCtlReplyControl"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingCtlTtl"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingCtlRegister"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingCtlFlood"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingCtlForce"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingCtlAge"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingCtlSapPortId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingCtlSapEncapValue"))
)
if mibBuilder.loadTexts:
    tmnxOamMacPingCtlV11v0Group.setStatus("current")

tmnxOamMacPingHistoryV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 51)
)
tmnxOamMacPingHistoryV11v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingHistoryResponse"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingHistoryOneWayTime"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingHistoryStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingHistoryTime"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingHistoryReturnCode"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingHistoryAddressType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingHistorySapId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingHistorySdpId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingHistoryAdminStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingHistoryOperStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingHistoryResponsePlane"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingHistorySize"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingHistoryInOneWayTime"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingHistorySrcAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingHistorySrcAddress"))
)
if mibBuilder.loadTexts:
    tmnxOamMacPingHistoryV11v0Group.setStatus("current")

tmnxOamLspPingV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 52)
)
tmnxOamLspPingV11v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlAssocChannel"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlForce"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlLdpPrefix"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlLdpPrefixLen"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlLdpPrefixType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlLspName"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlMplsTpGlobalId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlMplsTpNodeId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlMplsTpPathType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlNhAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlNhAddressType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlNhIntfName"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlPathDest"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlPathDestType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlPathName"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlTestSubMode"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlTtl"))
)
if mibBuilder.loadTexts:
    tmnxOamLspPingV11v0Group.setStatus("current")

tmnxOamVccvPingV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 53)
)
tmnxOamVccvPingV11v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPingCtlAssocChannel"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPingCtlMplsTpGlobalId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPingCtlMplsTpNodeId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPingCtlTestSubMode"))
)
if mibBuilder.loadTexts:
    tmnxOamVccvPingV11v0Group.setStatus("current")

tmnxOamPingV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 54)
)
tmnxOamPingV11v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryRtrnSubcode"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistorySdpBindId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistorySrcGlobalId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistorySrcNodeId"))
)
if mibBuilder.loadTexts:
    tmnxOamPingV11v0Group.setStatus("current")

tmnxOamPingV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 55)
)
tmnxOamPingV12v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPgTgFec128CtlDstAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPgTgFec128CtlDstAddrT"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPgTgFec128CtlPwId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPgTgFec128CtlPwType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPgTgFec128CtlSrcAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPgTgFec128CtlSrcAddrT"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPgTgStaticCtlAgi"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPgTgStaticCtlSaiiAcId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPgTgStaticCtlSaiiGlbl"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPgTgStaticCtlSaiiNode"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPgTgStaticCtlTaiiAcId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPgTgStaticCtlTaiiGlbl"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPgTgStaticCtlTaiiNode"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPingCtlSwitTgtFecType"))
)
if mibBuilder.loadTexts:
    tmnxOamPingV12v0Group.setStatus("current")

tmnxOamPingV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 56)
)
tmnxOamPingV13v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamBfdOnLspBootStrRetryCount"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBfdOnLspLspName"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBfdOnLspPathState"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBfdOnLspPingReturnCode"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBfdOnLspPingReturnSubcode"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBfdOnLspPingRxCount"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBfdOnLspPingTxCount"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBfdOnLspPingTxInterval"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBfdOnLspRemoteAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBfdOnLspRemoteAddressType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBfdOnLspRemoteBfdDiscrim"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryNetworkIfName"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsOutOfOrder"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVxlanPingCtlEndSysMacAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVxlanPingCtlIFlag"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVxlanPingCtlInIpDstAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVxlanPingCtlInIpDstAddrT"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVxlanPingCtlInIpSrcAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVxlanPingCtlInIpSrcAddrT"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVxlanPingCtlInL2DestMac"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVxlanPingCtlNetworkId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVxlanPingCtlOutIpTtl"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVxlanPingCtlOutSrcUdpPt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVxlanPingCtlReflectPad"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVxlanPingCtlReplyMode"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVxlanPingCtlTestId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVxlanPingHistNetworkId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVxlanPingHistOutIpTtl"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVxlanPingHistReturnCode"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVxlanPingHistRtrnSubCode"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVxlanPingHistValidationRC"))
)
if mibBuilder.loadTexts:
    tmnxOamPingV13v0Group.setStatus("current")

tmnxOamPingObsoleteV14v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 57)
)
tmnxOamPingObsoleteV14v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlDescr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlStorageType"))
)
if mibBuilder.loadTexts:
    tmnxOamPingObsoleteV14v0Group.setStatus("current")

tmnxOamPingV14v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 58)
)
tmnxOamPingV14v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamVxlanPingResOutSrcAddrTyp"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVxlanPingResOutSrcAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamP2mpLspPingCtlOptionalTLV"))
)
if mibBuilder.loadTexts:
    tmnxOamPingV14v0Group.setStatus("current")

tmnxOamPingV15v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 59)
)
tmnxOamPingV15v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamBfdOnLspFecType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBfdOnLspOperState"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBfdOnLspPrefix"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBfdOnLspPrefixLen"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBfdOnLspPrefixType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBfdOnLspSessBootstrInProg"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBfdOnLspSessBootstrNoPV"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBfdOnLspSessBootstrSendPV"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBfdOnLspSourceAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBfdOnLspSourceAddressType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamEthCfmPingCtlRemoteMepId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlIgpInstance"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlSubscriberName"))
)
if mibBuilder.loadTexts:
    tmnxOamPingV15v0Group.setStatus("current")

tmnxOamPingV16v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 60)
)
tmnxOamPingV16v0Group.setObjects(
    ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlRouterInstanceName")
)
if mibBuilder.loadTexts:
    tmnxOamPingV16v0Group.setStatus("current")

tmnxOamPingObsoletedV16v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 61)
)
tmnxOamPingObsoletedV16v0Group.setObjects(
    ("TIMETRA-OAM-TEST-MIB", "tmnxOamMobGtpPingVRtrId")
)
if mibBuilder.loadTexts:
    tmnxOamPingObsoletedV16v0Group.setStatus("current")

tmnxOamMobilePingV16v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 62)
)
tmnxOamMobilePingV16v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamMobGtpPingRefPointType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMobGtpPingPort"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMobGtpPingGateway"))
)
if mibBuilder.loadTexts:
    tmnxOamMobilePingV16v0Group.setStatus("current")

tmnxOamPingV19v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 63, 1)
)
tmnxOamPingV19v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlSrPlcyColor"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlSrPlcyEndPtAddT"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlSrPlcyEndPtAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlSrPlcySegList"))
)
if mibBuilder.loadTexts:
    tmnxOamPingV19v0Group.setStatus("current")

tmnxOamBierPingV20v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 64, 1)
)
tmnxOamBierPingV20v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamBierPingBfrPfxCtlAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBierPingBfrPfxCtlAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBierPingBfrPfxCtlRowState"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBierPingCtlBfrId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBierPingCtlBfrIdEnd"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBierPingCtlBfrIdStart"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBierPingCtlSubDomain"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBierPingCtlTtl"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBierPingHistoryBfrId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBierPingHistoryBfrPfx"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBierPingHistoryBfrPfxType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBierPingHistoryReturnCode"))
)
if mibBuilder.loadTexts:
    tmnxOamBierPingV20v0Group.setStatus("current")

tmnxOamIfPingV20v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 3, 1)
)
tmnxOamIfPingV20v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamIfPingIfAdminState"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIfPingIfCtlDot1p"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIfPingIfCtlDscp"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIfPingIfCtlFailThrld"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIfPingIfCtlInterval"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIfPingIfCtlReactInt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIfPingIfCtlReactFailThr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIfPingIfCtlReactThrld"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIfPingIfCtlReactTimeout"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIfPingIfCtlSize"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIfPingIfCtlTimeout"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIfPingIfCtlTtl"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIfPingIfDestAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIfPingIfDestAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIfPingIfFailThrldCnt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIfPingIfLastChanged"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIfPingIfPassThrldCnt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIfPingIfRowStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIfPingIfTemplate"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIfPingIfCurrentInterval"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIfPingIfCurrentState"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIfPingTmplCtlDescription"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIfPingTmplCtlDot1p"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIfPingTmplCtlDscp"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIfPingTmplCtlFailThrld"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIfPingTmplCtlInterval"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIfPingTmplCtlLastMgmtChg"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIfPingTmplCtlReactInt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIfPingTmplCtlReactFailThr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIfPingTmplCtlReactThrld"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIfPingTmplCtlReactTimeout"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIfPingTmplCtlRowStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIfPingTmplCtlSize"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIfPingTmplCtlSync"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIfPingTmplCtlTimeout"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIfPingTmplCtlTtl"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSysBgIcmpIfCtlSessCount"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSysBgIcmpIfCtlSessLimit"))
)
if mibBuilder.loadTexts:
    tmnxOamIfPingV20v0Group.setStatus("current")

tmnxOamLnkMeasV21v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 4, 1)
)
tmnxOamLnkMeasV21v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasTmplCtlAdminState"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasTmplCtlASWIntgrity"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasTmplCtlASWMultplir"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasTmplCtlASWThrldAbs"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasTmplCtlASWThrldRel"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasTmplCtlDelayMeasTy"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasTmplCtlDescription"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasTmplCtlDscpEgrRmrk"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasTmplCtlDscpName"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasTmplCtlDstUdpPort"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasTmplCtlFC"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasTmplCtlInterval"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasTmplCtlIpv6UdpZero"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasTmplCtlLastMgmtChg"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasTmplCtlLastRepHold"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasTmplCtlProfile"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasTmplCtlRowStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasTmplCtlSWIntegrity"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasTmplCtlSWMultplir"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasTmplCtlSWThrldAbs"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasTmplCtlSWThrldRel"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasTmplCtlTwlTimeLive"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasTmplCtlTwlTmStpFmt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasTmplCtlUnidirMeasT"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasIfResDelayReported"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasIfResDetctbleTxErr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasIfResDstIpAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasIfResDstIpAddrTy"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasIfResDstIpAssigned"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasIfResFailureCond"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasIfResNewestASWIdx"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasIfResNewestSWIdx"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasIfResOperState"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasIfResReporting"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasIfResSrcIpAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasIfResSrcIpAddrTy"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasIfResSrcIpAssigned"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasIfResTimestampUTC"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasIfResTriggeredBy"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasIfResASWEndUTC"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasIfResASWIntegrity"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasIfResASWReportAvg"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasIfResASWReportMax"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasIfResASWReportMin"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasIfResASWResult"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasIfResASWState"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasIfResASWWindCount"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasIfResSWAvg"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasIfResSWEndUTC"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasIfResSWErrors"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasIfResSWIntegrity"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasIfResSWMax"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasIfResSWMin"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasIfResSWReceived"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasIfResSWResult"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasIfResSWSent"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasIfResSWState"))
)
if mibBuilder.loadTexts:
    tmnxOamLnkMeasV21v0Group.setStatus("current")

tmnxOamMacTrV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 2, 10)
)
tmnxOamMacTrV3v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamMacTrCtlTargetMacAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacTrCtlSourceMacAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacTrCtlSendControl"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacTrCtlReplyControl"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacTrL2MapRouterID"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacTrL2MapLabel"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacTrL2MapProtocol"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacTrL2MapVCType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacTrL2MapVCID"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacTrL2MapDirection"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacTrL2MapSdpId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacTrL2MapSapName"))
)
if mibBuilder.loadTexts:
    tmnxOamMacTrV3v0Group.setStatus("current")

tmnxOamTrObsoleteV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 2, 11)
)
tmnxOamTrObsoleteV3v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsTestAttempts"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsTestSuccesses"))
)
if mibBuilder.loadTexts:
    tmnxOamTrObsoleteV3v0Group.setStatus("current")

tmnxOamTrGeneralV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 2, 12)
)
tmnxOamTrGeneralV4v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamTrMaxConcurrentRequests"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlRowStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlStorageType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlDescr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestMode"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlAdminStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlFcName"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlProfile"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlServiceId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlDataSize"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTimeOut"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlProbesPerHop"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlMaxTtl"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlInitialTtl"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlDSField"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlMaxFailures"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlInterval"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlMaxRows"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTrapGeneration"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlCreateHopsEntries"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlSAA"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlRuns"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlFailures"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlLastRunResult"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlLastChanged"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlVRtrID"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTgtAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTgtAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlSrcAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlSrcAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlWaitMilliSec"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsOperStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsCurHopCount"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsCurProbeCount"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsLastGoodPath"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsTgtAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsTgtAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryResponse"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryOneWayTime"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryLastRC"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryTime"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryResponsePlane"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryAddressType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistorySapId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryVersion"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryRouterID"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryIfIndex"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryDataLen"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistorySize"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryInOneWayTime"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryAddress"))
)
if mibBuilder.loadTexts:
    tmnxOamTrGeneralV4v0Group.setStatus("obsolete")

tmnxOamTrHopsV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 2, 13)
)
tmnxOamTrHopsV4v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsMinRtt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsMaxRtt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsAverageRtt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsRttSumOfSquares"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsMinTt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsMaxTt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsAverageTt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsTtSumOfSquares"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsSentProbes"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsProbeResponses"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsLastGoodProbe"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsMinInTt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsMaxInTt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsAverageInTt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsInTtSumOfSqrs"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsOutJitter"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsInJitter"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsRtJitter"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsProbeTimeouts"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsProbeFailures"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsTgtAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsTgtAddress"))
)
if mibBuilder.loadTexts:
    tmnxOamTrHopsV4v0Group.setStatus("current")

tmnxOamLspTrV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 2, 14)
)
tmnxOamLspTrV4v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrCtlVRtrID"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrCtlLspName"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrCtlPathName"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrCtlLdpPrefixType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrCtlLdpPrefix"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrCtlLdpPrefixLen"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrMapAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrMapDSIPv4Addr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrMapDSIfAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrMapMTU"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrMapDSIndex"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrDSLabelLabel"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrDSLabelProtocol"))
)
if mibBuilder.loadTexts:
    tmnxOamLspTrV4v0Group.setStatus("obsolete")

tmnxOamVprnTrV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 2, 15)
)
tmnxOamVprnTrV4v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrCtlReplyControl"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrCtlSrcAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrCtlSrcAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrL3MapRouterID"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrL3MapRteVprnLabel"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrL3MapRteMetrics"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrL3MapRteLastUp"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrL3MapRteOwner"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrL3MapRtePref"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrL3MapRteDist"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrL3MapNumNextHops"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrL3MapNumRteTargets"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrL3MapDestAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrL3MapDestAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrL3MapDestMaskLen"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrNextHopRtrID"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrNextHopType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrNextHopTunnelID"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrNextHopTunnelType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrNextHopIfIndex"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrRouteTarget"))
)
if mibBuilder.loadTexts:
    tmnxOamVprnTrV4v0Group.setStatus("obsolete")

tmnxOamMcastTrV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 2, 16)
)
tmnxOamMcastTrV4v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrCtlVRtrID"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrCtlHops"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrQueryId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrCtlSrcAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrCtlSrcAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrCtlDestAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrCtlDestAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrCtlRespAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrCtlRespAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrCtlGrpAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrCtlGrpAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrRespQueryArrivalTime"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrRespInPktCount"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrRespOutPktCount"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrRespSGPktCount"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrRespRtgProtocol"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrRespFwdTtl"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrRespMBZBit"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrRespSrcBit"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrRespSrcMask"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrRespFwdCode"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrRespInIfAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrRespInIfAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrRespOutIfAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrRespOutIfAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrRespPhRtrAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrRespPhRtrAddress"))
)
if mibBuilder.loadTexts:
    tmnxOamMcastTrV4v0Group.setStatus("current")

tmnxOamTrObsoleteV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 2, 17)
)
tmnxOamTrObsoleteV4v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTargetIpAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsIpTgtAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryIpAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsIpTgtAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrCtlLdpIpPrefix"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrCtlLdpIpPrefixLen"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrCtlSourceIpAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrL3MapRteDestAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrL3MapRteDestMask"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrCtlSrcIpAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrCtlDestIpAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrCtlRespIpAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrCtlGrpIpAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrRespPrevHopRtrAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrRespInIfAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrRespOutIfAddr"))
)
if mibBuilder.loadTexts:
    tmnxOamTrObsoleteV4v0Group.setStatus("current")

tmnxOamLspTrV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 2, 19)
)
tmnxOamLspTrV5v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrCtlVRtrID"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrCtlLspName"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrCtlPathName"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrCtlLdpPrefixType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrCtlLdpPrefix"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrCtlLdpPrefixLen"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrCtlPathDestType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrCtlPathDest"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrCtlNhIntfName"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrCtlNhAddressType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrCtlNhAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrMapAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrMapDSIPv4Addr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrMapDSIfAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrMapMTU"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrDSLabelLabel"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrDSLabelProtocol"))
)
if mibBuilder.loadTexts:
    tmnxOamLspTrV5v0Group.setStatus("obsolete")

tmnxOamTrObsoleteV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 2, 20)
)
tmnxOamTrObsoleteV5v0Group.setObjects(
    ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrMapDSIndex")
)
if mibBuilder.loadTexts:
    tmnxOamTrObsoleteV5v0Group.setStatus("current")

tmnxOamTrGeneralV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 2, 21)
)
tmnxOamTrGeneralV5v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamTrMaxConcurrentRequests"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlRowStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlStorageType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlDescr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestMode"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlAdminStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlFcName"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlProfile"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlServiceId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlDataSize"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTimeOut"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlProbesPerHop"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlMaxTtl"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlInitialTtl"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlDSField"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlMaxFailures"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlInterval"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlMaxRows"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTrapGeneration"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlCreateHopsEntries"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlSAA"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlRuns"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlFailures"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlLastRunResult"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlLastChanged"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlVRtrID"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTgtAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTgtAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlSrcAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlSrcAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlWaitMilliSec"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsOperStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsCurHopCount"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsCurProbeCount"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsLastGoodPath"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsTgtAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsTgtAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryResponse"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryOneWayTime"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryLastRC"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryTime"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryResponsePlane"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryAddressType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistorySapId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryVersion"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryRouterID"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryIfIndex"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryDataLen"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistorySize"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryInOneWayTime"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceFecDiscoveryState"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceFecDisStatusBits"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceFecDisPaths"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceFecFailedHops"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceFecLastDisEnd"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceFecFailedProbes"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceFecProbeState"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtracePathRemAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtracePathRemoteAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtracePathEgrNhAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtracePathEgrNhAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtracePathDisTtl"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtracePathLastDisTime"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtracePathLastRc"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtracePathProbeState"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceCtlLdpPrefixType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceCtlLdpPrefix"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceCtlLdpPrefixLen"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceCtlMaxPath"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceResultsDisPaths"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceResultsFailedHops"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceResultsDisState"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceResultsDisStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceUpStreamHopIndex"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceHopAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceHopAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceHopDstAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceHopDstAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceHopEgrNhAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceHopEgrNhAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceHopDisTtl"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceHopLastRc"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceHopDiscoveryState"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceHopDiscoveryTime"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoRowStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoLastChanged"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoStorageType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoAdminState"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoFcName"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoProfile"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoDiscIntvl"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoMaxPath"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoTrMaxTtl"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoTrTimeOut"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoTrMaxFailures"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoPolicy1"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoPolicy2"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoPolicy3"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoPolicy4"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoPolicy5"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoProbeIntvl"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoPrTimeOut"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoPrMaxFailures"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoDiscoveryState"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoTotalFecs"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoDisFecs"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoLastDisStart"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoLastDisEnd"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoLastDisDur"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtracePathProbeState"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtracePathProbeTmOutCnt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceMaxConRequests"))
)
if mibBuilder.loadTexts:
    tmnxOamTrGeneralV5v0Group.setStatus("obsolete")

tmnxOamVccvTrV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 2, 23)
)
tmnxOamVccvTrV6v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrCtlSdpIdVcId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrCtlReplyMode"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrNextPwID"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrNextPwType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrNextSenderAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrNextSenderAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrNextRemoteAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrNextRemoteAddr"))
)
if mibBuilder.loadTexts:
    tmnxOamVccvTrV6v0Group.setStatus("current")

tmnxOamVprnTrObsoleteV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 2, 24)
)
tmnxOamVprnTrObsoleteV6v0Group.setObjects(
    ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrNextHopRtrID")
)
if mibBuilder.loadTexts:
    tmnxOamVprnTrObsoleteV6v0Group.setStatus("current")

tmnxOamVprnTrV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 2, 25)
)
tmnxOamVprnTrV6v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrCtlReplyControl"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrCtlSrcAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrCtlSrcAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrL3MapRouterID"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrL3MapRteVprnLabel"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrL3MapRteMetrics"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrL3MapRteLastUp"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrL3MapRteOwner"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrL3MapRtePref"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrL3MapRteDist"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrL3MapNumNextHops"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrL3MapNumRteTargets"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrL3MapDestAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrL3MapDestAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrL3MapDestMaskLen"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrNextHopType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrNextHopTunnelID"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrNextHopTunnelType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrNextHopIfIndex"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrNextHopAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrNextHopAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrRouteTarget"))
)
if mibBuilder.loadTexts:
    tmnxOamVprnTrV6v0Group.setStatus("current")

tmnxOamP2mpLspTraceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 2, 26)
)
tmnxOamP2mpLspTraceGroup.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamP2mpLspTrCtlInstName"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamP2mpLspTrCtlLeafIpAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamP2mpLspTrCtlLeafIpAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamP2mpLspTrCtlLspName"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamP2mpLspTrMapAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamP2mpLspTrMapDSIPv4Addr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamP2mpLspTrMapDSIfAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamP2mpLspTrMapMTU"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamP2mpLspTrMapP2mpBranch"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamP2mpLspTrMapP2mpBud"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamP2mpLspTrDSLabelLabel"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamP2mpLspTrDSLabelProtocol"))
)
if mibBuilder.loadTexts:
    tmnxOamP2mpLspTraceGroup.setStatus("current")

tmnxOamTrGeneralV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 2, 27)
)
tmnxOamTrGeneralV6v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamTrMaxConcurrentRequests"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlRowStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlStorageType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlDescr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestMode"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlAdminStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlFcName"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlProfile"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlServiceId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlDataSize"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTimeOut"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlProbesPerHop"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlMaxTtl"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlInitialTtl"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlDSField"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlMaxFailures"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlInterval"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTrapGeneration"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlSAA"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlRuns"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlFailures"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlLastRunResult"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlLastChanged"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlVRtrID"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTgtAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTgtAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlSrcAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlSrcAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlWaitMilliSec"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsOperStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsCurHopCount"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsCurProbeCount"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsLastGoodPath"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsTgtAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsTgtAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryResponse"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryOneWayTime"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryLastRC"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryTime"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryResponsePlane"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryAddressType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistorySapId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryVersion"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryRouterID"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryIfIndex"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryDataLen"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistorySize"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryInOneWayTime"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceFecDiscoveryState"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceFecDisStatusBits"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceFecDisPaths"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceFecFailedHops"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceFecLastDisEnd"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceFecFailedProbes"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceFecProbeState"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtracePathRemAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtracePathRemoteAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtracePathEgrNhAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtracePathEgrNhAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtracePathDisTtl"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtracePathLastDisTime"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtracePathLastRc"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtracePathProbeState"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceCtlLdpPrefixType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceCtlLdpPrefix"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceCtlLdpPrefixLen"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceCtlMaxPath"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceResultsDisPaths"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceResultsFailedHops"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceResultsDisState"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceResultsDisStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceUpStreamHopIndex"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceHopAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceHopAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceHopDstAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceHopDstAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceHopEgrNhAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceHopEgrNhAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceHopDisTtl"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceHopLastRc"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceHopDiscoveryState"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceHopDiscoveryTime"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoRowStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoLastChanged"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoStorageType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoAdminState"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoFcName"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoProfile"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoDiscIntvl"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoMaxPath"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoTrMaxTtl"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoTrTimeOut"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoTrMaxFailures"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoPolicy1"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoPolicy2"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoPolicy3"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoPolicy4"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoPolicy5"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoProbeIntvl"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoPrTimeOut"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoPrMaxFailures"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoDiscoveryState"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoTotalFecs"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoDisFecs"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoLastDisStart"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoLastDisEnd"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoLastDisDur"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtracePathProbeState"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtracePathProbeTmOutCnt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceMaxConRequests"))
)
if mibBuilder.loadTexts:
    tmnxOamTrGeneralV6v0Group.setStatus("obsolete")

tmnxOamTrObsoleteV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 2, 28)
)
tmnxOamTrObsoleteV6v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlCreateHopsEntries"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrCtlVRtrID"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlMaxRows"))
)
if mibBuilder.loadTexts:
    tmnxOamTrObsoleteV6v0Group.setStatus("current")

tmnxOamTrGeneralV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 2, 29)
)
tmnxOamTrGeneralV7v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamTrMaxConcurrentRequests"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlRowStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestMode"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlAdminStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlFcName"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlProfile"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlServiceId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlDataSize"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTimeOut"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlProbesPerHop"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlMaxTtl"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlInitialTtl"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlDSField"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlMaxFailures"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlInterval"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTrapGeneration"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlSAA"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlRuns"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlFailures"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlLastRunResult"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlLastChanged"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlVRtrID"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTgtAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTgtAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlSrcAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlSrcAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlWaitMilliSec"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsOperStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsCurHopCount"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsCurProbeCount"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsLastGoodPath"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsTgtAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsTgtAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryResponse"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryOneWayTime"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryLastRC"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryTime"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryResponsePlane"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryAddressType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistorySapId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryVersion"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryRouterID"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryIfIndex"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryDataLen"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistorySize"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryInOneWayTime"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceFecDiscoveryState"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceFecDisStatusBits"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceFecDisPaths"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceFecFailedHops"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceFecLastDisEnd"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceFecFailedProbes"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceFecProbeState"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtracePathRemAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtracePathRemoteAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtracePathEgrNhAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtracePathEgrNhAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtracePathDisTtl"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtracePathLastDisTime"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtracePathLastRc"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtracePathProbeState"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceCtlLdpPrefixType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceCtlLdpPrefix"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceCtlLdpPrefixLen"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceCtlMaxPath"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceResultsDisPaths"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceResultsFailedHops"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceResultsDisState"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceResultsDisStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceUpStreamHopIndex"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceHopAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceHopAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceHopDstAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceHopDstAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceHopEgrNhAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceHopEgrNhAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceHopDisTtl"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceHopLastRc"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceHopDiscoveryState"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceHopDiscoveryTime"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoRowStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoLastChanged"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoAdminState"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoFcName"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoProfile"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoDiscIntvl"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoMaxPath"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoTrMaxTtl"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoTrTimeOut"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoTrMaxFailures"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoPolicy1"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoPolicy2"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoPolicy3"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoPolicy4"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoPolicy5"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoProbeIntvl"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoPrTimeOut"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoPrMaxFailures"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoDiscoveryState"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoTotalFecs"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoDisFecs"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoLastDisStart"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoLastDisEnd"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoLastDisDur"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtracePathProbeState"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtracePathProbeTmOutCnt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceMaxConRequests"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsRttOFSumSquares"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsRttHCSumSquares"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsTtOFSumSquares"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsTtHCSumSquares"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsInTtOFSumSqrs"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsInTtHCSumSqrs"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsTestRunResult"))
)
if mibBuilder.loadTexts:
    tmnxOamTrGeneralV7v0Group.setStatus("current")

tmnxOamEthCfmTrV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 2, 30)
)
tmnxOamEthCfmTrV8v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamEthCfmTrCtlTgtMacAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamEthCfmTrCtlSrcMdIndex"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamEthCfmTrCtlSrcMaIndex"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamEthCfmTrCtlSrcMepId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamEthCfmTrPrHistIngressMac"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamEthCfmTrPrHistEgressMac"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamEthCfmTrPrHistRelayAction"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamEthCfmTrPrHistForwarded"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamEthCfmTrPrHistTerminalMep"))
)
if mibBuilder.loadTexts:
    tmnxOamEthCfmTrV8v0Group.setStatus("current")

tmnxOamLspTrV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 2, 31)
)
tmnxOamLspTrV6v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrCtlLspName"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrCtlPathName"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrCtlLdpPrefixType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrCtlLdpPrefix"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrCtlLdpPrefixLen"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrCtlPathDestType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrCtlPathDest"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrCtlNhIntfName"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrCtlNhAddressType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrCtlNhAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrMapAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrMapDSIPv4Addr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrMapDSIfAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrMapMTU"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrDSLabelLabel"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrDSLabelProtocol"))
)
if mibBuilder.loadTexts:
    tmnxOamLspTrV6v0Group.setStatus("current")

tmnxOamTrGeneralV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 2, 32)
)
tmnxOamTrGeneralV8v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtracePathProbeSendErr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceFecSendErrProbes"))
)
if mibBuilder.loadTexts:
    tmnxOamTrGeneralV8v0Group.setStatus("current")

tmnxOamVccvTrV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 2, 34)
)
tmnxOamVccvTrV9v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrCtlSpokeSdpId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrCtlSaiiGlobalId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrCtlSaiiPrefix"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrCtlSaiiAcId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrCtlTaiiGlobalId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrCtlTaiiPrefix"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrCtlTaiiAcId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrNextSaiiGlobalId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrNextSaiiPrefix"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrNextSaiiAcId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrNextTaiiGlobalId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrNextTaiiPrefix"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrNextTaiiAcId"))
)
if mibBuilder.loadTexts:
    tmnxOamVccvTrV9v0Group.setStatus("current")

tmnxOamLTtraceV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 2, 35)
)
tmnxOamLTtraceV9v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceHopLabel1"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceHopLabel2"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceHopLabel3"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceHopLabel4"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceHopLabel5"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceHopLabel6"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceHopIfAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceHopIfAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceHopRouterIdType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceHopRouterId"))
)
if mibBuilder.loadTexts:
    tmnxOamLTtraceV9v0Group.setStatus("current")

tmnxOamTrGeneralV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 2, 36)
)
tmnxOamTrGeneralV11v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceCtlDownstreamMpTlv"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrCtlAssocChannel"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrCtlDownstreamMapTlv"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrCtlForce"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrCtlMplsTpPathType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrCtlTestSubMode"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrFecStackFecSubType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrFecStackOperType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrFecStackPrefix"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrFecStackPrefixLen"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrFecStackPrefixType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrFecStackRemPeerAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrFecStackRemPeerAddrT"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryRtrnSubcode"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistorySdpBindId"))
)
if mibBuilder.loadTexts:
    tmnxOamTrGeneralV11v0Group.setStatus("current")

tmnxOamVccvTrV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 2, 37)
)
tmnxOamVccvTrV11v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrCtlAssocChannel"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrCtlTestSubMode"))
)
if mibBuilder.loadTexts:
    tmnxOamVccvTrV11v0Group.setStatus("current")

tmnxOamTrV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 2, 38)
)
tmnxOamTrV11v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistorySrcGlobalId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistorySrcNodeId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrNextTpAgi"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrNextTpSaiiAcId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrNextTpSaiiGlobalId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrNextTpSaiiNodeId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrNextTpTaiiAcId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrNextTpTaiiGlobalId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrNextTpTaiiNodeId"))
)
if mibBuilder.loadTexts:
    tmnxOamTrV11v0Group.setStatus("current")

tmnxOamTrV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 2, 39)
)
tmnxOamTrV12v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamIcmpTrLabelStackBottom"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIcmpTrLabelStackExperimnt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIcmpTrLabelStackLabel"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIcmpTrLabelStackTtl"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrCtlSwitTgtFecType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrTgFec128CtlDstAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrTgFec128CtlDstAddrT"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrTgFec128CtlPwId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrTgFec128CtlPwType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrTgFec128CtlSrcAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrTgFec128CtlSrcAddrT"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrTgStaticCtlAgi"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrTgStaticCtlSaiiAcId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrTgStaticCtlSaiiGlbl"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrTgStaticCtlSaiiNode"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrTgStaticCtlTaiiAcId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrTgStaticCtlTaiiGlbl"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrTgStaticCtlTaiiNode"))
)
if mibBuilder.loadTexts:
    tmnxOamTrV12v0Group.setStatus("current")

tmnxOamTrObsoleteV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 2, 40)
)
tmnxOamTrObsoleteV13v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrMapDSIPv4Addr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrMapDSIfAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryRouterID"))
)
if mibBuilder.loadTexts:
    tmnxOamTrObsoleteV13v0Group.setStatus("current")

tmnxOamTrV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 2, 41)
)
tmnxOamTrV13v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrMapDsEgrIfNum"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrMapDsIfAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrMapDsIfAddressType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrMapDsIngIfNum"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrMapDsIpAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrMapDsIpAddressType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryNtwrkIfName"))
)
if mibBuilder.loadTexts:
    tmnxOamTrV13v0Group.setStatus("current")

tmnxOamTrObsoleteV14v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 2, 42)
)
tmnxOamTrObsoleteV14v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoStorageType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlDescr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlStorageType"))
)
if mibBuilder.loadTexts:
    tmnxOamTrObsoleteV14v0Group.setStatus("current")

tmnxOamTrV15v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 2, 44)
)
tmnxOamTrV15v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamEthCfmTrCtlRemoteMepId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrCtlIgpInstance"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrCtlTestSubMode"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrRespInIfIndex"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrRespInPktCountHC"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrRespLocalAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrRespLocalAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrRespMcastRtgProto"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrRespOutIfIndex"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrRespOutPktCountHC"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrRespRtgProtocol2"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrRespSGPktCountHC"))
)
if mibBuilder.loadTexts:
    tmnxOamTrV15v0Group.setStatus("current")

tmnxOamTrV16v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 2, 45)
)
tmnxOamTrV16v0Group.setObjects(
    ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlRouterInstanceName")
)
if mibBuilder.loadTexts:
    tmnxOamTrV16v0Group.setStatus("current")

tmnxOamTrV19v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 2, 46, 1)
)
tmnxOamTrV19v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrCtlSrPlcyColor"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrCtlSrPlcyEndPtAddT"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrCtlSrPlcyEndPtAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrCtlSrPlcySegList"))
)
if mibBuilder.loadTexts:
    tmnxOamTrV19v0Group.setStatus("current")

tmnxOamBierTrV20v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 2, 47, 1)
)
tmnxOamBierTrV20v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamBierTrCtlBfrId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBierTrCtlBfrPfxAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBierTrCtlBfrPfxAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBierTrCtlSubDomain"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBierTrHistoryBfrId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBierTrHistoryDnStrAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBierTrHistoryDnStrAddrTyp"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBierTrHistoryDnStrIfAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBierTrHistoryDnStrIfAddrT"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBierTrHistoryDnStrIfNum"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBierTrHistoryReturnCode"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBierTrHistoryUpStrIfAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBierTrHistoryUpStrIfAddrT"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBierTrHistoryUpStrIfNum"))
)
if mibBuilder.loadTexts:
    tmnxOamBierTrV20v0Group.setStatus("current")

tmnxOamIcmpTrV21v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 2, 48, 1)
)
tmnxOamIcmpTrV21v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamIcmpTrCtlDestTcpUdpPort"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIcmpTrCtlDestUdpPortFixed"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIcmpTrCtlPadSize"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIcmpTrCtlProtocol"))
)
if mibBuilder.loadTexts:
    tmnxOamIcmpTrV21v0Group.setStatus("current")

tmnxOamSaaGeneralV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 3, 2, 1)
)
tmnxOamSaaGeneralV3v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamSaaCtlRowStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSaaCtlStorageType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSaaCtlLastChanged"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSaaCtlAdminStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSaaCtlTestMode"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSaaCtlDescr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSaaCtlRuns"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSaaCtlFailures"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSaaCtlLastRunResult"))
)
if mibBuilder.loadTexts:
    tmnxOamSaaGeneralV3v0Group.setStatus("obsolete")

tmnxOamSaaThresholdV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 3, 2, 2)
)
tmnxOamSaaThresholdV3v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamSaaTRowStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSaaTLastChanged"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSaaTThreshold"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSaaTValue"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSaaTLastSent"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSaaTTestMode"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSaaTTestRunIndex"))
)
if mibBuilder.loadTexts:
    tmnxOamSaaThresholdV3v0Group.setStatus("current")

tmnxOamSaaGeneralV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 3, 2, 4)
)
tmnxOamSaaGeneralV7v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamSaaCtlRowStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSaaCtlLastChanged"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSaaCtlAdminStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSaaCtlTestMode"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSaaCtlDescr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSaaCtlRuns"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSaaCtlFailures"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSaaCtlLastRunResult"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSaaCtlAcctPolicyId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSaaCtlSuppressAccounting"))
)
if mibBuilder.loadTexts:
    tmnxOamSaaGeneralV7v0Group.setStatus("current")

tmnxOamSaaGeneralV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 3, 2, 5)
)
tmnxOamSaaGeneralV8v0Group.setObjects(
    ("TIMETRA-OAM-TEST-MIB", "tmnxOamSaaCtlContinuous")
)
if mibBuilder.loadTexts:
    tmnxOamSaaGeneralV8v0Group.setStatus("current")

tmnxOamSaaGeneralV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 3, 2, 6)
)
tmnxOamSaaGeneralV10v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamSaaCtlKeepProbeHistoryAdm"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSaaCtlKeepProbeHistoryOpr"))
)
if mibBuilder.loadTexts:
    tmnxOamSaaGeneralV10v0Group.setStatus("current")

tmnxOamSaaObsoleteV14v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 3, 2, 7)
)
tmnxOamSaaObsoleteV14v0Group.setObjects(
    ("TIMETRA-OAM-TEST-MIB", "tmnxOamSaaCtlStorageType")
)
if mibBuilder.loadTexts:
    tmnxOamSaaObsoleteV14v0Group.setStatus("current")

tmnxOamGeneralV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 5, 2, 1)
)
tmnxOamGeneralV8v0Group.setObjects(
    ("TIMETRA-OAM-TEST-MIB", "tmnxOamMplsPduTimeStampFormat")
)
if mibBuilder.loadTexts:
    tmnxOamGeneralV8v0Group.setStatus("current")

tmnxOamGeneralV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 5, 2, 2)
)
tmnxOamGeneralV10v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamSysPerfOprLimitTx"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSysPerfCfgLimitTx"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSysPerfCfgTotalTx"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSysPerfLastClearedTime"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSysPerfLocalTestTx"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSysPerfRemoteTestRx"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSysPerfReqTypeLocalTestTx"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSysPerfReqTypeRemoteTstRx"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSysSessionLimit"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSysSessionCount"))
)
if mibBuilder.loadTexts:
    tmnxOamGeneralV10v0Group.setStatus("current")

tmnxOamGeneralV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 5, 2, 3)
)
tmnxOamGeneralV11v0Group.setObjects(
    ("TIMETRA-OAM-TEST-MIB", "tmnxOamMplsEchoDownstreamMapTlv")
)
if mibBuilder.loadTexts:
    tmnxOamGeneralV11v0Group.setStatus("current")

tmnxOamGeneralV14v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 5, 2, 6)
)
tmnxOamGeneralV14v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamSysBgIcmpBrgSessionCount"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSysBgIcmpBrgSessionLimit"))
)
if mibBuilder.loadTexts:
    tmnxOamGeneralV14v0Group.setStatus("current")

tmnxOamGeneralV19v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 5, 2, 9)
)
tmnxOamGeneralV19v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamSysLspSelfPingSessCount"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSysLspSelfPingSessLimit"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSysPerfCfgLspSelfTxLimit"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSysPerfCfgLspSelfTxTotal"))
)
if mibBuilder.loadTexts:
    tmnxOamGeneralV19v0Group.setStatus("current")

tmnxOamGenPoolSplitV20v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 5, 2, 10)
)
tmnxOamGenPoolSplitV20v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamSysTestLimit"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSysTestCount"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSysTxLimit"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSysTxTotal"))
)
if mibBuilder.loadTexts:
    tmnxOamGenPoolSplitV20v0Group.setStatus("current")

tmnxOamGenPoolShareV20v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 5, 2, 11)
)
tmnxOamGenPoolShareV20v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamSysShareTestLimit"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSysShareTestCount"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSysShareTxLimit"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSysShareTxTotal"))
)
if mibBuilder.loadTexts:
    tmnxOamGenPoolShareV20v0Group.setStatus("current")

tmnxOamGenObsoletedV21v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 5, 2, 12)
)
tmnxOamGenObsoletedV21v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamIcmpPingCtlEgrIfIndex"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSysPerfOprLimitTx"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSysPerfCfgLimitTx"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSysPerfCfgTotalTx"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSysSessionLimit"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSysSessionCount"))
)
if mibBuilder.loadTexts:
    tmnxOamGenObsoletedV21v0Group.setStatus("current")

tmnxOamDiagV16v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 6, 2, 1)
)
tmnxOamDiagV16v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktDot1qLastChanged"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktDot1qPrioCodePt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktDot1qTagProtoId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktDot1qVlanId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktEthDstMacAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktEthLastChanged"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktEthSrcMacAddr"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktGtpUserLastChgd"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktGtpUserTunnEpIdHi"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktGtpUserTunnEpIdLo"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktHdrLastChanged"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktHdrOvrLastChanged"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktHdrOvrRowStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktHdrRowStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktHdrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktHeaderSeq"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktIPsecAuthLastChgd"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktIPsecAuthSecPrIdx"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktIPv4MoreFragments"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktIpDscp"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktIpDstIpAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktIpDstIpAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktIpLastChanged"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktIpSrcIpAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktIpSrcIpAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktL2tpLastChanged"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktL2tpSessionId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktL2tpTunnelId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktLastChanged"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktMplsLabel"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktMplsLastChanged"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktMplsTrafficClass"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktPbbIsid"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktPbbLastChanged"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktPbbTagProtocolId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktRowStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktTcpUdpDstPort"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktTcpUdpLastChanged"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamBuildPktTcpUdpSrcPort"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamDiagCtlAdminState"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamDiagCtlLastChanged"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamDiagCtlRowStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamDiagCtlTestMode"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamFindEgrDiagCtlIngPortId"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamFindEgrDiagCtlLastChanged"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamFindEgrDiagCtlPacketNum"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamFindEgrDiagEgrRtrInstName"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamFindEgrDiagEgressIfName"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamFindEgrDiagEgressPort"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamFindEgrDiagNextHopAddrTyp"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamFindEgrDiagNextHopAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamFindEgrDiagOperState"))
)
if mibBuilder.loadTexts:
    tmnxOamDiagV16v0Group.setStatus("current")

tmnxOamDiagNotifyObjsV16v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 6, 2, 3)
)
tmnxOamDiagNotifyObjsV16v0Group.setObjects(
    ("TIMETRA-OAM-TEST-MIB", "tmnxOamTestRunIndex")
)
if mibBuilder.loadTexts:
    tmnxOamDiagNotifyObjsV16v0Group.setStatus("current")


# Notification objects

tmnxOamPingProbeFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 11, 1, 0, 1)
)
tmnxOamPingProbeFailed.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTargetIpAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsOperStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMinRtt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMaxRtt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsAverageRtt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsRttSumOfSquares"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMtuResponseSize"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsSvcPing"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsProbeResponses"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsSentProbes"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsLastGoodProbe"))
)
if mibBuilder.loadTexts:
    tmnxOamPingProbeFailed.setStatus(
        "obsolete"
    )

tmnxOamPingTestFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 11, 1, 0, 2)
)
tmnxOamPingTestFailed.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTargetIpAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsOperStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMinRtt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMaxRtt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsAverageRtt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsRttSumOfSquares"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMtuResponseSize"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsSvcPing"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsProbeResponses"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsSentProbes"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsLastGoodProbe"))
)
if mibBuilder.loadTexts:
    tmnxOamPingTestFailed.setStatus(
        "obsolete"
    )

tmnxOamPingTestCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 11, 1, 0, 3)
)
tmnxOamPingTestCompleted.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTargetIpAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsOperStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMinRtt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMaxRtt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsAverageRtt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsRttSumOfSquares"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMtuResponseSize"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsSvcPing"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsProbeResponses"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsSentProbes"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsLastGoodProbe"))
)
if mibBuilder.loadTexts:
    tmnxOamPingTestCompleted.setStatus(
        "obsolete"
    )

tmnxOamPingProbeFailedV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 11, 1, 0, 4)
)
tmnxOamPingProbeFailedV2.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTgtAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTgtAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsOperStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMinRtt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMaxRtt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsAverageRtt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsRttSumOfSquares"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMtuResponseSize"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsSvcPing"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsProbeResponses"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsSentProbes"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsLastGoodProbe"))
)
if mibBuilder.loadTexts:
    tmnxOamPingProbeFailedV2.setStatus(
        "obsolete"
    )

tmnxOamPingTestFailedV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 11, 1, 0, 5)
)
tmnxOamPingTestFailedV2.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTgtAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTgtAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsOperStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMinRtt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMaxRtt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsAverageRtt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsRttSumOfSquares"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMtuResponseSize"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsSvcPing"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsProbeResponses"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsSentProbes"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsLastGoodProbe"))
)
if mibBuilder.loadTexts:
    tmnxOamPingTestFailedV2.setStatus(
        "obsolete"
    )

tmnxOamPingTestCompletedV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 11, 1, 0, 6)
)
tmnxOamPingTestCompletedV2.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTgtAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTgtAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsOperStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMinRtt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMaxRtt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsAverageRtt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsRttSumOfSquares"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMtuResponseSize"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsSvcPing"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsProbeResponses"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsSentProbes"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsLastGoodProbe"))
)
if mibBuilder.loadTexts:
    tmnxOamPingTestCompletedV2.setStatus(
        "obsolete"
    )

tmnxAncpLoopbackTestCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 11, 1, 0, 7)
)
tmnxAncpLoopbackTestCompleted.setObjects(
    ("TIMETRA-OAM-TEST-MIB", "tmnxOamAncpHistoryAncpString")
)
if mibBuilder.loadTexts:
    tmnxAncpLoopbackTestCompleted.setStatus(
        "current"
    )

tmnxOamPingProbeFailedV3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 11, 1, 0, 8)
)
tmnxOamPingProbeFailedV3.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTgtAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTgtAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsOperStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMinRtt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMaxRtt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsAverageRtt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsRttSumOfSquares"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsRttOFSumSquares"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMtuResponseSize"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsSvcPing"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsProbeResponses"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsSentProbes"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsLastGoodProbe"))
)
if mibBuilder.loadTexts:
    tmnxOamPingProbeFailedV3.setStatus(
        "current"
    )

tmnxOamPingTestFailedV3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 11, 1, 0, 9)
)
tmnxOamPingTestFailedV3.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTgtAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTgtAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsOperStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMinRtt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMaxRtt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsAverageRtt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsRttSumOfSquares"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsRttOFSumSquares"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMtuResponseSize"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsSvcPing"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsProbeResponses"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsSentProbes"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsLastGoodProbe"))
)
if mibBuilder.loadTexts:
    tmnxOamPingTestFailedV3.setStatus(
        "current"
    )

tmnxOamPingTestCompletedV3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 11, 1, 0, 10)
)
tmnxOamPingTestCompletedV3.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTgtAddrType"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTgtAddress"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsOperStatus"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMinRtt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMaxRtt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsAverageRtt"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsRttSumOfSquares"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsRttOFSumSquares"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMtuResponseSize"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsSvcPing"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsProbeResponses"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsSentProbes"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsLastGoodProbe"))
)
if mibBuilder.loadTexts:
    tmnxOamPingTestCompletedV3.setStatus(
        "current"
    )

tmnxOamTrPathChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 11, 2, 0, 1)
)
tmnxOamTrPathChange.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestMode"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlLastRunResult"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsOperStatus"))
)
if mibBuilder.loadTexts:
    tmnxOamTrPathChange.setStatus(
        "current"
    )

tmnxOamTrTestFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 11, 2, 0, 2)
)
tmnxOamTrTestFailed.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestMode"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlLastRunResult"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsOperStatus"))
)
if mibBuilder.loadTexts:
    tmnxOamTrTestFailed.setStatus(
        "current"
    )

tmnxOamTrTestCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 11, 2, 0, 3)
)
tmnxOamTrTestCompleted.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestMode"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlLastRunResult"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsOperStatus"))
)
if mibBuilder.loadTexts:
    tmnxOamTrTestCompleted.setStatus(
        "current"
    )

tmnxOamLdpTtraceAutoDiscState = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 11, 2, 0, 4)
)
tmnxOamLdpTtraceAutoDiscState.setObjects(
    ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoDiscoveryState")
)
if mibBuilder.loadTexts:
    tmnxOamLdpTtraceAutoDiscState.setStatus(
        "current"
    )

tmnxOamLdpTtraceFecProbeState = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 11, 2, 0, 5)
)
tmnxOamLdpTtraceFecProbeState.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceFecProbeState"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceFecDisPaths"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceFecFailedProbes"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceFecSendErrProbes"))
)
if mibBuilder.loadTexts:
    tmnxOamLdpTtraceFecProbeState.setStatus(
        "current"
    )

tmnxOamLdpTtraceFecDisStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 11, 2, 0, 6)
)
tmnxOamLdpTtraceFecDisStatus.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceFecDisStatusBits"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceFecDisPaths"))
)
if mibBuilder.loadTexts:
    tmnxOamLdpTtraceFecDisStatus.setStatus(
        "current"
    )

tmnxOamLdpTtraceFecPFailUpdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 11, 2, 0, 7)
)
tmnxOamLdpTtraceFecPFailUpdate.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceFecProbeState"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceFecDisPaths"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceFecFailedProbes"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceFecSendErrProbes"))
)
if mibBuilder.loadTexts:
    tmnxOamLdpTtraceFecPFailUpdate.setStatus(
        "current"
    )

tmnxOamSaaThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 11, 3, 0, 1)
)
tmnxOamSaaThreshold.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamSaaTThreshold"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSaaTValue"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSaaCtlTestMode"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSaaCtlLastRunResult"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSaaTTestRunIndex"))
)
if mibBuilder.loadTexts:
    tmnxOamSaaThreshold.setStatus(
        "current"
    )

tmnxOamDiagTestCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 11, 6, 0, 1)
)
tmnxOamDiagTestCompleted.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamDiagCtlTestMode"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTestRunIndex"))
)
if mibBuilder.loadTexts:
    tmnxOamDiagTestCompleted.setStatus(
        "current"
    )


# Notifications groups

tmnxOamPingNotificationV4v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 25)
)
tmnxOamPingNotificationV4v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamPingProbeFailedV2"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingTestFailedV2"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingTestCompletedV2"))
)
if mibBuilder.loadTexts:
    tmnxOamPingNotificationV4v0Group.setStatus(
        "obsolete"
    )

tmnxOamPingNotificationObsoleteV4v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 26)
)
tmnxOamPingNotificationObsoleteV4v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamPingProbeFailed"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingTestFailed"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingTestCompleted"))
)
if mibBuilder.loadTexts:
    tmnxOamPingNotificationObsoleteV4v0Group.setStatus(
        "current"
    )

tmnxOamPingNotificationV5v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 30)
)
tmnxOamPingNotificationV5v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamPingProbeFailedV2"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingTestFailedV2"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingTestCompletedV2"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxAncpLoopbackTestCompleted"))
)
if mibBuilder.loadTexts:
    tmnxOamPingNotificationV5v0Group.setStatus(
        "obsolete"
    )

tmnxOamPingNotificationV7v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 36)
)
tmnxOamPingNotificationV7v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamPingProbeFailedV3"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingTestFailedV3"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingTestCompletedV3"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxAncpLoopbackTestCompleted"))
)
if mibBuilder.loadTexts:
    tmnxOamPingNotificationV7v0Group.setStatus(
        "current"
    )

tmnxOamTrNotificationV4v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 2, 18)
)
tmnxOamTrNotificationV4v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamTrPathChange"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrTestFailed"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrTestCompleted"))
)
if mibBuilder.loadTexts:
    tmnxOamTrNotificationV4v0Group.setStatus(
        "obsolete"
    )

tmnxOamTrNotificationV5v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 2, 22)
)
tmnxOamTrNotificationV5v0Group.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamTrPathChange"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrTestFailed"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrTestCompleted"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLdpTtraceAutoDiscState"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLdpTtraceFecProbeState"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLdpTtraceFecDisStatus"))
)
if mibBuilder.loadTexts:
    tmnxOamTrNotificationV5v0Group.setStatus(
        "current"
    )

tmnxOamTrNotificationV8v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 2, 33)
)
tmnxOamTrNotificationV8v0Group.setObjects(
    ("TIMETRA-OAM-TEST-MIB", "tmnxOamLdpTtraceFecPFailUpdate")
)
if mibBuilder.loadTexts:
    tmnxOamTrNotificationV8v0Group.setStatus(
        "current"
    )

tmnxOamSaaNotificationV3v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 3, 2, 3)
)
tmnxOamSaaNotificationV3v0Group.setObjects(
    ("TIMETRA-OAM-TEST-MIB", "tmnxOamSaaThreshold")
)
if mibBuilder.loadTexts:
    tmnxOamSaaNotificationV3v0Group.setStatus(
        "current"
    )

tmnxOamDiagNotificationV16v0Grp = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 6, 2, 2)
)
tmnxOamDiagNotificationV16v0Grp.setObjects(
    ("TIMETRA-OAM-TEST-MIB", "tmnxOamDiagTestCompleted")
)
if mibBuilder.loadTexts:
    tmnxOamDiagNotificationV16v0Grp.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxOamPing7450V4v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 1, 4)
)
tmnxOamPing7450V4v0Compliance.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamPingGeneralV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMfibPingV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamCpePingV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPingGroup"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIcmpPingGroup"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingNotificationV4v0Group"))
)
if mibBuilder.loadTexts:
    tmnxOamPing7450V4v0Compliance.setStatus(
        "obsolete"
    )

tmnxOamPing7750V4v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 1, 5)
)
tmnxOamPing7750V4v0Compliance.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamPingGeneralV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnPingV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMfibPingV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamCpePingV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMRInfoV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamAtmPingR2r1Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPingGroup"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIcmpPingGroup"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingNotificationV4v0Group"))
)
if mibBuilder.loadTexts:
    tmnxOamPing7750V4v0Compliance.setStatus(
        "obsolete"
    )

tmnxOamPing7450V5v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 1, 6)
)
tmnxOamPing7450V5v0Compliance.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamPingGeneralV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingV5v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMfibPingV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamCpePingV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPingV5v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIcmpPingGroup"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamAncpTestV5v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingNotificationV5v0Group"))
)
if mibBuilder.loadTexts:
    tmnxOamPing7450V5v0Compliance.setStatus(
        "obsolete"
    )

tmnxOamPing7750V5v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 1, 7)
)
tmnxOamPing7750V5v0Compliance.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamPingGeneralV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingV5v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnPingV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMfibPingV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamCpePingV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMRInfoV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamAtmPingR2r1Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPingV5v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIcmpPingGroup"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamAncpTestV5v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingNotificationV5v0Group"))
)
if mibBuilder.loadTexts:
    tmnxOamPing7750V5v0Compliance.setStatus(
        "obsolete"
    )

tmnxOamPing7450V6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 1, 8)
)
tmnxOamPing7450V6v0Compliance.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamPingGeneralV6v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingV6v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMfibPingV6v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamCpePingV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPingV5v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIcmpPingGroup"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamAncpTestV5v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingNotificationV5v0Group"))
)
if mibBuilder.loadTexts:
    tmnxOamPing7450V6v0Compliance.setStatus(
        "obsolete"
    )

tmnxOamPing7750V6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 1, 9)
)
tmnxOamPing7750V6v0Compliance.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamPingGeneralV6v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingV6v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnPingV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMfibPingV6v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamCpePingV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMRInfoV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamAtmPingR2r1Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPingV5v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIcmpPingGroup"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamAncpTestV5v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingNotificationV5v0Group"))
)
if mibBuilder.loadTexts:
    tmnxOamPing7750V6v0Compliance.setStatus(
        "obsolete"
    )

tmnxOamPing7450V7v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 1, 10)
)
tmnxOamPing7450V7v0Compliance.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamPingGeneralV7v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingV6v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMfibPingV6v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamCpePingV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPingV5v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIcmpPingGroup"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamAncpTestV5v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingNotificationV7v0Group"))
)
if mibBuilder.loadTexts:
    tmnxOamPing7450V7v0Compliance.setStatus(
        "obsolete"
    )

tmnxOamPing7750V7v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 1, 11)
)
tmnxOamPing7750V7v0Compliance.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamPingGeneralV7v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingV6v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnPingV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMfibPingV6v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamCpePingV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMRInfoV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamAtmPingR2r1Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPingV5v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIcmpPingGroup"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamAncpTestV5v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingNotificationV7v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamP2mpLspPingGroup"))
)
if mibBuilder.loadTexts:
    tmnxOamPing7750V7v0Compliance.setStatus(
        "obsolete"
    )

tmnxOamPing7450V8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 1, 12)
)
tmnxOamPing7450V8v0Compliance.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamPingGeneralV8v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingV6v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMfibPingV6v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamCpePingV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPingV5v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIcmpPingGroup"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamAncpTestV5v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamEthCfmPingV8v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingNotificationV7v0Group"))
)
if mibBuilder.loadTexts:
    tmnxOamPing7450V8v0Compliance.setStatus(
        "obsolete"
    )

tmnxOamPing77x0V8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 1, 13)
)
tmnxOamPing77x0V8v0Compliance.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamPingGeneralV8v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingV6v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnPingV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMfibPingV6v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamCpePingV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMRInfoV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamAtmPingR2r1Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPingV5v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIcmpPingGroup"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamAncpTestV5v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamEthCfmPingV8v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingNotificationV7v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamP2mpLspPingGroup"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamP2mpLspPingV8v0Group"))
)
if mibBuilder.loadTexts:
    tmnxOamPing77x0V8v0Compliance.setStatus(
        "obsolete"
    )

tmnxOamPing7xx0V9v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 1, 14)
)
tmnxOamPing7xx0V9v0Compliance.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamPingGeneralV8v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingV6v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnPingV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMfibPingV6v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamCpePingV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMRInfoV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamAtmPingR2r1Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPingV5v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIcmpPingGroup"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamAncpTestV5v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamEthCfmPingV8v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingNotificationV7v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamP2mpLspPingGroup"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamP2mpLspPingV8v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPingV9v0Group"))
)
if mibBuilder.loadTexts:
    tmnxOamPing7xx0V9v0Compliance.setStatus(
        "obsolete"
    )

tmnxOamPing7xx0V10v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 1, 15)
)
tmnxOamPing7xx0V10v0Compliance.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamPingGeneralV10v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingV6v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnPingV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMfibPingV6v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamCpePingV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMRInfoV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamAtmPingR2r1Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPingV5v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIcmpPingGroup"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamAncpTestV5v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamEthCfmPingV8v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingNotificationV7v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamP2mpLspPingGroup"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamP2mpLspPingV8v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPingV9v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlV10v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMobilePingGroup"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamP2mpLspPingV10v0Group"))
)
if mibBuilder.loadTexts:
    tmnxOamPing7xx0V10v0Compliance.setStatus(
        "obsolete"
    )

tmnxOamPing7xx0V11v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 1, 16)
)
tmnxOamPing7xx0V11v0Compliance.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamAncpTestV5v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamAtmPingR2r1Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamCpePingV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamEthCfmPingV8v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIcmpPingGroup"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingV11v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMRInfoV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingCtlV11v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingHistoryV11v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMfibPingV6v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMobilePingGroup"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamP2mpLspPingGroup"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamP2mpLspPingV10v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamP2mpLspPingV8v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlV10v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingGeneralV10v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingNotificationV7v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingV11v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPingV5v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPingV9v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPingV11v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnPingV4v0Group"))
)
if mibBuilder.loadTexts:
    tmnxOamPing7xx0V11v0Compliance.setStatus(
        "obsolete"
    )

tmnxOamPing7xx0V12v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 1, 17)
)
tmnxOamPing7xx0V12v0Compliance.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamAncpTestV5v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamAtmPingR2r1Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamCpePingV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamEthCfmPingV8v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIcmpPingGroup"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingV11v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMRInfoV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingCtlV11v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingHistoryV11v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMfibPingV6v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMobilePingGroup"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamP2mpLspPingGroup"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamP2mpLspPingV8v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamP2mpLspPingV10v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlV10v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingGeneralV10v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingNotificationV7v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingV11v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingV12v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPingV5v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPingV9v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPingV11v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnPingV4v0Group"))
)
if mibBuilder.loadTexts:
    tmnxOamPing7xx0V12v0Compliance.setStatus(
        "obsolete"
    )

tmnxOamPing7xx0V13v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 1, 18)
)
tmnxOamPing7xx0V13v0Compliance.setObjects(
    ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingV13v0Group")
)
if mibBuilder.loadTexts:
    tmnxOamPing7xx0V13v0Compliance.setStatus(
        "current"
    )

tmnxOamPing7xx0V14v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 1, 19)
)
tmnxOamPing7xx0V14v0Compliance.setObjects(
    ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingV14v0Group")
)
if mibBuilder.loadTexts:
    tmnxOamPing7xx0V14v0Compliance.setStatus(
        "current"
    )

tmnxOamPing7xx0V15v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 1, 20)
)
tmnxOamPing7xx0V15v0Compliance.setObjects(
    ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingV15v0Group")
)
if mibBuilder.loadTexts:
    tmnxOamPing7xx0V15v0Compliance.setStatus(
        "current"
    )

tmnxOamPing7xx0V16v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 1, 21)
)
tmnxOamPing7xx0V16v0Compliance.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamPingNotificationV7v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamAncpTestV5v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamAtmPingR2r1Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamCpePingV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamEthCfmPingV8v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamIcmpPingGroup"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingV11v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMRInfoV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingCtlV11v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingHistoryV11v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMfibPingV6v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMobilePingV16v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamP2mpLspPingGroup"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamP2mpLspPingV8v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamP2mpLspPingV10v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlV10v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingGeneralV10v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingObsoletedV16v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingV11v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingV12v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingV16v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrV16v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPingV5v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPingV9v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPingV11v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnPingV4v0Group"))
)
if mibBuilder.loadTexts:
    tmnxOamPing7xx0V16v0Compliance.setStatus(
        "current"
    )

tmnxOamPing7xx0V19v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 1, 22)
)
tmnxOamPing7xx0V19v0Compliance.setObjects(
    ("TIMETRA-OAM-TEST-MIB", "tmnxOamPingV19v0Group")
)
if mibBuilder.loadTexts:
    tmnxOamPing7xx0V19v0Compliance.setStatus(
        "current"
    )

tmnxOamPing7xx0V20v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 1, 23)
)
tmnxOamPing7xx0V20v0Compliance.setObjects(
    ("TIMETRA-OAM-TEST-MIB", "tmnxOamBierPingV20v0Group")
)
if mibBuilder.loadTexts:
    tmnxOamPing7xx0V20v0Compliance.setStatus(
        "current"
    )

tmnxOamTr7450V4v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 1, 3)
)
tmnxOamTr7450V4v0Compliance.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamTrGeneralV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacTrV3v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrNotificationV4v0Group"))
)
if mibBuilder.loadTexts:
    tmnxOamTr7450V4v0Compliance.setStatus(
        "obsolete"
    )

tmnxOamTr7750V4v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 1, 4)
)
tmnxOamTr7750V4v0Compliance.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamTrGeneralV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacTrV3v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrNotificationV4v0Group"))
)
if mibBuilder.loadTexts:
    tmnxOamTr7750V4v0Compliance.setStatus(
        "obsolete"
    )

tmnxOamTr7450V5v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 1, 5)
)
tmnxOamTr7450V5v0Compliance.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamTrGeneralV5v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacTrV3v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrV5v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrNotificationV5v0Group"))
)
if mibBuilder.loadTexts:
    tmnxOamTr7450V5v0Compliance.setStatus(
        "obsolete"
    )

tmnxOamTr7750V5v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 1, 6)
)
tmnxOamTr7750V5v0Compliance.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamTrGeneralV5v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacTrV3v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrV5v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrNotificationV5v0Group"))
)
if mibBuilder.loadTexts:
    tmnxOamTr7750V5v0Compliance.setStatus(
        "obsolete"
    )

tmnxOamTr7450V6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 1, 7)
)
tmnxOamTr7450V6v0Compliance.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamTrGeneralV6v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacTrV3v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrV6v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrV6v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrNotificationV5v0Group"))
)
if mibBuilder.loadTexts:
    tmnxOamTr7450V6v0Compliance.setStatus(
        "obsolete"
    )

tmnxOamTr77x0V6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 1, 8)
)
tmnxOamTr77x0V6v0Compliance.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamTrGeneralV6v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacTrV3v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrV6v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrV6v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrV6v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrNotificationV5v0Group"))
)
if mibBuilder.loadTexts:
    tmnxOamTr77x0V6v0Compliance.setStatus(
        "obsolete"
    )

tmnxOamTr7450V7v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 1, 9)
)
tmnxOamTr7450V7v0Compliance.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamTrGeneralV7v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacTrV3v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrV6v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrV6v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrNotificationV5v0Group"))
)
if mibBuilder.loadTexts:
    tmnxOamTr7450V7v0Compliance.setStatus(
        "obsolete"
    )

tmnxOamTr77x0V7v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 1, 10)
)
tmnxOamTr77x0V7v0Compliance.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamTrGeneralV7v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacTrV3v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrV6v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrV6v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrV6v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrNotificationV5v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamP2mpLspTraceGroup"))
)
if mibBuilder.loadTexts:
    tmnxOamTr77x0V7v0Compliance.setStatus(
        "obsolete"
    )

tmnxOamTr7xx0V8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 1, 11)
)
tmnxOamTr7xx0V8v0Compliance.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamTrGeneralV7v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacTrV3v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrV6v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrV6v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrV6v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrNotificationV5v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamP2mpLspTraceGroup"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamEthCfmTrV8v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrGeneralV8v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrNotificationV8v0Group"))
)
if mibBuilder.loadTexts:
    tmnxOamTr7xx0V8v0Compliance.setStatus(
        "obsolete"
    )

tmnxOamTr7xx0V9v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 1, 12)
)
tmnxOamTr7xx0V9v0Compliance.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamEthCfmTrV8v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceV9v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrV6v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacTrV3v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamP2mpLspTraceGroup"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrGeneralV7v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrGeneralV8v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrNotificationV5v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrNotificationV8v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrV6v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrV9v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrV6v0Group"))
)
if mibBuilder.loadTexts:
    tmnxOamTr7xx0V9v0Compliance.setStatus(
        "obsolete"
    )

tmnxOamTr7xx0V11v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 1, 13)
)
tmnxOamTr7xx0V11v0Compliance.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamEthCfmTrV8v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceV9v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrV6v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMacTrV3v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamP2mpLspTraceGroup"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrGeneralV7v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrGeneralV8v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrGeneralV11v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsV4v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrNotificationV5v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrNotificationV8v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrV11v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrV6v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrV9v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrV11v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrV6v0Group"))
)
if mibBuilder.loadTexts:
    tmnxOamTr7xx0V11v0Compliance.setStatus(
        "current"
    )

tmnxOamTr7xx0V12v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 1, 14)
)
tmnxOamTr7xx0V12v0Compliance.setObjects(
    ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrV12v0Group")
)
if mibBuilder.loadTexts:
    tmnxOamTr7xx0V12v0Compliance.setStatus(
        "current"
    )

tmnxOamTr7xx0V13v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 1, 15)
)
tmnxOamTr7xx0V13v0Compliance.setObjects(
    ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrV13v0Group")
)
if mibBuilder.loadTexts:
    tmnxOamTr7xx0V13v0Compliance.setStatus(
        "current"
    )

tmnxOamTr7xx0V15v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 1, 17)
)
tmnxOamTr7xx0V15v0Compliance.setObjects(
    ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrV15v0Group")
)
if mibBuilder.loadTexts:
    tmnxOamTr7xx0V15v0Compliance.setStatus(
        "current"
    )

tmnxOamTr7xx0V19v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 1, 18)
)
tmnxOamTr7xx0V19v0Compliance.setObjects(
    ("TIMETRA-OAM-TEST-MIB", "tmnxOamTrV19v0Group")
)
if mibBuilder.loadTexts:
    tmnxOamTr7xx0V19v0Compliance.setStatus(
        "current"
    )

tmnxOamTr7xx0V20v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 1, 19)
)
tmnxOamTr7xx0V20v0Compliance.setObjects(
    ("TIMETRA-OAM-TEST-MIB", "tmnxOamBierTrV20v0Group")
)
if mibBuilder.loadTexts:
    tmnxOamTr7xx0V20v0Compliance.setStatus(
        "current"
    )

tmnxOamTr7xx0V21v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 1, 20)
)
tmnxOamTr7xx0V21v0Compliance.setObjects(
    ("TIMETRA-OAM-TEST-MIB", "tmnxOamIcmpTrV21v0Group")
)
if mibBuilder.loadTexts:
    tmnxOamTr7xx0V21v0Compliance.setStatus(
        "current"
    )

tmnxOamSaaV3v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 3, 1, 1)
)
tmnxOamSaaV3v0Compliance.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamSaaGeneralV3v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSaaThresholdV3v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSaaNotificationV3v0Group"))
)
if mibBuilder.loadTexts:
    tmnxOamSaaV3v0Compliance.setStatus(
        "obsolete"
    )

tmnxOamSaaV7v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 3, 1, 2)
)
tmnxOamSaaV7v0Compliance.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamSaaGeneralV7v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSaaThresholdV3v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSaaNotificationV3v0Group"))
)
if mibBuilder.loadTexts:
    tmnxOamSaaV7v0Compliance.setStatus(
        "obsolete"
    )

tmnxOamSaaV8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 3, 1, 3)
)
tmnxOamSaaV8v0Compliance.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamSaaGeneralV7v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSaaGeneralV8v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSaaThresholdV3v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSaaNotificationV3v0Group"))
)
if mibBuilder.loadTexts:
    tmnxOamSaaV8v0Compliance.setStatus(
        "obsolete"
    )

tmnxOamSaaV10v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 3, 1, 4)
)
tmnxOamSaaV10v0Compliance.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamSaaGeneralV7v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSaaGeneralV8v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSaaThresholdV3v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSaaNotificationV3v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamSaaGeneralV10v0Group"))
)
if mibBuilder.loadTexts:
    tmnxOamSaaV10v0Compliance.setStatus(
        "current"
    )

tmnxOamGeneralV8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 5, 1, 1)
)
tmnxOamGeneralV8v0Compliance.setObjects(
    ("TIMETRA-OAM-TEST-MIB", "tmnxOamGeneralV8v0Group")
)
if mibBuilder.loadTexts:
    tmnxOamGeneralV8v0Compliance.setStatus(
        "obsolete"
    )

tmnxOamGeneralV10v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 5, 1, 2)
)
tmnxOamGeneralV10v0Compliance.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamGeneralV8v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamGeneralV10v0Group"))
)
if mibBuilder.loadTexts:
    tmnxOamGeneralV10v0Compliance.setStatus(
        "current"
    )

tmnxOamGeneralV11v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 5, 1, 3)
)
tmnxOamGeneralV11v0Compliance.setObjects(
    ("TIMETRA-OAM-TEST-MIB", "tmnxOamGeneralV11v0Group")
)
if mibBuilder.loadTexts:
    tmnxOamGeneralV11v0Compliance.setStatus(
        "current"
    )

tmnxOamGeneralV14v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 5, 1, 6)
)
tmnxOamGeneralV14v0Compliance.setObjects(
    ("TIMETRA-OAM-TEST-MIB", "tmnxOamGeneralV14v0Group")
)
if mibBuilder.loadTexts:
    tmnxOamGeneralV14v0Compliance.setStatus(
        "current"
    )

tmnxOamGeneralV19v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 5, 1, 9)
)
tmnxOamGeneralV19v0Compliance.setObjects(
    ("TIMETRA-OAM-TEST-MIB", "tmnxOamGeneralV19v0Group")
)
if mibBuilder.loadTexts:
    tmnxOamGeneralV19v0Compliance.setStatus(
        "current"
    )

tmnxOamGeneralV20v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 5, 1, 10)
)
tmnxOamGeneralV20v0Compliance.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamGenPoolShareV20v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamGenPoolSplitV20v0Group"))
)
if mibBuilder.loadTexts:
    tmnxOamGeneralV20v0Compliance.setStatus(
        "current"
    )

tmnxOamDiagV16v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 6, 1, 1)
)
tmnxOamDiagV16v0Compliance.setObjects(
      *(("TIMETRA-OAM-TEST-MIB", "tmnxOamDiagNotificationV16v0Grp"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamDiagNotifyObjsV16v0Group"),
        ("TIMETRA-OAM-TEST-MIB", "tmnxOamDiagV16v0Group"))
)
if mibBuilder.loadTexts:
    tmnxOamDiagV16v0Compliance.setStatus(
        "current"
    )

tmnxOamIfPingV20v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 7, 1, 1)
)
tmnxOamIfPingV20v0Compliance.setObjects(
    ("TIMETRA-OAM-TEST-MIB", "tmnxOamIfPingV20v0Group")
)
if mibBuilder.loadTexts:
    tmnxOamIfPingV20v0Compliance.setStatus(
        "current"
    )

tmnxOamLnkMeasV21v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 8, 1, 1)
)
tmnxOamLnkMeasV21v0Compliance.setObjects(
    ("TIMETRA-OAM-TEST-MIB", "tmnxOamLnkMeasV21v0Group")
)
if mibBuilder.loadTexts:
    tmnxOamLnkMeasV21v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-OAM-TEST-MIB",
    **{"TmnxOamBierHistoryReturnCode": TmnxOamBierHistoryReturnCode,
       "TmnxOamBuildPktHeaderType": TmnxOamBuildPktHeaderType,
       "TmnxOamLspAssocChannel": TmnxOamLspAssocChannel,
       "TmnxOamLspTestSubMode": TmnxOamLspTestSubMode,
       "TmnxOamMplsEchoDownMapTlv": TmnxOamMplsEchoDownMapTlv,
       "TmnxOamMplsEchoDownMapTlvOrNone": TmnxOamMplsEchoDownMapTlvOrNone,
       "TmnxOamMplsTpPathType": TmnxOamMplsTpPathType,
       "TmnxOamTestMode": TmnxOamTestMode,
       "TmnxOamPingRtnCode": TmnxOamPingRtnCode,
       "TmnxOamAddressType": TmnxOamAddressType,
       "TmnxOamResponseStatus": TmnxOamResponseStatus,
       "TmnxOamSignalProtocol": TmnxOamSignalProtocol,
       "TmnxOamTestResponsePlane": TmnxOamTestResponsePlane,
       "TmnxOamSaaThreshold": TmnxOamSaaThreshold,
       "TmnxOamVccvAssocChannel": TmnxOamVccvAssocChannel,
       "TmnxOamVccvTestSubMode": TmnxOamVccvTestSubMode,
       "TmnxOamVccvSwitTgtFecType": TmnxOamVccvSwitTgtFecType,
       "TmnxOamVcType": TmnxOamVcType,
       "TmnxOamLTtraceDisStatusBits": TmnxOamLTtraceDisStatusBits,
       "TmnxOamTestResult": TmnxOamTestResult,
       "timetraOamTestMIBModule": timetraOamTestMIBModule,
       "tmnxOamTestConformance": tmnxOamTestConformance,
       "tmnxOamPingConformance": tmnxOamPingConformance,
       "tmnxOamPingCompliances": tmnxOamPingCompliances,
       "tmnxOamPing7450V4v0Compliance": tmnxOamPing7450V4v0Compliance,
       "tmnxOamPing7750V4v0Compliance": tmnxOamPing7750V4v0Compliance,
       "tmnxOamPing7450V5v0Compliance": tmnxOamPing7450V5v0Compliance,
       "tmnxOamPing7750V5v0Compliance": tmnxOamPing7750V5v0Compliance,
       "tmnxOamPing7450V6v0Compliance": tmnxOamPing7450V6v0Compliance,
       "tmnxOamPing7750V6v0Compliance": tmnxOamPing7750V6v0Compliance,
       "tmnxOamPing7450V7v0Compliance": tmnxOamPing7450V7v0Compliance,
       "tmnxOamPing7750V7v0Compliance": tmnxOamPing7750V7v0Compliance,
       "tmnxOamPing7450V8v0Compliance": tmnxOamPing7450V8v0Compliance,
       "tmnxOamPing77x0V8v0Compliance": tmnxOamPing77x0V8v0Compliance,
       "tmnxOamPing7xx0V9v0Compliance": tmnxOamPing7xx0V9v0Compliance,
       "tmnxOamPing7xx0V10v0Compliance": tmnxOamPing7xx0V10v0Compliance,
       "tmnxOamPing7xx0V11v0Compliance": tmnxOamPing7xx0V11v0Compliance,
       "tmnxOamPing7xx0V12v0Compliance": tmnxOamPing7xx0V12v0Compliance,
       "tmnxOamPing7xx0V13v0Compliance": tmnxOamPing7xx0V13v0Compliance,
       "tmnxOamPing7xx0V14v0Compliance": tmnxOamPing7xx0V14v0Compliance,
       "tmnxOamPing7xx0V15v0Compliance": tmnxOamPing7xx0V15v0Compliance,
       "tmnxOamPing7xx0V16v0Compliance": tmnxOamPing7xx0V16v0Compliance,
       "tmnxOamPing7xx0V19v0Compliance": tmnxOamPing7xx0V19v0Compliance,
       "tmnxOamPing7xx0V20v0Compliance": tmnxOamPing7xx0V20v0Compliance,
       "tmnxOamPingGroups": tmnxOamPingGroups,
       "tmnxOamMacPingL2MapGroup": tmnxOamMacPingL2MapGroup,
       "tmnxOamAtmPingR2r1Group": tmnxOamAtmPingR2r1Group,
       "tmnxOamMacPingV4v0Group": tmnxOamMacPingV4v0Group,
       "tmnxOamVccvPingGroup": tmnxOamVccvPingGroup,
       "tmnxOamPingGeneralV4v0Group": tmnxOamPingGeneralV4v0Group,
       "tmnxOamLspPingV4v0Group": tmnxOamLspPingV4v0Group,
       "tmnxOamVprnPingV4v0Group": tmnxOamVprnPingV4v0Group,
       "tmnxOamMfibPingV4v0Group": tmnxOamMfibPingV4v0Group,
       "tmnxOamCpePingV4v0Group": tmnxOamCpePingV4v0Group,
       "tmnxOamMRInfoV4v0Group": tmnxOamMRInfoV4v0Group,
       "tmnxOamIcmpPingGroup": tmnxOamIcmpPingGroup,
       "tmnxOamPingObsoleteV4v0Group": tmnxOamPingObsoleteV4v0Group,
       "tmnxOamPingNotificationV4v0Group": tmnxOamPingNotificationV4v0Group,
       "tmnxOamPingNotificationObsoleteV4v0Group": tmnxOamPingNotificationObsoleteV4v0Group,
       "tmnxOamLspPingV5v0Group": tmnxOamLspPingV5v0Group,
       "tmnxOamVccvPingV5v0Group": tmnxOamVccvPingV5v0Group,
       "tmnxOamAncpTestV5v0Group": tmnxOamAncpTestV5v0Group,
       "tmnxOamPingNotificationV5v0Group": tmnxOamPingNotificationV5v0Group,
       "tmnxOamMfibPingV6v0Group": tmnxOamMfibPingV6v0Group,
       "tmnxOamPingGeneralV6v0Group": tmnxOamPingGeneralV6v0Group,
       "tmnxOamP2mpLspPingGroup": tmnxOamP2mpLspPingGroup,
       "tmnxOamLspPingV6v0Group": tmnxOamLspPingV6v0Group,
       "tmnxOamPingGeneralV7v0Group": tmnxOamPingGeneralV7v0Group,
       "tmnxOamPingNotificationV7v0Group": tmnxOamPingNotificationV7v0Group,
       "tmnxOamPingObsoleteV6v0Group": tmnxOamPingObsoleteV6v0Group,
       "tmnxOamPingObsoleteV6v1Group": tmnxOamPingObsoleteV6v1Group,
       "tmnxOamEthCfmPingV8v0Group": tmnxOamEthCfmPingV8v0Group,
       "tmnxOamP2mpLspPingV8v0Group": tmnxOamP2mpLspPingV8v0Group,
       "tmnxOamPingGeneralV8v0Group": tmnxOamPingGeneralV8v0Group,
       "tmnxOamPingObsoleteV8v0Group": tmnxOamPingObsoleteV8v0Group,
       "tmnxOamVccvPingV9v0Group": tmnxOamVccvPingV9v0Group,
       "tmnxOamPingCtlV10v0Group": tmnxOamPingCtlV10v0Group,
       "tmnxOamMobilePingGroup": tmnxOamMobilePingGroup,
       "tmnxOamPingObsoleteV10v0Group": tmnxOamPingObsoleteV10v0Group,
       "tmnxOamPingGeneralV10v0Group": tmnxOamPingGeneralV10v0Group,
       "tmnxOamP2mpLspPingV10v0Group": tmnxOamP2mpLspPingV10v0Group,
       "tmnxOamPingObsoleteV11v0Group": tmnxOamPingObsoleteV11v0Group,
       "tmnxOamMacPingCtlV11v0Group": tmnxOamMacPingCtlV11v0Group,
       "tmnxOamMacPingHistoryV11v0Group": tmnxOamMacPingHistoryV11v0Group,
       "tmnxOamLspPingV11v0Group": tmnxOamLspPingV11v0Group,
       "tmnxOamVccvPingV11v0Group": tmnxOamVccvPingV11v0Group,
       "tmnxOamPingV11v0Group": tmnxOamPingV11v0Group,
       "tmnxOamPingV12v0Group": tmnxOamPingV12v0Group,
       "tmnxOamPingV13v0Group": tmnxOamPingV13v0Group,
       "tmnxOamPingObsoleteV14v0Group": tmnxOamPingObsoleteV14v0Group,
       "tmnxOamPingV14v0Group": tmnxOamPingV14v0Group,
       "tmnxOamPingV15v0Group": tmnxOamPingV15v0Group,
       "tmnxOamPingV16v0Group": tmnxOamPingV16v0Group,
       "tmnxOamPingObsoletedV16v0Group": tmnxOamPingObsoletedV16v0Group,
       "tmnxOamMobilePingV16v0Group": tmnxOamMobilePingV16v0Group,
       "tmnxOamPingV19v0ObjGroups": tmnxOamPingV19v0ObjGroups,
       "tmnxOamPingV19v0Group": tmnxOamPingV19v0Group,
       "tmnxOamPingV20v0ObjGroups": tmnxOamPingV20v0ObjGroups,
       "tmnxOamBierPingV20v0Group": tmnxOamBierPingV20v0Group,
       "tmnxOamIfPingObjGroups": tmnxOamIfPingObjGroups,
       "tmnxOamIfPingV20v0Group": tmnxOamIfPingV20v0Group,
       "tmnxOamLnkMeasObjsGroups": tmnxOamLnkMeasObjsGroups,
       "tmnxOamLnkMeasV21v0Group": tmnxOamLnkMeasV21v0Group,
       "tmnxOamTraceRouteConformance": tmnxOamTraceRouteConformance,
       "tmnxOamTrCompliances": tmnxOamTrCompliances,
       "tmnxOamTr7450V4v0Compliance": tmnxOamTr7450V4v0Compliance,
       "tmnxOamTr7750V4v0Compliance": tmnxOamTr7750V4v0Compliance,
       "tmnxOamTr7450V5v0Compliance": tmnxOamTr7450V5v0Compliance,
       "tmnxOamTr7750V5v0Compliance": tmnxOamTr7750V5v0Compliance,
       "tmnxOamTr7450V6v0Compliance": tmnxOamTr7450V6v0Compliance,
       "tmnxOamTr77x0V6v0Compliance": tmnxOamTr77x0V6v0Compliance,
       "tmnxOamTr7450V7v0Compliance": tmnxOamTr7450V7v0Compliance,
       "tmnxOamTr77x0V7v0Compliance": tmnxOamTr77x0V7v0Compliance,
       "tmnxOamTr7xx0V8v0Compliance": tmnxOamTr7xx0V8v0Compliance,
       "tmnxOamTr7xx0V9v0Compliance": tmnxOamTr7xx0V9v0Compliance,
       "tmnxOamTr7xx0V11v0Compliance": tmnxOamTr7xx0V11v0Compliance,
       "tmnxOamTr7xx0V12v0Compliance": tmnxOamTr7xx0V12v0Compliance,
       "tmnxOamTr7xx0V13v0Compliance": tmnxOamTr7xx0V13v0Compliance,
       "tmnxOamTr7xx0V15v0Compliance": tmnxOamTr7xx0V15v0Compliance,
       "tmnxOamTr7xx0V19v0Compliance": tmnxOamTr7xx0V19v0Compliance,
       "tmnxOamTr7xx0V20v0Compliance": tmnxOamTr7xx0V20v0Compliance,
       "tmnxOamTr7xx0V21v0Compliance": tmnxOamTr7xx0V21v0Compliance,
       "tmnxOamTrGroups": tmnxOamTrGroups,
       "tmnxOamMacTrV3v0Group": tmnxOamMacTrV3v0Group,
       "tmnxOamTrObsoleteV3v0Group": tmnxOamTrObsoleteV3v0Group,
       "tmnxOamTrGeneralV4v0Group": tmnxOamTrGeneralV4v0Group,
       "tmnxOamTrHopsV4v0Group": tmnxOamTrHopsV4v0Group,
       "tmnxOamLspTrV4v0Group": tmnxOamLspTrV4v0Group,
       "tmnxOamVprnTrV4v0Group": tmnxOamVprnTrV4v0Group,
       "tmnxOamMcastTrV4v0Group": tmnxOamMcastTrV4v0Group,
       "tmnxOamTrObsoleteV4v0Group": tmnxOamTrObsoleteV4v0Group,
       "tmnxOamTrNotificationV4v0Group": tmnxOamTrNotificationV4v0Group,
       "tmnxOamLspTrV5v0Group": tmnxOamLspTrV5v0Group,
       "tmnxOamTrObsoleteV5v0Group": tmnxOamTrObsoleteV5v0Group,
       "tmnxOamTrGeneralV5v0Group": tmnxOamTrGeneralV5v0Group,
       "tmnxOamTrNotificationV5v0Group": tmnxOamTrNotificationV5v0Group,
       "tmnxOamVccvTrV6v0Group": tmnxOamVccvTrV6v0Group,
       "tmnxOamVprnTrObsoleteV6v0Group": tmnxOamVprnTrObsoleteV6v0Group,
       "tmnxOamVprnTrV6v0Group": tmnxOamVprnTrV6v0Group,
       "tmnxOamP2mpLspTraceGroup": tmnxOamP2mpLspTraceGroup,
       "tmnxOamTrGeneralV6v0Group": tmnxOamTrGeneralV6v0Group,
       "tmnxOamTrObsoleteV6v0Group": tmnxOamTrObsoleteV6v0Group,
       "tmnxOamTrGeneralV7v0Group": tmnxOamTrGeneralV7v0Group,
       "tmnxOamEthCfmTrV8v0Group": tmnxOamEthCfmTrV8v0Group,
       "tmnxOamLspTrV6v0Group": tmnxOamLspTrV6v0Group,
       "tmnxOamTrGeneralV8v0Group": tmnxOamTrGeneralV8v0Group,
       "tmnxOamTrNotificationV8v0Group": tmnxOamTrNotificationV8v0Group,
       "tmnxOamVccvTrV9v0Group": tmnxOamVccvTrV9v0Group,
       "tmnxOamLTtraceV9v0Group": tmnxOamLTtraceV9v0Group,
       "tmnxOamTrGeneralV11v0Group": tmnxOamTrGeneralV11v0Group,
       "tmnxOamVccvTrV11v0Group": tmnxOamVccvTrV11v0Group,
       "tmnxOamTrV11v0Group": tmnxOamTrV11v0Group,
       "tmnxOamTrV12v0Group": tmnxOamTrV12v0Group,
       "tmnxOamTrObsoleteV13v0Group": tmnxOamTrObsoleteV13v0Group,
       "tmnxOamTrV13v0Group": tmnxOamTrV13v0Group,
       "tmnxOamTrObsoleteV14v0Group": tmnxOamTrObsoleteV14v0Group,
       "tmnxOamTrV15v0Group": tmnxOamTrV15v0Group,
       "tmnxOamTrV16v0Group": tmnxOamTrV16v0Group,
       "tmnxOamTrV19v0ObjGroups": tmnxOamTrV19v0ObjGroups,
       "tmnxOamTrV19v0Group": tmnxOamTrV19v0Group,
       "tmnxOamTrV20v0ObjGroups": tmnxOamTrV20v0ObjGroups,
       "tmnxOamBierTrV20v0Group": tmnxOamBierTrV20v0Group,
       "tmnxOamTrV21v0ObjGroups": tmnxOamTrV21v0ObjGroups,
       "tmnxOamIcmpTrV21v0Group": tmnxOamIcmpTrV21v0Group,
       "tmnxOamSaaConformance": tmnxOamSaaConformance,
       "tmnxOamSaaCompliances": tmnxOamSaaCompliances,
       "tmnxOamSaaV3v0Compliance": tmnxOamSaaV3v0Compliance,
       "tmnxOamSaaV7v0Compliance": tmnxOamSaaV7v0Compliance,
       "tmnxOamSaaV8v0Compliance": tmnxOamSaaV8v0Compliance,
       "tmnxOamSaaV10v0Compliance": tmnxOamSaaV10v0Compliance,
       "tmnxOamSaaGroups": tmnxOamSaaGroups,
       "tmnxOamSaaGeneralV3v0Group": tmnxOamSaaGeneralV3v0Group,
       "tmnxOamSaaThresholdV3v0Group": tmnxOamSaaThresholdV3v0Group,
       "tmnxOamSaaNotificationV3v0Group": tmnxOamSaaNotificationV3v0Group,
       "tmnxOamSaaGeneralV7v0Group": tmnxOamSaaGeneralV7v0Group,
       "tmnxOamSaaGeneralV8v0Group": tmnxOamSaaGeneralV8v0Group,
       "tmnxOamSaaGeneralV10v0Group": tmnxOamSaaGeneralV10v0Group,
       "tmnxOamSaaObsoleteV14v0Group": tmnxOamSaaObsoleteV14v0Group,
       "tmnxOamMobGatewayConformance": tmnxOamMobGatewayConformance,
       "tmnxOamGeneralConformance": tmnxOamGeneralConformance,
       "tmnxOamGeneralCompliances": tmnxOamGeneralCompliances,
       "tmnxOamGeneralV8v0Compliance": tmnxOamGeneralV8v0Compliance,
       "tmnxOamGeneralV10v0Compliance": tmnxOamGeneralV10v0Compliance,
       "tmnxOamGeneralV11v0Compliance": tmnxOamGeneralV11v0Compliance,
       "tmnxOamGeneralV14v0Compliance": tmnxOamGeneralV14v0Compliance,
       "tmnxOamGeneralV19v0Compliance": tmnxOamGeneralV19v0Compliance,
       "tmnxOamGeneralV20v0Compliance": tmnxOamGeneralV20v0Compliance,
       "tmnxOamGeneralGroups": tmnxOamGeneralGroups,
       "tmnxOamGeneralV8v0Group": tmnxOamGeneralV8v0Group,
       "tmnxOamGeneralV10v0Group": tmnxOamGeneralV10v0Group,
       "tmnxOamGeneralV11v0Group": tmnxOamGeneralV11v0Group,
       "tmnxOamGeneralV14v0Group": tmnxOamGeneralV14v0Group,
       "tmnxOamGeneralV19v0Group": tmnxOamGeneralV19v0Group,
       "tmnxOamGenPoolSplitV20v0Group": tmnxOamGenPoolSplitV20v0Group,
       "tmnxOamGenPoolShareV20v0Group": tmnxOamGenPoolShareV20v0Group,
       "tmnxOamGenObsoletedV21v0Group": tmnxOamGenObsoletedV21v0Group,
       "tmnxOamDiagConformance": tmnxOamDiagConformance,
       "tmnxOamDiagCompliances": tmnxOamDiagCompliances,
       "tmnxOamDiagV16v0Compliance": tmnxOamDiagV16v0Compliance,
       "tmnxOamDiagGroups": tmnxOamDiagGroups,
       "tmnxOamDiagV16v0Group": tmnxOamDiagV16v0Group,
       "tmnxOamDiagNotificationV16v0Grp": tmnxOamDiagNotificationV16v0Grp,
       "tmnxOamDiagNotifyObjsV16v0Group": tmnxOamDiagNotifyObjsV16v0Group,
       "tmnxOamIfPingConformance": tmnxOamIfPingConformance,
       "tmnxOamIfPingCompliances": tmnxOamIfPingCompliances,
       "tmnxOamIfPingV20v0Compliance": tmnxOamIfPingV20v0Compliance,
       "tmnxOamLnkMeasConformance": tmnxOamLnkMeasConformance,
       "tmnxOamLnkMeasCompliances": tmnxOamLnkMeasCompliances,
       "tmnxOamLnkMeasV21v0Compliance": tmnxOamLnkMeasV21v0Compliance,
       "tmnxOamTestObjs": tmnxOamTestObjs,
       "tmnxOamPingObjs": tmnxOamPingObjs,
       "tmnxOamPingNotificationObjects": tmnxOamPingNotificationObjects,
       "tmnxOamPingMaxConcurrentTests": tmnxOamPingMaxConcurrentTests,
       "tmnxOamPingCtlTable": tmnxOamPingCtlTable,
       "tmnxOamPingCtlEntry": tmnxOamPingCtlEntry,
       "tmnxOamPingCtlOwnerIndex": tmnxOamPingCtlOwnerIndex,
       "tmnxOamPingCtlTestIndex": tmnxOamPingCtlTestIndex,
       "tmnxOamPingCtlRowStatus": tmnxOamPingCtlRowStatus,
       "tmnxOamPingCtlStorageType": tmnxOamPingCtlStorageType,
       "tmnxOamPingCtlDescr": tmnxOamPingCtlDescr,
       "tmnxOamPingCtlTestMode": tmnxOamPingCtlTestMode,
       "tmnxOamPingCtlAdminStatus": tmnxOamPingCtlAdminStatus,
       "tmnxOamPingCtlOrigSdpId": tmnxOamPingCtlOrigSdpId,
       "tmnxOamPingCtlRespSdpId": tmnxOamPingCtlRespSdpId,
       "tmnxOamPingCtlFcName": tmnxOamPingCtlFcName,
       "tmnxOamPingCtlProfile": tmnxOamPingCtlProfile,
       "tmnxOamPingCtlMtuStartSize": tmnxOamPingCtlMtuStartSize,
       "tmnxOamPingCtlMtuEndSize": tmnxOamPingCtlMtuEndSize,
       "tmnxOamPingCtlMtuStepSize": tmnxOamPingCtlMtuStepSize,
       "tmnxOamPingCtlTargetIpAddress": tmnxOamPingCtlTargetIpAddress,
       "tmnxOamPingCtlServiceId": tmnxOamPingCtlServiceId,
       "tmnxOamPingCtlLocalSdp": tmnxOamPingCtlLocalSdp,
       "tmnxOamPingCtlRemoteSdp": tmnxOamPingCtlRemoteSdp,
       "tmnxOamPingCtlSize": tmnxOamPingCtlSize,
       "tmnxOamPingCtlTimeOut": tmnxOamPingCtlTimeOut,
       "tmnxOamPingCtlProbeCount": tmnxOamPingCtlProbeCount,
       "tmnxOamPingCtlInterval": tmnxOamPingCtlInterval,
       "tmnxOamPingCtlMaxRows": tmnxOamPingCtlMaxRows,
       "tmnxOamPingCtlTrapGeneration": tmnxOamPingCtlTrapGeneration,
       "tmnxOamPingCtlTrapProbeFailureFilter": tmnxOamPingCtlTrapProbeFailureFilter,
       "tmnxOamPingCtlTrapTestFailureFilter": tmnxOamPingCtlTrapTestFailureFilter,
       "tmnxOamPingCtlSAA": tmnxOamPingCtlSAA,
       "tmnxOamPingCtlRuns": tmnxOamPingCtlRuns,
       "tmnxOamPingCtlFailures": tmnxOamPingCtlFailures,
       "tmnxOamPingCtlLastRunResult": tmnxOamPingCtlLastRunResult,
       "tmnxOamPingCtlLastChanged": tmnxOamPingCtlLastChanged,
       "tmnxOamPingCtlVRtrID": tmnxOamPingCtlVRtrID,
       "tmnxOamPingCtlTgtAddrType": tmnxOamPingCtlTgtAddrType,
       "tmnxOamPingCtlTgtAddress": tmnxOamPingCtlTgtAddress,
       "tmnxOamPingCtlSrcAddrType": tmnxOamPingCtlSrcAddrType,
       "tmnxOamPingCtlSrcAddress": tmnxOamPingCtlSrcAddress,
       "tmnxOamPingCtlDnsName": tmnxOamPingCtlDnsName,
       "tmnxOamPingCtlDNSRecord": tmnxOamPingCtlDNSRecord,
       "tmnxOamPingCtlIntervalUnits": tmnxOamPingCtlIntervalUnits,
       "tmnxOamPingCtlSubscriberName": tmnxOamPingCtlSubscriberName,
       "tmnxOamPingCtlRouterInstanceName": tmnxOamPingCtlRouterInstanceName,
       "tmnxOamPingResultsTable": tmnxOamPingResultsTable,
       "tmnxOamPingResultsEntry": tmnxOamPingResultsEntry,
       "tmnxOamPingResultsOperStatus": tmnxOamPingResultsOperStatus,
       "tmnxOamPingResultsMinRtt": tmnxOamPingResultsMinRtt,
       "tmnxOamPingResultsMaxRtt": tmnxOamPingResultsMaxRtt,
       "tmnxOamPingResultsAverageRtt": tmnxOamPingResultsAverageRtt,
       "tmnxOamPingResultsRttSumOfSquares": tmnxOamPingResultsRttSumOfSquares,
       "tmnxOamPingResultsMtuResponseSize": tmnxOamPingResultsMtuResponseSize,
       "tmnxOamPingResultsSvcPing": tmnxOamPingResultsSvcPing,
       "tmnxOamPingResultsProbeResponses": tmnxOamPingResultsProbeResponses,
       "tmnxOamPingResultsSentProbes": tmnxOamPingResultsSentProbes,
       "tmnxOamPingResultsLastGoodProbe": tmnxOamPingResultsLastGoodProbe,
       "tmnxOamPingResultsLastRespHeader": tmnxOamPingResultsLastRespHeader,
       "tmnxOamPingResultsMinTt": tmnxOamPingResultsMinTt,
       "tmnxOamPingResultsMaxTt": tmnxOamPingResultsMaxTt,
       "tmnxOamPingResultsAverageTt": tmnxOamPingResultsAverageTt,
       "tmnxOamPingResultsTtSumOfSquares": tmnxOamPingResultsTtSumOfSquares,
       "tmnxOamPingResultsMinInTt": tmnxOamPingResultsMinInTt,
       "tmnxOamPingResultsMaxInTt": tmnxOamPingResultsMaxInTt,
       "tmnxOamPingResultsAverageInTt": tmnxOamPingResultsAverageInTt,
       "tmnxOamPingResultsInTtSumOfSqrs": tmnxOamPingResultsInTtSumOfSqrs,
       "tmnxOamPingResultsOutJitter": tmnxOamPingResultsOutJitter,
       "tmnxOamPingResultsInJitter": tmnxOamPingResultsInJitter,
       "tmnxOamPingResultsRtJitter": tmnxOamPingResultsRtJitter,
       "tmnxOamPingResultsProbeTimeouts": tmnxOamPingResultsProbeTimeouts,
       "tmnxOamPingResultsProbeFailures": tmnxOamPingResultsProbeFailures,
       "tmnxOamPingResultsTestRunIndex": tmnxOamPingResultsTestRunIndex,
       "tmnxOamPingResultsRttOFSumSquares": tmnxOamPingResultsRttOFSumSquares,
       "tmnxOamPingResultsRttHCSumSquares": tmnxOamPingResultsRttHCSumSquares,
       "tmnxOamPingResultsTtOFSumSquares": tmnxOamPingResultsTtOFSumSquares,
       "tmnxOamPingResultsTtHCSumSquares": tmnxOamPingResultsTtHCSumSquares,
       "tmnxOamPingResultsInTtOFSumSqrs": tmnxOamPingResultsInTtOFSumSqrs,
       "tmnxOamPingResultsInTtHCSumSqrs": tmnxOamPingResultsInTtHCSumSqrs,
       "tmnxOamPingResultsTestRunResult": tmnxOamPingResultsTestRunResult,
       "tmnxOamPingResultsOutOfOrder": tmnxOamPingResultsOutOfOrder,
       "tmnxOamPingHistoryTable": tmnxOamPingHistoryTable,
       "tmnxOamPingHistoryEntry": tmnxOamPingHistoryEntry,
       "tmnxOamPingHistoryIndex": tmnxOamPingHistoryIndex,
       "tmnxOamPingHistoryResponse": tmnxOamPingHistoryResponse,
       "tmnxOamPingHistoryOneWayTime": tmnxOamPingHistoryOneWayTime,
       "tmnxOamPingHistorySize": tmnxOamPingHistorySize,
       "tmnxOamPingHistoryStatus": tmnxOamPingHistoryStatus,
       "tmnxOamPingHistoryTime": tmnxOamPingHistoryTime,
       "tmnxOamPingHistoryReturnCode": tmnxOamPingHistoryReturnCode,
       "tmnxOamPingHistorySrcIpAddress": tmnxOamPingHistorySrcIpAddress,
       "tmnxOamPingHistAddressType": tmnxOamPingHistAddressType,
       "tmnxOamPingHistSapId": tmnxOamPingHistSapId,
       "tmnxOamPingHistoryVersion": tmnxOamPingHistoryVersion,
       "tmnxOamPingHistoryCpeMacAddr": tmnxOamPingHistoryCpeMacAddr,
       "tmnxOamPingHistoryRespSvcId": tmnxOamPingHistoryRespSvcId,
       "tmnxOamPingHistorySequence": tmnxOamPingHistorySequence,
       "tmnxOamPingHistoryIfIndex": tmnxOamPingHistoryIfIndex,
       "tmnxOamPingHistoryDataLen": tmnxOamPingHistoryDataLen,
       "tmnxOamPingHistoryRespPlane": tmnxOamPingHistoryRespPlane,
       "tmnxOamPingHistoryReqHdr": tmnxOamPingHistoryReqHdr,
       "tmnxOamPingHistoryRespHdr": tmnxOamPingHistoryRespHdr,
       "tmnxOamPingHistoryDnsAddrType": tmnxOamPingHistoryDnsAddrType,
       "tmnxOamPingHistoryDnsAddress": tmnxOamPingHistoryDnsAddress,
       "tmnxOamPingHistorySrcAddrType": tmnxOamPingHistorySrcAddrType,
       "tmnxOamPingHistorySrcAddress": tmnxOamPingHistorySrcAddress,
       "tmnxOamPingHistoryInOneWayTime": tmnxOamPingHistoryInOneWayTime,
       "tmnxOamPingHistoryLspName": tmnxOamPingHistoryLspName,
       "tmnxOamPingHistNextHopAddrType": tmnxOamPingHistNextHopAddrType,
       "tmnxOamPingHistNextHopAddress": tmnxOamPingHistNextHopAddress,
       "tmnxOamPingHistorySrcGlobalId": tmnxOamPingHistorySrcGlobalId,
       "tmnxOamPingHistorySrcNodeId": tmnxOamPingHistorySrcNodeId,
       "tmnxOamPingHistorySdpBindId": tmnxOamPingHistorySdpBindId,
       "tmnxOamPingHistoryRtrnSubcode": tmnxOamPingHistoryRtrnSubcode,
       "tmnxOamPingHistoryNetworkIfName": tmnxOamPingHistoryNetworkIfName,
       "tmnxOamMacPingCtlTable": tmnxOamMacPingCtlTable,
       "tmnxOamMacPingCtlEntry": tmnxOamMacPingCtlEntry,
       "tmnxOamMacPingCtlTargetMacAddr": tmnxOamMacPingCtlTargetMacAddr,
       "tmnxOamMacPingCtlSourceMacAddr": tmnxOamMacPingCtlSourceMacAddr,
       "tmnxOamMacPingCtlSendControl": tmnxOamMacPingCtlSendControl,
       "tmnxOamMacPingCtlReplyControl": tmnxOamMacPingCtlReplyControl,
       "tmnxOamMacPingCtlTtl": tmnxOamMacPingCtlTtl,
       "tmnxOamMacPingCtlRegister": tmnxOamMacPingCtlRegister,
       "tmnxOamMacPingCtlFlood": tmnxOamMacPingCtlFlood,
       "tmnxOamMacPingCtlForce": tmnxOamMacPingCtlForce,
       "tmnxOamMacPingCtlAge": tmnxOamMacPingCtlAge,
       "tmnxOamMacPingCtlSapPortId": tmnxOamMacPingCtlSapPortId,
       "tmnxOamMacPingCtlSapEncapValue": tmnxOamMacPingCtlSapEncapValue,
       "tmnxOamMacPingCtlFibEntryName": tmnxOamMacPingCtlFibEntryName,
       "tmnxOamMacPingHistoryTable": tmnxOamMacPingHistoryTable,
       "tmnxOamMacPingHistoryEntry": tmnxOamMacPingHistoryEntry,
       "tmnxOamMacPingHistoryIndex": tmnxOamMacPingHistoryIndex,
       "tmnxOamMacPingReplyIndex": tmnxOamMacPingReplyIndex,
       "tmnxOamMacPingHistoryResponse": tmnxOamMacPingHistoryResponse,
       "tmnxOamMacPingHistoryOneWayTime": tmnxOamMacPingHistoryOneWayTime,
       "tmnxOamMacPingHistoryStatus": tmnxOamMacPingHistoryStatus,
       "tmnxOamMacPingHistoryTime": tmnxOamMacPingHistoryTime,
       "tmnxOamMacPingHistoryReturnCode": tmnxOamMacPingHistoryReturnCode,
       "tmnxOamMacPingHistorySrcIpAddress": tmnxOamMacPingHistorySrcIpAddress,
       "tmnxOamMacPingHistoryAddressType": tmnxOamMacPingHistoryAddressType,
       "tmnxOamMacPingHistorySapId": tmnxOamMacPingHistorySapId,
       "tmnxOamMacPingHistorySdpId": tmnxOamMacPingHistorySdpId,
       "tmnxOamMacPingHistoryAdminStatus": tmnxOamMacPingHistoryAdminStatus,
       "tmnxOamMacPingHistoryOperStatus": tmnxOamMacPingHistoryOperStatus,
       "tmnxOamMacPingHistoryResponsePlane": tmnxOamMacPingHistoryResponsePlane,
       "tmnxOamMacPingHistorySize": tmnxOamMacPingHistorySize,
       "tmnxOamMacPingHistoryInOneWayTime": tmnxOamMacPingHistoryInOneWayTime,
       "tmnxOamMacPingHistorySrcAddrType": tmnxOamMacPingHistorySrcAddrType,
       "tmnxOamMacPingHistorySrcAddress": tmnxOamMacPingHistorySrcAddress,
       "tmnxOamMacPingL2MapTable": tmnxOamMacPingL2MapTable,
       "tmnxOamMacPingL2MapEntry": tmnxOamMacPingL2MapEntry,
       "tmnxOamMacPingL2MapIndex": tmnxOamMacPingL2MapIndex,
       "tmnxOamMacPingL2MapRouterID": tmnxOamMacPingL2MapRouterID,
       "tmnxOamMacPingL2MapLabel": tmnxOamMacPingL2MapLabel,
       "tmnxOamMacPingL2MapProtocol": tmnxOamMacPingL2MapProtocol,
       "tmnxOamMacPingL2MapVCType": tmnxOamMacPingL2MapVCType,
       "tmnxOamMacPingL2MapVCID": tmnxOamMacPingL2MapVCID,
       "tmnxOamMacPingL2MapDirection": tmnxOamMacPingL2MapDirection,
       "tmnxOamLspPingCtlTable": tmnxOamLspPingCtlTable,
       "tmnxOamLspPingCtlEntry": tmnxOamLspPingCtlEntry,
       "tmnxOamLspPingCtlVRtrID": tmnxOamLspPingCtlVRtrID,
       "tmnxOamLspPingCtlLspName": tmnxOamLspPingCtlLspName,
       "tmnxOamLspPingCtlReturnLsp": tmnxOamLspPingCtlReturnLsp,
       "tmnxOamLspPingCtlTtl": tmnxOamLspPingCtlTtl,
       "tmnxOamLspPingCtlPathName": tmnxOamLspPingCtlPathName,
       "tmnxOamLspPingCtlLdpIpPrefix": tmnxOamLspPingCtlLdpIpPrefix,
       "tmnxOamLspPingCtlLdpIpPrefixLen": tmnxOamLspPingCtlLdpIpPrefixLen,
       "tmnxOamLspPingCtlLdpPrefixType": tmnxOamLspPingCtlLdpPrefixType,
       "tmnxOamLspPingCtlLdpPrefix": tmnxOamLspPingCtlLdpPrefix,
       "tmnxOamLspPingCtlLdpPrefixLen": tmnxOamLspPingCtlLdpPrefixLen,
       "tmnxOamLspPingCtlPathDestType": tmnxOamLspPingCtlPathDestType,
       "tmnxOamLspPingCtlPathDest": tmnxOamLspPingCtlPathDest,
       "tmnxOamLspPingCtlNhIntfName": tmnxOamLspPingCtlNhIntfName,
       "tmnxOamLspPingCtlNhAddressType": tmnxOamLspPingCtlNhAddressType,
       "tmnxOamLspPingCtlNhAddress": tmnxOamLspPingCtlNhAddress,
       "tmnxOamLspPingCtlTestSubMode": tmnxOamLspPingCtlTestSubMode,
       "tmnxOamLspPingCtlMplsTpPathType": tmnxOamLspPingCtlMplsTpPathType,
       "tmnxOamLspPingCtlMplsTpGlobalId": tmnxOamLspPingCtlMplsTpGlobalId,
       "tmnxOamLspPingCtlMplsTpNodeId": tmnxOamLspPingCtlMplsTpNodeId,
       "tmnxOamLspPingCtlAssocChannel": tmnxOamLspPingCtlAssocChannel,
       "tmnxOamLspPingCtlForce": tmnxOamLspPingCtlForce,
       "tmnxOamLspPingCtlIgpInstance": tmnxOamLspPingCtlIgpInstance,
       "tmnxOamLspPingCtlSrPlcyColor": tmnxOamLspPingCtlSrPlcyColor,
       "tmnxOamLspPingCtlSrPlcyEndPtAddT": tmnxOamLspPingCtlSrPlcyEndPtAddT,
       "tmnxOamLspPingCtlSrPlcyEndPtAddr": tmnxOamLspPingCtlSrPlcyEndPtAddr,
       "tmnxOamLspPingCtlSrPlcySegList": tmnxOamLspPingCtlSrPlcySegList,
       "tmnxOamVprnPingCtlTable": tmnxOamVprnPingCtlTable,
       "tmnxOamVprnPingCtlEntry": tmnxOamVprnPingCtlEntry,
       "tmnxOamVprnPingCtlSourceIpAddr": tmnxOamVprnPingCtlSourceIpAddr,
       "tmnxOamVprnPingCtlReplyControl": tmnxOamVprnPingCtlReplyControl,
       "tmnxOamVprnPingCtlTtl": tmnxOamVprnPingCtlTtl,
       "tmnxOamVprnPingCtlSrcAddrType": tmnxOamVprnPingCtlSrcAddrType,
       "tmnxOamVprnPingCtlSrcAddress": tmnxOamVprnPingCtlSrcAddress,
       "tmnxOamAtmPingCtlTable": tmnxOamAtmPingCtlTable,
       "tmnxOamAtmPingCtlEntry": tmnxOamAtmPingCtlEntry,
       "tmnxOamAtmPingCtlPortId": tmnxOamAtmPingCtlPortId,
       "tmnxOamAtmPingCtlVpi": tmnxOamAtmPingCtlVpi,
       "tmnxOamAtmPingCtlVci": tmnxOamAtmPingCtlVci,
       "tmnxOamAtmPingCtlLpbkLocation": tmnxOamAtmPingCtlLpbkLocation,
       "tmnxOamAtmPingCtlSegment": tmnxOamAtmPingCtlSegment,
       "tmnxOamMfibPingCtlTable": tmnxOamMfibPingCtlTable,
       "tmnxOamMfibPingCtlEntry": tmnxOamMfibPingCtlEntry,
       "tmnxOamMfibPingCtlSourceIpAddr": tmnxOamMfibPingCtlSourceIpAddr,
       "tmnxOamMfibPingCtlDestIpAddr": tmnxOamMfibPingCtlDestIpAddr,
       "tmnxOamMfibPingCtlReplyControl": tmnxOamMfibPingCtlReplyControl,
       "tmnxOamMfibPingCtlTtl": tmnxOamMfibPingCtlTtl,
       "tmnxOamMfibPingCtlSrcAddrType": tmnxOamMfibPingCtlSrcAddrType,
       "tmnxOamMfibPingCtlSrcAddress": tmnxOamMfibPingCtlSrcAddress,
       "tmnxOamMfibPingCtlDestAddrType": tmnxOamMfibPingCtlDestAddrType,
       "tmnxOamMfibPingCtlDestAddress": tmnxOamMfibPingCtlDestAddress,
       "tmnxOamMfibPingCtlDestMacAddr": tmnxOamMfibPingCtlDestMacAddr,
       "tmnxOamCpePingCtlTable": tmnxOamCpePingCtlTable,
       "tmnxOamCpePingCtlEntry": tmnxOamCpePingCtlEntry,
       "tmnxOamCpePingCtlSourceIpAddr": tmnxOamCpePingCtlSourceIpAddr,
       "tmnxOamCpePingCtlSendControl": tmnxOamCpePingCtlSendControl,
       "tmnxOamCpePingCtlReplyControl": tmnxOamCpePingCtlReplyControl,
       "tmnxOamCpePingCtlTtl": tmnxOamCpePingCtlTtl,
       "tmnxOamCpePingCtlSrceMacAddr": tmnxOamCpePingCtlSrceMacAddr,
       "tmnxOamCpePingCtlSrcAddrType": tmnxOamCpePingCtlSrcAddrType,
       "tmnxOamCpePingCtlSrcAddress": tmnxOamCpePingCtlSrcAddress,
       "tmnxOamMRInfoRespTable": tmnxOamMRInfoRespTable,
       "tmnxOamMRInfoRespEntry": tmnxOamMRInfoRespEntry,
       "tmnxOamMRInfoRespCapabilities": tmnxOamMRInfoRespCapabilities,
       "tmnxOamMRInfoRespMinorVersion": tmnxOamMRInfoRespMinorVersion,
       "tmnxOamMRInfoRespMajorVersion": tmnxOamMRInfoRespMajorVersion,
       "tmnxOamMRInfoRespNumInterfaces": tmnxOamMRInfoRespNumInterfaces,
       "tmnxOamMRInfoRespIfTable": tmnxOamMRInfoRespIfTable,
       "tmnxOamMRInfoRespIfEntry": tmnxOamMRInfoRespIfEntry,
       "tmnxOamMRInfoRespIfIndex": tmnxOamMRInfoRespIfIndex,
       "tmnxOamMRInfoRespIfAddress": tmnxOamMRInfoRespIfAddress,
       "tmnxOamMRInfoRespIfMetric": tmnxOamMRInfoRespIfMetric,
       "tmnxOamMRInfoRespIfThreshold": tmnxOamMRInfoRespIfThreshold,
       "tmnxOamMRInfoRespIfFlags": tmnxOamMRInfoRespIfFlags,
       "tmnxOamMRInfoRespIfNbrCount": tmnxOamMRInfoRespIfNbrCount,
       "tmnxOamMRInfoRespIfAddrType": tmnxOamMRInfoRespIfAddrType,
       "tmnxOamMRInfoRespIfAddr": tmnxOamMRInfoRespIfAddr,
       "tmnxOamMRInfoRespIfNbrTable": tmnxOamMRInfoRespIfNbrTable,
       "tmnxOamMRInfoRespIfNbrEntry": tmnxOamMRInfoRespIfNbrEntry,
       "tmnxOamMRInfoRespIfNbrIndex": tmnxOamMRInfoRespIfNbrIndex,
       "tmnxOamMRInfoRespIfNbrAddress": tmnxOamMRInfoRespIfNbrAddress,
       "tmnxOamMRInfoRespIfNbrAddrType": tmnxOamMRInfoRespIfNbrAddrType,
       "tmnxOamMRInfoRespIfNbrAddr": tmnxOamMRInfoRespIfNbrAddr,
       "tmnxOamVccvPingCtlTable": tmnxOamVccvPingCtlTable,
       "tmnxOamVccvPingCtlEntry": tmnxOamVccvPingCtlEntry,
       "tmnxOamVccvPingCtlSdpIdVcId": tmnxOamVccvPingCtlSdpIdVcId,
       "tmnxOamVccvPingCtlReplyMode": tmnxOamVccvPingCtlReplyMode,
       "tmnxOamVccvPingCtlPwId": tmnxOamVccvPingCtlPwId,
       "tmnxOamVccvPingCtlTtl": tmnxOamVccvPingCtlTtl,
       "tmnxOamVccvPingCtlSpokeSdpId": tmnxOamVccvPingCtlSpokeSdpId,
       "tmnxOamVccvPingCtlSaiiGlobalId": tmnxOamVccvPingCtlSaiiGlobalId,
       "tmnxOamVccvPingCtlSaiiPrefix": tmnxOamVccvPingCtlSaiiPrefix,
       "tmnxOamVccvPingCtlSaiiAcId": tmnxOamVccvPingCtlSaiiAcId,
       "tmnxOamVccvPingCtlTaiiGlobalId": tmnxOamVccvPingCtlTaiiGlobalId,
       "tmnxOamVccvPingCtlTaiiPrefix": tmnxOamVccvPingCtlTaiiPrefix,
       "tmnxOamVccvPingCtlTaiiAcId": tmnxOamVccvPingCtlTaiiAcId,
       "tmnxOamVccvPingCtlMplsTpGlobalId": tmnxOamVccvPingCtlMplsTpGlobalId,
       "tmnxOamVccvPingCtlMplsTpNodeId": tmnxOamVccvPingCtlMplsTpNodeId,
       "tmnxOamVccvPingCtlTestSubMode": tmnxOamVccvPingCtlTestSubMode,
       "tmnxOamVccvPingCtlAssocChannel": tmnxOamVccvPingCtlAssocChannel,
       "tmnxOamVccvPingCtlSwitTgtFecType": tmnxOamVccvPingCtlSwitTgtFecType,
       "tmnxOamIcmpPingCtlTable": tmnxOamIcmpPingCtlTable,
       "tmnxOamIcmpPingCtlEntry": tmnxOamIcmpPingCtlEntry,
       "tmnxOamIcmpPingCtlRapid": tmnxOamIcmpPingCtlRapid,
       "tmnxOamIcmpPingCtlTtl": tmnxOamIcmpPingCtlTtl,
       "tmnxOamIcmpPingCtlDSField": tmnxOamIcmpPingCtlDSField,
       "tmnxOamIcmpPingCtlPattern": tmnxOamIcmpPingCtlPattern,
       "tmnxOamIcmpPingCtlNhAddrType": tmnxOamIcmpPingCtlNhAddrType,
       "tmnxOamIcmpPingCtlNhAddress": tmnxOamIcmpPingCtlNhAddress,
       "tmnxOamIcmpPingCtlEgrIfIndex": tmnxOamIcmpPingCtlEgrIfIndex,
       "tmnxOamIcmpPingCtlBypassRouting": tmnxOamIcmpPingCtlBypassRouting,
       "tmnxOamIcmpPingCtlDoNotFragment": tmnxOamIcmpPingCtlDoNotFragment,
       "tmnxOamIcmpPingCtlEgrIfName": tmnxOamIcmpPingCtlEgrIfName,
       "tmnxOamAncpTestCtlTable": tmnxOamAncpTestCtlTable,
       "tmnxOamAncpTestCtlEntry": tmnxOamAncpTestCtlEntry,
       "tmnxOamAncpTestTarget": tmnxOamAncpTestTarget,
       "tmnxOamAncpTestTargetId": tmnxOamAncpTestTargetId,
       "tmnxOamAncpTestcount": tmnxOamAncpTestcount,
       "tmnxOamAncpTestTimeout": tmnxOamAncpTestTimeout,
       "tmnxOamAncpTestHistoryTable": tmnxOamAncpTestHistoryTable,
       "tmnxOamAncpTestHistoryEntry": tmnxOamAncpTestHistoryEntry,
       "tmnxOamAncpHistoryIndex": tmnxOamAncpHistoryIndex,
       "tmnxOamAncpHistoryAncpString": tmnxOamAncpHistoryAncpString,
       "tmnxOamAncpHistoryAccNodeCode": tmnxOamAncpHistoryAccNodeCode,
       "tmnxOamAncpHistoryAccNodeResult": tmnxOamAncpHistoryAccNodeResult,
       "tmnxOamAncpHistoryAccNodeRspStr": tmnxOamAncpHistoryAccNodeRspStr,
       "tmnxOamP2mpLspPingCtlTable": tmnxOamP2mpLspPingCtlTable,
       "tmnxOamP2mpLspPingCtlEntry": tmnxOamP2mpLspPingCtlEntry,
       "tmnxOamP2mpLspPingCtlLspName": tmnxOamP2mpLspPingCtlLspName,
       "tmnxOamP2mpLspPingCtlInstName": tmnxOamP2mpLspPingCtlInstName,
       "tmnxOamP2mpLspPingCtlTtl": tmnxOamP2mpLspPingCtlTtl,
       "tmnxOamP2mpLspPingCtlP2MPId": tmnxOamP2mpLspPingCtlP2MPId,
       "tmnxOamP2mpLspPingCtlSrcAddrType": tmnxOamP2mpLspPingCtlSrcAddrType,
       "tmnxOamP2mpLspPingCtlSrcAddr": tmnxOamP2mpLspPingCtlSrcAddr,
       "tmnxOamP2mpLspPingCtlGrpAddrType": tmnxOamP2mpLspPingCtlGrpAddrType,
       "tmnxOamP2mpLspPingCtlGrpAddr": tmnxOamP2mpLspPingCtlGrpAddr,
       "tmnxOamP2mpLspPingCtlOptionalTLV": tmnxOamP2mpLspPingCtlOptionalTLV,
       "tmnxOamP2mpLspPingIPAddressTable": tmnxOamP2mpLspPingIPAddressTable,
       "tmnxOamP2mpLspPingIPAddressEntry": tmnxOamP2mpLspPingIPAddressEntry,
       "tmnxOamP2mpLspPingCtlIpAddrIndex": tmnxOamP2mpLspPingCtlIpAddrIndex,
       "tmnxOamP2mpLspPingCtlIpRowStatus": tmnxOamP2mpLspPingCtlIpRowStatus,
       "tmnxOamP2mpLspPingCtlIpAddrType": tmnxOamP2mpLspPingCtlIpAddrType,
       "tmnxOamP2mpLspPingCtlIpAddr": tmnxOamP2mpLspPingCtlIpAddr,
       "tmnxOamEthCfmPingCtlTable": tmnxOamEthCfmPingCtlTable,
       "tmnxOamEthCfmPingCtlEntry": tmnxOamEthCfmPingCtlEntry,
       "tmnxOamEthCfmPingCtlTgtMacAddr": tmnxOamEthCfmPingCtlTgtMacAddr,
       "tmnxOamEthCfmPingCtlSrcMdIndex": tmnxOamEthCfmPingCtlSrcMdIndex,
       "tmnxOamEthCfmPingCtlSrcMaIndex": tmnxOamEthCfmPingCtlSrcMaIndex,
       "tmnxOamEthCfmPingCtlSrcMepId": tmnxOamEthCfmPingCtlSrcMepId,
       "tmnxOamEthCfmPingCtlRemoteMepId": tmnxOamEthCfmPingCtlRemoteMepId,
       "tmnxOamVccvPgTgFec128CtlTable": tmnxOamVccvPgTgFec128CtlTable,
       "tmnxOamVccvPgTgFec128CtlEntry": tmnxOamVccvPgTgFec128CtlEntry,
       "tmnxOamVccvPgTgFec128CtlSrcAddrT": tmnxOamVccvPgTgFec128CtlSrcAddrT,
       "tmnxOamVccvPgTgFec128CtlSrcAddr": tmnxOamVccvPgTgFec128CtlSrcAddr,
       "tmnxOamVccvPgTgFec128CtlDstAddrT": tmnxOamVccvPgTgFec128CtlDstAddrT,
       "tmnxOamVccvPgTgFec128CtlDstAddr": tmnxOamVccvPgTgFec128CtlDstAddr,
       "tmnxOamVccvPgTgFec128CtlPwId": tmnxOamVccvPgTgFec128CtlPwId,
       "tmnxOamVccvPgTgFec128CtlPwType": tmnxOamVccvPgTgFec128CtlPwType,
       "tmnxOamVccvPgTgStaticCtlTable": tmnxOamVccvPgTgStaticCtlTable,
       "tmnxOamVccvPgTgStaticCtlEntry": tmnxOamVccvPgTgStaticCtlEntry,
       "tmnxOamVccvPgTgStaticCtlAgi": tmnxOamVccvPgTgStaticCtlAgi,
       "tmnxOamVccvPgTgStaticCtlSaiiGlbl": tmnxOamVccvPgTgStaticCtlSaiiGlbl,
       "tmnxOamVccvPgTgStaticCtlSaiiNode": tmnxOamVccvPgTgStaticCtlSaiiNode,
       "tmnxOamVccvPgTgStaticCtlSaiiAcId": tmnxOamVccvPgTgStaticCtlSaiiAcId,
       "tmnxOamVccvPgTgStaticCtlTaiiGlbl": tmnxOamVccvPgTgStaticCtlTaiiGlbl,
       "tmnxOamVccvPgTgStaticCtlTaiiNode": tmnxOamVccvPgTgStaticCtlTaiiNode,
       "tmnxOamVccvPgTgStaticCtlTaiiAcId": tmnxOamVccvPgTgStaticCtlTaiiAcId,
       "tmnxOamVxlanPingCtlTable": tmnxOamVxlanPingCtlTable,
       "tmnxOamVxlanPingCtlEntry": tmnxOamVxlanPingCtlEntry,
       "tmnxOamVxlanPingCtlNetworkId": tmnxOamVxlanPingCtlNetworkId,
       "tmnxOamVxlanPingCtlReplyMode": tmnxOamVxlanPingCtlReplyMode,
       "tmnxOamVxlanPingCtlIFlag": tmnxOamVxlanPingCtlIFlag,
       "tmnxOamVxlanPingCtlTestId": tmnxOamVxlanPingCtlTestId,
       "tmnxOamVxlanPingCtlOutSrcUdpPt": tmnxOamVxlanPingCtlOutSrcUdpPt,
       "tmnxOamVxlanPingCtlOutIpTtl": tmnxOamVxlanPingCtlOutIpTtl,
       "tmnxOamVxlanPingCtlInL2DestMac": tmnxOamVxlanPingCtlInL2DestMac,
       "tmnxOamVxlanPingCtlInIpSrcAddrT": tmnxOamVxlanPingCtlInIpSrcAddrT,
       "tmnxOamVxlanPingCtlInIpSrcAddr": tmnxOamVxlanPingCtlInIpSrcAddr,
       "tmnxOamVxlanPingCtlInIpDstAddrT": tmnxOamVxlanPingCtlInIpDstAddrT,
       "tmnxOamVxlanPingCtlInIpDstAddr": tmnxOamVxlanPingCtlInIpDstAddr,
       "tmnxOamVxlanPingCtlEndSysMacAddr": tmnxOamVxlanPingCtlEndSysMacAddr,
       "tmnxOamVxlanPingCtlReflectPad": tmnxOamVxlanPingCtlReflectPad,
       "tmnxOamVxlanPingHistoryTable": tmnxOamVxlanPingHistoryTable,
       "tmnxOamVxlanPingHistoryEntry": tmnxOamVxlanPingHistoryEntry,
       "tmnxOamVxlanPingHistReturnCode": tmnxOamVxlanPingHistReturnCode,
       "tmnxOamVxlanPingHistRtrnSubCode": tmnxOamVxlanPingHistRtrnSubCode,
       "tmnxOamVxlanPingHistValidationRC": tmnxOamVxlanPingHistValidationRC,
       "tmnxOamVxlanPingHistNetworkId": tmnxOamVxlanPingHistNetworkId,
       "tmnxOamVxlanPingHistOutIpTtl": tmnxOamVxlanPingHistOutIpTtl,
       "tmnxOamBfdOnLspPingResultsTable": tmnxOamBfdOnLspPingResultsTable,
       "tmnxOamBfdOnLspPingResultsEntry": tmnxOamBfdOnLspPingResultsEntry,
       "tmnxOamBfdOnLspLocalBfdDiscrim": tmnxOamBfdOnLspLocalBfdDiscrim,
       "tmnxOamBfdOnLspRemoteBfdDiscrim": tmnxOamBfdOnLspRemoteBfdDiscrim,
       "tmnxOamBfdOnLspRemoteAddressType": tmnxOamBfdOnLspRemoteAddressType,
       "tmnxOamBfdOnLspRemoteAddress": tmnxOamBfdOnLspRemoteAddress,
       "tmnxOamBfdOnLspLspName": tmnxOamBfdOnLspLspName,
       "tmnxOamBfdOnLspPingReturnCode": tmnxOamBfdOnLspPingReturnCode,
       "tmnxOamBfdOnLspPingReturnSubcode": tmnxOamBfdOnLspPingReturnSubcode,
       "tmnxOamBfdOnLspPingTxCount": tmnxOamBfdOnLspPingTxCount,
       "tmnxOamBfdOnLspPingRxCount": tmnxOamBfdOnLspPingRxCount,
       "tmnxOamBfdOnLspPathState": tmnxOamBfdOnLspPathState,
       "tmnxOamBfdOnLspPingTxInterval": tmnxOamBfdOnLspPingTxInterval,
       "tmnxOamBfdOnLspBootStrRetryCount": tmnxOamBfdOnLspBootStrRetryCount,
       "tmnxOamBfdOnLspFecType": tmnxOamBfdOnLspFecType,
       "tmnxOamBfdOnLspPrefixType": tmnxOamBfdOnLspPrefixType,
       "tmnxOamBfdOnLspPrefix": tmnxOamBfdOnLspPrefix,
       "tmnxOamBfdOnLspPrefixLen": tmnxOamBfdOnLspPrefixLen,
       "tmnxOamBfdOnLspSourceAddressType": tmnxOamBfdOnLspSourceAddressType,
       "tmnxOamBfdOnLspSourceAddress": tmnxOamBfdOnLspSourceAddress,
       "tmnxOamBfdOnLspOperState": tmnxOamBfdOnLspOperState,
       "tmnxOamVxlanPingResultsTable": tmnxOamVxlanPingResultsTable,
       "tmnxOamVxlanPingResultsEntry": tmnxOamVxlanPingResultsEntry,
       "tmnxOamVxlanPingResOutSrcAddrTyp": tmnxOamVxlanPingResOutSrcAddrTyp,
       "tmnxOamVxlanPingResOutSrcAddress": tmnxOamVxlanPingResOutSrcAddress,
       "tmnxOamPingReadOnlyScalars": tmnxOamPingReadOnlyScalars,
       "tmnxOamBfdOnLspSessBootstrInProg": tmnxOamBfdOnLspSessBootstrInProg,
       "tmnxOamBfdOnLspSessBootstrNoPV": tmnxOamBfdOnLspSessBootstrNoPV,
       "tmnxOamBfdOnLspSessBootstrSendPV": tmnxOamBfdOnLspSessBootstrSendPV,
       "tmnxOamBierPingCtlTable": tmnxOamBierPingCtlTable,
       "tmnxOamBierPingCtlEntry": tmnxOamBierPingCtlEntry,
       "tmnxOamBierPingCtlSubDomain": tmnxOamBierPingCtlSubDomain,
       "tmnxOamBierPingCtlBfrId": tmnxOamBierPingCtlBfrId,
       "tmnxOamBierPingCtlBfrIdStart": tmnxOamBierPingCtlBfrIdStart,
       "tmnxOamBierPingCtlBfrIdEnd": tmnxOamBierPingCtlBfrIdEnd,
       "tmnxOamBierPingCtlTtl": tmnxOamBierPingCtlTtl,
       "tmnxOamBierPingBfrPfxCtlTable": tmnxOamBierPingBfrPfxCtlTable,
       "tmnxOamBierPingBfrPfxCtlEntry": tmnxOamBierPingBfrPfxCtlEntry,
       "tmnxOamBierPingPfxIndex": tmnxOamBierPingPfxIndex,
       "tmnxOamBierPingBfrPfxCtlRowState": tmnxOamBierPingBfrPfxCtlRowState,
       "tmnxOamBierPingBfrPfxCtlAddrType": tmnxOamBierPingBfrPfxCtlAddrType,
       "tmnxOamBierPingBfrPfxCtlAddress": tmnxOamBierPingBfrPfxCtlAddress,
       "tmnxOamBierPingHistoryTable": tmnxOamBierPingHistoryTable,
       "tmnxOamBierPingHistoryEntry": tmnxOamBierPingHistoryEntry,
       "tmnxOamBierPingHistoryBfrId": tmnxOamBierPingHistoryBfrId,
       "tmnxOamBierPingHistoryBfrPfxType": tmnxOamBierPingHistoryBfrPfxType,
       "tmnxOamBierPingHistoryBfrPfx": tmnxOamBierPingHistoryBfrPfx,
       "tmnxOamBierPingHistoryReturnCode": tmnxOamBierPingHistoryReturnCode,
       "tmnxOamTraceRouteObjs": tmnxOamTraceRouteObjs,
       "tmnxOamTraceRouteNotifyObjects": tmnxOamTraceRouteNotifyObjects,
       "tmnxOamTrMaxConcurrentRequests": tmnxOamTrMaxConcurrentRequests,
       "tmnxOamTrCtlTable": tmnxOamTrCtlTable,
       "tmnxOamTrCtlEntry": tmnxOamTrCtlEntry,
       "tmnxOamTrCtlOwnerIndex": tmnxOamTrCtlOwnerIndex,
       "tmnxOamTrCtlTestIndex": tmnxOamTrCtlTestIndex,
       "tmnxOamTrCtlRowStatus": tmnxOamTrCtlRowStatus,
       "tmnxOamTrCtlStorageType": tmnxOamTrCtlStorageType,
       "tmnxOamTrCtlDescr": tmnxOamTrCtlDescr,
       "tmnxOamTrCtlTestMode": tmnxOamTrCtlTestMode,
       "tmnxOamTrCtlAdminStatus": tmnxOamTrCtlAdminStatus,
       "tmnxOamTrCtlFcName": tmnxOamTrCtlFcName,
       "tmnxOamTrCtlProfile": tmnxOamTrCtlProfile,
       "tmnxOamTrCtlTargetIpAddress": tmnxOamTrCtlTargetIpAddress,
       "tmnxOamTrCtlServiceId": tmnxOamTrCtlServiceId,
       "tmnxOamTrCtlDataSize": tmnxOamTrCtlDataSize,
       "tmnxOamTrCtlTimeOut": tmnxOamTrCtlTimeOut,
       "tmnxOamTrCtlProbesPerHop": tmnxOamTrCtlProbesPerHop,
       "tmnxOamTrCtlMaxTtl": tmnxOamTrCtlMaxTtl,
       "tmnxOamTrCtlInitialTtl": tmnxOamTrCtlInitialTtl,
       "tmnxOamTrCtlDSField": tmnxOamTrCtlDSField,
       "tmnxOamTrCtlMaxFailures": tmnxOamTrCtlMaxFailures,
       "tmnxOamTrCtlInterval": tmnxOamTrCtlInterval,
       "tmnxOamTrCtlMaxRows": tmnxOamTrCtlMaxRows,
       "tmnxOamTrCtlTrapGeneration": tmnxOamTrCtlTrapGeneration,
       "tmnxOamTrCtlCreateHopsEntries": tmnxOamTrCtlCreateHopsEntries,
       "tmnxOamTrCtlSAA": tmnxOamTrCtlSAA,
       "tmnxOamTrCtlRuns": tmnxOamTrCtlRuns,
       "tmnxOamTrCtlFailures": tmnxOamTrCtlFailures,
       "tmnxOamTrCtlLastRunResult": tmnxOamTrCtlLastRunResult,
       "tmnxOamTrCtlLastChanged": tmnxOamTrCtlLastChanged,
       "tmnxOamTrCtlVRtrID": tmnxOamTrCtlVRtrID,
       "tmnxOamTrCtlTgtAddrType": tmnxOamTrCtlTgtAddrType,
       "tmnxOamTrCtlTgtAddress": tmnxOamTrCtlTgtAddress,
       "tmnxOamTrCtlSrcAddrType": tmnxOamTrCtlSrcAddrType,
       "tmnxOamTrCtlSrcAddress": tmnxOamTrCtlSrcAddress,
       "tmnxOamTrCtlWaitMilliSec": tmnxOamTrCtlWaitMilliSec,
       "tmnxOamTrCtlRouterInstanceName": tmnxOamTrCtlRouterInstanceName,
       "tmnxOamTrResultsTable": tmnxOamTrResultsTable,
       "tmnxOamTrResultsEntry": tmnxOamTrResultsEntry,
       "tmnxOamTrResultsOperStatus": tmnxOamTrResultsOperStatus,
       "tmnxOamTrResultsCurHopCount": tmnxOamTrResultsCurHopCount,
       "tmnxOamTrResultsCurProbeCount": tmnxOamTrResultsCurProbeCount,
       "tmnxOamTrResultsIpTgtAddr": tmnxOamTrResultsIpTgtAddr,
       "tmnxOamTrResultsTestAttempts": tmnxOamTrResultsTestAttempts,
       "tmnxOamTrResultsTestSuccesses": tmnxOamTrResultsTestSuccesses,
       "tmnxOamTrResultsLastGoodPath": tmnxOamTrResultsLastGoodPath,
       "tmnxOamTrResultsTestRunIndex": tmnxOamTrResultsTestRunIndex,
       "tmnxOamTrResultsTgtAddrType": tmnxOamTrResultsTgtAddrType,
       "tmnxOamTrResultsTgtAddress": tmnxOamTrResultsTgtAddress,
       "tmnxOamTrResultsTestRunResult": tmnxOamTrResultsTestRunResult,
       "tmnxOamTrProbeHistoryTable": tmnxOamTrProbeHistoryTable,
       "tmnxOamTrProbeHistoryEntry": tmnxOamTrProbeHistoryEntry,
       "tmnxOamTrProbeHistoryIndex": tmnxOamTrProbeHistoryIndex,
       "tmnxOamTrProbeHistoryHopIndex": tmnxOamTrProbeHistoryHopIndex,
       "tmnxOamTrProbeHistoryProbeIndex": tmnxOamTrProbeHistoryProbeIndex,
       "tmnxOamTrProbeHistoryIpAddr": tmnxOamTrProbeHistoryIpAddr,
       "tmnxOamTrProbeHistoryResponse": tmnxOamTrProbeHistoryResponse,
       "tmnxOamTrProbeHistoryOneWayTime": tmnxOamTrProbeHistoryOneWayTime,
       "tmnxOamTrProbeHistoryStatus": tmnxOamTrProbeHistoryStatus,
       "tmnxOamTrProbeHistoryLastRC": tmnxOamTrProbeHistoryLastRC,
       "tmnxOamTrProbeHistoryTime": tmnxOamTrProbeHistoryTime,
       "tmnxOamTrProbeHistoryResponsePlane": tmnxOamTrProbeHistoryResponsePlane,
       "tmnxOamTrProbeHistoryAddressType": tmnxOamTrProbeHistoryAddressType,
       "tmnxOamTrProbeHistorySapId": tmnxOamTrProbeHistorySapId,
       "tmnxOamTrProbeHistoryVersion": tmnxOamTrProbeHistoryVersion,
       "tmnxOamTrProbeHistoryRouterID": tmnxOamTrProbeHistoryRouterID,
       "tmnxOamTrProbeHistoryIfIndex": tmnxOamTrProbeHistoryIfIndex,
       "tmnxOamTrProbeHistoryDataLen": tmnxOamTrProbeHistoryDataLen,
       "tmnxOamTrProbeHistorySize": tmnxOamTrProbeHistorySize,
       "tmnxOamTrProbeHistoryInOneWayTime": tmnxOamTrProbeHistoryInOneWayTime,
       "tmnxOamTrProbeHistoryAddrType": tmnxOamTrProbeHistoryAddrType,
       "tmnxOamTrProbeHistoryAddress": tmnxOamTrProbeHistoryAddress,
       "tmnxOamTrProbeHistorySrcGlobalId": tmnxOamTrProbeHistorySrcGlobalId,
       "tmnxOamTrProbeHistorySrcNodeId": tmnxOamTrProbeHistorySrcNodeId,
       "tmnxOamTrProbeHistorySdpBindId": tmnxOamTrProbeHistorySdpBindId,
       "tmnxOamTrProbeHistoryRtrnSubcode": tmnxOamTrProbeHistoryRtrnSubcode,
       "tmnxOamTrProbeHistoryNtwrkIfName": tmnxOamTrProbeHistoryNtwrkIfName,
       "tmnxOamTrHopsTable": tmnxOamTrHopsTable,
       "tmnxOamTrHopsEntry": tmnxOamTrHopsEntry,
       "tmnxOamTrHopsHopIndex": tmnxOamTrHopsHopIndex,
       "tmnxOamTrHopsIpTgtAddress": tmnxOamTrHopsIpTgtAddress,
       "tmnxOamTrHopsMinRtt": tmnxOamTrHopsMinRtt,
       "tmnxOamTrHopsMaxRtt": tmnxOamTrHopsMaxRtt,
       "tmnxOamTrHopsAverageRtt": tmnxOamTrHopsAverageRtt,
       "tmnxOamTrHopsRttSumOfSquares": tmnxOamTrHopsRttSumOfSquares,
       "tmnxOamTrHopsMinTt": tmnxOamTrHopsMinTt,
       "tmnxOamTrHopsMaxTt": tmnxOamTrHopsMaxTt,
       "tmnxOamTrHopsAverageTt": tmnxOamTrHopsAverageTt,
       "tmnxOamTrHopsTtSumOfSquares": tmnxOamTrHopsTtSumOfSquares,
       "tmnxOamTrHopsSentProbes": tmnxOamTrHopsSentProbes,
       "tmnxOamTrHopsProbeResponses": tmnxOamTrHopsProbeResponses,
       "tmnxOamTrHopsLastGoodProbe": tmnxOamTrHopsLastGoodProbe,
       "tmnxOamTrHopsMinInTt": tmnxOamTrHopsMinInTt,
       "tmnxOamTrHopsMaxInTt": tmnxOamTrHopsMaxInTt,
       "tmnxOamTrHopsAverageInTt": tmnxOamTrHopsAverageInTt,
       "tmnxOamTrHopsInTtSumOfSqrs": tmnxOamTrHopsInTtSumOfSqrs,
       "tmnxOamTrHopsOutJitter": tmnxOamTrHopsOutJitter,
       "tmnxOamTrHopsInJitter": tmnxOamTrHopsInJitter,
       "tmnxOamTrHopsRtJitter": tmnxOamTrHopsRtJitter,
       "tmnxOamTrHopsProbeTimeouts": tmnxOamTrHopsProbeTimeouts,
       "tmnxOamTrHopsProbeFailures": tmnxOamTrHopsProbeFailures,
       "tmnxOamTrHopsTgtAddrType": tmnxOamTrHopsTgtAddrType,
       "tmnxOamTrHopsTgtAddress": tmnxOamTrHopsTgtAddress,
       "tmnxOamTrHopsRttOFSumSquares": tmnxOamTrHopsRttOFSumSquares,
       "tmnxOamTrHopsRttHCSumSquares": tmnxOamTrHopsRttHCSumSquares,
       "tmnxOamTrHopsTtOFSumSquares": tmnxOamTrHopsTtOFSumSquares,
       "tmnxOamTrHopsTtHCSumSquares": tmnxOamTrHopsTtHCSumSquares,
       "tmnxOamTrHopsInTtOFSumSqrs": tmnxOamTrHopsInTtOFSumSqrs,
       "tmnxOamTrHopsInTtHCSumSqrs": tmnxOamTrHopsInTtHCSumSqrs,
       "tmnxOamMacTrCtlTable": tmnxOamMacTrCtlTable,
       "tmnxOamMacTrCtlEntry": tmnxOamMacTrCtlEntry,
       "tmnxOamMacTrCtlTargetMacAddr": tmnxOamMacTrCtlTargetMacAddr,
       "tmnxOamMacTrCtlSourceMacAddr": tmnxOamMacTrCtlSourceMacAddr,
       "tmnxOamMacTrCtlSendControl": tmnxOamMacTrCtlSendControl,
       "tmnxOamMacTrCtlReplyControl": tmnxOamMacTrCtlReplyControl,
       "tmnxOamMacTrL2MapTable": tmnxOamMacTrL2MapTable,
       "tmnxOamMacTrL2MapEntry": tmnxOamMacTrL2MapEntry,
       "tmnxOamMacTrL2MapIndex": tmnxOamMacTrL2MapIndex,
       "tmnxOamMacTrL2MapRouterID": tmnxOamMacTrL2MapRouterID,
       "tmnxOamMacTrL2MapLabel": tmnxOamMacTrL2MapLabel,
       "tmnxOamMacTrL2MapProtocol": tmnxOamMacTrL2MapProtocol,
       "tmnxOamMacTrL2MapVCType": tmnxOamMacTrL2MapVCType,
       "tmnxOamMacTrL2MapVCID": tmnxOamMacTrL2MapVCID,
       "tmnxOamMacTrL2MapDirection": tmnxOamMacTrL2MapDirection,
       "tmnxOamMacTrL2MapSdpId": tmnxOamMacTrL2MapSdpId,
       "tmnxOamMacTrL2MapSapName": tmnxOamMacTrL2MapSapName,
       "tmnxOamLspTrCtlTable": tmnxOamLspTrCtlTable,
       "tmnxOamLspTrCtlEntry": tmnxOamLspTrCtlEntry,
       "tmnxOamLspTrCtlVRtrID": tmnxOamLspTrCtlVRtrID,
       "tmnxOamLspTrCtlLspName": tmnxOamLspTrCtlLspName,
       "tmnxOamLspTrCtlPathName": tmnxOamLspTrCtlPathName,
       "tmnxOamLspTrCtlLdpIpPrefix": tmnxOamLspTrCtlLdpIpPrefix,
       "tmnxOamLspTrCtlLdpIpPrefixLen": tmnxOamLspTrCtlLdpIpPrefixLen,
       "tmnxOamLspTrCtlLdpPrefixType": tmnxOamLspTrCtlLdpPrefixType,
       "tmnxOamLspTrCtlLdpPrefix": tmnxOamLspTrCtlLdpPrefix,
       "tmnxOamLspTrCtlLdpPrefixLen": tmnxOamLspTrCtlLdpPrefixLen,
       "tmnxOamLspTrCtlPathDestType": tmnxOamLspTrCtlPathDestType,
       "tmnxOamLspTrCtlPathDest": tmnxOamLspTrCtlPathDest,
       "tmnxOamLspTrCtlNhIntfName": tmnxOamLspTrCtlNhIntfName,
       "tmnxOamLspTrCtlNhAddressType": tmnxOamLspTrCtlNhAddressType,
       "tmnxOamLspTrCtlNhAddress": tmnxOamLspTrCtlNhAddress,
       "tmnxOamLspTrCtlDownstreamMapTlv": tmnxOamLspTrCtlDownstreamMapTlv,
       "tmnxOamLspTrCtlTestSubMode": tmnxOamLspTrCtlTestSubMode,
       "tmnxOamLspTrCtlMplsTpPathType": tmnxOamLspTrCtlMplsTpPathType,
       "tmnxOamLspTrCtlAssocChannel": tmnxOamLspTrCtlAssocChannel,
       "tmnxOamLspTrCtlForce": tmnxOamLspTrCtlForce,
       "tmnxOamLspTrCtlIgpInstance": tmnxOamLspTrCtlIgpInstance,
       "tmnxOamLspTrCtlSrPlcyColor": tmnxOamLspTrCtlSrPlcyColor,
       "tmnxOamLspTrCtlSrPlcyEndPtAddT": tmnxOamLspTrCtlSrPlcyEndPtAddT,
       "tmnxOamLspTrCtlSrPlcyEndPtAddr": tmnxOamLspTrCtlSrPlcyEndPtAddr,
       "tmnxOamLspTrCtlSrPlcySegList": tmnxOamLspTrCtlSrPlcySegList,
       "tmnxOamLspTrMapTable": tmnxOamLspTrMapTable,
       "tmnxOamLspTrMapEntry": tmnxOamLspTrMapEntry,
       "tmnxOamLspTrMapIndex": tmnxOamLspTrMapIndex,
       "tmnxOamLspTrMapDSIPv4Addr": tmnxOamLspTrMapDSIPv4Addr,
       "tmnxOamLspTrMapAddrType": tmnxOamLspTrMapAddrType,
       "tmnxOamLspTrMapDSIfAddr": tmnxOamLspTrMapDSIfAddr,
       "tmnxOamLspTrMapMTU": tmnxOamLspTrMapMTU,
       "tmnxOamLspTrMapDSIndex": tmnxOamLspTrMapDSIndex,
       "tmnxOamLspTrMapDsEgrIfNum": tmnxOamLspTrMapDsEgrIfNum,
       "tmnxOamLspTrMapDsIngIfNum": tmnxOamLspTrMapDsIngIfNum,
       "tmnxOamLspTrMapDsIpAddressType": tmnxOamLspTrMapDsIpAddressType,
       "tmnxOamLspTrMapDsIpAddress": tmnxOamLspTrMapDsIpAddress,
       "tmnxOamLspTrMapDsIfAddressType": tmnxOamLspTrMapDsIfAddressType,
       "tmnxOamLspTrMapDsIfAddress": tmnxOamLspTrMapDsIfAddress,
       "tmnxOamVprnTrCtlTable": tmnxOamVprnTrCtlTable,
       "tmnxOamVprnTrCtlEntry": tmnxOamVprnTrCtlEntry,
       "tmnxOamVprnTrCtlSourceIpAddr": tmnxOamVprnTrCtlSourceIpAddr,
       "tmnxOamVprnTrCtlReplyControl": tmnxOamVprnTrCtlReplyControl,
       "tmnxOamVprnTrCtlSrcAddrType": tmnxOamVprnTrCtlSrcAddrType,
       "tmnxOamVprnTrCtlSrcAddress": tmnxOamVprnTrCtlSrcAddress,
       "tmnxOamVprnTrL3MapTable": tmnxOamVprnTrL3MapTable,
       "tmnxOamVprnTrL3MapEntry": tmnxOamVprnTrL3MapEntry,
       "tmnxOamVprnTrL3MapReporter": tmnxOamVprnTrL3MapReporter,
       "tmnxOamVprnTrL3MapRouterID": tmnxOamVprnTrL3MapRouterID,
       "tmnxOamVprnTrL3MapRteDestAddr": tmnxOamVprnTrL3MapRteDestAddr,
       "tmnxOamVprnTrL3MapRteDestMask": tmnxOamVprnTrL3MapRteDestMask,
       "tmnxOamVprnTrL3MapRteVprnLabel": tmnxOamVprnTrL3MapRteVprnLabel,
       "tmnxOamVprnTrL3MapRteMetrics": tmnxOamVprnTrL3MapRteMetrics,
       "tmnxOamVprnTrL3MapRteLastUp": tmnxOamVprnTrL3MapRteLastUp,
       "tmnxOamVprnTrL3MapRteOwner": tmnxOamVprnTrL3MapRteOwner,
       "tmnxOamVprnTrL3MapRtePref": tmnxOamVprnTrL3MapRtePref,
       "tmnxOamVprnTrL3MapRteDist": tmnxOamVprnTrL3MapRteDist,
       "tmnxOamVprnTrL3MapNumNextHops": tmnxOamVprnTrL3MapNumNextHops,
       "tmnxOamVprnTrL3MapNumRteTargets": tmnxOamVprnTrL3MapNumRteTargets,
       "tmnxOamVprnTrL3MapDestAddrType": tmnxOamVprnTrL3MapDestAddrType,
       "tmnxOamVprnTrL3MapDestAddress": tmnxOamVprnTrL3MapDestAddress,
       "tmnxOamVprnTrL3MapDestMaskLen": tmnxOamVprnTrL3MapDestMaskLen,
       "tmnxOamVprnTrNextHopTable": tmnxOamVprnTrNextHopTable,
       "tmnxOamVprnTrNextHopEntry": tmnxOamVprnTrNextHopEntry,
       "tmnxOamVprnTrNextHopIndex": tmnxOamVprnTrNextHopIndex,
       "tmnxOamVprnTrNextHopRtrID": tmnxOamVprnTrNextHopRtrID,
       "tmnxOamVprnTrNextHopType": tmnxOamVprnTrNextHopType,
       "tmnxOamVprnTrNextHopTunnelID": tmnxOamVprnTrNextHopTunnelID,
       "tmnxOamVprnTrNextHopTunnelType": tmnxOamVprnTrNextHopTunnelType,
       "tmnxOamVprnTrNextHopIfIndex": tmnxOamVprnTrNextHopIfIndex,
       "tmnxOamVprnTrNextHopAddrType": tmnxOamVprnTrNextHopAddrType,
       "tmnxOamVprnTrNextHopAddress": tmnxOamVprnTrNextHopAddress,
       "tmnxOamVprnTrRTTable": tmnxOamVprnTrRTTable,
       "tmnxOamVprnTrRTEntry": tmnxOamVprnTrRTEntry,
       "tmnxOamVprnTrRTIndex": tmnxOamVprnTrRTIndex,
       "tmnxOamVprnTrRouteTarget": tmnxOamVprnTrRouteTarget,
       "tmnxOamLspTrDSLabelTable": tmnxOamLspTrDSLabelTable,
       "tmnxOamLspTrDSLabelEntry": tmnxOamLspTrDSLabelEntry,
       "tmnxOamLspTrDSLabelIndex": tmnxOamLspTrDSLabelIndex,
       "tmnxOamLspTrDSLabelLabel": tmnxOamLspTrDSLabelLabel,
       "tmnxOamLspTrDSLabelProtocol": tmnxOamLspTrDSLabelProtocol,
       "tmnxOamMcastTrCtlTable": tmnxOamMcastTrCtlTable,
       "tmnxOamMcastTrCtlEntry": tmnxOamMcastTrCtlEntry,
       "tmnxOamMcastTrCtlVRtrID": tmnxOamMcastTrCtlVRtrID,
       "tmnxOamMcastTrCtlSrcIpAddr": tmnxOamMcastTrCtlSrcIpAddr,
       "tmnxOamMcastTrCtlDestIpAddr": tmnxOamMcastTrCtlDestIpAddr,
       "tmnxOamMcastTrCtlRespIpAddr": tmnxOamMcastTrCtlRespIpAddr,
       "tmnxOamMcastTrCtlGrpIpAddr": tmnxOamMcastTrCtlGrpIpAddr,
       "tmnxOamMcastTrCtlHops": tmnxOamMcastTrCtlHops,
       "tmnxOamMcastTrQueryId": tmnxOamMcastTrQueryId,
       "tmnxOamMcastTrCtlSrcAddrType": tmnxOamMcastTrCtlSrcAddrType,
       "tmnxOamMcastTrCtlSrcAddress": tmnxOamMcastTrCtlSrcAddress,
       "tmnxOamMcastTrCtlDestAddrType": tmnxOamMcastTrCtlDestAddrType,
       "tmnxOamMcastTrCtlDestAddress": tmnxOamMcastTrCtlDestAddress,
       "tmnxOamMcastTrCtlRespAddrType": tmnxOamMcastTrCtlRespAddrType,
       "tmnxOamMcastTrCtlRespAddress": tmnxOamMcastTrCtlRespAddress,
       "tmnxOamMcastTrCtlGrpAddrType": tmnxOamMcastTrCtlGrpAddrType,
       "tmnxOamMcastTrCtlGrpAddress": tmnxOamMcastTrCtlGrpAddress,
       "tmnxOamMcastTrCtlTestSubMode": tmnxOamMcastTrCtlTestSubMode,
       "tmnxOamMcastTrRespTable": tmnxOamMcastTrRespTable,
       "tmnxOamMcastTrRespEntry": tmnxOamMcastTrRespEntry,
       "tmnxOamMcastTrRespQueryArrivalTime": tmnxOamMcastTrRespQueryArrivalTime,
       "tmnxOamMcastTrRespInIfAddr": tmnxOamMcastTrRespInIfAddr,
       "tmnxOamMcastTrRespOutIfAddr": tmnxOamMcastTrRespOutIfAddr,
       "tmnxOamMcastTrRespPrevHopRtrAddr": tmnxOamMcastTrRespPrevHopRtrAddr,
       "tmnxOamMcastTrRespInPktCount": tmnxOamMcastTrRespInPktCount,
       "tmnxOamMcastTrRespOutPktCount": tmnxOamMcastTrRespOutPktCount,
       "tmnxOamMcastTrRespSGPktCount": tmnxOamMcastTrRespSGPktCount,
       "tmnxOamMcastTrRespRtgProtocol": tmnxOamMcastTrRespRtgProtocol,
       "tmnxOamMcastTrRespFwdTtl": tmnxOamMcastTrRespFwdTtl,
       "tmnxOamMcastTrRespMBZBit": tmnxOamMcastTrRespMBZBit,
       "tmnxOamMcastTrRespSrcBit": tmnxOamMcastTrRespSrcBit,
       "tmnxOamMcastTrRespSrcMask": tmnxOamMcastTrRespSrcMask,
       "tmnxOamMcastTrRespFwdCode": tmnxOamMcastTrRespFwdCode,
       "tmnxOamMcastTrRespInIfAddrType": tmnxOamMcastTrRespInIfAddrType,
       "tmnxOamMcastTrRespInIfAddress": tmnxOamMcastTrRespInIfAddress,
       "tmnxOamMcastTrRespOutIfAddrType": tmnxOamMcastTrRespOutIfAddrType,
       "tmnxOamMcastTrRespOutIfAddress": tmnxOamMcastTrRespOutIfAddress,
       "tmnxOamMcastTrRespPhRtrAddrType": tmnxOamMcastTrRespPhRtrAddrType,
       "tmnxOamMcastTrRespPhRtrAddress": tmnxOamMcastTrRespPhRtrAddress,
       "tmnxOamMcastTrRespInPktCountHC": tmnxOamMcastTrRespInPktCountHC,
       "tmnxOamMcastTrRespOutPktCountHC": tmnxOamMcastTrRespOutPktCountHC,
       "tmnxOamMcastTrRespSGPktCountHC": tmnxOamMcastTrRespSGPktCountHC,
       "tmnxOamMcastTrRespRtgProtocol2": tmnxOamMcastTrRespRtgProtocol2,
       "tmnxOamMcastTrRespMcastRtgProto": tmnxOamMcastTrRespMcastRtgProto,
       "tmnxOamMcastTrRespInIfIndex": tmnxOamMcastTrRespInIfIndex,
       "tmnxOamMcastTrRespOutIfIndex": tmnxOamMcastTrRespOutIfIndex,
       "tmnxOamMcastTrRespLocalAddrType": tmnxOamMcastTrRespLocalAddrType,
       "tmnxOamMcastTrRespLocalAddress": tmnxOamMcastTrRespLocalAddress,
       "tmnxOamLTtraceCtlTable": tmnxOamLTtraceCtlTable,
       "tmnxOamLTtraceCtlEntry": tmnxOamLTtraceCtlEntry,
       "tmnxOamLTtraceCtlLdpPrefixType": tmnxOamLTtraceCtlLdpPrefixType,
       "tmnxOamLTtraceCtlLdpPrefix": tmnxOamLTtraceCtlLdpPrefix,
       "tmnxOamLTtraceCtlLdpPrefixLen": tmnxOamLTtraceCtlLdpPrefixLen,
       "tmnxOamLTtraceCtlMaxPath": tmnxOamLTtraceCtlMaxPath,
       "tmnxOamLTtraceCtlDownstreamMpTlv": tmnxOamLTtraceCtlDownstreamMpTlv,
       "tmnxOamLTtraceMaxConRequests": tmnxOamLTtraceMaxConRequests,
       "tmnxOamLTtraceResultsTable": tmnxOamLTtraceResultsTable,
       "tmnxOamLTtraceResultsEntry": tmnxOamLTtraceResultsEntry,
       "tmnxOamLTtraceResultsDisPaths": tmnxOamLTtraceResultsDisPaths,
       "tmnxOamLTtraceResultsFailedHops": tmnxOamLTtraceResultsFailedHops,
       "tmnxOamLTtraceResultsDisState": tmnxOamLTtraceResultsDisState,
       "tmnxOamLTtraceResultsDisStatus": tmnxOamLTtraceResultsDisStatus,
       "tmnxOamLTtraceHopInfoTable": tmnxOamLTtraceHopInfoTable,
       "tmnxOamLTtraceHopInfoEntry": tmnxOamLTtraceHopInfoEntry,
       "tmnxOamLTtraceHopIndex": tmnxOamLTtraceHopIndex,
       "tmnxOamLTtraceUpStreamHopIndex": tmnxOamLTtraceUpStreamHopIndex,
       "tmnxOamLTtraceHopAddrType": tmnxOamLTtraceHopAddrType,
       "tmnxOamLTtraceHopAddr": tmnxOamLTtraceHopAddr,
       "tmnxOamLTtraceHopDstAddrType": tmnxOamLTtraceHopDstAddrType,
       "tmnxOamLTtraceHopDstAddr": tmnxOamLTtraceHopDstAddr,
       "tmnxOamLTtraceHopEgrNhAddrType": tmnxOamLTtraceHopEgrNhAddrType,
       "tmnxOamLTtraceHopEgrNhAddr": tmnxOamLTtraceHopEgrNhAddr,
       "tmnxOamLTtraceHopDisTtl": tmnxOamLTtraceHopDisTtl,
       "tmnxOamLTtraceHopLastRc": tmnxOamLTtraceHopLastRc,
       "tmnxOamLTtraceHopDiscoveryState": tmnxOamLTtraceHopDiscoveryState,
       "tmnxOamLTtraceHopDiscoveryTime": tmnxOamLTtraceHopDiscoveryTime,
       "tmnxOamLTtraceHopLabel1": tmnxOamLTtraceHopLabel1,
       "tmnxOamLTtraceHopLabel2": tmnxOamLTtraceHopLabel2,
       "tmnxOamLTtraceHopLabel3": tmnxOamLTtraceHopLabel3,
       "tmnxOamLTtraceHopLabel4": tmnxOamLTtraceHopLabel4,
       "tmnxOamLTtraceHopLabel5": tmnxOamLTtraceHopLabel5,
       "tmnxOamLTtraceHopLabel6": tmnxOamLTtraceHopLabel6,
       "tmnxOamLTtraceHopIfAddrType": tmnxOamLTtraceHopIfAddrType,
       "tmnxOamLTtraceHopIfAddress": tmnxOamLTtraceHopIfAddress,
       "tmnxOamLTtraceHopRouterIdType": tmnxOamLTtraceHopRouterIdType,
       "tmnxOamLTtraceHopRouterId": tmnxOamLTtraceHopRouterId,
       "tmnxOamLTtraceAutoConfigTable": tmnxOamLTtraceAutoConfigTable,
       "tmnxOamLTtraceAutoConfigEntry": tmnxOamLTtraceAutoConfigEntry,
       "tmnxOamLTtraceAutoRowStatus": tmnxOamLTtraceAutoRowStatus,
       "tmnxOamLTtraceAutoLastChanged": tmnxOamLTtraceAutoLastChanged,
       "tmnxOamLTtraceAutoStorageType": tmnxOamLTtraceAutoStorageType,
       "tmnxOamLTtraceAutoAdminState": tmnxOamLTtraceAutoAdminState,
       "tmnxOamLTtraceAutoFcName": tmnxOamLTtraceAutoFcName,
       "tmnxOamLTtraceAutoProfile": tmnxOamLTtraceAutoProfile,
       "tmnxOamLTtraceAutoDiscIntvl": tmnxOamLTtraceAutoDiscIntvl,
       "tmnxOamLTtraceAutoMaxPath": tmnxOamLTtraceAutoMaxPath,
       "tmnxOamLTtraceAutoTrMaxTtl": tmnxOamLTtraceAutoTrMaxTtl,
       "tmnxOamLTtraceAutoTrTimeOut": tmnxOamLTtraceAutoTrTimeOut,
       "tmnxOamLTtraceAutoTrMaxFailures": tmnxOamLTtraceAutoTrMaxFailures,
       "tmnxOamLTtraceAutoPolicy1": tmnxOamLTtraceAutoPolicy1,
       "tmnxOamLTtraceAutoPolicy2": tmnxOamLTtraceAutoPolicy2,
       "tmnxOamLTtraceAutoPolicy3": tmnxOamLTtraceAutoPolicy3,
       "tmnxOamLTtraceAutoPolicy4": tmnxOamLTtraceAutoPolicy4,
       "tmnxOamLTtraceAutoPolicy5": tmnxOamLTtraceAutoPolicy5,
       "tmnxOamLTtraceAutoProbeIntvl": tmnxOamLTtraceAutoProbeIntvl,
       "tmnxOamLTtraceAutoPrTimeOut": tmnxOamLTtraceAutoPrTimeOut,
       "tmnxOamLTtraceAutoPrMaxFailures": tmnxOamLTtraceAutoPrMaxFailures,
       "tmnxOamLTtraceAutoStatusTable": tmnxOamLTtraceAutoStatusTable,
       "tmnxOamLTtraceAutoStatusEntry": tmnxOamLTtraceAutoStatusEntry,
       "tmnxOamLTtraceAutoDiscoveryState": tmnxOamLTtraceAutoDiscoveryState,
       "tmnxOamLTtraceAutoTotalFecs": tmnxOamLTtraceAutoTotalFecs,
       "tmnxOamLTtraceAutoDisFecs": tmnxOamLTtraceAutoDisFecs,
       "tmnxOamLTtraceAutoLastDisStart": tmnxOamLTtraceAutoLastDisStart,
       "tmnxOamLTtraceAutoLastDisEnd": tmnxOamLTtraceAutoLastDisEnd,
       "tmnxOamLTtraceAutoLastDisDur": tmnxOamLTtraceAutoLastDisDur,
       "tmnxOamLTtraceFecInfoTable": tmnxOamLTtraceFecInfoTable,
       "tmnxOamLTtraceFecInfoEntry": tmnxOamLTtraceFecInfoEntry,
       "tmnxOamLTtraceFecPrefixType": tmnxOamLTtraceFecPrefixType,
       "tmnxOamLTtraceFecPrefix": tmnxOamLTtraceFecPrefix,
       "tmnxOamLTtraceFecPrefLen": tmnxOamLTtraceFecPrefLen,
       "tmnxOamLTtraceFecDiscoveryState": tmnxOamLTtraceFecDiscoveryState,
       "tmnxOamLTtraceFecDisStatusBits": tmnxOamLTtraceFecDisStatusBits,
       "tmnxOamLTtraceFecDisPaths": tmnxOamLTtraceFecDisPaths,
       "tmnxOamLTtraceFecFailedHops": tmnxOamLTtraceFecFailedHops,
       "tmnxOamLTtraceFecLastDisEnd": tmnxOamLTtraceFecLastDisEnd,
       "tmnxOamLTtraceFecFailedProbes": tmnxOamLTtraceFecFailedProbes,
       "tmnxOamLTtraceFecProbeState": tmnxOamLTtraceFecProbeState,
       "tmnxOamLTtraceFecSendErrProbes": tmnxOamLTtraceFecSendErrProbes,
       "tmnxOamLTtracePathInfoTable": tmnxOamLTtracePathInfoTable,
       "tmnxOamLTtracePathInfoEntry": tmnxOamLTtracePathInfoEntry,
       "tmnxOamLTtracePathDstAddrType": tmnxOamLTtracePathDstAddrType,
       "tmnxOamLTtracePathDstAddr": tmnxOamLTtracePathDstAddr,
       "tmnxOamLTtracePathRemAddrType": tmnxOamLTtracePathRemAddrType,
       "tmnxOamLTtracePathRemoteAddr": tmnxOamLTtracePathRemoteAddr,
       "tmnxOamLTtracePathEgrNhAddrType": tmnxOamLTtracePathEgrNhAddrType,
       "tmnxOamLTtracePathEgrNhAddr": tmnxOamLTtracePathEgrNhAddr,
       "tmnxOamLTtracePathDisTtl": tmnxOamLTtracePathDisTtl,
       "tmnxOamLTtracePathLastDisTime": tmnxOamLTtracePathLastDisTime,
       "tmnxOamLTtracePathLastRc": tmnxOamLTtracePathLastRc,
       "tmnxOamLTtracePathProbeState": tmnxOamLTtracePathProbeState,
       "tmnxOamLTtracePathProbeTmOutCnt": tmnxOamLTtracePathProbeTmOutCnt,
       "tmnxOamLTtracePathProbeSendErr": tmnxOamLTtracePathProbeSendErr,
       "tmnxOamVccvTrCtlTable": tmnxOamVccvTrCtlTable,
       "tmnxOamVccvTrCtlEntry": tmnxOamVccvTrCtlEntry,
       "tmnxOamVccvTrCtlSdpIdVcId": tmnxOamVccvTrCtlSdpIdVcId,
       "tmnxOamVccvTrCtlReplyMode": tmnxOamVccvTrCtlReplyMode,
       "tmnxOamVccvTrCtlSpokeSdpId": tmnxOamVccvTrCtlSpokeSdpId,
       "tmnxOamVccvTrCtlSaiiGlobalId": tmnxOamVccvTrCtlSaiiGlobalId,
       "tmnxOamVccvTrCtlSaiiPrefix": tmnxOamVccvTrCtlSaiiPrefix,
       "tmnxOamVccvTrCtlSaiiAcId": tmnxOamVccvTrCtlSaiiAcId,
       "tmnxOamVccvTrCtlTaiiGlobalId": tmnxOamVccvTrCtlTaiiGlobalId,
       "tmnxOamVccvTrCtlTaiiPrefix": tmnxOamVccvTrCtlTaiiPrefix,
       "tmnxOamVccvTrCtlTaiiAcId": tmnxOamVccvTrCtlTaiiAcId,
       "tmnxOamVccvTrCtlTestSubMode": tmnxOamVccvTrCtlTestSubMode,
       "tmnxOamVccvTrCtlAssocChannel": tmnxOamVccvTrCtlAssocChannel,
       "tmnxOamVccvTrCtlSwitTgtFecType": tmnxOamVccvTrCtlSwitTgtFecType,
       "tmnxOamVccvTrNextPwSegmentTable": tmnxOamVccvTrNextPwSegmentTable,
       "tmnxOamVccvTrNextPwSegmentEntry": tmnxOamVccvTrNextPwSegmentEntry,
       "tmnxOamVccvTrNextPwID": tmnxOamVccvTrNextPwID,
       "tmnxOamVccvTrNextPwType": tmnxOamVccvTrNextPwType,
       "tmnxOamVccvTrNextSenderAddrType": tmnxOamVccvTrNextSenderAddrType,
       "tmnxOamVccvTrNextSenderAddr": tmnxOamVccvTrNextSenderAddr,
       "tmnxOamVccvTrNextRemoteAddrType": tmnxOamVccvTrNextRemoteAddrType,
       "tmnxOamVccvTrNextRemoteAddr": tmnxOamVccvTrNextRemoteAddr,
       "tmnxOamVccvTrNextSaiiGlobalId": tmnxOamVccvTrNextSaiiGlobalId,
       "tmnxOamVccvTrNextSaiiPrefix": tmnxOamVccvTrNextSaiiPrefix,
       "tmnxOamVccvTrNextSaiiAcId": tmnxOamVccvTrNextSaiiAcId,
       "tmnxOamVccvTrNextTaiiGlobalId": tmnxOamVccvTrNextTaiiGlobalId,
       "tmnxOamVccvTrNextTaiiPrefix": tmnxOamVccvTrNextTaiiPrefix,
       "tmnxOamVccvTrNextTaiiAcId": tmnxOamVccvTrNextTaiiAcId,
       "tmnxOamVccvTrNextTpAgi": tmnxOamVccvTrNextTpAgi,
       "tmnxOamVccvTrNextTpSaiiGlobalId": tmnxOamVccvTrNextTpSaiiGlobalId,
       "tmnxOamVccvTrNextTpSaiiNodeId": tmnxOamVccvTrNextTpSaiiNodeId,
       "tmnxOamVccvTrNextTpSaiiAcId": tmnxOamVccvTrNextTpSaiiAcId,
       "tmnxOamVccvTrNextTpTaiiGlobalId": tmnxOamVccvTrNextTpTaiiGlobalId,
       "tmnxOamVccvTrNextTpTaiiNodeId": tmnxOamVccvTrNextTpTaiiNodeId,
       "tmnxOamVccvTrNextTpTaiiAcId": tmnxOamVccvTrNextTpTaiiAcId,
       "tmnxOamP2mpLspTrCtlTable": tmnxOamP2mpLspTrCtlTable,
       "tmnxOamP2mpLspTrCtlEntry": tmnxOamP2mpLspTrCtlEntry,
       "tmnxOamP2mpLspTrCtlLspName": tmnxOamP2mpLspTrCtlLspName,
       "tmnxOamP2mpLspTrCtlInstName": tmnxOamP2mpLspTrCtlInstName,
       "tmnxOamP2mpLspTrCtlLeafIpAddr": tmnxOamP2mpLspTrCtlLeafIpAddr,
       "tmnxOamP2mpLspTrCtlLeafIpAddrType": tmnxOamP2mpLspTrCtlLeafIpAddrType,
       "tmnxOamP2mpLspTrMapTable": tmnxOamP2mpLspTrMapTable,
       "tmnxOamP2mpLspTrMapEntry": tmnxOamP2mpLspTrMapEntry,
       "tmnxOamP2mpLspTrMapIndex": tmnxOamP2mpLspTrMapIndex,
       "tmnxOamP2mpLspTrMapDSIPv4Addr": tmnxOamP2mpLspTrMapDSIPv4Addr,
       "tmnxOamP2mpLspTrMapAddrType": tmnxOamP2mpLspTrMapAddrType,
       "tmnxOamP2mpLspTrMapDSIfAddr": tmnxOamP2mpLspTrMapDSIfAddr,
       "tmnxOamP2mpLspTrMapMTU": tmnxOamP2mpLspTrMapMTU,
       "tmnxOamP2mpLspTrMapP2mpBranch": tmnxOamP2mpLspTrMapP2mpBranch,
       "tmnxOamP2mpLspTrMapP2mpBud": tmnxOamP2mpLspTrMapP2mpBud,
       "tmnxOamP2mpLspTrDSLabelTable": tmnxOamP2mpLspTrDSLabelTable,
       "tmnxOamP2mpLspTrDSLabelEntry": tmnxOamP2mpLspTrDSLabelEntry,
       "tmnxOamP2mpLspTrDSLabelIndex": tmnxOamP2mpLspTrDSLabelIndex,
       "tmnxOamP2mpLspTrDSLabelLabel": tmnxOamP2mpLspTrDSLabelLabel,
       "tmnxOamP2mpLspTrDSLabelProtocol": tmnxOamP2mpLspTrDSLabelProtocol,
       "tmnxOamEthCfmTrCtlTable": tmnxOamEthCfmTrCtlTable,
       "tmnxOamEthCfmTrCtlEntry": tmnxOamEthCfmTrCtlEntry,
       "tmnxOamEthCfmTrCtlTgtMacAddr": tmnxOamEthCfmTrCtlTgtMacAddr,
       "tmnxOamEthCfmTrCtlSrcMdIndex": tmnxOamEthCfmTrCtlSrcMdIndex,
       "tmnxOamEthCfmTrCtlSrcMaIndex": tmnxOamEthCfmTrCtlSrcMaIndex,
       "tmnxOamEthCfmTrCtlSrcMepId": tmnxOamEthCfmTrCtlSrcMepId,
       "tmnxOamEthCfmTrCtlRemoteMepId": tmnxOamEthCfmTrCtlRemoteMepId,
       "tmnxOamEthCfmTrPrHistTable": tmnxOamEthCfmTrPrHistTable,
       "tmnxOamEthCfmTrPrHistEntry": tmnxOamEthCfmTrPrHistEntry,
       "tmnxOamEthCfmTrPrHistIngressMac": tmnxOamEthCfmTrPrHistIngressMac,
       "tmnxOamEthCfmTrPrHistEgressMac": tmnxOamEthCfmTrPrHistEgressMac,
       "tmnxOamEthCfmTrPrHistRelayAction": tmnxOamEthCfmTrPrHistRelayAction,
       "tmnxOamEthCfmTrPrHistForwarded": tmnxOamEthCfmTrPrHistForwarded,
       "tmnxOamEthCfmTrPrHistTerminalMep": tmnxOamEthCfmTrPrHistTerminalMep,
       "tmnxOamLspTrFecStackTable": tmnxOamLspTrFecStackTable,
       "tmnxOamLspTrFecStackEntry": tmnxOamLspTrFecStackEntry,
       "tmnxOamLspTrFecStackFecIndex": tmnxOamLspTrFecStackFecIndex,
       "tmnxOamLspTrFecStackOperType": tmnxOamLspTrFecStackOperType,
       "tmnxOamLspTrFecStackFecSubType": tmnxOamLspTrFecStackFecSubType,
       "tmnxOamLspTrFecStackPrefixType": tmnxOamLspTrFecStackPrefixType,
       "tmnxOamLspTrFecStackPrefix": tmnxOamLspTrFecStackPrefix,
       "tmnxOamLspTrFecStackPrefixLen": tmnxOamLspTrFecStackPrefixLen,
       "tmnxOamLspTrFecStackRemPeerAddrT": tmnxOamLspTrFecStackRemPeerAddrT,
       "tmnxOamLspTrFecStackRemPeerAddr": tmnxOamLspTrFecStackRemPeerAddr,
       "tmnxOamVccvTrTgFec128CtlTable": tmnxOamVccvTrTgFec128CtlTable,
       "tmnxOamVccvTrTgFec128CtlEntry": tmnxOamVccvTrTgFec128CtlEntry,
       "tmnxOamVccvTrTgFec128CtlSrcAddrT": tmnxOamVccvTrTgFec128CtlSrcAddrT,
       "tmnxOamVccvTrTgFec128CtlSrcAddr": tmnxOamVccvTrTgFec128CtlSrcAddr,
       "tmnxOamVccvTrTgFec128CtlDstAddrT": tmnxOamVccvTrTgFec128CtlDstAddrT,
       "tmnxOamVccvTrTgFec128CtlDstAddr": tmnxOamVccvTrTgFec128CtlDstAddr,
       "tmnxOamVccvTrTgFec128CtlPwId": tmnxOamVccvTrTgFec128CtlPwId,
       "tmnxOamVccvTrTgFec128CtlPwType": tmnxOamVccvTrTgFec128CtlPwType,
       "tmnxOamVccvTrTgStaticCtlTable": tmnxOamVccvTrTgStaticCtlTable,
       "tmnxOamVccvTrTgStaticCtlEntry": tmnxOamVccvTrTgStaticCtlEntry,
       "tmnxOamVccvTrTgStaticCtlAgi": tmnxOamVccvTrTgStaticCtlAgi,
       "tmnxOamVccvTrTgStaticCtlSaiiGlbl": tmnxOamVccvTrTgStaticCtlSaiiGlbl,
       "tmnxOamVccvTrTgStaticCtlSaiiNode": tmnxOamVccvTrTgStaticCtlSaiiNode,
       "tmnxOamVccvTrTgStaticCtlSaiiAcId": tmnxOamVccvTrTgStaticCtlSaiiAcId,
       "tmnxOamVccvTrTgStaticCtlTaiiGlbl": tmnxOamVccvTrTgStaticCtlTaiiGlbl,
       "tmnxOamVccvTrTgStaticCtlTaiiNode": tmnxOamVccvTrTgStaticCtlTaiiNode,
       "tmnxOamVccvTrTgStaticCtlTaiiAcId": tmnxOamVccvTrTgStaticCtlTaiiAcId,
       "tmnxOamIcmpTrLabelStackTable": tmnxOamIcmpTrLabelStackTable,
       "tmnxOamIcmpTrLabelStackEntry": tmnxOamIcmpTrLabelStackEntry,
       "tmnxOamIcmpTrLabelStackMemberNum": tmnxOamIcmpTrLabelStackMemberNum,
       "tmnxOamIcmpTrLabelStackLabel": tmnxOamIcmpTrLabelStackLabel,
       "tmnxOamIcmpTrLabelStackExperimnt": tmnxOamIcmpTrLabelStackExperimnt,
       "tmnxOamIcmpTrLabelStackBottom": tmnxOamIcmpTrLabelStackBottom,
       "tmnxOamIcmpTrLabelStackTtl": tmnxOamIcmpTrLabelStackTtl,
       "tmnxOamBierTrCtlTable": tmnxOamBierTrCtlTable,
       "tmnxOamBierTrCtlEntry": tmnxOamBierTrCtlEntry,
       "tmnxOamBierTrCtlSubDomain": tmnxOamBierTrCtlSubDomain,
       "tmnxOamBierTrCtlBfrId": tmnxOamBierTrCtlBfrId,
       "tmnxOamBierTrCtlBfrPfxAddrType": tmnxOamBierTrCtlBfrPfxAddrType,
       "tmnxOamBierTrCtlBfrPfxAddress": tmnxOamBierTrCtlBfrPfxAddress,
       "tmnxOamBierTrProbeHistoryTable": tmnxOamBierTrProbeHistoryTable,
       "tmnxOamBierTrProbeHistoryEntry": tmnxOamBierTrProbeHistoryEntry,
       "tmnxOamBierTrHistoryBfrId": tmnxOamBierTrHistoryBfrId,
       "tmnxOamBierTrHistoryReturnCode": tmnxOamBierTrHistoryReturnCode,
       "tmnxOamBierTrHistoryUpStrIfAddrT": tmnxOamBierTrHistoryUpStrIfAddrT,
       "tmnxOamBierTrHistoryUpStrIfAddr": tmnxOamBierTrHistoryUpStrIfAddr,
       "tmnxOamBierTrHistoryUpStrIfNum": tmnxOamBierTrHistoryUpStrIfNum,
       "tmnxOamBierTrHistoryDnStrAddrTyp": tmnxOamBierTrHistoryDnStrAddrTyp,
       "tmnxOamBierTrHistoryDnStrAddr": tmnxOamBierTrHistoryDnStrAddr,
       "tmnxOamBierTrHistoryDnStrIfAddrT": tmnxOamBierTrHistoryDnStrIfAddrT,
       "tmnxOamBierTrHistoryDnStrIfAddr": tmnxOamBierTrHistoryDnStrIfAddr,
       "tmnxOamBierTrHistoryDnStrIfNum": tmnxOamBierTrHistoryDnStrIfNum,
       "tmnxOamIcmpTrCtlTable": tmnxOamIcmpTrCtlTable,
       "tmnxOamIcmpTrCtlEntry": tmnxOamIcmpTrCtlEntry,
       "tmnxOamIcmpTrCtlProtocol": tmnxOamIcmpTrCtlProtocol,
       "tmnxOamIcmpTrCtlDestTcpUdpPort": tmnxOamIcmpTrCtlDestTcpUdpPort,
       "tmnxOamIcmpTrCtlDestUdpPortFixed": tmnxOamIcmpTrCtlDestUdpPortFixed,
       "tmnxOamIcmpTrCtlPadSize": tmnxOamIcmpTrCtlPadSize,
       "tmnxOamSaaObjs": tmnxOamSaaObjs,
       "tmnxOamSaaNotifyObjects": tmnxOamSaaNotifyObjects,
       "tmnxOamSaaCtlTable": tmnxOamSaaCtlTable,
       "tmnxOamSaaCtlEntry": tmnxOamSaaCtlEntry,
       "tmnxOamSaaCtlOwnerIndex": tmnxOamSaaCtlOwnerIndex,
       "tmnxOamSaaCtlTestIndex": tmnxOamSaaCtlTestIndex,
       "tmnxOamSaaCtlRowStatus": tmnxOamSaaCtlRowStatus,
       "tmnxOamSaaCtlStorageType": tmnxOamSaaCtlStorageType,
       "tmnxOamSaaCtlLastChanged": tmnxOamSaaCtlLastChanged,
       "tmnxOamSaaCtlAdminStatus": tmnxOamSaaCtlAdminStatus,
       "tmnxOamSaaCtlDescr": tmnxOamSaaCtlDescr,
       "tmnxOamSaaCtlTestMode": tmnxOamSaaCtlTestMode,
       "tmnxOamSaaCtlRuns": tmnxOamSaaCtlRuns,
       "tmnxOamSaaCtlFailures": tmnxOamSaaCtlFailures,
       "tmnxOamSaaCtlLastRunResult": tmnxOamSaaCtlLastRunResult,
       "tmnxOamSaaCtlAcctPolicyId": tmnxOamSaaCtlAcctPolicyId,
       "tmnxOamSaaCtlSuppressAccounting": tmnxOamSaaCtlSuppressAccounting,
       "tmnxOamSaaCtlContinuous": tmnxOamSaaCtlContinuous,
       "tmnxOamSaaCtlKeepProbeHistoryAdm": tmnxOamSaaCtlKeepProbeHistoryAdm,
       "tmnxOamSaaCtlKeepProbeHistoryOpr": tmnxOamSaaCtlKeepProbeHistoryOpr,
       "tmnxOamSaaThresholdTable": tmnxOamSaaThresholdTable,
       "tmnxOamSaaThresholdEntry": tmnxOamSaaThresholdEntry,
       "tmnxOamSaaTType": tmnxOamSaaTType,
       "tmnxOamSaaTDirection": tmnxOamSaaTDirection,
       "tmnxOamSaaTRowStatus": tmnxOamSaaTRowStatus,
       "tmnxOamSaaTLastChanged": tmnxOamSaaTLastChanged,
       "tmnxOamSaaTThreshold": tmnxOamSaaTThreshold,
       "tmnxOamSaaTValue": tmnxOamSaaTValue,
       "tmnxOamSaaTLastSent": tmnxOamSaaTLastSent,
       "tmnxOamSaaTTestMode": tmnxOamSaaTTestMode,
       "tmnxOamSaaTTestRunIndex": tmnxOamSaaTTestRunIndex,
       "tmnxOamMobGatewayObjs": tmnxOamMobGatewayObjs,
       "tmnxOamMobGtpPingCtlTable": tmnxOamMobGtpPingCtlTable,
       "tmnxOamMobGtpPingCtlEntry": tmnxOamMobGtpPingCtlEntry,
       "tmnxOamMobGtpPingRefPointType": tmnxOamMobGtpPingRefPointType,
       "tmnxOamMobGtpPingVRtrId": tmnxOamMobGtpPingVRtrId,
       "tmnxOamMobGtpPingPort": tmnxOamMobGtpPingPort,
       "tmnxOamMobGtpPingGateway": tmnxOamMobGtpPingGateway,
       "tmnxOamDnsPingCtlTable": tmnxOamDnsPingCtlTable,
       "tmnxOamGeneralObjs": tmnxOamGeneralObjs,
       "tmnxOamMplsPduTimeStampFormat": tmnxOamMplsPduTimeStampFormat,
       "tmnxOamGeneralStats": tmnxOamGeneralStats,
       "tmnxOamSysPerfOprLimitTx": tmnxOamSysPerfOprLimitTx,
       "tmnxOamSysPerfCfgLimitTx": tmnxOamSysPerfCfgLimitTx,
       "tmnxOamSysPerfCfgTotalTx": tmnxOamSysPerfCfgTotalTx,
       "tmnxOamSysPerfLastClearedTime": tmnxOamSysPerfLastClearedTime,
       "tmnxOamSysPerfLocalTestTx": tmnxOamSysPerfLocalTestTx,
       "tmnxOamSysPerfRemoteTestRx": tmnxOamSysPerfRemoteTestRx,
       "tmnxOamSysPerfReqTypeTable": tmnxOamSysPerfReqTypeTable,
       "tmnxOamSysPerfReqTypeEntry": tmnxOamSysPerfReqTypeEntry,
       "tmnxOamSysPerfReqTypeName": tmnxOamSysPerfReqTypeName,
       "tmnxOamSysPerfReqTypeLocalTestTx": tmnxOamSysPerfReqTypeLocalTestTx,
       "tmnxOamSysPerfReqTypeRemoteTstRx": tmnxOamSysPerfReqTypeRemoteTstRx,
       "tmnxOamSysSessionLimit": tmnxOamSysSessionLimit,
       "tmnxOamSysSessionCount": tmnxOamSysSessionCount,
       "tmnxOamSysBgIcmpBrgSessionLimit": tmnxOamSysBgIcmpBrgSessionLimit,
       "tmnxOamSysBgIcmpBrgSessionCount": tmnxOamSysBgIcmpBrgSessionCount,
       "tmnxOamSysLspSelfPingSessLimit": tmnxOamSysLspSelfPingSessLimit,
       "tmnxOamSysLspSelfPingSessCount": tmnxOamSysLspSelfPingSessCount,
       "tmnxOamSysPerfCfgLspSelfTxLimit": tmnxOamSysPerfCfgLspSelfTxLimit,
       "tmnxOamSysPerfCfgLspSelfTxTotal": tmnxOamSysPerfCfgLspSelfTxTotal,
       "tmnxOamSysBgIcmpIfCtlSessLimit": tmnxOamSysBgIcmpIfCtlSessLimit,
       "tmnxOamSysBgIcmpIfCtlSessCount": tmnxOamSysBgIcmpIfCtlSessCount,
       "tmnxOamSysTestLimit": tmnxOamSysTestLimit,
       "tmnxOamSysTestCount": tmnxOamSysTestCount,
       "tmnxOamSysTxLimit": tmnxOamSysTxLimit,
       "tmnxOamSysTxTotal": tmnxOamSysTxTotal,
       "tmnxOamSysShareTestLimit": tmnxOamSysShareTestLimit,
       "tmnxOamSysShareTestCount": tmnxOamSysShareTestCount,
       "tmnxOamSysShareTxLimit": tmnxOamSysShareTxLimit,
       "tmnxOamSysShareTxTotal": tmnxOamSysShareTxTotal,
       "tmnxOamMplsEchoDownstreamMapTlv": tmnxOamMplsEchoDownstreamMapTlv,
       "tmnxOamDiagObjs": tmnxOamDiagObjs,
       "tmnxOamDiagCtlTable": tmnxOamDiagCtlTable,
       "tmnxOamDiagCtlEntry": tmnxOamDiagCtlEntry,
       "tmnxOamDiagCtlOwnerIndex": tmnxOamDiagCtlOwnerIndex,
       "tmnxOamDiagCtlTestIndex": tmnxOamDiagCtlTestIndex,
       "tmnxOamDiagCtlRowStatus": tmnxOamDiagCtlRowStatus,
       "tmnxOamDiagCtlLastChanged": tmnxOamDiagCtlLastChanged,
       "tmnxOamDiagCtlTestMode": tmnxOamDiagCtlTestMode,
       "tmnxOamDiagCtlAdminState": tmnxOamDiagCtlAdminState,
       "tmnxOamFindEgrDiagCtlTable": tmnxOamFindEgrDiagCtlTable,
       "tmnxOamFindEgrDiagCtlEntry": tmnxOamFindEgrDiagCtlEntry,
       "tmnxOamFindEgrDiagCtlLastChanged": tmnxOamFindEgrDiagCtlLastChanged,
       "tmnxOamFindEgrDiagCtlPacketNum": tmnxOamFindEgrDiagCtlPacketNum,
       "tmnxOamFindEgrDiagCtlIngPortId": tmnxOamFindEgrDiagCtlIngPortId,
       "tmnxOamFindEgrDiagResultsTable": tmnxOamFindEgrDiagResultsTable,
       "tmnxOamFindEgrDiagResultsEntry": tmnxOamFindEgrDiagResultsEntry,
       "tmnxOamDiagResultsTestRunIndex": tmnxOamDiagResultsTestRunIndex,
       "tmnxOamFindEgrDiagOperState": tmnxOamFindEgrDiagOperState,
       "tmnxOamFindEgrDiagEgressPort": tmnxOamFindEgrDiagEgressPort,
       "tmnxOamFindEgrDiagEgrRtrInstName": tmnxOamFindEgrDiagEgrRtrInstName,
       "tmnxOamFindEgrDiagEgressIfName": tmnxOamFindEgrDiagEgressIfName,
       "tmnxOamFindEgrDiagNextHopAddrTyp": tmnxOamFindEgrDiagNextHopAddrTyp,
       "tmnxOamFindEgrDiagNextHopAddress": tmnxOamFindEgrDiagNextHopAddress,
       "tmnxOamBuildPktCtlTable": tmnxOamBuildPktCtlTable,
       "tmnxOamBuildPktCtlEntry": tmnxOamBuildPktCtlEntry,
       "tmnxOamBuildPktNum": tmnxOamBuildPktNum,
       "tmnxOamBuildPktRowStatus": tmnxOamBuildPktRowStatus,
       "tmnxOamBuildPktLastChanged": tmnxOamBuildPktLastChanged,
       "tmnxOamBuildPktHeaderSeq": tmnxOamBuildPktHeaderSeq,
       "tmnxOamBuildPktHdrCtlTable": tmnxOamBuildPktHdrCtlTable,
       "tmnxOamBuildPktHdrCtlEntry": tmnxOamBuildPktHdrCtlEntry,
       "tmnxOamBuildPktHeaderNum": tmnxOamBuildPktHeaderNum,
       "tmnxOamBuildPktHdrRowStatus": tmnxOamBuildPktHdrRowStatus,
       "tmnxOamBuildPktHdrLastChanged": tmnxOamBuildPktHdrLastChanged,
       "tmnxOamBuildPktHdrType": tmnxOamBuildPktHdrType,
       "tmnxOamBuildPktHdrOvrCtlTable": tmnxOamBuildPktHdrOvrCtlTable,
       "tmnxOamBuildPktHdrOvrCtlEntry": tmnxOamBuildPktHdrOvrCtlEntry,
       "tmnxOamBuildPktHdrOvrRowStatus": tmnxOamBuildPktHdrOvrRowStatus,
       "tmnxOamBuildPktHdrOvrLastChanged": tmnxOamBuildPktHdrOvrLastChanged,
       "tmnxOamBuildPktEthCtlTable": tmnxOamBuildPktEthCtlTable,
       "tmnxOamBuildPktEthCtlEntry": tmnxOamBuildPktEthCtlEntry,
       "tmnxOamBuildPktNumOrZero": tmnxOamBuildPktNumOrZero,
       "tmnxOamBuildPktEthLastChanged": tmnxOamBuildPktEthLastChanged,
       "tmnxOamBuildPktEthDstMacAddr": tmnxOamBuildPktEthDstMacAddr,
       "tmnxOamBuildPktEthSrcMacAddr": tmnxOamBuildPktEthSrcMacAddr,
       "tmnxOamBuildPktIpCtlTable": tmnxOamBuildPktIpCtlTable,
       "tmnxOamBuildPktIpCtlEntry": tmnxOamBuildPktIpCtlEntry,
       "tmnxOamBuildPktIpLastChanged": tmnxOamBuildPktIpLastChanged,
       "tmnxOamBuildPktIpDstIpAddrType": tmnxOamBuildPktIpDstIpAddrType,
       "tmnxOamBuildPktIpDstIpAddress": tmnxOamBuildPktIpDstIpAddress,
       "tmnxOamBuildPktIpSrcIpAddrType": tmnxOamBuildPktIpSrcIpAddrType,
       "tmnxOamBuildPktIpSrcIpAddress": tmnxOamBuildPktIpSrcIpAddress,
       "tmnxOamBuildPktIpDscp": tmnxOamBuildPktIpDscp,
       "tmnxOamBuildPktIPv4MoreFragments": tmnxOamBuildPktIPv4MoreFragments,
       "tmnxOamBuildPktTcpUdpCtlTable": tmnxOamBuildPktTcpUdpCtlTable,
       "tmnxOamBuildPktTcpUdpCtlEntry": tmnxOamBuildPktTcpUdpCtlEntry,
       "tmnxOamBuildPktTcpUdpLastChanged": tmnxOamBuildPktTcpUdpLastChanged,
       "tmnxOamBuildPktTcpUdpDstPort": tmnxOamBuildPktTcpUdpDstPort,
       "tmnxOamBuildPktTcpUdpSrcPort": tmnxOamBuildPktTcpUdpSrcPort,
       "tmnxOamBuildPktDot1qCtlTable": tmnxOamBuildPktDot1qCtlTable,
       "tmnxOamBuildPktDot1qCtlEntry": tmnxOamBuildPktDot1qCtlEntry,
       "tmnxOamBuildPktDot1qLastChanged": tmnxOamBuildPktDot1qLastChanged,
       "tmnxOamBuildPktDot1qPrioCodePt": tmnxOamBuildPktDot1qPrioCodePt,
       "tmnxOamBuildPktDot1qTagProtoId": tmnxOamBuildPktDot1qTagProtoId,
       "tmnxOamBuildPktDot1qVlanId": tmnxOamBuildPktDot1qVlanId,
       "tmnxOamBuildPktIPsecAuthCtlTable": tmnxOamBuildPktIPsecAuthCtlTable,
       "tmnxOamBuildPktIPsecAuthCtlEntry": tmnxOamBuildPktIPsecAuthCtlEntry,
       "tmnxOamBuildPktIPsecAuthLastChgd": tmnxOamBuildPktIPsecAuthLastChgd,
       "tmnxOamBuildPktIPsecAuthSecPrIdx": tmnxOamBuildPktIPsecAuthSecPrIdx,
       "tmnxOamBuildPktPbbCtlTable": tmnxOamBuildPktPbbCtlTable,
       "tmnxOamBuildPktPbbCtlEntry": tmnxOamBuildPktPbbCtlEntry,
       "tmnxOamBuildPktPbbLastChanged": tmnxOamBuildPktPbbLastChanged,
       "tmnxOamBuildPktPbbIsid": tmnxOamBuildPktPbbIsid,
       "tmnxOamBuildPktPbbTagProtocolId": tmnxOamBuildPktPbbTagProtocolId,
       "tmnxOamBuildPktL2tpCtlTable": tmnxOamBuildPktL2tpCtlTable,
       "tmnxOamBuildPktL2tpCtlEntry": tmnxOamBuildPktL2tpCtlEntry,
       "tmnxOamBuildPktL2tpLastChanged": tmnxOamBuildPktL2tpLastChanged,
       "tmnxOamBuildPktL2tpSessionId": tmnxOamBuildPktL2tpSessionId,
       "tmnxOamBuildPktL2tpTunnelId": tmnxOamBuildPktL2tpTunnelId,
       "tmnxOamBuildPktMplsCtlTable": tmnxOamBuildPktMplsCtlTable,
       "tmnxOamBuildPktMplsCtlEntry": tmnxOamBuildPktMplsCtlEntry,
       "tmnxOamBuildPktMplsLastChanged": tmnxOamBuildPktMplsLastChanged,
       "tmnxOamBuildPktMplsLabel": tmnxOamBuildPktMplsLabel,
       "tmnxOamBuildPktMplsTrafficClass": tmnxOamBuildPktMplsTrafficClass,
       "tmnxOamBuildPktGtpUserCtlTable": tmnxOamBuildPktGtpUserCtlTable,
       "tmnxOamBuildPktGtpUserCtlEntry": tmnxOamBuildPktGtpUserCtlEntry,
       "tmnxOamBuildPktGtpUserLastChgd": tmnxOamBuildPktGtpUserLastChgd,
       "tmnxOamBuildPktGtpUserTunnEpIdHi": tmnxOamBuildPktGtpUserTunnEpIdHi,
       "tmnxOamBuildPktGtpUserTunnEpIdLo": tmnxOamBuildPktGtpUserTunnEpIdLo,
       "tmnxOamNotificationObjs": tmnxOamNotificationObjs,
       "tmnxOamTestRunIndex": tmnxOamTestRunIndex,
       "tmnxOamIfPingObjs": tmnxOamIfPingObjs,
       "tmnxOamIfPingTmplCtlTable": tmnxOamIfPingTmplCtlTable,
       "tmnxOamIfPingTmplCtlEntry": tmnxOamIfPingTmplCtlEntry,
       "tmnxOamIfPingTmplCtlName": tmnxOamIfPingTmplCtlName,
       "tmnxOamIfPingTmplCtlRowStatus": tmnxOamIfPingTmplCtlRowStatus,
       "tmnxOamIfPingTmplCtlLastMgmtChg": tmnxOamIfPingTmplCtlLastMgmtChg,
       "tmnxOamIfPingTmplCtlDescription": tmnxOamIfPingTmplCtlDescription,
       "tmnxOamIfPingTmplCtlDscp": tmnxOamIfPingTmplCtlDscp,
       "tmnxOamIfPingTmplCtlDot1p": tmnxOamIfPingTmplCtlDot1p,
       "tmnxOamIfPingTmplCtlInterval": tmnxOamIfPingTmplCtlInterval,
       "tmnxOamIfPingTmplCtlTimeout": tmnxOamIfPingTmplCtlTimeout,
       "tmnxOamIfPingTmplCtlFailThrld": tmnxOamIfPingTmplCtlFailThrld,
       "tmnxOamIfPingTmplCtlReactInt": tmnxOamIfPingTmplCtlReactInt,
       "tmnxOamIfPingTmplCtlReactFailThr": tmnxOamIfPingTmplCtlReactFailThr,
       "tmnxOamIfPingTmplCtlReactTimeout": tmnxOamIfPingTmplCtlReactTimeout,
       "tmnxOamIfPingTmplCtlReactThrld": tmnxOamIfPingTmplCtlReactThrld,
       "tmnxOamIfPingTmplCtlSize": tmnxOamIfPingTmplCtlSize,
       "tmnxOamIfPingTmplCtlTtl": tmnxOamIfPingTmplCtlTtl,
       "tmnxOamIfPingTmplCtlSync": tmnxOamIfPingTmplCtlSync,
       "tmnxOamIfPingIfTable": tmnxOamIfPingIfTable,
       "tmnxOamIfPingIfEntry": tmnxOamIfPingIfEntry,
       "tmnxOamIfPingIfRowStatus": tmnxOamIfPingIfRowStatus,
       "tmnxOamIfPingIfTemplate": tmnxOamIfPingIfTemplate,
       "tmnxOamIfPingIfLastChanged": tmnxOamIfPingIfLastChanged,
       "tmnxOamIfPingIfAdminState": tmnxOamIfPingIfAdminState,
       "tmnxOamIfPingIfDestAddrType": tmnxOamIfPingIfDestAddrType,
       "tmnxOamIfPingIfDestAddr": tmnxOamIfPingIfDestAddr,
       "tmnxOamIfPingIfFailThrldCnt": tmnxOamIfPingIfFailThrldCnt,
       "tmnxOamIfPingIfPassThrldCnt": tmnxOamIfPingIfPassThrldCnt,
       "tmnxOamIfPingIfCtlDscp": tmnxOamIfPingIfCtlDscp,
       "tmnxOamIfPingIfCtlDot1p": tmnxOamIfPingIfCtlDot1p,
       "tmnxOamIfPingIfCtlInterval": tmnxOamIfPingIfCtlInterval,
       "tmnxOamIfPingIfCtlTimeout": tmnxOamIfPingIfCtlTimeout,
       "tmnxOamIfPingIfCtlFailThrld": tmnxOamIfPingIfCtlFailThrld,
       "tmnxOamIfPingIfCtlReactInt": tmnxOamIfPingIfCtlReactInt,
       "tmnxOamIfPingIfCtlReactFailThr": tmnxOamIfPingIfCtlReactFailThr,
       "tmnxOamIfPingIfCtlReactTimeout": tmnxOamIfPingIfCtlReactTimeout,
       "tmnxOamIfPingIfCtlReactThrld": tmnxOamIfPingIfCtlReactThrld,
       "tmnxOamIfPingIfCtlSize": tmnxOamIfPingIfCtlSize,
       "tmnxOamIfPingIfCtlTtl": tmnxOamIfPingIfCtlTtl,
       "tmnxOamIfPingIfCurrentInterval": tmnxOamIfPingIfCurrentInterval,
       "tmnxOamIfPingIfCurrentState": tmnxOamIfPingIfCurrentState,
       "tmnxOamLnkMeasObjs": tmnxOamLnkMeasObjs,
       "tmnxOamLnkMeasTmplCtlTable": tmnxOamLnkMeasTmplCtlTable,
       "tmnxOamLnkMeasTmplCtlEntry": tmnxOamLnkMeasTmplCtlEntry,
       "tmnxOamLnkMeasTmplCtlName": tmnxOamLnkMeasTmplCtlName,
       "tmnxOamLnkMeasTmplCtlRowStatus": tmnxOamLnkMeasTmplCtlRowStatus,
       "tmnxOamLnkMeasTmplCtlLastMgmtChg": tmnxOamLnkMeasTmplCtlLastMgmtChg,
       "tmnxOamLnkMeasTmplCtlDescription": tmnxOamLnkMeasTmplCtlDescription,
       "tmnxOamLnkMeasTmplCtlUnidirMeasT": tmnxOamLnkMeasTmplCtlUnidirMeasT,
       "tmnxOamLnkMeasTmplCtlDelayMeasTy": tmnxOamLnkMeasTmplCtlDelayMeasTy,
       "tmnxOamLnkMeasTmplCtlInterval": tmnxOamLnkMeasTmplCtlInterval,
       "tmnxOamLnkMeasTmplCtlLastRepHold": tmnxOamLnkMeasTmplCtlLastRepHold,
       "tmnxOamLnkMeasTmplCtlDscpEgrRmrk": tmnxOamLnkMeasTmplCtlDscpEgrRmrk,
       "tmnxOamLnkMeasTmplCtlIpv6UdpZero": tmnxOamLnkMeasTmplCtlIpv6UdpZero,
       "tmnxOamLnkMeasTmplCtlDscpName": tmnxOamLnkMeasTmplCtlDscpName,
       "tmnxOamLnkMeasTmplCtlDstUdpPort": tmnxOamLnkMeasTmplCtlDstUdpPort,
       "tmnxOamLnkMeasTmplCtlFC": tmnxOamLnkMeasTmplCtlFC,
       "tmnxOamLnkMeasTmplCtlProfile": tmnxOamLnkMeasTmplCtlProfile,
       "tmnxOamLnkMeasTmplCtlTwlTmStpFmt": tmnxOamLnkMeasTmplCtlTwlTmStpFmt,
       "tmnxOamLnkMeasTmplCtlTwlTimeLive": tmnxOamLnkMeasTmplCtlTwlTimeLive,
       "tmnxOamLnkMeasTmplCtlSWMultplir": tmnxOamLnkMeasTmplCtlSWMultplir,
       "tmnxOamLnkMeasTmplCtlSWIntegrity": tmnxOamLnkMeasTmplCtlSWIntegrity,
       "tmnxOamLnkMeasTmplCtlSWThrldRel": tmnxOamLnkMeasTmplCtlSWThrldRel,
       "tmnxOamLnkMeasTmplCtlSWThrldAbs": tmnxOamLnkMeasTmplCtlSWThrldAbs,
       "tmnxOamLnkMeasTmplCtlASWMultplir": tmnxOamLnkMeasTmplCtlASWMultplir,
       "tmnxOamLnkMeasTmplCtlASWIntgrity": tmnxOamLnkMeasTmplCtlASWIntgrity,
       "tmnxOamLnkMeasTmplCtlASWThrldRel": tmnxOamLnkMeasTmplCtlASWThrldRel,
       "tmnxOamLnkMeasTmplCtlASWThrldAbs": tmnxOamLnkMeasTmplCtlASWThrldAbs,
       "tmnxOamLnkMeasTmplCtlAdminState": tmnxOamLnkMeasTmplCtlAdminState,
       "tmnxOamLnkMeasIfResTable": tmnxOamLnkMeasIfResTable,
       "tmnxOamLnkMeasIfResEntry": tmnxOamLnkMeasIfResEntry,
       "tmnxOamLnkMeasIfResSrcIpAddrTy": tmnxOamLnkMeasIfResSrcIpAddrTy,
       "tmnxOamLnkMeasIfResSrcIpAddr": tmnxOamLnkMeasIfResSrcIpAddr,
       "tmnxOamLnkMeasIfResSrcIpAssigned": tmnxOamLnkMeasIfResSrcIpAssigned,
       "tmnxOamLnkMeasIfResDstIpAddrTy": tmnxOamLnkMeasIfResDstIpAddrTy,
       "tmnxOamLnkMeasIfResDstIpAddr": tmnxOamLnkMeasIfResDstIpAddr,
       "tmnxOamLnkMeasIfResDstIpAssigned": tmnxOamLnkMeasIfResDstIpAssigned,
       "tmnxOamLnkMeasIfResOperState": tmnxOamLnkMeasIfResOperState,
       "tmnxOamLnkMeasIfResFailureCond": tmnxOamLnkMeasIfResFailureCond,
       "tmnxOamLnkMeasIfResDetctbleTxErr": tmnxOamLnkMeasIfResDetctbleTxErr,
       "tmnxOamLnkMeasIfResReporting": tmnxOamLnkMeasIfResReporting,
       "tmnxOamLnkMeasIfResDelayReported": tmnxOamLnkMeasIfResDelayReported,
       "tmnxOamLnkMeasIfResTimestampUTC": tmnxOamLnkMeasIfResTimestampUTC,
       "tmnxOamLnkMeasIfResTriggeredBy": tmnxOamLnkMeasIfResTriggeredBy,
       "tmnxOamLnkMeasIfResNewestASWIdx": tmnxOamLnkMeasIfResNewestASWIdx,
       "tmnxOamLnkMeasIfResNewestSWIdx": tmnxOamLnkMeasIfResNewestSWIdx,
       "tmnxOamLnkMeasIfResASWTable": tmnxOamLnkMeasIfResASWTable,
       "tmnxOamLnkMeasIfResASWEntry": tmnxOamLnkMeasIfResASWEntry,
       "tmnxOamLnkMeasIfResASWIndex": tmnxOamLnkMeasIfResASWIndex,
       "tmnxOamLnkMeasIfResASWEndUTC": tmnxOamLnkMeasIfResASWEndUTC,
       "tmnxOamLnkMeasIfResASWState": tmnxOamLnkMeasIfResASWState,
       "tmnxOamLnkMeasIfResASWWindCount": tmnxOamLnkMeasIfResASWWindCount,
       "tmnxOamLnkMeasIfResASWReportMin": tmnxOamLnkMeasIfResASWReportMin,
       "tmnxOamLnkMeasIfResASWReportMax": tmnxOamLnkMeasIfResASWReportMax,
       "tmnxOamLnkMeasIfResASWReportAvg": tmnxOamLnkMeasIfResASWReportAvg,
       "tmnxOamLnkMeasIfResASWIntegrity": tmnxOamLnkMeasIfResASWIntegrity,
       "tmnxOamLnkMeasIfResASWResult": tmnxOamLnkMeasIfResASWResult,
       "tmnxOamLnkMeasIfResSWTable": tmnxOamLnkMeasIfResSWTable,
       "tmnxOamLnkMeasIfResSWEntry": tmnxOamLnkMeasIfResSWEntry,
       "tmnxOamLnkMeasIfResSWIndex": tmnxOamLnkMeasIfResSWIndex,
       "tmnxOamLnkMeasIfResSWEndUTC": tmnxOamLnkMeasIfResSWEndUTC,
       "tmnxOamLnkMeasIfResSWState": tmnxOamLnkMeasIfResSWState,
       "tmnxOamLnkMeasIfResSWSent": tmnxOamLnkMeasIfResSWSent,
       "tmnxOamLnkMeasIfResSWReceived": tmnxOamLnkMeasIfResSWReceived,
       "tmnxOamLnkMeasIfResSWMin": tmnxOamLnkMeasIfResSWMin,
       "tmnxOamLnkMeasIfResSWMax": tmnxOamLnkMeasIfResSWMax,
       "tmnxOamLnkMeasIfResSWAvg": tmnxOamLnkMeasIfResSWAvg,
       "tmnxOamLnkMeasIfResSWErrors": tmnxOamLnkMeasIfResSWErrors,
       "tmnxOamLnkMeasIfResSWIntegrity": tmnxOamLnkMeasIfResSWIntegrity,
       "tmnxOamLnkMeasIfResSWResult": tmnxOamLnkMeasIfResSWResult,
       "tmnxOamTestNotifications": tmnxOamTestNotifications,
       "tmnxOamPingNotifyPrefix": tmnxOamPingNotifyPrefix,
       "tmnxOamPingNotifications": tmnxOamPingNotifications,
       "tmnxOamPingProbeFailed": tmnxOamPingProbeFailed,
       "tmnxOamPingTestFailed": tmnxOamPingTestFailed,
       "tmnxOamPingTestCompleted": tmnxOamPingTestCompleted,
       "tmnxOamPingProbeFailedV2": tmnxOamPingProbeFailedV2,
       "tmnxOamPingTestFailedV2": tmnxOamPingTestFailedV2,
       "tmnxOamPingTestCompletedV2": tmnxOamPingTestCompletedV2,
       "tmnxAncpLoopbackTestCompleted": tmnxAncpLoopbackTestCompleted,
       "tmnxOamPingProbeFailedV3": tmnxOamPingProbeFailedV3,
       "tmnxOamPingTestFailedV3": tmnxOamPingTestFailedV3,
       "tmnxOamPingTestCompletedV3": tmnxOamPingTestCompletedV3,
       "tmnxOamTraceRouteNotifyPrefix": tmnxOamTraceRouteNotifyPrefix,
       "tmnxOamTraceRouteNotifications": tmnxOamTraceRouteNotifications,
       "tmnxOamTrPathChange": tmnxOamTrPathChange,
       "tmnxOamTrTestFailed": tmnxOamTrTestFailed,
       "tmnxOamTrTestCompleted": tmnxOamTrTestCompleted,
       "tmnxOamLdpTtraceAutoDiscState": tmnxOamLdpTtraceAutoDiscState,
       "tmnxOamLdpTtraceFecProbeState": tmnxOamLdpTtraceFecProbeState,
       "tmnxOamLdpTtraceFecDisStatus": tmnxOamLdpTtraceFecDisStatus,
       "tmnxOamLdpTtraceFecPFailUpdate": tmnxOamLdpTtraceFecPFailUpdate,
       "tmnxOamSaaNotifyPrefix": tmnxOamSaaNotifyPrefix,
       "tmnxOamSaaNotifications": tmnxOamSaaNotifications,
       "tmnxOamSaaThreshold": tmnxOamSaaThreshold,
       "tmnxOamDiagNotifyPrefix": tmnxOamDiagNotifyPrefix,
       "tmnxOamDiagNotifications": tmnxOamDiagNotifications,
       "tmnxOamDiagTestCompleted": tmnxOamDiagTestCompleted}
)
