# SNMP MIB module (TN-OAM-TEST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\1830\TN-OAM-TEST-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:12:08 2025
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

(Dot1agCfmMepIdOrZero,) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "Dot1agCfmMepIdOrZero")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

(RouterID,) = mibBuilder.importSymbols(
    "OSPF-MIB",
    "RouterID")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(SdpBindVcType,
 SdpId) = mibBuilder.importSymbols(
    "TN-SERV-MIB",
    "SdpBindVcType",
    "SdpId")

(IpAddressPrefixLength,
 SdpBindId,
 TFCName,
 TItemDescription,
 TLNamedItemOrEmpty,
 TNamedItemOrEmpty,
 TProfile,
 TmnxAdminState,
 TmnxMplsTpGlobalID,
 TmnxMplsTpNodeID,
 TmnxPwGlobalIdOrZero,
 TmnxServId,
 TmnxSpokeSdpIdOrZero,
 TmnxStrSapId,
 TmnxVRtrID,
 TmnxVcIdOrNone) = mibBuilder.importSymbols(
    "TN-TC-MIB",
    "IpAddressPrefixLength",
    "SdpBindId",
    "TFCName",
    "TItemDescription",
    "TLNamedItemOrEmpty",
    "TNamedItemOrEmpty",
    "TProfile",
    "TmnxAdminState",
    "TmnxMplsTpGlobalID",
    "TmnxMplsTpNodeID",
    "TmnxPwGlobalIdOrZero",
    "TmnxServId",
    "TmnxSpokeSdpIdOrZero",
    "TmnxStrSapId",
    "TmnxVRtrID",
    "TmnxVcIdOrNone")

(tnSRMIBModules,
 tnSRNotifyPrefix,
 tnSRObjs) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnSRMIBModules",
    "tnSRNotifyPrefix",
    "tnSRObjs")

(tnSysSwitchId,) = mibBuilder.importSymbols(
    "TROPIC-SYSTEM-MIB",
    "tnSysSwitchId")


# MODULE-IDENTITY

tnOamTestMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 5, 1, 3, 11)
)
if mibBuilder.loadTexts:
    tnOamTestMIBModule.setRevisions(
        ("2021-06-04 00:00",
         "2020-06-19 00:00",
         "2019-11-15 00:00",
         "2019-03-29 00:00",
         "2015-08-24 00:00",
         "2015-08-05 00:00",
         "2015-05-05 00:00",
         "2013-08-22 00:00",
         "2013-03-26 00:00",
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
              3)
        )
    )
    namedValues = NamedValues(
        *(("unspecified", 1),
          ("static", 2),
          ("bgpLabeledPrefix", 3))
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
              9)
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
          ("sdpBindId", 9))
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
              155)
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
          ("l2tpv3DeliveryTypeUnsupported", 155))
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
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("static", 1),
          ("bgp", 2),
          ("ldp", 3),
          ("rsvpTe", 4),
          ("crLdp", 5))
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

_TnOamTestObjs_ObjectIdentity = ObjectIdentity
tnOamTestObjs = _TnOamTestObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11)
)
_TnOamPingObjs_ObjectIdentity = ObjectIdentity
tnOamPingObjs = _TnOamPingObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1)
)
_TnOamPingCtlAttributeTotal_Type = Integer32
_TnOamPingCtlAttributeTotal_Object = MibScalar
tnOamPingCtlAttributeTotal = _TnOamPingCtlAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 3),
    _TnOamPingCtlAttributeTotal_Type()
)
tnOamPingCtlAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingCtlAttributeTotal.setStatus("current")
_TnOamPingCtlTable_Object = MibTable
tnOamPingCtlTable = _TnOamPingCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4)
)
if mibBuilder.loadTexts:
    tnOamPingCtlTable.setStatus("current")
_TnOamPingCtlEntry_Object = MibTableRow
tnOamPingCtlEntry = _TnOamPingCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1)
)
tnOamPingCtlEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-OAM-TEST-MIB", "tnOamPingCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tnOamPingCtlEntry.setStatus("current")


class _TnOamPingCtlTestIndex_Type(SnmpAdminString):
    """Custom type tnOamPingCtlTestIndex based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TnOamPingCtlTestIndex_Type.__name__ = "SnmpAdminString"
_TnOamPingCtlTestIndex_Object = MibTableColumn
tnOamPingCtlTestIndex = _TnOamPingCtlTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 1),
    _TnOamPingCtlTestIndex_Type()
)
tnOamPingCtlTestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOamPingCtlTestIndex.setStatus("current")
_TnOamPingCtlRowStatus_Type = RowStatus
_TnOamPingCtlRowStatus_Object = MibTableColumn
tnOamPingCtlRowStatus = _TnOamPingCtlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 2),
    _TnOamPingCtlRowStatus_Type()
)
tnOamPingCtlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlRowStatus.setStatus("current")


class _TnOamPingCtlStorageType_Type(StorageType):
    """Custom type tnOamPingCtlStorageType based on StorageType"""
    defaultValue = 2


_TnOamPingCtlStorageType_Type.__name__ = "StorageType"
_TnOamPingCtlStorageType_Object = MibTableColumn
tnOamPingCtlStorageType = _TnOamPingCtlStorageType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 3),
    _TnOamPingCtlStorageType_Type()
)
tnOamPingCtlStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlStorageType.setStatus("current")


class _TnOamPingCtlDescr_Type(SnmpAdminString):
    """Custom type tnOamPingCtlDescr based on SnmpAdminString"""
    defaultHexValue = ""


_TnOamPingCtlDescr_Type.__name__ = "SnmpAdminString"
_TnOamPingCtlDescr_Object = MibTableColumn
tnOamPingCtlDescr = _TnOamPingCtlDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 4),
    _TnOamPingCtlDescr_Type()
)
tnOamPingCtlDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlDescr.setStatus("current")


class _TnOamPingCtlTestMode_Type(Integer32):
    """Custom type tnOamPingCtlTestMode based on Integer32"""
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
              24)
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
          ("mobGtpPing", 21),
          ("ethCfmTwoWaySlm", 22),
          ("ethCfmTwoWayLm", 23),
          ("ethCfmOneWayDelay", 24))
    )


_TnOamPingCtlTestMode_Type.__name__ = "Integer32"
_TnOamPingCtlTestMode_Object = MibTableColumn
tnOamPingCtlTestMode = _TnOamPingCtlTestMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 5),
    _TnOamPingCtlTestMode_Type()
)
tnOamPingCtlTestMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlTestMode.setStatus("current")


class _TnOamPingCtlAdminStatus_Type(Integer32):
    """Custom type tnOamPingCtlAdminStatus based on Integer32"""
    defaultValue = 2

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


_TnOamPingCtlAdminStatus_Type.__name__ = "Integer32"
_TnOamPingCtlAdminStatus_Object = MibTableColumn
tnOamPingCtlAdminStatus = _TnOamPingCtlAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 6),
    _TnOamPingCtlAdminStatus_Type()
)
tnOamPingCtlAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlAdminStatus.setStatus("current")


class _TnOamPingCtlOrigSdpId_Type(SdpId):
    """Custom type tnOamPingCtlOrigSdpId based on SdpId"""
    defaultValue = 0


_TnOamPingCtlOrigSdpId_Type.__name__ = "SdpId"
_TnOamPingCtlOrigSdpId_Object = MibTableColumn
tnOamPingCtlOrigSdpId = _TnOamPingCtlOrigSdpId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 7),
    _TnOamPingCtlOrigSdpId_Type()
)
tnOamPingCtlOrigSdpId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlOrigSdpId.setStatus("current")


class _TnOamPingCtlRespSdpId_Type(SdpId):
    """Custom type tnOamPingCtlRespSdpId based on SdpId"""
    defaultValue = 0


_TnOamPingCtlRespSdpId_Type.__name__ = "SdpId"
_TnOamPingCtlRespSdpId_Object = MibTableColumn
tnOamPingCtlRespSdpId = _TnOamPingCtlRespSdpId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 8),
    _TnOamPingCtlRespSdpId_Type()
)
tnOamPingCtlRespSdpId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlRespSdpId.setStatus("current")


class _TnOamPingCtlFcName_Type(TFCName):
    """Custom type tnOamPingCtlFcName based on TFCName"""
    defaultValue = OctetString("be")


_TnOamPingCtlFcName_Type.__name__ = "TFCName"
_TnOamPingCtlFcName_Object = MibTableColumn
tnOamPingCtlFcName = _TnOamPingCtlFcName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 9),
    _TnOamPingCtlFcName_Type()
)
tnOamPingCtlFcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlFcName.setStatus("current")


class _TnOamPingCtlProfile_Type(TProfile):
    """Custom type tnOamPingCtlProfile based on TProfile"""
    defaultValue = 2


_TnOamPingCtlProfile_Type.__name__ = "TProfile"
_TnOamPingCtlProfile_Object = MibTableColumn
tnOamPingCtlProfile = _TnOamPingCtlProfile_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 10),
    _TnOamPingCtlProfile_Type()
)
tnOamPingCtlProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlProfile.setStatus("current")


class _TnOamPingCtlMtuStartSize_Type(Unsigned32):
    """Custom type tnOamPingCtlMtuStartSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(40, 9198),
    )


_TnOamPingCtlMtuStartSize_Type.__name__ = "Unsigned32"
_TnOamPingCtlMtuStartSize_Object = MibTableColumn
tnOamPingCtlMtuStartSize = _TnOamPingCtlMtuStartSize_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 11),
    _TnOamPingCtlMtuStartSize_Type()
)
tnOamPingCtlMtuStartSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlMtuStartSize.setStatus("current")
if mibBuilder.loadTexts:
    tnOamPingCtlMtuStartSize.setUnits("Octets")


class _TnOamPingCtlMtuEndSize_Type(Unsigned32):
    """Custom type tnOamPingCtlMtuEndSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(40, 9198),
    )


_TnOamPingCtlMtuEndSize_Type.__name__ = "Unsigned32"
_TnOamPingCtlMtuEndSize_Object = MibTableColumn
tnOamPingCtlMtuEndSize = _TnOamPingCtlMtuEndSize_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 12),
    _TnOamPingCtlMtuEndSize_Type()
)
tnOamPingCtlMtuEndSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlMtuEndSize.setStatus("current")
if mibBuilder.loadTexts:
    tnOamPingCtlMtuEndSize.setUnits("Octets")


class _TnOamPingCtlMtuStepSize_Type(Unsigned32):
    """Custom type tnOamPingCtlMtuStepSize based on Unsigned32"""
    defaultValue = 32

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_TnOamPingCtlMtuStepSize_Type.__name__ = "Unsigned32"
_TnOamPingCtlMtuStepSize_Object = MibTableColumn
tnOamPingCtlMtuStepSize = _TnOamPingCtlMtuStepSize_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 13),
    _TnOamPingCtlMtuStepSize_Type()
)
tnOamPingCtlMtuStepSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlMtuStepSize.setStatus("current")
if mibBuilder.loadTexts:
    tnOamPingCtlMtuStepSize.setUnits("Octets")


class _TnOamPingCtlTargetIpAddress_Type(IpAddress):
    """Custom type tnOamPingCtlTargetIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_TnOamPingCtlTargetIpAddress_Type.__name__ = "IpAddress"
_TnOamPingCtlTargetIpAddress_Object = MibTableColumn
tnOamPingCtlTargetIpAddress = _TnOamPingCtlTargetIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 14),
    _TnOamPingCtlTargetIpAddress_Type()
)
tnOamPingCtlTargetIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlTargetIpAddress.setStatus("obsolete")


class _TnOamPingCtlServiceId_Type(TmnxServId):
    """Custom type tnOamPingCtlServiceId based on TmnxServId"""
    defaultValue = 0

    subtypeSpec = TmnxServId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TnOamPingCtlServiceId_Type.__name__ = "TmnxServId"
_TnOamPingCtlServiceId_Object = MibTableColumn
tnOamPingCtlServiceId = _TnOamPingCtlServiceId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 15),
    _TnOamPingCtlServiceId_Type()
)
tnOamPingCtlServiceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlServiceId.setStatus("current")


class _TnOamPingCtlLocalSdp_Type(TruthValue):
    """Custom type tnOamPingCtlLocalSdp based on TruthValue"""
    defaultValue = 2


_TnOamPingCtlLocalSdp_Type.__name__ = "TruthValue"
_TnOamPingCtlLocalSdp_Object = MibTableColumn
tnOamPingCtlLocalSdp = _TnOamPingCtlLocalSdp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 16),
    _TnOamPingCtlLocalSdp_Type()
)
tnOamPingCtlLocalSdp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlLocalSdp.setStatus("current")


class _TnOamPingCtlRemoteSdp_Type(TruthValue):
    """Custom type tnOamPingCtlRemoteSdp based on TruthValue"""
    defaultValue = 2


_TnOamPingCtlRemoteSdp_Type.__name__ = "TruthValue"
_TnOamPingCtlRemoteSdp_Object = MibTableColumn
tnOamPingCtlRemoteSdp = _TnOamPingCtlRemoteSdp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 17),
    _TnOamPingCtlRemoteSdp_Type()
)
tnOamPingCtlRemoteSdp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlRemoteSdp.setStatus("current")


class _TnOamPingCtlSize_Type(Unsigned32):
    """Custom type tnOamPingCtlSize based on Unsigned32"""
    defaultValue = 72

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16384),
    )


_TnOamPingCtlSize_Type.__name__ = "Unsigned32"
_TnOamPingCtlSize_Object = MibTableColumn
tnOamPingCtlSize = _TnOamPingCtlSize_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 18),
    _TnOamPingCtlSize_Type()
)
tnOamPingCtlSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlSize.setStatus("current")
if mibBuilder.loadTexts:
    tnOamPingCtlSize.setUnits("octets")


class _TnOamPingCtlTimeOut_Type(Unsigned32):
    """Custom type tnOamPingCtlTimeOut based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120000),
    )


_TnOamPingCtlTimeOut_Type.__name__ = "Unsigned32"
_TnOamPingCtlTimeOut_Object = MibTableColumn
tnOamPingCtlTimeOut = _TnOamPingCtlTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 19),
    _TnOamPingCtlTimeOut_Type()
)
tnOamPingCtlTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    tnOamPingCtlTimeOut.setUnits("milliseconds")


class _TnOamPingCtlProbeCount_Type(Unsigned32):
    """Custom type tnOamPingCtlProbeCount based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_TnOamPingCtlProbeCount_Type.__name__ = "Unsigned32"
_TnOamPingCtlProbeCount_Object = MibTableColumn
tnOamPingCtlProbeCount = _TnOamPingCtlProbeCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 20),
    _TnOamPingCtlProbeCount_Type()
)
tnOamPingCtlProbeCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlProbeCount.setStatus("current")
if mibBuilder.loadTexts:
    tnOamPingCtlProbeCount.setUnits("probes")


class _TnOamPingCtlInterval_Type(Unsigned32):
    """Custom type tnOamPingCtlInterval based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 90000),
    )


_TnOamPingCtlInterval_Type.__name__ = "Unsigned32"
_TnOamPingCtlInterval_Object = MibTableColumn
tnOamPingCtlInterval = _TnOamPingCtlInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 21),
    _TnOamPingCtlInterval_Type()
)
tnOamPingCtlInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlInterval.setStatus("current")
if mibBuilder.loadTexts:
    tnOamPingCtlInterval.setUnits("milliseconds")


class _TnOamPingCtlMaxRows_Type(Unsigned32):
    """Custom type tnOamPingCtlMaxRows based on Unsigned32"""
    defaultValue = 300


_TnOamPingCtlMaxRows_Type.__name__ = "Unsigned32"
_TnOamPingCtlMaxRows_Object = MibTableColumn
tnOamPingCtlMaxRows = _TnOamPingCtlMaxRows_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 22),
    _TnOamPingCtlMaxRows_Type()
)
tnOamPingCtlMaxRows.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlMaxRows.setStatus("obsolete")
if mibBuilder.loadTexts:
    tnOamPingCtlMaxRows.setUnits("rows")


class _TnOamPingCtlTrapGeneration_Type(Bits):
    """Custom type tnOamPingCtlTrapGeneration based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("probeFailure", 0),
          ("testFailure", 1),
          ("testCompletion", 2))
    )

_TnOamPingCtlTrapGeneration_Type.__name__ = "Bits"
_TnOamPingCtlTrapGeneration_Object = MibTableColumn
tnOamPingCtlTrapGeneration = _TnOamPingCtlTrapGeneration_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 23),
    _TnOamPingCtlTrapGeneration_Type()
)
tnOamPingCtlTrapGeneration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlTrapGeneration.setStatus("current")


class _TnOamPingCtlTrapProbeFailureFilter_Type(Unsigned32):
    """Custom type tnOamPingCtlTrapProbeFailureFilter based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_TnOamPingCtlTrapProbeFailureFilter_Type.__name__ = "Unsigned32"
_TnOamPingCtlTrapProbeFailureFilter_Object = MibTableColumn
tnOamPingCtlTrapProbeFailureFilter = _TnOamPingCtlTrapProbeFailureFilter_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 24),
    _TnOamPingCtlTrapProbeFailureFilter_Type()
)
tnOamPingCtlTrapProbeFailureFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlTrapProbeFailureFilter.setStatus("current")


class _TnOamPingCtlTrapTestFailureFilter_Type(Unsigned32):
    """Custom type tnOamPingCtlTrapTestFailureFilter based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_TnOamPingCtlTrapTestFailureFilter_Type.__name__ = "Unsigned32"
_TnOamPingCtlTrapTestFailureFilter_Object = MibTableColumn
tnOamPingCtlTrapTestFailureFilter = _TnOamPingCtlTrapTestFailureFilter_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 25),
    _TnOamPingCtlTrapTestFailureFilter_Type()
)
tnOamPingCtlTrapTestFailureFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlTrapTestFailureFilter.setStatus("current")


class _TnOamPingCtlSAA_Type(TruthValue):
    """Custom type tnOamPingCtlSAA based on TruthValue"""
    defaultValue = 2


_TnOamPingCtlSAA_Type.__name__ = "TruthValue"
_TnOamPingCtlSAA_Object = MibTableColumn
tnOamPingCtlSAA = _TnOamPingCtlSAA_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 26),
    _TnOamPingCtlSAA_Type()
)
tnOamPingCtlSAA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlSAA.setStatus("current")
_TnOamPingCtlRuns_Type = Counter32
_TnOamPingCtlRuns_Object = MibTableColumn
tnOamPingCtlRuns = _TnOamPingCtlRuns_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 27),
    _TnOamPingCtlRuns_Type()
)
tnOamPingCtlRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingCtlRuns.setStatus("current")
_TnOamPingCtlFailures_Type = Counter32
_TnOamPingCtlFailures_Object = MibTableColumn
tnOamPingCtlFailures = _TnOamPingCtlFailures_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 28),
    _TnOamPingCtlFailures_Type()
)
tnOamPingCtlFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingCtlFailures.setStatus("current")
_TnOamPingCtlLastRunResult_Type = TmnxOamTestResult
_TnOamPingCtlLastRunResult_Object = MibTableColumn
tnOamPingCtlLastRunResult = _TnOamPingCtlLastRunResult_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 29),
    _TnOamPingCtlLastRunResult_Type()
)
tnOamPingCtlLastRunResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingCtlLastRunResult.setStatus("current")
_TnOamPingCtlLastChanged_Type = TimeStamp
_TnOamPingCtlLastChanged_Object = MibTableColumn
tnOamPingCtlLastChanged = _TnOamPingCtlLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 30),
    _TnOamPingCtlLastChanged_Type()
)
tnOamPingCtlLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingCtlLastChanged.setStatus("current")


class _TnOamPingCtlVRtrID_Type(TmnxVRtrID):
    """Custom type tnOamPingCtlVRtrID based on TmnxVRtrID"""
    defaultValue = 1


_TnOamPingCtlVRtrID_Type.__name__ = "TmnxVRtrID"
_TnOamPingCtlVRtrID_Object = MibTableColumn
tnOamPingCtlVRtrID = _TnOamPingCtlVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 31),
    _TnOamPingCtlVRtrID_Type()
)
tnOamPingCtlVRtrID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlVRtrID.setStatus("current")


class _TnOamPingCtlTgtAddrType_Type(InetAddressType):
    """Custom type tnOamPingCtlTgtAddrType based on InetAddressType"""
    defaultValue = 0


_TnOamPingCtlTgtAddrType_Type.__name__ = "InetAddressType"
_TnOamPingCtlTgtAddrType_Object = MibTableColumn
tnOamPingCtlTgtAddrType = _TnOamPingCtlTgtAddrType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 32),
    _TnOamPingCtlTgtAddrType_Type()
)
tnOamPingCtlTgtAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlTgtAddrType.setStatus("current")


class _TnOamPingCtlTgtAddress_Type(InetAddress):
    """Custom type tnOamPingCtlTgtAddress based on InetAddress"""
    defaultHexValue = ""


_TnOamPingCtlTgtAddress_Type.__name__ = "InetAddress"
_TnOamPingCtlTgtAddress_Object = MibTableColumn
tnOamPingCtlTgtAddress = _TnOamPingCtlTgtAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 33),
    _TnOamPingCtlTgtAddress_Type()
)
tnOamPingCtlTgtAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlTgtAddress.setStatus("current")


class _TnOamPingCtlSrcAddrType_Type(InetAddressType):
    """Custom type tnOamPingCtlSrcAddrType based on InetAddressType"""
    defaultValue = 0


_TnOamPingCtlSrcAddrType_Type.__name__ = "InetAddressType"
_TnOamPingCtlSrcAddrType_Object = MibTableColumn
tnOamPingCtlSrcAddrType = _TnOamPingCtlSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 34),
    _TnOamPingCtlSrcAddrType_Type()
)
tnOamPingCtlSrcAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlSrcAddrType.setStatus("current")


class _TnOamPingCtlSrcAddress_Type(InetAddress):
    """Custom type tnOamPingCtlSrcAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TnOamPingCtlSrcAddress_Type.__name__ = "InetAddress"
_TnOamPingCtlSrcAddress_Object = MibTableColumn
tnOamPingCtlSrcAddress = _TnOamPingCtlSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 35),
    _TnOamPingCtlSrcAddress_Type()
)
tnOamPingCtlSrcAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlSrcAddress.setStatus("current")


class _TnOamPingCtlDnsName_Type(OctetString):
    """Custom type tnOamPingCtlDnsName based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnOamPingCtlDnsName_Type.__name__ = "OctetString"
_TnOamPingCtlDnsName_Object = MibTableColumn
tnOamPingCtlDnsName = _TnOamPingCtlDnsName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 36),
    _TnOamPingCtlDnsName_Type()
)
tnOamPingCtlDnsName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlDnsName.setStatus("current")


class _TnOamPingCtlDNSRecord_Type(Integer32):
    """Custom type tnOamPingCtlDNSRecord based on Integer32"""
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


_TnOamPingCtlDNSRecord_Type.__name__ = "Integer32"
_TnOamPingCtlDNSRecord_Object = MibTableColumn
tnOamPingCtlDNSRecord = _TnOamPingCtlDNSRecord_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 37),
    _TnOamPingCtlDNSRecord_Type()
)
tnOamPingCtlDNSRecord.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlDNSRecord.setStatus("current")


class _TnOamPingCtlIntervalUnits_Type(Integer32):
    """Custom type tnOamPingCtlIntervalUnits based on Integer32"""
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
        *(("seconds", 1),
          ("centiseconds", 2),
          ("decimilliseconds", 3))
    )


_TnOamPingCtlIntervalUnits_Type.__name__ = "Integer32"
_TnOamPingCtlIntervalUnits_Object = MibTableColumn
tnOamPingCtlIntervalUnits = _TnOamPingCtlIntervalUnits_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 4, 1, 38),
    _TnOamPingCtlIntervalUnits_Type()
)
tnOamPingCtlIntervalUnits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamPingCtlIntervalUnits.setStatus("current")
_TnOamPingResultsTable_Object = MibTable
tnOamPingResultsTable = _TnOamPingResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 6)
)
if mibBuilder.loadTexts:
    tnOamPingResultsTable.setStatus("current")
