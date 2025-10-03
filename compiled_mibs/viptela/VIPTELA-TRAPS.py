# SNMP MIB module (VIPTELA-TRAPS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\viptela\VIPTELA-TRAPS
# Produced by pysmi-1.6.2 at Thu Oct  2 12:34:10 2025
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
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(viptela,) = mibBuilder.importSymbols(
    "VIPTELA-GLOBAL",
    "viptela")


# MODULE-IDENTITY

viptela_traps = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 100)
)
if mibBuilder.loadTexts:
    viptela_traps.setRevisions(
        ("2020-07-01 00:00",
         "2020-02-24 00:00",
         "2019-11-15 00:00",
         "2019-08-15 00:00",
         "2018-11-01 00:00",
         "2018-08-20 00:00",
         "2018-06-25 00:00",
         "2018-04-25 00:00",
         "2018-03-15 00:00",
         "2018-01-16 00:00",
         "2017-11-01 00:00",
         "2017-08-01 00:00",
         "2017-05-25 00:00",
         "2017-04-06 00:00",
         "2017-02-15 00:00",
         "2017-02-06 00:00",
         "2016-11-16 00:00",
         "2016-10-25 00:00",
         "2016-10-24 00:00",
         "2016-08-10 00:00",
         "2016-08-01 00:00",
         "2016-06-09 00:00",
         "2016-04-22 00:00",
         "2016-03-15 00:00",
         "2016-01-30 00:00",
         "2015-12-28 00:00",
         "2015-12-01 00:00",
         "2015-10-31 00:00",
         "2015-09-27 00:00",
         "2015-09-01 00:00",
         "2015-07-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class NetconfNotificationSeverity(TextualConvention, Integer32):
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
        *(("critical", 1),
          ("major", 2),
          ("minor", 3))
    )



class DomainId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class UnsignedByte(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class ColorEnum(TextualConvention, Integer32):
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("mpls", 2),
          ("metro-ethernet", 3),
          ("biz-internet", 4),
          ("public-internet", 5),
          ("lte", 6),
          ("threeG", 7),
          ("red", 8),
          ("green", 9),
          ("blue", 10),
          ("gold", 11),
          ("silver", 12),
          ("bronze", 13),
          ("custom1", 14),
          ("custom2", 15),
          ("custom3", 16),
          ("private1", 17),
          ("private2", 18),
          ("private3", 19),
          ("private4", 20),
          ("private5", 21),
          ("private6", 22))
    )



class VpnId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )



class FailureStateEnum(TextualConvention, Integer32):
    status = "current"
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



class SensorStateEnum(TextualConvention, Integer32):
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
        *(("green", 0),
          ("yellow", 1),
          ("red", 2))
    )



class BoolEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )



class AddressFamilyEnum(TextualConvention, Integer32):
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



class AfTypeEnum(TextualConvention, Integer32):
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
        *(("tloc-ipv4", 0),
          ("tloc-ipv6", 1),
          ("service", 2),
          ("route-ipv4", 3),
          ("route-ipv6", 4),
          ("mcast-ipv4", 5),
          ("mcast-ipv6", 6))
    )



class OperState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("up", 0),
          ("down", 1))
    )



class AdminState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("up", 0),
          ("down", 1))
    )



class SiteId(TextualConvention, Unsigned32):
    status = "current"


class BgpState(TextualConvention, Integer32):
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
        *(("idle", 0),
          ("connect", 1),
          ("active", 2),
          ("opensent", 3),
          ("openconfirm", 4),
          ("established", 5),
          ("clearing", 6),
          ("deleted", 7))
    )



class HwSensorTypeEnum(TextualConvention, Integer32):
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
        *(("board", 0),
          ("cPU-Junction", 1),
          ("dRAM", 2),
          ("pIM", 3))
    )



class TunnelEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("delete", 2))
    )



class PersonalityEnumOper(TextualConvention, Integer32):
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
          ("vedge", 1),
          ("vhub", 2),
          ("vsmart", 3),
          ("vbond", 4),
          ("vmanage", 5),
          ("ztp", 6),
          ("vcontainer", 7))
    )



class Ipv4UcastAddrPrefix(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class EncapEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gre", 1),
          ("ipsec", 2))
    )



class Enumeration(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("up", 0),
          ("down", 1))
    )



class ViptelaIpAddress(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class OspfIfStateEnum(TextualConvention, Integer32):
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
        *(("if-depend-upon", 0),
          ("if-down", 1),
          ("if-loopback", 2),
          ("if-waiting", 3),
          ("if-point-to-point", 4),
          ("if-dr-other", 5),
          ("if-backup", 6),
          ("if-dr", 7))
    )



class OspfStateEnum(TextualConvention, Integer32):
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
        *(("full", 0),
          ("deleted", 1),
          ("depend-upon", 2),
          ("down", 3),
          ("attempt", 4),
          ("init", 5),
          ("two-way", 6),
          ("exstart", 7),
          ("exchange", 8),
          ("loading", 9))
    )



class StateEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dOWN", 1),
          ("uP", 2))
    )



class PeerState(TextualConvention, Integer32):
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
        *(("invalid", 0),
          ("init", 1),
          ("handshake", 2),
          ("up", 3),
          ("down", 4),
          ("init-in-gr", 5),
          ("down-in-gr", 6),
          ("handshake-in-gr", 7))
    )



class VrrpGroupStateEnum(TextualConvention, Integer32):
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
        *(("init", 1),
          ("backup", 2),
          ("master", 3))
    )



class InstallationStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
        *(("download-start", 2),
          ("download-complete", 3),
          ("verification-complete", 4),
          ("upgrade-apply-complete", 5),
          ("sync-partition-start", 6),
          ("sync-partition-complete", 7),
          ("install-complete", 8),
          ("install-fail", 9),
          ("reboot", 10))
    )



class OmpPolicyState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("add", 0),
          ("delete", 1))
    )



class AdminStateEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )



class BridgeId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )



class NumMacs(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class TrafficDirectionEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("downstream", 0),
          ("upstream", 1))
    )



class CloudAppEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              7,
              9,
              10,
              11,
              12,
              13,
              14,
              16)
        )
    )
    namedValues = NamedValues(
        *(("salesforce", 1),
          ("office365", 2),
          ("amazonAws", 3),
          ("oracle", 4),
          ("boxNet", 6),
          ("dropbox", 7),
          ("intuit", 9),
          ("concur", 10),
          ("sugarCrm", 11),
          ("zohoCrm", 12),
          ("zendesk", 13),
          ("gotomeeting", 14),
          ("googleApps", 16))
    )



class CloudExitEnum(TextualConvention, Integer32):
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
        *(("gateway", 1),
          ("local", 2),
          ("uncomputed", 3),
          ("none", 4))
    )



class WwanSimStatusEnum(TextualConvention, Integer32):
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
        *(("not-present", 0),
          ("present", 1),
          ("error", 2))
    )



class WwanDomainStatusEnum(TextualConvention, Integer32):
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
        *(("unknown", 0),
          ("attached", 1),
          ("detached", 2))
    )



class WwanRegStatusEnum(TextualConvention, Integer32):
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
        *(("not-registered", 0),
          ("registered", 1),
          ("searching", 2),
          ("registration-denied", 3),
          ("unknown", 4))
    )



class WwanBearerEnum(TextualConvention, Integer32):
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("cdma-1x", 1),
          ("cdma-1xevdo-rev0", 2),
          ("gprs", 3),
          ("umts", 4),
          ("cdma-1xevdo-revA", 5),
          ("edge", 6),
          ("hsdpa-wcdma", 7),
          ("wcdma-hsupa", 8),
          ("hsdpa-hsupa", 9),
          ("lte", 10),
          ("cdma-ehdrpd", 11),
          ("hsdpaplus-wcdma", 12),
          ("hsdpaplus-hsupa", 13),
          ("dchsdpaplus-wcdma", 14),
          ("dchsdpaplus-hsupa", 15),
          ("hsdpaplus-64qam", 16),
          ("hsdpaplus-64qam-hsupa", 17),
          ("tdscdma", 18),
          ("tdscdma-hsdpa", 19))
    )



class BfdFlapReasonEnum(TextualConvention, Integer32):
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
        *(("bfd-deleted", 1),
          ("remote-down", 2),
          ("timeout", 3),
          ("na", 4),
          ("not-known", 5),
          ("ondemand-idle-timeout-delete", 6))
    )



class WwanQosStatusEnum(TextualConvention, Integer32):
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
        *(("activated", 1),
          ("modified", 2),
          ("deleted", 3),
          ("suspended", 4),
          ("enabled", 5),
          ("disabled", 6))
    )



# MIB Managed Objects in the order of their OIDs

