# SNMP MIB module (TIMETRA-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\TIMETRA-TC-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:14:12 2025
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

(InetAddress,
 InetAddressIPv6,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv6",
    "InetAddressPrefixLength",
    "InetAddressType")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(timetraModules,) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraModules")


# MODULE-IDENTITY

timetraTCMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 2)
)
if mibBuilder.loadTexts:
    timetraTCMIBModule.setRevisions(
        ("2017-01-01 00:00",
         "2016-01-01 00:00",
         "2015-01-01 00:00",
         "2014-01-01 00:00",
         "2011-02-01 00:00",
         "2009-02-28 00:00",
         "2008-07-01 00:00",
         "2008-01-01 00:00",
         "2007-01-01 00:00",
         "2006-03-23 00:00",
         "2005-08-31 00:00",
         "2005-01-24 00:00",
         "2004-01-15 00:00",
         "2003-08-15 00:00",
         "2003-01-20 00:00",
         "2001-05-29 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxFPNumber(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )



class TmnxFPNumberOrZero(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 12),
    )



class InterfaceIndex(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"


class TmnxPortID(TextualConvention, Unsigned32):
    status = "current"


class TmnxEncapVal(TextualConvention, Unsigned32):
    status = "current"


class QTag(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )



class QTagOrZero(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )



class QTagFullRange(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )



class QTagFullRangeOrNone(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 4095),
    )



class TmnxSapAASubScope(TextualConvention, Integer32):
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
          ("subscriber", 1),
          ("mac", 2))
    )



class TmnxStrSapId(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class IpAddressPrefixLength(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )



class TmnxActionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doAction", 1),
          ("notApplicable", 2))
    )



class TmnxAdminState(TextualConvention, Integer32):
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
        *(("noop", 1),
          ("inService", 2),
          ("outOfService", 3))
    )



class TmnxOperState(TextualConvention, Integer32):
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
        *(("unknown", 1),
          ("inService", 2),
          ("outOfService", 3),
          ("transition", 4))
    )



class TmnxStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )



class TmnxEnabledDisabledAdminState(TextualConvention, Integer32):
    status = "current"
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



class TmnxEnabledDisabled(TextualConvention, Integer32):
    status = "current"
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



class TmnxEnabledDisabledOrNA(TextualConvention, Integer32):
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
        *(("enabled", 1),
          ("disabled", 2),
          ("notApplicable", 3))
    )



class TmnxEnabledDisabledOrInherit(TextualConvention, Integer32):
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
        *(("enabled", 1),
          ("disabled", 2),
          ("inherit", 3))
    )



class TmnxTimeInterval(TextualConvention, Unsigned32):
    status = "current"


class TNamedItem(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class TNamedItemOrEmpty(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 32),
    )



class TLNamedItem(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )



class TLNamedItemOrEmpty(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 64),
    )



class TXLNamedItem(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )



class TXLNamedItemOrEmpty(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 255),
    )



class TItemDescription(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )



class TItemLongDescription(DisplayString):
    status = "current"


class TItemVeryLongDescription(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class TRegularExpression(DisplayString):
    status = "current"


class TmnxHttpRedirectUrl(DisplayString):
    status = "current"


class TmnxDisplayStringURL(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 180),
    )



class TmnxVRtrID(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10240),
    )



class TmnxVRtrIDOrZero(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10240),
    )



class VRtrIgmpHostMcRDstStatType(TextualConvention, Integer32):
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
        *(("joinTx", 1),
          ("joinDenyTx", 2),
          ("dropTx", 3),
          ("joinLost", 4),
          ("joinDenyLost", 5),
          ("dropLost", 6))
    )



class TmnxBgpAutonomousSystem(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class TmnxBgpLocalPreference(TextualConvention, Unsigned32):
    status = "current"


class TmnxBgpPreference(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class TmnxCustId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )



class TmnxCustIdNoZero(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class BgpPeeringStatus(TextualConvention, Integer32):
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
        *(("notApplicable", 0),
          ("installed", 1),
          ("notInstalled", 2),
          ("noEnhancedSubmgt", 3),
          ("wrongAntiSpoof", 4),
          ("parentItfDown", 5),
          ("hostInactive", 6),
          ("noDualHomingSupport", 7),
          ("invalidRadiusAttr", 8),
          ("noDynamicPeerGroup", 9),
          ("duplicatePeer", 10),
          ("maxPeersReached", 11),
          ("l2AwNotSupported", 12),
          ("gtpNotSupported", 13),
          ("genError", 14))
    )



class TmnxRipListenerStatus(TextualConvention, Integer32):
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("active", 1),
          ("inactive", 2),
          ("noEnhancedSubmgt", 3),
          ("wrongAntiSpoof", 4),
          ("parentItfDown", 5),
          ("hostInactive", 6),
          ("l2AwNotSupported", 7),
          ("gtpNotSupported", 8),
          ("mcStandby", 9),
          ("ripDisabled", 10))
    )



class TmnxServId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
        ValueRangeConstraint(2147483648, 2147483648),
        ValueRangeConstraint(2147483649, 2147483649),
        ValueRangeConstraint(2147483650, 2147483650),
        ValueRangeConstraint(2147483651, 2147483690),
        ValueRangeConstraint(2147483691, 2148007980),
        ValueRangeConstraint(2148007981, 2148012076),
        ValueRangeConstraint(2148012077, 2148016172),
        ValueRangeConstraint(2148016173, 2148278316),
        ValueRangeConstraint(2148278317, 2148278317),
        ValueRangeConstraint(2148278318, 2148278381),
        ValueRangeConstraint(2148278382, 2148278382),
        ValueRangeConstraint(2148278382, 2148278386),
    )



class TmnxExtServId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )



class TmnxAdminStateUpDown(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )



class TmnxAdminStateTruthValue(TruthValue):
    status = "current"


class TruthValueNoTypeTranslator(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )



class ServiceAdminStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )



class ServiceOperStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )



class TPolicyID(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
        ValueRangeConstraint(65536, 65536),
        ValueRangeConstraint(65537, 65537),
        ValueRangeConstraint(65538, 65538),
        ValueRangeConstraint(65539, 65539),
        ValueRangeConstraint(65540, 65540),
    )



class TTmplPolicyID(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class TQosIngressPolicyID(TPolicyID):
    status = "current"


class TSapIngressPolicyID(TPolicyID):
    status = "current"


class TSapEgressPolicyID(TPolicyID):
    status = "current"
    subtypeSpec = TPolicyID.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
        ValueRangeConstraint(65536, 65536),
        ValueRangeConstraint(65537, 65537),
        ValueRangeConstraint(65538, 65538),
        ValueRangeConstraint(65539, 65539),
    )



class TAnyQosPolicyID(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class TAnyQosPolicyIDorZero(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )



class TSdpIngressPolicyID(TPolicyID):
    status = "current"


class TSdpEgressPolicyID(TPolicyID):
    status = "current"


class TQosQGrpInstanceIDorZero(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )



class TmnxCreateOrigin(TextualConvention, Integer32):
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
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              23,
              24,
              25,
              26)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("bgp-l2vpn", 2),
          ("radius", 3),
          ("bgpSignalL2vpn", 4),
          ("multiSegmentPW", 5),
          ("vplsPmsi", 6),
          ("dynScript", 7),
          ("bof", 8),
          ("bgpSignalVpws", 9),
          ("vsd", 12),
          ("evpn", 13),
          ("vsd-sd", 14),
          ("satellites", 15),
          ("fpe", 16),
          ("evpnIsa", 17),
          ("greBridged", 18),
          ("tli", 19),
          ("pdn", 20),
          ("ipsec", 23),
          ("esa", 24),
          ("pfcpCups", 25),
          ("manual-mci", 26))
    )



class TmnxBsxTransitIpPolicyId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class TmnxBsxTransitIpPolicyIdOrZero(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )



class TmnxBsxTransPrefPolicyId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class TmnxBsxTransPrefPolicyIdOrZero(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )



class TmnxBsxAarpId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class TmnxBsxAarpIdOrZero(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )



class TmnxBsxAarpServiceRefType(TextualConvention, Integer32):
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
        *(("none", 0),
          ("dualHomed", 1),
          ("shuntSubscriberSide", 2),
          ("shuntNetworkSide", 3),
          ("dualHomedSecondary", 4))
    )



class TmnxBsxIsaAaGroupIndexOrZero(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class TmnxBsxAaGrpPartIndexOrZero(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )



class TmnxBsxAaSubHttpUrlParam(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 247),
    )



class TSapEgrEncapGrpQosPolicyIdOrZero(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )



class TSapEgrEncapGroupType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("isid", 1)
    )



class TSapEgrEncapGroupActionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("destroy", 2))
    )



class TPerPacketOffset(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32, 31),
    )



class TPerPacketOffsetOvr(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, -128),
        ValueRangeConstraint(-32, 31),
    )



class TIngressHsmdaPerPacketOffset(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32, 31),
    )



class TIngHsmdaPerPacketOffsetOvr(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, -128),
        ValueRangeConstraint(-32, 31),
    )



class TEgressQPerPacketOffset(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-64, 32),
    )



class TEgressPerPacketOffset(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-64, 31),
    )



class TEgressPerPacketOffsetOvr(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, -128),
        ValueRangeConstraint(-64, 31),
    )



class TEgressHsmdaPerPacketOffset(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-64, 31),
    )



class TEgrHsmdaPerPacketOffsetOvr(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, -128),
        ValueRangeConstraint(-64, 31),
    )



class TIngressQPerPacketOffset(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32, 30),
    )



class THsmdaCounterIdOrZero(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8),
    )



class THsmdaCounterIdOrZeroOrAll(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8),
    )



class TIngressHsmdaCounterId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )



class TIngressHsmdaCounterIdOrZero(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8),
    )



class TEgressHsmdaCounterId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )



class TEgressHsmdaCounterIdOrZero(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8),
    )



class TEgrRateModType(TextualConvention, Integer32):
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
          ("aggRateLimit", 2),
          ("namedScheduler", 3))
    )



class TPolicyStatementName(TNamedItem):
    status = "current"


class TPolicyStatementNameOrEmpty(TNamedItemOrEmpty):
    status = "current"


class TLPolicyStatementNameOrEmpty(TLNamedItemOrEmpty):
    status = "current"


class TLPolicyNameOrExpOrEmpty(TLNamedItemOrEmpty):
    status = "current"


class TXLPolicyNameOrExpOrEmpty(TXLNamedItemOrEmpty):
    status = "current"


class TmnxVcType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              9,
              10,
              11,
              17,
              18,
              19,
              20,
              21,
              23,
              25,
              4096)
        )
    )
    namedValues = NamedValues(
        *(("frDlciMartini", 1),
          ("atmSdu", 2),
          ("atmCell", 3),
          ("ethernetVlan", 4),
          ("ethernet", 5),
          ("atmVccCell", 9),
          ("atmVpcCell", 10),
          ("ipipe", 11),
          ("satopE1", 17),
          ("satopT1", 18),
          ("satopE3", 19),
          ("satopT3", 20),
          ("cesopsn", 21),
          ("cesopsnCas", 23),
          ("frDlci", 25),
          ("mirrorDest", 4096))
    )



class TmnxVcId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class TmnxVcIdOrNone(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )



class DateAndTimeOrEmpty(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(11, 11),
    )



class ClassIndex(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )



class ClassIndexOrNone(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )



class Dot1PPriority(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )



class Dot1PPriorityMask(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



class Dot1PPriorityNonZeroMask(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )



class ServiceAccessPoint(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )



class TLspExpValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )



class TIpProtocol(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )



class TIpProtocolNumber(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class TIpOption(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class TIcmpTypeOrNone(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )



class TIcmpCodeOrNone(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )



class TTcpUdpPort(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )



class TOperator(TextualConvention, Integer32):
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
        *(("none", 0),
          ("eq", 1),
          ("range", 2),
          ("lt", 3),
          ("gt", 4))
    )



class TTcpUdpPortOperator(TOperator):
    status = "current"


class TFrameType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("e802dot3", 0),
          ("e802dot2LLC", 1),
          ("e802dot2SNAP", 2),
          ("ethernetII", 3),
          ("atm", 5))
    )



class TQueueId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 32),
    )



class TQueueIdOrAll(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 32),
    )



class TIngressQueueId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 32),
    )



class TEgressQueueId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8),
    )



class TIngressHsmdaQueueId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8),
    )



class TEgressHsmdaQueueId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8),
    )



class THsmdaSchedulerPolicyGroupId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2),
    )



class THsmdaPolicyIncludeQueues(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("q1to2", 1),
          ("q1to3", 2))
    )



class THsmdaPolicyScheduleClass(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )



class TDSCPName(TNamedItem):
    status = "current"


class TDSCPNameOrEmpty(TNamedItemOrEmpty):
    status = "current"


class TDSCPValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )



class TDSCPValueOrNone(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 63),
    )



class TDSCPFilterActionValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )



class TFCName(TNamedItem):
    status = "current"


class TFCNameOrEmpty(TNamedItemOrEmpty):
    status = "current"


class TFCSet(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("be", 0),
          ("l2", 1),
          ("af", 2),
          ("l1", 3),
          ("h2", 4),
          ("ef", 5),
          ("h1", 6),
          ("nc", 7))
    )


class TFCType(TextualConvention, Integer32):
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
        *(("be", 0),
          ("l2", 1),
          ("af", 2),
          ("l1", 3),
          ("h2", 4),
          ("ef", 5),
          ("h1", 6),
          ("nc", 7))
    )



class TFCTypeOrNone(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
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
        *(("none", -1),
          ("be", 0),
          ("l2", 1),
          ("af", 2),
          ("l1", 3),
          ("h2", 4),
          ("ef", 5),
          ("h1", 6),
          ("nc", 7))
    )



class TmnxTunnelType(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("sdp", 1),
          ("ldp", 2),
          ("rsvp", 3),
          ("gre", 4),
          ("bypass", 5),
          ("invalid", 6),
          ("bgp", 7))
    )



class TmnxTunnelID(TextualConvention, Unsigned32):
    status = "current"


class TmnxBgpRouteTarget(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class TmnxVPNRouteDistinguisher(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



class SdpBindId(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



class TmnxVRtrMplsLspID(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
        ValueRangeConstraint(65536, 131070),
    )



class TmnxVRtrMplsLspIDNoZero(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
        ValueRangeConstraint(65536, 131070),
    )



class TPortSchedulerPIR(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 100000000),
    )



class TPortSchedulerAggRateLimitPIR(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 800000000),
    )



class TPortSchedulerPIRRate(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 800000000),
    )