_TnOamPingResultsEntry_Object = MibTableRow
tnOamPingResultsEntry = _TnOamPingResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 6, 1)
)
tnOamPingResultsEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-OAM-TEST-MIB", "tnOamPingCtlTestIndex"),
    (0, "TN-OAM-TEST-MIB", "tnOamPingResultsTestRunIndex"),
)
if mibBuilder.loadTexts:
    tnOamPingResultsEntry.setStatus("current")


class _TnOamPingResultsOperStatus_Type(Integer32):
    """Custom type tnOamPingResultsOperStatus based on Integer32"""
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


_TnOamPingResultsOperStatus_Type.__name__ = "Integer32"
_TnOamPingResultsOperStatus_Object = MibTableColumn
tnOamPingResultsOperStatus = _TnOamPingResultsOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 6, 1, 1),
    _TnOamPingResultsOperStatus_Type()
)
tnOamPingResultsOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingResultsOperStatus.setStatus("current")
_TnOamPingResultsMinRtt_Type = Unsigned32
_TnOamPingResultsMinRtt_Object = MibTableColumn
tnOamPingResultsMinRtt = _TnOamPingResultsMinRtt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 6, 1, 4),
    _TnOamPingResultsMinRtt_Type()
)
tnOamPingResultsMinRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingResultsMinRtt.setStatus("current")
if mibBuilder.loadTexts:
    tnOamPingResultsMinRtt.setUnits("microseconds")
_TnOamPingResultsMaxRtt_Type = Unsigned32
_TnOamPingResultsMaxRtt_Object = MibTableColumn
tnOamPingResultsMaxRtt = _TnOamPingResultsMaxRtt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 6, 1, 5),
    _TnOamPingResultsMaxRtt_Type()
)
tnOamPingResultsMaxRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingResultsMaxRtt.setStatus("current")
if mibBuilder.loadTexts:
    tnOamPingResultsMaxRtt.setUnits("microseconds")
_TnOamPingResultsAverageRtt_Type = Unsigned32
_TnOamPingResultsAverageRtt_Object = MibTableColumn
tnOamPingResultsAverageRtt = _TnOamPingResultsAverageRtt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 6, 1, 6),
    _TnOamPingResultsAverageRtt_Type()
)
tnOamPingResultsAverageRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingResultsAverageRtt.setStatus("current")
if mibBuilder.loadTexts:
    tnOamPingResultsAverageRtt.setUnits("microseconds")
_TnOamPingResultsRttSumOfSquares_Type = Unsigned32
_TnOamPingResultsRttSumOfSquares_Object = MibTableColumn
tnOamPingResultsRttSumOfSquares = _TnOamPingResultsRttSumOfSquares_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 6, 1, 7),
    _TnOamPingResultsRttSumOfSquares_Type()
)
tnOamPingResultsRttSumOfSquares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingResultsRttSumOfSquares.setStatus("current")
if mibBuilder.loadTexts:
    tnOamPingResultsRttSumOfSquares.setUnits("microseconds squared")
_TnOamPingResultsMtuResponseSize_Type = Unsigned32
_TnOamPingResultsMtuResponseSize_Object = MibTableColumn
tnOamPingResultsMtuResponseSize = _TnOamPingResultsMtuResponseSize_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 6, 1, 8),
    _TnOamPingResultsMtuResponseSize_Type()
)
tnOamPingResultsMtuResponseSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingResultsMtuResponseSize.setStatus("current")
if mibBuilder.loadTexts:
    tnOamPingResultsMtuResponseSize.setUnits("Octets")


class _TnOamPingResultsSvcPing_Type(Integer32):
    """Custom type tnOamPingResultsSvcPing based on Integer32"""
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


_TnOamPingResultsSvcPing_Type.__name__ = "Integer32"
_TnOamPingResultsSvcPing_Object = MibTableColumn
tnOamPingResultsSvcPing = _TnOamPingResultsSvcPing_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 6, 1, 9),
    _TnOamPingResultsSvcPing_Type()
)
tnOamPingResultsSvcPing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingResultsSvcPing.setStatus("current")
_TnOamPingResultsProbeResponses_Type = Unsigned32
_TnOamPingResultsProbeResponses_Object = MibTableColumn
tnOamPingResultsProbeResponses = _TnOamPingResultsProbeResponses_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 6, 1, 10),
    _TnOamPingResultsProbeResponses_Type()
)
tnOamPingResultsProbeResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingResultsProbeResponses.setStatus("current")
if mibBuilder.loadTexts:
    tnOamPingResultsProbeResponses.setUnits("responses")
_TnOamPingResultsSentProbes_Type = Unsigned32
_TnOamPingResultsSentProbes_Object = MibTableColumn
tnOamPingResultsSentProbes = _TnOamPingResultsSentProbes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 6, 1, 11),
    _TnOamPingResultsSentProbes_Type()
)
tnOamPingResultsSentProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingResultsSentProbes.setStatus("current")
if mibBuilder.loadTexts:
    tnOamPingResultsSentProbes.setUnits("probes")
_TnOamPingResultsLastGoodProbe_Type = DateAndTime
_TnOamPingResultsLastGoodProbe_Object = MibTableColumn
tnOamPingResultsLastGoodProbe = _TnOamPingResultsLastGoodProbe_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 6, 1, 12),
    _TnOamPingResultsLastGoodProbe_Type()
)
tnOamPingResultsLastGoodProbe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingResultsLastGoodProbe.setStatus("current")


class _TnOamPingResultsLastRespHeader_Type(OctetString):
    """Custom type tnOamPingResultsLastRespHeader based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(100, 100),
    )
    fixed_length = 100


_TnOamPingResultsLastRespHeader_Type.__name__ = "OctetString"
_TnOamPingResultsLastRespHeader_Object = MibTableColumn
tnOamPingResultsLastRespHeader = _TnOamPingResultsLastRespHeader_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 6, 1, 13),
    _TnOamPingResultsLastRespHeader_Type()
)
tnOamPingResultsLastRespHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingResultsLastRespHeader.setStatus("obsolete")
_TnOamPingResultsMinTt_Type = Integer32
_TnOamPingResultsMinTt_Object = MibTableColumn
tnOamPingResultsMinTt = _TnOamPingResultsMinTt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 6, 1, 14),
    _TnOamPingResultsMinTt_Type()
)
tnOamPingResultsMinTt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingResultsMinTt.setStatus("current")
if mibBuilder.loadTexts:
    tnOamPingResultsMinTt.setUnits("microseconds")
_TnOamPingResultsMaxTt_Type = Integer32
_TnOamPingResultsMaxTt_Object = MibTableColumn
tnOamPingResultsMaxTt = _TnOamPingResultsMaxTt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 6, 1, 15),
    _TnOamPingResultsMaxTt_Type()
)
tnOamPingResultsMaxTt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingResultsMaxTt.setStatus("current")
if mibBuilder.loadTexts:
    tnOamPingResultsMaxTt.setUnits("microseconds")
_TnOamPingResultsAverageTt_Type = Integer32
_TnOamPingResultsAverageTt_Object = MibTableColumn
tnOamPingResultsAverageTt = _TnOamPingResultsAverageTt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 6, 1, 16),
    _TnOamPingResultsAverageTt_Type()
)
tnOamPingResultsAverageTt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingResultsAverageTt.setStatus("current")
if mibBuilder.loadTexts:
    tnOamPingResultsAverageTt.setUnits("microseconds")
_TnOamPingResultsTtSumOfSquares_Type = Unsigned32
_TnOamPingResultsTtSumOfSquares_Object = MibTableColumn
tnOamPingResultsTtSumOfSquares = _TnOamPingResultsTtSumOfSquares_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 6, 1, 17),
    _TnOamPingResultsTtSumOfSquares_Type()
)
tnOamPingResultsTtSumOfSquares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingResultsTtSumOfSquares.setStatus("current")
if mibBuilder.loadTexts:
    tnOamPingResultsTtSumOfSquares.setUnits("microseconds squared")
_TnOamPingResultsMinInTt_Type = Integer32
_TnOamPingResultsMinInTt_Object = MibTableColumn
tnOamPingResultsMinInTt = _TnOamPingResultsMinInTt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 6, 1, 18),
    _TnOamPingResultsMinInTt_Type()
)
tnOamPingResultsMinInTt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingResultsMinInTt.setStatus("current")
if mibBuilder.loadTexts:
    tnOamPingResultsMinInTt.setUnits("microseconds")
_TnOamPingResultsMaxInTt_Type = Integer32
_TnOamPingResultsMaxInTt_Object = MibTableColumn
tnOamPingResultsMaxInTt = _TnOamPingResultsMaxInTt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 6, 1, 19),
    _TnOamPingResultsMaxInTt_Type()
)
tnOamPingResultsMaxInTt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingResultsMaxInTt.setStatus("current")
if mibBuilder.loadTexts:
    tnOamPingResultsMaxInTt.setUnits("microseconds")
_TnOamPingResultsAverageInTt_Type = Integer32
_TnOamPingResultsAverageInTt_Object = MibTableColumn
tnOamPingResultsAverageInTt = _TnOamPingResultsAverageInTt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 6, 1, 20),
    _TnOamPingResultsAverageInTt_Type()
)
tnOamPingResultsAverageInTt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingResultsAverageInTt.setStatus("current")
if mibBuilder.loadTexts:
    tnOamPingResultsAverageInTt.setUnits("microseconds")
_TnOamPingResultsInTtSumOfSqrs_Type = Unsigned32
_TnOamPingResultsInTtSumOfSqrs_Object = MibTableColumn
tnOamPingResultsInTtSumOfSqrs = _TnOamPingResultsInTtSumOfSqrs_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 6, 1, 21),
    _TnOamPingResultsInTtSumOfSqrs_Type()
)
tnOamPingResultsInTtSumOfSqrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingResultsInTtSumOfSqrs.setStatus("current")
if mibBuilder.loadTexts:
    tnOamPingResultsInTtSumOfSqrs.setUnits("microseconds squared")
_TnOamPingResultsOutJitter_Type = Integer32
_TnOamPingResultsOutJitter_Object = MibTableColumn
tnOamPingResultsOutJitter = _TnOamPingResultsOutJitter_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 6, 1, 22),
    _TnOamPingResultsOutJitter_Type()
)
tnOamPingResultsOutJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingResultsOutJitter.setStatus("current")
if mibBuilder.loadTexts:
    tnOamPingResultsOutJitter.setUnits("microseconds")
_TnOamPingResultsInJitter_Type = Integer32
_TnOamPingResultsInJitter_Object = MibTableColumn
tnOamPingResultsInJitter = _TnOamPingResultsInJitter_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 6, 1, 23),
    _TnOamPingResultsInJitter_Type()
)
tnOamPingResultsInJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingResultsInJitter.setStatus("current")
if mibBuilder.loadTexts:
    tnOamPingResultsInJitter.setUnits("microseconds")
_TnOamPingResultsRtJitter_Type = Integer32
_TnOamPingResultsRtJitter_Object = MibTableColumn
tnOamPingResultsRtJitter = _TnOamPingResultsRtJitter_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 6, 1, 24),
    _TnOamPingResultsRtJitter_Type()
)
tnOamPingResultsRtJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingResultsRtJitter.setStatus("current")
if mibBuilder.loadTexts:
    tnOamPingResultsRtJitter.setUnits("microseconds")
_TnOamPingResultsProbeTimeouts_Type = Unsigned32
_TnOamPingResultsProbeTimeouts_Object = MibTableColumn
tnOamPingResultsProbeTimeouts = _TnOamPingResultsProbeTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 6, 1, 25),
    _TnOamPingResultsProbeTimeouts_Type()
)
tnOamPingResultsProbeTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingResultsProbeTimeouts.setStatus("current")
_TnOamPingResultsProbeFailures_Type = Unsigned32
_TnOamPingResultsProbeFailures_Object = MibTableColumn
tnOamPingResultsProbeFailures = _TnOamPingResultsProbeFailures_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 6, 1, 26),
    _TnOamPingResultsProbeFailures_Type()
)
tnOamPingResultsProbeFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingResultsProbeFailures.setStatus("current")


class _TnOamPingResultsTestRunIndex_Type(Unsigned32):
    """Custom type tnOamPingResultsTestRunIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TnOamPingResultsTestRunIndex_Type.__name__ = "Unsigned32"
_TnOamPingResultsTestRunIndex_Object = MibTableColumn
tnOamPingResultsTestRunIndex = _TnOamPingResultsTestRunIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 6, 1, 27),
    _TnOamPingResultsTestRunIndex_Type()
)
tnOamPingResultsTestRunIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOamPingResultsTestRunIndex.setStatus("current")
_TnOamPingResultsRttOFSumSquares_Type = Counter32
_TnOamPingResultsRttOFSumSquares_Object = MibTableColumn
tnOamPingResultsRttOFSumSquares = _TnOamPingResultsRttOFSumSquares_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 6, 1, 28),
    _TnOamPingResultsRttOFSumSquares_Type()
)
tnOamPingResultsRttOFSumSquares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingResultsRttOFSumSquares.setStatus("current")
_TnOamPingResultsRttHCSumSquares_Type = Counter64
_TnOamPingResultsRttHCSumSquares_Object = MibTableColumn
tnOamPingResultsRttHCSumSquares = _TnOamPingResultsRttHCSumSquares_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 6, 1, 29),
    _TnOamPingResultsRttHCSumSquares_Type()
)
tnOamPingResultsRttHCSumSquares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingResultsRttHCSumSquares.setStatus("current")
if mibBuilder.loadTexts:
    tnOamPingResultsRttHCSumSquares.setUnits("microseconds squared")
_TnOamPingResultsTtOFSumSquares_Type = Counter32
_TnOamPingResultsTtOFSumSquares_Object = MibTableColumn
tnOamPingResultsTtOFSumSquares = _TnOamPingResultsTtOFSumSquares_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 6, 1, 30),
    _TnOamPingResultsTtOFSumSquares_Type()
)
tnOamPingResultsTtOFSumSquares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingResultsTtOFSumSquares.setStatus("current")
_TnOamPingResultsTtHCSumSquares_Type = Counter64
_TnOamPingResultsTtHCSumSquares_Object = MibTableColumn
tnOamPingResultsTtHCSumSquares = _TnOamPingResultsTtHCSumSquares_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 6, 1, 31),
    _TnOamPingResultsTtHCSumSquares_Type()
)
tnOamPingResultsTtHCSumSquares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingResultsTtHCSumSquares.setStatus("current")
if mibBuilder.loadTexts:
    tnOamPingResultsTtHCSumSquares.setUnits("microseconds squared")
_TnOamPingResultsInTtOFSumSqrs_Type = Counter32
_TnOamPingResultsInTtOFSumSqrs_Object = MibTableColumn
tnOamPingResultsInTtOFSumSqrs = _TnOamPingResultsInTtOFSumSqrs_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 6, 1, 32),
    _TnOamPingResultsInTtOFSumSqrs_Type()
)
tnOamPingResultsInTtOFSumSqrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingResultsInTtOFSumSqrs.setStatus("current")
_TnOamPingResultsInTtHCSumSqrs_Type = Counter64
_TnOamPingResultsInTtHCSumSqrs_Object = MibTableColumn
tnOamPingResultsInTtHCSumSqrs = _TnOamPingResultsInTtHCSumSqrs_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 6, 1, 33),
    _TnOamPingResultsInTtHCSumSqrs_Type()
)
tnOamPingResultsInTtHCSumSqrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingResultsInTtHCSumSqrs.setStatus("current")
if mibBuilder.loadTexts:
    tnOamPingResultsInTtHCSumSqrs.setUnits("microseconds squared")
_TnOamPingResultsTestRunResult_Type = TmnxOamTestResult
_TnOamPingResultsTestRunResult_Object = MibTableColumn
tnOamPingResultsTestRunResult = _TnOamPingResultsTestRunResult_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 6, 1, 34),
    _TnOamPingResultsTestRunResult_Type()
)
tnOamPingResultsTestRunResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingResultsTestRunResult.setStatus("current")
_TnOamPingHistoryTable_Object = MibTable
tnOamPingHistoryTable = _TnOamPingHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 8)
)
if mibBuilder.loadTexts:
    tnOamPingHistoryTable.setStatus("current")
_TnOamPingHistoryEntry_Object = MibTableRow
tnOamPingHistoryEntry = _TnOamPingHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 8, 1)
)
tnOamPingHistoryEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-OAM-TEST-MIB", "tnOamPingCtlTestIndex"),
    (0, "TN-OAM-TEST-MIB", "tnOamPingResultsTestRunIndex"),
    (0, "TN-OAM-TEST-MIB", "tnOamPingHistoryIndex"),
)
if mibBuilder.loadTexts:
    tnOamPingHistoryEntry.setStatus("current")


class _TnOamPingHistoryIndex_Type(Unsigned32):
    """Custom type tnOamPingHistoryIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TnOamPingHistoryIndex_Type.__name__ = "Unsigned32"
_TnOamPingHistoryIndex_Object = MibTableColumn
tnOamPingHistoryIndex = _TnOamPingHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 8, 1, 1),
    _TnOamPingHistoryIndex_Type()
)
tnOamPingHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOamPingHistoryIndex.setStatus("current")
_TnOamPingHistoryResponse_Type = Unsigned32
_TnOamPingHistoryResponse_Object = MibTableColumn
tnOamPingHistoryResponse = _TnOamPingHistoryResponse_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 8, 1, 2),
    _TnOamPingHistoryResponse_Type()
)
tnOamPingHistoryResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingHistoryResponse.setStatus("current")
if mibBuilder.loadTexts:
    tnOamPingHistoryResponse.setUnits("microseconds")
_TnOamPingHistoryOneWayTime_Type = Integer32
_TnOamPingHistoryOneWayTime_Object = MibTableColumn
tnOamPingHistoryOneWayTime = _TnOamPingHistoryOneWayTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 8, 1, 3),
    _TnOamPingHistoryOneWayTime_Type()
)
tnOamPingHistoryOneWayTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingHistoryOneWayTime.setStatus("current")
if mibBuilder.loadTexts:
    tnOamPingHistoryOneWayTime.setUnits("microseconds")
_TnOamPingHistorySize_Type = Unsigned32
_TnOamPingHistorySize_Object = MibTableColumn
tnOamPingHistorySize = _TnOamPingHistorySize_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 8, 1, 4),
    _TnOamPingHistorySize_Type()
)
tnOamPingHistorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingHistorySize.setStatus("current")
if mibBuilder.loadTexts:
    tnOamPingHistorySize.setUnits("octets")
_TnOamPingHistoryStatus_Type = TmnxOamResponseStatus
_TnOamPingHistoryStatus_Object = MibTableColumn
tnOamPingHistoryStatus = _TnOamPingHistoryStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 8, 1, 5),
    _TnOamPingHistoryStatus_Type()
)
tnOamPingHistoryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingHistoryStatus.setStatus("current")
_TnOamPingHistoryTime_Type = DateAndTime
_TnOamPingHistoryTime_Object = MibTableColumn
tnOamPingHistoryTime = _TnOamPingHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 8, 1, 6),
    _TnOamPingHistoryTime_Type()
)
tnOamPingHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingHistoryTime.setStatus("current")
_TnOamPingHistoryReturnCode_Type = Integer32
_TnOamPingHistoryReturnCode_Object = MibTableColumn
tnOamPingHistoryReturnCode = _TnOamPingHistoryReturnCode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 8, 1, 7),
    _TnOamPingHistoryReturnCode_Type()
)
tnOamPingHistoryReturnCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingHistoryReturnCode.setStatus("current")
_TnOamPingHistorySrcIpAddress_Type = IpAddress
_TnOamPingHistorySrcIpAddress_Object = MibTableColumn
tnOamPingHistorySrcIpAddress = _TnOamPingHistorySrcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 8, 1, 8),
    _TnOamPingHistorySrcIpAddress_Type()
)
tnOamPingHistorySrcIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingHistorySrcIpAddress.setStatus("obsolete")
_TnOamPingHistAddressType_Type = TmnxOamAddressType
_TnOamPingHistAddressType_Object = MibTableColumn
tnOamPingHistAddressType = _TnOamPingHistAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 8, 1, 9),
    _TnOamPingHistAddressType_Type()
)
tnOamPingHistAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingHistAddressType.setStatus("current")
_TnOamPingHistSapId_Type = TmnxStrSapId
_TnOamPingHistSapId_Object = MibTableColumn
tnOamPingHistSapId = _TnOamPingHistSapId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 8, 1, 10),
    _TnOamPingHistSapId_Type()
)
tnOamPingHistSapId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingHistSapId.setStatus("current")
_TnOamPingHistoryVersion_Type = Unsigned32
_TnOamPingHistoryVersion_Object = MibTableColumn
tnOamPingHistoryVersion = _TnOamPingHistoryVersion_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 8, 1, 12),
    _TnOamPingHistoryVersion_Type()
)
tnOamPingHistoryVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingHistoryVersion.setStatus("current")
_TnOamPingHistoryCpeMacAddr_Type = MacAddress
_TnOamPingHistoryCpeMacAddr_Object = MibTableColumn
tnOamPingHistoryCpeMacAddr = _TnOamPingHistoryCpeMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 8, 1, 13),
    _TnOamPingHistoryCpeMacAddr_Type()
)
tnOamPingHistoryCpeMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingHistoryCpeMacAddr.setStatus("current")
_TnOamPingHistoryRespSvcId_Type = TmnxServId
_TnOamPingHistoryRespSvcId_Object = MibTableColumn
tnOamPingHistoryRespSvcId = _TnOamPingHistoryRespSvcId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 8, 1, 14),
    _TnOamPingHistoryRespSvcId_Type()
)
tnOamPingHistoryRespSvcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingHistoryRespSvcId.setStatus("current")
_TnOamPingHistorySequence_Type = Unsigned32
_TnOamPingHistorySequence_Object = MibTableColumn
tnOamPingHistorySequence = _TnOamPingHistorySequence_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 8, 1, 15),
    _TnOamPingHistorySequence_Type()
)
tnOamPingHistorySequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingHistorySequence.setStatus("current")
_TnOamPingHistoryIfIndex_Type = InterfaceIndexOrZero
_TnOamPingHistoryIfIndex_Object = MibTableColumn
tnOamPingHistoryIfIndex = _TnOamPingHistoryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 8, 1, 16),
    _TnOamPingHistoryIfIndex_Type()
)
tnOamPingHistoryIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingHistoryIfIndex.setStatus("current")
_TnOamPingHistoryDataLen_Type = Unsigned32
_TnOamPingHistoryDataLen_Object = MibTableColumn
tnOamPingHistoryDataLen = _TnOamPingHistoryDataLen_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 8, 1, 17),
    _TnOamPingHistoryDataLen_Type()
)
tnOamPingHistoryDataLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingHistoryDataLen.setStatus("current")
_TnOamPingHistoryRespPlane_Type = TmnxOamTestResponsePlane
_TnOamPingHistoryRespPlane_Object = MibTableColumn
tnOamPingHistoryRespPlane = _TnOamPingHistoryRespPlane_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 8, 1, 18),
    _TnOamPingHistoryRespPlane_Type()
)
tnOamPingHistoryRespPlane.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingHistoryRespPlane.setStatus("current")


class _TnOamPingHistoryReqHdr_Type(OctetString):
    """Custom type tnOamPingHistoryReqHdr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 150),
    )