_Fields_ObjectIdentity = ObjectIdentity
fields = _Fields_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1)
)
_EventTime_Type = DateAndTime
_EventTime_Object = MibScalar
eventTime = _EventTime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 1),
    _EventTime_Type()
)
eventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventTime.setStatus("current")
_NetconfNotificationSeverity_Type = NetconfNotificationSeverity
_NetconfNotificationSeverity_Object = MibScalar
netconfNotificationSeverity = _NetconfNotificationSeverity_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 2),
    _NetconfNotificationSeverity_Type()
)
netconfNotificationSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netconfNotificationSeverity.setStatus("current")
_ViptelaActionsRebootReason_Type = OctetString
_ViptelaActionsRebootReason_Object = MibScalar
viptelaActionsRebootReason = _ViptelaActionsRebootReason_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 3),
    _ViptelaActionsRebootReason_Type()
)
viptelaActionsRebootReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaActionsRebootReason.setStatus("current")
_ViptelaBfdSrcIp_Type = ViptelaIpAddress
_ViptelaBfdSrcIp_Object = MibScalar
viptelaBfdSrcIp = _ViptelaBfdSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 4),
    _ViptelaBfdSrcIp_Type()
)
viptelaBfdSrcIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaBfdSrcIp.setStatus("current")
_ViptelaBfdDstIp_Type = ViptelaIpAddress
_ViptelaBfdDstIp_Object = MibScalar
viptelaBfdDstIp = _ViptelaBfdDstIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 5),
    _ViptelaBfdDstIp_Type()
)
viptelaBfdDstIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaBfdDstIp.setStatus("current")
_ViptelaBfdProto_Type = EncapEnum
_ViptelaBfdProto_Object = MibScalar
viptelaBfdProto = _ViptelaBfdProto_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 6),
    _ViptelaBfdProto_Type()
)
viptelaBfdProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaBfdProto.setStatus("current")
_ViptelaBfdSrcPort_Type = Unsigned32
_ViptelaBfdSrcPort_Object = MibScalar
viptelaBfdSrcPort = _ViptelaBfdSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 7),
    _ViptelaBfdSrcPort_Type()
)
viptelaBfdSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaBfdSrcPort.setStatus("current")
_ViptelaBfdDstPort_Type = Unsigned32
_ViptelaBfdDstPort_Object = MibScalar
viptelaBfdDstPort = _ViptelaBfdDstPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 8),
    _ViptelaBfdDstPort_Type()
)
viptelaBfdDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaBfdDstPort.setStatus("current")
_ViptelaBfdLocalSystemIp_Type = ViptelaIpAddress
_ViptelaBfdLocalSystemIp_Object = MibScalar
viptelaBfdLocalSystemIp = _ViptelaBfdLocalSystemIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 9),
    _ViptelaBfdLocalSystemIp_Type()
)
viptelaBfdLocalSystemIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaBfdLocalSystemIp.setStatus("current")
_ViptelaBfdLocalColor_Type = OctetString
_ViptelaBfdLocalColor_Object = MibScalar
viptelaBfdLocalColor = _ViptelaBfdLocalColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 10),
    _ViptelaBfdLocalColor_Type()
)
viptelaBfdLocalColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaBfdLocalColor.setStatus("current")
_ViptelaBfdRemoteSystemIp_Type = ViptelaIpAddress
_ViptelaBfdRemoteSystemIp_Object = MibScalar
viptelaBfdRemoteSystemIp = _ViptelaBfdRemoteSystemIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 11),
    _ViptelaBfdRemoteSystemIp_Type()
)
viptelaBfdRemoteSystemIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaBfdRemoteSystemIp.setStatus("current")
_ViptelaBfdRemoteColor_Type = OctetString
_ViptelaBfdRemoteColor_Object = MibScalar
viptelaBfdRemoteColor = _ViptelaBfdRemoteColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 12),
    _ViptelaBfdRemoteColor_Type()
)
viptelaBfdRemoteColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaBfdRemoteColor.setStatus("current")
_ViptelaBfdNewState_Type = OperState
_ViptelaBfdNewState_Object = MibScalar
viptelaBfdNewState = _ViptelaBfdNewState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 13),
    _ViptelaBfdNewState_Type()
)
viptelaBfdNewState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaBfdNewState.setStatus("current")
_ViptelaHardwareNewState_Type = FailureStateEnum
_ViptelaHardwareNewState_Object = MibScalar
viptelaHardwareNewState = _ViptelaHardwareNewState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 14),
    _ViptelaHardwareNewState_Type()
)
viptelaHardwareNewState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaHardwareNewState.setStatus("current")
_ViptelaHardwareHwSensorType_Type = HwSensorTypeEnum
_ViptelaHardwareHwSensorType_Object = MibScalar
viptelaHardwareHwSensorType = _ViptelaHardwareHwSensorType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 15),
    _ViptelaHardwareHwSensorType_Type()
)
viptelaHardwareHwSensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaHardwareHwSensorType.setStatus("current")
_ViptelaHardwareHwDevIndex_Type = Unsigned32
_ViptelaHardwareHwDevIndex_Object = MibScalar
viptelaHardwareHwDevIndex = _ViptelaHardwareHwDevIndex_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 16),
    _ViptelaHardwareHwDevIndex_Type()
)
viptelaHardwareHwDevIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaHardwareHwDevIndex.setStatus("current")
_ViptelaHardwareName_Type = OctetString
_ViptelaHardwareName_Object = MibScalar
viptelaHardwareName = _ViptelaHardwareName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 17),
    _ViptelaHardwareName_Type()
)
viptelaHardwareName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaHardwareName.setStatus("current")
_ViptelaHardwareTemp_Type = Unsigned32
_ViptelaHardwareTemp_Object = MibScalar
viptelaHardwareTemp = _ViptelaHardwareTemp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 18),
    _ViptelaHardwareTemp_Type()
)
viptelaHardwareTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaHardwareTemp.setStatus("current")
_ViptelaHardwareFantrayId_Type = Unsigned32
_ViptelaHardwareFantrayId_Object = MibScalar
viptelaHardwareFantrayId = _ViptelaHardwareFantrayId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 19),
    _ViptelaHardwareFantrayId_Type()
)
viptelaHardwareFantrayId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaHardwareFantrayId.setStatus("current")
_ViptelaHardwareFanId_Type = Unsigned32
_ViptelaHardwareFanId_Object = MibScalar
viptelaHardwareFanId = _ViptelaHardwareFanId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 20),
    _ViptelaHardwareFanId_Type()
)
viptelaHardwareFanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaHardwareFanId.setStatus("current")
_ViptelaHardwarePemId_Type = Unsigned32
_ViptelaHardwarePemId_Object = MibScalar
viptelaHardwarePemId = _ViptelaHardwarePemId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 21),
    _ViptelaHardwarePemId_Type()
)
viptelaHardwarePemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaHardwarePemId.setStatus("current")
_ViptelaHardwarePimId_Type = Unsigned32
_ViptelaHardwarePimId_Object = MibScalar
viptelaHardwarePimId = _ViptelaHardwarePimId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 22),
    _ViptelaHardwarePimId_Type()
)
viptelaHardwarePimId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaHardwarePimId.setStatus("current")
_ViptelaHardwareSfpName_Type = OctetString
_ViptelaHardwareSfpName_Object = MibScalar
viptelaHardwareSfpName = _ViptelaHardwareSfpName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 23),
    _ViptelaHardwareSfpName_Type()
)
viptelaHardwareSfpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaHardwareSfpName.setStatus("current")
_ViptelaHardwareUsbSlot_Type = Unsigned32
_ViptelaHardwareUsbSlot_Object = MibScalar
viptelaHardwareUsbSlot = _ViptelaHardwareUsbSlot_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 24),
    _ViptelaHardwareUsbSlot_Type()
)
viptelaHardwareUsbSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaHardwareUsbSlot.setStatus("current")
_ViptelaOmpNumberOfVsmarts_Type = Unsigned32
_ViptelaOmpNumberOfVsmarts_Object = MibScalar
viptelaOmpNumberOfVsmarts = _ViptelaOmpNumberOfVsmarts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 25),
    _ViptelaOmpNumberOfVsmarts_Type()
)
viptelaOmpNumberOfVsmarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaOmpNumberOfVsmarts.setStatus("current")
_ViptelaOmpNewState_Type = OperState
_ViptelaOmpNewState_Object = MibScalar
viptelaOmpNewState = _ViptelaOmpNewState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 26),
    _ViptelaOmpNewState_Type()
)
viptelaOmpNewState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaOmpNewState.setStatus("current")
_ViptelaOmpPeer_Type = ViptelaIpAddress
_ViptelaOmpPeer_Object = MibScalar
viptelaOmpPeer = _ViptelaOmpPeer_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 27),
    _ViptelaOmpPeer_Type()
)
viptelaOmpPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaOmpPeer.setStatus("current")
_ViptelaOmpPeerNewState_Type = PeerState
_ViptelaOmpPeerNewState_Object = MibScalar
viptelaOmpPeerNewState = _ViptelaOmpPeerNewState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 28),
    _ViptelaOmpPeerNewState_Type()
)
viptelaOmpPeerNewState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaOmpPeerNewState.setStatus("current")
_ViptelaOmpOmpAddressFamily_Type = AfTypeEnum
_ViptelaOmpOmpAddressFamily_Object = MibScalar
viptelaOmpOmpAddressFamily = _ViptelaOmpOmpAddressFamily_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 29),
    _ViptelaOmpOmpAddressFamily_Type()
)
viptelaOmpOmpAddressFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaOmpOmpAddressFamily.setStatus("current")
_ViptelaOmpPolicy_Type = OmpPolicyState
_ViptelaOmpPolicy_Object = MibScalar
viptelaOmpPolicy = _ViptelaOmpPolicy_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 30),
    _ViptelaOmpPolicy_Type()
)
viptelaOmpPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaOmpPolicy.setStatus("current")
_ViptelaOmpVsmartPeer_Type = ViptelaIpAddress
_ViptelaOmpVsmartPeer_Object = MibScalar
viptelaOmpVsmartPeer = _ViptelaOmpVsmartPeer_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 31),
    _ViptelaOmpVsmartPeer_Type()
)
viptelaOmpVsmartPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaOmpVsmartPeer.setStatus("current")
_ViptelaSecurityPeerType_Type = PersonalityEnumOper
_ViptelaSecurityPeerType_Object = MibScalar
viptelaSecurityPeerType = _ViptelaSecurityPeerType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 32),
    _ViptelaSecurityPeerType_Type()
)
viptelaSecurityPeerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaSecurityPeerType.setStatus("current")
_ViptelaSecurityPeerSystemIp_Type = ViptelaIpAddress
_ViptelaSecurityPeerSystemIp_Object = MibScalar
viptelaSecurityPeerSystemIp = _ViptelaSecurityPeerSystemIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 33),
    _ViptelaSecurityPeerSystemIp_Type()
)
viptelaSecurityPeerSystemIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaSecurityPeerSystemIp.setStatus("current")
_ViptelaSecurityPublicIp_Type = ViptelaIpAddress
_ViptelaSecurityPublicIp_Object = MibScalar
viptelaSecurityPublicIp = _ViptelaSecurityPublicIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 34),
    _ViptelaSecurityPublicIp_Type()
)
viptelaSecurityPublicIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaSecurityPublicIp.setStatus("current")
_ViptelaSecurityPublicPort_Type = Unsigned32
_ViptelaSecurityPublicPort_Object = MibScalar
viptelaSecurityPublicPort = _ViptelaSecurityPublicPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 35),
    _ViptelaSecurityPublicPort_Type()
)
viptelaSecurityPublicPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaSecurityPublicPort.setStatus("current")
_ViptelaSecuritySrcColor_Type = ColorEnum
_ViptelaSecuritySrcColor_Object = MibScalar
viptelaSecuritySrcColor = _ViptelaSecuritySrcColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 36),
    _ViptelaSecuritySrcColor_Type()
)
viptelaSecuritySrcColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaSecuritySrcColor.setStatus("current")
_ViptelaSecurityRemoteColor_Type = ColorEnum
_ViptelaSecurityRemoteColor_Object = MibScalar
viptelaSecurityRemoteColor = _ViptelaSecurityRemoteColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 37),
    _ViptelaSecurityRemoteColor_Type()
)
viptelaSecurityRemoteColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaSecurityRemoteColor.setStatus("current")
_ViptelaSecurityUptime_Type = OctetString
_ViptelaSecurityUptime_Object = MibScalar
viptelaSecurityUptime = _ViptelaSecurityUptime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 38),
    _ViptelaSecurityUptime_Type()
)
viptelaSecurityUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaSecurityUptime.setStatus("current")
_ViptelaSecurityNewState_Type = OperState
_ViptelaSecurityNewState_Object = MibScalar
viptelaSecurityNewState = _ViptelaSecurityNewState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 39),
    _ViptelaSecurityNewState_Type()
)
viptelaSecurityNewState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaSecurityNewState.setStatus("current")
_ViptelaSecurityLocalSystemIp_Type = ViptelaIpAddress
_ViptelaSecurityLocalSystemIp_Object = MibScalar
viptelaSecurityLocalSystemIp = _ViptelaSecurityLocalSystemIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 40),
    _ViptelaSecurityLocalSystemIp_Type()
)
viptelaSecurityLocalSystemIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaSecurityLocalSystemIp.setStatus("current")
_ViptelaSecurityLocalColor_Type = ColorEnum
_ViptelaSecurityLocalColor_Object = MibScalar
viptelaSecurityLocalColor = _ViptelaSecurityLocalColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 41),
    _ViptelaSecurityLocalColor_Type()
)
viptelaSecurityLocalColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaSecurityLocalColor.setStatus("current")
_ViptelaSecurityReason_Type = OctetString
_ViptelaSecurityReason_Object = MibScalar
viptelaSecurityReason = _ViptelaSecurityReason_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 42),
    _ViptelaSecurityReason_Type()
)
viptelaSecurityReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaSecurityReason.setStatus("current")
_ViptelaSecurityOldPublicIp_Type = ViptelaIpAddress
_ViptelaSecurityOldPublicIp_Object = MibScalar
viptelaSecurityOldPublicIp = _ViptelaSecurityOldPublicIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 43),
    _ViptelaSecurityOldPublicIp_Type()
)
viptelaSecurityOldPublicIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaSecurityOldPublicIp.setStatus("current")
_ViptelaSecurityOldPublicPort_Type = Unsigned32
_ViptelaSecurityOldPublicPort_Object = MibScalar
viptelaSecurityOldPublicPort = _ViptelaSecurityOldPublicPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 44),
    _ViptelaSecurityOldPublicPort_Type()
)
viptelaSecurityOldPublicPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaSecurityOldPublicPort.setStatus("current")
_ViptelaSecurityNewPublicIp_Type = ViptelaIpAddress
_ViptelaSecurityNewPublicIp_Object = MibScalar
viptelaSecurityNewPublicIp = _ViptelaSecurityNewPublicIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 45),
    _ViptelaSecurityNewPublicIp_Type()
)
viptelaSecurityNewPublicIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaSecurityNewPublicIp.setStatus("current")
_ViptelaSecurityNewPublicPort_Type = Unsigned32
_ViptelaSecurityNewPublicPort_Object = MibScalar
viptelaSecurityNewPublicPort = _ViptelaSecurityNewPublicPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 46),
    _ViptelaSecurityNewPublicPort_Type()
)
viptelaSecurityNewPublicPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaSecurityNewPublicPort.setStatus("current")
_ViptelaSecurityColor_Type = ColorEnum
_ViptelaSecurityColor_Object = MibScalar
viptelaSecurityColor = _ViptelaSecurityColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 47),
    _ViptelaSecurityColor_Type()
)
viptelaSecurityColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaSecurityColor.setStatus("current")
_ViptelaSecurityPersonality_Type = PersonalityEnumOper
_ViptelaSecurityPersonality_Object = MibScalar
viptelaSecurityPersonality = _ViptelaSecurityPersonality_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 48),
    _ViptelaSecurityPersonality_Type()
)
viptelaSecurityPersonality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaSecurityPersonality.setStatus("current")
_ViptelaSecurityUuid_Type = OctetString
_ViptelaSecurityUuid_Object = MibScalar
viptelaSecurityUuid = _ViptelaSecurityUuid_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 49),
    _ViptelaSecurityUuid_Type()
)
viptelaSecurityUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaSecurityUuid.setStatus("current")
_ViptelaSecuritySerial_Type = OctetString
_ViptelaSecuritySerial_Object = MibScalar
viptelaSecuritySerial = _ViptelaSecuritySerial_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 50),
    _ViptelaSecuritySerial_Type()
)
viptelaSecuritySerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaSecuritySerial.setStatus("current")
_ViptelaSystemProcessName_Type = OctetString
_ViptelaSystemProcessName_Object = MibScalar
viptelaSystemProcessName = _ViptelaSystemProcessName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 51),
    _ViptelaSystemProcessName_Type()
)
viptelaSystemProcessName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaSystemProcessName.setStatus("current")
_ViptelaSystemProcessId_Type = Unsigned32
_ViptelaSystemProcessId_Object = MibScalar
viptelaSystemProcessId = _ViptelaSystemProcessId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 52),
    _ViptelaSystemProcessId_Type()
)
viptelaSystemProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaSystemProcessId.setStatus("current")
_ViptelaSystemReason_Type = OctetString
_ViptelaSystemReason_Object = MibScalar
viptelaSystemReason = _ViptelaSystemReason_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 53),
    _ViptelaSystemReason_Type()
)
viptelaSystemReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaSystemReason.setStatus("current")
_ViptelaSystemWarning_Type = OctetString
_ViptelaSystemWarning_Object = MibScalar
viptelaSystemWarning = _ViptelaSystemWarning_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 54),
    _ViptelaSystemWarning_Type()
)
viptelaSystemWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaSystemWarning.setStatus("current")
_ViptelaSystemTotalMb_Type = Unsigned32
_ViptelaSystemTotalMb_Object = MibScalar
viptelaSystemTotalMb = _ViptelaSystemTotalMb_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 55),
    _ViptelaSystemTotalMb_Type()
)
viptelaSystemTotalMb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaSystemTotalMb.setStatus("current")
_ViptelaSystemFreeMb_Type = Unsigned32
_ViptelaSystemFreeMb_Object = MibScalar
viptelaSystemFreeMb = _ViptelaSystemFreeMb_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 56),
    _ViptelaSystemFreeMb_Type()
)
viptelaSystemFreeMb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaSystemFreeMb.setStatus("current")
_ViptelaSystemOldSiteId_Type = SiteId
_ViptelaSystemOldSiteId_Object = MibScalar
viptelaSystemOldSiteId = _ViptelaSystemOldSiteId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 57),
    _ViptelaSystemOldSiteId_Type()
)
viptelaSystemOldSiteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaSystemOldSiteId.setStatus("current")
_ViptelaSystemNewSiteId_Type = SiteId
_ViptelaSystemNewSiteId_Object = MibScalar
viptelaSystemNewSiteId = _ViptelaSystemNewSiteId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 58),
    _ViptelaSystemNewSiteId_Type()
)
viptelaSystemNewSiteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaSystemNewSiteId.setStatus("current")
_ViptelaSystemOldDomainId_Type = DomainId
_ViptelaSystemOldDomainId_Object = MibScalar
viptelaSystemOldDomainId = _ViptelaSystemOldDomainId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 59),
    _ViptelaSystemOldDomainId_Type()
)
viptelaSystemOldDomainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaSystemOldDomainId.setStatus("current")
_ViptelaSystemNewDomainId_Type = DomainId
_ViptelaSystemNewDomainId_Object = MibScalar
viptelaSystemNewDomainId = _ViptelaSystemNewDomainId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 60),
    _ViptelaSystemNewDomainId_Type()
)
viptelaSystemNewDomainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaSystemNewDomainId.setStatus("current")
_ViptelaSystemOldSystemIp_Type = ViptelaIpAddress
_ViptelaSystemOldSystemIp_Object = MibScalar
viptelaSystemOldSystemIp = _ViptelaSystemOldSystemIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 61),
    _ViptelaSystemOldSystemIp_Type()
)
viptelaSystemOldSystemIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaSystemOldSystemIp.setStatus("current")
_ViptelaSystemNewSystemIp_Type = ViptelaIpAddress
_ViptelaSystemNewSystemIp_Object = MibScalar
viptelaSystemNewSystemIp = _ViptelaSystemNewSystemIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 62),
    _ViptelaSystemNewSystemIp_Type()
)
viptelaSystemNewSystemIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaSystemNewSystemIp.setStatus("current")
_ViptelaSystemOldOrganizationName_Type = OctetString
_ViptelaSystemOldOrganizationName_Object = MibScalar
viptelaSystemOldOrganizationName = _ViptelaSystemOldOrganizationName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 63),
    _ViptelaSystemOldOrganizationName_Type()
)
viptelaSystemOldOrganizationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaSystemOldOrganizationName.setStatus("current")
_ViptelaSystemNewOrganizationName_Type = OctetString
_ViptelaSystemNewOrganizationName_Object = MibScalar
viptelaSystemNewOrganizationName = _ViptelaSystemNewOrganizationName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 64),
    _ViptelaSystemNewOrganizationName_Type()
)
viptelaSystemNewOrganizationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaSystemNewOrganizationName.setStatus("current")
_ViptelaSystemUserName_Type = OctetString
_ViptelaSystemUserName_Object = MibScalar
viptelaSystemUserName = _ViptelaSystemUserName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 65),
    _ViptelaSystemUserName_Type()
)
viptelaSystemUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaSystemUserName.setStatus("current")
_ViptelaSystemUserId_Type = Integer32
_ViptelaSystemUserId_Object = MibScalar
viptelaSystemUserId = _ViptelaSystemUserId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 66),
    _ViptelaSystemUserId_Type()
)
viptelaSystemUserId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaSystemUserId.setStatus("current")
_ViptelaVpnVpnId_Type = VpnId
_ViptelaVpnVpnId_Object = MibScalar
viptelaVpnVpnId = _ViptelaVpnVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 67),
    _ViptelaVpnVpnId_Type()
)
viptelaVpnVpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaVpnVpnId.setStatus("current")
_ViptelaVpnPeer_Type = ViptelaIpAddress
_ViptelaVpnPeer_Object = MibScalar
viptelaVpnPeer = _ViptelaVpnPeer_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 68),
    _ViptelaVpnPeer_Type()
)
viptelaVpnPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaVpnPeer.setStatus("current")
_ViptelaVpnBgpNewState_Type = BgpState
_ViptelaVpnBgpNewState_Object = MibScalar
viptelaVpnBgpNewState = _ViptelaVpnBgpNewState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 69),
    _ViptelaVpnBgpNewState_Type()
)
viptelaVpnBgpNewState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaVpnBgpNewState.setStatus("current")
_ViptelaVpnLocalAddress_Type = ViptelaIpAddress
_ViptelaVpnLocalAddress_Object = MibScalar
viptelaVpnLocalAddress = _ViptelaVpnLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 70),
    _ViptelaVpnLocalAddress_Type()
)
viptelaVpnLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaVpnLocalAddress.setStatus("current")
_ViptelaVpnLocalRouterid_Type = ViptelaIpAddress
_ViptelaVpnLocalRouterid_Object = MibScalar
viptelaVpnLocalRouterid = _ViptelaVpnLocalRouterid_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 71),
    _ViptelaVpnLocalRouterid_Type()
)
viptelaVpnLocalRouterid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaVpnLocalRouterid.setStatus("current")
_ViptelaVpnPeerRouterid_Type = ViptelaIpAddress
_ViptelaVpnPeerRouterid_Object = MibScalar
viptelaVpnPeerRouterid = _ViptelaVpnPeerRouterid_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 72),
    _ViptelaVpnPeerRouterid_Type()
)
viptelaVpnPeerRouterid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaVpnPeerRouterid.setStatus("current")
_ViptelaVpnIfName_Type = OctetString
_ViptelaVpnIfName_Object = MibScalar
viptelaVpnIfName = _ViptelaVpnIfName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 73),
    _ViptelaVpnIfName_Type()
)
viptelaVpnIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaVpnIfName.setStatus("current")
_ViptelaVpnNewState_Type = OperState
_ViptelaVpnNewState_Object = MibScalar
viptelaVpnNewState = _ViptelaVpnNewState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 74),
    _ViptelaVpnNewState_Type()
)
viptelaVpnNewState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaVpnNewState.setStatus("current")
_ViptelaVpnGrpId_Type = Unsigned32
_ViptelaVpnGrpId_Object = MibScalar
viptelaVpnGrpId = _ViptelaVpnGrpId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 75),
    _ViptelaVpnGrpId_Type()
)
viptelaVpnGrpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaVpnGrpId.setStatus("current")


