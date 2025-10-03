# SNMP MIB module (CM-COMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\adva\CM-COMMON-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:15:04 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

cmCommonMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1)
)
if mibBuilder.loadTexts:
    cmCommonMIB.setRevisions(
        ("2021-01-27 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PortType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eth-access", 1),
          ("eth-network", 2))
    )



class TrafficDirection(TextualConvention, Integer32):
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
        *(("a2n", 1),
          ("n2a", 2),
          ("ingress", 3),
          ("egress", 4),
          ("n2n", 5))
    )



class VlanId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )



class VlanPriority(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



class VlanTagType(TextualConvention, Integer32):
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
        *(("inner-vlantag", 1),
          ("outer-vlantag", 2),
          ("n2a-priorityMapping", 3),
          ("mplsLabel", 4),
          ("vcLabel", 5),
          ("encapOuterVlanTag", 6))
    )



class AdminState(TextualConvention, Integer32):
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
        *(("in-service", 1),
          ("management", 2),
          ("maintenance", 3),
          ("disabled", 4),
          ("unassigned", 5),
          ("monitored", 6))
    )



class OperationalState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("outage", 2))
    )



class SecondaryState(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("not-applicable", 0),
          ("active", 1),
          ("automaticinservice", 2),
          ("facilityfailure", 3),
          ("fault", 4),
          ("loopback", 5),
          ("maintenance", 6),
          ("mismatchedeqpt", 7),
          ("standbyhot", 8),
          ("supportingentityoutage", 9),
          ("unassigned", 10),
          ("unequipped", 11),
          ("disabled", 12),
          ("forcedoffline", 13),
          ("initializing", 14),
          ("prtcl", 15),
          ("blckd", 16),
          ("mon-tx", 17),
          ("mir-rx", 18),
          ("cema", 19),
          ("lkdo", 20),
          ("nomber", 21))
    )


class EthernetPortSpeed(TextualConvention, Integer32):
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
              21)
        )
    )
    namedValues = NamedValues(
        *(("speed-unknown", 0),
          ("speed-10MB-full", 1),
          ("speed-10MB-half", 2),
          ("speed-100MB-full", 3),
          ("speed-100MB-half", 4),
          ("speed-1000MB-full", 5),
          ("speed-1000MB-half", 6),
          ("speed-auto", 7),
          ("speed-auto-10MB-full", 8),
          ("speed-auto-10MB-half", 9),
          ("speed-auto-100MB-full", 10),
          ("speed-auto-100MB-half", 11),
          ("speed-auto-1000MB-full", 12),
          ("speed-auto-1000MB-half", 13),
          ("speed-negotiating", 14),
          ("speed-auto-1000MB-full-master", 15),
          ("speed-auto-1000MB-full-slave", 16),
          ("speed-none", 17),
          ("speed-auto-1000MB-full-master-preferred", 18),
          ("speed-auto-1000MB-full-slave-preferred", 19),
          ("speed-10G-full", 20),
          ("speed-auto-detect", 21))
    )



class EthernetMediaType(TextualConvention, Integer32):
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
        *(("not-applicable", 0),
          ("copper", 1),
          ("fiber", 2),
          ("coppersfp", 3),
          ("auto", 4),
          ("none", 5),
          ("xdsl", 6),
          ("vmServerBackplane", 7))
    )



class PerfCounter64(TextualConvention, Counter64):
    status = "current"


class PerfCounter32(TextualConvention, Counter32):
    status = "current"


class IpVersion(TextualConvention, Integer32):
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



class IpPriorityMapMode(TextualConvention, Integer32):
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
        *(("not-applicable", 0),
          ("none", 1),
          ("priomap-tos", 2),
          ("priomap-dscp", 3))
    )



class PriorityMapMode(TextualConvention, Integer32):
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
        *(("priomap-none", 1),
          ("priomap-tos", 2),
          ("priomap-dscp", 3),
          ("priomap-8021p", 4),
          ("priomap-8021p-inner", 5),
          ("priomap-exp", 6),
          ("priomap-exp-inner", 7))
    )



class SfpConnectorValue(TextualConvention, Integer32):
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 0),
          ("unknown", 1),
          ("sc", 2),
          ("fcs1cu", 3),
          ("fcs2cu", 4),
          ("bnc-tnc", 5),
          ("fccoaxhdr", 6),
          ("fjack", 7),
          ("lc", 8),
          ("mt-rj", 9),
          ("mu", 10),
          ("sg", 11),
          ("optpigtail", 12),
          ("hssdc", 13),
          ("cupigtail", 14),
          ("vendorspecific", 15),
          ("rj45", 16))
    )