_TnOamPingHistoryReqHdr_Type.__name__ = "OctetString"
_TnOamPingHistoryReqHdr_Object = MibTableColumn
tnOamPingHistoryReqHdr = _TnOamPingHistoryReqHdr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 8, 1, 19),
    _TnOamPingHistoryReqHdr_Type()
)
tnOamPingHistoryReqHdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingHistoryReqHdr.setStatus("obsolete")


class _TnOamPingHistoryRespHdr_Type(OctetString):
    """Custom type tnOamPingHistoryRespHdr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 150),
    )


_TnOamPingHistoryRespHdr_Type.__name__ = "OctetString"
_TnOamPingHistoryRespHdr_Object = MibTableColumn
tnOamPingHistoryRespHdr = _TnOamPingHistoryRespHdr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 8, 1, 20),
    _TnOamPingHistoryRespHdr_Type()
)
tnOamPingHistoryRespHdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingHistoryRespHdr.setStatus("current")
_TnOamPingHistoryDnsAddrType_Type = InetAddressType
_TnOamPingHistoryDnsAddrType_Object = MibTableColumn
tnOamPingHistoryDnsAddrType = _TnOamPingHistoryDnsAddrType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 8, 1, 21),
    _TnOamPingHistoryDnsAddrType_Type()
)
tnOamPingHistoryDnsAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingHistoryDnsAddrType.setStatus("current")


class _TnOamPingHistoryDnsAddress_Type(InetAddress):
    """Custom type tnOamPingHistoryDnsAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TnOamPingHistoryDnsAddress_Type.__name__ = "InetAddress"
_TnOamPingHistoryDnsAddress_Object = MibTableColumn
tnOamPingHistoryDnsAddress = _TnOamPingHistoryDnsAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 8, 1, 22),
    _TnOamPingHistoryDnsAddress_Type()
)
tnOamPingHistoryDnsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingHistoryDnsAddress.setStatus("current")
_TnOamPingHistorySrcAddrType_Type = InetAddressType
_TnOamPingHistorySrcAddrType_Object = MibTableColumn
tnOamPingHistorySrcAddrType = _TnOamPingHistorySrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 8, 1, 23),
    _TnOamPingHistorySrcAddrType_Type()
)
tnOamPingHistorySrcAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingHistorySrcAddrType.setStatus("current")


class _TnOamPingHistorySrcAddress_Type(InetAddress):
    """Custom type tnOamPingHistorySrcAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TnOamPingHistorySrcAddress_Type.__name__ = "InetAddress"
_TnOamPingHistorySrcAddress_Object = MibTableColumn
tnOamPingHistorySrcAddress = _TnOamPingHistorySrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 8, 1, 24),
    _TnOamPingHistorySrcAddress_Type()
)
tnOamPingHistorySrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingHistorySrcAddress.setStatus("current")
_TnOamPingHistoryInOneWayTime_Type = Integer32
_TnOamPingHistoryInOneWayTime_Object = MibTableColumn
tnOamPingHistoryInOneWayTime = _TnOamPingHistoryInOneWayTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 8, 1, 25),
    _TnOamPingHistoryInOneWayTime_Type()
)
tnOamPingHistoryInOneWayTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingHistoryInOneWayTime.setStatus("current")
if mibBuilder.loadTexts:
    tnOamPingHistoryInOneWayTime.setUnits("microseconds")
_TnOamPingHistoryLspName_Type = TLNamedItemOrEmpty
_TnOamPingHistoryLspName_Object = MibTableColumn
tnOamPingHistoryLspName = _TnOamPingHistoryLspName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 8, 1, 26),
    _TnOamPingHistoryLspName_Type()
)
tnOamPingHistoryLspName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingHistoryLspName.setStatus("current")
_TnOamPingHistNextHopAddrType_Type = InetAddressType
_TnOamPingHistNextHopAddrType_Object = MibTableColumn
tnOamPingHistNextHopAddrType = _TnOamPingHistNextHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 8, 1, 27),
    _TnOamPingHistNextHopAddrType_Type()
)
tnOamPingHistNextHopAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingHistNextHopAddrType.setStatus("current")


class _TnOamPingHistNextHopAddress_Type(InetAddress):
    """Custom type tnOamPingHistNextHopAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TnOamPingHistNextHopAddress_Type.__name__ = "InetAddress"
_TnOamPingHistNextHopAddress_Object = MibTableColumn
tnOamPingHistNextHopAddress = _TnOamPingHistNextHopAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 8, 1, 28),
    _TnOamPingHistNextHopAddress_Type()
)
tnOamPingHistNextHopAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingHistNextHopAddress.setStatus("current")
_TnOamPingHistorySrcGlobalId_Type = TmnxMplsTpGlobalID
_TnOamPingHistorySrcGlobalId_Object = MibTableColumn
tnOamPingHistorySrcGlobalId = _TnOamPingHistorySrcGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 8, 1, 29),
    _TnOamPingHistorySrcGlobalId_Type()
)
tnOamPingHistorySrcGlobalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingHistorySrcGlobalId.setStatus("current")
_TnOamPingHistorySrcNodeId_Type = TmnxMplsTpNodeID
_TnOamPingHistorySrcNodeId_Object = MibTableColumn
tnOamPingHistorySrcNodeId = _TnOamPingHistorySrcNodeId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 8, 1, 30),
    _TnOamPingHistorySrcNodeId_Type()
)
tnOamPingHistorySrcNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingHistorySrcNodeId.setStatus("current")
_TnOamPingHistorySdpBindId_Type = TNamedItemOrEmpty
_TnOamPingHistorySdpBindId_Object = MibTableColumn
tnOamPingHistorySdpBindId = _TnOamPingHistorySdpBindId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 8, 1, 31),
    _TnOamPingHistorySdpBindId_Type()
)
tnOamPingHistorySdpBindId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingHistorySdpBindId.setStatus("current")
_TnOamPingHistoryRtrnSubcode_Type = Unsigned32
_TnOamPingHistoryRtrnSubcode_Object = MibTableColumn
tnOamPingHistoryRtrnSubcode = _TnOamPingHistoryRtrnSubcode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 8, 1, 32),
    _TnOamPingHistoryRtrnSubcode_Type()
)
tnOamPingHistoryRtrnSubcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamPingHistoryRtrnSubcode.setStatus("current")
_TnOamLspPingCtlTable_Object = MibTable
tnOamLspPingCtlTable = _TnOamLspPingCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 16)
)
if mibBuilder.loadTexts:
    tnOamLspPingCtlTable.setStatus("current")
_TnOamLspPingCtlEntry_Object = MibTableRow
tnOamLspPingCtlEntry = _TnOamLspPingCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 16, 1)
)
tnOamLspPingCtlEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-OAM-TEST-MIB", "tnOamPingCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tnOamLspPingCtlEntry.setStatus("current")


class _TnOamLspPingCtlVRtrID_Type(TmnxVRtrID):
    """Custom type tnOamLspPingCtlVRtrID based on TmnxVRtrID"""
    defaultValue = 1


_TnOamLspPingCtlVRtrID_Type.__name__ = "TmnxVRtrID"
_TnOamLspPingCtlVRtrID_Object = MibTableColumn
tnOamLspPingCtlVRtrID = _TnOamLspPingCtlVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 16, 1, 1),
    _TnOamLspPingCtlVRtrID_Type()
)
tnOamLspPingCtlVRtrID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamLspPingCtlVRtrID.setStatus("obsolete")


class _TnOamLspPingCtlLspName_Type(TNamedItemOrEmpty):
    """Custom type tnOamLspPingCtlLspName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TnOamLspPingCtlLspName_Type.__name__ = "TNamedItemOrEmpty"
_TnOamLspPingCtlLspName_Object = MibTableColumn
tnOamLspPingCtlLspName = _TnOamLspPingCtlLspName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 16, 1, 2),
    _TnOamLspPingCtlLspName_Type()
)
tnOamLspPingCtlLspName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamLspPingCtlLspName.setStatus("current")


class _TnOamLspPingCtlReturnLsp_Type(TNamedItemOrEmpty):
    """Custom type tnOamLspPingCtlReturnLsp based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TnOamLspPingCtlReturnLsp_Type.__name__ = "TNamedItemOrEmpty"
_TnOamLspPingCtlReturnLsp_Object = MibTableColumn
tnOamLspPingCtlReturnLsp = _TnOamLspPingCtlReturnLsp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 16, 1, 3),
    _TnOamLspPingCtlReturnLsp_Type()
)
tnOamLspPingCtlReturnLsp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamLspPingCtlReturnLsp.setStatus("obsolete")


class _TnOamLspPingCtlTtl_Type(Unsigned32):
    """Custom type tnOamLspPingCtlTtl based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TnOamLspPingCtlTtl_Type.__name__ = "Unsigned32"
_TnOamLspPingCtlTtl_Object = MibTableColumn
tnOamLspPingCtlTtl = _TnOamLspPingCtlTtl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 16, 1, 4),
    _TnOamLspPingCtlTtl_Type()
)
tnOamLspPingCtlTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamLspPingCtlTtl.setStatus("current")
if mibBuilder.loadTexts:
    tnOamLspPingCtlTtl.setUnits("time-to-live value")


class _TnOamLspPingCtlPathName_Type(TNamedItemOrEmpty):
    """Custom type tnOamLspPingCtlPathName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TnOamLspPingCtlPathName_Type.__name__ = "TNamedItemOrEmpty"
_TnOamLspPingCtlPathName_Object = MibTableColumn
tnOamLspPingCtlPathName = _TnOamLspPingCtlPathName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 16, 1, 5),
    _TnOamLspPingCtlPathName_Type()
)
tnOamLspPingCtlPathName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamLspPingCtlPathName.setStatus("current")


class _TnOamLspPingCtlLdpIpPrefix_Type(IpAddress):
    """Custom type tnOamLspPingCtlLdpIpPrefix based on IpAddress"""
    defaultHexValue = "00000000"


_TnOamLspPingCtlLdpIpPrefix_Type.__name__ = "IpAddress"
_TnOamLspPingCtlLdpIpPrefix_Object = MibTableColumn
tnOamLspPingCtlLdpIpPrefix = _TnOamLspPingCtlLdpIpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 16, 1, 6),
    _TnOamLspPingCtlLdpIpPrefix_Type()
)
tnOamLspPingCtlLdpIpPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamLspPingCtlLdpIpPrefix.setStatus("obsolete")


class _TnOamLspPingCtlLdpIpPrefixLen_Type(IpAddressPrefixLength):
    """Custom type tnOamLspPingCtlLdpIpPrefixLen based on IpAddressPrefixLength"""
    defaultValue = 32


_TnOamLspPingCtlLdpIpPrefixLen_Type.__name__ = "IpAddressPrefixLength"
_TnOamLspPingCtlLdpIpPrefixLen_Object = MibTableColumn
tnOamLspPingCtlLdpIpPrefixLen = _TnOamLspPingCtlLdpIpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 16, 1, 7),
    _TnOamLspPingCtlLdpIpPrefixLen_Type()
)
tnOamLspPingCtlLdpIpPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamLspPingCtlLdpIpPrefixLen.setStatus("obsolete")


class _TnOamLspPingCtlLdpPrefixType_Type(InetAddressType):
    """Custom type tnOamLspPingCtlLdpPrefixType based on InetAddressType"""
    defaultValue = 0


_TnOamLspPingCtlLdpPrefixType_Type.__name__ = "InetAddressType"
_TnOamLspPingCtlLdpPrefixType_Object = MibTableColumn
tnOamLspPingCtlLdpPrefixType = _TnOamLspPingCtlLdpPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 16, 1, 8),
    _TnOamLspPingCtlLdpPrefixType_Type()
)
tnOamLspPingCtlLdpPrefixType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamLspPingCtlLdpPrefixType.setStatus("current")


class _TnOamLspPingCtlLdpPrefix_Type(InetAddress):
    """Custom type tnOamLspPingCtlLdpPrefix based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TnOamLspPingCtlLdpPrefix_Type.__name__ = "InetAddress"
_TnOamLspPingCtlLdpPrefix_Object = MibTableColumn
tnOamLspPingCtlLdpPrefix = _TnOamLspPingCtlLdpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 16, 1, 9),
    _TnOamLspPingCtlLdpPrefix_Type()
)
tnOamLspPingCtlLdpPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamLspPingCtlLdpPrefix.setStatus("current")


class _TnOamLspPingCtlLdpPrefixLen_Type(InetAddressPrefixLength):
    """Custom type tnOamLspPingCtlLdpPrefixLen based on InetAddressPrefixLength"""
    defaultValue = 32


_TnOamLspPingCtlLdpPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_TnOamLspPingCtlLdpPrefixLen_Object = MibTableColumn
tnOamLspPingCtlLdpPrefixLen = _TnOamLspPingCtlLdpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 16, 1, 10),
    _TnOamLspPingCtlLdpPrefixLen_Type()
)
tnOamLspPingCtlLdpPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamLspPingCtlLdpPrefixLen.setStatus("current")


class _TnOamLspPingCtlPathDestType_Type(InetAddressType):
    """Custom type tnOamLspPingCtlPathDestType based on InetAddressType"""
    defaultValue = 0


_TnOamLspPingCtlPathDestType_Type.__name__ = "InetAddressType"
_TnOamLspPingCtlPathDestType_Object = MibTableColumn
tnOamLspPingCtlPathDestType = _TnOamLspPingCtlPathDestType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 16, 1, 11),
    _TnOamLspPingCtlPathDestType_Type()
)
tnOamLspPingCtlPathDestType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamLspPingCtlPathDestType.setStatus("current")


class _TnOamLspPingCtlPathDest_Type(InetAddress):
    """Custom type tnOamLspPingCtlPathDest based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TnOamLspPingCtlPathDest_Type.__name__ = "InetAddress"
_TnOamLspPingCtlPathDest_Object = MibTableColumn
tnOamLspPingCtlPathDest = _TnOamLspPingCtlPathDest_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 16, 1, 12),
    _TnOamLspPingCtlPathDest_Type()
)
tnOamLspPingCtlPathDest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamLspPingCtlPathDest.setStatus("current")


class _TnOamLspPingCtlNhIntfName_Type(TNamedItemOrEmpty):
    """Custom type tnOamLspPingCtlNhIntfName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TnOamLspPingCtlNhIntfName_Type.__name__ = "TNamedItemOrEmpty"
_TnOamLspPingCtlNhIntfName_Object = MibTableColumn
tnOamLspPingCtlNhIntfName = _TnOamLspPingCtlNhIntfName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 16, 1, 13),
    _TnOamLspPingCtlNhIntfName_Type()
)
tnOamLspPingCtlNhIntfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamLspPingCtlNhIntfName.setStatus("current")


class _TnOamLspPingCtlNhAddressType_Type(InetAddressType):
    """Custom type tnOamLspPingCtlNhAddressType based on InetAddressType"""
    defaultValue = 0


_TnOamLspPingCtlNhAddressType_Type.__name__ = "InetAddressType"
_TnOamLspPingCtlNhAddressType_Object = MibTableColumn
tnOamLspPingCtlNhAddressType = _TnOamLspPingCtlNhAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 16, 1, 14),
    _TnOamLspPingCtlNhAddressType_Type()
)
tnOamLspPingCtlNhAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamLspPingCtlNhAddressType.setStatus("current")


class _TnOamLspPingCtlNhAddress_Type(InetAddress):
    """Custom type tnOamLspPingCtlNhAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TnOamLspPingCtlNhAddress_Type.__name__ = "InetAddress"
_TnOamLspPingCtlNhAddress_Object = MibTableColumn
tnOamLspPingCtlNhAddress = _TnOamLspPingCtlNhAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 16, 1, 15),
    _TnOamLspPingCtlNhAddress_Type()
)
tnOamLspPingCtlNhAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamLspPingCtlNhAddress.setStatus("current")


class _TnOamLspPingCtlTestSubMode_Type(TmnxOamLspTestSubMode):
    """Custom type tnOamLspPingCtlTestSubMode based on TmnxOamLspTestSubMode"""
    defaultValue = 1


_TnOamLspPingCtlTestSubMode_Type.__name__ = "TmnxOamLspTestSubMode"
_TnOamLspPingCtlTestSubMode_Object = MibTableColumn
tnOamLspPingCtlTestSubMode = _TnOamLspPingCtlTestSubMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 16, 1, 16),
    _TnOamLspPingCtlTestSubMode_Type()
)
tnOamLspPingCtlTestSubMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamLspPingCtlTestSubMode.setStatus("current")


class _TnOamLspPingCtlMplsTpPathType_Type(TmnxOamMplsTpPathType):
    """Custom type tnOamLspPingCtlMplsTpPathType based on TmnxOamMplsTpPathType"""
    defaultValue = 3


_TnOamLspPingCtlMplsTpPathType_Type.__name__ = "TmnxOamMplsTpPathType"
_TnOamLspPingCtlMplsTpPathType_Object = MibTableColumn
tnOamLspPingCtlMplsTpPathType = _TnOamLspPingCtlMplsTpPathType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 16, 1, 17),
    _TnOamLspPingCtlMplsTpPathType_Type()
)
tnOamLspPingCtlMplsTpPathType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamLspPingCtlMplsTpPathType.setStatus("current")


class _TnOamLspPingCtlMplsTpGlobalId_Type(TmnxMplsTpGlobalID):
    """Custom type tnOamLspPingCtlMplsTpGlobalId based on TmnxMplsTpGlobalID"""
    defaultValue = 0


_TnOamLspPingCtlMplsTpGlobalId_Type.__name__ = "TmnxMplsTpGlobalID"
_TnOamLspPingCtlMplsTpGlobalId_Object = MibTableColumn
tnOamLspPingCtlMplsTpGlobalId = _TnOamLspPingCtlMplsTpGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 16, 1, 18),
    _TnOamLspPingCtlMplsTpGlobalId_Type()
)
tnOamLspPingCtlMplsTpGlobalId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamLspPingCtlMplsTpGlobalId.setStatus("current")


class _TnOamLspPingCtlMplsTpNodeId_Type(TmnxMplsTpNodeID):
    """Custom type tnOamLspPingCtlMplsTpNodeId based on TmnxMplsTpNodeID"""
    defaultValue = 0


_TnOamLspPingCtlMplsTpNodeId_Type.__name__ = "TmnxMplsTpNodeID"
_TnOamLspPingCtlMplsTpNodeId_Object = MibTableColumn
tnOamLspPingCtlMplsTpNodeId = _TnOamLspPingCtlMplsTpNodeId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 16, 1, 19),
    _TnOamLspPingCtlMplsTpNodeId_Type()
)
tnOamLspPingCtlMplsTpNodeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamLspPingCtlMplsTpNodeId.setStatus("current")


class _TnOamLspPingCtlAssocChannel_Type(TmnxOamLspAssocChannel):
    """Custom type tnOamLspPingCtlAssocChannel based on TmnxOamLspAssocChannel"""
    defaultValue = 1


_TnOamLspPingCtlAssocChannel_Type.__name__ = "TmnxOamLspAssocChannel"
_TnOamLspPingCtlAssocChannel_Object = MibTableColumn
tnOamLspPingCtlAssocChannel = _TnOamLspPingCtlAssocChannel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 16, 1, 20),
    _TnOamLspPingCtlAssocChannel_Type()
)
tnOamLspPingCtlAssocChannel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamLspPingCtlAssocChannel.setStatus("current")


class _TnOamLspPingCtlForce_Type(TruthValue):
    """Custom type tnOamLspPingCtlForce based on TruthValue"""
    defaultValue = 2


_TnOamLspPingCtlForce_Type.__name__ = "TruthValue"
_TnOamLspPingCtlForce_Object = MibTableColumn
tnOamLspPingCtlForce = _TnOamLspPingCtlForce_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 16, 1, 21),
    _TnOamLspPingCtlForce_Type()
)
tnOamLspPingCtlForce.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamLspPingCtlForce.setStatus("current")
_TnOamVccvPingCtlTable_Object = MibTable
tnOamVccvPingCtlTable = _TnOamVccvPingCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 32)
)
if mibBuilder.loadTexts:
    tnOamVccvPingCtlTable.setStatus("current")
_TnOamVccvPingCtlEntry_Object = MibTableRow
tnOamVccvPingCtlEntry = _TnOamVccvPingCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 32, 1)
)
tnOamVccvPingCtlEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-OAM-TEST-MIB", "tnOamPingCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tnOamVccvPingCtlEntry.setStatus("current")


class _TnOamVccvPingCtlSdpIdVcId_Type(SdpBindId):
    """Custom type tnOamVccvPingCtlSdpIdVcId based on SdpBindId"""
    defaultHexValue = "0000000000000000"


_TnOamVccvPingCtlSdpIdVcId_Type.__name__ = "SdpBindId"
_TnOamVccvPingCtlSdpIdVcId_Object = MibTableColumn
tnOamVccvPingCtlSdpIdVcId = _TnOamVccvPingCtlSdpIdVcId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 32, 1, 1),
    _TnOamVccvPingCtlSdpIdVcId_Type()
)
tnOamVccvPingCtlSdpIdVcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamVccvPingCtlSdpIdVcId.setStatus("current")


class _TnOamVccvPingCtlReplyMode_Type(Integer32):
    """Custom type tnOamVccvPingCtlReplyMode based on Integer32"""
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


_TnOamVccvPingCtlReplyMode_Type.__name__ = "Integer32"
_TnOamVccvPingCtlReplyMode_Object = MibTableColumn
tnOamVccvPingCtlReplyMode = _TnOamVccvPingCtlReplyMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 32, 1, 2),
    _TnOamVccvPingCtlReplyMode_Type()
)
tnOamVccvPingCtlReplyMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamVccvPingCtlReplyMode.setStatus("current")


class _TnOamVccvPingCtlPwId_Type(TmnxVcIdOrNone):
    """Custom type tnOamVccvPingCtlPwId based on TmnxVcIdOrNone"""
    defaultValue = 0


_TnOamVccvPingCtlPwId_Type.__name__ = "TmnxVcIdOrNone"
_TnOamVccvPingCtlPwId_Object = MibTableColumn
tnOamVccvPingCtlPwId = _TnOamVccvPingCtlPwId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 32, 1, 3),
    _TnOamVccvPingCtlPwId_Type()
)
tnOamVccvPingCtlPwId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamVccvPingCtlPwId.setStatus("current")