class TPortSchedulerCIR(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 800000000),
    )



class TPortQosPIRRate(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )



class TPortQosCIRRate(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )



class TWeight(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class TWeightOverride(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(0, 100),
    )



class TNonZeroWeight(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )



class TPolicerWeight(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )



class THsWrrWeightOvr(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(1, 127),
    )



class THsClassWeightOverride(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(8, 8),
    )



class THsmdaWeight(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )



class THsmdaWrrWeight(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )



class THsmdaWeightClass(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("class1", 1),
          ("class2", 2),
          ("class4", 4),
          ("class8", 8))
    )



class THsmdaWeightOverride(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(1, 100),
    )



class THsmdaWrrWeightOverride(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(1, 32),
    )



class TCIRRate(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 100000000),
    )



class THPolCIRRate(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2000000000),
    )



class TRateType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("kbps", 1),
          ("percent", 2))
    )



class TBWRateType(TextualConvention, Integer32):
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
        *(("kbps", 1),
          ("percentPortLimit", 2),
          ("percentLocalLimit", 3))
    )



class TPSPRateType(TextualConvention, Integer32):
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
        *(("kbps", 1),
          ("percentLocal", 2),
          ("percentLagActive", 3))
    )



class TPolicerRateType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("kbps", 1),
          ("percentLocalLimit", 2))
    )



class TCIRRateOverride(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 100000000),
    )



class THPolCIRRateOverride(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2000000000),
    )



class TCIRPercentOverride(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(0, 10000),
    )



class THsmdaCIRKRate(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 100000000),
    )



class THsmdaCIRKRateOverride(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 100000000),
    )



class THsmdaCIRMRate(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 100000),
    )



class THsmdaCIRMRateOverride(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 100000),
    )



class TPIRRate(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 100000000),
    )



class THPolVirtualSchePIRRate(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 800000000),
    )



class THPolVirtualScheCIRRate(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 800000000),
    )



class TAdvCfgRate(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )



class TMaxDecRate(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 100000000),
    )



class THPolPIRRate(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 2000000000),
    )



class TSecondaryShaper10GPIRRate(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 10000),
    )



class TExpSecondaryShaperPIRRate(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 10000000),
    )



class TExpSecondaryShaperClassRate(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 10000000),
    )



class TPIRRateOverride(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 100000000),
    )



class TPIRAggRateLimitOverride(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 800000000),
    )



class THPolPIRRateOverride(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 2000000000),
    )



class TPIRPercentOverride(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(1, 10000),
    )



class TPIRRateOrZero(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 100000000),
    )



class THsmdaPIRKRate(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 100000000),
    )



class THsmdaPIRKRateOverride(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 100000000),
    )



class THsmdaPIRMRate(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 100000),
    )



class THsmdaPIRMRateOverride(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 100000),
    )



class TmnxDHCP6MsgType(TextualConvention, Integer32):
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("dhcp6MsgTypeSolicit", 1),
          ("dhcp6MsgTypeAdvertise", 2),
          ("dhcp6MsgTypeRequest", 3),
          ("dhcp6MsgTypeConfirm", 4),
          ("dhcp6MsgTypeRenew", 5),
          ("dhcp6MsgTypeRebind", 6),
          ("dhcp6MsgTypeReply", 7),
          ("dhcp6MsgTypeRelease", 8),
          ("dhcp6MsgTypeDecline", 9),
          ("dhcp6MsgTypeReconfigure", 10),
          ("dhcp6MsgTypeInfoRequest", 11),
          ("dhcp6MsgTypeRelayForw", 12),
          ("dhcp6MsgTypeRelayReply", 13),
          ("dhcp6MsgTypeLeasequery", 14),
          ("dhcp6MsgTypeLeasequeryReply", 15))
    )



class TmnxDhcpClientState(TextualConvention, Integer32):
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
        *(("init", 0),
          ("init-reboot", 1),
          ("rebooting", 2),
          ("selecting", 3),
          ("requesting", 4),
          ("rebinding", 5),
          ("bound", 6),
          ("renewing", 7))
    )



class TmnxIgpInstance(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )



class TmnxOspfInstance(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )



class TmnxBGPFamilyType(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("ipv4Unicast", 0),
          ("ipv4Multicast", 1),
          ("ipv4UastMcast", 2),
          ("ipv4MplsLabel", 3),
          ("ipv4Vpn", 4),
          ("ipv6Unicast", 5),
          ("ipv6Multicast", 6),
          ("ipv6UcastMcast", 7),
          ("ipv6MplsLabel", 8),
          ("ipv6Vpn", 9),
          ("l2Vpn", 10),
          ("ipv4Mvpn", 11),
          ("msPw", 12),
          ("ipv4Flow", 13),
          ("mdtSafi", 14),
          ("routeTarget", 15),
          ("mcastVpnIpv4", 16),
          ("mvpnIpv6", 17),
          ("ipv6Flow", 18),
          ("evpn", 19),
          ("bgpLs", 20),
          ("mcastVpnIpv6", 21),
          ("srplcyIpv4", 22),
          ("srplcyIpv6", 23),
          ("reserved24", 24),
          ("reserved25", 25))
    )


class TmnxIgmpGroupFilterMode(TextualConvention, Integer32):
    status = "current"
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



class TmnxIgmpGroupType(TextualConvention, Integer32):
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
        *(("static", 1),
          ("dynamic", 2),
          ("bgp-smet", 3),
          ("bgp-sync", 4))
    )



class TmnxIgmpSnpgGroupType(TextualConvention, Integer32):
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
        *(("static", 1),
          ("dynamic", 2),
          ("bgp-smet", 3),
          ("bgp-sync", 4))
    )



class TmnxIgmpVersion(TextualConvention, Integer32):
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
        *(("version1", 1),
          ("version2", 2),
          ("version3", 3))
    )



class TmnxMldGroupFilterMode(TextualConvention, Integer32):
    status = "current"
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



class TmnxMldGroupType(TextualConvention, Integer32):
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
        *(("static", 1),
          ("dynamic", 2),
          ("bgp-smet", 3),
          ("bgp-sync", 4))
    )



class TmnxMldVersion(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("version1", 1),
          ("version2", 2))
    )



class TmnxManagedRouteStatus(TextualConvention, Integer32):
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
        *(("installed", 0),
          ("notYetInstalled", 1),
          ("wrongAntiSpoofType", 2),
          ("outOfMemory", 3),
          ("shadowed", 4),
          ("routeTableFull", 5),
          ("parentInterfaceDown", 6),
          ("hostInactive", 7),
          ("enhancedSubMgmtRequired", 8),
          ("deprecated1", 9),
          ("l2AwNotSupported", 10),
          ("nextHopLimitExceeded", 11),
          ("notApplicable", 12),
          ("noNextHop", 13),
          ("gtpNotSupported", 14))
    )



class TmnxTunnelTypeExt(TextualConvention, Integer32):
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("sdp", 2),
          ("rsvp", 3),
          ("ldp", 4),
          ("ospf", 5),
          ("isis", 6),
          ("bypass", 7),
          ("gre", 8),
          ("bgp", 9),
          ("srTe", 10),
          ("fpe", 11),
          ("udp", 12),
          ("ospfV3", 13),
          ("mplsFwdPolicy", 14),
          ("srPolicy", 15),
          ("ribApi", 16),
          ("bgpEpe", 17),
          ("srv6Isis", 18))
    )



class TmnxIgpSCFamilyType(TextualConvention, Integer32):
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
        *(("ipv4", 0),
          ("ipv6", 1),
          ("srv4", 2),
          ("srv6", 3))
    )



class TmnxAdjacencySetFamilyType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 0),
          ("ipv6", 1))
    )



class TmnxAncpString(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )



class TmnxAncpStringOrZero(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )



class TmnxMulticastAddrFamily(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ipv4Multicast", 0),
          ("ipv6Multicast", 1))
    )



class TmnxNatIsaGrpId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )



class TmnxNatIsaGrpIdOrZero(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )



class TmnxNatL2AwAccessMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("bridged", 2))
    )



class TmnxNatSubscriberType(TextualConvention, Integer32):
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
        *(("l2AwareSub", 1),
          ("classicLsnSub", 2),
          ("dsliteLsnSub", 3),
          ("nat64LsnSub", 4))
    )



class TmnxNatSubscriberTypeOrNone(TextualConvention, Integer32):
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
        *(("none", 0),
          ("l2AwareSub", 1),
          ("classicLsnSub", 2),
          ("dsliteLsnSub", 3),
          ("nat64LsnSub", 4))
    )



class TmnxNatWaterMark(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class TmnxAuthPassword(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class TmnxAsciiSpecification(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class TmnxMacSpecification(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )



class TmnxBinarySpecification(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class TmnxDefSubIdSource(TextualConvention, Integer32):
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
        *(("useSapId", 1),
          ("useString", 2),
          ("useAutoId", 3))
    )



class TmnxSubAuthPlcyUserNameOp(TextualConvention, Integer32):
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
        *(("noOperation", 0),
          ("appendDomain", 1),
          ("stripDomain", 2),
          ("replaceDomain", 3),
          ("defaultDomain", 4))
    )



class TmnxSubCallingStationIdType(TextualConvention, Integer32):
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
        *(("sapString", 1),
          ("mac", 2),
          ("sapId", 3),
          ("remoteId", 4),
          ("llid", 5))
    )



class TmnxSubAcctSessionId(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )



class TmnxSubHostGrouping(TextualConvention, Integer32):
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
        *(("perSap", 1),
          ("perGroup", 2),
          ("perSessionPpp", 3),
          ("perSessionIpoe", 4))
    )



class TmnxSubIdentString(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )



class TmnxSubIdentStringOrEmpty(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class TmnxSubIdentShortString(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class TmnxSubRadServAlgorithm(TextualConvention, Integer32):
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
        *(("direct", 1),
          ("roundRobin", 2),
          ("hashBased", 3))
    )



class TmnxSubRadIsaServAlgorithm(TextualConvention, Integer32):
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
        *(("direct", 1),
          ("roundRobin", 2),
          ("hashBased", 3),
          ("directPriority", 4))
    )



class TmnxSubRadiusAttrType(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class TmnxSubRadiusVendorId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )



class TmnxSubRadiusDisplayString(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 253),
    )



class TmnxSubRadiusOctetString(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(253, 253),
    )
    fixed_length = 253



class TmnxSubSlaMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("expanded", 0),
          ("single", 1))
    )



class TmnxRadiusPendingReqLimit(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )



class TmnxRadiusServerOperState(TextualConvention, Integer32):
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
        *(("unknown", 1),
          ("inService", 2),
          ("outOfService", 3),
          ("transition", 4),
          ("overloaded", 5),
          ("probing", 6))
    )



class TmnxSubShcvAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("remove", 2))
    )



class TmnxSubShcvInterval(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6000),
    )



class TmnxSubShcvRetryCount(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 29),
    )



class TmnxSubShcvRetryTimeout(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 60),
    )



class TmnxSubShcvSrcIpOrigin(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("interface", 1),
          ("vrrp", 2))
    )



class TmnxSubSpiGroupId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )



class TmnxSubOperSpiGroupId(TextualConvention, Integer32):
    status = "current"


class TmnxReferenceBandwidth(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4000000000),
    )



class TmnxSubPfcpNodeIdType(TextualConvention, Integer32):
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
          ("useIpAddress", 1),
          ("fqdn", 2))
    )



class TmnxSubPfcpNodeIdDomainName(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class TmnxSubPfcpPeerNodeIdType(TextualConvention, Integer32):
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
          ("useIpAddress", 1),
          ("reserved2", 2))
    )



class TmnxSubPfcpCurrPeerNodeIdType(TextualConvention, Integer32):
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
          ("useIpAddress", 1),
          ("fqdn", 2))
    )



class TmnxSubPoolName(TLNamedItem):
    status = "current"


class TmnxSubProfileString(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class TmnxSubProfileStringOrEmpty(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class TmnxSlaProfileString(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class TmnxSlaProfileStringOrEmpty(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class TmnxAppProfileString(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )



class TmnxAppProfileStringOrEmpty(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



class TmnxSubMgtIntDestIdOrEmpty(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class TmnxSubMgtIntDestId(TmnxSubMgtIntDestIdOrEmpty):
    status = "current"
    subtypeSpec = TmnxSubMgtIntDestIdOrEmpty.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class TmnxDefInterDestIdSource(TextualConvention, Integer32):
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
        *(("useString", 1),
          ("useTopQTag", 2),
          ("useVpi", 3))
    )



class TmnxSubNasPortSuffixType(TextualConvention, Integer32):
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
          ("circuitId", 1),
          ("remoteId", 2))
    )



class TmnxSubNasPortPrefixType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("userString", 1))
    )



class TmnxSubNasPortTypeType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("standard", 1),
          ("config", 2))
    )



class TmnxSubCreditVolumeUnit(TextualConvention, Integer32):
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
        *(("bytes", 0),
          ("kilobytes", 1),
          ("megabytes", 2),
          ("gigabytes", 3))
    )



class TmnxPccRuleFilterForwardAction(TextualConvention, Integer32):
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
        *(("none", 0),
          ("forward", 1),
          ("drop", 2),
          ("redirUrl", 3),
          ("redirNh", 4),
          ("redirNhOrFwd", 5))
    )



class TmnxPccRuleQosForwardAction(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("rateLimit", 0),
          ("fcRemark", 1),
          ("monitor", 2),
          ("account", 3),
          ("forward", 4))
    )


class TmnxRadiusFramedRouteMetric(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class TmnxRadiusFramedRoutePreference(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class TmnxRadiusFramedRouteTag(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class TmnxSubMgtOrgStrOrZero(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class TmnxSubMgtOrgString(TmnxSubMgtOrgStrOrZero):
    status = "current"
    subtypeSpec = TmnxSubMgtOrgStrOrZero.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class TmnxFilterProfileStringOrEmpty(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



class TmnxFpeId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )



class TmnxFpeIdOrZero(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )



class TmnxFpePathId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )



class TmnxAccessLoopEncapDataLink(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("aal5", 0),
          ("ethernet", 1))
    )



class TmnxAccessLoopEncaps1(TextualConvention, Integer32):
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
        *(("notAvailable", 0),
          ("untaggedEthernet", 1),
          ("singleTaggedEthernet", 2))
    )



class TmnxAccessLoopEncaps2(TextualConvention, Integer32):
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
        *(("notAvailable", 0),
          ("pppoaLlc", 1),
          ("pppoaNull", 2),
          ("ipoaLlc", 3),
          ("ipoaNull", 4),
          ("ethernetOverAal5LlcFcs", 5),
          ("ethernetOverAal5LlcNoFcs", 6),
          ("ethernetOverAal5NullFcs", 7),
          ("ethernetOverAal5NullNoFcs", 8))
    )



class TmnxSubAleOffsetMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("auto", 1))
    )



class TmnxSubAleOffset(TextualConvention, Integer32):
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
          ("pppoaLlc", 1),
          ("pppoaNull", 2),
          ("pppoeoaLlc", 3),
          ("pppoeoaLlcFcs", 4),
          ("pppoeoaLlcTagged", 5),
          ("pppoeoaLlcTaggedFcs", 6),
          ("pppoeoaNull", 7),
          ("pppoeoaNullFcs", 8),
          ("pppoeoaNullTagged", 9),
          ("pppoeoaNullTaggedFcs", 10),
          ("ipoaLlc", 11),
          ("ipoaNull", 12),
          ("ipoeoaLlc", 13),
          ("ipoeoaLlcFcs", 14),
          ("ipoeoaLlcTagged", 15),
          ("ipoeoaLlcTaggedFcs", 16),
          ("ipoeoaNull", 17),
          ("ipoeoaNullFcs", 18),
          ("ipoeoaNullTagged", 19),
          ("ipoeoaNullTaggedFcs", 20),
          ("pppoe", 21),
          ("pppoeTagged", 22),
          ("ipoe", 23),
          ("ipoeTagged", 24))
    )



class TmnxDataFormat(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 2),
          ("hex", 3))
    )



class TmnxDhcpOptionType(TextualConvention, Integer32):
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
        *(("ipv4", 1),
          ("ascii", 2),
          ("hex", 3),
          ("ipv6", 4),
          ("domain", 5))
    )



class TmnxDhcpOptionDisplay(TextualConvention, Integer32):
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
        *(("default", 1),
          ("hexDuration", 2),
          ("hexNetbiosNodeType", 3),
          ("hexIpv4Address", 4),
          ("hexIpv6Address", 5))
    )



class TmnxDhcpServerDUIDTypeCode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("duidEnterprise", 2),
          ("duidLinkLocal", 3))
    )



class TmnxPppoeUserName(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 253),
    )



class TmnxPppoeUserNameOrEmpty(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 253),
    )



class TCpmProtPolicyID(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class TCpmProtPolicyIDOrDefault(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 255),
    )



class TMlpppQoSProfileId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class TMcFrQoSProfileId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class TmnxPppoeSessionId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class TmnxPppoePadoDelay(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 30),
    )



class TmnxPppoeSessionInfoOrigin(TextualConvention, Integer32):
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
        *(("none", 0),
          ("default", 1),
          ("radius", 2),
          ("localUserDb", 3),
          ("dhcp", 4),
          ("midSessionChange", 5),
          ("tags", 6),
          ("l2tp", 7),
          ("localPool", 8),
          ("diameterNasreq", 9),
          ("diameterGx", 10),
          ("gtp", 11),
          ("python", 12),
          ("bonding", 13))
    )



class TmnxPppoeSessionType(TextualConvention, Integer32):
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
        *(("local", 1),
          ("localWholesale", 2),
          ("localRetail", 3),
          ("l2tp", 4))
    )



class TmnxPppNcpProtocol(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipcp", 1),
          ("ipv6cp", 2))
    )



class TmnxDiamCcFailureHndlng(TextualConvention, Integer32):
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
        *(("terminate", 1),
          ("continue", 2),
          ("retryAndTerminate", 3))
    )



class TmnxMlpppEpClass(TextualConvention, Integer32):
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
        *(("null", 0),
          ("local", 1),
          ("ipv4Address", 2),
          ("macAddress", 3),
          ("magicNumber", 4),
          ("directoryNumber", 5))
    )



class TNetworkPolicyID(TPolicyID):
    status = "current"
    subtypeSpec = TPolicyID.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
        ValueRangeConstraint(65536, 65536),
        ValueRangeConstraint(65537, 65537),
        ValueRangeConstraint(65538, 65538),
        ValueRangeConstraint(65539, 65539),
    )



class TItemScope(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exclusive", 1),
          ("template", 2))
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



class TPriority(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("high", 2))
    )



class TPriorityOrDefault(TextualConvention, Integer32):
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
        *(("low", 1),
          ("high", 2),
          ("default", 3))
    )



class TPriorityOrUndefined(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("low", 1),
          ("high", 2))
    )



class TProfile(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2))
    )



class TProfileOrNone(TextualConvention, Integer32):
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
          ("in", 1),
          ("out", 2))
    )



class TDEProfile(TextualConvention, Integer32):
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
        *(("in", 1),
          ("out", 2),
          ("de", 3))
    )



class TEgressProfile(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2),
          ("exceed", 4),
          ("inplus", 5))
    )



class TEgressProfileOrNone(TextualConvention, Integer32):
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
        *(("none", 0),
          ("in", 1),
          ("out", 2),
          ("de", 3),
          ("exceed", 4),
          ("inplus", 5))
    )



class TAdaptationRule(TextualConvention, Integer32):
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
        *(("max", 1),
          ("min", 2),
          ("closest", 3))
    )



class TAdaptationRuleOverride(TextualConvention, Integer32):
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
        *(("noOverride", 0),
          ("max", 1),
          ("min", 2),
          ("closest", 3))
    )



class TRemarkType(TextualConvention, Integer32):
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
          ("dscp", 2),
          ("precedence", 3))
    )



class TIngClassRemarkType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("dot1pExp", 2))
    )



class TPrecValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



class TPrecValueOrNone(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )



class TCpmFilterBurstSize(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 131072),
    )



class TBurstSize(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 1048576),
    )



class TBurstSizeOverride(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 1048576),
    )



class TBurstSizeBytesOvr(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 1073741824),
    )



class TBurstPercent(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class TBurstHundredthsOfPercent(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )



class TBurstPercentOrDefault(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 100),
    )



class TBurstPercentOrDefaultOverride(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 100),
    )



class TRatePercent(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class TPIRRatePercent(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )



class TLevel(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )



class TPortSchedLevel(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )



class TLevelOrDefault(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8),
    )



class TQueueMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("priority", 1),
          ("profile", 2))
    )



class TQueueStatModeFormat(TextualConvention, Integer32):
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
        *(("priority", 1),
          ("profile", 2),
          ("v4V6", 3))
    )



class TEntryIndicator(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class TEntryId(TEntryIndicator):
    status = "current"
    subtypeSpec = TEntryIndicator.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class TMatchCriteria(TextualConvention, Integer32):
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
        *(("ip", 1),
          ("mac", 2),
          ("none", 3))
    )



class TmnxMdaQos(TextualConvention, Integer32):
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
          ("mda", 1),
          ("hsmda1", 2),
          ("hsmda2", 3),
          ("hs", 4),
          ("fpHwAggShaper", 5))
    )



class TAtmTdpDescrType(TextualConvention, Integer32):
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
        *(("clp0And1pcr", 0),
          ("clp0And1pcrPlusClp0And1scr", 1),
          ("clp0And1pcrPlusClp0scr", 2),
          ("clp0And1pcrPlusClp0scrTag", 3))
    )



class TDEValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 1),
    )



class TQGroupType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("port", 0),
          ("vpls", 1))
    )



class TQosOverrideType(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("queue", 1),
          ("policer", 2),
          ("aggRateLimit", 3),
          ("arbiter", 4),
          ("scheduler", 5),
          ("slaAggRateLimit", 6),
          ("wrrGroup", 7))
    )



class TQosOverrideTypeId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )



class TmnxIPsecTunnelTemplateId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )



class TmnxIPsecTunnelTemplateIdOrZero(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )



class TmnxIpSecIsaOperFlags(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("adminDown", 0),
          ("noActive", 1),
          ("noResources", 2),
          ("mcAdminDown", 3))
    )


class TmnxIkePolicyAuthMethod(TextualConvention, Integer32):
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
        *(("psk", 1),
          ("hybridX509XAuth", 2),
          ("plainX509XAuth", 3),
          ("plainPskXAuth", 4),
          ("cert", 5),
          ("pskRadius", 6),
          ("certRadius", 7),
          ("eap", 8),
          ("autoEapRadius", 9),
          ("autoEap", 10))
    )



class TmnxIkePolicyAutoEapMethod(TextualConvention, Integer32):
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
        *(("psk", 1),
          ("cert", 2),
          ("pskOrCert", 3))
    )



class TmnxIkePolicyAutoEapOwnMethod(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("psk", 1),
          ("cert", 2))
    )



class TmnxIkePolicyOwnAuthMethod(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              5,
              8)
        )
    )
    namedValues = NamedValues(
        *(("symmetric", 0),
          ("psk", 1),
          ("cert", 5),
          ("eapOnly", 8))
    )



class TmnxRsvpDSTEClassType(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



class TmnxAccPlcyQICounters(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("hpo", 0),
          ("lpo", 1),
          ("ucp", 2),
          ("hoo", 3),
          ("loo", 4),
          ("uco", 5),
          ("apo", 6),
          ("aoo", 7),
          ("hpd", 8),
          ("lpd", 9),
          ("hod", 10),
          ("lod", 11),
          ("ipf", 12),
          ("opf", 13),
          ("iof", 14),
          ("oof", 15))
    )


class TmnxAccPlcyQECounters(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("ipf", 0),
          ("ipd", 1),
          ("opf", 2),
          ("opd", 3),
          ("iof", 4),
          ("iod", 5),
          ("oof", 6),
          ("ood", 7))
    )


class TmnxAccPlcyPolicerICounters(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("ipo", 0),
          ("ipd", 1),
          ("opo", 2),
          ("opd", 3),
          ("ioo", 4),
          ("iod", 5),
          ("ooo", 6),
          ("ood", 7),
          ("ucp", 8),
          ("uco", 9),
          ("ipf", 10),
          ("iof", 11),
          ("opf", 12),
          ("oof", 13))
    )


class TmnxAccPlcyPolicerECounters(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("ipo", 0),
          ("ipd", 1),
          ("opo", 2),
          ("opd", 3),
          ("ioo", 4),
          ("iod", 5),
          ("ooo", 6),
          ("ood", 7),
          ("ucp", 8),
          ("uco", 9),
          ("ipf", 10),
          ("iof", 11),
          ("opf", 12),
          ("oof", 13),
          ("xpo", 14),
          ("xpd", 15),
          ("xpf", 16),
          ("xoo", 17),
          ("xod", 18),
          ("xof", 19),
          ("ppo", 20),
          ("ppd", 21),
          ("ppf", 22),
          ("poo", 23),
          ("pod", 24),
          ("pof", 25))
    )


class TmnxAccPlcyOICounters(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("apo", 0),
          ("aoo", 1),
          ("hpd", 2),
          ("lpd", 3),
          ("hod", 4),
          ("lod", 5),
          ("ipf", 6),
          ("opf", 7),
          ("iof", 8),
          ("oof", 9))
    )


class TmnxAccPlcyOECounters(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("ipf", 0),
          ("ipd", 1),
          ("opf", 2),
          ("opd", 3),
          ("iof", 4),
          ("iod", 5),
          ("oof", 6),
          ("ood", 7))
    )


class TmnxAccPlcyAACounters(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("any", 0),
          ("sfa", 1),
          ("nfa", 2),
          ("sfd", 3),
          ("nfd", 4),
          ("saf", 5),
          ("naf", 6),
          ("spa", 7),
          ("npa", 8),
          ("sba", 9),
          ("nba", 10),
          ("spd", 11),
          ("npd", 12),
          ("sbd", 13),
          ("nbd", 14),
          ("sdf", 15),
          ("mdf", 16),
          ("ldf", 17),
          ("tfd", 18),
          ("tfc", 19),
          ("sbm", 20),
          ("spm", 21),
          ("smt", 22),
          ("nbm", 23),
          ("npm", 24),
          ("nmt", 25),
          ("sfc", 26),
          ("nfc", 27))
    )


class TmnxAccPlcyAASubAttributes(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("appProfile", 0),
          ("appServiceOption", 1))
    )


class TmnxIsaBbGrpId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )



class TmnxIsaScalingProfile(TextualConvention, Integer32):
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
        *(("profile1", 1),
          ("profile2", 2),
          ("profile3", 3))
    )



class TmnxVdoGrpIdIndex(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )



class TmnxVdoGrpId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )



class TmnxVdoGrpIdOrInherit(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 4),
    )



class TmnxVdoFccServerMode(TextualConvention, Integer32):
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
          ("burst", 1),
          ("dent", 2),
          ("hybrid", 3))
    )



class TmnxVdoPortNumber(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 5999),
        ValueRangeConstraint(6251, 65535),
    )



class TmnxVdoIfName(TNamedItem):
    status = "current"


class TmnxTimeInSec(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )



class TmnxReasContextVal(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )



class TmnxVdoStatInt(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("current", 1),
          ("interval", 2))
    )



class TmnxVdoOutputFormat(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("udp", 1),
          ("rtp-udp", 2))
    )



class TmnxVdoAnalyzerAlarm(TextualConvention, Integer32):
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
          ("tnc", 1),
          ("qos", 2),
          ("poa", 3))
    )



class TmnxVdoAnalyzerAlarmStates(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10



class SvcISID(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 16777215),
    )



class TmnxISID(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 16777215),
    )



class TIngPolicerId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )



class TNetIngPolicerId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )



class TNetIngPolicerIdOrNone(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 16),
    )



class TIngPolicerIdOrNone(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 32),
    )



class TIngressPolicerId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )



class TIngressPolicerIdOrNone(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 63),
    )



class TIngDynPolicerIdOrNone(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 63),
    )



class TEgrPolicerId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )



class TEgrPolicerIdOrNone(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8),
    )



class TEgressPolicerId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )



class TEgressPolicerIdOrNone(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 63),
    )



class TEgrDynPolicerIdOrNone(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 63),
    )



class TEgrDynQueueIdOrNone(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 63),
    )



class TFIRRate(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 100000000),
    )



class TBurstSizeBytes(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 1073741824),
    )



class THSMDABurstSizeBytes(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2688000),
    )



class THSMDAQueueBurstLimit(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 1000000),
    )



class TClassBurstLimit(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 327680),
    )



class TNetIngPlcrBurstSizeBytes(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(128, 4161536),
    )



class TPlcrBurstSizeBytes(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 16777216),
    )



class TBurstSizeBytesOverride(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 134217728),
    )



class TPolicerBurstSizeBytes(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 268435456),
    )



class THSMDABurstSizeBytesOverride(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2688000),
    )