class SfpIdentifierValue(TextualConvention, Integer32):
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("unknown", 1),
          ("gbic", 2),
          ("modsol", 3),
          ("sfp", 4),
          ("xbi300pin", 5),
          ("xenpak", 6),
          ("xfp", 7),
          ("xff", 8),
          ("xfpE", 9),
          ("xpak", 10),
          ("x2", 11),
          ("vendorSpecific", 12))
    )



class RestartType(TextualConvention, Integer32):
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
        *(("not-applicable", 0),
          ("warm-start", 1),
          ("cold-start", 2),
          ("boot-maintenance", 3),
          ("boot-normal", 4),
          ("boot-pxe", 5))
    )



class SfpMediaType(TextualConvention, Integer32):
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
        *(("not-applicable", 0),
          ("singlemode", 1),
          ("multimode", 2),
          ("multimode62-5", 3),
          ("copper", 4))
    )



class ScheduleType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("periodic", 1),
          ("one-shot", 2))
    )



class SchedActivityStatus(TextualConvention, Integer32):
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
        *(("initial", 1),
          ("active", 2),
          ("suspended", 3),
          ("completed", 4))
    )



class SchedActivityAction(TextualConvention, Integer32):
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
        *(("not-applicable", 0),
          ("suspend", 1),
          ("resume", 2))
    )



class MepDestinationType(TextualConvention, Integer32):
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
        *(("not-applicable", 0),
          ("mepid", 1),
          ("macaddress", 2))
    )



class ClassOfServiceType(TextualConvention, Integer32):
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
        *(("cos-not-applicable", 0),
          ("cos-zero", 1),
          ("cos-one", 2),
          ("cos-two", 3),
          ("cos-three", 4),
          ("cos-four", 5),
          ("cos-five", 6),
          ("cos-six", 7),
          ("cos-seven", 8))
    )



class SignalDirectionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2))
    )



class AfpTagControl(TextualConvention, Integer32):
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
        *(("ctag", 1),
          ("stag", 2),
          ("both", 3))
    )



class CmP2PFlowType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("eline", 1)
    )



class CmTrafficACLPriorityType(TextualConvention, Integer32):
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
          ("acl-tos", 1),
          ("acl-dscp", 2))
    )



class CmTrafficAclFilterActionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )



class CmTrafficAclFilterType(TextualConvention, Integer32):
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
        *(("mac", 1),
          ("ipv4", 2),
          ("ipv6", 3))
    )



class CmTrafficAclProtocolType(TextualConvention, Integer32):
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
          ("tcp", 1),
          ("udp", 2))
    )



class VlanEthertype(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cvlan", 1),
          ("svlan", 2))
    )



class CmPmBinAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 0),
          ("clear", 1))
    )



class CmPmIntervalType(TextualConvention, Integer32):
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
        *(("interval-15min", 1),
          ("interval-1day", 2),
          ("rollover", 3),
          ("interval-5min", 4))
    )



class TDMFrequencySourceType(TextualConvention, Integer32):
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
          ("loopTiming", 1),
          ("systemTiming", 2),
          ("lineTiming", 3))
    )



class F3DisplayString(TextualConvention, OctetString):
    status = "current"
    displayHint = "2047a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2047),
    )



class Decimal32(TextualConvention, Unsigned32):
    status = "current"


class UserInterfaceType(TextualConvention, Integer32):
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
        *(("cli", 1),
          ("gui", 2),
          ("netconf", 3),
          ("snmp", 4))
    )



class FlowSecState(TextualConvention, Integer32):
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
        *(("secureNormal", 1),
          ("secureBlocked", 2),
          ("unsecureNormal", 3),
          ("unsecureBlocked", 4))
    )



class UsbOperationalMode(TextualConvention, Integer32):
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
        *(("cellular-modem", 1),
          ("srv-access", 2),
          ("nte-access", 3))
    )



# MIB Managed Objects in the order of their OIDs