class _TnOamVccvPingCtlTtl_Type(Unsigned32):
    """Custom type tnOamVccvPingCtlTtl based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TnOamVccvPingCtlTtl_Type.__name__ = "Unsigned32"
_TnOamVccvPingCtlTtl_Object = MibTableColumn
tnOamVccvPingCtlTtl = _TnOamVccvPingCtlTtl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 32, 1, 4),
    _TnOamVccvPingCtlTtl_Type()
)
tnOamVccvPingCtlTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamVccvPingCtlTtl.setStatus("current")
if mibBuilder.loadTexts:
    tnOamVccvPingCtlTtl.setUnits("time-to-live value")


class _TnOamVccvPingCtlSpokeSdpId_Type(TmnxSpokeSdpIdOrZero):
    """Custom type tnOamVccvPingCtlSpokeSdpId based on TmnxSpokeSdpIdOrZero"""
    defaultValue = 0


_TnOamVccvPingCtlSpokeSdpId_Type.__name__ = "TmnxSpokeSdpIdOrZero"
_TnOamVccvPingCtlSpokeSdpId_Object = MibTableColumn
tnOamVccvPingCtlSpokeSdpId = _TnOamVccvPingCtlSpokeSdpId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 32, 1, 5),
    _TnOamVccvPingCtlSpokeSdpId_Type()
)
tnOamVccvPingCtlSpokeSdpId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamVccvPingCtlSpokeSdpId.setStatus("current")


class _TnOamVccvPingCtlSaiiGlobalId_Type(TmnxPwGlobalIdOrZero):
    """Custom type tnOamVccvPingCtlSaiiGlobalId based on TmnxPwGlobalIdOrZero"""
    defaultValue = 0


_TnOamVccvPingCtlSaiiGlobalId_Type.__name__ = "TmnxPwGlobalIdOrZero"
_TnOamVccvPingCtlSaiiGlobalId_Object = MibTableColumn
tnOamVccvPingCtlSaiiGlobalId = _TnOamVccvPingCtlSaiiGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 32, 1, 6),
    _TnOamVccvPingCtlSaiiGlobalId_Type()
)
tnOamVccvPingCtlSaiiGlobalId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamVccvPingCtlSaiiGlobalId.setStatus("current")


class _TnOamVccvPingCtlSaiiPrefix_Type(Unsigned32):
    """Custom type tnOamVccvPingCtlSaiiPrefix based on Unsigned32"""
    defaultValue = 0


_TnOamVccvPingCtlSaiiPrefix_Type.__name__ = "Unsigned32"
_TnOamVccvPingCtlSaiiPrefix_Object = MibTableColumn
tnOamVccvPingCtlSaiiPrefix = _TnOamVccvPingCtlSaiiPrefix_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 32, 1, 7),
    _TnOamVccvPingCtlSaiiPrefix_Type()
)
tnOamVccvPingCtlSaiiPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamVccvPingCtlSaiiPrefix.setStatus("current")


class _TnOamVccvPingCtlSaiiAcId_Type(Unsigned32):
    """Custom type tnOamVccvPingCtlSaiiAcId based on Unsigned32"""
    defaultValue = 0


_TnOamVccvPingCtlSaiiAcId_Type.__name__ = "Unsigned32"
_TnOamVccvPingCtlSaiiAcId_Object = MibTableColumn
tnOamVccvPingCtlSaiiAcId = _TnOamVccvPingCtlSaiiAcId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 32, 1, 8),
    _TnOamVccvPingCtlSaiiAcId_Type()
)
tnOamVccvPingCtlSaiiAcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamVccvPingCtlSaiiAcId.setStatus("current")


class _TnOamVccvPingCtlTaiiGlobalId_Type(TmnxPwGlobalIdOrZero):
    """Custom type tnOamVccvPingCtlTaiiGlobalId based on TmnxPwGlobalIdOrZero"""
    defaultValue = 0


_TnOamVccvPingCtlTaiiGlobalId_Type.__name__ = "TmnxPwGlobalIdOrZero"
_TnOamVccvPingCtlTaiiGlobalId_Object = MibTableColumn
tnOamVccvPingCtlTaiiGlobalId = _TnOamVccvPingCtlTaiiGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 32, 1, 9),
    _TnOamVccvPingCtlTaiiGlobalId_Type()
)
tnOamVccvPingCtlTaiiGlobalId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamVccvPingCtlTaiiGlobalId.setStatus("current")


class _TnOamVccvPingCtlTaiiPrefix_Type(Unsigned32):
    """Custom type tnOamVccvPingCtlTaiiPrefix based on Unsigned32"""
    defaultValue = 0


_TnOamVccvPingCtlTaiiPrefix_Type.__name__ = "Unsigned32"
_TnOamVccvPingCtlTaiiPrefix_Object = MibTableColumn
tnOamVccvPingCtlTaiiPrefix = _TnOamVccvPingCtlTaiiPrefix_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 32, 1, 10),
    _TnOamVccvPingCtlTaiiPrefix_Type()
)
tnOamVccvPingCtlTaiiPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamVccvPingCtlTaiiPrefix.setStatus("current")


class _TnOamVccvPingCtlTaiiAcId_Type(Unsigned32):
    """Custom type tnOamVccvPingCtlTaiiAcId based on Unsigned32"""
    defaultValue = 0


_TnOamVccvPingCtlTaiiAcId_Type.__name__ = "Unsigned32"
_TnOamVccvPingCtlTaiiAcId_Object = MibTableColumn
tnOamVccvPingCtlTaiiAcId = _TnOamVccvPingCtlTaiiAcId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 32, 1, 11),
    _TnOamVccvPingCtlTaiiAcId_Type()
)
tnOamVccvPingCtlTaiiAcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamVccvPingCtlTaiiAcId.setStatus("current")


class _TnOamVccvPingCtlMplsTpGlobalId_Type(TmnxMplsTpGlobalID):
    """Custom type tnOamVccvPingCtlMplsTpGlobalId based on TmnxMplsTpGlobalID"""
    defaultValue = 0


_TnOamVccvPingCtlMplsTpGlobalId_Type.__name__ = "TmnxMplsTpGlobalID"
_TnOamVccvPingCtlMplsTpGlobalId_Object = MibTableColumn
tnOamVccvPingCtlMplsTpGlobalId = _TnOamVccvPingCtlMplsTpGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 32, 1, 12),
    _TnOamVccvPingCtlMplsTpGlobalId_Type()
)
tnOamVccvPingCtlMplsTpGlobalId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamVccvPingCtlMplsTpGlobalId.setStatus("current")


class _TnOamVccvPingCtlMplsTpNodeId_Type(TmnxMplsTpNodeID):
    """Custom type tnOamVccvPingCtlMplsTpNodeId based on TmnxMplsTpNodeID"""
    defaultValue = 0


_TnOamVccvPingCtlMplsTpNodeId_Type.__name__ = "TmnxMplsTpNodeID"
_TnOamVccvPingCtlMplsTpNodeId_Object = MibTableColumn
tnOamVccvPingCtlMplsTpNodeId = _TnOamVccvPingCtlMplsTpNodeId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 32, 1, 13),
    _TnOamVccvPingCtlMplsTpNodeId_Type()
)
tnOamVccvPingCtlMplsTpNodeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamVccvPingCtlMplsTpNodeId.setStatus("current")


class _TnOamVccvPingCtlTestSubMode_Type(TmnxOamVccvTestSubMode):
    """Custom type tnOamVccvPingCtlTestSubMode based on TmnxOamVccvTestSubMode"""
    defaultValue = 1


_TnOamVccvPingCtlTestSubMode_Type.__name__ = "TmnxOamVccvTestSubMode"
_TnOamVccvPingCtlTestSubMode_Object = MibTableColumn
tnOamVccvPingCtlTestSubMode = _TnOamVccvPingCtlTestSubMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 32, 1, 14),
    _TnOamVccvPingCtlTestSubMode_Type()
)
tnOamVccvPingCtlTestSubMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamVccvPingCtlTestSubMode.setStatus("current")


class _TnOamVccvPingCtlAssocChannel_Type(TmnxOamVccvAssocChannel):
    """Custom type tnOamVccvPingCtlAssocChannel based on TmnxOamVccvAssocChannel"""
    defaultValue = 1


_TnOamVccvPingCtlAssocChannel_Type.__name__ = "TmnxOamVccvAssocChannel"
_TnOamVccvPingCtlAssocChannel_Object = MibTableColumn
tnOamVccvPingCtlAssocChannel = _TnOamVccvPingCtlAssocChannel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 32, 1, 15),
    _TnOamVccvPingCtlAssocChannel_Type()
)
tnOamVccvPingCtlAssocChannel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamVccvPingCtlAssocChannel.setStatus("current")
_TnOamEthCfmPingCtlTable_Object = MibTable
tnOamEthCfmPingCtlTable = _TnOamEthCfmPingCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 44)
)
if mibBuilder.loadTexts:
    tnOamEthCfmPingCtlTable.setStatus("current")
_TnOamEthCfmPingCtlEntry_Object = MibTableRow
tnOamEthCfmPingCtlEntry = _TnOamEthCfmPingCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 44, 1)
)
if mibBuilder.loadTexts:
    tnOamEthCfmPingCtlEntry.setStatus("current")


class _TnOamEthCfmPingCtlTgtMacAddr_Type(MacAddress):
    """Custom type tnOamEthCfmPingCtlTgtMacAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_TnOamEthCfmPingCtlTgtMacAddr_Type.__name__ = "MacAddress"
_TnOamEthCfmPingCtlTgtMacAddr_Object = MibTableColumn
tnOamEthCfmPingCtlTgtMacAddr = _TnOamEthCfmPingCtlTgtMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 44, 1, 1),
    _TnOamEthCfmPingCtlTgtMacAddr_Type()
)
tnOamEthCfmPingCtlTgtMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamEthCfmPingCtlTgtMacAddr.setStatus("current")


class _TnOamEthCfmPingCtlSrcMdIndex_Type(Unsigned32):
    """Custom type tnOamEthCfmPingCtlSrcMdIndex based on Unsigned32"""
    defaultValue = 0


_TnOamEthCfmPingCtlSrcMdIndex_Type.__name__ = "Unsigned32"
_TnOamEthCfmPingCtlSrcMdIndex_Object = MibTableColumn
tnOamEthCfmPingCtlSrcMdIndex = _TnOamEthCfmPingCtlSrcMdIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 44, 1, 2),
    _TnOamEthCfmPingCtlSrcMdIndex_Type()
)
tnOamEthCfmPingCtlSrcMdIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamEthCfmPingCtlSrcMdIndex.setStatus("current")


class _TnOamEthCfmPingCtlSrcMaIndex_Type(Unsigned32):
    """Custom type tnOamEthCfmPingCtlSrcMaIndex based on Unsigned32"""
    defaultValue = 0


_TnOamEthCfmPingCtlSrcMaIndex_Type.__name__ = "Unsigned32"
_TnOamEthCfmPingCtlSrcMaIndex_Object = MibTableColumn
tnOamEthCfmPingCtlSrcMaIndex = _TnOamEthCfmPingCtlSrcMaIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 44, 1, 3),
    _TnOamEthCfmPingCtlSrcMaIndex_Type()
)
tnOamEthCfmPingCtlSrcMaIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamEthCfmPingCtlSrcMaIndex.setStatus("current")


class _TnOamEthCfmPingCtlSrcMepId_Type(Dot1agCfmMepIdOrZero):
    """Custom type tnOamEthCfmPingCtlSrcMepId based on Dot1agCfmMepIdOrZero"""
    defaultValue = 0


_TnOamEthCfmPingCtlSrcMepId_Type.__name__ = "Dot1agCfmMepIdOrZero"
_TnOamEthCfmPingCtlSrcMepId_Object = MibTableColumn
tnOamEthCfmPingCtlSrcMepId = _TnOamEthCfmPingCtlSrcMepId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 1, 44, 1, 4),
    _TnOamEthCfmPingCtlSrcMepId_Type()
)
tnOamEthCfmPingCtlSrcMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamEthCfmPingCtlSrcMepId.setStatus("current")
_TnOamTraceRouteObjs_ObjectIdentity = ObjectIdentity
tnOamTraceRouteObjs = _TnOamTraceRouteObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2)
)
_TnOamTrCtlTable_Object = MibTable
tnOamTrCtlTable = _TnOamTrCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 3)
)
if mibBuilder.loadTexts:
    tnOamTrCtlTable.setStatus("current")
_TnOamTrCtlEntry_Object = MibTableRow
tnOamTrCtlEntry = _TnOamTrCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 3, 1)
)
tnOamTrCtlEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-OAM-TEST-MIB", "tnOamTrCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tnOamTrCtlEntry.setStatus("current")


class _TnOamTrCtlTestIndex_Type(SnmpAdminString):
    """Custom type tnOamTrCtlTestIndex based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TnOamTrCtlTestIndex_Type.__name__ = "SnmpAdminString"
_TnOamTrCtlTestIndex_Object = MibTableColumn
tnOamTrCtlTestIndex = _TnOamTrCtlTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 3, 1, 2),
    _TnOamTrCtlTestIndex_Type()
)
tnOamTrCtlTestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOamTrCtlTestIndex.setStatus("current")
_TnOamTrCtlRowStatus_Type = RowStatus
_TnOamTrCtlRowStatus_Object = MibTableColumn
tnOamTrCtlRowStatus = _TnOamTrCtlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 3, 1, 3),
    _TnOamTrCtlRowStatus_Type()
)
tnOamTrCtlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamTrCtlRowStatus.setStatus("current")


class _TnOamTrCtlStorageType_Type(StorageType):
    """Custom type tnOamTrCtlStorageType based on StorageType"""
    defaultValue = 2


_TnOamTrCtlStorageType_Type.__name__ = "StorageType"
_TnOamTrCtlStorageType_Object = MibTableColumn
tnOamTrCtlStorageType = _TnOamTrCtlStorageType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 3, 1, 4),
    _TnOamTrCtlStorageType_Type()
)
tnOamTrCtlStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamTrCtlStorageType.setStatus("current")


class _TnOamTrCtlDescr_Type(SnmpAdminString):
    """Custom type tnOamTrCtlDescr based on SnmpAdminString"""
    defaultHexValue = "00"


_TnOamTrCtlDescr_Type.__name__ = "SnmpAdminString"
_TnOamTrCtlDescr_Object = MibTableColumn
tnOamTrCtlDescr = _TnOamTrCtlDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 3, 1, 5),
    _TnOamTrCtlDescr_Type()
)
tnOamTrCtlDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamTrCtlDescr.setStatus("current")


class _TnOamTrCtlTestMode_Type(Integer32):
    """Custom type tnOamTrCtlTestMode based on Integer32"""
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
              9)
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
          ("ethCfmLinkTrace", 9))
    )


_TnOamTrCtlTestMode_Type.__name__ = "Integer32"
_TnOamTrCtlTestMode_Object = MibTableColumn
tnOamTrCtlTestMode = _TnOamTrCtlTestMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 3, 1, 6),
    _TnOamTrCtlTestMode_Type()
)
tnOamTrCtlTestMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamTrCtlTestMode.setStatus("current")


class _TnOamTrCtlAdminStatus_Type(Integer32):
    """Custom type tnOamTrCtlAdminStatus based on Integer32"""
    defaultValue = 2

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


_TnOamTrCtlAdminStatus_Type.__name__ = "Integer32"
_TnOamTrCtlAdminStatus_Object = MibTableColumn
tnOamTrCtlAdminStatus = _TnOamTrCtlAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 3, 1, 7),
    _TnOamTrCtlAdminStatus_Type()
)
tnOamTrCtlAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamTrCtlAdminStatus.setStatus("current")


class _TnOamTrCtlFcName_Type(TFCName):
    """Custom type tnOamTrCtlFcName based on TFCName"""
    defaultValue = OctetString("be")


_TnOamTrCtlFcName_Type.__name__ = "TFCName"
_TnOamTrCtlFcName_Object = MibTableColumn
tnOamTrCtlFcName = _TnOamTrCtlFcName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 3, 1, 8),
    _TnOamTrCtlFcName_Type()
)
tnOamTrCtlFcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamTrCtlFcName.setStatus("current")


class _TnOamTrCtlProfile_Type(TProfile):
    """Custom type tnOamTrCtlProfile based on TProfile"""
    defaultValue = 2


_TnOamTrCtlProfile_Type.__name__ = "TProfile"
_TnOamTrCtlProfile_Object = MibTableColumn
tnOamTrCtlProfile = _TnOamTrCtlProfile_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 3, 1, 9),
    _TnOamTrCtlProfile_Type()
)
tnOamTrCtlProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamTrCtlProfile.setStatus("current")


class _TnOamTrCtlTargetIpAddress_Type(IpAddress):
    """Custom type tnOamTrCtlTargetIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_TnOamTrCtlTargetIpAddress_Type.__name__ = "IpAddress"
_TnOamTrCtlTargetIpAddress_Object = MibTableColumn
tnOamTrCtlTargetIpAddress = _TnOamTrCtlTargetIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 3, 1, 10),
    _TnOamTrCtlTargetIpAddress_Type()
)
tnOamTrCtlTargetIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamTrCtlTargetIpAddress.setStatus("obsolete")


class _TnOamTrCtlServiceId_Type(TmnxServId):
    """Custom type tnOamTrCtlServiceId based on TmnxServId"""
    defaultValue = 0

    subtypeSpec = TmnxServId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TnOamTrCtlServiceId_Type.__name__ = "TmnxServId"
_TnOamTrCtlServiceId_Object = MibTableColumn
tnOamTrCtlServiceId = _TnOamTrCtlServiceId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 3, 1, 11),
    _TnOamTrCtlServiceId_Type()
)
tnOamTrCtlServiceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamTrCtlServiceId.setStatus("current")


class _TnOamTrCtlDataSize_Type(Unsigned32):
    """Custom type tnOamTrCtlDataSize based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9198),
    )


_TnOamTrCtlDataSize_Type.__name__ = "Unsigned32"
_TnOamTrCtlDataSize_Object = MibTableColumn
tnOamTrCtlDataSize = _TnOamTrCtlDataSize_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 3, 1, 12),
    _TnOamTrCtlDataSize_Type()
)
tnOamTrCtlDataSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamTrCtlDataSize.setStatus("current")
if mibBuilder.loadTexts:
    tnOamTrCtlDataSize.setUnits("octets")


class _TnOamTrCtlTimeOut_Type(Unsigned32):
    """Custom type tnOamTrCtlTimeOut based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TnOamTrCtlTimeOut_Type.__name__ = "Unsigned32"
_TnOamTrCtlTimeOut_Object = MibTableColumn
tnOamTrCtlTimeOut = _TnOamTrCtlTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 3, 1, 13),
    _TnOamTrCtlTimeOut_Type()
)
tnOamTrCtlTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamTrCtlTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    tnOamTrCtlTimeOut.setUnits("seconds")


class _TnOamTrCtlProbesPerHop_Type(Unsigned32):
    """Custom type tnOamTrCtlProbesPerHop based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TnOamTrCtlProbesPerHop_Type.__name__ = "Unsigned32"
_TnOamTrCtlProbesPerHop_Object = MibTableColumn
tnOamTrCtlProbesPerHop = _TnOamTrCtlProbesPerHop_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 3, 1, 14),
    _TnOamTrCtlProbesPerHop_Type()
)
tnOamTrCtlProbesPerHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamTrCtlProbesPerHop.setStatus("current")
if mibBuilder.loadTexts:
    tnOamTrCtlProbesPerHop.setUnits("probes")


class _TnOamTrCtlMaxTtl_Type(Unsigned32):
    """Custom type tnOamTrCtlMaxTtl based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TnOamTrCtlMaxTtl_Type.__name__ = "Unsigned32"
_TnOamTrCtlMaxTtl_Object = MibTableColumn
tnOamTrCtlMaxTtl = _TnOamTrCtlMaxTtl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 3, 1, 15),
    _TnOamTrCtlMaxTtl_Type()
)
tnOamTrCtlMaxTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamTrCtlMaxTtl.setStatus("current")
if mibBuilder.loadTexts:
    tnOamTrCtlMaxTtl.setUnits("time-to-live value")


class _TnOamTrCtlInitialTtl_Type(Unsigned32):
    """Custom type tnOamTrCtlInitialTtl based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TnOamTrCtlInitialTtl_Type.__name__ = "Unsigned32"
_TnOamTrCtlInitialTtl_Object = MibTableColumn
tnOamTrCtlInitialTtl = _TnOamTrCtlInitialTtl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 3, 1, 16),
    _TnOamTrCtlInitialTtl_Type()
)
tnOamTrCtlInitialTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamTrCtlInitialTtl.setStatus("current")


class _TnOamTrCtlDSField_Type(Unsigned32):
    """Custom type tnOamTrCtlDSField based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnOamTrCtlDSField_Type.__name__ = "Unsigned32"
_TnOamTrCtlDSField_Object = MibTableColumn
tnOamTrCtlDSField = _TnOamTrCtlDSField_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 3, 1, 17),
    _TnOamTrCtlDSField_Type()
)
tnOamTrCtlDSField.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamTrCtlDSField.setStatus("current")


class _TnOamTrCtlMaxFailures_Type(Unsigned32):
    """Custom type tnOamTrCtlMaxFailures based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TnOamTrCtlMaxFailures_Type.__name__ = "Unsigned32"
_TnOamTrCtlMaxFailures_Object = MibTableColumn
tnOamTrCtlMaxFailures = _TnOamTrCtlMaxFailures_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 3, 1, 18),
    _TnOamTrCtlMaxFailures_Type()
)
tnOamTrCtlMaxFailures.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamTrCtlMaxFailures.setStatus("current")
if mibBuilder.loadTexts:
    tnOamTrCtlMaxFailures.setUnits("timeouts")


class _TnOamTrCtlInterval_Type(Unsigned32):
    """Custom type tnOamTrCtlInterval based on Unsigned32"""
    defaultValue = 1


_TnOamTrCtlInterval_Type.__name__ = "Unsigned32"
_TnOamTrCtlInterval_Object = MibTableColumn
tnOamTrCtlInterval = _TnOamTrCtlInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 3, 1, 19),
    _TnOamTrCtlInterval_Type()
)
tnOamTrCtlInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamTrCtlInterval.setStatus("current")
if mibBuilder.loadTexts:
    tnOamTrCtlInterval.setUnits("seconds")


class _TnOamTrCtlMaxRows_Type(Unsigned32):
    """Custom type tnOamTrCtlMaxRows based on Unsigned32"""
    defaultValue = 300


_TnOamTrCtlMaxRows_Type.__name__ = "Unsigned32"
_TnOamTrCtlMaxRows_Object = MibTableColumn
tnOamTrCtlMaxRows = _TnOamTrCtlMaxRows_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 3, 1, 20),
    _TnOamTrCtlMaxRows_Type()
)
tnOamTrCtlMaxRows.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamTrCtlMaxRows.setStatus("obsolete")
if mibBuilder.loadTexts:
    tnOamTrCtlMaxRows.setUnits("rows")


class _TnOamTrCtlTrapGeneration_Type(Bits):
    """Custom type tnOamTrCtlTrapGeneration based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("pathChange", 0),
          ("testFailure", 1),
          ("testCompletion", 2))
    )

_TnOamTrCtlTrapGeneration_Type.__name__ = "Bits"
_TnOamTrCtlTrapGeneration_Object = MibTableColumn
tnOamTrCtlTrapGeneration = _TnOamTrCtlTrapGeneration_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 3, 1, 21),
    _TnOamTrCtlTrapGeneration_Type()
)
tnOamTrCtlTrapGeneration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamTrCtlTrapGeneration.setStatus("current")


class _TnOamTrCtlCreateHopsEntries_Type(TruthValue):
    """Custom type tnOamTrCtlCreateHopsEntries based on TruthValue"""
    defaultValue = 2


_TnOamTrCtlCreateHopsEntries_Type.__name__ = "TruthValue"
_TnOamTrCtlCreateHopsEntries_Object = MibTableColumn
tnOamTrCtlCreateHopsEntries = _TnOamTrCtlCreateHopsEntries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 3, 1, 22),
    _TnOamTrCtlCreateHopsEntries_Type()
)
tnOamTrCtlCreateHopsEntries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamTrCtlCreateHopsEntries.setStatus("obsolete")


class _TnOamTrCtlSAA_Type(TruthValue):
    """Custom type tnOamTrCtlSAA based on TruthValue"""
    defaultValue = 2


_TnOamTrCtlSAA_Type.__name__ = "TruthValue"
_TnOamTrCtlSAA_Object = MibTableColumn
tnOamTrCtlSAA = _TnOamTrCtlSAA_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 3, 1, 23),
    _TnOamTrCtlSAA_Type()
)
tnOamTrCtlSAA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamTrCtlSAA.setStatus("current")
_TnOamTrCtlRuns_Type = Counter32
_TnOamTrCtlRuns_Object = MibTableColumn
tnOamTrCtlRuns = _TnOamTrCtlRuns_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 3, 1, 24),
    _TnOamTrCtlRuns_Type()
)
tnOamTrCtlRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamTrCtlRuns.setStatus("current")
_TnOamTrCtlFailures_Type = Counter32
_TnOamTrCtlFailures_Object = MibTableColumn
tnOamTrCtlFailures = _TnOamTrCtlFailures_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 3, 1, 25),
    _TnOamTrCtlFailures_Type()
)
tnOamTrCtlFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamTrCtlFailures.setStatus("current")
_TnOamTrCtlLastRunResult_Type = TmnxOamTestResult
_TnOamTrCtlLastRunResult_Object = MibTableColumn
tnOamTrCtlLastRunResult = _TnOamTrCtlLastRunResult_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 3, 1, 26),
    _TnOamTrCtlLastRunResult_Type()
)
tnOamTrCtlLastRunResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamTrCtlLastRunResult.setStatus("current")
_TnOamTrCtlLastChanged_Type = TimeStamp
_TnOamTrCtlLastChanged_Object = MibTableColumn
tnOamTrCtlLastChanged = _TnOamTrCtlLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 3, 1, 27),
    _TnOamTrCtlLastChanged_Type()
)
tnOamTrCtlLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamTrCtlLastChanged.setStatus("current")