class _ViptelaVpnIpPrefix_Type(OctetString):
    """Custom type viptelaVpnIpPrefix based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_ViptelaVpnIpPrefix_Type.__name__ = "OctetString"
_ViptelaVpnIpPrefix_Object = MibScalar
viptelaVpnIpPrefix = _ViptelaVpnIpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 76),
    _ViptelaVpnIpPrefix_Type()
)
viptelaVpnIpPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaVpnIpPrefix.setStatus("current")
_ViptelaVpnFailureReason_Type = OctetString
_ViptelaVpnFailureReason_Object = MibScalar
viptelaVpnFailureReason = _ViptelaVpnFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 77),
    _ViptelaVpnFailureReason_Type()
)
viptelaVpnFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaVpnFailureReason.setStatus("current")
_ViptelaVpnFarEndSystemIp_Type = ViptelaIpAddress
_ViptelaVpnFarEndSystemIp_Object = MibScalar
viptelaVpnFarEndSystemIp = _ViptelaVpnFarEndSystemIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 78),
    _ViptelaVpnFarEndSystemIp_Type()
)
viptelaVpnFarEndSystemIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaVpnFarEndSystemIp.setStatus("current")
_ViptelaVpnFarEndColor_Type = ColorEnum
_ViptelaVpnFarEndColor_Object = MibScalar
viptelaVpnFarEndColor = _ViptelaVpnFarEndColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 79),
    _ViptelaVpnFarEndColor_Type()
)
viptelaVpnFarEndColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaVpnFarEndColor.setStatus("current")
_ViptelaVpnClientMac_Type = OctetString
_ViptelaVpnClientMac_Object = MibScalar
viptelaVpnClientMac = _ViptelaVpnClientMac_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 80),
    _ViptelaVpnClientMac_Type()
)
viptelaVpnClientMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaVpnClientMac.setStatus("current")
_ViptelaVpnIp_Type = ViptelaIpAddress
_ViptelaVpnIp_Object = MibScalar
viptelaVpnIp = _ViptelaVpnIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 81),
    _ViptelaVpnIp_Type()
)
viptelaVpnIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaVpnIp.setStatus("current")
_ViptelaVpnReason_Type = OctetString
_ViptelaVpnReason_Object = MibScalar
viptelaVpnReason = _ViptelaVpnReason_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 82),
    _ViptelaVpnReason_Type()
)
viptelaVpnReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaVpnReason.setStatus("current")
_ViptelaVpnState_Type = Enumeration
_ViptelaVpnState_Object = MibScalar
viptelaVpnState = _ViptelaVpnState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 83),
    _ViptelaVpnState_Type()
)
viptelaVpnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaVpnState.setStatus("current")
_ViptelaVpnNeighbor_Type = ViptelaIpAddress
_ViptelaVpnNeighbor_Object = MibScalar
viptelaVpnNeighbor = _ViptelaVpnNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 84),
    _ViptelaVpnNeighbor_Type()
)
viptelaVpnNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaVpnNeighbor.setStatus("current")
_ViptelaVpnPimNewState_Type = StateEnum
_ViptelaVpnPimNewState_Object = MibScalar
viptelaVpnPimNewState = _ViptelaVpnPimNewState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 85),
    _ViptelaVpnPimNewState_Type()
)
viptelaVpnPimNewState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaVpnPimNewState.setStatus("current")
_ViptelaVpnInterface_Type = OctetString
_ViptelaVpnInterface_Object = MibScalar
viptelaVpnInterface = _ViptelaVpnInterface_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 86),
    _ViptelaVpnInterface_Type()
)
viptelaVpnInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaVpnInterface.setStatus("current")
_ViptelaVpnTunnelAddress_Type = ViptelaIpAddress
_ViptelaVpnTunnelAddress_Object = MibScalar
viptelaVpnTunnelAddress = _ViptelaVpnTunnelAddress_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 87),
    _ViptelaVpnTunnelAddress_Type()
)
viptelaVpnTunnelAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaVpnTunnelAddress.setStatus("current")
_ViptelaVpnRouterId_Type = ViptelaIpAddress
_ViptelaVpnRouterId_Object = MibScalar
viptelaVpnRouterId = _ViptelaVpnRouterId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 88),
    _ViptelaVpnRouterId_Type()
)
viptelaVpnRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaVpnRouterId.setStatus("current")
_ViptelaVpnOspfNewState_Type = OspfStateEnum
_ViptelaVpnOspfNewState_Object = MibScalar
viptelaVpnOspfNewState = _ViptelaVpnOspfNewState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 89),
    _ViptelaVpnOspfNewState_Type()
)
viptelaVpnOspfNewState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaVpnOspfNewState.setStatus("current")
_ViptelaVpnIfAddr_Type = Ipv4UcastAddrPrefix
_ViptelaVpnIfAddr_Object = MibScalar
viptelaVpnIfAddr = _ViptelaVpnIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 90),
    _ViptelaVpnIfAddr_Type()
)
viptelaVpnIfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaVpnIfAddr.setStatus("current")
_ViptelaVpnOspfInterfaceNewState_Type = OspfIfStateEnum
_ViptelaVpnOspfInterfaceNewState_Object = MibScalar
viptelaVpnOspfInterfaceNewState = _ViptelaVpnOspfInterfaceNewState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 91),
    _ViptelaVpnOspfInterfaceNewState_Type()
)
viptelaVpnOspfInterfaceNewState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaVpnOspfInterfaceNewState.setStatus("current")
_ViptelaVpnVrrpGroupState_Type = VrrpGroupStateEnum
_ViptelaVpnVrrpGroupState_Object = MibScalar
viptelaVpnVrrpGroupState = _ViptelaVpnVrrpGroupState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 92),
    _ViptelaVpnVrrpGroupState_Type()
)
viptelaVpnVrrpGroupState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaVpnVrrpGroupState.setStatus("current")
_ViptelaSystemStatusStr_Type = OctetString
_ViptelaSystemStatusStr_Object = MibScalar
viptelaSystemStatusStr = _ViptelaSystemStatusStr_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 93),
    _ViptelaSystemStatusStr_Type()
)
viptelaSystemStatusStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaSystemStatusStr.setStatus("current")
_ViptelaAppRouteSrcIp_Type = ViptelaIpAddress
_ViptelaAppRouteSrcIp_Object = MibScalar
viptelaAppRouteSrcIp = _ViptelaAppRouteSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 94),
    _ViptelaAppRouteSrcIp_Type()
)
viptelaAppRouteSrcIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaAppRouteSrcIp.setStatus("current")
_ViptelaAppRouteDstIp_Type = ViptelaIpAddress
_ViptelaAppRouteDstIp_Object = MibScalar
viptelaAppRouteDstIp = _ViptelaAppRouteDstIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 95),
    _ViptelaAppRouteDstIp_Type()
)
viptelaAppRouteDstIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaAppRouteDstIp.setStatus("current")
_ViptelaAppRouteProto_Type = EncapEnum
_ViptelaAppRouteProto_Object = MibScalar
viptelaAppRouteProto = _ViptelaAppRouteProto_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 96),
    _ViptelaAppRouteProto_Type()
)
viptelaAppRouteProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaAppRouteProto.setStatus("current")
_ViptelaAppRouteSrcPort_Type = Unsigned32
_ViptelaAppRouteSrcPort_Object = MibScalar
viptelaAppRouteSrcPort = _ViptelaAppRouteSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 97),
    _ViptelaAppRouteSrcPort_Type()
)
viptelaAppRouteSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaAppRouteSrcPort.setStatus("current")
_ViptelaAppRouteDstPort_Type = Unsigned32
_ViptelaAppRouteDstPort_Object = MibScalar
viptelaAppRouteDstPort = _ViptelaAppRouteDstPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 98),
    _ViptelaAppRouteDstPort_Type()
)
viptelaAppRouteDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaAppRouteDstPort.setStatus("current")
_ViptelaAppRouteLocalSystemIp_Type = ViptelaIpAddress
_ViptelaAppRouteLocalSystemIp_Object = MibScalar
viptelaAppRouteLocalSystemIp = _ViptelaAppRouteLocalSystemIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 99),
    _ViptelaAppRouteLocalSystemIp_Type()
)
viptelaAppRouteLocalSystemIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaAppRouteLocalSystemIp.setStatus("current")
_ViptelaAppRouteLocalColor_Type = OctetString
_ViptelaAppRouteLocalColor_Object = MibScalar
viptelaAppRouteLocalColor = _ViptelaAppRouteLocalColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 100),
    _ViptelaAppRouteLocalColor_Type()
)
viptelaAppRouteLocalColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaAppRouteLocalColor.setStatus("current")
_ViptelaAppRouteRemoteSystemIp_Type = ViptelaIpAddress
_ViptelaAppRouteRemoteSystemIp_Object = MibScalar
viptelaAppRouteRemoteSystemIp = _ViptelaAppRouteRemoteSystemIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 101),
    _ViptelaAppRouteRemoteSystemIp_Type()
)
viptelaAppRouteRemoteSystemIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaAppRouteRemoteSystemIp.setStatus("current")
_ViptelaAppRouteRemoteColor_Type = OctetString
_ViptelaAppRouteRemoteColor_Object = MibScalar
viptelaAppRouteRemoteColor = _ViptelaAppRouteRemoteColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 102),
    _ViptelaAppRouteRemoteColor_Type()
)
viptelaAppRouteRemoteColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaAppRouteRemoteColor.setStatus("current")
_ViptelaAppRouteMeanLoss_Type = UnsignedByte
_ViptelaAppRouteMeanLoss_Object = MibScalar
viptelaAppRouteMeanLoss = _ViptelaAppRouteMeanLoss_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 103),
    _ViptelaAppRouteMeanLoss_Type()
)
viptelaAppRouteMeanLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaAppRouteMeanLoss.setStatus("current")
_ViptelaAppRouteMeanLatency_Type = Unsigned32
_ViptelaAppRouteMeanLatency_Object = MibScalar
viptelaAppRouteMeanLatency = _ViptelaAppRouteMeanLatency_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 104),
    _ViptelaAppRouteMeanLatency_Type()
)
viptelaAppRouteMeanLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaAppRouteMeanLatency.setStatus("current")
_ViptelaAppRouteSlaClasses_Type = OctetString
_ViptelaAppRouteSlaClasses_Object = MibScalar
viptelaAppRouteSlaClasses = _ViptelaAppRouteSlaClasses_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 105),
    _ViptelaAppRouteSlaClasses_Type()
)
viptelaAppRouteSlaClasses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaAppRouteSlaClasses.setStatus("current")
_ViptelaActionsStatus_Type = InstallationStatus
_ViptelaActionsStatus_Object = MibScalar
viptelaActionsStatus = _ViptelaActionsStatus_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 106),
    _ViptelaActionsStatus_Type()
)
viptelaActionsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaActionsStatus.setStatus("current")
_ViptelaActionsInstallId_Type = OctetString
_ViptelaActionsInstallId_Object = MibScalar
viptelaActionsInstallId = _ViptelaActionsInstallId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 107),
    _ViptelaActionsInstallId_Type()
)
viptelaActionsInstallId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaActionsInstallId.setStatus("current")
_ViptelaActionsMessage_Type = OctetString
_ViptelaActionsMessage_Object = MibScalar
viptelaActionsMessage = _ViptelaActionsMessage_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 108),
    _ViptelaActionsMessage_Type()
)
viptelaActionsMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaActionsMessage.setStatus("current")
_ViptelaVpnOperState_Type = StateEnum
_ViptelaVpnOperState_Object = MibScalar
viptelaVpnOperState = _ViptelaVpnOperState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 109),
    _ViptelaVpnOperState_Type()
)
viptelaVpnOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaVpnOperState.setStatus("current")
_ViptelaVpnAdminState_Type = AdminStateEnum
_ViptelaVpnAdminState_Object = MibScalar
viptelaVpnAdminState = _ViptelaVpnAdminState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 110),
    _ViptelaVpnAdminState_Type()
)
viptelaVpnAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaVpnAdminState.setStatus("current")
_ViptelaVpnAddressFamilyType_Type = AddressFamilyEnum
_ViptelaVpnAddressFamilyType_Object = MibScalar
viptelaVpnAddressFamilyType = _ViptelaVpnAddressFamilyType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 111),
    _ViptelaVpnAddressFamilyType_Type()
)
viptelaVpnAddressFamilyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaVpnAddressFamilyType.setStatus("current")
_ViptelaVpnFibLastUpdateTime_Type = DateAndTime
_ViptelaVpnFibLastUpdateTime_Object = MibScalar
viptelaVpnFibLastUpdateTime = _ViptelaVpnFibLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 112),
    _ViptelaVpnFibLastUpdateTime_Type()
)
viptelaVpnFibLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaVpnFibLastUpdateTime.setStatus("current")
_ViptelaBridgeId_Type = BridgeId
_ViptelaBridgeId_Object = MibScalar
viptelaBridgeId = _ViptelaBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 113),
    _ViptelaBridgeId_Type()
)
viptelaBridgeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaBridgeId.setStatus("current")
_ViptelaNumMacs_Type = NumMacs
_ViptelaNumMacs_Object = MibScalar
viptelaNumMacs = _ViptelaNumMacs_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 114),
    _ViptelaNumMacs_Type()
)
viptelaNumMacs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaNumMacs.setStatus("current")
_ViptelaPolicyVpnId_Type = VpnId
_ViptelaPolicyVpnId_Object = MibScalar
viptelaPolicyVpnId = _ViptelaPolicyVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 115),
    _ViptelaPolicyVpnId_Type()
)
viptelaPolicyVpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaPolicyVpnId.setStatus("current")
_ViptelaPolicyApplication_Type = OctetString
_ViptelaPolicyApplication_Object = MibScalar
viptelaPolicyApplication = _ViptelaPolicyApplication_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 116),
    _ViptelaPolicyApplication_Type()
)
viptelaPolicyApplication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaPolicyApplication.setStatus("current")
_ViptelaPolicySourceIp_Type = ViptelaIpAddress
_ViptelaPolicySourceIp_Object = MibScalar
viptelaPolicySourceIp = _ViptelaPolicySourceIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 117),
    _ViptelaPolicySourceIp_Type()
)
viptelaPolicySourceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaPolicySourceIp.setStatus("current")
_ViptelaPolicySourcePort_Type = Unsigned32
_ViptelaPolicySourcePort_Object = MibScalar
viptelaPolicySourcePort = _ViptelaPolicySourcePort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 118),
    _ViptelaPolicySourcePort_Type()
)
viptelaPolicySourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaPolicySourcePort.setStatus("current")
_ViptelaPolicyDestinationIp_Type = ViptelaIpAddress
_ViptelaPolicyDestinationIp_Object = MibScalar
viptelaPolicyDestinationIp = _ViptelaPolicyDestinationIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 119),
    _ViptelaPolicyDestinationIp_Type()
)
viptelaPolicyDestinationIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaPolicyDestinationIp.setStatus("current")
_ViptelaPolicyDestinationPort_Type = Unsigned32
_ViptelaPolicyDestinationPort_Object = MibScalar
viptelaPolicyDestinationPort = _ViptelaPolicyDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 120),
    _ViptelaPolicyDestinationPort_Type()
)
viptelaPolicyDestinationPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaPolicyDestinationPort.setStatus("current")
_ViptelaPolicyProtocol_Type = Unsigned32
_ViptelaPolicyProtocol_Object = MibScalar
viptelaPolicyProtocol = _ViptelaPolicyProtocol_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 121),
    _ViptelaPolicyProtocol_Type()
)
viptelaPolicyProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaPolicyProtocol.setStatus("current")
_ViptelaPolicyDscp_Type = Unsigned32
_ViptelaPolicyDscp_Object = MibScalar
viptelaPolicyDscp = _ViptelaPolicyDscp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 122),
    _ViptelaPolicyDscp_Type()
)
viptelaPolicyDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaPolicyDscp.setStatus("current")
_ViptelaPolicySlaInformation_Type = OctetString
_ViptelaPolicySlaInformation_Object = MibScalar
viptelaPolicySlaInformation = _ViptelaPolicySlaInformation_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 123),
    _ViptelaPolicySlaInformation_Type()
)
viptelaPolicySlaInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaPolicySlaInformation.setStatus("current")
_ViptelaPolicySlaStatus_Type = OctetString
_ViptelaPolicySlaStatus_Object = MibScalar
viptelaPolicySlaStatus = _ViptelaPolicySlaStatus_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 124),
    _ViptelaPolicySlaStatus_Type()
)
viptelaPolicySlaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaPolicySlaStatus.setStatus("current")
_ViptelaSystemDpiOutOfMemoryState_Type = TruthValue
_ViptelaSystemDpiOutOfMemoryState_Object = MibScalar
viptelaSystemDpiOutOfMemoryState = _ViptelaSystemDpiOutOfMemoryState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 125),
    _ViptelaSystemDpiOutOfMemoryState_Type()
)
viptelaSystemDpiOutOfMemoryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaSystemDpiOutOfMemoryState.setStatus("current")
_ViptelaBfdDeleted_Type = BoolEnum
_ViptelaBfdDeleted_Object = MibScalar
viptelaBfdDeleted = _ViptelaBfdDeleted_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 126),
    _ViptelaBfdDeleted_Type()
)
viptelaBfdDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaBfdDeleted.setStatus("current")
_ViptelaSecurityGreOldOperState_Type = OperState
_ViptelaSecurityGreOldOperState_Object = MibScalar
viptelaSecurityGreOldOperState = _ViptelaSecurityGreOldOperState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 127),
    _ViptelaSecurityGreOldOperState_Type()
)
viptelaSecurityGreOldOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaSecurityGreOldOperState.setStatus("current")
_ViptelaSecurityGreNewOperState_Type = OperState
_ViptelaSecurityGreNewOperState_Object = MibScalar
viptelaSecurityGreNewOperState = _ViptelaSecurityGreNewOperState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 128),
    _ViptelaSecurityGreNewOperState_Type()
)
viptelaSecurityGreNewOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaSecurityGreNewOperState.setStatus("current")
_ViptelaSecurityGreIfName_Type = OctetString
_ViptelaSecurityGreIfName_Object = MibScalar
viptelaSecurityGreIfName = _ViptelaSecurityGreIfName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 129),
    _ViptelaSecurityGreIfName_Type()
)
viptelaSecurityGreIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaSecurityGreIfName.setStatus("current")
_ViptelaSecurityGreVpnId_Type = VpnId
_ViptelaSecurityGreVpnId_Object = MibScalar
viptelaSecurityGreVpnId = _ViptelaSecurityGreVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 130),
    _ViptelaSecurityGreVpnId_Type()
)
viptelaSecurityGreVpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaSecurityGreVpnId.setStatus("current")
_ViptelaSecurityGreTunnelSource_Type = ViptelaIpAddress
_ViptelaSecurityGreTunnelSource_Object = MibScalar
viptelaSecurityGreTunnelSource = _ViptelaSecurityGreTunnelSource_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 131),
    _ViptelaSecurityGreTunnelSource_Type()
)
viptelaSecurityGreTunnelSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaSecurityGreTunnelSource.setStatus("current")
_ViptelaSecurityGreTunnelDestination_Type = ViptelaIpAddress
_ViptelaSecurityGreTunnelDestination_Object = MibScalar
viptelaSecurityGreTunnelDestination = _ViptelaSecurityGreTunnelDestination_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 132),
    _ViptelaSecurityGreTunnelDestination_Type()
)
viptelaSecurityGreTunnelDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaSecurityGreTunnelDestination.setStatus("current")
_ViptelaSecurityGreGreIp_Type = OctetString
_ViptelaSecurityGreGreIp_Object = MibScalar
viptelaSecurityGreGreIp = _ViptelaSecurityGreGreIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 133),
    _ViptelaSecurityGreGreIp_Type()
)
viptelaSecurityGreGreIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaSecurityGreGreIp.setStatus("current")
_ViptelaVpnIfCfgBwKbps_Type = Unsigned32
_ViptelaVpnIfCfgBwKbps_Object = MibScalar
viptelaVpnIfCfgBwKbps = _ViptelaVpnIfCfgBwKbps_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 134),
    _ViptelaVpnIfCfgBwKbps_Type()
)
viptelaVpnIfCfgBwKbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaVpnIfCfgBwKbps.setStatus("current")
_ViptelaVpnTrafficDirection_Type = TrafficDirectionEnum
_ViptelaVpnTrafficDirection_Object = MibScalar
viptelaVpnTrafficDirection = _ViptelaVpnTrafficDirection_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 135),
    _ViptelaVpnTrafficDirection_Type()
)
viptelaVpnTrafficDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaVpnTrafficDirection.setStatus("current")
_ViptelaVpnDuration_Type = Unsigned32
_ViptelaVpnDuration_Object = MibScalar
viptelaVpnDuration = _ViptelaVpnDuration_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 136),
    _ViptelaVpnDuration_Type()
)
viptelaVpnDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaVpnDuration.setStatus("current")
_ViptelaAppRouteMeanJitter_Type = Unsigned32
_ViptelaAppRouteMeanJitter_Object = MibScalar
viptelaAppRouteMeanJitter = _ViptelaAppRouteMeanJitter_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 137),
    _ViptelaAppRouteMeanJitter_Type()
)
viptelaAppRouteMeanJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaAppRouteMeanJitter.setStatus("current")
_ViptelaVpnPimEnabled_Type = TruthValue
_ViptelaVpnPimEnabled_Object = MibScalar
viptelaVpnPimEnabled = _ViptelaVpnPimEnabled_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 138),
    _ViptelaVpnPimEnabled_Type()
)
viptelaVpnPimEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaVpnPimEnabled.setStatus("current")
_ViptelaSystemRemoteHost_Type = OctetString
_ViptelaSystemRemoteHost_Object = MibScalar
viptelaSystemRemoteHost = _ViptelaSystemRemoteHost_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 139),
    _ViptelaSystemRemoteHost_Type()
)
viptelaSystemRemoteHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaSystemRemoteHost.setStatus("current")
_ViptelaPolicyVpnListName_Type = OctetString
_ViptelaPolicyVpnListName_Object = MibScalar
viptelaPolicyVpnListName = _ViptelaPolicyVpnListName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 140),
    _ViptelaPolicyVpnListName_Type()
)
viptelaPolicyVpnListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaPolicyVpnListName.setStatus("current")
_ViptelaPolicyName_Type = OctetString
_ViptelaPolicyName_Object = MibScalar
viptelaPolicyName = _ViptelaPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 141),
    _ViptelaPolicyName_Type()
)
viptelaPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaPolicyName.setStatus("current")
_ViptelaPolicyAccessListName_Type = OctetString
_ViptelaPolicyAccessListName_Object = MibScalar
viptelaPolicyAccessListName = _ViptelaPolicyAccessListName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 142),
    _ViptelaPolicyAccessListName_Type()
)
viptelaPolicyAccessListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaPolicyAccessListName.setStatus("current")
_ViptelaPolicyStatus_Type = OctetString
_ViptelaPolicyStatus_Object = MibScalar
viptelaPolicyStatus = _ViptelaPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 143),
    _ViptelaPolicyStatus_Type()
)
viptelaPolicyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaPolicyStatus.setStatus("current")
_ViptelaSecurityVmanageConnectionPreference_Type = UnsignedByte
_ViptelaSecurityVmanageConnectionPreference_Object = MibScalar
viptelaSecurityVmanageConnectionPreference = _ViptelaSecurityVmanageConnectionPreference_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 144),
    _ViptelaSecurityVmanageConnectionPreference_Type()
)
viptelaSecurityVmanageConnectionPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaSecurityVmanageConnectionPreference.setStatus("current")
_ViptelaHardwareSensorNewState_Type = SensorStateEnum
_ViptelaHardwareSensorNewState_Object = MibScalar
viptelaHardwareSensorNewState = _ViptelaHardwareSensorNewState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 145),
    _ViptelaHardwareSensorNewState_Type()
)
viptelaHardwareSensorNewState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaHardwareSensorNewState.setStatus("current")
_ViptelaCloudExpressApplication_Type = CloudAppEnum
_ViptelaCloudExpressApplication_Object = MibScalar
viptelaCloudExpressApplication = _ViptelaCloudExpressApplication_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 146),
    _ViptelaCloudExpressApplication_Type()
)
viptelaCloudExpressApplication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaCloudExpressApplication.setStatus("current")
_ViptelaCloudExpressExitType_Type = CloudExitEnum
_ViptelaCloudExpressExitType_Object = MibScalar
viptelaCloudExpressExitType = _ViptelaCloudExpressExitType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 147),
    _ViptelaCloudExpressExitType_Type()
)
viptelaCloudExpressExitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaCloudExpressExitType.setStatus("current")
_ViptelaGatewayIp_Type = ViptelaIpAddress
_ViptelaGatewayIp_Object = MibScalar
viptelaGatewayIp = _ViptelaGatewayIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 148),
    _ViptelaGatewayIp_Type()
)
viptelaGatewayIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaGatewayIp.setStatus("current")
_ViptelaAppLatency_Type = Unsigned32
_ViptelaAppLatency_Object = MibScalar
viptelaAppLatency = _ViptelaAppLatency_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 149),
    _ViptelaAppLatency_Type()
)
viptelaAppLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaAppLatency.setStatus("current")
_ViptelaAppLoss_Type = Unsigned32
_ViptelaAppLoss_Object = MibScalar
viptelaAppLoss = _ViptelaAppLoss_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 150),
    _ViptelaAppLoss_Type()
)
viptelaAppLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaAppLoss.setStatus("current")
_ViptelaWwanSimSlot_Type = Unsigned32
_ViptelaWwanSimSlot_Object = MibScalar
viptelaWwanSimSlot = _ViptelaWwanSimSlot_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 151),
    _ViptelaWwanSimSlot_Type()
)
viptelaWwanSimSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaWwanSimSlot.setStatus("current")
_ViptelaWwanSimState_Type = WwanSimStatusEnum
_ViptelaWwanSimState_Object = MibScalar
viptelaWwanSimState = _ViptelaWwanSimState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 152),
    _ViptelaWwanSimState_Type()
)
viptelaWwanSimState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaWwanSimState.setStatus("current")
_ViptelaAppRouteOldSlaClasses_Type = OctetString
_ViptelaAppRouteOldSlaClasses_Object = MibScalar
viptelaAppRouteOldSlaClasses = _ViptelaAppRouteOldSlaClasses_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 153),
    _ViptelaAppRouteOldSlaClasses_Type()
)
viptelaAppRouteOldSlaClasses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaAppRouteOldSlaClasses.setStatus("current")
_ViptelaVpnNewAdminState_Type = AdminState
_ViptelaVpnNewAdminState_Object = MibScalar
viptelaVpnNewAdminState = _ViptelaVpnNewAdminState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 154),
    _ViptelaVpnNewAdminState_Type()
)
viptelaVpnNewAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaVpnNewAdminState.setStatus("current")
_ViptelaWwanDomainState_Type = WwanDomainStatusEnum
_ViptelaWwanDomainState_Object = MibScalar
viptelaWwanDomainState = _ViptelaWwanDomainState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 155),
    _ViptelaWwanDomainState_Type()
)
viptelaWwanDomainState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaWwanDomainState.setStatus("current")
_ViptelaWwanRegState_Type = WwanRegStatusEnum
_ViptelaWwanRegState_Object = MibScalar
viptelaWwanRegState = _ViptelaWwanRegState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 156),
    _ViptelaWwanRegState_Type()
)
viptelaWwanRegState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaWwanRegState.setStatus("current")
_ViptelaWwanBearer_Type = WwanBearerEnum
_ViptelaWwanBearer_Object = MibScalar
viptelaWwanBearer = _ViptelaWwanBearer_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 157),
    _ViptelaWwanBearer_Type()
)
viptelaWwanBearer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaWwanBearer.setStatus("current")
_ViptelaActionsReason_Type = OctetString
_ViptelaActionsReason_Object = MibScalar
viptelaActionsReason = _ViptelaActionsReason_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 158),
    _ViptelaActionsReason_Type()
)
viptelaActionsReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaActionsReason.setStatus("current")
_ViptelaWwanIfname_Type = OctetString
_ViptelaWwanIfname_Object = MibScalar
viptelaWwanIfname = _ViptelaWwanIfname_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 159),
    _ViptelaWwanIfname_Type()
)
viptelaWwanIfname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaWwanIfname.setStatus("current")
_ViptelaExitLocalColor_Type = OctetString
_ViptelaExitLocalColor_Object = MibScalar
viptelaExitLocalColor = _ViptelaExitLocalColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 160),
    _ViptelaExitLocalColor_Type()
)
viptelaExitLocalColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaExitLocalColor.setStatus("current")
_ViptelaExitRemoteColor_Type = OctetString
_ViptelaExitRemoteColor_Object = MibScalar
viptelaExitRemoteColor = _ViptelaExitRemoteColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 161),
    _ViptelaExitRemoteColor_Type()
)
viptelaExitRemoteColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaExitRemoteColor.setStatus("current")
_ViptelaSecurityOrganizationName_Type = OctetString
_ViptelaSecurityOrganizationName_Object = MibScalar
viptelaSecurityOrganizationName = _ViptelaSecurityOrganizationName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 162),
    _ViptelaSecurityOrganizationName_Type()
)
viptelaSecurityOrganizationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaSecurityOrganizationName.setStatus("current")
_ViptelaSecuritySpOrganizationName_Type = OctetString
_ViptelaSecuritySpOrganizationName_Object = MibScalar
viptelaSecuritySpOrganizationName = _ViptelaSecuritySpOrganizationName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 163),
    _ViptelaSecuritySpOrganizationName_Type()
)
viptelaSecuritySpOrganizationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaSecuritySpOrganizationName.setStatus("current")
_ViptelaBfdFlapReason_Type = BfdFlapReasonEnum
_ViptelaBfdFlapReason_Object = MibScalar
viptelaBfdFlapReason = _ViptelaBfdFlapReason_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 164),
    _ViptelaBfdFlapReason_Type()
)
viptelaBfdFlapReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaBfdFlapReason.setStatus("current")
_ViptelaSecurityPeerVmanageSystemIp_Type = ViptelaIpAddress
_ViptelaSecurityPeerVmanageSystemIp_Object = MibScalar
viptelaSecurityPeerVmanageSystemIp = _ViptelaSecurityPeerVmanageSystemIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 165),
    _ViptelaSecurityPeerVmanageSystemIp_Type()
)
viptelaSecurityPeerVmanageSystemIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaSecurityPeerVmanageSystemIp.setStatus("current")
_ViptelaPolicySvcVpnId_Type = VpnId
_ViptelaPolicySvcVpnId_Object = MibScalar
viptelaPolicySvcVpnId = _ViptelaPolicySvcVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 166),
    _ViptelaPolicySvcVpnId_Type()
)
viptelaPolicySvcVpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaPolicySvcVpnId.setStatus("current")
_ViptelaPolicyZonePair_Type = OctetString
_ViptelaPolicyZonePair_Object = MibScalar
viptelaPolicyZonePair = _ViptelaPolicyZonePair_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 167),
    _ViptelaPolicyZonePair_Type()
)
viptelaPolicyZonePair.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaPolicyZonePair.setStatus("current")
_ViptelaPolicySourceVpn_Type = VpnId
_ViptelaPolicySourceVpn_Object = MibScalar
viptelaPolicySourceVpn = _ViptelaPolicySourceVpn_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 168),
    _ViptelaPolicySourceVpn_Type()
)
viptelaPolicySourceVpn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaPolicySourceVpn.setStatus("current")
_ViptelaPolicyDestinationVpn_Type = VpnId
_ViptelaPolicyDestinationVpn_Object = MibScalar
viptelaPolicyDestinationVpn = _ViptelaPolicyDestinationVpn_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 169),
    _ViptelaPolicyDestinationVpn_Type()
)
viptelaPolicyDestinationVpn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaPolicyDestinationVpn.setStatus("current")
_ViptelaPolicyState_Type = OctetString
_ViptelaPolicyState_Object = MibScalar
viptelaPolicyState = _ViptelaPolicyState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 170),
    _ViptelaPolicyState_Type()
)
viptelaPolicyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaPolicyState.setStatus("current")
_ViptelaPolicyCurrFlows_Type = Unsigned32
_ViptelaPolicyCurrFlows_Object = MibScalar
viptelaPolicyCurrFlows = _ViptelaPolicyCurrFlows_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 171),
    _ViptelaPolicyCurrFlows_Type()
)
viptelaPolicyCurrFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaPolicyCurrFlows.setStatus("current")
_ViptelaPolicyHthreshFlows_Type = Unsigned32
_ViptelaPolicyHthreshFlows_Object = MibScalar
viptelaPolicyHthreshFlows = _ViptelaPolicyHthreshFlows_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 172),
    _ViptelaPolicyHthreshFlows_Type()
)
viptelaPolicyHthreshFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaPolicyHthreshFlows.setStatus("current")
_ViptelaPolicyLthreshFlows_Type = Unsigned32
_ViptelaPolicyLthreshFlows_Object = MibScalar
viptelaPolicyLthreshFlows = _ViptelaPolicyLthreshFlows_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 173),
    _ViptelaPolicyLthreshFlows_Type()
)
viptelaPolicyLthreshFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaPolicyLthreshFlows.setStatus("current")
_ViptelaPolicyMaxFlows_Type = Unsigned32
_ViptelaPolicyMaxFlows_Object = MibScalar
viptelaPolicyMaxFlows = _ViptelaPolicyMaxFlows_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 174),
    _ViptelaPolicyMaxFlows_Type()
)
viptelaPolicyMaxFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaPolicyMaxFlows.setStatus("current")
_ViptelaPolicyAction_Type = OctetString
_ViptelaPolicyAction_Object = MibScalar
viptelaPolicyAction = _ViptelaPolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 175),
    _ViptelaPolicyAction_Type()
)
viptelaPolicyAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaPolicyAction.setStatus("current")
_ViptelaPolicyCurrHalfOpenFlows_Type = Unsigned32
_ViptelaPolicyCurrHalfOpenFlows_Object = MibScalar
viptelaPolicyCurrHalfOpenFlows = _ViptelaPolicyCurrHalfOpenFlows_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 176),
    _ViptelaPolicyCurrHalfOpenFlows_Type()
)
viptelaPolicyCurrHalfOpenFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaPolicyCurrHalfOpenFlows.setStatus("current")
_ViptelaPolicyHthreshHalfOpenFlows_Type = Unsigned32
_ViptelaPolicyHthreshHalfOpenFlows_Object = MibScalar
viptelaPolicyHthreshHalfOpenFlows = _ViptelaPolicyHthreshHalfOpenFlows_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 177),
    _ViptelaPolicyHthreshHalfOpenFlows_Type()
)
viptelaPolicyHthreshHalfOpenFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaPolicyHthreshHalfOpenFlows.setStatus("current")
_ViptelaPolicyMaxHalfOpenFlows_Type = Unsigned32
_ViptelaPolicyMaxHalfOpenFlows_Object = MibScalar
viptelaPolicyMaxHalfOpenFlows = _ViptelaPolicyMaxHalfOpenFlows_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 178),
    _ViptelaPolicyMaxHalfOpenFlows_Type()
)
viptelaPolicyMaxHalfOpenFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaPolicyMaxHalfOpenFlows.setStatus("current")
_ViptelaPolicyLthreshHalfOpenFlows_Type = Unsigned32
_ViptelaPolicyLthreshHalfOpenFlows_Object = MibScalar
viptelaPolicyLthreshHalfOpenFlows = _ViptelaPolicyLthreshHalfOpenFlows_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 179),
    _ViptelaPolicyLthreshHalfOpenFlows_Type()
)
viptelaPolicyLthreshHalfOpenFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaPolicyLthreshHalfOpenFlows.setStatus("current")
_ViptelaPolicySlaName_Type = OctetString
_ViptelaPolicySlaName_Object = MibScalar
viptelaPolicySlaName = _ViptelaPolicySlaName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 180),
    _ViptelaPolicySlaName_Type()
)
viptelaPolicySlaName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaPolicySlaName.setStatus("current")
_ViptelaPolicySlaOperation_Type = OctetString
_ViptelaPolicySlaOperation_Object = MibScalar
viptelaPolicySlaOperation = _ViptelaPolicySlaOperation_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 181),
    _ViptelaPolicySlaOperation_Type()
)
viptelaPolicySlaOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaPolicySlaOperation.setStatus("current")
_ViptelaPolicySlaLoss_Type = UnsignedByte
_ViptelaPolicySlaLoss_Object = MibScalar
viptelaPolicySlaLoss = _ViptelaPolicySlaLoss_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 182),
    _ViptelaPolicySlaLoss_Type()
)
viptelaPolicySlaLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaPolicySlaLoss.setStatus("current")
_ViptelaPolicySlaLatency_Type = Unsigned32
_ViptelaPolicySlaLatency_Object = MibScalar
viptelaPolicySlaLatency = _ViptelaPolicySlaLatency_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 183),
    _ViptelaPolicySlaLatency_Type()
)
viptelaPolicySlaLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaPolicySlaLatency.setStatus("current")
_ViptelaPolicySlaJitter_Type = Unsigned32
_ViptelaPolicySlaJitter_Object = MibScalar
viptelaPolicySlaJitter = _ViptelaPolicySlaJitter_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 184),
    _ViptelaPolicySlaJitter_Type()
)
viptelaPolicySlaJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaPolicySlaJitter.setStatus("current")
_ViptelaPolicyDevicePolicyName_Type = OctetString
_ViptelaPolicyDevicePolicyName_Object = MibScalar
viptelaPolicyDevicePolicyName = _ViptelaPolicyDevicePolicyName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 185),
    _ViptelaPolicyDevicePolicyName_Type()
)
viptelaPolicyDevicePolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaPolicyDevicePolicyName.setStatus("current")
_ViptelaWwanQosState_Type = WwanQosStatusEnum
_ViptelaWwanQosState_Object = MibScalar
viptelaWwanQosState = _ViptelaWwanQosState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 186),
    _ViptelaWwanQosState_Type()
)
viptelaWwanQosState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaWwanQosState.setStatus("current")
_ViptelaSecuritySubjectSerialNumber_Type = OctetString
_ViptelaSecuritySubjectSerialNumber_Object = MibScalar
viptelaSecuritySubjectSerialNumber = _ViptelaSecuritySubjectSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 41916, 100, 1, 187),
    _ViptelaSecuritySubjectSerialNumber_Type()
)
viptelaSecuritySubjectSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viptelaSecuritySubjectSerialNumber.setStatus("current")
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2)
)

# Managed Objects groups


# Notification objects

viptelaActionsSystemSoftwareInstallStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 1)
)
viptelaActionsSystemSoftwareInstallStatus.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaActionsStatus"),
        ("VIPTELA-TRAPS", "viptelaActionsInstallId"),
        ("VIPTELA-TRAPS", "viptelaActionsMessage"))
)
if mibBuilder.loadTexts:
    viptelaActionsSystemSoftwareInstallStatus.setStatus(
        "current"
    )

viptelaActionsSystemRebootIssued = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 2)
)
viptelaActionsSystemRebootIssued.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaActionsRebootReason"))
)
if mibBuilder.loadTexts:
    viptelaActionsSystemRebootIssued.setStatus(
        "current"
    )

viptelaActionsSystemRebootComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 3)
)
viptelaActionsSystemRebootComplete.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"))
)
if mibBuilder.loadTexts:
    viptelaActionsSystemRebootComplete.setStatus(
        "current"
    )

viptelaBfdBfdStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 4)
)
viptelaBfdBfdStateChange.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaBfdSrcIp"),
        ("VIPTELA-TRAPS", "viptelaBfdDstIp"),
        ("VIPTELA-TRAPS", "viptelaBfdProto"),
        ("VIPTELA-TRAPS", "viptelaBfdSrcPort"),
        ("VIPTELA-TRAPS", "viptelaBfdDstPort"),
        ("VIPTELA-TRAPS", "viptelaBfdLocalSystemIp"),
        ("VIPTELA-TRAPS", "viptelaBfdLocalColor"),
        ("VIPTELA-TRAPS", "viptelaBfdRemoteSystemIp"),
        ("VIPTELA-TRAPS", "viptelaBfdRemoteColor"),
        ("VIPTELA-TRAPS", "viptelaBfdNewState"),
        ("VIPTELA-TRAPS", "viptelaBfdDeleted"),
        ("VIPTELA-TRAPS", "viptelaBfdFlapReason"))
)
if mibBuilder.loadTexts:
    viptelaBfdBfdStateChange.setStatus(
        "current"
    )

viptelaHardwareFlashFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 5)
)
viptelaHardwareFlashFault.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaHardwareNewState"))
)
if mibBuilder.loadTexts:
    viptelaHardwareFlashFault.setStatus(
        "current"
    )

viptelaHardwareEmmcFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 6)
)
viptelaHardwareEmmcFault.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaHardwareNewState"))
)
if mibBuilder.loadTexts:
    viptelaHardwareEmmcFault.setStatus(
        "current"
    )

viptelaHardwareSdcardFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 7)
)
viptelaHardwareSdcardFault.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaHardwareNewState"))
)
if mibBuilder.loadTexts:
    viptelaHardwareSdcardFault.setStatus(
        "current"
    )

viptelaHardwareTempsensorFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 8)
)
viptelaHardwareTempsensorFault.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaHardwareHwSensorType"),
        ("VIPTELA-TRAPS", "viptelaHardwareHwDevIndex"),
        ("VIPTELA-TRAPS", "viptelaHardwareName"),
        ("VIPTELA-TRAPS", "viptelaHardwareNewState"))
)
if mibBuilder.loadTexts:
    viptelaHardwareTempsensorFault.setStatus(
        "current"
    )

viptelaHardwareTempsensorState = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 9)
)
viptelaHardwareTempsensorState.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaHardwareHwSensorType"),
        ("VIPTELA-TRAPS", "viptelaHardwareHwDevIndex"),
        ("VIPTELA-TRAPS", "viptelaHardwareName"),
        ("VIPTELA-TRAPS", "viptelaHardwareTemp"),
        ("VIPTELA-TRAPS", "viptelaHardwareSensorNewState"))
)
if mibBuilder.loadTexts:
    viptelaHardwareTempsensorState.setStatus(
        "current"
    )

viptelaHardwareFanFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 10)
)
viptelaHardwareFanFault.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaHardwareFantrayId"),
        ("VIPTELA-TRAPS", "viptelaHardwareFanId"),
        ("VIPTELA-TRAPS", "viptelaHardwareNewState"))
)
if mibBuilder.loadTexts:
    viptelaHardwareFanFault.setStatus(
        "current"
    )

viptelaHardwareFantrayFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 11)
)
viptelaHardwareFantrayFault.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaHardwareFantrayId"),
        ("VIPTELA-TRAPS", "viptelaHardwareNewState"))
)
if mibBuilder.loadTexts:
    viptelaHardwareFantrayFault.setStatus(
        "current"
    )

viptelaHardwarePemFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 12)
)
viptelaHardwarePemFault.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaHardwarePemId"),
        ("VIPTELA-TRAPS", "viptelaHardwareNewState"))
)
if mibBuilder.loadTexts:
    viptelaHardwarePemFault.setStatus(
        "current"
    )

viptelaHardwarePemStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 13)
)
viptelaHardwarePemStateChange.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaHardwarePemId"),
        ("VIPTELA-TRAPS", "viptelaHardwareNewState"))
)
if mibBuilder.loadTexts:
    viptelaHardwarePemStateChange.setStatus(
        "current"
    )

viptelaHardwarePimFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 14)
)
viptelaHardwarePimFault.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaHardwarePimId"),
        ("VIPTELA-TRAPS", "viptelaHardwareNewState"))
)
if mibBuilder.loadTexts:
    viptelaHardwarePimFault.setStatus(
        "current"
    )

viptelaHardwarePimStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 15)
)
viptelaHardwarePimStateChange.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaHardwarePimId"),
        ("VIPTELA-TRAPS", "viptelaHardwareNewState"))
)
if mibBuilder.loadTexts:
    viptelaHardwarePimStateChange.setStatus(
        "current"
    )

viptelaHardwareSfpStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 16)
)
viptelaHardwareSfpStateChange.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaHardwareSfpName"),
        ("VIPTELA-TRAPS", "viptelaHardwareNewState"))
)
if mibBuilder.loadTexts:
    viptelaHardwareSfpStateChange.setStatus(
        "current"
    )

viptelaHardwareUsbStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 17)
)
viptelaHardwareUsbStateChange.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaHardwareUsbSlot"),
        ("VIPTELA-TRAPS", "viptelaHardwareNewState"))
)
if mibBuilder.loadTexts:
    viptelaHardwareUsbStateChange.setStatus(
        "current"
    )

viptelaOmpOmpNumberOfVsmartsChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 18)
)
viptelaOmpOmpNumberOfVsmartsChange.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaOmpNumberOfVsmarts"))
)
if mibBuilder.loadTexts:
    viptelaOmpOmpNumberOfVsmartsChange.setStatus(
        "current"
    )

viptelaOmpOmpStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 19)
)
viptelaOmpOmpStateChange.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaOmpNewState"))
)
if mibBuilder.loadTexts:
    viptelaOmpOmpStateChange.setStatus(
        "current"
    )

viptelaOmpOmpPeerStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 20)
)
viptelaOmpOmpPeerStateChange.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaOmpPeer"),
        ("VIPTELA-TRAPS", "viptelaOmpPeerNewState"))
)
if mibBuilder.loadTexts:
    viptelaOmpOmpPeerStateChange.setStatus(
        "current"
    )

viptelaOmpOmpTlocStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 21)
)
viptelaOmpOmpTlocStateChange.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaOmpOmpAddressFamily"))
)
if mibBuilder.loadTexts:
    viptelaOmpOmpTlocStateChange.setStatus(
        "current"
    )

viptelaOmpOmpPolicy = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 22)
)
viptelaOmpOmpPolicy.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaOmpPolicy"),
        ("VIPTELA-TRAPS", "viptelaOmpVsmartPeer"))
)
if mibBuilder.loadTexts:
    viptelaOmpOmpPolicy.setStatus(
        "current"
    )

viptelaSecurityControlConnectionStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 23)
)
viptelaSecurityControlConnectionStateChange.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaSecurityPersonality"),
        ("VIPTELA-TRAPS", "viptelaSecurityPeerType"),
        ("VIPTELA-TRAPS", "viptelaSecurityPeerSystemIp"),
        ("VIPTELA-TRAPS", "viptelaSecurityPeerVmanageSystemIp"),
        ("VIPTELA-TRAPS", "viptelaSecurityPublicIp"),
        ("VIPTELA-TRAPS", "viptelaSecurityPublicPort"),
        ("VIPTELA-TRAPS", "viptelaSecuritySrcColor"),
        ("VIPTELA-TRAPS", "viptelaSecurityRemoteColor"),
        ("VIPTELA-TRAPS", "viptelaSecurityUptime"),
        ("VIPTELA-TRAPS", "viptelaSecurityNewState"))
)
if mibBuilder.loadTexts:
    viptelaSecurityControlConnectionStateChange.setStatus(
        "current"
    )

viptelaSecurityControlConnectionAuthFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 24)
)
viptelaSecurityControlConnectionAuthFail.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaSecurityPersonality"),
        ("VIPTELA-TRAPS", "viptelaSecurityPeerType"),
        ("VIPTELA-TRAPS", "viptelaSecurityPeerSystemIp"),
        ("VIPTELA-TRAPS", "viptelaSecurityLocalSystemIp"),
        ("VIPTELA-TRAPS", "viptelaSecurityLocalColor"),
        ("VIPTELA-TRAPS", "viptelaSecurityReason"))
)
if mibBuilder.loadTexts:
    viptelaSecurityControlConnectionAuthFail.setStatus(
        "current"
    )

viptelaSecurityControlVbondStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 25)
)
viptelaSecurityControlVbondStateChange.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaSecurityPersonality"),
        ("VIPTELA-TRAPS", "viptelaSecurityNewState"))
)
if mibBuilder.loadTexts:
    viptelaSecurityControlVbondStateChange.setStatus(
        "current"
    )

viptelaSecurityControlConnectionTlocIpChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 26)
)
viptelaSecurityControlConnectionTlocIpChange.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaSecurityPersonality"),
        ("VIPTELA-TRAPS", "viptelaSecurityOldPublicIp"),
        ("VIPTELA-TRAPS", "viptelaSecurityOldPublicPort"),
        ("VIPTELA-TRAPS", "viptelaSecurityNewPublicIp"),
        ("VIPTELA-TRAPS", "viptelaSecurityNewPublicPort"))
)
if mibBuilder.loadTexts:
    viptelaSecurityControlConnectionTlocIpChange.setStatus(
        "current"
    )

viptelaSecurityControlNoActiveVsmart = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 27)
)
viptelaSecurityControlNoActiveVsmart.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaSecurityPersonality"))
)
if mibBuilder.loadTexts:
    viptelaSecurityControlNoActiveVsmart.setStatus(
        "current"
    )

viptelaSecurityControlNoActiveVbond = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 28)
)
viptelaSecurityControlNoActiveVbond.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaSecurityPersonality"))
)
if mibBuilder.loadTexts:
    viptelaSecurityControlNoActiveVbond.setStatus(
        "current"
    )

viptelaSecurityTunnelIpsecRekey = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 29)
)
viptelaSecurityTunnelIpsecRekey.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaSecurityPersonality"),
        ("VIPTELA-TRAPS", "viptelaSecurityColor"))
)
if mibBuilder.loadTexts:
    viptelaSecurityTunnelIpsecRekey.setStatus(
        "current"
    )

viptelaSecurityTunnelIpsecManualRekey = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 30)
)
viptelaSecurityTunnelIpsecManualRekey.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaSecurityPersonality"),
        ("VIPTELA-TRAPS", "viptelaSecurityColor"))
)
if mibBuilder.loadTexts:
    viptelaSecurityTunnelIpsecManualRekey.setStatus(
        "current"
    )

viptelaSecuritySecurityRootCertChainInstalled = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 31)
)
viptelaSecuritySecurityRootCertChainInstalled.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"))
)
if mibBuilder.loadTexts:
    viptelaSecuritySecurityRootCertChainInstalled.setStatus(
        "current"
    )

viptelaSecuritySecurityCertificateInstalled = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 32)
)
viptelaSecuritySecurityCertificateInstalled.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"))
)
if mibBuilder.loadTexts:
    viptelaSecuritySecurityCertificateInstalled.setStatus(
        "current"
    )

viptelaSecuritySecurityNewCsrGenerated = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 33)
)
viptelaSecuritySecurityNewCsrGenerated.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"))
)
if mibBuilder.loadTexts:
    viptelaSecuritySecurityNewCsrGenerated.setStatus(
        "current"
    )

viptelaSecuritySecurityRootCertChainUninstalled = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 34)
)
viptelaSecuritySecurityRootCertChainUninstalled.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"))
)
if mibBuilder.loadTexts:
    viptelaSecuritySecurityRootCertChainUninstalled.setStatus(
        "current"
    )

viptelaSecuritySecurityClearInstalledCertificate = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 35)
)
viptelaSecuritySecurityClearInstalledCertificate.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"))
)
if mibBuilder.loadTexts:
    viptelaSecuritySecurityClearInstalledCertificate.setStatus(
        "current"
    )

viptelaSecuritySecurityVedgeSerialFileUploaded = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 36)
)
viptelaSecuritySecurityVedgeSerialFileUploaded.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"))
)
if mibBuilder.loadTexts:
    viptelaSecuritySecurityVedgeSerialFileUploaded.setStatus(
        "current"
    )

viptelaSecuritySecurityVsmartSerialFileUploaded = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 37)
)
viptelaSecuritySecurityVsmartSerialFileUploaded.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"))
)
if mibBuilder.loadTexts:
    viptelaSecuritySecurityVsmartSerialFileUploaded.setStatus(
        "current"
    )

viptelaSecuritySecurityVedgeEntryAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 38)
)
viptelaSecuritySecurityVedgeEntryAdded.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaSecurityUuid"),
        ("VIPTELA-TRAPS", "viptelaSecuritySerial"))
)
if mibBuilder.loadTexts:
    viptelaSecuritySecurityVedgeEntryAdded.setStatus(
        "current"
    )

viptelaSecuritySecurityVedgeEntryRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 39)
)
viptelaSecuritySecurityVedgeEntryRemoved.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaSecurityUuid"))
)
if mibBuilder.loadTexts:
    viptelaSecuritySecurityVedgeEntryRemoved.setStatus(
        "current"
    )

viptelaSecuritySecurityVsmartEntryAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 40)
)
viptelaSecuritySecurityVsmartEntryAdded.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaSecuritySerial"))
)
if mibBuilder.loadTexts:
    viptelaSecuritySecurityVsmartEntryAdded.setStatus(
        "current"
    )

viptelaSecuritySecurityVsmartEntryRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 41)
)
viptelaSecuritySecurityVsmartEntryRemoved.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaSecuritySerial"))
)
if mibBuilder.loadTexts:
    viptelaSecuritySecurityVsmartEntryRemoved.setStatus(
        "current"
    )

viptelaSystemProcessRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 42)
)
viptelaSystemProcessRestart.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaSystemProcessName"),
        ("VIPTELA-TRAPS", "viptelaSystemProcessId"),
        ("VIPTELA-TRAPS", "viptelaSystemReason"))
)
if mibBuilder.loadTexts:
    viptelaSystemProcessRestart.setStatus(
        "current"
    )

viptelaSystemDiskUsage = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 43)
)
viptelaSystemDiskUsage.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaSystemWarning"),
        ("VIPTELA-TRAPS", "viptelaSystemTotalMb"),
        ("VIPTELA-TRAPS", "viptelaSystemFreeMb"))
)
if mibBuilder.loadTexts:
    viptelaSystemDiskUsage.setStatus(
        "current"
    )

viptelaSystemMemoryUsage = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 44)
)
viptelaSystemMemoryUsage.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaSystemWarning"),
        ("VIPTELA-TRAPS", "viptelaSystemTotalMb"),
        ("VIPTELA-TRAPS", "viptelaSystemFreeMb"))
)
if mibBuilder.loadTexts:
    viptelaSystemMemoryUsage.setStatus(
        "current"
    )

viptelaSystemAaaAdminPwdChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 45)
)
viptelaSystemAaaAdminPwdChange.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"))
)
if mibBuilder.loadTexts:
    viptelaSystemAaaAdminPwdChange.setStatus(
        "current"
    )

viptelaSystemSiteIdChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 46)
)
viptelaSystemSiteIdChange.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaSystemOldSiteId"),
        ("VIPTELA-TRAPS", "viptelaSystemNewSiteId"))
)
if mibBuilder.loadTexts:
    viptelaSystemSiteIdChange.setStatus(
        "current"
    )

viptelaSystemDomainIdChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 47)
)
viptelaSystemDomainIdChange.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaSystemOldDomainId"),
        ("VIPTELA-TRAPS", "viptelaSystemNewDomainId"))
)
if mibBuilder.loadTexts:
    viptelaSystemDomainIdChange.setStatus(
        "current"
    )

viptelaSystemSystemIpChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 48)
)
viptelaSystemSystemIpChange.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaSystemOldSystemIp"),
        ("VIPTELA-TRAPS", "viptelaSystemNewSystemIp"))
)
if mibBuilder.loadTexts:
    viptelaSystemSystemIpChange.setStatus(
        "current"
    )

viptelaSystemOrgNameChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 49)
)
viptelaSystemOrgNameChange.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaSystemOldOrganizationName"),
        ("VIPTELA-TRAPS", "viptelaSystemNewOrganizationName"))
)
if mibBuilder.loadTexts:
    viptelaSystemOrgNameChange.setStatus(
        "current"
    )

viptelaSystemSystemLoginChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 50)
)
viptelaSystemSystemLoginChange.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaSystemUserName"),
        ("VIPTELA-TRAPS", "viptelaSystemUserId"))
)
if mibBuilder.loadTexts:
    viptelaSystemSystemLoginChange.setStatus(
        "current"
    )

viptelaSystemSystemLogoutChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 51)
)
viptelaSystemSystemLogoutChange.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaSystemUserName"),
        ("VIPTELA-TRAPS", "viptelaSystemUserId"))
)
if mibBuilder.loadTexts:
    viptelaSystemSystemLogoutChange.setStatus(
        "current"
    )

viptelaSystemSystemAaaLoginFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 52)
)
viptelaSystemSystemAaaLoginFail.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaSystemUserName"),
        ("VIPTELA-TRAPS", "viptelaSystemRemoteHost"))
)
if mibBuilder.loadTexts:
    viptelaSystemSystemAaaLoginFail.setStatus(
        "current"
    )

viptelaSystemSystemCommit = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 53)
)
viptelaSystemSystemCommit.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaSystemUserName"))
)
if mibBuilder.loadTexts:
    viptelaSystemSystemCommit.setStatus(
        "current"
    )

viptelaVpnBgpPeerStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 54)
)
viptelaVpnBgpPeerStateChange.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaVpnVpnId"),
        ("VIPTELA-TRAPS", "viptelaVpnPeer"),
        ("VIPTELA-TRAPS", "viptelaVpnBgpNewState"),
        ("VIPTELA-TRAPS", "viptelaVpnLocalAddress"),
        ("VIPTELA-TRAPS", "viptelaVpnLocalRouterid"),
        ("VIPTELA-TRAPS", "viptelaVpnPeerRouterid"))
)
if mibBuilder.loadTexts:
    viptelaVpnBgpPeerStateChange.setStatus(
        "current"
    )

viptelaVpnInterfaceStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 55)
)
viptelaVpnInterfaceStateChange.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaVpnVpnId"),
        ("VIPTELA-TRAPS", "viptelaVpnIfName"),
        ("VIPTELA-TRAPS", "viptelaVpnNewState"))
)
if mibBuilder.loadTexts:
    viptelaVpnInterfaceStateChange.setStatus(
        "current"
    )

viptelaVpnVrrpGroupStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 56)
)
viptelaVpnVrrpGroupStateChange.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaVpnVpnId"),
        ("VIPTELA-TRAPS", "viptelaVpnIfName"),
        ("VIPTELA-TRAPS", "viptelaVpnGrpId"),
        ("VIPTELA-TRAPS", "viptelaVpnVrrpGroupState"))
)
if mibBuilder.loadTexts:
    viptelaVpnVrrpGroupStateChange.setStatus(
        "current"
    )

viptelaVpnRouteInstallFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 57)
)
viptelaVpnRouteInstallFail.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaVpnIpPrefix"),
        ("VIPTELA-TRAPS", "viptelaVpnFailureReason"))
)
if mibBuilder.loadTexts:
    viptelaVpnRouteInstallFail.setStatus(
        "current"
    )

viptelaVpnTunnelInstallFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 58)
)
viptelaVpnTunnelInstallFail.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaVpnFarEndSystemIp"),
        ("VIPTELA-TRAPS", "viptelaVpnFarEndColor"),
        ("VIPTELA-TRAPS", "viptelaVpnFailureReason"))
)
if mibBuilder.loadTexts:
    viptelaVpnTunnelInstallFail.setStatus(
        "current"
    )

viptelaVpnDhcpAddressAssigned = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 59)
)
viptelaVpnDhcpAddressAssigned.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaVpnVpnId"),
        ("VIPTELA-TRAPS", "viptelaVpnIfName"),
        ("VIPTELA-TRAPS", "viptelaVpnClientMac"),
        ("VIPTELA-TRAPS", "viptelaVpnIp"))
)
if mibBuilder.loadTexts:
    viptelaVpnDhcpAddressAssigned.setStatus(
        "current"
    )

viptelaVpnDhcpAddressRenewed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 60)
)
viptelaVpnDhcpAddressRenewed.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaVpnVpnId"),
        ("VIPTELA-TRAPS", "viptelaVpnIfName"),
        ("VIPTELA-TRAPS", "viptelaVpnClientMac"),
        ("VIPTELA-TRAPS", "viptelaVpnIp"))
)
if mibBuilder.loadTexts:
    viptelaVpnDhcpAddressRenewed.setStatus(
        "current"
    )

viptelaVpnDhcpAddressReleased = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 61)
)
viptelaVpnDhcpAddressReleased.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaVpnVpnId"),
        ("VIPTELA-TRAPS", "viptelaVpnIfName"),
        ("VIPTELA-TRAPS", "viptelaVpnClientMac"),
        ("VIPTELA-TRAPS", "viptelaVpnIp"),
        ("VIPTELA-TRAPS", "viptelaVpnReason"))
)
if mibBuilder.loadTexts:
    viptelaVpnDhcpAddressReleased.setStatus(
        "current"
    )

viptelaVpnDhcpRequestRejected = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 62)
)
viptelaVpnDhcpRequestRejected.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaVpnVpnId"),
        ("VIPTELA-TRAPS", "viptelaVpnIfName"),
        ("VIPTELA-TRAPS", "viptelaVpnClientMac"),
        ("VIPTELA-TRAPS", "viptelaVpnIp"),
        ("VIPTELA-TRAPS", "viptelaVpnReason"))
)
if mibBuilder.loadTexts:
    viptelaVpnDhcpRequestRejected.setStatus(
        "current"
    )

viptelaVpnDhcpServerStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 63)
)
viptelaVpnDhcpServerStateChange.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaVpnVpnId"),
        ("VIPTELA-TRAPS", "viptelaVpnIfName"),
        ("VIPTELA-TRAPS", "viptelaVpnState"))
)
if mibBuilder.loadTexts:
    viptelaVpnDhcpServerStateChange.setStatus(
        "current"
    )

viptelaVpnPimNeighborStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 64)
)
viptelaVpnPimNeighborStateChange.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaVpnVpnId"),
        ("VIPTELA-TRAPS", "viptelaVpnNeighbor"),
        ("VIPTELA-TRAPS", "viptelaVpnPimNewState"))
)
if mibBuilder.loadTexts:
    viptelaVpnPimNeighborStateChange.setStatus(
        "current"
    )

viptelaVpnPimInterfaceStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 65)
)
viptelaVpnPimInterfaceStateChange.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaVpnVpnId"),
        ("VIPTELA-TRAPS", "viptelaVpnInterface"),
        ("VIPTELA-TRAPS", "viptelaVpnOperState"),
        ("VIPTELA-TRAPS", "viptelaVpnAdminState"),
        ("VIPTELA-TRAPS", "viptelaVpnPimEnabled"))
)
if mibBuilder.loadTexts:
    viptelaVpnPimInterfaceStateChange.setStatus(
        "current"
    )

viptelaVpnPimTunnelStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 66)
)
viptelaVpnPimTunnelStateChange.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaVpnTunnelAddress"),
        ("VIPTELA-TRAPS", "viptelaVpnPimNewState"))
)
if mibBuilder.loadTexts:
    viptelaVpnPimTunnelStateChange.setStatus(
        "current"
    )

viptelaVpnOspfNeighborStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 67)
)
viptelaVpnOspfNeighborStateChange.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaVpnVpnId"),
        ("VIPTELA-TRAPS", "viptelaVpnNeighbor"),
        ("VIPTELA-TRAPS", "viptelaVpnRouterId"),
        ("VIPTELA-TRAPS", "viptelaVpnIfAddr"),
        ("VIPTELA-TRAPS", "viptelaVpnOspfNewState"))
)
if mibBuilder.loadTexts:
    viptelaVpnOspfNeighborStateChange.setStatus(
        "current"
    )

viptelaVpnOspfInterfaceStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 68)
)
viptelaVpnOspfInterfaceStateChange.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaVpnVpnId"),
        ("VIPTELA-TRAPS", "viptelaVpnInterface"),
        ("VIPTELA-TRAPS", "viptelaVpnOspfInterfaceNewState"))
)
if mibBuilder.loadTexts:
    viptelaVpnOspfInterfaceStateChange.setStatus(
        "current"
    )

viptelaSystemPseudoCommitStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 69)
)
viptelaSystemPseudoCommitStatus.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaSystemStatusStr"))
)
if mibBuilder.loadTexts:
    viptelaSystemPseudoCommitStatus.setStatus(
        "current"
    )

viptelaAppRouteSlaChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 70)
)
viptelaAppRouteSlaChange.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaAppRouteSrcIp"),
        ("VIPTELA-TRAPS", "viptelaAppRouteDstIp"),
        ("VIPTELA-TRAPS", "viptelaAppRouteProto"),
        ("VIPTELA-TRAPS", "viptelaAppRouteSrcPort"),
        ("VIPTELA-TRAPS", "viptelaAppRouteDstPort"),
        ("VIPTELA-TRAPS", "viptelaAppRouteLocalSystemIp"),
        ("VIPTELA-TRAPS", "viptelaAppRouteLocalColor"),
        ("VIPTELA-TRAPS", "viptelaAppRouteRemoteSystemIp"),
        ("VIPTELA-TRAPS", "viptelaAppRouteRemoteColor"),
        ("VIPTELA-TRAPS", "viptelaAppRouteMeanLoss"),
        ("VIPTELA-TRAPS", "viptelaAppRouteMeanLatency"),
        ("VIPTELA-TRAPS", "viptelaAppRouteMeanJitter"),
        ("VIPTELA-TRAPS", "viptelaAppRouteSlaClasses"),
        ("VIPTELA-TRAPS", "viptelaAppRouteOldSlaClasses"))
)
if mibBuilder.loadTexts:
    viptelaAppRouteSlaChange.setStatus(
        "current"
    )

viptelaSecuritySecurityCertificateExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 71)
)
viptelaSecuritySecurityCertificateExpired.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"))
)
if mibBuilder.loadTexts:
    viptelaSecuritySecurityCertificateExpired.setStatus(
        "current"
    )

viptelaVpnFibStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 72)
)
viptelaVpnFibStateChange.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaVpnVpnId"),
        ("VIPTELA-TRAPS", "viptelaVpnAddressFamilyType"),
        ("VIPTELA-TRAPS", "viptelaVpnFibLastUpdateTime"))
)
if mibBuilder.loadTexts:
    viptelaVpnFibStateChange.setStatus(
        "current"
    )

viptelaBridgeCreation = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 73)
)
viptelaBridgeCreation.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaBridgeId"))
)
if mibBuilder.loadTexts:
    viptelaBridgeCreation.setStatus(
        "current"
    )

viptelaBridgeDeletion = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 74)
)
viptelaBridgeDeletion.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaBridgeId"))
)
if mibBuilder.loadTexts:
    viptelaBridgeDeletion.setStatus(
        "current"
    )

viptelaBridgeMaxMacReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 75)
)
viptelaBridgeMaxMacReached.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaBridgeId"),
        ("VIPTELA-TRAPS", "viptelaNumMacs"))
)
if mibBuilder.loadTexts:
    viptelaBridgeMaxMacReached.setStatus(
        "current"
    )

viptelaSecurityControlVedgeListRequest = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 76)
)
viptelaSecurityControlVedgeListRequest.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaSecurityPeerType"),
        ("VIPTELA-TRAPS", "viptelaSecurityPeerSystemIp"),
        ("VIPTELA-TRAPS", "viptelaSecurityUuid"))
)
if mibBuilder.loadTexts:
    viptelaSecurityControlVedgeListRequest.setStatus(
        "current"
    )

viptelaPolicySlaViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 77)
)
viptelaPolicySlaViolation.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaPolicyVpnId"),
        ("VIPTELA-TRAPS", "viptelaPolicyApplication"),
        ("VIPTELA-TRAPS", "viptelaPolicySourceIp"),
        ("VIPTELA-TRAPS", "viptelaPolicySourcePort"),
        ("VIPTELA-TRAPS", "viptelaPolicyDestinationIp"),
        ("VIPTELA-TRAPS", "viptelaPolicyDestinationPort"),
        ("VIPTELA-TRAPS", "viptelaPolicyProtocol"),
        ("VIPTELA-TRAPS", "viptelaPolicyDscp"),
        ("VIPTELA-TRAPS", "viptelaPolicySlaInformation"),
        ("VIPTELA-TRAPS", "viptelaPolicySlaStatus"))
)
if mibBuilder.loadTexts:
    viptelaPolicySlaViolation.setStatus(
        "current"
    )

viptelaPolicySlaViolationPktDrop = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 78)
)
viptelaPolicySlaViolationPktDrop.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaPolicyVpnId"),
        ("VIPTELA-TRAPS", "viptelaPolicyApplication"),
        ("VIPTELA-TRAPS", "viptelaPolicySourceIp"),
        ("VIPTELA-TRAPS", "viptelaPolicySourcePort"),
        ("VIPTELA-TRAPS", "viptelaPolicyDestinationIp"),
        ("VIPTELA-TRAPS", "viptelaPolicyDestinationPort"),
        ("VIPTELA-TRAPS", "viptelaPolicyProtocol"),
        ("VIPTELA-TRAPS", "viptelaPolicyDscp"),
        ("VIPTELA-TRAPS", "viptelaPolicySlaInformation"),
        ("VIPTELA-TRAPS", "viptelaPolicySlaStatus"))
)
if mibBuilder.loadTexts:
    viptelaPolicySlaViolationPktDrop.setStatus(
        "current"
    )

viptelaVpnInterfacePcsFaultDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 79)
)
viptelaVpnInterfacePcsFaultDetected.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaVpnVpnId"),
        ("VIPTELA-TRAPS", "viptelaVpnIfName"),
        ("VIPTELA-TRAPS", "viptelaVpnNewState"))
)
if mibBuilder.loadTexts:
    viptelaVpnInterfacePcsFaultDetected.setStatus(
        "current"
    )

viptelaSystemAppDpiFlowsOutOfMemory = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 80)
)
viptelaSystemAppDpiFlowsOutOfMemory.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaSystemDpiOutOfMemoryState"))
)
if mibBuilder.loadTexts:
    viptelaSystemAppDpiFlowsOutOfMemory.setStatus(
        "current"
    )

viptelaSecurityGreStateUpdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 81)
)
viptelaSecurityGreStateUpdate.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaSecurityGreOldOperState"),
        ("VIPTELA-TRAPS", "viptelaSecurityGreNewOperState"),
        ("VIPTELA-TRAPS", "viptelaSecurityGreIfName"),
        ("VIPTELA-TRAPS", "viptelaSecurityGreVpnId"),
        ("VIPTELA-TRAPS", "viptelaSecurityGreTunnelSource"),
        ("VIPTELA-TRAPS", "viptelaSecurityGreTunnelDestination"),
        ("VIPTELA-TRAPS", "viptelaSecurityGreGreIp"))
)
if mibBuilder.loadTexts:
    viptelaSecurityGreStateUpdate.setStatus(
        "current"
    )

viptelaVpnInterfaceBw = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 82)
)
viptelaVpnInterfaceBw.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaVpnVpnId"),
        ("VIPTELA-TRAPS", "viptelaVpnIfName"),
        ("VIPTELA-TRAPS", "viptelaVpnIfCfgBwKbps"),
        ("VIPTELA-TRAPS", "viptelaVpnTrafficDirection"),
        ("VIPTELA-TRAPS", "viptelaVpnDuration"))
)
if mibBuilder.loadTexts:
    viptelaVpnInterfaceBw.setStatus(
        "current"
    )

viptelaHardwareSfpSupportState = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 83)
)
viptelaHardwareSfpSupportState.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaHardwareSfpName"),
        ("VIPTELA-TRAPS", "viptelaHardwareNewState"))
)
if mibBuilder.loadTexts:
    viptelaHardwareSfpSupportState.setStatus(
        "current"
    )

viptelaPolicyDataPolicyAssociationStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 84)
)
viptelaPolicyDataPolicyAssociationStatus.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaPolicyVpnListName"),
        ("VIPTELA-TRAPS", "viptelaPolicyName"),
        ("VIPTELA-TRAPS", "viptelaPolicyStatus"))
)
if mibBuilder.loadTexts:
    viptelaPolicyDataPolicyAssociationStatus.setStatus(
        "current"
    )

viptelaPolicyAccessListAssociationStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 85)
)
viptelaPolicyAccessListAssociationStatus.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaPolicyAccessListName"),
        ("VIPTELA-TRAPS", "viptelaPolicyStatus"))
)
if mibBuilder.loadTexts:
    viptelaPolicyAccessListAssociationStatus.setStatus(
        "current"
    )

viptelaSecurityVmanageConnectionPreferenceChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 86)
)
viptelaSecurityVmanageConnectionPreferenceChanged.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaSecurityColor"),
        ("VIPTELA-TRAPS", "viptelaSecurityVmanageConnectionPreference"))
)
if mibBuilder.loadTexts:
    viptelaSecurityVmanageConnectionPreferenceChanged.setStatus(
        "current"
    )

viptelaVpnCloudExpressMaxLocalExitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 87)
)
viptelaVpnCloudExpressMaxLocalExitExceeded.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"))
)
if mibBuilder.loadTexts:
    viptelaVpnCloudExpressMaxLocalExitExceeded.setStatus(
        "current"
    )

viptelaVpnCloudExpressApplicationChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 88)
)
viptelaVpnCloudExpressApplicationChange.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaVpnVpnId"),
        ("VIPTELA-TRAPS", "viptelaCloudExpressApplication"),
        ("VIPTELA-TRAPS", "viptelaCloudExpressExitType"),
        ("VIPTELA-TRAPS", "viptelaGatewayIp"),
        ("VIPTELA-TRAPS", "viptelaVpnInterface"),
        ("VIPTELA-TRAPS", "viptelaAppLatency"),
        ("VIPTELA-TRAPS", "viptelaAppLoss"),
        ("VIPTELA-TRAPS", "viptelaExitLocalColor"),
        ("VIPTELA-TRAPS", "viptelaExitRemoteColor"))
)
if mibBuilder.loadTexts:
    viptelaVpnCloudExpressApplicationChange.setStatus(
        "current"
    )

viptelaVpnCloudExpressScoreChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 89)
)
viptelaVpnCloudExpressScoreChange.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaVpnVpnId"),
        ("VIPTELA-TRAPS", "viptelaCloudExpressApplication"),
        ("VIPTELA-TRAPS", "viptelaCloudExpressExitType"),
        ("VIPTELA-TRAPS", "viptelaGatewayIp"),
        ("VIPTELA-TRAPS", "viptelaVpnInterface"),
        ("VIPTELA-TRAPS", "viptelaAppLatency"),
        ("VIPTELA-TRAPS", "viptelaAppLoss"),
        ("VIPTELA-TRAPS", "viptelaExitLocalColor"),
        ("VIPTELA-TRAPS", "viptelaExitRemoteColor"))
)
if mibBuilder.loadTexts:
    viptelaVpnCloudExpressScoreChange.setStatus(
        "current"
    )

viptelaWwanSimStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 90)
)
viptelaWwanSimStateChange.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaWwanSimSlot"),
        ("VIPTELA-TRAPS", "viptelaWwanSimState"))
)
if mibBuilder.loadTexts:
    viptelaWwanSimStateChange.setStatus(
        "current"
    )

viptelaSystemAppDpiFlowsWriteFailedVedge = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 91)
)
viptelaSystemAppDpiFlowsWriteFailedVedge.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"))
)
if mibBuilder.loadTexts:
    viptelaSystemAppDpiFlowsWriteFailedVedge.setStatus(
        "current"
    )

viptelaVpnInterfaceAdminStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 92)
)
viptelaVpnInterfaceAdminStateChange.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaVpnVpnId"),
        ("VIPTELA-TRAPS", "viptelaVpnIfName"),
        ("VIPTELA-TRAPS", "viptelaVpnNewAdminState"))
)
if mibBuilder.loadTexts:
    viptelaVpnInterfaceAdminStateChange.setStatus(
        "current"
    )

viptelaWwanDomainStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 93)
)
viptelaWwanDomainStateChange.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaWwanIfname"),
        ("VIPTELA-TRAPS", "viptelaWwanDomainState"))
)
if mibBuilder.loadTexts:
    viptelaWwanDomainStateChange.setStatus(
        "current"
    )

viptelaWwanRegStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 94)
)
viptelaWwanRegStateChange.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaWwanIfname"),
        ("VIPTELA-TRAPS", "viptelaWwanRegState"))
)
if mibBuilder.loadTexts:
    viptelaWwanRegStateChange.setStatus(
        "current"
    )

viptelaWwanBearerChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 95)
)
viptelaWwanBearerChange.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaWwanIfname"),
        ("VIPTELA-TRAPS", "viptelaWwanBearer"))
)
if mibBuilder.loadTexts:
    viptelaWwanBearerChange.setStatus(
        "current"
    )

viptelaSystemProcessDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 96)
)
viptelaSystemProcessDown.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaSystemProcessName"),
        ("VIPTELA-TRAPS", "viptelaSystemProcessId"),
        ("VIPTELA-TRAPS", "viptelaSystemReason"))
)
if mibBuilder.loadTexts:
    viptelaSystemProcessDown.setStatus(
        "current"
    )

viptelaActionsSystemRebootAborted = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 97)
)
viptelaActionsSystemRebootAborted.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaActionsReason"))
)
if mibBuilder.loadTexts:
    viptelaActionsSystemRebootAborted.setStatus(
        "current"
    )

viptelaSecurityVbondRejectVedgeConnection = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 98)
)
viptelaSecurityVbondRejectVedgeConnection.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaSecurityUuid"),
        ("VIPTELA-TRAPS", "viptelaSecurityOrganizationName"),
        ("VIPTELA-TRAPS", "viptelaSecuritySpOrganizationName"),
        ("VIPTELA-TRAPS", "viptelaSecurityReason"))
)
if mibBuilder.loadTexts:
    viptelaSecurityVbondRejectVedgeConnection.setStatus(
        "current"
    )

viptelaSecurityDeviceTemplateMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 99)
)
viptelaSecurityDeviceTemplateMissing.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaSecurityUuid"),
        ("VIPTELA-TRAPS", "viptelaSecurityPeerType"))
)
if mibBuilder.loadTexts:
    viptelaSecurityDeviceTemplateMissing.setStatus(
        "current"
    )

viptelaSecurityDeviceTemplateAttachedDuringZtp = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 100)
)
viptelaSecurityDeviceTemplateAttachedDuringZtp.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaSecurityUuid"),
        ("VIPTELA-TRAPS", "viptelaSecurityPeerType"))
)
if mibBuilder.loadTexts:
    viptelaSecurityDeviceTemplateAttachedDuringZtp.setStatus(
        "current"
    )

viptelaPolicyZbfFlowCreation = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 101)
)
viptelaPolicyZbfFlowCreation.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaPolicySvcVpnId"),
        ("VIPTELA-TRAPS", "viptelaPolicyZonePair"),
        ("VIPTELA-TRAPS", "viptelaPolicySourceVpn"),
        ("VIPTELA-TRAPS", "viptelaPolicySourceIp"),
        ("VIPTELA-TRAPS", "viptelaPolicySourcePort"),
        ("VIPTELA-TRAPS", "viptelaPolicyDestinationVpn"),
        ("VIPTELA-TRAPS", "viptelaPolicyDestinationIp"),
        ("VIPTELA-TRAPS", "viptelaPolicyDestinationPort"),
        ("VIPTELA-TRAPS", "viptelaPolicyProtocol"),
        ("VIPTELA-TRAPS", "viptelaPolicyState"))
)
if mibBuilder.loadTexts:
    viptelaPolicyZbfFlowCreation.setStatus(
        "current"
    )

viptelaPolicyZbfFlowDeletion = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 102)
)
viptelaPolicyZbfFlowDeletion.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaPolicySvcVpnId"),
        ("VIPTELA-TRAPS", "viptelaPolicyZonePair"),
        ("VIPTELA-TRAPS", "viptelaPolicySourceVpn"),
        ("VIPTELA-TRAPS", "viptelaPolicySourceIp"),
        ("VIPTELA-TRAPS", "viptelaPolicySourcePort"),
        ("VIPTELA-TRAPS", "viptelaPolicyDestinationVpn"),
        ("VIPTELA-TRAPS", "viptelaPolicyDestinationIp"),
        ("VIPTELA-TRAPS", "viptelaPolicyDestinationPort"),
        ("VIPTELA-TRAPS", "viptelaPolicyProtocol"),
        ("VIPTELA-TRAPS", "viptelaPolicyState"))
)
if mibBuilder.loadTexts:
    viptelaPolicyZbfFlowDeletion.setStatus(
        "current"
    )

viptelaPolicyZbfFlowTableFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 103)
)
viptelaPolicyZbfFlowTableFull.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaPolicyCurrFlows"),
        ("VIPTELA-TRAPS", "viptelaPolicyHthreshFlows"),
        ("VIPTELA-TRAPS", "viptelaPolicyMaxFlows"))
)
if mibBuilder.loadTexts:
    viptelaPolicyZbfFlowTableFull.setStatus(
        "current"
    )

viptelaPolicyZbfClearFlowTableFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 104)
)
viptelaPolicyZbfClearFlowTableFull.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaPolicyCurrFlows"),
        ("VIPTELA-TRAPS", "viptelaPolicyLthreshFlows"),
        ("VIPTELA-TRAPS", "viptelaPolicyMaxFlows"))
)
if mibBuilder.loadTexts:
    viptelaPolicyZbfClearFlowTableFull.setStatus(
        "current"
    )

viptelaPolicyZbfPktLog = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 105)
)
viptelaPolicyZbfPktLog.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaPolicySvcVpnId"),
        ("VIPTELA-TRAPS", "viptelaPolicyZonePair"),
        ("VIPTELA-TRAPS", "viptelaPolicySourceVpn"),
        ("VIPTELA-TRAPS", "viptelaPolicySourceIp"),
        ("VIPTELA-TRAPS", "viptelaPolicySourcePort"),
        ("VIPTELA-TRAPS", "viptelaPolicyDestinationVpn"),
        ("VIPTELA-TRAPS", "viptelaPolicyDestinationIp"),
        ("VIPTELA-TRAPS", "viptelaPolicyDestinationPort"),
        ("VIPTELA-TRAPS", "viptelaPolicyProtocol"),
        ("VIPTELA-TRAPS", "viptelaPolicyAction"))
)
if mibBuilder.loadTexts:
    viptelaPolicyZbfPktLog.setStatus(
        "current"
    )

viptelaPolicyZbfHalfOpenHit = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 106)
)
viptelaPolicyZbfHalfOpenHit.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaPolicyCurrHalfOpenFlows"),
        ("VIPTELA-TRAPS", "viptelaPolicyHthreshHalfOpenFlows"),
        ("VIPTELA-TRAPS", "viptelaPolicyMaxHalfOpenFlows"))
)
if mibBuilder.loadTexts:
    viptelaPolicyZbfHalfOpenHit.setStatus(
        "current"
    )

viptelaPolicyZbfClearHalfOpenHit = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 107)
)
viptelaPolicyZbfClearHalfOpenHit.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaPolicyCurrHalfOpenFlows"),
        ("VIPTELA-TRAPS", "viptelaPolicyLthreshHalfOpenFlows"),
        ("VIPTELA-TRAPS", "viptelaPolicyMaxHalfOpenFlows"))
)
if mibBuilder.loadTexts:
    viptelaPolicyZbfClearHalfOpenHit.setStatus(
        "current"
    )

viptelaPolicySlaConfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 108)
)
viptelaPolicySlaConfig.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaPolicySlaName"),
        ("VIPTELA-TRAPS", "viptelaPolicySlaOperation"),
        ("VIPTELA-TRAPS", "viptelaPolicySlaLoss"),
        ("VIPTELA-TRAPS", "viptelaPolicySlaLatency"),
        ("VIPTELA-TRAPS", "viptelaPolicySlaJitter"))
)
if mibBuilder.loadTexts:
    viptelaPolicySlaConfig.setStatus(
        "current"
    )

viptelaVpnLastResortStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 109)
)
viptelaVpnLastResortStateChange.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaVpnVpnId"),
        ("VIPTELA-TRAPS", "viptelaVpnIfName"),
        ("VIPTELA-TRAPS", "viptelaVpnNewState"))
)
if mibBuilder.loadTexts:
    viptelaVpnLastResortStateChange.setStatus(
        "current"
    )

viptelaPolicyDevicePolicyAssociationStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 110)
)
viptelaPolicyDevicePolicyAssociationStatus.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaPolicyDevicePolicyName"),
        ("VIPTELA-TRAPS", "viptelaPolicyStatus"))
)
if mibBuilder.loadTexts:
    viptelaPolicyDevicePolicyAssociationStatus.setStatus(
        "current"
    )

viptelaWwanQosStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 111)
)
viptelaWwanQosStateChange.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaWwanIfname"),
        ("VIPTELA-TRAPS", "viptelaWwanQosState"))
)
if mibBuilder.loadTexts:
    viptelaWwanQosStateChange.setStatus(
        "current"
    )

viptelaCdbUnlocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 112)
)
viptelaCdbUnlocked.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaSecurityPersonality"))
)
if mibBuilder.loadTexts:
    viptelaCdbUnlocked.setStatus(
        "current"
    )

viptelaSecuritySecurityUnclaimedVedgeEntryAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 41916, 100, 2, 113)
)
viptelaSecuritySecurityUnclaimedVedgeEntryAdded.setObjects(
      *(("VIPTELA-TRAPS", "eventTime"),
        ("VIPTELA-TRAPS", "netconfNotificationSeverity"),
        ("VIPTELA-TRAPS", "viptelaSecurityUuid"),
        ("VIPTELA-TRAPS", "viptelaSecuritySerial"),
        ("VIPTELA-TRAPS", "viptelaSecuritySubjectSerialNumber"),
        ("VIPTELA-TRAPS", "viptelaSecurityOrganizationName"))
)
if mibBuilder.loadTexts:
    viptelaSecuritySecurityUnclaimedVedgeEntryAdded.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VIPTELA-TRAPS",
    **{"NetconfNotificationSeverity": NetconfNotificationSeverity,
       "DomainId": DomainId,
       "UnsignedByte": UnsignedByte,
       "ColorEnum": ColorEnum,
       "VpnId": VpnId,
       "FailureStateEnum": FailureStateEnum,
       "SensorStateEnum": SensorStateEnum,
       "BoolEnum": BoolEnum,
       "AddressFamilyEnum": AddressFamilyEnum,
       "AfTypeEnum": AfTypeEnum,
       "OperState": OperState,
       "AdminState": AdminState,
       "SiteId": SiteId,
       "BgpState": BgpState,
       "HwSensorTypeEnum": HwSensorTypeEnum,
       "TunnelEnum": TunnelEnum,
       "PersonalityEnumOper": PersonalityEnumOper,
       "Ipv4UcastAddrPrefix": Ipv4UcastAddrPrefix,
       "EncapEnum": EncapEnum,
       "Enumeration": Enumeration,
       "ViptelaIpAddress": ViptelaIpAddress,
       "OspfIfStateEnum": OspfIfStateEnum,
       "OspfStateEnum": OspfStateEnum,
       "StateEnum": StateEnum,
       "PeerState": PeerState,
       "VrrpGroupStateEnum": VrrpGroupStateEnum,
       "InstallationStatus": InstallationStatus,
       "OmpPolicyState": OmpPolicyState,
       "AdminStateEnum": AdminStateEnum,
       "BridgeId": BridgeId,
       "NumMacs": NumMacs,
       "TrafficDirectionEnum": TrafficDirectionEnum,
       "CloudAppEnum": CloudAppEnum,
       "CloudExitEnum": CloudExitEnum,
       "WwanSimStatusEnum": WwanSimStatusEnum,
       "WwanDomainStatusEnum": WwanDomainStatusEnum,
       "WwanRegStatusEnum": WwanRegStatusEnum,
       "WwanBearerEnum": WwanBearerEnum,
       "BfdFlapReasonEnum": BfdFlapReasonEnum,
       "WwanQosStatusEnum": WwanQosStatusEnum,
       "viptela-traps": viptela_traps,
       "fields": fields,
       "eventTime": eventTime,
       "netconfNotificationSeverity": netconfNotificationSeverity,
       "viptelaActionsRebootReason": viptelaActionsRebootReason,
       "viptelaBfdSrcIp": viptelaBfdSrcIp,
       "viptelaBfdDstIp": viptelaBfdDstIp,
       "viptelaBfdProto": viptelaBfdProto,
       "viptelaBfdSrcPort": viptelaBfdSrcPort,
       "viptelaBfdDstPort": viptelaBfdDstPort,
       "viptelaBfdLocalSystemIp": viptelaBfdLocalSystemIp,
       "viptelaBfdLocalColor": viptelaBfdLocalColor,
       "viptelaBfdRemoteSystemIp": viptelaBfdRemoteSystemIp,
       "viptelaBfdRemoteColor": viptelaBfdRemoteColor,
       "viptelaBfdNewState": viptelaBfdNewState,
       "viptelaHardwareNewState": viptelaHardwareNewState,
       "viptelaHardwareHwSensorType": viptelaHardwareHwSensorType,
       "viptelaHardwareHwDevIndex": viptelaHardwareHwDevIndex,
       "viptelaHardwareName": viptelaHardwareName,
       "viptelaHardwareTemp": viptelaHardwareTemp,
       "viptelaHardwareFantrayId": viptelaHardwareFantrayId,
       "viptelaHardwareFanId": viptelaHardwareFanId,
       "viptelaHardwarePemId": viptelaHardwarePemId,
       "viptelaHardwarePimId": viptelaHardwarePimId,
       "viptelaHardwareSfpName": viptelaHardwareSfpName,
       "viptelaHardwareUsbSlot": viptelaHardwareUsbSlot,
       "viptelaOmpNumberOfVsmarts": viptelaOmpNumberOfVsmarts,
       "viptelaOmpNewState": viptelaOmpNewState,
       "viptelaOmpPeer": viptelaOmpPeer,
       "viptelaOmpPeerNewState": viptelaOmpPeerNewState,
       "viptelaOmpOmpAddressFamily": viptelaOmpOmpAddressFamily,
       "viptelaOmpPolicy": viptelaOmpPolicy,
       "viptelaOmpVsmartPeer": viptelaOmpVsmartPeer,
       "viptelaSecurityPeerType": viptelaSecurityPeerType,
       "viptelaSecurityPeerSystemIp": viptelaSecurityPeerSystemIp,
       "viptelaSecurityPublicIp": viptelaSecurityPublicIp,
       "viptelaSecurityPublicPort": viptelaSecurityPublicPort,
       "viptelaSecuritySrcColor": viptelaSecuritySrcColor,
       "viptelaSecurityRemoteColor": viptelaSecurityRemoteColor,
       "viptelaSecurityUptime": viptelaSecurityUptime,
       "viptelaSecurityNewState": viptelaSecurityNewState,
       "viptelaSecurityLocalSystemIp": viptelaSecurityLocalSystemIp,
       "viptelaSecurityLocalColor": viptelaSecurityLocalColor,
       "viptelaSecurityReason": viptelaSecurityReason,
       "viptelaSecurityOldPublicIp": viptelaSecurityOldPublicIp,
       "viptelaSecurityOldPublicPort": viptelaSecurityOldPublicPort,
       "viptelaSecurityNewPublicIp": viptelaSecurityNewPublicIp,
       "viptelaSecurityNewPublicPort": viptelaSecurityNewPublicPort,
       "viptelaSecurityColor": viptelaSecurityColor,
       "viptelaSecurityPersonality": viptelaSecurityPersonality,
       "viptelaSecurityUuid": viptelaSecurityUuid,
       "viptelaSecuritySerial": viptelaSecuritySerial,
       "viptelaSystemProcessName": viptelaSystemProcessName,
       "viptelaSystemProcessId": viptelaSystemProcessId,
       "viptelaSystemReason": viptelaSystemReason,
       "viptelaSystemWarning": viptelaSystemWarning,
       "viptelaSystemTotalMb": viptelaSystemTotalMb,
       "viptelaSystemFreeMb": viptelaSystemFreeMb,
       "viptelaSystemOldSiteId": viptelaSystemOldSiteId,
       "viptelaSystemNewSiteId": viptelaSystemNewSiteId,
       "viptelaSystemOldDomainId": viptelaSystemOldDomainId,
       "viptelaSystemNewDomainId": viptelaSystemNewDomainId,
       "viptelaSystemOldSystemIp": viptelaSystemOldSystemIp,
       "viptelaSystemNewSystemIp": viptelaSystemNewSystemIp,
       "viptelaSystemOldOrganizationName": viptelaSystemOldOrganizationName,
       "viptelaSystemNewOrganizationName": viptelaSystemNewOrganizationName,
       "viptelaSystemUserName": viptelaSystemUserName,
       "viptelaSystemUserId": viptelaSystemUserId,
       "viptelaVpnVpnId": viptelaVpnVpnId,
       "viptelaVpnPeer": viptelaVpnPeer,
       "viptelaVpnBgpNewState": viptelaVpnBgpNewState,
       "viptelaVpnLocalAddress": viptelaVpnLocalAddress,
       "viptelaVpnLocalRouterid": viptelaVpnLocalRouterid,
       "viptelaVpnPeerRouterid": viptelaVpnPeerRouterid,
       "viptelaVpnIfName": viptelaVpnIfName,
       "viptelaVpnNewState": viptelaVpnNewState,
       "viptelaVpnGrpId": viptelaVpnGrpId,
       "viptelaVpnIpPrefix": viptelaVpnIpPrefix,
       "viptelaVpnFailureReason": viptelaVpnFailureReason,
       "viptelaVpnFarEndSystemIp": viptelaVpnFarEndSystemIp,
       "viptelaVpnFarEndColor": viptelaVpnFarEndColor,
       "viptelaVpnClientMac": viptelaVpnClientMac,
       "viptelaVpnIp": viptelaVpnIp,
       "viptelaVpnReason": viptelaVpnReason,
       "viptelaVpnState": viptelaVpnState,
       "viptelaVpnNeighbor": viptelaVpnNeighbor,
       "viptelaVpnPimNewState": viptelaVpnPimNewState,
       "viptelaVpnInterface": viptelaVpnInterface,
       "viptelaVpnTunnelAddress": viptelaVpnTunnelAddress,
       "viptelaVpnRouterId": viptelaVpnRouterId,
       "viptelaVpnOspfNewState": viptelaVpnOspfNewState,
       "viptelaVpnIfAddr": viptelaVpnIfAddr,
       "viptelaVpnOspfInterfaceNewState": viptelaVpnOspfInterfaceNewState,
       "viptelaVpnVrrpGroupState": viptelaVpnVrrpGroupState,
       "viptelaSystemStatusStr": viptelaSystemStatusStr,
       "viptelaAppRouteSrcIp": viptelaAppRouteSrcIp,
       "viptelaAppRouteDstIp": viptelaAppRouteDstIp,
       "viptelaAppRouteProto": viptelaAppRouteProto,
       "viptelaAppRouteSrcPort": viptelaAppRouteSrcPort,
       "viptelaAppRouteDstPort": viptelaAppRouteDstPort,
       "viptelaAppRouteLocalSystemIp": viptelaAppRouteLocalSystemIp,
       "viptelaAppRouteLocalColor": viptelaAppRouteLocalColor,
       "viptelaAppRouteRemoteSystemIp": viptelaAppRouteRemoteSystemIp,
       "viptelaAppRouteRemoteColor": viptelaAppRouteRemoteColor,
       "viptelaAppRouteMeanLoss": viptelaAppRouteMeanLoss,
       "viptelaAppRouteMeanLatency": viptelaAppRouteMeanLatency,
       "viptelaAppRouteSlaClasses": viptelaAppRouteSlaClasses,
       "viptelaActionsStatus": viptelaActionsStatus,
       "viptelaActionsInstallId": viptelaActionsInstallId,
       "viptelaActionsMessage": viptelaActionsMessage,
       "viptelaVpnOperState": viptelaVpnOperState,
       "viptelaVpnAdminState": viptelaVpnAdminState,
       "viptelaVpnAddressFamilyType": viptelaVpnAddressFamilyType,
       "viptelaVpnFibLastUpdateTime": viptelaVpnFibLastUpdateTime,
       "viptelaBridgeId": viptelaBridgeId,
       "viptelaNumMacs": viptelaNumMacs,
       "viptelaPolicyVpnId": viptelaPolicyVpnId,
       "viptelaPolicyApplication": viptelaPolicyApplication,
       "viptelaPolicySourceIp": viptelaPolicySourceIp,
       "viptelaPolicySourcePort": viptelaPolicySourcePort,
       "viptelaPolicyDestinationIp": viptelaPolicyDestinationIp,
       "viptelaPolicyDestinationPort": viptelaPolicyDestinationPort,
       "viptelaPolicyProtocol": viptelaPolicyProtocol,
       "viptelaPolicyDscp": viptelaPolicyDscp,
       "viptelaPolicySlaInformation": viptelaPolicySlaInformation,
       "viptelaPolicySlaStatus": viptelaPolicySlaStatus,
       "viptelaSystemDpiOutOfMemoryState": viptelaSystemDpiOutOfMemoryState,
       "viptelaBfdDeleted": viptelaBfdDeleted,
       "viptelaSecurityGreOldOperState": viptelaSecurityGreOldOperState,
       "viptelaSecurityGreNewOperState": viptelaSecurityGreNewOperState,
       "viptelaSecurityGreIfName": viptelaSecurityGreIfName,
       "viptelaSecurityGreVpnId": viptelaSecurityGreVpnId,
       "viptelaSecurityGreTunnelSource": viptelaSecurityGreTunnelSource,
       "viptelaSecurityGreTunnelDestination": viptelaSecurityGreTunnelDestination,
       "viptelaSecurityGreGreIp": viptelaSecurityGreGreIp,
       "viptelaVpnIfCfgBwKbps": viptelaVpnIfCfgBwKbps,
       "viptelaVpnTrafficDirection": viptelaVpnTrafficDirection,
       "viptelaVpnDuration": viptelaVpnDuration,
       "viptelaAppRouteMeanJitter": viptelaAppRouteMeanJitter,
       "viptelaVpnPimEnabled": viptelaVpnPimEnabled,
       "viptelaSystemRemoteHost": viptelaSystemRemoteHost,
       "viptelaPolicyVpnListName": viptelaPolicyVpnListName,
       "viptelaPolicyName": viptelaPolicyName,
       "viptelaPolicyAccessListName": viptelaPolicyAccessListName,
       "viptelaPolicyStatus": viptelaPolicyStatus,
       "viptelaSecurityVmanageConnectionPreference": viptelaSecurityVmanageConnectionPreference,
       "viptelaHardwareSensorNewState": viptelaHardwareSensorNewState,
       "viptelaCloudExpressApplication": viptelaCloudExpressApplication,
       "viptelaCloudExpressExitType": viptelaCloudExpressExitType,
       "viptelaGatewayIp": viptelaGatewayIp,
       "viptelaAppLatency": viptelaAppLatency,
       "viptelaAppLoss": viptelaAppLoss,
       "viptelaWwanSimSlot": viptelaWwanSimSlot,
       "viptelaWwanSimState": viptelaWwanSimState,
       "viptelaAppRouteOldSlaClasses": viptelaAppRouteOldSlaClasses,
       "viptelaVpnNewAdminState": viptelaVpnNewAdminState,
       "viptelaWwanDomainState": viptelaWwanDomainState,
       "viptelaWwanRegState": viptelaWwanRegState,
       "viptelaWwanBearer": viptelaWwanBearer,
       "viptelaActionsReason": viptelaActionsReason,
       "viptelaWwanIfname": viptelaWwanIfname,
       "viptelaExitLocalColor": viptelaExitLocalColor,
       "viptelaExitRemoteColor": viptelaExitRemoteColor,
       "viptelaSecurityOrganizationName": viptelaSecurityOrganizationName,
       "viptelaSecuritySpOrganizationName": viptelaSecuritySpOrganizationName,
       "viptelaBfdFlapReason": viptelaBfdFlapReason,
       "viptelaSecurityPeerVmanageSystemIp": viptelaSecurityPeerVmanageSystemIp,
       "viptelaPolicySvcVpnId": viptelaPolicySvcVpnId,
       "viptelaPolicyZonePair": viptelaPolicyZonePair,
       "viptelaPolicySourceVpn": viptelaPolicySourceVpn,
       "viptelaPolicyDestinationVpn": viptelaPolicyDestinationVpn,
       "viptelaPolicyState": viptelaPolicyState,
       "viptelaPolicyCurrFlows": viptelaPolicyCurrFlows,
       "viptelaPolicyHthreshFlows": viptelaPolicyHthreshFlows,
       "viptelaPolicyLthreshFlows": viptelaPolicyLthreshFlows,
       "viptelaPolicyMaxFlows": viptelaPolicyMaxFlows,
       "viptelaPolicyAction": viptelaPolicyAction,
       "viptelaPolicyCurrHalfOpenFlows": viptelaPolicyCurrHalfOpenFlows,
       "viptelaPolicyHthreshHalfOpenFlows": viptelaPolicyHthreshHalfOpenFlows,
       "viptelaPolicyMaxHalfOpenFlows": viptelaPolicyMaxHalfOpenFlows,
       "viptelaPolicyLthreshHalfOpenFlows": viptelaPolicyLthreshHalfOpenFlows,
       "viptelaPolicySlaName": viptelaPolicySlaName,
       "viptelaPolicySlaOperation": viptelaPolicySlaOperation,
       "viptelaPolicySlaLoss": viptelaPolicySlaLoss,
       "viptelaPolicySlaLatency": viptelaPolicySlaLatency,
       "viptelaPolicySlaJitter": viptelaPolicySlaJitter,
       "viptelaPolicyDevicePolicyName": viptelaPolicyDevicePolicyName,
       "viptelaWwanQosState": viptelaWwanQosState,
       "viptelaSecuritySubjectSerialNumber": viptelaSecuritySubjectSerialNumber,
       "traps": traps,
       "viptelaActionsSystemSoftwareInstallStatus": viptelaActionsSystemSoftwareInstallStatus,
       "viptelaActionsSystemRebootIssued": viptelaActionsSystemRebootIssued,
       "viptelaActionsSystemRebootComplete": viptelaActionsSystemRebootComplete,
       "viptelaBfdBfdStateChange": viptelaBfdBfdStateChange,
       "viptelaHardwareFlashFault": viptelaHardwareFlashFault,
       "viptelaHardwareEmmcFault": viptelaHardwareEmmcFault,
       "viptelaHardwareSdcardFault": viptelaHardwareSdcardFault,
       "viptelaHardwareTempsensorFault": viptelaHardwareTempsensorFault,
       "viptelaHardwareTempsensorState": viptelaHardwareTempsensorState,
       "viptelaHardwareFanFault": viptelaHardwareFanFault,
       "viptelaHardwareFantrayFault": viptelaHardwareFantrayFault,
       "viptelaHardwarePemFault": viptelaHardwarePemFault,
       "viptelaHardwarePemStateChange": viptelaHardwarePemStateChange,
       "viptelaHardwarePimFault": viptelaHardwarePimFault,
       "viptelaHardwarePimStateChange": viptelaHardwarePimStateChange,
       "viptelaHardwareSfpStateChange": viptelaHardwareSfpStateChange,
       "viptelaHardwareUsbStateChange": viptelaHardwareUsbStateChange,
       "viptelaOmpOmpNumberOfVsmartsChange": viptelaOmpOmpNumberOfVsmartsChange,
       "viptelaOmpOmpStateChange": viptelaOmpOmpStateChange,
       "viptelaOmpOmpPeerStateChange": viptelaOmpOmpPeerStateChange,
       "viptelaOmpOmpTlocStateChange": viptelaOmpOmpTlocStateChange,
       "viptelaOmpOmpPolicy": viptelaOmpOmpPolicy,
       "viptelaSecurityControlConnectionStateChange": viptelaSecurityControlConnectionStateChange,
       "viptelaSecurityControlConnectionAuthFail": viptelaSecurityControlConnectionAuthFail,
       "viptelaSecurityControlVbondStateChange": viptelaSecurityControlVbondStateChange,
       "viptelaSecurityControlConnectionTlocIpChange": viptelaSecurityControlConnectionTlocIpChange,
       "viptelaSecurityControlNoActiveVsmart": viptelaSecurityControlNoActiveVsmart,
       "viptelaSecurityControlNoActiveVbond": viptelaSecurityControlNoActiveVbond,
       "viptelaSecurityTunnelIpsecRekey": viptelaSecurityTunnelIpsecRekey,
       "viptelaSecurityTunnelIpsecManualRekey": viptelaSecurityTunnelIpsecManualRekey,
       "viptelaSecuritySecurityRootCertChainInstalled": viptelaSecuritySecurityRootCertChainInstalled,
       "viptelaSecuritySecurityCertificateInstalled": viptelaSecuritySecurityCertificateInstalled,
       "viptelaSecuritySecurityNewCsrGenerated": viptelaSecuritySecurityNewCsrGenerated,
       "viptelaSecuritySecurityRootCertChainUninstalled": viptelaSecuritySecurityRootCertChainUninstalled,
       "viptelaSecuritySecurityClearInstalledCertificate": viptelaSecuritySecurityClearInstalledCertificate,
       "viptelaSecuritySecurityVedgeSerialFileUploaded": viptelaSecuritySecurityVedgeSerialFileUploaded,
       "viptelaSecuritySecurityVsmartSerialFileUploaded": viptelaSecuritySecurityVsmartSerialFileUploaded,
       "viptelaSecuritySecurityVedgeEntryAdded": viptelaSecuritySecurityVedgeEntryAdded,
       "viptelaSecuritySecurityVedgeEntryRemoved": viptelaSecuritySecurityVedgeEntryRemoved,
       "viptelaSecuritySecurityVsmartEntryAdded": viptelaSecuritySecurityVsmartEntryAdded,
       "viptelaSecuritySecurityVsmartEntryRemoved": viptelaSecuritySecurityVsmartEntryRemoved,
       "viptelaSystemProcessRestart": viptelaSystemProcessRestart,
       "viptelaSystemDiskUsage": viptelaSystemDiskUsage,
       "viptelaSystemMemoryUsage": viptelaSystemMemoryUsage,
       "viptelaSystemAaaAdminPwdChange": viptelaSystemAaaAdminPwdChange,
       "viptelaSystemSiteIdChange": viptelaSystemSiteIdChange,
       "viptelaSystemDomainIdChange": viptelaSystemDomainIdChange,
       "viptelaSystemSystemIpChange": viptelaSystemSystemIpChange,
       "viptelaSystemOrgNameChange": viptelaSystemOrgNameChange,
       "viptelaSystemSystemLoginChange": viptelaSystemSystemLoginChange,
       "viptelaSystemSystemLogoutChange": viptelaSystemSystemLogoutChange,
       "viptelaSystemSystemAaaLoginFail": viptelaSystemSystemAaaLoginFail,
       "viptelaSystemSystemCommit": viptelaSystemSystemCommit,
       "viptelaVpnBgpPeerStateChange": viptelaVpnBgpPeerStateChange,
       "viptelaVpnInterfaceStateChange": viptelaVpnInterfaceStateChange,
       "viptelaVpnVrrpGroupStateChange": viptelaVpnVrrpGroupStateChange,
       "viptelaVpnRouteInstallFail": viptelaVpnRouteInstallFail,
       "viptelaVpnTunnelInstallFail": viptelaVpnTunnelInstallFail,
       "viptelaVpnDhcpAddressAssigned": viptelaVpnDhcpAddressAssigned,
       "viptelaVpnDhcpAddressRenewed": viptelaVpnDhcpAddressRenewed,
       "viptelaVpnDhcpAddressReleased": viptelaVpnDhcpAddressReleased,
       "viptelaVpnDhcpRequestRejected": viptelaVpnDhcpRequestRejected,
       "viptelaVpnDhcpServerStateChange": viptelaVpnDhcpServerStateChange,
       "viptelaVpnPimNeighborStateChange": viptelaVpnPimNeighborStateChange,
       "viptelaVpnPimInterfaceStateChange": viptelaVpnPimInterfaceStateChange,
       "viptelaVpnPimTunnelStateChange": viptelaVpnPimTunnelStateChange,
       "viptelaVpnOspfNeighborStateChange": viptelaVpnOspfNeighborStateChange,
       "viptelaVpnOspfInterfaceStateChange": viptelaVpnOspfInterfaceStateChange,
       "viptelaSystemPseudoCommitStatus": viptelaSystemPseudoCommitStatus,
       "viptelaAppRouteSlaChange": viptelaAppRouteSlaChange,
       "viptelaSecuritySecurityCertificateExpired": viptelaSecuritySecurityCertificateExpired,
       "viptelaVpnFibStateChange": viptelaVpnFibStateChange,
       "viptelaBridgeCreation": viptelaBridgeCreation,
       "viptelaBridgeDeletion": viptelaBridgeDeletion,
       "viptelaBridgeMaxMacReached": viptelaBridgeMaxMacReached,
       "viptelaSecurityControlVedgeListRequest": viptelaSecurityControlVedgeListRequest,
       "viptelaPolicySlaViolation": viptelaPolicySlaViolation,
       "viptelaPolicySlaViolationPktDrop": viptelaPolicySlaViolationPktDrop,
       "viptelaVpnInterfacePcsFaultDetected": viptelaVpnInterfacePcsFaultDetected,
       "viptelaSystemAppDpiFlowsOutOfMemory": viptelaSystemAppDpiFlowsOutOfMemory,
       "viptelaSecurityGreStateUpdate": viptelaSecurityGreStateUpdate,
       "viptelaVpnInterfaceBw": viptelaVpnInterfaceBw,
       "viptelaHardwareSfpSupportState": viptelaHardwareSfpSupportState,
       "viptelaPolicyDataPolicyAssociationStatus": viptelaPolicyDataPolicyAssociationStatus,
       "viptelaPolicyAccessListAssociationStatus": viptelaPolicyAccessListAssociationStatus,
       "viptelaSecurityVmanageConnectionPreferenceChanged": viptelaSecurityVmanageConnectionPreferenceChanged,
       "viptelaVpnCloudExpressMaxLocalExitExceeded": viptelaVpnCloudExpressMaxLocalExitExceeded,
       "viptelaVpnCloudExpressApplicationChange": viptelaVpnCloudExpressApplicationChange,
       "viptelaVpnCloudExpressScoreChange": viptelaVpnCloudExpressScoreChange,
       "viptelaWwanSimStateChange": viptelaWwanSimStateChange,
       "viptelaSystemAppDpiFlowsWriteFailedVedge": viptelaSystemAppDpiFlowsWriteFailedVedge,
       "viptelaVpnInterfaceAdminStateChange": viptelaVpnInterfaceAdminStateChange,
       "viptelaWwanDomainStateChange": viptelaWwanDomainStateChange,
       "viptelaWwanRegStateChange": viptelaWwanRegStateChange,
       "viptelaWwanBearerChange": viptelaWwanBearerChange,
       "viptelaSystemProcessDown": viptelaSystemProcessDown,
       "viptelaActionsSystemRebootAborted": viptelaActionsSystemRebootAborted,
       "viptelaSecurityVbondRejectVedgeConnection": viptelaSecurityVbondRejectVedgeConnection,
       "viptelaSecurityDeviceTemplateMissing": viptelaSecurityDeviceTemplateMissing,
       "viptelaSecurityDeviceTemplateAttachedDuringZtp": viptelaSecurityDeviceTemplateAttachedDuringZtp,
       "viptelaPolicyZbfFlowCreation": viptelaPolicyZbfFlowCreation,
       "viptelaPolicyZbfFlowDeletion": viptelaPolicyZbfFlowDeletion,
       "viptelaPolicyZbfFlowTableFull": viptelaPolicyZbfFlowTableFull,
       "viptelaPolicyZbfClearFlowTableFull": viptelaPolicyZbfClearFlowTableFull,
       "viptelaPolicyZbfPktLog": viptelaPolicyZbfPktLog,
       "viptelaPolicyZbfHalfOpenHit": viptelaPolicyZbfHalfOpenHit,
       "viptelaPolicyZbfClearHalfOpenHit": viptelaPolicyZbfClearHalfOpenHit,
       "viptelaPolicySlaConfig": viptelaPolicySlaConfig,
       "viptelaVpnLastResortStateChange": viptelaVpnLastResortStateChange,
       "viptelaPolicyDevicePolicyAssociationStatus": viptelaPolicyDevicePolicyAssociationStatus,
       "viptelaWwanQosStateChange": viptelaWwanQosStateChange,
       "viptelaCdbUnlocked": viptelaCdbUnlocked,
       "viptelaSecuritySecurityUnclaimedVedgeEntryAdded": viptelaSecuritySecurityUnclaimedVedgeEntryAdded}
)