_Subproducts_ObjectIdentity = ObjectIdentity
subproducts = _Subproducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1)
)
_Nemihubshelf_ObjectIdentity = ObjectIdentity
nemihubshelf = _Nemihubshelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 1)
)
_Ge101_ObjectIdentity = ObjectIdentity
ge101 = _Ge101_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 2)
)
_Ge206_ObjectIdentity = ObjectIdentity
ge206 = _Ge206_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 3)
)
_Ge201_ObjectIdentity = ObjectIdentity
ge201 = _Ge201_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 4)
)
_Ge201se_ObjectIdentity = ObjectIdentity
ge201se = _Ge201se_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 5)
)
_Ge206f_ObjectIdentity = ObjectIdentity
ge206f = _Ge206f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 6)
)
_Cmagg_ObjectIdentity = ObjectIdentity
cmagg = _Cmagg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 7)
)
_Ge112_ObjectIdentity = ObjectIdentity
ge112 = _Ge112_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 8)
)
_Ge114_ObjectIdentity = ObjectIdentity
ge114 = _Ge114_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 9)
)
_Ge206v_ObjectIdentity = ObjectIdentity
ge206v = _Ge206v_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 10)
)
_Xg210_ObjectIdentity = ObjectIdentity
xg210 = _Xg210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 11)
)
_T1804_ObjectIdentity = ObjectIdentity
t1804 = _T1804_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 12)
)
_T3204_ObjectIdentity = ObjectIdentity
t3204 = _T3204_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 13)
)
_Gesyncprobe_ObjectIdentity = ObjectIdentity
gesyncprobe = _Gesyncprobe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 14)
)
_Ge114H_ObjectIdentity = ObjectIdentity
ge114H = _Ge114H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 15)
)
_Ge114PH_ObjectIdentity = ObjectIdentity
ge114PH = _Ge114PH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 16)
)
_Ge114S_ObjectIdentity = ObjectIdentity
ge114S = _Ge114S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 17)
)
_Ge114SH_ObjectIdentity = ObjectIdentity
ge114SH = _Ge114SH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 18)
)
_Sh1pcs_ObjectIdentity = ObjectIdentity
sh1pcs = _Sh1pcs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 19)
)
_Ge112Pro_ObjectIdentity = ObjectIdentity
ge112Pro = _Ge112Pro_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 20)
)
_Ge112ProM_ObjectIdentity = ObjectIdentity
ge112ProM = _Ge112ProM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 21)
)
_Ge114Pro_ObjectIdentity = ObjectIdentity
ge114Pro = _Ge114Pro_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 22)
)
_Ge114ProC_ObjectIdentity = ObjectIdentity
ge114ProC = _Ge114ProC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 23)
)
_Ge114ProSH_ObjectIdentity = ObjectIdentity
ge114ProSH = _Ge114ProSH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 24)
)
_Ge114ProCSH_ObjectIdentity = ObjectIdentity
ge114ProCSH = _Ge114ProCSH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 25)
)
_Ge114ProHE_ObjectIdentity = ObjectIdentity
ge114ProHE = _Ge114ProHE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 26)
)
_Xg210c_ObjectIdentity = ObjectIdentity
xg210c = _Xg210c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 27)
)
_Ge112ProH_ObjectIdentity = ObjectIdentity
ge112ProH = _Ge112ProH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 28)
)
_Ge114G_ObjectIdentity = ObjectIdentity
ge114G = _Ge114G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 29)
)
_Ge114ProVMH_ObjectIdentity = ObjectIdentity
ge114ProVMH = _Ge114ProVMH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 30)
)
_Ge114ProVMCH_ObjectIdentity = ObjectIdentity
ge114ProVMCH = _Ge114ProVMCH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 31)
)
_Ge114ProVMCSH_ObjectIdentity = ObjectIdentity
ge114ProVMCSH = _Ge114ProVMCSH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 32)
)
_Ge112ProVM_ObjectIdentity = ObjectIdentity
ge112ProVM = _Ge112ProVM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 33)
)
_Ge101Pro_ObjectIdentity = ObjectIdentity
ge101Pro = _Ge101Pro_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 34)
)
_Go102ProS_ObjectIdentity = ObjectIdentity
go102ProS = _Go102ProS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 35)
)
_Go102ProSP_ObjectIdentity = ObjectIdentity
go102ProSP = _Go102ProSP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 36)
)
_Cx101Pro30A_ObjectIdentity = ObjectIdentity
cx101Pro30A = _Cx101Pro30A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 37)
)
_Cx102Pro30A_ObjectIdentity = ObjectIdentity
cx102Pro30A = _Cx102Pro30A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 38)
)
_Xg116Pro_ObjectIdentity = ObjectIdentity
xg116Pro = _Xg116Pro_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 39)
)
_Xg120Pro_ObjectIdentity = ObjectIdentity
xg120Pro = _Xg120Pro_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 40)
)
_Xg116ProH_ObjectIdentity = ObjectIdentity
xg116ProH = _Xg116ProH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 41)
)
_Ge102ProH_ObjectIdentity = ObjectIdentity
ge102ProH = _Ge102ProH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 42)
)
_Ge102ProEFMH_ObjectIdentity = ObjectIdentity
ge102ProEFMH = _Ge102ProEFMH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 43)
)
_Go102ProSM_ObjectIdentity = ObjectIdentity
go102ProSM = _Go102ProSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 44)
)
_Xg118ProSH_ObjectIdentity = ObjectIdentity
xg118ProSH = _Xg118ProSH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 45)
)
_Xg118ProacSH_ObjectIdentity = ObjectIdentity
xg118ProacSH = _Xg118ProacSH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 46)
)
_Ge114ProVMSH_ObjectIdentity = ObjectIdentity
ge114ProVMSH = _Ge114ProVMSH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 47)
)
_Ge104_ObjectIdentity = ObjectIdentity
ge104 = _Ge104_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 48)
)
_Xg120ProSH_ObjectIdentity = ObjectIdentity
xg120ProSH = _Xg120ProSH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 49)
)
_F3Capabilities_ObjectIdentity = ObjectIdentity
f3Capabilities = _F3Capabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CM-COMMON-MIB",
    **{"PortType": PortType,
       "TrafficDirection": TrafficDirection,
       "VlanId": VlanId,
       "VlanPriority": VlanPriority,
       "VlanTagType": VlanTagType,
       "AdminState": AdminState,
       "OperationalState": OperationalState,
       "SecondaryState": SecondaryState,
       "EthernetPortSpeed": EthernetPortSpeed,
       "EthernetMediaType": EthernetMediaType,
       "PerfCounter64": PerfCounter64,
       "PerfCounter32": PerfCounter32,
       "IpVersion": IpVersion,
       "IpPriorityMapMode": IpPriorityMapMode,
       "PriorityMapMode": PriorityMapMode,
       "SfpConnectorValue": SfpConnectorValue,
       "SfpIdentifierValue": SfpIdentifierValue,
       "RestartType": RestartType,
       "SfpMediaType": SfpMediaType,
       "ScheduleType": ScheduleType,
       "SchedActivityStatus": SchedActivityStatus,
       "SchedActivityAction": SchedActivityAction,
       "MepDestinationType": MepDestinationType,
       "ClassOfServiceType": ClassOfServiceType,
       "SignalDirectionType": SignalDirectionType,
       "AfpTagControl": AfpTagControl,
       "CmP2PFlowType": CmP2PFlowType,
       "CmTrafficACLPriorityType": CmTrafficACLPriorityType,
       "CmTrafficAclFilterActionType": CmTrafficAclFilterActionType,
       "CmTrafficAclFilterType": CmTrafficAclFilterType,
       "CmTrafficAclProtocolType": CmTrafficAclProtocolType,
       "VlanEthertype": VlanEthertype,
       "CmPmBinAction": CmPmBinAction,
       "CmPmIntervalType": CmPmIntervalType,
       "TDMFrequencySourceType": TDMFrequencySourceType,
       "F3DisplayString": F3DisplayString,
       "Decimal32": Decimal32,
       "UserInterfaceType": UserInterfaceType,
       "FlowSecState": FlowSecState,
       "UsbOperationalMode": UsbOperationalMode,
       "cmCommonMIB": cmCommonMIB,
       "subproducts": subproducts,
       "nemihubshelf": nemihubshelf,
       "ge101": ge101,
       "ge206": ge206,
       "ge201": ge201,
       "ge201se": ge201se,
       "ge206f": ge206f,
       "cmagg": cmagg,
       "ge112": ge112,
       "ge114": ge114,
       "ge206v": ge206v,
       "xg210": xg210,
       "t1804": t1804,
       "t3204": t3204,
       "gesyncprobe": gesyncprobe,
       "ge114H": ge114H,
       "ge114PH": ge114PH,
       "ge114S": ge114S,
       "ge114SH": ge114SH,
       "sh1pcs": sh1pcs,
       "ge112Pro": ge112Pro,
       "ge112ProM": ge112ProM,
       "ge114Pro": ge114Pro,
       "ge114ProC": ge114ProC,
       "ge114ProSH": ge114ProSH,
       "ge114ProCSH": ge114ProCSH,
       "ge114ProHE": ge114ProHE,
       "xg210c": xg210c,
       "ge112ProH": ge112ProH,
       "ge114G": ge114G,
       "ge114ProVMH": ge114ProVMH,
       "ge114ProVMCH": ge114ProVMCH,
       "ge114ProVMCSH": ge114ProVMCSH,
       "ge112ProVM": ge112ProVM,
       "ge101Pro": ge101Pro,
       "go102ProS": go102ProS,
       "go102ProSP": go102ProSP,
       "cx101Pro30A": cx101Pro30A,
       "cx102Pro30A": cx102Pro30A,
       "xg116Pro": xg116Pro,
       "xg120Pro": xg120Pro,
       "xg116ProH": xg116ProH,
       "ge102ProH": ge102ProH,
       "ge102ProEFMH": ge102ProEFMH,
       "go102ProSM": go102ProSM,
       "xg118ProSH": xg118ProSH,
       "xg118ProacSH": xg118ProacSH,
       "ge114ProVMSH": ge114ProVMSH,
       "ge104": ge104,
       "xg120ProSH": xg120ProSH,
       "f3Capabilities": f3Capabilities}
)