class _TnOamTrCtlVRtrID_Type(TmnxVRtrID):
    """Custom type tnOamTrCtlVRtrID based on TmnxVRtrID"""
    defaultValue = 1


_TnOamTrCtlVRtrID_Type.__name__ = "TmnxVRtrID"
_TnOamTrCtlVRtrID_Object = MibTableColumn
tnOamTrCtlVRtrID = _TnOamTrCtlVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 3, 1, 28),
    _TnOamTrCtlVRtrID_Type()
)
tnOamTrCtlVRtrID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamTrCtlVRtrID.setStatus("current")


class _TnOamTrCtlTgtAddrType_Type(InetAddressType):
    """Custom type tnOamTrCtlTgtAddrType based on InetAddressType"""
    defaultValue = 0


_TnOamTrCtlTgtAddrType_Type.__name__ = "InetAddressType"
_TnOamTrCtlTgtAddrType_Object = MibTableColumn
tnOamTrCtlTgtAddrType = _TnOamTrCtlTgtAddrType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 3, 1, 29),
    _TnOamTrCtlTgtAddrType_Type()
)
tnOamTrCtlTgtAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamTrCtlTgtAddrType.setStatus("current")


class _TnOamTrCtlTgtAddress_Type(InetAddress):
    """Custom type tnOamTrCtlTgtAddress based on InetAddress"""
    defaultHexValue = ""


_TnOamTrCtlTgtAddress_Type.__name__ = "InetAddress"
_TnOamTrCtlTgtAddress_Object = MibTableColumn
tnOamTrCtlTgtAddress = _TnOamTrCtlTgtAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 3, 1, 30),
    _TnOamTrCtlTgtAddress_Type()
)
tnOamTrCtlTgtAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamTrCtlTgtAddress.setStatus("current")


class _TnOamTrCtlSrcAddrType_Type(InetAddressType):
    """Custom type tnOamTrCtlSrcAddrType based on InetAddressType"""
    defaultValue = 0


_TnOamTrCtlSrcAddrType_Type.__name__ = "InetAddressType"
_TnOamTrCtlSrcAddrType_Object = MibTableColumn
tnOamTrCtlSrcAddrType = _TnOamTrCtlSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 3, 1, 31),
    _TnOamTrCtlSrcAddrType_Type()
)
tnOamTrCtlSrcAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamTrCtlSrcAddrType.setStatus("current")


class _TnOamTrCtlSrcAddress_Type(InetAddress):
    """Custom type tnOamTrCtlSrcAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TnOamTrCtlSrcAddress_Type.__name__ = "InetAddress"
_TnOamTrCtlSrcAddress_Object = MibTableColumn
tnOamTrCtlSrcAddress = _TnOamTrCtlSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 3, 1, 32),
    _TnOamTrCtlSrcAddress_Type()
)
tnOamTrCtlSrcAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamTrCtlSrcAddress.setStatus("current")


class _TnOamTrCtlWaitMilliSec_Type(Unsigned32):
    """Custom type tnOamTrCtlWaitMilliSec based on Unsigned32"""
    defaultValue = 5000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 60000),
    )


_TnOamTrCtlWaitMilliSec_Type.__name__ = "Unsigned32"
_TnOamTrCtlWaitMilliSec_Object = MibTableColumn
tnOamTrCtlWaitMilliSec = _TnOamTrCtlWaitMilliSec_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 3, 1, 33),
    _TnOamTrCtlWaitMilliSec_Type()
)
tnOamTrCtlWaitMilliSec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamTrCtlWaitMilliSec.setStatus("current")
if mibBuilder.loadTexts:
    tnOamTrCtlWaitMilliSec.setUnits("milliseconds")
_TnOamTrResultsTable_Object = MibTable
tnOamTrResultsTable = _TnOamTrResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 4)
)
if mibBuilder.loadTexts:
    tnOamTrResultsTable.setStatus("current")
_TnOamTrResultsEntry_Object = MibTableRow
tnOamTrResultsEntry = _TnOamTrResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 4, 1)
)
tnOamTrResultsEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-OAM-TEST-MIB", "tnOamTrCtlTestIndex"),
    (0, "TN-OAM-TEST-MIB", "tnOamTrResultsTestRunIndex"),
)
if mibBuilder.loadTexts:
    tnOamTrResultsEntry.setStatus("current")


class _TnOamTrResultsOperStatus_Type(Integer32):
    """Custom type tnOamTrResultsOperStatus based on Integer32"""
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


_TnOamTrResultsOperStatus_Type.__name__ = "Integer32"
_TnOamTrResultsOperStatus_Object = MibTableColumn
tnOamTrResultsOperStatus = _TnOamTrResultsOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 4, 1, 1),
    _TnOamTrResultsOperStatus_Type()
)
tnOamTrResultsOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamTrResultsOperStatus.setStatus("current")
_TnOamTrResultsCurHopCount_Type = Gauge32
_TnOamTrResultsCurHopCount_Object = MibTableColumn
tnOamTrResultsCurHopCount = _TnOamTrResultsCurHopCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 4, 1, 2),
    _TnOamTrResultsCurHopCount_Type()
)
tnOamTrResultsCurHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamTrResultsCurHopCount.setStatus("current")
if mibBuilder.loadTexts:
    tnOamTrResultsCurHopCount.setUnits("hops")
_TnOamTrResultsCurProbeCount_Type = Gauge32
_TnOamTrResultsCurProbeCount_Object = MibTableColumn
tnOamTrResultsCurProbeCount = _TnOamTrResultsCurProbeCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 4, 1, 3),
    _TnOamTrResultsCurProbeCount_Type()
)
tnOamTrResultsCurProbeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamTrResultsCurProbeCount.setStatus("current")
if mibBuilder.loadTexts:
    tnOamTrResultsCurProbeCount.setUnits("probes")
_TnOamTrResultsIpTgtAddr_Type = IpAddress
_TnOamTrResultsIpTgtAddr_Object = MibTableColumn
tnOamTrResultsIpTgtAddr = _TnOamTrResultsIpTgtAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 4, 1, 4),
    _TnOamTrResultsIpTgtAddr_Type()
)
tnOamTrResultsIpTgtAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamTrResultsIpTgtAddr.setStatus("obsolete")
_TnOamTrResultsTestAttempts_Type = Unsigned32
_TnOamTrResultsTestAttempts_Object = MibTableColumn
tnOamTrResultsTestAttempts = _TnOamTrResultsTestAttempts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 4, 1, 5),
    _TnOamTrResultsTestAttempts_Type()
)
tnOamTrResultsTestAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamTrResultsTestAttempts.setStatus("obsolete")
if mibBuilder.loadTexts:
    tnOamTrResultsTestAttempts.setUnits("tests")
_TnOamTrResultsTestSuccesses_Type = Unsigned32
_TnOamTrResultsTestSuccesses_Object = MibTableColumn
tnOamTrResultsTestSuccesses = _TnOamTrResultsTestSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 4, 1, 6),
    _TnOamTrResultsTestSuccesses_Type()
)
tnOamTrResultsTestSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamTrResultsTestSuccesses.setStatus("obsolete")
if mibBuilder.loadTexts:
    tnOamTrResultsTestSuccesses.setUnits("tests")
_TnOamTrResultsLastGoodPath_Type = DateAndTime
_TnOamTrResultsLastGoodPath_Object = MibTableColumn
tnOamTrResultsLastGoodPath = _TnOamTrResultsLastGoodPath_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 4, 1, 7),
    _TnOamTrResultsLastGoodPath_Type()
)
tnOamTrResultsLastGoodPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamTrResultsLastGoodPath.setStatus("current")


class _TnOamTrResultsTestRunIndex_Type(Unsigned32):
    """Custom type tnOamTrResultsTestRunIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TnOamTrResultsTestRunIndex_Type.__name__ = "Unsigned32"
_TnOamTrResultsTestRunIndex_Object = MibTableColumn
tnOamTrResultsTestRunIndex = _TnOamTrResultsTestRunIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 4, 1, 8),
    _TnOamTrResultsTestRunIndex_Type()
)
tnOamTrResultsTestRunIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOamTrResultsTestRunIndex.setStatus("current")
_TnOamTrResultsTgtAddrType_Type = InetAddressType
_TnOamTrResultsTgtAddrType_Object = MibTableColumn
tnOamTrResultsTgtAddrType = _TnOamTrResultsTgtAddrType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 4, 1, 9),
    _TnOamTrResultsTgtAddrType_Type()
)
tnOamTrResultsTgtAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamTrResultsTgtAddrType.setStatus("current")


class _TnOamTrResultsTgtAddress_Type(InetAddress):
    """Custom type tnOamTrResultsTgtAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TnOamTrResultsTgtAddress_Type.__name__ = "InetAddress"
_TnOamTrResultsTgtAddress_Object = MibTableColumn
tnOamTrResultsTgtAddress = _TnOamTrResultsTgtAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 4, 1, 10),
    _TnOamTrResultsTgtAddress_Type()
)
tnOamTrResultsTgtAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamTrResultsTgtAddress.setStatus("current")
_TnOamTrResultsTestRunResult_Type = TmnxOamTestResult
_TnOamTrResultsTestRunResult_Object = MibTableColumn
tnOamTrResultsTestRunResult = _TnOamTrResultsTestRunResult_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 4, 1, 11),
    _TnOamTrResultsTestRunResult_Type()
)
tnOamTrResultsTestRunResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamTrResultsTestRunResult.setStatus("current")
_TnOamTrProbeHistoryTable_Object = MibTable
tnOamTrProbeHistoryTable = _TnOamTrProbeHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 5)
)
if mibBuilder.loadTexts:
    tnOamTrProbeHistoryTable.setStatus("current")
_TnOamTrProbeHistoryEntry_Object = MibTableRow
tnOamTrProbeHistoryEntry = _TnOamTrProbeHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 5, 1)
)
tnOamTrProbeHistoryEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-OAM-TEST-MIB", "tnOamTrCtlTestIndex"),
    (0, "TN-OAM-TEST-MIB", "tnOamTrResultsTestRunIndex"),
    (0, "TN-OAM-TEST-MIB", "tnOamTrProbeHistoryIndex"),
    (0, "TN-OAM-TEST-MIB", "tnOamTrProbeHistoryHopIndex"),
    (0, "TN-OAM-TEST-MIB", "tnOamTrProbeHistoryProbeIndex"),
)
if mibBuilder.loadTexts:
    tnOamTrProbeHistoryEntry.setStatus("current")


class _TnOamTrProbeHistoryIndex_Type(Unsigned32):
    """Custom type tnOamTrProbeHistoryIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TnOamTrProbeHistoryIndex_Type.__name__ = "Unsigned32"
_TnOamTrProbeHistoryIndex_Object = MibTableColumn
tnOamTrProbeHistoryIndex = _TnOamTrProbeHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 5, 1, 1),
    _TnOamTrProbeHistoryIndex_Type()
)
tnOamTrProbeHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOamTrProbeHistoryIndex.setStatus("current")


class _TnOamTrProbeHistoryHopIndex_Type(Unsigned32):
    """Custom type tnOamTrProbeHistoryHopIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TnOamTrProbeHistoryHopIndex_Type.__name__ = "Unsigned32"
_TnOamTrProbeHistoryHopIndex_Object = MibTableColumn
tnOamTrProbeHistoryHopIndex = _TnOamTrProbeHistoryHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 5, 1, 2),
    _TnOamTrProbeHistoryHopIndex_Type()
)
tnOamTrProbeHistoryHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOamTrProbeHistoryHopIndex.setStatus("current")


class _TnOamTrProbeHistoryProbeIndex_Type(Unsigned32):
    """Custom type tnOamTrProbeHistoryProbeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TnOamTrProbeHistoryProbeIndex_Type.__name__ = "Unsigned32"
_TnOamTrProbeHistoryProbeIndex_Object = MibTableColumn
tnOamTrProbeHistoryProbeIndex = _TnOamTrProbeHistoryProbeIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 5, 1, 3),
    _TnOamTrProbeHistoryProbeIndex_Type()
)
tnOamTrProbeHistoryProbeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOamTrProbeHistoryProbeIndex.setStatus("current")
_TnOamTrProbeHistoryIpAddr_Type = IpAddress
_TnOamTrProbeHistoryIpAddr_Object = MibTableColumn
tnOamTrProbeHistoryIpAddr = _TnOamTrProbeHistoryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 5, 1, 4),
    _TnOamTrProbeHistoryIpAddr_Type()
)
tnOamTrProbeHistoryIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamTrProbeHistoryIpAddr.setStatus("obsolete")
_TnOamTrProbeHistoryResponse_Type = Unsigned32
_TnOamTrProbeHistoryResponse_Object = MibTableColumn
tnOamTrProbeHistoryResponse = _TnOamTrProbeHistoryResponse_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 5, 1, 5),
    _TnOamTrProbeHistoryResponse_Type()
)
tnOamTrProbeHistoryResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamTrProbeHistoryResponse.setStatus("current")
if mibBuilder.loadTexts:
    tnOamTrProbeHistoryResponse.setUnits("microseconds")
_TnOamTrProbeHistoryOneWayTime_Type = Integer32
_TnOamTrProbeHistoryOneWayTime_Object = MibTableColumn
tnOamTrProbeHistoryOneWayTime = _TnOamTrProbeHistoryOneWayTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 5, 1, 6),
    _TnOamTrProbeHistoryOneWayTime_Type()
)
tnOamTrProbeHistoryOneWayTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamTrProbeHistoryOneWayTime.setStatus("current")
if mibBuilder.loadTexts:
    tnOamTrProbeHistoryOneWayTime.setUnits("microseconds")
_TnOamTrProbeHistoryStatus_Type = TmnxOamResponseStatus
_TnOamTrProbeHistoryStatus_Object = MibTableColumn
tnOamTrProbeHistoryStatus = _TnOamTrProbeHistoryStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 5, 1, 7),
    _TnOamTrProbeHistoryStatus_Type()
)
tnOamTrProbeHistoryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamTrProbeHistoryStatus.setStatus("current")
_TnOamTrProbeHistoryLastRC_Type = Integer32
_TnOamTrProbeHistoryLastRC_Object = MibTableColumn
tnOamTrProbeHistoryLastRC = _TnOamTrProbeHistoryLastRC_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 5, 1, 8),
    _TnOamTrProbeHistoryLastRC_Type()
)
tnOamTrProbeHistoryLastRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamTrProbeHistoryLastRC.setStatus("current")
_TnOamTrProbeHistoryTime_Type = DateAndTime
_TnOamTrProbeHistoryTime_Object = MibTableColumn
tnOamTrProbeHistoryTime = _TnOamTrProbeHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 5, 1, 9),
    _TnOamTrProbeHistoryTime_Type()
)
tnOamTrProbeHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamTrProbeHistoryTime.setStatus("current")
_TnOamTrProbeHistoryResponsePlane_Type = TmnxOamTestResponsePlane
_TnOamTrProbeHistoryResponsePlane_Object = MibTableColumn
tnOamTrProbeHistoryResponsePlane = _TnOamTrProbeHistoryResponsePlane_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 5, 1, 10),
    _TnOamTrProbeHistoryResponsePlane_Type()
)
tnOamTrProbeHistoryResponsePlane.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamTrProbeHistoryResponsePlane.setStatus("current")
_TnOamTrProbeHistoryAddressType_Type = TmnxOamAddressType
_TnOamTrProbeHistoryAddressType_Object = MibTableColumn
tnOamTrProbeHistoryAddressType = _TnOamTrProbeHistoryAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 5, 1, 11),
    _TnOamTrProbeHistoryAddressType_Type()
)
tnOamTrProbeHistoryAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamTrProbeHistoryAddressType.setStatus("current")
_TnOamTrProbeHistorySapId_Type = TmnxStrSapId
_TnOamTrProbeHistorySapId_Object = MibTableColumn
tnOamTrProbeHistorySapId = _TnOamTrProbeHistorySapId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 5, 1, 12),
    _TnOamTrProbeHistorySapId_Type()
)
tnOamTrProbeHistorySapId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamTrProbeHistorySapId.setStatus("current")
_TnOamTrProbeHistoryVersion_Type = Unsigned32
_TnOamTrProbeHistoryVersion_Object = MibTableColumn
tnOamTrProbeHistoryVersion = _TnOamTrProbeHistoryVersion_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 5, 1, 14),
    _TnOamTrProbeHistoryVersion_Type()
)
tnOamTrProbeHistoryVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamTrProbeHistoryVersion.setStatus("current")
_TnOamTrProbeHistoryRouterID_Type = RouterID
_TnOamTrProbeHistoryRouterID_Object = MibTableColumn
tnOamTrProbeHistoryRouterID = _TnOamTrProbeHistoryRouterID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 5, 1, 15),
    _TnOamTrProbeHistoryRouterID_Type()
)
tnOamTrProbeHistoryRouterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamTrProbeHistoryRouterID.setStatus("current")
_TnOamTrProbeHistoryIfIndex_Type = InterfaceIndexOrZero
_TnOamTrProbeHistoryIfIndex_Object = MibTableColumn
tnOamTrProbeHistoryIfIndex = _TnOamTrProbeHistoryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 5, 1, 16),
    _TnOamTrProbeHistoryIfIndex_Type()
)
tnOamTrProbeHistoryIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamTrProbeHistoryIfIndex.setStatus("current")
_TnOamTrProbeHistoryDataLen_Type = Unsigned32
_TnOamTrProbeHistoryDataLen_Object = MibTableColumn
tnOamTrProbeHistoryDataLen = _TnOamTrProbeHistoryDataLen_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 5, 1, 17),
    _TnOamTrProbeHistoryDataLen_Type()
)
tnOamTrProbeHistoryDataLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamTrProbeHistoryDataLen.setStatus("current")
if mibBuilder.loadTexts:
    tnOamTrProbeHistoryDataLen.setUnits("octets")
_TnOamTrProbeHistorySize_Type = Unsigned32
_TnOamTrProbeHistorySize_Object = MibTableColumn
tnOamTrProbeHistorySize = _TnOamTrProbeHistorySize_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 5, 1, 18),
    _TnOamTrProbeHistorySize_Type()
)
tnOamTrProbeHistorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamTrProbeHistorySize.setStatus("current")
if mibBuilder.loadTexts:
    tnOamTrProbeHistorySize.setUnits("octets")
_TnOamTrProbeHistoryInOneWayTime_Type = Integer32
_TnOamTrProbeHistoryInOneWayTime_Object = MibTableColumn
tnOamTrProbeHistoryInOneWayTime = _TnOamTrProbeHistoryInOneWayTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 5, 1, 19),
    _TnOamTrProbeHistoryInOneWayTime_Type()
)
tnOamTrProbeHistoryInOneWayTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamTrProbeHistoryInOneWayTime.setStatus("current")
if mibBuilder.loadTexts:
    tnOamTrProbeHistoryInOneWayTime.setUnits("microseconds")
_TnOamTrProbeHistoryAddrType_Type = InetAddressType
_TnOamTrProbeHistoryAddrType_Object = MibTableColumn
tnOamTrProbeHistoryAddrType = _TnOamTrProbeHistoryAddrType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 5, 1, 20),
    _TnOamTrProbeHistoryAddrType_Type()
)
tnOamTrProbeHistoryAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamTrProbeHistoryAddrType.setStatus("current")


class _TnOamTrProbeHistoryAddress_Type(InetAddress):
    """Custom type tnOamTrProbeHistoryAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TnOamTrProbeHistoryAddress_Type.__name__ = "InetAddress"
_TnOamTrProbeHistoryAddress_Object = MibTableColumn
tnOamTrProbeHistoryAddress = _TnOamTrProbeHistoryAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 5, 1, 21),
    _TnOamTrProbeHistoryAddress_Type()
)
tnOamTrProbeHistoryAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamTrProbeHistoryAddress.setStatus("current")
_TnOamTrProbeHistorySrcGlobalId_Type = TmnxMplsTpGlobalID
_TnOamTrProbeHistorySrcGlobalId_Object = MibTableColumn
tnOamTrProbeHistorySrcGlobalId = _TnOamTrProbeHistorySrcGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 5, 1, 22),
    _TnOamTrProbeHistorySrcGlobalId_Type()
)
tnOamTrProbeHistorySrcGlobalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamTrProbeHistorySrcGlobalId.setStatus("current")
_TnOamTrProbeHistorySrcNodeId_Type = TmnxMplsTpNodeID
_TnOamTrProbeHistorySrcNodeId_Object = MibTableColumn
tnOamTrProbeHistorySrcNodeId = _TnOamTrProbeHistorySrcNodeId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 5, 1, 23),
    _TnOamTrProbeHistorySrcNodeId_Type()
)
tnOamTrProbeHistorySrcNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamTrProbeHistorySrcNodeId.setStatus("current")
_TnOamLspTrCtlTable_Object = MibTable
tnOamLspTrCtlTable = _TnOamLspTrCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 9)
)
if mibBuilder.loadTexts:
    tnOamLspTrCtlTable.setStatus("current")
_TnOamLspTrCtlEntry_Object = MibTableRow
tnOamLspTrCtlEntry = _TnOamLspTrCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 9, 1)
)
tnOamLspTrCtlEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-OAM-TEST-MIB", "tnOamTrCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tnOamLspTrCtlEntry.setStatus("current")


class _TnOamLspTrCtlVRtrID_Type(TmnxVRtrID):
    """Custom type tnOamLspTrCtlVRtrID based on TmnxVRtrID"""
    defaultValue = 1


_TnOamLspTrCtlVRtrID_Type.__name__ = "TmnxVRtrID"
_TnOamLspTrCtlVRtrID_Object = MibTableColumn
tnOamLspTrCtlVRtrID = _TnOamLspTrCtlVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 9, 1, 1),
    _TnOamLspTrCtlVRtrID_Type()
)
tnOamLspTrCtlVRtrID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamLspTrCtlVRtrID.setStatus("obsolete")


class _TnOamLspTrCtlLspName_Type(TNamedItemOrEmpty):
    """Custom type tnOamLspTrCtlLspName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TnOamLspTrCtlLspName_Type.__name__ = "TNamedItemOrEmpty"
_TnOamLspTrCtlLspName_Object = MibTableColumn
tnOamLspTrCtlLspName = _TnOamLspTrCtlLspName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 9, 1, 2),
    _TnOamLspTrCtlLspName_Type()
)
tnOamLspTrCtlLspName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamLspTrCtlLspName.setStatus("current")