class TPlcrBurstSizeBytesOverride(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 16777216),
    )



class TPolicerBurstSizeBytesOverride(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 268435456),
    )



class TmnxBfdSessionProtocols(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("ospfv2", 0),
          ("pim", 1),
          ("isis", 2),
          ("staticRoute", 3),
          ("mcRing", 4),
          ("rsvp", 5),
          ("bgp", 6),
          ("vrrp", 7),
          ("srrp", 8),
          ("mcep", 9),
          ("ldp", 10),
          ("ipsecTunnel", 11),
          ("ospfv3", 12),
          ("mcIpsec", 13),
          ("mcMobile", 14),
          ("mplsTp", 15),
          ("lag", 16),
          ("opergrp", 17),
          ("vccv", 18),
          ("rsvpLsp", 19),
          ("ldpLsp", 20),
          ("bgpLsp", 21),
          ("rip", 22),
          ("ripng", 23),
          ("mplsLsp", 24),
          ("reserved25", 25),
          ("srPolicy", 26),
          ("treeSid", 27),
          ("bier", 28))
    )


class TmnxBfdSessOperState(TextualConvention, Integer32):
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
        *(("unknown", 1),
          ("connected", 2),
          ("broken", 3),
          ("peerDetectsDown", 4),
          ("notConfigured", 5),
          ("noResources", 6))
    )



class TmnxBfdOnLspSessFecType(TextualConvention, Integer32):
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
        *(("rsvp", 1),
          ("ldp", 2),
          ("bgp", 3),
          ("srTe", 4),
          ("srPolicy", 5))
    )



class TmnxBfdSessProtocolState(TextualConvention, Integer32):
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
        *(("adminDown", 0),
          ("down", 1),
          ("init", 2),
          ("up", 3))
    )



class TmnxBfdSessOperFlags(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("noProtocols", 0),
          ("noHeartBeat", 1),
          ("echoFailed", 2),
          ("nbrSignalDown", 3),
          ("fwdPlaneReset", 4),
          ("pathDown", 5),
          ("nbrAdminDown", 6),
          ("adminClear", 7),
          ("misConnDefect", 8))
    )


class TmnxBfdTermination(TextualConvention, Integer32):
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
        *(("iom", 1),
          ("cpm", 2),
          ("cpmNp", 3),
          ("fp", 4))
    )



class TmnxIngPolicerStatMode(TextualConvention, Integer32):
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
        *(("noStats", 0),
          ("minimal", 1),
          ("offeredProfileNoCIR", 2),
          ("offeredTotalCIR", 3),
          ("offeredPriorityNoCIR", 4),
          ("offeredProfileCIR", 5),
          ("offeredPriorityCIR", 6),
          ("offeredLimitedProfileCIR", 7),
          ("offeredProfileCappedCIR", 8),
          ("offeredLimitedCappedCIR", 9))
    )



class TmnxSapIngPolicerStatMode(TextualConvention, Integer32):
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
        *(("noStats", 0),
          ("minimal", 1),
          ("offeredProfileNoCIR", 2),
          ("offeredTotalCIR", 3),
          ("offeredPriorityNoCIR", 4),
          ("offeredProfileCIR", 5),
          ("offeredPriorityCIR", 6),
          ("offeredLimitedProfileCIR", 7),
          ("offeredProfileCappedCIR", 8),
          ("offeredLimitedCappedCIR", 9),
          ("offeredProfileWithDiscards", 10),
          ("offeredFourProfileWithDiscards", 11))
    )



class TmnxNetIngPlcyPolicerStatMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              10)
        )
    )
    namedValues = NamedValues(
        *(("noStats", 0),
          ("offeredProfileWithDiscards", 10))
    )



class TmnxIngPolicerStatModeOverride(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
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
        *(("noOverride", -1),
          ("noStats", 0),
          ("minimal", 1),
          ("offeredProfileNoCIR", 2),
          ("offeredTotalCIR", 3),
          ("offeredPriorityNoCIR", 4),
          ("offeredProfileCIR", 5),
          ("offeredPriorityCIR", 6),
          ("offeredLimitedProfileCIR", 7),
          ("offeredProfileCappedCIR", 8),
          ("offeredLimitedCappedCIR", 9))
    )



class TmnxEgrPolicerStatMode(TextualConvention, Integer32):
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
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("noStats", 0),
          ("minimal", 1),
          ("offeredProfileNoCIR", 2),
          ("offeredTotalCIR", 3),
          ("offeredProfileCIR", 4),
          ("offeredLimitedCappedCIR", 5),
          ("offeredProfileCappedCIR", 6),
          ("offeredTotalCirExceed", 8),
          ("offeredFourProfileNoCir", 9),
          ("offeredTotalCirFourProfile", 10))
    )



class TmnxEgrPolicerStatModeOverride(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4,
              5,
              6,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("noOverride", -1),
          ("noStats", 0),
          ("minimal", 1),
          ("offeredProfileNoCIR", 2),
          ("offeredTotalCIR", 3),
          ("offeredProfileCIR", 4),
          ("offeredLimitedCappedCIR", 5),
          ("offeredProfileCappedCIR", 6),
          ("offeredTotalCirExceed", 8),
          ("offeredFourProfileNoCir", 9),
          ("offeredTotalCirFourProfile", 10))
    )



class TmnxTlsGroupId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )



class TSubHostId(TextualConvention, Unsigned32):
    status = "current"


class TDirection(TextualConvention, Integer32):
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
        *(("both", 0),
          ("ingress", 1),
          ("egress", 2))
    )



class TDirectionIngEgr(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ingress", 1),
          ("egress", 2))
    )



class TBurstLimit(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 14000000),
    )



class TMacFilterType(TextualConvention, Integer32):
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
        *(("normal", 1),
          ("isid", 2),
          ("vid", 3))
    )



class TIPFilterType(TextualConvention, Integer32):
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
        *(("normal", 1),
          ("vxlanVni", 2),
          ("tagged-entries", 3))
    )



class TmnxPwGlobalId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class TmnxPwGlobalIdOrZero(TextualConvention, Unsigned32):
    status = "current"


class TmnxPwPathHopId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )



class TmnxPwPathHopIdOrZero(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )



class TmnxSpokeSdpId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class TmnxSpokeSdpIdOrZero(TextualConvention, Unsigned32):
    status = "current"


class TmnxMsPwPeSignaling(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("master", 2))
    )



class TmnxLdpFECType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              128,
              129,
              130)
        )
    )
    namedValues = NamedValues(
        *(("addrWildcard", 1),
          ("addrPrefix", 2),
          ("addrHost", 3),
          ("vll", 128),
          ("vpws", 129),
          ("vpls", 130))
    )



class TmnxSvcOperGrpCreationOrigin(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              7,
              12)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("mvrp", 2),
          ("dynScript", 7),
          ("vsd", 12))
    )



class TmnxOperGrpHoldUpTime(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )



class TmnxOperGrpHoldDownTime(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )



class TmnxSrrpPriorityStep(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )



class TmnxAiiType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aiiType1", 1),
          ("aiiType2", 2))
    )



class TmnxSpbFid(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )



class TmnxSpbFidOrZero(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )



class TmnxSpbBridgePriority(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )



class TmnxSlopeMap(TextualConvention, Integer32):
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
          ("low", 1),
          ("high", 2),
          ("highLow", 3))
    )



class TmnxCdrType(TextualConvention, Integer32):
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
        *(("pgwCdr", 1),
          ("gCdr", 2),
          ("eGCdr", 3))
    )



class TmnxThresholdGroupType(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("brMgmtLimit", 1),
          ("brMgmtCfSuccess", 2),
          ("brMgmtCfFailure", 3),
          ("brMgmtTraffic", 4),
          ("pathMgmt", 5),
          ("pdnConnections", 6),
          ("mgIsmSystem", 7))
    )



class TmnxVpnIpBackupFamily(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("ipv4", 0),
          ("ipv6", 1))
    )


class TmnxTunnelGroupId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )



class TmnxTunnelGroupIdOrZero(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )



class TmnxQosBytesHex(TextualConvention, OctetString):
    status = "current"
    displayHint = "2x "
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )



class TSiteOperStatus(TextualConvention, Integer32):
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
        *(("up", 1),
          ("down", 2),
          ("outOfResource", 3))
    )



class TmnxSpbFdbLocale(TextualConvention, Integer32):
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
        *(("local", 1),
          ("sap", 2),
          ("sdp", 3),
          ("unknown", 4))
    )



class TmnxSpbFdbState(TextualConvention, Integer32):
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
        *(("ok", 0),
          ("addModPending", 1),
          ("delPending", 2),
          ("sysFdbLimit", 3),
          ("noFateShared", 4),
          ("svcFdbLimit", 5),
          ("noUcast", 6))
    )



class TmnxCdrDiagnosticAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("included", 1),
          ("excluded", 2))
    )



class TmnxLinkMapProfileId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )



class TmnxLinkMapProfileIdOrZero(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 64),
    )



class TmnxDayOfWeek(TextualConvention, Integer32):
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
        *(("unspecified", 0),
          ("sunday", 1),
          ("monday", 2),
          ("tuesday", 3),
          ("wednesday", 4),
          ("thursday", 5),
          ("friday", 6),
          ("saturday", 7))
    )



class TmnxDayOfWeekList(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("sunday", 0),
          ("monday", 1),
          ("tuesday", 2),
          ("wednesday", 3),
          ("thursday", 4),
          ("friday", 5),
          ("saturday", 6))
    )


class TmnxMplsTpGlobalID(TextualConvention, Unsigned32):
    status = "current"


class TmnxMplsTpNodeID(TextualConvention, Unsigned32):
    status = "current"


class TmnxMplsTpTunnelType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("mplsTpStatic", 1)
    )



class TmnxDistCpuProtPacketRateLimit(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )



class TmnxDistCpuProtPacketPolicerRateLimit(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 8000),
    )



class TmnxDistCpuProtRate(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 20000000),
    )



class TmnxDistCpuProtBurstSize(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 4194304),
    )



class TmnxDistCpuProtActionDuration(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 10080),
    )



class TmnxDistCpuProtAction(TextualConvention, Integer32):
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
        *(("discard", 1),
          ("low-priority", 2),
          ("none", 3))
    )



class TmnxDistCpuProtEnforceType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2))
    )



class TmnxDistCpuProtProtocolId(TextualConvention, Integer32):
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
              21)
        )
    )
    namedValues = NamedValues(
        *(("arp", 1),
          ("dhcp", 2),
          ("http-redirect", 3),
          ("icmp", 4),
          ("igmp", 5),
          ("mld", 6),
          ("ndis", 7),
          ("pppoe-pppoa", 8),
          ("all-unspecified", 9),
          ("mpls-ttl", 10),
          ("bfd-cpm", 11),
          ("bgp", 12),
          ("eth-cfm", 13),
          ("isis", 14),
          ("ldp", 15),
          ("ospf", 16),
          ("pim", 17),
          ("rsvp", 18),
          ("icmp-ping-check", 19),
          ("lacp", 21))
    )



class TmnxDistCpuProtRateType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("packets", 1),
          ("kbps", 2))
    )



class TmnxDistCpuProtLogEventType(TextualConvention, Integer32):
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
          ("enable", 1),
          ("verbose", 2))
    )



class TmnxDistCpuProtState(TextualConvention, Integer32):
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
        *(("exceed", 1),
          ("conform", 2),
          ("not-applicable", 3))
    )



class TmnxIsidMFibStatus(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("ok", 0),
          ("addPending", 1),
          ("delPending", 2),
          ("sysMFibLimit", 3),
          ("useDefMCTree", 4))
    )


class TmnxBfdIntfSessOperState(TextualConvention, Integer32):
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
        *(("unknown", 1),
          ("connected", 2),
          ("broken", 3),
          ("peerDetectsDown", 4),
          ("notConfigured", 5),
          ("noResources", 6))
    )



class TmnxBfdEncap(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ipv4", 1)
    )



class TLDisplayString(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1022),
    )



class IPv6FlowLabel(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 1048575),
    )



class IPv6FlowLabelMask(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )



class TmnxWlanGwIsaGrpId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )



class TmnxWlanGwIsaGrpIdOrZero(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )



class TmnxMplsLdpNgIdType(TextualConvention, Integer32):
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



class TmnxMplsLdpNgIdentifier(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )



class TmnxMplsLsrNgIdentifier(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16



class TmnxLagPerLinkHashClass(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )



class TmnxLagPerLinkHashClassOrNone(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )



class TmnxLagPerLinkHashWeight(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )



class BgpConnectRetryTime(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class BgpHoldTime(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 65535),
    )



class TmnxInternalSchedWeightMode(TextualConvention, Integer32):
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
        *(("noOverride", 1),
          ("default", 2),
          ("forceEqual", 3),
          ("offeredLoad", 4),
          ("cappedOfferedLoad", 5))
    )



class TmnxHigh32(TextualConvention, Unsigned32):
    status = "current"


class TmnxLow32(TextualConvention, Unsigned32):
    status = "current"


class TQosQueuePIRRate(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 2000000000),
    )



class TQosQueueCIRRate(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2000000000),
    )



class TQosQueuePIRRateOverride(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 2000000000),
    )



class TQosQueueCIRRateOverride(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2000000000),
    )



class TResolveStatus(TextualConvention, Integer32):
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
        *(("disabled", 0),
          ("filter", 1),
          ("any", 2),
          ("match-family-ip", 3))
    )



class LAGInterfaceNumber(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 800),
    )



class LAGInterfaceNumberOrZero(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 800),
    )



class TmnxRouteTargetOrigin(TextualConvention, Integer32):
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
        *(("none", 0),
          ("configured", 1),
          ("derivedVpls", 2),
          ("derivedEvi", 3),
          ("vsi", 4))
    )



class TmnxRouteDistType(TextualConvention, Integer32):
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
        *(("none", 0),
          ("configured", 1),
          ("derivedVpls", 2),
          ("derivedEvi", 3),
          ("auto", 4),
          ("default", 5))
    )



class TmnxScriptAuthType(TextualConvention, Integer32):
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
        *(("none", 0),
          ("cron", 1),
          ("xmpp", 2),
          ("event-script", 3),
          ("vsd", 4),
          ("cron-python", 5),
          ("event-script-python", 6))
    )



class TmnxISIDNoZero(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )



class TmnxSvcEvi(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )



class TmnxSecRadiusServAlgorithm(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("direct", 1),
          ("round-robin", 2))
    )



class TmnxSvcEviOrZero(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )



class TmnxSubTerminationType(TextualConvention, Integer32):
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
        *(("local", 1),
          ("localWholesale", 2),
          ("localRetail", 3))
    )



class TmnxSubTerminationTypeOrZero(TextualConvention, Integer32):
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
          ("local", 1),
          ("localWholesale", 2),
          ("localRetail", 3))
    )



class TmnxLongDisplayString(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )



class TmnxLongDisplayStringToBinary(TmnxLongDisplayString):
    status = "current"


class TmnxLongDisplayStringLegacyBinary(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 900),
    )



class TmnxProxyEntryType(TextualConvention, Integer32):
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
        *(("evpn", 1),
          ("stat", 2),
          ("dyn", 3),
          ("dup", 4))
    )



class TmnxCBFClasses(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("be", 0),
          ("l2", 1),
          ("af", 2),
          ("l1", 3),
          ("h2", 4),
          ("ef", 5),
          ("h1", 6),
          ("nc", 7),
          ("defaultLsp", 8))
    )


class TmnxUrpfCheckMode(TextualConvention, Integer32):
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
        *(("strict", 1),
          ("loose", 2),
          ("strictNoEcmp", 3))
    )



class TmnxUserPassword(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )



class TmnxUdpPort(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class TmnxUuid(TextualConvention, OctetString):
    status = "current"
    displayHint = "4x-2x-2x-2x-6x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16



class TmnxSyslogFacility(TextualConvention, Integer32):
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
              18,
              19,
              20,
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("kernel", 0),
          ("user", 1),
          ("mail", 2),
          ("systemd", 3),
          ("auth", 4),
          ("syslogd", 5),
          ("printer", 6),
          ("netnews", 7),
          ("uucp", 8),
          ("cron", 9),
          ("authpriv", 10),
          ("ftp", 11),
          ("ntp", 12),
          ("logaudit", 13),
          ("logalert", 14),
          ("cron2", 15),
          ("local0", 16),
          ("local1", 17),
          ("local2", 18),
          ("local3", 19),
          ("local4", 20),
          ("local5", 21),
          ("local6", 22),
          ("local7", 23))
    )



class TmnxSyslogSeverity(TextualConvention, Integer32):
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
        *(("emergency", 0),
          ("alert", 1),
          ("critical", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("info", 6),
          ("debug", 7))
    )



class TmnxEvpnMultiHomingState(TextualConvention, Integer32):
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
        *(("disabled", 0),
          ("singleActive", 1),
          ("singleActiveNoEsiLabel", 2),
          ("allActive", 3))
    )



class TmnxBgpEvpnAcEthTag(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )



class TmnxL2tpTunnelGroupName(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )



class TmnxL2tpTunnelGroupNameOrEmpty(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )



class TFilterID(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class TIPFilterID(TFilterID):
    status = "current"


class TDHCPFilterID(TFilterID):
    status = "current"


class TEntryIdOrZero(TEntryIndicator):
    status = "current"
    subtypeSpec = TEntryIndicator.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class MciBoolean(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mciTrue", 1),
          ("mciFalse", 2))
    )



class TmnxPppCpState(TextualConvention, Integer32):
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
        *(("initial", 1),
          ("starting", 2),
          ("closed", 3),
          ("stopped", 4),
          ("closing", 5),
          ("stopping", 6),
          ("requestSent", 7),
          ("ackReceived", 8),
          ("ackSent", 9),
          ("opened", 10))
    )



class TmnxRipNgAuthType(TextualConvention, Integer32):
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
        *(("noAuthentication", 1),
          ("simplePassword", 2),
          ("md5", 3),
          ("md20", 4))
    )



class TmnxRipNgAuthKey(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



class TmnxAddressAndPrefixType(InetAddressType):
    status = "current"


class TmnxAddressAndPrefixAddress(InetAddress):
    status = "current"


class TmnxAddressAndPrefixPrefix(InetAddressPrefixLength):
    status = "current"


class TmnxIpv6AddressAndPrefixAddress(InetAddressIPv6):
    status = "current"


class TmnxIpv6AddressAndPrefixPrefix(InetAddressPrefixLength):
    status = "current"


class TmnxIpv4AddressAndMaskOrPrefixAddress(TextualConvention, IpAddress):
    status = "current"


class TmnxIpv4AddressAndMaskOrPrefixMask(TextualConvention, IpAddress):
    status = "current"


class TmnxIpv4AddressAndMaskOrPrefixPrefix(IpAddressPrefixLength):
    status = "current"


class TmnxIpv4AddressAndPrefixAddress(TextualConvention, IpAddress):
    status = "current"


class TmnxIpv4AddressAndPrefixPrefix(IpAddressPrefixLength):
    status = "current"


class TmnxIpv6AddressAndMaskOrPrefixAddress(InetAddressIPv6):
    status = "current"


class TmnxIpv6AddressAndMaskOrPrefixMask(InetAddressIPv6):
    status = "current"


class TmnxIpv6AddressAndMaskOrPrefixPrefix(InetAddressPrefixLength):
    status = "current"


class TmnxAddressAndMaskOrPrefixType(InetAddressType):
    status = "current"


class TmnxAddressAndMaskOrPrefixAddress(InetAddress):
    status = "current"


class TmnxAddressAndMaskOrPrefixPrefix(InetAddressPrefixLength):
    status = "current"


class TmnxAddressAndMaskOrPrefixMask(InetAddress):
    status = "current"


class TmnxAddressWithZoneType(InetAddressType):
    status = "current"


class TmnxAddressWithZoneAddress(InetAddress):
    status = "current"


class THsPirRate(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
        ValueRangeConstraint(4294967295, 4294967295),
    )



class THsPirRateOverride(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
        ValueRangeConstraint(4294967294, 4294967294),
        ValueRangeConstraint(4294967295, 4294967295),
    )



class THsSchedulerPolicyGroupId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )



class THsSchedulerPolicyWeight(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )



class THsSchedulerPolicyWeightOverride(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(1, 127),
    )



class TmnxWaveKey(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )



class TmnxSubBondingConnIdOrEmpty(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2),
    )



class TBurstLimitOverride(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 14000000),
    )



class TmnxEvpnMHEthSegStatus(TextualConvention, Integer32):
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
        *(("df", 1),
          ("ndf", 2),
          ("notesmanaged", 3))
    )



class TmnxVxlanInstance(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )



class TmnxSvcEvpnMplsTransportType(TextualConvention, Integer32):
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
        *(("invalid", 0),
          ("local", 1),
          ("static", 2),
          ("rsvp", 3),
          ("ldp", 4),
          ("ospf", 5),
          ("isis", 6),
          ("bgp", 7),
          ("srTe", 8),
          ("udp", 9),
          ("srPolicy", 10),
          ("mplsFwdPolicy", 11),
          ("ribApi", 12),
          ("srOspf3", 13))
    )



class TmnxMplsLabel(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 1048575),
    )



class TmnxMplsLabelOrZero(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(32, 1048575),
    )



class TmnxMplsLspBandwidth(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6400000),
    )



class TmnxVni(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )



class TmnxVniOrZero(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )



class PwPortIdOrZero(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 32767),
    )



class TmnxCliEngine(TextualConvention, Integer32):
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
        *(("classicCli", 1),
          ("mdCli", 2),
          ("systemDerived", 3))
    )



class TmnxRsvpSessionNameString(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )



class TmnxQosMdAutoPolicyID(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 65535),
    )



class TmnxQosMdAutoIDCount(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class TmnxNhgDownReason(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("nextHopNotResolved", 1),
          ("nextHopIsLocal", 3),
          ("nextHopIsMcast", 4),
          ("resTypeMismatch", 5))
    )



class TmnxQosRateHigh32(TmnxHigh32):
    status = "current"
    subtypeSpec = TmnxHigh32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(4294967295, 4294967295),
    )



class TmnxQosRateLow32(TmnxLow32):
    status = "current"
    subtypeSpec = TmnxLow32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class AluNgeKeygroupIdOrZero(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )



class TmnxEsaNum(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 16),
    )



class TmnxEsaVappNum(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4),
    )



class TPolRateTypeRefOrLocalLimit(TextualConvention, Integer32):
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
        *(("kbps", 1),
          ("percentLocalLimit", 2),
          ("percentReferPortLimit", 3))
    )



class TPolicerRateTypeWithRefLimit(TextualConvention, Integer32):
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
        *(("kbps", 1),
          ("percentPortLimit", 2),
          ("percentLocalLimit", 3),
          ("percentReferPortLimit", 4))
    )



class TWredSlopeProfile(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2),
          ("exceed", 4),
          ("inplus", 5))
    )



class TDEWredSlopeProfile(TextualConvention, Integer32):
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
        *(("in", 1),
          ("out", 2),
          ("de", 3),
          ("exceed", 4),
          ("inplus", 5))
    )



class TmnxFlexAlgoId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 255),
    )



class TmnxFlexAlgoIdOrZero(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(128, 255),
    )



class TmnxAlgorithmId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class TmnxTreeSidOwner(TextualConvention, Integer32):
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
          ("static", 1),
          ("pce", 2),
          ("srPol", 3))
    )



class TmnxTreeSidOrigin(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              20,
              30)
        )
    )
    namedValues = NamedValues(
        *(("pcep", 10),
          ("bgpSrPolicy", 20),
          ("configuration", 30))
    )



class TmnxMacMask(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6



class TmnxVeId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 65535),
    )



class TmnxMcIPsecDomainId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )



class TmnxMcIPsecDomainDesignatedRole(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("standby", 1),
          ("active", 2))
    )



class TmnxMcIPsecDomainAdjRmtDesignatedRole(TextualConvention, Integer32):
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
        *(("standby", 1),
          ("active", 2),
          ("unknown", 3))
    )



class TmnxSubHostSessionLimitOverride(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 131071),
    )



class TPlcyAcctPolicerId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )



class TPktByteOffset(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-8, -8),
        ValueRangeConstraint(-4, -4),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(8, 8),
    )



class TmnxAuthAlgorithm(TextualConvention, Integer32):
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
        *(("null", 1),
          ("md5", 2),
          ("sha1", 3),
          ("sha256", 4),
          ("sha384", 5),
          ("sha512", 6),
          ("aesXcbc", 7),
          ("authEncryption", 8))
    )



class TmnxEncrAlgorithm(TextualConvention, Integer32):
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("null", 1),
          ("des", 2),
          ("des3", 3),
          ("aes128", 4),
          ("aes192", 5),
          ("aes256", 6),
          ("aes128Gcm8", 7),
          ("aes128Gcm12", 8),
          ("aes128Gcm16", 9),
          ("aes192Gcm8", 10),
          ("aes192Gcm12", 11),
          ("aes192Gcm16", 12),
          ("aes256Gcm8", 13),
          ("aes256Gcm12", 14),
          ("aes256Gcm16", 15),
          ("nullAes128Gmac", 16),
          ("nullAes192Gmac", 17),
          ("nullAes256Gmac", 18))
    )



class TmnxIkePolicyDHGroupOrZero(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              5,
              14,
              15,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("unspecified", 0),
          ("group1", 1),
          ("group2", 2),
          ("group5", 5),
          ("group14", 14),
          ("group15", 15),
          ("group19", 19),
          ("group20", 20),
          ("group21", 21))
    )



class TmnxIPsecDirection(TextualConvention, Integer32):
    status = "current"
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



class TmnxIPsecKeyingType(TextualConvention, Integer32):
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
          ("manual", 1),
          ("dynamic", 2))
    )



class TDCpuProtPolicyType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accessNetwork", 1),
          ("port", 2))
    )



class TQosHwAggShaperSchedClass(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )



class TSrv6FunctionValue(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )



class TSrv6FunctionType(TextualConvention, Integer32):
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
          ("dynamic", 1),
          ("static", 2))
    )



class TSrv6FunctionErrorCode(TextualConvention, Integer32):
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
        *(("noError", 0),
          ("error", 1),
          ("noResource", 2),
          ("locAdminDown", 3),
          ("noIntConfig", 4),
          ("fpeOperDown", 5))
    )



class TSrv6Function(TextualConvention, Integer32):
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
        *(("end", 0),
          ("end-x", 1),
          ("end-dt4", 2),
          ("end-dt6", 3),
          ("end-dt46", 4),
          ("end-dx2", 5),
          ("end-dt2u", 6),
          ("end-dt2m", 7))
    )



class TSrv6EndpointBehavior(TextualConvention, Integer32):
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
              39)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("end", 1),
          ("endPsp", 2),
          ("endUsp", 3),
          ("endPspUsp", 4),
          ("endX", 5),
          ("endXPsp", 6),
          ("endXUsp", 7),
          ("endXPspUsp", 8),
          ("endT", 9),
          ("endTPsp", 10),
          ("endTUsp", 11),
          ("endTPspUsp", 12),
          ("endB6Encaps", 14),
          ("endBM", 15),
          ("endDX6", 16),
          ("endDX4", 17),
          ("endDT6", 18),
          ("endDT4", 19),
          ("endDT46", 20),
          ("endDX2", 21),
          ("endDX2V", 22),
          ("endDT2U", 23),
          ("endDT2M", 24),
          ("endB6EncapsRed", 27),
          ("endUsd", 28),
          ("endPspUsd", 29),
          ("endUspUsd", 30),
          ("endPspUspUsd", 31),
          ("endXUsd", 32),
          ("endXPspUsd", 33),
          ("endXUspUsd", 34),
          ("endXPspUspUsd", 35),
          ("endTUsd", 36),
          ("endTPspUsd", 37),
          ("endTUspUsd", 38),
          ("endTPspUspUsd", 39))
    )



class TFirBurstLimit(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 102400),
    )



class TSchedulerMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("vlanQos", 1))
    )



class TmnxPacketMode(TextualConvention, Integer32):
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
        *(("dataOtwOtw", 0),
          ("lmotwLmotwOtwAtm", 1),
          ("lmotwLmotwOtwNonAtm", 2),
          ("otwOtwOtw", 3),
          ("dataData", 4))
    )



