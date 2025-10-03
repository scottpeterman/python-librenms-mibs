# SNMP MIB module (TIMETRA-FILTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\TIMETRA-FILTER-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:14:13 2025
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressIPv4,
 InetAddressIPv6,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv4",
    "InetAddressIPv6",
    "InetAddressPrefixLength",
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
 Opaque,
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
    "Opaque",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 MacAddress,
 PhysAddress,
 RowPointer,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowPointer",
    "RowStatus",
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

(ClassIndexOrNone,
 Dot1PPriority,
 IPv6FlowLabel,
 IPv6FlowLabelMask,
 IpAddressPrefixLength,
 QTagFullRange,
 QTagFullRangeOrNone,
 SdpBindId,
 ServiceAccessPoint,
 SvcISID,
 TDSCPFilterActionValue,
 TDSCPNameOrEmpty,
 TFCTypeOrNone,
 TFrameType,
 TIcmpCodeOrNone,
 TIcmpTypeOrNone,
 TIpOption,
 TIpProtocol,
 TIpProtocolNumber,
 TItemDescription,
 TLNamedItem,
 TLNamedItemOrEmpty,
 TMacFilterType,
 TNamedItem,
 TNamedItemOrEmpty,
 TOperator,
 TRegularExpression,
 TTcpUdpPort,
 TmnxAddressAndPrefixAddress,
 TmnxAddressAndPrefixPrefix,
 TmnxAddressAndPrefixType,
 TmnxAdminState,
 TmnxAdminStateTruthValue,
 TmnxEncapVal,
 TmnxHttpRedirectUrl,
 TmnxNatSubscriberType,
 TmnxNatSubscriberTypeOrNone,
 TmnxOperState,
 TmnxPortID,
 TmnxServId,
 TmnxSubBondingConnIdOrEmpty,
 TmnxVRtrID,
 TmnxVRtrIDOrZero,
 TmnxVRtrMplsLspID) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "ClassIndexOrNone",
    "Dot1PPriority",
    "IPv6FlowLabel",
    "IPv6FlowLabelMask",
    "IpAddressPrefixLength",
    "QTagFullRange",
    "QTagFullRangeOrNone",
    "SdpBindId",
    "ServiceAccessPoint",
    "SvcISID",
    "TDSCPFilterActionValue",
    "TDSCPNameOrEmpty",
    "TFCTypeOrNone",
    "TFrameType",
    "TIcmpCodeOrNone",
    "TIcmpTypeOrNone",
    "TIpOption",
    "TIpProtocol",
    "TIpProtocolNumber",
    "TItemDescription",
    "TLNamedItem",
    "TLNamedItemOrEmpty",
    "TMacFilterType",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TOperator",
    "TRegularExpression",
    "TTcpUdpPort",
    "TmnxAddressAndPrefixAddress",
    "TmnxAddressAndPrefixPrefix",
    "TmnxAddressAndPrefixType",
    "TmnxAdminState",
    "TmnxAdminStateTruthValue",
    "TmnxEncapVal",
    "TmnxHttpRedirectUrl",
    "TmnxNatSubscriberType",
    "TmnxNatSubscriberTypeOrNone",
    "TmnxOperState",
    "TmnxPortID",
    "TmnxServId",
    "TmnxSubBondingConnIdOrEmpty",
    "TmnxVRtrID",
    "TmnxVRtrIDOrZero",
    "TmnxVRtrMplsLspID")


# MODULE-IDENTITY

timetraFilterMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 21)
)
if mibBuilder.loadTexts:
    timetraFilterMIBModule.setRevisions(
        ("2017-01-01 00:00",
         "2016-01-01 00:00",
         "2015-01-01 00:00",
         "2014-01-01 00:00",
         "2012-08-01 00:00",
         "2011-02-01 00:00",
         "2009-07-01 00:00",
         "2008-07-01 00:00",
         "2008-01-01 00:00",
         "2007-01-01 00:00",
         "2006-02-28 00:00",
         "2005-08-31 00:00",
         "2005-01-24 00:00",
         "2004-01-15 00:00",
         "2003-08-15 00:00",
         "2003-01-29 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TFilterID(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class TFilterFlowspecGroupId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
        ValueRangeConstraint(65535, 65535),
    )



class TIPFilterIdOrEmpty(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )



class TVsdFilterID(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(67108865, 67174399),
    )



class TConfigOrVsdFilterID(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
        ValueRangeConstraint(67108865, 67174399),
    )



class TAnyFilterID(TextualConvention, Unsigned32):
    status = "current"


class TFilterScope(TextualConvention, Integer32):
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
        *(("exclusive", 1),
          ("template", 2),
          ("embedded", 3),
          ("system", 4))
    )



class TItemMatch(TextualConvention, Integer32):
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
        *(("off", 1),
          ("false", 2),
          ("true", 3))
    )



class TFragmentMatch(TextualConvention, Integer32):
    status = "current"
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
        *(("off", 1),
          ("false", 2),
          ("true", 3),
          ("first-only", 4),
          ("non-first-only", 5))
    )



class TAnyEntryId(TextualConvention, Unsigned32):
    status = "current"


class TEntryIdOrZero(TAnyEntryId):
    status = "current"
    subtypeSpec = TAnyEntryId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2097151),
    )



class TEntryId(TEntryIdOrZero):
    status = "current"
    subtypeSpec = TEntryIdOrZero.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2097151),
    )



class TLimitedEntryId(TEntryId):
    status = "current"
    subtypeSpec = TEntryId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class TDhcpEntryId(TLimitedEntryId):
    status = "current"


class TEntryBlockSize(TEntryIdOrZero):
    status = "current"
    subtypeSpec = TEntryIdOrZero.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class TFilterAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6,
              7,
              8,
              9,
              11)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("forward", 2),
          ("httpRedirect", 4),
          ("nat", 5),
          ("reassemble", 6),
          ("gtpLclBrkout", 7),
          ("forwardEsiL2", 8),
          ("forwardEsiL3", 9),
          ("unrecognized", 11))
    )



class TFilterPbrDownActionOvr(TextualConvention, Integer32):
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
        *(("none", 0),
          ("drop", 1),
          ("forward", 2),
          ("filterDefaultAction", 3))
    )



class TFilterActionOrDefault(TextualConvention, Integer32):
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
              11,
              30)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("forward", 2),
          ("default", 3),
          ("httpRedirect", 4),
          ("nat", 5),
          ("reassemble", 6),
          ("gtpLclBrkout", 7),
          ("forwardEsiL2", 8),
          ("forwardEsiL3", 9),
          ("unrecognized", 11),
          ("ignoreMatch", 30))
    )



class TIPvXFilterEntryAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
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
              38)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("forward", 2),
          ("httpRedirect", 4),
          ("nat", 5),
          ("reassemble", 6),
          ("gtpLclBrkout", 7),
          ("forwardEsiL2", 8),
          ("forwardEsiL3", 9),
          ("ofPacketIn", 10),
          ("dropTtl", 12),
          ("dropPktLen", 13),
          ("forwardRtr", 14),
          ("forwardNextHop", 15),
          ("forwardNextHopRtr", 16),
          ("forwardNHInterface", 17),
          ("forwardLsp", 18),
          ("forwardSdp", 19),
          ("forwardSap", 20),
          ("forwardRPlcy", 21),
          ("rateLimit", 22),
          ("tcpMssAdjust", 23),
          ("remarkDscp", 24),
          ("rateLimitPktLen", 25),
          ("rateLimitTtl", 26),
          ("dropExtractedTraffic", 27),
          ("forwardVprnTarget", 28),
          ("forwardBondingConnection", 29),
          ("ignoreMatch", 30),
          ("forwardGreTunnel", 31),
          ("dropPattern", 32),
          ("rateLimitPattern", 33),
          ("forwardPattern", 34),
          ("forwardMplsPlcyEndpt", 35),
          ("forwardSrtePlcyEndptColor", 36),
          ("httpRedirectCpf", 37),
          ("rateLimitExtractedTraffic", 38))
    )



class TFilterPbrTargetStatus(TextualConvention, Integer32):
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
        *(("unknown", 0),
          ("doesNotExist", 1),
          ("up", 2),
          ("down", 3),
          ("routerSpecific", 4))
    )



class TFilterDownloadedAction(TextualConvention, Integer32):
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
        *(("none", 1),
          ("primary", 2),
          ("secondary", 3),
          ("forward", 4),
          ("drop", 5),
          ("notDisplayed", 6))
    )



class TFilterEntryActionId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )



class TMacFilterEntryAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              19,
              20,
              22,
              30)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("forward", 2),
          ("httpRedirect", 4),
          ("forwardEsiL2", 8),
          ("forwardSdp", 19),
          ("forwardSap", 20),
          ("rateLimit", 22),
          ("ignoreMatch", 30))
    )



class TIPvXFilterEntryActionExt(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              24)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("remarkDscp", 24))
    )



class TFilterLogId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(101, 199),
    )



class TFilterLogDestination(TextualConvention, Integer32):
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
        *(("memory", 1),
          ("syslog", 2),
          ("file", 3))
    )



class TTimeRangeState(TextualConvention, Integer32):
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
        *(("timeRangeNotApplic", 0),
          ("timeRangeNotActive", 1),
          ("timeRangeActive", 2),
          ("timeRangeActiveDownloadFailed", 3))
    )



class TFilterLogSummaryCriterium(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("srcAddr", 0),
          ("dstAddr", 1))
    )



class TFilterType(TextualConvention, Integer32):
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
        *(("fltrtypeselNone", 0),
          ("fltrtypeselIp", 1),
          ("fltrtypeselMac", 2),
          ("fltrtypeselCpm", 3),
          ("fltrtypeselIpv6", 4),
          ("fltrtypeselCpm6", 5),
          ("fltrtypeselCpmMac", 6))
    )



class TFilterSubInsSpaceOwner(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              6,
              8)
        )
    )
    namedValues = NamedValues(
        *(("radius", 1),
          ("creditControl", 2),
          ("radiusSharedHost", 6),
          ("pccRule", 8))
    )



class TFltrGrpInsrtdEntriesApplication(TextualConvention, Integer32):
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
        *(("none", 0),
          ("radius", 1),
          ("creditControl", 2))
    )



class TDHCPFilterID(TFilterID):
    status = "current"


class TDhcpFilterAction(TextualConvention, Integer32):
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
          ("bypass-host-creation", 2),
          ("drop", 3))
    )



class TDhcpFilterMatch(TextualConvention, Integer32):
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("present", 1),
          ("absent", 2),
          ("string", 3),
          ("string-exact", 4),
          ("string-invert", 5),
          ("string-exact-invert", 6),
          ("hex", 7),
          ("hex-exact", 8),
          ("hex-invert", 9),
          ("hex-exact-invert", 10))
    )



class TFltrPrefixListType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
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



class TmnxEmbeddedFltrOperState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("embedFailedNoResources", -1),
          ("inactive", 0),
          ("active", 1))
    )



class TmnxEmbeddedFltrAdminState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )



class TmnxFltrEmbeddedEntryState(TextualConvention, Integer32):
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
        *(("inserted", 1),
          ("overruled", 2),
          ("inactiveAdminDown", 3),
          ("inactiveNoResources", 4))
    )



class TmnxFilterApplyPathSource(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("bgp-peers", 1))
    )



class TFltrPortSelector(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("and-port", 0),
          ("or-port", 1))
    )



class TFltrMatchIpSelector(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("and-ip", 0),
          ("or-ip", 1))
    )



class TFilterRPBindingOperator(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("and", 0),
          ("or", 1))
    )



class TFilterPacketLength(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class TFilterIpv6MatchPacketLength(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(40, 65575),
    )



class TFilterTTL(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class TmnxFilterRPlcyTestLastAction(TextualConvention, Integer32):
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
        *(("enable", 1),
          ("disable", 2),
          ("none", 3))
    )



class TmnxFilterRPlcyTestRespAction(TextualConvention, Integer32):
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
        *(("increase", 1),
          ("decrease", 2),
          ("disable", 3))
    )



class TFilterEgressPBR(TextualConvention, Integer32):
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
        *(("disable", 0),
          ("enable", 1),
          ("enableWithL4LB", 2))
    )



class TFilterEsi(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10



class TFilterEntryActionRateLimit(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2000000000),
    )



class TFilterEmbedOffset(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2097151),
    )



class TIPvXFilterType(TextualConvention, Integer32):
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
        *(("normal", 0),
          ("srcMac", 1),
          ("pktLen", 2),
          ("destClass", 3))
    )



class TmnxFilterCflowdSampleProfileId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 5),
    )



# MIB Managed Objects in the order of their OIDs

_TFilterMIBConformance_ObjectIdentity = ObjectIdentity
tFilterMIBConformance = _TFilterMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21)
)
_TFilterMIBCompliances_ObjectIdentity = ObjectIdentity
tFilterMIBCompliances = _TFilterMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 1)
)
_TFilterMIBGroups_ObjectIdentity = ObjectIdentity
tFilterMIBGroups = _TFilterMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2)
)
_TFilterObjects_ObjectIdentity = ObjectIdentity
tFilterObjects = _TFilterObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21)
)
_TIPFilterTable_Object = MibTable
tIPFilterTable = _TIPFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 1)
)
if mibBuilder.loadTexts:
    tIPFilterTable.setStatus("current")
_TIPFilterEntry_Object = MibTableRow
tIPFilterEntry = _TIPFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 1, 1)
)
tIPFilterEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tIPFilterId"),
)
if mibBuilder.loadTexts:
    tIPFilterEntry.setStatus("current")
_TIPFilterId_Type = TAnyFilterID
_TIPFilterId_Object = MibTableColumn
tIPFilterId = _TIPFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 1, 1, 1),
    _TIPFilterId_Type()
)
tIPFilterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPFilterId.setStatus("current")
_TIPFilterRowStatus_Type = RowStatus
_TIPFilterRowStatus_Object = MibTableColumn
tIPFilterRowStatus = _TIPFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 1, 1, 2),
    _TIPFilterRowStatus_Type()
)
tIPFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterRowStatus.setStatus("current")


class _TIPFilterScope_Type(TFilterScope):
    """Custom type tIPFilterScope based on TFilterScope"""
    defaultValue = 2


_TIPFilterScope_Type.__name__ = "TFilterScope"
_TIPFilterScope_Object = MibTableColumn
tIPFilterScope = _TIPFilterScope_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 1, 1, 3),
    _TIPFilterScope_Type()
)
tIPFilterScope.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterScope.setStatus("current")


class _TIPFilterDescription_Type(TItemDescription):
    """Custom type tIPFilterDescription based on TItemDescription"""
    defaultHexValue = ""


_TIPFilterDescription_Type.__name__ = "TItemDescription"
_TIPFilterDescription_Object = MibTableColumn
tIPFilterDescription = _TIPFilterDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 1, 1, 4),
    _TIPFilterDescription_Type()
)
tIPFilterDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterDescription.setStatus("current")


class _TIPFilterDefaultAction_Type(TFilterAction):
    """Custom type tIPFilterDefaultAction based on TFilterAction"""
    defaultValue = 1


_TIPFilterDefaultAction_Type.__name__ = "TFilterAction"
_TIPFilterDefaultAction_Object = MibTableColumn
tIPFilterDefaultAction = _TIPFilterDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 1, 1, 5),
    _TIPFilterDefaultAction_Type()
)
tIPFilterDefaultAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterDefaultAction.setStatus("current")


class _TIPFilterRadiusInsertPt_Type(TEntryIdOrZero):
    """Custom type tIPFilterRadiusInsertPt based on TEntryIdOrZero"""
    defaultValue = 0


_TIPFilterRadiusInsertPt_Type.__name__ = "TEntryIdOrZero"
_TIPFilterRadiusInsertPt_Object = MibTableColumn
tIPFilterRadiusInsertPt = _TIPFilterRadiusInsertPt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 1, 1, 6),
    _TIPFilterRadiusInsertPt_Type()
)
tIPFilterRadiusInsertPt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterRadiusInsertPt.setStatus("current")


class _TIPFilterRadiusInsertSize_Type(TEntryBlockSize):
    """Custom type tIPFilterRadiusInsertSize based on TEntryBlockSize"""
    defaultValue = 0


_TIPFilterRadiusInsertSize_Type.__name__ = "TEntryBlockSize"
_TIPFilterRadiusInsertSize_Object = MibTableColumn
tIPFilterRadiusInsertSize = _TIPFilterRadiusInsertSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 1, 1, 7),
    _TIPFilterRadiusInsertSize_Type()
)
tIPFilterRadiusInsertSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterRadiusInsertSize.setStatus("current")


class _TIPFilterCreditCntrlInsertPt_Type(TEntryIdOrZero):
    """Custom type tIPFilterCreditCntrlInsertPt based on TEntryIdOrZero"""
    defaultValue = 0


_TIPFilterCreditCntrlInsertPt_Type.__name__ = "TEntryIdOrZero"
_TIPFilterCreditCntrlInsertPt_Object = MibTableColumn
tIPFilterCreditCntrlInsertPt = _TIPFilterCreditCntrlInsertPt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 1, 1, 8),
    _TIPFilterCreditCntrlInsertPt_Type()
)
tIPFilterCreditCntrlInsertPt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterCreditCntrlInsertPt.setStatus("current")


class _TIPFilterCreditCntrlInsertSize_Type(TEntryBlockSize):
    """Custom type tIPFilterCreditCntrlInsertSize based on TEntryBlockSize"""
    defaultValue = 0


_TIPFilterCreditCntrlInsertSize_Type.__name__ = "TEntryBlockSize"
_TIPFilterCreditCntrlInsertSize_Object = MibTableColumn
tIPFilterCreditCntrlInsertSize = _TIPFilterCreditCntrlInsertSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 1, 1, 9),
    _TIPFilterCreditCntrlInsertSize_Type()
)
tIPFilterCreditCntrlInsertSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterCreditCntrlInsertSize.setStatus("current")


class _TIPFilterSubInsertHighWmark_Type(Integer32):
    """Custom type tIPFilterSubInsertHighWmark based on Integer32"""
    defaultValue = 95

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TIPFilterSubInsertHighWmark_Type.__name__ = "Integer32"
_TIPFilterSubInsertHighWmark_Object = MibTableColumn
tIPFilterSubInsertHighWmark = _TIPFilterSubInsertHighWmark_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 1, 1, 10),
    _TIPFilterSubInsertHighWmark_Type()
)
tIPFilterSubInsertHighWmark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterSubInsertHighWmark.setStatus("current")


class _TIPFilterSubInsertLowWmark_Type(Integer32):
    """Custom type tIPFilterSubInsertLowWmark based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TIPFilterSubInsertLowWmark_Type.__name__ = "Integer32"
_TIPFilterSubInsertLowWmark_Object = MibTableColumn
tIPFilterSubInsertLowWmark = _TIPFilterSubInsertLowWmark_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 1, 1, 11),
    _TIPFilterSubInsertLowWmark_Type()
)
tIPFilterSubInsertLowWmark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterSubInsertLowWmark.setStatus("current")
_TIpFilterCreditCntrlNbrInsertd_Type = Unsigned32
_TIpFilterCreditCntrlNbrInsertd_Object = MibTableColumn
tIpFilterCreditCntrlNbrInsertd = _TIpFilterCreditCntrlNbrInsertd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 1, 1, 12),
    _TIpFilterCreditCntrlNbrInsertd_Type()
)
tIpFilterCreditCntrlNbrInsertd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIpFilterCreditCntrlNbrInsertd.setStatus("current")
_TIpFilterRadiusNbrInsertd_Type = Unsigned32
_TIpFilterRadiusNbrInsertd_Object = MibTableColumn
tIpFilterRadiusNbrInsertd = _TIpFilterRadiusNbrInsertd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 1, 1, 13),
    _TIpFilterRadiusNbrInsertd_Type()
)
tIpFilterRadiusNbrInsertd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIpFilterRadiusNbrInsertd.setStatus("current")


class _TIpFilterName_Type(TLNamedItemOrEmpty):
    """Custom type tIpFilterName based on TLNamedItemOrEmpty"""
    defaultHexValue = ""


_TIpFilterName_Type.__name__ = "TLNamedItemOrEmpty"
_TIpFilterName_Object = MibTableColumn
tIpFilterName = _TIpFilterName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 1, 1, 14),
    _TIpFilterName_Type()
)
tIpFilterName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIpFilterName.setStatus("current")


class _TIPFilterHostSharedInsertPt_Type(TEntryIdOrZero):
    """Custom type tIPFilterHostSharedInsertPt based on TEntryIdOrZero"""
    defaultValue = 0


_TIPFilterHostSharedInsertPt_Type.__name__ = "TEntryIdOrZero"
_TIPFilterHostSharedInsertPt_Object = MibTableColumn
tIPFilterHostSharedInsertPt = _TIPFilterHostSharedInsertPt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 1, 1, 15),
    _TIPFilterHostSharedInsertPt_Type()
)
tIPFilterHostSharedInsertPt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterHostSharedInsertPt.setStatus("current")


class _TIPFilterHostSharedInsertSize_Type(TEntryBlockSize):
    """Custom type tIPFilterHostSharedInsertSize based on TEntryBlockSize"""
    defaultValue = 0


_TIPFilterHostSharedInsertSize_Type.__name__ = "TEntryBlockSize"
_TIPFilterHostSharedInsertSize_Object = MibTableColumn
tIPFilterHostSharedInsertSize = _TIPFilterHostSharedInsertSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 1, 1, 16),
    _TIPFilterHostSharedInsertSize_Type()
)
tIPFilterHostSharedInsertSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterHostSharedInsertSize.setStatus("current")
_TIpFilterHostSharedNbrInsertd_Type = Unsigned32
_TIpFilterHostSharedNbrInsertd_Object = MibTableColumn
tIpFilterHostSharedNbrInsertd = _TIpFilterHostSharedNbrInsertd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 1, 1, 17),
    _TIpFilterHostSharedNbrInsertd_Type()
)
tIpFilterHostSharedNbrInsertd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIpFilterHostSharedNbrInsertd.setStatus("current")


class _TIPFilterHostSharedHighWmark_Type(Integer32):
    """Custom type tIPFilterHostSharedHighWmark based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 8000),
    )


_TIPFilterHostSharedHighWmark_Type.__name__ = "Integer32"
_TIPFilterHostSharedHighWmark_Object = MibTableColumn
tIPFilterHostSharedHighWmark = _TIPFilterHostSharedHighWmark_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 1, 1, 18),
    _TIPFilterHostSharedHighWmark_Type()
)
tIPFilterHostSharedHighWmark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterHostSharedHighWmark.setStatus("current")


class _TIPFilterHostSharedLowWmark_Type(Integer32):
    """Custom type tIPFilterHostSharedLowWmark based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 8000),
    )


_TIPFilterHostSharedLowWmark_Type.__name__ = "Integer32"
_TIPFilterHostSharedLowWmark_Object = MibTableColumn
tIPFilterHostSharedLowWmark = _TIPFilterHostSharedLowWmark_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 1, 1, 19),
    _TIPFilterHostSharedLowWmark_Type()
)
tIPFilterHostSharedLowWmark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterHostSharedLowWmark.setStatus("current")
_TIPFilterNbrHostSharedFltrs_Type = Unsigned32
_TIPFilterNbrHostSharedFltrs_Object = MibTableColumn
tIPFilterNbrHostSharedFltrs = _TIPFilterNbrHostSharedFltrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 1, 1, 20),
    _TIPFilterNbrHostSharedFltrs_Type()
)
tIPFilterNbrHostSharedFltrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPFilterNbrHostSharedFltrs.setStatus("current")


class _TIPFilterSharedPccRuleInsrtPt_Type(TEntryIdOrZero):
    """Custom type tIPFilterSharedPccRuleInsrtPt based on TEntryIdOrZero"""
    defaultValue = 0


_TIPFilterSharedPccRuleInsrtPt_Type.__name__ = "TEntryIdOrZero"
_TIPFilterSharedPccRuleInsrtPt_Object = MibTableColumn
tIPFilterSharedPccRuleInsrtPt = _TIPFilterSharedPccRuleInsrtPt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 1, 1, 21),
    _TIPFilterSharedPccRuleInsrtPt_Type()
)
tIPFilterSharedPccRuleInsrtPt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterSharedPccRuleInsrtPt.setStatus("current")


class _TIPFilterSharedPccRuleInsrtSize_Type(TEntryBlockSize):
    """Custom type tIPFilterSharedPccRuleInsrtSize based on TEntryBlockSize"""
    defaultValue = 0


_TIPFilterSharedPccRuleInsrtSize_Type.__name__ = "TEntryBlockSize"
_TIPFilterSharedPccRuleInsrtSize_Object = MibTableColumn
tIPFilterSharedPccRuleInsrtSize = _TIPFilterSharedPccRuleInsrtSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 1, 1, 22),
    _TIPFilterSharedPccRuleInsrtSize_Type()
)
tIPFilterSharedPccRuleInsrtSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterSharedPccRuleInsrtSize.setStatus("current")
_TIPFilterSharedPccRuleNbrInsrtd_Type = Unsigned32
_TIPFilterSharedPccRuleNbrInsrtd_Object = MibTableColumn
tIPFilterSharedPccRuleNbrInsrtd = _TIPFilterSharedPccRuleNbrInsrtd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 1, 1, 23),
    _TIPFilterSharedPccRuleNbrInsrtd_Type()
)
tIPFilterSharedPccRuleNbrInsrtd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPFilterSharedPccRuleNbrInsrtd.setStatus("current")


class _TIPFilterChainToSystemFilter_Type(TruthValue):
    """Custom type tIPFilterChainToSystemFilter based on TruthValue"""
    defaultValue = 2


_TIPFilterChainToSystemFilter_Type.__name__ = "TruthValue"
_TIPFilterChainToSystemFilter_Object = MibTableColumn
tIPFilterChainToSystemFilter = _TIPFilterChainToSystemFilter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 1, 1, 24),
    _TIPFilterChainToSystemFilter_Type()
)
tIPFilterChainToSystemFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterChainToSystemFilter.setStatus("current")


class _TIPFilterType_Type(TIPvXFilterType):
    """Custom type tIPFilterType based on TIPvXFilterType"""
    defaultValue = 0


_TIPFilterType_Type.__name__ = "TIPvXFilterType"
_TIPFilterType_Object = MibTableColumn
tIPFilterType = _TIPFilterType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 1, 1, 25),
    _TIPFilterType_Type()
)
tIPFilterType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterType.setStatus("current")
_TIPFilterParamsTable_Object = MibTable
tIPFilterParamsTable = _TIPFilterParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2)
)
if mibBuilder.loadTexts:
    tIPFilterParamsTable.setStatus("current")
_TIPFilterParamsEntry_Object = MibTableRow
tIPFilterParamsEntry = _TIPFilterParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1)
)
tIPFilterParamsEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tIPFilterId"),
    (0, "TIMETRA-FILTER-MIB", "tIPFilterParamsIndex"),
)
if mibBuilder.loadTexts:
    tIPFilterParamsEntry.setStatus("current")
_TIPFilterParamsIndex_Type = TEntryId
_TIPFilterParamsIndex_Object = MibTableColumn
tIPFilterParamsIndex = _TIPFilterParamsIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 1),
    _TIPFilterParamsIndex_Type()
)
tIPFilterParamsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPFilterParamsIndex.setStatus("current")
_TIPFilterParamsRowStatus_Type = RowStatus
_TIPFilterParamsRowStatus_Object = MibTableColumn
tIPFilterParamsRowStatus = _TIPFilterParamsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 2),
    _TIPFilterParamsRowStatus_Type()
)
tIPFilterParamsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsRowStatus.setStatus("current")


class _TIPFilterParamsLogId_Type(TFilterLogId):
    """Custom type tIPFilterParamsLogId based on TFilterLogId"""
    defaultValue = 0


_TIPFilterParamsLogId_Type.__name__ = "TFilterLogId"
_TIPFilterParamsLogId_Object = MibTableColumn
tIPFilterParamsLogId = _TIPFilterParamsLogId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 3),
    _TIPFilterParamsLogId_Type()
)
tIPFilterParamsLogId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsLogId.setStatus("current")


class _TIPFilterParamsDescription_Type(TItemDescription):
    """Custom type tIPFilterParamsDescription based on TItemDescription"""
    defaultHexValue = ""


_TIPFilterParamsDescription_Type.__name__ = "TItemDescription"
_TIPFilterParamsDescription_Object = MibTableColumn
tIPFilterParamsDescription = _TIPFilterParamsDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 4),
    _TIPFilterParamsDescription_Type()
)
tIPFilterParamsDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsDescription.setStatus("current")


class _TIPFilterParamsAction_Type(TFilterActionOrDefault):
    """Custom type tIPFilterParamsAction based on TFilterActionOrDefault"""
    defaultValue = 30


_TIPFilterParamsAction_Type.__name__ = "TFilterActionOrDefault"
_TIPFilterParamsAction_Object = MibTableColumn
tIPFilterParamsAction = _TIPFilterParamsAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 5),
    _TIPFilterParamsAction_Type()
)
tIPFilterParamsAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsAction.setStatus("obsolete")


class _TIPFilterParamsForwardNH_Type(IpAddress):
    """Custom type tIPFilterParamsForwardNH based on IpAddress"""
    defaultHexValue = "00000000"


_TIPFilterParamsForwardNH_Type.__name__ = "IpAddress"
_TIPFilterParamsForwardNH_Object = MibTableColumn
tIPFilterParamsForwardNH = _TIPFilterParamsForwardNH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 6),
    _TIPFilterParamsForwardNH_Type()
)
tIPFilterParamsForwardNH.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsForwardNH.setStatus("obsolete")


class _TIPFilterParamsForwardNHIndirect_Type(TruthValue):
    """Custom type tIPFilterParamsForwardNHIndirect based on TruthValue"""
    defaultValue = 2


_TIPFilterParamsForwardNHIndirect_Type.__name__ = "TruthValue"
_TIPFilterParamsForwardNHIndirect_Object = MibTableColumn
tIPFilterParamsForwardNHIndirect = _TIPFilterParamsForwardNHIndirect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 7),
    _TIPFilterParamsForwardNHIndirect_Type()
)
tIPFilterParamsForwardNHIndirect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsForwardNHIndirect.setStatus("obsolete")


class _TIPFilterParamsRemarkDSCP_Type(TDSCPFilterActionValue):
    """Custom type tIPFilterParamsRemarkDSCP based on TDSCPFilterActionValue"""
    defaultValue = -1


_TIPFilterParamsRemarkDSCP_Type.__name__ = "TDSCPFilterActionValue"
_TIPFilterParamsRemarkDSCP_Object = MibTableColumn
tIPFilterParamsRemarkDSCP = _TIPFilterParamsRemarkDSCP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 8),
    _TIPFilterParamsRemarkDSCP_Type()
)
tIPFilterParamsRemarkDSCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsRemarkDSCP.setStatus("obsolete")


class _TIPFilterParamsRemarkDSCPMask_Type(TDSCPFilterActionValue):
    """Custom type tIPFilterParamsRemarkDSCPMask based on TDSCPFilterActionValue"""
    defaultValue = 255


_TIPFilterParamsRemarkDSCPMask_Type.__name__ = "TDSCPFilterActionValue"
_TIPFilterParamsRemarkDSCPMask_Object = MibTableColumn
tIPFilterParamsRemarkDSCPMask = _TIPFilterParamsRemarkDSCPMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 9),
    _TIPFilterParamsRemarkDSCPMask_Type()
)
tIPFilterParamsRemarkDSCPMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsRemarkDSCPMask.setStatus("obsolete")


class _TIPFilterParamsRemarkDot1p_Type(Dot1PPriority):
    """Custom type tIPFilterParamsRemarkDot1p based on Dot1PPriority"""
    defaultValue = -1


_TIPFilterParamsRemarkDot1p_Type.__name__ = "Dot1PPriority"
_TIPFilterParamsRemarkDot1p_Object = MibTableColumn
tIPFilterParamsRemarkDot1p = _TIPFilterParamsRemarkDot1p_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 10),
    _TIPFilterParamsRemarkDot1p_Type()
)
tIPFilterParamsRemarkDot1p.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsRemarkDot1p.setStatus("obsolete")


class _TIPFilterParamsSourceIpAddr_Type(IpAddress):
    """Custom type tIPFilterParamsSourceIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_TIPFilterParamsSourceIpAddr_Type.__name__ = "IpAddress"
_TIPFilterParamsSourceIpAddr_Object = MibTableColumn
tIPFilterParamsSourceIpAddr = _TIPFilterParamsSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 11),
    _TIPFilterParamsSourceIpAddr_Type()
)
tIPFilterParamsSourceIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsSourceIpAddr.setStatus("current")


class _TIPFilterParamsSourceIpMask_Type(IpAddressPrefixLength):
    """Custom type tIPFilterParamsSourceIpMask based on IpAddressPrefixLength"""
    defaultValue = 0


_TIPFilterParamsSourceIpMask_Type.__name__ = "IpAddressPrefixLength"
_TIPFilterParamsSourceIpMask_Object = MibTableColumn
tIPFilterParamsSourceIpMask = _TIPFilterParamsSourceIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 12),
    _TIPFilterParamsSourceIpMask_Type()
)
tIPFilterParamsSourceIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsSourceIpMask.setStatus("current")


class _TIPFilterParamsDestinationIpAddr_Type(IpAddress):
    """Custom type tIPFilterParamsDestinationIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_TIPFilterParamsDestinationIpAddr_Type.__name__ = "IpAddress"
_TIPFilterParamsDestinationIpAddr_Object = MibTableColumn
tIPFilterParamsDestinationIpAddr = _TIPFilterParamsDestinationIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 13),
    _TIPFilterParamsDestinationIpAddr_Type()
)
tIPFilterParamsDestinationIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsDestinationIpAddr.setStatus("current")


class _TIPFilterParamsDestinationIpMask_Type(IpAddressPrefixLength):
    """Custom type tIPFilterParamsDestinationIpMask based on IpAddressPrefixLength"""
    defaultValue = 0


_TIPFilterParamsDestinationIpMask_Type.__name__ = "IpAddressPrefixLength"
_TIPFilterParamsDestinationIpMask_Object = MibTableColumn
tIPFilterParamsDestinationIpMask = _TIPFilterParamsDestinationIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 14),
    _TIPFilterParamsDestinationIpMask_Type()
)
tIPFilterParamsDestinationIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsDestinationIpMask.setStatus("current")


class _TIPFilterParamsProtocol_Type(TIpProtocol):
    """Custom type tIPFilterParamsProtocol based on TIpProtocol"""
    defaultValue = -1


_TIPFilterParamsProtocol_Type.__name__ = "TIpProtocol"
_TIPFilterParamsProtocol_Object = MibTableColumn
tIPFilterParamsProtocol = _TIPFilterParamsProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 15),
    _TIPFilterParamsProtocol_Type()
)
tIPFilterParamsProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsProtocol.setStatus("current")


class _TIPFilterParamsSourcePortValue1_Type(TTcpUdpPort):
    """Custom type tIPFilterParamsSourcePortValue1 based on TTcpUdpPort"""
    defaultValue = 0


_TIPFilterParamsSourcePortValue1_Type.__name__ = "TTcpUdpPort"
_TIPFilterParamsSourcePortValue1_Object = MibTableColumn
tIPFilterParamsSourcePortValue1 = _TIPFilterParamsSourcePortValue1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 16),
    _TIPFilterParamsSourcePortValue1_Type()
)
tIPFilterParamsSourcePortValue1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsSourcePortValue1.setStatus("current")


class _TIPFilterParamsSourcePortValue2_Type(TTcpUdpPort):
    """Custom type tIPFilterParamsSourcePortValue2 based on TTcpUdpPort"""
    defaultValue = 0


_TIPFilterParamsSourcePortValue2_Type.__name__ = "TTcpUdpPort"
_TIPFilterParamsSourcePortValue2_Object = MibTableColumn
tIPFilterParamsSourcePortValue2 = _TIPFilterParamsSourcePortValue2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 17),
    _TIPFilterParamsSourcePortValue2_Type()
)
tIPFilterParamsSourcePortValue2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsSourcePortValue2.setStatus("current")


class _TIPFilterParamsSourcePortOperator_Type(TOperator):
    """Custom type tIPFilterParamsSourcePortOperator based on TOperator"""
    defaultValue = 0


_TIPFilterParamsSourcePortOperator_Type.__name__ = "TOperator"
_TIPFilterParamsSourcePortOperator_Object = MibTableColumn
tIPFilterParamsSourcePortOperator = _TIPFilterParamsSourcePortOperator_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 18),
    _TIPFilterParamsSourcePortOperator_Type()
)
tIPFilterParamsSourcePortOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsSourcePortOperator.setStatus("current")


class _TIPFilterParamsDestPortValue1_Type(TTcpUdpPort):
    """Custom type tIPFilterParamsDestPortValue1 based on TTcpUdpPort"""
    defaultValue = 0


_TIPFilterParamsDestPortValue1_Type.__name__ = "TTcpUdpPort"
_TIPFilterParamsDestPortValue1_Object = MibTableColumn
tIPFilterParamsDestPortValue1 = _TIPFilterParamsDestPortValue1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 19),
    _TIPFilterParamsDestPortValue1_Type()
)
tIPFilterParamsDestPortValue1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsDestPortValue1.setStatus("current")


class _TIPFilterParamsDestPortValue2_Type(TTcpUdpPort):
    """Custom type tIPFilterParamsDestPortValue2 based on TTcpUdpPort"""
    defaultValue = 0


_TIPFilterParamsDestPortValue2_Type.__name__ = "TTcpUdpPort"
_TIPFilterParamsDestPortValue2_Object = MibTableColumn
tIPFilterParamsDestPortValue2 = _TIPFilterParamsDestPortValue2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 20),
    _TIPFilterParamsDestPortValue2_Type()
)
tIPFilterParamsDestPortValue2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsDestPortValue2.setStatus("current")


class _TIPFilterParamsDestPortOperator_Type(TOperator):
    """Custom type tIPFilterParamsDestPortOperator based on TOperator"""
    defaultValue = 0


_TIPFilterParamsDestPortOperator_Type.__name__ = "TOperator"
_TIPFilterParamsDestPortOperator_Object = MibTableColumn
tIPFilterParamsDestPortOperator = _TIPFilterParamsDestPortOperator_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 21),
    _TIPFilterParamsDestPortOperator_Type()
)
tIPFilterParamsDestPortOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsDestPortOperator.setStatus("current")


class _TIPFilterParamsDSCP_Type(TDSCPNameOrEmpty):
    """Custom type tIPFilterParamsDSCP based on TDSCPNameOrEmpty"""
    defaultHexValue = ""


_TIPFilterParamsDSCP_Type.__name__ = "TDSCPNameOrEmpty"
_TIPFilterParamsDSCP_Object = MibTableColumn
tIPFilterParamsDSCP = _TIPFilterParamsDSCP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 22),
    _TIPFilterParamsDSCP_Type()
)
tIPFilterParamsDSCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsDSCP.setStatus("current")


class _TIPFilterParamsFragment_Type(TFragmentMatch):
    """Custom type tIPFilterParamsFragment based on TFragmentMatch"""
    defaultValue = 1


_TIPFilterParamsFragment_Type.__name__ = "TFragmentMatch"
_TIPFilterParamsFragment_Object = MibTableColumn
tIPFilterParamsFragment = _TIPFilterParamsFragment_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 24),
    _TIPFilterParamsFragment_Type()
)
tIPFilterParamsFragment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsFragment.setStatus("current")


class _TIPFilterParamsOptionPresent_Type(TItemMatch):
    """Custom type tIPFilterParamsOptionPresent based on TItemMatch"""
    defaultValue = 1


_TIPFilterParamsOptionPresent_Type.__name__ = "TItemMatch"
_TIPFilterParamsOptionPresent_Object = MibTableColumn
tIPFilterParamsOptionPresent = _TIPFilterParamsOptionPresent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 25),
    _TIPFilterParamsOptionPresent_Type()
)
tIPFilterParamsOptionPresent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsOptionPresent.setStatus("current")


class _TIPFilterParamsIpOptionValue_Type(TIpOption):
    """Custom type tIPFilterParamsIpOptionValue based on TIpOption"""
    defaultValue = 0


_TIPFilterParamsIpOptionValue_Type.__name__ = "TIpOption"
_TIPFilterParamsIpOptionValue_Object = MibTableColumn
tIPFilterParamsIpOptionValue = _TIPFilterParamsIpOptionValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 26),
    _TIPFilterParamsIpOptionValue_Type()
)
tIPFilterParamsIpOptionValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsIpOptionValue.setStatus("current")


class _TIPFilterParamsIpOptionMask_Type(TIpOption):
    """Custom type tIPFilterParamsIpOptionMask based on TIpOption"""
    defaultValue = 0


_TIPFilterParamsIpOptionMask_Type.__name__ = "TIpOption"
_TIPFilterParamsIpOptionMask_Object = MibTableColumn
tIPFilterParamsIpOptionMask = _TIPFilterParamsIpOptionMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 27),
    _TIPFilterParamsIpOptionMask_Type()
)
tIPFilterParamsIpOptionMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsIpOptionMask.setStatus("current")


class _TIPFilterParamsMultipleOption_Type(TItemMatch):
    """Custom type tIPFilterParamsMultipleOption based on TItemMatch"""
    defaultValue = 1


_TIPFilterParamsMultipleOption_Type.__name__ = "TItemMatch"
_TIPFilterParamsMultipleOption_Object = MibTableColumn
tIPFilterParamsMultipleOption = _TIPFilterParamsMultipleOption_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 28),
    _TIPFilterParamsMultipleOption_Type()
)
tIPFilterParamsMultipleOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsMultipleOption.setStatus("current")


class _TIPFilterParamsTcpSyn_Type(TItemMatch):
    """Custom type tIPFilterParamsTcpSyn based on TItemMatch"""
    defaultValue = 1


_TIPFilterParamsTcpSyn_Type.__name__ = "TItemMatch"
_TIPFilterParamsTcpSyn_Object = MibTableColumn
tIPFilterParamsTcpSyn = _TIPFilterParamsTcpSyn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 29),
    _TIPFilterParamsTcpSyn_Type()
)
tIPFilterParamsTcpSyn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsTcpSyn.setStatus("current")


class _TIPFilterParamsTcpAck_Type(TItemMatch):
    """Custom type tIPFilterParamsTcpAck based on TItemMatch"""
    defaultValue = 1


_TIPFilterParamsTcpAck_Type.__name__ = "TItemMatch"
_TIPFilterParamsTcpAck_Object = MibTableColumn
tIPFilterParamsTcpAck = _TIPFilterParamsTcpAck_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 30),
    _TIPFilterParamsTcpAck_Type()
)
tIPFilterParamsTcpAck.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsTcpAck.setStatus("current")


class _TIPFilterParamsIcmpCode_Type(TIcmpCodeOrNone):
    """Custom type tIPFilterParamsIcmpCode based on TIcmpCodeOrNone"""
    defaultValue = -1


_TIPFilterParamsIcmpCode_Type.__name__ = "TIcmpCodeOrNone"
_TIPFilterParamsIcmpCode_Object = MibTableColumn
tIPFilterParamsIcmpCode = _TIPFilterParamsIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 31),
    _TIPFilterParamsIcmpCode_Type()
)
tIPFilterParamsIcmpCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsIcmpCode.setStatus("current")


class _TIPFilterParamsIcmpType_Type(TIcmpTypeOrNone):
    """Custom type tIPFilterParamsIcmpType based on TIcmpTypeOrNone"""
    defaultValue = -1


_TIPFilterParamsIcmpType_Type.__name__ = "TIcmpTypeOrNone"
_TIPFilterParamsIcmpType_Object = MibTableColumn
tIPFilterParamsIcmpType = _TIPFilterParamsIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 32),
    _TIPFilterParamsIcmpType_Type()
)
tIPFilterParamsIcmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsIcmpType.setStatus("current")


class _TIPFilterParamsCflowdSample_Type(TruthValue):
    """Custom type tIPFilterParamsCflowdSample based on TruthValue"""
    defaultValue = 2


_TIPFilterParamsCflowdSample_Type.__name__ = "TruthValue"
_TIPFilterParamsCflowdSample_Object = MibTableColumn
tIPFilterParamsCflowdSample = _TIPFilterParamsCflowdSample_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 33),
    _TIPFilterParamsCflowdSample_Type()
)
tIPFilterParamsCflowdSample.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsCflowdSample.setStatus("current")


class _TIPFilterParamsCflowdIfSample_Type(TruthValue):
    """Custom type tIPFilterParamsCflowdIfSample based on TruthValue"""
    defaultValue = 1


_TIPFilterParamsCflowdIfSample_Type.__name__ = "TruthValue"
_TIPFilterParamsCflowdIfSample_Object = MibTableColumn
tIPFilterParamsCflowdIfSample = _TIPFilterParamsCflowdIfSample_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 34),
    _TIPFilterParamsCflowdIfSample_Type()
)
tIPFilterParamsCflowdIfSample.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsCflowdIfSample.setStatus("current")


class _TIPFilterParamsForwardNHInterface_Type(DisplayString):
    """Custom type tIPFilterParamsForwardNHInterface based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TIPFilterParamsForwardNHInterface_Type.__name__ = "DisplayString"
_TIPFilterParamsForwardNHInterface_Object = MibTableColumn
tIPFilterParamsForwardNHInterface = _TIPFilterParamsForwardNHInterface_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 35),
    _TIPFilterParamsForwardNHInterface_Type()
)
tIPFilterParamsForwardNHInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsForwardNHInterface.setStatus("obsolete")
_TIPFilterParamsIngressHitCount_Type = Counter64
_TIPFilterParamsIngressHitCount_Object = MibTableColumn
tIPFilterParamsIngressHitCount = _TIPFilterParamsIngressHitCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 36),
    _TIPFilterParamsIngressHitCount_Type()
)
tIPFilterParamsIngressHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPFilterParamsIngressHitCount.setStatus("current")
_TIPFilterParamsEgressHitCount_Type = Counter64
_TIPFilterParamsEgressHitCount_Object = MibTableColumn
tIPFilterParamsEgressHitCount = _TIPFilterParamsEgressHitCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 37),
    _TIPFilterParamsEgressHitCount_Type()
)
tIPFilterParamsEgressHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPFilterParamsEgressHitCount.setStatus("current")
_TIPFilterParamsLogInstantiated_Type = TruthValue
_TIPFilterParamsLogInstantiated_Object = MibTableColumn
tIPFilterParamsLogInstantiated = _TIPFilterParamsLogInstantiated_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 38),
    _TIPFilterParamsLogInstantiated_Type()
)
tIPFilterParamsLogInstantiated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPFilterParamsLogInstantiated.setStatus("current")


class _TIPFilterParamsForwardRedPlcy_Type(TNamedItemOrEmpty):
    """Custom type tIPFilterParamsForwardRedPlcy based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TIPFilterParamsForwardRedPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TIPFilterParamsForwardRedPlcy_Object = MibTableColumn
tIPFilterParamsForwardRedPlcy = _TIPFilterParamsForwardRedPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 39),
    _TIPFilterParamsForwardRedPlcy_Type()
)
tIPFilterParamsForwardRedPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsForwardRedPlcy.setStatus("obsolete")
_TIPFilterParamsActiveDest_Type = IpAddress
_TIPFilterParamsActiveDest_Object = MibTableColumn
tIPFilterParamsActiveDest = _TIPFilterParamsActiveDest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 40),
    _TIPFilterParamsActiveDest_Type()
)
tIPFilterParamsActiveDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPFilterParamsActiveDest.setStatus("current")
_TIPFilterParamsFwdSvcId_Type = TmnxServId
_TIPFilterParamsFwdSvcId_Object = MibTableColumn
tIPFilterParamsFwdSvcId = _TIPFilterParamsFwdSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 41),
    _TIPFilterParamsFwdSvcId_Type()
)
tIPFilterParamsFwdSvcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPFilterParamsFwdSvcId.setStatus("current")


class _TIPFilterParamsFwdSapPortId_Type(TmnxPortID):
    """Custom type tIPFilterParamsFwdSapPortId based on TmnxPortID"""
    defaultValue = 0


_TIPFilterParamsFwdSapPortId_Type.__name__ = "TmnxPortID"
_TIPFilterParamsFwdSapPortId_Object = MibTableColumn
tIPFilterParamsFwdSapPortId = _TIPFilterParamsFwdSapPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 42),
    _TIPFilterParamsFwdSapPortId_Type()
)
tIPFilterParamsFwdSapPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsFwdSapPortId.setStatus("obsolete")


class _TIPFilterParamsFwdSapEncapVal_Type(TmnxEncapVal):
    """Custom type tIPFilterParamsFwdSapEncapVal based on TmnxEncapVal"""
    defaultValue = 0


_TIPFilterParamsFwdSapEncapVal_Type.__name__ = "TmnxEncapVal"
_TIPFilterParamsFwdSapEncapVal_Object = MibTableColumn
tIPFilterParamsFwdSapEncapVal = _TIPFilterParamsFwdSapEncapVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 43),
    _TIPFilterParamsFwdSapEncapVal_Type()
)
tIPFilterParamsFwdSapEncapVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsFwdSapEncapVal.setStatus("obsolete")


class _TIPFilterParamsFwdSdpBind_Type(SdpBindId):
    """Custom type tIPFilterParamsFwdSdpBind based on SdpBindId"""
    defaultHexValue = "0000000000000000"


_TIPFilterParamsFwdSdpBind_Type.__name__ = "SdpBindId"
_TIPFilterParamsFwdSdpBind_Object = MibTableColumn
tIPFilterParamsFwdSdpBind = _TIPFilterParamsFwdSdpBind_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 44),
    _TIPFilterParamsFwdSdpBind_Type()
)
tIPFilterParamsFwdSdpBind.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsFwdSdpBind.setStatus("obsolete")


class _TIPFilterParamsTimeRangeName_Type(TNamedItemOrEmpty):
    """Custom type tIPFilterParamsTimeRangeName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TIPFilterParamsTimeRangeName_Type.__name__ = "TNamedItemOrEmpty"
_TIPFilterParamsTimeRangeName_Object = MibTableColumn
tIPFilterParamsTimeRangeName = _TIPFilterParamsTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 45),
    _TIPFilterParamsTimeRangeName_Type()
)
tIPFilterParamsTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsTimeRangeName.setStatus("obsolete")
_TIPFilterParamsTimeRangeState_Type = TTimeRangeState
_TIPFilterParamsTimeRangeState_Object = MibTableColumn
tIPFilterParamsTimeRangeState = _TIPFilterParamsTimeRangeState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 46),
    _TIPFilterParamsTimeRangeState_Type()
)
tIPFilterParamsTimeRangeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPFilterParamsTimeRangeState.setStatus("obsolete")


class _TIPFilterParamsRedirectURL_Type(TmnxHttpRedirectUrl):
    """Custom type tIPFilterParamsRedirectURL based on TmnxHttpRedirectUrl"""
    defaultHexValue = ""


_TIPFilterParamsRedirectURL_Type.__name__ = "TmnxHttpRedirectUrl"
_TIPFilterParamsRedirectURL_Object = MibTableColumn
tIPFilterParamsRedirectURL = _TIPFilterParamsRedirectURL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 47),
    _TIPFilterParamsRedirectURL_Type()
)
tIPFilterParamsRedirectURL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsRedirectURL.setStatus("obsolete")
_TIPFilterParamsSrcIpFullMask_Type = IpAddress
_TIPFilterParamsSrcIpFullMask_Object = MibTableColumn
tIPFilterParamsSrcIpFullMask = _TIPFilterParamsSrcIpFullMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 48),
    _TIPFilterParamsSrcIpFullMask_Type()
)
tIPFilterParamsSrcIpFullMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsSrcIpFullMask.setStatus("current")
_TIPFilterParamsDestIpFullMask_Type = IpAddress
_TIPFilterParamsDestIpFullMask_Object = MibTableColumn
tIPFilterParamsDestIpFullMask = _TIPFilterParamsDestIpFullMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 49),
    _TIPFilterParamsDestIpFullMask_Type()
)
tIPFilterParamsDestIpFullMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsDestIpFullMask.setStatus("current")
_TIPFilterParamsIngrHitByteCount_Type = Counter64
_TIPFilterParamsIngrHitByteCount_Object = MibTableColumn
tIPFilterParamsIngrHitByteCount = _TIPFilterParamsIngrHitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 50),
    _TIPFilterParamsIngrHitByteCount_Type()
)
tIPFilterParamsIngrHitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPFilterParamsIngrHitByteCount.setStatus("current")
_TIPFilterParamsEgrHitByteCount_Type = Counter64
_TIPFilterParamsEgrHitByteCount_Object = MibTableColumn
tIPFilterParamsEgrHitByteCount = _TIPFilterParamsEgrHitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 51),
    _TIPFilterParamsEgrHitByteCount_Type()
)
tIPFilterParamsEgrHitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPFilterParamsEgrHitByteCount.setStatus("current")


class _TIPFilterParamsFwdRtrId_Type(TmnxVRtrIDOrZero):
    """Custom type tIPFilterParamsFwdRtrId based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TIPFilterParamsFwdRtrId_Type.__name__ = "TmnxVRtrIDOrZero"
_TIPFilterParamsFwdRtrId_Object = MibTableColumn
tIPFilterParamsFwdRtrId = _TIPFilterParamsFwdRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 52),
    _TIPFilterParamsFwdRtrId_Type()
)
tIPFilterParamsFwdRtrId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsFwdRtrId.setStatus("obsolete")


class _TIPFilterParamsSrcRouteOption_Type(TItemMatch):
    """Custom type tIPFilterParamsSrcRouteOption based on TItemMatch"""
    defaultValue = 1


_TIPFilterParamsSrcRouteOption_Type.__name__ = "TItemMatch"
_TIPFilterParamsSrcRouteOption_Object = MibTableColumn
tIPFilterParamsSrcRouteOption = _TIPFilterParamsSrcRouteOption_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 53),
    _TIPFilterParamsSrcRouteOption_Type()
)
tIPFilterParamsSrcRouteOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsSrcRouteOption.setStatus("current")


class _TIPFilterParamsSrcIpPrefixList_Type(TNamedItemOrEmpty):
    """Custom type tIPFilterParamsSrcIpPrefixList based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TIPFilterParamsSrcIpPrefixList_Type.__name__ = "TNamedItemOrEmpty"
_TIPFilterParamsSrcIpPrefixList_Object = MibTableColumn
tIPFilterParamsSrcIpPrefixList = _TIPFilterParamsSrcIpPrefixList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 54),
    _TIPFilterParamsSrcIpPrefixList_Type()
)
tIPFilterParamsSrcIpPrefixList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsSrcIpPrefixList.setStatus("current")


class _TIPFilterParamsDstIpPrefixList_Type(TNamedItemOrEmpty):
    """Custom type tIPFilterParamsDstIpPrefixList based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TIPFilterParamsDstIpPrefixList_Type.__name__ = "TNamedItemOrEmpty"
_TIPFilterParamsDstIpPrefixList_Object = MibTableColumn
tIPFilterParamsDstIpPrefixList = _TIPFilterParamsDstIpPrefixList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 55),
    _TIPFilterParamsDstIpPrefixList_Type()
)
tIPFilterParamsDstIpPrefixList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsDstIpPrefixList.setStatus("current")


class _TIPFilterParamsPortSelector_Type(TFltrPortSelector):
    """Custom type tIPFilterParamsPortSelector based on TFltrPortSelector"""
    defaultValue = 0


_TIPFilterParamsPortSelector_Type.__name__ = "TFltrPortSelector"
_TIPFilterParamsPortSelector_Object = MibTableColumn
tIPFilterParamsPortSelector = _TIPFilterParamsPortSelector_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 56),
    _TIPFilterParamsPortSelector_Type()
)
tIPFilterParamsPortSelector.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsPortSelector.setStatus("current")


class _TIPFilterParamsSrcPortList_Type(TNamedItemOrEmpty):
    """Custom type tIPFilterParamsSrcPortList based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TIPFilterParamsSrcPortList_Type.__name__ = "TNamedItemOrEmpty"
_TIPFilterParamsSrcPortList_Object = MibTableColumn
tIPFilterParamsSrcPortList = _TIPFilterParamsSrcPortList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 57),
    _TIPFilterParamsSrcPortList_Type()
)
tIPFilterParamsSrcPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsSrcPortList.setStatus("current")


class _TIPFilterParamsDstPortList_Type(TNamedItemOrEmpty):
    """Custom type tIPFilterParamsDstPortList based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TIPFilterParamsDstPortList_Type.__name__ = "TNamedItemOrEmpty"
_TIPFilterParamsDstPortList_Object = MibTableColumn
tIPFilterParamsDstPortList = _TIPFilterParamsDstPortList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 58),
    _TIPFilterParamsDstPortList_Type()
)
tIPFilterParamsDstPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsDstPortList.setStatus("current")


class _TIPFilterParamsRdirAllwRadOvrd_Type(TruthValue):
    """Custom type tIPFilterParamsRdirAllwRadOvrd based on TruthValue"""
    defaultValue = 2


_TIPFilterParamsRdirAllwRadOvrd_Type.__name__ = "TruthValue"
_TIPFilterParamsRdirAllwRadOvrd_Object = MibTableColumn
tIPFilterParamsRdirAllwRadOvrd = _TIPFilterParamsRdirAllwRadOvrd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 59),
    _TIPFilterParamsRdirAllwRadOvrd_Type()
)
tIPFilterParamsRdirAllwRadOvrd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsRdirAllwRadOvrd.setStatus("obsolete")


class _TIPFilterParamsNatPolicyName_Type(TNamedItemOrEmpty):
    """Custom type tIPFilterParamsNatPolicyName based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TIPFilterParamsNatPolicyName_Type.__name__ = "TNamedItemOrEmpty"
_TIPFilterParamsNatPolicyName_Object = MibTableColumn
tIPFilterParamsNatPolicyName = _TIPFilterParamsNatPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 60),
    _TIPFilterParamsNatPolicyName_Type()
)
tIPFilterParamsNatPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsNatPolicyName.setStatus("obsolete")


class _TIPFilterParamsFwdLsp_Type(TmnxVRtrMplsLspID):
    """Custom type tIPFilterParamsFwdLsp based on TmnxVRtrMplsLspID"""
    defaultValue = 0


_TIPFilterParamsFwdLsp_Type.__name__ = "TmnxVRtrMplsLspID"
_TIPFilterParamsFwdLsp_Object = MibTableColumn
tIPFilterParamsFwdLsp = _TIPFilterParamsFwdLsp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 61),
    _TIPFilterParamsFwdLsp_Type()
)
tIPFilterParamsFwdLsp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsFwdLsp.setStatus("obsolete")


class _TIPFilterParamsFwdLspRtrId_Type(TmnxVRtrIDOrZero):
    """Custom type tIPFilterParamsFwdLspRtrId based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TIPFilterParamsFwdLspRtrId_Type.__name__ = "TmnxVRtrIDOrZero"
_TIPFilterParamsFwdLspRtrId_Object = MibTableColumn
tIPFilterParamsFwdLspRtrId = _TIPFilterParamsFwdLspRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 62),
    _TIPFilterParamsFwdLspRtrId_Type()
)
tIPFilterParamsFwdLspRtrId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsFwdLspRtrId.setStatus("obsolete")


class _TIPFilterParamsIpSelector_Type(TFltrMatchIpSelector):
    """Custom type tIPFilterParamsIpSelector based on TFltrMatchIpSelector"""
    defaultValue = 0


_TIPFilterParamsIpSelector_Type.__name__ = "TFltrMatchIpSelector"
_TIPFilterParamsIpSelector_Object = MibTableColumn
tIPFilterParamsIpSelector = _TIPFilterParamsIpSelector_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 2, 1, 63),
    _TIPFilterParamsIpSelector_Type()
)
tIPFilterParamsIpSelector.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsIpSelector.setStatus("current")
_TMacFilterTable_Object = MibTable
tMacFilterTable = _TMacFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 3)
)
if mibBuilder.loadTexts:
    tMacFilterTable.setStatus("current")
_TMacFilterEntry_Object = MibTableRow
tMacFilterEntry = _TMacFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 3, 1)
)
tMacFilterEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tMacFilterId"),
)
if mibBuilder.loadTexts:
    tMacFilterEntry.setStatus("current")
_TMacFilterId_Type = TAnyFilterID
_TMacFilterId_Object = MibTableColumn
tMacFilterId = _TMacFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 3, 1, 1),
    _TMacFilterId_Type()
)
tMacFilterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMacFilterId.setStatus("current")
_TMacFilterRowStatus_Type = RowStatus
_TMacFilterRowStatus_Object = MibTableColumn
tMacFilterRowStatus = _TMacFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 3, 1, 2),
    _TMacFilterRowStatus_Type()
)
tMacFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterRowStatus.setStatus("current")


class _TMacFilterScope_Type(TFilterScope):
    """Custom type tMacFilterScope based on TFilterScope"""
    defaultValue = 2


_TMacFilterScope_Type.__name__ = "TFilterScope"
_TMacFilterScope_Object = MibTableColumn
tMacFilterScope = _TMacFilterScope_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 3, 1, 3),
    _TMacFilterScope_Type()
)
tMacFilterScope.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterScope.setStatus("current")


class _TMacFilterDescription_Type(TItemDescription):
    """Custom type tMacFilterDescription based on TItemDescription"""
    defaultHexValue = ""


_TMacFilterDescription_Type.__name__ = "TItemDescription"
_TMacFilterDescription_Object = MibTableColumn
tMacFilterDescription = _TMacFilterDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 3, 1, 4),
    _TMacFilterDescription_Type()
)
tMacFilterDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterDescription.setStatus("current")


class _TMacFilterDefaultAction_Type(TFilterAction):
    """Custom type tMacFilterDefaultAction based on TFilterAction"""
    defaultValue = 1


_TMacFilterDefaultAction_Type.__name__ = "TFilterAction"
_TMacFilterDefaultAction_Object = MibTableColumn
tMacFilterDefaultAction = _TMacFilterDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 3, 1, 5),
    _TMacFilterDefaultAction_Type()
)
tMacFilterDefaultAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterDefaultAction.setStatus("current")


class _TMacFilterType_Type(TMacFilterType):
    """Custom type tMacFilterType based on TMacFilterType"""
    defaultValue = 1


_TMacFilterType_Type.__name__ = "TMacFilterType"
_TMacFilterType_Object = MibTableColumn
tMacFilterType = _TMacFilterType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 3, 1, 6),
    _TMacFilterType_Type()
)
tMacFilterType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterType.setStatus("current")


class _TMacFilterName_Type(TLNamedItemOrEmpty):
    """Custom type tMacFilterName based on TLNamedItemOrEmpty"""
    defaultHexValue = ""


_TMacFilterName_Type.__name__ = "TLNamedItemOrEmpty"
_TMacFilterName_Object = MibTableColumn
tMacFilterName = _TMacFilterName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 3, 1, 7),
    _TMacFilterName_Type()
)
tMacFilterName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterName.setStatus("current")
_TMacFilterParamsTable_Object = MibTable
tMacFilterParamsTable = _TMacFilterParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4)
)
if mibBuilder.loadTexts:
    tMacFilterParamsTable.setStatus("current")
_TMacFilterParamsEntry_Object = MibTableRow
tMacFilterParamsEntry = _TMacFilterParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1)
)
tMacFilterParamsEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tMacFilterId"),
    (0, "TIMETRA-FILTER-MIB", "tMacFilterParamsIndex"),
)
if mibBuilder.loadTexts:
    tMacFilterParamsEntry.setStatus("current")
_TMacFilterParamsIndex_Type = TEntryId
_TMacFilterParamsIndex_Object = MibTableColumn
tMacFilterParamsIndex = _TMacFilterParamsIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 1),
    _TMacFilterParamsIndex_Type()
)
tMacFilterParamsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMacFilterParamsIndex.setStatus("current")
_TMacFilterParamsRowStatus_Type = RowStatus
_TMacFilterParamsRowStatus_Object = MibTableColumn
tMacFilterParamsRowStatus = _TMacFilterParamsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 2),
    _TMacFilterParamsRowStatus_Type()
)
tMacFilterParamsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsRowStatus.setStatus("current")


class _TMacFilterParamsLogId_Type(TFilterLogId):
    """Custom type tMacFilterParamsLogId based on TFilterLogId"""
    defaultValue = 0


_TMacFilterParamsLogId_Type.__name__ = "TFilterLogId"
_TMacFilterParamsLogId_Object = MibTableColumn
tMacFilterParamsLogId = _TMacFilterParamsLogId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 3),
    _TMacFilterParamsLogId_Type()
)
tMacFilterParamsLogId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsLogId.setStatus("current")


class _TMacFilterParamsDescription_Type(TItemDescription):
    """Custom type tMacFilterParamsDescription based on TItemDescription"""
    defaultHexValue = ""


_TMacFilterParamsDescription_Type.__name__ = "TItemDescription"
_TMacFilterParamsDescription_Object = MibTableColumn
tMacFilterParamsDescription = _TMacFilterParamsDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 4),
    _TMacFilterParamsDescription_Type()
)
tMacFilterParamsDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsDescription.setStatus("current")


class _TMacFilterParamsAction_Type(TFilterActionOrDefault):
    """Custom type tMacFilterParamsAction based on TFilterActionOrDefault"""
    defaultValue = 30


_TMacFilterParamsAction_Type.__name__ = "TFilterActionOrDefault"
_TMacFilterParamsAction_Object = MibTableColumn
tMacFilterParamsAction = _TMacFilterParamsAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 5),
    _TMacFilterParamsAction_Type()
)
tMacFilterParamsAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsAction.setStatus("obsolete")


class _TMacFilterParamsFrameType_Type(TFrameType):
    """Custom type tMacFilterParamsFrameType based on TFrameType"""
    defaultValue = 0


_TMacFilterParamsFrameType_Type.__name__ = "TFrameType"
_TMacFilterParamsFrameType_Object = MibTableColumn
tMacFilterParamsFrameType = _TMacFilterParamsFrameType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 6),
    _TMacFilterParamsFrameType_Type()
)
tMacFilterParamsFrameType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsFrameType.setStatus("current")


class _TMacFilterParamsSrcMAC_Type(MacAddress):
    """Custom type tMacFilterParamsSrcMAC based on MacAddress"""
    defaultHexValue = "000000000000"


_TMacFilterParamsSrcMAC_Type.__name__ = "MacAddress"
_TMacFilterParamsSrcMAC_Object = MibTableColumn
tMacFilterParamsSrcMAC = _TMacFilterParamsSrcMAC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 8),
    _TMacFilterParamsSrcMAC_Type()
)
tMacFilterParamsSrcMAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsSrcMAC.setStatus("current")


class _TMacFilterParamsSrcMACMask_Type(MacAddress):
    """Custom type tMacFilterParamsSrcMACMask based on MacAddress"""
    defaultHexValue = "000000000000"


_TMacFilterParamsSrcMACMask_Type.__name__ = "MacAddress"
_TMacFilterParamsSrcMACMask_Object = MibTableColumn
tMacFilterParamsSrcMACMask = _TMacFilterParamsSrcMACMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 9),
    _TMacFilterParamsSrcMACMask_Type()
)
tMacFilterParamsSrcMACMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsSrcMACMask.setStatus("current")


class _TMacFilterParamsDstMAC_Type(MacAddress):
    """Custom type tMacFilterParamsDstMAC based on MacAddress"""
    defaultHexValue = "000000000000"


_TMacFilterParamsDstMAC_Type.__name__ = "MacAddress"
_TMacFilterParamsDstMAC_Object = MibTableColumn
tMacFilterParamsDstMAC = _TMacFilterParamsDstMAC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 10),
    _TMacFilterParamsDstMAC_Type()
)
tMacFilterParamsDstMAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsDstMAC.setStatus("current")


class _TMacFilterParamsDstMACMask_Type(MacAddress):
    """Custom type tMacFilterParamsDstMACMask based on MacAddress"""
    defaultHexValue = "000000000000"


_TMacFilterParamsDstMACMask_Type.__name__ = "MacAddress"
_TMacFilterParamsDstMACMask_Object = MibTableColumn
tMacFilterParamsDstMACMask = _TMacFilterParamsDstMACMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 11),
    _TMacFilterParamsDstMACMask_Type()
)
tMacFilterParamsDstMACMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsDstMACMask.setStatus("current")


class _TMacFilterParamsDot1pValue_Type(Dot1PPriority):
    """Custom type tMacFilterParamsDot1pValue based on Dot1PPriority"""
    defaultValue = -1


_TMacFilterParamsDot1pValue_Type.__name__ = "Dot1PPriority"
_TMacFilterParamsDot1pValue_Object = MibTableColumn
tMacFilterParamsDot1pValue = _TMacFilterParamsDot1pValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 12),
    _TMacFilterParamsDot1pValue_Type()
)
tMacFilterParamsDot1pValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsDot1pValue.setStatus("current")


class _TMacFilterParamsDot1pMask_Type(Dot1PPriority):
    """Custom type tMacFilterParamsDot1pMask based on Dot1PPriority"""
    defaultValue = 0

    subtypeSpec = Dot1PPriority.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TMacFilterParamsDot1pMask_Type.__name__ = "Dot1PPriority"
_TMacFilterParamsDot1pMask_Object = MibTableColumn
tMacFilterParamsDot1pMask = _TMacFilterParamsDot1pMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 13),
    _TMacFilterParamsDot1pMask_Type()
)
tMacFilterParamsDot1pMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsDot1pMask.setStatus("current")


class _TMacFilterParamsEtherType_Type(Integer32):
    """Custom type tMacFilterParamsEtherType based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1536, 65535),
    )


_TMacFilterParamsEtherType_Type.__name__ = "Integer32"
_TMacFilterParamsEtherType_Object = MibTableColumn
tMacFilterParamsEtherType = _TMacFilterParamsEtherType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 14),
    _TMacFilterParamsEtherType_Type()
)
tMacFilterParamsEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsEtherType.setStatus("current")


class _TMacFilterParamsDsap_Type(ServiceAccessPoint):
    """Custom type tMacFilterParamsDsap based on ServiceAccessPoint"""
    defaultValue = -1


_TMacFilterParamsDsap_Type.__name__ = "ServiceAccessPoint"
_TMacFilterParamsDsap_Object = MibTableColumn
tMacFilterParamsDsap = _TMacFilterParamsDsap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 15),
    _TMacFilterParamsDsap_Type()
)
tMacFilterParamsDsap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsDsap.setStatus("current")


class _TMacFilterParamsDsapMask_Type(ServiceAccessPoint):
    """Custom type tMacFilterParamsDsapMask based on ServiceAccessPoint"""
    defaultValue = -1


_TMacFilterParamsDsapMask_Type.__name__ = "ServiceAccessPoint"
_TMacFilterParamsDsapMask_Object = MibTableColumn
tMacFilterParamsDsapMask = _TMacFilterParamsDsapMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 16),
    _TMacFilterParamsDsapMask_Type()
)
tMacFilterParamsDsapMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsDsapMask.setStatus("current")


class _TMacFilterParamsSsap_Type(ServiceAccessPoint):
    """Custom type tMacFilterParamsSsap based on ServiceAccessPoint"""
    defaultValue = -1


_TMacFilterParamsSsap_Type.__name__ = "ServiceAccessPoint"
_TMacFilterParamsSsap_Object = MibTableColumn
tMacFilterParamsSsap = _TMacFilterParamsSsap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 17),
    _TMacFilterParamsSsap_Type()
)
tMacFilterParamsSsap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsSsap.setStatus("current")


class _TMacFilterParamsSsapMask_Type(ServiceAccessPoint):
    """Custom type tMacFilterParamsSsapMask based on ServiceAccessPoint"""
    defaultValue = -1


_TMacFilterParamsSsapMask_Type.__name__ = "ServiceAccessPoint"
_TMacFilterParamsSsapMask_Object = MibTableColumn
tMacFilterParamsSsapMask = _TMacFilterParamsSsapMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 18),
    _TMacFilterParamsSsapMask_Type()
)
tMacFilterParamsSsapMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsSsapMask.setStatus("current")


class _TMacFilterParamsSnapPid_Type(Integer32):
    """Custom type tMacFilterParamsSnapPid based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )


_TMacFilterParamsSnapPid_Type.__name__ = "Integer32"
_TMacFilterParamsSnapPid_Object = MibTableColumn
tMacFilterParamsSnapPid = _TMacFilterParamsSnapPid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 19),
    _TMacFilterParamsSnapPid_Type()
)
tMacFilterParamsSnapPid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsSnapPid.setStatus("current")


class _TMacFilterParamsSnapOui_Type(Integer32):
    """Custom type tMacFilterParamsSnapOui based on Integer32"""
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
        *(("off", 1),
          ("zero", 2),
          ("nonZero", 3))
    )


_TMacFilterParamsSnapOui_Type.__name__ = "Integer32"
_TMacFilterParamsSnapOui_Object = MibTableColumn
tMacFilterParamsSnapOui = _TMacFilterParamsSnapOui_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 20),
    _TMacFilterParamsSnapOui_Type()
)
tMacFilterParamsSnapOui.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsSnapOui.setStatus("current")
_TMacFilterParamsIngressHitCount_Type = Counter64
_TMacFilterParamsIngressHitCount_Object = MibTableColumn
tMacFilterParamsIngressHitCount = _TMacFilterParamsIngressHitCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 21),
    _TMacFilterParamsIngressHitCount_Type()
)
tMacFilterParamsIngressHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMacFilterParamsIngressHitCount.setStatus("current")
_TMacFilterParamsEgressHitCount_Type = Counter64
_TMacFilterParamsEgressHitCount_Object = MibTableColumn
tMacFilterParamsEgressHitCount = _TMacFilterParamsEgressHitCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 22),
    _TMacFilterParamsEgressHitCount_Type()
)
tMacFilterParamsEgressHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMacFilterParamsEgressHitCount.setStatus("current")
_TMacFilterParamsLogInstantiated_Type = TruthValue
_TMacFilterParamsLogInstantiated_Object = MibTableColumn
tMacFilterParamsLogInstantiated = _TMacFilterParamsLogInstantiated_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 23),
    _TMacFilterParamsLogInstantiated_Type()
)
tMacFilterParamsLogInstantiated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMacFilterParamsLogInstantiated.setStatus("current")
_TMacFilterParamsFwdSvcId_Type = TmnxServId
_TMacFilterParamsFwdSvcId_Object = MibTableColumn
tMacFilterParamsFwdSvcId = _TMacFilterParamsFwdSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 24),
    _TMacFilterParamsFwdSvcId_Type()
)
tMacFilterParamsFwdSvcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMacFilterParamsFwdSvcId.setStatus("current")


class _TMacFilterParamsFwdSapPortId_Type(TmnxPortID):
    """Custom type tMacFilterParamsFwdSapPortId based on TmnxPortID"""
    defaultValue = 0


_TMacFilterParamsFwdSapPortId_Type.__name__ = "TmnxPortID"
_TMacFilterParamsFwdSapPortId_Object = MibTableColumn
tMacFilterParamsFwdSapPortId = _TMacFilterParamsFwdSapPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 25),
    _TMacFilterParamsFwdSapPortId_Type()
)
tMacFilterParamsFwdSapPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsFwdSapPortId.setStatus("obsolete")


class _TMacFilterParamsFwdSapEncapVal_Type(TmnxEncapVal):
    """Custom type tMacFilterParamsFwdSapEncapVal based on TmnxEncapVal"""
    defaultValue = 0


_TMacFilterParamsFwdSapEncapVal_Type.__name__ = "TmnxEncapVal"
_TMacFilterParamsFwdSapEncapVal_Object = MibTableColumn
tMacFilterParamsFwdSapEncapVal = _TMacFilterParamsFwdSapEncapVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 26),
    _TMacFilterParamsFwdSapEncapVal_Type()
)
tMacFilterParamsFwdSapEncapVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsFwdSapEncapVal.setStatus("obsolete")


class _TMacFilterParamsFwdSdpBind_Type(SdpBindId):
    """Custom type tMacFilterParamsFwdSdpBind based on SdpBindId"""
    defaultHexValue = "0000000000000000"


_TMacFilterParamsFwdSdpBind_Type.__name__ = "SdpBindId"
_TMacFilterParamsFwdSdpBind_Object = MibTableColumn
tMacFilterParamsFwdSdpBind = _TMacFilterParamsFwdSdpBind_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 27),
    _TMacFilterParamsFwdSdpBind_Type()
)
tMacFilterParamsFwdSdpBind.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsFwdSdpBind.setStatus("obsolete")


class _TMacFilterParamsTimeRangeName_Type(TNamedItemOrEmpty):
    """Custom type tMacFilterParamsTimeRangeName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TMacFilterParamsTimeRangeName_Type.__name__ = "TNamedItemOrEmpty"
_TMacFilterParamsTimeRangeName_Object = MibTableColumn
tMacFilterParamsTimeRangeName = _TMacFilterParamsTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 28),
    _TMacFilterParamsTimeRangeName_Type()
)
tMacFilterParamsTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsTimeRangeName.setStatus("obsolete")
_TMacFilterParamsTimeRangeState_Type = TTimeRangeState
_TMacFilterParamsTimeRangeState_Object = MibTableColumn
tMacFilterParamsTimeRangeState = _TMacFilterParamsTimeRangeState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 29),
    _TMacFilterParamsTimeRangeState_Type()
)
tMacFilterParamsTimeRangeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMacFilterParamsTimeRangeState.setStatus("obsolete")


class _TMacFilterParamsRedirectURL_Type(TmnxHttpRedirectUrl):
    """Custom type tMacFilterParamsRedirectURL based on TmnxHttpRedirectUrl"""
    defaultHexValue = ""


_TMacFilterParamsRedirectURL_Type.__name__ = "TmnxHttpRedirectUrl"
_TMacFilterParamsRedirectURL_Object = MibTableColumn
tMacFilterParamsRedirectURL = _TMacFilterParamsRedirectURL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 30),
    _TMacFilterParamsRedirectURL_Type()
)
tMacFilterParamsRedirectURL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsRedirectURL.setStatus("obsolete")
_TMacFilterParamsIngrHitByteCount_Type = Counter64
_TMacFilterParamsIngrHitByteCount_Object = MibTableColumn
tMacFilterParamsIngrHitByteCount = _TMacFilterParamsIngrHitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 31),
    _TMacFilterParamsIngrHitByteCount_Type()
)
tMacFilterParamsIngrHitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMacFilterParamsIngrHitByteCount.setStatus("current")
_TMacFilterParamsEgrHitByteCount_Type = Counter64
_TMacFilterParamsEgrHitByteCount_Object = MibTableColumn
tMacFilterParamsEgrHitByteCount = _TMacFilterParamsEgrHitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 32),
    _TMacFilterParamsEgrHitByteCount_Type()
)
tMacFilterParamsEgrHitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMacFilterParamsEgrHitByteCount.setStatus("current")


class _TMacFilterParamsLowISID_Type(SvcISID):
    """Custom type tMacFilterParamsLowISID based on SvcISID"""
    defaultValue = -1


_TMacFilterParamsLowISID_Type.__name__ = "SvcISID"
_TMacFilterParamsLowISID_Object = MibTableColumn
tMacFilterParamsLowISID = _TMacFilterParamsLowISID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 33),
    _TMacFilterParamsLowISID_Type()
)
tMacFilterParamsLowISID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsLowISID.setStatus("current")


class _TMacFilterParamsHighISID_Type(SvcISID):
    """Custom type tMacFilterParamsHighISID based on SvcISID"""
    defaultValue = -1


_TMacFilterParamsHighISID_Type.__name__ = "SvcISID"
_TMacFilterParamsHighISID_Object = MibTableColumn
tMacFilterParamsHighISID = _TMacFilterParamsHighISID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 34),
    _TMacFilterParamsHighISID_Type()
)
tMacFilterParamsHighISID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsHighISID.setStatus("current")


class _TMacFilterParamsInnerTagValue_Type(QTagFullRangeOrNone):
    """Custom type tMacFilterParamsInnerTagValue based on QTagFullRangeOrNone"""
    defaultValue = -1


_TMacFilterParamsInnerTagValue_Type.__name__ = "QTagFullRangeOrNone"
_TMacFilterParamsInnerTagValue_Object = MibTableColumn
tMacFilterParamsInnerTagValue = _TMacFilterParamsInnerTagValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 35),
    _TMacFilterParamsInnerTagValue_Type()
)
tMacFilterParamsInnerTagValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsInnerTagValue.setStatus("current")


class _TMacFilterParamsInnerTagMask_Type(QTagFullRange):
    """Custom type tMacFilterParamsInnerTagMask based on QTagFullRange"""
    defaultValue = 4095

    subtypeSpec = QTagFullRange.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_TMacFilterParamsInnerTagMask_Type.__name__ = "QTagFullRange"
_TMacFilterParamsInnerTagMask_Object = MibTableColumn
tMacFilterParamsInnerTagMask = _TMacFilterParamsInnerTagMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 36),
    _TMacFilterParamsInnerTagMask_Type()
)
tMacFilterParamsInnerTagMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsInnerTagMask.setStatus("current")


class _TMacFilterParamsOuterTagValue_Type(QTagFullRangeOrNone):
    """Custom type tMacFilterParamsOuterTagValue based on QTagFullRangeOrNone"""
    defaultValue = -1


_TMacFilterParamsOuterTagValue_Type.__name__ = "QTagFullRangeOrNone"
_TMacFilterParamsOuterTagValue_Object = MibTableColumn
tMacFilterParamsOuterTagValue = _TMacFilterParamsOuterTagValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 37),
    _TMacFilterParamsOuterTagValue_Type()
)
tMacFilterParamsOuterTagValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsOuterTagValue.setStatus("current")


class _TMacFilterParamsOuterTagMask_Type(QTagFullRange):
    """Custom type tMacFilterParamsOuterTagMask based on QTagFullRange"""
    defaultValue = 4095

    subtypeSpec = QTagFullRange.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_TMacFilterParamsOuterTagMask_Type.__name__ = "QTagFullRange"
_TMacFilterParamsOuterTagMask_Object = MibTableColumn
tMacFilterParamsOuterTagMask = _TMacFilterParamsOuterTagMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 38),
    _TMacFilterParamsOuterTagMask_Type()
)
tMacFilterParamsOuterTagMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsOuterTagMask.setStatus("current")


class _TMacFilterParamsEsi_Type(TFilterEsi):
    """Custom type tMacFilterParamsEsi based on TFilterEsi"""
    defaultHexValue = "00000000000000000000"


_TMacFilterParamsEsi_Type.__name__ = "TFilterEsi"
_TMacFilterParamsEsi_Object = MibTableColumn
tMacFilterParamsEsi = _TMacFilterParamsEsi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 39),
    _TMacFilterParamsEsi_Type()
)
tMacFilterParamsEsi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsEsi.setStatus("obsolete")


class _TMacFilterParamsFwdEsiSvcId_Type(TmnxServId):
    """Custom type tMacFilterParamsFwdEsiSvcId based on TmnxServId"""
    defaultValue = 0


_TMacFilterParamsFwdEsiSvcId_Type.__name__ = "TmnxServId"
_TMacFilterParamsFwdEsiSvcId_Object = MibTableColumn
tMacFilterParamsFwdEsiSvcId = _TMacFilterParamsFwdEsiSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 40),
    _TMacFilterParamsFwdEsiSvcId_Type()
)
tMacFilterParamsFwdEsiSvcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsFwdEsiSvcId.setStatus("obsolete")


class _TMacFilterParamsPbrDwnActOvr_Type(TFilterPbrDownActionOvr):
    """Custom type tMacFilterParamsPbrDwnActOvr based on TFilterPbrDownActionOvr"""
    defaultValue = 0


_TMacFilterParamsPbrDwnActOvr_Type.__name__ = "TFilterPbrDownActionOvr"
_TMacFilterParamsPbrDwnActOvr_Object = MibTableColumn
tMacFilterParamsPbrDwnActOvr = _TMacFilterParamsPbrDwnActOvr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 41),
    _TMacFilterParamsPbrDwnActOvr_Type()
)
tMacFilterParamsPbrDwnActOvr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsPbrDwnActOvr.setStatus("current")


class _TMacFilterParamsStickyDst_Type(Integer32):
    """Custom type tMacFilterParamsStickyDst based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )


_TMacFilterParamsStickyDst_Type.__name__ = "Integer32"
_TMacFilterParamsStickyDst_Object = MibTableColumn
tMacFilterParamsStickyDst = _TMacFilterParamsStickyDst_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 42),
    _TMacFilterParamsStickyDst_Type()
)
tMacFilterParamsStickyDst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsStickyDst.setStatus("current")
if mibBuilder.loadTexts:
    tMacFilterParamsStickyDst.setUnits("seconds")


class _TMacFilterParamsHoldRemain_Type(Integer32):
    """Custom type tMacFilterParamsHoldRemain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TMacFilterParamsHoldRemain_Type.__name__ = "Integer32"
_TMacFilterParamsHoldRemain_Object = MibTableColumn
tMacFilterParamsHoldRemain = _TMacFilterParamsHoldRemain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 43),
    _TMacFilterParamsHoldRemain_Type()
)
tMacFilterParamsHoldRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMacFilterParamsHoldRemain.setStatus("current")
_TMacFilterParamsDownloadAct_Type = TFilterDownloadedAction
_TMacFilterParamsDownloadAct_Object = MibTableColumn
tMacFilterParamsDownloadAct = _TMacFilterParamsDownloadAct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 44),
    _TMacFilterParamsDownloadAct_Type()
)
tMacFilterParamsDownloadAct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMacFilterParamsDownloadAct.setStatus("current")


class _TMacFilterParamsCollectStats_Type(TruthValue):
    """Custom type tMacFilterParamsCollectStats based on TruthValue"""
    defaultValue = 2


_TMacFilterParamsCollectStats_Type.__name__ = "TruthValue"
_TMacFilterParamsCollectStats_Object = MibTableColumn
tMacFilterParamsCollectStats = _TMacFilterParamsCollectStats_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 4, 1, 45),
    _TMacFilterParamsCollectStats_Type()
)
tMacFilterParamsCollectStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFilterParamsCollectStats.setStatus("current")
_TFilterLogTable_Object = MibTable
tFilterLogTable = _TFilterLogTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 5)
)
if mibBuilder.loadTexts:
    tFilterLogTable.setStatus("current")
_TFilterLogEntry_Object = MibTableRow
tFilterLogEntry = _TFilterLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 5, 1)
)
tFilterLogEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tFilterLogId"),
)
if mibBuilder.loadTexts:
    tFilterLogEntry.setStatus("current")
_TFilterLogId_Type = TFilterLogId
_TFilterLogId_Object = MibTableColumn
tFilterLogId = _TFilterLogId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 5, 1, 1),
    _TFilterLogId_Type()
)
tFilterLogId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterLogId.setStatus("current")
_TFilterLogRowStatus_Type = RowStatus
_TFilterLogRowStatus_Object = MibTableColumn
tFilterLogRowStatus = _TFilterLogRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 5, 1, 2),
    _TFilterLogRowStatus_Type()
)
tFilterLogRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterLogRowStatus.setStatus("current")


class _TFilterLogDestination_Type(TFilterLogDestination):
    """Custom type tFilterLogDestination based on TFilterLogDestination"""
    defaultValue = 1


_TFilterLogDestination_Type.__name__ = "TFilterLogDestination"
_TFilterLogDestination_Object = MibTableColumn
tFilterLogDestination = _TFilterLogDestination_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 5, 1, 3),
    _TFilterLogDestination_Type()
)
tFilterLogDestination.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterLogDestination.setStatus("current")


class _TFilterLogDescription_Type(TItemDescription):
    """Custom type tFilterLogDescription based on TItemDescription"""
    defaultHexValue = ""


_TFilterLogDescription_Type.__name__ = "TItemDescription"
_TFilterLogDescription_Object = MibTableColumn
tFilterLogDescription = _TFilterLogDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 5, 1, 4),
    _TFilterLogDescription_Type()
)
tFilterLogDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterLogDescription.setStatus("current")


class _TFilterLogMaxNumEntries_Type(Unsigned32):
    """Custom type tFilterLogMaxNumEntries based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000),
    )


_TFilterLogMaxNumEntries_Type.__name__ = "Unsigned32"
_TFilterLogMaxNumEntries_Object = MibTableColumn
tFilterLogMaxNumEntries = _TFilterLogMaxNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 5, 1, 5),
    _TFilterLogMaxNumEntries_Type()
)
tFilterLogMaxNumEntries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterLogMaxNumEntries.setStatus("current")


class _TFilterLogSysLogId_Type(Unsigned32):
    """Custom type tFilterLogSysLogId based on Unsigned32"""
    defaultValue = 0


_TFilterLogSysLogId_Type.__name__ = "Unsigned32"
_TFilterLogSysLogId_Object = MibTableColumn
tFilterLogSysLogId = _TFilterLogSysLogId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 5, 1, 6),
    _TFilterLogSysLogId_Type()
)
tFilterLogSysLogId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterLogSysLogId.setStatus("current")


class _TFilterLogFileId_Type(Unsigned32):
    """Custom type tFilterLogFileId based on Unsigned32"""
    defaultValue = 0


_TFilterLogFileId_Type.__name__ = "Unsigned32"
_TFilterLogFileId_Object = MibTableColumn
tFilterLogFileId = _TFilterLogFileId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 5, 1, 7),
    _TFilterLogFileId_Type()
)
tFilterLogFileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterLogFileId.setStatus("current")


class _TFilterLogStopOnFull_Type(TruthValue):
    """Custom type tFilterLogStopOnFull based on TruthValue"""
    defaultValue = 2


_TFilterLogStopOnFull_Type.__name__ = "TruthValue"
_TFilterLogStopOnFull_Object = MibTableColumn
tFilterLogStopOnFull = _TFilterLogStopOnFull_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 5, 1, 8),
    _TFilterLogStopOnFull_Type()
)
tFilterLogStopOnFull.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterLogStopOnFull.setStatus("current")


class _TFilterLogEnabled_Type(TmnxAdminStateTruthValue):
    """Custom type tFilterLogEnabled based on TmnxAdminStateTruthValue"""
    defaultValue = 1


_TFilterLogEnabled_Type.__name__ = "TmnxAdminStateTruthValue"
_TFilterLogEnabled_Object = MibTableColumn
tFilterLogEnabled = _TFilterLogEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 5, 1, 9),
    _TFilterLogEnabled_Type()
)
tFilterLogEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterLogEnabled.setStatus("current")


class _TFilterLogSummaryEnabled_Type(TmnxAdminStateTruthValue):
    """Custom type tFilterLogSummaryEnabled based on TmnxAdminStateTruthValue"""
    defaultValue = 2


_TFilterLogSummaryEnabled_Type.__name__ = "TmnxAdminStateTruthValue"
_TFilterLogSummaryEnabled_Object = MibTableColumn
tFilterLogSummaryEnabled = _TFilterLogSummaryEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 5, 1, 10),
    _TFilterLogSummaryEnabled_Type()
)
tFilterLogSummaryEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterLogSummaryEnabled.setStatus("current")


class _TFilterLogSummaryCrit1_Type(TFilterLogSummaryCriterium):
    """Custom type tFilterLogSummaryCrit1 based on TFilterLogSummaryCriterium"""
    defaultValue = 0


_TFilterLogSummaryCrit1_Type.__name__ = "TFilterLogSummaryCriterium"
_TFilterLogSummaryCrit1_Object = MibTableColumn
tFilterLogSummaryCrit1 = _TFilterLogSummaryCrit1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 5, 1, 11),
    _TFilterLogSummaryCrit1_Type()
)
tFilterLogSummaryCrit1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterLogSummaryCrit1.setStatus("current")
_TFilterLogScalars_ObjectIdentity = ObjectIdentity
tFilterLogScalars = _TFilterLogScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 6)
)
_TFilterLogMaxInstances_Type = Gauge32
_TFilterLogMaxInstances_Object = MibScalar
tFilterLogMaxInstances = _TFilterLogMaxInstances_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 6, 1),
    _TFilterLogMaxInstances_Type()
)
tFilterLogMaxInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterLogMaxInstances.setStatus("current")
_TFilterLogInstances_Type = Gauge32
_TFilterLogInstances_Object = MibScalar
tFilterLogInstances = _TFilterLogInstances_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 6, 2),
    _TFilterLogInstances_Type()
)
tFilterLogInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterLogInstances.setStatus("current")
_TFilterLogBindings_Type = Gauge32
_TFilterLogBindings_Object = MibScalar
tFilterLogBindings = _TFilterLogBindings_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 6, 3),
    _TFilterLogBindings_Type()
)
tFilterLogBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterLogBindings.setStatus("current")
_TFilterNotificationObjects_ObjectIdentity = ObjectIdentity
tFilterNotificationObjects = _TFilterNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 8)
)


class _TFilterPBRDropReason_Type(Integer32):
    """Custom type tFilterPBRDropReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalidInterface", 0),
          ("interfaceDown", 1))
    )


_TFilterPBRDropReason_Type.__name__ = "Integer32"
_TFilterPBRDropReason_Object = MibScalar
tFilterPBRDropReason = _TFilterPBRDropReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 8, 1),
    _TFilterPBRDropReason_Type()
)
tFilterPBRDropReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tFilterPBRDropReason.setStatus("current")
_TFilterParmRow_Type = RowPointer
_TFilterParmRow_Object = MibScalar
tFilterParmRow = _TFilterParmRow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 8, 2),
    _TFilterParmRow_Type()
)
tFilterParmRow.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tFilterParmRow.setStatus("current")
_TFilterAlarmDescription_Type = DisplayString
_TFilterAlarmDescription_Object = MibScalar
tFilterAlarmDescription = _TFilterAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 8, 3),
    _TFilterAlarmDescription_Type()
)
tFilterAlarmDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tFilterAlarmDescription.setStatus("current")
_TFilterId_Type = TFilterID
_TFilterId_Object = MibScalar
tFilterId = _TFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 8, 4),
    _TFilterId_Type()
)
tFilterId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tFilterId.setStatus("current")
_TFilterType_Type = TFilterType
_TFilterType_Object = MibScalar
tFilterType = _TFilterType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 8, 5),
    _TFilterType_Type()
)
tFilterType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tFilterType.setStatus("current")
_TFilterSubInsSpaceOwner_Type = TFilterSubInsSpaceOwner
_TFilterSubInsSpaceOwner_Object = MibScalar
tFilterSubInsSpaceOwner = _TFilterSubInsSpaceOwner_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 8, 6),
    _TFilterSubInsSpaceOwner_Type()
)
tFilterSubInsSpaceOwner.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tFilterSubInsSpaceOwner.setStatus("current")
_TFilterThresholdReached_Type = Integer32
_TFilterThresholdReached_Object = MibScalar
tFilterThresholdReached = _TFilterThresholdReached_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 8, 7),
    _TFilterThresholdReached_Type()
)
tFilterThresholdReached.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tFilterThresholdReached.setStatus("current")


class _TFltrFlowSpecProblem_Type(Integer32):
    """Custom type tFltrFlowSpecProblem based on Integer32"""
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
        *(("nlriDecodeProblem", 0),
          ("maxNbrFlowSpecEntriesReached", 1),
          ("fltrResourceProblem", 2),
          ("other", 3))
    )


_TFltrFlowSpecProblem_Type.__name__ = "Integer32"
_TFltrFlowSpecProblem_Object = MibScalar
tFltrFlowSpecProblem = _TFltrFlowSpecProblem_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 8, 8),
    _TFltrFlowSpecProblem_Type()
)
tFltrFlowSpecProblem.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tFltrFlowSpecProblem.setStatus("current")
_TFltrFlowSpecProblemDescription_Type = DisplayString
_TFltrFlowSpecProblemDescription_Object = MibScalar
tFltrFlowSpecProblemDescription = _TFltrFlowSpecProblemDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 8, 9),
    _TFltrFlowSpecProblemDescription_Type()
)
tFltrFlowSpecProblemDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tFltrFlowSpecProblemDescription.setStatus("current")
_TFltrFLowSpecNLRI_Type = OctetString
_TFltrFLowSpecNLRI_Object = MibScalar
tFltrFLowSpecNLRI = _TFltrFLowSpecNLRI_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 8, 10),
    _TFltrFLowSpecNLRI_Type()
)
tFltrFLowSpecNLRI.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tFltrFLowSpecNLRI.setStatus("current")
_TFltrFlowSpecVrtrId_Type = Unsigned32
_TFltrFlowSpecVrtrId_Object = MibScalar
tFltrFlowSpecVrtrId = _TFltrFlowSpecVrtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 8, 11),
    _TFltrFlowSpecVrtrId_Type()
)
tFltrFlowSpecVrtrId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tFltrFlowSpecVrtrId.setStatus("current")
_TFltrPrefixListType_Type = TFltrPrefixListType
_TFltrPrefixListType_Object = MibScalar
tFltrPrefixListType = _TFltrPrefixListType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 8, 12),
    _TFltrPrefixListType_Type()
)
tFltrPrefixListType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tFltrPrefixListType.setStatus("current")
_TFltrPrefixListName_Type = TNamedItem
_TFltrPrefixListName_Object = MibScalar
tFltrPrefixListName = _TFltrPrefixListName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 8, 13),
    _TFltrPrefixListName_Type()
)
tFltrPrefixListName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tFltrPrefixListName.setStatus("current")
_TFltrApplyPathSource_Type = TmnxFilterApplyPathSource
_TFltrApplyPathSource_Object = MibScalar
tFltrApplyPathSource = _TFltrApplyPathSource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 8, 14),
    _TFltrApplyPathSource_Type()
)
tFltrApplyPathSource.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tFltrApplyPathSource.setStatus("current")
_TFltrApplyPathIndex_Type = Unsigned32
_TFltrApplyPathIndex_Object = MibScalar
tFltrApplyPathIndex = _TFltrApplyPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 8, 15),
    _TFltrApplyPathIndex_Type()
)
tFltrApplyPathIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tFltrApplyPathIndex.setStatus("current")
_TFltrNotifDescription_Type = DisplayString
_TFltrNotifDescription_Object = MibScalar
tFltrNotifDescription = _TFltrNotifDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 8, 16),
    _TFltrNotifDescription_Type()
)
tFltrNotifDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tFltrNotifDescription.setStatus("current")
_TFltrMdaId_Type = TmnxPortID
_TFltrMdaId_Object = MibScalar
tFltrMdaId = _TFltrMdaId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 8, 17),
    _TFltrMdaId_Type()
)
tFltrMdaId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tFltrMdaId.setStatus("current")
_TFilterTimeStampObjects_ObjectIdentity = ObjectIdentity
tFilterTimeStampObjects = _TFilterTimeStampObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 9)
)
_TFilterDomainLastChanged_Type = TimeStamp
_TFilterDomainLastChanged_Object = MibScalar
tFilterDomainLastChanged = _TFilterDomainLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 9, 1),
    _TFilterDomainLastChanged_Type()
)
tFilterDomainLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterDomainLastChanged.setStatus("current")
_TFilterRedirectPolicyTable_Object = MibTable
tFilterRedirectPolicyTable = _TFilterRedirectPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 10)
)
if mibBuilder.loadTexts:
    tFilterRedirectPolicyTable.setStatus("current")
_TFilterRedirectPolicyEntry_Object = MibTableRow
tFilterRedirectPolicyEntry = _TFilterRedirectPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 10, 1)
)
tFilterRedirectPolicyEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tFilterRedirectPolicy"),
)
if mibBuilder.loadTexts:
    tFilterRedirectPolicyEntry.setStatus("current")
_TFilterRedirectPolicy_Type = TNamedItem
_TFilterRedirectPolicy_Object = MibTableColumn
tFilterRedirectPolicy = _TFilterRedirectPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 10, 1, 1),
    _TFilterRedirectPolicy_Type()
)
tFilterRedirectPolicy.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterRedirectPolicy.setStatus("current")
_TFilterRPRowStatus_Type = RowStatus
_TFilterRPRowStatus_Object = MibTableColumn
tFilterRPRowStatus = _TFilterRPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 10, 1, 2),
    _TFilterRPRowStatus_Type()
)
tFilterRPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRPRowStatus.setStatus("current")


class _TFilterRPDescription_Type(TItemDescription):
    """Custom type tFilterRPDescription based on TItemDescription"""
    defaultHexValue = ""


_TFilterRPDescription_Type.__name__ = "TItemDescription"
_TFilterRPDescription_Object = MibTableColumn
tFilterRPDescription = _TFilterRPDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 10, 1, 3),
    _TFilterRPDescription_Type()
)
tFilterRPDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRPDescription.setStatus("current")


class _TFilterRPAdminState_Type(TmnxAdminState):
    """Custom type tFilterRPAdminState based on TmnxAdminState"""
    defaultValue = 3


_TFilterRPAdminState_Type.__name__ = "TmnxAdminState"
_TFilterRPAdminState_Object = MibTableColumn
tFilterRPAdminState = _TFilterRPAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 10, 1, 4),
    _TFilterRPAdminState_Type()
)
tFilterRPAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRPAdminState.setStatus("current")
_TFilterRPActiveDest_Type = IpAddress
_TFilterRPActiveDest_Object = MibTableColumn
tFilterRPActiveDest = _TFilterRPActiveDest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 10, 1, 5),
    _TFilterRPActiveDest_Type()
)
tFilterRPActiveDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRPActiveDest.setStatus("obsolete")


class _TFilterRPVrtrId_Type(TmnxVRtrIDOrZero):
    """Custom type tFilterRPVrtrId based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TFilterRPVrtrId_Type.__name__ = "TmnxVRtrIDOrZero"
_TFilterRPVrtrId_Object = MibTableColumn
tFilterRPVrtrId = _TFilterRPVrtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 10, 1, 6),
    _TFilterRPVrtrId_Type()
)
tFilterRPVrtrId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRPVrtrId.setStatus("current")


class _TFilterRPActiveDestAddrType_Type(InetAddressType):
    """Custom type tFilterRPActiveDestAddrType based on InetAddressType"""
    defaultValue = 0


_TFilterRPActiveDestAddrType_Type.__name__ = "InetAddressType"
_TFilterRPActiveDestAddrType_Object = MibTableColumn
tFilterRPActiveDestAddrType = _TFilterRPActiveDestAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 10, 1, 7),
    _TFilterRPActiveDestAddrType_Type()
)
tFilterRPActiveDestAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRPActiveDestAddrType.setStatus("current")


class _TFilterRPActiveDestAddr_Type(InetAddress):
    """Custom type tFilterRPActiveDestAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TFilterRPActiveDestAddr_Type.__name__ = "InetAddress"
_TFilterRPActiveDestAddr_Object = MibTableColumn
tFilterRPActiveDestAddr = _TFilterRPActiveDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 10, 1, 8),
    _TFilterRPActiveDestAddr_Type()
)
tFilterRPActiveDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRPActiveDestAddr.setStatus("current")


class _TFilterRPDstStickiness_Type(Integer32):
    """Custom type tFilterRPDstStickiness based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )


_TFilterRPDstStickiness_Type.__name__ = "Integer32"
_TFilterRPDstStickiness_Object = MibTableColumn
tFilterRPDstStickiness = _TFilterRPDstStickiness_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 10, 1, 9),
    _TFilterRPDstStickiness_Type()
)
tFilterRPDstStickiness.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRPDstStickiness.setStatus("current")
if mibBuilder.loadTexts:
    tFilterRPDstStickiness.setUnits("seconds")


class _TFilterRPBestDstAddrType_Type(InetAddressType):
    """Custom type tFilterRPBestDstAddrType based on InetAddressType"""
    defaultValue = 0


_TFilterRPBestDstAddrType_Type.__name__ = "InetAddressType"
_TFilterRPBestDstAddrType_Object = MibTableColumn
tFilterRPBestDstAddrType = _TFilterRPBestDstAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 10, 1, 10),
    _TFilterRPBestDstAddrType_Type()
)
tFilterRPBestDstAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRPBestDstAddrType.setStatus("current")


class _TFilterRPBestDstAddr_Type(InetAddress):
    """Custom type tFilterRPBestDstAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TFilterRPBestDstAddr_Type.__name__ = "InetAddress"
_TFilterRPBestDstAddr_Object = MibTableColumn
tFilterRPBestDstAddr = _TFilterRPBestDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 10, 1, 11),
    _TFilterRPBestDstAddr_Type()
)
tFilterRPBestDstAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRPBestDstAddr.setStatus("current")


class _TFilterRPStickinessHoldRemain_Type(Integer32):
    """Custom type tFilterRPStickinessHoldRemain based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TFilterRPStickinessHoldRemain_Type.__name__ = "Integer32"
_TFilterRPStickinessHoldRemain_Object = MibTableColumn
tFilterRPStickinessHoldRemain = _TFilterRPStickinessHoldRemain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 10, 1, 12),
    _TFilterRPStickinessHoldRemain_Type()
)
tFilterRPStickinessHoldRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRPStickinessHoldRemain.setStatus("current")


class _TFilterRPNotifyDestChange_Type(TruthValue):
    """Custom type tFilterRPNotifyDestChange based on TruthValue"""
    defaultValue = 2


_TFilterRPNotifyDestChange_Type.__name__ = "TruthValue"
_TFilterRPNotifyDestChange_Object = MibTableColumn
tFilterRPNotifyDestChange = _TFilterRPNotifyDestChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 10, 1, 13),
    _TFilterRPNotifyDestChange_Type()
)
tFilterRPNotifyDestChange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRPNotifyDestChange.setStatus("current")
_TFilterRedirectDestTable_Object = MibTable
tFilterRedirectDestTable = _TFilterRedirectDestTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 11)
)
if mibBuilder.loadTexts:
    tFilterRedirectDestTable.setStatus("obsolete")
_TFilterRedirectDestEntry_Object = MibTableRow
tFilterRedirectDestEntry = _TFilterRedirectDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 11, 1)
)
tFilterRedirectDestEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tFilterRedirectPolicy"),
    (0, "TIMETRA-FILTER-MIB", "tFilterRedirectDest"),
)
if mibBuilder.loadTexts:
    tFilterRedirectDestEntry.setStatus("obsolete")
_TFilterRedirectDest_Type = IpAddress
_TFilterRedirectDest_Object = MibTableColumn
tFilterRedirectDest = _TFilterRedirectDest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 11, 1, 1),
    _TFilterRedirectDest_Type()
)
tFilterRedirectDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterRedirectDest.setStatus("obsolete")
_TFilterRDRowStatus_Type = RowStatus
_TFilterRDRowStatus_Object = MibTableColumn
tFilterRDRowStatus = _TFilterRDRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 11, 1, 2),
    _TFilterRDRowStatus_Type()
)
tFilterRDRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRDRowStatus.setStatus("obsolete")


class _TFilterRDDescription_Type(TItemDescription):
    """Custom type tFilterRDDescription based on TItemDescription"""
    defaultHexValue = ""


_TFilterRDDescription_Type.__name__ = "TItemDescription"
_TFilterRDDescription_Object = MibTableColumn
tFilterRDDescription = _TFilterRDDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 11, 1, 3),
    _TFilterRDDescription_Type()
)
tFilterRDDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRDDescription.setStatus("obsolete")


class _TFilterRDAdminPriority_Type(Unsigned32):
    """Custom type tFilterRDAdminPriority based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TFilterRDAdminPriority_Type.__name__ = "Unsigned32"
_TFilterRDAdminPriority_Object = MibTableColumn
tFilterRDAdminPriority = _TFilterRDAdminPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 11, 1, 4),
    _TFilterRDAdminPriority_Type()
)
tFilterRDAdminPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRDAdminPriority.setStatus("obsolete")


class _TFilterRDOperPriority_Type(Unsigned32):
    """Custom type tFilterRDOperPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TFilterRDOperPriority_Type.__name__ = "Unsigned32"
_TFilterRDOperPriority_Object = MibTableColumn
tFilterRDOperPriority = _TFilterRDOperPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 11, 1, 5),
    _TFilterRDOperPriority_Type()
)
tFilterRDOperPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRDOperPriority.setStatus("obsolete")


class _TFilterRDAdminState_Type(TmnxAdminState):
    """Custom type tFilterRDAdminState based on TmnxAdminState"""
    defaultValue = 3


_TFilterRDAdminState_Type.__name__ = "TmnxAdminState"
_TFilterRDAdminState_Object = MibTableColumn
tFilterRDAdminState = _TFilterRDAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 11, 1, 6),
    _TFilterRDAdminState_Type()
)
tFilterRDAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRDAdminState.setStatus("obsolete")
_TFilterRDOperState_Type = TmnxOperState
_TFilterRDOperState_Object = MibTableColumn
tFilterRDOperState = _TFilterRDOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 11, 1, 7),
    _TFilterRDOperState_Type()
)
tFilterRDOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRDOperState.setStatus("obsolete")
_TFilterRedirectSNMPTestTable_Object = MibTable
tFilterRedirectSNMPTestTable = _TFilterRedirectSNMPTestTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 12)
)
if mibBuilder.loadTexts:
    tFilterRedirectSNMPTestTable.setStatus("obsolete")
_TFilterRedirectSNMPTestEntry_Object = MibTableRow
tFilterRedirectSNMPTestEntry = _TFilterRedirectSNMPTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 12, 1)
)
tFilterRedirectSNMPTestEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tFilterRedirectPolicy"),
    (0, "TIMETRA-FILTER-MIB", "tFilterRedirectDest"),
    (0, "TIMETRA-FILTER-MIB", "tFilterRedirectSNMPTest"),
)
if mibBuilder.loadTexts:
    tFilterRedirectSNMPTestEntry.setStatus("obsolete")
_TFilterRedirectSNMPTest_Type = TNamedItem
_TFilterRedirectSNMPTest_Object = MibTableColumn
tFilterRedirectSNMPTest = _TFilterRedirectSNMPTest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 12, 1, 1),
    _TFilterRedirectSNMPTest_Type()
)
tFilterRedirectSNMPTest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterRedirectSNMPTest.setStatus("obsolete")
_TFilterRSTRowStatus_Type = RowStatus
_TFilterRSTRowStatus_Object = MibTableColumn
tFilterRSTRowStatus = _TFilterRSTRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 12, 1, 2),
    _TFilterRSTRowStatus_Type()
)
tFilterRSTRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRSTRowStatus.setStatus("obsolete")
_TFilterRSTOID_Type = ObjectIdentifier
_TFilterRSTOID_Object = MibTableColumn
tFilterRSTOID = _TFilterRSTOID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 12, 1, 3),
    _TFilterRSTOID_Type()
)
tFilterRSTOID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRSTOID.setStatus("obsolete")


class _TFilterRSTCommunity_Type(DisplayString):
    """Custom type tFilterRSTCommunity based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TFilterRSTCommunity_Type.__name__ = "DisplayString"
_TFilterRSTCommunity_Object = MibTableColumn
tFilterRSTCommunity = _TFilterRSTCommunity_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 12, 1, 4),
    _TFilterRSTCommunity_Type()
)
tFilterRSTCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRSTCommunity.setStatus("obsolete")


class _TFilterRSTSNMPVersion_Type(Integer32):
    """Custom type tFilterRSTSNMPVersion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("snmpv1", 1),
          ("snmpv2c", 2),
          ("snmpv3", 3))
    )


_TFilterRSTSNMPVersion_Type.__name__ = "Integer32"
_TFilterRSTSNMPVersion_Object = MibTableColumn
tFilterRSTSNMPVersion = _TFilterRSTSNMPVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 12, 1, 5),
    _TFilterRSTSNMPVersion_Type()
)
tFilterRSTSNMPVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRSTSNMPVersion.setStatus("obsolete")


class _TFilterRSTInterval_Type(Unsigned32):
    """Custom type tFilterRSTInterval based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TFilterRSTInterval_Type.__name__ = "Unsigned32"
_TFilterRSTInterval_Object = MibTableColumn
tFilterRSTInterval = _TFilterRSTInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 12, 1, 6),
    _TFilterRSTInterval_Type()
)
tFilterRSTInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRSTInterval.setStatus("obsolete")
if mibBuilder.loadTexts:
    tFilterRSTInterval.setUnits("seconds")


class _TFilterRSTTimeout_Type(Unsigned32):
    """Custom type tFilterRSTTimeout based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TFilterRSTTimeout_Type.__name__ = "Unsigned32"
_TFilterRSTTimeout_Object = MibTableColumn
tFilterRSTTimeout = _TFilterRSTTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 12, 1, 7),
    _TFilterRSTTimeout_Type()
)
tFilterRSTTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRSTTimeout.setStatus("obsolete")
if mibBuilder.loadTexts:
    tFilterRSTTimeout.setUnits("seconds")


class _TFilterRSTDropCount_Type(Unsigned32):
    """Custom type tFilterRSTDropCount based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TFilterRSTDropCount_Type.__name__ = "Unsigned32"
_TFilterRSTDropCount_Object = MibTableColumn
tFilterRSTDropCount = _TFilterRSTDropCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 12, 1, 8),
    _TFilterRSTDropCount_Type()
)
tFilterRSTDropCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRSTDropCount.setStatus("obsolete")


class _TFilterRSTHoldDown_Type(Unsigned32):
    """Custom type tFilterRSTHoldDown based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_TFilterRSTHoldDown_Type.__name__ = "Unsigned32"
_TFilterRSTHoldDown_Object = MibTableColumn
tFilterRSTHoldDown = _TFilterRSTHoldDown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 12, 1, 9),
    _TFilterRSTHoldDown_Type()
)
tFilterRSTHoldDown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRSTHoldDown.setStatus("obsolete")
if mibBuilder.loadTexts:
    tFilterRSTHoldDown.setUnits("seconds")


class _TFilterRSTHoldDownRemain_Type(Unsigned32):
    """Custom type tFilterRSTHoldDownRemain based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_TFilterRSTHoldDownRemain_Type.__name__ = "Unsigned32"
_TFilterRSTHoldDownRemain_Object = MibTableColumn
tFilterRSTHoldDownRemain = _TFilterRSTHoldDownRemain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 12, 1, 10),
    _TFilterRSTHoldDownRemain_Type()
)
tFilterRSTHoldDownRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRSTHoldDownRemain.setStatus("obsolete")
if mibBuilder.loadTexts:
    tFilterRSTHoldDownRemain.setUnits("seconds")
_TFilterRSTLastActionTime_Type = TimeStamp
_TFilterRSTLastActionTime_Object = MibTableColumn
tFilterRSTLastActionTime = _TFilterRSTLastActionTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 12, 1, 11),
    _TFilterRSTLastActionTime_Type()
)
tFilterRSTLastActionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRSTLastActionTime.setStatus("obsolete")
_TFilterRSTLastOID_Type = ObjectIdentifier
_TFilterRSTLastOID_Object = MibTableColumn
tFilterRSTLastOID = _TFilterRSTLastOID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 12, 1, 12),
    _TFilterRSTLastOID_Type()
)
tFilterRSTLastOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRSTLastOID.setStatus("obsolete")


class _TFilterRSTLastType_Type(Integer32):
    """Custom type tFilterRSTLastType based on Integer32"""
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
          ("counter32", 1),
          ("unsigned32", 2),
          ("timeTicks", 3),
          ("integer32", 4),
          ("ipAddress", 5),
          ("octetString", 6),
          ("objectId", 7),
          ("counter64", 8),
          ("opaque", 9))
    )


_TFilterRSTLastType_Type.__name__ = "Integer32"
_TFilterRSTLastType_Object = MibTableColumn
tFilterRSTLastType = _TFilterRSTLastType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 12, 1, 13),
    _TFilterRSTLastType_Type()
)
tFilterRSTLastType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRSTLastType.setStatus("obsolete")
_TFilterRSTLastCounter32Val_Type = Counter32
_TFilterRSTLastCounter32Val_Object = MibTableColumn
tFilterRSTLastCounter32Val = _TFilterRSTLastCounter32Val_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 12, 1, 14),
    _TFilterRSTLastCounter32Val_Type()
)
tFilterRSTLastCounter32Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRSTLastCounter32Val.setStatus("obsolete")
_TFilterRSTLastUnsigned32Val_Type = Unsigned32
_TFilterRSTLastUnsigned32Val_Object = MibTableColumn
tFilterRSTLastUnsigned32Val = _TFilterRSTLastUnsigned32Val_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 12, 1, 15),
    _TFilterRSTLastUnsigned32Val_Type()
)
tFilterRSTLastUnsigned32Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRSTLastUnsigned32Val.setStatus("obsolete")
_TFilterRSTLastTimeTicksVal_Type = TimeTicks
_TFilterRSTLastTimeTicksVal_Object = MibTableColumn
tFilterRSTLastTimeTicksVal = _TFilterRSTLastTimeTicksVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 12, 1, 16),
    _TFilterRSTLastTimeTicksVal_Type()
)
tFilterRSTLastTimeTicksVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRSTLastTimeTicksVal.setStatus("obsolete")
_TFilterRSTLastInt32Val_Type = Integer32
_TFilterRSTLastInt32Val_Object = MibTableColumn
tFilterRSTLastInt32Val = _TFilterRSTLastInt32Val_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 12, 1, 17),
    _TFilterRSTLastInt32Val_Type()
)
tFilterRSTLastInt32Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRSTLastInt32Val.setStatus("obsolete")
_TFilterRSTLastOctetStringVal_Type = OctetString
_TFilterRSTLastOctetStringVal_Object = MibTableColumn
tFilterRSTLastOctetStringVal = _TFilterRSTLastOctetStringVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 12, 1, 18),
    _TFilterRSTLastOctetStringVal_Type()
)
tFilterRSTLastOctetStringVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRSTLastOctetStringVal.setStatus("obsolete")
_TFilterRSTLastIpAddressVal_Type = IpAddress
_TFilterRSTLastIpAddressVal_Object = MibTableColumn
tFilterRSTLastIpAddressVal = _TFilterRSTLastIpAddressVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 12, 1, 19),
    _TFilterRSTLastIpAddressVal_Type()
)
tFilterRSTLastIpAddressVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRSTLastIpAddressVal.setStatus("obsolete")
_TFilterRSTLastOidVal_Type = ObjectIdentifier
_TFilterRSTLastOidVal_Object = MibTableColumn
tFilterRSTLastOidVal = _TFilterRSTLastOidVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 12, 1, 20),
    _TFilterRSTLastOidVal_Type()
)
tFilterRSTLastOidVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRSTLastOidVal.setStatus("obsolete")
_TFilterRSTLastCounter64Val_Type = Counter64
_TFilterRSTLastCounter64Val_Object = MibTableColumn
tFilterRSTLastCounter64Val = _TFilterRSTLastCounter64Val_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 12, 1, 21),
    _TFilterRSTLastCounter64Val_Type()
)
tFilterRSTLastCounter64Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRSTLastCounter64Val.setStatus("obsolete")
_TFilterRSTLastOpaqueVal_Type = Opaque
_TFilterRSTLastOpaqueVal_Object = MibTableColumn
tFilterRSTLastOpaqueVal = _TFilterRSTLastOpaqueVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 12, 1, 22),
    _TFilterRSTLastOpaqueVal_Type()
)
tFilterRSTLastOpaqueVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRSTLastOpaqueVal.setStatus("obsolete")


class _TFilterRSTLastAction_Type(Integer32):
    """Custom type tFilterRSTLastAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("none", 3))
    )


_TFilterRSTLastAction_Type.__name__ = "Integer32"
_TFilterRSTLastAction_Object = MibTableColumn
tFilterRSTLastAction = _TFilterRSTLastAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 12, 1, 23),
    _TFilterRSTLastAction_Type()
)
tFilterRSTLastAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRSTLastAction.setStatus("obsolete")


class _TFilterRSTLastPrioChange_Type(Integer32):
    """Custom type tFilterRSTLastPrioChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-255, 255),
    )


_TFilterRSTLastPrioChange_Type.__name__ = "Integer32"
_TFilterRSTLastPrioChange_Object = MibTableColumn
tFilterRSTLastPrioChange = _TFilterRSTLastPrioChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 12, 1, 24),
    _TFilterRSTLastPrioChange_Type()
)
tFilterRSTLastPrioChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRSTLastPrioChange.setStatus("obsolete")


class _TFilterRSTNextRespIndex_Type(Integer32):
    """Custom type tFilterRSTNextRespIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 2147483647),
    )


_TFilterRSTNextRespIndex_Type.__name__ = "Integer32"
_TFilterRSTNextRespIndex_Object = MibTableColumn
tFilterRSTNextRespIndex = _TFilterRSTNextRespIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 12, 1, 25),
    _TFilterRSTNextRespIndex_Type()
)
tFilterRSTNextRespIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRSTNextRespIndex.setStatus("obsolete")
_TFilterRedirectSNMPRespTable_Object = MibTable
tFilterRedirectSNMPRespTable = _TFilterRedirectSNMPRespTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 13)
)
if mibBuilder.loadTexts:
    tFilterRedirectSNMPRespTable.setStatus("obsolete")
_TFilterRedirectSNMPRespEntry_Object = MibTableRow
tFilterRedirectSNMPRespEntry = _TFilterRedirectSNMPRespEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 13, 1)
)
tFilterRedirectSNMPRespEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tFilterRedirectPolicy"),
    (0, "TIMETRA-FILTER-MIB", "tFilterRedirectDest"),
    (0, "TIMETRA-FILTER-MIB", "tFilterRedirectSNMPTest"),
    (0, "TIMETRA-FILTER-MIB", "tFilterRSTRespId"),
)
if mibBuilder.loadTexts:
    tFilterRedirectSNMPRespEntry.setStatus("obsolete")


class _TFilterRSTRespId_Type(Integer32):
    """Custom type tFilterRSTRespId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TFilterRSTRespId_Type.__name__ = "Integer32"
_TFilterRSTRespId_Object = MibTableColumn
tFilterRSTRespId = _TFilterRSTRespId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 13, 1, 1),
    _TFilterRSTRespId_Type()
)
tFilterRSTRespId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterRSTRespId.setStatus("obsolete")
_TFilterRSTRespRowStatus_Type = RowStatus
_TFilterRSTRespRowStatus_Object = MibTableColumn
tFilterRSTRespRowStatus = _TFilterRSTRespRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 13, 1, 2),
    _TFilterRSTRespRowStatus_Type()
)
tFilterRSTRespRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRSTRespRowStatus.setStatus("obsolete")


class _TFilterRSTRespAction_Type(Integer32):
    """Custom type tFilterRSTRespAction based on Integer32"""
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
        *(("increase", 1),
          ("decrease", 2),
          ("disable", 3))
    )


_TFilterRSTRespAction_Type.__name__ = "Integer32"
_TFilterRSTRespAction_Object = MibTableColumn
tFilterRSTRespAction = _TFilterRSTRespAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 13, 1, 3),
    _TFilterRSTRespAction_Type()
)
tFilterRSTRespAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRSTRespAction.setStatus("obsolete")


class _TFilterRSTRespPrioChange_Type(Unsigned32):
    """Custom type tFilterRSTRespPrioChange based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TFilterRSTRespPrioChange_Type.__name__ = "Unsigned32"
_TFilterRSTRespPrioChange_Object = MibTableColumn
tFilterRSTRespPrioChange = _TFilterRSTRespPrioChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 13, 1, 4),
    _TFilterRSTRespPrioChange_Type()
)
tFilterRSTRespPrioChange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRSTRespPrioChange.setStatus("obsolete")
_TFilterRSTRespOID_Type = ObjectIdentifier
_TFilterRSTRespOID_Object = MibTableColumn
tFilterRSTRespOID = _TFilterRSTRespOID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 13, 1, 5),
    _TFilterRSTRespOID_Type()
)
tFilterRSTRespOID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRSTRespOID.setStatus("obsolete")


class _TFilterRSTRespType_Type(Integer32):
    """Custom type tFilterRSTRespType based on Integer32"""
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
        *(("counter32", 1),
          ("unsigned32", 2),
          ("timeTicks", 3),
          ("integer32", 4),
          ("ipAddress", 5),
          ("octetString", 6),
          ("objectId", 7),
          ("counter64", 8),
          ("opaque", 9))
    )


_TFilterRSTRespType_Type.__name__ = "Integer32"
_TFilterRSTRespType_Object = MibTableColumn
tFilterRSTRespType = _TFilterRSTRespType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 13, 1, 6),
    _TFilterRSTRespType_Type()
)
tFilterRSTRespType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRSTRespType.setStatus("obsolete")
_TFilterRSTCounter32Val_Type = Counter32
_TFilterRSTCounter32Val_Object = MibTableColumn
tFilterRSTCounter32Val = _TFilterRSTCounter32Val_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 13, 1, 7),
    _TFilterRSTCounter32Val_Type()
)
tFilterRSTCounter32Val.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRSTCounter32Val.setStatus("obsolete")
_TFilterRSTUnsigned32Val_Type = Unsigned32
_TFilterRSTUnsigned32Val_Object = MibTableColumn
tFilterRSTUnsigned32Val = _TFilterRSTUnsigned32Val_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 13, 1, 8),
    _TFilterRSTUnsigned32Val_Type()
)
tFilterRSTUnsigned32Val.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRSTUnsigned32Val.setStatus("obsolete")
_TFilterRSTTimeTicksVal_Type = TimeTicks
_TFilterRSTTimeTicksVal_Object = MibTableColumn
tFilterRSTTimeTicksVal = _TFilterRSTTimeTicksVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 13, 1, 9),
    _TFilterRSTTimeTicksVal_Type()
)
tFilterRSTTimeTicksVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRSTTimeTicksVal.setStatus("obsolete")
_TFilterRSTInt32Val_Type = Integer32
_TFilterRSTInt32Val_Object = MibTableColumn
tFilterRSTInt32Val = _TFilterRSTInt32Val_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 13, 1, 10),
    _TFilterRSTInt32Val_Type()
)
tFilterRSTInt32Val.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRSTInt32Val.setStatus("obsolete")
_TFilterRSTOctetStringVal_Type = OctetString
_TFilterRSTOctetStringVal_Object = MibTableColumn
tFilterRSTOctetStringVal = _TFilterRSTOctetStringVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 13, 1, 11),
    _TFilterRSTOctetStringVal_Type()
)
tFilterRSTOctetStringVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRSTOctetStringVal.setStatus("obsolete")
_TFilterRSTIpAddressVal_Type = IpAddress
_TFilterRSTIpAddressVal_Object = MibTableColumn
tFilterRSTIpAddressVal = _TFilterRSTIpAddressVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 13, 1, 12),
    _TFilterRSTIpAddressVal_Type()
)
tFilterRSTIpAddressVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRSTIpAddressVal.setStatus("obsolete")
_TFilterRSTOidVal_Type = ObjectIdentifier
_TFilterRSTOidVal_Object = MibTableColumn
tFilterRSTOidVal = _TFilterRSTOidVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 13, 1, 13),
    _TFilterRSTOidVal_Type()
)
tFilterRSTOidVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRSTOidVal.setStatus("obsolete")
_TFilterRSTCounter64Val_Type = Counter64
_TFilterRSTCounter64Val_Object = MibTableColumn
tFilterRSTCounter64Val = _TFilterRSTCounter64Val_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 13, 1, 14),
    _TFilterRSTCounter64Val_Type()
)
tFilterRSTCounter64Val.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRSTCounter64Val.setStatus("obsolete")
_TFilterRSTOpaqueVal_Type = Opaque
_TFilterRSTOpaqueVal_Object = MibTableColumn
tFilterRSTOpaqueVal = _TFilterRSTOpaqueVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 13, 1, 15),
    _TFilterRSTOpaqueVal_Type()
)
tFilterRSTOpaqueVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRSTOpaqueVal.setStatus("obsolete")
_TFilterRedirectURLTestTable_Object = MibTable
tFilterRedirectURLTestTable = _TFilterRedirectURLTestTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 14)
)
if mibBuilder.loadTexts:
    tFilterRedirectURLTestTable.setStatus("obsolete")
_TFilterRedirectURLTestEntry_Object = MibTableRow
tFilterRedirectURLTestEntry = _TFilterRedirectURLTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 14, 1)
)
tFilterRedirectURLTestEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tFilterRedirectPolicy"),
    (0, "TIMETRA-FILTER-MIB", "tFilterRedirectDest"),
    (0, "TIMETRA-FILTER-MIB", "tFilterRedirectURLTest"),
)
if mibBuilder.loadTexts:
    tFilterRedirectURLTestEntry.setStatus("obsolete")
_TFilterRedirectURLTest_Type = TNamedItem
_TFilterRedirectURLTest_Object = MibTableColumn
tFilterRedirectURLTest = _TFilterRedirectURLTest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 14, 1, 1),
    _TFilterRedirectURLTest_Type()
)
tFilterRedirectURLTest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterRedirectURLTest.setStatus("obsolete")
_TFilterRUTRowStatus_Type = RowStatus
_TFilterRUTRowStatus_Object = MibTableColumn
tFilterRUTRowStatus = _TFilterRUTRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 14, 1, 2),
    _TFilterRUTRowStatus_Type()
)
tFilterRUTRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRUTRowStatus.setStatus("obsolete")


class _TFilterRUTURL_Type(DisplayString):
    """Custom type tFilterRUTURL based on DisplayString"""
    defaultHexValue = ""


_TFilterRUTURL_Type.__name__ = "DisplayString"
_TFilterRUTURL_Object = MibTableColumn
tFilterRUTURL = _TFilterRUTURL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 14, 1, 3),
    _TFilterRUTURL_Type()
)
tFilterRUTURL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRUTURL.setStatus("obsolete")


class _TFilterRUTHTTPVersion_Type(DisplayString):
    """Custom type tFilterRUTHTTPVersion based on DisplayString"""
    defaultHexValue = ""


_TFilterRUTHTTPVersion_Type.__name__ = "DisplayString"
_TFilterRUTHTTPVersion_Object = MibTableColumn
tFilterRUTHTTPVersion = _TFilterRUTHTTPVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 14, 1, 4),
    _TFilterRUTHTTPVersion_Type()
)
tFilterRUTHTTPVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRUTHTTPVersion.setStatus("obsolete")


class _TFilterRUTInterval_Type(Unsigned32):
    """Custom type tFilterRUTInterval based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TFilterRUTInterval_Type.__name__ = "Unsigned32"
_TFilterRUTInterval_Object = MibTableColumn
tFilterRUTInterval = _TFilterRUTInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 14, 1, 5),
    _TFilterRUTInterval_Type()
)
tFilterRUTInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRUTInterval.setStatus("obsolete")
if mibBuilder.loadTexts:
    tFilterRUTInterval.setUnits("seconds")


class _TFilterRUTTimeout_Type(Unsigned32):
    """Custom type tFilterRUTTimeout based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TFilterRUTTimeout_Type.__name__ = "Unsigned32"
_TFilterRUTTimeout_Object = MibTableColumn
tFilterRUTTimeout = _TFilterRUTTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 14, 1, 6),
    _TFilterRUTTimeout_Type()
)
tFilterRUTTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRUTTimeout.setStatus("obsolete")
if mibBuilder.loadTexts:
    tFilterRUTTimeout.setUnits("seconds")


class _TFilterRUTDropCount_Type(Unsigned32):
    """Custom type tFilterRUTDropCount based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TFilterRUTDropCount_Type.__name__ = "Unsigned32"
_TFilterRUTDropCount_Object = MibTableColumn
tFilterRUTDropCount = _TFilterRUTDropCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 14, 1, 7),
    _TFilterRUTDropCount_Type()
)
tFilterRUTDropCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRUTDropCount.setStatus("obsolete")


class _TFilterRUTHoldDown_Type(Unsigned32):
    """Custom type tFilterRUTHoldDown based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_TFilterRUTHoldDown_Type.__name__ = "Unsigned32"
_TFilterRUTHoldDown_Object = MibTableColumn
tFilterRUTHoldDown = _TFilterRUTHoldDown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 14, 1, 8),
    _TFilterRUTHoldDown_Type()
)
tFilterRUTHoldDown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRUTHoldDown.setStatus("obsolete")
if mibBuilder.loadTexts:
    tFilterRUTHoldDown.setUnits("seconds")


class _TFilterRUTHoldDownRemain_Type(Unsigned32):
    """Custom type tFilterRUTHoldDownRemain based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_TFilterRUTHoldDownRemain_Type.__name__ = "Unsigned32"
_TFilterRUTHoldDownRemain_Object = MibTableColumn
tFilterRUTHoldDownRemain = _TFilterRUTHoldDownRemain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 14, 1, 9),
    _TFilterRUTHoldDownRemain_Type()
)
tFilterRUTHoldDownRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRUTHoldDownRemain.setStatus("obsolete")
if mibBuilder.loadTexts:
    tFilterRUTHoldDownRemain.setUnits("seconds")
_TFilterRUTLastActionTime_Type = TimeStamp
_TFilterRUTLastActionTime_Object = MibTableColumn
tFilterRUTLastActionTime = _TFilterRUTLastActionTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 14, 1, 10),
    _TFilterRUTLastActionTime_Type()
)
tFilterRUTLastActionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRUTLastActionTime.setStatus("obsolete")
_TFilterRUTLastRetCode_Type = Unsigned32
_TFilterRUTLastRetCode_Object = MibTableColumn
tFilterRUTLastRetCode = _TFilterRUTLastRetCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 14, 1, 11),
    _TFilterRUTLastRetCode_Type()
)
tFilterRUTLastRetCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRUTLastRetCode.setStatus("obsolete")


class _TFilterRUTLastAction_Type(Integer32):
    """Custom type tFilterRUTLastAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("none", 3))
    )


_TFilterRUTLastAction_Type.__name__ = "Integer32"
_TFilterRUTLastAction_Object = MibTableColumn
tFilterRUTLastAction = _TFilterRUTLastAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 14, 1, 12),
    _TFilterRUTLastAction_Type()
)
tFilterRUTLastAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRUTLastAction.setStatus("obsolete")


class _TFilterRUTLastPrioChange_Type(Integer32):
    """Custom type tFilterRUTLastPrioChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-255, 255),
    )


_TFilterRUTLastPrioChange_Type.__name__ = "Integer32"
_TFilterRUTLastPrioChange_Object = MibTableColumn
tFilterRUTLastPrioChange = _TFilterRUTLastPrioChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 14, 1, 13),
    _TFilterRUTLastPrioChange_Type()
)
tFilterRUTLastPrioChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRUTLastPrioChange.setStatus("obsolete")
_TFilterRedirectURLRespTable_Object = MibTable
tFilterRedirectURLRespTable = _TFilterRedirectURLRespTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 15)
)
if mibBuilder.loadTexts:
    tFilterRedirectURLRespTable.setStatus("obsolete")
_TFilterRedirectURLRespEntry_Object = MibTableRow
tFilterRedirectURLRespEntry = _TFilterRedirectURLRespEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 15, 1)
)
tFilterRedirectURLRespEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tFilterRedirectPolicy"),
    (0, "TIMETRA-FILTER-MIB", "tFilterRedirectDest"),
    (0, "TIMETRA-FILTER-MIB", "tFilterRedirectURLTest"),
    (0, "TIMETRA-FILTER-MIB", "tFilterRedirectURLLowRespCode"),
    (0, "TIMETRA-FILTER-MIB", "tFilterRedirectURLHighRespCode"),
)
if mibBuilder.loadTexts:
    tFilterRedirectURLRespEntry.setStatus("obsolete")
_TFilterRedirectURLLowRespCode_Type = Unsigned32
_TFilterRedirectURLLowRespCode_Object = MibTableColumn
tFilterRedirectURLLowRespCode = _TFilterRedirectURLLowRespCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 15, 1, 1),
    _TFilterRedirectURLLowRespCode_Type()
)
tFilterRedirectURLLowRespCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterRedirectURLLowRespCode.setStatus("obsolete")
_TFilterRedirectURLHighRespCode_Type = Unsigned32
_TFilterRedirectURLHighRespCode_Object = MibTableColumn
tFilterRedirectURLHighRespCode = _TFilterRedirectURLHighRespCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 15, 1, 2),
    _TFilterRedirectURLHighRespCode_Type()
)
tFilterRedirectURLHighRespCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterRedirectURLHighRespCode.setStatus("obsolete")
_TFilterRUTRespRowStatus_Type = RowStatus
_TFilterRUTRespRowStatus_Object = MibTableColumn
tFilterRUTRespRowStatus = _TFilterRUTRespRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 15, 1, 3),
    _TFilterRUTRespRowStatus_Type()
)
tFilterRUTRespRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRUTRespRowStatus.setStatus("obsolete")


class _TFilterRUTRespAction_Type(Integer32):
    """Custom type tFilterRUTRespAction based on Integer32"""
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
        *(("increase", 1),
          ("decrease", 2),
          ("disable", 3))
    )


_TFilterRUTRespAction_Type.__name__ = "Integer32"
_TFilterRUTRespAction_Object = MibTableColumn
tFilterRUTRespAction = _TFilterRUTRespAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 15, 1, 4),
    _TFilterRUTRespAction_Type()
)
tFilterRUTRespAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRUTRespAction.setStatus("obsolete")


class _TFilterRUTRespPrioChange_Type(Unsigned32):
    """Custom type tFilterRUTRespPrioChange based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TFilterRUTRespPrioChange_Type.__name__ = "Unsigned32"
_TFilterRUTRespPrioChange_Object = MibTableColumn
tFilterRUTRespPrioChange = _TFilterRUTRespPrioChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 15, 1, 5),
    _TFilterRUTRespPrioChange_Type()
)
tFilterRUTRespPrioChange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRUTRespPrioChange.setStatus("obsolete")
_TFilterRedirectPingTestTable_Object = MibTable
tFilterRedirectPingTestTable = _TFilterRedirectPingTestTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 16)
)
if mibBuilder.loadTexts:
    tFilterRedirectPingTestTable.setStatus("obsolete")
_TFilterRedirectPingTestEntry_Object = MibTableRow
tFilterRedirectPingTestEntry = _TFilterRedirectPingTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 16, 1)
)
tFilterRedirectPingTestEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tFilterRedirectPolicy"),
    (0, "TIMETRA-FILTER-MIB", "tFilterRedirectDest"),
)
if mibBuilder.loadTexts:
    tFilterRedirectPingTestEntry.setStatus("obsolete")
_TFilterRPTRowStatus_Type = RowStatus
_TFilterRPTRowStatus_Object = MibTableColumn
tFilterRPTRowStatus = _TFilterRPTRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 16, 1, 1),
    _TFilterRPTRowStatus_Type()
)
tFilterRPTRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRPTRowStatus.setStatus("obsolete")


class _TFilterRPTInterval_Type(Unsigned32):
    """Custom type tFilterRPTInterval based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TFilterRPTInterval_Type.__name__ = "Unsigned32"
_TFilterRPTInterval_Object = MibTableColumn
tFilterRPTInterval = _TFilterRPTInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 16, 1, 2),
    _TFilterRPTInterval_Type()
)
tFilterRPTInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRPTInterval.setStatus("obsolete")
if mibBuilder.loadTexts:
    tFilterRPTInterval.setUnits("seconds")


class _TFilterRPTTimeout_Type(Unsigned32):
    """Custom type tFilterRPTTimeout based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TFilterRPTTimeout_Type.__name__ = "Unsigned32"
_TFilterRPTTimeout_Object = MibTableColumn
tFilterRPTTimeout = _TFilterRPTTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 16, 1, 3),
    _TFilterRPTTimeout_Type()
)
tFilterRPTTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRPTTimeout.setStatus("obsolete")
if mibBuilder.loadTexts:
    tFilterRPTTimeout.setUnits("seconds")


class _TFilterRPTDropCount_Type(Unsigned32):
    """Custom type tFilterRPTDropCount based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TFilterRPTDropCount_Type.__name__ = "Unsigned32"
_TFilterRPTDropCount_Object = MibTableColumn
tFilterRPTDropCount = _TFilterRPTDropCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 16, 1, 4),
    _TFilterRPTDropCount_Type()
)
tFilterRPTDropCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRPTDropCount.setStatus("obsolete")


class _TFilterRPTHoldDown_Type(Unsigned32):
    """Custom type tFilterRPTHoldDown based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_TFilterRPTHoldDown_Type.__name__ = "Unsigned32"
_TFilterRPTHoldDown_Object = MibTableColumn
tFilterRPTHoldDown = _TFilterRPTHoldDown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 16, 1, 5),
    _TFilterRPTHoldDown_Type()
)
tFilterRPTHoldDown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRPTHoldDown.setStatus("obsolete")
if mibBuilder.loadTexts:
    tFilterRPTHoldDown.setUnits("seconds")


class _TFilterRPTHoldDownRemain_Type(Unsigned32):
    """Custom type tFilterRPTHoldDownRemain based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_TFilterRPTHoldDownRemain_Type.__name__ = "Unsigned32"
_TFilterRPTHoldDownRemain_Object = MibTableColumn
tFilterRPTHoldDownRemain = _TFilterRPTHoldDownRemain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 16, 1, 6),
    _TFilterRPTHoldDownRemain_Type()
)
tFilterRPTHoldDownRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRPTHoldDownRemain.setStatus("obsolete")
if mibBuilder.loadTexts:
    tFilterRPTHoldDownRemain.setUnits("seconds")
_TFilterRPTLastActionTime_Type = TimeStamp
_TFilterRPTLastActionTime_Object = MibTableColumn
tFilterRPTLastActionTime = _TFilterRPTLastActionTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 16, 1, 7),
    _TFilterRPTLastActionTime_Type()
)
tFilterRPTLastActionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRPTLastActionTime.setStatus("obsolete")


class _TFilterRPTLastAction_Type(Integer32):
    """Custom type tFilterRPTLastAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("none", 3))
    )


_TFilterRPTLastAction_Type.__name__ = "Integer32"
_TFilterRPTLastAction_Object = MibTableColumn
tFilterRPTLastAction = _TFilterRPTLastAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 16, 1, 8),
    _TFilterRPTLastAction_Type()
)
tFilterRPTLastAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRPTLastAction.setStatus("obsolete")
_TAutoIPFilterEntryTable_Object = MibTable
tAutoIPFilterEntryTable = _TAutoIPFilterEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 17)
)
if mibBuilder.loadTexts:
    tAutoIPFilterEntryTable.setStatus("obsolete")
_TAutoIPFilterEntry_Object = MibTableRow
tAutoIPFilterEntry = _TAutoIPFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 17, 1)
)
tAutoIPFilterEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tAutoIPFilterId"),
    (0, "TIMETRA-FILTER-MIB", "tAutoIPFilterEntrySourceIpAddr"),
)
if mibBuilder.loadTexts:
    tAutoIPFilterEntry.setStatus("obsolete")


class _TAutoIPFilterId_Type(TFilterID):
    """Custom type tAutoIPFilterId based on TFilterID"""
    subtypeSpec = TFilterID.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TAutoIPFilterId_Type.__name__ = "TFilterID"
_TAutoIPFilterId_Object = MibTableColumn
tAutoIPFilterId = _TAutoIPFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 17, 1, 1),
    _TAutoIPFilterId_Type()
)
tAutoIPFilterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tAutoIPFilterId.setStatus("obsolete")
_TAutoIPFilterEntrySourceIpAddr_Type = IpAddress
_TAutoIPFilterEntrySourceIpAddr_Object = MibTableColumn
tAutoIPFilterEntrySourceIpAddr = _TAutoIPFilterEntrySourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 17, 1, 2),
    _TAutoIPFilterEntrySourceIpAddr_Type()
)
tAutoIPFilterEntrySourceIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tAutoIPFilterEntrySourceIpAddr.setStatus("obsolete")
_TAutoIPFilterEntrySourceIpMask_Type = IpAddressPrefixLength
_TAutoIPFilterEntrySourceIpMask_Object = MibTableColumn
tAutoIPFilterEntrySourceIpMask = _TAutoIPFilterEntrySourceIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 17, 1, 3),
    _TAutoIPFilterEntrySourceIpMask_Type()
)
tAutoIPFilterEntrySourceIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAutoIPFilterEntrySourceIpMask.setStatus("obsolete")
_TIPv6FilterTable_Object = MibTable
tIPv6FilterTable = _TIPv6FilterTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 18)
)
if mibBuilder.loadTexts:
    tIPv6FilterTable.setStatus("current")
_TIPv6FilterEntry_Object = MibTableRow
tIPv6FilterEntry = _TIPv6FilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 18, 1)
)
tIPv6FilterEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tIPv6FilterId"),
)
if mibBuilder.loadTexts:
    tIPv6FilterEntry.setStatus("current")
_TIPv6FilterId_Type = TAnyFilterID
_TIPv6FilterId_Object = MibTableColumn
tIPv6FilterId = _TIPv6FilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 18, 1, 1),
    _TIPv6FilterId_Type()
)
tIPv6FilterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPv6FilterId.setStatus("current")
_TIPv6FilterRowStatus_Type = RowStatus
_TIPv6FilterRowStatus_Object = MibTableColumn
tIPv6FilterRowStatus = _TIPv6FilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 18, 1, 2),
    _TIPv6FilterRowStatus_Type()
)
tIPv6FilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterRowStatus.setStatus("current")


class _TIPv6FilterScope_Type(TFilterScope):
    """Custom type tIPv6FilterScope based on TFilterScope"""
    defaultValue = 2


_TIPv6FilterScope_Type.__name__ = "TFilterScope"
_TIPv6FilterScope_Object = MibTableColumn
tIPv6FilterScope = _TIPv6FilterScope_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 18, 1, 3),
    _TIPv6FilterScope_Type()
)
tIPv6FilterScope.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterScope.setStatus("current")


class _TIPv6FilterDescription_Type(TItemDescription):
    """Custom type tIPv6FilterDescription based on TItemDescription"""
    defaultHexValue = ""


_TIPv6FilterDescription_Type.__name__ = "TItemDescription"
_TIPv6FilterDescription_Object = MibTableColumn
tIPv6FilterDescription = _TIPv6FilterDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 18, 1, 4),
    _TIPv6FilterDescription_Type()
)
tIPv6FilterDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterDescription.setStatus("current")


class _TIPv6FilterDefaultAction_Type(TFilterAction):
    """Custom type tIPv6FilterDefaultAction based on TFilterAction"""
    defaultValue = 1


_TIPv6FilterDefaultAction_Type.__name__ = "TFilterAction"
_TIPv6FilterDefaultAction_Object = MibTableColumn
tIPv6FilterDefaultAction = _TIPv6FilterDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 18, 1, 5),
    _TIPv6FilterDefaultAction_Type()
)
tIPv6FilterDefaultAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterDefaultAction.setStatus("current")


class _TIPv6FilterRadiusInsertPt_Type(TEntryIdOrZero):
    """Custom type tIPv6FilterRadiusInsertPt based on TEntryIdOrZero"""
    defaultValue = 0


_TIPv6FilterRadiusInsertPt_Type.__name__ = "TEntryIdOrZero"
_TIPv6FilterRadiusInsertPt_Object = MibTableColumn
tIPv6FilterRadiusInsertPt = _TIPv6FilterRadiusInsertPt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 18, 1, 6),
    _TIPv6FilterRadiusInsertPt_Type()
)
tIPv6FilterRadiusInsertPt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterRadiusInsertPt.setStatus("current")


class _TIPv6FilterRadiusInsertSize_Type(TEntryBlockSize):
    """Custom type tIPv6FilterRadiusInsertSize based on TEntryBlockSize"""
    defaultValue = 0


_TIPv6FilterRadiusInsertSize_Type.__name__ = "TEntryBlockSize"
_TIPv6FilterRadiusInsertSize_Object = MibTableColumn
tIPv6FilterRadiusInsertSize = _TIPv6FilterRadiusInsertSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 18, 1, 7),
    _TIPv6FilterRadiusInsertSize_Type()
)
tIPv6FilterRadiusInsertSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterRadiusInsertSize.setStatus("current")


class _TIPv6FilterCreditCntrlInsertPt_Type(TEntryIdOrZero):
    """Custom type tIPv6FilterCreditCntrlInsertPt based on TEntryIdOrZero"""
    defaultValue = 0


_TIPv6FilterCreditCntrlInsertPt_Type.__name__ = "TEntryIdOrZero"
_TIPv6FilterCreditCntrlInsertPt_Object = MibTableColumn
tIPv6FilterCreditCntrlInsertPt = _TIPv6FilterCreditCntrlInsertPt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 18, 1, 8),
    _TIPv6FilterCreditCntrlInsertPt_Type()
)
tIPv6FilterCreditCntrlInsertPt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterCreditCntrlInsertPt.setStatus("current")


class _TIPv6FilterCreditCntrlInsertSize_Type(TEntryBlockSize):
    """Custom type tIPv6FilterCreditCntrlInsertSize based on TEntryBlockSize"""
    defaultValue = 0


_TIPv6FilterCreditCntrlInsertSize_Type.__name__ = "TEntryBlockSize"
_TIPv6FilterCreditCntrlInsertSize_Object = MibTableColumn
tIPv6FilterCreditCntrlInsertSize = _TIPv6FilterCreditCntrlInsertSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 18, 1, 9),
    _TIPv6FilterCreditCntrlInsertSize_Type()
)
tIPv6FilterCreditCntrlInsertSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterCreditCntrlInsertSize.setStatus("current")


class _TIPv6FilterSubInsertHighWmark_Type(Integer32):
    """Custom type tIPv6FilterSubInsertHighWmark based on Integer32"""
    defaultValue = 95

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TIPv6FilterSubInsertHighWmark_Type.__name__ = "Integer32"
_TIPv6FilterSubInsertHighWmark_Object = MibTableColumn
tIPv6FilterSubInsertHighWmark = _TIPv6FilterSubInsertHighWmark_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 18, 1, 10),
    _TIPv6FilterSubInsertHighWmark_Type()
)
tIPv6FilterSubInsertHighWmark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterSubInsertHighWmark.setStatus("current")


class _TIPv6FilterSubInsertLowWmark_Type(Integer32):
    """Custom type tIPv6FilterSubInsertLowWmark based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TIPv6FilterSubInsertLowWmark_Type.__name__ = "Integer32"
_TIPv6FilterSubInsertLowWmark_Object = MibTableColumn
tIPv6FilterSubInsertLowWmark = _TIPv6FilterSubInsertLowWmark_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 18, 1, 11),
    _TIPv6FilterSubInsertLowWmark_Type()
)
tIPv6FilterSubInsertLowWmark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterSubInsertLowWmark.setStatus("current")
_TIpv6FilterCreditCntrlNbrInsertd_Type = Unsigned32
_TIpv6FilterCreditCntrlNbrInsertd_Object = MibTableColumn
tIpv6FilterCreditCntrlNbrInsertd = _TIpv6FilterCreditCntrlNbrInsertd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 18, 1, 12),
    _TIpv6FilterCreditCntrlNbrInsertd_Type()
)
tIpv6FilterCreditCntrlNbrInsertd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIpv6FilterCreditCntrlNbrInsertd.setStatus("current")
_TIpv6FilterRadiusNbrInsertd_Type = Unsigned32
_TIpv6FilterRadiusNbrInsertd_Object = MibTableColumn
tIpv6FilterRadiusNbrInsertd = _TIpv6FilterRadiusNbrInsertd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 18, 1, 13),
    _TIpv6FilterRadiusNbrInsertd_Type()
)
tIpv6FilterRadiusNbrInsertd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIpv6FilterRadiusNbrInsertd.setStatus("current")


class _TIpv6FilterName_Type(TLNamedItemOrEmpty):
    """Custom type tIpv6FilterName based on TLNamedItemOrEmpty"""
    defaultHexValue = ""


_TIpv6FilterName_Type.__name__ = "TLNamedItemOrEmpty"
_TIpv6FilterName_Object = MibTableColumn
tIpv6FilterName = _TIpv6FilterName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 18, 1, 14),
    _TIpv6FilterName_Type()
)
tIpv6FilterName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIpv6FilterName.setStatus("current")


class _TIPv6FilterHostSharedInsertPt_Type(TEntryIdOrZero):
    """Custom type tIPv6FilterHostSharedInsertPt based on TEntryIdOrZero"""
    defaultValue = 0


_TIPv6FilterHostSharedInsertPt_Type.__name__ = "TEntryIdOrZero"
_TIPv6FilterHostSharedInsertPt_Object = MibTableColumn
tIPv6FilterHostSharedInsertPt = _TIPv6FilterHostSharedInsertPt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 18, 1, 15),
    _TIPv6FilterHostSharedInsertPt_Type()
)
tIPv6FilterHostSharedInsertPt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterHostSharedInsertPt.setStatus("current")


class _TIPv6FilterHostSharedInsertSize_Type(TEntryBlockSize):
    """Custom type tIPv6FilterHostSharedInsertSize based on TEntryBlockSize"""
    defaultValue = 0


_TIPv6FilterHostSharedInsertSize_Type.__name__ = "TEntryBlockSize"
_TIPv6FilterHostSharedInsertSize_Object = MibTableColumn
tIPv6FilterHostSharedInsertSize = _TIPv6FilterHostSharedInsertSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 18, 1, 16),
    _TIPv6FilterHostSharedInsertSize_Type()
)
tIPv6FilterHostSharedInsertSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterHostSharedInsertSize.setStatus("current")
_TIpv6FilterHostSharedNbrInsertd_Type = Unsigned32
_TIpv6FilterHostSharedNbrInsertd_Object = MibTableColumn
tIpv6FilterHostSharedNbrInsertd = _TIpv6FilterHostSharedNbrInsertd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 18, 1, 17),
    _TIpv6FilterHostSharedNbrInsertd_Type()
)
tIpv6FilterHostSharedNbrInsertd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIpv6FilterHostSharedNbrInsertd.setStatus("current")


class _TIPv6FilterHostSharedHighWmark_Type(Integer32):
    """Custom type tIPv6FilterHostSharedHighWmark based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 8000),
    )


_TIPv6FilterHostSharedHighWmark_Type.__name__ = "Integer32"
_TIPv6FilterHostSharedHighWmark_Object = MibTableColumn
tIPv6FilterHostSharedHighWmark = _TIPv6FilterHostSharedHighWmark_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 18, 1, 18),
    _TIPv6FilterHostSharedHighWmark_Type()
)
tIPv6FilterHostSharedHighWmark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterHostSharedHighWmark.setStatus("current")


class _TIPv6FilterHostSharedLowWmark_Type(Integer32):
    """Custom type tIPv6FilterHostSharedLowWmark based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 8000),
    )


_TIPv6FilterHostSharedLowWmark_Type.__name__ = "Integer32"
_TIPv6FilterHostSharedLowWmark_Object = MibTableColumn
tIPv6FilterHostSharedLowWmark = _TIPv6FilterHostSharedLowWmark_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 18, 1, 19),
    _TIPv6FilterHostSharedLowWmark_Type()
)
tIPv6FilterHostSharedLowWmark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterHostSharedLowWmark.setStatus("current")
_TIPv6FilterNbrHostSharedFltrs_Type = Unsigned32
_TIPv6FilterNbrHostSharedFltrs_Object = MibTableColumn
tIPv6FilterNbrHostSharedFltrs = _TIPv6FilterNbrHostSharedFltrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 18, 1, 20),
    _TIPv6FilterNbrHostSharedFltrs_Type()
)
tIPv6FilterNbrHostSharedFltrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPv6FilterNbrHostSharedFltrs.setStatus("current")


class _TIPv6FilterSharedPccRuleInsrtPt_Type(TEntryIdOrZero):
    """Custom type tIPv6FilterSharedPccRuleInsrtPt based on TEntryIdOrZero"""
    defaultValue = 0


_TIPv6FilterSharedPccRuleInsrtPt_Type.__name__ = "TEntryIdOrZero"
_TIPv6FilterSharedPccRuleInsrtPt_Object = MibTableColumn
tIPv6FilterSharedPccRuleInsrtPt = _TIPv6FilterSharedPccRuleInsrtPt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 18, 1, 21),
    _TIPv6FilterSharedPccRuleInsrtPt_Type()
)
tIPv6FilterSharedPccRuleInsrtPt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterSharedPccRuleInsrtPt.setStatus("current")


class _TIPv6FilterSharedPccRuleInsrtSiz_Type(TEntryBlockSize):
    """Custom type tIPv6FilterSharedPccRuleInsrtSiz based on TEntryBlockSize"""
    defaultValue = 0


_TIPv6FilterSharedPccRuleInsrtSiz_Type.__name__ = "TEntryBlockSize"
_TIPv6FilterSharedPccRuleInsrtSiz_Object = MibTableColumn
tIPv6FilterSharedPccRuleInsrtSiz = _TIPv6FilterSharedPccRuleInsrtSiz_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 18, 1, 22),
    _TIPv6FilterSharedPccRuleInsrtSiz_Type()
)
tIPv6FilterSharedPccRuleInsrtSiz.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterSharedPccRuleInsrtSiz.setStatus("current")
_TIPv6FilterSharedPccRuleNbrInsrt_Type = Unsigned32
_TIPv6FilterSharedPccRuleNbrInsrt_Object = MibTableColumn
tIPv6FilterSharedPccRuleNbrInsrt = _TIPv6FilterSharedPccRuleNbrInsrt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 18, 1, 23),
    _TIPv6FilterSharedPccRuleNbrInsrt_Type()
)
tIPv6FilterSharedPccRuleNbrInsrt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPv6FilterSharedPccRuleNbrInsrt.setStatus("current")


class _TIPv6FilterChainToSystemFilter_Type(TruthValue):
    """Custom type tIPv6FilterChainToSystemFilter based on TruthValue"""
    defaultValue = 2


_TIPv6FilterChainToSystemFilter_Type.__name__ = "TruthValue"
_TIPv6FilterChainToSystemFilter_Object = MibTableColumn
tIPv6FilterChainToSystemFilter = _TIPv6FilterChainToSystemFilter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 18, 1, 24),
    _TIPv6FilterChainToSystemFilter_Type()
)
tIPv6FilterChainToSystemFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterChainToSystemFilter.setStatus("current")


class _TIPv6FilterType_Type(TIPvXFilterType):
    """Custom type tIPv6FilterType based on TIPvXFilterType"""
    defaultValue = 0


_TIPv6FilterType_Type.__name__ = "TIPvXFilterType"
_TIPv6FilterType_Object = MibTableColumn
tIPv6FilterType = _TIPv6FilterType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 18, 1, 25),
    _TIPv6FilterType_Type()
)
tIPv6FilterType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterType.setStatus("current")
_TIPv6FilterParamsTable_Object = MibTable
tIPv6FilterParamsTable = _TIPv6FilterParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19)
)
if mibBuilder.loadTexts:
    tIPv6FilterParamsTable.setStatus("current")
_TIPv6FilterParamsEntry_Object = MibTableRow
tIPv6FilterParamsEntry = _TIPv6FilterParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1)
)
tIPv6FilterParamsEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tIPv6FilterId"),
    (0, "TIMETRA-FILTER-MIB", "tIPv6FilterParamsIndex"),
)
if mibBuilder.loadTexts:
    tIPv6FilterParamsEntry.setStatus("current")
_TIPv6FilterParamsIndex_Type = TEntryId
_TIPv6FilterParamsIndex_Object = MibTableColumn
tIPv6FilterParamsIndex = _TIPv6FilterParamsIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 1),
    _TIPv6FilterParamsIndex_Type()
)
tIPv6FilterParamsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPv6FilterParamsIndex.setStatus("current")
_TIPv6FilterParamsRowStatus_Type = RowStatus
_TIPv6FilterParamsRowStatus_Object = MibTableColumn
tIPv6FilterParamsRowStatus = _TIPv6FilterParamsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 2),
    _TIPv6FilterParamsRowStatus_Type()
)
tIPv6FilterParamsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsRowStatus.setStatus("current")


class _TIPv6FilterParamsLogId_Type(TFilterLogId):
    """Custom type tIPv6FilterParamsLogId based on TFilterLogId"""
    defaultValue = 0


_TIPv6FilterParamsLogId_Type.__name__ = "TFilterLogId"
_TIPv6FilterParamsLogId_Object = MibTableColumn
tIPv6FilterParamsLogId = _TIPv6FilterParamsLogId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 3),
    _TIPv6FilterParamsLogId_Type()
)
tIPv6FilterParamsLogId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsLogId.setStatus("current")


class _TIPv6FilterParamsDescription_Type(TItemDescription):
    """Custom type tIPv6FilterParamsDescription based on TItemDescription"""
    defaultHexValue = ""


_TIPv6FilterParamsDescription_Type.__name__ = "TItemDescription"
_TIPv6FilterParamsDescription_Object = MibTableColumn
tIPv6FilterParamsDescription = _TIPv6FilterParamsDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 4),
    _TIPv6FilterParamsDescription_Type()
)
tIPv6FilterParamsDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsDescription.setStatus("current")


class _TIPv6FilterParamsAction_Type(TFilterActionOrDefault):
    """Custom type tIPv6FilterParamsAction based on TFilterActionOrDefault"""
    defaultValue = 30


_TIPv6FilterParamsAction_Type.__name__ = "TFilterActionOrDefault"
_TIPv6FilterParamsAction_Object = MibTableColumn
tIPv6FilterParamsAction = _TIPv6FilterParamsAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 5),
    _TIPv6FilterParamsAction_Type()
)
tIPv6FilterParamsAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsAction.setStatus("obsolete")


class _TIPv6FilterParamsForwardNH_Type(InetAddressIPv6):
    """Custom type tIPv6FilterParamsForwardNH based on InetAddressIPv6"""
    defaultHexValue = "00000000000000000000000000000000"


_TIPv6FilterParamsForwardNH_Type.__name__ = "InetAddressIPv6"
_TIPv6FilterParamsForwardNH_Object = MibTableColumn
tIPv6FilterParamsForwardNH = _TIPv6FilterParamsForwardNH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 6),
    _TIPv6FilterParamsForwardNH_Type()
)
tIPv6FilterParamsForwardNH.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsForwardNH.setStatus("obsolete")


class _TIPv6FilterParamsForwardNHIndirect_Type(TruthValue):
    """Custom type tIPv6FilterParamsForwardNHIndirect based on TruthValue"""
    defaultValue = 2


_TIPv6FilterParamsForwardNHIndirect_Type.__name__ = "TruthValue"
_TIPv6FilterParamsForwardNHIndirect_Object = MibTableColumn
tIPv6FilterParamsForwardNHIndirect = _TIPv6FilterParamsForwardNHIndirect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 7),
    _TIPv6FilterParamsForwardNHIndirect_Type()
)
tIPv6FilterParamsForwardNHIndirect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsForwardNHIndirect.setStatus("obsolete")


class _TIPv6FilterParamsRemarkDSCP_Type(TDSCPFilterActionValue):
    """Custom type tIPv6FilterParamsRemarkDSCP based on TDSCPFilterActionValue"""
    defaultValue = -1


_TIPv6FilterParamsRemarkDSCP_Type.__name__ = "TDSCPFilterActionValue"
_TIPv6FilterParamsRemarkDSCP_Object = MibTableColumn
tIPv6FilterParamsRemarkDSCP = _TIPv6FilterParamsRemarkDSCP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 8),
    _TIPv6FilterParamsRemarkDSCP_Type()
)
tIPv6FilterParamsRemarkDSCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsRemarkDSCP.setStatus("obsolete")


class _TIPv6FilterParamsRemarkDSCPMask_Type(TDSCPFilterActionValue):
    """Custom type tIPv6FilterParamsRemarkDSCPMask based on TDSCPFilterActionValue"""
    defaultValue = 255


_TIPv6FilterParamsRemarkDSCPMask_Type.__name__ = "TDSCPFilterActionValue"
_TIPv6FilterParamsRemarkDSCPMask_Object = MibTableColumn
tIPv6FilterParamsRemarkDSCPMask = _TIPv6FilterParamsRemarkDSCPMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 9),
    _TIPv6FilterParamsRemarkDSCPMask_Type()
)
tIPv6FilterParamsRemarkDSCPMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsRemarkDSCPMask.setStatus("obsolete")


class _TIPv6FilterParamsRemarkDot1p_Type(Dot1PPriority):
    """Custom type tIPv6FilterParamsRemarkDot1p based on Dot1PPriority"""
    defaultValue = -1


_TIPv6FilterParamsRemarkDot1p_Type.__name__ = "Dot1PPriority"
_TIPv6FilterParamsRemarkDot1p_Object = MibTableColumn
tIPv6FilterParamsRemarkDot1p = _TIPv6FilterParamsRemarkDot1p_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 10),
    _TIPv6FilterParamsRemarkDot1p_Type()
)
tIPv6FilterParamsRemarkDot1p.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsRemarkDot1p.setStatus("obsolete")


class _TIPv6FilterParamsSourceIpAddr_Type(InetAddressIPv6):
    """Custom type tIPv6FilterParamsSourceIpAddr based on InetAddressIPv6"""
    defaultHexValue = "00000000000000000000000000000000"


_TIPv6FilterParamsSourceIpAddr_Type.__name__ = "InetAddressIPv6"
_TIPv6FilterParamsSourceIpAddr_Object = MibTableColumn
tIPv6FilterParamsSourceIpAddr = _TIPv6FilterParamsSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 11),
    _TIPv6FilterParamsSourceIpAddr_Type()
)
tIPv6FilterParamsSourceIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsSourceIpAddr.setStatus("current")


class _TIPv6FilterParamsSourceIpMask_Type(InetAddressPrefixLength):
    """Custom type tIPv6FilterParamsSourceIpMask based on InetAddressPrefixLength"""
    defaultValue = 0

    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_TIPv6FilterParamsSourceIpMask_Type.__name__ = "InetAddressPrefixLength"
_TIPv6FilterParamsSourceIpMask_Object = MibTableColumn
tIPv6FilterParamsSourceIpMask = _TIPv6FilterParamsSourceIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 12),
    _TIPv6FilterParamsSourceIpMask_Type()
)
tIPv6FilterParamsSourceIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsSourceIpMask.setStatus("current")


class _TIPv6FilterParamsDestinationIpAddr_Type(InetAddressIPv6):
    """Custom type tIPv6FilterParamsDestinationIpAddr based on InetAddressIPv6"""
    defaultHexValue = "00000000000000000000000000000000"


_TIPv6FilterParamsDestinationIpAddr_Type.__name__ = "InetAddressIPv6"
_TIPv6FilterParamsDestinationIpAddr_Object = MibTableColumn
tIPv6FilterParamsDestinationIpAddr = _TIPv6FilterParamsDestinationIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 13),
    _TIPv6FilterParamsDestinationIpAddr_Type()
)
tIPv6FilterParamsDestinationIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsDestinationIpAddr.setStatus("current")


class _TIPv6FilterParamsDestinationIpMask_Type(InetAddressPrefixLength):
    """Custom type tIPv6FilterParamsDestinationIpMask based on InetAddressPrefixLength"""
    defaultValue = 0

    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_TIPv6FilterParamsDestinationIpMask_Type.__name__ = "InetAddressPrefixLength"
_TIPv6FilterParamsDestinationIpMask_Object = MibTableColumn
tIPv6FilterParamsDestinationIpMask = _TIPv6FilterParamsDestinationIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 14),
    _TIPv6FilterParamsDestinationIpMask_Type()
)
tIPv6FilterParamsDestinationIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsDestinationIpMask.setStatus("current")


class _TIPv6FilterParamsNextHeader_Type(TIpProtocol):
    """Custom type tIPv6FilterParamsNextHeader based on TIpProtocol"""
    defaultValue = -1


_TIPv6FilterParamsNextHeader_Type.__name__ = "TIpProtocol"
_TIPv6FilterParamsNextHeader_Object = MibTableColumn
tIPv6FilterParamsNextHeader = _TIPv6FilterParamsNextHeader_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 15),
    _TIPv6FilterParamsNextHeader_Type()
)
tIPv6FilterParamsNextHeader.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsNextHeader.setStatus("current")


class _TIPv6FilterParamsSourcePortValue1_Type(TTcpUdpPort):
    """Custom type tIPv6FilterParamsSourcePortValue1 based on TTcpUdpPort"""
    defaultValue = 0


_TIPv6FilterParamsSourcePortValue1_Type.__name__ = "TTcpUdpPort"
_TIPv6FilterParamsSourcePortValue1_Object = MibTableColumn
tIPv6FilterParamsSourcePortValue1 = _TIPv6FilterParamsSourcePortValue1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 16),
    _TIPv6FilterParamsSourcePortValue1_Type()
)
tIPv6FilterParamsSourcePortValue1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsSourcePortValue1.setStatus("current")


class _TIPv6FilterParamsSourcePortValue2_Type(TTcpUdpPort):
    """Custom type tIPv6FilterParamsSourcePortValue2 based on TTcpUdpPort"""
    defaultValue = 0


_TIPv6FilterParamsSourcePortValue2_Type.__name__ = "TTcpUdpPort"
_TIPv6FilterParamsSourcePortValue2_Object = MibTableColumn
tIPv6FilterParamsSourcePortValue2 = _TIPv6FilterParamsSourcePortValue2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 17),
    _TIPv6FilterParamsSourcePortValue2_Type()
)
tIPv6FilterParamsSourcePortValue2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsSourcePortValue2.setStatus("current")


class _TIPv6FilterParamsSourcePortOperator_Type(TOperator):
    """Custom type tIPv6FilterParamsSourcePortOperator based on TOperator"""
    defaultValue = 0


_TIPv6FilterParamsSourcePortOperator_Type.__name__ = "TOperator"
_TIPv6FilterParamsSourcePortOperator_Object = MibTableColumn
tIPv6FilterParamsSourcePortOperator = _TIPv6FilterParamsSourcePortOperator_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 18),
    _TIPv6FilterParamsSourcePortOperator_Type()
)
tIPv6FilterParamsSourcePortOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsSourcePortOperator.setStatus("current")


class _TIPv6FilterParamsDestPortValue1_Type(TTcpUdpPort):
    """Custom type tIPv6FilterParamsDestPortValue1 based on TTcpUdpPort"""
    defaultValue = 0


_TIPv6FilterParamsDestPortValue1_Type.__name__ = "TTcpUdpPort"
_TIPv6FilterParamsDestPortValue1_Object = MibTableColumn
tIPv6FilterParamsDestPortValue1 = _TIPv6FilterParamsDestPortValue1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 19),
    _TIPv6FilterParamsDestPortValue1_Type()
)
tIPv6FilterParamsDestPortValue1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsDestPortValue1.setStatus("current")


class _TIPv6FilterParamsDestPortValue2_Type(TTcpUdpPort):
    """Custom type tIPv6FilterParamsDestPortValue2 based on TTcpUdpPort"""
    defaultValue = 0


_TIPv6FilterParamsDestPortValue2_Type.__name__ = "TTcpUdpPort"
_TIPv6FilterParamsDestPortValue2_Object = MibTableColumn
tIPv6FilterParamsDestPortValue2 = _TIPv6FilterParamsDestPortValue2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 20),
    _TIPv6FilterParamsDestPortValue2_Type()
)
tIPv6FilterParamsDestPortValue2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsDestPortValue2.setStatus("current")


class _TIPv6FilterParamsDestPortOperator_Type(TOperator):
    """Custom type tIPv6FilterParamsDestPortOperator based on TOperator"""
    defaultValue = 0


_TIPv6FilterParamsDestPortOperator_Type.__name__ = "TOperator"
_TIPv6FilterParamsDestPortOperator_Object = MibTableColumn
tIPv6FilterParamsDestPortOperator = _TIPv6FilterParamsDestPortOperator_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 21),
    _TIPv6FilterParamsDestPortOperator_Type()
)
tIPv6FilterParamsDestPortOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsDestPortOperator.setStatus("current")


class _TIPv6FilterParamsDSCP_Type(TDSCPNameOrEmpty):
    """Custom type tIPv6FilterParamsDSCP based on TDSCPNameOrEmpty"""
    defaultHexValue = ""


_TIPv6FilterParamsDSCP_Type.__name__ = "TDSCPNameOrEmpty"
_TIPv6FilterParamsDSCP_Object = MibTableColumn
tIPv6FilterParamsDSCP = _TIPv6FilterParamsDSCP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 22),
    _TIPv6FilterParamsDSCP_Type()
)
tIPv6FilterParamsDSCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsDSCP.setStatus("current")


class _TIPv6FilterParamsTcpSyn_Type(TItemMatch):
    """Custom type tIPv6FilterParamsTcpSyn based on TItemMatch"""
    defaultValue = 1


_TIPv6FilterParamsTcpSyn_Type.__name__ = "TItemMatch"
_TIPv6FilterParamsTcpSyn_Object = MibTableColumn
tIPv6FilterParamsTcpSyn = _TIPv6FilterParamsTcpSyn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 23),
    _TIPv6FilterParamsTcpSyn_Type()
)
tIPv6FilterParamsTcpSyn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsTcpSyn.setStatus("current")


class _TIPv6FilterParamsTcpAck_Type(TItemMatch):
    """Custom type tIPv6FilterParamsTcpAck based on TItemMatch"""
    defaultValue = 1


_TIPv6FilterParamsTcpAck_Type.__name__ = "TItemMatch"
_TIPv6FilterParamsTcpAck_Object = MibTableColumn
tIPv6FilterParamsTcpAck = _TIPv6FilterParamsTcpAck_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 24),
    _TIPv6FilterParamsTcpAck_Type()
)
tIPv6FilterParamsTcpAck.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsTcpAck.setStatus("current")


class _TIPv6FilterParamsIcmpCode_Type(TIcmpCodeOrNone):
    """Custom type tIPv6FilterParamsIcmpCode based on TIcmpCodeOrNone"""
    defaultValue = -1


_TIPv6FilterParamsIcmpCode_Type.__name__ = "TIcmpCodeOrNone"
_TIPv6FilterParamsIcmpCode_Object = MibTableColumn
tIPv6FilterParamsIcmpCode = _TIPv6FilterParamsIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 25),
    _TIPv6FilterParamsIcmpCode_Type()
)
tIPv6FilterParamsIcmpCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsIcmpCode.setStatus("current")


class _TIPv6FilterParamsIcmpType_Type(TIcmpTypeOrNone):
    """Custom type tIPv6FilterParamsIcmpType based on TIcmpTypeOrNone"""
    defaultValue = -1


_TIPv6FilterParamsIcmpType_Type.__name__ = "TIcmpTypeOrNone"
_TIPv6FilterParamsIcmpType_Object = MibTableColumn
tIPv6FilterParamsIcmpType = _TIPv6FilterParamsIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 26),
    _TIPv6FilterParamsIcmpType_Type()
)
tIPv6FilterParamsIcmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsIcmpType.setStatus("current")


class _TIPv6FilterParamsCflowdSample_Type(TruthValue):
    """Custom type tIPv6FilterParamsCflowdSample based on TruthValue"""
    defaultValue = 2


_TIPv6FilterParamsCflowdSample_Type.__name__ = "TruthValue"
_TIPv6FilterParamsCflowdSample_Object = MibTableColumn
tIPv6FilterParamsCflowdSample = _TIPv6FilterParamsCflowdSample_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 27),
    _TIPv6FilterParamsCflowdSample_Type()
)
tIPv6FilterParamsCflowdSample.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsCflowdSample.setStatus("current")


class _TIPv6FilterParamsCflowdIfSample_Type(TruthValue):
    """Custom type tIPv6FilterParamsCflowdIfSample based on TruthValue"""
    defaultValue = 1


_TIPv6FilterParamsCflowdIfSample_Type.__name__ = "TruthValue"
_TIPv6FilterParamsCflowdIfSample_Object = MibTableColumn
tIPv6FilterParamsCflowdIfSample = _TIPv6FilterParamsCflowdIfSample_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 28),
    _TIPv6FilterParamsCflowdIfSample_Type()
)
tIPv6FilterParamsCflowdIfSample.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsCflowdIfSample.setStatus("current")


class _TIPv6FilterParamsForwardNHInterface_Type(DisplayString):
    """Custom type tIPv6FilterParamsForwardNHInterface based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TIPv6FilterParamsForwardNHInterface_Type.__name__ = "DisplayString"
_TIPv6FilterParamsForwardNHInterface_Object = MibTableColumn
tIPv6FilterParamsForwardNHInterface = _TIPv6FilterParamsForwardNHInterface_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 29),
    _TIPv6FilterParamsForwardNHInterface_Type()
)
tIPv6FilterParamsForwardNHInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsForwardNHInterface.setStatus("obsolete")
_TIPv6FilterParamsIngressHitCount_Type = Counter64
_TIPv6FilterParamsIngressHitCount_Object = MibTableColumn
tIPv6FilterParamsIngressHitCount = _TIPv6FilterParamsIngressHitCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 30),
    _TIPv6FilterParamsIngressHitCount_Type()
)
tIPv6FilterParamsIngressHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPv6FilterParamsIngressHitCount.setStatus("current")
_TIPv6FilterParamsEgressHitCount_Type = Counter64
_TIPv6FilterParamsEgressHitCount_Object = MibTableColumn
tIPv6FilterParamsEgressHitCount = _TIPv6FilterParamsEgressHitCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 31),
    _TIPv6FilterParamsEgressHitCount_Type()
)
tIPv6FilterParamsEgressHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPv6FilterParamsEgressHitCount.setStatus("current")
_TIPv6FilterParamsLogInstantiated_Type = TruthValue
_TIPv6FilterParamsLogInstantiated_Object = MibTableColumn
tIPv6FilterParamsLogInstantiated = _TIPv6FilterParamsLogInstantiated_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 32),
    _TIPv6FilterParamsLogInstantiated_Type()
)
tIPv6FilterParamsLogInstantiated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPv6FilterParamsLogInstantiated.setStatus("current")


class _TIPv6FilterParamsForwardRedPlcy_Type(TNamedItemOrEmpty):
    """Custom type tIPv6FilterParamsForwardRedPlcy based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TIPv6FilterParamsForwardRedPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TIPv6FilterParamsForwardRedPlcy_Object = MibTableColumn
tIPv6FilterParamsForwardRedPlcy = _TIPv6FilterParamsForwardRedPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 33),
    _TIPv6FilterParamsForwardRedPlcy_Type()
)
tIPv6FilterParamsForwardRedPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsForwardRedPlcy.setStatus("obsolete")
_TIPv6FilterParamsActiveDest_Type = InetAddressIPv6
_TIPv6FilterParamsActiveDest_Object = MibTableColumn
tIPv6FilterParamsActiveDest = _TIPv6FilterParamsActiveDest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 34),
    _TIPv6FilterParamsActiveDest_Type()
)
tIPv6FilterParamsActiveDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPv6FilterParamsActiveDest.setStatus("current")


class _TIPv6FilterParamsTimeRangeName_Type(TNamedItemOrEmpty):
    """Custom type tIPv6FilterParamsTimeRangeName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TIPv6FilterParamsTimeRangeName_Type.__name__ = "TNamedItemOrEmpty"
_TIPv6FilterParamsTimeRangeName_Object = MibTableColumn
tIPv6FilterParamsTimeRangeName = _TIPv6FilterParamsTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 35),
    _TIPv6FilterParamsTimeRangeName_Type()
)
tIPv6FilterParamsTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsTimeRangeName.setStatus("obsolete")
_TIPv6FilterParamsTimeRangeState_Type = TTimeRangeState
_TIPv6FilterParamsTimeRangeState_Object = MibTableColumn
tIPv6FilterParamsTimeRangeState = _TIPv6FilterParamsTimeRangeState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 36),
    _TIPv6FilterParamsTimeRangeState_Type()
)
tIPv6FilterParamsTimeRangeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPv6FilterParamsTimeRangeState.setStatus("obsolete")
_TIPv6FilterParamsIngrHitByteCount_Type = Counter64
_TIPv6FilterParamsIngrHitByteCount_Object = MibTableColumn
tIPv6FilterParamsIngrHitByteCount = _TIPv6FilterParamsIngrHitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 37),
    _TIPv6FilterParamsIngrHitByteCount_Type()
)
tIPv6FilterParamsIngrHitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPv6FilterParamsIngrHitByteCount.setStatus("current")
_TIPv6FilterParamsEgrHitByteCount_Type = Counter64
_TIPv6FilterParamsEgrHitByteCount_Object = MibTableColumn
tIPv6FilterParamsEgrHitByteCount = _TIPv6FilterParamsEgrHitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 38),
    _TIPv6FilterParamsEgrHitByteCount_Type()
)
tIPv6FilterParamsEgrHitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPv6FilterParamsEgrHitByteCount.setStatus("current")
_TIPv6FilterParamsFwdSvcId_Type = TmnxServId
_TIPv6FilterParamsFwdSvcId_Object = MibTableColumn
tIPv6FilterParamsFwdSvcId = _TIPv6FilterParamsFwdSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 39),
    _TIPv6FilterParamsFwdSvcId_Type()
)
tIPv6FilterParamsFwdSvcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPv6FilterParamsFwdSvcId.setStatus("current")


class _TIPv6FilterParamsFwdSapPortId_Type(TmnxPortID):
    """Custom type tIPv6FilterParamsFwdSapPortId based on TmnxPortID"""
    defaultValue = 0


_TIPv6FilterParamsFwdSapPortId_Type.__name__ = "TmnxPortID"
_TIPv6FilterParamsFwdSapPortId_Object = MibTableColumn
tIPv6FilterParamsFwdSapPortId = _TIPv6FilterParamsFwdSapPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 40),
    _TIPv6FilterParamsFwdSapPortId_Type()
)
tIPv6FilterParamsFwdSapPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsFwdSapPortId.setStatus("obsolete")


class _TIPv6FilterParamsFwdSapEncapVal_Type(TmnxEncapVal):
    """Custom type tIPv6FilterParamsFwdSapEncapVal based on TmnxEncapVal"""
    defaultValue = 0


_TIPv6FilterParamsFwdSapEncapVal_Type.__name__ = "TmnxEncapVal"
_TIPv6FilterParamsFwdSapEncapVal_Object = MibTableColumn
tIPv6FilterParamsFwdSapEncapVal = _TIPv6FilterParamsFwdSapEncapVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 41),
    _TIPv6FilterParamsFwdSapEncapVal_Type()
)
tIPv6FilterParamsFwdSapEncapVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsFwdSapEncapVal.setStatus("obsolete")


class _TIPv6FilterParamsFwdSdpBind_Type(SdpBindId):
    """Custom type tIPv6FilterParamsFwdSdpBind based on SdpBindId"""
    defaultHexValue = "0000000000000000"


_TIPv6FilterParamsFwdSdpBind_Type.__name__ = "SdpBindId"
_TIPv6FilterParamsFwdSdpBind_Object = MibTableColumn
tIPv6FilterParamsFwdSdpBind = _TIPv6FilterParamsFwdSdpBind_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 42),
    _TIPv6FilterParamsFwdSdpBind_Type()
)
tIPv6FilterParamsFwdSdpBind.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsFwdSdpBind.setStatus("obsolete")


class _TIPv6FilterParamsRedirectURL_Type(TmnxHttpRedirectUrl):
    """Custom type tIPv6FilterParamsRedirectURL based on TmnxHttpRedirectUrl"""
    defaultHexValue = ""


_TIPv6FilterParamsRedirectURL_Type.__name__ = "TmnxHttpRedirectUrl"
_TIPv6FilterParamsRedirectURL_Object = MibTableColumn
tIPv6FilterParamsRedirectURL = _TIPv6FilterParamsRedirectURL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 43),
    _TIPv6FilterParamsRedirectURL_Type()
)
tIPv6FilterParamsRedirectURL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsRedirectURL.setStatus("obsolete")


class _TIPv6FilterParamsSrcIpPrefixList_Type(TNamedItemOrEmpty):
    """Custom type tIPv6FilterParamsSrcIpPrefixList based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TIPv6FilterParamsSrcIpPrefixList_Type.__name__ = "TNamedItemOrEmpty"
_TIPv6FilterParamsSrcIpPrefixList_Object = MibTableColumn
tIPv6FilterParamsSrcIpPrefixList = _TIPv6FilterParamsSrcIpPrefixList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 44),
    _TIPv6FilterParamsSrcIpPrefixList_Type()
)
tIPv6FilterParamsSrcIpPrefixList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsSrcIpPrefixList.setStatus("current")


class _TIPv6FilterParamsDstIpPrefixList_Type(TNamedItemOrEmpty):
    """Custom type tIPv6FilterParamsDstIpPrefixList based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TIPv6FilterParamsDstIpPrefixList_Type.__name__ = "TNamedItemOrEmpty"
_TIPv6FilterParamsDstIpPrefixList_Object = MibTableColumn
tIPv6FilterParamsDstIpPrefixList = _TIPv6FilterParamsDstIpPrefixList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 45),
    _TIPv6FilterParamsDstIpPrefixList_Type()
)
tIPv6FilterParamsDstIpPrefixList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsDstIpPrefixList.setStatus("current")


class _TIPv6FilterParamsFragment_Type(TFragmentMatch):
    """Custom type tIPv6FilterParamsFragment based on TFragmentMatch"""
    defaultValue = 1


_TIPv6FilterParamsFragment_Type.__name__ = "TFragmentMatch"
_TIPv6FilterParamsFragment_Object = MibTableColumn
tIPv6FilterParamsFragment = _TIPv6FilterParamsFragment_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 46),
    _TIPv6FilterParamsFragment_Type()
)
tIPv6FilterParamsFragment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsFragment.setStatus("current")


class _TIPv6FilterParamsHopByHopOpt_Type(TItemMatch):
    """Custom type tIPv6FilterParamsHopByHopOpt based on TItemMatch"""
    defaultValue = 1


_TIPv6FilterParamsHopByHopOpt_Type.__name__ = "TItemMatch"
_TIPv6FilterParamsHopByHopOpt_Object = MibTableColumn
tIPv6FilterParamsHopByHopOpt = _TIPv6FilterParamsHopByHopOpt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 47),
    _TIPv6FilterParamsHopByHopOpt_Type()
)
tIPv6FilterParamsHopByHopOpt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsHopByHopOpt.setStatus("current")


class _TIPv6FilterParamsRoutingType0_Type(TItemMatch):
    """Custom type tIPv6FilterParamsRoutingType0 based on TItemMatch"""
    defaultValue = 1


_TIPv6FilterParamsRoutingType0_Type.__name__ = "TItemMatch"
_TIPv6FilterParamsRoutingType0_Object = MibTableColumn
tIPv6FilterParamsRoutingType0 = _TIPv6FilterParamsRoutingType0_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 48),
    _TIPv6FilterParamsRoutingType0_Type()
)
tIPv6FilterParamsRoutingType0.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsRoutingType0.setStatus("current")


class _TIPv6FilterParamsPortSelector_Type(TFltrPortSelector):
    """Custom type tIPv6FilterParamsPortSelector based on TFltrPortSelector"""
    defaultValue = 0


_TIPv6FilterParamsPortSelector_Type.__name__ = "TFltrPortSelector"
_TIPv6FilterParamsPortSelector_Object = MibTableColumn
tIPv6FilterParamsPortSelector = _TIPv6FilterParamsPortSelector_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 49),
    _TIPv6FilterParamsPortSelector_Type()
)
tIPv6FilterParamsPortSelector.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsPortSelector.setStatus("current")


class _TIPv6FilterParamsSrcPortList_Type(TNamedItemOrEmpty):
    """Custom type tIPv6FilterParamsSrcPortList based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TIPv6FilterParamsSrcPortList_Type.__name__ = "TNamedItemOrEmpty"
_TIPv6FilterParamsSrcPortList_Object = MibTableColumn
tIPv6FilterParamsSrcPortList = _TIPv6FilterParamsSrcPortList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 50),
    _TIPv6FilterParamsSrcPortList_Type()
)
tIPv6FilterParamsSrcPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsSrcPortList.setStatus("current")


class _TIPv6FilterParamsDstPortList_Type(TNamedItemOrEmpty):
    """Custom type tIPv6FilterParamsDstPortList based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TIPv6FilterParamsDstPortList_Type.__name__ = "TNamedItemOrEmpty"
_TIPv6FilterParamsDstPortList_Object = MibTableColumn
tIPv6FilterParamsDstPortList = _TIPv6FilterParamsDstPortList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 51),
    _TIPv6FilterParamsDstPortList_Type()
)
tIPv6FilterParamsDstPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsDstPortList.setStatus("current")


class _TIPv6FilterParamsRdirAllwRadOvrd_Type(TruthValue):
    """Custom type tIPv6FilterParamsRdirAllwRadOvrd based on TruthValue"""
    defaultValue = 2


_TIPv6FilterParamsRdirAllwRadOvrd_Type.__name__ = "TruthValue"
_TIPv6FilterParamsRdirAllwRadOvrd_Object = MibTableColumn
tIPv6FilterParamsRdirAllwRadOvrd = _TIPv6FilterParamsRdirAllwRadOvrd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 52),
    _TIPv6FilterParamsRdirAllwRadOvrd_Type()
)
tIPv6FilterParamsRdirAllwRadOvrd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsRdirAllwRadOvrd.setStatus("obsolete")


class _TIPv6FilterParamsFwdRtrId_Type(TmnxVRtrIDOrZero):
    """Custom type tIPv6FilterParamsFwdRtrId based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TIPv6FilterParamsFwdRtrId_Type.__name__ = "TmnxVRtrIDOrZero"
_TIPv6FilterParamsFwdRtrId_Object = MibTableColumn
tIPv6FilterParamsFwdRtrId = _TIPv6FilterParamsFwdRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 53),
    _TIPv6FilterParamsFwdRtrId_Type()
)
tIPv6FilterParamsFwdRtrId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsFwdRtrId.setStatus("obsolete")


class _TIPv6FilterParamsSrcIpFullMask_Type(InetAddressIPv6):
    """Custom type tIPv6FilterParamsSrcIpFullMask based on InetAddressIPv6"""
    defaultHexValue = "00000000000000000000000000000000"


_TIPv6FilterParamsSrcIpFullMask_Type.__name__ = "InetAddressIPv6"
_TIPv6FilterParamsSrcIpFullMask_Object = MibTableColumn
tIPv6FilterParamsSrcIpFullMask = _TIPv6FilterParamsSrcIpFullMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 54),
    _TIPv6FilterParamsSrcIpFullMask_Type()
)
tIPv6FilterParamsSrcIpFullMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsSrcIpFullMask.setStatus("current")


class _TIPv6FilterParamsDstIpFullMask_Type(InetAddressIPv6):
    """Custom type tIPv6FilterParamsDstIpFullMask based on InetAddressIPv6"""
    defaultHexValue = "00000000000000000000000000000000"


_TIPv6FilterParamsDstIpFullMask_Type.__name__ = "InetAddressIPv6"
_TIPv6FilterParamsDstIpFullMask_Object = MibTableColumn
tIPv6FilterParamsDstIpFullMask = _TIPv6FilterParamsDstIpFullMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 55),
    _TIPv6FilterParamsDstIpFullMask_Type()
)
tIPv6FilterParamsDstIpFullMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsDstIpFullMask.setStatus("current")


class _TIPv6FilterParamsNatPolicyName_Type(TNamedItemOrEmpty):
    """Custom type tIPv6FilterParamsNatPolicyName based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TIPv6FilterParamsNatPolicyName_Type.__name__ = "TNamedItemOrEmpty"
_TIPv6FilterParamsNatPolicyName_Object = MibTableColumn
tIPv6FilterParamsNatPolicyName = _TIPv6FilterParamsNatPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 56),
    _TIPv6FilterParamsNatPolicyName_Type()
)
tIPv6FilterParamsNatPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsNatPolicyName.setStatus("obsolete")


class _TIPv6FilterParamsFlowLabel_Type(IPv6FlowLabel):
    """Custom type tIPv6FilterParamsFlowLabel based on IPv6FlowLabel"""
    defaultValue = -1


_TIPv6FilterParamsFlowLabel_Type.__name__ = "IPv6FlowLabel"
_TIPv6FilterParamsFlowLabel_Object = MibTableColumn
tIPv6FilterParamsFlowLabel = _TIPv6FilterParamsFlowLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 57),
    _TIPv6FilterParamsFlowLabel_Type()
)
tIPv6FilterParamsFlowLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsFlowLabel.setStatus("current")


class _TIPv6FilterParamsFlowLabelMask_Type(IPv6FlowLabelMask):
    """Custom type tIPv6FilterParamsFlowLabelMask based on IPv6FlowLabelMask"""
    defaultValue = 1048575


_TIPv6FilterParamsFlowLabelMask_Type.__name__ = "IPv6FlowLabelMask"
_TIPv6FilterParamsFlowLabelMask_Object = MibTableColumn
tIPv6FilterParamsFlowLabelMask = _TIPv6FilterParamsFlowLabelMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 58),
    _TIPv6FilterParamsFlowLabelMask_Type()
)
tIPv6FilterParamsFlowLabelMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsFlowLabelMask.setStatus("current")


class _TIPv6FilterParamsFwdLsp_Type(TmnxVRtrMplsLspID):
    """Custom type tIPv6FilterParamsFwdLsp based on TmnxVRtrMplsLspID"""
    defaultValue = 0


_TIPv6FilterParamsFwdLsp_Type.__name__ = "TmnxVRtrMplsLspID"
_TIPv6FilterParamsFwdLsp_Object = MibTableColumn
tIPv6FilterParamsFwdLsp = _TIPv6FilterParamsFwdLsp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 59),
    _TIPv6FilterParamsFwdLsp_Type()
)
tIPv6FilterParamsFwdLsp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsFwdLsp.setStatus("obsolete")


class _TIPv6FilterParamsFwdLspRtrId_Type(TmnxVRtrIDOrZero):
    """Custom type tIPv6FilterParamsFwdLspRtrId based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TIPv6FilterParamsFwdLspRtrId_Type.__name__ = "TmnxVRtrIDOrZero"
_TIPv6FilterParamsFwdLspRtrId_Object = MibTableColumn
tIPv6FilterParamsFwdLspRtrId = _TIPv6FilterParamsFwdLspRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 60),
    _TIPv6FilterParamsFwdLspRtrId_Type()
)
tIPv6FilterParamsFwdLspRtrId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsFwdLspRtrId.setStatus("obsolete")


class _TIPv6FilterParamsIpSelector_Type(TFltrMatchIpSelector):
    """Custom type tIPv6FilterParamsIpSelector based on TFltrMatchIpSelector"""
    defaultValue = 0


_TIPv6FilterParamsIpSelector_Type.__name__ = "TFltrMatchIpSelector"
_TIPv6FilterParamsIpSelector_Object = MibTableColumn
tIPv6FilterParamsIpSelector = _TIPv6FilterParamsIpSelector_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 19, 1, 61),
    _TIPv6FilterParamsIpSelector_Type()
)
tIPv6FilterParamsIpSelector.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsIpSelector.setStatus("current")
_TFilterGroupInsertedEntries_ObjectIdentity = ObjectIdentity
tFilterGroupInsertedEntries = _TFilterGroupInsertedEntries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 20)
)


class _TFltrGrpInsrtdEntriesFilterType_Type(TFilterType):
    """Custom type tFltrGrpInsrtdEntriesFilterType based on TFilterType"""
    defaultValue = 0


_TFltrGrpInsrtdEntriesFilterType_Type.__name__ = "TFilterType"
_TFltrGrpInsrtdEntriesFilterType_Object = MibScalar
tFltrGrpInsrtdEntriesFilterType = _TFltrGrpInsrtdEntriesFilterType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 20, 1),
    _TFltrGrpInsrtdEntriesFilterType_Type()
)
tFltrGrpInsrtdEntriesFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tFltrGrpInsrtdEntriesFilterType.setStatus("current")


class _TFltrGrpInsrtdEntriesFilterId_Type(TFilterID):
    """Custom type tFltrGrpInsrtdEntriesFilterId based on TFilterID"""
    defaultValue = 0


_TFltrGrpInsrtdEntriesFilterId_Type.__name__ = "TFilterID"
_TFltrGrpInsrtdEntriesFilterId_Object = MibScalar
tFltrGrpInsrtdEntriesFilterId = _TFltrGrpInsrtdEntriesFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 20, 2),
    _TFltrGrpInsrtdEntriesFilterId_Type()
)
tFltrGrpInsrtdEntriesFilterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tFltrGrpInsrtdEntriesFilterId.setStatus("current")


class _TFltrGrpInsrtdEntriesApplication_Type(TFltrGrpInsrtdEntriesApplication):
    """Custom type tFltrGrpInsrtdEntriesApplication based on TFltrGrpInsrtdEntriesApplication"""
    defaultValue = 0


_TFltrGrpInsrtdEntriesApplication_Type.__name__ = "TFltrGrpInsrtdEntriesApplication"
_TFltrGrpInsrtdEntriesApplication_Object = MibScalar
tFltrGrpInsrtdEntriesApplication = _TFltrGrpInsrtdEntriesApplication_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 20, 3),
    _TFltrGrpInsrtdEntriesApplication_Type()
)
tFltrGrpInsrtdEntriesApplication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tFltrGrpInsrtdEntriesApplication.setStatus("current")


class _TFltrGrpInsrtdEntriesLocation_Type(Integer32):
    """Custom type tFltrGrpInsrtdEntriesLocation based on Integer32"""
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
          ("top", 1),
          ("bottom", 2))
    )


_TFltrGrpInsrtdEntriesLocation_Type.__name__ = "Integer32"
_TFltrGrpInsrtdEntriesLocation_Object = MibScalar
tFltrGrpInsrtdEntriesLocation = _TFltrGrpInsrtdEntriesLocation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 20, 4),
    _TFltrGrpInsrtdEntriesLocation_Type()
)
tFltrGrpInsrtdEntriesLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tFltrGrpInsrtdEntriesLocation.setStatus("current")


class _TFltrGrpInsrtdEntriesResult_Type(Integer32):
    """Custom type tFltrGrpInsrtdEntriesResult based on Integer32"""
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
          ("success", 1),
          ("failure", 2))
    )


_TFltrGrpInsrtdEntriesResult_Type.__name__ = "Integer32"
_TFltrGrpInsrtdEntriesResult_Object = MibScalar
tFltrGrpInsrtdEntriesResult = _TFltrGrpInsrtdEntriesResult_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 20, 5),
    _TFltrGrpInsrtdEntriesResult_Type()
)
tFltrGrpInsrtdEntriesResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrGrpInsrtdEntriesResult.setStatus("current")


class _TFltrGrpInsrtdEntriesFeedback_Type(DisplayString):
    """Custom type tFltrGrpInsrtdEntriesFeedback based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_TFltrGrpInsrtdEntriesFeedback_Type.__name__ = "DisplayString"
_TFltrGrpInsrtdEntriesFeedback_Object = MibScalar
tFltrGrpInsrtdEntriesFeedback = _TFltrGrpInsrtdEntriesFeedback_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 20, 6),
    _TFltrGrpInsrtdEntriesFeedback_Type()
)
tFltrGrpInsrtdEntriesFeedback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrGrpInsrtdEntriesFeedback.setStatus("current")


class _TFltrGrpInsrtdEntriesExecute_Type(TruthValue):
    """Custom type tFltrGrpInsrtdEntriesExecute based on TruthValue"""
    defaultValue = 2


_TFltrGrpInsrtdEntriesExecute_Type.__name__ = "TruthValue"
_TFltrGrpInsrtdEntriesExecute_Object = MibScalar
tFltrGrpInsrtdEntriesExecute = _TFltrGrpInsrtdEntriesExecute_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 20, 7),
    _TFltrGrpInsrtdEntriesExecute_Type()
)
tFltrGrpInsrtdEntriesExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tFltrGrpInsrtdEntriesExecute.setStatus("current")
_TDhcpFilterTableLastChanged_Type = TimeStamp
_TDhcpFilterTableLastChanged_Object = MibScalar
tDhcpFilterTableLastChanged = _TDhcpFilterTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 21),
    _TDhcpFilterTableLastChanged_Type()
)
tDhcpFilterTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tDhcpFilterTableLastChanged.setStatus("current")
_TDhcpFilterTable_Object = MibTable
tDhcpFilterTable = _TDhcpFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 22)
)
if mibBuilder.loadTexts:
    tDhcpFilterTable.setStatus("current")
_TDhcpFilterEntry_Object = MibTableRow
tDhcpFilterEntry = _TDhcpFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 22, 1)
)
tDhcpFilterEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tDhcpFilterId"),
)
if mibBuilder.loadTexts:
    tDhcpFilterEntry.setStatus("current")


class _TDhcpFilterId_Type(TDHCPFilterID):
    """Custom type tDhcpFilterId based on TDHCPFilterID"""
    subtypeSpec = TDHCPFilterID.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TDhcpFilterId_Type.__name__ = "TDHCPFilterID"
_TDhcpFilterId_Object = MibTableColumn
tDhcpFilterId = _TDhcpFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 22, 1, 1),
    _TDhcpFilterId_Type()
)
tDhcpFilterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tDhcpFilterId.setStatus("current")
_TDhcpFilterRowStatus_Type = RowStatus
_TDhcpFilterRowStatus_Object = MibTableColumn
tDhcpFilterRowStatus = _TDhcpFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 22, 1, 2),
    _TDhcpFilterRowStatus_Type()
)
tDhcpFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tDhcpFilterRowStatus.setStatus("current")
_TDhcpFilterLastChanged_Type = TimeStamp
_TDhcpFilterLastChanged_Object = MibTableColumn
tDhcpFilterLastChanged = _TDhcpFilterLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 22, 1, 3),
    _TDhcpFilterLastChanged_Type()
)
tDhcpFilterLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tDhcpFilterLastChanged.setStatus("current")


class _TDhcpFilterDescription_Type(TItemDescription):
    """Custom type tDhcpFilterDescription based on TItemDescription"""
    defaultHexValue = ""


_TDhcpFilterDescription_Type.__name__ = "TItemDescription"
_TDhcpFilterDescription_Object = MibTableColumn
tDhcpFilterDescription = _TDhcpFilterDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 22, 1, 4),
    _TDhcpFilterDescription_Type()
)
tDhcpFilterDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tDhcpFilterDescription.setStatus("current")


class _TDhcpFilterDefAction_Type(TDhcpFilterAction):
    """Custom type tDhcpFilterDefAction based on TDhcpFilterAction"""
    defaultValue = 1


_TDhcpFilterDefAction_Type.__name__ = "TDhcpFilterAction"
_TDhcpFilterDefAction_Object = MibTableColumn
tDhcpFilterDefAction = _TDhcpFilterDefAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 22, 1, 5),
    _TDhcpFilterDefAction_Type()
)
tDhcpFilterDefAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tDhcpFilterDefAction.setStatus("current")
_TDhcpFilterParamsTblLastChanged_Type = TimeStamp
_TDhcpFilterParamsTblLastChanged_Object = MibScalar
tDhcpFilterParamsTblLastChanged = _TDhcpFilterParamsTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 23),
    _TDhcpFilterParamsTblLastChanged_Type()
)
tDhcpFilterParamsTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tDhcpFilterParamsTblLastChanged.setStatus("current")
_TDhcpFilterParamsTable_Object = MibTable
tDhcpFilterParamsTable = _TDhcpFilterParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 24)
)
if mibBuilder.loadTexts:
    tDhcpFilterParamsTable.setStatus("current")
_TDhcpFilterParamsEntry_Object = MibTableRow
tDhcpFilterParamsEntry = _TDhcpFilterParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 24, 1)
)
tDhcpFilterParamsEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tDhcpFilterId"),
    (0, "TIMETRA-FILTER-MIB", "tDhcpFilterParamsId"),
)
if mibBuilder.loadTexts:
    tDhcpFilterParamsEntry.setStatus("current")
_TDhcpFilterParamsId_Type = TDhcpEntryId
_TDhcpFilterParamsId_Object = MibTableColumn
tDhcpFilterParamsId = _TDhcpFilterParamsId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 24, 1, 1),
    _TDhcpFilterParamsId_Type()
)
tDhcpFilterParamsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tDhcpFilterParamsId.setStatus("current")
_TDhcpFilterParamsRowStatus_Type = RowStatus
_TDhcpFilterParamsRowStatus_Object = MibTableColumn
tDhcpFilterParamsRowStatus = _TDhcpFilterParamsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 24, 1, 2),
    _TDhcpFilterParamsRowStatus_Type()
)
tDhcpFilterParamsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tDhcpFilterParamsRowStatus.setStatus("current")
_TDhcpFilterParamsLastChanged_Type = TimeStamp
_TDhcpFilterParamsLastChanged_Object = MibTableColumn
tDhcpFilterParamsLastChanged = _TDhcpFilterParamsLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 24, 1, 3),
    _TDhcpFilterParamsLastChanged_Type()
)
tDhcpFilterParamsLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tDhcpFilterParamsLastChanged.setStatus("current")


class _TDhcpFilterParamsOptionNumber_Type(Integer32):
    """Custom type tDhcpFilterParamsOptionNumber based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_TDhcpFilterParamsOptionNumber_Type.__name__ = "Integer32"
_TDhcpFilterParamsOptionNumber_Object = MibTableColumn
tDhcpFilterParamsOptionNumber = _TDhcpFilterParamsOptionNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 24, 1, 4),
    _TDhcpFilterParamsOptionNumber_Type()
)
tDhcpFilterParamsOptionNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tDhcpFilterParamsOptionNumber.setStatus("current")


class _TDhcpFilterParamsOptionMatch_Type(TDhcpFilterMatch):
    """Custom type tDhcpFilterParamsOptionMatch based on TDhcpFilterMatch"""
    defaultValue = 1


_TDhcpFilterParamsOptionMatch_Type.__name__ = "TDhcpFilterMatch"
_TDhcpFilterParamsOptionMatch_Object = MibTableColumn
tDhcpFilterParamsOptionMatch = _TDhcpFilterParamsOptionMatch_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 24, 1, 5),
    _TDhcpFilterParamsOptionMatch_Type()
)
tDhcpFilterParamsOptionMatch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tDhcpFilterParamsOptionMatch.setStatus("current")


class _TDhcpFilterParamsAction_Type(TDhcpFilterAction):
    """Custom type tDhcpFilterParamsAction based on TDhcpFilterAction"""
    defaultValue = 1


_TDhcpFilterParamsAction_Type.__name__ = "TDhcpFilterAction"
_TDhcpFilterParamsAction_Object = MibTableColumn
tDhcpFilterParamsAction = _TDhcpFilterParamsAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 24, 1, 6),
    _TDhcpFilterParamsAction_Type()
)
tDhcpFilterParamsAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tDhcpFilterParamsAction.setStatus("current")


class _TDhcpFilterParamsOptionValue_Type(OctetString):
    """Custom type tDhcpFilterParamsOptionValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_TDhcpFilterParamsOptionValue_Type.__name__ = "OctetString"
_TDhcpFilterParamsOptionValue_Object = MibTableColumn
tDhcpFilterParamsOptionValue = _TDhcpFilterParamsOptionValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 24, 1, 7),
    _TDhcpFilterParamsOptionValue_Type()
)
tDhcpFilterParamsOptionValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tDhcpFilterParamsOptionValue.setStatus("current")
_TMacFilterNameTableLastChgd_Type = TimeStamp
_TMacFilterNameTableLastChgd_Object = MibScalar
tMacFilterNameTableLastChgd = _TMacFilterNameTableLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 25),
    _TMacFilterNameTableLastChgd_Type()
)
tMacFilterNameTableLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMacFilterNameTableLastChgd.setStatus("current")
_TMacFilterNameTable_Object = MibTable
tMacFilterNameTable = _TMacFilterNameTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 26)
)
if mibBuilder.loadTexts:
    tMacFilterNameTable.setStatus("current")
_TMacFilterNameEntry_Object = MibTableRow
tMacFilterNameEntry = _TMacFilterNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 26, 1)
)
tMacFilterNameEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tMacFilterName"),
)
if mibBuilder.loadTexts:
    tMacFilterNameEntry.setStatus("current")
_TMacFilterNameId_Type = TAnyFilterID
_TMacFilterNameId_Object = MibTableColumn
tMacFilterNameId = _TMacFilterNameId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 26, 1, 1),
    _TMacFilterNameId_Type()
)
tMacFilterNameId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMacFilterNameId.setStatus("current")
_TMacFilterNameRowStatus_Type = RowStatus
_TMacFilterNameRowStatus_Object = MibTableColumn
tMacFilterNameRowStatus = _TMacFilterNameRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 26, 1, 2),
    _TMacFilterNameRowStatus_Type()
)
tMacFilterNameRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMacFilterNameRowStatus.setStatus("current")
_TMacFilterNameLastChanged_Type = TimeStamp
_TMacFilterNameLastChanged_Object = MibTableColumn
tMacFilterNameLastChanged = _TMacFilterNameLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 26, 1, 3),
    _TMacFilterNameLastChanged_Type()
)
tMacFilterNameLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMacFilterNameLastChanged.setStatus("current")
_TIpFilterNameTableLastChgd_Type = TimeStamp
_TIpFilterNameTableLastChgd_Object = MibScalar
tIpFilterNameTableLastChgd = _TIpFilterNameTableLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 27),
    _TIpFilterNameTableLastChgd_Type()
)
tIpFilterNameTableLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIpFilterNameTableLastChgd.setStatus("current")
_TIpFilterNameTable_Object = MibTable
tIpFilterNameTable = _TIpFilterNameTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 28)
)
if mibBuilder.loadTexts:
    tIpFilterNameTable.setStatus("current")
_TIpFilterNameEntry_Object = MibTableRow
tIpFilterNameEntry = _TIpFilterNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 28, 1)
)
tIpFilterNameEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tIpFilterName"),
)
if mibBuilder.loadTexts:
    tIpFilterNameEntry.setStatus("current")
_TIpFilterNameId_Type = TAnyFilterID
_TIpFilterNameId_Object = MibTableColumn
tIpFilterNameId = _TIpFilterNameId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 28, 1, 1),
    _TIpFilterNameId_Type()
)
tIpFilterNameId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIpFilterNameId.setStatus("current")
_TIpFilterNameRowStatus_Type = RowStatus
_TIpFilterNameRowStatus_Object = MibTableColumn
tIpFilterNameRowStatus = _TIpFilterNameRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 28, 1, 2),
    _TIpFilterNameRowStatus_Type()
)
tIpFilterNameRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIpFilterNameRowStatus.setStatus("current")
_TIpFilterNameLastChanged_Type = TimeStamp
_TIpFilterNameLastChanged_Object = MibTableColumn
tIpFilterNameLastChanged = _TIpFilterNameLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 28, 1, 3),
    _TIpFilterNameLastChanged_Type()
)
tIpFilterNameLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIpFilterNameLastChanged.setStatus("current")
_TIpv6FilterNameTableLastChgd_Type = TimeStamp
_TIpv6FilterNameTableLastChgd_Object = MibScalar
tIpv6FilterNameTableLastChgd = _TIpv6FilterNameTableLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 29),
    _TIpv6FilterNameTableLastChgd_Type()
)
tIpv6FilterNameTableLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIpv6FilterNameTableLastChgd.setStatus("current")
_TIpv6FilterNameTable_Object = MibTable
tIpv6FilterNameTable = _TIpv6FilterNameTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 30)
)
if mibBuilder.loadTexts:
    tIpv6FilterNameTable.setStatus("current")
_TIpv6FilterNameEntry_Object = MibTableRow
tIpv6FilterNameEntry = _TIpv6FilterNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 30, 1)
)
tIpv6FilterNameEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tIpv6FilterName"),
)
if mibBuilder.loadTexts:
    tIpv6FilterNameEntry.setStatus("current")
_TIpv6FilterNameId_Type = TAnyFilterID
_TIpv6FilterNameId_Object = MibTableColumn
tIpv6FilterNameId = _TIpv6FilterNameId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 30, 1, 1),
    _TIpv6FilterNameId_Type()
)
tIpv6FilterNameId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIpv6FilterNameId.setStatus("current")
_TIpv6FilterNameRowStatus_Type = RowStatus
_TIpv6FilterNameRowStatus_Object = MibTableColumn
tIpv6FilterNameRowStatus = _TIpv6FilterNameRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 30, 1, 2),
    _TIpv6FilterNameRowStatus_Type()
)
tIpv6FilterNameRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIpv6FilterNameRowStatus.setStatus("current")
_TIpv6FilterNameLastChanged_Type = TimeStamp
_TIpv6FilterNameLastChanged_Object = MibTableColumn
tIpv6FilterNameLastChanged = _TIpv6FilterNameLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 30, 1, 3),
    _TIpv6FilterNameLastChanged_Type()
)
tIpv6FilterNameLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIpv6FilterNameLastChanged.setStatus("current")
_TFilterLiObjects_ObjectIdentity = ObjectIdentity
tFilterLiObjects = _TFilterLiObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31)
)
_TLiReservedBlockTableLastChanged_Type = TimeStamp
_TLiReservedBlockTableLastChanged_Object = MibScalar
tLiReservedBlockTableLastChanged = _TLiReservedBlockTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 1),
    _TLiReservedBlockTableLastChanged_Type()
)
tLiReservedBlockTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLiReservedBlockTableLastChanged.setStatus("current")
_TLiReservedBlockTable_Object = MibTable
tLiReservedBlockTable = _TLiReservedBlockTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 2)
)
if mibBuilder.loadTexts:
    tLiReservedBlockTable.setStatus("current")
_TLiReservedBlockEntry_Object = MibTableRow
tLiReservedBlockEntry = _TLiReservedBlockEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 2, 1)
)
tLiReservedBlockEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tLiReservedBlockName"),
)
if mibBuilder.loadTexts:
    tLiReservedBlockEntry.setStatus("current")
_TLiReservedBlockName_Type = TNamedItem
_TLiReservedBlockName_Object = MibTableColumn
tLiReservedBlockName = _TLiReservedBlockName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 2, 1, 1),
    _TLiReservedBlockName_Type()
)
tLiReservedBlockName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tLiReservedBlockName.setStatus("current")
_TLiReservedBlockRowStatus_Type = RowStatus
_TLiReservedBlockRowStatus_Object = MibTableColumn
tLiReservedBlockRowStatus = _TLiReservedBlockRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 2, 1, 2),
    _TLiReservedBlockRowStatus_Type()
)
tLiReservedBlockRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiReservedBlockRowStatus.setStatus("current")
_TLiReservedBlockLastChanged_Type = TimeStamp
_TLiReservedBlockLastChanged_Object = MibTableColumn
tLiReservedBlockLastChanged = _TLiReservedBlockLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 2, 1, 3),
    _TLiReservedBlockLastChanged_Type()
)
tLiReservedBlockLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLiReservedBlockLastChanged.setStatus("current")


class _TLiReservedBlockDescription_Type(TItemDescription):
    """Custom type tLiReservedBlockDescription based on TItemDescription"""
    defaultHexValue = ""


_TLiReservedBlockDescription_Type.__name__ = "TItemDescription"
_TLiReservedBlockDescription_Object = MibTableColumn
tLiReservedBlockDescription = _TLiReservedBlockDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 2, 1, 4),
    _TLiReservedBlockDescription_Type()
)
tLiReservedBlockDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiReservedBlockDescription.setStatus("current")


class _TLiReservedBlockStart_Type(TEntryIdOrZero):
    """Custom type tLiReservedBlockStart based on TEntryIdOrZero"""
    defaultValue = 0


_TLiReservedBlockStart_Type.__name__ = "TEntryIdOrZero"
_TLiReservedBlockStart_Object = MibTableColumn
tLiReservedBlockStart = _TLiReservedBlockStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 2, 1, 5),
    _TLiReservedBlockStart_Type()
)
tLiReservedBlockStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiReservedBlockStart.setStatus("current")


class _TLiReservedBlockSize_Type(TEntryBlockSize):
    """Custom type tLiReservedBlockSize based on TEntryBlockSize"""
    defaultValue = 0


_TLiReservedBlockSize_Type.__name__ = "TEntryBlockSize"
_TLiReservedBlockSize_Object = MibTableColumn
tLiReservedBlockSize = _TLiReservedBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 2, 1, 6),
    _TLiReservedBlockSize_Type()
)
tLiReservedBlockSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiReservedBlockSize.setStatus("current")
_TLiReservedBlockFltrTableLastChg_Type = TimeStamp
_TLiReservedBlockFltrTableLastChg_Object = MibScalar
tLiReservedBlockFltrTableLastChg = _TLiReservedBlockFltrTableLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 3),
    _TLiReservedBlockFltrTableLastChg_Type()
)
tLiReservedBlockFltrTableLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLiReservedBlockFltrTableLastChg.setStatus("current")
_TLiReservedBlockFltrTable_Object = MibTable
tLiReservedBlockFltrTable = _TLiReservedBlockFltrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 4)
)
if mibBuilder.loadTexts:
    tLiReservedBlockFltrTable.setStatus("current")
_TLiReservedBlockFltrEntry_Object = MibTableRow
tLiReservedBlockFltrEntry = _TLiReservedBlockFltrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 4, 1)
)
tLiReservedBlockFltrEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tLiReservedBlockName"),
    (0, "TIMETRA-FILTER-MIB", "tLiReservedBlockFltrType"),
    (0, "TIMETRA-FILTER-MIB", "tLiReservedBlockFltrIdStart"),
    (0, "TIMETRA-FILTER-MIB", "tLiReservedBlockFltrIdEnd"),
)
if mibBuilder.loadTexts:
    tLiReservedBlockFltrEntry.setStatus("current")
_TLiReservedBlockFltrType_Type = TFilterType
_TLiReservedBlockFltrType_Object = MibTableColumn
tLiReservedBlockFltrType = _TLiReservedBlockFltrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 4, 1, 1),
    _TLiReservedBlockFltrType_Type()
)
tLiReservedBlockFltrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tLiReservedBlockFltrType.setStatus("current")
_TLiReservedBlockFltrIdStart_Type = TFilterID
_TLiReservedBlockFltrIdStart_Object = MibTableColumn
tLiReservedBlockFltrIdStart = _TLiReservedBlockFltrIdStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 4, 1, 2),
    _TLiReservedBlockFltrIdStart_Type()
)
tLiReservedBlockFltrIdStart.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tLiReservedBlockFltrIdStart.setStatus("current")
_TLiReservedBlockFltrIdEnd_Type = TFilterID
_TLiReservedBlockFltrIdEnd_Object = MibTableColumn
tLiReservedBlockFltrIdEnd = _TLiReservedBlockFltrIdEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 4, 1, 3),
    _TLiReservedBlockFltrIdEnd_Type()
)
tLiReservedBlockFltrIdEnd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tLiReservedBlockFltrIdEnd.setStatus("current")
_TLiReservedBlockFltrRowStatus_Type = RowStatus
_TLiReservedBlockFltrRowStatus_Object = MibTableColumn
tLiReservedBlockFltrRowStatus = _TLiReservedBlockFltrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 4, 1, 4),
    _TLiReservedBlockFltrRowStatus_Type()
)
tLiReservedBlockFltrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiReservedBlockFltrRowStatus.setStatus("current")
_TLiReservedBlockFltrLastChanged_Type = TimeStamp
_TLiReservedBlockFltrLastChanged_Object = MibTableColumn
tLiReservedBlockFltrLastChanged = _TLiReservedBlockFltrLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 4, 1, 5),
    _TLiReservedBlockFltrLastChanged_Type()
)
tLiReservedBlockFltrLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLiReservedBlockFltrLastChanged.setStatus("current")
_TLiFilterTableLastChanged_Type = TimeStamp
_TLiFilterTableLastChanged_Object = MibScalar
tLiFilterTableLastChanged = _TLiFilterTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 5),
    _TLiFilterTableLastChanged_Type()
)
tLiFilterTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLiFilterTableLastChanged.setStatus("current")
_TLiFilterTable_Object = MibTable
tLiFilterTable = _TLiFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 6)
)
if mibBuilder.loadTexts:
    tLiFilterTable.setStatus("current")
_TLiFilterEntry_Object = MibTableRow
tLiFilterEntry = _TLiFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 6, 1)
)
tLiFilterEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tLiFilterType"),
    (0, "TIMETRA-FILTER-MIB", "tLiFilterName"),
)
if mibBuilder.loadTexts:
    tLiFilterEntry.setStatus("current")
_TLiFilterType_Type = TFilterType
_TLiFilterType_Object = MibTableColumn
tLiFilterType = _TLiFilterType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 6, 1, 1),
    _TLiFilterType_Type()
)
tLiFilterType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tLiFilterType.setStatus("current")
_TLiFilterName_Type = TNamedItem
_TLiFilterName_Object = MibTableColumn
tLiFilterName = _TLiFilterName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 6, 1, 2),
    _TLiFilterName_Type()
)
tLiFilterName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tLiFilterName.setStatus("current")
_TLiFilterRowStatus_Type = RowStatus
_TLiFilterRowStatus_Object = MibTableColumn
tLiFilterRowStatus = _TLiFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 6, 1, 3),
    _TLiFilterRowStatus_Type()
)
tLiFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiFilterRowStatus.setStatus("current")
_TLiFilterLastChanged_Type = TimeStamp
_TLiFilterLastChanged_Object = MibTableColumn
tLiFilterLastChanged = _TLiFilterLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 6, 1, 4),
    _TLiFilterLastChanged_Type()
)
tLiFilterLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLiFilterLastChanged.setStatus("current")


class _TLiFilterDescription_Type(TItemDescription):
    """Custom type tLiFilterDescription based on TItemDescription"""
    defaultHexValue = ""


_TLiFilterDescription_Type.__name__ = "TItemDescription"
_TLiFilterDescription_Object = MibTableColumn
tLiFilterDescription = _TLiFilterDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 6, 1, 5),
    _TLiFilterDescription_Type()
)
tLiFilterDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiFilterDescription.setStatus("current")
_TLiFilterAssociationTableLastChg_Type = TimeStamp
_TLiFilterAssociationTableLastChg_Object = MibScalar
tLiFilterAssociationTableLastChg = _TLiFilterAssociationTableLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 7),
    _TLiFilterAssociationTableLastChg_Type()
)
tLiFilterAssociationTableLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLiFilterAssociationTableLastChg.setStatus("current")
_TLiFilterAssociationTable_Object = MibTable
tLiFilterAssociationTable = _TLiFilterAssociationTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 8)
)
if mibBuilder.loadTexts:
    tLiFilterAssociationTable.setStatus("current")
_TLiFilterAssociationEntry_Object = MibTableRow
tLiFilterAssociationEntry = _TLiFilterAssociationEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 8, 1)
)
tLiFilterAssociationEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tLiFilterType"),
    (0, "TIMETRA-FILTER-MIB", "tLiFilterName"),
    (0, "TIMETRA-FILTER-MIB", "tLiFilterAssociationFltrId"),
)
if mibBuilder.loadTexts:
    tLiFilterAssociationEntry.setStatus("current")
_TLiFilterAssociationFltrId_Type = TFilterID
_TLiFilterAssociationFltrId_Object = MibTableColumn
tLiFilterAssociationFltrId = _TLiFilterAssociationFltrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 8, 1, 1),
    _TLiFilterAssociationFltrId_Type()
)
tLiFilterAssociationFltrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tLiFilterAssociationFltrId.setStatus("current")
_TLiFilterAssociationRowStatus_Type = RowStatus
_TLiFilterAssociationRowStatus_Object = MibTableColumn
tLiFilterAssociationRowStatus = _TLiFilterAssociationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 8, 1, 2),
    _TLiFilterAssociationRowStatus_Type()
)
tLiFilterAssociationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiFilterAssociationRowStatus.setStatus("current")
_TLiFilterAssociationLastChg_Type = TimeStamp
_TLiFilterAssociationLastChg_Object = MibTableColumn
tLiFilterAssociationLastChg = _TLiFilterAssociationLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 8, 1, 3),
    _TLiFilterAssociationLastChg_Type()
)
tLiFilterAssociationLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLiFilterAssociationLastChg.setStatus("current")
_TLiMacFilterParamsTableLastChg_Type = TimeStamp
_TLiMacFilterParamsTableLastChg_Object = MibScalar
tLiMacFilterParamsTableLastChg = _TLiMacFilterParamsTableLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 9),
    _TLiMacFilterParamsTableLastChg_Type()
)
tLiMacFilterParamsTableLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLiMacFilterParamsTableLastChg.setStatus("current")
_TLiMacFilterParamsTable_Object = MibTable
tLiMacFilterParamsTable = _TLiMacFilterParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 10)
)
if mibBuilder.loadTexts:
    tLiMacFilterParamsTable.setStatus("current")
_TLiMacFilterParamsEntry_Object = MibTableRow
tLiMacFilterParamsEntry = _TLiMacFilterParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 10, 1)
)
tLiMacFilterParamsEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tLiFilterType"),
    (0, "TIMETRA-FILTER-MIB", "tLiFilterName"),
    (0, "TIMETRA-FILTER-MIB", "tLiMacFilterParamsId"),
)
if mibBuilder.loadTexts:
    tLiMacFilterParamsEntry.setStatus("current")
_TLiMacFilterParamsId_Type = TLimitedEntryId
_TLiMacFilterParamsId_Object = MibTableColumn
tLiMacFilterParamsId = _TLiMacFilterParamsId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 10, 1, 1),
    _TLiMacFilterParamsId_Type()
)
tLiMacFilterParamsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tLiMacFilterParamsId.setStatus("current")
_TLiMacFilterParamsRowStatus_Type = RowStatus
_TLiMacFilterParamsRowStatus_Object = MibTableColumn
tLiMacFilterParamsRowStatus = _TLiMacFilterParamsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 10, 1, 2),
    _TLiMacFilterParamsRowStatus_Type()
)
tLiMacFilterParamsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiMacFilterParamsRowStatus.setStatus("current")
_TLiMacFilterParamsLastChanged_Type = TimeStamp
_TLiMacFilterParamsLastChanged_Object = MibTableColumn
tLiMacFilterParamsLastChanged = _TLiMacFilterParamsLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 10, 1, 3),
    _TLiMacFilterParamsLastChanged_Type()
)
tLiMacFilterParamsLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLiMacFilterParamsLastChanged.setStatus("current")


class _TLiMacFilterParamsDescription_Type(TItemDescription):
    """Custom type tLiMacFilterParamsDescription based on TItemDescription"""
    defaultHexValue = ""


_TLiMacFilterParamsDescription_Type.__name__ = "TItemDescription"
_TLiMacFilterParamsDescription_Object = MibTableColumn
tLiMacFilterParamsDescription = _TLiMacFilterParamsDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 10, 1, 4),
    _TLiMacFilterParamsDescription_Type()
)
tLiMacFilterParamsDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiMacFilterParamsDescription.setStatus("current")


class _TLiMacFilterParamsFrameType_Type(TFrameType):
    """Custom type tLiMacFilterParamsFrameType based on TFrameType"""
    defaultValue = 0


_TLiMacFilterParamsFrameType_Type.__name__ = "TFrameType"
_TLiMacFilterParamsFrameType_Object = MibTableColumn
tLiMacFilterParamsFrameType = _TLiMacFilterParamsFrameType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 10, 1, 5),
    _TLiMacFilterParamsFrameType_Type()
)
tLiMacFilterParamsFrameType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiMacFilterParamsFrameType.setStatus("current")


class _TLiMacFilterParamsSrcMAC_Type(MacAddress):
    """Custom type tLiMacFilterParamsSrcMAC based on MacAddress"""
    defaultHexValue = "000000000000"


_TLiMacFilterParamsSrcMAC_Type.__name__ = "MacAddress"
_TLiMacFilterParamsSrcMAC_Object = MibTableColumn
tLiMacFilterParamsSrcMAC = _TLiMacFilterParamsSrcMAC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 10, 1, 6),
    _TLiMacFilterParamsSrcMAC_Type()
)
tLiMacFilterParamsSrcMAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiMacFilterParamsSrcMAC.setStatus("current")


class _TLiMacFilterParamsSrcMACMask_Type(MacAddress):
    """Custom type tLiMacFilterParamsSrcMACMask based on MacAddress"""
    defaultHexValue = "000000000000"


_TLiMacFilterParamsSrcMACMask_Type.__name__ = "MacAddress"
_TLiMacFilterParamsSrcMACMask_Object = MibTableColumn
tLiMacFilterParamsSrcMACMask = _TLiMacFilterParamsSrcMACMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 10, 1, 7),
    _TLiMacFilterParamsSrcMACMask_Type()
)
tLiMacFilterParamsSrcMACMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiMacFilterParamsSrcMACMask.setStatus("current")


class _TLiMacFilterParamsDstMAC_Type(MacAddress):
    """Custom type tLiMacFilterParamsDstMAC based on MacAddress"""
    defaultHexValue = "000000000000"


_TLiMacFilterParamsDstMAC_Type.__name__ = "MacAddress"
_TLiMacFilterParamsDstMAC_Object = MibTableColumn
tLiMacFilterParamsDstMAC = _TLiMacFilterParamsDstMAC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 10, 1, 8),
    _TLiMacFilterParamsDstMAC_Type()
)
tLiMacFilterParamsDstMAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiMacFilterParamsDstMAC.setStatus("current")


class _TLiMacFilterParamsDstMACMask_Type(MacAddress):
    """Custom type tLiMacFilterParamsDstMACMask based on MacAddress"""
    defaultHexValue = "000000000000"


_TLiMacFilterParamsDstMACMask_Type.__name__ = "MacAddress"
_TLiMacFilterParamsDstMACMask_Object = MibTableColumn
tLiMacFilterParamsDstMACMask = _TLiMacFilterParamsDstMACMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 10, 1, 9),
    _TLiMacFilterParamsDstMACMask_Type()
)
tLiMacFilterParamsDstMACMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiMacFilterParamsDstMACMask.setStatus("current")
_TLiMacFilterParamsIngrHitCount_Type = Counter64
_TLiMacFilterParamsIngrHitCount_Object = MibTableColumn
tLiMacFilterParamsIngrHitCount = _TLiMacFilterParamsIngrHitCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 10, 1, 10),
    _TLiMacFilterParamsIngrHitCount_Type()
)
tLiMacFilterParamsIngrHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLiMacFilterParamsIngrHitCount.setStatus("current")
_TLiMacFilterParamsEgrHitCount_Type = Counter64
_TLiMacFilterParamsEgrHitCount_Object = MibTableColumn
tLiMacFilterParamsEgrHitCount = _TLiMacFilterParamsEgrHitCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 10, 1, 11),
    _TLiMacFilterParamsEgrHitCount_Type()
)
tLiMacFilterParamsEgrHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLiMacFilterParamsEgrHitCount.setStatus("current")
_TLiMacFilterParamsIngrHitBytes_Type = Counter64
_TLiMacFilterParamsIngrHitBytes_Object = MibTableColumn
tLiMacFilterParamsIngrHitBytes = _TLiMacFilterParamsIngrHitBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 10, 1, 12),
    _TLiMacFilterParamsIngrHitBytes_Type()
)
tLiMacFilterParamsIngrHitBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLiMacFilterParamsIngrHitBytes.setStatus("current")
_TLiMacFilterParamsEgrHitBytes_Type = Counter64
_TLiMacFilterParamsEgrHitBytes_Object = MibTableColumn
tLiMacFilterParamsEgrHitBytes = _TLiMacFilterParamsEgrHitBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 10, 1, 13),
    _TLiMacFilterParamsEgrHitBytes_Type()
)
tLiMacFilterParamsEgrHitBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLiMacFilterParamsEgrHitBytes.setStatus("current")
_TLiIpFilterParamsTableLastChg_Type = TimeStamp
_TLiIpFilterParamsTableLastChg_Object = MibScalar
tLiIpFilterParamsTableLastChg = _TLiIpFilterParamsTableLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 15),
    _TLiIpFilterParamsTableLastChg_Type()
)
tLiIpFilterParamsTableLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLiIpFilterParamsTableLastChg.setStatus("current")
_TLiIpFilterParamsTable_Object = MibTable
tLiIpFilterParamsTable = _TLiIpFilterParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 16)
)
if mibBuilder.loadTexts:
    tLiIpFilterParamsTable.setStatus("current")
_TLiIpFilterParamsEntry_Object = MibTableRow
tLiIpFilterParamsEntry = _TLiIpFilterParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 16, 1)
)
tLiIpFilterParamsEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tLiFilterType"),
    (0, "TIMETRA-FILTER-MIB", "tLiFilterName"),
    (0, "TIMETRA-FILTER-MIB", "tLiIpFilterParamsId"),
)
if mibBuilder.loadTexts:
    tLiIpFilterParamsEntry.setStatus("current")
_TLiIpFilterParamsId_Type = TLimitedEntryId
_TLiIpFilterParamsId_Object = MibTableColumn
tLiIpFilterParamsId = _TLiIpFilterParamsId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 16, 1, 1),
    _TLiIpFilterParamsId_Type()
)
tLiIpFilterParamsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tLiIpFilterParamsId.setStatus("current")
_TLiIpFilterParamsLastChanged_Type = TimeStamp
_TLiIpFilterParamsLastChanged_Object = MibTableColumn
tLiIpFilterParamsLastChanged = _TLiIpFilterParamsLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 16, 1, 2),
    _TLiIpFilterParamsLastChanged_Type()
)
tLiIpFilterParamsLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLiIpFilterParamsLastChanged.setStatus("current")
_TLiIpFilterParamsRowStatus_Type = RowStatus
_TLiIpFilterParamsRowStatus_Object = MibTableColumn
tLiIpFilterParamsRowStatus = _TLiIpFilterParamsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 16, 1, 3),
    _TLiIpFilterParamsRowStatus_Type()
)
tLiIpFilterParamsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiIpFilterParamsRowStatus.setStatus("current")


class _TLiIpFilterParamsDescription_Type(TItemDescription):
    """Custom type tLiIpFilterParamsDescription based on TItemDescription"""
    defaultHexValue = ""


_TLiIpFilterParamsDescription_Type.__name__ = "TItemDescription"
_TLiIpFilterParamsDescription_Object = MibTableColumn
tLiIpFilterParamsDescription = _TLiIpFilterParamsDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 16, 1, 4),
    _TLiIpFilterParamsDescription_Type()
)
tLiIpFilterParamsDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiIpFilterParamsDescription.setStatus("current")


class _TLiIpFilterParamsSrcIpAddrType_Type(InetAddressType):
    """Custom type tLiIpFilterParamsSrcIpAddrType based on InetAddressType"""
    defaultValue = 0


_TLiIpFilterParamsSrcIpAddrType_Type.__name__ = "InetAddressType"
_TLiIpFilterParamsSrcIpAddrType_Object = MibTableColumn
tLiIpFilterParamsSrcIpAddrType = _TLiIpFilterParamsSrcIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 16, 1, 5),
    _TLiIpFilterParamsSrcIpAddrType_Type()
)
tLiIpFilterParamsSrcIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiIpFilterParamsSrcIpAddrType.setStatus("current")


class _TLiIpFilterParamsSrcIpAddr_Type(InetAddress):
    """Custom type tLiIpFilterParamsSrcIpAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TLiIpFilterParamsSrcIpAddr_Type.__name__ = "InetAddress"
_TLiIpFilterParamsSrcIpAddr_Object = MibTableColumn
tLiIpFilterParamsSrcIpAddr = _TLiIpFilterParamsSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 16, 1, 6),
    _TLiIpFilterParamsSrcIpAddr_Type()
)
tLiIpFilterParamsSrcIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiIpFilterParamsSrcIpAddr.setStatus("current")


class _TLiIpFilterParamsSrcIpFullMask_Type(InetAddress):
    """Custom type tLiIpFilterParamsSrcIpFullMask based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TLiIpFilterParamsSrcIpFullMask_Type.__name__ = "InetAddress"
_TLiIpFilterParamsSrcIpFullMask_Object = MibTableColumn
tLiIpFilterParamsSrcIpFullMask = _TLiIpFilterParamsSrcIpFullMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 16, 1, 7),
    _TLiIpFilterParamsSrcIpFullMask_Type()
)
tLiIpFilterParamsSrcIpFullMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiIpFilterParamsSrcIpFullMask.setStatus("current")


class _TLiIpFilterParamsDstIpAddrType_Type(InetAddressType):
    """Custom type tLiIpFilterParamsDstIpAddrType based on InetAddressType"""
    defaultValue = 0


_TLiIpFilterParamsDstIpAddrType_Type.__name__ = "InetAddressType"
_TLiIpFilterParamsDstIpAddrType_Object = MibTableColumn
tLiIpFilterParamsDstIpAddrType = _TLiIpFilterParamsDstIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 16, 1, 8),
    _TLiIpFilterParamsDstIpAddrType_Type()
)
tLiIpFilterParamsDstIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiIpFilterParamsDstIpAddrType.setStatus("current")


class _TLiIpFilterParamsDstIpAddr_Type(InetAddress):
    """Custom type tLiIpFilterParamsDstIpAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TLiIpFilterParamsDstIpAddr_Type.__name__ = "InetAddress"
_TLiIpFilterParamsDstIpAddr_Object = MibTableColumn
tLiIpFilterParamsDstIpAddr = _TLiIpFilterParamsDstIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 16, 1, 9),
    _TLiIpFilterParamsDstIpAddr_Type()
)
tLiIpFilterParamsDstIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiIpFilterParamsDstIpAddr.setStatus("current")


class _TLiIpFilterParamsDstIpFullMask_Type(InetAddress):
    """Custom type tLiIpFilterParamsDstIpFullMask based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TLiIpFilterParamsDstIpFullMask_Type.__name__ = "InetAddress"
_TLiIpFilterParamsDstIpFullMask_Object = MibTableColumn
tLiIpFilterParamsDstIpFullMask = _TLiIpFilterParamsDstIpFullMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 16, 1, 10),
    _TLiIpFilterParamsDstIpFullMask_Type()
)
tLiIpFilterParamsDstIpFullMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiIpFilterParamsDstIpFullMask.setStatus("current")


class _TLiIpFilterParamsProtocolNextHdr_Type(TIpProtocol):
    """Custom type tLiIpFilterParamsProtocolNextHdr based on TIpProtocol"""
    defaultValue = -1


_TLiIpFilterParamsProtocolNextHdr_Type.__name__ = "TIpProtocol"
_TLiIpFilterParamsProtocolNextHdr_Object = MibTableColumn
tLiIpFilterParamsProtocolNextHdr = _TLiIpFilterParamsProtocolNextHdr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 16, 1, 11),
    _TLiIpFilterParamsProtocolNextHdr_Type()
)
tLiIpFilterParamsProtocolNextHdr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiIpFilterParamsProtocolNextHdr.setStatus("current")


class _TLiIpFilterParamsSrcPortValue1_Type(TTcpUdpPort):
    """Custom type tLiIpFilterParamsSrcPortValue1 based on TTcpUdpPort"""
    defaultValue = 0


_TLiIpFilterParamsSrcPortValue1_Type.__name__ = "TTcpUdpPort"
_TLiIpFilterParamsSrcPortValue1_Object = MibTableColumn
tLiIpFilterParamsSrcPortValue1 = _TLiIpFilterParamsSrcPortValue1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 16, 1, 12),
    _TLiIpFilterParamsSrcPortValue1_Type()
)
tLiIpFilterParamsSrcPortValue1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiIpFilterParamsSrcPortValue1.setStatus("current")


class _TLiIpFilterParamsSrcPortValue2_Type(TTcpUdpPort):
    """Custom type tLiIpFilterParamsSrcPortValue2 based on TTcpUdpPort"""
    defaultValue = 0


_TLiIpFilterParamsSrcPortValue2_Type.__name__ = "TTcpUdpPort"
_TLiIpFilterParamsSrcPortValue2_Object = MibTableColumn
tLiIpFilterParamsSrcPortValue2 = _TLiIpFilterParamsSrcPortValue2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 16, 1, 13),
    _TLiIpFilterParamsSrcPortValue2_Type()
)
tLiIpFilterParamsSrcPortValue2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiIpFilterParamsSrcPortValue2.setStatus("current")


class _TLiIpFilterParamsSrcPortOper_Type(TOperator):
    """Custom type tLiIpFilterParamsSrcPortOper based on TOperator"""
    defaultValue = 0


_TLiIpFilterParamsSrcPortOper_Type.__name__ = "TOperator"
_TLiIpFilterParamsSrcPortOper_Object = MibTableColumn
tLiIpFilterParamsSrcPortOper = _TLiIpFilterParamsSrcPortOper_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 16, 1, 14),
    _TLiIpFilterParamsSrcPortOper_Type()
)
tLiIpFilterParamsSrcPortOper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiIpFilterParamsSrcPortOper.setStatus("current")


class _TLiIpFilterParamsDstPortValue1_Type(TTcpUdpPort):
    """Custom type tLiIpFilterParamsDstPortValue1 based on TTcpUdpPort"""
    defaultValue = 0


_TLiIpFilterParamsDstPortValue1_Type.__name__ = "TTcpUdpPort"
_TLiIpFilterParamsDstPortValue1_Object = MibTableColumn
tLiIpFilterParamsDstPortValue1 = _TLiIpFilterParamsDstPortValue1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 16, 1, 15),
    _TLiIpFilterParamsDstPortValue1_Type()
)
tLiIpFilterParamsDstPortValue1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiIpFilterParamsDstPortValue1.setStatus("current")


class _TLiIpFilterParamsDstPortValue2_Type(TTcpUdpPort):
    """Custom type tLiIpFilterParamsDstPortValue2 based on TTcpUdpPort"""
    defaultValue = 0


_TLiIpFilterParamsDstPortValue2_Type.__name__ = "TTcpUdpPort"
_TLiIpFilterParamsDstPortValue2_Object = MibTableColumn
tLiIpFilterParamsDstPortValue2 = _TLiIpFilterParamsDstPortValue2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 16, 1, 16),
    _TLiIpFilterParamsDstPortValue2_Type()
)
tLiIpFilterParamsDstPortValue2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiIpFilterParamsDstPortValue2.setStatus("current")


class _TLiIpFilterParamsDstPortOper_Type(TOperator):
    """Custom type tLiIpFilterParamsDstPortOper based on TOperator"""
    defaultValue = 0


_TLiIpFilterParamsDstPortOper_Type.__name__ = "TOperator"
_TLiIpFilterParamsDstPortOper_Object = MibTableColumn
tLiIpFilterParamsDstPortOper = _TLiIpFilterParamsDstPortOper_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 16, 1, 17),
    _TLiIpFilterParamsDstPortOper_Type()
)
tLiIpFilterParamsDstPortOper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiIpFilterParamsDstPortOper.setStatus("current")


class _TLiIpFilterParamsFragment_Type(TItemMatch):
    """Custom type tLiIpFilterParamsFragment based on TItemMatch"""
    defaultValue = 1


_TLiIpFilterParamsFragment_Type.__name__ = "TItemMatch"
_TLiIpFilterParamsFragment_Object = MibTableColumn
tLiIpFilterParamsFragment = _TLiIpFilterParamsFragment_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 16, 1, 18),
    _TLiIpFilterParamsFragment_Type()
)
tLiIpFilterParamsFragment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiIpFilterParamsFragment.setStatus("current")
_TLiIpFilterParamsInfoTable_Object = MibTable
tLiIpFilterParamsInfoTable = _TLiIpFilterParamsInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 17)
)
if mibBuilder.loadTexts:
    tLiIpFilterParamsInfoTable.setStatus("current")
_TLiIpFilterParamsInfoEntry_Object = MibTableRow
tLiIpFilterParamsInfoEntry = _TLiIpFilterParamsInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 17, 1)
)
if mibBuilder.loadTexts:
    tLiIpFilterParamsInfoEntry.setStatus("current")
_TLiIpFltrParamsInfIngrHitCount_Type = Counter64
_TLiIpFltrParamsInfIngrHitCount_Object = MibTableColumn
tLiIpFltrParamsInfIngrHitCount = _TLiIpFltrParamsInfIngrHitCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 17, 1, 1),
    _TLiIpFltrParamsInfIngrHitCount_Type()
)
tLiIpFltrParamsInfIngrHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLiIpFltrParamsInfIngrHitCount.setStatus("current")
_TLiIpFltrParamsInfEgrHitCount_Type = Counter64
_TLiIpFltrParamsInfEgrHitCount_Object = MibTableColumn
tLiIpFltrParamsInfEgrHitCount = _TLiIpFltrParamsInfEgrHitCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 17, 1, 2),
    _TLiIpFltrParamsInfEgrHitCount_Type()
)
tLiIpFltrParamsInfEgrHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLiIpFltrParamsInfEgrHitCount.setStatus("current")
_TLiIpFltrParamsInfIngrHitBytes_Type = Counter64
_TLiIpFltrParamsInfIngrHitBytes_Object = MibTableColumn
tLiIpFltrParamsInfIngrHitBytes = _TLiIpFltrParamsInfIngrHitBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 17, 1, 3),
    _TLiIpFltrParamsInfIngrHitBytes_Type()
)
tLiIpFltrParamsInfIngrHitBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLiIpFltrParamsInfIngrHitBytes.setStatus("current")
_TLiIpFltrParamsInfEgrHitBytes_Type = Counter64
_TLiIpFltrParamsInfEgrHitBytes_Object = MibTableColumn
tLiIpFltrParamsInfEgrHitBytes = _TLiIpFltrParamsInfEgrHitBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 17, 1, 4),
    _TLiIpFltrParamsInfEgrHitBytes_Type()
)
tLiIpFltrParamsInfEgrHitBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLiIpFltrParamsInfEgrHitBytes.setStatus("current")
_TLiRsvdBlockFltrAssocTableLChg_Type = TimeStamp
_TLiRsvdBlockFltrAssocTableLChg_Object = MibScalar
tLiRsvdBlockFltrAssocTableLChg = _TLiRsvdBlockFltrAssocTableLChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 18),
    _TLiRsvdBlockFltrAssocTableLChg_Type()
)
tLiRsvdBlockFltrAssocTableLChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLiRsvdBlockFltrAssocTableLChg.setStatus("current")
_TLiRsvdBlockFltrAssocTable_Object = MibTable
tLiRsvdBlockFltrAssocTable = _TLiRsvdBlockFltrAssocTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 19)
)
if mibBuilder.loadTexts:
    tLiRsvdBlockFltrAssocTable.setStatus("current")
_TLiRsvdBlockFltrAssocEntry_Object = MibTableRow
tLiRsvdBlockFltrAssocEntry = _TLiRsvdBlockFltrAssocEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 19, 1)
)
tLiRsvdBlockFltrAssocEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tLiReservedBlockName"),
    (0, "TIMETRA-FILTER-MIB", "tLiRsvdBlockFltrAssocFltrType"),
    (0, "TIMETRA-FILTER-MIB", "tLiRsvdBlockFltrAssocFltrName"),
)
if mibBuilder.loadTexts:
    tLiRsvdBlockFltrAssocEntry.setStatus("current")
_TLiRsvdBlockFltrAssocFltrType_Type = TFilterType
_TLiRsvdBlockFltrAssocFltrType_Object = MibTableColumn
tLiRsvdBlockFltrAssocFltrType = _TLiRsvdBlockFltrAssocFltrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 19, 1, 1),
    _TLiRsvdBlockFltrAssocFltrType_Type()
)
tLiRsvdBlockFltrAssocFltrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tLiRsvdBlockFltrAssocFltrType.setStatus("current")
_TLiRsvdBlockFltrAssocFltrName_Type = TLNamedItem
_TLiRsvdBlockFltrAssocFltrName_Object = MibTableColumn
tLiRsvdBlockFltrAssocFltrName = _TLiRsvdBlockFltrAssocFltrName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 19, 1, 3),
    _TLiRsvdBlockFltrAssocFltrName_Type()
)
tLiRsvdBlockFltrAssocFltrName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tLiRsvdBlockFltrAssocFltrName.setStatus("current")
_TLiRsvdBlockFltrAssocRowStatus_Type = RowStatus
_TLiRsvdBlockFltrAssocRowStatus_Object = MibTableColumn
tLiRsvdBlockFltrAssocRowStatus = _TLiRsvdBlockFltrAssocRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 19, 1, 4),
    _TLiRsvdBlockFltrAssocRowStatus_Type()
)
tLiRsvdBlockFltrAssocRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiRsvdBlockFltrAssocRowStatus.setStatus("current")
_TLiRsvdBlockFltrAssocLastChanged_Type = TimeStamp
_TLiRsvdBlockFltrAssocLastChanged_Object = MibTableColumn
tLiRsvdBlockFltrAssocLastChanged = _TLiRsvdBlockFltrAssocLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 19, 1, 5),
    _TLiRsvdBlockFltrAssocLastChanged_Type()
)
tLiRsvdBlockFltrAssocLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLiRsvdBlockFltrAssocLastChanged.setStatus("current")
_TLiFltrAssocFltrNameTableLastChg_Type = TimeStamp
_TLiFltrAssocFltrNameTableLastChg_Object = MibScalar
tLiFltrAssocFltrNameTableLastChg = _TLiFltrAssocFltrNameTableLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 20),
    _TLiFltrAssocFltrNameTableLastChg_Type()
)
tLiFltrAssocFltrNameTableLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLiFltrAssocFltrNameTableLastChg.setStatus("current")
_TLiFltrAssocFltrNameTable_Object = MibTable
tLiFltrAssocFltrNameTable = _TLiFltrAssocFltrNameTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 21)
)
if mibBuilder.loadTexts:
    tLiFltrAssocFltrNameTable.setStatus("current")
_TLiFltrAssocFltrNameEntry_Object = MibTableRow
tLiFltrAssocFltrNameEntry = _TLiFltrAssocFltrNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 21, 1)
)
tLiFltrAssocFltrNameEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tLiFilterType"),
    (0, "TIMETRA-FILTER-MIB", "tLiFilterName"),
    (0, "TIMETRA-FILTER-MIB", "tLiFltrAssocFltrName"),
)
if mibBuilder.loadTexts:
    tLiFltrAssocFltrNameEntry.setStatus("current")
_TLiFltrAssocFltrName_Type = TLNamedItem
_TLiFltrAssocFltrName_Object = MibTableColumn
tLiFltrAssocFltrName = _TLiFltrAssocFltrName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 21, 1, 1),
    _TLiFltrAssocFltrName_Type()
)
tLiFltrAssocFltrName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tLiFltrAssocFltrName.setStatus("current")
_TLiFltrAssocFltrNameRowStatus_Type = RowStatus
_TLiFltrAssocFltrNameRowStatus_Object = MibTableColumn
tLiFltrAssocFltrNameRowStatus = _TLiFltrAssocFltrNameRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 21, 1, 2),
    _TLiFltrAssocFltrNameRowStatus_Type()
)
tLiFltrAssocFltrNameRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLiFltrAssocFltrNameRowStatus.setStatus("current")
_TLiFltrAssocFltrNameLastChg_Type = TimeStamp
_TLiFltrAssocFltrNameLastChg_Object = MibTableColumn
tLiFltrAssocFltrNameLastChg = _TLiFltrAssocFltrNameLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 31, 21, 1, 3),
    _TLiFltrAssocFltrNameLastChg_Type()
)
tLiFltrAssocFltrNameLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLiFltrAssocFltrNameLastChg.setStatus("current")
_TFilterPrefixListTableLstChng_Type = TimeStamp
_TFilterPrefixListTableLstChng_Object = MibScalar
tFilterPrefixListTableLstChng = _TFilterPrefixListTableLstChng_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 32),
    _TFilterPrefixListTableLstChng_Type()
)
tFilterPrefixListTableLstChng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterPrefixListTableLstChng.setStatus("current")
_TFilterPrefixListTable_Object = MibTable
tFilterPrefixListTable = _TFilterPrefixListTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 33)
)
if mibBuilder.loadTexts:
    tFilterPrefixListTable.setStatus("current")
_TFilterPrefixListEntry_Object = MibTableRow
tFilterPrefixListEntry = _TFilterPrefixListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 33, 1)
)
tFilterPrefixListEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tFilterPrefixListType"),
    (1, "TIMETRA-FILTER-MIB", "tFilterPrefixListName"),
)
if mibBuilder.loadTexts:
    tFilterPrefixListEntry.setStatus("current")
_TFilterPrefixListType_Type = TFltrPrefixListType
_TFilterPrefixListType_Object = MibTableColumn
tFilterPrefixListType = _TFilterPrefixListType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 33, 1, 1),
    _TFilterPrefixListType_Type()
)
tFilterPrefixListType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterPrefixListType.setStatus("current")
_TFilterPrefixListName_Type = TNamedItem
_TFilterPrefixListName_Object = MibTableColumn
tFilterPrefixListName = _TFilterPrefixListName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 33, 1, 2),
    _TFilterPrefixListName_Type()
)
tFilterPrefixListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterPrefixListName.setStatus("current")
_TFilterPrefixListRowStatus_Type = RowStatus
_TFilterPrefixListRowStatus_Object = MibTableColumn
tFilterPrefixListRowStatus = _TFilterPrefixListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 33, 1, 3),
    _TFilterPrefixListRowStatus_Type()
)
tFilterPrefixListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterPrefixListRowStatus.setStatus("current")
_TFilterPrefixListLastChanged_Type = TimeStamp
_TFilterPrefixListLastChanged_Object = MibTableColumn
tFilterPrefixListLastChanged = _TFilterPrefixListLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 33, 1, 4),
    _TFilterPrefixListLastChanged_Type()
)
tFilterPrefixListLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterPrefixListLastChanged.setStatus("current")


class _TFilterPrefixListDescription_Type(TItemDescription):
    """Custom type tFilterPrefixListDescription based on TItemDescription"""
    defaultHexValue = ""


_TFilterPrefixListDescription_Type.__name__ = "TItemDescription"
_TFilterPrefixListDescription_Object = MibTableColumn
tFilterPrefixListDescription = _TFilterPrefixListDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 33, 1, 5),
    _TFilterPrefixListDescription_Type()
)
tFilterPrefixListDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterPrefixListDescription.setStatus("current")
_TFilterPrefixListEntryTblLstChg_Type = TimeStamp
_TFilterPrefixListEntryTblLstChg_Object = MibScalar
tFilterPrefixListEntryTblLstChg = _TFilterPrefixListEntryTblLstChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 34),
    _TFilterPrefixListEntryTblLstChg_Type()
)
tFilterPrefixListEntryTblLstChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterPrefixListEntryTblLstChg.setStatus("current")
_TFilterPrefixListEntryTable_Object = MibTable
tFilterPrefixListEntryTable = _TFilterPrefixListEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 35)
)
if mibBuilder.loadTexts:
    tFilterPrefixListEntryTable.setStatus("current")
_TFilterPrefixListEntryEntry_Object = MibTableRow
tFilterPrefixListEntryEntry = _TFilterPrefixListEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 35, 1)
)
tFilterPrefixListEntryEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tFilterPrefixListType"),
    (0, "TIMETRA-FILTER-MIB", "tFilterPrefixListName"),
    (0, "TIMETRA-FILTER-MIB", "tFilterPrefixListEntryPrefixType"),
    (0, "TIMETRA-FILTER-MIB", "tFilterPrefixListEntryPrefix"),
    (0, "TIMETRA-FILTER-MIB", "tFilterPrefixListEntryPrefixLen"),
)
if mibBuilder.loadTexts:
    tFilterPrefixListEntryEntry.setStatus("current")
_TFilterPrefixListEntryPrefixType_Type = TmnxAddressAndPrefixType
_TFilterPrefixListEntryPrefixType_Object = MibTableColumn
tFilterPrefixListEntryPrefixType = _TFilterPrefixListEntryPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 35, 1, 1),
    _TFilterPrefixListEntryPrefixType_Type()
)
tFilterPrefixListEntryPrefixType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterPrefixListEntryPrefixType.setStatus("current")


class _TFilterPrefixListEntryPrefix_Type(TmnxAddressAndPrefixAddress):
    """Custom type tFilterPrefixListEntryPrefix based on TmnxAddressAndPrefixAddress"""
    subtypeSpec = TmnxAddressAndPrefixAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TFilterPrefixListEntryPrefix_Type.__name__ = "TmnxAddressAndPrefixAddress"
_TFilterPrefixListEntryPrefix_Object = MibTableColumn
tFilterPrefixListEntryPrefix = _TFilterPrefixListEntryPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 35, 1, 2),
    _TFilterPrefixListEntryPrefix_Type()
)
tFilterPrefixListEntryPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterPrefixListEntryPrefix.setStatus("current")
_TFilterPrefixListEntryPrefixLen_Type = TmnxAddressAndPrefixPrefix
_TFilterPrefixListEntryPrefixLen_Object = MibTableColumn
tFilterPrefixListEntryPrefixLen = _TFilterPrefixListEntryPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 35, 1, 3),
    _TFilterPrefixListEntryPrefixLen_Type()
)
tFilterPrefixListEntryPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterPrefixListEntryPrefixLen.setStatus("current")
_TFilterPrefixListEntryRowStatus_Type = RowStatus
_TFilterPrefixListEntryRowStatus_Object = MibTableColumn
tFilterPrefixListEntryRowStatus = _TFilterPrefixListEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 35, 1, 4),
    _TFilterPrefixListEntryRowStatus_Type()
)
tFilterPrefixListEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterPrefixListEntryRowStatus.setStatus("current")
_TFilterEmbeddedRefTableLstChg_Type = TimeStamp
_TFilterEmbeddedRefTableLstChg_Object = MibScalar
tFilterEmbeddedRefTableLstChg = _TFilterEmbeddedRefTableLstChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 36),
    _TFilterEmbeddedRefTableLstChg_Type()
)
tFilterEmbeddedRefTableLstChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterEmbeddedRefTableLstChg.setStatus("current")
_TFilterEmbeddedRefTable_Object = MibTable
tFilterEmbeddedRefTable = _TFilterEmbeddedRefTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 37)
)
if mibBuilder.loadTexts:
    tFilterEmbeddedRefTable.setStatus("current")
_TFilterEmbeddedRefTableEntry_Object = MibTableRow
tFilterEmbeddedRefTableEntry = _TFilterEmbeddedRefTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 37, 1)
)
tFilterEmbeddedRefTableEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tFilterEmbeddedRefFilterType"),
    (0, "TIMETRA-FILTER-MIB", "tFilterEmbeddedRefInsertFltrId"),
    (0, "TIMETRA-FILTER-MIB", "tFilterEmbeddedRefEmbeddedFltrId"),
    (0, "TIMETRA-FILTER-MIB", "tFilterEmbeddedRefOffset"),
)
if mibBuilder.loadTexts:
    tFilterEmbeddedRefTableEntry.setStatus("current")
_TFilterEmbeddedRefFilterType_Type = TFilterType
_TFilterEmbeddedRefFilterType_Object = MibTableColumn
tFilterEmbeddedRefFilterType = _TFilterEmbeddedRefFilterType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 37, 1, 1),
    _TFilterEmbeddedRefFilterType_Type()
)
tFilterEmbeddedRefFilterType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterEmbeddedRefFilterType.setStatus("current")
_TFilterEmbeddedRefInsertFltrId_Type = TFilterID
_TFilterEmbeddedRefInsertFltrId_Object = MibTableColumn
tFilterEmbeddedRefInsertFltrId = _TFilterEmbeddedRefInsertFltrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 37, 1, 2),
    _TFilterEmbeddedRefInsertFltrId_Type()
)
tFilterEmbeddedRefInsertFltrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterEmbeddedRefInsertFltrId.setStatus("current")
_TFilterEmbeddedRefEmbeddedFltrId_Type = TFilterID
_TFilterEmbeddedRefEmbeddedFltrId_Object = MibTableColumn
tFilterEmbeddedRefEmbeddedFltrId = _TFilterEmbeddedRefEmbeddedFltrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 37, 1, 3),
    _TFilterEmbeddedRefEmbeddedFltrId_Type()
)
tFilterEmbeddedRefEmbeddedFltrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterEmbeddedRefEmbeddedFltrId.setStatus("current")
_TFilterEmbeddedRefOffset_Type = TFilterEmbedOffset
_TFilterEmbeddedRefOffset_Object = MibTableColumn
tFilterEmbeddedRefOffset = _TFilterEmbeddedRefOffset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 37, 1, 4),
    _TFilterEmbeddedRefOffset_Type()
)
tFilterEmbeddedRefOffset.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterEmbeddedRefOffset.setStatus("current")
_TFilterEmbeddedRefRowStatus_Type = RowStatus
_TFilterEmbeddedRefRowStatus_Object = MibTableColumn
tFilterEmbeddedRefRowStatus = _TFilterEmbeddedRefRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 37, 1, 5),
    _TFilterEmbeddedRefRowStatus_Type()
)
tFilterEmbeddedRefRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterEmbeddedRefRowStatus.setStatus("current")


class _TFilterEmbeddedRefAdminState_Type(TmnxEmbeddedFltrAdminState):
    """Custom type tFilterEmbeddedRefAdminState based on TmnxEmbeddedFltrAdminState"""
    defaultValue = 1


_TFilterEmbeddedRefAdminState_Type.__name__ = "TmnxEmbeddedFltrAdminState"
_TFilterEmbeddedRefAdminState_Object = MibTableColumn
tFilterEmbeddedRefAdminState = _TFilterEmbeddedRefAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 37, 1, 6),
    _TFilterEmbeddedRefAdminState_Type()
)
tFilterEmbeddedRefAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterEmbeddedRefAdminState.setStatus("current")
_TFilterEmbeddedRefOperState_Type = TmnxEmbeddedFltrOperState
_TFilterEmbeddedRefOperState_Object = MibTableColumn
tFilterEmbeddedRefOperState = _TFilterEmbeddedRefOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 37, 1, 7),
    _TFilterEmbeddedRefOperState_Type()
)
tFilterEmbeddedRefOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterEmbeddedRefOperState.setStatus("current")
_TFilterEmbeddedRefLastChanged_Type = TimeStamp
_TFilterEmbeddedRefLastChanged_Object = MibTableColumn
tFilterEmbeddedRefLastChanged = _TFilterEmbeddedRefLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 37, 1, 8),
    _TFilterEmbeddedRefLastChanged_Type()
)
tFilterEmbeddedRefLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterEmbeddedRefLastChanged.setStatus("current")
_TFilterPortListTableLstChng_Type = TimeStamp
_TFilterPortListTableLstChng_Object = MibScalar
tFilterPortListTableLstChng = _TFilterPortListTableLstChng_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 38),
    _TFilterPortListTableLstChng_Type()
)
tFilterPortListTableLstChng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterPortListTableLstChng.setStatus("current")
_TFilterPortListTable_Object = MibTable
tFilterPortListTable = _TFilterPortListTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 39)
)
if mibBuilder.loadTexts:
    tFilterPortListTable.setStatus("current")
_TFilterPortListEntry_Object = MibTableRow
tFilterPortListEntry = _TFilterPortListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 39, 1)
)
tFilterPortListEntry.setIndexNames(
    (1, "TIMETRA-FILTER-MIB", "tFilterPortListName"),
)
if mibBuilder.loadTexts:
    tFilterPortListEntry.setStatus("current")
_TFilterPortListName_Type = TNamedItem
_TFilterPortListName_Object = MibTableColumn
tFilterPortListName = _TFilterPortListName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 39, 1, 1),
    _TFilterPortListName_Type()
)
tFilterPortListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterPortListName.setStatus("current")
_TFilterPortListRowStatus_Type = RowStatus
_TFilterPortListRowStatus_Object = MibTableColumn
tFilterPortListRowStatus = _TFilterPortListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 39, 1, 2),
    _TFilterPortListRowStatus_Type()
)
tFilterPortListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterPortListRowStatus.setStatus("current")
_TFilterPortListLastChanged_Type = TimeStamp
_TFilterPortListLastChanged_Object = MibTableColumn
tFilterPortListLastChanged = _TFilterPortListLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 39, 1, 3),
    _TFilterPortListLastChanged_Type()
)
tFilterPortListLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterPortListLastChanged.setStatus("current")


class _TFilterPortListDescription_Type(TItemDescription):
    """Custom type tFilterPortListDescription based on TItemDescription"""
    defaultHexValue = ""


_TFilterPortListDescription_Type.__name__ = "TItemDescription"
_TFilterPortListDescription_Object = MibTableColumn
tFilterPortListDescription = _TFilterPortListDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 39, 1, 4),
    _TFilterPortListDescription_Type()
)
tFilterPortListDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterPortListDescription.setStatus("current")
_TFilterPortListEntryTblLstChg_Type = TimeStamp
_TFilterPortListEntryTblLstChg_Object = MibScalar
tFilterPortListEntryTblLstChg = _TFilterPortListEntryTblLstChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 40),
    _TFilterPortListEntryTblLstChg_Type()
)
tFilterPortListEntryTblLstChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterPortListEntryTblLstChg.setStatus("current")
_TFilterPortListEntryTable_Object = MibTable
tFilterPortListEntryTable = _TFilterPortListEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 41)
)
if mibBuilder.loadTexts:
    tFilterPortListEntryTable.setStatus("current")
_TFilterPortListEntryEntry_Object = MibTableRow
tFilterPortListEntryEntry = _TFilterPortListEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 41, 1)
)
tFilterPortListEntryEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tFilterPortListName"),
    (0, "TIMETRA-FILTER-MIB", "tFilterPortListEntryPortLow"),
    (0, "TIMETRA-FILTER-MIB", "tFilterPortListEntryPortHigh"),
)
if mibBuilder.loadTexts:
    tFilterPortListEntryEntry.setStatus("current")
_TFilterPortListEntryPortLow_Type = TTcpUdpPort
_TFilterPortListEntryPortLow_Object = MibTableColumn
tFilterPortListEntryPortLow = _TFilterPortListEntryPortLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 41, 1, 1),
    _TFilterPortListEntryPortLow_Type()
)
tFilterPortListEntryPortLow.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterPortListEntryPortLow.setStatus("current")
_TFilterPortListEntryPortHigh_Type = TTcpUdpPort
_TFilterPortListEntryPortHigh_Object = MibTableColumn
tFilterPortListEntryPortHigh = _TFilterPortListEntryPortHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 41, 1, 2),
    _TFilterPortListEntryPortHigh_Type()
)
tFilterPortListEntryPortHigh.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterPortListEntryPortHigh.setStatus("current")
_TFilterPortListEntryRowStatus_Type = RowStatus
_TFilterPortListEntryRowStatus_Object = MibTableColumn
tFilterPortListEntryRowStatus = _TFilterPortListEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 41, 1, 3),
    _TFilterPortListEntryRowStatus_Type()
)
tFilterPortListEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterPortListEntryRowStatus.setStatus("current")
_TFilterApplyPathTableLstChng_Type = TimeStamp
_TFilterApplyPathTableLstChng_Object = MibScalar
tFilterApplyPathTableLstChng = _TFilterApplyPathTableLstChng_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 42),
    _TFilterApplyPathTableLstChng_Type()
)
tFilterApplyPathTableLstChng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterApplyPathTableLstChng.setStatus("current")
_TFilterApplyPathTable_Object = MibTable
tFilterApplyPathTable = _TFilterApplyPathTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 43)
)
if mibBuilder.loadTexts:
    tFilterApplyPathTable.setStatus("current")
_TFilterApplyPathEntry_Object = MibTableRow
tFilterApplyPathEntry = _TFilterApplyPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 43, 1)
)
tFilterApplyPathEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tFilterPrefixListType"),
    (0, "TIMETRA-FILTER-MIB", "tFilterPrefixListName"),
    (0, "TIMETRA-FILTER-MIB", "tFilterApplyPathSource"),
    (0, "TIMETRA-FILTER-MIB", "tFilterApplyPathIndex"),
)
if mibBuilder.loadTexts:
    tFilterApplyPathEntry.setStatus("current")


class _TFilterApplyPathSource_Type(Integer32):
    """Custom type tFilterApplyPathSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("bgp-peers", 1))
    )


_TFilterApplyPathSource_Type.__name__ = "Integer32"
_TFilterApplyPathSource_Object = MibTableColumn
tFilterApplyPathSource = _TFilterApplyPathSource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 43, 1, 1),
    _TFilterApplyPathSource_Type()
)
tFilterApplyPathSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterApplyPathSource.setStatus("current")


class _TFilterApplyPathIndex_Type(Unsigned32):
    """Custom type tFilterApplyPathIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TFilterApplyPathIndex_Type.__name__ = "Unsigned32"
_TFilterApplyPathIndex_Object = MibTableColumn
tFilterApplyPathIndex = _TFilterApplyPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 43, 1, 2),
    _TFilterApplyPathIndex_Type()
)
tFilterApplyPathIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterApplyPathIndex.setStatus("current")
_TFilterApplyPathRowStatus_Type = RowStatus
_TFilterApplyPathRowStatus_Object = MibTableColumn
tFilterApplyPathRowStatus = _TFilterApplyPathRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 43, 1, 3),
    _TFilterApplyPathRowStatus_Type()
)
tFilterApplyPathRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterApplyPathRowStatus.setStatus("current")
_TFilterApplyPathLastChanged_Type = TimeStamp
_TFilterApplyPathLastChanged_Object = MibTableColumn
tFilterApplyPathLastChanged = _TFilterApplyPathLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 43, 1, 4),
    _TFilterApplyPathLastChanged_Type()
)
tFilterApplyPathLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterApplyPathLastChanged.setStatus("current")


class _TFilterApplyPathMatch1_Type(TRegularExpression):
    """Custom type tFilterApplyPathMatch1 based on TRegularExpression"""
    defaultHexValue = ""


_TFilterApplyPathMatch1_Type.__name__ = "TRegularExpression"
_TFilterApplyPathMatch1_Object = MibTableColumn
tFilterApplyPathMatch1 = _TFilterApplyPathMatch1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 43, 1, 5),
    _TFilterApplyPathMatch1_Type()
)
tFilterApplyPathMatch1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterApplyPathMatch1.setStatus("current")


class _TFilterApplyPathMatch2_Type(TRegularExpression):
    """Custom type tFilterApplyPathMatch2 based on TRegularExpression"""
    defaultHexValue = ""


_TFilterApplyPathMatch2_Type.__name__ = "TRegularExpression"
_TFilterApplyPathMatch2_Object = MibTableColumn
tFilterApplyPathMatch2 = _TFilterApplyPathMatch2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 43, 1, 6),
    _TFilterApplyPathMatch2_Type()
)
tFilterApplyPathMatch2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterApplyPathMatch2.setStatus("current")


class _TFilterApplyPathVRtrId_Type(TmnxVRtrID):
    """Custom type tFilterApplyPathVRtrId based on TmnxVRtrID"""
    defaultValue = 1


_TFilterApplyPathVRtrId_Type.__name__ = "TmnxVRtrID"
_TFilterApplyPathVRtrId_Object = MibTableColumn
tFilterApplyPathVRtrId = _TFilterApplyPathVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 43, 1, 7),
    _TFilterApplyPathVRtrId_Type()
)
tFilterApplyPathVRtrId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterApplyPathVRtrId.setStatus("current")
_TFilterEmbeddedRefInfoTable_Object = MibTable
tFilterEmbeddedRefInfoTable = _TFilterEmbeddedRefInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 44)
)
if mibBuilder.loadTexts:
    tFilterEmbeddedRefInfoTable.setStatus("current")
_TFilterEmbeddedRefInfoEntry_Object = MibTableRow
tFilterEmbeddedRefInfoEntry = _TFilterEmbeddedRefInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 44, 1)
)
if mibBuilder.loadTexts:
    tFilterEmbeddedRefInfoEntry.setStatus("current")
_TFltrEmbedRefInfEntryCnt_Type = Unsigned32
_TFltrEmbedRefInfEntryCnt_Object = MibTableColumn
tFltrEmbedRefInfEntryCnt = _TFltrEmbedRefInfEntryCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 44, 1, 1),
    _TFltrEmbedRefInfEntryCnt_Type()
)
tFltrEmbedRefInfEntryCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrEmbedRefInfEntryCnt.setStatus("current")
_TFltrEmbedRefInfEntryCntInsrtd_Type = Unsigned32
_TFltrEmbedRefInfEntryCntInsrtd_Object = MibTableColumn
tFltrEmbedRefInfEntryCntInsrtd = _TFltrEmbedRefInfEntryCntInsrtd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 44, 1, 2),
    _TFltrEmbedRefInfEntryCntInsrtd_Type()
)
tFltrEmbedRefInfEntryCntInsrtd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrEmbedRefInfEntryCntInsrtd.setStatus("current")
_TFilterEmbeddedEntryRefInfoTable_Object = MibTable
tFilterEmbeddedEntryRefInfoTable = _TFilterEmbeddedEntryRefInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 45)
)
if mibBuilder.loadTexts:
    tFilterEmbeddedEntryRefInfoTable.setStatus("current")
_TFilterEmbeddedEntryRefInfoEntry_Object = MibTableRow
tFilterEmbeddedEntryRefInfoEntry = _TFilterEmbeddedEntryRefInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 45, 1)
)
tFilterEmbeddedEntryRefInfoEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tFltrEmbedEntryFilterType"),
    (0, "TIMETRA-FILTER-MIB", "tFltrEmbedEntryInsertFltrId"),
    (0, "TIMETRA-FILTER-MIB", "tFltrEmbedEntryEmbeddedFltrId"),
    (0, "TIMETRA-FILTER-MIB", "tFltrEmbedEntryEmbeddedEntryId"),
)
if mibBuilder.loadTexts:
    tFilterEmbeddedEntryRefInfoEntry.setStatus("current")
_TFltrEmbedEntryFilterType_Type = TFilterType
_TFltrEmbedEntryFilterType_Object = MibTableColumn
tFltrEmbedEntryFilterType = _TFltrEmbedEntryFilterType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 45, 1, 1),
    _TFltrEmbedEntryFilterType_Type()
)
tFltrEmbedEntryFilterType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFltrEmbedEntryFilterType.setStatus("current")
_TFltrEmbedEntryInsertFltrId_Type = TFilterID
_TFltrEmbedEntryInsertFltrId_Object = MibTableColumn
tFltrEmbedEntryInsertFltrId = _TFltrEmbedEntryInsertFltrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 45, 1, 2),
    _TFltrEmbedEntryInsertFltrId_Type()
)
tFltrEmbedEntryInsertFltrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFltrEmbedEntryInsertFltrId.setStatus("current")
_TFltrEmbedEntryEmbeddedFltrId_Type = TFilterID
_TFltrEmbedEntryEmbeddedFltrId_Object = MibTableColumn
tFltrEmbedEntryEmbeddedFltrId = _TFltrEmbedEntryEmbeddedFltrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 45, 1, 3),
    _TFltrEmbedEntryEmbeddedFltrId_Type()
)
tFltrEmbedEntryEmbeddedFltrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFltrEmbedEntryEmbeddedFltrId.setStatus("current")
_TFltrEmbedEntryEmbeddedEntryId_Type = TEntryId
_TFltrEmbedEntryEmbeddedEntryId_Object = MibTableColumn
tFltrEmbedEntryEmbeddedEntryId = _TFltrEmbedEntryEmbeddedEntryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 45, 1, 4),
    _TFltrEmbedEntryEmbeddedEntryId_Type()
)
tFltrEmbedEntryEmbeddedEntryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFltrEmbedEntryEmbeddedEntryId.setStatus("current")
_TFltrEmbedEntryInsrtEntryId_Type = TAnyEntryId
_TFltrEmbedEntryInsrtEntryId_Object = MibTableColumn
tFltrEmbedEntryInsrtEntryId = _TFltrEmbedEntryInsrtEntryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 45, 1, 5),
    _TFltrEmbedEntryInsrtEntryId_Type()
)
tFltrEmbedEntryInsrtEntryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrEmbedEntryInsrtEntryId.setStatus("current")
_TFltrEmbedEntryRefOperState_Type = TmnxFltrEmbeddedEntryState
_TFltrEmbedEntryRefOperState_Object = MibTableColumn
tFltrEmbedEntryRefOperState = _TFltrEmbedEntryRefOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 45, 1, 6),
    _TFltrEmbedEntryRefOperState_Type()
)
tFltrEmbedEntryRefOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrEmbedEntryRefOperState.setStatus("current")
_TIPv6FilterParamsExtTbleLstChgd_Type = TimeStamp
_TIPv6FilterParamsExtTbleLstChgd_Object = MibScalar
tIPv6FilterParamsExtTbleLstChgd = _TIPv6FilterParamsExtTbleLstChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 46),
    _TIPv6FilterParamsExtTbleLstChgd_Type()
)
tIPv6FilterParamsExtTbleLstChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPv6FilterParamsExtTbleLstChgd.setStatus("current")
_TIPv6FilterParamsExtTable_Object = MibTable
tIPv6FilterParamsExtTable = _TIPv6FilterParamsExtTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 47)
)
if mibBuilder.loadTexts:
    tIPv6FilterParamsExtTable.setStatus("current")
_TIPv6FilterParamsExtEntry_Object = MibTableRow
tIPv6FilterParamsExtEntry = _TIPv6FilterParamsExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 47, 1)
)
if mibBuilder.loadTexts:
    tIPv6FilterParamsExtEntry.setStatus("current")
_TIPv6FilterParamsExtLastChanged_Type = TimeStamp
_TIPv6FilterParamsExtLastChanged_Object = MibTableColumn
tIPv6FilterParamsExtLastChanged = _TIPv6FilterParamsExtLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 47, 1, 1),
    _TIPv6FilterParamsExtLastChanged_Type()
)
tIPv6FilterParamsExtLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPv6FilterParamsExtLastChanged.setStatus("current")


class _TIPv6FilterParamsExtAhExtHdr_Type(TItemMatch):
    """Custom type tIPv6FilterParamsExtAhExtHdr based on TItemMatch"""
    defaultValue = 1


_TIPv6FilterParamsExtAhExtHdr_Type.__name__ = "TItemMatch"
_TIPv6FilterParamsExtAhExtHdr_Object = MibTableColumn
tIPv6FilterParamsExtAhExtHdr = _TIPv6FilterParamsExtAhExtHdr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 47, 1, 2),
    _TIPv6FilterParamsExtAhExtHdr_Type()
)
tIPv6FilterParamsExtAhExtHdr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsExtAhExtHdr.setStatus("current")


class _TIPv6FilterParamsExtEspExtHdr_Type(TItemMatch):
    """Custom type tIPv6FilterParamsExtEspExtHdr based on TItemMatch"""
    defaultValue = 1


_TIPv6FilterParamsExtEspExtHdr_Type.__name__ = "TItemMatch"
_TIPv6FilterParamsExtEspExtHdr_Object = MibTableColumn
tIPv6FilterParamsExtEspExtHdr = _TIPv6FilterParamsExtEspExtHdr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 47, 1, 3),
    _TIPv6FilterParamsExtEspExtHdr_Type()
)
tIPv6FilterParamsExtEspExtHdr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsExtEspExtHdr.setStatus("current")


class _TIPv6FilterParamsExtNatType_Type(TmnxNatSubscriberType):
    """Custom type tIPv6FilterParamsExtNatType based on TmnxNatSubscriberType"""
    defaultValue = 3

    subtypeSpec = TmnxNatSubscriberType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("dsliteLsnSub", 3),
          ("nat64LsnSub", 4))
    )


_TIPv6FilterParamsExtNatType_Type.__name__ = "TmnxNatSubscriberType"
_TIPv6FilterParamsExtNatType_Object = MibTableColumn
tIPv6FilterParamsExtNatType = _TIPv6FilterParamsExtNatType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 47, 1, 4),
    _TIPv6FilterParamsExtNatType_Type()
)
tIPv6FilterParamsExtNatType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsExtNatType.setStatus("obsolete")


class _TIPv6FilterParamsExtPktLenVal1_Type(TFilterPacketLength):
    """Custom type tIPv6FilterParamsExtPktLenVal1 based on TFilterPacketLength"""
    defaultValue = 0


_TIPv6FilterParamsExtPktLenVal1_Type.__name__ = "TFilterPacketLength"
_TIPv6FilterParamsExtPktLenVal1_Object = MibTableColumn
tIPv6FilterParamsExtPktLenVal1 = _TIPv6FilterParamsExtPktLenVal1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 47, 1, 5),
    _TIPv6FilterParamsExtPktLenVal1_Type()
)
tIPv6FilterParamsExtPktLenVal1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsExtPktLenVal1.setStatus("obsolete")


class _TIPv6FilterParamsExtPktLenVal2_Type(TFilterPacketLength):
    """Custom type tIPv6FilterParamsExtPktLenVal2 based on TFilterPacketLength"""
    defaultValue = 0


_TIPv6FilterParamsExtPktLenVal2_Type.__name__ = "TFilterPacketLength"
_TIPv6FilterParamsExtPktLenVal2_Object = MibTableColumn
tIPv6FilterParamsExtPktLenVal2 = _TIPv6FilterParamsExtPktLenVal2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 47, 1, 6),
    _TIPv6FilterParamsExtPktLenVal2_Type()
)
tIPv6FilterParamsExtPktLenVal2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsExtPktLenVal2.setStatus("obsolete")


class _TIPv6FilterParamsExtPktLenOper_Type(TOperator):
    """Custom type tIPv6FilterParamsExtPktLenOper based on TOperator"""
    defaultValue = 0


_TIPv6FilterParamsExtPktLenOper_Type.__name__ = "TOperator"
_TIPv6FilterParamsExtPktLenOper_Object = MibTableColumn
tIPv6FilterParamsExtPktLenOper = _TIPv6FilterParamsExtPktLenOper_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 47, 1, 7),
    _TIPv6FilterParamsExtPktLenOper_Type()
)
tIPv6FilterParamsExtPktLenOper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsExtPktLenOper.setStatus("obsolete")


class _TIPv6FilterParamsExtHopLimitVal1_Type(TFilterTTL):
    """Custom type tIPv6FilterParamsExtHopLimitVal1 based on TFilterTTL"""
    defaultValue = 0


_TIPv6FilterParamsExtHopLimitVal1_Type.__name__ = "TFilterTTL"
_TIPv6FilterParamsExtHopLimitVal1_Object = MibTableColumn
tIPv6FilterParamsExtHopLimitVal1 = _TIPv6FilterParamsExtHopLimitVal1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 47, 1, 8),
    _TIPv6FilterParamsExtHopLimitVal1_Type()
)
tIPv6FilterParamsExtHopLimitVal1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsExtHopLimitVal1.setStatus("obsolete")


class _TIPv6FilterParamsExtHopLimitVal2_Type(TFilterTTL):
    """Custom type tIPv6FilterParamsExtHopLimitVal2 based on TFilterTTL"""
    defaultValue = 0


_TIPv6FilterParamsExtHopLimitVal2_Type.__name__ = "TFilterTTL"
_TIPv6FilterParamsExtHopLimitVal2_Object = MibTableColumn
tIPv6FilterParamsExtHopLimitVal2 = _TIPv6FilterParamsExtHopLimitVal2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 47, 1, 9),
    _TIPv6FilterParamsExtHopLimitVal2_Type()
)
tIPv6FilterParamsExtHopLimitVal2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsExtHopLimitVal2.setStatus("obsolete")


class _TIPv6FilterParamsExtHopLimitOper_Type(TOperator):
    """Custom type tIPv6FilterParamsExtHopLimitOper based on TOperator"""
    defaultValue = 0


_TIPv6FilterParamsExtHopLimitOper_Type.__name__ = "TOperator"
_TIPv6FilterParamsExtHopLimitOper_Object = MibTableColumn
tIPv6FilterParamsExtHopLimitOper = _TIPv6FilterParamsExtHopLimitOper_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 47, 1, 10),
    _TIPv6FilterParamsExtHopLimitOper_Type()
)
tIPv6FilterParamsExtHopLimitOper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsExtHopLimitOper.setStatus("obsolete")


class _TIPv6FilterParamsExtEgressPBR_Type(TFilterEgressPBR):
    """Custom type tIPv6FilterParamsExtEgressPBR based on TFilterEgressPBR"""
    defaultValue = 0


_TIPv6FilterParamsExtEgressPBR_Type.__name__ = "TFilterEgressPBR"
_TIPv6FilterParamsExtEgressPBR_Object = MibTableColumn
tIPv6FilterParamsExtEgressPBR = _TIPv6FilterParamsExtEgressPBR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 47, 1, 11),
    _TIPv6FilterParamsExtEgressPBR_Type()
)
tIPv6FilterParamsExtEgressPBR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsExtEgressPBR.setStatus("current")


class _TIPv6FilterParamsExtEsi_Type(TFilterEsi):
    """Custom type tIPv6FilterParamsExtEsi based on TFilterEsi"""
    defaultHexValue = "00000000000000000000"


_TIPv6FilterParamsExtEsi_Type.__name__ = "TFilterEsi"
_TIPv6FilterParamsExtEsi_Object = MibTableColumn
tIPv6FilterParamsExtEsi = _TIPv6FilterParamsExtEsi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 47, 1, 12),
    _TIPv6FilterParamsExtEsi_Type()
)
tIPv6FilterParamsExtEsi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsExtEsi.setStatus("obsolete")


class _TIPv6FilterParamsExtFwdEsiSvcId_Type(TmnxServId):
    """Custom type tIPv6FilterParamsExtFwdEsiSvcId based on TmnxServId"""
    defaultValue = 0


_TIPv6FilterParamsExtFwdEsiSvcId_Type.__name__ = "TmnxServId"
_TIPv6FilterParamsExtFwdEsiSvcId_Object = MibTableColumn
tIPv6FilterParamsExtFwdEsiSvcId = _TIPv6FilterParamsExtFwdEsiSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 47, 1, 13),
    _TIPv6FilterParamsExtFwdEsiSvcId_Type()
)
tIPv6FilterParamsExtFwdEsiSvcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsExtFwdEsiSvcId.setStatus("obsolete")


class _TIPv6FilterParamsExtFwdEsiVRtrId_Type(TmnxVRtrIDOrZero):
    """Custom type tIPv6FilterParamsExtFwdEsiVRtrId based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TIPv6FilterParamsExtFwdEsiVRtrId_Type.__name__ = "TmnxVRtrIDOrZero"
_TIPv6FilterParamsExtFwdEsiVRtrId_Object = MibTableColumn
tIPv6FilterParamsExtFwdEsiVRtrId = _TIPv6FilterParamsExtFwdEsiVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 47, 1, 14),
    _TIPv6FilterParamsExtFwdEsiVRtrId_Type()
)
tIPv6FilterParamsExtFwdEsiVRtrId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsExtFwdEsiVRtrId.setStatus("obsolete")


class _TIPv6FilterParamsExtFwdEsiSFIp_Type(InetAddressIPv6):
    """Custom type tIPv6FilterParamsExtFwdEsiSFIp based on InetAddressIPv6"""
    defaultHexValue = "00000000000000000000000000000000"


_TIPv6FilterParamsExtFwdEsiSFIp_Type.__name__ = "InetAddressIPv6"
_TIPv6FilterParamsExtFwdEsiSFIp_Object = MibTableColumn
tIPv6FilterParamsExtFwdEsiSFIp = _TIPv6FilterParamsExtFwdEsiSFIp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 47, 1, 15),
    _TIPv6FilterParamsExtFwdEsiSFIp_Type()
)
tIPv6FilterParamsExtFwdEsiSFIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsExtFwdEsiSFIp.setStatus("obsolete")


class _TIPv6FilterParamsExtPbrDwnActOvr_Type(TFilterPbrDownActionOvr):
    """Custom type tIPv6FilterParamsExtPbrDwnActOvr based on TFilterPbrDownActionOvr"""
    defaultValue = 0


_TIPv6FilterParamsExtPbrDwnActOvr_Type.__name__ = "TFilterPbrDownActionOvr"
_TIPv6FilterParamsExtPbrDwnActOvr_Object = MibTableColumn
tIPv6FilterParamsExtPbrDwnActOvr = _TIPv6FilterParamsExtPbrDwnActOvr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 47, 1, 16),
    _TIPv6FilterParamsExtPbrDwnActOvr_Type()
)
tIPv6FilterParamsExtPbrDwnActOvr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsExtPbrDwnActOvr.setStatus("current")


class _TIPv6FilterParamsExtFwdEsiVasIf_Type(InterfaceIndexOrZero):
    """Custom type tIPv6FilterParamsExtFwdEsiVasIf based on InterfaceIndexOrZero"""
    defaultValue = 0


_TIPv6FilterParamsExtFwdEsiVasIf_Type.__name__ = "InterfaceIndexOrZero"
_TIPv6FilterParamsExtFwdEsiVasIf_Object = MibTableColumn
tIPv6FilterParamsExtFwdEsiVasIf = _TIPv6FilterParamsExtFwdEsiVasIf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 47, 1, 17),
    _TIPv6FilterParamsExtFwdEsiVasIf_Type()
)
tIPv6FilterParamsExtFwdEsiVasIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsExtFwdEsiVasIf.setStatus("obsolete")


class _TIPv6FilterParamsExtStickyDst_Type(Integer32):
    """Custom type tIPv6FilterParamsExtStickyDst based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )


_TIPv6FilterParamsExtStickyDst_Type.__name__ = "Integer32"
_TIPv6FilterParamsExtStickyDst_Object = MibTableColumn
tIPv6FilterParamsExtStickyDst = _TIPv6FilterParamsExtStickyDst_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 47, 1, 18),
    _TIPv6FilterParamsExtStickyDst_Type()
)
tIPv6FilterParamsExtStickyDst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsExtStickyDst.setStatus("current")
if mibBuilder.loadTexts:
    tIPv6FilterParamsExtStickyDst.setUnits("seconds")


class _TIPv6FilterParamsExtHoldRemain_Type(Integer32):
    """Custom type tIPv6FilterParamsExtHoldRemain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TIPv6FilterParamsExtHoldRemain_Type.__name__ = "Integer32"
_TIPv6FilterParamsExtHoldRemain_Object = MibTableColumn
tIPv6FilterParamsExtHoldRemain = _TIPv6FilterParamsExtHoldRemain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 47, 1, 19),
    _TIPv6FilterParamsExtHoldRemain_Type()
)
tIPv6FilterParamsExtHoldRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPv6FilterParamsExtHoldRemain.setStatus("current")
_TIPv6FilterParamsExtDownloadAct_Type = TFilterDownloadedAction
_TIPv6FilterParamsExtDownloadAct_Object = MibTableColumn
tIPv6FilterParamsExtDownloadAct = _TIPv6FilterParamsExtDownloadAct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 47, 1, 20),
    _TIPv6FilterParamsExtDownloadAct_Type()
)
tIPv6FilterParamsExtDownloadAct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPv6FilterParamsExtDownloadAct.setStatus("current")


class _TIPv6FilterParamsExtTcpFin_Type(TItemMatch):
    """Custom type tIPv6FilterParamsExtTcpFin based on TItemMatch"""
    defaultValue = 1


_TIPv6FilterParamsExtTcpFin_Type.__name__ = "TItemMatch"
_TIPv6FilterParamsExtTcpFin_Object = MibTableColumn
tIPv6FilterParamsExtTcpFin = _TIPv6FilterParamsExtTcpFin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 47, 1, 21),
    _TIPv6FilterParamsExtTcpFin_Type()
)
tIPv6FilterParamsExtTcpFin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsExtTcpFin.setStatus("current")


class _TIPv6FilterParamsExtTcpRst_Type(TItemMatch):
    """Custom type tIPv6FilterParamsExtTcpRst based on TItemMatch"""
    defaultValue = 1


_TIPv6FilterParamsExtTcpRst_Type.__name__ = "TItemMatch"
_TIPv6FilterParamsExtTcpRst_Object = MibTableColumn
tIPv6FilterParamsExtTcpRst = _TIPv6FilterParamsExtTcpRst_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 47, 1, 22),
    _TIPv6FilterParamsExtTcpRst_Type()
)
tIPv6FilterParamsExtTcpRst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsExtTcpRst.setStatus("current")


class _TIPv6FilterParamsExtTcpPsh_Type(TItemMatch):
    """Custom type tIPv6FilterParamsExtTcpPsh based on TItemMatch"""
    defaultValue = 1


_TIPv6FilterParamsExtTcpPsh_Type.__name__ = "TItemMatch"
_TIPv6FilterParamsExtTcpPsh_Object = MibTableColumn
tIPv6FilterParamsExtTcpPsh = _TIPv6FilterParamsExtTcpPsh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 47, 1, 23),
    _TIPv6FilterParamsExtTcpPsh_Type()
)
tIPv6FilterParamsExtTcpPsh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsExtTcpPsh.setStatus("current")


class _TIPv6FilterParamsExtTcpUrg_Type(TItemMatch):
    """Custom type tIPv6FilterParamsExtTcpUrg based on TItemMatch"""
    defaultValue = 1


_TIPv6FilterParamsExtTcpUrg_Type.__name__ = "TItemMatch"
_TIPv6FilterParamsExtTcpUrg_Object = MibTableColumn
tIPv6FilterParamsExtTcpUrg = _TIPv6FilterParamsExtTcpUrg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 47, 1, 24),
    _TIPv6FilterParamsExtTcpUrg_Type()
)
tIPv6FilterParamsExtTcpUrg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsExtTcpUrg.setStatus("current")


class _TIPv6FilterParamsExtTcpEce_Type(TItemMatch):
    """Custom type tIPv6FilterParamsExtTcpEce based on TItemMatch"""
    defaultValue = 1


_TIPv6FilterParamsExtTcpEce_Type.__name__ = "TItemMatch"
_TIPv6FilterParamsExtTcpEce_Object = MibTableColumn
tIPv6FilterParamsExtTcpEce = _TIPv6FilterParamsExtTcpEce_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 47, 1, 25),
    _TIPv6FilterParamsExtTcpEce_Type()
)
tIPv6FilterParamsExtTcpEce.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsExtTcpEce.setStatus("current")


class _TIPv6FilterParamsExtTcpCwr_Type(TItemMatch):
    """Custom type tIPv6FilterParamsExtTcpCwr based on TItemMatch"""
    defaultValue = 1


_TIPv6FilterParamsExtTcpCwr_Type.__name__ = "TItemMatch"
_TIPv6FilterParamsExtTcpCwr_Object = MibTableColumn
tIPv6FilterParamsExtTcpCwr = _TIPv6FilterParamsExtTcpCwr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 47, 1, 26),
    _TIPv6FilterParamsExtTcpCwr_Type()
)
tIPv6FilterParamsExtTcpCwr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsExtTcpCwr.setStatus("current")


class _TIPv6FilterParamsExtTcpNs_Type(TItemMatch):
    """Custom type tIPv6FilterParamsExtTcpNs based on TItemMatch"""
    defaultValue = 1


_TIPv6FilterParamsExtTcpNs_Type.__name__ = "TItemMatch"
_TIPv6FilterParamsExtTcpNs_Object = MibTableColumn
tIPv6FilterParamsExtTcpNs = _TIPv6FilterParamsExtTcpNs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 47, 1, 27),
    _TIPv6FilterParamsExtTcpNs_Type()
)
tIPv6FilterParamsExtTcpNs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsExtTcpNs.setStatus("current")


class _TIPv6FilterParamsExtSrcMac_Type(MacAddress):
    """Custom type tIPv6FilterParamsExtSrcMac based on MacAddress"""
    defaultHexValue = "000000000000"


_TIPv6FilterParamsExtSrcMac_Type.__name__ = "MacAddress"
_TIPv6FilterParamsExtSrcMac_Object = MibTableColumn
tIPv6FilterParamsExtSrcMac = _TIPv6FilterParamsExtSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 47, 1, 28),
    _TIPv6FilterParamsExtSrcMac_Type()
)
tIPv6FilterParamsExtSrcMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsExtSrcMac.setStatus("current")


class _TIPv6FilterParamsExtSrcMacMask_Type(MacAddress):
    """Custom type tIPv6FilterParamsExtSrcMacMask based on MacAddress"""
    defaultHexValue = "000000000000"


_TIPv6FilterParamsExtSrcMacMask_Type.__name__ = "MacAddress"
_TIPv6FilterParamsExtSrcMacMask_Object = MibTableColumn
tIPv6FilterParamsExtSrcMacMask = _TIPv6FilterParamsExtSrcMacMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 47, 1, 29),
    _TIPv6FilterParamsExtSrcMacMask_Type()
)
tIPv6FilterParamsExtSrcMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsExtSrcMacMask.setStatus("current")


class _TIPv6FilterParamsExtMxPktLenVal1_Type(TFilterIpv6MatchPacketLength):
    """Custom type tIPv6FilterParamsExtMxPktLenVal1 based on TFilterIpv6MatchPacketLength"""
    defaultValue = 0


_TIPv6FilterParamsExtMxPktLenVal1_Type.__name__ = "TFilterIpv6MatchPacketLength"
_TIPv6FilterParamsExtMxPktLenVal1_Object = MibTableColumn
tIPv6FilterParamsExtMxPktLenVal1 = _TIPv6FilterParamsExtMxPktLenVal1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 47, 1, 30),
    _TIPv6FilterParamsExtMxPktLenVal1_Type()
)
tIPv6FilterParamsExtMxPktLenVal1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsExtMxPktLenVal1.setStatus("current")


class _TIPv6FilterParamsExtMxPktLenVal2_Type(TFilterIpv6MatchPacketLength):
    """Custom type tIPv6FilterParamsExtMxPktLenVal2 based on TFilterIpv6MatchPacketLength"""
    defaultValue = 0


_TIPv6FilterParamsExtMxPktLenVal2_Type.__name__ = "TFilterIpv6MatchPacketLength"
_TIPv6FilterParamsExtMxPktLenVal2_Object = MibTableColumn
tIPv6FilterParamsExtMxPktLenVal2 = _TIPv6FilterParamsExtMxPktLenVal2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 47, 1, 31),
    _TIPv6FilterParamsExtMxPktLenVal2_Type()
)
tIPv6FilterParamsExtMxPktLenVal2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsExtMxPktLenVal2.setStatus("current")


class _TIPv6FilterParamsExtMxPktLenOper_Type(TOperator):
    """Custom type tIPv6FilterParamsExtMxPktLenOper based on TOperator"""
    defaultValue = 0


_TIPv6FilterParamsExtMxPktLenOper_Type.__name__ = "TOperator"
_TIPv6FilterParamsExtMxPktLenOper_Object = MibTableColumn
tIPv6FilterParamsExtMxPktLenOper = _TIPv6FilterParamsExtMxPktLenOper_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 47, 1, 32),
    _TIPv6FilterParamsExtMxPktLenOper_Type()
)
tIPv6FilterParamsExtMxPktLenOper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsExtMxPktLenOper.setStatus("current")


class _TIPv6FilterParamsExtProtocolList_Type(TNamedItemOrEmpty):
    """Custom type tIPv6FilterParamsExtProtocolList based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TIPv6FilterParamsExtProtocolList_Type.__name__ = "TNamedItemOrEmpty"
_TIPv6FilterParamsExtProtocolList_Object = MibTableColumn
tIPv6FilterParamsExtProtocolList = _TIPv6FilterParamsExtProtocolList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 47, 1, 33),
    _TIPv6FilterParamsExtProtocolList_Type()
)
tIPv6FilterParamsExtProtocolList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsExtProtocolList.setStatus("current")


class _TIPv6FilterParamsExtDestClass_Type(ClassIndexOrNone):
    """Custom type tIPv6FilterParamsExtDestClass based on ClassIndexOrNone"""
    defaultValue = 0


_TIPv6FilterParamsExtDestClass_Type.__name__ = "ClassIndexOrNone"
_TIPv6FilterParamsExtDestClass_Object = MibTableColumn
tIPv6FilterParamsExtDestClass = _TIPv6FilterParamsExtDestClass_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 47, 1, 34),
    _TIPv6FilterParamsExtDestClass_Type()
)
tIPv6FilterParamsExtDestClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsExtDestClass.setStatus("current")


class _TIPv6FilterParamsExtSampleProf_Type(TmnxFilterCflowdSampleProfileId):
    """Custom type tIPv6FilterParamsExtSampleProf based on TmnxFilterCflowdSampleProfileId"""
    defaultValue = 0


_TIPv6FilterParamsExtSampleProf_Type.__name__ = "TmnxFilterCflowdSampleProfileId"
_TIPv6FilterParamsExtSampleProf_Object = MibTableColumn
tIPv6FilterParamsExtSampleProf = _TIPv6FilterParamsExtSampleProf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 47, 1, 35),
    _TIPv6FilterParamsExtSampleProf_Type()
)
tIPv6FilterParamsExtSampleProf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsExtSampleProf.setStatus("current")


class _TIPv6FilterParamsExtCollectStats_Type(TruthValue):
    """Custom type tIPv6FilterParamsExtCollectStats based on TruthValue"""
    defaultValue = 2


_TIPv6FilterParamsExtCollectStats_Type.__name__ = "TruthValue"
_TIPv6FilterParamsExtCollectStats_Object = MibTableColumn
tIPv6FilterParamsExtCollectStats = _TIPv6FilterParamsExtCollectStats_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 47, 1, 36),
    _TIPv6FilterParamsExtCollectStats_Type()
)
tIPv6FilterParamsExtCollectStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsExtCollectStats.setStatus("current")


class _TIPv6FilterParamsExtMxHopLmtVal1_Type(TFilterTTL):
    """Custom type tIPv6FilterParamsExtMxHopLmtVal1 based on TFilterTTL"""
    defaultValue = 0


_TIPv6FilterParamsExtMxHopLmtVal1_Type.__name__ = "TFilterTTL"
_TIPv6FilterParamsExtMxHopLmtVal1_Object = MibTableColumn
tIPv6FilterParamsExtMxHopLmtVal1 = _TIPv6FilterParamsExtMxHopLmtVal1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 47, 1, 37),
    _TIPv6FilterParamsExtMxHopLmtVal1_Type()
)
tIPv6FilterParamsExtMxHopLmtVal1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsExtMxHopLmtVal1.setStatus("current")


class _TIPv6FilterParamsExtMxHopLmtVal2_Type(TFilterTTL):
    """Custom type tIPv6FilterParamsExtMxHopLmtVal2 based on TFilterTTL"""
    defaultValue = 0


_TIPv6FilterParamsExtMxHopLmtVal2_Type.__name__ = "TFilterTTL"
_TIPv6FilterParamsExtMxHopLmtVal2_Object = MibTableColumn
tIPv6FilterParamsExtMxHopLmtVal2 = _TIPv6FilterParamsExtMxHopLmtVal2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 47, 1, 38),
    _TIPv6FilterParamsExtMxHopLmtVal2_Type()
)
tIPv6FilterParamsExtMxHopLmtVal2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsExtMxHopLmtVal2.setStatus("current")


class _TIPv6FilterParamsExtMxHopLmtOper_Type(TOperator):
    """Custom type tIPv6FilterParamsExtMxHopLmtOper based on TOperator"""
    defaultValue = 0


_TIPv6FilterParamsExtMxHopLmtOper_Type.__name__ = "TOperator"
_TIPv6FilterParamsExtMxHopLmtOper_Object = MibTableColumn
tIPv6FilterParamsExtMxHopLmtOper = _TIPv6FilterParamsExtMxHopLmtOper_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 47, 1, 39),
    _TIPv6FilterParamsExtMxHopLmtOper_Type()
)
tIPv6FilterParamsExtMxHopLmtOper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6FilterParamsExtMxHopLmtOper.setStatus("current")
_TFilterEmbedOpenflowTableLstChg_Type = TimeStamp
_TFilterEmbedOpenflowTableLstChg_Object = MibScalar
tFilterEmbedOpenflowTableLstChg = _TFilterEmbedOpenflowTableLstChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 48),
    _TFilterEmbedOpenflowTableLstChg_Type()
)
tFilterEmbedOpenflowTableLstChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterEmbedOpenflowTableLstChg.setStatus("current")
_TFilterEmbedOpenflowTable_Object = MibTable
tFilterEmbedOpenflowTable = _TFilterEmbedOpenflowTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 49)
)
if mibBuilder.loadTexts:
    tFilterEmbedOpenflowTable.setStatus("current")
_TFilterEmbedOpenflowEntry_Object = MibTableRow
tFilterEmbedOpenflowEntry = _TFilterEmbedOpenflowEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 49, 1)
)
tFilterEmbedOpenflowEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tFilterEmbedOpenflowOfsName"),
    (0, "TIMETRA-FILTER-MIB", "tFilterEmbedOpenflowFilterType"),
    (0, "TIMETRA-FILTER-MIB", "tFilterEmbedOpenflowInsertFltrId"),
    (0, "TIMETRA-FILTER-MIB", "tFilterEmbedOpenflowOffset"),
)
if mibBuilder.loadTexts:
    tFilterEmbedOpenflowEntry.setStatus("current")
_TFilterEmbedOpenflowOfsName_Type = TNamedItem
_TFilterEmbedOpenflowOfsName_Object = MibTableColumn
tFilterEmbedOpenflowOfsName = _TFilterEmbedOpenflowOfsName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 49, 1, 1),
    _TFilterEmbedOpenflowOfsName_Type()
)
tFilterEmbedOpenflowOfsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterEmbedOpenflowOfsName.setStatus("current")
_TFilterEmbedOpenflowFilterType_Type = TFilterType
_TFilterEmbedOpenflowFilterType_Object = MibTableColumn
tFilterEmbedOpenflowFilterType = _TFilterEmbedOpenflowFilterType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 49, 1, 2),
    _TFilterEmbedOpenflowFilterType_Type()
)
tFilterEmbedOpenflowFilterType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterEmbedOpenflowFilterType.setStatus("current")
_TFilterEmbedOpenflowInsertFltrId_Type = TConfigOrVsdFilterID
_TFilterEmbedOpenflowInsertFltrId_Object = MibTableColumn
tFilterEmbedOpenflowInsertFltrId = _TFilterEmbedOpenflowInsertFltrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 49, 1, 3),
    _TFilterEmbedOpenflowInsertFltrId_Type()
)
tFilterEmbedOpenflowInsertFltrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterEmbedOpenflowInsertFltrId.setStatus("current")
_TFilterEmbedOpenflowOffset_Type = TFilterEmbedOffset
_TFilterEmbedOpenflowOffset_Object = MibTableColumn
tFilterEmbedOpenflowOffset = _TFilterEmbedOpenflowOffset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 49, 1, 4),
    _TFilterEmbedOpenflowOffset_Type()
)
tFilterEmbedOpenflowOffset.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterEmbedOpenflowOffset.setStatus("current")
_TFilterEmbedOpenflowRowStatus_Type = RowStatus
_TFilterEmbedOpenflowRowStatus_Object = MibTableColumn
tFilterEmbedOpenflowRowStatus = _TFilterEmbedOpenflowRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 49, 1, 5),
    _TFilterEmbedOpenflowRowStatus_Type()
)
tFilterEmbedOpenflowRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterEmbedOpenflowRowStatus.setStatus("current")


class _TFilterEmbedOpenflowAdminState_Type(TmnxEmbeddedFltrAdminState):
    """Custom type tFilterEmbedOpenflowAdminState based on TmnxEmbeddedFltrAdminState"""
    defaultValue = 1


_TFilterEmbedOpenflowAdminState_Type.__name__ = "TmnxEmbeddedFltrAdminState"
_TFilterEmbedOpenflowAdminState_Object = MibTableColumn
tFilterEmbedOpenflowAdminState = _TFilterEmbedOpenflowAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 49, 1, 6),
    _TFilterEmbedOpenflowAdminState_Type()
)
tFilterEmbedOpenflowAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterEmbedOpenflowAdminState.setStatus("current")
_TFilterEmbedOpenflowOperState_Type = TmnxEmbeddedFltrOperState
_TFilterEmbedOpenflowOperState_Object = MibTableColumn
tFilterEmbedOpenflowOperState = _TFilterEmbedOpenflowOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 49, 1, 7),
    _TFilterEmbedOpenflowOperState_Type()
)
tFilterEmbedOpenflowOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterEmbedOpenflowOperState.setStatus("current")


class _TFilterEmbedOflowSvcContext_Type(Unsigned32):
    """Custom type tFilterEmbedOflowSvcContext based on Unsigned32"""
    defaultValue = 0


_TFilterEmbedOflowSvcContext_Type.__name__ = "Unsigned32"
_TFilterEmbedOflowSvcContext_Object = MibTableColumn
tFilterEmbedOflowSvcContext = _TFilterEmbedOflowSvcContext_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 49, 1, 8),
    _TFilterEmbedOflowSvcContext_Type()
)
tFilterEmbedOflowSvcContext.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterEmbedOflowSvcContext.setStatus("current")


class _TFilterEmbedOflowSapContextPort_Type(TmnxPortID):
    """Custom type tFilterEmbedOflowSapContextPort based on TmnxPortID"""
    defaultValue = 0


_TFilterEmbedOflowSapContextPort_Type.__name__ = "TmnxPortID"
_TFilterEmbedOflowSapContextPort_Object = MibTableColumn
tFilterEmbedOflowSapContextPort = _TFilterEmbedOflowSapContextPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 49, 1, 9),
    _TFilterEmbedOflowSapContextPort_Type()
)
tFilterEmbedOflowSapContextPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterEmbedOflowSapContextPort.setStatus("current")


class _TFilterEmbedOflowSapContextEncap_Type(TmnxEncapVal):
    """Custom type tFilterEmbedOflowSapContextEncap based on TmnxEncapVal"""
    defaultValue = 0


_TFilterEmbedOflowSapContextEncap_Type.__name__ = "TmnxEncapVal"
_TFilterEmbedOflowSapContextEncap_Object = MibTableColumn
tFilterEmbedOflowSapContextEncap = _TFilterEmbedOflowSapContextEncap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 49, 1, 10),
    _TFilterEmbedOflowSapContextEncap_Type()
)
tFilterEmbedOflowSapContextEncap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterEmbedOflowSapContextEncap.setStatus("current")


class _TFilterEmbedOflowContextType_Type(Integer32):
    """Custom type tFilterEmbedOflowContextType based on Integer32"""
    defaultValue = 1

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
        *(("grt", 1),
          ("system", 2),
          ("service", 3),
          ("sap", 4))
    )


_TFilterEmbedOflowContextType_Type.__name__ = "Integer32"
_TFilterEmbedOflowContextType_Object = MibTableColumn
tFilterEmbedOflowContextType = _TFilterEmbedOflowContextType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 49, 1, 11),
    _TFilterEmbedOflowContextType_Type()
)
tFilterEmbedOflowContextType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterEmbedOflowContextType.setStatus("current")
_TFilterEmbedOpenflowInfoTable_Object = MibTable
tFilterEmbedOpenflowInfoTable = _TFilterEmbedOpenflowInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 50)
)
if mibBuilder.loadTexts:
    tFilterEmbedOpenflowInfoTable.setStatus("current")
_TFilterEmbedOpenflowInfoEntry_Object = MibTableRow
tFilterEmbedOpenflowInfoEntry = _TFilterEmbedOpenflowInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 50, 1)
)
if mibBuilder.loadTexts:
    tFilterEmbedOpenflowInfoEntry.setStatus("current")
_TFltrEmbedOfInfoEntryCnt_Type = Unsigned32
_TFltrEmbedOfInfoEntryCnt_Object = MibTableColumn
tFltrEmbedOfInfoEntryCnt = _TFltrEmbedOfInfoEntryCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 50, 1, 1),
    _TFltrEmbedOfInfoEntryCnt_Type()
)
tFltrEmbedOfInfoEntryCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrEmbedOfInfoEntryCnt.setStatus("current")
_TFltrEmbedOfInfoEntryCntInsrtd_Type = Unsigned32
_TFltrEmbedOfInfoEntryCntInsrtd_Object = MibTableColumn
tFltrEmbedOfInfoEntryCntInsrtd = _TFltrEmbedOfInfoEntryCntInsrtd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 50, 1, 2),
    _TFltrEmbedOfInfoEntryCntInsrtd_Type()
)
tFltrEmbedOfInfoEntryCntInsrtd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrEmbedOfInfoEntryCntInsrtd.setStatus("current")
_TFilterOpenflowEntryInfoTable_Object = MibTable
tFilterOpenflowEntryInfoTable = _TFilterOpenflowEntryInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 51)
)
if mibBuilder.loadTexts:
    tFilterOpenflowEntryInfoTable.setStatus("current")
_TFilterOpenflowEntryInfoEntry_Object = MibTableRow
tFilterOpenflowEntryInfoEntry = _TFilterOpenflowEntryInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 51, 1)
)
tFilterOpenflowEntryInfoEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tFltrEmbedOfEntryOfsName"),
    (0, "TIMETRA-FILTER-MIB", "tFltrEmbedOfEntryFilterType"),
    (0, "TIMETRA-FILTER-MIB", "tFltrEmbedOfEntryInsertFltrId"),
    (0, "TIMETRA-FILTER-MIB", "tFltrEmbedOfEntryOfEntryId"),
)
if mibBuilder.loadTexts:
    tFilterOpenflowEntryInfoEntry.setStatus("current")
_TFltrEmbedOfEntryOfsName_Type = TNamedItem
_TFltrEmbedOfEntryOfsName_Object = MibTableColumn
tFltrEmbedOfEntryOfsName = _TFltrEmbedOfEntryOfsName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 51, 1, 1),
    _TFltrEmbedOfEntryOfsName_Type()
)
tFltrEmbedOfEntryOfsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFltrEmbedOfEntryOfsName.setStatus("current")
_TFltrEmbedOfEntryFilterType_Type = TFilterType
_TFltrEmbedOfEntryFilterType_Object = MibTableColumn
tFltrEmbedOfEntryFilterType = _TFltrEmbedOfEntryFilterType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 51, 1, 2),
    _TFltrEmbedOfEntryFilterType_Type()
)
tFltrEmbedOfEntryFilterType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFltrEmbedOfEntryFilterType.setStatus("current")
_TFltrEmbedOfEntryInsertFltrId_Type = TConfigOrVsdFilterID
_TFltrEmbedOfEntryInsertFltrId_Object = MibTableColumn
tFltrEmbedOfEntryInsertFltrId = _TFltrEmbedOfEntryInsertFltrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 51, 1, 3),
    _TFltrEmbedOfEntryInsertFltrId_Type()
)
tFltrEmbedOfEntryInsertFltrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFltrEmbedOfEntryInsertFltrId.setStatus("current")
_TFltrEmbedOfEntryOfEntryId_Type = TEntryId
_TFltrEmbedOfEntryOfEntryId_Object = MibTableColumn
tFltrEmbedOfEntryOfEntryId = _TFltrEmbedOfEntryOfEntryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 51, 1, 4),
    _TFltrEmbedOfEntryOfEntryId_Type()
)
tFltrEmbedOfEntryOfEntryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFltrEmbedOfEntryOfEntryId.setStatus("current")
_TFltrEmbedOfEntryInsrtEntryId_Type = TAnyEntryId
_TFltrEmbedOfEntryInsrtEntryId_Object = MibTableColumn
tFltrEmbedOfEntryInsrtEntryId = _TFltrEmbedOfEntryInsrtEntryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 51, 1, 5),
    _TFltrEmbedOfEntryInsrtEntryId_Type()
)
tFltrEmbedOfEntryInsrtEntryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrEmbedOfEntryInsrtEntryId.setStatus("current")
_TFltrEmbedOfEntryInsrtEntryState_Type = TmnxFltrEmbeddedEntryState
_TFltrEmbedOfEntryInsrtEntryState_Object = MibTableColumn
tFltrEmbedOfEntryInsrtEntryState = _TFltrEmbedOfEntryInsrtEntryState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 51, 1, 6),
    _TFltrEmbedOfEntryInsrtEntryState_Type()
)
tFltrEmbedOfEntryInsrtEntryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrEmbedOfEntryInsrtEntryState.setStatus("current")
_TIPFilterParamsExtTbleLstChgd_Type = TimeStamp
_TIPFilterParamsExtTbleLstChgd_Object = MibScalar
tIPFilterParamsExtTbleLstChgd = _TIPFilterParamsExtTbleLstChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 52),
    _TIPFilterParamsExtTbleLstChgd_Type()
)
tIPFilterParamsExtTbleLstChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPFilterParamsExtTbleLstChgd.setStatus("current")
_TIPFilterParamsExtTable_Object = MibTable
tIPFilterParamsExtTable = _TIPFilterParamsExtTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 53)
)
if mibBuilder.loadTexts:
    tIPFilterParamsExtTable.setStatus("current")
_TIPFilterParamsExtEntry_Object = MibTableRow
tIPFilterParamsExtEntry = _TIPFilterParamsExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 53, 1)
)
if mibBuilder.loadTexts:
    tIPFilterParamsExtEntry.setStatus("current")
_TIPFilterParamsExtLastChanged_Type = TimeStamp
_TIPFilterParamsExtLastChanged_Object = MibTableColumn
tIPFilterParamsExtLastChanged = _TIPFilterParamsExtLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 53, 1, 1),
    _TIPFilterParamsExtLastChanged_Type()
)
tIPFilterParamsExtLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPFilterParamsExtLastChanged.setStatus("current")


class _TIPFilterParamsExtPktLenVal1_Type(TFilterPacketLength):
    """Custom type tIPFilterParamsExtPktLenVal1 based on TFilterPacketLength"""
    defaultValue = 0


_TIPFilterParamsExtPktLenVal1_Type.__name__ = "TFilterPacketLength"
_TIPFilterParamsExtPktLenVal1_Object = MibTableColumn
tIPFilterParamsExtPktLenVal1 = _TIPFilterParamsExtPktLenVal1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 53, 1, 2),
    _TIPFilterParamsExtPktLenVal1_Type()
)
tIPFilterParamsExtPktLenVal1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsExtPktLenVal1.setStatus("obsolete")


class _TIPFilterParamsExtPktLenVal2_Type(TFilterPacketLength):
    """Custom type tIPFilterParamsExtPktLenVal2 based on TFilterPacketLength"""
    defaultValue = 0


_TIPFilterParamsExtPktLenVal2_Type.__name__ = "TFilterPacketLength"
_TIPFilterParamsExtPktLenVal2_Object = MibTableColumn
tIPFilterParamsExtPktLenVal2 = _TIPFilterParamsExtPktLenVal2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 53, 1, 3),
    _TIPFilterParamsExtPktLenVal2_Type()
)
tIPFilterParamsExtPktLenVal2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsExtPktLenVal2.setStatus("obsolete")


class _TIPFilterParamsExtPktLenOper_Type(TOperator):
    """Custom type tIPFilterParamsExtPktLenOper based on TOperator"""
    defaultValue = 0


_TIPFilterParamsExtPktLenOper_Type.__name__ = "TOperator"
_TIPFilterParamsExtPktLenOper_Object = MibTableColumn
tIPFilterParamsExtPktLenOper = _TIPFilterParamsExtPktLenOper_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 53, 1, 4),
    _TIPFilterParamsExtPktLenOper_Type()
)
tIPFilterParamsExtPktLenOper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsExtPktLenOper.setStatus("obsolete")


class _TIPFilterParamsExtTTLVal1_Type(TFilterTTL):
    """Custom type tIPFilterParamsExtTTLVal1 based on TFilterTTL"""
    defaultValue = 0


_TIPFilterParamsExtTTLVal1_Type.__name__ = "TFilterTTL"
_TIPFilterParamsExtTTLVal1_Object = MibTableColumn
tIPFilterParamsExtTTLVal1 = _TIPFilterParamsExtTTLVal1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 53, 1, 5),
    _TIPFilterParamsExtTTLVal1_Type()
)
tIPFilterParamsExtTTLVal1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsExtTTLVal1.setStatus("obsolete")


class _TIPFilterParamsExtTTLVal2_Type(TFilterTTL):
    """Custom type tIPFilterParamsExtTTLVal2 based on TFilterTTL"""
    defaultValue = 0


_TIPFilterParamsExtTTLVal2_Type.__name__ = "TFilterTTL"
_TIPFilterParamsExtTTLVal2_Object = MibTableColumn
tIPFilterParamsExtTTLVal2 = _TIPFilterParamsExtTTLVal2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 53, 1, 6),
    _TIPFilterParamsExtTTLVal2_Type()
)
tIPFilterParamsExtTTLVal2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsExtTTLVal2.setStatus("obsolete")


class _TIPFilterParamsExtTTLOper_Type(TOperator):
    """Custom type tIPFilterParamsExtTTLOper based on TOperator"""
    defaultValue = 0


_TIPFilterParamsExtTTLOper_Type.__name__ = "TOperator"
_TIPFilterParamsExtTTLOper_Object = MibTableColumn
tIPFilterParamsExtTTLOper = _TIPFilterParamsExtTTLOper_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 53, 1, 7),
    _TIPFilterParamsExtTTLOper_Type()
)
tIPFilterParamsExtTTLOper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsExtTTLOper.setStatus("obsolete")


class _TIPFilterParamsExtEgressPBR_Type(TFilterEgressPBR):
    """Custom type tIPFilterParamsExtEgressPBR based on TFilterEgressPBR"""
    defaultValue = 0


_TIPFilterParamsExtEgressPBR_Type.__name__ = "TFilterEgressPBR"
_TIPFilterParamsExtEgressPBR_Object = MibTableColumn
tIPFilterParamsExtEgressPBR = _TIPFilterParamsExtEgressPBR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 53, 1, 8),
    _TIPFilterParamsExtEgressPBR_Type()
)
tIPFilterParamsExtEgressPBR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsExtEgressPBR.setStatus("current")


class _TIPFilterParamsExtEsi_Type(TFilterEsi):
    """Custom type tIPFilterParamsExtEsi based on TFilterEsi"""
    defaultHexValue = "00000000000000000000"


_TIPFilterParamsExtEsi_Type.__name__ = "TFilterEsi"
_TIPFilterParamsExtEsi_Object = MibTableColumn
tIPFilterParamsExtEsi = _TIPFilterParamsExtEsi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 53, 1, 9),
    _TIPFilterParamsExtEsi_Type()
)
tIPFilterParamsExtEsi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsExtEsi.setStatus("obsolete")


class _TIPFilterParamsExtFwdEsiSvcId_Type(TmnxServId):
    """Custom type tIPFilterParamsExtFwdEsiSvcId based on TmnxServId"""
    defaultValue = 0


_TIPFilterParamsExtFwdEsiSvcId_Type.__name__ = "TmnxServId"
_TIPFilterParamsExtFwdEsiSvcId_Object = MibTableColumn
tIPFilterParamsExtFwdEsiSvcId = _TIPFilterParamsExtFwdEsiSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 53, 1, 10),
    _TIPFilterParamsExtFwdEsiSvcId_Type()
)
tIPFilterParamsExtFwdEsiSvcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsExtFwdEsiSvcId.setStatus("obsolete")


class _TIPFilterParamsExtFwdEsiVRtrId_Type(TmnxVRtrIDOrZero):
    """Custom type tIPFilterParamsExtFwdEsiVRtrId based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TIPFilterParamsExtFwdEsiVRtrId_Type.__name__ = "TmnxVRtrIDOrZero"
_TIPFilterParamsExtFwdEsiVRtrId_Object = MibTableColumn
tIPFilterParamsExtFwdEsiVRtrId = _TIPFilterParamsExtFwdEsiVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 53, 1, 11),
    _TIPFilterParamsExtFwdEsiVRtrId_Type()
)
tIPFilterParamsExtFwdEsiVRtrId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsExtFwdEsiVRtrId.setStatus("obsolete")


class _TIPFilterParamsExtFwdEsiSFIp_Type(InetAddressIPv4):
    """Custom type tIPFilterParamsExtFwdEsiSFIp based on InetAddressIPv4"""
    defaultHexValue = "00000000"


_TIPFilterParamsExtFwdEsiSFIp_Type.__name__ = "InetAddressIPv4"
_TIPFilterParamsExtFwdEsiSFIp_Object = MibTableColumn
tIPFilterParamsExtFwdEsiSFIp = _TIPFilterParamsExtFwdEsiSFIp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 53, 1, 12),
    _TIPFilterParamsExtFwdEsiSFIp_Type()
)
tIPFilterParamsExtFwdEsiSFIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsExtFwdEsiSFIp.setStatus("obsolete")


class _TIPFilterParamsExtPbrDwnActOvr_Type(TFilterPbrDownActionOvr):
    """Custom type tIPFilterParamsExtPbrDwnActOvr based on TFilterPbrDownActionOvr"""
    defaultValue = 0


_TIPFilterParamsExtPbrDwnActOvr_Type.__name__ = "TFilterPbrDownActionOvr"
_TIPFilterParamsExtPbrDwnActOvr_Object = MibTableColumn
tIPFilterParamsExtPbrDwnActOvr = _TIPFilterParamsExtPbrDwnActOvr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 53, 1, 13),
    _TIPFilterParamsExtPbrDwnActOvr_Type()
)
tIPFilterParamsExtPbrDwnActOvr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsExtPbrDwnActOvr.setStatus("current")


class _TIPFilterParamsExtFwdEsiVasIf_Type(InterfaceIndexOrZero):
    """Custom type tIPFilterParamsExtFwdEsiVasIf based on InterfaceIndexOrZero"""
    defaultValue = 0


_TIPFilterParamsExtFwdEsiVasIf_Type.__name__ = "InterfaceIndexOrZero"
_TIPFilterParamsExtFwdEsiVasIf_Object = MibTableColumn
tIPFilterParamsExtFwdEsiVasIf = _TIPFilterParamsExtFwdEsiVasIf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 53, 1, 14),
    _TIPFilterParamsExtFwdEsiVasIf_Type()
)
tIPFilterParamsExtFwdEsiVasIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsExtFwdEsiVasIf.setStatus("obsolete")


class _TIPFilterParamsExtStickyDst_Type(Integer32):
    """Custom type tIPFilterParamsExtStickyDst based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )


_TIPFilterParamsExtStickyDst_Type.__name__ = "Integer32"
_TIPFilterParamsExtStickyDst_Object = MibTableColumn
tIPFilterParamsExtStickyDst = _TIPFilterParamsExtStickyDst_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 53, 1, 15),
    _TIPFilterParamsExtStickyDst_Type()
)
tIPFilterParamsExtStickyDst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsExtStickyDst.setStatus("current")
if mibBuilder.loadTexts:
    tIPFilterParamsExtStickyDst.setUnits("seconds")


class _TIPFilterParamsExtHoldRemain_Type(Integer32):
    """Custom type tIPFilterParamsExtHoldRemain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TIPFilterParamsExtHoldRemain_Type.__name__ = "Integer32"
_TIPFilterParamsExtHoldRemain_Object = MibTableColumn
tIPFilterParamsExtHoldRemain = _TIPFilterParamsExtHoldRemain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 53, 1, 16),
    _TIPFilterParamsExtHoldRemain_Type()
)
tIPFilterParamsExtHoldRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPFilterParamsExtHoldRemain.setStatus("current")
_TIPFilterParamsExtDownloadAct_Type = TFilterDownloadedAction
_TIPFilterParamsExtDownloadAct_Object = MibTableColumn
tIPFilterParamsExtDownloadAct = _TIPFilterParamsExtDownloadAct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 53, 1, 17),
    _TIPFilterParamsExtDownloadAct_Type()
)
tIPFilterParamsExtDownloadAct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPFilterParamsExtDownloadAct.setStatus("current")


class _TIPFilterParamsExtTcpFin_Type(TItemMatch):
    """Custom type tIPFilterParamsExtTcpFin based on TItemMatch"""
    defaultValue = 1


_TIPFilterParamsExtTcpFin_Type.__name__ = "TItemMatch"
_TIPFilterParamsExtTcpFin_Object = MibTableColumn
tIPFilterParamsExtTcpFin = _TIPFilterParamsExtTcpFin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 53, 1, 18),
    _TIPFilterParamsExtTcpFin_Type()
)
tIPFilterParamsExtTcpFin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsExtTcpFin.setStatus("current")


class _TIPFilterParamsExtTcpRst_Type(TItemMatch):
    """Custom type tIPFilterParamsExtTcpRst based on TItemMatch"""
    defaultValue = 1


_TIPFilterParamsExtTcpRst_Type.__name__ = "TItemMatch"
_TIPFilterParamsExtTcpRst_Object = MibTableColumn
tIPFilterParamsExtTcpRst = _TIPFilterParamsExtTcpRst_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 53, 1, 19),
    _TIPFilterParamsExtTcpRst_Type()
)
tIPFilterParamsExtTcpRst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsExtTcpRst.setStatus("current")


class _TIPFilterParamsExtTcpPsh_Type(TItemMatch):
    """Custom type tIPFilterParamsExtTcpPsh based on TItemMatch"""
    defaultValue = 1


_TIPFilterParamsExtTcpPsh_Type.__name__ = "TItemMatch"
_TIPFilterParamsExtTcpPsh_Object = MibTableColumn
tIPFilterParamsExtTcpPsh = _TIPFilterParamsExtTcpPsh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 53, 1, 20),
    _TIPFilterParamsExtTcpPsh_Type()
)
tIPFilterParamsExtTcpPsh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsExtTcpPsh.setStatus("current")


class _TIPFilterParamsExtTcpUrg_Type(TItemMatch):
    """Custom type tIPFilterParamsExtTcpUrg based on TItemMatch"""
    defaultValue = 1


_TIPFilterParamsExtTcpUrg_Type.__name__ = "TItemMatch"
_TIPFilterParamsExtTcpUrg_Object = MibTableColumn
tIPFilterParamsExtTcpUrg = _TIPFilterParamsExtTcpUrg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 53, 1, 21),
    _TIPFilterParamsExtTcpUrg_Type()
)
tIPFilterParamsExtTcpUrg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsExtTcpUrg.setStatus("current")


class _TIPFilterParamsExtTcpEce_Type(TItemMatch):
    """Custom type tIPFilterParamsExtTcpEce based on TItemMatch"""
    defaultValue = 1


_TIPFilterParamsExtTcpEce_Type.__name__ = "TItemMatch"
_TIPFilterParamsExtTcpEce_Object = MibTableColumn
tIPFilterParamsExtTcpEce = _TIPFilterParamsExtTcpEce_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 53, 1, 22),
    _TIPFilterParamsExtTcpEce_Type()
)
tIPFilterParamsExtTcpEce.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsExtTcpEce.setStatus("current")


class _TIPFilterParamsExtTcpCwr_Type(TItemMatch):
    """Custom type tIPFilterParamsExtTcpCwr based on TItemMatch"""
    defaultValue = 1


_TIPFilterParamsExtTcpCwr_Type.__name__ = "TItemMatch"
_TIPFilterParamsExtTcpCwr_Object = MibTableColumn
tIPFilterParamsExtTcpCwr = _TIPFilterParamsExtTcpCwr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 53, 1, 23),
    _TIPFilterParamsExtTcpCwr_Type()
)
tIPFilterParamsExtTcpCwr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsExtTcpCwr.setStatus("current")


class _TIPFilterParamsExtTcpNs_Type(TItemMatch):
    """Custom type tIPFilterParamsExtTcpNs based on TItemMatch"""
    defaultValue = 1


_TIPFilterParamsExtTcpNs_Type.__name__ = "TItemMatch"
_TIPFilterParamsExtTcpNs_Object = MibTableColumn
tIPFilterParamsExtTcpNs = _TIPFilterParamsExtTcpNs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 53, 1, 24),
    _TIPFilterParamsExtTcpNs_Type()
)
tIPFilterParamsExtTcpNs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsExtTcpNs.setStatus("current")


class _TIPFilterParamsExtSrcMac_Type(MacAddress):
    """Custom type tIPFilterParamsExtSrcMac based on MacAddress"""
    defaultHexValue = "000000000000"


_TIPFilterParamsExtSrcMac_Type.__name__ = "MacAddress"
_TIPFilterParamsExtSrcMac_Object = MibTableColumn
tIPFilterParamsExtSrcMac = _TIPFilterParamsExtSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 53, 1, 25),
    _TIPFilterParamsExtSrcMac_Type()
)
tIPFilterParamsExtSrcMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsExtSrcMac.setStatus("current")


class _TIPFilterParamsExtSrcMacMask_Type(MacAddress):
    """Custom type tIPFilterParamsExtSrcMacMask based on MacAddress"""
    defaultHexValue = "000000000000"


_TIPFilterParamsExtSrcMacMask_Type.__name__ = "MacAddress"
_TIPFilterParamsExtSrcMacMask_Object = MibTableColumn
tIPFilterParamsExtSrcMacMask = _TIPFilterParamsExtSrcMacMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 53, 1, 26),
    _TIPFilterParamsExtSrcMacMask_Type()
)
tIPFilterParamsExtSrcMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsExtSrcMacMask.setStatus("current")


class _TIPFilterParamsExtMxPktLenVal1_Type(TFilterPacketLength):
    """Custom type tIPFilterParamsExtMxPktLenVal1 based on TFilterPacketLength"""
    defaultValue = 0


_TIPFilterParamsExtMxPktLenVal1_Type.__name__ = "TFilterPacketLength"
_TIPFilterParamsExtMxPktLenVal1_Object = MibTableColumn
tIPFilterParamsExtMxPktLenVal1 = _TIPFilterParamsExtMxPktLenVal1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 53, 1, 27),
    _TIPFilterParamsExtMxPktLenVal1_Type()
)
tIPFilterParamsExtMxPktLenVal1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsExtMxPktLenVal1.setStatus("current")


class _TIPFilterParamsExtMxPktLenVal2_Type(TFilterPacketLength):
    """Custom type tIPFilterParamsExtMxPktLenVal2 based on TFilterPacketLength"""
    defaultValue = 0


_TIPFilterParamsExtMxPktLenVal2_Type.__name__ = "TFilterPacketLength"
_TIPFilterParamsExtMxPktLenVal2_Object = MibTableColumn
tIPFilterParamsExtMxPktLenVal2 = _TIPFilterParamsExtMxPktLenVal2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 53, 1, 28),
    _TIPFilterParamsExtMxPktLenVal2_Type()
)
tIPFilterParamsExtMxPktLenVal2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsExtMxPktLenVal2.setStatus("current")


class _TIPFilterParamsExtMxPktLenOper_Type(TOperator):
    """Custom type tIPFilterParamsExtMxPktLenOper based on TOperator"""
    defaultValue = 0


_TIPFilterParamsExtMxPktLenOper_Type.__name__ = "TOperator"
_TIPFilterParamsExtMxPktLenOper_Object = MibTableColumn
tIPFilterParamsExtMxPktLenOper = _TIPFilterParamsExtMxPktLenOper_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 53, 1, 29),
    _TIPFilterParamsExtMxPktLenOper_Type()
)
tIPFilterParamsExtMxPktLenOper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsExtMxPktLenOper.setStatus("current")


class _TIPFilterParamsExtProtocolList_Type(TNamedItemOrEmpty):
    """Custom type tIPFilterParamsExtProtocolList based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TIPFilterParamsExtProtocolList_Type.__name__ = "TNamedItemOrEmpty"
_TIPFilterParamsExtProtocolList_Object = MibTableColumn
tIPFilterParamsExtProtocolList = _TIPFilterParamsExtProtocolList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 53, 1, 30),
    _TIPFilterParamsExtProtocolList_Type()
)
tIPFilterParamsExtProtocolList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsExtProtocolList.setStatus("current")


class _TIPFilterParamsExtDestClass_Type(ClassIndexOrNone):
    """Custom type tIPFilterParamsExtDestClass based on ClassIndexOrNone"""
    defaultValue = 0


_TIPFilterParamsExtDestClass_Type.__name__ = "ClassIndexOrNone"
_TIPFilterParamsExtDestClass_Object = MibTableColumn
tIPFilterParamsExtDestClass = _TIPFilterParamsExtDestClass_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 53, 1, 31),
    _TIPFilterParamsExtDestClass_Type()
)
tIPFilterParamsExtDestClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsExtDestClass.setStatus("current")


class _TIPFilterParamsExtSampleProf_Type(TmnxFilterCflowdSampleProfileId):
    """Custom type tIPFilterParamsExtSampleProf based on TmnxFilterCflowdSampleProfileId"""
    defaultValue = 0


_TIPFilterParamsExtSampleProf_Type.__name__ = "TmnxFilterCflowdSampleProfileId"
_TIPFilterParamsExtSampleProf_Object = MibTableColumn
tIPFilterParamsExtSampleProf = _TIPFilterParamsExtSampleProf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 53, 1, 32),
    _TIPFilterParamsExtSampleProf_Type()
)
tIPFilterParamsExtSampleProf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsExtSampleProf.setStatus("current")


class _TIPFilterParamsExtCollectStats_Type(TruthValue):
    """Custom type tIPFilterParamsExtCollectStats based on TruthValue"""
    defaultValue = 2


_TIPFilterParamsExtCollectStats_Type.__name__ = "TruthValue"
_TIPFilterParamsExtCollectStats_Object = MibTableColumn
tIPFilterParamsExtCollectStats = _TIPFilterParamsExtCollectStats_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 53, 1, 33),
    _TIPFilterParamsExtCollectStats_Type()
)
tIPFilterParamsExtCollectStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsExtCollectStats.setStatus("current")


class _TIPFilterParamsExtMxTTLVal1_Type(TFilterTTL):
    """Custom type tIPFilterParamsExtMxTTLVal1 based on TFilterTTL"""
    defaultValue = 0


_TIPFilterParamsExtMxTTLVal1_Type.__name__ = "TFilterTTL"
_TIPFilterParamsExtMxTTLVal1_Object = MibTableColumn
tIPFilterParamsExtMxTTLVal1 = _TIPFilterParamsExtMxTTLVal1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 53, 1, 34),
    _TIPFilterParamsExtMxTTLVal1_Type()
)
tIPFilterParamsExtMxTTLVal1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsExtMxTTLVal1.setStatus("current")


class _TIPFilterParamsExtMxTTLVal2_Type(TFilterTTL):
    """Custom type tIPFilterParamsExtMxTTLVal2 based on TFilterTTL"""
    defaultValue = 0


_TIPFilterParamsExtMxTTLVal2_Type.__name__ = "TFilterTTL"
_TIPFilterParamsExtMxTTLVal2_Object = MibTableColumn
tIPFilterParamsExtMxTTLVal2 = _TIPFilterParamsExtMxTTLVal2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 53, 1, 35),
    _TIPFilterParamsExtMxTTLVal2_Type()
)
tIPFilterParamsExtMxTTLVal2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsExtMxTTLVal2.setStatus("current")


class _TIPFilterParamsExtMxTTLOper_Type(TOperator):
    """Custom type tIPFilterParamsExtMxTTLOper based on TOperator"""
    defaultValue = 0


_TIPFilterParamsExtMxTTLOper_Type.__name__ = "TOperator"
_TIPFilterParamsExtMxTTLOper_Object = MibTableColumn
tIPFilterParamsExtMxTTLOper = _TIPFilterParamsExtMxTTLOper_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 53, 1, 36),
    _TIPFilterParamsExtMxTTLOper_Type()
)
tIPFilterParamsExtMxTTLOper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPFilterParamsExtMxTTLOper.setStatus("current")
_TFilterRPlcyDstTableLastChg_Type = TimeStamp
_TFilterRPlcyDstTableLastChg_Object = MibScalar
tFilterRPlcyDstTableLastChg = _TFilterRPlcyDstTableLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 54),
    _TFilterRPlcyDstTableLastChg_Type()
)
tFilterRPlcyDstTableLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRPlcyDstTableLastChg.setStatus("current")
_TFilterRPlcyDstTable_Object = MibTable
tFilterRPlcyDstTable = _TFilterRPlcyDstTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 55)
)
if mibBuilder.loadTexts:
    tFilterRPlcyDstTable.setStatus("current")
_TFilterRPlcyDstEntry_Object = MibTableRow
tFilterRPlcyDstEntry = _TFilterRPlcyDstEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 55, 1)
)
tFilterRPlcyDstEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tFilterRedirectPolicy"),
    (0, "TIMETRA-FILTER-MIB", "tFltrRPDstAddrType"),
    (0, "TIMETRA-FILTER-MIB", "tFltrRPDstAddr"),
)
if mibBuilder.loadTexts:
    tFilterRPlcyDstEntry.setStatus("current")
_TFltrRPDstAddrType_Type = InetAddressType
_TFltrRPDstAddrType_Object = MibTableColumn
tFltrRPDstAddrType = _TFltrRPDstAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 55, 1, 1),
    _TFltrRPDstAddrType_Type()
)
tFltrRPDstAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFltrRPDstAddrType.setStatus("current")


class _TFltrRPDstAddr_Type(InetAddress):
    """Custom type tFltrRPDstAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TFltrRPDstAddr_Type.__name__ = "InetAddress"
_TFltrRPDstAddr_Object = MibTableColumn
tFltrRPDstAddr = _TFltrRPDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 55, 1, 2),
    _TFltrRPDstAddr_Type()
)
tFltrRPDstAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFltrRPDstAddr.setStatus("current")
_TFltrRPDstLastChanged_Type = TimeStamp
_TFltrRPDstLastChanged_Object = MibTableColumn
tFltrRPDstLastChanged = _TFltrRPDstLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 55, 1, 3),
    _TFltrRPDstLastChanged_Type()
)
tFltrRPDstLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrRPDstLastChanged.setStatus("current")
_TFltrRPDstRowStatus_Type = RowStatus
_TFltrRPDstRowStatus_Object = MibTableColumn
tFltrRPDstRowStatus = _TFltrRPDstRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 55, 1, 4),
    _TFltrRPDstRowStatus_Type()
)
tFltrRPDstRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFltrRPDstRowStatus.setStatus("current")


class _TFltrRPDstAdminState_Type(TmnxAdminState):
    """Custom type tFltrRPDstAdminState based on TmnxAdminState"""
    defaultValue = 3


_TFltrRPDstAdminState_Type.__name__ = "TmnxAdminState"
_TFltrRPDstAdminState_Object = MibTableColumn
tFltrRPDstAdminState = _TFltrRPDstAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 55, 1, 5),
    _TFltrRPDstAdminState_Type()
)
tFltrRPDstAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFltrRPDstAdminState.setStatus("current")
_TFltrRPDstOperState_Type = TmnxOperState
_TFltrRPDstOperState_Object = MibTableColumn
tFltrRPDstOperState = _TFltrRPDstOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 55, 1, 6),
    _TFltrRPDstOperState_Type()
)
tFltrRPDstOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrRPDstOperState.setStatus("current")


class _TFltrRPDstDescription_Type(TItemDescription):
    """Custom type tFltrRPDstDescription based on TItemDescription"""
    defaultHexValue = ""


_TFltrRPDstDescription_Type.__name__ = "TItemDescription"
_TFltrRPDstDescription_Object = MibTableColumn
tFltrRPDstDescription = _TFltrRPDstDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 55, 1, 7),
    _TFltrRPDstDescription_Type()
)
tFltrRPDstDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFltrRPDstDescription.setStatus("current")


class _TFltrRPDstAdminPriority_Type(Unsigned32):
    """Custom type tFltrRPDstAdminPriority based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TFltrRPDstAdminPriority_Type.__name__ = "Unsigned32"
_TFltrRPDstAdminPriority_Object = MibTableColumn
tFltrRPDstAdminPriority = _TFltrRPDstAdminPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 55, 1, 8),
    _TFltrRPDstAdminPriority_Type()
)
tFltrRPDstAdminPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFltrRPDstAdminPriority.setStatus("current")


class _TFltrRPDstOperPriority_Type(Unsigned32):
    """Custom type tFltrRPDstOperPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TFltrRPDstOperPriority_Type.__name__ = "Unsigned32"
_TFltrRPDstOperPriority_Object = MibTableColumn
tFltrRPDstOperPriority = _TFltrRPDstOperPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 55, 1, 9),
    _TFltrRPDstOperPriority_Type()
)
tFltrRPDstOperPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrRPDstOperPriority.setStatus("current")
_TFilterRPlcySNMPTestTableLastChg_Type = TimeStamp
_TFilterRPlcySNMPTestTableLastChg_Object = MibScalar
tFilterRPlcySNMPTestTableLastChg = _TFilterRPlcySNMPTestTableLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 56),
    _TFilterRPlcySNMPTestTableLastChg_Type()
)
tFilterRPlcySNMPTestTableLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRPlcySNMPTestTableLastChg.setStatus("obsolete")
_TFilterRPlcySNMPTestTable_Object = MibTable
tFilterRPlcySNMPTestTable = _TFilterRPlcySNMPTestTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 57)
)
if mibBuilder.loadTexts:
    tFilterRPlcySNMPTestTable.setStatus("obsolete")
_TFilterRPlcySNMPTestEntry_Object = MibTableRow
tFilterRPlcySNMPTestEntry = _TFilterRPlcySNMPTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 57, 1)
)
tFilterRPlcySNMPTestEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tFilterRedirectPolicy"),
    (0, "TIMETRA-FILTER-MIB", "tFltrRPDstAddrType"),
    (0, "TIMETRA-FILTER-MIB", "tFltrRPDstAddr"),
    (0, "TIMETRA-FILTER-MIB", "tFltrRPSnmpTest"),
)
if mibBuilder.loadTexts:
    tFilterRPlcySNMPTestEntry.setStatus("obsolete")
_TFltrRPSnmpTest_Type = TNamedItem
_TFltrRPSnmpTest_Object = MibTableColumn
tFltrRPSnmpTest = _TFltrRPSnmpTest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 57, 1, 1),
    _TFltrRPSnmpTest_Type()
)
tFltrRPSnmpTest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFltrRPSnmpTest.setStatus("obsolete")
_TFltrRPSnmpTLastChanged_Type = TimeStamp
_TFltrRPSnmpTLastChanged_Object = MibTableColumn
tFltrRPSnmpTLastChanged = _TFltrRPSnmpTLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 57, 1, 2),
    _TFltrRPSnmpTLastChanged_Type()
)
tFltrRPSnmpTLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrRPSnmpTLastChanged.setStatus("obsolete")
_TFltrRPSnmpTRowStatus_Type = RowStatus
_TFltrRPSnmpTRowStatus_Object = MibTableColumn
tFltrRPSnmpTRowStatus = _TFltrRPSnmpTRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 57, 1, 3),
    _TFltrRPSnmpTRowStatus_Type()
)
tFltrRPSnmpTRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFltrRPSnmpTRowStatus.setStatus("obsolete")
_TFltrRPSnmpTOID_Type = ObjectIdentifier
_TFltrRPSnmpTOID_Object = MibTableColumn
tFltrRPSnmpTOID = _TFltrRPSnmpTOID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 57, 1, 4),
    _TFltrRPSnmpTOID_Type()
)
tFltrRPSnmpTOID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFltrRPSnmpTOID.setStatus("obsolete")


class _TFltrRPSnmpTCommunity_Type(DisplayString):
    """Custom type tFltrRPSnmpTCommunity based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TFltrRPSnmpTCommunity_Type.__name__ = "DisplayString"
_TFltrRPSnmpTCommunity_Object = MibTableColumn
tFltrRPSnmpTCommunity = _TFltrRPSnmpTCommunity_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 57, 1, 5),
    _TFltrRPSnmpTCommunity_Type()
)
tFltrRPSnmpTCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFltrRPSnmpTCommunity.setStatus("obsolete")


class _TFltrRPSnmpTSnmpVersion_Type(Integer32):
    """Custom type tFltrRPSnmpTSnmpVersion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("snmpv1", 1),
          ("snmpv2c", 2),
          ("snmpv3", 3))
    )


_TFltrRPSnmpTSnmpVersion_Type.__name__ = "Integer32"
_TFltrRPSnmpTSnmpVersion_Object = MibTableColumn
tFltrRPSnmpTSnmpVersion = _TFltrRPSnmpTSnmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 57, 1, 6),
    _TFltrRPSnmpTSnmpVersion_Type()
)
tFltrRPSnmpTSnmpVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFltrRPSnmpTSnmpVersion.setStatus("obsolete")


class _TFltrRPSnmpTInterval_Type(Unsigned32):
    """Custom type tFltrRPSnmpTInterval based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TFltrRPSnmpTInterval_Type.__name__ = "Unsigned32"
_TFltrRPSnmpTInterval_Object = MibTableColumn
tFltrRPSnmpTInterval = _TFltrRPSnmpTInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 57, 1, 7),
    _TFltrRPSnmpTInterval_Type()
)
tFltrRPSnmpTInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFltrRPSnmpTInterval.setStatus("obsolete")
if mibBuilder.loadTexts:
    tFltrRPSnmpTInterval.setUnits("seconds")


class _TFltrRPSnmpTTimeout_Type(Unsigned32):
    """Custom type tFltrRPSnmpTTimeout based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TFltrRPSnmpTTimeout_Type.__name__ = "Unsigned32"
_TFltrRPSnmpTTimeout_Object = MibTableColumn
tFltrRPSnmpTTimeout = _TFltrRPSnmpTTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 57, 1, 8),
    _TFltrRPSnmpTTimeout_Type()
)
tFltrRPSnmpTTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFltrRPSnmpTTimeout.setStatus("obsolete")
if mibBuilder.loadTexts:
    tFltrRPSnmpTTimeout.setUnits("seconds")


class _TFltrRPSnmpTDropCount_Type(Unsigned32):
    """Custom type tFltrRPSnmpTDropCount based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TFltrRPSnmpTDropCount_Type.__name__ = "Unsigned32"
_TFltrRPSnmpTDropCount_Object = MibTableColumn
tFltrRPSnmpTDropCount = _TFltrRPSnmpTDropCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 57, 1, 9),
    _TFltrRPSnmpTDropCount_Type()
)
tFltrRPSnmpTDropCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFltrRPSnmpTDropCount.setStatus("obsolete")


class _TFltrRPSnmpTHoldDown_Type(Unsigned32):
    """Custom type tFltrRPSnmpTHoldDown based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_TFltrRPSnmpTHoldDown_Type.__name__ = "Unsigned32"
_TFltrRPSnmpTHoldDown_Object = MibTableColumn
tFltrRPSnmpTHoldDown = _TFltrRPSnmpTHoldDown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 57, 1, 10),
    _TFltrRPSnmpTHoldDown_Type()
)
tFltrRPSnmpTHoldDown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFltrRPSnmpTHoldDown.setStatus("obsolete")
if mibBuilder.loadTexts:
    tFltrRPSnmpTHoldDown.setUnits("seconds")


class _TFltrRPSnmpTHoldDownRemain_Type(Unsigned32):
    """Custom type tFltrRPSnmpTHoldDownRemain based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_TFltrRPSnmpTHoldDownRemain_Type.__name__ = "Unsigned32"
_TFltrRPSnmpTHoldDownRemain_Object = MibTableColumn
tFltrRPSnmpTHoldDownRemain = _TFltrRPSnmpTHoldDownRemain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 57, 1, 11),
    _TFltrRPSnmpTHoldDownRemain_Type()
)
tFltrRPSnmpTHoldDownRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrRPSnmpTHoldDownRemain.setStatus("obsolete")
if mibBuilder.loadTexts:
    tFltrRPSnmpTHoldDownRemain.setUnits("seconds")
_TFltrRPSnmpTLastActionTime_Type = TimeStamp
_TFltrRPSnmpTLastActionTime_Object = MibTableColumn
tFltrRPSnmpTLastActionTime = _TFltrRPSnmpTLastActionTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 57, 1, 12),
    _TFltrRPSnmpTLastActionTime_Type()
)
tFltrRPSnmpTLastActionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrRPSnmpTLastActionTime.setStatus("obsolete")
_TFltrRPSnmpTLastOID_Type = ObjectIdentifier
_TFltrRPSnmpTLastOID_Object = MibTableColumn
tFltrRPSnmpTLastOID = _TFltrRPSnmpTLastOID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 57, 1, 13),
    _TFltrRPSnmpTLastOID_Type()
)
tFltrRPSnmpTLastOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrRPSnmpTLastOID.setStatus("obsolete")


class _TFltrRPSnmpTLastType_Type(Integer32):
    """Custom type tFltrRPSnmpTLastType based on Integer32"""
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
          ("counter32", 1),
          ("unsigned32", 2),
          ("timeTicks", 3),
          ("integer32", 4),
          ("ipAddress", 5),
          ("octetString", 6),
          ("objectId", 7),
          ("counter64", 8),
          ("opaque", 9))
    )


_TFltrRPSnmpTLastType_Type.__name__ = "Integer32"
_TFltrRPSnmpTLastType_Object = MibTableColumn
tFltrRPSnmpTLastType = _TFltrRPSnmpTLastType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 57, 1, 14),
    _TFltrRPSnmpTLastType_Type()
)
tFltrRPSnmpTLastType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrRPSnmpTLastType.setStatus("obsolete")
_TFltrRPSnmpTLastCounter32Val_Type = Counter32
_TFltrRPSnmpTLastCounter32Val_Object = MibTableColumn
tFltrRPSnmpTLastCounter32Val = _TFltrRPSnmpTLastCounter32Val_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 57, 1, 15),
    _TFltrRPSnmpTLastCounter32Val_Type()
)
tFltrRPSnmpTLastCounter32Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrRPSnmpTLastCounter32Val.setStatus("obsolete")
_TFltrRPSnmpTLastUnsigned32Val_Type = Unsigned32
_TFltrRPSnmpTLastUnsigned32Val_Object = MibTableColumn
tFltrRPSnmpTLastUnsigned32Val = _TFltrRPSnmpTLastUnsigned32Val_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 57, 1, 16),
    _TFltrRPSnmpTLastUnsigned32Val_Type()
)
tFltrRPSnmpTLastUnsigned32Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrRPSnmpTLastUnsigned32Val.setStatus("obsolete")
_TFltrRPSnmpTLastTimeTicksVal_Type = TimeTicks
_TFltrRPSnmpTLastTimeTicksVal_Object = MibTableColumn
tFltrRPSnmpTLastTimeTicksVal = _TFltrRPSnmpTLastTimeTicksVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 57, 1, 17),
    _TFltrRPSnmpTLastTimeTicksVal_Type()
)
tFltrRPSnmpTLastTimeTicksVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrRPSnmpTLastTimeTicksVal.setStatus("obsolete")
_TFltrRPSnmpTLastInt32Val_Type = Integer32
_TFltrRPSnmpTLastInt32Val_Object = MibTableColumn
tFltrRPSnmpTLastInt32Val = _TFltrRPSnmpTLastInt32Val_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 57, 1, 18),
    _TFltrRPSnmpTLastInt32Val_Type()
)
tFltrRPSnmpTLastInt32Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrRPSnmpTLastInt32Val.setStatus("obsolete")


class _TFltrRPSnmpTLastOctetStringVal_Type(OctetString):
    """Custom type tFltrRPSnmpTLastOctetStringVal based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TFltrRPSnmpTLastOctetStringVal_Type.__name__ = "OctetString"
_TFltrRPSnmpTLastOctetStringVal_Object = MibTableColumn
tFltrRPSnmpTLastOctetStringVal = _TFltrRPSnmpTLastOctetStringVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 57, 1, 19),
    _TFltrRPSnmpTLastOctetStringVal_Type()
)
tFltrRPSnmpTLastOctetStringVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrRPSnmpTLastOctetStringVal.setStatus("obsolete")
_TFltrRPSnmpTLastIpAddressVal_Type = IpAddress
_TFltrRPSnmpTLastIpAddressVal_Object = MibTableColumn
tFltrRPSnmpTLastIpAddressVal = _TFltrRPSnmpTLastIpAddressVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 57, 1, 20),
    _TFltrRPSnmpTLastIpAddressVal_Type()
)
tFltrRPSnmpTLastIpAddressVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrRPSnmpTLastIpAddressVal.setStatus("obsolete")
_TFltrRPSnmpTLastOidVal_Type = ObjectIdentifier
_TFltrRPSnmpTLastOidVal_Object = MibTableColumn
tFltrRPSnmpTLastOidVal = _TFltrRPSnmpTLastOidVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 57, 1, 21),
    _TFltrRPSnmpTLastOidVal_Type()
)
tFltrRPSnmpTLastOidVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrRPSnmpTLastOidVal.setStatus("obsolete")
_TFltrRPSnmpTLastCounter64Val_Type = Counter64
_TFltrRPSnmpTLastCounter64Val_Object = MibTableColumn
tFltrRPSnmpTLastCounter64Val = _TFltrRPSnmpTLastCounter64Val_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 57, 1, 22),
    _TFltrRPSnmpTLastCounter64Val_Type()
)
tFltrRPSnmpTLastCounter64Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrRPSnmpTLastCounter64Val.setStatus("obsolete")


class _TFltrRPSnmpTLastOpaqueVal_Type(Opaque):
    """Custom type tFltrRPSnmpTLastOpaqueVal based on Opaque"""
    subtypeSpec = Opaque.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TFltrRPSnmpTLastOpaqueVal_Type.__name__ = "Opaque"
_TFltrRPSnmpTLastOpaqueVal_Object = MibTableColumn
tFltrRPSnmpTLastOpaqueVal = _TFltrRPSnmpTLastOpaqueVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 57, 1, 23),
    _TFltrRPSnmpTLastOpaqueVal_Type()
)
tFltrRPSnmpTLastOpaqueVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrRPSnmpTLastOpaqueVal.setStatus("obsolete")
_TFltrRPSnmpTLastAction_Type = TmnxFilterRPlcyTestLastAction
_TFltrRPSnmpTLastAction_Object = MibTableColumn
tFltrRPSnmpTLastAction = _TFltrRPSnmpTLastAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 57, 1, 24),
    _TFltrRPSnmpTLastAction_Type()
)
tFltrRPSnmpTLastAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrRPSnmpTLastAction.setStatus("obsolete")


class _TFltrRPSnmpTLastPrioChange_Type(Integer32):
    """Custom type tFltrRPSnmpTLastPrioChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-255, 255),
    )


_TFltrRPSnmpTLastPrioChange_Type.__name__ = "Integer32"
_TFltrRPSnmpTLastPrioChange_Object = MibTableColumn
tFltrRPSnmpTLastPrioChange = _TFltrRPSnmpTLastPrioChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 57, 1, 25),
    _TFltrRPSnmpTLastPrioChange_Type()
)
tFltrRPSnmpTLastPrioChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrRPSnmpTLastPrioChange.setStatus("obsolete")


class _TFltrRPSnmpTNextRespIndex_Type(Integer32):
    """Custom type tFltrRPSnmpTNextRespIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 2147483647),
    )


_TFltrRPSnmpTNextRespIndex_Type.__name__ = "Integer32"
_TFltrRPSnmpTNextRespIndex_Object = MibTableColumn
tFltrRPSnmpTNextRespIndex = _TFltrRPSnmpTNextRespIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 57, 1, 26),
    _TFltrRPSnmpTNextRespIndex_Type()
)
tFltrRPSnmpTNextRespIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrRPSnmpTNextRespIndex.setStatus("obsolete")
_TFilterRPlcySNMPRespTableLastChg_Type = TimeStamp
_TFilterRPlcySNMPRespTableLastChg_Object = MibScalar
tFilterRPlcySNMPRespTableLastChg = _TFilterRPlcySNMPRespTableLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 58),
    _TFilterRPlcySNMPRespTableLastChg_Type()
)
tFilterRPlcySNMPRespTableLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRPlcySNMPRespTableLastChg.setStatus("obsolete")
_TFilterRPlcySNMPRespTable_Object = MibTable
tFilterRPlcySNMPRespTable = _TFilterRPlcySNMPRespTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 59)
)
if mibBuilder.loadTexts:
    tFilterRPlcySNMPRespTable.setStatus("obsolete")
_TFilterRPlcySNMPRespEntry_Object = MibTableRow
tFilterRPlcySNMPRespEntry = _TFilterRPlcySNMPRespEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 59, 1)
)
tFilterRPlcySNMPRespEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tFilterRedirectPolicy"),
    (0, "TIMETRA-FILTER-MIB", "tFltrRPDstAddrType"),
    (0, "TIMETRA-FILTER-MIB", "tFltrRPDstAddr"),
    (0, "TIMETRA-FILTER-MIB", "tFltrRPSnmpTest"),
    (0, "TIMETRA-FILTER-MIB", "tFltrRPSnmpRspId"),
)
if mibBuilder.loadTexts:
    tFilterRPlcySNMPRespEntry.setStatus("obsolete")


class _TFltrRPSnmpRspId_Type(Integer32):
    """Custom type tFltrRPSnmpRspId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TFltrRPSnmpRspId_Type.__name__ = "Integer32"
_TFltrRPSnmpRspId_Object = MibTableColumn
tFltrRPSnmpRspId = _TFltrRPSnmpRspId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 59, 1, 1),
    _TFltrRPSnmpRspId_Type()
)
tFltrRPSnmpRspId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFltrRPSnmpRspId.setStatus("obsolete")
_TFltrRPSnmpRspLastChanged_Type = TimeStamp
_TFltrRPSnmpRspLastChanged_Object = MibTableColumn
tFltrRPSnmpRspLastChanged = _TFltrRPSnmpRspLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 59, 1, 2),
    _TFltrRPSnmpRspLastChanged_Type()
)
tFltrRPSnmpRspLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrRPSnmpRspLastChanged.setStatus("obsolete")
_TFltrRPSnmpRspRowStatus_Type = RowStatus
_TFltrRPSnmpRspRowStatus_Object = MibTableColumn
tFltrRPSnmpRspRowStatus = _TFltrRPSnmpRspRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 59, 1, 3),
    _TFltrRPSnmpRspRowStatus_Type()
)
tFltrRPSnmpRspRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFltrRPSnmpRspRowStatus.setStatus("obsolete")


class _TFltrRPSnmpRspAction_Type(TmnxFilterRPlcyTestRespAction):
    """Custom type tFltrRPSnmpRspAction based on TmnxFilterRPlcyTestRespAction"""
    defaultValue = 3


_TFltrRPSnmpRspAction_Type.__name__ = "TmnxFilterRPlcyTestRespAction"
_TFltrRPSnmpRspAction_Object = MibTableColumn
tFltrRPSnmpRspAction = _TFltrRPSnmpRspAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 59, 1, 4),
    _TFltrRPSnmpRspAction_Type()
)
tFltrRPSnmpRspAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFltrRPSnmpRspAction.setStatus("obsolete")


class _TFltrRPSnmpRspPrioChange_Type(Unsigned32):
    """Custom type tFltrRPSnmpRspPrioChange based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TFltrRPSnmpRspPrioChange_Type.__name__ = "Unsigned32"
_TFltrRPSnmpRspPrioChange_Object = MibTableColumn
tFltrRPSnmpRspPrioChange = _TFltrRPSnmpRspPrioChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 59, 1, 5),
    _TFltrRPSnmpRspPrioChange_Type()
)
tFltrRPSnmpRspPrioChange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFltrRPSnmpRspPrioChange.setStatus("obsolete")
_TFltrRPSnmpRspOID_Type = ObjectIdentifier
_TFltrRPSnmpRspOID_Object = MibTableColumn
tFltrRPSnmpRspOID = _TFltrRPSnmpRspOID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 59, 1, 6),
    _TFltrRPSnmpRspOID_Type()
)
tFltrRPSnmpRspOID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFltrRPSnmpRspOID.setStatus("obsolete")


class _TFltrRPSnmpRspType_Type(Integer32):
    """Custom type tFltrRPSnmpRspType based on Integer32"""
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
        *(("counter32", 1),
          ("unsigned32", 2),
          ("timeTicks", 3),
          ("integer32", 4),
          ("ipAddress", 5),
          ("octetString", 6),
          ("objectId", 7),
          ("counter64", 8),
          ("opaque", 9))
    )


_TFltrRPSnmpRspType_Type.__name__ = "Integer32"
_TFltrRPSnmpRspType_Object = MibTableColumn
tFltrRPSnmpRspType = _TFltrRPSnmpRspType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 59, 1, 7),
    _TFltrRPSnmpRspType_Type()
)
tFltrRPSnmpRspType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFltrRPSnmpRspType.setStatus("obsolete")
_TFltrRPSnmpRspCounter32Val_Type = Unsigned32
_TFltrRPSnmpRspCounter32Val_Object = MibTableColumn
tFltrRPSnmpRspCounter32Val = _TFltrRPSnmpRspCounter32Val_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 59, 1, 8),
    _TFltrRPSnmpRspCounter32Val_Type()
)
tFltrRPSnmpRspCounter32Val.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFltrRPSnmpRspCounter32Val.setStatus("obsolete")
_TFltrRPSnmpRspUnsigned32Val_Type = Unsigned32
_TFltrRPSnmpRspUnsigned32Val_Object = MibTableColumn
tFltrRPSnmpRspUnsigned32Val = _TFltrRPSnmpRspUnsigned32Val_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 59, 1, 9),
    _TFltrRPSnmpRspUnsigned32Val_Type()
)
tFltrRPSnmpRspUnsigned32Val.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFltrRPSnmpRspUnsigned32Val.setStatus("obsolete")
_TFltrRPSnmpRspTimeTicksVal_Type = Unsigned32
_TFltrRPSnmpRspTimeTicksVal_Object = MibTableColumn
tFltrRPSnmpRspTimeTicksVal = _TFltrRPSnmpRspTimeTicksVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 59, 1, 10),
    _TFltrRPSnmpRspTimeTicksVal_Type()
)
tFltrRPSnmpRspTimeTicksVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFltrRPSnmpRspTimeTicksVal.setStatus("obsolete")
_TFltrRPSnmpRspInt32Val_Type = Integer32
_TFltrRPSnmpRspInt32Val_Object = MibTableColumn
tFltrRPSnmpRspInt32Val = _TFltrRPSnmpRspInt32Val_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 59, 1, 11),
    _TFltrRPSnmpRspInt32Val_Type()
)
tFltrRPSnmpRspInt32Val.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFltrRPSnmpRspInt32Val.setStatus("obsolete")


class _TFltrRPSnmpRspOctetStringVal_Type(OctetString):
    """Custom type tFltrRPSnmpRspOctetStringVal based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TFltrRPSnmpRspOctetStringVal_Type.__name__ = "OctetString"
_TFltrRPSnmpRspOctetStringVal_Object = MibTableColumn
tFltrRPSnmpRspOctetStringVal = _TFltrRPSnmpRspOctetStringVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 59, 1, 12),
    _TFltrRPSnmpRspOctetStringVal_Type()
)
tFltrRPSnmpRspOctetStringVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFltrRPSnmpRspOctetStringVal.setStatus("obsolete")
_TFltrRPSnmpRspIpAddressVal_Type = IpAddress
_TFltrRPSnmpRspIpAddressVal_Object = MibTableColumn
tFltrRPSnmpRspIpAddressVal = _TFltrRPSnmpRspIpAddressVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 59, 1, 13),
    _TFltrRPSnmpRspIpAddressVal_Type()
)
tFltrRPSnmpRspIpAddressVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFltrRPSnmpRspIpAddressVal.setStatus("obsolete")
_TFltrRPSnmpRspOidVal_Type = ObjectIdentifier
_TFltrRPSnmpRspOidVal_Object = MibTableColumn
tFltrRPSnmpRspOidVal = _TFltrRPSnmpRspOidVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 59, 1, 14),
    _TFltrRPSnmpRspOidVal_Type()
)
tFltrRPSnmpRspOidVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFltrRPSnmpRspOidVal.setStatus("obsolete")
_TFltrRPSnmpRspCounter64Val_Type = Counter64
_TFltrRPSnmpRspCounter64Val_Object = MibTableColumn
tFltrRPSnmpRspCounter64Val = _TFltrRPSnmpRspCounter64Val_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 59, 1, 15),
    _TFltrRPSnmpRspCounter64Val_Type()
)
tFltrRPSnmpRspCounter64Val.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFltrRPSnmpRspCounter64Val.setStatus("obsolete")


class _TFltrRPSnmpRspOpaqueVal_Type(Opaque):
    """Custom type tFltrRPSnmpRspOpaqueVal based on Opaque"""
    subtypeSpec = Opaque.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TFltrRPSnmpRspOpaqueVal_Type.__name__ = "Opaque"
_TFltrRPSnmpRspOpaqueVal_Object = MibTableColumn
tFltrRPSnmpRspOpaqueVal = _TFltrRPSnmpRspOpaqueVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 59, 1, 16),
    _TFltrRPSnmpRspOpaqueVal_Type()
)
tFltrRPSnmpRspOpaqueVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFltrRPSnmpRspOpaqueVal.setStatus("obsolete")
_TFilterRPlcyURLTestTableLastChg_Type = TimeStamp
_TFilterRPlcyURLTestTableLastChg_Object = MibScalar
tFilterRPlcyURLTestTableLastChg = _TFilterRPlcyURLTestTableLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 60),
    _TFilterRPlcyURLTestTableLastChg_Type()
)
tFilterRPlcyURLTestTableLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRPlcyURLTestTableLastChg.setStatus("obsolete")
_TFilterRPlcyURLTestTable_Object = MibTable
tFilterRPlcyURLTestTable = _TFilterRPlcyURLTestTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 61)
)
if mibBuilder.loadTexts:
    tFilterRPlcyURLTestTable.setStatus("obsolete")
_TFilterRPlcyURLTestEntry_Object = MibTableRow
tFilterRPlcyURLTestEntry = _TFilterRPlcyURLTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 61, 1)
)
tFilterRPlcyURLTestEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tFilterRedirectPolicy"),
    (0, "TIMETRA-FILTER-MIB", "tFltrRPDstAddrType"),
    (0, "TIMETRA-FILTER-MIB", "tFltrRPDstAddr"),
    (0, "TIMETRA-FILTER-MIB", "tFltrRPUrlTest"),
)
if mibBuilder.loadTexts:
    tFilterRPlcyURLTestEntry.setStatus("obsolete")
_TFltrRPUrlTest_Type = TNamedItem
_TFltrRPUrlTest_Object = MibTableColumn
tFltrRPUrlTest = _TFltrRPUrlTest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 61, 1, 1),
    _TFltrRPUrlTest_Type()
)
tFltrRPUrlTest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFltrRPUrlTest.setStatus("obsolete")
_TFltrRPUrlTLastChanged_Type = TimeStamp
_TFltrRPUrlTLastChanged_Object = MibTableColumn
tFltrRPUrlTLastChanged = _TFltrRPUrlTLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 61, 1, 2),
    _TFltrRPUrlTLastChanged_Type()
)
tFltrRPUrlTLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrRPUrlTLastChanged.setStatus("obsolete")
_TFltrRPUrlTRowStatus_Type = RowStatus
_TFltrRPUrlTRowStatus_Object = MibTableColumn
tFltrRPUrlTRowStatus = _TFltrRPUrlTRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 61, 1, 3),
    _TFltrRPUrlTRowStatus_Type()
)
tFltrRPUrlTRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFltrRPUrlTRowStatus.setStatus("obsolete")


class _TFltrRPUrlTUrl_Type(DisplayString):
    """Custom type tFltrRPUrlTUrl based on DisplayString"""
    defaultHexValue = ""


_TFltrRPUrlTUrl_Type.__name__ = "DisplayString"
_TFltrRPUrlTUrl_Object = MibTableColumn
tFltrRPUrlTUrl = _TFltrRPUrlTUrl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 61, 1, 4),
    _TFltrRPUrlTUrl_Type()
)
tFltrRPUrlTUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFltrRPUrlTUrl.setStatus("obsolete")


class _TFltrRPUrlTHttpVersion_Type(DisplayString):
    """Custom type tFltrRPUrlTHttpVersion based on DisplayString"""
    defaultValue = OctetString("1.1")


_TFltrRPUrlTHttpVersion_Type.__name__ = "DisplayString"
_TFltrRPUrlTHttpVersion_Object = MibTableColumn
tFltrRPUrlTHttpVersion = _TFltrRPUrlTHttpVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 61, 1, 5),
    _TFltrRPUrlTHttpVersion_Type()
)
tFltrRPUrlTHttpVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFltrRPUrlTHttpVersion.setStatus("obsolete")


class _TFltrRPUrlTInterval_Type(Unsigned32):
    """Custom type tFltrRPUrlTInterval based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TFltrRPUrlTInterval_Type.__name__ = "Unsigned32"
_TFltrRPUrlTInterval_Object = MibTableColumn
tFltrRPUrlTInterval = _TFltrRPUrlTInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 61, 1, 6),
    _TFltrRPUrlTInterval_Type()
)
tFltrRPUrlTInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFltrRPUrlTInterval.setStatus("obsolete")
if mibBuilder.loadTexts:
    tFltrRPUrlTInterval.setUnits("seconds")


class _TFltrRPUrlTTimeout_Type(Unsigned32):
    """Custom type tFltrRPUrlTTimeout based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TFltrRPUrlTTimeout_Type.__name__ = "Unsigned32"
_TFltrRPUrlTTimeout_Object = MibTableColumn
tFltrRPUrlTTimeout = _TFltrRPUrlTTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 61, 1, 7),
    _TFltrRPUrlTTimeout_Type()
)
tFltrRPUrlTTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFltrRPUrlTTimeout.setStatus("obsolete")
if mibBuilder.loadTexts:
    tFltrRPUrlTTimeout.setUnits("seconds")


class _TFltrRPUrlTDropCount_Type(Unsigned32):
    """Custom type tFltrRPUrlTDropCount based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TFltrRPUrlTDropCount_Type.__name__ = "Unsigned32"
_TFltrRPUrlTDropCount_Object = MibTableColumn
tFltrRPUrlTDropCount = _TFltrRPUrlTDropCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 61, 1, 8),
    _TFltrRPUrlTDropCount_Type()
)
tFltrRPUrlTDropCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFltrRPUrlTDropCount.setStatus("obsolete")


class _TFltrRPUrlTHoldDown_Type(Unsigned32):
    """Custom type tFltrRPUrlTHoldDown based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_TFltrRPUrlTHoldDown_Type.__name__ = "Unsigned32"
_TFltrRPUrlTHoldDown_Object = MibTableColumn
tFltrRPUrlTHoldDown = _TFltrRPUrlTHoldDown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 61, 1, 9),
    _TFltrRPUrlTHoldDown_Type()
)
tFltrRPUrlTHoldDown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFltrRPUrlTHoldDown.setStatus("obsolete")
if mibBuilder.loadTexts:
    tFltrRPUrlTHoldDown.setUnits("seconds")


class _TFltrRPUrlTHoldDownRemain_Type(Unsigned32):
    """Custom type tFltrRPUrlTHoldDownRemain based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_TFltrRPUrlTHoldDownRemain_Type.__name__ = "Unsigned32"
_TFltrRPUrlTHoldDownRemain_Object = MibTableColumn
tFltrRPUrlTHoldDownRemain = _TFltrRPUrlTHoldDownRemain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 61, 1, 10),
    _TFltrRPUrlTHoldDownRemain_Type()
)
tFltrRPUrlTHoldDownRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrRPUrlTHoldDownRemain.setStatus("obsolete")
if mibBuilder.loadTexts:
    tFltrRPUrlTHoldDownRemain.setUnits("seconds")
_TFltrRPUrlTLastActionTime_Type = TimeStamp
_TFltrRPUrlTLastActionTime_Object = MibTableColumn
tFltrRPUrlTLastActionTime = _TFltrRPUrlTLastActionTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 61, 1, 11),
    _TFltrRPUrlTLastActionTime_Type()
)
tFltrRPUrlTLastActionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrRPUrlTLastActionTime.setStatus("obsolete")
_TFltrRPUrlTLastRetCode_Type = Unsigned32
_TFltrRPUrlTLastRetCode_Object = MibTableColumn
tFltrRPUrlTLastRetCode = _TFltrRPUrlTLastRetCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 61, 1, 12),
    _TFltrRPUrlTLastRetCode_Type()
)
tFltrRPUrlTLastRetCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrRPUrlTLastRetCode.setStatus("obsolete")
_TFltrRPUrlTLastAction_Type = TmnxFilterRPlcyTestLastAction
_TFltrRPUrlTLastAction_Object = MibTableColumn
tFltrRPUrlTLastAction = _TFltrRPUrlTLastAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 61, 1, 13),
    _TFltrRPUrlTLastAction_Type()
)
tFltrRPUrlTLastAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrRPUrlTLastAction.setStatus("obsolete")


class _TFltrRPUrlTLastPrioChange_Type(Integer32):
    """Custom type tFltrRPUrlTLastPrioChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-255, 255),
    )


_TFltrRPUrlTLastPrioChange_Type.__name__ = "Integer32"
_TFltrRPUrlTLastPrioChange_Object = MibTableColumn
tFltrRPUrlTLastPrioChange = _TFltrRPUrlTLastPrioChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 61, 1, 14),
    _TFltrRPUrlTLastPrioChange_Type()
)
tFltrRPUrlTLastPrioChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrRPUrlTLastPrioChange.setStatus("obsolete")
_TFilterRPlcyURLRespTableLastChg_Type = TimeStamp
_TFilterRPlcyURLRespTableLastChg_Object = MibScalar
tFilterRPlcyURLRespTableLastChg = _TFilterRPlcyURLRespTableLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 62),
    _TFilterRPlcyURLRespTableLastChg_Type()
)
tFilterRPlcyURLRespTableLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRPlcyURLRespTableLastChg.setStatus("obsolete")
_TFilterRPlcyURLRespTable_Object = MibTable
tFilterRPlcyURLRespTable = _TFilterRPlcyURLRespTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 63)
)
if mibBuilder.loadTexts:
    tFilterRPlcyURLRespTable.setStatus("obsolete")
_TFilterRPlcyURLRespEntry_Object = MibTableRow
tFilterRPlcyURLRespEntry = _TFilterRPlcyURLRespEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 63, 1)
)
tFilterRPlcyURLRespEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tFilterRedirectPolicy"),
    (0, "TIMETRA-FILTER-MIB", "tFltrRPDstAddrType"),
    (0, "TIMETRA-FILTER-MIB", "tFltrRPDstAddr"),
    (0, "TIMETRA-FILTER-MIB", "tFltrRPUrlTest"),
    (0, "TIMETRA-FILTER-MIB", "tFltrRPUrlTRspLowRspCode"),
    (0, "TIMETRA-FILTER-MIB", "tFltrRPUrlTRspHighRspCode"),
)
if mibBuilder.loadTexts:
    tFilterRPlcyURLRespEntry.setStatus("obsolete")
_TFltrRPUrlTRspLowRspCode_Type = Unsigned32
_TFltrRPUrlTRspLowRspCode_Object = MibTableColumn
tFltrRPUrlTRspLowRspCode = _TFltrRPUrlTRspLowRspCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 63, 1, 1),
    _TFltrRPUrlTRspLowRspCode_Type()
)
tFltrRPUrlTRspLowRspCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFltrRPUrlTRspLowRspCode.setStatus("obsolete")
_TFltrRPUrlTRspHighRspCode_Type = Unsigned32
_TFltrRPUrlTRspHighRspCode_Object = MibTableColumn
tFltrRPUrlTRspHighRspCode = _TFltrRPUrlTRspHighRspCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 63, 1, 2),
    _TFltrRPUrlTRspHighRspCode_Type()
)
tFltrRPUrlTRspHighRspCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFltrRPUrlTRspHighRspCode.setStatus("obsolete")
_TFltrRPUrlTRspLastChanged_Type = TimeStamp
_TFltrRPUrlTRspLastChanged_Object = MibTableColumn
tFltrRPUrlTRspLastChanged = _TFltrRPUrlTRspLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 63, 1, 3),
    _TFltrRPUrlTRspLastChanged_Type()
)
tFltrRPUrlTRspLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrRPUrlTRspLastChanged.setStatus("obsolete")
_TFltrRPUrlTRspRowStatus_Type = RowStatus
_TFltrRPUrlTRspRowStatus_Object = MibTableColumn
tFltrRPUrlTRspRowStatus = _TFltrRPUrlTRspRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 63, 1, 4),
    _TFltrRPUrlTRspRowStatus_Type()
)
tFltrRPUrlTRspRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFltrRPUrlTRspRowStatus.setStatus("obsolete")


class _TFltrRPUrlTRspAction_Type(TmnxFilterRPlcyTestRespAction):
    """Custom type tFltrRPUrlTRspAction based on TmnxFilterRPlcyTestRespAction"""
    defaultValue = 3


_TFltrRPUrlTRspAction_Type.__name__ = "TmnxFilterRPlcyTestRespAction"
_TFltrRPUrlTRspAction_Object = MibTableColumn
tFltrRPUrlTRspAction = _TFltrRPUrlTRspAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 63, 1, 5),
    _TFltrRPUrlTRspAction_Type()
)
tFltrRPUrlTRspAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFltrRPUrlTRspAction.setStatus("obsolete")


class _TFltrRPUrlTRspPrioChange_Type(Unsigned32):
    """Custom type tFltrRPUrlTRspPrioChange based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TFltrRPUrlTRspPrioChange_Type.__name__ = "Unsigned32"
_TFltrRPUrlTRspPrioChange_Object = MibTableColumn
tFltrRPUrlTRspPrioChange = _TFltrRPUrlTRspPrioChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 63, 1, 6),
    _TFltrRPUrlTRspPrioChange_Type()
)
tFltrRPUrlTRspPrioChange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFltrRPUrlTRspPrioChange.setStatus("obsolete")
_TFilterRPlcyPingTestTableLastChg_Type = TimeStamp
_TFilterRPlcyPingTestTableLastChg_Object = MibScalar
tFilterRPlcyPingTestTableLastChg = _TFilterRPlcyPingTestTableLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 64),
    _TFilterRPlcyPingTestTableLastChg_Type()
)
tFilterRPlcyPingTestTableLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRPlcyPingTestTableLastChg.setStatus("current")
_TFilterRPlcyPingTestTable_Object = MibTable
tFilterRPlcyPingTestTable = _TFilterRPlcyPingTestTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 65)
)
if mibBuilder.loadTexts:
    tFilterRPlcyPingTestTable.setStatus("current")
_TFilterRPlcyPingTestEntry_Object = MibTableRow
tFilterRPlcyPingTestEntry = _TFilterRPlcyPingTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 65, 1)
)
tFilterRPlcyPingTestEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tFilterRedirectPolicy"),
    (0, "TIMETRA-FILTER-MIB", "tFltrRPDstAddrType"),
    (0, "TIMETRA-FILTER-MIB", "tFltrRPDstAddr"),
)
if mibBuilder.loadTexts:
    tFilterRPlcyPingTestEntry.setStatus("current")
_TFltrRPPingTLastChanged_Type = TimeStamp
_TFltrRPPingTLastChanged_Object = MibTableColumn
tFltrRPPingTLastChanged = _TFltrRPPingTLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 65, 1, 1),
    _TFltrRPPingTLastChanged_Type()
)
tFltrRPPingTLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrRPPingTLastChanged.setStatus("current")
_TFltrRPPingTRowStatus_Type = RowStatus
_TFltrRPPingTRowStatus_Object = MibTableColumn
tFltrRPPingTRowStatus = _TFltrRPPingTRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 65, 1, 2),
    _TFltrRPPingTRowStatus_Type()
)
tFltrRPPingTRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFltrRPPingTRowStatus.setStatus("current")


class _TFltrRPPingTInterval_Type(Unsigned32):
    """Custom type tFltrRPPingTInterval based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TFltrRPPingTInterval_Type.__name__ = "Unsigned32"
_TFltrRPPingTInterval_Object = MibTableColumn
tFltrRPPingTInterval = _TFltrRPPingTInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 65, 1, 3),
    _TFltrRPPingTInterval_Type()
)
tFltrRPPingTInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFltrRPPingTInterval.setStatus("current")
if mibBuilder.loadTexts:
    tFltrRPPingTInterval.setUnits("seconds")


class _TFltrRPPingTTimeout_Type(Unsigned32):
    """Custom type tFltrRPPingTTimeout based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TFltrRPPingTTimeout_Type.__name__ = "Unsigned32"
_TFltrRPPingTTimeout_Object = MibTableColumn
tFltrRPPingTTimeout = _TFltrRPPingTTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 65, 1, 4),
    _TFltrRPPingTTimeout_Type()
)
tFltrRPPingTTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFltrRPPingTTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tFltrRPPingTTimeout.setUnits("seconds")


class _TFltrRPPingTDropCount_Type(Unsigned32):
    """Custom type tFltrRPPingTDropCount based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TFltrRPPingTDropCount_Type.__name__ = "Unsigned32"
_TFltrRPPingTDropCount_Object = MibTableColumn
tFltrRPPingTDropCount = _TFltrRPPingTDropCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 65, 1, 5),
    _TFltrRPPingTDropCount_Type()
)
tFltrRPPingTDropCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFltrRPPingTDropCount.setStatus("current")


class _TFltrRPPingTHoldDown_Type(Unsigned32):
    """Custom type tFltrRPPingTHoldDown based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_TFltrRPPingTHoldDown_Type.__name__ = "Unsigned32"
_TFltrRPPingTHoldDown_Object = MibTableColumn
tFltrRPPingTHoldDown = _TFltrRPPingTHoldDown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 65, 1, 6),
    _TFltrRPPingTHoldDown_Type()
)
tFltrRPPingTHoldDown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFltrRPPingTHoldDown.setStatus("current")
if mibBuilder.loadTexts:
    tFltrRPPingTHoldDown.setUnits("seconds")


class _TFltrRPPingTHoldDownRemain_Type(Unsigned32):
    """Custom type tFltrRPPingTHoldDownRemain based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_TFltrRPPingTHoldDownRemain_Type.__name__ = "Unsigned32"
_TFltrRPPingTHoldDownRemain_Object = MibTableColumn
tFltrRPPingTHoldDownRemain = _TFltrRPPingTHoldDownRemain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 65, 1, 7),
    _TFltrRPPingTHoldDownRemain_Type()
)
tFltrRPPingTHoldDownRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrRPPingTHoldDownRemain.setStatus("current")
if mibBuilder.loadTexts:
    tFltrRPPingTHoldDownRemain.setUnits("seconds")
_TFltrRPPingTLastActionTime_Type = TimeStamp
_TFltrRPPingTLastActionTime_Object = MibTableColumn
tFltrRPPingTLastActionTime = _TFltrRPPingTLastActionTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 65, 1, 8),
    _TFltrRPPingTLastActionTime_Type()
)
tFltrRPPingTLastActionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrRPPingTLastActionTime.setStatus("current")
_TFltrRPPingTLastAction_Type = TmnxFilterRPlcyTestLastAction
_TFltrRPPingTLastAction_Object = MibTableColumn
tFltrRPPingTLastAction = _TFltrRPPingTLastAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 65, 1, 9),
    _TFltrRPPingTLastAction_Type()
)
tFltrRPPingTLastAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrRPPingTLastAction.setStatus("current")


class _TFilterRPPingSrcAddressAddrType_Type(InetAddressType):
    """Custom type tFilterRPPingSrcAddressAddrType based on InetAddressType"""
    defaultValue = 0


_TFilterRPPingSrcAddressAddrType_Type.__name__ = "InetAddressType"
_TFilterRPPingSrcAddressAddrType_Object = MibTableColumn
tFilterRPPingSrcAddressAddrType = _TFilterRPPingSrcAddressAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 65, 1, 10),
    _TFilterRPPingSrcAddressAddrType_Type()
)
tFilterRPPingSrcAddressAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRPPingSrcAddressAddrType.setStatus("current")


class _TFilterRPPingSrcAddressAddr_Type(InetAddress):
    """Custom type tFilterRPPingSrcAddressAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TFilterRPPingSrcAddressAddr_Type.__name__ = "InetAddress"
_TFilterRPPingSrcAddressAddr_Object = MibTableColumn
tFilterRPPingSrcAddressAddr = _TFilterRPPingSrcAddressAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 65, 1, 11),
    _TFilterRPPingSrcAddressAddr_Type()
)
tFilterRPPingSrcAddressAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRPPingSrcAddressAddr.setStatus("current")
_TFilterRPlcyUcastRtTTableLastChg_Type = TimeStamp
_TFilterRPlcyUcastRtTTableLastChg_Object = MibScalar
tFilterRPlcyUcastRtTTableLastChg = _TFilterRPlcyUcastRtTTableLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 66),
    _TFilterRPlcyUcastRtTTableLastChg_Type()
)
tFilterRPlcyUcastRtTTableLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRPlcyUcastRtTTableLastChg.setStatus("current")
_TFilterRPlcyUnicastRtTestTable_Object = MibTable
tFilterRPlcyUnicastRtTestTable = _TFilterRPlcyUnicastRtTestTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 67)
)
if mibBuilder.loadTexts:
    tFilterRPlcyUnicastRtTestTable.setStatus("current")
_TFilterRPlcyUnicastRtTestEntry_Object = MibTableRow
tFilterRPlcyUnicastRtTestEntry = _TFilterRPlcyUnicastRtTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 67, 1)
)
tFilterRPlcyUnicastRtTestEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tFilterRedirectPolicy"),
    (0, "TIMETRA-FILTER-MIB", "tFltrRPDstAddrType"),
    (0, "TIMETRA-FILTER-MIB", "tFltrRPDstAddr"),
)
if mibBuilder.loadTexts:
    tFilterRPlcyUnicastRtTestEntry.setStatus("current")
_TFltrRPUcastRtTLastChanged_Type = TimeStamp
_TFltrRPUcastRtTLastChanged_Object = MibTableColumn
tFltrRPUcastRtTLastChanged = _TFltrRPUcastRtTLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 67, 1, 1),
    _TFltrRPUcastRtTLastChanged_Type()
)
tFltrRPUcastRtTLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrRPUcastRtTLastChanged.setStatus("current")
_TFltrRPUcastRtTRowStatus_Type = RowStatus
_TFltrRPUcastRtTRowStatus_Object = MibTableColumn
tFltrRPUcastRtTRowStatus = _TFltrRPUcastRtTRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 67, 1, 2),
    _TFltrRPUcastRtTRowStatus_Type()
)
tFltrRPUcastRtTRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFltrRPUcastRtTRowStatus.setStatus("current")
_TFltrRPUcastRtTLastActionTime_Type = TimeStamp
_TFltrRPUcastRtTLastActionTime_Object = MibTableColumn
tFltrRPUcastRtTLastActionTime = _TFltrRPUcastRtTLastActionTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 67, 1, 3),
    _TFltrRPUcastRtTLastActionTime_Type()
)
tFltrRPUcastRtTLastActionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrRPUcastRtTLastActionTime.setStatus("current")
_TFltrRPUcastRtTLastAction_Type = TmnxFilterRPlcyTestLastAction
_TFltrRPUcastRtTLastAction_Object = MibTableColumn
tFltrRPUcastRtTLastAction = _TFltrRPUcastRtTLastAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 67, 1, 4),
    _TFltrRPUcastRtTLastAction_Type()
)
tFltrRPUcastRtTLastAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrRPUcastRtTLastAction.setStatus("current")
_TFilterSystemFilterTableLastChg_Type = TimeStamp
_TFilterSystemFilterTableLastChg_Object = MibScalar
tFilterSystemFilterTableLastChg = _TFilterSystemFilterTableLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 68),
    _TFilterSystemFilterTableLastChg_Type()
)
tFilterSystemFilterTableLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterSystemFilterTableLastChg.setStatus("current")
_TFilterSystemFilterTable_Object = MibTable
tFilterSystemFilterTable = _TFilterSystemFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 69)
)
if mibBuilder.loadTexts:
    tFilterSystemFilterTable.setStatus("current")
_TFilterSystemFilterEntry_Object = MibTableRow
tFilterSystemFilterEntry = _TFilterSystemFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 69, 1)
)
tFilterSystemFilterEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tFilterSystemFilterType"),
    (0, "TIMETRA-FILTER-MIB", "tFilterSystemFilterId"),
)
if mibBuilder.loadTexts:
    tFilterSystemFilterEntry.setStatus("current")
_TFilterSystemFilterType_Type = TFilterType
_TFilterSystemFilterType_Object = MibTableColumn
tFilterSystemFilterType = _TFilterSystemFilterType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 69, 1, 1),
    _TFilterSystemFilterType_Type()
)
tFilterSystemFilterType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterSystemFilterType.setStatus("current")
_TFilterSystemFilterId_Type = TConfigOrVsdFilterID
_TFilterSystemFilterId_Object = MibTableColumn
tFilterSystemFilterId = _TFilterSystemFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 69, 1, 2),
    _TFilterSystemFilterId_Type()
)
tFilterSystemFilterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterSystemFilterId.setStatus("current")
_TFilterSystemFilterLastChanged_Type = TimeStamp
_TFilterSystemFilterLastChanged_Object = MibTableColumn
tFilterSystemFilterLastChanged = _TFilterSystemFilterLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 69, 1, 3),
    _TFilterSystemFilterLastChanged_Type()
)
tFilterSystemFilterLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterSystemFilterLastChanged.setStatus("current")
_TFilterSystemFilterRowStatus_Type = RowStatus
_TFilterSystemFilterRowStatus_Object = MibTableColumn
tFilterSystemFilterRowStatus = _TFilterSystemFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 69, 1, 4),
    _TFilterSystemFilterRowStatus_Type()
)
tFilterSystemFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterSystemFilterRowStatus.setStatus("current")
_TDhcp6FilterTblLastChanged_Type = TimeStamp
_TDhcp6FilterTblLastChanged_Object = MibScalar
tDhcp6FilterTblLastChanged = _TDhcp6FilterTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 70),
    _TDhcp6FilterTblLastChanged_Type()
)
tDhcp6FilterTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tDhcp6FilterTblLastChanged.setStatus("current")
_TDhcp6FilterTable_Object = MibTable
tDhcp6FilterTable = _TDhcp6FilterTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 71)
)
if mibBuilder.loadTexts:
    tDhcp6FilterTable.setStatus("current")
_TDhcp6FilterEntry_Object = MibTableRow
tDhcp6FilterEntry = _TDhcp6FilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 71, 1)
)
tDhcp6FilterEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tDhcp6FilterId"),
)
if mibBuilder.loadTexts:
    tDhcp6FilterEntry.setStatus("current")


class _TDhcp6FilterId_Type(TDHCPFilterID):
    """Custom type tDhcp6FilterId based on TDHCPFilterID"""
    subtypeSpec = TDHCPFilterID.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TDhcp6FilterId_Type.__name__ = "TDHCPFilterID"
_TDhcp6FilterId_Object = MibTableColumn
tDhcp6FilterId = _TDhcp6FilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 71, 1, 1),
    _TDhcp6FilterId_Type()
)
tDhcp6FilterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tDhcp6FilterId.setStatus("current")
_TDhcp6FilterRowStatus_Type = RowStatus
_TDhcp6FilterRowStatus_Object = MibTableColumn
tDhcp6FilterRowStatus = _TDhcp6FilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 71, 1, 2),
    _TDhcp6FilterRowStatus_Type()
)
tDhcp6FilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tDhcp6FilterRowStatus.setStatus("current")
_TDhcp6FilterLastChanged_Type = TimeStamp
_TDhcp6FilterLastChanged_Object = MibTableColumn
tDhcp6FilterLastChanged = _TDhcp6FilterLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 71, 1, 3),
    _TDhcp6FilterLastChanged_Type()
)
tDhcp6FilterLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tDhcp6FilterLastChanged.setStatus("current")


class _TDhcp6FilterDescription_Type(TItemDescription):
    """Custom type tDhcp6FilterDescription based on TItemDescription"""
    defaultHexValue = ""


_TDhcp6FilterDescription_Type.__name__ = "TItemDescription"
_TDhcp6FilterDescription_Object = MibTableColumn
tDhcp6FilterDescription = _TDhcp6FilterDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 71, 1, 4),
    _TDhcp6FilterDescription_Type()
)
tDhcp6FilterDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tDhcp6FilterDescription.setStatus("current")


class _TDhcp6FilterDefAction_Type(TDhcpFilterAction):
    """Custom type tDhcp6FilterDefAction based on TDhcpFilterAction"""
    defaultValue = 1


_TDhcp6FilterDefAction_Type.__name__ = "TDhcpFilterAction"
_TDhcp6FilterDefAction_Object = MibTableColumn
tDhcp6FilterDefAction = _TDhcp6FilterDefAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 71, 1, 5),
    _TDhcp6FilterDefAction_Type()
)
tDhcp6FilterDefAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tDhcp6FilterDefAction.setStatus("current")


class _TDhcp6FilterDefActionFlags_Type(Bits):
    """Custom type tDhcp6FilterDefActionFlags based on Bits"""
    namedValues = NamedValues(
        *(("na", 0),
          ("pd", 1))
    )

_TDhcp6FilterDefActionFlags_Type.__name__ = "Bits"
_TDhcp6FilterDefActionFlags_Object = MibTableColumn
tDhcp6FilterDefActionFlags = _TDhcp6FilterDefActionFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 71, 1, 6),
    _TDhcp6FilterDefActionFlags_Type()
)
tDhcp6FilterDefActionFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tDhcp6FilterDefActionFlags.setStatus("current")
_TDhcp6FilterParamsTblLastChanged_Type = TimeStamp
_TDhcp6FilterParamsTblLastChanged_Object = MibScalar
tDhcp6FilterParamsTblLastChanged = _TDhcp6FilterParamsTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 72),
    _TDhcp6FilterParamsTblLastChanged_Type()
)
tDhcp6FilterParamsTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tDhcp6FilterParamsTblLastChanged.setStatus("current")
_TDhcp6FilterParamsTable_Object = MibTable
tDhcp6FilterParamsTable = _TDhcp6FilterParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 73)
)
if mibBuilder.loadTexts:
    tDhcp6FilterParamsTable.setStatus("current")
_TDhcp6FilterParamsEntry_Object = MibTableRow
tDhcp6FilterParamsEntry = _TDhcp6FilterParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 73, 1)
)
tDhcp6FilterParamsEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tDhcp6FilterId"),
    (0, "TIMETRA-FILTER-MIB", "tDhcp6FilterParamsId"),
)
if mibBuilder.loadTexts:
    tDhcp6FilterParamsEntry.setStatus("current")
_TDhcp6FilterParamsId_Type = TDhcpEntryId
_TDhcp6FilterParamsId_Object = MibTableColumn
tDhcp6FilterParamsId = _TDhcp6FilterParamsId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 73, 1, 1),
    _TDhcp6FilterParamsId_Type()
)
tDhcp6FilterParamsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tDhcp6FilterParamsId.setStatus("current")
_TDhcp6FilterParamsRowStatus_Type = RowStatus
_TDhcp6FilterParamsRowStatus_Object = MibTableColumn
tDhcp6FilterParamsRowStatus = _TDhcp6FilterParamsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 73, 1, 2),
    _TDhcp6FilterParamsRowStatus_Type()
)
tDhcp6FilterParamsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tDhcp6FilterParamsRowStatus.setStatus("current")
_TDhcp6FilterParamsLastChanged_Type = TimeStamp
_TDhcp6FilterParamsLastChanged_Object = MibTableColumn
tDhcp6FilterParamsLastChanged = _TDhcp6FilterParamsLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 73, 1, 3),
    _TDhcp6FilterParamsLastChanged_Type()
)
tDhcp6FilterParamsLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tDhcp6FilterParamsLastChanged.setStatus("current")


class _TDhcp6FilterParamsOptionNumber_Type(Integer32):
    """Custom type tDhcp6FilterParamsOptionNumber based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_TDhcp6FilterParamsOptionNumber_Type.__name__ = "Integer32"
_TDhcp6FilterParamsOptionNumber_Object = MibTableColumn
tDhcp6FilterParamsOptionNumber = _TDhcp6FilterParamsOptionNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 73, 1, 4),
    _TDhcp6FilterParamsOptionNumber_Type()
)
tDhcp6FilterParamsOptionNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tDhcp6FilterParamsOptionNumber.setStatus("current")


class _TDhcp6FilterParamsOptionMatch_Type(TDhcpFilterMatch):
    """Custom type tDhcp6FilterParamsOptionMatch based on TDhcpFilterMatch"""
    defaultValue = 1


_TDhcp6FilterParamsOptionMatch_Type.__name__ = "TDhcpFilterMatch"
_TDhcp6FilterParamsOptionMatch_Object = MibTableColumn
tDhcp6FilterParamsOptionMatch = _TDhcp6FilterParamsOptionMatch_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 73, 1, 5),
    _TDhcp6FilterParamsOptionMatch_Type()
)
tDhcp6FilterParamsOptionMatch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tDhcp6FilterParamsOptionMatch.setStatus("current")


class _TDhcp6FilterParamsAction_Type(TDhcpFilterAction):
    """Custom type tDhcp6FilterParamsAction based on TDhcpFilterAction"""
    defaultValue = 1


_TDhcp6FilterParamsAction_Type.__name__ = "TDhcpFilterAction"
_TDhcp6FilterParamsAction_Object = MibTableColumn
tDhcp6FilterParamsAction = _TDhcp6FilterParamsAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 73, 1, 6),
    _TDhcp6FilterParamsAction_Type()
)
tDhcp6FilterParamsAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tDhcp6FilterParamsAction.setStatus("current")


class _TDhcp6FilterParamsOptionValue_Type(OctetString):
    """Custom type tDhcp6FilterParamsOptionValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_TDhcp6FilterParamsOptionValue_Type.__name__ = "OctetString"
_TDhcp6FilterParamsOptionValue_Object = MibTableColumn
tDhcp6FilterParamsOptionValue = _TDhcp6FilterParamsOptionValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 73, 1, 7),
    _TDhcp6FilterParamsOptionValue_Type()
)
tDhcp6FilterParamsOptionValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tDhcp6FilterParamsOptionValue.setStatus("current")


class _TDhcp6FilterParamsActionFlags_Type(Bits):
    """Custom type tDhcp6FilterParamsActionFlags based on Bits"""
    namedValues = NamedValues(
        *(("na", 0),
          ("pd", 1))
    )

_TDhcp6FilterParamsActionFlags_Type.__name__ = "Bits"
_TDhcp6FilterParamsActionFlags_Object = MibTableColumn
tDhcp6FilterParamsActionFlags = _TDhcp6FilterParamsActionFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 73, 1, 8),
    _TDhcp6FilterParamsActionFlags_Type()
)
tDhcp6FilterParamsActionFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tDhcp6FilterParamsActionFlags.setStatus("current")
_TFilterEmbedFlowspecTableLstChg_Type = TimeStamp
_TFilterEmbedFlowspecTableLstChg_Object = MibScalar
tFilterEmbedFlowspecTableLstChg = _TFilterEmbedFlowspecTableLstChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 74),
    _TFilterEmbedFlowspecTableLstChg_Type()
)
tFilterEmbedFlowspecTableLstChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterEmbedFlowspecTableLstChg.setStatus("current")
_TFilterEmbedFlowspecTable_Object = MibTable
tFilterEmbedFlowspecTable = _TFilterEmbedFlowspecTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 75)
)
if mibBuilder.loadTexts:
    tFilterEmbedFlowspecTable.setStatus("current")
_TFilterEmbedFlowspecEntry_Object = MibTableRow
tFilterEmbedFlowspecEntry = _TFilterEmbedFlowspecEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 75, 1)
)
tFilterEmbedFlowspecEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tFilterEmbedFlowspecFilterType"),
    (0, "TIMETRA-FILTER-MIB", "tFilterEmbedFlowspecInsertFltrId"),
    (0, "TIMETRA-FILTER-MIB", "tFilterEmbedFlowspecOffset"),
)
if mibBuilder.loadTexts:
    tFilterEmbedFlowspecEntry.setStatus("current")
_TFilterEmbedFlowspecFilterType_Type = TFilterType
_TFilterEmbedFlowspecFilterType_Object = MibTableColumn
tFilterEmbedFlowspecFilterType = _TFilterEmbedFlowspecFilterType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 75, 1, 1),
    _TFilterEmbedFlowspecFilterType_Type()
)
tFilterEmbedFlowspecFilterType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterEmbedFlowspecFilterType.setStatus("current")
_TFilterEmbedFlowspecInsertFltrId_Type = TConfigOrVsdFilterID
_TFilterEmbedFlowspecInsertFltrId_Object = MibTableColumn
tFilterEmbedFlowspecInsertFltrId = _TFilterEmbedFlowspecInsertFltrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 75, 1, 2),
    _TFilterEmbedFlowspecInsertFltrId_Type()
)
tFilterEmbedFlowspecInsertFltrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterEmbedFlowspecInsertFltrId.setStatus("current")
_TFilterEmbedFlowspecOffset_Type = TFilterEmbedOffset
_TFilterEmbedFlowspecOffset_Object = MibTableColumn
tFilterEmbedFlowspecOffset = _TFilterEmbedFlowspecOffset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 75, 1, 3),
    _TFilterEmbedFlowspecOffset_Type()
)
tFilterEmbedFlowspecOffset.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterEmbedFlowspecOffset.setStatus("current")
_TFilterEmbedFlowspecRowStatus_Type = RowStatus
_TFilterEmbedFlowspecRowStatus_Object = MibTableColumn
tFilterEmbedFlowspecRowStatus = _TFilterEmbedFlowspecRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 75, 1, 4),
    _TFilterEmbedFlowspecRowStatus_Type()
)
tFilterEmbedFlowspecRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterEmbedFlowspecRowStatus.setStatus("current")
_TFilterEmbedFlowspecLastChanged_Type = TimeStamp
_TFilterEmbedFlowspecLastChanged_Object = MibTableColumn
tFilterEmbedFlowspecLastChanged = _TFilterEmbedFlowspecLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 75, 1, 5),
    _TFilterEmbedFlowspecLastChanged_Type()
)
tFilterEmbedFlowspecLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterEmbedFlowspecLastChanged.setStatus("current")
_TFilterEmbedFlowspecRtrId_Type = TmnxVRtrID
_TFilterEmbedFlowspecRtrId_Object = MibTableColumn
tFilterEmbedFlowspecRtrId = _TFilterEmbedFlowspecRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 75, 1, 6),
    _TFilterEmbedFlowspecRtrId_Type()
)
tFilterEmbedFlowspecRtrId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterEmbedFlowspecRtrId.setStatus("current")


class _TFilterEmbedFlowspecAdminState_Type(TmnxEmbeddedFltrAdminState):
    """Custom type tFilterEmbedFlowspecAdminState based on TmnxEmbeddedFltrAdminState"""
    defaultValue = 1


_TFilterEmbedFlowspecAdminState_Type.__name__ = "TmnxEmbeddedFltrAdminState"
_TFilterEmbedFlowspecAdminState_Object = MibTableColumn
tFilterEmbedFlowspecAdminState = _TFilterEmbedFlowspecAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 75, 1, 7),
    _TFilterEmbedFlowspecAdminState_Type()
)
tFilterEmbedFlowspecAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterEmbedFlowspecAdminState.setStatus("current")
_TFilterEmbedFlowspecOperState_Type = TmnxEmbeddedFltrOperState
_TFilterEmbedFlowspecOperState_Object = MibTableColumn
tFilterEmbedFlowspecOperState = _TFilterEmbedFlowspecOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 75, 1, 8),
    _TFilterEmbedFlowspecOperState_Type()
)
tFilterEmbedFlowspecOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterEmbedFlowspecOperState.setStatus("current")


class _TFilterEmbedFlowspecGroupId_Type(TFilterFlowspecGroupId):
    """Custom type tFilterEmbedFlowspecGroupId based on TFilterFlowspecGroupId"""
    defaultValue = 65535


_TFilterEmbedFlowspecGroupId_Type.__name__ = "TFilterFlowspecGroupId"
_TFilterEmbedFlowspecGroupId_Object = MibTableColumn
tFilterEmbedFlowspecGroupId = _TFilterEmbedFlowspecGroupId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 75, 1, 9),
    _TFilterEmbedFlowspecGroupId_Type()
)
tFilterEmbedFlowspecGroupId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterEmbedFlowspecGroupId.setStatus("current")
_TFltrEmbFlowspecInfoTable_Object = MibTable
tFltrEmbFlowspecInfoTable = _TFltrEmbFlowspecInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 76)
)
if mibBuilder.loadTexts:
    tFltrEmbFlowspecInfoTable.setStatus("current")
_TFltrEmbFlowspecInfoEntry_Object = MibTableRow
tFltrEmbFlowspecInfoEntry = _TFltrEmbFlowspecInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 76, 1)
)
if mibBuilder.loadTexts:
    tFltrEmbFlowspecInfoEntry.setStatus("current")
_TFltrEmbFlowSpecInfoFltrId_Type = TAnyFilterID
_TFltrEmbFlowSpecInfoFltrId_Object = MibTableColumn
tFltrEmbFlowSpecInfoFltrId = _TFltrEmbFlowSpecInfoFltrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 76, 1, 1),
    _TFltrEmbFlowSpecInfoFltrId_Type()
)
tFltrEmbFlowSpecInfoFltrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrEmbFlowSpecInfoFltrId.setStatus("current")
_TFltrEmbFlowSpecInfoEntryCnt_Type = Unsigned32
_TFltrEmbFlowSpecInfoEntryCnt_Object = MibTableColumn
tFltrEmbFlowSpecInfoEntryCnt = _TFltrEmbFlowSpecInfoEntryCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 76, 1, 2),
    _TFltrEmbFlowSpecInfoEntryCnt_Type()
)
tFltrEmbFlowSpecInfoEntryCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrEmbFlowSpecInfoEntryCnt.setStatus("current")
_TFltrEmbFlowSpecInfoEntryCntIns_Type = Unsigned32
_TFltrEmbFlowSpecInfoEntryCntIns_Object = MibTableColumn
tFltrEmbFlowSpecInfoEntryCntIns = _TFltrEmbFlowSpecInfoEntryCntIns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 76, 1, 3),
    _TFltrEmbFlowSpecInfoEntryCntIns_Type()
)
tFltrEmbFlowSpecInfoEntryCntIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrEmbFlowSpecInfoEntryCntIns.setStatus("current")
_TFltrEmbFlowspecEntryInfoTable_Object = MibTable
tFltrEmbFlowspecEntryInfoTable = _TFltrEmbFlowspecEntryInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 77)
)
if mibBuilder.loadTexts:
    tFltrEmbFlowspecEntryInfoTable.setStatus("current")
_TFltrEmbFlowspecEntryInfoEntry_Object = MibTableRow
tFltrEmbFlowspecEntryInfoEntry = _TFltrEmbFlowspecEntryInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 77, 1)
)
tFltrEmbFlowspecEntryInfoEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tFilterEmbedFlowspecFilterType"),
    (0, "TIMETRA-FILTER-MIB", "tFilterEmbedFlowspecInsertFltrId"),
    (0, "TIMETRA-FILTER-MIB", "tFltrEmbFlowspecEntryId"),
)
if mibBuilder.loadTexts:
    tFltrEmbFlowspecEntryInfoEntry.setStatus("current")
_TFltrEmbFlowspecEntryId_Type = TEntryId
_TFltrEmbFlowspecEntryId_Object = MibTableColumn
tFltrEmbFlowspecEntryId = _TFltrEmbFlowspecEntryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 77, 1, 1),
    _TFltrEmbFlowspecEntryId_Type()
)
tFltrEmbFlowspecEntryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFltrEmbFlowspecEntryId.setStatus("current")
_TFltrEmbFlowspecEntryInsEntryId_Type = TAnyEntryId
_TFltrEmbFlowspecEntryInsEntryId_Object = MibTableColumn
tFltrEmbFlowspecEntryInsEntryId = _TFltrEmbFlowspecEntryInsEntryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 77, 1, 2),
    _TFltrEmbFlowspecEntryInsEntryId_Type()
)
tFltrEmbFlowspecEntryInsEntryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrEmbFlowspecEntryInsEntryId.setStatus("current")
_TFltrEmbFlowspecEntryOperState_Type = TmnxFltrEmbeddedEntryState
_TFltrEmbFlowspecEntryOperState_Object = MibTableColumn
tFltrEmbFlowspecEntryOperState = _TFltrEmbFlowspecEntryOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 77, 1, 3),
    _TFltrEmbFlowspecEntryOperState_Type()
)
tFltrEmbFlowspecEntryOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrEmbFlowspecEntryOperState.setStatus("current")
_TFilterEmbedVsdTableLstChg_Type = TimeStamp
_TFilterEmbedVsdTableLstChg_Object = MibScalar
tFilterEmbedVsdTableLstChg = _TFilterEmbedVsdTableLstChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 78),
    _TFilterEmbedVsdTableLstChg_Type()
)
tFilterEmbedVsdTableLstChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterEmbedVsdTableLstChg.setStatus("current")
_TFilterEmbedVsdTable_Object = MibTable
tFilterEmbedVsdTable = _TFilterEmbedVsdTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 79)
)
if mibBuilder.loadTexts:
    tFilterEmbedVsdTable.setStatus("current")
_TFilterEmbedVsdEntry_Object = MibTableRow
tFilterEmbedVsdEntry = _TFilterEmbedVsdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 79, 1)
)
tFilterEmbedVsdEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tFilterEmbedVsdFilterType"),
    (0, "TIMETRA-FILTER-MIB", "tFilterEmbedVsdInsertFltrId"),
    (0, "TIMETRA-FILTER-MIB", "tFilterEmbedVsdEmbeddedFltrId"),
    (0, "TIMETRA-FILTER-MIB", "tFilterEmbedVsdOffset"),
)
if mibBuilder.loadTexts:
    tFilterEmbedVsdEntry.setStatus("current")
_TFilterEmbedVsdFilterType_Type = TFilterType
_TFilterEmbedVsdFilterType_Object = MibTableColumn
tFilterEmbedVsdFilterType = _TFilterEmbedVsdFilterType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 79, 1, 1),
    _TFilterEmbedVsdFilterType_Type()
)
tFilterEmbedVsdFilterType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterEmbedVsdFilterType.setStatus("current")
_TFilterEmbedVsdInsertFltrId_Type = TConfigOrVsdFilterID
_TFilterEmbedVsdInsertFltrId_Object = MibTableColumn
tFilterEmbedVsdInsertFltrId = _TFilterEmbedVsdInsertFltrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 79, 1, 2),
    _TFilterEmbedVsdInsertFltrId_Type()
)
tFilterEmbedVsdInsertFltrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterEmbedVsdInsertFltrId.setStatus("current")
_TFilterEmbedVsdEmbeddedFltrId_Type = TVsdFilterID
_TFilterEmbedVsdEmbeddedFltrId_Object = MibTableColumn
tFilterEmbedVsdEmbeddedFltrId = _TFilterEmbedVsdEmbeddedFltrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 79, 1, 3),
    _TFilterEmbedVsdEmbeddedFltrId_Type()
)
tFilterEmbedVsdEmbeddedFltrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterEmbedVsdEmbeddedFltrId.setStatus("current")
_TFilterEmbedVsdOffset_Type = TFilterEmbedOffset
_TFilterEmbedVsdOffset_Object = MibTableColumn
tFilterEmbedVsdOffset = _TFilterEmbedVsdOffset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 79, 1, 4),
    _TFilterEmbedVsdOffset_Type()
)
tFilterEmbedVsdOffset.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterEmbedVsdOffset.setStatus("current")
_TFilterEmbedVsdRowStatus_Type = RowStatus
_TFilterEmbedVsdRowStatus_Object = MibTableColumn
tFilterEmbedVsdRowStatus = _TFilterEmbedVsdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 79, 1, 5),
    _TFilterEmbedVsdRowStatus_Type()
)
tFilterEmbedVsdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterEmbedVsdRowStatus.setStatus("current")
_TFilterEmbedVsdLastChanged_Type = TimeStamp
_TFilterEmbedVsdLastChanged_Object = MibTableColumn
tFilterEmbedVsdLastChanged = _TFilterEmbedVsdLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 79, 1, 6),
    _TFilterEmbedVsdLastChanged_Type()
)
tFilterEmbedVsdLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterEmbedVsdLastChanged.setStatus("current")


class _TFilterEmbedVsdAdminState_Type(TmnxEmbeddedFltrAdminState):
    """Custom type tFilterEmbedVsdAdminState based on TmnxEmbeddedFltrAdminState"""
    defaultValue = 1


_TFilterEmbedVsdAdminState_Type.__name__ = "TmnxEmbeddedFltrAdminState"
_TFilterEmbedVsdAdminState_Object = MibTableColumn
tFilterEmbedVsdAdminState = _TFilterEmbedVsdAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 79, 1, 7),
    _TFilterEmbedVsdAdminState_Type()
)
tFilterEmbedVsdAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterEmbedVsdAdminState.setStatus("current")
_TFilterEmbedVsdOperState_Type = TmnxEmbeddedFltrOperState
_TFilterEmbedVsdOperState_Object = MibTableColumn
tFilterEmbedVsdOperState = _TFilterEmbedVsdOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 79, 1, 8),
    _TFilterEmbedVsdOperState_Type()
)
tFilterEmbedVsdOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterEmbedVsdOperState.setStatus("current")
_TFilterEmbedVsdInfoTable_Object = MibTable
tFilterEmbedVsdInfoTable = _TFilterEmbedVsdInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 80)
)
if mibBuilder.loadTexts:
    tFilterEmbedVsdInfoTable.setStatus("current")
_TFilterEmbedVsdInfoEntry_Object = MibTableRow
tFilterEmbedVsdInfoEntry = _TFilterEmbedVsdInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 80, 1)
)
if mibBuilder.loadTexts:
    tFilterEmbedVsdInfoEntry.setStatus("current")
_TFltrEmbedVsdInfoEntryCnt_Type = Unsigned32
_TFltrEmbedVsdInfoEntryCnt_Object = MibTableColumn
tFltrEmbedVsdInfoEntryCnt = _TFltrEmbedVsdInfoEntryCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 80, 1, 1),
    _TFltrEmbedVsdInfoEntryCnt_Type()
)
tFltrEmbedVsdInfoEntryCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrEmbedVsdInfoEntryCnt.setStatus("current")
_TFltrEmbedVsdInfoEntryCntInsrtd_Type = Unsigned32
_TFltrEmbedVsdInfoEntryCntInsrtd_Object = MibTableColumn
tFltrEmbedVsdInfoEntryCntInsrtd = _TFltrEmbedVsdInfoEntryCntInsrtd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 80, 1, 2),
    _TFltrEmbedVsdInfoEntryCntInsrtd_Type()
)
tFltrEmbedVsdInfoEntryCntInsrtd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrEmbedVsdInfoEntryCntInsrtd.setStatus("current")
_TFilterEmbedVsdEntryInfoTable_Object = MibTable
tFilterEmbedVsdEntryInfoTable = _TFilterEmbedVsdEntryInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 81)
)
if mibBuilder.loadTexts:
    tFilterEmbedVsdEntryInfoTable.setStatus("current")
_TFilterEmbedVsdEntryInfoEntry_Object = MibTableRow
tFilterEmbedVsdEntryInfoEntry = _TFilterEmbedVsdEntryInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 81, 1)
)
tFilterEmbedVsdEntryInfoEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tFilterEmbedVsdFilterType"),
    (0, "TIMETRA-FILTER-MIB", "tFilterEmbedVsdInsertFltrId"),
    (0, "TIMETRA-FILTER-MIB", "tFilterEmbedVsdEmbeddedFltrId"),
    (0, "TIMETRA-FILTER-MIB", "tFilterEmbedVsdEntryId"),
)
if mibBuilder.loadTexts:
    tFilterEmbedVsdEntryInfoEntry.setStatus("current")
_TFilterEmbedVsdEntryId_Type = TEntryId
_TFilterEmbedVsdEntryId_Object = MibTableColumn
tFilterEmbedVsdEntryId = _TFilterEmbedVsdEntryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 81, 1, 1),
    _TFilterEmbedVsdEntryId_Type()
)
tFilterEmbedVsdEntryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterEmbedVsdEntryId.setStatus("current")
_TFilterEmbedVsdEntryInsrtEntryId_Type = TAnyEntryId
_TFilterEmbedVsdEntryInsrtEntryId_Object = MibTableColumn
tFilterEmbedVsdEntryInsrtEntryId = _TFilterEmbedVsdEntryInsrtEntryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 81, 1, 2),
    _TFilterEmbedVsdEntryInsrtEntryId_Type()
)
tFilterEmbedVsdEntryInsrtEntryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterEmbedVsdEntryInsrtEntryId.setStatus("current")
_TFilterEmbedVsdEntryOperState_Type = TmnxFltrEmbeddedEntryState
_TFilterEmbedVsdEntryOperState_Object = MibTableColumn
tFilterEmbedVsdEntryOperState = _TFilterEmbedVsdEntryOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 81, 1, 3),
    _TFilterEmbedVsdEntryOperState_Type()
)
tFilterEmbedVsdEntryOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterEmbedVsdEntryOperState.setStatus("current")
_TMacFltrEntryActionTblLChg_Type = TimeStamp
_TMacFltrEntryActionTblLChg_Object = MibScalar
tMacFltrEntryActionTblLChg = _TMacFltrEntryActionTblLChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 82),
    _TMacFltrEntryActionTblLChg_Type()
)
tMacFltrEntryActionTblLChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMacFltrEntryActionTblLChg.setStatus("current")
_TMacFltrEntryActionTable_Object = MibTable
tMacFltrEntryActionTable = _TMacFltrEntryActionTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 83)
)
if mibBuilder.loadTexts:
    tMacFltrEntryActionTable.setStatus("current")
_TMacFltrEntryActionEntry_Object = MibTableRow
tMacFltrEntryActionEntry = _TMacFltrEntryActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 83, 1)
)
tMacFltrEntryActionEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tMacFilterId"),
    (0, "TIMETRA-FILTER-MIB", "tMacFilterParamsIndex"),
    (0, "TIMETRA-FILTER-MIB", "tMacFltrEntryActActionId"),
)
if mibBuilder.loadTexts:
    tMacFltrEntryActionEntry.setStatus("current")
_TMacFltrEntryActActionId_Type = TFilterEntryActionId
_TMacFltrEntryActActionId_Object = MibTableColumn
tMacFltrEntryActActionId = _TMacFltrEntryActActionId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 83, 1, 1),
    _TMacFltrEntryActActionId_Type()
)
tMacFltrEntryActActionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMacFltrEntryActActionId.setStatus("current")
_TMacFltrEntryActLastChanged_Type = TimeStamp
_TMacFltrEntryActLastChanged_Object = MibTableColumn
tMacFltrEntryActLastChanged = _TMacFltrEntryActLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 83, 1, 2),
    _TMacFltrEntryActLastChanged_Type()
)
tMacFltrEntryActLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMacFltrEntryActLastChanged.setStatus("current")
_TMacFltrEntryActRowStatus_Type = RowStatus
_TMacFltrEntryActRowStatus_Object = MibTableColumn
tMacFltrEntryActRowStatus = _TMacFltrEntryActRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 83, 1, 3),
    _TMacFltrEntryActRowStatus_Type()
)
tMacFltrEntryActRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFltrEntryActRowStatus.setStatus("current")


class _TMacFltrEntryActAction_Type(TMacFilterEntryAction):
    """Custom type tMacFltrEntryActAction based on TMacFilterEntryAction"""
    defaultValue = 30


_TMacFltrEntryActAction_Type.__name__ = "TMacFilterEntryAction"
_TMacFltrEntryActAction_Object = MibTableColumn
tMacFltrEntryActAction = _TMacFltrEntryActAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 83, 1, 4),
    _TMacFltrEntryActAction_Type()
)
tMacFltrEntryActAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFltrEntryActAction.setStatus("current")


class _TMacFltrEntryActFwdSapPortId_Type(TmnxPortID):
    """Custom type tMacFltrEntryActFwdSapPortId based on TmnxPortID"""
    defaultValue = 0


_TMacFltrEntryActFwdSapPortId_Type.__name__ = "TmnxPortID"
_TMacFltrEntryActFwdSapPortId_Object = MibTableColumn
tMacFltrEntryActFwdSapPortId = _TMacFltrEntryActFwdSapPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 83, 1, 5),
    _TMacFltrEntryActFwdSapPortId_Type()
)
tMacFltrEntryActFwdSapPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFltrEntryActFwdSapPortId.setStatus("current")


class _TMacFltrEntryActFwdSapEncapVal_Type(TmnxEncapVal):
    """Custom type tMacFltrEntryActFwdSapEncapVal based on TmnxEncapVal"""
    defaultValue = 0


_TMacFltrEntryActFwdSapEncapVal_Type.__name__ = "TmnxEncapVal"
_TMacFltrEntryActFwdSapEncapVal_Object = MibTableColumn
tMacFltrEntryActFwdSapEncapVal = _TMacFltrEntryActFwdSapEncapVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 83, 1, 6),
    _TMacFltrEntryActFwdSapEncapVal_Type()
)
tMacFltrEntryActFwdSapEncapVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFltrEntryActFwdSapEncapVal.setStatus("current")


class _TMacFltrEntryActFwdSdpBind_Type(SdpBindId):
    """Custom type tMacFltrEntryActFwdSdpBind based on SdpBindId"""
    defaultHexValue = "0000000000000000"


_TMacFltrEntryActFwdSdpBind_Type.__name__ = "SdpBindId"
_TMacFltrEntryActFwdSdpBind_Object = MibTableColumn
tMacFltrEntryActFwdSdpBind = _TMacFltrEntryActFwdSdpBind_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 83, 1, 7),
    _TMacFltrEntryActFwdSdpBind_Type()
)
tMacFltrEntryActFwdSdpBind.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFltrEntryActFwdSdpBind.setStatus("current")


class _TMacFltrEntryActRedirectURL_Type(TmnxHttpRedirectUrl):
    """Custom type tMacFltrEntryActRedirectURL based on TmnxHttpRedirectUrl"""
    defaultHexValue = ""


_TMacFltrEntryActRedirectURL_Type.__name__ = "TmnxHttpRedirectUrl"
_TMacFltrEntryActRedirectURL_Object = MibTableColumn
tMacFltrEntryActRedirectURL = _TMacFltrEntryActRedirectURL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 83, 1, 8),
    _TMacFltrEntryActRedirectURL_Type()
)
tMacFltrEntryActRedirectURL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFltrEntryActRedirectURL.setStatus("current")


class _TMacFltrEntryActEsi_Type(TFilterEsi):
    """Custom type tMacFltrEntryActEsi based on TFilterEsi"""
    defaultHexValue = "00000000000000000000"


_TMacFltrEntryActEsi_Type.__name__ = "TFilterEsi"
_TMacFltrEntryActEsi_Object = MibTableColumn
tMacFltrEntryActEsi = _TMacFltrEntryActEsi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 83, 1, 9),
    _TMacFltrEntryActEsi_Type()
)
tMacFltrEntryActEsi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFltrEntryActEsi.setStatus("current")


class _TMacFltrEntryActFwdEsiSvcId_Type(TmnxServId):
    """Custom type tMacFltrEntryActFwdEsiSvcId based on TmnxServId"""
    defaultValue = 0


_TMacFltrEntryActFwdEsiSvcId_Type.__name__ = "TmnxServId"
_TMacFltrEntryActFwdEsiSvcId_Object = MibTableColumn
tMacFltrEntryActFwdEsiSvcId = _TMacFltrEntryActFwdEsiSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 83, 1, 10),
    _TMacFltrEntryActFwdEsiSvcId_Type()
)
tMacFltrEntryActFwdEsiSvcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFltrEntryActFwdEsiSvcId.setStatus("current")


class _TMacFltrEntryActRateLimit_Type(TFilterEntryActionRateLimit):
    """Custom type tMacFltrEntryActRateLimit based on TFilterEntryActionRateLimit"""
    defaultValue = 0


_TMacFltrEntryActRateLimit_Type.__name__ = "TFilterEntryActionRateLimit"
_TMacFltrEntryActRateLimit_Object = MibTableColumn
tMacFltrEntryActRateLimit = _TMacFltrEntryActRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 83, 1, 11),
    _TMacFltrEntryActRateLimit_Type()
)
tMacFltrEntryActRateLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFltrEntryActRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    tMacFltrEntryActRateLimit.setUnits("kilobps")
_TMacFltrEntryActPbrTargetStatus_Type = TFilterPbrTargetStatus
_TMacFltrEntryActPbrTargetStatus_Object = MibTableColumn
tMacFltrEntryActPbrTargetStatus = _TMacFltrEntryActPbrTargetStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 83, 1, 12),
    _TMacFltrEntryActPbrTargetStatus_Type()
)
tMacFltrEntryActPbrTargetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMacFltrEntryActPbrTargetStatus.setStatus("current")


class _TMacFltrEntryActFcName_Type(TFCTypeOrNone):
    """Custom type tMacFltrEntryActFcName based on TFCTypeOrNone"""
    defaultValue = -1


_TMacFltrEntryActFcName_Type.__name__ = "TFCTypeOrNone"
_TMacFltrEntryActFcName_Object = MibTableColumn
tMacFltrEntryActFcName = _TMacFltrEntryActFcName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 83, 1, 13),
    _TMacFltrEntryActFcName_Type()
)
tMacFltrEntryActFcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMacFltrEntryActFcName.setStatus("current")
_TIPvXFltrEntryActionTblLChg_Type = TimeStamp
_TIPvXFltrEntryActionTblLChg_Object = MibScalar
tIPvXFltrEntryActionTblLChg = _TIPvXFltrEntryActionTblLChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 84),
    _TIPvXFltrEntryActionTblLChg_Type()
)
tIPvXFltrEntryActionTblLChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPvXFltrEntryActionTblLChg.setStatus("current")
_TIPvXFltrEntryActionTable_Object = MibTable
tIPvXFltrEntryActionTable = _TIPvXFltrEntryActionTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85)
)
if mibBuilder.loadTexts:
    tIPvXFltrEntryActionTable.setStatus("current")
_TIPvXFltrEntryActionEntry_Object = MibTableRow
tIPvXFltrEntryActionEntry = _TIPvXFltrEntryActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85, 1)
)
tIPvXFltrEntryActionEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tIPvXFltrEntryActFltrType"),
    (0, "TIMETRA-FILTER-MIB", "tIPvXFltrEntryActFltrId"),
    (0, "TIMETRA-FILTER-MIB", "tIPvXFltrEntryActEntryId"),
    (0, "TIMETRA-FILTER-MIB", "tIPvXFltrEntryActActionId"),
)
if mibBuilder.loadTexts:
    tIPvXFltrEntryActionEntry.setStatus("current")
_TIPvXFltrEntryActFltrType_Type = TFilterType
_TIPvXFltrEntryActFltrType_Object = MibTableColumn
tIPvXFltrEntryActFltrType = _TIPvXFltrEntryActFltrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85, 1, 1),
    _TIPvXFltrEntryActFltrType_Type()
)
tIPvXFltrEntryActFltrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPvXFltrEntryActFltrType.setStatus("current")
_TIPvXFltrEntryActFltrId_Type = TAnyFilterID
_TIPvXFltrEntryActFltrId_Object = MibTableColumn
tIPvXFltrEntryActFltrId = _TIPvXFltrEntryActFltrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85, 1, 2),
    _TIPvXFltrEntryActFltrId_Type()
)
tIPvXFltrEntryActFltrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPvXFltrEntryActFltrId.setStatus("current")
_TIPvXFltrEntryActEntryId_Type = TEntryId
_TIPvXFltrEntryActEntryId_Object = MibTableColumn
tIPvXFltrEntryActEntryId = _TIPvXFltrEntryActEntryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85, 1, 3),
    _TIPvXFltrEntryActEntryId_Type()
)
tIPvXFltrEntryActEntryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPvXFltrEntryActEntryId.setStatus("current")
_TIPvXFltrEntryActActionId_Type = TFilterEntryActionId
_TIPvXFltrEntryActActionId_Object = MibTableColumn
tIPvXFltrEntryActActionId = _TIPvXFltrEntryActActionId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85, 1, 4),
    _TIPvXFltrEntryActActionId_Type()
)
tIPvXFltrEntryActActionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPvXFltrEntryActActionId.setStatus("current")
_TIPvXFltrEntryActLastChanged_Type = TimeStamp
_TIPvXFltrEntryActLastChanged_Object = MibTableColumn
tIPvXFltrEntryActLastChanged = _TIPvXFltrEntryActLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85, 1, 5),
    _TIPvXFltrEntryActLastChanged_Type()
)
tIPvXFltrEntryActLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPvXFltrEntryActLastChanged.setStatus("current")
_TIPvXFltrEntryActRowStatus_Type = RowStatus
_TIPvXFltrEntryActRowStatus_Object = MibTableColumn
tIPvXFltrEntryActRowStatus = _TIPvXFltrEntryActRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85, 1, 6),
    _TIPvXFltrEntryActRowStatus_Type()
)
tIPvXFltrEntryActRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPvXFltrEntryActRowStatus.setStatus("current")


class _TIPvXFltrEntryActAction_Type(TIPvXFilterEntryAction):
    """Custom type tIPvXFltrEntryActAction based on TIPvXFilterEntryAction"""
    defaultValue = 30


_TIPvXFltrEntryActAction_Type.__name__ = "TIPvXFilterEntryAction"
_TIPvXFltrEntryActAction_Object = MibTableColumn
tIPvXFltrEntryActAction = _TIPvXFltrEntryActAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85, 1, 7),
    _TIPvXFltrEntryActAction_Type()
)
tIPvXFltrEntryActAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPvXFltrEntryActAction.setStatus("current")


class _TIPvXFltrEntryActFwdNHIpAddrType_Type(InetAddressType):
    """Custom type tIPvXFltrEntryActFwdNHIpAddrType based on InetAddressType"""
    defaultValue = 0


_TIPvXFltrEntryActFwdNHIpAddrType_Type.__name__ = "InetAddressType"
_TIPvXFltrEntryActFwdNHIpAddrType_Object = MibTableColumn
tIPvXFltrEntryActFwdNHIpAddrType = _TIPvXFltrEntryActFwdNHIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85, 1, 8),
    _TIPvXFltrEntryActFwdNHIpAddrType_Type()
)
tIPvXFltrEntryActFwdNHIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPvXFltrEntryActFwdNHIpAddrType.setStatus("current")


class _TIPvXFltrEntryActFwdNHIpAddr_Type(InetAddress):
    """Custom type tIPvXFltrEntryActFwdNHIpAddr based on InetAddress"""
    defaultHexValue = "00000000000000000000000000000000"

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TIPvXFltrEntryActFwdNHIpAddr_Type.__name__ = "InetAddress"
_TIPvXFltrEntryActFwdNHIpAddr_Object = MibTableColumn
tIPvXFltrEntryActFwdNHIpAddr = _TIPvXFltrEntryActFwdNHIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85, 1, 9),
    _TIPvXFltrEntryActFwdNHIpAddr_Type()
)
tIPvXFltrEntryActFwdNHIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPvXFltrEntryActFwdNHIpAddr.setStatus("current")


class _TIPvXFltrEntryActFwdNHIndirect_Type(TruthValue):
    """Custom type tIPvXFltrEntryActFwdNHIndirect based on TruthValue"""
    defaultValue = 2


_TIPvXFltrEntryActFwdNHIndirect_Type.__name__ = "TruthValue"
_TIPvXFltrEntryActFwdNHIndirect_Object = MibTableColumn
tIPvXFltrEntryActFwdNHIndirect = _TIPvXFltrEntryActFwdNHIndirect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85, 1, 10),
    _TIPvXFltrEntryActFwdNHIndirect_Type()
)
tIPvXFltrEntryActFwdNHIndirect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPvXFltrEntryActFwdNHIndirect.setStatus("current")


class _TIPvXFltrEntryActFwdNHInterface_Type(TNamedItemOrEmpty):
    """Custom type tIPvXFltrEntryActFwdNHInterface based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TIPvXFltrEntryActFwdNHInterface_Type.__name__ = "TNamedItemOrEmpty"
_TIPvXFltrEntryActFwdNHInterface_Object = MibTableColumn
tIPvXFltrEntryActFwdNHInterface = _TIPvXFltrEntryActFwdNHInterface_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85, 1, 11),
    _TIPvXFltrEntryActFwdNHInterface_Type()
)
tIPvXFltrEntryActFwdNHInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPvXFltrEntryActFwdNHInterface.setStatus("current")


class _TIPvXFltrEntryActFwdRedPlcy_Type(TNamedItemOrEmpty):
    """Custom type tIPvXFltrEntryActFwdRedPlcy based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TIPvXFltrEntryActFwdRedPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TIPvXFltrEntryActFwdRedPlcy_Object = MibTableColumn
tIPvXFltrEntryActFwdRedPlcy = _TIPvXFltrEntryActFwdRedPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85, 1, 12),
    _TIPvXFltrEntryActFwdRedPlcy_Type()
)
tIPvXFltrEntryActFwdRedPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPvXFltrEntryActFwdRedPlcy.setStatus("current")


class _TIPvXFltrEntryActFwdSapPortId_Type(TmnxPortID):
    """Custom type tIPvXFltrEntryActFwdSapPortId based on TmnxPortID"""
    defaultValue = 0


_TIPvXFltrEntryActFwdSapPortId_Type.__name__ = "TmnxPortID"
_TIPvXFltrEntryActFwdSapPortId_Object = MibTableColumn
tIPvXFltrEntryActFwdSapPortId = _TIPvXFltrEntryActFwdSapPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85, 1, 13),
    _TIPvXFltrEntryActFwdSapPortId_Type()
)
tIPvXFltrEntryActFwdSapPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPvXFltrEntryActFwdSapPortId.setStatus("current")


class _TIPvXFltrEntryActFwdSapEncapVal_Type(TmnxEncapVal):
    """Custom type tIPvXFltrEntryActFwdSapEncapVal based on TmnxEncapVal"""
    defaultValue = 0


_TIPvXFltrEntryActFwdSapEncapVal_Type.__name__ = "TmnxEncapVal"
_TIPvXFltrEntryActFwdSapEncapVal_Object = MibTableColumn
tIPvXFltrEntryActFwdSapEncapVal = _TIPvXFltrEntryActFwdSapEncapVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85, 1, 14),
    _TIPvXFltrEntryActFwdSapEncapVal_Type()
)
tIPvXFltrEntryActFwdSapEncapVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPvXFltrEntryActFwdSapEncapVal.setStatus("current")


class _TIPvXFltrEntryActFwdSdpBind_Type(SdpBindId):
    """Custom type tIPvXFltrEntryActFwdSdpBind based on SdpBindId"""
    defaultHexValue = "0000000000000000"


_TIPvXFltrEntryActFwdSdpBind_Type.__name__ = "SdpBindId"
_TIPvXFltrEntryActFwdSdpBind_Object = MibTableColumn
tIPvXFltrEntryActFwdSdpBind = _TIPvXFltrEntryActFwdSdpBind_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85, 1, 15),
    _TIPvXFltrEntryActFwdSdpBind_Type()
)
tIPvXFltrEntryActFwdSdpBind.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPvXFltrEntryActFwdSdpBind.setStatus("current")


class _TIPvXFltrEntryActRedirectURL_Type(TmnxHttpRedirectUrl):
    """Custom type tIPvXFltrEntryActRedirectURL based on TmnxHttpRedirectUrl"""
    defaultHexValue = ""


_TIPvXFltrEntryActRedirectURL_Type.__name__ = "TmnxHttpRedirectUrl"
_TIPvXFltrEntryActRedirectURL_Object = MibTableColumn
tIPvXFltrEntryActRedirectURL = _TIPvXFltrEntryActRedirectURL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85, 1, 16),
    _TIPvXFltrEntryActRedirectURL_Type()
)
tIPvXFltrEntryActRedirectURL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPvXFltrEntryActRedirectURL.setStatus("current")


class _TIPvXFltrEntryActRdirAllwRadOvr_Type(TruthValue):
    """Custom type tIPvXFltrEntryActRdirAllwRadOvr based on TruthValue"""
    defaultValue = 2


_TIPvXFltrEntryActRdirAllwRadOvr_Type.__name__ = "TruthValue"
_TIPvXFltrEntryActRdirAllwRadOvr_Object = MibTableColumn
tIPvXFltrEntryActRdirAllwRadOvr = _TIPvXFltrEntryActRdirAllwRadOvr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85, 1, 17),
    _TIPvXFltrEntryActRdirAllwRadOvr_Type()
)
tIPvXFltrEntryActRdirAllwRadOvr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPvXFltrEntryActRdirAllwRadOvr.setStatus("current")


class _TIPvXFltrEntryActFwdRtrId_Type(TmnxVRtrIDOrZero):
    """Custom type tIPvXFltrEntryActFwdRtrId based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TIPvXFltrEntryActFwdRtrId_Type.__name__ = "TmnxVRtrIDOrZero"
_TIPvXFltrEntryActFwdRtrId_Object = MibTableColumn
tIPvXFltrEntryActFwdRtrId = _TIPvXFltrEntryActFwdRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85, 1, 18),
    _TIPvXFltrEntryActFwdRtrId_Type()
)
tIPvXFltrEntryActFwdRtrId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPvXFltrEntryActFwdRtrId.setStatus("current")


class _TIPvXFltrEntryActNatPolicyName_Type(TNamedItemOrEmpty):
    """Custom type tIPvXFltrEntryActNatPolicyName based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TIPvXFltrEntryActNatPolicyName_Type.__name__ = "TNamedItemOrEmpty"
_TIPvXFltrEntryActNatPolicyName_Object = MibTableColumn
tIPvXFltrEntryActNatPolicyName = _TIPvXFltrEntryActNatPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85, 1, 19),
    _TIPvXFltrEntryActNatPolicyName_Type()
)
tIPvXFltrEntryActNatPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPvXFltrEntryActNatPolicyName.setStatus("current")


class _TIPvXFltrEntryActNatType_Type(TmnxNatSubscriberTypeOrNone):
    """Custom type tIPvXFltrEntryActNatType based on TmnxNatSubscriberTypeOrNone"""
    defaultValue = 3

    subtypeSpec = TmnxNatSubscriberTypeOrNone.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("dsliteLsnSub", 3),
          ("nat64LsnSub", 4))
    )


_TIPvXFltrEntryActNatType_Type.__name__ = "TmnxNatSubscriberTypeOrNone"
_TIPvXFltrEntryActNatType_Object = MibTableColumn
tIPvXFltrEntryActNatType = _TIPvXFltrEntryActNatType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85, 1, 20),
    _TIPvXFltrEntryActNatType_Type()
)
tIPvXFltrEntryActNatType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPvXFltrEntryActNatType.setStatus("current")


class _TIPvXFltrEntryActFwdLsp_Type(TmnxVRtrMplsLspID):
    """Custom type tIPvXFltrEntryActFwdLsp based on TmnxVRtrMplsLspID"""
    defaultValue = 0


_TIPvXFltrEntryActFwdLsp_Type.__name__ = "TmnxVRtrMplsLspID"
_TIPvXFltrEntryActFwdLsp_Object = MibTableColumn
tIPvXFltrEntryActFwdLsp = _TIPvXFltrEntryActFwdLsp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85, 1, 21),
    _TIPvXFltrEntryActFwdLsp_Type()
)
tIPvXFltrEntryActFwdLsp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPvXFltrEntryActFwdLsp.setStatus("current")


class _TIPvXFltrEntryActFwdLspRtrId_Type(TmnxVRtrIDOrZero):
    """Custom type tIPvXFltrEntryActFwdLspRtrId based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TIPvXFltrEntryActFwdLspRtrId_Type.__name__ = "TmnxVRtrIDOrZero"
_TIPvXFltrEntryActFwdLspRtrId_Object = MibTableColumn
tIPvXFltrEntryActFwdLspRtrId = _TIPvXFltrEntryActFwdLspRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85, 1, 22),
    _TIPvXFltrEntryActFwdLspRtrId_Type()
)
tIPvXFltrEntryActFwdLspRtrId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPvXFltrEntryActFwdLspRtrId.setStatus("current")


class _TIPvXFltrEntryActPktLenVal1_Type(TFilterPacketLength):
    """Custom type tIPvXFltrEntryActPktLenVal1 based on TFilterPacketLength"""
    defaultValue = 0


_TIPvXFltrEntryActPktLenVal1_Type.__name__ = "TFilterPacketLength"
_TIPvXFltrEntryActPktLenVal1_Object = MibTableColumn
tIPvXFltrEntryActPktLenVal1 = _TIPvXFltrEntryActPktLenVal1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85, 1, 23),
    _TIPvXFltrEntryActPktLenVal1_Type()
)
tIPvXFltrEntryActPktLenVal1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPvXFltrEntryActPktLenVal1.setStatus("current")


class _TIPvXFltrEntryActPktLenVal2_Type(TFilterPacketLength):
    """Custom type tIPvXFltrEntryActPktLenVal2 based on TFilterPacketLength"""
    defaultValue = 0


_TIPvXFltrEntryActPktLenVal2_Type.__name__ = "TFilterPacketLength"
_TIPvXFltrEntryActPktLenVal2_Object = MibTableColumn
tIPvXFltrEntryActPktLenVal2 = _TIPvXFltrEntryActPktLenVal2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85, 1, 24),
    _TIPvXFltrEntryActPktLenVal2_Type()
)
tIPvXFltrEntryActPktLenVal2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPvXFltrEntryActPktLenVal2.setStatus("current")


class _TIPvXFltrEntryActPktLenOper_Type(TOperator):
    """Custom type tIPvXFltrEntryActPktLenOper based on TOperator"""
    defaultValue = 0


_TIPvXFltrEntryActPktLenOper_Type.__name__ = "TOperator"
_TIPvXFltrEntryActPktLenOper_Object = MibTableColumn
tIPvXFltrEntryActPktLenOper = _TIPvXFltrEntryActPktLenOper_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85, 1, 25),
    _TIPvXFltrEntryActPktLenOper_Type()
)
tIPvXFltrEntryActPktLenOper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPvXFltrEntryActPktLenOper.setStatus("current")


class _TIPvXFltrEntryActTTLVal1_Type(TFilterTTL):
    """Custom type tIPvXFltrEntryActTTLVal1 based on TFilterTTL"""
    defaultValue = 0


_TIPvXFltrEntryActTTLVal1_Type.__name__ = "TFilterTTL"
_TIPvXFltrEntryActTTLVal1_Object = MibTableColumn
tIPvXFltrEntryActTTLVal1 = _TIPvXFltrEntryActTTLVal1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85, 1, 26),
    _TIPvXFltrEntryActTTLVal1_Type()
)
tIPvXFltrEntryActTTLVal1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPvXFltrEntryActTTLVal1.setStatus("current")


class _TIPvXFltrEntryActTTLVal2_Type(TFilterTTL):
    """Custom type tIPvXFltrEntryActTTLVal2 based on TFilterTTL"""
    defaultValue = 0


_TIPvXFltrEntryActTTLVal2_Type.__name__ = "TFilterTTL"
_TIPvXFltrEntryActTTLVal2_Object = MibTableColumn
tIPvXFltrEntryActTTLVal2 = _TIPvXFltrEntryActTTLVal2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85, 1, 27),
    _TIPvXFltrEntryActTTLVal2_Type()
)
tIPvXFltrEntryActTTLVal2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPvXFltrEntryActTTLVal2.setStatus("current")


class _TIPvXFltrEntryActTTLOper_Type(TOperator):
    """Custom type tIPvXFltrEntryActTTLOper based on TOperator"""
    defaultValue = 0


_TIPvXFltrEntryActTTLOper_Type.__name__ = "TOperator"
_TIPvXFltrEntryActTTLOper_Object = MibTableColumn
tIPvXFltrEntryActTTLOper = _TIPvXFltrEntryActTTLOper_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85, 1, 28),
    _TIPvXFltrEntryActTTLOper_Type()
)
tIPvXFltrEntryActTTLOper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPvXFltrEntryActTTLOper.setStatus("current")


class _TIPvXFltrEntryActEsi_Type(TFilterEsi):
    """Custom type tIPvXFltrEntryActEsi based on TFilterEsi"""
    defaultHexValue = "00000000000000000000"


_TIPvXFltrEntryActEsi_Type.__name__ = "TFilterEsi"
_TIPvXFltrEntryActEsi_Object = MibTableColumn
tIPvXFltrEntryActEsi = _TIPvXFltrEntryActEsi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85, 1, 29),
    _TIPvXFltrEntryActEsi_Type()
)
tIPvXFltrEntryActEsi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPvXFltrEntryActEsi.setStatus("current")


class _TIPvXFltrEntryActFwdEsiSvcId_Type(TmnxServId):
    """Custom type tIPvXFltrEntryActFwdEsiSvcId based on TmnxServId"""
    defaultValue = 0


_TIPvXFltrEntryActFwdEsiSvcId_Type.__name__ = "TmnxServId"
_TIPvXFltrEntryActFwdEsiSvcId_Object = MibTableColumn
tIPvXFltrEntryActFwdEsiSvcId = _TIPvXFltrEntryActFwdEsiSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85, 1, 30),
    _TIPvXFltrEntryActFwdEsiSvcId_Type()
)
tIPvXFltrEntryActFwdEsiSvcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPvXFltrEntryActFwdEsiSvcId.setStatus("current")


class _TIPvXFltrEntryActFwdEsiVRtrId_Type(TmnxVRtrIDOrZero):
    """Custom type tIPvXFltrEntryActFwdEsiVRtrId based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TIPvXFltrEntryActFwdEsiVRtrId_Type.__name__ = "TmnxVRtrIDOrZero"
_TIPvXFltrEntryActFwdEsiVRtrId_Object = MibTableColumn
tIPvXFltrEntryActFwdEsiVRtrId = _TIPvXFltrEntryActFwdEsiVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85, 1, 31),
    _TIPvXFltrEntryActFwdEsiVRtrId_Type()
)
tIPvXFltrEntryActFwdEsiVRtrId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPvXFltrEntryActFwdEsiVRtrId.setStatus("current")


class _TIPvXFltrEntryActFwdEsiSFIpType_Type(InetAddressType):
    """Custom type tIPvXFltrEntryActFwdEsiSFIpType based on InetAddressType"""
    defaultValue = 0


_TIPvXFltrEntryActFwdEsiSFIpType_Type.__name__ = "InetAddressType"
_TIPvXFltrEntryActFwdEsiSFIpType_Object = MibTableColumn
tIPvXFltrEntryActFwdEsiSFIpType = _TIPvXFltrEntryActFwdEsiSFIpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85, 1, 32),
    _TIPvXFltrEntryActFwdEsiSFIpType_Type()
)
tIPvXFltrEntryActFwdEsiSFIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPvXFltrEntryActFwdEsiSFIpType.setStatus("current")


class _TIPvXFltrEntryActFwdEsiSFIp_Type(InetAddress):
    """Custom type tIPvXFltrEntryActFwdEsiSFIp based on InetAddress"""
    defaultHexValue = "00000000"

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TIPvXFltrEntryActFwdEsiSFIp_Type.__name__ = "InetAddress"
_TIPvXFltrEntryActFwdEsiSFIp_Object = MibTableColumn
tIPvXFltrEntryActFwdEsiSFIp = _TIPvXFltrEntryActFwdEsiSFIp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85, 1, 33),
    _TIPvXFltrEntryActFwdEsiSFIp_Type()
)
tIPvXFltrEntryActFwdEsiSFIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPvXFltrEntryActFwdEsiSFIp.setStatus("current")


class _TIPvXFltrEntryActFwdEsiVasIf_Type(InterfaceIndexOrZero):
    """Custom type tIPvXFltrEntryActFwdEsiVasIf based on InterfaceIndexOrZero"""
    defaultValue = 0


_TIPvXFltrEntryActFwdEsiVasIf_Type.__name__ = "InterfaceIndexOrZero"
_TIPvXFltrEntryActFwdEsiVasIf_Object = MibTableColumn
tIPvXFltrEntryActFwdEsiVasIf = _TIPvXFltrEntryActFwdEsiVasIf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85, 1, 34),
    _TIPvXFltrEntryActFwdEsiVasIf_Type()
)
tIPvXFltrEntryActFwdEsiVasIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPvXFltrEntryActFwdEsiVasIf.setStatus("current")


class _TIPvXFltrEntryActRateLimit_Type(TFilterEntryActionRateLimit):
    """Custom type tIPvXFltrEntryActRateLimit based on TFilterEntryActionRateLimit"""
    defaultValue = 0


_TIPvXFltrEntryActRateLimit_Type.__name__ = "TFilterEntryActionRateLimit"
_TIPvXFltrEntryActRateLimit_Object = MibTableColumn
tIPvXFltrEntryActRateLimit = _TIPvXFltrEntryActRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85, 1, 35),
    _TIPvXFltrEntryActRateLimit_Type()
)
tIPvXFltrEntryActRateLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPvXFltrEntryActRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    tIPvXFltrEntryActRateLimit.setUnits("kilobps")
_TIPvXFltrEntryActPbrTargetStatus_Type = TFilterPbrTargetStatus
_TIPvXFltrEntryActPbrTargetStatus_Object = MibTableColumn
tIPvXFltrEntryActPbrTargetStatus = _TIPvXFltrEntryActPbrTargetStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85, 1, 36),
    _TIPvXFltrEntryActPbrTargetStatus_Type()
)
tIPvXFltrEntryActPbrTargetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPvXFltrEntryActPbrTargetStatus.setStatus("current")


class _TIPvXFltrEntryActRemarkDSCP_Type(TDSCPNameOrEmpty):
    """Custom type tIPvXFltrEntryActRemarkDSCP based on TDSCPNameOrEmpty"""
    defaultHexValue = ""


_TIPvXFltrEntryActRemarkDSCP_Type.__name__ = "TDSCPNameOrEmpty"
_TIPvXFltrEntryActRemarkDSCP_Object = MibTableColumn
tIPvXFltrEntryActRemarkDSCP = _TIPvXFltrEntryActRemarkDSCP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85, 1, 37),
    _TIPvXFltrEntryActRemarkDSCP_Type()
)
tIPvXFltrEntryActRemarkDSCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPvXFltrEntryActRemarkDSCP.setStatus("current")


class _TIPvXFltrEntryActActionExt_Type(TIPvXFilterEntryActionExt):
    """Custom type tIPvXFltrEntryActActionExt based on TIPvXFilterEntryActionExt"""
    defaultValue = 0


_TIPvXFltrEntryActActionExt_Type.__name__ = "TIPvXFilterEntryActionExt"
_TIPvXFltrEntryActActionExt_Object = MibTableColumn
tIPvXFltrEntryActActionExt = _TIPvXFltrEntryActActionExt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85, 1, 38),
    _TIPvXFltrEntryActActionExt_Type()
)
tIPvXFltrEntryActActionExt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPvXFltrEntryActActionExt.setStatus("current")


class _TIPvXFltrEntryActFwdVprnTgtBgNHT_Type(InetAddressType):
    """Custom type tIPvXFltrEntryActFwdVprnTgtBgNHT based on InetAddressType"""
    defaultValue = 0


_TIPvXFltrEntryActFwdVprnTgtBgNHT_Type.__name__ = "InetAddressType"
_TIPvXFltrEntryActFwdVprnTgtBgNHT_Object = MibTableColumn
tIPvXFltrEntryActFwdVprnTgtBgNHT = _TIPvXFltrEntryActFwdVprnTgtBgNHT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85, 1, 39),
    _TIPvXFltrEntryActFwdVprnTgtBgNHT_Type()
)
tIPvXFltrEntryActFwdVprnTgtBgNHT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPvXFltrEntryActFwdVprnTgtBgNHT.setStatus("current")


class _TIPvXFltrEntryActFwdVprnTgtBgNH_Type(InetAddress):
    """Custom type tIPvXFltrEntryActFwdVprnTgtBgNH based on InetAddress"""
    defaultHexValue = "00000000"

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TIPvXFltrEntryActFwdVprnTgtBgNH_Type.__name__ = "InetAddress"
_TIPvXFltrEntryActFwdVprnTgtBgNH_Object = MibTableColumn
tIPvXFltrEntryActFwdVprnTgtBgNH = _TIPvXFltrEntryActFwdVprnTgtBgNH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85, 1, 40),
    _TIPvXFltrEntryActFwdVprnTgtBgNH_Type()
)
tIPvXFltrEntryActFwdVprnTgtBgNH.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPvXFltrEntryActFwdVprnTgtBgNH.setStatus("current")


class _TIPvXFltrEntryActFwdVprnTgtRtrId_Type(TmnxVRtrIDOrZero):
    """Custom type tIPvXFltrEntryActFwdVprnTgtRtrId based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TIPvXFltrEntryActFwdVprnTgtRtrId_Type.__name__ = "TmnxVRtrIDOrZero"
_TIPvXFltrEntryActFwdVprnTgtRtrId_Object = MibTableColumn
tIPvXFltrEntryActFwdVprnTgtRtrId = _TIPvXFltrEntryActFwdVprnTgtRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85, 1, 41),
    _TIPvXFltrEntryActFwdVprnTgtRtrId_Type()
)
tIPvXFltrEntryActFwdVprnTgtRtrId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPvXFltrEntryActFwdVprnTgtRtrId.setStatus("current")


class _TIPvXFltrEntryActFwdVprnTgtAdPxT_Type(TmnxAddressAndPrefixType):
    """Custom type tIPvXFltrEntryActFwdVprnTgtAdPxT based on TmnxAddressAndPrefixType"""
    defaultValue = 0


_TIPvXFltrEntryActFwdVprnTgtAdPxT_Type.__name__ = "TmnxAddressAndPrefixType"
_TIPvXFltrEntryActFwdVprnTgtAdPxT_Object = MibTableColumn
tIPvXFltrEntryActFwdVprnTgtAdPxT = _TIPvXFltrEntryActFwdVprnTgtAdPxT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85, 1, 42),
    _TIPvXFltrEntryActFwdVprnTgtAdPxT_Type()
)
tIPvXFltrEntryActFwdVprnTgtAdPxT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPvXFltrEntryActFwdVprnTgtAdPxT.setStatus("current")


class _TIPvXFltrEntryActFwdVprnTgtAdPx_Type(TmnxAddressAndPrefixAddress):
    """Custom type tIPvXFltrEntryActFwdVprnTgtAdPx based on TmnxAddressAndPrefixAddress"""
    defaultValue = OctetString("")

    subtypeSpec = TmnxAddressAndPrefixAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TIPvXFltrEntryActFwdVprnTgtAdPx_Type.__name__ = "TmnxAddressAndPrefixAddress"
_TIPvXFltrEntryActFwdVprnTgtAdPx_Object = MibTableColumn
tIPvXFltrEntryActFwdVprnTgtAdPx = _TIPvXFltrEntryActFwdVprnTgtAdPx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85, 1, 43),
    _TIPvXFltrEntryActFwdVprnTgtAdPx_Type()
)
tIPvXFltrEntryActFwdVprnTgtAdPx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPvXFltrEntryActFwdVprnTgtAdPx.setStatus("current")


class _TIPvXFltrEntryActFwdVprnTgtAdPxL_Type(TmnxAddressAndPrefixPrefix):
    """Custom type tIPvXFltrEntryActFwdVprnTgtAdPxL based on TmnxAddressAndPrefixPrefix"""
    defaultValue = 0


_TIPvXFltrEntryActFwdVprnTgtAdPxL_Type.__name__ = "TmnxAddressAndPrefixPrefix"
_TIPvXFltrEntryActFwdVprnTgtAdPxL_Object = MibTableColumn
tIPvXFltrEntryActFwdVprnTgtAdPxL = _TIPvXFltrEntryActFwdVprnTgtAdPxL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85, 1, 44),
    _TIPvXFltrEntryActFwdVprnTgtAdPxL_Type()
)
tIPvXFltrEntryActFwdVprnTgtAdPxL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPvXFltrEntryActFwdVprnTgtAdPxL.setStatus("current")


class _TIPvXFltrEntryActFwdVprnTgtLspId_Type(TmnxVRtrMplsLspID):
    """Custom type tIPvXFltrEntryActFwdVprnTgtLspId based on TmnxVRtrMplsLspID"""
    defaultValue = 0


_TIPvXFltrEntryActFwdVprnTgtLspId_Type.__name__ = "TmnxVRtrMplsLspID"
_TIPvXFltrEntryActFwdVprnTgtLspId_Object = MibTableColumn
tIPvXFltrEntryActFwdVprnTgtLspId = _TIPvXFltrEntryActFwdVprnTgtLspId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85, 1, 45),
    _TIPvXFltrEntryActFwdVprnTgtLspId_Type()
)
tIPvXFltrEntryActFwdVprnTgtLspId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPvXFltrEntryActFwdVprnTgtLspId.setStatus("current")


class _TIPvXFltrEntryActFwdBondingConn_Type(TmnxSubBondingConnIdOrEmpty):
    """Custom type tIPvXFltrEntryActFwdBondingConn based on TmnxSubBondingConnIdOrEmpty"""
    defaultValue = 0


_TIPvXFltrEntryActFwdBondingConn_Type.__name__ = "TmnxSubBondingConnIdOrEmpty"
_TIPvXFltrEntryActFwdBondingConn_Object = MibTableColumn
tIPvXFltrEntryActFwdBondingConn = _TIPvXFltrEntryActFwdBondingConn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85, 1, 46),
    _TIPvXFltrEntryActFwdBondingConn_Type()
)
tIPvXFltrEntryActFwdBondingConn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPvXFltrEntryActFwdBondingConn.setStatus("current")


class _TIPvXFltrEntryActFcName_Type(TFCTypeOrNone):
    """Custom type tIPvXFltrEntryActFcName based on TFCTypeOrNone"""
    defaultValue = -1


_TIPvXFltrEntryActFcName_Type.__name__ = "TFCTypeOrNone"
_TIPvXFltrEntryActFcName_Object = MibTableColumn
tIPvXFltrEntryActFcName = _TIPvXFltrEntryActFcName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85, 1, 47),
    _TIPvXFltrEntryActFcName_Type()
)
tIPvXFltrEntryActFcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPvXFltrEntryActFcName.setStatus("current")


class _TIPvXFltrEntryActFwdGreTun_Type(TNamedItemOrEmpty):
    """Custom type tIPvXFltrEntryActFwdGreTun based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TIPvXFltrEntryActFwdGreTun_Type.__name__ = "TNamedItemOrEmpty"
_TIPvXFltrEntryActFwdGreTun_Object = MibTableColumn
tIPvXFltrEntryActFwdGreTun = _TIPvXFltrEntryActFwdGreTun_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85, 1, 48),
    _TIPvXFltrEntryActFwdGreTun_Type()
)
tIPvXFltrEntryActFwdGreTun.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPvXFltrEntryActFwdGreTun.setStatus("current")


class _TIPvXFltrEntryActCondExpression_Type(OctetString):
    """Custom type tIPvXFltrEntryActCondExpression based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_TIPvXFltrEntryActCondExpression_Type.__name__ = "OctetString"
_TIPvXFltrEntryActCondExpression_Object = MibTableColumn
tIPvXFltrEntryActCondExpression = _TIPvXFltrEntryActCondExpression_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85, 1, 49),
    _TIPvXFltrEntryActCondExpression_Type()
)
tIPvXFltrEntryActCondExpression.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPvXFltrEntryActCondExpression.setStatus("current")


class _TIPvXFltrEntryActCondExpMask_Type(OctetString):
    """Custom type tIPvXFltrEntryActCondExpMask based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_TIPvXFltrEntryActCondExpMask_Type.__name__ = "OctetString"
_TIPvXFltrEntryActCondExpMask_Object = MibTableColumn
tIPvXFltrEntryActCondExpMask = _TIPvXFltrEntryActCondExpMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85, 1, 50),
    _TIPvXFltrEntryActCondExpMask_Type()
)
tIPvXFltrEntryActCondExpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPvXFltrEntryActCondExpMask.setStatus("current")


class _TIPvXFltrEntryActCondOffsetType_Type(Integer32):
    """Custom type tIPvXFltrEntryActCondOffsetType based on Integer32"""
    defaultValue = 0

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
        *(("none", 0),
          ("layer3", 1),
          ("layer4", 2),
          ("data", 3),
          ("dnsQType", 4))
    )


_TIPvXFltrEntryActCondOffsetType_Type.__name__ = "Integer32"
_TIPvXFltrEntryActCondOffsetType_Object = MibTableColumn
tIPvXFltrEntryActCondOffsetType = _TIPvXFltrEntryActCondOffsetType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85, 1, 51),
    _TIPvXFltrEntryActCondOffsetType_Type()
)
tIPvXFltrEntryActCondOffsetType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPvXFltrEntryActCondOffsetType.setStatus("current")


class _TIPvXFltrEntryActCondOffsetVal_Type(Integer32):
    """Custom type tIPvXFltrEntryActCondOffsetVal based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_TIPvXFltrEntryActCondOffsetVal_Type.__name__ = "Integer32"
_TIPvXFltrEntryActCondOffsetVal_Object = MibTableColumn
tIPvXFltrEntryActCondOffsetVal = _TIPvXFltrEntryActCondOffsetVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85, 1, 52),
    _TIPvXFltrEntryActCondOffsetVal_Type()
)
tIPvXFltrEntryActCondOffsetVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPvXFltrEntryActCondOffsetVal.setStatus("current")


class _TIPvXFltrFwdMplsPlcyEndptAddrTp_Type(InetAddressType):
    """Custom type tIPvXFltrFwdMplsPlcyEndptAddrTp based on InetAddressType"""
    defaultValue = 0


_TIPvXFltrFwdMplsPlcyEndptAddrTp_Type.__name__ = "InetAddressType"
_TIPvXFltrFwdMplsPlcyEndptAddrTp_Object = MibTableColumn
tIPvXFltrFwdMplsPlcyEndptAddrTp = _TIPvXFltrFwdMplsPlcyEndptAddrTp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85, 1, 53),
    _TIPvXFltrFwdMplsPlcyEndptAddrTp_Type()
)
tIPvXFltrFwdMplsPlcyEndptAddrTp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPvXFltrFwdMplsPlcyEndptAddrTp.setStatus("current")


class _TIPvXFltrFwdMplsPlcyEndptAddr_Type(InetAddress):
    """Custom type tIPvXFltrFwdMplsPlcyEndptAddr based on InetAddress"""
    defaultHexValue = "00000000"

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TIPvXFltrFwdMplsPlcyEndptAddr_Type.__name__ = "InetAddress"
_TIPvXFltrFwdMplsPlcyEndptAddr_Object = MibTableColumn
tIPvXFltrFwdMplsPlcyEndptAddr = _TIPvXFltrFwdMplsPlcyEndptAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85, 1, 54),
    _TIPvXFltrFwdMplsPlcyEndptAddr_Type()
)
tIPvXFltrFwdMplsPlcyEndptAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPvXFltrFwdMplsPlcyEndptAddr.setStatus("current")


class _TIPvXFltrFwdSrtePlcyEndptAddrTp_Type(InetAddressType):
    """Custom type tIPvXFltrFwdSrtePlcyEndptAddrTp based on InetAddressType"""
    defaultValue = 0


_TIPvXFltrFwdSrtePlcyEndptAddrTp_Type.__name__ = "InetAddressType"
_TIPvXFltrFwdSrtePlcyEndptAddrTp_Object = MibTableColumn
tIPvXFltrFwdSrtePlcyEndptAddrTp = _TIPvXFltrFwdSrtePlcyEndptAddrTp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85, 1, 55),
    _TIPvXFltrFwdSrtePlcyEndptAddrTp_Type()
)
tIPvXFltrFwdSrtePlcyEndptAddrTp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPvXFltrFwdSrtePlcyEndptAddrTp.setStatus("current")


class _TIPvXFltrFwdSrtePlcyEndptAddr_Type(InetAddress):
    """Custom type tIPvXFltrFwdSrtePlcyEndptAddr based on InetAddress"""
    defaultHexValue = "00000000"

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TIPvXFltrFwdSrtePlcyEndptAddr_Type.__name__ = "InetAddress"
_TIPvXFltrFwdSrtePlcyEndptAddr_Object = MibTableColumn
tIPvXFltrFwdSrtePlcyEndptAddr = _TIPvXFltrFwdSrtePlcyEndptAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85, 1, 56),
    _TIPvXFltrFwdSrtePlcyEndptAddr_Type()
)
tIPvXFltrFwdSrtePlcyEndptAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPvXFltrFwdSrtePlcyEndptAddr.setStatus("current")
_TIPvXFltrFwdSrtePlcyColor_Type = Unsigned32
_TIPvXFltrFwdSrtePlcyColor_Object = MibTableColumn
tIPvXFltrFwdSrtePlcyColor = _TIPvXFltrFwdSrtePlcyColor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85, 1, 57),
    _TIPvXFltrFwdSrtePlcyColor_Type()
)
tIPvXFltrFwdSrtePlcyColor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPvXFltrFwdSrtePlcyColor.setStatus("current")


class _TIPvXFltrActL2AwareNatBypass_Type(TruthValue):
    """Custom type tIPvXFltrActL2AwareNatBypass based on TruthValue"""
    defaultValue = 2


_TIPvXFltrActL2AwareNatBypass_Type.__name__ = "TruthValue"
_TIPvXFltrActL2AwareNatBypass_Object = MibTableColumn
tIPvXFltrActL2AwareNatBypass = _TIPvXFltrActL2AwareNatBypass_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 85, 1, 58),
    _TIPvXFltrActL2AwareNatBypass_Type()
)
tIPvXFltrActL2AwareNatBypass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPvXFltrActL2AwareNatBypass.setStatus("current")
_TFltrEntryStatTable_Object = MibTable
tFltrEntryStatTable = _TFltrEntryStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 86)
)
if mibBuilder.loadTexts:
    tFltrEntryStatTable.setStatus("current")
_TFltrEntryStatEntry_Object = MibTableRow
tFltrEntryStatEntry = _TFltrEntryStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 86, 1)
)
tFltrEntryStatEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tFltrEntryStatFltrType"),
    (0, "TIMETRA-FILTER-MIB", "tFltrEntryStatFltrId"),
    (0, "TIMETRA-FILTER-MIB", "tFltrEntryStatFltrEntryId"),
)
if mibBuilder.loadTexts:
    tFltrEntryStatEntry.setStatus("current")


class _TFltrEntryStatFltrType_Type(TFilterType):
    """Custom type tFltrEntryStatFltrType based on TFilterType"""
    subtypeSpec = TFilterType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("fltrtypeselIp", 1),
          ("fltrtypeselMac", 2),
          ("fltrtypeselIpv6", 4))
    )


_TFltrEntryStatFltrType_Type.__name__ = "TFilterType"
_TFltrEntryStatFltrType_Object = MibTableColumn
tFltrEntryStatFltrType = _TFltrEntryStatFltrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 86, 1, 1),
    _TFltrEntryStatFltrType_Type()
)
tFltrEntryStatFltrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFltrEntryStatFltrType.setStatus("current")
_TFltrEntryStatFltrId_Type = TAnyFilterID
_TFltrEntryStatFltrId_Object = MibTableColumn
tFltrEntryStatFltrId = _TFltrEntryStatFltrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 86, 1, 2),
    _TFltrEntryStatFltrId_Type()
)
tFltrEntryStatFltrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFltrEntryStatFltrId.setStatus("current")
_TFltrEntryStatFltrEntryId_Type = TEntryId
_TFltrEntryStatFltrEntryId_Object = MibTableColumn
tFltrEntryStatFltrEntryId = _TFltrEntryStatFltrEntryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 86, 1, 3),
    _TFltrEntryStatFltrEntryId_Type()
)
tFltrEntryStatFltrEntryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFltrEntryStatFltrEntryId.setStatus("current")
_TFltrEntryStatIngHitCnt_Type = Counter64
_TFltrEntryStatIngHitCnt_Object = MibTableColumn
tFltrEntryStatIngHitCnt = _TFltrEntryStatIngHitCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 86, 1, 4),
    _TFltrEntryStatIngHitCnt_Type()
)
tFltrEntryStatIngHitCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrEntryStatIngHitCnt.setStatus("current")
_TFltrEntryStatIngHitCntB_Type = Counter64
_TFltrEntryStatIngHitCntB_Object = MibTableColumn
tFltrEntryStatIngHitCntB = _TFltrEntryStatIngHitCntB_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 86, 1, 5),
    _TFltrEntryStatIngHitCntB_Type()
)
tFltrEntryStatIngHitCntB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrEntryStatIngHitCntB.setStatus("current")
_TFltrEntryStatEgrHitCnt_Type = Counter64
_TFltrEntryStatEgrHitCnt_Object = MibTableColumn
tFltrEntryStatEgrHitCnt = _TFltrEntryStatEgrHitCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 86, 1, 6),
    _TFltrEntryStatEgrHitCnt_Type()
)
tFltrEntryStatEgrHitCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrEntryStatEgrHitCnt.setStatus("current")
_TFltrEntryStatEgrHitCntB_Type = Counter64
_TFltrEntryStatEgrHitCntB_Object = MibTableColumn
tFltrEntryStatEgrHitCntB = _TFltrEntryStatEgrHitCntB_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 86, 1, 7),
    _TFltrEntryStatEgrHitCntB_Type()
)
tFltrEntryStatEgrHitCntB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrEntryStatEgrHitCntB.setStatus("current")
_TFltrEntryStatRateLmtIngHitCnt_Type = Counter64
_TFltrEntryStatRateLmtIngHitCnt_Object = MibTableColumn
tFltrEntryStatRateLmtIngHitCnt = _TFltrEntryStatRateLmtIngHitCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 86, 1, 8),
    _TFltrEntryStatRateLmtIngHitCnt_Type()
)
tFltrEntryStatRateLmtIngHitCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrEntryStatRateLmtIngHitCnt.setStatus("current")
_TFltrEntryStatRateLmtIngHitCntB_Type = Counter64
_TFltrEntryStatRateLmtIngHitCntB_Object = MibTableColumn
tFltrEntryStatRateLmtIngHitCntB = _TFltrEntryStatRateLmtIngHitCntB_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 86, 1, 9),
    _TFltrEntryStatRateLmtIngHitCntB_Type()
)
tFltrEntryStatRateLmtIngHitCntB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrEntryStatRateLmtIngHitCntB.setStatus("current")
_TFltrEntryStatRateLmtIngDrop_Type = Counter64
_TFltrEntryStatRateLmtIngDrop_Object = MibTableColumn
tFltrEntryStatRateLmtIngDrop = _TFltrEntryStatRateLmtIngDrop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 86, 1, 10),
    _TFltrEntryStatRateLmtIngDrop_Type()
)
tFltrEntryStatRateLmtIngDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrEntryStatRateLmtIngDrop.setStatus("current")
_TFltrEntryStatRateLmtIngDropB_Type = Counter64
_TFltrEntryStatRateLmtIngDropB_Object = MibTableColumn
tFltrEntryStatRateLmtIngDropB = _TFltrEntryStatRateLmtIngDropB_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 86, 1, 11),
    _TFltrEntryStatRateLmtIngDropB_Type()
)
tFltrEntryStatRateLmtIngDropB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrEntryStatRateLmtIngDropB.setStatus("current")
_TFltrEntryStatRateLmtIngFwd_Type = Counter64
_TFltrEntryStatRateLmtIngFwd_Object = MibTableColumn
tFltrEntryStatRateLmtIngFwd = _TFltrEntryStatRateLmtIngFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 86, 1, 12),
    _TFltrEntryStatRateLmtIngFwd_Type()
)
tFltrEntryStatRateLmtIngFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrEntryStatRateLmtIngFwd.setStatus("current")
_TFltrEntryStatRateLmtIngFwdB_Type = Counter64
_TFltrEntryStatRateLmtIngFwdB_Object = MibTableColumn
tFltrEntryStatRateLmtIngFwdB = _TFltrEntryStatRateLmtIngFwdB_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 86, 1, 13),
    _TFltrEntryStatRateLmtIngFwdB_Type()
)
tFltrEntryStatRateLmtIngFwdB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrEntryStatRateLmtIngFwdB.setStatus("current")
_TFltrEntryStatRateLmtEgrHitCnt_Type = Counter64
_TFltrEntryStatRateLmtEgrHitCnt_Object = MibTableColumn
tFltrEntryStatRateLmtEgrHitCnt = _TFltrEntryStatRateLmtEgrHitCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 86, 1, 14),
    _TFltrEntryStatRateLmtEgrHitCnt_Type()
)
tFltrEntryStatRateLmtEgrHitCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrEntryStatRateLmtEgrHitCnt.setStatus("current")
_TFltrEntryStatRateLmtEgrHitCntB_Type = Counter64
_TFltrEntryStatRateLmtEgrHitCntB_Object = MibTableColumn
tFltrEntryStatRateLmtEgrHitCntB = _TFltrEntryStatRateLmtEgrHitCntB_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 86, 1, 15),
    _TFltrEntryStatRateLmtEgrHitCntB_Type()
)
tFltrEntryStatRateLmtEgrHitCntB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrEntryStatRateLmtEgrHitCntB.setStatus("current")
_TFltrEntryStatRateLmtEgrDrop_Type = Counter64
_TFltrEntryStatRateLmtEgrDrop_Object = MibTableColumn
tFltrEntryStatRateLmtEgrDrop = _TFltrEntryStatRateLmtEgrDrop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 86, 1, 16),
    _TFltrEntryStatRateLmtEgrDrop_Type()
)
tFltrEntryStatRateLmtEgrDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrEntryStatRateLmtEgrDrop.setStatus("current")
_TFltrEntryStatRateLmtEgrDropB_Type = Counter64
_TFltrEntryStatRateLmtEgrDropB_Object = MibTableColumn
tFltrEntryStatRateLmtEgrDropB = _TFltrEntryStatRateLmtEgrDropB_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 86, 1, 17),
    _TFltrEntryStatRateLmtEgrDropB_Type()
)
tFltrEntryStatRateLmtEgrDropB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrEntryStatRateLmtEgrDropB.setStatus("current")
_TFltrEntryStatRateLmtEgrFwd_Type = Counter64
_TFltrEntryStatRateLmtEgrFwd_Object = MibTableColumn
tFltrEntryStatRateLmtEgrFwd = _TFltrEntryStatRateLmtEgrFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 86, 1, 18),
    _TFltrEntryStatRateLmtEgrFwd_Type()
)
tFltrEntryStatRateLmtEgrFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrEntryStatRateLmtEgrFwd.setStatus("current")
_TFltrEntryStatRateLmtEgrFwdB_Type = Counter64
_TFltrEntryStatRateLmtEgrFwdB_Object = MibTableColumn
tFltrEntryStatRateLmtEgrFwdB = _TFltrEntryStatRateLmtEgrFwdB_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 86, 1, 19),
    _TFltrEntryStatRateLmtEgrFwdB_Type()
)
tFltrEntryStatRateLmtEgrFwdB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrEntryStatRateLmtEgrFwdB.setStatus("current")
_TFltrPrefListInfoTable_Object = MibTable
tFltrPrefListInfoTable = _TFltrPrefListInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 87)
)
if mibBuilder.loadTexts:
    tFltrPrefListInfoTable.setStatus("current")
_TFltrPrefListInfoEntry_Object = MibTableRow
tFltrPrefListInfoEntry = _TFltrPrefListInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 87, 1)
)
tFltrPrefListInfoEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tFilterPrefixListType"),
    (0, "TIMETRA-FILTER-MIB", "tFilterPrefixListName"),
    (0, "TIMETRA-FILTER-MIB", "tFltrPrefListInfoPrefixSrc"),
    (0, "TIMETRA-FILTER-MIB", "tFltrPrefListInfoPrefixSrcIndex"),
    (0, "TIMETRA-FILTER-MIB", "tFltrPrefListInfoPrefixType"),
    (0, "TIMETRA-FILTER-MIB", "tFltrPrefListInfoPrefix"),
    (0, "TIMETRA-FILTER-MIB", "tFltrPrefListInfoPrefixLen"),
)
if mibBuilder.loadTexts:
    tFltrPrefListInfoEntry.setStatus("current")


class _TFltrPrefListInfoPrefixSrc_Type(Integer32):
    """Custom type tFltrPrefListInfoPrefixSrc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("prefixConfig", 0),
          ("applyPathBgpPeer", 1),
          ("prefixConfigGenerated", 4))
    )


_TFltrPrefListInfoPrefixSrc_Type.__name__ = "Integer32"
_TFltrPrefListInfoPrefixSrc_Object = MibTableColumn
tFltrPrefListInfoPrefixSrc = _TFltrPrefListInfoPrefixSrc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 87, 1, 1),
    _TFltrPrefListInfoPrefixSrc_Type()
)
tFltrPrefListInfoPrefixSrc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFltrPrefListInfoPrefixSrc.setStatus("current")
_TFltrPrefListInfoPrefixSrcIndex_Type = Unsigned32
_TFltrPrefListInfoPrefixSrcIndex_Object = MibTableColumn
tFltrPrefListInfoPrefixSrcIndex = _TFltrPrefListInfoPrefixSrcIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 87, 1, 2),
    _TFltrPrefListInfoPrefixSrcIndex_Type()
)
tFltrPrefListInfoPrefixSrcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFltrPrefListInfoPrefixSrcIndex.setStatus("current")
_TFltrPrefListInfoPrefixType_Type = InetAddressType
_TFltrPrefListInfoPrefixType_Object = MibTableColumn
tFltrPrefListInfoPrefixType = _TFltrPrefListInfoPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 87, 1, 3),
    _TFltrPrefListInfoPrefixType_Type()
)
tFltrPrefListInfoPrefixType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFltrPrefListInfoPrefixType.setStatus("current")


class _TFltrPrefListInfoPrefix_Type(InetAddress):
    """Custom type tFltrPrefListInfoPrefix based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TFltrPrefListInfoPrefix_Type.__name__ = "InetAddress"
_TFltrPrefListInfoPrefix_Object = MibTableColumn
tFltrPrefListInfoPrefix = _TFltrPrefListInfoPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 87, 1, 4),
    _TFltrPrefListInfoPrefix_Type()
)
tFltrPrefListInfoPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFltrPrefListInfoPrefix.setStatus("current")
_TFltrPrefListInfoPrefixLen_Type = InetAddressPrefixLength
_TFltrPrefListInfoPrefixLen_Object = MibTableColumn
tFltrPrefListInfoPrefixLen = _TFltrPrefListInfoPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 87, 1, 5),
    _TFltrPrefListInfoPrefixLen_Type()
)
tFltrPrefListInfoPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFltrPrefListInfoPrefixLen.setStatus("current")


class _TFltrPrefListInfoPrefixOwner_Type(Integer32):
    """Custom type tFltrPrefListInfoPrefixOwner based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("config", 0),
          ("applyPath", 1),
          ("prefixExclude", 2))
    )


_TFltrPrefListInfoPrefixOwner_Type.__name__ = "Integer32"
_TFltrPrefListInfoPrefixOwner_Object = MibTableColumn
tFltrPrefListInfoPrefixOwner = _TFltrPrefListInfoPrefixOwner_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 87, 1, 6),
    _TFltrPrefListInfoPrefixOwner_Type()
)
tFltrPrefListInfoPrefixOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrPrefListInfoPrefixOwner.setStatus("current")
_TFltrPrefListInfoPrefixProg_Type = TruthValue
_TFltrPrefListInfoPrefixProg_Object = MibTableColumn
tFltrPrefListInfoPrefixProg = _TFltrPrefListInfoPrefixProg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 87, 1, 7),
    _TFltrPrefListInfoPrefixProg_Type()
)
tFltrPrefListInfoPrefixProg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrPrefListInfoPrefixProg.setStatus("current")
_TFilterEmbFlowspecEntryInfoTable_Object = MibTable
tFilterEmbFlowspecEntryInfoTable = _TFilterEmbFlowspecEntryInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 94)
)
if mibBuilder.loadTexts:
    tFilterEmbFlowspecEntryInfoTable.setStatus("current")
_TFilterEmbFlowspecEntryInfoEntry_Object = MibTableRow
tFilterEmbFlowspecEntryInfoEntry = _TFilterEmbFlowspecEntryInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 94, 1)
)
tFilterEmbFlowspecEntryInfoEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tFilterEmbedFlowspecFilterType"),
    (0, "TIMETRA-FILTER-MIB", "tFilterEmbedFlowspecInsertFltrId"),
    (0, "TIMETRA-FILTER-MIB", "tFilterEmbedFlowspecEmbFltrId"),
    (0, "TIMETRA-FILTER-MIB", "tFilterEmbedFlowspecEmbEntryId"),
)
if mibBuilder.loadTexts:
    tFilterEmbFlowspecEntryInfoEntry.setStatus("current")
_TFilterEmbedFlowspecEmbFltrId_Type = TAnyFilterID
_TFilterEmbedFlowspecEmbFltrId_Object = MibTableColumn
tFilterEmbedFlowspecEmbFltrId = _TFilterEmbedFlowspecEmbFltrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 94, 1, 1),
    _TFilterEmbedFlowspecEmbFltrId_Type()
)
tFilterEmbedFlowspecEmbFltrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterEmbedFlowspecEmbFltrId.setStatus("current")
_TFilterEmbedFlowspecEmbEntryId_Type = TEntryId
_TFilterEmbedFlowspecEmbEntryId_Object = MibTableColumn
tFilterEmbedFlowspecEmbEntryId = _TFilterEmbedFlowspecEmbEntryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 94, 1, 2),
    _TFilterEmbedFlowspecEmbEntryId_Type()
)
tFilterEmbedFlowspecEmbEntryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterEmbedFlowspecEmbEntryId.setStatus("current")
_TFilterEmbedFlowspecInsEntryId_Type = TAnyEntryId
_TFilterEmbedFlowspecInsEntryId_Object = MibTableColumn
tFilterEmbedFlowspecInsEntryId = _TFilterEmbedFlowspecInsEntryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 94, 1, 3),
    _TFilterEmbedFlowspecInsEntryId_Type()
)
tFilterEmbedFlowspecInsEntryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterEmbedFlowspecInsEntryId.setStatus("current")
_TFilterEmbedFlowspecEntryOpState_Type = TmnxFltrEmbeddedEntryState
_TFilterEmbedFlowspecEntryOpState_Object = MibTableColumn
tFilterEmbedFlowspecEntryOpState = _TFilterEmbedFlowspecEntryOpState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 94, 1, 4),
    _TFilterEmbedFlowspecEntryOpState_Type()
)
tFilterEmbedFlowspecEntryOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterEmbedFlowspecEntryOpState.setStatus("current")
_TFilterRPlcyBindingTableLastChg_Type = TimeStamp
_TFilterRPlcyBindingTableLastChg_Object = MibScalar
tFilterRPlcyBindingTableLastChg = _TFilterRPlcyBindingTableLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 95),
    _TFilterRPlcyBindingTableLastChg_Type()
)
tFilterRPlcyBindingTableLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRPlcyBindingTableLastChg.setStatus("current")
_TFilterRPlcyBindingTable_Object = MibTable
tFilterRPlcyBindingTable = _TFilterRPlcyBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 96)
)
if mibBuilder.loadTexts:
    tFilterRPlcyBindingTable.setStatus("current")
_TFilterRPlcyBindingEntry_Object = MibTableRow
tFilterRPlcyBindingEntry = _TFilterRPlcyBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 96, 1)
)
tFilterRPlcyBindingEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tFilterRPlcyBindingName"),
)
if mibBuilder.loadTexts:
    tFilterRPlcyBindingEntry.setStatus("current")
_TFilterRPlcyBindingName_Type = TNamedItem
_TFilterRPlcyBindingName_Object = MibTableColumn
tFilterRPlcyBindingName = _TFilterRPlcyBindingName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 96, 1, 1),
    _TFilterRPlcyBindingName_Type()
)
tFilterRPlcyBindingName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFilterRPlcyBindingName.setStatus("current")
_TFilterRPlcyBindingLastChange_Type = TimeStamp
_TFilterRPlcyBindingLastChange_Object = MibTableColumn
tFilterRPlcyBindingLastChange = _TFilterRPlcyBindingLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 96, 1, 2),
    _TFilterRPlcyBindingLastChange_Type()
)
tFilterRPlcyBindingLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRPlcyBindingLastChange.setStatus("current")
_TFilterRPlcyBindingRowStatus_Type = RowStatus
_TFilterRPlcyBindingRowStatus_Object = MibTableColumn
tFilterRPlcyBindingRowStatus = _TFilterRPlcyBindingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 96, 1, 3),
    _TFilterRPlcyBindingRowStatus_Type()
)
tFilterRPlcyBindingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRPlcyBindingRowStatus.setStatus("current")


class _TFilterRPlcyBindingOperator_Type(TFilterRPBindingOperator):
    """Custom type tFilterRPlcyBindingOperator based on TFilterRPBindingOperator"""
    defaultValue = 0


_TFilterRPlcyBindingOperator_Type.__name__ = "TFilterRPBindingOperator"
_TFilterRPlcyBindingOperator_Object = MibTableColumn
tFilterRPlcyBindingOperator = _TFilterRPlcyBindingOperator_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 96, 1, 4),
    _TFilterRPlcyBindingOperator_Type()
)
tFilterRPlcyBindingOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRPlcyBindingOperator.setStatus("current")
_TFilterRPlcyBindingOperState_Type = TmnxOperState
_TFilterRPlcyBindingOperState_Object = MibTableColumn
tFilterRPlcyBindingOperState = _TFilterRPlcyBindingOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 96, 1, 5),
    _TFilterRPlcyBindingOperState_Type()
)
tFilterRPlcyBindingOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRPlcyBindingOperState.setStatus("current")
_TFilterRPlcyBindingDestTableLCh_Type = TimeStamp
_TFilterRPlcyBindingDestTableLCh_Object = MibScalar
tFilterRPlcyBindingDestTableLCh = _TFilterRPlcyBindingDestTableLCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 97),
    _TFilterRPlcyBindingDestTableLCh_Type()
)
tFilterRPlcyBindingDestTableLCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRPlcyBindingDestTableLCh.setStatus("current")
_TFilterRPlcyBindingDestTable_Object = MibTable
tFilterRPlcyBindingDestTable = _TFilterRPlcyBindingDestTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 98)
)
if mibBuilder.loadTexts:
    tFilterRPlcyBindingDestTable.setStatus("current")
_TFilterRPlcyBindingDestEntry_Object = MibTableRow
tFilterRPlcyBindingDestEntry = _TFilterRPlcyBindingDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 98, 1)
)
tFilterRPlcyBindingDestEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tFilterRPlcyBindingName"),
    (0, "TIMETRA-FILTER-MIB", "tFilterRedirectPolicy"),
    (0, "TIMETRA-FILTER-MIB", "tFltrRPDstAddrType"),
    (0, "TIMETRA-FILTER-MIB", "tFltrRPDstAddr"),
)
if mibBuilder.loadTexts:
    tFilterRPlcyBindingDestEntry.setStatus("current")
_TFilterRPlcyBindingDestRowStatus_Type = RowStatus
_TFilterRPlcyBindingDestRowStatus_Object = MibTableColumn
tFilterRPlcyBindingDestRowStatus = _TFilterRPlcyBindingDestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 98, 1, 1),
    _TFilterRPlcyBindingDestRowStatus_Type()
)
tFilterRPlcyBindingDestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterRPlcyBindingDestRowStatus.setStatus("current")
_TFilterRPlcyBindingDestOperState_Type = TmnxOperState
_TFilterRPlcyBindingDestOperState_Object = MibTableColumn
tFilterRPlcyBindingDestOperState = _TFilterRPlcyBindingDestOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 98, 1, 5),
    _TFilterRPlcyBindingDestOperState_Type()
)
tFilterRPlcyBindingDestOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFilterRPlcyBindingDestOperState.setStatus("current")
_TFltrGreTunTempTableLastChg_Type = TimeStamp
_TFltrGreTunTempTableLastChg_Object = MibScalar
tFltrGreTunTempTableLastChg = _TFltrGreTunTempTableLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 99),
    _TFltrGreTunTempTableLastChg_Type()
)
tFltrGreTunTempTableLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrGreTunTempTableLastChg.setStatus("current")
_TFltrGreTunTempTable_Object = MibTable
tFltrGreTunTempTable = _TFltrGreTunTempTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 100)
)
if mibBuilder.loadTexts:
    tFltrGreTunTempTable.setStatus("current")
_TFltrGreTunTempEntry_Object = MibTableRow
tFltrGreTunTempEntry = _TFltrGreTunTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 100, 1)
)
tFltrGreTunTempEntry.setIndexNames(
    (1, "TIMETRA-FILTER-MIB", "tFltrGreTunTempName"),
)
if mibBuilder.loadTexts:
    tFltrGreTunTempEntry.setStatus("current")
_TFltrGreTunTempName_Type = TNamedItem
_TFltrGreTunTempName_Object = MibTableColumn
tFltrGreTunTempName = _TFltrGreTunTempName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 100, 1, 1),
    _TFltrGreTunTempName_Type()
)
tFltrGreTunTempName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFltrGreTunTempName.setStatus("current")
_TFltrGreTunTempRowStatus_Type = RowStatus
_TFltrGreTunTempRowStatus_Object = MibTableColumn
tFltrGreTunTempRowStatus = _TFltrGreTunTempRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 100, 1, 2),
    _TFltrGreTunTempRowStatus_Type()
)
tFltrGreTunTempRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFltrGreTunTempRowStatus.setStatus("current")
_TFltrGreTunTempLastChanged_Type = TimeStamp
_TFltrGreTunTempLastChanged_Object = MibTableColumn
tFltrGreTunTempLastChanged = _TFltrGreTunTempLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 100, 1, 3),
    _TFltrGreTunTempLastChanged_Type()
)
tFltrGreTunTempLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrGreTunTempLastChanged.setStatus("current")


class _TFltrGreTunTempDescription_Type(TItemDescription):
    """Custom type tFltrGreTunTempDescription based on TItemDescription"""
    defaultHexValue = ""


_TFltrGreTunTempDescription_Type.__name__ = "TItemDescription"
_TFltrGreTunTempDescription_Object = MibTableColumn
tFltrGreTunTempDescription = _TFltrGreTunTempDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 100, 1, 4),
    _TFltrGreTunTempDescription_Type()
)
tFltrGreTunTempDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFltrGreTunTempDescription.setStatus("current")


class _TFltrGreTunTempIpv4SrcAddr_Type(IpAddress):
    """Custom type tFltrGreTunTempIpv4SrcAddr based on IpAddress"""
    defaultHexValue = "00000000"


_TFltrGreTunTempIpv4SrcAddr_Type.__name__ = "IpAddress"
_TFltrGreTunTempIpv4SrcAddr_Object = MibTableColumn
tFltrGreTunTempIpv4SrcAddr = _TFltrGreTunTempIpv4SrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 100, 1, 5),
    _TFltrGreTunTempIpv4SrcAddr_Type()
)
tFltrGreTunTempIpv4SrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFltrGreTunTempIpv4SrcAddr.setStatus("current")


class _TFltrGreTunTempIpv4GreKeyIfIndex_Type(TruthValue):
    """Custom type tFltrGreTunTempIpv4GreKeyIfIndex based on TruthValue"""
    defaultValue = 2


_TFltrGreTunTempIpv4GreKeyIfIndex_Type.__name__ = "TruthValue"
_TFltrGreTunTempIpv4GreKeyIfIndex_Object = MibTableColumn
tFltrGreTunTempIpv4GreKeyIfIndex = _TFltrGreTunTempIpv4GreKeyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 100, 1, 6),
    _TFltrGreTunTempIpv4GreKeyIfIndex_Type()
)
tFltrGreTunTempIpv4GreKeyIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFltrGreTunTempIpv4GreKeyIfIndex.setStatus("current")


class _TFltrGreTunTempIpv4SkipTllDecr_Type(TruthValue):
    """Custom type tFltrGreTunTempIpv4SkipTllDecr based on TruthValue"""
    defaultValue = 2


_TFltrGreTunTempIpv4SkipTllDecr_Type.__name__ = "TruthValue"
_TFltrGreTunTempIpv4SkipTllDecr_Object = MibTableColumn
tFltrGreTunTempIpv4SkipTllDecr = _TFltrGreTunTempIpv4SkipTllDecr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 100, 1, 7),
    _TFltrGreTunTempIpv4SkipTllDecr_Type()
)
tFltrGreTunTempIpv4SkipTllDecr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFltrGreTunTempIpv4SkipTllDecr.setStatus("current")
_TFltrGreTunTempIpv4DstTblLstChg_Type = TimeStamp
_TFltrGreTunTempIpv4DstTblLstChg_Object = MibScalar
tFltrGreTunTempIpv4DstTblLstChg = _TFltrGreTunTempIpv4DstTblLstChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 101),
    _TFltrGreTunTempIpv4DstTblLstChg_Type()
)
tFltrGreTunTempIpv4DstTblLstChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrGreTunTempIpv4DstTblLstChg.setStatus("current")
_TFltrGreTunTempIpv4DstTable_Object = MibTable
tFltrGreTunTempIpv4DstTable = _TFltrGreTunTempIpv4DstTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 102)
)
if mibBuilder.loadTexts:
    tFltrGreTunTempIpv4DstTable.setStatus("current")
_TFltrGreTunTempIpv4DstEntry_Object = MibTableRow
tFltrGreTunTempIpv4DstEntry = _TFltrGreTunTempIpv4DstEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 102, 1)
)
tFltrGreTunTempIpv4DstEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tFltrGreTunTempName"),
    (0, "TIMETRA-FILTER-MIB", "tFltrGreTunTempIpv4DstAddr"),
)
if mibBuilder.loadTexts:
    tFltrGreTunTempIpv4DstEntry.setStatus("current")
_TFltrGreTunTempIpv4DstAddr_Type = IpAddress
_TFltrGreTunTempIpv4DstAddr_Object = MibTableColumn
tFltrGreTunTempIpv4DstAddr = _TFltrGreTunTempIpv4DstAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 102, 1, 1),
    _TFltrGreTunTempIpv4DstAddr_Type()
)
tFltrGreTunTempIpv4DstAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFltrGreTunTempIpv4DstAddr.setStatus("current")
_TFltrGreTunTempIpv4DstRowStatus_Type = RowStatus
_TFltrGreTunTempIpv4DstRowStatus_Object = MibTableColumn
tFltrGreTunTempIpv4DstRowStatus = _TFltrGreTunTempIpv4DstRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 102, 1, 2),
    _TFltrGreTunTempIpv4DstRowStatus_Type()
)
tFltrGreTunTempIpv4DstRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFltrGreTunTempIpv4DstRowStatus.setStatus("current")
_TFltrGreTunTempIpv4DstLstChg_Type = TimeStamp
_TFltrGreTunTempIpv4DstLstChg_Object = MibTableColumn
tFltrGreTunTempIpv4DstLstChg = _TFltrGreTunTempIpv4DstLstChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 102, 1, 3),
    _TFltrGreTunTempIpv4DstLstChg_Type()
)
tFltrGreTunTempIpv4DstLstChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrGreTunTempIpv4DstLstChg.setStatus("current")
_TFltrPrefListPrefExclTblLstChg_Type = TimeStamp
_TFltrPrefListPrefExclTblLstChg_Object = MibScalar
tFltrPrefListPrefExclTblLstChg = _TFltrPrefListPrefExclTblLstChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 103),
    _TFltrPrefListPrefExclTblLstChg_Type()
)
tFltrPrefListPrefExclTblLstChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrPrefListPrefExclTblLstChg.setStatus("current")
_TFltrPrefListPrefExclTable_Object = MibTable
tFltrPrefListPrefExclTable = _TFltrPrefListPrefExclTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 104)
)
if mibBuilder.loadTexts:
    tFltrPrefListPrefExclTable.setStatus("current")
_TFltrPrefListPrefExclEntry_Object = MibTableRow
tFltrPrefListPrefExclEntry = _TFltrPrefListPrefExclEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 104, 1)
)
tFltrPrefListPrefExclEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tFilterPrefixListType"),
    (0, "TIMETRA-FILTER-MIB", "tFilterPrefixListName"),
    (0, "TIMETRA-FILTER-MIB", "tFltrPrefListPrefExclPrefType"),
    (0, "TIMETRA-FILTER-MIB", "tFltrPrefListPrefExclPref"),
    (0, "TIMETRA-FILTER-MIB", "tFltrPrefListPrefExclPrefLen"),
)
if mibBuilder.loadTexts:
    tFltrPrefListPrefExclEntry.setStatus("current")
_TFltrPrefListPrefExclPrefType_Type = TmnxAddressAndPrefixType
_TFltrPrefListPrefExclPrefType_Object = MibTableColumn
tFltrPrefListPrefExclPrefType = _TFltrPrefListPrefExclPrefType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 104, 1, 1),
    _TFltrPrefListPrefExclPrefType_Type()
)
tFltrPrefListPrefExclPrefType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFltrPrefListPrefExclPrefType.setStatus("current")


class _TFltrPrefListPrefExclPref_Type(TmnxAddressAndPrefixAddress):
    """Custom type tFltrPrefListPrefExclPref based on TmnxAddressAndPrefixAddress"""
    subtypeSpec = TmnxAddressAndPrefixAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TFltrPrefListPrefExclPref_Type.__name__ = "TmnxAddressAndPrefixAddress"
_TFltrPrefListPrefExclPref_Object = MibTableColumn
tFltrPrefListPrefExclPref = _TFltrPrefListPrefExclPref_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 104, 1, 2),
    _TFltrPrefListPrefExclPref_Type()
)
tFltrPrefListPrefExclPref.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFltrPrefListPrefExclPref.setStatus("current")
_TFltrPrefListPrefExclPrefLen_Type = TmnxAddressAndPrefixPrefix
_TFltrPrefListPrefExclPrefLen_Object = MibTableColumn
tFltrPrefListPrefExclPrefLen = _TFltrPrefListPrefExclPrefLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 104, 1, 3),
    _TFltrPrefListPrefExclPrefLen_Type()
)
tFltrPrefListPrefExclPrefLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFltrPrefListPrefExclPrefLen.setStatus("current")
_TFltrPrefListPrefExclRowStatus_Type = RowStatus
_TFltrPrefListPrefExclRowStatus_Object = MibTableColumn
tFltrPrefListPrefExclRowStatus = _TFltrPrefListPrefExclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 104, 1, 4),
    _TFltrPrefListPrefExclRowStatus_Type()
)
tFltrPrefListPrefExclRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFltrPrefListPrefExclRowStatus.setStatus("current")
_TFltrPrefListPrefExclLastChg_Type = TimeStamp
_TFltrPrefListPrefExclLastChg_Object = MibTableColumn
tFltrPrefListPrefExclLastChg = _TFltrPrefListPrefExclLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 104, 1, 5),
    _TFltrPrefListPrefExclLastChg_Type()
)
tFltrPrefListPrefExclLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrPrefListPrefExclLastChg.setStatus("current")
_FltrMdAutoIdGroup_ObjectIdentity = ObjectIdentity
fltrMdAutoIdGroup = _FltrMdAutoIdGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 105)
)


class _FltrMdAutoIdFilterRangeStart_Type(TFilterID):
    """Custom type fltrMdAutoIdFilterRangeStart based on TFilterID"""
    defaultValue = 0


_FltrMdAutoIdFilterRangeStart_Type.__name__ = "TFilterID"
_FltrMdAutoIdFilterRangeStart_Object = MibScalar
fltrMdAutoIdFilterRangeStart = _FltrMdAutoIdFilterRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 105, 1),
    _FltrMdAutoIdFilterRangeStart_Type()
)
fltrMdAutoIdFilterRangeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltrMdAutoIdFilterRangeStart.setStatus("current")


class _FltrMdAutoIdFilterRangeEnd_Type(TFilterID):
    """Custom type fltrMdAutoIdFilterRangeEnd based on TFilterID"""
    defaultValue = 0


_FltrMdAutoIdFilterRangeEnd_Type.__name__ = "TFilterID"
_FltrMdAutoIdFilterRangeEnd_Object = MibScalar
fltrMdAutoIdFilterRangeEnd = _FltrMdAutoIdFilterRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 105, 2),
    _FltrMdAutoIdFilterRangeEnd_Type()
)
fltrMdAutoIdFilterRangeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltrMdAutoIdFilterRangeEnd.setStatus("current")
_FltrMdAutoIdIPv4FilterCount_Type = TFilterID
_FltrMdAutoIdIPv4FilterCount_Object = MibScalar
fltrMdAutoIdIPv4FilterCount = _FltrMdAutoIdIPv4FilterCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 105, 3),
    _FltrMdAutoIdIPv4FilterCount_Type()
)
fltrMdAutoIdIPv4FilterCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltrMdAutoIdIPv4FilterCount.setStatus("current")
_FltrMdAutoIdIPv6FilterCount_Type = TFilterID
_FltrMdAutoIdIPv6FilterCount_Object = MibScalar
fltrMdAutoIdIPv6FilterCount = _FltrMdAutoIdIPv6FilterCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 105, 4),
    _FltrMdAutoIdIPv6FilterCount_Type()
)
fltrMdAutoIdIPv6FilterCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltrMdAutoIdIPv6FilterCount.setStatus("current")
_FltrMdAutoIdMacFilterCount_Type = TFilterID
_FltrMdAutoIdMacFilterCount_Object = MibScalar
fltrMdAutoIdMacFilterCount = _FltrMdAutoIdMacFilterCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 105, 5),
    _FltrMdAutoIdMacFilterCount_Type()
)
fltrMdAutoIdMacFilterCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltrMdAutoIdMacFilterCount.setStatus("current")
_FltrMdAutoIdIPv4ExceptionCount_Type = TFilterID
_FltrMdAutoIdIPv4ExceptionCount_Object = MibScalar
fltrMdAutoIdIPv4ExceptionCount = _FltrMdAutoIdIPv4ExceptionCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 105, 6),
    _FltrMdAutoIdIPv4ExceptionCount_Type()
)
fltrMdAutoIdIPv4ExceptionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltrMdAutoIdIPv4ExceptionCount.setStatus("current")
_FltrMdAutoIdIPv6ExceptionCount_Type = TFilterID
_FltrMdAutoIdIPv6ExceptionCount_Object = MibScalar
fltrMdAutoIdIPv6ExceptionCount = _FltrMdAutoIdIPv6ExceptionCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 105, 7),
    _FltrMdAutoIdIPv6ExceptionCount_Type()
)
fltrMdAutoIdIPv6ExceptionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltrMdAutoIdIPv6ExceptionCount.setStatus("current")
_TIPv6ExceptionTable_Object = MibTable
tIPv6ExceptionTable = _TIPv6ExceptionTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 106)
)
if mibBuilder.loadTexts:
    tIPv6ExceptionTable.setStatus("current")
_TIPv6ExceptionEntry_Object = MibTableRow
tIPv6ExceptionEntry = _TIPv6ExceptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 106, 1)
)
tIPv6ExceptionEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tIPv6ExceptionId"),
)
if mibBuilder.loadTexts:
    tIPv6ExceptionEntry.setStatus("current")


class _TIPv6ExceptionId_Type(TAnyFilterID):
    """Custom type tIPv6ExceptionId based on TAnyFilterID"""
    subtypeSpec = TAnyFilterID.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TIPv6ExceptionId_Type.__name__ = "TAnyFilterID"
_TIPv6ExceptionId_Object = MibTableColumn
tIPv6ExceptionId = _TIPv6ExceptionId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 106, 1, 1),
    _TIPv6ExceptionId_Type()
)
tIPv6ExceptionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPv6ExceptionId.setStatus("current")
_TIPv6ExceptionRowStatus_Type = RowStatus
_TIPv6ExceptionRowStatus_Object = MibTableColumn
tIPv6ExceptionRowStatus = _TIPv6ExceptionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 106, 1, 2),
    _TIPv6ExceptionRowStatus_Type()
)
tIPv6ExceptionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6ExceptionRowStatus.setStatus("current")


class _TIPv6ExceptionDescription_Type(TItemDescription):
    """Custom type tIPv6ExceptionDescription based on TItemDescription"""
    defaultHexValue = ""


_TIPv6ExceptionDescription_Type.__name__ = "TItemDescription"
_TIPv6ExceptionDescription_Object = MibTableColumn
tIPv6ExceptionDescription = _TIPv6ExceptionDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 106, 1, 3),
    _TIPv6ExceptionDescription_Type()
)
tIPv6ExceptionDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6ExceptionDescription.setStatus("current")


class _TIPv6ExceptionName_Type(TLNamedItemOrEmpty):
    """Custom type tIPv6ExceptionName based on TLNamedItemOrEmpty"""
    defaultHexValue = ""


_TIPv6ExceptionName_Type.__name__ = "TLNamedItemOrEmpty"
_TIPv6ExceptionName_Object = MibTableColumn
tIPv6ExceptionName = _TIPv6ExceptionName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 106, 1, 4),
    _TIPv6ExceptionName_Type()
)
tIPv6ExceptionName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6ExceptionName.setStatus("current")
_TIPv6ExceptionNameTable_Object = MibTable
tIPv6ExceptionNameTable = _TIPv6ExceptionNameTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 107)
)
if mibBuilder.loadTexts:
    tIPv6ExceptionNameTable.setStatus("current")
_TIPv6ExceptionNameEntry_Object = MibTableRow
tIPv6ExceptionNameEntry = _TIPv6ExceptionNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 107, 1)
)
tIPv6ExceptionNameEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tIPv6ExceptionName"),
)
if mibBuilder.loadTexts:
    tIPv6ExceptionNameEntry.setStatus("current")
_TIPv6ExceptionNameId_Type = TAnyFilterID
_TIPv6ExceptionNameId_Object = MibTableColumn
tIPv6ExceptionNameId = _TIPv6ExceptionNameId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 107, 1, 1),
    _TIPv6ExceptionNameId_Type()
)
tIPv6ExceptionNameId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPv6ExceptionNameId.setStatus("current")
_TIPv6ExceptionParamsTable_Object = MibTable
tIPv6ExceptionParamsTable = _TIPv6ExceptionParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 108)
)
if mibBuilder.loadTexts:
    tIPv6ExceptionParamsTable.setStatus("current")
_TIPv6ExceptionParamsEntry_Object = MibTableRow
tIPv6ExceptionParamsEntry = _TIPv6ExceptionParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 108, 1)
)
tIPv6ExceptionParamsEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tIPv6ExceptionId"),
    (0, "TIMETRA-FILTER-MIB", "tIPv6ExcParamsIndex"),
)
if mibBuilder.loadTexts:
    tIPv6ExceptionParamsEntry.setStatus("current")
_TIPv6ExcParamsIndex_Type = TEntryId
_TIPv6ExcParamsIndex_Object = MibTableColumn
tIPv6ExcParamsIndex = _TIPv6ExcParamsIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 108, 1, 1),
    _TIPv6ExcParamsIndex_Type()
)
tIPv6ExcParamsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPv6ExcParamsIndex.setStatus("current")
_TIPv6ExcParamsRowStatus_Type = RowStatus
_TIPv6ExcParamsRowStatus_Object = MibTableColumn
tIPv6ExcParamsRowStatus = _TIPv6ExcParamsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 108, 1, 2),
    _TIPv6ExcParamsRowStatus_Type()
)
tIPv6ExcParamsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6ExcParamsRowStatus.setStatus("current")


class _TIPv6ExcParamsDescription_Type(TItemDescription):
    """Custom type tIPv6ExcParamsDescription based on TItemDescription"""
    defaultHexValue = ""


_TIPv6ExcParamsDescription_Type.__name__ = "TItemDescription"
_TIPv6ExcParamsDescription_Object = MibTableColumn
tIPv6ExcParamsDescription = _TIPv6ExcParamsDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 108, 1, 3),
    _TIPv6ExcParamsDescription_Type()
)
tIPv6ExcParamsDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6ExcParamsDescription.setStatus("current")


class _TIPv6ExcParamsNextHeader_Type(TIpProtocol):
    """Custom type tIPv6ExcParamsNextHeader based on TIpProtocol"""
    defaultValue = -1


_TIPv6ExcParamsNextHeader_Type.__name__ = "TIpProtocol"
_TIPv6ExcParamsNextHeader_Object = MibTableColumn
tIPv6ExcParamsNextHeader = _TIPv6ExcParamsNextHeader_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 108, 1, 4),
    _TIPv6ExcParamsNextHeader_Type()
)
tIPv6ExcParamsNextHeader.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6ExcParamsNextHeader.setStatus("current")


class _TIPv6ExcParamsSrcIpAddr_Type(InetAddressIPv6):
    """Custom type tIPv6ExcParamsSrcIpAddr based on InetAddressIPv6"""
    defaultHexValue = "00000000000000000000000000000000"


_TIPv6ExcParamsSrcIpAddr_Type.__name__ = "InetAddressIPv6"
_TIPv6ExcParamsSrcIpAddr_Object = MibTableColumn
tIPv6ExcParamsSrcIpAddr = _TIPv6ExcParamsSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 108, 1, 5),
    _TIPv6ExcParamsSrcIpAddr_Type()
)
tIPv6ExcParamsSrcIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6ExcParamsSrcIpAddr.setStatus("current")


class _TIPv6ExcParamsSrcIpMask_Type(InetAddressPrefixLength):
    """Custom type tIPv6ExcParamsSrcIpMask based on InetAddressPrefixLength"""
    defaultValue = 0

    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_TIPv6ExcParamsSrcIpMask_Type.__name__ = "InetAddressPrefixLength"
_TIPv6ExcParamsSrcIpMask_Object = MibTableColumn
tIPv6ExcParamsSrcIpMask = _TIPv6ExcParamsSrcIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 108, 1, 6),
    _TIPv6ExcParamsSrcIpMask_Type()
)
tIPv6ExcParamsSrcIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6ExcParamsSrcIpMask.setStatus("current")


class _TIPv6ExcParamsSrcIpFullMask_Type(InetAddressIPv6):
    """Custom type tIPv6ExcParamsSrcIpFullMask based on InetAddressIPv6"""
    defaultHexValue = "00000000000000000000000000000000"


_TIPv6ExcParamsSrcIpFullMask_Type.__name__ = "InetAddressIPv6"
_TIPv6ExcParamsSrcIpFullMask_Object = MibTableColumn
tIPv6ExcParamsSrcIpFullMask = _TIPv6ExcParamsSrcIpFullMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 108, 1, 7),
    _TIPv6ExcParamsSrcIpFullMask_Type()
)
tIPv6ExcParamsSrcIpFullMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6ExcParamsSrcIpFullMask.setStatus("current")


class _TIPv6ExcParamsSrcIpPrefixList_Type(TNamedItemOrEmpty):
    """Custom type tIPv6ExcParamsSrcIpPrefixList based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TIPv6ExcParamsSrcIpPrefixList_Type.__name__ = "TNamedItemOrEmpty"
_TIPv6ExcParamsSrcIpPrefixList_Object = MibTableColumn
tIPv6ExcParamsSrcIpPrefixList = _TIPv6ExcParamsSrcIpPrefixList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 108, 1, 8),
    _TIPv6ExcParamsSrcIpPrefixList_Type()
)
tIPv6ExcParamsSrcIpPrefixList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6ExcParamsSrcIpPrefixList.setStatus("current")


class _TIPv6ExcParamsDstIpAddr_Type(InetAddressIPv6):
    """Custom type tIPv6ExcParamsDstIpAddr based on InetAddressIPv6"""
    defaultHexValue = "00000000000000000000000000000000"


_TIPv6ExcParamsDstIpAddr_Type.__name__ = "InetAddressIPv6"
_TIPv6ExcParamsDstIpAddr_Object = MibTableColumn
tIPv6ExcParamsDstIpAddr = _TIPv6ExcParamsDstIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 108, 1, 9),
    _TIPv6ExcParamsDstIpAddr_Type()
)
tIPv6ExcParamsDstIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6ExcParamsDstIpAddr.setStatus("current")


class _TIPv6ExcParamsDstIpMask_Type(InetAddressPrefixLength):
    """Custom type tIPv6ExcParamsDstIpMask based on InetAddressPrefixLength"""
    defaultValue = 0

    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_TIPv6ExcParamsDstIpMask_Type.__name__ = "InetAddressPrefixLength"
_TIPv6ExcParamsDstIpMask_Object = MibTableColumn
tIPv6ExcParamsDstIpMask = _TIPv6ExcParamsDstIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 108, 1, 10),
    _TIPv6ExcParamsDstIpMask_Type()
)
tIPv6ExcParamsDstIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6ExcParamsDstIpMask.setStatus("current")


class _TIPv6ExcParamsDstIpFullMask_Type(InetAddressIPv6):
    """Custom type tIPv6ExcParamsDstIpFullMask based on InetAddressIPv6"""
    defaultHexValue = "00000000000000000000000000000000"


_TIPv6ExcParamsDstIpFullMask_Type.__name__ = "InetAddressIPv6"
_TIPv6ExcParamsDstIpFullMask_Object = MibTableColumn
tIPv6ExcParamsDstIpFullMask = _TIPv6ExcParamsDstIpFullMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 108, 1, 11),
    _TIPv6ExcParamsDstIpFullMask_Type()
)
tIPv6ExcParamsDstIpFullMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6ExcParamsDstIpFullMask.setStatus("current")


class _TIPv6ExcParamsDstIpPrefixList_Type(TNamedItemOrEmpty):
    """Custom type tIPv6ExcParamsDstIpPrefixList based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TIPv6ExcParamsDstIpPrefixList_Type.__name__ = "TNamedItemOrEmpty"
_TIPv6ExcParamsDstIpPrefixList_Object = MibTableColumn
tIPv6ExcParamsDstIpPrefixList = _TIPv6ExcParamsDstIpPrefixList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 108, 1, 12),
    _TIPv6ExcParamsDstIpPrefixList_Type()
)
tIPv6ExcParamsDstIpPrefixList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6ExcParamsDstIpPrefixList.setStatus("current")


class _TIPv6ExcParamsSourcePortValue1_Type(TTcpUdpPort):
    """Custom type tIPv6ExcParamsSourcePortValue1 based on TTcpUdpPort"""
    defaultValue = 0


_TIPv6ExcParamsSourcePortValue1_Type.__name__ = "TTcpUdpPort"
_TIPv6ExcParamsSourcePortValue1_Object = MibTableColumn
tIPv6ExcParamsSourcePortValue1 = _TIPv6ExcParamsSourcePortValue1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 108, 1, 13),
    _TIPv6ExcParamsSourcePortValue1_Type()
)
tIPv6ExcParamsSourcePortValue1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6ExcParamsSourcePortValue1.setStatus("current")


class _TIPv6ExcParamsSourcePortValue2_Type(TTcpUdpPort):
    """Custom type tIPv6ExcParamsSourcePortValue2 based on TTcpUdpPort"""
    defaultValue = 0


_TIPv6ExcParamsSourcePortValue2_Type.__name__ = "TTcpUdpPort"
_TIPv6ExcParamsSourcePortValue2_Object = MibTableColumn
tIPv6ExcParamsSourcePortValue2 = _TIPv6ExcParamsSourcePortValue2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 108, 1, 14),
    _TIPv6ExcParamsSourcePortValue2_Type()
)
tIPv6ExcParamsSourcePortValue2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6ExcParamsSourcePortValue2.setStatus("current")


class _TIPv6ExcParamsSourcePortOperator_Type(TOperator):
    """Custom type tIPv6ExcParamsSourcePortOperator based on TOperator"""
    defaultValue = 0


_TIPv6ExcParamsSourcePortOperator_Type.__name__ = "TOperator"
_TIPv6ExcParamsSourcePortOperator_Object = MibTableColumn
tIPv6ExcParamsSourcePortOperator = _TIPv6ExcParamsSourcePortOperator_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 108, 1, 15),
    _TIPv6ExcParamsSourcePortOperator_Type()
)
tIPv6ExcParamsSourcePortOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6ExcParamsSourcePortOperator.setStatus("current")


class _TIPv6ExcParamsSourcePortList_Type(TNamedItemOrEmpty):
    """Custom type tIPv6ExcParamsSourcePortList based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TIPv6ExcParamsSourcePortList_Type.__name__ = "TNamedItemOrEmpty"
_TIPv6ExcParamsSourcePortList_Object = MibTableColumn
tIPv6ExcParamsSourcePortList = _TIPv6ExcParamsSourcePortList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 108, 1, 16),
    _TIPv6ExcParamsSourcePortList_Type()
)
tIPv6ExcParamsSourcePortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6ExcParamsSourcePortList.setStatus("current")


class _TIPv6ExcParamsDestPortValue1_Type(TTcpUdpPort):
    """Custom type tIPv6ExcParamsDestPortValue1 based on TTcpUdpPort"""
    defaultValue = 0


_TIPv6ExcParamsDestPortValue1_Type.__name__ = "TTcpUdpPort"
_TIPv6ExcParamsDestPortValue1_Object = MibTableColumn
tIPv6ExcParamsDestPortValue1 = _TIPv6ExcParamsDestPortValue1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 108, 1, 17),
    _TIPv6ExcParamsDestPortValue1_Type()
)
tIPv6ExcParamsDestPortValue1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6ExcParamsDestPortValue1.setStatus("current")


class _TIPv6ExcParamsDestPortValue2_Type(TTcpUdpPort):
    """Custom type tIPv6ExcParamsDestPortValue2 based on TTcpUdpPort"""
    defaultValue = 0


_TIPv6ExcParamsDestPortValue2_Type.__name__ = "TTcpUdpPort"
_TIPv6ExcParamsDestPortValue2_Object = MibTableColumn
tIPv6ExcParamsDestPortValue2 = _TIPv6ExcParamsDestPortValue2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 108, 1, 18),
    _TIPv6ExcParamsDestPortValue2_Type()
)
tIPv6ExcParamsDestPortValue2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6ExcParamsDestPortValue2.setStatus("current")


class _TIPv6ExcParamsDestPortOperator_Type(TOperator):
    """Custom type tIPv6ExcParamsDestPortOperator based on TOperator"""
    defaultValue = 0


_TIPv6ExcParamsDestPortOperator_Type.__name__ = "TOperator"
_TIPv6ExcParamsDestPortOperator_Object = MibTableColumn
tIPv6ExcParamsDestPortOperator = _TIPv6ExcParamsDestPortOperator_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 108, 1, 19),
    _TIPv6ExcParamsDestPortOperator_Type()
)
tIPv6ExcParamsDestPortOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6ExcParamsDestPortOperator.setStatus("current")


class _TIPv6ExcParamsDestPortList_Type(TNamedItemOrEmpty):
    """Custom type tIPv6ExcParamsDestPortList based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TIPv6ExcParamsDestPortList_Type.__name__ = "TNamedItemOrEmpty"
_TIPv6ExcParamsDestPortList_Object = MibTableColumn
tIPv6ExcParamsDestPortList = _TIPv6ExcParamsDestPortList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 108, 1, 20),
    _TIPv6ExcParamsDestPortList_Type()
)
tIPv6ExcParamsDestPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6ExcParamsDestPortList.setStatus("current")


class _TIPv6ExcParamsPortSelector_Type(TFltrPortSelector):
    """Custom type tIPv6ExcParamsPortSelector based on TFltrPortSelector"""
    defaultValue = 0


_TIPv6ExcParamsPortSelector_Type.__name__ = "TFltrPortSelector"
_TIPv6ExcParamsPortSelector_Object = MibTableColumn
tIPv6ExcParamsPortSelector = _TIPv6ExcParamsPortSelector_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 108, 1, 21),
    _TIPv6ExcParamsPortSelector_Type()
)
tIPv6ExcParamsPortSelector.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6ExcParamsPortSelector.setStatus("current")


class _TIPv6ExcParamsIcmpCode_Type(TIcmpCodeOrNone):
    """Custom type tIPv6ExcParamsIcmpCode based on TIcmpCodeOrNone"""
    defaultValue = -1


_TIPv6ExcParamsIcmpCode_Type.__name__ = "TIcmpCodeOrNone"
_TIPv6ExcParamsIcmpCode_Object = MibTableColumn
tIPv6ExcParamsIcmpCode = _TIPv6ExcParamsIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 108, 1, 22),
    _TIPv6ExcParamsIcmpCode_Type()
)
tIPv6ExcParamsIcmpCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6ExcParamsIcmpCode.setStatus("current")


class _TIPv6ExcParamsIcmpType_Type(TIcmpTypeOrNone):
    """Custom type tIPv6ExcParamsIcmpType based on TIcmpTypeOrNone"""
    defaultValue = -1


_TIPv6ExcParamsIcmpType_Type.__name__ = "TIcmpTypeOrNone"
_TIPv6ExcParamsIcmpType_Object = MibTableColumn
tIPv6ExcParamsIcmpType = _TIPv6ExcParamsIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 108, 1, 23),
    _TIPv6ExcParamsIcmpType_Type()
)
tIPv6ExcParamsIcmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPv6ExcParamsIcmpType.setStatus("current")
_TIPv6ExcParamsIngressHitCount_Type = Counter64
_TIPv6ExcParamsIngressHitCount_Object = MibTableColumn
tIPv6ExcParamsIngressHitCount = _TIPv6ExcParamsIngressHitCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 108, 1, 24),
    _TIPv6ExcParamsIngressHitCount_Type()
)
tIPv6ExcParamsIngressHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPv6ExcParamsIngressHitCount.setStatus("current")
_TIPv6ExcParamsEgressHitCount_Type = Counter64
_TIPv6ExcParamsEgressHitCount_Object = MibTableColumn
tIPv6ExcParamsEgressHitCount = _TIPv6ExcParamsEgressHitCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 108, 1, 25),
    _TIPv6ExcParamsEgressHitCount_Type()
)
tIPv6ExcParamsEgressHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPv6ExcParamsEgressHitCount.setStatus("current")
_TIPv6ExcParamsIngrHitByteCount_Type = Counter64
_TIPv6ExcParamsIngrHitByteCount_Object = MibTableColumn
tIPv6ExcParamsIngrHitByteCount = _TIPv6ExcParamsIngrHitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 108, 1, 26),
    _TIPv6ExcParamsIngrHitByteCount_Type()
)
tIPv6ExcParamsIngrHitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPv6ExcParamsIngrHitByteCount.setStatus("current")
_TIPv6ExcParamsEgrHitByteCount_Type = Counter64
_TIPv6ExcParamsEgrHitByteCount_Object = MibTableColumn
tIPv6ExcParamsEgrHitByteCount = _TIPv6ExcParamsEgrHitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 108, 1, 27),
    _TIPv6ExcParamsEgrHitByteCount_Type()
)
tIPv6ExcParamsEgrHitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPv6ExcParamsEgrHitByteCount.setStatus("current")
_TFltrProtocolListTableLstChng_Type = TimeStamp
_TFltrProtocolListTableLstChng_Object = MibScalar
tFltrProtocolListTableLstChng = _TFltrProtocolListTableLstChng_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 109),
    _TFltrProtocolListTableLstChng_Type()
)
tFltrProtocolListTableLstChng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrProtocolListTableLstChng.setStatus("current")
_TFltrProtocolListTable_Object = MibTable
tFltrProtocolListTable = _TFltrProtocolListTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 110)
)
if mibBuilder.loadTexts:
    tFltrProtocolListTable.setStatus("current")
_TFltrProtocolListEntry_Object = MibTableRow
tFltrProtocolListEntry = _TFltrProtocolListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 110, 1)
)
tFltrProtocolListEntry.setIndexNames(
    (1, "TIMETRA-FILTER-MIB", "tFltrProtocolListName"),
)
if mibBuilder.loadTexts:
    tFltrProtocolListEntry.setStatus("current")
_TFltrProtocolListName_Type = TNamedItem
_TFltrProtocolListName_Object = MibTableColumn
tFltrProtocolListName = _TFltrProtocolListName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 110, 1, 1),
    _TFltrProtocolListName_Type()
)
tFltrProtocolListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFltrProtocolListName.setStatus("current")
_TFltrProtocolListRowStatus_Type = RowStatus
_TFltrProtocolListRowStatus_Object = MibTableColumn
tFltrProtocolListRowStatus = _TFltrProtocolListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 110, 1, 2),
    _TFltrProtocolListRowStatus_Type()
)
tFltrProtocolListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFltrProtocolListRowStatus.setStatus("current")
_TFltrProtocolListLastChanged_Type = TimeStamp
_TFltrProtocolListLastChanged_Object = MibTableColumn
tFltrProtocolListLastChanged = _TFltrProtocolListLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 110, 1, 3),
    _TFltrProtocolListLastChanged_Type()
)
tFltrProtocolListLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrProtocolListLastChanged.setStatus("current")


class _TFltrProtocolListDescription_Type(TItemDescription):
    """Custom type tFltrProtocolListDescription based on TItemDescription"""
    defaultHexValue = ""


_TFltrProtocolListDescription_Type.__name__ = "TItemDescription"
_TFltrProtocolListDescription_Object = MibTableColumn
tFltrProtocolListDescription = _TFltrProtocolListDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 110, 1, 4),
    _TFltrProtocolListDescription_Type()
)
tFltrProtocolListDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFltrProtocolListDescription.setStatus("current")
_TFltrProtocolListItemTblLstChg_Type = TimeStamp
_TFltrProtocolListItemTblLstChg_Object = MibScalar
tFltrProtocolListItemTblLstChg = _TFltrProtocolListItemTblLstChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 111),
    _TFltrProtocolListItemTblLstChg_Type()
)
tFltrProtocolListItemTblLstChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFltrProtocolListItemTblLstChg.setStatus("current")
_TFltrProtocolListItemTable_Object = MibTable
tFltrProtocolListItemTable = _TFltrProtocolListItemTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 112)
)
if mibBuilder.loadTexts:
    tFltrProtocolListItemTable.setStatus("current")
_TFltrProtocolListItemEntry_Object = MibTableRow
tFltrProtocolListItemEntry = _TFltrProtocolListItemEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 112, 1)
)
tFltrProtocolListItemEntry.setIndexNames(
    (0, "TIMETRA-FILTER-MIB", "tFltrProtocolListName"),
    (0, "TIMETRA-FILTER-MIB", "tFltrProtocolListItemProtocol"),
)
if mibBuilder.loadTexts:
    tFltrProtocolListItemEntry.setStatus("current")
_TFltrProtocolListItemProtocol_Type = TIpProtocolNumber
_TFltrProtocolListItemProtocol_Object = MibTableColumn
tFltrProtocolListItemProtocol = _TFltrProtocolListItemProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 112, 1, 1),
    _TFltrProtocolListItemProtocol_Type()
)
tFltrProtocolListItemProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFltrProtocolListItemProtocol.setStatus("current")
_TFltrProtocolListItemRowStatus_Type = RowStatus
_TFltrProtocolListItemRowStatus_Object = MibTableColumn
tFltrProtocolListItemRowStatus = _TFltrProtocolListItemRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 21, 112, 1, 2),
    _TFltrProtocolListItemRowStatus_Type()
)
tFltrProtocolListItemRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFltrProtocolListItemRowStatus.setStatus("current")
_TFilterNotificationsPrefix_ObjectIdentity = ObjectIdentity
tFilterNotificationsPrefix = _TFilterNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 21)
)
_TFilterNotifications_ObjectIdentity = ObjectIdentity
tFilterNotifications = _TFilterNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 21, 0)
)
tLiIpFilterParamsEntry.registerAugmentions(
    ("TIMETRA-FILTER-MIB",
     "tLiIpFilterParamsInfoEntry")
)
tLiIpFilterParamsInfoEntry.setIndexNames(*tLiIpFilterParamsEntry.getIndexNames())
tFilterEmbeddedRefTableEntry.registerAugmentions(
    ("TIMETRA-FILTER-MIB",
     "tFilterEmbeddedRefInfoEntry")
)
tFilterEmbeddedRefInfoEntry.setIndexNames(*tFilterEmbeddedRefTableEntry.getIndexNames())
tIPv6FilterParamsEntry.registerAugmentions(
    ("TIMETRA-FILTER-MIB",
     "tIPv6FilterParamsExtEntry")
)
tIPv6FilterParamsExtEntry.setIndexNames(*tIPv6FilterParamsEntry.getIndexNames())
tFilterEmbedOpenflowEntry.registerAugmentions(
    ("TIMETRA-FILTER-MIB",
     "tFilterEmbedOpenflowInfoEntry")
)
tFilterEmbedOpenflowInfoEntry.setIndexNames(*tFilterEmbedOpenflowEntry.getIndexNames())
tIPFilterParamsEntry.registerAugmentions(
    ("TIMETRA-FILTER-MIB",
     "tIPFilterParamsExtEntry")
)
tIPFilterParamsExtEntry.setIndexNames(*tIPFilterParamsEntry.getIndexNames())
tFilterEmbedFlowspecEntry.registerAugmentions(
    ("TIMETRA-FILTER-MIB",
     "tFltrEmbFlowspecInfoEntry")
)
tFltrEmbFlowspecInfoEntry.setIndexNames(*tFilterEmbedFlowspecEntry.getIndexNames())
tFilterEmbedVsdEntry.registerAugmentions(
    ("TIMETRA-FILTER-MIB",
     "tFilterEmbedVsdInfoEntry")
)
tFilterEmbedVsdInfoEntry.setIndexNames(*tFilterEmbedVsdEntry.getIndexNames())

# Managed Objects groups

tFilterLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 3)
)
tFilterLogGroup.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterLogRowStatus"),
        ("TIMETRA-FILTER-MIB", "tFilterLogDestination"),
        ("TIMETRA-FILTER-MIB", "tFilterLogDescription"),
        ("TIMETRA-FILTER-MIB", "tFilterLogMaxNumEntries"),
        ("TIMETRA-FILTER-MIB", "tFilterLogSysLogId"),
        ("TIMETRA-FILTER-MIB", "tFilterLogFileId"),
        ("TIMETRA-FILTER-MIB", "tFilterLogStopOnFull"),
        ("TIMETRA-FILTER-MIB", "tFilterLogEnabled"),
        ("TIMETRA-FILTER-MIB", "tFilterLogMaxInstances"),
        ("TIMETRA-FILTER-MIB", "tFilterLogInstances"),
        ("TIMETRA-FILTER-MIB", "tFilterLogBindings"))
)
if mibBuilder.loadTexts:
    tFilterLogGroup.setStatus("current")

tFilterRedirectPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 4)
)
tFilterRedirectPolicyGroup.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterRPRowStatus"),
        ("TIMETRA-FILTER-MIB", "tFilterRPDescription"),
        ("TIMETRA-FILTER-MIB", "tFilterRPAdminState"),
        ("TIMETRA-FILTER-MIB", "tFilterRPActiveDest"),
        ("TIMETRA-FILTER-MIB", "tFilterRDRowStatus"),
        ("TIMETRA-FILTER-MIB", "tFilterRDDescription"),
        ("TIMETRA-FILTER-MIB", "tFilterRDAdminPriority"),
        ("TIMETRA-FILTER-MIB", "tFilterRDOperPriority"),
        ("TIMETRA-FILTER-MIB", "tFilterRDAdminState"),
        ("TIMETRA-FILTER-MIB", "tFilterRDOperState"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTRowStatus"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTOID"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTCommunity"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTSNMPVersion"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTInterval"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTTimeout"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTDropCount"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTHoldDown"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTHoldDownRemain"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTLastActionTime"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTLastOID"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTLastType"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTLastCounter32Val"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTLastUnsigned32Val"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTLastTimeTicksVal"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTLastInt32Val"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTLastOctetStringVal"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTLastIpAddressVal"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTLastOidVal"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTLastCounter64Val"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTLastOpaqueVal"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTLastAction"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTLastPrioChange"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTNextRespIndex"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTRespRowStatus"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTRespAction"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTRespPrioChange"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTRespOID"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTRespType"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTCounter32Val"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTUnsigned32Val"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTTimeTicksVal"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTInt32Val"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTOctetStringVal"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTIpAddressVal"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTOidVal"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTCounter64Val"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTOpaqueVal"),
        ("TIMETRA-FILTER-MIB", "tFilterRUTRowStatus"),
        ("TIMETRA-FILTER-MIB", "tFilterRUTURL"),
        ("TIMETRA-FILTER-MIB", "tFilterRUTHTTPVersion"),
        ("TIMETRA-FILTER-MIB", "tFilterRUTInterval"),
        ("TIMETRA-FILTER-MIB", "tFilterRUTTimeout"),
        ("TIMETRA-FILTER-MIB", "tFilterRUTDropCount"),
        ("TIMETRA-FILTER-MIB", "tFilterRUTHoldDown"),
        ("TIMETRA-FILTER-MIB", "tFilterRUTHoldDownRemain"),
        ("TIMETRA-FILTER-MIB", "tFilterRUTLastActionTime"),
        ("TIMETRA-FILTER-MIB", "tFilterRUTLastRetCode"),
        ("TIMETRA-FILTER-MIB", "tFilterRUTLastAction"),
        ("TIMETRA-FILTER-MIB", "tFilterRUTLastPrioChange"),
        ("TIMETRA-FILTER-MIB", "tFilterRUTRespRowStatus"),
        ("TIMETRA-FILTER-MIB", "tFilterRUTRespAction"),
        ("TIMETRA-FILTER-MIB", "tFilterRUTRespPrioChange"),
        ("TIMETRA-FILTER-MIB", "tFilterRPTRowStatus"),
        ("TIMETRA-FILTER-MIB", "tFilterRPTInterval"),
        ("TIMETRA-FILTER-MIB", "tFilterRPTTimeout"),
        ("TIMETRA-FILTER-MIB", "tFilterRPTDropCount"),
        ("TIMETRA-FILTER-MIB", "tFilterRPTHoldDown"),
        ("TIMETRA-FILTER-MIB", "tFilterRPTHoldDownRemain"),
        ("TIMETRA-FILTER-MIB", "tFilterRPTLastActionTime"),
        ("TIMETRA-FILTER-MIB", "tFilterRPTLastAction"))
)
if mibBuilder.loadTexts:
    tFilterRedirectPolicyGroup.setStatus("obsolete")

tFilterScalarGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 7)
)
tFilterScalarGroup.setObjects(
    ("TIMETRA-FILTER-MIB", "tFilterDomainLastChanged")
)
if mibBuilder.loadTexts:
    tFilterScalarGroup.setStatus("current")

tFilterNotificationObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 8)
)
tFilterNotificationObjGroup.setObjects(
    ("TIMETRA-FILTER-MIB", "tFilterPBRDropReason")
)
if mibBuilder.loadTexts:
    tFilterNotificationObjGroup.setStatus("obsolete")

tIPv6FilterV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 11)
)
tIPv6FilterV4v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPv6FilterRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterScope"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterDescription"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterDefaultAction"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsLogId"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDescription"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsAction"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsForwardNH"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsForwardNHIndirect"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRemarkDSCP"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRemarkDSCPMask"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRemarkDot1p"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourceIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourceIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestinationIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestinationIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsNextHeader"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourcePortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourcePortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourcePortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestPortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestPortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestPortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDSCP"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsTcpSyn"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsTcpAck"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsIcmpCode"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsIcmpType"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsCflowdSample"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsCflowdIfSample"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsForwardNHInterface"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsIngressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsEgressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsLogInstantiated"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsForwardRedPlcy"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsActiveDest"))
)
if mibBuilder.loadTexts:
    tIPv6FilterV4v0Group.setStatus("obsolete")

tIPFilterV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 12)
)
tIPFilterV4v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPFilterRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPFilterScope"),
        ("TIMETRA-FILTER-MIB", "tIPFilterDescription"),
        ("TIMETRA-FILTER-MIB", "tIPFilterDefaultAction"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsLogId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDescription"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsAction"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardNH"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardNHIndirect"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRemarkDSCP"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRemarkDSCPMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRemarkDot1p"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourceIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourceIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestinationIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestinationIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsProtocol"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourcePortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourcePortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourcePortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestPortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestPortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestPortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDSCP"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFragment"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsOptionPresent"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIpOptionValue"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIpOptionMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsMultipleOption"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsTcpSyn"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsTcpAck"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIcmpCode"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIcmpType"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsCflowdSample"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsCflowdIfSample"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardNHInterface"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIngressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsEgressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsLogInstantiated"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardRedPlcy"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsActiveDest"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSvcId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSapPortId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSapEncapVal"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSdpBind"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRedirectURL"))
)
if mibBuilder.loadTexts:
    tIPFilterV4v0Group.setStatus("obsolete")

tMacFilterV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 13)
)
tMacFilterV4v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tMacFilterRowStatus"),
        ("TIMETRA-FILTER-MIB", "tMacFilterScope"),
        ("TIMETRA-FILTER-MIB", "tMacFilterDescription"),
        ("TIMETRA-FILTER-MIB", "tMacFilterDefaultAction"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsRowStatus"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsLogId"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsDescription"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsAction"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsFrameType"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsSrcMAC"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsSrcMACMask"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsDstMAC"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsDstMACMask"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsDot1pValue"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsDot1pMask"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsEtherType"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsDsap"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsDsapMask"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsSsap"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsSsapMask"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsSnapPid"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsSnapOui"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsIngressHitCount"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsEgressHitCount"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsLogInstantiated"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsFwdSvcId"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsFwdSapPortId"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsFwdSapEncapVal"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsFwdSdpBind"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsRedirectURL"))
)
if mibBuilder.loadTexts:
    tMacFilterV4v0Group.setStatus("obsolete")

tTodPoliciesV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 14)
)
tTodPoliciesV4v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPFilterParamsTimeRangeName"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsTimeRangeState"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsTimeRangeName"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsTimeRangeState"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsTimeRangeName"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsTimeRangeState"))
)
if mibBuilder.loadTexts:
    tTodPoliciesV4v0Group.setStatus("obsolete")

tmnxFilterObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 15)
)
tmnxFilterObsoleteGroup.setObjects(
    ("TIMETRA-FILTER-MIB", "tAutoIPFilterEntrySourceIpMask")
)
if mibBuilder.loadTexts:
    tmnxFilterObsoleteGroup.setStatus("current")

tIPFilterV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 17)
)
tIPFilterV5v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPFilterRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPFilterScope"),
        ("TIMETRA-FILTER-MIB", "tIPFilterDescription"),
        ("TIMETRA-FILTER-MIB", "tIPFilterDefaultAction"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsLogId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDescription"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsAction"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardNH"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardNHIndirect"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRemarkDSCP"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRemarkDSCPMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRemarkDot1p"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourceIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourceIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestinationIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestinationIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsProtocol"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourcePortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourcePortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourcePortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestPortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestPortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestPortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDSCP"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFragment"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsOptionPresent"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIpOptionValue"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIpOptionMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsMultipleOption"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsTcpSyn"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsTcpAck"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIcmpCode"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIcmpType"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsCflowdSample"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsCflowdIfSample"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardNHInterface"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIngressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsEgressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsLogInstantiated"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardRedPlcy"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsActiveDest"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSvcId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSapPortId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSapEncapVal"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSdpBind"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRedirectURL"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSrcIpFullMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestIpFullMask"))
)
if mibBuilder.loadTexts:
    tIPFilterV5v0Group.setStatus("obsolete")

tFilterLogV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 18)
)
tFilterLogV5v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterLogSummaryEnabled"),
        ("TIMETRA-FILTER-MIB", "tFilterLogSummaryCrit1"))
)
if mibBuilder.loadTexts:
    tFilterLogV5v0Group.setStatus("current")

tTodPolicies77450V5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 19)
)
tTodPolicies77450V5v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPFilterParamsTimeRangeName"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsTimeRangeState"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsTimeRangeName"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsTimeRangeState"))
)
if mibBuilder.loadTexts:
    tTodPolicies77450V5v0Group.setStatus("obsolete")

tTodPolicies77x0V5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 20)
)
tTodPolicies77x0V5v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPFilterParamsTimeRangeName"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsTimeRangeState"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsTimeRangeName"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsTimeRangeState"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsTimeRangeName"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsTimeRangeState"))
)
if mibBuilder.loadTexts:
    tTodPolicies77x0V5v0Group.setStatus("obsolete")

tFilterNotificationObjV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 21)
)
tFilterNotificationObjV5v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterPBRDropReason"),
        ("TIMETRA-FILTER-MIB", "tFilterParmRow"),
        ("TIMETRA-FILTER-MIB", "tFilterAlarmDescription"))
)
if mibBuilder.loadTexts:
    tFilterNotificationObjV5v0Group.setStatus("obsolete")

tIPFilterV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 22)
)
tIPFilterV6v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPFilterRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPFilterScope"),
        ("TIMETRA-FILTER-MIB", "tIPFilterDescription"),
        ("TIMETRA-FILTER-MIB", "tIPFilterDefaultAction"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsLogId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDescription"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsAction"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardNH"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardNHIndirect"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRemarkDSCP"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRemarkDSCPMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRemarkDot1p"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourceIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourceIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestinationIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestinationIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsProtocol"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourcePortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourcePortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourcePortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestPortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestPortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestPortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDSCP"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFragment"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsOptionPresent"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIpOptionValue"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIpOptionMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsMultipleOption"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsTcpSyn"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsTcpAck"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIcmpCode"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIcmpType"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsCflowdSample"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsCflowdIfSample"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardNHInterface"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIngressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsEgressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsLogInstantiated"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardRedPlcy"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsActiveDest"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSvcId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSapPortId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSapEncapVal"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSdpBind"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRedirectURL"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSrcIpFullMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestIpFullMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIngrHitByteCount"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsEgrHitByteCount"))
)
if mibBuilder.loadTexts:
    tIPFilterV6v0Group.setStatus("obsolete")

tMacFilterV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 23)
)
tMacFilterV6v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tMacFilterRowStatus"),
        ("TIMETRA-FILTER-MIB", "tMacFilterScope"),
        ("TIMETRA-FILTER-MIB", "tMacFilterDescription"),
        ("TIMETRA-FILTER-MIB", "tMacFilterDefaultAction"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsRowStatus"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsLogId"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsDescription"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsAction"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsFrameType"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsSrcMAC"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsSrcMACMask"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsDstMAC"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsDstMACMask"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsDot1pValue"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsDot1pMask"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsEtherType"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsDsap"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsDsapMask"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsSsap"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsSsapMask"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsSnapPid"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsSnapOui"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsIngressHitCount"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsEgressHitCount"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsLogInstantiated"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsFwdSvcId"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsFwdSapPortId"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsFwdSapEncapVal"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsFwdSdpBind"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsRedirectURL"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsIngrHitByteCount"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsEgrHitByteCount"))
)
if mibBuilder.loadTexts:
    tMacFilterV6v0Group.setStatus("obsolete")

tIPv6FilterV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 24)
)
tIPv6FilterV6v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPv6FilterRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterScope"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterDescription"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterDefaultAction"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsLogId"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDescription"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsAction"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsForwardNH"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsForwardNHIndirect"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRemarkDSCP"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRemarkDSCPMask"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRemarkDot1p"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourceIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourceIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestinationIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestinationIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsNextHeader"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourcePortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourcePortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourcePortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestPortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestPortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestPortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDSCP"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsTcpSyn"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsTcpAck"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsIcmpCode"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsIcmpType"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsCflowdSample"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsCflowdIfSample"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsForwardNHInterface"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsIngressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsEgressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsLogInstantiated"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsForwardRedPlcy"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsActiveDest"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsIngrHitByteCount"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsEgrHitByteCount"))
)
if mibBuilder.loadTexts:
    tIPv6FilterV6v0Group.setStatus("obsolete")

tIPFilterV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 25)
)
tIPFilterV8v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPFilterRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPFilterScope"),
        ("TIMETRA-FILTER-MIB", "tIPFilterDescription"),
        ("TIMETRA-FILTER-MIB", "tIPFilterDefaultAction"),
        ("TIMETRA-FILTER-MIB", "tIPFilterRadiusInsertPt"),
        ("TIMETRA-FILTER-MIB", "tIPFilterRadiusInsertSize"),
        ("TIMETRA-FILTER-MIB", "tIPFilterCreditCntrlInsertPt"),
        ("TIMETRA-FILTER-MIB", "tIPFilterCreditCntrlInsertSize"),
        ("TIMETRA-FILTER-MIB", "tIPFilterSubInsertHighWmark"),
        ("TIMETRA-FILTER-MIB", "tIPFilterSubInsertLowWmark"),
        ("TIMETRA-FILTER-MIB", "tIpFilterCreditCntrlNbrInsertd"),
        ("TIMETRA-FILTER-MIB", "tIpFilterRadiusNbrInsertd"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsLogId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDescription"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsAction"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardNH"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardNHIndirect"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRemarkDSCP"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRemarkDSCPMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRemarkDot1p"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourceIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourceIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestinationIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestinationIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsProtocol"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourcePortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourcePortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourcePortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestPortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestPortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestPortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDSCP"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFragment"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsOptionPresent"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIpOptionValue"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIpOptionMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsMultipleOption"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsTcpSyn"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsTcpAck"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIcmpCode"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIcmpType"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsCflowdSample"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsCflowdIfSample"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardNHInterface"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIngressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsEgressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsLogInstantiated"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardRedPlcy"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsActiveDest"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSvcId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSapPortId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSapEncapVal"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSdpBind"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRedirectURL"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSrcIpFullMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestIpFullMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIngrHitByteCount"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsEgrHitByteCount"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesFilterType"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesFilterId"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesApplication"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesLocation"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesResult"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesFeedback"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesExecute"))
)
if mibBuilder.loadTexts:
    tIPFilterV8v0Group.setStatus("obsolete")

tIPv6FilterV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 26)
)
tIPv6FilterV8v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPv6FilterRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterScope"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterDescription"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterDefaultAction"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterRadiusInsertPt"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterRadiusInsertSize"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterCreditCntrlInsertPt"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterCreditCntrlInsertSize"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterSubInsertHighWmark"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterSubInsertLowWmark"),
        ("TIMETRA-FILTER-MIB", "tIpv6FilterCreditCntrlNbrInsertd"),
        ("TIMETRA-FILTER-MIB", "tIpv6FilterRadiusNbrInsertd"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsLogId"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDescription"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsAction"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsForwardNH"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsForwardNHIndirect"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRemarkDSCP"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRemarkDSCPMask"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRemarkDot1p"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourceIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourceIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestinationIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestinationIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsNextHeader"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourcePortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourcePortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourcePortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestPortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestPortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestPortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDSCP"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsTcpSyn"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsTcpAck"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsIcmpCode"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsIcmpType"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsCflowdSample"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsCflowdIfSample"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsForwardNHInterface"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsIngressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsEgressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsLogInstantiated"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsForwardRedPlcy"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsActiveDest"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsIngrHitByteCount"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsEgrHitByteCount"))
)
if mibBuilder.loadTexts:
    tIPv6FilterV8v0Group.setStatus("obsolete")

tFilterNotificationObjV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 27)
)
tFilterNotificationObjV8v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterPBRDropReason"),
        ("TIMETRA-FILTER-MIB", "tFilterParmRow"),
        ("TIMETRA-FILTER-MIB", "tFilterAlarmDescription"),
        ("TIMETRA-FILTER-MIB", "tFilterId"),
        ("TIMETRA-FILTER-MIB", "tFilterType"),
        ("TIMETRA-FILTER-MIB", "tFilterSubInsSpaceOwner"),
        ("TIMETRA-FILTER-MIB", "tFilterThresholdReached"))
)
if mibBuilder.loadTexts:
    tFilterNotificationObjV8v0Group.setStatus("obsolete")

tMacFilterV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 29)
)
tMacFilterV8v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tMacFilterRowStatus"),
        ("TIMETRA-FILTER-MIB", "tMacFilterScope"),
        ("TIMETRA-FILTER-MIB", "tMacFilterDescription"),
        ("TIMETRA-FILTER-MIB", "tMacFilterDefaultAction"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsRowStatus"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsLogId"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsDescription"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsAction"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsFrameType"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsSrcMAC"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsSrcMACMask"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsDstMAC"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsDstMACMask"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsDot1pValue"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsDot1pMask"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsEtherType"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsDsap"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsDsapMask"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsSsap"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsSsapMask"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsSnapPid"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsSnapOui"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsIngressHitCount"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsEgressHitCount"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsLogInstantiated"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsFwdSvcId"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsFwdSapPortId"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsFwdSapEncapVal"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsFwdSdpBind"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsRedirectURL"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsIngrHitByteCount"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsEgrHitByteCount"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsLowISID"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsHighISID"),
        ("TIMETRA-FILTER-MIB", "tMacFilterType"))
)
if mibBuilder.loadTexts:
    tMacFilterV8v0Group.setStatus("obsolete")

tMacFilterVidFilteringV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 30)
)
tMacFilterVidFilteringV9v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tMacFilterParamsInnerTagValue"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsInnerTagMask"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsOuterTagValue"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsOuterTagMask"))
)
if mibBuilder.loadTexts:
    tMacFilterVidFilteringV9v0Group.setStatus("current")

tIPFilterV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 31)
)
tIPFilterV9v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPFilterRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPFilterScope"),
        ("TIMETRA-FILTER-MIB", "tIPFilterDescription"),
        ("TIMETRA-FILTER-MIB", "tIPFilterDefaultAction"),
        ("TIMETRA-FILTER-MIB", "tIPFilterRadiusInsertPt"),
        ("TIMETRA-FILTER-MIB", "tIPFilterRadiusInsertSize"),
        ("TIMETRA-FILTER-MIB", "tIPFilterCreditCntrlInsertPt"),
        ("TIMETRA-FILTER-MIB", "tIPFilterCreditCntrlInsertSize"),
        ("TIMETRA-FILTER-MIB", "tIPFilterSubInsertHighWmark"),
        ("TIMETRA-FILTER-MIB", "tIPFilterSubInsertLowWmark"),
        ("TIMETRA-FILTER-MIB", "tIpFilterCreditCntrlNbrInsertd"),
        ("TIMETRA-FILTER-MIB", "tIpFilterRadiusNbrInsertd"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsLogId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDescription"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsAction"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardNH"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardNHIndirect"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRemarkDSCP"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRemarkDSCPMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRemarkDot1p"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourceIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourceIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestinationIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestinationIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsProtocol"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourcePortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourcePortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourcePortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestPortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestPortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestPortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDSCP"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFragment"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsOptionPresent"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIpOptionValue"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIpOptionMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsMultipleOption"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsTcpSyn"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsTcpAck"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIcmpCode"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIcmpType"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsCflowdSample"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsCflowdIfSample"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardNHInterface"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIngressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsEgressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsLogInstantiated"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardRedPlcy"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsActiveDest"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSvcId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSapPortId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSapEncapVal"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSdpBind"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRedirectURL"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSrcIpFullMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestIpFullMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIngrHitByteCount"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsEgrHitByteCount"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesFilterType"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesFilterId"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesApplication"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesLocation"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesResult"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesFeedback"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesExecute"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdRtrId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSrcRouteOption"))
)
if mibBuilder.loadTexts:
    tIPFilterV9v0Group.setStatus("obsolete")

tFilterNotificationObjV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 33)
)
tFilterNotificationObjV9v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterPBRDropReason"),
        ("TIMETRA-FILTER-MIB", "tFilterParmRow"),
        ("TIMETRA-FILTER-MIB", "tFilterAlarmDescription"),
        ("TIMETRA-FILTER-MIB", "tFilterId"),
        ("TIMETRA-FILTER-MIB", "tFilterType"),
        ("TIMETRA-FILTER-MIB", "tFilterSubInsSpaceOwner"),
        ("TIMETRA-FILTER-MIB", "tFilterThresholdReached"),
        ("TIMETRA-FILTER-MIB", "tFltrFlowSpecProblem"),
        ("TIMETRA-FILTER-MIB", "tFltrFlowSpecProblemDescription"),
        ("TIMETRA-FILTER-MIB", "tFltrFLowSpecNLRI"),
        ("TIMETRA-FILTER-MIB", "tFltrFlowSpecVrtrId"))
)
if mibBuilder.loadTexts:
    tFilterNotificationObjV9v0Group.setStatus("obsolete")

tDhcpFilterV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 34)
)
tDhcpFilterV9v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tDhcpFilterTableLastChanged"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterRowStatus"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterLastChanged"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterDescription"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterParamsTblLastChanged"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterParamsRowStatus"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterParamsLastChanged"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterParamsOptionNumber"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterParamsOptionMatch"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterParamsAction"))
)
if mibBuilder.loadTexts:
    tDhcpFilterV9v0Group.setStatus("obsolete")

tIPv6FilterV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 35)
)
tIPv6FilterV10v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPv6FilterRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterScope"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterDescription"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterDefaultAction"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterRadiusInsertPt"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterRadiusInsertSize"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterCreditCntrlInsertPt"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterCreditCntrlInsertSize"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterSubInsertHighWmark"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterSubInsertLowWmark"),
        ("TIMETRA-FILTER-MIB", "tIpv6FilterCreditCntrlNbrInsertd"),
        ("TIMETRA-FILTER-MIB", "tIpv6FilterRadiusNbrInsertd"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsLogId"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDescription"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsAction"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsForwardNH"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsForwardNHIndirect"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRemarkDSCP"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRemarkDSCPMask"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRemarkDot1p"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourceIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourceIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestinationIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestinationIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsNextHeader"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourcePortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourcePortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourcePortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestPortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestPortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestPortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDSCP"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsTcpSyn"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsTcpAck"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsIcmpCode"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsIcmpType"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsCflowdSample"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsCflowdIfSample"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsForwardNHInterface"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsIngressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsEgressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsLogInstantiated"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsForwardRedPlcy"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsActiveDest"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsIngrHitByteCount"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsEgrHitByteCount"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFwdSvcId"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFwdSapPortId"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFwdSapEncapVal"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFwdSdpBind"))
)
if mibBuilder.loadTexts:
    tIPv6FilterV10v0Group.setStatus("obsolete")

tFilterNameV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 36)
)
tFilterNameV10v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIpFilterName"),
        ("TIMETRA-FILTER-MIB", "tIpFilterNameId"),
        ("TIMETRA-FILTER-MIB", "tIpFilterNameLastChanged"),
        ("TIMETRA-FILTER-MIB", "tIpFilterNameRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIpFilterNameTableLastChgd"),
        ("TIMETRA-FILTER-MIB", "tIpv6FilterName"),
        ("TIMETRA-FILTER-MIB", "tIpv6FilterNameId"),
        ("TIMETRA-FILTER-MIB", "tIpv6FilterNameLastChanged"),
        ("TIMETRA-FILTER-MIB", "tIpv6FilterNameRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIpv6FilterNameTableLastChgd"),
        ("TIMETRA-FILTER-MIB", "tMacFilterName"),
        ("TIMETRA-FILTER-MIB", "tMacFilterNameId"),
        ("TIMETRA-FILTER-MIB", "tMacFilterNameLastChanged"),
        ("TIMETRA-FILTER-MIB", "tMacFilterNameRowStatus"),
        ("TIMETRA-FILTER-MIB", "tMacFilterNameTableLastChgd"))
)
if mibBuilder.loadTexts:
    tFilterNameV10v0Group.setStatus("current")

tDhcpFilterV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 37)
)
tDhcpFilterV10v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tDhcpFilterTableLastChanged"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterRowStatus"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterLastChanged"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterDescription"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterParamsTblLastChanged"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterParamsRowStatus"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterParamsLastChanged"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterParamsOptionNumber"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterParamsOptionMatch"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterParamsAction"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterParamsOptionValue"))
)
if mibBuilder.loadTexts:
    tDhcpFilterV10v0Group.setStatus("current")

tLiFilterV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 38)
)
tLiFilterV10v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tLiReservedBlockRowStatus"),
        ("TIMETRA-FILTER-MIB", "tLiReservedBlockDescription"),
        ("TIMETRA-FILTER-MIB", "tLiReservedBlockStart"),
        ("TIMETRA-FILTER-MIB", "tLiReservedBlockSize"),
        ("TIMETRA-FILTER-MIB", "tLiReservedBlockLastChanged"),
        ("TIMETRA-FILTER-MIB", "tLiReservedBlockTableLastChanged"),
        ("TIMETRA-FILTER-MIB", "tLiReservedBlockFltrRowStatus"),
        ("TIMETRA-FILTER-MIB", "tLiReservedBlockFltrLastChanged"),
        ("TIMETRA-FILTER-MIB", "tLiReservedBlockFltrTableLastChg"),
        ("TIMETRA-FILTER-MIB", "tLiFilterDescription"),
        ("TIMETRA-FILTER-MIB", "tLiFilterRowStatus"),
        ("TIMETRA-FILTER-MIB", "tLiFilterLastChanged"),
        ("TIMETRA-FILTER-MIB", "tLiFilterTableLastChanged"),
        ("TIMETRA-FILTER-MIB", "tLiFilterAssociationRowStatus"),
        ("TIMETRA-FILTER-MIB", "tLiFilterAssociationLastChg"),
        ("TIMETRA-FILTER-MIB", "tLiFilterAssociationTableLastChg"),
        ("TIMETRA-FILTER-MIB", "tLiMacFilterParamsDescription"),
        ("TIMETRA-FILTER-MIB", "tLiMacFilterParamsDstMAC"),
        ("TIMETRA-FILTER-MIB", "tLiMacFilterParamsDstMACMask"),
        ("TIMETRA-FILTER-MIB", "tLiMacFilterParamsFrameType"),
        ("TIMETRA-FILTER-MIB", "tLiMacFilterParamsRowStatus"),
        ("TIMETRA-FILTER-MIB", "tLiMacFilterParamsSrcMAC"),
        ("TIMETRA-FILTER-MIB", "tLiMacFilterParamsSrcMACMask"),
        ("TIMETRA-FILTER-MIB", "tLiMacFilterParamsLastChanged"),
        ("TIMETRA-FILTER-MIB", "tLiMacFilterParamsTableLastChg"),
        ("TIMETRA-FILTER-MIB", "tLiMacFilterParamsIngrHitCount"),
        ("TIMETRA-FILTER-MIB", "tLiMacFilterParamsEgrHitCount"),
        ("TIMETRA-FILTER-MIB", "tLiMacFilterParamsIngrHitBytes"),
        ("TIMETRA-FILTER-MIB", "tLiMacFilterParamsEgrHitBytes"))
)
if mibBuilder.loadTexts:
    tLiFilterV10v0Group.setStatus("obsolete")

tFilterPrefixListV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 39)
)
tFilterPrefixListV10v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterPrefixListTableLstChng"),
        ("TIMETRA-FILTER-MIB", "tFilterPrefixListRowStatus"),
        ("TIMETRA-FILTER-MIB", "tFilterPrefixListLastChanged"),
        ("TIMETRA-FILTER-MIB", "tFilterPrefixListDescription"),
        ("TIMETRA-FILTER-MIB", "tFilterPrefixListEntryTblLstChg"),
        ("TIMETRA-FILTER-MIB", "tFilterPrefixListEntryRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSrcIpPrefixList"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDstIpPrefixList"))
)
if mibBuilder.loadTexts:
    tFilterPrefixListV10v0Group.setStatus("obsolete")

tIPv6FilterV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 40)
)
tIPv6FilterV11v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPv6FilterRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterScope"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterDescription"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterDefaultAction"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterRadiusInsertPt"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterRadiusInsertSize"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterCreditCntrlInsertPt"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterCreditCntrlInsertSize"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterSubInsertHighWmark"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterSubInsertLowWmark"),
        ("TIMETRA-FILTER-MIB", "tIpv6FilterCreditCntrlNbrInsertd"),
        ("TIMETRA-FILTER-MIB", "tIpv6FilterRadiusNbrInsertd"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterHostSharedInsertPt"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterHostSharedInsertSize"),
        ("TIMETRA-FILTER-MIB", "tIpv6FilterHostSharedNbrInsertd"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterHostSharedHighWmark"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterHostSharedLowWmark"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterNbrHostSharedFltrs"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsLogId"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDescription"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsAction"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsForwardNH"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsForwardNHIndirect"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRemarkDSCP"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRemarkDSCPMask"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRemarkDot1p"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourceIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourceIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestinationIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestinationIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsNextHeader"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourcePortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourcePortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourcePortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestPortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestPortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestPortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDSCP"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsTcpSyn"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsTcpAck"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsIcmpCode"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsIcmpType"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsCflowdSample"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsCflowdIfSample"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsForwardNHInterface"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsIngressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsEgressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsLogInstantiated"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsForwardRedPlcy"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsActiveDest"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsIngrHitByteCount"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsEgrHitByteCount"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFwdSvcId"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFwdSapPortId"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFwdSapEncapVal"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFwdSdpBind"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRedirectURL"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSrcIpPrefixList"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDstIpPrefixList"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFragment"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsHopByHopOpt"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRoutingType0"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsPortSelector"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSrcPortList"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDstPortList"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFwdRtrId"))
)
if mibBuilder.loadTexts:
    tIPv6FilterV11v0Group.setStatus("obsolete")

tFilterEmbeddedInsertV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 41)
)
tFilterEmbeddedInsertV11v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterEmbeddedRefRowStatus"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbeddedRefTableLstChg"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbeddedRefOperState"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbeddedRefAdminState"),
        ("TIMETRA-FILTER-MIB", "tFltrEmbedRefInfEntryCnt"),
        ("TIMETRA-FILTER-MIB", "tFltrEmbedRefInfEntryCntInsrtd"),
        ("TIMETRA-FILTER-MIB", "tFltrEmbedEntryInsrtEntryId"),
        ("TIMETRA-FILTER-MIB", "tFltrEmbedEntryRefOperState"))
)
if mibBuilder.loadTexts:
    tFilterEmbeddedInsertV11v0Group.setStatus("current")

tFilterPortListV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 42)
)
tFilterPortListV11v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterPortListTableLstChng"),
        ("TIMETRA-FILTER-MIB", "tFilterPortListRowStatus"),
        ("TIMETRA-FILTER-MIB", "tFilterPortListLastChanged"),
        ("TIMETRA-FILTER-MIB", "tFilterPortListDescription"),
        ("TIMETRA-FILTER-MIB", "tFilterPortListEntryTblLstChg"),
        ("TIMETRA-FILTER-MIB", "tFilterPortListEntryRowStatus"))
)
if mibBuilder.loadTexts:
    tFilterPortListV11v0Group.setStatus("current")

tFilterPrefixListV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 43)
)
tFilterPrefixListV11v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterPrefixListTableLstChng"),
        ("TIMETRA-FILTER-MIB", "tFilterPrefixListRowStatus"),
        ("TIMETRA-FILTER-MIB", "tFilterPrefixListLastChanged"),
        ("TIMETRA-FILTER-MIB", "tFilterPrefixListDescription"),
        ("TIMETRA-FILTER-MIB", "tFilterPrefixListEntryTblLstChg"),
        ("TIMETRA-FILTER-MIB", "tFilterPrefixListEntryRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSrcIpPrefixList"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDstIpPrefixList"),
        ("TIMETRA-FILTER-MIB", "tFilterApplyPathTableLstChng"),
        ("TIMETRA-FILTER-MIB", "tFilterApplyPathRowStatus"),
        ("TIMETRA-FILTER-MIB", "tFilterApplyPathLastChanged"),
        ("TIMETRA-FILTER-MIB", "tFilterApplyPathMatch1"),
        ("TIMETRA-FILTER-MIB", "tFilterApplyPathMatch2"))
)
if mibBuilder.loadTexts:
    tFilterPrefixListV11v0Group.setStatus("current")

tIPFilterV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 44)
)
tIPFilterV11v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPFilterRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPFilterScope"),
        ("TIMETRA-FILTER-MIB", "tIPFilterDescription"),
        ("TIMETRA-FILTER-MIB", "tIPFilterDefaultAction"),
        ("TIMETRA-FILTER-MIB", "tIPFilterRadiusInsertPt"),
        ("TIMETRA-FILTER-MIB", "tIPFilterRadiusInsertSize"),
        ("TIMETRA-FILTER-MIB", "tIPFilterCreditCntrlInsertPt"),
        ("TIMETRA-FILTER-MIB", "tIPFilterCreditCntrlInsertSize"),
        ("TIMETRA-FILTER-MIB", "tIPFilterSubInsertHighWmark"),
        ("TIMETRA-FILTER-MIB", "tIPFilterSubInsertLowWmark"),
        ("TIMETRA-FILTER-MIB", "tIpFilterCreditCntrlNbrInsertd"),
        ("TIMETRA-FILTER-MIB", "tIpFilterRadiusNbrInsertd"),
        ("TIMETRA-FILTER-MIB", "tIPFilterHostSharedInsertPt"),
        ("TIMETRA-FILTER-MIB", "tIPFilterHostSharedInsertSize"),
        ("TIMETRA-FILTER-MIB", "tIpFilterHostSharedNbrInsertd"),
        ("TIMETRA-FILTER-MIB", "tIPFilterHostSharedHighWmark"),
        ("TIMETRA-FILTER-MIB", "tIPFilterHostSharedLowWmark"),
        ("TIMETRA-FILTER-MIB", "tIPFilterNbrHostSharedFltrs"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsLogId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDescription"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsAction"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardNH"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardNHIndirect"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRemarkDSCP"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRemarkDSCPMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRemarkDot1p"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourceIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourceIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestinationIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestinationIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsProtocol"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourcePortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourcePortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourcePortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestPortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestPortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestPortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDSCP"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFragment"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsOptionPresent"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIpOptionValue"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIpOptionMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsMultipleOption"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsTcpSyn"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsTcpAck"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIcmpCode"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIcmpType"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsCflowdSample"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsCflowdIfSample"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardNHInterface"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIngressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsEgressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsLogInstantiated"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardRedPlcy"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsActiveDest"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSvcId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSapPortId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSapEncapVal"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSdpBind"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRedirectURL"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSrcIpFullMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestIpFullMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIngrHitByteCount"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsEgrHitByteCount"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesFilterType"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesFilterId"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesApplication"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesLocation"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesResult"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesFeedback"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesExecute"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdRtrId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSrcRouteOption"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsPortSelector"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSrcPortList"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDstPortList"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtTbleLstChgd"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtLastChanged"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtPktLenVal1"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtPktLenVal2"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtPktLenOper"))
)
if mibBuilder.loadTexts:
    tIPFilterV11v0Group.setStatus("obsolete")

tFilterNotificationObjV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 46)
)
tFilterNotificationObjV11v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterPBRDropReason"),
        ("TIMETRA-FILTER-MIB", "tFilterParmRow"),
        ("TIMETRA-FILTER-MIB", "tFilterAlarmDescription"),
        ("TIMETRA-FILTER-MIB", "tFilterId"),
        ("TIMETRA-FILTER-MIB", "tFilterType"),
        ("TIMETRA-FILTER-MIB", "tFilterSubInsSpaceOwner"),
        ("TIMETRA-FILTER-MIB", "tFilterThresholdReached"),
        ("TIMETRA-FILTER-MIB", "tFltrFlowSpecProblem"),
        ("TIMETRA-FILTER-MIB", "tFltrFlowSpecProblemDescription"),
        ("TIMETRA-FILTER-MIB", "tFltrFLowSpecNLRI"),
        ("TIMETRA-FILTER-MIB", "tFltrFlowSpecVrtrId"),
        ("TIMETRA-FILTER-MIB", "tFltrPrefixListType"),
        ("TIMETRA-FILTER-MIB", "tFltrPrefixListName"),
        ("TIMETRA-FILTER-MIB", "tFltrApplyPathSource"),
        ("TIMETRA-FILTER-MIB", "tFltrApplyPathIndex"),
        ("TIMETRA-FILTER-MIB", "tFltrNotifDescription"))
)
if mibBuilder.loadTexts:
    tFilterNotificationObjV11v0Group.setStatus("obsolete")

tIPFilterV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 47)
)
tIPFilterV12v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPFilterRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPFilterScope"),
        ("TIMETRA-FILTER-MIB", "tIPFilterDescription"),
        ("TIMETRA-FILTER-MIB", "tIPFilterDefaultAction"),
        ("TIMETRA-FILTER-MIB", "tIPFilterRadiusInsertPt"),
        ("TIMETRA-FILTER-MIB", "tIPFilterRadiusInsertSize"),
        ("TIMETRA-FILTER-MIB", "tIPFilterCreditCntrlInsertPt"),
        ("TIMETRA-FILTER-MIB", "tIPFilterCreditCntrlInsertSize"),
        ("TIMETRA-FILTER-MIB", "tIPFilterSubInsertHighWmark"),
        ("TIMETRA-FILTER-MIB", "tIPFilterSubInsertLowWmark"),
        ("TIMETRA-FILTER-MIB", "tIpFilterCreditCntrlNbrInsertd"),
        ("TIMETRA-FILTER-MIB", "tIpFilterRadiusNbrInsertd"),
        ("TIMETRA-FILTER-MIB", "tIPFilterHostSharedInsertPt"),
        ("TIMETRA-FILTER-MIB", "tIPFilterHostSharedInsertSize"),
        ("TIMETRA-FILTER-MIB", "tIpFilterHostSharedNbrInsertd"),
        ("TIMETRA-FILTER-MIB", "tIPFilterHostSharedHighWmark"),
        ("TIMETRA-FILTER-MIB", "tIPFilterHostSharedLowWmark"),
        ("TIMETRA-FILTER-MIB", "tIPFilterNbrHostSharedFltrs"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsLogId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDescription"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsAction"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardNH"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardNHIndirect"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRemarkDSCP"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRemarkDSCPMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRemarkDot1p"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourceIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourceIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestinationIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestinationIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsProtocol"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourcePortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourcePortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourcePortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestPortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestPortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestPortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDSCP"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFragment"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsOptionPresent"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIpOptionValue"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIpOptionMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsMultipleOption"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsTcpSyn"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsTcpAck"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIcmpCode"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIcmpType"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsCflowdSample"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsCflowdIfSample"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardNHInterface"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIngressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsEgressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsLogInstantiated"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardRedPlcy"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsActiveDest"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSvcId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSapPortId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSapEncapVal"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSdpBind"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRedirectURL"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSrcIpFullMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestIpFullMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIngrHitByteCount"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsEgrHitByteCount"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesFilterType"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesFilterId"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesApplication"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesLocation"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesResult"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesFeedback"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesExecute"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdRtrId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSrcRouteOption"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsPortSelector"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSrcPortList"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDstPortList"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtTbleLstChgd"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtLastChanged"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtPktLenVal1"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtPktLenVal2"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtPktLenOper"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRdirAllwRadOvrd"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsNatPolicyName"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdLsp"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdLspRtrId"))
)
if mibBuilder.loadTexts:
    tIPFilterV12v0Group.setStatus("obsolete")

tIPv6FilterV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 48)
)
tIPv6FilterV12v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPv6FilterRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterScope"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterDescription"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterDefaultAction"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterRadiusInsertPt"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterRadiusInsertSize"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterCreditCntrlInsertPt"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterCreditCntrlInsertSize"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterSubInsertHighWmark"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterSubInsertLowWmark"),
        ("TIMETRA-FILTER-MIB", "tIpv6FilterCreditCntrlNbrInsertd"),
        ("TIMETRA-FILTER-MIB", "tIpv6FilterRadiusNbrInsertd"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterHostSharedInsertPt"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterHostSharedInsertSize"),
        ("TIMETRA-FILTER-MIB", "tIpv6FilterHostSharedNbrInsertd"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterHostSharedHighWmark"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterHostSharedLowWmark"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterNbrHostSharedFltrs"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsLogId"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDescription"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsAction"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsForwardNH"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsForwardNHIndirect"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRemarkDSCP"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRemarkDSCPMask"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRemarkDot1p"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourceIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourceIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestinationIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestinationIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsNextHeader"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourcePortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourcePortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourcePortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestPortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestPortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestPortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDSCP"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsTcpSyn"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsTcpAck"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsIcmpCode"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsIcmpType"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsCflowdSample"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsCflowdIfSample"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsForwardNHInterface"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsIngressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsEgressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsLogInstantiated"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsForwardRedPlcy"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsActiveDest"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsIngrHitByteCount"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsEgrHitByteCount"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFwdSvcId"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFwdSapPortId"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFwdSapEncapVal"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFwdSdpBind"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRedirectURL"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSrcIpPrefixList"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDstIpPrefixList"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFragment"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsHopByHopOpt"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRoutingType0"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsPortSelector"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSrcPortList"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDstPortList"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRdirAllwRadOvrd"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFwdRtrId"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSrcIpFullMask"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDstIpFullMask"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsNatPolicyName"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFlowLabel"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFlowLabelMask"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFwdLspRtrId"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFwdLsp"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtTbleLstChgd"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtLastChanged"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtAhExtHdr"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtEspExtHdr"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtNatType"))
)
if mibBuilder.loadTexts:
    tIPv6FilterV12v0Group.setStatus("obsolete")

tLiFilterV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 49)
)
tLiFilterV12v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tLiReservedBlockRowStatus"),
        ("TIMETRA-FILTER-MIB", "tLiReservedBlockDescription"),
        ("TIMETRA-FILTER-MIB", "tLiReservedBlockStart"),
        ("TIMETRA-FILTER-MIB", "tLiReservedBlockSize"),
        ("TIMETRA-FILTER-MIB", "tLiReservedBlockLastChanged"),
        ("TIMETRA-FILTER-MIB", "tLiReservedBlockTableLastChanged"),
        ("TIMETRA-FILTER-MIB", "tLiReservedBlockFltrRowStatus"),
        ("TIMETRA-FILTER-MIB", "tLiReservedBlockFltrLastChanged"),
        ("TIMETRA-FILTER-MIB", "tLiReservedBlockFltrTableLastChg"),
        ("TIMETRA-FILTER-MIB", "tLiFilterDescription"),
        ("TIMETRA-FILTER-MIB", "tLiFilterRowStatus"),
        ("TIMETRA-FILTER-MIB", "tLiFilterLastChanged"),
        ("TIMETRA-FILTER-MIB", "tLiFilterTableLastChanged"),
        ("TIMETRA-FILTER-MIB", "tLiFilterAssociationRowStatus"),
        ("TIMETRA-FILTER-MIB", "tLiFilterAssociationLastChg"),
        ("TIMETRA-FILTER-MIB", "tLiFilterAssociationTableLastChg"),
        ("TIMETRA-FILTER-MIB", "tLiMacFilterParamsDescription"),
        ("TIMETRA-FILTER-MIB", "tLiMacFilterParamsDstMAC"),
        ("TIMETRA-FILTER-MIB", "tLiMacFilterParamsDstMACMask"),
        ("TIMETRA-FILTER-MIB", "tLiMacFilterParamsFrameType"),
        ("TIMETRA-FILTER-MIB", "tLiMacFilterParamsRowStatus"),
        ("TIMETRA-FILTER-MIB", "tLiMacFilterParamsSrcMAC"),
        ("TIMETRA-FILTER-MIB", "tLiMacFilterParamsSrcMACMask"),
        ("TIMETRA-FILTER-MIB", "tLiMacFilterParamsLastChanged"),
        ("TIMETRA-FILTER-MIB", "tLiMacFilterParamsTableLastChg"),
        ("TIMETRA-FILTER-MIB", "tLiMacFilterParamsIngrHitCount"),
        ("TIMETRA-FILTER-MIB", "tLiMacFilterParamsEgrHitCount"),
        ("TIMETRA-FILTER-MIB", "tLiMacFilterParamsIngrHitBytes"),
        ("TIMETRA-FILTER-MIB", "tLiMacFilterParamsEgrHitBytes"),
        ("TIMETRA-FILTER-MIB", "tLiIpFilterParamsTableLastChg"),
        ("TIMETRA-FILTER-MIB", "tLiIpFilterParamsLastChanged"),
        ("TIMETRA-FILTER-MIB", "tLiIpFilterParamsRowStatus"),
        ("TIMETRA-FILTER-MIB", "tLiIpFilterParamsDescription"),
        ("TIMETRA-FILTER-MIB", "tLiIpFilterParamsSrcIpAddrType"),
        ("TIMETRA-FILTER-MIB", "tLiIpFilterParamsSrcIpAddr"),
        ("TIMETRA-FILTER-MIB", "tLiIpFilterParamsSrcIpFullMask"),
        ("TIMETRA-FILTER-MIB", "tLiIpFilterParamsDstIpAddrType"),
        ("TIMETRA-FILTER-MIB", "tLiIpFilterParamsDstIpAddr"),
        ("TIMETRA-FILTER-MIB", "tLiIpFilterParamsDstIpFullMask"),
        ("TIMETRA-FILTER-MIB", "tLiIpFilterParamsProtocolNextHdr"),
        ("TIMETRA-FILTER-MIB", "tLiIpFilterParamsSrcPortValue1"),
        ("TIMETRA-FILTER-MIB", "tLiIpFilterParamsSrcPortValue2"),
        ("TIMETRA-FILTER-MIB", "tLiIpFilterParamsSrcPortOper"),
        ("TIMETRA-FILTER-MIB", "tLiIpFilterParamsDstPortValue1"),
        ("TIMETRA-FILTER-MIB", "tLiIpFilterParamsDstPortValue2"),
        ("TIMETRA-FILTER-MIB", "tLiIpFilterParamsDstPortOper"),
        ("TIMETRA-FILTER-MIB", "tLiIpFltrParamsInfIngrHitCount"),
        ("TIMETRA-FILTER-MIB", "tLiIpFltrParamsInfEgrHitCount"),
        ("TIMETRA-FILTER-MIB", "tLiIpFltrParamsInfIngrHitBytes"),
        ("TIMETRA-FILTER-MIB", "tLiIpFltrParamsInfEgrHitBytes"))
)
if mibBuilder.loadTexts:
    tLiFilterV12v0Group.setStatus("current")

tFilterEmbeddedInsertV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 50)
)
tFilterEmbeddedInsertV12v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterEmbedOpenflowRowStatus"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbedOpenflowTableLstChg"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbedOpenflowOperState"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbedOpenflowAdminState"),
        ("TIMETRA-FILTER-MIB", "tFltrEmbedOfInfoEntryCnt"),
        ("TIMETRA-FILTER-MIB", "tFltrEmbedOfInfoEntryCntInsrtd"),
        ("TIMETRA-FILTER-MIB", "tFltrEmbedOfEntryInsrtEntryId"),
        ("TIMETRA-FILTER-MIB", "tFltrEmbedOfEntryInsrtEntryState"))
)
if mibBuilder.loadTexts:
    tFilterEmbeddedInsertV12v0Group.setStatus("current")

tFilterRedirectPolicyV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 52)
)
tFilterRedirectPolicyV13v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterRPVrtrId"),
        ("TIMETRA-FILTER-MIB", "tFilterRPRowStatus"),
        ("TIMETRA-FILTER-MIB", "tFilterRPDescription"),
        ("TIMETRA-FILTER-MIB", "tFilterRPAdminState"),
        ("TIMETRA-FILTER-MIB", "tFilterRPActiveDestAddrType"),
        ("TIMETRA-FILTER-MIB", "tFilterRPActiveDestAddr"),
        ("TIMETRA-FILTER-MIB", "tFilterRPDstStickiness"),
        ("TIMETRA-FILTER-MIB", "tFilterRPBestDstAddrType"),
        ("TIMETRA-FILTER-MIB", "tFilterRPBestDstAddr"),
        ("TIMETRA-FILTER-MIB", "tFilterRPStickinessHoldRemain"),
        ("TIMETRA-FILTER-MIB", "tFilterRPlcyDstTableLastChg"),
        ("TIMETRA-FILTER-MIB", "tFltrRPDstLastChanged"),
        ("TIMETRA-FILTER-MIB", "tFltrRPDstRowStatus"),
        ("TIMETRA-FILTER-MIB", "tFltrRPDstDescription"),
        ("TIMETRA-FILTER-MIB", "tFltrRPDstAdminPriority"),
        ("TIMETRA-FILTER-MIB", "tFltrRPDstOperPriority"),
        ("TIMETRA-FILTER-MIB", "tFltrRPDstAdminState"),
        ("TIMETRA-FILTER-MIB", "tFltrRPDstOperState"),
        ("TIMETRA-FILTER-MIB", "tFilterRPlcyPingTestTableLastChg"),
        ("TIMETRA-FILTER-MIB", "tFltrRPPingTLastChanged"),
        ("TIMETRA-FILTER-MIB", "tFltrRPPingTRowStatus"),
        ("TIMETRA-FILTER-MIB", "tFltrRPPingTInterval"),
        ("TIMETRA-FILTER-MIB", "tFltrRPPingTTimeout"),
        ("TIMETRA-FILTER-MIB", "tFltrRPPingTDropCount"),
        ("TIMETRA-FILTER-MIB", "tFltrRPPingTHoldDown"),
        ("TIMETRA-FILTER-MIB", "tFltrRPPingTHoldDownRemain"),
        ("TIMETRA-FILTER-MIB", "tFltrRPPingTLastActionTime"),
        ("TIMETRA-FILTER-MIB", "tFltrRPPingTLastAction"),
        ("TIMETRA-FILTER-MIB", "tFilterRPlcySNMPTestTableLastChg"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpTLastChanged"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpTRowStatus"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpTOID"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpTCommunity"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpTSnmpVersion"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpTInterval"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpTTimeout"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpTDropCount"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpTHoldDown"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpTHoldDownRemain"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpTLastActionTime"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpTLastOID"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpTLastType"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpTLastCounter32Val"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpTLastUnsigned32Val"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpTLastTimeTicksVal"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpTLastInt32Val"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpTLastOctetStringVal"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpTLastIpAddressVal"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpTLastOidVal"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpTLastCounter64Val"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpTLastOpaqueVal"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpTLastAction"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpTLastPrioChange"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpTNextRespIndex"),
        ("TIMETRA-FILTER-MIB", "tFilterRPlcySNMPRespTableLastChg"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpRspLastChanged"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpRspRowStatus"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpRspAction"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpRspPrioChange"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpRspOID"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpRspType"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpRspCounter32Val"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpRspUnsigned32Val"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpRspTimeTicksVal"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpRspInt32Val"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpRspOctetStringVal"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpRspIpAddressVal"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpRspOidVal"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpRspCounter64Val"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpRspOpaqueVal"),
        ("TIMETRA-FILTER-MIB", "tFilterRPlcyURLTestTableLastChg"),
        ("TIMETRA-FILTER-MIB", "tFltrRPUrlTLastChanged"),
        ("TIMETRA-FILTER-MIB", "tFltrRPUrlTRowStatus"),
        ("TIMETRA-FILTER-MIB", "tFltrRPUrlTUrl"),
        ("TIMETRA-FILTER-MIB", "tFltrRPUrlTHttpVersion"),
        ("TIMETRA-FILTER-MIB", "tFltrRPUrlTInterval"),
        ("TIMETRA-FILTER-MIB", "tFltrRPUrlTTimeout"),
        ("TIMETRA-FILTER-MIB", "tFltrRPUrlTDropCount"),
        ("TIMETRA-FILTER-MIB", "tFltrRPUrlTHoldDown"),
        ("TIMETRA-FILTER-MIB", "tFltrRPUrlTHoldDownRemain"),
        ("TIMETRA-FILTER-MIB", "tFltrRPUrlTLastActionTime"),
        ("TIMETRA-FILTER-MIB", "tFltrRPUrlTLastRetCode"),
        ("TIMETRA-FILTER-MIB", "tFltrRPUrlTLastAction"),
        ("TIMETRA-FILTER-MIB", "tFltrRPUrlTLastPrioChange"),
        ("TIMETRA-FILTER-MIB", "tFilterRPlcyURLRespTableLastChg"),
        ("TIMETRA-FILTER-MIB", "tFltrRPUrlTRspLastChanged"),
        ("TIMETRA-FILTER-MIB", "tFltrRPUrlTRspRowStatus"),
        ("TIMETRA-FILTER-MIB", "tFltrRPUrlTRspAction"),
        ("TIMETRA-FILTER-MIB", "tFltrRPUrlTRspPrioChange"),
        ("TIMETRA-FILTER-MIB", "tFilterRPlcyUcastRtTTableLastChg"),
        ("TIMETRA-FILTER-MIB", "tFltrRPUcastRtTLastChanged"),
        ("TIMETRA-FILTER-MIB", "tFltrRPUcastRtTRowStatus"),
        ("TIMETRA-FILTER-MIB", "tFltrRPUcastRtTLastActionTime"),
        ("TIMETRA-FILTER-MIB", "tFltrRPUcastRtTLastAction"))
)
if mibBuilder.loadTexts:
    tFilterRedirectPolicyV13v0Group.setStatus("obsolete")

tFilterNotificationObjV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 53)
)
tFilterNotificationObjV12v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterPBRDropReason"),
        ("TIMETRA-FILTER-MIB", "tFilterParmRow"),
        ("TIMETRA-FILTER-MIB", "tFilterAlarmDescription"),
        ("TIMETRA-FILTER-MIB", "tFilterId"),
        ("TIMETRA-FILTER-MIB", "tFilterType"),
        ("TIMETRA-FILTER-MIB", "tFilterSubInsSpaceOwner"),
        ("TIMETRA-FILTER-MIB", "tFilterThresholdReached"),
        ("TIMETRA-FILTER-MIB", "tFltrFlowSpecProblem"),
        ("TIMETRA-FILTER-MIB", "tFltrFlowSpecProblemDescription"),
        ("TIMETRA-FILTER-MIB", "tFltrFLowSpecNLRI"),
        ("TIMETRA-FILTER-MIB", "tFltrFlowSpecVrtrId"),
        ("TIMETRA-FILTER-MIB", "tFltrPrefixListType"),
        ("TIMETRA-FILTER-MIB", "tFltrPrefixListName"),
        ("TIMETRA-FILTER-MIB", "tFltrApplyPathSource"),
        ("TIMETRA-FILTER-MIB", "tFltrApplyPathIndex"),
        ("TIMETRA-FILTER-MIB", "tFltrNotifDescription"),
        ("TIMETRA-FILTER-MIB", "tFltrMdaId"))
)
if mibBuilder.loadTexts:
    tFilterNotificationObjV12v0Group.setStatus("current")

tIPFilterV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 54)
)
tIPFilterV13v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPFilterParamsExtTbleLstChgd"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtLastChanged"),
        ("TIMETRA-FILTER-MIB", "tIPFilterSharedPccRuleInsrtPt"),
        ("TIMETRA-FILTER-MIB", "tIPFilterSharedPccRuleInsrtSize"),
        ("TIMETRA-FILTER-MIB", "tIPFilterSharedPccRuleNbrInsrtd"),
        ("TIMETRA-FILTER-MIB", "tIPFilterChainToSystemFilter"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtTTLVal1"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtTTLVal2"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtTTLOper"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtEgressPBR"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtEsi"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtFwdEsiSvcId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtFwdEsiVRtrId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtFwdEsiSFIp"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtPbrDwnActOvr"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtFwdEsiVasIf"))
)
if mibBuilder.loadTexts:
    tIPFilterV13v0Group.setStatus("obsolete")

tIPv6FilterV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 55)
)
tIPv6FilterV13v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtPktLenVal1"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtPktLenVal2"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtPktLenOper"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterSharedPccRuleInsrtPt"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterSharedPccRuleInsrtSiz"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterSharedPccRuleNbrInsrt"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterChainToSystemFilter"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtHopLimitVal1"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtHopLimitVal2"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtHopLimitOper"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtEgressPBR"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtEsi"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtFwdEsiSvcId"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtFwdEsiVRtrId"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtFwdEsiSFIp"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtPbrDwnActOvr"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtFwdEsiVasIf"))
)
if mibBuilder.loadTexts:
    tIPv6FilterV13v0Group.setStatus("obsolete")

tFilterRPlcyV13v0ObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 56)
)
tFilterRPlcyV13v0ObsoleteGroup.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterRPActiveDest"),
        ("TIMETRA-FILTER-MIB", "tFilterRDRowStatus"),
        ("TIMETRA-FILTER-MIB", "tFilterRDDescription"),
        ("TIMETRA-FILTER-MIB", "tFilterRDAdminPriority"),
        ("TIMETRA-FILTER-MIB", "tFilterRDOperPriority"),
        ("TIMETRA-FILTER-MIB", "tFilterRDAdminState"),
        ("TIMETRA-FILTER-MIB", "tFilterRDOperState"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTRowStatus"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTOID"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTCommunity"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTSNMPVersion"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTInterval"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTTimeout"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTDropCount"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTHoldDown"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTHoldDownRemain"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTLastActionTime"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTLastOID"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTLastType"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTLastCounter32Val"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTLastUnsigned32Val"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTLastTimeTicksVal"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTLastInt32Val"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTLastOctetStringVal"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTLastIpAddressVal"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTLastOidVal"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTLastCounter64Val"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTLastOpaqueVal"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTLastAction"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTLastPrioChange"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTNextRespIndex"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTRespRowStatus"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTRespAction"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTRespPrioChange"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTRespOID"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTRespType"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTCounter32Val"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTUnsigned32Val"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTTimeTicksVal"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTInt32Val"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTOctetStringVal"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTIpAddressVal"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTOidVal"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTCounter64Val"),
        ("TIMETRA-FILTER-MIB", "tFilterRSTOpaqueVal"),
        ("TIMETRA-FILTER-MIB", "tFilterRUTRowStatus"),
        ("TIMETRA-FILTER-MIB", "tFilterRUTURL"),
        ("TIMETRA-FILTER-MIB", "tFilterRUTHTTPVersion"),
        ("TIMETRA-FILTER-MIB", "tFilterRUTInterval"),
        ("TIMETRA-FILTER-MIB", "tFilterRUTTimeout"),
        ("TIMETRA-FILTER-MIB", "tFilterRUTDropCount"),
        ("TIMETRA-FILTER-MIB", "tFilterRUTHoldDown"),
        ("TIMETRA-FILTER-MIB", "tFilterRUTHoldDownRemain"),
        ("TIMETRA-FILTER-MIB", "tFilterRUTLastActionTime"),
        ("TIMETRA-FILTER-MIB", "tFilterRUTLastRetCode"),
        ("TIMETRA-FILTER-MIB", "tFilterRUTLastAction"),
        ("TIMETRA-FILTER-MIB", "tFilterRUTLastPrioChange"),
        ("TIMETRA-FILTER-MIB", "tFilterRUTRespRowStatus"),
        ("TIMETRA-FILTER-MIB", "tFilterRUTRespAction"),
        ("TIMETRA-FILTER-MIB", "tFilterRUTRespPrioChange"),
        ("TIMETRA-FILTER-MIB", "tFilterRPTRowStatus"),
        ("TIMETRA-FILTER-MIB", "tFilterRPTInterval"),
        ("TIMETRA-FILTER-MIB", "tFilterRPTTimeout"),
        ("TIMETRA-FILTER-MIB", "tFilterRPTDropCount"),
        ("TIMETRA-FILTER-MIB", "tFilterRPTHoldDown"),
        ("TIMETRA-FILTER-MIB", "tFilterRPTHoldDownRemain"),
        ("TIMETRA-FILTER-MIB", "tFilterRPTLastActionTime"),
        ("TIMETRA-FILTER-MIB", "tFilterRPTLastAction"))
)
if mibBuilder.loadTexts:
    tFilterRPlcyV13v0ObsoleteGroup.setStatus("current")

tFilterSystemFilterV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 57)
)
tFilterSystemFilterV13v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterSystemFilterTableLastChg"),
        ("TIMETRA-FILTER-MIB", "tFilterSystemFilterLastChanged"),
        ("TIMETRA-FILTER-MIB", "tFilterSystemFilterRowStatus"))
)
if mibBuilder.loadTexts:
    tFilterSystemFilterV13v0Group.setStatus("current")

tFilterEmbeddedInsertV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 58)
)
tFilterEmbeddedInsertV13v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterEmbedOflowSvcContext"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbedOflowSapContextPort"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbedOflowSapContextEncap"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbedOflowContextType"))
)
if mibBuilder.loadTexts:
    tFilterEmbeddedInsertV13v0Group.setStatus("current")

tDhcpFilterV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 59)
)
tDhcpFilterV13v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tDhcpFilterDefAction"),
        ("TIMETRA-FILTER-MIB", "tDhcp6FilterTblLastChanged"),
        ("TIMETRA-FILTER-MIB", "tDhcp6FilterRowStatus"),
        ("TIMETRA-FILTER-MIB", "tDhcp6FilterLastChanged"),
        ("TIMETRA-FILTER-MIB", "tDhcp6FilterDescription"),
        ("TIMETRA-FILTER-MIB", "tDhcp6FilterDefAction"),
        ("TIMETRA-FILTER-MIB", "tDhcp6FilterParamsTblLastChanged"),
        ("TIMETRA-FILTER-MIB", "tDhcp6FilterParamsRowStatus"),
        ("TIMETRA-FILTER-MIB", "tDhcp6FilterParamsLastChanged"),
        ("TIMETRA-FILTER-MIB", "tDhcp6FilterParamsOptionNumber"),
        ("TIMETRA-FILTER-MIB", "tDhcp6FilterParamsOptionMatch"),
        ("TIMETRA-FILTER-MIB", "tDhcp6FilterParamsAction"),
        ("TIMETRA-FILTER-MIB", "tDhcp6FilterParamsOptionValue"),
        ("TIMETRA-FILTER-MIB", "tDhcp6FilterDefActionFlags"),
        ("TIMETRA-FILTER-MIB", "tDhcp6FilterParamsActionFlags"))
)
if mibBuilder.loadTexts:
    tDhcpFilterV13v0Group.setStatus("current")

tMacFilterV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 60)
)
tMacFilterV13v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tMacFilterParamsEsi"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsFwdEsiSvcId"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsPbrDwnActOvr"))
)
if mibBuilder.loadTexts:
    tMacFilterV13v0Group.setStatus("obsolete")

tFilterEmbedFlowspecGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 62)
)
tFilterEmbedFlowspecGroup.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterEmbedFlowspecTableLstChg"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbedFlowspecRowStatus"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbedFlowspecLastChanged"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbedFlowspecRtrId"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbedFlowspecAdminState"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbedFlowspecOperState"),
        ("TIMETRA-FILTER-MIB", "tFltrEmbFlowSpecInfoFltrId"),
        ("TIMETRA-FILTER-MIB", "tFltrEmbFlowSpecInfoEntryCnt"),
        ("TIMETRA-FILTER-MIB", "tFltrEmbFlowSpecInfoEntryCntIns"),
        ("TIMETRA-FILTER-MIB", "tFltrEmbFlowspecEntryInsEntryId"),
        ("TIMETRA-FILTER-MIB", "tFltrEmbFlowspecEntryOperState"))
)
if mibBuilder.loadTexts:
    tFilterEmbedFlowspecGroup.setStatus("current")

tFilterIPvXRedundantActionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 63)
)
tFilterIPvXRedundantActionGroup.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPvXFltrEntryActionTblLChg"),
        ("TIMETRA-FILTER-MIB", "tIPvXFltrEntryActRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPvXFltrEntryActLastChanged"),
        ("TIMETRA-FILTER-MIB", "tIPvXFltrEntryActAction"),
        ("TIMETRA-FILTER-MIB", "tIPvXFltrEntryActFwdNHIpAddrType"),
        ("TIMETRA-FILTER-MIB", "tIPvXFltrEntryActFwdNHIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPvXFltrEntryActFwdNHIndirect"),
        ("TIMETRA-FILTER-MIB", "tIPvXFltrEntryActFwdNHInterface"),
        ("TIMETRA-FILTER-MIB", "tIPvXFltrEntryActFwdRedPlcy"),
        ("TIMETRA-FILTER-MIB", "tIPvXFltrEntryActFwdSapPortId"),
        ("TIMETRA-FILTER-MIB", "tIPvXFltrEntryActFwdSapEncapVal"),
        ("TIMETRA-FILTER-MIB", "tIPvXFltrEntryActFwdSdpBind"),
        ("TIMETRA-FILTER-MIB", "tIPvXFltrEntryActRedirectURL"),
        ("TIMETRA-FILTER-MIB", "tIPvXFltrEntryActRdirAllwRadOvr"),
        ("TIMETRA-FILTER-MIB", "tIPvXFltrEntryActFwdRtrId"),
        ("TIMETRA-FILTER-MIB", "tIPvXFltrEntryActNatPolicyName"),
        ("TIMETRA-FILTER-MIB", "tIPvXFltrEntryActNatType"),
        ("TIMETRA-FILTER-MIB", "tIPvXFltrEntryActFwdLsp"),
        ("TIMETRA-FILTER-MIB", "tIPvXFltrEntryActFwdLspRtrId"),
        ("TIMETRA-FILTER-MIB", "tIPvXFltrEntryActPktLenVal1"),
        ("TIMETRA-FILTER-MIB", "tIPvXFltrEntryActPktLenVal2"),
        ("TIMETRA-FILTER-MIB", "tIPvXFltrEntryActPktLenOper"),
        ("TIMETRA-FILTER-MIB", "tIPvXFltrEntryActTTLVal1"),
        ("TIMETRA-FILTER-MIB", "tIPvXFltrEntryActTTLVal2"),
        ("TIMETRA-FILTER-MIB", "tIPvXFltrEntryActTTLOper"),
        ("TIMETRA-FILTER-MIB", "tIPvXFltrEntryActEsi"),
        ("TIMETRA-FILTER-MIB", "tIPvXFltrEntryActFwdEsiSvcId"),
        ("TIMETRA-FILTER-MIB", "tIPvXFltrEntryActFwdEsiVRtrId"),
        ("TIMETRA-FILTER-MIB", "tIPvXFltrEntryActFwdEsiSFIpType"),
        ("TIMETRA-FILTER-MIB", "tIPvXFltrEntryActFwdEsiSFIp"),
        ("TIMETRA-FILTER-MIB", "tIPvXFltrEntryActFwdEsiVasIf"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtStickyDst"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtDownloadAct"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtHoldRemain"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtStickyDst"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtDownloadAct"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtHoldRemain"),
        ("TIMETRA-FILTER-MIB", "tIPvXFltrEntryActPbrTargetStatus"),
        ("TIMETRA-FILTER-MIB", "tIPvXFltrEntryActRateLimit"))
)
if mibBuilder.loadTexts:
    tFilterIPvXRedundantActionGroup.setStatus("current")

tFilterMacRedundantActionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 64)
)
tFilterMacRedundantActionGroup.setObjects(
      *(("TIMETRA-FILTER-MIB", "tMacFltrEntryActionTblLChg"),
        ("TIMETRA-FILTER-MIB", "tMacFltrEntryActRowStatus"),
        ("TIMETRA-FILTER-MIB", "tMacFltrEntryActLastChanged"),
        ("TIMETRA-FILTER-MIB", "tMacFltrEntryActAction"),
        ("TIMETRA-FILTER-MIB", "tMacFltrEntryActRowStatus"),
        ("TIMETRA-FILTER-MIB", "tMacFltrEntryActFwdSapPortId"),
        ("TIMETRA-FILTER-MIB", "tMacFltrEntryActFwdSapEncapVal"),
        ("TIMETRA-FILTER-MIB", "tMacFltrEntryActFwdSdpBind"),
        ("TIMETRA-FILTER-MIB", "tMacFltrEntryActRedirectURL"),
        ("TIMETRA-FILTER-MIB", "tMacFltrEntryActEsi"),
        ("TIMETRA-FILTER-MIB", "tMacFltrEntryActFwdEsiSvcId"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsStickyDst"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsHoldRemain"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsDownloadAct"),
        ("TIMETRA-FILTER-MIB", "tMacFltrEntryActPbrTargetStatus"),
        ("TIMETRA-FILTER-MIB", "tMacFltrEntryActRateLimit"))
)
if mibBuilder.loadTexts:
    tFilterMacRedundantActionGroup.setStatus("current")

tFilterEmbedVsdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 65)
)
tFilterEmbedVsdGroup.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterEmbedVsdTableLstChg"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbedVsdRowStatus"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbedVsdLastChanged"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbedVsdAdminState"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbedVsdOperState"),
        ("TIMETRA-FILTER-MIB", "tFltrEmbedVsdInfoEntryCnt"),
        ("TIMETRA-FILTER-MIB", "tFltrEmbedVsdInfoEntryCntInsrtd"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbedVsdEntryInsrtEntryId"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbedVsdEntryOperState"))
)
if mibBuilder.loadTexts:
    tFilterEmbedVsdGroup.setStatus("current")

tFilterEmbeddedRefGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 66)
)
tFilterEmbeddedRefGroup.setObjects(
    ("TIMETRA-FILTER-MIB", "tFilterEmbeddedRefLastChanged")
)
if mibBuilder.loadTexts:
    tFilterEmbeddedRefGroup.setStatus("current")

tFilterTimeRangeObsoletedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 67)
)
tFilterTimeRangeObsoletedGroup.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPFilterParamsTimeRangeName"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsTimeRangeState"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsTimeRangeName"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsTimeRangeState"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsTimeRangeName"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsTimeRangeState"))
)
if mibBuilder.loadTexts:
    tFilterTimeRangeObsoletedGroup.setStatus("current")

tFilterEntryStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 69)
)
tFilterEntryStatGroup.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFltrEntryStatIngHitCnt"),
        ("TIMETRA-FILTER-MIB", "tFltrEntryStatEgrHitCnt"),
        ("TIMETRA-FILTER-MIB", "tFltrEntryStatIngHitCntB"),
        ("TIMETRA-FILTER-MIB", "tFltrEntryStatEgrHitCntB"),
        ("TIMETRA-FILTER-MIB", "tFltrEntryStatRateLmtIngHitCnt"),
        ("TIMETRA-FILTER-MIB", "tFltrEntryStatRateLmtIngDrop"),
        ("TIMETRA-FILTER-MIB", "tFltrEntryStatRateLmtIngFwd"),
        ("TIMETRA-FILTER-MIB", "tFltrEntryStatRateLmtIngHitCntB"),
        ("TIMETRA-FILTER-MIB", "tFltrEntryStatRateLmtIngDropB"),
        ("TIMETRA-FILTER-MIB", "tFltrEntryStatRateLmtIngFwdB"),
        ("TIMETRA-FILTER-MIB", "tFltrEntryStatRateLmtEgrHitCnt"),
        ("TIMETRA-FILTER-MIB", "tFltrEntryStatRateLmtEgrDrop"),
        ("TIMETRA-FILTER-MIB", "tFltrEntryStatRateLmtEgrFwd"),
        ("TIMETRA-FILTER-MIB", "tFltrEntryStatRateLmtEgrHitCntB"),
        ("TIMETRA-FILTER-MIB", "tFltrEntryStatRateLmtEgrDropB"),
        ("TIMETRA-FILTER-MIB", "tFltrEntryStatRateLmtEgrFwdB"))
)
if mibBuilder.loadTexts:
    tFilterEntryStatGroup.setStatus("current")

tFilterRemarkDscpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 70)
)
tFilterRemarkDscpGroup.setObjects(
    ("TIMETRA-FILTER-MIB", "tIPvXFltrEntryActRemarkDSCP")
)
if mibBuilder.loadTexts:
    tFilterRemarkDscpGroup.setStatus("current")

tIPFilterV14v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 71)
)
tIPFilterV14v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPFilterRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPFilterScope"),
        ("TIMETRA-FILTER-MIB", "tIPFilterDescription"),
        ("TIMETRA-FILTER-MIB", "tIPFilterDefaultAction"),
        ("TIMETRA-FILTER-MIB", "tIPFilterRadiusInsertPt"),
        ("TIMETRA-FILTER-MIB", "tIPFilterRadiusInsertSize"),
        ("TIMETRA-FILTER-MIB", "tIPFilterCreditCntrlInsertPt"),
        ("TIMETRA-FILTER-MIB", "tIPFilterCreditCntrlInsertSize"),
        ("TIMETRA-FILTER-MIB", "tIPFilterSubInsertHighWmark"),
        ("TIMETRA-FILTER-MIB", "tIPFilterSubInsertLowWmark"),
        ("TIMETRA-FILTER-MIB", "tIpFilterCreditCntrlNbrInsertd"),
        ("TIMETRA-FILTER-MIB", "tIpFilterRadiusNbrInsertd"),
        ("TIMETRA-FILTER-MIB", "tIPFilterHostSharedInsertPt"),
        ("TIMETRA-FILTER-MIB", "tIPFilterHostSharedInsertSize"),
        ("TIMETRA-FILTER-MIB", "tIpFilterHostSharedNbrInsertd"),
        ("TIMETRA-FILTER-MIB", "tIPFilterHostSharedHighWmark"),
        ("TIMETRA-FILTER-MIB", "tIPFilterHostSharedLowWmark"),
        ("TIMETRA-FILTER-MIB", "tIPFilterNbrHostSharedFltrs"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsLogId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDescription"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsAction"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardNH"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardNHIndirect"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourceIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourceIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestinationIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestinationIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsProtocol"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourcePortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourcePortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourcePortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestPortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestPortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestPortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDSCP"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFragment"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsOptionPresent"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIpOptionValue"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIpOptionMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsMultipleOption"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsTcpSyn"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsTcpAck"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIcmpCode"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIcmpType"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsCflowdSample"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsCflowdIfSample"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardNHInterface"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIngressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsEgressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsLogInstantiated"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardRedPlcy"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsActiveDest"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSvcId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSapPortId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSapEncapVal"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSdpBind"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRedirectURL"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSrcIpFullMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestIpFullMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIngrHitByteCount"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsEgrHitByteCount"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesFilterType"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesFilterId"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesApplication"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesLocation"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesResult"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesFeedback"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesExecute"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdRtrId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSrcRouteOption"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsPortSelector"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSrcPortList"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDstPortList"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtTbleLstChgd"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtLastChanged"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtPktLenVal1"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtPktLenVal2"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtPktLenOper"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRdirAllwRadOvrd"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsNatPolicyName"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdLsp"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdLspRtrId"))
)
if mibBuilder.loadTexts:
    tIPFilterV14v0Group.setStatus("obsolete")

tIPv6FilterV14v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 72)
)
tIPv6FilterV14v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPv6FilterRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterScope"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterDescription"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterDefaultAction"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterRadiusInsertPt"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterRadiusInsertSize"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterCreditCntrlInsertPt"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterCreditCntrlInsertSize"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterSubInsertHighWmark"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterSubInsertLowWmark"),
        ("TIMETRA-FILTER-MIB", "tIpv6FilterCreditCntrlNbrInsertd"),
        ("TIMETRA-FILTER-MIB", "tIpv6FilterRadiusNbrInsertd"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterHostSharedInsertPt"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterHostSharedInsertSize"),
        ("TIMETRA-FILTER-MIB", "tIpv6FilterHostSharedNbrInsertd"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterHostSharedHighWmark"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterHostSharedLowWmark"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterNbrHostSharedFltrs"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsLogId"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDescription"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsAction"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsForwardNH"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsForwardNHIndirect"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourceIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourceIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestinationIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestinationIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsNextHeader"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourcePortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourcePortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourcePortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestPortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestPortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestPortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDSCP"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsTcpSyn"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsTcpAck"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsIcmpCode"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsIcmpType"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsCflowdSample"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsCflowdIfSample"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsForwardNHInterface"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsIngressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsEgressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsLogInstantiated"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsForwardRedPlcy"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsActiveDest"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsIngrHitByteCount"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsEgrHitByteCount"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFwdSvcId"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFwdSapPortId"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFwdSapEncapVal"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFwdSdpBind"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRedirectURL"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSrcIpPrefixList"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDstIpPrefixList"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFragment"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsHopByHopOpt"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRoutingType0"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsPortSelector"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSrcPortList"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDstPortList"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRdirAllwRadOvrd"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFwdRtrId"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSrcIpFullMask"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDstIpFullMask"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsNatPolicyName"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFlowLabel"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFlowLabelMask"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFwdLspRtrId"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFwdLsp"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtTbleLstChgd"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtLastChanged"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtAhExtHdr"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtEspExtHdr"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtNatType"))
)
if mibBuilder.loadTexts:
    tIPv6FilterV14v0Group.setStatus("obsolete")

tFilterParamsObsoletedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 73)
)
tFilterParamsObsoletedGroup.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPFilterParamsRemarkDSCP"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRemarkDSCPMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRemarkDot1p"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRemarkDSCP"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRemarkDSCPMask"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRemarkDot1p"))
)
if mibBuilder.loadTexts:
    tFilterParamsObsoletedGroup.setStatus("current")

tFilterRemarkDscpExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 74)
)
tFilterRemarkDscpExtGroup.setObjects(
    ("TIMETRA-FILTER-MIB", "tIPvXFltrEntryActActionExt")
)
if mibBuilder.loadTexts:
    tFilterRemarkDscpExtGroup.setStatus("current")

tFilterPrefListRtrBgpPeersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 75)
)
tFilterPrefListRtrBgpPeersGroup.setObjects(
    ("TIMETRA-FILTER-MIB", "tFilterApplyPathVRtrId")
)
if mibBuilder.loadTexts:
    tFilterPrefListRtrBgpPeersGroup.setStatus("current")

tFilterPrefListInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 76)
)
tFilterPrefListInfoGroup.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFltrPrefListInfoPrefixOwner"),
        ("TIMETRA-FILTER-MIB", "tFltrPrefListInfoPrefixProg"))
)
if mibBuilder.loadTexts:
    tFilterPrefListInfoGroup.setStatus("current")

tFilterForwardVprnTargetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 77)
)
tFilterForwardVprnTargetGroup.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPvXFltrEntryActFwdVprnTgtBgNHT"),
        ("TIMETRA-FILTER-MIB", "tIPvXFltrEntryActFwdVprnTgtBgNH"),
        ("TIMETRA-FILTER-MIB", "tIPvXFltrEntryActFwdVprnTgtRtrId"),
        ("TIMETRA-FILTER-MIB", "tIPvXFltrEntryActFwdVprnTgtAdPxT"),
        ("TIMETRA-FILTER-MIB", "tIPvXFltrEntryActFwdVprnTgtAdPx"),
        ("TIMETRA-FILTER-MIB", "tIPvXFltrEntryActFwdVprnTgtAdPxL"),
        ("TIMETRA-FILTER-MIB", "tIPvXFltrEntryActFwdVprnTgtLspId"))
)
if mibBuilder.loadTexts:
    tFilterForwardVprnTargetGroup.setStatus("current")

tFilterFwdBondingConnectionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 82)
)
tFilterFwdBondingConnectionGroup.setObjects(
    ("TIMETRA-FILTER-MIB", "tIPvXFltrEntryActFwdBondingConn")
)
if mibBuilder.loadTexts:
    tFilterFwdBondingConnectionGroup.setStatus("current")

tFilterSelectiveFlowspecGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 83)
)
tFilterSelectiveFlowspecGroup.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterEmbedFlowspecGroupId"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbedFlowspecInsEntryId"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbedFlowspecEntryOpState"))
)
if mibBuilder.loadTexts:
    tFilterSelectiveFlowspecGroup.setStatus("current")

tFilterMatchTcpFlagsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 84)
)
tFilterMatchTcpFlagsGroup.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPFilterParamsExtTcpFin"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtTcpRst"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtTcpPsh"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtTcpUrg"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtTcpEce"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtTcpCwr"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtTcpNs"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtTcpFin"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtTcpRst"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtTcpPsh"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtTcpUrg"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtTcpEce"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtTcpCwr"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtTcpNs"))
)
if mibBuilder.loadTexts:
    tFilterMatchTcpFlagsGroup.setStatus("current")

tFilterActionFc = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 86)
)
tFilterActionFc.setObjects(
    ("TIMETRA-FILTER-MIB", "tIPvXFltrEntryActFcName")
)
if mibBuilder.loadTexts:
    tFilterActionFc.setStatus("current")

tFilterRPPingSrcAddressGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 87)
)
tFilterRPPingSrcAddressGroup.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterRPPingSrcAddressAddrType"),
        ("TIMETRA-FILTER-MIB", "tFilterRPPingSrcAddressAddr"))
)
if mibBuilder.loadTexts:
    tFilterRPPingSrcAddressGroup.setStatus("current")

tFilterRPActiveDstChangeGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 89)
)
tFilterRPActiveDstChangeGrp.setObjects(
    ("TIMETRA-FILTER-MIB", "tFilterRPNotifyDestChange")
)
if mibBuilder.loadTexts:
    tFilterRPActiveDstChangeGrp.setStatus("current")

tFilterRPlcyBindingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 90)
)
tFilterRPlcyBindingGroup.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterRPlcyBindingTableLastChg"),
        ("TIMETRA-FILTER-MIB", "tFilterRPlcyBindingLastChange"),
        ("TIMETRA-FILTER-MIB", "tFilterRPlcyBindingRowStatus"),
        ("TIMETRA-FILTER-MIB", "tFilterRPlcyBindingOperator"),
        ("TIMETRA-FILTER-MIB", "tFilterRPlcyBindingOperState"),
        ("TIMETRA-FILTER-MIB", "tFilterRPlcyBindingDestTableLCh"),
        ("TIMETRA-FILTER-MIB", "tFilterRPlcyBindingDestRowStatus"),
        ("TIMETRA-FILTER-MIB", "tFilterRPlcyBindingDestOperState"))
)
if mibBuilder.loadTexts:
    tFilterRPlcyBindingGroup.setStatus("current")

tFltrGreTunTempGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 91)
)
tFltrGreTunTempGroup.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFltrGreTunTempTableLastChg"),
        ("TIMETRA-FILTER-MIB", "tFltrGreTunTempLastChanged"),
        ("TIMETRA-FILTER-MIB", "tFltrGreTunTempDescription"),
        ("TIMETRA-FILTER-MIB", "tFltrGreTunTempIpv4SrcAddr"),
        ("TIMETRA-FILTER-MIB", "tFltrGreTunTempIpv4GreKeyIfIndex"),
        ("TIMETRA-FILTER-MIB", "tFltrGreTunTempIpv4SkipTllDecr"),
        ("TIMETRA-FILTER-MIB", "tFltrGreTunTempRowStatus"),
        ("TIMETRA-FILTER-MIB", "tFltrGreTunTempIpv4DstTblLstChg"),
        ("TIMETRA-FILTER-MIB", "tFltrGreTunTempIpv4DstLstChg"),
        ("TIMETRA-FILTER-MIB", "tFltrGreTunTempIpv4DstRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPvXFltrEntryActFwdGreTun"))
)
if mibBuilder.loadTexts:
    tFltrGreTunTempGroup.setStatus("current")

tFltrPrefListPrefExcludeGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 92)
)
tFltrPrefListPrefExcludeGrp.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFltrPrefListPrefExclTblLstChg"),
        ("TIMETRA-FILTER-MIB", "tFltrPrefListPrefExclLastChg"),
        ("TIMETRA-FILTER-MIB", "tFltrPrefListPrefExclRowStatus"))
)
if mibBuilder.loadTexts:
    tFltrPrefListPrefExcludeGrp.setStatus("current")

fltrMdAutoIdV16v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 93)
)
fltrMdAutoIdV16v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "fltrMdAutoIdFilterRangeStart"),
        ("TIMETRA-FILTER-MIB", "fltrMdAutoIdFilterRangeEnd"),
        ("TIMETRA-FILTER-MIB", "fltrMdAutoIdIPv4FilterCount"),
        ("TIMETRA-FILTER-MIB", "fltrMdAutoIdIPv6FilterCount"),
        ("TIMETRA-FILTER-MIB", "fltrMdAutoIdMacFilterCount"))
)
if mibBuilder.loadTexts:
    fltrMdAutoIdV16v0Group.setStatus("current")

tFltrPatternMatchGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 94)
)
tFltrPatternMatchGroup.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPvXFltrEntryActCondExpression"),
        ("TIMETRA-FILTER-MIB", "tIPvXFltrEntryActCondExpMask"),
        ("TIMETRA-FILTER-MIB", "tIPvXFltrEntryActCondOffsetType"),
        ("TIMETRA-FILTER-MIB", "tIPvXFltrEntryActCondOffsetVal"))
)
if mibBuilder.loadTexts:
    tFltrPatternMatchGroup.setStatus("current")

tFilterRedirectPolicyV19v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 95)
)
tFilterRedirectPolicyV19v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterRPVrtrId"),
        ("TIMETRA-FILTER-MIB", "tFilterRPRowStatus"),
        ("TIMETRA-FILTER-MIB", "tFilterRPDescription"),
        ("TIMETRA-FILTER-MIB", "tFilterRPAdminState"),
        ("TIMETRA-FILTER-MIB", "tFilterRPActiveDestAddrType"),
        ("TIMETRA-FILTER-MIB", "tFilterRPActiveDestAddr"),
        ("TIMETRA-FILTER-MIB", "tFilterRPDstStickiness"),
        ("TIMETRA-FILTER-MIB", "tFilterRPBestDstAddrType"),
        ("TIMETRA-FILTER-MIB", "tFilterRPBestDstAddr"),
        ("TIMETRA-FILTER-MIB", "tFilterRPStickinessHoldRemain"),
        ("TIMETRA-FILTER-MIB", "tFilterRPlcyDstTableLastChg"),
        ("TIMETRA-FILTER-MIB", "tFltrRPDstLastChanged"),
        ("TIMETRA-FILTER-MIB", "tFltrRPDstRowStatus"),
        ("TIMETRA-FILTER-MIB", "tFltrRPDstDescription"),
        ("TIMETRA-FILTER-MIB", "tFltrRPDstAdminPriority"),
        ("TIMETRA-FILTER-MIB", "tFltrRPDstOperPriority"),
        ("TIMETRA-FILTER-MIB", "tFltrRPDstAdminState"),
        ("TIMETRA-FILTER-MIB", "tFltrRPDstOperState"),
        ("TIMETRA-FILTER-MIB", "tFilterRPlcyPingTestTableLastChg"),
        ("TIMETRA-FILTER-MIB", "tFltrRPPingTLastChanged"),
        ("TIMETRA-FILTER-MIB", "tFltrRPPingTRowStatus"),
        ("TIMETRA-FILTER-MIB", "tFltrRPPingTInterval"),
        ("TIMETRA-FILTER-MIB", "tFltrRPPingTTimeout"),
        ("TIMETRA-FILTER-MIB", "tFltrRPPingTDropCount"),
        ("TIMETRA-FILTER-MIB", "tFltrRPPingTHoldDown"),
        ("TIMETRA-FILTER-MIB", "tFltrRPPingTHoldDownRemain"),
        ("TIMETRA-FILTER-MIB", "tFltrRPPingTLastActionTime"),
        ("TIMETRA-FILTER-MIB", "tFltrRPPingTLastAction"),
        ("TIMETRA-FILTER-MIB", "tFilterRPlcyUcastRtTTableLastChg"),
        ("TIMETRA-FILTER-MIB", "tFltrRPUcastRtTLastChanged"),
        ("TIMETRA-FILTER-MIB", "tFltrRPUcastRtTRowStatus"),
        ("TIMETRA-FILTER-MIB", "tFltrRPUcastRtTLastActionTime"),
        ("TIMETRA-FILTER-MIB", "tFltrRPUcastRtTLastAction"))
)
if mibBuilder.loadTexts:
    tFilterRedirectPolicyV19v0Group.setStatus("current")

tFltrRPTestV19v0ObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 96)
)
tFltrRPTestV19v0ObsoleteGroup.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterRPlcySNMPRespTableLastChg"),
        ("TIMETRA-FILTER-MIB", "tFilterRPlcySNMPTestTableLastChg"),
        ("TIMETRA-FILTER-MIB", "tFilterRPlcyURLRespTableLastChg"),
        ("TIMETRA-FILTER-MIB", "tFilterRPlcyURLTestTableLastChg"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpRspAction"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpRspCounter32Val"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpRspCounter64Val"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpRspInt32Val"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpRspIpAddressVal"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpRspLastChanged"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpRspOID"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpRspOctetStringVal"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpRspOidVal"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpRspOpaqueVal"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpRspPrioChange"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpRspRowStatus"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpRspTimeTicksVal"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpRspType"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpRspUnsigned32Val"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpTCommunity"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpTDropCount"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpTHoldDown"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpTHoldDownRemain"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpTInterval"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpTLastAction"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpTLastActionTime"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpTLastChanged"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpTLastCounter32Val"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpTLastCounter64Val"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpTLastInt32Val"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpTLastIpAddressVal"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpTLastOID"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpTLastOctetStringVal"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpTLastOidVal"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpTLastOpaqueVal"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpTLastPrioChange"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpTLastTimeTicksVal"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpTLastType"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpTLastUnsigned32Val"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpTNextRespIndex"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpTOID"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpTRowStatus"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpTSnmpVersion"),
        ("TIMETRA-FILTER-MIB", "tFltrRPSnmpTTimeout"),
        ("TIMETRA-FILTER-MIB", "tFltrRPUrlTDropCount"),
        ("TIMETRA-FILTER-MIB", "tFltrRPUrlTHoldDown"),
        ("TIMETRA-FILTER-MIB", "tFltrRPUrlTHoldDownRemain"),
        ("TIMETRA-FILTER-MIB", "tFltrRPUrlTHttpVersion"),
        ("TIMETRA-FILTER-MIB", "tFltrRPUrlTInterval"),
        ("TIMETRA-FILTER-MIB", "tFltrRPUrlTLastAction"),
        ("TIMETRA-FILTER-MIB", "tFltrRPUrlTLastActionTime"),
        ("TIMETRA-FILTER-MIB", "tFltrRPUrlTLastChanged"),
        ("TIMETRA-FILTER-MIB", "tFltrRPUrlTLastPrioChange"),
        ("TIMETRA-FILTER-MIB", "tFltrRPUrlTLastRetCode"),
        ("TIMETRA-FILTER-MIB", "tFltrRPUrlTRowStatus"),
        ("TIMETRA-FILTER-MIB", "tFltrRPUrlTRspAction"),
        ("TIMETRA-FILTER-MIB", "tFltrRPUrlTRspLastChanged"),
        ("TIMETRA-FILTER-MIB", "tFltrRPUrlTRspPrioChange"),
        ("TIMETRA-FILTER-MIB", "tFltrRPUrlTRspRowStatus"),
        ("TIMETRA-FILTER-MIB", "tFltrRPUrlTTimeout"),
        ("TIMETRA-FILTER-MIB", "tFltrRPUrlTUrl"))
)
if mibBuilder.loadTexts:
    tFltrRPTestV19v0ObsoleteGroup.setStatus("current")

tFltrCAMTypeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 97)
)
tFltrCAMTypeGroup.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPFilterType"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterType"))
)
if mibBuilder.loadTexts:
    tFltrCAMTypeGroup.setStatus("current")

tFltrMatchMacForIPvXGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 98)
)
tFltrMatchMacForIPvXGroup.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPFilterParamsExtSrcMac"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtSrcMacMask"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtSrcMac"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtSrcMacMask"))
)
if mibBuilder.loadTexts:
    tFltrMatchMacForIPvXGroup.setStatus("current")

tFltrMatchPacketLengthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 99)
)
tFltrMatchPacketLengthGroup.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPFilterParamsExtMxPktLenVal1"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtMxPktLenVal2"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtMxPktLenOper"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtMxPktLenVal1"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtMxPktLenVal2"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtMxPktLenOper"))
)
if mibBuilder.loadTexts:
    tFltrMatchPacketLengthGroup.setStatus("current")

tFltrFilterNameInLIGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 100)
)
tFltrFilterNameInLIGroup.setObjects(
      *(("TIMETRA-FILTER-MIB", "tLiRsvdBlockFltrAssocTableLChg"),
        ("TIMETRA-FILTER-MIB", "tLiRsvdBlockFltrAssocRowStatus"),
        ("TIMETRA-FILTER-MIB", "tLiRsvdBlockFltrAssocLastChanged"))
)
if mibBuilder.loadTexts:
    tFltrFilterNameInLIGroup.setStatus("current")

tLiFltrAssocFltrNameGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 102)
)
tLiFltrAssocFltrNameGroup.setObjects(
      *(("TIMETRA-FILTER-MIB", "tLiFltrAssocFltrNameTableLastChg"),
        ("TIMETRA-FILTER-MIB", "tLiFltrAssocFltrNameRowStatus"),
        ("TIMETRA-FILTER-MIB", "tLiFltrAssocFltrNameLastChg"))
)
if mibBuilder.loadTexts:
    tLiFltrAssocFltrNameGroup.setStatus("current")

tFltrIPv6ExceptionV19v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 103)
)
tFltrIPv6ExceptionV19v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPv6ExceptionRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPv6ExceptionDescription"),
        ("TIMETRA-FILTER-MIB", "tIPv6ExceptionName"),
        ("TIMETRA-FILTER-MIB", "tIPv6ExceptionNameId"),
        ("TIMETRA-FILTER-MIB", "tIPv6ExcParamsRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPv6ExcParamsDescription"),
        ("TIMETRA-FILTER-MIB", "tIPv6ExcParamsNextHeader"),
        ("TIMETRA-FILTER-MIB", "tIPv6ExcParamsSrcIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPv6ExcParamsSrcIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPv6ExcParamsSrcIpFullMask"),
        ("TIMETRA-FILTER-MIB", "tIPv6ExcParamsSrcIpPrefixList"),
        ("TIMETRA-FILTER-MIB", "tIPv6ExcParamsDstIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPv6ExcParamsDstIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPv6ExcParamsDstIpFullMask"),
        ("TIMETRA-FILTER-MIB", "tIPv6ExcParamsDstIpPrefixList"),
        ("TIMETRA-FILTER-MIB", "tIPv6ExcParamsSourcePortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPv6ExcParamsSourcePortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPv6ExcParamsSourcePortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPv6ExcParamsSourcePortList"),
        ("TIMETRA-FILTER-MIB", "tIPv6ExcParamsDestPortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPv6ExcParamsDestPortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPv6ExcParamsDestPortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPv6ExcParamsDestPortList"),
        ("TIMETRA-FILTER-MIB", "tIPv6ExcParamsPortSelector"),
        ("TIMETRA-FILTER-MIB", "tIPv6ExcParamsIcmpCode"),
        ("TIMETRA-FILTER-MIB", "tIPv6ExcParamsIcmpType"),
        ("TIMETRA-FILTER-MIB", "tIPv6ExcParamsIngressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPv6ExcParamsEgressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPv6ExcParamsIngrHitByteCount"),
        ("TIMETRA-FILTER-MIB", "tIPv6ExcParamsEgrHitByteCount"))
)
if mibBuilder.loadTexts:
    tFltrIPv6ExceptionV19v0Group.setStatus("current")

tFltrFwdMplsPlcyEndptGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 104)
)
tFltrFwdMplsPlcyEndptGrp.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPvXFltrFwdMplsPlcyEndptAddrTp"),
        ("TIMETRA-FILTER-MIB", "tIPvXFltrFwdMplsPlcyEndptAddr"))
)
if mibBuilder.loadTexts:
    tFltrFwdMplsPlcyEndptGrp.setStatus("current")

tFltrFwdSrtePlcyEndptColorGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 105)
)
tFltrFwdSrtePlcyEndptColorGrp.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPvXFltrFwdSrtePlcyEndptAddrTp"),
        ("TIMETRA-FILTER-MIB", "tIPvXFltrFwdSrtePlcyEndptAddr"),
        ("TIMETRA-FILTER-MIB", "tIPvXFltrFwdSrtePlcyColor"))
)
if mibBuilder.loadTexts:
    tFltrFwdSrtePlcyEndptColorGrp.setStatus("current")

tLiFltrMatchFragmentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 106)
)
tLiFltrMatchFragmentGroup.setObjects(
    ("TIMETRA-FILTER-MIB", "tLiIpFilterParamsFragment")
)
if mibBuilder.loadTexts:
    tLiFltrMatchFragmentGroup.setStatus("current")

fltrMdAutoIdV20v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 107)
)
fltrMdAutoIdV20v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "fltrMdAutoIdIPv4ExceptionCount"),
        ("TIMETRA-FILTER-MIB", "fltrMdAutoIdIPv6ExceptionCount"))
)
if mibBuilder.loadTexts:
    fltrMdAutoIdV20v0Group.setStatus("current")

tFilterMatchProtocolListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 108)
)
tFilterMatchProtocolListGroup.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFltrProtocolListTableLstChng"),
        ("TIMETRA-FILTER-MIB", "tFltrProtocolListRowStatus"),
        ("TIMETRA-FILTER-MIB", "tFltrProtocolListLastChanged"),
        ("TIMETRA-FILTER-MIB", "tFltrProtocolListDescription"),
        ("TIMETRA-FILTER-MIB", "tFltrProtocolListItemTblLstChg"),
        ("TIMETRA-FILTER-MIB", "tFltrProtocolListItemRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtProtocolList"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtProtocolList"))
)
if mibBuilder.loadTexts:
    tFilterMatchProtocolListGroup.setStatus("current")

tFilterMatchDestClassGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 109)
)
tFilterMatchDestClassGroup.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPFilterParamsExtDestClass"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtDestClass"))
)
if mibBuilder.loadTexts:
    tFilterMatchDestClassGroup.setStatus("current")

tFilterL2AwareNatBypassGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 110)
)
tFilterL2AwareNatBypassGroup.setObjects(
    ("TIMETRA-FILTER-MIB", "tIPvXFltrActL2AwareNatBypass")
)
if mibBuilder.loadTexts:
    tFilterL2AwareNatBypassGroup.setStatus("current")

tFltrCflowdSampleProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 112)
)
tFltrCflowdSampleProfileGroup.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPFilterParamsExtSampleProf"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtSampleProf"))
)
if mibBuilder.loadTexts:
    tFltrCflowdSampleProfileGroup.setStatus("current")

tFltrEntryCollectStatsIPvXGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 113)
)
tFltrEntryCollectStatsIPvXGroup.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPFilterParamsExtCollectStats"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtCollectStats"))
)
if mibBuilder.loadTexts:
    tFltrEntryCollectStatsIPvXGroup.setStatus("current")

tFltrEntryCollectStatsMacGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 114)
)
tFltrEntryCollectStatsMacGroup.setObjects(
    ("TIMETRA-FILTER-MIB", "tMacFilterParamsCollectStats")
)
if mibBuilder.loadTexts:
    tFltrEntryCollectStatsMacGroup.setStatus("current")

tFilterMacFltrActionGroupV21 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 115)
)
tFilterMacFltrActionGroupV21.setObjects(
    ("TIMETRA-FILTER-MIB", "tMacFltrEntryActFcName")
)
if mibBuilder.loadTexts:
    tFilterMacFltrActionGroupV21.setStatus("current")

tFltrParamsActionObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 116)
)
tFltrParamsActionObsoleteGroup.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPFilterParamsAction"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardNH"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardNHIndirect"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardNHInterface"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardRedPlcy"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSapPortId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSapEncapVal"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSdpBind"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRedirectURL"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdRtrId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRdirAllwRadOvrd"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsNatPolicyName"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdLsp"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdLspRtrId"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsAction"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsFwdSapPortId"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsFwdSapEncapVal"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsFwdSdpBind"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsRedirectURL"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsEsi"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsFwdEsiSvcId"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsAction"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsForwardNH"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsForwardNHIndirect"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsForwardNHInterface"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsForwardRedPlcy"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFwdSapPortId"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFwdSapEncapVal"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFwdSdpBind"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRedirectURL"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRdirAllwRadOvrd"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFwdRtrId"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsNatPolicyName"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFwdLsp"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFwdLspRtrId"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtNatType"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtPktLenVal1"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtPktLenVal2"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtPktLenOper"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtHopLimitVal1"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtHopLimitVal2"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtHopLimitOper"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtEsi"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtFwdEsiSvcId"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtFwdEsiVRtrId"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtFwdEsiSFIp"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtFwdEsiVasIf"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtPktLenVal1"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtPktLenVal2"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtPktLenOper"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtTTLVal1"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtTTLVal2"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtTTLOper"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtEsi"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtFwdEsiSvcId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtFwdEsiVRtrId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtFwdEsiSFIp"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtFwdEsiVasIf"))
)
if mibBuilder.loadTexts:
    tFltrParamsActionObsoleteGroup.setStatus("current")

tIPFilterV21v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 117)
)
tIPFilterV21v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPFilterParamsExtTbleLstChgd"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtLastChanged"),
        ("TIMETRA-FILTER-MIB", "tIPFilterSharedPccRuleInsrtPt"),
        ("TIMETRA-FILTER-MIB", "tIPFilterSharedPccRuleInsrtSize"),
        ("TIMETRA-FILTER-MIB", "tIPFilterSharedPccRuleNbrInsrtd"),
        ("TIMETRA-FILTER-MIB", "tIPFilterChainToSystemFilter"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtEgressPBR"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtPbrDwnActOvr"),
        ("TIMETRA-FILTER-MIB", "tIPFilterRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPFilterScope"),
        ("TIMETRA-FILTER-MIB", "tIPFilterDescription"),
        ("TIMETRA-FILTER-MIB", "tIPFilterDefaultAction"),
        ("TIMETRA-FILTER-MIB", "tIPFilterRadiusInsertPt"),
        ("TIMETRA-FILTER-MIB", "tIPFilterRadiusInsertSize"),
        ("TIMETRA-FILTER-MIB", "tIPFilterCreditCntrlInsertPt"),
        ("TIMETRA-FILTER-MIB", "tIPFilterCreditCntrlInsertSize"),
        ("TIMETRA-FILTER-MIB", "tIPFilterSubInsertHighWmark"),
        ("TIMETRA-FILTER-MIB", "tIPFilterSubInsertLowWmark"),
        ("TIMETRA-FILTER-MIB", "tIpFilterCreditCntrlNbrInsertd"),
        ("TIMETRA-FILTER-MIB", "tIpFilterRadiusNbrInsertd"),
        ("TIMETRA-FILTER-MIB", "tIPFilterHostSharedInsertPt"),
        ("TIMETRA-FILTER-MIB", "tIPFilterHostSharedInsertSize"),
        ("TIMETRA-FILTER-MIB", "tIpFilterHostSharedNbrInsertd"),
        ("TIMETRA-FILTER-MIB", "tIPFilterHostSharedHighWmark"),
        ("TIMETRA-FILTER-MIB", "tIPFilterHostSharedLowWmark"),
        ("TIMETRA-FILTER-MIB", "tIPFilterNbrHostSharedFltrs"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsLogId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDescription"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourceIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourceIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestinationIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestinationIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsProtocol"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourcePortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourcePortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSourcePortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestPortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestPortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestPortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDSCP"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFragment"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsOptionPresent"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIpOptionValue"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIpOptionMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsMultipleOption"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsTcpSyn"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsTcpAck"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIcmpCode"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIcmpType"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsCflowdSample"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsCflowdIfSample"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsFwdSvcId"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIngressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsEgressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsLogInstantiated"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsActiveDest"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSrcIpFullMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDestIpFullMask"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIngrHitByteCount"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsEgrHitByteCount"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesFilterType"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesFilterId"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesApplication"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesLocation"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesResult"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesFeedback"),
        ("TIMETRA-FILTER-MIB", "tFltrGrpInsrtdEntriesExecute"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSrcRouteOption"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsPortSelector"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsSrcPortList"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsDstPortList"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtTbleLstChgd"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtLastChanged"))
)
if mibBuilder.loadTexts:
    tIPFilterV21v0Group.setStatus("current")

tIPv6FilterV21v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 118)
)
tIPv6FilterV21v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPv6FilterSharedPccRuleInsrtPt"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterSharedPccRuleInsrtSiz"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterSharedPccRuleNbrInsrt"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterChainToSystemFilter"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtEgressPBR"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtPbrDwnActOvr"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterScope"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterDescription"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterDefaultAction"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterRadiusInsertPt"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterRadiusInsertSize"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterCreditCntrlInsertPt"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterCreditCntrlInsertSize"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterSubInsertHighWmark"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterSubInsertLowWmark"),
        ("TIMETRA-FILTER-MIB", "tIpv6FilterCreditCntrlNbrInsertd"),
        ("TIMETRA-FILTER-MIB", "tIpv6FilterRadiusNbrInsertd"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterHostSharedInsertPt"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterHostSharedInsertSize"),
        ("TIMETRA-FILTER-MIB", "tIpv6FilterHostSharedNbrInsertd"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterHostSharedHighWmark"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterHostSharedLowWmark"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterNbrHostSharedFltrs"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRowStatus"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsLogId"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDescription"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourceIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourceIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestinationIpAddr"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestinationIpMask"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsNextHeader"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourcePortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourcePortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSourcePortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestPortValue1"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestPortValue2"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDestPortOperator"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDSCP"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsTcpSyn"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsTcpAck"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsIcmpCode"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsIcmpType"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsCflowdSample"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsCflowdIfSample"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFwdSvcId"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsIngressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsEgressHitCount"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsLogInstantiated"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsActiveDest"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsIngrHitByteCount"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsEgrHitByteCount"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSrcIpPrefixList"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDstIpPrefixList"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFragment"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsHopByHopOpt"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsRoutingType0"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsPortSelector"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSrcPortList"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDstPortList"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsSrcIpFullMask"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsDstIpFullMask"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFlowLabel"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsFlowLabelMask"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtTbleLstChgd"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtLastChanged"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtAhExtHdr"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtEspExtHdr"))
)
if mibBuilder.loadTexts:
    tIPv6FilterV21v0Group.setStatus("current")

tMacFilterV21v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 119)
)
tMacFilterV21v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tMacFilterParamsPbrDwnActOvr"),
        ("TIMETRA-FILTER-MIB", "tMacFilterRowStatus"),
        ("TIMETRA-FILTER-MIB", "tMacFilterScope"),
        ("TIMETRA-FILTER-MIB", "tMacFilterDescription"),
        ("TIMETRA-FILTER-MIB", "tMacFilterDefaultAction"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsRowStatus"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsLogId"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsDescription"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsFrameType"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsSrcMAC"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsSrcMACMask"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsDstMAC"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsDstMACMask"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsDot1pValue"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsDot1pMask"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsEtherType"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsDsap"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsDsapMask"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsSsap"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsSsapMask"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsSnapPid"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsSnapOui"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsIngressHitCount"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsEgressHitCount"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsLogInstantiated"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsFwdSvcId"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsRedirectURL"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsIngrHitByteCount"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsEgrHitByteCount"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsLowISID"),
        ("TIMETRA-FILTER-MIB", "tMacFilterParamsHighISID"),
        ("TIMETRA-FILTER-MIB", "tMacFilterType"))
)
if mibBuilder.loadTexts:
    tMacFilterV21v0Group.setStatus("current")

tFilterMatchTTLGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 120)
)
tFilterMatchTTLGroup.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPFilterParamsExtMxTTLVal1"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtMxTTLVal2"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsExtMxTTLOper"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtMxHopLmtVal1"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtMxHopLmtVal2"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterParamsExtMxHopLmtOper"))
)
if mibBuilder.loadTexts:
    tFilterMatchTTLGroup.setStatus("current")

tFltrMatchSrcOrDstIpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 121)
)
tFltrMatchSrcOrDstIpGroup.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPv6FilterParamsIpSelector"),
        ("TIMETRA-FILTER-MIB", "tIPFilterParamsIpSelector"))
)
if mibBuilder.loadTexts:
    tFltrMatchSrcOrDstIpGroup.setStatus("current")


# Notification objects

tIPFilterPBRPacketsDrop = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 21, 0, 1)
)
tIPFilterPBRPacketsDrop.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPFilterParamsForwardNHInterface"),
        ("TIMETRA-FILTER-MIB", "tFilterPBRDropReason"))
)
if mibBuilder.loadTexts:
    tIPFilterPBRPacketsDrop.setStatus(
        "current"
    )

tFilterEntryActivationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 21, 0, 2)
)
tFilterEntryActivationFailed.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterParmRow"),
        ("TIMETRA-FILTER-MIB", "tFilterAlarmDescription"))
)
if mibBuilder.loadTexts:
    tFilterEntryActivationFailed.setStatus(
        "obsolete"
    )

tFilterEntryActivationRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 21, 0, 3)
)
tFilterEntryActivationRestored.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterParmRow"),
        ("TIMETRA-FILTER-MIB", "tFilterAlarmDescription"))
)
if mibBuilder.loadTexts:
    tFilterEntryActivationRestored.setStatus(
        "obsolete"
    )

tFilterSubInsSpaceAlarmRaised = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 21, 0, 4)
)
tFilterSubInsSpaceAlarmRaised.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterType"),
        ("TIMETRA-FILTER-MIB", "tFilterId"),
        ("TIMETRA-FILTER-MIB", "tFilterSubInsSpaceOwner"),
        ("TIMETRA-FILTER-MIB", "tFilterThresholdReached"))
)
if mibBuilder.loadTexts:
    tFilterSubInsSpaceAlarmRaised.setStatus(
        "current"
    )

tFilterSubInsSpaceAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 21, 0, 5)
)
tFilterSubInsSpaceAlarmCleared.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterType"),
        ("TIMETRA-FILTER-MIB", "tFilterId"),
        ("TIMETRA-FILTER-MIB", "tFilterSubInsSpaceOwner"),
        ("TIMETRA-FILTER-MIB", "tFilterThresholdReached"))
)
if mibBuilder.loadTexts:
    tFilterSubInsSpaceAlarmCleared.setStatus(
        "current"
    )

tFilterSubInsFltrEntryDropped = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 21, 0, 6)
)
tFilterSubInsFltrEntryDropped.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterType"),
        ("TIMETRA-FILTER-MIB", "tFilterId"),
        ("TIMETRA-FILTER-MIB", "tFilterSubInsSpaceOwner"),
        ("TIMETRA-FILTER-MIB", "tFilterAlarmDescription"))
)
if mibBuilder.loadTexts:
    tFilterSubInsFltrEntryDropped.setStatus(
        "current"
    )

tFilterBgpFlowSpecProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 21, 0, 7)
)
tFilterBgpFlowSpecProblem.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterType"),
        ("TIMETRA-FILTER-MIB", "tFltrFlowSpecVrtrId"),
        ("TIMETRA-FILTER-MIB", "tFltrFlowSpecProblem"),
        ("TIMETRA-FILTER-MIB", "tFltrFlowSpecProblemDescription"),
        ("TIMETRA-FILTER-MIB", "tFltrFLowSpecNLRI"))
)
if mibBuilder.loadTexts:
    tFilterBgpFlowSpecProblem.setStatus(
        "current"
    )

tFilterApplyPathProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 21, 0, 8)
)
tFilterApplyPathProblem.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFltrPrefixListType"),
        ("TIMETRA-FILTER-MIB", "tFltrPrefixListName"),
        ("TIMETRA-FILTER-MIB", "tFltrApplyPathSource"),
        ("TIMETRA-FILTER-MIB", "tFltrApplyPathIndex"),
        ("TIMETRA-FILTER-MIB", "tFilterAlarmDescription"))
)
if mibBuilder.loadTexts:
    tFilterApplyPathProblem.setStatus(
        "current"
    )

tFilterRadSharedFltrAlarmRaised = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 21, 0, 9)
)
tFilterRadSharedFltrAlarmRaised.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterType"),
        ("TIMETRA-FILTER-MIB", "tFilterId"),
        ("TIMETRA-FILTER-MIB", "tFilterThresholdReached"))
)
if mibBuilder.loadTexts:
    tFilterRadSharedFltrAlarmRaised.setStatus(
        "current"
    )

tFilterRadSharedFltrAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 21, 0, 10)
)
tFilterRadSharedFltrAlarmClear.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterType"),
        ("TIMETRA-FILTER-MIB", "tFilterId"),
        ("TIMETRA-FILTER-MIB", "tFilterThresholdReached"))
)
if mibBuilder.loadTexts:
    tFilterRadSharedFltrAlarmClear.setStatus(
        "current"
    )

tFilterEmbeddingOperStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 21, 0, 11)
)
tFilterEmbeddingOperStateChange.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterEmbeddedRefOperState"),
        ("TIMETRA-FILTER-MIB", "tFltrNotifDescription"))
)
if mibBuilder.loadTexts:
    tFilterEmbeddingOperStateChange.setStatus(
        "current"
    )

tFilterEmbedOpenflowOperStateChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 21, 0, 12)
)
tFilterEmbedOpenflowOperStateChg.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterEmbedOpenflowOperState"),
        ("TIMETRA-FILTER-MIB", "tFltrNotifDescription"))
)
if mibBuilder.loadTexts:
    tFilterEmbedOpenflowOperStateChg.setStatus(
        "current"
    )

tFilterTmsEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 21, 0, 13)
)
tFilterTmsEvent.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFltrMdaId"),
        ("TIMETRA-FILTER-MIB", "tFltrNotifDescription"))
)
if mibBuilder.loadTexts:
    tFilterTmsEvent.setStatus(
        "obsolete"
    )

tFilterEmbedFlowspecOperStateChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 21, 0, 14)
)
tFilterEmbedFlowspecOperStateChg.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterEmbedFlowspecRtrId"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbedFlowspecOperState"),
        ("TIMETRA-FILTER-MIB", "tFltrNotifDescription"))
)
if mibBuilder.loadTexts:
    tFilterEmbedFlowspecOperStateChg.setStatus(
        "current"
    )

tFilterEmbedVsdOperStateChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 21, 0, 15)
)
tFilterEmbedVsdOperStateChg.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterEmbedVsdOperState"),
        ("TIMETRA-FILTER-MIB", "tFltrNotifDescription"))
)
if mibBuilder.loadTexts:
    tFilterEmbedVsdOperStateChg.setStatus(
        "current"
    )

tFilterRPActiveDestChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 21, 0, 16)
)
tFilterRPActiveDestChangeEvent.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterRPActiveDestAddrType"),
        ("TIMETRA-FILTER-MIB", "tFilterRPActiveDestAddr"),
        ("TIMETRA-FILTER-MIB", "tFltrNotifDescription"))
)
if mibBuilder.loadTexts:
    tFilterRPActiveDestChangeEvent.setStatus(
        "current"
    )

tFltrLiRsvdBlockRangeChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 21, 0, 17)
)
tFltrLiRsvdBlockRangeChangeEvent.setObjects(
      *(("TIMETRA-FILTER-MIB", "tLiReservedBlockStart"),
        ("TIMETRA-FILTER-MIB", "tLiReservedBlockSize"))
)
if mibBuilder.loadTexts:
    tFltrLiRsvdBlockRangeChangeEvent.setStatus(
        "current"
    )


# Notifications groups

tFilterNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 9)
)
tFilterNotificationsGroup.setObjects(
    ("TIMETRA-FILTER-MIB", "tIPFilterPBRPacketsDrop")
)
if mibBuilder.loadTexts:
    tFilterNotificationsGroup.setStatus(
        "obsolete"
    )

tToDPoliciesV5v0NotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 16)
)
tToDPoliciesV5v0NotifyGroup.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterEntryActivationFailed"),
        ("TIMETRA-FILTER-MIB", "tFilterEntryActivationRestored"))
)
if mibBuilder.loadTexts:
    tToDPoliciesV5v0NotifyGroup.setStatus(
        "obsolete"
    )

tFilterNotificationsV8v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 28)
)
tFilterNotificationsV8v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPFilterPBRPacketsDrop"),
        ("TIMETRA-FILTER-MIB", "tFilterSubInsSpaceAlarmRaised"),
        ("TIMETRA-FILTER-MIB", "tFilterSubInsSpaceAlarmCleared"),
        ("TIMETRA-FILTER-MIB", "tFilterSubInsFltrEntryDropped"))
)
if mibBuilder.loadTexts:
    tFilterNotificationsV8v0Group.setStatus(
        "obsolete"
    )

tFilterNotificationsV9v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 32)
)
tFilterNotificationsV9v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPFilterPBRPacketsDrop"),
        ("TIMETRA-FILTER-MIB", "tFilterSubInsSpaceAlarmRaised"),
        ("TIMETRA-FILTER-MIB", "tFilterSubInsSpaceAlarmCleared"),
        ("TIMETRA-FILTER-MIB", "tFilterSubInsFltrEntryDropped"),
        ("TIMETRA-FILTER-MIB", "tFilterBgpFlowSpecProblem"))
)
if mibBuilder.loadTexts:
    tFilterNotificationsV9v0Group.setStatus(
        "obsolete"
    )

tFilterNotificationsV11v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 45)
)
tFilterNotificationsV11v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tIPFilterPBRPacketsDrop"),
        ("TIMETRA-FILTER-MIB", "tFilterSubInsSpaceAlarmRaised"),
        ("TIMETRA-FILTER-MIB", "tFilterSubInsSpaceAlarmCleared"),
        ("TIMETRA-FILTER-MIB", "tFilterSubInsFltrEntryDropped"),
        ("TIMETRA-FILTER-MIB", "tFilterBgpFlowSpecProblem"),
        ("TIMETRA-FILTER-MIB", "tFilterApplyPathProblem"),
        ("TIMETRA-FILTER-MIB", "tFilterRadSharedFltrAlarmRaised"),
        ("TIMETRA-FILTER-MIB", "tFilterRadSharedFltrAlarmClear"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbeddingOperStateChange"))
)
if mibBuilder.loadTexts:
    tFilterNotificationsV11v0Group.setStatus(
        "current"
    )

tFilterNotificationsV12v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 51)
)
tFilterNotificationsV12v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterEmbedOpenflowOperStateChg"),
        ("TIMETRA-FILTER-MIB", "tFilterTmsEvent"))
)
if mibBuilder.loadTexts:
    tFilterNotificationsV12v0Group.setStatus(
        "obsolete"
    )

tFilterNotificationsV14v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 61)
)
tFilterNotificationsV14v0Group.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterEmbedFlowspecOperStateChg"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbedVsdOperStateChg"))
)
if mibBuilder.loadTexts:
    tFilterNotificationsV14v0Group.setStatus(
        "current"
    )

tFilterObsoletedNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 68)
)
tFilterObsoletedNotifsGroup.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterEntryActivationFailed"),
        ("TIMETRA-FILTER-MIB", "tFilterEntryActivationRestored"))
)
if mibBuilder.loadTexts:
    tFilterObsoletedNotifsGroup.setStatus(
        "current"
    )

tFilterNotificationsV15v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 80)
)
tFilterNotificationsV15v0Group.setObjects(
    ("TIMETRA-FILTER-MIB", "tFilterEmbedOpenflowOperStateChg")
)
if mibBuilder.loadTexts:
    tFilterNotificationsV15v0Group.setStatus(
        "current"
    )

tFilterObsoleteNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 81)
)
tFilterObsoleteNotifsGroup.setObjects(
    ("TIMETRA-FILTER-MIB", "tFilterTmsEvent")
)
if mibBuilder.loadTexts:
    tFilterObsoleteNotifsGroup.setStatus(
        "current"
    )

tFilterRPActiveDstChangeNotifGrp = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 88)
)
tFilterRPActiveDstChangeNotifGrp.setObjects(
    ("TIMETRA-FILTER-MIB", "tFilterRPActiveDestChangeEvent")
)
if mibBuilder.loadTexts:
    tFilterRPActiveDstChangeNotifGrp.setStatus(
        "current"
    )

tFltrLiRsvdBlockRangeChgNotifGrp = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 2, 111)
)
tFltrLiRsvdBlockRangeChgNotifGrp.setObjects(
    ("TIMETRA-FILTER-MIB", "tFltrLiRsvdBlockRangeChangeEvent")
)
if mibBuilder.loadTexts:
    tFltrLiRsvdBlockRangeChgNotifGrp.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tFilter7450V4v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 1, 4)
)
tFilter7450V4v0Compliance.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterScalarGroup"),
        ("TIMETRA-FILTER-MIB", "tIPFilterV4v0Group"),
        ("TIMETRA-FILTER-MIB", "tMacFilterV4v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterLogGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterRedirectPolicyGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationsGroup"))
)
if mibBuilder.loadTexts:
    tFilter7450V4v0Compliance.setStatus(
        "obsolete"
    )

tFilter7750V4v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 1, 5)
)
tFilter7750V4v0Compliance.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterScalarGroup"),
        ("TIMETRA-FILTER-MIB", "tIPFilterV4v0Group"),
        ("TIMETRA-FILTER-MIB", "tMacFilterV4v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterLogGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterRedirectPolicyGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationsGroup"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterV4v0Group"))
)
if mibBuilder.loadTexts:
    tFilter7750V4v0Compliance.setStatus(
        "obsolete"
    )

tFilter7450V5v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 1, 6)
)
tFilter7450V5v0Compliance.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterScalarGroup"),
        ("TIMETRA-FILTER-MIB", "tIPFilterV5v0Group"),
        ("TIMETRA-FILTER-MIB", "tMacFilterV4v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterLogGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterRedirectPolicyGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationsGroup"),
        ("TIMETRA-FILTER-MIB", "tTodPolicies77450V5v0Group"),
        ("TIMETRA-FILTER-MIB", "tToDPoliciesV5v0NotifyGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterLogV5v0Group"))
)
if mibBuilder.loadTexts:
    tFilter7450V5v0Compliance.setStatus(
        "obsolete"
    )

tFilter77x0V5v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 1, 7)
)
tFilter77x0V5v0Compliance.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterScalarGroup"),
        ("TIMETRA-FILTER-MIB", "tIPFilterV5v0Group"),
        ("TIMETRA-FILTER-MIB", "tMacFilterV4v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterLogGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterRedirectPolicyGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationsGroup"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterV4v0Group"),
        ("TIMETRA-FILTER-MIB", "tTodPolicies77x0V5v0Group"),
        ("TIMETRA-FILTER-MIB", "tToDPoliciesV5v0NotifyGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterLogV5v0Group"))
)
if mibBuilder.loadTexts:
    tFilter77x0V5v0Compliance.setStatus(
        "obsolete"
    )

tFilter7450V6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 1, 8)
)
tFilter7450V6v0Compliance.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterScalarGroup"),
        ("TIMETRA-FILTER-MIB", "tIPFilterV6v0Group"),
        ("TIMETRA-FILTER-MIB", "tMacFilterV6v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterLogGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterRedirectPolicyGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationsGroup"),
        ("TIMETRA-FILTER-MIB", "tTodPolicies77450V5v0Group"),
        ("TIMETRA-FILTER-MIB", "tToDPoliciesV5v0NotifyGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterLogV5v0Group"))
)
if mibBuilder.loadTexts:
    tFilter7450V6v0Compliance.setStatus(
        "obsolete"
    )

tFilter77x0V6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 1, 9)
)
tFilter77x0V6v0Compliance.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterScalarGroup"),
        ("TIMETRA-FILTER-MIB", "tIPFilterV6v0Group"),
        ("TIMETRA-FILTER-MIB", "tMacFilterV6v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterLogGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterRedirectPolicyGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationsGroup"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterV6v0Group"),
        ("TIMETRA-FILTER-MIB", "tTodPolicies77x0V5v0Group"),
        ("TIMETRA-FILTER-MIB", "tToDPoliciesV5v0NotifyGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterLogV5v0Group"))
)
if mibBuilder.loadTexts:
    tFilter77x0V6v0Compliance.setStatus(
        "obsolete"
    )

tFilter7450V8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 1, 10)
)
tFilter7450V8v0Compliance.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterScalarGroup"),
        ("TIMETRA-FILTER-MIB", "tIPFilterV8v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterLogGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterLogV5v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterRedirectPolicyGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationsV8v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationObjV8v0Group"),
        ("TIMETRA-FILTER-MIB", "tTodPolicies77450V5v0Group"),
        ("TIMETRA-FILTER-MIB", "tToDPoliciesV5v0NotifyGroup"))
)
if mibBuilder.loadTexts:
    tFilter7450V8v0Compliance.setStatus(
        "obsolete"
    )

tFilter77x0V8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 1, 11)
)
tFilter77x0V8v0Compliance.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterScalarGroup"),
        ("TIMETRA-FILTER-MIB", "tIPFilterV8v0Group"),
        ("TIMETRA-FILTER-MIB", "tMacFilterV8v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterLogGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterLogV5v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterRedirectPolicyGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationsV8v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationObjV8v0Group"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterV8v0Group"),
        ("TIMETRA-FILTER-MIB", "tTodPolicies77x0V5v0Group"),
        ("TIMETRA-FILTER-MIB", "tToDPoliciesV5v0NotifyGroup"))
)
if mibBuilder.loadTexts:
    tFilter77x0V8v0Compliance.setStatus(
        "obsolete"
    )

tFilter7xxxV9v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 1, 12)
)
tFilter7xxxV9v0Compliance.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterScalarGroup"),
        ("TIMETRA-FILTER-MIB", "tIPFilterV9v0Group"),
        ("TIMETRA-FILTER-MIB", "tMacFilterV8v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterLogGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterLogV5v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterRedirectPolicyGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationsV9v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationObjV9v0Group"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterV8v0Group"),
        ("TIMETRA-FILTER-MIB", "tTodPolicies77x0V5v0Group"),
        ("TIMETRA-FILTER-MIB", "tToDPoliciesV5v0NotifyGroup"),
        ("TIMETRA-FILTER-MIB", "tMacFilterVidFilteringV9v0Group"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterV9v0Group"))
)
if mibBuilder.loadTexts:
    tFilter7xxxV9v0Compliance.setStatus(
        "obsolete"
    )

tFilter7xxxV10v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 1, 13)
)
tFilter7xxxV10v0Compliance.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterScalarGroup"),
        ("TIMETRA-FILTER-MIB", "tIPFilterV9v0Group"),
        ("TIMETRA-FILTER-MIB", "tMacFilterV8v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterLogGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterLogV5v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterRedirectPolicyGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationsV9v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationObjV9v0Group"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterV10v0Group"),
        ("TIMETRA-FILTER-MIB", "tTodPolicies77x0V5v0Group"),
        ("TIMETRA-FILTER-MIB", "tToDPoliciesV5v0NotifyGroup"),
        ("TIMETRA-FILTER-MIB", "tMacFilterVidFilteringV9v0Group"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterV10v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterNameV10v0Group"),
        ("TIMETRA-FILTER-MIB", "tLiFilterV10v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterPrefixListV10v0Group"))
)
if mibBuilder.loadTexts:
    tFilter7xxxV10v0Compliance.setStatus(
        "obsolete"
    )

tFilter7xxxV11v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 1, 14)
)
tFilter7xxxV11v0Compliance.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterScalarGroup"),
        ("TIMETRA-FILTER-MIB", "tIPFilterV11v0Group"),
        ("TIMETRA-FILTER-MIB", "tMacFilterV8v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterLogGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterLogV5v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterRedirectPolicyGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationsV11v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationObjV11v0Group"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterV11v0Group"),
        ("TIMETRA-FILTER-MIB", "tTodPolicies77x0V5v0Group"),
        ("TIMETRA-FILTER-MIB", "tToDPoliciesV5v0NotifyGroup"),
        ("TIMETRA-FILTER-MIB", "tMacFilterVidFilteringV9v0Group"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterV10v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterNameV10v0Group"),
        ("TIMETRA-FILTER-MIB", "tLiFilterV10v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterPrefixListV11v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbeddedInsertV11v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterPortListV11v0Group"))
)
if mibBuilder.loadTexts:
    tFilter7xxxV11v0Compliance.setStatus(
        "obsolete"
    )

tFilter7xxxV12v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 1, 15)
)
tFilter7xxxV12v0Compliance.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterScalarGroup"),
        ("TIMETRA-FILTER-MIB", "tIPFilterV12v0Group"),
        ("TIMETRA-FILTER-MIB", "tMacFilterV8v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterLogGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterLogV5v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterRedirectPolicyGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationsV11v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationsV12v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationObjV12v0Group"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterV12v0Group"),
        ("TIMETRA-FILTER-MIB", "tTodPolicies77x0V5v0Group"),
        ("TIMETRA-FILTER-MIB", "tToDPoliciesV5v0NotifyGroup"),
        ("TIMETRA-FILTER-MIB", "tMacFilterVidFilteringV9v0Group"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterV10v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterNameV10v0Group"),
        ("TIMETRA-FILTER-MIB", "tLiFilterV12v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterPrefixListV11v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbeddedInsertV11v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbeddedInsertV12v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterPortListV11v0Group"))
)
if mibBuilder.loadTexts:
    tFilter7xxxV12v0Compliance.setStatus(
        "obsolete"
    )

tFilterV13v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 1, 16)
)
tFilterV13v0Compliance.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterScalarGroup"),
        ("TIMETRA-FILTER-MIB", "tIPFilterV12v0Group"),
        ("TIMETRA-FILTER-MIB", "tIPFilterV13v0Group"),
        ("TIMETRA-FILTER-MIB", "tMacFilterV8v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterLogGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterLogV5v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterRedirectPolicyV13v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationsV11v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationsV12v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationObjV12v0Group"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterV12v0Group"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterV13v0Group"),
        ("TIMETRA-FILTER-MIB", "tTodPolicies77x0V5v0Group"),
        ("TIMETRA-FILTER-MIB", "tToDPoliciesV5v0NotifyGroup"),
        ("TIMETRA-FILTER-MIB", "tMacFilterVidFilteringV9v0Group"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterV10v0Group"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterV13v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterNameV10v0Group"),
        ("TIMETRA-FILTER-MIB", "tLiFilterV12v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterPrefixListV11v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbeddedInsertV11v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbeddedInsertV12v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbeddedInsertV13v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterPortListV11v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterSystemFilterV13v0Group"),
        ("TIMETRA-FILTER-MIB", "tMacFilterV13v0Group"))
)
if mibBuilder.loadTexts:
    tFilterV13v0Compliance.setStatus(
        "obsolete"
    )

tFilterV14v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 1, 17)
)
tFilterV14v0Compliance.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterScalarGroup"),
        ("TIMETRA-FILTER-MIB", "tIPFilterV14v0Group"),
        ("TIMETRA-FILTER-MIB", "tIPFilterV13v0Group"),
        ("TIMETRA-FILTER-MIB", "tMacFilterV8v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterLogGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterLogV5v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterRedirectPolicyV13v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationsV11v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationsV12v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationObjV12v0Group"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterV14v0Group"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterV13v0Group"),
        ("TIMETRA-FILTER-MIB", "tMacFilterVidFilteringV9v0Group"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterV10v0Group"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterV13v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterNameV10v0Group"),
        ("TIMETRA-FILTER-MIB", "tLiFilterV12v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterPrefixListV11v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbeddedInsertV11v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbeddedInsertV12v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbeddedInsertV13v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterPortListV11v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterSystemFilterV13v0Group"),
        ("TIMETRA-FILTER-MIB", "tMacFilterV13v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbedFlowspecGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationsV14v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterIPvXRedundantActionGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterMacRedundantActionGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbedVsdGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterEntryStatGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbeddedRefGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterRemarkDscpGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterRemarkDscpExtGroup"))
)
if mibBuilder.loadTexts:
    tFilterV14v0Compliance.setStatus(
        "obsolete"
    )

tFilterV15v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 1, 18)
)
tFilterV15v0Compliance.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterScalarGroup"),
        ("TIMETRA-FILTER-MIB", "tIPFilterV14v0Group"),
        ("TIMETRA-FILTER-MIB", "tIPFilterV13v0Group"),
        ("TIMETRA-FILTER-MIB", "tMacFilterV8v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterLogGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterLogV5v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterRedirectPolicyV13v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationsV11v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationObjV12v0Group"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterV14v0Group"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterV13v0Group"),
        ("TIMETRA-FILTER-MIB", "tMacFilterVidFilteringV9v0Group"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterV10v0Group"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterV13v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterNameV10v0Group"),
        ("TIMETRA-FILTER-MIB", "tLiFilterV12v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterPrefixListV11v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbeddedInsertV11v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbeddedInsertV12v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbeddedInsertV13v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterPortListV11v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterSystemFilterV13v0Group"),
        ("TIMETRA-FILTER-MIB", "tMacFilterV13v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbedFlowspecGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationsV14v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterIPvXRedundantActionGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterMacRedundantActionGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbedVsdGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterEntryStatGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbeddedRefGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterRemarkDscpGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterRemarkDscpExtGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterPrefListRtrBgpPeersGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterPrefListInfoGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterForwardVprnTargetGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationsV15v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterFwdBondingConnectionGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterSelectiveFlowspecGroup"))
)
if mibBuilder.loadTexts:
    tFilterV15v0Compliance.setStatus(
        "obsolete"
    )

tFilterV16v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 1, 19)
)
tFilterV16v0Compliance.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterScalarGroup"),
        ("TIMETRA-FILTER-MIB", "tIPFilterV14v0Group"),
        ("TIMETRA-FILTER-MIB", "tIPFilterV13v0Group"),
        ("TIMETRA-FILTER-MIB", "tMacFilterV8v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterLogGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterLogV5v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterRedirectPolicyV13v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationsV11v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationObjV12v0Group"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterV14v0Group"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterV13v0Group"),
        ("TIMETRA-FILTER-MIB", "tMacFilterVidFilteringV9v0Group"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterV10v0Group"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterV13v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterNameV10v0Group"),
        ("TIMETRA-FILTER-MIB", "tLiFilterV12v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterPrefixListV11v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbeddedInsertV11v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbeddedInsertV12v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbeddedInsertV13v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterPortListV11v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterSystemFilterV13v0Group"),
        ("TIMETRA-FILTER-MIB", "tMacFilterV13v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbedFlowspecGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationsV14v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterIPvXRedundantActionGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterMacRedundantActionGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbedVsdGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterEntryStatGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbeddedRefGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterRemarkDscpGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterRemarkDscpExtGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterPrefListRtrBgpPeersGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterPrefListInfoGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterForwardVprnTargetGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationsV15v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterFwdBondingConnectionGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterSelectiveFlowspecGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterMatchTcpFlagsGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterActionFc"),
        ("TIMETRA-FILTER-MIB", "tFilterRPPingSrcAddressGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterRPActiveDstChangeNotifGrp"),
        ("TIMETRA-FILTER-MIB", "tFilterRPActiveDstChangeGrp"),
        ("TIMETRA-FILTER-MIB", "tFilterRPlcyBindingGroup"),
        ("TIMETRA-FILTER-MIB", "tFltrGreTunTempGroup"),
        ("TIMETRA-FILTER-MIB", "tFltrPrefListPrefExcludeGrp"),
        ("TIMETRA-FILTER-MIB", "fltrMdAutoIdV16v0Group"),
        ("TIMETRA-FILTER-MIB", "tFltrPatternMatchGroup"))
)
if mibBuilder.loadTexts:
    tFilterV16v0Compliance.setStatus(
        "obsolete"
    )

tFilterV19v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 1, 20)
)
tFilterV19v0Compliance.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterScalarGroup"),
        ("TIMETRA-FILTER-MIB", "tIPFilterV14v0Group"),
        ("TIMETRA-FILTER-MIB", "tIPFilterV13v0Group"),
        ("TIMETRA-FILTER-MIB", "tMacFilterV8v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterLogGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterLogV5v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterRedirectPolicyV19v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationsV11v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationObjV12v0Group"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterV14v0Group"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterV13v0Group"),
        ("TIMETRA-FILTER-MIB", "tMacFilterVidFilteringV9v0Group"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterV10v0Group"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterV13v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterNameV10v0Group"),
        ("TIMETRA-FILTER-MIB", "tLiFilterV12v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterPrefixListV11v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbeddedInsertV11v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbeddedInsertV12v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbeddedInsertV13v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterPortListV11v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterSystemFilterV13v0Group"),
        ("TIMETRA-FILTER-MIB", "tMacFilterV13v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbedFlowspecGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationsV14v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterIPvXRedundantActionGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterMacRedundantActionGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbedVsdGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterEntryStatGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbeddedRefGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterRemarkDscpGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterRemarkDscpExtGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterPrefListRtrBgpPeersGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterPrefListInfoGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterForwardVprnTargetGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationsV15v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterFwdBondingConnectionGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterSelectiveFlowspecGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterMatchTcpFlagsGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterActionFc"),
        ("TIMETRA-FILTER-MIB", "tFilterRPPingSrcAddressGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterRPActiveDstChangeNotifGrp"),
        ("TIMETRA-FILTER-MIB", "tFilterRPActiveDstChangeGrp"),
        ("TIMETRA-FILTER-MIB", "tFilterRPlcyBindingGroup"),
        ("TIMETRA-FILTER-MIB", "tFltrGreTunTempGroup"),
        ("TIMETRA-FILTER-MIB", "tFltrPrefListPrefExcludeGrp"),
        ("TIMETRA-FILTER-MIB", "fltrMdAutoIdV16v0Group"),
        ("TIMETRA-FILTER-MIB", "tFltrPatternMatchGroup"),
        ("TIMETRA-FILTER-MIB", "tFltrMatchMacForIPvXGroup"),
        ("TIMETRA-FILTER-MIB", "tFltrMatchPacketLengthGroup"),
        ("TIMETRA-FILTER-MIB", "tFltrFilterNameInLIGroup"),
        ("TIMETRA-FILTER-MIB", "tFltrCAMTypeGroup"),
        ("TIMETRA-FILTER-MIB", "tLiFltrAssocFltrNameGroup"),
        ("TIMETRA-FILTER-MIB", "tFltrIPv6ExceptionV19v0Group"),
        ("TIMETRA-FILTER-MIB", "tFltrFwdMplsPlcyEndptGrp"),
        ("TIMETRA-FILTER-MIB", "tFltrFwdSrtePlcyEndptColorGrp"))
)
if mibBuilder.loadTexts:
    tFilterV19v0Compliance.setStatus(
        "obsolete"
    )

tFilterV20v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 1, 21)
)
tFilterV20v0Compliance.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterScalarGroup"),
        ("TIMETRA-FILTER-MIB", "tIPFilterV14v0Group"),
        ("TIMETRA-FILTER-MIB", "tIPFilterV13v0Group"),
        ("TIMETRA-FILTER-MIB", "tMacFilterV8v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterLogGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterLogV5v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterRedirectPolicyV19v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationsV11v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationObjV12v0Group"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterV14v0Group"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterV13v0Group"),
        ("TIMETRA-FILTER-MIB", "tMacFilterVidFilteringV9v0Group"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterV10v0Group"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterV13v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterNameV10v0Group"),
        ("TIMETRA-FILTER-MIB", "tLiFilterV12v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterPrefixListV11v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbeddedInsertV11v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbeddedInsertV12v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbeddedInsertV13v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterPortListV11v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterSystemFilterV13v0Group"),
        ("TIMETRA-FILTER-MIB", "tMacFilterV13v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbedFlowspecGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationsV14v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterIPvXRedundantActionGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterMacRedundantActionGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbedVsdGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterEntryStatGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbeddedRefGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterRemarkDscpGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterRemarkDscpExtGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterPrefListRtrBgpPeersGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterPrefListInfoGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterForwardVprnTargetGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationsV15v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterFwdBondingConnectionGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterSelectiveFlowspecGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterMatchTcpFlagsGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterActionFc"),
        ("TIMETRA-FILTER-MIB", "tFilterRPPingSrcAddressGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterRPActiveDstChangeNotifGrp"),
        ("TIMETRA-FILTER-MIB", "tFilterRPActiveDstChangeGrp"),
        ("TIMETRA-FILTER-MIB", "tFilterRPlcyBindingGroup"),
        ("TIMETRA-FILTER-MIB", "tFltrGreTunTempGroup"),
        ("TIMETRA-FILTER-MIB", "tFltrPrefListPrefExcludeGrp"),
        ("TIMETRA-FILTER-MIB", "fltrMdAutoIdV16v0Group"),
        ("TIMETRA-FILTER-MIB", "tFltrPatternMatchGroup"),
        ("TIMETRA-FILTER-MIB", "tFltrMatchMacForIPvXGroup"),
        ("TIMETRA-FILTER-MIB", "tFltrMatchPacketLengthGroup"),
        ("TIMETRA-FILTER-MIB", "tFltrFilterNameInLIGroup"),
        ("TIMETRA-FILTER-MIB", "tFltrCAMTypeGroup"),
        ("TIMETRA-FILTER-MIB", "tLiFltrAssocFltrNameGroup"),
        ("TIMETRA-FILTER-MIB", "tFltrIPv6ExceptionV19v0Group"),
        ("TIMETRA-FILTER-MIB", "tFltrFwdMplsPlcyEndptGrp"),
        ("TIMETRA-FILTER-MIB", "tFltrFwdSrtePlcyEndptColorGrp"),
        ("TIMETRA-FILTER-MIB", "tLiFltrMatchFragmentGroup"),
        ("TIMETRA-FILTER-MIB", "fltrMdAutoIdV20v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterMatchProtocolListGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterMatchDestClassGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterL2AwareNatBypassGroup"),
        ("TIMETRA-FILTER-MIB", "tFltrLiRsvdBlockRangeChgNotifGrp"),
        ("TIMETRA-FILTER-MIB", "tFltrCflowdSampleProfileGroup"))
)
if mibBuilder.loadTexts:
    tFilterV20v0Compliance.setStatus(
        "obsolete"
    )

tFilterV21v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 1, 22)
)
tFilterV21v0Compliance.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterScalarGroup"),
        ("TIMETRA-FILTER-MIB", "tIPFilterV21v0Group"),
        ("TIMETRA-FILTER-MIB", "tMacFilterV21v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterLogGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterLogV5v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterRedirectPolicyV19v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationsV11v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationObjV12v0Group"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterV21v0Group"),
        ("TIMETRA-FILTER-MIB", "tMacFilterVidFilteringV9v0Group"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterV10v0Group"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterV13v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterNameV10v0Group"),
        ("TIMETRA-FILTER-MIB", "tLiFilterV12v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterPrefixListV11v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbeddedInsertV11v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbeddedInsertV12v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbeddedInsertV13v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterPortListV11v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterSystemFilterV13v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbedFlowspecGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationsV14v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterIPvXRedundantActionGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterMacRedundantActionGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbedVsdGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterEntryStatGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbeddedRefGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterRemarkDscpGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterRemarkDscpExtGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterPrefListRtrBgpPeersGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterPrefListInfoGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterForwardVprnTargetGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationsV15v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterFwdBondingConnectionGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterSelectiveFlowspecGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterMatchTcpFlagsGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterActionFc"),
        ("TIMETRA-FILTER-MIB", "tFilterRPPingSrcAddressGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterRPActiveDstChangeNotifGrp"),
        ("TIMETRA-FILTER-MIB", "tFilterRPActiveDstChangeGrp"),
        ("TIMETRA-FILTER-MIB", "tFilterRPlcyBindingGroup"),
        ("TIMETRA-FILTER-MIB", "tFltrGreTunTempGroup"),
        ("TIMETRA-FILTER-MIB", "tFltrPrefListPrefExcludeGrp"),
        ("TIMETRA-FILTER-MIB", "fltrMdAutoIdV16v0Group"),
        ("TIMETRA-FILTER-MIB", "tFltrPatternMatchGroup"),
        ("TIMETRA-FILTER-MIB", "tFltrMatchMacForIPvXGroup"),
        ("TIMETRA-FILTER-MIB", "tFltrMatchPacketLengthGroup"),
        ("TIMETRA-FILTER-MIB", "tFltrFilterNameInLIGroup"),
        ("TIMETRA-FILTER-MIB", "tFltrCAMTypeGroup"),
        ("TIMETRA-FILTER-MIB", "tLiFltrAssocFltrNameGroup"),
        ("TIMETRA-FILTER-MIB", "tFltrIPv6ExceptionV19v0Group"),
        ("TIMETRA-FILTER-MIB", "tFltrFwdMplsPlcyEndptGrp"),
        ("TIMETRA-FILTER-MIB", "tFltrFwdSrtePlcyEndptColorGrp"),
        ("TIMETRA-FILTER-MIB", "tLiFltrMatchFragmentGroup"),
        ("TIMETRA-FILTER-MIB", "fltrMdAutoIdV20v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterMatchProtocolListGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterMatchDestClassGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterL2AwareNatBypassGroup"),
        ("TIMETRA-FILTER-MIB", "tFltrLiRsvdBlockRangeChgNotifGrp"),
        ("TIMETRA-FILTER-MIB", "tFltrCflowdSampleProfileGroup"),
        ("TIMETRA-FILTER-MIB", "tFltrEntryCollectStatsIPvXGroup"),
        ("TIMETRA-FILTER-MIB", "tFltrEntryCollectStatsMacGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterMacFltrActionGroupV21"),
        ("TIMETRA-FILTER-MIB", "tFilterMatchTTLGroup"),
        ("TIMETRA-FILTER-MIB", "tFltrMatchSrcOrDstIpGroup"))
)
if mibBuilder.loadTexts:
    tFilterV21v0Compliance.setStatus(
        "current"
    )

tFilterV22v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 21, 1, 23)
)
tFilterV22v0Compliance.setObjects(
      *(("TIMETRA-FILTER-MIB", "tFilterScalarGroup"),
        ("TIMETRA-FILTER-MIB", "tIPFilterV21v0Group"),
        ("TIMETRA-FILTER-MIB", "tMacFilterV21v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterLogGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterLogV5v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterRedirectPolicyV19v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationsV11v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationObjV12v0Group"),
        ("TIMETRA-FILTER-MIB", "tIPv6FilterV21v0Group"),
        ("TIMETRA-FILTER-MIB", "tMacFilterVidFilteringV9v0Group"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterV10v0Group"),
        ("TIMETRA-FILTER-MIB", "tDhcpFilterV13v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterNameV10v0Group"),
        ("TIMETRA-FILTER-MIB", "tLiFilterV12v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterPrefixListV11v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbeddedInsertV11v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbeddedInsertV12v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbeddedInsertV13v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterPortListV11v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterSystemFilterV13v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbedFlowspecGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationsV14v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterIPvXRedundantActionGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterMacRedundantActionGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbedVsdGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterEntryStatGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterEmbeddedRefGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterRemarkDscpGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterRemarkDscpExtGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterPrefListRtrBgpPeersGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterPrefListInfoGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterForwardVprnTargetGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterNotificationsV15v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterFwdBondingConnectionGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterSelectiveFlowspecGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterMatchTcpFlagsGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterActionFc"),
        ("TIMETRA-FILTER-MIB", "tFilterRPPingSrcAddressGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterRPActiveDstChangeNotifGrp"),
        ("TIMETRA-FILTER-MIB", "tFilterRPActiveDstChangeGrp"),
        ("TIMETRA-FILTER-MIB", "tFilterRPlcyBindingGroup"),
        ("TIMETRA-FILTER-MIB", "tFltrGreTunTempGroup"),
        ("TIMETRA-FILTER-MIB", "tFltrPrefListPrefExcludeGrp"),
        ("TIMETRA-FILTER-MIB", "fltrMdAutoIdV16v0Group"),
        ("TIMETRA-FILTER-MIB", "tFltrPatternMatchGroup"),
        ("TIMETRA-FILTER-MIB", "tFltrMatchMacForIPvXGroup"),
        ("TIMETRA-FILTER-MIB", "tFltrMatchPacketLengthGroup"),
        ("TIMETRA-FILTER-MIB", "tFltrFilterNameInLIGroup"),
        ("TIMETRA-FILTER-MIB", "tFltrCAMTypeGroup"),
        ("TIMETRA-FILTER-MIB", "tLiFltrAssocFltrNameGroup"),
        ("TIMETRA-FILTER-MIB", "tFltrIPv6ExceptionV19v0Group"),
        ("TIMETRA-FILTER-MIB", "tFltrFwdMplsPlcyEndptGrp"),
        ("TIMETRA-FILTER-MIB", "tFltrFwdSrtePlcyEndptColorGrp"),
        ("TIMETRA-FILTER-MIB", "tLiFltrMatchFragmentGroup"),
        ("TIMETRA-FILTER-MIB", "fltrMdAutoIdV20v0Group"),
        ("TIMETRA-FILTER-MIB", "tFilterMatchProtocolListGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterMatchDestClassGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterL2AwareNatBypassGroup"),
        ("TIMETRA-FILTER-MIB", "tFltrLiRsvdBlockRangeChgNotifGrp"),
        ("TIMETRA-FILTER-MIB", "tFltrCflowdSampleProfileGroup"),
        ("TIMETRA-FILTER-MIB", "tFltrEntryCollectStatsIPvXGroup"),
        ("TIMETRA-FILTER-MIB", "tFltrEntryCollectStatsMacGroup"),
        ("TIMETRA-FILTER-MIB", "tFilterMacFltrActionGroupV21"),
        ("TIMETRA-FILTER-MIB", "tFilterMatchTTLGroup"),
        ("TIMETRA-FILTER-MIB", "tFltrMatchSrcOrDstIpGroup"))
)
if mibBuilder.loadTexts:
    tFilterV22v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-FILTER-MIB",
    **{"TFilterID": TFilterID,
       "TFilterFlowspecGroupId": TFilterFlowspecGroupId,
       "TIPFilterIdOrEmpty": TIPFilterIdOrEmpty,
       "TVsdFilterID": TVsdFilterID,
       "TConfigOrVsdFilterID": TConfigOrVsdFilterID,
       "TAnyFilterID": TAnyFilterID,
       "TFilterScope": TFilterScope,
       "TItemMatch": TItemMatch,
       "TFragmentMatch": TFragmentMatch,
       "TAnyEntryId": TAnyEntryId,
       "TEntryIdOrZero": TEntryIdOrZero,
       "TEntryId": TEntryId,
       "TLimitedEntryId": TLimitedEntryId,
       "TDhcpEntryId": TDhcpEntryId,
       "TEntryBlockSize": TEntryBlockSize,
       "TFilterAction": TFilterAction,
       "TFilterPbrDownActionOvr": TFilterPbrDownActionOvr,
       "TFilterActionOrDefault": TFilterActionOrDefault,
       "TIPvXFilterEntryAction": TIPvXFilterEntryAction,
       "TFilterPbrTargetStatus": TFilterPbrTargetStatus,
       "TFilterDownloadedAction": TFilterDownloadedAction,
       "TFilterEntryActionId": TFilterEntryActionId,
       "TMacFilterEntryAction": TMacFilterEntryAction,
       "TIPvXFilterEntryActionExt": TIPvXFilterEntryActionExt,
       "TFilterLogId": TFilterLogId,
       "TFilterLogDestination": TFilterLogDestination,
       "TTimeRangeState": TTimeRangeState,
       "TFilterLogSummaryCriterium": TFilterLogSummaryCriterium,
       "TFilterType": TFilterType,
       "TFilterSubInsSpaceOwner": TFilterSubInsSpaceOwner,
       "TFltrGrpInsrtdEntriesApplication": TFltrGrpInsrtdEntriesApplication,
       "TDHCPFilterID": TDHCPFilterID,
       "TDhcpFilterAction": TDhcpFilterAction,
       "TDhcpFilterMatch": TDhcpFilterMatch,
       "TFltrPrefixListType": TFltrPrefixListType,
       "TmnxEmbeddedFltrOperState": TmnxEmbeddedFltrOperState,
       "TmnxEmbeddedFltrAdminState": TmnxEmbeddedFltrAdminState,
       "TmnxFltrEmbeddedEntryState": TmnxFltrEmbeddedEntryState,
       "TmnxFilterApplyPathSource": TmnxFilterApplyPathSource,
       "TFltrPortSelector": TFltrPortSelector,
       "TFltrMatchIpSelector": TFltrMatchIpSelector,
       "TFilterRPBindingOperator": TFilterRPBindingOperator,
       "TFilterPacketLength": TFilterPacketLength,
       "TFilterIpv6MatchPacketLength": TFilterIpv6MatchPacketLength,
       "TFilterTTL": TFilterTTL,
       "TmnxFilterRPlcyTestLastAction": TmnxFilterRPlcyTestLastAction,
       "TmnxFilterRPlcyTestRespAction": TmnxFilterRPlcyTestRespAction,
       "TFilterEgressPBR": TFilterEgressPBR,
       "TFilterEsi": TFilterEsi,
       "TFilterEntryActionRateLimit": TFilterEntryActionRateLimit,
       "TFilterEmbedOffset": TFilterEmbedOffset,
       "TIPvXFilterType": TIPvXFilterType,
       "TmnxFilterCflowdSampleProfileId": TmnxFilterCflowdSampleProfileId,
       "timetraFilterMIBModule": timetraFilterMIBModule,
       "tFilterMIBConformance": tFilterMIBConformance,
       "tFilterMIBCompliances": tFilterMIBCompliances,
       "tFilter7450V4v0Compliance": tFilter7450V4v0Compliance,
       "tFilter7750V4v0Compliance": tFilter7750V4v0Compliance,
       "tFilter7450V5v0Compliance": tFilter7450V5v0Compliance,
       "tFilter77x0V5v0Compliance": tFilter77x0V5v0Compliance,
       "tFilter7450V6v0Compliance": tFilter7450V6v0Compliance,
       "tFilter77x0V6v0Compliance": tFilter77x0V6v0Compliance,
       "tFilter7450V8v0Compliance": tFilter7450V8v0Compliance,
       "tFilter77x0V8v0Compliance": tFilter77x0V8v0Compliance,
       "tFilter7xxxV9v0Compliance": tFilter7xxxV9v0Compliance,
       "tFilter7xxxV10v0Compliance": tFilter7xxxV10v0Compliance,
       "tFilter7xxxV11v0Compliance": tFilter7xxxV11v0Compliance,
       "tFilter7xxxV12v0Compliance": tFilter7xxxV12v0Compliance,
       "tFilterV13v0Compliance": tFilterV13v0Compliance,
       "tFilterV14v0Compliance": tFilterV14v0Compliance,
       "tFilterV15v0Compliance": tFilterV15v0Compliance,
       "tFilterV16v0Compliance": tFilterV16v0Compliance,
       "tFilterV19v0Compliance": tFilterV19v0Compliance,
       "tFilterV20v0Compliance": tFilterV20v0Compliance,
       "tFilterV21v0Compliance": tFilterV21v0Compliance,
       "tFilterV22v0Compliance": tFilterV22v0Compliance,
       "tFilterMIBGroups": tFilterMIBGroups,
       "tFilterLogGroup": tFilterLogGroup,
       "tFilterRedirectPolicyGroup": tFilterRedirectPolicyGroup,
       "tFilterScalarGroup": tFilterScalarGroup,
       "tFilterNotificationObjGroup": tFilterNotificationObjGroup,
       "tFilterNotificationsGroup": tFilterNotificationsGroup,
       "tIPv6FilterV4v0Group": tIPv6FilterV4v0Group,
       "tIPFilterV4v0Group": tIPFilterV4v0Group,
       "tMacFilterV4v0Group": tMacFilterV4v0Group,
       "tTodPoliciesV4v0Group": tTodPoliciesV4v0Group,
       "tmnxFilterObsoleteGroup": tmnxFilterObsoleteGroup,
       "tToDPoliciesV5v0NotifyGroup": tToDPoliciesV5v0NotifyGroup,
       "tIPFilterV5v0Group": tIPFilterV5v0Group,
       "tFilterLogV5v0Group": tFilterLogV5v0Group,
       "tTodPolicies77450V5v0Group": tTodPolicies77450V5v0Group,
       "tTodPolicies77x0V5v0Group": tTodPolicies77x0V5v0Group,
       "tFilterNotificationObjV5v0Group": tFilterNotificationObjV5v0Group,
       "tIPFilterV6v0Group": tIPFilterV6v0Group,
       "tMacFilterV6v0Group": tMacFilterV6v0Group,
       "tIPv6FilterV6v0Group": tIPv6FilterV6v0Group,
       "tIPFilterV8v0Group": tIPFilterV8v0Group,
       "tIPv6FilterV8v0Group": tIPv6FilterV8v0Group,
       "tFilterNotificationObjV8v0Group": tFilterNotificationObjV8v0Group,
       "tFilterNotificationsV8v0Group": tFilterNotificationsV8v0Group,
       "tMacFilterV8v0Group": tMacFilterV8v0Group,
       "tMacFilterVidFilteringV9v0Group": tMacFilterVidFilteringV9v0Group,
       "tIPFilterV9v0Group": tIPFilterV9v0Group,
       "tFilterNotificationsV9v0Group": tFilterNotificationsV9v0Group,
       "tFilterNotificationObjV9v0Group": tFilterNotificationObjV9v0Group,
       "tDhcpFilterV9v0Group": tDhcpFilterV9v0Group,
       "tIPv6FilterV10v0Group": tIPv6FilterV10v0Group,
       "tFilterNameV10v0Group": tFilterNameV10v0Group,
       "tDhcpFilterV10v0Group": tDhcpFilterV10v0Group,
       "tLiFilterV10v0Group": tLiFilterV10v0Group,
       "tFilterPrefixListV10v0Group": tFilterPrefixListV10v0Group,
       "tIPv6FilterV11v0Group": tIPv6FilterV11v0Group,
       "tFilterEmbeddedInsertV11v0Group": tFilterEmbeddedInsertV11v0Group,
       "tFilterPortListV11v0Group": tFilterPortListV11v0Group,
       "tFilterPrefixListV11v0Group": tFilterPrefixListV11v0Group,
       "tIPFilterV11v0Group": tIPFilterV11v0Group,
       "tFilterNotificationsV11v0Group": tFilterNotificationsV11v0Group,
       "tFilterNotificationObjV11v0Group": tFilterNotificationObjV11v0Group,
       "tIPFilterV12v0Group": tIPFilterV12v0Group,
       "tIPv6FilterV12v0Group": tIPv6FilterV12v0Group,
       "tLiFilterV12v0Group": tLiFilterV12v0Group,
       "tFilterEmbeddedInsertV12v0Group": tFilterEmbeddedInsertV12v0Group,
       "tFilterNotificationsV12v0Group": tFilterNotificationsV12v0Group,
       "tFilterRedirectPolicyV13v0Group": tFilterRedirectPolicyV13v0Group,
       "tFilterNotificationObjV12v0Group": tFilterNotificationObjV12v0Group,
       "tIPFilterV13v0Group": tIPFilterV13v0Group,
       "tIPv6FilterV13v0Group": tIPv6FilterV13v0Group,
       "tFilterRPlcyV13v0ObsoleteGroup": tFilterRPlcyV13v0ObsoleteGroup,
       "tFilterSystemFilterV13v0Group": tFilterSystemFilterV13v0Group,
       "tFilterEmbeddedInsertV13v0Group": tFilterEmbeddedInsertV13v0Group,
       "tDhcpFilterV13v0Group": tDhcpFilterV13v0Group,
       "tMacFilterV13v0Group": tMacFilterV13v0Group,
       "tFilterNotificationsV14v0Group": tFilterNotificationsV14v0Group,
       "tFilterEmbedFlowspecGroup": tFilterEmbedFlowspecGroup,
       "tFilterIPvXRedundantActionGroup": tFilterIPvXRedundantActionGroup,
       "tFilterMacRedundantActionGroup": tFilterMacRedundantActionGroup,
       "tFilterEmbedVsdGroup": tFilterEmbedVsdGroup,
       "tFilterEmbeddedRefGroup": tFilterEmbeddedRefGroup,
       "tFilterTimeRangeObsoletedGroup": tFilterTimeRangeObsoletedGroup,
       "tFilterObsoletedNotifsGroup": tFilterObsoletedNotifsGroup,
       "tFilterEntryStatGroup": tFilterEntryStatGroup,
       "tFilterRemarkDscpGroup": tFilterRemarkDscpGroup,
       "tIPFilterV14v0Group": tIPFilterV14v0Group,
       "tIPv6FilterV14v0Group": tIPv6FilterV14v0Group,
       "tFilterParamsObsoletedGroup": tFilterParamsObsoletedGroup,
       "tFilterRemarkDscpExtGroup": tFilterRemarkDscpExtGroup,
       "tFilterPrefListRtrBgpPeersGroup": tFilterPrefListRtrBgpPeersGroup,
       "tFilterPrefListInfoGroup": tFilterPrefListInfoGroup,
       "tFilterForwardVprnTargetGroup": tFilterForwardVprnTargetGroup,
       "tFilterNotificationsV15v0Group": tFilterNotificationsV15v0Group,
       "tFilterObsoleteNotifsGroup": tFilterObsoleteNotifsGroup,
       "tFilterFwdBondingConnectionGroup": tFilterFwdBondingConnectionGroup,
       "tFilterSelectiveFlowspecGroup": tFilterSelectiveFlowspecGroup,
       "tFilterMatchTcpFlagsGroup": tFilterMatchTcpFlagsGroup,
       "tFilterActionFc": tFilterActionFc,
       "tFilterRPPingSrcAddressGroup": tFilterRPPingSrcAddressGroup,
       "tFilterRPActiveDstChangeNotifGrp": tFilterRPActiveDstChangeNotifGrp,
       "tFilterRPActiveDstChangeGrp": tFilterRPActiveDstChangeGrp,
       "tFilterRPlcyBindingGroup": tFilterRPlcyBindingGroup,
       "tFltrGreTunTempGroup": tFltrGreTunTempGroup,
       "tFltrPrefListPrefExcludeGrp": tFltrPrefListPrefExcludeGrp,
       "fltrMdAutoIdV16v0Group": fltrMdAutoIdV16v0Group,
       "tFltrPatternMatchGroup": tFltrPatternMatchGroup,
       "tFilterRedirectPolicyV19v0Group": tFilterRedirectPolicyV19v0Group,
       "tFltrRPTestV19v0ObsoleteGroup": tFltrRPTestV19v0ObsoleteGroup,
       "tFltrCAMTypeGroup": tFltrCAMTypeGroup,
       "tFltrMatchMacForIPvXGroup": tFltrMatchMacForIPvXGroup,
       "tFltrMatchPacketLengthGroup": tFltrMatchPacketLengthGroup,
       "tFltrFilterNameInLIGroup": tFltrFilterNameInLIGroup,
       "tLiFltrAssocFltrNameGroup": tLiFltrAssocFltrNameGroup,
       "tFltrIPv6ExceptionV19v0Group": tFltrIPv6ExceptionV19v0Group,
       "tFltrFwdMplsPlcyEndptGrp": tFltrFwdMplsPlcyEndptGrp,
       "tFltrFwdSrtePlcyEndptColorGrp": tFltrFwdSrtePlcyEndptColorGrp,
       "tLiFltrMatchFragmentGroup": tLiFltrMatchFragmentGroup,
       "fltrMdAutoIdV20v0Group": fltrMdAutoIdV20v0Group,
       "tFilterMatchProtocolListGroup": tFilterMatchProtocolListGroup,
       "tFilterMatchDestClassGroup": tFilterMatchDestClassGroup,
       "tFilterL2AwareNatBypassGroup": tFilterL2AwareNatBypassGroup,
       "tFltrLiRsvdBlockRangeChgNotifGrp": tFltrLiRsvdBlockRangeChgNotifGrp,
       "tFltrCflowdSampleProfileGroup": tFltrCflowdSampleProfileGroup,
       "tFltrEntryCollectStatsIPvXGroup": tFltrEntryCollectStatsIPvXGroup,
       "tFltrEntryCollectStatsMacGroup": tFltrEntryCollectStatsMacGroup,
       "tFilterMacFltrActionGroupV21": tFilterMacFltrActionGroupV21,
       "tFltrParamsActionObsoleteGroup": tFltrParamsActionObsoleteGroup,
       "tIPFilterV21v0Group": tIPFilterV21v0Group,
       "tIPv6FilterV21v0Group": tIPv6FilterV21v0Group,
       "tMacFilterV21v0Group": tMacFilterV21v0Group,
       "tFilterMatchTTLGroup": tFilterMatchTTLGroup,
       "tFltrMatchSrcOrDstIpGroup": tFltrMatchSrcOrDstIpGroup,
       "tFilterObjects": tFilterObjects,
       "tIPFilterTable": tIPFilterTable,
       "tIPFilterEntry": tIPFilterEntry,
       "tIPFilterId": tIPFilterId,
       "tIPFilterRowStatus": tIPFilterRowStatus,
       "tIPFilterScope": tIPFilterScope,
       "tIPFilterDescription": tIPFilterDescription,
       "tIPFilterDefaultAction": tIPFilterDefaultAction,
       "tIPFilterRadiusInsertPt": tIPFilterRadiusInsertPt,
       "tIPFilterRadiusInsertSize": tIPFilterRadiusInsertSize,
       "tIPFilterCreditCntrlInsertPt": tIPFilterCreditCntrlInsertPt,
       "tIPFilterCreditCntrlInsertSize": tIPFilterCreditCntrlInsertSize,
       "tIPFilterSubInsertHighWmark": tIPFilterSubInsertHighWmark,
       "tIPFilterSubInsertLowWmark": tIPFilterSubInsertLowWmark,
       "tIpFilterCreditCntrlNbrInsertd": tIpFilterCreditCntrlNbrInsertd,
       "tIpFilterRadiusNbrInsertd": tIpFilterRadiusNbrInsertd,
       "tIpFilterName": tIpFilterName,
       "tIPFilterHostSharedInsertPt": tIPFilterHostSharedInsertPt,
       "tIPFilterHostSharedInsertSize": tIPFilterHostSharedInsertSize,
       "tIpFilterHostSharedNbrInsertd": tIpFilterHostSharedNbrInsertd,
       "tIPFilterHostSharedHighWmark": tIPFilterHostSharedHighWmark,
       "tIPFilterHostSharedLowWmark": tIPFilterHostSharedLowWmark,
       "tIPFilterNbrHostSharedFltrs": tIPFilterNbrHostSharedFltrs,
       "tIPFilterSharedPccRuleInsrtPt": tIPFilterSharedPccRuleInsrtPt,
       "tIPFilterSharedPccRuleInsrtSize": tIPFilterSharedPccRuleInsrtSize,
       "tIPFilterSharedPccRuleNbrInsrtd": tIPFilterSharedPccRuleNbrInsrtd,
       "tIPFilterChainToSystemFilter": tIPFilterChainToSystemFilter,
       "tIPFilterType": tIPFilterType,
       "tIPFilterParamsTable": tIPFilterParamsTable,
       "tIPFilterParamsEntry": tIPFilterParamsEntry,
       "tIPFilterParamsIndex": tIPFilterParamsIndex,
       "tIPFilterParamsRowStatus": tIPFilterParamsRowStatus,
       "tIPFilterParamsLogId": tIPFilterParamsLogId,
       "tIPFilterParamsDescription": tIPFilterParamsDescription,
       "tIPFilterParamsAction": tIPFilterParamsAction,
       "tIPFilterParamsForwardNH": tIPFilterParamsForwardNH,
       "tIPFilterParamsForwardNHIndirect": tIPFilterParamsForwardNHIndirect,
       "tIPFilterParamsRemarkDSCP": tIPFilterParamsRemarkDSCP,
       "tIPFilterParamsRemarkDSCPMask": tIPFilterParamsRemarkDSCPMask,
       "tIPFilterParamsRemarkDot1p": tIPFilterParamsRemarkDot1p,
       "tIPFilterParamsSourceIpAddr": tIPFilterParamsSourceIpAddr,
       "tIPFilterParamsSourceIpMask": tIPFilterParamsSourceIpMask,
       "tIPFilterParamsDestinationIpAddr": tIPFilterParamsDestinationIpAddr,
       "tIPFilterParamsDestinationIpMask": tIPFilterParamsDestinationIpMask,
       "tIPFilterParamsProtocol": tIPFilterParamsProtocol,
       "tIPFilterParamsSourcePortValue1": tIPFilterParamsSourcePortValue1,
       "tIPFilterParamsSourcePortValue2": tIPFilterParamsSourcePortValue2,
       "tIPFilterParamsSourcePortOperator": tIPFilterParamsSourcePortOperator,
       "tIPFilterParamsDestPortValue1": tIPFilterParamsDestPortValue1,
       "tIPFilterParamsDestPortValue2": tIPFilterParamsDestPortValue2,
       "tIPFilterParamsDestPortOperator": tIPFilterParamsDestPortOperator,
       "tIPFilterParamsDSCP": tIPFilterParamsDSCP,
       "tIPFilterParamsFragment": tIPFilterParamsFragment,
       "tIPFilterParamsOptionPresent": tIPFilterParamsOptionPresent,
       "tIPFilterParamsIpOptionValue": tIPFilterParamsIpOptionValue,
       "tIPFilterParamsIpOptionMask": tIPFilterParamsIpOptionMask,
       "tIPFilterParamsMultipleOption": tIPFilterParamsMultipleOption,
       "tIPFilterParamsTcpSyn": tIPFilterParamsTcpSyn,
       "tIPFilterParamsTcpAck": tIPFilterParamsTcpAck,
       "tIPFilterParamsIcmpCode": tIPFilterParamsIcmpCode,
       "tIPFilterParamsIcmpType": tIPFilterParamsIcmpType,
       "tIPFilterParamsCflowdSample": tIPFilterParamsCflowdSample,
       "tIPFilterParamsCflowdIfSample": tIPFilterParamsCflowdIfSample,
       "tIPFilterParamsForwardNHInterface": tIPFilterParamsForwardNHInterface,
       "tIPFilterParamsIngressHitCount": tIPFilterParamsIngressHitCount,
       "tIPFilterParamsEgressHitCount": tIPFilterParamsEgressHitCount,
       "tIPFilterParamsLogInstantiated": tIPFilterParamsLogInstantiated,
       "tIPFilterParamsForwardRedPlcy": tIPFilterParamsForwardRedPlcy,
       "tIPFilterParamsActiveDest": tIPFilterParamsActiveDest,
       "tIPFilterParamsFwdSvcId": tIPFilterParamsFwdSvcId,
       "tIPFilterParamsFwdSapPortId": tIPFilterParamsFwdSapPortId,
       "tIPFilterParamsFwdSapEncapVal": tIPFilterParamsFwdSapEncapVal,
       "tIPFilterParamsFwdSdpBind": tIPFilterParamsFwdSdpBind,
       "tIPFilterParamsTimeRangeName": tIPFilterParamsTimeRangeName,
       "tIPFilterParamsTimeRangeState": tIPFilterParamsTimeRangeState,
       "tIPFilterParamsRedirectURL": tIPFilterParamsRedirectURL,
       "tIPFilterParamsSrcIpFullMask": tIPFilterParamsSrcIpFullMask,
       "tIPFilterParamsDestIpFullMask": tIPFilterParamsDestIpFullMask,
       "tIPFilterParamsIngrHitByteCount": tIPFilterParamsIngrHitByteCount,
       "tIPFilterParamsEgrHitByteCount": tIPFilterParamsEgrHitByteCount,
       "tIPFilterParamsFwdRtrId": tIPFilterParamsFwdRtrId,
       "tIPFilterParamsSrcRouteOption": tIPFilterParamsSrcRouteOption,
       "tIPFilterParamsSrcIpPrefixList": tIPFilterParamsSrcIpPrefixList,
       "tIPFilterParamsDstIpPrefixList": tIPFilterParamsDstIpPrefixList,
       "tIPFilterParamsPortSelector": tIPFilterParamsPortSelector,
       "tIPFilterParamsSrcPortList": tIPFilterParamsSrcPortList,
       "tIPFilterParamsDstPortList": tIPFilterParamsDstPortList,
       "tIPFilterParamsRdirAllwRadOvrd": tIPFilterParamsRdirAllwRadOvrd,
       "tIPFilterParamsNatPolicyName": tIPFilterParamsNatPolicyName,
       "tIPFilterParamsFwdLsp": tIPFilterParamsFwdLsp,
       "tIPFilterParamsFwdLspRtrId": tIPFilterParamsFwdLspRtrId,
       "tIPFilterParamsIpSelector": tIPFilterParamsIpSelector,
       "tMacFilterTable": tMacFilterTable,
       "tMacFilterEntry": tMacFilterEntry,
       "tMacFilterId": tMacFilterId,
       "tMacFilterRowStatus": tMacFilterRowStatus,
       "tMacFilterScope": tMacFilterScope,
       "tMacFilterDescription": tMacFilterDescription,
       "tMacFilterDefaultAction": tMacFilterDefaultAction,
       "tMacFilterType": tMacFilterType,
       "tMacFilterName": tMacFilterName,
       "tMacFilterParamsTable": tMacFilterParamsTable,
       "tMacFilterParamsEntry": tMacFilterParamsEntry,
       "tMacFilterParamsIndex": tMacFilterParamsIndex,
       "tMacFilterParamsRowStatus": tMacFilterParamsRowStatus,
       "tMacFilterParamsLogId": tMacFilterParamsLogId,
       "tMacFilterParamsDescription": tMacFilterParamsDescription,
       "tMacFilterParamsAction": tMacFilterParamsAction,
       "tMacFilterParamsFrameType": tMacFilterParamsFrameType,
       "tMacFilterParamsSrcMAC": tMacFilterParamsSrcMAC,
       "tMacFilterParamsSrcMACMask": tMacFilterParamsSrcMACMask,
       "tMacFilterParamsDstMAC": tMacFilterParamsDstMAC,
       "tMacFilterParamsDstMACMask": tMacFilterParamsDstMACMask,
       "tMacFilterParamsDot1pValue": tMacFilterParamsDot1pValue,
       "tMacFilterParamsDot1pMask": tMacFilterParamsDot1pMask,
       "tMacFilterParamsEtherType": tMacFilterParamsEtherType,
       "tMacFilterParamsDsap": tMacFilterParamsDsap,
       "tMacFilterParamsDsapMask": tMacFilterParamsDsapMask,
       "tMacFilterParamsSsap": tMacFilterParamsSsap,
       "tMacFilterParamsSsapMask": tMacFilterParamsSsapMask,
       "tMacFilterParamsSnapPid": tMacFilterParamsSnapPid,
       "tMacFilterParamsSnapOui": tMacFilterParamsSnapOui,
       "tMacFilterParamsIngressHitCount": tMacFilterParamsIngressHitCount,
       "tMacFilterParamsEgressHitCount": tMacFilterParamsEgressHitCount,
       "tMacFilterParamsLogInstantiated": tMacFilterParamsLogInstantiated,
       "tMacFilterParamsFwdSvcId": tMacFilterParamsFwdSvcId,
       "tMacFilterParamsFwdSapPortId": tMacFilterParamsFwdSapPortId,
       "tMacFilterParamsFwdSapEncapVal": tMacFilterParamsFwdSapEncapVal,
       "tMacFilterParamsFwdSdpBind": tMacFilterParamsFwdSdpBind,
       "tMacFilterParamsTimeRangeName": tMacFilterParamsTimeRangeName,
       "tMacFilterParamsTimeRangeState": tMacFilterParamsTimeRangeState,
       "tMacFilterParamsRedirectURL": tMacFilterParamsRedirectURL,
       "tMacFilterParamsIngrHitByteCount": tMacFilterParamsIngrHitByteCount,
       "tMacFilterParamsEgrHitByteCount": tMacFilterParamsEgrHitByteCount,
       "tMacFilterParamsLowISID": tMacFilterParamsLowISID,
       "tMacFilterParamsHighISID": tMacFilterParamsHighISID,
       "tMacFilterParamsInnerTagValue": tMacFilterParamsInnerTagValue,
       "tMacFilterParamsInnerTagMask": tMacFilterParamsInnerTagMask,
       "tMacFilterParamsOuterTagValue": tMacFilterParamsOuterTagValue,
       "tMacFilterParamsOuterTagMask": tMacFilterParamsOuterTagMask,
       "tMacFilterParamsEsi": tMacFilterParamsEsi,
       "tMacFilterParamsFwdEsiSvcId": tMacFilterParamsFwdEsiSvcId,
       "tMacFilterParamsPbrDwnActOvr": tMacFilterParamsPbrDwnActOvr,
       "tMacFilterParamsStickyDst": tMacFilterParamsStickyDst,
       "tMacFilterParamsHoldRemain": tMacFilterParamsHoldRemain,
       "tMacFilterParamsDownloadAct": tMacFilterParamsDownloadAct,
       "tMacFilterParamsCollectStats": tMacFilterParamsCollectStats,
       "tFilterLogTable": tFilterLogTable,
       "tFilterLogEntry": tFilterLogEntry,
       "tFilterLogId": tFilterLogId,
       "tFilterLogRowStatus": tFilterLogRowStatus,
       "tFilterLogDestination": tFilterLogDestination,
       "tFilterLogDescription": tFilterLogDescription,
       "tFilterLogMaxNumEntries": tFilterLogMaxNumEntries,
       "tFilterLogSysLogId": tFilterLogSysLogId,
       "tFilterLogFileId": tFilterLogFileId,
       "tFilterLogStopOnFull": tFilterLogStopOnFull,
       "tFilterLogEnabled": tFilterLogEnabled,
       "tFilterLogSummaryEnabled": tFilterLogSummaryEnabled,
       "tFilterLogSummaryCrit1": tFilterLogSummaryCrit1,
       "tFilterLogScalars": tFilterLogScalars,
       "tFilterLogMaxInstances": tFilterLogMaxInstances,
       "tFilterLogInstances": tFilterLogInstances,
       "tFilterLogBindings": tFilterLogBindings,
       "tFilterNotificationObjects": tFilterNotificationObjects,
       "tFilterPBRDropReason": tFilterPBRDropReason,
       "tFilterParmRow": tFilterParmRow,
       "tFilterAlarmDescription": tFilterAlarmDescription,
       "tFilterId": tFilterId,
       "tFilterType": tFilterType,
       "tFilterSubInsSpaceOwner": tFilterSubInsSpaceOwner,
       "tFilterThresholdReached": tFilterThresholdReached,
       "tFltrFlowSpecProblem": tFltrFlowSpecProblem,
       "tFltrFlowSpecProblemDescription": tFltrFlowSpecProblemDescription,
       "tFltrFLowSpecNLRI": tFltrFLowSpecNLRI,
       "tFltrFlowSpecVrtrId": tFltrFlowSpecVrtrId,
       "tFltrPrefixListType": tFltrPrefixListType,
       "tFltrPrefixListName": tFltrPrefixListName,
       "tFltrApplyPathSource": tFltrApplyPathSource,
       "tFltrApplyPathIndex": tFltrApplyPathIndex,
       "tFltrNotifDescription": tFltrNotifDescription,
       "tFltrMdaId": tFltrMdaId,
       "tFilterTimeStampObjects": tFilterTimeStampObjects,
       "tFilterDomainLastChanged": tFilterDomainLastChanged,
       "tFilterRedirectPolicyTable": tFilterRedirectPolicyTable,
       "tFilterRedirectPolicyEntry": tFilterRedirectPolicyEntry,
       "tFilterRedirectPolicy": tFilterRedirectPolicy,
       "tFilterRPRowStatus": tFilterRPRowStatus,
       "tFilterRPDescription": tFilterRPDescription,
       "tFilterRPAdminState": tFilterRPAdminState,
       "tFilterRPActiveDest": tFilterRPActiveDest,
       "tFilterRPVrtrId": tFilterRPVrtrId,
       "tFilterRPActiveDestAddrType": tFilterRPActiveDestAddrType,
       "tFilterRPActiveDestAddr": tFilterRPActiveDestAddr,
       "tFilterRPDstStickiness": tFilterRPDstStickiness,
       "tFilterRPBestDstAddrType": tFilterRPBestDstAddrType,
       "tFilterRPBestDstAddr": tFilterRPBestDstAddr,
       "tFilterRPStickinessHoldRemain": tFilterRPStickinessHoldRemain,
       "tFilterRPNotifyDestChange": tFilterRPNotifyDestChange,
       "tFilterRedirectDestTable": tFilterRedirectDestTable,
       "tFilterRedirectDestEntry": tFilterRedirectDestEntry,
       "tFilterRedirectDest": tFilterRedirectDest,
       "tFilterRDRowStatus": tFilterRDRowStatus,
       "tFilterRDDescription": tFilterRDDescription,
       "tFilterRDAdminPriority": tFilterRDAdminPriority,
       "tFilterRDOperPriority": tFilterRDOperPriority,
       "tFilterRDAdminState": tFilterRDAdminState,
       "tFilterRDOperState": tFilterRDOperState,
       "tFilterRedirectSNMPTestTable": tFilterRedirectSNMPTestTable,
       "tFilterRedirectSNMPTestEntry": tFilterRedirectSNMPTestEntry,
       "tFilterRedirectSNMPTest": tFilterRedirectSNMPTest,
       "tFilterRSTRowStatus": tFilterRSTRowStatus,
       "tFilterRSTOID": tFilterRSTOID,
       "tFilterRSTCommunity": tFilterRSTCommunity,
       "tFilterRSTSNMPVersion": tFilterRSTSNMPVersion,
       "tFilterRSTInterval": tFilterRSTInterval,
       "tFilterRSTTimeout": tFilterRSTTimeout,
       "tFilterRSTDropCount": tFilterRSTDropCount,
       "tFilterRSTHoldDown": tFilterRSTHoldDown,
       "tFilterRSTHoldDownRemain": tFilterRSTHoldDownRemain,
       "tFilterRSTLastActionTime": tFilterRSTLastActionTime,
       "tFilterRSTLastOID": tFilterRSTLastOID,
       "tFilterRSTLastType": tFilterRSTLastType,
       "tFilterRSTLastCounter32Val": tFilterRSTLastCounter32Val,
       "tFilterRSTLastUnsigned32Val": tFilterRSTLastUnsigned32Val,
       "tFilterRSTLastTimeTicksVal": tFilterRSTLastTimeTicksVal,
       "tFilterRSTLastInt32Val": tFilterRSTLastInt32Val,
       "tFilterRSTLastOctetStringVal": tFilterRSTLastOctetStringVal,
       "tFilterRSTLastIpAddressVal": tFilterRSTLastIpAddressVal,
       "tFilterRSTLastOidVal": tFilterRSTLastOidVal,
       "tFilterRSTLastCounter64Val": tFilterRSTLastCounter64Val,
       "tFilterRSTLastOpaqueVal": tFilterRSTLastOpaqueVal,
       "tFilterRSTLastAction": tFilterRSTLastAction,
       "tFilterRSTLastPrioChange": tFilterRSTLastPrioChange,
       "tFilterRSTNextRespIndex": tFilterRSTNextRespIndex,
       "tFilterRedirectSNMPRespTable": tFilterRedirectSNMPRespTable,
       "tFilterRedirectSNMPRespEntry": tFilterRedirectSNMPRespEntry,
       "tFilterRSTRespId": tFilterRSTRespId,
       "tFilterRSTRespRowStatus": tFilterRSTRespRowStatus,
       "tFilterRSTRespAction": tFilterRSTRespAction,
       "tFilterRSTRespPrioChange": tFilterRSTRespPrioChange,
       "tFilterRSTRespOID": tFilterRSTRespOID,
       "tFilterRSTRespType": tFilterRSTRespType,
       "tFilterRSTCounter32Val": tFilterRSTCounter32Val,
       "tFilterRSTUnsigned32Val": tFilterRSTUnsigned32Val,
       "tFilterRSTTimeTicksVal": tFilterRSTTimeTicksVal,
       "tFilterRSTInt32Val": tFilterRSTInt32Val,
       "tFilterRSTOctetStringVal": tFilterRSTOctetStringVal,
       "tFilterRSTIpAddressVal": tFilterRSTIpAddressVal,
       "tFilterRSTOidVal": tFilterRSTOidVal,
       "tFilterRSTCounter64Val": tFilterRSTCounter64Val,
       "tFilterRSTOpaqueVal": tFilterRSTOpaqueVal,
       "tFilterRedirectURLTestTable": tFilterRedirectURLTestTable,
       "tFilterRedirectURLTestEntry": tFilterRedirectURLTestEntry,
       "tFilterRedirectURLTest": tFilterRedirectURLTest,
       "tFilterRUTRowStatus": tFilterRUTRowStatus,
       "tFilterRUTURL": tFilterRUTURL,
       "tFilterRUTHTTPVersion": tFilterRUTHTTPVersion,
       "tFilterRUTInterval": tFilterRUTInterval,
       "tFilterRUTTimeout": tFilterRUTTimeout,
       "tFilterRUTDropCount": tFilterRUTDropCount,
       "tFilterRUTHoldDown": tFilterRUTHoldDown,
       "tFilterRUTHoldDownRemain": tFilterRUTHoldDownRemain,
       "tFilterRUTLastActionTime": tFilterRUTLastActionTime,
       "tFilterRUTLastRetCode": tFilterRUTLastRetCode,
       "tFilterRUTLastAction": tFilterRUTLastAction,
       "tFilterRUTLastPrioChange": tFilterRUTLastPrioChange,
       "tFilterRedirectURLRespTable": tFilterRedirectURLRespTable,
       "tFilterRedirectURLRespEntry": tFilterRedirectURLRespEntry,
       "tFilterRedirectURLLowRespCode": tFilterRedirectURLLowRespCode,
       "tFilterRedirectURLHighRespCode": tFilterRedirectURLHighRespCode,
       "tFilterRUTRespRowStatus": tFilterRUTRespRowStatus,
       "tFilterRUTRespAction": tFilterRUTRespAction,
       "tFilterRUTRespPrioChange": tFilterRUTRespPrioChange,
       "tFilterRedirectPingTestTable": tFilterRedirectPingTestTable,
       "tFilterRedirectPingTestEntry": tFilterRedirectPingTestEntry,
       "tFilterRPTRowStatus": tFilterRPTRowStatus,
       "tFilterRPTInterval": tFilterRPTInterval,
       "tFilterRPTTimeout": tFilterRPTTimeout,
       "tFilterRPTDropCount": tFilterRPTDropCount,
       "tFilterRPTHoldDown": tFilterRPTHoldDown,
       "tFilterRPTHoldDownRemain": tFilterRPTHoldDownRemain,
       "tFilterRPTLastActionTime": tFilterRPTLastActionTime,
       "tFilterRPTLastAction": tFilterRPTLastAction,
       "tAutoIPFilterEntryTable": tAutoIPFilterEntryTable,
       "tAutoIPFilterEntry": tAutoIPFilterEntry,
       "tAutoIPFilterId": tAutoIPFilterId,
       "tAutoIPFilterEntrySourceIpAddr": tAutoIPFilterEntrySourceIpAddr,
       "tAutoIPFilterEntrySourceIpMask": tAutoIPFilterEntrySourceIpMask,
       "tIPv6FilterTable": tIPv6FilterTable,
       "tIPv6FilterEntry": tIPv6FilterEntry,
       "tIPv6FilterId": tIPv6FilterId,
       "tIPv6FilterRowStatus": tIPv6FilterRowStatus,
       "tIPv6FilterScope": tIPv6FilterScope,
       "tIPv6FilterDescription": tIPv6FilterDescription,
       "tIPv6FilterDefaultAction": tIPv6FilterDefaultAction,
       "tIPv6FilterRadiusInsertPt": tIPv6FilterRadiusInsertPt,
       "tIPv6FilterRadiusInsertSize": tIPv6FilterRadiusInsertSize,
       "tIPv6FilterCreditCntrlInsertPt": tIPv6FilterCreditCntrlInsertPt,
       "tIPv6FilterCreditCntrlInsertSize": tIPv6FilterCreditCntrlInsertSize,
       "tIPv6FilterSubInsertHighWmark": tIPv6FilterSubInsertHighWmark,
       "tIPv6FilterSubInsertLowWmark": tIPv6FilterSubInsertLowWmark,
       "tIpv6FilterCreditCntrlNbrInsertd": tIpv6FilterCreditCntrlNbrInsertd,
       "tIpv6FilterRadiusNbrInsertd": tIpv6FilterRadiusNbrInsertd,
       "tIpv6FilterName": tIpv6FilterName,
       "tIPv6FilterHostSharedInsertPt": tIPv6FilterHostSharedInsertPt,
       "tIPv6FilterHostSharedInsertSize": tIPv6FilterHostSharedInsertSize,
       "tIpv6FilterHostSharedNbrInsertd": tIpv6FilterHostSharedNbrInsertd,
       "tIPv6FilterHostSharedHighWmark": tIPv6FilterHostSharedHighWmark,
       "tIPv6FilterHostSharedLowWmark": tIPv6FilterHostSharedLowWmark,
       "tIPv6FilterNbrHostSharedFltrs": tIPv6FilterNbrHostSharedFltrs,
       "tIPv6FilterSharedPccRuleInsrtPt": tIPv6FilterSharedPccRuleInsrtPt,
       "tIPv6FilterSharedPccRuleInsrtSiz": tIPv6FilterSharedPccRuleInsrtSiz,
       "tIPv6FilterSharedPccRuleNbrInsrt": tIPv6FilterSharedPccRuleNbrInsrt,
       "tIPv6FilterChainToSystemFilter": tIPv6FilterChainToSystemFilter,
       "tIPv6FilterType": tIPv6FilterType,
       "tIPv6FilterParamsTable": tIPv6FilterParamsTable,
       "tIPv6FilterParamsEntry": tIPv6FilterParamsEntry,
       "tIPv6FilterParamsIndex": tIPv6FilterParamsIndex,
       "tIPv6FilterParamsRowStatus": tIPv6FilterParamsRowStatus,
       "tIPv6FilterParamsLogId": tIPv6FilterParamsLogId,
       "tIPv6FilterParamsDescription": tIPv6FilterParamsDescription,
       "tIPv6FilterParamsAction": tIPv6FilterParamsAction,
       "tIPv6FilterParamsForwardNH": tIPv6FilterParamsForwardNH,
       "tIPv6FilterParamsForwardNHIndirect": tIPv6FilterParamsForwardNHIndirect,
       "tIPv6FilterParamsRemarkDSCP": tIPv6FilterParamsRemarkDSCP,
       "tIPv6FilterParamsRemarkDSCPMask": tIPv6FilterParamsRemarkDSCPMask,
       "tIPv6FilterParamsRemarkDot1p": tIPv6FilterParamsRemarkDot1p,
       "tIPv6FilterParamsSourceIpAddr": tIPv6FilterParamsSourceIpAddr,
       "tIPv6FilterParamsSourceIpMask": tIPv6FilterParamsSourceIpMask,
       "tIPv6FilterParamsDestinationIpAddr": tIPv6FilterParamsDestinationIpAddr,
       "tIPv6FilterParamsDestinationIpMask": tIPv6FilterParamsDestinationIpMask,
       "tIPv6FilterParamsNextHeader": tIPv6FilterParamsNextHeader,
       "tIPv6FilterParamsSourcePortValue1": tIPv6FilterParamsSourcePortValue1,
       "tIPv6FilterParamsSourcePortValue2": tIPv6FilterParamsSourcePortValue2,
       "tIPv6FilterParamsSourcePortOperator": tIPv6FilterParamsSourcePortOperator,
       "tIPv6FilterParamsDestPortValue1": tIPv6FilterParamsDestPortValue1,
       "tIPv6FilterParamsDestPortValue2": tIPv6FilterParamsDestPortValue2,
       "tIPv6FilterParamsDestPortOperator": tIPv6FilterParamsDestPortOperator,
       "tIPv6FilterParamsDSCP": tIPv6FilterParamsDSCP,
       "tIPv6FilterParamsTcpSyn": tIPv6FilterParamsTcpSyn,
       "tIPv6FilterParamsTcpAck": tIPv6FilterParamsTcpAck,
       "tIPv6FilterParamsIcmpCode": tIPv6FilterParamsIcmpCode,
       "tIPv6FilterParamsIcmpType": tIPv6FilterParamsIcmpType,
       "tIPv6FilterParamsCflowdSample": tIPv6FilterParamsCflowdSample,
       "tIPv6FilterParamsCflowdIfSample": tIPv6FilterParamsCflowdIfSample,
       "tIPv6FilterParamsForwardNHInterface": tIPv6FilterParamsForwardNHInterface,
       "tIPv6FilterParamsIngressHitCount": tIPv6FilterParamsIngressHitCount,
       "tIPv6FilterParamsEgressHitCount": tIPv6FilterParamsEgressHitCount,
       "tIPv6FilterParamsLogInstantiated": tIPv6FilterParamsLogInstantiated,
       "tIPv6FilterParamsForwardRedPlcy": tIPv6FilterParamsForwardRedPlcy,
       "tIPv6FilterParamsActiveDest": tIPv6FilterParamsActiveDest,
       "tIPv6FilterParamsTimeRangeName": tIPv6FilterParamsTimeRangeName,
       "tIPv6FilterParamsTimeRangeState": tIPv6FilterParamsTimeRangeState,
       "tIPv6FilterParamsIngrHitByteCount": tIPv6FilterParamsIngrHitByteCount,
       "tIPv6FilterParamsEgrHitByteCount": tIPv6FilterParamsEgrHitByteCount,
       "tIPv6FilterParamsFwdSvcId": tIPv6FilterParamsFwdSvcId,
       "tIPv6FilterParamsFwdSapPortId": tIPv6FilterParamsFwdSapPortId,
       "tIPv6FilterParamsFwdSapEncapVal": tIPv6FilterParamsFwdSapEncapVal,
       "tIPv6FilterParamsFwdSdpBind": tIPv6FilterParamsFwdSdpBind,
       "tIPv6FilterParamsRedirectURL": tIPv6FilterParamsRedirectURL,
       "tIPv6FilterParamsSrcIpPrefixList": tIPv6FilterParamsSrcIpPrefixList,
       "tIPv6FilterParamsDstIpPrefixList": tIPv6FilterParamsDstIpPrefixList,
       "tIPv6FilterParamsFragment": tIPv6FilterParamsFragment,
       "tIPv6FilterParamsHopByHopOpt": tIPv6FilterParamsHopByHopOpt,
       "tIPv6FilterParamsRoutingType0": tIPv6FilterParamsRoutingType0,
       "tIPv6FilterParamsPortSelector": tIPv6FilterParamsPortSelector,
       "tIPv6FilterParamsSrcPortList": tIPv6FilterParamsSrcPortList,
       "tIPv6FilterParamsDstPortList": tIPv6FilterParamsDstPortList,
       "tIPv6FilterParamsRdirAllwRadOvrd": tIPv6FilterParamsRdirAllwRadOvrd,
       "tIPv6FilterParamsFwdRtrId": tIPv6FilterParamsFwdRtrId,
       "tIPv6FilterParamsSrcIpFullMask": tIPv6FilterParamsSrcIpFullMask,
       "tIPv6FilterParamsDstIpFullMask": tIPv6FilterParamsDstIpFullMask,
       "tIPv6FilterParamsNatPolicyName": tIPv6FilterParamsNatPolicyName,
       "tIPv6FilterParamsFlowLabel": tIPv6FilterParamsFlowLabel,
       "tIPv6FilterParamsFlowLabelMask": tIPv6FilterParamsFlowLabelMask,
       "tIPv6FilterParamsFwdLsp": tIPv6FilterParamsFwdLsp,
       "tIPv6FilterParamsFwdLspRtrId": tIPv6FilterParamsFwdLspRtrId,
       "tIPv6FilterParamsIpSelector": tIPv6FilterParamsIpSelector,
       "tFilterGroupInsertedEntries": tFilterGroupInsertedEntries,
       "tFltrGrpInsrtdEntriesFilterType": tFltrGrpInsrtdEntriesFilterType,
       "tFltrGrpInsrtdEntriesFilterId": tFltrGrpInsrtdEntriesFilterId,
       "tFltrGrpInsrtdEntriesApplication": tFltrGrpInsrtdEntriesApplication,
       "tFltrGrpInsrtdEntriesLocation": tFltrGrpInsrtdEntriesLocation,
       "tFltrGrpInsrtdEntriesResult": tFltrGrpInsrtdEntriesResult,
       "tFltrGrpInsrtdEntriesFeedback": tFltrGrpInsrtdEntriesFeedback,
       "tFltrGrpInsrtdEntriesExecute": tFltrGrpInsrtdEntriesExecute,
       "tDhcpFilterTableLastChanged": tDhcpFilterTableLastChanged,
       "tDhcpFilterTable": tDhcpFilterTable,
       "tDhcpFilterEntry": tDhcpFilterEntry,
       "tDhcpFilterId": tDhcpFilterId,
       "tDhcpFilterRowStatus": tDhcpFilterRowStatus,
       "tDhcpFilterLastChanged": tDhcpFilterLastChanged,
       "tDhcpFilterDescription": tDhcpFilterDescription,
       "tDhcpFilterDefAction": tDhcpFilterDefAction,
       "tDhcpFilterParamsTblLastChanged": tDhcpFilterParamsTblLastChanged,
       "tDhcpFilterParamsTable": tDhcpFilterParamsTable,
       "tDhcpFilterParamsEntry": tDhcpFilterParamsEntry,
       "tDhcpFilterParamsId": tDhcpFilterParamsId,
       "tDhcpFilterParamsRowStatus": tDhcpFilterParamsRowStatus,
       "tDhcpFilterParamsLastChanged": tDhcpFilterParamsLastChanged,
       "tDhcpFilterParamsOptionNumber": tDhcpFilterParamsOptionNumber,
       "tDhcpFilterParamsOptionMatch": tDhcpFilterParamsOptionMatch,
       "tDhcpFilterParamsAction": tDhcpFilterParamsAction,
       "tDhcpFilterParamsOptionValue": tDhcpFilterParamsOptionValue,
       "tMacFilterNameTableLastChgd": tMacFilterNameTableLastChgd,
       "tMacFilterNameTable": tMacFilterNameTable,
       "tMacFilterNameEntry": tMacFilterNameEntry,
       "tMacFilterNameId": tMacFilterNameId,
       "tMacFilterNameRowStatus": tMacFilterNameRowStatus,
       "tMacFilterNameLastChanged": tMacFilterNameLastChanged,
       "tIpFilterNameTableLastChgd": tIpFilterNameTableLastChgd,
       "tIpFilterNameTable": tIpFilterNameTable,
       "tIpFilterNameEntry": tIpFilterNameEntry,
       "tIpFilterNameId": tIpFilterNameId,
       "tIpFilterNameRowStatus": tIpFilterNameRowStatus,
       "tIpFilterNameLastChanged": tIpFilterNameLastChanged,
       "tIpv6FilterNameTableLastChgd": tIpv6FilterNameTableLastChgd,
       "tIpv6FilterNameTable": tIpv6FilterNameTable,
       "tIpv6FilterNameEntry": tIpv6FilterNameEntry,
       "tIpv6FilterNameId": tIpv6FilterNameId,
       "tIpv6FilterNameRowStatus": tIpv6FilterNameRowStatus,
       "tIpv6FilterNameLastChanged": tIpv6FilterNameLastChanged,
       "tFilterLiObjects": tFilterLiObjects,
       "tLiReservedBlockTableLastChanged": tLiReservedBlockTableLastChanged,
       "tLiReservedBlockTable": tLiReservedBlockTable,
       "tLiReservedBlockEntry": tLiReservedBlockEntry,
       "tLiReservedBlockName": tLiReservedBlockName,
       "tLiReservedBlockRowStatus": tLiReservedBlockRowStatus,
       "tLiReservedBlockLastChanged": tLiReservedBlockLastChanged,
       "tLiReservedBlockDescription": tLiReservedBlockDescription,
       "tLiReservedBlockStart": tLiReservedBlockStart,
       "tLiReservedBlockSize": tLiReservedBlockSize,
       "tLiReservedBlockFltrTableLastChg": tLiReservedBlockFltrTableLastChg,
       "tLiReservedBlockFltrTable": tLiReservedBlockFltrTable,
       "tLiReservedBlockFltrEntry": tLiReservedBlockFltrEntry,
       "tLiReservedBlockFltrType": tLiReservedBlockFltrType,
       "tLiReservedBlockFltrIdStart": tLiReservedBlockFltrIdStart,
       "tLiReservedBlockFltrIdEnd": tLiReservedBlockFltrIdEnd,
       "tLiReservedBlockFltrRowStatus": tLiReservedBlockFltrRowStatus,
       "tLiReservedBlockFltrLastChanged": tLiReservedBlockFltrLastChanged,
       "tLiFilterTableLastChanged": tLiFilterTableLastChanged,
       "tLiFilterTable": tLiFilterTable,
       "tLiFilterEntry": tLiFilterEntry,
       "tLiFilterType": tLiFilterType,
       "tLiFilterName": tLiFilterName,
       "tLiFilterRowStatus": tLiFilterRowStatus,
       "tLiFilterLastChanged": tLiFilterLastChanged,
       "tLiFilterDescription": tLiFilterDescription,
       "tLiFilterAssociationTableLastChg": tLiFilterAssociationTableLastChg,
       "tLiFilterAssociationTable": tLiFilterAssociationTable,
       "tLiFilterAssociationEntry": tLiFilterAssociationEntry,
       "tLiFilterAssociationFltrId": tLiFilterAssociationFltrId,
       "tLiFilterAssociationRowStatus": tLiFilterAssociationRowStatus,
       "tLiFilterAssociationLastChg": tLiFilterAssociationLastChg,
       "tLiMacFilterParamsTableLastChg": tLiMacFilterParamsTableLastChg,
       "tLiMacFilterParamsTable": tLiMacFilterParamsTable,
       "tLiMacFilterParamsEntry": tLiMacFilterParamsEntry,
       "tLiMacFilterParamsId": tLiMacFilterParamsId,
       "tLiMacFilterParamsRowStatus": tLiMacFilterParamsRowStatus,
       "tLiMacFilterParamsLastChanged": tLiMacFilterParamsLastChanged,
       "tLiMacFilterParamsDescription": tLiMacFilterParamsDescription,
       "tLiMacFilterParamsFrameType": tLiMacFilterParamsFrameType,
       "tLiMacFilterParamsSrcMAC": tLiMacFilterParamsSrcMAC,
       "tLiMacFilterParamsSrcMACMask": tLiMacFilterParamsSrcMACMask,
       "tLiMacFilterParamsDstMAC": tLiMacFilterParamsDstMAC,
       "tLiMacFilterParamsDstMACMask": tLiMacFilterParamsDstMACMask,
       "tLiMacFilterParamsIngrHitCount": tLiMacFilterParamsIngrHitCount,
       "tLiMacFilterParamsEgrHitCount": tLiMacFilterParamsEgrHitCount,
       "tLiMacFilterParamsIngrHitBytes": tLiMacFilterParamsIngrHitBytes,
       "tLiMacFilterParamsEgrHitBytes": tLiMacFilterParamsEgrHitBytes,
       "tLiIpFilterParamsTableLastChg": tLiIpFilterParamsTableLastChg,
       "tLiIpFilterParamsTable": tLiIpFilterParamsTable,
       "tLiIpFilterParamsEntry": tLiIpFilterParamsEntry,
       "tLiIpFilterParamsId": tLiIpFilterParamsId,
       "tLiIpFilterParamsLastChanged": tLiIpFilterParamsLastChanged,
       "tLiIpFilterParamsRowStatus": tLiIpFilterParamsRowStatus,
       "tLiIpFilterParamsDescription": tLiIpFilterParamsDescription,
       "tLiIpFilterParamsSrcIpAddrType": tLiIpFilterParamsSrcIpAddrType,
       "tLiIpFilterParamsSrcIpAddr": tLiIpFilterParamsSrcIpAddr,
       "tLiIpFilterParamsSrcIpFullMask": tLiIpFilterParamsSrcIpFullMask,
       "tLiIpFilterParamsDstIpAddrType": tLiIpFilterParamsDstIpAddrType,
       "tLiIpFilterParamsDstIpAddr": tLiIpFilterParamsDstIpAddr,
       "tLiIpFilterParamsDstIpFullMask": tLiIpFilterParamsDstIpFullMask,
       "tLiIpFilterParamsProtocolNextHdr": tLiIpFilterParamsProtocolNextHdr,
       "tLiIpFilterParamsSrcPortValue1": tLiIpFilterParamsSrcPortValue1,
       "tLiIpFilterParamsSrcPortValue2": tLiIpFilterParamsSrcPortValue2,
       "tLiIpFilterParamsSrcPortOper": tLiIpFilterParamsSrcPortOper,
       "tLiIpFilterParamsDstPortValue1": tLiIpFilterParamsDstPortValue1,
       "tLiIpFilterParamsDstPortValue2": tLiIpFilterParamsDstPortValue2,
       "tLiIpFilterParamsDstPortOper": tLiIpFilterParamsDstPortOper,
       "tLiIpFilterParamsFragment": tLiIpFilterParamsFragment,
       "tLiIpFilterParamsInfoTable": tLiIpFilterParamsInfoTable,
       "tLiIpFilterParamsInfoEntry": tLiIpFilterParamsInfoEntry,
       "tLiIpFltrParamsInfIngrHitCount": tLiIpFltrParamsInfIngrHitCount,
       "tLiIpFltrParamsInfEgrHitCount": tLiIpFltrParamsInfEgrHitCount,
       "tLiIpFltrParamsInfIngrHitBytes": tLiIpFltrParamsInfIngrHitBytes,
       "tLiIpFltrParamsInfEgrHitBytes": tLiIpFltrParamsInfEgrHitBytes,
       "tLiRsvdBlockFltrAssocTableLChg": tLiRsvdBlockFltrAssocTableLChg,
       "tLiRsvdBlockFltrAssocTable": tLiRsvdBlockFltrAssocTable,
       "tLiRsvdBlockFltrAssocEntry": tLiRsvdBlockFltrAssocEntry,
       "tLiRsvdBlockFltrAssocFltrType": tLiRsvdBlockFltrAssocFltrType,
       "tLiRsvdBlockFltrAssocFltrName": tLiRsvdBlockFltrAssocFltrName,
       "tLiRsvdBlockFltrAssocRowStatus": tLiRsvdBlockFltrAssocRowStatus,
       "tLiRsvdBlockFltrAssocLastChanged": tLiRsvdBlockFltrAssocLastChanged,
       "tLiFltrAssocFltrNameTableLastChg": tLiFltrAssocFltrNameTableLastChg,
       "tLiFltrAssocFltrNameTable": tLiFltrAssocFltrNameTable,
       "tLiFltrAssocFltrNameEntry": tLiFltrAssocFltrNameEntry,
       "tLiFltrAssocFltrName": tLiFltrAssocFltrName,
       "tLiFltrAssocFltrNameRowStatus": tLiFltrAssocFltrNameRowStatus,
       "tLiFltrAssocFltrNameLastChg": tLiFltrAssocFltrNameLastChg,
       "tFilterPrefixListTableLstChng": tFilterPrefixListTableLstChng,
       "tFilterPrefixListTable": tFilterPrefixListTable,
       "tFilterPrefixListEntry": tFilterPrefixListEntry,
       "tFilterPrefixListType": tFilterPrefixListType,
       "tFilterPrefixListName": tFilterPrefixListName,
       "tFilterPrefixListRowStatus": tFilterPrefixListRowStatus,
       "tFilterPrefixListLastChanged": tFilterPrefixListLastChanged,
       "tFilterPrefixListDescription": tFilterPrefixListDescription,
       "tFilterPrefixListEntryTblLstChg": tFilterPrefixListEntryTblLstChg,
       "tFilterPrefixListEntryTable": tFilterPrefixListEntryTable,
       "tFilterPrefixListEntryEntry": tFilterPrefixListEntryEntry,
       "tFilterPrefixListEntryPrefixType": tFilterPrefixListEntryPrefixType,
       "tFilterPrefixListEntryPrefix": tFilterPrefixListEntryPrefix,
       "tFilterPrefixListEntryPrefixLen": tFilterPrefixListEntryPrefixLen,
       "tFilterPrefixListEntryRowStatus": tFilterPrefixListEntryRowStatus,
       "tFilterEmbeddedRefTableLstChg": tFilterEmbeddedRefTableLstChg,
       "tFilterEmbeddedRefTable": tFilterEmbeddedRefTable,
       "tFilterEmbeddedRefTableEntry": tFilterEmbeddedRefTableEntry,
       "tFilterEmbeddedRefFilterType": tFilterEmbeddedRefFilterType,
       "tFilterEmbeddedRefInsertFltrId": tFilterEmbeddedRefInsertFltrId,
       "tFilterEmbeddedRefEmbeddedFltrId": tFilterEmbeddedRefEmbeddedFltrId,
       "tFilterEmbeddedRefOffset": tFilterEmbeddedRefOffset,
       "tFilterEmbeddedRefRowStatus": tFilterEmbeddedRefRowStatus,
       "tFilterEmbeddedRefAdminState": tFilterEmbeddedRefAdminState,
       "tFilterEmbeddedRefOperState": tFilterEmbeddedRefOperState,
       "tFilterEmbeddedRefLastChanged": tFilterEmbeddedRefLastChanged,
       "tFilterPortListTableLstChng": tFilterPortListTableLstChng,
       "tFilterPortListTable": tFilterPortListTable,
       "tFilterPortListEntry": tFilterPortListEntry,
       "tFilterPortListName": tFilterPortListName,
       "tFilterPortListRowStatus": tFilterPortListRowStatus,
       "tFilterPortListLastChanged": tFilterPortListLastChanged,
       "tFilterPortListDescription": tFilterPortListDescription,
       "tFilterPortListEntryTblLstChg": tFilterPortListEntryTblLstChg,
       "tFilterPortListEntryTable": tFilterPortListEntryTable,
       "tFilterPortListEntryEntry": tFilterPortListEntryEntry,
       "tFilterPortListEntryPortLow": tFilterPortListEntryPortLow,
       "tFilterPortListEntryPortHigh": tFilterPortListEntryPortHigh,
       "tFilterPortListEntryRowStatus": tFilterPortListEntryRowStatus,
       "tFilterApplyPathTableLstChng": tFilterApplyPathTableLstChng,
       "tFilterApplyPathTable": tFilterApplyPathTable,
       "tFilterApplyPathEntry": tFilterApplyPathEntry,
       "tFilterApplyPathSource": tFilterApplyPathSource,
       "tFilterApplyPathIndex": tFilterApplyPathIndex,
       "tFilterApplyPathRowStatus": tFilterApplyPathRowStatus,
       "tFilterApplyPathLastChanged": tFilterApplyPathLastChanged,
       "tFilterApplyPathMatch1": tFilterApplyPathMatch1,
       "tFilterApplyPathMatch2": tFilterApplyPathMatch2,
       "tFilterApplyPathVRtrId": tFilterApplyPathVRtrId,
       "tFilterEmbeddedRefInfoTable": tFilterEmbeddedRefInfoTable,
       "tFilterEmbeddedRefInfoEntry": tFilterEmbeddedRefInfoEntry,
       "tFltrEmbedRefInfEntryCnt": tFltrEmbedRefInfEntryCnt,
       "tFltrEmbedRefInfEntryCntInsrtd": tFltrEmbedRefInfEntryCntInsrtd,
       "tFilterEmbeddedEntryRefInfoTable": tFilterEmbeddedEntryRefInfoTable,
       "tFilterEmbeddedEntryRefInfoEntry": tFilterEmbeddedEntryRefInfoEntry,
       "tFltrEmbedEntryFilterType": tFltrEmbedEntryFilterType,
       "tFltrEmbedEntryInsertFltrId": tFltrEmbedEntryInsertFltrId,
       "tFltrEmbedEntryEmbeddedFltrId": tFltrEmbedEntryEmbeddedFltrId,
       "tFltrEmbedEntryEmbeddedEntryId": tFltrEmbedEntryEmbeddedEntryId,
       "tFltrEmbedEntryInsrtEntryId": tFltrEmbedEntryInsrtEntryId,
       "tFltrEmbedEntryRefOperState": tFltrEmbedEntryRefOperState,
       "tIPv6FilterParamsExtTbleLstChgd": tIPv6FilterParamsExtTbleLstChgd,
       "tIPv6FilterParamsExtTable": tIPv6FilterParamsExtTable,
       "tIPv6FilterParamsExtEntry": tIPv6FilterParamsExtEntry,
       "tIPv6FilterParamsExtLastChanged": tIPv6FilterParamsExtLastChanged,
       "tIPv6FilterParamsExtAhExtHdr": tIPv6FilterParamsExtAhExtHdr,
       "tIPv6FilterParamsExtEspExtHdr": tIPv6FilterParamsExtEspExtHdr,
       "tIPv6FilterParamsExtNatType": tIPv6FilterParamsExtNatType,
       "tIPv6FilterParamsExtPktLenVal1": tIPv6FilterParamsExtPktLenVal1,
       "tIPv6FilterParamsExtPktLenVal2": tIPv6FilterParamsExtPktLenVal2,
       "tIPv6FilterParamsExtPktLenOper": tIPv6FilterParamsExtPktLenOper,
       "tIPv6FilterParamsExtHopLimitVal1": tIPv6FilterParamsExtHopLimitVal1,
       "tIPv6FilterParamsExtHopLimitVal2": tIPv6FilterParamsExtHopLimitVal2,
       "tIPv6FilterParamsExtHopLimitOper": tIPv6FilterParamsExtHopLimitOper,
       "tIPv6FilterParamsExtEgressPBR": tIPv6FilterParamsExtEgressPBR,
       "tIPv6FilterParamsExtEsi": tIPv6FilterParamsExtEsi,
       "tIPv6FilterParamsExtFwdEsiSvcId": tIPv6FilterParamsExtFwdEsiSvcId,
       "tIPv6FilterParamsExtFwdEsiVRtrId": tIPv6FilterParamsExtFwdEsiVRtrId,
       "tIPv6FilterParamsExtFwdEsiSFIp": tIPv6FilterParamsExtFwdEsiSFIp,
       "tIPv6FilterParamsExtPbrDwnActOvr": tIPv6FilterParamsExtPbrDwnActOvr,
       "tIPv6FilterParamsExtFwdEsiVasIf": tIPv6FilterParamsExtFwdEsiVasIf,
       "tIPv6FilterParamsExtStickyDst": tIPv6FilterParamsExtStickyDst,
       "tIPv6FilterParamsExtHoldRemain": tIPv6FilterParamsExtHoldRemain,
       "tIPv6FilterParamsExtDownloadAct": tIPv6FilterParamsExtDownloadAct,
       "tIPv6FilterParamsExtTcpFin": tIPv6FilterParamsExtTcpFin,
       "tIPv6FilterParamsExtTcpRst": tIPv6FilterParamsExtTcpRst,
       "tIPv6FilterParamsExtTcpPsh": tIPv6FilterParamsExtTcpPsh,
       "tIPv6FilterParamsExtTcpUrg": tIPv6FilterParamsExtTcpUrg,
       "tIPv6FilterParamsExtTcpEce": tIPv6FilterParamsExtTcpEce,
       "tIPv6FilterParamsExtTcpCwr": tIPv6FilterParamsExtTcpCwr,
       "tIPv6FilterParamsExtTcpNs": tIPv6FilterParamsExtTcpNs,
       "tIPv6FilterParamsExtSrcMac": tIPv6FilterParamsExtSrcMac,
       "tIPv6FilterParamsExtSrcMacMask": tIPv6FilterParamsExtSrcMacMask,
       "tIPv6FilterParamsExtMxPktLenVal1": tIPv6FilterParamsExtMxPktLenVal1,
       "tIPv6FilterParamsExtMxPktLenVal2": tIPv6FilterParamsExtMxPktLenVal2,
       "tIPv6FilterParamsExtMxPktLenOper": tIPv6FilterParamsExtMxPktLenOper,
       "tIPv6FilterParamsExtProtocolList": tIPv6FilterParamsExtProtocolList,
       "tIPv6FilterParamsExtDestClass": tIPv6FilterParamsExtDestClass,
       "tIPv6FilterParamsExtSampleProf": tIPv6FilterParamsExtSampleProf,
       "tIPv6FilterParamsExtCollectStats": tIPv6FilterParamsExtCollectStats,
       "tIPv6FilterParamsExtMxHopLmtVal1": tIPv6FilterParamsExtMxHopLmtVal1,
       "tIPv6FilterParamsExtMxHopLmtVal2": tIPv6FilterParamsExtMxHopLmtVal2,
       "tIPv6FilterParamsExtMxHopLmtOper": tIPv6FilterParamsExtMxHopLmtOper,
       "tFilterEmbedOpenflowTableLstChg": tFilterEmbedOpenflowTableLstChg,
       "tFilterEmbedOpenflowTable": tFilterEmbedOpenflowTable,
       "tFilterEmbedOpenflowEntry": tFilterEmbedOpenflowEntry,
       "tFilterEmbedOpenflowOfsName": tFilterEmbedOpenflowOfsName,
       "tFilterEmbedOpenflowFilterType": tFilterEmbedOpenflowFilterType,
       "tFilterEmbedOpenflowInsertFltrId": tFilterEmbedOpenflowInsertFltrId,
       "tFilterEmbedOpenflowOffset": tFilterEmbedOpenflowOffset,
       "tFilterEmbedOpenflowRowStatus": tFilterEmbedOpenflowRowStatus,
       "tFilterEmbedOpenflowAdminState": tFilterEmbedOpenflowAdminState,
       "tFilterEmbedOpenflowOperState": tFilterEmbedOpenflowOperState,
       "tFilterEmbedOflowSvcContext": tFilterEmbedOflowSvcContext,
       "tFilterEmbedOflowSapContextPort": tFilterEmbedOflowSapContextPort,
       "tFilterEmbedOflowSapContextEncap": tFilterEmbedOflowSapContextEncap,
       "tFilterEmbedOflowContextType": tFilterEmbedOflowContextType,
       "tFilterEmbedOpenflowInfoTable": tFilterEmbedOpenflowInfoTable,
       "tFilterEmbedOpenflowInfoEntry": tFilterEmbedOpenflowInfoEntry,
       "tFltrEmbedOfInfoEntryCnt": tFltrEmbedOfInfoEntryCnt,
       "tFltrEmbedOfInfoEntryCntInsrtd": tFltrEmbedOfInfoEntryCntInsrtd,
       "tFilterOpenflowEntryInfoTable": tFilterOpenflowEntryInfoTable,
       "tFilterOpenflowEntryInfoEntry": tFilterOpenflowEntryInfoEntry,
       "tFltrEmbedOfEntryOfsName": tFltrEmbedOfEntryOfsName,
       "tFltrEmbedOfEntryFilterType": tFltrEmbedOfEntryFilterType,
       "tFltrEmbedOfEntryInsertFltrId": tFltrEmbedOfEntryInsertFltrId,
       "tFltrEmbedOfEntryOfEntryId": tFltrEmbedOfEntryOfEntryId,
       "tFltrEmbedOfEntryInsrtEntryId": tFltrEmbedOfEntryInsrtEntryId,
       "tFltrEmbedOfEntryInsrtEntryState": tFltrEmbedOfEntryInsrtEntryState,
       "tIPFilterParamsExtTbleLstChgd": tIPFilterParamsExtTbleLstChgd,
       "tIPFilterParamsExtTable": tIPFilterParamsExtTable,
       "tIPFilterParamsExtEntry": tIPFilterParamsExtEntry,
       "tIPFilterParamsExtLastChanged": tIPFilterParamsExtLastChanged,
       "tIPFilterParamsExtPktLenVal1": tIPFilterParamsExtPktLenVal1,
       "tIPFilterParamsExtPktLenVal2": tIPFilterParamsExtPktLenVal2,
       "tIPFilterParamsExtPktLenOper": tIPFilterParamsExtPktLenOper,
       "tIPFilterParamsExtTTLVal1": tIPFilterParamsExtTTLVal1,
       "tIPFilterParamsExtTTLVal2": tIPFilterParamsExtTTLVal2,
       "tIPFilterParamsExtTTLOper": tIPFilterParamsExtTTLOper,
       "tIPFilterParamsExtEgressPBR": tIPFilterParamsExtEgressPBR,
       "tIPFilterParamsExtEsi": tIPFilterParamsExtEsi,
       "tIPFilterParamsExtFwdEsiSvcId": tIPFilterParamsExtFwdEsiSvcId,
       "tIPFilterParamsExtFwdEsiVRtrId": tIPFilterParamsExtFwdEsiVRtrId,
       "tIPFilterParamsExtFwdEsiSFIp": tIPFilterParamsExtFwdEsiSFIp,
       "tIPFilterParamsExtPbrDwnActOvr": tIPFilterParamsExtPbrDwnActOvr,
       "tIPFilterParamsExtFwdEsiVasIf": tIPFilterParamsExtFwdEsiVasIf,
       "tIPFilterParamsExtStickyDst": tIPFilterParamsExtStickyDst,
       "tIPFilterParamsExtHoldRemain": tIPFilterParamsExtHoldRemain,
       "tIPFilterParamsExtDownloadAct": tIPFilterParamsExtDownloadAct,
       "tIPFilterParamsExtTcpFin": tIPFilterParamsExtTcpFin,
       "tIPFilterParamsExtTcpRst": tIPFilterParamsExtTcpRst,
       "tIPFilterParamsExtTcpPsh": tIPFilterParamsExtTcpPsh,
       "tIPFilterParamsExtTcpUrg": tIPFilterParamsExtTcpUrg,
       "tIPFilterParamsExtTcpEce": tIPFilterParamsExtTcpEce,
       "tIPFilterParamsExtTcpCwr": tIPFilterParamsExtTcpCwr,
       "tIPFilterParamsExtTcpNs": tIPFilterParamsExtTcpNs,
       "tIPFilterParamsExtSrcMac": tIPFilterParamsExtSrcMac,
       "tIPFilterParamsExtSrcMacMask": tIPFilterParamsExtSrcMacMask,
       "tIPFilterParamsExtMxPktLenVal1": tIPFilterParamsExtMxPktLenVal1,
       "tIPFilterParamsExtMxPktLenVal2": tIPFilterParamsExtMxPktLenVal2,
       "tIPFilterParamsExtMxPktLenOper": tIPFilterParamsExtMxPktLenOper,
       "tIPFilterParamsExtProtocolList": tIPFilterParamsExtProtocolList,
       "tIPFilterParamsExtDestClass": tIPFilterParamsExtDestClass,
       "tIPFilterParamsExtSampleProf": tIPFilterParamsExtSampleProf,
       "tIPFilterParamsExtCollectStats": tIPFilterParamsExtCollectStats,
       "tIPFilterParamsExtMxTTLVal1": tIPFilterParamsExtMxTTLVal1,
       "tIPFilterParamsExtMxTTLVal2": tIPFilterParamsExtMxTTLVal2,
       "tIPFilterParamsExtMxTTLOper": tIPFilterParamsExtMxTTLOper,
       "tFilterRPlcyDstTableLastChg": tFilterRPlcyDstTableLastChg,
       "tFilterRPlcyDstTable": tFilterRPlcyDstTable,
       "tFilterRPlcyDstEntry": tFilterRPlcyDstEntry,
       "tFltrRPDstAddrType": tFltrRPDstAddrType,
       "tFltrRPDstAddr": tFltrRPDstAddr,
       "tFltrRPDstLastChanged": tFltrRPDstLastChanged,
       "tFltrRPDstRowStatus": tFltrRPDstRowStatus,
       "tFltrRPDstAdminState": tFltrRPDstAdminState,
       "tFltrRPDstOperState": tFltrRPDstOperState,
       "tFltrRPDstDescription": tFltrRPDstDescription,
       "tFltrRPDstAdminPriority": tFltrRPDstAdminPriority,
       "tFltrRPDstOperPriority": tFltrRPDstOperPriority,
       "tFilterRPlcySNMPTestTableLastChg": tFilterRPlcySNMPTestTableLastChg,
       "tFilterRPlcySNMPTestTable": tFilterRPlcySNMPTestTable,
       "tFilterRPlcySNMPTestEntry": tFilterRPlcySNMPTestEntry,
       "tFltrRPSnmpTest": tFltrRPSnmpTest,
       "tFltrRPSnmpTLastChanged": tFltrRPSnmpTLastChanged,
       "tFltrRPSnmpTRowStatus": tFltrRPSnmpTRowStatus,
       "tFltrRPSnmpTOID": tFltrRPSnmpTOID,
       "tFltrRPSnmpTCommunity": tFltrRPSnmpTCommunity,
       "tFltrRPSnmpTSnmpVersion": tFltrRPSnmpTSnmpVersion,
       "tFltrRPSnmpTInterval": tFltrRPSnmpTInterval,
       "tFltrRPSnmpTTimeout": tFltrRPSnmpTTimeout,
       "tFltrRPSnmpTDropCount": tFltrRPSnmpTDropCount,
       "tFltrRPSnmpTHoldDown": tFltrRPSnmpTHoldDown,
       "tFltrRPSnmpTHoldDownRemain": tFltrRPSnmpTHoldDownRemain,
       "tFltrRPSnmpTLastActionTime": tFltrRPSnmpTLastActionTime,
       "tFltrRPSnmpTLastOID": tFltrRPSnmpTLastOID,
       "tFltrRPSnmpTLastType": tFltrRPSnmpTLastType,
       "tFltrRPSnmpTLastCounter32Val": tFltrRPSnmpTLastCounter32Val,
       "tFltrRPSnmpTLastUnsigned32Val": tFltrRPSnmpTLastUnsigned32Val,
       "tFltrRPSnmpTLastTimeTicksVal": tFltrRPSnmpTLastTimeTicksVal,
       "tFltrRPSnmpTLastInt32Val": tFltrRPSnmpTLastInt32Val,
       "tFltrRPSnmpTLastOctetStringVal": tFltrRPSnmpTLastOctetStringVal,
       "tFltrRPSnmpTLastIpAddressVal": tFltrRPSnmpTLastIpAddressVal,
       "tFltrRPSnmpTLastOidVal": tFltrRPSnmpTLastOidVal,
       "tFltrRPSnmpTLastCounter64Val": tFltrRPSnmpTLastCounter64Val,
       "tFltrRPSnmpTLastOpaqueVal": tFltrRPSnmpTLastOpaqueVal,
       "tFltrRPSnmpTLastAction": tFltrRPSnmpTLastAction,
       "tFltrRPSnmpTLastPrioChange": tFltrRPSnmpTLastPrioChange,
       "tFltrRPSnmpTNextRespIndex": tFltrRPSnmpTNextRespIndex,
       "tFilterRPlcySNMPRespTableLastChg": tFilterRPlcySNMPRespTableLastChg,
       "tFilterRPlcySNMPRespTable": tFilterRPlcySNMPRespTable,
       "tFilterRPlcySNMPRespEntry": tFilterRPlcySNMPRespEntry,
       "tFltrRPSnmpRspId": tFltrRPSnmpRspId,
       "tFltrRPSnmpRspLastChanged": tFltrRPSnmpRspLastChanged,
       "tFltrRPSnmpRspRowStatus": tFltrRPSnmpRspRowStatus,
       "tFltrRPSnmpRspAction": tFltrRPSnmpRspAction,
       "tFltrRPSnmpRspPrioChange": tFltrRPSnmpRspPrioChange,
       "tFltrRPSnmpRspOID": tFltrRPSnmpRspOID,
       "tFltrRPSnmpRspType": tFltrRPSnmpRspType,
       "tFltrRPSnmpRspCounter32Val": tFltrRPSnmpRspCounter32Val,
       "tFltrRPSnmpRspUnsigned32Val": tFltrRPSnmpRspUnsigned32Val,
       "tFltrRPSnmpRspTimeTicksVal": tFltrRPSnmpRspTimeTicksVal,
       "tFltrRPSnmpRspInt32Val": tFltrRPSnmpRspInt32Val,
       "tFltrRPSnmpRspOctetStringVal": tFltrRPSnmpRspOctetStringVal,
       "tFltrRPSnmpRspIpAddressVal": tFltrRPSnmpRspIpAddressVal,
       "tFltrRPSnmpRspOidVal": tFltrRPSnmpRspOidVal,
       "tFltrRPSnmpRspCounter64Val": tFltrRPSnmpRspCounter64Val,
       "tFltrRPSnmpRspOpaqueVal": tFltrRPSnmpRspOpaqueVal,
       "tFilterRPlcyURLTestTableLastChg": tFilterRPlcyURLTestTableLastChg,
       "tFilterRPlcyURLTestTable": tFilterRPlcyURLTestTable,
       "tFilterRPlcyURLTestEntry": tFilterRPlcyURLTestEntry,
       "tFltrRPUrlTest": tFltrRPUrlTest,
       "tFltrRPUrlTLastChanged": tFltrRPUrlTLastChanged,
       "tFltrRPUrlTRowStatus": tFltrRPUrlTRowStatus,
       "tFltrRPUrlTUrl": tFltrRPUrlTUrl,
       "tFltrRPUrlTHttpVersion": tFltrRPUrlTHttpVersion,
       "tFltrRPUrlTInterval": tFltrRPUrlTInterval,
       "tFltrRPUrlTTimeout": tFltrRPUrlTTimeout,
       "tFltrRPUrlTDropCount": tFltrRPUrlTDropCount,
       "tFltrRPUrlTHoldDown": tFltrRPUrlTHoldDown,
       "tFltrRPUrlTHoldDownRemain": tFltrRPUrlTHoldDownRemain,
       "tFltrRPUrlTLastActionTime": tFltrRPUrlTLastActionTime,
       "tFltrRPUrlTLastRetCode": tFltrRPUrlTLastRetCode,
       "tFltrRPUrlTLastAction": tFltrRPUrlTLastAction,
       "tFltrRPUrlTLastPrioChange": tFltrRPUrlTLastPrioChange,
       "tFilterRPlcyURLRespTableLastChg": tFilterRPlcyURLRespTableLastChg,
       "tFilterRPlcyURLRespTable": tFilterRPlcyURLRespTable,
       "tFilterRPlcyURLRespEntry": tFilterRPlcyURLRespEntry,
       "tFltrRPUrlTRspLowRspCode": tFltrRPUrlTRspLowRspCode,
       "tFltrRPUrlTRspHighRspCode": tFltrRPUrlTRspHighRspCode,
       "tFltrRPUrlTRspLastChanged": tFltrRPUrlTRspLastChanged,
       "tFltrRPUrlTRspRowStatus": tFltrRPUrlTRspRowStatus,
       "tFltrRPUrlTRspAction": tFltrRPUrlTRspAction,
       "tFltrRPUrlTRspPrioChange": tFltrRPUrlTRspPrioChange,
       "tFilterRPlcyPingTestTableLastChg": tFilterRPlcyPingTestTableLastChg,
       "tFilterRPlcyPingTestTable": tFilterRPlcyPingTestTable,
       "tFilterRPlcyPingTestEntry": tFilterRPlcyPingTestEntry,
       "tFltrRPPingTLastChanged": tFltrRPPingTLastChanged,
       "tFltrRPPingTRowStatus": tFltrRPPingTRowStatus,
       "tFltrRPPingTInterval": tFltrRPPingTInterval,
       "tFltrRPPingTTimeout": tFltrRPPingTTimeout,
       "tFltrRPPingTDropCount": tFltrRPPingTDropCount,
       "tFltrRPPingTHoldDown": tFltrRPPingTHoldDown,
       "tFltrRPPingTHoldDownRemain": tFltrRPPingTHoldDownRemain,
       "tFltrRPPingTLastActionTime": tFltrRPPingTLastActionTime,
       "tFltrRPPingTLastAction": tFltrRPPingTLastAction,
       "tFilterRPPingSrcAddressAddrType": tFilterRPPingSrcAddressAddrType,
       "tFilterRPPingSrcAddressAddr": tFilterRPPingSrcAddressAddr,
       "tFilterRPlcyUcastRtTTableLastChg": tFilterRPlcyUcastRtTTableLastChg,
       "tFilterRPlcyUnicastRtTestTable": tFilterRPlcyUnicastRtTestTable,
       "tFilterRPlcyUnicastRtTestEntry": tFilterRPlcyUnicastRtTestEntry,
       "tFltrRPUcastRtTLastChanged": tFltrRPUcastRtTLastChanged,
       "tFltrRPUcastRtTRowStatus": tFltrRPUcastRtTRowStatus,
       "tFltrRPUcastRtTLastActionTime": tFltrRPUcastRtTLastActionTime,
       "tFltrRPUcastRtTLastAction": tFltrRPUcastRtTLastAction,
       "tFilterSystemFilterTableLastChg": tFilterSystemFilterTableLastChg,
       "tFilterSystemFilterTable": tFilterSystemFilterTable,
       "tFilterSystemFilterEntry": tFilterSystemFilterEntry,
       "tFilterSystemFilterType": tFilterSystemFilterType,
       "tFilterSystemFilterId": tFilterSystemFilterId,
       "tFilterSystemFilterLastChanged": tFilterSystemFilterLastChanged,
       "tFilterSystemFilterRowStatus": tFilterSystemFilterRowStatus,
       "tDhcp6FilterTblLastChanged": tDhcp6FilterTblLastChanged,
       "tDhcp6FilterTable": tDhcp6FilterTable,
       "tDhcp6FilterEntry": tDhcp6FilterEntry,
       "tDhcp6FilterId": tDhcp6FilterId,
       "tDhcp6FilterRowStatus": tDhcp6FilterRowStatus,
       "tDhcp6FilterLastChanged": tDhcp6FilterLastChanged,
       "tDhcp6FilterDescription": tDhcp6FilterDescription,
       "tDhcp6FilterDefAction": tDhcp6FilterDefAction,
       "tDhcp6FilterDefActionFlags": tDhcp6FilterDefActionFlags,
       "tDhcp6FilterParamsTblLastChanged": tDhcp6FilterParamsTblLastChanged,
       "tDhcp6FilterParamsTable": tDhcp6FilterParamsTable,
       "tDhcp6FilterParamsEntry": tDhcp6FilterParamsEntry,
       "tDhcp6FilterParamsId": tDhcp6FilterParamsId,
       "tDhcp6FilterParamsRowStatus": tDhcp6FilterParamsRowStatus,
       "tDhcp6FilterParamsLastChanged": tDhcp6FilterParamsLastChanged,
       "tDhcp6FilterParamsOptionNumber": tDhcp6FilterParamsOptionNumber,
       "tDhcp6FilterParamsOptionMatch": tDhcp6FilterParamsOptionMatch,
       "tDhcp6FilterParamsAction": tDhcp6FilterParamsAction,
       "tDhcp6FilterParamsOptionValue": tDhcp6FilterParamsOptionValue,
       "tDhcp6FilterParamsActionFlags": tDhcp6FilterParamsActionFlags,
       "tFilterEmbedFlowspecTableLstChg": tFilterEmbedFlowspecTableLstChg,
       "tFilterEmbedFlowspecTable": tFilterEmbedFlowspecTable,
       "tFilterEmbedFlowspecEntry": tFilterEmbedFlowspecEntry,
       "tFilterEmbedFlowspecFilterType": tFilterEmbedFlowspecFilterType,
       "tFilterEmbedFlowspecInsertFltrId": tFilterEmbedFlowspecInsertFltrId,
       "tFilterEmbedFlowspecOffset": tFilterEmbedFlowspecOffset,
       "tFilterEmbedFlowspecRowStatus": tFilterEmbedFlowspecRowStatus,
       "tFilterEmbedFlowspecLastChanged": tFilterEmbedFlowspecLastChanged,
       "tFilterEmbedFlowspecRtrId": tFilterEmbedFlowspecRtrId,
       "tFilterEmbedFlowspecAdminState": tFilterEmbedFlowspecAdminState,
       "tFilterEmbedFlowspecOperState": tFilterEmbedFlowspecOperState,
       "tFilterEmbedFlowspecGroupId": tFilterEmbedFlowspecGroupId,
       "tFltrEmbFlowspecInfoTable": tFltrEmbFlowspecInfoTable,
       "tFltrEmbFlowspecInfoEntry": tFltrEmbFlowspecInfoEntry,
       "tFltrEmbFlowSpecInfoFltrId": tFltrEmbFlowSpecInfoFltrId,
       "tFltrEmbFlowSpecInfoEntryCnt": tFltrEmbFlowSpecInfoEntryCnt,
       "tFltrEmbFlowSpecInfoEntryCntIns": tFltrEmbFlowSpecInfoEntryCntIns,
       "tFltrEmbFlowspecEntryInfoTable": tFltrEmbFlowspecEntryInfoTable,
       "tFltrEmbFlowspecEntryInfoEntry": tFltrEmbFlowspecEntryInfoEntry,
       "tFltrEmbFlowspecEntryId": tFltrEmbFlowspecEntryId,
       "tFltrEmbFlowspecEntryInsEntryId": tFltrEmbFlowspecEntryInsEntryId,
       "tFltrEmbFlowspecEntryOperState": tFltrEmbFlowspecEntryOperState,
       "tFilterEmbedVsdTableLstChg": tFilterEmbedVsdTableLstChg,
       "tFilterEmbedVsdTable": tFilterEmbedVsdTable,
       "tFilterEmbedVsdEntry": tFilterEmbedVsdEntry,
       "tFilterEmbedVsdFilterType": tFilterEmbedVsdFilterType,
       "tFilterEmbedVsdInsertFltrId": tFilterEmbedVsdInsertFltrId,
       "tFilterEmbedVsdEmbeddedFltrId": tFilterEmbedVsdEmbeddedFltrId,
       "tFilterEmbedVsdOffset": tFilterEmbedVsdOffset,
       "tFilterEmbedVsdRowStatus": tFilterEmbedVsdRowStatus,
       "tFilterEmbedVsdLastChanged": tFilterEmbedVsdLastChanged,
       "tFilterEmbedVsdAdminState": tFilterEmbedVsdAdminState,
       "tFilterEmbedVsdOperState": tFilterEmbedVsdOperState,
       "tFilterEmbedVsdInfoTable": tFilterEmbedVsdInfoTable,
       "tFilterEmbedVsdInfoEntry": tFilterEmbedVsdInfoEntry,
       "tFltrEmbedVsdInfoEntryCnt": tFltrEmbedVsdInfoEntryCnt,
       "tFltrEmbedVsdInfoEntryCntInsrtd": tFltrEmbedVsdInfoEntryCntInsrtd,
       "tFilterEmbedVsdEntryInfoTable": tFilterEmbedVsdEntryInfoTable,
       "tFilterEmbedVsdEntryInfoEntry": tFilterEmbedVsdEntryInfoEntry,
       "tFilterEmbedVsdEntryId": tFilterEmbedVsdEntryId,
       "tFilterEmbedVsdEntryInsrtEntryId": tFilterEmbedVsdEntryInsrtEntryId,
       "tFilterEmbedVsdEntryOperState": tFilterEmbedVsdEntryOperState,
       "tMacFltrEntryActionTblLChg": tMacFltrEntryActionTblLChg,
       "tMacFltrEntryActionTable": tMacFltrEntryActionTable,
       "tMacFltrEntryActionEntry": tMacFltrEntryActionEntry,
       "tMacFltrEntryActActionId": tMacFltrEntryActActionId,
       "tMacFltrEntryActLastChanged": tMacFltrEntryActLastChanged,
       "tMacFltrEntryActRowStatus": tMacFltrEntryActRowStatus,
       "tMacFltrEntryActAction": tMacFltrEntryActAction,
       "tMacFltrEntryActFwdSapPortId": tMacFltrEntryActFwdSapPortId,
       "tMacFltrEntryActFwdSapEncapVal": tMacFltrEntryActFwdSapEncapVal,
       "tMacFltrEntryActFwdSdpBind": tMacFltrEntryActFwdSdpBind,
       "tMacFltrEntryActRedirectURL": tMacFltrEntryActRedirectURL,
       "tMacFltrEntryActEsi": tMacFltrEntryActEsi,
       "tMacFltrEntryActFwdEsiSvcId": tMacFltrEntryActFwdEsiSvcId,
       "tMacFltrEntryActRateLimit": tMacFltrEntryActRateLimit,
       "tMacFltrEntryActPbrTargetStatus": tMacFltrEntryActPbrTargetStatus,
       "tMacFltrEntryActFcName": tMacFltrEntryActFcName,
       "tIPvXFltrEntryActionTblLChg": tIPvXFltrEntryActionTblLChg,
       "tIPvXFltrEntryActionTable": tIPvXFltrEntryActionTable,
       "tIPvXFltrEntryActionEntry": tIPvXFltrEntryActionEntry,
       "tIPvXFltrEntryActFltrType": tIPvXFltrEntryActFltrType,
       "tIPvXFltrEntryActFltrId": tIPvXFltrEntryActFltrId,
       "tIPvXFltrEntryActEntryId": tIPvXFltrEntryActEntryId,
       "tIPvXFltrEntryActActionId": tIPvXFltrEntryActActionId,
       "tIPvXFltrEntryActLastChanged": tIPvXFltrEntryActLastChanged,
       "tIPvXFltrEntryActRowStatus": tIPvXFltrEntryActRowStatus,
       "tIPvXFltrEntryActAction": tIPvXFltrEntryActAction,
       "tIPvXFltrEntryActFwdNHIpAddrType": tIPvXFltrEntryActFwdNHIpAddrType,
       "tIPvXFltrEntryActFwdNHIpAddr": tIPvXFltrEntryActFwdNHIpAddr,
       "tIPvXFltrEntryActFwdNHIndirect": tIPvXFltrEntryActFwdNHIndirect,
       "tIPvXFltrEntryActFwdNHInterface": tIPvXFltrEntryActFwdNHInterface,
       "tIPvXFltrEntryActFwdRedPlcy": tIPvXFltrEntryActFwdRedPlcy,
       "tIPvXFltrEntryActFwdSapPortId": tIPvXFltrEntryActFwdSapPortId,
       "tIPvXFltrEntryActFwdSapEncapVal": tIPvXFltrEntryActFwdSapEncapVal,
       "tIPvXFltrEntryActFwdSdpBind": tIPvXFltrEntryActFwdSdpBind,
       "tIPvXFltrEntryActRedirectURL": tIPvXFltrEntryActRedirectURL,
       "tIPvXFltrEntryActRdirAllwRadOvr": tIPvXFltrEntryActRdirAllwRadOvr,
       "tIPvXFltrEntryActFwdRtrId": tIPvXFltrEntryActFwdRtrId,
       "tIPvXFltrEntryActNatPolicyName": tIPvXFltrEntryActNatPolicyName,
       "tIPvXFltrEntryActNatType": tIPvXFltrEntryActNatType,
       "tIPvXFltrEntryActFwdLsp": tIPvXFltrEntryActFwdLsp,
       "tIPvXFltrEntryActFwdLspRtrId": tIPvXFltrEntryActFwdLspRtrId,
       "tIPvXFltrEntryActPktLenVal1": tIPvXFltrEntryActPktLenVal1,
       "tIPvXFltrEntryActPktLenVal2": tIPvXFltrEntryActPktLenVal2,
       "tIPvXFltrEntryActPktLenOper": tIPvXFltrEntryActPktLenOper,
       "tIPvXFltrEntryActTTLVal1": tIPvXFltrEntryActTTLVal1,
       "tIPvXFltrEntryActTTLVal2": tIPvXFltrEntryActTTLVal2,
       "tIPvXFltrEntryActTTLOper": tIPvXFltrEntryActTTLOper,
       "tIPvXFltrEntryActEsi": tIPvXFltrEntryActEsi,
       "tIPvXFltrEntryActFwdEsiSvcId": tIPvXFltrEntryActFwdEsiSvcId,
       "tIPvXFltrEntryActFwdEsiVRtrId": tIPvXFltrEntryActFwdEsiVRtrId,
       "tIPvXFltrEntryActFwdEsiSFIpType": tIPvXFltrEntryActFwdEsiSFIpType,
       "tIPvXFltrEntryActFwdEsiSFIp": tIPvXFltrEntryActFwdEsiSFIp,
       "tIPvXFltrEntryActFwdEsiVasIf": tIPvXFltrEntryActFwdEsiVasIf,
       "tIPvXFltrEntryActRateLimit": tIPvXFltrEntryActRateLimit,
       "tIPvXFltrEntryActPbrTargetStatus": tIPvXFltrEntryActPbrTargetStatus,
       "tIPvXFltrEntryActRemarkDSCP": tIPvXFltrEntryActRemarkDSCP,
       "tIPvXFltrEntryActActionExt": tIPvXFltrEntryActActionExt,
       "tIPvXFltrEntryActFwdVprnTgtBgNHT": tIPvXFltrEntryActFwdVprnTgtBgNHT,
       "tIPvXFltrEntryActFwdVprnTgtBgNH": tIPvXFltrEntryActFwdVprnTgtBgNH,
       "tIPvXFltrEntryActFwdVprnTgtRtrId": tIPvXFltrEntryActFwdVprnTgtRtrId,
       "tIPvXFltrEntryActFwdVprnTgtAdPxT": tIPvXFltrEntryActFwdVprnTgtAdPxT,
       "tIPvXFltrEntryActFwdVprnTgtAdPx": tIPvXFltrEntryActFwdVprnTgtAdPx,
       "tIPvXFltrEntryActFwdVprnTgtAdPxL": tIPvXFltrEntryActFwdVprnTgtAdPxL,
       "tIPvXFltrEntryActFwdVprnTgtLspId": tIPvXFltrEntryActFwdVprnTgtLspId,
       "tIPvXFltrEntryActFwdBondingConn": tIPvXFltrEntryActFwdBondingConn,
       "tIPvXFltrEntryActFcName": tIPvXFltrEntryActFcName,
       "tIPvXFltrEntryActFwdGreTun": tIPvXFltrEntryActFwdGreTun,
       "tIPvXFltrEntryActCondExpression": tIPvXFltrEntryActCondExpression,
       "tIPvXFltrEntryActCondExpMask": tIPvXFltrEntryActCondExpMask,
       "tIPvXFltrEntryActCondOffsetType": tIPvXFltrEntryActCondOffsetType,
       "tIPvXFltrEntryActCondOffsetVal": tIPvXFltrEntryActCondOffsetVal,
       "tIPvXFltrFwdMplsPlcyEndptAddrTp": tIPvXFltrFwdMplsPlcyEndptAddrTp,
       "tIPvXFltrFwdMplsPlcyEndptAddr": tIPvXFltrFwdMplsPlcyEndptAddr,
       "tIPvXFltrFwdSrtePlcyEndptAddrTp": tIPvXFltrFwdSrtePlcyEndptAddrTp,
       "tIPvXFltrFwdSrtePlcyEndptAddr": tIPvXFltrFwdSrtePlcyEndptAddr,
       "tIPvXFltrFwdSrtePlcyColor": tIPvXFltrFwdSrtePlcyColor,
       "tIPvXFltrActL2AwareNatBypass": tIPvXFltrActL2AwareNatBypass,
       "tFltrEntryStatTable": tFltrEntryStatTable,
       "tFltrEntryStatEntry": tFltrEntryStatEntry,
       "tFltrEntryStatFltrType": tFltrEntryStatFltrType,
       "tFltrEntryStatFltrId": tFltrEntryStatFltrId,
       "tFltrEntryStatFltrEntryId": tFltrEntryStatFltrEntryId,
       "tFltrEntryStatIngHitCnt": tFltrEntryStatIngHitCnt,
       "tFltrEntryStatIngHitCntB": tFltrEntryStatIngHitCntB,
       "tFltrEntryStatEgrHitCnt": tFltrEntryStatEgrHitCnt,
       "tFltrEntryStatEgrHitCntB": tFltrEntryStatEgrHitCntB,
       "tFltrEntryStatRateLmtIngHitCnt": tFltrEntryStatRateLmtIngHitCnt,
       "tFltrEntryStatRateLmtIngHitCntB": tFltrEntryStatRateLmtIngHitCntB,
       "tFltrEntryStatRateLmtIngDrop": tFltrEntryStatRateLmtIngDrop,
       "tFltrEntryStatRateLmtIngDropB": tFltrEntryStatRateLmtIngDropB,
       "tFltrEntryStatRateLmtIngFwd": tFltrEntryStatRateLmtIngFwd,
       "tFltrEntryStatRateLmtIngFwdB": tFltrEntryStatRateLmtIngFwdB,
       "tFltrEntryStatRateLmtEgrHitCnt": tFltrEntryStatRateLmtEgrHitCnt,
       "tFltrEntryStatRateLmtEgrHitCntB": tFltrEntryStatRateLmtEgrHitCntB,
       "tFltrEntryStatRateLmtEgrDrop": tFltrEntryStatRateLmtEgrDrop,
       "tFltrEntryStatRateLmtEgrDropB": tFltrEntryStatRateLmtEgrDropB,
       "tFltrEntryStatRateLmtEgrFwd": tFltrEntryStatRateLmtEgrFwd,
       "tFltrEntryStatRateLmtEgrFwdB": tFltrEntryStatRateLmtEgrFwdB,
       "tFltrPrefListInfoTable": tFltrPrefListInfoTable,
       "tFltrPrefListInfoEntry": tFltrPrefListInfoEntry,
       "tFltrPrefListInfoPrefixSrc": tFltrPrefListInfoPrefixSrc,
       "tFltrPrefListInfoPrefixSrcIndex": tFltrPrefListInfoPrefixSrcIndex,
       "tFltrPrefListInfoPrefixType": tFltrPrefListInfoPrefixType,
       "tFltrPrefListInfoPrefix": tFltrPrefListInfoPrefix,
       "tFltrPrefListInfoPrefixLen": tFltrPrefListInfoPrefixLen,
       "tFltrPrefListInfoPrefixOwner": tFltrPrefListInfoPrefixOwner,
       "tFltrPrefListInfoPrefixProg": tFltrPrefListInfoPrefixProg,
       "tFilterEmbFlowspecEntryInfoTable": tFilterEmbFlowspecEntryInfoTable,
       "tFilterEmbFlowspecEntryInfoEntry": tFilterEmbFlowspecEntryInfoEntry,
       "tFilterEmbedFlowspecEmbFltrId": tFilterEmbedFlowspecEmbFltrId,
       "tFilterEmbedFlowspecEmbEntryId": tFilterEmbedFlowspecEmbEntryId,
       "tFilterEmbedFlowspecInsEntryId": tFilterEmbedFlowspecInsEntryId,
       "tFilterEmbedFlowspecEntryOpState": tFilterEmbedFlowspecEntryOpState,
       "tFilterRPlcyBindingTableLastChg": tFilterRPlcyBindingTableLastChg,
       "tFilterRPlcyBindingTable": tFilterRPlcyBindingTable,
       "tFilterRPlcyBindingEntry": tFilterRPlcyBindingEntry,
       "tFilterRPlcyBindingName": tFilterRPlcyBindingName,
       "tFilterRPlcyBindingLastChange": tFilterRPlcyBindingLastChange,
       "tFilterRPlcyBindingRowStatus": tFilterRPlcyBindingRowStatus,
       "tFilterRPlcyBindingOperator": tFilterRPlcyBindingOperator,
       "tFilterRPlcyBindingOperState": tFilterRPlcyBindingOperState,
       "tFilterRPlcyBindingDestTableLCh": tFilterRPlcyBindingDestTableLCh,
       "tFilterRPlcyBindingDestTable": tFilterRPlcyBindingDestTable,
       "tFilterRPlcyBindingDestEntry": tFilterRPlcyBindingDestEntry,
       "tFilterRPlcyBindingDestRowStatus": tFilterRPlcyBindingDestRowStatus,
       "tFilterRPlcyBindingDestOperState": tFilterRPlcyBindingDestOperState,
       "tFltrGreTunTempTableLastChg": tFltrGreTunTempTableLastChg,
       "tFltrGreTunTempTable": tFltrGreTunTempTable,
       "tFltrGreTunTempEntry": tFltrGreTunTempEntry,
       "tFltrGreTunTempName": tFltrGreTunTempName,
       "tFltrGreTunTempRowStatus": tFltrGreTunTempRowStatus,
       "tFltrGreTunTempLastChanged": tFltrGreTunTempLastChanged,
       "tFltrGreTunTempDescription": tFltrGreTunTempDescription,
       "tFltrGreTunTempIpv4SrcAddr": tFltrGreTunTempIpv4SrcAddr,
       "tFltrGreTunTempIpv4GreKeyIfIndex": tFltrGreTunTempIpv4GreKeyIfIndex,
       "tFltrGreTunTempIpv4SkipTllDecr": tFltrGreTunTempIpv4SkipTllDecr,
       "tFltrGreTunTempIpv4DstTblLstChg": tFltrGreTunTempIpv4DstTblLstChg,
       "tFltrGreTunTempIpv4DstTable": tFltrGreTunTempIpv4DstTable,
       "tFltrGreTunTempIpv4DstEntry": tFltrGreTunTempIpv4DstEntry,
       "tFltrGreTunTempIpv4DstAddr": tFltrGreTunTempIpv4DstAddr,
       "tFltrGreTunTempIpv4DstRowStatus": tFltrGreTunTempIpv4DstRowStatus,
       "tFltrGreTunTempIpv4DstLstChg": tFltrGreTunTempIpv4DstLstChg,
       "tFltrPrefListPrefExclTblLstChg": tFltrPrefListPrefExclTblLstChg,
       "tFltrPrefListPrefExclTable": tFltrPrefListPrefExclTable,
       "tFltrPrefListPrefExclEntry": tFltrPrefListPrefExclEntry,
       "tFltrPrefListPrefExclPrefType": tFltrPrefListPrefExclPrefType,
       "tFltrPrefListPrefExclPref": tFltrPrefListPrefExclPref,
       "tFltrPrefListPrefExclPrefLen": tFltrPrefListPrefExclPrefLen,
       "tFltrPrefListPrefExclRowStatus": tFltrPrefListPrefExclRowStatus,
       "tFltrPrefListPrefExclLastChg": tFltrPrefListPrefExclLastChg,
       "fltrMdAutoIdGroup": fltrMdAutoIdGroup,
       "fltrMdAutoIdFilterRangeStart": fltrMdAutoIdFilterRangeStart,
       "fltrMdAutoIdFilterRangeEnd": fltrMdAutoIdFilterRangeEnd,
       "fltrMdAutoIdIPv4FilterCount": fltrMdAutoIdIPv4FilterCount,
       "fltrMdAutoIdIPv6FilterCount": fltrMdAutoIdIPv6FilterCount,
       "fltrMdAutoIdMacFilterCount": fltrMdAutoIdMacFilterCount,
       "fltrMdAutoIdIPv4ExceptionCount": fltrMdAutoIdIPv4ExceptionCount,
       "fltrMdAutoIdIPv6ExceptionCount": fltrMdAutoIdIPv6ExceptionCount,
       "tIPv6ExceptionTable": tIPv6ExceptionTable,
       "tIPv6ExceptionEntry": tIPv6ExceptionEntry,
       "tIPv6ExceptionId": tIPv6ExceptionId,
       "tIPv6ExceptionRowStatus": tIPv6ExceptionRowStatus,
       "tIPv6ExceptionDescription": tIPv6ExceptionDescription,
       "tIPv6ExceptionName": tIPv6ExceptionName,
       "tIPv6ExceptionNameTable": tIPv6ExceptionNameTable,
       "tIPv6ExceptionNameEntry": tIPv6ExceptionNameEntry,
       "tIPv6ExceptionNameId": tIPv6ExceptionNameId,
       "tIPv6ExceptionParamsTable": tIPv6ExceptionParamsTable,
       "tIPv6ExceptionParamsEntry": tIPv6ExceptionParamsEntry,
       "tIPv6ExcParamsIndex": tIPv6ExcParamsIndex,
       "tIPv6ExcParamsRowStatus": tIPv6ExcParamsRowStatus,
       "tIPv6ExcParamsDescription": tIPv6ExcParamsDescription,
       "tIPv6ExcParamsNextHeader": tIPv6ExcParamsNextHeader,
       "tIPv6ExcParamsSrcIpAddr": tIPv6ExcParamsSrcIpAddr,
       "tIPv6ExcParamsSrcIpMask": tIPv6ExcParamsSrcIpMask,
       "tIPv6ExcParamsSrcIpFullMask": tIPv6ExcParamsSrcIpFullMask,
       "tIPv6ExcParamsSrcIpPrefixList": tIPv6ExcParamsSrcIpPrefixList,
       "tIPv6ExcParamsDstIpAddr": tIPv6ExcParamsDstIpAddr,
       "tIPv6ExcParamsDstIpMask": tIPv6ExcParamsDstIpMask,
       "tIPv6ExcParamsDstIpFullMask": tIPv6ExcParamsDstIpFullMask,
       "tIPv6ExcParamsDstIpPrefixList": tIPv6ExcParamsDstIpPrefixList,
       "tIPv6ExcParamsSourcePortValue1": tIPv6ExcParamsSourcePortValue1,
       "tIPv6ExcParamsSourcePortValue2": tIPv6ExcParamsSourcePortValue2,
       "tIPv6ExcParamsSourcePortOperator": tIPv6ExcParamsSourcePortOperator,
       "tIPv6ExcParamsSourcePortList": tIPv6ExcParamsSourcePortList,
       "tIPv6ExcParamsDestPortValue1": tIPv6ExcParamsDestPortValue1,
       "tIPv6ExcParamsDestPortValue2": tIPv6ExcParamsDestPortValue2,
       "tIPv6ExcParamsDestPortOperator": tIPv6ExcParamsDestPortOperator,
       "tIPv6ExcParamsDestPortList": tIPv6ExcParamsDestPortList,
       "tIPv6ExcParamsPortSelector": tIPv6ExcParamsPortSelector,
       "tIPv6ExcParamsIcmpCode": tIPv6ExcParamsIcmpCode,
       "tIPv6ExcParamsIcmpType": tIPv6ExcParamsIcmpType,
       "tIPv6ExcParamsIngressHitCount": tIPv6ExcParamsIngressHitCount,
       "tIPv6ExcParamsEgressHitCount": tIPv6ExcParamsEgressHitCount,
       "tIPv6ExcParamsIngrHitByteCount": tIPv6ExcParamsIngrHitByteCount,
       "tIPv6ExcParamsEgrHitByteCount": tIPv6ExcParamsEgrHitByteCount,
       "tFltrProtocolListTableLstChng": tFltrProtocolListTableLstChng,
       "tFltrProtocolListTable": tFltrProtocolListTable,
       "tFltrProtocolListEntry": tFltrProtocolListEntry,
       "tFltrProtocolListName": tFltrProtocolListName,
       "tFltrProtocolListRowStatus": tFltrProtocolListRowStatus,
       "tFltrProtocolListLastChanged": tFltrProtocolListLastChanged,
       "tFltrProtocolListDescription": tFltrProtocolListDescription,
       "tFltrProtocolListItemTblLstChg": tFltrProtocolListItemTblLstChg,
       "tFltrProtocolListItemTable": tFltrProtocolListItemTable,
       "tFltrProtocolListItemEntry": tFltrProtocolListItemEntry,
       "tFltrProtocolListItemProtocol": tFltrProtocolListItemProtocol,
       "tFltrProtocolListItemRowStatus": tFltrProtocolListItemRowStatus,
       "tFilterNotificationsPrefix": tFilterNotificationsPrefix,
       "tFilterNotifications": tFilterNotifications,
       "tIPFilterPBRPacketsDrop": tIPFilterPBRPacketsDrop,
       "tFilterEntryActivationFailed": tFilterEntryActivationFailed,
       "tFilterEntryActivationRestored": tFilterEntryActivationRestored,
       "tFilterSubInsSpaceAlarmRaised": tFilterSubInsSpaceAlarmRaised,
       "tFilterSubInsSpaceAlarmCleared": tFilterSubInsSpaceAlarmCleared,
       "tFilterSubInsFltrEntryDropped": tFilterSubInsFltrEntryDropped,
       "tFilterBgpFlowSpecProblem": tFilterBgpFlowSpecProblem,
       "tFilterApplyPathProblem": tFilterApplyPathProblem,
       "tFilterRadSharedFltrAlarmRaised": tFilterRadSharedFltrAlarmRaised,
       "tFilterRadSharedFltrAlarmClear": tFilterRadSharedFltrAlarmClear,
       "tFilterEmbeddingOperStateChange": tFilterEmbeddingOperStateChange,
       "tFilterEmbedOpenflowOperStateChg": tFilterEmbedOpenflowOperStateChg,
       "tFilterTmsEvent": tFilterTmsEvent,
       "tFilterEmbedFlowspecOperStateChg": tFilterEmbedFlowspecOperStateChg,
       "tFilterEmbedVsdOperStateChg": tFilterEmbedVsdOperStateChg,
       "tFilterRPActiveDestChangeEvent": tFilterRPActiveDestChangeEvent,
       "tFltrLiRsvdBlockRangeChangeEvent": tFltrLiRsvdBlockRangeChangeEvent}
)