class _TnOamLspTrCtlPathName_Type(TNamedItemOrEmpty):
    """Custom type tnOamLspTrCtlPathName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TnOamLspTrCtlPathName_Type.__name__ = "TNamedItemOrEmpty"
_TnOamLspTrCtlPathName_Object = MibTableColumn
tnOamLspTrCtlPathName = _TnOamLspTrCtlPathName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 9, 1, 3),
    _TnOamLspTrCtlPathName_Type()
)
tnOamLspTrCtlPathName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamLspTrCtlPathName.setStatus("current")


class _TnOamLspTrCtlLdpIpPrefix_Type(IpAddress):
    """Custom type tnOamLspTrCtlLdpIpPrefix based on IpAddress"""
    defaultHexValue = "00000000"


_TnOamLspTrCtlLdpIpPrefix_Type.__name__ = "IpAddress"
_TnOamLspTrCtlLdpIpPrefix_Object = MibTableColumn
tnOamLspTrCtlLdpIpPrefix = _TnOamLspTrCtlLdpIpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 9, 1, 4),
    _TnOamLspTrCtlLdpIpPrefix_Type()
)
tnOamLspTrCtlLdpIpPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamLspTrCtlLdpIpPrefix.setStatus("obsolete")


class _TnOamLspTrCtlLdpIpPrefixLen_Type(IpAddressPrefixLength):
    """Custom type tnOamLspTrCtlLdpIpPrefixLen based on IpAddressPrefixLength"""
    defaultValue = 32


_TnOamLspTrCtlLdpIpPrefixLen_Type.__name__ = "IpAddressPrefixLength"
_TnOamLspTrCtlLdpIpPrefixLen_Object = MibTableColumn
tnOamLspTrCtlLdpIpPrefixLen = _TnOamLspTrCtlLdpIpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 9, 1, 5),
    _TnOamLspTrCtlLdpIpPrefixLen_Type()
)
tnOamLspTrCtlLdpIpPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamLspTrCtlLdpIpPrefixLen.setStatus("obsolete")


class _TnOamLspTrCtlLdpPrefixType_Type(InetAddressType):
    """Custom type tnOamLspTrCtlLdpPrefixType based on InetAddressType"""
    defaultValue = 0


_TnOamLspTrCtlLdpPrefixType_Type.__name__ = "InetAddressType"
_TnOamLspTrCtlLdpPrefixType_Object = MibTableColumn
tnOamLspTrCtlLdpPrefixType = _TnOamLspTrCtlLdpPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 9, 1, 6),
    _TnOamLspTrCtlLdpPrefixType_Type()
)
tnOamLspTrCtlLdpPrefixType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamLspTrCtlLdpPrefixType.setStatus("current")


class _TnOamLspTrCtlLdpPrefix_Type(InetAddress):
    """Custom type tnOamLspTrCtlLdpPrefix based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TnOamLspTrCtlLdpPrefix_Type.__name__ = "InetAddress"
_TnOamLspTrCtlLdpPrefix_Object = MibTableColumn
tnOamLspTrCtlLdpPrefix = _TnOamLspTrCtlLdpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 9, 1, 7),
    _TnOamLspTrCtlLdpPrefix_Type()
)
tnOamLspTrCtlLdpPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamLspTrCtlLdpPrefix.setStatus("current")


class _TnOamLspTrCtlLdpPrefixLen_Type(InetAddressPrefixLength):
    """Custom type tnOamLspTrCtlLdpPrefixLen based on InetAddressPrefixLength"""
    defaultValue = 32


_TnOamLspTrCtlLdpPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_TnOamLspTrCtlLdpPrefixLen_Object = MibTableColumn
tnOamLspTrCtlLdpPrefixLen = _TnOamLspTrCtlLdpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 9, 1, 8),
    _TnOamLspTrCtlLdpPrefixLen_Type()
)
tnOamLspTrCtlLdpPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamLspTrCtlLdpPrefixLen.setStatus("current")


class _TnOamLspTrCtlPathDestType_Type(InetAddressType):
    """Custom type tnOamLspTrCtlPathDestType based on InetAddressType"""
    defaultValue = 0


_TnOamLspTrCtlPathDestType_Type.__name__ = "InetAddressType"
_TnOamLspTrCtlPathDestType_Object = MibTableColumn
tnOamLspTrCtlPathDestType = _TnOamLspTrCtlPathDestType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 9, 1, 9),
    _TnOamLspTrCtlPathDestType_Type()
)
tnOamLspTrCtlPathDestType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamLspTrCtlPathDestType.setStatus("current")


class _TnOamLspTrCtlPathDest_Type(InetAddress):
    """Custom type tnOamLspTrCtlPathDest based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TnOamLspTrCtlPathDest_Type.__name__ = "InetAddress"
_TnOamLspTrCtlPathDest_Object = MibTableColumn
tnOamLspTrCtlPathDest = _TnOamLspTrCtlPathDest_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 9, 1, 10),
    _TnOamLspTrCtlPathDest_Type()
)
tnOamLspTrCtlPathDest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamLspTrCtlPathDest.setStatus("current")


class _TnOamLspTrCtlNhIntfName_Type(TNamedItemOrEmpty):
    """Custom type tnOamLspTrCtlNhIntfName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TnOamLspTrCtlNhIntfName_Type.__name__ = "TNamedItemOrEmpty"
_TnOamLspTrCtlNhIntfName_Object = MibTableColumn
tnOamLspTrCtlNhIntfName = _TnOamLspTrCtlNhIntfName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 9, 1, 11),
    _TnOamLspTrCtlNhIntfName_Type()
)
tnOamLspTrCtlNhIntfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamLspTrCtlNhIntfName.setStatus("current")


class _TnOamLspTrCtlNhAddressType_Type(InetAddressType):
    """Custom type tnOamLspTrCtlNhAddressType based on InetAddressType"""
    defaultValue = 0


_TnOamLspTrCtlNhAddressType_Type.__name__ = "InetAddressType"
_TnOamLspTrCtlNhAddressType_Object = MibTableColumn
tnOamLspTrCtlNhAddressType = _TnOamLspTrCtlNhAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 9, 1, 12),
    _TnOamLspTrCtlNhAddressType_Type()
)
tnOamLspTrCtlNhAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamLspTrCtlNhAddressType.setStatus("current")


class _TnOamLspTrCtlNhAddress_Type(InetAddress):
    """Custom type tnOamLspTrCtlNhAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TnOamLspTrCtlNhAddress_Type.__name__ = "InetAddress"
_TnOamLspTrCtlNhAddress_Object = MibTableColumn
tnOamLspTrCtlNhAddress = _TnOamLspTrCtlNhAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 9, 1, 13),
    _TnOamLspTrCtlNhAddress_Type()
)
tnOamLspTrCtlNhAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamLspTrCtlNhAddress.setStatus("current")


class _TnOamLspTrCtlDownstreamMapTlv_Type(TmnxOamMplsEchoDownMapTlvOrNone):
    """Custom type tnOamLspTrCtlDownstreamMapTlv based on TmnxOamMplsEchoDownMapTlvOrNone"""
    defaultValue = 1


_TnOamLspTrCtlDownstreamMapTlv_Type.__name__ = "TmnxOamMplsEchoDownMapTlvOrNone"
_TnOamLspTrCtlDownstreamMapTlv_Object = MibTableColumn
tnOamLspTrCtlDownstreamMapTlv = _TnOamLspTrCtlDownstreamMapTlv_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 9, 1, 14),
    _TnOamLspTrCtlDownstreamMapTlv_Type()
)
tnOamLspTrCtlDownstreamMapTlv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamLspTrCtlDownstreamMapTlv.setStatus("current")


class _TnOamLspTrCtlTestSubMode_Type(TmnxOamLspTestSubMode):
    """Custom type tnOamLspTrCtlTestSubMode based on TmnxOamLspTestSubMode"""
    defaultValue = 1


_TnOamLspTrCtlTestSubMode_Type.__name__ = "TmnxOamLspTestSubMode"
_TnOamLspTrCtlTestSubMode_Object = MibTableColumn
tnOamLspTrCtlTestSubMode = _TnOamLspTrCtlTestSubMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 9, 1, 15),
    _TnOamLspTrCtlTestSubMode_Type()
)
tnOamLspTrCtlTestSubMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamLspTrCtlTestSubMode.setStatus("current")


class _TnOamLspTrCtlMplsTpPathType_Type(TmnxOamMplsTpPathType):
    """Custom type tnOamLspTrCtlMplsTpPathType based on TmnxOamMplsTpPathType"""
    defaultValue = 3


_TnOamLspTrCtlMplsTpPathType_Type.__name__ = "TmnxOamMplsTpPathType"
_TnOamLspTrCtlMplsTpPathType_Object = MibTableColumn
tnOamLspTrCtlMplsTpPathType = _TnOamLspTrCtlMplsTpPathType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 9, 1, 16),
    _TnOamLspTrCtlMplsTpPathType_Type()
)
tnOamLspTrCtlMplsTpPathType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamLspTrCtlMplsTpPathType.setStatus("current")


class _TnOamLspTrCtlAssocChannel_Type(TmnxOamLspAssocChannel):
    """Custom type tnOamLspTrCtlAssocChannel based on TmnxOamLspAssocChannel"""
    defaultValue = 1


_TnOamLspTrCtlAssocChannel_Type.__name__ = "TmnxOamLspAssocChannel"
_TnOamLspTrCtlAssocChannel_Object = MibTableColumn
tnOamLspTrCtlAssocChannel = _TnOamLspTrCtlAssocChannel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 9, 1, 17),
    _TnOamLspTrCtlAssocChannel_Type()
)
tnOamLspTrCtlAssocChannel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamLspTrCtlAssocChannel.setStatus("current")


class _TnOamLspTrCtlForce_Type(TruthValue):
    """Custom type tnOamLspTrCtlForce based on TruthValue"""
    defaultValue = 2


_TnOamLspTrCtlForce_Type.__name__ = "TruthValue"
_TnOamLspTrCtlForce_Object = MibTableColumn
tnOamLspTrCtlForce = _TnOamLspTrCtlForce_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 9, 1, 18),
    _TnOamLspTrCtlForce_Type()
)
tnOamLspTrCtlForce.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamLspTrCtlForce.setStatus("current")
_TnOamLspTrMapTable_Object = MibTable
tnOamLspTrMapTable = _TnOamLspTrMapTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 10)
)
if mibBuilder.loadTexts:
    tnOamLspTrMapTable.setStatus("current")
_TnOamLspTrMapEntry_Object = MibTableRow
tnOamLspTrMapEntry = _TnOamLspTrMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 10, 1)
)
tnOamLspTrMapEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-OAM-TEST-MIB", "tnOamTrCtlTestIndex"),
    (0, "TN-OAM-TEST-MIB", "tnOamTrResultsTestRunIndex"),
    (0, "TN-OAM-TEST-MIB", "tnOamTrProbeHistoryIndex"),
    (0, "TN-OAM-TEST-MIB", "tnOamTrProbeHistoryHopIndex"),
    (0, "TN-OAM-TEST-MIB", "tnOamTrProbeHistoryProbeIndex"),
    (0, "TN-OAM-TEST-MIB", "tnOamLspTrMapIndex"),
)
if mibBuilder.loadTexts:
    tnOamLspTrMapEntry.setStatus("current")


class _TnOamLspTrMapIndex_Type(Unsigned32):
    """Custom type tnOamLspTrMapIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TnOamLspTrMapIndex_Type.__name__ = "Unsigned32"
_TnOamLspTrMapIndex_Object = MibTableColumn
tnOamLspTrMapIndex = _TnOamLspTrMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 10, 1, 1),
    _TnOamLspTrMapIndex_Type()
)
tnOamLspTrMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOamLspTrMapIndex.setStatus("current")
_TnOamLspTrMapDSIPv4Addr_Type = IpAddress
_TnOamLspTrMapDSIPv4Addr_Object = MibTableColumn
tnOamLspTrMapDSIPv4Addr = _TnOamLspTrMapDSIPv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 10, 1, 2),
    _TnOamLspTrMapDSIPv4Addr_Type()
)
tnOamLspTrMapDSIPv4Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamLspTrMapDSIPv4Addr.setStatus("current")
_TnOamLspTrMapAddrType_Type = TmnxOamAddressType
_TnOamLspTrMapAddrType_Object = MibTableColumn
tnOamLspTrMapAddrType = _TnOamLspTrMapAddrType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 10, 1, 3),
    _TnOamLspTrMapAddrType_Type()
)
tnOamLspTrMapAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamLspTrMapAddrType.setStatus("current")
_TnOamLspTrMapDSIfAddr_Type = Unsigned32
_TnOamLspTrMapDSIfAddr_Object = MibTableColumn
tnOamLspTrMapDSIfAddr = _TnOamLspTrMapDSIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 10, 1, 4),
    _TnOamLspTrMapDSIfAddr_Type()
)
tnOamLspTrMapDSIfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamLspTrMapDSIfAddr.setStatus("current")


class _TnOamLspTrMapMTU_Type(Unsigned32):
    """Custom type tnOamLspTrMapMTU based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TnOamLspTrMapMTU_Type.__name__ = "Unsigned32"
_TnOamLspTrMapMTU_Object = MibTableColumn
tnOamLspTrMapMTU = _TnOamLspTrMapMTU_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 10, 1, 5),
    _TnOamLspTrMapMTU_Type()
)
tnOamLspTrMapMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamLspTrMapMTU.setStatus("current")


class _TnOamLspTrMapDSIndex_Type(Unsigned32):
    """Custom type tnOamLspTrMapDSIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnOamLspTrMapDSIndex_Type.__name__ = "Unsigned32"
_TnOamLspTrMapDSIndex_Object = MibTableColumn
tnOamLspTrMapDSIndex = _TnOamLspTrMapDSIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 10, 1, 6),
    _TnOamLspTrMapDSIndex_Type()
)
tnOamLspTrMapDSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamLspTrMapDSIndex.setStatus("obsolete")
_TnOamVccvTrCtlTable_Object = MibTable
tnOamVccvTrCtlTable = _TnOamVccvTrCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 26)
)
if mibBuilder.loadTexts:
    tnOamVccvTrCtlTable.setStatus("current")
_TnOamVccvTrCtlEntry_Object = MibTableRow
tnOamVccvTrCtlEntry = _TnOamVccvTrCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 26, 1)
)
tnOamVccvTrCtlEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-OAM-TEST-MIB", "tnOamTrCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tnOamVccvTrCtlEntry.setStatus("current")


class _TnOamVccvTrCtlSdpIdVcId_Type(SdpBindId):
    """Custom type tnOamVccvTrCtlSdpIdVcId based on SdpBindId"""
    defaultHexValue = "0000000000000000"


_TnOamVccvTrCtlSdpIdVcId_Type.__name__ = "SdpBindId"
_TnOamVccvTrCtlSdpIdVcId_Object = MibTableColumn
tnOamVccvTrCtlSdpIdVcId = _TnOamVccvTrCtlSdpIdVcId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 26, 1, 1),
    _TnOamVccvTrCtlSdpIdVcId_Type()
)
tnOamVccvTrCtlSdpIdVcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamVccvTrCtlSdpIdVcId.setStatus("current")


class _TnOamVccvTrCtlReplyMode_Type(Integer32):
    """Custom type tnOamVccvTrCtlReplyMode based on Integer32"""
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


_TnOamVccvTrCtlReplyMode_Type.__name__ = "Integer32"
_TnOamVccvTrCtlReplyMode_Object = MibTableColumn
tnOamVccvTrCtlReplyMode = _TnOamVccvTrCtlReplyMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 26, 1, 2),
    _TnOamVccvTrCtlReplyMode_Type()
)
tnOamVccvTrCtlReplyMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamVccvTrCtlReplyMode.setStatus("current")


class _TnOamVccvTrCtlSpokeSdpId_Type(TmnxSpokeSdpIdOrZero):
    """Custom type tnOamVccvTrCtlSpokeSdpId based on TmnxSpokeSdpIdOrZero"""
    defaultValue = 0


_TnOamVccvTrCtlSpokeSdpId_Type.__name__ = "TmnxSpokeSdpIdOrZero"
_TnOamVccvTrCtlSpokeSdpId_Object = MibTableColumn
tnOamVccvTrCtlSpokeSdpId = _TnOamVccvTrCtlSpokeSdpId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 26, 1, 3),
    _TnOamVccvTrCtlSpokeSdpId_Type()
)
tnOamVccvTrCtlSpokeSdpId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamVccvTrCtlSpokeSdpId.setStatus("current")


class _TnOamVccvTrCtlSaiiGlobalId_Type(TmnxPwGlobalIdOrZero):
    """Custom type tnOamVccvTrCtlSaiiGlobalId based on TmnxPwGlobalIdOrZero"""
    defaultValue = 0


_TnOamVccvTrCtlSaiiGlobalId_Type.__name__ = "TmnxPwGlobalIdOrZero"
_TnOamVccvTrCtlSaiiGlobalId_Object = MibTableColumn
tnOamVccvTrCtlSaiiGlobalId = _TnOamVccvTrCtlSaiiGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 26, 1, 4),
    _TnOamVccvTrCtlSaiiGlobalId_Type()
)
tnOamVccvTrCtlSaiiGlobalId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamVccvTrCtlSaiiGlobalId.setStatus("current")


class _TnOamVccvTrCtlSaiiPrefix_Type(Unsigned32):
    """Custom type tnOamVccvTrCtlSaiiPrefix based on Unsigned32"""
    defaultValue = 0


_TnOamVccvTrCtlSaiiPrefix_Type.__name__ = "Unsigned32"
_TnOamVccvTrCtlSaiiPrefix_Object = MibTableColumn
tnOamVccvTrCtlSaiiPrefix = _TnOamVccvTrCtlSaiiPrefix_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 26, 1, 5),
    _TnOamVccvTrCtlSaiiPrefix_Type()
)
tnOamVccvTrCtlSaiiPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamVccvTrCtlSaiiPrefix.setStatus("current")


class _TnOamVccvTrCtlSaiiAcId_Type(Unsigned32):
    """Custom type tnOamVccvTrCtlSaiiAcId based on Unsigned32"""
    defaultValue = 0


_TnOamVccvTrCtlSaiiAcId_Type.__name__ = "Unsigned32"
_TnOamVccvTrCtlSaiiAcId_Object = MibTableColumn
tnOamVccvTrCtlSaiiAcId = _TnOamVccvTrCtlSaiiAcId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 26, 1, 6),
    _TnOamVccvTrCtlSaiiAcId_Type()
)
tnOamVccvTrCtlSaiiAcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamVccvTrCtlSaiiAcId.setStatus("current")


class _TnOamVccvTrCtlTaiiGlobalId_Type(TmnxPwGlobalIdOrZero):
    """Custom type tnOamVccvTrCtlTaiiGlobalId based on TmnxPwGlobalIdOrZero"""
    defaultValue = 0


_TnOamVccvTrCtlTaiiGlobalId_Type.__name__ = "TmnxPwGlobalIdOrZero"
_TnOamVccvTrCtlTaiiGlobalId_Object = MibTableColumn
tnOamVccvTrCtlTaiiGlobalId = _TnOamVccvTrCtlTaiiGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 26, 1, 7),
    _TnOamVccvTrCtlTaiiGlobalId_Type()
)
tnOamVccvTrCtlTaiiGlobalId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamVccvTrCtlTaiiGlobalId.setStatus("current")


class _TnOamVccvTrCtlTaiiPrefix_Type(Unsigned32):
    """Custom type tnOamVccvTrCtlTaiiPrefix based on Unsigned32"""
    defaultValue = 0


_TnOamVccvTrCtlTaiiPrefix_Type.__name__ = "Unsigned32"
_TnOamVccvTrCtlTaiiPrefix_Object = MibTableColumn
tnOamVccvTrCtlTaiiPrefix = _TnOamVccvTrCtlTaiiPrefix_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 26, 1, 8),
    _TnOamVccvTrCtlTaiiPrefix_Type()
)
tnOamVccvTrCtlTaiiPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamVccvTrCtlTaiiPrefix.setStatus("current")


class _TnOamVccvTrCtlTaiiAcId_Type(Unsigned32):
    """Custom type tnOamVccvTrCtlTaiiAcId based on Unsigned32"""
    defaultValue = 0


_TnOamVccvTrCtlTaiiAcId_Type.__name__ = "Unsigned32"
_TnOamVccvTrCtlTaiiAcId_Object = MibTableColumn
tnOamVccvTrCtlTaiiAcId = _TnOamVccvTrCtlTaiiAcId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 26, 1, 9),
    _TnOamVccvTrCtlTaiiAcId_Type()
)
tnOamVccvTrCtlTaiiAcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamVccvTrCtlTaiiAcId.setStatus("current")


class _TnOamVccvTrCtlTestSubMode_Type(TmnxOamVccvTestSubMode):
    """Custom type tnOamVccvTrCtlTestSubMode based on TmnxOamVccvTestSubMode"""
    defaultValue = 1


_TnOamVccvTrCtlTestSubMode_Type.__name__ = "TmnxOamVccvTestSubMode"
_TnOamVccvTrCtlTestSubMode_Object = MibTableColumn
tnOamVccvTrCtlTestSubMode = _TnOamVccvTrCtlTestSubMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 26, 1, 10),
    _TnOamVccvTrCtlTestSubMode_Type()
)
tnOamVccvTrCtlTestSubMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamVccvTrCtlTestSubMode.setStatus("current")


class _TnOamVccvTrCtlAssocChannel_Type(TmnxOamVccvAssocChannel):
    """Custom type tnOamVccvTrCtlAssocChannel based on TmnxOamVccvAssocChannel"""
    defaultValue = 1


_TnOamVccvTrCtlAssocChannel_Type.__name__ = "TmnxOamVccvAssocChannel"
_TnOamVccvTrCtlAssocChannel_Object = MibTableColumn
tnOamVccvTrCtlAssocChannel = _TnOamVccvTrCtlAssocChannel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 26, 1, 11),
    _TnOamVccvTrCtlAssocChannel_Type()
)
tnOamVccvTrCtlAssocChannel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamVccvTrCtlAssocChannel.setStatus("current")
_TnOamVccvTrNextPwSegmentTable_Object = MibTable
tnOamVccvTrNextPwSegmentTable = _TnOamVccvTrNextPwSegmentTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 27)
)
if mibBuilder.loadTexts:
    tnOamVccvTrNextPwSegmentTable.setStatus("current")
_TnOamVccvTrNextPwSegmentEntry_Object = MibTableRow
tnOamVccvTrNextPwSegmentEntry = _TnOamVccvTrNextPwSegmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 27, 1)
)
tnOamVccvTrNextPwSegmentEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-OAM-TEST-MIB", "tnOamTrCtlTestIndex"),
    (0, "TN-OAM-TEST-MIB", "tnOamTrResultsTestRunIndex"),
    (0, "TN-OAM-TEST-MIB", "tnOamTrProbeHistoryIndex"),
    (0, "TN-OAM-TEST-MIB", "tnOamTrProbeHistoryHopIndex"),
    (0, "TN-OAM-TEST-MIB", "tnOamTrProbeHistoryProbeIndex"),
)
if mibBuilder.loadTexts:
    tnOamVccvTrNextPwSegmentEntry.setStatus("current")
_TnOamVccvTrNextPwID_Type = TmnxVcIdOrNone
_TnOamVccvTrNextPwID_Object = MibTableColumn
tnOamVccvTrNextPwID = _TnOamVccvTrNextPwID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 27, 1, 1),
    _TnOamVccvTrNextPwID_Type()
)
tnOamVccvTrNextPwID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamVccvTrNextPwID.setStatus("current")
_TnOamVccvTrNextPwType_Type = SdpBindVcType
_TnOamVccvTrNextPwType_Object = MibTableColumn
tnOamVccvTrNextPwType = _TnOamVccvTrNextPwType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 27, 1, 2),
    _TnOamVccvTrNextPwType_Type()
)
tnOamVccvTrNextPwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamVccvTrNextPwType.setStatus("current")
_TnOamVccvTrNextSenderAddrType_Type = InetAddressType
_TnOamVccvTrNextSenderAddrType_Object = MibTableColumn
tnOamVccvTrNextSenderAddrType = _TnOamVccvTrNextSenderAddrType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 27, 1, 3),
    _TnOamVccvTrNextSenderAddrType_Type()
)
tnOamVccvTrNextSenderAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamVccvTrNextSenderAddrType.setStatus("current")