class TmnxDPathDomainId(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6



class TmnxTacplusAccessOpType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("delete", 1))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-TC-MIB",
    **{"TmnxFPNumber": TmnxFPNumber,
       "TmnxFPNumberOrZero": TmnxFPNumberOrZero,
       "InterfaceIndex": InterfaceIndex,
       "TmnxPortID": TmnxPortID,
       "TmnxEncapVal": TmnxEncapVal,
       "QTag": QTag,
       "QTagOrZero": QTagOrZero,
       "QTagFullRange": QTagFullRange,
       "QTagFullRangeOrNone": QTagFullRangeOrNone,
       "TmnxSapAASubScope": TmnxSapAASubScope,
       "TmnxStrSapId": TmnxStrSapId,
       "IpAddressPrefixLength": IpAddressPrefixLength,
       "TmnxActionType": TmnxActionType,
       "TmnxAdminState": TmnxAdminState,
       "TmnxOperState": TmnxOperState,
       "TmnxStatus": TmnxStatus,
       "TmnxEnabledDisabledAdminState": TmnxEnabledDisabledAdminState,
       "TmnxEnabledDisabled": TmnxEnabledDisabled,
       "TmnxEnabledDisabledOrNA": TmnxEnabledDisabledOrNA,
       "TmnxEnabledDisabledOrInherit": TmnxEnabledDisabledOrInherit,
       "TmnxTimeInterval": TmnxTimeInterval,
       "TNamedItem": TNamedItem,
       "TNamedItemOrEmpty": TNamedItemOrEmpty,
       "TLNamedItem": TLNamedItem,
       "TLNamedItemOrEmpty": TLNamedItemOrEmpty,
       "TXLNamedItem": TXLNamedItem,
       "TXLNamedItemOrEmpty": TXLNamedItemOrEmpty,
       "TItemDescription": TItemDescription,
       "TItemLongDescription": TItemLongDescription,
       "TItemVeryLongDescription": TItemVeryLongDescription,
       "TRegularExpression": TRegularExpression,
       "TmnxHttpRedirectUrl": TmnxHttpRedirectUrl,
       "TmnxDisplayStringURL": TmnxDisplayStringURL,
       "TmnxVRtrID": TmnxVRtrID,
       "TmnxVRtrIDOrZero": TmnxVRtrIDOrZero,
       "VRtrIgmpHostMcRDstStatType": VRtrIgmpHostMcRDstStatType,
       "TmnxBgpAutonomousSystem": TmnxBgpAutonomousSystem,
       "TmnxBgpLocalPreference": TmnxBgpLocalPreference,
       "TmnxBgpPreference": TmnxBgpPreference,
       "TmnxCustId": TmnxCustId,
       "TmnxCustIdNoZero": TmnxCustIdNoZero,
       "BgpPeeringStatus": BgpPeeringStatus,
       "TmnxRipListenerStatus": TmnxRipListenerStatus,
       "TmnxServId": TmnxServId,
       "TmnxExtServId": TmnxExtServId,
       "TmnxAdminStateUpDown": TmnxAdminStateUpDown,
       "TmnxAdminStateTruthValue": TmnxAdminStateTruthValue,
       "TruthValueNoTypeTranslator": TruthValueNoTypeTranslator,
       "ServiceAdminStatus": ServiceAdminStatus,
       "ServiceOperStatus": ServiceOperStatus,
       "TPolicyID": TPolicyID,
       "TTmplPolicyID": TTmplPolicyID,
       "TQosIngressPolicyID": TQosIngressPolicyID,
       "TSapIngressPolicyID": TSapIngressPolicyID,
       "TSapEgressPolicyID": TSapEgressPolicyID,
       "TAnyQosPolicyID": TAnyQosPolicyID,
       "TAnyQosPolicyIDorZero": TAnyQosPolicyIDorZero,
       "TSdpIngressPolicyID": TSdpIngressPolicyID,
       "TSdpEgressPolicyID": TSdpEgressPolicyID,
       "TQosQGrpInstanceIDorZero": TQosQGrpInstanceIDorZero,
       "TmnxCreateOrigin": TmnxCreateOrigin,
       "TmnxBsxTransitIpPolicyId": TmnxBsxTransitIpPolicyId,
       "TmnxBsxTransitIpPolicyIdOrZero": TmnxBsxTransitIpPolicyIdOrZero,
       "TmnxBsxTransPrefPolicyId": TmnxBsxTransPrefPolicyId,
       "TmnxBsxTransPrefPolicyIdOrZero": TmnxBsxTransPrefPolicyIdOrZero,
       "TmnxBsxAarpId": TmnxBsxAarpId,
       "TmnxBsxAarpIdOrZero": TmnxBsxAarpIdOrZero,
       "TmnxBsxAarpServiceRefType": TmnxBsxAarpServiceRefType,
       "TmnxBsxIsaAaGroupIndexOrZero": TmnxBsxIsaAaGroupIndexOrZero,
       "TmnxBsxAaGrpPartIndexOrZero": TmnxBsxAaGrpPartIndexOrZero,
       "TmnxBsxAaSubHttpUrlParam": TmnxBsxAaSubHttpUrlParam,
       "TSapEgrEncapGrpQosPolicyIdOrZero": TSapEgrEncapGrpQosPolicyIdOrZero,
       "TSapEgrEncapGroupType": TSapEgrEncapGroupType,
       "TSapEgrEncapGroupActionType": TSapEgrEncapGroupActionType,
       "TPerPacketOffset": TPerPacketOffset,
       "TPerPacketOffsetOvr": TPerPacketOffsetOvr,
       "TIngressHsmdaPerPacketOffset": TIngressHsmdaPerPacketOffset,
       "TIngHsmdaPerPacketOffsetOvr": TIngHsmdaPerPacketOffsetOvr,
       "TEgressQPerPacketOffset": TEgressQPerPacketOffset,
       "TEgressPerPacketOffset": TEgressPerPacketOffset,
       "TEgressPerPacketOffsetOvr": TEgressPerPacketOffsetOvr,
       "TEgressHsmdaPerPacketOffset": TEgressHsmdaPerPacketOffset,
       "TEgrHsmdaPerPacketOffsetOvr": TEgrHsmdaPerPacketOffsetOvr,
       "TIngressQPerPacketOffset": TIngressQPerPacketOffset,
       "THsmdaCounterIdOrZero": THsmdaCounterIdOrZero,
       "THsmdaCounterIdOrZeroOrAll": THsmdaCounterIdOrZeroOrAll,
       "TIngressHsmdaCounterId": TIngressHsmdaCounterId,
       "TIngressHsmdaCounterIdOrZero": TIngressHsmdaCounterIdOrZero,
       "TEgressHsmdaCounterId": TEgressHsmdaCounterId,
       "TEgressHsmdaCounterIdOrZero": TEgressHsmdaCounterIdOrZero,
       "TEgrRateModType": TEgrRateModType,
       "TPolicyStatementName": TPolicyStatementName,
       "TPolicyStatementNameOrEmpty": TPolicyStatementNameOrEmpty,
       "TLPolicyStatementNameOrEmpty": TLPolicyStatementNameOrEmpty,
       "TLPolicyNameOrExpOrEmpty": TLPolicyNameOrExpOrEmpty,
       "TXLPolicyNameOrExpOrEmpty": TXLPolicyNameOrExpOrEmpty,
       "TmnxVcType": TmnxVcType,
       "TmnxVcId": TmnxVcId,
       "TmnxVcIdOrNone": TmnxVcIdOrNone,
       "DateAndTimeOrEmpty": DateAndTimeOrEmpty,
       "ClassIndex": ClassIndex,
       "ClassIndexOrNone": ClassIndexOrNone,
       "Dot1PPriority": Dot1PPriority,
       "Dot1PPriorityMask": Dot1PPriorityMask,
       "Dot1PPriorityNonZeroMask": Dot1PPriorityNonZeroMask,
       "ServiceAccessPoint": ServiceAccessPoint,
       "TLspExpValue": TLspExpValue,
       "TIpProtocol": TIpProtocol,
       "TIpProtocolNumber": TIpProtocolNumber,
       "TIpOption": TIpOption,
       "TIcmpTypeOrNone": TIcmpTypeOrNone,
       "TIcmpCodeOrNone": TIcmpCodeOrNone,
       "TTcpUdpPort": TTcpUdpPort,
       "TOperator": TOperator,
       "TTcpUdpPortOperator": TTcpUdpPortOperator,
       "TFrameType": TFrameType,
       "TQueueId": TQueueId,
       "TQueueIdOrAll": TQueueIdOrAll,
       "TIngressQueueId": TIngressQueueId,
       "TEgressQueueId": TEgressQueueId,
       "TIngressHsmdaQueueId": TIngressHsmdaQueueId,
       "TEgressHsmdaQueueId": TEgressHsmdaQueueId,
       "THsmdaSchedulerPolicyGroupId": THsmdaSchedulerPolicyGroupId,
       "THsmdaPolicyIncludeQueues": THsmdaPolicyIncludeQueues,
       "THsmdaPolicyScheduleClass": THsmdaPolicyScheduleClass,
       "TDSCPName": TDSCPName,
       "TDSCPNameOrEmpty": TDSCPNameOrEmpty,
       "TDSCPValue": TDSCPValue,
       "TDSCPValueOrNone": TDSCPValueOrNone,
       "TDSCPFilterActionValue": TDSCPFilterActionValue,
       "TFCName": TFCName,
       "TFCNameOrEmpty": TFCNameOrEmpty,
       "TFCSet": TFCSet,
       "TFCType": TFCType,
       "TFCTypeOrNone": TFCTypeOrNone,
       "TmnxTunnelType": TmnxTunnelType,
       "TmnxTunnelID": TmnxTunnelID,
       "TmnxBgpRouteTarget": TmnxBgpRouteTarget,
       "TmnxVPNRouteDistinguisher": TmnxVPNRouteDistinguisher,
       "SdpBindId": SdpBindId,
       "TmnxVRtrMplsLspID": TmnxVRtrMplsLspID,
       "TmnxVRtrMplsLspIDNoZero": TmnxVRtrMplsLspIDNoZero,
       "TPortSchedulerPIR": TPortSchedulerPIR,
       "TPortSchedulerAggRateLimitPIR": TPortSchedulerAggRateLimitPIR,
       "TPortSchedulerPIRRate": TPortSchedulerPIRRate,
       "TPortSchedulerCIR": TPortSchedulerCIR,
       "TPortQosPIRRate": TPortQosPIRRate,
       "TPortQosCIRRate": TPortQosCIRRate,
       "TWeight": TWeight,
       "TWeightOverride": TWeightOverride,
       "TNonZeroWeight": TNonZeroWeight,
       "TPolicerWeight": TPolicerWeight,
       "THsWrrWeightOvr": THsWrrWeightOvr,
       "THsClassWeightOverride": THsClassWeightOverride,
       "THsmdaWeight": THsmdaWeight,
       "THsmdaWrrWeight": THsmdaWrrWeight,
       "THsmdaWeightClass": THsmdaWeightClass,
       "THsmdaWeightOverride": THsmdaWeightOverride,
       "THsmdaWrrWeightOverride": THsmdaWrrWeightOverride,
       "TCIRRate": TCIRRate,
       "THPolCIRRate": THPolCIRRate,
       "TRateType": TRateType,
       "TBWRateType": TBWRateType,
       "TPSPRateType": TPSPRateType,
       "TPolicerRateType": TPolicerRateType,
       "TCIRRateOverride": TCIRRateOverride,
       "THPolCIRRateOverride": THPolCIRRateOverride,
       "TCIRPercentOverride": TCIRPercentOverride,
       "THsmdaCIRKRate": THsmdaCIRKRate,
       "THsmdaCIRKRateOverride": THsmdaCIRKRateOverride,
       "THsmdaCIRMRate": THsmdaCIRMRate,
       "THsmdaCIRMRateOverride": THsmdaCIRMRateOverride,
       "TPIRRate": TPIRRate,
       "THPolVirtualSchePIRRate": THPolVirtualSchePIRRate,
       "THPolVirtualScheCIRRate": THPolVirtualScheCIRRate,
       "TAdvCfgRate": TAdvCfgRate,
       "TMaxDecRate": TMaxDecRate,
       "THPolPIRRate": THPolPIRRate,
       "TSecondaryShaper10GPIRRate": TSecondaryShaper10GPIRRate,
       "TExpSecondaryShaperPIRRate": TExpSecondaryShaperPIRRate,
       "TExpSecondaryShaperClassRate": TExpSecondaryShaperClassRate,
       "TPIRRateOverride": TPIRRateOverride,
       "TPIRAggRateLimitOverride": TPIRAggRateLimitOverride,
       "THPolPIRRateOverride": THPolPIRRateOverride,
       "TPIRPercentOverride": TPIRPercentOverride,
       "TPIRRateOrZero": TPIRRateOrZero,
       "THsmdaPIRKRate": THsmdaPIRKRate,
       "THsmdaPIRKRateOverride": THsmdaPIRKRateOverride,
       "THsmdaPIRMRate": THsmdaPIRMRate,
       "THsmdaPIRMRateOverride": THsmdaPIRMRateOverride,
       "TmnxDHCP6MsgType": TmnxDHCP6MsgType,
       "TmnxDhcpClientState": TmnxDhcpClientState,
       "TmnxIgpInstance": TmnxIgpInstance,
       "TmnxOspfInstance": TmnxOspfInstance,
       "TmnxBGPFamilyType": TmnxBGPFamilyType,
       "TmnxIgmpGroupFilterMode": TmnxIgmpGroupFilterMode,
       "TmnxIgmpGroupType": TmnxIgmpGroupType,
       "TmnxIgmpSnpgGroupType": TmnxIgmpSnpgGroupType,
       "TmnxIgmpVersion": TmnxIgmpVersion,
       "TmnxMldGroupFilterMode": TmnxMldGroupFilterMode,
       "TmnxMldGroupType": TmnxMldGroupType,
       "TmnxMldVersion": TmnxMldVersion,
       "TmnxManagedRouteStatus": TmnxManagedRouteStatus,
       "TmnxTunnelTypeExt": TmnxTunnelTypeExt,
       "TmnxIgpSCFamilyType": TmnxIgpSCFamilyType,
       "TmnxAdjacencySetFamilyType": TmnxAdjacencySetFamilyType,
       "TmnxAncpString": TmnxAncpString,
       "TmnxAncpStringOrZero": TmnxAncpStringOrZero,
       "TmnxMulticastAddrFamily": TmnxMulticastAddrFamily,
       "TmnxNatIsaGrpId": TmnxNatIsaGrpId,
       "TmnxNatIsaGrpIdOrZero": TmnxNatIsaGrpIdOrZero,
       "TmnxNatL2AwAccessMode": TmnxNatL2AwAccessMode,
       "TmnxNatSubscriberType": TmnxNatSubscriberType,
       "TmnxNatSubscriberTypeOrNone": TmnxNatSubscriberTypeOrNone,
       "TmnxNatWaterMark": TmnxNatWaterMark,
       "TmnxAuthPassword": TmnxAuthPassword,
       "TmnxAsciiSpecification": TmnxAsciiSpecification,
       "TmnxMacSpecification": TmnxMacSpecification,
       "TmnxBinarySpecification": TmnxBinarySpecification,
       "TmnxDefSubIdSource": TmnxDefSubIdSource,
       "TmnxSubAuthPlcyUserNameOp": TmnxSubAuthPlcyUserNameOp,
       "TmnxSubCallingStationIdType": TmnxSubCallingStationIdType,
       "TmnxSubAcctSessionId": TmnxSubAcctSessionId,
       "TmnxSubHostGrouping": TmnxSubHostGrouping,
       "TmnxSubIdentString": TmnxSubIdentString,
       "TmnxSubIdentStringOrEmpty": TmnxSubIdentStringOrEmpty,
       "TmnxSubIdentShortString": TmnxSubIdentShortString,
       "TmnxSubRadServAlgorithm": TmnxSubRadServAlgorithm,
       "TmnxSubRadIsaServAlgorithm": TmnxSubRadIsaServAlgorithm,
       "TmnxSubRadiusAttrType": TmnxSubRadiusAttrType,
       "TmnxSubRadiusVendorId": TmnxSubRadiusVendorId,
       "TmnxSubRadiusDisplayString": TmnxSubRadiusDisplayString,
       "TmnxSubRadiusOctetString": TmnxSubRadiusOctetString,
       "TmnxSubSlaMode": TmnxSubSlaMode,
       "TmnxRadiusPendingReqLimit": TmnxRadiusPendingReqLimit,
       "TmnxRadiusServerOperState": TmnxRadiusServerOperState,
       "TmnxSubShcvAction": TmnxSubShcvAction,
       "TmnxSubShcvInterval": TmnxSubShcvInterval,
       "TmnxSubShcvRetryCount": TmnxSubShcvRetryCount,
       "TmnxSubShcvRetryTimeout": TmnxSubShcvRetryTimeout,
       "TmnxSubShcvSrcIpOrigin": TmnxSubShcvSrcIpOrigin,
       "TmnxSubSpiGroupId": TmnxSubSpiGroupId,
       "TmnxSubOperSpiGroupId": TmnxSubOperSpiGroupId,
       "TmnxReferenceBandwidth": TmnxReferenceBandwidth,
       "TmnxSubPfcpNodeIdType": TmnxSubPfcpNodeIdType,
       "TmnxSubPfcpNodeIdDomainName": TmnxSubPfcpNodeIdDomainName,
       "TmnxSubPfcpPeerNodeIdType": TmnxSubPfcpPeerNodeIdType,
       "TmnxSubPfcpCurrPeerNodeIdType": TmnxSubPfcpCurrPeerNodeIdType,
       "TmnxSubPoolName": TmnxSubPoolName,
       "TmnxSubProfileString": TmnxSubProfileString,
       "TmnxSubProfileStringOrEmpty": TmnxSubProfileStringOrEmpty,
       "TmnxSlaProfileString": TmnxSlaProfileString,
       "TmnxSlaProfileStringOrEmpty": TmnxSlaProfileStringOrEmpty,
       "TmnxAppProfileString": TmnxAppProfileString,
       "TmnxAppProfileStringOrEmpty": TmnxAppProfileStringOrEmpty,
       "TmnxSubMgtIntDestIdOrEmpty": TmnxSubMgtIntDestIdOrEmpty,
       "TmnxSubMgtIntDestId": TmnxSubMgtIntDestId,
       "TmnxDefInterDestIdSource": TmnxDefInterDestIdSource,
       "TmnxSubNasPortSuffixType": TmnxSubNasPortSuffixType,
       "TmnxSubNasPortPrefixType": TmnxSubNasPortPrefixType,
       "TmnxSubNasPortTypeType": TmnxSubNasPortTypeType,
       "TmnxSubCreditVolumeUnit": TmnxSubCreditVolumeUnit,
       "TmnxPccRuleFilterForwardAction": TmnxPccRuleFilterForwardAction,
       "TmnxPccRuleQosForwardAction": TmnxPccRuleQosForwardAction,
       "TmnxRadiusFramedRouteMetric": TmnxRadiusFramedRouteMetric,
       "TmnxRadiusFramedRoutePreference": TmnxRadiusFramedRoutePreference,
       "TmnxRadiusFramedRouteTag": TmnxRadiusFramedRouteTag,
       "TmnxSubMgtOrgStrOrZero": TmnxSubMgtOrgStrOrZero,
       "TmnxSubMgtOrgString": TmnxSubMgtOrgString,
       "TmnxFilterProfileStringOrEmpty": TmnxFilterProfileStringOrEmpty,
       "TmnxFpeId": TmnxFpeId,
       "TmnxFpeIdOrZero": TmnxFpeIdOrZero,
       "TmnxFpePathId": TmnxFpePathId,
       "TmnxAccessLoopEncapDataLink": TmnxAccessLoopEncapDataLink,
       "TmnxAccessLoopEncaps1": TmnxAccessLoopEncaps1,
       "TmnxAccessLoopEncaps2": TmnxAccessLoopEncaps2,
       "TmnxSubAleOffsetMode": TmnxSubAleOffsetMode,
       "TmnxSubAleOffset": TmnxSubAleOffset,
       "TmnxDataFormat": TmnxDataFormat,
       "TmnxDhcpOptionType": TmnxDhcpOptionType,
       "TmnxDhcpOptionDisplay": TmnxDhcpOptionDisplay,
       "TmnxDhcpServerDUIDTypeCode": TmnxDhcpServerDUIDTypeCode,
       "TmnxPppoeUserName": TmnxPppoeUserName,
       "TmnxPppoeUserNameOrEmpty": TmnxPppoeUserNameOrEmpty,
       "TCpmProtPolicyID": TCpmProtPolicyID,
       "TCpmProtPolicyIDOrDefault": TCpmProtPolicyIDOrDefault,
       "TMlpppQoSProfileId": TMlpppQoSProfileId,
       "TMcFrQoSProfileId": TMcFrQoSProfileId,
       "TmnxPppoeSessionId": TmnxPppoeSessionId,
       "TmnxPppoePadoDelay": TmnxPppoePadoDelay,
       "TmnxPppoeSessionInfoOrigin": TmnxPppoeSessionInfoOrigin,
       "TmnxPppoeSessionType": TmnxPppoeSessionType,
       "TmnxPppNcpProtocol": TmnxPppNcpProtocol,
       "TmnxDiamCcFailureHndlng": TmnxDiamCcFailureHndlng,
       "TmnxMlpppEpClass": TmnxMlpppEpClass,
       "TNetworkPolicyID": TNetworkPolicyID,
       "TItemScope": TItemScope,
       "TItemMatch": TItemMatch,
       "TPriority": TPriority,
       "TPriorityOrDefault": TPriorityOrDefault,
       "TPriorityOrUndefined": TPriorityOrUndefined,
       "TProfile": TProfile,
       "TProfileOrNone": TProfileOrNone,
       "TDEProfile": TDEProfile,
       "TEgressProfile": TEgressProfile,
       "TEgressProfileOrNone": TEgressProfileOrNone,
       "TAdaptationRule": TAdaptationRule,
       "TAdaptationRuleOverride": TAdaptationRuleOverride,
       "TRemarkType": TRemarkType,
       "TIngClassRemarkType": TIngClassRemarkType,
       "TPrecValue": TPrecValue,
       "TPrecValueOrNone": TPrecValueOrNone,
       "TCpmFilterBurstSize": TCpmFilterBurstSize,
       "TBurstSize": TBurstSize,
       "TBurstSizeOverride": TBurstSizeOverride,
       "TBurstSizeBytesOvr": TBurstSizeBytesOvr,
       "TBurstPercent": TBurstPercent,
       "TBurstHundredthsOfPercent": TBurstHundredthsOfPercent,
       "TBurstPercentOrDefault": TBurstPercentOrDefault,
       "TBurstPercentOrDefaultOverride": TBurstPercentOrDefaultOverride,
       "TRatePercent": TRatePercent,
       "TPIRRatePercent": TPIRRatePercent,
       "TLevel": TLevel,
       "TPortSchedLevel": TPortSchedLevel,
       "TLevelOrDefault": TLevelOrDefault,
       "TQueueMode": TQueueMode,
       "TQueueStatModeFormat": TQueueStatModeFormat,
       "TEntryIndicator": TEntryIndicator,
       "TEntryId": TEntryId,
       "TMatchCriteria": TMatchCriteria,
       "TmnxMdaQos": TmnxMdaQos,
       "TAtmTdpDescrType": TAtmTdpDescrType,
       "TDEValue": TDEValue,
       "TQGroupType": TQGroupType,
       "TQosOverrideType": TQosOverrideType,
       "TQosOverrideTypeId": TQosOverrideTypeId,
       "TmnxIPsecTunnelTemplateId": TmnxIPsecTunnelTemplateId,
       "TmnxIPsecTunnelTemplateIdOrZero": TmnxIPsecTunnelTemplateIdOrZero,
       "TmnxIpSecIsaOperFlags": TmnxIpSecIsaOperFlags,
       "TmnxIkePolicyAuthMethod": TmnxIkePolicyAuthMethod,
       "TmnxIkePolicyAutoEapMethod": TmnxIkePolicyAutoEapMethod,
       "TmnxIkePolicyAutoEapOwnMethod": TmnxIkePolicyAutoEapOwnMethod,
       "TmnxIkePolicyOwnAuthMethod": TmnxIkePolicyOwnAuthMethod,
       "TmnxRsvpDSTEClassType": TmnxRsvpDSTEClassType,
       "TmnxAccPlcyQICounters": TmnxAccPlcyQICounters,
       "TmnxAccPlcyQECounters": TmnxAccPlcyQECounters,
       "TmnxAccPlcyPolicerICounters": TmnxAccPlcyPolicerICounters,
       "TmnxAccPlcyPolicerECounters": TmnxAccPlcyPolicerECounters,
       "TmnxAccPlcyOICounters": TmnxAccPlcyOICounters,
       "TmnxAccPlcyOECounters": TmnxAccPlcyOECounters,
       "TmnxAccPlcyAACounters": TmnxAccPlcyAACounters,
       "TmnxAccPlcyAASubAttributes": TmnxAccPlcyAASubAttributes,
       "TmnxIsaBbGrpId": TmnxIsaBbGrpId,
       "TmnxIsaScalingProfile": TmnxIsaScalingProfile,
       "TmnxVdoGrpIdIndex": TmnxVdoGrpIdIndex,
       "TmnxVdoGrpId": TmnxVdoGrpId,
       "TmnxVdoGrpIdOrInherit": TmnxVdoGrpIdOrInherit,
       "TmnxVdoFccServerMode": TmnxVdoFccServerMode,
       "TmnxVdoPortNumber": TmnxVdoPortNumber,
       "TmnxVdoIfName": TmnxVdoIfName,
       "TmnxTimeInSec": TmnxTimeInSec,
       "TmnxReasContextVal": TmnxReasContextVal,
       "TmnxVdoStatInt": TmnxVdoStatInt,
       "TmnxVdoOutputFormat": TmnxVdoOutputFormat,
       "TmnxVdoAnalyzerAlarm": TmnxVdoAnalyzerAlarm,
       "TmnxVdoAnalyzerAlarmStates": TmnxVdoAnalyzerAlarmStates,
       "SvcISID": SvcISID,
       "TmnxISID": TmnxISID,
       "TIngPolicerId": TIngPolicerId,
       "TNetIngPolicerId": TNetIngPolicerId,
       "TNetIngPolicerIdOrNone": TNetIngPolicerIdOrNone,
       "TIngPolicerIdOrNone": TIngPolicerIdOrNone,
       "TIngressPolicerId": TIngressPolicerId,
       "TIngressPolicerIdOrNone": TIngressPolicerIdOrNone,
       "TIngDynPolicerIdOrNone": TIngDynPolicerIdOrNone,
       "TEgrPolicerId": TEgrPolicerId,
       "TEgrPolicerIdOrNone": TEgrPolicerIdOrNone,
       "TEgressPolicerId": TEgressPolicerId,
       "TEgressPolicerIdOrNone": TEgressPolicerIdOrNone,
       "TEgrDynPolicerIdOrNone": TEgrDynPolicerIdOrNone,
       "TEgrDynQueueIdOrNone": TEgrDynQueueIdOrNone,
       "TFIRRate": TFIRRate,
       "TBurstSizeBytes": TBurstSizeBytes,
       "THSMDABurstSizeBytes": THSMDABurstSizeBytes,
       "THSMDAQueueBurstLimit": THSMDAQueueBurstLimit,
       "TClassBurstLimit": TClassBurstLimit,
       "TNetIngPlcrBurstSizeBytes": TNetIngPlcrBurstSizeBytes,
       "TPlcrBurstSizeBytes": TPlcrBurstSizeBytes,
       "TBurstSizeBytesOverride": TBurstSizeBytesOverride,
       "TPolicerBurstSizeBytes": TPolicerBurstSizeBytes,
       "THSMDABurstSizeBytesOverride": THSMDABurstSizeBytesOverride,
       "TPlcrBurstSizeBytesOverride": TPlcrBurstSizeBytesOverride,
       "TPolicerBurstSizeBytesOverride": TPolicerBurstSizeBytesOverride,
       "TmnxBfdSessionProtocols": TmnxBfdSessionProtocols,
       "TmnxBfdSessOperState": TmnxBfdSessOperState,
       "TmnxBfdOnLspSessFecType": TmnxBfdOnLspSessFecType,
       "TmnxBfdSessProtocolState": TmnxBfdSessProtocolState,
       "TmnxBfdSessOperFlags": TmnxBfdSessOperFlags,
       "TmnxBfdTermination": TmnxBfdTermination,
       "TmnxIngPolicerStatMode": TmnxIngPolicerStatMode,
       "TmnxSapIngPolicerStatMode": TmnxSapIngPolicerStatMode,
       "TmnxNetIngPlcyPolicerStatMode": TmnxNetIngPlcyPolicerStatMode,
       "TmnxIngPolicerStatModeOverride": TmnxIngPolicerStatModeOverride,
       "TmnxEgrPolicerStatMode": TmnxEgrPolicerStatMode,
       "TmnxEgrPolicerStatModeOverride": TmnxEgrPolicerStatModeOverride,
       "TmnxTlsGroupId": TmnxTlsGroupId,
       "TSubHostId": TSubHostId,
       "TDirection": TDirection,
       "TDirectionIngEgr": TDirectionIngEgr,
       "TBurstLimit": TBurstLimit,
       "TMacFilterType": TMacFilterType,
       "TIPFilterType": TIPFilterType,
       "TmnxPwGlobalId": TmnxPwGlobalId,
       "TmnxPwGlobalIdOrZero": TmnxPwGlobalIdOrZero,
       "TmnxPwPathHopId": TmnxPwPathHopId,
       "TmnxPwPathHopIdOrZero": TmnxPwPathHopIdOrZero,
       "TmnxSpokeSdpId": TmnxSpokeSdpId,
       "TmnxSpokeSdpIdOrZero": TmnxSpokeSdpIdOrZero,
       "TmnxMsPwPeSignaling": TmnxMsPwPeSignaling,
       "TmnxLdpFECType": TmnxLdpFECType,
       "TmnxSvcOperGrpCreationOrigin": TmnxSvcOperGrpCreationOrigin,
       "TmnxOperGrpHoldUpTime": TmnxOperGrpHoldUpTime,
       "TmnxOperGrpHoldDownTime": TmnxOperGrpHoldDownTime,
       "TmnxSrrpPriorityStep": TmnxSrrpPriorityStep,
       "TmnxAiiType": TmnxAiiType,
       "TmnxSpbFid": TmnxSpbFid,
       "TmnxSpbFidOrZero": TmnxSpbFidOrZero,
       "TmnxSpbBridgePriority": TmnxSpbBridgePriority,
       "TmnxSlopeMap": TmnxSlopeMap,
       "TmnxCdrType": TmnxCdrType,
       "TmnxThresholdGroupType": TmnxThresholdGroupType,
       "TmnxVpnIpBackupFamily": TmnxVpnIpBackupFamily,
       "TmnxTunnelGroupId": TmnxTunnelGroupId,
       "TmnxTunnelGroupIdOrZero": TmnxTunnelGroupIdOrZero,
       "TmnxQosBytesHex": TmnxQosBytesHex,
       "TSiteOperStatus": TSiteOperStatus,
       "TmnxSpbFdbLocale": TmnxSpbFdbLocale,
       "TmnxSpbFdbState": TmnxSpbFdbState,
       "TmnxCdrDiagnosticAction": TmnxCdrDiagnosticAction,
       "TmnxLinkMapProfileId": TmnxLinkMapProfileId,
       "TmnxLinkMapProfileIdOrZero": TmnxLinkMapProfileIdOrZero,
       "TmnxDayOfWeek": TmnxDayOfWeek,
       "TmnxDayOfWeekList": TmnxDayOfWeekList,
       "TmnxMplsTpGlobalID": TmnxMplsTpGlobalID,
       "TmnxMplsTpNodeID": TmnxMplsTpNodeID,
       "TmnxMplsTpTunnelType": TmnxMplsTpTunnelType,
       "TmnxDistCpuProtPacketRateLimit": TmnxDistCpuProtPacketRateLimit,
       "TmnxDistCpuProtPacketPolicerRateLimit": TmnxDistCpuProtPacketPolicerRateLimit,
       "TmnxDistCpuProtRate": TmnxDistCpuProtRate,
       "TmnxDistCpuProtBurstSize": TmnxDistCpuProtBurstSize,
       "TmnxDistCpuProtActionDuration": TmnxDistCpuProtActionDuration,
       "TmnxDistCpuProtAction": TmnxDistCpuProtAction,
       "TmnxDistCpuProtEnforceType": TmnxDistCpuProtEnforceType,
       "TmnxDistCpuProtProtocolId": TmnxDistCpuProtProtocolId,
       "TmnxDistCpuProtRateType": TmnxDistCpuProtRateType,
       "TmnxDistCpuProtLogEventType": TmnxDistCpuProtLogEventType,
       "TmnxDistCpuProtState": TmnxDistCpuProtState,
       "TmnxIsidMFibStatus": TmnxIsidMFibStatus,
       "TmnxBfdIntfSessOperState": TmnxBfdIntfSessOperState,
       "TmnxBfdEncap": TmnxBfdEncap,
       "TLDisplayString": TLDisplayString,
       "IPv6FlowLabel": IPv6FlowLabel,
       "IPv6FlowLabelMask": IPv6FlowLabelMask,
       "TmnxWlanGwIsaGrpId": TmnxWlanGwIsaGrpId,
       "TmnxWlanGwIsaGrpIdOrZero": TmnxWlanGwIsaGrpIdOrZero,
       "TmnxMplsLdpNgIdType": TmnxMplsLdpNgIdType,
       "TmnxMplsLdpNgIdentifier": TmnxMplsLdpNgIdentifier,
       "TmnxMplsLsrNgIdentifier": TmnxMplsLsrNgIdentifier,
       "TmnxLagPerLinkHashClass": TmnxLagPerLinkHashClass,
       "TmnxLagPerLinkHashClassOrNone": TmnxLagPerLinkHashClassOrNone,
       "TmnxLagPerLinkHashWeight": TmnxLagPerLinkHashWeight,
       "BgpConnectRetryTime": BgpConnectRetryTime,
       "BgpHoldTime": BgpHoldTime,
       "TmnxInternalSchedWeightMode": TmnxInternalSchedWeightMode,
       "TmnxHigh32": TmnxHigh32,
       "TmnxLow32": TmnxLow32,
       "TQosQueuePIRRate": TQosQueuePIRRate,
       "TQosQueueCIRRate": TQosQueueCIRRate,
       "TQosQueuePIRRateOverride": TQosQueuePIRRateOverride,
       "TQosQueueCIRRateOverride": TQosQueueCIRRateOverride,
       "TResolveStatus": TResolveStatus,
       "LAGInterfaceNumber": LAGInterfaceNumber,
       "LAGInterfaceNumberOrZero": LAGInterfaceNumberOrZero,
       "TmnxRouteTargetOrigin": TmnxRouteTargetOrigin,
       "TmnxRouteDistType": TmnxRouteDistType,
       "TmnxScriptAuthType": TmnxScriptAuthType,
       "TmnxISIDNoZero": TmnxISIDNoZero,
       "TmnxSvcEvi": TmnxSvcEvi,
       "TmnxSecRadiusServAlgorithm": TmnxSecRadiusServAlgorithm,
       "TmnxSvcEviOrZero": TmnxSvcEviOrZero,
       "TmnxSubTerminationType": TmnxSubTerminationType,
       "TmnxSubTerminationTypeOrZero": TmnxSubTerminationTypeOrZero,
       "TmnxLongDisplayString": TmnxLongDisplayString,
       "TmnxLongDisplayStringToBinary": TmnxLongDisplayStringToBinary,
       "TmnxLongDisplayStringLegacyBinary": TmnxLongDisplayStringLegacyBinary,
       "TmnxProxyEntryType": TmnxProxyEntryType,
       "TmnxCBFClasses": TmnxCBFClasses,
       "TmnxUrpfCheckMode": TmnxUrpfCheckMode,
       "TmnxUserPassword": TmnxUserPassword,
       "TmnxUdpPort": TmnxUdpPort,
       "TmnxUuid": TmnxUuid,
       "TmnxSyslogFacility": TmnxSyslogFacility,
       "TmnxSyslogSeverity": TmnxSyslogSeverity,
       "TmnxEvpnMultiHomingState": TmnxEvpnMultiHomingState,
       "TmnxBgpEvpnAcEthTag": TmnxBgpEvpnAcEthTag,
       "TmnxL2tpTunnelGroupName": TmnxL2tpTunnelGroupName,
       "TmnxL2tpTunnelGroupNameOrEmpty": TmnxL2tpTunnelGroupNameOrEmpty,
       "TFilterID": TFilterID,
       "TIPFilterID": TIPFilterID,
       "TDHCPFilterID": TDHCPFilterID,
       "TEntryIdOrZero": TEntryIdOrZero,
       "MciBoolean": MciBoolean,
       "TmnxPppCpState": TmnxPppCpState,
       "TmnxRipNgAuthType": TmnxRipNgAuthType,
       "TmnxRipNgAuthKey": TmnxRipNgAuthKey,
       "TmnxAddressAndPrefixType": TmnxAddressAndPrefixType,
       "TmnxAddressAndPrefixAddress": TmnxAddressAndPrefixAddress,
       "TmnxAddressAndPrefixPrefix": TmnxAddressAndPrefixPrefix,
       "TmnxIpv6AddressAndPrefixAddress": TmnxIpv6AddressAndPrefixAddress,
       "TmnxIpv6AddressAndPrefixPrefix": TmnxIpv6AddressAndPrefixPrefix,
       "TmnxIpv4AddressAndMaskOrPrefixAddress": TmnxIpv4AddressAndMaskOrPrefixAddress,
       "TmnxIpv4AddressAndMaskOrPrefixMask": TmnxIpv4AddressAndMaskOrPrefixMask,
       "TmnxIpv4AddressAndMaskOrPrefixPrefix": TmnxIpv4AddressAndMaskOrPrefixPrefix,
       "TmnxIpv4AddressAndPrefixAddress": TmnxIpv4AddressAndPrefixAddress,
       "TmnxIpv4AddressAndPrefixPrefix": TmnxIpv4AddressAndPrefixPrefix,
       "TmnxIpv6AddressAndMaskOrPrefixAddress": TmnxIpv6AddressAndMaskOrPrefixAddress,
       "TmnxIpv6AddressAndMaskOrPrefixMask": TmnxIpv6AddressAndMaskOrPrefixMask,
       "TmnxIpv6AddressAndMaskOrPrefixPrefix": TmnxIpv6AddressAndMaskOrPrefixPrefix,
       "TmnxAddressAndMaskOrPrefixType": TmnxAddressAndMaskOrPrefixType,
       "TmnxAddressAndMaskOrPrefixAddress": TmnxAddressAndMaskOrPrefixAddress,
       "TmnxAddressAndMaskOrPrefixPrefix": TmnxAddressAndMaskOrPrefixPrefix,
       "TmnxAddressAndMaskOrPrefixMask": TmnxAddressAndMaskOrPrefixMask,
       "TmnxAddressWithZoneType": TmnxAddressWithZoneType,
       "TmnxAddressWithZoneAddress": TmnxAddressWithZoneAddress,
       "THsPirRate": THsPirRate,
       "THsPirRateOverride": THsPirRateOverride,
       "THsSchedulerPolicyGroupId": THsSchedulerPolicyGroupId,
       "THsSchedulerPolicyWeight": THsSchedulerPolicyWeight,
       "THsSchedulerPolicyWeightOverride": THsSchedulerPolicyWeightOverride,
       "TmnxWaveKey": TmnxWaveKey,
       "TmnxSubBondingConnIdOrEmpty": TmnxSubBondingConnIdOrEmpty,
       "TBurstLimitOverride": TBurstLimitOverride,
       "TmnxEvpnMHEthSegStatus": TmnxEvpnMHEthSegStatus,
       "TmnxVxlanInstance": TmnxVxlanInstance,
       "TmnxSvcEvpnMplsTransportType": TmnxSvcEvpnMplsTransportType,
       "TmnxMplsLabel": TmnxMplsLabel,
       "TmnxMplsLabelOrZero": TmnxMplsLabelOrZero,
       "TmnxMplsLspBandwidth": TmnxMplsLspBandwidth,
       "TmnxVni": TmnxVni,
       "TmnxVniOrZero": TmnxVniOrZero,
       "PwPortIdOrZero": PwPortIdOrZero,
       "TmnxCliEngine": TmnxCliEngine,
       "TmnxRsvpSessionNameString": TmnxRsvpSessionNameString,
       "TmnxQosMdAutoPolicyID": TmnxQosMdAutoPolicyID,
       "TmnxQosMdAutoIDCount": TmnxQosMdAutoIDCount,
       "TmnxNhgDownReason": TmnxNhgDownReason,
       "TmnxQosRateHigh32": TmnxQosRateHigh32,
       "TmnxQosRateLow32": TmnxQosRateLow32,
       "AluNgeKeygroupIdOrZero": AluNgeKeygroupIdOrZero,
       "TmnxEsaNum": TmnxEsaNum,
       "TmnxEsaVappNum": TmnxEsaVappNum,
       "TPolRateTypeRefOrLocalLimit": TPolRateTypeRefOrLocalLimit,
       "TPolicerRateTypeWithRefLimit": TPolicerRateTypeWithRefLimit,
       "TWredSlopeProfile": TWredSlopeProfile,
       "TDEWredSlopeProfile": TDEWredSlopeProfile,
       "TmnxFlexAlgoId": TmnxFlexAlgoId,
       "TmnxFlexAlgoIdOrZero": TmnxFlexAlgoIdOrZero,
       "TmnxAlgorithmId": TmnxAlgorithmId,
       "TmnxTreeSidOwner": TmnxTreeSidOwner,
       "TmnxTreeSidOrigin": TmnxTreeSidOrigin,
       "TmnxMacMask": TmnxMacMask,
       "TmnxVeId": TmnxVeId,
       "TmnxMcIPsecDomainId": TmnxMcIPsecDomainId,
       "TmnxMcIPsecDomainDesignatedRole": TmnxMcIPsecDomainDesignatedRole,
       "TmnxMcIPsecDomainAdjRmtDesignatedRole": TmnxMcIPsecDomainAdjRmtDesignatedRole,
       "TmnxSubHostSessionLimitOverride": TmnxSubHostSessionLimitOverride,
       "TPlcyAcctPolicerId": TPlcyAcctPolicerId,
       "TPktByteOffset": TPktByteOffset,
       "TmnxAuthAlgorithm": TmnxAuthAlgorithm,
       "TmnxEncrAlgorithm": TmnxEncrAlgorithm,
       "TmnxIkePolicyDHGroupOrZero": TmnxIkePolicyDHGroupOrZero,
       "TmnxIPsecDirection": TmnxIPsecDirection,
       "TmnxIPsecKeyingType": TmnxIPsecKeyingType,
       "TDCpuProtPolicyType": TDCpuProtPolicyType,
       "TQosHwAggShaperSchedClass": TQosHwAggShaperSchedClass,
       "TSrv6FunctionValue": TSrv6FunctionValue,
       "TSrv6FunctionType": TSrv6FunctionType,
       "TSrv6FunctionErrorCode": TSrv6FunctionErrorCode,
       "TSrv6Function": TSrv6Function,
       "TSrv6EndpointBehavior": TSrv6EndpointBehavior,
       "TFirBurstLimit": TFirBurstLimit,
       "TSchedulerMode": TSchedulerMode,
       "TmnxPacketMode": TmnxPacketMode,
       "TmnxDPathDomainId": TmnxDPathDomainId,
       "TmnxTacplusAccessOpType": TmnxTacplusAccessOpType,
       "timetraTCMIBModule": timetraTCMIBModule}
)