class _TnOamVccvTrNextSenderAddr_Type(InetAddress):
    """Custom type tnOamVccvTrNextSenderAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TnOamVccvTrNextSenderAddr_Type.__name__ = "InetAddress"
_TnOamVccvTrNextSenderAddr_Object = MibTableColumn
tnOamVccvTrNextSenderAddr = _TnOamVccvTrNextSenderAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 27, 1, 4),
    _TnOamVccvTrNextSenderAddr_Type()
)
tnOamVccvTrNextSenderAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamVccvTrNextSenderAddr.setStatus("current")
_TnOamVccvTrNextRemoteAddrType_Type = InetAddressType
_TnOamVccvTrNextRemoteAddrType_Object = MibTableColumn
tnOamVccvTrNextRemoteAddrType = _TnOamVccvTrNextRemoteAddrType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 27, 1, 5),
    _TnOamVccvTrNextRemoteAddrType_Type()
)
tnOamVccvTrNextRemoteAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamVccvTrNextRemoteAddrType.setStatus("current")


class _TnOamVccvTrNextRemoteAddr_Type(InetAddress):
    """Custom type tnOamVccvTrNextRemoteAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TnOamVccvTrNextRemoteAddr_Type.__name__ = "InetAddress"
_TnOamVccvTrNextRemoteAddr_Object = MibTableColumn
tnOamVccvTrNextRemoteAddr = _TnOamVccvTrNextRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 27, 1, 6),
    _TnOamVccvTrNextRemoteAddr_Type()
)
tnOamVccvTrNextRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamVccvTrNextRemoteAddr.setStatus("current")
_TnOamVccvTrNextSaiiGlobalId_Type = TmnxPwGlobalIdOrZero
_TnOamVccvTrNextSaiiGlobalId_Object = MibTableColumn
tnOamVccvTrNextSaiiGlobalId = _TnOamVccvTrNextSaiiGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 27, 1, 7),
    _TnOamVccvTrNextSaiiGlobalId_Type()
)
tnOamVccvTrNextSaiiGlobalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamVccvTrNextSaiiGlobalId.setStatus("current")
_TnOamVccvTrNextSaiiPrefix_Type = Unsigned32
_TnOamVccvTrNextSaiiPrefix_Object = MibTableColumn
tnOamVccvTrNextSaiiPrefix = _TnOamVccvTrNextSaiiPrefix_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 27, 1, 8),
    _TnOamVccvTrNextSaiiPrefix_Type()
)
tnOamVccvTrNextSaiiPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamVccvTrNextSaiiPrefix.setStatus("current")
_TnOamVccvTrNextSaiiAcId_Type = Unsigned32
_TnOamVccvTrNextSaiiAcId_Object = MibTableColumn
tnOamVccvTrNextSaiiAcId = _TnOamVccvTrNextSaiiAcId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 27, 1, 9),
    _TnOamVccvTrNextSaiiAcId_Type()
)
tnOamVccvTrNextSaiiAcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamVccvTrNextSaiiAcId.setStatus("current")
_TnOamVccvTrNextTaiiGlobalId_Type = TmnxPwGlobalIdOrZero
_TnOamVccvTrNextTaiiGlobalId_Object = MibTableColumn
tnOamVccvTrNextTaiiGlobalId = _TnOamVccvTrNextTaiiGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 27, 1, 10),
    _TnOamVccvTrNextTaiiGlobalId_Type()
)
tnOamVccvTrNextTaiiGlobalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamVccvTrNextTaiiGlobalId.setStatus("current")
_TnOamVccvTrNextTaiiPrefix_Type = Unsigned32
_TnOamVccvTrNextTaiiPrefix_Object = MibTableColumn
tnOamVccvTrNextTaiiPrefix = _TnOamVccvTrNextTaiiPrefix_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 27, 1, 11),
    _TnOamVccvTrNextTaiiPrefix_Type()
)
tnOamVccvTrNextTaiiPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamVccvTrNextTaiiPrefix.setStatus("current")
_TnOamVccvTrNextTaiiAcId_Type = Unsigned32
_TnOamVccvTrNextTaiiAcId_Object = MibTableColumn
tnOamVccvTrNextTaiiAcId = _TnOamVccvTrNextTaiiAcId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 27, 1, 12),
    _TnOamVccvTrNextTaiiAcId_Type()
)
tnOamVccvTrNextTaiiAcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamVccvTrNextTaiiAcId.setStatus("current")


class _TnOamVccvTrNextTpAgi_Type(OctetString):
    """Custom type tnOamVccvTrNextTpAgi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_TnOamVccvTrNextTpAgi_Type.__name__ = "OctetString"
_TnOamVccvTrNextTpAgi_Object = MibTableColumn
tnOamVccvTrNextTpAgi = _TnOamVccvTrNextTpAgi_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 27, 1, 13),
    _TnOamVccvTrNextTpAgi_Type()
)
tnOamVccvTrNextTpAgi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamVccvTrNextTpAgi.setStatus("current")
_TnOamVccvTrNextTpSaiiGlobalId_Type = TmnxMplsTpGlobalID
_TnOamVccvTrNextTpSaiiGlobalId_Object = MibTableColumn
tnOamVccvTrNextTpSaiiGlobalId = _TnOamVccvTrNextTpSaiiGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 27, 1, 14),
    _TnOamVccvTrNextTpSaiiGlobalId_Type()
)
tnOamVccvTrNextTpSaiiGlobalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamVccvTrNextTpSaiiGlobalId.setStatus("current")
_TnOamVccvTrNextTpSaiiNodeId_Type = TmnxMplsTpNodeID
_TnOamVccvTrNextTpSaiiNodeId_Object = MibTableColumn
tnOamVccvTrNextTpSaiiNodeId = _TnOamVccvTrNextTpSaiiNodeId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 27, 1, 15),
    _TnOamVccvTrNextTpSaiiNodeId_Type()
)
tnOamVccvTrNextTpSaiiNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamVccvTrNextTpSaiiNodeId.setStatus("current")
_TnOamVccvTrNextTpSaiiAcId_Type = Unsigned32
_TnOamVccvTrNextTpSaiiAcId_Object = MibTableColumn
tnOamVccvTrNextTpSaiiAcId = _TnOamVccvTrNextTpSaiiAcId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 27, 1, 16),
    _TnOamVccvTrNextTpSaiiAcId_Type()
)
tnOamVccvTrNextTpSaiiAcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamVccvTrNextTpSaiiAcId.setStatus("current")
_TnOamVccvTrNextTpTaiiGlobalId_Type = TmnxMplsTpGlobalID
_TnOamVccvTrNextTpTaiiGlobalId_Object = MibTableColumn
tnOamVccvTrNextTpTaiiGlobalId = _TnOamVccvTrNextTpTaiiGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 27, 1, 17),
    _TnOamVccvTrNextTpTaiiGlobalId_Type()
)
tnOamVccvTrNextTpTaiiGlobalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamVccvTrNextTpTaiiGlobalId.setStatus("current")
_TnOamVccvTrNextTpTaiiNodeId_Type = TmnxMplsTpNodeID
_TnOamVccvTrNextTpTaiiNodeId_Object = MibTableColumn
tnOamVccvTrNextTpTaiiNodeId = _TnOamVccvTrNextTpTaiiNodeId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 27, 1, 18),
    _TnOamVccvTrNextTpTaiiNodeId_Type()
)
tnOamVccvTrNextTpTaiiNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamVccvTrNextTpTaiiNodeId.setStatus("current")
_TnOamVccvTrNextTpTaiiAcId_Type = Unsigned32
_TnOamVccvTrNextTpTaiiAcId_Object = MibTableColumn
tnOamVccvTrNextTpTaiiAcId = _TnOamVccvTrNextTpTaiiAcId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 2, 27, 1, 19),
    _TnOamVccvTrNextTpTaiiAcId_Type()
)
tnOamVccvTrNextTpTaiiAcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamVccvTrNextTpTaiiAcId.setStatus("current")
_TnOamSaaObjs_ObjectIdentity = ObjectIdentity
tnOamSaaObjs = _TnOamSaaObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 3)
)
_TnOamSaaCtlAttributeTotal_Type = Integer32
_TnOamSaaCtlAttributeTotal_Object = MibScalar
tnOamSaaCtlAttributeTotal = _TnOamSaaCtlAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 3, 3),
    _TnOamSaaCtlAttributeTotal_Type()
)
tnOamSaaCtlAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamSaaCtlAttributeTotal.setStatus("current")
_TnOamSaaCtlTable_Object = MibTable
tnOamSaaCtlTable = _TnOamSaaCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 3, 4)
)
if mibBuilder.loadTexts:
    tnOamSaaCtlTable.setStatus("current")
_TnOamSaaCtlEntry_Object = MibTableRow
tnOamSaaCtlEntry = _TnOamSaaCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 3, 4, 1)
)
tnOamSaaCtlEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-OAM-TEST-MIB", "tnOamSaaCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tnOamSaaCtlEntry.setStatus("current")


class _TnOamSaaCtlTestIndex_Type(SnmpAdminString):
    """Custom type tnOamSaaCtlTestIndex based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TnOamSaaCtlTestIndex_Type.__name__ = "SnmpAdminString"
_TnOamSaaCtlTestIndex_Object = MibTableColumn
tnOamSaaCtlTestIndex = _TnOamSaaCtlTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 3, 4, 1, 1),
    _TnOamSaaCtlTestIndex_Type()
)
tnOamSaaCtlTestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOamSaaCtlTestIndex.setStatus("current")
_TnOamSaaCtlRowStatus_Type = RowStatus
_TnOamSaaCtlRowStatus_Object = MibTableColumn
tnOamSaaCtlRowStatus = _TnOamSaaCtlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 3, 4, 1, 2),
    _TnOamSaaCtlRowStatus_Type()
)
tnOamSaaCtlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamSaaCtlRowStatus.setStatus("current")


class _TnOamSaaCtlStorageType_Type(StorageType):
    """Custom type tnOamSaaCtlStorageType based on StorageType"""
    defaultValue = 3


_TnOamSaaCtlStorageType_Type.__name__ = "StorageType"
_TnOamSaaCtlStorageType_Object = MibTableColumn
tnOamSaaCtlStorageType = _TnOamSaaCtlStorageType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 3, 4, 1, 3),
    _TnOamSaaCtlStorageType_Type()
)
tnOamSaaCtlStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamSaaCtlStorageType.setStatus("current")
_TnOamSaaCtlLastChanged_Type = TimeStamp
_TnOamSaaCtlLastChanged_Object = MibTableColumn
tnOamSaaCtlLastChanged = _TnOamSaaCtlLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 3, 4, 1, 4),
    _TnOamSaaCtlLastChanged_Type()
)
tnOamSaaCtlLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamSaaCtlLastChanged.setStatus("current")


class _TnOamSaaCtlAdminStatus_Type(TmnxAdminState):
    """Custom type tnOamSaaCtlAdminStatus based on TmnxAdminState"""
    defaultValue = 3


_TnOamSaaCtlAdminStatus_Type.__name__ = "TmnxAdminState"
_TnOamSaaCtlAdminStatus_Object = MibTableColumn
tnOamSaaCtlAdminStatus = _TnOamSaaCtlAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 3, 4, 1, 5),
    _TnOamSaaCtlAdminStatus_Type()
)
tnOamSaaCtlAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamSaaCtlAdminStatus.setStatus("current")


class _TnOamSaaCtlDescr_Type(TItemDescription):
    """Custom type tnOamSaaCtlDescr based on TItemDescription"""
    defaultHexValue = ""


_TnOamSaaCtlDescr_Type.__name__ = "TItemDescription"
_TnOamSaaCtlDescr_Object = MibTableColumn
tnOamSaaCtlDescr = _TnOamSaaCtlDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 3, 4, 1, 6),
    _TnOamSaaCtlDescr_Type()
)
tnOamSaaCtlDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamSaaCtlDescr.setStatus("current")


class _TnOamSaaCtlTestMode_Type(TmnxOamTestMode):
    """Custom type tnOamSaaCtlTestMode based on TmnxOamTestMode"""
    defaultValue = 0


_TnOamSaaCtlTestMode_Type.__name__ = "TmnxOamTestMode"
_TnOamSaaCtlTestMode_Object = MibTableColumn
tnOamSaaCtlTestMode = _TnOamSaaCtlTestMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 3, 4, 1, 7),
    _TnOamSaaCtlTestMode_Type()
)
tnOamSaaCtlTestMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamSaaCtlTestMode.setStatus("current")
_TnOamSaaCtlRuns_Type = Counter32
_TnOamSaaCtlRuns_Object = MibTableColumn
tnOamSaaCtlRuns = _TnOamSaaCtlRuns_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 3, 4, 1, 8),
    _TnOamSaaCtlRuns_Type()
)
tnOamSaaCtlRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamSaaCtlRuns.setStatus("current")
_TnOamSaaCtlFailures_Type = Counter32
_TnOamSaaCtlFailures_Object = MibTableColumn
tnOamSaaCtlFailures = _TnOamSaaCtlFailures_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 3, 4, 1, 9),
    _TnOamSaaCtlFailures_Type()
)
tnOamSaaCtlFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamSaaCtlFailures.setStatus("current")
_TnOamSaaCtlLastRunResult_Type = TmnxOamTestResult
_TnOamSaaCtlLastRunResult_Object = MibTableColumn
tnOamSaaCtlLastRunResult = _TnOamSaaCtlLastRunResult_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 3, 4, 1, 10),
    _TnOamSaaCtlLastRunResult_Type()
)
tnOamSaaCtlLastRunResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamSaaCtlLastRunResult.setStatus("current")


class _TnOamSaaCtlAcctPolicyId_Type(Integer32):
    """Custom type tnOamSaaCtlAcctPolicyId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_TnOamSaaCtlAcctPolicyId_Type.__name__ = "Integer32"
_TnOamSaaCtlAcctPolicyId_Object = MibTableColumn
tnOamSaaCtlAcctPolicyId = _TnOamSaaCtlAcctPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 3, 4, 1, 11),
    _TnOamSaaCtlAcctPolicyId_Type()
)
tnOamSaaCtlAcctPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamSaaCtlAcctPolicyId.setStatus("current")


class _TnOamSaaCtlSuppressAccounting_Type(TruthValue):
    """Custom type tnOamSaaCtlSuppressAccounting based on TruthValue"""
    defaultValue = 2


_TnOamSaaCtlSuppressAccounting_Type.__name__ = "TruthValue"
_TnOamSaaCtlSuppressAccounting_Object = MibTableColumn
tnOamSaaCtlSuppressAccounting = _TnOamSaaCtlSuppressAccounting_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 3, 4, 1, 12),
    _TnOamSaaCtlSuppressAccounting_Type()
)
tnOamSaaCtlSuppressAccounting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamSaaCtlSuppressAccounting.setStatus("current")


class _TnOamSaaCtlContinuous_Type(TruthValue):
    """Custom type tnOamSaaCtlContinuous based on TruthValue"""
    defaultValue = 2


_TnOamSaaCtlContinuous_Type.__name__ = "TruthValue"
_TnOamSaaCtlContinuous_Object = MibTableColumn
tnOamSaaCtlContinuous = _TnOamSaaCtlContinuous_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 3, 4, 1, 13),
    _TnOamSaaCtlContinuous_Type()
)
tnOamSaaCtlContinuous.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamSaaCtlContinuous.setStatus("current")


class _TnOamSaaCtlKeepProbeHistoryAdm_Type(Integer32):
    """Custom type tnOamSaaCtlKeepProbeHistoryAdm based on Integer32"""
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


_TnOamSaaCtlKeepProbeHistoryAdm_Type.__name__ = "Integer32"
_TnOamSaaCtlKeepProbeHistoryAdm_Object = MibTableColumn
tnOamSaaCtlKeepProbeHistoryAdm = _TnOamSaaCtlKeepProbeHistoryAdm_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 3, 4, 1, 15),
    _TnOamSaaCtlKeepProbeHistoryAdm_Type()
)
tnOamSaaCtlKeepProbeHistoryAdm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamSaaCtlKeepProbeHistoryAdm.setStatus("current")


class _TnOamSaaCtlKeepProbeHistoryOpr_Type(Integer32):
    """Custom type tnOamSaaCtlKeepProbeHistoryOpr based on Integer32"""
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


_TnOamSaaCtlKeepProbeHistoryOpr_Type.__name__ = "Integer32"
_TnOamSaaCtlKeepProbeHistoryOpr_Object = MibTableColumn
tnOamSaaCtlKeepProbeHistoryOpr = _TnOamSaaCtlKeepProbeHistoryOpr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 3, 4, 1, 16),
    _TnOamSaaCtlKeepProbeHistoryOpr_Type()
)
tnOamSaaCtlKeepProbeHistoryOpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamSaaCtlKeepProbeHistoryOpr.setStatus("current")


class _TnOamSaaCtlAlmProfName_Type(OctetString):
    """Custom type tnOamSaaCtlAlmProfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_TnOamSaaCtlAlmProfName_Type.__name__ = "OctetString"
_TnOamSaaCtlAlmProfName_Object = MibTableColumn
tnOamSaaCtlAlmProfName = _TnOamSaaCtlAlmProfName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 3, 4, 1, 17),
    _TnOamSaaCtlAlmProfName_Type()
)
tnOamSaaCtlAlmProfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOamSaaCtlAlmProfName.setStatus("current")
_TnOamTestScalar1_Type = Unsigned32
_TnOamTestScalar1_Object = MibScalar
tnOamTestScalar1 = _TnOamTestScalar1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 101),
    _TnOamTestScalar1_Type()
)
tnOamTestScalar1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamTestScalar1.setStatus("current")
_TnOamTestScalar2_Type = Unsigned32
_TnOamTestScalar2_Object = MibScalar
tnOamTestScalar2 = _TnOamTestScalar2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 11, 102),
    _TnOamTestScalar2_Type()
)
tnOamTestScalar2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOamTestScalar2.setStatus("current")
_TnOamTestNotifications_ObjectIdentity = ObjectIdentity
tnOamTestNotifications = _TnOamTestNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 11)
)
_TnOamPingNotifyPrefix_ObjectIdentity = ObjectIdentity
tnOamPingNotifyPrefix = _TnOamPingNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 11, 1)
)
_TnOamPingNotifications_ObjectIdentity = ObjectIdentity
tnOamPingNotifications = _TnOamPingNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 11, 1, 0)
)
_TnOamTraceRouteNotifyPrefix_ObjectIdentity = ObjectIdentity
tnOamTraceRouteNotifyPrefix = _TnOamTraceRouteNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 11, 2)
)
_TnOamTraceRouteNotifications_ObjectIdentity = ObjectIdentity
tnOamTraceRouteNotifications = _TnOamTraceRouteNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 11, 2, 0)
)
_TnOamSaaNotifyPrefix_ObjectIdentity = ObjectIdentity
tnOamSaaNotifyPrefix = _TnOamSaaNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 11, 3)
)
_TnOamSaaNotifications_ObjectIdentity = ObjectIdentity
tnOamSaaNotifications = _TnOamSaaNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 11, 3, 0)
)
tnOamPingCtlEntry.registerAugmentions(
    ("TN-OAM-TEST-MIB",
     "tnOamEthCfmPingCtlEntry")
)
tnOamEthCfmPingCtlEntry.setIndexNames(*tnOamPingCtlEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-OAM-TEST-MIB",
    **{"TmnxOamLspAssocChannel": TmnxOamLspAssocChannel,
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
       "TmnxOamVcType": TmnxOamVcType,
       "TmnxOamTestResult": TmnxOamTestResult,
       "tnOamTestMIBModule": tnOamTestMIBModule,
       "tnOamTestObjs": tnOamTestObjs,
       "tnOamPingObjs": tnOamPingObjs,
       "tnOamPingCtlAttributeTotal": tnOamPingCtlAttributeTotal,
       "tnOamPingCtlTable": tnOamPingCtlTable,
       "tnOamPingCtlEntry": tnOamPingCtlEntry,
       "tnOamPingCtlTestIndex": tnOamPingCtlTestIndex,
       "tnOamPingCtlRowStatus": tnOamPingCtlRowStatus,
       "tnOamPingCtlStorageType": tnOamPingCtlStorageType,
       "tnOamPingCtlDescr": tnOamPingCtlDescr,
       "tnOamPingCtlTestMode": tnOamPingCtlTestMode,
       "tnOamPingCtlAdminStatus": tnOamPingCtlAdminStatus,
       "tnOamPingCtlOrigSdpId": tnOamPingCtlOrigSdpId,
       "tnOamPingCtlRespSdpId": tnOamPingCtlRespSdpId,
       "tnOamPingCtlFcName": tnOamPingCtlFcName,
       "tnOamPingCtlProfile": tnOamPingCtlProfile,
       "tnOamPingCtlMtuStartSize": tnOamPingCtlMtuStartSize,
       "tnOamPingCtlMtuEndSize": tnOamPingCtlMtuEndSize,
       "tnOamPingCtlMtuStepSize": tnOamPingCtlMtuStepSize,
       "tnOamPingCtlTargetIpAddress": tnOamPingCtlTargetIpAddress,
       "tnOamPingCtlServiceId": tnOamPingCtlServiceId,
       "tnOamPingCtlLocalSdp": tnOamPingCtlLocalSdp,
       "tnOamPingCtlRemoteSdp": tnOamPingCtlRemoteSdp,
       "tnOamPingCtlSize": tnOamPingCtlSize,
       "tnOamPingCtlTimeOut": tnOamPingCtlTimeOut,
       "tnOamPingCtlProbeCount": tnOamPingCtlProbeCount,
       "tnOamPingCtlInterval": tnOamPingCtlInterval,
       "tnOamPingCtlMaxRows": tnOamPingCtlMaxRows,
       "tnOamPingCtlTrapGeneration": tnOamPingCtlTrapGeneration,
       "tnOamPingCtlTrapProbeFailureFilter": tnOamPingCtlTrapProbeFailureFilter,
       "tnOamPingCtlTrapTestFailureFilter": tnOamPingCtlTrapTestFailureFilter,
       "tnOamPingCtlSAA": tnOamPingCtlSAA,
       "tnOamPingCtlRuns": tnOamPingCtlRuns,
       "tnOamPingCtlFailures": tnOamPingCtlFailures,
       "tnOamPingCtlLastRunResult": tnOamPingCtlLastRunResult,
       "tnOamPingCtlLastChanged": tnOamPingCtlLastChanged,
       "tnOamPingCtlVRtrID": tnOamPingCtlVRtrID,
       "tnOamPingCtlTgtAddrType": tnOamPingCtlTgtAddrType,
       "tnOamPingCtlTgtAddress": tnOamPingCtlTgtAddress,
       "tnOamPingCtlSrcAddrType": tnOamPingCtlSrcAddrType,
       "tnOamPingCtlSrcAddress": tnOamPingCtlSrcAddress,
       "tnOamPingCtlDnsName": tnOamPingCtlDnsName,
       "tnOamPingCtlDNSRecord": tnOamPingCtlDNSRecord,
       "tnOamPingCtlIntervalUnits": tnOamPingCtlIntervalUnits,
       "tnOamPingResultsTable": tnOamPingResultsTable,
       "tnOamPingResultsEntry": tnOamPingResultsEntry,
       "tnOamPingResultsOperStatus": tnOamPingResultsOperStatus,
       "tnOamPingResultsMinRtt": tnOamPingResultsMinRtt,
       "tnOamPingResultsMaxRtt": tnOamPingResultsMaxRtt,
       "tnOamPingResultsAverageRtt": tnOamPingResultsAverageRtt,
       "tnOamPingResultsRttSumOfSquares": tnOamPingResultsRttSumOfSquares,
       "tnOamPingResultsMtuResponseSize": tnOamPingResultsMtuResponseSize,
       "tnOamPingResultsSvcPing": tnOamPingResultsSvcPing,
       "tnOamPingResultsProbeResponses": tnOamPingResultsProbeResponses,
       "tnOamPingResultsSentProbes": tnOamPingResultsSentProbes,
       "tnOamPingResultsLastGoodProbe": tnOamPingResultsLastGoodProbe,
       "tnOamPingResultsLastRespHeader": tnOamPingResultsLastRespHeader,
       "tnOamPingResultsMinTt": tnOamPingResultsMinTt,
       "tnOamPingResultsMaxTt": tnOamPingResultsMaxTt,
       "tnOamPingResultsAverageTt": tnOamPingResultsAverageTt,
       "tnOamPingResultsTtSumOfSquares": tnOamPingResultsTtSumOfSquares,
       "tnOamPingResultsMinInTt": tnOamPingResultsMinInTt,
       "tnOamPingResultsMaxInTt": tnOamPingResultsMaxInTt,
       "tnOamPingResultsAverageInTt": tnOamPingResultsAverageInTt,
       "tnOamPingResultsInTtSumOfSqrs": tnOamPingResultsInTtSumOfSqrs,
       "tnOamPingResultsOutJitter": tnOamPingResultsOutJitter,
       "tnOamPingResultsInJitter": tnOamPingResultsInJitter,
       "tnOamPingResultsRtJitter": tnOamPingResultsRtJitter,
       "tnOamPingResultsProbeTimeouts": tnOamPingResultsProbeTimeouts,
       "tnOamPingResultsProbeFailures": tnOamPingResultsProbeFailures,
       "tnOamPingResultsTestRunIndex": tnOamPingResultsTestRunIndex,
       "tnOamPingResultsRttOFSumSquares": tnOamPingResultsRttOFSumSquares,
       "tnOamPingResultsRttHCSumSquares": tnOamPingResultsRttHCSumSquares,
       "tnOamPingResultsTtOFSumSquares": tnOamPingResultsTtOFSumSquares,
       "tnOamPingResultsTtHCSumSquares": tnOamPingResultsTtHCSumSquares,
       "tnOamPingResultsInTtOFSumSqrs": tnOamPingResultsInTtOFSumSqrs,
       "tnOamPingResultsInTtHCSumSqrs": tnOamPingResultsInTtHCSumSqrs,
       "tnOamPingResultsTestRunResult": tnOamPingResultsTestRunResult,
       "tnOamPingHistoryTable": tnOamPingHistoryTable,
       "tnOamPingHistoryEntry": tnOamPingHistoryEntry,
       "tnOamPingHistoryIndex": tnOamPingHistoryIndex,
       "tnOamPingHistoryResponse": tnOamPingHistoryResponse,
       "tnOamPingHistoryOneWayTime": tnOamPingHistoryOneWayTime,
       "tnOamPingHistorySize": tnOamPingHistorySize,
       "tnOamPingHistoryStatus": tnOamPingHistoryStatus,
       "tnOamPingHistoryTime": tnOamPingHistoryTime,
       "tnOamPingHistoryReturnCode": tnOamPingHistoryReturnCode,
       "tnOamPingHistorySrcIpAddress": tnOamPingHistorySrcIpAddress,
       "tnOamPingHistAddressType": tnOamPingHistAddressType,
       "tnOamPingHistSapId": tnOamPingHistSapId,
       "tnOamPingHistoryVersion": tnOamPingHistoryVersion,
       "tnOamPingHistoryCpeMacAddr": tnOamPingHistoryCpeMacAddr,
       "tnOamPingHistoryRespSvcId": tnOamPingHistoryRespSvcId,
       "tnOamPingHistorySequence": tnOamPingHistorySequence,
       "tnOamPingHistoryIfIndex": tnOamPingHistoryIfIndex,
       "tnOamPingHistoryDataLen": tnOamPingHistoryDataLen,
       "tnOamPingHistoryRespPlane": tnOamPingHistoryRespPlane,
       "tnOamPingHistoryReqHdr": tnOamPingHistoryReqHdr,
       "tnOamPingHistoryRespHdr": tnOamPingHistoryRespHdr,
       "tnOamPingHistoryDnsAddrType": tnOamPingHistoryDnsAddrType,
       "tnOamPingHistoryDnsAddress": tnOamPingHistoryDnsAddress,
       "tnOamPingHistorySrcAddrType": tnOamPingHistorySrcAddrType,
       "tnOamPingHistorySrcAddress": tnOamPingHistorySrcAddress,
       "tnOamPingHistoryInOneWayTime": tnOamPingHistoryInOneWayTime,
       "tnOamPingHistoryLspName": tnOamPingHistoryLspName,
       "tnOamPingHistNextHopAddrType": tnOamPingHistNextHopAddrType,
       "tnOamPingHistNextHopAddress": tnOamPingHistNextHopAddress,
       "tnOamPingHistorySrcGlobalId": tnOamPingHistorySrcGlobalId,
       "tnOamPingHistorySrcNodeId": tnOamPingHistorySrcNodeId,
       "tnOamPingHistorySdpBindId": tnOamPingHistorySdpBindId,
       "tnOamPingHistoryRtrnSubcode": tnOamPingHistoryRtrnSubcode,
       "tnOamLspPingCtlTable": tnOamLspPingCtlTable,
       "tnOamLspPingCtlEntry": tnOamLspPingCtlEntry,
       "tnOamLspPingCtlVRtrID": tnOamLspPingCtlVRtrID,
       "tnOamLspPingCtlLspName": tnOamLspPingCtlLspName,
       "tnOamLspPingCtlReturnLsp": tnOamLspPingCtlReturnLsp,
       "tnOamLspPingCtlTtl": tnOamLspPingCtlTtl,
       "tnOamLspPingCtlPathName": tnOamLspPingCtlPathName,
       "tnOamLspPingCtlLdpIpPrefix": tnOamLspPingCtlLdpIpPrefix,
       "tnOamLspPingCtlLdpIpPrefixLen": tnOamLspPingCtlLdpIpPrefixLen,
       "tnOamLspPingCtlLdpPrefixType": tnOamLspPingCtlLdpPrefixType,
       "tnOamLspPingCtlLdpPrefix": tnOamLspPingCtlLdpPrefix,
       "tnOamLspPingCtlLdpPrefixLen": tnOamLspPingCtlLdpPrefixLen,
       "tnOamLspPingCtlPathDestType": tnOamLspPingCtlPathDestType,
       "tnOamLspPingCtlPathDest": tnOamLspPingCtlPathDest,
       "tnOamLspPingCtlNhIntfName": tnOamLspPingCtlNhIntfName,
       "tnOamLspPingCtlNhAddressType": tnOamLspPingCtlNhAddressType,
       "tnOamLspPingCtlNhAddress": tnOamLspPingCtlNhAddress,
       "tnOamLspPingCtlTestSubMode": tnOamLspPingCtlTestSubMode,
       "tnOamLspPingCtlMplsTpPathType": tnOamLspPingCtlMplsTpPathType,
       "tnOamLspPingCtlMplsTpGlobalId": tnOamLspPingCtlMplsTpGlobalId,
       "tnOamLspPingCtlMplsTpNodeId": tnOamLspPingCtlMplsTpNodeId,
       "tnOamLspPingCtlAssocChannel": tnOamLspPingCtlAssocChannel,
       "tnOamLspPingCtlForce": tnOamLspPingCtlForce,
       "tnOamVccvPingCtlTable": tnOamVccvPingCtlTable,
       "tnOamVccvPingCtlEntry": tnOamVccvPingCtlEntry,
       "tnOamVccvPingCtlSdpIdVcId": tnOamVccvPingCtlSdpIdVcId,
       "tnOamVccvPingCtlReplyMode": tnOamVccvPingCtlReplyMode,
       "tnOamVccvPingCtlPwId": tnOamVccvPingCtlPwId,
       "tnOamVccvPingCtlTtl": tnOamVccvPingCtlTtl,
       "tnOamVccvPingCtlSpokeSdpId": tnOamVccvPingCtlSpokeSdpId,
       "tnOamVccvPingCtlSaiiGlobalId": tnOamVccvPingCtlSaiiGlobalId,
       "tnOamVccvPingCtlSaiiPrefix": tnOamVccvPingCtlSaiiPrefix,
       "tnOamVccvPingCtlSaiiAcId": tnOamVccvPingCtlSaiiAcId,
       "tnOamVccvPingCtlTaiiGlobalId": tnOamVccvPingCtlTaiiGlobalId,
       "tnOamVccvPingCtlTaiiPrefix": tnOamVccvPingCtlTaiiPrefix,
       "tnOamVccvPingCtlTaiiAcId": tnOamVccvPingCtlTaiiAcId,
       "tnOamVccvPingCtlMplsTpGlobalId": tnOamVccvPingCtlMplsTpGlobalId,
       "tnOamVccvPingCtlMplsTpNodeId": tnOamVccvPingCtlMplsTpNodeId,
       "tnOamVccvPingCtlTestSubMode": tnOamVccvPingCtlTestSubMode,
       "tnOamVccvPingCtlAssocChannel": tnOamVccvPingCtlAssocChannel,
       "tnOamEthCfmPingCtlTable": tnOamEthCfmPingCtlTable,
       "tnOamEthCfmPingCtlEntry": tnOamEthCfmPingCtlEntry,
       "tnOamEthCfmPingCtlTgtMacAddr": tnOamEthCfmPingCtlTgtMacAddr,
       "tnOamEthCfmPingCtlSrcMdIndex": tnOamEthCfmPingCtlSrcMdIndex,
       "tnOamEthCfmPingCtlSrcMaIndex": tnOamEthCfmPingCtlSrcMaIndex,
       "tnOamEthCfmPingCtlSrcMepId": tnOamEthCfmPingCtlSrcMepId,
       "tnOamTraceRouteObjs": tnOamTraceRouteObjs,
       "tnOamTrCtlTable": tnOamTrCtlTable,
       "tnOamTrCtlEntry": tnOamTrCtlEntry,
       "tnOamTrCtlTestIndex": tnOamTrCtlTestIndex,
       "tnOamTrCtlRowStatus": tnOamTrCtlRowStatus,
       "tnOamTrCtlStorageType": tnOamTrCtlStorageType,
       "tnOamTrCtlDescr": tnOamTrCtlDescr,
       "tnOamTrCtlTestMode": tnOamTrCtlTestMode,
       "tnOamTrCtlAdminStatus": tnOamTrCtlAdminStatus,
       "tnOamTrCtlFcName": tnOamTrCtlFcName,
       "tnOamTrCtlProfile": tnOamTrCtlProfile,
       "tnOamTrCtlTargetIpAddress": tnOamTrCtlTargetIpAddress,
       "tnOamTrCtlServiceId": tnOamTrCtlServiceId,
       "tnOamTrCtlDataSize": tnOamTrCtlDataSize,
       "tnOamTrCtlTimeOut": tnOamTrCtlTimeOut,
       "tnOamTrCtlProbesPerHop": tnOamTrCtlProbesPerHop,
       "tnOamTrCtlMaxTtl": tnOamTrCtlMaxTtl,
       "tnOamTrCtlInitialTtl": tnOamTrCtlInitialTtl,
       "tnOamTrCtlDSField": tnOamTrCtlDSField,
       "tnOamTrCtlMaxFailures": tnOamTrCtlMaxFailures,
       "tnOamTrCtlInterval": tnOamTrCtlInterval,
       "tnOamTrCtlMaxRows": tnOamTrCtlMaxRows,
       "tnOamTrCtlTrapGeneration": tnOamTrCtlTrapGeneration,
       "tnOamTrCtlCreateHopsEntries": tnOamTrCtlCreateHopsEntries,
       "tnOamTrCtlSAA": tnOamTrCtlSAA,
       "tnOamTrCtlRuns": tnOamTrCtlRuns,
       "tnOamTrCtlFailures": tnOamTrCtlFailures,
       "tnOamTrCtlLastRunResult": tnOamTrCtlLastRunResult,
       "tnOamTrCtlLastChanged": tnOamTrCtlLastChanged,
       "tnOamTrCtlVRtrID": tnOamTrCtlVRtrID,
       "tnOamTrCtlTgtAddrType": tnOamTrCtlTgtAddrType,
       "tnOamTrCtlTgtAddress": tnOamTrCtlTgtAddress,
       "tnOamTrCtlSrcAddrType": tnOamTrCtlSrcAddrType,
       "tnOamTrCtlSrcAddress": tnOamTrCtlSrcAddress,
       "tnOamTrCtlWaitMilliSec": tnOamTrCtlWaitMilliSec,
       "tnOamTrResultsTable": tnOamTrResultsTable,
       "tnOamTrResultsEntry": tnOamTrResultsEntry,
       "tnOamTrResultsOperStatus": tnOamTrResultsOperStatus,
       "tnOamTrResultsCurHopCount": tnOamTrResultsCurHopCount,
       "tnOamTrResultsCurProbeCount": tnOamTrResultsCurProbeCount,
       "tnOamTrResultsIpTgtAddr": tnOamTrResultsIpTgtAddr,
       "tnOamTrResultsTestAttempts": tnOamTrResultsTestAttempts,
       "tnOamTrResultsTestSuccesses": tnOamTrResultsTestSuccesses,
       "tnOamTrResultsLastGoodPath": tnOamTrResultsLastGoodPath,
       "tnOamTrResultsTestRunIndex": tnOamTrResultsTestRunIndex,
       "tnOamTrResultsTgtAddrType": tnOamTrResultsTgtAddrType,
       "tnOamTrResultsTgtAddress": tnOamTrResultsTgtAddress,
       "tnOamTrResultsTestRunResult": tnOamTrResultsTestRunResult,
       "tnOamTrProbeHistoryTable": tnOamTrProbeHistoryTable,
       "tnOamTrProbeHistoryEntry": tnOamTrProbeHistoryEntry,
       "tnOamTrProbeHistoryIndex": tnOamTrProbeHistoryIndex,
       "tnOamTrProbeHistoryHopIndex": tnOamTrProbeHistoryHopIndex,
       "tnOamTrProbeHistoryProbeIndex": tnOamTrProbeHistoryProbeIndex,
       "tnOamTrProbeHistoryIpAddr": tnOamTrProbeHistoryIpAddr,
       "tnOamTrProbeHistoryResponse": tnOamTrProbeHistoryResponse,
       "tnOamTrProbeHistoryOneWayTime": tnOamTrProbeHistoryOneWayTime,
       "tnOamTrProbeHistoryStatus": tnOamTrProbeHistoryStatus,
       "tnOamTrProbeHistoryLastRC": tnOamTrProbeHistoryLastRC,
       "tnOamTrProbeHistoryTime": tnOamTrProbeHistoryTime,
       "tnOamTrProbeHistoryResponsePlane": tnOamTrProbeHistoryResponsePlane,
       "tnOamTrProbeHistoryAddressType": tnOamTrProbeHistoryAddressType,
       "tnOamTrProbeHistorySapId": tnOamTrProbeHistorySapId,
       "tnOamTrProbeHistoryVersion": tnOamTrProbeHistoryVersion,
       "tnOamTrProbeHistoryRouterID": tnOamTrProbeHistoryRouterID,
       "tnOamTrProbeHistoryIfIndex": tnOamTrProbeHistoryIfIndex,
       "tnOamTrProbeHistoryDataLen": tnOamTrProbeHistoryDataLen,
       "tnOamTrProbeHistorySize": tnOamTrProbeHistorySize,
       "tnOamTrProbeHistoryInOneWayTime": tnOamTrProbeHistoryInOneWayTime,
       "tnOamTrProbeHistoryAddrType": tnOamTrProbeHistoryAddrType,
       "tnOamTrProbeHistoryAddress": tnOamTrProbeHistoryAddress,
       "tnOamTrProbeHistorySrcGlobalId": tnOamTrProbeHistorySrcGlobalId,
       "tnOamTrProbeHistorySrcNodeId": tnOamTrProbeHistorySrcNodeId,
       "tnOamLspTrCtlTable": tnOamLspTrCtlTable,
       "tnOamLspTrCtlEntry": tnOamLspTrCtlEntry,
       "tnOamLspTrCtlVRtrID": tnOamLspTrCtlVRtrID,
       "tnOamLspTrCtlLspName": tnOamLspTrCtlLspName,
       "tnOamLspTrCtlPathName": tnOamLspTrCtlPathName,
       "tnOamLspTrCtlLdpIpPrefix": tnOamLspTrCtlLdpIpPrefix,
       "tnOamLspTrCtlLdpIpPrefixLen": tnOamLspTrCtlLdpIpPrefixLen,
       "tnOamLspTrCtlLdpPrefixType": tnOamLspTrCtlLdpPrefixType,
       "tnOamLspTrCtlLdpPrefix": tnOamLspTrCtlLdpPrefix,
       "tnOamLspTrCtlLdpPrefixLen": tnOamLspTrCtlLdpPrefixLen,
       "tnOamLspTrCtlPathDestType": tnOamLspTrCtlPathDestType,
       "tnOamLspTrCtlPathDest": tnOamLspTrCtlPathDest,
       "tnOamLspTrCtlNhIntfName": tnOamLspTrCtlNhIntfName,
       "tnOamLspTrCtlNhAddressType": tnOamLspTrCtlNhAddressType,
       "tnOamLspTrCtlNhAddress": tnOamLspTrCtlNhAddress,
       "tnOamLspTrCtlDownstreamMapTlv": tnOamLspTrCtlDownstreamMapTlv,
       "tnOamLspTrCtlTestSubMode": tnOamLspTrCtlTestSubMode,
       "tnOamLspTrCtlMplsTpPathType": tnOamLspTrCtlMplsTpPathType,
       "tnOamLspTrCtlAssocChannel": tnOamLspTrCtlAssocChannel,
       "tnOamLspTrCtlForce": tnOamLspTrCtlForce,
       "tnOamLspTrMapTable": tnOamLspTrMapTable,
       "tnOamLspTrMapEntry": tnOamLspTrMapEntry,
       "tnOamLspTrMapIndex": tnOamLspTrMapIndex,
       "tnOamLspTrMapDSIPv4Addr": tnOamLspTrMapDSIPv4Addr,
       "tnOamLspTrMapAddrType": tnOamLspTrMapAddrType,
       "tnOamLspTrMapDSIfAddr": tnOamLspTrMapDSIfAddr,
       "tnOamLspTrMapMTU": tnOamLspTrMapMTU,
       "tnOamLspTrMapDSIndex": tnOamLspTrMapDSIndex,
       "tnOamVccvTrCtlTable": tnOamVccvTrCtlTable,
       "tnOamVccvTrCtlEntry": tnOamVccvTrCtlEntry,
       "tnOamVccvTrCtlSdpIdVcId": tnOamVccvTrCtlSdpIdVcId,
       "tnOamVccvTrCtlReplyMode": tnOamVccvTrCtlReplyMode,
       "tnOamVccvTrCtlSpokeSdpId": tnOamVccvTrCtlSpokeSdpId,
       "tnOamVccvTrCtlSaiiGlobalId": tnOamVccvTrCtlSaiiGlobalId,
       "tnOamVccvTrCtlSaiiPrefix": tnOamVccvTrCtlSaiiPrefix,
       "tnOamVccvTrCtlSaiiAcId": tnOamVccvTrCtlSaiiAcId,
       "tnOamVccvTrCtlTaiiGlobalId": tnOamVccvTrCtlTaiiGlobalId,
       "tnOamVccvTrCtlTaiiPrefix": tnOamVccvTrCtlTaiiPrefix,
       "tnOamVccvTrCtlTaiiAcId": tnOamVccvTrCtlTaiiAcId,
       "tnOamVccvTrCtlTestSubMode": tnOamVccvTrCtlTestSubMode,
       "tnOamVccvTrCtlAssocChannel": tnOamVccvTrCtlAssocChannel,
       "tnOamVccvTrNextPwSegmentTable": tnOamVccvTrNextPwSegmentTable,
       "tnOamVccvTrNextPwSegmentEntry": tnOamVccvTrNextPwSegmentEntry,
       "tnOamVccvTrNextPwID": tnOamVccvTrNextPwID,
       "tnOamVccvTrNextPwType": tnOamVccvTrNextPwType,
       "tnOamVccvTrNextSenderAddrType": tnOamVccvTrNextSenderAddrType,
       "tnOamVccvTrNextSenderAddr": tnOamVccvTrNextSenderAddr,
       "tnOamVccvTrNextRemoteAddrType": tnOamVccvTrNextRemoteAddrType,
       "tnOamVccvTrNextRemoteAddr": tnOamVccvTrNextRemoteAddr,
       "tnOamVccvTrNextSaiiGlobalId": tnOamVccvTrNextSaiiGlobalId,
       "tnOamVccvTrNextSaiiPrefix": tnOamVccvTrNextSaiiPrefix,
       "tnOamVccvTrNextSaiiAcId": tnOamVccvTrNextSaiiAcId,
       "tnOamVccvTrNextTaiiGlobalId": tnOamVccvTrNextTaiiGlobalId,
       "tnOamVccvTrNextTaiiPrefix": tnOamVccvTrNextTaiiPrefix,
       "tnOamVccvTrNextTaiiAcId": tnOamVccvTrNextTaiiAcId,
       "tnOamVccvTrNextTpAgi": tnOamVccvTrNextTpAgi,
       "tnOamVccvTrNextTpSaiiGlobalId": tnOamVccvTrNextTpSaiiGlobalId,
       "tnOamVccvTrNextTpSaiiNodeId": tnOamVccvTrNextTpSaiiNodeId,
       "tnOamVccvTrNextTpSaiiAcId": tnOamVccvTrNextTpSaiiAcId,
       "tnOamVccvTrNextTpTaiiGlobalId": tnOamVccvTrNextTpTaiiGlobalId,
       "tnOamVccvTrNextTpTaiiNodeId": tnOamVccvTrNextTpTaiiNodeId,
       "tnOamVccvTrNextTpTaiiAcId": tnOamVccvTrNextTpTaiiAcId,
       "tnOamSaaObjs": tnOamSaaObjs,
       "tnOamSaaCtlAttributeTotal": tnOamSaaCtlAttributeTotal,
       "tnOamSaaCtlTable": tnOamSaaCtlTable,
       "tnOamSaaCtlEntry": tnOamSaaCtlEntry,
       "tnOamSaaCtlTestIndex": tnOamSaaCtlTestIndex,
       "tnOamSaaCtlRowStatus": tnOamSaaCtlRowStatus,
       "tnOamSaaCtlStorageType": tnOamSaaCtlStorageType,
       "tnOamSaaCtlLastChanged": tnOamSaaCtlLastChanged,
       "tnOamSaaCtlAdminStatus": tnOamSaaCtlAdminStatus,
       "tnOamSaaCtlDescr": tnOamSaaCtlDescr,
       "tnOamSaaCtlTestMode": tnOamSaaCtlTestMode,
       "tnOamSaaCtlRuns": tnOamSaaCtlRuns,
       "tnOamSaaCtlFailures": tnOamSaaCtlFailures,
       "tnOamSaaCtlLastRunResult": tnOamSaaCtlLastRunResult,
       "tnOamSaaCtlAcctPolicyId": tnOamSaaCtlAcctPolicyId,
       "tnOamSaaCtlSuppressAccounting": tnOamSaaCtlSuppressAccounting,
       "tnOamSaaCtlContinuous": tnOamSaaCtlContinuous,
       "tnOamSaaCtlKeepProbeHistoryAdm": tnOamSaaCtlKeepProbeHistoryAdm,
       "tnOamSaaCtlKeepProbeHistoryOpr": tnOamSaaCtlKeepProbeHistoryOpr,
       "tnOamSaaCtlAlmProfName": tnOamSaaCtlAlmProfName,
       "tnOamTestScalar1": tnOamTestScalar1,
       "tnOamTestScalar2": tnOamTestScalar2,
       "tnOamTestNotifications": tnOamTestNotifications,
       "tnOamPingNotifyPrefix": tnOamPingNotifyPrefix,
       "tnOamPingNotifications": tnOamPingNotifications,
       "tnOamTraceRouteNotifyPrefix": tnOamTraceRouteNotifyPrefix,
       "tnOamTraceRouteNotifications": tnOamTraceRouteNotifications,
       "tnOamSaaNotifyPrefix": tnOamSaaNotifyPrefix,
       "tnOamSaaNotifications": tnOamSaaNotifications}
)
